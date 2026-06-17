<#
.SYNOPSIS
  ja 翻訳追従リンク自動注入 watch bot（無人実行用・生成 bot とは別 bot）。

.DESCRIPTION
  Windows タスクスケジューラから、生成 bot（run-doc-summary.ps1）とは別枠で起動される想定。
  専用 bot ブランチ bot/doc-summary 上で、公式 ja ドキュメントへの翻訳反映を検出し、
  既存サマリ（detail/light）の en 単独リンクへ [日本語] リンクを純追記（本文不変）する。
  検出と注入は watch.py が担い、本スクリプトは bot ブランチ準備・commit・
  bot 限定セキュア push を担当する。生成 bot と同じ共通基盤 doc-summary-common.ps1 を
  dot-source して git ラッパ・セキュア push・ログを共有する。

  生成 bot と分離する理由: 役割（原文→サマリ生成 vs 既存サマリへの ja 追従）が異なり、
  実行頻度・失敗時の影響範囲・モデル要否（watch は LLM 不要の純機械処理）が異なる。
  共有はセキュリティ上慎重な push と git ラッパに限定し、その他は独立させる。

.PARAMETER DryRun
  push のみ抑止する。scan/check/inject・ローカル commit は実施する（一周検証用）。

.PARAMETER SkipCheck
  ja 反映の再チェック（network）をスキップし、既存 registry の ready のみで inject する
  （オフライン検証・高速確認用）。

.PARAMETER RestoreBranch
  終了時に開始前のブランチへ戻す（手動テスト時の利便。既定は戻さない）。

.NOTES
  - 生成 bot（15:00）と時間をずらして実行する（推奨 15:30）。同一 bot ブランチを共有する
    ため同時実行は避ける。
  - 注入は本文不変・置換数==1 検証済の純追記のみ。push は bot ブランチ限定（実行直前 assert）。
  - registry.json の last_checked 等の churn は、実 .md 注入が無い日には revert して
    ツリーをクリーンに保つ（次回 run の未コミット判定を通すため。registry は .md から再導出可能）。
