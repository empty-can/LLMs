---
対象期間: 2026年06月16日 〜 2026年06月17日
作成日: 2026-06-17
---

# Claude Code 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
今回は新規ページ・新着情報の追加はなく、changelog への v2.1.181（2026年06月17日）リリース追加（新機能・改善・多数のバグ修正）と、既存リファレンスページの小規模な精緻化が中心です。主要な新機能 3 件をハイライトとして整理します。

主要なものを以下に挙げます。

1. `/config key=value` 構文が追加され、任意の設定をプロンプトから直接変更できるようになった（対話・`-p`・Remote Control で動作。例: `/config thinking=false`）（v2.1.181）
2. 新環境変数 `CLAUDE_CLIENT_PRESENCE_FILE` が追加され、指定したマーカーファイルでマシン在席中はモバイルプッシュ通知を抑止できるようになった（v2.1.181）
3. macOS 向けに `sandbox.allowAppleEvents` オプトイン設定が追加され、sandbox 化されたコマンドが Apple Events を送信できるようになった（v2.1.181）
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**プロンプトから任意の設定を変更する新構文**](#1-プロンプトから任意の設定を変更する新構文):  
  `/config key=value` 構文が追加され、任意の設定をプロンプトから直接変更できるようになった（v2.1.181）。例として `/config thinking=false` のように入力でき、対話モード・`-p`（ヘッドレス）・Remote Control のいずれでも動作する。
2. [**在席中のモバイルプッシュ通知を抑止する環境変数**](#2-在席中のモバイルプッシュ通知を抑止する環境変数):  
  新しい環境変数 `CLAUDE_CLIENT_PRESENCE_FILE`（v2.1.181）が追加された。マーカーファイルのパスを指すよう設定すると、ユーザーがそのマシンの前にいる間はモバイルプッシュ通知が抑止される。
3. [**sandbox コマンドからの Apple Events 送信を許可する設定**](#3-sandbox-コマンドからの-apple-events-送信を許可する設定):  
  macOS 向けに `sandbox.allowAppleEvents` というオプトイン設定が追加された（v2.1.181）。有効にすると、sandbox 化されたコマンドが macOS 上で Apple Events を送信できるようになる。
<!-- light:highlight-list:end -->

## 1. プロンプトから任意の設定を変更する新構文

v2.1.181 で `/config key=value` 構文が追加され、任意の設定をプロンプトから直接変更できるようになりました。例えば `/config thinking=false` のように入力でき、対話モード・`-p`（ヘッドレス）・Remote Control のいずれの実行形態でも動作します。これまで設定の切り替えにはメニュー操作や `settings.json` の編集が必要だった場面でも、プロンプト 1 行で目的の設定キーに値を割り当てられます。

> 本項目は changelog（v2.1.181）でのみ告知されており、対応する通常リファレンスページにはまだ記載がないためページリンクは省略します。

## 2. 在席中のモバイルプッシュ通知を抑止する環境変数

新しい環境変数 `CLAUDE_CLIENT_PRESENCE_FILE`（v2.1.181）が追加されました。この変数にマーカーファイルのパスを指すよう設定しておくと、ユーザーがそのマシンの前にいる間はモバイルへのプッシュ通知が抑止されます。デスクトップで作業中の通知と、離席中に受け取りたいモバイル通知を切り分けるための仕組みです。

> 本項目は changelog（v2.1.181）でのみ告知されており、対応する通常リファレンスページにはまだ記載がないためページリンクは省略します。

## 3. sandbox コマンドからの Apple Events 送信を許可する設定

macOS 向けに `sandbox.allowAppleEvents` というオプトイン設定が追加されました（v2.1.181）。有効にすると、sandbox 化されたコマンドが macOS 上で Apple Events を送信できるようになります。あわせて、`open`・`osascript`・ブラウザベースの認証フローが macOS でエラー -600 で失敗する問題が、Apple Events エンタイトルメントの追加で修正されています（「軽微な更新」のバグ修正参照）。

> 本項目は changelog（v2.1.181）でのみ告知されており、対応する通常リファレンスページにはまだ記載がないためページリンクは省略します。

## 新規追加されたページ

<!-- light:new-pages:start -->
*(今回の対象期間に新規追加されたページはありません)*
<!-- light:new-pages:end -->

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
*(今回の対象期間に大幅に更新されたページはありません)*
<!-- light:updated-pages:end -->

## 軽微な更新

<!-- light:minor-updates:start -->
今回の対象期間は新規ページ・新着情報の追加はなく、changelog への v2.1.181（2026年06月17日）追加と既存リファレンスページの小規模な精緻化が中心です。新機能はハイライトに挙げたとおりです。それ以外の更新を分類別に示します（特記なき項目は v2.1.181）。

**機能改善**
- 長い段落のストリーミング表示が改善され、最初の改行を待たずに行単位でテキストが現れるようになった。
- thinking 中の API 接続切断が、「Connection closed while thinking」表示の代わりに自動でリトライされるようになった。
- サブエージェントパネルが改善され、アイドルのサブエージェントは 30 秒後に自動で隠れ、一覧はスクロールヒント付きで最大 5 行に制限され、キーボードヒントがフッターに表示されるようになった。
- MCP の OAuth ブラウザページが Claude Code の見た目に揃えられ、成功時に自動で閉じるようになった。
- フルスクリーンモードでの URL オープンが Cmd+クリック（macOS）/ Ctrl+クリックを要するよう変更され、ネイティブターミナルの挙動に揃えられた。
- メモリ改善時の「Improved N memories」行が、verbose モード以外では個々のファイルを列挙しなくなった。
- 同梱の Bun ランタイムが 1.4 に更新された。
- スキルのコマンド名解決の表に、別のスキルと名前が衝突するネストした `.claude/skills/` の行が追加され、作業ディレクトリからの相対サブディレクトリパスで修飾した名前（例: `apps/web:deploy`）になることが明記された。 — [日本語](https://code.claude.com/docs/ja/skills#how-a-skill-gets-its-command-name) / [English](https://code.claude.com/docs/en/skills#how-a-skill-gets-its-command-name)
- サブエージェント定義の `tools` / `disallowedTools` が MCP サーバーレベルのパターンを受け付ける説明に、`disallowedTools: mcp__github` で他サーバーと組み込みツールを保ったまま github MCP サーバーの全ツールだけを除去する YAML 例が追加された。 — [日本語](https://code.claude.com/docs/ja/sub-agents#available-tools) / [English](https://code.claude.com/docs/en/sub-agents#available-tools)
- スキルの説明が文字予算で短縮される件のトラブルシューティングで、`/doctor` が「いくつのスキル説明が短縮/削除されているか」と影響を受けるスキルを示す、と説明が更新された（旧: 予算が溢れているかと影響スキルを確認）。 — [日本語](https://code.claude.com/docs/ja/skills#skill-descriptions-are-cut-short) / [English](https://code.claude.com/docs/en/skills#skill-descriptions-are-cut-short)

**バグ修正**

changelog に v2.1.181（2026年06月17日）が追加され、既存の v2.1.178 エントリにも 1 行が追記された。リリース単位で示す。

- **v2.1.181**（2026年06月17日）
  - カスタム `ANTHROPIC_BASE_URL` および Foundry で、リクエストごとのアテステーショントークンが毎ターン変わるためにプロンプトキャッシュが読み取れなかった問題を修正。
  - ネットワークドライブやクラウド同期フォルダで Write/Edit が 0 バイトまたは切り詰められたファイルを生成する問題を修正。
  - macOS で `open`・`osascript`・ブラウザベースの認証フローがエラー -600 で失敗する問題を、Apple Events エンタイトルメントの追加で修正。
  - 新規環境で起動ごとに約 120ms 遅くなる退行（2.1.169 で混入）を修正し、MCP サーバー未設定時は最初のプロンプトが managed-settings の取得を待たなくなった。
  - 劣化したネットワークでアカウント設定の取得が遅いとき、空のターミナルで最大 15 秒起動がブロックされる問題を修正。
  - `.claude.json` に破損した null のプロジェクトエントリがあると起動時にクラッシュ（`TypeError: Cannot read properties of null`）する問題を修正。
  - Spotlight が再インデックス中のとき、macOS の TUI がセッション開始時にフリーズ（Ctrl+C 無反応）する問題を修正。
  - 別の Claude Code プロセスが 30 日トランスクリプトのクリーンアップを実行すると、長時間アイドルのセッションが履歴を失う問題を修正。
  - フォアグラウンドのサブエージェントが際限なくネストした連鎖を生成する問題を修正し、バックグラウンドと同じ 5 階層の深さ制限に従うようにした。
  - モデル切替直後に `/recap` と会話フォークが切替前のモデルを使う問題を修正。
  - サブエージェントの「Thinking」表示時間が、サブエージェント自身ではなく親エージェントの経過時間を表示する問題を修正。
  - ネストしたエージェントで待機中のサブエージェントが、エージェントパネルで「waiting」ではなく経過時間が進み続ける表示になる問題を修正。
  - リトライ成功後も API リトライ表示（「Retrying in 0s · attempt N/10」）が画面に残る問題を修正。
  - AWS `awsCredentialExport` の残存寿命が短い認証情報が毎分リフレッシュを起こす問題を修正し、`aws configure export-credentials` の JSON 形式も受け付けるようにした。
  - `claude mcp get`/`list` が tools/list 失敗時に `✓ Connected` と表示する問題を修正し、エラー詳細付きで `! Connected · tools fetch failed` と表示するようにした。
  - `/remote-control` が古い「connecting…」行を残す問題を修正し、接続後にトランスクリプトで確認を示すようにした。
  - Windows で素の `git` を解決できないとき、ExitWorktree がクリーンな worktree の削除を「Could not verify worktree state」で拒否する問題を修正。
  - `~/.claude/settings.json` がシンボリックリンクされた `~/.claude` 配下の相対シンボリックリンクのとき、`/effort` や `/model` などの設定変更が ENOENT で失敗する問題を修正。
  - IDE の選択行番号がコンテキストリマインダーで 1 つずれる問題（IntelliJ・VS Code）を修正。
  - フルスクリーンでネイティブターミナル選択（修飾キー+ドラッグ）後の Ctrl+C が、アプリの直前の選択でクリップボードを上書きする問題を修正。
  - クリップボードにテキストがあるとき Ctrl+V が貼り付けずに「No image found in clipboard」と表示する問題を修正。
  - エージェントディレクトリが既に存在するときにエージェント作成が「EEXIST: file already exists」で失敗する問題（Windows/OneDrive）を修正。
  - AskUserQuestion のプレビュー内容がダイアログ端で折り返されず切れる問題を修正。
  - AskUserQuestion の複数選択質問で、入力した「Other」の自由記述回答が送信時に黙って捨てられる問題を修正。
  - `/stats` の「Most active day」と日次トークングラフの日付が、UTC マイナス圏のタイムゾーンで 1 日早く表示される問題を修正。
  - Linux で `/copy` と選択時コピーが、Claude Code 起動後にインストールされたクリップボードユーティリティを検出しない問題を修正。
  - Write（ファイル作成）プレビューでタブインデントのコードが誤ったインデントで描画される問題を修正。
  - ターン中にキューされたユーザープロンプトが、トランスクリプトで全幅の背景ハイライトを表示しない問題を修正。
  - Ghostty でアクティビティスピナーのパルスが誤ったグリフサイズに留まる問題を修正。
- **v2.1.178**（既存エントリへの追記）
  - `.claude/skills` または `.claude/hooks` がシンボリックリンクのとき Linux sandbox が起動に失敗する問題を修正。
<!-- light:minor-updates:end -->

## 新着情報

<!-- light:whats-new:start -->
*(今回の対象期間に新着情報（whats-new）ページの更新はありません)*
<!-- light:whats-new:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-06-16.md](./archives/latest/2026-06-16.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-06-16.md](./archives/latest-detail/2026-06-16.md)

<!--
base_commit: 903188279ac643213af8353f48bbc9b9c6dff390
head_commit: 36ebe5ec3ed55ca4d8d65463453e514b6892594d
generated_at_full: 2026-06-18T15:03:07+09:00
-->
