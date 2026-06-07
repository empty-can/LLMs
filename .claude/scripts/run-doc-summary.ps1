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

# claude -p の JSON 出力（日本語を含む）を UTF-8 で受ける。既定のコンソール
# コードページ（CP932 等）で外部プロセス出力をデコードすると日本語が文字化けし、
# result JSON の ConvertFrom-Json が壊れて is_error を誤判定する（生成成功でも
# 失敗扱いになり生成物が破棄される）。実害として 2026-06-07 の自動実行が
# Phase 3 PASS 済みの生成物を破棄し FAILURE 終了した。
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$OutputEncoding = [System.Text.Encoding]::UTF8

# --- 定数 -------------------------------------------------------------------
$BOT_BRANCH  = "bot/doc-summary"
$BASE_BRANCH = "main"
$REPO_ROOT   = (Resolve-Path (Join-Path $PSScriptRoot "..\..")).Path
$LOG_DIR     = Join-Path $REPO_ROOT "work\doc-summary-bot"
$GEN_MODEL   = "opus"               # ヘッドレス生成のモデル（レビューは agent 定義で sonnet 固定）
# bot push 用 PAT を DPAPI 暗号化して保管するファイル（同一ユーザー・同一マシンでのみ復号可）。
# 初回セットアップ: Read-Host -AsSecureString | Export-Clixml $TOKEN_FILE
$TOKEN_FILE  = Join-Path $env:USERPROFILE ".claude\doc-summary-bot-token.xml"
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

function Write-Log {
    param([string]$Message, [string]$Level = "INFO")
    $line = "{0} [{1}] {2}" -f (Get-Date -Format "yyyy-MM-dd HH:mm:ss"), $Level, $Message
    $line | Tee-Object -FilePath $LOG_FILE -Append
}

# git をラップし、失敗時に例外化（$LASTEXITCODE を確実に判定）。
# git は正常時も "Switched to branch" / "Already up to date." 等を stderr に書く。
# 呼び出し側セッションが $ErrorActionPreference='Stop'（本スクリプト既定）や、
# PowerShell 7.4 既定の $PSNativeCommandUseErrorActionPreference=$true の下では、
# この正常 stderr が終端エラー化し、成功した checkout/merge まで FAILURE 扱いになる
# （実害: 対話 pwsh での手動実行が bot 切替直後に "Switched to branch" で異常終了）。
# 対策は 2 点。(1) 関数内だけ EAP を Continue に下げ、成否は $LASTEXITCODE のみで判定。
# (2) stderr を含む出力は ErrorRecord のまま返すと呼び出し側のパイプ（| Out-Null）で
# エラーストリームへ再放出され得るため、文字列化して返す。
function Invoke-Git {
    param([Parameter(ValueFromRemainingArguments = $true)][string[]]$GitArgs)
    $prevEAP = $ErrorActionPreference
    $ErrorActionPreference = 'Continue'
    try {
        $out = & git @GitArgs 2>&1
        $code = $LASTEXITCODE
    } finally {
        $ErrorActionPreference = $prevEAP
    }
    if ($code -ne 0) {
        throw "git $($GitArgs -join ' ') が失敗 (exit $code): $($out -join "`n")"
    }
    return ($out | ForEach-Object { $_.ToString() })
}

# bash を解決する。PATH に無ければ Git for Windows 同梱の bash を探す
# （タスクスケジューラ実行時は PATH に Git の bin が通っていない構成があり得るため）。
function Resolve-BashExe {
    $c = Get-Command bash -ErrorAction SilentlyContinue
    if ($c) { return $c.Source }
    $g = Get-Command git -ErrorAction SilentlyContinue
    if ($g) {
        $gitRoot = Split-Path (Split-Path $g.Source -Parent) -Parent
        foreach ($rel in @("bin\bash.exe", "usr\bin\bash.exe")) {
            $p = Join-Path $gitRoot $rel
            if (Test-Path $p) { return $p }
        }
    }
    throw "bash が見つからない（PATH にも Git for Windows 同梱位置にも無い）。Git for Windows を導入するか PATH を通すこと"
}

# bot ブランチ限定 push。GCM を一時無効化し、User scope の PAT を inline
# credential helper 経由でその push 1 回だけ git に渡す（URL/引数/ログに露出させない）。
# 無人実行で GCM の GUI プロンプトが出ないため確実に非対話で push できる。
function Invoke-BotPush {
    param([string]$Branch)
    if (-not (Test-Path $TOKEN_FILE)) {
        throw "トークンファイル $TOKEN_FILE が無い。初回セットアップ (Export-Clixml) を実施してください"
    }
    # DPAPI 復号（同一 Windows ユーザー・同一マシンでのみ成功する）
    try {
        $sec = Import-Clixml $TOKEN_FILE
        $token = (New-Object System.Management.Automation.PSCredential("x-access-token", $sec)).GetNetworkCredential().Password
    } catch {
        throw "トークン復号に失敗（別ユーザー/別マシンでは復号不可）: $($_.Exception.Message)"
    }
    if ([string]::IsNullOrEmpty($token)) { throw "復号したトークンが空です" }
    # sh 関数が展開する変数。PowerShell ではなく git の子 sh が参照する
    $env:GH_PUSH_TOKEN = $token
    # push も正常時に進捗・"To <url>" 等を stderr に書くため、Invoke-Git と同じく
    # 関数内だけ EAP を Continue に下げ、成否は $LASTEXITCODE で判定し、出力は文字列化して返す。
    $prevEAP = $ErrorActionPreference
    $ErrorActionPreference = 'Continue'
    try {
        $helper = '!f() { echo username=x-access-token; echo "password=$GH_PUSH_TOKEN"; }; f'
        $out = & git -c credential.helper= -c "credential.helper=$helper" push origin $Branch 2>&1
        $code = $LASTEXITCODE
        if ($code -ne 0) { throw "push 失敗 (exit $code): $($out -join "`n")" }
        return ($out | ForEach-Object { $_.ToString() })
    } finally {
        Remove-Item Env:\GH_PUSH_TOKEN -ErrorAction SilentlyContinue
        $ErrorActionPreference = $prevEAP
    }
}

