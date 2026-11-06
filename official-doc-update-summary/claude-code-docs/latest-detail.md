---
対象期間: 2026年11月04日 〜 2026年11月05日
作成日: 2026-11-05
---

# Claude Code 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
**今回は changelog に新しいリリースはなく（最新は前回と同じ v2.1.318）、通常のページに、`Bash` マッチャーのフックと Monitor コマンドの関係、サブエージェントがフラグ付きの要求で失敗する場合、`REVIEW.md` が効かないサブディレクトリ、IDE の拡張機能を起動時に入れなくなったこと、Agent SDK の `origin` の使い分けが載りました**。新しいページはなく、228 ページ中 35 ページが変わり、変更はページ単位で 319 行（追加 204・削除 115）です。50 行以上変わったページはないので、大幅更新はありません。見出しは 7 つ加わり 1 つ改称され、どれも見出しマップの変更と一致します。総行数は 127,658 行から 127,747 行に増えました。

主要なものを以下に挙げます。

1. `hooks` に h4「Match Monitor commands」ができ、`Bash` マッチャーのフックが Monitor のシェルコマンドでも動くものの、`allow` と `updatedInput` は効かないことが載った
2. `model-config` に h4「Subagents switch or fail without asking」ができ、**Ask each time** ではサブエージェントがモデルを切り替えず失敗することが載った
3. `code-review-customize` に h3「When a subdirectory REVIEW.md doesn't apply」ができ、`tests`・`vendor` のような名前のサブディレクトリの `REVIEW.md` は適用されないことと、150,000 バイトの上限が載った
4. `vs-code`・`settings-reference`・`env-vars` が、v2.1.318 以降は `claude` の起動で IDE の拡張機能を入れない、という説明に揃えられた
5. `agent-sdk/typescript` の `SDKMessageOrigin` に、アプリケーションが設定してよい `origin` は 2 種類で、ユーザーが書いていないテキストは `isSynthetic` と `client_composed` で送る、と載った
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**Bash マッチャーのフックと Monitor コマンドの関係が載った**](#1-bash-マッチャーのフックと-monitor-コマンドの関係が載った):  
  `hooks` の「Matcher patterns」に h4「Match Monitor commands」ができました。`Bash` マッチャーの `PreToolUse` と `PermissionRequest` のフックは Monitor ツールのシェルコマンドでも動きますが（Claude Code v2.1.314 以降）、拒否か確認しかできず、`allow` と `updatedInput` は効きません。許可か書き換えをするには、`Bash|Monitor` のように Monitor を含むマッチャーに替えます。`agent-sdk/hooks` の「Matchers」も追従しています
2. [**サブエージェントがフラグ付きの要求で失敗する場合が載った**](#2-サブエージェントがフラグ付きの要求で失敗する場合が載った):  
  `model-config` の「Automatic model fallback」に h4「Subagents switch or fail without asking」ができました。Claude が Agent ツールで始めたサブエージェントは確認のために止まらず、**Switch automatically** か未選択ならフォールバックのモデルで再実行し、**Ask each time** なら `Agent terminated early due to an API error` で失敗します（changelog の v2.1.318）
3. [**サブディレクトリの REVIEW.md が適用されない場合が載った**](#3-サブディレクトリの-reviewmd-が適用されない場合が載った):  
  `code-review-customize` に h3「When a subdirectory REVIEW.md doesn't apply」ができました。`tests`・`examples`・`generated`・`vendor` のような名前のサブディレクトリの中か下の `REVIEW.md` は、中身にかかわらず適用されません。残りのサブディレクトリの `REVIEW.md` は、ルートのファイルを除いて合計 150,000 バイトの上限を共有します
4. [**IDE の拡張機能を起動時に入れない説明に揃えられた**](#4-ide-の拡張機能を起動時に入れない説明に揃えられた):  
  changelog の v2.1.318 の、IDE のターミナルで起動しても拡張機能をインストール・更新しなくなった変更が、`vs-code`・`settings-reference` の `autoInstallIdeExtension`・`env-vars` の `CLAUDE_CODE_IDE_SKIP_AUTO_INSTALL` に載りました。`vs-code` の「Uninstall the extension」は、拡張機能が戻る 2 つの場合と、戻さない 3 つの方法を挙げる形になっています
5. [**Agent SDK の origin の使い分けが書き直された**](#5-agent-sdk-の-origin-の使い分けが書き直された):  
  `agent-sdk/typescript` の `SDKMessageOrigin` に、アプリケーションが設定してよいのは `human` と `task-notification`（`scheduled-trigger`）の 2 種類で、ほかの kind を設定すると Claude は既定でユーザーのメッセージとして読む、と載りました。ユーザーが書いていないテキストは `isSynthetic` と `client_composed` で送ります。`SDKResultMessage` の `origin` は、送った値のコピーではなく Claude Code が割り当てた値だと改められています
<!-- light:highlight-list:end -->

## 1. Bash マッチャーのフックと Monitor コマンドの関係が載った

**`hooks` の「Matcher patterns」に h4「Match Monitor commands」ができました。** changelog の v2.1.314 の、`Bash` に一致するフックが Monitor ツールの始めたシェルコマンドで動かなかった問題の修正と、`Monitor(tail *)` のようなフックの `if` の変更に対応します。

`Bash` マッチャーの `PreToolUse` か `PermissionRequest` のフックは、Claude が Monitor ツールで始めたシェルコマンドでも動きますが（Claude Code v2.1.314 以降が要ります）、その `allow` と `updatedInput` は効きません。フックができるのは、コマンドを拒否するか、Claude Code に確認させることです。`Bash|PowerShell`・`^Bash$`・`Bash.*` のようなマッチャーも `Bash` マッチャーです。WebSocket の監視では `Bash` マッチャーのフックは動かず、`Bash` マッチャーの `PostToolUse` のフックは Monitor では動きません。

コマンドを許可するか書き換えるには、Monitor を含むマッチャーに替えます。

- **Monitor を含むマッチャー**: `Bash|Monitor`・`.*` のようなマッチャーか、マッチャーなしなら、フックは Monitor の呼び出しそのものの入力を受け取り、`allow` と `updatedInput` が効く。`if` では `Monitor(tail *)` のように Monitor を名指し、`Bash(tail *)` と同じ規則で一致する。`if` が Bash を名指すと、フックは Monitor の呼び出しの入力を受け取るものの、`allow` と `updatedInput` は効かない
- **`Bash` マッチャー**: フックは Bash の呼び出しを受け取る。`if` では `Bash(tail *)` のように Bash を名指す。`if` が Monitor を名指すとフックは動かない

**ほかの箇所も追従しました。**

- **`hooks` の同じページ**: 「Matcher patterns」の表の `Bash` の例と、「How a hook resolves」の例の説明が Monitor のコマンドに触れるようになりました。「PreToolUse decision control」と「PermissionRequest decision control」には、Monitor のコマンドを許可するか書き換えるなら新しい節を見る、という案内が加わっています
- **`agent-sdk/hooks` の「Matchers」**: `'Bash'` マッチャーのコールバックは Bash のコマンドで走り、Claude Code v2.1.314 以降は `PreToolUse` と `PermissionRequest` で Monitor のコマンドでも走って、拒否はできるが承認はできない、となりました
- **`agent-sdk/python` の「Hook Usage Example」**: セキュリティのフックは `Bash` マッチャーで Bash のツールの呼び出しに走り、ロギングのフックはマッチャーがないのですべてのツールの呼び出しに走る、という説明に替わりました

- [フックリファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/hooks#match-monitor-commands)
- [Hooks reference - Claude Code Docs (English)](https://code.claude.com/docs/en/hooks#match-monitor-commands)
- [フックでエージェントの動作を傍受して制御する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/agent-sdk/hooks#matchers)
- [Intercept and control agent behavior with hooks - Claude Code Docs (English)](https://code.claude.com/docs/en/agent-sdk/hooks#matchers)

## 2. サブエージェントがフラグ付きの要求で失敗する場合が載った

**`model-config` の「Automatic model fallback」に h4「Subagents switch or fail without asking」ができました。** changelog の v2.1.318 の、**Switch models when a message is flagged** が **Ask each time** のときサブエージェントはモデルを切り替えず止まる、という変更に対応します。

Claude が Agent ツールで始めた組み込みかカスタムのサブエージェントでは、フラグ付きの要求で Claude Code が確認のために止まることはありません。フォールバックのモデルがあるときの動きは、`/config` の選択で分かれます。

- **Switch automatically、または未選択**: 要求はフォールバックのモデルで再実行され、セッションのモデルは変わらない
- **Ask each time**: サブエージェントは `Agent terminated early due to an API error` と拒否のメッセージで失敗する。Claude はそのエラーを受け取り、終わっていないタスクをどうするかを決める。サブエージェントに切り替えさせるには **Switch automatically** を選ぶが、そうするとメインの会話も確認なしで切り替わる

フォールバックのモデルがないときは、どちらの選択でも同じように失敗します。v2.1.318 より前は、サブエージェントのフラグ付きの要求は、どちらを選んでいても使えるフォールバックのモデルで再実行されていました。「Ask before switching」の例外の項目も、サブエージェントはフォールバックのモデルで再実行する、から、Agent ツールで始めたサブエージェントは確認のために止まらず、モデルを切り替えず失敗する、に改められています。

- [モデル設定 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/model-config#subagents-switch-or-fail-without-asking)
- [Model configuration - Claude Code Docs (English)](https://code.claude.com/docs/en/model-config#subagents-switch-or-fail-without-asking)

## 3. サブディレクトリの REVIEW.md が適用されない場合が載った

**`code-review-customize` の「Use REVIEW.md for review-only rules」に h3「When a subdirectory REVIEW.md doesn't apply」ができました。** 次の名前のサブディレクトリの中か下にある `REVIEW.md` は、そのサブディレクトリの中身にかかわらず適用されません。名前は全体でだけ一致し、大文字小文字と深さは問わないので、`Tests` は一致し、`integration-tests` は一致しません。

- **Tests**: `test`・`tests`・`__tests__`・`testdata`・`fixtures`・`__fixtures__`・`golden`・`corpus`・`snapshots`・`__snapshots__`
- **Examples**: `example`・`examples`・`sample`・`samples`・`demo`・`demos`
- **Generated code**: `generated`
- **Third-party code**: `vendor`・`third_party`・`third-party`・`thirdparty`・`node_modules`・`bower_components`・`external`・`extern`・`deps`・`godeps`・`pods`・`carthage`・`site-packages`・`contrib`

これらのサブディレクトリのチェックは、ルートの `REVIEW.md` か、親のサブディレクトリの `REVIEW.md`（その親もその上も一覧にないとき）に書きます。プルリクエストが変更するパスにある残りのサブディレクトリの `REVIEW.md` は、ルートのファイルを除いて合計 150,000 バイトの上限を共有します。check run が一部のファイルが収まらなかったと報告したら、上限に収まるよう短くします。

同じページの導入は、保護されたブランチで、ほとんどのサブディレクトリに `REVIEW.md` を足せる、という言い方になりました。「What a review reads for each branch setup」の表の 2 行も、読むものが「subdirectory files」から「most subdirectory files」に替わっています。

- [Code Review をカスタマイズする - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/code-review-customize#when-a-subdirectory-review-md-doesnt-apply)
- [Customize Code Review - Claude Code Docs (English)](https://code.claude.com/docs/en/code-review-customize#when-a-subdirectory-review-md-doesnt-apply)
- [Code Review をカスタマイズする - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/code-review-customize#what-a-review-reads-for-each-branch-setup)
- [Customize Code Review - Claude Code Docs (English)](https://code.claude.com/docs/en/code-review-customize#what-a-review-reads-for-each-branch-setup)

## 4. IDE の拡張機能を起動時に入れない説明に揃えられた

**changelog の v2.1.318 の、IDE のターミナルで起動しても IDE の拡張機能をインストール・更新しなくなった変更が、通常のページに載りました。** changelog は、代わりに外のターミナルからの `/ide` かエディターの拡張機能のビューを使う、と述べています。

- **`vs-code` の「Run CLI in VS Code」**: 統合ターミナルの項目に、Claude Code v2.1.318 以降は拡張機能を入れないので、インストールするまで `/ide` は "No available IDEs detected" と報告し、`/status` は IDE を "Not connected" と示す、と載りました（前の段落にあった同じ内容の文はここへ移っています）
- **`vs-code` の「Uninstall the extension」**: 拡張機能が戻るのは、VS Code の動作中に外のターミナルから `/ide` を実行したときと、v2.1.318 より前の Claude Code で統合ターミナルで `claude` を始めたときです。戻さないためには、`~/.claude.json` の `autoInstallIdeExtension` を `false` にする、設定ファイルの `env` で `CLAUDE_CODE_IDE_SKIP_AUTO_INSTALL` を `1` にする、統合ターミナルの `/config` で **Auto-install IDE extension** をオフにする、のいずれかを行い、すでに戻っていたらアンインストールし直します
- **`settings-reference` の `autoInstallIdeExtension`**: Claude Code は `claude` の起動で拡張機能をインストールも更新もしない、と改められました。v2.1.318 より前は、このキーが `false` でない限り、それらのエディターのターミナルで `claude` を始めるとインストールか更新をしました
- **`env-vars` の `CLAUDE_CODE_IDE_SKIP_AUTO_INSTALL`**: v2.1.318 より前の Claude Code は、VS Code・Cursor・Devin Desktop のターミナルで `claude` を始めても拡張機能をインストールか更新をするので、この変数はそれも止める、と加わりました

- [VS Code で Claude Code を使う - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/vs-code#run-cli-in-vs-code)
- [Use Claude Code in VS Code - Claude Code Docs (English)](https://code.claude.com/docs/en/vs-code#run-cli-in-vs-code)
- [VS Code で Claude Code を使う - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/vs-code#uninstall-the-extension)
- [Use Claude Code in VS Code - Claude Code Docs (English)](https://code.claude.com/docs/en/vs-code#uninstall-the-extension)
- [すべての設定 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/settings-reference#autoinstallideextension)
- [All settings - Claude Code Docs (English)](https://code.claude.com/docs/en/settings-reference#autoinstallideextension)
- [環境変数 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/env-vars#variables)
- [Environment variables - Claude Code Docs (English)](https://code.claude.com/docs/en/env-vars#variables)

## 5. Agent SDK の origin の使い分けが書き直された

**`agent-sdk/typescript` の `SDKMessageOrigin` に、アプリケーションが設定してよい `origin` の説明ができました。**

- **設定してよいもの**: `{ kind: "human" }`（ユーザーが入力したもの）と、`{ kind: "task-notification", subkind: "scheduled-trigger" }`（宣言したスケジュールの実行）です。ほかの kind は Claude Code と Anthropic のサーバーに任せます。設定すると、Claude は既定でそのメッセージをユーザーのものとして読みます
- **ユーザーが書いていないテキスト**: 取得したページやほかのエージェントの出力は、`isSynthetic` を `true`、`origin` を未設定にした別のメッセージで送ります。`/` で始まるテキストがコマンドとして動かないよう、`client_composed` も `true` にします

**kind の表も改められました。**

- **`human`**: アプリケーションがユーザーの入力を転送するなら `{ kind: "human" }` を設定する、という点は同じです。`origin` がなくても Claude はユーザーのものとして読みますが、`ultracode` のワークフローのキーワードのように人の入力を要するチェックは受け付けません。v2.1.210 より前の動きを述べた文は外れました
- **`peer`**: 「ほかの Claude Code のエージェントからのメッセージ」に改められました。セッションの間でメッセージを中継するデスクトップアプリがこの kind を `fromMode` で宣言し、自分のアプリケーションでほかのエージェントの出力を中継するなら `isSynthetic` と `client_composed` を使います。「Peer origin fields」の `fromMode` の説明からは、宣言するホストの部分が外れています
- **`unclassified`**: 「由来を判断できなかった注入のターン」から、「`isSynthetic: true` で送る `SDKUserMessage` のように、ユーザーからではないと示されたメッセージ」に短くなりました

**`SDKResultMessage` の `origin` の説明も替わりました。** ターンを引き起こしたユーザーのメッセージに Claude Code が割り当てた値で、送った `origin` のコピーではありません。Claude Code が割り当てなかったとき（`origin` も `isSynthetic` もないメッセージで始めたターン、起動のエラーのようにユーザーのターンの前に出た結果）は欠けます。

- [Agent SDK リファレンス - TypeScript - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/agent-sdk/typescript#sdkmessageorigin)
- [Agent SDK reference - TypeScript - Claude Code Docs (English)](https://code.claude.com/docs/en/agent-sdk/typescript#sdkmessageorigin)
- [Agent SDK リファレンス - TypeScript - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/agent-sdk/typescript#sdkresultmessage)
- [Agent SDK reference - TypeScript - Claude Code Docs (English)](https://code.claude.com/docs/en/agent-sdk/typescript#sdkresultmessage)

## 新規追加されたページ

<!-- light:new-pages:start -->
（今回の対象期間に新規追加・削除されたドキュメントページはありません。`llms.txt` のページの一覧は変わっておらず、`llms-full.txt` に展開されている固有のページも 228 のままで、`Source:` の行が 231 あり 3 ページが 2 回展開されている状態も前回と同じです）
<!-- light:new-pages:end -->

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
（今回の対象期間に 50 行以上変わったページはありません。最も多いのは `hooks` の 37 行です）
<!-- light:updated-pages:end -->

**行数の数え方**: `llms-full.txt` の生の差分（追加 204 行・削除 115 行）のハンクを、head 側の `Source:` 行でページに振り分けた値です（ページの並びは変わっておらず、ページ本文どうしの比較で変わった 35 ページと一致し、ページ単位の合計は生の差分と一致します）。base と head は同じ書式なので、正規化はしていません。多い順に、`hooks` の 37 行（追加 28・削除 9）、`agent-sdk/typescript` の 28 行（追加 20・削除 8）、`errors` の 19 行（追加 14・削除 5）、`desktop-ios-simulator` の 19 行（追加 13・削除 6）、`code-review-customize` の 19 行（追加 16・削除 3）です。

## 軽微な更新

<!-- light:minor-updates:start -->
今回の差分は **3 ファイル**（`llms-full.txt`・`llms.txt`・見出しマップ）です。`llms-full.txt` の生の差分は追加 204 行・削除 115 行で、ページの並びは変わっていません。228 ページ中 **35 ページ**が変わり、**changelog のページは変わっていません**。大幅更新はないので、35 ページすべてを以下にまとめます。

`llms-full.txt` の総行数は **127,658 行から 127,747 行へ 89 行増え**ました（生の差分の差し引き 204 − 115 と一致）。`Source:` の行は 231、固有のページは 228 のままで、2 回展開されている 3 ページ（`plugins/create`・`plugins/install`・`plugins/mods/overview`）も前回と同じです。コードフェンスの外の見出しは、引用の中の見出しも数えると 6,056 から 6,063 へ、行頭が `#` の見出しだけを数えると 6,045 から 6,052 へ、どちらも 7 増えました（外れた見出しはなく、`permissions` の 1 つが改称されました）。changelog の最新は v2.1.318 のままです。`llms.txt` の変更は 1 行で、`desktop-ios-simulator` の説明文から、セッションごとに別のシミュレーターを使う、という部分が外れました。

**新機能**

- **PreCompact のフックの stdout が compaction のサマリの指示になると載った**（`hooks` の h4「PreCompact output」）。フックがコード 0 で終わりブロックしないとき、Claude Code はその stdout を compaction のサマリの指示に使います。stdout はフックごとに 10,000 文字未満に保ちます。長い出力はその上限で切られ、マーカーが付きます。「Exit code 0」の、stdout が届くイベントの説明に `PreCompact` が加わり、「JSON output」の、上限を超えた出力をファイルに保存する説明では PreCompact の stdout が例外になりました。changelog の v2.1.314 の、出力の大きい PreCompact のフックで compaction が失敗した問題の修正に対応します — [日本語](https://code.claude.com/docs/ja/hooks#precompact-output) / [English](https://code.claude.com/docs/en/hooks#precompact-output)
- **通知の種類 `auth_storage_failure` が載った**（`hooks` の「Notification」・`hooks-guide` の「Get notified when Claude needs input」）。サインインは終わったものの、Claude Code が新しい資格情報を保存できないときに、`auth_success` の代わりに発火します（Claude Code v2.1.288 以降が要ります）。`hooks` の「Matcher patterns」の表と `hooks-guide` の「Filter hooks with matchers」の表にも加わり、`hooks-guide` の導入は「次の値のいずれか」から「次のような通知の種類」に改められました — [日本語](https://code.claude.com/docs/ja/hooks#notification) / [English](https://code.claude.com/docs/en/hooks#notification)、[日本語](https://code.claude.com/docs/ja/hooks-guide#get-notified-when-claude-needs-input) / [English](https://code.claude.com/docs/en/hooks-guide#get-notified-when-claude-needs-input)
- **Agent SDK で動いているセッションのプラグインを読み込み直す方法が載った**（`agent-sdk/plugins` の h3「Reload plugins in a running session」）。プラグインのスキル・コマンド・エージェント・フックの変更を新しいセッションなしで反映するには、TypeScript の SDK の `Query` オブジェクトの `reloadPlugins()` を呼びます。Python の SDK には同じメソッドがないので、代わりにセッションのプロンプトとして `/reload-plugins` を送ります — [日本語](https://code.claude.com/docs/ja/agent-sdk/plugins#reload-plugins-in-a-running-session) / [English](https://code.claude.com/docs/en/agent-sdk/plugins#reload-plugins-in-a-running-session)
- **Projects の設定 Auto-continue when usage limits reset が載った**（`claude-projects`）。「Project settings reference」の表の **General** の行で、使用量の上限で止まったスレッドかプロジェクトの会話が、上限のリセットで自動で続くかを決めます（既定でオン）。「A thread hit the usage limit」は、続かせないならメッセージが示すリセットの時刻より前にこの設定をオフにする、プロジェクト全体の設定である、オフのまま続けるにはリセットの後にメッセージを送る、という説明になりました。**Service is busy** と **Stop** についての文、スケジュールされたタスクが始めたスレッドは待たない、という文は外れています — [日本語](https://code.claude.com/docs/ja/claude-projects#project-settings-reference) / [English](https://code.claude.com/docs/en/claude-projects#project-settings-reference)、[日本語](https://code.claude.com/docs/ja/claude-projects#usage-limit-reached) / [English](https://code.claude.com/docs/en/claude-projects#usage-limit-reached)
- **Claude apps gateway の Admin UI が「Spend limits only」になった**（`claude-apps-gateway` の「Availability and limitations」）。ゲートウェイに接続した Claude Desktop 4.23118.0 以降で、`admin.admin_groups` のメンバーが支出の上限を管理できます。ほかの設定はこれまでどおり YAML のファイルで、変えるには再デプロイします — [日本語](https://code.claude.com/docs/ja/claude-apps-gateway#availability-and-limitations) / [English](https://code.claude.com/docs/en/claude-apps-gateway#availability-and-limitations)

**機能改善**

- `hooks`・`agent-sdk/hooks`・`agent-sdk/python` の Monitor のコマンドの説明（詳細はハイライト 1 参照）
- `model-config` のサブエージェントとフォールバックの説明（詳細はハイライト 2 参照）
- `code-review-customize` のサブディレクトリの `REVIEW.md` の説明（詳細はハイライト 3 参照）
- `vs-code`・`settings-reference`・`env-vars` の IDE の拡張機能の説明（詳細はハイライト 4 参照）
- `agent-sdk/typescript` の `origin` の説明（詳細はハイライト 5 参照）
- **セルフホストのラッパーで権限モードを固定する説明が書き直された**（`self-hosted-environments-configuration`）。「Permissions and tool approval」に h3「Pin a permission mode from your wrapper」と「Pre-approve specific tools」ができました。ラッパーの `"$@"` の後に足した `--permission-mode` が効くのは、claude.ai/code かほかのクライアントがセッションの権限モードを設定するまでで、設定された後はセッションがランナーで再起動しても効きません。claude.ai/code は、モードのドロップダウンが Auto を示しているとき、または誰かがそこでモードを選んだとき、セッションの最初のメッセージでモードを設定します。deny ルールが止める呼び出しはどのモードでも止まったままです。「Wrapper scripts」の `CLAUDE_CODE_REMOTE_MCP_CONFIG` の行は、ラッパーが子の環境を作り直すならこの変数と `CLAUDE_CODE_REMOTE`・`CLAUDE_CODE_ENVIRONMENT_KIND` をそのまま引き継ぐ、`CLAUDE_CODE_REMOTE` が届いてこの変数か `CLAUDE_CODE_ENVIRONMENT_KIND` が届かないと、配信されたサーバーの更新に含まれない `--mcp-config` のサーバーを子が止める、と改められました — [日本語](https://code.claude.com/docs/ja/self-hosted-environments-configuration#pin-a-permission-mode-from-your-wrapper) / [English](https://code.claude.com/docs/en/self-hosted-environments-configuration#pin-a-permission-mode-from-your-wrapper)、[日本語](https://code.claude.com/docs/ja/self-hosted-environments-configuration#wrapper-scripts) / [English](https://code.claude.com/docs/en/self-hosted-environments-configuration#wrapper-scripts)
- **iOS Simulator のペインのセッションとデバイスの説明が替わった**（`desktop-ios-simulator`）。「How sessions manage devices」は、プロンプトがシミュレーターを名指さなければ、別の並行セッションが開いたものでも Claude はすでに動いているものを使う、という説明になりました。セッションごとに別のシミュレーターにするには、各セッションのプロンプトで別のものを名指します。デバイスは起動したセッションのもの、1 セッションに 4 つまで、という文は外れています。「Actions that follow your permission mode」にはアプリのインストールと起動が加わって 3 つになり、Claude の要求を断るとデバイスはアタッチされず Desktop は起動もしない、と改められました。自分で使うには **Attach simulator**、**Continue**、続くダイアログの **Cancel** の順に押し、後で Claude にアクセスを与えるには **Let Claude use it** を押します — [日本語](https://code.claude.com/docs/ja/desktop-ios-simulator#how-sessions-manage-devices) / [English](https://code.claude.com/docs/en/desktop-ios-simulator#how-sessions-manage-devices)、[日本語](https://code.claude.com/docs/ja/desktop-ios-simulator#allow-a-device-the-first-time) / [English](https://code.claude.com/docs/en/desktop-ios-simulator#allow-a-device-the-first-time)、[日本語](https://code.claude.com/docs/ja/desktop-ios-simulator#actions-that-follow-your-permission-mode) / [English](https://code.claude.com/docs/en/desktop-ios-simulator#actions-that-follow-your-permission-mode)
- **Desktop のスケジュールタスクの権限の説明が改められた**（`desktop-scheduled-tasks`）。「Permissions for scheduled tasks」では、「always allow」を選ぶと以後の実行が飛ばすのは「ほとんどの」確認になり、タスクのフォルダーのファイル編集で「always allow」を選んでも **Accept edits** に移るのはそのセッションだけなので、タスクの権限モードを **Accept edits** にする、と加わりました。「Manage scheduled tasks」の `update_scheduled_task` の説明は、タスクに自分のスケジュールかプロンプトを変えさせるには **Run now** を押して毎回呼び出しを承認する、に替わりました — [日本語](https://code.claude.com/docs/ja/desktop-scheduled-tasks#permissions-for-scheduled-tasks) / [English](https://code.claude.com/docs/en/desktop-scheduled-tasks#permissions-for-scheduled-tasks)、[日本語](https://code.claude.com/docs/ja/desktop-scheduled-tasks#manage-scheduled-tasks) / [English](https://code.claude.com/docs/en/desktop-scheduled-tasks#manage-scheduled-tasks)
- **claude.ai のログインを送らなかったときのメッセージが替わった**（`errors` の「Claude Code didn't send your claude.ai login」）。メッセージは `Your organization's settings need an update`・`Couldn't load your organization's settings`・`Restart Claude Code to finish signing in` の 3 つになり、対処も、管理者に API キーヘルパーの設定を直すよう頼む、接続を確かめて再起動する（戻るなら管理者に伝える）、再起動する、に分かれました。v2.1.315 より前は、拒否されたプロンプトかファイルのアップロードが `Claude Code didn't send your claude.ai login` で始まる 1 つのメッセージを出しました。「Find your error」の表の行も 3 行に替わっています — [日本語](https://code.claude.com/docs/ja/errors#claude-code-didnt-send-your-claude-ai-login) / [English](https://code.claude.com/docs/en/errors#claude-code-didnt-send-your-claude-ai-login)
- **一致しないパスのルールの説明に `Grep` が加わった**（`permissions`）。「Read and Edit」の h4 は「`Write(path)`, `NotebookEdit(path)`, and `Glob(path)` rules never match」から「`Write(path)`, `Glob(path)`, and `Grep(path)` rules don't match」に改称されました。`Grep(docs/**)` の deny ルールは Grep の `docs` の検索を止めません。`Write`・`NotebookEdit`・legacy の `MultiEdit` は `Edit(docs/**)` で、`Glob`・`Grep` は `Read(docs/**)` で書きます。ask ルールの `Read(docs/**)` は、一致するパスで Claude が Grep か Glob を呼ぶと確認を求めますが、その上の作業ディレクトリの検索が一致するファイルを返しても確認は求めません。「What `Read` and `Edit` rules cover」も、ベストエフォートで当てるのは `Read(path)` の deny ルールだ、と明示しました — [日本語](https://code.claude.com/docs/ja/permissions#path-rules-that-never-match) / [English](https://code.claude.com/docs/en/permissions#path-rules-that-never-match)、[日本語](https://code.claude.com/docs/ja/permissions#what-read-and-edit-rules-cover) / [English](https://code.claude.com/docs/en/permissions#what-read-and-edit-rules-cover)
- **SSH と tmux のデスクトップ通知の説明が改められた**（`terminal-config`・`settings-reference` の `preferredNotifChannel`）。Ghostty・Kitty・iTerm2 の通知は「Claude Code がそれらを検出したとき」と明示されました。tmux の外のターミナルから SSH でつなぐときは、Claude Code が動くマシンで `preferredNotifChannel` をローカルのターミナルの値（`"iterm2"`・`"kitty"`・`"ghostty"`）にすると、通知がローカルのマシンに届きます。「Configure tmux」は、見えているペインから外のターミナルへ通知を送るには `allow-passthrough` の行を残して同じ設定をする、この例では見ていないウィンドウのペインは送らない、という説明に替わり、進捗バーへの言及は外れました — [日本語](https://code.claude.com/docs/ja/terminal-config#get-a-terminal-bell-or-notification) / [English](https://code.claude.com/docs/en/terminal-config#get-a-terminal-bell-or-notification)、[日本語](https://code.claude.com/docs/ja/terminal-config#configure-tmux) / [English](https://code.claude.com/docs/en/terminal-config#configure-tmux)、[日本語](https://code.claude.com/docs/ja/settings-reference#preferrednotifchannel) / [English](https://code.claude.com/docs/en/settings-reference#preferrednotifchannel)
- **fast mode の説明が対応モデルに絞られた**（`fast-mode`・`settings-reference`・`prompt-caching`）。`"fastMode": true` は対応モデルで設定するもので、ほかのモデルで設定してもそのモデルのまま fast mode はオフです。セッションをまたいで続くのも対応モデルのときで、Opus への切り替えは `/fast` を実行したときの動きと明示されました。`settings-reference` の `fastMode` では、対応モデルの説明が別の段落に分かれ、`fastModePerSessionOptIn` も同じ言い方に揃えられました。使用量のクレジットが切れたときの通知は `Fast mode disabled · Out of usage credits` に替わり、「セッションの残りの間」という言い方が外れています — [日本語](https://code.claude.com/docs/ja/fast-mode#toggle-fast-mode) / [English](https://code.claude.com/docs/en/fast-mode#toggle-fast-mode)、[日本語](https://code.claude.com/docs/ja/fast-mode#require-per-session-opt-in) / [English](https://code.claude.com/docs/en/fast-mode#require-per-session-opt-in)、[English](https://code.claude.com/docs/en/settings-reference#fastmode)、[日本語](https://code.claude.com/docs/ja/prompt-caching#turning-on-fast-mode) / [English](https://code.claude.com/docs/en/prompt-caching#turning-on-fast-mode)
- **Claude in Slack が読むコンテキストの説明が改められた**（`slack`）。「Context gathering」は、スレッドでは最初にメンションしたときに、そのスレッドの自分のメッセージと Claude 自身のメッセージを、チャンネルでは自分の最近のメッセージと Claude 自身のメッセージに加えて、チャンネルの名前・トピック・説明を読む、という説明になりました。チームメイトが書いたもの（エラーの報告など）を渡すには、そのテキストを Claude にメンションするメッセージに貼り付けます。「Use cases」の **Collaborative debugging** と「Writing effective requests」の **Use threads** の項目は外れ、「When to use Slack vs. web」からもコンテキストがすでに Slack の議論にあるとき、という部分が外れました — [日本語](https://code.claude.com/docs/ja/slack#context-gathering) / [English](https://code.claude.com/docs/en/slack#context-gathering)
- **セットアップスクリプトが失敗したときの説明が改められた**（`web-quickstart` の「Setup script failed」・`cloud-environments` の「Script requirements」・`claude-projects` の「Other messages」）。ゼロ以外で終わると、セッションの開始に失敗するか、スクリプトがインストールできなかったものなしでセッションが始まり、始まったなら作業を続けられます。原因を直した後は新しいセッションを始めてスクリプトを実行し直します。失敗したのがクラウドのスケジュールタスクの実行なら、タスクの詳細ページの **Run now** を押します。Projects では、環境のスクリプトを直してから、プロジェクトの会話で Claude に新しいスレッドで実行するよう頼みます — [日本語](https://code.claude.com/docs/ja/web-quickstart#setup-script-failed) / [English](https://code.claude.com/docs/en/web-quickstart#setup-script-failed)、[日本語](https://code.claude.com/docs/ja/cloud-environments#script-requirements) / [English](https://code.claude.com/docs/en/cloud-environments#script-requirements)、[日本語](https://code.claude.com/docs/ja/claude-projects#other-messages) / [English](https://code.claude.com/docs/en/claude-projects#other-messages)
- **クラウド環境のシークレットのフォームの説明が改められた**（`cloud-environments`）。「Add a secret」と「Add a secret without an organization admin role」から **Name** の項目が外れました。**Custom headers** の行には **Header name** に `Authorization`、**Prefix** に `Bearer` がすでに入っています。管理者のロールなしで足すときは、キーを **Token** のフィールドに貼り、`X-Api-Key` のような `Authorization` 以外のヘッダーなら **Header** をその名前に変えます — [日本語](https://code.claude.com/docs/ja/cloud-environments#add-a-secret) / [English](https://code.claude.com/docs/en/cloud-environments#add-a-secret)、[日本語](https://code.claude.com/docs/ja/cloud-environments#add-a-secret-without-an-organization-admin-role) / [English](https://code.claude.com/docs/en/cloud-environments#add-a-secret-without-an-organization-admin-role)
- **auto モードが表示される条件の説明が改められた**（`web-quickstart` の「Start a task」・`permission-modes` の「Switch permission modes」）。**Auto** は組織がオフにしない限り表示され、claude.ai/code では選択したモデルが対応しないとグレーアウトします。これまでは、組織が許可し選択したモデルが対応するときに表示される、という説明でした — [日本語](https://code.claude.com/docs/ja/web-quickstart#start-a-task) / [English](https://code.claude.com/docs/en/web-quickstart#start-a-task)、[日本語](https://code.claude.com/docs/ja/permission-modes#switch-permission-modes) / [English](https://code.claude.com/docs/en/permission-modes#switch-permission-modes)
- **Claude apps gateway の負荷テストの説明が増えた**（`claude-apps-gateway-config` の `load_test_mode`・`claude-apps-gateway-deploy` の「Concurrent upstream requests」）。このモードの負荷テストは、各レプリカの同時のアップストリームの要求の上限での待ちも対象外です。要求はこの上限で待ちませんが、開いている要求が上限を超えるとレプリカは `client requests are open` の警告をログに残します。これは本番の要求が待ち始める点です。`claude-apps-gateway-on-aws` と `claude-apps-gateway-on-gcp` の「Next steps」にも Load-test mode の項目が加わりました — [English](https://code.claude.com/docs/en/claude-apps-gateway-config#load_test_mode)、[日本語](https://code.claude.com/docs/ja/claude-apps-gateway-deploy#concurrent-upstream-requests) / [English](https://code.claude.com/docs/en/claude-apps-gateway-deploy#concurrent-upstream-requests)、[日本語](https://code.claude.com/docs/ja/claude-apps-gateway-on-aws#next-steps) / [English](https://code.claude.com/docs/en/claude-apps-gateway-on-aws#next-steps)、[日本語](https://code.claude.com/docs/ja/claude-apps-gateway-on-gcp#next-steps) / [English](https://code.claude.com/docs/en/claude-apps-gateway-on-gcp#next-steps)
- **Claude Desktop とゲートウェイの説明が短くなった**（`claude-apps-gateway`）。「Deliver policy to Claude Desktop sessions」は Cowork・Code・Chat の名前を挙げず「タブ」と述べるようになりました。「Connect Claude Desktop」の、既定で Cowork と Code のタブを示し、Chat を出すには `chatTabEnabled` を `true` にする、という段落は外れています（接続すると有効なすべてのタブのモデルの要求がゲートウェイを通る、という文は前の段落へ移りました）。「Availability and limitations」の Claude Desktop の行も短くなりました — [日本語](https://code.claude.com/docs/ja/claude-apps-gateway#connect-claude-desktop) / [English](https://code.claude.com/docs/en/claude-apps-gateway#connect-claude-desktop)
- **`SandboxIgnoreViolations` の説明が書き直された**（`agent-sdk/python`・`agent-sdk/typescript` の `SandboxSettings`）。Python の型は `file` と `network` を持つ `TypedDict` から `dict[str, list[str]]` に替わり、プロパティの表は外れました。sandbox の違反レポートから除く違反を表し、各キーはコマンドの一部か `*` に一致し、各値は違反の行の中で一致させるテキストです。`{"*": ["/etc/hosts"]}` は `/etc/hosts` に触れる違反を隠しますが、一致するアクセスはそれでも止まります — [日本語](https://code.claude.com/docs/ja/agent-sdk/python#sandboxignoreviolations) / [English](https://code.claude.com/docs/en/agent-sdk/python#sandboxignoreviolations)、[日本語](https://code.claude.com/docs/ja/agent-sdk/typescript#sandboxsettings) / [English](https://code.claude.com/docs/en/agent-sdk/typescript#sandboxsettings)
- **`CLAUDE_CODE_EXTRA_BODY` の当たる範囲が改められた**（`env-vars`）。「すべての API の要求の本文」から、「`/model` の確認のような会話の外の一部の要求を除く、モデルの要求の本文」に替わりました — [日本語](https://code.claude.com/docs/ja/env-vars#variables) / [English](https://code.claude.com/docs/en/env-vars#variables)
- **分割ペインのチームメイトの権限モードに版の条件が加わった**（`agent-teams` の「Permissions」）。リードが Manual か `dontAsk` モードのとき、新しいチームメイトが Manual モードで始まる動きは、分割ペインのチームメイトでは Claude Code v2.1.317 以降が要ります — [日本語](https://code.claude.com/docs/ja/agent-teams#permissions) / [English](https://code.claude.com/docs/en/agent-teams#permissions)
- **アーティファクトの読み取りの確認に auto モードの場合が加わった**（`artifacts` の「Read an artifact shared with you」）。Claude Code が所有者かネットワークの設定を確かめられないとき、auto モードでは確認の代わりに分類器が読み取りを承認かブロックできます — [日本語](https://code.claude.com/docs/ja/artifacts#read-an-artifact-shared-with-you) / [English](https://code.claude.com/docs/en/artifacts#read-an-artifact-shared-with-you)
- **ランブックのディープリンクの前提が改められた**（`deep-links` の「Embed a link in a runbook」）。手順 2 を押す前に、マシンに `claude-cli://` のハンドラーが登録され、ローカルのクローンかワークツリーで `claude` を実行してある必要があります — [日本語](https://code.claude.com/docs/ja/deep-links#embed-a-link-in-a-runbook) / [English](https://code.claude.com/docs/en/deep-links#embed-a-link-in-a-runbook)
- **Agent SDK のツールの権限の導入が改められた**（`agent-sdk/agent-loop` の「Tool permissions」）。「3 つのオプションが連携して動くものを決める」という説明が、ツールの自動承認、ブロック、権限モードの設定にこれらのオプションを使う、に替わりました — [日本語](https://code.claude.com/docs/ja/agent-sdk/agent-loop#tool-permissions) / [English](https://code.claude.com/docs/en/agent-sdk/agent-loop#tool-permissions)
- **Agent SDK のストリーム中の出力トークン数の案内が外れた**（`agent-sdk/cost-tracking` の「Read output tokens from the result message」）。`includePartialMessages` を設定して `message_delta` のイベントの `usage` を読む、という段落が外れました — [日本語](https://code.claude.com/docs/ja/agent-sdk/cost-tracking#read-output-tokens-from-the-result-message) / [English](https://code.claude.com/docs/en/agent-sdk/cost-tracking#read-output-tokens-from-the-result-message)

**その他**

- **Projects の作成の項目名が替わった**（`claude-projects` の「Start a new project from scratch」）。**Goal** が **What do you want to work on?** になりました。「Usage and cost」の、上限で止まったスレッドの説明も短くなっています — [日本語](https://code.claude.com/docs/ja/claude-projects#start-a-new-project-from-scratch) / [English](https://code.claude.com/docs/en/claude-projects#start-a-new-project-from-scratch)
- **`channels` の表の字句が替わった**（「How channels compare」）。Claude in Slack の行の最後が「チームの会話のコンテキストから」から「チームの会話から」になりました — [日本語](https://code.claude.com/docs/ja/channels#how-channels-compare) / [English](https://code.claude.com/docs/en/channels#how-channels-compare)
<!-- light:minor-updates:end -->

見出しマップ（`en/claude_code_docs_map.md`）は 9 行が加わり 2 行が外れました。加わったのは 7 つの新しい見出し（`code-review-customize` の 1 つ、`self-hosted-environments-configuration` の 2 つ、`model-config` の 1 つ、`hooks` の 2 つ、`agent-sdk/plugins` の 1 つ）と、改称された `permissions` の見出し、新しいスタンプで、外れたのは改称前の見出しと古いスタンプです。`llms-full.txt` の見出しの増加（7）と同じ見出しで、今回、見出しマップにだけ先に載った見出しはありません。

**参考リンクについて**: 日本語版は、今回変わった 35 ページすべてを取得し、該当する節があるかと今回の内容になっているかを、計 65 項目について確かめました。62 項目は本文で今回の内容になっていることを確かめました。残りの 3 項目（`settings-reference` の `fastMode` と `fastModePerSessionOptIn`、`claude-apps-gateway-config` の `load_test_mode`）は本文で確かめられなかったので、`fastMode` と `load_test_mode` のリンクは英語版だけにしています（`fastModePerSessionOptIn` にはリンクを付けていません）。アンカーは、見出しから作った id か、ページ内・ページ間のリンクが使っている id です。見出しと id が違うもの（`claude-projects` の `#usage-limit-reached`、`permissions` の `#path-rules-that-never-match`）は、ページ内かほかのページのリンクが使っている id です。**changelog ページへのリンクは、本サマリの方針どおり付けていません。**

## 新着情報

<!-- light:whats-new:start -->
**今回、新着情報（`whats-new/`）のページに変更はありません**（最新の週のダイジェストは前回と同じ Week 37 です）。
<!-- light:whats-new:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-11-04.md](./archives/latest/2026-11-04.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-11-04.md](./archives/latest-detail/2026-11-04.md)

<!--
base_commit: 759bf707239c765d7cc90918f4b58b6f5344ef70
head_commit: eeed443cb82c4c74a7a5581909f72f58ace3b41c
generated_at_full: 2026-11-06T15:05:38+09:00
-->
