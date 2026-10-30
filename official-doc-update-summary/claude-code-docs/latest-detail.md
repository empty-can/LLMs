---
対象期間: 2026年10月28日 〜 2026年10月29日
作成日: 2026-10-29
---

# Claude Code 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
**今回は changelog に v2.1.314（2026年10月30日）の 1 リリースが積まれ（v2.1.313 の項目はありません）、通常のページには、npm 12 で入れると Claude Code のバイナリーが置かれない場合の直し方、effort のレベルの解決順の 5 段階への書き直しとスキルの effort が効く範囲の整理、セルフホスト環境で GitHub 以外の git ホストのリポジトリのセッションを始める手順、Claude Desktop のサインインを組織に限る `forceLoginOrgUUID` のポリシー、更新を適用してセッションを再開する `/restart` が載りました**。新しいページはなく、228 ページ中 40 ページ（changelog を含む）が変わり、changelog を除く変更はページ単位で 320 行（追加 234・削除 86）、大幅更新は `self-hosted-environments-deploy` の 1 ページです。見出しマップに加わった 9 の見出しは、すべて `llms-full.txt` にも入っています。総行数は 126,019 行から 126,302 行に増えました。

主要なものを以下に挙げます。

1. npm 12 は既定で Claude Code の postinstall の手順を飛ばすので、`claude` が `Error: claude native binary not installed.` と出す場合の直し方（ネイティブインストーラーへの切り替えか、npm の `allow-scripts` への追加）が `troubleshoot-install` に載り、`setup` の npm のインストールにも注記が付いた
2. `model-config` の effort の解決順が、環境変数・セッションで選んだレベル・`--effort`・設定・モデルの既定の 5 段階になり、スキルの `effort` はそのターンの終わりまで効くことと、ステータスライン・フック・Agent SDK に出るレベルの意味も整理された
3. セルフホスト環境で、GitHub 以外の git ホストのリポジトリのチェックアウトから `claude -p --environment` でセッションを始める手順と要件（`origin` のパスは `<owner>/<name>` の形など）が `self-hosted-environments-deploy` に載った
4. Claude Desktop のポリシーに `forceLoginOrgUUID` を設定して、サインインできる claude.ai の組織を限る方法（Claude Desktop v1.2581.0 以降）が `desktop` と `hipaa-setup` に載った
5. 更新を適用してセッションを再開する `/restart`（エイリアス `/update`・Pro か Max・macOS か Linux のネイティブインストール・v2.1.288 以降）が `commands` に載り、再起動できないときのエラーの節もできた
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**npm 12 で入れると Claude Code のバイナリーが置かれない場合の直し方が載った**](#1-npm-12-で入れると-claude-code-のバイナリーが置かれない場合の直し方が載った):  
  `troubleshoot-install` に h4「Fix an npm 12 install」ができ、npm 12 は npm の設定で許していない限りバイナリーを置く postinstall の手順を飛ばすので、ネイティブインストーラーに切り替えるか、ユーザーの npm の設定の `allow-scripts` に Claude Code を加えて入れ直す、と載りました。原因の一覧の先頭にも npm 12 が加わり、`setup` の「Install with npm」にも注記が付いています
2. [**effort のレベルの解決順が 5 段階になり、スキルの effort が効く範囲と各所に出るレベルの意味が整理された**](#2-effort-のレベルの解決順が-5-段階になりスキルの-effort-が効く範囲と各所に出るレベルの意味が整理された):  
  `model-config` の解決順が、`CLAUDE_CODE_EFFORT_LEVEL`・セッションで選んだレベル・`--effort`・設定・モデルの既定の 5 段階に書き直され、スキルの `effort` はそれが動くターンの終わりまで効く、と改められました。ステータスラインの `effort.level` はセッションに設定したレベル、フックの `effort` はスキルなどのレベルを含む、と書き分けられ、Agent SDK の `applyFlagSettings()` の `effortLevel` は managed settings のものも置き換える例外になっています
3. [**セルフホスト環境で、GitHub 以外の git ホストのリポジトリでセッションを始められると載った**](#3-セルフホスト環境でgithub-以外の-git-ホストのリポジトリでセッションを始められると載った):  
  `self-hosted-environments-deploy` に h3「Start a session on a repository outside GitHub」ができ、そのリポジトリのチェックアウトの中で `claude -p` を `--environment` 付きで実行してセッションを始める手順と、資格情報・git のプロキシ・`origin` のアドレス・ブランチの要件が載りました。`self-hosted-environments` と `claude-code-on-the-web` の制限の記述も追従しています
4. [**Claude Desktop のサインインを組織に限る forceLoginOrgUUID のポリシーが載った**](#4-claude-desktop-のサインインを組織に限る-forceloginorguuid-のポリシーが載った):  
  `desktop` に h4「Restrict sign-in to your organization」ができ、Claude Desktop のポリシーで `forceLoginOrgUUID` を設定すると、サインインできる claude.ai の組織を限れる（Claude Desktop v1.2581.0 以降）と載りました。Claude Code の managed settings の同じキーでは Claude Desktop のサインインの画面は変わらないので、`hipaa-setup` にも h3「Restrict Claude Desktop sign-in」ができています
5. [**更新を適用してセッションを再開する /restart が載った**](#5-更新を適用してセッションを再開する-restart-が載った):  
  `commands` の表に `/restart`（エイリアス `/update`）の行が加わり、インストール済みの更新を適用して Claude Code を再起動し、このセッションを再開する、Pro か Max のプランと macOS か Linux のネイティブインストールが要る（v2.1.288 以降）と載りました。`errors` に再起動できないときの h3 ができ、`env-vars`・`interactive-mode` も追従しています
<!-- light:highlight-list:end -->

## 1. npm 12 で入れると Claude Code のバイナリーが置かれない場合の直し方が載った

**`troubleshoot-install` に h4「Fix an npm 12 install」ができました。** npm でインストールか更新をした後に `claude` が `Error: claude native binary not installed.` と出すか、Windows でシェルがそれを実行できないなら、`npm --version` を実行します。12 で始まるなら、npm の設定で許していない限り、npm はバイナリーを置く Claude Code の postinstall の手順を飛ばしています（ほかの版なら、ほかの原因を確かめる）。直し方は 2 つです。

- **ネイティブインストーラーに切り替える**: ネイティブインストーラーで入れてから npm のパッケージを外す。更新に npm を使わなくなるので、エラーは戻らない
- **npm のままにする**: グローバルの npm のインストールなら、ユーザーの npm の設定の `allow-scripts` に Claude Code を加える。npm はその後のインストールと更新のたびに、また `package.json` が `allowScripts` を設定していないプロジェクトのインストールでも、Claude Code のインストールスクリプトを動かす

npm のままにする手順は次の 4 つです。12.0.x なら npm を 12.1 以降に上げます（12.0.x では、`npx` のツールか `npm run` のスクリプトが始めるプロジェクトのインストールが、設定を保存すると `EALLOWSCRIPTS` で失敗しうる）。次のコマンドは値全体を置き換えるので、`npm config get allow-scripts` で今の一覧を控えてから `npm config set "allow-scripts=@anthropic-ai/claude-code" --location=user` で保存します（控えたパッケージも引用符の中に並べる）。`npm install -g @anthropic-ai/claude-code` で入れ直し、`claude --version` が版を出さなければほかの原因を確かめます。入れ直すか npm を上げるときに `EACCES` で失敗したら、`sudo` で再実行せずにネイティブインストーラーに切り替えます（Claude Code は自分を更新するとき `sudo` なしで npm を動かすので、自動の更新も同じく失敗する）。`~/.claude/local` へのローカルのインストールと、`npm install` を呼ぶ `package.json` のスクリプトを pnpm 9・pnpm 10・Yarn 1 などで動かす場合も、ネイティブインストーラーを使います（npm 12.1 以降では、設定を保存するとそれらのインストールが `EALLOWSCRIPTS` で失敗しうる）。元に戻すには、`@anthropic-ai/claude-code` を除いて一覧を設定し直すか、`npm config delete allow-scripts --location=user` で一覧ごと消します（npm 12 では、次の更新の後にエラーが戻る）。

同じページの「Native binary not found after npm install」では、原因の一覧の先頭に「npm 12 は既定で postinstall の手順を飛ばす」（npm 12 で入れるか更新すると、npm はその手順を動かさないままインストールを終える）が加わり、冒頭の説明も、`@anthropic-ai/claude-code` のパッケージの postinstall の手順がプレースホルダーをバイナリーで置き換えるまで `claude` はプレースホルダーのスクリプトだ、と言い換えられました。「npm install errors in WSL」と「npm `ENOTEMPTY` error during update or reinstall」にも、npm 12 なら新しい h4 に従う、という一文が加わっています。`setup` の「Install with npm」の冒頭にも、`npm --version` が 12 で始まるなら代わりに新しい h4 に従い、`sudo` で入れない（`sudo` が要るインストールは自動で更新できない）という注記が付きました。changelog に対応する項目はありません。

- [インストールとログインのトラブルシューティング - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/troubleshoot-install#fix-an-npm-12-install)
- [Troubleshoot installation and login - Claude Code Docs (English)](https://code.claude.com/docs/en/troubleshoot-install#fix-an-npm-12-install)
- [高度なセットアップ - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/setup#install-with-npm)
- [Advanced setup - Claude Code Docs (English)](https://code.claude.com/docs/en/setup#install-with-npm)

## 2. effort のレベルの解決順が 5 段階になり、スキルの effort が効く範囲と各所に出るレベルの意味が整理された

**`model-config` の「Adjust effort level」で、セッションの effort のレベルを決める順が 3 段階から 5 段階に書き直されました。** これまでは 1 段目の「明示的な選択」に `CLAUDE_CODE_EFFORT_LEVEL` の環境変数・`--effort` での起動・セッションの `/effort` が並んでいましたが、今は次の順で、最初に当てはまるものを使います。セッションで選んだレベルが、`--effort` での起動より上に置かれています。

1. `CLAUDE_CODE_EFFORT_LEVEL` の環境変数
2. セッションで選んだレベル（`/effort`・`/model` のピッカー・Agent SDK の `applyFlagSettings()` など）
3. `--effort` を付けた起動
4. 設定（モデルに保存したレベルか `effortLevel` のキー）
5. モデルの既定の effort（組織の既定のモデルに組織が既定の effort を決めていれば、そのモデルではそれが既定）

「Set the effort level」の `/model` の項目には、新しいレベルは遅くとも次のメッセージから効き、それまでは新しいモデルでも Claude が古いレベルで作業を続けうること、`CLAUDE_CODE_EFFORT_LEVEL` のように選んだレベルより上のソースが効いている間はそのソースのレベルで動くこと、が加わりました。フロントマターの段落も書き直され、スキルの `effort` はそれが動くターンの終わりまで（`context: fork` なら fork したサブエージェントの実行の間）、サブエージェントの `effort` はそのサブエージェントが動く間（呼び出しが上書きしない限り）効き、その間は起動時・保存・選択のどのレベルよりもそのレベルで動き、`CLAUDE_CODE_EFFORT_LEVEL` を設定していればそちらが効く、となっています（これまでは「そのスキルかサブエージェントがアクティブな間効き、セッションのレベルを上書きするが環境変数は上書きしない」）。`skills` のフロントマターの表の `effort` も「現在のターンの残りの effort。セッションのレベルを上書きするが `CLAUDE_CODE_EFFORT_LEVEL` は上書きしない。`context: fork` なら fork したサブエージェントの effort を設定する」に改められました。

**各所に出る effort のレベルの意味も書き分けられました。**

- **ステータスラインの `effort.level`**（`statusline`）: セッションに設定したレベルで、スキル・サブエージェント・`ultrathink` が設定したものではない。モデルが対応しないレベルを設定したなら実際に動いたレベルを示し、変えたレベルは効き始める前から示し、`CLAUDE_CODE_EFFORT_LEVEL` にレベルがあればそれを示す（これまでは「今の推論の effort。セッション中の `/effort` の変更を含む生きた値」）
- **フックの入力の `effort`**（`hooks` の「Common input fields」）: スキル・サブエージェント・`ultrathink` のレベルを含む、フックが動くときの effort のレベルの設定。モデルが対応しないレベルなら動いたレベルになり、変えたレベルは効き始める前にここに出ることがあり、`$CLAUDE_EFFORT` も同じレベルを持つ。`env-vars` の `CLAUDE_EFFORT` も「効いている effort のレベル」から「effort のレベルの設定」に言い換えられた
- **Agent SDK**（`agent-sdk/typescript`）: `applyFlagSettings()` の `effortLevel` は「次のターンで適用」から外れて新しい「次のターンまでに適用」の項目になり、Claude Code の次のモデルの呼び出しから効く（Claude Opus 5.5 を API キーか Claude のサブスクリプションで使うときのように、effort を変えてもプロンプトキャッシュが保たれるなら次のターンから）。渡したレベルは `--effort` や設定（managed settings を含む）のものを置き換える例外だ、と加わり、「Settings precedence」の「managed のポリシーの設定はプログラムのオプションより優先される」という文も、同じキーなら managed の値が効くが `applyFlagSettings()` に渡した `effortLevel` などの例外がある、と改められた。`SDKSystemMessage` の `effort` も「次の要求で送るレベル」から「次のターンに設定したレベル」になった

`model-config` の「Check the effort level you set」のフッターの文と「Effort level after a fallback」の `/effort status` の文も「セッションに設定したレベル」という言い方にそろえられ、`prompt-caching` の「Changing effort level」は「When a new effort level starts」へのリンクを持つ言い方になりました。changelog に対応する項目はありません。

- [モデル設定 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/model-config#adjust-effort-level)
- [Model configuration - Claude Code Docs (English)](https://code.claude.com/docs/en/model-config#adjust-effort-level)
- [ステータスラインをカスタマイズする - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/statusline#available-data)
- [Customize your status line - Claude Code Docs (English)](https://code.claude.com/docs/en/statusline#available-data)

## 3. セルフホスト環境で、GitHub 以外の git ホストのリポジトリでセッションを始められると載った

**`self-hosted-environments-deploy` に h3「Start a session on a repository outside GitHub」ができました。** GitHub 以外の git ホストのリポジトリでセッションを動かすには、そのリポジトリのチェックアウトの中で、ターミナルからセッションを始めます。先に次を確かめます。

- **git の資格情報とネットワーク**: ランナーがクローンするアドレス `https://<host>/<owner>/<name>` に対して確認なしで通る資格情報を用意し、ランナーが git ホストに届くようにする。SSH しか受け付けない git ホストなら `--git-ssh-rewrite` を見る
- **git のプロキシ**: 環境のランナーが Anthropic の git プロキシを使っているなら、オフにする
- **リポジトリのアドレス**: チェックアウトの `origin` のリモートのホストは `git.example.com` のようなドメイン名で、パスは `<owner>/<name>` の形でなければならない。`group/subgroup/name` のような入れ子のパスは通らない
- **ブランチ**: ランナーはそのブランチをクローンするので、今いるブランチを git ホストに push しておく

チェックアウトの中で、「Authenticate from CI」のとおりに claude.ai にサインインした状態で、`--environment` と環境の `ccpool_...` の ID を付けて `claude -p` を実行します（例: `claude -p "Fix the login bug" --environment ccpool_abc123 --output-format json`）。セッションができると `{"ok":true` で始まる 1 行の JSON を出し、`origin` のリモートが合わなければ `requires a git source, but no GitHub remote was detected` で失敗します。セッションが push したブランチは、git ホストでレビューしてマージします。

`self-hosted-environments` の「Availability and limitations」の「Repositories」も、セッションは GitHub か GitHub Enterprise Server からリポジトリをチェックアウトし、`--environment` のディスパッチで始めたセッションはほかの git ホストも使える、と改められ、GitHub・GitHub Enterprise Server・ほかの git ホストの 3 つの子項目になりました（これまでは GitHub からチェックアウトする、だけ）。`claude-code-on-the-web` の「Limitations」の「Platform restrictions」も、GitHub が要るのは Anthropic がホストする環境でのリポジトリのクローンとプルリクエストの作成だ、と改められ、セルフホスト環境の子項目からこの h3 へ案内されています。changelog の v2.1.314 には、セルフホストのランナーで、セッションのブランチが git のリモートにないときのエラーが、一度も push していないブランチも扱い、それぞれの直し方を示すようになった、という改善があります。

- [本番環境へのセルフホスト環境のデプロイ - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/self-hosted-environments-deploy#start-a-session-on-a-repository-outside-github)
- [Deploy self-hosted environments to production - Claude Code Docs (English)](https://code.claude.com/docs/en/self-hosted-environments-deploy#start-a-session-on-a-repository-outside-github)
- [自己ホスト環境 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/self-hosted-environments#availability-and-limitations)
- [Self-hosted environments - Claude Code Docs (English)](https://code.claude.com/docs/en/self-hosted-environments#availability-and-limitations)

## 4. Claude Desktop のサインインを組織に限る forceLoginOrgUUID のポリシーが載った

**`desktop` の「Device management policies」に h4「Restrict sign-in to your organization」ができました。** Claude Desktop にサインインできる claude.ai の組織を限るには、Claude Desktop のポリシーで `forceLoginOrgUUID` を設定します（Claude Desktop v1.2581.0 以降）。Linux では、このキーだけを設定するポリシーのファイル `/etc/claude-desktop/managed-settings.json` は `{"forceLoginOrgUUID": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"}` になります。プレースホルダーは claude.ai の管理者の設定に出る組織 ID に置き換え、これは Claude Code の `forceLoginOrgUUID` の設定が取るのと同じ ID です。macOS と Windows の例は、HIPAA に対応した組織向けの Cowork のガイドの「Deploy the Claude Desktop policy」にあります。Claude Code の managed settings で `forceLoginMethod` と `forceLoginOrgUUID` を設定しても、Claude Desktop のサインインの画面は変わりません。

**`hipaa-setup` にも h3「Restrict Claude Desktop sign-in」ができました。** 開発者が Claude Desktop の Code タブを使うなら、`desktop` の h4 のとおりに Claude Desktop のポリシーにも `forceLoginOrgUUID` を設定します。managed settings で `forceLoginMethod` と `forceLoginOrgUUID` を配っても、Claude Desktop のサインインの画面は変わらないためです。冒頭の表の「Before the configuration is applied」の行にも、Claude Desktop のサインインを制限する、が加わりました。前回のハイライト 2 で扱ったのは Claude Code の managed settings の `forceLoginOrgUUID` で、今回のものはそれとは別の Claude Desktop 側のポリシーです。changelog に対応する項目はありません。

- [デスクトップアプリケーション - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/desktop#restrict-sign-in-to-your-organization)
- [Desktop application - Claude Code Docs (English)](https://code.claude.com/docs/en/desktop#restrict-sign-in-to-your-organization)
- [HIPAA 対応組織向けに Claude Code（ローカルモード）をセットアップする - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/hipaa-setup#restrict-claude-desktop-sign-in)
- [Set up Claude Code (local mode) for a HIPAA-ready organization - Claude Code Docs (English)](https://code.claude.com/docs/en/hipaa-setup#restrict-claude-desktop-sign-in)

## 5. 更新を適用してセッションを再開する /restart が載った

**`commands` の表に `/restart` の行が加わりました。** Claude Code を再起動してこのセッションを再開し、インストール済みの更新を適用するコマンドで、更新がインストールされた後にフッターが勧めたときに実行します。Pro か Max のプランと、macOS か Linux（WSL を除く）のネイティブインストールが要り、Claude Code v2.1.288 以降で使えます。エイリアスは `/update` です。

- **`errors`**: 「Find your error」の表に `Can't restart while work is running in the background — wait for it to finish (or stop it via /tasks), then try again.` と `Can't restart while Remote Control is connected. To use the installed version, exit and start Claude Code again, then run /resume.` の 2 行が加わった。新しい h3「Can't restart while work is running or Remote Control is connected」は、Claude Code は再起動せず、セッションはそのまま動き続けるので、メッセージの対処に従う、と述べる
- **`env-vars`**: 機能フラグの取得をオフにしたときにできないことの一覧に、Pro と Max のプランでの `/restart` の実行が加わった
- **`interactive-mode`**: 「Cancel the wait」で、待ちを終わらせる「会話の持ち主が変わる」場合に `/restart` での再起動が加わった（Claude Desktop・バックグラウンドのセッション・クラウドへセッションを「渡す」も「移す」に言い換えられた）

changelog には `/update` についての既存の修正が載っていますが、`/restart` の名前の項目はありません。

- [コマンド - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/commands#all-commands)
- [Commands - Claude Code Docs (English)](https://code.claude.com/docs/en/commands#all-commands)
- [エラーリファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/errors#cant-restart-while-work-is-running-or-remote-control-is-connected)
- [Error reference - Claude Code Docs (English)](https://code.claude.com/docs/en/errors#cant-restart-while-work-is-running-or-remote-control-is-connected)

## 新規追加されたページ

<!-- light:new-pages:start -->
（今回の対象期間に新規追加・削除されたドキュメントページはありません。`llms.txt` は変わっておらず、URL は 275 のままです。`llms-full.txt` に展開されている固有のページも 228 のままで、`Source:` の行が 231 あり 3 ページが 2 回展開されている状態も前回と同じです）
<!-- light:new-pages:end -->

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
- [**Deploy self-hosted environments to production**](#1-deploy-self-hosted-environments-to-production) ([日本語](https://code.claude.com/docs/ja/self-hosted-environments-deploy#resumed-sessions-lose-unpushed-work) / [English](https://code.claude.com/docs/en/self-hosted-environments-deploy#resumed-sessions-lose-unpushed-work)):  
  56 行（追加 45・削除 11）が変わりました。ハイライト 3 の h3 のほか、「Additional limitations」の箇条書きだった「Resumed sessions lose unpushed work」が独立した h3 になり、ランナーのイメージに GitHub CLI を入れる場合の h4 と、`api.github.com` の行が加わりました
<!-- light:updated-pages:end -->

**行数の数え方**: `llms-full.txt` をページ単位に切り出し、`git diff --no-index --numstat` で数えた値です。base と head はどちらも Markdown の書式なので、書式の正規化はしていません。この方法で 50 行以上のページを挙げました。changelog（追加 135 行）は新しい 1 リリースの分なので大幅更新には入れず、「軽微な更新」で扱っています。次点は `troubleshoot-install` の 38 行（追加 35・削除 3。ハイライト 1）、`model-config` の 20 行（追加 11・削除 9。ハイライト 2）、`desktop` の 18 行（追加のみ。ハイライト 4）です。`setup` の 14 行（追加 9・削除 5）のうち 10 行（追加 5・削除 5）は、コードブロックの開始行の書式の重複です（「その他」参照）。

## 1. Deploy self-hosted environments to production

ページの差分のうち、h3「Start a session on a repository outside GitHub」はハイライト 3 のとおりです。そのほかは次のとおりです。

- **新しい h3「Resumed sessions lose unpushed work」**: これまで「Additional limitations」の最初の項目とその子項目、最後の項目に分かれていた内容が、「Additional limitations」の前の 1 つの h3 にまとめられました。新しいランナーで再開したセッションは、そのランナーがリポジトリを開始時のブランチからクローンし直すので、push していない作業を失います。コミットした作業を残すには、環境のすべてのランナーに `--push-outcome-on-release` を設定します。このフラグのあるランナーは解放の前にセッションの outcome のブランチをベストエフォートで push し、再開したセッションはそのコミットから始まります（フラグのないランナーは開始時のブランチから再開する）。push にはランナーのホスト自身の git の資格情報を使い、Anthropic が管理する git を使うランナーでも同じです。警告の囲みは、フラグを設定する前に元のリモートの `claude/*` の ref に push できる人を限るよう求めます（再開のとき、ランナーは前に push したブランチを、誰が push したかを確かめずに取ってくる）。フラグがあっても、次の作業は別の方法で残します
  - **コミットしていない変更**: 失われるので、「Prompt sessions to push their work」を見る
  - **`checkout` のライフサイクルのフックで取り出したリポジトリ**: push されないので、`post-session` のフックでスナップショットを取る
  - **誰かがアーカイブか削除したセッションや、セッションのメニューからランナーを解放したセッションのコミット**: フラグの push を当てにせず、`post-session` のフックで `HEAD` を退避用のブランチに push する。そこの例はスナップショットのコミットの後にだけ push するので、コミットしていないものがなくても push するようにする

  このページの「Let running turns finish before a restart」「Release idle sessions on a fixed fleet」「Some sessions don't count as idle」、`self-hosted-environments-configuration` の 2 か所（「Make on-demand runners exit when idle」の表と「Prompt sessions to push their work」）、`self-hosted-environments-reference` の `--push-outcome-on-release` の行のリンクも、`#additional-limitations` からこの h3 に付け替えられました。`self-hosted-environments-reference` の `--push-outcome-on-release` の説明は、ランナーが起こしたセッションの終わりに「追跡している outcome のブランチ」ではなく「新しいコミットのある主要なセッションのブランチ」を `origin` に push する、と短く改められています
- **新しい h4「GitHub API access with the GitHub CLI」**: 「When the image includes the GitHub CLI, sessions use it.」の 1 文が節になりました。ランナーのイメージにセッション用の GitHub CLI を入れるなら、ラッパーのスクリプトで、セッションの作成者のために短命で最小のスコープの `GH_TOKEN` をセッションごとに発行させます。Claude Code が始まるときの `PATH` に `gh` があると、セッションはその `gh` を使い、組み込みの `gh` はありません。トークンがあると、その `gh` はトークンが許すアクセスで、Anthropic が管理する git の外から GitHub に届くので、`api.github.com` を許可します。Anthropic が管理する git を使うなら、イメージに GitHub CLI を入れずに組み込みの `gh` を使います。「Network requirements」の条件付きのホストの表にも、`--use-anthropic-git-proxy` の有無にかかわらず、ランナーのイメージに GitHub CLI があり、セッションに `GH_TOKEN` のような github.com の資格情報を渡すときに要る `api.github.com`（443）の行が加わりました
- **「Ship git config in your image」**: ランナーが git・SSH・Git Credential Manager の確認を止める仕組みの一覧で、`GCM_INTERACTIVE=never` の項目に、v2.1.229 より前はリポジトリの準備が Git Credential Manager の確認で止まることがあった、と加わりました

- [本番環境へのセルフホスト環境のデプロイ - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/self-hosted-environments-deploy#resumed-sessions-lose-unpushed-work)
- [Deploy self-hosted environments to production - Claude Code Docs (English)](https://code.claude.com/docs/en/self-hosted-environments-deploy#resumed-sessions-lose-unpushed-work)
- [本番環境へのセルフホスト環境のデプロイ - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/self-hosted-environments-deploy#github-api-access-with-the-github-cli)
- [Deploy self-hosted environments to production - Claude Code Docs (English)](https://code.claude.com/docs/en/self-hosted-environments-deploy#github-api-access-with-the-github-cli)

## 軽微な更新

<!-- light:minor-updates:start -->
今回の差分は **2 ファイル**（`llms-full.txt` と見出しマップ）で、`llms.txt` は変わっていません。`llms-full.txt` の生の差分は追加 369 行・削除 86 行で、ページの並びは変わっていません。ページ単位に切り出すと 228 ページ中 **40 ページ**が変わり、changelog が 135 行（追加のみ）、ほかの 39 ページが 320 行（追加 234・削除 86）で、ページ単位の合計は生の差分と一致します（2 回展開されている 3 ページはどれも変わっていません）。大幅更新の 1 ページを除く **38 ページ**と、changelog に加わった **v2.1.314（2026年10月30日）** を以下にまとめます。

`llms-full.txt` の総行数は **126,019 行から 126,302 行へ 283 行増え**ました（生の差分の差し引き 369 − 86 と一致）。`Source:` の行は 231、固有のページは 228 のままで、2 回展開されている 3 ページ（`plugins/create`・`plugins/install`・`plugins/mods/overview`）も前回と同じです。コードフェンスの外の見出しは 5,987 から 5,996 へ 9 増えました（加わった 9・外れた 0）。changelog の収録リリースは 432 から 433 になりました。changelog は v2.1.312 の次が v2.1.314 で、v2.1.313 の項目はありません。v2.1.314 は 119 項目（追加 6・変更 16・改善 16・バグ修正 81）で、単一のリリースなので各項目への版の併記は省いています。v2.1.314 の項目には、今回の通常のページの変更に対応するものはほぼなく、多くは changelog だけで確認できる変更です。

**新機能**

- npm 12 で Claude Code のバイナリーが置かれない場合の直し方（`troubleshoot-install`・`setup`。詳細はハイライト 1 参照）
- セルフホスト環境で GitHub 以外の git ホストのリポジトリでセッションを始める手順（`self-hosted-environments-deploy`・`self-hosted-environments`・`claude-code-on-the-web`。詳細はハイライト 3 参照）
- Claude Desktop のサインインを組織に限る `forceLoginOrgUUID` のポリシー（`desktop`・`hipaa-setup`。詳細はハイライト 4 参照）
- 更新を適用してセッションを再開する `/restart`（`commands`・`errors`・`env-vars`・`interactive-mode`。詳細はハイライト 5 参照）
- `permissions.blockWritesOutsideWorkingDirectories` を追加。どの権限モードでも、Write・Edit・NotebookEdit が作業ディレクトリの外のパスを拒みます
- Claude apps gateway の上流に、省略可能な `groups` の一覧を追加。一覧にある IdP のグループの開発者だけがその上流に送られ、フェイルオーバーでも同じです
- Claude apps gateway の Bedrock の上流に `guardrail_trace` を追加。要求でどの Amazon Bedrock のガードレールのフィルターが発火したかを、一致した文を含めずにログに残します
- VS Code と Claude Desktop の Code タブにアイドルの圧縮を追加。20 万トークン以上の会話をアイドルのままにすると要約され、プロンプトキャッシュが切れていれば次のメッセージでその要約が使われます（`settings-reference` の `idleCompaction` には、VS Code のチャットパネルと Code タブの条件がすでに載っています）
- [Cloud sessions] 終わった 1 回限りのタスクだけが隠れているとき、Scheduled tasks のページに Include completed のボタンを追加。Sort のメニューを開かずに表示できます
- [Claude Tag] Slack をつないだ Enterprise の組織向けに、管理者の設定の Bundles と Channels のタブに、閉じられる Claude Tag API のドキュメントへのリンクを追加
- **Chrome の起動時のダイアログへの答え方が載った**（`chrome` の新しい h3「Answer the startup dialog」・`settings-reference`）。`claude` の起動時に「Claude in Chrome extension detected」のダイアログが出たら、その答えが **Enabled by default** の設定を変えます。**Yes, use my browser** は設定をオンにしてこのセッションをつなぎ、**No, keep browser tools off** か Esc は設定をオフにして、Claude Code は Chrome の設定を勧めなくなります。後のセッションのために答えを変えるには `/chrome` を実行します。`settings-reference` の `claudeInChromeDefaultEnabled` にも、このダイアログに答えるとキーが設定される、と加わりました — [日本語](https://code.claude.com/docs/ja/chrome#answer-the-startup-dialog) / [English](https://code.claude.com/docs/en/chrome#answer-the-startup-dialog)
- **Code Review の分析に指摘の数のカードが載った**（`code-review-costs` の「View usage」）。表に「Code Review findings」の行が加わり、選んだ期間に Claude が投稿したレビューの指摘を、重大度のレベルごとに日次で数えます — [日本語](https://code.claude.com/docs/ja/code-review-costs#view-usage) / [English](https://code.claude.com/docs/en/code-review-costs#view-usage)
- **フックが受け取る WebSearch の入力に `mode` が載った**（`hooks` の WebSearch のツールの入力）。`"standard"` は軽い検索を、`"extended"` は完全な検索を求める省略可能なフィールドです。`mode` を送らないセッションもあり、`mode` のない呼び出しは完全な検索になります（v2.1.282 以降） — [日本語](https://code.claude.com/docs/ja/hooks#websearch) / [English](https://code.claude.com/docs/en/hooks#websearch)
- **セルフホストのラッパーの環境に `CLAUDE_RUNNER_ALIVE_EVERY_MS` が載った**（`self-hosted-environments-configuration` の「Wrapper scripts」）。子が初期化する前にターンが始まったとき、子が生きていると報告する間隔（ミリ秒）をランナーが設定する変数です。ラッパーが子の環境を作り直すならこの変数を引き継がないと、そのターンの間にランナーがセッションを解放し、`no child output for <n> — releasing` と記録することがあります（ランナーと子の両方で v2.1.309 以降） — [日本語](https://code.claude.com/docs/ja/self-hosted-environments-configuration#wrapper-scripts) / [English](https://code.claude.com/docs/en/self-hosted-environments-configuration#wrapper-scripts)
- **保持期間のスイープのイベントに、理由 `remote_settings_unknowable` が載った**（`monitoring-usage` の「Retention sweep event」）。サードパーティのデプロイの Claude Desktop の Code タブのセッションが server-managed settings を求めて使える応答を受け取れず、`cleanupPeriodDays` が Claude Code に見えない値に設定されているかもしれないことを示します — [日本語](https://code.claude.com/docs/ja/monitoring-usage#retention-sweep-event) / [English](https://code.claude.com/docs/en/monitoring-usage#retention-sweep-event)

**機能改善**

- effort のレベルの解決順と、スキル・サブエージェントの effort が効く範囲、各所に出るレベルの意味の整理（`model-config`・`skills`・`statusline`・`hooks`・`env-vars`・`prompt-caching`・`agent-sdk/typescript`。詳細はハイライト 2 参照）
- `/claude-api` スキルを更新。API のトレースの Datadog の設定が、Console と同じく `dd-llmobs-enabled: true` のヘッダーを送るようになり、`ant` のインストールの手順から古い macOS の `xattr` の手順が外れました
- 同梱の dataviz スキルを更新し、y 軸の目盛りのラベルは 10,000 未満なら、横向きのものは収まる範囲で 100 万未満なら、省略せずに出すよう勧めるようにしました
- 同梱の dataviz スキルを更新し、ドーナツや円グラフの依頼には、順位を付けた棒グラフか、値を示す区分けした棒で答えるようにしました
- 組織の server-managed settings の手元のコピーを編集する前に、設定ファイルと同じく Claude のファイルのツールが確認を求めるよう変更
- `/ultrareview` が、`claude ultrareview` と同じく git を動かす前にワークスペースの信頼を確かめるよう変更
- Bash ツールのシェルが、継承した `which` のエイリアスか関数を消し、export された `which`・`unsetenv` の関数をコマンドに渡さないよう変更。`which` はシステムのコマンドか zsh の組み込みになります
- `/permissions` の Recently blocked で、全文を読めない呼び出し（ターミナルが短すぎて示せないものを含む）の承認を拒むよう変更
- Cowork のクラウドのセッションの auto モードで、MCP のツールの呼び出しをフックが許可しても答えなしと数え、分類器か権限の確認が決めるよう変更
- `Monitor(tail *)` のようなフックの `if` の条件が、`Bash(tail *)` が Bash に一致するのと同じく、Monitor ツールのシェルのコマンドに一致するよう変更
- `claude-api` スキルが、Managed Agents のワークフローの実行を良くするためにエージェントを変える前に、その実行のワークフローを読んでよいか尋ねるよう変更
- `ANTHROPIC_DEFAULT_OPUS_MODEL`・`availableModels`・`deniedModels` によって古い Opus のモデルしか残らないか何も残らないとき、フラグの付いた要求が拒否で終わらず、別のモデルで再試行されるよう変更
- アイドルの圧縮が、テレメトリーをオフにした加入者でも、また 1 時間のプロンプトキャッシュがオンなら Bedrock・Vertex・Foundry・LLM ゲートウェイでも動くよう変更
- `FORCE_HYPERLINK=false`（`no`・`off` も）が、ハイパーリンクをオンではなくオフにするよう変更
- macOS: Claude が動かすほとんどのコマンドの `git grep` を C ロケールで動かすよう変更。UTF-8 として正しくないファイルで、macOS の正規表現のライブラリにメモリリークが報告されているのを避けるためです
- [VSCode] `CLAUDE_CODE_DISABLE_CFC_PROMPT` が、拡張機能がセッションのメッセージに Claude in Chrome の指示を加えるのも止めるよう変更。ブラウザーのツールは使えるままです
- [Cloud sessions] Web・デスクトップ・モバイルのアプリから始めたクラウドのセッションが、セットアップスクリプトがエラーで終わっても、始まらずに失敗するのではなく始まるよう変更
- 多くのサブエージェントを動かす長いヘッドレスと SDK のターンのメモリーの使用を改善。親のセッションが、各サブエージェントのツールの結果をターンの終わりまで持たなくなりました
- プロンプトの履歴を改善。Ctrl+R が、折りたたんだ `[Pasted text]` のピルの中の文にも一致します
- `/design-sync` のアップロードの確認を改善。フォルダー・プロジェクト・アップロードか削除するファイルを示します
- `/permissions` の確認のタブ（名前は Recently blocked に）を改善。フッターが、印を付けた行に Esc で何をするかを示します
- auto モードで止められた呼び出しを改善。メッセージがコマンドを名指し、Claude が再試行して auto モードがもう一度確かめうること、確認には `/permissions` を見ることを示します
- 権限の確認を改善。長い理由が取る行が減り、承認するコマンドが画面の外に押し出される端末が減ります
- claude.ai のログインで拒まれた要求をまだ再試行している間に出る、クラウドのセッションのエラーを改善。`claude auth login` も勧めます
- MDM と remote settings でベース URL か `apiKeyHelper` が違うときの、保存された claude.ai・Team・Enterprise のログインの挙動を改善
- エージェントビューの `/config` を改善。エージェントビューが既定で開かないようにする方法を示します
- セッションの自動のタイトルを改善。スキルか `/security-review` のようなプロンプトベースのコマンドで始めたセッションが、無題のままではなく、そこからタイトルを得ます
- 壊れたトランスクリプトでの `--resume` の速さとメモリーの使用を改善
- MCP のツールが 1 万以上あるセッションでの `/context` の速さを改善
- セルフホストのランナー: セッションのブランチが git のリモートにないときのエラーを改善。一度も push していないブランチも扱い、それぞれの直し方を示し、再試行を勧めなくなりました
- [Cloud sessions] スケジュールしたタスクを改善。Anthropic のクラウドでの実行が、claude.ai のアカウントで有効にしたプラグインを読み込みます
- [Cloud sessions] 管理者の設定の GitHub Enterprise の Test connection を改善。クラウドのセッションと同じ方法でもつなぎ、その 2 回目のテストが失敗すると警告します
- [Cloud sessions] クラウドのセッションのトランスクリプトを改善。名前の変更の行が新しいタイトルを示し、リポジトリと環境の一覧が 1 行の JSON ではなく表で出ます
- **auto モードでの PreToolUse のフックの `ask` の扱いが節になった**（`hooks` の新しい h4「PreToolUse `ask` decisions in auto mode」）。auto モードでは、PreToolUse のフックの `"ask"` は通常ツールの呼び出しを権限の確認に送り、分類器は決めません。ただし、保護されたパスへの書き込みやサンドボックスの外で動かすことを求めるコマンドのように、Claude Code 自身のチェックも引っかける呼び出しは、確認が出る前に分類器が拒めます（承認しても通常は確認に進む）。サブエージェントの報告を届ける `SubagentHandback` の呼び出しには確認が出ず、分類器が反対しても動きます。これを止めるには `"deny"` を返し、Claude Code はサブエージェントに、報告が届かなかったのでツールをもう一度呼ぶよう 3 回まで伝えます。拒み続けると、サブエージェントはこのツールで報告を届けずに終わり、それを待つ会話にそう記した注記が届きます。「PreToolUse decision control」からは、「`"ask"` は auto モードでも権限の確認を強制し、分類器は拒めるが黙って承認はできない」という段落が外れました — [日本語](https://code.claude.com/docs/ja/hooks#pretooluse) / [English](https://code.claude.com/docs/en/hooks#pretooluse)
- **クラウドのセッションをターミナルに引き寄せるとき、圧縮した前のメッセージはコピーされないと載った**（`claude-code-on-the-web` の「Continue a cloud session in your terminal」）。Claude Code がクラウドのセッションを圧縮していたら（長いセッションでは自動で行う）、要約した前のメッセージはターミナルにコピーされず、Claude は要約から続けます。元のメッセージは、claude.ai か Claude のモバイルアプリのクラウドのセッションで上にスクロールして読みます。テレポートで「会話の完全な履歴」を読み込む、という言い方は「会話」を読み込む、に改められ、`--teleport` と `--resume` の違いを述べた段落は、`--teleport` の項目の 1 文（`--resume` はこのマシンの手元の履歴から会話を開き直し、クラウドのセッションを一覧しない）にまとめられました。changelog の既存の v2.1.311 の改善（圧縮したクラウドのセッションを読み込むとき、要約したメッセージが手元のコピーにないと警告する）に対応します — [日本語](https://code.claude.com/docs/ja/claude-code-on-the-web#from-cloud-to-terminal) / [English](https://code.claude.com/docs/en/claude-code-on-the-web#from-cloud-to-terminal)
- **ディープリンクのハンドラーはエージェントビューの起動でも登録されると載った**（`deep-links` の「Registration and supported platforms」など・`settings-reference`）。`claude-cli://` のハンドラーを登録するきっかけが、対話的な `claude` のセッションにメッセージか `/help` のような何かを送ったとき（何も送らなければ登録しない）と、信頼したフォルダーで `claude agents` などによってエージェントビューの Claude Code を始めたとき、の 2 つになりました（これまでは、対話的なセッションで最初のプロンプトを送ったときだけ）。「Open a link from the shell」と「Clicking the link does nothing」もこれに合わせて言い換えられ、`settings-reference` の `disableDeepLinkRegistration` からは、最初のプロンプトを送った後に登録する、という説明が外れています — [日本語](https://code.claude.com/docs/ja/deep-links#registration-and-supported-platforms) / [English](https://code.claude.com/docs/en/deep-links#registration-and-supported-platforms)
- **バックグラウンドのトークンの使用の説明が書き直された**（`costs` の「Background token usage」・`goal`）。アイドルの間にトークンを使いうるのはセッションのリキャップとアイドルの圧縮で、それぞれいつ動き、どうオフにするかはその節を見る、という 1 段落になりました。これまでの「`claude --resume` のための会話の要約」と「`/usage` のようなコマンドの処理」の 2 項目と、「通常セッションあたり $0.04 未満」という目安は外れています。`goal` の「Evaluation model and cost」の警告も、`ANTHROPIC_DEFAULT_HAIKU_MODEL` を設定すると、会話の要約のようなバックグラウンドの機能ではなく、セッションのタイトルの生成とほかの一部のバックグラウンドのタスクがそのモデルで動く、と改められました。changelog の v2.1.314 にも、アイドルの圧縮の追加と変更があります — [日本語](https://code.claude.com/docs/ja/costs#background-token-usage) / [English](https://code.claude.com/docs/en/costs#background-token-usage)
- **ultrareview の所要時間の目安が 5〜15 分になった**（`ultrareview` の「Track a running review」と `/code-review` との比較の表）。これまでは 15〜25 分でした — [日本語](https://code.claude.com/docs/ja/ultrareview#track-a-running-review) / [English](https://code.claude.com/docs/en/ultrareview#track-a-running-review)
- **プロジェクトの新しいスレッドの上限が 1 日 500 になった**（`claude-projects` の「What draws on your plan」）。プロジェクト全体で 1 日に始められる新しいスレッドの強制される上限が、200 から 500 に改められました — [日本語](https://code.claude.com/docs/ja/claude-projects#what-draws-on-your-plan) / [English](https://code.claude.com/docs/en/claude-projects#what-draws-on-your-plan)
- **ターミナルごとの既定の通知が書き分けられた**（`terminal-config` の「Get a terminal bell or notification」）。Ghostty・Kitty・iTerm2 はデスクトップの通知（iTerm2 はアラートの設定をオンにした後だけ出る）、Apple Terminal は音を鳴らさず、前面の Terminal のウィンドウのプロファイルで「Audible bell」がオフだと Claude Code が見つけたときに無音のベル文字を送り、それ以外は何もしません（そのベル文字は、そのプロファイルの「Visual bell」か Dock のバウンスの選択肢がオンなら、ウィンドウの点滅か、Terminal が背後にあるときの Dock のバウンスとして見える）。ほかのターミナルは何もしません。ターミナルやプロファイルにかかわらずベル文字を送らせるには `preferredNotifChannel` を `"terminal_bell"` にし、Apple Terminal で聞くには **Settings > Profiles > Advanced** の **Audible bell** もオンにします（これまでは、デスクトップの通知は Ghostty・Kitty・iTerm2 だけで、ほかのターミナルでは `"terminal_bell"` にすると代わりにベルを鳴らす、と書かれていた） — [日本語](https://code.claude.com/docs/ja/terminal-config#get-a-terminal-bell-or-notification) / [English](https://code.claude.com/docs/en/terminal-config#get-a-terminal-bell-or-notification)
- **Agent SDK のセッションのストレージで、一時の設定ディレクトリでの認証の方法が箇条書きになった**（`agent-sdk/session-storage` の「Dual-write architecture」）。`CLAUDE_CONFIG_DIR` は「新しい、自分だけの一時ディレクトリ」にするよう改められ、一時ディレクトリにして claude.ai のログインかユーザーの `settings.json` の `apiKeyHelper` でサインインしていると `Not logged in` で失敗する、と明記されました。対処は、自分の Claude のサブスクリプションで自分がエージェントを動かすなら `claude setup-token` のトークンを `CLAUDE_CODE_OAUTH_TOKEN` に設定する（モデルの要求にしか使えないので、claude.ai のコネクターはその実行で使えない）、`ANTHROPIC_API_KEY` を設定する、ふだんの設定ディレクトリの OAuth の資格情報や `apiKeyHelper` のファイルを一時ディレクトリにコピーする、の 3 つです — [日本語](https://code.claude.com/docs/ja/agent-sdk/session-storage#dual-write-architecture) / [English](https://code.claude.com/docs/en/agent-sdk/session-storage#dual-write-architecture)
- **サンドボックスの書き込みの拒否が、ワイルドカードを含む項目でもシンボリックリンクの先に及ぶと載った**（`sandboxing` の「Denied paths that pass through a symlink」）。`*`・`?`・`[` を含む `denyWrite` の項目も、最初のその文字より前のフォルダーがシンボリックリンクなら対象になります（例: `~/.claude/*.json` は `~/.claude` の実際の場所の下でも拒まれる） — [日本語](https://code.claude.com/docs/ja/sandboxing#denied-paths-that-pass-through-a-symlink) / [English](https://code.claude.com/docs/en/sandboxing#denied-paths-that-pass-through-a-symlink)
- **Claude apps gateway での Claude Desktop の Chat の説明が改められた**（`claude-apps-gateway` の「Connect Claude Desktop」など）。Chat も使えるようにするには、Claude Code v2.1.227 以降のゲートウェイで、ポリシーの `desktop` のブロックの `chatTabEnabled` を `true` にする、と改められ、Claude Desktop の managed configuration で設定するという選択肢の記述が外れました。Cowork がオンなら Claude Desktop は Chat と Cowork を 1 つのタブにまとめて示す、と加わっています。「Deliver policy to Claude Desktop sessions」の「Chat タブ」も「Chat」と言い換えられ、構成図の説明文と可用性の表の Claude Desktop の行からはタブの列挙が外れました — [日本語](https://code.claude.com/docs/ja/claude-apps-gateway#connect-claude-desktop) / [English](https://code.claude.com/docs/en/claude-apps-gateway#connect-claude-desktop)
- **Fable の使用量クレジットの同意の確認の言い方が改められた**（`model-config` の「Fable and usage credits」・`errors` の「The prompt to confirm went unanswered」）。「Fable の要求が使用量クレジットに課金される前に同意の確認を示す」が「Fable の使用量クレジットの同意の確認を示すことがある」になり、`errors` の節の前置きも、アカウントが同意を要する場合という説明を省いて、同意の確認が誰にも答えられずに閉じたとき、だけになりました — [日本語](https://code.claude.com/docs/ja/model-config#fable-and-usage-credits) / [English](https://code.claude.com/docs/en/model-config#fable-and-usage-credits)
- **Agent SDK の `settingSources` の `"local"` で、`settings.local.json` がリポジトリのルートからも読まれうると載った**（`agent-sdk/claude-code-features` の「Control filesystem settings with settingSources」）。`<cwd>` が git リポジトリの中なら、`settings.local.json` はリポジトリのルートからも読み込まれえます。`cwd` のオプションの説明からは、親ディレクトリへのフォールバックなしに `<cwd>/.claude/` から読み込むものとしての「フック」が外れ、プロジェクトの `settings.json` だけになりました — [日本語](https://code.claude.com/docs/ja/agent-sdk/claude-code-features#control-filesystem-settings-with-settingsources) / [English](https://code.claude.com/docs/en/agent-sdk/claude-code-features#control-filesystem-settings-with-settingsources)
- **Agent SDK の `TaskStop` の古い名前を使える場所が明確になった**（`agent-sdk/python` の「TaskStop」）。以前の名前 `KillShell` と `KillBash` は、権限ルール・フックのマッチャー・`tools`・`allowed_tools`・`disallowed_tools` のオプションで引き続き使える、と改められました（これまでは、エイリアスとして受け付ける） — [日本語](https://code.claude.com/docs/ja/agent-sdk/python#taskstop) / [English](https://code.claude.com/docs/en/agent-sdk/python#taskstop)
- **mod の中断の後、動いていたフォアグラウンドのシェルのコマンドがタイムアウトで止まる場合が載った**（`plugins/mods/api` の「Work your mod started before the interruption」）。ユーザーがターンを止めたときにすでに動いていた `$.tool.call` のフォアグラウンドの Bash か PowerShell のコマンドが、次の入力の前にタイムアウトに達すると、バックグラウンドへ移らずにタイムアウトで止まり、呼び出しは `isError` 付きで解決し、出力に `Ended instead of moving to the background: plugins' input is held, by a Stop or by the host's limits.` の行が入ります。ユーザーの次の入力の後で、もう一度実行します — [日本語](https://code.claude.com/docs/ja/plugins/mods/api#work-your-mod-started-before-the-interruption) / [English](https://code.claude.com/docs/en/plugins/mods/api#work-your-mod-started-before-the-interruption)
- **`commands` の `/model` の行が短くなった**。切り替えた新しいモデルがいつから使われるかは `interactive-mode` の「When Claude Code sends what you queued」へのリンクに任され、v2.1.242 より前の挙動は「待つことがあった」の 1 文に、`-p` での使い方も短く改められました。`interactive-mode` の同じ節の `/model` の項目も、「変更を適用する」から「新しいモデルを使う」に言い換えられています。日本語版の `/model` の行はまだ前の長い説明なので、英語版だけにリンクします — [English](https://code.claude.com/docs/en/commands#all-commands)

**バグ修正**

- 組織の管理者がモデルの effort に上限を設けたとき、セッションがターンのたびに「Invalid effort level」で失敗する問題を修正。Claude Code が effort を下げて再試行し、使うレベルを示します
- 起動に失敗したとき、`claude -p` が出力なしに終了コード 0 で終わる問題を修正。エラーを出して 1 で終わります
- 画像の多い Bedrock のセッションで、古い画像を外して圧縮する代わりに、毎ターンと `/compact` が「400 Input is too long.」で失敗する問題を修正
- Microsoft Foundry のリソースに、既定の Sonnet・Opus・Haiku のモデルのデプロイがないとセッションが失敗する問題を修正。そのファミリーの古いモデルにフォールバックします
- ツール検索の `tool_reference` のブロックを受け付けないゲートウェイの後ろで、要求の拒否が繰り返される問題を修正。ツール検索なしで一度送り直し、セッションはそれを覚えます
- システムの証明書ストアに、前のものとクロス署名された更新済みのルート証明書があると、TLS の接続が `UNABLE_TO_GET_ISSUER_CERT` で失敗する問題を修正
- サインインなしでも動く MCP サーバーが、保存したサインインが効かなくなった後に「needs authentication」と示される問題を修正。サインインなしで使われます
- SSH 越しで macOS のキーチェーンがロックされているときなど、MCP のサインインが消えていないのに `claude mcp logout` が成功と報告する問題を修正
- 複数のセッションが Anthropic のプロファイルのログインを共有し、資格情報のロックが使用中のときに、サインインの更新が余分に起きる問題を修正
- ターミナルのある CI のジョブで、`claude ultrareview` と `claude remote-control` がワークスペースの信頼を尋ねる問題を修正。`CI` を設定していれば、信頼していないフォルダーをすぐに拒みます
- managed settings にある管理者の TLS の信頼の設定が、Claude Desktop のセッションに適用されない問題を修正
- managed のプラグインの設定のあるマシンで、自分の `--plugin-dir` か `--plugin-url` のプラグインのマニフェストが壊れているかダウンロードに失敗すると、モデルの切り替えが拒まれる問題を修正
- managed settings がモデルを固定しているとき、Bedrock と Vertex のモデルのアップグレードの提案が起動のたびに戻ってくる問題を修正
- remote の managed settings にだけ設定した `forceRemoteSettingsRefresh` が、保存したコピーの期限が切れると効かなくなり、サーバーに届かないとポリシーなしでセッションが始まりえた問題を修正
- 待ちの間にタスクが自分で再開したとき（/goal の確認、バックグラウンドかスケジュールしたタスク）、「Continue automatically at usage limit」があなたのプロンプトなしに 3 回を超えて続く問題を修正
- Ultracode で始めたバックグラウンドとクラウドのセッションが、Ultracode をオフにした後の次の起動でまたオンに戻る問題を修正
- パースできないツールの呼び出しを Claude が諦めた後、最後の壊れた返事とその再試行のプロンプトが会話に残る問題を修正
- 出力がとても大きい PreCompact のフックで、圧縮が失敗するか繰り返す問題を修正。各フックの出力は 10,000 文字で切られます
- バックグラウンドの差分の更新がリポジトリのインデックスのロックを一瞬取り、同時に動いた git のコマンドが「Unable to create '.git/index.lock': File exists」で失敗しうる問題を修正
- ストリーミング中に、書きかけの行で markdown の表がグリッドと縦積みのレイアウトの間で跳ね、長い表が生のパイプに戻る問題を修正
- スラッシュコマンドしか動かしていないセッションで、/resume のピッカーが CLAUDE.md か CLAUDE.local.md の文をセッションのタイトルとして示す問題を修正
- サブエージェントのトランスクリプトを開いて尋ねたとき、`/btw` がメインの会話から答える問題を修正
- SSH 越しの Linux のマシンに画像を貼り付けても、何も言わずに何も起きない問題を修正。ファイルをコピーしてそのパスを貼るよう示します
- セッションのサービスが一瞬遅いと `claude remote-control` のセッションが始まらない問題を修正。ワーカーの登録を、待ちを伸ばしながら再試行します
- Remote Control 越しの 8 秒を超えるモデルの切り替えが、最終的な結果ではなく「still pending」のエラーを受け取る問題を修正
- `sandbox.excludedCommands` の設定の説明が、一覧のコマンドは常にサンドボックスの外で動くと言っていた問題を修正。呼び出しのすべてのコマンドが項目に一致する必要がある、と言います
- auto モード・拒否のルール・PreToolUse のフックが止めたか、ほかの理由で動かなかったシェルと MCP の呼び出しが、折りたたんだツールのグループで動いたように読める問題を修正
- `claude -p --resume` か `--continue` で入った worktree に、サンドボックスの保護が効かない問題を修正
- Bash に一致するフックが、Monitor ツールが始めたシェルのコマンドで動かない問題を修正。そうしたフックはそのコマンドを止めるか確認を求められますが、承認や書き換えはできません
- `--setting-sources` で除いた設定ファイルが、auto モードのルールや保存した権限の同意など一部の設定をまだ与えていた問題を修正
- 安全性のチェックが判定を出さなかったとき、auto モードが呼び出しを止めたと報告し、`/permissions` に載せる問題を修正
- Google のトークンのエンドポイントが接続を受けて答えないとき、Claude apps gateway の Vertex の上流が数分止まる問題を修正
- Claude apps gateway がまだ書かれたとおりに提供している非推奨の Claude Desktop のキーについて、キーの終了日の後に起動時の警告が「stops being accepted」と言う問題を修正
- App Store か Google Play で請求されるプランで、`/upgrade` がブラウザーを開いて新しいログインを始める問題を修正。プランを変える場所を示します
- `--resume` するか、拒否の後に別のモデルへ切り替えた点より前に巻き戻すと、Claude Code が知らないモデル名のセッションが別のモデルに移る問題を修正
- ゲートウェイかクラウドのプロバイダーが Claude Code のベータのヘッダーの 1 つを名指しで拒むと、要求が失敗する問題を修正。そのヘッダーなしで送り直します
- LLM ゲートウェイの後ろで `claude-opus-4.8` のようにドットで書いたモデルの ID が古いモデルとして扱われ、コンテキストウィンドウ・出力の上限・effort・思考のモード・コストを誤る問題を修正
- /compact の後、Remote Control のクライアントに余分な「Compacted (ctrl+o to see full summary)」の行が出る問題を修正
- 組織のポリシーがクラウドのセッションと Remote Control をオフにしているのに、クラウドのセッションのヒントと Remote Control のアイドルの通知が出る問題を修正
- 前のワーカーが新しいチャットのファイルを受け取った直後に止まると、再開した claude.ai のクラウドのセッションが誰も頼んでいないモデルの呼び出しをする問題を修正
- Cowork のクラウドのセッションの WebFetch が、PDF の 100,000 文字を超える文を何も言わずに落とす問題を修正。どれだけ読まれていないかと、どこから読めばよいかを示します
- クラウドのセッションか IDE で Esc か Stop でコマンドを止めた後、Claude にはコマンドが断られたとしか伝わらない問題を修正。コマンドが動いたかもしれないことも伝わります
- 引用を開くコードブロックで、コードブロックの先頭の空行が消える問題を修正
- トランスクリプトのビュー（Ctrl+O）で、一部の `⎿` の行の上に空行が出る問題を修正
- vim モードの `dw`・`dW`・`yw`・`yW` が行末を越えて続く問題を修正し、`w` と `W` が空行で止まるようにしました
- 別のエージェントが始まるか終わったとき、エージェントのパネルの x と Enter が違うエージェントに効くことがある問題を修正
- 「Other」の行にフォーカスがないと、Claude の質問のダイアログで貼り付けた文とドラッグしたファイルが失われる問題を修正
- プロンプトのフッターの行を選んでいると、貼り付けた文が失われる問題を修正
- 文字の選択の上での vim モードの `p` が、ヤンクした文が行全体かどうかを無視する問題を修正
- vim モードの `aw` と `iw` が行末の改行を取る問題を修正
- ↓ が、? のヘルプのメニュー・コマンドの一覧・貼り付けのヒントに隠れたフッターの項目を選ぶ問題を修正
- `/btw` のようなコマンドのパネルでの Esc が、トランスクリプトを開いているサブエージェントも中断する問題を修正
- 別のモデルで動くサブエージェントかチームメイトを見ている間、フルスクリーンのモードのウェルカムのヘッダーがセッションのモデルを示す問題を修正
- 上にスクロールしている間に巻き戻しのメニューで「Restore conversation」をすると、フルスクリーンのトランスクリプトが会話の途中に残される問題を修正
- 消したセッションが、ほとんど空の項目として再開の一覧にまた出ることがある、まれな問題を修正
- `<bash-stdout>` や `<local-command-stdout>` のようなタグを含むプロンプトについて、ローカルの stream-json のホストに受け取りが返されない問題を修正
- 最初のプロンプトが（たとえば利用上限で）失敗し、その後に会話が続いたとき、セッションが無題のままになる問題を修正
- スキルのファイルの監視が `~/.claude/skills/.trash` に残った削除済みのスキルをすべて確かめ、削除のたびにファイルシステムの負荷が増える問題を修正
- Claude が権限か plan の判断を求めている間、/rename のセッション名が消える問題を修正。並べたセッションを見分けられたままになります
- 始まらなかったバックグラウンドのセッションが、バイナリーがまだディスクにあるのに、デーモンのバイナリーが消されたと報告される問題を修正
- `/config` のプッシュの設定が隠れているか、組織が Remote Control をオフにしているのに、プッシュ通知についてのヒントとアイドルのリマインダーが出る問題を修正
- `~/.claude/skills/.trash` と `~/.claude/plugins/.trash` が際限なく増える問題を修正。`cleanupPeriodDays` にかかわらず、それぞれ約 1024 項目を保ちます
- git の改行の変換を受ける CRLF のファイルを、変えずに保存し直すか 1 行を編集すると、Bash の編集の差分がファイル全体を変更として示す問題を修正
- セルフホストのランナー: アイドルのセッションを一時停止するランナーの要求が、Anthropic の応答の前に接続を失うと、セッションが一時停止せずに別のランナーへ移る問題を修正
- [VSCode] 保存したサインインを消せなかったのに、MCP サーバーの「Clear authentication」が成功と報告する問題を修正
- [VSCode] キューに入れたメッセージのフックが動く間、スピナーと Stop ボタンが出ない問題を修正
- [VSCode] 削除など、保存できないセッションのグループの変更が何も言わずに失敗する問題を修正。エラーの通知が出ます
- [VSCode] plan のプレビューのタブで Cmd+F / Ctrl+F が検索のウィジェットを開かない問題を修正
- [VSCode] ロシア語・ギリシャ語・ヘブライ語のようなラテン文字でないキーボードの配列で、音声入力のショートカット（Ctrl+D）が何もしない問題を修正
- [VSCode] チャットなしで拡張機能が開いたとき、逃した 1 回限りの保存されたスケジュールのタスクが尋ねずに消される問題を修正
- [Cloud sessions] 最近使ったセルフホストの環境が、新しいセッションのカードの最近の環境に出ない問題を修正
- [Cloud sessions] Claude が別の worktree から push したコミットにブランチを動かした後、クラウドのセッションが毎ターンコミットしていない変更を報告する問題を修正
- [Cloud sessions] とても低いウィンドウか高い拡大率で、管理者の設定のセルフホストの環境の詳細のダイアログが中身を見えないところへ押し出す問題を修正。ダイアログがスクロールします
- [Cloud sessions] 動いているクラウドか Remote Control のセッションが切り替えを拒んだ後、権限のモードのピッカーが Auto のままになる問題を修正。使われているモードを示し、そう伝えます
- [Remote Control] Remote Control のセッションの権限のモードのボタンが、入力するまで違うモードを示す問題を修正。コンピューターがオンラインなら、開いたときに本当のモードを示します
- [Claude Tag] Enterprise Grid のワークスペースで共有したチャンネルで、`@Claude !restart` がワークスペースの確認に 1 回失敗すると諦める問題を修正。再試行し、それでもだめならもう一度実行するよう求めます
- [Claude Tag] 同じリンクから数分以内に Slack から Claude のアカウントを 2 回つなぐと、確認の DM とチャンネルの通知が 2 度目も出る問題を修正
- [Claude Tag] Claude のセッションがセルフホストのランナーを待つ間、Slack の後続のメッセージに進み具合が何も出ない問題を修正。Claude がスレッドに待ちの通知を投稿します
- [Claude Tag] 両方の組織が Claude を入れている Slack Connect のチャンネルで、Claude が自分のスレッドでのタグに答えないことがある問題を修正
- [Claude Tag] 読み込みの失敗の後、Claude Tag の管理者の設定のプラグインとスキルのページで Retry が保存していないアクセスの変更を捨てる問題を修正。編集はそのまま残ります
- [Claude Tag] Claude Tag の管理者の設定のリポジトリのコントロールが同じ操作を 2 回示す問題を修正。メニューにはボタンがまだしないことだけが並びます

**その他**

- **Claude Tag のチャンネルのセッションについての説明の簡略化**（`artifacts`・`slack`・`cloud-environments`・`monitoring-usage`・`self-hosted-environments-configuration`・`self-hosted-environments-identity`）。Claude Tag のセッションはエージェントの ID でサインインしている（`artifacts` の「Availability」）、Claude はメンバーのアカウントとしてではなく組織の共有の ID としてチャンネルで働く（`slack` の「Sessions from a Claude Tag channel fail to start」）、チャンネルのセッションは組織レベルの環境だけを使う（`cloud-environments`・`monitoring-usage`）、どのアカウントもエンキューしないので `CLAUDE_RUNNER_ACCOUNT_ID` は常に空（`self-hosted-environments-configuration`）、組織のサービスの ID が作るセッションに Claude Tag のチャンネルのセッションが含まれる（`self-hosted-environments-identity` の 3 か所）、という説明がそれぞれ外れました。`artifacts` はサインインの手順は要らない、とだけ言い、`cloud-environments` は「Set the environment a Claude Tag channel uses」へ案内しています。`self-hosted-environments-identity` の「Claims reference」の前置きと手順 7 は段落が分かれ、表の前の説明の順も入れ替わりました
- **`setup` のコードブロックの開始行の重複**: 「Install Claude Code」の 5 つのコードブロック（macOS・Linux・WSL、Windows PowerShell、Windows CMD、Homebrew、WinGet）の開始行で、`theme={null}` が 1 回から 29 回に重なりました。コマンドそのものは変わっておらず、内容の変更ではなく書式の崩れと見られます
- **`self-hosted-environments` の「Network paths」の言い換え**: Anthropic が管理する git を使うセッションで、子が `api.anthropic.com` に開く WebSocket の接続が `git` と `gh` の github.com への通信を運ぶ、と語順が改められました
<!-- light:minor-updates:end -->

見出しマップ（`en/claude_code_docs_map.md`）は 10 行が加わり 1 行が外れました。加わったのは 9 の見出しと新しいスタンプ、外れたのは古いスタンプで、加わった 9 の見出しは `llms-full.txt` で加わった 9 の見出しと同じです。今回、見出しマップにだけ先に載った見出しはありません。

**参考リンクについて**: 日本語版は、ハイライト・大幅更新・軽微な更新で扱った 34 ページを取得し、該当する節があるかと今回の内容になっているかを、計 54 項目について確かめました（長いページは生の Markdown を区切って読んでいます）。53 項目は日本語版がすでに今回の内容になっていたので日本語版を併記し、`commands` の `/model` の行だけはまだ前の長い説明だったので、その項目は英語版だけにリンクしています（同じページの `/restart` の行は日本語版にもあるので、ハイライト 5 は併記しています）。`claude-code-on-the-web` の「Continue a cloud session in your terminal」は、ページ内外のリンクが使っている前からの `#from-cloud-to-terminal` を id として使いました。`errors` の「Can't restart while work is running or Remote Control is connected」は、ページ内の表のリンクが使っている `#cant-restart-while-work-is-running-or-remote-control-is-connected` を id として使っています。`hooks` のバッククォートを含む新しい h4「PreToolUse `ask` decisions in auto mode」は id を確かめられないので、上位の h3「PreToolUse」へリンクしています。changelog だけに載っている項目にはリンクを付けていません。**changelog ページへのリンクは、本サマリの方針どおり付けていません。**

## 新着情報

<!-- light:whats-new:start -->
**今回、新着情報（`whats-new/`）のページに変更はありません**（最新の週のダイジェストは前回と同じ Week 37 です）。
<!-- light:whats-new:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-10-28.md](./archives/latest/2026-10-28.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-10-28.md](./archives/latest-detail/2026-10-28.md)

<!--
base_commit: 7ff696fc9bf91ed3aa99a3749a2d4e451d873d85
head_commit: daf68aee10e1e23402b90d685734b8fa2df7beb5
generated_at_full: 2026-10-30T15:12:23+09:00
-->
