---
対象期間: 2026年10月17日 〜 2026年10月20日
作成日: 2026-10-20
---

# MCP 公式ドキュメント更新サマリ

```markdown
今回の差分の大半は、本文 `llms-full.txt` の生成形式が MDX のコンポーネントから GitHub 風の Markdown に変わったことによるもので、157 ページ中 136 ページに差分が出ました（追加 9,821 行・削除 10,130 行）。内容が変わったのは、コミュニティのグループ再編で新しい URL に移った 2 つの憲章と、それを参照する 6 ページだけです。Agents Working Group が Interest Group に転換し、Tasks の所管は Triggers and Events Working Group 改め Tasks and Events Working Group に移りました。

主要なものを以下に挙げます。

1. `llms-full.txt` の書式が MDX から Markdown に変わり（コールアウトは `> [!NOTE]` など）、カードのリンク先や画像の URL が読めるようになった。一方、Extensions の Support matrix ではチェックマーク 15 個が消え、対応状況が読めなくなった
2. Agents WG が 2026年10月16日 付けで Interest Group に転換し、憲章の URL が `community/interest-groups/agents` に移った。Tasks の所管が外れ、リード 2 名はファシリテーター 1 名になり、WG 専用の意思決定権限の表なども無くなった
3. Triggers and Events WG が同じ日付で Tasks and Events WG に改称し（URL は `community/working-groups/tasks-events`）、Tasks の安定化とコアプロトコルへの昇格を引き継いだ。リードは 4 名になり、他の 6 ページの参照も新しい名称に追従した
```

## ハイライト

