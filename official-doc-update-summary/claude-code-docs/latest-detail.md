---
対象期間: 2026年11月25日 〜 2026年11月27日
作成日: 2026-11-27
---

# Claude Code 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
**今回は、Desktop アプリの管理者向けの記述が増えました。SSH とローカルセッションを制限する 3 つのキーは、サーバー管理設定（server-managed settings）と各コンピューターの管理設定の両方に置く、という節ができました。管理設定の `model` で、新しいセッションが始まるモデルを決める節も加わりました**。変わったのは `desktop`・`settings-reference`・`model-config` の 3 ページです。このうち `desktop` は 78 行（追加 62・削除 16）が変わった大幅更新です。changelog への追加、新規ページ、新着情報のページはなく、`llms.txt` も変わっていません（URL は 221 のまま）。`llms-full.txt` の生の差分は追加 75・削除 25 で、総行数は 137,484 行から 137,534 行になりました。

主要なものを以下に挙げます。

1. Claude Desktop v3.1623.0 以降は、`sshHostAllowlist`・`disableDesktopLocalSessions`・`disableSshSavedPasswords` を、サーバー管理設定と、コンピューター上の Claude Code の MDM ポリシーか管理設定ファイルの両方から読む。両方に同じ値を置き、コンピューター側は Desktop 自身のデバイス管理ポリシーではなく Claude Code のものに置く
2. Desktop の管理設定の表に `model` が加わり、モデルピッカーの **Set by admin** の意味と、開始時のモデルの設定をやめる手順が載った。`model-config` では、組織のデフォルトの上書きが有効でも `--model` などのモデルで始まるのは「ターミナルでは」と限定された
3. Linux か macOS のリモートマシンでは、Claude Desktop v6.6395.0 以降なら、フォルダーの制限があっても Desktop の切断中にファイルの読み取り・検索・編集を続けられる。新しいワークフローも、条件を満たせば前もって承認しておくことで切断中に始められる
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**Desktop の SSH とローカルセッションの 3 つのキーをサーバー管理設定とコンピューターの両方に置くようになった**](#1-desktop-の-ssh-とローカルセッションの-3-つのキーをサーバー管理設定とコンピューターの両方に置くようになった):  
  `desktop` に h4「Keys that apply from server-managed settings and managed settings on a computer」と、その下の h5「Which SSH host allowlists apply」ができました。Claude Desktop v3.1623.0 以降が `sshHostAllowlist`・`disableDesktopLocalSessions`・`disableSshSavedPasswords` を両方から読むこと、どちらの値が効くか、なぜ同じ許可リストを両方に置くのかが載っています。`settings-reference` の 2 つのキーの説明と、`policyHelper` の h4「Keys that only Claude Desktop uses」もこれに合わせて改められました
2. [**管理設定の model で Desktop の新しいセッションが始まるモデルを決められることが載った**](#2-管理設定の-model-で-desktop-の新しいセッションが始まるモデルを決められることが載った):  
  `desktop` の管理設定の表に `model` の行が加わり、h4「Set the model that new sessions start on」ができました。モデルピッカーの **Set by admin** の意味、設定をやめる 3 つの手順、組織のデフォルトモデルが上書きする場合の扱いが載っています。`model-config` の「Organization default model」も、`--model` などのモデルで始まるのは「ターミナルでは」と書き直されました
3. [**Desktop の切断中も SSH のタスクでファイルの操作とワークフローを続けられる条件が載った**](#3-desktop-の切断中も-ssh-のタスクでファイルの操作とワークフローを続けられる条件が載った):  
  `desktop` の「Limits while Desktop is disconnected」で、フォルダーの制限があっても、Linux か macOS のリモートマシンで Claude Desktop v6.6395.0 以降ならファイルの読み取り・検索・編集を続けられる、となりました。新しいワークフローを切断中に始めるための事前の承認の手順と、それを試す「Test file work and workflows」も加わっています。Windows のリモートマシンでの MCP サーバーの扱いも v6.6395.0 に合わせて書き直されました
<!-- light:highlight-list:end -->

## 1. Desktop の SSH とローカルセッションの 3 つのキーをサーバー管理設定とコンピューターの両方に置くようになった

**`desktop` の「Managed settings」の下に、h4「Keys that apply from server-managed settings and managed settings on a computer」と、h5「Which SSH host allowlists apply」ができました。** 以前の「Restrict which SSH hosts users can connect to」の警告は、サーバー管理設定を配るなら `sshHostAllowlist` はそこに置くこと、という内容でした。Desktop は既定ではポリシーのキーを配る最上位の管理ソースからしかこのキーを読まず、そこで未設定なら下位の MDM ポリシーや管理設定ファイルの一覧は無視して未設定として扱う、とありました。さらに、Desktop は起動時にサーバー管理設定を取得してキャッシュを持たないので、取得に成功するまではマシン上の一覧が効く、という理由で、同じ一覧を各マシンにも置くよう求めていました。今は、両方に置く理由を新しい節で説明する形になっています。

- **読む場所**: Claude Desktop v3.1623.0 以降は、表の 3 つのキーを、サーバー管理設定と、コンピューター上の Claude Code の MDM ポリシーか管理設定ファイルの両方から読みます。MDM ポリシーを使うなら Claude Code のもの（macOS では `com.anthropic.claudecode` ドメイン、Windows では `HKLM\SOFTWARE\Policies\ClaudeCode`）に置き、Desktop 自身のデバイス管理ポリシーには置きません。Claude アカウントでサインインしないサードパーティのプロバイダーの利用者には、claude.com の「SSH remote sessions in Claude Desktop on 3P」を案内しています
- **どの値が効くか**（表）: `sshHostAllowlist` は、設定した一覧のそれぞれにホストが一致しなければなりません（例外は h5 に記載）。緩めるには、設定した一覧のそれぞれにホストを足します。`disableDesktopLocalSessions` と `disableSshSavedPasswords` は、コンピューター上の `true`、または Desktop が取得した後のサーバー管理設定の `true` で、もう一方が `false` でも機能がオフになります。緩めるには、`true` を置いたすべての場所から外します
- **注意の 3 点**: 1 台のコンピューターに Claude Code の MDM ポリシーと管理設定ファイルの両方がある場合は、ポリシーに置きます。ポリシーが何かのポリシーキーを設定していると、Desktop は既定でファイルにあるこれらのキーを無視するためです。v3.1623.0 より前の版では、各キーをサーバー管理設定にも置きます。既定では、Desktop が取得した後はそちらの値だけが効きます。2 つの `disable` のキーは、Desktop が片方のソースしか持たない間も効くよう、サーバー管理設定と各コンピューターの両方で `true` にします
- **h5「Which SSH host allowlists apply」**: サーバー管理設定と各コンピューターに同じ一覧を置くよう求めています。両方の一覧に縛られない場面として、次の 3 つを挙げています。起動のたびに、Desktop がサーバー管理設定を取得するまでの間（コンピューターに一覧がないと、どのホストも許しうる。v4.16336.0 以降は、30 日未満の以前の取得で得たサーバー管理設定の一覧のコピーとも照合するが、利用者が消したり書き換えたりできるので頼らない）。利用者が別の組織か個人のアカウントにサインインしたとき（サーバー管理設定の一覧が届かない）。最上位のソースで `managedSourcesBehavior` を `"merge"` にしたとき（Desktop が両方の一覧を合わせ、片方にしかないホストも許しうる）。空の配列は、どのホストにも一致しない一覧として扱われ、何も制限しない未設定とは違います。SSH セッションをオフにするには、すべてのソースに空の配列を置きます

同じページのほかの箇所も、この節に合わせて改められました。「Turn off local sessions and distribute SSH connections」は、3 つのキーを最上位の管理ソース 1 つに置き、サーバー管理設定を配るならコンピューターにもコピーを置く、という説明でした。今は、サーバー管理設定を配るならそこと各コンピューター（Claude Code の MDM ポリシーか、それがなければ管理設定ファイル）に置き、配らないなら最上位の管理ソースに置く、となりました。「Managed settings」の表の `sshHostAllowlist`・`disableDesktopLocalSessions`・`disableSshSavedPasswords` の行にも、サーバー管理設定を使うなら両方に置く、と加わりました。SSH セッションに届く管理設定の項目は、複数の管理ソースを配る場合、`sshConfigs` は `settings-reference` のその項目を、残りの 3 つは新しい h4 を見る、という案内になりました。

`settings-reference` も同じ方向で書き直されました。`disableDesktopLocalSessions` と `sshHostAllowlist` の Scope は、サーバー管理設定を配るならそこと各コンピューターに置く、となりました。`disableDesktopLocalSessions` の `false` には「もう一方の場所の `true` がローカルセッションをオフにしうる」と加わっています。`sshHostAllowlist` には、Desktop はこのキーをポリシーヘルパーからは読まない、と加わりました。既定値にも、サードパーティのプロバイダーでは SSH セッションは既定でオフ、と加わっています。`policyHelper` の下には h4「Keys that only Claude Desktop uses」ができました。Desktop は自分だけが使うキー（`sshHostAllowlist`・`disableDesktopLocalSessions` など）をヘルパーを走らせずに読むので、ヘルパーだけが出すキーは未設定として扱います。こうしたキーは、ヘルパーを指定している MDM ポリシーか管理設定ファイルに置きます。

- [Desktop application - Claude Code Docs (English)](https://code.claude.com/docs/en/desktop#keys-that-apply-from-server-managed-settings-and-managed-settings-on-a-computer)
- [All settings - Claude Code Docs (English)](https://code.claude.com/docs/en/settings-reference#keys-that-only-claude-desktop-uses)

## 2. 管理設定の model で Desktop の新しいセッションが始まるモデルを決められることが載った

**`desktop` の「Managed settings」の表に `model` の行（新しいローカルセッションが始まるモデルの ID を設定する）が加わり、h4「Set the model that new sessions start on」ができました。**

- **Set by admin**: モデルピッカーのモデルの横にこの表示があれば、管理設定がそのモデルを `model` に設定しています。表示があるとき、新しいローカルセッションの開始時には、利用者が選べる限り、利用者が最後に選んだモデルよりそのモデルが優先されます。利用者はセッションごとに別のモデルを選べます
- **設定をやめる手順**: 1）利用者のコンピューターで **Settings > Code** か **Settings > Claude Code** を開き、**Starting values from your organization** の下で、どの管理ソースが効いているかを確かめる。2）`model` を設定しているすべての管理ソースから外し、利用者に Desktop を再起動してもらう。3）利用者に、使う各フォルダーで、セッションの最初のメッセージを送る前にモデルを選んでもらう。それまでは、新しいセッションが外したモデルで始まることがあります
- **組織のデフォルトモデルとの関係**: 組織のデフォルトモデルが利用者の選択を上書きする設定なら、これらのセッションは、利用者が選べる限りそのデフォルトで始まります。ターミナルでは `model` が優先されるのとは違います。利用者に選ばせるには、**Organization settings > Models** と、独自のデフォルトを持つ各カスタムロールで、**Always start with the default model and effort level** もオフにします

`model-config` の「Organization default model」では、上書きが有効でも `--model` フラグ・`ANTHROPIC_MODEL`・管理設定・`--settings` が「なお優先される」という文が、「ターミナルでは、上書きが有効でも、新しいセッションはそれらが設定するモデルで始まる」になりました（末尾の「instead」も外れています）。`model-config` は `llms-full.txt` に 2 回載っており、同じ 1 行の変更が 2 か所に出ています。`desktop` の「Shared configuration」の Models の項目からは、Desktop と CLI で同じモデルが使える、という文が外れ、Desktop でのモデルの選び方だけになりました。

- [デスクトップアプリ - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/desktop#set-the-model-that-new-sessions-start-on)
- [Desktop application - Claude Code Docs (English)](https://code.claude.com/docs/en/desktop#set-the-model-that-new-sessions-start-on)
- [モデル設定 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/model-config#organization-default-model)
- [Model configuration - Claude Code Docs (English)](https://code.claude.com/docs/en/model-config#organization-default-model)

## 3. Desktop の切断中も SSH のタスクでファイルの操作とワークフローを続けられる条件が載った

**`desktop` の「Keep a task running while Desktop is disconnected」の下の h5「Limits while Desktop is disconnected」で、切断中に失敗しうるものの説明が書き直されました。**

- **Folder restrictions**: 組織がセッションで使えるフォルダーを制限していると、Desktop はファイルの読み取り・検索・編集をそれぞれ確認します。以前は、切断中はそれぞれ最大 10 分待って失敗する、とだけありました。今は、Linux か macOS のリモートマシンで Claude Desktop v6.6395.0 以降なら、3 つとも切断中に続けられます。タスクのファイルはセッションのワークツリー（ワークツリーがなければセッションのフォルダー）に置き、リモートマシンで試してから使います。Windows のリモートマシンか、それより前の版では、Desktop を接続したままにします
- **Workflows**: 切断中に新しいワークフローが最大 10 分待って失敗する、という説明はそのままです。フォルダーの制限があるとき、企業ランチャー（corporate launcher）を通すとき、Claude Desktop v5.11492.0 より前のときは、切断中に新しいワークフローを始められない、と加わりました。それ以外なら、長いタスクの前にワークフローを承認しておきます。リモートマシンのセッションで Claude にワークフローを頼み、Desktop が尋ねたら承認します。承認はその後に開いたセッションでしか効かないので、長いタスクは新しいセッションで始めます。そのセッションでは、Auto のようにワークフローのたびに尋ねない権限モードを選び、先にリモートマシンで試します
- **ワークツリーの編集が続くとき**（アコーディオン）: 編集が失敗する場合のうち、フォルダーの制限は「Claude Desktop が v6.6395.0 より前のとき」に限られ、Desktop を更新するよう書かれました

h5「Prepare a long task」には「Test file work and workflows」の項目が加わりました。長いタスクでファイルの操作かワークフローが要るなら、数分後にファイルを編集するかワークフローを始める短いタスクを走らせ、その前に Desktop を終了します。20 分以上たってからセッションを開き、読み取り・検索・編集・ワークフローのどれかが失敗していたら、長いタスクの間は Desktop を接続したままにします。

h4「Windows remote machines」の MCP サーバーの項目は「MCP servers while disconnected」になりました。以前は、一部の Windows のリモートマシンでは `claude_desktop_config.json` の MCP サーバーの呼び出しが Desktop を通るので切断中は使えず、Claude Desktop v2.37337.0 より前はすべての Windows のリモートマシンがそうだ、という説明でした。今は、切断中にコンピューターの `claude_desktop_config.json` の MCP サーバーを使うには、Claude Desktop v6.6395.0 以降で OpenSSH クライアントを通して接続し、そうでなければタスクがそれらのサーバーを使う間は Desktop を接続したままにする、となりました。

- [Desktop application - Claude Code Docs (English)](https://code.claude.com/docs/en/desktop#keep-a-task-running-while-desktop-is-disconnected)
- [Desktop application - Claude Code Docs (English)](https://code.claude.com/docs/en/desktop#windows-remote-machines)

## 新規追加されたページ

<!-- light:new-pages:start -->
（今回の対象期間に新規追加されたドキュメントページはありません。`llms.txt` は変わっておらず、URL は 221 のままです。`llms-full.txt` の `Source:` の行も 226、固有のページも 221 のままです）
<!-- light:new-pages:end -->

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
- [**Desktop application**](#1-desktop-application) ([English](https://code.claude.com/docs/en/desktop#keys-that-apply-from-server-managed-settings-and-managed-settings-on-a-computer)):  
  78 行（追加 62・削除 16）が変わりました。管理設定の 2 つの h4 と 1 つの h5 が加わり（詳細はハイライト 1・2 参照）、切断中のタスクの制限（ハイライト 3）と、SSH の接続のタイムアウトの再試行の条件が書き直されました
<!-- light:updated-pages:end -->

**行数の数え方**: `llms-full.txt` の生の差分のハンクを、追加行は head 側、削除行は base 側の `Source:` 行でページに振り分けた値です。ページの並びは変わっていません。大幅更新の 1 ページに次いで多いのは `settings-reference` の 18 行（追加 11・削除 7）、`model-config` の 4 行（追加 2・削除 2）で、どちらも 50 行に届きません。

## 1. Desktop application

**`desktop` は 78 行（追加 62・削除 16）が変わり、`llms-full.txt` の中のページは 2,519 行から 2,565 行になりました。** 見出しは h4「Keys that apply from server-managed settings and managed settings on a computer」・h5「Which SSH host allowlists apply」・h4「Set the model that new sessions start on」の 3 つが加わり、外れたものはありません。`llms.txt` の説明文は変わっていません。

- **「Managed settings」**: 2 つの h4 と 1 つの h5、表の `model` の行、表の 3 つのキーの行への追記、SSH セッションに届く管理設定の項目の書き直し（詳細はハイライト 1・2 参照）。SSH セッションの項目にあった、ローカルの管理設定で `permissions.disableBypassPermissionsMode` か `disableAutoMode` を設定するとリモートホストの設定にかかわらずそのモードがモードセレクターに出ない、という文は、下の段落へ移りました（内容は変わっていません）
- **「Restrict which SSH hosts users can connect to」と「Turn off local sessions and distribute SSH connections」**: サーバー管理設定とコンピューターの両方に置く、という説明に書き直されました（詳細はハイライト 1 参照）
- **「Limits while Desktop is disconnected」「Prepare a long task」「Windows remote machines」**: フォルダーの制限・ワークフロー・MCP サーバーの扱い（詳細はハイライト 3 参照）
- **「Raise the SSH connection timeout」**（h4「Use your SSH configuration」の下の h5）: `ConnectTimeout` を設定していないときの表が書き直されました。以前の 1 行目は、macOS か Linux の Claude Desktop v4.4212.0 以降でジャンプホストか `ProxyCommand` を通してセッションを始めるとき、30 秒の後に 90 秒の 2 回目がある、というものでした。そこでは、Desktop が `ProxyJump` のホストに出すログインのプロンプトの時間は数えない、とされていました。今は、新しいセッション・メッセージ・リトライで自分から始めるジャンプホストか `ProxyCommand` を通した接続なら 30 秒で、表の下の版なら、時間切れの後に 90 秒でもう 1 回試せます。最初の試行でプロンプトが出ていれば 2 回目はなく、経路の待ち時間はすべて数えます。それ以外の接続と、Desktop が自分で始める再接続は「30 秒と見込む」になりました。表の下には、90 秒の 2 回目には OpenSSH クライアントを通した接続が要り、新しいセッションには v4.4212.0 以降、メッセージかリトライには v4.23118.0 以降が要る、と加わりました。Desktop が Windows で動くときと、リモートマシンが `MaxSessions 1` を設定しているときは v6.6395.0 以降が要ります
- **「Shared configuration」**: Models の項目から、Desktop と CLI で同じモデルが使える、という文が外れました（ハイライト 2 参照）

- [Desktop application - Claude Code Docs (English)](https://code.claude.com/docs/en/desktop#keys-that-apply-from-server-managed-settings-and-managed-settings-on-a-computer)
- [Desktop application - Claude Code Docs (English)](https://code.claude.com/docs/en/desktop#use-your-ssh-configuration)

## 軽微な更新

<!-- light:minor-updates:start -->
今回の差分は **2 ファイル**（`llms-full.txt`・見出しマップ）で、`llms.txt` は変わっていません。対象期間の途中の取り込み（`479f813`）では Claude Code の入力ファイルは変わっておらず、差分はすべて `ff1331b` の取り込みのものです。`llms-full.txt` で内容が変わったのは **3 ページ**で、大幅更新の `desktop` が 78 行（追加 62・削除 16）、`settings-reference` が 18 行（追加 11・削除 7）、`model-config` が 4 行（追加 2・削除 2。`llms-full.txt` に 2 回載っているページの同じ変更が 2 か所に出たもの）です（合計で追加 75・削除 25 で、生の差分と一致します）。以下は、大幅更新の `desktop` を除く 2 ページの変更です。changelog への追加と、新着情報（whats-new）のページはありません。

**新機能**

- `settings-reference` の `policyHelper` の下に h4「Keys that only Claude Desktop uses」ができた。Desktop は自分だけが使うキーをヘルパーを走らせずに読むので、そうしたキーはヘルパーを指定する MDM ポリシーか管理設定ファイルに置く（詳細はハイライト 1 参照） — [English](https://code.claude.com/docs/en/settings-reference#keys-that-only-claude-desktop-uses)

**機能改善**

- `settings-reference` の `sshHostAllowlist` の Scope が、サーバー管理設定を配るならそこと各コンピューターに同じ一覧を置く、になり、Desktop はこのキーをポリシーヘルパーから読まない、と加わった。Default には、サードパーティのプロバイダーでは SSH セッションは既定でオフ、と加わった（詳細はハイライト 1 参照） — [English](https://code.claude.com/docs/en/settings-reference#sshhostallowlist)
- `settings-reference` の `disableDesktopLocalSessions` の Scope が、サーバー管理設定を配るならそこと各コンピューターに置く、になり、`false` に「もう一方の場所の `true` がローカルセッションをオフにしうる」と加わった（詳細はハイライト 1 参照） — [English](https://code.claude.com/docs/en/settings-reference#disabledesktoplocalsessions)
- `model-config` の「Organization default model」で、上書きが有効でも `--model` フラグ・`ANTHROPIC_MODEL`・管理設定・`--settings` のモデルで新しいセッションが始まるのは「ターミナルでは」と限定された（詳細はハイライト 2 参照） — [日本語](https://code.claude.com/docs/ja/model-config#organization-default-model) / [English](https://code.claude.com/docs/en/model-config#organization-default-model)

**その他**

- `settings-reference` の `disableDesktopLocalSessions` で、Type の「JSON の Boolean の `true` だけが効く」が「JSON の Boolean の `true` を使う」という言い方になった。ほかの値は無視し、文字列の `"true"` や `1` のような Boolean でない値には警告も記録する、という文と、「Local sessions on managed devices」へのリンクの文が外れた — [English](https://code.claude.com/docs/en/settings-reference#disabledesktoplocalsessions)
- `settings-reference` の `sshHostAllowlist` の、`managedSourcesBehavior` を `"merge"` にしたときの段落で、どれかに一致するホストを「許す」が、片方にしか一致しないホストも「許しうる」に、空の配列を置いても SSH セッションがほかのソースのホストで「オンのまま」が「オンのままでありうる」になった — [English](https://code.claude.com/docs/en/settings-reference#sshhostallowlist)
<!-- light:minor-updates:end -->

見出しマップ（`en/claude_code_docs_map.md`）は、更新時刻が 2026年11月25日 06:20:24 UTC から 2026年11月28日 05:00:48 UTC に替わったほか、見出しの 4 行が加わりました（6,998 行から 7,002 行）。`desktop` の h4「Keys that apply from server-managed settings and managed settings on a computer」とその下の h5「Which SSH host allowlists apply」、h4「Set the model that new sessions start on」、`settings-reference` の h4「Keys that only Claude Desktop uses」で、どれも `llms-full.txt` に加わった見出しです。今回、見出しマップにだけ先に載った見出しはありません。

**参考リンクについて**: 日本語版は、リンクを付けた 3 ページの HTML を取得して確かめました。見るのは、見出しの id があるかと、今回の差分で出入りしたコードの字句（版の数字・キー名・リンク先。base と head の `llms-full.txt` で数が違うものだけ）が英語版と同じだけあるかです。`model-config` は、日本語版の「Organization default model」が「ターミナルでは」の文になっていたので、日本語版にもリンクしています。`desktop` は、日本語版に h4「Set the model that new sessions start on」と表の `model` の行があり、「Shared configuration」の Models の項目も今回の内容になっていたので、その節には日本語版にもリンクしています。一方、`desktop` の日本語版には h4「Keys that apply from server-managed settings and managed settings on a computer」がなく、`v6.6395.0` も 0 か所で、`v4.23118.0` や `#prepare-a-long-task` の数も英語版より少なくなっていました。SSH の節はまだ追従していないため、英語版だけにリンクしています。`settings-reference` の日本語版にも h4「Keys that only Claude Desktop uses」と新しいリンク先がないので、英語版だけにしています。h5 の「Which SSH host allowlists apply」「Raise the SSH connection timeout」「Prepare a long task」「Limits while Desktop is disconnected」には HTML の id がないため、親の h4 の id を使っています。**changelog ページへのリンクは、本サマリの方針どおり付けていません。**

## 新着情報

<!-- light:whats-new:start -->
（今回の差分に新着情報（`whats-new/`）のページはありません）
<!-- light:whats-new:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-11-25.md](./archives/latest/2026-11-25.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-11-25.md](./archives/latest-detail/2026-11-25.md)

<!--
base_commit: 1fbf59d6a37ee0c078616ce1887005838b16c3ae
head_commit: ff1331b1ac08161c9abe13ea96b72c30b1a450ff
generated_at_full: 2026-11-28T15:05:59+09:00
-->
