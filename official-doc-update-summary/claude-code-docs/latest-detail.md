---
対象期間: 2026年06月06日 〜 2026年06月08日
作成日: 2026-06-08
---

# Claude Code 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
> 今回の更新は、changelog への v2.1.169（新機能・修正・改善を多数含む大型リリース）追加と、スキル・ゼロデータ保持（ZDR）関連の通常ページ更新が中心です。リファレンスの新規追加・大幅更新ページはありません。
>
> 主要なものを以下に挙げます。
>
> 1. トラブルシュート用に全カスタマイズを無効化して起動する `--safe-mode` フラグ（と `CLAUDE_CODE_SAFE_MODE`）を追加
> 2. プロンプトキャッシュを壊さずセッションの作業ディレクトリを変更する `/cd` コマンドを追加
> 3. バンドルスキル・ワークフロー・組み込みコマンドをモデルから隠す `disableBundledSkills` 設定（と `CLAUDE_CODE_DISABLE_BUNDLED_SKILLS`）を追加
> 4. スキル稼働中だけツールを利用可能プールから外す frontmatter `disallowed-tools` を追加
> 5. ZDR が標準 Enterprise プランに非同梱で、適格アカウント向け・Anthropic による個別有効化が必要である旨を明確化
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**safe-mode フラグによる全カスタマイズ無効化**](#1-safe-mode-フラグによる全カスタマイズ無効化):  
  CLAUDE.md・プラグイン・スキル・フック・MCP サーバーといった全カスタマイズを無効化した状態で起動する `--safe-mode` フラグ（と環境変数 `CLAUDE_CODE_SAFE_MODE`）が追加された。設定やプラグイン起因の不具合を切り分けるトラブルシュート用途に使える。
2. [**/cd コマンドによる作業ディレクトリの変更**](#2-cd-コマンドによる作業ディレクトリの変更):  
  セッション途中でプロンプトキャッシュを壊すことなく作業ディレクトリを移動できる `/cd` コマンドが追加された。セッションを開き直さずに別ディレクトリへ移れる。
3. [**disableBundledSkills 設定によるバンドルスキルの非表示**](#3-disablebundledskills-設定によるバンドルスキルの非表示):  
  バンドルされたスキル・ワークフロー・組み込みスラッシュコマンドをモデルから隠す `disableBundledSkills` 設定と環境変数 `CLAUDE_CODE_DISABLE_BUNDLED_SKILLS` が追加された。
4. [**スキルの disallowed-tools によるツール除外**](#4-スキルの-disallowed-tools-によるツール除外):  
  スキルの frontmatter に `disallowed-tools` を指定すると、そのスキルがアクティブな間だけ Claude の利用可能ツールから特定ツールを外せるようになった。制限は次のメッセージ送信時に解除される。
5. [**ゼロデータ保持 ZDR の適格アカウント要件の明確化**](#5-ゼロデータ保持-zdr-の適格アカウント要件の明確化):  
  ZDR が Claude for Enterprise の適格アカウント向けであり、標準の Enterprise プランには含まれず、Anthropic による個別有効化と適格性確認が必要である旨が複数ページで明確化された。
<!-- light:highlight-list:end -->

## 1. safe-mode フラグによる全カスタマイズ無効化

新しい `--safe-mode` フラグ（および環境変数 `CLAUDE_CODE_SAFE_MODE`）が追加されました。これを付けて起動すると、CLAUDE.md・プラグイン・スキル・フック・MCP サーバーといった**すべてのカスタマイズを無効化**した状態で Claude Code が立ち上がります。

設定やプラグインが原因の不具合を切り分けたいときに、素の状態から動作を確認できるトラブルシュート用途を想定した機能です。本変更は v2.1.169 の changelog に記載されています（設定・CLI リファレンス等の通常ページには未反映のため、参考リンクは省略します）。

## 2. /cd コマンドによる作業ディレクトリの変更

`/cd` コマンドが追加されました。セッションの途中で**プロンプトキャッシュを壊すことなく**、作業ディレクトリ（working directory）を新しい場所へ移動できます。

これまでディレクトリを切り替えるにはセッションを開き直す必要があり、その際にプロンプトキャッシュが失われていましたが、セッションを維持したまま別ディレクトリへ移れるようになりました。本変更は v2.1.169 の changelog に記載されています（該当する通常ページが無いため、参考リンクは省略します）。

## 3. disableBundledSkills 設定によるバンドルスキルの非表示

新しい設定 `disableBundledSkills` と環境変数 `CLAUDE_CODE_DISABLE_BUNDLED_SKILLS` が追加されました。これらを使うと、バンドルされたスキル・ワークフロー・組み込みスラッシュコマンドを**モデルから隠す**ことができます。

不要な組み込み機能をモデルの選択肢から外したい場合に利用できます。本変更は v2.1.169 の changelog に記載されています（設定リファレンス等の通常ページには未反映のため、参考リンクは省略します）。

## 4. スキルの disallowed-tools によるツール除外

スキルの frontmatter に `disallowed-tools` を指定することで、**そのスキルがアクティブな間だけ** Claude の利用可能なツールのプールから特定のツールを外せるようになりました。この制限は**次のメッセージを送った時点で解除**されます。

すべてのスキルとプロンプトにわたってツールを恒久的にブロックしたい場合は、従来どおり権限設定（permission settings）の deny ルールを使います。スキルのドキュメントも、従来の「deny ルールを使う」記述からこの新しい `disallowed-tools` の説明へ更新されました。

- [スキルで Claude を拡張する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/skills)
- [Extend Claude with skills - Claude Code Docs (English)](https://code.claude.com/docs/en/skills)

## 5. ゼロデータ保持 ZDR の適格アカウント要件の明確化

ゼロデータ保持（Zero Data Retention; ZDR）に関する記述が更新され、ZDR が **Claude for Enterprise の適格アカウント（qualified accounts）向け**であることが明確化されました。

あわせて、ZDR は**標準の Enterprise プランには含まれず**、管理者設定からは有効化できないこと、有効化には Anthropic による**個別の手続き**が必要で、適格性の確認が前提となることが追記されました。ZDR が必要な組織は、セールスまたは Anthropic のアカウントチームに問い合わせて適格性を確認します。この趣旨はゼロデータ保持ページ本文（Note を含む）のほか、データ利用ページや組織向けセットアップページの概要表にも反映されています。

- [ゼロデータ保持 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/zero-data-retention)
- [Zero data retention - Claude Code Docs (English)](https://code.claude.com/docs/en/zero-data-retention)

## 新規追加されたページ

<!-- light:new-pages:start -->
*(新規追加されたページはありません)*
<!-- light:new-pages:end -->

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
*(大幅に更新されたページはありません)*
<!-- light:updated-pages:end -->

## 軽微な更新

<!-- light:minor-updates:start -->
- changelog ページに 1 つのリリースエントリ（v2.1.169、2026年06月08日）が追加されました。
  - **v2.1.169**: ハイライトに挙げた 3 件（`--safe-mode`／`/cd`／`disableBundledSkills`）に加え、次の修正・改善を含みます。
    - 長い入力行で折り返した行を超えてコマンド履歴へジャンプしていた上下矢印を修正。各表示行を先に移動するようになり、履歴呼び出しは近い端から入るようになった。
    - エンタープライズの管理 MCP ポリシー（`allowedMcpServers`／`deniedMcpServers`）が、再接続時・IDE で入力した構成・インストール後最初のセッション中の `--mcp-config` サーバー・リモート設定の読み込み前に強制されない問題を修正。リモート設定を持たない組織での遅いコールドスタートも修正。
    - claude.ai 認証情報でログインした macOS ユーザーで、各ターン開始時に約 30〜50ms の UI 停止が起きる問題を修正。
    - Windows で `claude -p` がスラッシュコマンド／スキルのスキャン待ちの間に遅くなる・ハングしたように見える問題を修正（2.1.161 のリグレッション）。
    - セッション再開時に OAuth トークン更新が同時に起きると、リモートコントロールが「reconnecting」で止まる問題を修正。
    - バックグラウンドの git コマンドがキャッシュ済み認証情報なしで実行されたとき、Windows の起動時に Git Credential Manager の「Connect to GitHub」ポップアップが出る問題を修正。
    - カスタムステータスラインを使うユーザーでフッターのヒント（例: 「esc to interrupt」）が表示されない問題を修正。
    - ワーカーが死んだリモートセッションに再アタッチするたび、待機中だった古い権限・ダイアログのプロンプトが再表示される問題を修正。
    - `claude agents --json` がブロック中・ディスパッチ直後のバックグラウンドセッションを省く問題を修正。完了済みセッションを含める `--all` と、新しい `id`・`state` フィールドを追加。
    - Windows Terminal の WSL でエージェントから戻ったあと、エージェントビューに古い／文字化けしたフレームが残る問題を修正。
    - 事前ウォームされたワーカーにディスパッチされたバックグラウンドエージェントが、プロジェクトレベル設定の `env` 値（例: `ANTHROPIC_MODEL`）を無視する問題を修正。
    - Windows で MCPB プラグインのキャッシュが誤って無効化され、不要な再展開が起きる問題を修正。
    - プラグインの `.in_use` PID ロックファイルが際限なく蓄積する問題を修正。クラッシュしたセッションの古いマーカーは 1 日 1 回掃除されるようになった。
    - 信頼されていないプロジェクト設定が、信頼確認なしに OTEL クライアント証明書のパスを設定できる問題を修正。
    - ターン進行中でも `/workflows` がすぐ開くようになった。
    - `TaskCreate` の信頼性を改善。不正な入力は自動修復され、未ロードのツールに対する検証エラーにスキーマが含まれるようになった。
    - 組織が API キー認証を無効化している場合のエラーメッセージを改善し、現在の API キーの出所に基づくガイダンスを表示するようにした。
    - 応答ストリーミング中とスピナーアニメーション中の CPU 使用率を削減。
    - Vertex／Foundry でデフォルト 5 分のアイドルタイムアウトを復活させ、停止したストリームが無限にハングせず中断されるようにした。`API_FORCE_IDLE_TIMEOUT=0` で無効化可能。
    - リモート管理設定に無効なエントリがあるとき、ペイロード全体を黙って破棄せず、残りの有効なポリシーを適用して検証エラーを表面化するようにした。
    - バックグラウンドセッションが retire→wake をまたいで `--ide`・`--chrome`・`--bare`・`--remote-control` などのフラグを保持するようになり、再生成時の状態検証も強化された。
    - バックグラウンドセッションに、worktree に入るまで共有チェックアウトの編集がブロックされる旨を伝えるようにし、`EnterWorktree` 前の無駄な編集拒否を避けるようにした。
    - 「CLAUDE.md is too long」警告のしきい値が、モデルのコンテキストウィンドウに応じてスケールするようになった。
    - Windows の自動更新が、`claude.exe` が別プロセスに保持されている場合、セッション内での再試行を停止するようになった。
    - スラッシュコマンドメニューのスキルタグの色コントラストを改善。
    - 支払い方法のない Apple／Google 課金のサブスクライバーがプロモクレジットを請求する際、支払い方法の追加場所を案内するようにした。
    - 複数の並行セッションを実行しているとき、`claude agents` を提案するヒントを追加。
- [日本語](https://code.claude.com/docs/ja/skills) / [English](https://code.claude.com/docs/en/skills):  
  スキルの frontmatter `disallowed-tools` でスキル稼働中のツールを除外できる旨が追記されました（詳細はハイライト 4 参照）。
- [日本語](https://code.claude.com/docs/ja/zero-data-retention) / [English](https://code.claude.com/docs/en/zero-data-retention):  
  ゼロデータ保持ページ本文が拡充され、ZDR が標準 Enterprise プランに非同梱で適格アカウント向け・Anthropic による個別有効化が必要である旨の Note が追加されました（詳細はハイライト 5 参照）。
- [日本語](https://code.claude.com/docs/ja/data-usage) / [English](https://code.claude.com/docs/en/data-usage):  
  データ利用ページの保持に関する記述が、ZDR は適格アカウント向け・標準プラン非同梱で適格確認後に有効化される、という表現へ更新されました。
- [日本語](https://code.claude.com/docs/ja/admin-setup) / [English](https://code.claude.com/docs/en/admin-setup):  
  組織向けセットアップページのデータ取り扱い概要表の ZDR 行が「適格アカウント向け（available to qualified accounts）」表記へ更新されました。
<!-- light:minor-updates:end -->

## 新着情報

<!-- light:whats-new:start -->
*(今回の対象期間に新着情報（週間ダイジェスト）の更新はありません)*
<!-- light:whats-new:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-06-07.md](./archives/latest/2026-06-07.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-06-07.md](./archives/latest-detail/2026-06-07.md)

<!--
base_commit: e5d9dfc35723075599065ec9bc400eacf168e564
head_commit: f31d0c4aeda71092a3db3bbef9405dcfc432e5ab
generated_at_full: 2026-06-09T15:02:52+09:00
-->
