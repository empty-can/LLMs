---
対象期間: 2026年10月13日 〜 2026年10月14日
作成日: 2026-10-14
---

# Claude Code 公式ドキュメント更新サマリ

```markdown
**今回は、デスクトップアプリの SSH のセッションのリモートマシン側の設定と調べ方（プロキシと CA 証明書、`ProxyCommand`、ポートの転送、リモートマシン上のファイルとプロセス、ログイン前に閉じる接続、接続失敗の表とログ）、ネットワークシークレットの Team・Enterprise プランへの拡大、サブエージェントごとの自動圧縮のウィンドウ `autoCompactWindow`、スキルとコマンドの名前に使えない文字、アーティファクトの小さな変更を公開と一度に済ませる動作が文書に加わりました。changelog には v2.1.300（2026年10月14日、88 項目）が積まれています**。新しいページはなく、ページ単位で数えると 222 ページ中 43 ページ（changelog を含む）が変わり、changelog を除く変更は 745 行（追加 628・削除 117）、2 ページが大幅更新です。総行数は 121,690 行から 122,303 行に増えました。

主要なものを以下に挙げます。

1. デスクトップアプリの SSH のセッションに、リモートマシンのプロキシと CA 証明書、コンテナや AWS への `ProxyCommand`、ポートの転送、リモートマシン上のファイルとプロセス、ログイン前に閉じる接続（fail2ban）、ログイン後の接続失敗のコード表とログの取り方が載った
2. クラウド環境のネットワークシークレットが Pro・Max に加えて Team・Enterprise のプランでも使えるようになり、組織管理者のロールの有無で変わる追加の仕方と、ロールのない Team 向けの短いフォームが載った
3. サブエージェントの frontmatter の `autoCompactWindow`（100,000〜1,000,000 トークン）で、そのサブエージェントだけ早く自動圧縮できることが載った（v2.1.296 以降）
4. ゼロ幅スペース・向きを変える文字・空白に見える文字・`<`・`>` を含むスキルとコマンドの名前は拒否され、`claude --debug` のログの `[names]` で見つけられることが載った（v2.1.299 の変更の文書化）
5. アーティファクトのファイルへの小さな変更を公開と一度に済ませる動作と、それを止める `CLAUDE_CODE_ARTIFACT_PUBLISH_EDITS`（v2.1.300 以降）が載った
```

## ハイライト

