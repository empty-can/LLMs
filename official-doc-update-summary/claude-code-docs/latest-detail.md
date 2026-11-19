---
対象期間: 2026年11月17日 〜 2026年11月18日
作成日: 2026-11-18
---

# Claude Code 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
**今回は changelog に v2.1.328（2026年11月19日、144 項目）が積まれ、OpenTelemetry のデータにセッションを動かしたマシンの名前と ID を載せる `OTEL_RESOURCE_INCLUDE_HOST` の節が `monitoring-usage` にできました。VS Code の拡張機能から Claude apps gateway にサインインする手順、セッション同士のやり取りが長く続いたときの制限、7 つの手順に書き直された GitHub Actions のクイックセットアップ、組み込みのガードとユーザーの mod の関係の説明も載っています**。新規ページと新着情報（whats-new）のページはありません。`llms.txt` は変わっていません。`llms-full.txt` では 205 ページのうち 52 ページ（changelog を含む）の内容が変わりました。生の差分は 630 行（追加 459・削除 171）で、うち 160 行は changelog の新しいリリースです。大幅更新は `monitoring-usage` の 1 ページです。総行数は 129,614 行から 129,902 行に増えました。

主要なものを以下に挙げます。

1. `monitoring-usage` に、`OTEL_RESOURCE_INCLUDE_HOST=1`（v2.1.326 以降）でメトリクス・イベント・トレースのリソースの属性に `host.name` と `host.id` を載せる節と、それが届かないときの 9 つの原因の節ができた
2. VS Code の拡張機能のパネルから Claude apps gateway にサインインする 4 つの手順が `vs-code` に載った（v2.1.316 以降）。`authentication`・`cli-reference`・`errors` もこれに合わせて改められた
3. `cross-session-messaging` の「Limitations」に、ゆっくり答え合うセッション同士は数千のメッセージをやり取りしうること、長いやり取りの後は送信が止まりうること、長い返信の連なりは切られうることが載った
4. `github-actions` の「Quick setup」が、GitHub CLI へのサインインからプルリクエストのマージまでの 7 つの手順に書き直された
5. `plugins/mods/admin` で、組み込みのガードが止めるもの、ユーザーの mod が Claude の呼び出しを承認したときに保たれる結果、mod 自身の呼び出しが飛ばしうるチェックが、項目に分けて書き直された
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**マシンの名前と ID を OpenTelemetry に載せる変数の節ができた**](#1-マシンの名前と-id-を-opentelemetry-に載せる変数の節ができた):  
  `monitoring-usage` に h3「Identify the machine a session ran on」と h4「Troubleshoot missing host attributes」ができ、`OTEL_RESOURCE_INCLUDE_HOST` の設定場所・値・プライバシーの注意が載りました。`env-vars` と `settings-reference` にもこの変数が加わっています
2. [**VS Code から Claude apps gateway にサインインできることが載った**](#2-vs-code-から-claude-apps-gateway-にサインインできることが載った):  
  `vs-code` に h2「Sign in to a Claude apps gateway」ができ、パネルからのサインインの 4 つの手順と、ターミナルで済ませるよう求められたときの対処が載りました。changelog の v2.1.316 にある変更にページが追従したものです
3. [**セッション同士のやり取りが長く続いたときの制限が載った**](#3-セッション同士のやり取りが長く続いたときの制限が載った):  
  `cross-session-messaging` の「Limitations」から「ループは自然に止まる」という文が外れ、遅いループは続きうる・送信が止まりうる・返信の連なりが切られうる、の 3 項目が加わりました
4. [**GitHub Actions のクイックセットアップが 7 つの手順になった**](#4-github-actions-のクイックセットアップが-7-つの手順になった):  
  `github-actions` の「Quick setup」が番号付きの手順に書き直され、ワークフローの選び方、既存の `claude.yml` を残す方法、変更の確認が加わりました
5. [**組み込みのガードとユーザーの mod の関係が書き直された**](#5-組み込みのガードとユーザーの-mod-の関係が書き直された):  
  `plugins/mods/admin` の「Know what happens by default」が項目に分けて書き直され、`permissions` の「Precedence among rules, hooks, and mods」も、ガードの有無で何が変わるかという言い方になりました
<!-- light:highlight-list:end -->

## 1. マシンの名前と ID を OpenTelemetry に載せる変数の節ができた

**`monitoring-usage` に h3「Identify the machine a session ran on」ができました（詳細は大幅更新 1 参照）。** Claude Code v2.1.326 以降で `OTEL_RESOURCE_INCLUDE_HOST=1` を設定すると、各セッションがどのマシンで動いたかがわかるよう、メトリクス・イベント・トレースのリソースのブロックに `host.name` と `host.id` が載ります。メトリクスのデータポイントには載りません。

- **設定する場所**: managed settings かユーザーの設定の `env`、または `claude` を始めるシェル。プロジェクトとローカルの設定では無視される（`settings-reference` の「Variables Claude Code ignores in `env`」にもこの変数が加わった）
- **値**: `host.name` はマシンのホスト名。`host.id` は OS のマシン ID をハッシュせずに載せたもので、Linux では `/etc/machine-id` の内容、macOS では `IOPlatformUUID`、Windows ではレジストリーの `MachineGuid` の値。マシン ID のないイメージのコンテナーのように、Claude Code が読めなければ外れる
- **どのマシンを指すか**: どちらも Claude Code が動くマシンを指す。Desktop の SSH のセッションならリモートのマシンなので、そちらで設定する。コンテナーでは `host.name` はコンテナー自身のホスト名なので、コンテナーを動かすマシンを名指すには `OTEL_RESOURCE_ATTRIBUTES` で自分で宣言する
- **届かないとき**: h4「Troubleshoot missing host attributes」に 9 つの原因と対処が並んだ。セッションの Claude Code が v2.1.326 より古い、プロジェクトかローカルの設定だけで設定した、managed かユーザーの設定ファイルで `0` になっている、セッションの開始後に設定した（起動時に 1 度だけ読む）、デスクトップアプリが始めたセッション（シェルのプロファイルからこの変数を受け取らない）、Anthropic がホストする環境のクラウドのセッション（属性が付かない）、エクスポーターの変数に `console` がある、シグナル別のエンドポイントの変数が URL でない、メトリクスのバックエンドがリソースの属性を出さない（`prometheus` のエクスポーターなら `target_info` のメトリクスの `host_name` と `host_id` のラベルを見る）、の 9 つ
- **プライバシー**: 「Security and privacy」に、マシンの名前と ID は既定では含まれず、ホスト名には人の名前が含まれることが多く、`host.id` はマシンを長く識別する値である、と加わった。managed settings で設定するなら、Claude Code はその人たちに通知を出さないので、それらのマシンを使う人に伝える

`env-vars` の表にも `OTEL_RESOURCE_INCLUDE_HOST` の行が加わり、「Common configuration variables」の表と「Service information」にも載っています。changelog の v2.1.326 の Added にある、`host.name` と `host.id` を OpenTelemetry のリソースの属性に含める `OTEL_RESOURCE_INCLUDE_HOST`（既定はオフ）の追加に、ページが追従した形です。

- [監視 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/monitoring-usage#identify-the-machine-a-session-ran-on)
- [Monitoring - Claude Code Docs (English)](https://code.claude.com/docs/en/monitoring-usage#identify-the-machine-a-session-ran-on)
- [環境変数 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/env-vars#variables)
- [Environment variables - Claude Code Docs (English)](https://code.claude.com/docs/en/env-vars#variables)

## 2. VS Code から Claude apps gateway にサインインできることが載った

**`vs-code` に h2「Sign in to a Claude apps gateway」ができました。** マシンの設定がゲートウェイを名指していれば（`claude-apps-gateway` の「Set the gateway URL」）、Claude Code のパネルから Claude apps gateway にサインインできます。Claude Code v2.1.316 以降が要ります。

1. パネルがチャットで開いたら、プロンプトの欄に `/` と入力して **Sign in to Cloud gateway** を選ぶ。一覧になければ **Switch account** を選ぶ
2. サインインの画面で **Cloud gateway** をクリックする
3. 示されたゲートウェイの URL と証明書のフィンガープリントを、管理者が公開したものと比べる。どちらかが違えば **Cancel sign-in** をクリックして管理者に伝え、同じなら URL では **Sign in**、フィンガープリントでは **Yes, trust this gateway** をクリックする
4. ブラウザーで開いたページのコードがパネルのものと一致するかを確かめる。一致すれば続けて業務のアカウントでサインインし、一致しなければページを閉じて管理者に伝える

画面に `Login is managed by your organization and must be completed in the terminal.` と出たら、拡張機能を更新します。更新せずにサインインするには、CLI を入れ、**Run `claude` in terminal** をクリックして、そこで `/login` を実行します。「Fix common issues」の表にもこのメッセージの行が加わり、「Prerequisites」も、Claude apps gateway ならこの節を見る、となりました。

ほかのページもこれに合わせて改められています。

- **`authentication` の「Log in to Claude Code」**: Cloud gateway の項目が、`/login` に加えて VS Code からも企業の SSO でサインインできる、となった
- **`cli-reference` の `claude auth login`**: managed settings が Claude apps gateway へのサインインを求めるなら、v2.1.316 以降でフラグを付けずにターミナルで実行する。コマンドが `/login` を案内したら `claude` の中でそれを実行する、と加わった
- **`errors` の「Find your error」**: `Managed settings on this machine configure a Cloud gateway sign-in; run interactive /login to authenticate.` の行が加わった（`cli-reference` の `claude auth login` へ）
- **`claude-apps-gateway` の「Set the gateway URL」**: 「ログインのピッカーにはゲートウェイの選択肢がない」が「ターミナルのログインのピッカーには」になった

changelog の v2.1.316 にある、VS Code のチャットのパネルからターミナルなしに Claude apps gateway にサインインできるようにした追加に、ページが追従した形です。

- [VS Code で Claude Code を使用する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/vs-code#sign-in-to-a-claude-apps-gateway)
- [Use Claude Code in VS Code - Claude Code Docs (English)](https://code.claude.com/docs/en/vs-code#sign-in-to-a-claude-apps-gateway)
- [CLI リファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/cli-reference#cli-commands)
- [CLI reference - Claude Code Docs (English)](https://code.claude.com/docs/en/cli-reference#cli-commands)

## 3. セッション同士のやり取りが長く続いたときの制限が載った

**`cross-session-messaging` の「Limitations」に 3 つの項目が加わりました。** 受け手のセッションがメッセージのループを抑える、という項目からは、「そのため 2 つのセッションのループは自然に止まる」という結びの文が外れています。

- **このマシンの遅いループは続きうる**: 抑えられない程度にゆっくり答え合う 2 つのセッションは、あなたのプロンプトなしに数千のメッセージをやり取りでき、届いた各メッセージは使用量に数えられる。止めるには、どちらかのセッションを終えるか、メッセージを受け取らないようにする。バックグラウンドのセッションなら、アタッチして `/stop` を実行する
- **長いやり取りの後は送信が止まりうる**: `SendMessage` の結果が `Not delivered: this session keeps answering other sessions` で始まったら、そのセッションにプロンプトを入力すると送信を再開できる
- **一部の長い返信の連なりは切られうる**: 返信の連なりが長くなると、届けるのが止まることがある（たとえば、このマシンの外のセッションを含む連なり）。やり取りを続けるには、連なりの中のどれかのセッションにプロンプトを入力する

「Availability」のトラブルシューティングにも「Long exchange between sessions」の項目が加わり、多くの返信の後に止まったやり取りは、送る側のセッションにプロンプトを入力すると再開する、となりました。`errors` の「Cross-session message was dropped at the recipient session's inbox」でも、`a relay loop between sessions was cut` の説明が、「セッションが互いに送り合う連なりで、受け手を何度も通ったか長くなりすぎた」から、「切られうる長い返信の連なり（このマシンの外のセッションを含むものなど）を続けた」に替わっています。

同じページのほかの変更です。

- **ほかのマシンからの返信**: ほかのマシンのセッションから返信を受けるには、Claude が送る前にセッションを Remote Control につなぐ。つながないとメッセージに返信先が付かず、受け手の Claude は答えられない、という言い方になった
- **`isolatePeerMachines`**: このマシンの外へ出る前に承認を求める対象が、「どのメッセージも」「どの `SendMessage` も」から「Claude のメッセージ」「Claude の `SendMessage`」になった

changelog の v2.1.328 には、クラウドのセッションかほかのコンピューターが一覧にないときに Remote Control がオフだと Claude が説明するようにした改善と、始まったばかりかタイトルに @ を含むセッションにセッション間のメッセージが届かない問題の修正があります。

- [他の Claude Code セッションにメッセージを送信する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/cross-session-messaging#limitations)
- [Message your other Claude Code sessions - Claude Code Docs (English)](https://code.claude.com/docs/en/cross-session-messaging#limitations)
- [エラーリファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/errors#cross-session-message-dropped-at-the-inbox)
- [Error reference - Claude Code Docs (English)](https://code.claude.com/docs/en/errors#cross-session-message-dropped-at-the-inbox)

## 4. GitHub Actions のクイックセットアップが 7 つの手順になった

**`github-actions` の「Quick setup」が、番号付きの 7 つの手順に書き直されました。** 冒頭に、ブラウザーで Claude GitHub App を入れ、プルリクエストを作ってマージする、という流れの説明が置かれています。

1. **GitHub CLI にサインインする**: GitHub CLI を入れ、まだサインインしていなければシェルで `gh auth login` を実行する
2. **Claude Code からセットアップを始める**: 接続するリポジトリで `claude` を起動し、`/install-github-app` を実行する。GitHub CLI の権限が足りないと報告されたら、表示されたコマンドを実行してやり直す
3. **Claude GitHub App を入れる**: ブラウザーで開いたページでアプリを入れてリポジトリへのアクセスを与え、Claude Code に戻って Enter を押す
4. **ワークフローを選ぶ**: **Set up GitHub Actions workflows** を選ぶ。アプリだけを入れて止めるなら、ワークフローのセットアップを断り、後で `/install-github-app` を実行し直す。一覧では、`@claude` のメンションのワークフローかプルリクエストのレビューのワークフローの選択を外せる。リポジトリにすでに `claude.yml` があれば、一覧の代わりに更新の質問が出るので、ファイルを残すなら **Skip workflow update (configure secrets only)** を選び、プルリクエストの手順を飛ばす
5. **ワークフローの認証情報を選ぶ**: Claude のサブスクリプションで長期のトークンを作るか、API キーを貼り付けるかを選ぶ。Claude Code がすでに API キーを持っていれば、この質問を飛ばしてそのキーを使う。既定では、リポジトリのシークレット `ANTHROPIC_API_KEY` か `CLAUDE_CODE_OAUTH_TOKEN` として保存する
6. **変更を確かめる**: リポジトリへの予定の変更が一覧になったら **Yes, make these changes** を選ぶ
7. **プルリクエストを作ってマージする**: Claude Code がワークフローのファイルのブランチをプッシュし、プルリクエストを作れる状態で GitHub を開く。マージするとワークフローが有効になり、issue のコメントで `@claude` をタグ付けして試せる

これまでの、既存の API キーを使い回すときにリポジトリの既存の `ANTHROPIC_API_KEY` のシークレットを残すかを尋ねる、という説明と、GitHub App を入れた後に **Skip for now** で止められる、という段落は外れました。Esc で途中で止めたときの説明も、「進行中の手順は終わり、後の手順は始まらない」から「リポジトリに書き込み中の変更は終え、新しい変更は始めない」になっています。「Setup」の項目も、「GitHub App を入れ、認証のシークレットを加え、ワークフローのプルリクエストを用意する」から「認証のシークレットとワークフローのファイルを用意する」になり、`github-actions-cloud-providers` からは、クイックセットアップが公式の Claude GitHub App を入れる、という文が外れました。

changelog の v2.1.327 には `/install-github-app` がリポジトリを変更する前の確認の追加と画面の改善が、v2.1.328 には既存のワークフローのファイルの更新を頼んだときにコードレビューのワークフローを加える問題の修正があります。

- [Claude Code GitHub Actions - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/github-actions#quick-setup)
- [Claude Code GitHub Actions - Claude Code Docs (English)](https://code.claude.com/docs/en/github-actions#quick-setup)

## 5. 組み込みのガードとユーザーの mod の関係が書き直された

**`plugins/mods/admin` の「Know what happens by default」で、組み込みのガードとユーザーの mod の関係が項目に分けて書き直されました。** ガードが読み込まれる条件（managed settings か `managed-mcp.json` があるマシン、または Team か Enterprise のプランの `/login` の認証情報で動くセッション）は変わっていません。

- **ガードが書き換えを止めるもの**: ガードが読み込まれると、ユーザーの mod は、システムプロンプト、managed の `CLAUDE.md` とほかの managed の指示、mod が設定を読んだときに得る答え、接続した managed の MCP サーバーのツールの一覧とツールの説明を書き換えられない。これまでは「管理するものを守る」の 1 項目で、managed のフックが受け取るものと判断も挙げていた
- **Claude の呼び出しを mod が承認したとき**: ガードが読み込まれていれば既定で、ルールかフックがどの設定ファイルにあっても、`deny` ルールが拒む呼び出しは拒まれたまま、`ask` ルールが確認を求める呼び出しは確認を求め、`PreToolUse` のフックが止めた呼び出しは止まったまま
- **mod 自身の呼び出しはチェックを飛ばしうる**: `$.fs` と `$.process` の呼び出しは、権限のルールと `PreToolUse` のフックを飛ばしうる（`Read(.env)` を拒んでも、mod は `$.fs.read` か、それを読むプログラムを始めて読める）。`$.tool.call` や `$.mcp.call` のような呼び出しは、権限のルール・許可のプロンプト・フックの `ask`・auto モードの分類器を飛ばしうる。ユーザーの mod を制限するには、読み込ませないか、ポリシーの mod でその呼び出しを扱う
- **ガードがなければ**: ユーザーの mod はさらに多くのチェックを飛ばしうる、として `permissions` の節にリンクする
- **外れた項目**: auto モードで mod が承認した呼び出しは分類器の確認なしに実行されるが、ガードがあり `--permission-prompt-tool` か Agent SDK の `canUseTool` のコールバックで動くセッションでは先に分類器が確かめる、という項目

同じページの「Know which controls still apply」は、「既存の制御はこの範囲で mod に及ぶ」という前置きになりました。設定ファイルのフックは mod と並んで実行される、ガードが読み込まれるところでは Claude の呼び出しについて `deny` ルールがユーザーの mod より優先する（`allowModsToOverrideDenyRules` で一部の呼び出しを承認させられる）、許可のプロンプトは Claude Code が描くとおりに出る、という言い方です。「Review what a mod can do」の `$.mcp.call` の行からは、deny ルールか managed の ask ルールの下の呼び出し・`requiresUserInteraction` の付いたツール・組織が `ask` にしたツールへの呼び出しを Claude Code が拒む、という文が外れ、「許可のプロンプトなしに、接続した MCP サーバーのツールを呼ぶ」だけになっています。

**`permissions` の「Precedence among rules, hooks, and mods」も改められました。** managed settings か `managed-mcp.json`、または Team か Enterprise の `/login` がセッションの認証情報であれば、組み込みのガードが既定で読み込まれ、組織のものではない mod が Claude の呼び出しを承認したときに上の結果が保たれる、という説明になりました。そうした構成がないときについては、次のようになっています。

- mod は、`PreToolUse` のフックが止めた呼び出しと、deny ルールが拒む「一部の」呼び出しを承認できる（これまでは、deny ルールが拒む呼び出しを承認できる）
- mod が承認した呼び出しは、ask ルール・`PreToolUse` のフック・`permissions.blockReadsOutsideWorkingDirectories` のプロンプトと、`--permission-prompt-tool` か `canUseTool` のコールバックを飛ばし「うる」
- auto モード・plan モード・`dontAsk` モードがそれぞれ結果を加えるのは「どの構成でも」から「その構成で」になり、auto モードでは mod が承認した呼び出しが分類器の確認なしに実行され「うる」となった（許可のプロンプトのツールか Agent SDK のコールバックがある場合の例外は外れた）

関連して、`permissions` の「Permission modes」の表の `dontAsk` の行は「一部の構成で」mod が承認できる、`hooks` の「PermissionRequest decision control」の `behavior` は、mod がルールを上書きしない限りフックは deny ルールが拒むものを承認できない、となりました。`plugins/mods/reference` の「Mods API methods」の `$.tool` の行からは、人の承認が要る `call` が `{ deny: "<tool> wasn't run: …" }` で解決する、という説明が外れています。

- [組織向けの mod を管理する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/plugins/mods/admin#know-what-happens-by-default)
- [Manage mods for your organization - Claude Code Docs (English)](https://code.claude.com/docs/en/plugins/mods/admin#know-what-happens-by-default)
- [権限を設定する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/permissions#precedence-among-rules-hooks-and-mods)
- [Configure permissions - Claude Code Docs (English)](https://code.claude.com/docs/en/permissions#precedence-among-rules-hooks-and-mods)

## 新規追加されたページ

<!-- light:new-pages:start -->
（今回の対象期間に新規追加されたドキュメントページはありません。`llms.txt` は変わっておらず、`llms-full.txt` の `Source:` の行も 208、固有のページも 205 のままです）
<!-- light:new-pages:end -->

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
- [**Monitoring**](#1-monitoring) ([日本語](https://code.claude.com/docs/ja/monitoring-usage#identify-the-machine-a-session-ran-on) / [English](https://code.claude.com/docs/en/monitoring-usage#identify-the-machine-a-session-ran-on)):  
  50 行（追加 46・削除 4）が変わりました。`OTEL_RESOURCE_INCLUDE_HOST` でマシンの名前と ID を載せる h3 と、それが届かないときの h4 ができ（詳細はハイライト 1 参照）、Desktop の SSH のセッションのマシンを見分ける節も、この変数とカスタムの属性の 2 つの方法を並べる形になりました
<!-- light:updated-pages:end -->

**行数の数え方**: `llms-full.txt` の生の差分のハンクを、追加行は head 側、削除行は base 側の `Source:` 行でページに振り分けた値です。ページの並びは変わっていません。changelog（160 行）は新しい 1 リリースの分なので、これまでどおり「軽微な更新」で扱います。大幅更新の 1 ページに次いで多いのは `github-actions` の 45 行（追加 35・削除 10）、`plugins/troubleshooting` の 36 行（追加 18・削除 18）、`errors` と `plugins/mods/admin` の各 30 行（追加 21・削除 9／追加 19・削除 11）で、どれも 50 行に届きません。

## 1. Monitoring

**`monitoring-usage` は 50 行（追加 46・削除 4）が変わり、`llms-full.txt` の中のページは 1,844 行から 1,886 行になりました。** 見出しは h3「Identify the machine a session ran on」と、h4「Troubleshoot missing host attributes」「Name each remote machine in a custom attribute」の 3 つが加わり、外れたものはありません。`llms.txt` の説明文は変わっていません。

- **「Common configuration variables」**: 表に `OTEL_RESOURCE_INCLUDE_HOST` の行が加わった（既定はオフ、`1` でオン、v2.1.326 以降）
- **新しい h3 と h4**: 「Identify the machine a session ran on」と「Troubleshoot missing host attributes」（詳細はハイライト 1 参照）
- **「Attribute telemetry to Desktop SSH sessions」**: Desktop の SSH のセッションが動いたリモートのマシンを見分けるには、`OTEL_RESOURCE_INCLUDE_HOST=1` を設定するか、各マシンにカスタムの属性で名前を付ける、の 2 つの方法になった。`OTEL_RESOURCE_INCLUDE_HOST=1` では `host.name` がリソースのブロックにしか出ないので、メトリクスのデータポイントに名前が要るならカスタムの属性を選ぶ。変数は、リモートのマシンの、セッションが読む managed settings のファイルの、テレメトリーをオンにする `env` のブロックに設定し、セッションが動かす Claude Code のコピーは v2.1.326 以降でなければならない。「メトリクスとイベントはセッションが動いたマシンを名指さない」という文は外れた
- **新しい h4「Name each remote machine in a custom attribute」**: これまでの `OTEL_RESOURCE_ATTRIBUTES` で名前を付ける手順がこの h4 の下に入った。`host.name` は、ほかに変数を設定するものがなければリソースのブロックに届く、から、リソースのブロックと、既定ではメトリクスのデータポイントとイベントに届き、Desktop の SSH のセッションとそのマシンの CLI の両方が送る、になった（データポイントから外すには「Multi-team organization support」を見る）。届かないときの原因の一覧も、`OTEL_RESOURCE_ATTRIBUTES` で設定した名前が届かないとき、と対象が明示された
- **「Managed settings resolved event」**: `managed_settings.resolved_sha256` は、同じダイジェストのマシンは「同じポリシーで動く」から「同じ managed settings を解決した」に、オプトインのときだけダイジェストを送るのは「Claude Code」から「イベント」になった
- **「Service information」**: `host.name` と `host.id`（既定はオフ）の項目が加わった
- **「Security and privacy」**: マシンの名前と ID についての注意が加わった（ハイライト 1 参照）

- [監視 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/monitoring-usage#identify-the-machine-a-session-ran-on)
- [Monitoring - Claude Code Docs (English)](https://code.claude.com/docs/en/monitoring-usage#identify-the-machine-a-session-ran-on)
- [監視 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/monitoring-usage#attribute-telemetry-to-desktop-ssh-sessions)
- [Monitoring - Claude Code Docs (English)](https://code.claude.com/docs/en/monitoring-usage#attribute-telemetry-to-desktop-ssh-sessions)

## 軽微な更新

<!-- light:minor-updates:start -->
今回の差分は **2 ファイル**（`llms-full.txt`・見出しマップ）で、`llms.txt` は変わっていません。`llms-full.txt` では、205 ページのうち **52 ページ**（changelog を含む）の内容が変わりました。大幅更新の 1 ページを除く **50 ページ**と、changelog に加わった **v2.1.328（2026年11月19日、144 項目。Added 14・Changed 20・Improvements 19・Bug fixes 91）** を以下にまとめます。単一のリリースなので、changelog の各項目への版の併記は省いています。changelog の収録リリースは 443 から 444 になり、先頭は v2.1.328 です。新着情報（whats-new）のページはありません。

`llms-full.txt` の総行数は **129,614 行から 129,902 行へ 288 行増え**ました（生の差分の差し引き 459 − 171 と一致）。生の差分 630 行の内訳は、changelog の新しいリリースが 160 行、`monitoring-usage` が 50 行（追加 46・削除 4）、残りの 50 ページが 420 行（追加 253・削除 167）です。この 420 行のうち 10 行は、`llms-full.txt` に 2 回載っている `plugins/install` の同じ変更が、2 か所目に出たものです。

コードフェンスの外の見出しは、行頭が `#` の見出しだけを数えると 6,154 から 6,160 へ、引用の中の見出しも数えると 6,165 から 6,171 へ、どちらも 6 増えました。加わったのは、`vs-code` の h2「Sign in to a Claude apps gateway」、`monitoring-usage` の h3「Identify the machine a session ran on」と h4「Troubleshoot missing host attributes」「Name each remote machine in a custom attribute」、`permission-modes` の h3「Restricted mode refuses bypassPermissions」、`plugins/mods/api` の h4「Hide command text from Claude」の 6 つです。ほかに 5 つの見出しが改称されました（下の「その他」）。

**新機能**

- マシンの名前と ID を OpenTelemetry に載せる `OTEL_RESOURCE_INCLUDE_HOST`（`monitoring-usage`・`env-vars`・`settings-reference`。詳細はハイライト 1 参照）
- VS Code から Claude apps gateway へのサインイン（`vs-code`・`authentication`・`cli-reference`・`errors`・`claude-apps-gateway`。詳細はハイライト 2 参照）
- **mod のコマンドのテキストを Claude に読ませない方法が載った**（`plugins/mods/api` の新しい h4「Hide command text from Claude」）。コマンドのテキストを Claude に読ませずに表示するには、`next` を呼ばないフックから `{ text, isTextDisplayOnly: true }` を返し、登録に `immediate` を付けません。そうでないとき、または v2.1.326 より前は、Claude がテキストを読めます。「Add a command」の、返した `text` を Claude が読む、という文にも、この節で隠さない限り、と加わりました — [日本語](https://code.claude.com/docs/ja/plugins/mods/api#hide-command-text-from-claude) / [English](https://code.claude.com/docs/en/plugins/mods/api#hide-command-text-from-claude)
- **mods API の `$.agent` に `call` と `limits` が加わった**（`plugins/mods/reference` の「Mods API methods」）。どちらも Claude Code v2.1.326 以降が要ります — [日本語](https://code.claude.com/docs/ja/plugins/mods/reference#mods-api-methods) / [English](https://code.claude.com/docs/en/plugins/mods/reference#mods-api-methods)
- **VS Code のエクスプローラーから @-メンションする方法が載った**（`vs-code` の「Reference files and folders」）。エクスプローラーでファイルかフォルダーを右クリックし、**Claude Code: Add to Chat** を選びます。Claude Code v2.1.327 以降が要ります。changelog の v2.1.327 にある追加にページが追従しました — [日本語](https://code.claude.com/docs/ja/vs-code#reference-files-and-folders) / [English](https://code.claude.com/docs/en/vs-code#reference-files-and-folders)
- **`claude mcp add-json` に JSON を標準入力から渡す方法が載った**（`mcp` の「Add MCP servers from JSON configuration」）。JSON の代わりに `-` を渡します（`cat server.json | claude mcp add-json <name> -`）。Claude Code のセッションの外で実行し、v2.1.327 以降が要ります。changelog の v2.1.327 にある追加にページが追従しました — [日本語](https://code.claude.com/docs/ja/mcp#add-mcp-servers-from-json-configuration) / [English](https://code.claude.com/docs/en/mcp#add-mcp-servers-from-json-configuration)
- **`HTTPS_PROXY` に `http://` がないときの扱いと、それを止める変数が載った**（`network-config` の「Verify your configuration」・`env-vars`）。v2.1.327 以降では、標準入力も標準出力もターミナルでない起動（Claude Desktop・SDK・cron が Claude Code を始めるとき）は、`http://` のない `HTTPS_PROXY` の値でも先へ進みます。一部のセッションで単なる `host:port` が動いても、値は `http://proxy.example.com:8080` のような完全な URL で書きます。`env-vars` には、ターミナルなしに始めたときも単なる `host:port` で起動時に止める `CLAUDE_CODE_DISABLE_PROXY_SCHEME_REPAIR`（プロジェクトとローカルの設定では無視、v2.1.327 以降）が加わりました。changelog の v2.1.327 にある、このとき Claude Code が起動を拒む問題の修正にページが追従した形です — [日本語](https://code.claude.com/docs/ja/network-config#verify-your-configuration) / [English](https://code.claude.com/docs/en/network-config#verify-your-configuration)
- **`/tui classic` が載った**（`commands` の「All commands」）。`/tui [classic|fullscreen]` になり、`default`、または v2.1.327 以降では `classic` でクラシックのレンダラーを選ぶ、となりました。changelog の v2.1.327 にある追加にページが追従しました — [日本語](https://code.claude.com/docs/ja/commands#all-commands) / [English](https://code.claude.com/docs/en/commands#all-commands)
- Amazon Bedrock・Google Cloud の Agent Platform・Microsoft Foundry・Claude apps gateway で、Claude Opus 4.6 と Sonnet 4.6 の auto モードを追加。権限モードを指定しない対話のセッションは auto モードで始まります（`permission-modes` の「Auto mode on Bedrock, Agent Platform, or Foundry」は、head の時点でも、これらのプロバイダーで使えるモデルを Claude Sonnet 5 以降・Opus 4.7 以降・Haiku 5.5・Fable のモデルとしており、まだこの変更に追従していません）
- command と HTTP のフックと同じく、`mcp_tool` のフックにも `"onFailure": "block"` を追加。呼び出しが失敗したフックが操作を止めます
- 許可のプロンプトを飛ばすセッションからのメッセージが、クラウドのセッションに保留されて落とされうるときの警告を追加
- OpenTelemetry のエクスポーターにエンドポイントがなく、データが失われそうなときの通知を `/status` と `claude doctor` に追加
- フックが保留したツールの呼び出しを `claude -p --resume` と `--continue` が実行しないよう、ホストが止められる `CLAUDE_CODE_DISABLE_DEFERRED_TOOL_RESUME` を追加
- Claude Code を組み込むアプリが、ポリシーのプラグインの `allowManagedModsOnly` のオプションをオンにできるよう対応。管理者の managed settings が引き続き優先されます
- ポリシーの `maxEffortLevel` が有効な effort のレベルでないときの起動時の警告を Claude apps gateway に追加
- セルフホストのランナー: `--capacity 1` でセッションがリポジトリに使うフォルダーを、ベースのフォルダーの下のパス（シンボリックリンクにできない）の代わりに名指す `--repository-folder` を追加
- セルフホストのランナー: ホストの settings.json が、セッションが無視する既定の権限モードを設定しているときの起動時の警告を追加
- セルフホストのランナー: 選んだセッションのラベルを `spawn-runner` のフックに渡す `--hook-label` を `claude self-hosted-runner orchestrator` に追加
- セルフホストのランナー: `spawn-runner` のフック向けにセッションにラベルを付ける `--metadata key=value` を `claude --environment` に追加
- セルフホストのランナー: オーケストレーターの `/metrics` に `claude_code_self_hosted_orchestrator_session_queue_wait_by_reason_seconds` を追加。開き直したセッションの待ちを、新しいセッションの待ちと区別できます
- セルフホストのランナー: Anthropic がセッションのランナーの起動をあきらめた回数を原因別に数える、オーケストレーターのメトリクス `claude_code_self_hosted_orchestrator_sessions_given_up_total` を追加
- [VSCode] ほかのセッションからのメッセージが保留されたときの通知を、それを許可できる設定ファイルへのリンク付きで追加

**機能改善**

- セッション同士の長いやり取りの制限（`cross-session-messaging`・`errors`。詳細はハイライト 3 参照）
- GitHub Actions のクイックセットアップの手順（`github-actions`・`github-actions-cloud-providers`。詳細はハイライト 4 参照）
- 組み込みのガードとユーザーの mod の関係（`plugins/mods/admin`・`permissions`・`hooks`・`plugins/mods/reference`。詳細はハイライト 5 参照）
- Desktop の SSH のセッションのマシンの見分け方と `managed_settings.resolved_sha256` の説明（`monitoring-usage`。詳細は大幅更新 1 参照）
- **auto-compact の窓の値の範囲の書き方から、上限の 1,000,000 が外れた**（`sub-agents`・`model-config`・`env-vars`・`settings-reference`・`agent-sdk/subagents`・`agent-sdk/typescript`）。`autoCompactWindow`・`CLAUDE_CODE_AUTO_COMPACT_WINDOW`・`modelSettings` の `autoCompactWindow`・`/autocompact` の値は、「`100000` から `1000000`（100K から 1M）」ではなく「`100000`（100K）以上」と書かれるようになりました。ただし `model-config` の「Values and warnings for `CLAUDE_CODE_AUTO_COMPACT_WINDOW`」の表には、大きすぎる値を 1M の上限として扱う、という警告の行が残っています。`sub-agents` では、`200k` が 200 と読まれるのは「許される範囲の外」から「最小値を下回る」に、`CLAUDE_CODE_AUTO_COMPACT_WINDOW` も設定したときは、変数の窓が使われてこのフィールドは効かない、から、`autoCompactWindow` の値・モデルのコンテキストウィンドウ・変数が設定する窓のうち最も小さいものを使い、v2.1.312 より前はこのフィールドが効かなかった、になりました（changelog の v2.1.312 にある変更）。`model-config` では、値を引用する警告の意味が「100,000 から 1,000,000 の外か、トークン数でない」から「設定したとおりの値をセッションが使っていない」になっています — [日本語](https://code.claude.com/docs/ja/sub-agents#subagent-auto-compact-window) / [English](https://code.claude.com/docs/en/sub-agents#subagent-auto-compact-window)、[日本語](https://code.claude.com/docs/ja/model-config#set-the-auto-compact-window) / [English](https://code.claude.com/docs/en/model-config#set-the-auto-compact-window)
- **制限モードと `bypassPermissions` の節ができた**（`permission-modes` の新しい h3「Restricted mode refuses bypassPermissions」）。`--restricted` で始めたセッションが `bypassPermissions` を拒むという文がこの h3 に移り、`Error: bypassPermissions not supported in restricted mode` が出たら、`--dangerously-skip-permissions` のような `bypassPermissions` を有効にするフラグか設定を外し、`bypassPermissions` を保つなら `--restricted` か `CLAUDE_CODE_RESTRICTED` なしに始める、と加わりました。`errors` の「Find your error」にもこの行と、`Session was started with bypass permissions, so plan mode won't ask before most edits or commands` の行（plan モードへ）が加わっています — [日本語](https://code.claude.com/docs/ja/permission-modes#restricted-mode-refuses-bypasspermissions) / [English](https://code.claude.com/docs/en/permission-modes#restricted-mode-refuses-bypasspermissions)
- **auto モードの `git status` の確認と `-c` のスクリプトの説明が改められた**（`permission-modes` の「How auto mode evaluates actions」「Removals inside nested commands and inline scripts」）。作業を捨てるコマンドの前に Claude Code が `git status` を実行する、という文は「実行することがある」になり、サーバー側の分類器の確認の下では、auto モードが最近操作を止めていない限り Claude Code は `git status` を飛ばしうるので、クリーンな作業ツリーでも `git reset --hard` が止められることがあり、止めた後は分類器がクリーンな状態を見て Claude の再試行を許しうる、と加わりました。`This shell -c script runs rm and could not be checked` が出たら、承認する前にスクリプトを読む（危険なパスの削除に数えられる）、という項目も加わっています — [日本語](https://code.claude.com/docs/ja/permission-modes#how-auto-mode-evaluates-actions) / [English](https://code.claude.com/docs/en/permission-modes#how-auto-mode-evaluates-actions)
- **`errors` の「Find your error」に 8 行が加わった**。Cloud gateway（ハイライト 2 参照）と、制限モード・plan モード（上の項目）の 3 行のほか、`Can't add to .mcp.json: it lists servers at the top level`（サーバーを `mcpServers` のキーの下に移す）、`This command's variables and substitutions expand to more text than the permission check reads, so it was not run`（変数と置換を減らすか短くするよう Claude に頼む）、`Sandbox settings can't be changed here` / `Sandbox settings are overridden by a higher-priority configuration`（`sandboxing` へ）、`Couldn't restore N files: the backup is missing or the file can't be written`（失敗したファイルを書き込めるようにしてバージョン管理から戻す）、`a settings change wasn't saved`（`~/.claude/settings.json` とプロジェクトの `.claude/settings.local.json` を書き込めるようにしてやり直す）です。`.mcp.json` と変数の展開の 2 行は、changelog の v2.1.327 にある変更のメッセージです — [日本語](https://code.claude.com/docs/ja/errors#find-your-error) / [English](https://code.claude.com/docs/en/errors#find-your-error)
- **`errors` のいくつかの節が改められた**（「Could not update your spend limit」「Workspace not trusted when running claude ultrareview」「Workspace not trusted when starting Remote Control」「A command-line deny rule cannot be handed to a teammate intact」）。上限を外すときの汎用の形は v2.1.327 以降 `Could not remove your spend limit` で始まる、と加わりました。セッションの中の `/ultrareview` と `/code-review ultra` が `Ultrareview did not start: "<folder>" is not trusted, and this session started without asking whether you trust it` で止まることがあり、そのときは `IS_DEMO` を設定せずにそのフォルダーで `claude` を始め、信頼のダイアログを受け入れて新しいセッションで実行する、という段落も加わっています。Remote Control の節からは、`claude rc` を実行して `y` と答える方法が外れました。チームメイトに渡せない deny ルールのメッセージは `The deny rule "<rule>" cannot be handed to a teammate intact, so the teammate was not started. Remove that rule or move it to permissions.deny in settings, then try again.` になり、**Teammate mode** の行が `overridden` で、すでに `in-process` を示しているなら、値を一巡させて `in-process` に戻す、と加わりました — [日本語](https://code.claude.com/docs/ja/errors#workspace-not-trusted-when-running-claude-ultrareview) / [English](https://code.claude.com/docs/en/errors#workspace-not-trusted-when-running-claude-ultrareview)、[日本語](https://code.claude.com/docs/ja/errors#command-line-deny-rule-cannot-be-handed-to-a-teammate) / [English](https://code.claude.com/docs/en/errors#command-line-deny-rule-cannot-be-handed-to-a-teammate)
- **`CLAUDE_CODE_DISABLE_ULTRAREVIEW_TRUST_CHECK` の対象が広がった**（`env-vars`）。ターミナルなしか `CI=true` で実行した `claude ultrareview` が `Error: Workspace not trusted` で終わらないようにする変数で、`claude ultrareview` は尋ねられるときは尋ねます。v2.1.314 以降は `/ultrareview` と `/code-review ultra` の信頼の確認も飛ばす、と加わりました。`settings-reference` の「Variables Claude Code ignores in `env`」の、起動の環境からだけ読む変数の一覧にも、この変数と `CLAUDE_CODE_STRICT_INLINE_SHELL_RM_PROMPT` が加わっています — [日本語](https://code.claude.com/docs/ja/env-vars#variables) / [English](https://code.claude.com/docs/en/env-vars#variables)
- **`CLAUDE_CODE_STRICT_INLINE_SHELL_RM_PROMPT` が `env-vars` に載った**。Claude Code が確かめられない `-c` のスクリプトを、`rm` も `rmdir` も名指さないものを含め、より多く印付けする変数です。起動の環境で設定し、`CLAUDE_CODE_DISABLE_INLINE_SHELL_RM_PROMPT` が `1` のときは効かず、v2.1.299 以降が要ります（changelog の v2.1.299 にこの変数の言及があります） — [日本語](https://code.claude.com/docs/ja/env-vars#variables) / [English](https://code.claude.com/docs/en/env-vars#variables)
- **リモートの MCP サーバーの切断の通知と再試行の説明が改められた**（`mcp` の「Mid-session drops of a remote server」）。対話のセッションでサーバーを失敗と印付けしたときの通知が 2 つになり、`MCP server "<name>" disconnected · still retrying · open /mcp to reconnect now` なら Claude Code は最大約 1 日サーバーの再試行を続けうり、`/mcp` ではそのサーバーが `retrying` と示されます（再試行を止めるには `/mcp` からプロジェクトでそのサーバーを無効にする）。`MCP server "<name>" disconnected · open /mcp to reconnect` ならバックグラウンドでは再試行していません。`claude -p` と Agent SDK の一時的なエラーの後の再試行も、最大約 30 分に「一部のサーバーでは約 1 日」が加わりました。changelog の v2.1.327 にある、長めの障害の後にリモートの MCP サーバーが切断されたままになる問題の修正に追従した形です — [日本語](https://code.claude.com/docs/ja/mcp#mid-session-drops-of-a-remote-server) / [English](https://code.claude.com/docs/en/mcp#mid-session-drops-of-a-remote-server)
- **組織が `ask` にしたコネクターのツールと `requiresUserInteraction` の説明が改められた**（`mcp` の「Organization controls on connector tools」「Require approval for a specific tool」・`permissions` の「MCP」）。確認を求めるのは「Claude が行う呼び出しのたびに」となり、`dontAsk` モードに加えて、プロンプトに答えるもののない `-p` の実行でも Claude Code が呼び出しを拒む、と加わりました。`blocked` にしたツールの `/mcp` での印は `disabled by your organization` から `turned off by your organization` になっています — [日本語](https://code.claude.com/docs/ja/mcp#organization-controls-on-connector-tools) / [English](https://code.claude.com/docs/en/mcp#organization-controls-on-connector-tools)
- **許可のプロンプトのコメントの欄で `Tab` を押したときの説明が改められた**（`permissions` の「Add a comment when you answer a permission prompt」）。`Tab` は答えずに欄を閉じ、入力したテキストを送るには、答える前に `Tab` をもう一度押す、となりました（これまでは、入力したテキストは残り、その選択肢で答えれば送られる、としていました）。同じページの「Additional directories grant file access, not configuration」からは、`/add-dir` でサブディレクトリーを読み込むときに確認を求めない、という部分とその理由が外れています — [日本語](https://code.claude.com/docs/ja/permissions#add-a-comment-when-you-answer-a-permission-prompt) / [English](https://code.claude.com/docs/en/permissions#add-a-comment-when-you-answer-a-permission-prompt)
- **`permissions.ask` に一致しても承認なしに実行されうる場合が載った**（`settings-reference` の `permissions.ask`）。`PermissionRequest` のフックか mod が許せば、一致するツールの使用も承認なしに実行されうり、サンドボックスの自動許可があれば、サンドボックスの中のコマンドは裸の `Bash` の ask ルールを飛ばしうる、と加わりました。「Settings index」の説明も「常に確認を求める」から「確認を求める」になっています — [日本語](https://code.claude.com/docs/ja/settings-reference#permissions-ask) / [English](https://code.claude.com/docs/en/settings-reference#permissions-ask)
- **`/login` が保存した API キーと Anthropic のプロファイルの順位が載った**（`authentication` の「Anthropic profiles and federation credentials」）。`/login` が API キーを保存していて `CI` が設定されていなければ、Claude Code はこれらのソースではなくそのキーを使い、外すには `/logout` を実行する、と加わりました。表の列は「`/login` に対する順位」から「claude.ai のログインに対して」になり、`env-vars` の `ANTHROPIC_FEDERATION_RULE_ID` からも、フェデレーションの認証情報は `/login` の認証情報より上、という部分が外れています — [日本語](https://code.claude.com/docs/ja/authentication#anthropic-profiles-and-federation-credentials) / [English](https://code.claude.com/docs/en/authentication#anthropic-profiles-and-federation-credentials)
- **SSH と tmux の通知に `preferredNotifChannel` の設定が要らなくなった**（`terminal-config` の「Get a terminal bell or notification」「Configure tmux」）。tmux の外の SSH で Ghostty・Kitty・iTerm2 にデスクトップの通知を届けるには、`preferredNotifChannel` を既定の `"auto"` のままにし、v2.1.326 より前は `"iterm2"`・`"kitty"`・`"ghostty"` のいずれかにする、となりました。tmux でも `allow-passthrough` の行を残して Claude Code を再起動すれば足り、v2.1.326 より前か、`allow-passthrough` のない 3.3 より古い tmux では `preferredNotifChannel` を設定します。changelog の v2.1.326 にある、既定の設定で tmux の中と SSH 越しの iTerm2 に通知が送られない問題の修正に追従した形です — [日本語](https://code.claude.com/docs/ja/terminal-config#get-a-terminal-bell-or-notification) / [English](https://code.claude.com/docs/en/terminal-config#get-a-terminal-bell-or-notification)
- **Bash のツールが読むシェルの起動ファイルの説明が改められた**（`tools-reference` の「What persists between commands」・`claude-directory`）。Claude Code は対話でないシェルを始め、Zsh なら `~/.zshrc`、Bash なら `~/.bashrc` を読み、取り込んだエイリアス・関数・シェルのオプションを Bash のコマンドに当てる、となりました（`~/.profile` は外れました）。`claude-directory` の `shell-snapshots/` からも「起動時に取り込んだ」が外れています — [日本語](https://code.claude.com/docs/ja/tools-reference#what-persists-between-commands) / [English](https://code.claude.com/docs/en/tools-reference#what-persists-between-commands)
- **`WorktreeRemove` のフックの説明が改められた**（`hooks` の「WorktreeRemove」）。`claude remote-control` の後始末ではフックを確認なしに実行する、となり、`ExitWorktree` の呼び出しでも確認しないという部分と、フックがその経路の最後の確認になる、という部分が外れました（`ExitWorktree` が `discard_changes: true` なしにフックが作ったワークツリーの削除を拒むことは残っています） — [日本語](https://code.claude.com/docs/ja/hooks#worktreeremove) / [English](https://code.claude.com/docs/en/hooks#worktreeremove)
- **Agent SDK のフックの `updatedInput` の失敗の対処が載った**（`agent-sdk/hooks` の「Tool blocked unexpectedly」）。ツールの結果がフックについて `returned updatedInput that failed schema validation` か `returned updatedInput that the tool refused` と述べたら、そのフックの `updatedInput` を直します。`updatedInput` は入力全体を置き換えるので、変えない `tool_input` のフィールドも含めます — [日本語](https://code.claude.com/docs/ja/agent-sdk/hooks#tool-blocked-unexpectedly) / [English](https://code.claude.com/docs/en/agent-sdk/hooks#tool-blocked-unexpectedly)
- **managed settings の `permissions.deny` の注意書きが改められた**（`auto-mode-config` の「Where the classifier reads configuration」）。「ユーザーの意図や分類器の設定にかかわらず決して実行してはならない操作には、managed settings の `permissions.deny` を使う。分類器より前に止め、上書きできない」から、「分類器が動く前に Claude の一致する呼び出しを止めるには、managed settings の `permissions.deny` を使う」になりました。「Inspect the defaults and your effective config」の出力例の `soft_deny` も、`Git Destructive` のルールの代わりに `...` と `Production Deploy` のルールを示す形になっています — [日本語](https://code.claude.com/docs/ja/auto-mode-config#where-the-classifier-reads-configuration) / [English](https://code.claude.com/docs/en/auto-mode-config#where-the-classifier-reads-configuration)
- **マーケットプレイスの `github` のソースの `path` の説明が改められた**（`settings-reference` の「Allowed source types」「Exact matching」）。`path` は「サブディレクトリー」ではなく「リポジトリの中のマーケットプレイスのファイルのパス」となり、例も `"path": "marketplace"` から `"path": ".claude-plugin/marketplace.json"` になりました — [日本語](https://code.claude.com/docs/ja/settings-reference#allowed-source-types) / [English](https://code.claude.com/docs/en/settings-reference#allowed-source-types)
- **プラグインの画面とメッセージの文言の変更にページが追従した**（`plugins/troubleshooting`・`plugins/install`・`plugins/loading`・`plugins/host-marketplace`・`plugins/measure`・`plugins/org`・`plugins/cli-reference`・`security-guidance`）。`plugins/troubleshooting`・`plugins/host-marketplace` と `plugins/install` の「Add a marketplace」からは、`Successfully added marketplace: <name>` の出力で成功を確かめる説明が外れ、追加できたかは `/plugin marketplace list` か `/plugin` の **Marketplaces** のタブで確かめる、となりました（`plugins/install` のシェルからインストールする説明などには、この出力の例が残っています）。マーケットプレイスの自動更新は、**Enable auto-update** を選ぶのではなく、マーケットプレイスを選んでメニューを開いてオンかオフにする、となり、トグルが `autoUpdate` を書くのはユーザー・プロジェクト・ローカルの設定がそのマーケットプレイスを宣言しているとき、と明示されました。マーケットプレイスから外されたプラグインは **Flagged** の見出しではなく **Installed** のタブの **Needs attention** の下に並び、**Not used recently** のプラグインの詳細は `Last used:` の行ではなく最後に使った時刻を示します。`Plugin "<name>" not cached at <path>` が、リポジトリの設定だけが有効にしていてまだ入れていないプラグインにも出たのは v2.1.323 より前のこと、となり、managed settings が有効にした `security-guidance` のプラグインでは `/plugin` が **Disable plugin** と **Uninstall** を拒む（これまでは、管理者だけが無効にできる）、となっています。依存関係のエラーは読み込みのときは `/plugin` の **Errors** のタブに出て、表は代表的なメッセージを `claude plugin list` が出す形で引用する、となりました — [日本語](https://code.claude.com/docs/ja/plugins/troubleshooting#dependency-errors) / [English](https://code.claude.com/docs/en/plugins/troubleshooting#dependency-errors)、[日本語](https://code.claude.com/docs/ja/plugins/host-marketplace#uninstall-removed-plugins-from-users’-machines) / [English](https://code.claude.com/docs/en/plugins/host-marketplace#uninstall-removed-plugins-from-users’-machines)
- **Code Review の指摘の探し方が改められた**（`code-review-troubleshooting` の「Find issues that aren't showing as inline comments」・`code-review-pull-requests` の「Severity levels」）。行ではなくファイル全体へのコメントを PR の **Conversation** のタブで探す項目が加わり、**Additional findings** の見出しも **Conversation** のタブの Claude のレビューで探す、となりました（これまでは、行の位置がないか今の diff の外の指摘がレビューの本文のこの見出しの下に出る、としていました）。`code-review-pull-requests` も、Claude は各指摘を該当する行のインラインのコメントとして投稿する、という部分が外れ、各指摘に 3 つの重大度のいずれかの印を付ける、だけになっています — [日本語](https://code.claude.com/docs/ja/code-review-troubleshooting#find-issues-that-aren’t-showing-as-inline-comments) / [English](https://code.claude.com/docs/en/code-review-troubleshooting#find-issues-that-aren’t-showing-as-inline-comments)
- **Trusted Devices のベータの注記が外れた**（`remote-control` の「Trusted Devices」）。「Trusted Devices は現在ベータで、機能は変わりうる」という注記が外れました — [日本語](https://code.claude.com/docs/ja/remote-control#trusted-devices) / [English](https://code.claude.com/docs/en/remote-control#trusted-devices)
- サードパーティのプロバイダーの Opus 4.6 と Sonnet 4.6 で、plan モードと Bash のプロンプトが、新しいモデルと同じく auto モードを使い、提案するよう変更。`disableAutoMode` で両方をオフにできます
- Code Mode が、スクリプトの出力に対して UserPromptSubmit のフック（managed のものを含む）を実行しないよう変更。その出力を伏せるには、`updatedToolOutput` を使う PostToolUse のフックを使います
- ほとんどのモデルで、`/code-review` がバグと CLAUDE.md の違反だけを報告するよう変更。再利用・簡素化・効率の整理には `/simplify` を実行します
- ほとんどのモデルで、`/code-review` が各指摘に Important・Pre-existing・Nit の印を付け、各要約を修正の提案で締めるよう変更。問題のないレビューの一覧は「Code review found no issues.」になりました
- `claude.ai <name>` の形の `deniedMcpServers` のエントリが、クラウドとセルフホストのランナーのセッションでもそのコネクターに当てはまるよう変更
- managed の `PostToolUse` のフックが、実行前に拒まれた呼び出しには発火しないよう変更。そこではログの記録・書き換え・ブロック・停止が起きません。`PostToolBatch` はほとんどを受け取りますが、拒まれたという印は付きません
- `/bug` が送信の前に Yes か No を尋ねるよう変更。Enter の連打で報告が送られたり GitHub が開いたりしなくなりました
- `CLAUDE_CODE_FORK_SUBAGENT=0` を設定したとき、`claude -p`・Agent SDK・デスクトップ・VS Code のサブエージェントが、既定で自身のサブエージェントを待つよう変更
- `CLAUDE_CODE_FORK_SUBAGENT=0` の `claude -p` で、バックグラウンドのサブエージェントとそれが待つものを、1 つの 10 分の待ちに数えるよう変更。より長い連なりには `CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS` を上げます
- PermissionRequest のフックがサンドボックスの除外の対象のコマンドに書き換えたシェルのコマンドを、サンドボックスの外で実行するよう変更
- Claude in Chrome の歓迎の画面と `/chrome` が、権限モードか `/permissions` のルールが答えない限り、Claude がサイトで操作する前に Claude Code が尋ねる、と述べるよう変更
- サードパーティのプロバイダーか、テレメトリーか機能フラグがオフの Claude Desktop と Agent SDK のセッションが、質問を開いたまま閉じられたとき、答えなしに続けずにターンを終えるよう変更
- サードパーティのプロバイダーか、テレメトリーか機能フラグがオフのとき、貼り付けたテキストに、貼り付けたものだという Claude 向けの印を付けるよう変更
- Anthropic API のターミナルのセッションで、サブエージェントの進捗の要約を、既定の小さく速いモデルが短いメモから書くよう変更（テレメトリーがオフでも）。トークンを大幅に減らします
- `sandbox.failIfUnavailable` を設定していなければ、始められないサンドボックスの報告の仕方を変更。次のサンドボックスの中の Bash のコマンドが拒まれ、そのセッションではサンドボックスがオフだと述べます
- `/list-agents` が一覧をあなたにだけ示すよう変更。必要なときは Claude が自分でセッションを一覧にします
- セルフホストのランナー: 設定が Claude の GitHub のツールを名前で守っているところでは、組み込みの `gh api` を既定でオフにするよう変更。`--use-anthropic-gh true` でオンにできます
- セルフホストのランナー: セッション自身の `claude` が立ち上がる前か終わった後に、ラッパーのスクリプトが実行する `claude` には、Anthropic が管理する git を与えないよう変更
- セルフホストのランナー: `CLAUDE_RUNNER_SESSION_UUID` と `CLAUDE_CODE_REMOTE_SESSION_UUID` の両方を、セッションとその `checkout`・`post-session`・`spawn-runner` のフックに設定するよう変更
- `--capacity 1` のセルフホストのランナーが、プッシュ先のリポジトリのパスがシンボリックリンクのとき、より早くセッションを拒むよう変更
- `claude -p` と SDK のセッションで、自身の git リポジトリを持つ managed settings のプラグインを、後のセッションのためにバックグラウンドで取得するよう改善
- 新しいマシンの `claude -p`・SDK・Claude Desktop のセッションで、git のマーケットプレイスからの managed settings のプラグインが読み込まれるまでの早さを改善。短い実行は最大 30 秒遅く終わることがあります
- 大きなセッションの再開にかかる時間を改善
- 多くの画像を含むセッションを再開するときのメモリーの使用を改善
- 遅いコマンドかツールを実行する長い SDK とデスクトップのセッションで、メモリーの使用と応答の時間を改善
- auto と bypass permissions のモードで、ほとんどのスクリプトの後の 0.75 秒の間を除き、Code Mode の速さを改善
- MCP サーバーを持つ新しい Code Mode のセッションのプロンプトキャッシュを改善。サーバーがまだ接続中のときと、サーバーの一覧が変わったときに、Claude に伝わるようになりました
- ツールの説明を短くして、Code Mode のトークンの使用を改善
- Code Mode を改善。スクリプトが実行中のコマンドとその出力を、実行の間に示します
- Code Mode の編集を改善。何も変えない編集でスクリプトが止まらなくなり、失敗した編集が一致する場所か最も近い場所が Claude に伝わります
- Code Mode を改善。スクリプトが失敗したときにまだ実行中だったツールの呼び出しが Claude に伝わるようになりました
- Code Mode の auto と bypass のモードで、Claude が開発サーバーを始める方法を改善。`/tasks` に出るバックグラウンドのタスクとして実行するよう Claude に伝えます
- Windows: スクリプトのシェルのコマンドが Git Bash で実行されることと、同じ名前の関数の代わりに PowerShell のエイリアスが実行されることを Claude に伝え、Code Mode を改善
- 複数の in-process のチームメイトを一度に始める動きを改善。「Lock file is already being held」で失敗するものが大幅に減りました
- computer use の承認のダイアログを改善。各アプリのアクセスのレベルと、より平易な警告を示します
- セッション間のメッセージを改善。クラウドのセッションかほかのコンピューターが一覧にないとき、Remote Control がオフだと Claude が説明するようになりました
- `claude -p` のテキストの出力を改善。ほかのセッションからのメッセージが保留されたか落とされたことと、それを許可する方法を標準エラーに出します
- 公開したアーティファクトを誰が開けるかについての Claude の答えを改善。前回の公開の答えを繰り返さず、アーティファクトをもう一度確かめるよう Claude に伝えます
- 再開したセルフホストのランナーのセッションを改善。Claude が以前の作業がまだ残っているかを確かめ、欠けているものを述べるようになりました

**バグ修正**

- zsh の Bash のコマンドが、`echo ====` や `[ a == b ]` のような `=` で始まる語で「not found」のエラーで止まる問題を修正。`=cmd` はコマンドのパスに展開されなくなりました
- 自動のコンパクションが、`/compact` のように作り直さずに、セッションの以前のシステムプロンプトを使い回す問題を修正
- 一部の非常に長いか不正な形の入力で、Markdown の表示が固まる問題を修正
- まれな画面の固まりを修正
- 許可のプロンプトか質問で、Esc の直後に続けて入力すると、Esc がしばしば失われる問題を修正。Alt を Esc とキーとして送るターミナルでは、そこで使われていない Alt か Option のキーが断る操作になりました
- 遅い接続で 2 つに切れた貼り付けかターミナルの応答が、プロンプトに入力される問題を修正
- サードパーティのプロバイダーか、テレメトリーか機能フラグがオフのとき、スケジュールされたタスクのファイルが読めないと、タスクの保存でプロジェクトのほかの保存済みのタスクが消える問題を修正
- プロジェクトのスケジュールされたタスクのファイルで、タイプミスのあるタスクが、次にそのファイルを保存したときに削除される問題を修正
- メッセージの保存が遅れたとき、再開したクラウドのセッションがコンパクションの要約か最近のメッセージを失うことがある場合を修正
- スピナーとサブエージェントのトークン数が、再試行した返答を 2 回数え、ストリーミングされなかった返答を漏らし、Claude が考えている間止まったままになる問題を修正
- 応答の途中で使用クレジットが尽きたときに出るエラーが、レート制限を名指していた問題を修正
- Bedrock・Agent Platform・Foundry・Claude apps gateway で、ベータを拒むゲートウェイの背後で `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS` を設定していると、Claude Desktop の外で auto モードが毎ターン失敗する問題を修正
- ゲートウェイ・カスタムのベース URL・クラウドのプロバイダーで、`CLAUDE_STREAM_IDLE_TIMEOUT_MS` が 5 分の接続の上限を延ばさない問題を修正
- サードパーティのプロバイダーの一部の Claude Desktop のセッション（スケジュールされたタスクを除く）が、大きなツールの結果の後に「Prompt is too long」で終わったままになる問題を修正。最も大きいものは除かれるようになりました
- サードパーティのプロバイダーか、テレメトリーか機能フラグがオフのとき、入力のスキーマが `anyOf`・`oneOf`・`allOf` で始まる MCP のツールが消える問題を修正
- サードパーティのプロバイダーか、テレメトリーか機能フラグがオフのとき、不正な入力のスキーマを持つ MCP のツールが要求を失敗させる問題を修正。そのツールは除かれ、理由が Claude に伝わります
- Bedrock・Google Cloud の Agent Platform・Foundry がサブエージェントの進捗の要約の effort の設定を拒むと、そのセッションの間、サブエージェントのモデルの effort がオフになる問題を修正（2.1.327 での退行）
- auto か bypass のモードの外の許可のプロンプト・計画の承認・質問が 10 分開いたままだと、Code Mode がスクリプトを止める問題を修正
- auto と bypass permissions のモードで、前のスクリプトの実行中に接続した MCP サーバーを、Code Mode のスクリプトが呼べない問題を修正
- `claude --resume` のピッカーで選んだセッションで、auto か bypass permissions のモードの Code Mode のスクリプトがバックグラウンドで実行されない問題を修正
- 1 つの返答が複数のスクリプトを実行したセッションを再開すると、Code Mode が読み込んだスキル・フックのコンテキスト・許可の承認と一緒に入力したメモを失う問題を修正
- ピッカーから、または許可を求めるモードでセッションを再開したとき、Code Mode のスクリプトが途中で切れたことが Claude に伝わらない問題を修正
- 以前に失敗したスクリプトが設定しなかった最上位の変数に、Code Mode が何も言わずに `undefined` を使う問題を修正
- 失敗したコマンドの長い出力が切られたことが、Code Mode のスクリプトに伝わらない問題を修正
- `{` のブロックで始まる正しいスクリプトを Code Mode が拒む問題を修正
- 最上位の `await` と最上位の `return` の両方を使うスクリプトを Code Mode が拒む問題を修正
- スクリプトが読むか書いた後、Code Mode で @-メンションした小さなファイルが添付されない問題を修正
- 呼び出せない読み取り専用のサブエージェントに、Code Mode が `write()` と `edit()` を提供する問題を修正
- Code Mode で Esc の後に `/model` のようなコマンドを続けると、Claude が自らターンを始める問題を修正
- Code Mode の Claude に、頼まれたときだけワークフローを実行することと、`/config` で設定したワークフローの規模が伝わらない問題を修正
- Remote Control が同じ切断のメッセージを繰り返し、再接続できないセッションの再試行を勧める問題を修正
- サービスが遅い間にリモートのセッションが再起動すると、待っている許可のプロンプトが失われ、その答えが無視される問題を修正
- 巻き戻しの後に `/clear` すると、クラウドのセッションが消した会話を再開する問題を修正
- 途切れたモデルのストリームを再試行した後にランナーかワーカーが失われると、リモートのセッションがターンのツールの呼び出しと結果を失う問題を修正
- 始まったばかりか、タイトルに @ を含むクラウドと Remote Control のセッションに、Remote Control がオンのセッションからセッション間のメッセージで届かない問題を修正
- クラウドのセッションは決して返信できないと Claude に伝わる問題を修正。返信が来うるときと、結果を得るほかの方法が伝わるようになりました
- コマンドが別のリポジトリに移った後、`/diff`・Remote Control のセッションの Changes のペイン・編集の横の diff が、コミット済みの作業を除く問題を修正
- IDE の拡張機能かほかの SDK のアプリが実行するセッションを、ワークフローが最後に進んでから 1 時間以上たって開くと、Remote Control が実行中のワークフローのエージェントを示さない問題を修正
- Remote Control: Remote Control をオンにした後、アイドルの Desktop か VS Code のセッションが実行中と示される問題を修正
- SDK の中断がバックグラウンドのエージェントを止めた後も、まだ実行中だとモデルが述べる問題を修正
- デスクトップアプリと SDK のホストの Send now が、止めた Web 検索について結果が見つからなかったと Claude に伝える問題を修正
- Cmd を報告するターミナルで、Cmd+文字がプロンプトに入力される問題を修正
- フルスクリーンのモードで、GNOME Terminal の Ctrl+クリックがリンクを 2 回開く問題、マウスのサイドボタンがクリックとして働く問題、間を置いた後の逆方向へのホイールの最初の 1 目盛りが無視される問題を修正
- tmux と ssh の外の Konsole での Shift+Enter と、kitty のキーボードのプロトコルを話すターミナルでの、ラテン文字以外のキーボードの配列の Alt のショートカットを修正
- Linux: `xclip` か `wl-copy` が入っているとき、Claude Code を Ctrl+Z で一時停止している間、ほかのアプリでの貼り付けが固まる問題を修正
- Linux: Ctrl+V がクリップボードの画像を取りこぼす、古い画像を貼り付ける、ハングする問題を修正
- フルスクリーンのモードでコピーしたテキストが、引用の縦線を含む、ドラッグで上にスクロールしたときに折り返しの位置の空白を失う、「Jump to bottom」の表示の下の語を欠く問題を修正
- `!` のコマンドに貼り付けた画像のパスが添付になる問題を修正
- `?` のショートカットの一覧を開いている間、Ctrl+C が終了の警告を出さない問題を修正
- キーがまとめて届いたとき、フルスクリーンのモードの Ctrl+R の検索と `/theme` の色のエディターが間違った行を選ぶ問題と、そこと `/config`・`/plugin` の検索でキーが落ちる問題を修正
- GNU screen の中で色が間違うか欠ける問題を修正
- フルスクリーンのモードで、多くのバックグラウンドの通知が開いているダイアログの上の枠に食い込む問題を修正
- バックグラウンドのエージェントへのメッセージが、貼り付けた画像の代わりに長いファイルのパスを示す問題を修正
- 文言が同じとき、`/goal` がスキルの Stop のフックを外すか、別のフックの結果で早く終わる問題を修正
- 報告を送った後に `/bug` が取り消したと述べる問題を修正
- Pro と Max のユーザーで、Esc がトランスクリプトの共有の質問を閉じない問題を修正
- 戻るときに `/hooks` が位置を失う問題を修正
- 名前を空にしたとき、`/export` が `.txt` という名前のファイルを書く問題を修正
- Zed で `/terminal-setup` が、シンボリックリンクの `keymap.json` を普通のファイルに置き換える問題を修正
- 既存のワークフローのファイルの更新を頼んだとき、`/install-github-app` がコードレビューのワークフローを加える問題を修正
- 戻った後に遅い保存か削除が終わると、`/plugin` がスキルを開き直すか、開いているページを閉じる問題を修正
- 変更の実行中にプラグインを離れた後、`/plugin` が間違ったプラグインのアンインストールを尋ねるか、Esc を無視する問題を修正
- 結果のない検索かタブの行のクリックの後、`/plugin` の Installed のタブで入力と矢印キーが効かない問題を修正
- `/plugin` で Enter を押し続けると、インストール済みの複数のプラグインがオフになる問題を修正
- 1M コンテキストのモデルで `/usage` のプラグインの合計が 2,000 トークンで止まる問題と、モデルを選んでいないときの `/usage` と `/plugin` のトークンの見積もりが低い問題を修正
- Bedrock のアクセスキーの手順で、Esc が戻る代わりに `/login` を閉じる問題を修正
- `/exit` と Ctrl+D が実行中の作業を違うように述べる問題と、`/exit` が止まったワークフローについて警告する問題を修正
- 共有フォルダーのアーティファクトを読んだ後か、別の組織のフォルダーに公開した後に、Claude がアーティファクトを非公開と呼ぶ問題と、フォルダーの人も開けるのに名指しした人だけが開けると述べる問題を修正
- プラグインのトーストに別のプラグインのテキストが出ることがある問題を修正
- ターンの開始直後に保存した mod が、ターンの終わりではなく途中で再読み込みされることがある問題を修正
- `OTEL_RESOURCE_ATTRIBUTES` の 1 つの不正なエントリが、メトリクスのポイント・イベント・スパンからその変数のほかのラベルを落とす問題を修正。そのエントリだけが除かれるようになりました
- 要求が大きすぎるとして拒まれた後のコンパクションの間、エージェントのフックがタイムアウトを過ぎても実行される問題を修正
- `FORCE_COLOR` が負の数に設定されているときの起動時のクラッシュを修正
- マシンのメモリーが尽きかけているときの、秘密のマスクでのクラッシュを修正
- ブランチ名が正しい UTF-8 でないとき、Linux の Bash のサンドボックスが各コマンドの後に `.git/HEAD` の名前を変える問題を修正
- セルフホストのランナー: プロキシか Web のフィルターがポーリングに HTTP 200 と `{}` のような本文で答えると、実行中のすべてのセッションが止められる問題を修正。ランナーはそのようなポーリングを再試行するようになりました
- セルフホストのランナー: 一時的なディスクのエラーの後、残したクローンのオブジェクトか ref と、そこにしかないコミットが削除される問題を修正。代わりにその起動が失敗するようになりました
- 時計が遅れているか巻き戻されたホストで、トークンが切れるとセルフホストのランナーが止まる問題を修正
- セルフホストのランナー: セッションの中のスクリプトかフックが `claude` を再び実行した後、Anthropic が管理する git を持つセッションが GitHub への git のアクセスを失う問題を修正
- マシンの git の設定が `http.proactiveAuth` を設定しているところで、Anthropic が管理する git を持つセルフホストのランナーがフェッチもプッシュもできない問題を修正
- セルフホストのランナー: 登録した後にセットアップが失敗すると、ランナーがサーバーに伝えずに終わる問題を修正。理由を付けて登録を外し、オンデマンドのランナーは失敗した起動を報告するようになりました
- セルフホストのランナー: 別のセッションが同じリポジトリを準備するのを待っている間（`--capacity` が 1 より大きいとき）、セッションのアーカイブかキューへの戻しが効かない問題を修正
- セルフホストのランナー: `--trust-workspace false` の下で、壊れた `.claude.json` を持つセッションが以後のすべての起動に失敗する問題を修正。既定の値で始まり、そこでオフにした MCP サーバーは再びオンになります
- セルフホストのランナー: checkout のフックか git が多くを出力したとき、失敗した起動のメッセージが、何が失敗したかを述べる語を失う問題を修正
- ディスクが数秒止まったとき、セルフホストのランナーが post-session のフックを飛ばす問題を修正。応答しないディスクでは、既定でセッションの終了が 25 秒長くかかることがあります
- セルフホストのランナーを修正。新しい Claude の設定ディレクトリーで再開したセッションが、タスクの一覧を失わなくなりました
- セルフホストのセッションがリポジトリの 1 つなしに始まったとき、そのことと理由が Claude に伝わらない問題を修正
- セルフホストのランナー: `claude --environment` の `--correlation-id` が `spawn-runner` のフックに届かない問題を修正
- セルフホストのランナーのセットアップのウィザードのキーのローテーションの助言を修正。キーを取り消すと、その下で実行中のセッションが止まると警告するようになりました
- [VSCode] パネルが低いとき、またはコマンド・URL・説明が長いとき、許可のプロンプトが No のボタン・返信の欄・タイトルを切る問題を修正
- [VSCode] 失敗したか止められたツールの呼び出しが理由を示さないか短く切れた理由を示す問題と、Glob と Grep がエラーを結果として数える問題を修正

**その他**

- **見出しの改称**: 5 つの見出しが、メッセージの文言の変更に合わせて改称されました。`plugins/troubleshooting` の h3 は `Failed to install: <plugin> (<reason>)` が `Couldn't install: <plugin> (<reason>)` or `Failed to install: <plugin> (<reason>)` に、`Plugin "<name>" is enabled in project settings but isn't installed here` が `Plugin "<name>" is on in project settings but isn't installed here` に、`Failed to load hooks from <path>` and hooks that don't fire が `Couldn't load hooks from <path>` and hooks that don't fire に、`sandboxing` の h3 は `/sandbox` fails with `Sandbox settings are overridden by a higher-priority configuration` が `/sandbox` fails with `Sandbox settings can't be changed here` に（メッセージは `Sandbox settings can't be changed here. Higher-priority settings override them.`）、`plugins/mods/troubleshoot` の h3 は `Stopped: type a message to continue; a mod cannot resume work after Stop` が `stopped · type a message to continue` になりました（id は下の「参考リンクについて」参照）
- **メッセージの文言の更新**: `plugins/troubleshooting`（`Invalid marketplace source format` か `That isn't a marketplace source`、`Couldn't load hooks from <path>: <reason>` か `Failed to load hooks from <path>: <reason>` は `<reason>` が名指す問題を直す）、`plugins/install`（バンドルした MCP サーバーの設定が要るときのメモは `Its bundled MCP server needs` で始まり、読み込みの失敗の要約は `The plugin couldn't` を含む）、`plugins/loading`・`plugins/org`（`isn't installed here` で終わる行）、`plugins/cli-reference`（`run /reload-plugins to apply` の印と、`installed in this project` で終わるメッセージ）、`interactive-mode`（プラグインがこのプロジェクトに入っていないと述べる）、`sandboxing`（`Sandboxing needs WSL2` か `Sandboxing requires WSL2`）、`errors`（`path couldn't be checked` / `path could not be checked`、`Can't restart while work is running in the background`・`cannot be handed to a teammate intact` を短い形で引用）、`voice-dictation`（`Turned on voice mode (hold)`）、`remote-control`（コネクターを再び認可したときに、ターミナルでは `claude.ai Slack` に再接続したと述べる）、`mcp-quickstart`（アコーディオンの題が「/mcp shows No MCP servers」に）、`web-quickstart`（`/web-setup` が使えないと述べる場合も加わった）、`worktrees`（`its recorded path` で始まる場合は、そのパスのフォルダーを開けなければアクセスを戻し、そうでなければローカルのパスにワークツリーを作り直す）、`plugins/mods/api`（トーストを `type a message to continue` と呼ぶ）
- **Claude in Chrome の `/chrome` の操作の言い方**: `chrome` と `settings-reference` の `claudeInChromeDefaultEnabled` で、`/chrome` の **Select browser…** と **Enabled by default** を選ぶ説明が、別のブラウザーを選ぶ、Chrome を既定でオンにする選択肢を選ぶ、という言い方になりました。プロジェクトの設定で Chrome をオンにできない場合の項目からは、後で始めるセッションに当てはまり実行中のセッションには当てはまらない、という文が外れています
- **外れた文**: `plugin-evals`（インストールされていてもバックエンドがないと名指す）、`vs-code`（組み込みの IDE の MCP サーバーが十数のツールを持ち、残りは差分を開く・選択を読む・ファイルを保存するといった CLI の内部の RPC である、という説明）、`fullscreen`・`commands`（`/tui` で会話を保ったまま再起動する、という部分）、`permissions`（権限のルールの指定子の中の括弧はリテラルなのでエスケープは要らない）、`plugins/mods/api`（予定のジョブが来るかモニターがイベントを上げたときにトーストが出る、という文）、`plugins/measure`（「Find plugins you no longer use」へのリンク）、`sub-agents`（フロントマターに問題のあるファイルをセッションで報告せずに飛ばす、の「報告せずに」）
- **字句の小さな修正**: `artifacts`（公開で共有したアーティファクトを変える前に「会話ごとに 1 回」が「会話ごとに少なくとも 1 回」に）、`claude-apps-gateway`（ハイライト 2 参照）、`cross-session-messaging`（ハイライト 3 参照）、`mcp`（`/tasks` の詳細の表示を引用せず、終了後も実行が続くと述べる、という言い方に）、`sandboxing`（「folder」が「directory」に）
<!-- light:minor-updates:end -->

見出しマップ（`en/claude_code_docs_map.md`）は、更新時刻が 2026年11月18日 01:22:40 UTC から 2026年11月19日 02:17:59 UTC に替わり、12 行が加わり 6 行が外れました（6,633 行から 6,639 行）。加わったのは、`llms-full.txt` に加わった 6 つの見出しと改称した 5 つの見出しと新しいスタンプで、外れたのは改称前の 5 つの見出しと古いスタンプです。今回、見出しマップにだけ先に載った見出しはありません。

**参考リンクについて**: 日本語版は、今回リンクを付けたページの HTML を取得し、新しい節の id があるか、今回の差分で出入りしたコードの字句（変数名・版の数字・パス・リンク先・メッセージの文字列。base と head の `llms-full.txt` で数が違うものだけ）が英語版と同じだけあるかで、今回の内容になっているかを確かめました。`overridden` や `classic` のような訳文の中にも出る語や、地の文だけの変更（`code-review-troubleshooting`・`code-review-pull-requests`・`model-config`・`mcp` の `-p` の文など）は、該当する箇所の訳文で確かめています。今回リンクを付けたページは、すべて今回の内容になっていました。アンカーは英語版・日本語版の HTML の見出しの id で確かめました。改称した見出しには、改称後の文字列から作るスラッグとは違う id が付いています。`plugins/troubleshooting` の「`Couldn't install: <plugin> (<reason>)` or …」は `#failed-to-install-from-the-plugin-menu`、「`Plugin "<name>" is on in project settings but isn't installed here`」は `#plugin-is-enabled-in-project-settings-but-isnt-installed-here`、「`Couldn't load hooks from <path>` and hooks that don't fire」は `#failed-to-load-hooks-from-and-hooks-that-dont-fire`、`sandboxing` の「`/sandbox` fails with `Sandbox settings can't be changed here`」は `#sandbox-settings-overridden`、`plugins/mods/troubleshoot` の「`stopped · type a message to continue`」は `#stopped-type-a-message-to-continue` です。`sub-agents` の「Set the auto-compact window for one subagent」は `#subagent-auto-compact-window` を指しています。`plugins/host-marketplace` と `code-review-troubleshooting` の見出しの id には曲がった引用符（’）が含まれ、そのまま使っています。**changelog ページへのリンクは、本サマリの方針どおり付けていません。**

## 新着情報

<!-- light:whats-new:start -->
（今回の差分に新着情報（`whats-new/`）のページはありません。head の `llms.txt`・`llms-full.txt`・見出しマップにも whats-new のページは載っていません）
<!-- light:whats-new:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-11-17.md](./archives/latest/2026-11-17.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-11-17.md](./archives/latest-detail/2026-11-17.md)

<!--
base_commit: ab0340993aa5987d27a891141698d57dc355b88b
head_commit: 831f1678213f7b2708b300fbfd4e73aa7b6ac427
generated_at_full: 2026-11-19T15:20:45+09:00
-->
