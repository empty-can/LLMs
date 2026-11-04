---
対象期間: 2026年11月02日 〜 2026年11月03日
作成日: 2026-11-03
---

# Claude Code 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
**今回は changelog に v2.1.318（2026年11月04日）の 1 リリースが積まれ、通常のページには、Claude Desktop のコマンドから作る SSH 接続の Windows 対応、Ubuntu の AppArmor の制限で bubblewrap が止まるときの対処、Agent SDK のフックのコールバックの `onFailure`、auto モードでフックが入力を変えた呼び出しの拒否、起動時に IDE の拡張機能を入れなくなった変更が載りました**。新しいページはなく、228 ページ中 40 ページ（changelog を含む）が変わり、changelog を除く変更はページ単位で 480 行（追加 368・削除 112）、大幅更新は `sandboxing`・`desktop`・`agent-sdk/hooks` の 3 ページです。見出しマップに加わった 12 の見出しは、すべて `llms-full.txt` にも入っています。総行数は 127,052 行から 127,408 行に増えました。

主要なものを以下に挙げます。

1. `sshHostCommands` が Windows の Claude Desktop v4.16336.0 以降でも使えるようになり、`desktop` に h5「Write the command on Windows」と、ホストだけを出力するバッチファイルの例の h5 が加わった
2. `sandboxing` の Ubuntu 24.04 のアコーディオンが h4「Add an AppArmor profile for bubblewrap」になり、制限のメッセージと `bwrap: setting up uid map: Permission denied` の 2 つのトラブルシューティングの h3 ができた
3. Agent SDK のフックのマッチャーの `onFailure: "block"`（Python は `on_failure="block"`）の解説が `agent-sdk/hooks` の新しい h3 に載り、失敗の扱い、挙動が違うイベント、起動時のエラーが説明された
4. `permissionDecision` のない `updatedInput` を返すフックの呼び出しを auto モードが拒みうること、`a hook changed this call's input after auto mode reviewed it` の意味と対処が `hooks`・`errors` などに載った
5. Claude Code は起動時に IDE の拡張機能を入れなくなり（v2.1.318）、`autoInstallIdeExtension` は外部のターミナルの `/ide` がインストールするかを決めるキーになった
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**Claude Desktop のコマンドから作る SSH 接続が Windows でも使えるようになった**](#1-claude-desktop-のコマンドから作る-ssh-接続が-windows-でも使えるようになった):  
  `sshHostCommands` の要件に、Windows の Claude Desktop v4.16336.0 以降が加わりました（OpenSSH クライアントでつなぐことも要ります）。`desktop` に h5「Write the command on Windows」ができ、Windows では `command` を `.exe`・`.cmd`・`.bat` のフルパスで始める、名前だけのエントリーは灰色になる、といった規則が載りました。ホストだけを出力するバッチファイルの例の h5 も加わっています
2. [**Ubuntu の AppArmor の制限で bubblewrap が止まるときの対処が節になった**](#2-ubuntu-の-apparmor-の制限で-bubblewrap-が止まるときの対処が節になった):  
  `sandboxing` の「Set up Linux and WSL2」の Ubuntu 24.04 のアコーディオンが h4「Add an AppArmor profile for bubblewrap」に置き換わり、トラブルシューティングに h3「Ubuntu's AppArmor restriction stops bubblewrap」と、`bwrap: setting up uid map: Permission denied` の h3 ができました。プロファイルを加えるか `sysctl` で制限を解除し、`/usr/bin/bwrap` 以外を動かしているなら `sysctl` を使います
3. [**Agent SDK のコールバックが失敗したら操作を止める onFailure の解説が載った**](#3-agent-sdk-のコールバックが失敗したら操作を止める-onfailure-の解説が載った):  
  `agent-sdk/hooks` に h3「Block the action when a callback fails」ができ、マッチャーに `onFailure: "block"`（Python は `on_failure="block"`）を設定すると、失敗したコールバックが操作を止める、と載りました（TypeScript の Agent SDK v0.3.317 以降、Python の Agent SDK v0.2.177 以降）。何も返さないコールバックも失敗に数えること、挙動が違うイベント、起動時のエラーも説明されています
4. [**auto モードでフックが入力を変えた呼び出しが拒まれる場合の説明が載った**](#4-auto-モードでフックが入力を変えた呼び出しが拒まれる場合の説明が載った):  
  `hooks` に h4「PreToolUse `updatedInput` in auto mode」ができ、フックが `permissionDecision` なしで `updatedInput` を返すと、サーバーがレビューしたのはフックが返した入力ではないので、Claude Code がその呼び出しを拒みうる、と載りました。`errors` の新しい h4 が `a hook changed this call's input after auto mode reviewed it` の対処を説明し、`permission-modes`・`plugins/mods/troubleshoot` も追従しています
5. [**Claude Code が起動時に IDE の拡張機能を入れなくなった**](#5-claude-code-が起動時に-ide-の拡張機能を入れなくなった):  
  `vs-code` の「Run CLI in VS Code」が、`claude` を起動しても拡張機能はインストールされない、と書き直されました。`autoInstallIdeExtension` は、外部のターミナルから `/ide` を実行したときに拡張機能をインストールさせるキーになり、`CLAUDE_CODE_IDE_SKIP_AUTO_INSTALL` も `/ide` がインストールしないようにする変数と改められています（changelog の v2.1.318）
<!-- light:highlight-list:end -->

## 1. Claude Desktop のコマンドから作る SSH 接続が Windows でも使えるようになった

**`sshHostCommands`（コマンドが出力するホストへつなぐ SSH 接続）の要件に、Windows の Claude Desktop v4.16336.0 以降が加わりました。** これまでは macOS か Linux の v3.6556.0 以降だけで、Windows では環境の選択に **Create** の項目が出ませんでした。Windows では、Desktop が OpenSSH クライアントでつないでいることも要ります。どちらも Claude アカウントでのサインインが要る点は同じです。

`desktop` にできた h5「Write the command on Windows」によると、Windows では `command` をドライブ文字から始まる `.exe`・`.cmd`・`.bat` のファイルのフルパスで始めます。Desktop は名前だけの指定を `PATH` から探さないので、`command` が `acme-dev create` のエントリーは灰色になります。例は `%USERPROFILE%\.claude\settings.json` のエントリーで、スペースのあるパスをシングルクォートで囲んだ `'C:\\Program Files\\Acme\\acme-dev.exe' create` です（JSON ではバックスラッシュを 2 回書くか `/` を使う）。パスのスペース・入力・時間の上限・プログラムが出力するものは「Write the command」の規則に従い、ほかは次の規則に置き換わります。

- **Program**: `\\server\share` のようなネットワークパス、`%USERPROFILE%` のような変数、ASCII の外の文字を使えない。どれかがパスにあるとエントリーは灰色になるので、ユーザーのフォルダーの名前にそのような文字があれば、プログラムをそのフォルダーの外に置く
- **Arguments**: 「Write the command」の規則に従い、`\` も書けるが、語の末尾には置けない
- **Scripts**: `.cmd` か `.bat` のファイルを使い、Desktop は `cmd.exe` で動かす。引用符の中でもファイルのパスに `&`・`^`・`;` は使えない。`%1` から `%9` は `,` と `=` で引数を分けるので、自分で書くファイルでは `%*` で読む
- **Environment**: プログラムはシェルのプロファイルではなく Desktop のアプリの環境変数を受け取る。変えたら Desktop を終了して開き直す
- **Test**: Command Prompt で `"C:\Program Files\Acme\acme-dev.exe" create < NUL > host.txt` のようにコマンドを実行すると、Desktop が読む出力を見られる。ファイルにはホストだけが要り、このテストもマシンを作るので、後でツールで削除する

h5「Wrap a Windows tool that prints other lines」は、ツールがホストの前に進捗のメッセージのような行を出力するなら、ホストだけを出力するバッチファイルで包む方法です。例の `make-devbox.cmd` はツールの出力の最後の行を出力し、ツールが失敗すればその終了コードで終わります。最後の 2 行は、ホストをコマンドとして動かさずに出力するためのものなので、そのまま保ちます。

ページのほかの部分と `settings-reference` の `sshHostCommands` も追従しました（大幅更新 2 参照）。

- [デスクトップアプリケーション - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/desktop#write-the-command-on-windows)
- [Desktop application - Claude Code Docs (English)](https://code.claude.com/docs/en/desktop#write-the-command-on-windows)
- [すべての設定 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/settings-reference#sshhostcommands)
- [All settings - Claude Code Docs (English)](https://code.claude.com/docs/en/settings-reference#sshhostcommands)

## 2. Ubuntu の AppArmor の制限で bubblewrap が止まるときの対処が節になった

**`sandboxing` の「Set up Linux and WSL2」にあった、Ubuntu 24.04 以降の bubblewrap のアコーディオンが外れ、h4「Add an AppArmor profile for bubblewrap」になりました。** プロファイルを加える条件は、Claude Code が `/usr/bin/bwrap` を動かしていて、制限が報告されたか、制限がオンの間に `bwrap: setting up uid map: Permission denied` か `bwrap: loopback: Failed RTM_NEWADDR: Operation not permitted` でサンドボックスの中のコマンドが失敗することです。Claude Code は、managed settings が `sandbox.bwrapPath` で名指していなければ `PATH` の最初の `bwrap` を動かすので、Claude Code を起動するシェルで `which bwrap` を実行して確かめます。`/usr/bin/bwrap` 以外を動かしているなら、プロファイルではなく `sysctl` で制限を解除します。プロファイルを書く `sudo tee /etc/apparmor.d/bwrap` のコマンドと `sudo systemctl reload apparmor` は前と同じで、その後に Claude Code を再起動してサンドボックスが動くことを確かめる、と加わりました。アコーディオンにあった、`sysctl kernel.apparmor_restrict_unprivileged_userns` で要否を確かめる手順と、プロファイルは `bwrap` 自体にだけ当たるという文は、この節にはありません。

**トラブルシューティングに 2 つの h3 ができました。**

- **「Ubuntu's AppArmor restriction stops bubblewrap」**: Linux と WSL2 で `Ubuntu's AppArmor restriction on user namespaces stops bubblewrap here` と出たら、Ubuntu の AppArmor の制限でサンドボックスが起動できない。解除するには、Claude Code が `/usr/bin/bwrap` を動かしていればプロファイルを加えるか、シェルで `sudo sysctl -w kernel.apparmor_restrict_unprivileged_userns=0` を実行する（マシンのすべてのプログラムの制限が再起動まで外れる）。解除するまで、コマンドはサンドボックスなしで通常の権限の流れで動くか、`sandbox.failIfUnavailable` が `true` なら Claude Code が起動を拒む
- **「Sandboxed commands fail with `bwrap: setting up uid map: Permission denied`」**: このエラーか `bwrap: loopback: Failed RTM_NEWADDR: Operation not permitted` は、この制限が原因のことがある。シェルで `sysctl kernel.apparmor_restrict_unprivileged_userns` を実行し、`kernel.apparmor_restrict_unprivileged_userns = 1` なら制限がオンなので同じ 2 つの方法で解除する。ほかの出力なら原因は制限ではないので、`/feedback` で報告する。v2.1.310 より前は Claude Code が起動時にこの制限を確かめなかったので、`/sandbox` はこれを報告しなかった

`errors` の「Find your error」の表にも、この 2 つの節へ案内する行が加わりました。`sandboxing` のほかの部分の変更は大幅更新 1 のとおりです。

- [サンドボックス化された Bash ツールを設定する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/sandboxing#add-an-apparmor-profile-for-bubblewrap)
- [Configure the sandboxed Bash tool - Claude Code Docs (English)](https://code.claude.com/docs/en/sandboxing#add-an-apparmor-profile-for-bubblewrap)
- [サンドボックス化された Bash ツールを設定する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/sandboxing#apparmor-restriction-stops-bubblewrap)
- [Configure the sandboxed Bash tool - Claude Code Docs (English)](https://code.claude.com/docs/en/sandboxing#apparmor-restriction-stops-bubblewrap)
- [サンドボックス化された Bash ツールを設定する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/sandboxing#bwrap-uid-map-permission-denied)
- [Configure the sandboxed Bash tool - Claude Code Docs (English)](https://code.claude.com/docs/en/sandboxing#bwrap-uid-map-permission-denied)

## 3. Agent SDK のコールバックが失敗したら操作を止める onFailure の解説が載った

**`agent-sdk/hooks` に h3「Block the action when a callback fails」ができました。** 多くのイベントでは、コールバックが例外を投げるか、検証に通らない出力を返しても操作は進み、アプリは `tag` が `hook_callback_failed` の `SDKInformationalMessage` の警告を受け取ります（Python では `SystemMessage.data` から `tag` を読む）。そのため、落ちた `PreToolUse` のガードは、ツールの呼び出しを通常の権限の流れへ通してしまいます。何も返さないコールバックも失敗に数えます。

代わりに操作を止めるには、マッチャーに `onFailure: "block"`（Python は `on_failure="block"`）を設定します。TypeScript の Agent SDK v0.3.317 以降か、Python の Agent SDK v0.2.177 以降が要ります。試すには、コールバックにエラーを起こさせて Claude に Bash のコマンドを動かしてもらうと、ツールの結果に `failed; blocking because onFailure is "block"` が入り、Claude にはエラーの文は見えません。意見がないときのコールバックは `{}` を返します。`"block"` を設定していると `return` のない経路は操作を止め、自分でエラーを捕まえて `{}` を返すコールバックは失敗にならないので、ガードではエラーをそのまま伝えます。

- **h4「Events that behave differently」**: `Stop`・`SubagentStop`・`TaskCompleted`・`TeammateIdle` はこのオプションを無視して操作が進む。`PermissionRequest` は `canUseTool` のコールバックが答える前に届いたときだけ止める。`PostToolUse` はツールが動いた後なので、Claude は失敗をフィードバックとして受け取る。タイムアウトは「Hook timeout」に従い、`"block"` があれば `PreCompact`・`Elicitation`・`WorktreeCreate` も止める
- **h4「Startup errors for `onFailure`」**: `"block"` を守れないとき、クエリーは起動時に失敗してプロンプトを送らない。Claude Code がオプションに対応していなければエラーに `does not honor` が入り（更新するかオプションを外す）、セッションがすでに動いていてフックを登録しなかったなら `did not register your hooks` が入る（新しいセッションを始める）

マッチャーの表にも `onFailure` の行が加わり、`agent-sdk/python` の `HookMatcher`、`agent-sdk/typescript` の `HookCallbackMatcher` にそれぞれのフィールドが、`SDKInformationalMessage` の型に `tag` が加わりました。`hooks` の h4「Block the action when a hook fails」からも、この節へのリンクが張られています。changelog の v2.1.317 の `onFailure: "block"` の追加（2026年11月02日 版のサマリでは、ページのない changelog だけの項目として扱ったもの）に対応します。

- [フックを使用してエージェントの動作をインターセプトして制御する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/agent-sdk/hooks#block-the-action-when-a-callback-fails)
- [Intercept and control agent behavior with hooks - Claude Code Docs (English)](https://code.claude.com/docs/en/agent-sdk/hooks#block-the-action-when-a-callback-fails)
- [Agent SDK リファレンス - TypeScript - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/agent-sdk/typescript#hookcallbackmatcher)
- [Agent SDK reference - TypeScript - Claude Code Docs (English)](https://code.claude.com/docs/en/agent-sdk/typescript#hookcallbackmatcher)
- [Agent SDK リファレンス - Python - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/agent-sdk/python#hookmatcher)
- [Agent SDK reference - Python - Claude Code Docs (English)](https://code.claude.com/docs/en/agent-sdk/python#hookmatcher)

## 4. auto モードでフックが入力を変えた呼び出しが拒まれる場合の説明が載った

**`hooks` に h4「PreToolUse `updatedInput` in auto mode」ができました。** auto モードでフックが `permissionDecision` なしで `updatedInput` を返すと、Claude Code は変えた呼び出しを拒むことがあります。サーバーがレビューしたのは Claude が書いた入力で、フックが返した入力ではないからです。Anthropic の API に直接つなぐ対話的なターミナルのセッションと VS Code のセッションでは、拒否に `a hook changed this call's input after auto mode reviewed it` の文が入ります。

- **拒否の後**: Claude は変えた呼び出しをもう一度出し、サーバーにレビューさせられる。Claude が次の応答で変えた入力をそのまま繰り返すとフックはまた動き、呼び出しを拒むか権限の確認へ送れるが、返した `updatedInput` は捨てられるので、動くのはサーバーがレビューしたものになる
- **フックを変える必要**: Claude が返事で auto モードは呼び出しを確かめられなかったと言わない限り、この拒否のためにフックを変える必要はない
- **拒否が出ない場合**: この文を示すセッションでは、設定かプラグインのフックのファイルの `command` のフックは、Bash・PowerShell・Monitor・Edit・Write・NotebookEdit の呼び出しをこの拒否なしで変えられる。ただし、同じ応答の前の呼び出しをフックが変えたときや、Bash のコマンドがサンドボックスの外で動くよう求めるときなどは、やはり拒否が出ることがある

`errors` の「The server returned no safety verdict」の下にも h4「`a hook changed this call's input after auto mode reviewed it`」ができました。これは安全でないという判定ではなく、レビューが動くものを覆っていないという意味で、同じ応答の後の呼び出しは `another call in this response was changed by a hook after auto mode reviewed it, or could not be confirmed unchanged` の理由で拒まれることがあります。Claude は拒まれた呼び出しをもう一度出せるので、権限の確認が開いたら答えるだけで済み、Claude が確かめられなかったと返事で言ったときは、変更を止める（フックか mod をオフにする。`/hooks` でフックを探し、ターミナルのセッションでは `/plugin` で動いている mod を見る）か、Manual モードに切り替えて自分で呼び出しを承認し、Claude に呼び出しを試し直すよう頼みます。同じ節には、10 回の数に入らない拒否がある、という文も加わりました。

`permission-modes` の「Server-side classifier review」にも、サーバーのレビューの後にフックか mod が入力を変えると、判定なしで拒むことがある、という段落が加わり、「When auto mode falls back」の 10 回の項目は「ターンを止める」から「止めることがある」に改められました。`plugins/mods/troubleshoot` の `a hook changed this call's input after the model wrote it` にも、一部のセッションでは同じ拒否の理由がこの文になり、繰り返した呼び出しは mod の最初の変更を運び、`tool.call` のフックはまた動くが、それ以上の変更は捨てられる、という注記が加わっています。`hooks` の `updatedInput` の表の説明にも、`permissionDecision` がなければ auto モードが変えた呼び出しを拒みうる、と加わりました。

- [フックリファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/hooks#pretooluse-updatedinput-in-auto-mode)
- [Hooks reference - Claude Code Docs (English)](https://code.claude.com/docs/en/hooks#pretooluse-updatedinput-in-auto-mode)
- [エラーリファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/errors#hook-changed-input-after-review)
- [Error reference - Claude Code Docs (English)](https://code.claude.com/docs/en/errors#hook-changed-input-after-review)
- [権限モードを選択する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/permission-modes#server-side-classifier-review)
- [Choose a permission mode - Claude Code Docs (English)](https://code.claude.com/docs/en/permission-modes#server-side-classifier-review)
- [mod のトラブルシューティング - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/plugins/mods/troubleshoot#a-tool-call-is-denied)
- [Troubleshoot a mod - Claude Code Docs (English)](https://code.claude.com/docs/en/plugins/mods/troubleshoot#a-tool-call-is-denied)

## 5. Claude Code が起動時に IDE の拡張機能を入れなくなった

**changelog の v2.1.318 は、IDE のターミナルで起動したとき Claude Code が IDE の拡張機能をインストールも更新もしなくなった、と述べています。** 代わりに外部のターミナルの `/ide` かエディターの拡張機能のビューを使います。通常のページもこれに合わせて改められました。

- **`vs-code` の「Run CLI in VS Code」**: 「CLI は IDE と自動で統合する」が、`claude` を起動しても拡張機能はインストールされない、に改められた。拡張機能がないと、統合ターミナルの `/ide` は「No available IDEs detected」と報告し、`/status` は IDE を「Not connected」と示す。差分の表示や診断の共有を使うには、統合ターミナルでは拡張機能をインストールしてから `claude` を起動し（自動でつながる）、外部のターミナルでは `/ide` を実行する（VS Code が拡張機能なしで動いていれば、`autoInstallIdeExtension` をオフにしていない限り `/ide` がインストールする）
- **`vs-code` の「Uninstall the extension」**: 統合ターミナルで `claude` を実行すると再インストールされる、という記述が、`claude` を起動してもアンインストールされたままで、VS Code が動いている間に外部のターミナルから `/ide` を実行すると再インストールされる、に改められた。止めるには `~/.claude.json` の `autoInstallIdeExtension` を `false` にするか、統合ターミナルの `/config` で **Auto-install IDE extension** をオフにするか、`CLAUDE_CODE_IDE_SKIP_AUTO_INSTALL` を `1` にする
- **`settings-reference` の `autoInstallIdeExtension`**: 外部のターミナルからコマンドを実行したとき、`/ide` が動いている VS Code・Cursor・Devin Desktop に拡張機能をインストールできるようにするキーになり、`true`・`false` の説明も `/ide` がインストールするか、に替わった。「Settings index」の行も同じ
- **`env-vars` の `CLAUDE_CODE_IDE_SKIP_AUTO_INSTALL`**: IDE の拡張機能の自動インストールを飛ばす変数から、`/ide` が拡張機能をインストールしないようにする変数に改められた

- [VS Code で Claude Code を使用する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/vs-code#run-cli-in-vs-code)
- [Use Claude Code in VS Code - Claude Code Docs (English)](https://code.claude.com/docs/en/vs-code#run-cli-in-vs-code)
- [すべての設定 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/settings-reference#autoinstallideextension)
- [All settings - Claude Code Docs (English)](https://code.claude.com/docs/en/settings-reference#autoinstallideextension)

## 新規追加されたページ

<!-- light:new-pages:start -->
（今回の対象期間に新規追加・削除されたドキュメントページはありません。`llms.txt` は変わっておらず、`llms-full.txt` に展開されている固有のページも 228 のままで、`Source:` の行が 231 あり 3 ページが 2 回展開されている状態も前回と同じです）
<!-- light:new-pages:end -->

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
- [**Configure the sandboxed Bash tool**](#1-configure-the-sandboxed-bash-tool) ([日本語](https://code.claude.com/docs/ja/sandboxing#set-up-linux-and-wsl2) / [English](https://code.claude.com/docs/en/sandboxing#set-up-linux-and-wsl2)):  
  86 行（追加 59・削除 27）が変わりました。ハイライト 2 の h4 と 2 つの h3 のほか、Dependencies のタブの読み方と、サンドボックスが起動できないときの言い方が改められました
- [**Desktop application**](#2-desktop-application) ([日本語](https://code.claude.com/docs/ja/desktop#write-the-command) / [English](https://code.claude.com/docs/en/desktop#write-the-command)):  
  76 行（追加 66・削除 10）が変わりました。ハイライト 1 の 2 つの h5 のほか、macOS と Linux でもスペースのあるパスを引用符で書けるようになり、配布と灰色のエントリーの説明が Windows に合わせて改められました
- [**Intercept and control agent behavior with hooks**](#3-intercept-and-control-agent-behavior-with-hooks) ([日本語](https://code.claude.com/docs/ja/agent-sdk/hooks#block-the-action-when-a-callback-fails) / [English](https://code.claude.com/docs/en/agent-sdk/hooks#block-the-action-when-a-callback-fails)):  
  50 行（追加 49・削除 1）が変わりました。ほぼすべてがハイライト 3 の h3 と 2 つの h4 で、ほかはマッチャーの表の行と「Hook timeout」の文です
<!-- light:updated-pages:end -->

**行数の数え方**: `llms-full.txt` の生の差分（追加 468 行・削除 112 行）のハンクを、head 側の `Source:` 行でページに振り分けた値です（ページの並びは変わっておらず、ページ単位の合計は生の差分と一致します）。base と head はどちらも引用ブロックの書式なので、正規化はしていません。この値が 50 行以上のページを大幅更新として挙げました。changelog（追加 100 行）は新しい 1 リリースの分なので大幅更新には入れず、「軽微な更新」で扱っています。空行（と `>` だけの行）を除くと、`desktop` は 64 行、`sandboxing` は 60 行、`agent-sdk/hooks` は 35 行で、`agent-sdk/hooks` は 50 行に届きませんが、これまでどおり生の行数で判定しました。次点は `errors` の 44 行（追加 37・削除 7）、`self-hosted-environments-configuration` の 24 行（追加 19・削除 5）、`hooks` の 21 行（追加 19・削除 2）です。

## 1. Configure the sandboxed Bash tool

ページの差分のうち、h4「Add an AppArmor profile for bubblewrap」と 2 つのトラブルシューティングの h3 はハイライト 2 のとおりです。そのほかは次のとおりです。

- **「Set up Linux and WSL2」の Dependencies のタブ**: 必要な依存関係がなければ Dependencies のタブだけが出る、という文が 2 つの項目になった。Dependencies が唯一のタブならサンドボックスは起動できないので、タブが足りないと示すものをインストールするか、Ubuntu の AppArmor の制限を報告していればプロファイルを加える。ほかのタブと並ぶなら、タブは seccomp フィルターのような省ける項目の欠けを示しており、サンドボックスはそれなしで起動できるので、それが加えるものが欲しいときだけインストールする
- **「Get started」**: パネルに Dependencies のタブしかないときの理由が「必要なパッケージがない」から「サンドボックスがまだ起動できない」に、対処が「タブの報告を直す」に改められた
- **サンドボックスが起動できないときの言い方**: 「Get started」の警告と「Enforce sandboxing with managed settings」の `failIfUnavailable`、`settings-reference` の `sandbox.failIfUnavailable` が、「依存関係がないかプラットフォームに対応していない」から、「プラットフォームが対応していないか、起動時の依存関係のチェックが失敗した」に揃えられた

- [サンドボックス化された Bash ツールを設定する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/sandboxing#set-up-linux-and-wsl2)
- [Configure the sandboxed Bash tool - Claude Code Docs (English)](https://code.claude.com/docs/en/sandboxing#set-up-linux-and-wsl2)
- [サンドボックス化された Bash ツールを設定する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/sandboxing#enforce-sandboxing-with-managed-settings)
- [Configure the sandboxed Bash tool - Claude Code Docs (English)](https://code.claude.com/docs/en/sandboxing#enforce-sandboxing-with-managed-settings)

## 2. Desktop application

ページの差分のうち、h5「Write the command on Windows」「Wrap a Windows tool that prints other lines」はハイライト 1 のとおりです。そのほかは次のとおりです。

- **「Create an SSH connection from a command」**: 要件の注記に、Windows の v4.16336.0 以降と OpenSSH クライアントでつなぐことが加わった。JSON の例の後には、Windows では `acme-dev` のような名前だけでは動かないのでプログラムのフルパスで始める、と加わった
- **「Write the command」**: 冒頭に、Windows では「Write the command on Windows」から始める、と加わり、これまでの規則は macOS と Linux の規則になった。新しい **Spaces in the path** の項目で、パスにスペースがあるならプログラムのフルパスをシングルクォートで囲める（`'/Users/you/My Tools/make-devbox' create` など。引用符は一重でも二重でも Claude Desktop v4.16336.0 以降が要り、プログラムのパスの周りでだけ使える）。**Arguments** は、引用符の外で使える文字の説明になり、引用したパスは `(`・`)`・`&` のような文字も持てる、と加わった。**Scripts** の、スクリプトに入れるものの例は「引用符」から「引用した引数」になった
- **「Connect to a new host」**: **Host key** の項目に Windows の `%USERPROFILE%\.ssh\known_hosts` が加わり、続きが 3 つの子項目に分かれた
- **「Distribute commands to your team」**: **The program** の項目が、macOS と Linux では各利用者の `PATH` から探し、Windows では名前だけのエントリーは灰色になる、に改められた。新しい **Each platform** の項目は、Windows と macOS・Linux に別のエントリーを配る（Windows のパスのエントリーは macOS と Linux で灰色になり、その逆も同じ）よう求める
- **「If a command is missing or gray」**: **Platform and account** の項目が **Account**（サードパーティのプロバイダー）と **Windows**（Desktop が v4.16336.0 より古いか、OpenSSH クライアントでつないでいない）に分かれた。灰色のエントリーの **A mistake in the entry** にも、Windows ではプログラムのフルパスで始める、と加わった
- **「Managed settings」の表**: `sshHostCommands` の行に Windows の要件が加わった

`settings-reference` の `sshHostCommands` にも Windows の要件と、Windows ではフルパスで始める、という文が加わりました。このキーの説明は、接続を作るかそのホストを置き換えるとき、から、接続を作るか別のマシンを作るとき、に改められ、**Type** の `command` も、シェルなしで始める、から、シェルの構文として読まないのでパイプと変数は動かない、に改められています。

- [デスクトップアプリケーション - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/desktop#write-the-command)
- [Desktop application - Claude Code Docs (English)](https://code.claude.com/docs/en/desktop#write-the-command)
- [デスクトップアプリケーション - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/desktop#if-a-command-is-missing-or-gray)
- [Desktop application - Claude Code Docs (English)](https://code.claude.com/docs/en/desktop#if-a-command-is-missing-or-gray)

## 3. Intercept and control agent behavior with hooks

ページの差分のうち、h3「Block the action when a callback fails」と 2 つの h4 はハイライト 3 のとおりです。そのほかは次のとおりです。

- **「Matchers」の表**: `onFailure` の行が加わった（型は `"continue" \| "block"`、既定は `undefined`。Python では `on_failure`）
- **「Hook timeout」**: ほかのイベントでは失敗を記録して続ける、という項目に、`onFailure: "block"` があれば `PreCompact`・`Elicitation`・`WorktreeCreate` のタイムアウトは操作を止める、と加わった

- [フックを使用してエージェントの動作をインターセプトして制御する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/agent-sdk/hooks#hook-timeout)
- [Intercept and control agent behavior with hooks - Claude Code Docs (English)](https://code.claude.com/docs/en/agent-sdk/hooks#hook-timeout)

## 軽微な更新

<!-- light:minor-updates:start -->
今回の差分は **2 ファイル**（`llms-full.txt` と見出しマップ）で、`llms.txt` は変わっていません。`llms-full.txt` の生の差分は追加 468 行・削除 112 行で、ページの並びは変わっていません。228 ページ中 **40 ページ**が変わり、changelog が 100 行（追加のみ）、ほかの 39 ページが 480 行（追加 368・削除 112）で、ページ単位の合計は生の差分と一致します（2 回展開されている 3 ページはどれも変わっていません）。大幅更新の 3 ページを除く **36 ページ**と、changelog に加わった **v2.1.318（2026年11月04日）** を以下にまとめます。

`llms-full.txt` の総行数は **127,052 行から 127,408 行へ 356 行増え**ました（生の差分の差し引き 468 − 112 と一致）。`Source:` の行は 231、固有のページは 228 のままで、2 回展開されている 3 ページ（`plugins/create`・`plugins/install`・`plugins/mods/overview`）も前回と同じです。コードフェンスの外の見出しは、引用の中の見出しも数えると 6,031 から 6,043 へ、行頭が `#` の見出しだけを数えると 6,020 から 6,032 へ、どちらも 12 増えました（加わった 14・外れた 2。外れた 2 つは改称された見出しです）。changelog の収録リリースは 435 から 436 になりました。v2.1.318 は 84 項目（追加 11・変更 11・改善 15・バグ修正 47）で、単一のリリースなので各項目への版の併記は省いています。v2.1.318 の項目で今回の通常のページの変更に対応するのは、IDE の拡張機能（ハイライト 5）と `mantle` の上流の `assume_role` で、多くは changelog だけで確認できる変更です。

**新機能**

- Claude Desktop の Windows での `sshHostCommands`（`desktop`・`settings-reference`。詳細はハイライト 1 参照）
- Agent SDK のフックの `onFailure`（`agent-sdk/python`・`agent-sdk/typescript`・`hooks`。詳細はハイライト 3 参照）
- **Claude apps gateway の `mantle` の上流に `assume_role` が加わった**（`claude-apps-gateway-config` の「Amazon Bedrock Mantle endpoint」）。`mantle` の上流の表に行が加わり、キーは `bedrock` の上流と同じで、開発者ごとの帰属のための `session_name` も含み、ロールには Mantle の IAM のアクションを与えます。ゲートウェイのサーバーに Claude Code v2.1.318 以降が要り、前の版は起動時に `Unrecognized key(s) in object: 'assume_role'` で終わります。`mantle` の上流は `assume_role` を取らず開発者ごとに帰属しない、という項目は、`mantle` の上流自身に設定する、それがなければ `mantle` の上流の `auth` の資格情報で送る、に改められ、「Bedrock in another AWS account」の、`assume_role` は `provider: bedrock` だけに当たる、という文も外れました。changelog の v2.1.318 の、別の AWS アカウントのロールと開発者ごとの AWS のコストの帰属のための `assume_role` の追加に対応します — [日本語](https://code.claude.com/docs/ja/claude-apps-gateway-config#amazon-bedrock-mantle-endpoint) / [English](https://code.claude.com/docs/en/claude-apps-gateway-config#amazon-bedrock-mantle-endpoint)
- **Claude Desktop の Code タブの、remote managed settings の警告が載った**（`errors` の「Remote managed settings failed to load」・`server-managed-settings` の「Fetch and caching behavior」）。警告が対話的なセッションだけでなく Code タブにも出るとなり、Code タブではメッセージを送ると会話の行として出て、取得の状態が変わると新しい行が出ます。関連する 3 つのメッセージは、`Remote managed settings are still loading`（取得の途中でセッションが進んだ）、`Remote managed settings did not load`（取得が答えなしに終わった）、`Remote managed settings have now loaded`（警告の後に読み込まれた。行の残りがリモートのポリシーが当たるかを述べる）です。「Find your error」の表には、前の 2 つと、`Your organization requires remote managed settings to load, but they could not be loaded` の行が加わりました。changelog の v2.1.317 の Code タブの通知の追加に対応します — [日本語](https://code.claude.com/docs/ja/errors#remote-managed-settings-failed-to-load) / [English](https://code.claude.com/docs/en/errors#remote-managed-settings-failed-to-load)
- セッションで書いた mod をオンにするかを尋ねられたときの答えの記録を追加
- mod の `$.model.fork` に `effort` のオプションを追加。短い横の作業を、セッションの effort にかかわらず `low` で動かせます。結果は送った effort を報告します
- `claude auth status`（`loginExpiresAt`）と `claude -p` の JSON の結果（`credential_expires_at`）に、保存した claude.ai のサインインが切れる日を追加
- `claude -p` のテキストの出力に、保存した claude.ai のサインインが切れる 10 日前から出る、stderr の 1 行の警告を追加
- Gateway: フェデレーション（`external_account`）の資格情報のファイルの Google のアクセストークンが切れそうなときのログの警告を追加
- Self-hosted runner: オーケストレーターの spawn-runner のフックの環境に `CLAUDE_RUNNER_SPAWN_REASON` を追加。Anthropic が要求を送った理由（`runner_lost`・`resumed` など）で、送られなければ未設定です
- Self-hosted runner: `--release-idle-session-min` が値のない最後の引数（引き続き無視）か、値が空白だけ（引き続き `0` と読む）のとき、起動時の警告を追加
- [Cloud sessions] No repository の選択肢を追加。Anthropic がホストする環境のクラウドのセッションは、リポジトリを選ばずに始められます
- [Cloud sessions] クラウドのセッションに通常の Chrome の名前を追加。Playwright 以外のツールも、google-chrome と CHROME_PATH で組み込みの Chromium を見つけられます
- [Cloud sessions] クラウドのセッションの環境が削除されたときのカード（メッセージの欄が隠れる）に New session のボタンを追加

**機能改善**

- Ubuntu の AppArmor の制限のメッセージの案内（`errors`・`settings-reference`。詳細はハイライト 2 参照）
- auto モードの `updatedInput` の拒否（`errors`・`permission-modes`・`plugins/mods/troubleshoot`。詳細はハイライト 4 参照）
- IDE の拡張機能を起動時に入れない変更（`vs-code`・`settings-reference`・`env-vars`。詳細はハイライト 5 参照）
- **サブエージェントと teammate の effort が、別のモデルではセッションのレベルを受け継がないと載った**（`model-config` の新しい h4「Effort level of subagents and teammates」・`sub-agents` の新しい h4「When a subagent has no `effort` field or parameter」）。主な会話のモデルなら、自分の `effort` のないサブエージェントや teammate はセッションで選んだか `--effort` で設定したレベルで動き、別のモデルではそのレベルは効きません。サブエージェントのレベルを選ぶには定義に `effort` を設定します。`agent-teams` の「Specify teammates and models」は、リーダーのモデルの teammate がリーダーの effort を受け継ぐ、に、`cli-reference` の `--effort` は「主な会話のモデルでは」設定を上書きする、に改められ、`model-config` の解決の順の節からもこの節へのリンクが張られました。changelog の v2.1.317 の、主な会話と違うモデルのサブエージェントと teammate の effort の変更に対応します — [日本語](https://code.claude.com/docs/ja/model-config#effort-level-of-subagents-and-teammates) / [English](https://code.claude.com/docs/en/model-config#effort-level-of-subagents-and-teammates)
- **agent team の権限の説明が書き直された**（`agent-teams` の「Permissions」・「Have teammates plan before implementing」・「Limitations」）。動いている teammate の権限モードは `Shift+Tab` で切り替えます（split-pane の teammate はそのペインで、in-process の teammate はそのセッションを見ている間に押し、次のターンの始めにモードを確かめる）。注記によると、plan モードでない in-process の teammate は、リーダーが `acceptEdits`・`auto`・`bypassPermissions` の間はリーダーのモードで動き、teammate を Manual にしてもステータスバーの表示にかかわらず変わりません。編集の前に尋ねさせるには、エージェントのパネルの `main` の行で Enter を押してリーダーも Manual にします（リーダーも、Manual のほかの teammate も尋ねるようになる）。新しい teammate はリーダーのモード（`--dangerously-skip-permissions` がオンにする `bypassPermissions` も含む）で始まり、リーダーが `dontAsk` なら Manual で始まります。plan の節では、読み取り専用の plan モードで動く、が plan モードで動く、に改められ、計画が承認されると Claude Code がリーダーの今の権限モード（plan なら Manual）を渡す、と加わって、編集とコマンドは権限の確認を通る、という文が外れました。「Limitations」の項目の名前は **No per-teammate permission modes at spawn** になっています — [日本語](https://code.claude.com/docs/ja/agent-teams#permissions) / [English](https://code.claude.com/docs/en/agent-teams#permissions)
- **mod の `agent.spawn` が、サブエージェントの再開でも動くと改められた**（`plugins/mods/reference` の「Subagents」）。これまでは `SendMessage` で再開するとフックは動かない、とありましたが、v2.1.299 以降は、終わったか止まったサブエージェントがまた動く前にも動き、`e.resume` が `{ agentId }` になります。サブエージェントを数えるフックは `e.resume` のあるイベントを飛ばします。`{ deny: reason }` で再開を拒むと実行は始まらず、`SendMessage` の呼び出しが頼んだものなら、Claude はその結果として `a plugin declined the resume:` に続く理由を読みます。再開で `next` に変えたイベントを渡しても無視されます。v2.1.299 より前の版で再開を拒むには、前のとおり `tool.call` のフックでそのツールに合わせます — [日本語](https://code.claude.com/docs/ja/plugins/mods/reference#subagents) / [English](https://code.claude.com/docs/en/plugins/mods/reference#subagents)
- **クラウドのスケジュールしたタスクがオフのときのメッセージが改められた**（`errors`・`routines`）。見出しが「Routines are disabled by your organization's policy」から「Scheduled tasks are off for your organization」に替わり、メッセージは `Scheduled tasks are off for your organization. …` か `Routines are off for your organization. …` で、管理者についての文が続きます。トグルの名前は **Scheduled tasks (Was Routines)** か **Routines** の 2 通りになり、Team か Enterprise の Owner にオンにできるかを尋ねる、と改められました。この 2 つの節からは、v2.1.227 以降は同じ設定が `/schedule` を隠す、という文が外れています。リンクの id は旧見出しのままです — [日本語](https://code.claude.com/docs/ja/errors#routines-are-disabled-by-your-organizations-policy) / [English](https://code.claude.com/docs/en/errors#routines-are-disabled-by-your-organizations-policy)、[日本語](https://code.claude.com/docs/ja/routines#troubleshooting) / [English](https://code.claude.com/docs/en/routines#troubleshooting)
- **セルフホストのランナーのラッパーとフックの動く回数が改められた**（`self-hosted-environments-configuration`）。ラッパーは「セッションごとに 1 回」ではなく、再開か再キューも含めてセッションを始めるたびに起動します。`checkout` のフックも同じく各リポジトリについてセッションを始めるたびに、`command` のフックはセッションの開始か再開のたびに動き、`post-session` のフックの説明からも「セッションごとに 1 回」が外れて、`--capacity` が 2 以上と 1 の場合が項目に分かれました。「Send model requests to Bedrock or Agent Platform」の **Wrapper script** の項目も、ラッパーが書き出す資格情報の値は Claude Code が動いている間は更新されないので、長いセッションでは自分で更新する方法を使う、に改められています — [日本語](https://code.claude.com/docs/ja/self-hosted-environments-configuration#wrapper-scripts) / [English](https://code.claude.com/docs/en/self-hosted-environments-configuration#wrapper-scripts)
- **セルフホストのランナーの `last_poll_age_ms` を liveness probe に使わないと改められた**（`self-hosted-environments-reference` の「Health endpoint」）。アラートには使いますが、値は最後に成功したポーリングからの時間で、ランナーが Anthropic に届かない間も増えるので、liveness probe は HTTP のステータスコードのままにします。`last_poll_at` と `last_poll_age_ms` は最初のポーリングが成功するまで `null` で、最初から失敗するポーリングを捕まえるには `claude_code_self_hosted_runner_poll_errors_total` にもアラートを設定します。`self-hosted-environments-deploy` の「Some sessions don't count as idle」でも、「終わらない」バックグラウンドのタスクが「動き続ける」タスクに言い換えられています — [日本語](https://code.claude.com/docs/ja/self-hosted-environments-reference#health-endpoint) / [English](https://code.claude.com/docs/en/self-hosted-environments-reference#health-endpoint)
- **連携した GitHub のアカウントのページには Owner の役割が要ると改められた**（`admin-setup` の「Connected GitHub accounts」・`web-quickstart` の「Connect GitHub」）。ページを開くには Claude の組織の Owner の役割が要り、Admin の役割では開けません。**Admin connection** の項目は **Owner connection** になり、GitHub の組織をこの方法でつなぐには、その GitHub の組織も持つ Claude の組織の Owner が要ります。`web-quickstart` も、一覧でアカウントを見るのは Claude の組織の Owner、に改められました — [日本語](https://code.claude.com/docs/ja/admin-setup#connected-github-accounts) / [English](https://code.claude.com/docs/en/admin-setup#connected-github-accounts)
- **Bedrock のガードレールの適用先が、ゲートウェイの有無で分けられた**（`amazon-bedrock` の「AWS Guardrails」）。Claude apps gateway を通すなら `claude-apps-gateway-config` の「Apply an Amazon Bedrock guardrail」に従い、なければ設定ファイルにガードレールのヘッダーを加えます。ゲートウェイのポリシーでヘッダーを配ると承認の要る設定に数えられる、という文は外れました — [日本語](https://code.claude.com/docs/ja/amazon-bedrock#aws-guardrails) / [English](https://code.claude.com/docs/en/amazon-bedrock#aws-guardrails)
- **読み込んだファイルの確かめ方が `/context all` になった**（`debug-your-config` の「See what loaded into context」・`memory`・`large-codebases`・`best-practices`）。全画面モードでは `/context` が項目ごとの内訳を畳むので、`/context all` で開く、と `debug-your-config` に加わり、ほかのページの確かめ方も `/context all` に替わりました。`memory` の「View and edit with `/memory`」からは、起動時に読み込んだファイルは `/context` で確かめる、という文が外れています — [日本語](https://code.claude.com/docs/ja/debug-your-config#see-what-loaded-into-context) / [English](https://code.claude.com/docs/en/debug-your-config#see-what-loaded-into-context)、[日本語](https://code.claude.com/docs/ja/memory#set-up-a-project-claude-md) / [English](https://code.claude.com/docs/en/memory#set-up-a-project-claude-md)
- **`Ctrl+R` の検索の説明が改められた**（`interactive-mode` の「Reverse search with Ctrl+R」）。全画面のダイアログに、ハイライトした一致の先頭を示すプレビューのペインが載り、インラインの検索の手順は、検索語が結果で強調される、から、今の一致がプロンプトの入力に出る、に改められました。履歴を新しい順に検索して重複をまとめる、という段落は外れています — [日本語](https://code.claude.com/docs/ja/interactive-mode#command-history) / [English](https://code.claude.com/docs/en/interactive-mode#command-history)
- **`ENABLE_BETA_TRACING_DETAILED` を本番で使わないよう警告が加わった**（`monitoring-usage` の `claude_code.hook` のスパン）。デバッグのときだけ設定します。詳細なベータのトレースはエクスポートの量が多く、その内容の属性は安定したスパンのスキーマの一部ではありません — [日本語](https://code.claude.com/docs/ja/monitoring-usage#traces-beta) / [English](https://code.claude.com/docs/en/monitoring-usage#traces-beta)
- **MCP の `stdio` サーバーで `CLAUDE_PROJECT_DIR` を展開できると載った**（`plugins/manifest-reference` の「Where each variable resolves」）。表の行に、`CLAUDE_PLUGIN_ROOT`・`CLAUDE_PLUGIN_DATA` に並んで加わりました — [日本語](https://code.claude.com/docs/ja/plugins/manifest-reference#where-each-variable-resolves) / [English](https://code.claude.com/docs/en/plugins/manifest-reference#where-each-variable-resolves)
- **`/batch` の各単位の終わり方が改められた**（`commands`・`best-practices`）。各サブエージェントは変更を公開するのではなく、PR を開くか、何が起きたかを報告します — [日本語](https://code.claude.com/docs/ja/commands#all-commands) / [English](https://code.claude.com/docs/en/commands#all-commands)
- **終了時の `Background work is running` のダイアログの説明が改められた**（`agent-view` の「Send the session to the background」）。バックグラウンドの作業があれば、という説明が、サブエージェントやワークフローのような一部の種類の作業が動いている間に終了すると、作業が止まると警告する、に改められ、例からシェルのコマンドとモニターが外れました — [日本語](https://code.claude.com/docs/ja/agent-view#send-the-session-to-the-background) / [English](https://code.claude.com/docs/en/agent-view#send-the-session-to-the-background)
- Claude Code が IDE のターミナルで起動したとき、IDE の拡張機能をインストールも更新もしないよう変更（詳細はハイライト 5 参照）
- 「Switch models when a message is flagged」が「Ask each time」のとき、サブエージェントがモデルを切り替えずに止まるよう変更
- バックグラウンドのサブエージェントが、どのプロバイダーでも 3 分後にシェルのコマンドをバックグラウンドへ移すよう変更。コマンドが動く間にプロンプトキャッシュが切れません
- Bedrock・Vertex・Foundry かテレメトリーがオフのときのサブエージェントの進捗の要約を変更。冷えたプロンプトキャッシュでは、サブエージェントの返答を最大 5 分待てます
- mod が `prompt.submit` で添えるものが、システムメッセージにならず利用者のターンに留まるよう変更
- `deniedMcpServers` の URL の項目が、上流の URL が合う Anthropic 提供のサーバーと、クラウドのセッションとセルフホストのランナーのコネクター（セッションがコネクター自身の URL を受け取るもの）も止めるよう変更。ほかはコネクターを名前で拒みます
- `/permissions` のルールの詳細・組み込みのルール・削除の確認の画面が標準のダイアログを使うよう変更。そこで Ctrl+C を 2 回押すと、終了ではなく戻るか取り消します
- `/claude-api managed-agents-onboard` が、新しいエージェントの組み込みのツールとクイックスタートのテンプレートの MCP のツールに、既定で `auto` の権限ポリシー（「Judge risky actions」）を与えるよう変更。Claude Console に合わせたもので、「run without asking」と言えば外せます
- 2.1.286 以前に始めた会話を再開するときモデルの前の思考を保つ、2.1.288 の修正を廃止。その思考は落ちることがあります
- Self-hosted runner: オーケストレーターのログの行を変更。`ok session=…` はどのログレベルでも stdout に出て（これまでは debug だけで stderr）`jti=…` の後に `reason=…` が付き、`nack session=…` は `retryable=…` の後の `reason=…` でフィールドが終わります。`retryable=true:` か `retryable=false:` に合わせるスクリプトは更新します
- [Cloud sessions] コネクターの検索の結果が、検索はコネクターのディレクトリの一部しか覆わないと Claude に伝えるよう変更
- 共有のネットワークのホームディレクトリで、`~/.claude.json`・設定ファイル・保存したログインが保存を生き延びるよう改善。削除される、一時的に空になる、ほぼ空か古いコピーに置き換わることが減ります
- ネットワークのファイルシステムのセッションで、設定ファイルがないと誤って報告されたときに見直すよう改善。MCP サーバーと信頼したフォルダーなしで始まるセッションが減ります
- MCP のツールのエラーを改善。ツールを読み込む前の呼び出しは、その入力のスキーマを返します
- Bash のツールが macOS の組み込みの `/bin/bash` を動かすときの、git のコミットとプルリクエストの作成の信頼性を改善
- 使用量の上限のメニューの「Ask your admin for more usage」が、要求を 1 回の操作で送るよう改善
- 一時停止かスリープの後のリモートのセッションの再接続の速さを改善
- You should know のトーストが、ターミナルでしか効かない「press 2」ではなく「try again」と言うよう改善
- 自動更新の信頼性を改善。リリースの検証中の短いネットワークの失敗は、次の確認を待たずにすぐ再試行します
- 無人の実行（`claude -p`・SDK のアプリ）が、何も変わらないのに実行のたびに `~/.claude.json` を書き直さないよう改善
- Gateway: `listen.trusted_proxies` のログのヒントを改善。接続元のアドレスを自分で `X-Forwarded-For` に加えるプロキシだけを並べる、と伝えます
- Gateway: Amazon Bedrock で AWS の CountTokens が失敗したときの警告を改善。501 の後に数えるのはゲートウェイではなく Claude Code だと伝え、AWS がアクセスを拒んだときだけ IAM を指します
- Remote Control: アプリが名前を付けないとき、ターミナルのフォークのフォークに付くタイトルを「Name (fork 2)」に改善
- [VSCode] サインインの状態の確認が失敗したとき、サインインの画面が Claude Code の出力を示すよう改善
- [Cloud sessions] クラウドと Remote Control のセッションの Create PR の失敗のメッセージの多くを改善。Try again ではなく、理由か GitHub へのリンクを示します
- [Code Review] Code Review の分析のページが、サーバーかネットワークの失敗の後に 1 回再試行し、空のカードではなく Try again のバナーを示すよう改善

**バグ修正**

- 不正なツールの呼び出しの再試行が尽きた後、`--continue` が前の会話を失うことがある問題を修正（2.1.314 の退行）
- 動いている Bash のコマンドの多い macOS のセッションが、メモリーが増える間に止まる問題を修正
- メッセージを送った直後か、遅い確認が出る前に打ったキーが権限の確認に答えてしまう問題を修正
- 共有のネットワークのホームディレクトリで設定ファイルを更新できないとき、`/logout`・`claude auth logout`・`claude mcp remove` が成功と報告し、信頼・同意・MCP の設定の変更が何も言わずに捨てられる問題を修正
- 同じホームで別のターミナルかホストが同じアカウントと組織に再度サインインすると、ジョブが `Not logged in` で終わる問題を修正
- `claude mcp add` と `remove` がロックなしで設定を書く問題を修正。ロックを待つか 1 で終わります（ほかのジョブの保存が、保存したサーバーを置き換えることはまだありえます）
- 遅いトークンの更新が保存される前に `claude plugin` のコマンドが終わり、次の実行でサインアウトしうる問題を修正
- `claude plugin marketplace add` が拒む、独自の名前のマーケットプレイスのファイルを `claude plugin validate` が通す問題を修正
- バージョンの確認で終了する stdio の MCP サーバーが起動のたびに確認し直される問題を修正。自分の理由で 3 秒未満で落ちるサーバーも、7 日間は古いハンドシェイクに固定されます
- 同じマシンの別のログインが保存した `allowedProviders` の一覧で、セッションが起動時に拒まれる問題を修正
- アイドルの圧縮が、要約でない返事で会話を置き換える問題を修正
- バックグラウンドのサブエージェントが動く間、「Now using usage credits」の通知が 30 秒ほどごとにまた出る問題を修正
- 失敗するか Claude だけが呼び出せる独自のスラッシュコマンドが、`claude -p` と SDK のセッションで何も出力しない問題を修正
- mod が `turn.step` をフックしている間に API のエラーが返事を切ると、`claude -p` と Agent SDK のセッションが成功と報告する問題を修正
- ヘッドレスのセッションで、モデルの変更の直後に送ったメッセージが Stop の後も動く問題を修正。Stop は、キューのメッセージと同じように取り消すか止めます
- アイドルの非対話のセッションが終わるとき、削除したセッションのトランスクリプトが最後のプロンプトで作り直される問題を修正
- 更新かバージョンの片付けが動いているプロセスのバイナリを消した後、`claude remote-control` のホスト・バックグラウンドのデーモン・セルフホストのランナーが新しいセッションを始められない（`spawn ENOENT`）問題を修正
- 別の利用者が持つ動いている Claude Code のプロセス（`sudo claude` が残したものなど）がバージョンの片付けで死んだと扱われ、そのバイナリが削除されうる問題を修正
- 接続の失敗の後も `/remote-control` がセッションを使えると示す問題を修正
- 要求が 404 で失敗したのに `/design revoke` が成功と報告する問題を修正
- セルフホストのランナーかクラウドのセッションの再起動の後に承認したシェルのコマンドが、頼まれたフォルダーではなくセッションの開始のフォルダーで動く問題を修正。そのフォルダーに入れなければ動きません
- クラウドのセッションの再起動の後、承認したコネクターのツールが使えないことが Claude に伝わらない問題を修正
- サービスが数分間アップロードを拒むと、クラウドのセッションがターンの途中で止められる問題を修正
- 一部のクラウドのセッションで、`Setup` のフックが `CLAUDE_ENV_FILE` に書いた変数が Bash のツールに届かない問題を修正
- 応答がツールの呼び出しで切れたか、拒まれた画像か文書が外された後、iPhone のアプリがクラウドのセッションのターンを終わったと示したまま動き続ける問題を修正
- 再起動したセッションが、API のエラーで失敗したメッセージを、その後ろで待つ新しいメッセージより先に送り直す問題を修正
- Claude が大きな画像を読むかツールの呼び出しを再試行した直後の再起動で、再起動したセッションが中断したターンを落とす問題を修正
- `NODE_EXTRA_CA_CERTS` のファイルが空か、PEM でないか、壊れた証明書で始まると、すべての接続が失敗する問題を修正。読める証明書を使い、stderr に警告を出します
- 使用量の上限の後に再開したワークフローが、終わったエージェントをまた動かす問題を修正
- クラウドのセッションの `/mcp` がモデルの使えないツールを数える問題を修正。サーバーの行は、そのツールのうち使える数を示します
- Claude が PushNotification の呼び出しで status のフィールドを省くと、通知が重複する問題を修正
- 20 枚を超える画像のある要求で、大きすぎる画像のエラーが常に上限を 2000px と言う問題を修正。API の上限を示します
- ダイアログを開いている間、バックグラウンドのシェルの詳細の実行時間が更新されない問題を修正
- mod の `turn.step` のフックが、止めた返事をヘッドレスの実行で成功として終わらせる問題を修正
- 保持の後始末が、`claude -p` だけを動かすホームに `~/.claude.json` のバックアップを残さない問題を修正。最後の良いバックアップを削除する前に新しいバックアップを取ります
- ネットワークのホームディレクトリがデータの空きを失っても新しいファイルは受け付けるとき、保存したログインが空のファイルに置き換わる問題を修正
- `forceLoginOrgUUID` のあるマシンで、許された組織のものなのに `setup-token` のトークンが起動時に拒まれる問題を修正
- 非対話の起動が、JSON として正しくない `~/.claude.json` を既定で置き換える問題を修正。起動は失敗し、ファイルの戻し方を伝え、ファイルはそのままにします（anthropics/claude-code#87551）
- バックアップのない空の `~/.claude.json` が壊れていると報告される問題を修正。ファイルがないときと同じように起動します
- 壊れたかない `~/.claude.json` について出す復元のコマンドが、空か途中で切れたバックアップを名指すか、読み取り専用のファイルで失敗する問題を修正
- 保存した claude.ai のログインが時間の上限に達したときのサインインの失敗を修正。そう伝え、`claude -p` では `claude auth login` と `claude setup-token` を名指します
- Remote Control: セッションの作業フォルダーがないとき「spawn error: ENOENT」と紛らわしく出る問題を修正。エラーはフォルダーを名指します
- [VSCode] 組織の設定がサインインを拒むウィンドウが、1 分ごとにバックグラウンドで新しい Claude Code のプロセスを始める問題を修正
- [VSCode] チャットのパネルのエラーのバナーの長い語が、閉じるボタンを見えなくする問題を修正
- [Cloud sessions] クラウドのセッションで GitHub Actions のログを読む問題を修正。`gh run view --log` と `gh api` のログの要求は、届かないリダイレクトではなく、多くの環境でログを受け取ります
- [Remote Control] 環境のメニューの Remote Control の行で、1 つのリポジトリの並んだチェックアウトが同じに見える問題を修正。それぞれのフォルダーの名前を示します
- [Claude Tag] Claude Tag の管理の設定のキーボードのフォーカスとスクリーンリーダーの読み上げを修正。接続のフォームで Escape を押しても Add のダイアログは閉じなくなりました

**その他**

- **JetBrains Marketplace についての注記が加わった**（`jetbrains` の「Installation」）。JetBrains Marketplace はサードパーティのソフトウェアで、Anthropic は推奨・保守・監査をせず、Claude Code のプラグインの公開を申請している、というものです — [日本語](https://code.claude.com/docs/ja/jetbrains#installation) / [English](https://code.claude.com/docs/en/jetbrains#installation)
- **字句の小さな修正**: `code-review-local` のレビューがバックグラウンドのサブエージェントで動くという文に「ターミナルのセッションでは」が付き、`agent-sdk/agent-loop` の effort の段落は括弧が言い換えられて「セッション全体」が「セッション」（`sub-agents` の effort の節へのリンク付き）になりました
- **`setup` のコードフェンスの重複が解消された**: インストールの 5 つのコードフェンスの `theme={null}` の 11 重の重複が 1 つに戻りました。書式だけの変更で、コマンドは変わっていません
<!-- light:minor-updates:end -->

見出しマップ（`en/claude_code_docs_map.md`）は 15 行が加わり 3 行が外れました。加わったのは 12 の新しい見出し、改称された 2 行（`errors` と `routines` の「Scheduled tasks are off for your organization」）、新しいスタンプで、外れたのは改称前の 2 行と古いスタンプです。`llms-full.txt` の見出しの増減（加わった 14・外れた 2）と同じで、今回、見出しマップにだけ先に載った見出しはありません。

**参考リンクについて**: 日本語版は、今回取り上げたページのうち 33 ページを取得し、該当する節があるかと今回の内容になっているかを、計 54 項目について確かめました。54 項目とも日本語版がすでに今回の内容になっていたので、リンクはすべて日本語版を併記しています。アンカーは、見出しから作った id か、ページ内・ページ間のリンクが使っている id です。見出しと id が違う 4 つ（`sandboxing` の 2 つのトラブルシューティングの h3 の `#apparmor-restriction-stops-bubblewrap`・`#bwrap-uid-map-permission-denied`、`errors` の新しい h4 の `#hook-changed-input-after-review`、改称した h3 の `#routines-are-disabled-by-your-organizations-policy`）は、ページ内かほかのページのリンクが使っている id です。記号を含む見出し（`plugins/mods/troubleshoot` の h3、`interactive-mode` の「Reverse search with Ctrl+R」）と、リンクに id の裏付けがない新しい見出し（`sub-agents` の h4 など）は、上位の節か同じ内容の別の節にリンクしました。リンクを付けなかった `large-codebases`・`best-practices`・`self-hosted-environments-deploy`・`code-review-local`・`agent-sdk/agent-loop`・`setup` は、字句か言い換えだけの変更で、ほかのページの項目に添えて扱っています。**changelog ページへのリンクは、本サマリの方針どおり付けていません。**

## 新着情報

<!-- light:whats-new:start -->
**今回、新着情報（`whats-new/`）のページに変更はありません**（最新の週のダイジェストは前回と同じ Week 37 です）。
<!-- light:whats-new:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-11-02.md](./archives/latest/2026-11-02.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-11-02.md](./archives/latest-detail/2026-11-02.md)

<!--
base_commit: acb459e04e57acda73f439e58d2759ea5599cdf6
head_commit: 91ce08863140666e5065f2a289650527b5eff4bb
generated_at_full: 2026-11-04T15:11:34+09:00
-->
