---
対象期間: 2026年08月19日 〜 2026年08月20日
作成日: 2026-08-20
---

# Claude Code 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
今回は 1 日分の取り込みで、60 ページに差分がありました。changelog には v2.1.238 の 1 リリースが加わっています。新規ページ・削除ページはなく、v2.1.238 で入った挙動変更を各ページに書き下ろす更新が中心です。

主要なものを以下に挙げます。

1. アーティファクトにコメントが付けられるようになり、Claude が自分で返信できるようになった
2. 権限プロンプトの Yes / No に一言添えて答えられるようになった
3. MCP の接続が新しいクライアントランタイム v2 に切り替わった
4. MCP の `headersHelper` がトラスト済みフォルダでしか動かなくなった
5. 別セッションがアイドルになったら 1 度だけ知らせてもらえるようになった
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**アーティファクトのコメントと Claude の自動返信**](#1-アーティファクトのコメントと-claude-の自動返信):  
  組織内で共有したアーティファクトにコメントスレッドが付き、`@claude` を付けたコメントは Claude が読んで返信できる。公開したセッションが動いている間は、Claude が自分から返信・編集するところまで解説された。
2. [**権限プロンプトにコメントを添えて答える**](#2-権限プロンプトにコメントを添えて答える):  
  Yes / No にカーソルを合わせて `Tab` を押すとコメント欄が開き、承認・拒否の理由を Claude に渡せる。`Esc` はコメント無しの No と同じ扱いになった。
3. [**MCP クライアントランタイム v2 への切り替え**](#3-mcp-クライアントランタイム-v2-への切り替え):  
  v2.1.232 以降は MCP TypeScript SDK 2.0 ベースの v2 ランタイムが既定になり、プロトコル改定 `2026-07-28` の打診・通知ストリーム・チャネルの制約が新設節としてまとまった。
4. [**headersHelper はトラスト済みフォルダでしか動かない**](#4-headershelper-はトラスト済みフォルダでしか動かない):  
  プロジェクトの `.mcp.json` やローカルスコープの `headersHelper` は、そのフォルダのトラストダイアログを受け入れるまで実行されなくなった。作業ディレクトリの決まり方と、資格情報の環境変数が除去される条件も明文化された。
5. [**別セッションがアイドルになったら 1 度だけ知らせてもらう**](#5-別セッションがアイドルになったら-1-度だけ知らせてもらう):  
  前回 changelog だけで告知された `notify_when_idle` に専用の節ができた。同じマシンの別セッションが次にアイドルへ入るか終了したときに、1 度だけ通知が返る。
<!-- light:highlight-list:end -->

## 1. アーティファクトのコメントと Claude の自動返信

アーティファクトのページに **Collect comments on an artifact** が新設されました。組織内で共有したアーティファクトには、共有された人がページ上でコメントを残せます。Claude Code v2.1.221 以降と Team / Enterprise プランが要り、コメントを受け付けるのは組織内で共有したアーティファクトだけです。公開リンクで共有したページはコメントできず、`Comments aren't available while this Artifact is shared publicly.` と表示されます。既にコメントスレッドがあるアーティファクトを公開リンクに切り替えるには、先にスレッドを消す必要があります。Claude がコメントを読むのは 2 通りで、アーティファクトの URL を渡して読むよう頼んだ場合と、スレッドで `@claude` に言及するかスレッドの Claude コントロールを使ってコメントが Claude 宛に送られた場合です。後者の操作がスレッドを有効化し、Claude が返信できるのは誰かが有効化したスレッドだけです。ビューアには各返信が「Claude が、あなたを介して」書いたものとして表示されます。Claude がコメントを読めないと答えるときの確認先も 3 つ挙げられました。バージョンが v2.1.221 以降であること、インストールやアップグレード直後の最初のセッションでないこと、そしてフィーチャーフラグの取得を切っているなら `CLAUDE_CODE_ARTIFACT_COMMENTS=1` を設定することです。

配下に **Let Claude reply to comments on its own** も新設されました。セッションがアーティファクトを公開すると、Claude Code はそのセッションが動いている間そのアーティファクトを見張ります。Claude 宛のコメントが届くとすぐセッションに入り、頼まなくても Claude がスレッドを読んで返信します。v2.1.228 以降が必要で、フラグ取得を切っている場合は `CLAUDE_CODE_ARTIFACT_COMMENTS_AUTOREACT=1` も要ります。何が起きるかは権限モード次第で、返信を承認無しで投稿できるモードなら Claude が自分で返信し、必要なら記事も直します（`Auto-replied to comment thread on Artifact: <name>` などが出ます）。承認が要るモードでは `Comments are waiting on Artifact: <name>` が出て、スレッドを読む承認と返信を投稿する承認の 2 回を求められます。プランモードではモードを抜けるまで返信しません。1 時間のうちに同じアーティファクトで 60 件を処理すると自動返信を止め、その 1 時間分が抜けていくにつれ再開します。見張っているアーティファクトは `/tasks` にライブ更新タスクとして並びます。止め方は 3 通りで、`Ctrl+C` を 1 回押すと全アーティファクトで止まり（再公開すると再開）、`/tasks` でタスクを止めるとそのアーティファクトではセッションの残りの間止まり（再公開しても再開せず、後でセッションを再開しても返信しません）、`Ctrl+X Ctrl+K` を 3 秒以内に 2 回押すとセッションの残りの間すべてのアーティファクトで止まります。

- [Share session output as artifacts - Claude Code Docs (English)](https://code.claude.com/docs/en/artifacts#collect-comments-on-an-artifact)
- [Share session output as artifacts - Claude Code Docs (English)](https://code.claude.com/docs/en/artifacts#let-claude-reply-to-comments-on-its-own)

## 2. 権限プロンプトにコメントを添えて答える

権限のページに **Add a comment when you answer a permission prompt** が新設されました。1 回分の承認・拒否に、Claude 宛のメモを添えられます。Bash・PowerShell・ファイル・MCP ツールなど多くの権限プロンプトで、**Yes** か **No** にカーソルを合わせて `Tab` を押すと、その選択肢にコメント欄が開きます。WebFetch とブラウザのプロンプトには欄がなく、セッションの残りの間許可する選択肢やルールを保存する選択肢も受け付けません。欄を開いた状態でのキーは 3 通りで、`Enter` はコメント付きで回答（空欄ならコメント無しで回答）、`Tab` は回答せずに欄を閉じる（打った文字は保持され、その選択肢で回答すれば送られます）、ファイルのプロンプトでの `Shift+Tab` は `Tab` と同じく欄を閉じるだけです。v2.1.235 より前は、欄の中で `Shift+Tab` を押すとセッションの残りの間許可する選択肢が選ばれてしまい、コメントは捨てられていました。コメントの届き方は回答で変わり、**Yes** なら Claude Code が動作を実行してから結果の後にコメントを送り、**No** なら拒否の理由として送って Claude が作業を続けます。メインの会話のプロンプトでコメント無しの **No** を選んだ場合だけは、ターンが止まります。

インタラクティブモードとキーバインドの側も追随しました。ショートカット表に `Tab` の行が新設され、オートコンプリートの候補が出ているときは候補の確定、権限プロンプトでは **Yes** / **No** にコメント欄を開く（もう一度押すと閉じる）と整理されています。`Esc` の説明も、ダイアログを閉じるだけでなく「権限プロンプトではコメント無しの **No** と同じく動作を拒否する」に変わりました。`Shift+Tab` はファイルのプロンプトで開いている欄を閉じ、欄が無ければ（その選択肢がある場合に）セッションの残りの間許可する選択肢を選びます。キーバインドのリファレンスでも `confirm:cycleMode` の説明に同じ内容が入り、既定キーの表記が `Shift+Tab` から `Shift+Tab\*`（VT 入力モードが無い Windows では Meta+M）に揃えられました。あわせて、権限プロンプトが 1 回限りの承認しか出さない条件も書き直され、起動ディレクトリが長すぎてラベルに収まらない場合はホームディレクトリを `~` に、末尾を `…` に縮めて選択肢を残す（保存されるルールは同じ）ことと、それでも省く 3 つの場合が箇条書きになりました。

- [Configure permissions - Claude Code Docs (English)](https://code.claude.com/docs/en/permissions#add-a-comment-when-you-answer-a-permission-prompt)
- [Interactive mode - Claude Code Docs (English)](https://code.claude.com/docs/en/interactive-mode#general-controls)

## 3. MCP クライアントランタイム v2 への切り替え

MCP のページに **MCP client runtimes** が新設されました。Claude Code は 2 つのクライアントランタイムのどちらかで MCP サーバーにつなぎます。v1 は MCP TypeScript SDK 1.x 上に、v2 は同じコードを MCP TypeScript SDK 2.0 に載せたもので、こちらは MCP のプロトコル改定 `2026-07-28` に対応します。v2.1.232 以降は v2 が使われ、ランタイムは起動ごとに 1 度決めて終了まで変わりません。v1 になるのは、Amazon Bedrock・Claude Platform on AWS・Google Cloud の Agent Platform・Microsoft Foundry で動かしている場合（ホストプラットフォームが `CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST` を設定している場合を除く）、Claude apps gateway 経由でサインインしている場合、フィーチャーフラグの取得を切っている場合の 3 つです。v2 では、HTTP・claude.ai コネクタ・stdio のサーバーに新しい改定に対応しているかを尋ね、対応していればそれを使います。それ以外のサーバーは v1 と同じ接続です。新しい改定でつないだチャネルサーバーはチャネルのメッセージを運べないため、チャネルとして登録されません。MCP の OAuth サインインで認可応答の issuer が想定と違えば失敗させます。自分でランタイムを選ぶには `MCP_SDK_GENERATION` に `v1` / `v2` を、打診の有無は `MCP_PROTOCOL_NEGOTIATION` に `auto` / `legacy` を設定します。既定で v1 になる環境では `v2` を固定しても打診は始まらないため、`auto` も併せて設定する必要があります。

`list_changed` の受け取り方も **Notification streams on the v2 runtime** として分けて書かれました。v2 では、新しい改定のサーバーからの `list_changed` を、開いたままにしたストリームで受け取ります。ストリームが閉じたら開き直しますが、上限が 2 つあります。10 秒以内にまた閉じる場合は 3 回まで開き直してその接続では諦め、10 秒より長く開いてから閉じる場合（サーバーレスのホストでよくある形）は 1 時間に 5 回開き直した後、次まで約 6 時間待ちます。開き直すまでは、そのサーバーの最後に取得したツール・プロンプト・リソースがそのまま使われます。早く反映したい場合は `/mcp` からサーバーを再接続します。なお Claude Code on the web のセッションでは、`MCP_PROTOCOL_NEGOTIATION` を `auto` にしたときだけ MCP コネクタに打診します。Anthropic 側のフィーチャーフラグで、特定のサーバーだけ以前のプロトコルに留めたりストリームから外したりもできます。

- [Connect Claude Code to tools via MCP - Claude Code Docs (English)](https://code.claude.com/docs/en/mcp#mcp-client-runtimes)
- [Connect Claude Code to tools via MCP - Claude Code Docs (English)](https://code.claude.com/docs/en/mcp#notification-streams-on-the-v2-runtime)

## 4. headersHelper はトラスト済みフォルダでしか動かない

MCP の動的ヘッダーの節が 3 つの小節に分割され、v2.1.238 での挙動変更がまとまりました。**Trust a folder before its headersHelper runs** が中心です。`headersHelper` は任意のシェルコマンドを実行するため、プロジェクトの `.mcp.json` やローカルスコープのサーバーについては、セッションを開始したフォルダのトラストダイアログを受け入れるまで実行されなくなりました。v2.1.238 より前は、`claude -p` や SDK のセッションはトラストを確かめずに実行し、対話セッションは親フォルダをトラストしていれば実行していました。数え方も明記され、親フォルダのトラストと、`claude -p` / SDK のセッションが設定ファイルのフックのために自動で得るトラストは、いずれも数に入りません。トラストするまでは静的な `headers` だけでサーバーにつなぎ、`claude -p` や SDK のセッションではサーバーごとに 1 行 [`headersHelper not run`](https://code.claude.com/docs/en/errors#headershelper-not-run) を標準エラーに出します。ダイアログを出さずにトラストするには、`~/.claude.json` の `projects["<path>"].hasTrustDialogAccepted` を `true` にします。同じ規則はサブエージェントのファイルにインラインで宣言したサーバーにも適用され、そのフォルダをトラストするまではサーバー自体が読み込まれないため、ヘルパーも動きません。

残る 2 小節は実行環境の話です。**Where the helper runs** では、`headersHelper` の作業ディレクトリがサーバーを宣言した設定によって決まり、セッション中に `cd` しても動かないことが表で整理されました。プラグインならプラグインのルート、プロジェクトの `.mcp.json` / ローカルスコープ / プロジェクト内のエージェントファイル / SDK の `mcpServers` / `--mcp-config` なら Claude Code を起動したディレクトリ、ユーザースコープ / 管理 MCP / claude.ai コネクタ / プロジェクト外のエージェントファイルなら設定ディレクトリ（既定は `~/.claude`）です。v2.1.238 より前は、後者の 3 つ目のグループも起動したディレクトリで動いていました。**Which variables a helper can read** では、自分で書いていないヘルパー、つまりプロジェクトの `.mcp.json`・プラグイン・プロジェクトや `--add-dir` のエージェントファイル由来のヘルパーには、環境から資格情報らしい変数を渡さないことが書かれました。Git の `GIT_CONFIG_KEY_<n>` を除き、名前をアンダースコアで区切った要素に `TOKEN`・`SECRET`・`PASSWORD`・`PASSWD`・`PASSPHRASE`・`KEY`・`AUTH`・`COOKIE`・`PAT`・`DSN`・`CREDENTIAL`・`CREDENTIALS` のいずれかを含む変数（大文字小文字を問わず）はすべて除かれ、`ANTHROPIC_CUSTOM_HEADERS` のようにこの形に合わない資格情報変数も固定の一覧で除かれます。サーバーの `url` がこれらの変数を展開している場合、ヘルパーが受け取る `CLAUDE_CODE_MCP_SERVER_URL` の該当部分は `REDACTED` に置き換わります。

- [Connect Claude Code to tools via MCP - Claude Code Docs (English)](https://code.claude.com/docs/en/mcp#trust-a-folder-before-its-headershelper-runs)
- [Error reference - Claude Code Docs (English)](https://code.claude.com/docs/en/errors#headershelper-not-run)

## 5. 別セッションがアイドルになったら 1 度だけ知らせてもらう

クロスセッションメッセージのページに **Get a notice when another session goes idle** が新設されました。同じマシンの自分のセッションに対して、そのセッションが次にアイドルへ入るか終了したときに 1 度だけ通知を返すよう頼めます。ここでのアイドルは「ターンが終わり、キューに何も残っていない状態」です。両方のセッションで Claude Code v2.1.236 以降が必要です。頼み方は待っている対象を伝えるだけで、Claude は `SendMessage` ツールの `notify_when_idle` 入力で購読します。ついでに送るメッセージに付ける形でも、単独でも購読でき、単独の場合は見張る側のセッションでターンを開始せずトークンも使いません。そのセッションが既にアイドルならすぐ通知が返ります。メッセージに付けた場合はメッセージを先に届け、通知は後から返ります。見張られる側には「別のプロセスが、次にアイドルになったら知らせるよう頼んだ」旨の行が出て、頼んだ側には見張っている相手を名指しした通知の行が出ます。この行には、相手のターンが終わった時刻と、そのターンの 1 行の状況が入ることがあります。頼んだ側がアイドルなら、その通知で新しいターンが始まります。

制限も整理されました。通知は 1 回限りで、どちらのセッションもポーリングはしません。12 時間以内に通知が来なければ購読を落とし、Claude に伝えるので待ち続けません。受信制御は通知にもメッセージと同じように効きます。どちらかが `refuse` なら何も届かず（見張られる側は記録も応答もせずに要求を捨てるため、購読は 12 時間後に無応答のまま期限切れになります。頼む側が `refuse` ならそもそも購読しません）、どちらかが `hold` なら通知は内容を減らして届きます（見張られる側は 1 行の状況を省き、頼んだ側は Claude に渡さずトランスクリプトに出すだけです）。購読できるのはメインの会話の Claude だけで、相手も同じマシンの自分のセッションに限られます。サブエージェントやエージェントチームのチームメイトが `notify_when_idle` を付けた場合、Claude Code は購読せずにその旨を伝えます。それ以外の相手（チームメイト・サブエージェント・このマシンの外のセッション）に通知を求めた場合は、付随するメッセージも含めて呼び出し全体を拒否し、その旨を Claude に報告するので、要求を外して送り直せます。

- [Message your other Claude Code sessions - Claude Code Docs (English)](https://code.claude.com/docs/en/cross-session-messaging#get-a-notice-when-another-session-goes-idle)
- [Tools reference - Claude Code Docs (English)](https://code.claude.com/docs/en/tools-reference)

## 新規追加されたページ

<!-- light:new-pages:start -->
（今回の対象期間に新規追加されたページはありません。削除されたページもなく、`llms.txt` の差分は Agent SDK の Todo 追跡ページのタイトルと説明が変わった 1 行だけでした）
<!-- light:new-pages:end -->

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
- [**Agent SDK の Todo 追跡ページの全面改稿**](#1-agent-sdk-の-todo-追跡ページの全面改稿) ([English](https://code.claude.com/docs/en/agent-sdk/todo-tracking#model-availability)):  
  追加 218 行・削除 193 行で今回最大の差分。ページ名が「Todo Lists」から「Track todos」に変わり、`TodoWrite` からの移行節が消えて Task ツール前提の解説に一本化された。
- [**MCP**](#2-mcp) ([English](https://code.claude.com/docs/en/mcp#server-status-detail)):  
  追加 80 行・削除 17 行。クライアントランタイム v2 と `headersHelper` の 2 つの新設群（ハイライト 3・4 参照）に加え、ディスカバリキャッシュが既定オフに変わった。
- [**ツールリファレンス**](#3-ツールリファレンス) ([English](https://code.claude.com/docs/en/tools-reference)):  
  追加 46 行・削除 46 行。ただし内容が変わったのは `SendMessage` の行だけで、残りはツール表の桁揃えの引き直し。
- [**エラーリファレンス**](#4-エラーリファレンス) ([English](https://code.claude.com/docs/en/errors#the-proxy-refused-the-connection)):  
  追加 82 行・削除 5 行。プロキシが接続を拒否した場合と、セッションをホストするアプリがサインアウト・アカウント切り替えした場合の節が新設された。
- [**Agent SDK の MCP**](#5-agent-sdk-の-mcp) ([English](https://code.claude.com/docs/en/agent-sdk/mcp#httpsse-servers)):  
  追加 29 行・削除 50 行。HTTP / SSE サーバーの例からタブ切り替えが外れ、`.mcp.json` の書き方は同ページ内の別節へ委ねる形に整理された。
- [**セルフホスト環境リファレンス**](#6-セルフホスト環境リファレンス) ([English](https://code.claude.com/docs/en/self-hosted-environments-reference#runner-cli-flags)):  
  追加 33 行・削除 30 行。v2.1.238 の新フラグ 3 つが CLI フラグ表に加わり、既存のドレイン系フラグの説明もそれに合わせて書き直された。
- [**セルフホスト環境のデプロイ**](#7-セルフホスト環境のデプロイ) ([English](https://code.claude.com/docs/en/self-hosted-environments-deploy#defer-the-drain-past-the-first-signal)):  
  追加 54 行・削除 3 行。最初のシグナルでドレインせず稼働を続ける設定と、送出プロキシへの認証の 2 節が新設された。
- [**キーボードショートカットのカスタマイズ**](#8-キーボードショートカットのカスタマイズ) ([English](https://code.claude.com/docs/en/keybindings#chat-actions)):  
  追加 29 行・削除 27 行。`Ctrl+L` / `Cmd+K` の二度押しによる `/clear` が廃止され、`confirm:cycleMode` にコメント欄との関係が加わった。
- [**権限の設定**](#9-権限の設定) ([English](https://code.claude.com/docs/en/permissions#when-your-local-settings-file-needs-trust)):  
  追加 43 行・削除 11 行。権限プロンプトのコメント欄（ハイライト 2 参照）に加え、`settings.local.json` のトラスト判定とトラスト前の挙動の表が書き直された。
<!-- light:updated-pages:end -->

## 1. Agent SDK の Todo 追跡ページの全面改稿

追加 218 行・削除 193 行。ページ名が **Todo Lists** から **Track todos** に変わり、説明文も「Agent SDK のセッションで Todo を追跡し、構造化されたツール呼び出しからアプリケーション側で Claude の進捗を描画する」に書き換えられました。`llms.txt` に差分が出たのもこの 1 行です。冒頭の位置づけも変わり、**Model availability** に挙げたモデルでは Claude が書き出した Todo リスト無しで複数ステップの作業をこなすため、Claude Code は既定でタスク追跡ツールをセッションに入れない、まずこのページの内容は要らない、という書き出しになりました。セッションをオプトインするのは、アプリケーションがそのツール呼び出しを読んでタスクの記録を取るか、独自の進捗表示を描くときだけです。

構成では **Migrate to Task tools** の節が丸ごと消えました。`TodoWrite` と Task ツールを対比する表と、移行の最小差分を示す例が載っていた節で、`agent-sdk/typescript`・`agent-sdk/python`・`env-vars` からこの節へ張られていた参照も同時に外れています。代わりに、残った 2 つの例が Task ツール前提で書き直され、見出しも **Monitor todo changes** / **Display progress in real time** に改められました。両例に共通の前提として、実際にファイルを編集させるプロンプトなので `permissionMode: "acceptEdits"`（Python は `permission_mode`）を置くこと、ターン上限に達した場合の結果メッセージは `error_max_turns` サブタイプになること、単発の `query()` はその結果を返した後にエラーを投げるのでループを try で囲むことが、箇条書きで前置きされました。前者の例には、`+` の行に ID が入らないため更新と作成を突き合わせられないという但し書きが付き、後者の例には、`TaskCreate` の入力に割り当て済みの ID が無く、`tool_result` を運ぶユーザーメッセージの `tool_use_result` から `task.id` を読む必要がある（TypeScript では `TaskCreateOutput` として文書化されている）ことが説明されています。`Related documentation` も 4 項目に整理され、各リンクに何が書かれているかの説明が付きました。

- [Track todos - Claude Code Docs (English)](https://code.claude.com/docs/en/agent-sdk/todo-tracking#model-availability)
- [Track todos - Claude Code Docs (English)](https://code.claude.com/docs/en/agent-sdk/todo-tracking#display-progress-in-real-time)

## 2. MCP

追加 80 行・削除 17 行。新設された **MCP client runtimes** と **Notification streams on the v2 runtime** はハイライト 3、`headersHelper` の 3 小節はハイライト 4 のとおりです。ここではもう 1 つの変更、ディスカバリキャッシュの扱いを扱います。

**Server status detail** が書き足され、リモートの HTTP / SSE サーバーに出る `cached` ステータスの説明が「前のセッションで保存したディスカバリキャッシュから読んだ」と明示されました。そのうえで、キャッシュは**既定でオフ**になり、段階的なロールアウトでアカウントに有効化されている場合だけ効くことが加わっています。自分で入れるには `MCP_DISCOVERY_CACHE=1`、ロールアウトで有効になっていても切りたければ `0` です。v2.1.238 より前は既定でオンでした。あわせて、`/mcp` のサーバーメニューの 2 つの操作がキャッシュエントリに与える影響も整理されました。**Reconnect** は、`cached` のサーバーなら最初のツール呼び出しを待たずに今つなぎエントリは残し、接続済みや失敗しているサーバーなら再接続したうえでエントリを捨てます。**Clear authentication** は認証を取り消してエントリも捨てます。エントリを捨てた後は、キャッシュではなくサーバーからツール一覧を取り直します。

環境変数の側も同時に増えました。キャッシュエントリを再取得せずに使う秒数の `MCP_DISCOVERY_CACHE_TTL_S`（既定 900）、これを超えたエントリを捨てる上限の `MCP_DISCOVERY_CACHE_MAX_STALE_S`（既定 14400 = 4 時間、上限は 7 日）、TTL 超過後のバックグラウンド再取得が何回続けて失敗したらエントリを捨てるかの `MCP_DISCOVERY_CACHE_STRIKES`（既定 1）の 3 つです。v2.1.238 より前は `MAX_STALE` の既定が 86400（24 時間）で、どちらの値にも上限がありませんでした。ページ内では、`cached` ステータスに触れていた他の箇所のリンク先も `#managing-your-servers` から `#server-status-detail` へ張り替えられています。

- [Connect Claude Code to tools via MCP - Claude Code Docs (English)](https://code.claude.com/docs/en/mcp#server-status-detail)
- [Environment variables - Claude Code Docs (English)](https://code.claude.com/docs/en/env-vars#variables)

## 3. ツールリファレンス

追加 46 行・削除 46 行と数字の上では大きい差分ですが、内容が変わったのは 1 行だけです。ページ冒頭のツール表で `SendMessage` の説明が長くなり、その結果として表全体の桁揃えが引き直されたため、残り 44 行ほどは余白の変更にすぎません。

加わったのは `notify_when_idle` 入力の説明です（詳細はハイライト 5 参照）。Claude はこの入力で、同じマシンにある自分の別のセッションに対して、次にアイドルへ入るか終了したときに 1 度だけ知らせるよう頼めます。両方のセッションで Claude Code v2.1.236 以降が必要である旨も併記されました。

- [Tools reference - Claude Code Docs (English)](https://code.claude.com/docs/en/tools-reference)

## 4. エラーリファレンス

追加 82 行・削除 5 行。新設された節が 3 つあり、うち 1 つの `headersHelper not run` はハイライト 4 のとおりです。残る 2 つを扱います。

**The proxy refused the connection** は、`HTTPS_PROXY` などのプロキシ変数を設定した環境で Claude がアーティファクトを読むときに出るメッセージです。アーティファクトの中身は `*.frame.claudeusercontent.com` から来るため、Claude Code はまずプロキシに `CONNECT` を送ってそのホストへのトンネルを頼みます。プロキシが断ると何もホストに届かず、メッセージにはプロキシの HTTP ステータスが載ります。ステータスごとの対処も分けて書かれ、`HTTP 407` は資格情報が渡っていないのでプロキシ URL に入れる、`HTTP 403` はそのホストへのトンネルを断られているのでプロキシの管理者に許可を頼む、それ以外（`HTTP 502` など）はプロキシ側の事情なのでログを見る、ステータスの代わりに `unreadable reply` が出る場合はそのアドレスが HTTP プロキシかを確かめる、という内容です。対処としては、`curl -x http://proxy.example.com:8080 -I https://api.anthropic.com` を Claude Code を起動するシェルから試して同じように失敗するならプロキシ設定側の問題であること、アーティファクトのホストに直接届くネットワークなら `.claudeusercontent.com` を `NO_PROXY` に足すことが挙げられています。v2.1.238 より前は、断られたトンネルは汎用のネットワークエラーとして報告されていました。

**Remote Control stopped because the app running the session signed out or switched accounts** は、Claude デスクトップアプリや IDE がセッションをホストしている場合の節です。この構成では Claude Code は `/login` ではなくホストのアプリからログイントークンを受け取ります。claude.ai がそのトークンを拒否すると Claude Code はアプリに新しいトークンを求め、アプリが「サインアウト済み」または「別の Claude アカウントにサインイン中」と答えた場合に Remote Control セッションを終了して、対応する 2 行のいずれかをアプリへ送ります。サインアウトならアプリで再度サインインしてから Remote Control を入れ直し、アカウントが切り替わった場合は終了したセッションを新しいアカウントで続けられないので新しい Remote Control セッションを始める、という案内です。v2.1.238 より前は、どちらの場合もログインの更新失敗の節に載っている `run /login` のメッセージを送っていました。あわせて、そのログイン更新失敗の節も書き足され、更新要求に応答が無い間は現在の資格情報が有効なうちは再試行を続けること、期限切れまで応答が無ければ `OAuth token refresh failed` で止めること、`/logout` などで手元のサインアウトが起きた場合の `Signed out of Claude` が新しく分けられたことが加わりました。

- [Error reference - Claude Code Docs (English)](https://code.claude.com/docs/en/errors#the-proxy-refused-the-connection)
- [Error reference - Claude Code Docs (English)](https://code.claude.com/docs/en/errors#remote-control-stopped-because-the-app-running-the-session-signed-out-or-switched-accounts)

## 5. Agent SDK の MCP

追加 29 行・削除 50 行。**HTTP/SSE servers** の書き方が整理されました。これまでは「In code」と「.mcp.json」の 2 タブで同じ設定を並べていましたが、タブ構造をやめて TypeScript / Python のコード例だけを残し、`.mcp.json` の書き方は同じページの **HTTP headers for remote servers** の例と同じフィールドを使い、SSE なら `"type": "sse"` にする、という 1 文で済ませる形になりました。差分の大半はこのタブ構造の除去によるものです。

残りは参照の整理です。MCP の出力上限の節で、サーバーがツールごとに上限を宣言する手段の名前（`anthropic/maxResultSizeChars` アノテーション）が本文に書かれ、代わりに `Related resources` から MCP 出力上限へのリンク 1 項目が外れました。

- [Connect to external tools with MCP - Claude Code Docs (English)](https://code.claude.com/docs/en/agent-sdk/mcp#httpsse-servers)

## 6. セルフホスト環境リファレンス

追加 33 行・削除 30 行。CLI フラグ表に v2.1.238 の新フラグが 3 つ加わりました。`--defer-shutdown-max-min <n>`（環境変数 `SELF_HOSTED_RUNNER_DEFER_SHUTDOWN_MAX_MS`、既定 `0`）は、最初の `SIGTERM` / `SIGINT` で既に受け持っているセッションをドレインせず、その後 n 分たった時点で残っているものを手放して終了します。設定する前にホスト側の停止タイムアウトを上げるよう注意書きが付いています。`--proxy-authorization-command <command>` と `--proxy-authorization-file <path>`（同 `..._PROXY_AUTHORIZATION_COMMAND` / `..._FILE`、いずれも既定は未設定）は、送出プロキシへの接続ごとに `Proxy-Authorization` ヘッダの値をコマンドの標準出力またはファイルの内容から取ります。どちらも `HTTPS_PROXY` か `HTTP_PROXY` が必要で、併用はできません。

既存フラグの説明も、この延期を前提に書き直されました。`--drain-grace-sec` と `--release-idle-session-min` には「シャットダウンシグナルを受け取るか退役時刻に達するまでは」という限定が付き、`--defer-shutdown-max-min` で最初のシグナルを延期した後は、設定値によらずセッションを 1 つも持たなくなった時点で終了する旨が加わりました。`--drain-wait-sec` も「`SIGTERM` で」ではなく「ドレインが始まったら（`--defer-shutdown-max-min` を設定していなければそれは `SIGTERM` の時点）」という書き方に変わっています。セッション終了理由 `interrupted` の説明からは `released=false` バックストップの記述が外れ、ドレインと最大寿命ウォッチドッグの 2 つに整理されました。

- [Self-hosted environments reference - Claude Code Docs (English)](https://code.claude.com/docs/en/self-hosted-environments-reference#runner-cli-flags)

## 7. セルフホスト環境のデプロイ

追加 54 行・削除 3 行。新設が 2 節です。**Defer the drain past the first signal** は `--defer-shutdown-max-min <n>` の運用解説で、再起動するランナーに、最初のシグナルでドレインさせず受け持ちのセッションを最大 n 分そのまま担当させたい場合に使います。最初の `SIGTERM` / `SIGINT` で新しい作業の受け取りをやめ、既存のセッションは担当し続け、コントロールプレーンにそれらを再キューさせないためポーリングも続けます。シグナルからの経過は 3 段階に分かれ、最初の n 分はセッションを通常どおり処理しつつ `--startup-timeout-min` と `--kill-session-after-min` を効かせ、`--release-idle-session-min` を併用していればその時間ユーザーがアイドルなセッションを手放します。ドレイン経路の所要時間の記述にも、このフラグを設定した場合は設定した分数と解放後の猶予（既定で 75 秒）の 2 つが加算され、起動時にドレイン経路の合計に続けて合算値も表示される旨が加わりました。

**Authenticate to an egress proxy** は、接続ごとに `Proxy-Authorization` ヘッダを要求する企業の送出プロキシ向けです。トークンの回転が速すぎて `HTTPS_PROXY` の URL に書き込めない場合に、`--proxy-authorization-command`（都度生成するトークン向け・標準出力を trim して使用）か `--proxy-authorization-file`（別プロセスが同じ場所を書き換えるトークン向け・内容を trim して使用）で値の取得元を指定します。ランナーが起動を拒否する構成も 3 つ明記されました。両方のフラグを設定した場合（片方のフラグともう片方の環境変数でも該当）、`HTTPS_PROXY` / `HTTP_PROXY` のどちらにも `http://` か `https://` の URL が無い場合（大文字小文字どちらも読みますが `ALL_PROXY` は見ません）、そして `self-hosted-runner orchestrator` サブコマンドにこのフラグを渡した場合です。フラグを設定するとランナーは `127.0.0.1` に自前のフォワードプロキシを立ち上げ、`HTTPS_PROXY` / `HTTP_PROXY` をそこに向け直します。ランナー自身・ライフサイクルフック・各セッションのプロキシ通信はすべてそのリスナーを通り、リスナーがプロキシへ向かう際にヘッダを付けます。トークンの回転は再起動なしで反映され、各セッションの環境からは `ALL_PROXY` と、設定していない綴りの `HTTPS_PROXY` / `HTTP_PROXY` が除かれ、`NO_PROXY` はランナー自身の値に固定されます。ヘッダの値がログに出ることはありません。

- [Deploy self-hosted environments to production - Claude Code Docs (English)](https://code.claude.com/docs/en/self-hosted-environments-deploy#defer-the-drain-past-the-first-signal)
- [Deploy self-hosted environments to production - Claude Code Docs (English)](https://code.claude.com/docs/en/self-hosted-environments-deploy#authenticate-to-an-egress-proxy)

## 8. キーボードショートカットのカスタマイズ

追加 29 行・削除 27 行。`Chat` コンテキストの表で、`chat:clearInput`（`Ctrl+L`）と `chat:clearScreen`（`Cmd+K`）の説明から、フルスクリーンで 2 秒以内に二度押しすると `/clear` が走るという記述が消えました。どちらも「入力と会話を保ったまま全画面を描き直す」だけになり、`Cmd+K` の側には iTerm2 と Terminal.app での振る舞いについてフルスクリーンのページを参照する案内が付いています。`chat:killAgents`（`Ctrl+X Ctrl+K`）には、このセッションのバックグラウンドサブエージェントを止めるのに加えて、セッションの残りの間アーティファクトの自動返信も切る（ハイライト 1 参照）ことが加わりました。

`Confirmation` コンテキストの表では `confirm:cycleMode` の説明が増えました。ファイルの権限プロンプトでは開いているコメント欄を閉じ、欄が開いていなければ（その選択肢がある場合に）セッションの残りの間許可する選択肢を選びます（ハイライト 2 参照）。既定キーの表記も `Shift+Tab` から `Shift+Tab\*` になり、表の下に「VT モードが無い Windows（Node \<24.2.0/\<22.17.0、Bun \<1.2.23）では Meta+M が既定」という脚注が加わりました。`Chat` コンテキストの `chat:cycleMode` に既に付いていた脚注と同じものです。

- [Customize keyboard shortcuts - Claude Code Docs (English)](https://code.claude.com/docs/en/keybindings#chat-actions)
- [Customize keyboard shortcuts - Claude Code Docs (English)](https://code.claude.com/docs/en/keybindings#confirmation-actions)

## 9. 権限の設定

追加 43 行・削除 11 行。新設された **Add a comment when you answer a permission prompt** と、1 回限りの承認しか出ない条件の書き直しはハイライト 2 のとおりです。残る 2 箇所はワークスペースのトラストまわりです。

**When your local settings file needs trust** が箇条書きに組み替えられました。`.claude/settings.local.json` は通常は自分のファイルなのでトラストの手順なしに効きますが、git で追跡されている場合や `.claude` がシンボリックリンクの場合はリポジトリ由来として扱われ、フォルダをトラストするまでルールが保留されます。この判別に git を走らせること自体がトラスト後にしか行われないため、それまでは起動した場所で扱いが変わります。設定ホーム（ホームディレクトリ、または `.claude` を `CLAUDE_CONFIG_DIR` にしたディレクトリ）では git を走らせずに即座に適用されますが、その `CLAUDE_CONFIG_DIR` が git リポジトリの中にあり、ローカル設定をリポジトリルートに置く扱いになる場合は他と同じく保留されます。それ以外の場所ではプロジェクト設定と同様に保留され、判定が済んだ後は追跡されていないファイルやリポジトリ外のファイルなら、そのフォルダをトラストしていなくても適用されます。注記も新設され、この設定ホームの例外はトラストの手順を飛ばすだけであり、`~/.claude/settings.local.json` はローカルスコープのままなのでホームディレクトリで開始したセッションでしか読まれない、全プロジェクトに効かせたいならユーザー設定（`~/.claude/settings.json`）に書く、と案内されています。

**What runs before you trust a folder** の表には行が 2 つ増えました。リポジトリや `--add-dir` のサブエージェントのフロントマターにインラインで書いた `mcpServers` は、親フォルダのトラストでもダイアログでも使われません。`.mcp.json` のサーバーの `headersHelper` は、親フォルダだけをトラストしている場合はヘルパーの宣言場所を示すダイアログが再度出るまで実行されず、それまでは静的な `headers` だけで接続し、`claude -p` / SDK の場合は実行されずサーバーごとに `headersHelper not run` を標準エラーに出します（ハイライト 4 参照）。既存の `.mcp.json` の行からは `headersHelper` の記述が分離され、表の下の案内も、正確なキーがデバッグログ（サブエージェントのフックとインライン MCP サーバー）・標準エラーの警告（allow ルール）・`headersHelper not run` の行のそれぞれに出ることを列挙する形になりました。

- [Configure permissions - Claude Code Docs (English)](https://code.claude.com/docs/en/permissions#when-your-local-settings-file-needs-trust)
- [Configure permissions - Claude Code Docs (English)](https://code.claude.com/docs/en/permissions#what-runs-before-you-trust-a-folder)

## 軽微な更新

<!-- light:minor-updates:start -->
今回は 1 日分の取り込みをまとめた対象期間で、差分のあったページは 60 です。changelog には v2.1.238（2026年08月20日）の 1 リリースが加わりました。上記の大幅更新 9 ページを除く 51 ページの変更をここで扱います。なお本サマリの参考リンクは全て英語版のみです。今回変更のあったページは日本語版がまだ追従していないためで、MCP とアーティファクトの 2 ページを実際に確認したところ、いずれも新設された節が無く、旧記述のままでした。

**新機能**

- `keybindingFlavor` 設定が加わりました。`"readline"` にするとプロンプトの Ctrl+W が Bash と同じく直前の空白まで削除します。既定の `"classic"` は変わりません（v2.1.238）
- `CLAUDE_CODE_BS_AS_CTRL_BACKSPACE` が加わり、ターミナル設定のページにも Windows で Backspace が単語ごと消える場合の対処が新設されました。Windows では `^H` を Ctrl+Backspace として読むため（`TERM_PROGRAM` が `mintty`、`TERM` が `cygwin` の場合を除く）、プレーンな Backspace で `^H` を送るターミナルではこの変数を `0` にします — [English](https://code.claude.com/docs/en/terminal-config#fix-backspace-deleting-a-whole-word-on-windows)
- 組み込みの出力スタイルに **Concise** が加わったことがページ側にも記載されました。結果から述べて前置きと実況を省き、既定では短く返しますが、説明や詳細を求めれば省略せずに答え、エラー報告・セキュリティ警告・破壊的な操作の確認は常に全文を保ちます（v2.1.237）— [English](https://code.claude.com/docs/en/output-styles#built-in-output-styles)
- VS Code 拡張のスクリーンリーダー対応が新設節としてまとまりました。設定は不要で、返答（完成時に 1 度）・権限リクエストや質問・状態変化・エラーとモデル関連のプロンプトを読み上げます。ターンごとに視覚的に隠された見出しが付くため見出しナビゲーションで移動でき、`Tab` でトランスクリプトへフォーカスも移せます。セッションを開き直したときは何も読み上げません（v2.1.236）— [English](https://code.claude.com/docs/en/vs-code#use-a-screen-reader)
- `/goal` にアイドル時のチェックインが加わりました。対話セッションでは、次のプロンプトを待たずに Claude Code が自分でターンを開始してチェックインを届けます。最初のチェックインの後は待ち時間が倍々になり、間隔の 4 倍が上限です（既定なら 1 時間後、以降 2 時間ごと）。`-p` のような非対話セッションではターン終了時のみです（v2.1.236）— [English](https://code.claude.com/docs/en/goal#background-work-defers-evaluation)
- セルフホストランナーに `--defer-shutdown-max-min` と `--proxy-authorization-command` / `--proxy-authorization-file` が加わりました（v2.1.238、詳細は大幅更新 6・7 参照）— [English](https://code.claude.com/docs/en/self-hosted-environments-reference#runner-cli-flags)
- プラグインマーケットプレイスの `headersHelper` が加わりました。url マーケットプレイスやカタログエントリで、カタログと同一オリジンのアーカイブ取得用に HTTP ヘッダ（短命トークンなど）を作るコマンドを走らせます。カタログエントリの `headersHelper` はそのプラグインをインストール・更新するときだけ、コマンドを表示したうえで `[y/N]` を尋ねてから動きます（v2.1.238）
- `SDKControlInitializeResponse` に `hooks_applied` が加わりました。`initialize` リクエストが運んだ `hooks` を登録したかを示すもので、セッション最初の initialize と、CLI の標準入力経由で送った再度の initialize では `true`（後者は登録済みのフックを置き換えます）、リモートセッションへ送った再度の initialize では `false` になり、後から参加したクライアントが先のフックを置き換えられないようになっています（Agent SDK v0.3.238 以降）— [English](https://code.claude.com/docs/en/agent-sdk/typescript#sdkcontrolinitializeresponse)
- `SDKTaskStartedMessage` に `is_backgrounded` と `spawn_depth` が加わりました。前者は `"local_agent"` と `"local_bash"` のタスクに付き、フォアグラウンドで動く場合は `false`（開始したツール呼び出しはタスクが終わるかバックグラウンドへ移るまでブロックされます）。後者は `"local_agent"` のみで、メインスレッドが起動したサブエージェントが `1`、その入れ子が `2` と続きます。再開したサブエージェントは常に `is_backgrounded: true` です（Agent SDK v0.3.238 以降）— [English](https://code.claude.com/docs/en/agent-sdk/typescript#sdktaskstartedmessage)
- 環境変数の一覧に `CLAUDE_CODE_ARTIFACT_COMMENTS` と `CLAUDE_CODE_ARTIFACT_COMMENTS_AUTOREACT` が加わりました（v2.1.221 / v2.1.228、詳細はハイライト 1 参照）— [English](https://code.claude.com/docs/en/env-vars#variables)
- 環境変数の一覧に `MCP_PROTOCOL_NEGOTIATION` が新設され、`MCP_SDK_GENERATION` の説明も v1 / v2 の実体を明記する形に書き直されました。フィーチャーフラグの取得が要る機能の一覧にも、v2 ランタイムとプロトコル打診の項目が加わっています（詳細はハイライト 3 参照）— [English](https://code.claude.com/docs/en/env-vars#features-that-need-feature-flag-fetching)
- 環境変数の一覧にディスカバリキャッシュの `MCP_DISCOVERY_CACHE_TTL_S`・`MCP_DISCOVERY_CACHE_MAX_STALE_S`・`MCP_DISCOVERY_CACHE_STRIKES` の 3 つが加わりました（v2.1.238、詳細は大幅更新 2 参照）— [English](https://code.claude.com/docs/en/env-vars#variables)

**機能改善**

- フルスクリーンで `Ctrl+L` / `Cmd+K` を 2 秒以内に二度押ししても `/clear` が走らなくなりました。会話を消すには `/clear` を実行します。iTerm2 と Terminal.app では `Cmd+K` をターミナル自身が処理して画面を消しますが、Claude Code はそれを検知して会話を描き直します（v2.1.238、詳細は大幅更新 8 参照）— [English](https://code.claude.com/docs/en/fullscreen#clear-the-conversation)
- フルスクリーンの起動に失敗した場合の節が新設されました。最初のフレームを描いた後 10 秒持ちこたえるか `/exit`・Ctrl+C・Ctrl+D で終えれば「起動成功」で、そこに至る前にクラッシュすると次のセッションは従来のレンダラーで始まり、1 回目と 2 回目で別のメッセージが出ます。2 回目以降は Claude Code を更新するか `/tui fullscreen` を実行するまで従来のレンダラーのままです。失敗回数は Claude Code のバージョンごとに数え、成功でリセットされます。`CLAUDE_CODE_NO_FLICKER=1` を設定したセッションは失敗後もフルスクリーンで描かれ、回数にも数えません（v2.1.236）— [English](https://code.claude.com/docs/en/fullscreen#fullscreen-renderer-didnt-finish-starting)
- `/tui fullscreen` の再起動が引き継ぐものに `--agent`・`--agents`・`--append-system-prompt` が加わりました。起動時のダイアログを受け入れた場合の `tui` 設定の保存も、再起動したセッションが起動に成功してからになりました — [English](https://code.claude.com/docs/en/fullscreen#enable-fullscreen-rendering)
- `/model` でモデルを切り替えるときの確認ダイアログが、キャッシュがまだ生きているときだけ出るようになりました。会話で最後にリクエストを送ったか Claude が応答してからキャッシュ TTL 未満なら確認し、TTL 以上たっていれば確認せずに切り替えます。エフォートの変更も同じ確認に従い、既に有効な水準に解決される変更ではキャッシュを保ったまま確認なしで適用されます。v2.1.238 より前は TTL を見ずに、キャッシュが切れていても確認していました（v2.1.238）— [English](https://code.claude.com/docs/en/prompt-caching#switching-models)
- プロンプト候補が出ない条件に「アカウントが利用上限に近いか達している」が加わりました。上限に達するまで出し続けたい場合は `CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION` を `true` にします。v2.1.238 より前は、この変数を `true` にしていても上限付近では候補を出しませんでした（v2.1.238）— [English](https://code.claude.com/docs/en/interactive-mode#when-claude-code-skips-suggestions)
- サンドボックスの重なりの表に、ワイルドカードの `denyRead`（`~/**/.env` など）が広い `allowRead` の内側でも維持される行が加わりました。設定のページ側でも、ワイルドカードが一致したディレクトリの中身も読めなくなること、v2.1.236 より前の macOS では広い `allowRead` に覆われた場所で再開放されていたことが明記されています（v2.1.236）— [English](https://code.claude.com/docs/en/sandboxing#configure-sandboxing)
- `policyHelper` が他の管理設定を置き換える条件が 6 ページにわたって書き直されました。従来は「`policyHelper` が設定されていれば管理ソースをすべて置き換える」でしたが、「管理階層の優先順位で勝ったソースが MDM またはファイルベースで、それが `policyHelper` を設定している場合に、ヘルパーの出力がそのソースを置き換える」に変わりました。サーバー管理設定が空でない構成を配っている間は、MDM やファイルの `policyHelper` は動きません。設定・サーバー管理設定・Claude apps gateway とその構成リファレンス・組織向けセットアップ・Agent SDK の `managedSettings` の各記述がこれに合わせて直っています — [English](https://code.claude.com/docs/en/settings#precedence-within-the-managed-tier)
- `--bare`（`CLAUDE_CODE_SIMPLE`）が自動検出を飛ばす対象に、カスタムコマンドとサブエージェントが明記されました。一方で `--add-dir` で渡したディレクトリの `.claude/skills/` のスキルは読み込まれる（`.claude/commands/` と `.claude/agents/` は飛ばす）という例外も加わっています — [English](https://code.claude.com/docs/en/headless#start-faster-with-bare-mode)
- `claude -p` を SIGTERM で止めたときの挙動が独立した節になり、内容も精密になりました。進行中のターンは中断されず結果も記録されないため、走っていたコマンドは kill 済みとして、回答待ちの権限プロンプトは未回答として記録され、終了処理が始まった後は `SessionEnd` 以外のツール・モデルリクエスト・フックは開始されません。セッションを再開するとその地点から続きます。SDK ホストがセッションを閉じる場合は入力を先に閉じるためシグナルの前に待機中のプロンプトが取り消されます。ターンをきれいに終えたい場合は、プロセスを止める前に SIGINT（SDK なら `interrupt()`）を送ります — [English](https://code.claude.com/docs/en/headless#stop-a-run-with-sigterm)
- Hooks リファレンスと worktree のページの双方に、worktree に入った後の `${CLAUDE_PROJECT_DIR}` の扱いが注記として加わりました。この変数はセッションを開始したプロジェクトルートを指したまま動かず、Claude が今いるディレクトリはフック入力 JSON の `cwd` から読みます（`cd` にも追随します）— [English](https://code.claude.com/docs/en/hooks#reference-scripts-by-path)
- クロスセッションメッセージで、受信側が拒否・ドロップしたときに送信側へ伝わるようになりました。受信側が `refuse` の場合は「クロスセッションメッセージを受け付けていない」という通知が出て、待つな・送り直すなと送信側の Claude に伝えられます。レート制限・重複判定・キュー上限（1 セッションあたり 50 件）でメッセージが落ちた場合も、どれが落としたかが送信側に伝わります（v2.1.238）— [English](https://code.claude.com/docs/en/cross-session-messaging#control-inbound-messages)
- クロスセッションの一覧に、エージェントビューのスーパーバイザプロセスが次のバックグラウンドセッション用に温めているワーカーが、作業を割り当てた後にだけ現れる旨が加わりました — [English](https://code.claude.com/docs/en/cross-session-messaging#see-which-sessions-claude-can-reach)
- Remote Control で接続したデバイスからできることが増えました。バックグラウンドで動いているサブエージェントやワークフローをデバイスから止めると手元のマシンでも止まり、ターンの途中で送ったプロンプトはキューに入りターン終了後もデバイスのトランスクリプトに残ります。デバイスからモデルを選ぶとセッションがそのモデルで動き、ターミナルの `/model`・`/status`・`/config` にも反映されます（デバイスのモデルコントロールからの選択は現在のセッション限り、`/model <name>` を送った場合は新規セッションの既定にもなります）。`claude remote-control` が提供するセッションがクラッシュしても、デバイスからメッセージを送れば提供し直されます。接続後の HTTP 403 は最大 3 分再試行し、それ以上続く場合は何が拒否したか（ネットワークエッジか、自分のネットワークのプロキシ・VPN・ファイアウォールか）を示して切断します（v2.1.238）— [English](https://code.claude.com/docs/en/remote-control#what-connected-devices-see)
- Remote Control が「研究プレビュー」ではなく全プラン提供として書かれ、`Remote Control is not yet enabled for your account` のエラーが `Remote Control isn't enabled for this account` に改称されました（v2.1.239 で改称）。原因の説明も「ロールアウトが届いていない」から「アカウントレベルの可用性チェックがオフを返した。よくある原因はプラン変更後の古いキャッシュ」に変わり、`claude auth logout` / `login` に加えて古いバージョンなら更新するよう案内が付いています — [English](https://code.claude.com/docs/en/remote-control#remote-control-isnt-enabled-for-this-account)
- サブエージェントのページに、エージェントファイルのインライン MCP サーバーがフォルダのトラストを要する旨が加わりました。プロジェクトや `--add-dir` の `.claude/agents/` にあるファイルのインラインサーバーは、そのフォルダをトラストするまで読み込まれず、`~/.claude.json` に書くべきキーがデバッグログに出ます。名前で既存サーバーを参照する場合や、`~/.claude/agents/`・`--agents`・SDK の `agents` オプション・管理設定由来のエージェントファイルは対象外です（v2.1.238、詳細はハイライト 4 参照）— [English](https://code.claude.com/docs/en/sub-agents#scope-mcp-servers-to-a-subagent)
- `claude plugin validate` の節が 4 つの小節（指定するディレクトリの選び方 / ルートの `SKILL.md` を持つプラグイン / シンボリックリンクの先 / 検証結果の読み方）に再編されました。内容は前回の対象期間に入ったものと同じで、読み進めやすさのための再構成です — [English](https://code.claude.com/docs/en/plugin-marketplaces#validate-a-plugin-or-a-directory-without-a-manifest)
- Agent SDK のサブエージェントのページで、利点を並べた 4 つの h3 が 1 つの箇条書きにまとめられ、あわせてフォークしたサブエージェントの場合はコンテキストが新規に始まるわけではない旨が加わりました — [English](https://code.claude.com/docs/en/agent-sdk/subagents#benefits-of-using-subagents)
- `REVIEW.md` の効き方の説明が書き直されました。従来の「全エージェントのシステムプロンプトに最優先で注入される」から、「検出・検証を行うエージェントがリポジトリのレビュー指示として受け取り、順位付けと報告を行うエージェントは重大度を決めてレビューを書く前に参照する」という書き方になっています。あわせて関連リンクに Anthropic のセキュア開発ライフサイクルの記事が加わりました — [English](https://code.claude.com/docs/en/code-review#reviewmd)
- 用語集の 3 項目が更新されました。auto モードの分類器は「ツール結果を一切見ない」から「ツール結果を取り除いた状態で見る」に、`--bare` は上記の対象追加に、出力スタイルはカスタムスタイルが `keep-coding-instructions: true` を設定しない限り組み込みのソフトウェアエンジニアリング指示を外すこと・組み込みスタイルに Concise が加わったことに、それぞれ直っています — [English](https://code.claude.com/docs/en/glossary#output-style)
- コマンド一覧とモデル設定のページで、`/model` の確認に関する記述がプロンプトキャッシュのページへの参照に置き換えられました。`/run`・`/run-skill-generator`・`/verify` からは v2.1.145 以降が必要という注記が外れています — [English](https://code.claude.com/docs/en/model-config#setting-your-model)
- Amazon Bedrock と Google Cloud の Agent Platform のページに、`ANTHROPIC_DEFAULT_MODEL` でセッションを開始した場合はバックグラウンドタスクもそのモデルを使う旨が加わりました — [English](https://code.claude.com/docs/en/amazon-bedrock#4-pin-model-versions)
- セルフホスト環境の概要とライフサイクル設定にも v2.1.238 の変更が反映されました。ポーリング要求は 10 秒でタイムアウトし、失われた場合は 1〜2 秒後に再試行して以降は最大 20 秒まで間隔を倍にする（リースの期限が近いときは短縮する）ことと、`post-session` フックがセッション解放の前に走るか後に走るかがターンの状態で決まること（v2.1.236 以降）が加わっています — [English](https://code.claude.com/docs/en/self-hosted-environments-configuration#post-session)
- デスクトップアプリの受信制御で、拒否した場合にその旨が Claude デスクトップアプリへ報告されるようになりました — [English](https://code.claude.com/docs/en/desktop#work-across-sessions)
- ルーティンとデスクトップの定期タスクのページで、サイドバーの **Routines** に至る導線が「デスクトップアプリの **Code** タブで」と明示されました — [English](https://code.claude.com/docs/en/routines#create-a-routine)
- Agent SDK の `promptSuggestions` オプションと `prompt_suggestion` メッセージの説明に、ターンによっては候補が生成されないこと（利用上限付近など）と、その条件を示すページへの参照が加わりました — [English](https://code.claude.com/docs/en/agent-sdk/typescript#options)
- Agent SDK の `task_started` の説明から「バックグラウンドの」という限定が外れ、フォアグラウンドのタスクでも発行されることが読み取れるようになりました — [English](https://code.claude.com/docs/en/agent-sdk/typescript#sdktaskstartedmessage)
- Agent SDK の Hooks のページで、MCP ツール名の付き方（`mcp__<server>__<action>` の `<server>` は `mcpServers` 設定のキー）の説明が Tip から `matcher` の表と本文に移されました — [English](https://code.claude.com/docs/en/agent-sdk/hooks#matchers)
- プラグインのヒントで、インストールを促すプロンプトを出すのはユーザーが打ち込んでいるメインの対話セッションだけであることが明記されました。サブエージェントのコマンドや `-p` / Agent SDK では出ませんが、コマンド出力からヒント行を取り除く処理はいずれの場合も行われます — [English](https://code.claude.com/docs/en/plugin-hints#what-the-user-sees)
- コスト管理のページに、ゴールのアイドル時チェックインが（セッションが待機していてもターンを開始してコンテキスト全文を送るため）コストに効く旨と、`CLAUDE_CODE_GOAL_CHECKIN_MINUTES=0` で切れることが加わりました（v2.1.236）— [English](https://code.claude.com/docs/en/costs#background-token-usage)
- スクリーンリーダーのページに、スクリーンリーダーモードはターミナルの UI にだけ効くもので VS Code 拡張のチャットパネルでは不要である旨が加わりました — [English](https://code.claude.com/docs/en/accessibility#turn-on-screen-reader-mode)
- ディープリンクのページで、GitHub がカスタム URL スキームを剥がす話が冒頭の注記からトラブルシューティングの節への参照 1 文に集約されました — [English](https://code.claude.com/docs/en/deep-links#the-link-renders-as-plain-text-instead-of-being-clickable)
- アーティファクトの共有で、作成者名が誰に見えるかが整理されました。組織内で共有したアーティファクトではタイトルメニューに、公開したアーティファクトではサインイン済みの同じ組織のビューアに対してページヘッダーに名前が出ます。サインインせずに公開リンクを開いた場合や組織外のビューアには、名前の代わりに `Content is user-generated and unverified.` というラベルが表示されます — [English](https://code.claude.com/docs/en/artifacts#share-an-artifact)
- 起動時のパフォーマンスが改善され、素の `claude` が macOS でより早く起動するようになりました（v2.1.238）
- シェルの条件式に含まれる zsh 固有の構文について、Bash ツールの権限チェックが改善されました（v2.1.238）
- 自動更新チェックが起動から約 10 秒後に走るようになり、起動時の CPU を奪わなくなりました（v2.1.238）
- 同梱の `claude-api` スキルが、Managed Agents の 8 月 19 日リリース（ウェブ検索・取得のドメイン設定、セルフホストサンドボックスのメモリストア）に合わせて更新されました（v2.1.238）
- `claude mcp list` と `claude mcp get` が、無効化されたサーバーにヘルスチェックのために接続せず `⊘ Disabled` と表示するようになりました（v2.1.238）

**バグ修正**

以下は v2.1.238（2026年08月20日）の changelog に `Fixed` として載った修正です。

- 長い対話セッションでメモリが際限なく増える問題を修正し、表示ウィンドウから外れたサブエージェントのツール結果を解放するようにした
- カスタム・プロジェクト・プラグインの出力スタイルが、セッションの途中で既定の文体に戻ってしまう問題を修正
- `CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION=true` が、アカウントが利用上限の手前（超過はしていない）にあるときにプロンプト候補を保てない問題を修正
- worktree の隔離による Bash の拒否が、リダイレクトの無いコマンドに対して「リダイレクトを外せ」と告げる問題を修正
- セルフホストランナーが、遅い／失われたポーリング要求 1 回でサーバーから除去され、正常なセッションが別のランナーへ渡ってしまう問題を修正
- MCP のエリシテーションダイアログが 4,096 文字を超える URL で何も表示しない問題と、権限プロンプトがプロジェクトパスの幅に収まらないときに「今後は聞かない」の選択肢を落とす問題を修正
- Bash コマンドが kill・タイムアウト・中断されたときに `/tmp/claude-*-cwd` が残る問題を修正
- Backspace として Ctrl+H を送るターミナルで、キー入力がまとめて届く（遅い SSH / mosh 回線）と Backspace の長押しが無視される問題を修正
- 権限プロンプトの差分表示で、絵文字のような複数コードポイントの文字やタブを含む行が切れてしまう折り返しの問題を修正
- Ctrl+Z でサスペンドしたセッションを kill すると、ターミナルがブラケットペーストモードのままカーソルが隠れた状態になることがある問題を修正
- stdio の MCP サーバーが `initialize` の前に `server/discover` を受け取り、遅延起動のサーバーがセッションを開くたびにバックエンドを起動させられる問題を修正
- プロキシによる接続拒否が、プロキシを名指しせず汎用のネットワークエラーとして報告される問題を修正（詳細は大幅更新 4 参照）
- `/model` と `/effort` のキャッシュミス警告が、プロンプトキャッシュが既に切れているときにも出る問題を修正
- Remote Control のタスクパネルからのタスク単位の Stop が、CLI がホストするセッションで何も起きない問題を修正
- クライアントが有効な role の無いユーザーメッセージを渡したときにリモートセッションが終了する問題を修正
- `claude remote-control` で開始した Remote Control セッションが、起動したシェルのセッションスコープの環境変数を引き継いでしまう問題を修正
- プロセスがクラッシュした Remote Control セッションが、`claude remote-control` を再起動するまで使えないままになる問題を修正（次にメッセージを送れば再利用できるようになった）
- ターンの途中に web やデスクトップから送った Remote Control のメッセージが、ターン終了後にトランスクリプトから消える問題を修正
- 電話や web で選んだ Remote Control のモデルが、ターミナル側の表示に反映されない問題を修正
- 短いネットワークの不調でサインインの更新が遅れたときに、Remote Control が「login expired」で切断する問題を修正（再試行して接続を保つようになった）
- サインアウト時に Remote Control が再接続の失敗を報告する問題を修正（サインアウトで明確なメッセージとともにセッションを終えるようになった）
- `claude remote-control`（サーバーモード）やデスクトップ／IDE がホストするセッションで、`ListAgents` / `SendMessage` が「Remote Control is not connected」と報告する問題を修正
- `ListAgents` と `SendMessage` が、エージェントビューが次のバックグラウンドセッション用に温めているアイドルワーカーを露出させる問題を修正（タスクが割り当てられてから現れるようになった）

**その他**

- `llms.txt` の差分は 1 行だけで、Agent SDK の Todo 追跡ページのタイトルが「Todo Lists」から「Track todos」に、説明も新しいものに変わりました（詳細は大幅更新 1 参照）
- ページ見出しマップには、今回の `llms-full.txt` にはまだ現れていない見出しが 2 つあります。インタラクティブモードの **Make Ctrl+W delete back to whitespace**（`keybindingFlavor` の解説と思われます）と、Hooks リファレンスの PostToolUse 配下の **Annotate a result for the auto mode classifier** です。次回以降の取り込みで本文が入る見込みです
- Agent SDK のカスタムツール・ファイルチェックポイント・ワークフローの 3 ページで、内容の重複していた末尾の節（関連ドキュメントの箇条書き、チェックポイントが追跡する対象の再掲、`/workflows` のコードブロック）が削除されました
- スキルのページ冒頭から、スキルのディレクトリ構成を示すツリーと `SKILL.md` の説明が削除され、同ページ内の **Add supporting files** への参照に置き換えられました — [English](https://code.claude.com/docs/en/skills#add-supporting-files)
- 認証・LLM ゲートウェイの接続とロールアウトの 3 ページ、およびセキュリティガイダンスから、`v2.1.146` / `v2.1.144` 以降という古いバージョン条件の注記が削除されました — [English](https://code.claude.com/docs/en/llm-gateway-rollout#distribute-through-managed-settings)
<!-- light:minor-updates:end -->

## 新着情報

<!-- light:whats-new:start -->
（今回の対象期間に更新された新着情報ページはありません。前回に続き Week 32 が最新のままです）
<!-- light:whats-new:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-08-19.md](./archives/latest/2026-08-19.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-08-19.md](./archives/latest-detail/2026-08-19.md)

<!--
base_commit: a4f51fbfe83670c58f484e3fb81935316a500138
head_commit: 374b2af0b3a3dbc0f997d926da13c0fbf25fa843
generated_at_full: 2026-08-21T15:10:21+09:00
-->
