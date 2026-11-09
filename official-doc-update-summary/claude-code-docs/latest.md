---
対象期間: 2026年11月07日 〜 2026年11月08日
作成日: 2026-11-08
---

# Claude Code 公式ドキュメント更新サマリ

```markdown
**今回は通常のページ 2 つに小さな変更があり、`desktop` に SSH と WSL のセッションで HTML ファイルをプレビューする節と、組織がそのプレビューのスクリプトを止める節が加わり、`settings-reference` の `disableBrowserExternalNavigation` にも同じことが載りました**。新しいページはなく、228 ページ中 2 ページが変わり、変更はページ単位で 37 行（追加 33・削除 4）です。50 行以上変わったページはないので、大幅更新はありません。changelog と `llms.txt` は変わっておらず、見出しマップには `desktop` の見出しが 2 つ加わりました。総行数は 127,978 行から 128,007 行に増えました。取り上げる項目が 2 つなので、ハイライトも 2 件です。

主要なものを以下に挙げます。

1. `desktop` に h4「Preview HTML files in SSH and WSL sessions」が加わり、SSH か WSL のセッションでは、チャットの HTML ファイルのパスをクリックすると Browser ペインでプレビューでき、グラフや表が空のままなら上に出る通知が理由を示す、と載った（Claude Desktop v4.23118.0 より前は、このプレビューでスクリプトが動かなかった）
2. `desktop` に h4「Turn off scripts in SSH and WSL previews for your organization」が加わり、managed setting の `disableBrowserExternalNavigation` を `true` にすると SSH と WSL の HTML プレビューでもスクリプトが動かなくなる、と載った（managed settings をまだ受け取っていないコンピューターでは `parentSettingsBehavior` も `"merge"` にする、という警告つき。`settings-reference` の同じキーにも加わった）
```

## ハイライト

1. [**SSH と WSL のセッションで HTML ファイルをプレビューする節が加わった**](./latest-detail.md#1-ssh-と-wsl-のセッションで-html-ファイルをプレビューする節が加わった):  
  `desktop` の「Preview your app」に h4「Preview HTML files in SSH and WSL sessions」が加わりました。SSH か WSL のセッションでは、チャットに出た HTML ファイルのパスをクリックすると、そのファイルを Browser ペインでプレビューできます。グラフや表が空のままなら、プレビューの上に出る通知が理由を示します。`This preview doesn't load anything from the web` はスクリプトは動くがウェブからは何も読み込まないこと、`This preview doesn't run scripts or load anything from the web` はスクリプトも動かないことを示し、後者は Claude Desktop v4.23118.0 より前はこのプレビューでスクリプトが動かなかったので、Desktop を更新して開き直すよう案内しています
2. [**disableBrowserExternalNavigation で SSH と WSL のプレビューのスクリプトも止まる**](./latest-detail.md#2-disablebrowserexternalnavigation-で-ssh-と-wsl-のプレビューのスクリプトも止まる):  
  `desktop` に h4「Turn off scripts in SSH and WSL previews for your organization」が加わり、SSH と WSL のセッションの HTML プレビューでスクリプトを動かさないようにするには、managed setting の `disableBrowserExternalNavigation` を `true` にする、と載りました。設定はサーバー管理の設定か、Desktop を動かすコンピューターの MDM ポリシーや managed settings ファイルに置き（リモートのマシンや WSL のディストリビューションからは読まれない）、Claude Code の managed settings をまだ受け取っていないコンピューターでは `parentSettingsBehavior` も `"merge"` にする、という警告がついています。同じページの「Restrict external browsing for your organization」と「Managed settings」の表、`settings-reference` の `disableBrowserExternalNavigation` にも、SSH と WSL の HTML プレビューではスクリプトが動かない、と加わりました

## 新規追加されたページ

（今回の対象期間に新規追加・削除されたドキュメントページはありません。`llms.txt` は変わっておらず、`llms-full.txt` に展開されている固有のページも 228 のままで、`Source:` の行が 231 あり 3 ページが 2 回展開されている状態も前回と同じです）

## 大幅に更新されたページ

（今回の対象期間に、50 行以上変わったページはありません。最も多いのは `desktop` の 33 行です）

## 軽微な更新

今回の差分は **`llms-full.txt` と見出しマップの 2 ファイル**で、`llms.txt` は変わっていません。`llms-full.txt` の生の差分は追加 33 行・削除 4 行で、ページの並びは変わっていません。228 ページ中 **2 ページ**（`desktop`・`settings-reference`）が変わり、ページ単位の合計は 37 行（追加 33・削除 4）で生の差分と一致します（2 回展開されている 3 ページはどれも変わっていません）。changelog は変わっておらず、収録リリースは 437 のまま、最新は前回と同じ v2.1.319（2026年11月06日）です。大幅更新はないので、**2 ページ**すべてを以下にまとめます。

`llms-full.txt` の総行数は **127,978 行から 128,007 行へ 29 行増え**ました（生の差分の差し引き 33 − 4 と一致）。`Source:` の行は 231、固有のページは 228 のままで、2 回展開されている 3 ページ（`plugins/create`・`plugins/install`・`plugins/mods/overview`）も前回と同じです。コードフェンスの外の見出しは、引用の中の見出しも数えると 6,070 から 6,072 へ、行頭が `#` の見出しだけを数えると 6,059 から 6,061 へ、どちらも 2 つ増えました。加わったのは `desktop` の h4「Preview HTML files in SSH and WSL sessions」と「Turn off scripts in SSH and WSL previews for your organization」で、外れた見出しや改称された見出しはありません。

**新機能**

- SSH と WSL のセッションで HTML ファイルをプレビューする節（`desktop`。詳細はハイライト 1 参照）

**機能改善**

- `disableBrowserExternalNavigation` で SSH と WSL のプレビューのスクリプトも止まること（`desktop`・`settings-reference`。詳細はハイライト 2 参照）

## 新着情報

**今回、新着情報（`whats-new/`）のページに変更はありません**（最新の週のダイジェストは前回と同じ Week 37 です）。

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-11-07.md](./archives/latest/2026-11-07.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-11-07.md](./archives/latest-detail/2026-11-07.md)

<!--
base_commit: 0b52aad1c2858e15e1387c14baa0116109fe73bd
head_commit: f31cb8e4e9faf9cb1bbe213ad567b17f36459a04
generated_at_full: 2026-11-09T15:06:25+09:00
-->
