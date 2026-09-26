---
対象期間: 2026年09月24日 〜 2026年09月25日
作成日: 2026-09-25
---

# Claude Code 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
**前回「索引にだけ載り、本文はまだ」と書いたプラグインの新しい 20 ページに、今回は本文が入りました**。`llms-full.txt` の展開ページは 197 から 210 に増え、索引の 210 件とそろいました。総行数は 100,393 行から 103,108 行へ **2,715 行増えています**。changelog には **v2.1.282（86 項目）** が積まれ、前回「changelog に項目がない」と書いた AGENTS.md の制約解除も、v2.1.281 の項目として後から加わりました。

主要なものを以下に挙げます。

1. プラグインの新しい 20 ページに本文が入り、旧 7 ページが本文から消えた
2. v2.1.282 の 86 項目が積まれ、v2.1.281 に AGENTS.md の項目が後から加わった
3. OpenTelemetry の変数がプロジェクト設定とローカル設定から無視されるようになった
4. auto モードのサーバー側レビューの説明が書き直された
5. プロジェクトのスレッドを自分のマシンで動かせるようになった
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**プラグインの新しい 20 ページに本文が入り、旧 7 ページが本文から消えた**](#1-プラグインの新しい-20-ページに本文が入り旧-7-ページが本文から消えた):  
  前回、`llms.txt` と見出しマップにだけ載っていた `/docs/en/plugins/` 配下の **20 ページの本文が、今回 `llms-full.txt` に入りました**（計 6,999 行）。索引から外れていた**旧 7 ページ**（`discover-plugins`・`plugins`・`plugins-reference`・`plugin-marketplaces`・`plugin-dependencies`・`plugin-hints`・`plugin-relevance`、計 4,705 行）の本文は消えました。既存の **53 ページでも、プラグイン関連のリンク先が新しい URL に張り替えられています**。前回「404」と書いた `plugins/overview` の日本語版も、今回は日本語で公開されていました
2. [**v2.1.282 の 86 項目が積まれ、v2.1.281 に AGENTS.md の項目が後から加わった**](#2-v21282-の-86-項目が積まれv21281-に-agentsmd-の項目が後から加わった):  
  changelog に **v2.1.282（2026年09月24日）** が積まれました。**修正 59・変更 11・追加 8・改善 6・更新 2** の計 86 項目です。あわせて、既存の **v2.1.281 に「AGENTS.md を Amazon Bedrock・Google Vertex AI・Microsoft Foundry・LLM ゲートウェイ・テレメトリ無効のセッションでも使えるようにした」という項目が追加**され、v2.1.277 の項目からは「（Bedrock・Vertex・Foundry ではまだ使えない）」の但し書きが消えました。前回ハイライト 2 で「changelog に該当項目が見当たらない」と書いた点が、これで解消しました
3. [**OpenTelemetry の変数がプロジェクト設定とローカル設定から無視されるようになった**](#3-opentelemetry-の変数がプロジェクト設定とローカル設定から無視されるようになった):  
  **v2.1.282 から、リポジトリの `.claude/settings.json` と `.claude/settings.local.json` の `env` に書いた `CLAUDE_CODE_ENABLE_TELEMETRY`・エクスポーターの選択・送信先・内容を記録する `OTEL_LOG_*` などが無視されます**。例外は、`none` や `0` のようにテレメトリを止める値だけです。`settings-reference` に一覧が加わり、`env-vars`・`monitoring-usage`・`settings`・`settings-example` も同じ方針に書き換わりました
4. [**auto モードのサーバー側レビューの説明が書き直された**](#4-auto-モードのサーバー側レビューの説明が書き直された):  
  `permission-modes` の「サーバー側の分類器レビュー」が、**Anthropic API 直結・クラウドプロバイダーや LLM ゲートウェイ・Claude apps gateway の 3 種類の接続ごと**の説明になりました。**v2.1.282 からは、テレメトリを切ったセッションでも既定でサーバーに問い合わせます**。サーバーが判定を返さなかった操作は拒否され、**判定なしが 10 回続くとターンが止まる**ことも明記され、`errors` にこの状況の新しい節が加わりました
5. [**プロジェクトのスレッドを自分のマシンで動かせるようになった**](#5-プロジェクトのスレッドを自分のマシンで動かせるようになった):  
  `claude-projects` で、スレッドの説明が「各スレッドはクラウドセッション」から「**各スレッドは通常はクラウドセッション**」に変わりました。**自分のコンピューターにしかないものが要るタスクは、Remote Control 経由でそのスレッドを自分のマシンで動かすよう Claude に頼めます**。そのマシンには **Claude Code v2.1.280 以降**が必要で、claude.ai の設定で **Require trusted devices** がオンだと使えません
<!-- light:highlight-list:end -->

## 1. プラグインの新しい 20 ページに本文が入り、旧 7 ページが本文から消えた

**前回は索引（`llms.txt`）と見出しマップだけが先に組み替わり、本文（`llms-full.txt`）は旧構成のままでした。今回、本文も新しい構成に追いつきました。**

| | base | head |
|---|---|---|
| 展開ページ数 | 197 | **210**（索引の収録 URL 210 件と一致） |
| `/docs/en/plugins/` 配下 | 0 ページ | **20 ページ・6,999 行** |
| 旧 7 ページ | 4,705 行（`plugin-marketplaces` 1,538・`plugins-reference` 1,537・`discover-plugins` 586・`plugins` 482・`plugin-dependencies` 242・`plugin-relevance` 167・`plugin-hints` 153） | **本文から削除** |

**新しいページは、旧ページの文章を移しただけではありません。** 行単位で比べると、旧 7 ページの文がそのまま残っている箇所は少なく、見出しも大半が新しく付け直されています。各ページの中身は新規追加ページ 1 にまとめました。

### ほかのページのリンクも張り替わった

**既存の 53 ページで、プラグイン関連のリンク先が新しい URL に変わりました。** たとえば `/docs/en/plugins` へのリンクは `/docs/en/plugins/overview` などへ、`/docs/en/plugins-reference#synced-plugins` へのリンクは `/docs/en/plugins/loading#synced-plugins` へ、`/docs/en/discover-plugins#code-intelligence` へのリンクは `/docs/en/plugins/code-intelligence` へ置き換わっています。`channels`・`vs-code`・`workflows`・`statusline` などの 19 ページは、今回の変更がリンクの張り替えだけでした。

### 本文と索引で、まだ呼び名がそろっていない箇所

`llms.txt` の `plugins/publish` の説明文と見出しマップは、公開先を「**Anthropic's directory**」と呼ぶようになりました（マップの見出しも `Submit to the community marketplace` → `Submit to Anthropic's directory`）。一方、**`plugins/publish` の本文の見出しは、まだ `Submit to the community marketplace` のままです**。

- [プラグインの概要 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/plugins/overview)
- [Plugins overview - Claude Code Docs (English)](https://code.claude.com/docs/en/plugins/overview)

## 2. v2.1.282 の 86 項目が積まれ、v2.1.281 に AGENTS.md の項目が後から加わった

**`changelog` の差分は 92 行（追加 91・削除 1）で、収録リリースは 403 から 404 になりました。**

| 種別 | 件数 |
|---|---|
| Fixed（修正） | **59** |
| Changed（変更） | 11 |
| Added（追加） | 8 |
| Improved（改善） | 6 |
| Updated（更新） | 2 |

タグ付きは **`[Claude Tag]` 11・`[Cloud sessions]` 5・`[VSCode]` 4・`Vertex AI:` 1** で、残る **65 件が CLI 本体**です。前回までのクラウドセッション向けタグは `[Claude Code on the web]` でしたが、今回は **`[Cloud sessions]`** になっています。

### 追加（8 件）の主なもの

- **`maxProseWidth` 設定**: 横に広いターミナルで、Claude の文章の幅だけを制限します。表とコードブロックは全幅のままです
- **無視されたテレメトリ変数の通知**: プロジェクトの設定ファイルにある、無視された（またはテレメトリを止めた）テレメトリ変数を、起動時の通知と `/status`・`claude doctor` で一覧します（ハイライト 3）
- **`allowClaudeInChromeWithManagedMcp` 管理設定**: 排他的な `managed-mcp.json` があっても `claude --chrome` を動かせるようにします
- **Claude apps gateway の `store.readiness_grace_seconds`**: データベースのフェイルオーバーのような短い Postgres の停止中も、`/readyz` を ready のまま保てます
- **`[Cloud sessions]`**: Settings › Connectors › GitHub に Claude GitHub App の状態表示が付き、GitHub 以外の Git サーバーのリポジトリには「Open repository」「Open compare page」のリンクが付きました。実行中のクラウドセッションに、フォークの upstream のような**別の GitHub オーナーのリポジトリも追加**できるようになりました

### 変更（11 件）のうち挙動が大きく変わるもの

- **テレメトリを切った Anthropic API 直結のセッションでも、auto モードがサーバー側の分類器を既定で使う**ようになりました（`CLAUDE_CODE_AUTO_MODE_SERVER=0` でオプトアウト。ハイライト 4）
- **プロジェクト設定とローカル設定が、エクスポートを有効にする・送信先を決める・内容を記録する OpenTelemetry 変数を無視する**ようになりました（ハイライト 3）
- **`anthropic-skills` と `claude-ai` の名前空間が、claude.ai から同期したスキル専用になりました**。この名前空間のスキルフォルダー・コマンドファイル・ワークフローコマンドは読み込まれなくなり、この名前で設定した MCP サーバーはスキルとプロンプトを一覧しなくなります（ツールは使えます）。`Skill(anthropic-skills:*)` と `Skill(claude-ai:*)` の許可ルールも、同期スキルだけを対象にします
- **`sandbox.excludedCommands`**: 管理設定や `--settings` で `allowUnsandboxedCommands: false` を設定しているとき、または管理設定で `allowManagedDomainsOnly: true` を設定しているとき、プロジェクト設定とローカル設定のエントリーを無視するようになりました
- **Windows/WSL の管理設定**: 管理者のポリシー（HKLM・`managed-settings.json`）が存在するのに無効または読めないときも、ユーザーが書ける HKCU や WSL の `/etc/claude-code` は適用されなくなりました

### v2.1.281 と v2.1.277 の後追い修正

**既存のリリースにも手が入りました。** v2.1.281 に「**Changed AGENTS.md support to also work on Amazon Bedrock, Google Vertex AI, Microsoft Foundry, LLM gateways, and sessions with telemetry disabled**」が加わり、同版の項目数は 176 から **177** になりました。v2.1.277 の「AGENTS.md support を追加」の項目からは、末尾の「(not yet on Bedrock, Vertex or Foundry)」が削除されました。前回ハイライト 2 は本文の書き方から「制約が外れたのは v2.1.281」と読み取っていましたが、**changelog でもそれが確認できるようになりました**。

**本サマリは方針として changelog ページの URL を掲載しません。** 上記のうち本文ページに対応する記述があるものは、軽微な更新の各項目にリンクを付けています。

## 3. OpenTelemetry の変数がプロジェクト設定とローカル設定から無視されるようになった

**チェックインされた設定ファイルだけで、リポジトリがテレメトリを有効にしたり、送信先を変えたり、プロンプトの内容を記録させたりできないようにする変更です。** `settings-reference` の「`env` で Claude Code が無視する変数」に、次のグループが加わりました（**v2.1.282 以降**）。

| 無視される変数 | 例 |
|---|---|
| テレメトリの有効化 | `CLAUDE_CODE_ENABLE_TELEMETRY`、強化テレメトリ beta の `CLAUDE_CODE_ENHANCED_TELEMETRY_BETA`・`ENABLE_ENHANCED_TELEMETRY_BETA` |
| エクスポーターの選択 | `OTEL_LOGS_EXPORTER`・`OTEL_METRICS_EXPORTER`・`OTEL_TRACES_EXPORTER` |
| 内容の記録 | `OTEL_LOG_USER_PROMPTS`・`OTEL_LOG_ASSISTANT_RESPONSES`・`OTEL_LOG_TOOL_CONTENT`・`OTEL_LOG_TOOL_DETAILS` |
| 送信先と認証 | 名前が `_ENDPOINT`・`_HEADERS`・`_PROTOCOL`・`_CERTIFICATE`・`_CLIENT_KEY`・`_INSECURE` で終わる `OTEL_EXPORTER_OTLP_*`、`OTEL_EXPORTER_PROMETHEUS_HOST`・`_PORT` |

**止める方向の値だけは、プロジェクト設定とローカル設定からも効きます。** 3 つのエクスポーター選択の `none` と、`OTEL_LOG_USER_PROMPTS`・`OTEL_LOG_TOOL_CONTENT`・`OTEL_LOG_TOOL_DETAILS` の `0` などです。これらはユーザー設定の同じ変数より優先されますが、起動時の環境・`--settings` ファイル・管理設定には負けます。一方、`OTEL_RESOURCE_ATTRIBUTES` やエクスポート間隔・タイムアウト・圧縮の変数は、引き続きプロジェクト設定とローカル設定から効きます。

**影響に気づけるよう、通知も用意されました。** ローカルの対話セッションでは起動時に通知が出て、`/status` と `claude doctor` で、どの変数が無視されたか・どれがテレメトリを止めたかを確認できます（名前だけで、値は出ません）。**`-p` の非対話実行と Agent SDK のセッションでは通知が出ない**ため、アップグレード後はコレクターにデータが届き続けているかを確認するよう書かれています。届かない場合は、ユーザー設定・管理設定・ジョブの環境・`--settings` のファイルのいずれかに移します。

周辺のページも同じ方針に書き換わりました。

- **`settings-example`**: チーム共有の `.claude/settings.json` の例から、OpenTelemetry を送る `env` ブロックが削除され、「テレメトリは管理設定か個人の設定に置く」という注意が加わりました
- **`settings`**: 「`.claude/settings.json` をコミットすると権限・フック・テレメトリ・プラグインをそろえられる」から「テレメトリ」が外れました
- **`env-vars`**: `CLAUDE_CODE_ENABLE_TELEMETRY` と `OTEL_LOG_*` の各行に「シェル・ユーザー設定・管理設定で設定する。プロジェクト設定とローカル設定では無視される」が加わりました
- **`monitoring-usage`**: 管理者向け設定の節に、リポジトリの設定ファイルではエクスポーター変数が無視されることが書き加えられました

- [All settings - Claude Code Docs (English)](https://code.claude.com/docs/en/settings-reference#variables-claude-code-ignores-in-env)
- [Monitoring - Claude Code Docs (English)](https://code.claude.com/docs/en/monitoring-usage#administrator-configuration)

## 4. auto モードのサーバー側レビューの説明が書き直された

**`permission-modes` の「サーバー側の分類器レビュー」が、接続の種類ごとの説明に変わりました。** 以前は「Enterprise プランと Claude API のアカウント、クラウドプロバイダー、LLM ゲートウェイでは」とひとまとめにした 1 段落でした。

| 接続 | サーバーに問い合わせる条件 |
|---|---|
| **Anthropic API 直結** | 対話ターミナルのセッションで、全 claude.ai プランと Claude API のアカウントに段階的に展開。Pro・Max・Team は v2.1.271 以降、Enterprise と Claude API は v2.1.278 以降。**v2.1.282 からは、feature flag を取得しないセッション（テレメトリを切った場合など）も、セッションの種類を問わず既定で問い合わせる** |
| **クラウドプロバイダー、LLM ゲートウェイやプロキシ** | Claude Platform on AWS・Amazon Bedrock・Google Cloud の Agent Platform・Microsoft Foundry、`ANTHROPIC_BASE_URL` をゲートウェイに向けた場合。プランを問わず、v2.1.278 以降は既定で問い合わせる |
| **Claude apps gateway にサインインしたセッション** | v2.1.280 以降 |

**サーバーから判定が返らなかったときの扱いも、2 通りに分けて書かれました。**

- **サーバーがそのセッションをレビューしない**（ゲートウェイがレビュー要求や結果を落とす、プラットフォームやリージョンが未対応など）: Claude Code は自前の分類器リクエストにフォールバックします
- **サーバーが特定の操作に判定を返さない**: Claude Code は、レビューされていない操作を実行せずに**拒否**します。**10 回続けて判定がないと、auto モードはターンを止めます**

`errors` に新しい節「**The server returned no safety verdict**」が加わり、拒否メッセージ（`The server-side auto mode classifier gave no verdict (timed out), …`）と停止メッセージ（`Auto mode is unavailable — the server returned no safety verdict for the last 10 responses, …`）、対処（もう一度メッセージを送る、ゲートウェイの設定を確かめる、`CLAUDE_CODE_AUTO_MODE_SERVER=0` にする、auto モードを抜ける）が載りました。**v2.1.280 より前は、判定のない操作をその場で拒否するだけで、ターンを止めることはなかった**とも書かれています。

`CLAUDE_CODE_AUTO_MODE_SERVER` の説明も更新されました。Anthropic API 直結では **v2.1.281 以降**で効き、`1` にすると `-p` や Agent SDK のセッションでもサーバーレビューがオンになります（`CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS=1` を設定していない場合）。`permissions` と `sandboxing` にも、読み取り専用のコマンドやサンドボックス内のコマンドがこのレビューを待つことがある、という一文が加わりました。

- [権限モードを選択する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/permission-modes#server-side-classifier-review)
- [Choose a permission mode - Claude Code Docs (English)](https://code.claude.com/docs/en/permission-modes#server-side-classifier-review)

## 5. プロジェクトのスレッドを自分のマシンで動かせるようになった

**`claude-projects` は差分 100 行（追加 51・削除 49）で、スレッドの前提が「すべてクラウドセッション」から「通常はクラウドセッション」に変わりました。**

- **冒頭の説明**: 「各スレッドはクラウドセッション」が「**各スレッドは通常はクラウドセッション**」になり、「コンピューターにしかないものが要るタスクは、Remote Control 経由でそのスレッドを自分のコンピューターで動かすよう Claude に頼める」が加わりました
- **使い分け**: 「自分のマシンからしか届かないツールやサービスが要る作業は、ローカルセッションを使う」という案内が、「**すべてのタスクが自分のマシンを必要とする作業**は、ローカルセッションを使う」に狭まりました
- **制限事項**: スレッドを自分のマシンで動かすには、作業させるフォルダーを **Remote Control で接続**します。Claude デスクトップアプリの **Settings > Claude Code** で Remote Control をオンにするか、そのフォルダーで `claude remote-control` を実行したままにします。**そのマシンには Claude Code v2.1.280 以降**が必要で、claude.ai の設定で **Require trusted devices** がオンのあいだは、プロジェクトがスレッドを自分のマシンで動かすことはできません
- **用語**: ページ全体で、クラウドに固有の説明（リポジトリのクローン、クラウド環境、プロジェクトメモリの読み込みなど）の主語が「スレッド」から「**クラウドスレッド**」に書き分けられました。「コンテキストを 1 回設定する」の説明からは「リポジトリ」と「メモリ」が外れ、「プロジェクトの指示」だけが残っています

見出しマップには `Run a thread on your own computer` と `Lost contact with your folder` の 2 見出しが加わりましたが、**この 2 つは本文にはまだありません**。

- [Claude がプロジェクトで進行中の作業を調整する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/claude-projects#limitations)
- [Let Claude coordinate ongoing work with Projects - Claude Code Docs (English)](https://code.claude.com/docs/en/claude-projects#limitations)

## 新規追加されたページ

<!-- light:new-pages:start -->
- [**プラグインの新しい 20 ページ**](#1-プラグインの新しい-20-ページ) ([日本語](https://code.claude.com/docs/ja/plugins/overview) / [English](https://code.claude.com/docs/en/plugins/overview)):  
  前回は索引と見出しマップにだけあった `/docs/en/plugins/` 配下の 20 ページに、本文が入りました。**概要・インストール・作成・マーケットプレイス運用・組織管理・トラブルシューティング・リファレンス**の 7 グループです。ここでは本文の実際の構成をもとに、各ページの範囲をまとめています
<!-- light:new-pages:end -->

## 1. プラグインの新しい 20 ページ

**前回サマリの表は、索引の説明文と見出しマップだけから作ったものでした。今回は本文の見出しと行数をもとにまとめ直しています。**「見出し」は本文の `##`・`###` の数（コードフェンス内は除く）です。

| グループ | ページ | 行数 | 見出し | 本文の主な `##` 見出し |
|---|---|---|---|---|
| Plugins | `plugins/overview` | 123 | 8 | プラグインとは何か／マーケットプレイスから入手する／Anthropic のマーケットプレイスとサードパーティの見分け方／インストールスコープ |
| Use plugins | `plugins/install` | 371 | 22 | インストール／マーケットプレイスの追加／インストール済みの管理／更新を保つ |
| Use plugins | `plugins/anthropic-marketplaces` | 86 | 7 | 公式マーケットプレイスでの検索／Anthropic のマーケットプレイスからの閲覧とインストール／サードパーティのマーケットプレイス |
| Use plugins | `plugins/code-intelligence` | 133 | 10 | インストール／Claude が得るもの／推奨ダイアログへの応じ方／トラブルシューティング／公式プラグインがない言語の追加 |
| Use plugins | `plugins/security` | 161 | 11 | プラグインにできること／Anthropic のマーケットプレイスを名前で見分ける／インストール前の確認／拒否や警告が出るとき |
| Create plugins | `plugins/create` | 375 | 15 | プラグインを使うべきとき／最初のプラグイン／マーケットプレイスなしで開発する／テストとデバッグ／既存の `.claude/` 構成の変換 |
| Create plugins | `plugins/components` | 679 | 18 | ディレクトリの探索／コンポーネントの種類ごとの追加／設定値をユーザーに尋ねる／パスの参照とデータの保存 |
| Create plugins | `plugins/dependencies` | 216 | 13 | 依存の宣言／他から依存されるプラグインのリリース／ユーザー側での依存の振る舞い |
| Create plugins | `plugins/publish` | 175 | 16 | 配布方法の選択／リリースの準備／マーケットプレイスなしで共有する／自前のマーケットプレイスで公開する／コミュニティマーケットプレイスへの提出 |
| Create plugins | `plugins/measure` | 164 | 13 | プラグインのコストの計測／使われているかの確認／組織全体での計測 |
| Create plugins | `plugins/cli-hints` | 123 | 5 | ヒントの出し方／ヒントの形式／プロンプトが出る条件／ユーザーに見える表示 |
| Run a marketplace | `plugins/create-marketplace` | 222 | 13 | マーケットプレイスの作成／プラグインエントリーの追加と規則／プラグインソースの選択／検証とテスト |
| Run a marketplace | `plugins/host-marketplace` | 395 | 30 | ホスト／組織設定での配布／非公開マーケットプレイスへのアクセス付与／全社展開／リリースチャネル／改名と削除／アーカイブのダウンロード認証 |
| Run a marketplace | `plugins/relevance` | 220 | 9 | 関連性の仕組み／エントリーへの `relevance` の追加／フィールドリファレンス／管理設定での有効化 |
| Manage plugins for your organization | `plugins/org` | 399 | 23 | 事前インストールと必須化／コンテナと CI への事前配置／インストールできるものの制限／更新ポリシー／監査とレビュー |
| Troubleshooting | `plugins/troubleshooting` | 905 | 67 | `/plugin` が動く場所／マーケットプレイスの追加／インストール／インストール後に動かない／作成／ホスト／組織によるブロック |
| Troubleshooting | `plugins/loading` | 363 | 22 | どの段階まで進んだか／読み込み元／有効化している設定ファイル／ディスク上の場所／バージョンと更新／名前の衝突 |
| Reference | `plugins/manifest-reference` | 637 | 35 | マニフェストファイル／フィールド／コンポーネントのパス形式とパス規則／ユーザー設定／チャネル／環境変数／標準レイアウト |
| Reference | `plugins/marketplace-reference` | 474 | 22 | マーケットプレイスファイル／トップレベルのフィールド／プラグインエントリー／プラグインソース／マーケットプレイスソース／検証メッセージ |
| Reference | `plugins/cli-reference` | 778 | 26 | `claude plugin` コマンド／`claude plugin marketplace` コマンド／セッション内の `/plugin`／`/reload-plugins`／1 セッションだけ読み込むフラグ |

**最も大きいのは `plugins/troubleshooting`（905 行・67 見出し）**で、見出しの大半は `Marketplace "claude-plugins-official" not found` や `Git clone timed out after 120s` のようなエラーメッセージそのものです。旧ページで同様の内容を扱っていた `plugin-marketplaces` と `plugins-reference` は、いずれも約 1,540 行ありました。

**旧ページにあった節の一部は、新しいページの節へ移ったとみられます。** 他ページのリンクの張り替えを見ると、たとえば `plugin-marketplaces#managed-marketplace-restrictions` は `plugins/org#restrict-what-users-can-install` に、`plugins-reference#synced-plugins` は `plugins/loading#synced-plugins` に、`discover-plugins#apply-plugin-changes-without-restarting` は `plugins/cli-reference#reload-plugins` に置き換えられています。

**日本語版は、`plugins/overview` が日本語で公開されていることを確認しました**（前回は 404 でした）。`llms.txt` の日本語インデックスも 196 ページから 209 ページに増えています。ほかの 19 ページの日本語版は確認していないため、ここでは概要ページのみ日本語リンクを付けています。

- [プラグインの概要 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/plugins/overview)
- [Plugins overview - Claude Code Docs (English)](https://code.claude.com/docs/en/plugins/overview)
- [Troubleshoot plugins - Claude Code Docs (English)](https://code.claude.com/docs/en/plugins/troubleshooting)

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
- [**Environment variables**](#1-environment-variables) ([English](https://code.claude.com/docs/en/env-vars#variables)):  
  差分 746 行の大半は表の桁揃えです。実質的な変更は、テレメトリ変数がプロジェクト設定とローカル設定で無視されることの追記、`CLAUDE_CODE_AUTO_MODE_SERVER` の説明の更新、`CLAUDE_CODE_RESUME_PROMPT` の適用範囲の拡大などです
- [**Test plugins with evals**](#2-test-plugins-with-evals) ([日本語](https://code.claude.com/docs/ja/plugin-evals#troubleshooting) / [English](https://code.claude.com/docs/en/plugin-evals#troubleshooting)):  
  段落の多くが箇条書きに組み直されました。`CI` 環境変数が真のときは信頼の確認ができずに拒否されること、ベースライン実行でプラグインのエージェントが見つからないときの節などが加わりました
- [**All settings**](#3-all-settings) ([English](https://code.claude.com/docs/en/settings-reference#variables-claude-code-ignores-in-env)):  
  `env` で無視される変数にテレメトリのグループが加わったほか、`attribution` に `false` を書けること、マーケットプレイスの `hostPattern`・`pathPattern` の照合方法などが更新されました
- [**Error reference**](#4-error-reference) ([日本語](https://code.claude.com/docs/ja/errors#the-server-returned-no-safety-verdict) / [English](https://code.claude.com/docs/en/errors#the-server-returned-no-safety-verdict)):  
  前回、見出しマップにだけあった 5 項目の本文が入りました
- [**Let Claude coordinate ongoing work with Projects**](#5-let-claude-coordinate-ongoing-work-with-projects) ([日本語](https://code.claude.com/docs/ja/claude-projects#limitations) / [English](https://code.claude.com/docs/en/claude-projects#limitations)):  
  スレッドを Remote Control 経由で自分のマシンで動かせるようになりました（ハイライト 5）
- [**Deploy managed settings**](#6-deploy-managed-settings) ([English](https://code.claude.com/docs/en/managed-settings#let-an-embedding-host-add-policy)):  
  埋め込みホストから渡される `strictKnownMarketplaces` と `blockedMarketplaces` の扱いが加わりました。残りは表の桁揃えとリンクの張り替えです
- [**Explore the .claude directory**](#7-explore-the-claude-directory) ([English](https://code.claude.com/docs/en/claude-directory)):  
  差分 52 行はすべて表の桁揃えとリンクの張り替えで、内容の変更はありません
- [**Customize keyboard shortcuts**](#8-customize-keyboard-shortcuts) ([日本語](https://code.claude.com/docs/ja/keybindings#text-fields) / [English](https://code.claude.com/docs/en/keybindings#text-fields)):  
  新しい節「Text fields」が加わり、`chat:sendNow` の説明が v2.1.281 の挙動に合わせて書き換わりました
<!-- light:updated-pages:end -->

**ここでは、changelog を除き、`llms-full.txt` で差分が 50 行（追加と削除の合計）以上あった既存ページを挙げています。** `env-vars`・`managed-settings`・`claude-directory` は、差分の大半が表の桁揃え（リンク先 URL が長くなり、列幅が変わったもの）です。

## 1. Environment variables

**差分は 746 行（追加 374・削除 372）ですが、ほとんどは変数表の列幅が変わっただけです。** 内容が変わったのは次の行です。

- **`env` の優先順位の説明**: 「プロジェクト設定とローカル設定では、`CLAUDE_CONFIG_DIR` や OpenTelemetry のエクスポーター変数など、一部の変数を設定できない」が加わりました（ハイライト 3）
- **`CLAUDE_CODE_ENABLE_TELEMETRY`・`OTEL_LOG_ASSISTANT_RESPONSES`・`OTEL_LOG_TOOL_CONTENT`・`OTEL_LOG_TOOL_DETAILS`・`OTEL_LOG_USER_PROMPTS`**: 「シェル・ユーザー設定・管理設定で設定する。プロジェクト設定とローカル設定では無視される」が加わりました
- **`CLAUDE_CODE_AUTO_MODE_SERVER`**: 「Anthropic API 直結では読まれない」が「Anthropic API 直結では v2.1.281 以降が必要」になり、既定で問い合わせる条件の説明は `permission-modes` に移されました（ハイライト 4）
- **`CLAUDE_CODE_RESUME_PROMPT`**: 中断したターンを `CLAUDE_CODE_RESUME_INTERRUPTED_TURN` で続けるときに加えて、**`-p` で保留したツール呼び出し（deferred tool call）を再開するとき**にも送る継続メッセージになりました
- **`CLAUDE_CODE_PLUGIN_GIT_TIMEOUT_MS`**: 対象の説明が「プラグインのインストールと更新での git 操作」から「**プラグインマーケットプレイスのクローンと更新**」に変わりました
- **`CLAUDE_CODE_SIMPLE`**: 自動検出しなくなるものの「プラグイン」が「**インストール済みの**プラグイン」になりました（`cli-reference` の `--bare`、`headless`、`glossary` も同じ書き換え）

- [Environment variables - Claude Code Docs (English)](https://code.claude.com/docs/en/env-vars#variables)

## 2. Test plugins with evals

**差分は 205 行（追加 136・削除 69）で、長い段落の多くが箇条書きに組み直されました。** 内容の変更は次のとおりです。

- **CI での信頼確認**: stdin・stdout が端末でないときや `--json` のときに加えて、**`CI` 環境変数が `true` などの真の値のときも、信頼の確認ができずに終了コード 1 で拒否**されるようになりました。`--trust-plugin` で信頼を自分で宣言できます
- **新しいトラブルシューティング「"Agent type '...' not found" for one of your plugin's agents」**: プラグインなしのベースライン実行でプラグインのエージェントを呼ぶと、このエラーになります。`Δ` はベースラインと比べる指標なので、想定どおりの挙動だと説明されています
- **読み込まれるもの**: `claude plugin eval` が読み込むのは「スキルとフック」から「**スキル・フック・エージェント**」になりました
- **許可ツール**: 読み取り専用で許可できるツールに **`AskUserQuestion`** が加わりました
- **スキルが使われたかの採点**: 例のグレーダーでは、`SKILL.md` の `name` ではなく、**`skills/` 配下のディレクトリ名**（Claude がスキルを呼ぶときの名前）を使うようになりました
- **採点からの除外**: モック化したサーバーがすべてプラグイン自身の宣言したものである場合、`target: mock_calls` の `regex` グレーダーと `focus: mock_calls` の `llm` グレーダーも、プラグインなしの側では採点から除外される対象に加わりました

見出しマップには `"is too old for claude plugin eval"` も加わりましたが、この見出しは本文にはまだありません。

- [evals でプラグインをテストする - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/plugin-evals#troubleshooting)
- [Test plugins with evals - Claude Code Docs (English)](https://code.claude.com/docs/en/plugin-evals#troubleshooting)

## 3. All settings

**差分は 150 行（追加 85・削除 65）です。** テレメトリの件（ハイライト 3）のほかに、次の変更があります。

- **`attribution`**: 型が「`commit`・`pr`・`sessionUrl` を持つオブジェクト」から「**オブジェクト、またはすべての帰属表示を隠す `false`**」になりました。`false` は **v2.1.281 以降**で、古い版はこの値を拒否し、それを含むユーザー・プロジェクト・ローカルの設定ファイルを丸ごと読み飛ばすため、複数の版で読むファイルではオブジェクト形式のまま空文字と `false` を使うよう案内されています（前回ハイライト 3 で changelog から紹介した件が本文に入りました）
- **`strictKnownMarketplaces` の許可ソース種別（Allowed source types）の `hostPattern` と `pathPattern`**: 正規表現は値の「**どこか**に一致すればよい」と明記され、ホスト全体に一致させるには `^` と `$` で囲む、`path` の前方一致には `^` で始める、と書かれました
- **GitHub のオーナーワイルドカード**: `*`・`*/plugins`・`acme-corp/tools-*` のような位置が不正なワイルドカードは、「文字どおりに比較する」から「**不正として無視する**」に変わりました
- **公式マーケットプレイスの自動登録**: 登録のきっかけが「Claude Code を初めて対話的に起動したとき」から「**初めて対話ターミナルセッションを始めたとき**」になり、登録されにくい例に「**VS Code 拡張機能でしか Claude Code を使っていないマシン**」が加わりました
- **`syncClaudeAiPlugins`**: 同期先の説明から「クラウドセッション」が外れ、「サインインしたターミナルセッションと Cowork セッション」になりました
- **`strictKnownMarketplaces`・`blockedMarketplaces`**: claude.ai の管理コンソールで設定した場合、**claude.ai 上で Git リポジトリからマーケットプレイスを追加するときにも claude.ai 自身が適用する**と追記されました
- **`disableSideloadFlags`**: `CLAUDE_CODE_PLUGIN_DIRS` 環境変数で指定したプラグインフォルダーも同じチェックの対象になりました（変数は v2.1.280 以降）
- **古い版の注記の削除**: `sandbox.credentials` などに付いていた「v2.1.186 / v2.1.187 以降が必要」が外れました

- [All settings - Claude Code Docs (English)](https://code.claude.com/docs/en/settings-reference#variables-claude-code-ignores-in-env)

## 4. Error reference

**差分は 149 行（追加 134・削除 15）で、前回「見出しマップにだけある」と書いた 5 項目の本文が入りました。** 早見表にも各項目の行が加わっています。

| 節 | 内容 |
|---|---|
| **The server returned no safety verdict** | auto モードのサーバー側レビューで判定が返らなかったときの拒否と、10 回続いたときの停止（ハイライト 4） |
| **role 'system' must precede an 'assistant' message** | 会話内のシステムメッセージの位置を API が拒否した 400。Claude Code は、そのテキストを通常のユーザーメッセージとして 1 回だけ送り直します。それでも出る場合は、プロキシや LLM ゲートウェイがシステムメッセージを足したか、会話を並べ替えた可能性が高いとされています |
| **Invalid encrypted_content in search_result block** | 会話履歴にある、API が復号できないホスト型 Web 検索の結果による 400。Claude Code 自身の WebSearch ツールは結果を平文で記録するので、多くはゲートウェイ経由で入り込みます。拒否されたブロックは履歴に残るため、`/clear` か新しいセッションで抜けます |
| **Temp directory refused or cannot be created** | macOS と Linux で、起動時に `claude-<uid>` の一時ディレクトリを作れない、または安全チェックに通らないときに終了コード 1 で終わる件。`ENOSPC`、所有者の不一致、読み取り不可などの文言と対処 |
| **Marketplace name is another spelling of a reserved name** | 予約名の別表記（例: `claude.code.plugins` は `claude-code-plugins` の別表記）とみなされたマーケットプレイス名の拒否と、登録済みエントリーの無視 |

一方、見出しマップには今回も **`errors` の新しい見出しが 12 件**加わりましたが（`Invalid data in redacted_thinking block`・`Disk quota or temp filesystem is full`・`Managed settings block the default model` など）、**これらはまだ本文にありません**。

- [エラーリファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/errors#the-server-returned-no-safety-verdict)
- [Error reference - Claude Code Docs (English)](https://code.claude.com/docs/en/errors#the-server-returned-no-safety-verdict)

## 5. Let Claude coordinate ongoing work with Projects

**差分は 100 行（追加 51・削除 49）で、内容はハイライト 5 のとおりです。** 変更行の多くは、「スレッド」を「クラウドスレッド」に書き分けたことによるものです。「他の Claude Code 機能との関係」でも、「すべてのスレッドはクラウドセッション」が「**自分のマシンで動かすよう頼まない限り**クラウドセッション」に、「ローカルセッションはプロジェクトの一部にできない」が「**自分で始めた**セッションはプロジェクトに追加できない。プロジェクトが自分のマシンに届くのは Remote Control でスレッドを動かすときだけ」に変わりました。

- [Claude がプロジェクトで進行中の作業を調整する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/claude-projects#limitations)
- [Let Claude coordinate ongoing work with Projects - Claude Code Docs (English)](https://code.claude.com/docs/en/claude-projects#limitations)

## 6. Deploy managed settings

**差分は 90 行（追加 46・削除 44）で、大半は表の桁揃えとリンクの張り替えです。** 内容の変更は 2 か所です。

- **埋め込みホストが渡すポリシー**: 親（埋め込みホスト）から渡された `strictKnownMarketplaces` は、**適用される管理ソースがどれも設定していないときに限って**効くこと、親から渡された `blockedMarketplaces` は**管理ソースのブロックリストに追加で**効くことが加わりました（いずれも **v2.1.282 以降**）。`claude-apps-gateway` でも、ロックをすべてかけても通る親の設定が「4 つ」から「**6 つ**」になり、この 2 キーが加わっています
- **Cowork**: どこでセッションが動いていても、Cowork タブの **Customize** や claude.ai 上で Git リポジトリからマーケットプレイスを追加するときは、claude.ai が管理コンソールの `strictKnownMarketplaces`・`blockedMarketplaces` を自分で適用する、と追記されました（`server-managed-settings` にも同じ追記）

- [Deploy managed settings - Claude Code Docs (English)](https://code.claude.com/docs/en/managed-settings#let-an-embedding-host-add-policy)

## 7. Explore the .claude directory

**差分は 52 行（追加 26・削除 26）で、すべてが表の桁揃えとプラグイン関連リンクの張り替えです。** 内容の変更はありません。見出しマップには `Session scratchpad directory` が加わりましたが、この見出しは本文にはまだありません。

- [Explore the .claude directory - Claude Code Docs (English)](https://code.claude.com/docs/en/claude-directory)

## 8. Customize keyboard shortcuts

**差分は 50 行（追加 32・削除 18）です。**

- **新しい節「Text fields」**: 裸の文字・数字・スペースにバインドを割り当てても、ダイアログやパネルのテキストフィールド（Claude の質問への `Other` の回答など）では、その文字をそのまま入力できます。フィールドにフォーカスがあるあいだも、Enter・Escape・Tab・矢印キーのような文字を入力しないキー、Ctrl・Alt・Cmd との組み合わせ、進行中のコードの 2 打目はバインドどおりに動きます。メインのプロンプトでは、どのバインドにも当たらないときだけ文字が入力されます
- **`chat:sendNow`**: 「実行中のターンを中断して、キューのメッセージを送る」から「**キューのメッセージを送る。作業中のターンがどうなるかは『When Claude Code sends what you queued』を参照**」になりました。前回サマリで「changelog では挙動が変わったが、本文は旧記述のまま」と書いた点で、`interactive-mode` とあわせて本文が更新されました（軽微な更新を参照）

- [キーボードショートカットのカスタマイズ - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/keybindings#text-fields)
- [Customize keyboard shortcuts - Claude Code Docs (English)](https://code.claude.com/docs/en/keybindings#text-fields)

## 軽微な更新

<!-- light:minor-updates:start -->
今回の差分は **3 ファイル**です。`git diff` の行数では `llms-full.txt` が 106,481 行（追加 54,598・削除 51,883）と大きく出ますが、これはページの差し替えで行の対応がずれたためで、**ページ単位で比べると追加 8,386 行・削除 5,697 行**です。見出しマップ（`en/claude_code_docs_map.md`）は 43 行（追加 38・削除 5）、`llms.txt` は 26 行（追加 13・削除 13）でした。`llms-full.txt` の総行数は **100,393 行から 103,108 行へ 2,715 行増え**、展開ページ数は **197 から 210** になりました（20 ページ追加・7 ページ削除）。既存のページで本文が変わったのは **79 ページ**で、そのうち 19 ページはリンクの張り替えだけです。changelog に積まれたのは **v2.1.282 の 1 本**です（詳細はハイライト 2）。

**新機能**

- **プラグインのドキュメント 20 ページの本文が公開されました**（詳細はハイライト 1 と新規追加ページ 1 を参照）
- **テキストフィールドでは、裸の文字にバインドを割り当てていても文字を入力できる**ことが、新しい節として説明されました（詳細は大幅更新ページ 8 を参照）— [日本語](https://code.claude.com/docs/ja/keybindings#text-fields) / [Customize keyboard shortcuts](https://code.claude.com/docs/en/keybindings#text-fields)
- **Claude apps gateway に `load_test_mode` ブロックが加わりました**。モデルプロバイダーを呼ばずにゲートウェイを負荷試験するモードで、プロバイダーへのリクエストを組み立てて署名したうえで送らずに捨て、定型の応答をストリームで返します。`reply_tokens`（既定 750）と `reply_seconds`（既定 9.5）で応答の大きさと長さを決め、`x-load-test-user` ヘッダーで開発者を最大 7 桁の番号で分けて数えられます。**必要な版は v2.1.283 以降と書かれていますが、今回の changelog の最新は v2.1.282 です**。開発者が使うゲートウェイでは決して有効にしないよう警告されています — [Claude apps gateway configuration](https://code.claude.com/docs/en/claude-apps-gateway-config#load_test_mode)
- **Agent SDK のトラブルシューティングページに、症状から該当ページを引く表が加わりました**。スキル・MCP・プラグイン・サブエージェント・ファイルのチェックポイント・フック・デプロイ・認証エラーごとに参照先が示され、ページ自体は CLI の起動・CLI プロセスの終了・構造化出力のエラーに範囲を絞りました（`llms.txt` の説明文は前回すでに変わっていました）— [Troubleshoot the Agent SDK](https://code.claude.com/docs/en/agent-sdk/troubleshooting)
- **フルスクリーン表示で、選択メニューをマウスホイールでスクロールできる**ようになりました（v2.1.280 以降）。短いウィンドウでの `/model` の一覧などが対象です — [Fullscreen rendering](https://code.claude.com/docs/en/fullscreen)

**機能改善**

- **OpenTelemetry の変数がプロジェクト設定とローカル設定から無視されるようになりました**（詳細はハイライト 3 を参照）— [All settings](https://code.claude.com/docs/en/settings-reference#variables-claude-code-ignores-in-env)
- **auto モードのサーバー側レビューが、接続の種類ごとに説明し直され、テレメトリを切ったセッションでも既定で使われるようになりました**（詳細はハイライト 4 を参照）— [日本語](https://code.claude.com/docs/ja/permission-modes#server-side-classifier-review) / [Choose a permission mode](https://code.claude.com/docs/en/permission-modes#server-side-classifier-review)
- **プロジェクトのスレッドを Remote Control 経由で自分のマシンで動かせるようになりました**（詳細はハイライト 5 を参照）— [日本語](https://code.claude.com/docs/ja/claude-projects#limitations) / [Let Claude coordinate ongoing work with Projects](https://code.claude.com/docs/en/claude-projects#limitations)
- **送信の即時実行（`Ctrl+Enter` / `Ctrl+X Ctrl+S`）の本文が、v2.1.281 の挙動に更新されました**。新しい節「When Claude Code sends what you queued」によると、キューの先頭に `!` のシェルコマンドがあればターンを中断します。それ以外は、Claude がシェルコマンドやサブエージェントなどバックグラウンドへ移せる作業をしていればそれを移してそのターンでメッセージを読み、応答を書いているだけかバックグラウンドへ移せない作業なら、ターンを中断して次にメッセージを送ります。「v2.1.281 より前は、どちらの場合も中断していた」と書かれています — [日本語](https://code.claude.com/docs/ja/interactive-mode#when-claude-code-sends-what-you-queued) / [Interactive mode](https://code.claude.com/docs/en/interactive-mode#when-claude-code-sends-what-you-queued)
- **`Ctrl+S` での退避と復元が、入力モードも戻す**ようになりました。退避した `!` のシェルコマンドは、シェルモードのまま戻ります — [日本語](https://code.claude.com/docs/ja/interactive-mode) / [Interactive mode](https://code.claude.com/docs/en/interactive-mode)
- **Remote Control の Trusted Devices が Pro・Max プランでも使えるようになりました**。Team・Enterprise では Owner が組織に対して有効にし、Pro・Max では各自が Cowork またはアカウントの設定ページで **Require trusted devices** をオンにします。組織での有効化の場所も、Claude Code の管理設定から **Organization settings > Capabilities > Remote sessions** に変わりました（見出しも「Team または Enterprise 組織で Trusted Devices を有効にする」に改称）— [日本語](https://code.claude.com/docs/ja/remote-control#trusted-devices) / [Continue local sessions from any device with Remote Control](https://code.claude.com/docs/en/remote-control#trusted-devices)
- **Amazon Bedrock の Mantle エンドポイントに必要な IAM アクションが明記されました**。Mantle には `bedrock-mantle:` プレフィックスの独自アクションがあり、`bedrock:` のアクションでは足りません。推論には `bedrock-mantle:CreateInference`、トークン数の計測には `bedrock-mantle:CountTokens` を付与します。`403` の読み方も、エラーが `bedrock-mantle:` のアクションを名指ししていればそのアクションを付与する、名指ししていなければモデルへのアクセスが許可されていない、の 2 通りに分けられました — [日本語](https://code.claude.com/docs/ja/amazon-bedrock#use-the-mantle-endpoint) / [Claude Code on Amazon Bedrock](https://code.claude.com/docs/en/amazon-bedrock#use-the-mantle-endpoint)
- **`/batch` が、各サブエージェントに「プルリクエストを開く」ではなく「変更を公開する」と書かれるようになり、git リポジトリの外でも `WorktreeCreate` フックがあれば動く**ことが本文に入りました（git リポジトリの外では v2.1.281 以降）。プルリクエストを開けないときは、何を公開したかを報告します（`commands`・`worktrees`・`best-practices`・`agents`）— [Run parallel sessions with worktrees](https://code.claude.com/docs/en/worktrees)
- **中断されたツール呼び出しの再開時の扱いが更新されました**。前のプロセスが終わったときに実行中だったツールは、「結果が記録される前に打ち切られた」と Claude に示され、もう一度実行する前に効果があったかを確かめるよう伝えられます（`CLAUDE_CODE_RESUME_INTERRUPTED_TURN` を設定していない場合）。v2.1.281 より前は、その呼び出しを会話から落とすか、ユーザーが中断したものとして見せていました — [Manage sessions](https://code.claude.com/docs/en/sessions)
- **プロンプト候補（prompt suggestions）のコストの説明が詳しくなりました**。候補を作るリクエストはセッションと同じモデルに送られ、プランの使用量上限か API コストに数えられます。プロンプトキャッシュを再利用するので大半はキャッシュ読み取りと少しの出力トークンで、`costs` にも同じ説明と、止める方法へのリンクが加わりました — [Manage costs effectively](https://code.claude.com/docs/en/costs)
- **テレメトリの帰属属性の伏せ字が、`OTEL_LOG_TOOL_DETAILS=1` で外せる**ことが明記されました。`agent.name`・`skill.name`・`plugin.name`・`mcp_server.name` が対象です — [Monitoring](https://code.claude.com/docs/en/monitoring-usage)
- **Agent SDK（Python）の説明が更新されました**。`user` は「ユーザー識別子」から「POSIX で Claude Code のサブプロセスを実行する OS ユーザー」に、`debug_stderr` は「SDK はこの値を無視する」に、`env` には `CLAUDE_AGENT_SDK_CLIENT_APP` で User-Agent にアプリを示せることが加わりました。`agent-sdk/permissions` には、Linux と macOS では認識されたサンドボックスの外で root や `sudo` のもと `bypassPermissions` で起動すると、最初のターンの前にクエリが失敗することが加わりました — [Agent SDK reference - Python](https://code.claude.com/docs/en/agent-sdk/python)
- **Claude apps gateway の IdP 停止時の説明が変わりました**。停止中のセッション更新は「失敗する」から「再試行を促す応答を受け、IdP が戻れば通る」になりました — [Claude apps gateway for Amazon Bedrock, Claude Platform on AWS, Google Cloud, and Microsoft Foundry](https://code.claude.com/docs/en/claude-apps-gateway)

**バグ修正**

- **v2.1.282 の修正 59 件のうち、本文ページに対応する記述が今回の差分で見つかったものは、ほぼありません。** 影響の大きいものを挙げます
- **API が復号できない Web 検索結果を履歴に持つ会話で、すべてのリクエストが 400 で失敗する問題を修正しました**（サードパーティのゲートウェイ経由で答えたターンなど）。`errors` の新しい節「Invalid encrypted_content in search_result block」はこの状況を説明しています
- **`Invalid data in redacted_thinking block` の API エラーで毎ターン失敗するセッションを修正しました**。Claude Code は会話の思考ブロックを落として 1 回だけ再試行します
- **`--continue`・`--resume` で続けた会話が、以前のメッセージを形を変えて送り直すケースをさらに修正しました**。API が Claude の以前の推論を捨てる原因になっていました。`/model` などのスラッシュコマンドを作業中に使ったときや、以前に提供した組み込みツールを外した `--tools` で再起動したときに、拡張思考が失われる問題も直りました
- **別の Claude Code プロセスがログインの更新中に閉じられたり強制終了されたりすると、最大 1 分間「another Claude Code process is refreshing it」でリクエストが失敗する問題を修正しました**
- **設定ファイルで、パターン途中に `:*` を含む Bash の許可ルールが読み飛ばされていた問題を修正しました**（`--allowedTools` では効いていました）。どこから設定しても効くようになり、起動時にどう一致するかの警告が出ます
- **管理設定の `permissions`・`autoMode`・`worktree`・`attribution` が、入れ子の値が 1 つ不正なだけで丸ごと無視されていた問題を修正しました**。残りの値は適用されます
- **Bash と PowerShell が、ディスククォータの満杯を「Exit code 1」の陰に隠し、一時領域に大きな出力ファイルを残していた問題を修正しました**
- **要約リクエストが拒否されると圧縮（compaction）が失敗していた問題を修正しました**。代替モデルで再試行します
- **vim モードの不具合をまとめて修正しました**。`>>` が空行をインデントする、回数付きの `r` が行より長いと文字を変える、`2J` が 1 行多く連結する、`.` の前の回数を無視する、などです

**その他**

- **v2.1.153〜v2.1.191 の古い版の注記 30 か所が、14 ページから外されました**。`mcp`（`claude mcp login` の v2.1.186・v2.1.191 など）、`sub-agents`（v2.1.153・v2.1.178・v2.1.186・v2.1.191）、`settings-reference`（`sandbox.credentials` の v2.1.187 など）、`cli-reference`・`commands`・`agent-teams`・`hooks`・`hooks-guide`・`checkpointing`・`github-actions`・`fullscreen`・`sandboxing`・`server-managed-settings`・`claude-platform-on-aws` です
- **クラウドセッションでプラグインを使う方法として「claude.ai アカウントで有効にすれば同期プラグインとして読み込まれる」と書いていた案内が、`cloud-environments`・`desktop`・`hooks`・`security-guidance` から削除されました**。`security-guidance` では代わりに、組織が管理設定で配布するプラグインの案内（`plugins/org`）へのリンクが置かれています
- **Claude Tag へのリンクが、`/docs/en/claude-tag` から `https://claude.com/docs/claude-tag` に変わりました**（`platforms`・`zero-data-retention`）
- **`channels-reference` から「承認済み許可リストは Anthropic が選定する」という記述が外れました**。研究プレビュー中は自作のチャネルが許可リストに載らないので開発フラグのままにする、という説明に変わっています
- **`github-enterprise-server` と `monitoring-usage` の組織設定のリンク先が、「Organization settings > Plugins」から「Organization settings > Plugins & skills」に変わりました**
- **`llms.txt` では、`desktop-quickstart` と `plugins/publish` の説明文が書き換わりました**。前者は「Claude デスクトップアプリをインストールし、Code タブを開いて、コンピューター上のプロジェクトフォルダーで最初の Claude Code セッションを始める」に、後者は公開先が「Anthropic のコミュニティマーケットプレイス」から「**Anthropic's directory**」になりました（本文はまだ旧名。ハイライト 1 を参照）
- **`llms.txt` の言語別インデックスのページ数が、おおむね 197 から 209 に増えました**（日本語は 196 → 209）。中国語は「Chinese（`cn.md`）」が「Simplified Chinese（`zh-cn.md`・210 ページ）」に、繁体字中国語は `zh-hant.md` が `zh-tw.md` に変わっています
- **見出しマップにだけ新しい見出しが入り、本文にはまだないものが約 35 件あります**。`settings-reference` の `availableModelsMatch`・`deniedModels`・`maxProseWidth`、`model-config` の `Block specific models or versions`、`terminal-config` の `Cap response width in wide terminals`、`agent-sdk/typescript` の `prewarm()`・`SpareProcess`、`mcp` の `Images in tool results`、`skills` の `Names reserved for synced skills`、`remote-control` の `"Couldn't verify your organization's policy for remote control"`、`errors` の 12 件、`troubleshoot-install` の 2 件（`claude.exe` missing after an update on Windows など）などです。逆に、マップから消えた `remote-control` の `Session URL reminders`・`Choose the right approach` は、**本文にはまだ残っています**
- **見出しマップ冒頭の自動生成スタンプが、2026年09月25日 03時24分49秒 UTC から 2026年09月26日 05時25分36秒 UTC へ進みました**

**参考リンクについて**: **日本語版の追従状況は、リンクするページごとに実測しました。反映を確認できたページにだけ日本語リンクを付けています。** 確認できたのは、`plugins/overview`（前回は 404）、`permission-modes`（v2.1.282 の記述まで反映）、`errors`（新しい 5 節あり）、`claude-projects`（制限事項に Remote Control の記述あり）、`interactive-mode`（`#when-claude-code-sends-what-you-queued` と v2.1.281 の注記あり）、`keybindings`（`#text-fields` あり）、`remote-control`（Trusted Devices の Pro・Max 対応あり）、`amazon-bedrock`（`bedrock-mantle:` の記述あり）、`plugin-evals`（`CI` 環境変数とエージェントが見つからない件の節あり）です。`claude-apps-gateway-config` の日本語版には `load_test_mode` がまだなく、`settings-reference` は取得した内容が途中で切れて確認できなかったため、いずれも英語版だけにしています。そのほかの未確認ページも英語版だけです。**changelog ページへのリンクは、本サマリの方針どおり付けていません。**
<!-- light:minor-updates:end -->

## 新着情報

<!-- light:whats-new:start -->
**`whats-new/` 配下では 7 ページが動きましたが、いずれもリンク先の張り替えだけです。** 2026年の Week 14・17・19・23・32・33・37 の各ダイジェストで、`/docs/en/plugins`・`/docs/en/plugins-reference` などへのリンクが `/docs/en/plugins/` 配下の新しい URL に置き換わりました（たとえば Week 37 の「`--plugin-dir` にプラグインのフォルダーを渡す」のリンク先は `plugins/create#load-a-directory-or-archive-for-one-session` になりました）。ダイジェストの本文に変更はなく、**Week 38 はまだ追加されていません**。
<!-- light:whats-new:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-09-24.md](./archives/latest/2026-09-24.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-09-24.md](./archives/latest-detail/2026-09-24.md)

<!--
base_commit: 9e4a9ca8dd012676f943d04b4ad641296ec601bb
head_commit: df1f117ca1144390ad3e12cf43bbdea20661d7d4
generated_at_full: 2026-09-26T15:07:47+09:00
-->
