---
対象期間: 2026年08月01日 〜 2026年08月03日
作成日: 2026-08-03
---

# Claude Code 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
今回は約 2 日ぶんの差分で、changelog へのリリースエントリ追加はありません。フルスクリーンレンダリングの既定化、フックの新イベント、公式プラグインマーケットプレイスの自動登録が届かない条件の明文化が中心です。

主要なものを以下に挙げます。

1. フルスクリーンレンダリングが、2026年05月06日以降に Claude Code を使い始めたユーザーでは既定になった
2. セッション途中の作業ディレクトリ追加で発火するフックイベント `DirectoryAdded` が新設された
3. 公式 Anthropic マーケットプレイスの自動登録が届かないマシンの条件と、その場合の対処が明文化された
4. `claude -p` の終了コードと、bare mode が要求する認証情報の渡し方が明記された
5. バックグラウンドセッションの既定エージェントとして `claude` が組み込みエージェント表に加わった
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**フルスクリーンレンダリングが新しいユーザーには既定に**](#1-フルスクリーンレンダリングが新しいユーザーには既定に):  
  2026年05月06日以降に Claude Code を使い始めた場合、既定でフルスクリーン描画になり、`/tui default` でクラシックレンダラーへ戻す形になった。それ以前から使っている場合は従来どおり。
2. [**ディレクトリ追加で発火するフックイベント DirectoryAdded の新設**](#2-ディレクトリ追加で発火するフックイベント-directoryadded-の新設):  
  `/add-dir` や SDK の `register_repo_root` でセッション途中に作業ディレクトリを足したあとに走る。新しく足したリポジトリの依存関係を入れる、といった下準備に使える。
3. [**公式マーケットプレイスの自動登録が届かないケースの明文化**](#3-公式マーケットプレイスの自動登録が届かないケースの明文化):  
  自動登録は初回の対話起動時にしか働かず、非対話環境や過去にポリシーでブロックされたマシンは漏れる。漏れたマシンでは `extraKnownMarketplaces` か手動登録が要る。
4. [**ヘッドレス実行の終了コードと bare mode の認証要件が明記された**](#4-ヘッドレス実行の終了コードと-bare-mode-の認証要件が明記された):  
  `claude -p` は成功で 0・失敗で非ゼロを返す。bare mode はサブスクリプションのログインを使わないため、`ANTHROPIC_API_KEY` などを明示的に渡す必要がある。
5. [**バックグラウンドセッションの既定エージェント claude が一覧に追加**](#5-バックグラウンドセッションの既定エージェント-claude-が一覧に追加):  
  `claude agents` や `claude --bg` でエージェントを指定せずに起動したときに使われるヘルパーエージェントで、モデルは親から継承する。
<!-- light:highlight-list:end -->

## 1. フルスクリーンレンダリングが新しいユーザーには既定に

フルスクリーンレンダリングのページ冒頭の注記が書き換わり、**オプトインではなくなりました**。従来は「フルスクリーンレンダリングはオプトインのリサーチプレビューです。現在の会話で `/tui fullscreen` を実行して切り替えてください」でしたが、現在は「フルスクリーンレンダリングはリサーチプレビューです。**2026年05月06日以降に初めて Claude Code を使った場合、Claude Code はフルスクリーンで描画します**。`/tui default` を実行するとクラシックレンダラーに戻せます。それ以前から使っている場合はクラシックレンダラーのままなので、`/tui fullscreen` で現在の会話を切り替えてください」となっています。リサーチプレビューであること自体と、フィードバック次第で挙動が変わりうる点は変わりません。

この既定の入れ替わりに合わせて、これまで「default renderer（既定のレンダラー）」と呼んでいたものが**クラシックレンダラー**という呼称に統一されました。インタラクティブモードのページでは、トランスクリプトビューアの `Ctrl+E`（全内容の表示トグル）がクラシックレンダラー専用であること、`Ctrl+R` の説明の「以下の手順は既定のインライン検索について述べたもの」が「以下の手順はクラシックレンダラーのインライン検索について述べたもの」に変わっています。キーバインドのページでも、`transcript:toggleShowAll` が効くのはクラシックレンダラーのみであること、`historySearch:next` などの既定バインドがクラシックレンダラーのインライン履歴検索に対応することが同じ言い方に揃えられました。どれも指している挙動は従来と同じで、既定側が入れ替わったことによる呼称の整理です。

- [日本語](https://code.claude.com/docs/ja/fullscreen) / [Fullscreen rendering - Claude Code Docs (English)](https://code.claude.com/docs/en/fullscreen)
- [Interactive mode - Claude Code Docs (English)](https://code.claude.com/docs/en/interactive-mode#transcript-viewer)

## 2. ディレクトリ追加で発火するフックイベント DirectoryAdded の新設

セッションの途中で作業ディレクトリが追加されたあとに走る **`DirectoryAdded`** イベントが追加されました。発火元は `/add-dir` コマンドと、SDK の `register_repo_root` 制御リクエストの 2 つです。新しく加えたリポジトリの依存関係をインストールする、といった下準備に使えます。起動フラグの `--add-dir` で渡したディレクトリでは発火せず、そちらは従来どおり `SessionStart` が受け持ちます。発火のタイミングは Claude Code がサンドボックスと権限の状態を更新し終えたあとなので、フックが走る時点でサンドボックス化されたツールからも新しいディレクトリが見えています（フックのコマンド自体はサンドボックス外で実行されます）。matcher は追加経路で絞るもので、`slash_command`（`/add-dir` での追加）と `register_repo_root`（SDK クライアントからの追加）の 2 つです。

入力は共通フィールドに加えて `directory`（追加されたディレクトリの絶対パス）と `source`（`"slash_command"` または `"register_repo_root"`）を受け取ります。決定制御は持たず、フックが走る時点で追加は完了しているため中止はできません。特徴的なのは出力の扱いが追加経路で異なる点で、`slash_command` の場合は**他のどのイベントとも違って**、フックの `systemMessage` が次の会話ターンの文脈として Claude に渡されます（他のイベントでは `systemMessage` はユーザーに見えて Claude には渡りません）。失敗したフックについてはトランスクリプトに件数だけが出て、詳細な失敗出力はデバッグログ行きです。`register_repo_root` の場合は `systemMessage` も失敗出力もデバッグログにのみ書かれます。exit code 2 も特別扱いで、ブロックはできず stderr はデバッグログに送られます。対応するフック形式は `command` / `http` / `mcp_tool` で、`prompt` と `agent` には対応しません。

- [Hooks reference - Claude Code Docs (English)](https://code.claude.com/docs/en/hooks#directoryadded)
- [Automate actions with hooks - Claude Code Docs (English)](https://code.claude.com/docs/en/hooks-guide#how-hooks-work)

## 3. 公式マーケットプレイスの自動登録が届かないケースの明文化

`strictKnownMarketplaces` で公式 Anthropic マーケットプレイスだけを許可する構成について、従来は「このエントリがあれば公式マーケットプレイスは初回の対話起動時に自分で登録されるので、`extraKnownMarketplaces` と組み合わせる必要はない」と書かれていました。現在は「Claude Code は既に登録済みの公式マーケットプレイスを使えるまま保ち、まっさらなマシンでは初回の対話起動時に自動で登録する」に改められ、そのうえで**自動登録が全てのマシンをカバーするわけではない**ことが明記されました。よく漏れるのは 2 つで、①そのマシンで最初の対話起動が起きる前に走る非対話環境、②空配列によるロックダウンのように、マーケットプレイスをブロックするポリシーの下で既に対話起動したことのあるマシンです。②では Claude Code がブロックされた試行を記録するため、**ポリシーを変えたあとも再試行しません**。これらのマシンでは、同じ `managed-settings.json` の `extraKnownMarketplaces` に公式マーケットプレイスを加えて自動登録させるか、`claude plugin marketplace add anthropics/claude-plugins-official` を実行します。設定ページの `strictKnownMarketplaces` の説明にも同じ内容が入り、「`strictKnownMarketplaces` だけを設定した場合、許可したマーケットプレイスは手動でしか追加できない」という記述が、Claude Code が自ら登録するのは公式マーケットプレイスだけであること、それも許可リストが許している場合に限られること、漏れるマシンをカバーするには `extraKnownMarketplaces` にも入れることを含む形に書き換えられています。

関連する記述が周辺ページにも反映されました。プラグインの発見ページの「Claude Code は起動時に公式 Anthropic マーケットプレイスを自動で追加します」は「**初めて対話的に起動したとき**に自動で追加します」に変わり、自分で追加すべき理由に「ネットワークがダウンロードをブロックしている場合」に加えて「マーケットプレイスのポリシーが以前の試行をブロックした場合」が並びました。プラグイン作成ページの 2 つの公開マーケットプレイスの説明も同様です。環境変数 `CLAUDE_CODE_DISABLE_OFFICIAL_MARKETPLACE_AUTOINSTALL` は、従来の「初回実行時の公式プラグインマーケットプレイスの自動追加をスキップするには `1` を設定」から大きく書き足され、Claude Code がこの変数を読むのは**マーケットプレイスを登録しようとする時点**（通常はそのマシンの初回対話起動時）であること、その時点で設定されていれば登録を**恒久的に**スキップすること、あとから変数を解除してもスキップは取り消されないこと、`claude plugin marketplace add anthropics/claude-plugins-official` を実行すればいつでも登録できることが明記されました。

- [日本語](https://code.claude.com/docs/ja/plugin-marketplaces#managed-marketplace-restrictions) / [Create and distribute a plugin marketplace - Claude Code Docs (English)](https://code.claude.com/docs/en/plugin-marketplaces#managed-marketplace-restrictions)
- [Claude Code settings - Claude Code Docs (English)](https://code.claude.com/docs/en/settings#strictknownmarketplaces)

## 4. ヘッドレス実行の終了コードと bare mode の認証要件が明記された

`claude -p` の基本的な使い方の節に、**終了コード**の説明が加わりました。Claude Code は成功時に 0、実行が失敗したときは非ゼロで終了するため、スクリプト側は終了ステータスで分岐できます。無効なフラグを渡した場合は実行が始まる前に stderr へエラーを報告し、認証が無いなど**実行の内側で**起きた失敗は、失敗内容が結果として stdout に出力されます。

bare mode の認証の説明も、節の末尾からコード例の直前へ移ったうえで具体化されました。例の前に「bare mode はサブスクリプションのログインを使わないため、実行前に `ANTHROPIC_API_KEY` を設定してください」が置かれ、例の直後に「bare mode は OAuth とシステムキーチェーンをスキップするので、Claude Code が見るのは明示的に渡した認証情報だけです。Anthropic API なら [Claude Console](https://platform.claude.com) で作ったキーを環境変数 `ANTHROPIC_API_KEY` に設定するか、`--settings` に渡す JSON で `apiKeyHelper` を指定します。Amazon Bedrock、Google Cloud の Agent Platform、Microsoft Foundry は従来どおり各プロバイダの認証情報を読みます」と続きます。例のプロンプトも `Summarize this file` から `Summarize README.md` に変わり、そのまま実行できる形になりました。

例の節そのものも読者が写経しやすい方向に手が入っています。導入文に「`auth.py` や `build-error.txt` のようにファイル名が出てくる箇所は自分のプロジェクトのファイルに読み替えてください」が加わり、ビルドスクリプトの例には `npm run lint:claude` で実行する旨が、システムプロンプトをカスタマイズする例には `review.sh` として保存する前提と、`bash review.sh 123` と実行するとシェルが `"$1"` を `123` に置き換えるので PR 123 の diff を取得すること、レビュー結果は JSON で出力され本文は `result` フィールドに入ることが書き足されました。

- [Run Claude Code programmatically - Claude Code Docs (English)](https://code.claude.com/docs/en/headless#basic-usage)
- [Run Claude Code programmatically - Claude Code Docs (English)](https://code.claude.com/docs/en/headless#start-faster-with-bare-mode)

## 5. バックグラウンドセッションの既定エージェント claude が一覧に追加

組み込みサブエージェントの「その他」タブにあるヘルパーエージェントの表に、**`claude`** の行が加わりました。モデルは親から継承（Inherits）で、`claude agents` や `claude --bg` から**エージェントを指定せずに**バックグラウンドセッションを起動したときに使われます。ほかのサブエージェントと同じように、Claude 自身がこのエージェントへ委譲することもできます。この表はこれまで `statusline-setup`（Sonnet、`/statusline` でステータスラインを設定するとき）と `claude-code-guide`（Haiku、Claude Code の機能について質問したとき）の 2 行だけで、いずれも「通常は自動的に呼ばれるので直接使う必要はない」ものとして紹介されていました。バックグラウンドセッションで何が動いているのかが、この表から辿れるようになった形です。

- [Create custom subagents - Claude Code Docs (English)](https://code.claude.com/docs/en/sub-agents#built-in-subagents)

## 新規追加されたページ

<!-- light:new-pages:start -->
（今回の対象期間では、索引（`llms.txt`）への新しいページの追加はありません。見出しマップに新たに掲載された `claude-apps-gateway` と `llm-gateway` の 2 ページは、いずれも以前から索引にある既存ページです。詳細は「軽微な更新」の「その他」を参照してください。）
<!-- light:new-pages:end -->

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
- [**フックリファレンス**](#1-フックリファレンス) ([日本語](https://code.claude.com/docs/ja/hooks) / [English](https://code.claude.com/docs/en/hooks)):  
  新イベント `DirectoryAdded`（ハイライト 2 参照）が、ライフサイクル図・イベント一覧・matcher 一覧・exit code 表・JSON 出力表・対応フック形式の一覧まで一通りに反映された。
- [**フックでアクションを自動化する**](#2-フックでアクションを自動化する) ([日本語](https://code.claude.com/docs/ja/hooks-guide) / [English](https://code.claude.com/docs/en/hooks-guide)):  
  イベント一覧への `DirectoryAdded` 追加に加えて、フック入力の説明が JSON 内コメントから地の文と箇条書きに再構成された。
- [**インストールとログインのトラブルシューティング**](#3-インストールとログインのトラブルシューティング) ([日本語](https://code.claude.com/docs/ja/troubleshoot-install) / [English](https://code.claude.com/docs/en/troubleshoot-install)):  
  ダウンロードサーバーへの到達確認が macOS/Linux と Windows PowerShell の 2 タブに分かれ、成功判定の説明も両プラットフォームぶんに書き分けられた。
<!-- light:updated-pages:end -->

## 1. フックリファレンス

このページの変更はほぼすべて `DirectoryAdded` の新設に伴うもので、内容はハイライト 2 を参照してください。リファレンスとしては、新しいイベントが**どこに何行足されたか**が分かるように全体へ行き渡っています。フックライフサイクルの図の代替テキストでは、非同期に走る単発イベントの列挙が「…`CwdChanged`、`FileChanged`」から「…`CwdChanged`、`FileChanged`、`DirectoryAdded`」に変わりました。発火タイミングをまとめたイベント一覧、イベントごとの matcher の対象と値を並べた表（`slash_command` / `register_repo_root`）、exit code 2 がブロックになるかどうかの表（「stderr はデバッグログ行き。ディレクトリの追加は既に完了している」）、JSON で決定制御できるかどうかの表（`WorktreeRemove`・`Notification`・`SessionEnd` などと同じ「決定制御なし・ロギングやクリーンアップといった副作用向け」のグループ）にも、それぞれ行が加わっています。

加えて、`command` / `http` / `mcp_tool` のフックには対応するが `prompt` と `agent` には対応しないイベントの一覧にも `DirectoryAdded` が入りました。イベント本体の解説は `CwdChanged` の直後、`FileChanged` の前に置かれています。プラグインが定義できるフックのイベント表（プラグインリファレンス側）にも同じ行が追加されました。

- [Hooks reference - Claude Code Docs (English)](https://code.claude.com/docs/en/hooks#hook-lifecycle)
- [Plugins reference - Claude Code Docs (English)](https://code.claude.com/docs/en/plugins-reference#hooks)

## 2. フックでアクションを自動化する

イベント一覧への `DirectoryAdded` 追加（ハイライト 2 参照）のほかに、**フック入力の説明が書き直されました**。従来は JSON の例に `// unique ID for this session` のような行コメントを付けて各フィールドを説明していましたが、コメント付き JSON はそのままコピーすると使えないため、説明が本文側へ移されています。共通フィールドは地の文で説明され（`session_id` はそのセッションの一意な ID、`cwd` はイベントが発火した時点の作業ディレクトリ）、Claude が Bash コマンドを実行するときに `PreToolUse` フックが stdin で受け取るフィールドは `hook_event_name`（フックを起動したイベント）、`tool_name`（Claude がこれから使うツール）、`tool_input`（Claude がツールに渡した引数。Bash ならその `command` フィールドにシェルコマンドが入る）の箇条書きになりました。そのうえで、`npm test` を実行する場合の入力例がコメント無しの JSON として示されます。

- [Automate actions with hooks - Claude Code Docs (English)](https://code.claude.com/docs/en/hooks-guide#hook-input)

## 3. インストールとログインのトラブルシューティング

「ネットワーク接続を確認する」の節で、`downloads.claude.ai` への到達確認の手順が **macOS/Linux と Windows PowerShell の 2 タブ**に分かれました。従来は単一の bash コードブロックを置き、その下に「PowerShell では代わりに `curl.exe -sI` を実行してください。PowerShell は `curl` を `Invoke-WebRequest` にエイリアスしており、`-sI` フラグを拒否します」という 1 文を添える形でしたが、PowerShell 用のコードブロック（`curl.exe -sI https://downloads.claude.ai/claude-code-releases/latest`）が独立し、エイリアスの説明はそのタブ内の補足として置き直されています。

成功判定の説明も両プラットフォームぶんに書き分けられました。従来の「`HTTP/2 200` という行が出ればサーバーに到達しています」は、「最初の行のステータスが `200` ならサーバーに到達しています。macOS と Linux では `HTTP/2 200` が、Windows 同梱の `curl.exe` からは `HTTP/1.1 200 OK` が表示されます」となり、Windows で `HTTP/2 200` が出ないことを不具合と誤解しないようになっています。`403` はプロキシやネットワークフィルタ、または地域による利用不可、`5xx` は一時的なサービス障害、という後続の切り分けは変わりません。

- [Troubleshoot installation and login - Claude Code Docs (English)](https://code.claude.com/docs/en/troubleshoot-install#check-network-connectivity)

## 軽微な更新

<!-- light:minor-updates:start -->
今回の対象期間には changelog ページの更新がありません。以下ではハイライトと上記カテゴリに含めなかった変更を挙げます。

**新機能**

- fast mode のページに「Switch models while fast mode is on」（fast mode を有効にしたままモデルを切り替える）という小見出しが加わりました。ただし本文は本サマリの対象差分に含まれる集約全文（`llms-full.txt`）にまだ取り込まれておらず、見出しマップにのみ現れているため、内容の確認は次回以降になります — [English](https://code.claude.com/docs/en/fast-mode#switch-models-while-fast-mode-is-on)
- iOS シミュレータのページのトラブルシュートに「The simulator pane fails with Xcode 27」（Xcode 27 でシミュレータペインが失敗する）が加わりました。こちらも見出しマップにのみ現れており、本文は未取り込みです — [English](https://code.claude.com/docs/en/desktop-ios-simulator#the-simulator-pane-fails-with-xcode-27)

**機能改善**

- 公式 Anthropic マーケットプレイスの自動登録に関する記述が、プラグインの発見・プラグイン作成・環境変数の各ページにも反映されました（詳細はハイライト 3 参照） — [English](https://code.claude.com/docs/en/discover-plugins#official-anthropic-marketplace)
- フルスクリーンレンダリングの既定化に伴い、インタラクティブモードとキーバインドの各ページで「既定のレンダラー」が「クラシックレンダラー」に統一されました（詳細はハイライト 1 参照） — [English](https://code.claude.com/docs/en/keybindings#history-search-actions)
- Claude Desktop のサイドチャットの説明に、**デスクトップアプリはサイドチャットをディスクに保存しないため、アプリを閉じたあとに元のサイドチャットへ戻ることはできない**という制限が加わりました。利用できるのがローカル・SSH・WSL のセッションであることは変わりません — [English](https://code.claude.com/docs/en/desktop#ask-a-side-question-without-derailing-the-session)
- routines の「`/schedule` が Unknown command を返す」トラブルシュートで、認証方法によってメッセージが違うことが明記されました。Console API キーで認証している場合は `/schedule is available with Claude for Enterprise — ask your admin about migrating from API-key access` が表示され、クラウドプロバイダのログインでは従来どおり `Unknown command: /schedule` になります。フィーチャーフラグ取得を止める環境変数を設定している場合など、それ以外の原因では引き続き `Unknown command: /schedule` です — [English](https://code.claude.com/docs/en/routines#schedule-returns-unknown-command)
- Agent SDK の権限モードの説明が、エージェントループとクイックスタートの双方で書き直されました。従来の「allow / deny ルールでカバーされないツール呼び出しの扱いを決めるもの」から「どれだけ人の監督を入れるかを決めるもので、SDK は有効なモードを allow / deny ルールとあわせて決まった順序で評価する」となり、権限ページの「権限がどう評価されるか」への導線が加わっています — [English](https://code.claude.com/docs/en/agent-sdk/agent-loop#tool-permissions)
- Agent SDK の入力モードのページで、2 つのモードの並記から「（デフォルト・推奨）」の表記が外れ、「Streaming Input Mode: 永続的で対話的なセッション」「Single Message Input: セッション状態と再開を使う単発クエリ」という説明の形に揃えられました — [English](https://code.claude.com/docs/en/agent-sdk/streaming-vs-single-mode#overview)

**バグ修正**

- Agent SDK のカスタムツールのページで、Python のサンプルコードにあった `from claude_agent_sdk import tool` の重複行が 2 か所（エラー処理の例と画像を返すツールの例）で削除されました — [English](https://code.claude.com/docs/en/agent-sdk/custom-tools#handle-errors)

**その他**

- Agent SDK への移行ガイドで、ドキュメントの移動先の記述が「API Guide の Agent SDK セクション」から「Claude Code ドキュメント内の専用の Agent SDK セクション」に訂正され、同じ内容を重ねて述べていた Note（「Claude Code ドキュメントは CLI ツールと自動化機能に集中するようになりました」）が削除されました — [English](https://code.claude.com/docs/en/agent-sdk/migration-guide#whats-changed)
- 見出しマップ（`claude_code_docs_map.md`）の生成方式が変わりました。凡例に「`### Parent > Child` は入れ子のグループを、`####` はその配下のページを示す」が加わり、「Platforms and integrations」と「Gateways」の各グループが、自分の入れ子グループより**前**に置かれる並びに変わっています。あわせて、これまで見出しマップに載っていなかった `claude-apps-gateway`（Claude apps gateway の導入ガイド）と `llm-gateway`（その他の LLM ゲートウェイ）の 2 ページが掲載されるようになりました。いずれもページ自体は以前から索引（`llms.txt`）にあり、新設ではありません
<!-- light:minor-updates:end -->

## 新着情報

<!-- light:whats-new:start -->
（今回の対象期間では、新着情報ページ（`whats-new/`）に差分がありません。最新は Week 29（2026年07月13日～17日）のままで、Week 30 以降は本サマリ作成時点で未公開です。）
<!-- light:whats-new:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-08-01.md](./archives/latest/2026-08-01.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-08-01.md](./archives/latest-detail/2026-08-01.md)

<!--
base_commit: 2b1ea9facf64443e0a685bf0d7e42794cbbdc509
head_commit: 0616e41115819d35457d4265f785d4cfc3a6757f
generated_at_full: 2026-08-04T15:05:29+09:00
-->
