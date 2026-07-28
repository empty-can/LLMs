---
対象期間: 2026年07月16日 〜 2026年07月27日
作成日: 2026-07-27
---

# MCP 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
今回の対象期間の原文差分は 5 ページ・計 6 か所で、いずれも 50 行未満の小規模な更新でした。実体的な変更は、JSON-RPC エラーコードの再割り当ての反映、仕様への用語注記の追加、認可チュートリアルのコード例修正の 3 点です。

主要なものを以下に挙げます。

1. SEP-2575 のエラーコード定数が `-32004`→`-32022`・`-32003`→`-32021` に更新され、SEP-2243 には `HeaderMismatch` が `-32001`→`-32020` に再割り当てされた旨を記す節が新設された
2. 仕様 2025-11-25 の Tools ページに、`structuredContent` は LLM の「structured outputs」とは無関係である旨の注記が追加された
3. 認可チュートリアルの TypeScript コード例が、Keycloak の付与する URL でない audience でクラッシュしないよう修正された
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**JSON-RPC エラーコードの再割り当て**](#1-json-rpc-エラーコードの再割り当て):  
  SEP-2575 の `UNSUPPORTED_PROTOCOL_VERSION` が `-32022` に、`MISSING_REQUIRED_CLIENT_CAPABILITY` が `-32021` に更新され、SEP-2243 には Final 到達後の変更を追跡する節が新設されて `HeaderMismatch` の `-32020` への再割り当てが記された。
2. [**structuredContent と LLM の structured outputs は別物と明記**](#2-structuredcontent-と-llm-の-structured-outputs-は別物と明記):  
  仕様 2025-11-25 の Tools ページに、`structuredContent` はサーバーが生成する結果データであり、スキーマ制約付きのモデル生成を指す「structured outputs」とは無関係である旨の注記が追加された。
3. [**認可チュートリアルの audience 検証コードを修正**](#3-認可チュートリアルの-audience-検証コードを修正):  
  `aud` クレーム検証のコード例が `try`/`catch` で包まれ、Keycloak が付与する `account` などの URL でない audience で例外が投げられて検証全体が落ちる問題が解消された。
<!-- light:highlight-list:end -->

## 1. JSON-RPC エラーコードの再割り当て

MCP 仕様側のエラーコード割り当ての見直し（[modelcontextprotocol#2907](https://github.com/modelcontextprotocol/modelcontextprotocol/pull/2907)）が、2 つの SEP ページに反映されました。

SEP-2575「Make MCP Stateless」では、本文中の TypeScript 定義がそのまま新しい値に書き換えられました。「Unsupported Protocol Versions」節の `UNSUPPORTED_PROTOCOL_VERSION` は `-32004` から `-32022` に、「Missing Required Capabilities」節の `MISSING_REQUIRED_CLIENT_CAPABILITY` は `-32003` から `-32021` に変更されています。いずれもエラーの発生条件（サーバーが実装していないプロトコルバージョンを受け取った場合、クライアントが宣言していないケイパビリティを必要とする場合。HTTP では `400 Bad Request`）や `data` に載せる情報（`supported` / `requested`、`requiredCapabilities`）に変更はなく、定数値のみの更新です。

SEP-2243「HTTP Header Standardization for Streamable HTTP Transport」では、本文中の `-32001` という記述は据え置いたまま、末尾に「Changes since SEP became Final」節が新設されました。この節は、当該 SEP が受理内容の歴史的記録として保存されるものであり、Final 到達後に加えられた仕様変更をここで追跡する（権威ある最新の要件は現行の仕様を参照すること）と述べています。最初の項目として、`HeaderMismatch` が上記 PR により `-32001` から `-32020` へ再割り当てされたこと、現行仕様に対して実装する際は本文中の `-32001` をすべて `-32020` と読み替えるべきことが記載されました。

- [SEP-2575: Make MCP Stateless - MCP Docs](https://modelcontextprotocol.io/seps/2575-stateless-mcp#unsupported-protocol-versions)
- [SEP-2243: HTTP Header Standardization for Streamable HTTP Transport - MCP Docs](https://modelcontextprotocol.io/seps/2243-http-standardization#changes-since-sep-became-final)

## 2. structuredContent と LLM の structured outputs は別物と明記

仕様 2025-11-25 の Tools ページ「Structured Content」節に、用語の混同を防ぐための注記が追加されました。`structuredContent` は**サーバーが生成する結果データ**であり、スキーマで制約したモデル生成を指す LLM の「structured outputs」とは無関係である、という内容です。

節の既存の記述（構造化コンテンツは結果の `structuredContent` フィールドに JSON オブジェクトとして返すこと、後方互換のため構造化コンテンツを返すツールは直列化した JSON を TextContent ブロックにも返すべき（SHOULD）であること）や、後続の「Output Schema」節の要件に変更はありません。名称の似た 2 つの概念を取り違えないよう読み手に注意を促すだけの追記です。

- [Tools - MCP Docs](https://modelcontextprotocol.io/specification/2025-11-25/server/tools#structured-content)

## 3. 認可チュートリアルの audience 検証コードを修正

「Understanding Authorization in MCP」の「Implementation Example」（Keycloak を認可サーバーとして動かす例）にある、MCP サーバー側の TypeScript コード例が修正されました。アクセストークンの `aud` クレームを検証する箇所で、各 audience に対して `checkResourceAllowed`（要求リソースと設定リソースを突き合わせるヘルパー）を呼ぶ処理が `try`/`catch` で包まれ、例外が発生した場合は `false`（不一致）を返すようになっています。

追加されたコメントでは、Keycloak のトークンには `account` や `test-client` のように URL でない audience が含まれること、それらは決して自分のリソースを指さないため、クラッシュさせずに「不一致」として扱うべきであることが説明されています。従来のコードは URL でない audience を渡された時点で `checkResourceAllowed` が例外を投げ、検証処理そのものが落ちていました。修正後は各 audience の判定が独立して行われ、許可される audience が 1 つも無かった場合には従来どおり「None of the provided audiences are allowed.」というエラーが送出されます。

- [Understanding Authorization in MCP - MCP Docs](https://modelcontextprotocol.io/docs/tutorials/security/authorization#mcp-server-setup)

## 新規追加されたページ

<!-- light:new-pages:start -->
（今回の対象期間に新規追加されたページはありません）
<!-- light:new-pages:end -->

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
（今回の対象期間に大幅更新されたページはありません）
<!-- light:updated-pages:end -->

## 軽微な更新

<!-- light:minor-updates:start -->
今回の対象期間に更新されたのは 5 ページで、いずれも 50 行未満の小規模な変更です。

**機能改善**

- SEP-2575「Make MCP Stateless」のエラーコード定数 2 件と、SEP-2243「HTTP Header Standardization for Streamable HTTP Transport」への追記節の新設（詳細はハイライト 1 参照）。 — [SEP-2575: Make MCP Stateless](https://modelcontextprotocol.io/seps/2575-stateless-mcp#missing-required-capabilities) / [SEP-2243: HTTP Header Standardization for Streamable HTTP Transport](https://modelcontextprotocol.io/seps/2243-http-standardization#changes-since-sep-became-final)
- 仕様 2025-11-25 の Tools ページ「Structured Content」節への用語注記の追加（詳細はハイライト 2 参照）。 — [Tools](https://modelcontextprotocol.io/specification/2025-11-25/server/tools#structured-content)

**バグ修正**

- 「Understanding Authorization in MCP」の TypeScript コード例で、URL でない audience による例外でトークン検証が落ちる問題の修正（詳細はハイライト 3 参照）。 — [Understanding Authorization in MCP](https://modelcontextprotocol.io/docs/tutorials/security/authorization#mcp-server-setup)

**その他**

- SEP-2549「TTL for List Results」の「Error handling」節で、`ttlMs` が欠落している場合の既定値を述べる記述の `ttlMs` と `0` がインラインコード書式に統一されました。規範の内容に変更はありません。 — [SEP-2549: TTL for List Results](https://modelcontextprotocol.io/seps/2549-TTL-for-list-results#error-handling)
<!-- light:minor-updates:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-07-16.md](./archives/latest/2026-07-16.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-07-16.md](./archives/latest-detail/2026-07-16.md)

<!--
base_commit: 5cf373da86d5703c50540e7e49df4d79e33d4c76
head_commit: d07523a8a8c8d9625ae653077944846e251bd565
generated_at_full: 2026-07-28T13:14:32+09:00
-->
