---
対象期間: 2026年08月25日 〜 2026年08月26日
作成日: 2026-08-26
---

# Claude Code 公式ドキュメント更新サマリ

```markdown
今回は 1 日分の取り込みで、36 ページに差分がありました。差分行は 633 行で、うち 36 行は changelog の v2.1.247（2026年08月26日）1 リリース分です。ページの新規追加・削除はなく、`llms.txt` にも差分はありません。最大の変更は「Claude がフィードバックの下書きを作る」新機能で、ツールリファレンス・設定リファレンス・環境変数など 7 ページにまたがって追記されました。

主要なものを以下に挙げます。

1. Claude が自分でフィードバックの下書きを作って手元のキューに溜め、`/feedback` で確認してから送れるようになった
2. スピナーのカスタムヒントが、ID・再表示までの間隔・優先度を持てるようになり、外部ファイルからも読めるようになった
3. バックグラウンドセッションのターミナルホストが死んだ／無応答になった場合を検出して、Enter で再起動できるようになった
4. 組織で IP 許可リストを使っている場合に `bridge.claudeusercontent.com` をどう通すかが明記された
5. Team / Enterprise の Claude Code on the web のオンボーディング手順が実態に合わせて全面的に書き直された
```

## ハイライト

1. [**Claude がフィードバックの下書きを作る `SendFeedback` ツール**](./latest-detail.md#1-claude-がフィードバックの下書きを作る-sendfeedback-ツール):  
  ツールや操作が繰り返し失敗したとき、間違いを指摘されたときなどに、Claude がフィードバック報告の下書きを作って手元（`~/.claude/feedback/drafts/`）に溜める。送るまで Anthropic には何も届かない。`/feedback` を引数なしで実行するとキューが開く。設定キー `feedbackDrafts` で挙動を選べる。
2. [**スピナーのカスタムヒントが ID・クールダウン・優先度・外部ファイルに対応した**](./latest-detail.md#2-スピナーのカスタムヒントが-idクールダウン優先度外部ファイルに対応した):  
  `spinnerTipsOverride` の `tips` に `{id, text, cooldownSessions, priority}` のオブジェクトを書けるようになり、`tipsFile` で外部 JSON から、`label` で `Tip:` 以外の接頭辞で出せる。プロジェクト／ローカル設定からは素の文字列のみ。v2.1.247 以降。
3. [**バックグラウンドセッションのターミナルホスト死亡・無応答を検出して再起動できるようになった**](./latest-detail.md#3-バックグラウンドセッションのターミナルホスト死亡無応答を検出して再起動できるようになった):  
  Linux と WSL では数秒ごとにホストプロセスを点検し、死んでいれば行を失敗にして理由を出す。開いても 10 秒ほど出力が来なければ再起動を提案する。いずれも会話は保存されており、`Enter` か `claude attach` で再開できる。v2.1.247 以降。
4. [**組織の IP 許可リストと `bridge.claudeusercontent.com` のプロキシ egress**](./latest-detail.md#4-組織の-ip-許可リストと-bridgeclaudeusercontentcom-のプロキシ-egress):  
  Claude で IP 許可リストを使っている組織は、`bridge.claudeusercontent.com` を `claude.ai` や `api.anthropic.com` と同じプロキシ egress に通す必要がある。外れていると Claude in Chrome だけがつながらず、他は動くという症状になる。
5. [**Team / Enterprise の Claude Code on the web オンボーディングが書き直された**](./latest-detail.md#5-team--enterprise-の-claude-code-on-the-web-オンボーディングが書き直された):  
  GitHub コネクタを Owner が有効にするまで **Sign in with GitHub** が出ないこと、**Quick web setup** が既定でオフでその場合は環境作成フォームが出ることなど、Team / Enterprise で実際に起きることが 4 ページにわたって明記された。

## 新規追加されたページ

（今回の対象期間に新規追加・削除されたドキュメントページはありません。`llms-full.txt` に展開されているページ数は前後とも 191 で、`llms.txt` 自体にも差分はありませんでした）

## 大幅に更新されたページ

- [**エラーリファレンス**](./latest-detail.md#1-エラーリファレンス) ([English](https://code.claude.com/docs/en/errors#find-your-error)):  
  差分 170 行で今回最大。新設セクションが 7 本（うち 3 本は v2.1.247 由来）入り、応答が途中で切れたときの扱いも書き直された。
- [**設定リファレンス**](./latest-detail.md#2-設定リファレンス) ([English](https://code.claude.com/docs/en/settings-reference#all-settings)):  
  差分 80 行。`spinnerTipsOverride` の全面書き直し（ハイライト 2）と、新キー `feedbackDrafts`（ハイライト 1）の 2 か所でほぼ全てを占める。
- [**ツールリファレンス**](./latest-detail.md#3-ツールリファレンス) ([English](https://code.claude.com/docs/en/tools-reference#sendfeedback-tool-behavior)):  
  差分 59 行、全て追加。`SendFeedback` ツールの行と、小見出し 6 本を持つ新設セクション（ハイライト 1）。

## 軽微な更新

今回は 1 日分の取り込みで、`llms-full.txt` に差分のあったページは 36、差分行は合計 633 行です。ページの新規追加・削除はなく、`llms.txt` にも差分はありません（前回大きく組み替わったカテゴリ別構成のままです）。**大幅更新に入れる基準は前回同様「実質の差分 50 行以上 かつ 内容の変更を伴うこと」**とし、今回はエラーリファレンス（170 行）・設定リファレンス（80 行）・ツールリファレンス（59 行）の 3 ページが該当しました。

changelog に加わったのは **v2.1.247（2026年08月26日）の 1 リリース**だけで、差分は 36 行です。項目は 33 件（Added 4・Updated 1・Fixed 19・Improved 2・Changed 7）で、以下では単一リリースなので各 bullet へのバージョン併記は省きます。**changelog ページへのリンクは張りません**。

ページ見出しマップ（`claude_code_docs_map.md`）は、上記の新設セクション（fork PR のレビュー、ターミナルホスト関連、`Raw mode is not supported`、エラーの 4 節、IP 許可リスト、`feedbackDrafts`、`SendFeedback tool behavior` の 6 小見出し、`ResultError`）を取り込みました。生成時刻の表記も 2026年08月26日 02:08 UTC から 2026年08月27日 00:36 UTC に進んでいます。

なお本サマリの参考リンクは全て英語版のみです。今回の変更に日本語版が追従していないためで、日本語版のツールリファレンスとエラーリファレンスを実際に取得して確認したところ、前者には `SendFeedback` の記載が一切なく、後者には今回の新設 7 節のアンカーがどれも存在しませんでした（前回扱った `has-a-wildcard-before-the-rest-of-the-command` すら未反映です）。また日本語版の設定リファレンス（`/docs/ja/settings-reference`）は現時点で 404 を返します。他のページは個別には確認していませんが、いずれも直近 1〜2 日の変更であるため未追従とみなし、安全側に倒して英語版のみを載せています。

**新機能**

- `SendFeedback` ツールが加わり、Claude がフィードバック報告の下書きを作って `/feedback` のキューに溜められるようになりました（詳細はハイライト 1 参照）— [English](https://code.claude.com/docs/en/tools-reference#sendfeedback-tool-behavior)
- 設定キー `feedbackDrafts` が加わりました（詳細はハイライト 1 参照）— [English](https://code.claude.com/docs/en/settings-reference#feedbackdrafts)
- 環境変数 `CLAUDE_CODE_SEND_FEEDBACK` が加わりました。`0` でそのセッションの下書き機能を切り、`1` は既にアクセス権がある場合に有効化します（変数自体がアクセス権を与えることはできず、`DISABLE_FEEDBACK_COMMAND` や `feedbackDrafts` の `off` といった他の停止スイッチは引き続き効きます）— [English](https://code.claude.com/docs/en/env-vars#variables)
- `spinnerTipsOverride` にヒントのオブジェクト形式・`tipsFile`・`label` が加わりました（詳細はハイライト 2 参照）— [English](https://code.claude.com/docs/en/settings-reference#spinnertipsoverride)
- Code Review に **Review pull requests from forks** が新設されました。fork からのプルリクエストは、リポジトリの **Review Behavior** 設定に関わらず**自動ではレビューされず**、`@claude review` をコメントしたときだけ動きます。必要な書き込み権限は fork 側ではなくベースリポジトリのものです。再度レビューさせるには `@claude review` をもう一度投稿します（`@claude review always` も使えますが、fork の PR は以後の push に購読されません）。チェック実行の **Re-run** も、新しいコミットの push も、fork の PR ではレビューを開始しません — [English](https://code.claude.com/docs/en/code-review#review-pull-requests-from-forks)
- キーバインドの `Select` コンテキストに `select:pageUp`・`select:pageDown`・`select:first`・`select:last` の 4 アクションが加わりました（既定は PageUp / PageDown / Home / End）。これらのバインドが効くのは `/skills` メニューで、`/model` ピッカーなど他の多くのリストではバインドに関わらず PageUp / PageDown でページ送りし、Home / End は無視されます。特殊キー名にも `pageup`・`pagedown`・`home`・`end` が加わりました — [English](https://code.claude.com/docs/en/keybindings#select-actions)
- インストールのトラブルシュートに `Raw mode is not supported` during install が新設されました。組織のサーバー管理設定にセキュリティ承認が要る変更が含まれる場合、v2.1.246 より前は `claude install` の最中に承認ダイアログを出そうとし、`curl … | bash` のようにパイプから実行するとダイアログが端末を掴めず失敗していました。v2.1.246 以降はこれらのコマンド中にダイアログを出さず、次の対話セッションに回します（`forceRemoteSettingsRefresh` などで起動時に設定取得を待つ構成では従来どおり出るため、パイプ実行は失敗します）。それ以外の構成では、インストーラを再実行すれば通ります — [English](https://code.claude.com/docs/en/troubleshoot-install#raw-mode-is-not-supported-during-install)
- Python Agent SDK に例外クラス `ResultError` が加わりました（0.2.140 以降）。`ProcessError` を継承するため既存の `except ProcessError` でも捕まり、`subtype`・`errors`・`result`・`api_error_status`・`terminal_reason`・`session_id`・`data` の属性で失敗の理由をメッセージ本文の解析なしに分岐できます。0.2.140 より前は `ClaudeSDKError` を継承しない素の `Exception` が送出されていました — [English](https://code.claude.com/docs/en/agent-sdk/python#resulterror)
- `~/.claude` ディレクトリの説明に `feedback/drafts/`（レビュー待ちの下書き）が、自動削除の表と手動削除の表の両方に加わりました — [English](https://code.claude.com/docs/en/claude-directory#cleaned-up-automatically)
- ゼロデータ保持で使えなくなる機能の表に **Claude Tag** が加わりました（チャンネルメモリとセッションのトランスクリプトを保持するため）— [English](https://code.claude.com/docs/en/zero-data-retention#features-disabled-under-zdr)
- Bash の権限プロンプトに auto モードを案内するヒントが加わり、1 キーで選べる「Yes, and switch to auto mode」の選択肢が付きました
- `/claude-api cost-optimize` が加わりました。既存プロジェクトの Claude API 費用をプロファイルし、キャッシュ・トークン整理・バッチ・effort・モデル選択といったコスト要因を、1 回に 1 つずつ計測しながら詰めていくものです
- `/claude-api` スキルが Admin API（組織メンバー・招待・ワークスペース・API キー・レート制限レポート・ワークロード ID フェデレーション・CMEK）を扱えるよう更新されました

**機能改善**

- エージェントビューのページに **The terminal host died or the session stopped responding**（小見出し 2 本）が新設され、バージョン履歴の表にも v2.1.247 の行が加わりました（詳細はハイライト 3 参照）— [English](https://code.claude.com/docs/en/agent-view#the-terminal-host-died-or-the-session-stopped-responding)
- Claude Code on the web の入門ページの **Connect GitHub** が、注記の追加と 3 ステップの改称を含めて全面的に書き直されました（詳細はハイライト 5 参照）— [English](https://code.claude.com/docs/en/web-quickstart#connect-github)
- プラグイン推奨のページで、スピナーヒントとセッション開始通知が消える条件が、設定ファイル全体での解決結果に基づく形に書き直されました（詳細はハイライト 2 参照）— [English](https://code.claude.com/docs/en/plugin-relevance#how-it-works)
- `/terminal-setup` が Zed の `keymap.json` を**その場でマージ**するようになりました。既存のバインドがあって Terminal の `shift-enter` が無い場合は、まず同じディレクトリに `keymap.json.1a2b3c4d.bak` のようなバックアップを取ってから Shift+Enter のバインドを差し込み、他のキーバインドとコメントを保ちます。読めない・パースできない・バックアップできない・マージ結果を検証できないときはファイルを変えず、追記すべきキーバインドのブロックを表示します（同一修正のエラーリファレンス側での言及はバグ修正を参照）— [English](https://code.claude.com/docs/en/terminal-config#enter-multiline-prompts)
- 非対話セッションで、途中で切れた応答を Claude Code が最大 3 回まで自動で続けさせるようになりました（v2.1.246 以降。詳細は大幅更新 1 参照）— [English](https://code.claude.com/docs/en/errors#the-response-above-may-be-incomplete)
- Code Review のコメントコマンドに必要な権限の記述が「owner・member・collaborator のアクセス」から「**write・maintain・admin のいずれかの権限**」に改められました。あわせて、組織のメンバーシップを非公開（GitHub の既定）にしていると GitHub が本人をメンバーとして通知しないため、Claude が 👀 を付けてもレビューが始まらないことが明記されました。直すにはメンバーシップを公開にするか、リポジトリの管理者に collaborator として直接追加してもらいます — [English](https://code.claude.com/docs/en/code-review#manually-trigger-reviews)
- Code Review の失敗・タイムアウトからの再実行で、GitHub の Checks タブの **Re-run** ボタンが使えることになりました（fork の PR を除く）。従来は「**Re-run** ボタンでは Code Review は再実行されない」と書かれていました — [English](https://code.claude.com/docs/en/code-review#retrigger-a-failed-or-timed-out-review)
- サーバー管理設定の承認ダイアログについて、ダイアログを出せない場合の扱いが 4 つの箇条書きに整理されました。新たに **`claude install` / `claude update` の最中はダイアログを出さず、最後に承認した設定でコマンドを実行して次の対話セッションで出す**（v2.1.246 以降）が加わっています — [English](https://code.claude.com/docs/en/server-managed-settings#security-approval-dialogs)
- ストリーミングのアイドル監視でストリームを打ち切ったときの扱いが、応答がどこまで進んでいたかで再送・不完全通知・正常終了に分かれることと、非対話セッションでは先に続きを促す場合があることが明記されました — [English](https://code.claude.com/docs/en/network-config#streaming-idle-watchdogs)
- `Notification` フックの `permission_prompt` が、ツール使用の承認だけでなく**サンドボックス化されたコマンドのネットワークリクエスト**の承認でも発火することが明記されました（ターミナルセッションでは v2.1.246 以降）。あわせて `PermissionRequest` フックは**このネットワークリクエストのプロンプトでは走らない**ことが明記され、即時のシグナルが欲しい場合は `permission_prompt` を使うよう案内されています — [English](https://code.claude.com/docs/en/hooks#permissionrequest)
- `/reload-plugins` のスキル件数に、プラグインの `commands/` エントリだけでなく `SKILL.md` スキルも含まれるようになりました（v2.1.246 以降）。v2.1.246 より前は `commands/` しか数えなかったため、`SKILL.md` スキルを読み直しても `0 skills` と報告していました。— [English](https://code.claude.com/docs/en/discover-plugins#apply-plugin-changes-without-restarting)
- プラグイン作成のクイックスタートから、`/reload-plugins` の要約が「`0 skills` と報告することがある」という注意書きが削除されました（上記の修正が入ったため）— [English](https://code.claude.com/docs/en/plugins#create-your-first-plugin)
- `claude plugin update` が素のプラグイン名を解決するようになりました（v2.1.246 以降）。別々のマーケットプレイス由来の同名プラグインが入っている場合は更新を拒否し、`plugin-name@marketplace-name` の完全修飾コマンドを提示します。v2.1.246 より前は完全修飾形しか受け付けず、素の名前は「見つからない」として弾いていました — [English](https://code.claude.com/docs/en/plugins-reference#plugin-update)
- プラグインスキルの frontmatter の `name` が既にプラグインの接頭辞で始まっている場合、v2.1.246 以降は接頭辞を二重に付けなくなりました（`name: my-plugin:fancy` は `/my-plugin:fancy` のまま）。v2.1.216 から v2.1.245 までは二重になっていました — [English](https://code.claude.com/docs/en/skills#how-a-skill-gets-its-command-name)
- MCP のページで、Anthropic ホストのコネクタにローカル OAuth でサインインしようとしたときの案内が具体化され、エラーリファレンスの該当節と claude.ai の Connectors ページへのリンクが付きました。`claude mcp remove <name>` で自分のエントリを消してから claude.ai でつなぐと、コネクタが自動で現れます — [English](https://code.claude.com/docs/en/mcp#use-mcp-servers-from-claude-ai)
- コマンドリファレンスの `/feedback` の説明に、下書きキューが使えるセッションでは引数なしの `/feedback` がキューを開くこと（引数付きと `/bug` は従来どおりダイアログを直接開くこと）が加わりました — [English](https://code.claude.com/docs/en/commands#all-commands)
- コマンドリファレンスの `/skills` の説明が更新されました。絞り込みが名前だけでなく**説明とソース**でもできること、`Space` に加えて `Enter` でも可視性を切り替えられること、`Esc` で保存して閉じること、そして**プラグインスキル・`disable-model-invocation: true` のスキル・管理設定や `--settings` の `skillOverrides` があるスキルは切り替えられない**ことが加わりました — [English](https://code.claude.com/docs/en/commands#all-commands)
- 環境変数のページで、`CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` と `DISABLE_FEEDBACK_COMMAND` が止めるものに「Claude が下書きするフィードバック」が加わり、feature flag 取得がオフだと使えない機能の一覧にも同機能が追加されました — [English](https://code.claude.com/docs/en/env-vars#features-that-need-feature-flag-fetching)
- データ利用のページに、Claude が下書きしたフィードバックも送信すれば `/feedback` 報告と同じ経路・保持期間で扱われることと、トランスクリプトを含めるかは下書きのレビュー画面での選択によることが明記されました — [English](https://code.claude.com/docs/en/data-usage#feedback-using-the-%2Ffeedback-command)
- デスクトップアプリのページのネットワーク要件に、IP 許可リストと `bridge.claudeusercontent.com` の扱いが加わりました（詳細はハイライト 4 参照）— [English](https://code.claude.com/docs/en/desktop#network-access-requirements)
- Claude in Chrome のエラー表で、`"Browser extension is not connected"` の原因と対処に組織の IP 許可リストの場合が加わりました（詳細はハイライト 4 参照）— [English](https://code.claude.com/docs/en/chrome#common-error-messages)
- クラウド環境の **The Default environment** が、CLI 経由・ブラウザ（Pro / Max）・ブラウザ（Team / Enterprise）の 3 通りに書き分けられました（詳細はハイライト 5 参照）— [English](https://code.claude.com/docs/en/cloud-environments#the-default-environment)
- Slack のページの「Claude Code is not enabled for your account」の対処に、ウェブのオンボーディングを完了することが加わりました（詳細はハイライト 5 参照）— [English](https://code.claude.com/docs/en/slack#claude-code-is-not-enabled-for-your-account)
- プラグインマーケットプレイスの堅牢化が進みました。制御文字や不可視文字を含む名前を拒否し、`/plugin` と `claude plugin` の出力に出るマーケットプレイス由来のテキストをエスケープ安全にしています
- Bedrock・Vertex・Foundry のセッション（およびテレメトリを切ったセッション）で、設定した MCP サーバーが接続に失敗したことが Claude に伝わるようになりました。従来は「そのツールは存在しない」と結論づけていました
- Sonnet 5 の自動コンパクトの既定ウィンドウが 1M コンテキスト全体になりました。1M ウィンドウのセッションは約 934K トークンではなく約 967K トークンで自動コンパクトします
- クロスセッションのピアメッセージが既定で 1 行の `Message from @<sender>: <first line>` プレビューに畳まれるようになりました（Ctrl+O で全文を展開）
- Markdown 描画中のターミナルハイパーリンクで、ネットワークパスや自動マウントのパスを指すもの・制御文字を含むもの・不可視文字で始まるものはプレーンテキストとして描画されるようになりました
- プロンプトフッタの PR バッジが、直近のチェックから 1 分未満ならターミナルにフォーカスが戻っても GitHub への再チェックを飛ばすようになりました
- 管理設定でゲートウェイログインが強制されている場合やカスタム OAuth 配備の場合に、アナリティクスがログイン後だけでなく起動時からオフになりました
- Claude apps ゲートウェイへのサインインリクエストが、Claude Code であることを示すようになりました（`surface=claude_code` のデバイス認可パラメータと `claude-code/<version>` の User-Agent）
- 組織のサインイン強制が、管理者の管理設定を読めない場合には（ホスト提供の設定や Windows レジストリのユーザー単位設定があっても）起動時に終了するようになりました

**バグ修正**

- `/terminal-setup` が Zed の `keymap.json` 全体を自分のキーバインドで**上書きしてしまう**問題を修正。v2.1.247 より前は `//` コメントや末尾カンマを含む keymap をパースできず、ファイル全体を自分のバインドだけに置き換えたうえで「インストール済み」と報告していました。置き換えられた keymap は `.bak` バックアップから戻せます — [English](https://code.claude.com/docs/en/errors#terminal-setup-left-your-zed-keymap-unchanged)
- 履歴検索・`/config`・`/mcp`・`/skills`・バックグラウンドタスク・`/model` で、矢印キーと Enter を素早く続けて押すと、移動先の 1 つ上の行に対して操作が効いてしまう問題を修正
- サブエージェントが最初の呼び出しでモデルの 404 に当たると落ちる問題を修正。セッションのフォールバックモデル連鎖を使うようになり、親へ返るエラーにもエラー種別・ステータス・リクエスト ID・モデルが含まれます
- フックやバックグラウンドエージェントが数 MB のエラー出力を吐くと会話が溢れ、「Prompt is too long」でセッションが動かなくなる問題を修正
- kitty プロトコルのターミナルで、非ラテン系（キリル文字など）のキーボードレイアウトだと Ctrl のショートカットが効かない問題を修正
- エスケープの接頭辞直後で読み込みが分割されてマウスレポートが届くと、`<35;150;7M` のような文字列がプロンプトに入力される問題を修正
- Bash サンドボックスのコマンド後の後始末が、書き込み可能領域の外に張り直された dotfile 管理（nix / home-manager、stow）の `~/.claude/settings.json` シンボリックリンクを消してしまう問題を修正
- `/rename` が、セッションレジストリを更新できなかった場合にも黙って成功したように見せる問題を修正。他のセッションには古い名前が見えたままかもしれない旨を伝えます
- `--agent` で始めたセッションの `/compact` と「Summarize from here」が、その会話自身のシステムプロンプトではなく既定のシステムプロンプトで要約する問題を修正
- `claude agents` で、ターミナルホストプロセスが死んだバックグラウンドセッションが「opening…」のまま止まる問題を修正（詳細はハイライト 3 参照）— [English](https://code.claude.com/docs/en/errors#terminal-host-process-died)
- フックやバックグラウンドタスクの出力ファイルを書けなかったときにメモリが際限なく増える問題を修正。ファイルにはどこで出力が失われたかが記録されます
- SSH 越しの `/install-github-app` を修正。コピーのショートカットが常に成功したと言う代わりにどうコピーしたかを伝え、ブラウザを開けない場合はサインイン URL がすぐ表示されます
- フォアグラウンドから引き継いだシェルコマンドが、バックグラウンドセッションで終了したときに内部エラーを記録したり誤解を招く `[exited with code -1]` の行を出したりする問題を修正
- バージョン指定のないマーケットプレイスプラグインで、2 つ目のスコープにインストールするとライブキャッシュのディレクトリが削除・再作成され、それを使っている実行中セッションが乱される問題を修正
- `/remote-control` で始めた Remote Control セッションが、作業ツリーの差分を接続中のクライアントに報告しない問題を修正
- セルフホストのランナーのセッションが、Claude Code が起動する前に `running` と報告する問題を修正。Claude デスクトップアプリから「Claude is waiting for your input」の通知が早すぎるタイミングで出ることがありました
- 管理設定が Claude apps ゲートウェイのサインインを構成していて Anthropic のエンドポイントに到達できないとき、初回セットアップが「Unable to connect to Anthropic services」で終了する問題を修正
- クラウドセッション（Claude Code on the web、デスクトップ／モバイルアプリ）で、メッセージ送信直後にモードを切り替えると前の権限モードが表示されることがある問題を修正
- バックグラウンドエージェント・シェル・モニターが動いている最中にターン間でコンテナが再起動すると、クラウドセッションが無言になる問題を修正。再開したセッションが失われた作業を報告します

**その他**

- ドキュメントの例文で使われる技術の組み合わせが差し替えられました。ダイナミックワークフローの例は「styled-components から Tailwind へ」から「JavaScript から TypeScript へ」に、コマンドリファレンスの `/batch` の例は「Solid から React へ」から「JavaScript から TypeScript へ」に変わっています。いずれも記述内容の変更ではありません — [English](https://code.claude.com/docs/en/workflows#migrate-many-files-in-parallel)
- 同じく例文の差し替えで、ベストプラクティスの並列実行の例は「React から Vue へ」から「Python 2 から Python 3 へ」に、スキルの引数の例は「React / Vue」から「JavaScript / TypeScript」に変わりました — [English](https://code.claude.com/docs/en/best-practices#fan-out-across-files)
- 権限モードのページで、プロンプトを出せないセッションの auto モードのフォールバックの説明から「メインの会話でもサブエージェントでも同様に」が外れ、代わりにエラーリファレンスへのリンクが付きました — [English](https://code.claude.com/docs/en/permission-modes#when-auto-mode-falls-back)
- セキュリティガイダンスのページで、プロジェクトの `.claude/settings.json` 経由で有効化されたプラグインについて、`/plugin` から行う操作の呼び方が「disabling（無効化）」から「uninstalling（アンインストール）」に統一されました — [English](https://code.claude.com/docs/en/security-guidance#disable-or-uninstall)
- プラグインリファレンスのエラー例に、`plugin.json` が UTF-8 の BOM 付きで保存されている場合も v2.1.246 より前は「corrupt manifest file」になっていた旨が加わりました（この修正自体は前回サマリで扱っています）— [English](https://code.claude.com/docs/en/plugins-reference#example-error-messages)
- Agent SDK（Python）のエラー処理のサンプルコードが `ResultError` を捕まえる形に更新されました。`ResultError` は `ProcessError` を継承するため、`except ProcessError` より**前**に置く必要があります — [English](https://code.claude.com/docs/en/agent-sdk/python#error-handling)
- Streaming Input のページのサンプルコードでも、「素の `Exception` が送出される」という前提のコメントが `ResultError` を前提とする記述に置き換わりました — [English](https://code.claude.com/docs/en/agent-sdk/streaming-vs-single-mode#implementation-example)
- フック入門のページでも `permission_prompt` の説明とバージョン注記が本編と同じ内容に更新され、`PermissionRequest` の注意書きが「あらゆる権限プロンプト」から「あらゆる**ツール**の権限プロンプト」に限定されました — [English](https://code.claude.com/docs/en/hooks-guide#get-notified-when-claude-needs-input)
- Claude Code on the web のページの Auto-fix の注記から、「セットアップ中に促されたときにインストールする」という導線が削除されました（オンボーディングの手順が変わったため）— [English](https://code.claude.com/docs/en/claude-code-on-the-web#auto-fix-pull-requests)

## 新着情報

（今回の対象期間に新着情報ページの追加・更新はありません。Week 34（2026年08月17日～21日）が最新のままです）

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-08-25.md](./archives/latest/2026-08-25.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-08-25.md](./archives/latest-detail/2026-08-25.md)

<!--
base_commit: 9183e5fb58ed21ba3079f4e0f6a528c4e46d1ea7
head_commit: 1178d4a1adaaa1829aeb0ab27ac4940eb1bd90bb
generated_at_full: 2026-08-27T15:09:38+09:00
-->
