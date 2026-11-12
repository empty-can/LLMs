---
対象期間: 2026年11月10日 〜 2026年11月11日
作成日: 2026-11-11
---

# Claude Code 公式ドキュメント更新サマリ

```markdown
**今回は、Desktop で SSH と WSL のセッションの HTML プレビューのスクリプトだけを止める managed setting `disableRemotePreviewScripts` が載り、Claude Desktop のポリシーで個人の API キーや Console アカウントでの利用を止める方法と、thinking を切れないモデルとプロバイダーごとの止め方が整理されました**。新しいページ・大幅更新のページ・changelog の新しいリリースはなく、`llms.txt` も変わっていません。`llms-full.txt` では 203 ページのうち 24 ページが変わり、変更は 173 行（追加 126・削除 47）で、総行数は 127,144 行から 127,223 行に増えました。

主要なものを以下に挙げます。

1. Desktop で、SSH と WSL のセッションの HTML プレビューのスクリプトだけを止める managed setting `disableRemotePreviewScripts`（Claude Desktop v5.1231.0 以降）が載った。これまでの `disableBrowserExternalNavigation` と違い、外部のサイトの閲覧は止めない
2. Claude Code の managed settings の `forceLoginOrgUUID` だけでは、個人の Claude API キーや Claude Console のアカウントでの Claude Desktop の利用は止まらず、Claude Desktop のポリシーにも配る必要があると載った
3. thinking を切れない場所を述べる h4 ができ、Anthropic API ではモデルを ID で指定し、サードパーティのプロバイダーでは effort を下げる、とプロバイダーごとの止め方が整理された
4. `/claude-api` に、Claude API のコードで人を待たせている箇所を見つけて改善を提案する `latency-optimize`（v2.1.319 以降）が載った
5. セルフホストのランナーで、ブランチが見つからないときのエラーの項目が新しいメッセージに合わせて書き直され、モデルへのアクセスの更新を断られたときの警告を止める `CLAUDE_RUNNER_DISABLE_RENEWAL_WARNING` が載った
```

## ハイライト

