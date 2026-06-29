<#
.SYNOPSIS
  run-ja-follow-watch.ps1 を Windows タスクスケジューラに日次登録するヘルパー。

.DESCRIPTION
  毎日 -At の時刻に `run-ja-follow-watch.ps1`（引数なし＝フル実行: scan→check→inject→
  commit→bot 限定 push）を現在の Windows ユーザーとして登録する。

  生成 bot（CC-DocSummaryBot, 既定 15:00）とは別 bot として独立登録する。watch bot は
  生成 bot が当日生成した最新サマリの en 単独リンクも拾うため、必ず生成 bot の後に走らせる
  （既定 15:30）。同一 bot ブランチ bot/doc-summary を共有するので時間を重ねないこと
  （万一重なっても git の index.lock で一方が失敗するだけで破壊はしないが、その日の実行は
  取りこぼす）。生成 bot が長引いた場合に備え十分な間隔を空けるのが安全。

  ログオン種別は既定で「対話（ユーザーがログオン中のみ実行）」にする。push 認証で使う
  DPAPI 暗号化トークン（doc-summary-bot-token.xml）が、S4U（パスワードなし）ログオン下では
  ユーザーのマスターキーを復号できず復号に失敗し得るため。常時実行が必要なら
  -RunWhenLoggedOff を付けるが、その場合は DPAPI 復号可否を必ず実走検証すること。

  前提:
    1. doc-summary-bot-token.xml の初回セットアップ（DPAPI 暗号化）が済んでいること
       （生成 bot と同一トークンを共有する）
    2. run-ja-follow-watch.ps1 が単体 dry-run（-DryRun -SkipCheck）で一周成功していること
  詳細手順は同フォルダ README-doc-summary-bot.md を参照。

.PARAMETER At
  起動時刻 "HH:mm"（24h）。既定 "15:30"（生成 bot の後）。

.PARAMETER TaskName
  登録タスク名。既定 "CC-DocJaFollowBot"。

.PARAMETER RunWhenLoggedOff
  ログオフ中も実行する（S4U）。DPAPI 復号に失敗し得るため非推奨。付ける場合は実走検証必須。

.PARAMETER WhatIfOnly
  実登録せず、登録内容（trigger / action / principal）を表示するだけにする。

.EXAMPLE
  pwsh -NoProfile -File .claude\scripts\register-ja-follow-task.ps1 -At 15:30 -WhatIfOnly
  pwsh -NoProfile -File .claude\scripts\register-ja-follow-task.ps1 -At 15:30
#>
[CmdletBinding()]
param(
    [ValidatePattern('^\d{2}:\d{2}$')]
    [string]$At = "15:30",
    [string]$TaskName = "CC-DocJaFollowBot",
    [switch]$RunWhenLoggedOff,
    [switch]$WhatIfOnly
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$REPO_ROOT = (Resolve-Path (Join-Path $PSScriptRoot "..\..")).Path
$RUNNER    = Join-Path $REPO_ROOT ".claude\scripts\run-ja-follow-watch.ps1"
if (-not (Test-Path $RUNNER)) { throw "ランナーが見つからない: $RUNNER" }

# pwsh を優先（無ければ Windows PowerShell）
$pwshExe = (Get-Command pwsh -ErrorAction SilentlyContinue).Source
if (-not $pwshExe) { $pwshExe = (Get-Command powershell -ErrorAction SilentlyContinue).Source }
if (-not $pwshExe) { throw "pwsh / powershell が PATH に見つからない" }

# watch bot は引数なしのフル実行（-Site 不要・claude-code-docs のみが watch 対象）
$argLine = '-NoProfile -ExecutionPolicy Bypass -File "{0}"' -f $RUNNER
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
$settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -DontStopOnIdleEnd `
    -ExecutionTimeLimit (New-TimeSpan -Hours 1)

Write-Host "=== ja-follow-watch-bot タスク登録内容 ==="
Write-Host "TaskName    : $TaskName"
Write-Host "実行ユーザー: $me ($([string]($principal.LogonType)))"
Write-Host "起動        : 毎日 $At（生成 bot CC-DocSummaryBot の後に走らせること）"
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
