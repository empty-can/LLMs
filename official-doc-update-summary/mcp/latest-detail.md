---
対象期間: 2026年11月02日 〜 2026年11月06日
作成日: 2026-11-06
---

# MCP 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
今回の対象期間には取り込みが 5 回あり、MCP に差分が出たのは最後の 1 回だけで、`llms-full.txt` の 4 ページが変わりました。新規ページはなく、Build an MCP client と Build an MCP server の 2 ページが大幅更新です。中心は、クライアントのチュートリアルの 4 言語がツール呼び出しのループに書き直されたことと、サーバーのチュートリアルの Rust 版が rmcp 3.4 と構造化された結果に対応したことです。

主要なものを以下に挙げます。

1. Build an MCP client の Python・TypeScript・Kotlin・Ruby のタブが、最大 `MAX_TOOL_TURNS`（`10`）回のツール呼び出しのループになり、`max_tokens` の上限も 1,000 前後から `10000` に上がった
2. Build an MCP server の Rust のタブが rmcp `3.4` に合わせて書き直され、ツールがテキストと一緒に `outputSchema` に沿った構造化された結果を返すようになった（`get_alerts` は根が配列）
3. Build an MCP client の TypeScript のタブが `versionNegotiation: { mode: "auto" }` で接続するようになり、Kotlin のタブには、使うプロトコルの版は `2025-11-25` で `2026-07-28` しか受け付けないサーバーにはつながらないという注記が加わった
4. Schema Reference の `Tool` に、`inputSchema` で composition keyword を使うときの注意と、`find_resource`・`list_users` の 2 つの例が加わった
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**Build an MCP client の 4 言語がツール呼び出しのループになった**](#1-build-an-mcp-client-の-4-言語がツール呼び出しのループになった):  
  Python・TypeScript・Kotlin・Ruby のタブの `process_query` が、Claude がツールを呼ばずに答えるまで、最大 `MAX_TOOL_TURNS`（`10`）回繰り返す形になった。これまでは 1 回ツールを実行して応答を受け取ったら終わりだった。TypeScript と Kotlin は、ツールの結果を `tool_use` に対応する `tool_result` のブロックで返す形に改まり、上限に達すると `[Stopped after 10 tool-use turns]` を出す。
2. [**Build an MCP server の Rust 版が rmcp 3.4 と構造化された結果に対応した**](#2-build-an-mcp-server-の-rust-版が-rmcp-34-と構造化された結果に対応した):  
  Rust のタブの rmcp が `0.3` から `3.4` になり、必要な Rust の版も 1.70 から 1.88 に上がった。2 つのツールは文字列の代わりに `Result<CallToolResult, ErrorData>` を返し、`output_schema` を宣言して、テキストと構造化された結果の両方を返す。`get_alerts` の結果は根が配列で、コメントはこれを 2026-07-28 のリビジョンで初めて許されたものと説明している。
3. [**TypeScript と Kotlin のクライアントにプロトコルの版の扱いが加わった**](#3-typescript-と-kotlin-のクライアントにプロトコルの版の扱いが加わった):  
  TypeScript のタブは `Client` に `versionNegotiation: { mode: "auto" }` を渡すようになった。`server/discover` を試し、`2025-11-25` のハンドシェイクにフォールバックする設定で、SDK の既定は `legacy` だと説明している。Kotlin のタブには、最新の安定版の Kotlin SDK が対応する `2025-11-25` を使うので `2026-07-28` しか受け付けないサーバーにはつながらない、という NOTE が加わり、`mcpVersion` も `0.16.0` になった。
4. [**Schema Reference の Tool に composition keyword の注意と例が加わった**](#4-schema-reference-の-tool-に-composition-keyword-の注意と例が加わった):  
  `Tool` の `inputSchema` の説明に、composition keyword を使うときは `properties` をスキーマの根に宣言し、分岐は `required` のような存在の検査に留めるよう求める文が加わった。`Tool` の例も、`oneOf` を使う `find_resource` と、配列の `outputSchema` を持つ `list_users` の 2 つが増えた。
<!-- light:highlight-list:end -->

## 1. Build an MCP client の 4 言語がツール呼び出しのループになった

今回の対象期間の取り込みは 5 回（2026年11月03日の追加 11 URL の初回取り込みと、11月04日〜07日の定期取り込み 4 回）で、MCP の入力ファイルに差分が出たのは最後の 11月07日の 1 回だけです。差分は本文 `llms-full.txt` の追加 495 行・削除 233 行で、索引 `llms.txt` は変わらず（エントリ数は 364 件のまま）、`llms-full.txt` の総行数は 46,112 行から 46,374 行になり、収録ページ数は 159 件（`examples` が 2 回収録されているため、URL としては 158 件）で変わっていません。差分のあったページは 4 件で、Build an MCP client（追加 314 行・削除 157 行）、Build an MCP server（追加 174 行・削除 72 行）、Schema Reference（追加 5 行・削除 2 行）、SEP Guidelines（追加 2 行・削除 2 行）です。ページごとの行数は、`git diff` のハンクを head 側の `Source:` の行と `[tab]` の行でページとタブに振り分けたもので、合計は上の追加 495 行・削除 233 行に一致します。4 ページとも見出しの増減はありません。

Build an MCP client では、Python・TypeScript・Kotlin・Ruby の 4 つのタブの `process_query` が、同じ考え方で書き直されました。2026年10月31日版のサマリで取り上げた Rust のタブは、すでにこの形になっています。

**ツール呼び出しがループになりました。** これまでの 4 言語は、最初の応答で求められたツールを実行し、次の応答のテキストを集めて終わっていました。新しいコードは、応答の中の `tool_use` をすべて集めて実行し、結果を送って Claude を呼び直すことを、Claude がツールを呼ばずに答えるか、`MAX_TOOL_TURNS`（`10`）に達するまで繰り返します。上限に達すると、最後の応答のテキストを残し、まだツールを求めていれば `[Stopped after 10 tool-use turns]` を加えます。

**どのリクエストにも `tools` を付けるようになりました。** TypeScript・Kotlin・Ruby はこれまで、ツールの結果を送る 2 回目のリクエストに `tools` を付けていませんでした（Python は付けていた）。今回から 4 言語とも毎回付けるので、Claude は結果を読んだ後もツールを呼び続けられます。Ruby の `chat` ヘルパーは `tools` が任意の引数から必須の引数に変わりました。

**TypeScript と Kotlin は `tool_result` のブロックで結果を返すようになりました。** この 2 言語はこれまで、ツールの結果を `tool_use` と対応付けず、`role: "user"` のメッセージの地の文として 1 件ずつ送っていました。今回から、アシスタントのターンをそのまま送り返した上で、`tool_use` ごとの `tool_result` を 1 つの user メッセージにまとめます。Python の説明は、この 2 つが揃っていない会話を Messages API が拒否することと、thinking block を含めてアシスタントのメッセージをそのまま送り返すことを加えました。

**失敗したツールの扱いが揃いました。** TypeScript は `isError` を `is_error` に、Kotlin は `isError` を `ToolResultBlockParam` の `isError(true)` に、Ruby は `result.dig("result", "isError")` を `is_error` に渡すようになり、Claude が失敗を読んで別の手を試せます（Python はもともと渡していた）。TypeScript の Best practices の「ツールの呼び出しを try-catch で囲む」は、「失敗したツールが例外を投げると期待せず `result.isError` を確かめる」に替わりました。

**`max_tokens` の上限が上がりました。** Python・TypeScript・Ruby の `1000`、Kotlin の `1024` が、定数 `MAX_TOKENS` の `10000`（Kotlin は `10_000L`）になりました。コメントは、モデルは指定が無ければ適応的に考え、`max_tokens` は thinking と応答の合計の上限なので、両方の余地を残す、と説明しています。C# のタブの変更は、対応する `MaxOutputTokens` が `1000` から `10000` になった 1 行だけです。

- [Build an MCP client - MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-client#query-processing-logic)
- [Build an MCP client - MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-client#query-processing-logic-2)

## 2. Build an MCP server の Rust 版が rmcp 3.4 と構造化された結果に対応した

Build an MCP server の変更（追加 174 行・削除 72 行）はすべて Rust のタブで、ほかの 7 つのタブは変わっていません。

**依存が上がりました。** `Cargo.toml` の rmcp は `0.3` から `3.4`、`tokio` は `1.46` から `1.53`、`reqwest` は `0.12` から `0.13` になり、`tracing`・`tracing-subscriber` は依存から外れました。System requirements の Rust は 1.70 以上から 1.88 以上になり、これは `rmcp` クレートが宣言する最小の版だと書かれています。

**ツールはテキストと構造化された結果の両方を返すようになりました。** これまでの `get_alerts`・`get_forecast` は `String` を返していました。今回から `Result<CallToolResult, ErrorData>` を返し、`#[tool]` の属性に `output_schema = schema_for_output::<…>()` を宣言します。結果の型として `Alert`・`Forecast`・`Period` が加わり、`JsonSchema` を derive することで形が出力スキーマとして公開され、doc コメントがスキーマのプロパティの説明になります。新しいヘルパー `dual_channel_result` は、`content` に人が読むテキストを、`structured_content` にスキーマに沿った JSON を入れた `CallToolResult` を作ります。

**`get_alerts` の結果は根が配列です。** `get_alerts` は `Vec<Alert>` を出力スキーマとするので、`structuredContent` はオブジェクトで包まない最上位の JSON 配列になり、コメントはこれを 2026-07-28 のリビジョンで初めて許されたものと説明しています。`get_forecast` の `Forecast` はオブジェクトの場合の例です。

**失敗はツールの失敗として返すようになりました。** 天気のサービスへのリクエストが失敗すると `CallToolResult::error` を返し、クライアントはこれをツールの失敗として受け取ります。これまではエラーの文も通常の文字列として返していました。警報が無いときは、エラーではなく空の配列を返します。メッセージも変わり、`get_alerts` の失敗は `Unable to fetch alerts for {state}.`、`get_forecast` の 2 回目のリクエストの失敗は `Unable to fetch detailed forecast.` になりました。

**サーバーの名前と版を自分で示すようになりました。** `get_info` の戻り値は `ServerInfo` から `ServerConfig` になり、`server_info` に `Implementation::new("weather", "1.0.0")` を入れます。コメントは、これが無いと rmcp 自身のクレート名と版を報告すると説明しています。節ごとの変更は「大幅に更新されたページ」の表を参照してください。

- [Build an MCP server - MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-server#implementing-the-weather-server-and-tools)
- [Build an MCP server - MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-server#system-requirements-7)

## 3. TypeScript と Kotlin のクライアントにプロトコルの版の扱いが加わった

**TypeScript のタブは版を自動で交渉するようになりました。** Basic Client Structure の `Client` の生成が、`new Client({ name: "mcp-client-cli", version: "1.0.0" })` から、第 2 引数に `{ versionNegotiation: { mode: "auto" } }` を渡す形になりました。コメントによると、`auto` は `server/discover` を試し、`2025-11-25` のハンドシェイクにフォールバックします。SDK の既定は `legacy` です。

**Kotlin のタブに版の注記が加わりました。** タブの冒頭に NOTE が加わりました。このクライアントは、最新の安定版の Kotlin SDK が対応する MCP プロトコルの版 `2025-11-25` を使い、その版を受け付けるサーバーには接続できるが、`2026-07-28` しか受け付けないサーバーには接続できない、という内容で、仕様の versioning の backward compatibility の節へ案内しています。2026年10月31日版のサマリで取り上げた、Build an MCP client の Java のタブと Build an MCP server の Java・Kotlin のタブの注記と同じ趣旨です。

同じ Kotlin のタブの `build.gradle.kts` では、`mcpVersion` が `0.9.0` から `0.16.0` になり、`repositories { mavenCentral() }` のブロックが加わりました。

- [Build an MCP client - MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-client#basic-client-structure)
- [Build an MCP client - MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-client#setting-up-your-environment-4)

## 4. Schema Reference の Tool に composition keyword の注意と例が加わった

2026-07-28 の Schema Reference の `Tool` に、次の変更がありました（追加 5 行・削除 2 行）。

**`inputSchema` の説明に注意が加わりました。** composition keyword（`oneOf`・`anyOf`・`allOf`・`not`）も使えるという既存の説明の後に、使うときは `properties` をスキーマの根に宣言し、分岐は `required` のような存在の検査に留める、という文が加わりました。理由は、型のエラーで失敗するサブスキーマは適用されないサブスキーマと区別できないので、`oneOf` の分岐の中に置いた型の制約は、一致しなかった分岐については強制されないためです。

**例が 2 つ加わりました。** `Tool` の例はこれまで 4 つ（既定の 2020-12 の入力スキーマ、明示した draft-07 の入力スキーマ、パラメーター無し、構造化された内容の出力スキーマ）でした。今回、次の 2 つが加わって 6 つになりました。

- **With a composition input schema**: `find_resource` というツールの例。`id` と `name` を根の `properties` に宣言し、`"oneOf": [{ "required": ["id"] }, { "required": ["name"] }]` でどちらか一方を求める
- **With an array output schema**: `list_users` というツールの例。`outputSchema` の `type` が `array` で、`items` に `id`・`name`・`email` を持つオブジェクトを宣言する

同じ名前のツールの例は、SEP-2106 のページにすでにありました（`list_users` は仕様の Tools のページにも）。これらのページは今回変わっていません。

- [Schema Reference - MCP Docs](https://modelcontextprotocol.io/specification/2026-07-28/schema#tool)

## 新規追加されたページ

<!-- light:new-pages:start -->
今回の対象期間に新たに追加されたページはありません。索引 `llms.txt` に変更はなく、索引側のエントリ数（364 件）と本文 `llms-full.txt` の収録ページ数（159 件。URL としては 158 件）はどちらも前回と同じです。
<!-- light:new-pages:end -->

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
- [**Build an MCP client**](#1-build-an-mcp-client) ([MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-client#query-processing-logic)):  
  Python・TypeScript・Kotlin・Ruby のタブを、最大 `MAX_TOOL_TURNS` 回のツール呼び出しのループに書き直し、TypeScript に版の自動交渉と Ctrl-D・Ctrl-C の処理を、Kotlin に版の注記を加えた（追加 314 行・削除 157 行。詳細はハイライト 1・3 参照）。
- [**Build an MCP server**](#2-build-an-mcp-server) ([MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-server#implementing-the-weather-server-and-tools)):  
  Rust のタブを rmcp `3.4` に合わせて書き直し、ツールがテキストと `outputSchema` に沿った構造化された結果を返す形にした（追加 174 行・削除 72 行。詳細はハイライト 2 参照）。
<!-- light:updated-pages:end -->

## 1. Build an MCP client

変更（追加 314 行・削除 157 行）のタブごとの内訳は、Python が追加 37 行・削除 21 行、TypeScript が追加 94 行・削除 33 行、Kotlin が追加 96 行・削除 48 行、C# が追加 1 行・削除 1 行、Ruby が追加 86 行・削除 54 行です。Java と Rust のタブは変わっていません。ループの内容はハイライト 1 を参照してください。タブごとの変更は次のとおりです。

| タブ | 節 | 変更 |
|---|---|---|
| Python | Imports and Setup | 定数 `MAX_TOKENS`・`MAX_TOOL_TURNS` を追加 |
| Python | Query Processing Logic | `process_query` をループに。コードの後に、アシスタントのメッセージの送り返し方とループの説明を追加 |
| Python | Key Components Explained の 3. Query Processing | 「メッセージの流れを管理する」を、ターンのツール呼び出しをすべて実行して 1 つのメッセージで答えることと、`MAX_TOOL_TURNS` までループすることの 2 項目に |
| Python | Common Customization Points | `MAX_TOOL_TURNS` の調整を追加 |
| Python | How It Works・Best practices | 手順 5 にループを追記。上限を保つ項目を追加 |
| TypeScript | Basic Client Structure | `ContentBlockParam`・`ToolResultBlockParam`・`ToolUseBlock` の import、定数 `MODEL`・`MAX_TOKENS`・`MAX_TOOL_TURNS`、`versionNegotiation` を追加 |
| TypeScript | Query Processing Logic | `processQuery` をループに。コードの後に説明の段落を追加 |
| TypeScript | Interactive Chat Interface | `rl.question()` に `AbortSignal` を渡し、Ctrl-D と Ctrl-C で抜ける処理を追加。`cleanup()` まで進んで終了コード 0 で終わり、`ERR_USE_AFTER_CLOSE` で失敗しない、と説明 |
| TypeScript | How It Works・Best practices | 手順 4〜6 を書き換え。try-catch の項目を `result.isError` の確認に |
| Kotlin | タブの冒頭・Setting up your environment | 版の NOTE、`mcpVersion`、`repositories` のブロック（ハイライト 3） |
| Kotlin | Basic Client Structure | 定数 `MODEL`・`MAX_TOKENS`・`MAX_TOOL_TURNS` を追加 |
| Kotlin | Query processing logic | `processQuery` をループに。節の冒頭の説明を書き換え、コードの後に説明の段落を追加 |
| Kotlin | How it works | シーケンス図にループのブロックを追加し、手順 4〜6 を書き換え |
| Kotlin | Best practices・Common Error Messages | `result.isError` と `MAX_TOOL_TURNS` の項目、`[Stopped after 10 tool-use turns]` の説明を追加 |
| C# | Query processing logic | `MaxOutputTokens` を `1000` から `10000` に |
| Ruby | Basic Client Structure | 定数 `MAX_TOKENS`・`MAX_TOOL_TURNS` を追加 |
| Ruby | Query Processing Logic | `process_query` をループに。節の冒頭の説明を書き換え |
| Ruby | Interactive Chat Interface | `private` のヘルパー（`assistant_content`・`chat`・`anthropic_client`）をこの節のコードへ移した。`assistant_content` に、thinking block を `signature` ごと変えずに返さないと API が後続のリクエストを拒否する、というコメントとともに `ThinkingBlock`・`RedactedThinkingBlock` の処理を追加 |
| Ruby | Key Components Explained の 3. Query Processing | ループ・`isError`・`assistant_content`・`chat` の説明に書き換え |
| Ruby | How It Works・Best practices・Common Error Messages | 手順を 7 つから 8 つに。`isError` と `MAX_TOOL_TURNS` の項目、`[Stopped after 10 tool-use turns]` の説明を追加 |

- [Build an MCP client - MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-client#query-processing-logic-3)
- [Build an MCP client - MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-client#query-processing-logic-5)

## 2. Build an MCP server

変更（追加 174 行・削除 72 行）はすべて Rust のタブです。節ごとの変更は次のとおりです（内容はハイライト 2）。

| 節 | 変更 |
|---|---|
| System requirements | Rust を 1.70 以上から 1.88 以上に |
| Set up your environment | `Cargo.toml` の rmcp・`tokio`・`reqwest` の版を上げ、`tracing`・`tracing-subscriber` を削除 |
| Importing packages and constants | `ErrorData`・`schema_for_output`・`JsonSchema`・`stdio`・`Serialize` を追加し、`Parameters` の import 元を `tool` から `wrapper` に。`Parameters`・`schema_for_output`・`stdio` の役割の説明を追加 |
| Data structures | `Alert`・`Forecast`・`Period` を追加。リクエストの型（`MCPForecastRequest`・`MCPAlertRequest`）は後ろの節へ移した |
| Helper functions | `format_alert`・`format_period` の引数を新しい型に変え、`dual_channel_result` を追加 |
| Implementing the Weather server and tools | リクエストの型をここで定義し、各フィールドに doc コメントを追加。`Weather` に `#[derive(Clone)]`、`#[tool_router(router = tool_router)]`。2 つのツールを `output_schema` 付きで `Result<CallToolResult, ErrorData>` を返す形に |
| Implementing the ServerHandler | `#[tool_handler(router = self.tool_router)]`。`get_info` が `ServerConfig` を返し `server_info` を設定する |
| Running the server | `(tokio::io::stdin(), tokio::io::stdout())` の組の代わりに `Weather::new().serve(stdio())` |

- [Build an MCP server - MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-server#data-structures)
- [Build an MCP server - MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-server#implementing-the-serverhandler)

## 軽微な更新

<!-- light:minor-updates:start -->
今回差分が出たファイルは `llms-full.txt` の 1 件で、差分のあった 4 ページのうち、大幅更新の 2 ページのほかに、次の 2 ページで内容が変わりました。

**機能改善**

- Schema Reference の `Tool` で、`inputSchema` の説明に composition keyword を使うときの注意を追加し、`find_resource`（`oneOf` の入力スキーマ）と `list_users`（配列の出力スキーマ）の例を追加（詳細はハイライト 4 参照） — [Schema Reference](https://modelcontextprotocol.io/specification/2026-07-28/schema#tool)
- SEP Guidelines の Step-by-Step Process の手順 3 に、PR のタイトルを `sep: propose task cancellation` のようにすることを追加し、`CONTRIBUTING.md` の PR タイトルの指針へのリンクを追加 — [SEP Guidelines](https://modelcontextprotocol.io/community/sep-guidelines#step-by-step-process)
- 同じ節の手順 4 に、PR の番号が決まったら PR のタイトルを `sep(SEP-1850): describe the proposal` のように改めることを追加。追加のコミットで足り、amend や force-push は要らない。この SEP に関する後続の PR は `SEP-1850` をスコープとして残し、説明欄で元の SEP にリンクする — [SEP Guidelines](https://modelcontextprotocol.io/community/sep-guidelines#step-by-step-process)
<!-- light:minor-updates:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-11-02.md](./archives/latest/2026-11-02.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-11-02.md](./archives/latest-detail/2026-11-02.md)

<!--
base_commit: acb459e04e57acda73f439e58d2759ea5599cdf6
head_commit: b3f45341023a7453d8b8e8e11e025447ef991a24
generated_at_full: 2026-11-07T15:21:16+09:00
-->
