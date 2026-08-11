<#
.SYNOPSIS
  公式ドキュメント更新サマリ自動生成パイプラインのラッパー（無人実行用）。

.DESCRIPTION
  Windows タスクスケジューラから起動される想定。専用 bot ブランチ上で
  dl→差分判定→ヘッドレス生成（claude -p）→commit→bot ブランチ限定 push を行う。
  品質ゲートは「人間が bot→main へマージする」段階に置く。
  main へは構造的に push しない（push 先をブランチ名で固縛 + 実行直前に assert）。

.PARAMETER Site
  対象サイト。"all"（既定）/ "claude-code-docs" / "mcp"。

.PARAMETER DryRun
  push のみ抑止する。dl・生成・commit はローカルで実施する（一周の検証用）。

.PARAMETER SkipDownload
  dl_llms.sh をスキップする（既存の取り込み済み状態で生成のみ試すテスト用）。

.PARAMETER RestoreBranch
  終了時に開始前のブランチへ戻す（手動テスト時の利便のため。既定は戻さない）。

.NOTES
  無人実行であることは子プロセスへ --automated 引数で伝え、SKILL の
  Phase 3（第三者レビュー）を必須化する。
#>
[CmdletBinding()]
param(
    [ValidateSet("all", "claude-code-docs", "mcp")]
    [string]$Site = "all",
    [switch]$DryRun,
    [switch]$SkipDownload,
    [switch]$RestoreBranch
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

# 共通基盤（共有定数 $BOT_BRANCH/$BASE_BRANCH/$TOKEN_FILE・コンソール UTF-8 設定・
# Write-Log・Invoke-Git・Invoke-BotPush）を dot-source で取り込む。ja 追従 watch bot
# （run-ja-follow-watch.ps1）と同一実装を共有し、特にセキュリティ上慎重な push の
# 二重保守による drift を防ぐ。
. (Join-Path $PSScriptRoot "doc-summary-common.ps1")

# --- 定数（本 bot 固有）-----------------------------------------------------
$REPO_ROOT   = (Resolve-Path (Join-Path $PSScriptRoot "..\..")).Path
$LOG_DIR     = Join-Path $REPO_ROOT "work\doc-summary-bot"
$GEN_MODEL   = "opus"               # ヘッドレス生成のモデル（レビューは agent 定義で sonnet 固定）

# claude が SKILL 実行で使うツール群（acceptEdits と二重で明示）。
# 注: これらは「単純コマンド」のみ許可する。claude が複合コマンド
# （例 `cd X && git mv A B`、`f=...; for ...; awk ...`）で呼ぶと先頭トークンが
# パターンに一致せず拒否される。SKILL 側で補助計算・退避を単純コマンドに
# 分解させる必要がある（2026-06-07 の自動実行で git mv/python3/node/awk が
# 複合形で permission_denied になった。ただし claude は代替手段で完走した）。
$ALLOWED_TOOLS = "Read Write Edit Grep Bash(git diff:*) Bash(git log:*) Bash(git show:*) Bash(git rev-parse:*) Bash(mkdir -p:*) Bash(mv:*) Bash(git mv:*) Bash(git checkout:*) Bash(git clean:*) Bash(python:*) Bash(python3:*) Bash(node:*) Bash(awk:*) Bash(echo:*) Task Agent(doc-summary-reviewer)"

# サイト設定（SKILL.md サイト設定テーブルと一致させる）
$SITES = @(
    [pscustomobject]@{ Slug = "claude-code-docs"; Input = "official-llms-txts/code.claude.com/docs/"; Detail = "official-doc-update-summary/claude-code-docs/latest-detail.md" }
    [pscustomobject]@{ Slug = "mcp";              Input = "official-llms-txts/modelcontextprotocol.io/"; Detail = "official-doc-update-summary/mcp/latest-detail.md" }
)

# --- ログ -------------------------------------------------------------------
New-Item -ItemType Directory -Force -Path $LOG_DIR | Out-Null
$LOG_FILE = Join-Path $LOG_DIR ("run-{0}.log" -f (Get-Date -Format "yyyyMMdd-HHmmss"))

# bash を解決する。Git for Windows 同梱の bash を最優先し、無ければ PATH を見る
# （タスクスケジューラ実行時は PATH に Git の bin が通っていない構成があり得るため）。
# 注: PATH 先頭の `bash` は WindowsApps の WSL 実行エイリアスに解決されることがあり、
# ディストリ未導入だと即 exit 1 になる（2026-07-20 以降の毎日 FAILURE の原因）。
# よって PATH 由来の候補からは WindowsApps 配下を除外する。
function Resolve-BashExe {
    $g = Get-Command git -ErrorAction SilentlyContinue
    if ($g) {
        $gitRoot = Split-Path (Split-Path $g.Source -Parent) -Parent
        foreach ($rel in @("bin\bash.exe", "usr\bin\bash.exe")) {
            $p = Join-Path $gitRoot $rel
            if (Test-Path $p) { return $p }
        }
    }
    $c = @(Get-Command bash -All -ErrorAction SilentlyContinue |
        Where-Object { $_.Source -and $_.Source -notmatch '\\WindowsApps\\' }) | Select-Object -First 1
    if ($c) { return $c.Source }
    throw "bash が見つからない（Git for Windows 同梱位置にも PATH にも無い。PATH 上の WSL エイリアスは除外対象）。Git for Windows を導入するか PATH を通すこと"
}

# 詳細版が「最後まで書き終わった形」かを判定する。SKILL は詳細版の末尾に
# base_commit / head_commit / generated_at_full を持つ HTML コメントのフッタを書くため、
# その有無で「途中書き」と「書き終わり」を切り分けられる。
# 注意: このフッタは SKILL 手順 11（詳細版書き出し）で入る。手順 13 の Phase 3
# 第三者レビューはその後なので、**フッタがあってもレビュー済みとは限らない**。
# 判定は固定行数ではなく正規表現で行う（行数固定だと末尾に空行が 1 つ増えただけで
# 完成品を未完成と誤判定し、実データを破棄してしまうため）。
function Test-SummaryComplete {
    param([string]$DetailPath)
    if (-not (Test-Path $DetailPath)) { return $false }
    $tail = (@(Get-Content $DetailPath -Tail 20) -join "`n")
    return ($tail -match '(?s)<!--.*?head_commit:\s*[0-9a-f]{7,}.*?generated_at_full:\s*\S+.*?-->')
}

# 指定パス配下を HEAD の状態へ戻す。`git checkout -- <path>` だけでは index から
# 復元されるため、手順 6 の `git add` 直後に kill された場合の staged 残留が
# 生き残ってしまう。先に reset で index を HEAD に揃えてから復元する
# （ja 追従 bot が registry churn を捨てるときと同じ手順）。
# 未追跡の途中生成物も消えるので、消す前に対象を必ずログへ残す。
function Reset-BotPath {
    param([string]$PathSpec)
    foreach ($d in @(& git clean -nd $PathSpec 2>$null)) { Write-Log "  $d" "WARN" }
    & git reset -q $PathSpec 2>$null | Out-Null
    & git checkout HEAD -- $PathSpec 2>$null | Out-Null
    & git clean -fdq $PathSpec 2>$null | Out-Null
}

# 例外を握り潰して続行するためのラッパ。手順 1 は「絶対に throw しない」ことを最優先する
# ため、個々の回復操作はすべてこれで包む。
function Invoke-Safely {
    param([string]$What, [scriptblock]$Body)
    try { & $Body } catch { Write-Log "$What に失敗したが続行する: $($_.Exception.Message)" "WARN" }
}

# 中断した merge / rebase / cherry-pick / revert を片付ける。放置するとブランチ切替も
# commit もできず、以後の実行が丸ごと止まる。
function Clear-InProgressGitOperation {
    $gitDir = (& git rev-parse --git-dir 2>$null)
    if (-not $gitDir) { return }
    $gitDir = $gitDir.Trim()
    $ops = @(
        @{ Marker = "MERGE_HEAD";       Args = @("merge", "--abort") }
        @{ Marker = "CHERRY_PICK_HEAD"; Args = @("cherry-pick", "--abort") }
        @{ Marker = "REVERT_HEAD";      Args = @("revert", "--abort") }
        @{ Marker = "rebase-merge";     Args = @("rebase", "--abort") }
        @{ Marker = "rebase-apply";     Args = @("rebase", "--abort") }
    )
    foreach ($op in $ops) {
        if (Test-Path (Join-Path $gitDir $op.Marker)) {
            Write-Log "中断状態 $($op.Marker) を検出。git $($op.Args -join ' ') する" "WARN"
            & git @($op.Args) 2>$null | Out-Null
        }
    }
}

# tracked の未コミット変更をパス配列で返す。
# core.quotePath=false で非 ASCII パスが C エスケープ（\346\227\245...）されるのを防ぐ。
# 空白を含むパスは引用符で囲まれるので、それは剥がす。rename は移動元・移動先の両方を
# 返す（移動元が bot 所有外なら人の作業とみなすため）。
function Get-DirtyPath {
    $dirty = @(& git -c core.quotePath=false status --porcelain --untracked-files=no)
    return @($dirty | ForEach-Object {
        $p = $_.Substring(3)
        if ($p -match ' -> ') { ($p -split ' -> ') | ForEach-Object { $_.Trim('"') } }
        else { $p.Trim('"') }
    })
}

# bot が所有するのは「取り込み原文」と「各サイトの成果物ディレクトリ」だけ。
# official-doc-update-summary/README.md のような人手管理ファイルは所有外として扱う。
function Get-BotOwnedPath {
    return @("official-llms-txts") + @($SITES | ForEach-Object { ((Split-Path $_.Detail -Parent) -replace '\\', '/') })
}

# 中断残留（前回実行が commit 前に落ちて残した生成物）を回収する。bot ブランチ上でのみ動く。
function Invoke-ResidueRecovery {
    $paths = @(Get-DirtyPath)
    if ($paths.Count -eq 0) { return }
    $cur = (& git rev-parse --abbrev-ref HEAD).Trim()
    if ($cur -ne $BOT_BRANCH) {
        Write-Log "現在のブランチが $cur のため中断残留の回収は行わない" "WARN"
        return
    }
    Write-Log "未コミットの残留を検出。前回実行の中断残留とみなして回収する" "WARN"

    # サイトごとに救出/破棄を決める。判定材料は「詳細版そのものが dirty か」に限る。
    # 同じディレクトリ配下の watch/registry.json（ja 追従 bot が毎回書き換える）や
    # archives/ が dirty なだけで完成品と誤判定しないため。それらは .md から再導出
    # できるので破棄してよい。
    $rescued = @()
    foreach ($s in $SITES) {
        $siteDir = (Split-Path $s.Detail -Parent) -replace '\\', '/'
        if (@($paths | Where-Object { $_.StartsWith("$siteDir/") }).Count -eq 0) { continue }
        $detail = $s.Detail -replace '\\', '/'
        if (@($paths | Where-Object { $_ -eq $detail }).Count -eq 0) {
            Write-Log "[$($s.Slug)] 詳細版以外の残留のみ。破棄する" "WARN"
            Reset-BotPath $siteDir
        } elseif (Test-SummaryComplete $s.Detail) {
            # フッタまで書けていても Phase 3（第三者レビュー）通過は保証されない。
            # bot ブランチは人間が main へマージする前段なので、破棄せず残したうえで
            # 未確認である旨をログとコミットメッセージに明示する。
            Write-Log "[$($s.Slug)] 残留生成物は末尾まで書けている。救出する（Phase 3 通過は未確認）"
            $rescued += $s.Slug
        } else {
            Write-Log "[$($s.Slug)] 詳細版が途中書き（フッタ欠落）。破棄する" "WARN"
            Reset-BotPath $siteDir
        }
    }

    if ($rescued.Count -gt 0) {
        foreach ($slug in $rescued) {
            $s = @($SITES | Where-Object { $_.Slug -eq $slug })[0]
            Invoke-Git add ((Split-Path $s.Detail -Parent) -replace '\\', '/') | Out-Null
        }
        & git diff --cached --quiet | Out-Null
        if ($LASTEXITCODE -ne 0) {
            Invoke-Git commit -m "feat(official-docs): 公式ドキュ更新サマリ自動生成 (bot・中断分の遅延コミット/Phase 3 未確認: $($rescued -join ', '))" | Out-Null
            Write-Log "残留生成物を救出コミット ($($rescued -join ', '))"
        }
    }

    # 取り込み原文の残留は破棄する。直後の手順 3 で同じファイルを上書き DL するため
    # 実質の損失は無く、残したままだと手順 2 の merge が拒否されうる。
    if (@($paths | Where-Object { $_.StartsWith("official-llms-txts/") }).Count -gt 0) {
        if ($SkipDownload) {
            Write-Log "取り込み原文が dirty だが -SkipDownload のため破棄しない" "WARN"
        } else {
            Write-Log "取り込み原文の残留を破棄（手順 3 で再 DL される）" "WARN"
            Reset-BotPath "official-llms-txts"
        }
    }

}

# 手順 1: 取り込み（手順 3）へ確実に到達するための整地。ブランチ準備もここに含む。
#
# **この関数は throw しない。** 要約生成は失敗しても翌日以降に作り直せるが、llms.txt の
# 日次取り込みだけは取り逃すと二度と再現できない（`download_list.tsv` の URL は履歴を
# 持たない live URL で、その日の断面はその日にしか取れない）。したがって「多少の不整合は
# 握り潰してでも dl まで進む」ことを最優先し、回復できない事象は WARN としてログに残す。
#
# 実害の記録: 2026-07-29 の実行が ExecutionTimeLimit 超過で kill され生成物が未コミットで
# 残った結果、従来の即 throw 型の前提チェックによって以後 4 日間 dl まで到達せず、
# 4 日分のスナップショットを恒久的に失った。
function Initialize-TreeForDownload {
    # 非 throw の保証をホスト設定に依存させない。PowerShell 7.4 以降は
    # $PSNativeCommandUseErrorActionPreference が $true だと EAP='Stop' の下で
    # native コマンドの非ゼロ終了が終端エラーになる。git は「ブランチが無い」等を
    # 正常な非ゼロで返すため、この区間だけ両方を無効化して $LASTEXITCODE で判断する。
    $prevEAP    = $ErrorActionPreference
    $prevNative = $PSNativeCommandUseErrorActionPreference
    $ErrorActionPreference = 'Continue'
    $PSNativeCommandUseErrorActionPreference = $false
    try {
        Initialize-TreeForDownloadCore
    } catch {
        # ここへ来るのは想定外だが、それでも dl は諦めない
        Write-Log "整地中に想定外の例外（続行して取り込みへ進む）: $($_.Exception.Message)" "WARN"
    } finally {
        $ErrorActionPreference = $prevEAP
        $PSNativeCommandUseErrorActionPreference = $prevNative
    }
}

function Initialize-TreeForDownloadCore {
    Invoke-Safely "中断状態の解消" { Clear-InProgressGitOperation }

    # bot 所有外の変更は捨てずに stash へ退避する（人の作業中に bot が走っても壊さない）。
    Invoke-Safely "bot 所有外の変更の退避" {
        $owned = Get-BotOwnedPath
        $foreign = @(Get-DirtyPath | Where-Object { $x = $_; -not @($owned | Where-Object { $x.StartsWith("$_/") }) })
        if ($foreign.Count -gt 0) {
            Write-Log "bot 所有外の未コミット変更を検出。stash へ退避する（git stash list で復元可能）:`n$($foreign -join "`n")" "WARN"
            $stashMsg = "doc-summary bot 退避 {0}" -f (Get-Date -Format "yyyy-MM-dd HH:mm:ss")
            & git stash push -m $stashMsg -- @foreign 2>&1 | Out-Null
        }
    }

    # bot ブランチへ移る。残留が邪魔で切り替えられない場合は残留を捨ててから再試行する。
    Invoke-Safely "bot ブランチの準備" {
        & git rev-parse --verify --quiet "refs/heads/$BOT_BRANCH" 2>$null | Out-Null
        if ($LASTEXITCODE -ne 0) {
            Write-Log "bot ブランチを $BASE_BRANCH から新規作成"
            & git checkout -b $BOT_BRANCH $BASE_BRANCH 2>&1 | Out-Null
            return
        }
        if ((& git rev-parse --abbrev-ref HEAD).Trim() -eq $BOT_BRANCH) { return }
        & git checkout $BOT_BRANCH 2>&1 | Out-Null
        if ($LASTEXITCODE -ne 0) {
            Write-Log "bot ブランチへの切替に失敗。bot 所有パスの残留を捨てて再試行する" "WARN"
            foreach ($p in (Get-BotOwnedPath)) { Reset-BotPath $p }
            & git checkout $BOT_BRANCH 2>&1 | Out-Null
        }
    }

    Invoke-Safely "中断残留の回収" { Invoke-ResidueRecovery }

    # main の取り込み。コンフリクトしても dl 自体は続行できるので、abort して先へ進む
    # （取り込めなかった分は翌日以降の実行で入る）。
    Invoke-Safely "$BASE_BRANCH の取り込み" {
        if ((& git rev-parse --abbrev-ref HEAD).Trim() -ne $BOT_BRANCH) { return }
        & git merge --no-edit $BASE_BRANCH 2>&1 | Out-Null
        if ($LASTEXITCODE -ne 0) {
            Write-Log "$BASE_BRANCH の取り込みに失敗。abort して取り込まずに続行する" "WARN"
            & git merge --abort 2>$null | Out-Null
        } else {
            Write-Log "bot ブランチへ $BASE_BRANCH を取り込み"
        }
    }

    # 最終手段: それでも bot 所有パスが dirty なら HEAD の状態へ強制的に戻す。
    # 捨てるのは bot 所有パスだけで、退避済みの人の作業には触れない。
    Invoke-Safely "最終クリーンアップ" {
        if (@(Get-DirtyPath).Count -eq 0) { return }
        Write-Log "回収後も未コミット変更が残存。bot 所有パスを HEAD の状態へ戻す" "WARN"
        foreach ($p in (Get-BotOwnedPath)) {
            if ($SkipDownload -and $p -eq "official-llms-txts") { continue }
            Reset-BotPath $p
        }
    }

    $left = @(Get-DirtyPath)
    if ($left.Count -gt 0) {
        # ここまで来ても残るなら諦めて進む。手順 4 の commit は official-llms-txts だけを
        # 対象にするため、残留があっても取り込みコミット自体は成立する。
        Write-Log "未コミット変更が残ったまま取り込みへ進む:`n$($left -join "`n")" "WARN"
    }
}

# --- メイン -----------------------------------------------------------------
Set-Location $REPO_ROOT
Write-Log "=== run-doc-summary 開始 (Site=$Site DryRun=$DryRun SkipDownload=$SkipDownload) ==="

$startBranch = (& git rev-parse --abbrev-ref HEAD).Trim()
$hadFailure  = $false
$pushAborted = $false

try {
    # 1-2. 整地とブランチ準備。**ここは throw しない**（手順 3 の dl へ必ず到達させる）。
    #      中断残留・中断した merge・人の作業・ブランチのずれは、この中で退避 / 回収 /
    #      HEAD への巻き戻しによって解消し、解消しきれなくても WARN を残して先へ進む。
    Initialize-TreeForDownload

    # 3. dl_llms.sh（公式 llms.txt 取り込み）
    if (-not $SkipDownload) {
        Write-Log "dl_llms.sh 実行"
        $bashExe = Resolve-BashExe
        & $bashExe ".claude/scripts/dl_llms.sh" 2>&1 | Tee-Object -FilePath $LOG_FILE -Append | Out-Null
        if ($LASTEXITCODE -ne 0) { throw "dl_llms.sh が失敗 (exit $LASTEXITCODE)" }
    } else {
        Write-Log "dl_llms.sh はスキップ (-SkipDownload)"
    }

    # 4. dl 差分を commit（取り込みと生成のコミットを分離）
    #    手順 1-2 は throw しないため、bot ブランチへ移れていない可能性がここで残る。
    #    その状態で commit すると別ブランチを汚すので、ここでだけは明示的に止める。
    $cur = (& git rev-parse --abbrev-ref HEAD).Trim()
    if ($cur -ne $BOT_BRANCH) {
        throw "bot ブランチへ切り替えられていないため取り込みを commit できません（現在: $cur）。DL 済みファイルは作業ツリーに残っています"
    }
    Invoke-Git add "official-llms-txts" | Out-Null
    & git diff --cached --quiet "official-llms-txts" | Out-Null; $dlChanged = ($LASTEXITCODE -ne 0)
    if ($dlChanged) {
        Invoke-Git commit -m "chore(official-docs): 公式 llms.txt 定期取り込み (bot)" | Out-Null
        Write-Log "dl 差分を commit"
    } else {
        Write-Log "dl 差分なし"
    }

    # 4.5 取り込みだけ先に push する。手順 5 の生成は 30 分以上かかることがあり、そこで
    #     落ちるとその日のスナップショットがローカルにしか無い状態が続く。llms.txt は
    #     履歴を持たない live URL が相手なので、ローカルを失えばその日の断面は二度と
    #     再現できない。よって生成の成否を待たずにリモートへ逃がす。
    #     push に失敗しても手順 7 で再度 push されるため、ここでは実行を止めない。
    if ($dlChanged) {
        if ($DryRun) {
            Write-Log "DryRun: 取り込みの先行 push を抑止"
        } else {
            Invoke-Safely "取り込みの先行 push" {
                $curForPush = (& git rev-parse --abbrev-ref HEAD).Trim()
                if ($curForPush -ne $BOT_BRANCH) {
                    throw "想定外ブランチ '$curForPush' での push を中止（期待: $BOT_BRANCH）"
                }
                Write-Log "取り込みを先行 push: origin $BOT_BRANCH (inline credential helper)"
                Invoke-BotPush $BOT_BRANCH | Out-Null
                Write-Log "先行 push 完了"
            }
        }
    }

    $headCommit = (& git rev-parse HEAD).Trim()

    # 5. 対象サイトを生成
    $targets = if ($Site -eq "all") { $SITES } else { $SITES | Where-Object { $_.Slug -eq $Site } }
    foreach ($s in $targets) {
        # BASE_COMMIT は前回サマリのフッタ head_commit
        if (-not (Test-Path $s.Detail)) {
            Write-Log "[$($s.Slug)] latest-detail.md 不在。初版は手動 --from 指定が必要のためスキップ" "WARN"
            continue
        }
        $m = Select-String -Path $s.Detail -Pattern 'head_commit:\s*([0-9a-f]+)' | Select-Object -First 1
        if (-not $m) { Write-Log "[$($s.Slug)] head_commit 抽出失敗、スキップ" "WARN"; continue }
        $baseCommit = $m.Matches[0].Groups[1].Value

        # 終了コードを必ず見る。フッタの head_commit が到達不能（履歴書き換え・再 clone・
        # 未参照オブジェクトの GC）になると git diff は stderr に fatal を出して exit 128 で
        # 終わり stdout は空になる。exit を見ないと「原文差分なし」と誤判定し、そのサイトが
        # 以後ずっと無言でスキップされ続ける（ログにも残らず SUCCESS で終わる）。
        $diffRaw = & git diff $baseCommit $headCommit -- $s.Input 2>&1
        $diffExit = $LASTEXITCODE
        if ($diffExit -ne 0) {
            Write-Log "[$($s.Slug)] git diff が失敗 (exit $diffExit)。base=$baseCommit が到達不能の可能性" "ERROR"
            Write-Log (@($diffRaw | ForEach-Object { $_.ToString() }) -join "`n") "ERROR"
            $hadFailure = $true
            continue
        }
        # 2>&1 で混ざる stderr は ErrorRecord として来る。差分の有無は stdout だけで判定し、
        # git が成功時に出す警告を「差分あり」と誤読しないようにする。
        $diff = @($diffRaw | Where-Object { $_ -isnot [System.Management.Automation.ErrorRecord] })
        if (-not $diff) {
            Write-Log "[$($s.Slug)] 原文差分なし、生成スキップ"
            continue
        }

        Write-Log "[$($s.Slug)] 差分あり。ヘッドレス生成を開始 ($baseCommit..$($headCommit.Substring(0,7)))"
        # 無人実行であることは --automated 引数で SKILL へ確実に伝える。
        # （環境変数 + Bash echo 経由の検知はモデルが命令形を改変し allowedTools 不一致で
        #   拒否され、Phase 3 がスキップされ得るため。引数はプロンプト内で権限不要に読める）
        $raw = & claude -p "/update-official-doc-summary --site $($s.Slug) --automated" `
            --model $GEN_MODEL `
            --permission-mode acceptEdits `
            --allowedTools $ALLOWED_TOOLS `
            --output-format json 2>&1
        $cliExit = $LASTEXITCODE

        # 終了コード + result JSON の is_error を二重判定。stdout 末尾の result 行
        # （"type":"result" を含む）だけを取り出して解釈し、2>&1 で混入する stderr 警告
        # （"no stdin data received" 等）が JSON parse を壊すのを防ぐ。
        $isError = $true
        $jsonLine = @($raw | ForEach-Object { $_.ToString() } | Where-Object { $_ -match '"type":"result"' }) | Select-Object -Last 1
        if ($jsonLine) {
            try { $isError = [bool]($jsonLine | ConvertFrom-Json).is_error } catch { $isError = $true }
        }
        if ($cliExit -ne 0 -or $isError) {
            Write-Log "[$($s.Slug)] 生成失敗 (exit=$cliExit is_error=$isError)。当該サイトの生成物を破棄し push 抑止" "ERROR"
            Write-Log $raw "ERROR"
            # 失敗サイトの生成途中物をロールバック（他サイト・dl commit は保持）。
            # Reset-BotPath を使う。単なる `git checkout -- <dir>` は index から復元するため、
            # SKILL が自分でステージした内容（$ALLOWED_TOOLS に Bash(git mv:*) があり、
            # git mv は add 不要でステージする）が生き残り、手順 6 が成功メッセージのまま
            # コミットしてしまう。Reset-BotPath は reset → checkout HEAD → clean の順で
            # index ごと戻すので、ステージ済みの生成物も確実に破棄される。
            Reset-BotPath ((Split-Path $s.Detail -Parent) -replace '\\', '/')
            $hadFailure = $true
        } else {
            Write-Log "[$($s.Slug)] 生成成功 (Phase 3 含む)"
        }
    }

    # 5.5 生成中の scratch を除去（決定論ガード）。ヘッドレス claude が差分照合等で
    #     official-llms-txts 配下へ一時ファイル（例: Windows パスを bash リダイレクトに
    #     渡して名前が潰れた `C:cc-workspace...tmp-llms-full-*.txt`）を残すことがある。
    #     dl 済みの正規ファイルは手順 4 で既に追跡・コミット済みのため、ここで
    #     official-llms-txts 配下の未追跡物を消しても実害はなく、scratch のみ除去される。
    #     これを怠ると次回 dl の `git add official-llms-txts`（手順 4）で誤コミットされる。
    & git clean -fd "official-llms-txts" 2>$null | Out-Null

    # 6. 生成物を commit
    $summaryDir = "official-doc-update-summary"
    Invoke-Git add $summaryDir | Out-Null
    & git diff --cached --quiet $summaryDir | Out-Null; $genChanged = ($LASTEXITCODE -ne 0)
    if ($genChanged) {
        Invoke-Git commit -m "feat(official-docs): 公式ドキュ更新サマリ自動生成 (bot)" | Out-Null
        Write-Log "生成サマリを commit"
    } else {
        Write-Log "生成サマリの差分なし"
    }

    # 7. push（bot ブランチ限定・二重防御）
    if ($DryRun) {
        Write-Log "DryRun: push を抑止"
        $pushAborted = $true
    } elseif ($hadFailure) {
        Write-Log "生成失敗ありのため push を抑止（未確定生成が bot ローカルに残存）" "WARN"
        $pushAborted = $true
    } else {
        $cur = (& git rev-parse --abbrev-ref HEAD).Trim()
        if ($cur -ne $BOT_BRANCH) {
            throw "想定外ブランチ '$cur' での push を中止（期待: $BOT_BRANCH）"
        }
        Write-Log "bot ブランチへ push: origin $BOT_BRANCH (inline credential helper)"
        Invoke-BotPush $BOT_BRANCH | Out-Null
        Write-Log "push 完了"
    }
}
catch {
    Write-Log $_.Exception.Message "ERROR"
    $hadFailure = $true
}
finally {
    if ($RestoreBranch -and $startBranch) {
        try { Invoke-Git checkout $startBranch | Out-Null; Write-Log "開始ブランチ $startBranch へ復帰" } catch { Write-Log "ブランチ復帰失敗: $($_.Exception.Message)" "WARN" }
    }
    $status = if ($hadFailure) { "FAILURE" } else { "SUCCESS" }
    Write-Log "=== run-doc-summary 終了: $status (pushAborted=$pushAborted) ==="
}

if ($hadFailure) { exit 1 } else { exit 0 }
