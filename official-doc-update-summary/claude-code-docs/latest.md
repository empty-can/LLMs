---
対象期間: 2026年10月10日 〜 2026年10月11日
作成日: 2026-10-11
---

# Claude Code 公式ドキュメント更新サマリ

```markdown
**今回は、デスクトップアプリでローカルのセッションを止めて SSH の接続だけを配る構成、サンドボックスの自動許可のモードでも通常の権限の確認に回るコマンド、WorktreeCreate・WorktreeRemove のフックが動く場面の拡大、Agent SDK のタスクのメッセージの `run_id`、定期タスクの遅延の新しい説明が文書に加わりました。changelog に新しいリリースはありません**。新しいページはなく、ページ単位で数えると既存の 222 ページ中 16 ページが変わり、変更は 271 行（追加 221・削除 50）、大幅更新は 2 ページです。総行数は 120,807 行から 120,978 行に増えました。

主要なものを以下に挙げます。

1. デスクトップアプリで `disableDesktopLocalSessions`・`sshConfigs`・`sshHostAllowlist` を組み合わせ、ローカルのセッションを止めて決めたホストへの SSH のセッションだけにする手順が載った（Claude Desktop v1.37937.0 以降）
2. サンドボックスの自動許可のモードでも、`FOO=bar npm test`・`make CC=clang`・`eval "ls"` のようなコマンドは通常の権限の確認に回ること、それを止める allow ルールの書き方が載った
3. WorktreeCreate のフックが `EnterWorktree` ツール・ワークフロー・`claude remote-control` の `worktree` モードでも動くこと、WorktreeRemove のフックが `ExitWorktree` ツールと `claude remote-control` の後片付けでも動くことが明記された
4. Agent SDK（TypeScript）のタスクのメッセージに、同じ `task_id` のタスクの実行ごとに変わる `run_id` が加わった（v0.3.292 以降）
5. 定期タスクの遅延は次の実行までの間隔の半分まで（最大 30 分）と改められ、`*/5 * * * *` のタスクは遅らせずに前回の 4 分 45 秒後に動くと明記された
```

## ハイライト

