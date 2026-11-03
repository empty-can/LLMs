---
対象期間: 2026年10月31日 〜 2026年11月02日
作成日: 2026-11-02
---

# MCP 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
今回の対象期間には取り込みが 2 回あり、MCP に差分が出たのは後の 1 回だけで、`llms-full.txt` の追加 1 行・削除 94 行でした。新規ページも大幅更新もなく、内容の変更は Extension Support Matrix に Glean の行が加わったことだけで、残りは 47 ページの冒頭の空行の整理です。

主要なものを以下に挙げます。

1. Extension Support Matrix の Support matrix に Glean の行が加わり、掲載クライアントは 16 件から 17 件になった（セルは空で、対応する拡張は読み取れない）
2. `llms-full.txt` で、索引に説明文の無い 47 ページの冒頭（`Source:` の行の後）の空行が 3 行から 1 行に詰まった。本文の変更はない
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**Extension Support Matrix に Glean が加わった**](#1-extension-support-matrix-に-glean-が加わった):  
  Support matrix の表の末尾、mcpc MCP CLI の次に Glean の行が加わり、掲載クライアントは 16 件から 17 件になった。ただしセルは 5 列とも空で、どの拡張に対応しているかは `llms-full.txt` からは読み取れない。今回の差分のうち、内容の変更はこの 1 行だけ。
2. [**llms-full.txt で説明文の無い 47 ページの冒頭の空行が詰まった**](#2-llms-fulltxt-で説明文の無い-47-ページの冒頭の空行が詰まった):  
  索引 `llms.txt` で説明文を持たない 47 ページで、`Source:` の行と本文の間の空行が 3 行から 1 行になった。本文の変更はなく、生の差分の削除 94 行はすべてこれ。説明文のあるページはもとから空行 1 行の後に説明文が続く形で、これで全ページの `Source:` の行の直後の空行が 1 行に揃った。
<!-- light:highlight-list:end -->

## 1. Extension Support Matrix に Glean が加わった

今回の対象期間には取り込みが 2 回ありましたが、MCP のファイルに差分が出たのは後の 1 回だけで、差分は本文 `llms-full.txt` の追加 1 行・削除 94 行です。索引 `llms.txt` は変わらず（エントリ数は 364 件のまま）、`llms-full.txt` の総行数は 46,205 行から 46,112 行になり、収録ページ数は 159 件（`examples` が 2 回収録されているため、URL としては 158 件）で変わっていません。追加の 1 行が Extension Support Matrix への追記で、削除の 94 行はすべて 47 ページの空行です（ハイライト 2）。

Extension Support Matrix は、どの MCP クライアントがどの公式拡張に対応しているかをまとめたページです。今回、Support matrix の表の末尾、mcpc MCP CLI の次に、**Glean**（`https://www.glean.com/` へのリンク）の行が加わりました。これで表に並ぶクライアントは 16 件から 17 件になりました。

表のセルは、Skills 列にある 3 件の Partial のリンク（ChatGPT・fast-agent・MCP Inspector）を除いてすべて空で、追加された Glean の行も 5 列（MCP Apps・OAuth Client Credentials・Enterprise Auth・Skills・Tasks）すべてが空です。このため、Glean がどの拡張に対応しているかは `llms-full.txt` からは読み取れません。同じページの Extension overview の表（4 件）、表の後ろの注記、Adding extension support to your client の節には変更がありません。

- [Extension Support Matrix - MCP Docs](https://modelcontextprotocol.io/extensions/client-matrix#support-matrix)

## 2. llms-full.txt で説明文の無い 47 ページの冒頭の空行が詰まった

`llms-full.txt` の各ページは、`# <題>` の行と `Source: <URL>` の行で始まります。これまで、索引 `llms.txt` のエントリに説明文が無いページでは、`Source:` の行と本文の間に空行が 3 行ありました。今回、この空行が 1 行になりました。該当するのは 47 ページで、1 ページあたり 2 行、合わせて 94 行の削除が、生の差分の削除のすべてです。本文には変更がありません。

- **対象**: `llms-full.txt` に収録されたページのうち、索引で説明文を持たないページ 47 件のすべてです。説明文を持つページ（111 件。`examples` の重複を含めて 112 件）には差分がありません。説明文のあるページは、もとから `Source:` の行、空行、説明文の行、空行の順に続く形で、これで全 159 件で `Source:` の行の直後の空行が 1 行に揃いました
- **内訳**: ドキュメント（`docs/2026-07-28/`）が 5 ページ（Getting Started の intro と、Learn の architecture・client-concepts・server-concepts・versioning）、仕様（`specification/2026-07-28/`）が 31 ページ、Registry（`registry/`）が 11 ページです。一覧は「軽微な更新」の「その他」を参照してください

## 新規追加されたページ

<!-- light:new-pages:start -->
今回の対象期間に新たに追加されたページはありません。索引 `llms.txt` に変更はなく、索引側のエントリ数（364 件）と本文 `llms-full.txt` の収録ページ数（159 件。URL としては 158 件）はどちらも前回と同じです。
<!-- light:new-pages:end -->

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
今回の対象期間に大幅な更新（本文 50 行以上の変更）があったページはありません。差分が出た 48 ページは、Extension Support Matrix の追加 1 行と、47 ページの各削除 2 行（空行）だけで、いずれも「軽微な更新」で扱います。
<!-- light:updated-pages:end -->

## 軽微な更新

<!-- light:minor-updates:start -->
今回差分が出たファイルは `llms-full.txt` の 1 件で、差分のあった 48 ページのうち、内容が変わったのは 1 ページ、残る 47 ページは空行の整理だけでした。

**機能改善**

- Extension Support Matrix の Support matrix の末尾（mcpc MCP CLI の次）に Glean の行を追加。掲載クライアントは 16 件から 17 件になった。追加された行のセルは 5 列とも空（詳細はハイライト 1 参照） — [Extension Support Matrix](https://modelcontextprotocol.io/extensions/client-matrix#support-matrix)

**その他**

- **空行の整理だけのページ**（詳細はハイライト 2 参照）: 次の 47 ページは、`Source:` の行の後の空行が 3 行から 1 行になっただけで、内容は変わっていません。ドキュメント（`docs/2026-07-28/` 配下）の 5 ページ: `getting-started/intro`・`learn/architecture`・`learn/client-concepts`・`learn/server-concepts`・`learn/versioning`。仕様（`specification/2026-07-28/` 配下）の 31 ページ: `architecture/index`・`basic/authorization/authorization-server-discovery`・`basic/authorization/client-registration`・`basic/authorization/index`・`basic/authorization/security-considerations`・`basic/index`・`basic/patterns/cancellation`・`basic/patterns/index`・`basic/patterns/mrtr`・`basic/patterns/progress`・`basic/patterns/subscriptions`・`basic/transports/index`・`basic/transports/stdio`・`basic/transports/streamable-http`・`basic/versioning`・`changelog`・`client/elicitation`・`client/roots`・`client/sampling`・`deprecated`・`index`・`schema`・`server/discover`・`server/index`・`server/prompts`・`server/resources`・`server/tools`・`server/utilities/caching`・`server/utilities/completion`・`server/utilities/logging`・`server/utilities/pagination`。Registry（`registry/` 配下）の 11 ページ: `about`・`authentication`・`faq`・`github-actions`・`moderation-policy`・`package-types`・`quickstart`・`registry-aggregators`・`remote-servers`・`terms-of-service`・`versioning`
<!-- light:minor-updates:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-10-31.md](./archives/latest/2026-10-31.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-10-31.md](./archives/latest-detail/2026-10-31.md)

<!--
base_commit: 40e270212cf60c02b47a1f36e25f55319f572f41
head_commit: acb459e04e57acda73f439e58d2759ea5599cdf6
generated_at_full: 2026-11-03T15:35:34+09:00
-->
