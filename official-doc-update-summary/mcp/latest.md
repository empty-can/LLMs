---
対象期間: 2026年10月30日 〜 2026年10月31日
作成日: 2026-10-31
---

# MCP 公式ドキュメント更新サマリ

```markdown
今回の対象期間の取り込みは 1 回で、新規ページはなく、`llms-full.txt` の 32 ページに差分がありました。うち 17 ページはタブなどの書式の書き換えだけで、内容が変わったのは 15 ページ（うち 2 件は 50 行以上の大幅更新）です。中心は、Build an MCP client の Rust 版が Messages API を直接呼ぶ形に書き直されたことと、MCP Inspector に負荷試験と `Host` ヘッダーの検査が加わったことです。

主要なものを以下に挙げます。

1. Build an MCP client の Rust 版が書き直され、`genai` クレートをやめて Messages API を直接呼び、プロトコルの版の自動交渉・`outputSchema` による結果の検証・複数回のツール呼び出しのループを備えた
2. MCP Inspector の CLI に、ツールを繰り返し並行して呼ぶ負荷試験の `--load` と、エラー率や p99 のしきい値を超えると終了コード `10` で終わる CI ゲートが加わった（mcpdo でも使える）
3. Inspector の Web バックエンドがすべての経路の前で `Host` ヘッダーを許可リストと照合するようになり（`MCP_INSPECTOR_ALLOWED_HOSTS`）、`INSPECTOR_TLS_KEY_PATH`・`INSPECTOR_TLS_CERT_PATH` で Web UI を `https` で配信できるようになった
4. Java と Kotlin のサンプルに、各 SDK の最新の安定版が対応するプロトコルの版は `2025-11-25` で、`2026-07-28` にしか対応しない相手とはつながらないという注記が加わり、SDKs のページも、SDK は新しいリビジョンを独自の予定で採用すると明記した
5. `llms-full.txt` で、タブが `> [tab]` の行で始まる引用のブロックになり、アコーディオンとカードにも `[accordion]`・`[card]` の印が付いた。生の差分の大半はこの書き換え
```

## ハイライト

1. [**Build an MCP client の Rust 版が Messages API を直接呼ぶ形に書き直された**](./latest-detail.md#1-build-an-mcp-client-の-rust-版が-messages-api-を直接呼ぶ形に書き直された):  
  Build an MCP client の Rust のタブが書き直された。Claude の呼び出しを `genai` クレートから `reqwest` による Messages API の直接の呼び出しに替え、rmcp を `3.4` のクライアント部分だけにして、`ClientLifecycleMode::Auto` で `2026-07-28` を試し `2025-11-25` にフォールバックする形にした。ツールの `outputSchema` による結果の検証、最大 10 回のツール呼び出しのループ、拒否されたツール呼び出しを `is_error` 付きの `tool_result` で Claude に返す処理も加わった。
2. [**MCP Inspector の CLI に負荷試験と CI ゲートが加わった**](./latest-detail.md#2-mcp-inspector-の-cli-に負荷試験と-ci-ゲートが加わった):  
  Inspector の CLI の `tools/call` に、ツールを繰り返し並行して呼び、結果の代わりにレイテンシとエラー率の要約を出す `--load` の一連のフラグが加わった。`--load-max-error-rate`・`--load-max-p99` のしきい値を超えると終了コード `10` で終わる。サーバーが HTTP 429 を返したときの終了コード `11`（`rate_limited`）も加わり、mcpdo の `tools/call` も同じフラグを受け付ける。
3. [**Inspector の Web バックエンドが Host ヘッダーを検査し UI を HTTPS で配信できるようになった**](./latest-detail.md#3-inspector-の-web-バックエンドが-host-ヘッダーを検査し-ui-を-https-で配信できるようになった):  
  Inspector の Web バックエンドは、`GET /` を含むすべての経路の前で `Host` ヘッダーを許可リストと照合し、合わなければ `403` を返す。DNS リバインディングを使うページがトークンを読み取るのを防ぐためで、`Host` を書き換えるリバースプロキシのために `MCP_INSPECTOR_ALLOWED_HOSTS` で許可するホスト名を足せる。`INSPECTOR_TLS_KEY_PATH`・`INSPECTOR_TLS_CERT_PATH` を設定すると、Web UI 自体を `https` で配信できる。
4. [**Java と Kotlin のサンプルに対応するプロトコルの版の注記が加わった**](./latest-detail.md#4-java-と-kotlin-のサンプルに対応するプロトコルの版の注記が加わった):  
  Build an MCP server の Java・Kotlin のタブと Build an MCP client の Java のタブに、サンプルは各 SDK の最新の安定版が対応するプロトコルの版 `2025-11-25` を使い、`2026-07-28` にしか対応しない相手とはつながらない、という注記が加わった。SDKs のページも「どの SDK も同じ機能を提供する」という記述をやめ、SDK は新しいリビジョンを独自の予定で採用するので、対応するリビジョンは各 SDK のドキュメントで確かめるよう求めている。
5. [**llms-full.txt でタブが印付きの引用として出るようになった**](./latest-detail.md#5-llms-fulltxt-でタブが印付きの引用として出るようになった):  
  `llms-full.txt` で、これまで太字の行で始まり中身が地の文として続いていたタブが、`> [tab] 名前` の行で始まり中身も引用の中に入るブロックになった。すでに引用だったアコーディオンとカードにも `[accordion]`・`[card]` の印が付いた。24 ページに及び、生の差分の大半と、差分のあった 32 ページのうち 17 ページの変更はこの書き換えだけ。

## 新規追加されたページ

*(新規追加されたページはありません)*

## 大幅に更新されたページ

- [**Build an MCP client**](./latest-detail.md#1-build-an-mcp-client) ([MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-client#imports-and-client-structure)):  
  Rust のタブを、Messages API の直接の呼び出し・プロトコルの版の交渉・`outputSchema` による検証・ツール呼び出しのループを備えた形に書き直し、Java のタブにプロトコルの版の注記を加えて Spring AI の例を改めた（追加 445 行・削除 195 行。詳細はハイライト 1・4 参照）。
- [**Configuration and flags**](./latest-detail.md#2-configuration-and-flags) ([MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/configuration#catalog-file-format)):  
  Inspector に固有のカタログの項目と既定値の表（27 行）を Catalog file format に加え、負荷試験のフラグ、TUI・mcpdo が読む環境変数、`Host` の許可リストと TLS の環境変数などを表に足した（追加 47 行・削除 8 行）。

## 軽微な更新

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

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-10-30.md](./archives/latest/2026-10-30.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-10-30.md](./archives/latest-detail/2026-10-30.md)

<!--
base_commit: a900109552b6641cda7666a841e6800cad45d7ae
head_commit: 40e270212cf60c02b47a1f36e25f55319f572f41
generated_at_full: 2026-11-01T15:08:35+09:00
-->
