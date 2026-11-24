---
対象期間: 2026年11月21日 〜 2026年11月23日
作成日: 2026-11-23
---

# MCP 公式ドキュメント更新サマリ

```markdown
今回の対象期間の取り込みは 2 回で、MCP の入力ファイルに差分が出たのはそのうち 1 回でした。新規ページが 1 件（Core Primitives Working Group の憲章）加わり、既存ページは 2 件で、WG の一覧からこの憲章ページへのリンクが張られました。

主要なものを以下に挙げます。

1. Core Primitives Working Group の憲章ページが加わった。当面はツールの結果の形（shape）・安定性（stability）・宛先（audience）の 3 つの問題に取り組み、リードは Kurtis Van Gent 氏と David Soria Parra 氏、会合は週 1 回 60 分
2. Working Groups Overview の表の Core Primitives のリンク先が GitHub のリポジトリから憲章ページに変わり、Working Groups and Interest Groups の Current groups の一覧にも Core Primitives が加わって WG は 15 になった
```

## ハイライト

1. [**Core Primitives WG の憲章ページが加わった**](./latest-detail.md#1-core-primitives-wg-の憲章ページが加わった):  
  新しいページ Core Primitives Charter（`community/working-groups/core-primitives`、91 行）が加わり、索引 `llms.txt` にもエントリが入った。ロードマップの Improved Primitives の優先領域に置かれた WG で、当面はツールの結果について、形（`content`・`structuredContent`・`outputSchema`・audience の注釈に形式と宛先が混在している）、安定性（同じツールと入力でも結果のスキーマが変わりうる）、宛先（形式と宛先を分けて扱う）の 3 つに取り組む。ロードマップが割り当てた content annotations の扱いの判断も受け持ち、progressive discovery は対象外として Progressive Disclosure WG に委ねている。リードは Kurtis Van Gent 氏（Google）と David Soria Parra 氏（Anthropic）、会合は週 1 回 60 分。
2. [**WG の一覧 2 ページで Core Primitives が憲章ページにつながった**](./latest-detail.md#2-wg-の一覧-2-ページで-core-primitives-が憲章ページにつながった):  
  Working Groups Overview の表では、Core Primitives の行のリンク先が GitHub の `modelcontextprotocol/core-primitives-wg` から新しい憲章ページ（`/community/working-groups/core-primitives`）に変わった。リード・Discord・Focus の列は変わっていない。Working Groups and Interest Groups の Current groups では、WG の一覧に Core Primitives が MCP Apps と File Uploads の間に加わり、14 から 15 になった。

## 新規追加されたページ

- [**Core Primitives Charter**](./latest-detail.md#1-core-primitives-charter) ([MCP Docs](https://modelcontextprotocol.io/community/working-groups/core-primitives)):  
  Core Primitives Working Group の憲章（91 行）。ツールの結果の形・安定性・宛先の 3 つの問題を対象範囲とし、関連する WG、リーダーシップ、決定権限、運営、作業項目を定めている。索引 `llms.txt` にもエントリが加わった（位置づけはハイライト 1 参照）。

## 大幅に更新されたページ

今回の対象期間に大幅な更新（本文 50 行以上の変更）があった既存ページはありません。既存ページの変更は 2 ページで計 3 行（追加 2 行・削除 1 行）にとどまり、軽微な更新に当たります（ハイライト 2 参照）。

## 軽微な更新

今回差分が出たファイルは `llms.txt` と `llms-full.txt` の 2 件で、新規ページ（Core Primitives Charter）のほかに、次の変更がありました。

**機能改善**

- Working Groups and Interest Groups の Current groups の WG の一覧に、Core Primitives を MCP Apps と File Uploads の間に追加し、WG は 15 になった（詳細はハイライト 2 参照） — [Working Groups and Interest Groups](https://modelcontextprotocol.io/community/working-interest-groups#current-groups)

**その他**

- Working Groups Overview の表で、Core Primitives の行のリンク先を GitHub の `modelcontextprotocol/core-primitives-wg` から新しい憲章ページに変更（詳細はハイライト 2 参照） — [Working Groups Overview](https://modelcontextprotocol.io/community/working-groups/overview)
- 索引 `llms.txt` で、MCP Apps Working Group Charter と File Uploads Charter のエントリの間に Core Primitives Charter のエントリ（説明文「Charter for the MCP Core Primitives Working Group.」）を追加。エントリ数は 364 件から 365 件、ファイルは 369 行から 370 行になった（末尾に改行が無いため、改行の数では 368 から 369） — [Core Primitives Charter](https://modelcontextprotocol.io/community/working-groups/core-primitives)

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-11-21.md](./archives/latest/2026-11-21.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-11-21.md](./archives/latest-detail/2026-11-21.md)

<!--
base_commit: 3279a161e968357548276a7baa091d6d6f481473
head_commit: 6b8844c93bee3ab36c9d7bb656a2476fb661c469
generated_at_full: 2026-11-24T15:29:36+09:00
-->
