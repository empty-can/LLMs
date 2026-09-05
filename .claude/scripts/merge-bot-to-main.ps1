<#
.SYNOPSIS
  bot/doc-summary → main の合流を、アンカー保全チェック付きで安全に実施する。

.DESCRIPTION
  人間が対話的に実行する品質ゲート用スクリプト。生の git コマンドを都度組み立てる
  代わりに本スクリプトを使うことで、.claude/CLAUDE.md §タグ運用ルールが要求する
  事前チェックの実施漏れを防ぐ。

  外部文書（cc-relative-info の「結論・構成案_ポータブルな.claude共有_v1.2.md」）が
  本リポジトリの特定 commit を出典として引用しており、また本リポジトリの生成サマリも
  フッタの base_commit / head_commit で過去 commit を参照している。履歴を書き換えると
  双方の参照が壊れるため、合流は必ず fast-forward merge で行い、rebase / squash は
  使わない。本スクリプトは --ff-only 固定で、それ以外の合流方法を提供しない。

  検証は「.claude/CLAUDE.md の『現行の anchor タグ』表」を正本として行う。表・タグ・
  blob の三者が一致しない場合は合流を中止する。

.PARAMETER DryRun
  検証のみ実施し、マージは行わない。分岐状態の確認にも使える。

.NOTES
  - push は行わない。run-doc-summary.ps1 と同じく「main へは構造的に push しない」
    設計を維持し、最後に実行すべき push コマンドを表示するに留める。
    そのかわり push.followTags が有効だとその push がタグを漏らすため、事前に検査する。
  - Write-Log は使わない。$LOG_FILE は bot 実行側が用意する前提の変数であり、
    人間が対話実行する本スクリプトが bot のログへ書き込むのは不適切なため。
