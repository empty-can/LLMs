---
対象期間: 2026年11月26日 〜 2026年11月27日
作成日: 2026-11-27
---

# MCP 公式ドキュメント更新サマリ

```markdown
今回の対象期間の取り込みは 1 回で、差分は本文 `llms-full.txt` の 2 ページで計 5 行（追加 4 行・削除 1 行）にとどまり、索引 `llms.txt` は変わりませんでした。拡張の対応表にクライアントが 1 つ加わり、Roadmap の冒頭からリリース周期のページへの案内が張られています。

主要なものを以下に挙げます。

1. Extension Support Matrix の対応表にクライアント OpenCode の行が加わり（Events の列は Partial）、Events の Partial の注記が「ChatGPT は webhook のみ、OpenCode は push のみ」とクライアントごとに書き分けられた
2. Roadmap の冒頭に、仕様のリリースの時期と SEP のリリースへの組み込み方は Release Cycle のページを参照するよう案内する 1 文が加わった
```

## ハイライト

1. [**拡張の対応表に OpenCode が加わり Events の Partial の意味が書き分けられた**](./latest-detail.md#1-拡張の対応表に-opencode-が加わり-events-の-partial-の意味が書き分けられた):  
  Extension Support Matrix の Support matrix の表の末尾（mcp-use の後）に、クライアント OpenCode（リンク先は `opencode.ai`）の行が加わり、クライアントの行は 18 から 19 になった。Events の列は `Partial`（リンク先は GitHub の `anomalyco/opencode` のプルリクエスト #65271）。表の後の注記は、旧版の「Events の Partial は webhook での配信のみを意味する」から、「一部の配信方式のみを意味する。ChatGPT は webhook のみ、OpenCode は push のみ」に書き換わった。
2. [**Roadmap の冒頭から Release Cycle のページへ案内が張られた**](./latest-detail.md#2-roadmap-の冒頭から-release-cycle-のページへ案内が張られた):  
  Roadmap の冒頭の説明の段落の後に、「仕様のリリースがいつ出るか、SEP がどのようにリリースに組み込まれるかは、[release cycle](https://modelcontextprotocol.io/community/release-cycle) を参照」という 1 文が加わった。リリース周期の内容そのものや、Next Release の節、最終更新日（`2026-11-16`）は変わっていない。

## 新規追加されたページ

今回の対象期間に新たに追加されたページはありません。本文 `llms-full.txt` の収録ページ数（165 件。URL としては 164 件）と、索引 `llms.txt`（エントリ 366 件）は前回と同じです。

## 大幅に更新されたページ

今回の対象期間に大幅な更新（本文 50 行以上の変更）があったページはありません。変更は 2 ページで計 5 行（追加 4 行・削除 1 行）にとどまり、軽微な更新に当たります（ハイライト 1 参照）。

## 軽微な更新

今回差分が出たファイルは `llms-full.txt` の 1 件で、既存の 2 ページに次の変更がありました。

**機能改善**

- Extension Support Matrix の Support matrix の表の末尾に、クライアント OpenCode の行を追加（Events の列は `Partial`）し、クライアントは 19 になった（詳細はハイライト 1 参照） — [Extension Support Matrix](https://modelcontextprotocol.io/extensions/client-matrix#support-matrix)
- Extension Support Matrix の注記で、Events の Partial の意味を「webhook での配信のみ」から「一部の配信方式のみ（ChatGPT は webhook のみ、OpenCode は push のみ）」に書き換えた（詳細はハイライト 1 参照） — [Extension Support Matrix](https://modelcontextprotocol.io/extensions/client-matrix#support-matrix)

**その他**

- Roadmap の冒頭に、仕様のリリースの時期と SEP のリリースへの組み込み方について Release Cycle のページを案内する 1 文を追加（詳細はハイライト 2 参照） — [Roadmap](https://modelcontextprotocol.io/development/roadmap)

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-11-26.md](./archives/latest/2026-11-26.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-11-26.md](./archives/latest-detail/2026-11-26.md)

<!--
base_commit: 479f8136ffd1756a957a6892afc01a4896b6be77
head_commit: ff1331b1ac08161c9abe13ea96b72c30b1a450ff
generated_at_full: 2026-11-28T15:10:08+09:00
-->
