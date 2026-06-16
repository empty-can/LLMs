---
対象期間: 2026年06月13日 〜 2026年06月15日
作成日: 2026-06-15
---

# Claude Code 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
今回は週間ダイジェスト（新着情報）2 件（Week 23 / Week 24）の追加が中心で、加えて多数の既存ページの記述精緻化と changelog（v2.1.178）の追加がありました。新規追加・大幅更新のリファレンスページはなく、新着情報で取り上げられた主要機能から 5 件をハイライトとして整理します。

主要なものを以下に挙げます。

1. 新コマンド `/cd` で、プロンプトキャッシュを壊さずにセッションの作業ディレクトリを別ディレクトリへ移動できるようになった（v2.1.169）
2. サブエージェントが自身のサブエージェントを生成できるようになり、サブエージェントパネルがネストツリーを表示する（バックグラウンドは 5 階層上限、v2.1.172）
3. `--safe-mode`（`CLAUDE_CODE_SAFE_MODE`）で CLAUDE.md・スキル・プラグイン・hooks・MCP 等のカスタマイズを全て無効化したクリーン起動が可能になり、設定起因の問題切り分けに使える（v2.1.169）
4. Amazon Bedrock・Google Vertex AI・Microsoft Foundry でも auto mode が利用可能になった（Opus 4.7 / 4.8 対応、`CLAUDE_CODE_ENABLE_AUTO_MODE=1` でオプトイン、v2.1.158）
5. `acceptEdits` モードでも、コードを実行しうるファイル（`.zshenv`・`.npmrc` 等）への書き込み前に確認が入るようになった（保護パスの拡充、v2.1.160）
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**`/cd` でセッションの作業ディレクトリを移動**](#1-cd-でセッションの作業ディレクトリを移動):  
  新コマンド `/cd` は、プロンプトキャッシュを再構築せずに現在のセッションを別の作業ディレクトリへ移動する。新ディレクトリの `CLAUDE.md` はシステムプロンプトを置き換えるのではなくメッセージとして追記され、セッションは移動先のプロジェクトストレージに再配置されるため `--resume` / `--continue` から見つかる。初めて作業するディレクトリの場合は信頼確認を求められる。
2. [**サブエージェントがサブエージェントを生成可能に**](#2-サブエージェントがサブエージェントを生成可能に):  
  サブエージェントが自身のサブエージェントを生成できるようになった。プロンプト下のサブエージェントパネルがツリー全体を表示し、各行に子孫数と `main` への経路が付く。バックグラウンドのサブエージェントは暴走を防ぐため 5 階層までに制限され、フォアグラウンドの連鎖は任意の深さで生成でき自己制限的に動作する。
3. [**セーフモードによるクリーンな設定の起動**](#3-セーフモードによるクリーンな設定の起動):  
  `--safe-mode` フラグ（または `CLAUDE_CODE_SAFE_MODE`）で、`CLAUDE.md`・スキル・プラグイン・hooks・MCP サーバー・カスタムコマンド/エージェントを一切ロードしないクリーンな状態で起動する。認証・モデル選択・組み込みツール・権限は引き続き機能し、セーフモードで問題が消えればそれらカスタマイズのいずれかが原因と切り分けられる。
4. [**サードパーティプロバイダでの auto mode 対応**](#4-サードパーティプロバイダでの-auto-mode-対応):  
  auto mode が Amazon Bedrock・Google Cloud Vertex AI・Microsoft Foundry でも利用可能になり、これらのプロバイダ上で権限プロンプトをバックグラウンドの安全チェックに置き換える。対応モデルは Opus 4.7 と Opus 4.8 のみで、`CLAUDE_CODE_ENABLE_AUTO_MODE=1` を設定するとオプトインできる。
5. [**acceptEdits モードでのファイル書き込み保護**](#5-acceptedits-モードでのファイル書き込み保護):  
  `acceptEdits` モードでも、コードを実行しうるファイルへの書き込み前に確認が入るようになった。保護対象は `.zshenv`・`.bash_login` 等のシェル起動ファイル、`~/.config/git/` 配下の git 設定、`.npmrc`・`.bazelrc`・`.pre-commit-config.yaml` 等のビルドツール設定で、これらは `bypassPermissions` を除くどのモードでも自動承認されない。
<!-- light:highlight-list:end -->

## 1. `/cd` でセッションの作業ディレクトリを移動

新コマンド `/cd`（v2.1.169 以降）は、会話の途中で現在のセッションを別の作業ディレクトリへ移動します。最大の特徴は、プロンプトキャッシュを再構築しない点です。移動先ディレクトリの `CLAUDE.md` はシステムプロンプトを差し替えるのではなく、メッセージとして会話に追記されます。これによりキャッシュを維持したままコンテキストを切り替えられます。

セッションは移動先ディレクトリのプロジェクトストレージへ再配置されるため、以降は移動先で `--resume` や `--continue` を実行するとそのセッションが見つかります（移動元のセッションピッカーには表示されなくなります）。これまで作業したことのないディレクトリへ移動する場合は、信頼の確認を求められます。`/cd ../other-project` のように相対パスで指定でき、`/add-dir` がディレクトリを追加するだけなのに対し、`/cd` はセッションの主作業ディレクトリそのものを移し替える点が異なります。

- [Week 24 · June 8–12, 2026 - Claude Code Docs (English)](https://code.claude.com/docs/en/whats-new/2026-w24)

## 2. サブエージェントがサブエージェントを生成可能に

サブエージェントが自身のサブエージェントを生成できるようになりました（v2.1.172 以降）。プロンプト下のサブエージェントパネルはツリー全体を表示し、各行にはその配下の子孫数と `main`（メインスレッド）までの経路が示されます。これにより、作業が枝分かれしていく様子を `/agents` のビューで追跡できます。

暴走する並行ツリーを防ぐため、**バックグラウンド**のサブエージェントは 5 階層の深さまでに制限されます。一方、**フォアグラウンド**の連鎖は任意の深さで生成でき、ブロッキング実行であるため自己制限的に振る舞います。

- [Create custom subagents - Claude Code Docs (English)](https://code.claude.com/docs/en/sub-agents#spawn-nested-subagents)

## 3. セーフモードによるクリーンな設定の起動

`--safe-mode` フラグ（または環境変数 `CLAUDE_CODE_SAFE_MODE`）を付けて Claude Code を起動すると、全てのカスタマイズを無効化した状態で立ち上がります。具体的には `CLAUDE.md`、スキル、プラグイン、hooks、MCP サーバー、カスタムコマンド・カスタムエージェントがロードされません。一方で、認証・モデル選択・組み込みツール・権限は引き続き機能します。

これは設定起因の不具合を切り分けるための機能です。ある問題がセーフモードで再現しなくなれば、原因は無効化されたカスタマイズ群（`CLAUDE.md`・スキル・プラグイン・hooks・MCP・カスタムコマンド/エージェント）のいずれかにあると判断できます。「設定をデバッグする」ページの「クリーン設定に対してテストする」節がこの手順の出発点になります。

- [Debug your configuration - Claude Code Docs (English)](https://code.claude.com/docs/en/debug-your-config#test-against-a-clean-configuration)

## 4. サードパーティプロバイダでの auto mode 対応

auto mode が Amazon Bedrock・Google Cloud Vertex AI・Microsoft Foundry でも利用可能になりました（v2.1.158 以降）。これらのサードパーティプロバイダ上で、権限プロンプトをバックグラウンドの安全チェック（別の分類器モデルによる事前評価）に置き換えます。対応モデルは **Opus 4.7 と Opus 4.8 のみ**です。

これらのプロバイダでは、`CLAUDE_CODE_ENABLE_AUTO_MODE` を `1` に設定するまで auto mode は `Shift+Tab` のサイクルに現れません。1 人の開発者には `~/.claude/settings.json` の `env` ブロックに、組織全体には管理設定の同じ `env` ブロックに変数を追加します。デフォルトの開始モードにするには、あわせてユーザー/管理設定で `"permissions": {"defaultMode": "auto"}` を設定します。管理者は `disableAutoMode` を `"disable"` にすることで開発者による有効化を抑止できます。

- [パーミッションモードを選択する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/permission-modes#enable-auto-mode-on-bedrock-vertex-ai-or-foundry)
- [Choose a permission mode - Claude Code Docs (English)](https://code.claude.com/docs/en/permission-modes#enable-auto-mode-on-bedrock-vertex-ai-or-foundry)

## 5. acceptEdits モードでのファイル書き込み保護

`acceptEdits` モードでも、コードを実行しうるファイルへの書き込み前には確認が入るようになりました（v2.1.160 以降）。保護対象には、`.zshenv` や `.bash_login` などのシェル起動ファイル、`~/.config/git/` 配下の git 設定、`.npmrc`・`.bazelrc`・`.pre-commit-config.yaml` などのビルドツール設定が含まれます。

これらのパスへの書き込みは、`bypassPermissions` を除くどのモードでも自動承認されることはありません。`default`・`acceptEdits`・`plan` ではプロンプトが表示され、`auto` では分類器にルーティングされ、`dontAsk` では拒否されます。リポジトリ状態（`.git` 等）や Claude 自身の設定（`.claude` の大部分）も同じ保護パスの仕組みで偶発的な破損から守られます。

- [パーミッションモードを選択する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/permission-modes#protected-paths)
- [Choose a permission mode - Claude Code Docs (English)](https://code.claude.com/docs/en/permission-modes#protected-paths)

## 新規追加されたページ

<!-- light:new-pages:start -->
*(今回の対象期間に新規追加されたページはありません)*
<!-- light:new-pages:end -->

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
*(今回の対象期間に大幅な更新を受けたページはありません)*
<!-- light:updated-pages:end -->

## 軽微な更新

<!-- light:minor-updates:start -->
今回の対象期間は、新着情報（後述）に加えて既存ページの記述精緻化と changelog（v2.1.178）の追加が中心です。新着情報のハイライトに挙げた以外の更新を分類別に示します。

**新機能**
- 権限ルールに `Tool(param:value)` 構文が追加され、ツールの入力パラメータにマッチできるようになった（`*` ワイルドカード可。例: `Agent(model:opus)` で Opus を使うサブエージェントをブロック）（v2.1.178）。現時点では changelog のみの記載で、権限リファレンスページには未反映。
- ネストした `.claude/skills` ディレクトリのスキルが、その配下のファイルを扱う際にロードされるようになった。名前衝突時はネスト側スキルが `<dir>:<name>` として現れ、双方が利用可能に保たれる（v2.1.178）。

**機能改善**
- 「Model configuration」ページの設定テーブルに、`/config` 由来の各種 preference キー（`theme`・`verbose`・`autoCompactEnabled`・`fileCheckpointingEnabled`・`agentPushNotifEnabled`・`inputNeededNotifEnabled`）の行が追加され、各キーが `/config` のどのトグルに対応するかが明文化された。あわせて v2.1.119 以前はこれらが `~/.claude.json` に保存される旨の注記も更新された。 — [English](https://code.claude.com/docs/en/settings#available-settings)
- 「Remote control」ページで、モバイルプッシュ通知が 2 つのトグルに整理された。**Push when Claude decides**（`agentPushNotifEnabled`、長時間タスク完了時等の能動通知）と **Push when actions required**（`inputNeededNotifEnabled`、権限プロンプトや質問の待ち時）で、`/config` から個別に有効化できる。 — [English](https://code.claude.com/docs/en/remote-control#mobile-push-notifications)
- `claude daemon status` が、起動中のスーパバイザと呼び出した `claude` のバージョンが異なる場合に警告するようになった（更新後にスーパバイザが新バージョンへ再起動していない状況で発生）。両方のバージョンを示し、`claude daemon stop --any` で新バージョンを取り込むよう促す。OS サービスとしてインストールされている場合は `claude daemon stop`（フラグなし）が案内される。 — [English](https://code.claude.com/docs/en/agent-view#where-state-is-stored)
- 「Permissions」ページに、トランスクリプトや権限ダイアログに表示されるツールのラベルが正規名と異なりうる旨の説明が追加された（例: 表示が `Stop Task` のツールの正規名は `TaskStop`）。権限ルールと hook マッチャーは正規名のみにマッチするため、`Stop Task` と書いたルールはマッチしない。 — [English](https://code.claude.com/docs/en/permissions#tool-name-wildcards)
- 「Troubleshooting」ページに「Homebrew cask unavailable or outdated」項目が追加された。`Cask 'claude-code' is unavailable` エラーはローカルの cask インデックスが古い場合に起き、`brew update` 後に再試行する。期待より古いバージョンが入る場合も同じ原因で、最新版は `brew install --cask claude-code@latest` で取得できる旨が解説された（エラー対応表にも該当行を追加）。 — [English](https://code.claude.com/docs/en/troubleshooting#homebrew-cask-unavailable-or-outdated)
- デスクトップアプリのトラブルシューティング「Still stuck?」のサポート導線が更新され、まず Help → Get Support またはサポートセンターを案内し、standalone の `claude` CLI でも再現する問題のみ GitHub Issues へ、という整理になった。

以下は v2.1.178 の changelog 由来の改善で、いずれも対応する通常ページへの記載が無いためリンクは付けない。

- ネストした `.claude/` ディレクトリで、agent・workflow・output-style の名前が衝突した場合に作業ディレクトリに最も近いものが優先されるようになった（プロジェクトスコープの workflow 保存も最も近い既存の `.claude/workflows/` を対象にする）（v2.1.178）。
- `/doctor` の表示が全セクションで一貫したフラットツリーになり、セクションのステータスアイコンとコマンド名の強調が改善された（v2.1.178）。
- workflow のプロンプトキーワードが purple shimmer の強調表示になり、「run a workflow」「workflow:」のような明示的フレーズでのみ発火する（単に "workflow" と述べただけでは発火しない）よう変更された（v2.1.178）。
- Remote Control のエラーメッセージが改善され、接続失敗時はフッタに赤い「/rc failed」インジケータが表示され続け、「未有効化」エラーがゲート/チェック失敗/期限切れ entitlement/組織ポリシーのいずれかを説明するようになった（v2.1.178）。
- スキル一覧の切り詰め警告が、影響を受けるスキル説明の件数を示すよう改善された（v2.1.178）。

**バグ修正**

v2.1.178 で多数の修正が入った。主なものを挙げる。

- compaction が `--fallback-model` を尊重するようになり、過負荷・モデル不可時に設定済みのフォールバックチェーンへ切り替わるようになった。
- サブエージェントのトランスクリプト閲覧でツール結果とライブ進捗が表示されるようになった。
- サブエージェントがターンを終える間に送ったメッセージが破棄されなくなった。
- 実行中サブエージェントの `ctrl+b` でのバックグラウンド化が、タスクを最初からやり直さなくなった。
- vim モードの取り消しが修正され、`u` が連続入力されたコマンドを 1 つにまとめず 1 ステップずつ取り消すようになった。
- `/bug` が送信前に説明を必須とするようになり、モデルの拒否テキストを GitHub issue のタイトルに使わなくなった。
- 親プロセスから古い websocket/OAuth のファイルディスクリプタ環境変数を継承した際のクラッシュ（OOM）が修正された。
- `ANTHROPIC_BASE_URL` と `ANTHROPIC_AUTH_TOKEN` でカスタム API ゲートウェイを使うシェルからデーモンを起動した際に `claude agents` のワーカーが `401 Invalid bearer token` で失敗する問題が修正された。

**その他**
- 「2026年06月15日以降、サブスクリプションプランでの Agent SDK / `claude -p` の利用が対話利用とは別枠の月次 Agent SDK クレジットを消費する」旨の注記が、認証（long-lived トークン生成）・headless・Agent SDK overview・法務とコンプライアンスの計 4 ページから削除された。
- 「Overview」ページのインストールタブ（Native Install / Homebrew / WinGet 等）のコードブロックで、前回サマリの「その他」で触れた `theme={null}` 属性の重複付与が解消され、単一指定に正規化された（表示内容に変化はなく、ソース生成由来の重複が是正された）。
<!-- light:minor-updates:end -->

## 新着情報

<!-- light:whats-new:start -->
- [**2026年06月01日～05日(Week 23)**](#2026年06月01日05日week-23) ([English](https://code.claude.com/docs/en/whats-new/2026-w23)):  
  サードパーティプロバイダ（Bedrock/Vertex/Foundry）での auto mode、`acceptEdits` でのより安全な自動編集、`/plugin list` によるインストール済みプラグインの一覧表示、管理デプロイ向けの承認済みバージョン範囲指定（v2.1.158〜v2.1.165）。
- [**2026年06月08日～12日(Week 24)**](#2026年06月08日12日week-24) ([English](https://code.claude.com/docs/en/whats-new/2026-w24)):  
  `/cd` によるセッションの作業ディレクトリ移動、サブエージェントによるサブエージェント生成、`--safe-mode` での設定問題の切り分け（v2.1.166〜v2.1.176）。
<!-- light:whats-new:end -->

## 2026年06月01日～05日(Week 23)

Week 23（v2.1.158〜v2.1.165）では 4 つの主要機能が取り上げられました。**サードパーティプロバイダでの auto mode**（ハイライト 4 参照）と **acceptEdits でのより安全な自動編集**（ハイライト 5 参照）に加え、次の 2 つが紹介されています。

`/plugin list` コマンドが追加され、`/plugin` メニューを開かずにインストール済みプラグインをインラインで一覧表示できます。シェルからは `claude plugin list` としても利用でき、対話形式では `--enabled` / `--disabled` を付けて状態で絞り込めます。また、管理設定に `requiredMinimumVersion` と `requiredMaximumVersion` の 2 つが追加され、組織が承認済みの Claude Code バージョン範囲を要求できるようになりました。範囲外のクライアントは起動時に終了し、組織の方法で更新するよう促されますが、`claude update` / `claude install` / `claude doctor` は引き続き動作するため復旧は可能です。

このほか「Other wins」として、dynamic workflows のトリガーキーワードが `workflow` から `ultracode` へ変更、Stop / SubagentStop hooks が `hookSpecificOutput.additionalContext` を返してターンを継続できるように、`claude mcp` の list/get/add が秘密情報（環境変数参照・認証ヘッダ・URL 内シークレット）を出力しないように、並列ツールバッチ内の Bash 失敗が他を巻き込まないように、などの改善が挙げられています。

- [Week 23 · June 1–5, 2026 - Claude Code Docs (English)](https://code.claude.com/docs/en/whats-new/2026-w23)

## 2026年06月08日～12日(Week 24)

Week 24（v2.1.166〜v2.1.176）では 3 つの主要機能が取り上げられました。いずれもハイライトとして整理済みです。**`/cd` によるセッション移動**（ハイライト 1 参照）、**サブエージェントによるサブエージェント生成**（ハイライト 2 参照）、**`--safe-mode` でのクリーン起動**（ハイライト 3 参照）です。

「Other wins」では、`fallbackModel` が最大 3 つのフォールバックモデルを順に試すよう設定でき `--fallback-model` が対話セッションにも適用されるようになった点、セッションタイトルが会話の言語で生成されるようになった点（`language` 設定で固定可能）、`claude agents --json` に `--all` と `id` / `state` フィールドが追加された点、`/plugin` のマーケットプレース閲覧に検索バーが付いた点、新設定 `disableBundledSkills`（と `CLAUDE_CODE_DISABLE_BUNDLED_SKILLS`）でバンドルのスキル・ワークフロー・組み込みコマンドを隠せる点、deny ルールのツール名位置にグロブを書けるようになり `"*"` で全ツールを拒否できる点、新管理設定 `enforceAvailableModels` が `availableModels` アローリストを Default モデルにも適用する点などが挙げられています。

- [Week 24 · June 8–12, 2026 - Claude Code Docs (English)](https://code.claude.com/docs/en/whats-new/2026-w24)

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-06-13.md](./archives/latest/2026-06-13.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-06-13.md](./archives/latest-detail/2026-06-13.md)

<!--
base_commit: ebc2609266a75e810f43ebdb2b01c73bbb73db73
head_commit: 045e333d0dbf9f1ed09cfee6e2ec61227aa03027
generated_at_full: 2026-06-16T15:07:19+09:00
-->