# --- メイン -----------------------------------------------------------------
Set-Location $REPO_ROOT
Write-Log "=== run-doc-summary 開始 (Site=$Site DryRun=$DryRun SkipDownload=$SkipDownload) ==="

$startBranch = (& git rev-parse --abbrev-ref HEAD).Trim()
$hadFailure  = $false
$pushAborted = $false

try {
    # 1. 前提: tracked の未コミット変更が無いこと（untracked は無視）
    $dirty = & git status --porcelain --untracked-files=no
    if ($dirty) {
        throw "作業ツリーに未コミットの変更があります。bot ブランチ操作前にクリーンにしてください:`n$dirty"
    }

    # 2. bot ブランチ準備（無ければ BASE から作成、有れば BASE を取り込み最新化）
    & git rev-parse --verify --quiet "refs/heads/$BOT_BRANCH" 2>$null | Out-Null
    $botExists = ($LASTEXITCODE -eq 0)
    if ($botExists) {
        Write-Log "bot ブランチへ切替し $BASE_BRANCH を取り込み"
        Invoke-Git checkout $BOT_BRANCH | Out-Null
        try {
            Invoke-Git merge --no-edit $BASE_BRANCH | Out-Null
        } catch {
            # コンフリクト等の merge 失敗時はツリーを mid-merge で残さず中断する
            # （残すと次回以降の未コミット判定で全実行が恒久ブロックされるため）
            & git merge --abort 2>$null | Out-Null
            throw "bot ブランチへの $BASE_BRANCH 取り込みに失敗（merge --abort 実施済み）: $($_.Exception.Message)"
        }
    } else {
        Write-Log "bot ブランチを $BASE_BRANCH から新規作成"
        Invoke-Git checkout -b $BOT_BRANCH $BASE_BRANCH | Out-Null
    }

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
    Invoke-Git add "official-llms-txts" | Out-Null
    & git diff --cached --quiet "official-llms-txts" | Out-Null; $dlChanged = ($LASTEXITCODE -ne 0)
    if ($dlChanged) {
        Invoke-Git commit -m "chore(official-docs): 公式 llms.txt 定期取り込み (bot)" | Out-Null
        Write-Log "dl 差分を commit"
    } else {
        Write-Log "dl 差分なし"
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

        $diff = & git diff $baseCommit $headCommit -- $s.Input
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
            # checkout で追跡ファイルを HEAD へ戻し、clean で手順10退避コピー等の
            # 未追跡ファイルも除去する（次の git add で混入させない）。
            $siteDir = Split-Path $s.Detail -Parent
            Invoke-Git checkout -- $siteDir | Out-Null
            & git clean -fd $siteDir 2>$null | Out-Null
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
