---
対象期間: 2026年11月13日 〜 2026年11月15日
作成日: 2026-11-15
---

# MCP 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
今回の対象期間の取り込みは 2 回で、MCP の入力ファイルが変わったのは 2 回目だけでした（`llms-full.txt` の追加 597 行・削除 329 行、14 ページ）。中心は Understanding MCP servers と Understanding MCP clients の書き直しで、例が `_meta` と `resultType` を含む完全な JSON-RPC メッセージになり、非推奨の Roots と Sampling の解説が外れました。

主要なものを以下に挙げます。

1. Understanding MCP clients から非推奨の Roots と Sampling の節が削られ、新設の h2「Deprecated Features」の警告に代わりの方法がまとまった。Architecture overview の非推奨の一覧も Roots・Sampling・プロトコルのログの 3 つに改められ、Debugging の TypeScript のログの例はプロトコル経由から stderr への出力に替わった
2. Understanding MCP servers の例が完全な JSON-RPC メッセージになり、`structuredContent`・キャッシュのヒント・`completion/complete`・`prompts/get` のやり取りが加わった。プロンプトの引数には型が無く、値はすべて文字列で送ると明記された
3. Understanding MCP clients の Elicitation の例が、`tools/call`・`InputRequiredResult`・`inputResponses` を付けた再送・最終の結果の 4 つのメッセージになった。クライアントが対応するモードを `elicitation` の capability で宣言する方法も書かれた
4. Understanding Authorization in MCP で、DCR が登録方式の表と h3 の節から外れ、CIMD に対応しない認可サーバーに対して既存のクライアントが使える代替手段として、警告の中で扱われるようになった
5. OAuth Client Credentials の JWT の流れが `client_credentials` グラントと `client_assertion` の形になり、`aud` には認可サーバーの issuer 識別子だけを入れるよう改められた。Enterprise-Managed Authorization では、ID-JAG を求めるトークン交換のパラメーターが明記された
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**非推奨の機能の解説が削られ代わりの方法の案内にまとまった**](#1-非推奨の機能の解説が削られ代わりの方法の案内にまとまった):  
  Understanding MCP clients から Roots と Sampling の h3 の節（それぞれの例や User Interaction Model を含む）が削除され、ページ末尾に新設された h2「Deprecated Features」の警告が、Roots はツールのパラメーター・リソース URI・サーバーの設定で渡し、Sampling は LLM プロバイダーの API と直接統合する、と代わりの方法を示すようになった。Architecture overview の非推奨の一覧は Roots・Sampling・プロトコルのログの 3 つになり、Debugging の TypeScript のログの例は `notifications/message` を送る例から `console.error` で stderr に書く例に替わった。
2. [**Understanding MCP servers の例が完全な JSON-RPC メッセージになった**](#2-understanding-mcp-servers-の例が完全な-json-rpc-メッセージになった):  
  Understanding MCP servers（追加 344 行・削除 65 行）で、Tools・Resources・Prompts と The Complete Flow の例が、`_meta` にプロトコルのバージョンとクライアントの capability を持つリクエストと、`resultType` を持つ結果の組になった。`outputSchema` と `structuredContent`、`resources/read` の結果のキャッシュのヒント（`ttlMs`・`cacheScope`）、`completion/complete` による値の提案の例が加わり、プロンプトの引数には型が無く値はすべて文字列で送る、と明記された。
3. [**Elicitation の例が MRTR の往復を 4 つのメッセージで示すようになった**](#3-elicitation-の例が-mrtr-の往復を-4-つのメッセージで示すようになった):  
  Understanding MCP clients の Elicitation で、`elicitation/create` のリクエストを 1 つだけ載せていた例が、`bookVacation` ツールの `tools/call`、`resultType` が `"input_required"` の `InputRequiredResult`、`inputResponses` と `requestState` を付けた再送、`resultType` が `"complete"` の結果、の 4 つのメッセージになった。クライアントが対応するモードを `elicitation` の capability で宣言する方法と、ユーザーの応答が `accept`・`decline`・`cancel` の action に対応することも書かれた。
4. [**認可のチュートリアルで DCR が登録方式の表から外れた**](#4-認可のチュートリアルで-dcr-が登録方式の表から外れた):  
  Understanding Authorization in MCP で、Dynamic Client Registration（DCR）が登録方式の表と h3 の節から外れ、事前登録と Client ID Metadata Documents（CIMD）の 2 つになった。DCR は警告の中で、CIMD に対応せず実行時の登録を受け付ける認可サーバーに対し、既存のクライアントがユーザーにクライアント ID を尋ねる前に使える手段として扱われる。Security Best Practices と Extension Support Matrix の注記も同じ方向に改められた。
5. [**認可の拡張 2 件でトークン要求のパラメーターが明記された**](#5-認可の拡張-2-件でトークン要求のパラメーターが明記された):  
  OAuth Client Credentials の JWT Bearer Assertions の流れで、トークンの要求が `grant_type=client_credentials` と `client_assertion_type`・`client_assertion`・`resource` の形になり、JWT の `aud` は認可サーバーのトークンエンドポイントの URL から issuer 識別子だけに改められた。Enterprise-Managed Authorization では、ID-JAG を IdP のトークンエンドポイントへの Token Exchange（RFC 8693）で求めることと、そのパラメーターが明記された。
<!-- light:highlight-list:end -->

## 1. 非推奨の機能の解説が削られ代わりの方法の案内にまとまった

今回の対象期間の取り込みは 2 回で、MCP の入力ファイルが変わったのは 2 回目だけです。変わったのは本文 `llms-full.txt` だけで（追加 597 行・削除 329 行）、索引 `llms.txt` には差分がありません。`llms-full.txt` の総行数は 45,256 行から 45,524 行になり、収録ページ数（160 件。`examples` が 2 回収録されているため、URL としては 159 件）と索引のエントリ数（365 件）は変わっていません。

差分のハンクをページに振り分けると、変更のあったページは次の 14 件です。50 行以上の変更は Understanding MCP servers と Understanding MCP clients の 2 件で、Understanding Authorization in MCP（45 行）以下は軽微な更新に当たります。

| ページ | 行数 | 追加 | 削除 | 主な変更 |
|---|---|---|---|---|
| Understanding MCP servers | 286 → 565 | 344 | 65 | 例を完全な JSON-RPC メッセージに（ハイライト 2） |
| Understanding MCP clients | 269 → 230 | 145 | 184 | Roots と Sampling の節を削除（ハイライト 1）、Elicitation の例を書き直し（ハイライト 3） |
| Understanding Authorization in MCP | 804 → 787 | 14 | 31 | DCR の扱い（ハイライト 4）、Inspector での確認手順 |
| Architecture overview | 557 → 570 | 28 | 15 | 非推奨の一覧（ハイライト 1）、JSON-RPC とプリミティブの説明 |
| Debugging | 368 → 369 | 21 | 20 | ログの例（ハイライト 1） |
| Authorization（仕様） | 423 → 443 | 21 | 1 | アクセストークンを付けたリクエストの例 |
| Enterprise-Managed Authorization | 200 → 207 | 8 | 1 | ID-JAG を求めるトークン交換（ハイライト 5） |
| OAuth Client Credentials | 414 → 414 | 3 | 3 | トークンの要求と `aud`（ハイライト 5） |
| Specification | 137 → 139 | 4 | 2 | 拡張のネゴシエーション |
| Security Best Practices | 986 → 990 | 4 | 0 | DCR の注記（ハイライト 4） |
| Schema Reference | 1,574 → 1,574 | 2 | 2 | `InvalidParamsError` と `CallToolResult` |
| Extensions Overview | 284 → 282 | 1 | 3 | 初期化の例の capability |
| MCP Inspector | 165 → 165 | 1 | 1 | 必要な Node.js のバージョン |
| Extension Support Matrix | 58 → 58 | 1 | 1 | 注記から「(DCR, CIMD)」を削除 |

行数は、ページのタイトルの行（`# `）から次のページの直前までを数えたものです。

Roots・Sampling・プロトコル経由のログ（`notifications/message`）は、base の時点でもプロトコルのバージョン `2026-07-28` で非推奨と書かれていました。今回は、これらを解説していた本文が削られ、代わりの方法を示す案内にまとめられています。

**Understanding MCP clients。** Core Client Features の冒頭にあった Elicitation・Roots・Sampling の 3 行の表が削除され、「クライアントはサーバーに elicitation などの機能を提供できる」という 1 文になりました（表にあった Elicitation の例の文は、Elicitation の節の冒頭に移っています）。続いて、Roots の h3 の節（Overview・Example: Travel Planning Workspace・Design Philosophy・User Interaction Model の h4 を含む）と、Sampling の h3 の節（Overview・Example: Flight Analysis Tool・User Interaction Model の h4 を含む）が丸ごと削除されました。どちらの節も、冒頭に非推奨の警告を置いたうえで、ルートの構造やサンプリングの要求パラメーターの例、利用の流れを説明していました。代わりにページ末尾に h2「Deprecated Features」が新設され、Roots と Sampling はプロトコルのバージョン `2026-07-28` で非推奨となり削除が予定されているとして、警告の中で代わりの方法を示しています。見出しは 14 個から 6 個になりました（削除 9・追加 1）。

- **Roots**: ディレクトリやファイルは、ツールのパラメーター・リソース URI・サーバーの設定で渡す
- **Sampling**: LLM プロバイダーの API と直接統合する。クライアントを通じて補完を求める仕組みの代わりは、プロトコルでは定めない

**Architecture overview。** Primitives の節で、非推奨の一覧が書き換えられました。これまでは「次のクライアントのプリミティブは非推奨」として Sampling と Logging の 2 つを、それぞれの説明とともに挙げていました。新しい記述は、クライアントの機能である Roots と Sampling、サーバーの機能であるプロトコルのログが `2026-07-28` で非推奨だとし、新しい実装が使う代わりの方法を挙げます。Roots と Sampling は Understanding MCP clients と同じ文面で、ログは「stdio のサーバーなら stderr に書く（Debugging の Implementing logging へのリンク）か、OpenTelemetry を使う」です。あわせて、Data layer の Client features の項から「Sampling は非推奨」の 1 文が外れました。

**Debugging。** Server-side logging の節で、「以下の `notifications/message` の仕組みは非推奨」という警告と、MCP が RFC 5424 の 8 つの重大度（`debug` から `emergency` まで）を定め、クライアントはリクエストの `_meta` の `io.modelcontextprotocol/logLevel` でリクエストごとにログを求める、という段落が削除されました。TypeScript の例は、`server.sendLoggingMessage` でログのメッセージを送る例から、`McpServer` にツールを登録し、その処理の中で `console.error` を使って stderr に書く例に替わり、例の前の文には「たとえば stderr に書くには」が加わりました。Python の例（`logging` モジュールを使う）は変わっていません。Debugging tools overview の Server logging の項では、プロトコル経由のログが非推奨だという注記のリンク先が、ログの仕様のページから非推奨の機能の一覧のページ（`/specification/2026-07-28/deprecated`）に変わりました。

- [Understanding MCP clients - MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/learn/client-concepts#deprecated-features)
- [Architecture overview - MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture#primitives)
- [Debugging - MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/tools/debugging#server-side-logging)

## 2. Understanding MCP servers の例が完全な JSON-RPC メッセージになった

Understanding MCP servers は追加 344 行・削除 65 行で、行数は 286 行から 565 行になりました。見出し（17 個）は変わっておらず、変更は各節の本文と例にあります。Core Server Features の冒頭（3 つの構成要素の表の後）には、`jsonrpc` のフィールドを持つ例は完全なメッセージで、それ以外は抜粋であることと、すべてのリクエストは `_meta` にプロトコルのバージョンとクライアントの capability を持ち、すべての結果は `resultType` を持つこと、の 2 文が加わりました。

- **Tools**: ツール定義の例が「`tools/list` が返すもの」として JSON で書かれ（これまでは TypeScript のオブジェクトの書き方）、`title` と `outputSchema`（`flightNumber` と `priceUsd` を持つ便の配列）が加わった。Example: Travel Booking では、`searchFlights` を呼ぶ `tools/call` のリクエストとその結果が載った。結果の `structuredContent` は `outputSchema` に従い、後方互換のため、同じ JSON を文字列にしたテキストも `content` に入れる。ほかの 2 つのツール（`createCalendarEvent`・`sendEmail`）は、関数呼び出し風の擬似コードから、`name` と `arguments` を持つ JSON の抜粋になった
- **Resources**: 各リソースは MIME タイプを「宣言する」から「宣言できる」に、リソーステンプレートのメタデータも「含む」から「含められる」になった。操作の表に `completion/complete`（パラメーターの値を提案する）の行が加わり、個々のリソースの更新通知に対応するサーバーは `resources` の capability で `"subscribe": true` を宣言する、という文が加わった。Example: Getting Travel Planning Context では、AI アプリケーションが使うリソースが 3 件から 5 件（旅行の好みと天気予報が加わった）になり、`resources/read` のリクエストと結果の例が加わった。結果には 2 つのキャッシュのヒントがあり、`ttlMs` はクライアントが結果を新しいとみなしてよい時間（ミリ秒）、`cacheScope` の `"private"` は、キャッシュがそれを認可のコンテキストをまたいで共有してはならないことを示す
- **Parameter Completion**: 「`completions` の capability を宣言したサーバーは、テンプレートのパラメーターの値を提案できる」と前提が書かれた。テンプレートに複数のパラメーターがある場合、クライアントは確定済みの値を `context.arguments` に入れるべきだとして、`origin` に `JFK` を選んだ後に `destination` に「Bar」と打った場合の `completion/complete` のリクエストと、`BCN` と `BGI` を提案する結果の例が加わった
- **Prompts**: 操作の表で、`prompts/list` の戻り値が「各プロンプトが受け付ける引数を含む定義の配列」に、`prompts/get` が「プロンプトの取得」で戻り値が「プロンプトのメッセージの配列」に改められ、`completion/complete`（引数の値を提案する）の行が加わった。「Plan a vacation」の例は `prompts/list` が返す形になり、引数から `type` が消え、どれも `description` を持つ 7 つになった（`required` は `origin`・`destination`・`departureDate`・`returnDate` が true、`budget`・`travelers` が false で、`interests` には無い）。その後に「プロンプトの引数には型が無い。値はすべて文字列で送るので、期待する形式は `description` で示す。`required` が `true` でない引数は任意」という段落が加わった
- **The Complete Flow**: 手順 1 に、Travel Server への `prompts/get` のリクエストと、AI アプリケーションが会話に加えるメッセージを返す結果の例が加わった。手順 3 は、AI アプリケーションが 3 つのサーバーすべてのツールをモデルに渡すので、Travel Server のプロンプトによってモデルが Weather Server の `checkWeather` を呼ぶことがある、と説明が改められた。モデルが呼ぶツールにはどのサーバーのものかが添えられ、検索の段階に `searchHotels` が加わった。予約の段階は `bookHotel` に代わって、便とホテルを予約する `bookVacation` になり、サーバーが elicitation でユーザーに予約の確認を求めると書かれた（ハイライト 3 の例はこの場面の続き）

例の日付は 2024 年から 2027 年に改められ、カレンダーのリソースの URI は `calendar://events/2027-06` に、過去の旅行は `travel://past-trips/spain-2023` にそろえられました。

- [Understanding MCP servers - MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/learn/server-concepts#example-travel-booking)
- [Understanding MCP servers - MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/learn/server-concepts#parameter-completion)
- [Understanding MCP servers - MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/learn/server-concepts#example-streamlined-workflows)

## 3. Elicitation の例が MRTR の往復を 4 つのメッセージで示すようになった

Understanding MCP clients の Elicitation の Overview で、これまで「`InputRequiredResult.inputRequests` の中で届く」として `elicitation/create` のリクエストを 1 つ（TypeScript のオブジェクトの書き方）載せていた例が、「Elicitation example」として 4 つの JSON-RPC メッセージになりました。Understanding MCP servers の旅行計画のシナリオ（The Complete Flow）の続きという位置付けです。

1. クライアントが `bookVacation` ツールを呼ぶ `tools/call`（`id` は 1。`_meta` の `io.modelcontextprotocol/clientCapabilities` に `"elicitation": {}`）
2. サーバーはユーザーに予約の確認を求める必要があるので、`InputRequiredResult` を返す。`resultType` の `"input_required"` は、サーバーが要求を完了するにはクライアントが追加の入力を渡す必要があることを示す。`inputRequests` の `bookingConfirmation` キーに form モードの `elicitation/create`（予約の確認・座席・部屋・旅行保険の 4 項目のスキーマ）を入れ、`requestState` を付ける
3. ユーザーがフォームに記入した後、クライアントは新しい `id`（2）で呼び直す。ユーザーの回答を、サーバーの要求と同じ `bookingConfirmation` キーで `inputResponses` に入れ（`action` は `accept`）、結果にあった `requestState` の値をそのまま返す
4. サーバーが予約を済ませ、`CallToolResult` を返す。`resultType` の `"complete"` は、要求が正常に完了したことを示す

ほかに 2 つの変更があります。Overview の、Elicitation が Multi Round-Trip Requests のパターンに従うという段落の後に、「クライアントは各リクエストの `elicitation` capability で対応するモードを宣言し、サーバーはそれ以外のモードを使ってはならない。空のオブジェクト（`{}`）は form モードだけを、`{ "form": {}, "url": {} }` は両方を宣言する」という段落が加わりました。User Interaction Model の Response options は、ユーザーが UI で情報を提供する・明示的に断る・選ばずに閉じる、の 3 つが `accept`・`decline`・`cancel` の action に対応する、と書き換えられました（これまでは「説明を付けて断る、または操作全体を取り消す」）。

Example: Holiday Booking Approval と、User Interaction Model のほかの項目（Request presentation・URL handling・Privacy considerations）の文面は変わっていません。

- [Understanding MCP clients - MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/learn/client-concepts#overview)
- [Understanding MCP clients - MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/learn/client-concepts#user-interaction-model)

## 4. 認可のチュートリアルで DCR が登録方式の表から外れた

Understanding Authorization in MCP（追加 14 行・削除 31 行）で、Dynamic Client Registration（DCR）の扱いが変わりました。DCR は base の時点でもこのページで非推奨とされていましたが、登録方式の表に 3 つ目の方式として並び、h3 の節もありました。

- **Client Registration Approaches**: 表から DCR の行が外れ、事前登録と Client ID Metadata Documents（CIMD）の 2 行になった。「3 つすべてに対応するクライアントはこの順に試す」は「両方に対応するクライアントは」になり、どれも使えないときにユーザーに入力してもらうものが「クライアントの情報」から「認可サーバーに登録済みのクライアントの ID と、あればクライアントシークレット」に具体化された
- **警告の新設**: 表の後に、DCR は `2026-07-28` で非推奨で、新しい実装は CIMD を使う、という警告が加わった。既存のクライアントは、ユーザーにクライアント ID とシークレットを尋ねる前に DCR にフォールバックできる。これは、認可サーバーが CIMD に対応せず、`registration_endpoint` で実行時のクライアント登録を受け付ける場合に当てはまる
- **h3「Dynamic Client Registration」の削除**: `registration_endpoint` に送るメタデータの JSON の例と、適切な `application_type` を含めるという要件を載せていた節が削除された。節の末尾の「事前登録と DCR の資格情報は、発行した認可サーバーに属する」は「資格情報は」になり、Pre-registration の節の後に残った
- **ほかの記述**: 流れの図の注記が「pre-registered ID, metadata document, or DCR」から「pre-registered ID or metadata document」に、Choosing an Authorization Server の「MCP サーバーには CIMD や DCR のコードは要らない」が「登録のコードは要らない」になった。Testing the Server からは、認可サーバーが DCR に対応し手元のマシンからの登録を受け付けるなら `--client-metadata-url` を省ける、という文が削除された
- **Common Pitfalls and How to Avoid Them**: 「Restrict Dynamic Client Registration」が、「認可サーバーが開いた `registration_endpoint` で DCR に対応していると、誰でもクライアントを登録できる。クライアントが DCR に依存していなければ無効にし、そうでなければ信頼するホストやレート制限で登録を制限する」と書き換えられた。Related Standards and Documentation からは RFC 7591（Dynamic Client Registration）が外れた

ほかのページにも同じ方向の変更があります。Security Best Practices の Confused Deputy Problem の冒頭には、「DCR は `2026-07-28` で非推奨だが、この攻撃は DCR に対応する MCP プロキシサーバーには依然として当てはまる」という NOTE が加わりました。Extension Support Matrix の NOTE では、認可の拡張の対応状況はコアの MCP 認可の機能とは別に追跡する、という文で例として挙げていた「(DCR, CIMD)」が外れました。

- [Understanding Authorization in MCP - MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/authorization#client-registration-approaches)
- [Security Best Practices - MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices#confused-deputy-problem)

## 5. 認可の拡張 2 件でトークン要求のパラメーターが明記された

**OAuth Client Credentials。** How it works の JWT Bearer Assertions（推奨）の流れの図で、トークンの要求が `grant_type=urn:ietf:params:oauth:grant-type:jwt-bearer` と `assertion=<signed JWT>` から、`grant_type=client_credentials`・`client_assertion_type=urn:ietf:params:oauth:client-assertion-type:jwt-bearer`・`client_assertion=<signed JWT>`・`resource=<MCP server URI>` になりました。JWT の `aud` クレームの説明は「認可サーバーのトークンエンドポイントの URL」から「認可サーバーの issuer 識別子（メタデータの `issuer` の値）を唯一の値として」に改められ、RFC 7523 が許していたトークンエンドポイントの URL を RFC 10070 は認めない、と添えられました。Client Secrets の流れの図でも、トークンの要求に `resource=<MCP server URI>` が加わりました。

**Enterprise-Managed Authorization。** Implementation guide の For MCP clients の 3 番目「Handle ID-JAGs」で、ID-JAG を求める先が企業の IdP の「authorization endpoint」から「token endpoint」に改められ、その要求が Token Exchange（[RFC 8693](https://datatracker.ietf.org/doc/html/rfc8693)）であることと、次のパラメーターが明記されました。

- `requested_token_type`: `urn:ietf:params:oauth:token-type:id-jag`
- `subject_token` と `subject_token_type`: Identity Assertion とその種類。SAML のクライアントは、代わりに assertion を Refresh Token に交換して、それを送ることができる
- `audience`: MCP の認可サーバーの issuer 識別子
- `resource`: MCP サーバーのリソース識別子。任意で、含めると ID-JAG に対して発行されるアクセストークンはその MCP サーバーに audience が限定される。省いた場合の挙動は認可サーバーしだいで、たとえば既定のリソースを使うことも、`invalid_target` エラーで要求を拒否することもある

ID-JAG をアクセストークンに交換する先も「MCP の認可サーバー」から「MCP の認可サーバーのトークンエンドポイント」になり、`urn:ietf:params:oauth:grant-type:jwt-bearer` グラントを使うと書かれました。MCP の認可サーバーの authorization endpoint にユーザーをリダイレクトしない、という指示は変わっていません。

- [OAuth Client Credentials - MCP Docs](https://modelcontextprotocol.io/extensions/auth/oauth-client-credentials#jwt-bearer-assertions-recommended)
- [Enterprise-Managed Authorization - MCP Docs](https://modelcontextprotocol.io/extensions/auth/enterprise-managed-authorization#for-mcp-clients)

## 新規追加されたページ

<!-- light:new-pages:start -->
今回の対象期間に新たに追加されたページはありません。索引 `llms.txt` に変更はなく、索引のエントリ数（365 件）と本文 `llms-full.txt` の収録ページ数（160 件。URL としては 159 件）はどちらも前回と同じです。
<!-- light:new-pages:end -->

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
- [**Understanding MCP servers**](#1-understanding-mcp-servers) ([MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/learn/server-concepts#core-server-features)):  
  Tools・Resources・Prompts と The Complete Flow の例を、`_meta` と `resultType` を含む完全な JSON-RPC メッセージに書き直し、`completion/complete` による値の提案と、型を持たないプロンプトの引数の説明を加えた（追加 344 行・削除 65 行。詳細はハイライト 2 参照）。
- [**Understanding MCP clients**](#2-understanding-mcp-clients) ([MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/learn/client-concepts#core-client-features)):  
  非推奨の Roots と Sampling の節を削除して h2「Deprecated Features」の警告にまとめ、Elicitation の例を MRTR の往復を示す 4 つのメッセージに書き直した（追加 145 行・削除 184 行。詳細はハイライト 1・3 参照）。
<!-- light:updated-pages:end -->

## 1. Understanding MCP servers

変更は Core Server Features の冒頭、Tools（How Tools Work・Example: Travel Booking）、Resources（How Resources Work・Example: Getting Travel Planning Context・Parameter Completion）、Prompts（How Prompts Work・Example: Streamlined Workflows）、Bringing Servers Together の The Complete Flow にあります。3 つの User Interaction Model の節と、Bringing Servers Together の導入（3 つのサーバーの一覧）は変わっていません。主な内容はハイライト 2 を参照してください。

ハイライト 2 で挙げたもののほかに、次の変更があります。

- Resources の Direct Resources の例が、2024 年のカレンダーの空き状況を返す `calendar://events/2024` から、2027年06月の空き状況を返す `calendar://events/2027-06` になった。Resource Templates の説明は「dynamic URIs with parameters」から「parameterized URIs」になり、`travel://activities/barcelona/museums` の例は入れ子の項目から本文の文に移った（表記は `travel://activities/Barcelona/museums`）
- リソーステンプレートの例が、天気のサーバーのもの（`weather://forecast/{city}/{date}`）と旅行のサーバーのもの（`travel://flights/{origin}/{destination}`）の 2 つのコードブロックに分かれ、後者の説明が「都市の間の便を検索する」から「2 つの空港の間の便を検索する」になった。テンプレートの後の段落からは、`origin` に「NYC」を入れ `destination` に「Bar」と打ったときに「Barcelona (BCN)」や「Barbados (BGI)」を提案する、という文が外れ、同じ場面は Parameter Completion の `completion/complete` の例として書き直された
- Prompts の Example: Streamlined Workflows で、構造化された入力の例が「目的地・日数・予算・配列で表した興味」（Barcelona、7 日、$3000、beaches・architecture・food）から、出発地と目的地（New York から Barcelona）・日程・予算 $3000・2 人・興味（ビーチ・建築・食事）を文で並べた形になった
- The Complete Flow の結論の段落で、ツールの例が「便の検索・ホテルの予約・カレンダーの更新」から「便とホテルの検索・それらの予約・カレンダーの更新」に改められた

- [Understanding MCP servers - MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/learn/server-concepts#the-complete-flow)

## 2. Understanding MCP clients

見出しの構成は次のように変わりました（14 個から 6 個）。

| 区分 | base | head |
|---|---|---|
| h2 | Core Client Features | Core Client Features、Deprecated Features（新設） |
| Elicitation（h3） | Overview・Example: Holiday Booking Approval・User Interaction Model | 同じ |
| Roots（h3） | Overview・Example: Travel Planning Workspace・Design Philosophy・User Interaction Model | 削除 |
| Sampling（h3） | Overview・Example: Flight Analysis Tool・User Interaction Model | 削除 |

削除された Roots の節は、ルートが `file://` の URI で表すファイルシステムの境界で、セキュリティの境界ではなく調整の仕組みであることを、旅行計画のワークスペースの例とともに説明していました。Sampling の節は、サーバーがクライアントを通じて言語モデルの補完を求める流れを、人による確認の段階を含むシーケンス図、`modelPreferences` を含む要求パラメーターの例、便を分析するツールの例とともに説明していました。Roots と Sampling の代わりの方法はハイライト 1、Elicitation の変更はハイライト 3 を参照してください。

- [Understanding MCP clients - MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/learn/client-concepts#elicitation)

## 軽微な更新

<!-- light:minor-updates:start -->
今回差分が出たファイルは `llms-full.txt` の 1 件で、大幅更新の 2 ページのほかに、次の 12 ページに変更がありました。

**機能改善**

- Architecture overview の Primitives で、非推奨の一覧を Roots・Sampling・プロトコルのログの 3 つとそれぞれの代わりの方法に改め、Data layer の Client features の項から Sampling は非推奨という 1 文を外した（詳細はハイライト 1 参照） — [Architecture overview](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture#primitives)
- 同ページの Data Layer Protocol で、JSON-RPC の説明を「クライアントとサーバーは互いにリクエストを送り、それに応答する」から「クライアントがリクエストを送り、サーバーが応答する。サーバーは Multi Round-Trip Requests のパターンでクライアントに入力を求められる」に改めた — [Architecture overview](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture#data-layer-protocol)
- 同ページの Primitives で、各プリミティブのメソッドを「発見（`*/list`）、取得（`*/get`）、場合によっては実行（`tools/call`）」から「発見（`*/list`）と、取得（`resources/read`・`prompts/get`）または実行（`tools/call`）」に改め、例を「ツールを一覧し（`tools/list`）、モデルに渡し、モデルが呼んだものを実行する（`tools/call`）」とした — [Architecture overview](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture#primitives)
- 同ページの Example で、`tools/list` と `tools/call` の応答の例に、`_meta` の `io.modelcontextprotocol/serverInfo` を加えた — [Architecture overview](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture#example)
- 同ページの Understanding the Tool Execution Response で、内容の種類として text のほかに画像（`image`）・音声（`audio`）・リソースリンク（`resource_link`）・埋め込みリソース（`resource`）を挙げ、すべての種類を受け付けるモデルばかりではないので、クライアントはモデルが対応しない内容を扱う必要がありうる、と加えた。「Structured Output」の項は「Structured Content（任意）」になり、ツールは結果の `structuredContent` に JSON の値を返せること、この例のツールはテキストだけを返すことを述べるようになった — [Architecture overview](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture#understanding-the-tool-execution-response)
- 同ページの Why Notifications Matter で、Efficiency を「クライアントは変更をポーリングする必要がない」から「更新時に通知されるので、ポーリングの頻度を下げられる」に、Consistency を「常に正確な情報を持てるようにする」から「利用できる機能についての見方を最新に保つのを助ける」に改めた — [Architecture overview](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture#why-notifications-matter)
- Debugging の Server-side logging で、プロトコル経由のログの警告と、重大度と `io.modelcontextprotocol/logLevel` の段落を削除し、TypeScript の例を `console.error` で stderr に書く例に替えた（詳細はハイライト 1 参照） — [Debugging](https://modelcontextprotocol.io/docs/2026-07-28/tools/debugging#server-side-logging)
- Understanding Authorization in MCP で、DCR を登録方式の表と h3 の節から外し、警告の中で扱うようにした（詳細はハイライト 4 参照） — [Understanding Authorization in MCP](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/authorization#client-registration-approaches)
- 同ページの Testing the Server で、MCP Inspector に必要な Node.js を「22.19 以上」から「22.23.4 以上・24.22.1 以上・26.12.1 以上」に、Inspector のコマンドの説明を「ログインのためにブラウザーを開いてツールを呼ぶ」から「ログインの流れを実行してツールを呼ぶ」に改めた。Inspector のリダイレクト URI は既定値で、`--callback-url` で変えられる（ループバックのアドレスでなければならない）こと、`--client-metadata-url` の文書は認可サーバーが取得できなければならないことを加えた。トラブルシューティングでは、Inspector が実行をまたいで保持するものを「トークンと登録したクライアント」から「トークンとクライアントの情報」に改めた — [Understanding Authorization in MCP](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/authorization#testing-the-server)
- MCP Inspector の Quickstart で、必要な Node.js を「22.19.0 以上」から「22.23.4 以上・24.22.1 以上・26.12.1 以上」に改めた — [MCP Inspector](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector#quickstart)
- Security Best Practices の Confused Deputy Problem に、DCR は非推奨だがこの攻撃は DCR に対応する MCP プロキシサーバーに当てはまる、という NOTE を加えた（詳細はハイライト 4 参照） — [Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices#confused-deputy-problem)
- Authorization（仕様）の Token Requirements で、アクセストークンを付けたリクエストの例を `GET /mcp` から `POST /mcp` に改め、`Content-Type`・`Accept`・`MCP-Protocol-Version: 2026-07-28`・`Mcp-Method: tools/list` のヘッダーと、`tools/list` を呼ぶ JSON-RPC の本文を加えた — [Authorization](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index#token-requirements)
- Specification の Extensions で、拡張のネゴシエーションを「初期化の際に行う」から「クライアントが各リクエストで宣言し、サーバーが `server/discover` の結果で宣言する capability を通じて行う」に改めた — [Specification](https://modelcontextprotocol.io/specification/2026-07-28/index#extensions)
- Schema Reference の `InvalidParamsError` で、Tools の項を「未知のツール名、または無効なツールの引数」から「未知のツール名、または `CallToolRequest` のスキーマを満たさないリクエスト」に改め、無効なツールの引数は `isError` を true にしたツールの実行エラーとして報告する、と加えた。Logging と Sampling の項には「(deprecated)」が付き、例の「Invalid tool arguments」は `'arguments' must be an object` を返す「Malformed tool call」に替わった。Tools の仕様のページの Error Handling は、すでに入力の検証エラーをツールの実行エラー（Tool Execution Errors）に含めている — [Schema Reference](https://modelcontextprotocol.io/specification/2026-07-28/schema#invalidparamserror)
- 同ページの `CallToolResult` に、必須の引数が足りないときに `isError` が true の結果を返す例「Missing required tool argument」を加えた — [Schema Reference](https://modelcontextprotocol.io/specification/2026-07-28/schema#calltoolresult)
- OAuth Client Credentials で、JWT Bearer Assertions のトークンの要求を `client_credentials` グラントと `client_assertion` の形に改めて `resource` を加え、`aud` を認可サーバーの issuer 識別子だけとした。Client Secrets のトークンの要求にも `resource` を加えた（詳細はハイライト 5 参照） — [OAuth Client Credentials](https://modelcontextprotocol.io/extensions/auth/oauth-client-credentials#jwt-bearer-assertions-recommended)
- Enterprise-Managed Authorization の For MCP clients で、ID-JAG を IdP のトークンエンドポイントへの Token Exchange で求めることと、そのパラメーターを明記した（詳細はハイライト 5 参照） — [Enterprise-Managed Authorization](https://modelcontextprotocol.io/extensions/auth/enterprise-managed-authorization#for-mcp-clients)

**その他**

- Extension Support Matrix の NOTE で、コアの MCP 認可の機能の例として挙げていた「(DCR, CIMD)」を削除（詳細はハイライト 4 参照） — [Extension Support Matrix](https://modelcontextprotocol.io/extensions/client-matrix#support-matrix)
- Extensions Overview の Initialization-Based Versions で、`initialize` リクエストの例の `capabilities` を `roots`（`listChanged: true`）から `elicitation: {}` に替えた — [Extensions Overview](https://modelcontextprotocol.io/extensions/overview#initialization-based-versions)
<!-- light:minor-updates:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-11-13.md](./archives/latest/2026-11-13.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-11-13.md](./archives/latest-detail/2026-11-13.md)

<!--
base_commit: 1e8d14825866e74000053b24496de73f02e2e71f
head_commit: 080ef492a175aad917a584b345b6ed85c63c5b84
generated_at_full: 2026-11-16T15:10:02+09:00
-->
