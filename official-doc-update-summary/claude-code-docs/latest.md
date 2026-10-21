---
対象期間: 2026年10月19日 〜 2026年10月20日
作成日: 2026-10-20
---

# Claude Code 公式ドキュメント更新サマリ

```markdown
**今回は、`llms-full.txt` の書式が MDX のコンポーネント（`<Note>`・`<Steps>`・`<Tabs>`・`<Update>` など）から GitHub 風の Markdown に変わり、228 ページ中 220 ページに差分が出ました。内容の変更ではなく生成形式の変更ですが、changelog の各リリースの日付が消えるなどの影響があります。その下で本文も 81 ページが変わり、routines が「cloud scheduled tasks」に改称され、mod の承認と権限のルール・フックの優先順位が書き直され、マウントしたドライブへの `rm` の確認と、`/usage` の推奨を `f` で適用する機能（v2.1.305 以降）が載りました**。新しいページはなく、changelog に新しい版の項はありません（先頭は v2.1.304 のまま）。書式の変換を吸収して数えると、本文の変更は 81 ページ・1,324 行（追加 934・削除 390）で、大幅更新は `routines`・`errors`・`agent-view`・`desktop-scheduled-tasks`・`plugins/mods/api`・`permission-modes`・`agent-sdk/typescript` の 7 ページです。総行数は 121,524 行から 120,396 行に減りました。

主要なものを以下に挙げます。

1. `llms-full.txt` の書式が MDX から Markdown に変わり（コールアウトは `> [!NOTE]` など）、changelog の 424 リリースと whats-new の索引の 24 週の日付が消え、whats-new の「Other wins」は 1 行に連結された
2. routines が「cloud scheduled tasks」に、`/loop` などのセッション内の予定が「session-scoped scheduled tasks」に改称され（31 ページ）、旧名が残る場所の節と Desktop の新しい作成手順が載った
3. mod の承認が権限のルールとフックをどこまで越えられるかが、managed settings と Team・Enterprise の `/login` の有無で書き分けられ、`dontAsk` モードでも mod が承認しうると 8 ページに添えられた
4. マウントしたドライブ（`/Volumes`・`/media`・`/mnt` など）への再帰的な `rm` に確認を出す「The mounted drive prompt」の節と、それをオフにする `CLAUDE_CODE_DISABLE_MOUNTED_DRIVE_RM_PROMPT` が載った
5. `/usage` の内訳が使用量を減らす推奨を示すようになり、`f` キー（VS Code ではボタン）で適用できる推奨をまとめて適用できると載った（v2.1.305 以降）
```

## ハイライト

