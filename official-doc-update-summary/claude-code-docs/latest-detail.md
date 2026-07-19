---
対象期間: 2026年07月17日 〜 2026年07月18日
作成日: 2026-07-18
---

# Claude Code 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
今回の対象期間は、セキュリティ・権限まわりの新規変更に加え、前回まで索引・`docs_map` のみだった多数のページ本文が集約全文（llms-full.txt）へまとめて着地した「本文キャッチアップ」回です。新規の索引ページ・新着情報ページの追加はありませんでした。

主要なものを以下に挙げます。

1. 権限チェックのハードニングと会話終了ツール（EndConversation）を中心とする changelog リリース v2.1.214（2026年07月18日）が追加された
2. 企業向けゲートウェイのドキュメントに、Claude Desktop の埋め込みセッションへポリシーを配信する `parentSettingsBehavior: "merge"` と、親設定を制限する `allowManaged*Only` ロック群という新セクションが加わった
3. 組織ログイン制限の `forceLoginMethod` が、ターミナルだけでなく VS Code 拡張・Agent SDK・`claude setup-token`・`/install-github-app` を含む全ログイン経路で強制されることが明記された（v2.1.212 以降）
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**権限チェックのハードニングと会話終了ツールの追加**](#1-権限チェックのハードニングと会話終了ツールの追加):  
  changelog に v2.1.214（2026年07月18日）が追加。多数の権限バイパス修正と、悪用・脱獄試行のセッションを終了できる EndConversation ツールが目玉。
2. [**企業向けゲートウェイの親設定制御**](#2-企業向けゲートウェイの親設定制御):  
  Claude Desktop の埋め込みセッションへゲートウェイのポリシーを配信する `parentSettingsBehavior: "merge"` と、親設定を制限する 5 つの `allowManaged*Only` ロックの新セクションが追加された。
3. [**forceLoginMethod の全ログイン経路への強制**](#3-forceloginmethod-の全ログイン経路への強制):  
  組織ログイン制限がターミナル・VS Code 拡張・Agent SDK・`claude setup-token`・`/install-github-app` の全経路で `forceLoginMethod` を強制することが明記された（v2.1.212 以降）。
<!-- light:highlight-list:end -->

## 1. 権限チェックのハードニングと会話終了ツールの追加

changelog に v2.1.214（2026年07月18日）が追加されました。このリリースは**権限（permission）チェックのハードニング**が主眼で、自動承認の抜け穴を塞ぐ修正が多数含まれます。具体的には、`Edit(src/**)` のような単一セグメントの `dir/**` 許可ルールがツリー内のどこにある `dir/` への書き込みでも自動承認していた不具合（`<cwd>/dir` のみに限定するよう修正）、Windows PowerShell 5.1 セッションでの権限チェックバイパス、bash が権限アナライザーと異なる解釈をするファイルディスクリプタ・リダイレクト形式での fail-closed 化、10,000 文字超のコマンドを常にプロンプト表示、`[[ ]]` 比較内の zsh 変数サブスクリプト・修飾子の承認要求、安全でないオプションを走らせうる一部の `help` / `man` コマンドの自動承認停止、リモートセッションでローカル確認ダイアログより先に処理が進みうる問題、そして Podman の `docker` シムを含むデーモンリダイレクト系フラグ（`--url` / `--connection` / `--identity` 等）を伴う `docker` コマンドへのプロンプト追加などです。

新機能として、claude.ai で 2025 年から運用されているのと同様に、極めて悪質なユーザーや脱獄（jailbreak）試行に対して Claude がセッションを終了できる **EndConversation ツール**が追加されました。あわせて、長時間サイレントだったツール呼び出しに定期的な進捗ハートビートが加わり、メモリファイルの frontmatter に ISO 形式の `modified` タイムスタンプ、OpenTelemetry ログイベントにメッセージ単位の相関・ツール来歴用の `message.uuid` / `client_request_id` / `tool_source` 属性（および 60KB 切り詰めを調整する `CLAUDE_CODE_OTEL_CONTENT_MAX_LENGTH`）、`subagentStatusLine` ペイロードへの reasoning effort が追加されました。その他、Windows の PowerShell ツール関連（UTF-16LE 出力・UnicodeDecodeError・標準入力待ちでのハング・`where.exe`/`fc.exe` の誤エラー扱いなど）、バックグラウンドデーモンの制御ソケット取り違え、完了済みバックグラウンドセッションの削除不能、スケジュールタスクが自身の割当プロンプトを不審入力として拒否する問題、`/ultrareview` がマージベースの無いリポジトリで動かない点、`--settings` 由来プラグインの読み込み不全（v2.1.181 からのリグレッション）など、多数のバグ修正が含まれます。

## 2. 企業向けゲートウェイの親設定制御

企業向けゲートウェイのページ（Claude apps gateway）に、**Claude Desktop の埋め込み Claude Code セッションへポリシーを配信する仕組み**と、**親設定（parent settings）を制限する仕組み**という 2 つの新セクションが追加されました。中心となるのが `parentSettingsBehavior: "merge"` 設定です。Claude Desktop は自身が起動する Claude Code セッションにゲートウェイのポリシーを親設定として渡しますが、管理者配備の managed ソースがあるマシンでは、最優先ソースが `parentSettingsBehavior: "merge"` をオプトインしない限り親設定は無視されます。Claude Desktop しか動かないマシンでは、この親設定がゲートウェイのポリシーを埋め込みセッションに届ける唯一の経路のため、オプトインが無いとセッションはゲートウェイの制限をまったく受けずに動作してしまう点が注意喚起されています。一方、開発者が `/login` でサインインするマシンや `policyHelper` を構成したフリートではオプトインは不要／不可です。

もう一方の「Restrict parent settings」セクションは、`merge` を有効化すると Claude Desktop に限らず Agent SDK アプリや IDE 拡張などホストプロセス全般が親設定を供給できるようになるため、それを制限する 5 つの `allowManaged*Only` ロック（`allowManagedPermissionRulesOnly` / `allowManagedMcpServersOnly` / `allowManagedHooksOnly` と 2 つのサンドボックスロック）とその配備方法を説明します。ロックをかけても許可方向に働くキーが残るため、組織の許可リストをロックと同じソースに併記すべきこと、5 つのロックを設定しても honored される 4 つの親設定（`forceLoginOrgUUID` / `allowedMcpServers` / `availableModels` / `strictPluginOnlyCustomization`）などが整理されています。あわせて `claude-apps-gateway-config` のクライアント側管理設定や、`settings` / `server-managed-settings` の優先順位の記述にも `parentSettingsBehavior` と `policyHelper` 配下の読み取り規則が反映されました。

- [Claude apps gateway for Amazon Bedrock, Claude Platform on AWS, Google Cloud, and Microsoft Foundry - Claude Code Docs (English)](https://code.claude.com/docs/en/claude-apps-gateway#deliver-policy-to-claude-desktop-sessions)
- [Claude apps gateway for Amazon Bedrock, Claude Platform on AWS, Google Cloud, and Microsoft Foundry - Claude Code Docs (English)](https://code.claude.com/docs/en/claude-apps-gateway#restrict-parent-settings)

## 3. forceLoginMethod の全ログイン経路への強制

認証ページの「Restrict login to your organization（組織へのログイン制限）」に、`forceLoginMethod` / `forceLoginOrgUUID` の**強制が及ぶログイン経路**が明記されました。開発者はターミナルの `/login`、VS Code 拡張、Agent SDK、`claude setup-token`、`/install-github-app` の複数経路からログインできますが、Claude Code v2.1.212 以降は**すべての経路で `forceLoginMethod` が強制**されます（v2.1.212 以前はターミナルログインのみが両キーを強制）。`forceLoginOrgUUID` の扱いは経路で異なり、ターミナル・VS Code 拡張・Agent SDK は両キーを強制する一方、`claude setup-token` と `/install-github-app` は `forceLoginMethod` のみを強制するため、別組織でトークンを発行しうる点が注意点として挙げられています。

この記述は、managed 設定を「デバイスへどう届けるか」を整理するページの「Login enforcement」制御行にも反映され、同行に上記の経路差が追記されました。

- [Authentication - Claude Code Docs (English)](https://code.claude.com/docs/en/authentication#restrict-login-to-your-organization)

## 新規追加されたページ

<!-- light:new-pages:start -->
（今回の対象期間では、`llms.txt`（索引）への新規ページ追加はありませんでした。前回索引のみだった「Claude Code on mobile」ページの本文が集約全文に着地しましたが、内容は前回サマリで既報のため「軽微な更新」に記録しています。）
<!-- light:new-pages:end -->

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
- [**Claude apps gateway（親設定の配信と制限）**](#1-claude-apps-gateway-の親設定制御) ([English](https://code.claude.com/docs/en/claude-apps-gateway#restrict-parent-settings)):  
  企業向けゲートウェイのページに、Claude Desktop へのポリシー配信と親設定の制限という 2 セクションが追加された（詳細はハイライト2参照）。
- [**Run parallel sessions with worktrees（ページ再構成）**](#2-worktrees-ページの再構成) ([English](https://code.claude.com/docs/en/worktrees#ask-claude-to-create-a-worktree)):  
  worktrees ページがセクション再構成され、`EnterWorktree` ツールによる worktree 作成/切替やクリーンアップ機構などの本文が集約全文に着地した。
<!-- light:updated-pages:end -->

## 1. Claude apps gateway の親設定制御

企業向けゲートウェイのページ（Claude apps gateway）に、「Deliver policy to Claude Desktop sessions」「Restrict parent settings」という 2 つの新セクションが追加されました。`parentSettingsBehavior: "merge"` によるポリシー配信のオプトインと、`allowManaged*Only` ロック群による親設定の制限を扱う、この対象期間で最も分量の多い新規本文追加です。内容の詳細はハイライト2を参照してください。

- [Claude apps gateway for Amazon Bedrock, Claude Platform on AWS, Google Cloud, and Microsoft Foundry - Claude Code Docs (English)](https://code.claude.com/docs/en/claude-apps-gateway#deliver-policy-to-claude-desktop-sessions)
- [Claude apps gateway for Amazon Bedrock, Claude Platform on AWS, Google Cloud, and Microsoft Foundry - Claude Code Docs (English)](https://code.claude.com/docs/en/claude-apps-gateway#restrict-parent-settings)

## 2. worktrees ページの再構成

git worktrees ページ（Run parallel sessions with worktrees）が大きく再構成され、集約全文（`llms-full.txt`）に本文が着地しました。「Start Claude in a worktree」直下に「Set up the worktree environment」「Ask Claude to create a worktree」などの節が新設され、セッション中に Claude が **`EnterWorktree` ツール**で worktree を作成・切替できること、リポジトリの `.claude/worktrees/` 外パスへ移動する際は承認が必要で `bypassPermissions` でのみスキップされること（v2.1.206 以降）、`--worktree` の対話実行にはワークスペース信頼が要ること、サブエージェント／バックグラウンドセッションの worktree 掃除や Windows での削除に関する記述などが含まれます。ページ構成の再編が主体で、対応機能の多くは前回サマリ（Week 29）で既報です。

- [Run parallel sessions with worktrees - Claude Code Docs (English)](https://code.claude.com/docs/en/worktrees#ask-claude-to-create-a-worktree)

## 軽微な更新

<!-- light:minor-updates:start -->
今回の対象期間は、原文差分の大半が集約全文（`llms-full.txt`）における本文の反映・改訂です。changelog v2.1.214 の個別修正はハイライト1に、企業ゲートウェイと worktrees の大規模な本文着地は上記カテゴリにまとめました。ここではそれ以外の、通常ドキュメントページ側の記述変更を挙げます。多くは前回サマリで「`docs_map`（索引）に見出しは追加されたが本文が集約全文に未反映」と記録していた各ページ本文が、今回まとめて着地したものです（対応機能は Week 29 等で既報のため、下記は変更のあった記述の記録に留めます）。

**新機能**（新規セクション・新エイリアス・新規イベント等）

- Agent SDK のフックリファレンス（「Available hooks」表）に、TypeScript SDK 限定の新規イベントとして `StopFailure`（API エラーでターン終了）・`PostCompact`（圧縮完了）・`PermissionDenied`（Auto モード分類器の拒否）・`TaskCreated`・`Elicitation` / `ElicitationResult`（MCP のユーザー入力要求と応答）・`InstructionsLoaded`（CLAUDE.md／rules の読み込み）・`CwdChanged`・`FileChanged` の各フックイベントを追加。
- `remote-control`: 新セクション「Session URL reminders」を追加（長時間ターンや連続する許可プロンプト時に、電話・ブラウザへ切り替えるためのセッション URL リンクをプロンプト上部に表示。v2.1.208 以降。無効化不可）。
- `routines`: `/schedule` コマンドに `/routines` エイリアスを追加。

**機能改善**（本文の着地・記述の明確化）

- `mobile`（Claude Code on mobile）: 前回索引のみだったページ本文が集約全文に着地（iOS/Android の Claude アプリをクライアントとして、クラウドセッション／Remote Control／Dispatch／プッシュ通知で Claude Code を操作。内容は前回サマリのハイライト1で既報）。
- `agent-view`: 前回 pending だった本文（「Send the session to the background」「Copy the session with /fork」「What carries over when you background」「List sessions as JSON」、および削除済みセッションを bare `/resume` ピッカーで復帰させる操作）が集約全文に着地。あわせて各所の「Before v2.1.xxx」版数注記を整理（実機能は Week 29 で既報）。
- `tools-reference`: WebSearch の「Session search limit」（1 セッション最大 200 回、`CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION` で調整、`/clear` でリセット）本文が着地。あわせて SDK ツールリファレンスの Agent/Task ツールに `model` / `run_in_background` / `name` / `mode` / `isolation` フィールドと詳細な出力スキーマを追記。
- `auto-mode-config`: `claude auto-mode defaults` / `config` の出力 JSON 例と、`claude auto-mode reset`（v2.1.212 以降。`--yes` で確認スキップ）の手順本文が着地。
- `authentication`: `claude setup-token` が `/login` と同じブラウザ認可フローでトークンを発行する点、および発行トークンは推論のみで claude.ai コネクタ取得や Remote Control には使えないがローカル設定の MCP サーバーは動作する点を明確化。
- `claude-apps-gateway-config` / `settings` / `server-managed-settings`: クライアント側管理設定への `parentSettingsBehavior: "merge"` 追加と、`policyHelper` 配下でのロックキー・親設定チェックの読み取り規則を明確化（ハイライト2関連）。
- managed 設定の配信ページ（「Login enforcement」制御行）: `forceLoginMethod` / `forceLoginOrgUUID` の強制経路の差を追記（ハイライト3参照）。
- `memory`（CLAUDE.md）: `/context` を実行して CLAUDE.md の読み込みを確認するヒントを追加。
- `headless`: `claude -p` の 3 出力形式（`text` / `json` / `stream-json`）の違いを明記。
- `monitoring-usage`: OTLP エクスポートに `Content-Length` ヘッダーを付与（v2.1.212。chunked 転送を拒む Azure Monitor 等の `411`/`400` エラーを回避）。`-p`／Agent SDK セッションで `TRACEPARENT` 設定時に OTLP イベントログへ `trace_id`/`span_id` を付与する挙動も追記。
- `prompt-caching`: LLM ゲートウェイやカスタム `ANTHROPIC_BASE_URL` 経由でキャッシュブレークポイントが拒否された場合、そのブロックを外してリクエストを再試行し、以降そのブロックを非キャッシュ化する挙動を明記。

**その他**

- `claude-code-on-the-web`: クラウドセッションで利用不可な項目に「リポジトリの `.claude/settings.json` `env` ブロックのトランスポート変数（`NODE_EXTRA_CA_CERTS` や mTLS クライアント証明書変数）」の行を追加（ホスティング環境が API 接続を管理するため無視され、デバッグログに記録される）。
- `chrome`（ブラウザ操作）: 記録した GIF にはログイン済みページのアカウント情報など画面に映るものがすべて含まれるため、チーム外へ共有する前に確認する注意を追加。
- 集約全文（`llms-full.txt`）の構成変更: `sandboxing` ページの掲載位置がファイル前方へ移動（内容の実質的変更なし）。Week 29 週刊ダイジェスト本文および「What's new」索引の Week 29 エントリも着地（内容は前回サマリで既報）。
- `fast-mode`: プロキシ／LLM ゲートウェイ配下での可用性チェックを回避する環境変数（`CLAUDE_CODE_SKIP_FAST_MODE_NETWORK_ERRORS` / `CLAUDE_CODE_SKIP_FAST_MODE_ORG_CHECK`）の新設を含むトラブルシュート節が着地。
- 上記のほか、`code-review` / `plugins`（marketplace・依存関係・plugin-hints）/ `permission-modes` / `sub-agents` / `sessions` / `settings`（優先順位）/ `mcp` / `network-config`（mTLS）/ `agent-sdk`（python・typescript）/ `env-vars` / 各トラブルシュート（`errors` ほか）/ `data-usage`（エラー報告）/ `ultrareview` 等の多数ページで、記述の明確化やバージョン注記の整理（多くは前回 `docs_map` 追加分の本文着地）が行われました。
<!-- light:minor-updates:end -->

## 新着情報

<!-- light:whats-new:start -->
（今回の対象期間では、新規の新着情報ページ（`whats-new/`）の追加はありませんでした。前回取り上げた Week 29 ダイジェストの本文が集約全文に着地しましたが、内容は前回サマリで既報のため「軽微な更新」に記録しています。）
<!-- light:whats-new:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-07-17.md](./archives/latest/2026-07-17.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-07-17.md](./archives/latest-detail/2026-07-17.md)

<!--
base_commit: 9ec2f2d1cbe194850dc2cd57ad42803d8aa90d80
head_commit: c7a24cbea7b808c9e8931fe91809d80b7495c53e
generated_at_full: 2026-07-19T15:05:11+09:00
-->
