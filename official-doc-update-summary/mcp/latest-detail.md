---
対象期間: 2026年07月28日 〜 2026年08月01日
作成日: 2026-08-01
---

# MCP 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
今回の対象期間は、2026年07月28日に公開された仕様リビジョン `2026-07-28` を受けた記述の整備が中心です。新規追加ページと大幅更新ページはなく、43 ページの軽微な更新にとどまりました。うち 41 ページは SEP ページ群への一斉注記追加で、残りはエラーコードの追従修正とバージョン表記の更新です。

主要なものを以下に挙げます。

1. Final ステータスの SEP ページ 41 件すべてに、採択時点の設計の歴史的記録である旨の注記が追加された
2. Tasks 拡張に残っていたエラーコード `-32003` が、現行仕様の採番に合わせて `-32021` に修正された
3. Versioning ページの現行プロトコルバージョン表記が `2026-07-28` に更新された
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**Final SEP への歴史的記録注記の一斉付与**](#1-final-sep-への歴史的記録注記の一斉付与):  
  Final ステータスに達した SEP ページ 41 件すべての冒頭に、当該 SEP は採択時点の設計の歴史的記録であり最終化後の変更は反映されない旨の注記が置かれた。SEP Guidelines 側にも同じ方針が明文化されている。
2. [**Tasks 拡張のエラーコードを現行採番に修正**](#2-tasks-拡張のエラーコードを現行採番に修正):  
  `2026-07-28` でエラーコード割り当て方針が定められた際に `-32003` から `-32021` へ再採番された Missing Required Client Capability が、Tasks 拡張のページでは旧番号のまま残っていた。3 つの節にまたがる計 4 箇所が現行の `-32021` に修正された。
3. [**現行プロトコルバージョン表記の更新**](#3-現行プロトコルバージョン表記の更新):  
  Versioning ページの「Revisions」節で、current として示されるプロトコルバージョンが `2025-11-25` から `2026-07-28` に更新された。
<!-- light:highlight-list:end -->

## 1. Final SEP への歴史的記録注記の一斉付与

Final ステータスに達した SEP のページに、冒頭注記が一斉に追加されました。文面は全ページ共通で、本 SEP は Final に達しており採択された時点の設計の歴史的記録として保存されていること、最終化後にプロトコルへ加えられた変更はここに反映されないこと、権威ある要件は現行仕様とその changelog を参照すべきことを述べています。

今回の差分で変更された 43 ページのうち 41 ページがこの注記の追加によるものです。`llms-full.txt` に含まれる SEP ページは一覧ページ `/seps/index` を除いて 41 件で、そのすべてが対象になりました。SEP-414 のような古い番号から SEP-2663 まで、Standards Track・Extensions Track・ガバナンス系の区別なく一律に適用されています。

背景として、SEP Guidelines の「Reporting SEP Bugs or Updates」にも同じ方針を述べる段落が追加されました。Final SEP は最終化後に更新されないこと、SEP 確定後に仕様が変わった場合は現行仕様が権威を持つこと、そして各 Final SEP のページにその旨の告知を表示することが明記されています。`2026-07-28` では `initialize` ハンドシェイクの廃止や MRTR の導入といった大きな設計変更が入っており、確定済み SEP の記述と現行仕様が食い違う場面が生じ得ます。今回の注記は、読み手が SEP の記述を現行仕様と取り違えないようにするための措置と読めます。

- [SEP Guidelines - MCP Docs](https://modelcontextprotocol.io/community/sep-guidelines#reporting-sep-bugs-or-updates)
- [SEP-2575: Make MCP Stateless - MCP Docs](https://modelcontextprotocol.io/seps/2575-stateless-mcp)

## 2. Tasks 拡張のエラーコードを現行採番に修正

`2026-07-28` では、JSON-RPC が実装定義用に予約するサーバーエラー範囲を分割するエラーコード割り当て方針が定められました。`-32000`〜`-32019` は既存実装のために据え置き、`-32020`〜`-32099` を仕様専用としたもので、この際にドラフト段階で導入されていたエラーコードが再採番されています。Missing Required Client Capability は `-32003` から `-32021` に変わりました。

Tasks 拡張の SEP-2663 のページには旧番号の `-32003` が残っていましたが、今回それが `-32021` に修正されました。修正箇所は「Capability Negotiation」節の説明文と JSON 例、「Task Status Notifications」節の JSON 例、「Error Handling」節のエラー一覧の計 4 箇所です。いずれも記述の意味そのものは変わっておらず、コア仕様の採番への追従にあたります。

この修正により、`llms-full.txt` 上で `-32003` に言及している箇所は、再採番の経緯を説明する changelog の記載だけになりました。

- [SEP-2663: Tasks Extension - MCP Docs](https://modelcontextprotocol.io/seps/2663-tasks-extension#error-handling)
- [Overview - MCP Docs](https://modelcontextprotocol.io/specification/2026-07-28/basic/index#error-codes)

## 3. 現行プロトコルバージョン表記の更新

Versioning ページの「Revisions」節は、リビジョンが Draft・Current・Final のいずれかで示されることを説明したうえで、現行のプロトコルバージョンを 1 行で示しています。この行が `2025-11-25` から `2026-07-28` に更新され、リンク先も `/specification/2026-07-28/` になりました。

仕様本体の切り替えは前回サマリで扱ったとおり 2026年07月28日のリリースで完了していましたが、学習ガイド側の Versioning ページには旧リビジョンの表記が残っていました。今回の更新で、ドキュメント全体の現行版表記が揃ったことになります。

- [Versioning - MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/learn/versioning#revisions)

## 新規追加されたページ

<!-- light:new-pages:start -->
今回の対象期間では `llms.txt` のページ一覧に変更がなく、新規追加されたページはありません。
<!-- light:new-pages:end -->

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
単一ページで 50 行以上に及ぶ変更はありませんでした。最も変更量の多いページでも 18 行（注記の追加と著者一覧の補完）にとどまります。変更のあった 43 ページはすべて下記「軽微な更新」に整理しています。
<!-- light:updated-pages:end -->

## 軽微な更新

<!-- light:minor-updates:start -->
今回変更のあった 43 ページは、内容としては以下に集約されます。

**機能改善**

- Final ステータスに達した SEP ページ 41 件すべての冒頭に、当該 SEP が採択時点の設計の歴史的記録であり、最終化後のプロトコル変更は反映されない旨の注記が追加された（詳細はハイライト 1 参照）
- SEP Guidelines の「Reporting SEP Bugs or Updates」に、Final SEP は最終化後に更新されず、SEP 確定後に仕様が変わった場合は現行仕様が権威を持つ旨の段落が追加された（詳細はハイライト 1 参照） — [SEP Guidelines](https://modelcontextprotocol.io/community/sep-guidelines#reporting-sep-bugs-or-updates)
- Versioning ページの「Revisions」で、current として示されるプロトコルバージョンが `2025-11-25` から `2026-07-28` に更新された（詳細はハイライト 3 参照） — [Versioning](https://modelcontextprotocol.io/docs/2026-07-28/learn/versioning#revisions)

**バグ修正**

- Tasks 拡張（SEP-2663）に残っていた Missing Required Client Capability のエラーコード `-32003` が、現行仕様の採番である `-32021` に修正された（詳細はハイライト 2 参照） — [SEP-2663: Tasks Extension](https://modelcontextprotocol.io/seps/2663-tasks-extension#error-handling)
- SEP-1865（MCP Apps）の著者一覧が末尾のカンマで途切れていたものが補完され、3 名から 9 名になった — [SEP-1865: MCP Apps - Interactive User Interfaces for MCP](https://modelcontextprotocol.io/seps/1865-mcp-apps-interactive-user-interfaces-for-mcp)
- SEP-2322（Multi Round-Trip Requests）の著者一覧が同様に補完され、Gabriel Zimmerman が加わって 3 名になった — [SEP-2322: Multi Round-Trip Requests](https://modelcontextprotocol.io/seps/2322-MRTR)
- SEP-2575（Make MCP Stateless）の著者一覧が同様に補完され、Shaun Smith・Harvey Tuch・Kurtis Van Gent が加わって 5 名になった — [SEP-2575: Make MCP Stateless](https://modelcontextprotocol.io/seps/2575-stateless-mcp)
<!-- light:minor-updates:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-07-28.md](./archives/latest/2026-07-28.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-07-28.md](./archives/latest-detail/2026-07-28.md)

<!--
base_commit: 37f111d9d0c49fa9fd2ab79826f803c7de899551
head_commit: 19822214b48ea654ba58df34a2f03353c8f7a40b
generated_at_full: 2026-08-02T19:32:36+09:00
-->
