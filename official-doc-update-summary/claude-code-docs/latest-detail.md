---
対象期間: 2026年07月02日 〜 2026年07月03日
作成日: 2026-07-03
---

# Claude Code 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
今回の対象期間は、大規模なリブランド・改称と、これまで changelog 先行だった多数の機能・エラーのドキュメント実体化が中心です。「Google Vertex AI」が「Google Cloud's Agent Platform」へ、Web セッション作成フラグ `--remote` が `--cloud` へ改称され、v2.1.200／v2.1.201 の 2 リリースも加わりました。今回、週刊ダイジェスト「新着情報」の新規追加はありません。

主要なものを以下に挙げます。

1. 「Google Vertex AI」がドキュメント全体で「Google Cloud's Agent Platform」（旧 Vertex AI）へリブランドされた
2. Web（クラウド）セッションを作成する CLI フラグが `--cloud` へ改称され、従来の `--remote` は非推奨エイリアスになった
3. 権限モードの `default` が CLI・IDE 拡張で「Manual」と表示されるようになり（別名 `manual`）、AskUserQuestion ダイアログの自動継続が既定オフになった（v2.1.200）
4. エラーリファレンスに新エラー節が多数追加され、ワークスペース未信頼・モデルID検証・AWS 認証・不完全応答の保持・インストール OOM 等が文書化された
5. Enterprise 管理者向けに「組織デフォルトモデル」と「組織エフォート上限」がドキュメント化された
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**Google Cloud's Agent Platform へのリブランド**](#1-google-clouds-agent-platform-へのリブランド):  
  「Google Vertex AI」がページタイトル・説明・ドキュメントマップ全体で「Google Cloud's Agent Platform（旧 Vertex AI）」へ改称された。ゲートウェイ設定・機能可用性表・GitLab／GitHub CI 例など多数のページに波及するが、機能自体は変わらず名称のみの変更で、URL パス（`/google-vertex-ai`）や環境変数（`CLAUDE_CODE_USE_VERTEX` 等）は据え置き。
