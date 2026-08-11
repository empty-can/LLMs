<#
.SYNOPSIS
  run-ja-follow-watch.ps1 を Windows タスクスケジューラに週次登録するヘルパー。

.DESCRIPTION
  毎週 -DayOfWeek の -At 時刻に `run-ja-follow-watch.ps1`（引数なし＝フル実行:
  scan→check→inject→commit→bot 限定 push）を現在の Windows ユーザーとして登録する。

  生成 bot（CC-DocSummaryBot, 15:00）とは別 bot として独立登録する。同一 bot ブランチ
  bot/doc-summary と作業ツリーを共有するため、生成 bot の実行中に走ると作業ツリーが
  dirty で弾かれる。ランナー側に 20 分の dirty 待機があるが、生成が 15:50 を跨ぐ日は
  待機上限に達して失敗する（2026-07-14 / 08-07 / 08-08 / 08-11 に実発生）。生成の所要は
  差分量で決まりこちらでは制御できないため、時間差を広げる方向では解決しない。

  日次でなく週次にしているのは、日次で回す実益が観測されないため。2026-06-24 以降
  24 回連続で注入 0 件であり、待ち行列は上流で詰まっている（人手 promote 待ち 569 件 /
  公式 ja ページの出現待ち 314 件）。どちらも日単位では動かない。加えて watch.py の
  iter_pairs は live と archives/ 配下の全スナップショットを走査するため、週次にしても
  日次分の取りこぼしは発生しない。check のコストは pending+manual の件数に比例する
  固定コストで、実行間隔には比例しない。

  【暫定】最終形はジョブの直列化（dl → 要約 → ja 追従）で、ja 追従の先頭で実行日を
  判定する。この時刻トリガはそれが実装されるまでの暫定措置であり、生成が
  ExecutionTimeLimit（PT4H＝遅くとも 19:00）で必ず終わることを前提に 20:00 に置いている。

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
  起動時刻 "HH:mm"（24h）。既定 "20:00"（生成 bot の ExecutionTimeLimit 満了後）。

.PARAMETER DayOfWeek
  起動曜日。既定 Sunday（月曜の朝に前週分が反映済みの状態になるように）。

.PARAMETER TaskName
  登録タスク名。既定 "CC-DocJaFollowBot"。

.PARAMETER RunWhenLoggedOff
  ログオフ中も実行する（S4U）。DPAPI 復号に失敗し得るため非推奨。付ける場合は実走検証必須。

.PARAMETER WhatIfOnly
  実登録せず、登録内容（trigger / action / principal）を表示するだけにする。

.EXAMPLE
  pwsh -NoProfile -File .claude\scripts\register-ja-follow-task.ps1 -WhatIfOnly
  pwsh -NoProfile -File .claude\scripts\register-ja-follow-task.ps1 -At 20:00 -DayOfWeek Sunday
#>
[CmdletBinding()]
param(
    [ValidatePattern('^\d{2}:\d{2}$')]
    [string]$At = "20:00",
    [ValidateSet("Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday")]
    [string]$DayOfWeek = "Sunday",
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
$trigger = New-ScheduledTaskTrigger -Weekly -DaysOfWeek $DayOfWeek `
    -At ([datetime]::ParseExact($At, 'HH:mm', $null))

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
Write-Host "起動        : 毎週 $DayOfWeek $At（生成 bot CC-DocSummaryBot と重ねないこと）"
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
