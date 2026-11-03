---
対象期間: 2026年11月01日 〜 2026年11月02日
作成日: 2026-11-02
---

# Claude Code 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
**今回は changelog に v2.1.317（2026年11月03日）の 1 リリースが積まれ、通常のページには、v2.1.314・v2.1.316 で入った機能の解説として、作業ディレクトリの外への書き込みを拒む `permissions.blockWritesOutsideWorkingDirectories`、Claude apps gateway の上流の `groups` と `policy_mode: layered`、Bedrock のガードレールの入力タグとフィルターのログ、auto モードの Recently blocked タブでの承認の手順が載り、Opus 4.8 の fast mode が 2026年11月30日に削除されると告知されました**。新しいページはなく、228 ページ中 47 ページ（changelog を含む）が変わり、changelog を除く変更はページ単位で 777 行（追加 636・削除 141）、大幅更新は `claude-apps-gateway-config`・`errors`・`settings-reference` の 3 ページです。見出しマップに加わった 24 の見出しは、すべて `llms-full.txt` にも入っています。総行数は 126,454 行から 127,052 行に増えました。

主要なものを以下に挙げます。

1. `permissions.blockWritesOutsideWorkingDirectories`（v2.1.314 以降）の h3 が `settings-reference` に、関連する節が `permissions`・`permission-modes`・`errors`・`worktrees`・`tools-reference` に載り、Write・Edit・NotebookEdit がどの権限モードでも作業ディレクトリの外へ書かないこと、書き込めるまま残るファイル、worktree のツールが外れることが説明された
2. Claude apps gateway の上流に IdP のグループの `groups` の一覧を付けてチームごとに上流を分ける方法（v2.1.314 以降）と、合うポリシーをすべて重ねる `managed.policy_mode: layered`（v2.1.316 以降）が `claude-apps-gateway-config` に載った
3. Claude apps gateway の Bedrock のガードレールに入力タグを付ける `input_tagging`（v2.1.316 以降、4 つの値）と、どのフィルターが反応したかを監査ログに残す `guardrail_trace`（v2.1.314 以降）が載った
4. auto モードで止められた操作の承認が、`/permissions` の **Recently blocked** タブ（旧 Recently denied）での 4 つの手順と、後で承認する・取り消す・捨てる操作に書き直された
5. Opus 4.8 の fast mode は 2026年10月30日に非推奨になり 2026年11月30日に削除されるので、それまでに Opus 5.5 へ切り替えるか `/fast off` にする、という警告が `fast-mode` に載った
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**作業ディレクトリの外への書き込みを拒む blockWritesOutsideWorkingDirectories の解説が載った**](#1-作業ディレクトリの外への書き込みを拒む-blockwritesoutsideworkingdirectories-の解説が載った):  
  `settings-reference` に h3「`permissions.blockWritesOutsideWorkingDirectories`」ができ、`true` にすると Write・Edit・NotebookEdit が `bypassPermissions` を含むどの権限モードでも作業ディレクトリの外のパスを拒み（v2.1.314 以降）、シェルのコマンド・MCP のツール・フックが動かすプログラムは制限しない、と載りました。書き込めるまま残る Claude Code 自身のファイル、作業ディレクトリの中でも拒む設定ファイル、外れる worktree のツールとその回避の方法も、`permissions`・`permission-modes`・`errors`・`worktrees`・`tools-reference` に載っています
2. [**Claude apps gateway で IdP のグループごとに上流を分け、合うポリシーを重ねられるようになった**](#2-claude-apps-gateway-で-idp-のグループごとに上流を分け合うポリシーを重ねられるようになった):  
  `claude-apps-gateway-config` に h4「Send each team to its own upstream」ができ、上流に `groups` の一覧を付けると、そのグループの開発者だけが最初の試行でもフェイルオーバーでもその上流に送られる（v2.1.314 以降）と載りました。h4「Apply every matching policy」もでき、`managed` に `policy_mode: layered` を置くと、最初に合うポリシーだけでなく合うポリシーがすべて重なる（v2.1.316 以降）と、重ね方の規則とともに説明されています
3. [**Claude apps gateway の Bedrock のガードレールに入力タグとフィルターのログが加わった**](#3-claude-apps-gateway-の-bedrock-のガードレールに入力タグとフィルターのログが加わった):  
  「ゲートウェイはガードレールの入力タグに対応していない」という警告が外れ、`guardrail` のブロックの `input_tagging`（`last_message`・`user_messages`・`all_messages`・`all_messages_and_system`。v2.1.316 以降）でプロンプト攻撃のフィルターが要る入力タグを付けられる、と載りました。上流に `guardrail_trace: true` を置くと、どのフィルターが要求を止めたかを一致した文なしに監査ログの `guardrail.trace` に残せます（v2.1.314 以降）
4. [**auto モードで止められた操作の承認が Recently blocked タブの 4 つの手順になった**](#4-auto-モードで止められた操作の承認が-recently-blocked-タブの-4-つの手順になった):  
  `auto-mode-config` の「Review denials」が、`/permissions` の **Recently blocked** タブ（これまでの **Recently denied**）を開き、行のコマンドか入力を確かめ、`r` で承認し、`Esc` で閉じる 4 つの手順に書き直されました。後で承認する・承認を取り消す・承認を捨てる操作と、タブから承認できない場合も加わり、`permission-modes` と `best-practices` のタブの名前も改められています
5. [**Opus 4.8 の fast mode が 2026年11月30日に削除されると告知された**](#5-opus-48-の-fast-mode-が-2026年11月30日に削除されると告知された):  
  `fast-mode` の冒頭に、Opus 4.8 の fast mode は 2026年10月30日に非推奨になり、2026年11月30日に削除される、その後も Opus 4.8 で fast mode をオンにしていると API が要求を拒む、という警告が加わりました。fast mode を続けるなら `/model` で Opus 5.5 に切り替え（v2.1.280 以降）、Opus 4.8 を標準の速さで使うなら `/fast off` を実行します
<!-- light:highlight-list:end -->

## 1. 作業ディレクトリの外への書き込みを拒む blockWritesOutsideWorkingDirectories の解説が載った

**`settings-reference` に h3「`permissions.blockWritesOutsideWorkingDirectories`」ができました。** このキーを `true` にすると、Write・Edit・NotebookEdit のツールは、`bypassPermissions` を含むどの権限モードでも作業ディレクトリの外のパスを拒みます（Claude Code v2.1.314 以降）。シェルのコマンド・MCP のツール・フックが動かすプログラムは制限しないので、シェルのコマンドの書き込み先を限るにはサンドボックスをオンにします。キーをオンにすると、Claude Code は `EnterWorktree` と `ExitWorktree` のツールも外すか、その呼び出しを拒みます。

- **Scope**: どのファイルでもよく、セッションが読み込むどれかのファイルの `true` が効く。そのため、リポジトリは自分で区画をオンにできても、ユーザーの区画を外すことはできない。クラウドのセッションでは、ファイルのツールが動くコンテナー自体が境界なので、キーが適用されないことがある
- **Type と既定**: `true` で区画をオンにし、`false` は未設定と同じ（ほかのファイルが `true` なら区画は効く）。既定は未設定で、作業ディレクトリの外への書き込みは権限モードに従う。managed settings の `permissions` を読めない間も区画はオンになる
- **試し方と解除**: Write のツールで作業ディレクトリの外（ホームディレクトリが作業ディレクトリでなければ `~/block-test.txt` など）にファイルを作らせると、呼び出しは拒まれる。解除するには、キーを設定しているすべての設定ファイルから外して Claude Code を再起動する

h4「What the write block refuses and what stays writable」によると、plan のファイル・scratchpad・バックグラウンドのセッションの `tmp` ディレクトリ・このプロジェクトの auto memory の `.md` ファイルのような Claude Code 自身のファイルは書き込めるままです。一方、作業ディレクトリの外の自分のファイルに加えて、次の書き込みも拒まれます。

- **Claude Code の設定ファイル**: 設定ファイルは区画を外せるので、作業ディレクトリの中でも拒む。設定ファイルは自分で編集する
- **リポジトリの設定だけが加えたディレクトリ**: `additionalDirectories` が `.claude/settings.json` だけに（git が未追跡と報告しない限り `.claude/settings.local.json` も）並べたもの
- **サブエージェントの worktree**: `isolation: worktree` のサブエージェントの worktree が作業ディレクトリの外にあるとき
- **リポジトリが選んだ auto memory**: リポジトリの設定の `autoMemoryDirectory` が指すディレクトリ

設定ファイル以外は、作業ディレクトリに加えれば通せます。h4「Let one directory through the read or write block」は、`blockReadsOutsideWorkingDirectories` か `blockWritesOutsideWorkingDirectories` が `true` の間に 1 つのディレクトリへ届かせるには、`/add-dir <directory>`・`--add-dir <directory>`・ユーザーか managed の設定の `additionalDirectories` のどれかで作業ディレクトリに加え、allow のルールではどちらの区画も通せない、と述べます（`/add-dir` は存在するディレクトリが要るので、サブエージェントの worktree にはリポジトリのルートの `.claude/worktrees` を名指す）。「Settings index」の表と `permissions` の **Type** にもこのキーが加わりました。

ほかのページも追従しています。

- **`permissions`**: 「Working directories」の下に h3「Block file-tool reads and writes outside the working directories」ができ、`blockReadsOutsideWorkingDirectories` と並べて 2 つのキーが説明された（読み取りの区画の段落はこの h3 に移った）
- **`permission-modes`**: 「Actions no mode auto-approves」に、このキーがオンの間の作業ディレクトリの外への書き込みの項目が加わった。「Protected paths」にも、このキーがオンの間は設定ファイルへの Write・Edit・NotebookEdit の書き込みをどの権限モードでも拒む、という段落と、保護されたファイルの一覧に、`remote-settings.json`（server-managed settings の保存したコピー）と、それとともに保つ署名・同期・同意のファイルの項目が加わった
- **`errors`**: h3「Setting blocks writes outside the working directories」と「Writes to Claude Code settings files are blocked」ができ、「Find your error」の表に 3 つのメッセージの行が加わった。前者の対処は `/add-dir`・`--add-dir`・`additionalDirectories`、設定ファイルなら自分で編集、キーをすべての設定ファイルから外して再起動、などで、どの設定ファイルにもキーがなければ `--settings` かホストのアプリケーションから来うる（managed settings の `permissions` を読めない間も拒む）とする。後者は、`--agents`・`--mcp-config` に渡したファイル、server-managed settings の保存したコピーとともに保つファイル、`managed-settings.d/` の行き先を解決できない間の `.json` ファイルも設定ファイルとして扱う、と述べる
- **`worktrees`**: h4「Claude has no `EnterWorktree` tool」ができた。キーがオンでも、対話的なセッションは `claude --worktree` で始めれば worktree で動き、バックグラウンドのセッションは `claude --bg --worktree` で始めるか、`worktree.bgIsolation` を `"none"` にするか、セッションを始めたディレクトリの下に `git worktree add` で作った worktree で編集させれば編集できる。ツールを戻すには `/status` で読み込んだ設定の源を確かめ、キーをすべてのファイルから外して再起動する（managed settings が設定しているなら管理者に尋ねる）。「Resume a worktree session」の `ExitWorktree` にも「セッションにそのツールがあるとき」が付いた
- **`tools-reference`**: h2「EnterWorktree tool behavior」ができ、表の `EnterWorktree` の行にあった説明（`path` で名指せる worktree・確認が出る場合・worktree の中から）がそこへ移り、ツールがない場合の項目が加わった。`ExitWorktree` の行にも、キーがオンなら外されるか拒まれる、と加わった
- **`settings`**: 「Exceptions to managed settings precedence」の表に、どのスコープの `true` も managed の `false` より優先する（v2.1.314 以降）という行が加わった

changelog の v2.1.314 の「`permissions.blockWritesOutsideWorkingDirectories` を追加」に対応します（2026年10月29日 版のサマリでは、ページのない changelog だけの項目として扱ったものです）。

- [すべての設定 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/settings-reference#permissions-blockwritesoutsideworkingdirectories)
- [All settings - Claude Code Docs (English)](https://code.claude.com/docs/en/settings-reference#permissions-blockwritesoutsideworkingdirectories)
- [権限を設定する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/permissions#block-file-tool-reads-and-writes-outside-the-working-directories)
- [Configure permissions - Claude Code Docs (English)](https://code.claude.com/docs/en/permissions#block-file-tool-reads-and-writes-outside-the-working-directories)
- [worktree を使用して並列セッションを実行する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/worktrees#claude-has-no-enterworktree-tool)
- [Run parallel sessions with worktrees - Claude Code Docs (English)](https://code.claude.com/docs/en/worktrees#claude-has-no-enterworktree-tool)

## 2. Claude apps gateway で IdP のグループごとに上流を分け、合うポリシーを重ねられるようになった

**`claude-apps-gateway-config` の「Multiple upstreams」の後に、h4「Send each team to its own upstream」ができました。** 上流に `groups` の一覧を付けると、一覧にある IdP のグループの開発者だけが、最初の試行でもフェイルオーバーでもその上流に送られます。チームごとの AWS のアカウントや Google Cloud のプロジェクトへ要求を分けるためのもので、どのプロバイダーにも付けられ、ゲートウェイのサーバーに Claude Code v2.1.314 以降が要ります。例は `payments-eng` と `search-eng` にそれぞれのアカウントの上流を割り当て、最後に `groups` のない共有の上流を置くもので、両方のグループにいる開発者は 3 つの上流を順に、どちらにもいない開発者は共有の上流だけを使う、という表が付いています。

- **書き方**: グループは IdP がグループのクレームで送るとおりに書く（`match.groups` も同じクレームを読む）。空の一覧や空の項目があるとゲートウェイは起動を拒むが、IdP と照合はしないので、誰にも合わない項目でも警告は出ない
- **順序**: `groups` のない上流は全員に使われるので、最後に置く（前に置くと、チームの要求をそのチーム自身の上流より先に取る）
- **1 つの上流に留める**: チームの上流が `403` で要求したモデルを拒むと、その行の次の上流が試される。チームを 1 つの上流に留めるには、すべての上流に `groups` を付け、ほかの上流がそのチームの開発者のいるグループを並べないようにする（そのチームのフェイルオーバーはなくなる）
- **警告**: v2.1.314 より前のゲートウェイは `groups` があると起動を拒むので、すべてのレプリカを上げてから加える。元に戻す前には、`groups` のある上流と、それを名指す `upstream_model` のキーと価格の上書きを外し、上流を 1 つは残す。`groups` のキーだけを外すと、その上流はすべての開発者に開かれる

h5「What happens when a developer is in no listed group」によると、すべての上流に `groups` があり、開発者がどれにも入っていなければ、ゲートウェイはプロバイダーに問い合わせずに `API Error: 400 you aren't in a group that can use this gateway. Ask your administrator to add you to one` を返します。ゲートウェイはトークンの更新のたびに開発者のグループを読み直すので、IdP が更新でグループを省くと、`oidc.allowed_groups` があれば更新を拒んでセッションが終わり、なければ `groups` のない上流へ移り、それもなければこのエラーになります。IdP の userinfo のエンドポイントがグループのクレームを返し、`oidc.google_groups` を設定していないなら、`oidc.userinfo_fallback` を `true` にするとそこからグループを補えます。

同じページの `upstreams`・「Upstream error messages」・「Bedrock in another AWS account」・「Multiple upstreams」・「Send the rates to signed-in clients」も `groups` に合わせて改められました（大幅更新 1 参照）。`claude-apps-gateway` の「Why Claude apps gateway」の Access control にも、IdP のグループが上流にも対応付けられる、と加わり、`claude-apps-gateway-deploy` には、「Upgrades」の警告（`groups` のキーだけを外すと全開発者に開かれる）・トラブルシューティングの表の上のエラーの行・「Request headers too large after sign-in」でグループのクレームを削るときに残す設定の一覧の上流の `groups` が加わっています。

**`managed` の下には h4「Apply every matching policy」ができました。** 既定（`first_match`）では、2 つの役割のポリシーに合う利用者には最初のポリシーだけが当たり、2 つ目のポリシーの deny のルールは効きません（この注意は `managed` の冒頭にも加わり、組織全体の deny のルールは `match: {}` のポリシーに置く、グループのポリシーのルールは利用者のトークンがそのグループを運ぶ間しか効かないから、という段落も加わった）。`policies` の横に `policy_mode: layered` を置くと、最初の `match: {}` のポリシーまで、利用者に合うポリシーがすべて重なります。ゲートウェイのサーバーに v2.1.316 以降が要り、キーを知らない版は起動を拒むので、すべてのレプリカを上げてから加え、前の版に戻す前に外します。各ポリシーは、下に並ぶポリシーの上に、基本の層と同じ規則で重ねられます。

- **許可の一覧・単一の値・`sandbox` のようなブロック**: 合うポリシーのうち先に並んだものから丸ごと取るので、2 つのグループの `availableModels` の一覧は足されない
- **deny の一覧とフックの配列**: 合うすべてのポリシーで足されるので、2 つのグループにいる利用者は両方のグループの deny のルールを受ける
- **`env`・`modelOverrides`・`skillOverrides`**: 名前ごとにマージし、その名前を設定する先に並んだポリシーの値を使う
- **`desktop` のキー**: 基本の `desktop` のブロックを受け継ぐ規則に従う

例の表では、`no-web` と `opus-users` の両方にいる利用者の `availableModels` は、`first_match` では `sonnet`、`layered` では `opus`・`sonnet` になり、`enforceAvailableModels` の `true` と `permissions.deny` の `WebFetch` はどちらでも効きます。警告は、重ねたポリシーがどれか 1 つよりも緩い規則になりうること（`match: {}` が `sandbox.enabled: true`、あるグループが `Bash` の許可、別のグループが `sandbox.enabled: false` なら、両方にいる利用者は `Bash` を許されサンドボックスはオフになる）を挙げ、その場合は `Bash` を許すポリシーを先に並べて `match: {}` の `sandbox` のブロック全体をそこへ写すよう勧めます。`layered` では、どれかのポリシーの `permissions.deny` か `permissions.ask` の `Read`・`Edit` のルールの `!` の否定や、`match: {}` 以外のポリシーの `disableAllHooks`・`allowedHttpHookUrls`・`httpHookAllowedEnvVars` などで、ゲートウェイは起動を拒みます。`claude-apps-gateway-on-aws` と `plugins/org` の「ゲートウェイは最初に合うポリシーを適用する」にも「既定では」が付きました。

changelog の v2.1.314（上流の `groups` の追加）と v2.1.316（`managed.policy_mode: layered` の追加）に対応します。

- [Claude apps gateway 設定 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/claude-apps-gateway-config#send-each-team-to-its-own-upstream)
- [Claude apps gateway configuration - Claude Code Docs (English)](https://code.claude.com/docs/en/claude-apps-gateway-config#send-each-team-to-its-own-upstream)
- [Claude apps gateway 設定 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/claude-apps-gateway-config#apply-every-matching-policy)
- [Claude apps gateway configuration - Claude Code Docs (English)](https://code.claude.com/docs/en/claude-apps-gateway-config#apply-every-matching-policy)

## 3. Claude apps gateway の Bedrock のガードレールに入力タグとフィルターのログが加わった

**`claude-apps-gateway-config` の Amazon Bedrock のガードレールの節で、「ゲートウェイはガードレールの入力タグに対応していない」という警告が外れ、h5「Add guardrail input tags」ができました。** `guardrail` のブロックに `input_tagging` を設定してゲートウェイを再起動すると、ガードレールのプロンプト攻撃のフィルターが要る入力タグをゲートウェイが付けます。ゲートウェイのサーバーに Claude Code v2.1.316 以降が要り、キーのない版は起動時に `Unrecognized key(s) in object: 'input_tagging'` で終わります。すべての `bedrock` の上流に同じ値を設定しないと、ゲートウェイは起動を拒みます。置き換わった警告は「既定ではゲートウェイは入力タグを付けないので、タグの付いた入力だけに Amazon Bedrock が適用するフィルターは動かない、付けるには `input_tagging` を設定する」となり、新しい警告は、Amazon Bedrock の文書によると要求に入力タグがあるとガードレールのすべてのフィルターがタグのない内容を評価しなくなるので、開発者が使うゲートウェイに設定する前にテスト用のゲートウェイで試す、と求めます。値は次の 4 つです。

- **`last_message`**: Claude の最後の返事の後の `user` のメッセージにタグを付ける（ツールの呼び出しも返事に数え、タグを付ける文がなければ、その返事の後の会話途中のシステムメッセージに付ける）。ガードレールがプロンプトを止めても、Claude Code では次のプロンプトが通りえ、Claude は止められたプロンプトを会話の一部として受け取る
- **`user_messages`**: `user` のメッセージ。止められたプロンプトを開発者が外すまで、セッションの後のプロンプトも止められうる
- **`all_messages`**: `user` と `assistant` のメッセージ（止められた後は `user_messages` と同じ）
- **`all_messages_and_system`**: システムプロンプトと、会話途中のシステムメッセージを含むすべてのメッセージ（同上）。Amazon Bedrock はプロンプト攻撃のフィルターにはシステムプロンプトを除いてユーザーの入力にタグを付けるよう勧めており、Claude Code 自身のシステムプロンプトにフィルターが反応すると要求が止まりうる

`user` のメッセージには system reminder のような Claude Code が加える文も入るので、テスト用のゲートウェイで普通の要求が止められないかを確かめます。Anthropic のテストでは、タグを付けたセッションでもプロンプトキャッシュの読み取りはプロンプトをまたいで続き、タグは入力トークンを増やさなかった、とあります。h5「What input tags don't cover」は、どの値でも、タグの付かない所へ意図的に文を置く開発者は止められないとし、ガードレールが評価すると当てにできない部分として、ゲートウェイがタグを付けない内容（値が外すメッセージ・ツールの定義・ツールの呼び出しの入力・画像・PDF など。`all_messages_and_system` 以外ではシステムプロンプトも）と、ツールの結果（ファイルの中身や Web のページ。Anthropic のテストでは、単語のフィルターはタグの有無にかかわらず評価しなかった）を挙げます。AWS のアカウントか組織がガードレールを強制しているなら、その扱いは Amazon Bedrock の文書を見ます。

**h5「Log which guardrail filter fired」もできました。** Bedrock の上流に `guardrail_trace: true` を設定して（`guardrail` のブロックの中ではなく横に置く）ゲートウェイを再起動し、開発者に要求を送り直してもらうと、監査ログのその要求の `guardrail.trace` のイベントで、どのフィルターが要求を止めたかを確かめられます（ゲートウェイのサーバーに v2.1.314 以降。前の版は `guardrail_trace` があると起動を拒む）。

- **出るとき**: フィルターが反応したか、ガードレールのアクションが `INTERVENED` のとき。一致した文（Bedrock のトレースの `match` のフィールドも）は含まない
- **フィールド**: `request_id`・`sub`・`email`・`upstream`・`action`・`filters`（`side` は `input` か `output`、`guardrail`、`policy` は `contentPolicy.filters` などの Bedrock のポリシーと一覧、ほかに `action`・`name`・`type`・`confidence`・`filterStrength`・`score`・`threshold` などを持ちうる）。AWS がフィルターの詳細を送らないと `filters` は空
- **読み方**: 開発者のイベントは `email` か `sub` で探す。1 つのストリームの要求が複数のイベントを出し、`filters` が空のものもあるので、同じ `request_id` のイベントをすべて読む
- **開発者に届くもの**: ゲートウェイは Bedrock のトレースのデータを、ストリームでもそうでなくても各返事から外すので、開発者には届かない。`guardrail_trace` のある上流でも、クライアントが `/v1/messages` の本文に `amazon-bedrock-*` のフィールドを送ると 400 を返す

`claude-apps-gateway-deploy` の「Logs」の監査イベントの一覧にも、`guardrail.trace` がどのフィルターが反応したかを一致した文なしに記録する、と加わりました。changelog の v2.1.316（`guardrail.input_tagging` の追加）と v2.1.314（`guardrail_trace` の追加）に対応します。

- [Claude apps gateway 設定 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/claude-apps-gateway-config#add-guardrail-input-tags)
- [Claude apps gateway configuration - Claude Code Docs (English)](https://code.claude.com/docs/en/claude-apps-gateway-config#add-guardrail-input-tags)
- [Claude apps gateway 設定 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/claude-apps-gateway-config#log-which-guardrail-filter-fired)
- [Claude apps gateway configuration - Claude Code Docs (English)](https://code.claude.com/docs/en/claude-apps-gateway-config#log-which-guardrail-filter-fired)

## 4. auto モードで止められた操作の承認が Recently blocked タブの 4 つの手順になった

**`auto-mode-config` の「Review denials」が、`/permissions` の **Recently blocked** タブ（これまでの **Recently denied**）を使う 4 つの手順に書き直されました。** これまでは、**Recently denied** のタブで拒否された操作に `r` を押して再試行の印を付けると、ダイアログを出たときに Claude にその呼び出しを再試行してよいと伝えて会話を再開する、という 1 段落でした。

1. **タブを開く**: セッションで `/permissions` を実行し、**Recently blocked** のタブを選ぶ
2. **操作を確かめる**: 操作の行を選び、一覧の下のコマンドか入力を読む。Claude かツールが書いた行の説明ではなく、コマンドか入力で判断する
3. **操作を承認する**: `r` を押して操作を承認し、Claude に再試行させる
4. **ダイアログを閉じる**: `Esc` で閉じて承認を適用する。`/permissions` を開いたとき Claude が動いていたなら、終わってからメッセージを送ると Claude が再試行する。そうでなければ何も送らなくても Claude は続けて再試行しうる。しなければ、「Approvals you state in conversation」のとおり次のメッセージで操作を名指す

承認しても権限のルールは加わらず、auto モードでは再試行した操作がもう一度確かめられるので、また止められえます。これから先も通すには `allow` のルールを加えます。すぐに再試行させたくない場合の操作も加わりました。

- **後で承認する**: 行で `Enter`、続けて `Esc`。行はタブから消え、Claude は次のメッセージの後、Claude が終わってから操作を再試行しうる。ほかの行で `r` も押した場合は、`Enter` の行はタブに残って Claude には知らされないので、次に開いたときに承認するか、両方で `r` を押す
- **承認を取り消す**: `Esc` の前に、`Enter` と `r` のどちらで承認した行でも、その行で `Enter`
- **閉じて承認を捨てる**: `Ctrl+C` を 2 回

行が `This row can't be approved here` と出る（コマンドか入力をすべて示せない）ときは次のメッセージで Claude に伝え、行がなく会話に `Not run` か分類器のエラーがあるとき（分類器が判定を返さなかった）は `errors` の「Auto mode cannot determine the safety of an action」を見ます。どちらもタブからは承認できません。

「Fix a denial with an allow rule, an environment entry, or a retry」も改められ、通知の例は `bash blocked by auto mode · /permissions · Auto mode: [Data Exfiltration]` の形に、分類器が危ないと判じた呼び出しの行は `Blocked by auto mode` に（これまでは `[Production Deploy]` などの理由の付いた `Denied by auto mode classifier`）なりました。`PermissionDenied` のフックが `reason` を読むなら、`Auto mode:` の接頭辞はなく、`No reason provided` の代わりに `Blocked by classifier` のような文になる、とも加わっています。`permission-modes` の「When auto mode falls back」（分類器が判定を返さない場合も「拒む」から「止める」に）と `best-practices` も **Recently blocked** と「Claude が再試行できるよう操作を承認する」に言い換えられ、現行の通常のページからは **Recently denied** の名前が消えました（残るのは changelog と過去の週のダイジェストだけです）。changelog の v2.1.314 の、タブの改称（フッターが `Esc` で印を付けた行をどうするかを示す）と、全文を読めない呼び出しの承認を拒む変更に対応します。

- [オートモードの設定 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/auto-mode-config#review-denials)
- [Configure auto mode - Claude Code Docs (English)](https://code.claude.com/docs/en/auto-mode-config#review-denials)
- [権限モードを選択する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/permission-modes#when-auto-mode-falls-back)
- [Choose a permission mode - Claude Code Docs (English)](https://code.claude.com/docs/en/permission-modes#when-auto-mode-falls-back)

## 5. Opus 4.8 の fast mode が 2026年11月30日に削除されると告知された

**`fast-mode` の冒頭に、Opus 4.8 の fast mode は 2026年10月30日に非推奨になり、2026年11月30日に削除される、という警告が加わりました。** その日の後も Opus 4.8 で fast mode をオンにしたままだと、API が要求を拒みます。それまでに次のどちらかをします。

- **fast mode を続ける**: `/model` で Opus 5.5 に切り替える（Claude Code v2.1.280 以降）。切り替えても fast mode はオンのまま。新しいセッションがまだ Opus 4.8 で始まるなら、`model-config` の「A new session starts on a different model than you picked」を見る
- **Opus 4.8 を標準の速さで使い続ける**: `/fast off` を実行する

ページには、fast mode は Opus 5.5・Opus 5・Opus 4.8 で使える、という記述と、Opus 4.7 の fast mode は 2026年06月25日に非推奨になり 2026年07月24日に外された、という前例が前から載っています。changelog の v2.1.316 にも、削除の後は Opus 4.8 の fast mode の要求がエラーを返し、標準の Opus 4.8 にはフォールバックしない、速さを保つには Opus 5.5 に移る、という項目があります。同じページの「See where fast mode spend appears」の **Speed (Research Preview)** は **Speed (research preview)** に表記が改められました。

- [fast mode で応答を高速化する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/fast-mode)
- [Speed up responses with fast mode - Claude Code Docs (English)](https://code.claude.com/docs/en/fast-mode)

## 新規追加されたページ

<!-- light:new-pages:start -->
（今回の対象期間に新規追加・削除されたドキュメントページはありません。`llms.txt` は変わっておらず、`llms-full.txt` に展開されている固有のページも 228 のままで、`Source:` の行が 231 あり 3 ページが 2 回展開されている状態も前回と同じです）
<!-- light:new-pages:end -->

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
- [**Claude apps gateway configuration**](#1-claude-apps-gateway-configuration) ([日本語](https://code.claude.com/docs/ja/claude-apps-gateway-config#multiple-upstreams) / [English](https://code.claude.com/docs/en/claude-apps-gateway-config#multiple-upstreams)):  
  229 行（追加 218・削除 11）が変わりました。ハイライト 2・3 の 6 つの見出し（h4 2・h5 4）のほか、上流の選び方・すべての上流が失敗したときのエラー・別の AWS アカウントの上流・料金の配り方・`managed` の冒頭の記述が `groups` と `policy_mode` に合わせて改められました
- [**Error reference**](#2-error-reference) ([日本語](https://code.claude.com/docs/ja/errors#claude-code-didnt-send-your-claude-ai-login) / [English](https://code.claude.com/docs/en/errors#claude-code-didnt-send-your-claude-ai-login)):  
  77 行（追加 66・削除 11）が変わりました。ハイライト 1 の 2 つの h3 のほか、管理者が設定した API キーヘルパーが効かないので claude.ai のログインを送らなかった、というエラーの h3 ができ、LLM ゲートウェイでツール検索を確かめる方法が 5 か所で改められました
- [**All settings**](#3-all-settings) ([日本語](https://code.claude.com/docs/ja/settings-reference#useautomodeduringplan) / [English](https://code.claude.com/docs/en/settings-reference#useautomodeduringplan)):  
  57 行（追加 50・削除 7）が変わりました。ハイライト 1 のキーの h3 と 2 つの h4 のほか、`useAutoModeDuringPlan`・`env` で無視される変数・`idleCompaction`・`sandbox.network.allowMachLookup`・読み取りの区画の解除の記述が改められました
<!-- light:updated-pages:end -->

**行数の数え方**: `llms-full.txt` の生の差分（追加 739 行・削除 141 行）のハンクを、head 側の `Source:` 行でページに振り分けた値です（ページの並びは変わっておらず、ページ単位の合計は生の差分と一致します）。base と head はどちらも 2026年10月31日 の取り込みからの引用ブロックの書式なので、正規化はしていません。この値が 50 行以上のページを大幅更新として挙げました。changelog（追加 103 行）は新しい 1 リリースの分なので大幅更新には入れず、「軽微な更新」で扱っています。空行（と `>` だけの行）を除くと、`claude-apps-gateway-config` は 168 行、`errors` は 60 行、`settings-reference` は 41 行で、`settings-reference` は 50 行に届きませんが、これまでどおり生の行数で判定しました。次点は `auto-mode-config` の 39 行（追加 33・削除 6。ハイライト 4）、`llm-gateway-protocol` の 35 行（追加 30・削除 5）、`desktop` の 33 行（追加 23・削除 10）です。

## 1. Claude apps gateway configuration

ページの差分のうち、h4「Send each team to its own upstream」とその h5、h4「Apply every matching policy」はハイライト 2、ガードレールの 3 つの h5 と警告の置き換えはハイライト 3 のとおりです。そのほかは次のとおりです。

- **`upstreams`**: ゲートウェイは要求したモデルを解決する最初の上流へ推論を送る、に、開発者を外す `groups` の一覧のある上流は飛ばす、が加わった
- **「Upstream error messages」**: 試したすべての上流がフェイルオーバーする形で失敗し、`429`・`401`・`403`・`404`・`501` のどれも返らなかったときの `502` の `all upstreams failed (N attempted)` の N は、`upstreams` の項目の数（要求したモデルを出さないので飛ばしたものも含む）から、`groups` の一覧が開発者を外す上流を除いた数になった
- **「Bedrock in another AWS account」**: 最後の項目が 3 つに分けられた。`groups` の一覧がなければ、ゲートウェイが認めた開発者は誰でもこの上流を使え、使えるモデルを限るには `managed` のポリシーで `availableModels` を設定する、となった（これまでは「どの開発者がどのモデルを使えるかは `managed` が決める」）。カスタムの id で別のアカウントへのフェイルオーバーを防ぐ方法と、組み込みのモデルの名前の要求もこの上流に届きうるので最後に並べる、という内容は同じ
- **「Multiple upstreams」**: 「すべての要求は最初の上流から始まり、後の上流に届くのは前のすべてが失敗したかモデルを出さないときだけ」という文が、要求が上流を飛ばすのは、上流が失敗したとき・要求したモデルを出さないとき・`groups` の一覧が開発者を外すとき、の 3 つの箇条書きになった。表には「Different teams」（チームの上流に `groups` の一覧を付ける）の行が加わり、「Model-scoped routing」の行は、カスタムの id は `upstream_model:` の対応表にない上流を飛ばし、`models` の一覧のある上流（`mantle` の上流はこの一覧が要る）はそのモデルにだけ試される、に短くなった。組み込みのモデルの扱いは新しい「Built-in model routing」の行に分かれ、`models` も `groups` もない上流で組み込みのモデルを順に試し、対応表に項目がなければプロバイダーの既定の ID を使う、となった
- **「Send the rates to signed-in clients」**: 段落が 2 つに分かれ、ポリシーに合う開発者は「各モデル ID を出す最初の上流の」料金を見る、から、`pricing` の料金を見る、に短くなった。ゲートウェイが加えるものの一覧には、`groups` の一覧のある上流があるモデル ID を出す最初の上流なら、ゲートウェイはその ID の行を加えず、開発者には Claude Code 自身の料金（Claude Code がその ID を知っていればモデルの標準の料金）に `multiplier` を掛けたものが見える、という項目が加わった
- **`managed`**: ポリシーは順に評価され「既定では」最初に合うものを選ぶ、と言い換えられ、2 つの役割のポリシーに合う利用者には最初のものしか当たらない、という注意と、組織全体の deny のルールは `match: {}` のポリシーに置く、という段落が加わった（ハイライト 2 参照）

- [Claude apps gateway 設定 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/claude-apps-gateway-config#multiple-upstreams)
- [Claude apps gateway configuration - Claude Code Docs (English)](https://code.claude.com/docs/en/claude-apps-gateway-config#multiple-upstreams)
- [Claude apps gateway 設定 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/claude-apps-gateway-config#send-the-rates-to-signed-in-clients)
- [Claude apps gateway configuration - Claude Code Docs (English)](https://code.claude.com/docs/en/claude-apps-gateway-config#send-the-rates-to-signed-in-clients)

## 2. Error reference

ページの差分のうち、h3「Setting blocks writes outside the working directories」「Writes to Claude Code settings files are blocked」と「Find your error」の表の 3 行はハイライト 1 のとおりです。そのほかは次のとおりです。

- **新しい h3「Claude Code didn't send your claude.ai login」**: `Claude Code didn't send your claude.ai login, because the API key helper your administrator set isn't in effect. …` というメッセージは、Claude Code がプロンプトを拒んだことを意味し、claude.ai のログインを使う間は再起動しても拒み続ける。メッセージは、組織の managed settings がヘルパーを上書きしているかもしれないとし、管理者に、キーヘルパーとその API のアドレスを効かせたままにするか、managed settings で Anthropic の API のアドレスを名指すか、キーヘルパーを外すよう頼む、と続く。メッセージ全体を管理者に送り（管理者ができる変更が並ぶ）、`/status` の `Setting sources` の行（あれば `Skipped sources` の行も）をコピーして、マシンにどの managed の源があるかを伝える。自分で設定を管理しているなら `server-managed-settings` の新しい h4 を見る（「軽微な更新」参照）。「Find your error」の表の Authentication にもこのメッセージの行が加わった。この拒否には v2.1.314 以降が要り（`server-managed-settings`）、changelog の v2.1.314 には、MDM と remote settings でベース URL か `apiKeyHelper` が違うときの、保存した claude.ai・Team・Enterprise のログインの挙動の改善があります
- **LLM ゲートウェイでツール検索を確かめる方法（4 か所）**: 「API Error: 500 Internal server error」「API Error: 401 Invalid authentication credentials」「Unable to connect to API」「There's an issue with the selected model」で、ゲートウェイを指していてすべての要求（かすべてのモデル）が失敗するときの項目が、「ゲートウェイが Claude Code の既定で送るツール検索のフィールドを拒んでいないか、`ENABLE_TOOL_SEARCH=false` を設定して試す」から、「ゲートウェイとその上流がツール検索のフィールドを受け付けるか確かめる。既定では `defer_loading` のツールのフィールドと `tool_reference` のブロックを、それらを有効にする `anthropic-beta` ヘッダー付きで送る」に改められた
- **「Extra inputs are not permitted」**: メッセージが `defer_loading` か `tool_reference` を名指すときの対処が、v2.1.305 以降に更新する（Claude Code がツール検索のフィールドなしで要求をもう一度送る。`llm-gateway-protocol` の「Retry without tool search」へのリンク付き）の 1 項目になり、更新できないか更新しても出るときに `ENABLE_TOOL_SEARCH=false` をシェルか設定の `env` に設定する、という子項目が外れた
- **「Auto mode cannot determine the safety of an action」**: 対話的なセッションでこのメッセージの代わりに出る淡い `Not run · auto mode's check had no usable answer` の行は、これまでも挙げていたサーバーが判定を返さなかった場合に加えて、リモートのセッションの外では `Auto mode could not evaluate` で始まるメッセージの代わりにも出うる、と改められた
- **「You've hit your session limit」**: 残りを見る方法の Desktop の使用量のリングから「モデルピッカーの隣の」が外れ、「継続的に見る」も「見る」になった（`desktop` で、リングはプロンプトの欄の下の行にある、と改められたのに合わせたもの）
- **「Unrecognized model ID on a request」**: `query_source` の説明が「たとえば `-p` の実行の主な会話では `sdk`、サブエージェントでは `agent:` で始まる」に、行を 1 回だけ書く単位が「モデルの文字列」から「モデル ID」に、バックグラウンドの機能のリンク先が `costs` の「Background token usage」から `model-config` の「Environment variables」に改められた

- [エラーリファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/errors#claude-code-didnt-send-your-claude-ai-login)
- [Error reference - Claude Code Docs (English)](https://code.claude.com/docs/en/errors#claude-code-didnt-send-your-claude-ai-login)
- [エラーリファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/errors#extra-inputs-are-not-permitted)
- [Error reference - Claude Code Docs (English)](https://code.claude.com/docs/en/errors#extra-inputs-are-not-permitted)

## 3. All settings

ページの差分のうち、h3「`permissions.blockWritesOutsideWorkingDirectories`」と 2 つの h4、「Settings index」の行、`permissions` の **Type** への追加はハイライト 1 のとおりです。そのほかは次のとおりです。

- **`useAutoModeDuringPlan`**: **Scope** に、これらのファイルか `--settings` の `false` はオフにするが、`--setting-sources` のようなオプションで外したユーザーかローカルのファイルの `false` は数えない（外したファイルを無視するのは v2.1.314 以降）という子項目が加わり、`true` の説明は「auto モードが使えるとき、分類器が計画の間のシェルのコマンドを確かめる」に短くなった（これまでの「これらのファイルのどれかの `false` はそれでもオフにする」はこの子項目に置き換わった）。`managed-settings` の「Keys read from every admin source」と `settings` の「Exceptions to managed settings precedence」の表も追従している。changelog の v2.1.314 には、`--setting-sources` で外した設定ファイルが auto モードのルールや保存した権限の同意などを供給し続ける問題の修正があります
- **「Variables Claude Code ignores in env」**: プロジェクトとローカルの設定で無視される変数に、claude.ai のサインインを設定する `CLAUDE_CODE_OAUTH_TOKEN`・`CLAUDE_CODE_OAUTH_REFRESH_TOKEN`・`CLAUDE_CODE_OAUTH_SCOPES` の項目が加わった（`env-vars`・`authentication`・`network-config` も追従。「軽微な更新」参照）
- **`idleCompaction`**: 既定でオンになる条件から「Claude Code が Anthropic から機能フラグを取得できる」が外れ、`/config` に **Idle compaction** の行が出ない原因の「機能フラグが使えない」は「v2.1.314 より前の版で」に限られた（`env-vars` の「Features that need feature-flag fetching」の一覧からも、アイドルの圧縮が外れた）。changelog の v2.1.314 には、アイドルの圧縮がテレメトリーをオフにした加入者でも、1 時間のプロンプトキャッシュがオンなら Bedrock・Vertex・Foundry・LLM ゲートウェイでも動くようにする変更があります
- **`sandbox.network.allowMachLookup`**: サンドボックスの中のコマンドは列挙した各サービスへサンドボックスの外まで届き、サンドボックスはそれらのサービスがコマンドのためにすることを閉じ込めない、と加わった（`sandboxing` の「Security limitations」にも同じ項目が加わった）
- **`permissions.blockReadsOutsideWorkingDirectories`**: 区画を解除する文がコード例の直後へ移り、キーをすべての設定ファイルから外した後に「新しいセッションを始める」から「動いている各セッションを再起動する」に改められた

- [すべての設定 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/settings-reference#useautomodeduringplan)
- [All settings - Claude Code Docs (English)](https://code.claude.com/docs/en/settings-reference#useautomodeduringplan)
- [すべての設定 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/settings-reference#variables-claude-code-ignores-in-env)
- [All settings - Claude Code Docs (English)](https://code.claude.com/docs/en/settings-reference#variables-claude-code-ignores-in-env)

## 軽微な更新

<!-- light:minor-updates:start -->
今回の差分は **2 ファイル**（`llms-full.txt` と見出しマップ）で、`llms.txt` は変わっていません。`llms-full.txt` の生の差分は追加 739 行・削除 141 行で、ページの並びは変わっていません。228 ページ中 **47 ページ**が変わり、changelog が 103 行（追加のみ）、ほかの 46 ページが 777 行（追加 636・削除 141）で、ページ単位の合計は生の差分と一致します（2 回展開されている 3 ページはどれも変わっていません）。大幅更新の 3 ページを除く **43 ページ**と、changelog に加わった **v2.1.317（2026年11月03日）** を以下にまとめます。

`llms-full.txt` の総行数は **126,454 行から 127,052 行へ 598 行増え**ました（生の差分の差し引き 739 − 141 と一致）。`Source:` の行は 231、固有のページは 228 のままで、2 回展開されている 3 ページ（`plugins/create`・`plugins/install`・`plugins/mods/overview`）も前回と同じです。コードフェンスの外の見出しは、引用の中の見出しも数えると 6,007 から 6,031 へ、行頭が `#` の見出しだけを数えると 5,996 から 6,020 へ、どちらも 24 増えました（加わった 24・外れた 0）。changelog の収録リリースは 434 から 435 になりました。v2.1.317 は 87 項目（追加 10・変更 7・改善 8・バグ修正 62）で、単一のリリースなので各項目への版の併記は省いています。v2.1.317 の項目で今回の通常のページの変更に対応するのは、クラウドのセッションの MCP のリンクのカード（`mcp` の新しい h3）くらいで、多くは changelog だけで確認できる変更です。今回の通常のページの変更の多くは、前回までに changelog に載った v2.1.314・v2.1.316 の機能の解説です。

**新機能**

- 作業ディレクトリの外への書き込みを拒む `permissions.blockWritesOutsideWorkingDirectories`（`permissions`・`permission-modes`・`worktrees`・`tools-reference`・`settings`。詳細はハイライト 1 参照）
- Claude apps gateway の上流の `groups` と `managed.policy_mode: layered`（`claude-apps-gateway`・`claude-apps-gateway-deploy`・`claude-apps-gateway-on-aws`・`plugins/org`。詳細はハイライト 2 参照）
- Claude apps gateway の Bedrock のガードレールの `input_tagging` と `guardrail_trace`（`claude-apps-gateway-deploy`。詳細はハイライト 3 参照）
- `/schedule` に、新しいクラウドのスケジュールしたタスクが頼んでいないコネクターを得たときの警告を追加。外し方も示します
- Web かシェルのツールの呼び出しがアカウントのメールアドレスをネットワークに送る前に尋ねる確認を追加
- Agent SDK のフックのコールバックに `onFailure: "block"` を追加。失敗したコールバックが、操作を通さずに止めます
- 組織の remote managed settings がセッションに読み込まれていないとき、Claude Desktop の Code タブに通知を出し、読み込まれたときにもう 1 つ通知を出すよう追加
- サブエージェントのツールの呼び出しに auto モードの確認が答えを持たないときの通知を追加。これまでは主な画面に何も残りませんでした
- OTel のメトリクス・イベント・スパンに `anthropic.plan`・`anthropic.seat_type`・`anthropic.provider`・`anthropic.custom_base_url` を追加
- Claude apps gateway の管理 API に、過去の支出を期間で、全体・開発者ごと・日ごと・IdP のグループごとに読むコストのレポート `GET /v1/organizations/analytics/cost` を追加
- `admin:` を設定した Claude apps gateway に、各開発者の IdP のグループの日ごとの記録を追加。`admin.identity_retention_days` の間保たれ、コストのレポートはこれでグループ分けします
- `CLAUDE_CODE_DISABLE_NESTED_SESSION_ID` を追加。セルフホストのランナーで `1` にすると、セッションの中で動く `claude -p` が、以前の版と同じくそのセッションの ID とトランスクリプトを使います
- [Cloud sessions] クラウドのセッションにリンクのカードを追加。MCP サーバーが訪れるよう求めるリンクを、要求が見過ごされる代わりに開くか断れます（下の `mcp` の新しい h3 に対応）
- **クラウドのセッションで MCP の elicitation の要求に答える方法が載った**（`mcp` の新しい h3「Answer an elicitation request in a cloud session」）。クラウドのセッションの Claude のタスクが MCP サーバーの要求（値やサインインなど）を待ち、その要求が claude.ai/code か Desktop の **Code** タブにカードとして出たら、カードで答えます。フォームのモードは項目を埋めて **Submit** を、URL のモードは **Open link** で開いた流れを終えてからカードの **I’m done, continue** を押します。断るには **Decline** を押し、サーバーが応えると Claude は続けます。どちらにもカードがなければそこでは答えられず、自分のセッションなら停止のボタンでターンを終えます。節の冒頭の、elicitation のダイアログを出すという説明にも「ターミナルに」が付きました。changelog の v2.1.317 のリンクのカードの追加に対応します — [日本語](https://code.claude.com/docs/ja/mcp#answer-an-elicitation-request-in-a-cloud-session) / [English](https://code.claude.com/docs/en/mcp#answer-an-elicitation-request-in-a-cloud-session)
- **サブエージェントのトランスクリプトから /btw で尋ねられると載った**（`interactive-mode` の新しい h3「Ask /btw about a subagent」・`sub-agents`）。サブエージェントのトランスクリプトを開いていると、Claude は `/btw` に主な会話ではなくそのトランスクリプトから答えるので、サブエージェントが何をしたかを尋ねられます。そのトランスクリプトからの後の `/btw` は、そこで尋ねた横の質問だけを見ます（v2.1.314 以降）。agent team の teammate のトランスクリプトからは、主な会話から答えます。同じページの `/btw` の説明も「会話全体か開いているサブエージェントのトランスクリプトを見る」に改められ、`sub-agents` の「Observe and steer running forks」には「v2.1.314 以降、`/btw` は開いているトランスクリプトから答え、ほかの組み込みのコマンドは主な会話へ行く」と加わり、「Choose between subagents and main conversation」からは `/btw` が全体のコンテキストを見る、という部分が外れました。changelog の v2.1.314 の、サブエージェントの開いたトランスクリプトから尋ねた `/btw` が主な会話から答える問題の修正に対応します — [日本語](https://code.claude.com/docs/ja/interactive-mode#ask-btw-about-a-subagent) / [English](https://code.claude.com/docs/en/interactive-mode#ask-btw-about-a-subagent)
- **LLM ゲートウェイが `anthropic-beta` の値を名指しで拒んだときの再試行と、拒まれた値を省く期間の表が載った**（`llm-gateway-protocol` の新しい h4「Retry without a rejected beta value」「How long a rejected beta value stays out」）。`400` が、この再試行の対象の `anthropic-beta` の値を名指しで拒むと、ゲートウェイは同じ要求をその値なしでもう一度受け取ります（対象の値の多くは v2.1.314 以降）。ゲートウェイが返す `400` のメッセージが、API の `Unexpected value(s)` の文か、`capability_rejected: beta_header:` に値を続けたトークンで値を運べば、ゲートウェイ側の変更は要りません。advisor やツール検索のように専用の再試行がある値、Claude Code が知らない値（開発者が `ANTHROPIC_BETAS` で設定した値は要求に残って `400` が続くので、項目を外してもらう）、値を名指さない素の `invalid beta flag`（Claude Code が推測し、それでも `400` が届くならゲートウェイに値を名指させる）は対象外です。表は、advisor のツールの型かその値は同じベース URL への要求で Claude Code が終わるまで（その間 `/advisor` は使えない）、`output_config.effort` かその値は同じモデルへの要求で終わるまで、`context_management` かこの再試行の対象の値は同じ会話の要求で、会話が終わるか主な会話の圧縮のように Claude Code がプロンプトを作り直すまで省き、エラーのメッセージが拒否についての API 自身の文で始まるか `beta_header:` のトークンを運ぶなら、拒まれた要求が名指したモデルの新しい会話（`/clear` の後も）でも Claude Code が終わるまで省く、と整理しています。advisor・effort・`context_management` の各項目の「後の要求」もこの表へのリンクに揃えられました。「Retry without tool search」は、ツール検索を名指すか原因が分からない `400` か `422` の後に送り直し、成功した後はその会話の後の要求も省く、と改められ、`ENABLE_TOOL_SEARCH=false` を設定させる文が外れました。changelog の v2.1.314 の、ゲートウェイかクラウドのプロバイダーが Claude Code のベータのヘッダーを名指しで拒むと要求が失敗する問題の修正に対応します — [日本語](https://code.claude.com/docs/ja/llm-gateway-protocol#retry-without-a-rejected-beta-value) / [English](https://code.claude.com/docs/en/llm-gateway-protocol#retry-without-a-rejected-beta-value)
- **マシンの `apiKeyHelper` が効かないとき claude.ai のログインでのプロンプトを拒むことが載った**（`server-managed-settings` の新しい h4「When a machine's `apiKeyHelper` isn't in effect」）。server-managed settings が選ばれた源のとき、マシンの managed settings のファイルか MDM のポリシーの `apiKeyHelper` は効きません。そのファイルかポリシーがクラウドのプロバイダーをオンにするか、どれかの源が Anthropic 以外の API のアドレスを設定していて、server-managed settings がヘルパーを設定せず Anthropic の API のアドレスも名指さないと、保存した claude.ai のログインを使うセッションで Claude Code はプロンプトを拒みます（v2.1.314 以降）。解消するには、ヘルパーとその API のアドレスを効かせたままにするか、server-managed settings で Anthropic の API のアドレスを名指すか、マシンのポリシーからヘルパーを外します。利用者に出るエラーは `errors` の新しい h3 です（大幅更新 2 参照） — [日本語](https://code.claude.com/docs/ja/server-managed-settings#machine-apikeyhelper-not-in-effect) / [English](https://code.claude.com/docs/en/server-managed-settings#machine-apikeyhelper-not-in-effect)
- **Claude Desktop の SSH のエラーのカードの表に 2 行が加わった**（`desktop` の「SSH connection fails after you log in」）。`Ask <host>'s administrator to let Claude's server run`（`[SERVER_NOT_RUNNABLE]` か `[SETUP_DIR_NOEXEC]`）は、要件のとおりそのマシンの `~/.claude/remote/` からプログラムを動かせるよう管理者に頼み、`Try again in a few minutes`（`[DOWNLOAD_BUSY]`）は、Anthropic のダウンロードのサーバーかコンピューターのネットワークのプロキシが混んでいると報告したので数分待ってから試し直す（繰り返すなら、プロキシがダウンロードを制限していないかそのネットワークの管理者に尋ねる）、というものです — [日本語](https://code.claude.com/docs/ja/desktop#ssh-connection-fails-after-you-log-in) / [English](https://code.claude.com/docs/en/desktop#ssh-connection-fails-after-you-log-in)
- **クラウドの環境に Chrome for Testing が入っていると載った**（`cloud-environments` の「Installed tools」）。表に「Browser」の行が加わり、`/usr/bin/google-chrome` の Chrome for Testing と、そのパスを指す `CHROME_PATH` の環境変数が載りました — [日本語](https://code.claude.com/docs/ja/cloud-environments#installed-tools) / [English](https://code.claude.com/docs/en/cloud-environments#installed-tools)
- **Agent SDK の起動の失敗の理由に `sandbox_required_unavailable` が加わった**（`agent-sdk/typescript` の `startup_failure_reason`）。`failIfUnavailable` がオンでサンドボックスを起動できないときの値で、`errors` の文は `Set sandbox.failIfUnavailable=false to allow unsandboxed execution.` で終わります（Agent SDK v0.3.314 以降）。`SDKStartupFailureReason` の型にもこの値が加わり、`startup_failure_reason` が持ちうる値をこの型が並べる、という前置きも付きました — [日本語](https://code.claude.com/docs/ja/agent-sdk/typescript#startup_failure_reason) / [English](https://code.claude.com/docs/en/agent-sdk/typescript#startup_failure_reason)

**機能改善**

- auto モードの **Recently blocked** タブでの承認の手順（`auto-mode-config`・`permission-modes`・`best-practices`。詳細はハイライト 4 参照）
- Opus 4.8 の fast mode の削除の告知（`fast-mode`。詳細はハイライト 5 参照）
- 動いているバックグラウンドのエージェントへの SendMessage のメッセージが早く届くよう変更。そのエージェントの動いているコマンドは、止められずにバックグラウンドへ移ります
- 主な会話と違うモデルのサブエージェントと teammate が、セッションの effort のレベルではなく、そのモデルに保存した effort のレベルか既定を使うよう変更
- 終了するとき、プラグインのモニターについては「Background work is running」の確認を出さないよう変更
- 組み込みの `plugin-authoring` スキルが、作った mod が動いた後に一度だけ、mod の共有を手伝うと申し出るよう変更
- Read ツールの「前回の Read から変わっていない」という短い返事を廃止。変わっていないファイルを読み直すと中身を返します
- [Cloud sessions] 管理者の設定の組織の環境のダイアログを、個人のダイアログの短いレイアウトに変更。各セクションは行から開き、保存していない入力があると閉じる前に尋ねます
- [Claude Tag] Slack に新しく貼った成果物のリンクが、Slack のサイドパネルではなく、Claude で成果物を開く Open のボタン付きの簡単なカードを示すよう変更
- Azure の資格情報を読み込めないときの Microsoft Foundry のエラーを改善。確かめるか更新するよう伝え、`cloud_credential_error` として報告します
- `/design-sync` を改善。デザインシステムが Claude に移ったときは最初にそう伝え、アップロードで失敗する代わりにビルドの前に止まります
- 必要な Claude apps gateway に届かないときの起動のエラーを改善。サインインではなくネットワークを指し、ゲートウェイの TLS の証明書を検証できないときはそう伝えます
- 終了時に出る「Resume this session with」のヒントを改善。起動したときのフラグ（例: `--chrome --debug`）を `--resume` の前に繰り返します
- セルフホストのランナーのサーバーのエラーからの回復を改善。501 と 529 以外の 5xx の後、ランナーの次のポーリングは失敗した接続を使い回さず、新しい接続を開きます
- セルフホストのランナーのセッションのサーバーのエラーからの回復を改善。501 と 529 以外の 5xx の後、セッションは失敗した接続を使い回さず、新しい接続を開きます
- 接続が応えなくなったときのセルフホストのランナーのセッションの回復を改善。ハートビートに答えがないと、アイドルの接続を順に試す代わりに新しい接続を開きます
- Remote Control: アプリが名前を付けないときのフォークの名前を改善。長い名前も「(fork)」の終わりを保ち、`claude remote-control` で始めたセッションでは「Name (fork)」のフォークが「Name (fork 2)」になります
- **Claude Desktop の SSH の接続のタイムアウトの持ち時間が表になった**（`desktop` の「Raise the SSH connection timeout」）。冒頭が、ジャンプホストか `ProxyCommand` 経由で接続する間にセッションがタイムアウトするなら、`~/.ssh/config` のリモートのマシンのエントリーの `ConnectTimeout` を 90 秒より長くし、ジャンプホストか `ProxyCommand` が利用者を待つ時間（ログインの確認や電話へのプッシュ）を足す、に改められました。表は、`ConnectTimeout` が未設定で、macOS か Linux の Claude Desktop v4.4212.0 以降でジャンプホストか `ProxyCommand` 経由でセッションを始めるときは 30 秒の後に 90 秒の 2 回目があり（1 回目に Desktop が確認を示したら 2 回目はない。Desktop が `ProxyJump` のホストのために示すログインの確認の時間は数えないが、経路のほかの待ちは数える）、Windows の Desktop・前の版・`MaxSessions 1` を設定したリモートのマシン・Desktop が自分で始める再接続では 30 秒、設定していればどの接続と再接続も設定した値（経路のどの待ちも数える）、としています。設定がなければ 30 秒、という段落は表の前に、リモートのマシン自身が電話での承認を待つなら `ConnectTimeout` にかかわらず 45 秒以内に承認する、という段落は表の後に残っています — [日本語](https://code.claude.com/docs/ja/desktop#raise-the-ssh-connection-timeout) / [English](https://code.claude.com/docs/en/desktop#raise-the-ssh-connection-timeout)
- **Claude Desktop の内蔵の SSH クライアントの説明が改められた**（`desktop` の「Connect on Windows without the OpenSSH client」・「Limits while Desktop is disconnected」）。サードパーティのプロバイダーでは「既定で内蔵のクライアントでつなぎ、管理者が変えられる」という記述が、どちらのクライアントでつなぐかは Desktop の版と管理者の設定にも依る、に改められ、切断の間に編集が失敗する場合の内蔵のクライアントの例からも「サードパーティのプロバイダーの Windows では既定で」が外れました。SSH の設定のエントリーから Desktop が取る設定には `ConnectTimeout` が加わっています — [日本語](https://code.claude.com/docs/ja/desktop#connect-on-windows-without-the-openssh-client) / [English](https://code.claude.com/docs/en/desktop#connect-on-windows-without-the-openssh-client)
- **Claude Desktop の SSH のセッションで、組織の設定が読み込まれる前のメッセージを留める行が載った**（`desktop` の「Reconnect after sleep or a network loss」）。アコーディオンの題に「メッセージが送られない」が加わり、「Message not sent」の項目で、メッセージの下の `Your organization's settings haven't loaded, so your message to <host> wasn't sent. Retry to send it.` の行は、Desktop が再接続して、組織の設定がまだ読み込まれていないのでメッセージを留めたことを示し、**Retry** で今送り、何もしなければ設定が読み込まれたときにもう一度試す、と載りました。長い停止の項目も、接続したらメッセージを「届ける」から「届けようとする」に改められています — [日本語](https://code.claude.com/docs/ja/desktop#reconnect-after-sleep-or-a-network-loss) / [English](https://code.claude.com/docs/en/desktop#reconnect-after-sleep-or-a-network-loss)
- **Claude Desktop の Browser ペインの Cookie と使用量のリングの記述が改められた**（`desktop` の「Preview your app」・「Check usage」など）。「Preview your app」に、SSH のセッションでは Desktop を終了するとペインの Cookie を失い、**Keep cookies** では変えられない、と加わり、「Check usage」の使用量のリングは、どちらのレイアウトでも「モデルピッカーの隣」ではなく「プロンプトの欄の下の行」にある、と改められました（`errors` の「You've hit your session limit」も追従）。「Run a session in its own worktree」の **Worktree** は「ボタン」と呼ばなくなりました — [日本語](https://code.claude.com/docs/ja/desktop#preview-your-app) / [English](https://code.claude.com/docs/en/desktop#preview-your-app)
- **リフレッシュトークンのない MCP のログインが拒まれたときの挙動が載った**（`mcp` の「Authenticate with remote MCP servers」）。サインイン済みの OAuth のサーバーが保存したトークンを `401 Unauthorized` で拒むと、保存したログインにリフレッシュトークンがあればトークンを更新して再接続し、要求を 1 回再試行します（その再試行も失敗したときだけ `/mcp` で印が付く）。リフレッシュトークンがなければトークンなしで 1 回接続し、サーバーが応えればサインアウトした状態でツールが動いて拒まれたトークンは消され、その接続も拒まれれば `/mcp` に認証が要ると出ます。changelog の v2.1.314 の、サインインなしでも動く MCP サーバーが、保存したサインインが効かなくなった後に「needs authentication」と示される問題の修正（サインアウトしたまま使われる）に対応します — [日本語](https://code.claude.com/docs/ja/mcp#authenticate-with-remote-mcp-servers) / [English](https://code.claude.com/docs/en/mcp#authenticate-with-remote-mcp-servers)
- **ゲートウェイの後ろでツール検索を切る案内が外れた**（`mcp` の「Tool search through an LLM gateway」）。`ANTHROPIC_BASE_URL` がゲートウェイを指すとき、Claude Code はゲートウェイが `defer_loading` のツールのフィールドと `tool_reference` のブロックを `anthropic-beta` ヘッダーと共に転送することを期待し、ゲートウェイの後ろではツール検索が既定でオンなので MCP のツールは後から読み込まれる、と書き直されました。`ENABLE_TOOL_SEARCH=false` ですべてのツールを先に読み込む案内と、拒まれる要求を飛ばすために同じ変数を設定する文が外れ、v2.1.305 以降の再試行の条件からも「原因を認識しない」が外れています（`errors` の 5 か所と `llm-gateway-protocol` の「Retry without tool search」も同じ向きの変更。大幅更新 2 参照） — [日本語](https://code.claude.com/docs/ja/mcp#tool-search-through-a-gateway) / [English](https://code.claude.com/docs/en/mcp#tool-search-through-a-gateway)
- **Amazon Bedrock と Agent Platform の起動時のモデルの確認で、managed settings の固定は確かめないと載った**（`amazon-bedrock`・`google-vertex-ai` の「Startup model checks」）。古い版に固定していて新しい版を呼び出せるときの更新の提案について、managed settings の `env` のブロックの固定には確かめも提案もしない（Bedrock では、前から飛ばしていたアプリケーションの推論プロファイルの ARN を指す固定と並べて箇条書きになった）、managed の固定にまだ提案が出るなら v2.1.314 以降に更新する（それより前は、受け入れても managed の固定が効いたままで、次の起動で提案が戻った）と加わりました。特定のモデルでセッションを始める段落は h3「Start a session on a specific model」に、拒否を覚える段落は h3「Remembered model refusals」に分かれ、「最大 1 日覚え、その間の起動は問い合わせずに覚えたモデルを飛ばす」は「最大 1 日覚えることがある」に短くなりました（`google-vertex-ai` も同じ構成）。changelog の v2.1.314 の、managed settings がモデルを固定しているとき Bedrock と Vertex のモデルの更新の提案が起動のたびに戻る問題の修正に対応します — [日本語](https://code.claude.com/docs/ja/amazon-bedrock#startup-model-checks) / [English](https://code.claude.com/docs/en/amazon-bedrock#startup-model-checks)
- **分析の「承認されたコードの行」の定義と Console のダッシュボードの項目が改められた**（`analytics` の「Review summary metrics」・「Access analytics for API customers」）。**Lines of code accepted** は、承認された編集で Claude Code の Edit と Write のツールが加えたか削除した行の合計で、却下した提案は除き、後で削除した行は合計を減らさない、となりました（これまでは、利用者がセッションで承認した Claude Code が書いたコードの行の合計で、後の削除は追わない）。Console のダッシュボードでは **Activity** が **Active users** と **Sessions**（アクティブな利用者と Claude Code のセッションの日ごとの数）に、**Spend** は利用者の数を並べない日ごとの API のコストになりました。team insights の表はダッシュボードの上で選んだ期間（既定は過去 30 日）の列になり、**Members** はその期間に Claude Code の使用が報告された利用者と API キー（API キーはキーの名前で示す）、**Spend this month**・**Lines this month** の列は **Spend**・**Lines accepted** に改められ、実際のコストは請求のページではなく Console の Cost のページを見る、となっています — [日本語](https://code.claude.com/docs/ja/analytics#access-analytics-for-api-customers) / [English](https://code.claude.com/docs/en/analytics#access-analytics-for-api-customers)
- **Slack の Claude Code の画面の要素の名前と動きが改められた**（`slack` の「Session flow」・「Message actions」など）。App Home のタブのボタンは **Connect Claude account** に、Code + Chat モードで Chat に答えられたがコーディングのセッションが欲しかったときは、返事の **Switch to code repo...** を押してリポジトリを選ぶとそのメッセージで Claude Code のセッションが始まる（「Retry as Code」に代わる）、となりました。完了すると Claude はスレッドのメッセージを最終の応答と操作のボタンで更新し、それへのリンクをダイレクトメッセージで送り（これまでは要約と操作のボタン付きで @メンション）、**Create PR** はセッションのブランチの GitHub の compare のページを開いてそこでプルリクエストを作る（セッションの開始時に投稿した状況のメッセージに、セッションが終わると出る）、となっています。**Change Repo** のボタンはなくなり（「Wrong repository selected」の手順からも外れた）、Claude がどのリポジトリか分からないときは **Select repository** で一覧から選ぶよう尋ねられます — [日本語](https://code.claude.com/docs/ja/slack#message-actions) / [English](https://code.claude.com/docs/en/slack#message-actions)
- **環境変数の表の 6 つの行が改められた**（`env-vars` の「Variables」）。`FORCE_HYPERLINK` は、`0`・`false`・`no`・`off` で、フッターの PR かマージリクエストのバッジと長いサインインの URL も含めてすべてプレーンテキストになる（v2.1.314 より前は `false`・`no`・`off` がハイパーリンクをオンにした）、となり、表の前の「数値として読むので `0` だけがオフにする」という注記は外れました。`CLAUDE_CODE_DISABLE_CFC_PROMPT` には、VS Code では v2.1.314 以降の拡張機能がセッションのメッセージからも Claude in Chrome の指示を外す、と加わり、`CLAUDE_CODE_GLOB_TIMEOUT_SECONDS` は Glob と Grep のツールの検索のタイムアウトになりました。`CLAUDE_CODE_OAUTH_TOKEN`・`CLAUDE_CODE_OAUTH_REFRESH_TOKEN`・`CLAUDE_CODE_OAUTH_SCOPES` には、プロジェクトとローカルの設定では無視される、と加わっています（下の項目参照）。changelog の v2.1.314 の `FORCE_HYPERLINK=false` と `CLAUDE_CODE_DISABLE_CFC_PROMPT` の変更に対応します — [日本語](https://code.claude.com/docs/ja/env-vars#variables) / [English](https://code.claude.com/docs/en/env-vars#variables)
- **claude.ai のサインインの変数がプロジェクトとローカルの設定では無視されると載った**（`authentication`・`network-config`・`env-vars`・`settings-reference`）。`authentication` の「Authentication precedence」の `CLAUDE_CODE_OAUTH_TOKEN` の項目は、変数を設定したまま `/login` を実行すると今のセッションは新しいログインに替わり、新しいセッションでもそのログインを使うには、シェルのプロファイルと、ユーザーの設定のような変数を設定できる設定ファイルから変数を外す、と改められました（これまでは、シェルのプロファイルか設定ファイルの `env` のブロックから外すまで、新しいセッションのたびに変数を読み直す）。`network-config` の「mTLS authentication」では、アプリがプロバイダーの接続を管理する Claude Desktop のセッションで managed settings と `~/.claude/settings.json` からだけ読む変数から `CLAUDE_CODE_OAUTH_SCOPES` が除かれ、claude.ai でサインインしたローカル・SSH・WSL の Code タブのセッションでは `CLAUDE_CODE_OAUTH_SCOPES` を除いてどの設定ファイルでも設定できる（Desktop が Code タブと Cowork のセッションで自分で設定するので設定できない）、起動の環境が既に変数を設定していれば設定ファイルの値は無視されデバッグログに名前が出る、自分のプロキシか証明書の値をローカルのセッションで使うには保存したローカルの環境に加える、と段落が分けられました — [日本語](https://code.claude.com/docs/ja/authentication#authentication-precedence) / [English](https://code.claude.com/docs/en/authentication#authentication-precedence)
- **使用量の上限で自動で続ける回数の説明が改められた**（`interactive-mode` の「Wait for a usage limit to reset」）。続けたタスクでも権限の確認は出るので離れている間に止まりうる、という点は同じで、また上限に当たると待ちがまた始まります。自動の継続が 3 回あると止まって `Automatic continue stopped after repeated usage-limit hits` の通知が出て、`/rate-limit-options` で次を選びます。別のプロンプトを送るかそのメニューで待ちを選ぶと数え直し、いくつものリセットの区切りにまたがる `/goal` かセッションのスケジュールしたタスクも 3 回の継続で止まります（これまでは「続けて最大 2 回まで自分で待ちを設定し直し、その後止まる」）。changelog の v2.1.314 の、待ちの間にタスクが自分で再開したとき「Continue automatically at usage limit」がプロンプトなしに 3 回を超えて続く問題の修正に対応します — [日本語](https://code.claude.com/docs/ja/interactive-mode#wait-for-a-usage-limit-to-reset) / [English](https://code.claude.com/docs/en/interactive-mode#wait-for-a-usage-limit-to-reset)
- **ルールの `paths` のパターンの表が、ルールのベースディレクトリを基準に書き直された**（`memory` の「Path-specific rules」）。`**/*.ts` はベースディレクトリの下のどこでもの `.ts`、`src/**/*` はベースディレクトリの `src/` の下のすべて、`*.md` はベースディレクトリの下のどこでもの `.md`（これまでは「プロジェクトのルートの Markdown」）、`src/components/*.tsx` はベースディレクトリの `src/components/` の直下の `.tsx` だけ（サブフォルダーは含まない）となり、ベースディレクトリの直下の `.md` だけに合う `/*.md` の行が加わりました。表の前の「`paths` のないルールは無条件に読み込まれ、すべてのファイルに当たる」という文は外れています — [日本語](https://code.claude.com/docs/ja/memory#path-specific-rules) / [English](https://code.claude.com/docs/en/memory#path-specific-rules)
- **読み取りの区画の解除には動いている各セッションの再起動が要ると改められた**（`settings` の「When edits take effect」・`permission-modes`・`settings-reference`）。`settings` に、セッションの途中で `permissions.blockReadsOutsideWorkingDirectories` を外しても、動いているセッションではファイルのツールが区画を保つので、キーを設定しているすべての設定ファイルから外して動いている各セッションを再起動する、と加わりました。`permission-modes` の「The first read outside the working directories」の **No, and block reads outside the working directories from now on** の項目も、このセッションとその後のすべてのセッションで拒み、解除するにはキーをすべての設定ファイルから外して各セッションを再起動し、このセッションで 1 つのディレクトリだけなら `/add-dir` を使う、と改められています（これまでは、後で読ませるには `/add-dir` でディレクトリを加えるか設定を外す） — [日本語](https://code.claude.com/docs/ja/settings#when-edits-take-effect) / [English](https://code.claude.com/docs/en/settings#when-edits-take-effect)
- **`useAutoModeDuringPlan` で、起動時に外したファイルの `false` を数えないと載った**（`managed-settings` の「Keys read from every admin source」・`settings`）。どの管理の源の `false` でもオフになり、各キーは拒むことしかできない、という項目が子項目に分かれ、開発者のユーザーかローカルの設定の `false` もオフにする一方、`useAutoModeDuringPlan` では `--setting-sources` のようなオプションで開発者が外したユーザーかローカルのファイルの `false` は数えない（v2.1.314 以降）と加わりました。`settings` の「Exceptions to managed settings precedence」の表の行にも、起動時に外したファイルについてはキーの項目を見る、と加わっています（大幅更新 3 参照） — [日本語](https://code.claude.com/docs/ja/managed-settings#keys-read-from-every-admin-source) / [English](https://code.claude.com/docs/en/managed-settings#keys-read-from-every-admin-source)
- **コストの正式な確かめ方が「Manage costs for your organization」に揃えられた**（`costs`・`monitoring-usage`・`agent-sdk/cost-tracking`）。`costs` の「Using the `/usage` command」の段落が 2 つに分かれ、金額は見積もりなので正式な請求は Console の Usage のページではなく同じページの「Manage costs for your organization」を見る、となりました。その節の表で Claude Console の支出を見る場所は **Console usage page** から **Console Cost page** に、Claude Console の組織ごとの報告の説明も「承認された行」と言い換えられ、使用量クレジットが残っていて支出の上限に達したときに上限を上げるよう促すプランに Ultra が加わりました。`monitoring-usage` のコストのメトリクスの注記と `agent-sdk/cost-tracking` の正式な請求の案内も、この節へのリンクに替わっています — [日本語](https://code.claude.com/docs/ja/costs#manage-costs-for-your-organization) / [English](https://code.claude.com/docs/en/costs#manage-costs-for-your-organization)
- **サンドボックスのセキュリティの制限に macOS の Mach と XPC のサービスが加わった**（`sandboxing` の「Security limitations」）。サンドボックスの中のコマンドは `network.allowMachLookup` に列挙した各サービスへサンドボックスの外まで届き、サンドボックスはそれらのサービスがコマンドのためにすることを閉じ込めない、という項目です（`settings-reference` の `sandbox.network.allowMachLookup` にも同じ注記が加わった） — [日本語](https://code.claude.com/docs/ja/sandboxing#security-limitations) / [English](https://code.claude.com/docs/en/sandboxing#security-limitations)
- **WSL のセッションでの `allowedWorkspaceFolders` の `~` の意味が載った**（`admin-setup` の「WSL sessions in Claude Code Desktop」）。Claude Desktop の `allowedWorkspaceFolders` の一覧があるデバイスで WSL のセッションが始まるなら、`~` の項目はディストリビューションの中のホームディレクトリを意味します — [日本語](https://code.claude.com/docs/ja/admin-setup#wsl-sessions-in-claude-code-desktop) / [English](https://code.claude.com/docs/en/admin-setup#wsl-sessions-in-claude-code-desktop)
- **worktree で隔離したセッションからメインのチェックアウトのファイルを変える方法が加わった**（`worktrees` の「How Claude Code enforces isolation」）。メインのチェックアウトのパスへの Edit・Write・NotebookEdit を止める File edits の項目に、メインのチェックアウトのファイルを変えるには自分で編集するか、そこで対話的なセッションを始める、と加わりました。「Ask Claude to create a worktree」の `EnterWorktree` のリンク先も `tools-reference` の新しい h2 になっています — [日本語](https://code.claude.com/docs/ja/worktrees#how-claude-code-enforces-isolation) / [English](https://code.claude.com/docs/en/worktrees#how-claude-code-enforces-isolation)
- **Agent SDK の `/core` のエントリーが `prewarm()` もエクスポートすると改められた**（`agent-sdk/typescript` の「Import the `/core` entry when you bundle the Agent SDK」）。`/core` がエクスポートするものに `prewarm()` が加わり（アルファの `prewarm()` を `/core` から読み込むには Agent SDK v0.3.314 以降）、外すものの例から `prewarm()` が外れ、エクスポートするものと外すもの（`InMemorySessionStore` のクラスと、セッションを一覧・読み取り・フォーク・取り込み・要約するヘルパーなど）が 2 つの項目に分けられました — [日本語](https://code.claude.com/docs/ja/agent-sdk/typescript#import-the-core-entry-when-you-bundle-the-agent-sdk) / [English](https://code.claude.com/docs/en/agent-sdk/typescript#import-the-core-entry-when-you-bundle-the-agent-sdk)

**バグ修正**

- 一部の Claude Desktop のセッションで、プロジェクトとローカルの MCP サーバーが最初のターンの後に切れる問題を修正
- ベース URL に設定した LLM ゲートウェイが、サーバー側の安全性の確認に 403 か 422 で答えると、auto モードが毎ターン失敗する問題を修正（`apiKeyHelper` のある 403 は変わりません）
- 遅いトークンの更新が保存される前に `claude auth status` が終わり、次の実行でサインアウトしうる問題を修正
- アプリが前もって始めてからプロジェクトで開くセッション（デスクトップアプリの Code タブの新しいセッションなど）で、プロジェクトの `effortLevel` の設定が無視される問題を修正
- セッションの多いプロジェクトで、リンクしたセッションが最初のページより古いと、`claude --from-pr` が「No conversations found」と報告する問題を修正
- claude.ai とモバイルアプリで、同時に出た 2 つの権限の確認のうち 2 つ目にファイルのパスもコマンドも示されない問題を修正
- Remote Control と SDK のホストが、mod のツールの呼び出しに「don't ask again」を示す問題を修正
- クラウドと SDK のセッションで、タイトルの生成中に新しいメッセージか Stop が届くとセッションのタイトルが失われる問題を修正
- Claude が要求の項目を 1 つ省くと、自分のペースで動く `/loop` の起動がスケジュールされないことがある問題を修正
- クラウドのセッションの auto モードで、Artifact ツールがアップロード・データベースへの書き込み・outputs のフォルダー経由のファイルの保存をすると、承認待ちで止まる問題を修正
- claude.ai から同期したスキルをディスクに書けないとき、スキルが失われるか 10 分ごとにダウンロードし直される問題を修正
- `/schedule` が、クラウドのスケジュールしたタスクを作るか更新した後の結果に、次の実行の時刻とリンクを入れない問題を修正
- スクリーンリーダーのモードで、動いているサブエージェントの経過時間とトークン数が変わるたびに読み上げられる問題を修正
- 地域かネットワークによるブロック（HTTP 403）がサインインの失敗として示される問題を修正。エラーがブロックを説明します
- クラウドのセッションで、同期したプラグインが同じサーバーを含むと、動いている claude.ai のコネクターを Claude が認可が要るか失敗したと言う問題を修正
- ディスクかクォータが満杯でトランスクリプトか `~/.claude.json` の書き込みが失われたとき、`claude -p` が 0 で終わる問題を修正。エラーを出し、text と json の出力では 1 で終わります（満杯の NFS のエクスポートは見逃されることがあります）
- 起動から 1 秒ほどの間に設定ファイルに加えた編集が、設定ファイルがまた変わるまで効かない問題を修正
- 一部の実行が後始末を飛ばすマシン（`--setting-sources` を使う実行など）で、古いトランスクリプトが片付けられない問題を修正
- 削除したエージェントチームの受信箱が、teammate の遅れたメッセージで作り直される問題を修正
- 作り直したエージェントの teammate が、前のシャットダウンの承認でチームから外される問題を修正
- スケジュールしたタスクをオフにした後、保存されたスケジュールしたタスクを一覧も削除もできない問題を修正
- どれかを名指さずに削除を頼むと、Claude が最も最近更新した `/team-onboarding` のガイドを削除する問題を修正
- サーバーが削除を拒んだのに、Claude が `/team-onboarding` のガイドを削除したと言う問題を修正
- Claude apps gateway が Amazon Bedrock の「Input is too long.」のエラーを隠し、セッションが圧縮せずに「upstream rejected the request」で毎ターン失敗する問題を修正
- plan が承認を待つ間に再起動すると、セルフホストのランナーのセッションが最近のターンか会話全体を失う問題を修正
- 非常に大きな CLAUDE.md が前に送ってから変わったセッションで、自動の圧縮の後に「Prompt is too long」になる問題を修正
- コマンドを登録するプラグインの多いヘッドレスのセッションで、メモリーの使用が多く起動が遅い問題を修正
- env の設定で `AWS_BEARER_TOKEN_BEDROCK` を空にすると、stdio の MCP サーバーが空の値を受け取る問題を修正。変数は外され、サーバーはマシン自身の AWS の資格情報を使えます
- 一部の TLS を検査するプロキシの後ろで、ルート証明書の更新の後に API の要求が「unable to get local issuer certificate」で失敗する問題を修正
- 圧縮が自分の要求を縮めなければならなかったとき、非常に長い会話が前の要約を失う問題を修正
- PDF 自身のメタデータによって、Read と @ メンションがページ数を少なく数えうる問題を修正
- `DISABLE_PROMPT_CACHING_OPUS` と `DISABLE_PROMPT_CACHING_SONNET` が、既定のモデルの `[1m]`・別の地域・日付のない書き方に効かない問題を修正
- 自分の成果物が 200 以上あると、`/artifacts` と Artifact ツールの共有の一覧に共有された成果物が出ない問題を修正
- 検索が時間の上限に当たったとき、Claude が Grep と Glob の途中の結果を完全なものとして扱う問題を修正
- プロキシ経由の `https://` のエンドポイントへの OpenTelemetry のエクスポートが、別のエクスポートの途中に始まると送られない問題を修正
- `http://` のエンドポイントへの OpenTelemetry のエクスポートを止める（HTTP 403）プロキシへ、接続の試みが殺到する問題を修正
- 応えないプロキシの後ろで OpenTelemetry のエクスポートが止まったままになる問題を修正。10 秒で（`OTEL_EXPORTER_OTLP_TIMEOUT` で最大 30 秒）タイムアウトします
- 再開したセッションが、Claude が既に知っていたファイルの変更をまた伝える問題を修正
- ツールがオフにされていたため前の呼び出しが失敗した後、再開したセッションで Claude が組み込みのツールを使わないことがある問題を修正
- `disableRemoteControl` の設定で Remote Control がオフなのに、`/remote-control` がそう言わずに「Unknown command」と答える問題を修正
- リードのセッションが手動のモードなのに、tmux か iTerm2 のペインのエージェントチームの teammate が auto モードで始まる問題を修正
- バックグラウンドのセッションが更新されるか退役するとき、直前の権限モードの変更を失うことがある問題を修正
- プロンプトに打った文を消すために押した Ctrl+C が、動いているすべてのバックグラウンドのエージェントを止める問題を修正
- 報告を送っている間に /feedback が「Enter to confirm」を示す問題を修正
- 止めたシェルのコマンドの子プロセスに SIGTERM が 2 回送られることがあり、一部のプログラムが後始末を飛ばしうる問題を修正
- クラウドかセルフホストのランナーのセッションの中で動かした `claude -p` が、そのセッションの ID を共有する問題を修正。セッションのトランスクリプトに書き込み、再起動で違う会話を再開しえました
- クラウドかセルフホストのランナーのセッションの中で動かした `claude -p` が、自分のタイトルを作ってそのセッションに送る問題を修正
- Windows: ネイティブのパスの照会が失敗する一部のボリュームで、すべてのツールの呼び出しが拒まれる問題を修正。作業ディレクトリの確認が、フォルダーの同一性を比べるようになりました
- Windows: Claude Desktop が始めていないセッションで、セッションの scratchpad などの一時パスがプロジェクトのパスの長さとともに伸び、そこへクローンしたリポジトリが 260 文字のパスの上限に当たる問題を修正
- Gateway: グループの共有の予算が尽きた後、ステータスラインと `/usage` が開発者自身の支出の上限を 100% 使用と示す問題を修正
- Self-hosted runner: セッションが新しいランナーへ移り、ターンが `CLAUDE_CODE_RESUME_INTERRUPTED_TURN_MAX_AGE_MS` より古いとき、Claude が中断したツールの呼び出しを見ない問題を修正
- Self-hosted runner: セッションのサービスが切り替えの保存を拒んでいたとき、オフにした MCP サーバーが、セッションの新しいマシンへの移動の後にオンに戻る問題を修正
- [VSCode] フォークした会話がメッセージを落とす問題を修正。Claude が並行して動かしたツールの呼び出しが 1 つしか残らず、圧縮が残した最後のメッセージが失われ、Claude の答えが答えた質問なしに残りえました
- [VSCode] Claude が時間内に起動を終えないとメッセージが失われる問題を修正。拡張機能は、エラーを示す前に Claude をもう一度起動します
- [VSCode] 要求が地域かネットワークでブロックされたとき、サインインの画面が開く問題を修正
- [VSCode] Account のパネルが、プラン名の 2 語目を小文字で示す問題を修正
- [VSCode] Claude のタブのファイルのリンクが、別のエディターグループではなくチャットの上に開く問題を修正
- [VSCode] `chat.fontSize` を上げても、Claude のパネルの添付のチップ・メニュー・バナー・ダイアログが小さいままの問題を修正
- [VSCode] テレメトリーがオフのとき、`ultrathink` がそのターンの effort を上げず、虹色も示さない問題を修正
- [Cloud sessions] すでにシークレットのあるホストにネットワークのシークレットを加えると、黙って置き換わる問題を修正。Add secret のフォームは拒み、既存のシークレットを案内します
- [Cloud sessions] 新しいスケジュールしたタスクが組織の既定の環境を無視する問題を修正。フォームは Anthropic がホストする既定ではなく、管理者が選んだ環境から始まります
- [Remote Control] `claude remote-control` を再起動した後、前のメッセージから 1 分以内にアイドルのセッションへ送った次のメッセージに答えがない問題を修正

**その他**

- **「バックグラウンドの機能」のリンク先の一部が `model-config` に移った**（`hooks`・`errors`・`llm-gateway-rollout`・`model-config`）。`hooks` の prompt と agent のフックの `model` の既定（2 つの表と「How prompt-based hooks work」）、`errors` の「Unrecognized model ID on a request」、`llm-gateway-rollout` の「What to distribute」の表の「バックグラウンドの機能」のリンクが、`costs` の「Background token usage」から `model-config` の「Environment variables」に替わり、`model-config` の `ANTHROPIC_DEFAULT_HAIKU_MODEL` の行ではリンクが外れました。`llm-gateway-rollout` の同じ行からは、各部分がどのモデルを使うかは `model-config` にある、という文も外れています。`env-vars` の `ANTHROPIC_DEFAULT_HAIKU_MODEL` の行と `llm-gateway-protocol` の表は今も `costs` の節を指しており、その節（h2「Background token usage」）も残っています
- **字句と例の小さな修正**: `remote-control` の「session URL」が「URL」（Claude Code が示す URL）に言い換えられ、`plugins/mods/api`・`plugins/mods/interface` のタイマーが止まるのはモジュールの再読み込み「のとき」から「の後」に、`routines` の環境の選択に「環境がすでに選ばれていれば、そのままにするか別のものを選べる」が加わり、`cli-reference` の `--input-format` の例が `claude -p --input-format stream-json --output-format stream-json --verbose` に改められました
- **版の注記などの削除**: `commands` から、`/verify` の「v2.1.215 より前は Claude が自分で動かすこともあった」と、`/permissions` の「Claude の応答中に実行するとすぐにダイアログを開き、同じターンの次のツールの呼び出しから変更を適用する（v2.1.234 より前はターンの終わりまで待った）」が、`cli-reference` の `--max-turns` から「上限に達するとエラーで終わる」が外れました（挙動の変更かどうかは原文からは分かりません）
<!-- light:minor-updates:end -->

見出しマップ（`en/claude_code_docs_map.md`）は 25 行が加わり 1 行が外れました。加わったのは 24 の見出し（ハイライト・大幅更新・軽微な更新で触れた新しい見出し）と新しいスタンプ、外れたのは古いスタンプで、`llms-full.txt` の見出しの増減（加わった 24・外れた 0）と同じです。今回、見出しマップにだけ先に載った見出しはありません。

**参考リンクについて**: 日本語版は、今回取り上げたページのうち 33 ページを取得し、該当する節があるかと今回の内容になっているかを、計 67 項目について確かめました。67 項目とも日本語版がすでに今回の内容になっていたので、リンクはすべて日本語版を併記しています。アンカーは、見出しから作った id か、ページ内・ページ間のリンクが使っている id です。見出しと id が違う 3 つ（`server-managed-settings` の「When a machine's `apiKeyHelper` isn't in effect」の `#machine-apikeyhelper-not-in-effect`、`mcp` の「Tool search through an LLM gateway」の `#tool-search-through-a-gateway`、`permission-modes` の「The first read outside the working directories」の `#first-read-outside-the-working-directories`）は、ほかのページからのリンクが使っている id で、`errors` の「Claude Code didn't send your claude.ai login」は、表のリンクが使っている `#claude-code-didnt-send-your-claude-ai-login` です。`fast-mode` の警告は最初の見出しより前にあるので、ページの URL にアンカーを付けていません。リンクを付けなかった「その他」の項目は、複数のページにまたがる字句やリンク先の変更です。**changelog ページへのリンクは、本サマリの方針どおり付けていません。**

## 新着情報

<!-- light:whats-new:start -->
**今回、新着情報（`whats-new/`）のページに変更はありません**（最新の週のダイジェストは前回と同じ Week 37 です）。
<!-- light:whats-new:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-11-01.md](./archives/latest/2026-11-01.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-11-01.md](./archives/latest-detail/2026-11-01.md)

<!--
base_commit: 3516469056879756b0d664613b6c6840754794fb
head_commit: acb459e04e57acda73f439e58d2759ea5599cdf6
generated_at_full: 2026-11-03T15:19:51+09:00
-->
