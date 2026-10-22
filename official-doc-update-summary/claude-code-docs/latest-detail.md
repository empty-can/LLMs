---
対象期間: 2026年10月20日 〜 2026年10月21日
作成日: 2026-10-21
---

# Claude Code 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
**今回は、changelog に v2.1.305・v2.1.306・v2.1.307 の 3 版（83 項目）が積まれ、`/claude-api api-version` や `sandbox.allowNestedUserNamespaces` が加わりました。通常のページでは、`ANTHROPIC_BASE_URL` のゲートウェイの裏でも tool search が既定でオンで、拒まれたら tool search なしで送り直すことが 8 ページに載り、プロジェクトのクラウドスレッドがリポジトリのスキル・`.mcp.json`・`.claude/settings.json` を読まないことが 10 ページで書き改められ、managed settings が skills ディレクトリのプラグインを止める場合の節ができました**。新しいページはなく、228 ページ中 94 ページ（changelog を含む）が変わり、changelog を除く変更は 1,658 行（追加 1,302・削除 356）、大幅更新は `errors`・`claude-apps-gateway-deploy`・`permission-modes`・`mcp`・`desktop`・`sandboxing`・`settings-reference` の 7 ページです。総行数は 120,396 行から 121,457 行に増えました。

主要なものを以下に挙げます。