1. [**デスクトップアプリでローカルのセッションを止めて SSH の接続だけを配る構成が載った**](./latest-detail.md#1-デスクトップアプリでローカルのセッションを止めて-ssh-の接続だけを配る構成が載った):  
  `desktop` に「Turn off local sessions and distribute SSH connections」の節ができました。`disableDesktopLocalSessions`・`sshConfigs`・`sshHostAllowlist` を 1 つの管理設定の出どころにまとめて配る例と、効く範囲（CLI・Cowork・クラウドのセッションには効かない）、確かめ方が載っています
2. [**サンドボックスの自動許可のモードでも通常の権限の確認に回るコマンドが明記された**](./latest-detail.md#2-サンドボックスの自動許可のモードでも通常の権限の確認に回るコマンドが明記された):  
  前に変数の代入を置いたコマンドや `make CC=clang`・`eval "ls"` は自動では承認されず、allow ルールと権限モードで決まります。`Bash(eval *)` のようなワイルドカードでは止まらない点や、一致する allow ルールはサンドボックスの外での再試行も承認する点も加わりました
3. [**WorktreeCreate と WorktreeRemove のフックが動く場面が広がった**](./latest-detail.md#3-worktreecreate-と-worktreeremove-のフックが動く場面が広がった):  
  WorktreeCreate は `EnterWorktree` ツール・ワークフローのエージェント・`claude remote-control` の `worktree` モードでも動き、WorktreeRemove は `ExitWorktree` ツールと `claude remote-control` の後片付けでも動きます。Bash の `git worktree add` ではフックが動かないことも明記されました
4. [**Agent SDK のタスクのメッセージに実行ごとの run_id が加わった**](./latest-detail.md#4-agent-sdk-のタスクのメッセージに実行ごとの-run_id-が加わった):  
  再開されたサブエージェントのように同じ `task_id` で何度も動くタスクを実行ごとに見分ける `run_id` が、`task_started`・`task_progress`・`task_updated`・`task_notification` と `background_tasks_changed` の各項目に、通知を届けるユーザーメッセージの origin には `runId` として載ります（v0.3.292 以降）
5. [**定期タスクの遅延の説明が改められ 5 分ごとのタスクの扱いが加わった**](./latest-detail.md#5-定期タスクの遅延の説明が改められ-5-分ごとのタスクの扱いが加わった):  
  定期タスクの各実行は、次の実行までの間隔の半分まで、最大 30 分遅れます。間隔が不揃いなら実行ごとに遅れが変わり、`*/5 * * * *`（`/loop 5m` が作るもの）は遅らせずに前回の 4 分 45 秒後に動きます

## 新規追加されたページ

（今回の対象期間に新規追加・削除されたドキュメントページはありません。`llms.txt` は変わらず、収録 URL は 233 のままです。`llms-full.txt` に展開されている固有のページも 222 のままで、`Source:` の行が 230 あり 8 ページが 2 回展開されている状態も前回と同じです）

## 大幅に更新されたページ

- [**Debug your configuration**](./latest-detail.md#1-debug-your-configuration) ([日本語](https://code.claude.com/docs/ja/debug-your-config#test-against-a-clean-configuration) / [English](https://code.claude.com/docs/en/debug-your-config#test-against-a-clean-configuration)):  
  66 行（追加 54・削除 12）が変わりました。「Test against a clean configuration」が 3 つの手順に組み直され、`--setting-sources user` でプロジェクトの設定を止める方法と PowerShell での手順が加わりました
- [**Desktop application**](./latest-detail.md#2-desktop-application) ([日本語](https://code.claude.com/docs/ja/desktop#turn-off-local-sessions-and-distribute-ssh-connections) / [English](https://code.claude.com/docs/en/desktop#turn-off-local-sessions-and-distribute-ssh-connections)):  
  51 行（追加 51・削除 0）が変わりました。ローカルのセッションを止めて SSH の接続を配る節ができ、`sshHost` に `user@` を書かないときの接続ユーザーが加わりました（詳細はハイライト 1）

## 軽微な更新

今回の差分は **2 ファイル**（`llms-full.txt`・見出しマップ）で、`llms.txt` は変わっていません。**changelog は変わっておらず新しいリリースはない**ので、以下はすべて通常のページの文書の変更で、changelog 由来の項目はありません（そのため「バグ修正」の分類はありません）。`llms-full.txt` の生の差分は追加 217 行・削除 46 行で、ページ単位に切り出して数えると、既存の 222 ページ中 **16 ページ**が変わり、変更は 271 行（追加 221・削除 50）でした。大幅更新の 2 ページ（`debug-your-config`・`desktop`）を除く **14 ページ**を以下にまとめます（ハイライトで扱ったものは一言で示します）。`llms-full.txt` の総行数は **120,807 行から 120,978 行へ 171 行増え**ました。`Source:` の行は 230、固有のページは 222 のままです。

**新機能**

- **mod のフックに `prompt.autocomplete` のイベントが加わった**（`plugins/mods/reference` の「Prompts and what Claude reads」）。利用者が入力欄に打ち込み、カーソルの位置で語が終わると動き、`e.token` がその語です。Claude Code はフックを待たず、自分の補完の行を先に出します。フックは `{ text, label, description }` の行の一覧の `{ suggestions }` を返し、それらは Claude Code 自身の行の下に出ます。行を選ぶとその `text` が語を上書きします — [日本語](https://code.claude.com/docs/ja/plugins/mods/reference#prompts-and-what-claude-reads) / [English](https://code.claude.com/docs/en/plugins/mods/reference#prompts-and-what-claude-reads)

**機能改善**

- **サンドボックスの自動許可のモードの例外への案内が加わった**（`permission-modes` の「Common setups」・`permissions` の「How permissions interact with sandboxing」・`settings-reference` の `sandbox.autoAllowBashIfSandboxed`。詳細はハイライト 2 参照） — [日本語](https://code.claude.com/docs/ja/permissions#how-permissions-interact-with-sandboxing) / [English](https://code.claude.com/docs/en/permissions#how-permissions-interact-with-sandboxing)
- **`claude remote-control` の `--spawn worktree` が WorktreeCreate のフックでも使えると明記された**（`remote-control` の「Start a Remote Control session」。詳細はハイライト 3 参照） — [日本語](https://code.claude.com/docs/ja/remote-control#start-a-remote-control-session) / [English](https://code.claude.com/docs/en/remote-control#start-a-remote-control-session)
- **サブエージェントの worktree の説明に WorktreeRemove への案内が加わった**（`worktrees` の「Isolate subagents with worktrees」。詳細はハイライト 3 参照） — [日本語](https://code.claude.com/docs/ja/worktrees#isolate-subagents-with-worktrees) / [English](https://code.claude.com/docs/en/worktrees#isolate-subagents-with-worktrees)
- **期限切れの Anthropic のプロファイルのログインの、新しいメッセージの形と対処が載った**（`errors` の「Anthropic profile login expired」）。Claude Code が構成のディレクトリから見つけた認証モード `user_oauth` のプロファイルでは、メッセージが `Login expired · Run /login to sign in again, or re-authenticate your Anthropic profile` になり、`/login` を先に勧めます（その場合 Claude Code は動く `/login` を見つけたプロファイルより優先し、claude.ai のアカウントで認証する）。v2.1.234 から v2.1.277 まではこの形が `Anthropic profile login expired · Run /login to use your claude.ai account instead, or re-authenticate the profile` でした。`ANTHROPIC_PROFILE` で選んだプロファイルでは `Anthropic profile login expired` で始まります。対処も、`Login expired` で始まるなら `/login` で再びサインインする、キーなしの Console のサインインか Claude Platform CLI の `ant auth login` が書いたプロファイルは `/login` で Anthropic Console のアカウントを選んで **Sign in with your Console account** を選ぶ、ほかのツールが作ったプロファイルはそのツールでサインインし直す（`/login` で **Sign in with your Console account** を選ぶとプロファイルはそのままで API キーが作られる）、と分けて書かれました。「Find your error」の表に新しい形の行が、「Login expired」の節にこの形の案内が加わり、`authentication` の 2 か所のリンクの文言も「expired profile login error」に改められています — [日本語](https://code.claude.com/docs/ja/errors#anthropic-profile-login-expired) / [English](https://code.claude.com/docs/en/errors#anthropic-profile-login-expired)
- **設定ファイルで宣言したマーケットプレイスが公式の名前をまねて断られたときの手順が載った**（`errors` の「Claude Code refuses the marketplace name」）。設定ファイルが `"source": "settings"` でその場で宣言したマーケットプレイスを残すには、古い名前を消す前に名前を変えます。マーケットプレイスを消すと設定ファイルからその項目も消えるためで、Claude Code v2.1.292 以降はメッセージにこの手順が出ます。手順は、`extraKnownMarketplaces` に載せた各設定ファイルで項目のキーと `source.name` を公式に見えない 1 つの新しい ASCII の名前にする（組織の管理設定が加えたものは管理者が行う）、`claude plugin marketplace remove <old-name>` か `/plugin` の **Marketplaces** タブで古い名前を消す、Claude Code を起動し直して（プロジェクトの設定ファイルならそのフォルダーで）名前を変えたマーケットプレイスからプラグインを入れ直す、の 3 つです。消すとプラグインのデータに加えて選択肢とシークレットも消える、とも改められ、`plugins/marketplace-reference` の「Reserved names」にも同じ案内が加わりました — [日本語](https://code.claude.com/docs/ja/errors#claude-code-refuses-the-marketplace-name) / [English](https://code.claude.com/docs/en/errors#claude-code-refuses-the-marketplace-name)
- **ワークフローの再開の説明が 2 つの小見出しに分かれ、スクリプトの順序を変えたときの例が加わった**（`workflows` の「Resume after a pause」）。「Which agents run again」と「Resume after you leave the session」の小見出しができ、A・B・C・D の順に始めるスクリプトを A・C・B・D の順に変えると、2 番目に始まるのが前回の B ではなく C になるので、再起動すると A はキャッシュから返り、C・B・D がもう一度動く、という例が加わりました — [日本語](https://code.claude.com/docs/ja/workflows#which-agents-run-again) / [English](https://code.claude.com/docs/en/workflows#which-agents-run-again)

**その他**

- **言い回しの調整**: `agent-sdk/typescript` の「Tool Input Types」「Tool Output Types」の説明が「すべての組み込みのツール」から「組み込みのツール」に改められました
- **見出しマップ**: 4 行が加わり 1 行が外れました。加わったのは自動生成のスタンプ 1 行と、既存ページの 3 つの見出し（`desktop` の「Turn off local sessions and distribute SSH connections」、`workflows` の「Which agents run again」「Resume after you leave the session」）で、外れたのはスタンプの古い行だけです
- **見出しマップ冒頭の自動生成スタンプが、2026年10月11日 03時17分49秒 UTC から 2026年10月11日 19時46分55秒 UTC へ進みました**

**参考リンクについて**: 日本語版は、変更のあった 16 ページをすべて取得して、リンクを付けた節の id と今回の内容（新しい節や書き換えた文）があるかを確かめました。今回も日本語版の追従が早く、`desktop`・`sandboxing`・`hooks`・`agent-sdk/typescript`・`scheduled-tasks`・`debug-your-config` をはじめ、16 ページすべての該当の節がすでに今回の内容になっていたため、すべて日本語版のリンクを付けています。**changelog ページへのリンクは、本サマリの方針どおり付けていません。**

## 新着情報

**今回、`whats-new/` 配下のページに変更はありません。**

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-10-10.md](./archives/latest/2026-10-10.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-10-10.md](./archives/latest-detail/2026-10-10.md)

<!--
base_commit: 096d54cbb316fc19ca321240fcef28dc6ea22401
head_commit: 98d1f105aec298de4131f50d6044a9d5ea41da93
generated_at_full: 2026-10-12T15:05:25+09:00
-->