2. [**Web セッション作成フラグの改称**](#2-web-セッション作成フラグの改称):  
  Web（クラウド）セッションを作成する CLI フラグが `--remote` から `--cloud` へ改称された。`--cloud` が正式名となり、`--remote` は当面「`--cloud` の非推奨エイリアス」として動作を維持する。`claude-code-on-the-web`・CLI リファレンス・GitHub Enterprise Server ページ・エラー文言などが一斉に `--cloud` 表記へ更新された。
3. [**権限モードの Manual 改称と質問ダイアログの既定変更**](#3-権限モードの-manual-改称と質問ダイアログの既定変更):  
  v2.1.200 で `default` 権限モードが CLI・`claude --help`・VS Code・JetBrains 上で「Manual」と表示されるようになり、値としての別名 `manual`（`--permission-mode manual` / `"defaultMode": "manual"`）も受け付ける。設定値・フック／SDK が受け取る値は引き続き `default`。あわせて AskUserQuestion ダイアログの自動継続が既定オフ（`never`）になり、`askUserQuestionTimeout` 設定または `/config` でオプトインする形に変わった。
4. [**エラーリファレンスの大幅拡充**](#4-エラーリファレンスの大幅拡充):  
  `errors` ページに新エラー節が多数追加された。ワークスペース未信頼（allow ルール無視）、認識されないモデルID、AWS 認証情報の失効／認証失敗、ストリーム途中失敗時の部分応答保持、サブエージェントの API エラーによる早期終了、インストールの OOM 強制終了、`--bg` と `--print` の競合、Remote Control 再接続失敗など。多くは v2.1.198〜200 の changelog 先行項目が正式に文書化されたもの。
5. [**組織デフォルトモデルと組織エフォート上限**](#5-組織デフォルトモデルと組織エフォート上限):  
  Claude Enterprise プランの管理者が claude.ai 管理コンソールから、Claude Code メンバーの既定モデル（組織全体／カスタムロール単位）と、モデル別のエフォート上限をロール単位で設定できることが `model-config` に文書化された。既定モデルは「制限」ではなく開始点で、`--model` 等が優先される。
<!-- light:highlight-list:end -->

## 1. Google Cloud's Agent Platform へのリブランド

「Google Vertex AI」ブランドが、Claude Code ドキュメント全体で **「Google Cloud's Agent Platform」（旧 Vertex AI）** へ改称されました。`llms.txt` のページタイトルが「Claude Code on Google Cloud's Agent Platform」に、説明文も「formerly Vertex AI」を添えた新名称に更新され、ドキュメントマップでも「Sign in with Agent Platform」「Enable Agent Platform API」「Enable auto mode on Bedrock, Agent Platform, or Foundry」などへ一斉に置き換わっています。

波及範囲は広く、Claude apps ゲートウェイ設定（`gateway.yaml` の upstream 説明）、機能可用性表（`feature-availability`）、GitLab CI/CD・GitHub Actions の「Amazon Bedrock and Google Cloud」節や CI ジョブ例、フォールバック設定の説明などが同様に更新されました。一方で **これは名称のみの変更** であり、URL パスは `/google-vertex-ai` のまま、`CLAUDE_CODE_USE_VERTEX`・`ANTHROPIC_VERTEX_PROJECT_ID`・`CLOUD_ML_REGION` などの環境変数や `VERTEX_REGION_CLAUDE_*` の挙動は据え置きです。日本語版 `google-vertex-ai` ページは本サマリ作成時点で旧称「Google Vertex AI」のままのため、日本語リンクは省略しています。

- [日本語](https://code.claude.com/docs/ja/google-vertex-ai) / [Claude Code on Google Cloud's Agent Platform - Claude Code Docs (English)](https://code.claude.com/docs/en/google-vertex-ai)

> リブランドは llms.txt・ドキュメントマップ・原文全文（llms-full）の en 側で反映済みですが、日本語ページ群（`google-vertex-ai` 等）は本サマリ作成時点で「Vertex AI」表記のままです。翻訳追従待ちとして日本語リンクは付けていません。

## 2. Web セッション作成フラグの改称

Web（クラウド）セッションを作成する CLI フラグが `--remote` から **`--cloud`** へ改称されました。`claude --cloud "<task>"` が正式な書き方になり、`claude-code-on-the-web` ページ本文・CLI リファレンス・GitHub Enterprise Server ページ・関連するエラー文言（「Could not create a cloud environment ... when using `--cloud` or ultraplan」）が一斉に `--cloud` 表記へ更新されています。

**後方互換は保たれ**、原文には「The older `--remote` spelling still works as a deprecated alias for `--cloud`」と明記され、CLI リファレンスでも `--remote` は「Deprecated alias for `--cloud`」として掲載されています。あわせて `CCR_FORCE_BUNDLE=1 claude --cloud ...` によるローカルリポジトリのバンドル送信、並列実行、テレポート（`--teleport`／`/teleport`）との対比も `--cloud` 前提で記述し直されました。なお `--remote-control`（ローカル CLI セッションを Web から監視する Remote Control）は無関係で、名称の混同に注意する旨も補足されています。日本語版 `claude-code-on-the-web` ページは本サマリ作成時点でまだ `--remote` 表記のため、日本語リンクは省略しています。

- [Use Claude Code on the web (Move tasks between web and terminal) - Claude Code Docs (English)](https://code.claude.com/docs/en/claude-code-on-the-web#move-tasks-between-web-and-terminal)
- [日本語](https://code.claude.com/docs/ja/cli-reference#cli-flags) / [CLI reference (CLI flags) - Claude Code Docs (English)](https://code.claude.com/docs/en/cli-reference#cli-flags)

> `--cloud`／`--remote` 改称は en 側で反映済みですが、日本語 `claude-code-on-the-web` は本サマリ作成時点で `--remote` 表記のままのため、日本語リンクは省略しています。

## 3. 権限モードの Manual 改称と質問ダイアログの既定変更

v2.1.200 で、権限モードの **`default` が UI 上「Manual」と表示** されるようになりました。CLI・`claude --help`・VS Code／JetBrains 拡張のいずれでも「各アクションを個別に確認する」モードが「Manual」と表記され、値としての別名 `manual` も受け付けます（`claude --permission-mode manual`、`"defaultMode": "manual"`）。ただし **設定値・フック／SDK が受け取る値は引き続き `default`** で、`permission_mode` フィールドや `initialPermissionMode` も `"default"` のまま届くため、`"default"` を判定する既存スクリプトはそのまま動作します。`Shift+Tab` のモード循環表示も「Manual」を先頭に表示するようになりました。

もう一つの変更として、**AskUserQuestion ダイアログの自動継続が既定オフ（`never`）** になりました。v2.1.198／v2.1.199 では 60 秒アイドルで自動継続していましたが、v2.1.200 以降は既定で「回答するまで待つ」挙動になり、自動継続したい場合は `askUserQuestionTimeout` 設定（`60s`／`5m`／`10m`）または `/config` の「Question auto-continue timeout」でオプトインします。カウントダウンは最後の 20 秒で表示され、`CLAUDE_AFK_TIMEOUT_MS`／`CLAUDE_AFK_COUNTDOWN_MS` はデモ・自動テスト用のオーバーライドとして残ります。権限プロンプト（プラン承認を含む）はアイドルで自動解決しません。

- [Permission modes (Permission modes) - Claude Code Docs (English)](https://code.claude.com/docs/en/permission-modes#permission-modes)
- [日本語](https://code.claude.com/docs/ja/settings#available-settings) / [Settings (Available settings) - Claude Code Docs (English)](https://code.claude.com/docs/en/settings#available-settings)

> 本節は主に changelog（v2.1.200）由来で、日本語版 `permission-modes`・`settings` ページは本サマリ作成時点で「Manual」表記・`askUserQuestionTimeout` 既定変更を反映していないため、日本語リンクは省略しています。

## 4. エラーリファレンスの大幅拡充

`errors` ページに、これまで changelog 先行だった挙動を説明する **新エラー節が多数追加** されました。主なものは次のとおりです。

- **不完全応答の保持**（`The response above may be incomplete`）: ストリーム途中でサーバーエラー・接続切断・停滞が起きても、可視出力済みの応答を破棄せず不完全注記付きで保持する（v2.1.199 以降）。
- **サブエージェントの早期終了**（`Agent terminated early due to an API error`）: 使用制限到達やサーバーエラーの再試行枯渇でサブエージェントが打ち切られた際、エラー本文を成果として返さず失敗として親へ報告する（v2.1.199 以降）。
- **AWS 認証系**（`AWS credentials expired or invalid` / `AWS authentication failed`）: `awsAuthRefresh` 設定時の 401／403 に対する復旧手順を明文化（v2.1.198 以降）。
- **認識されないモデルID**（`Model is not a recognized model id`）: SDK `setModel()` や Desktop アプリ経由で不正なモデル文字列を指定した際、リクエスト前にローカルで拒否する（v2.1.200 以降）。
- **ワークスペース未信頼**（`Workspace has not been trusted`）: プロジェクト設定の `permissions.allow`／`additionalDirectories` がワークスペース信頼前のため無視された旨を stderr に警告（v2.1.200 以降）。
- **インストールの OOM 強制終了**（`Installation was killed before it could finish`）: Linux の終了コード 137（OOM killer）等でインストールが中断された理由を説明（v2.1.200 以降）。
- そのほか `Conflict between --bg and --print`、`Couldn't reconnect to your Remote Control session`、ページ全体の再構成（リクエストエラーの導入文更新など）。

このうち、不完全応答・サブエージェント早期終了・AWS 認証系は日本語版 `errors` ページも反映済みですが、v2.1.200 由来のワークスペース未信頼・認識されないモデルID・インストール OOM は本サマリ作成時点で日本語未追従のため、それらは英語リンクのみ掲載します。

- [エラーリファレンス（上記の応答は不完全な可能性があります） - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/errors#the-response-above-may-be-incomplete)
- [Error reference (The response above may be incomplete) - Claude Code Docs (English)](https://code.claude.com/docs/en/errors#the-response-above-may-be-incomplete)
- [エラーリファレンス（API エラーによりエージェントが早期終了） - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/errors#agent-terminated-early-due-to-an-api-error)
- [Error reference (Agent terminated early due to an API error) - Claude Code Docs (English)](https://code.claude.com/docs/en/errors#agent-terminated-early-due-to-an-api-error)
- [Error reference (Workspace has not been trusted) - Claude Code Docs (English)](https://code.claude.com/docs/en/errors#workspace-has-not-been-trusted)
- [Error reference (Model is not a recognized model id) - Claude Code Docs (English)](https://code.claude.com/docs/en/errors#model-is-not-a-recognized-model-id)

## 5. 組織デフォルトモデルと組織エフォート上限

`model-config` に、Claude Enterprise 管理者向けの 2 つの統制機能が文書化されました。

**組織デフォルトモデル**（Organization default model）は、管理者が claude.ai 管理コンソールから Claude Code メンバーの既定モデルを、組織全体またはカスタムロール単位で設定するものです（v2.1.196 以降）。設定すると `/model` ピッカーの Default 行が組織既定モデル名を「Org default」ラベル付きで表示します。これは **制限ではなく開始点** で、`--model`／`ANTHROPIC_MODEL`、管理設定や `--settings` の `model`、ユーザー／プロジェクト／ローカル設定の `model`（`/model` で保存したものを含む）が優先されます。管理者が「ユーザー選択をオーバーライド」に設定した場合のみ、ユーザー／プロジェクト／ローカル設定より優先され、次回起動で組織既定へ戻ります。`availableModels`／`enforceAvailableModels`・組織モデル制限・ゼロデータ保持といった既存の制限チェックも通過します。

**組織エフォート上限**（Organization effort limits）は、ロールごと・モデルごとに最大エフォートレベルを設定するものです（v2.1.195 以降）。上限超のレベルは `/effort` ピッカーに出ず、`--effort`／`/effort` で高いレベルを指定しても上限で実行されます。対話・プレーンテキスト `--print` では要求レベルと適用レベルを示す警告が出ますが、`json`／`stream-json` 出力やバックグラウンドエージェントでは無警告でクランプされます。いずれの機能も Anthropic API 認証セッションにのみ配信され、Amazon Bedrock・Google Cloud's Agent Platform・Microsoft Foundry・Claude Platform on AWS には配信されません（それらでは管理設定の `model` キーや `availableModels` を使用）。

- [モデル設定（組織デフォルトモデル） - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/model-config#organization-default-model)
- [Model configuration (Organization default model) - Claude Code Docs (English)](https://code.claude.com/docs/en/model-config#organization-default-model)
- [モデル設定（組織努力制限） - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/model-config#organization-effort-limits)
- [Model configuration (Organization effort limits) - Claude Code Docs (English)](https://code.claude.com/docs/en/model-config#organization-effort-limits)

## 新規追加されたページ

<!-- light:new-pages:start -->
今回、リファレンス系で新規追加されたページはありません。
<!-- light:new-pages:end -->

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
上記ハイライト以外で、既存ページに実体化した規模の大きい更新は以下の 3 件です。

- [**ワークスペース信頼とプロジェクト allow ルール**](#1-ワークスペース信頼とプロジェクト-allow-ルール) ([English](https://code.claude.com/docs/en/permissions#project-allow-rules-and-workspace-trust)):  
  プロジェクトの `.claude/settings.json` の `permissions.allow`／`additionalDirectories` は、ワークスペース信頼ダイアログを受け入れるまで適用されないという規則が明文化された。親ディレクトリを信頼済みでも入れ子プロジェクトの allow ルールは適用されず、v2.1.196〜199 で誤って無視されていた自分の `.claude/settings.local.json` の扱いが v2.1.200 で v2.1.195 以前の挙動に復元された。
- [**MCP のツール承認強制とルートレベル結合子対応**](#2-mcp-のツール承認強制とルートレベル結合子対応) ([日本語](https://code.claude.com/docs/ja/mcp#require-approval-for-a-specific-tool) / [English](https://code.claude.com/docs/en/mcp#require-approval-for-a-specific-tool)):  
  MCP サーバーが `_meta["anthropic/requiresUserInteraction"]` でツールを「毎回承認必須」にできる仕組み（v2.1.199 以降）と、入力スキーマのルート直下に `anyOf`／`oneOf`／`allOf` を持つツールを Claude Code がフラット化して利用可能に保つ仕組み（v2.1.195 以降）が追加された。
- [**サンドボックスの認証情報マスキング**](#3-サンドボックスの認証情報マスキング) ([日本語](https://code.claude.com/docs/ja/sandboxing#mask-environment-variables) / [English](https://code.claude.com/docs/en/sandboxing#mask-environment-variables)):  
  `sandbox.credentials` の環境変数エントリに `"mode": "mask"` が追加され、認証情報を削除せずセンチネル値に置換し、`injectHosts` 宛のリクエスト時のみプロキシが実値へ差し替える方式が文書化された（v2.1.199 以降、`network.tlsTerminate` 前提）。
<!-- light:updated-pages:end -->

## 1. ワークスペース信頼とプロジェクト allow ルール

`permissions` ページに「Project allow rules and workspace trust」節が追加され、**プロジェクトの `.claude/settings.json` の `permissions.allow` ルールと `permissions.additionalDirectories` は、そのワークスペースの信頼ダイアログを受け入れるまで適用されない**ことが明文化されました。信頼を受け入れるまで Claude Code はルールを読み込むだけで適用せず、信頼ダイアログには付与される allow ルール・追加ディレクトリが一覧表示されます。`deny`／`ask` ルールは制限のみのため影響を受けません。信頼はワークスペース単位（git リポジトリルート、リポジトリ外なら起動ディレクトリ）で保存され、親ディレクトリを信頼済みでも入れ子プロジェクトの allow ルールは適用されません。

`.claude/settings.local.json` は本来自分のファイルなので通常は信頼チェックの対象外ですが、リポジトリが供給し得る場合（git にコミット済み・`.claude` がシンボリックリンク）は信頼チェックを経ます。**v2.1.196〜199 では git リポジトリ外やホーム／`CLAUDE_CONFIG_DIR` 配下で自分の `.claude/settings.local.json` を「リポジトリ供給」と誤判定して allow ルールを無視し stderr 警告を出していた**不具合が、v2.1.200 で v2.1.195 以前の挙動（この 2 ケースは信頼不要）に復元されました。また、親ディレクトリが信頼済みで信頼ダイアログが一度も出ずルール未適用のワークスペースでは、v2.1.200 以降、次回対話起動時に信頼ダイアログが表示されるようになりました。

- [Permissions (Project allow rules and workspace trust) - Claude Code Docs (English)](https://code.claude.com/docs/en/permissions#project-allow-rules-and-workspace-trust)

> 本節は日本語版 `permissions` ページに本サマリ作成時点で未追従（該当見出しが存在しない）のため、日本語リンクは省略しています。関連するエラー文言は `errors#workspace-has-not-been-trusted`（英語）にあります。

## 2. MCP のツール承認強制とルートレベル結合子対応

`mcp` ページに、MCP サーバー作成者向けの 2 つの節が追加されました。

1 つ目の「**特定のツールの承認を要求する**」は、`tools/list` 応答エントリで `_meta["anthropic/requiresUserInteraction"]` を `true` にすると、そのツールを **すべての呼び出しで明示承認必須** にできる仕組みです（v2.1.199 以降）。`acceptEdits`／`auto`／`bypassPermissions` モードでもプロンプトを表示し、「今後は聞かない」も提供せず、allow ルールにマッチしてもスキップしません。`dontAsk` モードでは拒否されます。`--permission-prompt-tool` 経由の `allow` は拒否へ変換され、SDK の `canUseTool` コールバックには到達します。同意・アクセス付与などプロンプト自体が目的のツールが想定用途です。

2 つ目の「**ルートレベルの結合子を持つツール入力スキーマ**」は、入力スキーマのルート直下に `anyOf`／`oneOf`／`allOf` を持つツールへの対応です（v2.1.195 以降）。Claude API はこれらをスキーマルートで受け付けないため、Claude Code がスキーマを単一オブジェクトへフラット化し、どのパラメータ群が同時指定かをツール説明の先頭文で補足します（`allOf` は各分岐の `required` を維持、`anyOf`／`oneOf` は説明文で補足）。スキーマを生成できない環境ではそのツールのみスキップし、他ツールは利用可能に保ちます。

- [MCP を使用して Claude Code をツールに接続する（特定のツールの承認を要求する） - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/mcp#require-approval-for-a-specific-tool)
- [Connect Claude Code to tools via MCP (Require approval for a specific tool) - Claude Code Docs (English)](https://code.claude.com/docs/en/mcp#require-approval-for-a-specific-tool)
- [MCP を使用して Claude Code をツールに接続する（ツール入力スキーマとルートレベルのコンビネータ） - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/mcp#tool-input-schemas-with-a-root-level-combinator)
- [Connect Claude Code to tools via MCP (Tool input schemas with a root-level combinator) - Claude Code Docs (English)](https://code.claude.com/docs/en/mcp#tool-input-schemas-with-a-root-level-combinator)

## 3. サンドボックスの認証情報マスキング

`sandboxing` ページの「認証情報を保護する」節が再構成され、環境変数エントリに新モード **`"mode": "mask"`** が追加されました（v2.1.199 以降）。`deny` が変数を完全に削除して `gh` や `npm` などのツールも壊すのに対し、`mask` は認証情報を保護しつつ、それで認証するツールを動作させ続けます。

`mask` では、サンドボックス化されたコマンドはセッションごとのセンチネル値のみを見て、リクエストが認証情報の `injectHosts`（省略時は `network.allowedDomains` の全ホスト）宛にサンドボックスを離れるとき、サンドボックスプロキシがセンチネルを実値へ差し替えます。プロキシがリクエスト内容を見る必要があるため **`network.tlsTerminate` が前提** で、未設定時はマスキングがフェイルクローズします（センチネルのまま送出され認証失敗、起動時と `/doctor` で警告）。マスキングはプロキシに実値送信を認可するため、ユーザー設定・管理設定・`--settings` からのみ有効で、リポジトリの `.claude/settings.json`／`.claude/settings.local.json` の `mask` エントリ・`tlsTerminate`・`allowPlaintextInject` は無視されます。同一変数が `deny` されている場合は `deny` が優先します。

- [サンドボックス化された Bash ツールを設定する（環境変数をマスクする） - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/sandboxing#mask-environment-variables)
- [Configure the sandboxed Bash tool (Mask environment variables) - Claude Code Docs (English)](https://code.claude.com/docs/en/sandboxing#mask-environment-variables)

## 軽微な更新

<!-- light:minor-updates:start -->
今回の軽微な更新は、v2.1.200／v2.1.201 の 2 リリースに伴う多数のバグ修正と、既存ページへの記述明確化・実体化が中心です。以下に分類して整理します（複数リリースを含むため、識別が必要な項目にはバージョンを併記します）。

**新機能**

- Remote Control に再開系フラグが追加された。`-c`／`--continue`（このディレクトリで開始した直近セッションを再開）、`--session-id <id>`（ID 指定で再開）、`--[no-]create-session-in-dir`（起動時に現在ディレクトリへ 1 セッション事前作成）（v2.1.200） — [日本語](https://code.claude.com/docs/ja/remote-control) / [English](https://code.claude.com/docs/en/remote-control)。

**機能改善**

- Chrome のプランモードで、ページ／ブラウザ状態を読むだけの呼び出しは確認なしで実行し、状態変更呼び出しは承認を求めるようになった。`createIfEmpty`／`clear`／`save_to_disk` など状態変更フラグを伴う読み取りも承認対象で、`browser_batch` は全アクションが読み取り専用のときのみ無確認（v2.1.199） — [日本語](https://code.claude.com/docs/ja/chrome#browser-tools-in-plan-mode) / [English](https://code.claude.com/docs/en/chrome#browser-tools-in-plan-mode)。
- サブエージェント関連の挙動が複数明確化された。API エラー時の親への報告（詳細はハイライト4参照）、`SendMessage` が会話内で名前の指す相手が変わっていないか検証し誤配送を拒否、起動元エージェントからのメッセージを通常のタスク指示として扱う一方で承認や設定変更には決してならない境界（v2.1.198／v2.1.199） — [English](https://code.claude.com/docs/en/sub-agents#api-errors-in-subagents)（日本語版 `sub-agents` ページの該当節は本サマリ作成時点で未確認のため英語リンクのみ掲載）。
- エージェントチーム（実験的機能）のパネル挙動が変わった（v2.1.199）。アイドルの担当者行はパネル全体がアイドルになるまで残り、全員アイドル後 30 秒で非表示になる（次のターンで再表示、非表示中も稼働・宛先指定は可能）。4 人以上が同時にアイドルのときは先頭 3 行以外が「N idle agents」の 1 行に折りたたまれる。担当者（in-process teammate）を表示中はテキスト入力と skills はその担当者へ送られ、組み込みコマンドは lead セッションで実行される。また in-process teammate は自身のサブエージェントを常にフォアグラウンドで実行し、`run_in_background` や `background: true` でバックグラウンド起動を求めるとエラーになる — [日本語](https://code.claude.com/docs/ja/agent-teams) / [English](https://code.claude.com/docs/en/agent-teams)（日本語版 `agent-teams` ページの該当記述は本サマリ作成時点で未確認のため英語リンクのみ掲載）。
- モデル切替の検証が追加された。SDK `setModel()` や Desktop アプリ経由で不正なモデル文字列を指定すると、リクエスト前にローカルで拒否するようになった（v2.1.200、詳細はハイライト4参照） — [日本語](https://code.claude.com/docs/ja/model-config#setting-your-model) / [English](https://code.claude.com/docs/en/model-config#setting-your-model)。
- 管理設定の優先順位の記述が整理され、例外的に「いずれの管理ソースが設定しても尊重されるキー」に `forceRemoteSettingsRefresh` が追加された — [日本語](https://code.claude.com/docs/ja/settings#settings-precedence) / [English](https://code.claude.com/docs/en/settings#settings-precedence)。
- システムプロンプトの帰属ブロックについて、ゲートウェイが `system` 配列を改変するとストリップが効かなくなる条件が詳述された（先頭・単独エントリ維持、崩す場合は `CLAUDE_CODE_ATTRIBUTION_HEADER=0`）。
- `.claude/rules/` の path-scoped ルールが、v2.1.198 以降シンボリックリンク経由でファイルに到達した場合もマッチするようになった旨が追記された。

**バグ修正**

- バックグラウンドセッション／エージェントの多数の不具合を修正（v2.1.200）: sleep/wake 後や停滞セッション再開後の無言停止、停滞後の再生成で Esc キャンセル済みターンの再実行、OS が PID を再利用した stale `daemon.lock` によるバックグラウンドエージェント不起動、再インストールした古いビルドによる daemon 乗っ取り防止（ビルドのタイムスタンプで新しさを判定）、ロスターの一時破損による孤児クリーンアップ無効化・socket 認証トークン喪失など。
- `.claude.json` の `disabledMcpServers`／`enabledMcpServers` が非配列値のとき起動時にクラッシュする不具合を修正（v2.1.200）。
- サブエージェントがテキスト出力前にレート制限で打ち切られた際、クリーンに失敗せず空結果を返す不具合を修正（v2.1.200）。
- `claude agents --plugin-dir <dir>` でフラグが `agents` の後だとプラグインの agents／skills がエージェントビューに出ない不具合、同一リポジトリの git worktree からプロジェクトスコーププラグインが正しく読み込まれない不具合を修正（v2.1.200）。
- `/mcp` サーバー一覧がスクリーンリーダー・拡大鏡向けにフォーカス追跡しない不具合、無音録音時に音声ディクテーションが誤って「Voice connection failed」と表示する不具合、tmux 3.4+ での描画ちらつきを修正（v2.1.200）。
- Claude Sonnet 5 セッションが、ハーネスのリマインダーに会話途中の system ロールを使わなくなった（v2.1.201）。

**その他**

- スクリーンリーダー出力が改善され、装飾グリフの非表示、トランスクリプト記号の短ラベル読み上げ、ネストしたテーブルの `Header: value.` 形式読み上げが行われるようになった（v2.1.200）。
- インストールスクリプトが、システムのメモリ不足でインストールが強制終了された場合に説明を表示するようになった（v2.1.200、詳細はハイライト4・`errors#installation-was-killed-before-it-could-finish` 参照）。
- チェックポイント（Agent SDK）に「File rewinding is not enabled」エラー節が追加され、非対話 rewind でチェックポイント未有効時の対処（`CLAUDE_CODE_ENABLE_SDK_FILE_CHECKPOINTING=true`）が示された。
- ドキュメントマップに複数の新エラー節・新見出しが追加された（`errors` の「Model is not a recognized model id」「Installation was killed before it could finish」「Workspace has not been trusted」「Couldn't reconnect to your Remote Control session」「File rewinding is not enabled」、`settings` の「Project allow rules and workspace trust」など）。いずれも今回、原文全文（llms-full）にも本文が実体化している。
- `llms.txt` のページ説明・タイトルが多数更新された（`google-vertex-ai`・`feature-availability`・ゲートウェイ系の「Agent Platform」化、`claude-code-on-the-web` の `--remote`→`--cloud`、Week 23 ダイジェスト説明の「Agent Platform」化など）。
<!-- light:minor-updates:end -->

## 新着情報

<!-- light:whats-new:start -->
今回、週刊ダイジェスト「新着情報」（`whats-new/`）ページの新規追加はありません。ドキュメントマップにも `whats-new/` の新規エントリ追加はなく、`llms.txt` の Week 23 ダイジェスト説明が「Amazon Bedrock, Google Cloud's Agent Platform, and Microsoft Foundry」へ改称された（リブランドの一環）のみです。
<!-- light:whats-new:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-07-02.md](./archives/latest/2026-07-02.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-07-02.md](./archives/latest-detail/2026-07-02.md)

<!--
base_commit: 331621b2d46b6f0f04b5dc7868b469f76a64d0a4
head_commit: da00f2b5089c533aaf3714238391edee13fa9a25
generated_at_full: 2026-07-04T15:06:19+09:00
-->
