---
対象期間: 2026年10月09日 〜 2026年10月10日
作成日: 2026-10-10
---

# Claude Code 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
**今回は、auto モードの分類器の料金の通知を説明する新しいページ、ネットワークパスからの読み取りに入った専用の権限の確認、Agent SDK のセッションを分岐する `forkSession()`・`fork_session()`、Read ツールの大きなファイルの読み取りと UTF-8 でないファイルの扱い、デスクトップアプリの SSH セッションの worktree の置き場所が文書に加わりました。changelog に新しいリリースはありません**。新しいページが 1 つ加わり、ページ単位で数えると既存の 221 ページ中 62 ページが変わり、変更は 805 行（追加 583・削除 222）、大幅更新は 1 ページです。総行数は 120,369 行から 120,807 行に増えました。

主要なものを以下に挙げます。

1. auto モードで「このセッションは無料の分類器の要求の対象ではない」という通知が出る理由と、ゲートウェイの設定や `CLAUDE_CODE_AUTO_MODE_SERVER=0` での対処を説明するページができた
2. Read・Grep・Glob がネットワークパス（Windows の UNC パス、macOS と Linux の `/net` の自動マウント）から読むときは、allow ルールも PreToolUse フックの `"allow"` も auto モードも確認を飛ばさなくなった（v2.1.292 以降）
3. Agent SDK に、セッションのトランスクリプトを新しいセッションに写して分岐させる `forkSession()`（TypeScript）と `fork_session()`（Python）の節ができた
4. Read ツールが `allow_large: true` で大きなファイルを 1 回で読めること（v2.1.296 以降）と、Edit と NotebookEdit が UTF-8 でないファイルの変更を断ることが文書になった
5. デスクトップアプリの SSH セッションで、接続の **Worktree folder** かリモートの `worktree.location` で worktree の置き場所を選べるようになった（Claude Desktop v1.44121.0 以降）
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**auto モードの分類器の料金の通知を説明する新しいページができた**](#1-auto-モードの分類器の料金の通知を説明する新しいページができた):  
  `auto-mode-classifier-billing` が加わりました。サーバー側の確認がセッションに届かず Claude Code が自分で分類器の要求を送る（トークンの使用量に数えられる）ときの通知の意味と、Enter・Esc での応じ方、ゲートウェイの設定や `CLAUDE_CODE_AUTO_MODE_SERVER=0` での対処が載っています
2. [**ネットワークパスからの読み取りに専用の権限の確認が入った**](#2-ネットワークパスからの読み取りに専用の権限の確認が入った):  
  Read・Grep・Glob が UNC パスや `/net` の自動マウントから読むときは、allow ルール・PreToolUse フックの `"allow"`・auto モードの分類器のどれも確認を飛ばさず、`dontAsk` モードでは拒否されます（v2.1.292 以降）。権限まわりの十数ページにこの例外が書き足されました
3. [**Agent SDK にセッションを分岐する forkSession が加わった**](#3-agent-sdk-にセッションを分岐する-forksession-が加わった):  
  TypeScript の `forkSession()` と Python の `fork_session()` が、セッションのトランスクリプトを新しいセッションに写します。`upToMessageId`（`up_to_message_id`）で途中のメッセージまでに絞れ、返る ID を `resume` に渡して続けます
4. [**大きなファイルの一括読み取りと UTF-8 でないファイルの扱いが文書になった**](#4-大きなファイルの一括読み取りと-utf-8-でないファイルの扱いが文書になった):  
  Read は既定で 1 回 25,000 トークンまで・ファイル全体なら 256 KB までですが、v2.1.296 以降は `allow_large: true` で残りのコンテキストに収まる限り 1 回で読めます。Edit と NotebookEdit は UTF-8 でないファイルの変更を断り、何も書きません
5. [**デスクトップの SSH セッションで worktree の置き場所を選べるようになった**](#5-デスクトップの-ssh-セッションで-worktree-の置き場所を選べるようになった):  
  SSH の接続の **Worktree folder**、リモートの `~/.claude/settings.json` の `worktree.location`、既定の `<project-root>/.claude/worktrees/` の順に決まります（Claude Desktop v1.44121.0 以降）。デスクトップアプリで始めた worktree のセッションがプロジェクトの設定をメインのチェックアウトから読むことも明記されました
<!-- light:highlight-list:end -->

## 1. auto モードの分類器の料金の通知を説明する新しいページができた

**新しいページ `auto-mode-classifier-billing`（「Auto mode classifier request charges」）ができました。** auto モードでは、シェルのコマンドやネットワークの要求などの操作を、動かす前に分類器が確かめます。サーバー側の確認が有効な場所では、サーバーがその確認をセッション自身のモデルの要求の一部として無料で行います。次の通知は、そのサーバーの確認がセッションに届いていないため Claude Code が代わりに自分で分類器の要求を送っており、そのアカウントではそれらがトークンの使用量に数えられる、という意味です。

```text
We're changing auto mode to no longer charge for classifier requests in Claude Code. However, this session isn't eligible.
```

Claude Code は、こうして確かめる最初の操作を、答えるまで止めておきます。壊れたものはなく、auto モードは動き続け、分類器の要求もこれまでどおり請求される、とされています。いちばん多い原因は Claude Code と API の間の LLM ゲートウェイかプロキシで、Claude Code がそれを特定できれば通知に名前が出ます。

- **通知への応じ方**: **Enter** で続けると、止めていた操作とセッションの残りは Claude Code 自身の分類器の要求を使い（これまでどおりトークンの使用量として請求）、そのセッションでは通知は再び出ません。通知がゲートウェイを名指ししていれば、このマシンでは 24 時間出なくなり、そうでなければ次にセッションが Claude Code 自身の分類器の要求に切り替わったときにまた出ます。**Esc** か **Ctrl+C** で取り消すと、止めていた操作は動かずターンが止まり、セッションは auto モードのままで、次に確かめる操作の前にまた通知が出ます。auto モードをやめるなら、答えた後に `Shift+Tab` でモードを切り替えます
- **答えを待てないとき**: Claude Code は同じ文を報告し、セッションは auto モードのまま続きます（このマシンで過去 24 時間にゲートウェイの通知を承認していれば報告も出ない）。`-p` の非対話モードでは標準エラーに出し、`stream-json` の出力では `system` の警告メッセージとして出すので、Agent SDK のアプリケーションはメッセージのストリームから読めます
- **対象にする**: ゲートウェイが原因なら、管理者かゲートウェイの提供元に、要求と応答をそのまま通すよう頼みます。要求のヘッダーと本文のフィールドを（`safeguards` の要求のフィールドのように知らないものも含めて）そのまま転送し、応答とストリーミングのイベントを `safeguard_results` のフィールドなどのキーを落とさず、ツールの使用の ID を書き換えずに返すことです。そうすれば新しいセッションはまたサーバーの確認を使います
- **`CLAUDE_CODE_AUTO_MODE_SERVER=0`**: ゲートウェイがサーバーの確認を提供できないと分かっているなら、セッションを始める前にシェルか `env` の設定キーでこれを設定すると、分類器の要求は常に Claude Code 自身のものになり（請求は同じ）、通知は出ません。Anthropic API への直接の接続では Claude Code v2.1.281 以降が要ります。`CLAUDE_CODE_AUTO_MODE_SERVER` が未設定のまま `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS=1` を設定してもサーバーの確認はオフになります。この変数は一時的なもので、後のリリースで外れうるとされています
- **通知が出る理由**: Pro・Max・Team のプランでは出ません。主な原因は、要求のヘッダーを外したり書き換えたり、知らない要求のフィールドを落としたり、応答を書き換えたりする LLM ゲートウェイかプロキシが経路にあること、または、サーバー側の確認がまだそのプラットフォーム・リージョン・資格情報に展開されていないことです。後者はゲートウェイがなくても通知が出続ける場合に疑い、サポートか管理者に確かめるか `/feedback` で報告します。auto モードのセッションで `/status` を実行すると、**Auto mode server** の行がサーバーの確認が判断している間は `Enabled`、切り替わった後は `Disabled` になります

- [auto モード分類器リクエスト料金 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/auto-mode-classifier-billing#respond-to-the-notice)
- [Auto mode classifier request charges - Claude Code Docs (English)](https://code.claude.com/docs/en/auto-mode-classifier-billing#respond-to-the-notice)
- [auto モード分類器リクエスト料金 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/auto-mode-classifier-billing#make-the-session-eligible)
- [Auto mode classifier request charges - Claude Code Docs (English)](https://code.claude.com/docs/en/auto-mode-classifier-billing#make-the-session-eligible)

## 2. ネットワークパスからの読み取りに専用の権限の確認が入った

**`permissions` に「Network paths」の節ができました。** Read・Grep・Glob のようなファイルを読むツールがネットワークパスから読むとき、その読み取りには専用の権限の確認がかかります。ネットワークパスとはほかのコンピューターに届きうるパスで、Windows では `\\server\share\file` のような UNC パス、macOS と Linux では `/net/fileserver/notes.txt` のような `/net` の自動マウントのパスです。そうしたパスを引くだけで名指しされたホストに接続することがあり、Windows ではその接続で資格情報がホストに送られうるためです。シェルのコマンドには別の確認があり、Manual モードでは UNC パスを引数に持つ読み取り専用の Bash・PowerShell のコマンドは Windows で引き続き確認を求めます。

Claude Code v2.1.292 以降、次のどれもこの確認を消しません。

- **allow ルール**: `Read` のようなツール全体のルールを含め、ルールは読み取りを事前に承認しません
- **PreToolUse フック**: `"allow"` を返すフックも確認を飛ばしません
- **auto モード**: 確認は利用者に届き、分類器は判断しません

`dontAsk` モードでは確認の代わりに読み取りを拒否します。`bypassPermissions` モードと、bypass permissions を使える状態の対話の端末のセッションの plan モードでは、この確認なしに読み取りが動きます。確認なしにネットワークの共有のファイルを読むには、先にローカルのパスを与えます。Windows では共有をドライブ文字に割り当てて起動時に `--add-dir` で渡し、macOS と Linux では `/mnt` や `/Volumes` の下などのローカルのパスにマウントしてそこから読みます。

この例外は権限を扱う多くのページに書き足されました。`permission-modes`（`dontAsk` の表の「Reads and pre-approved tools」が「作業ディレクトリの中のファイルの読み取り」に絞られ、auto モードの評価の順序と最初の作業ディレクトリ外の読み取りにも追記）、`hooks`・`hooks-guide`（`permissionDecision: "allow"` の例外）、`settings-reference`（`dontAsk`）、`cli-reference`（`--allowedTools`）、`headless`、`sub-agents`、`agent-sdk/permissions`・`agent-sdk/typescript`・`agent-sdk/python`・`agent-sdk/agent-loop`・`agent-sdk/hooks` です。追加の作業ディレクトリのファイルも、このネットワークパスの確認を除いて確認なしに読める、と改められ、`errors` の自動マウントのパスの説明にも、そのマウントの下の読み取りはこの確認を通る、と加わりました。同じページの「Extend permissions with hooks」には、`AskUserQuestion` や `requiresUserInteraction` の MCP のツールのようにユーザーの操作が要るツールでは、mod の `tool.check` の承認も確認を飛ばさない（v2.1.292 以降）、という文も加わっています。

- [権限を設定する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/permissions#network-paths)
- [Configure permissions - Claude Code Docs (English)](https://code.claude.com/docs/en/permissions#network-paths)

## 3. Agent SDK にセッションを分岐する forkSession が加わった

**`agent-sdk/typescript` に `forkSession()`、`agent-sdk/python` に `fork_session()` の節ができました。** どちらもセッションのトランスクリプトを新しいセッションに写し、元のセッションを変えずに会話を別の方向へ進められるようにします。会話の途中の時点から分岐するには、メッセージの ID を渡します。

- **TypeScript**: `forkSession(sessionId, options?)` は `Promise<ForkSessionResult>` を返します。`options.dir`（プロジェクトのディレクトリ。省略すると全プロジェクトを探す）、`options.upToMessageId`（その `uuid` のメッセージまでを写す。`getSessionMessages()` の値か、ストリームで送った `SDKUserMessage` に自分で付けた `uuid`）、`options.title`（省略すると元のセッションから作った名前の後に `(fork)`）を取ります。`sessionId` が UUID でない、セッションが見つからないかメッセージがない、`upToMessageId` に当たるメッセージがない、のときに例外を投げます
- **Python**: `fork_session(session_id, directory=None, up_to_message_id=None, title=None)` は同期で `ForkSessionResult` を返します。`session_id` か `up_to_message_id` が正しい UUID でない、またはセッションにメッセージがないか `up_to_message_id` が当たらないときは `ValueError`、セッションが見つからないときは `FileNotFoundError` を投げます。例は、`list_sessions(directory=..., limit=1)` で得た最新のセッションを `title="Try the OAuth approach"` で分岐させ、`forked.session_id` を `ClaudeAgentOptions(resume=...)` に渡して続けるものです
- **共通の注意**: 返る新しいセッションの ID を `resume` に渡すと分岐を続けられます。分岐には元のセッションのファイルのチェックポイントは含まれないので、分岐の前に取ったチェックポイントへ巻き戻すことはできません

`agent-sdk/session-storage` の `sessionStore` を取る関数の一覧の `forkSession()` も、この節を指すようになりました。

- [Agent SDK リファレンス - TypeScript - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/agent-sdk/typescript#forksession)
- [Agent SDK reference - TypeScript - Claude Code Docs (English)](https://code.claude.com/docs/en/agent-sdk/typescript#forksession)
- [Agent SDK リファレンス - Python - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/agent-sdk/python#fork_session)
- [Agent SDK reference - Python - Claude Code Docs (English)](https://code.claude.com/docs/en/agent-sdk/python#fork_session)

## 4. 大きなファイルの一括読み取りと UTF-8 でないファイルの扱いが文書になった

**`tools-reference` の Read ツールの説明に「Large files」の節ができました。** 既定では 1 回の Read は最大 25,000 トークン（`CLAUDE_CODE_FILE_READ_MAX_OUTPUT_TOKENS` で変更可）を返し、256 KB を超えるファイル全体の読み取りは断るので、Claude は大きなファイルを `offset` と `limit` で区切って読みます。Claude Code v2.1.296 以降は、ファイル全体が要るとき（利用者がファイル全体を求めた場合など）に `allow_large: true` を付けて、ファイル全体か長い行の範囲を 1 回で読めます。その読み取りの大きさは既定の上限ではなく、セッションのコンテキストウィンドウの残りに合わせて決まります。画像・PDF・ノートブックの上限は変わりません。

- **既定の上限を超えたとき**: ファイル全体がトークンの上限を超えると、最初のページと、どれだけ受け取ったか・`offset` と `limit` で続きを読む方法を示す `PARTIAL view` の通知が返ります。256 KB を超えるファイル全体か、トークンの上限を超える `offset`・`limit` の読み取りでは、範囲を絞るか Grep で探すよう求めるエラーが返ります
- **ノートブック**: セルの合計が 256 KB かトークンの上限を超える `.ipynb` も、内容の代わりにエラーを返すようになりました
- **関連の改訂**: `env-vars` の `CLAUDE_CODE_FILE_READ_MAX_OUTPUT_TOKENS` に既定値 25,000 トークンと、`allow_large` の読み取りはコンテキストに余裕があればこの上限を超えうることが加わりました。明示した `limit` の読み取りを早めに打ち切る仕組み（v2.1.208 での変更）の段落は外れています

**同じページに「Non-UTF-8 files」の節もできました。** UTF-8 として正しくないファイルには NotebookEdit を使えず、Edit も、ファイルがリトルエンディアンの UTF-16 のバイト順マークで始まる場合を除いて使えません。試すとツールは変更を断り、ファイルには手を付けません。Windows-1252 や Shift-JIS のような古い符号化で保存した非 ASCII のテキスト、バイナリーのファイル、不正なバイト列を含む UTF-8 が当てはまります。これらのツールはファイル全体を UTF-8 で書き戻すため、解読できないバイトをすべて置換文字 `U+FFFD` に変えてしまうからです。

- **Claude が受け取るエラー**: 符号化を保つシェルのコマンドで変更するか、先に UTF-8 へ変換するかを利用者に尋ねるよう伝えます。`errors` の新しい節「File is not valid UTF-8」は、そのメッセージ（`File is not valid UTF-8. It may use a legacy encoding such as Windows-1252, Shift-JIS or GBK, or be binary. ...`）と、今の符号化のまま Claude にシェルのコマンドで変えさせるか、UTF-8 に変換して（UTF-8 のつもりのファイルなら不正なバイトを直して）から編集を頼み直すかの 2 つの対処を挙げています。v2.1.296 より前は Edit と NotebookEdit がそのまま編集を適用し、解読できないバイトを `U+FFFD` にして保存していました
- **Write**: そうしたファイルも置き換えられますが、新しい内容が `U+FFFD`（Read が解読できないバイトの代わりに Claude に見せる文字）を含むと断ります。読んだ文字化けをそのまま書き戻さないための守りで、置き換えると UTF-8 で保存されるので元の符号化は失われます
- **Bash で見たファイル**: `cat` や `grep` などで見たファイルを Read なしに編集できる、という説明に、一致がなく何も出さない検索は読み取りに数えない、と加わりました

- [ツールリファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/tools-reference#large-files)
- [Tools reference - Claude Code Docs (English)](https://code.claude.com/docs/en/tools-reference#large-files)
- [ツールリファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/tools-reference#non-utf-8-files)
- [Tools reference - Claude Code Docs (English)](https://code.claude.com/docs/en/tools-reference#non-utf-8-files)

## 5. デスクトップの SSH セッションで worktree の置き場所を選べるようになった

**`desktop` に「Choose where SSH session worktrees go」の節ができました。** worktree の既定の置き場所は `<project-root>/.claude/worktrees/` で、ローカルのセッションは **Settings > Claude Code** の **Worktree location** で、SSH のセッションは SSH の接続の **Worktree folder** で変えられます。組織がセッションの使えるフォルダーを制限していない限り、新しい SSH のセッションは次のうち最初に設定されたものに worktree を作ります。

1. SSH の接続の **Worktree folder**（接続の追加時の項目に加わった。`~/worktrees` のようなリモートのマシンのフォルダー）
2. リモートのマシンの `~/.claude/settings.json` の `worktree.location`
3. 既定の `<project-root>/.claude/worktrees/`

設定したフォルダーの中にはプロジェクトごとのサブフォルダーができ、`~/worktrees` なら worktree のパスは `~/worktrees/<project>-<id>/<worktree-name>` です。設定したフォルダーがプロジェクトの中にあると、そのプロジェクトでは無視して既定を使います。以前に加えた接続や組織が管理する接続の **Worktree folder** は、環境のドロップダウンで接続にマウスを重ねて歯車のアイコンから設定します。この項目には Claude Desktop v1.44121.0 以降が要り、組織がフォルダーを制限していれば項目は隠れ、worktree はプロジェクトの中に置かれます。

- **`worktree.location`**: `settings-reference` に加わった新しいキーで、スコープは `User`（リモートのマシンの `~/.claude/settings.json`）、値は絶対パスか `~/` で始まるパスの文字列、既定は未設定です。読むのはデスクトップアプリだけで、`--worktree`・`EnterWorktree` ツール・隔離したサブエージェント・バックグラウンドのセッションは無視します。接続の **Worktree folder** が優先します。`settings` の、リポジトリのファイルでは効かないスコープの一覧にも `User` が加わりました
- **管理された接続**: `sshConfigs` で配った接続も、利用者は自分の **Worktree folder** を設定できるようになり、ほかの項目の編集と削除はできない、と改められました（`desktop`・`settings-reference`）
- **テレメトリー**: `monitoring-usage` に「Attribute telemetry to Desktop SSH sessions」の節ができました。メトリクスとイベントはセッションが動いたマシンを名指さないので、各リモートのマシンのテレメトリーをオンにする管理設定の `env` に `OTEL_RESOURCE_ATTRIBUTES`（例は `host.name=build-7`）を書きます。Claude Code は値を展開しないので `host.name=$(hostname)` は文字どおり届きます。名前が届かない原因として、Desktop を動かすコンピューターに設定した、ログイン用のファイルで `export` した（Desktop はログインシェルを通さない）、値に空白がある、ほかのものが既に変数を設定している、の 4 つが挙がっています。`service.name` の `claude-code-desktop` は「ローカルの」Code タブのセッションのもの、と改められました

**`worktrees` の「What worktrees share with the main checkout」には、デスクトップアプリで始めた worktree のセッションの扱いが加わりました。** そうしたセッションでは、Claude Code は設定・フック・スキル・エージェント・コマンド・`.mcp.json` のサーバーといったプロジェクトの構成を worktree ではなくメインのチェックアウトのルートから読みます。フックのコマンドはそのルートで動き、`${CLAUDE_PROJECT_DIR}` もそこを指すので、Claude が作業するファイルに届くにはフックの入力の `cwd` から worktree のパスを読みます。`CLAUDE.md` と `.claude/rules/` は worktree から読み込まれます。これまでの「`--worktree`・`git worktree add`・デスクトップアプリのどれで作っても同じ」という文からはデスクトップアプリが外れ、`hooks`・`skills`・`settings`・`plugins/loading`・`desktop` からもこの節への案内が加わりました。

- [Desktop アプリケーション - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/desktop#choose-where-ssh-session-worktrees-go)
- [Desktop application - Claude Code Docs (English)](https://code.claude.com/docs/en/desktop#choose-where-ssh-session-worktrees-go)
- [worktree を使用して並列セッションを実行する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/worktrees#what-worktrees-share-with-the-main-checkout)
- [Run parallel sessions with worktrees - Claude Code Docs (English)](https://code.claude.com/docs/en/worktrees#what-worktrees-share-with-the-main-checkout)

## 新規追加されたページ

<!-- light:new-pages:start -->
- [**Auto mode classifier request charges**](#1-auto-mode-classifier-request-charges) ([日本語](https://code.claude.com/docs/ja/auto-mode-classifier-billing) / [English](https://code.claude.com/docs/en/auto-mode-classifier-billing)):  
  auto モードの「このセッションは無料の分類器の要求の対象ではない」という通知の意味、応じ方、セッションを対象にする方法、通知が出る理由をまとめたページです（58 行。詳細はハイライト 1）
<!-- light:new-pages:end -->

## 1. Auto mode classifier request charges

`llms.txt` の「Configure permissions」「Choose a permission mode」の後に加わった、権限まわりの新しいページです。冒頭で通知の文と意味を示し、「Respond to the notice」（Enter・Esc・Ctrl+C での応じ方と、答えを待てない非対話の実行での扱い）、「Make the session eligible」（ゲートウェイに要求と応答をそのまま通させるか、`CLAUDE_CODE_AUTO_MODE_SERVER=0` を設定する）、「Why the notice appears」（原因と `/status` の **Auto mode server** の行での確かめ方）、「Related resources」の 4 節が続きます。内容はハイライト 1 のとおりです。

関連のページとして、`permission-modes` の auto モードとサーバー側の分類器の確認、`llm-gateway-protocol` のゲートウェイの互換性（機能のパススルーと先行機能のオフ）、`errors` の「The server returned no safety verdict」、`costs` を挙げています。ゲートウェイが応答を途中で切ったり Claude Code が読めない形に書き換えたりすると、この通知の代わりに判定のない拒否になる、という点も添えられています。日本語版（「auto モード分類器リクエスト料金」）も同時に公開されており、4 節の id は英語版と同じです。

- [auto モード分類器リクエスト料金 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/auto-mode-classifier-billing#why-the-notice-appears)
- [Auto mode classifier request charges - Claude Code Docs (English)](https://code.claude.com/docs/en/auto-mode-classifier-billing#why-the-notice-appears)

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
- [**Manage sessions**](#1-manage-sessions) ([日本語](https://code.claude.com/docs/ja/sessions#where-the-session-picker-looks) / [English](https://code.claude.com/docs/en/sessions#where-the-session-picker-looks)):  
  78 行（追加 37・削除 41）が変わりました。再開の節の説明が「Where the session picker looks」の 3 つの小見出しに移り、deny ルールが `ExitPlanMode` を外すと plan モードを戻さないことが加わり、同名のセッションの改名の記述や古い版の注記が外れました
<!-- light:updated-pages:end -->

`llms-full.txt` から切り出したページ単位の差分（`git diff --no-index --numstat`）が 50 行以上の既存ページを挙げています。今回これに当たるのは `sessions` だけで、次点は `agent-sdk/python`（47 行）、`hooks`（47 行）、`agent-view`（46 行）、`settings-reference`（45 行）、`permissions`（43 行）で、いずれも「軽微な更新」かハイライトで扱います。changelog は今回変わっていません。

## 1. Manage sessions

ページの大半は構成の組み替えと言い回しの整理で、新しい振る舞いは plan モードの 1 点です。

- **再開の説明の移動**: 「Resume a session」の表の後にあった、`claude -p` と Agent SDK のセッションを一覧と `claude --continue` から外す説明、`claude --resume <session-id>` が今のプロジェクト（とその git worktree）→ このマシンのほかのすべてのプロジェクトの順に ID を探す説明、動いているバックグラウンドのセッションでは `claude --continue` が `Your most recent conversation is running in the background` で終わる説明が、「Where the session picker looks」の下の 3 つの小見出し（「`/loop`, `-p`, Agent SDK, and background sessions」「Sessions in other worktrees and projects」「Resume by session ID or name」）に移りました。`errors`・`headless`・`cli-reference`・`agent-sdk/sessions`・`permissions` からのリンクもこの節を指すように改められています
- **plan モードを戻さない場合**: deny ルールが `ExitPlanMode` ツールを外していると、Claude は承認のための計画を出せないので、Claude Code は plan モードを戻さず、同じコマンドラインで新しいセッションが始まるときの権限モードで始めます（`/resume` なら今の権限モードのまま）。権限モードの表に「`plan` / Terminal, when a deny rule removes `ExitPlanMode`」の行が、`-p` で plan モードに戻す条件にも同じ項目が加わり、`vs-code` の「Resume past conversations」にも 3 つ目の例外として載りました。起動時の一覧から選ぶ場合の文も、`--permission-mode`・`--dangerously-skip-permissions`・`--fork-session` を渡すと plan モードを戻さない、と独立した文に分けられています
- **要約からの再開**: 長く止まっていた大きなセッションを再開するときのダイアログの説明が短くなり、選択肢の比較の前置きと、**Resume from summary** が全履歴に 1 回の要約の要求を送って最近の 5 ファイルまでを残すこと、**Resume full session as-is** が最初のメッセージの後に全履歴を処理し直してキャッシュすること、の説明が外れました
- **名前の記述の削除**: 同じマシンで動いているほかのセッションが既に使う名前で始めたり改名したりすると、自分の側を `auth-refactor-graceful-unicorn` のような 2 語の接尾辞付きの名前に変える、という段落（v2.1.232 以降）と、改名しない 3 つの場合の一覧が外れました。`cli-reference` の `--name`、`commands` の `/rename`、`cross-session-messaging` からも同じ説明が外れています。既定の表示名を名前付けや計画の承認が置き換える文、生成されたタイトルが一覧とステータスラインの `session_name` に出るという文も外れました
- **版の注記の削除**: v2.1.223 より前の ID の探し方、v2.1.281 より前の途中で切れたツールの呼び出しの扱い、v2.1.211 より前の `/loop` の扱い、v2.1.196 での `/cd` で移したセッションの扱い、v2.1.198 での圧縮後の `/branch` の名前の付け方の注記が外れました。一覧で `Ctrl+A` で全プロジェクトに広げると各セッションのプロジェクトのパスも見える、という文も外れています
- **言い回し**: 冒頭の「セッション」に用語集へのリンクが付き、コマンドの表と `/clear` の説明の「conversation」の多くが「session」に改められました

- [セッションの管理 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/sessions#where-the-session-picker-looks)
- [Manage sessions - Claude Code Docs (English)](https://code.claude.com/docs/en/sessions#where-the-session-picker-looks)
- [セッションの管理 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/sessions#permission-mode-on-resume)
- [Manage sessions - Claude Code Docs (English)](https://code.claude.com/docs/en/sessions#permission-mode-on-resume)

## 軽微な更新

<!-- light:minor-updates:start -->
今回の差分は **3 ファイル**（`llms-full.txt`・`llms.txt`・見出しマップ）です。**changelog は変わっておらず新しいリリースはない**ので、以下はすべて通常のページの文書の変更で、changelog 由来の項目はありません（そのため「バグ修正」の分類はありません）。`llms-full.txt` の生の差分は追加 1,007 行・削除 569 行ですが、ページ単位に切り出して数えると、既存の 221 ページ中 **62 ページ**が変わり、変更は 805 行（追加 583・削除 222）でした（生の差分は段落の移動を追加と削除の両方に数えるなどで多めに出ます）。新規の 1 ページ（ハイライト 1）と大幅更新の 1 ページ（`sessions`）を除く **61 ページ**を以下にまとめます。`llms-full.txt` の総行数は **120,369 行から 120,807 行へ 438 行増え**ました（既存ページの純増 361 行、新しいページの 58 行、2 回展開されている `plugins/troubleshooting` の 2 つ目の写しの 19 行）。`Source:` の行は 229 から 230 になり、固有のページは 221 から 222 へ、2 回展開されている 8 ページは変わりません。

**新機能**

- **ユーザー設定で Claude apps gateway の URL を指定できるようになった**（`claude-apps-gateway` の「Set the gateway URL in user settings」）。管理設定のないマシンでは、各開発者が自分の `~/.claude/settings.json` に `forceLoginMethod: "gateway"` と `forceLoginGatewayUrl` を書くと、`/login` が **Cloud gateway** の画面をその URL で開きます（開発者のマシンに Claude Code v2.1.295 以降が要り、初回接続の TLS のフィンガープリントの確認は出る）。読むのはユーザー設定だけでプロジェクトの `.claude/settings.json`・`.claude/settings.local.json` は読まず、管理設定のファイル・macOS の plist・Windows の HKLM の方針・ポリシーヘルパーが届くとユーザー設定のゲートウェイは無視されます。これに合わせて `settings-reference` の `forceLoginGatewayUrl` のスコープが `Managed` から `User or managed` になり、`forceLoginMethod` の `"gateway"` も同じ場所から読む、と改められました。`errors` には、この場合は起動時の接続の確認を飛ばす（v2.1.295 より前は確認していた）と加わり、`claude-apps-gateway-config`・`claude-apps-gateway-deploy` の「開発者自身の設定では構成できない」趣旨の文も改められています — [日本語](https://code.claude.com/docs/ja/claude-apps-gateway#set-the-gateway-url-in-user-settings) / [English](https://code.claude.com/docs/en/claude-apps-gateway#set-the-gateway-url-in-user-settings)
- **フックが `CLAUDE_ENV_FILE` に書いた変数が PowerShell のコマンドにも届くようになった**（`hooks` の「Persisted variables in PowerShell commands」）。Claude Code v2.1.296 以降、PowerShell はファイルを実行せず、Claude Code が代入を読み出してコマンドの環境に写します。そうするのは、このセッションのすべてのフックが書いた内容と起動前に設定したスクリプトのすべての行が、空行か `#` のコメント、または行頭の 1 つの代入（`export NAME=value`・`declare -x NAME=value`・`NAME=value`。値は Bash が書かれたとおりに使うもので、英数字と `_ @ % + = : , . / -` だけの引用符なしのテキスト、単一引用符のテキスト、`$`・バッククォート・`"` をバックスラッシュでエスケープした二重引用符のテキストの組み合わせ）のときだけです。`export PATH="$PATH:./node_modules/.bin"` や `source`、`direnv export bash` の `$'...'` のような行が 1 つでもあると PowerShell には何も届かず、`claude --debug` が `Session environment is not all plain assignments` を記録します（Bash には引き続きすべて届く）。Windows では値に `/` か `\` を含む変数は届かず、サンドボックスの PowerShell のコマンドには何も届きません。PowerShell で動くフック自身は `CLAUDE_ENV_FILE` を使えない、とも加わり、`tools-reference`・`env-vars` にも同じ案内が載りました — [日本語](https://code.claude.com/docs/ja/hooks#persisted-variables-in-powershell-commands) / [English](https://code.claude.com/docs/en/hooks#persisted-variables-in-powershell-commands)
- **端末にセッションの状態を表示する OSC 7501 への対応が載った**（`terminal-config` の「See session status in your terminal」）。端末が OSC 7501 Program Status Protocol を実装していれば、対話の Claude Code のセッションが作業中か、利用者を待っているか、終わったかを端末が示せます。Claude Code の側で有効にするものはありません。状態が出ないときの原因として、Claude Code v2.1.295 より前、tmux の中（端末ではなく tmux の対応を確かめるので `allow-passthrough` は効かない。tmux の外で始める）、バックグラウンドのセッション（アタッチ中も報告しない。エージェントビューが状態を示す）、`CLAUDE_CODE_DISABLE_TERMINAL_TITLE=1` の 4 つが挙がっています。`env-vars`・`agent-view` にも対応する記述が加わりました — [日本語](https://code.claude.com/docs/ja/terminal-config#see-session-status-in-your-terminal) / [English](https://code.claude.com/docs/en/terminal-config#see-session-status-in-your-terminal)
- **スピナーの横のトークン数の読み方が載った**（`costs` の「Read the token count beside the spinner」）。`Deciphering… (10m 27s · ↓ 5.5k tokens)` のような数は、今のターンがこれまでに出した出力のおおよその数をその場で数えたものです。Claude がストリームで返すテキストとツールの呼び出し、思考、前面で動くサブエージェントの出力を含み、モデルに送るもの（プロンプト・会話の履歴・ほかのコンテキスト）は含みません。各ターンの始めと会話の圧縮で戻り、出力が届くまで・行が狭すぎるとき・スクリーンリーダーのモードでは出ません。`/usage` の Session の `Usage by model` の出力の数（セッション全体の合計）や、verbose モードが加えるトークン数（コンテキストの大きさ）とは一致しない、とされ、`statusline` の verbose モードの説明にも同じ区別が加わりました — [日本語](https://code.claude.com/docs/ja/costs#read-the-token-count-beside-the-spinner) / [English](https://code.claude.com/docs/en/costs#read-the-token-count-beside-the-spinner)
- **同じ名前のプラグインが 2 つ有効なときのフックの扱いが載った**（`plugins/loading` の「Hooks when two enabled plugins share a name」）。別々のマーケットプレイスから同じマニフェストの名前のプラグインを 2 つ入れて有効にすると、`/plugin` ではどちらも有効に見えますが、一方のフックは外れます。`hooks/hooks.json` のフックを登録するのも hooks モジュールを読み込むのも名前ごとに 1 つで、組織の管理設定がオンにした方、なければ先に読み込まれた方がその名前を持ちます。`/plugin` の **Errors** タブと外れた方の詳細に `Its hooks.json hooks do not run` か `Its hooks module does not load` で始まる注記が出ます（v2.1.296 以降）。外れた方のフックを動かすには、名前を持つ方を無効にするかアンインストールして `/reload-plugins` を実行します（管理設定がオンにした方は無効にできない）。`plugins/troubleshooting` の「Hook loads but never fires」はまず `/plugin` でこの注記を見るよう改められ、`plugins/components`・`plugins/mods/troubleshoot` からも案内が加わりました — [日本語](https://code.claude.com/docs/ja/plugins/loading#hooks-when-two-enabled-plugins-share-a-name) / [English](https://code.claude.com/docs/en/plugins/loading#hooks-when-two-enabled-plugins-share-a-name)
- **JavaScript のオブジェクトのメンバー名をマーケットプレイスの名前に使えなくなった**（`plugins/troubleshooting` の「`Cannot add marketplace "<name>": Claude Code reserves this name and cannot register a marketplace under it`」）。`marketplace.json` の `name` が `constructor`・`hasOwnProperty`・`isPrototypeOf`・`propertyIsEnumerable`・`toLocaleString`・`toString`・`valueOf` のどれかだと、Claude Code は追加を断り何も登録しません（v2.1.296 以降。それより前は内部エラーで失敗した）。設定ファイルの `extraKnownMarketplaces` で宣言したものは起動時の追加が同じく失敗し、`/plugin` の **Errors** タブに出ます。持ち主なら `name` を変え、ほかの人のものなら持ち主に頼みます。`plugins/marketplace-reference` の予約名と `errors` の早見表にも加わりました — [日本語](https://code.claude.com/docs/ja/plugins/troubleshooting#claude-code-reserves-this-name) / [English](https://code.claude.com/docs/en/plugins/troubleshooting#claude-code-reserves-this-name)
- **遅いフックを見つけるデバッグログの行が載った**（`hooks` の「Debug hooks」）。Claude Code v2.1.296 以降、ツールのイベント・`UserPromptSubmit`・`SessionStart`・`Stop` などの command のフックは、終わると何を出力したかによらず `Hooks:` で始まる行を残します。イベント名と照合した値、括弧の中のコマンド、出どころのプラグイン、終わり方、所要時間が並び（例: `Hooks: PostToolUse:Write [.claude/hooks/log-write.sh] finished with status 0 (31ms)`）、終わり方には `timed out after <N>ms`・`cancelled`・`moved to the background`・`failed to start` もあります。`Notification`・`SessionEnd`・`PreCompact` などでは所要時間のない `completed with status` の行になります — [日本語](https://code.claude.com/docs/ja/hooks#debug-hooks) / [English](https://code.claude.com/docs/en/hooks#debug-hooks)

**機能改善**

- **フックの標準出力の JSON の読み方が 4 つの場合に整理された**（`hooks`）。async でないフックでは、空白以外に何もない 1 つの JSON オブジェクト（1 行でも複数行でも）が JSON の出力として読まれ、`{` で始まらないか `}` で終わらないものは平文、各行が単独で JSON として読める複数行は項目を設定する行がなければ平文・あれば解析の失敗、それ以外で `{` に始まり `}` に終わる不正な JSON は解析の失敗です。async のフックは JSON の応答を標準出力にそれだけで置けば複数行にでき（v2.1.295 以降。`jq` の整形出力など）、1 行に収めればほかのテキストと並べられます（`jq -c`）。`additionalContext` の文字列の `<system-reminder>`・`</system-reminder>` のタグは `<` が `&lt;` に置き換わって Claude に届き、`agent_id` はサブエージェントに加えてプロセス内のチームメイトでも付く、と改められました。`hooks-guide` の「Hook JSON has no effect」も「Shell profile output before the JSON」（`claude --debug` のログで `Hook output does not start with {` を探す）と「Fields at the wrong level」の 2 つの小見出しに分かれています — [日本語](https://code.claude.com/docs/ja/hooks-guide#shell-profile-output-before-the-json) / [English](https://code.claude.com/docs/en/hooks-guide#shell-profile-output-before-the-json)
- **`watch` などの exec ラッパーと `find` の操作が独立した小見出しになった**（`permissions` の「Exec wrappers and `find` actions」）。`Bash(watch *)` や `Bash(find *)` のような前方一致のルールでは、`watch`・`setsid`・`ionice`・`flock` などの exec ラッパーと、コマンドを動かす・ファイルを消す・書く操作（`-exec`・`-delete`・`-fprint` など）か検索するパスをファイルから取る `-files0-from` を持つ `find` を承認できません。`*` を含まない呼び出しは `Bash(find build -type f -delete)` のような完全一致のルールで承認でき、`find . -name '*.tmp' -delete` のように `*` を含むものはルールがワイルドカードとして読まれるので確認が残る（その都度承認するか、`"allow"` を返す PreToolUse フックを使う）とされました。読み取り専用のコマンドの例外にも、`ps auxe` や `ps aux -e` のように環境変数を出しうる `e` の選択肢を持つ `ps` が加わり（ダッシュ付きの形の確認は v2.1.290 以降）、`WebFetch(domain:example.com)` はサブドメインを含まない、と明記されました — [日本語](https://code.claude.com/docs/ja/permissions#exec-wrappers-and-find-actions) / [English](https://code.claude.com/docs/en/permissions#exec-wrappers-and-find-actions)
- **保護されたパスと重要なパスの対象が広がった**（`permission-modes`）。ユーザー・プロジェクト・ローカルの設定ファイルがシンボリックリンク（dotfiles のリポジトリへのリンクなど）のとき、その指す先のファイルも保護され、分類器に回すモードでもその書き込みは allow ルールがあっても確認を求めます。`rm`・`rmdir` の重要なパスには、Windows のホームディレクトリの 8.3 形式の短い名前（`C:\Users\LONGNA~1`）、`C:\` と同じ意味の `\\?\C:\`・`\\localhost\C$`、ドライブ文字の代わりに GUID でボリュームを示すパス（`\\?\Volume{GUID}\work\build`）が加わりました（いずれも v2.1.292 以降） — [日本語](https://code.claude.com/docs/ja/permission-modes#other-targets-that-count-as-critical-paths) / [English](https://code.claude.com/docs/en/permission-modes#other-targets-that-count-as-critical-paths)
- **バックグラウンドのセッションでの `bypassPermissions` の承認の扱いが載った**（`permission-modes` の「Skip all checks with bypassPermissions mode」）。バックグラウンドのセッションは、ユーザー設定か管理設定に記録された承認を尊重します。記録がなければ `claude --bg --permission-mode bypassPermissions` は対話のセッションで承認するまで断られ、`skipDangerousModePermissionPrompt` が `.claude/settings.local.json` にしかなければ、バイパスの要求を無視して始まり `Bypass permissions was requested at launch and ignored · ...` の通知を固定します（`~/.claude/settings.json` にそのキーを加えて新しいバックグラウンドのセッションを始める）。`agent-view` の同じ説明も、承認が記録されていること、と改められました — [日本語](https://code.claude.com/docs/ja/permission-modes#skip-all-checks-with-bypasspermissions-mode) / [English](https://code.claude.com/docs/en/permission-modes#skip-all-checks-with-bypasspermissions-mode)
- **スーパーバイザーが止まった後のバックグラウンドのセッションの振る舞いが載った**（`agent-view` の「The supervisor process」）。スーパーバイザー自体が（Claude Code の外から終了されるなどで）止まると、macOS と Linux では各セッションのプロセスが新しいスーパーバイザーの再接続を約 1 分待ち、来なければ止まります。その 1 分のうちに `claude agents` を実行すればセッションは動き続け、過ぎても保存された会話はディスクに残り、アタッチか返信で再開します。`claude daemon stop --any --keep-workers` の後の手順も、約 1 分のうちに `claude agents` を実行する、と改められました — [日本語](https://code.claude.com/docs/ja/agent-view#the-supervisor-process) / [English](https://code.claude.com/docs/en/agent-view#the-supervisor-process)
- **`←` でバックグラウンドに移すときの細かな振る舞いが加わった**（`agent-view` の「Switch sessions without leaving the terminal」）。権限の確認に **Yes** と答えるなどでターンが続けば今のツールが終わった時点で移り、`Esc` で中断するなどターンを止めると `Backgrounding cancelled — the turn was stopped.` で切り替えを取り消します。移すときに Claude が前面で動かしているシェルのコマンドは（ダイアログなしに）止まり、バックグラウンドのセッションの Claude はそれを始めた記録を持たないので再び動かしうる（待っている間に `Ctrl+B` でバックグラウンドのコマンドにすれば続く）、とされました。`/loop` が次の反復を待つ間にデタッチしてもループは続き、`claude attach` に名前を渡せるのはプロセスが動いている間だけ（止まったセッションは ID で再開）、とも加わりました（`cli-reference` も同じ） — [日本語](https://code.claude.com/docs/ja/agent-view#switch-sessions-without-leaving-the-terminal) / [English](https://code.claude.com/docs/en/agent-view#switch-sessions-without-leaving-the-terminal)
- **取り戻した下書きと待ち行列のテキストの扱いが載った**（`interactive-mode`）。何も動いていないときの `Ctrl+C` で消した入力は、入力欄が空のまま `Up` を押すと戻ります（v2.1.288 以降）。`←` がバックグラウンドへの切り替えを待つ間に待ち行列のテキストを取り戻すと、テキストは入力欄に残って切り替えは取り消され、セッションが移る瞬間に取り戻したテキストは送られずに消えますが、それぞれコマンドの履歴に残るので、セッションを開き直して空のプロンプトで `Up` を押せば戻せます — [日本語](https://code.claude.com/docs/ja/interactive-mode#take-back-what-you-queued) / [English](https://code.claude.com/docs/en/interactive-mode#take-back-what-you-queued)
- **巻き戻しのメニューの「No code restore」の印が説明された**（`checkpointing` の「Messages sent mid-turn not checkpointed」）。Claude の作業中に入力しターンの終わる前に Claude が読んだメッセージには自分のチェックポイントがなく、この印が付きます。その部分のファイルの変更を戻すにはターンを始めたプロンプトで **Restore code** か **Restore code and conversation** を選び（ターン全体の編集が戻る）、印の付いたメッセージでは **Restore conversation** で会話だけを巻き戻せます — [日本語](https://code.claude.com/docs/ja/checkpointing#messages-sent-mid-turn-not-checkpointed) / [English](https://code.claude.com/docs/en/checkpointing#messages-sent-mid-turn-not-checkpointed)
- **auto モードが判定を得られなかった呼び出しの「Not run」の行が載った**（`errors`・`auto-mode-config`）。対話のセッションでは、分類器のモデルが使えないなどで判定を得られなかったツールの呼び出しの下に、エラーの代わりに薄い `Not run · auto mode's check had no usable answer` の行が出ます。`Ctrl+O` のトランスクリプトの表示で全文を読め、「The server returned no safety verdict」の拒否も同じ行になります（v2.1.296 より前は赤いエラー）。`auto-mode-config` の「Fix a denial with an allow rule, an environment entry, or a retry」の説明も、この行を判定のない拒否として扱うよう改められました — [日本語](https://code.claude.com/docs/ja/errors#auto-mode-cannot-determine-the-safety-of-an-action) / [English](https://code.claude.com/docs/en/errors#auto-mode-cannot-determine-the-safety-of-an-action)
- **mod の `$.http.fetch` の上限とリダイレクトの扱いが載った**（`plugins/mods/reference`・`plugins/mods/api`）。上限の表に、要求の本文 4 MiB（文字数で数え、超えると拒否）、応答の本文 4 MiB（`text` は最初の 4 MiB で残りは読まない。`Content-Length` がそれ以上を宣言すると `is over the 4194304-byte limit` で終わる理由で拒否するが、リダイレクト後の最後の要求が `HEAD` なら例外。`HEAD` の例外は v2.1.296 以降）、リダイレクトと本文を含めて 1 回 30 秒、リダイレクトは 5 回まで、が加わりました。別のオリジンへのリダイレクトでは `accept`・`accept-language`・`content-type`・`user-agent` 以外の要求ヘッダーを落とすので、`Authorization` に頼る要求は失敗しうる、とされています。このほか、相対パスはフックが扱うイベントのサブエージェントの作業ディレクトリでも解決する、`SendMessage` でサブエージェントを再開しても `agent.spawn` のフックは動かない（断るなら `tool.call` で照合する）、`engine.create` で加えた名前空間のメソッドはほかの mod のフックから呼ばれるとそのフックの文脈で動く、と加わり、`plugins/mods/troubleshoot` には `$.agent.register refused: the hooks module that made the call is no longer loaded`（読み込み直す前の古い写しからの呼び出し。`session.start` で登録する）の節ができました — [日本語](https://code.claude.com/docs/ja/plugins/mods/reference#limits) / [English](https://code.claude.com/docs/en/plugins/mods/reference#limits)
- **mod のネットワークの方針の範囲が書き分けられた**（`plugins/mods/admin` の「Know which controls still apply」）。組織の方針が WebFetch を許さないとすべての mod の `$.http.fetch` も断られますが、`CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` が止めるのは Claude Code に組み込まれた mod と、セッションの Anthropic の資格情報を持つ要求だけで、利用者が入れた mod の要求は止めません（v2.1.288 より前はすべての mod の要求を止めた）。mod の `tool.check` の承認が飛ばさない確認への案内も加わりました — [日本語](https://code.claude.com/docs/ja/plugins/mods/admin#know-which-controls-still-apply) / [English](https://code.claude.com/docs/en/plugins/mods/admin#know-which-controls-still-apply)
- **セルフホストの Anthropic git proxy の制約が 2 つ加わった**（`self-hosted-environments-deploy` の「Use the Anthropic git proxy」）。Anthropic が git の資格情報を与えるのはセッションに含まれるリポジトリだけで、同じホストのほかのリポジトリ（非公開のサブモジュール、パッケージマネージャーが git で取る依存、別のリポジトリのプラグインのマーケットプレイス）には与えないので、セッションを作る人に必要なリポジトリをすべて加えてもらいます。プッシュはブランチだけで、ブランチを消すプッシュやタグなどほかの参照へのプッシュは失敗します — [日本語](https://code.claude.com/docs/ja/self-hosted-environments-deploy#use-the-anthropic-git-proxy) / [English](https://code.claude.com/docs/en/self-hosted-environments-deploy#use-the-anthropic-git-proxy)
- **`post-session` のフックに渡す資格情報の注意が強まった**（`self-hosted-environments-configuration` の「post-session」）。フックが git に渡す資格情報はセッションが取得できるものとして扱い、そのプッシュ以上のことができないよう発行するよう求めています。フックの中の git はセッションが書ける設定ファイルを読み、そこで指定された認証情報ヘルパーやフィルタードライバーはフックの権限で動き、そこの設定はどのリモートを指定してもプッシュの行き先を変えうるためです — [日本語](https://code.claude.com/docs/ja/self-hosted-environments-configuration#post-session) / [English](https://code.claude.com/docs/en/self-hosted-environments-configuration#post-session)
- **ルーティンが pull request のイベントで動くときの起点が載った**（`routines`）。GitHub の pull request のイベントで動いた実行で、その pull request のリポジトリがルーティンの最初のリポジトリなら、既定のブランチではなく pull request の head のコミットから始めます。Team と Enterprise のプランでは、GitHub の認証の各方法を使う前に組織の Owner がそれをオンにする必要がある、とも加わりました — [日本語](https://code.claude.com/docs/ja/routines#repositories-and-branch-permissions) / [English](https://code.claude.com/docs/en/routines#repositories-and-branch-permissions)
- **Code Review の分析の画面の説明が改められた**（`code-review` の「View usage」）。週ごとの費用の「Cost weekly」が今月の支出を示す「Code Review cost」に替わり（今月を選んだときだけ金額を出す）、「Repository breakdown」はレビューの実行回数・見積もりの費用・pull request ごとの表示も示します。分析の費用は請求書と違うことがあり、Repository breakdown の費用は割引やクレジットの前の定価で、pull request に投稿したレビューだけを数える、と加わりました — [日本語](https://code.claude.com/docs/ja/code-review#view-usage) / [English](https://code.claude.com/docs/en/code-review#view-usage)
- **ワークフローのエージェントが呼んだフォークのスキルの結果の扱いが載った**（`skills`）。動的なワークフローのエージェントがフォークのスキルを呼ぶと、`background: false` がなくてもそのエージェントが結果を待って受け取ります。v2.1.295 より前は待たず、スキルがバックグラウンドで動くと結果は本体の会話に届いていました — [日本語](https://code.claude.com/docs/ja/skills#run-skills-in-a-subagent) / [English](https://code.claude.com/docs/en/skills#run-skills-in-a-subagent)
- **Agent SDK の細かな追記**: `agent-sdk/python` の `ResultMessage` に、近いうちに終わった複数のバックグラウンドのタスクの通知に 1 ターンで答えることがあり、そのときも通知ごとに `origin.kind` が `"task-notification"` の `ResultMessage` が順に届き、最後以外は `num_turns` が `0` で `result` が空、と加わりました。`agent-sdk/typescript` では、`tools/list` の項目が MCP Apps の `ui://` のリソースを宣言するツールの `structuredContent` の上限が 8,388,608 文字になった（v2.1.295 以降。それより前は除外）と改められています — [日本語](https://code.claude.com/docs/ja/agent-sdk/python#resultmessage) / [English](https://code.claude.com/docs/en/agent-sdk/python#resultmessage)
- **サブエージェントとサンドボックスの細かな追記**: `sub-agents` の、自分の worktree で動くサブエージェントの git の状態のスナップショットはその worktree のブランチ・状態・最近のコミットを示す、という文（「What loads at startup」）、`sandboxing` の自動許可のモードでも Monitor ツールのコマンドはサンドボックスで動くが自動では承認されない（`Bash(npm run *)` のような allow ルールを加える）、という項目、`env-vars` の `CLAUDE_AUTO_BACKGROUND_TASKS` で、サブエージェントの後ろにファイルの編集などのツールの呼び出しが待っていれば、そのサブエージェントは前面で終わってから呼び出しが始まる、という文が加わりました — [日本語](https://code.claude.com/docs/ja/sub-agents#what-loads-at-startup) / [English](https://code.claude.com/docs/en/sub-agents#what-loads-at-startup)
- **プラグインのマーケットプレイスを HTTPS で配るときの注意が加わった**（`plugins/host-marketplace` の「Serve users who have no git host account」）。SSH の鍵のない利用者には `CLAUDE_CODE_PLUGIN_PREFER_HTTPS=1` を案内し続けるよう求めています。シェルからの `claude plugin install` は `github` のソースで `SSH not configured, cloning via HTTPS` を出して自分で HTTPS に切り替えうるものの、セッションの中の `/plugin` からのインストールとプラグインの更新は切り替えないためです — [日本語](https://code.claude.com/docs/ja/plugins/host-marketplace#serve-users-who-have-no-git-host-account) / [English](https://code.claude.com/docs/en/plugins/host-marketplace#serve-users-who-have-no-git-host-account)
- **設定のキーの細かな改訂**（`settings-reference`）。`forceLoginOrgUUID` を管理された場所が空の配列か文字列（の配列）でない値にすると、Anthropic のアカウントでサインインする利用者は Claude Code を始めることもログインを終えることもできず、`forceLoginOrgUUID` を名指しして管理者に連絡するよう求めるメッセージが出る（型の違う値を出すポリシーヘルパーは実行の失敗になる）と改められました。`copyFullResponse` と `commands` の `/copy` は、コードブロックに加えてブロック引用があるときもピッカーを出す、とされています — [日本語](https://code.claude.com/docs/ja/settings-reference#forceloginorguuid) / [English](https://code.claude.com/docs/en/settings-reference#forceloginorguuid)

**その他**

- **GitHub Enterprise Server の Contribution metrics が「対応」から「非対応」に改められた**（`github-enterprise-server`・`analytics`）。対応状況の表の Contribution metrics が ✅ Supported から ❌ Not supported になり、github.com のリポジトリが要る（GHES のリポジトリの作業も分析の画面には使用量のメトリクスとして出る）とされました。設定の手順の「Enable features」は「Enable Code Review」に、GitHub App の権限の説明からも Contribution metrics が外れ、`analytics` の「Contribution metrics support GitHub Cloud and GitHub Enterprise Server」は github.com のリポジトリが対象、と書き換えられています — [日本語](https://code.claude.com/docs/ja/github-enterprise-server#what-works-with-github-enterprise-server) / [English](https://code.claude.com/docs/en/github-enterprise-server#what-works-with-github-enterprise-server)
- **OS のサービスとして入れたスーパーバイザーの記述が外れた**（`agent-view`・`corporate-launcher`・`network-config`）。`claude daemon status` の版の不一致の警告で OS のサービスなら `--any` なしの `claude daemon stop` を勧める文、`launchd` か `systemd` のユニットから起動するサービスはランチャーを通らないという項目、「OS にインストールされたスーパーバイザーはシェルの環境を受け取らない」という文、インストールしたサービスは `--any` なしで止めるという注記が外れました
- **古い版の注記の整理**: `skills`（`disable-model-invocation` と `${CLAUDE_PROJECT_DIR}` の v2.1.196）、`mcp`（ワークスペースの信頼と非対話の認証と OAuth のスコープの v2.1.196。スコープの説明は `scopes_supported` の一覧全体を要求しないという要点だけになった）、`sub-agents`（`inherit` の v2.1.196）、`settings-reference`（`enableArtifact` の v2.1.196）、`llm-gateway-connect`・`plugins/dependencies`（v2.1.196）、`debug-your-config`（v2.1.288。サブディレクトリの `CLAUDE.md` は、そのサブディレクトリのほかのファイルを Claude に読ませると読み込まれる、という案内に替わった）、`headless`（v2.1.223）から版の注記が外れました
- **言い回しの調整**: `agent-view`（「in-flight work」を「in-flight background work」に、`claude respawn` の説明、終わったプロセスの行の説明、シャットダウン後のセッションは保存された会話から再開し、中断した作業を続けるには続けるよう返信する）、`env-vars`（`CLAUDE_CODE_DISABLE_BG_EXIT_HANDOFF` の言い回し）、`corporate-launcher`（スーパーバイザーへのリンク）、`claude-apps-gateway`（「開発者の側で手作業の設定は要らない」の文を削除）、`agent-sdk/permissions`（`disallowedTools` の説明）、`settings-reference`（`sandbox.credentials` のすべて不正な値の扱いの文を削除）、`workflows`（`/workflows` の進行の表示がモデルの置き換えを警告する、という文を削除）、`troubleshoot-install`・`authentication`（Console のメンバーのページを `platform.claude.com/settings/members` と URL で示す）、`agent-sdk/session-storage`（`forkSession()` へのアンカー）
- **`llms.txt`**: 「Choose a permission mode」の後に新しいページ「Auto mode classifier request charges」の行が加わり、固有のページの URL は 221 から 222 に、Indexes の 11 言語の行を含めた収録 URL は 232 から 233 になりました。Indexes の各言語の行は「221 pages」から「222 pages」になり、リンク先が `_llms/<lang>.md` から `_llms/<lang>.txt` に変わっています
- **見出しマップ**: 33 行が加わり 1 行が外れました。加わったのは自動生成のスタンプ 1 行、新しいページの 7 行（ページの見出しと 4 つの節）、既存ページの 25 行の見出し（`sessions` の 3 つの小見出し、`agent-sdk/typescript` の `forkSession()`・`agent-sdk/python` の `fork_session()` とその小見出し、`tools-reference` の「Non-UTF-8 files」「Large files」、`permissions` の「Exec wrappers and `find` actions」「Network paths」など）で、外れたのはスタンプの古い行だけです
- **見出しマップ冒頭の自動生成スタンプが、2026年10月10日 01時38分51秒 UTC から 2026年10月11日 03時17分49秒 UTC へ進みました**

**参考リンクについて**: 日本語版は、新しいページと変更のあった既存の 62 ページをすべて取得して、リンクを付けた節の id と今回の内容（新しい節や書き換えた文）があるかを確かめました。今回も日本語版の追従が早く、新しいページ `auto-mode-classifier-billing` の日本語版がすでに公開され、`permissions`・`agent-sdk/typescript`・`agent-sdk/python`・`tools-reference`・`desktop`・`worktrees`・`sessions` をはじめ、リンクを付けたすべてのページの該当の節がすでに今回の内容になっていたため、すべて日本語版のリンクを付けています。**changelog ページへのリンクは、本サマリの方針どおり付けていません。**
<!-- light:minor-updates:end -->

## 新着情報

<!-- light:whats-new:start -->
**今回、`whats-new/` 配下のページに変更はありません。**
<!-- light:whats-new:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-10-09.md](./archives/latest/2026-10-09.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-10-09.md](./archives/latest-detail/2026-10-09.md)

<!--
base_commit: 83613c64d38ac27f70c52d6b25167a2fa1f233f2
head_commit: 096d54cbb316fc19ca321240fcef28dc6ea22401
generated_at_full: 2026-10-11T15:09:30+09:00
-->
