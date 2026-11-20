---
対象期間: 2026年11月18日 〜 2026年11月19日
作成日: 2026-11-19
---

# Claude Code 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
**今回は changelog に v2.1.329（2026年11月19日、130 項目）が積まれ、`code-mode` に権限の確認・サンドボックス・コードの止め方・出力を確かめるフックの 10 の見出しが加わりました。保存したログインがいつ終わるかを確かめる方法、`mcp_tool` のフックの `"onFailure": "block"`、設定のリストが上書きされずに合わさること、サブエージェントの effort が決まる順番も載っています**。新規ページと新着情報（whats-new）のページはありません。`llms.txt` は変わっていません。`llms-full.txt` では 205 ページのうち 96 ページ（changelog を含む）の内容が変わりました。生の差分は 1,153 行（追加 754・削除 399）で、うち 146 行は changelog の新しいリリースです。大幅更新は `code-mode`・`errors`・`desktop` の 3 ページです。総行数は 129,902 行から 130,257 行に増えました。

主要なものを以下に挙げます。

1. `code-mode` に、auto と `bypassPermissions` のモードでも確認を求める方法、サンドボックスとの関係、実行中のコードの止め方、コードの出力を `PostToolUse` のフックで確かめて伏せる方法の節ができた（v2.1.328 以降、`UserPromptSubmit` のフックはコードの出力を受け取らない）
2. `authentication` に、`claude auth status --text` の `Sign-in` の行で、保存した claude.ai のログインが終わる日を確かめる節ができた（v2.1.318 以降）。`cli-reference` の `loginExpiresAt` と Agent SDK の `credential_expires_at` も載った
3. `hooks` で、`mcp_tool` のフックにも `"onFailure": "block"` を設定でき（v2.1.328 以降）、サーバーにつながらないかツールがエラーを返したときに操作を止められることが載った
4. `--settings` のフラグ・Agent SDK の `settings`・managed settings の説明で、`permissions.allow` のようなリストは上書きされず、各ファイルの分と合わさる、という書き方になった
5. `sub-agents` に、`effort` を持たないサブエージェントのレベルが決まる順番と、その既定を決める `CLAUDE_CODE_SUBAGENT_EFFORT` が載った
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**Code Mode に権限の確認と出力のフックの節ができた**](#1-code-mode-に権限の確認と出力のフックの節ができた):  
  `code-mode` の「Permissions and long-running code」に 3 つの h3 と 7 つの h4 が加わり、auto モードでもコマンドやコードに確認を求めるルール、サンドボックス、コードの止め方、`PostToolUse` のフックで出力を伏せる方法が載りました
2. [**保存したログインの終わる日を確かめる方法が載った**](#2-保存したログインの終わる日を確かめる方法が載った):  
  `authentication` に h3「Check when a stored login ends」ができ、`claude auth status --text` の `Sign-in` の行の読み方が載りました。`cli-reference`・`agent-sdk/typescript`・`errors`・`self-hosted-environments-testing` もこれに合わせて改められています
3. [**MCP ツールのフックでも失敗したときに操作を止められるようになった**](#3-mcp-ツールのフックでも失敗したときに操作を止められるようになった):  
  `hooks` の「Block the action when a hook fails」で、`"onFailure": "block"` を設定できるフックに `mcp_tool` が加わり、失敗に数えるものに「MCP failure」の項目ができました。changelog の v2.1.328 にある追加にページが追従したものです
4. [**設定のリストは上書きではなく合わさるという書き方になった**](#4-設定のリストは上書きではなく合わさるという書き方になった):  
  `cli-reference`・`agent-sdk/configuration`・`agent-sdk/python`・`agent-sdk/typescript`・`managed-settings`・`server-managed-settings`・`settings-reference` が、`settings` の「Lists merge instead of overriding」へリンクする形で改められました
5. [**サブエージェントの effort が決まる順番が載った**](#5-サブエージェントの-effort-が決まる順番が載った):  
  `sub-agents` の「When a subagent has no `effort` field or parameter」に 3 段の順番が載り、`env-vars` に `CLAUDE_CODE_SUBAGENT_EFFORT` が加わりました。終わったサブエージェントのトランスクリプトを `/tasks` から開き直す方法も載っています
<!-- light:highlight-list:end -->

## 1. Code Mode に権限の確認と出力のフックの節ができた

**`code-mode` の「Permissions and long-running code」に 10 の見出しが加わりました（詳細は大幅更新 1 参照）。** 「Permission checks」の冒頭には、auto と `bypassPermissions` のモードではコードが許可のプロンプトなしに最後まで動きうるが、どのモードも自動では承認しない操作のように、一部の呼び出しは確認を求める、という段落が加わっています。

- **コマンドに承認を求める**（h4「Require approval for a command」）: auto か `bypassPermissions` のモードで特定のコマンドに確認を求めるには、そのコマンドの `ask` ルールを加える。例は `~/.claude/settings.json` に保存する `"ask": ["Bash(git push *)"]` で、リモートのないリポジトリで auto モードのセッションを始め、`git push origin main` を頼むと確かめられる
- **コードを 1 つずつ先に承認する**（h4「Approve each piece of code first」）: コードを実行するツール `REPL` の `ask` ルールを加える。プロンプトにはコードが出ないので、答える前に `Ctrl+O` を押して **Code** の行を開いて読む（メインの会話からはサブエージェントのコードは見えない）。auto モードで承認すると、分類器が止めたはずのコードも始まり、その中のプロジェクトの編集と読み取り専用のコマンドはプロンプトなしに動く。コードがサブエージェントを始められないと Claude が報告したら、このルールを外す
- **実行中のプロンプトに答える**（h4「Answer a permission prompt while code runs」）: コメントなしの **No** か `Esc` ではコードが止まり、すでに終わった呼び出しの変更は残る。コメント付きの **No** ではその呼び出しだけが拒まれ、コードはほかの呼び出しを続けられる。サブエージェントからと表示されたプロンプトは対象外
- **サンドボックス**（h3「Limit shell commands with the sandbox」）: サンドボックスの設定は、コードが実行するシェルのコマンドに当てはまる。JavaScript そのものと、そのファイル・Web・MCP のツールの呼び出しはサンドボックスの外で動くので、それらも隔離するにはコンテナーか仮想マシンで Claude Code を動かす。コードがサンドボックスの外での実行を求めたときもコマンドをサンドボックスに留めるには、strict sandbox mode をオンにする（auto モードでは、分類器が確かめるのはその要求をするコードで、コマンドに別の確認はない）。`sandboxing` の「The unsandboxed retry escape hatch」にも、Code Mode では auto モードの再試行が違う動きをする、とこの節へのリンクが加わった
- **コードを止める**（h3「Stop code in progress」）: Claude が応答中かコードを待っている間は `Esc` を押す。Claude の応答が終わった後のバックグラウンドのコードは、`/tasks` で実行中のタスクを選んで `x` を押す。止めた後は、そのコードが始めてまだ動いているサブエージェント・シェルのコマンド・MCP の呼び出しを `/tasks` で確かめる
- **出力をフックで確かめる**（h3「Check code output with a hook」と 4 つの h4）: Claude が読む前にコードが返すものを確かめるか伏せるには、`REPL` に一致する `PostToolUse` のフックを書く。バックグラウンドのコードが終わったときと、コードがエラーを投げたときも同じフックが動く。出力は `tool_response`（`code`・`result`・`stdout`・`stderr`・`toolsUsed` などのフィールド）から読み、伏せるときは `tool_response` を変えた写しを `updatedToolOutput` で返す。`result`・`stdout`・`stderr`・`error` のテキストを伏せ、`code`・`stdout`・`stderr` は文字列のまま返し、画像と PDF を隠すなら `images`・`documents` を `[]` にする（形を崩すと Claude は元の出力を受け取る）。フックがブロックするときも、エラーになるときも写しを返す。拒まれたツールの呼び出しの入力は `refusedCalls` に繰り返されることがあり、Claude はそれを変えずに読むので、このフックでその入力の値を隠せると思わない、という警告もある

**`UserPromptSubmit` のフックでコードの出力を確かめていたなら、`PostToolUse` のフックへ移します。** v2.1.328 以降、`UserPromptSubmit` のフックは、管理者が managed settings で設定したものも含め、コードの出力を受け取りません（h4「Move a check from a `UserPromptSubmit` hook」）。`hooks` の「UserPromptSubmit」でも、このフックが受け取るものの一覧の Code Mode の出力の項目と、「UserPromptSubmit decision control」の `reason` の説明が、「v2.1.328 より前」の話になりました。changelog の v2.1.328 にある、Code Mode がスクリプトの出力に対して `UserPromptSubmit` のフックを実行しないようにした変更に、ページが追従した形です。

- [Code Mode でコードからツール呼び出しを実行する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/code-mode#permission-checks)
- [Run tool calls from code with Code Mode - Claude Code Docs (English)](https://code.claude.com/docs/en/code-mode#permission-checks)
- [Code Mode でコードからツール呼び出しを実行する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/code-mode#check-code-output-with-a-hook)
- [Run tool calls from code with Code Mode - Claude Code Docs (English)](https://code.claude.com/docs/en/code-mode#check-code-output-with-a-hook)

## 2. 保存したログインの終わる日を確かめる方法が載った

**`authentication` の「Credential management」に h3「Check when a stored login ends」ができました。** 使っている claude.ai のログインがいつ終わるかは、シェルで `claude auth status --text` を実行して確かめます。Claude Code v2.1.318 以降では、`Sign-in` で始まる行に、ログインが終わる時期が 2 つの日付の間として示されます。

- **早いほうの日付より前に**、ブラウザーで `/login` か `claude auth login` を使ってサインインし直す。Claude Code を使ってもログインは延びない
- 行が `any day now` か `may have ended` なら、今すぐサインインする。ほかの認証情報のときと、日付がわからないときは、この行が出ない
- 遅いほうの日付まで 10 日を切ると、テキストの出力の `claude -p` が標準エラーに `Warning: this sign-in` を出すので、早いほうの日付より前にサインインし直す

同じページの「Renew an expiring login」でも、起動時の警告 `Your login expires in 3 days · run /login to renew` が出るのは、「`/login` で作ったログインの期限の 3 日前から」ではなく、「ログインの 2 つの終わる日の早いほうから」となりました。

ほかのページもこれに合わせて改められています。

- **`cli-reference` の `claude auth status`**: v2.1.318 から、JSON の `loginExpiresAt` フィールドが、保存したログインの見込みの最も遅い終わる日か `null` を示す、と加わった
- **`agent-sdk/typescript` の `SDKResultMessage`**: `credential_expires_at`（保存した claude.ai のログインの見込みの最も遅い終わりを示す ISO 8601 のタイムスタンプ。ログインは最大 3 日早く終わりうる。ほかの認証情報のときと日付がわからないときは出ない。Agent SDK v0.3.318 以降）が加わった
- **`errors` の「Find your error」**: `Warning: this sign-in` の行（この節へ）と、`The refresh token in CLAUDE_CODE_OAUTH_REFRESH_TOKEN was used for this attempt` の行（その上に出た拒否を直し、`CLAUDE_CODE_OAUTH_REFRESH_TOKEN` に新しいトークンを設定する）が加わった
- **`self-hosted-environments-testing` の「Long-lived CI host」**: リフレッシュトークンの付与が最初のログインから 30 日で切れるのは変わらず、そのホストで `claude auth login` を対話で実行し直すのが「30 日ごと」から「ログインの最も早い終わる日より前」になった

- [認証 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/authentication#check-when-a-stored-login-ends)
- [Authentication - Claude Code Docs (English)](https://code.claude.com/docs/en/authentication#check-when-a-stored-login-ends)
- [CLI リファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/cli-reference#cli-commands)
- [CLI reference - Claude Code Docs (English)](https://code.claude.com/docs/en/cli-reference#cli-commands)

## 3. MCP ツールのフックでも失敗したときに操作を止められるようになった

**`hooks` の「Block the action when a hook fails」で、`"onFailure": "block"` を設定できるフックに `mcp_tool` が加わりました。** `onFailure` は v2.1.295 以降で使え、`mcp_tool` のフックでは v2.1.328 以降が要ります。

- **失敗に数えるもの**: 「MCP failure」の項目が加わり、`mcp_tool` のフックのサーバーがつながっていないか、ツールがエラーを返すと失敗になる。`PreToolUse` や `UserPromptSubmit` のようなイベントで `"block"` を設定したときは、`{}` か、`reason` 以外のフックの出力のフィールドを設定する JSON でない限り、空でない答えも失敗に数える
- **「MCP tool hook fields」**: 表に `onFailure`（`"continue"` か `"block"`）の行が加わった
- **「How the tool's result is read」「When the server is still connecting」**: ツールが `isError: true` を返したときに操作を止めるには `onFailure: "block"` を設定する、と加わった。フックがツールを呼ぶ時点でサーバーがつながっていなければ、「非ブロックのエラーで実行が続く」ではなく「フックが失敗する」となった
- **「Timeouts」と「UserPromptSubmit」**: タイムアウトでブロックさせるために `onFailure: "block"` を設定できるのは「`command` か `http` のフック」、という限定が外れた

`best-practices` の「Enforce steps with hooks」でも、実際に強制するためのフックの種類に `mcp_tool` が加わり、`errors` の「Find your error」には `blocking because onFailure is "block"` の行（この節へ）が加わりました。changelog の v2.1.328 にある、command と HTTP のフックと同じく `mcp_tool` のフックにも `"onFailure": "block"` を加えた変更に、ページが追従した形です。

- [Hooks リファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/hooks#block-the-action-when-a-hook-fails)
- [Hooks reference - Claude Code Docs (English)](https://code.claude.com/docs/en/hooks#block-the-action-when-a-hook-fails)
- [Claude Code のベストプラクティス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/best-practices#enforce-steps-with-hooks)
- [Best practices for Claude Code - Claude Code Docs (English)](https://code.claude.com/docs/en/best-practices#enforce-steps-with-hooks)

## 4. 設定のリストは上書きではなく合わさるという書き方になった

**`--settings` のフラグ、Agent SDK の `settings`、managed settings の説明で、`permissions.allow` のようなリストはほかのファイルの分と合わさる、と明記されました。** どれも `settings` の「Lists merge instead of overriding」（同じリストのキーを複数のファイルで設定すると、Claude Code は 1 つを選ばずにリストを合わせ、各ファイルがほかのファイルの項目を消さずに項目を足せる）へリンクしています。

- **`cli-reference` の `--settings`**: ここで設定した値はこのセッションで `settings.json` の同じキーを上書きするが、ほとんどのリストはそれらと合わさる、となった
- **`agent-sdk/configuration` の「Load settings files」**: 渡した権限のルールとほかのほとんどのリストは、ユーザー・プロジェクト・ローカルの設定ファイルの分に加わり、単一の値のほとんどは渡したものがそれらのファイルより優先する、となった（これまでは、渡したものはどの形でもそれらのファイルの設定を上書きする、としていた）
- **`agent-sdk/python`・`agent-sdk/typescript` の「Settings precedence」**: `allowed_tools`（TypeScript は `allowedTools`）か `settings` で渡した権限のルールはこれらのファイルのルールに加わり、単一の値のほとんどは `settings` のものが優先する、となった（これまでは、`agents`・`allowed_tools`・`settings` のようなプログラムのオプションがファイルの設定を上書きする、としていた）。Python では、managed policy の設定が「ほとんどの」プログラムのオプションより優先する、となっている
- **`managed-settings` の「What a developer can change」**: 「Allow rules and allowlists」の項目が加わった。開発者は `permissions.allow` や `allowedMcpServers` のようなリストに項目を足せるので、そのリストに `allowManaged*Only` のキーがあれば配る。`allowManagedPermissionRulesOnly` を使うなら、頼りにする deny と ask のルールも managed settings へ移す
- **`server-managed-settings` の「Settings precedence」**: ユーザーの allow ルールはこちらのものと合わさり、リストを固定するには「What a developer can change」を見る、と加わった
- **`settings-reference`**: `allowedMcpServers` は、ユーザーが加えるサーバーについて各ファイルの項目が 1 つの許可リストに合わさり、ユーザーに項目を足させないには両方のキーを managed settings に配る、となった。既定の説明も、「空の配列」ではなく「合わさったリストが空なら」ユーザーが加えるすべてのサーバーを止める、となっている。`parentSettingsBehavior` の `"merge"` も、制限するキーを残すフィルターを通し、`allowManaged*Only` のロックを設定しない限り権限の allow ルールとサンドボックスの許可リストも通る、となった

- [設定ファイルと優先順位 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/settings#lists-merge-instead-of-overriding)
- [Settings files and precedence - Claude Code Docs (English)](https://code.claude.com/docs/en/settings#lists-merge-instead-of-overriding)
- [マネージド設定をデプロイする - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/managed-settings#what-a-developer-can-change)
- [Deploy managed settings - Claude Code Docs (English)](https://code.claude.com/docs/en/managed-settings#what-a-developer-can-change)

## 5. サブエージェントの effort が決まる順番が載った

**`sub-agents` の「When a subagent has no `effort` field or parameter」に、フォーク・フォークしたスキル・チームメイト以外のサブエージェントは、次のうち最初に当てはまるレベルで動く、という順番が載りました。**

1. 設定していれば、`CLAUDE_CODE_EFFORT_LEVEL` のレベル
2. そのサブエージェントを始めたサブエージェントに設定した `effort`、またはスキルの `effort` のように今のターンだけに設定したレベル
3. 設定していれば、`CLAUDE_CODE_SUBAGENT_EFFORT` のレベル

どれもなければ、これまでどおり、メインの会話と同じモデルのサブエージェントはセッションで選んだレベル（`/effort` や `--effort`）で動き、別のモデルではそのレベルは当てはまりません。`env-vars` には `CLAUDE_CODE_SUBAGENT_EFFORT`（サブエージェントとワークフローのエージェントの既定の effort のレベルで、`low`・`medium`・`high`・`xhigh`・`max` のいずれか。フォーク・フォークしたスキル・チームメイトには当てはまらない。v2.1.315 以降）の行が加わり、`model-config` の「Effort level of subagents and teammates」も、「`effort` を持たない」ではなく「ほかのレベルが設定されていない」サブエージェントかチームメイト、という言い方でこの節にリンクしています。

同じページのほかの変更です。

- **終わったサブエージェントを開き直す**（「Finished subagents in the panel and task list」）: 一覧から外れた一部のサブエージェントのトランスクリプトを開き直せる、と加わった。ターミナルで `/tasks` を実行し、詳細の表示が開いたら `go back` と書かれたキーを押し、**Earlier in this session** の行を開いてサブエージェントで `Enter` を押す。v2.1.319 以降が要る。`env-vars` に加わった `CLAUDE_CODE_SUBAGENT_HISTORY` を `0` にすると、この `/tasks` の行が外れる。完了したバックグラウンドのサブエージェントが `/tasks` に残るのも、「フッターのヒントと同じ 30 秒」から「30 秒、メッセージを送ったならそれより長く」になった
- **「Available tools」**: `propose_skills` が一覧に加わり、バックグラウンドのサブエージェントが残す組み込みのツールに `ListPlugins`・`ListSkills`・`SearchPlugins`・`SearchSkills` が加わった。ほかの組み込みのツールは Claude Code が「ほとんど」外すので、バックグラウンドのサブエージェントでは頼らない、という書き方になった
- **「Let subagents spawn their own subagents」**: `claude -p` と Agent SDK では、サブエージェントを始めたサブエージェントはフォアグラウンドの入れ子のサブエージェントだけを待つ、となり、フォークのモードをオフにすると入れ子のサブエージェントがバックグラウンドで始まる、という説明が外れた。`agent-sdk/python` の「Agent」からも、`CLAUDE_CODE_FORK_SUBAGENT` を `0` にすると新しいエージェントがバックグラウンドで動く、という部分が外れている
- **新しい `agents` ディレクトリー**: 「Quickstart: create your first subagent」と「Write subagent files」から、セッションの開始時になかった `agents` ディレクトリーは実行中のセッションが検出しない、という説明が外れ、再起動が要るのは「3 つの場合」から「いくつかの場合」になった

- [カスタムサブエージェントの作成 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/sub-agents#when-a-subagent-has-no-effort-field-or-parameter)
- [Create custom subagents - Claude Code Docs (English)](https://code.claude.com/docs/en/sub-agents#when-a-subagent-has-no-effort-field-or-parameter)
- [環境変数 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/env-vars#variables)
- [Environment variables - Claude Code Docs (English)](https://code.claude.com/docs/en/env-vars#variables)

## 新規追加されたページ

<!-- light:new-pages:start -->
（今回の対象期間に新規追加されたドキュメントページはありません。`llms.txt` は変わっておらず、`llms-full.txt` の `Source:` の行も 208、固有のページも 205 のままです）
<!-- light:new-pages:end -->

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
- [**Run tool calls from code with Code Mode**](#1-run-tool-calls-from-code-with-code-mode) ([日本語](https://code.claude.com/docs/ja/code-mode#permission-checks) / [English](https://code.claude.com/docs/en/code-mode#permission-checks)):  
  139 行（追加 129・削除 10）が変わりました。「Permission checks」の下に 3 つの h4、その後に 3 つの h3 と 4 つの h4 が加わり（詳細はハイライト 1 参照）、長く動くコードとカウントダウンのプロンプトの説明も v2.1.327・v2.1.328 の変更に合わせて改められました
- [**Error reference**](#2-error-reference) ([日本語](https://code.claude.com/docs/ja/errors#find-your-error) / [English](https://code.claude.com/docs/en/errors#find-your-error)):  
  72 行（追加 22・削除 50）が変わりました。「Find your error」に 9 行が加わり、3 つの節の本文が `remote-control` と `plugins/troubleshooting` の同じメッセージの節へのリンクに置き換わりました。「Request timed out」の対処も書き直されています
- [**Desktop application**](#3-desktop-application) ([日本語](https://code.claude.com/docs/ja/desktop#arrange-your-workspace) / [English](https://code.claude.com/docs/en/desktop#arrange-your-workspace)):  
  51 行（追加 30・削除 21）が変わりました。ペインの開き方がサイドパネルとタイトルバーのボタンの 2 通りで説明し直され、外部のサイトでの Claude の操作の承認と、SSH の接続を加える手順も改められました
<!-- light:updated-pages:end -->

**行数の数え方**: `llms-full.txt` の生の差分のハンクを、追加行は head 側、削除行は base 側の `Source:` 行でページに振り分けた値です。ページの並びは変わっていません。changelog（146 行）は新しい 1 リリースの分なので、これまでどおり「軽微な更新」で扱います。大幅更新の 3 ページに次いで多いのは `settings-reference` の 40 行（追加 20・削除 20）、`hooks` の 38 行（追加 21・削除 17）、`permissions` の 33 行（追加 25・削除 8）、`plugins/troubleshooting` の 32 行（追加 22・削除 10）で、どれも 50 行に届きません。

## 1. Run tool calls from code with Code Mode

**`code-mode` は 139 行（追加 129・削除 10）が変わり、`llms-full.txt` の中のページは 227 行から 346 行になりました。** 見出しは、「Permission checks」の下の h4「Require approval for a command」「Approve each piece of code first」「Answer a permission prompt while code runs」、h3「Limit shell commands with the sandbox」「Stop code in progress」「Check code output with a hook」、その下の h4「Read code output in the hook」「Redact code output」「Redact when your hook blocks or hits an error」「Move a check from a `UserPromptSubmit` hook」の 10 が加わり、外れたものはありません。`llms.txt` の説明文は変わっていません。

- **新しい見出し**: ハイライト 1 参照
- **「Code Mode limitations」**: 「Hooks」の項目から、`UserPromptSubmit` のフックがコードの出力をブロックすることがある、という部分が外れた
- **「Permission checks」**: 冒頭の段落が加わり（ハイライト 1 参照）、ルールとフックがツールの通常の名前で当てはまる例に、MCP のツールの名前が加わった。auto モードの項目は、分類器に繰り返し止められた後に自分で承認したコードの呼び出しのように、一部の呼び出しで確認を求められうる、となった（これまでは、前のコードの実行中に新しいコードが始まると確認を求められうる、としていた）。ほかのモードの項目からは「コードは確認なしに始まる」という部分が外れ、コードが返すものを確かめるには「Check code output with a hook」を見る、とも加わった
- **「Long-running code」**: Manual と `acceptEdits` のモードでは、ツールの許可のプロンプトで過ごした時間は 10 分に数えない（v2.1.328 より前は数えた）、となった。Claude がまだ待つ場合の項目では、`claude --resume` の一覧から選んだセッションは v2.1.328 より前のときだけの話になり、そのときは Claude Code を更新して同じ `claude --resume` のコマンドを Code Mode をオンにして実行し、版を保つなら `--resume` を `--continue` に替える、となった
- **「Permission prompt with a countdown」**: auto モードで、分類器に繰り返し止められた後に自分でコードを承認すると、そのコードと、まだ動いている前のコードのツールの呼び出しについて尋ねられうる、という説明になった（これまでは、Claude が前のコードの実行中に新しいコードを始めると、前のコードが分類器の確認を失う、としていた）。v2.1.327 より前は、分類器が新しいコードを許しても実行中のコードの残りの呼び出しについて尋ねられることがあったので、こうしたプロンプトを減らすには v2.1.327 以降に更新する、と加わった
- **「Code output withheld by a hook」**: コードの出力を期待したのに Claude の返答に `UserPromptSubmit operation blocked by hook` が出たら、`UserPromptSubmit` のフックが出力をプロンプトとして受け取って止めた、という説明になった。v2.1.328 以降はこのフックがコードの出力を受け取らないので、それより前の版では、先にチェックを `PostToolUse` のフックへ移してから更新するか、版を保つならフックの入力の `source` が `poll_event` のときにブロックしないようにする、となった
- **「Related resources」**: Hooks reference のリンクの説明が「`PreToolUse` と `UserPromptSubmit` のフック」から「`PreToolUse` と `PostToolUse` のフック」になった

changelog の v2.1.328 には、auto か bypass のモードの外で許可のプロンプト・計画の承認・質問が 10 分開いたままだと Code Mode がスクリプトを止める問題の修正と、`claude --resume` のピッカーで選んだセッションで Code Mode のスクリプトがバックグラウンドで実行されない問題の修正があります。v2.1.329 にも Code Mode の項目が 17 あり（下の「軽微な更新」）、そのうちの 1 つは、エラーになった `PreToolUse` のフックがスクリプトのツールの呼び出しを拒まないようにした変更です。head の「Tool call refused by a hook」は、`PreToolUse` のフックが判断を返さなければ `onFailure` が未設定でも呼び出しを拒む、と書いたままです。

- [Code Mode でコードからツール呼び出しを実行する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/code-mode#long-running-code)
- [Run tool calls from code with Code Mode - Claude Code Docs (English)](https://code.claude.com/docs/en/code-mode#long-running-code)
- [Code Mode でコードからツール呼び出しを実行する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/code-mode#code-output-withheld-by-a-hook)
- [Run tool calls from code with Code Mode - Claude Code Docs (English)](https://code.claude.com/docs/en/code-mode#code-output-withheld-by-a-hook)

## 2. Error reference

**`errors` は 72 行（追加 22・削除 50）が変わり、`llms-full.txt` の中のページは 6,812 行から 6,784 行になりました。** 見出しの出入りはありません。削除が多いのは、3 つの節の本文を、別のページの同じメッセージの節へのリンクに置き換えたためです。`llms.txt` の説明文は変わっていません。

- **「Find your error」に 9 行が加わった**: `Usage credits ran out before the response was finished.`（`costs` の「Add usage credits to your subscription」へ）、`Session failed: program not found:`（`remote-control` のプログラムのファイルがなくなったときの節へ）、`Warning: this sign-in` と `The refresh token in CLAUDE_CODE_OAUTH_REFRESH_TOKEN was used for this attempt`（ハイライト 2 参照）、`ENOTFOUND` と `In this cloud session a host fails to resolve like this`（「Host not allowed in a cloud session」へ）、`API Error: 400 Invalid effort level` / `Your organization limits effort for <model>, so Claude Code is using '<level>' instead of '<level>'`（`model-config` の「Organization effort limits」へ）、`was updated or removed, so this hook did not run`（`plugins/troubleshooting` の「`Plugin directory does not exist: <path>`」へ）、`Held a message from <sender>` / `Dropped the held message from <sender> without delivering it`（`cross-session-messaging` の「Control inbound messages」へ、`claude -p` なら「Non-interactive sessions」へ）、`blocking because onFailure is "block"`（ハイライト 3 参照）の 9 行です。ほかに 2 行が改められ、`Couldn't reconnect to your Remote Control session` の行のリンク先が `remote-control` の同じ節になり、Zed のキーマップの行に `Your Zed keymap is a symbolic link` が加わった
- **本文をリンクにした 3 つの節**: 「Couldn't reconnect to your Remote Control session」「Marketplace is registered from an untrusted source」「Plugin archive integrity check failed」は、原因と直し方を `remote-control` か `plugins/troubleshooting` の同じメッセージの節で見る、という 1 文になった。移った先の `remote-control` の節には、メッセージの全文の例と、前のセッションがなくなったとサーバーが報告したときはこのメッセージが出ない、という段落が加わった。`plugins/troubleshooting` の 2 つの節には、アーカイブのダイジェストが合わない 3 つの原因と、ローカルのディレクトリーのような GitHub か Git 以外のソースでは予約名の文が `can only be used with GitHub sources from the 'anthropics' organization` で終わること、`claude plugin marketplace add` も同じ確認をすること、が加わった。`Marketplace "<name>" is registered from an untrusted source` が出る場面も、「`/plugin` の **Errors** のタブか次の更新」から「シェルで `claude plugin marketplace update <name>` を実行したとき」になっている
- **「Request timed out」**: メッセージが `Request timed out` の後に続いて環境変数を名指すならその指示に従い、`No data arrived` はボディのアイドルタイムアウトが要求を終えたことを意味する、と加わった。遅いネットワークかプロキシで v2.1.328 より前の版なら `API_TIMEOUT_MS` を上げ、それでもタイムアウトするなら v2.1.328 以降に更新して次のタイムアウトのメッセージが名指す変数を設定し、更新できなければ `API_FORCE_IDLE_TIMEOUT` を `0` にする、となった。「How long a non-streaming attempt waits」のボディのアイドルタイムアウトの説明も、「動くところでは、既定で 5 分から 6 分」という言い方になった
- **「Tool input schema is invalid」**: エラーがまだ起きる場合が、機能フラグの取得がオンなのにフラグが届いていないとき（v2.1.328 より前は取得がオフでも起きた）と、`$schema` で draft 2020-12 以外の JSON Schema の方言を宣言したとき、の 2 項目になった。v2.1.216 より前はどの環境でも除外の確認を実行しなかった、という文は外れた
- **「/terminal-setup left your Zed keymap unchanged」**: `Your Zed keymap is a symbolic link, so it was left unchanged.`（`keymap.json` が別のファイルへのリンク）の項目が加わり、各メッセージがキーバインドのブロックで「終わる」は「それを含む」になった。`terminal-config` の「Enter multiline prompts」にも、キーマップがシンボリックリンクなら自分でキーバインドを加える、と加わった。changelog の v2.1.328 にある、Zed で `/terminal-setup` がシンボリックリンクの `keymap.json` を普通のファイルに置き換える問題の修正に追従した形です

- [エラーリファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/errors#find-your-error)
- [Error reference - Claude Code Docs (English)](https://code.claude.com/docs/en/errors#find-your-error)
- [エラーリファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/errors#request-timed-out)
- [Error reference - Claude Code Docs (English)](https://code.claude.com/docs/en/errors#request-timed-out)

## 3. Desktop application

**`desktop` は 51 行（追加 30・削除 21）が変わり、`llms-full.txt` の中のページは 2,480 行から 2,489 行になりました。** 見出しの出入りはありません。`llms.txt` の説明文は変わっていません。

- **「Arrange your workspace」**: ペインはヘッダーではなく、タブか上端のハンドルでドラッグして動かす、となった。ほかのペインを開くには、セッションの上部のアイコンにホバーして各ボタンの名前（**Terminal** や **Show side panel** など）を見て、持っているボタンに応じて操作する。**Show side panel** か **Hide side panel** なら、パネルを表示してパネルの一覧か **+** のメニューからペインを選び、**Terminal**・**Changes**（diff の表示）・**Browser**・**Files** なら、そのボタンをクリックする（ボタンがなければ横の **⋮** のメニューから選ぶ）。**Background tasks** と **Plan** は、セッションに表示するものができたら、サイドパネルか **⋮** のメニューから選ぶ。窓が狭いとボタンがメニューへ移る、という項目は外れた
- **各ペインの開き方**: Browser・diff の表示・ターミナル・バックグラウンドのタスクのペインを開く説明が、タイトルバーの **Browser**・**Changes**・**Terminal** をクリックする、**⋮** のメニューの **Background tasks** を選ぶ、から、「Arrange your workspace」の手順で選ぶ、という形になった。2 つ目のターミナルのタブは、ターミナルの上の **+** をクリックし、メニューが開いたら **Terminal** を選ぶ（チャットのフォルダーを右クリックして **Open in terminal** を選ぶ方法は外れた）。セッションの詳細のパネルにも、**Hide session rail** と **Show session rail** のどちらも見えなければタイトルバーの **Activity panel** をクリックする、と加わった
- **外部のサイト**（「Browse external sites」「Approve Claude's actions on a site」）: 安全の分類器が、入力のような外部のページでの Claude の書き込みの操作を確かめるのは、セッションで auto モードが使えるときになり、印を付けた操作は、モードを問わない許可のプロンプトではなく、ブロックされるか、繰り返しブロックされた後に確認を求める、となった。許可のカードは、Auto と Bypass permissions 以外のモードで、承認していない外部のサイトを Claude が使う前に出る、となり、サブドメインも個別の承認が要るという部分と、auto-verify がプロンプトなしに動き続けるという部分は外れた。「Open the preview at a specific URL」でも、ほかのアドレスは Claude がプレビューで開く新しいサイトと同じサイトの承認を通る、という言い方になった
- **「SSH sessions」**: **New environment** のダイアログで **SSH** のタブを選び、**Host** がボタンなら **Add SSH connection…** を選び、一覧なら一覧を開いて一番下の **Add SSH connection…** を選ぶ、という手順になった。**Name** は省略できるようになり、空なら **SSH host** の値を名前に使う
- **computer use**（「Enable computer use」「App permissions」）: computer use がオフのときに頼むと、設定でオンにすればできると Claude が伝える、という文が外れ、権限が拒まれていればその横の **Open System Settings** をクリックする、となった。アプリの権限の表の「Full control」は「Full access」に、対象も「Everything else」から「Most other apps」になった（`computer-use` の「Approve apps per session」も同じ言い方になり、警告の表の「Equivalent to shell access」は「Can run commands on your computer」に、「Can read or write any file」は「Can open, change, or delete any file, and run apps and scripts」になった）
- **HTML のプレビュー**: 「Turn off scripts in SSH and WSL previews for your organization」と「Managed settings」の表の `disableBrowserExternalNavigation`・`disableRemotePreviewScripts` の説明が、「Browser pane の」HTML のプレビューという言い方になり、`disableRemotePreviewScripts` は外部の閲覧をオフにせずにスクリプトだけをオフにする、となった。スクリプトを実行しないプレビューの通知が `This preview doesn't run scripts` で始まる、という文は外れた。`settings-reference` の「Settings index」と `disableRemotePreviewScripts`・`disableBrowserExternalNavigation` の節も同じ言い方になっている

関連して、`desktop-ios-simulator` にも h3「Open the simulator pane yourself」ができ、セッションにシミュレーターが接続されるか iOS のアプリの作業を Claude Code が検出したら、タイトルバーかサイドパネルで **iOS Simulator** を選ぶ、となりました（「Minimize or close the simulator pane」も、閉じたペインはこの節の手順で開き直す、となりました）。`claude-code-on-the-web` の「Review changes」と `web-quickstart` の「Review and iterate」も、隠れたパネルを表示するにはタイトルバーの **Activity panel** か **Show session rail**、またはバーの **⋮** のメニューの **Show session rail** をクリックし、**Changes** はペインとして開ける、となりました。

- [デスクトップアプリケーション - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/desktop#arrange-your-workspace)
- [Desktop application - Claude Code Docs (English)](https://code.claude.com/docs/en/desktop#arrange-your-workspace)
- [デスクトップアプリケーション - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/desktop#browse-external-sites)
- [Desktop application - Claude Code Docs (English)](https://code.claude.com/docs/en/desktop#browse-external-sites)

## 軽微な更新

<!-- light:minor-updates:start -->
今回の差分は **2 ファイル**（`llms-full.txt`・見出しマップ）で、`llms.txt` は変わっていません。`llms-full.txt` では、205 ページのうち **96 ページ**（changelog を含む）の内容が変わりました。大幅更新の 3 ページを除く **92 ページ**と、changelog に加わった **v2.1.329（2026年11月19日、130 項目。Added 7・Changed 22・Improvements 10・Bug fixes 91）** を以下にまとめます。単一のリリースなので、changelog の各項目への版の併記は省いています。changelog の収録リリースは 444 から 445 になり、先頭は v2.1.329 です。新着情報（whats-new）のページはありません。

`llms-full.txt` の総行数は **129,902 行から 130,257 行へ 355 行増え**ました（生の差分の差し引き 754 − 399 と一致）。生の差分 1,153 行の内訳は、changelog の新しいリリースが 146 行、大幅更新の 3 ページが 262 行（追加 181・削除 81）、残りの 92 ページが 745 行（追加 427・削除 318）です。この 745 行のうち 14 行は、`llms-full.txt` に 2 回載っている `plugins/install`・`plugins/create`・`plugins/mods/overview` の同じ変更が、2 か所目に出たものです。

コードフェンスの外の見出しは、行頭が `#` の見出しだけを数えると 6,160 から 6,176 へ、引用の中の見出しも数えると 6,171 から 6,187 へ、どちらも 16 増えました。加わったのは、`code-mode` の 10（ハイライト 1 参照）と、`authentication` の「Check when a stored login ends」、`permissions` の「Check the parameters Claude sends」、`plugins/dependencies` の「When a dependency installs automatically」、`plugins/cli-reference` の「Dependencies installed during a reload」、`desktop-ios-simulator` の「Open the simulator pane yourself」、`agent-sdk/subagents` の「Resume a subagent from your code」の 16 です。ほかに 3 つの見出しが改称されました（下の「その他」）。

**新機能**

- Code Mode の権限の確認・サンドボックス・コードの止め方・出力のフック（`code-mode`・`hooks`・`sandboxing`。詳細はハイライト 1 参照）
- 保存したログインの終わる日の確かめ方（`authentication`・`cli-reference`・`agent-sdk/typescript`・`errors`・`self-hosted-environments-testing`。詳細はハイライト 2 参照）
- `mcp_tool` のフックの `"onFailure": "block"`（`hooks`・`best-practices`・`errors`。詳細はハイライト 3 参照）
- `CLAUDE_CODE_SUBAGENT_EFFORT`・終わったサブエージェントの開き直し・`CLAUDE_CODE_SUBAGENT_HISTORY`（`sub-agents`・`env-vars`・`model-config`。詳細はハイライト 5 参照）
- **claude.ai のプラグインとスキルを扱うツールが `tools-reference` に載った**。`ListPlugins`（claude.ai のアカウントで有効なプラグインを一覧にする。クラウドのセッションかデスクトップアプリが要り、サードパーティのプロバイダーでは使えない）のほか、`ListSkills`・`SearchPlugins`・`SearchSkills`・`SuggestPluginInstall`（追加できるおすすめのプラグインのカードを示す）・`SuggestSkills` が `ListPlugins` と同じセッションで使えます。`propose_skills`（提案するスキルのカードを示し、claude.ai のアカウントに保存できる）は、クラウドの Cowork のセッションのような一部のクラウドのセッションで使えます。どれも許可は要りません。表の `EnterWorktree` の許可の列は「Yes」から「Some worktrees」になり、「Agent tool behavior」では、`tools` だけを設定したサブエージェントも `memory` を有効にすれば Read・Write・Edit を得る、と加わりました（`agent-sdk/subagents` の「Tool restrictions」も同じで、ツールを並べたサブエージェントは「それだけ」を得る、という書き方と、外したツールはセッションにまったくない、という文が外れました） — [日本語](https://code.claude.com/docs/ja/tools-reference#agent-tool-behavior) / [English](https://code.claude.com/docs/en/tools-reference#agent-tool-behavior)
- **プラグインのマニフェストに `network` のフィールドが加わった**（`plugins/manifest-reference` の「Fields」）。プラグインが接続するホストを `sandbox.network.allowedDomains` の構文で書き（`"network": { "hosts": ["api.example.com"] }`）、`claude plugin validate` がそれを一覧にします。どのホストも許しも止めもせず、v2.1.328 以降が要ります。`plugins/cli-reference` の「Output and exit codes」にも、validate の出力の `hosts`（`named` のホストと、ほかのホストに届きうる `unread` のプラグインの部分。一覧にできなければ `null`。プラグインは一覧にないホストにも届きうる。v2.1.328 以降）が加わりました — [日本語](https://code.claude.com/docs/ja/plugins/manifest-reference#fields) / [English](https://code.claude.com/docs/en/plugins/manifest-reference#fields)
- **プラグインの依存関係が自動で入る場合がまとまった**（`plugins/dependencies` の新しい h3「When a dependency installs automatically」・`plugins/cli-reference` の新しい h3「Dependencies installed during a reload」）。`claude plugin install` のほか、依存するプラグインを `claude plugin update` か `/plugin` の **Update now** で更新したときも、足りない依存関係が入る、と加わりました（非必須の通信がオフなら入らず、v2.1.319 以降が要る）。マーケットプレイスの自動更新でバンドルに加わった依存関係が入るのも v2.1.319 以降です。`/reload-plugins` では、解決できる依存関係が足りなければ Claude Code がそれを入れ、再読み込みが適用されれば要約に `(+ N dependencies: <names>) resolved` が出ます。適用されないか、要約に `installed but not applied` が出たら `/reload-plugins --force` を実行します。`plugins/troubleshooting` の「Dependency errors」には、`... still unresolved: <names>`（シェルで `claude plugin list` を実行し、各エラーを表の行に照らす）と、`Dependencies are not installed while non-essential traffic is turned off.`（`CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` が設定されているので、シェルで依存関係を 1 つずつ `claude plugin install` で入れる）の 2 行が加わりました。一方、`plugins/install` の「Install a plugin」は、スコープを選ぶと宣言した依存関係と一緒にプラグインを入れる、から、プラグインを入れる、だけになり、`plugins/cli-reference` の「plugin marketplace add」からも、追加すると入っていなかった依存関係を入れる、という文が外れています — [日本語](https://code.claude.com/docs/ja/plugins/dependencies#when-a-dependency-installs-automatically) / [English](https://code.claude.com/docs/en/plugins/dependencies#when-a-dependency-installs-automatically)、[日本語](https://code.claude.com/docs/ja/plugins/cli-reference#dependencies-installed-during-a-reload) / [English](https://code.claude.com/docs/en/plugins/cli-reference#dependencies-installed-during-a-reload)
- **セルフホストのランナーの新しいフラグとメトリクスがページに載った**（`self-hosted-environments-reference`・`self-hosted-environments-deploy`・`self-hosted-environments-configuration`・`cli-reference`）。`--repository-folder <owner>/<repo>=<folder>`（`--capacity 1` で、`checkout` のフックが用意しないリポジトリのクローンとして `<folder>` を使う。`--base-dir` の外のクローンも実際のパスで渡せ、ランナーはセッションごとにクローンの追跡するファイルをリセットする）、オーケストレーターの `--hook-label <label>=<values>`（セッションの `--metadata` のラベルを `CLAUDE_RUNNER_META_<LABEL>` としてフックに渡す。許す値以外の要求はセッションの起動を止める。`--min-idle 0` が要る）、`claude --environment` の `--metadata <key=value>` と `--correlation-id <id>`、Prometheus のメトリクス `claude_code_self_hosted_orchestrator_sessions_given_up_total{cause}` と `claude_code_self_hosted_orchestrator_session_queue_wait_by_reason_seconds{reason}` で、どれも v2.1.328 以降が要ります。`self-hosted-environments-deploy` の「Troubleshooting」にも、セッションが `This runner couldn’t use a folder on its machine` で始まらないときの項目が加わりました。changelog の v2.1.328 にあるこれらの追加と、`--correlation-id` がフックに届かない問題の修正に、ページが追従した形です — [日本語](https://code.claude.com/docs/ja/self-hosted-environments-reference#runner-cli-flags) / [English](https://code.claude.com/docs/en/self-hosted-environments-reference#runner-cli-flags)、[日本語](https://code.claude.com/docs/ja/self-hosted-environments-deploy#reuse-a-pre-warmed-checkout) / [English](https://code.claude.com/docs/en/self-hosted-environments-deploy#reuse-a-pre-warmed-checkout)
- **`CLAUDE_CODE_DISABLE_DEFERRED_TOOL_RESUME` が `env-vars` に載った**。`-p` で再開か続行するとき、保留したツールの呼び出しを飛ばす変数です。Claude はその呼び出しを繰り返せます。設定の `env` のブロックでは無視され、v2.1.328 以降が要ります（changelog の v2.1.328 にある追加） — [日本語](https://code.claude.com/docs/ja/env-vars#variables) / [English](https://code.claude.com/docs/en/env-vars#variables)
- **`CLAUDE_CODE_LOOP_KEEPALIVE` が `env-vars` に載った**。対話の自己ペースの `/loop` の 2 回目以降の反復が何も予定せずに終わったとき、もう 1 回反復する変数です。`scheduled-tasks` の「Stop a loop」も、自己ペースのループは Claude が次を予定せずに反復を終えると止まることがあり、約 20 分後の 1 回の追加の反復はこの変数を見る、となりました（これまでは、Claude Code が約 20 分後に 1 回のフォールバックの起床を予定する、としていました）。`goal` の比較の表でも、`/loop` が止まるのは「Claude が作業を終えたと判断したとき」から「ループが自ら終わるとき」になっています — [日本語](https://code.claude.com/docs/ja/scheduled-tasks#stop-a-loop) / [English](https://code.claude.com/docs/en/scheduled-tasks#stop-a-loop)
- **`permissions` に h4「Check the parameters Claude sends」ができた**。Claude がツールに送るパラメーターの名前と値を見るには、シェルで `stream-json` の出力と、そのツールを呼ぶプロンプトで `claude -p` を実行し（例は `claude -p "Use a subagent on Opus to list the test files" --output-format stream-json --verbose`）、`name` がそのツールの `tool_use` のブロックの `input` を見ます。「Match by input parameter」の、`--verbose` で実行すると各ツールの呼び出しのパラメーターがわかる、という項目はこの h4 に替わりました — [日本語](https://code.claude.com/docs/ja/permissions#check-the-parameters-claude-sends) / [English](https://code.claude.com/docs/en/permissions#check-the-parameters-claude-sends)
- **`--add-dir` で加えるフォルダーの信頼の確認が載った**（`permissions` の「Working directories」・`plugins/loading` の「Enabled in an `--add-dir` directory but not loaded」・`self-hosted-environments-configuration`）。対話のターミナルのセッションで `claude --add-dir` か `/add-dir` を使い、ワークスペースの信頼が及ばないフォルダーを加えると、先に信頼するよう尋ねる（v2.1.326 以降）、という注記が加わりました。加えたディレクトリーの信頼を保存するまで、Claude Code はその `extraKnownMarketplaces` を飛ばし、対話のターミナルのセッションでは `true` の `enabledPlugins` も飛ばします（v2.1.319 以降）。`--add-dir` のプロンプトに答えても信頼は保存されないので、そのディレクトリーでセッションを始めて信頼のダイアログを受け入れるか、信頼のキーを自分で設定します。プルリクエストのワークツリーの中のディレクトリーは信頼しても飛ばされうるので、メインのチェックアウトのコピーを渡す、という注記もあります。`self-hosted-environments-configuration` の「Repository settings in sessions with several repositories」にも、`--trust-workspace false` でランナーを始めると両方のキーを飛ばす（`enabledPlugins` を飛ばすのは v2.1.323 以降）、と加わりました — [日本語](https://code.claude.com/docs/ja/plugins/loading#enabled-in-an-add-dir-directory-but-not-loaded) / [English](https://code.claude.com/docs/en/plugins/loading#enabled-in-an-add-dir-directory-but-not-loaded)、[日本語](https://code.claude.com/docs/ja/permissions#working-directories) / [English](https://code.claude.com/docs/en/permissions#working-directories)
- **mod の UI の要素に新しい props が載った**（`plugins/mods/interface` の「Build a tree from elements」）。`Box` に `overflowX`、`Text` に `maxLines` が加わり、`wrap` の値に `'clip'` が加わりました。どれも v2.1.326 以降が要ります — [日本語](https://code.claude.com/docs/ja/plugins/mods/interface#build-a-tree-from-elements) / [English](https://code.claude.com/docs/en/plugins/mods/interface#build-a-tree-from-elements)
- **アーティファクトの監視が止まったときのメッセージが載った**（`artifacts` の「Let Claude reply to comments on its own」）。活動のない監視が止まると `Stopped watching Artifact: <name> (idle)` が出ます。`(idle)` の代わりに `(made room for a newer watch)` が出たら、セッションが 25 の監視の上限に達したので、公開し直してその監視を始め直します — [日本語](https://code.claude.com/docs/ja/artifacts#let-claude-reply-to-comments-on-its-own) / [English](https://code.claude.com/docs/en/artifacts#let-claude-reply-to-comments-on-its-own)
- **`web-quickstart` にリポジトリなしで始める方法が載った**（「Start a task」）。claude.ai/code でリポジトリなしに始めるには、リポジトリの選択で **No repository** を選びます — [日本語](https://code.claude.com/docs/ja/web-quickstart#start-a-task) / [English](https://code.claude.com/docs/en/web-quickstart#start-a-task)
- **組織の effort の上限に当たったときの対処が載った**（`model-config` の「Organization effort limits」）。`Your organization limits effort for <model>` が出て高いレベルが要るなら、組織の管理者に上限を上げてもらって Claude Code を再起動します。要求が `API Error: 400 Invalid effort level` で失敗するなら v2.1.314 以降に更新して再起動し、それでも失敗するなら `CLAUDE_CODE_EXTRA_BODY` から `output_config.effort` のキーを外します（`errors` の表にもこの 2 つのメッセージの行が加わりました） — [日本語](https://code.claude.com/docs/ja/model-config#organization-effort-limits) / [English](https://code.claude.com/docs/en/model-config#organization-effort-limits)
- **再開のときに渡し直すフラグにツールのアクセスが加わった**（`sessions` の「Flags to pass again when you resume」）。`--tools`・`--allowedTools`・`--disallowedTools` です — [日本語](https://code.claude.com/docs/ja/sessions#flags-to-pass-again-when-you-resume) / [English](https://code.claude.com/docs/en/sessions#flags-to-pass-again-when-you-resume)
- フォルダーのフックがどこで宣言されているかを述べる警告を、信頼のダイアログに追加
- Claude Desktop とほかの対話でないホストで、managed settings のフックを読み込めないときの会話の中の警告を追加
- このセッションのスケジュールされたタスク・`/loop` の起床・ゴール・この会話のフォークを `/tasks` に追加。`x` で、確かめた後に 1 つを止めます
- 接続を拒むリモートの HTTP の MCP サーバーの JSON-RPC のエラーメッセージを示す「Server message」の行を、`/mcp` のサーバーのページに追加
- 自動の更新を受けない managed のマーケットプレイスとその理由を示す「Marketplace auto-update」の行を `/status` に追加
- OpenTelemetry のイベントとメトリクスが有効なまま Code Mode をオンにできるよう対応。コードの各ツールの呼び出しがイベントを送ります。トレースが有効なら、引き続き Code Mode はオフのままです
- [VSCode] 信頼のプロンプトを断った後、ウィンドウを再読み込みせずにプロンプトを戻せる Review trust 付きの行を、メッセージの欄の上に追加

**機能改善**

- 設定のリストが上書きされずに合わさること（`cli-reference`・`agent-sdk/configuration`・`agent-sdk/python`・`agent-sdk/typescript`・`managed-settings`・`server-managed-settings`・`settings-reference`。詳細はハイライト 4 参照）
- `errors` の「Find your error」の 9 行と、`remote-control`・`plugins/troubleshooting` へ移した 3 つの節（詳細は大幅更新 2 参照）
- Desktop のペインの開き方と外部のサイトの承認（`desktop`・`desktop-ios-simulator`・`claude-code-on-the-web`・`web-quickstart`・`computer-use`・`settings-reference`。詳細は大幅更新 3 参照）
- **機能フラグの取得がオフでも MCP のツールのスキーマの書き換えと確認が動く、という書き方になった**（`mcp` の「Tool input schemas with a root-level combinator」「Tools with invalid input schemas」・`env-vars` の「Features that need feature-flag fetching」・`terminal-config` の「How Claude treats pasted text」）。ルートに結合子を持つ入力のスキーマのツールが飛ばされるのは、API が受け付けるスキーマを作れないときか、機能フラグの取得がオンなのにフラグが届いていないとき（インストールか更新の後の最初のセッションなど）になり、v2.1.328 より前は取得がオフでも飛ばされた、となりました。規則を破る入力のスキーマのツールが除かれずに残るのも、取得がオンなのにフラグが届いていないときだけになり、v2.1.328 より前は取得がオフでも除かれなかった、となっています。`env-vars` の機能フラグの取得が要る機能の一覧からは、大きな貼り付けを貼り付けとして扱うことと、API が拒むスキーマの MCP のツールを除くことの 2 項目が外れ、`terminal-config` も、貼り付けは、インストールの後の最初のセッションのように印なしで Claude に届くことがある、となりました。changelog の v2.1.328 にある、サードパーティのプロバイダーか、テレメトリーか機能フラグがオフのときの MCP のツールの 2 つの修正と、貼り付けたテキストに印を付ける変更に、ページが追従した形です（`errors` の「Tool input schema is invalid」は大幅更新 2 参照） — [日本語](https://code.claude.com/docs/ja/mcp#tools-with-invalid-input-schemas) / [English](https://code.claude.com/docs/en/mcp#tools-with-invalid-input-schemas)
- **ボディのアイドルタイムアウトの説明が改められた**（`network-config` の「Streaming idle watchdogs」・`claude-apps-gateway-deploy`）。v2.1.328 以降では、`CLAUDE_STREAM_IDLE_TIMEOUT_MS` に 5 分より長い値を設定すると、ボディのアイドルタイムアウトも最大 30 分まで延びる、と加わりました。そのほかの接続の要求が 5 分から 6 分で終わるのは「既定で」となり、表のボディのアイドルタイムアウトの条件からも「5 分間」が外れています。`claude-apps-gateway-deploy` の「Retry an unanswered request sooner with the first-byte deadline」も「既定で」5 分から 6 分待ちうる、となり、再試行を早めるためだけに下げた `API_TIMEOUT_MS` は外す、という助言は、`API_TIMEOUT_MS` をボディのアイドルタイムアウトより十分大きく保つ、になりました。「Pick a value」からは、完全に黙った接続は 5 分から 6 分で終わる、という文が外れています。changelog の v2.1.328 にある、ゲートウェイ・カスタムのベース URL・クラウドのプロバイダーで `CLAUDE_STREAM_IDLE_TIMEOUT_MS` が 5 分の接続の上限を延ばさない問題の修正に追従した形です — [日本語](https://code.claude.com/docs/ja/network-config#streaming-idle-watchdogs) / [English](https://code.claude.com/docs/en/network-config#streaming-idle-watchdogs)
- **Manual（`default`）モードで承認なしに動くものの書き方が改められた**（`permission-modes` の「Available modes」「Common setups」・`permissions` の「Permission modes」・`settings-reference` の `permissions.defaultMode`）。`default` で確認なしに動くのは「読み取りだけ」ではなく、「作業ディレクトリーの中のファイルの読み取りと、サブエージェントを始めるような承認の要らないほかの操作」になり、`permissions` の表でも「各ツールの最初の使用で許可を求める」から「ほとんどの編集・シェルのコマンド・ネットワークの要求の前に確認を求める」になりました。「Common setups」の行の名前も「Review every action yourself」から「Answer permission prompts yourself」になり、Manual という名前がどこで使われるかを述べた段落は、`manual` を `default` の別名として受け付ける、という文だけになっています — [日本語](https://code.claude.com/docs/ja/permission-modes#available-modes) / [English](https://code.claude.com/docs/en/permission-modes#available-modes)
- **`dontAsk` モードの説明が項目に分けられた**（`permission-modes` の「Allow only pre-approved tools with dontAsk mode」）。プロンプトが出るはずのところで拒まれる呼び出しが、`ask` ルール・`AskUserQuestion`・組織が `ask` にしたコネクターのツール・`requiresUserInteraction` の印の付いた MCP のツールの 4 項目に分けられ、mod 自身が行うツールの呼び出しを止めるのに `dontAsk` に頼らない、と加わりました。セッションが入力を待たない、という部分は外れています。`agent-sdk/python` と `agent-sdk/typescript` の `PermissionMode` のコメントも「プロンプトが出るはずの呼び出しを拒む」になりました — [日本語](https://code.claude.com/docs/ja/permission-modes#allow-only-pre-approved-tools-with-dontask-mode) / [English](https://code.claude.com/docs/en/permission-modes#allow-only-pre-approved-tools-with-dontask-mode)
- **auto モードと最初の読み取りの説明が改められた**（`permission-modes` の「The first read outside the working directories」「Boundaries you state in conversation」「How auto mode evaluates actions」・`permissions` の「Block file-tool reads and writes outside the working directories」）。作業ディレクトリーの外の最初の読み取りのプロンプトが出ないのは、`-p` の実行とバックグラウンドのセッションに加えて、Agent SDK のセッション・VS Code のチャットのパネル・デスクトップアプリでもあり、そこでは読み取りが実行される、となりました。`permissions.blockReadsOutsideWorkingDirectories` をオンにするよう auto モードが「申し出る」は「申し出ることがある」になっています。会話で述べた境界で分類器が止めるのは「分類器が確かめる」操作、と限定され、サーバー側の分類器の確認の下ではクリーンな作業ツリーでも `git reset --hard` が止められうる、という注意からは、auto モードが最近操作を止めていない限り Claude Code が `git status` を飛ばしうるから、という理由が外れました（changelog の v2.1.329 には、auto モードが `git status` を実行する回数を減らした変更があります） — [日本語](https://code.claude.com/docs/ja/permission-modes#how-auto-mode-evaluates-actions) / [English](https://code.claude.com/docs/en/permission-modes#how-auto-mode-evaluates-actions)
- **`Read` と `Edit` の deny ルールが及ぶ範囲が改められた**（`permissions` の「What `Read` and `Edit` rules cover」）。Bash のコマンドでは、Claude Code が解析できるコマンドに限って、リダイレクトの対象と `cat`・`head`・`tail`・`sed`・`tee` のような認識するファイルのコマンドに及ぶ、となりました。OS のレベルの強制のためにサンドボックスを有効にする、という助言も、サンドボックスの中のシェルのコマンドに対するもので、サンドボックスの外での再試行もオフにする、となっています。同じページの「Permission system」の表では、ファイルの変更に承認が要らない例外として Claude Code 自身の計画と auto memory のファイルが挙がり、「Precedence among rules, hooks, and mods」には、mod 自身が行うツールの呼び出しを止めるのに権限のルールに頼らない、と加わりました — [日本語](https://code.claude.com/docs/ja/permissions#what-read-and-edit-rules-cover) / [English](https://code.claude.com/docs/en/permissions#what-read-and-edit-rules-cover)
- **再開のときに戻るスケジュールされたタスクの説明が改められた**（`scheduled-tasks` の「Limitations」・`sessions` の「What a resumed session restores」・`tools-reference`・`agent-sdk/typescript` の「CronCreate」・`common-workflows` の「Run Claude on a schedule」）。`scheduled-tasks` には、ターンの合間に `Exit and stop tasks` を選んで終了するとセッションのタスクを失う、と加わり、`sessions` も、期限の切れていないタスクが戻る、から、例外を除いて戻る、になりました。`tools-reference` の `CronCreate`、`agent-sdk/typescript` の `CronCreate`、`common-workflows` の `/loop` の行からは、`--resume` と `--continue` で期限の切れていないタスクやループが戻る、という説明が外れています。changelog の v2.1.329 には、保存したスケジュールされたタスクの扱いと「Exit and stop tasks」の変更があります — [日本語](https://code.claude.com/docs/ja/scheduled-tasks#limitations) / [English](https://code.claude.com/docs/en/scheduled-tasks#limitations)
- **セッションのピッカーの説明が改められた**（`sessions` の「Use the session picker」）。キーの表から `→` / `←`（まとめたセッションを開く・閉じる）と `1` から `9`（その位置のセッションを再開する）の行が外れ、検索に入る文字の例外からも数字が外れました。各行のラベルは、付けた名前・AI が作ったセッションの題・会話の要約・プロンプトのいずれかのうち最初にあるもの、となり、最終の活動からの時間・git のブランチ・ファイルの大きさを示す、という部分と、同じセッションの複数の項目を 1 行にまとめる説明、`claude --resume` のピッカーで選んだセッションを読み込めないときの説明は外れています — [日本語](https://code.claude.com/docs/ja/sessions#use-the-session-picker) / [English](https://code.claude.com/docs/en/sessions#use-the-session-picker)
- **Agent SDK の `skills` のオプションはメインのエージェントのスキルを絞る、という書き方になった**（`agent-sdk/claude-code-features` の「Skills」・`agent-sdk/skills`・`agent-sdk/python` と `agent-sdk/typescript` の `skills`）。`skills` はセッションではなくメインのエージェント（メインの会話）が呼べるスキルを決め、一覧を絞ってもサブエージェントは絞られない、となりました。`skills` を設定すると SDK が `allowedTools` に Skill のツールを自動で加える、という説明は、`agent-sdk/skills` では「有効にしたスキルを加える」になり、ほかのページからは外れています — [日本語](https://code.claude.com/docs/ja/agent-sdk/skills#allow-only-specific-skills) / [English](https://code.claude.com/docs/en/agent-sdk/skills#allow-only-specific-skills)
- **Agent SDK のフックが `{}` を返す意味が改められた**（`agent-sdk/claude-code-features` の「Hooks」・`agent-sdk/hooks` の「How hooks work」「Outputs」）。`PreToolUse` で `{}` を返すのは「ツールを進めてよい」ではなく「判断をしない」で、通常の権限の流れが当てはまる、となり、コードの例のコメントも同じ言い方になりました。Windows の `C:\project\.env` への呼び出しも、フックが「許す」ではなく「止めない」になっています。関連して、`agent-sdk/user-input` の「Detect when Claude needs input」は、権限の流れがまだ承認も拒否もしていない呼び出しで承認が要る、となり、`agent-sdk/permissions`・`agent-sdk/agent-loop`・`agent-sdk/custom-tools`・`agent-sdk/configuration`・`agent-sdk/hosting` も言い方が改められました — [日本語](https://code.claude.com/docs/ja/agent-sdk/hooks#outputs) / [English](https://code.claude.com/docs/en/agent-sdk/hooks#outputs)
- **`agent-sdk/subagents` の「Resume subagents」に h3「Resume a subagent from your code」ができた**。プログラムからの再開の説明がこの h3 の下に入り、組み込みの `Explore` と `Plan` のエージェントは `agentId` を「返さない」から「テキストから外すことがある」になりました。`sub-agents` の「Resume subagents」も同じ言い方です。「AgentDefinition configuration」の `tools` には、並べても事前に承認したことにはならない、と加わり、プログラムの定義の例の `allowedTools` にも `Bash(npm test *)` が加わっています — [日本語](https://code.claude.com/docs/ja/agent-sdk/subagents#resume-a-subagent-from-your-code) / [English](https://code.claude.com/docs/en/agent-sdk/subagents#resume-a-subagent-from-your-code)
- **サブエージェントのツールの呼び出しの数から `SubagentHandback` が外れると明記された**（`hooks` の「Agent」の `totalToolUseCount`・`monitoring-usage` の「Subagent completed event」の `total_tool_uses`・`agent-sdk/python` の「Agent」） — [日本語](https://code.claude.com/docs/ja/monitoring-usage#subagent-completed-event) / [English](https://code.claude.com/docs/en/monitoring-usage#subagent-completed-event)
- **`hooks` のいくつかの説明が改められた**（「Exit code output」「Exit code 2 behavior per event」「UserPromptSubmit decision control」「What a blocked prompt leaves behind」「Stop input」「WorktreeRemove」「ElicitationResult output」）。終了コードの出力の表で、プレーンテキストか何もない出力の非ブロックのエラーの通知が標準エラーの最初の行を含む、という部分が外れました。ブロックしたプロンプトは「Claude に届かない」という説明が表・`decision`・「What a blocked prompt leaves behind」から外れ、`decision` は「プロンプトを拒む」になっています。「Stop input」の `command` は、`shell` のタスクに加えて、コマンドを実行する `monitor` のタスクにも出る、となりました（changelog の v2.1.329 にある、Stop と SubagentStop のフックが Monitor のスクリプトを `monitor` と示すようにした変更）。`WorktreeRemove` は、`claude remote-control` の後始末ではフックがプロンプトなしに動き、Claude にフックが作ったワークツリーの削除を頼んでも、`discard_changes: true` を渡さない限り `ExitWorktree` は拒む、という言い方になりました。`ElicitationResult` の `cancel` からは、ユーザーが送った値が一緒に渡る、という部分が外れています — [日本語](https://code.claude.com/docs/ja/hooks#what-a-blocked-prompt-leaves-behind) / [English](https://code.claude.com/docs/en/hooks#what-a-blocked-prompt-leaves-behind)
- **スキルの `paths` の基準の説明が改められた**（`skills` の「Frontmatter reference」「Skill not triggering」「Edit a skill during a session」・`large-codebases`）。`paths` のパターンは Claude の今の作業ディレクトリーからの相対で、メインの会話では、同じ Git のワークツリーの中のサブディレクトリーへ `cd` した後も主の作業ディレクトリーからの相対のまま、と加わり、パターンはその基準のディレクトリーの中のファイルにだけ一致する、となりました。パターンに一致するファイルを扱うとき「だけ」スキルを読み込む、の「だけ」は `skills` と `large-codebases` の両方で外れています。セッションの開始時になかったスキルのディレクトリーを作ったときの説明は、新しいスキルが出なければ `/reload-skills` を実行する、だけになりました — [日本語](https://code.claude.com/docs/ja/skills#frontmatter-reference) / [English](https://code.claude.com/docs/en/skills#frontmatter-reference)
- **`remote-control` のいくつかの説明が改められた**（「Requirements」「Enable Remote Control for all sessions」「Auto-connect with `DISABLE_TELEMETRY` or `DO_NOT_TRACK` set」「Remote Control is disabled by your organization's policy」「Couldn't verify your organization's policy for remote control」「The program file this Remote Control started from is gone」）。`/config` の **Enable Remote Control for all sessions** の値は `true` / `false` から **`on`** / **`off`** になりました。資格のあるログインなしの `claude --remote-control` は、Remote Control がオフの対話のセッションを始める、となり、組織のカスタムロールが足りないときの `Remote Control is disabled by your organization's policy` は `/remote-control` で出る、となっています。エラーが `disableRemoteControl` を名指すなら設定ファイルからそのキーを外し、managed settings にあるなら管理者に尋ねる（サインインや組織のトグルを変えても役に立たない）、となりました。組織のポリシーを確かめられないときのメッセージは、次にすることが続く形になり、メッセージがそう言うなら Claude Code を再起動してから再び実行する、となっています。プログラムのファイルがなくなったときのエラーの例に `Session failed: program not found:` が加わりました（大幅更新 2 も参照） — [日本語](https://code.claude.com/docs/ja/remote-control#enable-remote-control-for-all-sessions) / [English](https://code.claude.com/docs/en/remote-control#enable-remote-control-for-all-sessions)
- **プラグインのコマンドの成功の行から `Successfully` が外れることが載った**（`plugins/cli-reference` の「claude plugin commands」・`plugins/install`・`plugins/create-marketplace`・`plugins/troubleshooting`）。ターミナルでは成功の行が `Installed plugin:` のように `Successfully` を省き、標準出力か標準エラーがターミナルでないときは `Successfully` が残ります。各ページの出力の例も `Installed plugin:`・`Added marketplace:`・`Updated marketplace:` になりました — [日本語](https://code.claude.com/docs/ja/plugins/cli-reference#claude-plugin-commands) / [English](https://code.claude.com/docs/en/plugins/cli-reference#claude-plugin-commands)
- **プラグインを更新した後に `/reload-plugins` を実行する、という書き方になった**（`plugins/install` の「Keep plugins updated」・`plugins/loading` の「When auto-update runs」「Check which stage a plugin reached」）。`Plugin updated: <name> · Run /reload-plugins to apply` が出たらそのセッションで `/reload-plugins` を実行し、再読み込みしてもしなくても次の起動で新しい版が読み込まれる、となりました。`plugins/loading` も、`/plugin` のパネルの外でプラグインを入れる・更新する・有効にする・無効にした後は `/reload-plugins` を実行するか新しいセッションを始める、となり、`claude plugin update` が `Restart to apply changes.` で終わる、という部分は外れています。同じページの「Find plugins on disk」には、`synced/` と `.trash/` は `CLAUDE_CODE_PLUGIN_CACHE_DIR` を設定しても `~/.claude/plugins` の下に残る、と加わりました — [日本語](https://code.claude.com/docs/ja/plugins/install#keep-plugins-updated) / [English](https://code.claude.com/docs/en/plugins/install#keep-plugins-updated)
- **プラグインのフォルダーの読み込みで、名前が `.` で始まるサブフォルダーは読み込まれない、と明記された**（`plugins/create` の「Load a folder of plugins」・`plugins/dependencies` の「Test a plugin and its dependency locally」・`plugins/cli-reference` の「Flags that load a plugin for one session」）。読み込まないときは、サブフォルダーの名前とマニフェストを確かめる、となりました。`plugins/dependencies` と `plugins/cli-reference` の `--plugin-dir` の説明も、この節へのリンクになっています — [日本語](https://code.claude.com/docs/ja/plugins/create#load-a-folder-of-plugins) / [English](https://code.claude.com/docs/en/plugins/create#load-a-folder-of-plugins)
- **組織向けの mod の管理の説明が改められた**（`plugins/mods/admin` の「Stop user-installed mods from loading」「Know which hooks of a user's mod don't run」「Decide whether to leave mods on」「Choose how much to allow」「Set options on the built-in guard」）。ガードが飛ばすユーザーの mod のフックの表に、OpenTelemetry のコレクターへ向かう記録 `telemetry.log`（v2.1.328 以降）が加わりました。「Decide whether to leave mods on」には、どの設定でもユーザーは claude.ai から同期したプラグインの mod と、許可リストが `skills-dir` を外していない限りスキルのディレクトリーのプラグインの mod を読み込める、と加わり、「Choose how much to allow」の、承認したマーケットプレイスの mod だけを許す行は、claude.ai の外のマーケットプレイスの場合として、`skills-dir` のない許可リスト・`disableSideloadFlags` の `true`・`syncClaudeAiPlugins` の `false` の 3 つを設定する、となりました。managed settings 以外のファイルのオプションを無視する、という項目の言い方も改められています — [日本語](https://code.claude.com/docs/ja/plugins/mods/admin#choose-how-much-to-allow) / [English](https://code.claude.com/docs/en/plugins/mods/admin#choose-how-much-to-allow)
- **クラウドのセッションの隔離の書き方が改められた**（`claude-code-on-the-web` の冒頭と「Security and isolation」・`security` の「Cloud execution security」・`sandbox-environments` の「Compare sandboxing approaches」「Cloud sessions」・`cloud-environments` の「Security proxy」「Limitations in cloud sessions」・`settings` の「Settings in cloud sessions」・`web-quickstart` の冒頭）。既定では、クラウドのセッションはシェルのコマンドとファイルの編集を Anthropic が管理する隔離された VM で実行する、という言い方になり、「Isolated virtual machines」の項目は冒頭の文に入りました。`claude-code-on-the-web` からは「Secure analysis」の項目が外れ、`sandbox-environments` の表の Cloud sessions の行も、「Anthropic がホストする完全な OS」から「既定で、Anthropic がホストする VM の中のシェルのコマンドとファイルの編集」になっています。プロキシを通るのも「セッションの VM からの」外向きの通信、となりました。`claude-code-on-the-web` の「Unable to get organization UUID」では、`claude --teleport` のピッカーのメッセージが `Couldn't load cloud sessions` になり、v2.1.328 より前は `Couldn't load Claude Code sessions` か `Error loading Claude Code sessions` だった、と加わり、v2.1.274 から v2.1.289 のサインインのメッセージの段落は外れています — [日本語](https://code.claude.com/docs/ja/claude-code-on-the-web#security-and-isolation) / [English](https://code.claude.com/docs/en/claude-code-on-the-web#security-and-isolation)
- **bare モードの説明が改められた**（`headless` の「Start faster with bare mode」・`best-practices` の「Run Claude from a script」・`glossary` の「Bare mode」）。`--bare` が飛ばすのは「あなたの」フック・スキル・プラグインなどで、bare モードでも Claude Code は設定ファイルとその権限のルールを読み、`~/.claude/settings.json` のフックとプロジェクトの `.mcp.json` の MCP サーバーは動かない、となりました。どのマシンでも同じ結果になる、という説明は 3 ページとも外れています — [日本語](https://code.claude.com/docs/ja/headless#start-faster-with-bare-mode) / [English](https://code.claude.com/docs/en/headless#start-faster-with-bare-mode)
- **managed settings の届き方の説明が改められた**（`managed-settings` の「How Claude Code combines managed sources」・`model-config` の「Surface coverage」「Organization model restrictions」「Pin models for third-party deployments」・`llm-gateway-rollout` の「Distribute through managed settings」・`feature-availability` の「Admin and analytics」）。リモートの設定を取得する条件が 3 項目に分けられ、プロバイダーか `ANTHROPIC_BASE_URL` を設定したなら、マシンで取得の結果を確かめてこのソースが飛ばされるかを見る、となりました（これまでは、ほかのプロバイダーか `ANTHROPIC_BASE_URL` が Anthropic の API 以外を指すなら次のソースから始める、としていました）。`model-config` の「Surface coverage」「Pin models for third-party deployments」と `llm-gateway-rollout` からは、サードパーティのプロバイダーやゲートウェイを通るセッションには server-managed settings が届かない、という文が外れ、`llm-gateway-rollout` からは、managed の `ANTHROPIC_BASE_URL` は開発者のシェルの export で上書きできない、という文も外れました。`feature-availability` でも、`ANTHROPIC_BASE_URL` が `api.anthropic.com` 以外を指すと Claude Code がオフにする機能の例から server-managed settings が外れています。`model-config` の組織のモデルの制限は、ゲートウェイの認証情報のときも `availableModels` を使う、となりました — [日本語](https://code.claude.com/docs/ja/managed-settings#how-claude-code-combines-managed-sources) / [English](https://code.claude.com/docs/en/managed-settings#how-claude-code-combines-managed-sources)
- **`CLAUDE_CODE_DISABLE_THINKING` の対象が明記された**（`env-vars`）。`thinking` のパラメーターを外すのは、メインの会話のターン・サブエージェントのターン・コンパクションの要約の API の要求で、考えることをオフにできないモデルの説明は `model-config` の「Where you can't turn thinking off」へのリンクになりました — [日本語](https://code.claude.com/docs/ja/env-vars#variables) / [English](https://code.claude.com/docs/en/env-vars#variables)
- **`opusplan` と `[1m]` の説明が短くなった**（`model-config` の「`opusplan` model setting」「Pin models for third-party deployments」）。`opusplan` の各段階がどのモデルの設定と同じコンテキストウィンドウを使うかの説明が外れ、既定で 1M を持たないところで両方の段階に 1M を求めるには `opusplan[1m]` にする、だけになりました。`[1m]` の接尾辞も、固定した別名が 1M のコンテキストウィンドウで動く、だけになっています — [日本語](https://code.claude.com/docs/ja/model-config#opusplan-model-setting) / [English](https://code.claude.com/docs/en/model-config#opusplan-model-setting)
- **`cli-reference` のフラグの説明が改められた**（「CLI flags」）。`--allow-dangerously-skip-permissions` は、対話のターミナルのセッションで `bypassPermissions` がモードの循環にある間、plan モードで Claude が試みるほとんどの編集とコマンドが計画の承認の前にプロンプトなしに動く、という説明になり、例も `--permission-mode plan` から `--permission-mode default` になりました（`--settings` はハイライト 4、`--metadata` と `--correlation-id` は上の「新機能」参照） — [日本語](https://code.claude.com/docs/ja/cli-reference#cli-flags) / [English](https://code.claude.com/docs/en/cli-reference#cli-flags)
- **`settings-reference` のいくつかのキーの説明が改められた**。`attribution.sessionUrl` は、Claude Code がリンクを付けるのではなく、リンクを付けるよう Claude に伝える、となりました。`agentPushNotifEnabled` と `inputNeededNotifEnabled` の既定は `false` から「未設定で、アカウントに保存した値を使う」になり、`allowedChannelPlugins` の空の配列は、`--dangerously-load-development-channels` で読み込まない限りすべてのチャネルのプラグインを止める、となっています。`enableAllProjectMcpServers` の `false` と既定は、対話のターミナルのセッションが保留中のサーバーごとに承認を求める、となり、`disableRemoteControl` からは、組織のポリシーがオフにしたと報告する、という部分が外れました。`injectHosts` を持たない変数で許可するすべてのホストに本当の値を入れるのは「ほとんどの」変数、`sandbox.credentials.awsPairs` のプロキシは `injectHosts` のホストで要求を「再署名できる」、という言い方になっています（`sandboxing` の「Mask credentials」も「ほとんどの」`mask` の項目、という言い方になりました） — [日本語](https://code.claude.com/docs/ja/settings-reference#attribution-sessionurl) / [English](https://code.claude.com/docs/en/settings-reference#attribution-sessionurl)
- **`settings` の設定ファイルを作るタイミングの説明が改められた**（「Find or create your settings files」「Use the /config menu」）。`~/.claude/settings.json` を書くのはユーザーの設定を保存したとき、となり、**Show tips** などいくつかの `/config` の選択肢が `.claude/settings.local.json` に保存される、という説明は、`.claude/settings.local.json` に保存するのは **Output style**、になりました — [日本語](https://code.claude.com/docs/ja/settings#find-or-create-your-settings-files) / [English](https://code.claude.com/docs/en/settings#find-or-create-your-settings-files)
- **`self-hosted-environments-configuration` の「How each session's config is assembled」が改められた**。`--settings` で渡すフックを律するのは Claude Code が当てはめる managed settings で、そこで `disableAllHooks` を設定すれば渡したフックは動かない、という言い方になりました（`allowManagedHooksOnly` が残すものに入らない点は変わっていません）
- **チャネルの送信者の許可リストは DM に当てはまる、と明記された**（`channels` の「Security」・`channels-reference` の「Gate inbound messages」）。Telegram・Discord・iMessage のチャネルのプラグインは DM を送信者の許可リストに照らし、ほかの人の DM はその人を一覧に加えた後にだけセッションに届く、となりました — [日本語](https://code.claude.com/docs/ja/channels#security) / [English](https://code.claude.com/docs/en/channels#security)
- **vim モードで `Esc` を 2 回押したときの説明が加わった**（`checkpointing` の「Rewind and summarize」・`interactive-mode` の「General controls」）。vim モードでは NORMAL モードから `Esc` を 2 回押すと巻き戻しのメニューが開き、入力のテキストを消す動きは vim モードの外の話、となりました — [日本語](https://code.claude.com/docs/ja/checkpointing#rewind-and-summarize) / [English](https://code.claude.com/docs/en/checkpointing#rewind-and-summarize)
- **`terminal-config` の「Enable Option key shortcuts on macOS」が改められた**。`/terminal-setup` と初回のターミナルのセットアップのプロンプトがこの設定をオンにするのは macOS 26 以前だけで、どちらもプロファイルの音のベルをオフにする、となりました。`commands` の `/terminal-setup` の行からも、Apple Terminal で Option+Enter の改行を有効にする、という部分が外れています（changelog の v2.1.329 にある、macOS 27 の Terminal.app で「Use Option as Meta key」をオンにする問題の修正） — [日本語](https://code.claude.com/docs/ja/terminal-config#enable-option-key-shortcuts-on-macos) / [English](https://code.claude.com/docs/en/terminal-config#enable-option-key-shortcuts-on-macos)
- **使えないコマンドを送ったときの説明が改められた**（`commands` の「How the command menu matches what you type」・`routines` の「`/schedule` returns "Unknown command"」）。使えないコマンドは「ほとんど」メニューから外れ、送ると `Unknown command` か、使えない理由を述べるメッセージが出る、となりました。`routines` も同じ言い方になり、メニューに `No commands match "/schedule"` が出る、という説明と、クラウドのプロバイダーのログインでは `Unknown command: /schedule` のまま、という部分は外れています — [日本語](https://code.claude.com/docs/ja/routines#schedule-returns-unknown-command) / [English](https://code.claude.com/docs/en/routines#schedule-returns-unknown-command)
- **音声のディクテーションのメッセージの文言にページが追従した**（`voice-dictation` の「Troubleshooting」「Hold to record」）。`/voice needs a Claude subscription` か `/voice isn't available with <provider>`（これまでは `Unknown command: /voice`）、`Voice mode needs a Claude.ai account`、`Voice mode needs SoX to record`、`Voice mode needs a microphone, and SoX couldn't open one` になり、v2.1.195 より前の動きの説明は外れました。`Space` がディクテーションを始める場所の段落は節の後ろへ移り、文字起こしの表示か vim モードからディクテーションするには修飾キーの組み合わせに割り当て直す、という言い方になっています — [日本語](https://code.claude.com/docs/ja/voice-dictation#troubleshooting) / [English](https://code.claude.com/docs/en/voice-dictation#troubleshooting)
- **`keybindings` の「History search actions」が改められた**。`historySearch:accept`・`historySearch:cancel`・`historySearch:execute` が効くのはクラシックのレンダラーのインラインの検索だけ、となり、`historySearch:next` は挙がらなくなりました。フルスクリーンの検索のダイアログのキーは割り当て直せない、という部分も外れています — [日本語](https://code.claude.com/docs/ja/keybindings#history-search-actions) / [English](https://code.claude.com/docs/en/keybindings#history-search-actions)
- **Claude Console のワークスペースの説明が改められた**（`costs` の「Claude Console」・`quickstart` の「Step 2: Start your first session」）。「Claude Code」というワークスペースは、メンバーが初めてサインインして Claude Code がその人の API キーを作るときに作られる、となり、レートの制限はコンソールの **Rate limits** のページで設定する、となりました。`quickstart` からは、最初のログインで Console に「Claude Code」のワークスペースが作られる、という文が外れ、資格情報の文も「Claude Code はログインを保存する」になっています — [日本語](https://code.claude.com/docs/ja/costs#claude-console) / [English](https://code.claude.com/docs/en/costs#claude-console)
- `code-review-setup` の「Turn on Code Review」「Add more repositories」で、リポジトリを選んだ後に押すボタンが **Continue** ではなく、加える数を示すボタン（2 つ選んだら **Add 2 repositories**）になりました — [日本語](https://code.claude.com/docs/ja/code-review-setup#turn-on-code-review) / [English](https://code.claude.com/docs/en/code-review-setup#turn-on-code-review)
- `github-actions` の「Quick setup」で、レビューのワークフローの更新の説明が、v2.1.229 より前に作ったファイルに、`prompt` の行の `--comment` と例の `claude_args` の行を足す、だけになりました（`/install-github-app` をもう一度実行して **Update workflow file with latest version** を選ぶ方法は外れました） — [日本語](https://code.claude.com/docs/ja/github-actions#quick-setup) / [English](https://code.claude.com/docs/en/github-actions#quick-setup)
- `chrome` の「Manage site permissions」で、サイトの権限は Chrome の拡張機能の設定で管理する、という説明が、Claude Code が尋ねたときに承認する、になり、auto モードで分類器が承認したときに拡張機能がサイトごとの確認を飛ばすのも「飛ばしうる」になりました — [日本語](https://code.claude.com/docs/ja/chrome#manage-site-permissions) / [English](https://code.claude.com/docs/en/chrome#manage-site-permissions)
- `agent-view` の「Peek and reply」で、許可のプロンプトのようなダイアログに答えるには返信の欄が空のときに `→` でアタッチする、となり、メッセージがキューで待つ、という文が外れました。「Switch sessions without leaving the terminal」も、確認のメッセージの文言を引かずに、もう一度 `←` を押す、だけになっています — [日本語](https://code.claude.com/docs/ja/agent-view#peek-and-reply) / [English](https://code.claude.com/docs/en/agent-view#peek-and-reply)
- `prompt-caching` の「Compacting the conversation」で、システムプロンプトが古くなっているとき（会話を再開した後など）、Claude Code は今のプロンプトに切り替え、次の要求がこの層のキャッシュを 1 回作り直す、という言い方になりました（これまでは、その会話が最初にコンパクションされたときに切り替える、としていました） — [日本語](https://code.claude.com/docs/ja/prompt-caching#compacting-the-conversation) / [English](https://code.claude.com/docs/en/prompt-caching#compacting-the-conversation)
- `mcp-quickstart` の「Edit .mcp.json directly」で、プロジェクトのスコープのサーバーの承認の説明が、Claude Code が承認を求めたら承認する、だけになりました（クローンしたリポジトリが同意なしにプロセスを始められないためのプロンプトだ、という説明は外れました） — [日本語](https://code.claude.com/docs/ja/mcp-quickstart#edit-mcp-json-directly) / [English](https://code.claude.com/docs/en/mcp-quickstart#edit-mcp-json-directly)
- `monitoring-usage` の「Name each remote machine in a custom attribute」で、値に空白があるとき、Claude Code がイベントとデータポイントにどのキーも写さない、から、`host.name` を外すことがある、になりました。「Retention sweep event」の説明も、`/status` が報告する「どの」設定のエラーも直す、`settings_unknowable` は「設定のソース」を読めなかった、という言い方になっています（`claude-directory` の「Cleaned up automatically」も、`retention_sweep` のイベントが一時停止の理由を報告する、となりました） — [日本語](https://code.claude.com/docs/ja/monitoring-usage#retention-sweep-event) / [English](https://code.claude.com/docs/en/monitoring-usage#retention-sweep-event)
- `plugins/org` の「Recommend plugins」で、`pluginSuggestionMarketplaces` にかかわらず Claude がプラグインを提案するのが、クラウドのセッションの会話に加えて、デスクトップアプリの Code のタブでも、となりました。`plugins/relevance` の冒頭でも、提案を止める案内の対象が「クラウドのセッションの会話で」Claude がする提案から「会話で」Claude がする提案になっています — [日本語](https://code.claude.com/docs/ja/plugins/org#recommend-plugins) / [English](https://code.claude.com/docs/en/plugins/org#recommend-plugins)
- macOS の computer use を新しい安全のルールに更新。一部の操作が拒まれ、一部のアプリのアクセスが減ります
- 保存したスケジュールされたタスクを変更。サインインした新しいセッションでは、以前の版が保存したタスクのほとんどは予定し直しが要ります。ただし、それぞれのセッションを `--resume` すれば実行されます
- ほとんどのモデルで、対象のない `/code-review` が既定のブランチに対してブランチ全体をレビューするよう変更し、複数のコミットのブランチで diff を失う問題を修正
- auto モードが `git status` を実行する回数を減らし、大きなリポジトリでほとんどの要求の待ちを短くするよう変更。変更を捨てる git のコマンドは、作業ツリーが確かめられるまでブロックされることがあります
- `/code-review <pr number> --fix` と、プルリクエストの URL を渡した `/code-review` が、`gh pr diff` が拒まれるか失敗するとレビューせずに止まるよう変更
- 「Exit and stop tasks」が、Claude の応答中に終了した場合を除き、このセッションのスケジュールされたタスクを終え、再開しても再び実行されないよう変更
- 一部のチームメイトのペインが `/bin/sh` を通して始まるよう変更。シェルの起動ファイルを読まないことがあります
- macOS の computer use が、30 秒たっても終わらないアプリの起動をあきらめるよう変更
- ゲートウェイ: `access_control.allow_cidrs` が空の間に出る起動時の警告を、毎回の起動時の通知に変更（テキストのログでは枠で囲む）。ゲートウェイを決して公開のインターネットに晒さないこと、という内容です
- セルフホストのランナー: 同じ owner/name の 2 つ目のホスト名のクローンを、ベースのフォルダーの `_repos/clones/<host>/` の下に置くよう変更。既存のクローンは動きません
- セルフホストのランナー: アドレスのパスに珍しい文字を含むリポジトリを、新しいフォルダーにクローンし直すよう変更。古いフォルダーを名指すルールとボリュームは当てはまらなくなり、古いクローンはそのまま残ります
- セルフホストのランナー: `--capacity 1` で、`--repository-folder` がベースのフォルダーの中のほとんどのフォルダーを取れるよう変更（1 より大きいとき、そこにあるものは起動を止めます）。重なる別のリポジトリのセッションは拒まれます
- Code Mode で、エラーになった `PreToolUse` のフックが、Code Mode の外と同じく、スクリプトのツールの呼び出しを拒まないよう変更。拒まなければならない command・HTTP・MCP のツールのフックには `"onFailure": "block"` を設定します（大幅更新 1 の末尾も参照）
- Code Mode が、256 MiB を超える行の範囲のスクリプトの読み込み（ギガバイトのメモリーを使いうる）を拒むよう変更し、非常に長い行の読み込みのタイムアウトを修正
- テレメトリー・非必須の通信・機能フラグがオフでも Code Mode が始まるよう変更。管理者は managed settings でオフに保てます
- 自分で `log`・`preview`・`sleep` を宣言するスクリプトを、これまでは拒んでいたのを、Code Mode が実行するよう変更
- macOS のログインの更新が、`Claude Code-write-check` の項目でキーチェーンを試すよう変更
- `/tasks` の見出しとフッターのバックグラウンドの数を、シェル・モニター・MCP の呼び出し・エージェント・ワークフロー・スケジュールされたタスクをまとめた 1 つの数に変更
- Stop と SubagentStop のフックが、`background_tasks` で Monitor のスクリプトを `shell` ではなく `monitor` として示すよう変更
- 2.1.326 の、`max_tokens` のエラーが名指す上限での自動の再試行を廃止。出力のトークンが少ないモデルのゲートウェイの背後では、`CLAUDE_CODE_MAX_OUTPUT_TOKENS` をその上限に設定します
- [VSCode] 許可のプロンプトの最後の項目で、Down が Yes に戻らずに止まるよう変更
- [VSCode] コマンドの出力で、普通の色以外の隠れた文字と制御シーケンスを記号で示すよう変更。そのため、ペルシア語・クメール語・ラオ語・シンハラ語・マラヤーラム語のテキストが崩れて見えるか、順序が乱れて見えることがあります
- managed settings のあるコンピューターで、古いセッションの自動の後始末を改善
- `/tui` とほかのその場での再起動が、ログインの更新を少し待つよう改善。サインアウトされにくくなります
- 多くのファイルを編集する長いセッションと、多くの大きな MCP のツールの結果を持つ macOS と Linux の長い Claude Desktop のセッションのメモリーの使用を改善
- Windows: Claude Code の検索のプログラムの起動が遅い PC で、起動と最初の検索を改善
- テレメトリーがオフのとき、Anthropic API へのゲートウェイの背後、または Microsoft Foundry で、Claude の質問への「yes」のような短い返事の auto モードの扱いを改善
- 長いターンの後と、スクリーンショットか大きなツールの結果を持つセッションの `--resume` か `--continue` の後に、アイドルの Claude Desktop と SDK のセッションのメモリーの使用を改善
- Remote Control がオンの Claude Desktop の Code のセッションが、答えた後に次のメッセージを受けられるまでの早さを改善
- 起動時にダウンロードに失敗したプラグインを、クラウドのセッションが再試行するよう改善
- Code Mode を改善。スクリプトが数千のツールの呼び出しをした後にターミナルが固まる時間が大幅に減りました
- Code Mode を改善。サブエージェントを始めた後、Code Mode の外と同じ待ち方の案内が Claude に伝わります

**バグ修正**

- ネットワークの停滞かファイルのロックで読めなくなり、保存中に消えたとき、`~/.claude.json` が既定の値に戻されることがある問題を修正
- Claude Code がキーチェーンを読めても保存できないとき、macOS で繰り返しサインアウトされる問題を修正。そのセッションは期限で止まって理由を述べ、ほかのセッションはサインインしたままになりました
- `/terminal-setup` が、ブロックコメントの周りで VS Code の設定かキーバインドのファイルを壊す問題と、keybindings.json に閉じていない文字列があるところで、Shift+Enter のバインドを失いながら成功と報告する問題を修正
- IDE の diff で受け入れたファイルが最後の改行なしに保存される問題と、VS Code で diff を保存して編集を受け入れたときに、バイトオーダーマーク（BOM）を失う問題を修正
- `/teleport` でクラウドのセッションを選ぶと、開いている会話が置き換わる問題を修正。選ぶと `/clear` のように新しいセッションが始まり、`/resume` で前の会話に戻れます
- `/usage-credits` が、ブラウザーを開いた後に Pro と Max のユーザーにログインし直すよう求める問題と、ブラウザーが開かず、使用クレジットのためにタスクが止まったときに、リンクが 8 秒で消える問題を修正
- 使用クレジットが尽きたか月の上限に達したときに `/usage` がオフと述べる問題と、その上限が使用クレジットで動くモデルを止めているときに `/model` が Pro と Max のユーザーに伝えない問題を修正
- 支出の上限のメニューが、支出を月の上限として示す問題と、狭い窓で行がポインターの下に折り返す問題を修正
- 終わりなく出力するステータスラインのスクリプトが、プロンプトを固め、ギガバイトのメモリーを使う問題を修正
- `--resume` のピッカー・信頼のダイアログ・ほかのセットアップの画面が待っている間に managed settings を承認すると、空の画面のまま固まる問題を修正
- Default の行がすでに保存したモデルを示しているときに `/model` で Default を選ぶと、保存したモデルが組織の既定に置き換わる問題を修正
- トークンの更新の実行中に認証を消した MCP サーバーが、再びサインインされる問題を修正
- 遅い再接続の後にバックグラウンドの MCP のタスクが止まる問題を修正。古いプロトコルの版のまま残された HTTP の MCP サーバーのほとんどに、Claude Code が自ら再接続します
- MCP サーバーか Web サイトが `application/octet-stream` として送る PDF・画像・`.docx`・`.xlsx`・`.pptx` のファイルが .bin として保存され、Claude が PDF と画像を読めなかった問題を修正
- `/code-review <pr number>` が、知らせずにプルリクエストではなくチェックアウトしたブランチをレビューすることがある問題を修正。`gh pr diff` でプルリクエストを読むか、読めないときはそう述べます
- ほとんどのモデルで、`/code-review` が存在しない `~/.claude/CLAUDE.md` を探すために許可のプロンプトで止まる問題を修正
- セルフホストのランナー: `--push-outcome-on-release` が、git のホストにあるセッションのブランチを削除することがある問題を修正
- Esc の後、Code Mode がスクリプトの終わった編集と止めたコマンドを隠し、終了時に失う問題を修正
- Code Mode の暴走したループがマシンのメモリーを埋める問題を修正。上限で止められるようになりました
- 再開中に止めたバックグラウンドのエージェントが動き続ける問題を修正
- バックグラウンドのシェルのコマンドが、終わるまで以前の会話のためのメモリーを使う問題を修正
- Claude Desktop・IDE・SDK が実行するセッションで、コンパクションか `/clear` の後に Remote Control が以前の会話のためのメモリーを使う問題を修正
- Bedrock の Claude Desktop のセッションで、ハングした AWS の credential_process かサインインの呼び出しを待っている間、Stop が要求を終えない問題を修正
- Opus 4.8 と Opus 5 で、Claude が最初の試みでファイルを送れないことがある問題を修正
- ツールの検索のあるセッションで、接続した MCP サーバーのツールを読み込めなかったことが Claude に伝わらず、ツールのないサーバーと受け取る問題を修正
- サービスのクライアントの登録が廃止されていたとき（HTTP 410 Gone）、`claude mcp login` と `/mcp` が、サービスが Claude Code からのサインインを受け付けないと述べる問題を修正
- macOS でセッションがまだ実行中に、claude.ai から同期したプラグインのフックが「Plugin directory does not exist」で失敗する、別の場合を修正
- 作業ディレクトリーの外か自身を指すシンボリックリンクの `rm` に、auto モードが手動の承認を求める問題を修正
- Linux で `/sandbox` が `allowUnixSockets` の項目を許可済みと示す問題を修正。Linux ではそれらのソケットは開かれず、`/sandbox` がそう述べます
- `/install-github-app` で、打ち間違えたコードを消そうと Esc を 2 回押すとサインインが終わる問題を修正
- Remote Control: 再起動の後、アプリが選んだレベルを示したまま、セッションが最初の effort のレベルに戻る問題を修正（Ultracode で始まるセッションはまだ対象外）
- ヘッドレスのセッションで、`reload_plugins` の後か、アカウントのプラグインの一覧から外れたときに、外したプラグインの MCP サーバーが接続したままになる問題を修正
- 同じアドレスのプラグインか MCP サーバーが接続に失敗したときに Claude Docs のコネクターのツールが消える問題と、そのエラーが誤って `/login` を勧める問題を修正
- `--add-dir` が作業ディレクトリーを名指すか、Claude Code がホームのフォルダーで始まるときに、新しい skills・commands・agents のフォルダーを見落とす問題を修正
- 事前に温めたプロセスから始めたセッションが、プロジェクトの `.claude/settings.json` の `autoCompactWindow` の設定を無視する問題を修正
- settings.json から外した後も、実行中のセッションで `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` が効いたままになる問題を修正
- エージェントチームの名前付きのチームメイトで、Agent のツールの `effort` のパラメーターが無視される問題を修正
- `/auto-mode-setup` が、提案するルールのためにプロジェクトを調べるとき、最近の auto モードの拒否を無視する問題を修正。それらから allow ルールを提案することがあり、保存の前に 1 つずつ確かめます
- 自身の `.claude/settings.local.json` が読めないか不正なサブフォルダーかワークツリーで、権限のルールかディレクトリーを加えた後に、誤った「Couldn't save this change」の警告が出る問題を修正
- 失敗した要求の後、クラウドのセッションがネットワークのプロキシの確認を実行するよう Claude に伝え、auto モードがそれをブロックする問題を修正
- モデルの変更の直後に送ったメッセージがまだそれを待っている間に、ヘッドレスの巻き戻しとフォークが進む問題を修正
- クラウドのセッションの再起動中にバックグラウンドのタスクが止められたことが、Claude に伝わらない問題を修正
- Team と Enterprise のプランで、サーバーがアップロードを拒んだのに、`/team-onboarding` がガイドを共有したと報告する問題を修正
- フルスクリーンでパネルと質問がプロンプトで切れる問題、低い窓で `/help`・履歴の検索・バックグラウンドのタスクの一覧が行か題を失う問題、ダイアログで表が折り返す問題を修正
- 再開したセッションが、セッションの終了で途切れた編集・質問・計画を「Rejected」か「Declined」と示す問題を修正
- サーバーのエラーの後に `/passes` が間違ったパスの数を示す問題と、ゲストパスが残っていないのに共有の見返りに使用クレジットを示す問題を修正
- ほかのプログラムにパイプしたときに、`claude --help` の出力が途中で切れる問題を修正
- macOS 27 の Terminal.app で `/terminal-setup` が「Use Option as Meta key」をオンにする問題と、そこでのヒントが Shift+Enter ではなく Option+Enter を勧める問題を修正（`terminal-config` の「Enable Option key shortcuts on macOS」がこれに追従しています。上の「機能改善」参照）
- セルフホストのランナー: Anthropic が管理する git でクローンした Git LFS のリポジトリで、セットアップが失敗する問題を修正。セッションはポインターのファイルのまま始まり、`git lfs pull` で中身を取得します
- SSH のホストのエイリアス・GitHub の SSH の証明書・GHE.com の SSH のユーザーを持つ git のリモートから、セルフホストの環境のセッションが始まらない問題を修正。解決できないエイリアスのエラーは 2 つの git のコマンドを示します
- セルフホストのランナーのセッションで、タイムアウトかネットワークのエラーの後、リモートの MCP サーバーがツールなしのまま、または（https では）切断されたままになる問題を修正
- Claude Code がまだ起動中なのに、セルフホストのランナーのセッションが応答を止めたと示される問題を修正
- コードが読んだ大きなテキストファイルをすべて Code Mode がメモリーに保つ問題と、バックグラウンドのサブエージェントを起こすたびにメモリーが増える問題を修正
- MCP のフォーム・MCP のリンクのプロンプト・常に尋ねるプロンプトが答えを待っている間に、Code Mode がスクリプトを 10 分の上限で止める問題を修正
- 2 分を超えるほとんどの MCP の呼び出しから、Code Mode のスクリプトが「moved to the background」のメッセージをデータとして受け取る問題を修正。スクリプトは最大 10 分待ち、その後エラーを受け取ります
- 一部のツールだけを並べる mod が、知らせずに Code Mode をオフにする問題を修正。そうした mod はもう Code Mode をオフに保たないので、オフにするには managed settings を使います
- Claude が待つスクリプトからツールを呼んだときに、ターンを終える MCP のツールの要求を Code Mode が無視する問題を修正
- Code Mode のスクリプトの `let x;` が、前のスクリプトが `x` に与えた値を保つ問題を修正
- 引数の要らないツールで、Code Mode のスクリプトの引数なしの呼び出しが、パラメーターがないというエラーで失敗する問題を修正
- 4,096 を超えるツールを持つセッションで、Code Mode のスクリプトが `tools` を通じたツールへのアクセスを失う問題を修正
- ほとんどのモデルで、medium で実行したレビューに `/code-review` の指摘のカードがしばしば「high」と示す問題を修正
- 許可のプロンプト・質問・`/model`・`/rewind` のキーのヒントが `keybindings.json` を無視する問題を修正
- 実行中のセッションで、自動のスクロール・PR の状態のバッジ・auto-compact の警告・ultracode のタグが、それらを制御する `/config` のスイッチに従わない問題を修正
- `/add-dir`・`/tui` のフィードバック・ワークフローの保存のフォームで、カスタムの取り消しのキーが効かない問題を修正
- ワークフローの保存のフォームの矢印キーが、背後のワークフローの表示の選択を動かす問題を修正
- 多くの設定を変えた後に、`/config` が何も述べないか「dismissed」と述べる問題を修正
- 改行で終わるファイルで、Read と @-メンションが 1 行多く示す問題を修正
- opusplan と haiku が plan モードで使うモデルを、`/status` が名指さない問題を修正
- ロックの解除が役に立たない macOS のサンドボックスの中で、`claude doctor` がキーチェーンのロックの解除を勧める問題を修正
- フルスクリーンで、テキストをコピーしてスクロールで離れた後に「Jump to bottom」の表示が隠れたままになる問題、その表示の文字が変わるとその下の行が空白になる問題、PageUp を素早く押すとスクロールしすぎる問題を修正
- メモリーが少ないときに、画面の更新が飛ばされることがある問題を修正
- スクロールバックで、長いコードブロックが空行を 1 つ失い、別の行を繰り返す問題を修正
- プロンプトの提案が `_(no suggestion)_` のようなプレースホルダーのテキストを示すことがある問題を修正
- 再開のときの以前のメッセージについての行が、ファイルが無事なのに壊れたファイルのせいにする問題を修正
- プロンプトのテキストが複数のスタイルを設定する色のコードを含み、キーワードかコマンドが強調されていると、プロンプトから文字が消える問題を修正
- `claude remote-control` のセッションで、`/rename` と `UserPromptSubmit` のフックの題が claude.ai とモバイルに出ない問題を修正
- ブランチで名前を変えた後に編集したファイルを、Remote Control の diff が 2 回並べる問題を修正
- [VSCode] 拡張機能のトークンの更新にサインインのサーバーが 10〜30 秒かけて答えると、すべての窓とターミナルで Claude Code からサインアウトされる問題を修正
- [VSCode] 入力メソッド（IME）の変換中に押したキーが、許可のプロンプトでフォーカスを進めるか断る、メニューの行を実行する、ダイアログを閉じる問題を修正（anthropics/claude-code#106358）
- [VSCode] Bash・Edit・Write とほかの組み込みのツールの許可のプロンプトが、安全の確認が尋ねる理由を示さない問題を修正
- [VSCode] 書きかけの計画のコメントが失われるか別の箇所へ動く問題と、入力メソッドの Enter がコメントを送る、セッションの名前の変更を終える、@-メンションのファイルを選ぶ問題を修正
- [VSCode] 上限のバナーが使用クレジットを使っているときにそう述べない問題と、セッションのアンケートがそのバナーと使用クレジットのカードを覆う問題を修正
- [VSCode] Account & Usage のダイアログが開いている間に届いた許可の要求を、そのダイアログを閉じるまでスクリーンリーダーが読み上げない問題を修正
- [VSCode] ターミナルの Claude Code のセッションが切断された後、提案した編集の diff のタブが、何もしない Accept のボタンとともに開いたままになる問題を修正
- [VSCode] 短いツールの入力と出力がパネルの端で切れて残りを読めない問題（エディターのタブで開くようになりました）と、ドラッグでテキストを選ぶとタブも開く問題を修正
- [VSCode] メッセージの欄で入力メソッド（IME）が変換中のテキストの上に、Up キーが以前のメッセージを置く問題を修正（anthropics/claude-code#101294）
- [VSCode] VS Code 1.103〜1.139 か浮動のチャットの窓で、エクスプローラーのフォルダーをチャットにドロップしても何も挿入されない問題と、ドロップの強調が誤った「Hold Shift」のヒントとともに消える問題を修正
- [VSCode] ボタンが有効になるときに、許可のプロンプトがスクロール中の詳細からキーボードのフォーカスを外す問題を修正
- [VSCode] `claudeCode.lockEditorGroups` がオフのとき、Claude のタブのファイルのリンクが別のエディターのグループで開く問題を修正（anthropics/claude-code#108884）
- [VSCode] 1 つのチルダで書いた範囲（`3~5 … 7~10`）がチルダを失い、その間のテキストが取り消し線で示される問題を修正。取り消し線は `~~text~~` だけになりました
- [VSCode] ディクテーションのエラーが狭い列に折り返す問題、質問のカードが待っている間にスピナーが回る問題、失敗した UTF-16 のコマンドの出力で各文字の後に NUL の記号が出る問題を修正

**その他**

- **見出しの改称**: 3 つの見出しが改称されました。`artifacts` の h3「Set a retention policy」が「Set a retention policy on Enterprise plans」に、`troubleshoot-install` の h3「OAuth error: Invalid code」が「That doesn't look like the full code」に（`That doesn't look like the full code` が出たら、ブラウザーのログインのコードを真ん中の `#` も含めて全部コピーして貼り直す、という段落が加わり、「Find your error」の表の行にもこのメッセージが加わりました。`OAuth error: Invalid code` の説明は残っています）、`plugins/troubleshooting` の h3「`No plugins available` or `No marketplaces configured`」が「`No plugins yet` or `No marketplaces configured`」になりました（id は下の「参考リンクについて」参照）
- **書式の変化**: `quickstart` の「Step 1: Install Claude Code」で、引用の中のコードフェンスの 5 つの開始行の `theme={null}` が 1 回から 87 回の繰り返しになりました（生の差分の 10 行）。`quickstart` の残りの 4 行が内容の変更です（上の「機能改善」の Claude Console の項目）
- **外れた文**: `cross-session-messaging`（ほかのマシンのセッションとの会話を始めるのに、対象が一覧に出ていることが要る、という部分）、`devcontainer`（managed settings の値が `~/.claude` やプロジェクトの `.claude/` で開発者が設定したものより優先する、という部分）、`third-party-integrations`（managed の権限はローカルの構成で上書きできない、という部分）、`managed-mcp`（「hard」な許可リスト、の「hard」）、`plugins/mods/overview`（表にない **Built-in** のプラグインを `/plugin` で無効にする、という部分）、`plugins/cli-reference`（`/plugin help` の行と、認識しない最初の語でも **Discover** のタブを開く、という部分）、`code-mode`（大幅更新 1 参照）
- **字句の小さな修正**: `plugins/code-intelligence`（ダイアログの選択肢 **No, not now** が **Not now** に）、`plugins/mods/events`（`'*'` は「テレメトリーのイベント以外のすべて」から「ほとんどのイベント」に一致）、`plugins/dependencies`（「engineers」が「users」に）、`plugins/troubleshooting`（`Plugin directory does not exist` のメッセージの引用を短く、「even though」が「even if」に）、`security`（ネットワークのコマンドの承認と Web ページの要約の言い方）、`permissions`（「Manage permissions」の注意と、サンドボックスとの関係の「holds」が「applies」に）
<!-- light:minor-updates:end -->

見出しマップ（`en/claude_code_docs_map.md`）は、更新時刻が 2026年11月19日 02:17:59 UTC から 2026年11月19日 23:09:38 UTC に替わり、20 行が加わり 4 行が外れました（6,639 行から 6,655 行）。加わったのは、`llms-full.txt` に加わった 16 の見出しと改称した 3 つの見出しと新しいスタンプで、外れたのは改称前の 3 つの見出しと古いスタンプです。今回、見出しマップにだけ先に載った見出しはありません。

**参考リンクについて**: 日本語版は、今回リンクを付けたページの HTML を取得し、新しい節の id があるか、今回の差分で出入りしたコードの字句（変数名・版の数字・パス・リンク先・メッセージの文字列。base と head の `llms-full.txt` で数が違うものだけ）が英語版と同じだけあるかで、今回の内容になっているかを確かめました。`settings` や `code` のような訳文の地の文にも出る語や、ページの外枠にも出るリンクのパスで件数が合わないものは、該当する箇所の訳文で確かめています。今回リンクを付けたページは、すべて今回の内容になっていました。アンカーは英語版・日本語版の HTML の見出しの id で確かめました。改称した見出しのうち、`troubleshoot-install` の「That doesn't look like the full code」は旧い id の `#oauth-error-invalid-code`、`plugins/troubleshooting` の「`No plugins yet` or `No marketplaces configured`」は `#no-plugins-available-or-no-marketplaces-configured` のままで、`artifacts` の「Set a retention policy on Enterprise plans」は `#set-a-retention-policy-on-enterprise-plans` に変わりました。`desktop` の日本語版のページの題は英語のまま（Desktop application）なので、リンクの日本語の題は訳を当てています。**changelog ページへのリンクは、本サマリの方針どおり付けていません。**

## 新着情報

<!-- light:whats-new:start -->
（今回の差分に新着情報（`whats-new/`）のページはありません。head の `llms.txt`・`llms-full.txt`・見出しマップにも whats-new のページは載っていません）
<!-- light:whats-new:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-11-18.md](./archives/latest/2026-11-18.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-11-18.md](./archives/latest-detail/2026-11-18.md)

<!--
base_commit: 831f1678213f7b2708b300fbfd4e73aa7b6ac427
head_commit: 2864b8c8e49e5201a3575b16751cc5caf78f4b1c
generated_at_full: 2026-11-20T15:31:13+09:00
-->
