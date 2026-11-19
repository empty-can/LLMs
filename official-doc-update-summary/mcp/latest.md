---
対象期間: 2026年11月17日 〜 2026年11月18日
作成日: 2026-11-18
---

# MCP 公式ドキュメント更新サマリ

```markdown
今回の対象期間の取り込みは 1 回で、入力の 2 ファイルとも差分がありました（`llms-full.txt` は追加 938 行・削除 429 行で、そのうち 309 行ずつは SEP 2 ページの収録位置の移動、`llms.txt` は追加 2 行）。MCP Inspector の負荷テストを解説するページが新しく加わり、Build an MCP server のサンプルはツールの失敗をエラーとして返す形に改められました。

主要なものを以下に挙げます。

1. MCP Inspector の負荷テストを 1 ページにまとめた Load testing が加わった。Web client・CLI・mcpdo の 3 つの入口から同じエンジンで負荷をかける方法と、要約の各フィールド、シナリオ、段階的な負荷、しきい値とベースライン比較による CI のゲートなどを説明している
2. CLI client・mcpdo connection client・Configuration and flags の負荷テストの記述が Load testing への案内に置き換わり、CLI client には「Load testing a tool」の節と、終了コード `130`（中断）の行が加わった
3. Web client に、Web バックエンドが保持しているセッションを一覧して終了させる Active sessions の節と、Tools 画面の Load test ボタンの説明が加わった
4. Build an MCP server で、天気サーバーのサンプルが取得の失敗を `ToolError` や `isError` でエラーとして返すようになったほか、州コードの大文字化、C# の .NET 10 への引き上げ、Spring AI の stdio の指定などが直った
5. 仕様 2026-07-28 で、`_meta` の予約キーの表に `io.modelcontextprotocol/serverInfo` の行が加わり、例のリクエストに必須の `_meta` フィールドが入り、拡張を広告するクライアントの例が `_meta` の形になった。`_meta` 節を指すリンク 17 か所のアンカーも `#_meta` に直った
```

## ハイライト

1. [**MCP Inspector の負荷テストを解説する Load testing のページが新設された**](./latest-detail.md#1-mcp-inspector-の負荷テストを解説する-load-testing-のページが新設された):  
  `docs/2026-07-28/tools/inspector/load-testing`（412 行・見出し 17 個）が本文と索引に加わった。Inspector の接続をそのまま使ってツールを繰り返し同時に呼び、レイテンシとエラー率の要約を得る機能を、Web client・CLI・mcpdo の 3 つの入口に分けて説明している。負荷テスト自体は base の時点から CLI client などに書かれていたが、シナリオ（`--load-scenario`）、段階的な負荷（`--load-steps` / `--load-ramp`）、open loop、ベースライン比較（`--load-baseline`）、セッションの churn、通知の fan-out、複数の生成プロセス（`--load-workers`）などのフラグは、base の `llms-full.txt` には出てこなかった。
2. [**CLI と mcpdo と設定のページの負荷テストの記述が Load testing に集約された**](./latest-detail.md#2-cli-と-mcpdo-と設定のページの負荷テストの記述が-load-testing-に集約された):  
  CLI client に「Load testing a tool」の節が新設され、Exit codes の表では `10` の説明がしきい値とベースラインの両方に広がり、`130`（Ctrl+C か SIGTERM による中断）の行が加わった。CLI client の CI gates、mcpdo connection client の Addressing a connection、Configuration and flags の Load test の行は、フラグを列挙する代わりに Load testing のページを指すようになった。mcpdo connection client には「Load testing」の節が、MCP Inspector の Where to go next には Load testing のカードが加わった。
3. [**Web client にセッションを一覧して終了させる Active sessions の節が加わった**](./latest-detail.md#3-web-client-にセッションを一覧して終了させる-active-sessions-の節が加わった):  
  Web バックエンドは接続をセッションとして保持し、タブを閉じたり再読み込みしたりしても 60 秒は残す。ヘッダーの Active sessions ボタンから、すべてのタブのセッションを状態（This tab / Attached / Detached / Closed）付きで一覧し、Terminate で終了させられる（stdio サーバーのプロセスも終わる）。一覧と終了のルートは `GET /api/mcp/sessions` と `DELETE /api/mcp/sessions/<id>`。Tools の節には、Load test ボタンを説明する「Load testing」の小節が加わった。
4. [**Build an MCP server のサンプルがツールの失敗をエラーとして返すようになった**](./latest-detail.md#4-build-an-mcp-server-のサンプルがツールの失敗をエラーとして返すようになった):  
  天気サーバーを作るチュートリアル（追加 44 行・削除 27 行）で、データを取得できなかったときの返し方が、エラー文の文字列を普通の結果として返す形から、エラーとして返す形に変わった。Python は `ToolError` を送出し、TypeScript・Kotlin・Go は結果に `isError` を付ける。ほかに、州コードの大文字化（Python・Kotlin・C#）、TypeScript の警報 API の URL、C# の .NET 10 への引き上げと `--prerelease` の削除、Java（Spring AI）の Windows 向けの設定の stdio の指定などが直った。
5. [**仕様 2026-07-28 の例と表がリクエストごとのメタデータの規則に揃った**](./latest-detail.md#5-仕様-2026-07-28-の例と表がリクエストごとのメタデータの規則に揃った):  
  Base Protocol の Overview（`basic/index`）で、`_meta` の予約キーの表に `io.modelcontextprotocol/serverInfo` の行が加わり、OpenTelemetry のトレースコンテキストの例に必須の `_meta` フィールドが入った。Versioning and Compatibility では、MCP Apps 拡張を広告するクライアントの例が `capabilities` から `_meta` の `io.modelcontextprotocol/clientCapabilities` の形になった。Streamable HTTP の HTTP リクエストの例 3 つには `Host` と `Accept` の行が加わった。`_meta` 節を指すリンクは 13 ページの 17 か所でアンカーが `#meta` から `#_meta` になった。

