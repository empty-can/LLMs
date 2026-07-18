---
対象期間: 2026年07月16日 〜 2026年07月17日
作成日: 2026-07-17
---

# Claude Code 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
今回の対象期間は、公式ドキュメントが Week 29（v2.1.207〜v2.1.212）のリリース群に追従した回です。新規ページ「Claude Code on mobile」と週刊ダイジェスト「Week 29」が索引に加わり、企業ランチャー統合ガイドの全文が集約全文（llms-full）にはじめて反映され、前回 pending だった各ページの本文もあわせて着地しました。

主要なものを以下に挙げます。

1. スマートフォンの Claude アプリ（iOS / Android）からクラウドセッション・Remote Control・プッシュ通知で Claude Code を操作する方法をまとめた新規ページ「Claude Code on mobile」が索引に追加された
2. 公開したアーティファクトが閲覧のたびに MCP コネクタを呼び出し、各閲覧者自身の接続を通じてライブデータの取得・操作を行えるようになった（v2.1.209 以降。Week 29 の目玉機能）
3. 視覚的なターミナル UI を線形テキストに置き換え VoiceOver / NVDA での読み上げに対応する「スクリーンリーダーモード」が Week 29 で紹介された（`--ax-screen-reader` / `CLAUDE_AX_SCREEN_READER` / `axScreenReader`）
4. 前回ハイライトの企業ランチャー統合ガイド（`CLAUDE_CODE_PROCESS_WRAPPER` / `processWrapper`）の全文が、今回はじめて集約全文（llms-full）に反映された
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**モバイル版 Claude Code ページの新設**](#1-モバイル版-claude-code-ページの新設):  
  スマホの Claude アプリを Claude Code のクライアントとして使う方法（クラウドセッション / Remote Control / Dispatch / プッシュ通知）を集約した新規ページが索引に追加された。
2. [**アーティファクトが MCP コネクタでライブデータを取得**](#2-アーティファクトが-mcp-コネクタでライブデータを取得):  
  公開ページが表示のたびに閲覧者自身の MCP コネクタを呼び出し、最新データの表示や副作用を伴うアクション実行を行えるようになった（Claude Code v2.1.209 以降）。Week 29 の目玉機能。
3. [**スクリーンリーダーモードでの Claude Code 利用**](#3-スクリーンリーダーモードでの-claude-code-利用):  
  視覚的ターミナル UI を線形テキストに置き換え、VoiceOver / NVDA が順に読み上げられるようにするモード。Week 29 でアクセシビリティページとともに取り上げられた。
4. [**企業ランチャー統合ガイドの本文が集約全文に反映**](#4-企業ランチャー統合ガイドの本文が集約全文に反映):  
  前回は索引のみだった `CLAUDE_CODE_PROCESS_WRAPPER` / `processWrapper` の専用ガイド全文が、今回はじめて集約全文（llms-full）に着地した。
<!-- light:highlight-list:end -->

## 1. モバイル版 Claude Code ページの新設

スマートフォンから Claude Code を扱う方法をまとめた「Claude Code on mobile」ページが新設され、ドキュメント索引（`llms.txt`）に追加されました。このページの前提は「Claude Code 専用のモバイルアプリは存在せず、iOS / Android 向け Claude アプリが Claude Code セッションの**クライアント**として機能する」という点です。スマホからは 3 つの接続先に到達できます。Anthropic 管理インフラ上で走る**クラウドセッション**（Claude Code on the web）、自分のマシンで走るセッションを操作する **Remote Control**、そしてデスクトップアプリにタスクを投げる **Dispatch** です。いずれもアプリの **Code** タブ（Dispatch はメッセージ送信）から扱います。アプリの入手は各ストアからのインストールに加え、セッション内で `/mobile`（`/ios` / `/android` も同義）を実行すると表示されるダウンロード用 QR コードからも行えます。サインインは Claude Code と同じ claude.ai アカウント／組織で行う必要があり、クラウドセッションと Remote Control は claude.ai アカウント必須のため Console API キーや Amazon Bedrock 等のサードパーティプロバイダーでは利用できません。

用途の使い分けとして、マシンをオフにしていてもよいタスクは Anthropic インフラで継続するクラウドセッション、ローカルのファイルシステム・ツール・MCP サーバーが要る作業は Remote Control、実行方法を Dispatch に任せたいときは Dispatch（Pro / Max プラン必須）が推奨されます。Remote Control ではセッションを `claude remote-control`（または既存セッションで `/remote-control`）で開始し、端末に表示されるセッション QR をスキャンするかアプリの一覧から選んで接続します。アプリで添付した画像・ファイルはローカルセッションにダウンロードされ `@` ファイル参照として渡されます。Remote Control が有効な間は、長時間タスクの完了時や判断が必要なときにプッシュ通知が届き、プロンプトに `notify me when the tests finish` のように書いて明示的に要求することもできます。**制限**として、`/plugin` や `/resume` などターミナル UI 専用コマンドはアプリから動作せず、権限モードはアプリからは Bypass permissions を選べない（Remote Control では Auto も不可）、Dispatch は Team / Enterprise では使えず Pro / Max プラン必須、といった点が明記されています。

- [Claude Code on mobile - Claude Code Docs (English)](https://code.claude.com/docs/en/mobile)

## 2. アーティファクトが MCP コネクタでライブデータを取得

公開したアーティファクト（claude.ai 上のライブなインタラクティブページ）が、**表示されるたびに MCP コネクタを呼び出して現在のデータを取得できる**ようになりました。これにより、ダッシュボードなどのページが「作成したセッション時点のスナップショット」ではなく最新データを表示し、必要に応じて操作も実行できます。プロンプトでコネクタ名と取得したいデータを指定すると（例: 「open PR の一覧を GitHub コネクタ経由でロード時に取得するダッシュボードを作って」）、Claude は公開時にページが呼び出しうるコネクタを宣言し、ページはその宣言の外のコネクタを呼べません。対象は claude.ai アカウントのコネクタに限られ、`.mcp.json` 等のローカル MCP サーバーはページ構築時のデータ供給には使えても公開ページからは呼べません。アーティファクトからのコネクタ呼び出しは Pro / Max / Team / Enterprise プランで利用でき、**Claude Code v2.1.209 以降**が必要です（それ以前はセッション中に集めたデータで公開されます）。

閲覧者側の挙動が要点です。公開ページがコネクタを呼ぶとき、呼び出しは**公開者ではなく閲覧者自身のアカウント**を通じて実行されます。したがって同じダッシュボードでも閲覧者ごとにアクセスできるデータが異なり、ページが認証情報を見ることはなく claude.ai が代理で呼び出します。閲覧者はページ最初のコネクタ呼び出し前に権限を承認する必要があり、拒否や未接続の場合はライブセクションなしでページが表示されます。副作用を伴うアクション（メッセージ投稿や issue 更新など）も選択した閲覧者のアカウントで行われます。コネクタを呼ぶアーティファクトはどのプランでも公開リンクにできず、Team / Enterprise では組織内共有、Pro / Max では自分だけのプライベートに留まります。あわせて Week 29 では公開共有リンク・共有編集用の editor ロール（Team / Enterprise）・Claude Tag セッション由来のアーティファクト作成も追加されています。

- [セッション出力をアーティファクトとして共有する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/artifacts#pull-live-data-with-mcp-connectors)
- [Share session output as artifacts - Claude Code Docs (English)](https://code.claude.com/docs/en/artifacts#pull-live-data-with-mcp-connectors)

## 3. スクリーンリーダーモードでの Claude Code 利用

Week 29 のもう一つの目玉として、視覚的なターミナル UI をプレーンな線形テキストに置き換える**スクリーンリーダーモード**が取り上げられました。ボックス罫線・進捗アニメーション・その場再描画をやめ、ラベル付きの行を順に出力するため、VoiceOver や NVDA が端から端まで読み上げられ、会話・ツール権限の承認・出力確認を音声だけで完結できます。有効化はオプトインで、使用頻度に応じて 3 通りから選べます（優先順位が高い順）: 1 セッション限定の `claude --ax-screen-reader` フラグ、シェル単位の `CLAUDE_AX_SCREEN_READER=1` 環境変数、マシン全体の `"axScreenReader": true` 設定です。モードが有効なとき、Claude Code は最初に `[Screen Reader Mode: on via flag/env/settings]` の確認行を出力します（この命名形式は v2.1.206 以降。モード自体は v2.1.181 以降が必要）。

出力はフラットテキストになり、罫線・色のみのキュー・未変更コンテンツの再描画がなくなり、表は `Header: value` の文として読み上げられます（v2.1.198 以降）。各メッセージは `you:` / `claude:` / `tool:` / `Permission Required:` 等のラベルで始まり、ターミナルのスクロールバック検索でセクション間をジャンプできます。メニューや権限プロンプトは番号付きリストになり、番号入力で選択、yes/no は `y` / `n` を入力して答えます。長時間ツールの完了や権限待ちではターミナルベルで通知します。なお、スクリーンリーダーが動いていても自動では有効化されない点、`-p` 非対話モードには影響しない点などが既知の制限として挙げられています。スクリーン拡大鏡向けの `CLAUDE_CODE_ACCESSIBILITY`、アニメーション抑制の `prefersReducedMotion`、色覚対応テーマ（`dark-daltonized` / `light-daltonized`）といったモード外の設定も同ページで案内されています。

- [スクリーンリーダーで Claude Code を使用する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/accessibility#turn-on-screen-reader-mode)
- [日本語](https://code.claude.com/docs/ja/accessibility#turn-on-screen-reader-mode) / [Use Claude Code with a screen reader - Claude Code Docs (English)](https://code.claude.com/docs/en/accessibility#turn-on-screen-reader-mode)

## 4. 企業ランチャー統合ガイドの本文が集約全文に反映

前回（2026年07月16日サマリ）でハイライトとして取り上げた「企業ランチャーの背後で Claude Code を実行する」ガイドは、当時は索引（`llms.txt`）にのみ追加され本文が集約全文（`llms-full.txt`）に未反映でしたが、今回はじめて全文が集約エクスポートに着地しました。内容は既報どおり、企業の必須ランチャー経由で Claude Code が自身のバイナリから起動するプロセス（バックグラウンドサービス、agent view の各セッション、更新後の自己再起動など）をラップするための `CLAUDE_CODE_PROCESS_WRAPPER` 環境変数（v2.1.208 以降）と、同値を名前付き設定キーとして持つ `processWrapper` 設定（v2.1.210 以降）の使い方をまとめたものです。`PATH` 上の `claude` をラップするランチャーではこれらのプロセスに届かない点、Windows では `exec` 非対応のため無視される点が要点として示されます。

セットアップは「`exec "$@"` で終わる実行可能スクリプトを絶対パスに作成 → 設定ファイルの `env` ブロック（またはトップレベルの `processWrapper` キー）に絶対パスを設定 → `claude daemon stop --any` でバックグラウンドサービスを再起動 → `/status` の Self-exec エントリで検証」という手順です。managed 設定値がユーザー設定・シェル export より優先され、プロジェクト／ローカル設定からは指定できません。ランチャーコントラクトとして、引数の並べ替え・吸収・前置の禁止、継承した環境変数の全通過、約 3 秒以内の `exec` 到達、自己ネスト呼び出しへの耐性などが定義され、値は（シェルコマンドではなく）引数リストとして解析されます（空白でトークン分割、二重引用符でグループ化、`[` 始まりは JSON 文字列配列）。値が使えない場合はプロセスをラップなしで起動する代わりに起動を拒否します。シェルコマンドをラップする `CLAUDE_CODE_SHELL_PREFIX` とは別系統である点も明記されています。

- [企業ランチャーの背後で Claude Code を実行する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/corporate-launcher#what-the-launcher-covers)
- [Run Claude Code behind a corporate launcher - Claude Code Docs (English)](https://code.claude.com/docs/en/corporate-launcher#what-the-launcher-covers)

## 新規追加されたページ

<!-- light:new-pages:start -->
- [**Claude Code on mobile**](#1-モバイルでの-claude-code-利用) ([English](https://code.claude.com/docs/en/mobile)):  
  スマホの Claude アプリから Claude Code を操作する方法を集約した新規ページ（日本語ページは未作成のため英語のみ。詳細はハイライト1参照）。
<!-- light:new-pages:end -->

## 1. モバイルでの Claude Code 利用

iOS / Android 向け Claude アプリを Claude Code のクライアントとして使う方法をまとめた新規ページが、ドキュメント索引に追加されました。クラウドセッション・Remote Control・Dispatch の 3 経路と、プッシュ通知・制限事項を扱います。内容の詳細はハイライト1を参照してください（現時点で日本語ページは未提供のため、参考リンクは英語のみです）。

- [Claude Code on mobile - Claude Code Docs (English)](https://code.claude.com/docs/en/mobile)

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
- [**Run Claude Code behind a corporate launcher**](#1-企業ランチャーの背後で-claude-code-を実行する) ([日本語](https://code.claude.com/docs/ja/corporate-launcher#what-the-launcher-covers) / [English](https://code.claude.com/docs/en/corporate-launcher#what-the-launcher-covers)):  
  前回索引のみだった企業ランチャー統合ガイドの全文が、今回はじめて集約全文に反映された（詳細はハイライト4参照）。
<!-- light:updated-pages:end -->

## 1. 企業ランチャーの背後で Claude Code を実行する

`CLAUDE_CODE_PROCESS_WRAPPER` / `processWrapper` による企業ランチャー統合を解説する専用ページの全文が、今回はじめて集約全文（`llms-full.txt`）に反映されました。前回サマリでは索引追加のみを検出しハイライトとして扱っていましたが、今回で本文（「ランチャーがカバーするもの」「ランチャーのセットアップ」「ランチャーコントラクト」「`CLAUDE_CODE_SHELL_PREFIX` との関係」など）が集約エクスポート側でも参照可能になりました。内容の詳細はハイライト4を参照してください。

- [企業ランチャーの背後で Claude Code を実行する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/corporate-launcher#what-the-launcher-covers)
- [Run Claude Code behind a corporate launcher - Claude Code Docs (English)](https://code.claude.com/docs/en/corporate-launcher#what-the-launcher-covers)

## 軽微な更新

<!-- light:minor-updates:start -->
今回の対象期間は Week 29（v2.1.207〜v2.1.212）への追従回で、軽微な変更は大きく 2 系統に分かれます。①前回サマリで「`docs_map` に見出しは追加されたが本文が集約全文に未反映」と記録していた各ページ本文が、今回まとめて集約全文（`llms-full.txt`）に着地したもの。②今回新たに `docs_map` に追加された Week 29 分の見出し群で、対応本文はまだ集約全文に未反映のもの。いずれも構造・索引側の変化が主体のため、各項目の内容要約は本文が反映された回に譲り、下記は変更のあったページ・節の記録に留めます（個別リンクは付けません）。

**機能改善**（前回 pending の本文が集約全文に着地）

- `sessions`: 「What a resumed session restores」（resume が復元する範囲）
- `sub-agents`: 「Subagent output scanning」（サブエージェント出力のスキャン）
- `workflows`: 「Dismiss or turn off the keyword」「Where the keyword works」（起動キーワードの無効化と有効範囲）
- `worktrees`: 「Clean up subagent and background-session worktrees」「Worktree removal on Windows」（サブエージェント／バックグラウンドセッションの worktree 掃除、Windows での削除）
- `chrome`: 「Upload files to web pages」「Save screenshots to disk」（Web ページへのファイルアップロード、スクリーンショットのディスク保存）
- `authentication`: 「Restrict login to your organization」（組織へのログイン制限）
- `auto-mode-config`: 「Add a human checkpoint」（人手チェックポイントの追加）
- `network-config`: 「Apply network settings to background agents」「Configure a corporate launcher as a setting」「Set network variables in settings, not the shell」（バックグラウンドエージェントへのネットワーク設定適用、ランチャーを設定として構成、設定ファイルでのネットワーク変数指定）
- `zero-data-retention`: 「Route Claude Code traffic to your ZDR organization」（ZDR 組織へのトラフィックルーティング）
- `claude-platform-on-aws`「4. Launch and verify」／`google-vertex-ai`「6. Verify your configuration」（各セットアップ手順への検証ステップ）
- `tools-reference`: Bash ツール挙動に「What persists between commands」「Timeout and output limits」「Background commands」
- トラブルシュート項目: `errors`「Memory index is over its read limit」「This session has no saved transcript」、`agent-view`「Opening a session says it has no saved transcript」、`claude-code-on-the-web`／`github-enterprise-server`「Unable to get organization UUID」系、`deep-links`「xdg-open is not found on Linux」

**その他**（今回 `docs_map` に追加された Week 29 分の見出し。対応本文は集約全文に未反映）

- `remote-control`: 「Session URL reminders」（セッション URL のリマインド）
- `agent-view`: 「Send the session to the background」「Copy the session with /fork」「What carries over when you background」「List sessions as JSON」（`/fork` によるバックグラウンドセッション化、`claude agents --json` 相当のセッション一覧）
- `sub-agents`: 「Session subagent limit」／`tools-reference`（WebSearch）「Session search limit」（サブエージェント生成・WebSearch のセッション上限。既定各 200）
- `mcp`: 「Automatic backgrounding of long tool calls」（長時間 MCP ツール呼び出しの自動バックグラウンド化）
- `skills`: 「Skills in Cowork and cloud sessions」（Cowork / クラウドセッションでのスキル）
- `errors`: 「EUNKNOWN when starting a background session」（バックグラウンドセッション起動時の EUNKNOWN）
- `fast-mode`: 「Use fast mode behind proxies and LLM gateways」（プロキシ／LLM ゲートウェイ配下での fast mode）
- `worktrees`: セクション構成の大幅再編（「Set up the worktree environment」「Ask Claude to create a worktree」「Resume a worktree session」「Customize worktree creation」「Branch from a pull request」「Replace worktree creation with a hook」「What worktrees share with the main checkout」「Troubleshooting」ほか）
- `mcp-quickstart`: 「Connection timing」（MCP サーバー接続のタイミング）
- 用語集（glossary）に「Connector」「MCP server」を追加
- SDK リファレンス: 型「TaskBudget」を追加、ツール「BashOutput」「KillBash」を「TaskOutput」「TaskStop」に改称
- 参考: これら Week 29 分の各機能は、新着情報「Week 29」ダイジェストで機能単位に解説されています（本サマリ「新着情報」参照）。
<!-- light:minor-updates:end -->

## 新着情報

<!-- light:whats-new:start -->
- [**2026年07月13日～17日(Week 29)**](#2026年07月13日17日week-29) ([English](https://code.claude.com/docs/en/whats-new/2026-w29)):  
  MCP コネクタ連携アーティファクトとスクリーンリーダーモードを目玉に、v2.1.207〜v2.1.212 の変更を集約した週刊ダイジェスト（日本語ページは未作成のため英語のみ）。
<!-- light:whats-new:end -->

## 2026年07月13日～17日(Week 29)

週刊ダイジェスト「Week 29」が索引に追加されました。対象リリースは v2.1.207〜v2.1.212 で、目玉は 2 件です。**アーティファクトの MCP コネクタ連携**（公開ページが表示のたびに閲覧者自身のコネクタを呼びライブデータを取得。詳細はハイライト2参照）と、**スクリーンリーダーモード**（`claude --ax-screen-reader` などで有効化。詳細はハイライト3参照）です。

そのほかの主な変更（Other wins）は次のとおりです。

- `/fork` が会話を新しいバックグラウンドセッションへコピーし、`claude agents` に独自の行を持たせながら作業を続けられるようになった。従来 `/fork` が起動していたセッション内フォーク・サブエージェントは `/subtask` に改称。
- Amazon Bedrock / Google Cloud の Agent Platform / Microsoft Foundry で Auto モードに `CLAUDE_CODE_ENABLE_AUTO_MODE` のオプトインが不要になった。管理者は `disableAutoMode` で無効化できる。
- 2 分を超える MCP ツール呼び出しが自動的にバックグラウンドへ移り、セッションを使い続けられるようになった。しきい値は `CLAUDE_CODE_MCP_AUTO_BACKGROUND_MS` で調整・無効化できる。
- `claude auto-mode reset` で Auto モード設定を既定へ戻せるようになった（`--yes` で確認プロンプトをスキップ）。
- 企業ランチャー対応: `CLAUDE_CODE_PROCESS_WRAPPER` または `processWrapper` 設定で、Claude Code が自身のバイナリから起動するプロセスを必須ラッパー経由で実行できる（詳細はハイライト4参照）。
- `vimInsertModeRemaps` 設定で、vim モードの挿入モードにおける `jj` などの 2 キー連続入力を Escape にマップできる。
- `--forward-subagent-text` フラグと `CLAUDE_CODE_FORWARD_SUBAGENT_TEXT` により、stream-json 出力にサブエージェントのテキスト・思考ブロックを含められる。
- 暴走ループ防止のセッション上限: WebSearch 呼び出しとサブエージェント生成が各既定 200 になり、`CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION` / `CLAUDE_CODE_MAX_SUBAGENTS_PER_SESSION` で調整できる。
- 「Always allow」の権限ルールがリポジトリルートに保存されるようになり、git worktree で付与した承認がセッション・worktree をまたいで持続する。
- Amazon Bedrock / Google Cloud の Agent Platform / Claude Platform on AWS の既定モデルが Claude Opus 4.8 になった。
- 折りたたみ時のツール要約行に経過時間カウンターが表示され、長時間ツールが止まって見えず動作中とわかるようになった。

- [Week 29 · July 13–17, 2026 - Claude Code Docs (English)](https://code.claude.com/docs/en/whats-new/2026-w29)

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-07-16.md](./archives/latest/2026-07-16.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-07-16.md](./archives/latest-detail/2026-07-16.md)

<!--
base_commit: 5cf373da86d5703c50540e7e49df4d79e33d4c76
head_commit: 9ec2f2d1cbe194850dc2cd57ad42803d8aa90d80
generated_at_full: 2026-07-18T15:01:04+09:00
-->
