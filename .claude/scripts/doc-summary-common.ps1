<#
.SYNOPSIS
  doc-summary 系 bot の共通基盤（dot-source 用）。
.DESCRIPTION
  生成 bot（run-doc-summary.ps1）と ja 追従 watch bot（run-ja-follow-watch.ps1）が
  共有する定数・git ラッパ・bot ブランチ限定セキュア push・ログ関数を 1 箇所に集約する。
  両 bot が同一実装を二重保守して drift するのを防ぐのが目的（特にセキュリティ上慎重な
  Invoke-BotPush）。

  使い方（各 bot 側）:
    Set-StrictMode -Version Latest
    $ErrorActionPreference = "Stop"
    . (Join-Path $PSScriptRoot "doc-summary-common.ps1")
    $LOG_DIR  = ...; New-Item -ItemType Directory -Force -Path $LOG_DIR | Out-Null
    $LOG_FILE = Join-Path $LOG_DIR ("run-{0}.log" -f (Get-Date -Format "yyyyMMdd-HHmmss"))
    # 以降 Write-Log / Invoke-Git / Invoke-BotPush を使用可

  ※ dot-source されると関数・定数は呼び出し元スコープに定義され、Write-Log は呼び出し元の
    $LOG_FILE を参照する。REPO_ROOT は各 bot 側で自前の $PSScriptRoot から解決する
    （本ファイルと各 bot は同じ .claude\scripts に置く前提）。
#>

# --- 共有定数 ---------------------------------------------------------------
$BOT_BRANCH  = "bot/doc-summary"
$BASE_BRANCH = "main"
# bot push 用 PAT を DPAPI 暗号化して保管するファイル（同一ユーザー・同一マシンのみ復号可）。
# 初回セットアップ: Read-Host -AsSecureString | Export-Clixml $TOKEN_FILE
$TOKEN_FILE  = Join-Path $env:USERPROFILE ".claude\doc-summary-bot-token.xml"

# 外部プロセス（claude -p / python）の UTF-8 出力を正しくデコードする。既定コンソール
# コードページ（CP932 等）でデコードすると日本語が化け、claude -p の result JSON の
# ConvertFrom-Json が壊れて is_error を誤判定する（生成成功でも失敗扱いで生成物が破棄され
# 得る。実害: 2026-06-07 の自動実行が Phase 3 PASS 済み生成物を破棄し FAILURE 終了した）。
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$OutputEncoding = [System.Text.Encoding]::UTF8

# --- ログ -------------------------------------------------------------------
# 呼び出し元が事前に設定した $LOG_FILE へ追記する（dot-source により本関数は
# 呼び出し元スコープに置かれ、$LOG_FILE を解決できる）。
function Write-Log {
    param([string]$Message, [string]$Level = "INFO")
    $line = "{0} [{1}] {2}" -f (Get-Date -Format "yyyy-MM-dd HH:mm:ss"), $Level, $Message
    $line | Tee-Object -FilePath $LOG_FILE -Append
}

# --- git ラッパ -------------------------------------------------------------
# 成否は $LASTEXITCODE のみで判定する。git は正常時も "Switched to branch" /
# "Already up to date." 等を stderr に書くため、呼び出し側が EAP='Stop' や PowerShell 7.4
# 既定の $PSNativeCommandUseErrorActionPreference=$true の下では正常 stderr が終端エラー化し、
# 成功した checkout/merge まで FAILURE 扱いになる（実害: 対話 pwsh の手動実行が bot 切替直後の
# "Switched to branch" で異常終了）。対策: (1) 関数内だけ EAP を Continue に下げ $LASTEXITCODE で
# 判定 (2) 出力は ErrorRecord のままだと呼び出し側パイプで再放出され得るため文字列化して返す。
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

# --- bot ブランチ限定セキュア push ------------------------------------------
# GCM を一時無効化し、PAT を inline credential helper 経由でその push 1 回だけ git に
# 渡す（URL/引数/ログに露出させない）。無人実行で GCM の GUI プロンプトを出さずに
# 非対話 push できる。
# トークン取得元は (1) 環境変数 GITHUB_PERSONAL_ACCESS_TOKEN を優先し、(2) 無ければ
# DPAPI 暗号化ファイル $TOKEN_FILE にフォールバックする。env 変数は失効時の再設定が
# 容易（ファイル再暗号化が不要）で、User スコープに置けば Interactive ログオンの
# スケジュールタスクからも参照できる。
function Invoke-BotPush {
    param([string]$Branch)
    $token = $env:GITHUB_PERSONAL_ACCESS_TOKEN
    if (-not [string]::IsNullOrEmpty($token)) {
        $tokenSrc = "env:GITHUB_PERSONAL_ACCESS_TOKEN"
    } else {
        if (-not (Test-Path $TOKEN_FILE)) {
            throw "環境変数 GITHUB_PERSONAL_ACCESS_TOKEN が未設定で、トークンファイル $TOKEN_FILE も無い。どちらかを用意してください"
        }
        # DPAPI 復号（同一 Windows ユーザー・同一マシンでのみ成功する）
        try {
            $sec = Import-Clixml $TOKEN_FILE
            $token = (New-Object System.Management.Automation.PSCredential("x-access-token", $sec)).GetNetworkCredential().Password
        } catch {
            throw "トークン復号に失敗（別ユーザー/別マシンでは復号不可）: $($_.Exception.Message)"
        }
        $tokenSrc = "DPAPI $TOKEN_FILE"
    }
    if ([string]::IsNullOrEmpty($token)) { throw "トークンが空です（取得元: $tokenSrc）" }
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
