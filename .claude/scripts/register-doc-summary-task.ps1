<#
.SYNOPSIS
  run-doc-summary.ps1 を Windows タスクスケジューラに日次登録するヘルパー。

.DESCRIPTION
  毎日 -At の時刻に `run-doc-summary.ps1 -Site all` を実行するスケジュールタスクを
  現在の Windows ユーザーとして登録する。

  ログオン種別は既定で「対話（ユーザーがログオン中のみ実行）」にする。これは push 認証で
  使う DPAPI 暗号化トークン（doc-summary-bot-token.xml）が、S4U（パスワードなし）ログオン
  下ではユーザーのマスターキーを復号できず復号に失敗し得るため。常時実行が必要なら
  -RunWhenLoggedOff を付けるが、その場合は DPAPI 復号可否を必ず実走検証すること。

  前提:
    1. doc-summary-bot-token.xml の初回セットアップ（DPAPI 暗号化）が済んでいること
    2. run-doc-summary.ps1 が単体 dry-run で一周成功していること
  詳細手順は同フォルダ README-doc-summary-bot.md を参照。

.PARAMETER At
  起動時刻 "HH:mm"（24h）。既定 "15:00"（実運用値）。

.PARAMETER TaskName
  登録タスク名。既定 "CC-DocSummaryBot"。

.PARAMETER RunWhenLoggedOff
  ログオフ中も実行する（S4U）。DPAPI 復号に失敗し得るため非推奨。付ける場合は実走検証必須。

.PARAMETER WhatIfOnly
  実登録せず、登録内容（trigger / action / principal）を表示するだけにする。

.EXAMPLE
  pwsh -NoProfile -File .claude\scripts\register-doc-summary-task.ps1 -At 15:00 -WhatIfOnly
  pwsh -NoProfile -File .claude\scripts\register-doc-summary-task.ps1 -At 15:00
#>
[CmdletBinding()]
param(
    [ValidatePattern('^\d{2}:\d{2}$')]
    [string]$At = "15:00",
    [string]$TaskName = "CC-DocSummaryBot",
    [switch]$RunWhenLoggedOff,
    [switch]$WhatIfOnly
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$REPO_ROOT = (Resolve-Path (Join-Path $PSScriptRoot "..\..")).Path
$RUNNER    = Join-Path $REPO_ROOT ".claude\scripts\run-doc-summary.ps1"
if (-not (Test-Path $RUNNER)) { throw "ランナーが見つからない: $RUNNER" }

# pwsh を優先（無ければ Windows PowerShell）
$pwshExe = (Get-Command pwsh -ErrorAction SilentlyContinue).Source
if (-not $pwshExe) { $pwshExe = (Get-Command powershell -ErrorAction SilentlyContinue).Source }
if (-not $pwshExe) { throw "pwsh / powershell が PATH に見つからない" }

$argLine = '-NoProfile -ExecutionPolicy Bypass -File "{0}" -Site all' -f $RUNNER
$action  = New-ScheduledTaskAction -Execute $pwshExe -Argument $argLine -WorkingDirectory $REPO_ROOT
$trigger = New-ScheduledTaskTrigger -Daily -At ([datetime]::ParseExact($At, 'HH:mm', $null))

$me = "$env:USERDOMAIN\$env:USERNAME"
if ($RunWhenLoggedOff) {
    # S4U: パスワード保存なしでログオフ中も起動（DPAPI 復号は要検証）
    $principal = New-ScheduledTaskPrincipal -UserId $me -LogonType S4U -RunLevel Limited
} else {
    # Interactive: ユーザーログオン中のみ。DPAPI 復号が確実
    $principal = New-ScheduledTaskPrincipal -UserId $me -LogonType Interactive -RunLevel Limited
}
# ExecutionTimeLimit は「翌日 15:00 の発火と衝突させない」ためだけの上限であり、
# 所要時間の見積もりではない。実測は差分量に比例して伸びる（2026-08-11 で 68 分＝
# claude-code-docs 42 分 + mcp 27 分）。1h では 2026-07-29 に kill され、残留生成物が
# 以後 4 日間の取り込みを止めた。長期停止明けは差分が肥大して確実に超えるため、
# 上限は十分に余らせる。超過して kill されても整地ロジック（Initialize-TreeForDownload）
# が翌日の dl を守るので、上限を短く保つ動機はない。
$settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -DontStopOnIdleEnd `
    -ExecutionTimeLimit (New-TimeSpan -Hours 4)

Write-Host "=== doc-summary-bot タスク登録内容 ==="
Write-Host "TaskName    : $TaskName"
Write-Host "実行ユーザー: $me ($([string]($principal.LogonType)))"
Write-Host "起動        : 毎日 $At"
Write-Host "コマンド    : $pwshExe $argLine"
Write-Host "作業ディレクトリ: $REPO_ROOT"

if ($WhatIfOnly) {
    Write-Host "`n-WhatIfOnly 指定のため実登録はしない。"
    return
}

Register-ScheduledTask -TaskName $TaskName -Action $action -Trigger $trigger `
    -Principal $principal -Settings $settings -Force | Out-Null
Write-Host "`n登録完了。確認: Get-ScheduledTask -TaskName '$TaskName'"
Write-Host "手動テスト実行: Start-ScheduledTask -TaskName '$TaskName'"
Write-Host "削除: Unregister-ScheduledTask -TaskName '$TaskName' -Confirm:`$false"
