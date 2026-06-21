---
対象期間: 2026年06月17日 〜 2026年06月20日
作成日: 2026-06-20
---

# Claude Code 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
今回はガイド・リファレンス各ページが v2.1.179〜v2.1.183 の機能に追従し、新規ページ「アーティファクト」の追加と changelog への v2.1.183（2026年06月19日）追加が中心です。主要な新機能 5 件をハイライトとして整理します。

主要なものを以下に挙げます。

1. セッション出力を claude.ai 上の限定公開・対話的ページとして公開・共有できる新機能「アーティファクト」が追加された（ベータ／Team・Enterprise プラン）
2. エージェントチームの操作がエージェントパネル（上下矢印＋Enter）に刷新され、`teammateMode` の既定が `auto` から `in-process` に変更された（v2.1.179）
3. `disableClaudeAiConnectors` 設定が追加され、claude.ai コネクタを設定スコープ単位で一括無効化できるようになった（v2.1.182）
4. skills ドキュメントに「スキルの評価と改善」が追加され、`skill-creator` プラグインで評価ループ（ベンチマーク・A/B 比較・説明調整）を自動化できるようになった
5. 自動モードの分類器が破壊的な git コマンドや `terraform`／`pulumi`／`cdk` の `destroy` などをデフォルトでブロックするようになった（v2.1.183）
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**セッション出力をアーティファクトとして共有**](#1-セッション出力をアーティファクトとして共有):  
  セッションの成果物を claude.ai 上の限定公開 URL に「アーティファクト」（ライブで対話的な Web ページ）として公開し、組織内で共有できる新機能が追加された。ベータ機能で、Team または Enterprise プランかつ `/login` 認証のセッションが必要。
2. [**エージェントチームの操作画面とデフォルト表示モードの刷新**](#2-エージェントチームの操作画面とデフォルト表示モードの刷新):  
  チームメイトの操作がプロンプト下の「エージェントパネル」（上下矢印で選択・Enter で表示と送信・`x` で停止）に刷新され、`teammateMode` の既定が `auto` から `in-process` へ変更された（v2.1.179）。アイドルのチームメイト行は 30 秒後に自動で隠れる。
3. [**claude.aiコネクタの一括無効化設定**](#3-claudeaiコネクタの一括無効化設定):  
  `disableClaudeAiConnectors` 設定が追加され（v2.1.182）、claude.ai 由来の MCP コネクタを任意の設定スコープでまとめて無効化できるようになった。any-source-true セマンティクスで、いずれかのソースの `true` が優先される。
4. [**skill-creator によるスキル評価の自動化**](#4-skill-creator-によるスキル評価の自動化):  
  skills ドキュメントに「スキルの評価と改善」セクションが追加された。`skill-creator` プラグインがベースライン比較ループ（テストケース・分離実行・採点・ベンチマーク・バージョン A/B 比較・説明調整）を Claude Code 内で自動化する。
5. [**自動モードの破壊的コマンド保護の拡充**](#5-自動モードの破壊的コマンド保護の拡充):  
  自動モードの分類器が「デフォルトでブロック」する対象に、未コミット変更を破棄しうる破壊的 git コマンド、当該セッション外コミットへの `git commit --amend`、`terraform`／`pulumi`／`cdk`／`terragrunt` の `destroy` を追加した（v2.1.183）。

<!-- light:highlight-list:end -->

## 1. セッション出力をアーティファクトとして共有

Claude Code のセッション成果物を claude.ai 上の限定公開 URL に「アーティファクト」として公開できる新機能が追加されました。アーティファクトは、ブラウザで開く対話的な Web ページで、セッションの進行に合わせてその場で更新されます。ページヘッダーの **Share** から組織内の特定メンバーや全員に共有でき、注釈付き diff による PR ウォークスルー、セッションデータからのダッシュボード、長時間タスクの進捗タイムラインなどに使えます。Claude が成果物に適すると判断したときに自動で公開する場合もあれば、明示的に依頼して作らせることもできます。公開時は許可を求められ（再公開時は再プロンプトなし）、`Ctrl+]` で最新のアーティファクトを再表示できます。ブラウザ自動オープンは `CLAUDE_CODE_ARTIFACT_AUTO_OPEN=0` で抑止できます。

アーティファクトはベータ機能で、利用には Team または Enterprise プラン、`/login`（claude.ai）認証、Anthropic API（Bedrock／Vertex AI／Foundry では不可）、CMEK・HIPAA・ZDR が無効な組織、といった条件をすべて満たす必要があります。各ページはバックエンドを持たない単一の自己完結 HTML で、厳格な CSP により外部リクエスト不可・複数ページ不可・ファイル種別は `.html`／`.htm`／`.md`・レンダリングサイズ 16 MiB 以下といった制約があります。共有は組織内に限定され、外部公開はできません。無効化は `disableArtifact` 設定・`CLAUDE_CODE_DISABLE_ARTIFACT=1` 環境変数・`permissions.deny` への `Artifact` 追加のいずれかで行えます。組織管理者は claude.ai 管理設定から有効化・保持ポリシー・監査ログ・Compliance API による一覧/削除を管理できます。

- [Share session output as artifacts - Claude Code Docs (English)](https://code.claude.com/docs/en/artifacts)

## 2. エージェントチームの操作画面とデフォルト表示モードの刷新

エージェントチームのチームメイト操作が、従来の「Shift+Down でサイクル」から、プロンプト入力欄の下に表示される**エージェントパネル**ベースに刷新されました。パネルでは上下矢印キーでチームメイトを選択し、**Enter** でそのトランスクリプトを開いて直接メッセージを送信、**Escape** で現在のターンを中断、選択中のチームメイトに対し **`x`** で停止できます。あわせて、アイドル状態のチームメイトの行は 30 秒後に自動で隠れ（次のターンで再表示）、隠れている間も実行・宛先指定は維持されます。

表示モードの既定値も変更されました。`teammateMode` の既定は v2.1.179 で `auto` から `in-process` になり、`--teammate-mode` フラグの既定も `in-process` です。これにより、以前は分割ペインで開いていたアップグレード済みセッションも、明示的に `auto` を設定しない限り単一ターミナル内に留まります。分割ペイン（tmux／iTerm2）を使いたい場合は `teammateMode: "auto"` または `--teammate-mode auto` を指定します。なお、この変更を反映した日本語ページは未公開のため、リンクは英語版のみを記載します。

- [Orchestrate teams of Claude Code sessions - Claude Code Docs (English)](https://code.claude.com/docs/en/agent-teams#choose-a-display-mode)

## 3. claude.aiコネクタの一括無効化設定

claude.ai 由来の MCP コネクタをまとめて無効化する `disableClaudeAiConnectors` 設定が追加されました（v2.1.182）。任意の設定スコープで設定でき、any-source-true セマンティクス（いずれかのソースで `true` が優先）を採ります。チェックインしたプロジェクトの `.claude/settings.json` でリポジトリをクラウドコネクタからオプトアウトできますが、プロジェクトレベルの `false` でユーザー／ポリシーレベルの `true` を上書きして再有効化することはできません。`--mcp-config` で明示的に渡したサーバーは影響を受けません。

個別のコネクタだけを無効化したい場合は `deniedMcpServers` に表示名または URL パターンで追加します（例: `serverName` が `"claude.ai Slack"` で Slack コネクタをブロック）。環境変数 `ENABLE_CLAUDEAI_MCP_SERVERS=false` も同等の効果を持ちます。なお、これらはローカルセッション向けのクライアント側設定で、Claude Code on the web のクラウドセッションではコネクタがホストから `--mcp-config` で供給されるため `disableClaudeAiConnectors` は適用されません。この変更を反映した日本語ページは未公開のため、リンクは英語版のみを記載します。

- [Connect Claude Code to tools via MCP - Claude Code Docs (English)](https://code.claude.com/docs/en/mcp#disable-claude-ai-connectors)

## 4. skill-creator によるスキル評価の自動化

skills ドキュメントに「スキルの評価と改善」セクションが追加されました。スキルがトリガーされること自体は「Claude が見つけた」ことを示すに過ぎず、意図どおり動くかを知るには、①あるべきプロンプトで呼び出されるか、②呼び出されたときの出力が期待どおりか、を分けて測る必要があります。確認方法はベースライン比較で、現実的なプロンプトを集め、スキル有効時と無効時をそれぞれ新規セッションで実行して結果を比べます（作成時の残コンテキストが指示の不備を隠さないよう、新規セッションが重要）。

この比較ループを Claude Code 内で自動化するのが `skill-creator` プラグインです（`/plugin install skill-creator@claude-plugins-official` でインストールし、`/reload-plugins` で有効化）。テストケース（`evals/evals.json`）の作成、テストケースごとにサブエージェントを分離実行してトークン数・所要時間を記録、各アサーションの採点（`grading.json`）、スキル有無での合格率・時間・トークンの集計（`benchmark.json`）、2 バージョンのブラインド A/B 比較、トリガー精度を測っての説明文調整、結果を確認する HTML ビューアまでを担います。なお、この内容を反映した日本語ページは未公開のため、リンクは英語版のみを記載します。

- [Extend Claude with skills - Claude Code Docs (English)](https://code.claude.com/docs/en/skills#evaluate-and-iterate-on-a-skill)

## 5. 自動モードの破壊的コマンド保護の拡充

自動モードの分類器が「デフォルトでブロック」する操作が拡充されました（v2.1.183）。新たに、未コミットの変更を破棄するとみなされる破壊的 git コマンド（`git reset --hard`、`git checkout -- .`、`git restore .`、`git clean -fd`、`git stash drop`、`git stash clear`）、HEAD のコミットが当該セッションで作成されたものでない場合の `git commit --amend`、および `terraform destroy`／`pulumi destroy`／`cdk destroy`／`terragrunt destroy` とリソースを破棄するプランの適用が、ユーザーが明示的に依頼しない限りブロックされます。

これらは従来からの「外部エンドポイントへの機密データ送信」「本番デプロイ／マイグレーション」「フォースプッシュや `main` への直接プッシュ」などと並ぶ既定ブロック項目に追加されたものです。日常的な操作が誤ってブロックされる場合は、管理者が `autoMode.environment` 設定で信頼するリポジトリ・バケット・サービスを追加できます。この変更を反映した日本語ページは未公開のため、リンクは英語版のみを記載します。

- [Choose a permission mode - Claude Code Docs (English)](https://code.claude.com/docs/en/permission-modes#what-the-classifier-blocks-by-default)

## 新規追加されたページ

<!-- light:new-pages:start -->
- [**アーティファクトページ（artifacts）**](#1-アーティファクトページartifacts) ([English](https://code.claude.com/docs/en/artifacts)):  
  セッション出力をアーティファクトとして共有する新機能の専用ページ。詳細はハイライト 1 参照。
<!-- light:new-pages:end -->

## 1. アーティファクトページ（artifacts）

新機能「アーティファクト」を解説する新規ページ `artifacts` が追加されました。使いどころ・作成・更新・共有・プロンプトパターン（変更のウォークスルー、選択肢の比較、対話的コントロール、結果のセッションへの戻し、進行中作業のトラッキング）・デザインシステムの適用・ページ制約・利用可否・無効化・組織での管理までを網羅します。機能の詳細はハイライト 1 を参照してください。日本語ページは未公開のため、リンクは英語版のみを記載します。

- [Share session output as artifacts - Claude Code Docs (English)](https://code.claude.com/docs/en/artifacts)

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
- [**エージェントチーム（agent-teams）**](#1-エージェントチームagent-teams) ([English](https://code.claude.com/docs/en/agent-teams#choose-a-display-mode)):  
  チームメイト操作のエージェントパネル化とデフォルト表示モード変更を反映した大規模な記述更新。詳細はハイライト 2 参照。
<!-- light:updated-pages:end -->

## 1. エージェントチーム（agent-teams）

エージェントチームのページが、チームメイト操作のエージェントパネル化（上下矢印・Enter・Escape・`x`）、アイドル行の自動非表示、`teammateMode` の既定変更（`auto`→`in-process`、v2.1.179）を反映して広範に更新されました。「最初のエージェントチームを開始する」「表示モードを選択する」「チームメイトと直接通信する」「トラブルシューティング」など複数セクションにまたがる書き換えです。詳細はハイライト 2 を参照してください。日本語ページは未追従のため、リンクは英語版のみを記載します。

- [Orchestrate teams of Claude Code sessions - Claude Code Docs (English)](https://code.claude.com/docs/en/agent-teams#choose-a-display-mode)

## 軽微な更新

<!-- light:minor-updates:start -->
今回は新規ページ「アーティファクト」の追加と、各リファレンスページの v2.1.179〜v2.1.183 機能反映、changelog への v2.1.183（2026年06月19日）追加が中心です。主要機能はハイライトに挙げたとおりです。それ以外の更新を分類別に示します（特記なき項目は対象期間内のリリース。新しい変更を反映した日本語ページは未追従のため、リンクは英語版のみを記載します）。

**新機能**
- `/config key=value` 構文が拡張され、名前付き短縮キー（`/config theme=dark`、`/config model=sonnet` など）に対応し、`/config --help` で設定可能なキーを一覧できるようになった（v2.1.182）。`-p`（非対話）・Remote Control・モバイル/web からも `key=value` での設定変更が可能。 — [English](https://code.claude.com/docs/en/cli-reference#slash-commands)
- `attribution.sessionUrl` 設定が追加された（v2.1.182、リンク付与自体は v2.1.179 から）。web／Remote Control セッションで作成した commit に `Claude-Session` トレーラー、PR 本文にセッションリンクを付与する。`false` で抑止。あわせて claude-code-on-the-web のセクション名が「Link artifacts back to the session」→「Link output back to the session」に変更された。 — [English](https://code.claude.com/docs/en/settings#attribution-settings)
- スクリーンリーダー対応出力が追加された（v2.1.181）。`--ax-screen-reader` フラグ／`axScreenReader` 設定／`CLAUDE_AX_SCREEN_READER` 環境変数で、装飾枠やアニメーションの無いフラットなテキスト出力（クラシックレンダラ強制）に切り替えられる。 — [English](https://code.claude.com/docs/en/cli-reference#cli-flags)
- 新しい環境変数が追加された: `CLAUDE_CODE_CONNECT_TIMEOUT_MS`（接続・TLS・レスポンスヘッダ段階のタイムアウト、既定 60 秒）、`CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS`（`-p` 終了時にバックグラウンドのサブエージェント／ワークフローを待つ上限、既定 10 分。v2.1.182）、`CLAUDE_CODE_OTEL_DIAG_STDERR`（OpenTelemetry エクスポータの診断エラーを stderr に出力。v2.1.179）。 — [English](https://code.claude.com/docs/en/env-vars)
- `remoteControlAtStartup` 設定が追加され、各対話セッション開始時に Remote Control を自動接続できるようになった。 — [English](https://code.claude.com/docs/en/settings#available-settings)
- CLAUDE.md のインポート解析がコードスパン／フェンスコードブロックをスキップするようになった。パスを取り込まずに言及するにはバッククォートで囲む（`` `@README` `` はリテラル、囲まない `@README` はインポート）。 — [English](https://code.claude.com/docs/en/memory)

**機能改善**
- changelog v2.1.183 由来の改善: 非推奨／自動更新されるモデルを要求した際に警告を表示するようになり（`-p` では stderr に出力、サブエージェント frontmatter の `model` も対象）、`/config` のトグル操作が変更され（Enter・Space で変更、Esc は保存して閉じる）、ロゴ下の起動時「setup issues」行が削除された（設定の問題は `/doctor` か `--debug` で確認）。
- エージェントチームのセットアップが簡素化された（v2.1.178 既存エントリへの追記）。`TeamCreate`／`TeamDelete` ツールが削除され、`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` で各セッションに暗黙の 1 チームができ、Agent ツールの `name` パラメータで直接チームメイトをスポーンできる（`team_name` は受理されるが無視）。
- ネストしたサブエージェントの深さ制限が前景・背景で統一された。従来は「背景は深さ 5 で制限、前景は任意深さ可」だったのを、前景・背景を問わず深さ 5 でそれ以上スポーン不可に変更（説明を修正）。 — [English](https://code.claude.com/docs/en/sub-agents#spawn-nested-subagents)
- `claude mcp get`／`list` の接続状態に `! Connected · tools fetch failed`（接続したがツール一覧の取得に失敗）が追加された（リファレンスのステータス表に反映）。 — [English](https://code.claude.com/docs/en/mcp)
- OpenTelemetry の `api_refusal` イベントに属性が追加された（`query_source`・`speed`・`attempt`・`effort`・`server_fallback_hop`・`has_category`／`category`・`has_explanation`、およびエージェント／スキル／プラグイン／MCP 帰属など）。 — [English](https://code.claude.com/docs/en/monitoring-usage#api-refusal-event)
- ネットワーク許可リストに `*.claudeusercontent.com`（アーティファクト閲覧用。ビューア側ブラウザで必要で CLI 自体には不要）が追加された。 — [English](https://code.claude.com/docs/en/network-config#network-access-requirements)
- Agent SDK の `SDKRateLimitEvent` に `errorCode: "credits_required"`・`canUserPurchaseCredits`・`hasChargeableSavedPaymentMethod` が追加された（claude.ai サブスクの含有枠が尽きクレジット購入が必要な拒否を識別。v2.1.181）。 — [English](https://code.claude.com/docs/en/agent-sdk/typescript)
- `/code-review ultra` が、PR の差分が大きすぎる場合にレビュー実行前にスコープ縮小を促して拒否するようになった。 — [English](https://code.claude.com/docs/en/ultrareview)
- ワークフローのプロジェクト保存が、モノレポで作業ディレクトリからリポジトリルートまでの最も近い既存 `.claude/workflows/` を対象にする旨が明確化された（v2.1.178）。 — [English](https://code.claude.com/docs/en/workflows)
- Zero Data Retention（ZDR）で自動的に無効化される機能の一覧にアーティファクトが追加された。 — [English](https://code.claude.com/docs/en/zero-data-retention)
- Remote Control の接続失敗時の挙動が変更され、失敗理由を通知で表示してフッターの指標を消すようになった（従来は赤い `/rc failed` 指標を残していた）。あわせて `CLAUDE_CLIENT_PRESENCE_FILE`（前回ハイライト済み）によるモバイルプッシュ抑止がリファレンス本文に反映された。 — [English](https://code.claude.com/docs/en/remote-control#mobile-push-notifications)
- macOS サンドボックスの `allowAppleEvents` 設定（前回ハイライト済み）と、`open`／`osascript`／ブラウザ認証フローがエラー `-600` で失敗する件のトラブルシュートが sandboxing／settings に反映された。 — [English](https://code.claude.com/docs/en/sandboxing#troubleshooting)
- プラグインの `skills` フィールドについて、marketplace-root ソース（`source: "./"`）時に特定サブディレクトリを列挙するとそのエントリの読み込み対象が限定される挙動が JSON 例付きで明確化された（plugins-reference／plugin-marketplaces）。 — [English](https://code.claude.com/docs/en/plugins-reference#mcp-servers)
- AWS の `aws configure export-credentials --format process` のフラット出力（`Credentials` 配下にネストせずトップレベルに同じキーを置く形式）も受け付けるようになった（v2.1.181）。 — [English](https://code.claude.com/docs/en/amazon-bedrock)
- フルスクリーンモードでの URL・ファイルパスのオープン操作が変更され、単なるクリックではリンクを開かず、`Cmd`-click（macOS）または `Ctrl`-click（Linux／Windows）が必要になった（v2.1.181、ネイティブターミナル挙動に整合）。 — [English](https://code.claude.com/docs/en/fullscreen#use-the-mouse)
- `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` の説明から、積極的コンパクション対象の例として挙げられていた Remote Control セッションが削除された（env-vars ページの記述更新）。 — [English](https://code.claude.com/docs/en/env-vars)

**バグ修正**

changelog に v2.1.183（2026年06月19日）が追加された。主な修正をリリース単位で示す。

- **v2.1.183**（2026年06月19日）
  - サブエージェントのスポーンとセッションタイトル生成で `thinking.disabled.display: Extra inputs are not permitted` の 400 エラーが出る問題を修正。
  - サブエージェント内で WebSearch が空の結果を返す問題を修正。
  - vim モードでネイティブカーソル有効時、履歴移動後にターミナルカーソルがプロンプト上部に取り残される問題を修正。
  - Windows Terminal でネストしたサブエージェント高負荷時のフルスクリーン TUI 崩れ（ステータスライン混在、スピナー行重複、テキスト融合）を修正。
  - モデルが thinking ブロックのみを返したターンが無出力で完了する問題を修正（1 度だけ再プロンプトするように）。
  - 複数プラグイン有効時にユーザーレベルのスキルがスラッシュコマンド補完に重複表示される問題を修正。
  - 認証が必要な MCP サーバーが headless／SDK モードで auth-stub ツールをモデルに露出する問題を修正。
  - シェルの rc ファイル初期化が遅いと tmux のチームメイトペインが起動しない問題、およびスポーン中の打鍵が新しい tmux ペインに漏れる問題を修正。
  - チームメイトが開始したバックグラウンドタスクが、そのチームメイトのターン終了時に kill される問題を修正。
  - スケジュールタスクと webhook トリガーの配信がキーボード入力として扱われる問題を修正（タスク通知として分類し、auto モードで保留中アクションの承認やセッションタイトル設定をしないように）。
  - フォーカスモードで各応答の下に「Ran N PostToolUse hooks」のタイミング行が表示される問題を修正。
<!-- light:minor-updates:end -->

## 新着情報

<!-- light:whats-new:start -->
- [**2026年06月08日～12日(Week 24)**](#2026年06月08日12日week-24) ([English](https://code.claude.com/docs/en/whats-new/2026-w24)):  
  既存の週間ダイジェストの記述更新。サブエージェントの深さ制限の説明が前景・背景統一（深さ 5）に修正され、"sub-agents" の表記が "subagents" に統一された。
<!-- light:whats-new:end -->

## 2026年06月08日～12日(Week 24)

既存の週間ダイジェスト Week 24 の記述が更新されました。「サブエージェントによるサブエージェント生成」の項で、深さ制限の説明が「背景は深さ 5 で制限、前景は任意深さ可」から「前景・背景を問わずサブエージェントの連鎖は深さ 5 で制限」へと修正されました（リファレンス sub-agents 側の挙動統一に追従）。あわせて本文の "sub-agents" 表記が "subagents" に統一されています。日本語ページは未追従のため、リンクは英語版のみを記載します。

- [Week 24 · June 8–12, 2026 - Claude Code Docs (English)](https://code.claude.com/docs/en/whats-new/2026-w24)

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-06-17.md](./archives/latest/2026-06-17.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-06-17.md](./archives/latest-detail/2026-06-17.md)

<!--
base_commit: 36ebe5ec3ed55ca4d8d65463453e514b6892594d
head_commit: fd2ef0a97668a2c792c7c16e7eee4a5d0a25174d
generated_at_full: 2026-06-21T09:07:34+09:00
-->
