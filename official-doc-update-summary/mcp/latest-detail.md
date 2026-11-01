---
対象期間: 2026年10月30日 〜 2026年10月31日
作成日: 2026-10-31
---

# MCP 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
今回の対象期間の取り込みは 1 回で、新規ページはなく、`llms-full.txt` の 32 ページに差分がありました。うち 17 ページはタブなどの書式の書き換えだけで、内容が変わったのは 15 ページ（うち 2 件は 50 行以上の大幅更新）です。中心は、Build an MCP client の Rust 版が Messages API を直接呼ぶ形に書き直されたことと、MCP Inspector に負荷試験と `Host` ヘッダーの検査が加わったことです。

主要なものを以下に挙げます。

1. Build an MCP client の Rust 版が書き直され、`genai` クレートをやめて Messages API を直接呼び、プロトコルの版の自動交渉・`outputSchema` による結果の検証・複数回のツール呼び出しのループを備えた
2. MCP Inspector の CLI に、ツールを繰り返し並行して呼ぶ負荷試験の `--load` と、エラー率や p99 のしきい値を超えると終了コード `10` で終わる CI ゲートが加わった（mcpdo でも使える）
3. Inspector の Web バックエンドがすべての経路の前で `Host` ヘッダーを許可リストと照合するようになり（`MCP_INSPECTOR_ALLOWED_HOSTS`）、`INSPECTOR_TLS_KEY_PATH`・`INSPECTOR_TLS_CERT_PATH` で Web UI を `https` で配信できるようになった
4. Java と Kotlin のサンプルに、各 SDK の最新の安定版が対応するプロトコルの版は `2025-11-25` で、`2026-07-28` にしか対応しない相手とはつながらないという注記が加わり、SDKs のページも、SDK は新しいリビジョンを独自の予定で採用すると明記した
5. `llms-full.txt` で、タブが `> [tab]` の行で始まる引用のブロックになり、アコーディオンとカードにも `[accordion]`・`[card]` の印が付いた。生の差分の大半はこの書き換え
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**Build an MCP client の Rust 版が Messages API を直接呼ぶ形に書き直された**](#1-build-an-mcp-client-の-rust-版が-messages-api-を直接呼ぶ形に書き直された):  
  Build an MCP client の Rust のタブが書き直された。Claude の呼び出しを `genai` クレートから `reqwest` による Messages API の直接の呼び出しに替え、rmcp を `3.4` のクライアント部分だけにして、`ClientLifecycleMode::Auto` で `2026-07-28` を試し `2025-11-25` にフォールバックする形にした。ツールの `outputSchema` による結果の検証、最大 10 回のツール呼び出しのループ、拒否されたツール呼び出しを `is_error` 付きの `tool_result` で Claude に返す処理も加わった。
2. [**MCP Inspector の CLI に負荷試験と CI ゲートが加わった**](#2-mcp-inspector-の-cli-に負荷試験と-ci-ゲートが加わった):  
  Inspector の CLI の `tools/call` に、ツールを繰り返し並行して呼び、結果の代わりにレイテンシとエラー率の要約を出す `--load` の一連のフラグが加わった。`--load-max-error-rate`・`--load-max-p99` のしきい値を超えると終了コード `10` で終わる。サーバーが HTTP 429 を返したときの終了コード `11`（`rate_limited`）も加わり、mcpdo の `tools/call` も同じフラグを受け付ける。
3. [**Inspector の Web バックエンドが Host ヘッダーを検査し UI を HTTPS で配信できるようになった**](#3-inspector-の-web-バックエンドが-host-ヘッダーを検査し-ui-を-https-で配信できるようになった):  
  Inspector の Web バックエンドは、`GET /` を含むすべての経路の前で `Host` ヘッダーを許可リストと照合し、合わなければ `403` を返す。DNS リバインディングを使うページがトークンを読み取るのを防ぐためで、`Host` を書き換えるリバースプロキシのために `MCP_INSPECTOR_ALLOWED_HOSTS` で許可するホスト名を足せる。`INSPECTOR_TLS_KEY_PATH`・`INSPECTOR_TLS_CERT_PATH` を設定すると、Web UI 自体を `https` で配信できる。
4. [**Java と Kotlin のサンプルに対応するプロトコルの版の注記が加わった**](#4-java-と-kotlin-のサンプルに対応するプロトコルの版の注記が加わった):  
  Build an MCP server の Java・Kotlin のタブと Build an MCP client の Java のタブに、サンプルは各 SDK の最新の安定版が対応するプロトコルの版 `2025-11-25` を使い、`2026-07-28` にしか対応しない相手とはつながらない、という注記が加わった。SDKs のページも「どの SDK も同じ機能を提供する」という記述をやめ、SDK は新しいリビジョンを独自の予定で採用するので、対応するリビジョンは各 SDK のドキュメントで確かめるよう求めている。
5. [**llms-full.txt でタブが印付きの引用として出るようになった**](#5-llms-fulltxt-でタブが印付きの引用として出るようになった):  
  `llms-full.txt` で、これまで太字の行で始まり中身が地の文として続いていたタブが、`> [tab] 名前` の行で始まり中身も引用の中に入るブロックになった。すでに引用だったアコーディオンとカードにも `[accordion]`・`[card]` の印が付いた。24 ページに及び、生の差分の大半と、差分のあった 32 ページのうち 17 ページの変更はこの書き換えだけ。
<!-- light:highlight-list:end -->

## 1. Build an MCP client の Rust 版が Messages API を直接呼ぶ形に書き直された

今回の取り込みは 1 回で、差分は本文 `llms-full.txt` だけです。索引 `llms.txt` は変わらず（エントリ数は 364 件のまま）、`llms-full.txt` の総行数は 45,863 行から 46,205 行になり、収録ページ数は 159 件（`examples` が 2 回収録されているため、URL としては 158 件）で変わっていません。ファイル全体の生の差分は追加 10,113 行・削除 9,771 行ですが、その大半はタブの書式の書き換えです（ハイライト 5）。書き換えを戻してページごとに数えると、内容が変わったのは 15 ページ・追加 553 行・削除 239 行で（数え方はハイライト 5 の末尾）、50 行以上の変更は Build an MCP client（追加 445 行・削除 195 行）と Configuration and flags（追加 47 行・削除 8 行）の 2 件です。Build an MCP client の変更のほとんどは Rust のタブ（追加 438 行・削除 190 行）にあります。

**依存と前提が変わりました。** System Requirements は「Linux のシステム」から「システム」になり、Rust と Cargo は「最新の安定版」から「1.88 以降」になりました。`Cargo.toml` の依存からは `genai`・`tracing`・`tracing-subscriber` が外れ、`jsonschema`（`0.59`）と `serde`（`derive` 機能付き）が加わりました。rmcp は `0.8.0` から `3.4` になり、`default-features = false` でクライアントと子プロセスの stdio トランスポートの機能だけを有効にしています。`reqwest` は `0.12.23` から `0.13`（`json` 機能付き）になりました。

**Claude を Messages API で直接呼ぶようになりました。** これまでは `genai` クレートの `Client` で Claude を呼び、ツールも `genai` の型で表していました。新しいコードは `reqwest` で Messages API の `/v1/messages` に POST し、`x-api-key` と `anthropic-version`（`2023-06-01`）のヘッダーを付けます。直接呼ぶ理由として、各応答の content block をそのまま保てることを挙げており、アシスタントの応答は次のリクエストで、thinking block とその `signature` も含めて手を加えずに送り返します。`ANTHROPIC_API_KEY` はリクエストのたびに読み、`ANTHROPIC_BASE_URL` でエンドポイントを差し替えられます（ローカルの代替サーバーに向けるため）。定数として `MAX_TOKENS`（`10000`。thinking と応答の合計の上限）・`MAX_TOOL_TURNS`（`10`）・`REQUEST_TIMEOUT`（120 秒）が加わりました。

**サーバーとはプロトコルの版を交渉して接続します。** `connect_to_server` は、`ClientConfig` でクライアントの名前を `mcp-client-rust` とし、`serve_with_lifecycle` に `ClientLifecycleMode::Auto` を渡して接続します。これは `server/discover` で `2026-07-28` を試し、`2025-11-25` の `initialize` のハンドシェイクにフォールバックするもので、Python と TypeScript のクライアントに合わせたものだと説明しています。rmcp の `serve` だけでは旧来のハンドシェイクしか行わず、根が配列の `outputSchema` のような現行リビジョンの機能が使えないためです。接続すると、取り決めたプロトコルの版をツール名と並べて表示します（例: `Connected over protocol 2026-07-28 with tools: ["get_alerts", "get_forecast"]`）。

**ツールの結果を検証する節が新設されました。** 「Validating Structured Tool Output」の節の説明によると、仕様はツールが宣言した `outputSchema` に照らして `structuredContent` を検証するようクライアントに求めていますが、rmcp はこれを行いません。そこでクライアントがツールごとに `jsonschema` の検証器をコンパイルしておき、成功した結果を検証します。`is_error` が立った結果は対象外で、スキーマを宣言したツールが構造化された内容を返さなければエラーとします。

**ツール呼び出しはループになりました。** これまでの `process_query` は、最初の応答で求められたツールを実行して結果を送り、次の応答のテキストを集めて終わっていました。新しいコードは、Claude がツールを呼ばずに答えるまで、最大 `MAX_TOOL_TURNS` 回ループします。サーバーが拒否したツール呼び出しはクエリを打ち切らずに `is_error` 付きの `tool_result` として返し、すべての `tool_use` に対応する結果を 1 つの user メッセージにまとめて送ります。結果は、これまでの「結果全体を JSON にした文字列」ではなく、テキストのブロックをつないだものを送り、テキストのブロックが無いときは `structured_content` をシリアライズして代わりに送ります。上限に達すると `[Stopped after 10 tool-use turns]` を加えます。

**API キーが無くても接続までは試せます。** `.env` は任意になり（無ければ環境変数から読む）、`ANTHROPIC_API_KEY` が未設定か空なら、サーバーに接続してツールを一覧した後、キーの設定方法を表示して終了します。

節の構成は、「Converting MCP Tools」がなくなって同じ `convert_tools` 関数が末尾の新しい節「Describing Tools to the Model」に移り（Messages API 向けの `ToolDefinition` を返す）、「Query Processing Logic」が「Sending Model Requests」の前に移りました。各節の詳細は「大幅に更新されたページ」の表を参照してください。

- [Build an MCP client - MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-client#server-connection-management-5)
- [Build an MCP client - MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-client#validating-structured-tool-output)

## 2. MCP Inspector の CLI に負荷試験と CI ゲートが加わった

CLI client の CI gates の節に、`--load-max-error-rate <fraction>` と `--load-max-p99 <ms>` の項目が加わり、負荷試験の `--load` の一連のフラグが説明されました。

- **`--load`**（`tools/call --tool-name` と併用）: ツールを繰り返し並行して呼び、結果の代わりにレイテンシとエラー率の要約を出す。実行は `--load-duration <sec>`（`--load-requests` を指定しないときの既定は `10`）と `--load-requests <n>` で区切られ、実行中の呼び出しは最後まで終える
- **`--load-concurrency <n>`**（既定 `10`）: 同時に実行中にする呼び出しの上限
- **`--load-connections <n>`**（既定 `1`、`--load-concurrency` 以下、HTTP と SSE のサーバーのみ）: 計測を始める前に開いておく独立したセッションの数。呼び出しをこれらに振り分ける
- **`--load-rate <n>`**（既定は無制限）: 1 秒あたりに始める呼び出しの上限
- **`--load-max-error-rate <fraction>` と `--load-max-p99 <ms>`**: 負荷試験をゲートにする。要約を出した後、失敗した呼び出しの割合が指定の比率（`0`〜`1`。`0` なら 1 件でも失敗があれば失敗）を超えたとき、p99 のレイテンシが指定のミリ秒を超えたとき、または 1 件も呼び出しが完了しなかったときに、終了コード `10` で終わる

例として `mcp-inspector --cli <server> --method tools/call --tool-name get_weather --load --load-requests 200 --load-max-p99 500` が加わりました。

Exit codes and error envelopes の表には 2 つの終了コードが加わりました。`10` は、`--load` の実行が 2 つのしきい値のどちらかを破ったときで、要約が先に出て、エラーのエンベロープの `code` がしきい値の名前（`load_error_rate_exceeded` か `load_p99_exceeded`）になります。`11` は、サーバーが HTTP 429 を返したときで、`code` は `rate_limited` です。エンベロープには `method` が入り、サーバーが解釈できる `Retry-After` ヘッダーを送ったときは、`retryAfter`（ヘッダーの値そのまま）と `retryAfterMs` も入ります。`code` の値の一覧にも `rate_limited` が加わりました。

mcpdo の `tools/call` も同じ一連のフラグを受け付け、同じ既定値と同じ要約で、デーモンの中で接続に対して実行します（`--load-connections` の追加のセッションは保存済みの資格情報だけで開き、実行が終わるまで同じ接続への後続のコマンドは待たされる）。Configuration and flags の CLI-only flags の表にも「Load test」の行として 8 つのフラグが加わりました。

- [CLI client - MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/cli#ci-gates)
- [mcpdo connection client - MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/mcpdo#addressing-a-connection)

## 3. Inspector の Web バックエンドが Host ヘッダーを検査し UI を HTTPS で配信できるようになった

**`Host` ヘッダーの許可リストが加わりました。** Web client の Host binding and origins の節によると、この許可リストは `GET /` を含むすべての経路の前で働き、`Host` が次のいずれでもなければ `403` を返します。ポートは比べません。

- `localhost` か `*.localhost` の名前
- IPv4 か、角括弧で囲んだ IPv6 のリテラル
- バインドしたホスト（Configuration and flags によると、ワイルドカードでない場合）
- `ALLOWED_ORIGINS` の各エントリのホスト名
- `MCP_INSPECTOR_ALLOWED_HOSTS` のエントリ

同じ節は、同一オリジンの `GET /` には `Origin` ヘッダーが付かないのでオリジンの許可リストでは検査されず、DNS リバインディングを使うページがこのページを読み込んでトークンを読み取るのを止めるのは `Host` の検査だ、と説明しています（`GET /` は再読み込みやブックマークでも使えるよう、トークンを HTML に埋め込んで返す）。Security の The web backend and its API token の節にも、同じ説明が加わりました。

Configuration and flags の Web backend environment variables の表には `MCP_INSPECTOR_ALLOWED_HOSTS` が加わりました。カンマ区切りで、`Host` を書き換えるリバースプロキシのために許可するホスト名を足すもので、`.` で始まるエントリ（`.example.com`）はそのドメインとサブドメインを許します。スキーム・ポート・パス・ワイルドカード・空白を含むエントリは警告とともに捨てられます。

**Web UI を `https` で配信できるようになりました。** 同じ表に `INSPECTOR_TLS_KEY_PATH`（Web UI のリスナーの PEM の秘密鍵）と `INSPECTOR_TLS_CERT_PATH`（その鍵の PEM の証明書またはチェーン）が加わりました。両方を設定すると UI を `https` で配信します。片方だけの設定、読めないファイル、組にならない鍵と証明書は起動時のエラーで、`http` にはフォールバックしません。空の値は未設定とみなします。対象は UI のリスナーだけで、サンドボックスと app-origin のリスナーは `http` のままです。両方が設定されていると、CLI の `--print-handoff` は `https://` のディープリンクを出します。

これに合わせて、Web client の Apps の節には、サンドボックスの URL が既定で `http` のため `https` の Inspector のページでは混在コンテンツとしてフレームが止められる点は、プロキシ経由で `https` にした場合も 2 つの TLS の変数で `https` にした場合も同じだ、という説明が加わりました。Recipes の Hosting on a network の表の「Behind TLS or a reverse proxy」の行にも、プロキシが `Host` を `ALLOWED_ORIGINS` に無い名前に書き換えるなら `MCP_INSPECTOR_ALLOWED_HOSTS=inspector.example.com`（ドメインとサブドメインなら `.example.com`）も設定しないとバックエンドが `403` を返すこと、プロキシを使わなければ 2 つの TLS の変数で UI 自体を `https` で配信できることが加わりました。

- [Web client - MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/web#host-binding-and-origins)
- [Configuration and flags - MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/configuration#web-backend-environment-variables)

## 4. Java と Kotlin のサンプルに対応するプロトコルの版の注記が加わった

Build an MCP server の Java と Kotlin のタブ、Build an MCP client の Java のタブの冒頭に、NOTE が加わりました。サンプルは、各 SDK（Java SDK・Kotlin SDK）の最新の安定版が対応する MCP プロトコルの版 `2025-11-25` を使う、という内容です。サーバーの NOTE は「その版にも対応するクライアントからは接続できるが、`2026-07-28` にしか対応しないクライアントは接続できない」、クライアントの NOTE は「その版を受け付けるサーバーには接続できるが、`2026-07-28` しか受け付けないサーバーには接続できない」としており、いずれも仕様の versioning の backward compatibility の節へ案内しています。

SDKs の Getting Started も、「各 SDK は同じ機能を提供し、その言語の慣用とベストプラクティスに従う」から、「各 SDK はその言語の慣用とベストプラクティスに従う。SDK は新しいプロトコルのリビジョンを独自の予定で採用するので、対応するリビジョンは各 SDK のドキュメントで確かめる」に改められました。

同じタブでは、ほかにも次の変更がありました。

- **Build an MCP server の Java**: System requirements の Spring Boot が「3.3.x 以上」から「4.1.x 以上」になった。Create an MCP Client manually の例で、`new StdioClientTransport(stdioParams)` が `new StdioClientTransport(stdioParams, McpJsonDefaults.getMapper())` になった
- **Build an MCP server の Kotlin**: `build.gradle.kts` の `mcpVersion` が `0.9.0` から `0.16.0` になり、`repositories { mavenCentral() }` のブロックが加わった。ビルドされる jar の名前が `weather-0.1.0-all.jar` から `weather-all.jar` になり、実行コマンド、Claude for Desktop の設定例（macOS/Linux と Windows）、設定の説明の 4 か所が改められた
- **Build an MCP client の Java（Spring AI）**: リポジトリを clone した後の `cd` のパスの先頭に `spring-ai-examples/` が付いた。`spring.ai.mcp.client.toolcallback.enabled` の説明が「既定で無効」から「既定で有効」になった。`ChatClient` の例が `.defaultTools(SyncMcpToolCallbackProvider.builder().mcpClients(mcpSyncClients).build())` と `MessageChatMemoryAdvisor.builder(MessageWindowChatMemory.builder().build()).build()` を使う形になり、会話の記憶は `InMemoryChatMemory` から `MessageWindowChatMemory` になった

- [Build an MCP server - MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-server#system-requirements-3)
- [SDKs - MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/sdk#getting-started)

## 5. llms-full.txt でタブが印付きの引用として出るようになった

**`llms-full.txt` で、タブ・アコーディオン・カードの書き方が変わりました。** これまでタブは `**Python**` のような太字の行で始まり、中身は印のない地の文として続いていました。今回からは `> [tab] Python` の行で始まる引用のブロックになり、中身の行もすべて `> ` 付きで続きます（中のコールアウトは `> > [!NOTE]` のような二重の引用になる）。アコーディオンとカードは以前から `> **題**`・`> **[題](url)**` のような引用の中の太字の行でしたが、それぞれ `> [accordion] 題`・`> [card] [題](url)` になりました。

- **数**: `[tab]` が 41 行（8 ページ）、`[accordion]` が 8 行（3 ページ。うち 1 行は Build an MCP client の Kotlin のタブの中にあり `> > [accordion]` になっている）、`[card]` が 83 行（21 ページ）で、合わせて 24 ページです。字下げの後ろが `>` で始まる行は 1,641 行から 8,303 行に、二重の引用のコールアウトは 2 行から 26 行になりました
- **差分への影響**: 生の差分の追加 10,113 行・削除 9,771 行のほとんどはこの書き換えで、差分のあった 32 ページのうち 17 ページはこの書き換えだけです（一覧は「軽微な更新」の「その他」）。内容の変わった 15 ページのうち 7 ページにも、この書き換えがあります
- **見出しの数への影響**: タブの中の見出しが引用の中に入ったので、行頭が `#` の見出し（h2〜h6、コードフェンスの外）だけを数えると 2,628 から 2,415 に減って見えます。引用の中も数えると 2,631 から 2,632 で、増えた 1 つは Build an MCP client の Rust のタブで 2 つの節が加わり 1 つがなくなった差です（ハイライト 1）

**行数の数え方**: 本サマリのページごとの行数は、両側で `[tab]`・`[accordion]`・`[card]` の印の行を元の太字の行に戻し、行頭（字下げの後ろ）の `> ` を外し、空行を除いてから、ページごとに difflib（autojunk 無効）で比べたものです。2 回収録されている `examples` は写しごとに比べました（今回はどちらも変わっていない）。

## 新規追加されたページ

<!-- light:new-pages:start -->
*(新規追加されたページはありません)*
<!-- light:new-pages:end -->

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
- [**Build an MCP client**](#1-build-an-mcp-client) ([MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-client#imports-and-client-structure)):  
  Rust のタブを、Messages API の直接の呼び出し・プロトコルの版の交渉・`outputSchema` による検証・ツール呼び出しのループを備えた形に書き直し、Java のタブにプロトコルの版の注記を加えて Spring AI の例を改めた（追加 445 行・削除 195 行。詳細はハイライト 1・4 参照）。
- [**Configuration and flags**](#2-configuration-and-flags) ([MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/configuration#catalog-file-format)):  
  Inspector に固有のカタログの項目と既定値の表（27 行）を Catalog file format に加え、負荷試験のフラグ、TUI・mcpdo が読む環境変数、`Host` の許可リストと TLS の環境変数などを表に足した（追加 47 行・削除 8 行）。
<!-- light:updated-pages:end -->

## 1. Build an MCP client

変更（追加 445 行・削除 195 行）は Rust のタブ（追加 438 行・削除 190 行）と Java のタブ（追加 7 行・削除 5 行）にあり、Python・TypeScript・Kotlin・C#・Ruby のタブは書式の書き換えだけです。Java のタブの変更はハイライト 4 を参照してください。Rust のタブの変更は、節ごとに次のとおりです（内容はハイライト 1）。

| 節 | 変更 |
|---|---|
| System Requirements | 対象を「Linux のシステム」から「システム」に。Rust と Cargo を 1.88 以降に |
| Setting Up Your Environment | `Cargo.toml` の依存を差し替え、`Cargo.toml` の後の説明を Messages API を直接呼ぶ理由と `jsonschema` の役割に |
| Setting Up Your API Key | `.env` があれば読み、シェルで `ANTHROPIC_API_KEY` を export してもよい、と追加 |
| Imports and Client Structure | 定数と、Messages API 向けの型（`Message`・`ToolDefinition`・`MessagesRequest`・`MessagesResponse`）と `block_type` 関数を追加。`MCPClient` に `http`・`output_schemas` を持たせた |
| Client Initialization | `impl MCPClient` のブロックをここで開き、タイムアウト付きの `reqwest::Client` を作る |
| Validating Structured Tool Output | 新設 |
| Server Connection Management | `ClientConfig` と `ClientLifecycleMode::Auto` で接続し、取り決めた版を表示して、`outputSchema` の検証器をコンパイルする |
| Query Processing Logic | 「Sending Model Requests」の後から前に移り、最大 `MAX_TOOL_TURNS` 回のループと `is_error` の `tool_result` を備えた |
| Sending Model Requests | `/v1/messages` への直接の POST に |
| Interactive Chat Interface | エラーを `{:#}` で、`anyhow` の文脈ごと 1 行に出す |
| Cleanup | ここで `impl MCPClient` のブロックを閉じる |
| Main Entry Point | `.env` を任意にし、API キーが無ければツールを一覧して終了する |
| Describing Tools to the Model | 新設。旧 Converting MCP Tools の `convert_tools` が移り、`ToolDefinition` を返す |
| Verify the Complete File | 確認項目に `validate_tool_output`、`impl Message` の `user`・`assistant`、`block_type` を追加 |
| Running the Client | 取り決めた版を表示することと、その出力例を追加 |
| How It Works | 6 つの手順を、検証・`is_error`・`MAX_TOOL_TURNS` までのループを含む形に |
| Best Practices | 「Conversation History」の項目を加えて 4 項目に。Security の項目に構造化された結果の検証を追加 |
| Troubleshooting | `.env` が任意になったことと、新しいエラーメッセージ（`[... failed: ...]`、出力スキーマの不一致、`Anthropic request failed with ...`、`[Stopped after 10 tool-use turns]`）を説明 |

- [Build an MCP client - MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-client#imports-and-client-structure)

## 2. Configuration and flags

Inspector の起動・フラグ・環境変数をまとめたページで、次の変更がありました（追加 47 行・削除 8 行）。

- **The launcher owns exactly two things**: `-V` / `--version` の行が加わった。ランチャーのヘルプには載っているがランチャー自身は処理せず、選んだクライアントに渡され、クライアントが Inspector の版を出す（`mcp-inspector -V` は Web クライアント、`mcp-inspector --cli -V` は CLI を通して出す）
- **CLI-only flags**: 「Load test」の行（ハイライト 2）
- **Read by the launcher**: TUI も、自身のトップレベルの失敗について `MCP_DEBUG` と `DEBUG` を同じ規則で読む、と追加
- **CLI and TUI**: 「Read by」の列で、`MCP_CATALOG_PATH`・`MCP_CLIENT_CONFIG_PATH`・`MCP_OAUTH_CALLBACK_URL`・`MCP_STORAGE_DIR`・`MCP_INSPECTOR_OAUTH_STATE_PATH`・`MCP_AUTO_OPEN_ENABLED` の 6 つに mcpdo が加わった。新しい変数として、`MCP_INSPECTOR_LOG_DIR`（TUI の `auth.log` の置き場所。既定は `~/.mcp-inspector`）、`LOG_LEVEL`（そのログのレベル。pino のレベル名で、既定は `info`）、`NO_COLOR`（CLI と mcpdo。空でない値を入れると、人が読む出力の ANSI の装飾を止める。対象は mcpdo の `--format text` の出力すべて（`--plain` と同じ）と、CLI が標準エラーに出すサインインの案内）が加わった
- **Web backend environment variables**: `MCP_INSPECTOR_ALLOWED_HOSTS`・`INSPECTOR_TLS_KEY_PATH`・`INSPECTOR_TLS_CERT_PATH`（ハイライト 3）
- **Catalog file format**: `"type": "http"` を `"streamable-http"` の別名として受け付け、書き戻すときは長い形にする、と追加。さらに、Inspector に固有の項目と既定値の表（27 行。最上位の 16 項目と `oauth.` の 11 項目）が加わった

カタログの項目の表の主なものは次のとおりです（既定値が空欄の項目は省略）。

| 項目 | 既定値 | 意味 |
|---|---|---|
| `protocolEra` | `legacy` | `legacy`・`auto`・`modern` のいずれか |
| `elicitCapability` | `both` | サーバーに示す elicitation の能力（`off`・`url`・`form`・`both`）。mcpdo だけが読む |
| `modernLogLevel` | `debug` | modern の接続でリクエストごとに付けるログのレベル、または `off`。legacy の接続では無視 |
| `connectionTimeout` | `30000` | 接続時のタイムアウト（ミリ秒）。`0` で無効 |
| `taskTtl` | `60000` | **Run as task** で作ったタスクの TTL（ミリ秒） |
| `autoRefreshOnListChanged` | `false` | `list_changed` で、表示の印を付けるだけでなく、ツール・リソース・プロンプトの一覧を読み直す |
| `paginatedLists` | `false` | 読み込み時に全ページをまとめる代わりに、一覧を 1 ページずつ取る |
| `suppressNotificationStream` | `false` | legacy の Streamable HTTP のみ。単独の `GET` の通知ストリームを開かない |
| `maxFetchRequests` | `1000` | このサーバーについて Network のログに残す HTTP リクエストの数。`0` で無制限 |
| `skillCatalogMaxSkills` | `256` | 1 回のスキルの検証で読むスキルの最大数 |
| `skillCatalogMaxBytes` | `67108864` | 1 回のスキルの検証で読む合計の最大バイト数（64 MiB） |
| `oauth.onInsufficientScope` | `reauthorize` | `403 insufficient_scope` のときの方針（`reauthorize` か `throw`） |
| `oauth.requestRefreshToken` | `true` | 登録時に `refresh_token` のグラントを宣言するか。`false` のときだけ書き出す |
| `oauth.scopeOnRefresh` | `false` | リフレッシュトークンのリクエストに `scope` を付けるか。`true` のときだけ書き出す |
| `oauth.revokeOnClear` | `true` | このサーバーの OAuth の状態を消すときに、認可サーバーでグラントも取り消すか（RFC 7009）。`false` のときだけ書き出す |

既定値の無い項目は、`headers`・`metadata`・`requestTimeout`・`advertisedExtensions`・`roots`・`oauth.clientId`・`oauth.clientSecret`・`oauth.scopes`・`oauth.enterpriseManaged`（`true` で標準の OAuth の代わりに企業の IdP（EMA）を通して接続）・`oauth.authorizationParams`・`oauth.authorizationUrl`・`oauth.tokenUrl` です。

- [Configuration and flags - MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/configuration#catalog-file-format)

## 軽微な更新

<!-- light:minor-updates:start -->
今回差分が出たファイルは `llms-full.txt` の 1 件で、大幅更新の 2 ページのほかに、13 ページで内容が変わり、17 ページは書式の書き換えだけでした。

**新機能**

- CLI client に、負荷試験の `--load` の一連のフラグと、しきい値を超えると終了コード `10` で終わる `--load-max-error-rate`・`--load-max-p99` を追加（詳細はハイライト 2 参照） — [CLI client](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/cli#ci-gates)
- CLI client の Exit codes and error envelopes に、サーバーが HTTP 429 を返したときの終了コード `11` を追加し、エンベロープの `code` の値に `rate_limited` を追加（詳細はハイライト 2 参照） — [CLI client](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/cli#exit-codes-and-error-envelopes)
- mcpdo の `tools/call` が、CLI と同じ `--load` の一連のフラグを受け付けるようになった（詳細はハイライト 2 参照） — [mcpdo connection client](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/mcpdo#addressing-a-connection)
- mcpdo に、サーバーへ何も送らずに、指定した接続を直近に使った接続として設定する `mcpdo connections/use <name>` を追加 — [mcpdo connection client](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/mcpdo#addressing-a-connection)
- mcpdo に、カタログのエントリをその接続に限り enterprise-managed として扱う `mcpdo connect <name> --ema` を追加（エントリの `oauth.enterpriseManaged` より優先される。エントリの OAuth のクライアント ID とシークレットが要るので、アドホックの接続先には使えない） — [mcpdo connection client](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/mcpdo#authorization)
- Web client の Host binding and origins に、`Host` ヘッダーの許可リストの段落を追加（詳細はハイライト 3 参照） — [Web client](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/web#host-binding-and-origins)
- Inspector の Security の The web backend and its API token に、同じ `Host` ヘッダーの許可リストが DNS リバインディングを使うページからトークンを守る、という説明を追加（詳細はハイライト 3 参照） — [Security](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/security#the-web-backend-and-its-api-token)

**機能改善**

- Build an MCP server の Java のタブに、対応するプロトコルの版の注記を追加し、Spring Boot を 4.1.x 以上に、`StdioClientTransport` の例を `McpJsonDefaults.getMapper()` を渡す形に変更（詳細はハイライト 4 参照） — [Build an MCP server](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-server#system-requirements-3)
- Build an MCP server の Kotlin のタブに、対応するプロトコルの版の注記を追加し、`mcpVersion` を `0.16.0` に、jar の名前を `weather-all.jar` に変更（詳細はハイライト 4 参照） — [Build an MCP server](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-server#set-up-your-environment-4)
- SDKs の Getting Started で、SDK は新しいプロトコルのリビジョンを独自の予定で採用するので、対応するリビジョンは各 SDK のドキュメントで確かめるよう明記（詳細はハイライト 4 参照） — [SDKs](https://modelcontextprotocol.io/docs/2026-07-28/sdk#getting-started)
- Recipes の Hosting on a network の「Behind TLS or a reverse proxy」の行に、`MCP_INSPECTOR_ALLOWED_HOSTS` と 2 つの TLS の変数の案内を追加（詳細はハイライト 3 参照） — [Recipes](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/recipes#hosting-on-a-network)
- Web client の Apps で、サンドボックスの URL が `http` のままなのは、プロキシ経由で `https` にした場合も 2 つの TLS の変数で `https` にした場合も同じだと追記（詳細はハイライト 3 参照） — [Web client](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/web#apps)
- Debugging の Viewing logs で、ログの場所に Linux の `~/.config/Claude/logs` を加え、ログを追うコマンド例に Linux 版（`tail -n 20 -F ~/.config/Claude/logs/mcp*.log`）を追加 — [Debugging](https://modelcontextprotocol.io/docs/2026-07-28/tools/debugging#viewing-logs)
- mcpdo の Tasks で、`--task` が意味を持つのは legacy の接続だけで、modern の接続ではタスクを返すかどうかをサーバーがリクエストごとに決めるので、このフラグは通信の内容を変えないと明記 — [mcpdo connection client](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/mcpdo#tasks)
- Protocol eras の Tasks（modern）で、modern の接続には **Run as task** の操作がなく、タスクの作成はサーバー主導で、`tools/call` が `CreateTaskResult` を返すかどうかはサーバーがリクエストごとに決めると改めた — [Protocol eras](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/protocol-eras#tasks)
- Recipes の Keeping a connection open with mcpdo の例で、`--task` のコメントを「legacy の接続での」タスク付きの呼び出しと明記 — [Recipes](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/recipes#keeping-a-connection-open-with-mcpdo)
- mcpdo の Using mcpdo from a coding agent に、`npx skills add modelcontextprotocol/inspector --skill mcpdo` でもスキルを入れられると追加 — [mcpdo connection client](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/mcpdo#using-mcpdo-from-a-coding-agent)
- Understanding MCP clients の Sampling の Overview にある例で、モデルのヒントを `claude-sonnet-4-20250514` から `claude-sonnet`（コメントは「Sonnet クラスのモデルを優先」）に変更 — [Understanding MCP clients](https://modelcontextprotocol.io/docs/2026-07-28/learn/client-concepts#overview-3)
- Security Charter（Security Interest Group の憲章）の Mission Statement を、「MCP 固有の脅威を整理し、セキュリティに関わる提案をレビューし、検証した問題を WG や SEP に切り出す」から「MCP 固有のセキュリティの話題の最初の窓口として、持ち込まれた脅威・提案・開示の質問を見極め、担当の WG や SEP に回す」に改め、In Scope の先頭に「Triage and routing」（Discord や GitHub で挙がった話題を Auth IG・Transports WG・Registry WG・Tool Annotations IG・SDK メンテナーに渡す）を追加 — [Security Charter](https://modelcontextprotocol.io/community/interest-groups/security#mission-statement)
- 同じ憲章の Operations で、会合を隔週 45 分の「Office Hours」から月次 45 分の「Forum call」と月次の「Digest」（回した項目・未決の話題・勧告のまとめ）に変え、各回の議題はファシリテーターが `#security-ig` で募り誰でも足せる、とした。Membership の記述も、会合の間はチャンネルで非同期に議論し、月次の会合の議題もそこでまとめる、という形に。Changelog に 2026年08月26日 の行（ルーティング型のグループへの再編。discussion #3316）を追加 — [Security Charter](https://modelcontextprotocol.io/community/interest-groups/security#operations)
- Security Policy の Security Interest Group の節を、「MCP 固有のセキュリティの話題を持ち込む場で、ファシリテーターが担当のグループに回す」という新しい位置付けに合わせて書き換え — [Security Policy](https://modelcontextprotocol.io/community/security#security-interest-group)

**その他**

- Protocol eras の Tasks と Multi-round tool results (MRTR) で、elicitation・sampling・roots へのリンク先を `/specification/draft/client/…` から `/specification/2026-07-28/client/…` に変更 — [Protocol eras](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/protocol-eras#multi-round-tool-results-mrtr)
- CLI client の Choosing a server で、roots へのリンク先を `/specification/draft/client/roots` から `/specification/2026-07-28/client/roots` に変更 — [CLI client](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/cli#choosing-a-server)
- CLI client の CI gates の冒頭の「Three flags」を「These flags」に変更 — [CLI client](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/cli#ci-gates)
- OAuth Client Credentials の SDK examples で、「各サンプルは資格情報を発行した認可サーバーの発行元を固定している」の文が、「Choose the credential format that matches your setup:」の後ろから前に移った（文面は同じ） — [OAuth Client Credentials](https://modelcontextprotocol.io/extensions/auth/oauth-client-credentials#sdk-examples)
- **書式の書き換えだけのページ**（詳細はハイライト 5 参照）: 次の 17 ページは、タブ・アコーディオン・カードの書き換えだけで、内容は変わっていません。`community/contributing`・`docs/2026-07-28/develop/build-with-agent-skills`・`docs/2026-07-28/develop/connect-local-servers`・`docs/2026-07-28/develop/connect-remote-servers`・`docs/2026-07-28/getting-started/intro`・`docs/2026-07-28/tools/inspector`・`docs/2026-07-28/tutorials/security/authorization`・`docs/2026-07-28/tutorials/security/local-server-security`・`extensions/apps/build`・`extensions/auth/enterprise-managed-authorization`・`extensions/auth/overview`・`extensions/overview`・`extensions/skills/overview`・`extensions/tasks/overview`・`seps/index`・`specification/2026-07-28/index`・`specification/2026-07-28/server/index`。内容の変わった 15 ページのうち 7 ページ（`develop/build-client`・`develop/build-server`・`sdk`・`tools/debugging`・`tools/inspector/protocol-eras`・`tools/inspector/recipes`・`extensions/auth/oauth-client-credentials`）にも、この書き換えがあります
<!-- light:minor-updates:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-10-30.md](./archives/latest/2026-10-30.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-10-30.md](./archives/latest-detail/2026-10-30.md)

<!--
base_commit: a900109552b6641cda7666a841e6800cad45d7ae
head_commit: 40e270212cf60c02b47a1f36e25f55319f572f41
generated_at_full: 2026-11-01T15:08:35+09:00
-->
