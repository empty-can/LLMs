---
対象期間: 2026年10月29日 〜 2026年10月30日
作成日: 2026-10-30
---

# MCP 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
今回の対象期間の取り込みは 1 回で、新規ページはなく、既存ページ 12 件に変更がありました（うち 2 件は 50 行以上の大幅更新）。中心は、Enterprise-Managed Authorization に対応製品の一覧が加わったことと、Filesystems Working Group の憲章が書き込み操作からファイルシステムの意味論全般へと対象を広げたことです。

主要なものを以下に挙げます。

1. Enterprise-Managed Authorization に「Implementation support」の節が新設され、ID-JAG を発行する IdP と受け入れる認可サーバーについて、12 製品の対応状況（Available・Early access・Experimental）が一覧になった
2. Filesystems Working Group の憲章が、Resources への書き込み操作から、範囲を絞った一覧・サーバー側の検索・読み取り・書き込み・型付きのエラーまでを含むファイルシステムの意味論全般へと対象を広げた
3. OAuth Client Credentials の SDK 例が、資格情報を発行した認可サーバーの発行元（issuer）を固定する形になった。あわせて ext-auth の仕様へのリンクが `specification/stable/<name>/2026-07-28/` の版付きパスになった
4. Build an MCP client のサンプルで、TypeScript と Kotlin がツール呼び出し後の応答のテキストブロックをすべて拾うようになり、Ruby は複数のツール結果を 1 つの user メッセージにまとめて返すようになった
5. Example Servers の「Official integrations」「Community implementations」の節が「More servers」にまとまり、案内先が GitHub の servers リポジトリから MCP Registry に変わった
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**Enterprise-Managed Authorization に対応製品の一覧が加わった**](#1-enterprise-managed-authorization-に対応製品の一覧が加わった):  
  Enterprise-Managed Authorization に「Implementation support」の節が新設された。ID-JAG を発行する企業の IdP と、それを受け入れてアクセストークンを返す MCP サーバーの認可サーバーという 2 つの役割について、Athenz・Auth0・Okta・Ping Identity など 12 製品の対応状況を、各ベンダー自身のリリース表記（Available・Early access・Experimental）で一覧にしている。ID-JAG を受け入れるサーバー側のフレームワークとして、Cloudflare の `workers-oauth-provider` と FastMCP も挙がった。
2. [**Filesystems Working Group が対象をファイルシステムの意味論全般に広げた**](#2-filesystems-working-group-が対象をファイルシステムの意味論全般に広げた):  
  Filesystems Charter の Mission Statement が「Resources を双方向にして書き戻せるようにする」から「Resources を一般的なファイルシステムの意味論にそろえる」に改められた。In Scope の仕様作業は 3 項目から 7 項目になり、範囲を絞った一覧とディレクトリの走査、サーバー側の検索、一括読み取りや `seek` を含む読み取りの意味論、型付きのエラーが加わった。成果物も「単一の SEP」から「1 つ以上の Extensions Track SEP」になった。
3. [**OAuth Client Credentials の SDK 例が認可サーバーの発行元を固定するようになった**](#3-oauth-client-credentials-の-sdk-例が認可サーバーの発行元を固定するようになった):  
  OAuth Client Credentials の SDK 例に、資格情報を発行した認可サーバーの発行元を固定し、MCP サーバーが別の認可サーバーを示しても資格情報を送らないようにする、という説明が加わった。TypeScript の例には `expectedIssuer`、Python の例には `issuer` が加わり、Python の `scopes` 引数は `scope` に改められた。あわせて ext-auth の仕様へのリンクが `specification/stable/<name>/2026-07-28/` の版付きパスになった。
4. [**Build an MCP client のサンプルで応答とツール結果の扱いが改められた**](#4-build-an-mcp-client-のサンプルで応答とツール結果の扱いが改められた):  
  Build an MCP client のサンプルコードで、TypeScript と Kotlin は、ツール呼び出し後の応答から先頭のブロックだけを取り出していた処理を、テキストブロックをすべて拾う処理に変えた。Ruby は、ツール呼び出しのたびに結果を別々の user メッセージで送っていた処理を、すべてのツール結果を 1 つの user メッセージにまとめて送る処理に書き換えた。
5. [**Example Servers の外部サーバーの案内先が MCP Registry になった**](#5-example-servers-の外部サーバーの案内先が-mcp-registry-になった):  
  Example Servers で、企業が保守するサーバーと、コミュニティが保守するサーバーを GitHub の servers リポジトリの各セクションへ案内していた 2 つの節が、「More servers」の 1 つの節にまとまり、案内先が MCP Registry（registry.modelcontextprotocol.io）になった。Claude での設定例からは GitHub サーバーの項目が、Additional resources からは servers リポジトリの Resources セクションへの案内が削除された。
<!-- light:highlight-list:end -->

## 1. Enterprise-Managed Authorization に対応製品の一覧が加わった

今回の取り込みは 1 回で、差分は本文 `llms-full.txt` の追加 145 行・削除 90 行だけです。索引 `llms.txt` は変わらず（エントリ数は 364 件のまま）、`llms-full.txt` の総行数は 45,808 行から 45,863 行になり、収録ページ数は 159 件（`examples` が 2 回収録されているため、URL としては 158 件）で変わっていません。差分のハンクをページに振り分けて数えると、変更のあったページは 12 件で、50 行以上の変更は Filesystems Charter（追加 42 行・削除 22 行）と Build an MCP client（追加 28 行・削除 23 行）の 2 件です。Enterprise-Managed Authorization は追加 44 行・削除 3 行で 50 行に届かないため分類上は軽微な更新ですが、今回最も大きな内容の追加なのでハイライトの先頭に置きます。

**「Implementation support」の節が、Client support の節の後（Related resources の前）に新設されました。** 冒頭の NOTE は、この一覧は網羅的ではなく、文書化された対応だけを記録したものなので、製品が載っていないことや空欄のセルは、その役割に対応していないことを意味しない、と断っています。本文によると、このフローには MCP クライアントのほかに 2 つの製品が関わります。ID-JAG（Identity Assertion JWT Authorization Grant）を発行する企業の IdP と、それを受け入れてアクセストークンを返す MCP サーバーの認可サーバーで、1 つの製品が両方の役割を担うこともあります。表には、少なくとも一方の役割について公開ドキュメントがある製品を載せ、各ベンダー自身のリリース表記を使います。**Available** は先行リリースの表記がない本番リリース、**Early access** はプラン・環境・申請によって提供が限られるもの、**Experimental** はベンダーの先行リリースの表記です。ID-JAG は IETF の OAuth ワーキンググループが [draft-ietf-oauth-identity-assertion-authz-grant](https://datatracker.ietf.org/doc/draft-ietf-oauth-identity-assertion-authz-grant/) で定めていますが、実装ごとに追っているドラフトの版が違うため、対象の版は各ベンダーのドキュメントで確かめるよう求めています。

表の内容は次のとおりです（「—」は原文で空欄のセル）。

| 製品 | ID-JAG の発行 | ID-JAG の受け入れ | 備考 |
|---|---|---|---|
| Athenz | Available | Available | オープンソース。ZTS がトークン交換で ID-JAG を発行し、JWT bearer grant で受け入れる |
| Auth0 | — | Early access | Cross App Access for Resource Apps。Enterprise・B2B Pro・B2B Essential の各プランで early access。外部の OIDC や SAML のエンタープライズ接続から来た ID-JAG を検証する |
| AuthPlane | — | Available | MCP 向けのセルフホスト型の認可サーバー。JWT bearer grant で受け入れ、v0.2.0 から既定で有効 |
| Descope | Available | Available | Agentic Identity Hub がエージェント向けにトークン交換で発行する。MCP サーバーの認可サーバーとしては、テナントごとの信頼する発行元に照らして検証し、Descope のアクセストークンを返す |
| Janssen Project | Available | Available | 2.2.0 以降。`identity_assertion_authz_grant` のフィーチャーフラグで既定は無効。ドラフトの revision 04 が対象 |
| Keycloak | — | Experimental | 26.7.0 以降、`identity-assertion-jwt` のフィーチャーフラグで受け入れ側に対応。ガイドはドラフトの revision 01 が対象 |
| Okta | Available | Available | Cross App Access（XAA）。発行は Identity Engine の組織向けの Okta SSO に含まれ、ユーザーごと・リソースアプリごとに月 250 件まで。それを超えるには Okta for AI Agents が要る。受け入れは、カスタム認可サーバーが Okta の発行した ID-JAG を、Okta for AI Agents とともに JWT bearer grant で受け入れる |
| Ping Identity | Available | Available | PingFederate 13.1 以降。SP 接続でのトークン交換で発行し、OAuth assertion grant の IdP 接続で受け入れる |
| Scalekit | — | Early access | Enterprise プラン。ワークスペースごとに、申請に応じて XAA を有効にする |
| Stytch | — | Available | B2B プロジェクトの Connected Apps が、外部の従業員向け IdP の ID-JAG を JWT bearer grant で Stytch のアクセストークンに交換する |
| ThunderID | Available | Available | LF Decentralized Trust のオープンソースの IAM プロジェクトで、1.0 以降。両方の役割を扱う Enterprise-Managed Authorization 専用のガイドがある |
| WorkOS AuthKit | — | Early access | 環境ごとに、申請に応じて Cross App Access を有効にする。その後はサーバーのコードの変更が要らない。Standalone MCP Auth では使えない |

発行と受け入れの両方が Available なのは 6 製品（Athenz・Descope・Janssen Project・Okta・Ping Identity・ThunderID）です。表の後には、ID-JAG を受け入れるサーバー側のフレームワークとして、Cloudflare の [`workers-oauth-provider`](https://github.com/cloudflare/workers-oauth-provider)（0.7.0 以降、実験的な `enterpriseManagedAuthorization` オプション）と FastMCP 4.0 以降（ベータ）が挙がっています。また、要求側のアプリケーションも含むコミュニティの一覧として oauth.net の [Cross-App Access directory](https://oauth.net/cross-app-access/) を紹介し、MCP クライアントの対応状況は client matrix を見るよう案内しています。

同じページでは、ほかに 2 つの変更がありました。冒頭と Related resources にある仕様へのリンクが、`ext-auth` リポジトリの `specification/stable/enterprise-managed-authorization.mdx` から `specification/stable/enterprise-managed-authorization/2026-07-28/enterprise-managed-authorization.mdx` に変わりました（版のディレクトリが挟まった形。ハイライト 3 参照）。また What it is の節で、IdP の例として挙げていた「Okta, Azure AD, or a corporate SSO system」の括弧書きが削除されました。

- [Enterprise-Managed Authorization - MCP Docs](https://modelcontextprotocol.io/extensions/auth/enterprise-managed-authorization#implementation-support)

## 2. Filesystems Working Group が対象をファイルシステムの意味論全般に広げた

Filesystems Working Group の憲章（Filesystems Charter）が書き換えられました（追加 42 行・削除 22 行）。

**Mission Statement** はこれまで、MCP の Resources を双方向にして、エージェントが入力を読んだサーバーへ結果を書き戻せるようにすることを目的に掲げ、現状の Resources は読み取りの方向しか扱っていないとして、書き込み操作・楽観的並行性制御・変更通知とキャッシュとの関係を扱う単一の Extensions Track SEP を作るとしていました。新しい記述では、Resources を一般的なファイルシステムの意味論にそろえ、MCP クライアントが提供元をまたいで、ファイルシステムの形をしたリソースを見つけ・取得し・変更するための 1 つのインターフェースを、効率よく使えるようにすることを目的としています。WG はどのファイルシステムの意味論が MCP に合うかを見極め、それを Resources に一貫して適用する 1 つ以上の Extensions Track SEP を作ります。

**In Scope** の仕様作業は、「Filesystem Operations for Resources」という仮題の単一の SEP から、リソースの操作を定める 1 つ以上の Extensions Track SEP に変わり、扱う項目が 3 つから 7 つになりました。

| 新 | 項目 | 内容 | 旧との対応 |
|---|---|---|---|
| 1 | Scoped listing and directory traversal | URI を起点にした、階層を意識した一覧を検討する。URI の 1 階層下を列挙する `readdir` に相当する操作、サブツリー全体の走査、両者と既存の平坦な `resources/list` との関係を含む | 新規 |
| 2 | Server-side search | サーバー側で評価する検索と glob マッチを検討し、すべてのリソースを一覧して読まなくても内容を見つけられるようにする。サーバーが受け付ける URI を示すリソーステンプレートを超えるもので、1 と合わせて、クライアントがサーバー上の内容を見つける方法を扱う | 新規 |
| 3 | Read semantics | MCP に合う読み取りの意味論を検討する。1 回のリクエストで複数の URI を読む一括読み取りと、プロトコルが `seek` 操作を扱えるかを含む | 新規 |
| 4 | Write and metadata operations | 作成・更新・削除と、本体を取得せずに 1 つの URI の有無・サイズ・最終更新日時を答えるメタデータの読み取り（`stat`）を定める | 旧 1（Operations） |
| 5 | Optimistic concurrency control | 2 つの書き手が更新を失わずに済む方法と、存在しない場合だけ作成する前提条件でのリソースの作成を定める | 旧 2（文面は同じ） |
| 6 | Typed errors | not found・already exists・precondition failed・permission denied などのリソース操作のエラーを定め、サーバーが違ってもクライアントが同じように失敗を扱えるようにする。現状、存在しないリソースには汎用の `-32602`（Invalid Params）が返る | 新規 |
| 7 | Change notification and caching | `notifications/resources/updated`、有効期間とキャッシュ範囲のフィールド `ttlMs`・`cacheScope`、`lastModified` 注釈との関係を定める | 旧 3（対象が「書き込み」から「ファイルシステムの操作」に） |

周辺の記述も、書き込みからファイルシステムの意味論全般へと言い換えられています。

- **Documentation**: 仕様に記すものが「新しい操作」から「採用したファイルシステムの意味論」に、サーバー作者向けの指針が「リソースの書き込み経路とツールベースの経路のどちらを選ぶか」から「リソースの操作とツールベースの操作のどちらを選ぶか」になった
- **Out of Scope**: 「POSIX など、OS のファイルシステム API の完全な写像」が加わった（WG はクライアントとサーバーのプロトコルに合う意味論を選び、除外したものはその理由を記録する）。認可ポリシーの除外対象は「書き込み」から「ファイルシステムの操作」になった
- **Related Groups**: File Uploads WG の項目に、発見・検索・メタデータ・小さなインラインの書き込みは大きな内容の転送に依存しないので独立に進められること、ツールがすでにリソースリンクを返すことから、ファイルを受け取るツールの入力が Resource への参照を受け取れるかについても両グループで合意すべきことが加わった。Agents IG の項目は、マルチエージェントやジョブのオーケストレーションの仕組みを「共有の書き込み経路」ではなく「共有のファイルシステムの意味論」の主な利用者と位置付けた
- **Success Criteria**: 1 つ目の基準が、範囲を絞った一覧とディレクトリの走査、サーバー側の検索、一括読み取りを含む読み取り・書き込み・メタデータの意味論を定める 1 つ以上の Extensions Track SEP の採択に変わった。採択される成果物には、`seek` についての WG の結論の記録、楽観的並行性制御の仕組みと型付きのエラーの一式の定義、`notifications/resources/updated`・`ttlMs`・`cacheScope`・`lastModified` との関係の規定が求められる。4 つ目の基準の「書き込み経路を使う独立した 2 つのサーバー実装」は「採用したファイルシステムの操作を使う独立した 2 つのサーバー実装」になった

**Changelog** の表には、初版（2026年08月24日「Initial charter」）の上に 2 行が加わりました。2026年09月10日の「Broaden scope to filesystem semantics」と 2026年10月27日の「Add search, bulk reads and typed errors to resource scope」で、2026年09月10日付けの行も今回の取り込みで初めて現れたものです。なお Active Work Items の表は変わっておらず、「SEP: Filesystem Operations for Resources」（Ideating）の行も旧来の仮題のまま残っています。

- [Filesystems Charter - MCP Docs](https://modelcontextprotocol.io/community/working-groups/filesystems#in-scope)

## 3. OAuth Client Credentials の SDK 例が認可サーバーの発行元を固定するようになった

OAuth Client Credentials の SDK examples の節で、資格情報の形式を選ぶよう促す文の後に、「各サンプルは資格情報を発行した認可サーバーの発行元（issuer）を固定しており、MCP サーバーが別の認可サーバーを示しても、クライアントはそこへ資格情報を送らない」という説明が加わりました。これに合わせて、4 つのサンプルが次のように変わっています。

- **TypeScript**: クライアントシークレットを使う `ClientCredentialsProvider` と、JWT の秘密鍵を使う `PrivateKeyJwtProvider` の両方に `expectedIssuer: "https://auth.example.com"` が加わった
- **Python**: `ClientCredentialsOAuthProvider` と `PrivateKeyJWTOAuthProvider` の両方で、`scopes="read write"` が `scope="read write"` に改められ、`issuer="https://auth.example.com"` が加わった

**あわせて、ext-auth の仕様へのリンクが版付きのパスになりました。** OAuth Client Credentials の冒頭と Related resources にある仕様へのリンクは、`specification/draft/oauth-client-credentials.mdx` から `specification/stable/oauth-client-credentials/2026-07-28/oauth-client-credentials.mdx` に変わりました。Enterprise-Managed Authorization の仕様へのリンクも `specification/stable/enterprise-managed-authorization/2026-07-28/` 配下になり（ハイライト 1 参照）、Authorization Extensions の Specification の節で両拡張の仕様の置き場所として示すリンクは、`ext-auth` リポジトリの `specification/draft` から `specification/stable` に変わりました。SEP-2133（Extensions）の Official Extensions の節で、拡張の例として挙げているリンクも、同じ OAuth Client Credentials の新しいパスに差し替えられています。この `specification/stable/<name>/2026-07-28/` という形は、Extensions Overview が Stable の拡張について「コアプロトコルのリビジョンに対応する版として公開する（例: `specification/stable/<name>/2026-07-28/`）」としている置き場所と同じ形です。

- [OAuth Client Credentials - MCP Docs](https://modelcontextprotocol.io/extensions/auth/oauth-client-credentials#sdk-examples)
- [Authorization Extensions - MCP Docs](https://modelcontextprotocol.io/extensions/auth/overview#specification)

## 4. Build an MCP client のサンプルで応答とツール結果の扱いが改められた

Build an MCP client のチュートリアルで、クエリを処理するサンプルコードが 3 つの言語のタブで書き換えられました。いずれも、モデルがツールを呼び出した後の処理です。

- **TypeScript**（Query Processing Logic）: ツールの結果を送った後の応答について、これまでは `response.content[0]` だけを見て、それがテキストならその文字列を、そうでなければ空文字列を加えていた。新しいコードは応答のブロックを順に見て、テキストのブロックをすべて加える
- **Kotlin**（Query processing logic）: 同様に、`aiResponse.content().first()` の先頭のブロックからテキストを取り出していた処理が、`aiResponse.content().forEach` でテキストのブロックをすべて加える処理になった
- **Ruby**（Query Processing Logic）: これまでは応答の `tool_use` ブロックごとに、ツールの結果を 1 件だけ含む user メッセージを加えてモデルを呼び直していた。新しいコードは、まずすべてのツールの結果を集め、それらを 1 つの user メッセージにまとめて送ってから、モデルを 1 回だけ呼び直す。その箇所には「すべての `tool_use` ブロックには、1 つの user メッセージの中に対応する `tool_result` が要る」というコメントが付いている

ほかのタブにも小さな変更があります（詳細は「大幅に更新されたページ」を参照）。

- [Build an MCP client - MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-client#query-processing-logic)

## 5. Example Servers の外部サーバーの案内先が MCP Registry になった

Example Servers では、これまで 2 つの h2 の節で外部のサーバーを案内していました。「Official integrations」は企業が自社のプラットフォーム向けに保守するサーバーの一覧として、「Community implementations」はコミュニティのメンバーが保守するサーバーの一覧として、それぞれ GitHub の `modelcontextprotocol/servers` リポジトリの該当セクションへのリンクを置いていました。この 2 つの節が「More servers」の 1 つの節にまとまり、企業やコミュニティのメンバーが公開したサーバーは MCP Registry（[registry.modelcontextprotocol.io](https://registry.modelcontextprotocol.io/)）で探すよう案内する 1 文になりました。

同じページでは、ほかに 2 つの項目が削除されました。

- **Configuring with Claude**: 設定の JSON の例から、`@modelcontextprotocol/server-github` を `npx` で起動し `GITHUB_PERSONAL_ACCESS_TOKEN` を渡す `github` サーバーの項目が削除され、`memory` と `filesystem` の 2 つが残った
- **Additional resources**: servers リポジトリの Resources セクション（MCP に関連するリソースやプロジェクトの一覧）への案内が削除され、GitHub Discussions への案内だけが残った

Reference implementations の節（現行の参照サーバー 7 件と、アーカイブ済みのサーバーの案内）は変わっていません。このページは `llms-full.txt` に 2 回収録されており、両方に同じ変更が入っています（それぞれ追加 2 行・削除 15 行）。

- [Example Servers - MCP Docs](https://modelcontextprotocol.io/examples#more-servers)

## 新規追加されたページ

<!-- light:new-pages:start -->
*(新規追加されたページはありません)*
<!-- light:new-pages:end -->

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
- [**Filesystems Charter**](#1-filesystems-charter) ([MCP Docs](https://modelcontextprotocol.io/community/working-groups/filesystems#in-scope)):  
  Filesystems Working Group の憲章で、Mission Statement・In Scope・Out of Scope・Related Groups・Success Criteria を、Resources への書き込みからファイルシステムの意味論全般へと対象を広げる形に書き換え、Changelog に 2 行を加えた（追加 42 行・削除 22 行。詳細はハイライト 2 参照）。
- [**Build an MCP client**](#2-build-an-mcp-client) ([MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-client#query-processing-logic)):  
  TypeScript・Kotlin・Ruby のクエリ処理のサンプルを書き換えたほか、Java（Spring AI）の設定・C# の `using`・Ruby の依存 gem からそれぞれ 1 項目を削除した（追加 28 行・削除 23 行。詳細はハイライト 4 参照）。
<!-- light:updated-pages:end -->

## 1. Filesystems Charter

変更は Mission Statement・Scope（In Scope・Out of Scope・Related Groups）・Success Criteria・Changelog の各節にあり、Group Type・Leadership・Authority & Decision Rights・Membership・Operations の各節と、Deliverables & Success Metrics の Active Work Items の表は変わっていません。In Scope のうち Cross-Cutting Concerns の項目（SEP-2571・SEP-2532・SEP-1708 の 3 つの提案を 1 つの設計にまとめる）と、Out of Scope の `files/*` の並立する仕組みとホスト側のサンドボックスを除外する 2 項目も、そのままです。内容はハイライト 2 を参照してください。

- [Filesystems Charter - MCP Docs](https://modelcontextprotocol.io/community/working-groups/filesystems#mission-statement)

## 2. Build an MCP client

変更（追加 28 行・削除 23 行）は、言語のタブごとに次のとおりです。Python と Rust のタブは変わっていません。

| タブ | 節 | 行数 | 変更 |
|---|---|---|---|
| TypeScript | Query Processing Logic | 追加 5・削除 3 | ツール呼び出し後の応答のテキストブロックをすべて加える（ハイライト 4） |
| Java | MCP Client Configuration | 削除 1 | Spring AI の `application.yml` の例で、`spring.ai.mcp.client.stdio` の下の `root-change-notification: true` を削除 |
| Kotlin | Query processing logic | 追加 3・削除 1 | ツール呼び出し後の応答のテキストブロックをすべて加える（ハイライト 4） |
| C# | Basic Client Structure | 削除 1 | `using ModelContextProtocol.Protocol.Transport;` を削除 |
| Ruby | Setting Up Your Environment | 追加 2・削除 2 | 2 つのコマンド例（`touch client.rb` の版と `new-item client.rb` の版）で、`bundle add` から `base64` を外し `anthropic dotenv mcp` にした |
| Ruby | Query Processing Logic | 追加 18・削除 15 | ツールの結果を 1 つの user メッセージにまとめて送る（ハイライト 4） |

- [Build an MCP client - MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-client#query-processing-logic)

## 軽微な更新

<!-- light:minor-updates:start -->
今回差分が出たファイルは `llms-full.txt` の 1 件で、大幅更新の 2 ページのほかに、次の 10 ページに変更がありました。

**新機能**

- Enterprise-Managed Authorization に、ID-JAG の発行・受け入れに対応する製品の一覧「Implementation support」の節を新設（詳細はハイライト 1 参照） — [Enterprise-Managed Authorization](https://modelcontextprotocol.io/extensions/auth/enterprise-managed-authorization#implementation-support)

**機能改善**

- OAuth Client Credentials の SDK 例で、認可サーバーの発行元を固定する `expectedIssuer`（TypeScript）・`issuer`（Python）を追加し、Python の `scopes` を `scope` に変更（詳細はハイライト 3 参照） — [OAuth Client Credentials](https://modelcontextprotocol.io/extensions/auth/oauth-client-credentials#sdk-examples)
- Connect to local MCP servers の Installing the Filesystem Server で、設定ファイルの場所に Linux の `~/.config/Claude/claude_desktop_config.json` を追加 — [Connect to local MCP servers](https://modelcontextprotocol.io/docs/2026-07-28/develop/connect-local-servers#installing-the-filesystem-server)
- 同ページの Troubleshooting の「Getting logs from Claude Desktop」で、ログの場所に Linux の `~/.config/Claude/logs` を加え、ログを追うコマンド例を macOS（`~/Library/Logs/Claude/mcp*.log`。これまでは「macOS/Linux」の表記）と Linux（`~/.config/Claude/logs/mcp*.log`）に分けた — [Connect to local MCP servers](https://modelcontextprotocol.io/docs/2026-07-28/develop/connect-local-servers#troubleshooting)
- Skills の Reading Directories で、`resources/directory/read` の応答例に `"ttlMs": 300000` と `"cacheScope": "public"` を追加（Listing Skills と Reading Skill Content の応答例と同じ値） — [Skills](https://modelcontextprotocol.io/extensions/skills/overview#reading-directories)

**その他**

- Example Servers で、「Official integrations」「Community implementations」の節を MCP Registry へ案内する「More servers」にまとめ、設定例の `github` サーバーと Additional resources の servers リポジトリへの案内を削除（詳細はハイライト 5 参照） — [Example Servers](https://modelcontextprotocol.io/examples#more-servers)
- Enterprise-Managed Authorization で、仕様へのリンク（冒頭と Related resources の 2 か所）を `specification/stable/enterprise-managed-authorization/2026-07-28/` 配下に変更（詳細はハイライト 3 参照） — [Enterprise-Managed Authorization](https://modelcontextprotocol.io/extensions/auth/enterprise-managed-authorization#related-resources)
- 同ページの What it is で、IdP の例「such as Okta, Azure AD, or a corporate SSO system」の括弧書きを削除 — [Enterprise-Managed Authorization](https://modelcontextprotocol.io/extensions/auth/enterprise-managed-authorization#what-it-is)
- OAuth Client Credentials で、仕様へのリンク（冒頭と Related resources の 2 か所）を `specification/draft/` から `specification/stable/oauth-client-credentials/2026-07-28/` 配下に変更（詳細はハイライト 3 参照） — [OAuth Client Credentials](https://modelcontextprotocol.io/extensions/auth/oauth-client-credentials#related-resources)
- Authorization Extensions の Specification で、両拡張の仕様の置き場所として示すリンクを `ext-auth` リポジトリの `specification/draft` から `specification/stable` に変更 — [Authorization Extensions](https://modelcontextprotocol.io/extensions/auth/overview#specification)
- SEP-2133: Extensions の Official Extensions で、拡張の例として挙げるリンクを `specification/draft/oauth-client-credentials.mdx` から `specification/stable/oauth-client-credentials/2026-07-28/oauth-client-credentials.mdx` に変更 — [SEP-2133: Extensions](https://modelcontextprotocol.io/seps/2133-extensions#official-extensions)
- Build an MCP server の Go のタブの System requirements で、必要な Go のバージョンを 1.24 以上から 1.25 以上に変更 — [Build an MCP server](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-server#system-requirements)
- Build an MCP App の Prerequisites で、必要な Node.js のバージョンを 18 以上から 20 以上に変更 — [Build an MCP App](https://modelcontextprotocol.io/extensions/apps/build#prerequisites)
- Security Best Practices の Confused Deputy Problem で、攻撃の説明にある dynamic client registration へのリンク先を `/specification/latest/basic/authorization#dynamic-client-registration` から `/specification/latest/basic/authorization/client-registration#dynamic-client-registration` に変更 — [Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices#confused-deputy-problem)
- Connect to local MCP servers の Troubleshooting で、ログの説明へのページ内リンクを `#getting-logs-from-claude-for-desktop` から `#getting-logs-from-claude-desktop` に修正 — [Connect to local MCP servers](https://modelcontextprotocol.io/docs/2026-07-28/develop/connect-local-servers#troubleshooting)
<!-- light:minor-updates:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-10-29.md](./archives/latest/2026-10-29.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-10-29.md](./archives/latest-detail/2026-10-29.md)

<!--
base_commit: daf68aee10e1e23402b90d685734b8fa2df7beb5
head_commit: a900109552b6641cda7666a841e6800cad45d7ae
generated_at_full: 2026-10-31T15:29:12+09:00
-->
