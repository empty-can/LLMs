---
対象期間: 2026年06月06日 〜 2026年06月07日
作成日: 2026-06-07
---

# Claude Code 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
> 今回の更新は changelog ページのみの変更で、リリースエントリ v2.1.166・v2.1.167・v2.1.168 が追加されました。リファレンスページ本体の変更はありません。v2.1.167・v2.1.168 はバグ修正と信頼性向上のみですが、v2.1.166 には複数の新機能とセキュリティ強化、多数のバグ修正が含まれます。
>
> 主要なものを以下に挙げます。
>
> 1. プライマリモデルが過負荷・利用不可のときに順に試す最大 3 つのフォールバックモデルを設定する `fallbackModel` を追加
> 2. deny ルールのツール名位置で glob パターンに対応（`"*"` で全ツール拒否）
> 3. 別セッションから `SendMessage` で中継されたメッセージがユーザー権限を持たないようクロスセッションメッセージングを強化
> 4. Claude API 経由でデフォルトで思考するモデルに対し thinking の無効化操作が効くよう変更
> 5. API が予期しない非リトライ可能エラーを返したとき、フォールバックモデルでターンを 1 回だけ再試行
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**フォールバックモデル設定 fallbackModel の追加**](#1-フォールバックモデル設定-fallbackmodel-の追加):  
  プライマリモデルが過負荷または利用不可のときに順に試す最大 3 つのフォールバックモデルを設定できる `fallbackModel` が追加された。`--fallback-model` フラグも対話セッションに適用されるようになった。
2. [**deny ルールでのツール名 glob パターン対応**](#2-deny-ルールでのツール名-glob-パターン対応):  
  deny ルールのツール名位置で glob パターンが使えるようになり、`"*"` で全ツールを拒否できる。allow ルールは非 MCP の glob を拒否し、deny ルール中の未知のツール名は起動時に警告される。
3. [**クロスセッションメッセージングのセキュリティ強化**](#3-クロスセッションメッセージングのセキュリティ強化):  
  他の Claude セッションから `SendMessage` で中継されたメッセージはユーザー権限を持たなくなった。受信側は中継された権限要求を拒否し、auto モードはこれをブロックする。
4. [**デフォルトで思考するモデルの thinking 無効化対応**](#4-デフォルトで思考するモデルの-thinking-無効化対応):  
  `MAX_THINKING_TOKENS=0`・`--thinking disabled`・モデル別の thinking トグルが、Claude API 経由でデフォルトで思考するモデルに対しても thinking を無効化できるようになった（サードパーティプロバイダーは従来どおり）。
5. [**非リトライ可能エラー時のフォールバックモデルへの自動リトライ**](#5-非リトライ可能エラー時のフォールバックモデルへの自動リトライ):  
  API が予期しない非リトライ可能エラーを拒否で返したとき、Claude Code がフォールバックモデルでそのターンを 1 回だけ再試行するようになった。認証・レート制限・リクエストサイズ・トランスポートのエラーは従来どおり即座に表面化する。
<!-- light:highlight-list:end -->

## 1. フォールバックモデル設定 fallbackModel の追加

新しい設定 `fallbackModel` が追加されました。プライマリモデルが過負荷（overloaded）または利用不可（unavailable）のときに、順に試行する**最大 3 つ**のフォールバックモデルを構成できます。指定した順序で試されるため、優先度の高い代替モデルから順にフォールバックさせられます。

あわせて、これまで主にヘッドレス／非対話起動向けだった `--fallback-model` フラグが、**対話セッションにも適用される**ようになりました。これにより、対話的に Claude Code を使っている最中でもプライマリモデルが落ちた際のフォールバック先をコマンドラインから指定できます。本変更は v2.1.166 の changelog に記載されています。

- [Claude Code 変更履歴 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/changelog)
- [Claude Code changelog - Claude Code Docs (English)](https://code.claude.com/docs/en/changelog)

## 2. deny ルールでのツール名 glob パターン対応

権限ルールの deny ルールにおいて、ツール名を書く位置で **glob パターン**が使えるようになりました。たとえば `"*"` を指定するとすべてのツールを拒否できます。広範なツール群を一括で拒否する用途が簡潔に書けるようになります。

一方で allow ルールは MCP 以外の glob を**拒否**します（許可は広く効きすぎるとリスクが大きいため、ワイルドカード許可は MCP に限定される趣旨です）。また、deny ルール中に未知（存在しない）のツール名が含まれている場合は、**起動時に警告**が出るようになり、ルールの綴り間違いなどに気づきやすくなりました。本変更は v2.1.166 の changelog に記載されています。

- [Claude Code 変更履歴 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/changelog)
- [Claude Code changelog - Claude Code Docs (English)](https://code.claude.com/docs/en/changelog)

## 3. クロスセッションメッセージングのセキュリティ強化

複数の Claude セッション間でメッセージをやり取りする仕組みが強化されました。他の Claude セッションから `SendMessage` で**中継された**メッセージは、もはや**ユーザー権限（user authority）を持ちません**。これにより、別セッション経由で権限昇格を引き起こすような中継を防ぎます。

具体的には、受信側のセッションは中継された権限要求（permission request）を**拒否**し、auto モードはそれらを**ブロック**します。セッション間メッセージングを悪用して、本来ユーザーの承認が必要な操作を別セッション経由で通そうとする経路が塞がれました。本変更は v2.1.166 の changelog に記載されています。

- [Claude Code 変更履歴 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/changelog)
- [Claude Code changelog - Claude Code Docs (English)](https://code.claude.com/docs/en/changelog)

## 4. デフォルトで思考するモデルの thinking 無効化対応

`MAX_THINKING_TOKENS=0`・`--thinking disabled`・およびモデル別の thinking トグルが、**Claude API 経由でデフォルトで思考する**モデルに対しても thinking を無効化できるようになりました。これまでデフォルトで思考が有効なモデルでは、これらの操作で思考を止めきれないケースがありましたが、今回それらが期待どおり thinking を無効化します。

なお、この挙動変更は Claude API 経由のモデルが対象で、**サードパーティプロバイダー（3P）は従来どおり**で変更されません。本変更は v2.1.166 の changelog に記載されています。

- [Claude Code 変更履歴 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/changelog)
- [Claude Code changelog - Claude Code Docs (English)](https://code.claude.com/docs/en/changelog)

## 5. 非リトライ可能エラー時のフォールバックモデルへの自動リトライ

API が**予期しない非リトライ可能エラー**を拒否（reject）として返したとき、Claude Code がそのターンを**フォールバックモデルで 1 回だけ再試行**するようになりました。プライマリモデル側で想定外のエラーが起きても、フォールバック先で一度リカバリを試みることで、ターンが即失敗するのを避けられます。

ただし、認証（auth）・レート制限（rate-limit）・リクエストサイズ（request-size）・トランスポート（transport）の各エラーは、これまでどおり**即座に表面化**します（これらは再試行で解決しない性質のため）。本変更は v2.1.166 の changelog に記載されています。

- [Claude Code 変更履歴 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/changelog)
- [Claude Code changelog - Claude Code Docs (English)](https://code.claude.com/docs/en/changelog)

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
- [日本語](https://code.claude.com/docs/ja/changelog) / [English](https://code.claude.com/docs/en/changelog): changelog ページに 3 つのリリースエントリ（v2.1.166・v2.1.167・v2.1.168、いずれも 2026年06月06日）が追加されました。
  - **v2.1.168**: バグ修正と信頼性向上のみ。
  - **v2.1.167**: バグ修正と信頼性向上のみ。
  - **v2.1.166**: ハイライトに挙げた上位 5 項目（`fallbackModel`・deny ルールの glob 対応・クロスセッションメッセージング強化・thinking 無効化・非リトライ可能エラー時のフォールバック再試行）に加え、次の改善・修正を含みます。
    - `claude update` がダウンロード前に対象バージョンを通知するようになった（従来は無言）。
    - `claude agents` の一覧で URL を入力すると、その URL を最初のプロンプトに含むセッションに絞り込めるようになった。
    - 処理できない画像を送信した際に繰り返し出ていた「image could not be processed」エラーと余分なトークン消費を修正。
    - 起動時のワーカー登録中に短時間のバックエンド障害が起きると、リモートセッションが恒久的に固まる問題を修正。
    - JetBrains 系 IDE（IntelliJ・PyCharm・WebStorm 等）2026.1 以降のターミナルのちらつきを、同期出力の有効化で修正。
    - Kitty キーボードプロトコルを使うターミナル（WezTerm・Ghostty・kitty）で Shift＋非 ASCII 文字（例: Shift+ä → Ä）が脱落する問題を修正。
    - Windows で、kill されたプロセスの子が出力パイプを保持した際に PowerShell コマンド検証が制限時間を大幅に超えてハングする問題を修正。
    - macOS で、デーモン停止後に接続が残ると孤立した `claude --bg-pty-host` プロセスが CPU 100% で回り続ける問題を修正。
    - `/voice` 切替後に古い認証チェックを消すため `/login` が必要だった voice モードの問題を修正。
    - 管理設定（managed settings）に無効なエントリが 1 つあると、残りの有効なポリシーの強制まで無言で無効化される問題を修正。
    - 管理設定の `allowedMcpServers`／`deniedMcpServers` 述語が `${VAR}` 参照を使うとマッチしない問題を修正。
    - git worktree に入ったバックグラウンドエージェントのセッションが、`claude agents` から再オープンすると「No conversation found」でクラッシュループする問題を修正。
    - ストリーミング中に Ctrl+O のトランスクリプト表示で思考テキストが重複する問題を修正。
    - リモートセッション内で実行した `/doctor` が「Not inside a remote session」という矛盾した失敗チェックを表示する問題を修正。
    - `claude agents` のディスパッチ／返信入力で、複数行プロンプト入力時にカーソルが 1 行目末尾に張り付く問題を修正。
    - Unicode 非対応ターミナルで、タスクリストのバックグラウンドエージェント行間に空行が出る問題を修正。
<!-- light:minor-updates:end -->

## 新着情報

<!-- light:whats-new:start -->
*(今回の対象期間に新着情報（週間ダイジェスト）の更新はありません)*
<!-- light:whats-new:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/2026-06-06/latest.md](./archives/2026-06-06/latest.md)
- 前回サマリ(詳細版): [./archives/2026-06-06/latest-detail.md](./archives/2026-06-06/latest-detail.md)

<!--
base_commit: 980975cf497b0cce6847425a0787fccd839be1ae
head_commit: e5d9dfc35723075599065ec9bc400eacf168e564
generated_at_full: 2026-06-07T18:53:07+09:00
-->
