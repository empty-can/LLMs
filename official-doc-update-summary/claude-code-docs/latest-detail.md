---
対象期間: 2026年11月13日 〜 2026年11月14日
作成日: 2026-11-14
---

# Claude Code 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
**今回は、Google Cloud のプロジェクトを通じて Anthropic が運用する Claude API を使う新しいプロバイダー「Claude Models on Google Cloud (Anthropic managed)」のページ（`claude-models-on-google-cloud-anthropic-managed`）が加わり、`feature-availability` をはじめ既存の 10 ページがこのプロバイダーを扱うようになりました。認識できないモデル ID に想定するコンテキストウィンドウ、server-managed settings のキャッシュの期限、auto mode の設定、Agent SDK の大きなメッセージの扱いも書き直されています**。changelog と新着情報（whats-new）のページは変わっていません。`llms.txt` は新しいページの 1 行が加わって URL が 240 から 241 になり、各言語の索引のページ数も 204 から 205 になりました。`llms-full.txt` では 205 ページのうち 47 ページ（新しいページを含む）の内容が変わり、生の差分は 907 行（追加 627・削除 280）です。うち 182 行は `agent-sdk/overview` の掲載位置の移動で、これを除くと 725 行（追加 536・削除 189）です。大幅更新は `feature-availability` の 1 ページです。総行数は 128,207 行から 128,554 行に増えました。

主要なものを以下に挙げます。