1. [**デスクトップアプリの SSH のセッションにリモートマシン側の設定と調べ方の節が加わった**](./latest-detail.md#1-デスクトップアプリの-ssh-のセッションにリモートマシン側の設定と調べ方の節が加わった):  
  `desktop` の「SSH sessions」に、プロキシと CA 証明書、`~/.ssh/config` でのコンテナ・シェルの変数・AWS の認証情報・`Match host` の扱い、Desktop が切る転送の設定、ポートの転送、リモートマシン上のファイルとプロセス、ログイン前に閉じる接続と fail2ban、リモートマシンの MCP サーバーの節ができ、トラブルシューティングに接続失敗のコード表とログの取り方が加わりました
2. [**ネットワークシークレットが Team と Enterprise のプランでも使えるようになった**](./latest-detail.md#2-ネットワークシークレットが-team-と-enterprise-のプランでも使えるようになった):  
  `cloud-environments` で、これまで Pro と Max だけだったネットワークシークレットが Team と Enterprise でも使えるようになりました。組織管理者のロールの有無で、自分の環境と共有の環境で追加できるかが変わり、ロールのない Team の利用者には 1 つのホストだけを取る短いフォームが開きます
3. [**サブエージェントごとに自動圧縮のウィンドウを下げる autoCompactWindow が載った**](./latest-detail.md#3-サブエージェントごとに自動圧縮のウィンドウを下げる-autocompactwindow-が載った):  
  `sub-agents` の frontmatter の表に `autoCompactWindow` が加わり、「Set the auto-compact window for one subagent」の節ができました。100,000〜1,000,000 のトークン数で、そのサブエージェントだけ早く圧縮させます（v2.1.296 以降）。エージェントチーム・プラグインのエージェント・Agent SDK（TypeScript）の説明も追従しました
4. [**スキルとコマンドの名前に使えない文字と拒否されたときの調べ方が載った**](./latest-detail.md#4-スキルとコマンドの名前に使えない文字と拒否されたときの調べ方が載った):  
  `skills` に「Characters a skill name can't hold」の節が、`errors` に「Skill or command name refused」の節ができました。隠れた文字・向きを変える文字・空白に見える文字・`<`・`>` を含む名前は拒否され、フォルダーやファイルの名前なら読み込まれず、frontmatter の `name` なら無視されます
5. [**アーティファクトの小さな変更を公開と一度に済ませる動作が載った**](./latest-detail.md#5-アーティファクトの小さな変更を公開と一度に済ませる動作が載った):  
  `artifacts` で、公開の確認に `Also makes 1 edit to that file on disk.` のような文があれば、Claude はファイルの変更と公開を 1 つの手順で行う、と載りました。Manual・`acceptEdits` モードでそうした変更が承認を要るときの行も加わり、`env-vars` には止めるための `CLAUDE_CODE_ARTIFACT_PUBLISH_EDITS`（v2.1.300 以降）が載りました

## 新規追加されたページ

（今回の対象期間に新規追加・削除されたドキュメントページはありません。`llms.txt` は変わらず、`llms-full.txt` に展開されている固有のページも 222 のままで、`Source:` の行が 230 あり 8 ページが 2 回展開されている状態も前回と同じです）

## 大幅に更新されたページ

- [**Desktop application**](./latest-detail.md#1-desktop-application) ([日本語](https://code.claude.com/docs/ja/desktop#set-a-proxy-or-a-ca-certificate-for-ssh-sessions) / [English](https://code.claude.com/docs/en/desktop#set-a-proxy-or-a-ca-certificate-for-ssh-sessions)):  
  348 行（追加 338・削除 10）が変わりました。SSH のセッションのリモートマシン側の節が大きく加わったほか、Auto と Bypass permissions でのアーカイブの承認、プレビューのサーバーの `autoPort` の既定が改められました（詳細はハイライト 1）
- [**Configure cloud environments**](./latest-detail.md#2-configure-cloud-environments) ([日本語](https://code.claude.com/docs/ja/cloud-environments#add-network-secrets) / [English](https://code.claude.com/docs/en/cloud-environments#add-network-secrets)):  
  60 行（追加 33・削除 27）が変わりました。ネットワークシークレットが Team と Enterprise に広がり、環境のセレクターとダイアログの説明が今の画面に合わせて書き直されました（詳細はハイライト 2）

## 軽微な更新

今回の差分は **2 ファイル**（`llms-full.txt`・見出しマップ）で、`llms.txt` は変わっていません。`llms-full.txt` の差分は追加 730 行・削除 117 行で、ページ単位に切り出して数えると 222 ページ中 **43 ページ**が変わり、合計は生の差分と一致しました（2 回展開されているページに変更はありませんでした）。うち changelog が 102 行（追加のみ）、ほかのページが 745 行（追加 628・削除 117）です。大幅更新の 2 ページを除く **41 ページ**（changelog を含む）と、changelog に加わった **v2.1.300**（2026年10月14日、88 項目。Added 12・Changed 13・Improved 4・Fixed 59）を以下にまとめます。changelog の項目はすべて v2.1.300 のもので、前回の v2.1.299 との間の版の項はありません。`llms-full.txt` の総行数は **121,690 行から 122,303 行へ 613 行増え**ました。`Source:` の行は 230、固有のページは 222 のままです。

**新機能**

- mod のプロンプトの装飾に `virtualText` を追加。プロンプトボックスに描くが、下書きにも送信するプロンプトにも入らない文字です
- OpenTelemetry の `api_request` のイベントに `cache_creation_5m_tokens` と `cache_creation_1h_tokens` を追加。キャッシュの書き込みを寿命ごとに分けます
- mod 向けに `$.ui.view({ agentId })` を追加。求められたときにエージェントのトランスクリプトをメインのビューに出し、`$.ui.view({})` で戻ります
- mod の `Text` に右から左に書く文字のための `dir` を追加。Windows と VS Code の端末では行がその向きに読まれ、右に寄ります
- Claude Platform on AWS に `/advisor` を追加。`/advisor`・`advisorModel`・`--advisor` で選ぶまでアドバイザーは動かず、`CLAUDE_CODE_DISABLE_ADVISOR_TOOL=1` でオフにできます
- トレースのスパンに、`gen_ai.provider.name`・`gen_ai.conversation.id`・`gen_ai.tool.name`・`error.type` のような OpenTelemetry の GenAI のセマンティック規約の属性を追加
- mod の `agent.spawn` フックで、ワークフローのエージェントの `prompt` と `model` を書き換えられるようにした（これまでは断ることしかできなかった）
- mod の `prompt.change` フックを追加。打った編集以外でプロンプトボックスの文字が変わったとき（履歴の呼び出し、クリア、元に戻す、プラグインによる入力）に発生します
- [VSCode] エディターで選んだ文字をメッセージに加えないための `claudeCode.attachSelection` の設定を追加
- [Claude Tag] Slack Connect のチャンネルに対応。Owner か Claude Tag の管理者が、別の組織と共有するチャンネルで Slack の Claude に答えさせられます（既定はオフ）
- [Claude Tag] 承認が要るコネクタの操作について、Slack のスレッドに本人だけに見える Allow once / Deny のカードを追加。Claude は断る代わりに尋ね、ほかの人には本人を待っていることだけが見えます
- [Claude Tag] Slack の音声クリップに対応。Slack にクリップの文字起こしがあれば Claude はそれを読みます
- **`skill.prompt` のフックでスキルの出どころと frontmatter を読めるフィールドが載った**（`plugins/mods/reference` の「Source and frontmatter fields on `skill.prompt`」）。`e.source`（`policySettings`・`userSettings`・`projectSettings`、ほかに `plugin`・`mcp`・`syncedSkills`・`built-in` など）、`e.pluginName`、`e.path`（`SKILL.md` かコマンドファイルの絶対パス）、`e.frontmatter`、`e.frontmatterProblem` で、フックは変えた `text` か `frontmatter` を `next` に渡せます（ほかのフィールドを変えるとフックは失敗）。v2.1.299 以降が要り、v2.1.299 の changelog に載っていた追加の文書側です（`plugins/mods/events` にもこの節への案内が加わった）。`next.error.cause` も独立した行になり、`tool.call` か `PreToolUse` のフック、または `agent.spawn` のフックが元の呼び出しを変えたときの `rewritten`（v2.1.300 以降）が加わりました — [日本語](https://code.claude.com/docs/ja/plugins/mods/reference#skill-prompt-fields) / [English](https://code.claude.com/docs/en/plugins/mods/reference#skill-prompt-fields)
- **セルフホストのラッパー向けに `CLAUDE_CODE_REMOTE_MCP_CONFIG` が載った**（`self-hosted-environments-configuration` の「Wrapper scripts」）。コントロールプレーンが届けた MCP サーバーの定義を持つ、`CLAUDE_CONFIG_DIR` 内のファイルのパスです。子の環境を作り直すラッパーがこれを引き継がないと、届けられるサーバーが更新されたとき、`--mcp-config` で足した stdio・HTTP・SSE のサーバーのうち更新に含まれないものを子が止めます（v2.1.299 以降）。MCP サーバーの読み込み元の一覧にも、ラッパーで `"$@"` の後に `--mcp-config` を足す項目が加わりました（v2.1.299 より前は最初の更新で止まった）— [日本語](https://code.claude.com/docs/ja/self-hosted-environments-configuration#wrapper-scripts) / [English](https://code.claude.com/docs/en/self-hosted-environments-configuration#wrapper-scripts)

**機能改善**

- Cowork のクラウドのセッションの WebFetch を改善。少し前に失敗したページは取得し直さず、そう Claude に伝えます
- 組み込みの `plugin-authoring` スキルの mod の共有を改善。Claude は mod のファイルを開く前にキーが含まれていないか調べ、プロジェクトの外のフォルダーを調べる前に尋ねます
- Claude 3 のモデルが @ メンションした PDF について受け取る注記を改善。読まずに答えることが減ります
- アーティファクトの更新を改善。Claude は小さな変更を加えて 1 回の呼び出しで公開し直し、大きな編集と再公開も 1 つの返答の中で済ませます（詳細はハイライト 5 参照）
- **API のエラーで終わった `claude plugin eval` の実行の扱いが節になった**（`plugin-evals` の「"ended on an API error and scored 0 without grading"」）。最後の要求に API がレート制限やプランの使用上限などの HTTP エラーで答えた実行は、グレーダーの結果なしで 0 点になり、スコアと `--threshold` によらずコマンドは 0 以外で終わります。エラーは進捗の行の `error:` の後か、JSON の `cases[].arms.with[].error`・`cases[].arms.without[].error` にあります。ベースラインの実行も数えるので、すべてのケースが通ってもコマンドが失敗することがあり、2 つの arm の実行では `W/OUT` と `Δ` が `—` になります。v2.1.299 より前は生成したものを採点していました（v2.1.299 の修正の文書側）。終了コードの表（`plugins/cli-reference` も）と、「The run exits 1 but the results look fine」（stderr の行が原因を示す）も改められています — [日本語](https://code.claude.com/docs/ja/plugin-evals#runs-ended-on-an-api-error) / [English](https://code.claude.com/docs/en/plugin-evals#runs-ended-on-an-api-error)
- **システムプロンプトを置き換えると git status のスナップショットなしで始まると明記された**（`settings-reference` の「`includeGitInstructions`」）。`-p` で `--system-prompt`・`--system-prompt-file` を渡すか、自分のプロンプトを持つカスタムのエージェントを `--agent` か `agent` の設定で使う場合と、Agent SDK でカスタムのシステムプロンプトかカスタムのメインスレッドのエージェントを使う場合は、このキーが `true` でもスナップショットが付きません（SDK でシステムプロンプトを設定しないと、最小の既定でもスナップショットなし）。残すには、ベアモードの外で、カスタムのエージェントなしに `--append-system-prompt` で指示を足すか、SDK では `claude_code` のプリセットを使います。`headless`・`sub-agents`・`agent-sdk/modifying-system-prompts`・`context-window`（圧縮の後に読み直すのは、始まりにスナップショットがあった場合だけ）も同じく改められました — [日本語](https://code.claude.com/docs/ja/settings-reference#includegitinstructions) / [English](https://code.claude.com/docs/en/settings-reference#includegitinstructions)
- **`CLAUDE_CODE_DISABLE_FILE_MENTIONS` への案内が各ページに加わった**（前回の v2.1.299 で加わった変数）。`common-workflows` の「Reference files and directories」（`@` 参照がファイルの内容とディレクトリの一覧を含めないようにする）、`hooks` の PreToolUse の警告（特定のパスは `Read` の deny ルールで止め、挿入そのものはこの変数でオフにする。オフにすると Claude はファイルのツールで読むので、一致する PreToolUse のフックが動く）、`agent-sdk/modifying-system-prompts`（`CLAUDE_CODE_DISABLE_ATTACHMENTS` の代わりに `@` のメンションだけを止める）です — [日本語](https://code.claude.com/docs/ja/common-workflows#reference-files-and-directories) / [English](https://code.claude.com/docs/en/common-workflows#reference-files-and-directories)
- **予定したタスクの次の実行時刻の確かめ方が載った**（`scheduled-tasks` の「Jitter」）。端末の `CronCreate` の呼び出しの下の行（例: `next run 10:21 AM`）か、`CronList` の呼び出しの下の行の `next run` で見られます（v2.1.299 以降。v2.1.299 の、スケジュールのツールが各ジョブの実際の次の実行時刻を報告する修正の文書側）。`CronList` の説明にも次の実行時刻が加わり、動的なループの保留中の wakeup は 1 回限りのタスクとして一覧に出るので、`:00` か `:30` に予定されたものは少し早く動きうる、と改められました — [日本語](https://code.claude.com/docs/ja/scheduled-tasks#jitter) / [English](https://code.claude.com/docs/en/scheduled-tasks#jitter)
- **VS Code で再開した会話が最初は空白になる理由が載った**（`vs-code` の「A resumed conversation is blank at first」）。過去の会話を再開したときや再読み込みの後に戻ったとき、その会話の Claude Code のプロセスが始まる間はメッセージが空白のことがあり、約 1 秒後に `Waiting for your plugins…` が出ます。何もしなくてよく、プロセスが始まってプラグインの確認が要らないと分かるか、20 秒たつとメッセージが出ます — [日本語](https://code.claude.com/docs/ja/vs-code#a-resumed-conversation-is-blank-at-first) / [English](https://code.claude.com/docs/en/vs-code#a-resumed-conversation-is-blank-at-first)
- **スペースを含むパスを引用符で囲まないフックの通知が載った**（`errors` の「Hook needs quotes around a path with a space」）。シェル形式の `asyncRewake` のフックで、`python3` などのインタープリターの後のパスのプレースホルダーが引用符なしで、解決したパスにスペースを含むと、スクリプトは動かず `Stop hook needs quotes around a path with a space (check.py)` のような通知が出ます。JSON では `"command": "python3 \"${CLAUDE_PLUGIN_ROOT}/hooks/check.py\""` のように囲みます — [日本語](https://code.claude.com/docs/ja/errors#hook-needs-quotes-around-a-path-with-a-space) / [English](https://code.claude.com/docs/en/errors#hook-needs-quotes-around-a-path-with-a-space)
- **オンデマンドのランナーをアイドルで終わらせる方法が載った**（`self-hosted-environments-configuration` の「Make on-demand runners exit when idle」）。フックが始めるランナーは既定ではセッションのターンが終わっても終わらないので、すべてのランナーに `--release-idle-session-min`（アイドルの分数の後にセッションを放して 0 で終わる）と `--kill-session-after-min`（アイドルに数えないセッションの上限）を、待機用のランナーに `--exit-if-unused-min` を渡し、ランナーが終わったらワークロードを消します（Kubernetes の Job の `ttlSecondsAfterFinished` など）。spawn-runner のフックが `--hook-timeout` の終わりにまだ動いていれば、再試行できる失敗として扱う、とも明記されました — [日本語](https://code.claude.com/docs/ja/self-hosted-environments-configuration#make-on-demand-runners-exit-when-idle) / [English](https://code.claude.com/docs/en/self-hosted-environments-configuration#make-on-demand-runners-exit-when-idle)
- **ラッパーとフックで引数と変数を引用符で囲むよう求める節になった**（`self-hosted-environments-configuration` の「Quote the arguments and variables your script expands」）。JSON・文・`Bash(npm run test *)` のような権限ルールを含む値があるので、引数は `"$@"` で渡し、変数はそれぞれ引用符で囲み、`eval` と `sh -c` の文字列に値を埋め込まない、としています（これまでは Slack のスレッドのリンクについてだけの注意）。`checkout` のフックが結果をプッシュするリポジトリで失敗するときは、理由を短い 1 行で最後に stderr に書いてから 0 以外で終わる（秘密を出さず、配備の前に `set -x` を外す）、とも加わりました — [日本語](https://code.claude.com/docs/ja/self-hosted-environments-configuration#quote-the-arguments-and-variables-your-script-expands) / [English](https://code.claude.com/docs/en/self-hosted-environments-configuration#quote-the-arguments-and-variables-your-script-expands)
- **セルフホストのランナーの TLS 証明書のエラーの対処が載った**（`self-hosted-environments-deploy` の「Troubleshooting」）。ランナーが起動時に `RegisterRunner failed:` と `self signed certificate in certificate chain` のような TLS のエラーで終わるときと、オーケストレーターが `poll failed:` を記録して再試行し続けるときは、TLS を検査するプロキシのルート CA を含む PEM を `NODE_EXTRA_CA_CERTS` に設定します（git には `GIT_SSL_CAINFO` も要る。オーケストレーターの `/healthz` の `connected` が `true` になれば直った）。ほかに、SSH の鍵しかないランナーのホストで `--git-ssh-rewrite github.com` を使い github.com を SSH でクローンする例、git プロキシではユーザーのセッションを作る各人が自分の GitHub をつなぐこと、ホストのプッシュの資格情報をグローバルの git の設定に置かないことが加わりました — [日本語](https://code.claude.com/docs/ja/self-hosted-environments-deploy#troubleshooting) / [English](https://code.claude.com/docs/en/self-hosted-environments-deploy#troubleshooting)
- **セルフホストのクイックスタートの注意が増えた**（`self-hosted-environments-quickstart`）。ベースディレクトリはホームや自分のクローンのディレクトリではなくランナー専用のものにする（`<writable-dir>/<repo-owner>/<repo>` を自分のクローンとして扱い、リセット・上書き・削除しうる）警告、このコマンドで始めたランナーはターンごとではなく 1 つのセッションを処理した後に終わる仕様であること、SSH の鍵だけでは足りない（`https://` の URL でクローンする）こと、Owner が GitHub のコネクタをオンにし各開発者が自分の GitHub をつなぐ前提が加わり、「If the runner exits」はセッションをアーカイブ・削除した場合と開始に失敗した場合に分けて書き直されました — [日本語](https://code.claude.com/docs/ja/self-hosted-environments-quickstart#if-the-runner-exits) / [English](https://code.claude.com/docs/en/self-hosted-environments-quickstart#if-the-runner-exits)
- **セルフホストのリファレンスの補足**（`self-hosted-environments-reference`）。`--startup-timeout-min` の N 分は、子が初期化するか状態を報告する前に出す `user`・`assistant` のメッセージのたびに数え直す（v2.1.299 より前は最初のそうしたメッセージで効かなくなった）、オーケストレーターの `/healthz` の `connected` が `false` の理由はトップレベルの `last_error`（ポーリングが成功するたびに `null`）で見る、と加わりました — [日本語](https://code.claude.com/docs/ja/self-hosted-environments-reference#runner-cli-flags) / [English](https://code.claude.com/docs/en/self-hosted-environments-reference#runner-cli-flags)
- **`-p` と Agent SDK でワークフローを始めさせる方法の書き方が改められた**（`workflows` の「Approve the plan before it runs」）。各項目が「何をすればよいか」の形になり、フックは呼び出しに `"allow"` を返すが、プランモードではフックの承認だけではワークフローが始まらないので、権限ルールかホストの承認を使う、と加わりました — [日本語](https://code.claude.com/docs/ja/workflows#approve-the-plan-before-it-runs) / [English](https://code.claude.com/docs/en/workflows#approve-the-plan-before-it-runs)
- **GHES のクラウドのセッションで認証に失敗したときの対処が載った**（`github-enterprise-server` の「Cloud session fails to clone repository」）。「Authentication failed while accessing the repository」で止まるなら自分の GitHub Enterprise のアカウントをつないでいない可能性があるので、claude.ai/code のリポジトリのピッカーからつないで新しいセッションを始めます。Owner がつないだ後は開発者側の設定が要らない、という文は外れました — [日本語](https://code.claude.com/docs/ja/github-enterprise-server#cloud-session-fails-to-clone-repository) / [English](https://code.claude.com/docs/en/github-enterprise-server#cloud-session-fails-to-clone-repository)
- **ストリームのバイト単位のウォッチドッグの時間が整理された**（`network-config`）。直接の Anthropic API では 180 秒、Claude Platform on AWS・Amazon Bedrock・Claude apps gateway のセッション・カスタムの `ANTHROPIC_BASE_URL` では 300 秒になりました（カスタムの `ANTHROPIC_BASE_URL` は、機能フラグを取得したかで 180 秒か 300 秒としていた。前回まとめた v2.1.299 の修正の文書側）
- **Agent SDK（TypeScript）の peer のメッセージの `body` が、まとめられたときは付かないと明記された**（`agent-sdk/typescript`）。チームメイトの 1 つのメッセージには付き、複数がまとめられると付きません。v2.1.299 より前は、まとめたメッセージが最初のメッセージの `body` を持っていました
- **`autoCompactWindow` がほかのページにも載った**（`agent-teams`・`plugins/components`・`claude-directory`・`agent-sdk/typescript`・`agent-sdk/subagents`・`model-config`。詳細はハイライト 3 参照） — [日本語](https://code.claude.com/docs/ja/sub-agents#supported-frontmatter-fields) / [English](https://code.claude.com/docs/en/sub-agents#supported-frontmatter-fields)
- **ネットワークシークレットとダイアログの名前の変更がほかのページにも反映された**（`claude-code-on-the-web`・`routines`・`errors`。詳細はハイライト 2 と大幅更新 2 参照） — [日本語](https://code.claude.com/docs/ja/cloud-environments#add-network-secrets) / [English](https://code.claude.com/docs/en/cloud-environments#add-network-secrets)

**バグ修正**

- クラウドのセッションで、セッション自身のネットワークの設定がホストを止めたのに、組織のポリシーが止めたと Claude に伝える問題を修正
- 小さい自動圧縮のウィンドウを選んだとき、`/autocompact` がトークンの使用量が多いと警告する問題を修正
- バックグラウンドのコマンドが動いている間に終了すると、SessionEnd のフックが動かないことがある問題を修正
- `claude --help` の `--restricted` の説明が、削除されたツールの名前を挙げる問題を修正
- 1 つのプルリクエストのデータが不完全に返ったとき、`claude agents` がどのプルリクエストの状態も更新しない問題を修正
- クラウドのセッションのコンテナが入れ替わった後、一度再開済みのバックグラウンドのエージェントについて、失われて再開できないと Claude に伝える問題を修正
- メッセージを打ったサブエージェントが、終わった少し後に `/tasks` から消え、会話に戻れなくなる問題を修正
- 子のエージェントを見ている間に、終わった親のエージェントがパンくずから外れる（子がトップに付け直されて見える）問題を修正
- 入力がまとまって届いたとき、agents view が「up」「down」「escape」のような打った語をそのキーと取り、返答の途中でピークを動かしたり下書きを消したりしうる問題を修正
- 再開の後に MCP サーバーがつなぎ直す間などに、自動のツール検索（`ENABLE_TOOL_SEARCH=auto`）が会話の途中でオフになる問題を修正
- `forceLoginOrgUUID` に断られたログインで、断られた組織のトークンが保存されたままになるか、`/login` の後も生きている問題を修正
- reftable のリポジトリで、Claude Desktop と Remote Control のセッションの差分の表示が、衝突した cherry-pick や revert に気づかない問題を修正
- 呼び出しの入力が届く間、Artifact ツールの詳細表示と ctrl+o の行が `Artifact("(unprintable path)")` と出る問題を修正。Bash と同じく「Waiting…」「Running…」を出します
- クラッシュでトランスクリプトの最後の行が途中で切れていたとき、セッションの再開後に最初に書いたトランスクリプトの項目が失われる問題を修正
- Unicode の行区切り・段落区切り（U+2028、U+2029）を含むと、`/branch` がメッセージを落とし、`claude purge` がサブフォルダーのプロジェクトを飛ばす問題を修正
- `--worktree` で始めたとき、プラグインの `WorktreeCreate` と `WorktreeRemove` のフックが動かない問題を修正（`--tmux` とともに使う場合はまだ）
- reftable のリポジトリで `git commit -q` の後、OpenTelemetry の `tool_result` のイベントに `git_commit_id` がない問題を修正
- mod の `prompt.submit` フックが書き換えたか落としたプロンプトが、OpenTelemetry の `user_prompt` のイベントとやり取りのスパン、セッションのタイトルの要求で、打ったまま記録される問題を修正
- mod のホットリロードについての Claude 向けの注記が、利用者が打ったかのようにトランスクリプトに出る問題を修正
- エージェントのフックが自分の `model` を無視する問題を修正。`haiku` のような別名が解決され、サブエージェントのモデルで上書きされず、使えないモデルは操作を許す代わりに呼び出し元のモデルに戻ります
- コミット ID のような名前のタグやブランチがあると、`--worktree` のセッションが誤ったコミットから始まることがあり、始まりの git status が新しい worktree 以外のブランチを挙げる問題を修正
- git の reftable の ref ストレージを使うリポジトリで、ブランチが「.invalid」と出て、`--worktree` が worktree を開き直せない問題を修正
- Claude がセッションのスクラッチパッドのファイルを、完全なパスではなくファイル名だけか相対パスで呼ぶ問題を修正
- キーチェーンのロックのような短いサインインのエラーの後、`claude remote-control` のサーバーが接続の更新をあきらめる問題を修正。再試行し、`claude /login` が要るときは警告します
- origin の既定のブランチを取得できないとき、ベアリポジトリの worktree で `--worktree` が失敗する問題を修正。代わりの基点はメインのリポジトリではなく今のチェックアウトの HEAD になりました
- VS Code・Cursor・Devin Desktop の統合の端末で Claude Code を始めると、拡張機能を確かめるためにエディターのコマンドラインのツールを 2 回起動する問題を修正。1 回だけ起動します
- `chat:newline` のキーバインド（Ctrl+J か割り当て直した Enter）で入れた改行で、mod の `prompt.edit` フックが発生しない問題を修正
- API が MCP のツールの入力スキーマを断ったとき、会話が毎ターン 400 のエラーで失敗する問題を修正。会話の残りではそのツールをパラメーターなしで送ります
- 出力トークンの上限で切れた返答の後の圧縮で、ヘッドレスか Agent SDK のセッションを再開すると、圧縮が残した最近のメッセージが失われる問題を修正（この版以降の圧縮が対象）
- 圧縮の後に MCP サーバーがつながり終えたとき、次のツールの呼び出しまでそのサーバーのツールと指示が Claude に伝わらない問題を修正
- 複数のセッションを動かすコンピューターで、Remote Control のセッションが動いているのに止まったと示される問題を修正
- 同じターンで再試行したか終わらなかった返答の後の圧縮で、ヘッドレスか Agent SDK のセッションを再開すると、圧縮の要約が失われるか圧縮前の履歴が戻る問題を修正
- バックグラウンドのコマンドが動いている間、Claude がその出力ファイルをポーリングしたり sleep したりする問題を修正
- OS の証明書ストアでだけ信頼された証明書を持つ、TLS を検査するプロキシの後ろで、機能フラグと段階的な展開が古いままになる問題を修正
- 止まったバックグラウンドのサービスが動き続けているのに `claude daemon stop --any` が「stopped」と出す問題を修正。待ってからサービスを強制終了してそう伝え、まだ残っていれば終了コード 1 で終わります
- テレメトリーがオフのとき、`claude daemon stop` が何も出さずに終わり、セッションが動いているように一覧に残る問題を修正
- Cowork のクラウドのセッションの Write・Edit・NotebookEdit が、利用者のコンピューター上のパス（ファイルは届かない）に成功と報告する問題を修正
- それらを一度も挙げなかった履歴をセッションが再開したとき、会話の前のほうで読み込み済みの後回しのツールを Claude が検索する問題を修正
- 暗い ANSI のテーマと 16 色の端末で、補助の（dim の）文字が普通の文字と同じに見える問題を修正
- 組織のポリシーを読めないとき、クラウドのセッションがターンごとに 5 分ハングする問題を修正。ターンはすぐに終わり、理由を伝えます
- 長い返答の途中でセッションが再起動した後、クラウドのセッションが答え済みのメッセージをもう一度動かすことがある問題を修正
- セルフホストのランナー: 誰も出力を読まない間、ランナーとオーケストレーターが固まる（ポーリング・`/healthz`・`SIGTERM` での停止が止まる）問題を修正。ログは直近の 256 KiB を保ち、落とした量を数えます（Windows を除く）
- [VSCode] 使用量のクレジットが尽きた後も高速モードがオンのままで、各要求が断られては送り直される問題を修正。オンに戻すまでオフになり、エラーの通知を出します
- [VSCode] 常に考えるモデルで Thinking の切り替えが Off になる問題を修正。そうしたモデルでは切り替えを出しません
- [VSCode] フラグの付いたメッセージの「Edit prompt」が、復元したプロンプトの上にファイルかコマンドのメニューを開く問題を修正。Enter で書いたまま送ります
- [VSCode] Windows でファイルをプロンプトに Shift を押しながらドラッグすると、作業ディレクトリからの相対のメンションではなく読めない `/c:/…` のパスを入れる問題を修正
- [VSCode] VS Code のチャットのフォントサイズの設定の変更に、ウィンドウの再読み込みが要るかテーマの変更で戻される問題を修正。差分とプランのプレビューも従います
- [VSCode] 「Resume session」と再読み込み後に復元したタブが、git の worktree に移った会話ではなく空の新しい会話を開く問題を修正
- [VSCode] 呼び出したスラッシュコマンドで ↑ の後に Enter を押すと引数なしで動く問題を修正。呼び出したプロンプトの上には、編集するまでコマンドとファイルのメニューを開きません
- [VSCode] WSL・SSH・Dev Container のウィンドウで、エクスプローラーかエディターのタブからファイルをプロンプトに Shift を押しながらドラッグしても何も入らない問題を修正
- [VSCode] Windows と Linux で、エクスプローラー・ほかのツリービュー・デバッグコンソールの Ctrl+Alt+F が、検索を開く代わりに Focus view を切り替える問題を修正
- [VSCode] macOS で、ほかのウィンドウや端末で開いているセッションの確認が余分なプロセスを作る問題を修正。確認のたびに PATH から `ps` を探さず、`/bin/ps` を直接始めます
- [VSCode] Windows: クラッシュか電源断の後、再起動した Windows が古いプロセス ID をほかのプログラムに与えたとき、会話が「still open somewhere else」と出る問題を修正
- [Cloud sessions] 組織が「Always allow」をオフにしたコネクタのツールについて、Cowork の承認の確認に「Allow for this task」がない問題を修正（2.1.292 での退行）
- [Cloud sessions] 2 つ目のメッセージを送ると、クラウドのセッションの / メニューのほとんどのコマンドの説明が消える問題を修正
- [Remote Control] claude.ai とデスクトップアプリの Remote Control のセッションの差分の表示が、削除・名前変更したファイルを変更として出す問題を修正（自分のマシンに Claude Code v2.1.296 以降が要る）
- [Claude Tag] Claude 自身がチャンネルに投稿したメッセージの下のスレッドでほかのアプリがタグ付けしても、Slack の Claude が答えない問題を修正
- [Code Review] GitHub の組織のメンバーシップを非公開にしている書き込み権限のある人の `@claude review` のコメントを、Code Review が無視する問題を修正。そのコメントでレビューが始まります
- [Code Review] Code Review の「paused for this repository」のコメントが管理者を Code Review の設定へ送る問題を修正。誰が直せるかを伝え、Git providers のページにリンクします

**その他**

- `CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST` のセッションが、設定の `SSL_CERT_FILE` のような CA バンドル・ツールのプロキシ・git の TLS・git の設定の変数を無視するように変更（Claude Desktop の下ではプロジェクトの設定のものだけ）
- 終了時、止めるよう求めてから 1.5 秒後も動いているバックグラウンドのコマンドを強制終了するように変更（全画面モードでは動いたまま残ることがあった）
- `forceLoginGatewayUrl` がセッションのホスト名を提供する Anthropic が運用するゲートウェイを指すとき、Claude Desktop の Code タブが管理設定を適用するように変更。そのゲートウェイは開始時に到達できる必要があります
- Claude Desktop がゲートウェイから使えない `desktop:` のポリシーのキーがあるとき、`claude gateway` が開始時にそのキーを挙げて止まるように変更（これまでは警告して始まった）
- テレメトリーがオフでも、api.anthropic.com への大きな要求に gzip の圧縮を使うように変更。`CLAUDE_CODE_GZIP_REQUEST_BODIES=0` でオフにできます
- `claude-api` スキルが、アーカイブか削除を求められない限り Managed Agents のセッションをそのまま残すように変更
- バックグラウンドのセッションが、引き継いだワークフローをハンドオフのファイルから動かす代わりに、Workflow ツールの承認を通して再開するように変更
- ローカルのセッションのトランスクリプトに、各 API の要求のシステムプロンプト・ツール・パラメーターも記録するように変更。共有を選んだトランスクリプトで要求を正確に再現できます
- `/sandbox` のモードの選択肢を「Sandbox BashTool」から「Sandbox commands」の表記に変更
- Cowork のクラウドのセッションの `PermissionRequest` フックを変更。フックの allow の中の `setMode` の更新は無視され、承認のほかの部分は引き続き適用されます
- フックを変更。PreToolUse と PermissionRequest のフックの `updatedInput` を Claude 自身の入力と同じく検証し、知らないキーは落とし、ツールが断る入力は呼び出しを拒否します
- 効果のなかった `claude remote-control` の `--sandbox` と `--no-sandbox` のフラグを削除。渡すとエラーで終わります。セッションをサンドボックスで動かすには設定の `sandbox.enabled` を使います
- [Claude Tag] 管理者が Slack のチャンネルに付けたアクセスのバンドルが、そのチャンネルが Slack Connect のチャンネルになっても付け直さずに効き続けるように変更
- **Claude API と Managed Agents の OpenTelemetry への案内**（`monitoring-usage`・`agent-sdk/observability`）: 冒頭に、Claude API か Managed Agents については platform.claude.com の「OpenTelemetry for the Claude API」を見るよう注記が加わりました
- **`/mcp` での確かめ方の書き方**（`mcp`）: サーバーが `connected`・`failed` と出る、から、サーバーの行にチェックマーク・✘ が出る、に改められました
- **Trusted Devices の対象**（`remote-control`）: 設定が Claude Code の Remote Control と、Cowork の Computer access に効く、と改められました
- **プロジェクトの設定**（`claude-projects`）: MCP サーバーの説明から **Project settings > Environment** の **Manage connectors** のリンクが、設定の表から Connectors の行が外れました
- **クラウドのセッションのブランチの選び方**（`web-quickstart`）: claude.ai/code では、リポジトリのセレクターの後のコントロールでブランチを変える、と書き直されました
- **`CLAUDE_CODE_RESUME_INTERRUPTED_TURN_MAX_AGE_MS` の書き方**（`env-vars`）: 未設定か `0` のとき、API のエラーで終わったターンなど一部のターンは最後のメッセージから 6 時間以内だけ再開する、という書き方になりました
- **`--bare` の説明**（`headless`）: ベアモードでない `claude -p` は、対話のセッションと同じようにフックやスキルなどを見つけて読み込む、という言い回しになりました
- **セルフホストのセッションの再キュー**（`self-hosted-environments`・`self-hosted-environments-deploy`）: ランナーのリースが切れた後の再キューは「数分以内」ではなく「数分、ときにはそれ以上」かかりうる、と改められました
- **`setup` の書式の崩れが直った**: 前回挙げた、インストールのコマンドの 5 つのコードブロックの開始行で `theme={null}` が 21 回ずつ繰り返されていた状態が、1 回に戻りました
- **見出しマップ**: 31 行が加わり 1 行が外れました。外れたのは自動生成のスタンプの古い行で、加わったのは新しいスタンプと、`desktop`（20）・`errors`（2）・`self-hosted-environments-configuration`（2）・`vs-code`・`sub-agents`・`skills`・`plugin-evals`・`plugins/mods/reference`・`cloud-environments`（各 1）の 30 の見出しです
- **見出しマップ冒頭の自動生成スタンプが、2026年10月14日 03時39分40秒 UTC から 2026年10月15日 04時55分03秒 UTC へ進みました**

**参考リンクについて**: 日本語版は、リンクを付けたページをすべて取得して、該当する節があるかと今回の内容（新しい節や書き換えた文）になっているかを確かめました。今回も日本語版の追従が早く、`desktop` の SSH のセッションの新しい節（プロキシと CA 証明書・`ProxyCommand`・ポートの転送・ファイルとプロセス・ログイン前に閉じる接続・ログイン後の接続失敗・ログの取り方）、`cloud-environments` のネットワークシークレット、`sub-agents` の `autoCompactWindow`、`skills` と `errors` の名前の拒否、`artifacts` の公開と編集をはじめ、リンクを付けたすべてのページの該当の節がすでに今回の内容になっていたため、すべて日本語版のリンクを付けています。取得して確かめていないページ（`network-config`・`agent-sdk/typescript`・`env-vars` など）と、changelog だけに載っていて対応する節のない項目にはリンクを付けていません。**changelog ページへのリンクは、本サマリの方針どおり付けていません。**

## 新着情報

**今回、`whats-new/` 配下のページに変更はありません。**

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-10-13.md](./archives/latest/2026-10-13.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-10-13.md](./archives/latest-detail/2026-10-13.md)

<!--
base_commit: fff3c0a4cd3191932565fb654f66a1d7539bbc49
head_commit: eeed0d5ebbc9b23608e5903e7bc33bb6c996a581
generated_at_full: 2026-10-15T15:09:28+09:00
-->
