---
対象期間: 2026年07月28日 〜 2026年08月01日
作成日: 2026-08-01
---

# Claude Code 公式ドキュメント更新サマリ

```markdown
今回は約 5 日ぶんの差分で、changelog へのリリースエントリ追加はありません。前回サマリで見出しだけを報告した項目の本文が集約全文（`llms-full.txt`）に取り込まれて中身を確認できるようになったほか、Claude Desktop のセッション横断操作をはじめとする新しい変更も入っています。

主要なものを以下に挙げます。

1. Claude Desktop の Code タブで、Claude が他のセッションを一覧・確認し、メッセージ送信やリネーム・アーカイブまでできるようになった
2. 長時間放置した大きなセッションを再開するとき、サマリから再開するかフルのまま再開するかを選べるダイアログが出るようになった（Pro / Max）
3. auto モードが Team と Enterprise で既定利用可能になり、Owner による有効化が前提ではなくなった
4. テレメトリやフィーチャーフラグ取得を止める環境変数が Remote Control を使用不可にすることが明記され、専用のエラーメッセージが追加された
5. Microsoft Foundry の Azure ホスト型デプロイではツール検索とサーバーサイドツールが使えないことが、MCP・ツール・キャッシュの各ページに反映された
```

## ハイライト

1. [**Claude Desktop がセッションをまたいだ操作に対応**](./latest-detail.md#1-claude-desktop-がセッションをまたいだ操作に対応):  
  Claude に「どのセッションが認証まわりを触った？」「支払いのセッションにスキーマ変更を伝えて」のように頼めるようになった。アーカイブは常に事前確認が入り、誰も見ていないセッションとの送受信はできない。
2. [**長時間放置した大きなセッションをサマリから再開できるように**](./latest-detail.md#2-長時間放置した大きなセッションをサマリから再開できるように):  
  Pro / Max プランで、約 1 時間以上非アクティブかつ 10 万トークン超のセッションを再開すると、サマリ化するかそのまま読み込むかを選ぶダイアログが出る。以降のリクエストが運ぶ履歴の量が変わる。
3. [**auto モードが Team と Enterprise で既定利用可能に**](./latest-detail.md#3-auto-モードが-team-と-enterprise-で既定利用可能に):  
  要件の記述が「Owner が管理設定で有効化する必要がある」から「既定で利用可能。管理者は `permissions.disableAutoMode` で組織単位に無効化できる」に変わった。
4. [**テレメトリ無効化系の環境変数が Remote Control を使えなくする**](./latest-detail.md#4-テレメトリ無効化系の環境変数が-remote-control-を使えなくする):  
  `DISABLE_TELEMETRY` / `DO_NOT_TRACK` / `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` / `DISABLE_GROWTHBOOK` はいずれもフィーチャーフラグ評価を止めるため Remote Control が使えなくなる。専用メッセージが変数名を名指しする。
5. [**Microsoft Foundry の Azure ホスト型デプロイでツール検索とサーバーサイドツールが使えない**](./latest-detail.md#5-microsoft-foundry-の-azure-ホスト型デプロイでツール検索とサーバーサイドツールが使えない):  
  Azure ホスト型デプロイはツール検索をサーバー側で拒否するため MCP ツールは事前ロードになり、`ENABLE_TOOL_SEARCH` では上書きできない。WebSearch も呼び出しが失敗する。

## 新規追加されたページ

- [**クラウド環境の設定**](./latest-detail.md#1-クラウド環境の設定) ([English](https://code.claude.com/docs/en/cloud-environments)):  
  前回サマリで新設を報告したページ。今回の差分で本文が取り込まれ、Claude Code on the web から移った内容に加えて Default 環境の扱い・`/remote-env` による選択・環境のアーカイブといった新しい節があることが確認できた。
- [**AWS への Claude apps gateway デプロイ**](./latest-detail.md#2-aws-への-claude-apps-gateway-デプロイ) ([English](https://code.claude.com/docs/en/claude-apps-gateway-on-aws)):  
  同じく前回サマリで報告済みのページ。ECS Fargate または EKS、Amazon RDS for PostgreSQL、AWS Secrets Manager、IAM ロールによる Amazon Bedrock 認証で構成する実例で、Terraform 一式とテレメトリの配線も扱う。

## 大幅に更新されたページ

- [**Agent SDK TypeScript リファレンス**](./latest-detail.md#1-agent-sdk-typescript-リファレンス) ([English](https://code.claude.com/docs/en/agent-sdk/typescript)):  
  前回サマリで型名だけを報告した拡充の中身が読めるようになった。`getContextUsage()`、キュー済みメッセージも取り消す interrupt、fast mode の無効理由コードなどが追加。
- [**Claude Desktop**](./latest-detail.md#2-claude-desktop) ([English](https://code.claude.com/docs/en/desktop)):  
  セッション横断操作（ハイライト 1 参照）のほか、`claude_desktop_config.json` の MCP サーバーが同名定義とどう優先されるかが専用の小見出しにまとめられた。
- [**エラーリファレンス**](./latest-detail.md#3-エラーリファレンス) ([English](https://code.claude.com/docs/en/errors)):  
  自動再試行の節が「再試行する／しない」の 2 リストに整理され、`/security-review` の `origin/HEAD` 不在エラーとファイル権限ルールの警告が新設された。
- [**環境変数**](./latest-detail.md#4-環境変数) ([English](https://code.claude.com/docs/en/env-vars)):  
  オン / オフ変数の解釈規則が明文化され、`0` を入れても有効になる変数が列挙された。モデル既定値の変数群にも具体的な説明が入った。
- [**MCP**](./latest-detail.md#5-mcp) ([English](https://code.claude.com/docs/en/mcp)):  
  Microsoft Foundry の Azure ホスト型の制約（ハイライト 5 参照）に加え、`claude mcp list` の健全性表示や SSE トランスポートの案内、各種サンプルの刷新が入った。
- [**設定**](./latest-detail.md#6-設定) ([English](https://code.claude.com/docs/en/settings)):  
  `remote.defaultEnvironmentId` と `switchModelsOnFlag` が一覧に追加され、`settings.local.json` を gitignore する方式がグローバル除外ファイルへの追記に変わった。
- [**フックリファレンス**](./latest-detail.md#7-フックリファレンス) ([English](https://code.claude.com/docs/en/hooks)):  
  `PermissionRequest` の発火条件が「ダイアログが出るとき」から「権限判断が必要になったとき」に変わり、プロンプトを出せない場面での扱いが明示された。
- [**カスタムサブエージェント**](./latest-detail.md#8-カスタムサブエージェント) ([English](https://code.claude.com/docs/en/sub-agents)):  
  `name` に `:` を使えなくなり、プロジェクト配下の frontmatter フックを動かすにはワークスペース信頼が必要になった。
- [**プラグインマーケットプレイス**](./latest-detail.md#9-プラグインマーケットプレイス) ([English](https://code.claude.com/docs/en/plugin-marketplaces)):  
  組織設定から配布する場合のソース規則が追加され、プライベートリポジトリの節が手動操作とバックグラウンド更新に分割された。
- [**動的ワークフロー**](./latest-detail.md#10-動的ワークフロー) ([English](https://code.claude.com/docs/en/workflows)):  
  中断して再開したときにどのエージェントの結果がキャッシュから返るかの規則が、具体例つきで明文化された。
- [**Claude Code をウェブで使う**](./latest-detail.md#11-claude-code-をウェブで使う) ([English](https://code.claude.com/docs/en/claude-code-on-the-web)):  
  前回サマリで報告したページ再構成が集約全文にも反映され、多数のページの参照先がクラウド環境ページへ張り替えられた。
- [**Agent SDK 概要**](./latest-detail.md#12-agent-sdk-概要) ([English](https://code.claude.com/docs/en/agent-sdk/overview)):  
  導入コード例とインストール手順が削られ、使い分け表と機能一覧を中心にしたランディングページへ再構成された。

## 軽微な更新

今回の対象期間には changelog ページの更新がありません。以下ではハイライトと上記カテゴリに含めなかった変更を挙げます。

**新機能**

- `/goal` の評価モデルを変更できることが明記されました。評価は小型高速モデル（Claude API では既定で Haiku、サードパーティプロバイダでは各プロバイダのページを参照）で行われ、`ANTHROPIC_DEFAULT_HAIKU_MODEL` で変更できます。ただしこの変数は小型高速モデルを使う全ての場面に効き、`haiku` エイリアスの解決先や会話要約などのバックグラウンド処理も同じモデルになる、という警告付きです — [English](https://code.claude.com/docs/en/goal#how-evaluation-works)
- スクリーンリーダーモードで、確認行を読み上げ終えるまで 3 秒間 UI の描画を保留するようになりました。`CLAUDE_AX_STARTUP_QUIET_MS`（ミリ秒、既定 `3000`、`0` で無効、上限は 600000 = 10 分）で長さを変えられ、任意のキーで打ち切れます（v2.1.217 以降）。また入力行の末尾で入力しているあいだは入力した文字だけを書き出すようになり、スクリーンリーダーが 1 打鍵ごとに行全体を読み直さなくなりました（v2.1.219 以降） — [English](https://code.claude.com/docs/en/accessibility#turn-on-screen-reader-mode)
- Code Review が、ホストアプリケーションから要求された場合にレビュー結果を `ReportFindings` ツールで報告するようになりました。Claude Code は 1 件 1 エントリの findings リストとして描画し、各エントリにファイル位置・1 文の要約・`correctness` などのカテゴリタグを表示します。要求はどの effort レベルでも有効で、v2.1.218 以降が必要です。ターミナルの `/code-review` はフォークとして実行してテキストで報告し、`-p` 実行もテキスト出力・JSON 出力のいずれでもテキストで報告します。後からセッション内で指摘を修正すると再度報告され、各項目に fixed / skipped / no change needed が付きます — [English](https://code.claude.com/docs/en/code-review#review-a-diff-locally)
- ヘッドレス実行の `system/init` イベントに `mcp_servers` と `mcp_server_errors` が加わりました。`--mcp-config` の各エントリは起動時に検証され、`url` があるのに `type` が無いといった不正なものはスキップされたうえで実行は継続します。`mcp_server_errors` の `type` は `unknown_type` / `url_missing_type` / `invalid_config` / `reserved_name` などのスキップ理由で、配列が空でないことを CI のゲートに使えます。手で実行したときは stderr にも警告が出ますが、CI ランナーや SDK ホストが stderr を捕捉している場合はフィールドにのみ現れます（v2.1.219 以降） — [English](https://code.claude.com/docs/en/headless#stream-responses)
- `--forward-subagent-text` / `CLAUDE_CODE_FORWARD_SUBAGENT_TEXT` を有効にすると、サブエージェントがさらに生成したサブエージェントのメッセージもストリームに流れるようになりました。入れ子のサブエージェントのメッセージは、それを生成した Agent ツール呼び出しの ID を `parent_tool_use_id` に持つため、ID をたどれば入れ子構造を再構成できます（v2.1.219 以降。それ以前は入れ子のサブエージェントのメッセージは流れませんでした） — [English](https://code.claude.com/docs/en/headless#stream-responses)
- エンタープライズネットワーク設定に「Verify your configuration」の節が追加されました。プロキシ URL だけは起動時に検証され、`http://` スキームが無いなどでパースできない場合は起動を止めて変数名を示します。それ以外は後続のリクエストでエラーになるため、`claude --debug` のログで CA 証明書や mTLS の読み込み行を確認する方法と、`/status` の **Proxy** / **mTLS client cert** / **mTLS client key** / **Additional CA cert(s)** の各行の読み方が示されています — [English](https://code.claude.com/docs/en/network-config#verify-your-configuration)
- vim の NORMAL モードで、空のプロンプトのときに `←` を押すと agent view が開くようになりました（従来は INSERT モードのみで、NORMAL では何も起きませんでした。v2.1.219 以降） — [English](https://code.claude.com/docs/en/interactive-mode#vim-editor-mode)
- サーバー管理設定に「Environment variables and the approval dialog」の節が追加され、配信された `env` 変数のうちどれが承認ダイアログ無しで適用されるかが整理されました。機能やコマンドのトグル、`ANTHROPIC_MODEL` などのモデル関連、`DISABLE_AUTO_COMPACT` などのコンテキスト関連、端末 UI とアクセシビリティ、数値の上限・予算・タイムアウトは承認不要です。一方、プロキシ・ベース URL・`OTEL_EXPORTER_OTLP_ENDPOINT` に非空の値が入る場合は必ず承認が要ります。`CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` / `DISABLE_ERROR_REPORTING` / `DISABLE_TELEMETRY` / `DO_NOT_TRACK` の 4 つは変数名ではなく配信された値で判断され、`1` や `true` のような真の値なら承認不要、それ以外の非空の値ならダイアログが出ます（v2.1.218 以降） — [English](https://code.claude.com/docs/en/server-managed-settings#environment-variables-and-the-approval-dialog)

**機能改善**

- auto モードの組織要件が変わりました（詳細はハイライト 3 参照）
- Remote Control とフィーチャーフラグ評価の関係が明記されました（詳細はハイライト 4 参照）
- Microsoft Foundry の Azure ホスト型デプロイの制約が各ページに反映されました（詳細はハイライト 5 参照）。機能可用性のページでは Microsoft Foundry の説明から「Azure 上で」が外れて「Anthropic が運用」となり、ツール検索と Web 検索の行に Anthropic ホスト型デプロイ限定の注記が入りました。Agent SDK のツール検索ページとエージェントループのページにも同じ制約が反映されています — [English](https://code.claude.com/docs/en/feature-availability#features-available-on-every-provider)
- モニタリングの「Managed endpoints govern signal-specific endpoints」の節が「How managed settings lock the OTLP destination」に改称され、管理設定に置いた `OTEL_EXPORTER_OTLP_*` 変数がどの開発者側変数を起動時に取り除くかが、エンドポイント・プロトコル・認証情報・エクスポータ選択の 4 分類で整理されました。`OTEL_EXPORTER_OTLP_PROTOCOL` には「Claude Code に既定のプロトコルは無いので、`otlp` エクスポータを有効にするならこれか信号別の変数を設定すること」が加わり、設定が効いているかを `claude_code.session.count` メトリクスや `claude_code.user_prompt` イベントで確かめる手順も追加されました — [English](https://code.claude.com/docs/en/monitoring-usage#how-managed-settings-lock-the-otlp-destination)
- Claude apps gateway の支出上限で、リクエストごとの料金ティアの解決順が 3 段階として明文化されました。①上流のモデル ID に対する正確なレート、②その ID に対応づけた `models[].id` のレート（Amazon Bedrock の application-inference-profile ARN や Microsoft Foundry のデプロイ名のようにモデル名を含まない上流文字列を救済する。ゲートウェイ側に v2.1.218 以降が必要）、③未知モデルの既定ティア（100 万トークンあたり入力 5 ドル / 出力 25 ドル）。v2.1.218 より前は②が無く、テーブルに載らない上流 ID は設定側のレートが分かっていても未知モデル扱いでした — [English](https://code.claude.com/docs/en/claude-apps-gateway-spend-limits#how-enforcement-works)
- Claude apps gateway の設定リファレンスにも、承認ダイアログの対象が「既知の安全リストに無いカスタム環境変数」から「承認が必要な配信済み `env` 変数（プロキシやベース URL など）」に改められ、テレメトリ転送時にゲートウェイが push する 6 つの環境変数に `OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf` が明示されました。トレースに必要な `CLAUDE_CODE_ENHANCED_TELEMETRY_BETA=1` はゲートウェイが push しないため管理ポリシーの `env` で配る必要があり、その配信も承認ダイアログの対象になる旨が追記されています — [English](https://code.claude.com/docs/en/claude-apps-gateway-config#managed)
- プラグインの発見・検証まわりの説明が拡充されました。公式 Anthropic マーケットプレイスは起動時に自動追加されること、コード知能プラグインは言語サーバーのバイナリを自分で入れる必要があり、編集ごとに診断が返るため Claude が型エラーや import 漏れをその場で直せること、`/plugin disable|enable|uninstall` がパネルを開いたままにするのでスクリプトからは `claude plugin` を使うこと、`/reload-plugins` のスキル件数は `commands/` ディレクトリしか数えないため `0 skills` と出ても実際には再読み込みされていることなどが加わりました。プラグインリファレンスにも、プラグインテーマの保存形式、`@skills-dir` プラグインが親ディレクトリをたどらないこと、トラブルシュート表の各項目に具体的な確認コマンドが追加されています — [English](https://code.claude.com/docs/en/discover-plugins#official-anthropic-marketplace)
- スキルの探索規則が整理されました。節名が「Automatic discovery from parent and nested directories」から「Discovery from parent and nested directories」に変わり、起動ディレクトリからリポジトリルートまでの各 `.claude/skills/` を読むこと、起動ディレクトリより下の入れ子のスキルは起動時には読まれず Claude がそのサブディレクトリ内のファイルを読むか編集した時点で有効になること、Cowork セッションとクラウドセッションは手元の `~/.claude/skills/` を読まないことが明示されました。`/verify` が実行手順を `.claude/skills/verify/SKILL.md` に記録する仕組みと、v2.1.205 以降は誤った手順を直したときだけ書き換えるためコミットしても差分が出にくいことも加筆されています — [English](https://code.claude.com/docs/en/skills#discovery-from-parent-and-nested-directories)
- サンドボックス環境の選び方が表形式になりました。サンドボックス Bash ツール・サンドボックスランタイム・dev container・カスタムコンテナ・仮想マシン・Claude Code on the web の 6 つについて、何が隔離されるか・Docker が要るか・準備の手間を並べた比較表と、目的から出発して選ぶ表が追加されています — [English](https://code.claude.com/docs/en/sandbox-environments#compare-sandboxing-approaches)
- routines のページが、環境まわりの説明をクラウド環境ページに委ねる形に整理されました。実行が完全自律（権限モードの選択も承認プロンプトも無い）であること、到達範囲はリポジトリ・環境のネットワークとの変数・含めたコネクタで決まること、コネクタの通信は Anthropic のサーバー経由なので許可ドメインの変更が要らないこと、Claude が `claude/` 接頭辞のブランチには常に push でき、それ以外のブランチは保護・他人の PR・他人のコミットのいずれかがあれば拒否されることが明記されました — [English](https://code.claude.com/docs/en/routines#environments-and-network-access)
- プロンプトキャッシュのページに、キャッシュが何を節約しているのか（キャッシュ読み取りレートでの再処理）、`/compact` がキャッシュの温かい状態と冷えた状態でどう変わるか、サブスクリプションでは 1 時間 TTL が自動的に要求され、使用クレジットを使い始めると 5 分 TTL に落ちることが加筆されました — [English](https://code.claude.com/docs/en/prompt-caching#cache-lifetime)
- dev container のページに、リビルドをまたいで認証情報と設定を保つ手順が追加されました。`~/.claude` に名前付きボリュームをマウントするだけでは `~/.claude.json` が volume の外にあるためサインイン状態が保てないため、`CLAUDE_CONFIG_DIR` を同じパスに設定する必要があります。GitHub Codespaces でも同様で、`ANTHROPIC_API_KEY` か `claude setup-token` のトークンを Codespaces シークレットに置く方法が示されています — [English](https://code.claude.com/docs/en/devcontainer#persist-authentication-and-settings-across-rebuilds)
- Debian / Ubuntu 向けのインストール手順に、`curl` と `gnupg` が入っていない場合の対処と、署名鍵のフィンガープリント（`31DDDE24DDFAB679F42D7BD2BAA929FF1A7ECACE`）を `gpg --show-keys` で確認する手順が追加されました（Linux 版 Desktop のページも同様）。インストールのトラブルシュートにも、再インストール後に `claude --version` で確認する手順が各所に追加されています — [English](https://code.claude.com/docs/en/setup#install-with-linux-package-managers)
- Slack のページ冒頭に、Team / Enterprise ワークスペース向けにこの旧版を Claude Tag へ移行する旨の警告が置かれ（Pro / Max では引き続きこのページがセットアップ経路）、トラブルシュートに「Claude Tag のチャネルからセッションが開始できない」が追加されました。個人アカウントで作ったクラウド環境ではチャネルセッションを開始できないため、管理設定から組織共有環境として作り直す必要があります — [English](https://code.claude.com/docs/en/slack#troubleshooting)
- Claude Code on the web のクイックスタートで「Connect GitHub and create an environment」が「Connect GitHub」に改称され、Default 環境の確認手順、`/web-setup` が「Not signed in to Claude」と表示する場合の対処、コマンド自体が見つからない場合（API キー認証や組織による無効化）の切り分け、セットアップスクリプトが約 5 分の環境キャッシュ構築予算を超えた場合の対処が追加されました — [English](https://code.claude.com/docs/en/web-quickstart#connect-github)
- チェックポイントの「Restore vs. summarize」が「Guide a summary」に改称され、要約オプションの選び分けの説明がベストプラクティスのページ側に移りました。あわせて、チェックポイントの保存と削除の説明が能動的な言い回しに改められています — [English](https://code.claude.com/docs/en/checkpointing#rewind-and-summarize)
- Agent SDK のフックのページで、コールバックのタイムアウト時の挙動がイベント別に整理されました。`PreToolUse` はツールを実行せずタイムアウトを伝えるツール結果を返してターンを続け（v2.1.210 より前はユーザーによる拒否として報告していたため無人セッションが入力待ちで止まっていました）、`UserPromptSubmit` と `UserPromptExpansion` はポリシーゲートになりうるため必ずプロンプトをブロックし（v2.1.208 より前はクエリを `error_during_execution` で終了）、`Stop` と `SubagentStop` は警告を出して正常に停止します。利用可能なフックの表には `DirectoryAdded` が追加され、`PermissionRequest` の説明も「権限ダイアログが表示されるとき」から「ツール呼び出しに権限判断が必要になったとき」に改められました。`updatedInput` と `permissionDecision` の組み合わせ方も整理されています — [English](https://code.claude.com/docs/en/agent-sdk/hooks#hook-timeout)
- Agent SDK のファイルチェックポイントで、巻き戻し時にシンボリックリンク・ハードリンク・通常ファイル以外はスキップされ、その件数が `RewindFilesResult` の `skippedLinks` に入ることが明記されました（v2.1.216 以降。それ以前はリンク越しに書き込み・削除していました）。サブエージェントの編集が追跡対象外であること、例外として `context: fork` のスキルをフォアグラウンドで動かした場合は追跡されることも制限事項の表に加わりました — [English](https://code.claude.com/docs/en/agent-sdk/file-checkpointing)
- Python 版 Agent SDK リファレンスで、`interrupt()` がメッセージバッファをクリアしないため中断されたタスクのメッセージと `ResultMessage` が残り、新しいクエリの応答を読む前に `receive_response()` で吐き出す必要があることが明記されました。`terminal_reason` の `"aborted_streaming"` / `"aborted_tools"` の意味、単発の `query()` がエラー結果を出したあと `ClaudeSDKError` ではなく素の `Exception` を送出すること、`context-1m-2025-08-07` ベータが 2026 年 04 月 30 日で廃止されたことも追加されています。システムプロンプトの改変ページには、大きなカスタムプロンプトを Python から渡す場合は文字列ではなく `system_prompt={"type": "file", "path": "..."}` を使う（文字列はコマンドライン引数として渡されるため OS の上限を超えると `Argument list too long` で失敗する）という注意が加わりました — [English](https://code.claude.com/docs/en/agent-sdk/python)
- そのほか Agent SDK 各ページで、サンプルコードが実際に動く形に直されました。Python の例が `asyncio.run(main())` を伴う形に揃えられ（システムプロンプトの改変、スキル、プラグイン、ホスティング、ユーザー入力）、単発の `query()` がエラー結果のあとに送出／raise することの注意がセッション・MCP・構造化出力の各ページに入り、スキルのページには init メッセージの `skills` 配列で読み込みを確認する方法、プラグインのページにはチルダ展開が効かないことと存在しないパスは黙ってスキップされること、セッションストアのページには適合性テストの走らせ方、TODO 追跡のページには todo のライフサイクル、可観測性のページにはエクスポート失敗が既定では黙殺されるため `CLAUDE_CODE_OTEL_DIAG_STDERR=1` で表面化させる方法が加筆されています — [English](https://code.claude.com/docs/en/agent-sdk/skills)
- セキュリティのページで、クラウド実行のクリーンアップの説明が「クラウド環境はセッション完了後に自動的に終了される」から「セッションの VM は一定時間の無操作後に回収される」に変わりました。監査ログの説明も「クラウド環境での全操作」から「クラウドセッションでの全操作」に改められています — [English](https://code.claude.com/docs/en/security#cloud-execution-security)
- セキュリティガイダンスプラグインのページに、すでに書かれているコードの脆弱性を探したい場合の案内が追加されました。セッションで対象のファイルやディレクトリのレビューを頼むか、リポジトリ全体を多エージェントで走査する Claude Security プラグインを使う（`/security-review` は現在のブランチの変更しか見ない）という内容で、いずれも手元のチェックアウトのソースを読むもので稼働中のサイトを見るわけではない、と補足されています。冒頭にあった Code Review との使い分けの説明からも、この節への導線にこの用途が書き足されました。ガイダンスファイルのスコープ表では、プロジェクトローカル版の注記が「gitignore 済み」から「個人的な上書き用。`.gitignore` に追加すること」に修正されています — [English](https://code.claude.com/docs/en/security-guidance#how-this-fits-with-other-security-tools)
- Agent SDK のカスタムスラッシュコマンドで、プロンプトが渡す引数の数がプレースホルダより少ない場合、`$1` のような未対応のインデックス付きプレースホルダはコマンドテキストにそのまま残ることが明記されました — [English](https://code.claude.com/docs/en/agent-sdk/slash-commands#creating-custom-slash-commands)
- 細かな改善として、`/security-review` の説明が「ブランチと origin の既定ブランチの差分をレビューする」と具体化（コマンド一覧・セキュリティ）、`apiKeyHelper` や `gcpAuthRefresh` の説明の主語が Claude Code に統一（認証・Google Cloud の Agent Platform）、`ANTHROPIC_API_KEY` を設定済みならログインプロンプトの代わりにキーの承認を求められる旨が追加（概要・認証・クイックスタート）、advisor のエイリアスが「各モデルファミリの Claude Code 組み込み既定バージョン」に解決されると明確化、JetBrains の diff 表示先を `/config` の **Diff tool** で変えられることを追記、VS Code 拡張の自動再インストールを止める方法を追記、`git worktree add` の例のブランチ名を実在しそうな名前に変更（worktrees）、Claude Security プラグインのインストール失敗をメッセージ別に切り分ける手順を追加、といった更新が入りました — [English](https://code.claude.com/docs/en/commands#all-commands)

**その他**

- 文体の一括見直しが多数のページに入りました。受動態を能動態に直し、動作の主体を Claude Code / Claude / ユーザーのいずれかに明示する書き換えで、agent view・Amazon Bedrock・チャネルリファレンス・Claude in Chrome・コスト管理・ディープリンク・WSL 上の Desktop・機能概要・ゲートウェイ・GitHub Enterprise Server・用語集・JetBrains・大規模コードベース・LLM ゲートウェイ接続とプロトコル・モバイル・モデル設定・出力スタイル・プラグインヒント・プラグイン関連度・サンドボックス・インストールのトラブルシュート・ultraplan・ultrareview・音声入力・worktrees・Agent SDK のカスタムツールとセキュアデプロイと TypeScript v2 プレビューといったページが該当します。内容の変更を伴わないものがほとんどで、コスト管理は「サマリから再開」への参照が、モデル設定は `switchModelsOnFlag` への参照が加わり、あわせて `CLAUDE_CODE_SUBAGENT_MODEL` の説明が能動態に言い換えられただけです
- 例示用コードフェンスの書式が一括変更され、`text` ブロックに `wrap` 属性が付き、例示プロンプト先頭の `>` が除かれました。一般的なワークフロー・プロンプトライブラリ・MCP クイックスタート・GitLab CI/CD・エージェントチーム・動的ワークフロー・ベストプラクティス・クイックスタートおよび新着情報の各週ページが該当し、いずれも表示上の変更のみです
- 一部のページで図版の記述が重複して出力されるようになりました（データ使用・機能概要・Claude Code の仕組み・チャネルリファレンス・フックリファレンス・Agent SDK のコスト追跡と権限）。内容の変更はありません
- `/desktop` の対応環境が「macOS と Windows」から「macOS と x64 Windows」に統一され、claude.ai サブスクリプションが必要である旨も明記されました（コマンド一覧・Desktop・概要） — [English](https://code.claude.com/docs/en/commands#all-commands)

## 新着情報

（今回の対象期間では、新着情報ページ（`whats-new/`）に新しい週間ダイジェストは追加されていません。最新は Week 29（2026年07月13日～17日）のままで、Week 30 以降は本サマリ作成時点で未公開です。Week 13・14・15・22・25・29 の各ページに差分がありますが、いずれも例示用コードフェンスへの `wrap` 属性と `title` 属性の付与、および例示プロンプト先頭の `>` の除去という表示上の変更のみで、内容の追加・修正はありません。）

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-07-28.md](./archives/latest/2026-07-28.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-07-28.md](./archives/latest-detail/2026-07-28.md)

<!--
base_commit: 37f111d9d0c49fa9fd2ab79826f803c7de899551
head_commit: 2b1ea9facf64443e0a685bf0d7e42794cbbdc509
generated_at_full: 2026-08-02T19:02:34+09:00
-->
