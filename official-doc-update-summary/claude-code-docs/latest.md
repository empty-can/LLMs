---
対象期間: 2026年10月03日 〜 2026年10月04日
作成日: 2026-10-04
---

# Claude Code 公式ドキュメント更新サマリ

```markdown
**今回は changelog に新しいリリースはなく、v2.1.283〜v2.1.289 の変更をドキュメントが追いかけた回です**。Bash の拒否ルールと PowerShell ツールの関係や、サブプロセスの環境から消える認証情報の範囲など、権限と認証情報まわりの説明が具体的になりました。ページ単位で数えると 220 ページ中 53 ページが変わり、変更は 805 行（追加 590・削除 215）です。総行数は 111,638 行から 112,013 行に増えました。

主要なものを以下に挙げます。

1. Bash を拒否すると PowerShell ツールも止まることが明記され、警告も出るようになった
2. サブプロセスの環境のスクラブが消すものと残すものが表になった
3. Claude apps gateway が Amazon Bedrock の Mantle エンドポイントを上流に使えるようになった
4. モデルの許可リストの強制が Bedrock と Agent Platform の起動時のモデル確認にも効くようになった
5. MCP のツール結果に 50,000 文字の退避基準と、エラー結果の切り詰めが載った
```

## ハイライト

1. [**Bash を拒否すると PowerShell ツールも止まることが明記され警告も出るようになった**](./latest-detail.md#1-bash-を拒否すると-powershell-ツールも止まることが明記され警告も出るようになった):  
  Windows で Git Bash がある場合、Bash の拒否ルールは範囲を絞ったものでも PowerShell ツールを止めます。Bash ツールごと外したときは、v2.1.287 以降は起動時に警告が出ます
2. [**サブプロセスの環境のスクラブが消すものと残すものが表になった**](./latest-detail.md#2-サブプロセスの環境のスクラブが消すものと残すものが表になった):  
  `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB=1` は変数名か値の形で認証情報を見分けて消します。一方、`GITHUB_TOKEN` などの GitHub のトークンとプロキシの設定は残すことが表で示されました
3. [**Claude apps gateway が Amazon Bedrock の Mantle エンドポイントを上流に使えるようになった**](./latest-detail.md#3-claude-apps-gateway-が-amazon-bedrock-の-mantle-エンドポイントを上流に使えるようになった):  
  `provider: mantle` の上流が加わりました（ゲートウェイサーバーで v2.1.283 以降）。`models` に挙げたモデルだけが Mantle に送られ、Bedrock の上流の `guardrail` と `assume_role` は適用されません
4. [**モデルの許可リストの強制が Bedrock と Agent Platform の起動時のモデル確認にも効くようになった**](./latest-detail.md#4-モデルの許可リストの強制が-bedrock-と-agent-platform-の起動時のモデル確認にも効くようになった):  
  管理設定で `enforceAvailableModels` を設定すると、起動時のモデルの確認は `availableModels` が許すモデルだけを使います（v2.1.287 以降）。ゲートウェイでも、既定のモデルが一覧にないと `400` になる問題への対処が節になりました
5. [**MCP のツール結果に 50,000 文字の退避基準とエラー結果の切り詰めが載った**](./latest-detail.md#5-mcp-のツール結果に-50000-文字の退避基準とエラー結果の切り詰めが載った):  
  成功したテキストの結果は、トークン数に関係なく 50,000 文字を超えるとファイルに退避されます。`isError: true` の結果は約 11,000 文字を超えると先頭と末尾の 5,000 文字ずつに切り詰められます

## 新規追加されたページ

*(今回の対象期間に新規追加されたページはありません)*

## 大幅に更新されたページ

- [**Use Claude Code in the cloud**](./latest-detail.md#1-use-claude-code-in-the-cloud) ([日本語](https://code.claude.com/docs/ja/claude-code-on-the-web#quick-setup-for-team-and-enterprise) / [English](https://code.claude.com/docs/en/claude-code-on-the-web#quick-setup-for-team-and-enterprise)):  
  152 行（追加 94・削除 58）が変わりました。大半は節の分割・移動と箇条書き化で、「Quick setup for Team and Enterprise」と「Errors when sending to a cloud session」が独立しました
- [**Claude apps gateway configuration**](./latest-detail.md#2-claude-apps-gateway-configuration) ([日本語](https://code.claude.com/docs/ja/claude-apps-gateway-config#start-sessions-on-a-model-the-policy-allows) / [English](https://code.claude.com/docs/en/claude-apps-gateway-config#start-sessions-on-a-model-the-policy-allows)):  
  86 行（追加 78・削除 8）が変わりました。Mantle の上流（ハイライト 3）と、ポリシーが許すモデルでセッションを始める節が加わりました
- [**Control MCP server access for your organization**](./latest-detail.md#3-control-mcp-server-access-for-your-organization) ([日本語](https://code.claude.com/docs/ja/managed-mcp#servers-that-skip-the-allowlist-check) / [English](https://code.claude.com/docs/en/managed-mcp#servers-that-skip-the-allowlist-check)):  
  84 行（追加 53・削除 31）が変わりました。照合の規則がエントリの種類ごとの小節に分かれ、`serverCommand` は `env` ブロックを比べないことが加わりました
- [**Hooks reference**](./latest-detail.md#4-hooks-reference) ([English](https://code.claude.com/docs/en/hooks#tools-that-require-user-interaction)):  
  56 行（追加 45・削除 11）が変わりました。ユーザーの操作が要るツールを `PreToolUse` で答える節と例ができ、Stop フックの連続回数の数え方が加わりました
- [**Environment variables**](./latest-detail.md#5-environment-variables) ([English](https://code.claude.com/docs/en/env-vars#what-the-subprocess-environment-scrub-removes)):  
  51 行（追加 44・削除 7）が変わりました。スクラブの節（ハイライト 2）と 4 つの変数が加わり、1 つが「v2.1.283 で削除」になりました

## 軽微な更新

今回の差分は **3 ファイル**（`llms-full.txt`・`llms.txt`・見出しマップ）です。`llms-full.txt` をページ単位に切り出して数えると、220 ページ中 **53 ページ**が変わり、変更は 805 行（追加 590・削除 215）でした。大幅更新の 5 ページを除く **48 ページ**を以下にまとめます。**changelog に新しいリリースはなく**、各項目の版は本文の「Requires」などの記載から拾っています。`llms-full.txt` の総行数は **111,638 行から 112,013 行へ 375 行増え**ました。

**新機能**

- **セルフホストのランナーで、GitHub CLI のないイメージにも組み込みの `gh` が使えることが載った**（v2.1.287 以降。「GitHub API access without the GitHub CLI」）。Anthropic が管理する git を使うランナー向けで、対応するのは GitHub の REST API を呼ぶ `gh api` だけです。`gh pr create` の代わりに `gh api repos/{owner}/{repo}/pulls -f title='Fix' ...` で PR を開け、資格情報は Anthropic 側で付くのでイメージにトークンは要りません。使えるかはセッションごとに Anthropic が決め、ランナーのログの `gh_path_shim=true` で分かります。`CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` を設定すると提供されず、イメージに GitHub CLI があればそちらを使います — [日本語](https://code.claude.com/docs/ja/self-hosted-environments-deploy#github-api-access-without-the-github-cli) / [English](https://code.claude.com/docs/en/self-hosted-environments-deploy#github-api-access-without-the-github-cli)
- **エージェントビューで、名前でセッションを探す `Ctrl+F` と、グループの見出し間を移る `Alt+↑`・`Alt+↓` が載った**（v2.1.288）。`keybindings` の `Agents` コンテキストにも `agents:find`・`agents:rename`・`agents:previousGroup`・`agents:nextGroup`（v2.1.288 以降）が加わり、`Agents` コンテキストにアクションのあるショートカットは `keybindings.json` に従う、と改められました — [日本語](https://code.claude.com/docs/ja/agent-view#keyboard-shortcuts) / [English](https://code.claude.com/docs/en/agent-view#keyboard-shortcuts)
- **mod に `ui.fault` イベントが加わった**（v2.1.289 以降）。mod が描いた `Client` 要素の読み込み・描画・実行が失敗すると `e.phase`（`load`・`render`・`run`）と `e.reason` 付きで届き、`ui.fault` のフックが返った後に `ui.render` がもう一度呼ばれるので、失敗した `Client` を外して描き直せます（`plugins/mods/interface` にも追記）。リファレンスの対象版は v2.1.289 になり、`$.ui` に `selection` が載り、`agent.spawn` はエージェントチームのチームメイトでも発火して `e.isTeammate` が `true` になります — [English](https://code.claude.com/docs/en/plugins/mods/reference#interface)
- **`claude plugin list --json` に `readFromFolder` と `folderVersion` が加わった**（v2.1.289 以降）。マーケットプレイスのフォルダーからその場で読み込むプラグインのソースのディレクトリと、そこから読み込んだときの `version` を示します（このときの `installPath` は読み込み元ではありません）。`claude plugin validate` は、ディレクトリに `marketplace.json` と `plugin.json` の両方があればプラグインのマニフェストと部品のファイルも検証するようになりました（v2.1.289 以降）
- **OpenTelemetry の `user_prompt` イベントに `prompt_text` が加わった**（v2.1.287 以降）。`prompt` と同じ値で、ドット区切りの属性名を入れ子のオブジェクトとして保存するバックエンドが `prompt.id` のせいでプロンプトの文字列を失う場合に読みます。詳細なベータのトレースで `OTEL_LOG_USER_PROMPTS=1` のときは、完全なシステムプロンプトを運ぶ `claude_code.system_prompt` イベントも出ます（`monitoring-usage`）
- **Agent SDK（TypeScript）で、インプロセスの SDK MCP サーバー向けの機能 `sdk_mcp_manifests` と `sdk_mcp_tools_list_changed` が載った**（v2.1.286 以降で通知）。後者により、サーバーが `tools/list_changed` を送るとツールの一覧を取り直し、途中で加えたツールも Claude に届きます。`initialize` の応答の `sdk_mcp_manifests_parked` もアプリが設定・読み取りするものではない、と加わりました
- **Agent SDK のサブエージェントの `usage` に `fallback_credit` が加わった**（TypeScript SDK v0.3.285・Python SDK v0.2.162 以降、Claude Code v2.1.285 を同梱）。TypeScript の `Usage` の型にも `fallback_credit: BetaFallbackCreditUsage | null` が加わり、`NonNullableUsage` ではこれだけ `null` を許します。`Usage` に含まれるかは、入っている `@anthropic-ai/sdk`（0.115.0 で追加）次第です

**機能改善**

- **詳細なベータのトレースで出る内容の属性が、スパンと必要な変数の表になった**（`monitoring-usage`）。`new_context`（`claude_code.interaction`・`claude_code.llm_request`・`claude_code.tool` で中身と変数が違う）、新しい `system_reminders`、`system_prompt_preview`、`user_system_prompt`、`response.model_output`、`tool_input`（`claude_code.tool`・`OTEL_LOG_TOOL_DETAILS`）が並びます。セキュリティの節には、コレクターで `prompt` と `prompt_text` の両方を消す `attributes` プロセッサーの例と、`response.model_output` は `OTEL_LOG_ASSISTANT_RESPONSES` ではなく `OTEL_LOG_USER_PROMPTS` に従うことが加わりました — [日本語](https://code.claude.com/docs/ja/monitoring-usage#new-context-gates) / [English](https://code.claude.com/docs/en/monitoring-usage#new-context-gates)
- **重要なパスの削除の確認に、`/*` や `/*/` で終わる一部の対象が加わった**（`rm -rf logs/*/*`、`cd logs && rm -rf a/*` など。どのディレクトリに届くか実行前に分からないため）。`-c` で渡すインラインのスクリプトは、`sh`・`bash`・`zsh` など POSIX のシェルで書いた重要なパスの削除そのものも確認の対象と明記され、止めるには `CLAUDE_CODE_DISABLE_INLINE_SHELL_RM_PROMPT=1` を使います — [日本語](https://code.claude.com/docs/ja/permission-modes#removals-inside-nested-commands-and-inline-scripts) / [English](https://code.claude.com/docs/en/permission-modes#removals-inside-nested-commands-and-inline-scripts)
- **保護されたディレクトリの `.claude` の例外に、`--restricted` なしで始めたセッションの自動メモリのディレクトリにある markdown ファイルが加わった**（`permission-modes`）
- **Agent SDK の MCP のトラブルシューティングに「A tool is missing from an SDK MCP server」ができた**。TypeScript SDK で、入力のスキーマを JSON Schema に変換できないツールは `createSdkMcpServer()` のサーバーの一覧から外され、Node.js ではコード `CLAUDE_SDK_MCP_TOOL_SCHEMA_UNCONVERTIBLE` の警告が出ます。TypeScript Agent SDK v0.3.286 より前は、1 つのスキーマのせいでサーバーのツールの一覧全体が失敗していました（`agent-sdk/troubleshooting` の表にも追記） — [English](https://code.claude.com/docs/en/agent-sdk/mcp#a-tool-is-missing-from-an-sdk-mcp-server)
- **管理設定で、埋め込みのホストが渡す `allowedProviders` も扱いが決まった**（v2.1.285 以降）。選ばれた管理ソースの一覧が親の一覧を止め、`managedSourcesBehavior` が `"merge"` ならどの管理ソースの一覧でも止めます。`claude-apps-gateway` の「Settings the locks don't cover」にも同じ項目が加わり、「6 つ」という数が消えました（`managed-settings`）
- **管理設定の `autoCompactWindow` も既定値にすぎない、と加わった**。`--autocompact` フラグと `CLAUDE_CODE_AUTO_COMPACT_WINDOW` は引き続きそのセッションの値を決めます（`managed-settings`）
- **LLM ゲートウェイのプロトコルの「Streaming」の要件が箇条書きに整理された**（`llm-gateway-protocol`）。応答をまとめてから中継すると止まる、最後の `message_delta` の前で本文が終わると接続の切断とみなす、Bedrock のガードレールのイベントはそのまま渡す、`ping` を落とすとストリーミングのアイドルのタイムアウトに当たる、Bedrock の InvokeModel 形式のバイナリの本文を SSE に変えると解析できない、という 5 点です
- **アーティファクトのコメントの監視は、Claude Code が自分で始めたものなら数時間動きがないと終わることがある、と加わった**。再開するにはもう一度公開するか、Claude に監視を頼みます（「セッションが動いている間ずっと」の表現は削除。`artifacts`）
- **`Ctrl+X Ctrl+K` は、バックグラウンドのサブエージェントの権限の確認が開いている間も押せる、と加わった**（`interactive-mode`・`keybindings` の `chat:killAgents`）
- **プロンプトの提案の `Showing fewer prompt suggestions · use one to bring them back` の意味が載った**。使わない提案が続くと頻度を下げ、提案を 1 つ使うか `CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION=true` で戻ります（`interactive-mode`）
- **別のセッションからのメッセージの短い表示を、フルスクリーンではクリックしてその場で広げられるようになった**（`cross-session-messaging`。`fullscreen` からは「別のセッションからの行はクリックできない」が消えた）
- **`best-practices` の、ファイルごとに `claude -p` を回す例に `--permission-mode dontAsk` が加わった**。`--allowedTools` は「制限する」ではなく「事前に許可する」もので、それ以外の承認が要る操作は `dontAsk` が拒否する、と改められています
- **`headless` の bare モードの表で、カスタムエージェントが `--agents <file-or-json>` になった**
- **デスクトップアプリで、表示のモードとクラウドへの移動がセッションのメニューに移ったことが載った**。セッション名の横のキャレットから開くメニューの **Transcript view** で表示のモードを、**Open in** の **Cloud** でセッションをクラウドに移します（会話は要約で引き継ぎ、ファイルも移るか・元のセッションをアーカイブするかを確認画面が示す。SSH と WSL のセッションは不可）。エディターやファイルマネージャーでフォルダーを開くこともできます（`desktop`・`desktop-quickstart`）
- **iOS シミュレーターのペインの映像の調整が **Display** メニューに移った**。**Frame rate** と **Resolution** の説明が残り、**Encoding** と **FPS** の記述は消えました（`desktop-ios-simulator`）

**その他**

- **claude.ai の管理画面の表記が「Admin settings」から「Organization settings」になった**（`admin-setup`・`channels`・`claude-code-on-the-web`・`costs`・`errors`・`fast-mode`・`server-managed-settings`・`web-quickstart`）。`web-quickstart` の GitHub の接続前に出るメッセージも「GitHub access is required for Claude Code cloud sessions」に、トグルの名前も「Quick setup」になり、リンク先は `#quick-setup-for-team-and-enterprise` に替わっています（`cloud-environments` も同様）
- **「ローカルのディレクトリとして追加したマーケットプレイス」が「ローカルのパスから追加したマーケットプレイス」に言い換えられた**（`claude-directory`・`plugins/host-marketplace`・`plugins/loading`・`plugins/manifest-reference`）
- **v2.1.145〜v2.1.193 の版についての「Requires」などの注記が削除された**（`mcp`・`plugins/cli-reference`・`plugins/create`・`plugins/host-marketplace`・`plugins/marketplace-reference`・`settings-reference`）
- **mods のリファレンスの制限の表で、`prompt.edit` のフックの実行時間が 50 ミリ秒、`session.end` のフック全体が SessionEnd フックの予算（既定 1.5 秒、設定の `SessionEnd` フックが終わってから数える）になった**（`plugins/mods/reference`）
- **このほか、`self-hosted-environments-quickstart` の「エラーの一覧は Send follow-ups from the CLI にある」の記述の削除、`model-config` の `MAX_THINKING_TOKENS` の行から「ほかの値は固定の思考予算でだけ効く」が外れたこと、`agent-view` のフィルター中に Enter で開く行が「最初の一致」から「選ばれた一致」になったことなどの言い回しの修正があった**
- **`llms.txt` の日本語版のページ数が 219 から 220 になった**（ほかの言語と揃った）
- **前回までに見出しマップにだけ先に載っていた見出しが、すべて本文に入りました**（`claude-code-on-the-web` の「Quick setup for Team and Enterprise」「Errors when sending to a cloud session」と「Output」への改称・節の並べ替え、`claude-apps-gateway-config` の「Start sessions on a model the policy allows」、`hooks` の 2 見出し）。今回マップに加わった 13 見出しも、すべて本文にあります
- **見出しマップ冒頭の自動生成スタンプが、2026年10月04日 05時16分55秒 UTC から 2026年10月04日 15時59分42秒 UTC へ進みました**

**参考リンクについて**: 日本語版は、`tools-reference`・`errors`・`claude-apps-gateway-config`・`amazon-bedrock`・`google-vertex-ai`・`mcp`・`claude-code-on-the-web`・`managed-mcp`・`monitoring-usage`・`self-hosted-environments-deploy`・`agent-view`・`permission-modes` の 12 ページを実測し、今回の内容に更新されていたためリンクを付けています。**`env-vars` は変数の表は更新済みでしたが、スクラブの節そのものを確かめられず、`hooks` も新しい節を確かめられなかったため、英語版だけにしています。** それ以外のページ（`agent-sdk/mcp`・`plugins/mods/reference` など）も日本語版を確かめていないため、英語版だけです。 **changelog ページへのリンクは、本サマリの方針どおり付けていません。**

## 新着情報

**今回、`whats-new/` 配下のページに変更はありません。**

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-10-03.md](./archives/latest/2026-10-03.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-10-03.md](./archives/latest-detail/2026-10-03.md)

<!--
base_commit: dce38920d12d39a079b4f53b19149f8f3ed45f63
head_commit: 39d4fa8afc2b6111b66fec97040194774d7ecd80
generated_at_full: 2026-10-05T15:06:38+09:00
-->