#>
[CmdletBinding()]
param(
    [switch]$DryRun,
    [switch]$SkipCheck,
    [switch]$RestoreBranch
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

# 共通基盤（共有定数・Write-Log・Invoke-Git・Invoke-BotPush・コンソール UTF-8）を読み込む。
# dot-source により関数・定数は本スクリプトのスコープへ定義され、Write-Log は後述の
# $LOG_FILE を解決する。
. (Join-Path $PSScriptRoot "doc-summary-common.ps1")

# --- 定数（本 bot 固有）-----------------------------------------------------
$REPO_ROOT   = (Resolve-Path (Join-Path $PSScriptRoot "..\..")).Path
$LOG_DIR     = Join-Path $REPO_ROOT "work\ja-follow-watch"
$WATCH_PY    = Join-Path $REPO_ROOT ".claude\skills\update-official-doc-summary\scripts\watch.py"
$SUMMARY_DIR = "official-doc-update-summary"

# python の UTF-8 入出力を強制（Windows 既定 CP932 だと ja を含む処理・出力が壊れる）。
$env:PYTHONUTF8 = "1"
$env:PYTHONIOENCODING = "utf-8"

# --- ログ -------------------------------------------------------------------
New-Item -ItemType Directory -Force -Path $LOG_DIR | Out-Null
$LOG_FILE = Join-Path $LOG_DIR ("run-{0}.log" -f (Get-Date -Format "yyyyMMdd-HHmmss"))

# python を解決する（タスクスケジューラ実行時に PATH が通っていない構成も考慮）。
function Resolve-PythonExe {
    foreach ($name in @("python", "python3", "py")) {
        $c = Get-Command $name -ErrorAction SilentlyContinue
        if ($c) { return $c.Source }
    }
    throw "python が見つからない（python / python3 / py いずれも PATH に無い）。Python を導入するか PATH を通すこと"
}

# watch.py を実行し、出力をログへ tee しつつ文字列配列で返す。失敗時は例外化。
# git ラッパと同様、関数内だけ EAP を Continue に下げ、成否は $LASTEXITCODE で判定する
# （python は進捗を stderr に書くため）。ログ出力は Out-Null で抑止し、返り値を汚さない
# （Write-Log は Tee-Object のパススルーを持つため）。
function Invoke-WatchPy {
    param([Parameter(ValueFromRemainingArguments = $true)][string[]]$WatchArgs)
    $py = Resolve-PythonExe
    $prevEAP = $ErrorActionPreference
    $ErrorActionPreference = 'Continue'
    try {
        $out = & $py $WATCH_PY @WatchArgs 2>&1
        $code = $LASTEXITCODE
    } finally {
        $ErrorActionPreference = $prevEAP
    }
    $lines = @($out | ForEach-Object { $_.ToString() })
    foreach ($l in $lines) { Write-Log "  | $l" | Out-Null }
    if ($code -ne 0) {
        throw "watch.py $($WatchArgs -join ' ') が失敗 (exit $code)"
    }
    return $lines
}

# --- メイン -----------------------------------------------------------------
Set-Location $REPO_ROOT
Write-Log "=== run-ja-follow-watch 開始 (DryRun=$DryRun SkipCheck=$SkipCheck) ==="

if (-not (Test-Path $WATCH_PY)) { throw "watch.py が見つからない: $WATCH_PY" }

$startBranch = (& git rev-parse --abbrev-ref HEAD).Trim()
$hadFailure  = $false
$pushAborted = $false
$injected    = $false

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

    # 3. scan（en 単独リンクを registry へ seed・冪等・ネットワーク不要）
    Write-Log "watch.py scan"
    Invoke-WatchPy --root $REPO_ROOT scan | Out-Null

    # 4. check（ja ページを GET して二信号ゲートで ready/pending/manual を再判定）
    if ($SkipCheck) {
        Write-Log "watch.py check はスキップ (-SkipCheck)"
    } else {
        Write-Log "watch.py check"
        Invoke-WatchPy --root $REPO_ROOT check | Out-Null
    }

    # 5. inject --apply（ready を detail+light へ純追記。--commit はせず PowerShell 側で制御）
    Write-Log "watch.py inject --apply"
    $injectOut = Invoke-WatchPy --root $REPO_ROOT inject --apply
    $appliedLines = @($injectOut | Where-Object { $_ -match '\(applied\)' })

    # 6. 実 .md 注入の有無を git で判定して commit / revert を分岐。
    #    inject --apply は registry.json を常に書き換える（last_checked 等の churn）ため、
    #    staged の .md（detail/light）が無ければ「静かな日」とみなし churn を revert する。
    Invoke-Git add $SUMMARY_DIR | Out-Null
    $stagedMd = @(& git diff --cached --name-only -- $SUMMARY_DIR | Where-Object { $_ -match '\.md$' })
    if ($stagedMd.Count -gt 0) {
        $injected = $true
        $count = $appliedLines.Count
        $bodyLines = @($appliedLines | ForEach-Object {
                (($_ -replace '^\s*\+\s*', '') -replace '\s*\(applied\)\s*$', '')
            } | ForEach-Object { "- $_" })

        # コミットメッセージは BOM 無し UTF-8・LF で一時ファイルに書き、-F で渡す
        # （here-string を介さず文字化け/CRLF 混入を避ける）。
        $msgLines = @(
            "refactor(official-docs): ja 翻訳追従リンクを自動注入 ($count件・watch bot)"
            ""
            "req4 watch bot: live ja ドキュメントへの反映を検出した en 単独リンクへ"
            "[日本語] リンクを追加。本文は不変（リンク注入のみ・置換数==1検証済）。"
            ""
        ) + $bodyLines + @(
            ""
            "Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
        )
        $msg = ($msgLines -join "`n") + "`n"
        $msgFile = Join-Path ([System.IO.Path]::GetTempPath()) ("ja-follow-msg-{0}.txt" -f ([System.Guid]::NewGuid().ToString("N")))
        [System.IO.File]::WriteAllText($msgFile, $msg, [System.Text.UTF8Encoding]::new($false))
        try {
            Invoke-Git commit -F $msgFile | Out-Null
        } finally {
            Remove-Item $msgFile -ErrorAction SilentlyContinue
        }
        Write-Log "ja 追従リンクを commit ($count件)"
    } else {
        Write-Log "ja 追従の新規注入なし。registry churn を revert してツリーをクリーン化"
        & git reset -q -- $SUMMARY_DIR 2>$null | Out-Null
        Invoke-Git checkout -- $SUMMARY_DIR | Out-Null
    }

    # 7. push（注入があった場合のみ・bot ブランチ限定・二重防御）
    if (-not $injected) {
        Write-Log "注入なしのため push 不要"
    } elseif ($DryRun) {
        Write-Log "DryRun: push を抑止"
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
    Write-Log "=== run-ja-follow-watch 終了: $status (injected=$injected pushAborted=$pushAborted) ==="
}

if ($hadFailure) { exit 1 } else { exit 0 }
