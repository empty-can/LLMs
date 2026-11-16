---
対象期間: 2026年11月13日 〜 2026年11月15日
作成日: 2026-11-15
---

# MCP 公式ドキュメント更新サマリ

```markdown
今回の対象期間の取り込みは 2 回で、MCP の入力ファイルが変わったのは 2 回目だけでした（`llms-full.txt` の追加 597 行・削除 329 行、14 ページ）。中心は Understanding MCP servers と Understanding MCP clients の書き直しで、例が `_meta` と `resultType` を含む完全な JSON-RPC メッセージになり、非推奨の Roots と Sampling の解説が外れました。

主要なものを以下に挙げます。

1. Understanding MCP clients から非推奨の Roots と Sampling の節が削られ、新設の h2「Deprecated Features」の警告に代わりの方法がまとまった。Architecture overview の非推奨の一覧も Roots・Sampling・プロトコルのログの 3 つに改められ、Debugging の TypeScript のログの例はプロトコル経由から stderr への出力に替わった
2. Understanding MCP servers の例が完全な JSON-RPC メッセージになり、`structuredContent`・キャッシュのヒント・`completion/complete`・`prompts/get` のやり取りが加わった。プロンプトの引数には型が無く、値はすべて文字列で送ると明記された
3. Understanding MCP clients の Elicitation の例が、`tools/call`・`InputRequiredResult`・`inputResponses` を付けた再送・最終の結果の 4 つのメッセージになった。クライアントが対応するモードを `elicitation` の capability で宣言する方法も書かれた
4. Understanding Authorization in MCP で、DCR が登録方式の表と h3 の節から外れ、CIMD に対応しない認可サーバーに対して既存のクライアントが使える代替手段として、警告の中で扱われるようになった
5. OAuth Client Credentials の JWT の流れが `client_credentials` グラントと `client_assertion` の形になり、`aud` には認可サーバーの issuer 識別子だけを入れるよう改められた。Enterprise-Managed Authorization では、ID-JAG を求めるトークン交換のパラメーターが明記された
```

## ハイライト

1. [**非推奨の機能の解説が削られ代わりの方法の案内にまとまった**](./latest-detail.md#1-非推奨の機能の解説が削られ代わりの方法の案内にまとまった):  
  Understanding MCP clients から Roots と Sampling の h3 の節（それぞれの例や User Interaction Model を含む）が削除され、ページ末尾に新設された h2「Deprecated Features」の警告が、Roots はツールのパラメーター・リソース URI・サーバーの設定で渡し、Sampling は LLM プロバイダーの API と直接統合する、と代わりの方法を示すようになった。Architecture overview の非推奨の一覧は Roots・Sampling・プロトコルのログの 3 つになり、Debugging の TypeScript のログの例は `notifications/message` を送る例から `console.error` で stderr に書く例に替わった。
2. [**Understanding MCP servers の例が完全な JSON-RPC メッセージになった**](./latest-detail.md#2-understanding-mcp-servers-の例が完全な-json-rpc-メッセージになった):  
  Understanding MCP servers（追加 344 行・削除 65 行）で、Tools・Resources・Prompts と The Complete Flow の例が、`_meta` にプロトコルのバージョンとクライアントの capability を持つリクエストと、`resultType` を持つ結果の組になった。`outputSchema` と `structuredContent`、`resources/read` の結果のキャッシュのヒント（`ttlMs`・`cacheScope`）、`completion/complete` による値の提案の例が加わり、プロンプトの引数には型が無く値はすべて文字列で送る、と明記された。
3. [**Elicitation の例が MRTR の往復を 4 つのメッセージで示すようになった**](./latest-detail.md#3-elicitation-の例が-mrtr-の往復を-4-つのメッセージで示すようになった):  
  Understanding MCP clients の Elicitation で、`elicitation/create` のリクエストを 1 つだけ載せていた例が、`bookVacation` ツールの `tools/call`、`resultType` が `"input_required"` の `InputRequiredResult`、`inputResponses` と `requestState` を付けた再送、`resultType` が `"complete"` の結果、の 4 つのメッセージになった。クライアントが対応するモードを `elicitation` の capability で宣言する方法と、ユーザーの応答が `accept`・`decline`・`cancel` の action に対応することも書かれた。
4. [**認可のチュートリアルで DCR が登録方式の表から外れた**](./latest-detail.md#4-認可のチュートリアルで-dcr-が登録方式の表から外れた):  
  Understanding Authorization in MCP で、Dynamic Client Registration（DCR）が登録方式の表と h3 の節から外れ、事前登録と Client ID Metadata Documents（CIMD）の 2 つになった。DCR は警告の中で、CIMD に対応せず実行時の登録を受け付ける認可サーバーに対し、既存のクライアントがユーザーにクライアント ID を尋ねる前に使える手段として扱われる。Security Best Practices と Extension Support Matrix の注記も同じ方向に改められた。
5. [**認可の拡張 2 件でトークン要求のパラメーターが明記された**](./latest-detail.md#5-認可の拡張-2-件でトークン要求のパラメーターが明記された):  
  OAuth Client Credentials の JWT Bearer Assertions の流れで、トークンの要求が `grant_type=client_credentials` と `client_assertion_type`・`client_assertion`・`resource` の形になり、JWT の `aud` は認可サーバーのトークンエンドポイントの URL から issuer 識別子だけに改められた。Enterprise-Managed Authorization では、ID-JAG を IdP のトークンエンドポイントへの Token Exchange（RFC 8693）で求めることと、そのパラメーターが明記された。

## 新規追加されたページ

今回の対象期間に新たに追加されたページはありません。索引 `llms.txt` に変更はなく、索引のエントリ数（365 件）と本文 `llms-full.txt` の収録ページ数（160 件。URL としては 159 件）はどちらも前回と同じです。

## 大幅に更新されたページ

- [**Understanding MCP servers**](./latest-detail.md#1-understanding-mcp-servers) ([MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/learn/server-concepts#core-server-features)):  
  Tools・Resources・Prompts と The Complete Flow の例を、`_meta` と `resultType` を含む完全な JSON-RPC メッセージに書き直し、`completion/complete` による値の提案と、型を持たないプロンプトの引数の説明を加えた（追加 344 行・削除 65 行。詳細はハイライト 2 参照）。
- [**Understanding MCP clients**](./latest-detail.md#2-understanding-mcp-clients) ([MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/learn/client-concepts#core-client-features)):  
  非推奨の Roots と Sampling の節を削除して h2「Deprecated Features」の警告にまとめ、Elicitation の例を MRTR の往復を示す 4 つのメッセージに書き直した（追加 145 行・削除 184 行。詳細はハイライト 1・3 参照）。

## 軽微な更新

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

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-11-13.md](./archives/latest/2026-11-13.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-11-13.md](./archives/latest-detail/2026-11-13.md)

<!--
base_commit: 1e8d14825866e74000053b24496de73f02e2e71f
head_commit: 080ef492a175aad917a584b345b6ed85c63c5b84
generated_at_full: 2026-11-16T15:10:02+09:00
-->