1. changelog に v2.1.305・v2.1.306・v2.1.307 の 3 版が積まれ（424 → 427 リリース）、`/claude-api api-version`、OpenTelemetry の `claude_code.safety_event`、解析できないツールの呼び出しの 2 回の再試行などが加わった
2. `ANTHROPIC_BASE_URL` のゲートウェイの裏でも tool search が既定でオンで（v2.1.304 以降）、原因の分からない `400` か `422` の後は tool search なしで送り直す（v2.1.305 以降）と 8 ページに載り、「ファーストパーティでないホストでは tool search がオフ」という説明が外れた
3. プロジェクトのクラウドスレッドは、リポジトリが 1 つでも複数でも、各リポジトリの `CLAUDE.md` の指示だけを読み、スキル・`.mcp.json`・`.claude/settings.json` の権限のルール・フック・`env` は使わないと 10 ページで書き改められた
4. Linux と WSL2 のサンドボックスの中のコマンドにユーザー名前空間の作成を許す `sandbox.allowNestedUserNamespaces` が載り（v2.1.305 以降）、Chromium や rootless の Podman が失敗するときの h3 と、セキュリティの境界をオフにするという警告ができた
5. `strictPluginOnlyCustomization` か `skills-dir` の項目のない `strictKnownMarketplaces` があると、skills ディレクトリのプラグインがエラーなしで読み込まれない、という h3 が `plugins/loading` にでき、9 ページに反映された
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**changelog に v2.1.305・v2.1.306・v2.1.307 の 3 版が積まれた**](#1-changelog-に-v21305v21306v21307-の-3-版が積まれた):  
  changelog の先頭が v2.1.304 から v2.1.307 に進み、83 項目（v2.1.307 が 43、v2.1.306 が 2、v2.1.305 が 38）が加わりました。`/claude-api api-version`、OpenTelemetry の `claude_code.safety_event`、解析できないツールの呼び出しを最大 2 回やり直す改善、`sandbox.allowNestedUserNamespaces`、v2.1.304 でゲートウェイの裏の tool search が既定でオンになったことによる失敗の修正などです。前回までに通常のページが先に載せていた変更（`/usage` の推奨を `f` で適用する機能など）にも、changelog の項が付きました
2. [**LLM ゲートウェイの裏でも tool search が既定でオンになり拒まれたら tool search なしで送り直すと載った**](#2-llm-ゲートウェイの裏でも-tool-search-が既定でオンになり拒まれたら-tool-search-なしで送り直すと載った):  
  `mcp` に h4「Tool search through an LLM gateway」が、`llm-gateway-protocol` に h4「Retry without tool search」ができ、`ANTHROPIC_BASE_URL` のゲートウェイの裏でも tool search は既定でオン（v2.1.304 より前はオフ）、原因の分からない `400` か `422` の後は tool search なしで送り直す（v2.1.305 以降）と説明しています。`errors` の 5 つの項目、`env-vars`・`agent-sdk/tool-search`・`agent-sdk/mcp`・`feature-availability`・`prompt-caching` も改められました
3. [**プロジェクトのクラウドスレッドはリポジトリのスキル・.mcp.json・.claude/settings.json を読まないと改められた**](#3-プロジェクトのクラウドスレッドはリポジトリのスキルmcpjsonclaudesettingsjson-を読まないと改められた):  
  `claude-projects` の「What threads pick up from your repositories」の表が書き直され、クラウドスレッドが各リポジトリから読むのは直下の `CLAUDE.md`・`.claude/CLAUDE.md`・`.claude/rules/` だけで、スキル・エージェント・コマンド・`.mcp.json`・プラグイン・権限のルール・フック・`env` は、リポジトリが 1 つでも使わない、となりました。`cloud-environments`・`settings`・`skills` など 9 ページにも「プロジェクトのスレッドの外では」という限定が入っています
4. [**sandbox.allowNestedUserNamespaces で Linux のサンドボックスの中でユーザー名前空間を作れるようになった**](#4-sandboxallownestedusernamespaces-で-linux-のサンドボックスの中でユーザー名前空間を作れるようになった):  
  `sandboxing` に h3「Chromium or rootless Podman fails inside the sandbox on Linux」が、`settings-reference` に `sandbox.allowNestedUserNamespaces` の h3 ができました（v2.1.305 以降）。Chromium の `No usable sandbox!` や rootless の Podman の失敗に、`--no-sandbox`・`excludedCommands`・この設定の 3 つの対処を挙げ、この設定はセキュリティの境界をオフにする、という警告が 4 か所に入っています
5. [**managed settings で skills ディレクトリのプラグインが読み込まれなくなる場合の節ができた**](#5-managed-settings-で-skills-ディレクトリのプラグインが読み込まれなくなる場合の節ができた):  
  `plugins/loading` に h3「Skills-directory plugins blocked by managed settings」ができ、`strictPluginOnlyCustomization` で何かの種類をロックするか、`{ "source": "skills-dir" }` のない `strictKnownMarketplaces`（またはそれを含む `blockedMarketplaces`）を設定すると、`~/.claude/skills/` などのプラグインのフォルダーがエラーなしで飛ばされる、と説明しています。`plugins/org`・`settings-reference` など 9 ページに反映されました
<!-- light:highlight-list:end -->

## 1. changelog に v2.1.305・v2.1.306・v2.1.307 の 3 版が積まれた

**changelog の先頭が v2.1.304 から v2.1.307 に進み、3 版・83 項目が加わりました。** v2.1.307 が 43 項目（Added 4・Changed 7・改善 6・修正 26）、v2.1.306 が修正の 2 項目、v2.1.305 が 38 項目（Added 4・Changed 6・改善 6・修正 22）で、収録リリースは 424 から 427 になりました。前回の書式の変換から `llms-full.txt` の changelog には各版のリリース日がなく、日付はここからは分かりません。

- **v2.1.307**: `/claude-api` に、Claude API のコードを API の版 `2026-10-21` に移すサブコマンド `api-version` が加わり（`skills` のサブコマンドの表に行が、`commands` の `/claude-api` の引数の一覧にも加わった）、権限のルール・auto モード・安全のチェック・フック・サンドボックスがツールの呼び出しを止めたか、確認を求めたか、送り返したときに 1 件ずつ出る OpenTelemetry のイベント `claude_code.safety_event` が加わりました（`monitoring-usage` にはまだ載っていない）。解析できないツールの呼び出しは、ターンをエラーで終える前に最大 2 回やり直すようになり、`errors` の「Automatic retries」にも `The model's tool call could not be parsed (retry also failed).` とともに載りました（v2.1.307 より前は 1 回）。セルフホストのランナーの checkout フックは既定で 30 分で止まるようになっています
- **v2.1.306**: クラウドのセッションの中の `claude -p` が「Not logged in」と出る問題と、多くの MCP のツールを持つセッションで API のエラーが「prompt is too long」に置き換わる問題の 2 つの修正です。後者は `errors` の「Prompt is too long」にも、v2.1.305 でこの問題が出たら v2.1.306 以降に更新する、と載りました
- **v2.1.305**: `sandbox.allowNestedUserNamespaces`（詳細はハイライト 4）が加わり、v2.1.304 で tool search がゲートウェイの裏で既定でオンになったために、tool search を拒むエンドポイントやゲートウェイでどの要求も失敗した後退が直りました（詳細はハイライト 2）。起動時の警告はロゴの上に生のテキストで出るのではなくデバッグログへ送られ、何も制限しない権限のルールはバナーの下の警告の行で示されます（詳細は大幅更新 1）

前回までに通常のページが先に載せていた変更、すなわち `/usage` の推奨を `f` で適用する機能、`CLAUDE_CODE_RETRY_WATCHDOG_USAGE_LIMIT_RECHECK_MS`、mod の `Image` の iTerm2 での描画、mod のペインの幅の上限、Remote Control の spawn モードのメッセージ、VS Code の「Running start-up hooks」、Code Review の `@claude review stop` などにも、今回 changelog の項が付きました。すべての項目は「軽微な更新」に版ごとにまとめています。

- [Claude をスキルで拡張する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/skills#work-on-claude-api-projects)
- [Extend Claude with skills - Claude Code Docs (English)](https://code.claude.com/docs/en/skills#work-on-claude-api-projects)
- [Error reference - Claude Code Docs (English)](https://code.claude.com/docs/en/errors#automatic-retries)

## 2. LLM ゲートウェイの裏でも tool search が既定でオンになり拒まれたら tool search なしで送り直すと載った

**`ANTHROPIC_BASE_URL` がゲートウェイを指すときも MCP の tool search が既定でオンだと、通常のページに載りました。** これまでの `mcp`・`env-vars`・`agent-sdk/tool-search`・`feature-availability` は、`ANTHROPIC_BASE_URL` がファーストパーティでないホストを指すと、多くのプロキシが `tool_reference` のブロックを転送しないので tool search はオフになり、`ENABLE_TOOL_SEARCH=true` で上書きする、と説明していました。この記述はすべて外れ、v2.1.304 より前は `ENABLE_TOOL_SEARCH` を `true`・`auto`・`auto:N` にしない限りゲートウェイの裏で tool search はオフだった、という版の注記に変わっています。changelog の v2.1.304 には前回までに「カスタムの `ANTHROPIC_BASE_URL` の裏で tool search を既定でオンにし、ゲートウェイの 400 か 422 は tool search なしで再試行する」という項がありました。

- **`mcp` の新しい h4「Tool search through an LLM gateway」**: ゲートウェイの裏では要求に `defer_loading` のツールのフィールドと `tool_reference` のブロックが入るので、ゲートウェイはそれを転送する必要があり、すべてのツールを最初から読み込むなら `ENABLE_TOOL_SEARCH=false` をシェルか設定の `env` に書きます。v2.1.305 以降は、原因を認識できない `400` か `422` の後に tool search なしで送り直し、うまくいけば画面には何も出ずに MCP のツールが最初から読み込まれます（後でまた tool search を試すので、そのたびに拒まれる要求が 1 つ増える）。`ToolSearch` を禁じるか `--tools` から外しても、要求にはプレースホルダーの `defer_loading` の項目が残りうる、とも加わりました
- **`llm-gateway-protocol` の新しい h4「Retry without tool search」**: ゲートウェイの側から見た同じ動き（v2.1.305 以降、`defer_loading` のフィールドと `tool_reference` のブロックを外した要求がもう一度届き、再試行が成功すると以後の要求もそれらを省く）と、tool search のためには `defer_loading` と `tool_reference` を `anthropic-beta` の値とともに転送することを説明しています。同じページでは「Beta header and body field pairs」が h3 として独立し、`context_management` のフィールドの拒否も v2.1.304 以降は Claude Code が外して送り直す、と再試行の一覧が書き直されました
- **`errors`**: 「API Error: 500 Internal server error」「API Error: 401 Invalid authentication credentials」「Unable to connect to API」「There's an issue with the selected model」の 4 つの項目に、ゲートウェイの裏ですべての要求がそのように失敗するなら tool search のフィールドを拒んでいないかを `ENABLE_TOOL_SEARCH=false` で確かめる、という手順が加わり、「Extra inputs are not permitted」は、`defer_loading` か `tool_reference` を名指しするメッセージなら v2.1.305 以降に更新するか tool search をオフにする、と書き直されました

`mcp` の `ENABLE_TOOL_SEARCH` の表の `auto` の行には、いったんオンになった tool search は合計が 10% を下回っても同じ会話ではオンのままでありうる、と加わり、新しい h4「Tools that stay deferred below the `ENABLE_TOOL_SEARCH=auto` threshold」がその場合（`/context` がツールを `(deferred)` か `(loaded on-demand)` と示す）を説明しています。`agent-sdk/mcp` には、`options.mcpServers` に stdio・HTTP・SSE のサーバーがなく、`ENABLE_TOOL_SEARCH` を設定しないゲートウェイの裏では、最初のターンが保留中の設定ファイルとプラグインのサーバーをすべて最大 2 秒待つ場合が加わり、`prompt-caching` のツールを最初から読み込む場合の例からはカスタムの `ANTHROPIC_BASE_URL` のゲートウェイが外れました。

- [MCP を使用して Claude Code をツールに接続する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/mcp#tool-search-through-a-gateway)
- [Connect Claude Code to tools via MCP - Claude Code Docs (English)](https://code.claude.com/docs/en/mcp#tool-search-through-a-gateway)
- [Claude Code ゲートウェイ互換性ガイド - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/llm-gateway-protocol#retry-without-tool-search)
- [Claude Code gateway compatibility guide - Claude Code Docs (English)](https://code.claude.com/docs/en/llm-gateway-protocol#retry-without-tool-search)

## 3. プロジェクトのクラウドスレッドはリポジトリのスキル・.mcp.json・.claude/settings.json を読まないと改められた

**`claude-projects` の「What threads pick up from your repositories」が書き直され、プロジェクトのクラウドスレッドが各リポジトリから読むのは `CLAUDE.md` の指示だけになりました。** これまでは、各スレッドがプロジェクトのすべてのリポジトリの `CLAUDE.md` とスキルを読み、リポジトリが 1 つなら `.claude/settings.json` の権限のルール・フック・`env` も適用される、と 1 リポジトリと複数リポジトリの 2 列の表で説明していました。新しい表は列が 1 つで、リポジトリが 1 つでも複数でも次のとおりです。

- **読み込む**: リポジトリの直下の `CLAUDE.md`・`.claude/CLAUDE.md`・`.claude/rules/`（サブディレクトリの `CLAUDE.md` とパス固有のルールは読まない）
- **読み込まない**: `.claude/skills/` のスキル（claude.ai のアカウントで有効にする）、`.claude/` のエージェントとコマンド（スレッドを自分のコンピューターで動かす）、`.mcp.json` の MCP サーバー（claude.ai のコネクターを使う）、`.claude/settings.json` で有効にしたプラグイン（**Project settings > Plugins** で加える）
- **適用しない・動かさない**: `.claude/settings.json` の権限のルール（スレッドの中で承認するか、自分のコンピューターで動かす）、フック、`env`（クラウド環境で設定する）

同じページの承認の節からは、リポジトリの `.claude/settings.json` の権限のルールでスレッドのコマンドを許す方法と、リポジトリの数ごとの場合分けが外れ、スレッドはリポジトリの権限のルールを読まないので auto モードとスレッドの中での承認に頼る、の 1 文になりました。スキルをスレッドに届ける方法も、リポジトリにコミットするのではなく claude.ai のアカウントで有効にする形に改められています。

この書き分けに合わせて、`cloud-environments`（引き継がれる設定の表への注記と、プロジェクトのスレッドではリポジトリのフックが動かないこと）、`settings`（「Settings in cloud sessions」の新しい項目「Cloud threads in a project」）、`skills`（Project と Nested のスキルはプロジェクトのクラウドスレッドに読まれない）、`routines`、`mcp`、`mcp-quickstart`、`self-hosted-environments-configuration`、`settings-example`、`claude-code-on-the-web` の 9 ページにも「プロジェクトのスレッドの外では」という限定が入りました。changelog に対応する項目はありません。

- [Projects で Claude に継続的な作業を調整させる - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/claude-projects#what-threads-pick-up-from-your-repositories)
- [Let Claude coordinate ongoing work with Projects - Claude Code Docs (English)](https://code.claude.com/docs/en/claude-projects#what-threads-pick-up-from-your-repositories)
- [設定ファイルと優先順位 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/settings#settings-in-cloud-sessions)
- [Settings files and precedence - Claude Code Docs (English)](https://code.claude.com/docs/en/settings#settings-in-cloud-sessions)

## 4. sandbox.allowNestedUserNamespaces で Linux のサンドボックスの中でユーザー名前空間を作れるようになった

**Linux と WSL2 で、サンドボックスの中のコマンドにユーザー名前空間の作成を許す設定キー `sandbox.allowNestedUserNamespaces` が載りました**（Claude Code v2.1.305 以降。changelog の v2.1.305 の Added）。サンドボックスは既定でユーザー名前空間の作成を許さないので、それに頼るツールが失敗します。`sandboxing` の新しい h3「Chromium or rootless Podman fails inside the sandbox on Linux」は、その症状（Chromium の `No usable sandbox!`、`unshare -U true` の `Operation not permitted`（`allowAllUnixSockets` がオンなら `No space left on device`）、rootless の Podman の `cannot clone: Operation not permitted` か自分のフォルダーでの `read-only file system`）と、隔離の一部と引き換えの 3 つの対処を挙げています。

- **Chromium か Electron**: ブラウザーを `--no-sandbox` で起動する（Claude Code のサンドボックスはそのままで、ブラウザーが自分のサンドボックスなしで Web の内容を動かす）
- **rootless の Podman・Buildah、ブラウザーか `unshare` を動かすスクリプトやテストのコマンド**: `sandbox.excludedCommands` に `podman *` のようなパターンを加える（一致したコマンドはサンドボックスの外で完全なアクセスで動く。ブラウザーではブラウザーではなくテストのコマンドに一致させる）
- **Chromium・Electron の自分のサンドボックスを保つか、入れ子の bubblewrap か `unshare` を動かす**: `sandbox.allowNestedUserNamespaces` を、プロジェクトの `.claude/settings.json` ではなく `~/.claude/settings.json` で `true` にする。`unshare` で始まるコマンドは `excludedCommands` のパターンにかかわらずサンドボックスに残り、rootless の Podman と Buildah にはこの設定だけでは足りない

`CLAUDE_CODE_SUBPROCESS_ENV_SCRUB` を `1` にしたセッションでは、すべてのコマンドがサンドボックスで動き、ほかの対処の設定は効かないので、Chromium か Electron は `--no-sandbox` で起動し、ほかのツールは Claude Code の外で自分で動かします。

**この設定はセキュリティの境界をオフにします。** サンドボックスの中のコマンドのコードがサンドボックスの外で動くことがありうるので、保護されたパスや `credentials.files` の項目を含むサンドボックスの制限で悪意のあるコマンドを止められると考えないよう、警告が `sandboxing` の 3 か所（新しい h3・「Protected paths」・「Security limitations」）と `settings-reference` に入りました。auto-allow モードではそのコマンドが権限のプロンプトなしで動きうること、組織にセキュリティのチームがあればオンにする前に相談することも書かれています。`settings-reference` の新しい h3 によれば、スコープはユーザーか managed で（`~/.claude/settings.json`・`--settings` の JSON・managed settings の `true` が数えられ、プロジェクトの `.claude/settings.json` と `.claude/settings.local.json` の `true` は無視される。`CLAUDE_CODE_SUBPROCESS_ENV_SCRUB=1` のセッションではどこの `true` も無視）、既定は `false` です。`sandboxing` の「Keep developers from widening the policy」にはリポジトリがオンにできないキーとしてこのキーが、`server-managed-settings` にはユーザーの承認が要るサンドボックスの設定としてこのキーが加わりました。

- [Configure the sandboxed Bash tool - Claude Code Docs (English)](https://code.claude.com/docs/en/sandboxing#chromium-or-rootless-podman-fails-inside-the-sandbox-on-linux)
- [All settings - Claude Code Docs (English)](https://code.claude.com/docs/en/settings-reference#sandbox-allownestedusernamespaces)

## 5. managed settings で skills ディレクトリのプラグインが読み込まれなくなる場合の節ができた

**`~/.claude/skills/` かプロジェクトの `.claude/skills/` に置いた、`.claude-plugin/plugin.json` を持つフォルダー（skills ディレクトリのプラグイン）を、管理者が managed settings で止める場合が、`plugins/loading` の新しい h3「Skills-directory plugins blocked by managed settings」にまとまりました。** 次のどちらかが設定されると、これらのフォルダーはマーケットプレイスではなくユーザーかリポジトリから来るので、Claude Code は読み込みを飛ばします。

- **カスタマイズをプラグインに限るロック**: `strictPluginOnlyCustomization` が `true` か、カスタマイズの種類を 1 つ以上名指しする配列。どれか 1 種類（`mcp` など）がロックされれば、プラグインが持つ部品にかかわらずプラグイン全体が飛ばされます
- **マーケットプレイスの出どころの制限**: `{ "source": "skills-dir" }` の項目のない `strictKnownMarketplaces` の許可リスト、またはその項目のある `blockedMarketplaces`

飛ばされたフォルダーは `/plugin` にも `claude plugin list` にも出ず、エラーも出ません。`/<name>:<skill>` のコマンド・エージェント・フック・MCP サーバーがなくなりますが、スキルがロックの種類に含まれなければ、フォルダーの直下の `SKILL.md` は普通のスキルとして読み込まれます。原因は `/status` の `Setting sources` の行に `Enterprise managed settings` があるかで確かめ、プラグイン全体を読み込むには組織が許すマーケットプレイスに加えてそこから入れるか、1 回のセッションだけなら `--plugin-dir` でフォルダーを指定します。

これまで `plugins/org`・`plugins/marketplace-reference`・`settings-reference` は、`{ "source": "skills-dir" }` を許可リストに加えれば skills ディレクトリのプラグインが読み込まれ続ける、と説明していましたが、今回は、`strictPluginOnlyCustomization` で何かの種類をロックすると、この項目があっても読み込まれない、と加わりました。`settings-reference` の `strictPluginOnlyCustomization` の 4 つのサブキーの項目も、読み込まれ続けるものを「skills ディレクトリのプラグイン以外のプラグイン」のスキル・エージェント・フック・MCP サーバーと改めています。`plugins/loading` では、リポジトリのプラグインが読み込まれない原因の一覧が h4「Check why a repository plugin didn't load」になり、組織が Claude Code を管理している場合が加わりました。`plugins/cli-reference`・`plugins/create`・`plugins/publish`・`skills`・`managed-mcp` も、この場合を除く形に改められています（計 9 ページ）。changelog に対応する項目はありません。

- [Plugin loading reference - Claude Code Docs (English)](https://code.claude.com/docs/en/plugins/loading#skills-directory-plugins-blocked-by-managed-settings)
- [Manage Claude Code plugins for your organization - Claude Code Docs (English)](https://code.claude.com/docs/en/plugins/org#keep-skills-directory-plugins-loading)

## 新規追加されたページ

<!-- light:new-pages:start -->
（今回の対象期間に新規追加・削除されたドキュメントページはありません。`llms.txt` は変わらず、URL は 275 のままで、`llms-full.txt` に展開されている固有のページも 228 のままです。`Source:` の行が 231 あり 3 ページが 2 回展開されている状態も前回と同じです）
<!-- light:new-pages:end -->

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
- [**Error reference**](#1-error-reference) ([日本語](https://code.claude.com/docs/ja/errors#matches-no-tool) / [English](https://code.claude.com/docs/en/errors#matches-no-tool)):  
  197 行（追加 165・削除 32）が変わりました。「Matches no tool · check for typos」「Only a teammate can approve a shutdown request」「Managed settings need your approval」の 3 つの h3 ができ、「Failed to start OAuth callback server」は「Couldn't start the local listener that receives the browser sign-in」に改称されました。起動時の警告が対話的なセッションではバナーの下の行とデバッグログに出るようになった（v2.1.305 以降）ことに合わせて、設定の警告の各項目も書き直されています
- [**Claude apps gateway deployment and operations**](#2-claude-apps-gateway-deployment-and-operations) ([English](https://code.claude.com/docs/en/claude-apps-gateway-deploy#long-thinking-ends-in-proxy-timeouts)):  
  91 行（追加 90・削除 1）が変わりました。長い thinking の後にプロキシのタイムアウトで失敗するときの 2 つの h3（Anthropic の API の上流とそれ以外）と、Postgres の接続のプールの大きさを見積もる h4「Size the connection pool」、`API_TIMEOUT_MS` をゲートウェイの最初のバイトまでの時間より大きく保つ h3 ができました
- [**Choose a permission mode**](#3-choose-a-permission-mode) ([English](https://code.claude.com/docs/en/permission-modes#critical-paths)):  
  67 行（追加 53・削除 14）が変わりました。「Critical paths」が書き直され、`rm` と `rmdir` の重要なパスのチェックは一部のコマンドを見逃しうるので OS の制御の代わりにはならない、という警告が入りました。バックグラウンドのセッションで bypass が無視されるときと、`claude agents` が bypass の警告を出すときの 2 つの h3 もできています
- [**Connect Claude Code to tools via MCP**](#4-connect-claude-code-to-tools-via-mcp) ([English](https://code.claude.com/docs/en/mcp#read-a-background-commands-output-as-an-mcp-client)):  
  64 行（追加 55・削除 9）が変わりました。ゲートウェイの裏の tool search の 2 つの h4（詳細はハイライト 2）のほか、MCP クライアントとしてバックグラウンドのコマンドの出力を読む h3 と、ヘッダーを求めるゲートウェイの裏の MCP サーバーにサインインする h3 ができました
- [**Desktop application**](#5-desktop-application) ([English](https://code.claude.com/docs/en/desktop#start-a-task-that-claude-suggests)):  
  64 行（追加 48・削除 16）が変わりました。Claude が提案したタスクをカードのボタンで始める h3、**Option**（Windows は **Alt**）のクリックでの分割表示と **Cmd**（**Ctrl**）のクリックでの別のウィンドウ、コンテキストの使用量を示す **Context** カードが載り、「3 つのタブ」という説明が外れました
- [**Configure the sandboxed Bash tool**](#6-configure-the-sandboxed-bash-tool) ([日本語](https://code.claude.com/docs/ja/sandboxing#denied-paths-that-pass-through-a-symlink) / [English](https://code.claude.com/docs/en/sandboxing#denied-paths-that-pass-through-a-symlink)):  
  58 行（追加 50・削除 8）が変わりました。ハイライト 4 の h3 と警告のほか、macOS で symlink を経由する拒否のパスの h4 と、書き込めるプロジェクトのフォルダーがないときにユーザーの設定からサンドボックスをオンにする手順が加わりました
- [**All settings**](#7-all-settings) ([English](https://code.claude.com/docs/en/settings-reference#agentpushnotifenabled)):  
  54 行（追加 42・削除 12）が変わりました。ハイライト 4 の `sandbox.allowNestedUserNamespaces` の h3 とハイライト 5 の skills ディレクトリのプラグインの扱いのほか、`claude remote-control` のサーバーの下で動くセッションのプッシュ通知の扱いが加わりました
<!-- light:updated-pages:end -->

**行数の数え方**: `llms-full.txt` をページ単位に切り出し、`git diff --no-index --numstat` で数えた値です。今回は base と head がどちらも前回からの Markdown の書式なので、書式の正規化はしていません。この方法で 50 行以上のページを挙げました。changelog（追加 114 行）は新しい版の項が積まれただけなので大幅更新には入れず、ハイライト 1 と「軽微な更新」で扱っています。次点は `agent-view` の 49 行（追加 36・削除 13）、`code-review-customize` の 42 行、`claude-apps-gateway-on-aws` の 41 行です。

## 1. Error reference

**起動時の警告の出る場所が書き直されました（v2.1.305 以降）。** 「Configuration warnings」の冒頭は、対話的なセッションで起動時に出た警告を探すには、まず起動のバナーの下の行（`⚠ Deny rule Bsh matches no tool · check for typos` のような権限のルールの警告の一部）を、次にデバッグログ（デバッグのモードのときだけ残り、`claude --debug-file <path>` で起動して読む）を見る、テキスト出力の非対話モードでは、バックグラウンドのセッションでなければ stderr を見る、と改められました。v2.1.305 より前は、対話的なセッションでも stderr に出ていました。

- **新しい h3「Matches no tool · check for typos」**: 認識できないツール名の deny か ask のルール（`Bsh` と書いた deny ルールや、正規の名前ではなくトランスクリプトに出るラベルを使ったルール）が意図したツールに効かないことを示す、バナーの下の行です。テキスト出力の非対話モードでは `Permission deny rule "Bsh" matches no known tool — check for typos.` の長い形で stderr に出ます。`/permissions` でルールを選ぶと `From project local settings` のように定義した場所が分かり、`From enterprise managed settings` なら managed settings を管理する人に伝えます
- **既存の警告**: 「Is not matched by file permission checks」は、対話的なセッションでは全文がデバッグログに行き、deny か ask のルールなら `⚠ Deny rule Write(docs/**) never matches · use Edit(docs/**)` の行が出る（allow ルールには行が出ない）、「Has a wildcard before the rest of the command」は `⚠ Allow rule Bash(git -C * status *) allows any option at its * · use an exact value` の行が出る、と書き分けられました。「Denying Bash also turns off the PowerShell tool」「The 200K limit isn't enforced」「Working directory is a network path」の起動時の警告と、「Advisor is less capable than the current main model」の `--advisor` の警告も、対話的なセッションではデバッグログにだけ書かれる、と改められています

**ほかに 2 つの h3 が加わり、1 つが改称されました。**

- **「Couldn't start the local listener that receives the browser sign-in」（旧「Failed to start OAuth callback server」）**: ブラウザーがサインインの結果を返す `127.0.0.1` のポートを開けないときの 2 つのメッセージです。`The browser can't return the sign-in to Claude Code automatically` の通知なら、ブラウザーは開かず、通知の下の URL でサインインし、表示されたコードを `Paste code here >` に貼れば続きます。`Couldn't start the local listener that receives the browser sign-in. Try again.` ならサインインは止まっているので（`claude auth login` に入力をパイプしたときなど）、同じコマンドをやり直すか、トークンか API キーでサインインします。v2.1.305 より前は、ポートを開けないとすぐ止まって URL も示さず、`Failed to start OAuth callback server: Failed to start server. Is port 0 in use?` などと出ていました
- **「Only a teammate can approve a shutdown request」**: エージェントチームのシャットダウンの承認を、チームメイトとして動いていないセッションが送ったので断った、というメッセージです。何も送られず、何も止まりません。リードのセッションなら、まずチームメイトがすでに止まったかを確かめ、動いていればリードにそのチームメイトを止めるよう頼みます
- **「Managed settings need your approval」**: サーバー管理設定に承認の要る設定があり、実行した `claude plugin` のコマンドがキーボードから読めない（入力をパイプかリダイレクトし、macOS と Linux では `/dev/tty` も開けない）ため承認のダイアログを出せず、何も変えずに止まった、というメッセージです。ターミナルで `claude` を起動して承認してから、同じコマンドをもう一度実行します

**修正と回避の手順も加わりました。**

- **ディスクがいっぱい**: 出力を記録するファイルを作れないと、コマンドは始まらず `The command was not started: this computer's disk is full (ENOSPC)`（自分のクォータなら `EDQUOT`）と返ります。v2.1.305 より前は、`ENOSPC: no space left on device, open <path>.output` のような OS のエラーの文だけでした
- **Prompt is too long**: カスタムの `ANTHROPIC_BASE_URL` で `Prompt is too long · automatic compaction failed` が出たらモデルのコンテキストウィンドウを設定するか v2.1.299 以降に更新する、会話の圧縮中に Claude を止めた直後に出たら `/compact` してから送り直す（v2.1.304 以降に更新すれば再発しない）、v2.1.305 で MCP のツールが多く Anthropic の API に直接つないでいると無関係な 400 か 422 を隠しうるので v2.1.306 以降に更新する、の 3 つが加わりました
- **ゲートウェイの tool search**: 4 つの項目への確認の手順と「Extra inputs are not permitted」の書き直しです（詳細はハイライト 2）。「Extra inputs are not permitted」は、ゲートウェイがヘッダーを落とした場合に限らず、要求を受けたエンドポイントがフィールドを受け付けない入力として拒んだ、と説明が広がり、`context_management` を名指しするなら v2.1.304 以降に更新する（そのフィールドなしで 1 回送り直す）、とも加わっています
- **そのほか**: 「Automatic retries」にツールの呼び出しの解析の失敗の 2 回の再試行（v2.1.307）が、「Find your error」の表に `API Error: Stream idle timeout - no chunks received`（Claude apps gateway の裏なら「Long thinking ends in proxy timeouts」へ）などの新しいメッセージの行が加わりました。`~/.claude.json` の説明は「ログインとプロジェクトごとの状態」から「アカウントの詳細とプロジェクトごとの状態」に、Windows のネットワークの共有をドライブにつなぐ例は PowerShell での手順に改められています

- [エラーリファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/errors#matches-no-tool)
- [Error reference - Claude Code Docs (English)](https://code.claude.com/docs/en/errors#matches-no-tool)
- [エラーリファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/errors#couldnt-start-the-local-sign-in-listener)
- [Error reference - Claude Code Docs (English)](https://code.claude.com/docs/en/errors#couldnt-start-the-local-sign-in-listener)

## 2. Claude apps gateway deployment and operations

**長い thinking の間に止まる要求の対処が 2 つの h3 になりました。** Claude が考える間、ストリームは最初の応答のイベント `message_start` の後に keepalive の ping だけを運び、Claude Code は既定の設定では一定の時間の後にそのストリームを終えて、ストリーミングなしで要求を送り直します。

- **「Long thinking ends in proxy timeouts」（`provider: anthropic` 以外の上流）**: プロキシのログに約 12.5 分開いたままの要求が 1 つあり、その後に `504` が続くなら、ゲートウェイの policy で `CLAUDE_STREAM_IDLE_TIMEOUT_MS` を上げます。プロキシのアイドルのタイムアウトが 240 秒なら、ストリーミングなしの送信と再試行の計 10 回がそれぞれ 240 秒で切られます。プロキシのタイムアウトだけを延ばしても、ストリーミングなしの要求は Claude Code 自身の待ち（既定 300 秒）を超えると失敗します。h4「Confirm the cause」はデバッグのファイルで `Error streaming, falling back to non-streaming mode: Stream idle timeout - no chunks received` を探す手順（`CLAUDE_CODE_DISABLE_NONSTREAMING_FALLBACK=1` なら `API Error: Stream idle timeout - no chunks received` でターンが終わる）、h4「Pick a value」は ping だけで保てる時間の表（`300000` で約 12.5 分、`900000` で約 22.5 分、`1800000` で約 37.5 分。値より約 7.5 分長い）、h4「Deliver the value in a policy」は policy の `cli` などのキーの `env` に書く例と、ゲートウェイと Claude Code の再起動を示します
- **「Long thinking on an Anthropic API upstream」**: `provider: anthropic` がモデルの唯一の上流で、約 20 分開いたままの要求の後に `502` か `504` が出る場合です。保てる時間は既定で約 20 分、`900000` で 30 分、`1800000` で 45 分で、ゲートウェイの上流への待ち `timeouts.upstream_ttfb_ms` を上げる必要はありません

**Postgres の接続の数の見積もりが h4「Size the connection pool」になりました。** 各レプリカは `store.max_connections`（既定 5）まで接続を開くので、レプリカの数 × `store.max_connections` を、データベースがゲートウェイに残す接続の数（`max_connections` から予約の `superuser_reserved_connections`（PostgreSQL の既定 3）とほかのクライアントの分を引く）以下に保ちます。レプリカの数には、ローリングアップデートが古いレプリカを止める前に始める分も数えます（Amazon ECS の既定の設定と Cloud Run では同じ数だけ増えうる）。例は、自動スケールの最大 6、追加 2、プール 5 で (6 + 2) × 5 = 40、`max_connections` が 50 でほかのクライアントが 2 なら 50 − 3 − 2 = 45 で収まる、というものです。収まらなければデータベースの `max_connections` を上げるか、レプリカを減らすか、プールを小さくします（spend limits がオンでプールが小さすぎると、`spend check failed: spend precheck timed out` が出る）。トラブルシューティングの表には `remaining connection slots are reserved` と `sorry, too many clients already` の行と、`Postgres <version> is below the supported floor` の行が加わりました。

**新しい h3「Keep `API_TIMEOUT_MS` above the gateway's time to first byte」** は、応答のない要求を早く再試行するため `API_TIMEOUT_MS` を下げるなら、ゲートウェイがストリーミングの応答の最初のバイトを送るまでの時間より大きく保つよう求めています。`provider: anthropic` では上流が最初のイベントを送るまでの最長の時間より、それ以外の上流ではレスポンスヘッダーを返すまでの最長の時間より 20 秒以上大きくします（ゲートウェイはヘッダーの約 15 秒後に最初の keepalive の `ping` を送る。v2.1.229 より古いゲートウェイは ping を送らない）。

ゲートウェイのほかのページも変わりました。`claude-apps-gateway-config` には policy で 1 時間のプロンプトキャッシュを要求する h4「One-hour prompt cache」（軽微な更新を参照）と `deniedModels`・`availableModelsMatch` の行が、`claude-apps-gateway-on-gcp` には接続のプールの見積もりへの案内が、`network-config` には、Claude apps gateway の 15 秒ごとの ping ではイベントのウォッチドッグが約 7.5 分まで延び、ping だけのストリームは既定のタイムアウトで約 12.5 分で終わる、という説明が加わっています。

- [Claude apps gateway deployment and operations - Claude Code Docs (English)](https://code.claude.com/docs/en/claude-apps-gateway-deploy#long-thinking-ends-in-proxy-timeouts)
- [Claude apps gateway deployment and operations - Claude Code Docs (English)](https://code.claude.com/docs/en/claude-apps-gateway-deploy#size-the-connection-pool)

## 3. Choose a permission mode

**「Critical paths」の冒頭が書き直され、重要なパスのチェックの限界が明記されました。** Claude Code は `rm` と `rmdir` のコマンドを動かす前に調べ、対象を重要なパスと認識したものは allow ルールでも `"allow"` を返す `PreToolUse` フックでも承認しませんが、チェックは一部のコマンドを見逃しうるので、サンドボックスのような OS の制御の代わりにはならない、と加わりました。

- **警告**: チェックが見逃したコマンドは特別に扱われないので、セッションで Bash のコマンドを承認するもの（allow ルール、`bypassPermissions` モード、サンドボックスの auto-allow モード）がプロンプトなしで承認しえます。チェックは `rm` と `rmdir` だけに効くので、承認されたほかのコマンドも重要なパスを消しえます
- **認識にかかわらず効く制御**: deny ルール（インストールした mod が一部を承認しうる）、サンドボックス（OS が Bash のコマンドの書き込める場所を限る。作業ディレクトリは消しうる）、strict sandbox mode（既定ではサンドボックスの外での再試行を allow ルールか `bypassPermissions` がプロンプトなしで承認しうるので、その再試行をオフにする）

この限定に合わせて、ページ全体（どのモードも自動では承認しないものの一覧、`acceptEdits`・auto・`dontAsk`・bypass の各節）と `agent-sdk/permissions` の「重要なパスを対象とする `rm` と `rmdir`」は「認識された（recognized）重要なパスの削除」に改められ、`agent-sdk/permissions` には、そのチェックが一部のコマンドを見逃しうる、という注記が 3 か所に入りました。

**bypass の同意について 2 つの h3 ができました。**

- **「Bypass permissions ignored in a background session」**: バックグラウンドのセッションがユーザーか managed の設定に bypass の警告への同意を見つけられず、起動時の bypass の要求を無視したことを示す `Bypass permissions was requested at launch and ignored · if that was you, ~/.claude/settings.json needs "skipDangerousModePermissionPrompt": true` の通知と、`~/.claude/settings.json` にそのキーを加えて新しいバックグラウンドのセッションを始める対処です。`errors` と `agent-view` のこの通知へのリンクもこの節に改められました
- **「`claude agents` shows the bypass permissions warning that interactive sessions skip」**: 対話的なセッションは `.claude/settings.local.json` か `--settings` のファイルの `skipDangerousModePermissionPrompt` を同意とみなしますが、`claude agents` はみなさないので、警告に同意して `~/.claude/settings.json` にキーを加えます

そのほか、`acceptEdits` で確認が残るものと、`dontAsk` で allow ルールやフックが承認できないものが箇条書きになり、「the Cowork tab」の呼び方が「Cowork」に改められました。

- [Choose a permission mode - Claude Code Docs (English)](https://code.claude.com/docs/en/permission-modes#critical-paths)
- [権限モードを選択する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/permission-modes#bypass-permissions-ignored-in-a-background-session)
- [Choose a permission mode - Claude Code Docs (English)](https://code.claude.com/docs/en/permission-modes#bypass-permissions-ignored-in-a-background-session)

## 4. Connect Claude Code to tools via MCP

ページの差分の約半分は、ハイライト 2 の tool search の 2 つの h4 と `ENABLE_TOOL_SEARCH` の表の書き直しです。そのほかは次のとおりです。

- **新しい h3「Read a background command's output as an MCP client」**: `claude mcp serve` の Bash か PowerShell の結果の `backgroundOutputPath` は、コマンドがバックグラウンドで動き続けていることを示します（クライアントが `run_in_background: true` を付けたか、前景のコマンドがタイムアウトに達して移った）。出力はそのパスのファイルを開くかサーバーの `Read` に `file_path` として渡して読み、終わったかは `npm test; echo DONE` のように決まった文字列を `echo` して見分けます（ファイルには終わりの行が付かず、クライアントへの通知もない）。長い出力の末尾は、`offset` と `limit` を `1` にした `Read` で `totalLines` を取り、`offset` を `totalLines` − 9、`limit` を `10` にしてもう一度読みます（`backgroundOutputPath` は v2.1.295 以降）
- **新しい h3「Sign in to an MCP server behind a gateway that requires a header」**: ゲートウェイが `X-API-Key` のようなヘッダーを求めると、Claude Code がそれを送らない限り OAuth のサインインは失敗します。v2.1.299 以降で、サーバーの設定の `headers` に書くか `headersHelper` から返せば（managed MCP やプラグインのサーバーは管理者か作者に頼む）、`Authorization` を除く設定したヘッダーが、サーバーのオリジンへのサインイン・トークンの更新・取り消しの要求に付きます。ブラウザーで開く認可のページや、別のオリジンの認可サーバーの前のゲートウェイでは、ヘッダーなしで通すよう運用者に頼みます
- **リモートのサーバーが途中で切れたとき（「Mid-session drops of a remote server」）**: `claude -p` と Agent SDK で 5 回の再接続がすべて失敗した後の扱いが 2 つに分かれました。5xx やタイムアウトのような一時的なエラーなら HTTP か SSE のサーバーをバックグラウンドで約 30 分まで再試行し続け、その間 Agent SDK のセッションは状態を `failed` と報告し、コードから再接続できます。サインインし直す必要があれば再試行をやめて `needs-auth` を報告するので、シェルで `claude mcp login <name>` を実行します
- **そのほか**: プロジェクトのスコープのサーバーを確認なしで読み込むクラウドのセッションが「プロジェクトのスレッドの外の」ものに限られ（ハイライト 3）、組織が `ask` にしたコネクターのツールのプロンプトに選択を覚える選択肢がないのは「ターミナルでは」と限られました

- [Connect Claude Code to tools via MCP - Claude Code Docs (English)](https://code.claude.com/docs/en/mcp#read-a-background-commands-output-as-an-mcp-client)
- [Connect Claude Code to tools via MCP - Claude Code Docs (English)](https://code.claude.com/docs/en/mcp#sign-in-to-an-mcp-server-behind-a-gateway-that-requires-a-header)

## 5. Desktop application

- **新しい h3「Start a task that Claude suggests」**: Claude が今のタスクの外で直す価値のあるものに気づくと、その作業をタスクとして提案します。現在のレイアウトのローカルと SSH のセッションでは、チャットのカードの **Start**（別のセッションで始める。既定では今のセッションの環境で動き、カードが始めたセッションの状態を、サイドバーが今のセッションの下にそのセッションを示す）、**Do it here**（今のセッションにメッセージとして送る）、**Options**（環境・モデル・worktree・権限を確かめるか変える）、**Start all**（カードに複数のタスクがあれば、それぞれのセッションで順番を待たずに始める）のボタンで選びます。クラウドのセッションと以前のレイアウトでは **Suggested task** のカードの主ボタン（**Send to cloud** や **Start with worktree**）か、その横のキャレットで選びます。これまでは、タスクのチップをクリックすると自分の worktree を持つ新しいセッションで始まる、という 1 文でした
- **2 つ目のセッションの開き方（「Work in parallel with sessions」）**: 並べて開くには **Option**（Windows は **Alt**）を押しながらクリックするか、右クリックの **Open in** > **Split view**、別のウィンドウで開くには **Cmd**（Windows は **Ctrl**）を押しながらクリックするか **Open in** > **New window** を選びます。これまでは Cmd（Ctrl）のクリックが 2 つ目のペインを開く操作でした。分割表示ではフォーカスのないペインが暗くなり、フォーカスのあるセッションを分割から外すには **Cmd+Ctrl+W**（Windows は **Ctrl+Alt+W**）を押します（ショートカットの表にも加わった）
- **コンテキストの使用量（「Check usage」）**: 現在のレイアウトではセッションの詳細のパネルの **Context** カードの見出しが割合を示し、開くと分類ごとの内訳が見えます。以前のレイアウトではモデルのピッカーの横の使用量のリングのポップオーバーです。どちらでも `/context` で内訳をチャットに出せ、リングはプランの使用量を示します
- **ペインとファイル**: ペインはタイトルバーのアイコンのボタンで開き（ホバーで **Terminal**・**Changes**・**Browser**・**Files** などの名前が出る）、ボタンのない **Background tasks** や **Plan** のペインは、表示するものができると **⋮** のメニューに出ます。ファイルの右クリックの **Copy path** は、**Absolute path**・**Relative path**・**Filename** を選ぶ **Copy** のサブメニューになりました
- **Dispatch**: Dispatch が始めた Code のセッションに **Dispatch** のバッジが付く、という記述が外れ、新しい h4「Follow a session that Dispatch started」は、ほかのセッションと一緒にサイドバーに出るので、既定のグループと並びでは動くフォルダーのグループの最も新しいセッションを探す、と説明しています。設定の案内は h4「Set up Dispatch」になりました
- **そのほか**: 冒頭の「Chat・Cowork・Code の 3 つのタブ」が「Claude Code は **Code** タブで、アプリにはチャットと Cowork もある」になり（`desktop-quickstart` も同様で、**Code** タブはサイドバーの上にある、と改められた）、「Cowork タブ」は「Cowork」に改められました。computer use には macOS 14 以降が要る、と加わり、セッションをまたぐ安全の振る舞いは 4 つから 3 つになって、だれも見ていないセッション（スケジュールされたタスクの実行など）とのメッセージの送受信を禁じる項目が外れています。「Check which layout you have」では、手元で動くサードパーティのプロバイダーのセッションも Claude Desktop v3.1623.0 以降で現在のレイアウトになり（組織が自動更新を止めていれば管理者に頼む）、組織の基盤で動くセッションだけが以前のレイアウトのまま、と改められました

- [Desktop application - Claude Code Docs (English)](https://code.claude.com/docs/en/desktop#start-a-task-that-claude-suggests)
- [Desktop application - Claude Code Docs (English)](https://code.claude.com/docs/en/desktop#work-in-parallel-with-sessions)
- [Desktop アプリケーション - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/desktop#check-usage)
- [Desktop application - Claude Code Docs (English)](https://code.claude.com/docs/en/desktop#check-usage)

## 6. Configure the sandboxed Bash tool

ページの差分の大半は、ハイライト 4 の h3「Chromium or rootless Podman fails inside the sandbox on Linux」と、`allowNestedUserNamespaces` の警告（「Protected paths」と「Security limitations」）です。そのほかは次のとおりです。

- **新しい h4「Denied paths that pass through a symlink」**: macOS で、拒否するパスが symlink を経由するとき（dotfiles のリポジトリへのリンクの `~/.claude` など）、サンドボックスはそのパスの実際の場所も拒否します。サンドボックス自身の拒否と、文字どおりの `denyWrite`・`denyRead` の項目が対象です
- **`/sandbox` の `Sandbox settings not changed`**: 書き込めるプロジェクトのフォルダーがなければ、`~/.claude/settings.json` に `"sandbox": { "enabled": true }` を書いてユーザーの設定からオンにする手順が加わりました。これは auto-allow モードになり、通常の権限のモードにするには `sandbox.autoAllowBashIfSandboxed` も `false` にします。動いているセッションでは Claude が次に動かすシェルのコマンドから効き、`/sandbox` の **Mode** タブが効いているモードを示します
- **そのほか**: 保護されたパスは `allowWrite` や `Edit` の allow ルールでも外れず、外すには残りの filesystem の隔離ごとオフにする `filesystem.disabled` を使う、という説明の言い回しが改められ、managed settings が `sandbox.filesystem` を設定する場合などに `filesystem.disabled` を managed settings だけが設定できる理由が、「開発者がそのキーで filesystem の隔離をオフにできないように」と改められました。「Keep developers from widening the policy」の `allowManagedReadPathsOnly` と `allowManagedDomainsOnly` の 2 段落は 1 つにまとまっています

- [サンドボックス化された Bash ツールを設定する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/sandboxing#denied-paths-that-pass-through-a-symlink)
- [Configure the sandboxed Bash tool - Claude Code Docs (English)](https://code.claude.com/docs/en/sandboxing#denied-paths-that-pass-through-a-symlink)

## 7. All settings

- **`sandbox.allowNestedUserNamespaces`**（新しい h3。詳細はハイライト 4）: 索引の表と `sandbox` の型の一覧にも加わりました
- **skills ディレクトリのプラグイン**（詳細はハイライト 5）: `strictPluginOnlyCustomization` でどれかの面をロックすると skills ディレクトリのプラグインも読み込まれなくなる、と加わり、4 つのサブキーの項目は読み込まれ続けるものから skills ディレクトリのプラグインを除きました。`strictKnownMarketplaces` の `skills-dir` の行からは「`~/.claude/skills/` のプラグインの走査を戻す」の説明が外れ、読み込み続けるには項目を加えて `strictPluginOnlyCustomization` を設定しない、と改められています
- **`agentPushNotifEnabled`**: `claude remote-control` のサーバーの下で動くセッションは、このキーではなくアカウントに保存された値に従う、という段落が加わりました。値を変えるにはターミナルの Claude Code のセッションで `/config` の **Push when Claude decides** を切り替え、すでに望む値なら一度切り替えて戻してアカウントに保存させます。冒頭も、Claude Code がこの選択をアカウントに同期する、から、`/config` で変えるとアカウントにも保存する、に改められました
- **そのほか**: `preferredNotifChannel` に、mod の通知も同じ設定を使う、と加わり、「Sandbox path prefixes」に、波括弧は名前の中の普通の文字として一致する（`~/data/{keys,tokens}` は 2 つの候補ではなく、その名前のディレクトリ）、と加わりました。`showThinkingSummaries` からはサードパーティのプロバイダーは thinking を伏せないという記述が外れ、`allowedMcpServers` の型の説明は言い回しが改められています

- [All settings - Claude Code Docs (English)](https://code.claude.com/docs/en/settings-reference#agentpushnotifenabled)
- [All settings - Claude Code Docs (English)](https://code.claude.com/docs/en/settings-reference#strictpluginonlycustomization)

## 軽微な更新

<!-- light:minor-updates:start -->
今回の差分は **2 ファイル**（`llms-full.txt` と見出しマップ）で、`llms.txt` は変わっていません。`llms-full.txt` の生の差分は追加 1,420 行・削除 359 行で、ページの並びは変わっていません。ページ単位に切り出すと 228 ページ中 **94 ページ**が変わり、changelog が 114 行（追加のみ）、ほかの 93 ページが 1,658 行（追加 1,302・削除 356）です。生の差分との差（追加 4・削除 3）は、2 回展開されている `plugins/create` のもう一方の写しにも同じ変更が入っているためです。大幅更新の 7 ページを除く **86 ページ**と、changelog に加わった **v2.1.305・v2.1.306・v2.1.307**（83 項目）を以下にまとめます。

`llms-full.txt` の総行数は **120,396 行から 121,457 行へ 1,061 行増え**ました（生の差分の差し引き 1,420 − 359 と一致）。`Source:` の行は 231、固有のページは 228 のままで、2 回展開されている 3 ページ（`plugins/create`・`plugins/install`・`plugins/mods/overview`）も前回と同じです。コードフェンスの外の見出しは 5,737 から 5,790 へ増えました。加わった 54 は本文の新しい見出しと改称で、外れた 1 は `errors` の改称前の「Failed to start OAuth callback server」です。changelog の収録リリースは 424 から 427 になりました。

**新機能**

- `/claude-api api-version` を追加。Claude API のコードを API の版 `2026-10-21` に移します（v2.1.307。詳細はハイライト 1 参照）
- 権限のルール・auto モード・安全のチェック・フック・サンドボックスがツールの呼び出しを止めたか、確認を求めたか、送り返したときに、呼び出しごとに出る OpenTelemetry のイベント `claude_code.safety_event` を追加（v2.1.307）
- [VSCode] 音声入力が自分で止まったとき（認識された発話のないまま 15 秒たったか、2 分の上限）に、マイクのボタンに理由と、それまでのテキストは残ることを示す通知を追加（v2.1.307）
- [Code Review] Code Review に `@claude review stop`（`off`・`pause` も）を追加。新しいレビューを始めずに、プルリクエストの `@claude review always` の購読を終えます（v2.1.307。通常のページには前回までに載っていた）
- `sandbox.allowNestedUserNamespaces` を追加（v2.1.305。詳細はハイライト 4 参照）
- 無人の再試行のモード（`CLAUDE_CODE_RETRY_WATCHDOG`）が、リセットの前に解けた使用量の上限に気づくための `CLAUDE_CODE_RETRY_WATCHDOG_USAGE_LIMIT_RECHECK_MS` を追加（v2.1.305。通常のページには前回から載っていた）
- [VSCode] SessionStart か Setup のフックが動く間の「Running start-up hooks」のスピナーの状態と、スクリーンリーダーの読み上げを追加（v2.1.305。通常のページには前回から載っていた）
- [Claude Tag] Claude Tag の管理の Add place の検索に、Claude が参加していない公開の Slack チャンネルを追加。管理者がそこから設定できます（v2.1.305）
- **Claude apps gateway の policy で 1 時間のプロンプトキャッシュを要求できると載った**（`claude-apps-gateway-config` の新しい h4「One-hour prompt cache」・`claude-apps-gateway`・`prompt-caching`・`llm-gateway-protocol`・`env-vars`）。policy の `code`・`cli`・`settings` のブロックに `promptCacheTtl: 1h`（メインの会話）と `subagentPromptCacheTtl: 1h`（サブエージェント・ワークフロー・バックグラウンドの要求）を加えます（ゲートウェイのサーバーとクライアントに v2.1.242 以降）。上流が TTL を拒むと要求は失敗し、ゲートウェイも Claude Code も 5 分の TTL で再試行しないので、すべての上流がゲートウェイの扱うすべてのモデルで 1 時間を提供するときだけ設定します。spend limits が高い書き込みの料金を数えるには、ゲートウェイのサーバーに v2.1.286 以降が要ります。`claude-apps-gateway` の表の「1-hour cache TTL」は「Not available」から「Available with opt-in」に改められ、`ENABLE_PROMPT_CACHING_1H_BEDROCK` はゲートウェイが Amazon Bedrock に送る場合も Claude apps gateway のセッションでは効かない、と `env-vars` に加わりました — [English](https://code.claude.com/docs/en/claude-apps-gateway-config#one-hour-prompt-cache)
- **mod がターンを始めずに通知を出す `$.ui.notify` が載った**（`plugins/mods/api` の「Show something without starting a turn」・`plugins/mods/reference`・`plugins/mods/test`・`hooks`・`hooks-guide`・`agent-sdk/hooks`・`settings-reference`）。ユーザーの `preferredNotifChannel` に従って Claude Code の外の端末の通知を送り、タイトルは mod の名前です（空でない `{ title }` で変えられる）。`{ isSent: true, channel }` か `{ isSent: false, reason }`（`disabled`・`no-channel`・`no-surface`・`refused`）で解決し、`terminal_bell` は文字もタイトルも出さずベルを鳴らします。実行中のセッションに届くとユーザーの `Notification` フックが種類 `plugin_notification` で動き、通知の種類の一覧にも加わりました。changelog に対応する項目はありません — [日本語](https://code.claude.com/docs/ja/plugins/mods/api#show-something-without-starting-a-turn) / [English](https://code.claude.com/docs/en/plugins/mods/api#show-something-without-starting-a-turn)
- **`REVIEW.md` からほかのファイルを取り込めると載った**（`code-review-customize` の新しい h3「Include other files in REVIEW.md」・`code-review-troubleshooting`）。ルートの `REVIEW.md` に `@` とファイル名だけの行（`@review-security.md` など）を書くと、保護されたブランチから読むときにその行がファイルの内容に置き換わります。ファイルはリポジトリの直下に置き、名前は大文字・小文字まで一致させ空白を含めず、取り込みは 1 段だけで、異なるファイルは 8 つまで、合わせて 150,000 バイト未満、Markdown のリンクは合わせて 64 個までです（超えるとルートの `REVIEW.md` 全体が飛ばされる）。`code-review-troubleshooting` には、リンクが多すぎるかプルリクエストが変えるファイルへのリンクで `REVIEW.md` を飛ばしたときのメッセージの項目が加わりました — [日本語](https://code.claude.com/docs/ja/code-review-customize#include-other-files-in-review-md) / [English](https://code.claude.com/docs/en/code-review-customize#include-other-files-in-review-md)
- **構造化された出力の `StructuredOutput` のツールの呼び出しの見分け方が載った**（`agent-sdk/structured-outputs` の新しい h2「Recognize the StructuredOutput tool call」・`agent-sdk/typescript`・`agent-sdk/streaming-output`）。`outputFormat`（Python は `output_format`）を設定すると、定義していない `StructuredOutput` という名前のツールの呼び出しがメッセージのストリームに入り、`tool_use` のブロックと `Structured output provided successfully` の `tool_result` の 2 つで届きます。スキーマに合わなければ `is_error: true` で呼び直されるので、検証済みのデータは結果のメッセージの `structured_output` から読み、ツールの呼び出しを示すアプリではこの名前の呼び出しを飛ばします — [日本語](https://code.claude.com/docs/ja/agent-sdk/structured-outputs#recognize-the-structuredoutput-tool-call) / [English](https://code.claude.com/docs/en/agent-sdk/structured-outputs#recognize-the-structuredoutput-tool-call)
- **`getContextUsage()` の応答の項目の使い方が載った**（`agent-sdk/typescript` の新しい h4「Find a row by ID, a server's instruction tokens, or an entry's plugin and file」）。`categories` の各行の `id`、応答の `mcpInstructions`（指示を持つ MCP サーバーごとの `{ serverName, tokens }`）、`agents` と `skills.skillFrontmatter` の項目の `pluginId`（`name@marketplace` の形）と `path` の表と、`id` で `mcp_instructions` の行を探す例があります — [日本語](https://code.claude.com/docs/ja/agent-sdk/typescript#sdkcontrolgetcontextusageresponse) / [English](https://code.claude.com/docs/en/agent-sdk/typescript#sdkcontrolgetcontextusageresponse)
- **Agent SDK の例に完成したプロジェクトの h2 ができた**（`agent-sdk/examples` の「Fork a complete project」）。Python の SDK で買い物のエージェントかマーチャントのエージェントを作るなら、Claude for commerce の参照実装から始めます — [日本語](https://code.claude.com/docs/ja/agent-sdk/examples#fork-a-complete-project) / [English](https://code.claude.com/docs/en/agent-sdk/examples#fork-a-complete-project)
- **artifact の特定のビューへのリンクが載った**（`artifacts` の新しい h3「Link to a specific view」）。タブやセクションのあるページは、Claude にリンクを頼めば `#overview` のようなアンカー付きのリンクで 1 つのビューを直接指せます — [日本語](https://code.claude.com/docs/ja/artifacts#link-to-a-specific-view) / [English](https://code.claude.com/docs/en/artifacts#link-to-a-specific-view)
- **vim モードで質問を 1 回のキーで取り消す方法が載った**（`keybindings` の新しい h3「Cancel a question with one key press」・`interactive-mode` の新しい h3「Cancel a question in vim mode」）。質問の `Other` の行で自分の答えを入力中は `Esc` を 2 回押して取り消し、1 回で取り消すには `Select` のコンテキストで `ctrl+q` などを `select:cancel` に割り当てます（1 つを選ぶ質問の `Other` の行で、INSERT でも NORMAL でも閉じる。スクリーンリーダーのモードと複数を選ぶ質問では効かない） — [日本語](https://code.claude.com/docs/ja/keybindings#cancel-a-question-with-one-key-press) / [English](https://code.claude.com/docs/en/keybindings#cancel-a-question-with-one-key-press)
- **メッセージを並べたままセッションをバックグラウンドに移せると載った**（`interactive-mode` の新しい h3「Background a session with messages queued」）。`←` でバックグラウンドに移すと、並べたメッセージも移って送った順に読まれます。コマンド・`!` のシェルのコマンド・IDE の選択を付けたメッセージなどは移れず、並んでいると `Cannot open agents` で始まる通知が出てフォアグラウンドに残ります — [日本語](https://code.claude.com/docs/ja/interactive-mode#background-a-session-with-messages-queued) / [English](https://code.claude.com/docs/en/interactive-mode#background-a-session-with-messages-queued)
- **ループを止めずにバックグラウンドのセッションから離れる方法が載った**（`scheduled-tasks` の新しい h4「Detach without stopping a loop」）。アタッチしたバックグラウンドのセッションで Claude が待機中なら、空のプロンプトで `Ctrl+C` を 2 回押すと、自分のペースの `/loop` を止めずに切り離せます（v2.1.295 以降）。「Stop a loop」は、自分のペースのループは `Esc`（アタッチしたバックグラウンドのセッション以外では待機中の `Ctrl+C` も）で止まり `Pending wakeup cancelled` が出る、`/loop 5m` のような固定の間隔のループは Claude に取り消しを頼み、`Esc` と `Ctrl+C` では止まらない、と書き分けられました。制約の一覧にも、バックグラウンドのセッションのプロセスが動いていない間に次の起床が来ると自分のペースのループが止まること、再開したセッションの繰り返しのタスクは逃した回を実行しないことが加わっています — [日本語](https://code.claude.com/docs/ja/scheduled-tasks#detach-without-stopping-a-loop) / [English](https://code.claude.com/docs/en/scheduled-tasks#detach-without-stopping-a-loop)
- **Desktop のローカルのスケジュールされたタスクに cron の「Custom」と実行のセッションを開く方法が載った**（`desktop-scheduled-tasks` の新しい h3「Find a run's session」・`routines`・`scheduled-tasks`）。編集のフォームと「Only on this computer」が上にあるダイアログに、ローカルの時刻で評価する cron の式を取る **Custom** が加わりました（曜日と月は数字で、日曜は `0`。1 時間に 1 回より多い式は断る）。Desktop のセッションで Claude に頼めば 1 時間の制限なく、未来の 1 回の時刻も設定できます。「Find a run's session」は、実行が始めたセッションをタスクの詳細ページの **History** の行から開く方法と、サイドバーの **Scheduled** のグループ（現在のレイアウトでは **Group and sort** > **Show** > **Scheduled**）を説明しています。cloud scheduled tasks も、プリセットにない間隔は作成後の編集のダイアログの **Custom** で cron の式（`0 */2 * * *` など）を入れる形になり、比較の表は cloud の「Customizable schedule」が Yes に、Desktop の最小の間隔が「Claude が設定すれば 1 分、フォームでは 1 時間」になりました。タスクを削除してもセッションはアーカイブされるだけで、`~/.claude/scheduled-tasks/<task-name>/` のフォルダーはディスクに残る（自分で消す）、とも改められています — [日本語](https://code.claude.com/docs/ja/desktop-scheduled-tasks#find-a-runs-session) / [English](https://code.claude.com/docs/en/desktop-scheduled-tasks#find-a-runs-session)
- **以前にサインインしたのにログインのプロンプトが出る原因の h3 ができた**（`authentication` の「Login prompt still appears after an earlier sign-in」・`devcontainer`）。初回起動のログインのプロンプトは、API キーを承認した場合に加え、最初のセッションの前にシェルで `claude auth login` を実行したか、資格情報をボリュームに保つ dev container を作り直した場合にも省かれる、と書かれ、それでも出る原因（サインインの期限切れ、`forceLoginOrgUUID`、`forceLoginMethod` の種類の違い、v2.1.290 より前）を挙げています。`devcontainer` にも、ボリュームをマウントしても作り直すたびに初回のセットアップが繰り返されるなら `containerEnv` が `CLAUDE_CONFIG_DIR` を設定しているか確かめる、という注記が加わりました — [English](https://code.claude.com/docs/en/authentication#login-prompt-still-appears-after-an-earlier-sign-in)
- **Claude apps gateway で、開発者がセッションごとに請求するチームを選べる手順が載った**（`claude-apps-gateway-on-aws` の新しい h4「Let a developer choose which team to bill」）。2 つのチームで働く開発者に 2 チーム用の IdP のグループと、単一チームの policy より上に置く policy を作り、`claude --model data-claude-opus-4-8` のようにチームの id でセッションを始めます。spend limits では、どの id を使っても開発者の合計と上限は 1 つです — [English](https://code.claude.com/docs/en/claude-apps-gateway-on-aws#let-a-developer-choose-which-team-to-bill)
- **Claude apps gateway の spend limits に長いプロンプトの料金が載った**（`claude-apps-gateway-spend-limits` の新しい h4「Long-prompt rates」）。Claude Haiku 5.5 のしきい値を超えるプロンプトの高い料金について、v2.1.293 以降のゲートウェイのサーバーは要求全体をその料金で数えます（入力・キャッシュの読み取り・書き込みのトークンをしきい値に数え、`pricing.overrides` の行が一致すればその料金） — [English](https://code.claude.com/docs/en/claude-apps-gateway-spend-limits#long-prompt-rates)
- **Claude apps gateway の policy の `deniedModels` と `availableModelsMatch` の行が載った**（`claude-apps-gateway-config`）。`availableModels` が許すモデルや版をブロックし、ブロックしたモデルは `/v1/messages` で `400` になり `/v1/models` から外れます（ゲートウェイの判定に v2.1.299 以降、CLI の判定に v2.1.283 以降）。deny のリストの和集合に `deniedModels` が加わり、Claude Desktop に渡すモデルの一覧からもブロックしたモデルが外れます
- **名前を付けたサブエージェントに再起動の後もメッセージを送る方法が載った**（`sub-agents` の新しい h5「Message a subagent by name after a restart」）。再起動して再開した後に名前で送れなければ、エージェントの ID を Claude に渡します。メインの会話で最後の圧縮より後に付けた名前は再起動の後も残り、それより前の名前は残りません。ID は `~/.claude/projects/{project}/{sessionId}/subagents/` の `agent-{agentId}.meta.json` で探し、ID で 1 回送ると名前が使えるようになります（v2.1.299 より前はどの名前も残らなかった） — [日本語](https://code.claude.com/docs/ja/sub-agents#message-a-subagent-by-name-after-a-restart) / [English](https://code.claude.com/docs/en/sub-agents#message-a-subagent-by-name-after-a-restart)

**機能改善**

- WebSearch の予算を使い切ったときに Claude が受け取る通知を、ブラウザーやコンピューター使用で検索エンジンに問い合わせないようにも伝える形に変更（v2.1.307）
- `axScreenReader` の設定と、設定の `env` ブロックの `CLAUDE_AX_SCREEN_READER` を、ユーザー・managed・`--settings` の設定からだけ適用するよう変更（v2.1.307 の項。変更は v2.1.305 から）
- セルフホストのランナー: checkout フックを既定で 30 分で止め、セッションのセットアップを失敗させるよう変更。もっと長くかかるなら `--checkout-hook-timeout-min` を上げるか `0` にします（v2.1.307）
- セルフホストのランナー: Anthropic が管理する git のために作る証明書のファイルが、CLI と同じく信頼する証明書を絞るよう変更。外した数は `[runner:warn]` の行が示します（v2.1.307）
- [VSCode] 「still open somewhere else」の通知が、拡張機能の再起動で残った Claude のプロセス（たいてい 10 分ほどで自分で終わる）も扱うよう変更（v2.1.307）
- [VSCode] 音声入力が、CLI と同じく信頼する証明書を絞るよう変更（v2.1.307）
- [VSCode] 拡張機能自身の要求が、CLI と同じく信頼する証明書を絞り、環境かユーザーの設定で名指しした `NODE_EXTRA_CA_CERTS` のファイルを信頼するよう変更（v2.1.307）
- 解析できないツールの呼び出しからの回復を改善。ターンをエラーで終える前に最大 2 回呼び出しをやり直します（v2.1.307。詳細はハイライト 1 参照）
- 一緒に起動したフォークのサブエージェントを改善。それぞれがどの起動が自分のものかを知らされ、互いの作業を始めようとすることがずっと減ります（v2.1.307）
- ブラウザーでのサインインを改善。アカウントのプロフィールの読み込みを待たず、サインインが終わるとすぐ成功のページが出ます（v2.1.307）
- クラウドとセルフホストのランナーのセッションの Web 検索のエラーを改善。理由付きの 403 で断られた検索は、汎用の「Authentication error」ではなくその理由を示します（v2.1.307）
- デスクトップアプリの MCP サーバーの 1 つが接続できないときの、クラウドのセッションの最初の返答までの時間を改善（v2.1.307）
- 大きな貼り付けた画像や PDF の読み込みを含むトランスクリプトのセッションで、Remote Control の接続の時間を改善（v2.1.307）
- `allowedMcpServers` が、`env` でだけ `${VAR}` を使う `managed-mcp.json` の stdio サーバーを絞らないよう変更。許可リストが外していたサーバーが更新で読み込まれるので、止めたままにするには `deniedMcpServers` を使います（v2.1.305）
- 組織の managed settings が `allowManagedPermissionRulesOnly` を設定しているとき、Claude Desktop がパスで組み込むプラグインが `allowed-tools` を保たないよう変更（v2.1.305）
- `/artifacts` の削除の確認を、1 か Enter で残す・2 で削除・Esc で取り消す形に変更。`y` と `n` では答えられなくなりました（v2.1.305）
- mod のドッキングしたペインを、広い端末から引き継いだ幅も含め、端末の幅の 45% までに保つよう変更（v2.1.305。通常のページには前回から載っていた）
- [VSCode] セッションが時間内に始まらず、どのフックも動いていないときのメッセージを、サインインやネットワークより先に出力のログを示し、原因を挙げる形に変更（v2.1.305）
- [Code Review] 以前のブロッキングの指摘がまだ開いている間は、再レビューが LGTM で始まらないよう変更（v2.1.305）
- `/usage` を改善。各警告がその出どころを名指しする 1 行の修正になり、`f` で修正を適用します。同じ修正が VS Code と `/doctor` にも出ます（v2.1.305。通常のページには前回から載っていた）
- MCP の同意のダイアログを改善。プロンプトのつもりの Enter が Accept と取られにくくなります（v2.1.305）
- mod の `Image` を改善。fullscreen のレンダリングの iTerm2 3.5 以降で、`alt` のテキストだけでなく画像を描きます（v2.1.305。通常のページには前回から載っていた）
- Remote Control: spawn モードのメッセージを改善。`w` を押すと新しいモードがフォルダーに保存されたと示し、保存したモードを使う後の `claude remote-control` の起動はその出どころを示します（v2.1.305。通常のページには前回から載っていた）
- [Cloud sessions] セルフホストの環境の削除を改善。ダイアログとエラーのメッセージが、削除を妨げるものと影響を受けるものを示します（v2.1.305。`cloud-environments` には、Anthropic がホストする環境は削除できずアーカイブするだけで、セルフホストの環境は Owner が管理の設定の **Cloud environments** のページで削除できる、と加わった）
- [Claude Tag] 大きな組織の Claude Tag の管理のページを改善。チャンネルの一覧の読み込み中もプラグイン・スキル・バンドルの編集が動きます（v2.1.305）
- **ゲートウェイの裏の tool search が既定でオンと書き改められた**（`mcp`・`llm-gateway-protocol`・`errors`・`env-vars`・`agent-sdk/tool-search`・`agent-sdk/mcp`・`feature-availability`・`prompt-caching`。詳細はハイライト 2 参照）
- **プロジェクトのクラウドスレッドが読むものが書き改められた**（`claude-projects` ほか 9 ページ。詳細はハイライト 3 参照）
- **skills ディレクトリのプラグインが managed settings で止められる場合が書き分けられた**（`plugins/loading` ほか 8 ページ。詳細はハイライト 5 参照）
- **スキルのフロントマターのフックの上限とロックの節ができた**（`hooks` の新しい h4「Limits on skill hooks」・`hooks-guide`・`debug-your-config`・`skills`）。スキルを呼んだ後にフロントマターのフックが動かず `/hooks` にも出ないなら、`strictPluginOnlyCustomization` のロック（プラグイン・同梱・managed のディレクトリのスキルだけがフックを保つ）か上限を疑います。上限は v2.1.304 以降、スキルの出どころ（プロジェクト・個人のスキルのフォルダー・各プラグイン）ごとにセッションで 1,024 個のフック、matcher の合計 16,384 文字で、デバッグログの `registers none of its hooks` で超えたスキルが分かります。`/hooks` はまだ呼んでいないスキルのフックを示さない、とも `hooks-guide` と `debug-your-config` に加わりました — [English](https://code.claude.com/docs/en/hooks#limits-on-skill-hooks)
- **`defer` で保留したツールの呼び出しと再開のプロンプトの扱いが明記された**（`hooks` の「Defer a tool call for later」・`agent-sdk/python`・`hooks-guide`）。`"defer"` はプロセスを終えるのではなくターンを終える、と言い方が改められ、再開したときにツールがなければ `stop_reason: "tool_deferred_unavailable"` になり、プロンプトを送っていなければ呼び出しは保留のまま、送っていればツールの結果なしで答えて保留した呼び出しを捨てる、と書き分けられました。`agent-sdk/python` の `ResultMessage` の `is_error` は、`subtype="success"` で `True` になる 3 つの場合を `stop_reason`（`"refusal"`・`"tool_deferred_unavailable"`・それ以外）で見分ける形になり、失敗の見分け方も `stop_reason`・`terminal_reason`・`subtype` の順になっています — [日本語](https://code.claude.com/docs/ja/hooks#defer-a-tool-call-for-later) / [English](https://code.claude.com/docs/en/hooks#defer-a-tool-call-for-later)
- **Agent SDK の `Agent` ツールの `run_in_background` を省いたときの既定が明記された**（`agent-sdk/python` の「Agent」）。メインのエージェントの呼び出しは新しいエージェントをバックグラウンドで動かし（結果は `status: "async_launched"`）、サブエージェントの呼び出しはその終わりを待ちます。Python SDK v0.2.169（Claude Code v2.1.302 以降を同梱する最初の版）より前は、サブエージェントが始めたエージェントも既定でバックグラウンドで動いていました
- **Agent SDK の MCP の最初のターンの待ち方が組み直された**（`agent-sdk/mcp` の「Connection timing」・`env-vars`）。h3「Named servers」（`allowedTools` か `permissions.allow` でツールを挙げるとそのサーバーを名指しすることになり、tool search がオンでも最初のターンが最大 2 秒待つ。v2.1.284 より前は効果なし）、「Set the first-turn wait yourself」（`CLAUDE_CODE_MCP_STARTUP_WAIT_MS` を `0` にしても、`permissionPromptToolName` のサーバー・プロセス内の SDK のサーバー・接続中の名指ししたサーバーの 3 つの待ちは残る）、「Make startup wait for servers」に分かれました — [日本語](https://code.claude.com/docs/ja/agent-sdk/mcp#connection-timing) / [English](https://code.claude.com/docs/en/agent-sdk/mcp#connection-timing)
- **Agent SDK の `setMcpServers()` で同名のサーバーの扱いが載った**（`agent-sdk/typescript` の「`McpSetServersResult`」）。`.mcp.json` などのインストールのスコープのサーバーと同じ名前の stdio・HTTP・SSE のサーバーを渡すと、その名前ではアプリのサーバーのツールが使われます。v2.1.305 より前は、プラグインを読み込み直すとアプリのサーバーが切られ、スコープのサーバーがつながることがありました（changelog の v2.1.305 の修正に対応）
- **Agent SDK のサブエージェントのスキルの事前の読み込みの上限が載った**（`agent-sdk/subagents`）。`skills` の一覧の最初の 32 個の異なる名前までを読み込み、`agent_id` はサブエージェントを再開しても変わりません
- **パス固有のルールのパターンの基準のディレクトリが明記された**（`memory` の「Path-specific rules」・`skills`）。プロジェクトのルールは `.claude` フォルダーを含むディレクトリ、ユーザーのルールはセッションの主な作業ディレクトリが基準で、隣の git の worktree のファイルに効かせるには、その worktree で起動するか `/cd` で移ります。スキルの `paths` も Claude の現在の作業ディレクトリが基準で、外のファイル（`/add-dir` で加えた隣の worktree など）には効かない、と `skills` のフロントマターの表とトラブルシューティングに加わりました — [日本語](https://code.claude.com/docs/ja/memory#path-specific-rules) / [English](https://code.claude.com/docs/en/memory#path-specific-rules)
- **組織の managed CLAUDE.md は指針で、ルールの強制には managed settings を使うと明記された**（`memory` の「Deploy organization-wide CLAUDE.md」・`admin-setup`・`large-codebases`）。`claudeMdExcludes` では除外できないものの、CLAUDE.md の読み込みを丸ごとオフにして始めたセッションは managed の内容も読まないので、`permissions.deny` などの managed settings でルールを強制します。`admin-setup` の表も「除外できない組織全体の指示」から「クライアントが強制するルールではなく Claude への振る舞いの指針」に改められました — [日本語](https://code.claude.com/docs/ja/memory#deploy-organization-wide-claude-md) / [English](https://code.claude.com/docs/en/memory#deploy-organization-wide-claude-md)
- **`@` で参照したファイルの取り込みでは `PreToolUse` フックが動かないと明記された**（`common-workflows` の「Reference files and directories」）。ツールの呼び出しがないためで、フックで読むものを管理しているなら、`Read` の deny ルールで特定のパスを止めるか、`CLAUDE_CODE_DISABLE_FILE_MENTIONS=1` で `@` の取り込みをやめます（この変数は managed settings の `env` でも設定できる、と加わった） — [日本語](https://code.claude.com/docs/ja/common-workflows#reference-files-and-directories) / [English](https://code.claude.com/docs/en/common-workflows#reference-files-and-directories)
- **シンボリックリンクを経由する添付への `Read` の deny ルールの効き方が載った**（`permissions` の新しい h5「Attachments through a symlink」）。`@` のメンション・ターミナルに貼るかドラッグした画像のパス・ディスクで変わって読み直すファイル・IDE が共有する文脈も、名前のパスと解決先の両方で照らし、一致すれば会話から外します。パスを調べきれない `@` のメンションは `Referenced <path> (not read: could not be examined)` になります。同じページには、`find` の `-rm` も prefix のルールで承認されないこと、`mcp__reports__v2` のような名前が deny と ask のルールでは `reports__v2` のサーバーのすべてのツールにもかかること、Windows で後から `/add-dir` で加えたドライブの読み取りは確認が残ることも加わりました — [日本語](https://code.claude.com/docs/ja/permissions#attachments-through-a-symlink) / [English](https://code.claude.com/docs/en/permissions#attachments-through-a-symlink)
- **名前に `__` を含む MCP サーバーのサブエージェントでの書き方が載った**（`sub-agents` の新しい h5「MCP server names that contain a double underscore」）。`tools` には `mcp__reports__v2__*` のようにサーバーの名前全体と `__*` を書き、`disallowedTools` の `mcp__reports` か `mcp__reports__*` は `reports__v2` のツールも外すので、`reports` だけを外すならツールを 1 つずつ挙げます。サブエージェントの名前は、エージェントチームを有効にして始めたセッションで Claude が付ける、と改められ、v2.1.304 より前は終わった直後に送ったか再開したサブエージェントが最近の作業を忘れることがあった、という注記も加わっています — [日本語](https://code.claude.com/docs/ja/sub-agents#mcp-server-names-that-contain-a-double-underscore) / [English](https://code.claude.com/docs/en/sub-agents#mcp-server-names-that-contain-a-double-underscore)
- **エージェントビューの `--bg` を含むプロンプトとバックグラウンドへの移行の間の入力の扱いが載った**（`agent-view`）。`--bg` か `--background` を含むプロンプトや `--bg` という返信はそのまま届き、Claude Code はフラグが立てる位置（素の `--` の前で、ほかのフラグの値でない所）でだけフラグと読み、曖昧な位置なら `Couldn't tell whether --bg is a flag or text here` で何も始めません（v2.1.299）。セッションがバックグラウンドに移る瞬間に入れたプロンプトや `!` のコマンドは止まるか送られず、テキストはプロンプトの履歴に残るので、開いて `↑` で戻せます（v2.1.296）。バージョン履歴には v2.1.299・v2.1.296 の行と、v2.1.295 の 3 行（アタッチ中の `Ctrl+C` と自分のペースの `/loop`、スーパーバイザーがないときの `claude agents` の終了、macOS のネイティブのインストーラーでの更新後の保護フォルダーのアクセス）が加わりました。ディスパッチの入力は `/effort ultracode` を受け付けず `claude agents --effort ultracode` で開く、文字を選んでいるときの `Ctrl+C` は選択を消す、とも加わっています — [日本語](https://code.claude.com/docs/ja/agent-view#switch-sessions-without-leaving-the-terminal) / [English](https://code.claude.com/docs/en/agent-view#switch-sessions-without-leaving-the-terminal)
- **エージェントチームの計画の承認が、途中で plan モードにしたチームメイトではリードのレビューになると載った**（`agent-teams` の「Have teammates plan before implementing」）。起動の後に権限モードを変えていなければ計画はすぐ承認されますが、動いているプロセス内のチームメイトをそのセッションを見ながら `Shift+Tab` で plan モードにすると、その回の計画はリードがレビューして承認するか差し戻します — [日本語](https://code.claude.com/docs/ja/agent-teams#have-teammates-plan-before-implementing) / [English](https://code.claude.com/docs/en/agent-teams#have-teammates-plan-before-implementing)
- **Enterprise のカスタムのロールで要る権限が載った**（`remote-control`・`routines`・`claude-code-on-the-web`）。カスタムのロールでアクセスを管理する組織では、クラウドのセッションにはクラウドのセッションの権限が、Remote Control にはそれと **Claude Code remote control** の権限の両方が、cloud scheduled tasks には **Remote sessions** の scheduled tasks の権限が要り、Owner が **Organization settings > Roles** で加えます。`remote-control` の `DISABLE_TELEMETRY`・`DO_NOT_TRACK` の要件には、Claude Desktop のアプリでは v2.1.304 以降、と加わりました — [日本語](https://code.claude.com/docs/ja/remote-control#requirements) / [English](https://code.claude.com/docs/en/remote-control#requirements)
- **PowerShell の検索と `git diff` の終了コード 1 の節ができた**（`tools-reference` の新しい h3「Exit code 1 from searches and `git diff` in PowerShell」・`skills`）。一致のない `grep` か `rg` が長いコマンドの一部だと `Error: Exit code 1` が出ることがあり（`rg foo | Out-Null` では出て `rg foo` では出ない）、検索は失敗していないので何もしなくてよい、と説明しています。`where.exe`・`fc.exe`・`diff.exe` と `robocopy` の 1〜7 の終了コードも同じ扱いです — [日本語](https://code.claude.com/docs/ja/tools-reference#exit-code-1-from-searches-and-git-diff-in-powershell) / [English](https://code.claude.com/docs/en/tools-reference#exit-code-1-from-searches-and-git-diff-in-powershell)
- **セルフホストの spawn-runner フックで投入のコマンドに `|| true` を付けないよう明記された**（`self-hosted-environments-configuration` の「The spawn-runner hook」）。付けるとプラットフォームが投入を断ってもフックが 0 で終わり、セッションが始まらないランナーを待ち続けます。ワークロードの名前を `CLAUDE_RUNNER_ORDER_ID` にし、already-exists の答えだけを成功とする `kubectl create` の例が載りました。checkout フックの stderr の終わり約 4 KB に `couldn't find remote ref` があるとランナーは消えたブランチと報告すること、`CLAUDE_RUNNER_ACCOUNT_ID` を重複の除去の鍵に使わないことも加わっています — [日本語](https://code.claude.com/docs/ja/self-hosted-environments-configuration#the-spawn-runner-hook) / [English](https://code.claude.com/docs/en/self-hosted-environments-configuration#the-spawn-runner-hook)
- **セルフホストの `no longer exists on the remote` の調べ方が載った**（`self-hosted-environments-deploy` のトラブルシューティング）。ランナーは git の `couldn't find remote ref` を消えたブランチと読むので、ブランチがまだあることもあります。消えていれば戻し、あるなら checkout フックの git のコマンド、`--git-host-rewrite` の書き換え先、v2.1.301 より古いランナー（ほかの失敗も消えたブランチと報告した）を確かめます — [English](https://code.claude.com/docs/en/self-hosted-environments-deploy#no-longer-exists-on-the-remote)
- **サーバー管理設定の承認のダイアログを出せない `claude plugin` の場合が載った**（`server-managed-settings`・`errors`）。端末に出力してもキーボードから読めない `claude plugin` のコマンドは、配信された設定を適用せず、キャッシュがなければプラグインやマーケットプレイスを変えるコマンドはエラーで止まり、あれば最後に承認した設定で動きます（詳細は大幅更新 1）。承認なしで適用する `env` の変数から `CLAUDE_CODE_DISABLE_1M_CONTEXT` が除かれ、対話的なセッションではプロキシ・ベース URL の変数や `OTEL_EXPORTER_OTLP_ENDPOINT` と同じく、空でない値で必ず承認が要る、と加わりました
- **イベントのウォッチドッグがゲートウェイの ping で延びる時間が明記された**（`network-config` の「Streaming idle watchdogs」）。バイトが 10 秒以内ごとに届けば約 5 分、Claude apps gateway の 15 秒ごとの ping では約 7.5 分で、ping だけのストリームは既定のタイムアウトで約 12.5 分で終わります（詳細は大幅更新 2） — [English](https://code.claude.com/docs/en/network-config#streaming-idle-watchdogs)
- **ゲートウェイの拒否の後の再試行の一覧が書き直された**（`llm-gateway-protocol` の「Automatic retry and error forwarding」）。`thinking.type` の `enabled` か `adaptive` を受け付けない `400` には、もう一方の種類で 1 回送り直して Claude Code が終わるまで保ち（v2.1.121 より前は再試行しなかった）、会話の途中の `role: "system"` が拒まれれば、その内容をユーザーのメッセージに入れて送り直し、`/clear` か圧縮まで保ち、その `cache_control` だけが拒まれればシステムのメッセージを残して印を動かす、と 3 つに分かれました。Claude apps gateway の列の 1 時間の TTL も「beta の値なしの `ttl` のフィールド」に改められています — [日本語](https://code.claude.com/docs/ja/llm-gateway-protocol#automatic-retry-and-error-forwarding) / [English](https://code.claude.com/docs/en/llm-gateway-protocol#automatic-retry-and-error-forwarding)
- **圧縮の後のキャッシュの説明が組み直された**（`prompt-caching` の「Compacting the conversation」）。システムプロンプトの層は（古いシステムプロンプトを保った再開の会話を除き）キャッシュから読まれ、プロジェクトの文脈の層は CLAUDE.md と記憶が変わっていなければ読まれる、と箇条書きになりました。ゲートウェイが `cache_control` を拒んだときに動かした印を保つ期間は「会話の残り」から「Claude Code が終わるまで」に改められています
- **そのほかの明確化**: `model-config` の組織の effort の上限（上限を超える `--effort` の警告が stderr に出るのはテキストの `--print` の実行だけで、ほかはデバッグログ）、`advisor`（メインのモデルより下位のアドバイザーを渡すと、バックグラウンドかにかかわらずセッションは始まり、メインのモデルはアドバイザーなしで動く）、`env-vars` の `CLAUDE_CODE_TRANSCRIPT_LOCAL_GC`（v2.1.296 以降は 10% 未満しか縮まないならファイルを触らない）と `CLAUDE_CODE_MCP_STARTUP_WAIT_MS`、`vs-code`（Claude が送ったファイルの行は Focus view でも残り（v2.1.295 以降）、ネットワークのホストを名指すパスはクリックできない）、`worktrees`（worktree が自分のものでないブランチ（作成時のコミットより先のコミットがあるもの）にいるときも終了時に確認が出て、どちらを選んでもそのブランチは残る）、`fullscreen`（`--chrome`・`--no-chrome` も開き直したセッションに引き継ぐ）、`plugins/mods/interface`（入力欄の `value` は初めのテキストで、同じ値を渡し続ければ入力中のテキストは保たれる）、`plugins/mods/troubleshoot`（新しい h3「`the parser stopped` or `the engine ran out of stack loading the file`」と、`; the version loaded before is unloaded` で終わる理由なら `/reload-plugins` で読み込み直す）、`plugins/components`（256 文字を超える `name` は無視してファイルの名前にする）、`monitoring-usage`（`has_hooks` は mod も数える）、`costs`（フックの例が `permissionDecision: "allow"` を返さず、より厳しいパターンで照合する形に改められた）、`code-review-pull-requests`（`@claude review stop` は動いているレビューを取り消さない。「待ち行列の」の語が外れた）、`desktop-quickstart`（Code タブの位置とアップグレード・サインイン・403 の対処が箇条書きに）、`llm-gateway-connect`（`400` の行から `errors` の「Extra inputs are not permitted」へ案内）などです

**バグ修正**

- `CLAUDE_CODE_DISABLE_1M_CONTEXT` を設定し、モデルが `opus[1m]` のような `[1m]` 付きの別名のとき、要求がモデルの見つからないエラーで失敗する問題を修正（v2.1.307）
- 効果のないカスタムの `ANTHROPIC_BASE_URL` のゲートウェイの裏と Foundry で、`prompt-caching-scope` の beta ヘッダーが送られる問題を修正（v2.1.307）
- macOS でログインのキーチェーンがロックされている間、`claude -p` で MCP サーバーが「needs authentication」と出る問題を修正。理由を示し、ロックを解いた後の次の実行は新しいサインインなしで接続します（v2.1.307）
- 接続中に macOS か Linux のコンピューターがスリープすると、MCP サーバーがタイムアウトと報告され、ヘッドレスの実行では失敗のままになる問題を修正（v2.1.307）
- 呼び出しの途中で接続が閉じると、HTTP の MCP のツールの呼び出しが 2 回送られる問題を修正。再試行するのは読み取り専用か冪等なツールだけになります（v2.1.307）
- バックグラウンドのタスクが動いていると、SDK の MCP サーバーの最新のツールなしでターンが始まることがある問題を修正（v2.1.307）
- 多くの PDF のページ・画像などの大きなツールの結果を読むターンで「Autocompact is thrashing」のエラーが出る場合の一部を修正（v2.1.307）
- クラウドのセッションの `/autocompact` が、セッションの再起動の後に既定のウィンドウに戻る問題を修正（v2.1.307）
- クラウドかセルフホストのランナーのセッションが再起動すると、`/clear` で消した会話が戻ることがある問題を修正（v2.1.307）
- Claude apps gateway のセッションで `CLAUDE_STREAM_FIRST_BYTE_TIMEOUT_MS` が無視される問題を修正（v2.1.307）
- `OTEL_EXPORTER_OTLP_HEADERS` を設定すると、Claude apps gateway の裏の Claude Desktop のセッションのテレメトリが拒まれる問題を修正（v2.1.307）
- `/permissions` の Recently denied が断られたシェルのコマンドを示さず、auto モードのローカルの分類器が再試行されたコマンドを確かめるときにそこからの承認を無視する問題を修正。行を承認すると、説明ではなくコマンドを名指しします（v2.1.307。`auto-mode-config` にも、リストで強調した Bash か PowerShell の操作のコマンドがリストの下に出る、と載った）
- `/help` と `/` のコマンドメニューが、`/claude-api` などの同梱のスキルについて、短い説明ではなくモデル向けの長い説明を示す問題を修正（v2.1.307）
- ストリーミングの応答で、サブエージェントのトランスクリプトに仮のトークンの使用量と空の停止理由が記録される問題を修正（v2.1.307）
- API がモデルの確認に 5 秒より長くかかると、Agent SDK の `setModel()` とその上に作ったアプリでのモデルの切り替えが断られる問題を修正。15 秒まで待ちます（v2.1.307）
- 接続したアプリ（アイドルのセッションをアーカイブするデスクトップアプリなど）が止めたバックグラウンドのコマンドが、ユーザーが止めたと Claude に報告される問題を修正。通知はその出力ファイルを名指しします（v2.1.307）
- Cowork のクラウドのセッションの WebFetch が、サイトが 4xx の状態か robots.txt の拒否で答えるとツールのエラーと報告する問題を修正。ローカルのセッションと同じく通常の結果になります（v2.1.307）
- 直接設定した GitHub の MCP サーバーの書き込みのツールで、デスクトップアプリの Code タブに何も作らずに閉じるフォームが出る問題を修正（v2.1.307）
- サーバーが再利用した接続を閉じていると、Artifact ツールの読み取りが接続のリセットで失敗する問題を修正（v2.1.307）
- セルフホストのランナー: `--use-anthropic-git-proxy` のセッションが、前のセッションがクローンに残した `.claude/settings.local.json` をコミットする問題を修正（v2.1.307）
- セルフホストのランナー: checkout フックの間にセッションをアーカイブするか並べ直すか、ランナーを止めると、フックのプロセスが動いたままでランナーの枠も握られたままになる問題を修正（v2.1.307）
- [VSCode] Show more で展開した長いプロンプトがチャットのパネル全体を覆う問題を修正。固定したプロンプトはパネルの 40% までになりスクロールします（v2.1.307）
- [VSCode] LaTeX の数式を含むリストの項目や表のセルの一部が、リッチテキストのエディターに新しいリストや表として貼られる問題を修正（v2.1.307）
- [VSCode] `NODE_EXTRA_CA_CERTS` を `~/.claude/settings.json` にだけ設定すると、TLS を検査するプロキシの裏で音声入力が失敗する問題を修正。`CLAUDE_CODE_CERT_STORE` にも従います（v2.1.307）
- [Cloud sessions] 検索がまだ動いている間、リポジトリのピッカーが「No repositories match」と出る問題を修正。結果が届くまで「Searching…」を示します（v2.1.307）
- [Cloud sessions] セルフホストの環境で「Waiting for a runner」の状態が切れて表示される問題を修正。オンデマンドのランナーでは最後のメッセージから時間を数え上げ、失敗した試行を示します（v2.1.307）
- セッションの環境変数なしで起動すると、クラウドのセッションの中の `claude -p` が「Not logged in」と報告する問題を修正（v2.1.306）
- 多くの MCP のツールを持つセッションで、API のエラーが「prompt is too long」に置き換わり、要らない圧縮が起こる問題を修正（v2.1.306。`errors` の「Prompt is too long」にも載った）
- エンドポイントかゲートウェイが tool search を拒むときや、ToolSearch を禁じたか `--tools` から外したゲートウェイの裏で、Vertex・Bedrock などでどの要求も失敗する問題を修正（v2.1.304 での後退）。tool search なしで再試行します（v2.1.305。詳細はハイライト 2 参照）
- モデルの名前が `modelOverrides` の値と大文字・小文字か `[1m]` のタグだけ違うと、`/effort` と `/autocompact` の設定が効かない問題を修正（v2.1.305）
- ベアリポジトリの新しい worktree が既定のブランチではなくローカルの HEAD から始まることがある問題と、変更のないサブエージェントの worktree が片付けられないことがある問題を修正（v2.1.305）
- 空きのないディスクで Bash のコマンドが生の `ENOSPC` のファイルパスで失敗する問題を修正。ディスクがいっぱいで何も動かなかったと示します（v2.1.305。詳細は大幅更新 1 参照）
- クラウドのセッションか SDK の `setMcpServers` が渡した MCP サーバーが、セッションの後半に自分の設定の同名のサーバーに置き換わる問題を修正（v2.1.305。`agent-sdk/typescript` にも載った）
- サブエージェントがフォールバックのモデルに切り替わった後、Claude がサブエージェントの作業のモデルを誤って名指しする問題を修正（v2.1.305）
- 圧縮が要約に収めるため最も古いメッセージを外したとき、クラウドのセッションとチームメイトがそれを Claude に伝えない問題を修正（v2.1.305）
- URL の承認をだれも与えられない WebFetch を使うサブエージェントごとに、スケジュールされた Cowork のクラウドのセッションが 5 分待つ場合をさらに修正（v2.1.305）
- Workflow の再開で、完了済みの `pipeline()` と `parallel()` のエージェントを実行のジャーナルから出さずに動かし直す問題を修正（v2.1.305。通常のページには前回から載っていた）
- `/resume` で会話を切り替えた後、Remote Control が `/resume` に空の「(session)」の項目を残す問題を修正（v2.1.305）
- 狭い端末で `/usage` の行が切れる問題を修正（v2.1.305）
- 起動時の警告がロゴの上に生のテキストで出る問題を修正。デバッグログに送り、何も制限しない権限のルールはバナーの下の警告の行で示します（v2.1.305。詳細は大幅更新 1 参照）
- スクリーンリーダーのモードを修正。検索ボックスが、VoiceOver が「telephone recorder」と読む記号ではなく「Search:」と読まれ、Ctrl+R の検索の一致や「ultrathink」のような強調されたプロンプトのテキストの単語の中に空白が入らなくなります（v2.1.305）
- セルフホストのランナー: `TERM` を設定していると、標準出力だけをランナーかオーケストレーターと共有する起動スクリプトが `Resource temporarily unavailable` で失敗する問題を修正（v2.1.300 での後退。v2.1.305）
- セルフホストのランナー: git の資格情報ヘルパーか askpass のプログラムが `GIT_CONFIG` から設定を読むと、v2.1.296 からリポジトリへのアクセスが失敗していた問題を修正（v2.1.305）
- セルフホストのランナー: バックグラウンドで始めたランナーが出力を開いたままにすると、オーケストレーターが spawn-runner フックをタイムアウトと報告する問題を修正（v2.1.305。通常のページには前回から載っていた）
- [VSCode] `spinnerVerbs` の設定が組み込みの動詞を短いものに置き換えると、スピナーが「Compacting...」を切る問題を修正（v2.1.305）
- [Cloud sessions] Cloud environments の管理のページが、既存の環境の保存を「installs packages」のエラーで誤って断る問題を修正（v2.1.305）
- [Claude Tag] 別の GitHub のアカウントに移ったリポジトリを、Claude Tag のアクセスのバンドルに加え直せるよう修正（v2.1.305）
- [Claude Tag] Slack の DM のスレッドで設定したルーティンが、同じスレッドの別のルーティンが会話をやり直した後に投稿しなくなる問題を修正。両方が投稿し続けます（v2.1.305）
- [Claude Tag] Slack のスレッドで設定したルーティンが、会話が終わった後に投稿せずに成功と報告する問題を修正。その実行は飛ばされ、作成者に伝えられます（v2.1.305）
- [Code Review] レビュー中にプルリクエストへ複数のプッシュがあると、Code Review が最新のコミットをレビューしないことがある問題を修正（v2.1.305）
- v2.1.299 より前に、別の Claude Code のセッションが直前に claude.ai から同期したプラグインを更新してファイルを動かすと、起動時に `synced[0]` のような札の行でパスのエラーが出た問題（changelog の項目ではなく、`plugins/troubleshooting` に加わった注記。再起動で読み込める）

**その他**

- **`claude-security` から、プラグインは管理された製品が届かないコード（GitLab・Bitbucket のリポジトリや受信の接続を許さないネットワーク）にも届く、という文が外れた**
- **単独の Claude Design のサイトが 2026年12月14日までに閉じると載った**（`commands` の `/design-login`・`/design-sync`）。どちらも単独の claude.ai/design のためのもので、移行のサポート記事へのリンクが付きました
- **`~/.claude.json` が保つものの呼び方が「アカウントの詳細」に改められた**（`claude-directory`・`devcontainer`・`errors`・`settings`。これまでは OAuth・認証・サインインのセッション・ログインなど）
- **「Cowork tab」が「Cowork」に改められた**（`desktop`・`desktop-linux`・`managed-settings`・`permission-modes`・`server-managed-settings`）
- **`setup` のコードフェンスの ` theme={null}` の繰り返しが 1 回に戻った**（前回の書式の変換の崩れが直り、5 つのフェンスで計 10 行が変わった）
- **言い回しの調整**: `features-overview` と `agent-teams` の名前を付けたサブエージェントへのリンク先が `sub-agents#subagent-names` に、`cross-session-messaging` の `hold` の設定のメッセージの届け方（「accept が後で効くときだけ」から「効くとき」へ）、`plugins/create` の「every session」から「across sessions」への言い換えなどです
- **見出しマップ**: 44 行が加わり 1 行が外れました。加わったのは 43 見出しと新しいスタンプで、43 見出しはすべて今回の `llms-full.txt` にも入っています（見出しマップにだけ先に載った見出しは今回ありません）。外れたのは古いスタンプです。前回、見出しマップにだけ載っていた 11 見出し（「Include other files in REVIEW.md」「Tool search through an LLM gateway」「Couldn't start the local listener that receives the browser sign-in」「Only a teammate can approve a shutdown request」「Matches no tool · check for typos」「Beta header and body field pairs」「Retry without tool search」「Bypass permissions ignored in a background session」「Denied paths that pass through a symlink」「Fork a complete project」「Recognize the StructuredOutput tool call」）は、今回すべて `llms-full.txt` に入りました。`llms-full.txt` に加わった 54 見出しは、この 11 と見出しマップに加わった 43 の合計です
- **見出しマップ冒頭の自動生成スタンプが、2026年10月21日 05時26分28秒 UTC から 2026年10月22日 00時45分00秒 UTC へ進みました**

**参考リンクについて**: 日本語版は、ハイライト・大幅更新・軽微な更新で取り上げたページのうち次の 48 ページ（`skills`・`errors`・`mcp`・`llm-gateway-protocol`・`agent-sdk/tool-search`・`agent-sdk/mcp`・`network-config`・`claude-apps-gateway-deploy`・`claude-apps-gateway-config`・`claude-apps-gateway-on-aws`・`claude-apps-gateway-spend-limits`・`claude-projects`・`settings`・`cloud-environments`・`sandboxing`・`settings-reference`・`plugins/loading`・`plugins/org`・`permission-modes`・`desktop`・`desktop-scheduled-tasks`・`routines`・`agent-view`・`authentication`・`code-review-customize`・`code-review-troubleshooting`・`agent-sdk/structured-outputs`・`agent-sdk/typescript`・`agent-sdk/examples`・`agent-sdk/python`・`hooks`・`keybindings`・`interactive-mode`・`scheduled-tasks`・`tools-reference`・`sub-agents`・`permissions`・`artifacts`・`plugins/mods/api`・`memory`・`agent-teams`・`remote-control`・`self-hosted-environments-deploy`・`self-hosted-environments-configuration`・`devcontainer`・`common-workflows`・`worktrees`・`vs-code`）を取得し、該当する節があるかと今回の内容になっているかを、計 80 項目について確かめました。今回は日本語版の追従にばらつきがあり、ハイライト 2・3 の節や `agent-sdk` の新しい節の多くはすでに今回の内容でしたが、次の節は日本語版にまだないか旧い記述のままだったため、英語版だけにリンクしています。`errors` の「Automatic retries」（ツールの呼び出しの再試行がない）、`sandboxing` の「Chromium or rootless Podman fails inside the sandbox on Linux」、`settings-reference` の `sandbox.allowNestedUserNamespaces`・`strictPluginOnlyCustomization`・`agentPushNotifEnabled`、`plugins/loading` の「Skills-directory plugins blocked by managed settings」、`plugins/org` の「Keep skills-directory plugins loading」、`claude-apps-gateway-deploy`・`claude-apps-gateway-config`・`claude-apps-gateway-on-aws`・`claude-apps-gateway-spend-limits` の新しい節、`permission-modes` の「Critical paths」、`mcp` の「Read a background command's output as an MCP client」「Sign in to an MCP server behind a gateway that requires a header」、`desktop` の「Start a task that Claude suggests」「Work in parallel with sessions」、`authentication` の「Login prompt still appears after an earlier sign-in」、`hooks` の「Limits on skill hooks」、`network-config` の「Streaming idle watchdogs」、`self-hosted-environments-deploy` のトラブルシューティングです。取得して確かめていないページ（`commands`・`env-vars`・`feature-availability`・`prompt-caching`・`monitoring-usage`・`plugins/mods/reference`・`plugins/mods/troubleshoot`・`plugins/cli-reference`・`plugins/create`・`plugins/publish`・`managed-mcp`・`server-managed-settings`・`model-config`・`advisor` など）と、changelog だけに載っていて対応する節のない項目にはリンクを付けていません。**changelog ページへのリンクは、本サマリの方針どおり付けていません。**
<!-- light:minor-updates:end -->

## 新着情報

<!-- light:whats-new:start -->
**今回、`whats-new/` 配下のページに変更はありません**（最新は前回と同じ Week 37）。
<!-- light:whats-new:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-10-20.md](./archives/latest/2026-10-20.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-10-20.md](./archives/latest-detail/2026-10-20.md)

<!--
base_commit: 9a810fc542230f7d1d5e0e958b239a460a6d260f
head_commit: 90e33ad9b987f232e063b09e44406cfc307abd87
generated_at_full: 2026-10-22T15:16:36+09:00
-->
