---
対象期間: 2026年06月25日 〜 2026年06月26日
作成日: 2026-06-26
---

# Claude Code 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
今回の対象期間は、Claude Code v2.1.193（2026年06月25日）のリリースに伴うドキュメント整備に加え、複数ページにまたがる編集が中心です。組織管理者を指す用語が「admin」から「Owner / Primary Owner」へ全面的に置き換えられ、前回新規追加として告知済みの「機能の利用可能性」ページの本文が公開されました。

主要なものを以下に挙げます。

1. 多数のページで、組織レベルの操作を行う役割の表記が「admin（管理者）」から「Owner / Primary Owner（オーナー）」へ統一された
2. 「機能の利用可能性（Feature availability）」ページの本文が公開され、プロバイダー別・プラン別の機能対応表が全文で参照できるようになった
3. Fast mode の対応モデルが整理され、Opus 4.6 が記載から外れ、Opus 4.7 の Fast mode が 2026年06月25日付で非推奨（2026年07月24日に削除予定）になった
4. セッションドキュメントに「スクリプトから会話にアクセスする」節が新設され、トランスクリプトの保存仕様も整理された
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**admin から Owner へのロール用語統一**](#1-admin-から-owner-へのロール用語統一):  
  Code Review・Remote Control・Channels・Routines・Fast mode・GitHub Enterprise Server・サーバー管理設定・自動モードなど多数のページで、組織レベルの設定を行う役割の表記が「admin（管理者）」から「Owner / Primary Owner（オーナー）」へ置き換えられた。サーバー管理設定では「Admin など Owner 以外のロールは管理設定を表示・編集できない」と明記され、必要ロールが Owner / Primary Owner であることが具体化された。
2. [**機能の利用可能性ページの本文公開**](#2-機能の利用可能性ページの本文公開):  
  前回サマリで新規追加として告知済みの「機能の利用可能性（Feature availability）」ページの本文が `llms-full.txt` に取り込まれ、全文で参照できるようになった。モデルプロバイダー別・サブスクリプションプラン別の機能対応を ✓／✗／脚注付きの表で比較し、プロバイダーごとに不足機能と代替手段をタブでまとめている。日本語ページも完訳済み。
3. [**Fast mode の対応モデル整理**](#3-fast-mode-の対応モデル整理):  
  Fast mode の説明から Opus 4.6 が外れ、対応は Opus 4.8 と Opus 4.7 のみになった。さらに Opus 4.7 の Fast mode は 2026年06月25日付で非推奨となり、2026年07月24日に削除予定（削除後はエラーを返し標準速度にフォールバックしない）であることが明記された。価格表・レート制限プールの記述も 2 モデルに整理されている。
4. [**セッションのスクリプト連携とトランスクリプト保存の整理**](#4-セッションのスクリプト連携とトランスクリプト保存の整理):  
  「セッションの管理」ページに「スクリプトから会話にアクセスする」節が新設され、`claude -p` の JSON 出力・`--resume` でのフォローアップ・hooks の `transcript_path`・Agent SDK という 4 つの構造化データ取得手段が整理された。あわせて「トランスクリプトが保存される場所」節で保存先・保持期間・書き込み抑制を表にまとめ、JSONL を直接解析せず `/export` かスクリプトインターフェースを使うよう案内が加わった。
<!-- light:highlight-list:end -->

## 1. admin から Owner へのロール用語統一

今回の更新で最も広範なのは、組織レベルの設定・有効化を行う役割の表記を「admin（管理者）」から「Owner / Primary Owner（オーナー）」へ置き換える編集です。Code Review、Remote Control、Channels、Routines、Fast mode、GitHub Enterprise Server（GHES）、サーバー管理設定、自動モード、Claude Code on the web、Artifacts など、多数のページで「an admin enables…」「Team and Enterprise admins…」といった記述が「an Owner enables…」「Team and Enterprise Owners…」へ改められました。たとえば Code Review のセットアップ手順では、必要な権限が「admin access」から「Owner または Primary Owner ロール」へ具体化され、GHES の接続やサーバー管理設定の編集にも同じく「Owner または Primary Owner ロール」が必要であることが明記されています。

特にサーバー管理設定のページには、リンクが別の管理設定ページにリダイレクトされる場合の説明として「Admin など Owner 以外のロールは管理設定を表示・編集できないため、組織の Owner または Primary Owner に変更を依頼すること」という注記と「Access control」への参照が追加されました。これは claude.ai のロールモデル（Owner / Primary Owner が最上位の管理権限を持つ）に文言を合わせるもので、機能自体の変更ではなく、誰がその操作を行えるのかをドキュメント上で正確化する整備です。なお日本語ページは追従の途上で、Code Review のセットアップ手順のように「Owner または Primary Owner」が反映済みの箇所と、「レビューの仕組み」節のように依然「管理者」のままの箇所が混在しています。

- [Code Review - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/code-review#set-up-code-review)
- [Code Review - Claude Code Docs (English)](https://code.claude.com/docs/en/code-review#set-up-code-review)

## 2. 機能の利用可能性ページの本文公開

前回サマリで「機能の利用可能性（Feature availability）」ページを新規追加として告知した際は、本文がまだ `llms-full.txt`（全文展開）に取り込まれていない状態でした。今回その本文が取り込まれ、全文で参照できるようになりました。

このページは、Claude Code の各機能がどの認証経路・プランで使えるかを一覧で比較するリファレンスです。まず「モデルプロバイダー別の利用可能性」として、すべてのプロバイダーで同じく動く機能（CLI・Agent SDK・拡張機能・サブエージェント・hooks・commands・skills・MCP・チェックポイント・サンドボックス・Workflows など）、Claude サブスクリプションが必要な機能（Web/モバイル/Slack の Claude Code、Desktop、Routines、Ultraplan/Ultrareview、Code Review、Remote Control、Chrome 拡張、Computer use、Artifacts、音声ディクテーション）、プロバイダーによって挙動が異なる CLI 機能（Web 検索・Fast mode・Auto mode・Advisor・Channels・`/loop`・GitHub Actions/GitLab CI/CD）、管理・アナリティクス機能を、✓／✗／脚注付きの表で示します。続いて「プロバイダー別サマリー」タブで各プロバイダーの不足機能と代替手段（スケジューリングは `/loop`、クラウドセッションは GitHub Actions/GitLab CI/CD など）をまとめ、最後に「サブスクリプションプラン別の利用可能性（Pro / Max / Team / Enterprise）」表とモデルの利用可能性についての案内が続きます。デプロイメント概要（third-party-integrations）からも、本ページへの「機能ごとの内訳はこちら」という案内リンクが追加されました。日本語ページも本文・表とも完訳済みです。

- [機能の利用可能性 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/feature-availability#availability-by-model-provider)
- [Feature availability - Claude Code Docs (English)](https://code.claude.com/docs/en/feature-availability#availability-by-model-provider)

## 3. Fast mode の対応モデル整理

Fast mode（高速モード）のドキュメントから Opus 4.6 への言及が取り除かれ、対応モデルは Opus 4.8 と Opus 4.7 の 2 つに整理されました。あわせて、Opus 4.7 の Fast mode は 2026年06月25日付で非推奨となり、2026年07月24日に削除予定であることが新しい警告として明記されています。削除後、Opus 4.7 への Fast mode リクエストはエラーを返し、標準速度の Opus 4.7 にはフォールバックしません。高速化を維持するには Opus 4.8 への移行が案内されています（従来は「Opus 4.6 の Fast mode が Opus 4.8 ローンチの約 30 日後に削除」という記述でした）。

これに伴い、価格表は「Opus 4.8: 入力 $10 / 出力 $50」「Opus 4.7: 入力 $30 / 出力 $150」の 2 行に整理され（旧表の「Opus 4.7 and Opus 4.6」の行が「Opus 4.7」のみに）、レート制限プールの説明も「Opus 4.8 と Opus 4.7 が同じレート制限プールを共有」に改められました。組織での有効化案内も「Console は管理者、Claude AI（Team/Enterprise）は Owner が有効化」とロール表記が更新されています。環境変数ページでも `CLAUDE_CODE_OPUS_4_6_FAST_MODE_OVERRIDE` の説明から「Opus 4.6 で Fast mode を使う方法」の案内が削除されました。日本語ページもこの変更を反映済みです。

- [高速モードでレスポンスを高速化 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/fast-mode)
- [日本語](https://code.claude.com/docs/ja/fast-mode) / [Get faster Opus responses with fast mode - Claude Code Docs (English)](https://code.claude.com/docs/en/fast-mode)

## 4. セッションのスクリプト連携とトランスクリプト保存の整理

「セッションの管理」ページの「セッションデータをエクスポートして見つける」節が再構成され、新たに 2 つのサブ節が追加されました。

1 つ目の「スクリプトから会話にアクセスする」節は、`/export` が人間向けのレンダリング済みトランスクリプトを生成するのに対し、スクリプトが解析できる構造化データを得る手段を、トリガー別に 4 つ整理しています。すなわち、(1) `claude -p` を `--output-format json`／`stream-json` で実行して結果・セッション ID・使用量・コストを構造化 JSON として取得する、(2) 既存セッションに `claude -p --resume` でフォローアップ（要約依頼など）を送り構造化応答を得る、(3) hooks やステータスラインが入力として受け取る `transcript_path` を読む（`SessionEnd` hook でセッション終了時にトランスクリプトをアーカイブする等）、(4) TypeScript／Python アプリには Agent SDK を使う、の 4 つです。`claude -p --resume <session-id> --output-format json "..." | jq -r '.result'` という具体例も示されています。

2 つ目の「トランスクリプトが保存される場所」節では、保存先が `~/.claude/projects/<project>/<session-id>.jsonl`（`<project>` は作業ディレクトリパスの英数字以外を `-` に置換したもの）であること、エントリ形式は Claude Code の内部形式でバージョン間で変わるため直接解析するスクリプトはリリースごとに壊れうること、そのため `/export` かスクリプトインターフェースを使うべきこと、が明記されました。さらに保存先（`CLAUDE_CONFIG_DIR`）・保持期間（`cleanupPeriodDays`）・書き込み抑制（`CLAUDE_CODE_SKIP_PROMPT_HISTORY`／`--no-session-persistence`）を表にまとめています。llms.txt のページ説明と docs_map にも「exporting transcripts」「Access conversations from scripts」「Where transcripts are stored」が反映されました。日本語ページも両節とも完訳済みです。

- [セッションの管理 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/sessions#access-conversations-from-scripts)
- [Manage sessions - Claude Code Docs (English)](https://code.claude.com/docs/en/sessions#access-conversations-from-scripts)

## 新規追加されたページ

<!-- light:new-pages:start -->
今回、リファレンス系で完全に新規追加されたページはありません。「機能の利用可能性（Feature availability）」ページは前回サマリで新規追加として告知済みで、今回その本文が公開されました（詳細はハイライト 2 参照）。
<!-- light:new-pages:end -->

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
今回の主要な大幅更新（admin → Owner のロール用語統一、機能の利用可能性ページの本文公開、Fast mode の対応モデル整理、セッションのスクリプト連携）は、いずれも上記ハイライトに整理しました。これら以外で単一ページ 50 行以上に該当するのは設定リファレンス（settings.md）ですが、その変更の大半は各設定の既定値を先頭に `**Default**: …` として明示する書式統一で、内容面の変更は一部の既定値の明確化にとどまります（詳細は下記「軽微な更新」の機能改善を参照）。なお CLI リファレンスページは `llms-full.txt` 内で末尾へ再配置されましたが、本文の実質的な変更は `--background` エイリアスの追記のみです。
<!-- light:updated-pages:end -->

## 軽微な更新

<!-- light:minor-updates:start -->
今回の軽微な更新は、Claude Code v2.1.193（2026年06月25日）リリースの各機能・修正と、複数ページにまたがる書式・字句の整備が中心です。以下に分類して整理します（特記なき限りバージョンは v2.1.193 を指します）。

**新機能**

- `--bg` に長形式 `--background` のエイリアスが追加された（バックグラウンドエージェントとしてセッションを開始） — [日本語](https://code.claude.com/docs/ja/cli-reference#cli-flags) / [English](https://code.claude.com/docs/en/cli-reference#cli-flags)
- `autoMode.classifyAllShell` 設定が追加され、すべての Bash／PowerShell コマンドを（任意コード実行パターンだけでなく）auto-mode 分類器に通せるようになった。あわせて auto-mode の拒否理由が transcript・拒否トースト・`/permissions` の最近の拒否に表示されるようになった
- `claude_code.assistant_response` という OpenTelemetry ログイベントが追加され、モデルの応答テキストを記録できるようになった。既定ではリダクトされ、`OTEL_LOG_ASSISTANT_RESPONSES=1` で記録。同変数が未設定のときは `OTEL_LOG_USER_PROMPTS` に従うため、既にプロンプト内容を記録している環境はアップグレード時に応答内容も記録され始める点に注意（プロンプトのみに留めるには `OTEL_LOG_ASSISTANT_RESPONSES=0`）
- bash モード（`!`）にライブのファイルパス補完が追加された
- MCP サーバーが認証を要するときに起動時通知が出るようになった（`/mcp` を案内）
- アイドル状態のバックグラウンドシェルコマンドに対する自動メモリ逼迫リーピングが追加された（`CLAUDE_CODE_DISABLE_BG_SHELL_PRESSURE_REAP=1` で無効化）
- `/tui default` で classic レンダラーへ明示的に戻せるようになった — [English](https://code.claude.com/docs/en/fullscreen#enable-fullscreen-rendering)

**機能改善**

- 設定リファレンス（settings.md）の各設定説明が、既定値を先頭に `**Default**: …` として明示する書式に統一された。あわせて `autoUpdatesChannel`（既定 `"latest"`）・`defaultShell`（既定 `"bash"`、Windows で Bash 不在時は `"powershell"`）など一部の既定値も明確化された — [日本語](https://code.claude.com/docs/ja/settings#available-settings) / [English](https://code.claude.com/docs/en/settings#available-settings)
- エージェントチームの teammate が、リードの effort level を継承するようになった（split-pane 表示では v2.1.186 以降に適用） — [日本語](https://code.claude.com/docs/ja/agent-teams) / [English](https://code.claude.com/docs/en/agent-teams)
- OpenTelemetry の `start_type` 属性に `"agents_view"` 値が追加され、`claude agents` ダッシュボードのプロセス（ユーザーが起動するローカル UI）を会話セッションと区別できるようになった — [日本語](https://code.claude.com/docs/ja/monitoring-usage) / [English](https://code.claude.com/docs/en/monitoring-usage)
- 監視ドキュメントに、コミットのモデル別内訳を出す際は token／cost 側を `query_source="main"` でフィルタし、補助・サブエージェントのリクエストを混入させないよう案内が追記された — [日本語](https://code.claude.com/docs/ja/monitoring-usage) / [English](https://code.claude.com/docs/en/monitoring-usage)
- インストール手順に、`syntax error near unexpected token '<'`・`403` などの curl エラー時は「インストールのトラブルシュート」を参照するよう誘導が追記された（複数の quickstart／setup ページ） — [English](https://code.claude.com/docs/en/troubleshoot-install#find-your-error)
- MCP サーバーが提供するツールを確認するコード例に、TypeScript に加えて Python 版が `CodeGroup` で併記された
- MCP `headersHelper` 認証が、ツール呼び出しで 401／403 が返ったときに自動で再実行・再接続するようになった
- プラグインの自動リネームが、marketplace の `renames` マップを自動追従して設定を新名へ更新するようになった
- バックグラウンドエージェントの起動結果が「end your response」と指示しなくなり、エージェント実行中も他タスクの作業を継続するようになった
- `/add-dir` で対象が既に作業ディレクトリの場合のメッセージが改善された

**バグ修正**

- `/login` 直後に `/model` などクライアントデータに依存する UI が、古い／空の状態を表示する不具合を修正
- バックグラウンド化（←←）が、実行中タスクがすべて新セッションへ引き継がれる場合でも「N background tasks would be abandoned」で誤ってキャンセルされる不具合を修正
- ピン留めしたバックグラウンドエージェントが、自動更新のたびに「Continue from where you left off」と再プロンプトされる不具合を修正
- メインターンのバックグラウンド化が、会話を再実行する幻の「general-purpose (resumed)」サブエージェントを生成する不具合を修正
- エージェントパネルでサブエージェントを表示すると兄弟エージェントが隠れる不具合を修正

**その他**

- 多数のリファレンス／ガイドページから「This page covers:」の目次ブロックが削除された（agent-teams・artifacts・channels・dev-containers・llm-gateway・sandbox-environments・sandboxing・sessions・sub-agents・workflows・scheduled-tasks・fast-mode・code-review・MCP tool search など）。
- CLI リファレンスページが `llms-full.txt` 内で末尾へ再配置された（本文の実質的な変更は `--background` エイリアスの追記のみ）。
- changelog ページに v2.1.193（2026年06月25日）のリリースエントリが追加された（changelog リンク不使用ポリシーによりリンクは付しません）。
- 見出しの字句修正が複数入った（docs_map 反映: 「Claude.ai」→「claude.ai」、「MCP Tool Search」→「MCP tool search」、「Excluding sensitive files」→「Exclude sensitive files」、「Managing plugins」→「Manage plugins」、「Background bash commands」→「Background Bash commands」、「Code Review Command」→「Pull Request Review Command」）。
- 環境変数 `CLAUDE_CODE_OPUS_4_6_FAST_MODE_OVERRIDE` の説明から「Opus 4.6 で Fast mode を使う方法」の案内が削除された（Opus 4.6 の Fast mode 廃止に伴う。詳細はハイライト 3 参照）。
<!-- light:minor-updates:end -->

## 新着情報

<!-- light:whats-new:start -->
今回、週刊ダイジェスト「新着情報」に 2 ページ（Week 25・Week 26）が追加されました。いずれも対応する日本語ページは未公開のため、英語リンクのみを記載します。

- [**2026年06月15日～19日(Week 25)**](#2026年06月15日19日week-25) ([English](https://code.claude.com/docs/en/whats-new/2026-w25)):  
  Artifacts（セッションから共有可能なライブページを公開、Team/Enterprise ベータ）、deny／ask ルールでのツール入力パラメータ一致（`Tool(param:value)` 構文）、`/config key=value` でプロンプトから任意の設定を変更、の 3 機能を紹介（リリース v2.1.178〜v2.1.183）。
- [**2026年06月22日～26日(Week 26)**](#2026年06月22日26日week-26) ([English](https://code.claude.com/docs/en/whats-new/2026-w26)):  
  `claude mcp login`／`logout` によるシェルからの MCP サーバー認証、`!` プレフィックスのシェルモードでコマンド出力への応答が得られるようになった点、の 2 機能を紹介（リリース v2.1.185〜v2.1.193）。
<!-- light:whats-new:end -->

## 2026年06月15日～19日(Week 25)

Week 25（リリース v2.1.178〜v2.1.183、3 機能）のダイジェストです。主要機能は次の 3 つです。

- **Artifacts**: Claude Code がセッションから claude.ai の非公開 URL にライブで対話的なページを公開し、セッションの進行に合わせてその場で更新する機能。ターミナルのテキストが不向きな出力（diff を注釈付きで示す PR ウォークスルー、セッションデータから作るダッシュボードなど）に使う。Team／Enterprise プランでベータ。
- **入力パラメータでの一致（Match by input parameter, v2.1.178)**: deny／ask の権限ルールが `Tool(param:value)` 構文でツールの入力パラメータに一致できるようになった。例えば `Agent(model:opus)` は Opus を要求するサブエージェント起動に一致し、値には `*` ワイルドカードも使える（`Agent(isolation:*)`）。
- **プロンプトから任意の設定を変更（v2.1.181）**: `/config` に `key=value` を渡すと、設定画面を開かずに設定を直接変更できる。`-p` フラグの非対話モードや Remote Control からも使える。

このほか「Other wins」として、auto mode が（ユーザーが破棄を求めていない場合に）`git reset --hard`・`git clean -fd`・`git stash drop` などの破壊的 git コマンドや `terraform destroy` をブロックするようになった点、`attribution.sessionUrl` を `false` にしてコミット／PR から claude.ai セッションリンクを省ける点、`/config` 画面で Esc が保存して閉じる挙動に変わった点、ネストした `.claude/skills` ディレクトリのスキルが作業対象のファイル配下で読み込まれるようになった点（名前衝突時は `<dir>:<name>` 表記で併存）、ネットワークドライブ／クラウド同期フォルダでの Write／Edit のゼロバイト・切り詰めファイル生成の修正などが挙げられています。

- [Week 25 · June 15–19, 2026 - Claude Code Docs (English)](https://code.claude.com/docs/en/whats-new/2026-w25)

## 2026年06月22日～26日(Week 26)

Week 26（リリース v2.1.185〜v2.1.193、2 機能）のダイジェストです。主要機能は次の 2 つです。

- **CLI から MCP サーバーを認証（v2.1.186）**: 新しい `claude mcp login <name>`／`claude mcp logout <name>` で、対話的な `/mcp` メニューを開かずにシェルから設定済み MCP サーバーを認証できる。`claude mcp login` はサーバーの OAuth フローを直接実行し、`claude mcp logout` は保存済み認証情報を消去する。
- **シェルモードがコマンド出力に応答（v2.1.186）**: `!` プレフィックスで実行したコマンドの出力がトランスクリプトに入ると Claude から応答が得られるようになり、`! npm test` の失敗説明などを追加プロンプトなしで受け取れる。応答コストは通常プロンプトと同じ。従来どおり応答なしで出力だけをコンテキストに加える挙動に戻すには `respondToBashCommands` を `false` にする。

このほか「Other wins」として、`/rewind` が `/clear` 前の会話復帰に対応した点、`sandbox.credentials` 設定で認証ファイル・秘密環境変数の読み取りをブロックできる点、組織のモデル制限がモデルピッカー・`--model`・`/model`・`ANTHROPIC_MODEL` に適用される点、`autoMode.classifyAllShell` 設定の追加、`claude_code.assistant_response` の OTel ログイベント追加、バックグラウンドサブエージェントが自動拒否でなくメインセッションに権限プロンプトを表示するようになった点、`/install-github-app` が GitHub App のみのインストールに対応した点、ストリーミング応答の CPU 使用量約 37% 削減、`/review <pr>` が `/code-review medium` と同じレビューエンジンを使うようになった点などが挙げられています（個別の挙動の多くは上記「軽微な更新」にも反映しています）。

- [Week 26 · June 22–26, 2026 - Claude Code Docs (English)](https://code.claude.com/docs/en/whats-new/2026-w26)

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-06-25.md](./archives/latest/2026-06-25.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-06-25.md](./archives/latest-detail/2026-06-25.md)

<!--
base_commit: 5c948aaefc1e28588e1f2e87aacec146ee8128ac
head_commit: f8479a4b550c9535b7213945696494c0dca75fc8
generated_at_full: 2026-06-27T15:02:44+09:00
-->
