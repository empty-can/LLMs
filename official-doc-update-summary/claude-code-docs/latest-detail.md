---
対象期間: 2026年11月03日 〜 2026年11月04日
作成日: 2026-11-04
---

# Claude Code 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
**今回は changelog に新しいリリースはなく（最新は前回と同じ v2.1.318）、通常のページが v2.1.318 の変更に追いつき、`~/.claude.json` の破損と保存の失敗の節、組織の設定を読み込めないとセッションが始まらない場合の説明、Agent SDK の権限の評価の書き直し、Remote Control と再起動の後のコマンドのエラーの節、セルフホストのランナーの spawn の要求の理由が載りました**。新しいページはなく、228 ページ中 25 ページが変わり、変更はページ単位で 426 行（追加 338・削除 88）、大幅更新は `errors`・`agent-sdk/permissions` の 2 ページです。見出しマップに加わった 13 の見出しは、すべて `llms-full.txt` にも入っています。総行数は 127,408 行から 127,658 行に増えました。

主要なものを以下に挙げます。

1. `errors` に `~/.claude.json` の解析の失敗、空のファイル、保存の失敗を説明する 5 つの h3 ができ、`claude -p` はファイルを既定の内容に置き換えず失敗して止まると載った
2. Team か Enterprise の claude.ai ログインでは Anthropic がセッションの開始前に組織の設定を要求でき、読み込めないと始まらないことが `errors` の新しい h3 と `server-managed-settings` の注記に載った
3. `agent-sdk/permissions` の評価の手順と plan モードの節が書き直され、呼び出しが `canUseTool` に届くかの表と h3「Path patterns in rules」ができた
4. `remote-control` に `working folder not found` とプログラムのファイルがなくなったときの 2 つの h3、`errors` に再起動の前に承認したコマンドが動かなかったときの h3 ができた
5. `self-hosted-environments-configuration` に h4「Find out why a spawn request was sent」ができ、`CLAUDE_RUNNER_SPAWN_REASON` の 9 つの値と確かめる先の表が載った
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**設定ファイルの破損と保存の失敗を説明する節ができた**](#1-設定ファイルの破損と保存の失敗を説明する節ができた):  
  `errors` に `~/.claude.json` についての h3 が 5 つできました。解析できないときの「Configuration error in \~/.claude.json」、空でバックアップもないとき、前のアカウントが残っているかもしれないときの 2 つ、変更を保存できなかったときです。`claude -p` のような非対話の起動はファイルを変えずにコード 1 で終わるようになり、`settings`・`claude-directory`・`agent-sdk/typescript`・`troubleshoot-install` も追従しています
2. [**組織の設定を読み込めないとセッションが始まらない場合の説明が載った**](#2-組織の設定を読み込めないとセッションが始まらない場合の説明が載った):  
  `errors` に h3「Claude Code couldn't load your organization's settings」ができ、`server-managed-settings` の「Fetch and caching behavior」の注記が、マシンに保存した Team か Enterprise の claude.ai ログインでは Anthropic がセッションの開始前に組織の設定を要求できる、と述べました。`forceRemoteSettingsRefresh` の説明も、キーが未設定でもこの要求があれば設定なしの起動は止まる、と改められています
3. [**Agent SDK の権限の評価の説明が書き直された**](#3-agent-sdk-の権限の評価の説明が書き直された):  
  `agent-sdk/permissions` の「How permissions are evaluated」は、各ステップが呼び出しを決めるか、`canUseTool` へ送るか、先へ渡す、という説明になりました。「Plan mode」には、レビューのオンとオフで呼び出しがコールバックに届くかの表ができ、パスのルールは新しい h3「Path patterns in rules」に移りました。`canUseTool` の説明からは、すべての呼び出しを確かめるには `PreToolUse` フックを使う、という言い方が外れています
4. [**Remote Control と再起動の後のコマンドのエラーの節ができた**](#4-remote-control-と再起動の後のコマンドのエラーの節ができた):  
  `remote-control` に「"working folder not found"」と「"The program file this Remote Control started from is gone"」の h3 ができ、`Session failed: spawn error:` に続く `ENOENT` の意味と対処が載りました。`errors` には、再起動の前に承認したコマンドが動かなかったときの h3「Command approved before Claude Code restarted was not run」ができています（changelog の v2.1.318）
5. [**セルフホストのランナーで spawn の要求の理由を確かめられるようになった**](#5-セルフホストのランナーで-spawn-の要求の理由を確かめられるようになった):  
  `self-hosted-environments-configuration` に h4「Find out why a spawn request was sent」ができました。フックが `CLAUDE_RUNNER_SPAWN_REASON` で受け取る理由（Claude Code v2.1.318 以降）の読み方、オーケストレーターのログからの探し方、`session_created` から `prewarm` までの 9 つの値とそれぞれ確かめる先が載っています
<!-- light:highlight-list:end -->

## 1. 設定ファイルの破損と保存の失敗を説明する節ができた

**`errors` に `~/.claude.json` についての h3 が 5 つできました。** changelog の v2.1.318 の、`~/.claude.json` と共有のネットワークのホームディレクトリについての修正に対応します（前回は changelog の項目として取り上げた分です）。

- **「Configuration error in \~/.claude.json」**（Command-line errors）: アカウントの情報・MCP サーバー・プロジェクトごとの状態を持つ `~/.claude.json` を解析できなかった、というエラーです。ファイルは変わらず、`claude -p` のような非対話の起動は、ファイルを直すまで毎回コード 1 で終わります。バックアップが見つかれば出力がその名前を挙げ、`cp` の行を出します。`cp` の行があればそれを実行し（Windows では PowerShell で）、なければ、またはエラーが戻るなら、JSON を直すか、`~/.claude/backups/` の別の `.claude.json.backup.<timestamp>` をかぶせるか、ファイルの名前を変えます。`~/.claude.json` がないと、Claude Code はファイルの中身なしで既定の設定で起動します。v2.1.318 より前は、非対話の起動がこのエラーを出した後に `~/.claude.json` が既定の内容になり、次の起動は設定なしで動きました
- **「Claude configuration file was empty and no backup holds anything」**（Command-line errors）: 名指されたファイルが空で、どの `.backup` のコピーにも中身がなく、Claude Code はそのファイルが持つものを既定にして起動した、という起動時のメッセージです。`settings.json` と `.mcp.json` は別のファイルです。そのファイルの設定をやり直し（`user` と `local` のスコープの MCP サーバーを `claude mcp add` で加えるなど）、求められたらサインインし直します。v2.1.318 より前は、バックアップのない空のファイルを壊れていると報告しました
- **「Sign in again to take your previous account or API key off the config file」**（Authentication errors）: サインインの後のこの警告は、前のアカウントが `~/.claude.json` にまだあるかもしれない、という意味です。Linux か Windows で Console のログインが作った API キーも残っているかもしれません。シェルで `claude auth login` を実行してサインインし直すと、保存が再試行されます
- **「Your account or API key may still be in the config file」**（Authentication errors）: `/logout` か `claude auth logout` でこのプロセスはサインアウトしたものの、ファイルがアカウントを持たなくなったことを確かめられなかった（保存が届かなかったか、読み戻せなかった）、という意味です。シェルで `claude auth logout` を実行して保存をやり直すと、成功すれば `Successfully logged out from your Anthropic account.` が出ます
- **「Make this change again later: \~/.claude.json could not be updated」**（Configuration warnings）: サインインや信頼の確認への答えのような `~/.claude.json` の変更がファイルに保存されなかった、という stderr の通知です。`/login` を実行し直すなど、後のセッションで変更をやり直します

**ほかのページも追従しました。**

- **`settings` の「Fix a broken settings file」**: **Configuration error** の項目が書き直されました。`claude -p` の実行は終わりファイルは変わらない、復元は `errors` の節を見る、壊れたファイルを `~/.claude/backups/.claude.json.corrupted.<timestamp>` にコピーして対話的なセッションでは尋ねる、空でバックアップがなければ既定の設定で起動する、という内容です。`-p` の段落も、飛ばすのは壊れた user・project・local のファイルか壊れた値だ、と限定されました
- **`claude-directory`**: 「Cleaned up automatically」の `backups/` の行に、期限を過ぎると設定を持つ最後のコピーも削除されること、今のファイルが解析でき、設定を持ち、8 MiB 未満なら、その新しいコピーが残ることが加わりました。「Clear local data」の表では `~/.claude/backups/` が別の行になり、失うものは `~/.claude.json` を復元できる前のコピーだと示されています
- **`agent-sdk/typescript` の `startup_failure_reason`**: `~/.claude.json` が正しい JSON でないときの値 `config_file_invalid` が加わりました（TypeScript の Agent SDK v0.3.318 以降と Claude Code v2.1.318 以降が要ります）。ファイルは変わらないので、直すまで再試行は同じように失敗します
- **`troubleshoot-install` の新しい h4「Login fails on a network home directory」**: 要求が `API Error: 401` で失敗し、設定のディレクトリがネットワークのファイルシステムにあるなら、そこか自分のクォータが一杯でないかを確かめます。空きがないと `.credentials.json` にログインを保存できず、それでも `claude auth login` が `Login successful.` と出すことがあります。空きを作ってから `/login` か `claude auth login` を実行します。v2.1.318 より前は、まだ有効な保存したログインが空のファイルに置き換わることがあり、後のコマンドが `Not logged in` と報告しました
- **`errors` の「Not logged in」**: 同じ claude.ai のアカウントと組織に誰かがサインインし直すと `claude -p` のジョブがこのメッセージで終わるなら、そのサインインが動く場所の Claude Code を更新する、という項目が加わりました。v2.1.318 より前は、そのサインインの間に、新しいログインを保存する前に保存したログインを消していました

- [エラーリファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/errors#configuration-error-in-claude-json)
- [Error reference - Claude Code Docs (English)](https://code.claude.com/docs/en/errors#configuration-error-in-claude-json)
- [エラーリファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/errors#your-account-or-api-key-may-still-be-in-the-config-file)
- [Error reference - Claude Code Docs (English)](https://code.claude.com/docs/en/errors#your-account-or-api-key-may-still-be-in-the-config-file)
- [設定ファイルと優先順位 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/settings#fix-a-broken-settings-file)
- [Settings files and precedence - Claude Code Docs (English)](https://code.claude.com/docs/en/settings#fix-a-broken-settings-file)
- [.claude ディレクトリを探索する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/claude-directory#cleaned-up-automatically)
- [Explore the .claude directory - Claude Code Docs (English)](https://code.claude.com/docs/en/claude-directory#cleaned-up-automatically)
- [インストールとログインのトラブルシューティング - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/troubleshoot-install#login-fails-on-a-network-home-directory)
- [Troubleshoot installation and login - Claude Code Docs (English)](https://code.claude.com/docs/en/troubleshoot-install#login-fails-on-a-network-home-directory)
- [Agent SDK リファレンス - TypeScript - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/agent-sdk/typescript#startup_failure_reason)
- [Agent SDK reference - TypeScript - Claude Code Docs (English)](https://code.claude.com/docs/en/agent-sdk/typescript#startup_failure_reason)

## 2. 組織の設定を読み込めないとセッションが始まらない場合の説明が載った

**`errors` の Configuration warnings に h3「Claude Code couldn't load your organization's settings」ができました。** 組織の設定（server-managed settings を含む）を先に読み込まなければならないのに読み込めず、セッションが始まっていない、という状況です。メッセージの例は `Claude Code couldn't reach Anthropic to load your organization's settings (could not connect). <Organization name> requires them before a session can start.` で、`Claude Code can't start this session yet` というタイトルのダイアログなら、設定が読み込まれ次第ダイアログは閉じてセッションが始まります。非対話モードとバックグラウンドのセッションでは、メッセージを出してステータス 1 で終わります。対処はメッセージの言葉で分かれます。

- **`could not connect`・`the reply came from a network proxy, not Anthropic`**: ネットワークの接続を確かめ、社内のネットワークなら `api.anthropic.com/api/claude_code/policy_limits` と `api.anthropic.com/api/claude_code/settings` への HTTPS を許すよう IT に頼み、**Retry now** を選ぶかコマンドを実行し直す
- **`timed out`・`Anthropic returned an error`・`Anthropic asked it to retry shortly`**: ダイアログに再試行させるか、後で実行し直す。続くなら status.anthropic.com を確かめる
- **`still loading`・`couldn't verify your sign-in with Anthropic yet`**: ダイアログに再試行させるか、実行し直す。サインインのメッセージが続くなら `claude auth login` を実行する
- **`Your Claude session has expired`**: このマシンに保存したサインインが無効なので、再試行は効かない。ダイアログの **Sign in again** で Claude Code を閉じ、シェルで `claude auth login` を実行する（セッションを始められない間も動く）
- **`none of the settings the server returned could be applied as written`**: 組織の server-managed settings を直すよう管理者に頼み、再試行する

**`server-managed-settings` の「Fetch and caching behavior」に注記が加わりました。** マシンに保存した Team か Enterprise の claude.ai ログインでは、Anthropic がセッションの開始前に組織の設定を要求できます。要求があるときは、その節のリストの内容にかかわらず、サインインが切れている（`claude auth login` を実行するまで）か、設定も最近のキャッシュのコピーもない（`api.anthropic.com` に届くかを確かめる）と、開発者はセッションを始められません。起動時のメッセージに `before a session can start` か `Your Claude session has expired` があれば、この要求が当たっています。

- **`server-managed-settings` のほかの節**: 「Enforce fail-closed startup」の既定の動きの説明の最後に、Anthropic が設定を要求することもある、と加わりました。「Invalid entries in delivered settings」は、`before a session can start` で起動が止まったら `errors` の新しい節を見るよう案内し、「Security considerations」の表の「API is unavailable」の行は短くなって、例外は「Fetch and caching behavior」に任せています
- **`settings-reference` の `forceRemoteSettingsRefresh`**: キーが未設定のときの段落に、Anthropic が設定を要求でき、そのときは設定なしの起動が止まる、と加わりました。`false` の説明も「Anthropic が要求しない限り」で始まります。「Cloud gateway のセッションは常に待つ」の「常に」は外れました

- [エラーリファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/errors#couldnt-load-your-organizations-settings)
- [Error reference - Claude Code Docs (English)](https://code.claude.com/docs/en/errors#couldnt-load-your-organizations-settings)
- [サーバー管理設定を構成する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/server-managed-settings#fetch-and-caching-behavior)
- [Configure server-managed settings - Claude Code Docs (English)](https://code.claude.com/docs/en/server-managed-settings#fetch-and-caching-behavior)
- [すべての設定 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/settings-reference#forceremotesettingsrefresh)
- [All settings - Claude Code Docs (English)](https://code.claude.com/docs/en/settings-reference#forceremotesettingsrefresh)

## 3. Agent SDK の権限の評価の説明が書き直された

**`agent-sdk/permissions` の説明が、呼び出しがどこで決まるかに沿って書き直されました。** 「How permissions are evaluated」は、「SDK が次の順に権限を確かめる」から、「Claude Code は次のステップで呼び出しを確かめ、各ステップは呼び出しを決めるか、`canUseTool` へ送るか、先へ渡す」に改められています（手順ごとの変更は大幅更新 2 のとおりです）。

**「Plan mode」の節は、呼び出しがコールバックに届くかの説明になりました。** 「ソースファイルを編集せずに」という言い方が外れ、計画の間に Claude のファイルツールで行う編集は、保護されたパスの外なら、allow ルールが一致するか `PreToolUse` フックが `allow` を返しても `canUseTool` に届く、となりました。`AskUserQuestion` の呼び出しも、allow ルールがそのツールを名指していても届きます。auto モードが使えるときは、allow ルールが承認しない次の呼び出しがコールバックではなく auto モードの分類器へ送られます。

- シェルのコマンド
- Web のフェッチ
- Web の検索
- サーバーが読み取り専用と示す MCP ツールの呼び出し

このレビューは既定でオンで、`query()` に渡す `settings` かユーザー設定で `useAutoModeDuringPlan` を `false` にするとオフになります。オフの間、Web の検索と読み取り専用の MCP ツールの呼び出しはコールバックに届きます。シェルのコマンドと Web のフェッチについては、次の表ができました。

| 計画の間の呼び出し | レビューがオン | レビューがオフ、または auto モードが使えない |
| :- | :- | :- |
| `ls` のような読み取り専用のシェルのコマンド | コールバックに届かず動く | コールバックに届かず動く |
| allow ルールが承認しないほかのシェルのコマンド（critical-path の削除を除く） | 分類器へ行き、コールバックなしで承認か拒否される | コールバックに届く |
| 事前に承認されたドキュメントのドメインへの `WebFetch` | コールバックに届かず動く | コールバックに届かず動く |
| allow ルールが承認しないほかの `WebFetch` | 分類器へ行き、コールバックなしで承認か拒否される | コールバックに届く |

**「Allow and deny rules」にあったパスのルールの説明は、新しい h3「Path patterns in rules」に移って広がりました。** `Edit(path)` のルールはファイルを書く組み込みのツールすべてに当たるので、`Write` と `NotebookEdit` のパスのルールも `Edit(path)` で書きます。`Write(path)` や `NotebookEdit(path)` と書いたルールはどの呼び出しにも一致せず、効果がありません。`allowed_tools` と `disallowed_tools` では、パスのパターンを絶対パスなら `//` で、セッションの作業ディレクトリの中のパスなら 1 つの `/` で始めます。

- **`//path`**: `Edit(//secrets/**)` の deny ルールは、Claude のファイルツールと、`tee` や `> file` のリダイレクトのような Bash のコマンドからの `/secrets` の下への書き込みを止める。Claude が動かしたスクリプトが自分でファイルを開くと、まだ書ける。オペレーティングシステムによる強制は `sandboxing` を見る
- **`/path`**: `Edit(/secrets/**)` は作業ディレクトリの中の `secrets` ディレクトリに一致する

**`canUseTool` の説明も揃えられました。** `agent-sdk/python` の `CanUseTool`、`agent-sdk/typescript` の `CanUseTool`、`agent-sdk/user-input` の警告から、「すべてのツールの呼び出しを確かめるには `PreToolUse` フックを使う」という言い方が外れました。代わりに、`allowed_tools` の項目か設定の allow ルールが承認する呼び出しと、権限モードが承認する呼び出しはコールバックなしで動くので、それらを確かめるには `PreToolUse` フックを使う、という説明になっています。`agent-sdk/user-input` の警告の見出しは「自動承認したツールでコールバックは動かない」から、「`canUseTool` が動く前に、前のステップが呼び出しを許可か拒否することがある」に替わりました。両 SDK の `PermissionMode` の `plan` のコメントは `Planning mode - Claude explores and plans` に、`agent-sdk/agent-loop` の「Permission mode」の表は、`acceptEdits` の承認が作業ディレクトリの中に限られること、`plan` の編集が allow ルールが一致しても `canUseTool` に届くことに改められました。

- [権限を設定する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/agent-sdk/permissions#plan-mode-plan)
- [Configure permissions - Claude Code Docs (English)](https://code.claude.com/docs/en/agent-sdk/permissions#plan-mode-plan)
- [権限を設定する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/agent-sdk/permissions#path-patterns-in-rules)
- [Configure permissions - Claude Code Docs (English)](https://code.claude.com/docs/en/agent-sdk/permissions#path-patterns-in-rules)
- [承認とユーザー入力を処理する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/agent-sdk/user-input#detect-when-claude-needs-input)
- [Handle approvals and user input - Claude Code Docs (English)](https://code.claude.com/docs/en/agent-sdk/user-input#detect-when-claude-needs-input)
- [Agent SDK リファレンス - Python - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/agent-sdk/python#canusetool)
- [Agent SDK reference - Python - Claude Code Docs (English)](https://code.claude.com/docs/en/agent-sdk/python#canusetool)
- [Agent SDK リファレンス - TypeScript - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/agent-sdk/typescript#canusetool)
- [Agent SDK reference - TypeScript - Claude Code Docs (English)](https://code.claude.com/docs/en/agent-sdk/typescript#canusetool)
- [エージェントループの仕組み - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/agent-sdk/agent-loop#permission-mode)
- [How the agent loop works - Claude Code Docs (English)](https://code.claude.com/docs/en/agent-sdk/agent-loop#permission-mode)

## 4. Remote Control と再起動の後のコマンドのエラーの節ができた

**`remote-control` の Troubleshooting に 2 つの h3 ができました。** changelog の v2.1.318 の、`claude remote-control` などが `spawn ENOENT` で新しいセッションを始められなかった問題と、作業フォルダーがないときの紛らわしいエラーの修正に対応します。`errors` の「Find your error」の表にも、3 つのメッセージからこの 2 つの節へ案内する行が加わりました。

- **「"working folder not found"」**: `claude remote-control` のターミナルの `Session failed: working folder not found:` と引用符で囲まれたパスは、そのパスにフォルダーがないのでセッションを始められなかった、という意味です。サーバーが動いていればフォルダーを戻してセッションを始め直すかサーバーを止め、終わっていれば存在するフォルダーから `claude remote-control` を実行し直します。v2.1.318 より前は、同じ失敗が `Session failed: spawn error:` と `ENOENT` のメッセージになり、なくなったフォルダーではなくプログラムのファイルを名指しました
- **「"The program file this Remote Control started from is gone"」**: サーバーが起動したプログラムのファイルがなくなり、新しいセッションはそれを置き換えた新しい版で動く、という警告です。サーバーも新しい版へ移すには、止めて `claude remote-control` を実行し直します。Claude Code をネットワークのストレージにインストールしているなら、すぐにサーバーを再起動して `setup` の「Install on network storage」に従います。それ以外は再起動しなくても新しいセッションが始まります。新しい版が見つからなければ新しいセッションは失敗し、`Session failed: spawn error:` に `ENOENT` のメッセージが続きます。そのときはサーバーを止め、`claude` がシェルで動かないならインストールし直してから、実行し直します。v2.1.318 より前は、新しい版がインストールされていてもこの形で失敗しました

**`errors` の Tool errors に h3「Command approved before Claude Code restarted was not run」ができました。** 承認したシェルのコマンドが動かず、Claude がその結果として `This call was not run. The command was approved before Claude Code restarted` で始まるメッセージを受け取る場合です。シェルが承認された時点のディレクトリに戻っていることを Claude Code が確かめられなかった（ディレクトリがなくなったか置き換わった、セッションの開始のディレクトリの外にある、入るのに承認が要るか調べられない）という内容で、3 つ目の文が `It does not keep track of that directory across a restart in a session that has been in a worktree.` になることもあります。Claude に続けさせ、コマンドの承認を求められたら答えれば足ります。changelog の v2.1.318 の、再起動の後に承認したコマンドが開始のフォルダーで動いた問題の修正（入れないフォルダーなら動かない）に対応します。

- [Remote Control でローカルセッションをどのデバイスからでも続ける - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/remote-control#working-folder-not-found)
- [Continue local sessions from any device with Remote Control - Claude Code Docs (English)](https://code.claude.com/docs/en/remote-control#working-folder-not-found)
- [Remote Control でローカルセッションをどのデバイスからでも続ける - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/remote-control#program-file-is-gone)
- [Continue local sessions from any device with Remote Control - Claude Code Docs (English)](https://code.claude.com/docs/en/remote-control#program-file-is-gone)
- [エラーリファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/errors#command-approved-before-a-restart-was-not-run)
- [Error reference - Claude Code Docs (English)](https://code.claude.com/docs/en/errors#command-approved-before-a-restart-was-not-run)

## 5. セルフホストのランナーで spawn の要求の理由を確かめられるようになった

**`self-hosted-environments-configuration` の「The spawn-runner hook」に h4「Find out why a spawn request was sent」ができました。** changelog の v2.1.318 の `CLAUDE_RUNNER_SPAWN_REASON` の追加と、オーケストレーターのログの行の変更に対応します。フックは spawn の要求ごとの理由をこの変数で受け取り、`CLAUDE_RUNNER_SESSION_UUID` と一緒にログに残せます（オーケストレーターに Claude Code v2.1.318 以降が要ります）。未設定のことがあるので `"${CLAUDE_RUNNER_SPAWN_REASON:-}"` で読み、値にかかわらずランナーを起動します。フックで分岐するなら、Anthropic が値を増やすことがあるので既定の分岐を残します。

前の要求の理由を探すには、すべてのオーケストレーターのレプリカのログで `session=` とそのセッションの `CLAUDE_RUNNER_SESSION_UUID`（`session_...` の ID ではない）を検索します。`ok session=` と `nack session=` の行は `reason=` の後にこの変数の値を示し、未設定なら `reason=-` です。`[runner:orchestrator] ok session=` はフックがコード 0 で終わったこと、`[runner:orchestrator] nack session=` はオーケストレーターが失敗した spawn の要求を Anthropic へ報告していることを表します。各値は Anthropic がそのセッションについて最後に記録した原因だけで、履歴ではありません。

| 値 | 起きたこと | 確かめること |
| :- | :- | :- |
| `session_created` | 新しいセッションの最初の spawn の要求 | なし。固定のランナーか待機中のランナーがセッションを持っていた後は、フックが見る最初の要求が `runner_lost` のことがあるので、最初の要求の目印にはしない |
| `no_runner_registered` | 前の要求で `--expected-spawn-seconds` の間にランナーが登録されず、Anthropic に失敗の報告の記録もない | セッションの前の行の `stop: no nack for session=` か `nack failed session=` は、失敗の報告が記録されなかったことを表す。`ok session=` の行の後なら、ランナーが時間内に起動して登録したかを確かめる |
| `hook_failed` | オーケストレーターが、前の要求は失敗し再試行できると報告した（フックがコード 1 で終わった、`--hook-timeout` の終わりにまだ動いていたなど）。オーケストレーターの停止中のように、フックを動かさず要求を Anthropic へ返したときも同じ値 | この要求の前の最後の `nack session=` か `stop: handing back session=` の行を探す。`handing back session=` なら、直すものはフックにない |
| `runner_lost` | セッションを持っていたランナーが Anthropic への報告を止めたか、登録を解除したか、削除された | ノードの追い出し、メモリー不足の強制終了、スポットの回収、自分のロールアウトかスケールダウンなど、ランナーを止めたか切り離したものを探す |
| `runner_reported_failure` | 前のランナーが、チェックアウトの間などにセッションが失敗したと報告した | 前のランナーのログを読む。多くのセッションでこの値が出るなら、イメージとリポジトリの準備を確かめる |
| `resumed` | セッションが一時停止し、またランナーが要る（`--release-idle-session-min` で解放され、後で新しいメッセージを受け取ったなど） | なし |
| `requeued` | Owner が **Retry** を選んだ、ブロックされたセッションが新しいメッセージを受け取ったなどで、セッションがキューへ戻された | 同じセッションで続くなら、`nack session=` の行のエラーを読む。フックがコード 0 で終わっていれば、ランナーのログを読む |
| `server_retry` | Anthropic が前の要求か、ランナーでのセッションの開始を諦めて再試行している。フックの失敗ではない | 1 回ならなし。続くなら Anthropic のアカウントチームに報告する |
| `prewarm` | まだセッションのない、事前に温める要求 | なし |

- [セルフホスト環境でセッションをカスタマイズする - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/self-hosted-environments-configuration#find-out-why-a-spawn-request-was-sent)
- [Customize sessions in self-hosted environments - Claude Code Docs (English)](https://code.claude.com/docs/en/self-hosted-environments-configuration#find-out-why-a-spawn-request-was-sent)

## 新規追加されたページ

<!-- light:new-pages:start -->
（今回の対象期間に新規追加・削除されたドキュメントページはありません。`llms.txt` は変わっておらず、`llms-full.txt` に展開されている固有のページも 228 のままで、`Source:` の行が 231 あり 3 ページが 2 回展開されている状態も前回と同じです）
<!-- light:new-pages:end -->

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
- [**Error reference**](#1-error-reference) ([日本語](https://code.claude.com/docs/ja/errors#find-your-error) / [English](https://code.claude.com/docs/en/errors#find-your-error)):  
  129 行（追加 129・削除 0）が変わりました。7 つの新しい h3（ハイライト 1・2・4）のほか、「Find your error」の表に 13 行が加わり、「Image was too large」に画像の多い要求の上限のメッセージが載りました
- [**Configure permissions**](#2-configure-permissions) ([日本語](https://code.claude.com/docs/ja/agent-sdk/permissions#how-permissions-are-evaluated) / [English](https://code.claude.com/docs/en/agent-sdk/permissions#how-permissions-are-evaluated)):  
  `agent-sdk/permissions` の 85 行（追加 56・削除 29）が変わりました。ハイライト 3 の plan モードとパスのルールのほか、評価の手順、`bypassPermissions` と `acceptEdits` の説明が改められました
<!-- light:updated-pages:end -->

**行数の数え方**: `llms-full.txt` の生の差分（追加 338 行・削除 88 行）のハンクを、head 側の `Source:` 行でページに振り分けた値です（ページの並びは変わっておらず、ページ本文どうしの比較で変わった 25 ページと一致し、ページ単位の合計は生の差分と一致します）。base と head は同じ書式なので、正規化はしていません。この値が 50 行以上のページを大幅更新として挙げました。空行（と `>` だけの行）を除くと、`errors` は 84 行、`agent-sdk/permissions` は 70 行で、どちらも 50 行を超えます。次点は `agent-sdk/secure-deployment` の 26 行（追加 14・削除 12）、`self-hosted-environments-configuration` の 23 行（追加 23）、`desktop` の 20 行（追加 16・削除 4）です。

## 1. Error reference

ページの差分のうち、7 つの新しい h3 と「Not logged in」の項目はハイライト 1・2・4 のとおりです。そのほかは次のとおりです。

- **「Find your error」の表**: 13 行が加わった。`Authentication` の 2 行、Remote Control の 3 行、`Request errors` の 1 行、`Command-line errors` の 2 行、`Tool errors` の 1 行、`Configuration warnings` の 4 行で、どれも今回の節へ案内する
- **「Image was too large」**: メッセージの例に `An image in the conversation exceeds the dimension limit for many-image requests (3000px). Run /compact to remove old images from context, or start a new session.` が加わった。対処には、`dimension limit for many-image requests` のメッセージなら、メッセージが `/compact` を名指していれば実行し、そうでなければ画像を減らして新しいセッションを始める、と加わり、このメッセージは API のエラーが名指すピクセルの上限を示す、と述べている。changelog の v2.1.318 の、20 枚を超える画像のある要求で上限を常に 2000px と言っていた問題の修正に対応する

- [エラーリファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/errors#find-your-error)
- [Error reference - Claude Code Docs (English)](https://code.claude.com/docs/en/errors#find-your-error)
- [エラーリファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/errors#image-was-too-large)
- [Error reference - Claude Code Docs (English)](https://code.claude.com/docs/en/errors#image-was-too-large)

## 2. Configure permissions

`agent-sdk/permissions` の差分のうち、「Plan mode」の節と h3「Path patterns in rules」はハイライト 3 のとおりです。そのほかは次のとおりです。

- **「How permissions are evaluated」の手順**: 手順 2 の deny ルールは、`disallowed_tools` か SDK が読み込む設定ファイルのルール、という説明になった。手順 4 の権限モードは書き直された。`bypassPermissions` はどのモードも自動で承認しないアクションでなければ承認する、`plan` は一部の呼び出しがコールバックに届き、auto モードが使えるときはほかが分類器へ行く、`default` と `dontAsk` は allow ルールへ進む、`auto` は「Auto mode」を見る、という内容で、「ほかのモードでは要求が下へ落ちる」という文は外れた
- **「Allow and deny rules」の警告**: `Bash(npm test *)` のようなスコープ付きのルールでは、ほかの `Bash` の呼び出しは「コールバックへ落ちる」から「権限モードへ落ちる」に改められた。末尾の案内も、すべての呼び出しに走る確認には、から、allow ルール・`acceptEdits`・`bypassPermissions` が承認する呼び出しを確かめるには `PreToolUse` フックを使う、に替わった。`allowed_tools` は `bypassPermissions` を制限しない、という警告は、`allowed_tools=["Read"]` の例を別の段落に分け、このモードでもコールバックに届く呼び出しは「Bypass permissions mode」を見るよう案内する。プロジェクトの `.claude/settings.json` の allow ルールがいつ当たるかは `permissions` の「Project allow rules and workspace trust」を見る、という文も加わった
- **「Available modes」の表と「Accept edits mode」**: `acceptEdits` の承認は作業ディレクトリの中のものと明示された。承認する操作に `NotebookEdit` が加わり、ディレクトリを足すには Python では `add_dirs`、TypeScript では `additionalDirectories` を使う、と分けられた。「Writes to a protected path」は `permission-modes` の保護されたパスにリンクした
- **「Don't ask mode」**: **Use when** が「ヘッドレスのエージェントを動かし、確認を求めるはずの呼び出しごとに確実に拒否したいとき」に短くなった
- **「Bypass permissions mode」**: 警告の、コールバックに落ちるものの一覧に、`Dangerous rm operation not ruled out` のフラグが付いた Bash のコマンドが加わった

- [権限を設定する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/agent-sdk/permissions#how-permissions-are-evaluated)
- [Configure permissions - Claude Code Docs (English)](https://code.claude.com/docs/en/agent-sdk/permissions#how-permissions-are-evaluated)
- [権限を設定する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/agent-sdk/permissions#bypass-permissions-mode-bypasspermissions)
- [Configure permissions - Claude Code Docs (English)](https://code.claude.com/docs/en/agent-sdk/permissions#bypass-permissions-mode-bypasspermissions)
- [権限を設定する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/agent-sdk/permissions#accept-edits-mode-acceptedits)
- [Configure permissions - Claude Code Docs (English)](https://code.claude.com/docs/en/agent-sdk/permissions#accept-edits-mode-acceptedits)

## 軽微な更新

<!-- light:minor-updates:start -->
今回の差分は **2 ファイル**（`llms-full.txt` と見出しマップ）で、`llms.txt` は変わっていません。`llms-full.txt` の生の差分は追加 338 行・削除 88 行で、ページの並びは変わっていません。228 ページ中 **25 ページ**が変わり、**changelog のページは変わっていません**。大幅更新の 2 ページを除く **23 ページ**を以下にまとめます。

`llms-full.txt` の総行数は **127,408 行から 127,658 行へ 250 行増え**ました（生の差分の差し引き 338 − 88 と一致）。`Source:` の行は 231、固有のページは 228 のままで、2 回展開されている 3 ページ（`plugins/create`・`plugins/install`・`plugins/mods/overview`）も前回と同じです。コードフェンスの外の見出しは、引用の中の見出しも数えると 6,043 から 6,056 へ、行頭が `#` の見出しだけを数えると 6,032 から 6,045 へ、どちらも 13 増えました（外れた見出しはありません）。changelog の収録リリースは 436 のままで、最新は v2.1.318 です。今回の変更の多くは、前回 changelog の項目として取り上げた v2.1.318 の内容が通常のページに載ったものです。

**新機能**

- `~/.claude.json` の `config_file_invalid`（`agent-sdk/typescript`。詳細はハイライト 1 参照）
- `CLAUDE_RUNNER_SPAWN_REASON` の説明（`self-hosted-environments-configuration`。詳細はハイライト 5 参照）
- **Claude Desktop のペインを小さくできると載った**（`desktop` の h3「Minimize a pane」）。Terminal・Browser・iOS Simulator のペインのヘッダーの **Minimize** で、小さな大きさのまま見える場所に置けます。Claude Desktop v4.0.0 以降と、サードパーティのプロバイダーではなく Claude アカウントが要り、Browser のペインにはローカルのセッションでだけあります。小さくしたペインは、セッションの詳細のパネルが画面にあればカードの下（動かせず大きさも変えられない）に、なければチャットの隅に浮かびます。隅ではヘッダーをドラッグして別の隅へ動かし、チャットの中心に近い角をドラッグして大きさを変えます。**Expand** で元に戻し、隣の閉じるボタンで閉じます — [日本語](https://code.claude.com/docs/ja/desktop#minimize-a-pane) / [English](https://code.claude.com/docs/en/desktop#minimize-a-pane)
- **`CLAUDE_CODE_DISABLE_BG_STABLE_PATH` が `env-vars` に載った**（Claude Code v2.1.295 以降が要ります）。macOS のネイティブインストーラーで `1` にすると、各バックグラウンドのセッションのホストプロセスを `~/.local/share/claude/ClaudeCode.app` ではなくインストールしたバイナリから動かします。macOS がフォルダーへのアクセスのような権限を、更新のたびも含めて尋ね直すことがあります。シェルではなく、ユーザー設定か managed settings のファイルの `env`、または MDM のポリシーで設定します。`ClaudeCode.app` を取り除くには自分で削除します — [日本語](https://code.claude.com/docs/ja/env-vars#variables) / [English](https://code.claude.com/docs/en/env-vars#variables)

**機能改善**

- `settings`・`claude-directory`・`troubleshoot-install` の `~/.claude.json` とログインの保存の説明（詳細はハイライト 1 参照）
- `server-managed-settings`・`settings-reference` の組織の設定の要求（詳細はハイライト 2 参照）
- `agent-sdk/python`・`agent-sdk/typescript`・`agent-sdk/user-input`・`agent-sdk/agent-loop` の `canUseTool` と権限モードの説明（詳細はハイライト 3 参照）
- **Agent SDK の安全な配備の説明が改められた**（`agent-sdk/secure-deployment`）。「Built-in security features」の **Permissions system** の項目が書き直され、**Command parsing for permissions** の項目は **Critical-path removals** に替わりました。権限モードが `default` なら、作業ディレクトリのような critical path を消す `rm` か `rmdir` は、allow ルールが一致しても承認が要る、という内容で、書き込みを制御するにはファイルシステムの制御を使います — [日本語](https://code.claude.com/docs/ja/agent-sdk/secure-deployment#built-in-security-features) / [English](https://code.claude.com/docs/en/agent-sdk/secure-deployment#built-in-security-features)
- **Agent SDK の Sandbox runtime の説明が改められた**（`agent-sdk/secure-deployment` の「Sandbox runtime」）。**Network** の説明が、コマンドをそれ自身のネットワーク名前空間（Linux）か Seatbelt のプロファイル（macOS）で動かしトラフィックを組み込みのプロキシへ通す、に改められ、プロキシを飛ばして外のホストへつなぐと失敗する、と加わりました。`npm install @anthropic-ai/sandbox-runtime` の手順は `sandbox-environments` の「Set up and launch the runtime」へのリンクになり、**No TLS inspection** には「既定では」が付き、許可したドメインの資格情報の注意が 3 つ目の項目に分かれました。`agent-sdk/python`・`agent-sdk/typescript` の `SandboxNetworkConfig` の注記にも「既定では」が付いています — [日本語](https://code.claude.com/docs/ja/agent-sdk/secure-deployment#sandbox-runtime) / [English](https://code.claude.com/docs/en/agent-sdk/secure-deployment#sandbox-runtime)
- **Agent SDK のコンテナのネットワークの説明が改められた**（`agent-sdk/secure-deployment` の「Containers」）。`--network none` の説明が「すべてのネットワークインターフェースを除く」から「コンテナを外部のネットワークから切り離す」に替わり、**Unix socket architecture** の段落が書き直されました（DNS の検索と別のホストへの直接の接続は失敗する、ほかのホストへ届かせるにはホストでプロキシを動かしそのソケットをマウントする、`ANTHROPIC_BASE_URL` か `HTTP_PROXY` を `localhost` のポートへ向けるならコンテナの中でそのポートをソケットへ中継する）。`sandbox-runtime` と同じアーキテクチャだという段落とブログへのリンクは外れ、プロキシの許可リストの中ならエージェントはどの許可されたドメインへもデータを送れる、という警告が加わりました — [日本語](https://code.claude.com/docs/ja/agent-sdk/secure-deployment#containers) / [English](https://code.claude.com/docs/en/agent-sdk/secure-deployment#containers)
- **Amazon Bedrock のサービスティアの当たる範囲が載った**（`amazon-bedrock` の「Service tiers」・`env-vars`）。`X-Amzn-Bedrock-Service-Tier` のヘッダーは、この変数のあるセッションの Invoke API の要求すべてに、モデルのアクセスの確認を除いて付きます。Mantle のエンドポイントへの要求と Claude apps gateway を通す要求には効きません。ターミナルから始めるバックグラウンドのセッションに当てるには、設定の `env` に書きます（シェルで export した値は、supervisor を始めたシェルが export していたときだけ届きます）。`env-vars` の `ANTHROPIC_BEDROCK_SERVICE_TIER` の行からは、ヘッダーとして送るという文が外れました。同じページの「Enable Mantle」の文は `CLAUDE_CODE_USE_MANTLE` とリージョンを設定する、に改められ、「Region issues」の下の Invoke API を使い Converse API に対応しない、という文は外れ、「Mantle endpoint errors」の `400` の項目の最後は、両方のエンドポイントを有効にすると推論プロファイルの ID を Invoke API へ送る、に替わりました — [日本語](https://code.claude.com/docs/ja/amazon-bedrock#service-tiers) / [English](https://code.claude.com/docs/en/amazon-bedrock#service-tiers)、[日本語](https://code.claude.com/docs/ja/amazon-bedrock#mantle-endpoint-errors) / [English](https://code.claude.com/docs/en/amazon-bedrock#mantle-endpoint-errors)
- **フォルダーごとに記憶する権限モードと `defaultMode` の関係が改められた**（`desktop` の「Choose a permission mode」・`permission-modes` の「Switch permission modes」）。ローカルのセッションで選んだモードはフォルダーごとに記憶され、これまでは `defaultMode` より優先するとありましたが、優先するのはプロジェクトの `.claude/` の設定の `defaultMode` になりました。新しいローカルのセッションは `~/.claude/settings.json` か managed settings の `defaultMode` で始まることがあるので、最初のメッセージの前にセレクターを確かめます。Plan はこのセッションだけです — [日本語](https://code.claude.com/docs/ja/desktop#choose-a-permission-mode) / [English](https://code.claude.com/docs/en/desktop#choose-a-permission-mode)、[日本語](https://code.claude.com/docs/ja/permission-modes#switch-permission-modes) / [English](https://code.claude.com/docs/en/permission-modes#switch-permission-modes)
- **`defaultMode` の言い方が「セッションが始まるモード」から「既定の権限モード」に揃えられた**（`settings-reference`・`permissions`）。`settings-reference` の「Settings index」の 2 行、「Permission settings」、`permissions`、`permissions.defaultMode` の節と、`permissions` の「Permission modes」が、新しいセッションの既定の権限モードを設定する、という言い方になりました — [日本語](https://code.claude.com/docs/ja/settings-reference#permissions-defaultmode) / [English](https://code.claude.com/docs/en/settings-reference#permissions-defaultmode)、[日本語](https://code.claude.com/docs/ja/permissions#permission-modes) / [English](https://code.claude.com/docs/en/permissions#permission-modes)
- **auto モードのサーバーのレビューの要件の版が分かれた**（`permission-modes` の「Server-side classifier review」）。`-p` と VS Code の拡張機能のセッションは v2.1.278 以降、Agent SDK とデスクトップアプリのセッションは v2.1.281 以降です（これまでは 4 つとも v2.1.281 以降でした） — [日本語](https://code.claude.com/docs/ja/permission-modes#server-side-classifier-review) / [English](https://code.claude.com/docs/en/permission-modes#server-side-classifier-review)
- **SSH のセッションの長いタスクとサインインの関係が加わった**（`desktop` の「Keep a task running while Desktop is disconnected」）。Claude アカウントで使うとき、Desktop がタスクのサインインを更新する条件に、Desktop が動いて接続していることに加えて、サインインしていることが加わりました。戻って確かめるものの先頭に **Sign-in page** の項目が加わり、サインインして、タスクが止まっていればメッセージを送ります。Enterprise プランでは、組織が活動の量にかかわらずサインインから決まった日数でサインアウトさせることがあり、サインアウトの間はタスクのサインインが更新されないので、タスクが止まることがあります — [日本語](https://code.claude.com/docs/ja/desktop#keep-a-task-running-while-desktop-is-disconnected) / [English](https://code.claude.com/docs/en/desktop#keep-a-task-running-while-desktop-is-disconnected)
- **bare モードではフックが動かないことが明記された**（`headless` の「Start faster with bare mode」・`best-practices` の「Run Claude from a script」）。`--settings` で渡したフックも、フラグで読み込むプラグインの `hooks/hooks.json` やマニフェストの `hooks` のキーのフックも動かないので、それらが要る実行には bare モードを使いません — [日本語](https://code.claude.com/docs/ja/headless#start-faster-with-bare-mode) / [English](https://code.claude.com/docs/en/headless#start-faster-with-bare-mode)、[日本語](https://code.claude.com/docs/ja/best-practices#run-claude-from-a-script) / [English](https://code.claude.com/docs/en/best-practices#run-claude-from-a-script)
- **macOS のバックグラウンドのセッションのフォルダーへのアクセスの説明が改められた**（`agent-view`）。「Background sessions can't read Desktop, Documents, or Downloads on macOS」は、ネイティブインストーラーかどうかの説明から、一覧で Claude Code か `claude` のバイナリのパス・ファイル名の項目を探す、に替わりました。ファイル名は `2.1.316` のような版番号のことがあり、更新の後に `Operation not permitted` が戻ったら、新しい版の名前のような新しい項目を探してアクセスを与えます。「Version history」の v2.1.295 の行も、再起動するセッションのホストプロセスが同じ `~/.local/share/claude/ClaudeCode.app` のフォルダーから動く、に改められました — [日本語](https://code.claude.com/docs/ja/agent-view#version-history) / [English](https://code.claude.com/docs/en/agent-view#version-history)
- **Projects でリポジトリのエラーを直した後の手順が改められた**（`claude-projects` の「Repository access errors」・「Other messages」）。「Couldn't start the session」か「Unable to access your repository」の GitHub のアクセスを直すには、**Install on GitHub** か **Select repositories** のようなメッセージのボタンを押します。直した後は、もう 1 通メッセージを送るのではなく、プロジェクトの会話で Claude に同じ作業の新しいスレッドを始めるよう頼みます。**Check again** と **See how to fix** についての文は外れ、`Claude couldn't reach GitHub to fetch your repository` の行も同じ手順になりました — [日本語](https://code.claude.com/docs/ja/claude-projects#repository-access-errors) / [English](https://code.claude.com/docs/en/claude-projects#repository-access-errors)、[日本語](https://code.claude.com/docs/ja/claude-projects#other-messages) / [English](https://code.claude.com/docs/en/claude-projects#other-messages)
- **Claude apps gateway の Google のアクセストークンの警告が載った**（`claude-apps-gateway-deploy` の「Troubleshooting」）。ログの `upstream <name>: Google issued an access token that expires in <N>s` の警告は、資格情報のファイルの種類が `external_account` のアップストリームで、そのトークンの期限まで要求は成功し、`credential_source` が指すトークンを先に更新しないと失敗する、という意味です。プロセスがトークンをファイルに書くなら、古いものが切れる 5 分より前に新しいものを書かせます。changelog の v2.1.318 の Gateway のログの警告の追加に対応します — [日本語](https://code.claude.com/docs/ja/claude-apps-gateway-deploy#troubleshooting) / [English](https://code.claude.com/docs/en/claude-apps-gateway-deploy#troubleshooting)

**その他**

- **`skills` の `effort` の行にリンクが加わった**（「Frontmatter reference」）。別のモデルで動くフォークについては `model-config` の「Effort level of subagents and teammates」を見る、という案内です — [日本語](https://code.claude.com/docs/ja/skills#frontmatter-reference) / [English](https://code.claude.com/docs/en/skills#frontmatter-reference)
<!-- light:minor-updates:end -->

見出しマップ（`en/claude_code_docs_map.md`）は 14 行が加わり 1 行が外れました。加わったのは 13 の新しい見出しと新しいスタンプで、外れたのは古いスタンプです。`llms-full.txt` の見出しの増加（13）と同じ見出しで、今回、見出しマップにだけ先に載った見出しはありません。

**参考リンクについて**: 日本語版は、今回変わった 25 ページすべてを取得し、該当する節があるかと今回の内容になっているかを、計 54 項目について確かめました。54 項目とも日本語版がすでに今回の内容になっていたので、リンクはすべて日本語版を併記しています。アンカーは、見出しから作った id か、ページ内・ページ間のリンクが使っている id です。見出しと id が違うもの（`errors` の `#configuration-error-in-claude-json`・`#claude-configuration-file-was-empty`・`#couldnt-load-your-organizations-settings`・`#make-this-change-again-later`・`#command-approved-before-a-restart-was-not-run`、`remote-control` の `#program-file-is-gone`）は、ページ内かほかのページのリンクが使っている id です。`agent-view` のアポストロフィを含む見出し（「Background sessions can't read Desktop, Documents, or Downloads on macOS」）は id に曲がったアポストロフィが残るので、同じページの「Version history」にリンクしました。**changelog ページへのリンクは、本サマリの方針どおり付けていません。**

## 新着情報

<!-- light:whats-new:start -->
**今回、新着情報（`whats-new/`）のページに変更はありません**（最新の週のダイジェストは前回と同じ Week 37 です）。
<!-- light:whats-new:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-11-03.md](./archives/latest/2026-11-03.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-11-03.md](./archives/latest-detail/2026-11-03.md)

<!--
base_commit: 91ce08863140666e5065f2a289650527b5eff4bb
head_commit: 759bf707239c765d7cc90918f4b58b6f5344ef70
generated_at_full: 2026-11-05T15:09:31+09:00
-->
