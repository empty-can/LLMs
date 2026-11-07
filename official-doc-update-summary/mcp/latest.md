---
対象期間: 2026年11月02日 〜 2026年11月06日
作成日: 2026-11-06
---

# MCP 公式ドキュメント更新サマリ

```markdown
今回の対象期間には取り込みが 5 回あり、MCP に差分が出たのは最後の 1 回だけで、`llms-full.txt` の 4 ページが変わりました。新規ページはなく、Build an MCP client と Build an MCP server の 2 ページが大幅更新です。中心は、クライアントのチュートリアルの 4 言語がツール呼び出しのループに書き直されたことと、サーバーのチュートリアルの Rust 版が rmcp 3.4 と構造化された結果に対応したことです。

主要なものを以下に挙げます。

1. Build an MCP client の Python・TypeScript・Kotlin・Ruby のタブが、最大 `MAX_TOOL_TURNS`（`10`）回のツール呼び出しのループになり、`max_tokens` の上限も 1,000 前後から `10000` に上がった
2. Build an MCP server の Rust のタブが rmcp `3.4` に合わせて書き直され、ツールがテキストと一緒に `outputSchema` に沿った構造化された結果を返すようになった（`get_alerts` は根が配列）
3. Build an MCP client の TypeScript のタブが `versionNegotiation: { mode: "auto" }` で接続するようになり、Kotlin のタブには、使うプロトコルの版は `2025-11-25` で `2026-07-28` しか受け付けないサーバーにはつながらないという注記が加わった
4. Schema Reference の `Tool` に、`inputSchema` で composition keyword を使うときの注意と、`find_resource`・`list_users` の 2 つの例が加わった
```

## ハイライト

1. [**Build an MCP client の 4 言語がツール呼び出しのループになった**](./latest-detail.md#1-build-an-mcp-client-の-4-言語がツール呼び出しのループになった):  
  Python・TypeScript・Kotlin・Ruby のタブの `process_query` が、Claude がツールを呼ばずに答えるまで、最大 `MAX_TOOL_TURNS`（`10`）回繰り返す形になった。これまでは 1 回ツールを実行して応答を受け取ったら終わりだった。TypeScript と Kotlin は、ツールの結果を `tool_use` に対応する `tool_result` のブロックで返す形に改まり、上限に達すると `[Stopped after 10 tool-use turns]` を出す。
2. [**Build an MCP server の Rust 版が rmcp 3.4 と構造化された結果に対応した**](./latest-detail.md#2-build-an-mcp-server-の-rust-版が-rmcp-34-と構造化された結果に対応した):  
  Rust のタブの rmcp が `0.3` から `3.4` になり、必要な Rust の版も 1.70 から 1.88 に上がった。2 つのツールは文字列の代わりに `Result<CallToolResult, ErrorData>` を返し、`output_schema` を宣言して、テキストと構造化された結果の両方を返す。`get_alerts` の結果は根が配列で、コメントはこれを 2026-07-28 のリビジョンで初めて許されたものと説明している。
3. [**TypeScript と Kotlin のクライアントにプロトコルの版の扱いが加わった**](./latest-detail.md#3-typescript-と-kotlin-のクライアントにプロトコルの版の扱いが加わった):  
  TypeScript のタブは `Client` に `versionNegotiation: { mode: "auto" }` を渡すようになった。`server/discover` を試し、`2025-11-25` のハンドシェイクにフォールバックする設定で、SDK の既定は `legacy` だと説明している。Kotlin のタブには、最新の安定版の Kotlin SDK が対応する `2025-11-25` を使うので `2026-07-28` しか受け付けないサーバーにはつながらない、という NOTE が加わり、`mcpVersion` も `0.16.0` になった。
4. [**Schema Reference の Tool に composition keyword の注意と例が加わった**](./latest-detail.md#4-schema-reference-の-tool-に-composition-keyword-の注意と例が加わった):  
  `Tool` の `inputSchema` の説明に、composition keyword を使うときは `properties` をスキーマの根に宣言し、分岐は `required` のような存在の検査に留めるよう求める文が加わった。`Tool` の例も、`oneOf` を使う `find_resource` と、配列の `outputSchema` を持つ `list_users` の 2 つが増えた。

## 新規追加されたページ

今回の対象期間に新たに追加されたページはありません。索引 `llms.txt` に変更はなく、索引側のエントリ数（364 件）と本文 `llms-full.txt` の収録ページ数（159 件。URL としては 158 件）はどちらも前回と同じです。

## 大幅に更新されたページ

- [**Build an MCP client**](./latest-detail.md#1-build-an-mcp-client) ([MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-client#query-processing-logic)):  
  Python・TypeScript・Kotlin・Ruby のタブを、最大 `MAX_TOOL_TURNS` 回のツール呼び出しのループに書き直し、TypeScript に版の自動交渉と Ctrl-D・Ctrl-C の処理を、Kotlin に版の注記を加えた（追加 314 行・削除 157 行。詳細はハイライト 1・3 参照）。
- [**Build an MCP server**](./latest-detail.md#2-build-an-mcp-server) ([MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-server#implementing-the-weather-server-and-tools)):  
  Rust のタブを rmcp `3.4` に合わせて書き直し、ツールがテキストと `outputSchema` に沿った構造化された結果を返す形にした（追加 174 行・削除 72 行。詳細はハイライト 2 参照）。

## 軽微な更新

今回差分が出たファイルは `llms-full.txt` の 1 件で、差分のあった 4 ページのうち、大幅更新の 2 ページのほかに、次の 2 ページで内容が変わりました。

**機能改善**

- Schema Reference の `Tool` で、`inputSchema` の説明に composition keyword を使うときの注意を追加し、`find_resource`（`oneOf` の入力スキーマ）と `list_users`（配列の出力スキーマ）の例を追加（詳細はハイライト 4 参照） — [Schema Reference](https://modelcontextprotocol.io/specification/2026-07-28/schema#tool)
- SEP Guidelines の Step-by-Step Process の手順 3 に、PR のタイトルを `sep: propose task cancellation` のようにすることを追加し、`CONTRIBUTING.md` の PR タイトルの指針へのリンクを追加 — [SEP Guidelines](https://modelcontextprotocol.io/community/sep-guidelines#step-by-step-process)
- 同じ節の手順 4 に、PR の番号が決まったら PR のタイトルを `sep(SEP-1850): describe the proposal` のように改めることを追加。追加のコミットで足り、amend や force-push は要らない。この SEP に関する後続の PR は `SEP-1850` をスコープとして残し、説明欄で元の SEP にリンクする — [SEP Guidelines](https://modelcontextprotocol.io/community/sep-guidelines#step-by-step-process)

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-11-02.md](./archives/latest/2026-11-02.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-11-02.md](./archives/latest-detail/2026-11-02.md)

<!--
base_commit: acb459e04e57acda73f439e58d2759ea5599cdf6
head_commit: b3f45341023a7453d8b8e8e11e025447ef991a24
generated_at_full: 2026-11-07T15:21:16+09:00
-->