1. [**llms-full.txt の書式が MDX から Markdown に変わり Support matrix のチェックマークが消えた**](./latest-detail.md#1-llms-fulltxt-の書式が-mdx-から-markdown-に変わり-support-matrix-のチェックマークが消えた):  
  `llms-full.txt` の生成形式が変わり、`<Note>`・`<Steps>`・`<Tabs>`・`<Card>`・`<Badge>` などの MDX のコンポーネントが GitHub 風の Markdown（`> [!NOTE]` のコールアウト、太字の行、リンク、URL 付きの画像）に置き換わった。157 ページ中 136 ページに差分が出たが、正規化して比べると内容の変更ではない。ただし `extensions/client-matrix` の Support matrix では `<CHECK />` が 15 個とも消え、対応を示すセルが空になった。
2. [**Agents WG が Interest Group に転換し Tasks の所管を手放した**](./latest-detail.md#2-agents-wg-が-interest-group-に転換し-tasks-の所管を手放した):  
  Agents の憲章が `community/working-groups/agents` から `community/interest-groups/agents` に移り、Group Type が Interest Group になった。Changelog には 2026年10月16日 付けで「Interest Group に転換し、Tasks の所管を Tasks and Events WG に移した」旨の行が加わった。In Scope から Tasks の項目が外れ、Lead 2 名はファシリテーター 1 名（Luca Chang）になり、WG 専用の節は Interest Group 向けの構成に改められた。
3. [**Triggers and Events WG が Tasks and Events WG に改称し Tasks を引き継いだ**](./latest-detail.md#3-triggers-and-events-wg-が-tasks-and-events-wg-に改称し-tasks-を引き継いだ):  
  Triggers and Events の憲章が `community/working-groups/tasks-events` に移り、グループは Tasks and Events Working Group に改称した。旧 Agents WG の憲章にあった Tasks の安定化とコアプロトコルへの昇格、Tasks 拡張のリポジトリと SEP-2663 への参照、関連する作業項目と成功基準がこちらに移り、Luca Chang と Caitie McCaffrey が加わってリードは 4 名になった。Transports WG・Roadmap など 6 ページの参照も新しい名称に追従した。

## 新規追加されたページ

今回の対象期間に新しい URL で収録されたページは次の 2 件です。いずれも既存の憲章が改称・転換に伴って URL を移したもので、旧 URL の本文は同時に削除されました（「軽微な更新」参照）。索引 `llms.txt` のエントリ数（362 件）と `llms-full.txt` の収録ページ数（157 件）は変わっていません。

- [**Agents Charter**](./latest-detail.md#1-agents-charter) ([MCP Docs](https://modelcontextprotocol.io/community/interest-groups/agents)):  
  Agents Interest Group の憲章（111 行、区切りの空行を含む）。旧 `community/working-groups/agents` の Agents WG の憲章を Interest Group に転換したもので、Tasks の所管が外れ、ファシリテーター 1 名と、Discussion Topics・Planned Outputs の構成になった（変更点はハイライト 2 参照）。
- [**Tasks and Events Charter**](./latest-detail.md#2-tasks-and-events-charter) ([MCP Docs](https://modelcontextprotocol.io/community/working-groups/tasks-events)):  
  Tasks and Events Working Group の憲章（115 行、区切りの空行を含む）。旧 `community/working-groups/triggers-events` の Triggers and Events WG を改称したもので、Tasks の安定化を引き継ぎ、リード 4 名と Membership の表が加わった（変更点はハイライト 3 参照）。

## 大幅に更新されたページ

今回の対象期間に大幅な更新（本文 50 行以上の変更）があった既存ページはありません。生の差分では `specification/2026-07-28/schema`（追加 1,406 行・削除 1,065 行）をはじめ多くのページが 50 行を超えますが、いずれも書式の変換によるもので、正規化すると本文に変化はありません（ハイライト 1 参照）。旧 URL の 2 ページの本文削除は、新しい URL へ移ったことによるもので、「軽微な更新」で扱います。

## 軽微な更新

今回差分が出たファイルは `llms-full.txt` と `llms.txt` の 2 件です。新しい URL の 2 ページは「新規追加されたページ」で扱い、ここでは残る変更を挙げます。

**その他**

- `llms-full.txt` の書式を MDX のコンポーネントから GitHub 風の Markdown に変更。157 ページ中 136 ページに差分が出たが、内容の変更ではない。Extensions の Support matrix のチェックマーク 15 個は失われた（詳細はハイライト 1 参照） — [Extension Support Matrix](https://modelcontextprotocol.io/extensions/client-matrix#support-matrix)
- 旧 Agents Charter（`community/working-groups/agents`）の本文 146 行（区切りの空行を含む）を削除。Interest Group への転換に伴い `community/interest-groups/agents` へ移った（詳細はハイライト 2 参照）
- 旧 Triggers and Events Charter（`community/working-groups/triggers-events`）の本文 85 行（区切りの空行を含む）を削除。改称に伴い `community/working-groups/tasks-events` へ移った（詳細はハイライト 3 参照）
- 索引 `llms.txt` で、Agents Charter のエントリを Interest Group の並びへ移し、Triggers and Events Charter のエントリを Tasks and Events Charter に差し替え（追加 2 行・削除 2 行）。エントリ数は 362 件のままで、`community/working-groups/` 配下は 14 件から 13 件に、`community/interest-groups/` 配下は 7 件から 8 件になった。`llms-full.txt` の内訳も同じく 13 件・8 件になっている
- Transports WG の憲章の Related Groups で、Agents WG と Triggers and Events WG の 2 項目を Tasks and Events WG の 1 項目に統合（詳細はハイライト 3 参照） — [Transports Charter](https://modelcontextprotocol.io/community/working-groups/transports#related-groups)
- Roadmap の「Agentic Messaging Primitives」で、サーバー起点のイベントの担当を Tasks & Events WG に、コンポジションのレビューを Tasks & Events・Transports の両 WG と Agents IG に改めた。ページ冒頭の更新日（2026年08月22日）は据え置き（詳細はハイライト 3 参照） — [Roadmap](https://modelcontextprotocol.io/development/roadmap#1-agentic-messaging-primitives)
- Scientific Computing IG の憲章の Related Groups で、Tasks に関する連携先のリンクを Agents WG から Tasks and Events WG に変更 — [Scientific Computing Charter](https://modelcontextprotocol.io/community/interest-groups/scientific-computing#related-groups)
- Authorization IG の憲章の Related Groups で、「Agents WG」の表記を「Agents IG」に変更 — [Authorization Charter](https://modelcontextprotocol.io/community/interest-groups/auth#related-groups)
- Filesystems WG の憲章の Related Groups で、「Agents WG」の表記を「Agents IG」に変更 — [Filesystems Charter](https://modelcontextprotocol.io/community/working-groups/filesystems#related-groups)
- Skills Over MCP WG の憲章の In Scope（Cross-Cutting Concerns）と Related Groups の 2 箇所で、「Agents WG」の表記を「Agents IG」に変更 — [Skills Over MCP Charter](https://modelcontextprotocol.io/community/working-groups/skills-over-mcp#related-groups)

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-10-17.md](./archives/latest/2026-10-17.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-10-17.md](./archives/latest-detail/2026-10-17.md)

<!--
base_commit: df8be8b99ca6342f63f7c7b52da55b4609b1c128
head_commit: 9a810fc542230f7d1d5e0e958b239a460a6d260f
generated_at_full: 2026-10-21T15:42:08+09:00
-->
