---
対象期間: 2026年06月09日 〜 2026年06月10日
作成日: 2026-06-10
---

# Claude Code 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
> 今回の更新は、リリース v2.1.172 の changelog 追加（主にバグ修正と細かな改善）が中心で、新機能としてはサブエージェントのネスト生成が目を引きます。あわせてプラグインページのマーケットプレイス登録・投稿フローの記述が更新されました。新規追加・大幅更新ページはなく、軽微更新のみです。
>
> 主要なものを以下に挙げます。
>
> 1. サブエージェントが自身のサブエージェントを生成できるようになった（v2.1.172、最大 5 階層）
> 2. `claude-plugins-official` マーケットプレイスの自動登録タイミングが明確化され、コミュニティ投稿フォームの URL・利用要件も更新された
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**サブエージェントのネスト生成**](#1-サブエージェントのネスト生成):  
  v2.1.172 で、サブエージェントが自身のサブエージェントを生成できるようになった（最大 5 階層の深さまで）。これまで単層だった委譲構造を多段に拡張できる。changelog（リリースノート）で告知された変更で、専用ドキュメントページにはまだ反映されていない。
2. [**プラグインマーケットプレイスの登録と投稿フローの変更**](#2-プラグインマーケットプレイスの登録と投稿フローの変更):  
  公式マーケットプレイス `claude-plugins-official` の自動登録タイミングが「初回の対話的起動時」と明確化され、それより前に走る非対話スクリプトでは明示追加が必要になった。あわせてコミュニティ投稿フォームの URL と利用要件（Team/Enterprise 組織・ディレクトリ管理アクセス）が更新された。
<!-- light:highlight-list:end -->

## 1. サブエージェントのネスト生成

リリース v2.1.172 で、サブエージェントが自身のサブエージェントを生成できるようになりました（最大 5 階層の深さまで）。これにより、親エージェントから委譲されたサブエージェントが、さらに下位のサブエージェントへ作業を分割・委譲する多段の構成が可能になります。

本項目は changelog（リリースノート）で告知されたもので、現時点で専用のドキュメントページには反映されていないため、末尾の参考リンクは省略します。サブエージェント全般については「カスタムサブエージェントを作成する」ページ（`/docs/ja/sub-agents`）を参照してください。

## 2. プラグインマーケットプレイスの登録と投稿フローの変更

「プラグインを作成する」ページのマーケットプレイス節で、公式マーケットプレイス `claude-plugins-official` の登録挙動が明確化されました。従来は「すべての Claude Code インストールで自動的に利用可能」とされていましたが、新しい記述では「Claude Code を初めて対話的に起動したときに自動登録される」と改められました。その初回起動より前に走る非対話スクリプトでは自動登録されないため、`claude plugin marketplace add anthropics/claude-plugins-official` で明示的に追加する必要があります。

あわせて、コミュニティマーケットプレイスへのプラグイン投稿フローも更新されました。claude.ai の投稿フォーム URL が `claude.ai/admin-settings/directory/submissions/plugins/new` に変更され、このフォームの利用には Team または Enterprise 組織とディレクトリ管理アクセスが必要（組織の Owner はデフォルトで保有）であることが明記されました。Team/Enterprise 組織に属さない個人作成者は、代わりに Console フォーム（`platform.claude.com/plugins/submit`）を利用できます。

- [プラグインを作成する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/plugins)
- [Create plugins - Claude Code Docs (English)](https://code.claude.com/docs/en/plugins)

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
- changelog ページに新しいリリースエントリ **v2.1.172**（2026年06月10日）が追加されました。サブエージェントのネスト生成（ハイライト 1 参照）に加え、次の機能追加・改善・修正を含みます（主なもの）。
  - **新機能・改善**
    - Amazon Bedrock が `AWS_REGION` 未設定時に `~/.aws` 設定ファイルから AWS リージョンを読むようになった（AWS SDK の優先順位に準拠）。`/status` にリージョンの取得元が表示される。
    - `/plugin` でマーケットプレイスのプラグインを閲覧する際の検索バーを追加。
    - OTEL メトリクス `claude_code.lines_of_code.count` に `model` 属性を追加。
    - 長い会話でのパフォーマンス改善（冗長なメッセージ正規化の除去、ツール使用状態が不変なときの全履歴変換の回避）と、アイドル時 CPU 使用量の削減。
  - **主な修正**
    - 使用クレジットなしで 1M コンテキストを使うセッションが恒久的にスタックする問題を修正（標準コンテキスト上限内に自動コンパクトされるようになった）。
    - `availableModels` の制限がサブエージェントのモデル上書き・エージェント発行時のモデルピッカー・アドバイザーモデルに適用されない問題を修正。
    - `availableModels` の許可リストが `claude-opus-4-8` のようなバージョン指定 ID を使うと、`/model` ピッカーの Opus・Sonnet の 1M 行を隠してしまう問題を修正。
    - Bedrock の `/model` ピッカーがプロバイダー非提供のモデルを提示していた問題を修正（選択するとセッションモデルが無言で切り替わっていた）。
    - `ANTHROPIC_DEFAULT_OPUS_MODEL` が既に 1M サフィックスを含む場合にモデル ID が二重（例 `[1M][1m]`）になる問題を修正。
    - `opusplan` 設定がプランモードで 1M コンテキストを伴って動作しない問題を修正（`opusplan[1m]` の回避策もプランモードで正しく Opus に切り替わるようになった）。
    - `WebFetch(domain:*.example.com)` のワイルドカードドメインルールがサブドメインに一致しない問題、および `Read(secrets-*/config.json)` のようなパターン途中のワイルドカードを含むファイル権限ルールが起動時に拒否される問題を修正。
    - チームメモリストア（`CLAUDE_MEMORY_STORES`）がリモートセッションのメモリ呼び出しで見つからない問題を修正。
    - \[VSCode] PowerShell のツール呼び出しが整形済みのコマンド表示・権限ダイアログではなく生の JSON として描画される問題を修正（表示されるシェル出力から ANSI エスケープも除去）。
    - ほか、バックグラウンドエージェント／エージェントビュー関連の複数の修正を含む。
- [日本語](https://code.claude.com/docs/ja/model-config) / [English](https://code.claude.com/docs/en/model-config):  
  「Work with Fable 5」セクション内の Fable 5 紹介ページへの外部リンク先が、`introducing-claude-fable-5` から `introducing-claude-fable-5-and-claude-mythos-5` に更新されました（リンク先 URL の変更のみで、本文の内容変更はありません）。
- [日本語](https://code.claude.com/docs/ja/plugins) / [English](https://code.claude.com/docs/en/plugins):  
  公式マーケットプレイスの自動登録タイミングと、コミュニティ投稿フォームの URL・利用要件が更新されました（詳細はハイライト 2 参照）。
<!-- light:minor-updates:end -->

## 新着情報

<!-- light:whats-new:start -->
*(今回の対象期間に新着情報（週間ダイジェスト）の更新はありません)*
<!-- light:whats-new:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-06-09.md](./archives/latest/2026-06-09.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-06-09.md](./archives/latest-detail/2026-06-09.md)

<!--
base_commit: e2d1b0571046ac6ca57dd9cd86ee5fb9a0e575b4
head_commit: 3c7fbb9579354ba1c5661f28ffd067f47e7775f7
generated_at_full: 2026-06-11T15:02:59+09:00
-->
