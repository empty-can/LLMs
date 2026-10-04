---
対象期間: 2026年10月02日 〜 2026年10月03日
作成日: 2026-10-03
---

# Claude Code 公式ドキュメント更新サマリ

```markdown
**今回はセルフホストのランナーから Amazon Bedrock・Agent Platform へモデルリクエストを送る手順が加わり、Claude apps gateway まわりの記述も大きく増えました**。changelog には v2.1.288（2026年10月02日、89 項目）と v2.1.289（2026年10月03日、27 項目）が積まれています。ページ単位で数えると 220 ページ中 80 ページが変わり、変更は 1,472 行（追加 1,129・削除 343）です。総行数は 110,852 行から 111,638 行に増えました。

主要なものを以下に挙げます。

1. セルフホストのランナーが Bedrock と Agent Platform にモデルリクエストを送れるようになった
2. Claude apps gateway が証明書でのクライアント認証と 1M コンテキストの選択肢に対応した
3. ゲートウェイの支出上限が /usage とステータスラインにドルで表示されるようになった
4. バックグラウンドのコマンドの時間制限が無人のセッションだけになった
5. /diff のパネルとダイアログが組み込みの mod になり、ファイルやターンごとに見られるようになった
```

## ハイライト

1. [**セルフホストのランナーが Bedrock と Agent Platform にモデルリクエストを送れるようになった**](./latest-detail.md#1-セルフホストのランナーが-bedrock-と-agent-platform-にモデルリクエストを送れるようになった):  
  これまで「Anthropic API 以外には送れない」とされていたセルフホスト環境の推論を、ランナーの環境変数で Amazon Bedrock か Google Cloud の Agent Platform に向けられるようになりました。セッションのイベントストリームは引き続き `api.anthropic.com` に送られます
2. [**Claude apps gateway が証明書でのクライアント認証と 1M コンテキストの選択肢に対応した**](./latest-detail.md#2-claude-apps-gateway-が証明書でのクライアント認証と-1m-コンテキストの選択肢に対応した):  
  IdP への認証に `private_key_jwt`（`client_assertion` で秘密鍵と証明書を渡す）が使えるようになりました。Claude Desktop のモデルピッカーの 1M の選択肢と、ターミナルのセッションの 1M コンテキストウィンドウの扱いも節になっています
3. [**ゲートウェイの支出上限が /usage とステータスラインにドルで表示されるようになった**](./latest-detail.md#3-ゲートウェイの支出上限が-usage-とステータスラインにドルで表示されるようになった):  
  開発者のマシンとゲートウェイサーバーの両方が v2.1.284 以降なら、`/usage` の **Spend limit** バーに推定支出と上限が米ドルで出ます。ステータスラインのスクリプトにも `used_usd`・`limit_usd`・`period` が渡ります
4. [**バックグラウンドのコマンドの時間制限が無人のセッションだけになった**](./latest-detail.md#4-バックグラウンドのコマンドの時間制限が無人のセッションだけになった):  
  v2.1.288 以降、バックグラウンドの Bash・PowerShell コマンドの時間制限は `-p`・Agent SDK・CI・クラウドなど無人のセッションでだけ効き、ターミナル・デスクトップアプリ・VS Code のローカルのセッションでは制限がなくなりました
5. [**/diff のパネルとダイアログが組み込みの mod になり、ファイルやターンごとに見られるようになった**](./latest-detail.md#5-diff-のパネルとダイアログが組み込みの-mod-になりファイルやターンごとに見られるようになった):  
  `/diff` が開くパネルとダイアログは組み込みの mod `cc-plugin-diff` が描くようになり、ファイルの差分を次のプロンプトに添付する `ask` と、ターンごとの編集を選ぶ `source` ピッカーが加わりました。クラシックレンダラーの「Diff viewer」は「Diff dialog」に置き換わっています

## 新規追加されたページ

*(今回の対象期間に新規追加されたページはありません)*

## 大幅に更新されたページ

- [**Error reference**](./latest-detail.md#1-error-reference) ([日本語](https://code.claude.com/docs/ja/errors#advisor-is-less-capable-than-the-current-main-model) / [English](https://code.claude.com/docs/en/errors#advisor-is-less-capable-than-the-current-main-model)):  
  184 行（追加 179・削除 5）が変わりました。新しい節が 8 つ加わり、索引の表と再試行の説明が増えました
- [**Claude apps gateway configuration**](./latest-detail.md#2-claude-apps-gateway-configuration) ([日本語](https://code.claude.com/docs/ja/claude-apps-gateway-config#extended-context-in-claude-desktop) / [English](https://code.claude.com/docs/en/claude-apps-gateway-config#extended-context-in-claude-desktop)):  
  123 行（追加 119・削除 4）が変わりました。証明書でのクライアント認証と 1M コンテキストの節が加わりました（ハイライト 2）
- [**Customize sessions in self-hosted environments**](./latest-detail.md#3-customize-sessions-in-self-hosted-environments) ([日本語](https://code.claude.com/docs/ja/self-hosted-environments-configuration#what-differs-from-sessions-on-the-anthropic-api) / [English](https://code.claude.com/docs/en/self-hosted-environments-configuration#what-differs-from-sessions-on-the-anthropic-api)):  
  93 行（追加 91・削除 2）が変わりました。Bedrock・Agent Platform に送る手順の節が加わりました（ハイライト 1）
- [**Agent SDK reference - TypeScript**](./latest-detail.md#4-agent-sdk-reference---typescript) ([日本語](https://code.claude.com/docs/ja/agent-sdk/typescript#sdkusermessage) / [English](https://code.claude.com/docs/en/agent-sdk/typescript#sdkusermessage)):  
  51 行（追加 42・削除 9）が変わりました。`SDKUserMessage` の `priority` と、`tool_use_result` の扱いが加わりました

## 軽微な更新

今回の差分は **2 ファイル**（`llms-full.txt` と見出しマップ。`llms.txt` は変わっていません）です。`llms-full.txt` をページ単位に切り出して数えると、220 ページ中 **80 ページ**が変わり、変更は 1,472 行（追加 1,129・削除 343）でした。大幅更新の 4 ページを除く **76 ページ**（changelog を含む）と、changelog に加わった **v2.1.288**（2026年10月02日、89 項目。Added 7・Fixed 64・Improved 12・Changed 6）と **v2.1.289**（2026年10月03日、27 項目。Fixed 23・Improved 2・Added 1・Reverted 1）を以下にまとめます。`llms-full.txt` の総行数は **110,852 行から 111,638 行へ 786 行増え**ました。

**新機能**

- **mod 向けに `$.ui.selection()` を追加**。フルスクリーンで最後に選択したテキストと、選択が 1 行に収まる場合はその行を返します（v2.1.288）
- **画像に GitHub CLI がないクラウドのセッションに組み込みの `gh api` を追加**。あわせて、ファイル名・jq のフィルター・GitHub のエラーの制御文字を端末に送っていた問題も修正しました（v2.1.288）
- **Ctrl+C で消したプロンプトを、空のプロンプトで Up を押して戻せるようにした**。貼り付けたテキストと画像も戻ります（v2.1.288）
- **MCP サーバーがツール呼び出し中により広い OAuth のスコープを求めたとき、再認証を促すようにした**（v2.1.288）
- **`/code-review` に `--max-findings <n>|all` を追加**。通常の上限より多く・少なく報告し、`--max-findings default` を渡すまで同じ値を使い続けます（v2.1.288） — [日本語](https://code.claude.com/docs/ja/code-review#review-a-diff-locally) / [English](https://code.claude.com/docs/en/code-review#review-a-diff-locally)
- **エージェントビューに、名前でセッションを探す Ctrl+F と、グループ間を移る Alt+↑/↓ を追加**。名前の変更とあわせて `keybindings.json` で割り当て直せます（v2.1.288）
- **スクリーンリーダーモードで、プランを承認したとき（Shift+Tab を含む）に新しい権限モードを読み上げるようにした**（v2.1.288）
- **チームメイト向けの `agent.spawn`、プラグインのフックのイベントをまたぐ 1 つのエージェント ID、`$.agent.list()` のアイドルと待機の状態を追加**（v2.1.289）
- **`CLAUDE_CODE_DISABLE_STRUCTURED_OUTPUTS` が載った**。構造化出力の `output_config.format` とそれに対応する `anthropic-beta` だけを送らないようにし、`CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS` が止めるほかの機能は残します（v2.1.288 以降。`llm-gateway-protocol` にも追記）
- **VS Code 拡張にブックマーク（Bookmark response、`/bookmarks`）が載った**（v2.1.286 以降） — [日本語](https://code.claude.com/docs/ja/vs-code#use-the-prompt-box) / [English](https://code.claude.com/docs/en/vs-code#use-the-prompt-box)
- **VS Code 拡張の設定に `showMessageTimestamps`（各メッセージの送信時刻を表示）が加わった**（v2.1.284 以降） — [日本語](https://code.claude.com/docs/ja/vs-code#extension-settings) / [English](https://code.claude.com/docs/en/vs-code#extension-settings)
- **VS Code のチャットパネルが、組み込みのサーバー `claude-vscode` を通じて Problems パネルの診断を読むことが載った**（v2.1.285 以降）。フックと権限ルールでは `mcp__claude-vscode__getDiagnostics` と見え、CLI の `mcp__ide__getDiagnostics` と両方を名指して拒否する例があります — [日本語](https://code.claude.com/docs/ja/vs-code#the-built-in-ide-mcp-server) / [English](https://code.claude.com/docs/en/vs-code#the-built-in-ide-mcp-server)
- **VS Code でも「Enabled by default」で Chrome に接続できるようになった**（v2.1.287 以降。セッションの開始時にブラウザに接続）。その場合、`@browser` と打つまでは許可していないサイトでのブラウザの操作の前に確認する、という「Permission prompts in VS Code sessions」の節ができました（`settings-reference` の `claudeInChromeDefaultEnabled`・`permission-modes`・`vs-code` にも追記） — [日本語](https://code.claude.com/docs/ja/chrome#permission-prompts-in-vs-code-sessions) / [English](https://code.claude.com/docs/en/chrome#permission-prompts-in-vs-code-sessions)
- **LSP サーバーの `requestTimeout`（既定 60000 ミリ秒）が `plugins/manifest-reference` に載った**（v2.1.288 以降）
- **mod の `tool.describe` が `isDeferred` でツールをツール検索の後ろに回すか最初から読み込むかを決められることが載った**（`plugins/mods/reference`・`agent-sdk/tool-search`）
- **mod のペインと帯のキー操作に、PgUp・PgDn・Home・End でのスクロール、`Ctrl+X` と矢印でのペインの大きさの変更、`Ctrl+X X` での閉じる操作が加わった**。`keybindings` にも `Pane`・`PaneField` のコンテキストと、`ctrl+x` で始まるそれらの既定のコードが加わりました
- **`claude-apps-gateway-deploy` に「Plugin marketplace requests」の節ができた**。公式マーケットプレイスの最初の登録は `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1` では止まらず、`strictKnownMarketplaces`・`blockedMarketplaces` か `CLAUDE_CODE_DISABLE_OFFICIAL_MARKETPLACE_AUTOINSTALL` で止める、と書かれています — [English](https://code.claude.com/docs/en/claude-apps-gateway-deploy#plugin-marketplace-requests)

**機能改善**

- **プラグインのコードのペインで、大きなファイルを開く速さを改善**（v2.1.289）
- **mod の帯やペインが描けなかったとき、作者に見える行で mod の名前と、何も描かれなかったことを示すようにした**（v2.1.289）
- **auto モードで、クライアント側の安全確認の分類器が見るには会話が長すぎる場合、ツール呼び出しのたびに確認・失敗するのではなくコンパクションするようにした**（v2.1.288）
- **スクリーンリーダーモードで、削除した単語のような短い読み上げを、次のキーを押すか上の表示が変わるまで画面に残すようにした**（v2.1.288）
- **スクリーンリーダーモードで、質問のダイアログの回答済みの質問に「answered」と出すようにした**（v2.1.288）
- **組織が使用クレジットの要求を止めている Team・Enterprise のメンバーに出す `/usage-credits` のメッセージを改善**（v2.1.288）
- **クラウドのセッションで、新しい会話の最初のターンが `alwaysLoad: false` の stdio の MCP サーバーを待たないようにした**（v2.1.288）
- **「You should know」の注記で、判断の責任に応じて「we」「the main agent」「you」を使い分けるようにした**（v2.1.288）
- **アーティファクトのデータベースへの書き込みが容量の上限で断られたときのエラーで、上限と空きを作る方法を示すようにした**（v2.1.288）
- **実行前に一部を確認できないコマンドの Bash の権限の確認で、理由を短くした**（v2.1.288）
- **[セルフホストのランナー] 組み込みの `gh api` を改善**。断られた gh のコマンドに対応する `gh api` を表示し、`--paginate` がリポジトリの一覧のすべてのページをたどり、入れ子の `claude` が消さないようにしました（v2.1.288）
- **Remote Control で、サーバーの資格情報が期限切れになったときの回復を改善**。更新中も接続を保ち、サーバーの障害で諦めた場合もセッションを残します（v2.1.288）
- **[Claude Tag] Claude が読んだだけの別のチャンネルの関連する Slack のスレッドも追うようにした**（v2.1.288）
- **[Claude Tag] チャンネルの Configure ページの保存のエラーを改善**。長すぎる指示は短くするよう示し、アクセスを失って断られた場合は再試行を勧めないようにしました（v2.1.288）
- **スキルの名前をどこに書くかの「Where you write the skill's name」ができた**。メッセージの先頭の `/deploy staging` は直接実行し、文の途中の `/deploy` は実行せず、そのメッセージでの実行の許可として扱います。スラッシュを外せば許可になりません。`disable-model-invocation: true` の説明も「あなただけが呼べる」から「Claude が自分では呼べない」に改められました（`features-overview`・`plugins/create`・`plugins/troubleshooting`・`sub-agents` も同様） — [日本語](https://code.claude.com/docs/ja/skills#where-you-write-the-skill’s-name) / [English](https://code.claude.com/docs/en/skills#where-you-write-the-skill’s-name)
- **ローカルのターミナルのセッションでは、同名のスキルが組み込みのコマンドを置き換える（エイリアスは除く）ことが載った**。プロジェクトの `usage` スキルは `/usage` を置き換え、`/cost` は組み込みのままです
- **`UserPromptSubmit` フックが、自分で打ったプロンプト以外でも動くことが載った**。スケジュールしたタスク（`/loop` の反復を含む）、バックグラウンドのサブエージェントの報告、別のセッションからのメッセージでも動きます（`hooks-guide`・`agent-sdk/hooks`・`agent-sdk/python`・`monitoring-usage` も同様） — [日本語](https://code.claude.com/docs/ja/hooks#userpromptsubmit) / [English](https://code.claude.com/docs/en/hooks#userpromptsubmit)
- **`PermissionRequest` フックの説明が改められた**。`--permission-prompt-tool` か `canUseTool` に届く呼び出しではフックとホストが並んで動き、先に決めた方が使われます。`-p` では `dontAsk` モード以外で動き、誰も決めなければ拒否されます。`permissionDecisionReason` の `"ask"` は、`-p` で拒否された場合は Claude がツールの結果で読む、と加わりました（`hooks-guide`・`workflows` も同様）
- **`idle_prompt` の通知は、バックグラウンドのサブエージェントなどが動いている間は送らない、と加わった**（`hooks`）
- **`/autocompact` の値がモデルごとに `modelSettings` に保存されるようになった**（v2.1.288 以降。前はトップレベルの `autoCompactWindow` に 1 つ）。`modelSettings` の `autoCompactWindow`（100000〜1000000 か `"auto"`）は同じファイルのトップレベルの値より優先されます（`settings-reference` も同様） — [日本語](https://code.claude.com/docs/ja/model-config#set-the-auto-compact-window) / [English](https://code.claude.com/docs/en/model-config#set-the-auto-compact-window)
- **`availableModels` に挙げたモデル ID に `/model` のピッカーの行が付くかどうかがプロバイダーごとに分かれた**。Anthropic API・Claude Platform on AWS・Claude apps gateway・LLM ゲートウェイでは行が付き、Bedrock・Agent Platform・Foundry では `anthropic.` で始まるものだけに付きます。`anthropic.` のエントリのうち Mantle に回るのは Mantle の形式に合うものだけ、とも改められました（`amazon-bedrock` も同様）。200K を超える要求を断るゲートウェイには `CLAUDE_CODE_AUTO_COMPACT_WINDOW=200000` を勧める形になっています
- **パスで範囲を絞った `.claude/rules` と入れ子の CLAUDE.md が、Read だけでなく Write・Edit でも読み込まれることが載った**（v2.1.288 以降。`memory`・`debug-your-config`・`glossary`）
- **`/memory` の自動メモリの切り替えは、バックグラウンドのセッションや別の Claude Code のセッションが始めたセッションではオフにはできてもオンには戻せない、と加わった**。その間は `off · can't be turned on here; ...` と表示されます（`memory`）
- **`claude --resume <session-id>` をどのディレクトリからでも使えることの説明が、独立した段落と番号付きの探索順に整理され、「Resume a running background session」の見出しができた** — [English](https://code.claude.com/docs/en/sessions#resume-a-running-background-session)
- **`AskUserQuestion` の自動続行のタイマーは、端末のウィンドウにフォーカスがある間は進まず、バックグラウンドのセッション・スクリーンリーダーモード・Remote Control の接続中は始まらない、と改められた**（`tools-reference`・`settings-reference`） — [English](https://code.claude.com/docs/en/tools-reference#question-auto-continue-timeout)
- **再開した直後に保存された会話のツールを呼ぶと、MCP サーバーが初回の接続中なら最大 10 秒待つことが載った**。`list_changed` の通知では、対話型の端末は一覧を取り直し、`-p` と Agent SDK はツールの一覧だけを更新する、とも分けて書かれました（`mcp`） — [English](https://code.claude.com/docs/en/mcp#tool-availability)
- **v2 の MCP クライアントで、v2.1.285 以降は機能フラグを取得するセッションで stdio のサーバーにも新しいプロトコルの版を問い合わせる（段階的に展開）ことが載った**。チャンネルのサーバーを古いハンドシェイクに留めるには `MCP_PROTOCOL_NEGOTIATION=legacy` を設定します（`mcp`・`env-vars`・`channels`）
- **advisor の受け付ける組み合わせの表が、メインのモデルの順位の低い順に並べ直された**。Opus 4.7・4.8 のメインに Sonnet 5.5 の advisor を付けられるようになり（v2.1.287 以降）、「API が断る」組み合わせの列は消えました — [English](https://code.claude.com/docs/en/advisor#choose-an-advisor-model)
- **エージェントチームでプラグインのサブエージェントの定義も使えること、インプロセスのチームメイトに定義の `disallowedTools` と `effort` が適用されることが加わった**（`SendMessage` などは残る） — [English](https://code.claude.com/docs/en/agent-teams#use-subagent-definitions-for-teammates)
- **プラグインの依存関係のインストールが終わらなかった場合、`/plugin` と `claude plugin list` に注記が出るようになったことが載った**。`are not installed` なら `claude plugin update` で再試行でき、`were not installed, because ...` なら理由（Yarn・pnpm・`bun.lockb` の lockfile や、パッケージマネージャーがない）が解消するまで入りません（`plugins/loading`・`plugins/cli-reference` の `notes` も同様） — [日本語](https://code.claude.com/docs/ja/plugins/troubleshooting#the-packages-it-lists-are-not-installed) / [English](https://code.claude.com/docs/en/plugins/troubleshooting#the-packages-it-lists-are-not-installed)
- **`claude plugin update` が、最新の版でも終わらなかった依存関係のインストールを再試行することが載った**。失敗すると `Failed to update plugin` と終了コード 1 になります（v2.1.287 より前は再試行しなかった）。節も「Which scope the command updates」「Update by bare name」などに分かれました — [English](https://code.claude.com/docs/en/plugins/cli-reference#retry-an-unfinished-dependency-install)
- **`managed-settings` に「When an admin document counts as present」の節ができた**。HKCU のレジストリを適用しない条件（管理用の文書が「ある」とみなす場合）が独立しました — [English](https://code.claude.com/docs/en/managed-settings#present-admin-documents)
- **プロジェクトとローカルの設定の `env` で無視される変数に、`SystemRoot`・`ComSpec`・`ProgramData`・`LOCALAPPDATA`・`PATHEXT`・`PSModulePath`・`ProgramFiles` など Windows の変数が加わった**（`settings-reference`）
- **`code-review` の「Review didn't run and the PR shows a spend-cap message」が「… budget message」になった**。月の支出上限に達した場合に加えて、使用クレジットの残高を使い切った場合もレビューを飛ばしてコメントを残し、チェックのカードにも原因と管理ページへのリンクを出します — [日本語](https://code.claude.com/docs/ja/code-review#review-didn’t-run-and-the-pr-shows-a-budget-message) / [English](https://code.claude.com/docs/en/code-review#review-didn’t-run-and-the-pr-shows-a-budget-message)
- **setup に、新しいモデルが stable チャネルより新しい版を要する場合は latest チャネルに移ること、apt・dnf・apk のリポジトリはリポジトリでチャネルを選ぶことが加わった**。Windows では Git Bash が Bash ツールに加えて Monitor ツールにも必要、とも改められました（`tools-reference` にも追記） — [English](https://code.claude.com/docs/en/setup#configure-release-channel)
- **バックグラウンドに移した既存のセッション（`←` や `/background`）はワークツリーに移らず、その場で編集を続けることが載った**（`agent-view`・`settings-reference` の `worktree.bgIsolation`）
- **VS Code・デスクトップアプリのセッションは別のセッションからのメッセージの承認ダイアログを出せないので、期限まで保留することが加わった**（`cross-session-messaging`）
- **VS Code で Stop か Esc を押すと今のターンは終わるが、バックグラウンドのエージェントはマップから止めるまで動き続ける、と加わった**（v2.1.286 以降）。拡張の版番号は同梱の Claude Code の版と同じであること、`/model` だけを打つとピッカーが開くこと（v2.1.284 以降）、`environmentVariables` の `CLAUDE_CONFIG_DIR` は絶対パスだけが効くことも加わりました
- **`sandboxing` で、ファイルシステムの配列をスコープ間でマージするとき、ロックの対象のエントリは外すと加わった**。TLS 終端の設定漏れは `claude doctor` の `TLS termination is unavailable` の警告で確かめる、とも改められました
- **`plugin-evals` の採点役のモデルが「小さく速いモデル」から「バックグラウンドのタスクに使うモデル」に改められた**（`plugins/cli-reference` も同様）。`goal`・`tools-reference` の WebFetch からも「小さく速いモデル」の言い回しが減っています
- **`plugins/publish` の「Anthropic のディレクトリに提出する」が 4 段階の手順になった**。`plugins/mods/create` には、数人・チーム・組織・誰にでも、と相手に応じた mod の配り方が加わりました — [English](https://code.claude.com/docs/en/plugins/publish#submit-to-anthropics-directory)
- **`artifacts` の制限の表に「Source location」が加わった**（ネットワーク上のパスは読まずに断る）

**バグ修正**

- 管理対象のマシンで、複合したシェルのコマンドの入れ子の部分への deny・ask ルールが、ユーザーが入れた mod の承認に負ける問題を修正（v2.1.289）
- 閉じていない `<script>` タグが多い、または `${` の入れ子が深い短いコードブロックで端末が固まる問題を修正（v2.1.289）
- シンボリックリンクを通じて @メンション・変更・IDE で選択したファイルに `Read` の deny ルールが効かない問題を修正（v2.1.289）
- ローカルのフォルダーのマーケットプレイスから入れたプラグインについて、`plugin list`・`plugin eval`・`plugin update` が古い写しを表示する問題と、シンボリックリンクの `--plugin-dir` のホットリロードを修正（v2.1.289）
- アップグレード後の最初のセッションで、インストール済みの mod が読み込まれない問題を修正（v2.1.289）
- フルスクリーンで Background tasks のダイアログを開いている間、プロンプトの上のプラグインの行が古いまま表示される問題を修正（v2.1.289）
- リンクが localhost のアドレス・パスの `@`・大文字のホスト・`file:` のパスを使うと、プラグインのペインが何も描かない問題を修正（v2.1.289）
- ユーザーが入れたプラグインが、組織が管理する MCP サーバーのサインインのツールの説明を書き換えられる問題を修正（v2.1.289）
- 端末が知らない枠線のスタイルの Box をプラグインが描くと、起動時に固まるか強制終了する問題を修正（v2.1.289）
- プラグインの画面上のハンドラーが非同期で例外を投げると、監視下のセッションとバックグラウンドのセッションが終わる問題を修正（v2.1.289）
- 高さのないプラグインの領域が伸び続けると、インターフェースのエラーでセッションが終わる問題を修正（v2.1.289）
- サンドボックスが自動で許可するとき、値を展開する環境変数の接頭辞（`TZ="$HOME" rm -rf build` など）の後ろのコマンドを Bash の deny・ask ルールが見落とす問題を修正（v2.1.289）
- サンドボックスの自動許可のもとで、コマンドの前に変数の代入だけがあると Bash の deny・ask ルールが飛ばされる問題を修正（v2.1.289）
- フォルダーにマーケットプレイスのマニフェストもあると `claude plugin validate` がプラグインを飛ばす問題を修正（v2.1.289）
- mod の `ui.render` フックが書いた値で行の描画が例外を投げると「unrecoverable interface error」でセッションが終わる問題を修正。Claude Code 自身の行を描くようにしました（v2.1.289）
- タブ・はぐれたエスケープ・C1 制御文字を含むテキスト、またはタブと CRLF を含む短いテキストが下の行に重なって描かれる問題を修正（v2.1.289）
- mod のペインや帯の右寄せの内容が閉じる印や `[-]` の下に描かれる問題を修正。それらも端末の端から 1 桁内側に置きます（v2.1.289）
- 描画中に失敗した mod の `Client` が、その mod が描いた周りのものまで巻き込む問題を修正。単独で失敗し `ui.fault` を起こします（v2.1.289）
- `claude plugin validate` が Anthropic のマーケットプレイス自身のプラグインを失敗させ、`--json` で問題のない `plugin.json` を一覧する問題を修正（v2.1.289）
- 描画に失敗した mod の帯が、一瞬だけ下のカードに場所を空けさせる問題を修正（v2.1.289）
- メッセージのない失敗で、失敗したプラグインの部品の理由が `Error` か空で表示される問題を修正（v2.1.289）
- 公開したアーティファクトのページが、閉じていない `<script>` タグの多い短いコードブロックで読み手のブラウザーのタブを固めるかクラッシュさせる問題を修正（v2.1.289）
- 描画中に端末が例外を投げた後、mod の `Client` の領域がセッションの間ずっと失敗のままになる問題を修正（v2.1.289）
- 応答の途中の API のタイムアウトでターンが失敗する問題を修正。非対話型のセッションとサブエージェントは途中の応答から続け、思考だけの応答は再試行します（v2.1.288）
- 最後の返信がトークン使用量 0 を報告したとき、長い会話が自動コンパクションせず「Prompt is too long」で失敗する問題を修正（v2.1.288）
- コンパクションが復元したばかりのファイルなどの文脈を、`--resume` がときどき落とす問題を修正（v2.1.288）
- 再開したセッションがターンの最後の応答を保存しないことがあり、次の `--resume` でプロンプトが未回答に見える問題を修正（v2.1.288）
- 読み込み中に同じセッションがファイルを書き換えると、再開で途中で切れたトランスクリプトを読み込むことがある問題を修正（v2.1.288）
- v2.1.286 以前に始めた会話を再開すると、モデルの前の思考が落ちる問題を修正（v2.1.288）
- Mantle や構造化出力を断るゲートウェイの背後で、セッションのタイトル・メモリーの呼び出し・プロンプトのフックが失敗する問題を修正し、`CLAUDE_CODE_DISABLE_STRUCTURED_OUTPUTS` を追加（v2.1.288）
- 止められたツールが Bash でないのに、auto モードの拒否が Claude に Bash の権限ルールを示す問題を修正（v2.1.288）
- Bedrock と Mantle の auto モードで、WebFetch の要約や `sonnet` のサブエージェントなど古いモデルへのリクエストの後、セッションの残りがローカルの分類器に切り替わる問題を修正（v2.1.288）
- 新しく選んだモデルで再起動したクラウドのセッションが、サーバーがそのモデルを断った後もそのモデルで返信する問題を修正（v2.1.288）
- 承認していない URL への WebFetch の権限の確認に 5 分答えないと、Cowork のクラウドのセッションが入力待ちのままになる問題を修正（v2.1.288）
- 別の端末で始めた Cowork のクラウドのセッションに参加したスマートフォンに、プロンプトの提案が出ない問題を修正（v2.1.288）
- Claude Code の再起動前に描いたビューで mod のボタンを押すと、別のボタンの動作が実行されることがある問題を修正（v2.1.288）
- 1 つの `Code` 要素が解析できない差分を持つと、プラグインのペインが何も表示しない問題を修正。プレーンなコードとして描きます（v2.1.288）
- プラグインの LSP サーバーが `initializationOptions` と `settings` で、置き換えた値やマニフェストの既定値ではなく `${user_config.*}`・`${CLAUDE_PLUGIN_ROOT}` をそのまま受け取る問題を修正（v2.1.288）
- ワークツリーで動くサブエージェントで、プラグインの `tool.call` フックが Bash を失敗させ、ファイルの検索が違うフォルダーを読む問題を修正（v2.1.288）
- 古い git（2.39 より前。Ubuntu 22.04 の 2.34 など）で、`git-subdir` のプラグインのインストールが失敗するか不完全なプラグインをキャッシュする問題を修正（v2.1.288）
- `--plugin-dir` で読み込んだプラグインに `/plugin` の「Configure options」が出ない問題を修正（v2.1.288）
- プラグインのタイマーや読み込みが動いている間にプラグインを再読み込み・無効化すると、バックグラウンドのセッションが終わる問題を修正（v2.1.288）
- サンドボックスの自動許可のもとで、本文が平文と単純な `$VAR` だけの、区切りを引用しないヒアドキュメント（`python3 <<EOF`）が毎回承認を求める問題を修正（v2.1.288）
- シェルが算術として評価する値の `BASHPID` の代入を、黙って許可せず確認するように Bash ツールの権限の確認を修正（v2.1.288）
- プラグインや mod がプロンプトの上に行を出している間にバックグラウンドのタスクのダイアログを開くと、フルスクリーンのセッションが「unrecoverable interface error」で終わる問題を修正（v2.1.288）
- 別のセッションが保留したメッセージを、Claude が届いたと報告する問題を修正。届いていないことと相手のセッションを示し、SDK のセッションではターンの途中で知れるようにしました（v2.1.288）
- `-p` と SDK のセッション、および PreToolUse フックの承認で、OpenTelemetry の `claude_code.tool.blocked_on_user` のスパンがソースや決定を `unknown` と報告する問題を修正（v2.1.288）
- `-p` や中断したターンで答えのないまま終わった権限の確認が、`tool_decision` のイベントを出さない問題を修正（v2.1.288）
- Cowork のクラウドのセッションの Edit と Retry が、履歴が残っているのに `/compact` の前に送ったメッセージを断る問題を修正（v2.1.288）
- 無人のセッション（`CLAUDE_CODE_RETRY_WATCHDOG`）が、とても長い応答のストリームの失敗の後に何時間も再試行する問題を修正。もう一度ストリームし、3 回タイムアウトすると諦めます（v2.1.288）
- 資格情報を安全な保存先に保存できなかったのに `/login` が「Login successful」と報告する問題を修正。失敗を示し、新しいログインが効かなかった場合は再試行を勧めます（v2.1.288）
- Bedrock の資格情報の検索中に Stop すると、リクエストを終える代わりにフォールバックのモデルに移ることがある問題を修正（v2.1.288）
- 別の Claude Code のプロセスがサインイン中にノート PC がスリープから復帰すると、`gcpAuthRefresh`・`awsAuthRefresh` のブラウザーのサインインが 2 つ開く問題を修正（v2.1.288）
- エージェントチームで、名前で起動したプラグインのエージェントが既定ではなく自身のプロンプト・ツール・`disallowedTools`・effort で動くように修正（v2.1.288）
- `timeout` や systemd などの監視役が SIGTERM と一緒に SIGCONT を送ると、ヘッドレス（`-p`・SDK）のセッションがときどき SIGTERM を無視する問題を修正（v2.1.288）
- 再起動したクラウドのセッションが、組織が強制するモデルの一覧で断られるモデルを復元する問題を修正（v2.1.288）
- リモートのサーバーの結果が 16 MB を超えるか解析できないと、MCP のツール呼び出しがときどき 2 回実行される問題を修正（v2.1.288）
- Claude Desktop の Code タブのサブエージェントに、ユーザーが設定した `memory` という名前の MCP サーバーのツールが 1 つも渡らない問題を修正（v2.1.288）
- auto モードが使えないとき（`disableAutoMode` や古いモデル）、許可したサイトでも Claude in Chrome がスクリーンショットとページの読み取りのたびに確認する問題を修正。入力・移動・JavaScript は引き続き確認します（v2.1.288）
- GitHub の SSH キーのない macOS と Linux のマシンで、GitHub をソースとするプラグインの `claude plugin install` が失敗する問題を修正。HTTPS にフォールバックして通知します（v2.1.288）
- `permissions.blockReadsOutsideWorkingDirectories` がオンの間、git の設定ファイルへの `sandbox.credentials.files` のエントリが効かない問題を修正（v2.1.288）
- Team・Enterprise のプランや管理設定のあるマシンで、Artifact ツールでスライドやデザインを始めるとき、組織のデザインシステムを Claude が使わない問題を修正（v2.1.288）
- Claude Code が自分を再起動した後（Claude apps gateway への最初のサインイン、プロバイダーの設定、`/tui`）、Windows でキーボードが効かない問題を修正（v2.1.288）
- `tools:` に `Agent(...)` のエントリがとても多いエージェントを起動すると止まる問題を修正（v2.1.288）
- PDF の全体が会話に入った後、Claude 3 Opus と Claude 3 Sonnet のセッションが毎ターン失敗する問題を修正（v2.1.288）
- プラットフォームのネイティブのバイナリのダウンロードに失敗し、仮の `claude` だけが入ったのに、npm の自動更新が成功と報告する問題を修正（v2.1.288）
- まだ接続しているか、別の Claude Code のプロセスがつなぎ直したばかりのセッションを、Remote Control の後片付けがアーカイブする問題を修正（v2.1.288）
- `owner/repo` のマーケットプレイスで SSH と HTTPS の取得が両方失敗したとき、2 回目のエラーだけが表示される問題を修正。両方を、先に試した方を上にして示します（v2.1.288）
- パスで範囲を絞った `.claude/rules` と入れ子の CLAUDE.md が、範囲内のファイルを Write や Edit で作成・変更したときに読み込まれない問題を修正（これまでは Read だけ）（v2.1.288）
- bypassPermissions モードやシェルの許可ルールのもとで、`bash -c`・`sh -c` のスクリプト内の危険な `rm`（`/` やホームディレクトリへのものなど）が確認なしで動く問題を修正（v2.1.288）
- 言語サーバーが動的な機能の登録を使うか応答しなくなると、LSP のツール呼び出しが無期限に止まる問題を修正。60 秒（サーバーごとの `requestTimeout`）でタイムアウトします（v2.1.288）
- バックグラウンドのエージェントが動いている間に `idle_prompt` の通知のフックが動く問題を修正（v2.1.288）
- 照合に失敗するか、ツールの入力を JSON にできないとき、PreToolUse と PermissionRequest のフックが飛ばされる問題を修正。その呼び出しはブロックします（v2.1.288）
- 新しい環境やモデルの切り替えの後の最初のリクエストが、サーバーのではなく組み込みの出力の上限と自動コンパクションのウィンドウを使う問題を修正。そのリクエストは最大 1.5 秒待つことがあります（v2.1.288）
- ctrl+enter でキューのメッセージを送った後、Interrupted の行に「What should Claude do instead?」のヒントが出る問題を修正（v2.1.288）
- `--bare` のセッションの `/login` が、セッションが読まないサインインを実行し、保存済みのログインを置き換えることがある問題を修正。使える資格情報を示します（v2.1.288）
- サブエージェントのファイルアクセスでルールや入れ子の CLAUDE.md が読み込まれたとき、InstructionsLoaded フックに agent\_id と agent\_type がない問題を修正。ファイルアクセスで読み込まれたものは effort も報告します（v2.1.288）
- `claude mcp serve` の Agent ツールが、使えるエージェントがないと常に報告し、すべての subagent\_type を断る問題を修正（v2.1.288）
- フルスクリーンのトランスクリプトビューアーの検索と `/theme` の色の検索で、端末のカーソルが入力したテキストを追わない問題を修正（v2.1.288）
- スクリーンリーダーモードの `/permissions` で、ルールの番号を打つと検索欄が開く代わりにそのルールを選ぶように修正（v2.1.288）
- `claude plugin test` が、古い保存済みの設定を読んだだけで mod がリモートでオフにされたと報告する問題を修正（v2.1.288）
- [VS Code] claude.ai のコネクタを承認した後も「Needs authentication」のままになる問題を修正。MCP サーバーのダイアログに Check connection を出します（v2.1.288）
- [VS Code] オプトインの New Conversation のショートカット（Cmd/Ctrl+N）が、表示中のすべての Claude のビューで会話を始める問題を修正（v2.1.288）
- [VS Code] 表示中のセッションをアーカイブすると、チャットのビューが次の保存済みのセッションを再開する問題を修正。新しい会話を始めます（v2.1.288）
- [クラウドセッション] 無関係のセキュリティ設定の読み込み中や失敗時に、管理画面の Cloud sessions のスイッチがオフでロックされる問題を修正（v2.1.288）
- [クラウドセッション] セルフホストのランナーの起動中に Stop を押してもキューのメッセージが取り消されず、ランナーが上がると実行されることがある問題を修正（v2.1.288）
- [Claude Tag] 自動で作られたチャンネルの設定に、必ず失敗する「Remove this scope」が出る問題を修正（v2.1.288）

**その他**

- **[VS Code] v2.1.288 の `claude auth status` の変更を元に戻した**。サインアウトが増えた可能性があるためです（v2.1.289）
- **`claude project purge` を `claude purge` に変更**。古い名前も通知を出して動きます（v2.1.288。`claude-directory`・`cli-reference`・`sessions` も変更、`claude-projects` からは `claude project` への言及が消えた） — [日本語](https://code.claude.com/docs/ja/claude-directory#clear-local-data) / [English](https://code.claude.com/docs/en/claude-directory#clear-local-data)
- **ANTHROPIC_DEFAULT_SONNET_MODEL が Claude Sonnet 5.5 か Opus 5.5 を指していても、クライアント側の auto モードの分類器は Claude Sonnet 5 を使うように変更**（v2.1.288）
- **エージェントビューの `n:` フィルター（と Ctrl+F の検索）で、Enter が先頭の行ではなく名前が最もよく合うセッションを開くように変更**（v2.1.288）
- **完了を報告できないサーバーからの MCP の URL のプロンプトは、「I'm done, continue」を待ってからツール呼び出しを続けるように変更**（v2.1.288。`mcp` の URL モードの説明からも「承認すると開く」が外れた）
- **`/autocompact` の保存をモデルごとに変更**（v2.1.288。詳細は「機能改善」の `/autocompact` の項目参照）
- **バックグラウンドのコマンドの時間制限を無人のセッションだけに変更**（v2.1.288。詳細はハイライト 4 参照）
- **デスクトップアプリの設定の場所の表記が「Settings > General（Desktop app の下）」から「Settings > This computer > System」になった**（`computer-use`・`desktop`・`desktop-scheduled-tasks`）。`desktop` の auto モードの利用条件は「Auto mode availability」の小節に移りました
- **クラウド環境の編集のダイアログ名が「Edit cloud environment」から「Edit environment」になった**（`cloud-environments`・`errors`・`routines`）。資格情報を追加できるのは既存の環境の編集画面だけ、という説明も消えています
- **`communications-kit`・`champion-kit` で、plan mode と権限についての表現が控えめになった**。「危ないことの前に許可を求める」「ファイルに触れる前に全部を示す」といった文が、「ソースを編集せずに調べて変更を提案する」などに改められています
- **`ultrareview` の料金の表から Team・Enterprise の行と、課金の権限のないメンバーが CLI から管理者に依頼する説明が消えた**
- **`voice-dictation` のトラブルシューティングに `Unknown command: /voice` が加わった**（claude.ai のアカウントがアクティブなサインインのときだけ使え、`ANTHROPIC_API_KEY` などがあるとそちらが優先される）
- **`permissions` に Manual モードの Bash の権限の確認の画面写真が、`permission-modes` に Shift+Tab でモードが切り替わる様子の動画が加わった**
- **v2.1.197〜v2.1.199 前後の版についての「As of」「Requires」などの注記が多くのページで削除された**（`agent-teams`・`agents`・`commands`・`cli-reference`・`hooks`・`hooks-guide`・`llm-gateway-protocol`・`mcp`・`permission-modes`・`sandboxing`・`settings-reference`・`setup`・`skills`・`sub-agents`・`claude-platform-on-aws` など）
- **このほか、`sub-agents` の「Trust required for inline MCP servers」の小節化、`settings-reference` の `customEndpoint` の説明から Foundry のリソース名の例が外れたこと、`best-practices` のパイプの例が `claude -p "explain this error"` になったこと、`accessibility`・`llm-gateway-connect`・`plugins/components`・`plugins/marketplace-reference`・`plugins/loading` などの言い回しの修正があった**
- **前回までに見出しマップにだけ先に載っていた見出しのうち、23 が本文に入りました**（`errors` の 8 見出し、`claude-apps-gateway-config` の「Certificate client authentication」「Extended context in Claude Desktop」など 5 見出し、`claude-apps-gateway-deploy` の 2 見出し、`plugins/cli-reference` の `plugin update` の 3 見出し、`self-hosted-environments-configuration` の 2 見出し、`sessions` の「Resume a running background session」、`statusline` の「Spend limit fields」、TypeScript SDK の `toggleMcpServer()`）
- **見出しマップには今回も、本文にまだない見出しが先に載りました**。`claude-code-on-the-web` の「Quick web setup for Team and Enterprise」「Errors when sending to a cloud session」、`claude-apps-gateway-config` の「Start sessions on a model the policy allows」、`hooks` の「How `if` patterns match Bash commands」「Tools that require user interaction」の 5 見出しです。`claude-code-on-the-web` の「Output and errors」はマップでは「Output」に変わり（本文は旧名のまま）、「Take back a queued message」と「Manage context」の位置も入れ替わっています
- **見出しマップ冒頭の自動生成スタンプが、2026年10月03日 00時40分44秒 UTC から 2026年10月04日 05時16分55秒 UTC へ進みました**

**参考リンクについて**: 日本語版は、`errors`・`claude-apps-gateway-config`・`claude-apps-gateway-spend-limits`・`self-hosted-environments-configuration`・`agent-sdk/typescript`・`statusline`・`tools-reference`・`interactive-mode`・`model-config`・`code-review`・`vs-code`・`chrome`・`skills`・`hooks`・`plugins/troubleshooting`・`claude-directory` の 16 ページを実測し、すべて今回の内容に更新されていたためリンクを付けています。**それ以外のページ（`advisor`・`agent-teams`・`mcp`・`sessions`・`setup`・`managed-settings`・`plugins/cli-reference`・`plugins/publish`・`claude-apps-gateway-deploy` など）は日本語版を確かめていないため、英語版だけにしています。** 見出しマップにだけある見出しは、本文に節がないためリンクを付けていません。 **changelog ページへのリンクは、本サマリの方針どおり付けていません。**

## 新着情報

**今回、`whats-new/` 配下のページに変更はありません。**

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-10-02.md](./archives/latest/2026-10-02.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-10-02.md](./archives/latest-detail/2026-10-02.md)

<!--
base_commit: f1380431c4bc062901668fe07773b6af5b247d50
head_commit: dce38920d12d39a079b4f53b19149f8f3ed45f63
generated_at_full: 2026-10-04T15:06:32+09:00
-->
