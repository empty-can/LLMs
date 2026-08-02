---
対象期間: 2026年07月28日 〜 2026年08月01日
作成日: 2026-08-01
---

# MCP 公式ドキュメント更新サマリ

```markdown
今回の対象期間は、2026年07月28日に公開された仕様リビジョン `2026-07-28` を受けた記述の整備が中心です。新規追加ページと大幅更新ページはなく、43 ページの軽微な更新にとどまりました。うち 41 ページは SEP ページ群への一斉注記追加で、残りはエラーコードの追従修正とバージョン表記の更新です。

主要なものを以下に挙げます。

1. Final ステータスの SEP ページ 41 件すべてに、採択時点の設計の歴史的記録である旨の注記が追加された
2. Tasks 拡張に残っていたエラーコード `-32003` が、現行仕様の採番に合わせて `-32021` に修正された
3. Versioning ページの現行プロトコルバージョン表記が `2026-07-28` に更新された
```

## ハイライト

1. [**Final SEP への歴史的記録注記の一斉付与**](./latest-detail.md#1-final-sep-への歴史的記録注記の一斉付与):  
  Final ステータスに達した SEP ページ 41 件すべての冒頭に、当該 SEP は採択時点の設計の歴史的記録であり最終化後の変更は反映されない旨の注記が置かれた。SEP Guidelines 側にも同じ方針が明文化されている。
2. [**Tasks 拡張のエラーコードを現行採番に修正**](./latest-detail.md#2-tasks-拡張のエラーコードを現行採番に修正):  
  `2026-07-28` でエラーコード割り当て方針が定められた際に `-32003` から `-32021` へ再採番された Missing Required Client Capability が、Tasks 拡張のページでは旧番号のまま残っていた。3 つの節にまたがる計 4 箇所が現行の `-32021` に修正された。
3. [**現行プロトコルバージョン表記の更新**](./latest-detail.md#3-現行プロトコルバージョン表記の更新):  
  Versioning ページの「Revisions」節で、current として示されるプロトコルバージョンが `2025-11-25` から `2026-07-28` に更新された。

## 新規追加されたページ

今回の対象期間では `llms.txt` のページ一覧に変更がなく、新規追加されたページはありません。

## 大幅に更新されたページ

単一ページで 50 行以上に及ぶ変更はありませんでした。最も変更量の多いページでも 18 行（注記の追加と著者一覧の補完）にとどまります。変更のあった 43 ページはすべて下記「軽微な更新」に整理しています。

## 軽微な更新

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

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-07-28.md](./archives/latest/2026-07-28.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-07-28.md](./archives/latest-detail/2026-07-28.md)

<!--
base_commit: 37f111d9d0c49fa9fd2ab79826f803c7de899551
head_commit: 19822214b48ea654ba58df34a2f03353c8f7a40b
generated_at_full: 2026-08-02T19:32:36+09:00
-->
