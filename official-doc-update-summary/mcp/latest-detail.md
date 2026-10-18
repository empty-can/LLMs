---
対象期間: 2026年10月14日 〜 2026年10月17日
作成日: 2026-10-17
---

# MCP 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
今回の対象期間の差分は本文 `llms-full.txt` の追加 4 行・削除 4 行だけで、索引 `llms.txt` には変更がありません。ページの追加・削除はなく、SEP 索引ページの件数表記の修正と、SEP-2640 の参考文献リストの記法変更の 2 点にとどまります。

主要なものを以下に挙げます。

1. SEP 索引ページの Summary にある Final の件数が 42 から 43 に修正された。一覧表には、2026年10月06日 作成のサマリで報告した SEP-2127 の追加以降すでに 43 件が並んでおり、件数表記が今回これに追い付いた
2. SEP-2640（Skills Extension）の References で、SEP-2133・SEP-2549・SEP-2076 への参照 3 件の書き方が `[SEP-xxxx]` から `[SEP-xxxx][]` に変わった。説明文と、ページ末尾にある GitHub の PR へのリンク定義は変わっていない
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**SEP 索引の Final 件数が一覧表の実数 43 件にそろう**](#1-sep-索引の-final-件数が一覧表の実数-43-件にそろう):  
  `seps/index` の Summary 節で、Final の件数が 42 から 43 に修正された。一覧表（All SEPs）は差分の前から 43 行すべてが Final で、表そのものは今回変わっていない。SEP-2127 の行が加わった際に据え置かれていた件数表記が、表の実数に追い付いた形になる。
2. [**SEP-2640 の References で SEP への参照 3 件の記法を変更**](#2-sep-2640-の-references-で-sep-への参照-3-件の記法を変更):  
  Skills Extension の References 節で、SEP-2133・SEP-2549・SEP-2076 を挙げた 3 項目が `* [SEP-2133]: Extensions` の形から `* [SEP-2133][]: Extensions` の形に書き換えられた。項目の説明文と、参照先となるページ末尾のリンク定義 3 行はいずれも変わっていない。
<!-- light:highlight-list:end -->

## 1. SEP 索引の Final 件数が一覧表の実数 43 件にそろう

今回の差分は本文 `llms-full.txt` だけで、追加 4 行・削除 4 行という内訳です。索引 `llms.txt` には 1 行の変更もなく、`llms-full.txt` の総行数（45,378 行）と収録ページ数（157 件）も変わっていません。対象期間中には取り込みが 3 回ありましたが、MCP 側の入力に変更があったのは最後の 1 回だけです。

変更行のうち 1 行は、SEP の索引ページ「Specification Enhancement Proposals (SEPs)」（`seps/index`）の Summary 節にある件数表記で、`* **Final**: 42` が `* **Final**: 43` になりました。その下の一覧表（All SEPs）は今回の差分に含まれていません。差分の前から 43 行が並び、そのすべてに `Final` のバッジが付いています。この 43 件という数は、`llms-full.txt` に本文が収録されている SEP ページの数、および索引 `llms.txt` の `SEP-` で始まるエントリ数とも一致します。

件数表記と表の行数がずれていたのは、2026年10月06日 作成のサマリで報告した取り込み（commit `4732026`）からです。このとき一覧表に SEP-2127「MCP Server Cards - HTTP Server Discovery」の行が加わりましたが、Summary の件数は 42 のまま据え置かれていました。この件数が前回変わったのは 2026年09月14日 作成のサマリで報告した SEP-2640 の追加時で、そのときは表への行の追加と同時に 41 から 42 へ更新されています。今回の修正で、索引ページの件数表記と一覧表の内容が再び一致しました。

- [Specification Enhancement Proposals (SEPs) - MCP Docs](https://modelcontextprotocol.io/seps/index#summary)

## 2. SEP-2640 の References で SEP への参照 3 件の記法を変更

残る 3 行の変更は、「SEP-2640: Skills Extension」（`seps/2640-skills-extension`）の末尾にある References 節です。参考文献リストのうち他の SEP を挙げた 3 項目、SEP-2133（Extensions）、SEP-2549（TTL for list results）、SEP-2076（Agent Skills as first-class primitive (alternative approach)）の書き方が、`* [SEP-2133]: Extensions` の形から `* [SEP-2133][]: Extensions` の形に変わりました。Markdown では `[ラベル]` も `[ラベル][]` も、同じラベルのリンク定義を参照する参照リンクの書き方です。参照先の定義はページ末尾に `[SEP-2133]: https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2133` のような形で 3 行置かれており、いずれも GitHub の本家リポジトリの PR を指しています。これらの定義行は差分の前からあり、今回も変わっていません。

各項目の説明文と、同じリストの他の項目（Agent Skills specification・Skills Over MCP Working Group charter・Decision Log など）も変わっていません。変更前の `[SEP-2133]: Extensions` のように行頭が `[ラベル]: ` で始まる書き方は、リンク定義そのものと同じ形をしています。今回の変更は、これを明示的な参照リンクの形に改めて紛れをなくす、記法上の修正と読めます。`llms-full.txt` 全体を見ても、リスト項目が `[ラベル]: ` や `[ラベル][]: ` で始まる箇所はこの 3 行だけです。なお、同じリストにある Skills Over MCP Working Group charter へのリンクは、`https://modelcontextprotocol.io/community/skills-over-mcp/charter` を指したまま今回も変更されていません。索引 `llms.txt` に載っている同憲章のパス（`community/working-groups/skills-over-mcp`）とは異なります。

- [SEP-2640: Skills Extension - MCP Docs](https://modelcontextprotocol.io/seps/2640-skills-extension#references)

## 新規追加されたページ

<!-- light:new-pages:start -->
今回の対象期間に新たに追加されたページはありません。索引 `llms.txt` に変更はなく、索引側のエントリ数（362 件）と本文 `llms-full.txt` の収録ページ数（157 件）はどちらも前回と同じです。
<!-- light:new-pages:end -->

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
今回の対象期間に大幅な更新（本文 50 行以上の変更）があったページはありません。差分が出た 2 ページはいずれも数行の変更で、「軽微な更新」で扱います。
<!-- light:updated-pages:end -->

## 軽微な更新

<!-- light:minor-updates:start -->
今回差分が出たファイルは `llms-full.txt` の 1 件のみで、変更のあったページは次の 2 件です。

**その他**

- SEP 索引ページの Summary で、Final の件数を 42 から 43 に修正。一覧表の行数（43 件）に合わせたもので、表自体に変更はない（詳細はハイライト 1 参照） — [Specification Enhancement Proposals (SEPs)](https://modelcontextprotocol.io/seps/index#summary)
- SEP-2640（Skills Extension）の References で、SEP-2133・SEP-2549・SEP-2076 への参照 3 件の書き方を `[SEP-xxxx]` から `[SEP-xxxx][]` に変更（詳細はハイライト 2 参照） — [SEP-2640: Skills Extension](https://modelcontextprotocol.io/seps/2640-skills-extension#references)
<!-- light:minor-updates:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-10-14.md](./archives/latest/2026-10-14.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-10-14.md](./archives/latest-detail/2026-10-14.md)

<!--
base_commit: eeed0d5ebbc9b23608e5903e7bc33bb6c996a581
head_commit: df8be8b99ca6342f63f7c7b52da55b4609b1c128
generated_at_full: 2026-10-18T15:20:39+09:00
-->
