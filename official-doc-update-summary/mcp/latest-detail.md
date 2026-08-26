---
対象期間: 2026年08月24日 〜 2026年08月25日
作成日: 2026-08-25
---

# MCP 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
今回の対象期間に差分が出たのは索引ファイル `llms.txt` の 1 件のみで、ページ本文を収める `llms-full.txt` には変更がありません。索引の収録範囲が現行プロトコルバージョンのみから全リビジョンへ拡大し、エントリは 144 件から 348 件になりました。

主要なものを以下に挙げます。

1. 索引 `llms.txt` の収録範囲が、現行バージョン 2026-07-28 のドキュメント／仕様だけだったところから、過去の確定版 4 系統（2025-11-25 / 2025-06-18 / 2025-03-26 / 2024-11-05）と draft を加えた全リビジョンへ拡大した。バージョン別エントリが 54 件から 252 件になり、索引全体は 144 件から 348 件になった
2. Transports Working Group の charter ページ `community/working-groups/transports` が索引に加わった。バージョン系統以外で今回増えた唯一のページで、同 WG は SEP-2243・SEP-2260 の起草者として既に活動していたが、charter ページが載るのは今回が初めて
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**索引が全プロトコルバージョンを収録するよう拡大**](#1-索引が全プロトコルバージョンを収録するよう拡大):  
  `llms.txt` に、これまで載っていた現行バージョン 2026-07-28 に加えて、draft と過去の確定版 4 系統（2025-11-25 / 2025-06-18 / 2025-03-26 / 2024-11-05）の `docs/` `specification/` 配下が追加された。バージョン別エントリは 54 件から 252 件に増え、索引全体では 144 件が 348 件（ユニーク URL 343 件）になっている。draft のページ構成は 2026-07-28 と完全に一致する一方、過去の確定版は当時の構成のまま収録されている。
2. [**Transports Working Group の charter ページが新設**](#2-transports-working-group-の-charter-ページが新設):  
  `community/working-groups/transports`（説明文「Charter for the MCP Transports Working Group.」）が索引に追加された。バージョン系統の追加を除くと、今回増えた唯一のページ。同 WG は SEP-2243（Streamable HTTP の HTTP ヘッダー標準化）と SEP-2260（サーバー発リクエストのクライアントリクエスト紐付け必須化）の起草者として `llms-full.txt` に既に登場しており、活動実体が先行していた形になる。
<!-- light:highlight-list:end -->

## 1. 索引が全プロトコルバージョンを収録するよう拡大

今回の差分は索引ファイル `llms.txt` に限られ、追加 204 行・削除 2 行という内訳です。最大の変更は収録範囲の拡大で、これまで `docs/` `specification/` 配下は現行バージョンである 2026-07-28 の分（ドキュメント 23 件・仕様 31 件の計 54 件）しか載っていませんでしたが、ここに draft（23 件・31 件の計 54 件）、2025-11-25（16 件・22 件の計 38 件）、2025-06-18（16 件・21 件の計 37 件）、2025-03-26（16 件・19 件の計 35 件）、2024-11-05（16 件・18 件の計 34 件）が加わりました。バージョン別エントリは 54 件から 252 件になり、索引全体のエントリ行数は 144 件から 348 件になっています。ただしユニーク URL は 343 件で、これは各バージョンのドキュメントブロックの末尾に置かれる `Example Servers` の参照先がバージョン非依存の同一 URL（`/examples`）であるためです。追加 204 行の内訳は、バージョン別の 198 件、後述の Transports Charter 1 件、そして `Example Servers` の重複 5 行となります。

「Versioning」ページによれば、MCP の仕様リビジョンは draft（策定中で利用向けではない）・current（現行版で後方互換な変更は続く）・final（変更されない過去の確定仕様）の 3 状態に分かれ、current は 2026-07-28 です。今回の変更は、索引がこのうち current だけを扱っていた状態から、draft と final を含む全リビジョンを扱う状態へ移ったものと読めます。実際に収録されたページ構成を見ると、draft は 2026-07-28 とドキュメント・仕様のパスが 1 件残らず一致しており、draft 固有の未リリースページはありません。一方で過去の確定版は当時の構成のままで、たとえば 2025-11-25 の仕様には `basic/authorization`・`basic/lifecycle`・`basic/transports` や `basic/utilities/` 配下の `cancellation` / `ping` / `progress` / `tasks` が単独ページとして並びます。これに対して 2026-07-28 では認可が `basic/authorization/` 配下の 4 ページに、`basic/patterns/` 配下に `cancellation` / `progress` / `subscriptions` / `mrtr` などが、トランスポートが `basic/transports/` 配下の `stdio` / `streamable-http` に分割され、`basic/versioning`・`deprecated`・`server/discover`・`server/utilities/caching` が加わった構成になっています。ドキュメント側も同様で、2026-07-28 と draft にある MCP Inspector の下位 7 ページ（`web` / `cli` / `tui` / `configuration` / `authorization` / `protocol-eras` / `recipes`）は過去 4 バージョンには存在しません。

なお、ページ本文を収める `llms-full.txt` には今回まったく差分がなく、既存ページの記述内容は変わっていません。今回追加されたバージョン別 URL の本文も `llms-full.txt` には含まれないため、索引側だけが先に全リビジョンをカバーした状態です。バージョンを指定した参照先を探す用途では索引の網羅性が上がった一方、本文をまとめて取得する用途では従来どおり現行バージョン中心の内容になります。

- [Versioning - MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/learn/versioning#revisions)

## 2. Transports Working Group の charter ページが新設

コミュニティの Working Group charter 一覧に `Transports Charter`（`community/working-groups/transports`、説明文は「Charter for the MCP Transports Working Group.」）が加わりました。索引上の位置は Skills Over MCP Charter と Triggers and Events Charter の間で、既存の charter 群と同じ命名規則・アルファベット順に沿っています。バージョン系統の一括追加を除くと、今回の差分で増えた URL はこの 1 件だけです。

Transports Working Group 自体は今回が初出ではありません。`llms-full.txt`（今回差分なし）に収録されている SEP のうち、SEP-2243「HTTP Header Standardization for Streamable HTTP Transport」（Standards Track・Final・2026年02月04日作成）と SEP-2260「Require Server requests to be associated with a Client request.」（Standards Track・Final・2026年02月16日作成）の 2 件が、著者欄に「MCP Transports Working Group」を挙げています。つまり同 WG は仕様提案の起草主体として先に活動しており、そこへ charter ページが後から用意された形です。

ページ本文は `llms-full.txt` にまだ取り込まれていません。同ファイルには Agents / File Uploads / Inspector V2 / Interceptors / Registry / SDK / Server Card / Skills Over MCP / Triggers and Events といった他の Working Group charter が本文つきで収録されている一方、Transports Charter だけが欠けています。このためミッション・スコープ・リーダーシップといった charter の中身は、今回の入力からは確認できません。

- [Transports Charter - MCP Docs](https://modelcontextprotocol.io/community/working-groups/transports)

## 新規追加されたページ

<!-- light:new-pages:start -->
今回索引に増えたユニーク URL 199 件のうち、198 件は draft と過去の確定版 4 系統について既存ページ構成をそのまま収録したもので、収録範囲の拡大にあたります（詳細はハイライト 1 参照）。それを除いた新規ページは次の 1 件です。

- [**Transports Charter**](#1-transports-charter) ([MCP Docs](https://modelcontextprotocol.io/community/working-groups/transports)):  
  MCP Transports Working Group の charter ページ。バージョン系統の追加を除くと今回唯一の新規ページで、本文は `llms-full.txt` に未収録のため中身は確認できない（詳細はハイライト 2 参照）。
<!-- light:new-pages:end -->

## 1. Transports Charter

索引に追加されたのはタイトル `Transports Charter`・パス `community/working-groups/transports`・説明文「Charter for the MCP Transports Working Group.」の 1 行です。説明文は他の Working Group charter と同じ定型（「Charter for the MCP <名称> Working Group.」）で、配置も `community/working-groups/` 配下の SDK・Server Card・Skills Over MCP・Triggers and Events と並ぶ位置にあります。

このページの本文は今回の入力に含まれていないため、charter の内容そのものについてここで述べられることはありません。同 WG の関心領域を推し量る材料としては、`llms-full.txt` に収録済みの SEP-2243（Streamable HTTP のルーティング情報を HTTP ヘッダーへ露出させ、ロードバランサやプロキシが JSON-RPC ペイロードを解析せずに処理できるようにする提案）と SEP-2260（`roots/list`・`sampling/createMessage`・`elicitation/create` をクライアント発リクエストに紐付けることを必須とする提案）があり、いずれも同 WG が著者となっています。

- [Transports Charter - MCP Docs](https://modelcontextprotocol.io/community/working-groups/transports)

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
今回の対象期間に大幅な更新（本文 50 行以上の変更）があったページはありません。ページ本文を収める `llms-full.txt` には差分が 1 行もなく、既存ページの記述内容は変わっていません。
<!-- light:updated-pages:end -->

## 軽微な更新

<!-- light:minor-updates:start -->
今回差分が出たファイルは索引 `llms.txt` の 1 件のみです。収録範囲の拡大と新規ページ 1 件（ハイライト 1・2 参照）を除くと、索引ファイル自体の体裁に関する変更が 2 点あります。いずれも対応するドキュメントページの変更ではないため、参考リンクはありません。

**その他**

- 索引冒頭にあった `## Docs` セクション見出しと直後の空行が削除された（削除 2 行はこの 2 行のみ）。これにより `llms.txt` からセクション見出しが完全に無くなり、タイトル行の直後からエントリの箇条書きが始まる構成になった
- `Example Servers`（`/examples`）のエントリが、各バージョンのドキュメントブロックの末尾に 1 件ずつ置かれる形になり、ファイル全体で同一 URL が 6 回登場するようになった。エントリ行数 348 件に対してユニーク URL が 343 件にとどまるのはこのため
<!-- light:minor-updates:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-08-24.md](./archives/latest/2026-08-24.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-08-24.md](./archives/latest-detail/2026-08-24.md)

<!--
base_commit: 961fa881bd3d4366c49a34b34508be3172b7c2fc
head_commit: 9183e5fb58ed21ba3079f4e0f6a528c4e46d1ea7
generated_at_full: 2026-08-26T15:36:50+09:00
-->
