---
対象期間: 2026年11月12日 〜 2026年11月13日
作成日: 2026-11-13
---

# MCP 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
今回の対象期間の取り込みは 1 回で、MCP の差分は `llms-full.txt` の追加 94 行・削除 82 行（23 ページ）でした。新規ページも大幅更新もなく、文面が変わったのは Project Policies と Contributor Ladder の 2 ページ（追加 12 行）だけで、残る 21 ページは書式だけの変更です。

主要なものを以下に挙げます。

1. Project Policies に h2「EU Cyber Resilience Act (CRA) stewardship」が加わった。悪用されている脆弱性や重大なインシデントを知ったメンテナーは、Discord の `#security-disclosures` で Core Maintainer か Lead Maintainer にすぐ知らせ、その人が Linux Foundation の CRA steward と連絡を取る。報告する人は、こうした場合も private advisory を使う
2. 21 ページの 81 行で、英数字に挟まれた `\_` のエスケープ（105 か所）がすべて外れた（`claude\_desktop\_config.json` → `claude_desktop_config.json` など）。`\_meta` などの 120 か所は残っている
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**悪用されている脆弱性と重大なインシデントの扱いが Project Policies に書かれた**](#1-悪用されている脆弱性と重大なインシデントの扱いが-project-policies-に書かれた):  
  Project Policies に h2「EU Cyber Resilience Act (CRA) stewardship」が新設された。悪用されている脆弱性や重大なインシデントを知ったメンテナーは、問題を直しながら Discord の `#security-disclosures` で Core Maintainer か Lead Maintainer にすぐ知らせ、その人が Linux Foundation の CRA steward に連絡する。Reporting a vulnerability には、こうした緊急の報告も private advisory で行うという段落が、Contributor Ladder の Escalation には、この規則に従うよう求める段落が加わった。
2. [**21 ページで英数字に挟まれたアンダースコアのエスケープが外れた**](#2-21-ページで英数字に挟まれたアンダースコアのエスケープが外れた):  
  `llms-full.txt` の 21 ページの 81 行で、英数字に挟まれた `\_` が `_` になった。base にあった 105 か所がすべて外れ、ほかの違いはない。語頭の `\_meta` などの 120 か所は残っている。SEP-1686 では強調の書き方が 1 行変わった。どちらも表示される文字は変わらない。
<!-- light:highlight-list:end -->

## 1. 悪用されている脆弱性と重大なインシデントの扱いが Project Policies に書かれた

今回の対象期間の取り込みは 1 回です。MCP の入力ファイルでは本文 `llms-full.txt` だけが変わり（追加 94 行・削除 82 行）、索引 `llms.txt` には差分がありません。`llms-full.txt` の総行数は 45,244 行から 45,256 行になり、収録ページ数（160 件。`examples` が 2 回収録されているため、URL としては 159 件）と索引のエントリ数（365 件）は変わっていません。

差分のあった 23 ページのうち、文面が変わったのは次の 2 ページです。残る 21 ページは書式だけの変更です（ハイライト 2）。

| ページ | 行数 | 追加 | 削除 | 内容 |
|---|---|---|---|---|
| Project Policies | 38 → 48 | 11 | 1 | 文面の追加 10 行（h2 は 6 個から 7 個）。ほかに `\_` のエスケープが外れた 1 組 |
| Contributor Ladder | 162 → 164 | 2 | 0 | 文面の追加 2 行（段落 1 つ） |

行数は、ページのタイトルの行（`# `）から次のページの直前までを数えたものです。

**Reporting a vulnerability。** 公開の issue・discussion・pull request で報告しないという WARNING と、`github.com/modelcontextprotocol/<repo>/security/advisories/new` で private advisory を開く手順の後に、段落が 1 つ加わりました。

- private advisory は、プロジェクトの緊急のセキュリティ報告の仕組みでもある
- 実際に悪用されている脆弱性と重大なインシデントも、影響を受けるリポジトリの private advisory で報告する
- 報告の冒頭に、その脆弱性が実際に悪用されていること、またはインシデントが起きていることを書く

**EU Cyber Resilience Act (CRA) stewardship。** Reporting a vulnerability と Communication and records の間に h2 が新設されました。

- MCP プロジェクトは、公式 SDK を含め、最終的に商業活動に使われることを意図したソフトウェアを公開している。プロジェクトは Linux Foundation の CRA stewardship framework のもとで支援を受けている。CRA がこうしたプロジェクトに求めることについては、Linux Foundation の「CRA guidance for open source projects」を参照するよう案内している
- 悪用されている脆弱性や、リリースの手順が侵害されたような重大なインシデントを知ったメンテナーは、Discord の `#security-disclosures` で Core Maintainer か Lead Maintainer に**すぐに**知らせなければならない。知らせるのは問題を直しながらであって、直す代わりに知らせるのではない
- 知らせを受けた Core Maintainer か Lead Maintainer が、Linux Foundation の CRA steward（`steward@linuxfoundation.org`）に連絡し、以後は steward とやり取りする。プロジェクトが steward に対して一つの声で話すため、とされる
- CRA は steward の報告に短い期限を設けている。まず 24 時間以内に早期警告、次に 72 時間以内により詳しい通知を出す
- advisory がある場合は、プロジェクトが問題を最初に知った時点と、steward に知らせた時点を記録する
- 悪用の証拠が無い脆弱性は、CRA のエスカレーションの対象ではない。ほかのメンテナーは steward に直接連絡せず、報告する人は private advisory を使わなければならない

**Contributor Ladder の Escalation。** エスカレーション先の表（「Security issue」の行は、最初が Core Maintainer、次が Lead Maintainer、応答は Immediate のまま）の後には、脆弱性はまず private advisory で報告し、表のセキュリティの行は報告があった後のメンテナー内のエスカレーションだ、という段落があります。その次に段落が 1 つ加わりました。悪用されている脆弱性や重大なインシデントを知ったメンテナーは、「EU Cyber Resilience Act (CRA) escalation rule」（Project Policies の上の節へのリンク）に従い、問題を直しながら Discord の `#security-disclosures` で Core Maintainer か Lead Maintainer にすぐ知らせる、その Core Maintainer か Lead Maintainer が Linux Foundation の CRA steward と連携する、という内容です。

`llms-full.txt` で `#security-disclosures` という名前が出てくるのは、今回加わったこの 2 か所だけです。Communication ページの Discord の節は、チャンネルの名付け方（`#general`・`#<name>-wg` など）と、プライベートのチャンネルはセキュリティのインシデントなどに限ると説明していますが、このチャンネルの名前は挙げていません。

- [Project Policies - MCP Docs](https://modelcontextprotocol.io/community/policies#eu-cyber-resilience-act-cra-stewardship)
- [Project Policies - MCP Docs](https://modelcontextprotocol.io/community/policies#reporting-a-vulnerability)
- [Contributor Ladder - MCP Docs](https://modelcontextprotocol.io/community/contributor-ladder#escalation)

## 2. 21 ページで英数字に挟まれたアンダースコアのエスケープが外れた

`llms-full.txt` の 21 ページの 81 行で、英数字に挟まれたアンダースコアの前のバックスラッシュが外れました（`\_` → `_`）。例は次のとおりです。

- Build an MCP server・Debugging: `claude\_desktop\_config.json` → `claude_desktop_config.json`
- Client Registration・SEP-991: `client\_id`・`client\_ids` → `client_id`・`client_ids`
- Schema Reference: `"tool\_result"` → `"tool_result"`、`HEADER\_MISMATCH` → `HEADER_MISMATCH`、`notifications/tools/list\_changed` → `notifications/tools/list_changed`

置き換わった 81 組の行は、どれもこの置き換えのほかに違いがありません。base にあった英数字に挟まれた `\_` は 105 か所で、すべて外れ、head には残っていません。英数字に挟まれた `_` は Markdown の強調の区切りにならないので、表示される文字は変わりません。

`\_` は 225 か所から 120 か所に減りました。残る 120 か所は、どれも英数字に挟まれていないものです。

| 残っている `\_` | か所 | ページ |
|---|---|---|
| 語頭の `\_meta` | 115 | Schema Reference 113、SEP-2133・SEP-2575 が各 1 |
| 単独の `\_`（使える文字を並べた文の中） | 4 | SEP-986 が 3、Tools が 1 |
| 語末（Discord の名前 `tadasant\_`） | 1 | Registry Charter |

`\_` が外れたページと、置き換わった行の組数は次のとおりです。

| 区分 | ページ | 組 |
|---|---|---|
| ドキュメント | Build an MCP server | 1 |
| ドキュメント | Debugging | 1 |
| ドキュメント | Protocol eras | 4 |
| ドキュメント | Security Best Practices | 2 |
| 仕様 | Client Registration | 1 |
| 仕様 | Sampling | 2 |
| 仕様 | Schema Reference | 21 |
| コミュニティ | Enterprise Interest Group Charter | 2 |
| コミュニティ | Project Policies | 1 |
| コミュニティ | Inspector V2 Working Group Charter | 1 |
| コミュニティ | Registry Charter | 1 |
| SEP | SEP-985: Align OAuth 2.0 Protected Resource Metadata with RFC 9728 | 2 |
| SEP | SEP-986: Specify Format for Tool Names | 1 |
| SEP | SEP-991: Enable URL-based Client Registration using OAuth Client ID Metadata Documents | 7 |
| SEP | SEP-1036: URL Mode Elicitation for secure out-of-band interactions | 1 |
| SEP | SEP-1577: Sampling With Tools | 2 |
| SEP | SEP-1730: SDKs Tiering System | 4 |
| SEP | SEP-2164: Standardize Resource Not Found Error Code | 7 |
| SEP | SEP-2322: Multi Round-Trip Requests | 17 |
| SEP | SEP-2468: Recommend Issuer (iss) Parameter in MCP Auth Responses | 2 |
| SEP | SEP-2567: Sessionless MCP via Explicit State Handles | 1 |

Project Policies 以外の 20 ページは、この置き換えだけのページです。

このほか、SEP-1686: Tasks の Motivation の Affected Customer Use Cases で、3 番目の Code Migration Workflows の行頭が `***Challenge*:**` から `**_Challenge_:**` になりました。どちらも「Challenge」を斜体にしてコロンまでを太字にする書き方で、表示は同じです。ほかのユースケースの `***Challenge:***` は変わっていません。

書式の変更は合わせて 164 行（`\_` の 81 組 162 行と、SEP-1686 の 1 組 2 行）で、文面の追加 12 行と合わせると、生の差分の 176 行（追加 94・削除 82）になります。

## 新規追加されたページ

<!-- light:new-pages:start -->
今回の対象期間に新たに追加されたページはありません。索引 `llms.txt` に変更はなく、索引のエントリ数（365 件）と本文 `llms-full.txt` の収録ページ数（160 件。URL としては 159 件）はどちらも前回と同じです。
<!-- light:new-pages:end -->

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
今回の対象期間に大幅な更新（本文 50 行以上の変更）があったページはありません。生の差分の行数が最も多い Schema Reference も 42 行（21 組で、すべて `\_` のエスケープ）で、文面の変更が最も多い Project Policies も追加 10 行です。差分のあった 23 ページは、いずれも「軽微な更新」で扱います。
<!-- light:updated-pages:end -->

## 軽微な更新

<!-- light:minor-updates:start -->
今回差分が出たファイルは `llms-full.txt` の 1 件で、差分のあった 23 ページのうち、文面が変わったのは 2 ページ、残る 21 ページは書式だけの変更でした。

**新機能**

- Project Policies に h2「EU Cyber Resilience Act (CRA) stewardship」が加わった。悪用されている脆弱性や重大なインシデントを知ったメンテナーは、問題を直しながら Discord の `#security-disclosures` で Core Maintainer か Lead Maintainer にすぐ知らせ、その人が Linux Foundation の CRA steward に連絡して以後のやり取りを受け持つ（詳細はハイライト 1 参照） — [Project Policies](https://modelcontextprotocol.io/community/policies#eu-cyber-resilience-act-cra-stewardship)

**機能改善**

- Project Policies の Reporting a vulnerability に、private advisory は緊急のセキュリティ報告の仕組みでもあり、悪用されている脆弱性や重大なインシデントもそれで報告して、報告の冒頭にその旨を書く、という段落が加わった（詳細はハイライト 1 参照） — [Project Policies](https://modelcontextprotocol.io/community/policies#reporting-a-vulnerability)
- Contributor Ladder の Escalation に、悪用されている脆弱性や重大なインシデントを知ったメンテナーは Project Policies の CRA のエスカレーションの規則に従う、という段落が加わった（詳細はハイライト 1 参照） — [Contributor Ladder](https://modelcontextprotocol.io/community/contributor-ladder#escalation)

**その他**

- 21 ページの 81 行で、英数字に挟まれた `\_` のエスケープが外れた。表示は変わらない。ドキュメントが 4 ページ（Build an MCP server・Debugging・Protocol eras・Security Best Practices）、仕様が 3 ページ（Client Registration・Sampling・Schema Reference）、コミュニティが 4 ページ（Enterprise Interest Group Charter・Project Policies・Inspector V2 Working Group Charter・Registry Charter）、SEP が 10 ページ（SEP-985・986・991・1036・1577・1730・2164・2322・2468・2567）（詳細はハイライト 2 参照）
- SEP-1686: Tasks の Motivation で、Code Migration Workflows の行頭の強調の書き方が `***Challenge*:**` から `**_Challenge_:**` になった。表示は同じ（詳細はハイライト 2 参照） — [SEP-1686: Tasks](https://modelcontextprotocol.io/seps/1686-tasks#motivation)
<!-- light:minor-updates:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-11-12.md](./archives/latest/2026-11-12.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-11-12.md](./archives/latest-detail/2026-11-12.md)

<!--
base_commit: 77f196ce342a0c6130e111a1fa66ada14d87a243
head_commit: 1e8d14825866e74000053b24496de73f02e2e71f
generated_at_full: 2026-11-14T15:39:58+09:00
-->