1. [**llms-full.txt の書式が MDX から Markdown に変わり changelog の日付などが消えた**](./latest-detail.md#1-llms-fulltxt-の書式が-mdx-から-markdown-に変わり-changelog-の日付などが消えた):  
  `llms-full.txt` の生成形式が変わり、`<Note>`・`<Steps>`・`<Tabs>`・`<Update>` などの MDX のコンポーネントが GitHub 風の Markdown（`> [!NOTE]` のコールアウト、太字の見出し、URL 付きの画像）に置き換わりました。228 ページ中 220 ページに差分が出ましたが、内容の変更ではありません。changelog の 424 リリースと whats-new の索引の 24 週は日付を失い、whats-new の 24 ページの「Other wins」は項目が区切りなく 1 行に連結されています
2. [**routines が cloud scheduled tasks に改称され /loop の予定は session-scoped scheduled tasks になった**](./latest-detail.md#2-routines-が-cloud-scheduled-tasks-に改称され-loop-の予定は-session-scoped-scheduled-tasks-になった):  
  `routines` のページが「Automate work with scheduled tasks」になり、クラウドで動く routines は「cloud scheduled tasks」（以前の routines）、`/loop` と cron のツールの予定は「session-scoped scheduled tasks」と呼ばれるようになりました。旧名が残る場所（`claude.ai/code/routines`・`/routines`・API の `/fire` など）を挙げる節ができ、組織のトグルは「Scheduled tasks (Was Routines)」に、Desktop の作成手順は「Only on this computer」をオンにする形になりました
3. [**mod の承認と権限のルール・フックの優先順位が managed settings と Team・Enterprise の /login の有無で書き分けられた**](./latest-detail.md#3-mod-の承認と権限のルールフックの優先順位が-managed-settings-と-teamenterprise-の-login-の有無で書き分けられた):  
  `permissions` の「Precedence among rules, hooks, and mods」が書き直され、managed settings があるか Team・Enterprise の `/login` がセッションの資格情報なら、mod が承認しても deny ルール・ask ルール・`PreToolUse` フックなどの結果は既定で残る、と整理されました。API キーや `CLAUDE_CODE_OAUTH_TOKEN` のセッションはこの `/login` に当たりません。`dontAsk` モードでも mod が一部の呼び出しを承認しうる、と 8 ページに添えられ、`tool.check` の `e.isReadOnly` の節もできています
4. [**マウントしたドライブへの再帰的な rm に確認を出す mounted drive prompt の節ができた**](./latest-detail.md#4-マウントしたドライブへの再帰的な-rm-に確認を出す-mounted-drive-prompt-の節ができた):  
  `permission-modes` に h3「The mounted drive prompt」と 3 つの h4 ができました。macOS・Linux・WSL で再帰的な `rm` が `/Volumes/<drive>`・`/media/<user>`・`/mnt/<name>` などを狙うと、allow ルールがあっても重要なパスの削除と同じく確認か拒否になります。`CLAUDE_CODE_DISABLE_MOUNTED_DRIVE_RM_PROMPT=1`（v2.1.304 以降、起動する環境で設定）でオフにできます
5. [**/usage が使用量を減らす推奨を示し f キーでまとめて適用できると載った**](./latest-detail.md#5-usage-が使用量を減らす推奨を示し-f-キーでまとめて適用できると載った):  
  `costs` の「Plan usage breakdown」の「Behavior flags」が「Recommendations」に代わり、使用量の 10% 以上に関わる変更を 1 行ずつ示すようになりました。h4「Apply recommendations with the fix shortcut」ができ、フッターに `f to fix 2 of 3` のような表示があれば `f` を押して、Claude Code が適用できる推奨を適用します（v2.1.305 以降）。VS Code では同じ推奨とボタンが Account & usage のダイアログに出ます

## 新規追加されたページ

（今回の対象期間に新規追加・削除されたドキュメントページはありません。`llms.txt` は変わらず、URL は 275 のままで、`llms-full.txt` に展開されている固有のページも 228 のままです。`Source:` の行が 231 あり 3 ページが 2 回展開されている状態も前回と同じです）

## 大幅に更新されたページ

- [**Automate work with scheduled tasks**](./latest-detail.md#1-automate-work-with-scheduled-tasks) ([日本語](https://code.claude.com/docs/ja/routines#create-from-the-web) / [English](https://code.claude.com/docs/en/routines#create-from-the-web)):  
  257 行（追加 143・削除 114）が変わりました。改称（詳細はハイライト 2）に加え、Web のダイアログでの作成手順、API のトリガーのトークンの扱い、トリガーの削除の仕方が新しい画面に合わせて書き直されています
- [**Error reference**](./latest-detail.md#2-error-reference) ([日本語](https://code.claude.com/docs/ja/errors#no-llm-gateway-opened-from-another-folder) / [English](https://code.claude.com/docs/en/errors#no-llm-gateway-opened-from-another-folder)):  
  132 行（追加 111・削除 21）が変わりました。`No LLM gateway`・`Plugin not loaded`・`File is too large to read as an image`・`/feedback is disabled`・artifact の `Not published` の 5 つの h3 ができ、Cowork の MCP の資格情報の拒否や `API_TIMEOUT_MS=0` の説明が加わりました
- [**Manage multiple agents with agent view**](./latest-detail.md#3-manage-multiple-agents-with-agent-view) ([日本語](https://code.claude.com/docs/ja/agent-view#set-the-model-effort-and-fast-mode) / [English](https://code.claude.com/docs/en/agent-view#set-the-model-effort-and-fast-mode)):  
  77 行（追加 53・削除 24）が変わりました。ディスパッチの入力の `/effort` と `/fast`（v2.1.299 以降）、過去のセッションを戻す `/resume`、スーパーバイザーが止まった後の手順、`No LLM gateway` のトラブルシューティングが載りました
- [**Schedule recurring tasks in Claude Code Desktop**](./latest-detail.md#4-schedule-recurring-tasks-in-claude-code-desktop) ([日本語](https://code.claude.com/docs/ja/desktop-scheduled-tasks#create-a-scheduled-task) / [English](https://code.claude.com/docs/en/desktop-scheduled-tasks#create-a-scheduled-task)):  
  62 行（追加 44・削除 18）が変わりました。**Scheduled** のページと **Only on this computer** をオンにして作る新しい手順（詳細はハイライト 2）、worktree を作成後の編集で選ぶ形が載りました
- [**Use the mods API**](./latest-detail.md#5-use-the-mods-api) ([日本語](https://code.claude.com/docs/ja/plugins/mods/api#calls-and-background-work-after-the-user-interrupts-a-turn) / [English](https://code.claude.com/docs/en/plugins/mods/api#calls-and-background-work-after-the-user-interrupts-a-turn)):  
  62 行（追加のみ）が変わりました。ユーザーがターンを止めた後に mod の呼び出しが次の入力まで断られることと、その再試行の方法を説明する h3 ができました（v2.1.304 以降）
- [**Choose a permission mode**](./latest-detail.md#6-choose-a-permission-mode) ([日本語](https://code.claude.com/docs/ja/permission-modes#the-mounted-drive-prompt) / [English](https://code.claude.com/docs/en/permission-modes#the-mounted-drive-prompt)):  
  53 行（追加 43・削除 10）が変わりました。「The mounted drive prompt」（詳細はハイライト 4）と `dontAsk` の mod の注記（詳細はハイライト 3）のほか、分類器のモデルの表が並べ直されました
- [**Agent SDK reference - TypeScript**](./latest-detail.md#7-agent-sdk-reference---typescript) ([日本語](https://code.claude.com/docs/ja/agent-sdk/typescript#sdkcontrolgetcontextusageresponse) / [English](https://code.claude.com/docs/en/agent-sdk/typescript#sdkcontrolgetcontextusageresponse)):  
  52 行（追加 40・削除 12）が変わりました。`getContextUsage()` の応答に `categories[].id`・`mcpInstructions`・`pluginId`・`path` の型が載り（Agent SDK v0.3.304 以降）、`RemoteTrigger` などの説明が改称に合わせて改められました

## 軽微な更新

今回の差分は **2 ファイル**（`llms-full.txt` と見出しマップ）で、`llms.txt` は変わっていません。`llms-full.txt` の生の差分は追加 30,037 行・削除 31,165 行で、ページの並びは変わらず、228 ページ中 220 ページ（changelog を含む）に差分が出ました。ハイライト 1 の書式の変換を吸収して数えると（方法は大幅更新の後の注記）、220 ページは次の 3 つに分かれます。

- **差分が残らないページ: 111**（changelog と whats-new の 20 ページを含む）。changelog は、各リリースの日付が消えたほかは変わっていません（日付は正規化で数えない属性なので、この 111 に入る）。新しい版の項はなく、先頭は前回と同じ v2.1.304、収録リリースは 424 です（前回サマリの「447 から 448」は whats-new の索引の週の項 24 も含めた `<Update>` の数でした）
- **書式の差だけが残るページ: 28**（図の代替テキストの重複の解消、独自のコンポーネントの展開、カードのタイトルのリンク化、whats-new の 5 ページの「Other wins」の連結など）
- **本文が変わったページ: 81**（1,324 行、追加 934・削除 390）。大幅更新の 7 ページを除く **74 ページ**を以下にまとめます

`llms-full.txt` の総行数は **121,524 行から 120,396 行へ 1,128 行減り**ました（生の差分の差し引き 30,037 − 31,165 と一致）。閉じタグの行や字下げの外れたコンポーネントの行がなくなったためで、本文が減ったわけではありません。`Source:` の行は 231、固有のページは 228 のままです。コードフェンスの外の見出しは 5,694 から 5,737 へ増えました。加わった 54 のうち 4 つは、`gitlab-ci-cd` の `<Steps>` の中で字下げされていた「Prerequisites」「Setup instructions」（2 つずつ）が字下げを外れて見出しとして数えられるようになったもので、残る 50 は本文の新しい見出しか改称です（`routines` 8・`permission-modes` 5・`errors` 5・`agent-view` 4・`plugins/mods/api` 4・`scheduled-tasks` 3 など）。外れた 11 はすべて改称で、`routines` 6（H1 を含む）・`scheduled-tasks` 3・`agent-view` と `permission-modes` 1 ずつです。

**新機能**

- **mounted drive prompt と `CLAUDE_CODE_DISABLE_MOUNTED_DRIVE_RM_PROMPT` が載った**（`permission-modes`・`env-vars`・`settings-reference`。v2.1.304 以降。詳細はハイライト 4 参照）
- **`/usage` の推奨と `f` での適用、`settings:fixUsage`、`/doctor` の「Usage」のチェックが載った**（`costs`・`vs-code`・`keybindings`・`skills`。v2.1.305 以降。詳細はハイライト 5 参照）
- **mod の `tool.check` の `e.isReadOnly` と、matcher の `isReadOnly: true` が載った**（`plugins/mods/events`・`plugins/mods/reference`。v2.1.304 以降。詳細はハイライト 3 参照）
- **ターンの中断の後の mods API の呼び出しの扱いが載った**（`plugins/mods/api`・`plugins/mods/troubleshoot`。v2.1.304 以降。詳細は大幅更新 5 参照）
- **エージェントビューのディスパッチの入力の `/effort` と `/fast`、`/resume` のピッカーの節が載った**（`agent-view`。詳細は大幅更新 3 参照）
- **`API_TIMEOUT_MS` を `0` にしてタイムアウトを外せると載った**（`env-vars`・`errors`。v2.1.305 以降）。`0` にしても、ローカルのセッションの非ストリーミングの試行は 300 秒で終わります。`errors` には、Bedrock 以外で `0` のときの再試行は 10 分と 32KB ごとに 1 秒（最初の試行のほうが長ければその長さ）待つ、とも書かれました — [日本語](https://code.claude.com/docs/ja/env-vars#variables) / [English](https://code.claude.com/docs/en/env-vars#variables)
- **使用量の上限の解除を確かめる `CLAUDE_CODE_RETRY_WATCHDOG_USAGE_LIMIT_RECHECK_MS` が載った**（`env-vars`・`errors`。v2.1.305 以降）。`CLAUDE_CODE_RETRY_WATCHDOG` で上限のリセットを待つ要求が、上限がすでに解けたかを確かめる最小の間隔（`60000`〜`10800000` のミリ秒）で、解けていればすぐ送ります。確かめるのは claude.ai のサブスクリプションのセッションか週の上限で、使用量のクレジットを使っていない間だけです
- **`Ctrl+C` で消した下書きを戻す節ができた**（`interactive-mode` の新しい h3「Bring back a cleared draft」）。`Ctrl+C` で消した下書きは、すぐなら空のプロンプトで `Up`（v2.1.288 以降）、メッセージを送った後でも `Up` で戻れます（v2.1.292 以降。セッションごとに直近 10 件を、貼り付けたテキストと画像とともに保ち、終了で捨てる） — [日本語](https://code.claude.com/docs/ja/interactive-mode#bring-back-a-cleared-draft) / [English](https://code.claude.com/docs/en/interactive-mode#bring-back-a-cleared-draft)
- **Remote Control のプロジェクトごとの既定の spawn モードと、`DISABLE_TELEMETRY`・`DO_NOT_TRACK` のときの自動接続の節ができた**（`remote-control`）。起動時に `Spawn mode: <mode> (saved for this folder; press w to change)` と出るのは、このプロジェクトに前に保存したモードで、`Spawn mode for this project:` への答えか、動作中に `w` で切り替えたモードが保存されます（`--spawn` で起動した回でも `w` で切り替えれば保存される）。`DISABLE_TELEMETRY` か `DO_NOT_TRACK` だけを設定したセッションは組織の既定や Claude Code の既定では自動接続せず、`/config` で「Enable Remote Control for all sessions」を `true` にします（v2.1.283 以降。組織が Trusted Devices を求めるなら変数を外す）。`claude remote-control --help` は、v2.1.302 以降は対象のサインインがなくてもフラグを表示します — [日本語](https://code.claude.com/docs/ja/remote-control#set-the-default-spawn-mode-for-a-project) / [English](https://code.claude.com/docs/en/remote-control#set-the-default-spawn-mode-for-a-project)
- **`claude --cloud` の「Branch is not on GitHub」の節ができた**（`claude-code-on-the-web`）。`Branch <name> is not on GitHub` で始まる行が出ると、クラウドのセッションはそのブランチではなく、ブランチの履歴のプッシュ済みのコミットかリポジトリの既定のブランチから始まります。手元だけのコミットとコミットしていない変更は入らないので、必要ならブランチをプッシュして新しいセッションを始めます — [日本語](https://code.claude.com/docs/ja/claude-code-on-the-web#branch-is-not-on-github) / [English](https://code.claude.com/docs/en/claude-code-on-the-web#branch-is-not-on-github)
- **Code Review の `@claude review stop` のコメントのコマンドが載った**（`code-review-pull-requests` の「Comment commands」）。`@claude review always` で購読したプルリクエストの、プッシュでのレビューの購読を終えます（実行中や待ち行列のレビューは取り消さず、チェックの実行ではなくコメントで返す）。`off` と `pause` も同じで、「After every push」のリポジトリではコメントで止められず、ドラフトにします。`always` か `stop` の綴りを誤るか次の行に書くと、ただの `@claude review` として 1 回レビューします。スクリプトで結果を読む手順は、最後の行の `<!-- bughunter-severity: {...} -->` の HTML コメントだけから数を取る `jq` のコマンドになり、行がなければ `no severity line` のエラーで 0 以外で終わります — [日本語](https://code.claude.com/docs/ja/code-review-pull-requests#comment-commands) / [English](https://code.claude.com/docs/en/code-review-pull-requests#comment-commands)
- **`/artifacts` で `d` を押して artifact を削除できると載った**（`artifacts` の「Find an artifact again」）。クラウドのセッションの外で、自分の artifact を確認の後に完全に削除し、リンクは誰にとっても使えなくなります。コンプライアンスの API のパスは `/v1/compliance/code/artifacts` から `/v1/compliance/apps/code/artifacts` に、リファレンスのリンク先も `platform.claude.com` に改められました
- **`/design consent` と `/design revoke` が載った**（`commands`）。Claude Design への Claude のアクセスを許すか取り消すコマンドで、Claude が `/design consent` の実行を求めたら自分でプロンプトに入力します。`/design-login` は `/design-sync` か `/design consent` が求めたときにサインインする、と添えられました
- **`/claude-api` の `managed-agents-secure` が載った**（`skills`・`commands`）。1 つの Managed Agent の設定を読み、「Secure your Managed Agents deployment」のガイドと合うか違うかを報告します（`ant` CLI が要る。v2.1.304 以降）
- **`/auto-mode-setup` が Enterprise のプランと Claude Console の API キーでも使えると載った**（`auto-mode-config`・`commands`）。Pro・Max・Team は v2.1.228 以降（ネイティブの Windows は v2.1.233 以降）、Enterprise と Console の API キーは v2.1.283 以降が要ります。新しい h3「`/auto-mode-setup` returns "Unknown command"」は、インストールか更新の後の最初のセッション、古い版、テレメトリをオフにしたセッション・サードパーティのプロバイダー・Claude apps gateway（v2.1.304 より前は機能フラグを取得しないセッションで使えない）、クラウドのセッション、の 4 つの原因を挙げます。`env-vars` の「機能フラグの取得をオフにするとできないこと」の一覧からは `/auto-mode-setup` が外れました — [日本語](https://code.claude.com/docs/ja/auto-mode-config#auto-mode-setup-returns-unknown-command) / [English](https://code.claude.com/docs/en/auto-mode-config#auto-mode-setup-returns-unknown-command)
- **`CLAUDE_CODE_AUTO_COMPACT_WINDOW` の値と警告の節ができた**（`model-config` の新しい h4「Values and warnings for `CLAUDE_CODE_AUTO_COMPACT_WINDOW`」）。値が 100,000〜1,000,000 の外か、トークン数でなければ警告が出て、v2.1.304 以降は `200k` や `1M` のように `k` と `M` を付けられます。警告の文面ごとに使われるウィンドウと直し方の表があり、接尾辞のない数はそのトークン数と読む（`200` は 200 トークン。`/autocompact 200` は 200,000）と注意しています。`env-vars`・`settings-reference`・`sub-agents` の説明も、Claude Code が値を無視する場合を除く形に改められました — [日本語](https://code.claude.com/docs/ja/model-config#claude_code_auto_compact_window-values) / [English](https://code.claude.com/docs/en/model-config#claude_code_auto_compact_window-values)
- **idle compaction を `/config` で切り替えられると載った**（`settings-reference` の `idleCompaction`）。`/config` の **Idle compaction** の行で切り替え、ユーザーの設定に保存されてすぐ効きます（v2.1.302 以降）。行が出なければ、ほかの設定のソースがキーを設定しているか、機能フラグを取得できず idle compaction が動かないかです
- **圧縮の後にスキルの説明を入れ直すと載った**（`context-window` の「What survives compaction」）。スキルの説明は現在のスキルから作り直して入れ直されます（v2.1.304 以降）
- **iTerm2 3.5 以降で mod の `Image` が描かれると載った**（`plugins/mods/gallery`・`plugins/mods/reference`。v2.1.305 以降）。iTerm2 では fullscreen のレンダリングの下だけで描かれ（`CLAUDE_CODE_ALT_SCREEN_FULL_REPAINT=1` の間は描かれない）、`source` が `png` か `rgba` のバイトのときに描き、`file` のパスでは代替テキストを出します。kitty と Ghostty を検出できなかった場合の説明は、描ける端末の一覧の形に改められました — [日本語](https://code.claude.com/docs/ja/plugins/mods/gallery#image-and-client) / [English](https://code.claude.com/docs/en/plugins/mods/gallery#image-and-client)
- **VS Code でバックグラウンドのサブエージェントのツールの呼び出しを見る節ができた**（`vs-code` の新しい h4「See a background subagent's tool calls」）。サブエージェントがツールの呼び出しのない 1 行の状態で出るときは、プロンプトボックスで `/tasks` を入力してエージェントマップを開き、そのサブエージェントをクリックします。`claudeProcessWrapper` を設定して会話が見つからないときは拡張機能を 2.1.304 以降に更新する、スクリーンリーダーが SessionStart のフックの実行中に「Running start-up hooks.」と読む、とも加わりました — [日本語](https://code.claude.com/docs/ja/vs-code#see-a-background-subagents-tool-calls) / [English](https://code.claude.com/docs/en/vs-code#see-a-background-subagents-tool-calls)
- **LLM ゲートウェイが会話の途中の system メッセージを転送すると載った**（`llm-gateway-protocol` の「Feature pass-through」）。Claude Code は Claude Opus 4.8 とその後のモデル、認識しないモデル ID に、リマインダーなどを `messages` の `role: "system"` の項目として送り、ゲートウェイが `Unexpected role "system"` などの `400` を返すと system メッセージなしで再試行します。Opus 5.5・Sonnet 5.5・Haiku 5.5・Fable 5.1 でターンごとに effort を設定する beta ヘッダーと `output_config.effort` の組の行も加わりました — [日本語](https://code.claude.com/docs/ja/llm-gateway-protocol#feature-pass-through) / [English](https://code.claude.com/docs/en/llm-gateway-protocol#feature-pass-through)
- **セルフホストの環境の運用の説明が加わった**（`self-hosted-environments-configuration`・`self-hosted-environments-deploy`）。`spawn-runner` フックがバックグラウンドに残すプロセスの出力をファイルへリダイレクトする h4「Send a background process's output to a file」ができ（しないとオーケストレーターが 64 KB まで記録して残りを捨てる。v2.1.305 より前は終了したフックも `--hook-timeout` に達した）、Activity タブの **Queued** と **Failed** の読み方、コネクターと同名のサーバーは接続されないこと、git のプロキシで `reftable` の形式の事前の clone が参照を失うこと、`Resource temporarily unavailable` の書き込みのエラーと `This runner couldn't read` で始まらないセッションの対処が加わりました — [日本語](https://code.claude.com/docs/ja/self-hosted-environments-configuration#send-a-background-processs-output-to-a-file) / [English](https://code.claude.com/docs/en/self-hosted-environments-configuration#send-a-background-processs-output-to-a-file)
- **プラグインの `bin/` が PowerShell のツールの `PATH` にも入ると載った**（`plugins/components`・`plugins/security`）。サンドボックスの外で動く PowerShell のコマンドは `bin/` を `PATH` に持ち、サンドボックスの中では持ちません
- **組み込みのプラグインが見つからないときのメッセージが載った**（`plugins/cli-reference`）。`@builtin` で終わる ID のプラグインが見つからなければ、組み込みのプラグインは `claude plugin list` に出ないので `/plugin` の **Installed** タブを見る、というメッセージになります
- **Claude Desktop on 3P が Claude API でも Code タブを動かせると載った**（`feature-availability`・`desktop-linux`）。Anthropic Console の API キーで Claude API を使う形で、プロバイダーの要約の表にも Desktop の部分的な対応として挙がりました
- **SSO のサインインで使うホスト `sso.claude.com` が載った**（`network-config`・`hipaa-setup`・`desktop`・`self-hosted-environments-deploy`）。シングルサインオンを使う組織のブラウザーのサインインの経路で、プロキシが止めるとサインインが失敗しえます
- **Chrome の「No browsers are connected」の行が加わった**（`chrome` のトラブルシューティングの表）。拡張機能が同じ claude.ai のアカウントと組織でサインインしているか、Claude Code が `bridge.claudeusercontent.com` に届くかを確かめます
- **MCP の `claude mcp get` が WebSocket のサーバーの値も隠すと載った**（`mcp` の「Plugin-provided MCP servers」）。`URL: ws` と `<name>: [REDACTED]` を示し、`claude mcp list` は URL の代わりに `ws` を示します

**機能改善**

- **routines の改称（cloud scheduled tasks・session-scoped scheduled tasks）が 31 ページに入った**（詳細はハイライト 2 参照）。routines を cloud scheduled tasks と呼び直したのは `routines`・`desktop-scheduled-tasks`・`scheduled-tasks`・`claude-projects`・`cloud-environments`・`claude-code-on-the-web`・`errors`・`commands`・`tools-reference`・`agent-sdk/typescript`・`skills`・`interactive-mode`・`feature-availability`・`overview`・`common-workflows`・`web-quickstart`・`glossary`・`goal`・`agents`・`admin-setup`・`github-enterprise-server`・`self-hosted-environments`・`self-hosted-environments-configuration`・`self-hosted-environments-deploy` の 24 ページ、`/loop` などの予定を session-scoped scheduled tasks と呼び直したのは `scheduled-tasks`・`tools-reference`・`agent-sdk/typescript`・`skills`・`env-vars`・`costs`・`hooks`・`sessions`・`artifacts`・`channels`・`code-review-local` の 11 ページです。`platforms` の「Scheduled tasks」へのリンクも「Scheduling options」（スケジュールの選択肢の比較）へのリンクに改められました
- **mod の承認と権限のルール・フックの優先順位が書き分けられ、`dontAsk` に mod の注記が添えられた**（`permissions`・`plugins/mods/admin` ほか。詳細はハイライト 3 参照）
- **Desktop のスケジュールされたタスクの作成手順が新しい画面に合わせて書き直された**（`desktop-scheduled-tasks`・`routines`。詳細は大幅更新 1・4 参照）
- **`CLAUDE_CODE_MAX_RETRIES` に、529 の過負荷のエラーで早く再試行をやめる場合が載った**（`env-vars`）。たとえば API キーで Opus のモデルを使うと 3 回目の `529` で止まり「Repeated 529 Overloaded errors」を示し、フォールバックのモデルを設定していればそちらに切り替えます
- **cross-session messaging の返事の制限が節になった**（`cross-session-messaging` の新しい h4「Replies from other machines and cloud sessions」）。クラウドのセッション（セルフホストのランナーを含む）は、返信先があってもほかのマシンからのメッセージに `SendMessage` で返事できず、応答は claude.ai/code のトランスクリプトで読みます。Remote Control なしで送ったメッセージには返信先がない、という文もここに移りました。`remote-control` からも、同じ接続がクラウドのセッションからのメッセージを運ぶ、という記述が外れています — [日本語](https://code.claude.com/docs/ja/cross-session-messaging#replies-from-other-machines-and-cloud-sessions) / [English](https://code.claude.com/docs/en/cross-session-messaging#replies-from-other-machines-and-cloud-sessions)
- **巻き戻したメッセージが戻る場合の節ができた**（`checkpointing` の新しい h4「Rewound messages can return if you exit before your next prompt」）。巻き戻した後、次のプロンプトを送る前に終了すると、巻き戻したメッセージが戻ることがあります。`/rewind` で同じプロンプトを選んで **Restore conversation** を選び、終了の前に Claude にプロンプトを送ります（巻き戻した会話はそのプロンプトとともに保存される） — [日本語](https://code.claude.com/docs/ja/checkpointing#rewound-messages-can-return-if-you-exit-before-your-next-prompt) / [English](https://code.claude.com/docs/en/checkpointing#rewound-messages-can-return-if-you-exit-before-your-next-prompt)
- **構造化された出力がないときの扱いが明記された**（`headless`・`agent-sdk/troubleshooting`）。Claude が要求を断ったときなどは `structured_output` のフィールドがないので、使う前に確かめます。Agent SDK では、結果のメッセージの `stop_reason` が `"refusal"` かで見分け、満たせないスキーマ（`minLength` が `maxLength` より大きいなど）と並べて原因が箇条書きになりました
- **サブエージェントがフォールバックのモデルで終わったときの表示が載った**（`sub-agents` の「API errors in subagents」）。報告が `⚠ This agent switched to <model> because its earlier model could not be used.` で始まります
- **WebSearch の上限が `-p` と Agent SDK ではターンごとと明記された**（`tools-reference` の「Session search limit」）。次のメッセージを送るか新しい `claude -p` を実行すると（`--continue`・`--resume` でも）上限は戻ります
- **mod のペインの幅の上限が載った**（`plugins/mods/interface`）。トランスクリプトの横のペインは端末の幅の 45% までで、ユーザーが一度幅を変えると、そのセッションか前のセッションで設定した幅で開きます
- **`strictPluginOnlyCustomization.hooks` のロックの範囲が明記された**（`settings-reference`）。ユーザー・プロジェクト・ローカルの `settings.json` のフックに加え、`skills` か `agents` のロックが止めるソースのスキル・カスタムコマンド・エージェントのフロントマターのフックも止めます（それらのスキルなどは、自分の面がロックされていなければ読み込まれる）
- **OpenTelemetry の属性の上限を下げたときに落ちる順が載った**（`monitoring-usage` の「Tool decision event」）。`OTEL_LOGRECORD_ATTRIBUTE_COUNT_LIMIT` を `tool_decision` の属性の数より下げると、`permission_mode`・`classifier_category`・`classifier_verdict` の順に落ち、ほかの属性はその後です（v2.1.302 以降）
- **キーバインドの検証の項目が加わった**（`keybindings` の「Validation」）。`ctrl+ k` のように `+` の隣に空白があると、`ctrl+` と `k` のコードと読まれて決して発火しません
- **言い回しの調整**: `agent-sdk/custom-tools` の完全修飾のツール名の説明、`agent-sdk/python` と `agent-sdk/typescript` の `/context` のデータ（「同じ」から「含む」へ）、`env-vars` の `CLAUDE_CODE_DISABLE_BG_EXIT_HANDOFF`・`CLAUDE_CODE_FORCE_TERMINAL_IMAGES`・`ENABLE_PROMPT_CACHING_1H`、`costs` のキャッシュのミスの項目（プロンプトキャッシュの寿命の決まり方へのリンクに置き換え）、`glossary` のクラウドのセッション、`cloud-environments`・`claude-projects` の段落の箇条書き化、`plugins/mods/create`・`workflows`・`self-hosted-environments` の文の組み替えなどです

**バグ修正**

changelog に新しい版の項はなく、通常のページに次の修正（と古い版での症状）が載りました。

- インストールと更新: `claude update` か `claude install` がリリースを本物と確かめられず何も入れなかった `Release verification failed for Claude Code <version> (<reason>)`（括弧の値が `sidecar_fetch_` で始まればもう一度実行する）と、セッションのフッターの赤い `Auto-update failed · Run claude doctor`（シェルで `claude update` を実行する）の h3 が `troubleshoot-install` にでき、`troubleshooting` と `errors` の表にも行が加わりました。`setup` の `claude doctor` の説明も、ネイティブのインストールで失敗を報告したらこの節を見る、と改められています — [日本語](https://code.claude.com/docs/ja/troubleshoot-install#release-verification-failed) / [English](https://code.claude.com/docs/en/troubleshoot-install#release-verification-failed)
- VTE 0.53 より古いライブラリの端末で、起動時に `>0q`、終了後に `>4m` が出る問題: v2.1.301 以降はそうした端末で 2 つの制御シーケンスを送りません（`troubleshooting` の新しい h3。`echo $VTE_VERSION` が `5300` 未満なら端末を更新する） — [日本語](https://code.claude.com/docs/ja/troubleshooting#stray-0q-at-startup-or-4m-after-exit) / [English](https://code.claude.com/docs/en/troubleshooting#stray-0q-at-startup-or-4m-after-exit)
- git のリポジトリから入れたプラグインが `Version: unknown` と出る問題: v2.1.302 以降はコミットを読める形で clone するので、`claude update`・`claude plugin marketplace update`・`claude plugin update` の順に実行します（`plugins/troubleshooting` の新しい h3） — [日本語](https://code.claude.com/docs/ja/plugins/troubleshooting#a-plugin-installed-from-a-git-repository-shows-version-unknown) / [English](https://code.claude.com/docs/en/plugins/troubleshooting#a-plugin-installed-from-a-git-repository-shows-version-unknown)
- v2.1.302 より前に、プロトコルの改訂 2026-07-28 のサーバーが `resultType`・`ttlMs`・`cacheScope` を返さないと `/mcp` が `tools fetch failed` を示した問題（`mcp-quickstart`）
- v2.1.302 より前に、git 2.56 以降で、保護されたチェックアウトのパスに迷子の `.git` ファイルがあると `could not be resolved` で終わった問題（`worktrees`）
- v2.1.305 より前に、`pipeline()` の項目か `parallel()` のタスクが 2 つ以上のエージェントを動かすスクリプトを編集せずに起動し直すと、終わったエージェントも動き直した問題（`workflows`）
- 拡張機能 2.1.304 より前に、`claudeProcessWrapper` を設定すると過去の会話が見つからなかった問題（`vs-code`）

**その他**

- **`llms-full.txt` の書式が MDX から Markdown に変わった**（詳細はハイライト 1 参照）
- **8 つの環境変数が `llms-full.txt` から消えた**: `CLAUDE_DISABLE_ADOPT`（`env-vars`・`agent-view`）、`CLAUDE_AFK_TIMEOUT_MS` と `CLAUDE_AFK_COUNTDOWN_MS`（`env-vars`・`settings-reference`。`askUserQuestionTimeout` の「セッションごとの上書き」の行と、未回答のダイアログのタイマーの変数の一覧からも外れた）、`CLAUDE_CODE_MAX_TOOL_USE_CONCURRENCY`（`env-vars`・`errors`）、`FALLBACK_FOR_ALL_PRIMARY_MODELS`、`CLAUDE_CODE_USE_NATIVE_FILE_SEARCH`、`CLAUDE_CODE_TEAM_TEARDOWN_PARK_TIMEOUT_MS`、`CLAUDE_CODE_DISABLE_ADMIN_ENV_UNION`（いずれも `env-vars`）です。changelog にはどれにも対応する項目がなく、廃止か説明の削除かは本文からは分かりません
- **カードのリンク先、Desktop のダウンロードのリンクなどが読めるようになった**: カードの変換で、`code-review`・`common-workflows`・`features-overview`・`how-claude-code-works`・`slack` などのカードのタイトルがリンクになり、`desktop`・`desktop-quickstart` のダウンロードのボタンもリンクになりました（書式の差なので本文の変更には数えていない）
- **見出しマップ**: 38 行が加わり 3 行が外れました。加わったのは 37 見出しと新しいスタンプです。そのうち 26 見出しは今回の `llms-full.txt` にも入った見出しで、残る 11 見出し（「Include other files in REVIEW.md」「Tool search through an LLM gateway」「Couldn't start the local listener that receives the browser sign-in」「Only a teammate can approve a shutdown request」「Matches no tool · check for typos」「Beta header and body field pairs」「Retry without tool search」「Bypass permissions ignored in a background session」「Denied paths that pass through a symlink」「Fork a complete project」「Recognize the StructuredOutput tool call」）は、今回の `llms-full.txt` にはまだ見出しがなく、本文の更新は今回の取り込みに入っていません。このうち「Couldn't start the local listener…」は、`errors` の「Failed to start OAuth callback server」の改称で（`llms-full.txt` は旧名のまま）、外れたのはこの旧名と、`agent-view` の「Set the model」（今回の `llms-full.txt` でも「Set the model, effort, and fast mode」に改称）と古いスタンプです。前回、見出しマップにだけ載っていた 23 見出し（`routines` 7・`permission-modes` 5・`plugins/mods/api` 4・`scheduled-tasks` 3 など）は、今回すべて `llms-full.txt` に入りました
- **見出しマップ冒頭の自動生成スタンプが、2026年10月20日 02時56分00秒 UTC から 2026年10月21日 05時26分28秒 UTC へ進みました**

**参考リンクについて**: 日本語版は、ハイライト・大幅更新・軽微な更新で取り上げたページのうち次の 35 ページ（`routines`・`desktop-scheduled-tasks`・`scheduled-tasks`・`agent-view`・`claude-projects`・`cloud-environments`・`permissions`・`plugins/mods/events`・`plugins/mods/reference`・`plugins/mods/admin`・`plugins/mods/api`・`plugins/mods/troubleshoot`・`permission-modes`・`env-vars`・`agent-sdk/permissions`・`hooks-guide`・`costs`・`vs-code`・`keybindings`・`errors`・`troubleshoot-install`・`agent-sdk/typescript`・`model-config`・`auto-mode-config`・`interactive-mode`・`claude-code-on-the-web`・`remote-control`・`code-review-pull-requests`・`plugins/troubleshooting`・`cross-session-messaging`・`checkpointing`・`troubleshooting`・`self-hosted-environments-configuration`・`plugins/mods/gallery`・`llm-gateway-protocol`）を取得し、該当する節があるかと今回の内容（新しい節や書き換えた文）になっているかを、計 45 項目について確かめました。今回も日本語版の追従が早く、確かめた節はすべてすでに今回の内容でした（`routines` の H1 は「スケジュールタスクで作業を自動化する」）。改称された見出しの id は、ページ内外のリンクが使う id で確かめ、確かめられなかった見出し（`routines` の「Create a scheduled task」、`scheduled-tasks` の改称した h2、`permission-modes` の「When your model doesn't review」）にはリンクを付けていません。取得して確かめていないページ（`artifacts`・`commands`・`skills`・`settings-reference`・`context-window`・`plugins/components`・`plugins/cli-reference`・`feature-availability`・`network-config`・`chrome`・`mcp`・`headless`・`sub-agents`・`tools-reference`・`plugins/mods/interface`・`monitoring-usage` など）と、版の注記だけが変わった項目にはリンクを付けていません。**changelog ページへのリンクは、本サマリの方針どおり付けていません。**

## 新着情報

**今回、新しい週のダイジェストはありません**（最新は前回と同じ Week 37）。`whats-new/` の 25 ページ（索引と週の 24 ページ）に差分がありますが、すべてハイライト 1 の書式の変換によるもので、内容は変わっていません。週のページは `<div>`・`<span>`・`<p>` で組まれていた部分が素の Markdown になり、24 ページすべてで「Other wins」の項目が区切りなく 1 行に連結されました。索引の 24 週の項は日付の範囲を失い、`**Week 37**` のような太字の行になっています。

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-10-19.md](./archives/latest/2026-10-19.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-10-19.md](./archives/latest-detail/2026-10-19.md)

<!--
base_commit: 6dff1bc5043031664bb7326db74d2fb009b92eca
head_commit: 9a810fc542230f7d1d5e0e958b239a460a6d260f
generated_at_full: 2026-10-21T15:26:19+09:00
-->
