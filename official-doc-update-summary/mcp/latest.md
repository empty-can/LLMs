---
対象期間: 2026年11月16日 〜 2026年11月17日
作成日: 2026-11-17
---

# MCP 公式ドキュメント更新サマリ

```markdown
今回の対象期間の取り込みは 1 回で、入力の 2 ファイルとも差分がありました（`llms-full.txt` は Extensions Overview の 1 ページで追加 20 行・削除 6 行、`llms.txt` は重複していた Example Servers のエントリ 5 件の削除）。本文の変更では、拡張のライフサイクルの規則がいくつか補われ、Experimental の作業を置くリポジトリの一覧が加わりました。

主要なものを以下に挙げます。

1. Extensions Overview で、拡張のライフサイクルの規則が補われた。Beta を経る要件は Core Maintainers が記録に残る投票で免除できること、段階の変更は Core Maintainer が承認すること、破壊的変更での `revision` 文字列の規則が Experimental にも及ぶこと（無ければ初期リビジョン、知らない値なら有効にすべきでない）が加わり、Experimental の作業を置く 5 つのリポジトリの表が載った
```

## ハイライト

1. [**Extensions Overview で拡張のライフサイクルの規則が補われた**](./latest-detail.md#1-extensions-overview-で拡張のライフサイクルの規則が補われた):  
  拡張の概要ページ Extensions Overview（追加 20 行・削除 6 行）で、ライフサイクルの規則が補われた。Beta を経る要件は Core Maintainers が記録に残る投票（recorded vote）で免除できること、段階の変更は Core Maintainer が承認すること、破壊的変更を加える拡張が settings オブジェクトの `revision` 文字列を追加・増分すべきなのは Experimental と Beta の両方であること（`revision` が無ければ初期リビジョンを意味し、知らない `revision` を受け取った側は拡張を有効にすべきでない）が書き加えられた。Experimental Extensions には、Experimental の作業を置く 5 つのリポジトリの表が加わった。

## 新規追加されたページ

今回の対象期間に新たに追加されたページはありません。本文 `llms-full.txt` の収録ページ数（160 件。URL としては 159 件）は前回と同じです。索引 `llms.txt` ではエントリが 5 件減りましたが、重複していたエントリが外れたもので、索引から消えたページはありません（一意の URL は 360 件のまま）。

## 大幅に更新されたページ

今回の対象期間に大幅な更新（本文 50 行以上の変更）があったページはありません。本文の変更は 1 ページで計 26 行（追加 20 行・削除 6 行）にとどまり、軽微な更新に当たります（ハイライト 1 参照）。

## 軽微な更新

今回差分が出たファイルは `llms-full.txt` と `llms.txt` の 2 件で、本文の 1 ページの変更と、索引の重複エントリの削除がありました。

**機能改善**

- Extensions Overview の Extension Lifecycle で、Experimental の段階に入る方法に `experimental-ext-` のリポジトリの作成を加え、Beta を経る要件は Core Maintainers が記録に残る投票で免除できると明記した（詳細はハイライト 1 参照） — [Extensions Overview](https://modelcontextprotocol.io/extensions/overview#extension-lifecycle)
- 同ページの Official Extension Repositories で、ライフサイクルより前からあるリポジトリは配置の移行中なので、各拡張の現在の段階は表を基準とすると明記した（詳細はハイライト 1 参照） — [Extensions Overview](https://modelcontextprotocol.io/extensions/overview#official-extension-repositories)
- 同ページの Experimental Extensions に、Experimental の作業を置く 5 つのリポジトリの表を加えた（詳細はハイライト 1 参照） — [Extensions Overview](https://modelcontextprotocol.io/extensions/overview#experimental-extensions)
- 同ページの Ground Rules で、実験的な状態の明示を、`experimental-ext-` のリポジトリ（README など）と公開するパッケージの名前に分けて定めた（詳細はハイライト 1 参照） — [Extensions Overview](https://modelcontextprotocol.io/extensions/overview#ground-rules)
- 同ページの Evolution で、段階の変更は Core Maintainer が承認すると明記し、`revision` 文字列の規則の対象を Experimental と Beta の拡張とし、`revision` が無い場合と知らない値を受け取った場合の扱いを加えた（詳細はハイライト 1 参照） — [Extensions Overview](https://modelcontextprotocol.io/extensions/overview#evolution)

**その他**

- Extensions Overview の MCP Apps の表で、説明の末尾にピリオドが付いた — [Extensions Overview](https://modelcontextprotocol.io/extensions/overview#mcp-apps)
- 索引 `llms.txt` で、`docs/2025-11-25/`・`docs/2025-06-18/`・`docs/2025-03-26/`・`docs/2024-11-05/`・`docs/draft/` の各ページの並びの末尾（Debugging の直後）にあった Example Servers（`examples.md`）のエントリ 5 件が外れた。`docs/2026-07-28/` の並びの後ろの 1 件は残り、同じ URL のエントリは 6 件から 1 件になった。エントリ数は 365 件から 360 件、ファイルは 370 行から 365 行になった（末尾に改行が無いため、改行の数では 369 から 364）。一意の URL は 360 件のままで、索引から消えたページはない

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-11-16.md](./archives/latest/2026-11-16.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-11-16.md](./archives/latest-detail/2026-11-16.md)

<!--
base_commit: 819daa7cd17307570b2a672fc258fafc61fd2cb2
head_commit: ab0340993aa5987d27a891141698d57dc355b88b
generated_at_full: 2026-11-18T15:27:25+09:00
-->
