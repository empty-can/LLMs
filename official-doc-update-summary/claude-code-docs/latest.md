---
対象期間: 2026年07月13日 〜 2026年07月14日
作成日: 2026-07-14
---

# Claude Code 公式ドキュメント更新サマリ

```markdown
今回の対象期間は、changelog に v2.1.209（1 件の修正）と大型の v2.1.208 追従ドキュメント、および v2.1.210（多数の修正）が入った回です。新規ページはなく、reference 系ページ（errors・agent-view・tools-reference・plugins-reference・permission-modes）に v2.1.208 の挙動を記述する追従改訂が集中しました。ファイル編集の可否、権限、Remote Control のデータ保存という中核の挙動が変わっている点に注意が必要です。

主要なものを以下に挙げます。

1. Edit ツールの read-before-edit 制約が緩和され、新しいモデルは未読ファイルや読み取り後にディスク上で変わったファイルも、条件を満たせば編集できるようになった
2. `Read` の deny ルールが同じパスへの Edit ツールもブロックするようになった（新規ファイル作成も含む）。Write / NotebookEdit は対象外
3. Remote Control の接続中はセッションのトランスクリプトが Anthropic サーバーに保存されるようになり、ZDR 有効組織では Remote Control が使えなくなった
4. Amazon Bedrock のストリーミング応答に content-type ガードが入り、ゲートウェイが応答を書き換えると即座にエラーで落ちるようになった（新しい環境変数と新エラーを追加）
5. バックグラウンドセッションの worktree 削除が、どこにも push されていないコミットを持つ worktree を破棄しなくなった
```

## ハイライト