1. [**SSH と WSL のプレビューのスクリプトだけを止める disableRemotePreviewScripts が載った**](./latest-detail.md#1-ssh-と-wsl-のプレビューのスクリプトだけを止める-disableremotepreviewscripts-が載った):  
  `desktop` の「Turn off scripts in SSH and WSL previews for your organization」で、プレビューのスクリプトを止めるキーが `disableBrowserExternalNavigation` から新しい managed setting の `disableRemotePreviewScripts` に替わりました。利用者は外部のサイトを引き続き閲覧でき、Claude Desktop v5.1231.0 以降が要ります。スクリプトがまだ動くコンピューターを確かめる h5 ができ、`settings-reference` にもこのキーの h3 ができました
2. [**Claude Desktop のポリシーで個人の API キーと Console アカウントの利用を止められると載った**](./latest-detail.md#2-claude-desktop-のポリシーで個人の-api-キーと-console-アカウントの利用を止められると載った):  
  `desktop` の「Restrict sign-in to your organization」に、Claude Code の managed settings の `forceLoginMethod` と `forceLoginOrgUUID` を設定しても、利用者は自分の Claude API キーか Claude Console のアカウントで Code タブのセッションを動かせる、と加わりました。止めるには Claude Desktop のポリシーにも `forceLoginOrgUUID` を配ります
3. [**thinking を切れないモデルとプロバイダーごとの止め方が整理された**](./latest-detail.md#3-thinking-を切れないモデルとプロバイダーごとの止め方が整理された):  
  `model-config` の「Extended thinking」に h4「Where you can't turn thinking off」ができました。Anthropic API では `claude-opus-5`・`claude-sonnet-5`・`claude-haiku-4-5` のようなモデルで thinking を切れ、エイリアスは切れないモデルを選ぶのでモデルを ID で指定します。サードパーティのプロバイダーでは effort を下げます。Agent SDK の `ThinkingConfig` の `disabled` もこの h4 にリンクしました
4. [**/claude-api に latency-optimize のサブコマンドが載った**](./latest-detail.md#4-claude-api-に-latency-optimize-のサブコマンドが載った):  
  `skills` の「Work on Claude API projects」の表と `commands` の `/claude-api` の行に、`latency-optimize` が加わりました。既存の Claude API のコードで時間がかかっている箇所を見つけ、人が待つ時間を減らす変更を提案します（v2.1.319 以降）
5. [**セルフホストのランナーのブランチが見つからないときのエラーが改められた**](./latest-detail.md#5-セルフホストのランナーのブランチが見つからないときのエラーが改められた):  
  `self-hosted-environments-deploy` のトラブルシューティングの項目が、v2.1.314 からのメッセージ `couldn't be found in the remote repository` に合わせて書き直され、一度も push していないブランチの直し方も載りました。`self-hosted-environments-reference` には、モデルへのアクセスの更新を断られたときの警告を止める `CLAUDE_RUNNER_DISABLE_RENEWAL_WARNING`（v2.1.319 以降）が加わりました

## 新規追加されたページ

（今回の対象期間に新規追加されたドキュメントページはありません。`llms.txt` は変わらず、URL は 239 のままです。`llms-full.txt` の `Source:` の行も 206、固有のページも 203 のままです）

## 大幅に更新されたページ

（今回の対象期間に、単一ページで 50 行以上の大幅更新に該当したページはありません。主要な更新はハイライト、その他はいずれも下記「軽微な更新」に整理しています）

## 軽微な更新

今回の差分は **2 ファイル**（`llms-full.txt`・見出しマップ）で、`llms.txt` は変わっていません。changelog に新しいリリースはなく（収録は 439 のままで、先頭は v2.1.322）、changelog のページも変わっていません。`llms-full.txt` では、203 ページのうち **24 ページ**が変わり、変更は 173 行（追加 126・削除 47）です。どのページも 50 行未満なので、すべてを以下にまとめます。今回の変更には、v2.1.314〜v2.1.319 の changelog の項目に対応するものがあります。

`llms-full.txt` の総行数は **127,144 行から 127,223 行へ 79 行増え**ました（生の差分の差し引き 126 − 47 と一致）。コードフェンスの外の見出しは、引用の中の見出しも数えると 6,078 から 6,082 へ、行頭が `#` の見出しだけを数えると 6,067 から 6,071 へ、どちらも 4 増えました。加わったのは `desktop` の h5「Check a computer for scripts that still run」、`plugins/mods/test` の h3「Check a result with `expect`」、`model-config` の h4「Where you can't turn thinking off」、`settings-reference` の h3「`disableRemotePreviewScripts`」で、外れた見出しも改称された見出しもありません。

**新機能**

- SSH と WSL のプレビューのスクリプトだけを止める `disableRemotePreviewScripts`（`desktop`・`settings-reference`。詳細はハイライト 1 参照）
- `/claude-api` の `latency-optimize` のサブコマンド（`skills`・`commands`。詳細はハイライト 4 参照）
- セルフホストのランナーの、モデルへのアクセスの更新を断られたときの警告を止める `CLAUDE_RUNNER_DISABLE_RENEWAL_WARNING`（`self-hosted-environments-reference`。詳細はハイライト 5 参照）

**機能改善**

- Claude Desktop のポリシーの `forceLoginOrgUUID` で、個人の API キーと Console アカウントでの利用を止める方法（`desktop`。詳細はハイライト 2 参照）
- thinking を切れないモデルと、プロバイダーごとの止め方（`model-config`・`agent-sdk/python`・`agent-sdk/typescript`・`agent-sdk/agent-loop`。詳細はハイライト 3 参照）
- セルフホストのランナーのブランチが見つからないときのエラー（`self-hosted-environments-deploy`・`self-hosted-environments-configuration`。詳細はハイライト 5 参照）
- **mod のテストキットの `expect` のアサーションが一覧になった**（`plugins/mods/test` の新しい h3「Check a result with `expect`」）。これまで 8 つ（`toBe`・`toEqual`・`toMatch`・`toMatchObject`・`toContain`・`toBeDefined`・`toBeUndefined`・`toThrow`）を挙げていた 1 文が、等しさ・テキスト・数値・中身・有無と型・例外の 6 つに分けた 23 のアサーションの一覧になりました。新たに挙がったのは `toStrictEqual`、`toStartWith`・`toEndWith`、`toBeGreaterThan`・`toBeGreaterThanOrEqual`・`toBeLessThan`・`toBeLessThanOrEqual`、`toContainEqual`・`toHaveLength`・`toHaveProperty`、`toBeNull`・`toBeTruthy`・`toBeFalsy`・`toBeNaN`・`toBeInstanceOf` の 15 です。アサーションは調べる値の後に置き（例: `expect(answer.text).toBe('ok')`）、前に `.not` を付けると反対を、`.resolves` か `.rejects` を付けると promise が落ち着く値を調べます。`toMatch` は正規表現か部分文字列を取り、`toThrow` は `expect` が呼ぶ関数か、`.rejects` で調べる promise に使います — [日本語](https://code.claude.com/docs/ja/plugins/mods/test#check-a-result-with-expect) / [English](https://code.claude.com/docs/en/plugins/mods/test#check-a-result-with-expect)
- **VS Code の拡張機能のコマンドの表に、音声入力の `claude-vscode.toggleDictation` が載った**（`vs-code` の「VS Code commands and shortcuts」）。`Cmd+D`（Mac）か `Ctrl+D`（Windows/Linux）で音声入力を始めるか止めます。ショートカットは Claude にフォーカスがあるときに働き、このコマンドはコマンドパレットにはありません。コマンドパレットで「Claude Code」と打つと出るものの説明も、拡張機能で使えるすべての VS Code のコマンド、から、拡張機能のコマンドパレットのコマンド、に改められました — [日本語](https://code.claude.com/docs/ja/vs-code#vs-code-commands-and-shortcuts) / [English](https://code.claude.com/docs/en/vs-code#vs-code-commands-and-shortcuts)
- **`CLAUDE_CODE_DISABLE_CRON` を設定しても、スケジュールしたタスクの一覧と取り消しはできると載った**（`scheduled-tasks` の「Disable session-scoped scheduled tasks」・`env-vars`）。使えなくなるのは `CronCreate` と `/loop` で、プロジェクトの `.claude/scheduled_tasks.json` にタスクがある間は `CronList` と `CronDelete` が使えるままなので、Claude にタスクの一覧や取り消しを頼めます。これまでは、cron のツールと `/loop` が使えなくなる、としていました。`env-vars` のこの変数の行も、「cron のツール」が `CronCreate` に改められ、リンク先がこの節になりました — [日本語](https://code.claude.com/docs/ja/scheduled-tasks#disable-scheduled-tasks) / [English](https://code.claude.com/docs/en/scheduled-tasks#disable-scheduled-tasks)

**バグ修正**

- **VS Code で plan モードのときに中断したステップの、再読み込みの後の通知と続け方が載った**（`vs-code` の「Interrupted steps after a reload」）。チャットの通知に `plan mode is now off, so Claude did not continue on its own` が含まれるときは、plan モードで中断したステップです。計画を続けるには、次のメッセージを送る前にモードの表示で **Plan** を選びます。changelog の v2.1.319 の、ウィンドウの再読み込みの後に Claude が承認していない計画を実行していた問題の修正（plan モードで中断したステップは、セッションが別の権限モードで戻ると通知を出して止まる。2026年11月06日 版のサマリで扱ったもの）に対応します — [日本語](https://code.claude.com/docs/ja/vs-code#interrupted-steps-after-a-reload) / [English](https://code.claude.com/docs/en/vs-code#interrupted-steps-after-a-reload)
- **Windows では scratchpad のディレクトリーの `<project>` がハッシュになると載った**（`claude-directory` の「Session scratchpad directory」）。`<project>` は作業ディレクトリーのパスの英数字以外を `-` にした文字列ですが、Windows ではその文字列の 16 文字のハッシュ（例: `73295dabccd14c56`）です。Desktop アプリのセッションでは文字列そのものの場合もあり、正確なパスは Claude に尋ねます。changelog の v2.1.317 の、Claude Desktop が始めていないセッションで scratchpad などの一時パスがプロジェクトのパスの長さとともに伸びていた問題の修正（2026年11月02日 版のサマリで扱ったもの）に対応します — [日本語](https://code.claude.com/docs/ja/claude-directory#session-scratchpad-directory) / [English](https://code.claude.com/docs/en/claude-directory#session-scratchpad-directory)

**その他**

- **Claude in Chrome のショートカットの操作が外れた**（`chrome` の「Browser tools in plan mode」）。plan モードで許可の確認が出る操作は、GIF の記録と新しいタブを開くことの 2 つになり、ショートカットの実行が外れました。changelog の v2.1.319 の、組み込みの Claude in Chrome のツールから `shortcuts_list` と `shortcuts_execute` を削除した変更（2026年11月06日 版のサマリで扱ったもの）に対応します — [日本語](https://code.claude.com/docs/ja/chrome#browser-tools-in-plan-mode) / [English](https://code.claude.com/docs/en/chrome#browser-tools-in-plan-mode)
- **`model-config` の h4「Fix a mistyped model name」が移った**: 2026年11月09日 版のサマリで新しい h4 として扱ったこの節が、自動コンパクトの「Correct the window for a gateway or custom model ID」の後ろから、「Setting your model」の中（「Set a default model for new sessions」の前）に移りました。文面は同じです。「Setting your model」の、Anthropic API ではモデル名かエイリアスに近い値で起動時の警告が出ることがある、という文も、最も近い名前を提案する警告が出ることがある、という言い方に改められています
- **auto モードの分類器がツールの結果を受け取らない、という説明の文が外れた**: `glossary` の「Auto mode」から、ツールの結果は分類器が見るものから除かれるので、ファイルやウェブページの悪意のある内容が分類器を直接操れない、という文が外れ、「Prompt injection」は、auto モードはツールの結果を調べるサーバー側のプローブと、ツールの結果を除いて操作を審査する分類器を加える（注入されたテキストが分類器を直接操れない）、から、auto モードではサーバー側のプローブがツールの結果を調べ、分類器が操作を審査する、に改められました。`hooks` の「Annotate a result for the auto mode classifier」では、分類器はツールの結果そのものを受け取らないので `classifierContext` が呼び出しの返したものを伝える方法だ、という文が、メモは分類器が後の操作を審査するためのもの、に替わりました。`permission-modes` の「What the classifier blocks by default」でも、値は分類器が受け取らない前のコマンドの出力からしか来ない、という説明が、その代入がなければ分類器は何を消すか分からない、に替わり、段落が分けられています。挙動の変更を述べる記述はなく、`permission-modes` には、Claude Code 自身が送る分類器の要求からはツールの結果が除かれる、という説明が残っています
- **ほかに外れた文**: `context-window` の「What survives compaction」（v2.1.198 から要約の要求はセッションの extended thinking の設定を引き継ぎ、thinking は要約の作り方にだけ効く、という文と、表への導入の文）、`common-workflows` の「Run parallel sessions with worktrees」（コミットのないリポジトリでは `Failed to resolve base branch "HEAD": git rev-parse failed` で失敗する）、`errors` の「Couldn't send feedback」（メッセージに `To report a bug, open an issue` が付いていれば GitHub の issue で報告する）と「Two Claude Code config files exist」（古い版は移した `.config.json` を書き戻すことがある）
- **字句の小さな修正**: `tools-reference`（フォアグラウンドで始まりバックグラウンドに移るコマンドの説明から「たとえば」が外れ、タイムアウトで移るコマンドの説明になった）、`settings-reference`（`permissions.denyInsteadOfPrompting` が止めるものの、分類器の課金の通知へのリンク先が節からページに）、`glossary`（「Prompt injection」の「never asked for」が「didn't ask for」に）

## 新着情報

（今回の差分に新着情報（`whats-new/`）のページはありません。前回 `llms.txt`・`llms-full.txt`・見出しマップから外れた whats-new の 25 ページは、今回も戻っていません）

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-11-10.md](./archives/latest/2026-11-10.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-11-10.md](./archives/latest-detail/2026-11-10.md)

<!--
base_commit: 5ed60081bc6921a82747ac292a0c99583f7521e4
head_commit: c85f1a228a539e3f1157cb0caf9aea01e5add4d1
generated_at_full: 2026-11-12T15:07:08+09:00
-->
