---
対象期間: 2026年11月06日 〜 2026年11月07日
作成日: 2026-11-07
---

# MCP 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
今回の対象期間の取り込みは 1 回で、MCP では `llms-full.txt` の 3 ページが変わりました。差分のほとんどは 2026-07-28 版の認可チュートリアル Understanding Authorization in MCP の書き直し（追加 536 行・削除 872 行）で、残る 2 ページは ext-skills の仕様へのリンク先が変わっただけです。

主要なものを以下に挙げます。

1. Understanding Authorization in MCP の実装例が、Keycloak を構築する手順から、どの認可サーバーにも使える JWT 検証の例（TypeScript は SDK v2、C# は .NET 10）に書き直された
2. 同じページの認可フローの説明にシーケンス図が加わり、`issuer`・`iss`・`state` の検証、`code_challenge_methods_supported` の確認、`403` の `insufficient_scope` と step-up authorization が書き込まれた
3. 新しい Client Registration Approaches の節が、事前登録・Client ID Metadata Documents（CIMD）・Dynamic Client Registration（DCR）の 3 方式と試す順序を示し、DCR を非推奨とした
4. 認可サーバーの選び方、不透明トークン、localhost 以外への配置の節が加わり、テストの節は MCP Inspector の CLI を使う手順とよくある問題 8 件に替わった
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**Authorization チュートリアルの実装例が特定の認可サーバーに依存しない形になった**](#1-authorization-チュートリアルの実装例が特定の認可サーバーに依存しない形になった):  
  Keycloak を Docker で動かして管理画面で設定する手順がなくなり、`ISSUER` と `METADATA_URL` を自分の認可サーバーに合わせて書き換える、`add` ツール 1 つのサーバーの例になった。TypeScript と Python はトークンイントロスペクションから JWT の検証（`jose`・PyJWT）に替わり、TypeScript は SDK v2 のパッケージ、C# は .NET 10 に上がった。
2. [**認可フローの説明が仕様の要件に沿って詳しくなった**](#2-認可フローの説明が仕様の要件に沿って詳しくなった):  
  3 者の役割の説明とシーケンス図が加わり、6 つの手順に、`401` の `scope`、`issuer` の一致と `code_challenge_methods_supported` の確認、`iss`（RFC 9207）と `state` の検証、`resource` パラメーター、`403` の `insufficient_scope` と step-up authorization が書き込まれた。
3. [**クライアント登録の 3 つの方式を整理する節が加わった**](#3-クライアント登録の-3-つの方式を整理する節が加わった):  
  新しい Client Registration Approaches の節が、事前登録・CIMD・DCR の 3 方式と試す順序を表で示し、CIMD を最も一般的な方式、DCR を非推奨としている。事前登録と DCR の資格情報は、発行した認可サーバーの `issuer` ごとに保存して使い分けるよう求めている。
4. [**認可サーバーの選定や本番への配置などを扱う節が加わった**](#4-認可サーバーの選定や本番への配置などを扱う節が加わった):  
  Choosing an Authorization Server（確かめる 8 項目）、Opaque Tokens、Deploying Beyond Localhost の 3 つの節が加わった。Testing the Server（旧 Testing the MCP Server）は、VS Code の画面を示す説明から、`curl` と MCP Inspector の CLI で確かめる手順と、よくある問題 8 件の一覧に替わった。
<!-- light:highlight-list:end -->

## 1. Authorization チュートリアルの実装例が特定の認可サーバーに依存しない形になった

今回の対象期間の取り込みは 1 回で、MCP の入力ファイルのうち差分が出たのは本文 `llms-full.txt` だけです（追加 539 行・削除 875 行）。索引 `llms.txt` は変わらず（エントリ数は 364 件のまま）、`llms-full.txt` の総行数は 46,374 行から 46,038 行になり、収録ページ数は 159 件（`examples` が 2 回収録されているため、URL としては 158 件）で変わっていません。差分のあったページは 3 件で、Understanding Authorization in MCP（追加 536 行・削除 872 行）、Skills（追加 2 行・削除 2 行）、Skills Over MCP Charter（追加 1 行・削除 1 行）です。ページごとの行数は、`git diff` のハンクを head 側の `Source:` の行でページに振り分けたもので、合計は上の追加 539 行・削除 875 行に一致します。

Understanding Authorization in MCP は 2026-07-28 版のチュートリアルで、ほぼ全体が書き直されました。ページの行数（`# ` のタイトルの行から次のページの直前まで）は 1,140 行から 804 行に減り、見出し（h2・h3。コードフェンスの外で数えた値）は 8 個から 13 個に増えています。索引 `llms.txt` にはほかの版（`2025-11-25`・`draft` など）のこのページもありますが、本文 `llms-full.txt` に収録されているのは 2026-07-28 版だけなので、ほかの版が変わったかどうかはわかりません。

**Keycloak を構築する手順がなくなりました。** これまでの実装例は、Keycloak を Docker で起動し、管理画面でスコープ `mcp:tools`、audience のマッパー、動的なクライアント登録を許す Trusted Hosts、イントロスペクションに使う MCP サーバー用のクライアントを設定する手順を、画面の画像 5 枚と発行されるトークンの例とともに説明していました。新しい実装例はどの認可サーバーにも使える形で、`http://localhost:3000/mcp` で動き、`mcp:tools` のスコープを求め、RS256 で署名された JWT のアクセストークンを受け付ける、`add` ツール 1 つのサーバーです（これまでの例は `http://localhost:3000` で動き、足し算と掛け算の 2 つのツールを持っていました）。動かす前に書き換える値として、`ISSUER`（認可サーバーのメタデータの `issuer` そのまま）、`METADATA_URL`、署名アルゴリズム、スコープ、期待する audience の 5 つを挙げています。Keycloak は、新しい節 Choosing an Authorization Server の TIP「Testing Locally」で、CIMD と resource indicators を実験的にサポートする例として触れられるだけになりました（`--features=cimd,resource-indicators` で起動する）。

**トークンの検証が JWT の検証に揃いました。** これまで TypeScript と Python の例は Keycloak のイントロスペクションのエンドポイントにトークンを問い合わせ、C# の例だけが JWT を検証していました。新しい例は 3 言語ともライブラリで JWT を検証します（TypeScript は `jose` の `jwtVerify`、Python は PyJWT の `jwt.decode`、C# は ASP.NET Core の JWT bearer 認証）。署名・issuer・audience・有効期限を確かめ、時計のずれは 30 秒まで許します。TypeScript と Python は起動時に認可サーバーのメタデータを取得して `issuer` を照合し、`jwks_uri` から鍵を取ります。鍵を取得できない障害のときは、トークンが不正なときの `401` ではなく `5xx` で応じます（C# は、一度も鍵を取得できていない間だけ `500` を返す）。不透明トークンの場合のイントロスペクションは、新しい節 Opaque Tokens が文章で説明しています。

**SDK と依存の版が上がりました。** TypeScript は、これまでの単一のパッケージ `@modelcontextprotocol/sdk` から、SDK v2 の `@modelcontextprotocol/server@^2.3.0`・`@modelcontextprotocol/express@^2.0.2`・`@modelcontextprotocol/node` に替わり、Zod 4 を使います。セッションごとに `StreamableHTTPServerTransport` を保持するコードはなくなり、`createMcpHandler` で応答します。Python は `mcp>=2.0.0rc1` から `mcp>=2.2` になり、`config.py`・`server.py`・`token_verifier.py`・`pyproject.toml` に分かれていた例が `server.py` 1 つにまとまりました。C# は .NET 9（`net9.0`）・`ModelContextProtocol.AspNetCore` 2.0.0 から .NET 10（`net10.0`）・2.4.0 になり、`Tools` フォルダーの `MathTools.cs` も `Program.cs` にまとまりました。サンプルリポジトリへのリンクは 3 言語ともなくなっています。

**SDK がしないことを補うコードと説明が加わりました。** 各タブのコードの後に、SDK が何をして何をしないかの説明が付きました。TypeScript の `expectedResource` と Python の `validate_token_resource` はトークンの中身を見ないので、JWT の検証の audience を外さないよう求めています。Python の SDK はチャレンジに `scope` を入れないため、`403` の後に、すでに持っているスコープだけを要求し直すクライアントでは足りないスコープを得られないことがある、と注意しています。C# の SDK の `401` のチャレンジには `scope` が無く、`403` のチャレンジは送らず、`Origin` ヘッダーも検証しないので、例は `OnChallenge`・`OnForbidden` のイベントとミドルウェアでこれを補っています。

- [Understanding Authorization in MCP - MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/authorization#implementation-example)
- [Understanding Authorization in MCP - MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/authorization#opaque-tokens)

## 2. 認可フローの説明が仕様の要件に沿って詳しくなった

The Authorization Flow: Step by Step の冒頭に、3 者の役割の説明が加わりました。MCP サーバーはアクセストークンを検証するだけで発行はしない OAuth のリソースサーバー、MCP クライアントはユーザーの代わりに動く OAuth クライアント、認可サーバーはユーザーを認証して MCP サーバー向けのトークンを発行するもので、MCP サーバーと同じところで動かしてもよい、という説明です。続いて、ブラウザー・クライアント・MCP サーバー・認可サーバーのやり取りを示す mermaid のシーケンス図が加わりました。6 つの手順は順序を保ったまま（1 つ目は Initial Handshake から Initial Request に改称）、次の点が書き込まれています。

- **1. Initial Request**: `401` の `WWW-Authenticate` の例が、`realm="mcp"` を外し、`resource_metadata` にエンドポイントのパスを付けた `/.well-known/oauth-protected-resource/mcp` と、`scope="mcp:tools"` を示す形になった。クライアントが要求するスコープは、チャレンジの `scope`、それが無ければ PRM の `scopes_supported` のすべて、それも無ければ `scope` を付けない、の順で決める。サーバーは `resource_metadata` を付けるか PRM を well-known の URI で提供しなければならず、付けない場合にクライアントが試す URL の順序（エンドポイントのパスを付けた URL、次にパス無しの URL）も示した
- **2. Protected Resource Metadata Discovery**: `authorization_servers` には 1 件以上が要る。`resource` はクライアントが接続する URL そのものにし、一致しない文書をクライアントは使ってはならない（RFC 9728 の 3.3 節）。例の `scopes_supported` から `mcp:resources` が外れた
- **3. Authorization Server Discovery**: クライアントは RFC 8414 と OpenID Connect Discovery の両方に対応し、仕様の定める順序で URL を試す。メタデータの例に `jwks_uri`・`code_challenge_methods_supported`・`client_id_metadata_document_supported`・`authorization_response_iss_parameter_supported` などが加わり（`registration_endpoint` は外れた）、クライアントが確かめる 2 点として、`issuer` がメタデータの URL を作るのに使った issuer と一致すること、`code_challenge_methods_supported` があること（無ければ認可サーバーが PKCE に対応していないので先へ進まない）を挙げた
- **4. Client Registration**: 事前登録と DCR の説明は、新しい節 Client Registration Approaches へ移った（ハイライト 3）
- **5. User Authorization**: PKCE の `code_challenge` と `resource` パラメーター（RFC 8707）を含む認可リクエストの例が加わった。認可サーバーが RFC 9207 に対応していれば応答に `iss` が付く。クライアントはブラウザーを開く前に検証済みのメタデータの `issuer` を記録し、コードを交換する前に、どちらも正規化せずに `iss` と照合する。`iss` への対応を宣言している認可サーバーの応答に `iss` が無ければ拒否する。エラーの応答も同じで、照合に失敗したらエラーを処理も表示もしない。`state` が無いか送った値と違う応答は捨てる。トークンの応答の例から `refresh_token` が外れて `scope` が加わり、リフレッシュトークンは認可サーバーが返すこともある、という書き方になった
- **6. Making Authenticated Requests**: トークンは**すべての** HTTP リクエストの `Authorization` ヘッダーで送り、URL には載せない。リクエストの例は `GET /mcp` から、`MCP-Protocol-Version: 2026-07-28`・`Mcp-Method: tools/list` のヘッダーと、`_meta` にプロトコルの版・クライアントの情報・capabilities を入れた JSON-RPC の本文を持つ `POST /mcp` になった。トークンが無効か期限切れなら `401`、有効でもスコープが足りなければ `insufficient_scope` の `403` を返す。クライアントはチャレンジのスコープを以前要求したスコープと合わせて step-up authorization を行い、再試行の回数を抑える

- [Understanding Authorization in MCP - MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/authorization#the-authorization-flow-step-by-step)

## 3. クライアント登録の 3 つの方式を整理する節が加わった

新しい節 Client Registration Approaches は、3 つの方式と使う場面を表にまとめています。

| 方式 | 使う場面 |
|---|---|
| Pre-registration（事前登録） | クライアントがこの認可サーバーの資格情報をすでに持っている |
| Client ID Metadata Documents | クライアントとサーバーに事前の関係が無い（最も一般的） |
| Dynamic Client Registration | 非推奨。Client ID Metadata Documents に対応していない認可サーバー向け |

3 つすべてに対応するクライアントはこの順で試し、どれも使えなければユーザーにクライアントの情報を入力してもらう、としています。これまでのページは手順 4 の中で事前登録と DCR の 2 つだけを説明し、どちらも使えない場合の入力を TIP で補っていました。配下の 3 つの節の内容は次のとおりです。

- **Client ID Metadata Documents**: クライアントは HTTPS の URL を `client_id` とし、その URL に JSON の文書を置く。認可サーバーは認可リクエストを受けたときに文書を取得して検証する。URL は `https` でパスを含み、文書には少なくとも `client_id`・`client_name`・`redirect_uris` が要り、文書の `client_id` は URL と完全に一致しなければならない。CIMD に対応する認可サーバーなら同じクライアント ID を使え、MCP サーバーが認可サーバーを替えても登録し直す必要はない
- **Pre-registration**: クライアント ID（必要なら資格情報も）を事前に用意し、クライアントに組み込むか、ユーザーが入力する
- **Dynamic Client Registration**: DCR は非推奨で、新しい実装は CIMD を使うべき、という WARNING が付いた。DCR のリクエストには適切な `application_type` を含める（例は `native`）。事前登録と DCR の資格情報は発行した認可サーバーに属し、`issuer` ごとに保存して、別の認可サーバーには使わない

- [Understanding Authorization in MCP - MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/authorization#client-registration-approaches)
- [Understanding Authorization in MCP - MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/authorization#dynamic-client-registration)

## 4. 認可サーバーの選定や本番への配置などを扱う節が加わった

**Choosing an Authorization Server**: 既存の ID プロバイダーや認可サーバーの製品を使うよう勧め、クライアントの登録はクライアントと認可サーバーの間で行われるので、MCP サーバーに CIMD や DCR のコードは要らない、と説明しています。選ぶ前に確かめる 8 項目は次のとおりです。

- **Audience**: クライアントが送る `resource` をトークンの `aud` にできるか。製品が常に独自の識別子を使う場合はそれと照合し、PRM の `resource` はサーバーの URL のままにする。識別子はこの MCP サーバー専用にする
- **Metadata**: RFC 8414 か OpenID Connect Discovery でメタデータを提供し、`code_challenge_methods_supported` を含むか。PKCE に対応していてもこの値を出さない製品があるので、実際の文書を見る
- **CIMD**: CIMD に対応し、`client_id_metadata_document_supported` で宣言するか
- **Token format**: 例は署名付きの JWT のアクセストークンが前提で、そうでなければイントロスペクションのエンドポイントが要る
- **Public clients**: シークレットを持たないクライアントを受け付け、`token_endpoint_auth_methods_supported` に `none` を含むか
- **Scopes**: `mcp:tools` のようなスコープを定義できるか。スコープの名前に接頭辞を付ける製品では、例の `mcp:tools` をその名前に置き換える
- **Token lifetime**: アクセストークンを短命にし、公開クライアントのリフレッシュトークンをローテーションするか
- **Issuer in responses**: 認可の応答に `iss` を返し、`authorization_response_iss_parameter_supported` を宣言するか

**Opaque Tokens**: 不透明トークンの場合は、メタデータの `introspection_endpoint`（RFC 7662）を使います。MCP サーバー自身の資格情報が要り、権限が無いと有効なトークンでも `active` が `false` になること、`aud` の無いトークンは拒否し、`scope`・`exp` も確かめること、エンドポイントに届かないかエラーの状態（`401` でも）を返すときは障害として扱うこと、キャッシュするならトークンを暗号化し、期限までにエントリを消すことを挙げています。

**Deploying Beyond Localhost**: サーバーの URL を、クライアントが接続する `https` の URL そのものに変え（PRM の `resource` と期待する audience に使われる）、TLS を終端して元の `Host` ヘッダーを保つリバースプロキシの後ろに置き、受け付ける `Host` と `Origin` を言語ごとに設定する方法を説明しています。`Origin` を受け付けても CORS が有効になるわけではないこと、このプロトコルのリビジョンにはセッションが無いので `Mcp-Session-Id` は無視し、古いクライアントも受け付けるならセッション ID を呼び出し元の証明に使わないことも書かれています。

**Testing the Server**（旧 Testing the MCP Server）: これまでは VS Code でサーバーを追加し、同意の画面とツールの一覧を画像 3 枚で示すだけでした。新しい節は、トークン無しの `curl` で `401` と PRM を確かめ、`METADATA_URL` の文書に `code_challenge_methods_supported` があるかを見た上で、MCP Inspector の CLI（Node.js 22.19 以上が必要）で一連の流れを試す手順です。`--protocol-era modern` で 2026-07-28 のプロトコルを使い、`--client-metadata-url` で自分が置いた CIMD の文書を指定します（Inspector のリダイレクト URI は `http://127.0.0.1:6276/oauth/callback`）。続く NOTE「Common Issues」は、認可サーバーがクライアント ID を拒否する、`resource` が拒否される（`invalid_target`）、ログインに成功しても Inspector が `auth_required` を出す、すべてのトークンが `401` または `403` になる、など 8 件の症状と対処を挙げています。

- [Understanding Authorization in MCP - MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/authorization#choosing-an-authorization-server)
- [Understanding Authorization in MCP - MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/authorization#testing-the-server)

## 新規追加されたページ

<!-- light:new-pages:start -->
今回の対象期間に新たに追加されたページはありません。索引 `llms.txt` に変更はなく、索引側のエントリ数（364 件）と本文 `llms-full.txt` の収録ページ数（159 件。URL としては 158 件）はどちらも前回と同じです。
<!-- light:new-pages:end -->

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
- [**Understanding Authorization in MCP**](#1-understanding-authorization-in-mcp) ([MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/authorization#implementation-example)):  
  2026-07-28 版の認可チュートリアルをほぼ全面的に書き直した。Keycloak を前提にした実装例を認可サーバーに依存しない JWT 検証の例に替え、認可フローの説明を詳しくし、クライアント登録の方式・認可サーバーの選び方・不透明トークン・localhost 以外への配置の節を加えた（追加 536 行・削除 872 行。詳細はハイライト 1〜4 参照）。
<!-- light:updated-pages:end -->

## 1. Understanding Authorization in MCP

変更（追加 536 行・削除 872 行）はページのほぼ全体に及び、行数は 1,140 行から 804 行に、h2・h3 の見出しは 8 個から 13 個になりました。ページにあった画像 8 枚（Keycloak Setup の節の 5 枚と、テストの節の 3 枚）はすべてなくなっています。節ごとの変更は次のとおりです（節の名前は新しいページのもの）。

| 節 | 変更 |
|---|---|
| 冒頭 | 文言を整理し、仕様へのリンクを `/specification/latest/...` から `/specification/2026-07-28/...` に |
| When Should You Use Authorization? | 文言を整理。ローカルのサーバーの TIP を、stdio のサーバーは資格情報を環境から取る、という短い説明に |
| The Authorization Flow: Step by Step | 3 者の役割の説明とシーケンス図を追加。手順 1 を Initial Request に改称し、6 つの手順を書き直した（ハイライト 2） |
| Client Registration Approaches（新設）と配下の Client ID Metadata Documents・Pre-registration・Dynamic Client Registration | 3 方式の表と試す順序、CIMD の要件、DCR の非推奨、資格情報を `issuer` ごとに保存すること（ハイライト 3） |
| Choosing an Authorization Server（新設） | 確かめる 8 項目と、Keycloak でローカルに試す TIP（ハイライト 4） |
| Implementation Example | 配下の Keycloak Setup と MCP Server Setup の節をなくし、書き換える値の一覧と TypeScript・Python・C# のタブに（ハイライト 1。タブごとの変更は下の表） |
| Opaque Tokens（新設） | イントロスペクションを使う場合の注意（ハイライト 4） |
| Deploying Beyond Localhost（新設） | `https` の URL、リバースプロキシ、`Host`・`Origin` の設定、CORS、セッション ID（ハイライト 4） |
| Testing the Server（旧 Testing the MCP Server） | VS Code の画面の説明を、`curl` と MCP Inspector の CLI による確認と Common Issues の 8 件に（ハイライト 4） |
| Common Pitfalls and How to Avoid Them | 14 項目の一覧を、ほかのページへ案内する 4 つの場面（ほかの API を呼ぶ、1 つの静的なクライアント ID で OAuth を中継する、ツールが状態のハンドルを返す、クライアントを作る）と 9 項目に再編。ID トークンを受け付けない、障害時は `5xx` を返す、などが加わり、チャレンジには `realm` ではなく `scope` を含めるよう改めた。Security Best Practices へのリンク先を `/specification/2026-07-28/basic/security_best_practices` から `/docs/2026-07-28/tutorials/security/security_best_practices` に |
| Related Standards and Documentation | 5 つの規格に、OpenID Connect Discovery 1.0・RFC 9207・OAuth Client ID Metadata Document・RFC 6750 を加えて 9 つに。Authorization Extensions へのリンクを追加 |

Implementation Example のタブごとの変更は次のとおりです。

| タブ | これまで | 今回 |
|---|---|---|
| TypeScript | `@modelcontextprotocol/sdk`。Keycloak のイントロスペクションで検証。セッションごとの transport。`requiredScopes: []`。`/` で待ち受け | `@modelcontextprotocol/server@^2.3.0`・`@modelcontextprotocol/express@^2.0.2`・`@modelcontextprotocol/node`。`jose` で JWT を検証。`createMcpHandler`。`requiredScopes: ["mcp:tools"]` と `expectedResource`。`/mcp` で待ち受け |
| Python | `config.py`・`server.py`・`token_verifier.py`・`pyproject.toml`。Keycloak のイントロスペクションで検証。`mcp>=2.0.0rc1` | `server.py` 1 つ。PyJWT で JWT を検証。`AuthSettings.model_validate` と `validate_token_resource`。`mcp>=2.2` |
| C# | `net9.0`、`ModelContextProtocol`・`ModelContextProtocol.AspNetCore` 2.0.0。`Authority` と、末尾のスラッシュと大文字小文字を無視する独自の audience の検証 | `net10.0`、`ModelContextProtocol.AspNetCore` 2.4.0。`MetadataAddress`、issuer と audience の厳密な照合、`mcp:tools` のポリシー、`OnChallenge`・`OnForbidden`、`Origin` を検証するミドルウェア |

- [Understanding Authorization in MCP - MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/authorization#deploying-beyond-localhost)
- [Understanding Authorization in MCP - MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/authorization#common-pitfalls-and-how-to-avoid-them)

## 軽微な更新

<!-- light:minor-updates:start -->
今回差分が出たファイルは `llms-full.txt` の 1 件で、差分のあった 3 ページのうち、大幅更新の 1 ページのほかに、次の 2 ページでリンク先が変わりました。

**その他**

- Skills の Security Considerations の節で、ext-skills リポジトリの仕様のセキュリティの節へのリンク先が `specification/stable/skills.mdx` から `specification/beta/skills.mdx` に変わった（リンクの文言は同じ） — [Skills](https://modelcontextprotocol.io/extensions/skills/overview#security-considerations)
- 同じページの Specification の節で、仕様の全文へのリンク先が同じく `specification/stable/skills.mdx` から `specification/beta/skills.mdx` に変わった（ページ冒頭の「SEP-2640 is Final」は変わらず） — [Skills](https://modelcontextprotocol.io/extensions/skills/overview#specification)
- Skills Over MCP Charter の Completed Milestones の節で、公式の仕様へのリンク先が `specification/stable/skills.mdx` から `specification/beta/skills.mdx` に変わった — [Skills Over MCP Charter](https://modelcontextprotocol.io/community/working-groups/skills-over-mcp#completed-milestones)
<!-- light:minor-updates:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-11-06.md](./archives/latest/2026-11-06.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-11-06.md](./archives/latest-detail/2026-11-06.md)

<!--
base_commit: b3f45341023a7453d8b8e8e11e025447ef991a24
head_commit: 0b52aad1c2858e15e1387c14baa0116109fe73bd
generated_at_full: 2026-11-08T15:17:09+09:00
-->
