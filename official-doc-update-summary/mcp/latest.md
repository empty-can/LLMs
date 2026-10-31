---
対象期間: 2026年10月29日 〜 2026年10月30日
作成日: 2026-10-30
---

# MCP 公式ドキュメント更新サマリ

```markdown
今回の対象期間の取り込みは 1 回で、新規ページはなく、既存ページ 12 件に変更がありました（うち 2 件は 50 行以上の大幅更新）。中心は、Enterprise-Managed Authorization に対応製品の一覧が加わったことと、Filesystems Working Group の憲章が書き込み操作からファイルシステムの意味論全般へと対象を広げたことです。

主要なものを以下に挙げます。

1. Enterprise-Managed Authorization に「Implementation support」の節が新設され、ID-JAG を発行する IdP と受け入れる認可サーバーについて、12 製品の対応状況（Available・Early access・Experimental）が一覧になった
2. Filesystems Working Group の憲章が、Resources への書き込み操作から、範囲を絞った一覧・サーバー側の検索・読み取り・書き込み・型付きのエラーまでを含むファイルシステムの意味論全般へと対象を広げた
3. OAuth Client Credentials の SDK 例が、資格情報を発行した認可サーバーの発行元（issuer）を固定する形になった。あわせて ext-auth の仕様へのリンクが `specification/stable/<name>/2026-07-28/` の版付きパスになった
4. Build an MCP client のサンプルで、TypeScript と Kotlin がツール呼び出し後の応答のテキストブロックをすべて拾うようになり、Ruby は複数のツール結果を 1 つの user メッセージにまとめて返すようになった
5. Example Servers の「Official integrations」「Community implementations」の節が「More servers」にまとまり、案内先が GitHub の servers リポジトリから MCP Registry に変わった
```

## ハイライト

1. [**Enterprise-Managed Authorization に対応製品の一覧が加わった**](./latest-detail.md#1-enterprise-managed-authorization-に対応製品の一覧が加わった):  
  Enterprise-Managed Authorization に「Implementation support」の節が新設された。ID-JAG を発行する企業の IdP と、それを受け入れてアクセストークンを返す MCP サーバーの認可サーバーという 2 つの役割について、Athenz・Auth0・Okta・Ping Identity など 12 製品の対応状況を、各ベンダー自身のリリース表記（Available・Early access・Experimental）で一覧にしている。ID-JAG を受け入れるサーバー側のフレームワークとして、Cloudflare の `workers-oauth-provider` と FastMCP も挙がった。
2. [**Filesystems Working Group が対象をファイルシステムの意味論全般に広げた**](./latest-detail.md#2-filesystems-working-group-が対象をファイルシステムの意味論全般に広げた):  
  Filesystems Charter の Mission Statement が「Resources を双方向にして書き戻せるようにする」から「Resources を一般的なファイルシステムの意味論にそろえる」に改められた。In Scope の仕様作業は 3 項目から 7 項目になり、範囲を絞った一覧とディレクトリの走査、サーバー側の検索、一括読み取りや `seek` を含む読み取りの意味論、型付きのエラーが加わった。成果物も「単一の SEP」から「1 つ以上の Extensions Track SEP」になった。
3. [**OAuth Client Credentials の SDK 例が認可サーバーの発行元を固定するようになった**](./latest-detail.md#3-oauth-client-credentials-の-sdk-例が認可サーバーの発行元を固定するようになった):  
  OAuth Client Credentials の SDK 例に、資格情報を発行した認可サーバーの発行元を固定し、MCP サーバーが別の認可サーバーを示しても資格情報を送らないようにする、という説明が加わった。TypeScript の例には `expectedIssuer`、Python の例には `issuer` が加わり、Python の `scopes` 引数は `scope` に改められた。あわせて ext-auth の仕様へのリンクが `specification/stable/<name>/2026-07-28/` の版付きパスになった。
4. [**Build an MCP client のサンプルで応答とツール結果の扱いが改められた**](./latest-detail.md#4-build-an-mcp-client-のサンプルで応答とツール結果の扱いが改められた):  
  Build an MCP client のサンプルコードで、TypeScript と Kotlin は、ツール呼び出し後の応答から先頭のブロックだけを取り出していた処理を、テキストブロックをすべて拾う処理に変えた。Ruby は、ツール呼び出しのたびに結果を別々の user メッセージで送っていた処理を、すべてのツール結果を 1 つの user メッセージにまとめて送る処理に書き換えた。
5. [**Example Servers の外部サーバーの案内先が MCP Registry になった**](./latest-detail.md#5-example-servers-の外部サーバーの案内先が-mcp-registry-になった):  
  Example Servers で、企業が保守するサーバーと、コミュニティが保守するサーバーを GitHub の servers リポジトリの各セクションへ案内していた 2 つの節が、「More servers」の 1 つの節にまとまり、案内先が MCP Registry（registry.modelcontextprotocol.io）になった。Claude での設定例からは GitHub サーバーの項目が、Additional resources からは servers リポジトリの Resources セクションへの案内が削除された。

## 新規追加されたページ

*(新規追加されたページはありません)*

## 大幅に更新されたページ

- [**Filesystems Charter**](./latest-detail.md#1-filesystems-charter) ([MCP Docs](https://modelcontextprotocol.io/community/working-groups/filesystems#in-scope)):  
  Filesystems Working Group の憲章で、Mission Statement・In Scope・Out of Scope・Related Groups・Success Criteria を、Resources への書き込みからファイルシステムの意味論全般へと対象を広げる形に書き換え、Changelog に 2 行を加えた（追加 42 行・削除 22 行。詳細はハイライト 2 参照）。
- [**Build an MCP client**](./latest-detail.md#2-build-an-mcp-client) ([MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-client#query-processing-logic)):  
  TypeScript・Kotlin・Ruby のクエリ処理のサンプルを書き換えたほか、Java（Spring AI）の設定・C# の `using`・Ruby の依存 gem からそれぞれ 1 項目を削除した（追加 28 行・削除 23 行。詳細はハイライト 4 参照）。

## 軽微な更新

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

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-10-29.md](./archives/latest/2026-10-29.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-10-29.md](./archives/latest-detail/2026-10-29.md)

<!--
base_commit: daf68aee10e1e23402b90d685734b8fa2df7beb5
head_commit: a900109552b6641cda7666a841e6800cad45d7ae
generated_at_full: 2026-10-31T15:29:12+09:00
-->