## 新規追加されたページ

- [**Load testing**](./latest-detail.md#1-load-testing) ([MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/load-testing)):  
  MCP Inspector の負荷テストを、Web client・CLI・mcpdo の 3 つの入口と、要約のフィールド・シナリオ・段階的な負荷・しきい値とベースライン比較・複数のセッションなどの節で説明する 412 行のページ（詳細はハイライト 1 参照）。

## 大幅に更新されたページ

- [**Build an MCP server**](./latest-detail.md#1-build-an-mcp-server) ([MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-server)):  
  天気サーバーのサンプルで、取得の失敗を `ToolError` や `isError` でエラーとして返すようになり、州コードの大文字化、C# の .NET 10 への引き上げ、Spring AI の stdio の指定などが直った（追加 44 行・削除 27 行。詳細はハイライト 4 参照）。

## 軽微な更新

既存のページで本文が変わったのは、Build an MCP server を除いて 33 件です。ほかに、SEP 2 ページの収録位置の移動、`llms-full.txt` の先頭の前置き、索引 `llms.txt` の 2 エントリの追加がありました。

**新機能**

- Web client に、Web バックエンドが保持しているセッションを一覧して終了させる Active sessions の節が加わった（詳細はハイライト 3 参照） — [Web client](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/web#active-sessions)
- Web client の Tools に、Load test ボタンを説明する Load testing の小節が加わり、スクリーンショットとその説明文が差し替わった（詳細はハイライト 3 参照） — [Web client](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/web#load-testing)

**機能改善**

- CLI client に「Load testing a tool」の節が加わり、Methods の表の `tools/call` の行に `--load` の注記が入った（詳細はハイライト 2 参照） — [CLI client](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/cli#load-testing-a-tool)
- CLI client の Exit codes の表で、`10` の説明がしきい値とベースラインの両方に広がり、`130`（`--load` の実行の中断）の行が加わった（詳細はハイライト 2 参照） — [CLI client](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/cli#exit-codes-and-error-envelopes)
- CLI client の CI gates で、負荷テストのしきい値の項目が、5 つのしきい値のフラグとベースライン比較を挙げて Load testing を指す説明になった（詳細はハイライト 2 参照） — [CLI client](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/cli#ci-gates)
- mcpdo connection client の Addressing a connection の `--load` の段落が Load testing への案内の 1 文になり、「Load testing」の節が新設された（詳細はハイライト 2 参照） — [mcpdo connection client](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/mcpdo#load-testing)
- Configuration and flags の CLI-only flags の表で、Load test の行がフラグの列挙から代表的なフラグの例に変わり、参照先が Load testing になった（詳細はハイライト 2 参照） — [Configuration and flags](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/configuration#cli-only-flags)
- MCP Inspector の Where to go next に、Load testing のカードが加わった（詳細はハイライト 2 参照） — [MCP Inspector](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector#where-to-go-next)
- Build an MCP client で、Python・TypeScript・Kotlin・Ruby・Rust のサンプルが使うモデルが `claude-opus-5` から `claude-haiku-5-5` になった。C# のサンプルも `claude-haiku-5-5` を指定する（追加 19 行・削除 27 行で、50 行に届かないため軽微な更新に分類） — [Build an MCP client](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-client#imports-and-setup)
- Build an MCP client の C# のサンプルで、パッケージが `Anthropic.SDK` から `Anthropic` に替わり（`using Anthropic;`）、クライアントを `new AnthropicClient(new() { ApiKey = ... }).AsIChatClient("claude-haiku-5-5")` で作るようになった。モデルの指定は `ChatOptions` の `ModelId` から `AsIChatClient` の引数に移った — [Build an MCP client](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-client#query-processing-logic-4)
- Build an MCP client の C# で、System Requirements の .NET が 8.0 から 10.0 になり、`dotnet add package ModelContextProtocol` から `--prerelease` が外れた — [Build an MCP client](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-client#setting-up-your-environment-5)
- Build an MCP client の C# の Key Components Explained の Query Processing で、「入力をサーバーに送り、サーバーが処理して応答を返す」という説明が、「入力を Claude に送り、Claude がツールを求めたらクライアントがサーバーで呼び出して結果を Claude に返し、Claude の応答を表示する」になった。Running the Client の、チャットでできることの一覧からは「See tool executions」が外れた — [Build an MCP client](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-client#3-query-processing-2)
- Build an MCP client の TypeScript で、`build` スクリプトの `chmod` が Node の `chmodSync` になり、Main Entry Point の使い方の表示が `node index.ts` から `node build/index.js` になった — [Build an MCP client](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-client#main-entry-point-2)
- Build an MCP client の Java で、System Requirements の「npx package manager」が「npm」になり、`npm install -g npx` を実行する手順が、`npx` を含む npm を入れる 1 行になった — [Build an MCP client](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-client#setting-up-your-environment-3)
- Build an MCP client の Python の Key Components Explained の Query Processing で、「Maintains conversation context」が「Starts a new conversation for each query」になった — [Build an MCP client](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-client#3-query-processing)
- Connect to local MCP servers の Troubleshooting で、Windows のログを見るコマンドが `type "%APPDATA%\Claude\logs\mcp*.log"` から PowerShell の書き方の `type "$env:AppData\Claude\logs\mcp*.log"` になった — [Connect to local MCP servers](https://modelcontextprotocol.io/docs/2026-07-28/develop/connect-local-servers#troubleshooting)
- Connect to local MCP servers の Troubleshooting の「ENOENT error and `${APPDATA}` in paths on Windows」で、設定例が `brave-search` サーバーの断片から、`mcpServers` で囲んだ `filesystem` サーバーの設定（Desktop と Downloads のパスを渡し、`env` に `APPDATA` を置く）になった — [Connect to local MCP servers](https://modelcontextprotocol.io/docs/2026-07-28/develop/connect-local-servers#troubleshooting)
- Connect to local MCP servers の Next Steps の「Explore other servers」のカードで、リンク先が GitHub の `modelcontextprotocol/servers` から MCP Registry（`https://registry.modelcontextprotocol.io/`）になり、説明が「MCP Registry に公開されたサーバーを見る」になった — [Connect to local MCP servers](https://modelcontextprotocol.io/docs/2026-07-28/develop/connect-local-servers#next-steps)
- Connect to remote MCP Servers の Next Steps の「Explore available servers」のカードも、リンク先が MCP Registry になり、説明が同じ文になった — [Connect to remote MCP Servers](https://modelcontextprotocol.io/docs/2026-07-28/develop/connect-remote-servers#next-steps)
- Overview（Base Protocol）の `_meta` で、予約キーの表に `io.modelcontextprotocol/serverInfo` の行が加わり、トレースコンテキストの例に必須の `_meta` フィールドが入った（詳細はハイライト 5 参照） — [Overview](https://modelcontextprotocol.io/specification/2026-07-28/basic/index#_meta)
- Versioning and Compatibility の Extension Negotiation で、拡張を広告するクライアントの例が `_meta` の `io.modelcontextprotocol/clientCapabilities` の形になり、Tasks 拡張の例が `server/discover` の結果だと明記された（詳細はハイライト 5 参照） — [Versioning and Compatibility](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning#extension-negotiation)
- Streamable HTTP の HTTP リクエストの例 3 つに、`Host` と `Accept` の行が加わった（詳細はハイライト 5 参照） — [Streamable HTTP](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http#standard-request-headers)
- Architecture の Capability Negotiation で、機能を「リクエストごとに」宣言する、という文から「on each request」が外れた（詳細はハイライト 5 参照） — [Architecture](https://modelcontextprotocol.io/specification/2026-07-28/architecture/index#capability-negotiation)
- Sampling の Creating Messages のリクエストの例から、`"includeContext": "thisServer"` が外れた。同じページは、`includeContext` の値 `"thisServer"` と `"allServers"` を非推奨とし、サーバーはこれらを使うのを避けるべき（SHOULD）としている — [Sampling](https://modelcontextprotocol.io/specification/2026-07-28/client/sampling#creating-messages)
- Pagination の Request Format の例で、`cursor` が `eyJwYWdlIjogMn0=`（`{"page": 2}`）から `eyJwYWdlIjogM30=`（`{"page": 3}`）になり、直前の Response Format の例の `nextCursor` と同じ値になった — [Pagination](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/pagination#request-format)
- Authorization（仕様）の Step-Up Authorization Flow の手順 4 が、「新しい認可で元のリクエストを数回まで再試行し、恒久的な認可の失敗として扱う」から、「数回まで再試行し、それでも失敗したら恒久的な認可の失敗として扱う」になった — [Authorization](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index#step-up-authorization-flow)
- Key Changes の Minor changes の 6 番目（リソースが見つからないときのエラーコードを `-32002` から `-32602` に変える）に、SEP-2164 へのリンクが付いた — [Key Changes](https://modelcontextprotocol.io/specification/2026-07-28/changelog#minor-changes)

**その他**

- 13 ページの 17 か所で、`_meta` 節を指すリンクのアンカーが `#meta` から `#_meta` になった。Tools の `$ref` の解決へのリンクは `#\$ref-resolution` に、Resources の Common URI Schemes へのリンクは `#https//` になった（詳細はハイライト 5 参照） — [Overview](https://modelcontextprotocol.io/specification/2026-07-28/basic/index#_meta)
- Inspector の Recipes の Hosting on a network で、「Two further caveats」が「Three further caveats」になった。続く一覧は base の時点から 3 項目（3 つ目は IPv6 リテラルでは MCP Apps が表示できないこと）で、数の書き間違いの訂正 — [Recipes](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/recipes#hosting-on-a-network)
- Local Server Security の冒頭の段落と Next Steps の Security Best Practices のカードで、「session hijacking」が「state handle hijacking」になった。Security Best Practices の見出し「State Handle Hijacking」に合わせた語 — [Local Server Security](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/local-server-security)
- Security Best Practices の Local MCP Server Compromise の Mitigation で、「MCP servers intending for their servers to be run locally」が「MCP server developers intending ...」になった — [Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices#mitigation-5)
- Specification（仕様のトップ）の Features で、Elicitation の説明が「Server-initiated requests for additional information from users」から「Server requests for ...」になった — [Specification](https://modelcontextprotocol.io/specification/2026-07-28/index#features)
- Overview（Base Protocol）の Error Responses で、「due a malformed request」が「due to a malformed request」になった — [Overview](https://modelcontextprotocol.io/specification/2026-07-28/basic/index#error-responses)
- Authorization（仕様）の Token Handling で、「a HTTP 401」が「an HTTP 401」になった — [Authorization](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index#token-handling)
- Resources の Capabilities で、`subscribe` の説明の `subscriptions/listen` と `resourceSubscriptions` がコード表記になり、余分な空白が外れた — [Resources](https://modelcontextprotocol.io/specification/2026-07-28/server/resources#capabilities)
- Resources の Custom URI Schemes で、「in to account」が「into account」になった — [Resources](https://modelcontextprotocol.io/specification/2026-07-28/server/resources#custom-uri-schemes)
- Caching の Cacheable Model で、`ttlMs` と `cacheScope` の前のカンマのあとに空白が入った — [Caching](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/caching#cacheable-model)
- Caching の Security Considerations で、「initial requests authorization context」が「initial request's authorization context」になり、文末の句読点が整った — [Caching](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/caching#security-considerations)
- Multi Round-Trip Requests の Basic Workflow のシーケンス図で、再試行への応答の型が `ToolCallResult` から `CallToolResult` になった — [Multi Round-Trip Requests](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr#basic-workflow)
- Elicitation の URL Mode Flow のシーケンス図で、`tools/call(id: 2, Accept Response, requestState))` の余分な閉じ括弧が外れた — [Elicitation](https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation#url-mode-flow)
- SEP-1303: Input Validation Errors as Tool Execution Errors（202 行）と SEP-1319: Decouple Request Payload from RPC Methods Definition（107 行）の 2 ページで、本文 `llms-full.txt` での収録位置が、SEP-1302 の直後（SEP-414 の前）から、Roadmap の直後（SEP-1330 の前）へ移った。移った 309 行は 1 行も変わっておらず、行単位の差分では追加・削除とも 309 行に数えられるが、本文の変更ではない。索引 `llms.txt` での位置（SEP-1302 と SEP-1330 の間）も変わっていない — [SEP-1303](https://modelcontextprotocol.io/seps/1303-input-validation-errors-as-tool-execution-errors) / [SEP-1319](https://modelcontextprotocol.io/seps/1319-decouple-request-payload-from-rpc-methods-definiti)
- 本文 `llms-full.txt` の先頭に、`# Model Context Protocol` の見出しと、「このファイルは非常に大きく、途中で切れることがある。内容の索引は `https://modelcontextprotocol.io/llms.txt` を参照」という引用の 1 行からなる、空行を含めて 4 行の前置きが加わった。最初のページ（Build an MCP client）はその後ろから始まる
- 索引 `llms.txt` に、Load testing のエントリが `docs/2026-07-28/` 版と `docs/draft/` 版の 2 件加わった（どちらも mcpdo connection client と Configuration and flags の間）。エントリ数は 360 件から 362 件（一意の URL も 362 件）、ファイルは 365 行から 367 行になった（末尾に改行が無いため、改行の数では 364 から 366） — [Load testing](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/load-testing)

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-11-17.md](./archives/latest/2026-11-17.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-11-17.md](./archives/latest-detail/2026-11-17.md)

<!--
base_commit: ab0340993aa5987d27a891141698d57dc355b88b
head_commit: 831f1678213f7b2708b300fbfd4e73aa7b6ac427
generated_at_full: 2026-11-19T15:40:10+09:00
-->