1. 新しいプロバイダー Claude Models on Google Cloud (Anthropic managed) のページが加わった。Google Cloud の認証情報で Anthropic が運用する Claude API を使い、`CLAUDE_CODE_USE_ANTHROPIC_GOOGLE_CLOUD` などの 3 つの環境変数で設定する（Claude Code v2.1.307 以降）。`feature-availability` の表には「Google Cloud (Anthropic managed)」の列ができ、これまでの Agent Platform の列は「Google Cloud (Google managed)」になった
2. 認識できないモデル ID に想定するコンテキストウィンドウの記述が 200K から 1M に替わった。`llm-gateway-protocol` と `microsoft-foundry` は既定で 1M と述べ、`model-config` と `errors` は警告が名指すウィンドウを想定する、という書き方になった
3. server-managed settings のキャッシュは最後に取得に成功してから 24 時間で期限が切れる、と載った。期限の後に起動時の取得が失敗すると、セッションは server-managed settings なしで始まる
4. auto mode の設定のページが改められた。h2「Route all shell commands through the classifier」は「Suspend shell allow rules」になって plan mode で分類器がコマンドを審査する間にも及び、`prod` か `production` を名前の中の単語として含むホストが機密のリモートの対象になり、push と pull request の既定の説明も書き直された
5. Agent SDK に大きなメッセージの対処が載った。Python SDK の `max_buffer_size`（既定 1,048,576 文字）を超えるメッセージは `CLIJSONDecodeError` になり、トラブルシューティングに対処の節ができた。TypeScript SDK には `matchDeniedModels()` と `SDKAssistantMessage` の `supersedes` が加わった
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**Claude Models on Google Cloud (Anthropic managed) のページが加わった**](#1-claude-models-on-google-cloud-anthropic-managed-のページが加わった):  
  新しいページ `claude-models-on-google-cloud-anthropic-managed` は、Google Cloud のプロジェクトを通じて Anthropic が運用する Claude API を Claude Code から使う手順をまとめています。`feature-availability`・`env-vars`・`model-config`・`permission-modes`・`advisor`・`settings-reference`・`tools-reference`・`errors`・`google-vertex-ai`・`third-party-integrations` にもこのプロバイダーの記述が加わりました
2. [**認識できないモデル ID のコンテキストウィンドウの想定が 1M になった**](#2-認識できないモデル-id-のコンテキストウィンドウの想定が-1m-になった):  
  `llm-gateway-protocol` と `microsoft-foundry` は、認識できない ID には既定で 1M のウィンドウを想定する、と述べるようになりました。`model-config` の警告の例は `context assumed to be 1m tokens` に替わり、`errors` の表の行も `<N> tokens` にまとめられています
3. [**server-managed settings のキャッシュに 24 時間の期限が載った**](#3-server-managed-settings-のキャッシュに-24-時間の期限が載った):  
  `server-managed-settings` の「Fetch and caching behavior」に、キャッシュした設定は最後に取得に成功してから 24 時間で期限が切れるものとして計画する、と載りました。期限の後に起動時の取得が失敗すると、セッションは server-managed settings なしで始まります
4. [**auto mode の設定のページが改められた**](#4-auto-mode-の設定のページが改められた):  
  `auto-mode-config` の h2「Route all shell commands through the classifier」が「Suspend shell allow rules」になり、`autoMode.classifyAllShell` は plan mode で分類器がコマンドを審査する間にも allow ルールを止める、と載りました。機密のリモートの対象の既定、push と pull request の既定、Desktop アプリの注記も改められています
5. [**Agent SDK に大きなメッセージの対処と `matchDeniedModels()` が載った**](#5-agent-sdk-に大きなメッセージの対処と-matchdeniedmodels-が載った):  
  `agent-sdk/troubleshooting` に h2「Large tool calls and results」ができ、Python SDK の `max_buffer_size` を超えるメッセージで出る `CLIJSONDecodeError` の対処が載りました。TypeScript SDK のリファレンスには `matchDeniedModels()`・`SDKAssistantMessage` の `supersedes`・フックのハートビートが加わっています
<!-- light:highlight-list:end -->

## 1. Claude Models on Google Cloud (Anthropic managed) のページが加わった

**新しいページ `claude-models-on-google-cloud-anthropic-managed`（151 行）は、Claude Models on Google Cloud (Anthropic managed) を「Anthropic が運用し、Google Cloud のプロジェクトを通じて使う Claude API」として説明します。** Claude Code から使うには、Google Cloud にサインインし、3 つの環境変数を設定します。Google が管理する Google Cloud の Agent Platform（旧 Vertex AI）を使っているなら `google-vertex-ai` のページに従う、という注記があり、どちらを使っているかは Claude Platform のドキュメントの「Which offering are you using?」で確かめます。Claude Code は v2.1.307 以降が要ります。

- **前提**: アカウントの設定が済んだ Google Cloud のプロジェクト、そのプロジェクトでの IAM のロール `roles/claude.user`（Claude Code を動かす Google アカウントかサービスアカウントごと）、プロジェクト ID と `wrkspc_` で始まるワークスペース ID、Google アカウントでサインインするなら gcloud CLI
- **手順**: ①Application Default Credentials を作る（Google アカウントなら `gcloud auth application-default login` を実行し、`GOOGLE_APPLICATION_CREDENTIALS` は外す。サービスアカウントのキーファイルならこの変数にそのパスを設定する）、②`~/.claude/settings.json` の `env` に `CLAUDE_CODE_USE_ANTHROPIC_GOOGLE_CLOUD`（`1`）・`ANTHROPIC_GOOGLE_CLOUD_PROJECT`・`ANTHROPIC_GOOGLE_CLOUD_WORKSPACE_ID` を加える（Anthropic のアカウントへのログインもログアウトも要らない）、③`claude` を始めて `/status` を実行し、`API provider` の行に `on Google Cloud` があり、その後ろに `Workspace ID`・`GCP project`・`GCP location` が出るのを確かめる（シェルや CI では `claude auth status --text`）
- **チームでの設定**: 手順 ②の `env` を各開発者のマシンの managed settings のファイルに置き、各開発者に `roles/claude.user` を与えて、それぞれのマシンで `gcloud auth application-default login` を実行してもらう。チームに配るなら `ANTHROPIC_DEFAULT_OPUS_MODEL` などでモデル ID を固定する（例は `claude-opus-5-5`・`claude-sonnet-5-5`・`claude-fable-5-1`・`claude-haiku-4-5-20251001`）
- **環境変数**: 必須の `CLAUDE_CODE_USE_ANTHROPIC_GOOGLE_CLOUD`、`ANTHROPIC_GOOGLE_CLOUD_BASE_URL` を設定しない限り必須の `ANTHROPIC_GOOGLE_CLOUD_WORKSPACE_ID`、推奨の `ANTHROPIC_GOOGLE_CLOUD_PROJECT`（ないと `GOOGLE_CLOUD_PROJECT` を使う）、既定が `global` の `ANTHROPIC_GOOGLE_CLOUD_LOCATION`、LLM ゲートウェイなどにベース URL を替える `ANTHROPIC_GOOGLE_CLOUD_BASE_URL`、ゲートウェイが Google の認証情報を付けるときに Google のアクセストークンを送らない `CLAUDE_CODE_SKIP_ANTHROPIC_GOOGLE_CLOUD_AUTH` の 6 つ
- **使えない機能**: fast mode、Remote Control とクラウドのセッション、claude.ai の MCP コネクター、Channels、`/design-sync` と `/import`、server-managed settings（チームには各マシンの managed settings を使う）。ほかは `feature-availability` の **Google Cloud (Anthropic managed)** のタブを見る
- **トラブルシューティング**: ログインを求められるか `/status` に `on Google Cloud` がないときは、変数が `1` か、版が 2.1.307 以降か、`CLAUDE_CODE_USE_BEDROCK`・`CLAUDE_CODE_USE_FOUNDRY`・`CLAUDE_CODE_USE_ANTHROPIC_AWS` が残っていないかを確かめる（`CLAUDE_CODE_USE_VERTEX` は残してよい）。h3 は `No workspace ID found`・`No project was given`・`Could not load Google Cloud credentials`・`Google Cloud credentials expired or invalid`・`Google Cloud authentication failed` の 5 つで、最後のものはプロジェクト・ワークスペース・IAM のロール（`roles/claude.user` か `roles/claude.admin`）・`claude.googleapis.com` のサービスの有効化を確かめる

**既存のページもこのプロバイダーを扱うようになりました。**

- **`feature-availability`**: 表の列と「Summary by provider」のタブができた（詳細は大幅更新 1 参照）
- **`env-vars`**: 上の 6 つの変数の行が加わった。`ANTHROPIC_GOOGLE_CLOUD_WORKSPACE_ID` は、v2.1.307 以降で `ANTHROPIC_GOOGLE_CLOUD_BASE_URL` を設定していれば要らない。「Features that need feature-flag fetching」の advisor の例外も、v2.1.300 以降の Claude Platform on AWS か Claude Models on Google Cloud (Anthropic managed) になった
- **`model-config`**: 「Model aliases」の表に、`opus` が Opus 5.5・`sonnet` が Sonnet 5.5・`haiku` が Haiku 4.5 を選ぶ行が加わり、「`default` model setting」でも既定が Opus 5.5 のプロバイダーにこのプロバイダーが加わった
- **`permission-modes`**: 「Eliminate permission prompts with auto mode」の「Model」と「Provider」の 2 項目が「Provider and model」にまとまり、Anthropic API・Claude Platform on AWS と並んでこのプロバイダーでも Opus 4.6 以降・Sonnet 4.6 以降・Haiku 5.5・Fable で auto mode を使える、となった
- **`advisor`・`settings-reference`・`tools-reference`**: advisor の要件と `advisorModel`（どちらも v2.1.300 以降）、`allowedProviders` の値 `"anthropicGoogleCloud"`、WebSearch を使えるプロバイダーにこのプロバイダーが加わった
- **`errors`・`google-vertex-ai`・`third-party-integrations`**: `errors` の「Google Cloud credentials expired or invalid」と「Google Cloud authentication failed」に、`CLAUDE_CODE_USE_ANTHROPIC_GOOGLE_CLOUD` を設定しているなら新しいページの手順に従う、という項目が加わった。`google-vertex-ai` の冒頭には、このページは Google が管理する Agent Platform のもので、Anthropic 管理の方は新しいページに従う、という注記が、`third-party-integrations` の「Compare deployment options」には新しいページへのリンクが加わった

`llms.txt` では、「Deployment」の `claude-platform-on-aws` と `google-vertex-ai` の間に「Claude Code with Claude Models on Google Cloud (Anthropic managed)」の行が加わり、`feature-availability` の説明文も「Amazon Bedrock、Claude Platform on AWS、Google Cloud's Agent Platform、Microsoft Foundry」を列挙する形から「Amazon Bedrock や Google Cloud のようなクラウドのプロバイダー」に替わりました。

- [Google Cloud 上の Claude モデル（Anthropic 管理）で Claude Code を使用する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/claude-models-on-google-cloud-anthropic-managed#set-up-claude-code)
- [Claude Code with Claude Models on Google Cloud (Anthropic managed) - Claude Code Docs (English)](https://code.claude.com/docs/en/claude-models-on-google-cloud-anthropic-managed#set-up-claude-code)
- [機能の利用可能性 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/feature-availability#availability-by-model-provider)
- [Feature availability - Claude Code Docs (English)](https://code.claude.com/docs/en/feature-availability#availability-by-model-provider)

## 2. 認識できないモデル ID のコンテキストウィンドウの想定が 1M になった

**認識できないモデル ID に Claude Code が想定するコンテキストウィンドウの記述が、200K から 1M に替わりました。** ページによって書き方が違います。

- **`llm-gateway-protocol`**: 「Settings for unrecognized model IDs」の「Context window」が、「200K、ID に `[1m]` があれば 1M を想定する」から「既定で 1M のコンテキストウィンドウを想定する」になった
- **`microsoft-foundry`**: 「1M token context window」が、デプロイメントの名前をモデルに対応づけられないときは既定で 1M を想定するので、デプロイしたモデルが受け付けるウィンドウがそれより小さければ実際のウィンドウを設定する、となった（これまでは 200K を想定する、としていた）。デプロイメントの名前の付け方の説明は注記になった
- **`model-config`**: 「Correct the window for a gateway or custom model ID」の警告の例が `context assumed to be 1m tokens` と `so it assumes a context window of 1m tokens` になり、警告は「200K を想定する」ではなく「警告が名指すウィンドウを想定する」という意味だ、と改められた。警告が実際のウィンドウを名指していれば直すものはない。「Pin models for third-party deployments」でも、固定した ID は、ネイティブで 1M のモデルに対応づけられる場合と、どのモデルにも対応づけられない場合に、既定で 1M のウィンドウとして扱われる、となった（後者はモデルが受け付けるウィンドウが小さければ設定する）
- **`errors`**: 「Find your error」の 2 行（`context assumed to be 200k tokens` と `assumes a context window of 200k tokens`）が `<N> tokens` の 1 行にまとまり、「Prompt is too long」の項目も、認識しない ID の警告が想定したウィンドウを名指すことがあり、それが実際と違えば実際のウィンドウを与える、という説明になった
- **`statusline`**: `context_window.context_window_size` の説明から「既定で 200000、拡張コンテキストのモデルでは 1000000」が外れた

どのページもこの想定の変更に必要な版は述べていません。`model-config` の「Which IDs `CLAUDE_CODE_MAX_CONTEXT_TOKENS` applies to」には、`[1m]` を含む認識しない ID の扱いと、200K の上限が適用されない警告の説明がこれまでどおり残っています。

**Microsoft Foundry で既定のモデルがないときの動きも書き直されました。** `microsoft-foundry` の「4. Pin model versions」と `model-config` の「Pin models for third-party deployments」は、これまで「Microsoft Foundry には起動時のモデルの確認がないので、既定が使えなければ要求が失敗する」としていましたが、リソースに既定のモデルのデプロイメントがなければ Claude Code は古いモデルに切り替えるか要求が失敗する、となりました。切り替えたときは `Switched to <fallback> because <model> is not available` で始まるメッセージが出ます。Amazon Bedrock と Agent Platform の起動時の確認は `amazon-bedrock` の「Startup model checks」へリンクしています。

日本語版の `errors` はまだ今回の内容になっていなかったので、英語版だけをリンクしています。

- [モデル設定 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/model-config#correct-the-window-for-a-gateway-or-custom-model-id)
- [Model configuration - Claude Code Docs (English)](https://code.claude.com/docs/en/model-config#correct-the-window-for-a-gateway-or-custom-model-id)
- [Claude Code ゲートウェイ互換性ガイド - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/llm-gateway-protocol#settings-for-unrecognized-model-ids)
- [Claude Code gateway compatibility guide - Claude Code Docs (English)](https://code.claude.com/docs/en/llm-gateway-protocol#settings-for-unrecognized-model-ids)
- [Claude Code on Microsoft Foundry - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/microsoft-foundry#1m-token-context-window)
- [Claude Code on Microsoft Foundry - Claude Code Docs (English)](https://code.claude.com/docs/en/microsoft-foundry#1m-token-context-window)
- [Error reference - Claude Code Docs (English)](https://code.claude.com/docs/en/errors#prompt-is-too-long)

## 3. server-managed settings のキャッシュに 24 時間の期限が載った

**`server-managed-settings` の「Fetch and caching behavior」に、キャッシュした設定は最後に取得に成功してから 24 時間で期限が切れるものとして計画する、という項目が加わりました。** これまでの「キャッシュした設定はネットワークの障害の間も残る」という項目は外れ、起動時の取得が失敗した場合が 2 つに分かれています。

- **期限の前に失敗した**: これまでどおり、対話のセッションと Code タブで、キャッシュしたポリシーが有効だと警告する
- **期限の後に失敗した**: セッションは server-managed settings なしで始まり、警告はリモートのポリシーが当たらないと述べる。代わりに Claude Code を終了させるには `forceRemoteSettingsRefresh` を設定する

同じページの「Enforce fail-closed startup」も、起動時の取得が失敗すると既定で最後に取得したキャッシュの設定で続けるが、期限が切れていればそうしない、期限切れかキャッシュがなければ server-managed settings なしで続ける（端末の endpoint-managed settings は当たる）、となりました。「Security considerations」の表では、キャッシュのファイルを書き換えた場合の説明が「書き換えたファイルは起動時に当たりうる」になり、API が使えない場合も「キャッシュした設定があり、期限が切れていなければ当たる」となっています。

ほかのページも追従しました。`errors` の「Remote managed settings failed to load」は、`no remote policy applied` になるのは当てるキャッシュがないとき、として、まだ取得していないマシンや最後の取得が 24 時間より前のマシンを例に挙げます（日本語版は未追従なので英語版だけをリンクしています）。`managed-settings` の「Where each mechanism stores the policy」も、ローカルのキャッシュを起動時に「当てる」から「当てうる」に改め、「Fetch and caching behavior」へリンクしています。

- [サーバー管理設定を構成する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/server-managed-settings#fetch-and-caching-behavior)
- [Configure server-managed settings - Claude Code Docs (English)](https://code.claude.com/docs/en/server-managed-settings#fetch-and-caching-behavior)
- [Error reference - Claude Code Docs (English)](https://code.claude.com/docs/en/errors#remote-managed-settings-failed-to-load)

## 4. auto mode の設定のページが改められた

**`auto-mode-config` の h2「Route all shell commands through the classifier」が「Suspend shell allow rules」になりました（アンカーは `#route-all-shell-commands-through-the-classifier` のまま）。** `autoMode.classifyAllShell` を `true` にすると、auto mode が有効な間と、plan mode で分類器がコマンドを審査する間に、Bash と PowerShell の allow ルールが止まります。これまでの「すべてのシェルのコマンドを分類器が評価する（クリティカルパスの削除を除く）」「この設定は auto mode が有効な間だけ当たる」という文は外れ、auto mode と plan mode では allow ルールだけが承認したはずのコマンドが分類器の決定を待つぶん遅くなる、という説明になりました。`settings-reference` の「`autoMode.classifyAllShell`」のリンクの文字も新しい見出しに替わっています。

- **「Common boundaries」**: auto mode では、Claude は既定で作業中のリポジトリ（既定のブランチを含む）にプロンプトなしで push でき、タスクが求めるときは pull request も開ける。一部の push と pull request（シークレットを含む push や別のリポジトリへの pull request など）は止められる。これまでの、`production`・`release`・`gh-pages` のようなデプロイ先らしい名前のブランチは既定の対象外で、分類器がそれ自体で判断する、という説明は外れた
- **「Add a human checkpoint」**: `permissions.ask` のルールは分類器より先に評価されるので「既定で」プロンプトが出る、という言い方になった（これまでは、auto mode でも必ずプロンプトを出す、としていた）。表の `permissions.ask` の行も「Always prompts」が「By default, prompts」になった
- **「Define trusted infrastructure」**: 機密のリモートの対象は、既定で `prod` か `production` が名前の中の 1 つの単語であるホストか名前空間になり、例として `prod-db` は当たり `webprod01` は当たらない、と載った。名前を挙げると規則がそれに当たる、という文と、リモートのシェルとポートフォワードに明示の承認が要る、という言葉は外れ、「heuristic」は「default」と言い換えられた
- **Desktop アプリ**: 「Edit rules from `/permissions`」に、Desktop アプリの `/permissions` には **Auto mode** タブがなく、ローカル・WSL・SSH のセッションではセッションが動くマシンか WSL のディストリビューションの `~/.claude/settings.json` の `autoMode` のブロックを編集する、という注記が加わった。「Review denials」にも **Recently blocked** タブがないので、意図した操作は次のメッセージで操作と詳細を名指してやり直させる、という注記が加わった。`commands` の `/permissions` の行も、Desktop アプリでは設定ファイルを編集する、となった

`model-config` の「Fallback model chains」には新しい h4「Which entries Claude Code tries」ができ、auto mode と、plan mode で分類器がコマンドを審査する間は、auto mode が対応しないモデルを飛ばすので、どちらかのモードを使うなら対応するモデルを含める、という項目が加わりました。

- [オートモードの設定 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/auto-mode-config#route-all-shell-commands-through-the-classifier)
- [Configure auto mode - Claude Code Docs (English)](https://code.claude.com/docs/en/auto-mode-config#route-all-shell-commands-through-the-classifier)
- [オートモードの設定 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/auto-mode-config#define-trusted-infrastructure)
- [Configure auto mode - Claude Code Docs (English)](https://code.claude.com/docs/en/auto-mode-config#define-trusted-infrastructure)

## 5. Agent SDK に大きなメッセージの対処と `matchDeniedModels()` が載った

**`agent-sdk/troubleshooting` に h2「Large tool calls and results」と h3「CLIJSONDecodeError: JSON message exceeded maximum buffer size」ができました。** Python SDK は、Claude Code からの 1 つのメッセージが `max_buffer_size`（既定 1,048,576 文字。エラーの文はバイトと呼ぶ）より長いとこのエラーを出します。

- **当たりやすいもの**: Read のツールで約 393 KB 以上の PDF 全体を読むと、ツールの結果がファイルの base64 を 2 回持つので上限に届きうる。Read か MCP のツールのスクリーンショットも同じ。Edit と Write のメッセージは、変わる量によっては 1 MB よりずっと小さいファイルでも届く
- **直し方**: `ClaudeAgentOptions(max_buffer_size=64 * 1024 * 1024)` のように上限を上げる。スクリーンショットにも、Read の上限 20 MB までの PDF 全体にも足りる
- **止まった作業を続ける**: ツールが既に行った変更は残る。`ClaudeSDKClient` を開いているなら `disconnect()` を呼び（このエラーの後は受け取らないが Claude Code は動き続ける）、上限を上げて `continue_conversation=True` で新しい `query()` か `ClaudeSDKClient` を始める。特定のセッションを選ぶには init の `SystemMessage` の `session_id` を `resume` に渡す

ページの説明文と冒頭も、大きなツールの呼び出しと結果を扱う、と替わりました（`llms.txt` の説明文も同じ）。`agent-sdk/python` の `ClaudeAgentOptions` の `max_buffer_size` も「CLI の stdout を溜める最大バイト」から「SDK が CLI から受け付ける 1 つのメッセージの最大の文字数」に替わり、`CLIJSONDecodeError` はこの上限を超えたときにも出る、と加わりました。

**`agent-sdk/typescript` には次が加わりました。**

- **`matchDeniedModels()`**: `models` のうち `deniedModels` の一覧が止めるものを報告する関数。`denied` はモデルごとの真偽値、`warnings` は無視した入力と見た目より多くか少なく止めるエントリーを挙げる。`false` は許可されたという意味ではない（Claude Code は別名とモデルの上書きも確かめる）。アルファで、Agent SDK v0.3.323 以降が要る
- **`SDKAssistantMessage` の `supersedes`**: このメッセージが置き換える前のメッセージの UUID の一覧。届いたら表示からそれらを外す
- **`SDKToolProgressMessage`**: Agent SDK v0.3.323 以降では、`tool_use_id` が `hook-` で始まるハートビートはツールの呼び出しではなく長く動くフックからのもので、`tool_name` は `PreToolUse` のようなフックのイベント名になる

`agent-sdk/python` には、このほか次の変更があります。`ResultMessage` の `"tool_deferred_unavailable"` で、再開と一緒にプロンプトを送った場合は、既定でプロンプトが Claude に届かず呼び出しは保留のまま、ツールなしで続けるには呼び出しを落とす、となりました（これまでは、Claude Code がツールの結果なしで答え、保留の呼び出しはなくなる、としていました）。`SandboxSettings` で `failIfUnavailable` を設定すると、サンドボックスを始められないとき `query()` が `ResultError` を出す、という説明になり、`SyncHookJSONOutput` の `suppressOutput` のコメントも「効果がない」になっています。

- [Agent SDK のトラブルシューティング - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/agent-sdk/troubleshooting#large-tool-calls-and-results)
- [Troubleshoot the Agent SDK - Claude Code Docs (English)](https://code.claude.com/docs/en/agent-sdk/troubleshooting#large-tool-calls-and-results)
- [Agent SDK リファレンス - TypeScript - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/agent-sdk/typescript#matchdeniedmodels)
- [Agent SDK reference - TypeScript - Claude Code Docs (English)](https://code.claude.com/docs/en/agent-sdk/typescript#matchdeniedmodels)

## 新規追加されたページ

<!-- light:new-pages:start -->
- [**Claude Code with Claude Models on Google Cloud (Anthropic managed)**](#1-claude-code-with-claude-models-on-google-cloud-anthropic-managed) ([日本語](https://code.claude.com/docs/ja/claude-models-on-google-cloud-anthropic-managed) / [English](https://code.claude.com/docs/en/claude-models-on-google-cloud-anthropic-managed)):  
  Google Cloud のプロジェクトを通じて Anthropic が運用する Claude API を使うための前提・設定の手順・チームでの設定・モデルの固定・環境変数・使えない機能・トラブルシューティングをまとめた 151 行のページです（詳細はハイライト 1 参照）
<!-- light:new-pages:end -->

## 1. Claude Code with Claude Models on Google Cloud (Anthropic managed)

**`llms.txt` では、「Deployment」の `claude-platform-on-aws` と `google-vertex-ai` の間に「Claude Code with Claude Models on Google Cloud (Anthropic managed)」の行が加わりました。** 説明文は「Configure Claude Code to use the Claude API that Anthropic runs through your Google Cloud project, with Google Cloud credentials, IAM, and Marketplace billing.」です。`llms-full.txt` では `claude-apps-gateway-spend-limits` と `claude-platform-on-aws` の間に 151 行で展開され、見出しは h2 が 7 つ（「Prerequisites」「Set up Claude Code」「Pin model versions」「Environment variables」「Claude Code features that aren't available」「Troubleshooting」「Related resources」）、h3 が 6 つ（「Set up Claude Code for a team」とトラブルシューティングの 5 つ）です。

ページは、Agent Platform との違いの注記と版の要件から始まり、前提・3 つの手順（Application Default Credentials を作る・変数を設定に加える・Claude Code を始めてプロバイダーを確かめる）・チームでの設定・モデルの固定・6 つの環境変数の表・使えない機能・トラブルシューティングが続きます。内容はハイライト 1 のとおりです。

- [Google Cloud 上の Claude モデル（Anthropic 管理）で Claude Code を使用する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/claude-models-on-google-cloud-anthropic-managed#troubleshooting)
- [Claude Code with Claude Models on Google Cloud (Anthropic managed) - Claude Code Docs (English)](https://code.claude.com/docs/en/claude-models-on-google-cloud-anthropic-managed#troubleshooting)

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
- [**Feature availability**](#1-feature-availability) ([日本語](https://code.claude.com/docs/ja/feature-availability#summary-by-provider) / [English](https://code.claude.com/docs/en/feature-availability#summary-by-provider)):  
  54 行（追加 42・削除 12）が変わりました。表に「Google Cloud (Anthropic managed)」の列ができ、Agent Platform の列とタブは「Google Cloud (Google managed)」になり、新しいプロバイダーのタブが加わりました
<!-- light:updated-pages:end -->

**行数の数え方**: `llms-full.txt` の生の差分のハンクを、追加行は head 側、削除行は base 側の `Source:` 行でページに振り分けた値です。今回はページの並びが 1 か所変わりました。`agent-sdk/overview` が `advisor` の後ろから `agent-sdk/observability` の後ろへ移り、生の差分ではこのページが 182 行（追加 91・削除 91）に見えますが、ページ同士を比べると変更はないので、どのカテゴリにも入れていません。`feature-availability` に次いで多いのは `model-config` の 47 行（追加 35・削除 12）で、50 行に届きません（ページを切り出して difflib で比べると 51 行になりますが、分類はハンクの振り分けの値で行っています）。changelog の変更はありません。

## 1. Feature availability

**新しいプロバイダーの列とタブが加わり、Google Cloud の 2 つの提供形態を区別するようになりました。** 冒頭の説明文は、プロバイダーを列挙する形から「Anthropic のサブスクリプションの各プラン、Anthropic Console、Amazon Bedrock や Google Cloud のようなクラウドのプロバイダー」に替わりました。

- **「Availability by model provider」**: 「Google Cloud (Anthropic managed)」の項目（Claude Models on Google Cloud (Anthropic managed) を使い `CLAUDE_CODE_USE_ANTHROPIC_GOOGLE_CLOUD` を設定する。Google Cloud のプロジェクトを通じて Anthropic が運用する Claude API に届く）が加わり、「Google Cloud's Agent Platform」の項目は「Google Cloud (Google managed)」（旧 Vertex AI の Agent Platform の一部として Google が運用し、`CLAUDE_CODE_USE_VERTEX` を設定する）になった
- **表の列**: 「CLI capabilities that vary by provider」と「Admin and analytics」の 2 つの表で、「Google Cloud's Agent Platform」の列が「Google Cloud (Google managed)」になり、その前に「Google Cloud (Anthropic managed)」の列ができた。新しい列は、Web search・Auto mode・Advisor（v2.1.300 以降）・Cross-session messaging（同じマシンだけ）・GitLab CI/CD が ✓、Fast mode・Code Mode・Channels・GitHub Actions・Analytics・Server-managed settings が ✗、Zero Data Retention が「✓ (on request)」
- **「Summary by provider」**: 新しいタブ「Google Cloud (Anthropic managed)」は、Claude のサブスクリプションが要る機能に加えて fast mode・Channels・GitHub Actions・Code Mode・analytics のダッシュボード・server-managed settings・`/design-sync` と `/import` を使えないものに、Google Cloud (Google managed) にはない Advisor（v2.1.300 以降）を使えるものに挙げる。部分的な対応はセッションの間のメッセージ（同じマシンだけ）と、依頼すれば使える Zero Data Retention（Anthropic のアカウントの担当者に連絡する）。「Google Cloud's Agent Platform」のタブは「Google Cloud (Google managed)」になり、`CLAUDE_CODE_USE_VERTEX` を設定して Agent Platform で使っているならこのプロバイダーだ、という文が加わった
- **言い換え**: 「Features available on every provider」の tool search の注記と、表の脚注 1・5 の「Google Cloud's Agent Platform」が「Google Cloud (Google managed)」になった（脚注 5 には「Google Cloud (Anthropic managed)」も加わった）。`/design-sync` と `/import` が使えないところと、「Availability by subscription plan」が当たらない認証は、プロバイダーの列挙から「クラウドのプロバイダー」に替わった。「Summary by provider」の冒頭の、エラーの報告と Anthropic へのテレメトリが既定でオフのプロバイダーの列挙では「Google Cloud's Agent Platform」が「Google Cloud (Google managed)」になり、新しいプロバイダーはこの列挙に入っていない
- **「Related resources」**: プロバイダーの設定のガイドに新しいページが加わった

新しいページの「Claude Code features that aren't available」は、fast mode・Remote Control とクラウドのセッション・claude.ai の MCP コネクター・Channels・`/design-sync` と `/import`・server-managed settings を挙げ、ほかはこのページのタブを見るよう案内しています。タブの「Not available」には、このほか GitHub Actions・Code Mode・analytics のダッシュボードも入っています。

- [機能の利用可能性 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/feature-availability#cli-capabilities-that-vary-by-provider)
- [Feature availability - Claude Code Docs (English)](https://code.claude.com/docs/en/feature-availability#cli-capabilities-that-vary-by-provider)
- [機能の利用可能性 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/feature-availability#summary-by-provider)
- [Feature availability - Claude Code Docs (English)](https://code.claude.com/docs/en/feature-availability#summary-by-provider)

## 軽微な更新

<!-- light:minor-updates:start -->
今回の差分は **3 ファイル**（`llms.txt`・`llms-full.txt`・見出しマップ）です。`llms.txt` は新しいページの行が 1 行加わり（URL は 240 から 241）、`feature-availability` と `agent-sdk/troubleshooting` の説明文が替わり、末尾の「Indexes」の 11 言語の索引のページ数が 204 から 205 になりました（14 行追加・13 行削除）。`llms-full.txt` では、205 ページのうち **47 ページ**（新しいページを含む）の内容が変わりました。新規の 1 ページと大幅更新の 1 ページを除く **45 ページ**を以下にまとめます。changelog に新しいリリースはなく（収録は 441 リリースのまま、先頭は v2.1.325）、新着情報（whats-new）のページもありません。

`llms-full.txt` の総行数は **128,207 行から 128,554 行へ 347 行増え**ました（生の差分の差し引き 627 − 280 と一致）。生の差分 907 行の内訳は、`agent-sdk/overview` の掲載位置の移動が 182 行（削除 91・追加 91）、新しいページが 151 行、残りの 46 ページが 574 行（追加 385・削除 189）です。`plugins/create` は `llms-full.txt` に 2 回展開されていて、両方の写しに同じ 1 組の置き換えが入っています（写しを両方数えると生の差分と一致します）。書式だけの変更は見当たらず、`setup` のコードフェンスの `theme={null}` の重なり（5 行）も前回から変わっていません。

コードフェンスの外の見出しは、行頭が `#` の見出しだけを数えると 6,112 から 6,138 へ、引用の中の見出しも数えると 6,123 から 6,149 へ、どちらも 26 増えました。加わったのは 28 で、新しいページの 14（ページの題を含む）と、既存のページの 14 です（`errors` 2・`vs-code` 3・`agent-sdk/troubleshooting` 2、`auto-mode-config`・`chrome`・`model-config`・`plugins/mods/troubleshoot`・`sessions`・`tools-reference`・`agent-sdk/typescript` が各 1）。外れたのは 2 つで、`errors` の「Command approved before Claude Code restarted was not run」と `auto-mode-config` の「Route all shell commands through the classifier」です。どちらも改称で、`errors` の加わった 1 つと `auto-mode-config` の加わった 1 つがその新しい名前です。

**新機能**

- Claude Models on Google Cloud (Anthropic managed) のページと関連の記述（`claude-models-on-google-cloud-anthropic-managed` ほか。詳細はハイライト 1 参照）
- Agent SDK の大きなメッセージの対処と TypeScript SDK の `matchDeniedModels()`・`supersedes`（`agent-sdk/troubleshooting`・`agent-sdk/python`・`agent-sdk/typescript`。詳細はハイライト 5 参照）
- **VS Code で Jupyter ノートブックを扱う節ができた**（`vs-code` の新しい h2「Work with Jupyter notebooks」と h3「Re-run edited cells」「Save the notebook before an edit」）。Claude Code は NotebookEdit のツールでノートブックを編集し、コードのセルを置き換えると、ファイルのセルのソースを書き直し、保存された出力と実行回数を消します。NotebookEdit はファイルに書くだけでカーネルにつながないので、カーネルの再起動は要らず、そのセルと、そこで定義した関数や変数を使うセルを実行し直します。拡張機能の `autosave` の設定は NotebookEdit の前には保存しないので、編集を頼む前にノートブックを保存します（`autosave` の説明も「Claude が読み書きする前」から「Read・Edit・Write のツールが動く前」に替わりました）。`tools-reference` の「NotebookEdit tool behavior」にも h3「Replacing a cell clears its saved outputs in the file」ができています — [日本語](https://code.claude.com/docs/ja/vs-code#work-with-jupyter-notebooks) / [English](https://code.claude.com/docs/en/vs-code#work-with-jupyter-notebooks)、[日本語](https://code.claude.com/docs/ja/tools-reference#replacing-a-cell-clears-its-saved-outputs-in-the-file) / [English](https://code.claude.com/docs/en/tools-reference#replacing-a-cell-clears-its-saved-outputs-in-the-file)
- **ゼロデータ保持の組織では Claude Code の Claude in Chrome を使えないと載った**（`chrome` の新しい h3「Chrome availability with HIPAA or zero data retention」・`zero-data-retention` の「What ZDR does not cover」）。Claude Code でゼロデータ保持（ZDR）を有効にした組織では、Owner が **Organization settings > Claude in Chrome** でオンにしても、`--chrome` を渡しても、Claude in Chrome はオフのままで、`/chrome` は `Claude in Chrome is disabled by your organization's policy` と報告します。組織が許すところでは Claude Code の外で拡張機能を使えます。HIPAA の組織での扱いの段落も「Prerequisites」からこの h3 に移りました。`zero-data-retention` の表にも、ブラウザーの拡張機能 Claude in Chrome は ZDR の対象外で、ZDR では Claude Code で使えない、という行が加わっています — [日本語](https://code.claude.com/docs/ja/chrome#chrome-availability-with-hipaa-or-zero-data-retention) / [English](https://code.claude.com/docs/en/chrome#chrome-availability-with-hipaa-or-zero-data-retention)
- **再開のときに渡し直すフラグの節ができた**（`sessions` の新しい h4「Flags to pass again when you resume」）。`claude --continue` か `claude --resume` では、`--mcp-config`・`--plugin-dir`・`--add-dir`（`/add-dir` で加えたディレクトリーも、例: `claude --continue --add-dir ../shared`）・`--settings`・`--fallback-model` のようなフラグを Claude Code が復元しないので、渡し直します。ただし、動いているバックグラウンドのセッションを開き直すときと、止まった後に完全なセッション ID と `--bg` で再開するときは、セッションがフラグを保つので繰り返さない、という注記があります。「Resume a session」の表にも `claude --resume <session-id>` の行が加わりました — [日本語](https://code.claude.com/docs/ja/sessions#flags-to-pass-again-when-you-resume) / [English](https://code.claude.com/docs/en/sessions#flags-to-pass-again-when-you-resume)
- **`ultrathink` が VS Code と Desktop の Code タブでも効くと載り、オフにする変数ができた**（`model-config` の「Use ultrathink for one-off deep reasoning」・`env-vars`）。そのターンを `xhigh` の effort に上げるには、ターミナルのプロンプト（v2.1.311 以降）、VS Code のチャットの欄（v2.1.316 以降、虹色で表示される）、Desktop アプリの Code タブのローカルのセッション（v2.1.316 以降）で入力します。上げられないところの例に Agent Platform と Claude apps gateway が加わりました。`CLAUDE_CODE_DISABLE_ULTRATHINK` を `1` にすると、コンテキストの中の指示を含めてキーワードがオフになります（v2.1.316 以降） — [日本語](https://code.claude.com/docs/ja/model-config#use-ultrathink-for-one-off-deep-reasoning) / [English](https://code.claude.com/docs/en/model-config#use-ultrathink-for-one-off-deep-reasoning)
- **Fable の usage credits の確認に接続したデバイスで答えられるようになった**（`remote-control` の「Limitations」・`model-config` の「Fable and usage credits」・`errors` の「The prompt to confirm went unanswered」）。ターミナルの対話のセッションでは、確認のプロンプトが接続したデバイスにも出ることがあり、そこで答えられます（v2.1.323 以降）。その答えはそのセッションの間続きます。`dialogExpiry` の期限までに誰も答えなければターンが終わり、何も送られません。これまでの「この確認は転送されない」という項目は書き直されました。`errors` には、Remote Control に接続していると、メッセージの最後が `Claude stopped here · send a message to be asked again, or switch models` になりうる、と加わっています（`errors` は日本語版が未追従なので英語版だけ） — [日本語](https://code.claude.com/docs/ja/remote-control#limitations) / [English](https://code.claude.com/docs/en/remote-control#limitations)、[English](https://code.claude.com/docs/en/errors#the-prompt-to-confirm-went-unanswered)
- **agent view の入力で消した文字を `Ctrl+Y` で戻せるようになった**（`agent-view` の「Keyboard shortcuts」「Version history」）。ディスパッチの入力で、最後に消したか `Ctrl+K`・`Ctrl+U`・`Ctrl+W` で削った文字を戻します（agent view を終えるとなくなる）。v2.1.323 以降、`Esc` でプロンプトを消すには 2 回押します — [日本語](https://code.claude.com/docs/ja/agent-view#keyboard-shortcuts) / [English](https://code.claude.com/docs/en/agent-view#keyboard-shortcuts)
- **mod の再読み込みに失敗したときの節ができた**（`plugins/mods/troubleshoot` の新しい h3「`reload failed`」）。`reload failed, the previous version stays loaded: <reason>` なら最後に動いた版が動き続けます（次にすべてのプラグインを再読み込みしてもまだ失敗すれば、その版も外れます）。`reload failed: <reason>` なら `/plugin` を実行し、`mods active` の行がその mod を名指せば最後に動いた版が読み込まれたまま、名指さないか行がなければどの版も読み込まれていません。理由を直して保存し、`reloaded` の行で読み込まれたことを確かめます。同じ内容の段落は「Read the debug log」から外れました — [日本語](https://code.claude.com/docs/ja/plugins/mods/troubleshoot#reload-failed) / [English](https://code.claude.com/docs/en/plugins/mods/troubleshoot#reload-failed)
- **スキル・コマンド・フックの 4,000,000 文字の上限の節ができた**（`errors` の新しい h3「Skill, command, or hook over the 4,000,000-character limit」）。`more than 4,000,000 characters` のメッセージは、スキル・コマンド・プロンプトかエージェントのフックが動かなかったという意味です。長い文を引数に貼ったなら、ファイルに保存して `/clear` を実行し（文は会話に残るため）、そのパスを渡します。Code Mode の外では、上限を超えた `PreToolUse` のプロンプトかエージェントのフックは呼び出しを止めないので、上限のないコマンドのフックを使います。日本語版はまだこの節がなかったので、英語版だけをリンクしています — [English](https://code.claude.com/docs/en/errors#skill-command-or-hook-over-the-4000000-character-limit)

**機能改善**

- 認識できないモデル ID に想定するコンテキストウィンドウと Microsoft Foundry の既定のモデル（`llm-gateway-protocol`・`microsoft-foundry`・`model-config`・`errors`・`statusline`。詳細はハイライト 2 参照）
- server-managed settings のキャッシュの期限（`server-managed-settings`・`errors`・`managed-settings`。詳細はハイライト 3 参照）
- auto mode の設定と、フォールバックのモデルの飛ばし方（`auto-mode-config`・`settings-reference`・`commands`・`model-config`。詳細はハイライト 4 参照）
- プロバイダーごとの機能の表（`feature-availability`。詳細は大幅更新 1 参照）
- **`permissions.denyInsteadOfPrompting` の説明がほかのページにも載った**（`headless`・`permissions`・`sessions`・`vs-code`）。`headless` の「Turn off permission prompts in unattended runs」には、`--permission-prompts none` は 1 回の実行だけ続き、後の実行でも許可のプロンプトを待つ呼び出しを拒むには、ユーザーか managed の設定で `permissions.denyInsteadOfPrompting` を `true` にする、という注記が加わりました。`permissions` の「Permission modes」は、`dontAsk` はそれ自体が権限モードで、このキーは今の権限モードと一緒に働く、と述べます。`sessions` の「Permission mode on resume」と `vs-code` の「Resume past conversations」には、このキーがオンなら Claude が計画を承認に出せないので plan mode を復元しない、という条件が加わっています — [日本語](https://code.claude.com/docs/ja/headless#turn-off-permission-prompts-in-unattended-runs) / [English](https://code.claude.com/docs/en/headless#turn-off-permission-prompts-in-unattended-runs)、[日本語](https://code.claude.com/docs/ja/permissions#permission-modes) / [English](https://code.claude.com/docs/en/permissions#permission-modes)
- **モデルの設定のそのほかの改訂**（`model-config`・`settings-reference`）。「Setting your model」に、Anthropic API で `claude-opus-4-1` のような Claude Opus 4 か Opus 4.1 の ID で始めたセッションは既定で `opus` が選ぶモデルで動く、という注記が加わりました。「Surface coverage」の表では、server-managed settings は Claude Tag のセッションと、Amazon Bedrock か Agent Platform を使うセルフホストのランナーのセッションには届かない、となりました。`fallbackModel` の例も `claude-haiku-4-5` から `claude-haiku-5-5` に替わっています — [日本語](https://code.claude.com/docs/ja/model-config#setting-your-model) / [English](https://code.claude.com/docs/en/model-config#setting-your-model)
- **「Find your error」の表に 10 行が加わった**（`errors`）。新しい 4,000,000 文字の節と Fable の確認の `Claude stopped here` のほか、`Remote Control didn't finish connecting`（`remote-control` の「Start a Remote Control session」へ）、`Unable to fetch your privacy settings at this time`（claude.ai のプライバシーの設定へ）、`NODE_EXTRA_CA_CERTS` のファイルの証明書を一部か全部読めなかったときの 2 つのメッセージ（`network-config` の「Custom CA certificates」へ）、`Not uploading this working tree` のほかの原因と `Git will not work in this checkout because its folder, or the .git in it, belongs to another user`（`claude-code-on-the-web` の「Send local repositories without GitHub」へ）、`credential store on this machine holds a symbolic link inside it`（`plugin-evals` の「Grant tools」へ）、`is not added on this machine, so your organization's marketplace policy keeps its plugins off`（`plugins/install` の「Add a marketplace」へ）、`A mod's http.fetch hook stopped this request`（`plugins/mods/overview` の「Turn mods on or off」へ）、`declares type "claudeai-proxy", which only claude.ai connectors use`（MCP の設定からその項目を外す）の行です。確認のメッセージの区切りは v2.1.324 から `—` ではなく `·` になり、h3「Command approved before Claude Code restarted was not run」は「Approved command was not run after Claude Code restarted」に改称され、メッセージの文から「The command was approved before Claude Code restarted, and」が外れました（表の行は v2.1.323 から、と述べる）。日本語版は未追従なので英語版だけをリンクしています — [English](https://code.claude.com/docs/en/errors#find-your-error)、[English](https://code.claude.com/docs/en/errors#command-approved-before-a-restart-was-not-run)
- **フックの JSON の出力と結果の書き換えの説明が改められた**（`hooks`・`agent-sdk/python`）。「JSON output」の表で、`continue` を `false` にしても `PreToolUse` のツールの呼び出しは止まらないので、止めるには `permissionDecision: "deny"` も返す、となり、`suppressOutput` は「効果がない」だけになりました。`continue` の停止は、許可の確認が `PreToolUse` の呼び出しを拒んだときには当たらない、とも加わっています。`PostToolUse` で書き換えられるのは成功した呼び出しの結果で、`PostToolUseFailure` は結果を書き換えられないので、失敗したコマンドの出力はそのまま Claude に届きます。「Exit code 0」と「Other exit codes」の説明も短くなり、「Hooks in skills and agents」の例のコマンドは `'"${CLAUDE_PROJECT_DIR}"/scripts/security-check.sh'` になりました — [日本語](https://code.claude.com/docs/ja/hooks#json-output) / [English](https://code.claude.com/docs/en/hooks#json-output)
- **フックのガイドの例と確かめ方が改められた**（`hooks-guide`・`plugins/troubleshooting`・`plugins/create`・`debug-your-config`）。「Filter hooks with matchers」のタブ「Log every Bash command」は「Log successful Bash commands」になり、`PostToolUse` はコマンドが成功した後に発火する、と言い換えられました。HTTP フックの例も成功したツールの呼び出しを送るものになっています。「Check what a hook did」は、`Failed with non-blocking status code:` の付いた `<hook name> hook error` の通知はフックが操作を止めなかったという意味で、`Notification` のようなイベントのコマンドのフックが失敗してもこの通知は出ない、と述べます。「Hook output」の終了コードの細かい場合分けは `hooks` の「Exit code output」への案内に替わりました。`plugins/troubleshooting` と `plugins/create` は、デバッグのログを先にオンにしてからイベントを起こす、という手順になりました。`debug-your-config` を含む 3 ページで、ログが何を記録するか（どのフックが当たったか・終了コード・出力）の説明が外れています — [日本語](https://code.claude.com/docs/ja/hooks-guide#check-what-a-hook-did) / [English](https://code.claude.com/docs/en/hooks-guide#check-what-a-hook-did)
- **スキルとカスタムコマンドの呼び出しの説明が改められた**（`skills`・`tools-reference`・`permissions`）。冒頭の「Custom commands have been merged into skills」は、Claude は入力しなくても既存のコマンドを呼び出せる、Claude が自分で呼ばないようにするにはコマンドのファイルのフロントマターに `disable-model-invocation: true` を加える、スクリプトのような補助のファイルが要るならスキルに変える（`.claude/commands/deploy.md` を `.claude/skills/deploy/SKILL.md` に移しても `/deploy` のまま）、という説明になりました。「Control who invokes a skill」では、メッセージに `/deploy` が句読点の付かない独立した語としてないのに Claude が試すと止められる、となり、表の「Description always in context」は「Description in context」になりました。「Restrict Claude's skill access」には、allow のルールを加えても Claude は名指したスキルに限られない、と加わり、例のコメントも「# Allow rules: skip the prompt」になっています。`tools-reference` の `Skill` の行は、`allowed-tools`・`disallowed-tools`・`hooks` を設定したスキルではプロンプトが出うる、として許可の列が「Some skills」になりました。claude.ai から同期したスキルの本文の扱いも「ターミナルか VS Code のセッションでは」と言い換えられています — [日本語](https://code.claude.com/docs/ja/skills#control-who-invokes-a-skill) / [English](https://code.claude.com/docs/en/skills#control-who-invokes-a-skill)
- **同じセッションを同時に再開したときの注意が載った**（`sessions` の「Branch a session」「Name your sessions」）。2 つのターミナルか 2 つの `claude -p` で同時に同じセッションを再開すると、どちらも 1 つのトランスクリプトに書き、後で再開したときに片方のメッセージが欠けうるので、両方の会話を残すにはそれぞれの `claude` のコマンドに `--fork-session` を付けます。`CLAUDE_CODE_DISABLE_TERMINAL_TITLE` を `1` にすると、ターミナルと Agent SDK のセッションには生成したタイトルが付かない、とも加わりました — [日本語](https://code.claude.com/docs/ja/sessions#branch-a-session) / [English](https://code.claude.com/docs/en/sessions#branch-a-session)
- **バックグラウンドにしたときアーティファクトへの自動の返信は止まる、となった**（`agent-view` の「What carries over when you background」「Backgrounding shows a `Background this session?` dialog」）。引き継がれるものの一覧からアーティファクトのコメントへの Claude の自動の返信が外れ、ダイアログの説明でも、その返信はバックグラウンドにすると止まる、となりました（これまでは、バックグラウンドのセッションで続く、としていました）。「Opening a session says the conversation is already open」も、2 つのメッセージごとに、別のプロセス（`claude -p` の実行や再開したターミナル）か別のバックグラウンドのセッションが会話を開いている、という説明に書き直されています — [日本語](https://code.claude.com/docs/ja/agent-view#what-carries-over-when-you-background) / [English](https://code.claude.com/docs/en/agent-view#what-carries-over-when-you-background)
- **Remote Control の認証情報の取得の失敗の調べ方が替わった**（`remote-control`）。「"Remote credentials fetch failed"」では、`claude remote-control --verbose` ではなく、`claude --remote-control --debug-file claude-debug.log` でデバッグのログ付きのセッションを始め、ログで `code-session` を探します。サインインしていない場合の項目は外れ、セッションの作成の失敗も同じ検索でエラーを探す、となりました。接続したデバイスの effort の操作が `CLAUDE_CODE_EFFORT_LEVEL` と違う値を拒む、という文が外れ、サーバーモードの再起動は「Resume sessions after stopping the server」への案内に、`/usage-credits` の制限は請求の権限のない Team と Enterprise のメンバーに限られました — [日本語](https://code.claude.com/docs/ja/remote-control#troubleshooting) / [English](https://code.claude.com/docs/en/remote-control#troubleshooting)
- **プロジェクトの MCP サーバーの承認をやり直すコマンドが載った**（`debug-your-config` の「Check MCP servers」「Check common causes」・`mcp-quickstart` の「Edit .mcp.json directly」）。承認のプロンプトを閉じてしまったら、`/mcp` で承認するのではなく、`claude mcp reset-project-choices` を実行して Claude Code を再起動するとプロンプトがまた出ます（すべてのプロジェクトのサーバーについてもう一度尋ねる） — [日本語](https://code.claude.com/docs/ja/debug-your-config#check-mcp-servers) / [English](https://code.claude.com/docs/en/debug-your-config#check-mcp-servers)
- **見えない文字を外したときの通知が 2 通りになった**（`interactive-mode` の「Invisible characters in prompts」・`terminal-config`）。`Removed 3 invisible characters from your prompt` なら、入力の欄が空のときはその文字を外して送られ、プロンプトが残っていれば送られていないのでもう一度 Enter を押します。`Removed 3 invisible characters · review and press Enter to send` なら何も送られていないので、外した後のプロンプトを読んで Enter を押します。これまでは、外したら Enter は何も送らない、としていました — [日本語](https://code.claude.com/docs/ja/interactive-mode#invisible-characters-in-prompts) / [English](https://code.claude.com/docs/en/interactive-mode#invisible-characters-in-prompts)
- **Anthropic がホストする環境では `sandbox.failIfUnavailable` があってもセッションが始まる、と載った**（`settings-reference` の「`sandbox.failIfUnavailable`」と「Settings index」・`settings-example`）。そうしたセッションは警告付きで始まり、`sandbox.filesystem` と `sandbox.network` のルールを適用しません — [日本語](https://code.claude.com/docs/ja/settings-reference#sandbox-failifunavailable) / [English](https://code.claude.com/docs/en/settings-reference#sandbox-failifunavailable)
- **mod の `$.model` の呼び出しの `marketplace.name` が載った**（`monitoring-usage` の「API request event」「API error event」）。公式のマーケットプレイスと組み込みのバンドルの外の mod が `$.model` を呼ぶと、`marketplace.name` も付き、`OTEL_LOG_TOOL_DETAILS=1` にしない限り `"third-party"` に伏せられます。Desktop の SSH のセッションの項目は、デバッグのログが無視した変数を「名指しうる」に改められました — [日本語](https://code.claude.com/docs/ja/monitoring-usage#api-request-event) / [English](https://code.claude.com/docs/en/monitoring-usage#api-request-event)
- **Agent Platform の fast mode の拒否のメッセージが替わった**（`fast-mode` の「Use fast mode on Agent Platform」）。Agent Platform が fast mode の要求に 403 か 404 で答えたときのメッセージは `Fast mode paused: your cloud provider refused a fast request · trying again in 30m` で、v2.1.323 以降が要ります（これまでは `Fast mode was refused for this project · trying again in 30m`） — [日本語](https://code.claude.com/docs/ja/fast-mode#use-fast-mode-on-agent-platform) / [English](https://code.claude.com/docs/en/fast-mode#use-fast-mode-on-agent-platform)
- **サードパーティのプロバイダーでも Desktop のペインを最小化できると載った**（`desktop` の「Minimize a pane」）。**Minimize** のボタンは Claude Desktop v4.0.0 以降が要り、サードパーティのプロバイダーでは v5.11492.0 以降が要ります（これまでは Claude のアカウントが要る、としていました） — [日本語](https://code.claude.com/docs/ja/desktop#minimize-a-pane) / [English](https://code.claude.com/docs/en/desktop#minimize-a-pane)
- **mod の組み込みのガードのメッセージが替わった**（`plugins/mods/troubleshoot` の「Messages from the built-in guard」ほか）。mod が承認した呼び出しの確認にガードが失敗したときのメッセージは `the rules and hooks in your settings could not be checked for this call, so it is refused` になり（これまでは `the deny rules in your settings could not be checked`）、管理者が設定するオプションを名指すのは「一部の」メッセージ、となりました — [日本語](https://code.claude.com/docs/ja/plugins/mods/troubleshoot#messages-from-the-built-in-guard) / [English](https://code.claude.com/docs/en/plugins/mods/troubleshoot#messages-from-the-built-in-guard)
- **コマンドの説明が短くなった**（`commands` の「All commands」）。`/add-dir` は、Claude の応答中に実行すると、追加を確かめた後の Claude の次のツールの呼び出しがそのディレクトリーを使える、という説明になり、v2.1.234 より前の扱いの文が外れました。`/config` の例は `/config verbose=true` になり、確認の要る設定をオフにはできる、という言葉が外れています — [日本語](https://code.claude.com/docs/ja/commands#all-commands) / [English](https://code.claude.com/docs/en/commands#all-commands)
- **Claude apps gateway のポリシーの `code` の設定の例外が載った**（`claude-apps-gateway-config` の「Claude Desktop overlay」の h5「Apply `code` settings in the Code tab」）。ポリシーの `code` のキーの設定は、一部のプロバイダーとモデルの変数を除いて Code タブに当たる、となり、`desktop` の「Managed settings」へリンクしています — [日本語](https://code.claude.com/docs/ja/claude-apps-gateway-config#claude-desktop-overlay) / [English](https://code.claude.com/docs/en/claude-apps-gateway-config#claude-desktop-overlay)

**その他**

- **`agent-sdk/overview` の掲載位置が移った**。`llms-full.txt` の中で `advisor` の後ろから `agent-sdk/observability` の後ろへ移りました（182 行の削除と追加はこの移動の分で、ページの内容は変わっていません）。`llms.txt` の並びは変わっていません
- **字句の小さな修正**: `best-practices`（auto mode の項目から「安全に」と分類器の説明が外れ、worktree を消すのは「Claude Code が git で作ったもの」になった）、`mcp`（MCP タスクを止める前にサーバーを再接続するのは取り消しの要求を送るため、止めたタスクはもう追えない、という言い方に）、`hooks`（「How a hook resolves」の例の説明が「破壊的なシェルのコマンド」から「`rm -rf` のコマンド」に、`if` の説明が「サブコマンドに分けられないとき」に。「WorktreeRemove input」からは、worktree はディスクに残りフックのコマンドと stderr はデバッグのログに行く、という項目が外れた）、`headless`（「Give a long subagent command more time」の、バックグラウンドに移ったコマンドは動き続ける、という言葉が外れた）、`hooks-guide`（同じ言い換え）、`env-vars`（`CLAUDE_CODE_DISABLE_NONSTREAMING_FALLBACK` の説明が短くなった）、`settings-reference`（「How `env` values interact with your shell」の言い方）、`advisor`（要件の言い方。内容はハイライト 1）、`managed-settings`（ハイライト 3）、`third-party-integrations`（ハイライト 1）
- **`artifacts` の「Page constraints」から「Single page」の行が外れた**。相対リンクは解決されないので、Claude は複数の節の内容にページの中のアンカーを使う、という行です
<!-- light:minor-updates:end -->

見出しマップ（`en/claude_code_docs_map.md`）は、更新時刻が 2026年11月14日 04:30:43 UTC から 2026年11月14日 16:52:20 UTC に替わり、31 行が加わり 3 行が外れました（6,590 行から 6,618 行）。加わったのは、`llms-full.txt` に加わった既存のページの 14 の見出し（`errors` と `auto-mode-config` の改称後の名前を含む）と、新しいページの項目（見出しの行と 13 の見出しと空行 2 行）と、新しいスタンプです。外れたのは 2 つの改称前の見出しと古いスタンプです。今回、見出しマップにだけ先に載った見出しはありません。

**参考リンクについて**: 日本語版は、今回リンクを付けたページの HTML を取得し、新しい節の id があるか、今回の差分で出入りしたコードの字句（変数名・版の数字・パス・リンク先・メッセージの文字列。base と head の `llms-full.txt` で数が違うものだけ）が英語版と同じだけあるかで、今回の内容になっているかを確かめました。新しいページを含めて今回の内容になっていましたが、`errors` だけはまだ新しい節も新しい表の行もなかったので、英語版だけをリンクしています。`best-practices`・`mcp`・`settings-example`・`terminal-config`・`plugins/create` は地の文の言い換えだけで字句による判定ができないので、リンクを付けていません。アンカーは英語版・日本語版の HTML の見出しの id で確かめました。改称した見出しは旧い id のままで、`auto-mode-config` の「Suspend shell allow rules」は `#route-all-shell-commands-through-the-classifier`、`errors` の「Approved command was not run after Claude Code restarted」は `#command-approved-before-a-restart-was-not-run` です。id に曲がったアポストロフィや引用符が入るもの（新しいページの「Claude Code features that aren't available」、`remote-control` の「"Remote credentials fetch failed"」）と、HTML の id がない h5（`claude-apps-gateway-config` の「Apply `code` settings in the Code tab」）は、親の節を指しています。**changelog ページへのリンクは、本サマリの方針どおり付けていません。**

## 新着情報

<!-- light:whats-new:start -->
（今回の差分に新着情報（`whats-new/`）のページはありません。head の `llms.txt`・`llms-full.txt`・見出しマップにも whats-new のページは載っていません）
<!-- light:whats-new:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-11-13.md](./archives/latest/2026-11-13.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-11-13.md](./archives/latest-detail/2026-11-13.md)

<!--
base_commit: 1e8d14825866e74000053b24496de73f02e2e71f
head_commit: 996d55263d4545284c549171f13940b746cfa3fe
generated_at_full: 2026-11-15T15:12:21+09:00
-->
