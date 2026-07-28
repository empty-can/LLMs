---
対象期間: 2026年07月16日 〜 2026年07月27日
作成日: 2026-07-27
---

# MCP 公式ドキュメント更新サマリ

```markdown
今回の対象期間の原文差分は 5 ページ・計 6 か所で、いずれも 50 行未満の小規模な更新でした。実体的な変更は、JSON-RPC エラーコードの再割り当ての反映、仕様への用語注記の追加、認可チュートリアルのコード例修正の 3 点です。

主要なものを以下に挙げます。

1. SEP-2575 のエラーコード定数が `-32004`→`-32022`・`-32003`→`-32021` に更新され、SEP-2243 には `HeaderMismatch` が `-32001`→`-32020` に再割り当てされた旨を記す節が新設された
2. 仕様 2025-11-25 の Tools ページに、`structuredContent` は LLM の「structured outputs」とは無関係である旨の注記が追加された
3. 認可チュートリアルの TypeScript コード例が、Keycloak の付与する URL でない audience でクラッシュしないよう修正された
```

## ハイライト

1. [**JSON-RPC エラーコードの再割り当て**](./latest-detail.md#1-json-rpc-エラーコードの再割り当て):  
  SEP-2575 の `UNSUPPORTED_PROTOCOL_VERSION` が `-32022` に、`MISSING_REQUIRED_CLIENT_CAPABILITY` が `-32021` に更新され、SEP-2243 には Final 到達後の変更を追跡する節が新設されて `HeaderMismatch` の `-32020` への再割り当てが記された。
2. [**structuredContent と LLM の structured outputs は別物と明記**](./latest-detail.md#2-structuredcontent-と-llm-の-structured-outputs-は別物と明記):  
  仕様 2025-11-25 の Tools ページに、`structuredContent` はサーバーが生成する結果データであり、スキーマ制約付きのモデル生成を指す「structured outputs」とは無関係である旨の注記が追加された。
3. [**認可チュートリアルの audience 検証コードを修正**](./latest-detail.md#3-認可チュートリアルの-audience-検証コードを修正):  
  `aud` クレーム検証のコード例が `try`/`catch` で包まれ、Keycloak が付与する `account` などの URL でない audience で例外が投げられて検証全体が落ちる問題が解消された。

## 新規追加されたページ

（今回の対象期間に新規追加されたページはありません）

## 大幅に更新されたページ

（今回の対象期間に大幅更新されたページはありません）

## 軽微な更新

今回の対象期間に更新されたのは 5 ページで、いずれも 50 行未満の小規模な変更です。

**機能改善**

- SEP-2575「Make MCP Stateless」のエラーコード定数 2 件と、SEP-2243「HTTP Header Standardization for Streamable HTTP Transport」への追記節の新設（詳細はハイライト 1 参照）。 — [SEP-2575: Make MCP Stateless](https://modelcontextprotocol.io/seps/2575-stateless-mcp#missing-required-capabilities) / [SEP-2243: HTTP Header Standardization for Streamable HTTP Transport](https://modelcontextprotocol.io/seps/2243-http-standardization#changes-since-sep-became-final)
- 仕様 2025-11-25 の Tools ページ「Structured Content」節への用語注記の追加（詳細はハイライト 2 参照）。 — [Tools](https://modelcontextprotocol.io/specification/2025-11-25/server/tools#structured-content)

**バグ修正**

- 「Understanding Authorization in MCP」の TypeScript コード例で、URL でない audience による例外でトークン検証が落ちる問題の修正（詳細はハイライト 3 参照）。 — [Understanding Authorization in MCP](https://modelcontextprotocol.io/docs/tutorials/security/authorization#mcp-server-setup)

**その他**

- SEP-2549「TTL for List Results」の「Error handling」節で、`ttlMs` が欠落している場合の既定値を述べる記述の `ttlMs` と `0` がインラインコード書式に統一されました。規範の内容に変更はありません。 — [SEP-2549: TTL for List Results](https://modelcontextprotocol.io/seps/2549-TTL-for-list-results#error-handling)

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-07-16.md](./archives/latest/2026-07-16.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-07-16.md](./archives/latest-detail/2026-07-16.md)

<!--
base_commit: 5cf373da86d5703c50540e7e49df4d79e33d4c76
head_commit: d07523a8a8c8d9625ae653077944846e251bd565
generated_at_full: 2026-07-28T13:14:32+09:00
-->