1. [**Edit ツールの read-before-edit 制約が緩和**](./latest-detail.md#1-edit-ツールの-read-before-edit-制約が緩和):  
  v2.1.208 で、Edit ツールの「編集前に必ず会話内で読む」要件が新しいモデルで緩められた。読み取りに権限プロンプトが不要で Read ツールが使える場合は、未読のファイルも編集できる。読み取り後にディスク上で変わったファイルも、`old_string` が現在の内容に一意に一致し権限プロンプトなしに読める限り編集できる。Claude Opus 4.6・Haiku 4.5・それ以前のモデルは従来どおり事前読み取りが必要。
2. [**Read deny ルールが Edit ツールもブロック**](./latest-detail.md#2-read-deny-ルールが-edit-ツールもブロック):  
  v2.1.208 で、`Read` の deny ルールが一致するパスへの Edit ツールも拒否するようになった（そのパスに新規ファイルを作る場合も含む）。編集は結果を読み戻せる必要があるためで、ファイルアクセスの前に拒否される。ブロックされるのは Edit だけで、Write と NotebookEdit は `Read` deny の対象外。触らせたくないパスには `Edit` deny ルールも足す必要がある。
3. [**Remote Control のトランスクリプトが Anthropic サーバーに保存**](./latest-detail.md#3-remote-control-のトランスクリプトが-anthropic-サーバーに保存):  
  Remote Control の接続中は、メッセージ・Claude の応答・ツール活動を含むセッションのトランスクリプトが Anthropic サーバーに保存されるようになった。デバイス間で会話を同期し、ネットワーク切断後に再接続するため。コード実行とファイルアクセスは従来どおりローカルに留まる。無効化は `disableRemoteControl` 設定。ZDR など compliance 要件のある組織は Remote Control を有効化できなくなった。
4. [**Amazon Bedrock ストリーミングの content-type ガード**](./latest-detail.md#4-amazon-bedrock-ストリーミングの-content-type-ガード):  
  v2.1.208 で、Amazon Bedrock のストリーミング応答が `application/vnd.amazon.eventstream` 以外の content-type を報告した場合、Claude Code が復号できない本文をデコードせずエラーで拒否するようになった。ゲートウェイやプロキシが応答を書き換えているサインで、従来は全体をバッファリングした後に `Truncated event message received` で落ちていた。ヘッダーだけ書き換わり本文が無傷なら `CLAUDE_CODE_DISABLE_BEDROCK_CONTENT_TYPE_GUARD=1` でチェックを外せる。
5. [**バックグラウンドセッションの worktree がコミットを破棄しなくなった**](./latest-detail.md#5-バックグラウンドセッションの-worktree-がコミットを破棄しなくなった):  
  v2.1.208 で、バックグラウンドセッションの削除が、どこにも push されていないコミットを持つ worktree や、別の実行中セッションが使用・ロックしている worktree を削除しなくなった。worktree はセッション行ごと保持され、フッタが保持したパスと理由を示す。`Ctrl+X` の二度押し削除は未コミットの変更を持つ worktree を（コミット前提で）削除し、`claude rm` は未コミットの変更を持つ worktree をセッション行ごと残す。

## 新規追加されたページ

今回の対象期間では、新規に追加されたリファレンス・ガイドページはありません。

## 大幅に更新されたページ

- [**エラーリファレンス**](./latest-detail.md#1-エラーリファレンス) ([English](https://code.claude.com/docs/en/errors)):  
  複数のエラーセクションが新設された。`apiKeyHelper` スクリプトの失敗、サブエージェントがツールゼロで起動されるケース、`Read` deny ルールによる編集拒否（ハイライト 2 参照）、バックグラウンドセッションで拒否されるコマンドと `CLAUDE_CODE_PROCESS_WRAPPER` ランチャーのエラー、Amazon Bedrock ストリーミングの content-type エラー（ハイライト 4 参照）。
- [**エージェントビュー**](./latest-detail.md#2-エージェントビュー) ([English](https://code.claude.com/docs/en/agent-view)):  
  待機中のバックグラウンドエージェント数を数える `←` フッタヒント、配信できなかった返信を次回プロンプトとして保存する挙動、バックグラウンドセッションでの `/install-github-app` と `/mcp` 設定一覧の拒否、supervisor のバージョン取り扱い、worktree 削除の安全化（ハイライト 5 参照）、バージョン履歴表への v2.1.208 行が加わった。
- [**ツールリファレンス**](./latest-detail.md#3-ツールリファレンス) ([English](https://code.claude.com/docs/en/tools-reference)):  
  Edit ツールの read-before-edit 緩和と Read deny による編集拒否（ハイライト 1・2 参照）に加え、Read の空ファイル通知と巨大 1 行の早期エラー、Grep が不正入力を `No files found` ではなくエラーで返す変更と件数モードの総数、Glob のヌルバイトエラーが加わった。
- [**プラグインリファレンス**](./latest-detail.md#4-プラグインリファレンス) ([English](https://code.claude.com/docs/en/plugins-reference)):  
  `${user_config.*}` がシェル経由のフィールドで拒否される仕様が表に再構成され（各フィールドの代替手段つき）、`${CLAUDE_PLUGIN_ROOT}` などパスプレースホルダの置換対象がコンポーネント別・サーバー型別の表に整理された。
- [**権限モード**](./latest-detail.md#5-権限モード) ([English](https://code.claude.com/docs/en/permission-modes)):  
  `bypassPermissions` モードの節が全面的に書き直され、ファイルシステムのルート・ホームディレクトリ削除のサーキットブレーカが `$(...)`・バックティック・`<(...)` を含むコマンドでも発火するようになった点が auto モードとあわせて明記された。

## 軽微な更新

今回の軽微な更新は、changelog に追加されたリリース **v2.1.209**・**v2.1.210** の内容と、v2.1.208 に追従した各ページの小規模な改訂です。複数リリースを含むため、changelog 由来の項目には必要に応じてバージョンを併記します。

**新機能**

- 組織共有のクラウド環境が追加された。Team / Enterprise の Owner / Admin が、admin settings の Cloud environments ページで、ネットワークアクセスレベル・環境変数・setup script を持つ環境を組織全員に共有でき、組織の既定環境も選べる。 — [English](https://code.claude.com/docs/en/claude-code-on-the-web#organization-shared-environments)
- 環境変数 `CLAUDE_CODE_PROCESS_WRAPPER` が追加された（v2.1.208）。Claude Code が自分のバイナリから起動するプロセス（agent view を支えるバックグラウンドサービス、それが spawn する各セッション、更新完了のための自己再起動）を、`exec "$@"` で終わるラッパー実行ファイル経由にする。値は argv プレフィックスで、user / managed 設定の `env` ブロックに置く（Windows では無視）。 — [English](https://code.claude.com/docs/en/env-vars)
- 設定 `vimInsertModeRemaps` が追加された（v2.1.208）。vim モードで `jj` のような 2 キーの INSERT モード列を Escape に割り当てる。ターゲットは `"<Esc>"` のみ。user・`--settings`・managed 設定からのみ読むため、リポジトリのチェックイン設定でキー操作を書き換えられない。 — [English](https://code.claude.com/docs/en/interactive-mode#remap-insert-mode-key-sequences)
- `claude auto-mode defaults` に `--label <prefix>` が追加された（v2.1.208）。ラベルの前置一致（大小無視）で特定のルールだけを表示し、`jq` を通さずに 1 ルールの全文を読める。
- SDK メッセージ型 `SDKThinkingTokensMessage` が型定義に追加された（v2.1.153）。thinking ブロック（redacted を含む）の生成中に、生成済み thinking トークンの推定累計と増分を流す。課金上の正値は result メッセージの `usage.output_tokens`。 — [English](https://code.claude.com/docs/en/agent-sdk/typescript#sdkthinkingtokensmessage)
- TypeScript SDK のフック表に `UserPromptExpansion` が追加された。ユーザーが打ったコマンドがプロンプトへ展開され Claude に届く前に発火し、コマンドの直接呼び出しをブロックしたりスキル入力時に文脈を足したりできる。
- worktree 名の再利用が明文化された（v2.1.208）。既存ディレクトリの worktree 名を再利用するとその worktree を再開し、未コミット変更も未追跡ファイルも無く・Claude が作ったブランチのまま・未コミットまたは PR がマージされ remote ブランチが消えている、をすべて満たす場合は現在の base にリセットされる。 — [English](https://code.claude.com/docs/en/worktrees#reuse-a-worktree-name)
- Pro / Max の支出上限ダイアログが、すべての購入とオートリロード変更で金額に関わらず `yes` の打ち込み確認を求めるようになった（v2.1.208）。金額欄は候補値がプリフィルされ最初の 1 桁で置き換わり、使用クレジット有効化画面は Cancel 選択で開く。 — [English](https://code.claude.com/docs/en/costs#set-a-spend-limit-on-pro-and-max)
- 設定 `fastMode` が settings 表に載った。`/fast` でオンにすると user 設定に `true` が書かれ、オフで削除される。

**機能改善**

- `/usage` が、プラン上限の取得に失敗（多くはレート制限）した場合、直近 60 分にこのマシンで読み込んだ last-known のバーを `Showing last-known usage` の注記つきで表示するようになった（v2.1.208）。`r` で再試行できる。 — [English](https://code.claude.com/docs/en/costs#using-the-usage-command)
- マーケットプレイスの自動更新が、起動後に最大 10 分のランダム遅延を挟んでチェックするようになった。実行中のセッションは起動時に読み込んだバージョンを使い続け、更新分は次回起動で読み込まれる。 — [English](https://code.claude.com/docs/en/plugin-marketplaces#configure-auto-updates)
- worktree の base branch が、24 時間以内に fetch が無いと `origin/HEAD` を 5 秒上限で fetch して更新し、失敗時はローカルキャッシュを使うようになった（v2.1.208）。 — [English](https://code.claude.com/docs/en/worktrees#choose-the-base-branch)
- ワークフローの resume で、停止時に実行中だったエージェントは保存されず最初からやり直しになるため、多数の小さなエージェントに分ける方が進捗を保てることが明記された。あわせて `CLAUDE_CODE_SUBAGENT_MODEL` がワークフローの各エージェントのモデルも上書きし、エイリアス指定も受け付けることが加わった。 — [English](https://code.claude.com/docs/en/workflows#resume-after-a-pause)
- 空の `url` を持つリモート MCP サーバーが `/mcp`・`claude mcp list`・`/plugin` で `not configured` と表示され、接続を試みなくなった（プラグインが後で設定するコネクタのプレースホルダを置ける）（v2.1.208）。 — [English](https://code.claude.com/docs/en/mcp#installing-mcp-servers)
- `Ctrl+O` のトランスクリプトビューアが、各アシスタントメッセージにタイムスタンプと使用モデルを表示するようになった。 — [English](https://code.claude.com/docs/en/interactive-mode#keyboard-shortcuts)
- コマンドが、Claude の応答中に送るとキューされ現在のターン後に実行されるようになった。`/status`・`/tasks`・`/usage` は応答を中断せず即時実行される。 — [English](https://code.claude.com/docs/en/commands#slash-commands)
- `/tasks` に、完了したバックグラウンドサブエージェントも（done 表示で実行中作業の下に並べて）表示されるようになった。詳細ビューも終了時に開いたまま残る。失敗・停止したサブエージェントは一覧から消える（v2.1.208）。サブエージェント・「Run agents in parallel」・バックグラウンドタスクの各ページに追記された。 — [English](https://code.claude.com/docs/en/sub-agents#run-subagents-in-foreground-or-background)
- 環境変数の優先順位が明記された。同じ変数が shell と設定ファイルの `env` ブロック両方にある場合は設定ファイルの値が適用され、設定ファイル間では settings precedence に従う（managed が user / project を上書き）。 — [English](https://code.claude.com/docs/en/env-vars)
- チェックポイントのファイルスナップショットが直近 100 チェックポイント分に絞られ、残らないチェックポイントが参照するスナップショットは削除されるようになった（各ファイルの最初のスナップショットは VS Code 拡張の差分基準として残す）（v2.1.208）。 — [English](https://code.claude.com/docs/en/checkpointing#how-checkpoints-work)
- スクリーンリーダーモードが、自己再起動時に `CLAUDE_AX_SCREEN_READER` 環境変数経由で引き継がれ、`Shift+Tab` でモードを巡回すると権限モードの変更を読み上げるようになった（v2.1.210）。 — [English](https://code.claude.com/docs/en/accessibility#turn-on-screen-reader-mode)
- auto モードで許可分類器が、外部セッションでは既定 Sonnet 5 になり、セッションの最初のリクエストで検証してセッションに固定するようになった（v2.1.210）。

**バグ修正**

- `claude agents` のバックグラウンドセッションで `/model` などのダイアログがブロックされる問題を修正（過度に広いガードのリバート、v2.1.209）。
- `isolation: 'worktree'` のサブエージェントが、自分の隔離 worktree ではなくメインリポジトリのチェックアウトに対して git 変更コマンドを実行できた問題を修正（v2.1.210）。
- `ultracode` キーワードのオプトインが、webhook ペイロードや中継された PR コメントなど人間由来でない入力で発火する問題を修正（v2.1.210）。
- hook コールバックのタイムアウトがユーザー拒否としてモデルに誤報告され、無人セッションが停止して待ち続ける問題を修正（v2.1.210）。あわせて、Agent SDK の `UserPromptSubmit` / `UserPromptExpansion` コールバックがタイムアウトすると、ターンをエラー終了させずにそのプロンプトをブロックしてセッションを継続するよう、hooks ページの記述も更新された。
- `cd` がバックグラウンド移行後に効いたと Claude が誤認する問題を修正（作業ディレクトリが変わっていない旨をツール結果に明記、v2.1.210）。
- Grep の content モードが結果末尾を越えてページングすると `No matches found` と誤報告する問題を修正（v2.1.210）。
- skills / commands で未対応の `$1`・`$2` 位置プレースホルダが黙って除去される問題を修正（そのまま保持、v2.1.210）。
- kill されたバックグラウンドセッションが `git worktree lock` を残す問題を修正（所有プロセスが消えたロックを定期スイープが解放、v2.1.210）。
- MEMORY.md インデックスが読み取り上限を超える書き込みで黙って切り詰められる問題を修正（明示エラーを出す、v2.1.210）。
- Agent ツールが、サブエージェントが読んだ内容経由の間接プロンプトインジェクションに対して強化された（v2.1.210）。
- Amazon Bedrock で、`sso_region` が Bedrock のリージョンと異なる AWS SSO プロファイルの認証が `Session token not found or invalid` で失敗する問題（v2.1.207 のリグレッション）について、Amazon Bedrock ページに切り分けの追記が入った。Claude Code は `sso_region` が示す IAM Identity Center リージョンからロール認証情報を要求する。 — [English](https://code.claude.com/docs/en/amazon-bedrock#2-configure-aws-credentials)
- `claude -p` で大きな応答をパイプするとストリーム出力の最終行（`result` メッセージ）が切り詰められ欠落する問題の修正が、headless ページに明記された（v2.1.208 より前の挙動として）。 — [English](https://code.claude.com/docs/en/headless#stream-responses)
- このほか v2.1.210 では、`claude attach` のセッション遷移中の失敗、プラグイン提供 MCP サーバーの再同期時の破棄、edits 無しの plan 承認が「(edited by user)」と誤ラベルされる問題、`/doctor` が Bedrock / Vertex / Foundry で auto モード提案をスキップする問題、Windows / ネットワークファイルシステムでのプラグインキャッシュのリネーム失敗、background worker のクラッシュループ、SDK MCP サーバーの接続遅延など、多数の修正が入っている。

**その他**

- Remote Control が、ZDR 有効組織で自動無効化される機能一覧に追加された（ハイライト 3 参照）。 — [English](https://code.claude.com/docs/en/data-usage#data-access)
- Desktop の Cowork の説明が、「サンドボックス化された仮想マシン」で動くと更新され、on-device の Cowork は自分の PC で VM を動かし、remote の Cowork は Anthropic 管理の VM で動く区別が加わった。 — [English](https://code.claude.com/docs/en/desktop#cowork)
- Windows インストールのトラブルシューティングが書き換えられた。証明書失効チェックがブロックされる場合、`--ssl-revoke-best-effort` はスクリプト自身のダウンロードには効かず直らないため、.NET 経由の PowerShell インストーラ（または `winget`）に切り替える案内になった。 — [English](https://code.claude.com/docs/en/troubleshooting#failed-to-fetch-version-from-downloadsclaudeai)
- 「大きなテーブルがターミナルで切り詰められる」Troubleshooting 項目が新設された。200 行を超える Markdown 表は先頭 200 行と「… N more rows not shown」を表示し、`/copy` は全行をコピーする（v2.1.208）。 — [English](https://code.claude.com/docs/en/troubleshooting#performance-and-stability)
- 多数のページにブログ記事へのリンクが追加された（best-practices・model-config・quickstart・agent-sdk overview・agents など。dynamic workflows / loop engineering / model と effort の選び方などの解説）。
- インストール手順のコードフェンスに重複していた `theme={null}` 属性が整理された（表示上の変化なし）。

## 新着情報

今回の対象期間では、週刊ダイジェスト「新着情報」（`whats-new/`）の**変更はありません**（新規追加・更新ともになし）。

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-07-13.md](./archives/latest/2026-07-13.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-07-13.md](./archives/latest-detail/2026-07-13.md)

<!--
base_commit: 68a6388fc3bd9e4928fb9b97e59c4de1d6120599
head_commit: 991b037c23024d28c04a58fcaebe2c1862fc912d
generated_at_full: 2026-07-15T15:01:13+09:00
-->
