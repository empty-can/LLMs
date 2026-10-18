---
対象期間: 2026年10月16日 〜 2026年10月17日
作成日: 2026-10-17
---

# Claude Code 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
**今回は changelog に変更がなく、前回は見出しマップにだけ先に載っていた 7 つの見出しの本文が `llms-full.txt` に入りました。plan モードではフックや mod の allow でファイルの編集を承認できないことが明記され、Git Bash のない Windows で失敗したフックがツールの呼び出しを止める場合の節ができたほか、MCP のツール名でのサーバー名の書き方、Agent SDK の auto モードが対応しないモデルへの切り替えで `default` モードに変わること（v2.1.299 以降）、bypass の同意が `~/.claude/settings.json` にないときのセッションの始まり方も載りました**。新しいページはなく、228 ページ中 17 ページが変わり、変更は 204 行（追加 157・削除 47）、大幅更新は `hooks` の 1 ページです。総行数は 120,838 行から 120,948 行に増えました。

主要なものを以下に挙げます。

1. plan モードでは、`PreToolUse` フックの `"allow"`（`ExitPlanMode` を除く）も `tool.check` を扱う mod の承認も、ファイルの編集など読み取り専用でない呼び出しに効かないと明記された（`permissions` の新しい 2 つの h3）
2. Git Bash のない Windows で `PreToolUse` か `PermissionRequest` のコマンドフックが失敗すると呼び出しが止まる場合の節ができ、メッセージごとの直し方が載った
3. MCP のツール名に書くサーバー名は、`.` やスペースが `_` になる・プラグインのサーバーはプラグインスコープの形・`__` を含む名前はワイルドカード形、と書き方が載った
4. Agent SDK で auto モードのセッションを対応しないモデルへ切り替えると `default` モードに変わり、戻すには対応モデルに戻して auto を設定し直す、と載った（v2.1.299 以降）
5. bypass の同意が `.claude/settings.local.json` などにだけあると、起動時の bypass の要求は無視され、セッションは Manual モードで始まることがあると明記された
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**plan モードではフックと mod の allow がファイルの編集に効かないと明記された**](#1-plan-モードではフックと-mod-の-allow-がファイルの編集に効かないと明記された):  
  `permissions` に「Precedence among rules, hooks, and mods」と「Hook approvals in plan mode」の h3 ができました。plan モードでは、`ExitPlanMode` を除き、`PreToolUse` フックの `"allow"` はファイルの編集やほかの読み取り専用でない呼び出しに効かず、`tool.check` を扱う mod もそうした呼び出しを承認できません。`hooks-guide`・`hooks`・`plugins/mods/events`・`agent-sdk/permissions` も同じ内容に改められています
2. [**Git Bash のない Windows で失敗したフックが呼び出しを止める場合の節ができた**](#2-git-bash-のない-windows-で失敗したフックが呼び出しを止める場合の節ができた):  
  `hooks` に「Failed hooks on Windows without Git Bash」の h4 ができました。`shell` を設定しない shell 形式のフックは Git Bash がないと PowerShell で動き、`onFailure` を設定しない `PreToolUse` か `PermissionRequest` のコマンドフックは、失敗かタイムアウトすると呼び出しを止めることがあります。フックの書き方に応じた 4 つの直し方が載り、`onFailure` の「既定値は `"continue"`」の文は外れました
3. [**MCP のツール名に書くサーバー名の綴り方が載った**](#3-mcp-のツール名に書くサーバー名の綴り方が載った):  
  `permissions` の「MCP」で、ルールの `<server>` にはそのサーバーのツール名に現れる形を書く、として `my.server`・プラグインのサーバー・`reports__v2` の 3 つの例が加わりました。`agent-sdk/mcp` の命名規則には表が、`errors` のツールが 0 個のエラーには対処の項目が加わり、`sub-agents` には MCP サーバー単位のエントリの表ができています
4. [**Agent SDK の auto モードは対応しないモデルへの切り替えで default モードに変わる**](#4-agent-sdk-の-auto-モードは対応しないモデルへの切り替えで-default-モードに変わる):  
  `agent-sdk/permissions` に「Auto mode (`auto`)」の h4 ができました。`set_model()`・`setModel()`・`applyFlagSettings()` で auto モードの対応しないモデルへ切り替えると、セッションは `default` モードに変わり、`permissionMode` が `"default"` の `status` メッセージが届きます（v2.1.299 以降）。auto に戻すには、対応するモデルに戻したうえで権限モードを設定し直します
5. [**bypass の同意がユーザー設定にないとセッションが Manual モードで始まることがあると明記された**](#5-bypass-の同意がユーザー設定にないとセッションが-manual-モードで始まることがあると明記された):  
  `permission-modes` で、`skipDangerousModePermissionPrompt` が `.claude/settings.local.json` にだけあるバックグラウンドのセッションは、通知を出したまま動き続け、無視されたフラグによって `Shift+Tab` の切り替えから `bypassPermissions` が外れるか、Manual モードで始まる、と書かれました。`agent-view` と `errors` にも同じ通知の説明が加わっています
<!-- light:highlight-list:end -->

## 1. plan モードではフックと mod の allow がファイルの編集に効かないと明記された

**`permissions` の「Extend permissions with hooks」の下に、前回は見出しマップにだけ載っていた 2 つの h3 ができました。**

- **「Precedence among rules, hooks, and mods」**: `PreToolUse` フックの決定は権限ルールを迂回しない、という既存の段落に見出しが付いたものです。`tool.check` を扱う mod の答えがルールやフックの決定を置き換えられるのは、「plan モードの外か、読み取り専用の呼び出し」の場合に限る、という限定が加わりました
- **「Hook approvals in plan mode」**: plan モードでは、`ExitPlanMode` を除き、`PreToolUse` フックの `"allow"` はファイルの編集やほかの読み取り専用でない呼び出しに効きません。その呼び出しは、フックがない場合と同じプロンプト・ブロック・承認になり、フックが返す `updatedInput` はそのまま適用されます。`ExitPlanMode` に `"allow"` と `updatedInput` で答えれば、このツールは plan モードでもプロンプトなしで動きます。`tool.check` を扱う mod も、plan モードでは読み取り専用でない呼び出しを承認できません（ブロックはできる）。この制限を外すには、プランを承認するか、別の権限モードに切り替えます

ほかのページも同じ線で改められました。

- **`hooks-guide` の「Hooks and permission modes」**: plan モードで `PreToolUse` フックがファイルの編集に `"allow"` を返しても、フックがない場合と同じプロンプト・ブロック・承認になる、という段落が加わりました。mod についても、plan モードでは読み取り専用の呼び出しなら承認できるが、ファイルの編集やほかの読み取り専用でない呼び出しは承認できない、という文が加わっています。`"allow"` でも抑えられないプロンプト（ネットワークパスからの読み取り・`requiresUserInteraction` の MCP ツール・組織が `ask` に設定したコネクタのツール）は箇条書きになり、「Structured JSON output」の `"allow"` の説明も同じ箇条書きと plan モードへのリンクの形になりました
- **`hooks` の「PreToolUse decision control」**: `permissionDecision` の説明に plan モードの節へのリンクが加わり、`AskUserQuestion` と `ExitPlanMode` は `"allow"` と組で `updatedInput` が要る、という部分が別の文に分かれました
- **`plugins/mods/events`**: `tool.check` の節に、plan モードでは、ファイルの編集のような読み取り専用でない呼び出しについて、フックは `next(e)` が返す決定を厳しくはできても緩められない、という文が加わりました。「Where settings hooks run in the order」の段落にも同じ限定が加わり、`main` での `git push` を断る例の説明は「`main` の場合」と「別のブランチやほかのコマンドの場合」の 2 つの箇条書きになっています
- **`agent-sdk/permissions`**: 「How permissions are evaluated」の Hooks のステップに plan モードの節へのリンクが、「Plan mode (`plan`)」に「`PreToolUse` フックが `allow` を返しても」ファイルの編集は自動承認されない、という文言が加わりました

- [権限を設定する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/permissions#hook-approvals-in-plan-mode)
- [Configure permissions - Claude Code Docs (English)](https://code.claude.com/docs/en/permissions#hook-approvals-in-plan-mode)
- [フックでアクションを自動化する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/hooks-guide#hooks-and-permission-modes)
- [Automate actions with hooks - Claude Code Docs (English)](https://code.claude.com/docs/en/hooks-guide#hooks-and-permission-modes)

## 2. Git Bash のない Windows で失敗したフックが呼び出しを止める場合の節ができた

**`hooks` に、前回は見出しマップにだけ載っていた h4「Failed hooks on Windows without Git Bash」ができました。** ブロックされたツールの呼び出しのエラーに次の文が含まれていれば、`PreToolUse` か `PermissionRequest` のコマンドフックが失敗かタイムアウトして、呼び出しを止めたことを示します。

```text
blocking because Git Bash wasn't found and this hook doesn't set "shell" to "powershell", so only exit code 0 or 2 counts as its verdict.
```

`shell` を設定しない shell 形式のフックは、Git Bash がないと PowerShell で動くので、Bash 向けに書いたスクリプトはそのままでは動かないことがあります。直し方はフックに応じて 4 つです。

- **Bash 向けに書いたフック**: Git for Windows を入れるか、Claude Code の見つけられない場所に Git Bash があるなら `CLAUDE_CODE_GIT_BASH_PATH` を設定して、新しいセッションを始めます
- **`.cmd` や `.bat` ではなく 1 つの `.exe` を動かすフック**: プログラムを `command` に、引数を `args` に書く exec 形式にし、`"onFailure": "block"` を加えます。シェルを使わずにプログラムが起動します。`"onFailure": "block"` がないと、プログラムが失敗する・見つからない・タイムアウトするときに呼び出しが進むことがあります
- **PowerShell 向けに書いたフック**: `"shell": "powershell"` と `"onFailure": "block"` を加えます。失敗の理由はデバッグログで確かめます
- **フックが失敗しても操作を進めたい場合**: `"onFailure": "continue"` を加えます

このエラーが出るフックでは、0 と 2 以外の終了コードは、呼び出しを断らない JSON を出力していても失敗と数えます。

**同じページの「Block the action when a hook fails」にも、Git Bash のない Windows では `onFailure` を設定しない shell 形式の `PreToolUse` か `PermissionRequest` のコマンドフックが失敗すると呼び出しを止めることがある、という Note が加わり、「既定値は `"continue"`」の文は外れました。** コマンドフックのフィールドの表の `onFailure` の説明も、「`"continue"`（既定）か `"block"`」から、「フックが失敗したときに、そのきっかけになった操作を進めるかどうか。`"block"` の場合と、設定しない場合はこの節を見る」に改められています。`hooks-guide` の「Hook error in output」にも、メッセージに `blocking because Git Bash wasn't found` があれば Windows で Git Bash が見つからず、失敗かタイムアウトしたフックが呼び出しを止めている、という項目が加わりました。同じページの「Hook output」の「Any other exit code」も、「結果はフックが stdout に出したものによる」から、「ほとんどのイベントで非ブロッキングエラーとして操作が進む。ただし失敗が操作を止めるフックか、JSON の出力が検証を通る場合は除く」に改められています。あわせて `hooks` の非ブロッキングエラーの説明は、「失敗が操作を止めるフック」を除く、という言い方に改められています（大幅更新 1 を参照）。

- [フックリファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/hooks#failed-hooks-on-windows-without-git-bash)
- [Hooks reference - Claude Code Docs (English)](https://code.claude.com/docs/en/hooks#failed-hooks-on-windows-without-git-bash)
- [フックでアクションを自動化する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/hooks-guide#hook-error-in-output)
- [Automate actions with hooks - Claude Code Docs (English)](https://code.claude.com/docs/en/hooks-guide#hook-error-in-output)

## 3. MCP のツール名に書くサーバー名の綴り方が載った

**`permissions` の「MCP」の冒頭が、「サーバーのすべてのツールに一致させるには `mcp__<server>__*`、1 つのツールにはその完全な名前 `mcp__<server>__<tool>` を書く」に書き直されました。** そのうえで、`<server>` にはそのサーバーのツール名に現れる形を書く、として次の 3 つの例が加わっています。

- **`.` やスペースを含む名前**: これらの文字は `_` になるので、`my.server` として設定したサーバーには `mcp__my_server__*` と書きます
- **プラグインが提供するサーバー**: `<server>` はプラグインスコープの形になるので、`my-plugin` というプラグインの `database-tools` サーバーには `mcp__plugin_my-plugin_database-tools__*` と書きます
- **`__` を含むか `_` で終わる名前**: 名前全体を使ったワイルドカード形を書きます。`reports__v2` というサーバーには `mcp__reports__v2__*` です。素の `mcp__reports__v2` も短い `mcp__reports` も、Claude Code はどちらも `reports` というサーバーのルールとして読むので、allow ルールとしてはそのツールに一致しません

ほかのページにも同じ説明が入りました。

- **`agent-sdk/mcp` の「Tool naming convention」**: `<server-name>` は `mcpServers` のキーのようにサーバーを登録した名前で、`.` やスペースは `_` に置き換わる、として `github` と `my.server` の 2 行の表（`mcp__github__list_issues`・`mcp__my_server__list_issues`）が加わりました。`allowedTools` と MCP の権限ルールには完全なツール名を使い、プラグインのサーバーは `plugin_` で始まるプラグインスコープの形になる、とも書かれています
- **`agent-sdk/custom-tools` の「Call a custom tool」と `agent-sdk/hooks` の「Matchers」**: `mcpServers` のキーに `.` やスペースがあれば `_` に置き換えて書く、`<server>` は命名規則のとおりに綴る、という説明とリンクが加わりました
- **`errors` の「Agent would be spawned with zero tools」**: 接続済みの MCP サーバーを指すエントリは、`mcp__reports__v2__get_totals` の `reports__v2` のようにツール名での綴りと比べ、そのサーバーには `mcp__reports__v2__*` と書く、という対処が加わりました。短い `mcp__reports` では、`reports__v2` のツールはサブエージェントに 1 つも渡りません
- **`sub-agents`**: `tools` と `disallowedTools` でツールを絞る説明が、前回は見出しマップにだけ載っていた h4「Restrict which tools a subagent can use」にまとまり、両方を設定したときは `disallowedTools` を先に適用する、という文がその冒頭へ移りました。MCP サーバー単位のエントリは、1 つのサーバーのツールをすべて与える（`tools` に `mcp__github__*`）・1 つのサーバーのツールを除く（`disallowedTools` に `mcp__github` か `mcp__github__*`）・すべてのサーバーの MCP ツールを除く（`disallowedTools` に `mcp__*`）の表になっています。フロントマターの表の `disallowedTools` の行のリンク先も、この h4 に改められました

- [権限を設定する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/permissions#mcp)
- [Configure permissions - Claude Code Docs (English)](https://code.claude.com/docs/en/permissions#mcp)
- [MCP を使用して外部ツールに接続する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/agent-sdk/mcp#tool-naming-convention)
- [Connect to external tools with MCP - Claude Code Docs (English)](https://code.claude.com/docs/en/agent-sdk/mcp#tool-naming-convention)

## 4. Agent SDK の auto モードは対応しないモデルへの切り替えで default モードに変わる

**`agent-sdk/permissions` の「Mode details」に、前回は見出しマップにだけ載っていた h4「Auto mode (`auto`)」ができました。** 分類器のモデルがシェルコマンドやネットワークの要求などを実行の前に確かめ、確かめたものをそれぞれ許可かブロックする、と述べ、必要なモデルとプロバイダーや評価の順序は `permission-modes` の auto モードの節を見るよう案内しています。

auto モードのセッションを、`set_model()`（Python）・`setModel()`（TypeScript）・`applyFlagSettings()` で auto モードの対応しないモデルへ切り替えると、セッションは `default` モードに変わります。

- **見えるもの**: subtype が `status` で `permissionMode` が `"default"` の `system` メッセージが届きます（TypeScript SDK の型は `SDKStatusMessage`）。それ以後、承認が要り allow ルールに一致しない呼び出しは `canUseTool` のコールバックに届きます
- **auto モードに戻すには**: 対応するモデルに切り替えてから `set_permission_mode("auto")` か `setPermissionMode("auto")` を呼びます。この呼び出しをせずにモデルだけ戻すと、セッションは `default` モードのままです。対応しないモデルの間は、この呼び出しが `Cannot set permission mode to auto: auto mode unavailable for this model` で失敗します

この `default` モードへの切り替わりには Claude Code v2.1.299 以降が要ります。`agent-sdk/python` の `set_model(model)` と `agent-sdk/typescript` の `setModel()` の説明にも、新しいモデルが auto モードに対応しなければ auto モードのセッションは `default` モードに変わる、という一文がこの節へのリンクつきで加わりました。また「Set permission mode」の「At query time」のタブからは、「動的に変えない限りセッション全体に効く」の文が外れています。

- [権限の設定 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/agent-sdk/permissions#auto-mode-auto)
- [Configure permissions - Claude Code Docs (English)](https://code.claude.com/docs/en/agent-sdk/permissions#auto-mode-auto)

## 5. bypass の同意がユーザー設定にないとセッションが Manual モードで始まることがあると明記された

**`permission-modes` の「Skip all checks with bypassPermissions mode」で、バックグラウンドのセッションの項目が書き足されました。** `skipDangerousModePermissionPrompt` が `.claude/settings.local.json` にだけあると、バックグラウンドのセッションは bypass の要求を無視して始まり、`Bypass permissions was requested at launch and ignored · …` の通知を固定します。今回、通知を出したそのセッションも動き続ける、として次の 2 つが加わりました。

- **`--allow-dangerously-skip-permissions` が無視された場合**: そのセッションの `Shift+Tab` の切り替えから `bypassPermissions` が外れます
- **`--permission-mode bypassPermissions` か `--dangerously-skip-permissions` が無視された場合**: そのセッションは Manual モードで始まります

bypass を効かせるには、そのキーを `~/.claude/settings.json` に加えてから新しいバックグラウンドのセッションを始めます。root や `sudo` での起動を断る文の「このモード」は「`bypassPermissions` モード」と明記され、同意のダイアログの段落の頭には空の `<span />` が置かれました（`errors` と `agent-view` はこの段落を `#bypass-permissions-acceptance` で指しています）。

- **`agent-view` の「Permission mode」**: `←` で開いたエージェントビューからディスパッチしたセッションの権限モードは、対象のディレクトリの設定を先に、元のセッションのモードを次に使う、と書き直されました。その 2 番目の「元のセッションの権限モード」には、元のセッションが `bypassPermissions` モードだと、新しいセッションが代わりに Manual モードで始まり `Bypass permissions was requested at launch and ignored` の通知が出ることがある、という説明が加わっています。bypass の免責への同意が `.claude/settings.local.json` か `--settings` のファイルにだけあるときに起こり、Manual モードで続けるか、同意を `~/.claude/settings.json` に加えます
- **`errors` の「Find your error」**: 表に `Bypass permissions was requested at launch and ignored` の行が加わり、`permission-modes` の同意の段落を案内しています

- [権限モードを選択する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/permission-modes#skip-all-checks-with-bypasspermissions-mode)
- [Choose a permission mode - Claude Code Docs (English)](https://code.claude.com/docs/en/permission-modes#skip-all-checks-with-bypasspermissions-mode)
- [複数のエージェントをエージェントビューで管理する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/agent-view#permission-mode)
- [Manage multiple agents with agent view - Claude Code Docs (English)](https://code.claude.com/docs/en/agent-view#permission-mode)

## 新規追加されたページ

<!-- light:new-pages:start -->
（今回の対象期間に新規追加・削除されたドキュメントページはありません。`llms.txt` は変わらず、`llms-full.txt` に展開されている固有のページも 228 のままで、`Source:` の行が 231 あり 3 ページが 2 回展開されている状態も前回と同じです）
<!-- light:new-pages:end -->

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
- [**Hooks reference**](#1-hooks-reference) ([日本語](https://code.claude.com/docs/ja/hooks#other-exit-codes) / [English](https://code.claude.com/docs/en/hooks#other-exit-codes)):  
  65 行（追加 49・削除 16）が変わりました。新しい 2 つの h4（「Failed hooks on Windows without Git Bash」はハイライト 2、「PreModelSwitch timeouts and other exit codes」）のほかは、非ブロッキングエラーの説明を「失敗が操作を止めるフック」を除く形に改めた書き換えが中心です
<!-- light:updated-pages:end -->

`llms-full.txt` から切り出したページ単位の差分（`git diff --no-index --numstat`）が 50 行以上の既存ページを挙げています。次点は `hooks-guide` の 21 行、`sub-agents` の 20 行、`permissions` の 18 行、`agent-sdk/permissions` の 17 行で、いずれもハイライトで扱います。

## 1. Hooks reference

ハイライト 1 と 2 で取り上げた箇所のほかに、次の記述が改められました。

- **非ブロッキングエラーの言い方**: 「Exit code output」の非ブロッキングエラーの項目が、「操作は進む。ただし失敗が操作を止めるフック（たとえば `onFailure` を `"block"` にしたフック）は除く」になりました。終了コードと stdout の表の「検証を通る JSON」×「0 と 2 以外の終了コード」のセルも、「`onFailure: "block"` ならこれは失敗と数える」から「失敗が操作を止めるフックでは、代わりに失敗と数える」に改められています。「Exit code 0」の JSON の解析の失敗、「Other exit codes」、起動できないフック、終了コード 1 の Warning、「Timeouts」の `PreToolUse` の項目にも、「失敗が操作を止めるフックでない限り」の限定が付きました。「Other exit codes」では、例の `Failed with non-blocking status code:` の行の前に「操作が進んだ場合は」の条件が付き、起動できないフックのメッセージの例は `text` のコードブロックに分かれています。検証を通る JSON の例の説明も、「その実行は成功になる」から「その JSON が結果を決めることがある」に改められました
- **HTTP フックの応答**: 「HTTP response handling」の 2xx 以外のステータスと接続の失敗の項目から「実行は続く」が外れ、「HTTP フックはステータスコードだけではブロッキングエラーを示せない」の文に代わって、「非ブロッキングエラーの後は、失敗が操作を止めるフックでない限り操作が進む」という文が入りました。決定のフィールドへのリンクも加わっています
- **「UserPromptSubmit input」**: 入力したスキルかカスタムコマンド（`/deploy staging` など）がプロンプトのときは、展開したスキルの内容ではなく、入力したとおりの行がフックに渡る、という段落が加わりました。フックがそのプロンプトをブロックするとコマンドは動かないので、スキルが `` !`<command>` `` で差し込むシェルコマンドも動きません。コマンドの名前や引数で照合したいなら `UserPromptExpansion` を使う、と案内しています
- **PreModelSwitch**: タイムアウトと終了コードの段落が、前回は見出しマップにだけ載っていた h4「PreModelSwitch timeouts and other exit codes」にまとまりました。「`PreModelSwitch` は `command`・`http`・`mcp_tool` のフックだけを動かすので、`prompt` と `agent` の既定は当たらない」の文と、「ほかのイベントのタイムアウトは Timeouts を見る」の文は外れ、0 と 2 以外の終了コードについては「Other exit codes」を見る、という 1 文になっています

- [フックリファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/hooks#other-exit-codes)
- [Hooks reference - Claude Code Docs (English)](https://code.claude.com/docs/en/hooks#other-exit-codes)
- [フックリファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/hooks#userpromptsubmit-input)
- [Hooks reference - Claude Code Docs (English)](https://code.claude.com/docs/en/hooks#userpromptsubmit-input)

## 軽微な更新

<!-- light:minor-updates:start -->
今回の差分は **`llms-full.txt` の 1 ファイル**だけで、`llms.txt` と見出しマップは変わっていません。`llms-full.txt` の生の差分は追加 157 行・削除 47 行で、ページの並びは変わっていないため、ページ単位に切り出して数えても同じ量です。228 ページ中 **17 ページ**が変わり、**changelog は変わっていません**（最新の収録は前回と同じ v2.1.302）。大幅更新の `hooks` を除く **16 ページ**の変更を以下にまとめます。

`llms-full.txt` の総行数は **120,838 行から 120,948 行へ 110 行増え**ました。`Source:` の行は 231、固有のページは 228 のままです。コードフェンスの外の見出しは 5,648 から 5,655 へ 7 つ増え、外れた見出しはありません。増えた 7 つは、前回のサマリで「見出しマップには載ったが、`llms-full.txt` にはまだ見出しも本文もない」とした 7 見出し（`sub-agents` の「Restrict which tools a subagent can use」、`permissions` の「Precedence among rules, hooks, and mods」「Hook approvals in plan mode」、`sandboxing` の「`/sandbox` prints `Sandbox settings not changed`」、`hooks` の「Failed hooks on Windows without Git Bash」「PreModelSwitch timeouts and other exit codes」、`agent-sdk/permissions` の「Auto mode (`auto`)」）そのもので、今回その本文が取り込まれました。

**新機能**

- **Agent SDK の auto モードのセッションが、対応しないモデルへの切り替えで `default` モードに変わる**（`agent-sdk/permissions`・`agent-sdk/python`・`agent-sdk/typescript`。v2.1.299 以降。詳細はハイライト 4 参照）

**機能改善**

- **plan モードではフックと mod の allow がファイルの編集に効かないと明記された**（`permissions`・`hooks-guide`・`hooks`・`plugins/mods/events`・`agent-sdk/permissions`。詳細はハイライト 1 参照）
- **Git Bash のない Windows で失敗したフックが呼び出しを止める場合の節ができた**（`hooks`・`hooks-guide`。詳細はハイライト 2 参照）
- **MCP のツール名に書くサーバー名の綴り方が載った**（`permissions`・`agent-sdk/mcp`・`agent-sdk/custom-tools`・`agent-sdk/hooks`・`errors`・`sub-agents`。詳細はハイライト 3 参照）
- **bypass の同意がユーザー設定にないときのセッションの始まり方が明記された**（`permission-modes`・`agent-view`・`errors`。詳細はハイライト 5 参照）
- **フックの非ブロッキングエラーの説明が「失敗が操作を止めるフック」を除く形に改められ、`UserPromptSubmit` の入力でスキルのコマンドが展開前の行のまま渡ると明記された**（`hooks`。詳細は大幅更新 1 参照）
- **`/sandbox` が `Sandbox settings not changed` と出したときの対処が載った**（`sandboxing` の「Troubleshooting」の新しい h3）。`/sandbox` のパネルで選んだ内容をプロジェクトの `.claude/settings.local.json` に保存できなかったことを示し、括弧の中の理由が `EACCES`・`EPERM`・`EROFS` なら、書き込めるプロジェクトのフォルダーで Claude Code を起動して `/sandbox` をやり直し、`Invalid JSON syntax in settings file` で始まるなら、そのファイルの JSON を直してやり直します — [日本語](https://code.claude.com/docs/ja/sandboxing#%2Fsandbox-prints-sandbox-settings-not-changed) / [English](https://code.claude.com/docs/en/sandboxing#%2Fsandbox-prints-sandbox-settings-not-changed)
- **Claude が書く mod のフォルダーが保護されたパスに挙がった**（`permission-modes` の「Protected paths」・`plugins/mods/create`）。保護されたディレクトリの一覧に、Claude がユーザーのために書いた mod を保存する `~/.claude/dev-mods/`（または `CLAUDE_CONFIG_DIR` が指すディレクトリの `dev-mods/`）が加わりました。`plugins/mods/create` の Note も、`default` と `acceptEdits` のモードで mod のファイルごとに確認を求める理由を、「`~/.claude` が保護されたパスだから」から「mods のフォルダーが保護されたパスだから」に改めています — [日本語](https://code.claude.com/docs/ja/permission-modes#protected-paths) / [English](https://code.claude.com/docs/en/permission-modes#protected-paths)
- **権限モードの変更のイベントで `trigger` が付かない場合の説明が改められた**（`monitoring-usage` の「Permission mode changed event」）。「SDK やブリッジからの遷移では付かない」から、「SDK が `setPermissionMode()` で権限モードを設定したときなど、一部の変更では付かない」になりました — [日本語](https://code.claude.com/docs/ja/monitoring-usage#permission-mode-changed-event) / [English](https://code.claude.com/docs/en/monitoring-usage#permission-mode-changed-event)

**その他**

- **サンドボックスの `denyWrite` から `.env` の注意が外れた**（`agent-sdk/python` の `SandboxSettings`・`agent-sdk/typescript` の `SandboxFilesystemConfig`）。前回加わった「`.env` や `./.env` と書くと、サンドボックスの中のコマンドは作業ディレクトリの `.env` に書き込める」の文が外れ、Python は「サンドボックスが始まると、書いた各絶対パスへの書き込みをブロックする」で終わる形になりました。前回、日本語版にだけこの注意がなかったため英語版だけにリンクしていましたが、今回は日本語版と英語版が同じ内容です — [日本語](https://code.claude.com/docs/ja/agent-sdk/python#sandboxsettings) / [English](https://code.claude.com/docs/en/agent-sdk/python#sandboxsettings)
- **見出しマップ**: 変わっていません。前回のマップにだけ載っていた 7 見出しは、上に書いたとおり今回の `llms-full.txt` に入りました

**参考リンクについて**: 日本語版は、ハイライト・大幅更新・軽微な更新で取り上げたページのうち次の 13 ページ（`permissions`・`hooks`・`hooks-guide`・`permission-modes`・`sandboxing`・`sub-agents`・`errors`・`plugins/mods/events`・`agent-view`・`agent-sdk/permissions`・`agent-sdk/mcp`・`agent-sdk/python`・`monitoring-usage`）を取得し、該当する節があるかと今回の内容（新しい節や書き換えた文）になっているかを確かめました。今回も日本語版の追従が早く、新しい 7 つの見出しを含め、確かめた節はすべてすでに今回の内容でした。取得して確かめていないページ（`agent-sdk/typescript`・`agent-sdk/custom-tools`・`agent-sdk/hooks`・`plugins/mods/create`）にはリンクを付けていません。**changelog ページへのリンクは、本サマリの方針どおり付けていません。**
<!-- light:minor-updates:end -->

## 新着情報

<!-- light:whats-new:start -->
**今回、`whats-new/` 配下のページに変更はありません。**
<!-- light:whats-new:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-10-16.md](./archives/latest/2026-10-16.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-10-16.md](./archives/latest-detail/2026-10-16.md)

<!--
base_commit: 954ed4f3b5d84b7a8a63fa77f4b496af355f42d6
head_commit: df8be8b99ca6342f63f7c7b52da55b4609b1c128
generated_at_full: 2026-10-18T15:08:12+09:00
-->
