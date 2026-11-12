---
対象期間: 2026年11月10日 〜 2026年11月11日
作成日: 2026-11-11
---

# MCP 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
今回の対象期間の取り込みは 1 回で、新規ページが 1 件と、既存の 4 ページの小さな変更がありました（`llms-full.txt` は追加 32 行・削除 10 行、索引 `llms.txt` は追加 1 行）。50 行以上の更新はありません。

主要なものを以下に挙げます。

1. ワーキンググループ 14 件の Leads・Discord のチャンネル・Focus を 1 つの表にまとめた Working Groups Overview のページが加わった
2. Extension Support Matrix で、MCP Inspector の行の MCP Apps 列に、リンク付きの `Partial` が入った
3. Security IG の憲章の Discussion Topics から、SEP-2809（Attested Tool-Server Admission）の行がなくなった
4. Transports WG の憲章が、上流リポジトリの `CHARTER.md` と `docs/` を指さなくなり、参照先が `proposals/` などに替わった
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**ワーキンググループを一覧するページが新設された**](#1-ワーキンググループを一覧するページが新設された):  
  Working Groups Overview（`community/working-groups/overview`、25 行）が索引と本文に加わった。活動中のワーキンググループ 14 件を、Leads・Discord・Focus の列を持つ 1 つの表にまとめている。並んでいるグループは、Working Groups and Interest Groups の Current groups にある 14 件と同じ。
2. [**Extension Support Matrix で MCP Inspector の MCP Apps 列に Partial が入った**](#2-extension-support-matrix-で-mcp-inspector-の-mcp-apps-列に-partial-が入った):  
  Support matrix の MCP Inspector の行で、空だった MCP Apps 列に、Inspector リポジトリの `docs/mcp-app-review.md` へリンクした `Partial` が入った。Skills 列の `Partial` は前からある。
3. [**Security IG の議題表から SEP-2809 の行がなくなった**](#3-security-ig-の議題表から-sep-2809-の行がなくなった):  
  Security Charter の Discussion Topics の表から、SEP-2809「Attested Tool-Server Admission (ATSA)」（Draft）の行が消え、議題は 6 件から 5 件になった。Changelog に行は足されていない。
4. [**Transports 憲章の上流リポジトリへの参照先が替わった**](#4-transports-憲章の上流リポジトリへの参照先が替わった):  
  Transports Charter で、上流リポジトリ `transports-wg` の `CHARTER.md` と `docs/` へのリンクがなくなった。補助資料の置き場所は `proposals/` に、範囲の補足の参照先はリポジトリのトップの `#mission` に替わり、Resources の 2 つのリンクは「Proposals and decision records」の 1 つにまとまった。
<!-- light:highlight-list:end -->

## 1. ワーキンググループを一覧するページが新設された

今回の対象期間の取り込みは 1 回で、MCP の索引 `llms.txt`（追加 1 行）と本文 `llms-full.txt`（追加 32 行・削除 10 行）の両方に差分がありました。`llms-full.txt` の総行数は 44,925 行から 44,947 行に、収録ページ数は 159 件から 160 件（`examples` が 2 回収録されているため、URL としては 158 件から 159 件）に、索引のエントリ数は 364 件から 365 件になっています。差分のあったページは 5 件です。

| ページ | 行数 | 追加 | 削除 | 扱い |
|---|---|---|---|---|
| Working Groups Overview | 新規 → 25 | 25 | 0 | 新規追加（ハイライト 1） |
| Extension Support Matrix | 58 → 58 | 1 | 1 | 軽微な更新（ハイライト 2） |
| Security Charter | 137 → 136 | 0 | 1 | 軽微な更新（ハイライト 3） |
| Transports Charter | 153 → 151 | 5 | 7 | 軽微な更新（ハイライト 4） |
| Governance Working Group Charter | 185 → 185 | 1 | 1 | 軽微な更新 |

行数は、ページのタイトルの行（`# `）から次のページの直前までを数えたものです。5 ページの追加・削除の合計は、`llms-full.txt` 全体の差分（追加 32 行・削除 10 行）と一致します。

新しいページは Working Groups Overview（`community/working-groups/overview`）で、説明文は「Current MCP working groups, their leads, channels, and focus.」です。本文はまず、ワーキンググループは SEP・拡張・コードのような具体的な成果を出すもので、それぞれが範囲・Leads・運営を定めた憲章のもとで動く、と述べます。続けて、このページは活動中のワーキンググループを一覧するものであり、グループの仕組みや参加・設立の方法は Working groups and interest groups のページに、憲章の出し方は charter template にある、と案内しています。

本体は Working group・Leads・Discord・Focus の 4 列の表で、次の 14 件がアルファベット順に並びます。

- Apps・File Uploads・Filesystems・Governance・Infrastructure・Inspector V2・Interceptors
- Progressive Disclosure・Registry・SDK・Server Card・Skills Over MCP・Tasks and Events・Transports

各列の内容は次のとおりです。

- **Working group**: 各グループの憲章へのリンク
- **Leads**: GitHub のプロフィールへリンクした名前。各憲章の Leadership の節で Lead とされている人と同じで、Progressive Disclosure だけは、憲章で Facilitator とされている 2 人が挙がっている
- **Discord**: チャンネル名。Infrastructure・Interceptors・Tasks and Events の 3 件は「Not listed yet」
- **Focus**: 1 行の説明。たとえば Transports は「Evolving transport bindings and transport-adjacent protocol architecture」

並んでいるグループは、Working Groups and Interest Groups の Current groups にあるワーキンググループの一覧（14 件）と同じです（Current groups では Apps を「MCP Apps」と書いています）。Current groups 自体は今回変わっておらず、この新しいページへのリンクもありません。`llms-full.txt` の中でこのページを指すリンクは、まだどこにもありません。憲章の出し方を書いた Group Charter Template も、新しいグループは Current groups に 1 行を足すよう求めたままです。interest group について同じような一覧ページは、索引にありません。

索引では Group Charter Template と MCP Apps Working Group Charter の間、つまりワーキンググループの憲章の並びの先頭に入りました。本文では、パスのアルファベット順どおり Interceptors Charter と Progressive Disclosure Charter の間に収録されています。

- [Working Groups Overview - MCP Docs](https://modelcontextprotocol.io/community/working-groups/overview)
- [Working Groups and Interest Groups - MCP Docs](https://modelcontextprotocol.io/community/working-interest-groups#current-groups)

## 2. Extension Support Matrix で MCP Inspector の MCP Apps 列に Partial が入った

Extension Support Matrix の Support matrix で、MCP Inspector の行が書き換わりました。MCP Apps 列は空でしたが、今回 `Partial` が入り、Inspector のリポジトリの `docs/mcp-app-review.md`（`https://github.com/modelcontextprotocol/inspector/blob/main/docs/mcp-app-review.md`）へリンクしています。Skills 列の `Partial`（CLI の README の `#skill-verification---verify` へのリンク）は前からあり、変わっていません。リンク先の文書の中身は、今回の入力からは確認できません。

なお、2026年10月20日のサマリで書いたとおり、`llms-full.txt` の書式が変わってから、この表では対応を示すチェックマークが出力されていません。空のセルが非対応を意味するとは限らず、`llms-full.txt` から読み取れるのはリンク付きの `Partial` だけです。

- [Extension Support Matrix - MCP Docs](https://modelcontextprotocol.io/extensions/client-matrix#support-matrix)

## 3. Security IG の議題表から SEP-2809 の行がなくなった

Security Charter（Security Interest Group の憲章）の Discussion Topics の表から、次の行がなくなりました。

| Item | Name | Status | Champion |
|---|---|---|---|
| SEP-2809（PR へのリンク） | Attested Tool-Server Admission (ATSA) | Draft | `@metereconsulting` |

これで表は 6 件から 5 件になり、残るのは SDK vulnerability disclosure（In progress、Champion は Facilitators）と、Open の 4 件です。Open の 4 件は、承認後の `list_changed` の意味（runtime drift）、サプライチェーンの完全性、サーバーをまたぐツールの識別、Tool Annotations IG と合同の capability declarations です。Item の列に SEP が書かれた行は、これでなくなりました。

行がなくなった理由は書かれておらず、Changelog の最新の行も 2026年08月26日（routing group への再編）のままです。SEP-2809 という番号は、`llms-full.txt` のどこにも出てこなくなりました。2026年06月16日のサマリでは、IG が新設されたときの議題の 1 つとしてこの SEP を挙げていました。

- [Security Charter - MCP Docs](https://modelcontextprotocol.io/community/interest-groups/security#discussion-topics)

## 4. Transports 憲章の上流リポジトリへの参照先が替わった

Transports Charter で、上流のリポジトリ `modelcontextprotocol/transports-wg` を指すリンクが、次の 4 か所で書き換わりました。

| 箇所 | これまで | 今回 |
|---|---|---|
| Mission Statement | working group repository とその upstream charter（`CHARTER.md`）が、技術的な焦点・提案の方針・補足の詳細を保つ | working group repository が保つ |
| In Scope の Validation and Guidance | 補助資料は upstream の documentation（`tree/main/docs`）に置く | 補助資料は upstream の proposals directory（`tree/main/proposals`）に置く |
| In Scope の直後の段落 | upstream の scope statement（`CHARTER.md#scope`）は補足の文脈であり、憲章の境界を広げられない | upstream の mission statement（リポジトリのトップの `#mission`）が同じ扱い |
| Resources | リポジトリの下に Proposals（`proposals`）と Supporting documentation and decision records（`docs`）の 2 つ | Proposals and decision records（`proposals`）の 1 つ |

これでこの憲章から、`CHARTER.md` と `docs/` へのリンクはなくなりました。上流のメンバー名簿（`GOVERNANCE.md#members`）、open な PR、`roadmaps/` と `meetings/` へのリンクは残っています。上流の側で何が変わったのかは、今回の入力からは分かりません。Changelog は 2026年08月23日の初版の行だけで、今回の変更は記録されていません。

2026年08月26日のサマリは、この憲章が技術的な詳細を上流の `CHARTER.md` に任せていると書きましたが、その記述はもう当てはまりません。なお、SEP-2575: Make MCP Stateless のページには、`transports-wg` の `docs/` 配下の文書（`sessions-vs-sessionless-decision.md`）へのリンクが残っています。

- [Transports Charter - MCP Docs](https://modelcontextprotocol.io/community/working-groups/transports#scope)

## 新規追加されたページ

<!-- light:new-pages:start -->
- [**Working Groups Overview**](#1-working-groups-overview) ([MCP Docs](https://modelcontextprotocol.io/community/working-groups/overview)):  
  活動中のワーキンググループ 14 件を、Leads・Discord のチャンネル・Focus とともに 1 つの表で一覧するページ（詳細はハイライト 1 参照）。
<!-- light:new-pages:end -->

## 1. Working Groups Overview

`community/working-groups/overview` に置かれた 25 行のページで、索引の説明文は「Current MCP working groups, their leads, channels, and focus.」です。短い前書きのあと、Working group・Leads・Discord・Focus の 4 列の表に 14 件のワーキンググループが並びます。グループの仕組み・参加・設立については Working groups and interest groups のページへ、憲章の出し方については charter template へ案内しています。

並んでいるのは Working Groups and Interest Groups の Current groups と同じ 14 件で、Discord が「Not listed yet」なのは Infrastructure・Interceptors・Tasks and Events の 3 件です。interest group を一覧するページはありません（詳細はハイライト 1 参照）。

- [Working Groups Overview - MCP Docs](https://modelcontextprotocol.io/community/working-groups/overview)

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
*(大幅に更新されたページはありません)*
<!-- light:updated-pages:end -->

## 軽微な更新

<!-- light:minor-updates:start -->
既存のページで差分があったのは 4 件で、いずれも追加・削除とも 10 行未満です。ハイライトで扱った 3 ページのほかに、Governance WG の憲章でリンク先のアンカーが替わりました。

**機能改善**

- Extension Support Matrix の Support matrix で、MCP Inspector の MCP Apps 列に、`docs/mcp-app-review.md` へリンクした `Partial` が入った（詳細はハイライト 2 参照） — [Extension Support Matrix](https://modelcontextprotocol.io/extensions/client-matrix#support-matrix)

**その他**

- Security Charter の Discussion Topics から、SEP-2809「Attested Tool-Server Admission (ATSA)」の行がなくなった（詳細はハイライト 3 参照） — [Security Charter](https://modelcontextprotocol.io/community/interest-groups/security#discussion-topics)
- Transports Charter で、上流リポジトリの `CHARTER.md` と `docs/` へのリンクがなくなり、参照先が `proposals/` とリポジトリのトップの `#mission` に替わった。Resources の 2 つのリンクは 1 つにまとまった（詳細はハイライト 4 参照） — [Transports Charter](https://modelcontextprotocol.io/community/working-groups/transports#scope)
- Governance Working Group Charter の Charter Updates で、改訂の手順を指すリンクの文言が「Charter Amendments」から「charter amendment」に、リンク先が `/community/working-interest-groups#charter-amendments` から `#amending-or-retiring-a-group` に替わった。リンク先は、Working Groups and Interest Groups に前回の時点からある見出し「Amending or retiring a group」 — [Governance Working Group Charter](https://modelcontextprotocol.io/community/working-groups/governance#charter-updates)
<!-- light:minor-updates:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-11-10.md](./archives/latest/2026-11-10.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-11-10.md](./archives/latest-detail/2026-11-10.md)

<!--
base_commit: 5ed60081bc6921a82747ac292a0c99583f7521e4
head_commit: c85f1a228a539e3f1157cb0caf9aea01e5add4d1
generated_at_full: 2026-11-12T15:19:05+09:00
-->
