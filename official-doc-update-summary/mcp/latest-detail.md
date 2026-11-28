---
対象期間: 2026年11月26日 〜 2026年11月27日
作成日: 2026-11-27
---

# MCP 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
今回の対象期間の取り込みは 1 回で、差分は本文 `llms-full.txt` の 2 ページで計 5 行（追加 4 行・削除 1 行）にとどまり、索引 `llms.txt` は変わりませんでした。拡張の対応表にクライアントが 1 つ加わり、Roadmap の冒頭からリリース周期のページへの案内が張られています。

主要なものを以下に挙げます。

1. Extension Support Matrix の対応表にクライアント OpenCode の行が加わり（Events の列は Partial）、Events の Partial の注記が「ChatGPT は webhook のみ、OpenCode は push のみ」とクライアントごとに書き分けられた
2. Roadmap の冒頭に、仕様のリリースの時期と SEP のリリースへの組み込み方は Release Cycle のページを参照するよう案内する 1 文が加わった
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**拡張の対応表に OpenCode が加わり Events の Partial の意味が書き分けられた**](#1-拡張の対応表に-opencode-が加わり-events-の-partial-の意味が書き分けられた):  
  Extension Support Matrix の Support matrix の表の末尾（mcp-use の後）に、クライアント OpenCode（リンク先は `opencode.ai`）の行が加わり、クライアントの行は 18 から 19 になった。Events の列は `Partial`（リンク先は GitHub の `anomalyco/opencode` のプルリクエスト #65271）。表の後の注記は、旧版の「Events の Partial は webhook での配信のみを意味する」から、「一部の配信方式のみを意味する。ChatGPT は webhook のみ、OpenCode は push のみ」に書き換わった。
2. [**Roadmap の冒頭から Release Cycle のページへ案内が張られた**](#2-roadmap-の冒頭から-release-cycle-のページへ案内が張られた):  
  Roadmap の冒頭の説明の段落の後に、「仕様のリリースがいつ出るか、SEP がどのようにリリースに組み込まれるかは、[release cycle](https://modelcontextprotocol.io/community/release-cycle) を参照」という 1 文が加わった。リリース周期の内容そのものや、Next Release の節、最終更新日（`2026-11-16`）は変わっていない。
<!-- light:highlight-list:end -->

## 1. 拡張の対応表に OpenCode が加わり Events の Partial の意味が書き分けられた

今回の対象期間の取り込みは 1 回（2026年11月28日の実行分）で、差分が出たのは本文 `llms-full.txt` だけでした（追加 4 行・削除 1 行）。総行数は 47,974 行から 47,977 行になり、収録ページ数（165 件。`examples` が 2 回収録されているため、URL としては 164 件）は変わっていません。索引 `llms.txt` には差分がありません（エントリ 366 件のまま）。変更のあった 2 ページはいずれも 50 行未満の変更で、軽微な更新に当たります。

| ページ | 行数 | 追加 | 削除 | 主な変更 |
|---|---|---|---|---|
| Extension Support Matrix | 64 → 65 | 2 | 1 | OpenCode の行の追加と、Events の Partial の注記の書き換え（このハイライト） |
| Roadmap | 109 → 111 | 2 | 0 | Release Cycle のページへの案内の 1 文の追加（ハイライト 2） |
| 計 | | 4 | 1 | |

行数は、ページのタイトルの行（`# `）から次のページの直前までを数えたものです。

**OpenCode の行の追加**: Extension Support Matrix（64 行から 65 行）の Support matrix の表で、末尾（mcp-use の後）にクライアント OpenCode の行が加わり、クライアントの行は 18 から 19 になりました。クライアント名のリンク先は `https://opencode.ai/` です。6 つの拡張の列（MCP Apps・OAuth Client Credentials・Enterprise Auth・Skills・Tasks・Events）のうち、Events の列に `Partial` が入り、そのリンク先は GitHub の `anomalyco/opencode` リポジトリのプルリクエスト #65271 です。これで Events の列に `Partial` があるクライアントは、ChatGPT と OpenCode の 2 つになりました。

**Events の Partial の注記**: 表の後の 1 つめの注記の最初の文が、次のように書き換わりました。

| | 原文 |
|---|---|
| 旧 | Events support marked **Partial** means webhook delivery only. |
| 新 | Events support marked **Partial** means only some delivery modes: webhook only for ChatGPT, and push only for OpenCode. |

旧版では Partial を一律に「webhook での配信のみ」としていましたが、push だけに対応する OpenCode が加わったため、Partial を「一部の配信方式のみ」と定義し直し、クライアントごとに対応する方式を書き分けています。Events の拡張は、上流のイベントを poll・push・webhook のいずれかで受け取る拡張です（Extension overview の表の説明）。注記の残りの 2 文（チェックの付いたクライアントは poll・push・webhook のすべての配信に対応すること、これらの実装の多くは SEP-3415 が Final になる前のもので、仕様の草案に沿っていること）は変わっていません。

なお、2026年10月20日のサマリで書いたとおり、`llms-full.txt` の書式が変わってから、この表では対応を示すチェックマークが出力されていません。OpenCode の行の Events 以外の 5 つのセルは空ですが、空のセルが非対応を意味するとは限らず、`llms-full.txt` から読み取れるのはリンク付きの `Partial` だけです。同じ理由で、注記がいう「チェックの付いたクライアント」がどれかも `llms-full.txt` からは読み取れません。Extension overview の表と、2 つめの注記（認可の拡張の対応状況は別に管理されている）は変わっていません。

- [Extension Support Matrix - MCP Docs](https://modelcontextprotocol.io/extensions/client-matrix#support-matrix)

## 2. Roadmap の冒頭から Release Cycle のページへ案内が張られた

Roadmap（109 行から 111 行、追加 2 行）では、冒頭の説明の段落（このページは今後 6〜12 か月の Core Maintainer のプロトコルの展望を示し、次の仕様の更新とその先に向けた目標と、Working Group と Interest Group からの成果物を述べる）の後、「このロードマップは確定した約束ではなく現時点の考えを示す」という注記の前に、次の 1 文（と空行）が加わりました。

> For when specification releases ship and how SEPs are scheduled into them, see the [release cycle](/community/release-cycle).

仕様のリリースがいつ出るか、SEP がどのようにリリースに組み込まれるかは、Release Cycle のページ（`community/release-cycle`。前回の対象期間に新規追加）を見るよう案内するものです。Roadmap では、前回の対象期間に加わった Next Release の節でも既に「6 か月のリリース周期」として同じページにリンクしており、今回はページの冒頭にも案内が置かれた形です。最終更新日の注記（`2026-11-16`）、Next Release の節、SEP Prioritization 以下の節は変わっていません。

- [Roadmap - MCP Docs](https://modelcontextprotocol.io/development/roadmap)

## 新規追加されたページ

<!-- light:new-pages:start -->
今回の対象期間に新たに追加されたページはありません。本文 `llms-full.txt` の収録ページ数（165 件。URL としては 164 件）と、索引 `llms.txt`（エントリ 366 件）は前回と同じです。
<!-- light:new-pages:end -->

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
今回の対象期間に大幅な更新（本文 50 行以上の変更）があったページはありません。変更は 2 ページで計 5 行（追加 4 行・削除 1 行）にとどまり、軽微な更新に当たります（ハイライト 1 参照）。
<!-- light:updated-pages:end -->

## 軽微な更新

<!-- light:minor-updates:start -->
今回差分が出たファイルは `llms-full.txt` の 1 件で、既存の 2 ページに次の変更がありました。

**機能改善**

- Extension Support Matrix の Support matrix の表の末尾に、クライアント OpenCode の行を追加（Events の列は `Partial`）し、クライアントは 19 になった（詳細はハイライト 1 参照） — [Extension Support Matrix](https://modelcontextprotocol.io/extensions/client-matrix#support-matrix)
- Extension Support Matrix の注記で、Events の Partial の意味を「webhook での配信のみ」から「一部の配信方式のみ（ChatGPT は webhook のみ、OpenCode は push のみ）」に書き換えた（詳細はハイライト 1 参照） — [Extension Support Matrix](https://modelcontextprotocol.io/extensions/client-matrix#support-matrix)

**その他**

- Roadmap の冒頭に、仕様のリリースの時期と SEP のリリースへの組み込み方について Release Cycle のページを案内する 1 文を追加（詳細はハイライト 2 参照） — [Roadmap](https://modelcontextprotocol.io/development/roadmap)
<!-- light:minor-updates:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-11-26.md](./archives/latest/2026-11-26.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-11-26.md](./archives/latest-detail/2026-11-26.md)

<!--
base_commit: 479f8136ffd1756a957a6892afc01a4896b6be77
head_commit: ff1331b1ac08161c9abe13ea96b72c30b1a450ff
generated_at_full: 2026-11-28T15:10:08+09:00
-->
