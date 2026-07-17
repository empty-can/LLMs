---
対象期間: 2026年07月15日 〜 2026年07月16日
作成日: 2026-07-16
---

# Claude Code 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
今回の対象期間は、原文の全文（llms-full.txt）に本文変更がなく、索引（llms.txt）とナビゲーション用の構造マップ（docs_map）だけが追いついた「追従回」です。唯一の実質的な新規事項として、既報の環境変数 CLAUDE_CODE_PROCESS_WRAPPER を独立ページへ統合した「企業ランチャーの背後で Claude Code を実行する」が新設されました。

主要なものを以下に挙げます。

1. 企業の必須ランチャー経由で Claude Code の自己起動プロセスをラップする CLAUDE_CODE_PROCESS_WRAPPER（環境変数自体は v2.1.208 で既報）の使い方をまとめた専用ページ「企業ランチャーの背後で Claude Code を実行する」が新設された
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**コーポレートランチャー専用ページの新設**](#1-コーポレートランチャー専用ページの新設):  
  企業の必須ランチャー経由で Claude Code の自己起動プロセスをラップする `CLAUDE_CODE_PROCESS_WRAPPER`（v2.1.208 で追加済み）の使い方が、独立した専用ページに統合された。argv プレフィックスの形式、`env` ブロックでの設定、ランチャーコントラクト、`CLAUDE_CODE_SHELL_PREFIX` との違いをまとめる。
<!-- light:highlight-list:end -->

## 1. コーポレートランチャー専用ページの新設

「企業ランチャーの背後で Claude Code を実行する」という専用ページが新設され、ドキュメント索引（`llms.txt`）に追加されました。一部の組織は、ワークステーション上の全プロセスを必須ランチャー経由で起動させ、サンドボックス・ネットワーク制御・認証情報注入といったセキュリティ機構を適用します。このページは、Claude Code が自身のバイナリから起動するプロセスをそのランチャー経由に通すための環境変数 `CLAUDE_CODE_PROCESS_WRAPPER`（v2.1.208 で追加。従来は環境変数・エラーの各リファレンスに散在して記載されていた）を、独立したガイドに統合したものです。

`CLAUDE_CODE_PROCESS_WRAPPER` はラッパー実行ファイルへの argv プレフィックス（例 `/opt/corp/launcher`）として指定し、agent view をホストするバックグラウンドサービス、それが spawn する各セッション、更新完了のための Claude Code の自己再起動を対象に含めます。値の先頭トークンは `exec "$@"` で終わる実行ファイルの絶対パスでなければならず、値はシェルコマンドではなく引数リストとして解釈されます（空白でトークン分割、二重引用符でスペースを含むパスをグループ化、`[` 始まりは JSON 文字列配列）。デタッチされたバックグラウンドサービスが継承できるよう、シェルの export ではなくユーザー設定または managed 設定の `env` ブロックに置く必要があり（プロジェクト／ローカル設定では指定不可）、Windows では無視されます。VS Code 拡張は独自の `claudeProcessWrapper` 設定で別に構成します。値が使えない場合、Claude Code は該当プロセスをラップなしで起動する代わりに起動を拒否し、変数名で始まる理由付きメッセージを表示します（修正後は `claude daemon stop --any` で再起動）。シェルコマンドをラップする `CLAUDE_CODE_SHELL_PREFIX` とは別系統の制御です。ランチャーは環境変数のほか設定項目としても構成でき（`network-config` に「Configure a corporate launcher as a setting」の導線が追加されている）、索引の説明でも `CLAUDE_CODE_PROCESS_WRAPPER` と `processWrapper` 設定の双方が経路として示されています。ページは「ランチャーがカバーするもの」「ランチャーのセットアップ」「ランチャーコントラクト」「`CLAUDE_CODE_SHELL_PREFIX` との関係」などの節で構成されています。

- [企業ランチャーの背後で Claude Code を実行する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/corporate-launcher)
- [日本語](https://code.claude.com/docs/ja/corporate-launcher) / [Run Claude Code behind a corporate launcher - Claude Code Docs (English)](https://code.claude.com/docs/en/corporate-launcher)

## 新規追加されたページ

<!-- light:new-pages:start -->
- [**企業ランチャーの背後で Claude Code を実行する**](#1-企業ランチャーの背後で-claude-code-を実行する) ([日本語](https://code.claude.com/docs/ja/corporate-launcher) / [English](https://code.claude.com/docs/en/corporate-launcher)):  
  企業の必須ランチャー経由で Claude Code の自己起動プロセスを通すための `CLAUDE_CODE_PROCESS_WRAPPER` を解説する専用ページ（詳細はハイライト1参照）。
<!-- light:new-pages:end -->

## 1. 企業ランチャーの背後で Claude Code を実行する

`CLAUDE_CODE_PROCESS_WRAPPER` による企業ランチャー統合を解説する専用ページが、ドキュメント索引に新規追加されました。内容の詳細はハイライト1を参照してください（環境変数自体は v2.1.208 で追加済みで、本ページはその使い方を独立したガイドにまとめ直したものです）。

- [企業ランチャーの背後で Claude Code を実行する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/corporate-launcher)
- [日本語](https://code.claude.com/docs/ja/corporate-launcher) / [Run Claude Code behind a corporate launcher - Claude Code Docs (English)](https://code.claude.com/docs/en/corporate-launcher)

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
今回の対象期間では、原文の全文（`llms-full.txt`）に本文変更がなかったため、大幅に更新されたページはありません。
<!-- light:updated-pages:end -->

## 軽微な更新

<!-- light:minor-updates:start -->
今回の対象期間は原文の全文（`llms-full.txt`）に本文変更がなく、索引（`llms.txt`）とナビゲーション用の構造マップ（`docs_map`）だけが更新されました。以下は索引・マップ側にのみ現れた構造上の変更で、対応する本文はまだ集約全文エクスポートに反映されていないため、各セクションの内容要約は本文が反映された回に譲ります（そのため下記は見出しの記録のみで、個別リンクは付けません）。

**その他**

- 索引 `llms.txt` に新規ページ `corporate-launcher`（企業ランチャー）が追加された（本文はハイライト1・新規追加参照）。
- ナビゲーションマップ `docs_map` が再生成され、以下のページに新しいセクション見出しが追加された（見出しのみ記録。対応本文は集約全文に未反映）:
  - `sessions`: 「What a resumed session restores」（resume が復元する範囲）
  - `sub-agents`: 「Subagent output scanning」（サブエージェント出力のスキャン）
  - `workflows`: 「Dismiss or turn off the keyword」「Where the keyword works」（ワークフロー起動キーワードの無効化と有効範囲）
  - `worktrees`: 「Clean up subagent and background-session worktrees」「Worktree removal on Windows」（サブエージェント／バックグラウンドセッションの worktree 掃除、Windows での worktree 削除）
  - `chrome`: 「Upload files to web pages」「Save screenshots to disk」（Web ページへのファイルアップロード、スクリーンショットのディスク保存）
  - `authentication`: 「Restrict login to your organization」（組織へのログイン制限）
  - `auto-mode-config`: 「Add a human checkpoint」（人手チェックポイントの追加）
  - `network-config`: 「Apply network settings to background agents」ほか（バックグラウンドエージェントへのネットワーク設定適用、企業ランチャーを設定として構成する導線）
  - `zero-data-retention`: 「Route Claude Code traffic to your ZDR organization」（ZDR 組織へのトラフィックルーティング）
  - `claude-platform-on-aws`「4. Launch and verify」／`google-vertex-ai`「6. Verify your configuration」（各セットアップ手順への検証ステップ追加）
  - `tools-reference`: Bash ツール挙動に「What persists between commands」「Timeout and output limits」「Background commands」の各節が追加
  - トラブルシュート項目の追加: `errors`「Memory index is over its read limit」「This session has no saved transcript」、`agent-view`「Opening a session says it has no saved transcript」、`claude-code-on-the-web`／`github-enterprise-server`「Unable to get organization UUID」系、`deep-links`「xdg-open is not found on Linux」
- 参考: `CLAUDE_CODE_PROCESS_WRAPPER` 環境変数そのものは 2026-07-13（軽微な更新の v2.1.208 新機能まとめ）および 2026-07-14（エラーリファレンスの大幅更新）のサマリで既報。今回はそれを独立ページ化した点が新規。
<!-- light:minor-updates:end -->

## 新着情報

<!-- light:whats-new:start -->
今回の対象期間では、週刊ダイジェスト「新着情報」（`whats-new/`）の変更はありません（新規追加・更新ともになし）。
<!-- light:whats-new:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-07-15.md](./archives/latest/2026-07-15.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-07-15.md](./archives/latest-detail/2026-07-15.md)

<!--
base_commit: fa4c4c546b211cf29cac5e7c4dcc5b3e95008594
head_commit: 5cf373da86d5703c50540e7e49df4d79e33d4c76
generated_at_full: 2026-07-17T15:06:39+09:00
-->
