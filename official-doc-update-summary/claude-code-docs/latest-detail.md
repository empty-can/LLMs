---
対象期間: 2026年10月01日 〜 2026年10月02日
作成日: 2026-10-02
---

# Claude Code 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
**今回は Mods の 10 ページの本文が `llms-full.txt` に入り、changelog には mod を既定でオンにした v2.1.287（2026年10月01日）の 106 項目が積まれました**。サンドボックスのページも全面的に書き直されています。ページ単位で数えると 220 ページ中 92 ページ（新規 10 ページを含む）が変わり、変更は 5,680 行（追加 5,180・削除 500）です。総行数は 106,132 行から 110,852 行に増えました。

主要なものを以下に挙げます。

1. Mods の本文が入り、v2.1.287 から mod が既定でオンになった
2. 組織が mod を止める・自前の mod を先に動かすための管理設定が載った
3. サンドボックスのページが書き直され、管理者が必須にしたサンドボックスではリポジトリの緩める設定が無視されるようになった
4. エージェントビューに名前と結果で絞るフィルターが加わり、覗き見からの返信の扱いが決まった
5. WebFetch を止める環境変数と、ドメインの安全確認が通らなかったときの扱いが載った
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**Mods の本文が入り、v2.1.287 から mod が既定でオンになった**](#1-mods-の本文が入りv21287-から-mod-が既定でオンになった):  
  前回は索引だけだった Mods の 10 ページの本文が `llms-full.txt` に入りました。mod は JavaScript / TypeScript のイベントハンドラーを持つプラグインで、v2.1.287 以降は既定でオンです。早期アクセスの `CLAUDE_CODE_ENABLE_FUNCTION_HOOKS` は無視されます
2. [**組織が mod を止める・自前の mod を先に動かすための管理設定が載った**](#2-組織が-mod-を止める自前の-mod-を先に動かすための管理設定が載った):  
  組み込みのガード `cc-plugin-sec-default@builtin` の `allowManagedModsOnly` で、ユーザーが持ち込む mod を止められます。組織の mod を先に・後に動かす `prependPlugins`・`appendPlugins` も `settings-reference` に節ができました
3. [**サンドボックスのページが書き直され、管理者が必須にしたサンドボックスではリポジトリの緩める設定が無視されるようになった**](#3-サンドボックスのページが書き直され管理者が必須にしたサンドボックスではリポジトリの緩める設定が無視されるようになった):  
  `sandboxing` が 623 行変わりました。管理設定などで `allowUnsandboxedCommands: false` か `allowManagedDomainsOnly` を設定すると、リポジトリの `excludedCommands` などは無視されます（v2.1.285 以降）。ローカルのアドレスに解決されるホスト名を拒否する動き（v2.1.284 以降）も載りました
4. [**エージェントビューに名前と結果で絞るフィルターが加わり、覗き見からの返信の扱いが決まった**](#4-エージェントビューに名前と結果で絞るフィルターが加わり覗き見からの返信の扱いが決まった):  
  `n:<text>`（v2.1.287 以降）と `o:<text>` のフィルターが加わり、組み合わせられるようになりました。覗き見から送ったコマンドはターンの終わりに実行され、`/stop` だけはすぐに止めます
5. [**WebFetch を止める環境変数と、ドメインの安全確認が通らなかったときの扱いが載った**](#5-webfetch-を止める環境変数とドメインの安全確認が通らなかったときの扱いが載った):  
  `CLAUDE_CODE_DISABLE_WEB_FETCH`（v2.1.285 以降）で WebFetch を止められます。ドメインの安全確認がレート制限などで通らなかったときのメッセージと対処が `errors` に節としてまとまりました
<!-- light:highlight-list:end -->

## 1. Mods の本文が入り、v2.1.287 から mod が既定でオンになった

**前回、`llms.txt` と見出しマップにだけ載っていた Mods の 10 ページの本文が、今回 `llms-full.txt` に入りました**（合わせて 3,647 行）。見出しは 180 で、前回マップに載った数と同じです。changelog の v2.1.287 の先頭にも「Added Claude Mods: plugins may now modify deeper behavior」とあります。

`plugins/mods/overview` によると、mod は Claude Code の見た目と動きを変えるプラグインで、JavaScript か TypeScript のイベントハンドラー（mod のページでは「hook」と呼び、設定ファイルのフックは「settings hook」と呼び分けます）でできています。ツール呼び出し・プロンプトの送信・画面の描画などのイベントが起きると Claude Code がハンドラーを呼び、ハンドラーはイベントを**見る（observe）・書き換える（rewrite）・自分で答える（answer）**のいずれかを選びます。

- **できること**: トランスクリプトの横のペインやプロンプトの上の帯を描く、ツール呼び出しの行やスピナーなど Claude Code 自身の表示を描き替える、ツール呼び出しを保留して質問する、Claude のターンを使わずにすぐ動く `/command` を加える、などです。ファイル・プロセス・ネットワークなど自分のコードの外に届くには、必ず mods API（`$`）を呼びます
- **使える場所とバージョン**: CLI と、デスクトップアプリの Code タブです。v2.1.287 以降が必要で、既定でオンです。VS Code 拡張・`claude -p`・Agent SDK・クラウドセッションではハンドラーは動きますが、描いたものは表示されません
- **止め方**: 1 つなら `/plugin` で無効化かアンインストール、そのセッションだけなら `--safe-mode`、自分が入れたすべての mod なら `~/.claude/settings.json` の `"disableAllHooks": true` です。早期アクセスで使った `CLAUDE_CODE_ENABLE_FUNCTION_HOOKS` は v2.1.287 以降は無視されるので、`0` にしても mod は止まりません
- **信頼**: mod はユーザーの権限で、サンドボックスの外で動きます。インストールする前に `claude plugin validate` の `hooks:` と `calls:` の行で、扱うイベントと呼ぶ API を確かめられます。mod は権限の確認の表示だけは変えられません

**組み込みの mod も一覧になりました。** `cc-plugin-agents-md`（`AGENTS.md` の読み込み）、`cc-plugin-diff`（`/diff` のペイン）、`cc-plugin-plugin-authoring`（mod を書くための `plugin-authoring` スキル）、`cc-plugin-sec-default`（組織の管理対象を守るガード）、`cc-plugin-telemetry`、そして既定でオフの **`cc-plugin-you-should-know`** です。最後のものは、長い作業の間に横で動くエージェントが、ユーザーが見落としそうなことをプロンプトの上に知らせるもので、`/plugin enable cc-plugin-you-should-know@builtin` でオンにします（changelog では、テレメトリをオンにしたファーストパーティのセッション向けとされています）。

各ページの内容は「新規追加されたページ」の 1〜10 にまとめています。

- [Mods の概要 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/plugins/mods/overview#turn-mods-on-or-off)
- [Mods overview - Claude Code Docs (English)](https://code.claude.com/docs/en/plugins/mods/overview#turn-mods-on-or-off)

## 2. 組織が mod を止める・自前の mod を先に動かすための管理設定が載った

**`plugins/mods/admin` によると、管理設定がない状態では mod はオンで、組み込みのガード `sec-default@builtin`（`/plugin` では `cc-plugin-sec-default`）が、ユーザーが入れた mod より先に読み込まれます。** ガードが読み込まれるのは、マシンに管理設定がある場合か、Team / Enterprise プランでサインインしている場合です。ガードは、管理しているフック・システムプロンプト・管理された `CLAUDE.md`・管理された MCP サーバーなどをユーザーの mod から守ります。ガードが読み込まれる環境では、ユーザーの mod は `deny` ルールが拒否する呼び出しを承認できません。

- **ユーザーの mod を止める**: 管理設定の `pluginConfigs` で、`cc-plugin-sec-default@builtin` の `options` に `"allowManagedModsOnly": true` を設定します。ユーザーが入れた mod、`--plugin-dir` の mod、セッション中に Claude が書いた mod は読み込まれず、組織の mod と組み込みの mod は動きます。ユーザーの settings hook やステータスラインは止まりません。もう 1 つのオプション `allowModsToOverrideDenyRules` を `true` にすると、ユーザーの mod が `deny` ルールの拒否を承認できるようになります
- **組織の mod と見なされる条件**: 管理設定の `enabledPlugins` でオンにし、マーケットプレイスを各マシン上の絶対パスのディレクトリとして管理設定で指定し、そのマーケットプレイスが相対パスでプラグインを載せている場合です。GitHub などから取得した mod はユーザーの mod と見なされます
- **順序**: `settings-reference` に **`prependPlugins`**（ユーザーの mod より先に動かす）と **`appendPlugins`**（後に動かす）の節ができました。どちらもスコープは「ユーザーまたは管理」ですが、ユーザー設定から読むのは、管理設定のないマシンで Team / Enterprise プランでサインインしていない場合だけです。管理設定で `prependPlugins` を設定するときは、ガードを残すために `sec-default@builtin` をリストに含めます
- **ほかの設定との関係**: `allowManagedHooksOnly` はより広く、ユーザーの設定ファイルのフックも止めます。`disableAllHooks` を管理設定に置くと、組織の mod も含めて止まります（`settings-reference` にもこの関係が追記されました）。`disableSideloadFlags` は `--plugin-dir`・`--plugin-url` を拒否し、Claude が書いた mod も読み込まなくします

`extraKnownMarketplaces` の `directory` ソースの説明も、「開発用」だけでなく「組織が各マシンに配るマーケットプレイス」にも使えると改められています。

- [すべての設定 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/settings-reference#prependplugins)
- [All settings - Claude Code Docs (English)](https://code.claude.com/docs/en/settings-reference#prependplugins)
- [組織の mod を管理する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/plugins/mods/admin#stop-user-installed-mods-from-loading)
- [Manage mods for your organization - Claude Code Docs (English)](https://code.claude.com/docs/en/plugins/mods/admin#stop-user-installed-mods-from-loading)

## 3. サンドボックスのページが書き直され、管理者が必須にしたサンドボックスではリポジトリの緩める設定が無視されるようになった

**`sandboxing` は 623 行（追加 439・削除 184）変わり、構成から書き直されました。** 冒頭に「What the sandbox restricts」（書き込み・読み取り・ネットワーク・環境変数の既定と、それを変える設定の表）と「What runs outside the sandbox」（ファイルツール・MCP サーバー・フック・`!` で自分で打ったコマンドなどは外で動く）が置かれ、「Confirm commands run inside the sandbox」で動作を確かめる手順も加わりました。トラブルシューティングは症状ごとの見出しに分かれています。

**中身の変更で大きいのは、「admin-required（管理者が必須にした）」サンドボックスという考え方です**（v2.1.285 以降）。

- **admin-required になる条件**: 管理設定で `allowUnsandboxedCommands` を `false` にした場合（`--settings` で `false` にした場合も、管理設定が `true` にしていなければ同じ）か、管理設定で `allowManagedDomainsOnly` を `true` にした場合です
- **無視されるもの**: その間、リポジトリの `.claude/settings.json` と `.claude/settings.local.json` にある、サンドボックスを緩める設定は無視されます。`excludedCommands`・`network.allowedDomains`・プロキシのポートなどはすべてのエントリが、`filesystem.allowWrite` や `Edit(...)` の許可ルールはサンドボックスへの書き込みの許可が無視されます。v2.1.282〜v2.1.284 では `excludedCommands` だけが無視されていました
- **admin-required でなくても効くロック**: 管理設定か `--settings` の `deniedDomains` はリポジトリのプロキシのポートを、`strictAllowlist` はリポジトリの `allowedDomains` などを無視させます（「Locks that apply without an admin-required sandbox」）
- **ユーザー設定の `false`**: ユーザー設定で `allowUnsandboxedCommands` を `false` にすると、プロジェクトが `true` にしても `false` のままになります（v2.1.285 より前はプロジェクトの `true` が勝っていました）。ただし、これだけでは admin-required になりません
- **プロキシのポート**: `httpProxyPort`・`socksProxyPort` を設定できるファイルが、ほかの設定によって限られるようになりました（v2.1.285 より前はどの設定ファイルでも設定できました）。ポートを設定すると、Claude Code のドメインのリストや確認はそのトラフィックに効かなくなる、という警告も加わっています

**ネットワークの動きも詳しくなりました。** 許可したホスト名でも、ローカルのアドレス（`127.0.0.1` などのループバック、`169.254.169.254` などのリンクローカル、自分のマシンのアドレス）にしか解決されない場合、サンドボックスのプロキシは接続を拒否します（v2.1.284 以降。`localhost` と `*.localhost` は例外）。許可していないホストへの接続を、権限モードごとにどう扱うかも表になりました（`bypassPermissions` は許可、Manual・`acceptEdits` は確認、auto はコマンドがホストを列挙して分類器が承認した場合を除き拒否、`dontAsk` は拒否）。

トラブルシューティングには、SSH で `git` を使えない場合（macOS ではサンドボックスの中では失敗する）、データベースのクライアントなどプロキシを使わないツールが許可したホストに届かない場合、localhost のサーバーに届かない場合、`resolved to a loopback address` で拒否される場合、上位の設定のために `/sandbox` が開かない場合（`Sandbox settings are overridden by a higher-priority configuration`）などの節が加わりました。「Platform and tool compatibility」の節は消え、対応する OS の説明は冒頭に移っています。範囲の説明には、mod が始めたプロセスはサンドボックスの外で動くことも加わりました。

- [サンドボックス化された Bash ツールを設定する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/sandboxing#repository-settings-under-an-admin-required-sandbox)
- [Configure the sandboxed Bash tool - Claude Code Docs (English)](https://code.claude.com/docs/en/sandboxing#repository-settings-under-an-admin-required-sandbox)

## 4. エージェントビューに名前と結果で絞るフィルターが加わり、覗き見からの返信の扱いが決まった

**`agent-view` の「Filter sessions」に、2 つのフィルターが加わりました。**

- **`n:<text>`**: 名前か最初のプロンプトにその文字列を含むセッション（例: `n:login`）。v2.1.287 以降
- **`o:<text>`**: 結果にその文字列を含むセッション（例: `o:merged`）。`o:` だけなら、結果を報告したすべてのセッション
- `s:<state>` はグループの見出しにも当たるようになりました（例: `s:ready`）。フィルターはスペースで区切って組み合わせられ（例: `s:blocked a:reviewer`）、フィルター中は畳んだグループが開いて最初の一致が選ばれるので、`Enter` でそれを開けます

**「Peek and reply」も書き直されました。** 作業中のセッションへの返信はメッセージのキューに入り、コマンドは今のターンが終わってから実行されます（v2.1.287 以降。セッション自身のプロンプトでは打った時点で動くコマンドも同じ）。返信がちょうど `/stop` のときだけは、セッションをすぐに止めます。選択肢のある質問には番号キーで選んで `Enter`、提案された返信は `Tab` で入力欄に入れられます。権限の確認・サンドボックスの確認・MCP サーバーの入力要求には返信では答えられないので、`→` で接続して答えます。キー操作には `PgUp` / `PgDn`・`Home` / `End` が加わりました。

関連して、`commands` の `/stop` も覗き見からの返信として使えると改められました。

- [エージェントビューで複数のエージェントを管理する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/agent-view#filter-sessions)
- [Manage multiple agents with agent view - Claude Code Docs (English)](https://code.claude.com/docs/en/agent-view#filter-sessions)

## 5. WebFetch を止める環境変数と、ドメインの安全確認が通らなかったときの扱いが載った

**`tools-reference` に「WebFetch availability」の節ができました。** v2.1.285 以降は `CLAUDE_CODE_DISABLE_WEB_FETCH=1` で WebFetch を止められます（WebSearch は残ります。`env-vars` にも追加）。Team / Enterprise の claude.ai アカウントでサインインし LLM ゲートウェイを使っていない場合、WebFetch はセッション開始時に `api.anthropic.com` から取得する組織のポリシーにも左右されます。WebFetch がない場合は `/status` の `Organization policy` の行で、ポリシーが読み込めずに WebFetch が保留されていないかを確かめます。

**`errors` には「WebFetch domain safety check failed」の節ができました。** WebFetch は取得の前にホスト名を `api.anthropic.com` に送ってドメインの安全性を確かめ、確かめられないとページを取得しません。

- **`rate-limited`**: 確認先が HTTP `429` を返した場合です。メッセージは、ループで再試行せずページなしで続け、後で 1 回だけ試すよう Claude に伝えます。よく起きるネットワークでは `skipWebFetchPreflight: true` で確認を省けます。v2.1.286 より前は「約 1 分後に再試行」という文面、v2.1.285 より前は `Unable to verify` のメッセージで報告されていました
- **`Unable to verify`**: 確認のリクエストが失敗・タイムアウトした場合です。`api.anthropic.com` を許可するか、`skipWebFetchPreflight` で確認を省きます

- [ツールリファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/tools-reference#webfetch-availability)
- [Tools reference - Claude Code Docs (English)](https://code.claude.com/docs/en/tools-reference#webfetch-availability)
- [エラーリファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/errors#webfetch-domain-safety-check-failed)
- [Error reference - Claude Code Docs (English)](https://code.claude.com/docs/en/errors#webfetch-domain-safety-check-failed)

## 新規追加されたページ

<!-- light:new-pages:start -->
- [**Mods overview**](#1-mods-overview) ([日本語](https://code.claude.com/docs/ja/plugins/mods/overview) / [English](https://code.claude.com/docs/en/plugins/mods/overview)):  
  mod とは何か、入れ方・試し方、信頼の判断、止め方、動く場所、ほかの拡張との比較、組み込みの mod（250 行）
- [**Create a mod**](#2-create-a-mod) ([日本語](https://code.claude.com/docs/ja/plugins/mods/create) / [English](https://code.claude.com/docs/en/plugins/mods/create)):  
  Claude に mod を書かせる方法と、ツール呼び出しを数える mod を自分で書くチュートリアル（366 行）
- [**Mods reference**](#3-mods-reference) ([日本語](https://code.claude.com/docs/ja/plugins/mods/reference) / [English](https://code.claude.com/docs/en/plugins/mods/reference)):  
  ファイル構成、フック関数、全イベント、mods API のメソッド、描画先、要素、制限、設定、コマンド（281 行）
- [**Draw in the interface with a mod**](#4-draw-in-the-interface-with-a-mod) ([日本語](https://code.claude.com/docs/ja/plugins/mods/interface) / [English](https://code.claude.com/docs/en/plugins/mods/interface)):  
  ペイン・プロンプトの上の帯・ボタン・入力欄を描き、押下と入力を扱い、状態を保つ（827 行）
- [**Interface gallery for mods**](#5-interface-gallery-for-mods) ([日本語](https://code.claude.com/docs/ja/plugins/mods/gallery) / [English](https://code.claude.com/docs/en/plugins/mods/gallery)):  
  描ける要素をサンプルコードと画面写真で示す（388 行）
- [**React to events with a mod**](#6-react-to-events-with-a-mod) ([日本語](https://code.claude.com/docs/ja/plugins/mods/events) / [English](https://code.claude.com/docs/en/plugins/mods/events)):  
  ツール呼び出し・プロンプト・ターンを見る・書き換える・答える方法と、mod が動く順序（324 行）
- [**Use the mods API**](#7-use-the-mods-api) ([日本語](https://code.claude.com/docs/ja/plugins/mods/api) / [English](https://code.claude.com/docs/en/plugins/mods/api)):  
  コマンドとツールの追加、モデルの呼び出し、バックグラウンドの処理、セッション間のメッセージ、ファイルとネットワーク（191 行）
- [**Test a mod**](#8-test-a-mod) ([日本語](https://code.claude.com/docs/ja/plugins/mods/test) / [English](https://code.claude.com/docs/en/plugins/mods/test)):  
  セッション・サインイン・ネットワークなしで動く自動テストと `claude plugin test`（399 行）
- [**Troubleshoot a mod**](#9-troubleshoot-a-mod) ([日本語](https://code.claude.com/docs/ja/plugins/mods/troubleshoot) / [English](https://code.claude.com/docs/en/plugins/mods/troubleshoot)):  
  mod が何もしない理由を症状とメッセージから引く。拒否メッセージとデバッグログ（228 行）
- [**Manage mods for your organization**](#10-manage-mods-for-your-organization) ([日本語](https://code.claude.com/docs/ja/plugins/mods/admin) / [English](https://code.claude.com/docs/en/plugins/mods/admin)):  
  管理設定でユーザーの mod を止める、組織の mod だけを許す、mod を審査する、自前の mod でポリシーを強制する（393 行）
<!-- light:new-pages:end -->

前回、索引と見出しマップにだけ載っていた 10 ページです。今回、本文が `llms-full.txt` に初めて入ったため、新規追加として扱います（行数は `llms-full.txt` から切り出した各ページの `git diff --no-index --numstat` の追加行数）。

## 1. Mods overview

mod の入口になるページです。内容はハイライト 1 のとおりで、mod を「作る（Claude に頼むか自分で書く）」「入れる（`/plugin install <plugin>@<marketplace>`）」「既にあるものを使う（組み込みの mod）」の 3 つの始め方を案内します。

サンプルの mod として、`claude-code-playground` リポジトリの `token-weather`（コンテキストウィンドウの予報をプロンプトの上に描く）、`blast-radius`（`rm -rf` や強制プッシュなどを保留し、変わるものを見せて続行か取り消しを選ばせる）、`replay-theater`（前のターンのファイル編集を順に見る `/replay`）が紹介されています。セッションが読み込んだ mod は、`/plugin` のタブの下に `1 mod active · first-mod` のように表示されます。

mod・settings hook・スキル・MCP サーバーを比べる表もあり、ペインや帯、独自のコマンド、イベントの書き換えが欲しいときは mod を選ぶ、としています。

- [Mods の概要 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/plugins/mods/overview#compare-mods-settings-hooks-skills-and-mcp-servers)
- [Mods overview - Claude Code Docs (English)](https://code.claude.com/docs/en/plugins/mods/overview#compare-mods-settings-hooks-skills-and-mcp-servers)

## 2. Create a mod

**Claude に頼む方法**: 対話型のセッションで欲しい mod を説明すると、Claude は組み込みの `plugin-authoring` スキルに沿って、`~/.claude/dev-mods/<セッション ID>/` の下に mod を書きます（`/plugin-authoring` で自分で読み込むこともできます）。最初のファイルを保存すると、そのセッションでホットリロードを有効にするかを尋ねられ、有効にするとターンの終わりに読み込まれます。Claude が書いた mod はそのセッションでだけ読み込まれ、残すには自分のディレクトリに写して `--plugin-dir` で読み込むかマーケットプレイスに載せます。`claude -p` や `dontAsk` モード、信頼していないワークスペース、`--safe-mode`・`--bare`・`disableAllHooks` のセッションでは読み込まれません。

**自分で書く方法**: ツール呼び出しを数え、スピナーの横に表示し、コマンドを加える mod を作るチュートリアルです。Claude Code は `.js` と `.ts` を直接読み込むので、Node.js やバンドラー、ビルドは要りません。`claude plugin validate` で Claude Code が mod から読み取る内容を確かめ、`--plugin-dir` で保存のたびに読み込み直しながら作ります。

- [Mod を作成する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/plugins/mods/create#ask-claude-for-a-mod)
- [Create a mod - Claude Code Docs (English)](https://code.claude.com/docs/en/plugins/mods/create#ask-claude-for-a-mod)

## 3. Mods reference

v2.1.287 時点の CLI とデスクトップアプリについて、イベント・mods API のメソッド・描画先などを一覧にしたリファレンスです。完全な定義は GitHub の TypeScript の型定義（`claude-code.d.ts`）だとしています。

- **ファイル**: `.claude-plugin/plugin.json`、`modules` で hooks モジュールを指す `hooks/hooks.json`、`register(on, options)` を公開する hooks モジュール（`.js`・`.ts` など）。`$.state` を使う場合は、マニフェストの `types` で指す `.d.ts` が要ります
- **フック関数**: `on(イベント名, [マッチャー], フック)` で登録し、フックは `$`（mods API）・`e`（凍結されたイベント）・`next`（次のハンドラー）を受け取ります。`next.origin.tier` は `prepend`・`user`・`append`・`builtin` のいずれかです
- **制限**: 1 つのイベントでのフック自身の実行は 10 秒、`$.process.run` は既定 30 秒・最長 10 分、`$.fs.read`・`$.fs.write` は 1 ファイル 4 MiB、`$.store` は合計 4 MiB などです
- **設定と環境変数**: `CLAUDE_CODE_PLUGIN_DIRS`・`CLAUDE_CODE_PLUGIN_DIR_WATCH`・`prependPlugins`・`appendPlugins`・`allowManagedModsOnly`・`allowModsToOverrideDenyRules` などの表があります

- [Mods リファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/plugins/mods/reference#mods-api-methods)
- [Mods reference - Claude Code Docs (English)](https://code.claude.com/docs/en/plugins/mods/reference#mods-api-methods)

## 4. Draw in the interface with a mod

mod が描ける場所（描画先）と、その描き方のページです。Claude Code は描画先を描く直前に `ui.render` イベントを起こし、フックがそこに描くものを返します。ターミナルでは、右側のペイン、トランスクリプト右上のトースト、トランスクリプト内のログ行、プロンプトの上の帯、プロンプトの下のステータスラインに描けて、メッセージ・ツール呼び出しの行・スピナーは描き替えられます。プロンプト自体は Claude Code のものです。

ボタンの押下や入力欄の入力を扱う方法、再描画やセッションをまたいで状態を保つ方法、Claude Code が既に描いているもの（質問のダイアログなど）を変える方法も説明しています。

- [mod でインターフェイスに描画する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/plugins/mods/interface#build-a-pane-with-tabs)
- [Draw in the interface with a mod - Claude Code Docs (English)](https://code.claude.com/docs/en/plugins/mods/interface#build-a-pane-with-tabs)

## 5. Interface gallery for mods

mod が描ける要素（テキスト・ボックス・ボタン・入力欄・Markdown・コード・差分など）を、要素ごとのサンプルコードと、多くはターミナルのペインの画面写真で示すページです。サンプルは 1 つの要素とその中身だけのコード片で、mod 全体ではありません。描き方の基本は「Draw in the interface」、主なプロパティとアプリごとの対応は Mods reference の要素の表を参照するよう案内しています。

- [mod のインターフェイスギャラリー - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/plugins/mods/gallery#try-a-sample)
- [Interface gallery for mods - Claude Code Docs (English)](https://code.claude.com/docs/en/plugins/mods/gallery#try-a-sample)

## 6. React to events with a mod

フックがイベントをどう扱うかのページです。同じイベントのハンドラーはミドルウェアの連鎖になり、`next(e)` は次の mod のフック、連鎖の最後では Claude Code 自身の動きを呼びます。`next` をそのまま呼べば「見る」、変えたコピーを渡せば「書き換える」、`next` を呼ばずに値を返せば「答える」になります。

ツール呼び出しを止めたり変えたりする方法、ターンを追う方法、扱うイベントをマッチャーで絞る方法、失敗したフックの扱い、そしてほかの mod と並んだときの**動く順序**を説明しています。順序は、①組み込みのガード・`prependPlugins` の mod・そのほかの組織の mod、②ユーザーが入れた mod、③`appendPlugins` の mod、④そのほかの組み込みの mod です。管理設定の `PreToolUse` フックは最初の mod より前に動いてその拒否は最終となり、ほかの設定ファイルやプラグインの `PreToolUse` フックは最後の mod の後に動きます。

- [mod でイベントに反応する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/plugins/mods/events#the-order-mods-run-in)
- [React to events with a mod - Claude Code Docs (English)](https://code.claude.com/docs/en/plugins/mods/events#the-order-mods-run-in)

## 7. Use the mods API

フックの第 1 引数 `$` で呼ぶ mods API のページです。`session.start` のフックでコマンド（ユーザーが実行）とツール（Claude が呼ぶ）を登録すると、最初のターンから使えます。モデルを呼ぶ `$.model.complete`、イベントの合間に処理を動かすタイマー、ほかのセッションとのメッセージのやり取り、ファイル・プロセス・ネットワークに届く `$.fs`・`$.process`・`$.http` などを扱います。

`plugins/mods/admin` では、`$.fs.read`・`$.process.run`・`$.http.fetch`・`$.env.get`・`$.model.complete`・`$.prompt.submit` などが、審査で特に確認すべき呼び出しとして挙げられています。

- [mods API を使用する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/plugins/mods/api#add-a-command-or-a-tool)
- [Use the mods API - Claude Code Docs (English)](https://code.claude.com/docs/en/plugins/mods/api#add-a-command-or-a-tool)

## 8. Test a mod

mod の自動テストのページです。テストファイルは名前を `.test.ts` で終え、`claude-code/testing` モジュールのテストキットを読み込みます。テストはイベントを起こし、Claude Code の応答をスタブにし、ボタンを押して、フックがしたことを確かめます。セッション・サインイン・ネットワークは要りません。シェルで `claude plugin test [directory]` を実行し、失敗があると終了ステータス 1 になります（`plugins/cli-reference` にも「plugin test」の節ができました）。タイマー、描画、`/clear` の後の描画、ポリシーの mod のテスト方法も載っています。

- [mod をテストする - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/plugins/mods/test#write-a-test)
- [Test a mod - Claude Code Docs (English)](https://code.claude.com/docs/en/plugins/mods/test#write-a-test)

## 9. Troubleshoot a mod

mod の読み込みやフックが失敗すると Claude Code はそれを飛ばしてセッションを続けるため、壊れた mod は「何もしない」ように見えます。このページは、`claude plugin validate` で Claude Code が mod から読み取る内容を確かめ、mod の名前が入った 1 行のログを探す手順から始め、症状やメッセージから原因を引けるようにしています。

「Your version is older than 2.1.287」（mod が既定でオンになる前の版）のように、メッセージや状況をそのまま見出しにした節が並びます。組み込みのガードが出すメッセージ、拒否のメッセージ、デバッグログの読み方もあります。

- [mod のトラブルシューティング - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/plugins/mods/troubleshoot#your-version-is-older-than-2-1-287)
- [Troubleshoot a mod - Claude Code Docs (English)](https://code.claude.com/docs/en/plugins/mods/troubleshoot#your-version-is-older-than-2-1-287)

## 10. Manage mods for your organization

管理設定を配る管理者向けのページで、内容はハイライト 2 のとおりです。このほか、ユーザーが何を読み込めるかが既存のプラグインの制御（マーケットプレイスの許可リスト、`disableSideloadFlags`）によって変わることの表、`claude plugin validate` の `calls:` 行で注意すべき呼び出しの表、ポリシーごとに設定する値の表（ユーザーの mod なし・組織の mod だけ・承認したマーケットプレイスの mod だけ・自前の mod でほかを確かめる）があります。自前の mod でポリシーを強制する例と、確認に失敗したときに mod を拒否する方法も載っています。

- [組織の mod を管理する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/plugins/mods/admin#know-what-happens-by-default)
- [Manage mods for your organization - Claude Code Docs (English)](https://code.claude.com/docs/en/plugins/mods/admin#know-what-happens-by-default)

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
- [**Configure the sandboxed Bash tool**](#1-configure-the-sandboxed-bash-tool) ([日本語](https://code.claude.com/docs/ja/sandboxing#what-the-sandbox-restricts) / [English](https://code.claude.com/docs/en/sandboxing#what-the-sandbox-restricts)):  
  623 行（追加 439・削除 184）が変わりました。ページ全体が書き直されています（ハイライト 3）
- [**All settings**](#2-all-settings) ([日本語](https://code.claude.com/docs/ja/settings-reference#allowmanagedpermissionrulesonly) / [English](https://code.claude.com/docs/en/settings-reference#allowmanagedpermissionrulesonly)):  
  179 行（追加 127・削除 52）が変わりました。`prependPlugins`・`appendPlugins` の節と、サンドボックスの各キーのスコープの注記が加わりました
- [**Error reference**](#3-error-reference) ([日本語](https://code.claude.com/docs/ja/errors#cannot-add-mcp-server-when-managed-settings-allow-only-plugin-servers) / [English](https://code.claude.com/docs/en/errors#cannot-add-mcp-server-when-managed-settings-allow-only-plugin-servers)):  
  107 行（追加 94・削除 13）が変わりました。新しい節が 3 つ加わり、認証まわりの説明が改められました
- [**Troubleshoot plugins**](#4-troubleshoot-plugins) ([日本語](https://code.claude.com/docs/ja/plugins/troubleshooting#marketplace-is-added-but-ignored) / [English](https://code.claude.com/docs/en/plugins/troubleshooting#marketplace-is-added-but-ignored)):  
  60 行（追加 55・削除 5）が変わりました。マーケットプレイスが無視される場合と、npm のソースが断られる場合の節が加わりました
- [**Customize sessions in self-hosted environments**](#5-customize-sessions-in-self-hosted-environments) ([日本語](https://code.claude.com/docs/ja/self-hosted-environments-configuration#git-configuration-inside-lifecycle-hooks) / [English](https://code.claude.com/docs/en/self-hosted-environments-configuration#git-configuration-inside-lifecycle-hooks)):  
  55 行（追加 47・削除 8）が変わりました。ライフサイクルフックの git の設定を固定する説明と、システムプロンプトのフラグの扱いが加わりました
- [**Plugin manifest reference**](#6-plugin-manifest-reference) ([日本語](https://code.claude.com/docs/ja/plugins/manifest-reference#directory-listing-fields) / [English](https://code.claude.com/docs/en/plugins/manifest-reference#directory-listing-fields)):  
  50 行（追加 48・削除 2）が変わりました。ディレクトリの掲載用のフィールドと、予約された名前のチェックが加わりました
<!-- light:updated-pages:end -->

`llms-full.txt` から切り出したページ単位の差分（`git diff --no-index --numstat`）が 50 行以上の既存ページを挙げています。changelog（109 行、すべて追加）は、これまでどおり「軽微な更新」で扱います。

## 1. Configure the sandboxed Bash tool

**ページの説明文も「組み込みのサンドボックスで、シェルコマンドが届くファイルとネットワークのホストを制限する。オンにし、境界を決め、壊れたものを直す」に変わりました。** 主な中身はハイライト 3 のとおりです。そのほかの変更は次のとおりです。

- **`excludedCommands` の節ができた**: パターンは `Bash(...)` の権限ルールと同じ書き方で、ワイルドカードのない `docker` は引数なしの `docker` にしか当たらないので ` *` で終えること、1 回の呼び出しに含まれるすべてのコマンドが当たる必要があること、リダイレクトや `cd`・`$(...)` を含む呼び出しはサンドボックスに残ることが、箇条書きでまとまりました。除外したコマンドはユーザーのすべての権限で動くので、狭いパターンにするよう警告しています
- **strict sandbox mode が独立した小節になった**: 「Turn off the retry with strict sandbox mode」で、`failIfUnavailable` と組み合わせる方法、ユーザー設定の `false` の扱い（ハイライト 3）、自分で打った `!` のコマンドがサンドボックスで動くセッションをまとめています
- **サンドボックスの外での再試行**: 誰が承認するかが権限モードごとに整理されました（`bypassPermissions` は確認なし、Manual と `acceptEdits` は「Bash command (unsandboxed)」の確認、auto は分類器、`dontAsk` は拒否）。`Bash(curl *)` のような許可ルールに当たると、確認なしでサンドボックスの外で動くことも明記されました
- **組織向け**: ネイティブの Windows についての注意が詳しくなり、`failIfUnavailable` を配るとそのマシンでは起動時に終了すること、OS ごとに配る場合はサーバー管理設定ではなく MDM か管理設定ファイルを使う（サーバー管理設定は組織の全ユーザーに適用される）ことが加わりました
- **トラブルシューティング**: 箇条書きだった項目が見出しになり、`docker` の対処は `docker *` ではなく `docker compose *` のような狭いパターンを勧める形になりました

- [サンドボックス化された Bash ツールを設定する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/sandboxing#run-commands-outside-the-sandbox-with-excludedcommands)
- [Configure the sandboxed Bash tool - Claude Code Docs (English)](https://code.claude.com/docs/en/sandboxing#run-commands-outside-the-sandbox-with-excludedcommands)

## 2. All settings

- **`prependPlugins`・`appendPlugins`**: 節と索引の行ができました（ハイライト 2）
- **サンドボックスのキーのスコープ**: `sandbox.enabled`・`failIfUnavailable`・`excludedCommands`・`filesystem.allowWrite`・`filesystem.allowRead`・`network.allowedDomains` など多くのキーのスコープに、「プロジェクトとローカルの設定には制限がある」という注記とサンドボックスのページへのリンクが付きました（ハイライト 3）。`httpProxyPort`・`socksProxyPort` は、自前のプロキシを指定するとそのトラフィックには Claude Code のドメインのリストと確認が効かなくなる、と明記されました
- **`excludedCommands`**: `git clone`・`git init`・`git worktree add` などで、パスが絶対パス・`~` で始まる・`..` を含む場合はサンドボックスに残る、と加わりました（例: `git *` のもとでも `git clone <url> ~/tools` は残る）
- **`allowLocalBinding`**: macOS でポートを待ち受けるだけでなく localhost の任意のポートに接続できるようになる、と書き改められ、Linux と WSL2 では効果がないことが加わりました
- **`allowManagedPermissionRulesOnly`**: v2.1.282 以降は、リポジトリの `.claude/`、`~/.claude/skills/`・`~/.claude/commands/`（claude.ai から同期したスキルを含む）、`--add-dir`、スキルのディレクトリ内の `.claude-plugin` のプラグインにあるスキルとコマンドの `allowed-tools` も無視する、と加わりました。管理設定のスキルと同梱のスキルは `allowed-tools` を保ちます
- **`allowManagedHooksOnly`・`disableAllHooks`**: mod についての説明が加わりました（ハイライト 2）
- **`awsAuthRefresh`・`gcpAuthRefresh`**: 同じコマンドと資格情報を使う複数のプロセスで同時に確認が失敗すると、1 つのプロセスだけがコマンドを実行し、ほかはそれを待つ（60 秒待つと自分で実行する）と加わりました。止めるには `CLAUDE_CODE_DISABLE_AUTH_REFRESH_LOCK=1` です（v2.1.286 以降、`env-vars` にも追加）
- **AWS の再署名**: アクセスキー ID のエントリの `injectHosts` のホストで再署名し、`sessionTokenVar` を設定すると本物のトークンを `x-amz-security-token` として送る、などの規則が加わりました

- [すべての設定 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/settings-reference#allowmanagedpermissionrulesonly)
- [All settings - Claude Code Docs (English)](https://code.claude.com/docs/en/settings-reference#allowmanagedpermissionrulesonly)

## 3. Error reference

**新しい節が 3 つ加わりました**（前回、見出しマップにだけ先に載っていたものを含みます）。

- **「Cannot add MCP server when managed settings allow only plugin servers」**: 管理設定の `strictPluginOnlyCustomization` が `true`（または `mcp` を含むリスト）のとき、`claude mcp add`・`add-json` は保存せずに終了コード 1 で終わります。v2.1.284 より前は保存して成功と表示し、そのサーバーは読み込まれませんでした（`managed-mcp` にも追記）
- **「Conflict between a system prompt flag and its file form」**: `--append-subagent-system-prompt` と `--append-subagent-system-prompt-file` は一緒に使えません。v2.1.283 より前は `--system-prompt` と `--system-prompt-file` などの組も同じく衝突していましたが、今は組み合わせられます（`cli-reference` の「System prompt flags」にも追記）
- **「WebFetch domain safety check failed」**: ハイライト 5 のとおりです

**既存の節の変更**は次のとおりです。

- **OAuth のトークンが取り消された・期限切れ**: `-p` と Agent SDK では `Failed to authenticate: OAuth token revoked. …` と表示され、構造化されたエラーコードは `authentication_failed` です。v2.1.287 より前は `Your account does not have access to Claude. …` という文面でした。`-p` やプログラムが保存済みのログインを使う場合は、同じ環境で `claude` を起動して `/login` してから実行し直します
- **Not logged in**: 同じ設定ディレクトリを使う別のウィンドウで claude.ai にサインインすると、このメッセージを出しているセッションもそのログインを使い始めます（macOS では v2.1.286 より前は再起動が必要でした）
- **Cloud gateway のサインインを求める起動時のメッセージ**: 設定されている資格情報とその場所、取り除く手順を名指しするようになりました（v2.1.284 以降）。対処も「メッセージの最後の手順に従う」になりました
- **自動再試行**: 考え終えた後、テキストやツール呼び出しを始める前にサーバーエラーか過負荷の応答が来た場合、最大 2 回再試行します（v2.1.284 より前はターンを終えていました）
- 索引の表に、Remote Control の組織ポリシーの 2 つのメッセージ、マーケットプレイスが無視される場合、npm のソースの拒否などが加わりました。使用量の上限の待機の説明は `interactive-mode` への参照になりました

- [エラーリファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/errors#cannot-add-mcp-server-when-managed-settings-allow-only-plugin-servers)
- [Error reference - Claude Code Docs (English)](https://code.claude.com/docs/en/errors#cannot-add-mcp-server-when-managed-settings-allow-only-plugin-servers)

## 4. Troubleshoot plugins

- **「`Marketplace "<name>" is added but ignored`」**: `~/.claude/plugins/known_marketplaces.json` のエントリが、読み込むたびのチェックに通らない場合です。そのマーケットプレイスとそこから入れたプラグインは読み込まれなくなり、`claude plugin list` が理由と直し方を示します。理由は、場所がネットワークドライブにある・パスに `.` か `..` がある、git の URL が使えない、`extraKnownMarketplaces` の宣言とソースが違う、などです。ネットワーク上の場所を使い続けるには、ユーザー設定か管理設定の `extraKnownMarketplaces` で宣言します（リポジトリの設定では数えません）。v2.1.286 より前は、理由に関係なく `Marketplace <name> not found` と報告されていました
- **「`An npm plugin source must name a registry package`」**: マーケットプレイスの `npm` ソースの `package` が、レジストリのパッケージか tarball へのリンクでない場合です。git のリポジトリなら `github`・`url`・`git-subdir` のソースを使います（`plugins/marketplace-reference` の「npm plugin source」にも、断られる値の一覧が加わりました）
- **「Cannot add marketplace … its source doesn't match its extraKnownMarketplaces entry …」**: 見出しとメッセージの文面が改められ（v2.1.287 より前は「its network source differs …」）、どの場合に「違う」と見なすか（設定していない `ref` がある、`https://github.com/` の URL で渡した、など）と、宣言どおりのソースで追加する手順が加わりました
- `claude plugin validate` のエラーの表に、予約された名前のエラーが加わりました（「6. Plugin manifest reference」参照）

- [プラグインのトラブルシューティング - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/plugins/troubleshooting#marketplace-is-added-but-ignored)
- [Troubleshoot plugins - Claude Code Docs (English)](https://code.claude.com/docs/en/plugins/troubleshooting#marketplace-is-added-but-ignored)

## 5. Customize sessions in self-hosted environments

- **「Git configuration inside lifecycle hooks」**: `checkout` と `post-session` のフックが実行する git に、ランナーが `GIT_CONFIG_COUNT`・`GIT_CONFIG_KEY_n`・`GIT_CONFIG_VALUE_n` などで設定を固定するようになりました（v2.1.280 以降）。セッションが書き込める `~/.gitconfig` や `.git/config` から、フックの権限でコードが動くのを防ぐためです。`core.hooksPath` は `/dev/null`、`core.fsmonitor` は空、`GIT_ALLOW_PROTOCOL` は `https:http:ssh`、`core.sshCommand`・`core.askPass` は設定ファイルから読まず、gpg のプログラムはランナーが決めます。`--configure-git` ではフックのコミットはセッションとして署名されます。資格情報ヘルパーやフィルタードライバーなど、ランナーが固定しない設定は引き続き読まれる、という注意もあります
- **「Pass the system prompt flags through」**: v2.1.281 以降のランナーは、コントロールプレーンが送るシステムプロンプトをファイルに書き、`--system-prompt-file <path>`・`--append-system-prompt-file <path>` としてラッパーに渡します。ラッパーは `exec "$CLAUDE_RUNNER_CLAUDE_BIN" "$@"` で転送し、後ろに自分のファイルのフラグを足すとサーバーの指示を置き換えてしまう、と注意しています
- **自動メモリ**: Claude Tag のセッション以外では、セルフホスト環境のセッションの自動メモリは既定でオフで、ランナーのスナップショットは `~/.claude/projects/` を含まない、と加わりました（`memory` にも追記）
- セッションのトークンの `act` クレームの説明から、上流の ID プロバイダーのサブジェクトが外れました（`self-hosted-environments-identity` でも `act.attested_by` は予約済みで「無いものと考える」とされました）

- [セルフホストされた環境でセッションをカスタマイズする - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/self-hosted-environments-configuration#git-configuration-inside-lifecycle-hooks)
- [Customize sessions in self-hosted environments - Claude Code Docs (English)](https://code.claude.com/docs/en/self-hosted-environments-configuration#git-configuration-inside-lifecycle-hooks)

## 6. Plugin manifest reference

- **「Directory listing fields」**: `icon`・`documentationUrl`・`supportUrl`・`privacyPolicyUrl`・`termsOfServiceUrl` は、Anthropic のディレクトリにプラグインを提出したときの掲載情報に使われ、Claude Code は読みません。`plugin.json` にだけ書き、マーケットプレイスのエントリに書くと `claude plugin validate` が不明なフィールドとして報告します。v2.1.281 より前の `validate` は警告を出すので、`--strict` では失敗します
- **予約された名前**: `claude plugin validate` は、名前が Anthropic のプラグインのように見えないかを確かめます。`claude-`・`anthropic-`・`anthropics-`・`cc-plugin-` で始まる名前や、`claude`・`claude-code`・`claude-mods` などはエラー、`mcp-for-claude` のように単語として含むものは警告です。`claude plugin init` と `claude plugin tag` はエラーの名前を断りますが、インストールと読み込みはできます
- **フィールドの表**: mod の `$.state` と `$` の名前を宣言する `.d.ts` を指す `types` が加わりました
- **`hooks`**: フックのファイルはイベントの定義を最上位の `"hooks"` キーで包む必要があり、包まないファイルは読み込みに失敗する、と例付きで明記されました
- **`experimental.evals`**: コンポーネントのパスではないのでパスの規則は適用されず、`claude plugin eval` の実行時に値を確かめる、と加わりました

- [プラグインマニフェストリファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/plugins/manifest-reference#name)
- [Plugin manifest reference - Claude Code Docs (English)](https://code.claude.com/docs/en/plugins/manifest-reference#name)

## 軽微な更新

<!-- light:minor-updates:start -->
今回の差分は **3 ファイル**です。`llms-full.txt` をページ単位に切り出して数えると、220 ページ中 **92 ページ**（新規 10 ページを含む）が変わり、変更は 5,680 行（追加 5,180・削除 500）でした。大幅更新の 6 ページと新規の 10 ページを除く **76 ページ**（changelog を含む）と、changelog に加わった **v2.1.287**（2026年10月01日、106 項目。Added 9・Fixed 67・Improved 20・Changed 10）を以下にまとめます。changelog 由来の項目はすべて v2.1.287 のものです。`llms-full.txt` の総行数は **106,132 行から 110,852 行へ 4,720 行増え**ました。

**新機能**

- **Claude Mods を追加**（詳細はハイライト 1 参照）
- **組み込みの mod「You should know」を追加**（詳細はハイライト 1 参照）
- **エージェントビューに `n:<text>` フィルターを追加**（詳細はハイライト 4 参照）
- **OpenTelemetry の `user_prompt` イベントに `prompt_text` を追加**。ドット区切りのキーを入れ子にするバックエンド向けの `prompt` の写しで、`prompt` を落とす・伏せる場所では同じように扱います
- **2025-11-25 版のプロトコルの MCP サーバーからの URL のプロンプト（サインインなど）に対応**。更新後にサーバーがつながらなくなった場合は、MCP の設定のエントリに `"bareElicitationCapability": true` を加えます
- **[Windows] Bash ツールを拒否すると PowerShell ツールも止まり、シェルのツールがなくなる場合に、起動時に警告を出すようにした**
- **[セルフホストのランナー] Anthropic が管理する git を使うセッション向けに、GitHub CLI のない macOS と Linux のマシンで、組み込みの `gh api`（REST のみ）を追加**
- **[VS Code] 実行中のコマンドとサブエージェントに「Run in background」を追加**。バックグラウンドに移して作業を続けられます — [日本語](https://code.claude.com/docs/ja/vs-code#move-a-running-command-or-subagent-to-the-background) / [English](https://code.claude.com/docs/en/vs-code#move-a-running-command-or-subagent-to-the-background)
- **[VS Code] エージェントマップのカードに、バックグラウンドのシェルと Monitor の出力を表示**
- **Python Agent SDK の `ClaudeSDKClient` に `get_context_usage()` と、その戻り値の型 `ContextUsageResponse` が載った**。`/context` と同じ内容で、メッセージのストリームに出ないトークン計数のリクエストを使います（Anthropic API では課金されません） — [日本語](https://code.claude.com/docs/ja/agent-sdk/python#contextusageresponse) / [English](https://code.claude.com/docs/en/agent-sdk/python#contextusageresponse)
- **mod のテストを実行する `claude plugin test [directory]` が載った**。`.test.ts`・`.test.tsx` のファイルを実行し、失敗すると終了ステータス 1 で終わります — [日本語](https://code.claude.com/docs/ja/plugins/cli-reference#plugin-test) / [English](https://code.claude.com/docs/en/plugins/cli-reference#plugin-test)
- **`/mcp reconnect all` が載った**。失敗したサーバーと認証待ちのサーバーをまとめて再試行します（対話型のターミナルでは v2.1.284 以降。前の版は `MCP server "all" not found` と表示） — [日本語](https://code.claude.com/docs/ja/mcp#retry-failed-servers-yourself) / [English](https://code.claude.com/docs/en/mcp#retry-failed-servers-yourself)
- **コマンドの一覧に `/plugin-authoring` が加わった**。mod を書くための組み込みのスキルで、v2.1.287 以降です
- **セッション開始時に `verify` か `simplify` という名前のスキルがあれば、コミットの直前（ドキュメントやテストだけの変更を除く）に実行するよう Claude に伝える、という「Run your checks before each commit」の節ができた**（v2.1.286 以降）。対象はエンタープライズ・個人・プロジェクト・追加ディレクトリのスキルと同名の `.claude/commands/` のファイルで、同梱の `/verify`・`/simplify`、プラグインのスキル、claude.ai のスキルは数えません — [日本語](https://code.claude.com/docs/ja/skills#run-your-checks-before-each-commit) / [English](https://code.claude.com/docs/en/skills#run-your-checks-before-each-commit)
- **管理画面の「Admin settings > GitHub」の一覧が「Connected GitHub accounts」として載った**。Claude Code・Claude Tag・Claude Security で共有され、**Unlink from this workspace** で外せます。Enterprise プランの Compliance API の活動の種類 `github_app_installation_linked`・`github_app_installation_unlinked` も記載されています — [日本語](https://code.claude.com/docs/ja/admin-setup#connected-github-accounts) / [English](https://code.claude.com/docs/en/admin-setup#connected-github-accounts)
- **Claude Code が `gen_ai.usage.*` を設定しないことと、OpenTelemetry の GenAI の規約への対応づけが載った**。入力の合計は `input_tokens`・`cache_read_tokens`・`cache_creation_tokens` の和で、`input_tokens` はキャッシュの読み書きを含みません — [日本語](https://code.claude.com/docs/ja/monitoring-usage#map-input-tokens-to-opentelemetry-genai-semantic-conventions) / [English](https://code.claude.com/docs/en/monitoring-usage#map-input-tokens-to-opentelemetry-genai-semantic-conventions)
- **スクリーンリーダーがプロンプトに戻ってしまう場合の対処が載った**。端末のカーソルを追っているためで、NVDA では `NVDA+6` で切り替えます — [日本語](https://code.claude.com/docs/ja/accessibility#read-earlier-output-without-losing-your-place) / [English](https://code.claude.com/docs/en/accessibility#read-earlier-output-without-losing-your-place)
- **`claude auth status` の出力に `authMethod`（`none`・`claude.ai`・`oauth_token`・`api_key`・`api_key_helper`・`third_party`）が加わった**
- **Claude Desktop と claude.ai で MCP Apps などのウィジェットを表示するために、`*.claudemcpcontent.com` を許可するよう加わった**。ブロックしてもアプリは動きますが、ウィジェットは読み込まれません — [日本語](https://code.claude.com/docs/ja/network-config#desktop-and-claude-ai) / [English](https://code.claude.com/docs/en/network-config#desktop-and-claude-ai)

**機能改善**

- **`/config` を改善**。値を巡回する設定は ‹ › を表示して ←/→ で前後に動き、幅の狭い端末では値をラベルの下に置き、PgUp/PgDn で一覧をページ送りします
- **プラグインのマーケットプレイスのエラーが、無視・拒否した理由と対処を平易に説明するようにした**（詳細は大幅更新 4 参照）
- **プラグインの一覧で依存関係がインストールされなかったことを示し、プラグインの更新で、終わらなかったインストールを再試行するようにした**
- **Amazon Bedrock がモデル ID を拒否したときの Claude apps ゲートウェイのエラーを改善**。開発者にはどのモデルが使えないかを示し、ゲートウェイのログには送った ID を記録します
- **SDK のセッションで、優先度「now」で送ったメッセージが実行中の Web 取得や Web 検索を取り消さず、バックグラウンドで続けるようにした**
- **`/memory` で、Auto-memory などのオン・オフを ←/→ で切り替えられるようにした**
- **メッセージの途中で打った `/skill` の名前が、`disable-model-invocation` のものも含め、スキルだと Claude に伝わるようにした**
- **ライトテーマでの入力欄の枠と、過去のメッセージの前の ❯ のコントラストを改善**
- **クラウドセッションと Remote Control から Claude が送るファイルの配信を改善**。タイムアウト・ネットワークエラー・502/503/504 で失敗したアップロードを 1 回再試行します
- **一時的かもしれない理由でファイルを送れなかったとき、数分後にもう一度頼めると Claude が伝えるようにした**
- **別のセッションから保留されたメッセージの確認で、メッセージを破線の間に表示するようにした**
- **MCP などのツールの権限の確認で、ツール呼び出しを破線の間に表示するようにした**
- **ヘッドレスモードで、最初の接続が一時的に失敗したリモートのサーバーを、最も遅いサーバーの接続を待たずに再試行するようにした**
- **リモートのセッションから送る大きなファイルを、メモリーに読み込まずディスクからストリームし、上限を超えるファイルはサーバーの上限を示して断るようにした**
- **Remote Control やクラウドセッションから送ったファイルをサーバーが断ったとき（大きすぎる画像など）の説明を改善**
- **大きな MCP のツールの結果の扱いを改善**。メモリーとセッションのファイルが小さくなり、上限を大きく超える結果でトークンを数えるための余分なアップロードをしません
- **[Windows] 毎回のコマンドの前に動いていたサブシェルをなくし、Bash ツールを速くした**
- **[VS Code] Manage plugins で、マーケットプレイスの追加・削除・更新に失敗したときに理由を示すようにした**
- **[Claude Tag] 長い Slack のスレッドで、バックグラウンドの作業が Claude のタスクリストを新しいメッセージとして投稿し直さないようにした**
- **[Code Review] 会話がロックされたプルリクエストで、ロックのためにレビューできず、何も投稿・請求していないと失敗のカードに示すようにした**
- **ネットワーク上のストレージに Claude Code を置く場合の「Install on network storage」の節ができた**。実行中のセッションは実行ファイルをディスクから読むので、失うと `Bus error` になります。ローカルのディスクに置く、版ごとにディレクトリを分ける、`DISABLE_UPDATES` を設定する（`DISABLE_AUTOUPDATER` だけでは足りない）などを勧めています。`troubleshoot-install` にも「Bus error while a session is running」が加わりました — [日本語](https://code.claude.com/docs/ja/setup#install-on-network-storage) / [English](https://code.claude.com/docs/en/setup#install-on-network-storage)
- **Linux のデスクトップアプリで、サインインが保存されない場合のキーリングの対処が載った** — [日本語](https://code.claude.com/docs/ja/desktop-linux#your-sign-in-won’t-be-saved-on-this-device) / [English](https://code.claude.com/docs/en/desktop-linux#your-sign-in-won’t-be-saved-on-this-device)
- **bare モードで、MCP をコマンドラインで指定したサーバーだけにし、システムリマインダーを送らず、バックグラウンドのタスクを始めない、と明記された**（v2.1.286 より前は一部だけ）。タイムアウトしたコマンドはバックグラウンドに移らず止まります — [日本語](https://code.claude.com/docs/ja/headless#start-faster-with-bare-mode) / [English](https://code.claude.com/docs/en/headless#start-faster-with-bare-mode)
- **GitHub なしでローカルのリポジトリをクラウドセッションに送る場合の条件が加わった**。macOS・Linux・WSL では git 2.31 以降が必要で、サブモジュールや `--separate-git-dir` などの構成では `Not uploading this working tree:` で断られます。Git LFS などのフィルターで管理するファイルの未コミットの変更も送りません — [日本語](https://code.claude.com/docs/ja/claude-code-on-the-web#send-local-repositories-without-github) / [English](https://code.claude.com/docs/en/claude-code-on-the-web#send-local-repositories-without-github)
- **`tool.check` を扱う mod が上書きできる権限の確認が一覧になった**（`ask` ルール、管理設定以外の `PreToolUse` フックの拒否、auto モードの分類器、条件付きで `deny` ルール）。`.claudeignore` は効かないので `Read` の拒否ルールに移す、とも加わりました — [日本語](https://code.claude.com/docs/ja/permissions#extend-permissions-with-hooks) / [English](https://code.claude.com/docs/en/permissions#extend-permissions-with-hooks)
- **プラグインの依存関係のインストールの制限が載った**。lockfile で版を固定したレジストリのパッケージだけ、ダウンロードは `https` だけ（インストールするユーザー自身の既定の npm レジストリを除く）で、別のフォルダーにインストールするため `.npmrc`・`.env`・`bunfig.toml` を読みません。lockfile の扱いも改められました — [日本語](https://code.claude.com/docs/ja/plugins/loading#limits-on-the-dependency-install) / [English](https://code.claude.com/docs/en/plugins/loading#limits-on-the-dependency-install)
- **マーケットプレイスの `npm` ソースで、`package` に書ける値と断られる値が明記された**（git・フォルダー・`file:`・github.com などの tarball・`http` の tarball は不可。`registry` は `https`） — [日本語](https://code.claude.com/docs/ja/plugins/marketplace-reference#npm-plugin-source) / [English](https://code.claude.com/docs/en/plugins/marketplace-reference#npm-plugin-source)
- **`CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS` が外すものと残すものが一覧になった**。`output_config.format` も外します（v2.1.287 以降）。changelog の「セッションのタイトルとプロンプトのフックのリクエストから構造化出力の形式が外れなかった」修正に対応します — [日本語](https://code.claude.com/docs/ja/llm-gateway-protocol#disable-pre-release-capabilities) / [English](https://code.claude.com/docs/en/llm-gateway-protocol#disable-pre-release-capabilities)
- **使用量の上限で待機しているときの表示が 2 行になった**（`Usage limit reached · limit resets 3:45pm` と `Continuing automatically at 3:45pm · esc to cancel`） — [日本語](https://code.claude.com/docs/ja/interactive-mode#wait-for-a-usage-limit-to-reset) / [English](https://code.claude.com/docs/en/interactive-mode#wait-for-a-usage-limit-to-reset)
- **Explore サブエージェントのモデルの説明が改められた**。メインの会話が Fable の場合、サブスクリプション・Console・ゲートウェイでは Opus で、Bedrock・Agent Platform・Foundry などでは Fable のまま動きます（`feature-availability` も同様） — [日本語](https://code.claude.com/docs/ja/sub-agents#built-in-subagents) / [English](https://code.claude.com/docs/en/sub-agents#built-in-subagents)
- **claude.ai のアーティファクトを読む前に承認を求める場合が一覧になった**（ネットワークが None のクラウドセッション、別の組織の公開アーティファクトなど）。`bypassPermissions` モードでは別の組織の公開アーティファクトを読めません — [日本語](https://code.claude.com/docs/ja/artifacts#read-an-artifact-shared-with-you) / [English](https://code.claude.com/docs/en/artifacts#read-an-artifact-shared-with-you)
- **スキルの `allowed-tools` が、`allowManagedPermissionRulesOnly` のもとでは無視されることが「When only managed permission rules apply」としてまとまった**（v2.1.282 以降）。`/status` に対象のスキルが表示されます — [日本語](https://code.claude.com/docs/ja/skills#when-only-managed-permission-rules-apply) / [English](https://code.claude.com/docs/en/skills#when-only-managed-permission-rules-apply)
- **システムプロンプトのフラグを、そのファイル形式と組み合わせられると明記された**（v2.1.283 以降。ファイルの内容が先） — [日本語](https://code.claude.com/docs/ja/cli-reference#system-prompt-flags) / [English](https://code.claude.com/docs/en/cli-reference#system-prompt-flags)
- **組織が Remote Control をオフにすると、接続中のセッションも約 1 時間ごとのポリシーの更新で切断されることが載った**（v2.1.286 以降。`managed-settings` にも追記） — [日本語](https://code.claude.com/docs/ja/remote-control#remote-control-was-turned-off-by-your-organizations-policy) / [English](https://code.claude.com/docs/en/remote-control#remote-control-was-turned-off-by-your-organizations-policy)
- **「Update one plugin now」が「Update plugins now」になった**。すべてを更新するコマンドはなく、マーケットプレイスの **Update marketplace** でそこから入れたプラグインを更新できる、と加わりました — [日本語](https://code.claude.com/docs/ja/plugins/install#update-plugins-now) / [English](https://code.claude.com/docs/en/plugins/install#update-plugins-now)
- **サーバー側の分類器のレビューが、`-p`・Agent SDK・VS Code・デスクトップのセッションにも及ぶと明記された**（v2.1.281 以降）。Fable のセッションで分類器が使う Opus は、Anthropic API 以外のプロバイダーでは `ANTHROPIC_DEFAULT_OPUS_MODEL` のモデル、未設定なら Opus 5 です（`model-config` も同様）
- **TypeScript Agent SDK で、`getContextUsage()` の `detail` の説明が分かれ、`apiUsage` は累計ではなく最新の応答の使用量だと明記された**。auto モード（v2.1.271 以降）では、fork でないサブエージェントの結果が `SubagentHandback` の短い注記になる場合も加わりました
- **Python・TypeScript の `SdkBeta` の警告が、Claude API では `context-1m-2025-08-07` が Sonnet 4.5・Sonnet 4 で廃止済みなので `betas` から外す、1M が要るなら既定で 1M のモデルか `[1m]` 付きのモデルを使う、と書き改められた**
- **VS Code で、別の場所で開いている会話を開くと「This conversation is still open somewhere else…」と表示されるようになった**。**Open here anyway** で開けます。プラグインのインストールリンクの検証規則も詳しくなりました
- **[ワークツリー・クラウドセッション] ベースブランチやプルリクエストの取得、テレポートの取得は入力を待たず、待つ必要があれば失敗として扱う、と明記された**。`.claude/worktrees/` のサブエージェントは、ワークツリーの `CLAUDE.md` を読まずメインの会話の指示ファイルを使います
- **別のマシンのセッションへのメッセージで、受け取れないセッションが `can't receive cross-session messages (off in that session)` と一覧に出ることが加わった**
- **チームメイトやサブエージェントを見ている間の `/compact`・`/clear`・`/rewind` は確認を求め、`/model`・`/fast` は実行されない、と改められた**（`agent-teams`・`sub-agents`）。サブエージェントを見ているときに `Ctrl+Enter` か `Ctrl+X Ctrl+S` でメッセージを早く読ませる操作も加わりました（v2.1.286 以降）

**バグ修正**

- エージェントが所有しユーザーアカウントのないリモートのセッションで、組織が許可していても fast mode がオフのままになる問題を修正
- 再接続の要求に応答がないと、Remote Control が数分間メッセージを受け取らない問題を修正。30 秒で諦めて再試行します
- `asyncRewake` を設定したフックのスクリプトがないと、「found issues」の通知で Claude を何度も起こす問題を修正。壊れたフックは 1 回だけ報告します
- モデルの応答のストリームが止まっている間、ツールのハートビートが SDK のホストに届かない問題を修正
- Bedrock と Vertex の起動時のモデルの確認が、強制した `availableModels` を無視し、`/model` が Opus の 1 行だけになることがある問題を修正
- Chrome に届かないとき、Claude in Chrome のブラウザーの選択で JSON の解析エラーが出る問題を修正
- claude.ai のログインで `/model` から Fable を選ぶと今の版の ID を保存してしまう問題を修正。Opus・Sonnet と同じく最新の Fable に追従します
- Opus 5.5 と Sonnet 5.5 を切り替えると（`/model`・`opusplan`）、前の MCP ツールの告知が書き換わり、前の拡張思考が落ちることがある問題を修正
- 応答が思考から始まった場合に、途中で届いた Amazon Bedrock のガードレールのブロックが、ガードレールのメッセージではなく API エラーでターンを終える問題を修正（`amazon-bedrock` にも、途中でブロックされた場合の説明を追記） — [English](https://code.claude.com/docs/en/amazon-bedrock#aws-guardrails)
- `/` やホームディレクトリへの危険な `rm` が、出力を `~` やワイルドカードのパスにリダイレクトすると、常に確認する保護を失う問題を修正
- 応答の途中でモデルを切り替えた後、`claude -p` と SDK のセッションが後のメッセージで毎回モデルのフォールバックを繰り返す問題を修正
- セッションの再開やコンパクションの後に、フォルダーの CLAUDE.md が 2 回目に添付される問題を修正
- エージェントが終了して開始時のワークツリーを消した後、バックグラウンドのセッションを `claude agents` から開き直せない問題を修正
- `/advisor` の組み合わせの確認を修正。Sonnet 5.5 が Opus 4.7・4.8 の advisor になれるようになり、API が断る advisor は黙って外さず先に示します
- Bash の権限の確認が「Contains simple\_expansion」のような内部のパーサー名を表示する問題を修正
- 遅い・忙しいマシンのフルスクリーンのセッションで、長い会話でスクロールキーを押し続けると「Claude Code exited after an unrecoverable interface error」で終了する原因の 1 つを修正
- `__proto__` という名前の MCP ツールで、組織のツールごとの権限の上限が黙って落ちる問題を修正
- JSON として保存した大きな MCP の結果を、1 行が長くて分けられないのに Read の offset と limit で読むよう Claude に伝えていた問題を修正
- コンパクションの後、コミットの帰属のリマインダーがツールの結果の中に入る問題を修正
- スクリーンリーダーモードで、検索欄（`/resume`・`/permissions` など）とサインインのコード欄で、カーソルが入力した文字から離れる問題を修正
- スクリーンリーダーモードで、`/rewind` の要約の選択肢で何も入力せずに Enter を押すと断られる問題を修正（追加の文脈は任意）
- スクリーンリーダーモードで、Tab が何もしない承認の確認に「Tab to amend」のヒントが出る問題を修正
- スクリーンリーダーモードで、`/permissions` と `/mcp` で何もしない矢印キーを案内し、空のメニューや検索欄の入力中に「Select with numbers」と言う問題を修正
- スクリーンリーダーモードで、ファイル編集の承認などの差分の変更行が読まれない問題を修正（`accessibility` にも、差分を `+`・`-` 付きで 1 行ずつ読むと追記）
- スクリーンリーダーモードで、`claude --teleport` の進行画面と、確認中の MCP のフォームの欄を、スピナーのフレームごとに読み直す問題を修正
- `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS` が、セッションのタイトルとプロンプトのフックのリクエストから構造化出力の形式を外さず、Bedrock を背後に持つゲートウェイに断られる問題を修正
- スクリーンリーダーモードで、前の画面が端末より高いと、2 つ目の承認の確認・変わった `/config` の行・却下したプランの行の上の部分が読まれない問題を修正
- `--include-partial-messages` で、途中で切れた応答の `message_stop` が遅れるか届かず、アプリが応答を進行中と表示し続ける問題を修正
- `claude agents` が、バックグラウンドのセッションが待っている権限の確認を表示しないことがある問題を修正
- コミットされた `.gitattributes` を読めない（UTF-16 で保存したなど）ためにアップロードが止まったとき、`/ultrareview` が `.git/info/attributes` についての助言を出す問題を修正
- HTTP プロキシの背後で `claude remote-control` が「Check your organization permissions」という誤解を招くエラーで登録に失敗する問題を修正
- Linux でサンドボックスの Bash のコマンドが Claude Code の実行ファイルの開いたハンドルを引き継ぐ問題を修正
- 「Reduce motion」をオンにしても、実行中のツールの点と 3 つのスピナーが動き、`/rewind` の確認画面でメモの入力中に「ago」の時刻が更新される問題を修正
- スクリーンリーダーモードで `claude agents` の時刻が毎秒変わる問題を修正。最短 10 秒ごとにします
- 取り消された claude.ai のログインで、「OAuth token revoked」ではなく一般的な `API Error: 401` を表示する問題を修正。`-p` モードでは「Failed to authenticate」で始まります（詳細は大幅更新 3 参照）
- `/ultrareview` のアップロードの拒否が、リポジトリの設定ファイルが名指しする変数を自分のユーザー設定に写すよう勧める問題を修正
- プロンプトとして `/<skill>` と打って実行した `context: fork` のスキルのターンを、`--output-format stream-json` と SDK がストリームしない問題を修正
- `/feedback` と `/bug` で、あらかじめ記入した GitHub の Issue に最近のエラーメッセージを含めないようにし、確認画面に報告の一部として一覧するようにした
- 素の http で配信されるリポジトリで、`claude plugin marketplace add --sparse` と `git-subdir` のプラグインのインストールが「transport 'http' not allowed」で失敗する問題を修正
- コンパクション中にセッションが再起動すると、クラウドセッションが前の会話を失うことがある問題を修正
- 起動時の `--plugin-url` のダウンロードとプラグインの再読み込みが重なると、キャッシュしたアーカイブが壊れる問題を修正
- Claude Desktop を開くのがタイムアウトしたか出力が多すぎたとき、`/desktop` が出力の一部を引用する問題を修正。原因を示します
- サーバーが対応する MCP のプロトコルの版を変えたとき、MCP のコネクタのツール呼び出しがまれに 2 回実行されるか、再起動まで失敗する問題を修正
- 同期したプラグインの SessionStart フックが、新しいクラウドセッションで動かない問題を修正
- トランスクリプトの「N hooks ran」とデバッグログの一致したフックの数が、内部のコールバックを含めて数える問題を修正
- クラウドセッションと Remote Control から送るファイルが、30 秒のタイムアウトの直後にアップロードが終わると失敗する問題を修正。35 秒待ちます
- クラウドと SDK のセッションで途中に加えたリポジトリが、スキルとプラグインを読み込まず、CLAUDE.md を遅れて読み込む問題を修正
- 1 辺が 8,000 ピクセルを超える PNG・JPEG・WebP の画像をリモートのセッションから送れない問題を修正。縮小した写しを送ります
- Claude のアプリから 17〜20 個のファイルを添付して送ると、最初の 16 個しか届かない問題を修正
- ヘッドレスのセッションで、1 回断られただけで MCP サーバーを認証が必要と報告する問題を修正
- [macOS] `claude remote-control` で始めた Remote Control のセッションが、Mac のアイドルスリープでターンの途中に止まる問題を修正
- [Windows] 入力をパイプかリダイレクトすると、対話型の `claude` が「Raw mode is not supported」で止まるかクラッシュする問題を修正。理由を示して終了します（パイプの入力には `-p`）
- [Bedrock・Vertex・Mantle] `CLAUDE_CODE_SKIP_*_AUTH` のもとで、`ANTHROPIC_CUSTOM_HEADERS` が `Authorization` を繰り返していると、モデルの確認が本来のリクエストと違うヘッダーを送る問題を修正
- [VS Code] Claude Code の応答が大きすぎて保存を確かめられないとき、設定のダイアログがタイムアウトのせいにする問題を修正
- [VS Code] サイドバーが既にこのマシンに持ってきたクラウドセッションを開き直すと、新しいタブで開く問題を修正。サイドバーを表示します
- [VS Code] サイドバーの Web タブが、ウィンドウを読み込んだ後に始めたクラウドセッションを一覧しない問題を修正。読み込みに失敗すると「Remote server is not connected」と表示します
- [VS Code] 再読み込み後に復元したタブが、サイドバーで開いている会話に 2 つ目の Claude のプロセスを始める問題を修正。「still open somewhere else」の通知を出します
- [VS Code] ツールの行のファイルリンク、セッション一覧のリンク、2 つのヒントがプレーンテキストで表示される問題を修正
- [VS Code] メインのターンが終わると、バックグラウンドのエージェントの実行中のコマンドが失敗と表示される問題を修正
- [VS Code] コマンドメニューから選んだユーザー自身の `/usage` や `/context` のコマンドが、実行されずに拡張のダイアログを開く問題を修正
- [VS Code] プランのプレビューのタブのファイルリンクをクリックしても何も起きない問題を修正
- [VS Code] WSL などのリモートのホストで、ツールの入力や出力をエディターのタブで開くと「Timeout waiting after 1000ms」で失敗する問題を修正
- [クラウドセッション] GitHub が新しく発行したアクセストークンを一時的に断ると、GitHub からの取得や GitHub へのプッシュがときどき失敗する問題を修正
- [Claude Tag] GitHub の動きなどのバックグラウンドのイベントで起きたとき、誰も返信を待っていないのに Slack のスレッドに支出上限などの失敗の警告を投稿する問題を修正
- [Claude Tag] チャンネルの多い組織で、管理画面の支出上限のページに最近作ったチャンネルと非公開のチャンネルが出ない問題を修正
- [Code Review] 指摘のコメントと「Why this was flagged」の文が文の途中で切れる問題を修正
- [Code Review] 前のコミットでレビューが 2 回失敗したプルリクエストを、新しいプッシュの後に飛ばす問題を修正。最新のコミットをレビューします

**その他**

- **リポジトリにコミットされたシンボリックリンクを通じて機密のファイルや作業ツリーの外に書き込むシェルの書き込みは、書き込み先を示して人の判断を待つように変更**（`~` が対象の行も含む）
- **Bedrock・Vertex・Foundry・Claude apps ゲートウェイで、Opus 4.7 以降と Fable が `[1m]` を付けずに既定で 1M のコンテキストウィンドウを使うように変更**（`CLAUDE_CODE_DISABLE_1M_CONTEXT=1` で 200K のまま）
- **`claude agents` からの返信をキューのメッセージとして届けるように変更**。ターンの実行中に送った `/stop` 以外のスラッシュコマンドは、ターンの終わりに実行します（詳細はハイライト 4 参照）
- **ツール全体の `Bash` 許可ルールと許可するフックでも、Claude Code のファイルツールが断るファイル（Anthropic のプロファイルの保存先、ホストの資格情報ファイル）へのシェルの書き込みは、実行せず確認するように変更**
- **Windows と Linux の右クリックの貼り付けと、Linux の中クリックの貼り付けを、ボタンを離したときに行うように変更**。離す前にポインターを動かすと取り消します
- **MCP サーバーの `alwaysLoad: false` で、そのサーバーのすべてのツールをツール検索の後ろに回すように変更**
- **スクリーンリーダーモードで、新しい行・変わった行を、行頭にカーソルを置いて待たずに書くように変更**。`CLAUDE_AX_PREPARK_MS=50` で元に戻せます（`env-vars` でも既定が `0` になり、v2.1.287 より前は `50` と記載）
- **フラグの付いたメッセージの後の自動のモデル切り替えで、新しいモデルの既定ではなく今の effort を保つように変更** — [日本語](https://code.claude.com/docs/ja/model-config#effort-level-after-a-fallback) / [English](https://code.claude.com/docs/en/model-config#effort-level-after-a-fallback)
- **待っている権限の確認を古い順に表示するように変更**。新しい確認が読んでいる確認を覆いません（カウントダウンのあるものは上に開きます）
- **[VS Code] Claude in Chrome の「Enabled by default」で、エディター自身のセッションもつなぐように変更**。ブラウザーの操作の前には確認します
- **クラウド環境の GitHub プロキシの「Push protection」（今のブランチにだけプッシュ）が「Push restrictions」に変わった**。ブランチの削除とブランチ以外（タグ）のプッシュは断りますが、ブランチは限らないので、GitHub のブランチ保護かルールセットを使うよう案内しています（`routines`・`security` も同様） — [日本語](https://code.claude.com/docs/ja/cloud-environments#github-proxy) / [English](https://code.claude.com/docs/en/cloud-environments#github-proxy)
- **`claude -p '/code-review ultra'` は指摘を返さないので、スクリプトや CI では `claude ultrareview` を使う、と改められた**（`code-review`・`ultrareview`）
- **`security` のページが整理された**。権限の仕組みが auto モードと Manual モードの項目に分かれ、「Context-aware analysis」「Input sanitization」「Natural language descriptions」が消え、「Web page summaries」が加わりました
- **sandbox runtime のリポジトリの URL が `anthropic-experimental/sandbox-runtime` から `anthropics/sandbox-runtime` に変わった**（`agent-sdk/secure-deployment`・`sandbox-environments`）
- **組織の既定のモデルについて、「一部の組織だけが使える」という注記が消えた**（`admin-setup`・`model-config`）
- **mod に関する記述が多くのページに加わった**（`hooks`・`hooks-guide`・`plugins/overview`・`plugins/components` の `modules` キー・`plugins/security`・`plugins/org` の `allowManagedModsOnly`・`claude-directory` の `dev-mods/`・`permission-modes` の保護されたパスなど）
- **このほか、`agent-sdk/hooks` の `"defer"` の結果（`stop_reason` が `"tool_deferred"`）、`agent-sdk/streaming-vs-single-mode` の不正な画像ブロックの扱い、`self-hosted-environments` のリースの説明、`troubleshooting` のコンパクションの空回り、`debug-your-config` のフックの確認などで記述が改められた**。`channels`・`claude-security`・`large-codebases`・`plugins/code-intelligence` などのインストール手順は、VS Code 拡張とデスクトップアプリにも触れる形になりました
- **`llms.txt` では、`Mods reference` と `Test a mod` の説明の言い回しが改められ、言語別の索引のページ数が各言語 220 ページ（日本語は 219 ページ）に増えた**
- **`llms-full.txt` では、`amazon-bedrock`・`google-vertex-ai`・`microsoft-foundry` など 10 ページと、`whats-new/` の 10 ページの並び順が変わった**。このため `git diff` をファイル全体にかけると 62,674 行（追加 33,697・削除 28,977）と大きく出ますが、本サマリの行数はすべてページ単位で数えたものです
- **前回までに見出しマップにだけ先に載っていた見出しの多くが本文に入りました**（Mods の 180 見出し、`sandboxing` の新しい見出し、`settings-reference` の `prependPlugins`・`appendPlugins`、`errors` の 2 見出し、`skills` の「Run your checks before each commit」、`vs-code` の 2 見出し、`self-hosted-environments-configuration` の 2 見出し、`plugins/troubleshooting` の 2 見出し、`plugins/install` の「Update plugins now」）
- **見出しマップには今回も、本文にまだない見出しが先に載りました**（追加 33・削除 2 見出しのうち、本文にないものが 30）。`errors` の「Advisor is less capable than the current main model」「Output blocked by content filtering policy」など 8 見出し、`claude-apps-gateway-config` の「Certificate client authentication」「Extended context in Claude Desktop」など 5 見出し、`claude-apps-gateway-deploy` の 2 見出し、`plugins/cli-reference` の `plugin update` の 3 見出し、`self-hosted-environments-configuration` の「Send model requests to Bedrock or Agent Platform」など 2 見出し、`sessions` の「Resume a running background session」、`statusline` の「Spend limit fields」、TypeScript SDK の `toggleMcpServer()` などです。`interactive-mode` の「Diff viewer」は、マップでは「Diff dialog」に変わりました（本文は「Diff viewer」のまま）
- **見出しマップ冒頭の自動生成スタンプが、2026年10月02日 05時05分46秒 UTC から 2026年10月03日 00時40分44秒 UTC へ進みました**

**参考リンクについて**: 日本語版は各ページを実測して、該当の記述が反映されていたものだけにリンクを付けています。**`amazon-bedrock` のガードレールについての記述は日本語版を確かめていないため、その項目は英語版だけにしています。** それ以外のリンク先のページは、日本語版も今回の内容に更新されていました。見出しマップにだけある見出しは、本文に節がないためリンクを付けていません。 **changelog ページへのリンクは、本サマリの方針どおり付けていません。**
<!-- light:minor-updates:end -->

## 新着情報

<!-- light:whats-new:start -->
**今回、`whats-new/` 配下のページの内容に変更はありません**（`llms-full.txt` の中で 10 ページの位置が末尾へ移っただけです）。
<!-- light:whats-new:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-10-01.md](./archives/latest/2026-10-01.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-10-01.md](./archives/latest-detail/2026-10-01.md)

<!--
base_commit: 9b8bb3ebf069837e81d6fe60dc072847b234733f
head_commit: f1380431c4bc062901668fe07773b6af5b247d50
generated_at_full: 2026-10-03T15:00:26+09:00
-->