#>
[CmdletBinding()]
param(
    [switch]$DryRun
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

# 共有定数（$BOT_BRANCH / $BASE_BRANCH）と Invoke-Git を取り込む。ブランチ名を
# 二重に持たないことで bot 側との drift を防ぐ。
. (Join-Path $PSScriptRoot "doc-summary-common.ps1")

$REPO_ROOT   = (Resolve-Path (Join-Path $PSScriptRoot "..\..")).Path
$RULE_DOC    = Join-Path $REPO_ROOT ".claude\CLAUDE.md"
$ANCHOR_FILE = "official-llms-txts/code.claude.com/docs/llms-full.txt"

function Write-Step { param([string]$Message) Write-Host "`n== $Message" -ForegroundColor Cyan }
function Write-Ok   { param([string]$Message) Write-Host "   OK   $Message" -ForegroundColor Green }
function Write-Note { param([string]$Message) Write-Host "        $Message" -ForegroundColor DarkGray }

function Get-AnchorDefinition {
    <#
      .claude/CLAUDE.md の「### 現行の anchor タグ」表を読む。
      同ファイルには「##### 削除済みアンカー」表もあり列構成が異なるため、
      見出しから次の ### までに範囲を限定して取り違えを防ぐ。
    #>
    if (-not (Test-Path -LiteralPath $RULE_DOC)) {
        throw "ルール文書が見つからない: $RULE_DOC"
    }
    $lines = @(Get-Content -LiteralPath $RULE_DOC -Encoding UTF8)

    $start = -1
    $end   = $lines.Count
    for ($i = 0; $i -lt $lines.Count; $i++) {
        if ($start -lt 0) {
            if ($lines[$i] -match '^###\s+現行の anchor タグ') { $start = $i }
        } elseif ($lines[$i] -match '^###\s') {
            $end = $i
            break
        }
    }
    if ($start -lt 0) {
        throw "『現行の anchor タグ』の節が $RULE_DOC に見つからない。ルール文書の構成が変わった可能性がある"
    }

    # | `anchor/<日付>` | `<commit 40桁>` | <断面の説明> | `<blob 40桁>` | <依存出典> |
    $rowPattern = '^\|\s*`(anchor/[^`]+)`\s*\|\s*`([0-9a-f]{40})`\s*\|[^|]*\|\s*`([0-9a-f]{40})`\s*\|'

    $anchors = @()
    foreach ($line in $lines[$start..($end - 1)]) {
        if ($line -match $rowPattern) {
            $anchors += [pscustomobject]@{
                Tag    = $Matches[1]
                Commit = $Matches[2]
                Blob   = $Matches[3]
            }
        }
    }
    # 0 件は「アンカーが無い」ではなく「表を読めていない」と解釈する。素通りさせない。
    if ($anchors.Count -eq 0) {
        throw "『現行の anchor タグ』表から 1 件も読み取れなかった。表の書式が変わった可能性がある（素通りを避けるため中止する）"
    }
    return $anchors
}

function Assert-AnchorsReachable {
    param([object[]]$Anchors, [string]$Ref)
    foreach ($a in $Anchors) {
        & git merge-base --is-ancestor $a.Commit $Ref
        if ($LASTEXITCODE -ne 0) {
            throw "アンカー $($a.Tag)（$($a.Commit)）が $Ref から到達不能。履歴が書き換えられた可能性がある"
        }
    }
    Write-Ok "$($Anchors.Count) 件のアンカーが $Ref から到達可能"
}

Push-Location $REPO_ROOT
try {
    Write-Host "bot → main 合流（アンカー保全チェック付き）" -ForegroundColor White
    Write-Note "リポジトリ: $REPO_ROOT"
    if ($DryRun) { Write-Note "DryRun: 検証のみ実施しマージはしない" }

    # --- 1. アンカー定義の読み込み（正本 = ルール文書の表）---------------------
    Write-Step "1. アンカー定義の読み込み（正本 = .claude/CLAUDE.md）"
    $anchors = @(Get-AnchorDefinition)
    Write-Ok "表から $($anchors.Count) 件のアンカーを読み取った"

    # --- 2. タグ本数の照合 ------------------------------------------------------
    # タグを消してしまうと到達性チェックは対象ゼロで素通りするため、本数照合を先に置く。
    Write-Step "2. タグ本数の照合（表 ⇔ 実タグ）"
    $tags = @(Invoke-Git tag -l 'anchor/*')
    if ($tags.Count -ne $anchors.Count) {
        throw ("anchor タグの本数が表と一致しない: 実タグ {0} 本 / 表 {1} 件。" -f $tags.Count, $anchors.Count +
               "新しい clone ならルール文書の再作成コマンドでタグを作る。意図的に整理した場合は表も更新する")
    }
    Write-Ok "$($tags.Count) 本で一致"

    # --- 3. タグ ⇔ 表 ⇔ blob の一致検証 -----------------------------------------
    Write-Step "3. タグ ⇔ commit ⇔ blob の一致検証"
    foreach ($a in $anchors) {
        if ($tags -notcontains $a.Tag) {
            throw "表にある $($a.Tag) が実タグに存在しない"
        }
        $type = @(Invoke-Git cat-file -t $a.Tag)[0]
        if ($type -ne 'tag') {
            throw "$($a.Tag) が注釈タグではない（type=$type）。ルールは -a での作成を要求している"
        }
        $target = @(Invoke-Git rev-parse "$($a.Tag)^{}")[0]
        if ($target -ne $a.Commit) {
            throw "$($a.Tag) の指す commit が表と異なる: タグ=$target / 表=$($a.Commit)。タグの付け替えは禁止されている"
        }
        $blob = @(Invoke-Git rev-parse "$($a.Commit):$ANCHOR_FILE")[0]
        if ($blob -ne $a.Blob) {
            throw "$($a.Tag) の対象ファイルの blob が表と異なる: 実際=$blob / 表=$($a.Blob)"
        }
        Write-Ok ("{0} -> {1} / blob {2}" -f $a.Tag, $a.Commit.Substring(0, 8), $a.Blob.Substring(0, 8))
    }

    # --- 4. 作業ツリーの確認 ----------------------------------------------------
    # untracked は対象外。リポジトリルートに追跡外の作業ファイルが常在するため。
    Write-Step "4. 作業ツリーの確認（tracked のみ）"
    $dirty = @(Invoke-Git status --porcelain --untracked-files=no)
    if ($dirty.Count -gt 0) {
        throw "tracked に未コミットの変更がある。commit または stash してから再実行する:`n$($dirty -join "`n")"
    }
    Write-Ok "tracked に未コミットの変更なし"

    # --- 5. リモートへのタグ漏れ確認 --------------------------------------------
    Write-Step "5. リモートに anchor タグが漏れていないこと"
    # パイプライン全体を @() で包む。包まないと該当なしのとき $null になり
    # StrictMode 下で .Count 参照が失敗する。
    $remoteAnchorTags = @(@(Invoke-Git ls-remote --tags origin) | Where-Object { $_ -match 'refs/tags/anchor/' })
    if ($remoteAnchorTags.Count -gt 0) {
        throw ("リモートに anchor タグが push されている（ルールで push 厳禁）:`n{0}" -f ($remoteAnchorTags -join "`n"))
    }
    Write-Ok "リモートに anchor タグなし"

    # --- 6. push.followTags の確認 ----------------------------------------------
    # 有効だと、この後に人が実行する git push が意図せずタグを送ってしまう。
    Write-Step "6. push.followTags が無効であること"
    $followTags = & git config --get push.followTags 2>$null
    if ($LASTEXITCODE -eq 0 -and $followTags -match '^(true|1|yes|on)$') {
        throw "push.followTags が有効。push がタグを巻き込むため、`git config --unset push.followTags` してから再実行する"
    }
    Write-Ok "push.followTags は無効（push がタグを巻き込まない）"

    # --- 7. fetch と分岐状態の確認 ----------------------------------------------
    Write-Step "7. fetch と分岐状態の確認"
    Invoke-Git fetch origin --no-tags | Out-Null
    $counts  = @(Invoke-Git rev-list --left-right --count "$BASE_BRANCH...$BOT_BRANCH")[0] -split '\s+'
    $ahead   = [int]$counts[0]
    $behind  = [int]$counts[1]
    Write-Note "$BASE_BRANCH は $BOT_BRANCH に対して $ahead ahead / $behind behind"
    if ($ahead -gt 0) {
        throw ("$BASE_BRANCH が $BOT_BRANCH に対して $ahead コミット先行しており fast-forward 関係が壊れている。" +
               "本スクリプトは --ff-only 固定なので中止する。真のマージが要るかは人が判断すること")
    }
    if ($behind -eq 0) {
        Write-Ok "差分なし。合流の必要はない"
        return
    }
    Write-Ok "fast-forward 可能（$behind コミット）"

    # --- 8. マージ前のアンカー到達性 --------------------------------------------
    Write-Step "8. マージ前: アンカーが $BOT_BRANCH から到達可能か"
    Assert-AnchorsReachable -Anchors $anchors -Ref $BOT_BRANCH

    if ($DryRun) {
        Write-Host "`nDryRun のため、ここで終了する（マージは実施していない）" -ForegroundColor Yellow
        Write-Note "実行するには -DryRun を外して再実行する"
        return
    }

    # --- 9. fast-forward マージ -------------------------------------------------
    Write-Step "9. $BOT_BRANCH -> $BASE_BRANCH を fast-forward マージ"
    $startBranch = @(Invoke-Git rev-parse --abbrev-ref HEAD)[0]
    try {
        Invoke-Git checkout $BASE_BRANCH | Out-Null
        Invoke-Git merge --ff-only $BOT_BRANCH | Out-Null
        Write-Ok "マージ完了: $BASE_BRANCH = $(@(Invoke-Git rev-parse --short $BASE_BRANCH)[0])"

        # --- 10. マージ後のアンカー到達性 ---------------------------------------
        Write-Step "10. マージ後: アンカーが $BASE_BRANCH から到達可能か"
        Assert-AnchorsReachable -Anchors $anchors -Ref $BASE_BRANCH
    } finally {
        # 実行前のブランチへ戻す（操作者は通常 bot ブランチに居る）
        Invoke-Git checkout $startBranch | Out-Null
        Write-Note "ブランチを $startBranch へ戻した"
    }

    Write-Host "`n合流はローカルで完了。push は本スクリプトでは行わない。" -ForegroundColor White
    Write-Host "  git push origin $BASE_BRANCH" -ForegroundColor Yellow
    Write-Note "タグは push しないこと（--tags / --follow-tags / --mirror を使わない）"
}
finally {
    Pop-Location
}
