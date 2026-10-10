---
対象期間: 2026年10月08日 〜 2026年10月09日
作成日: 2026-10-09
---

# Claude Code 公式ドキュメント更新サマリ

```markdown
**今回は、失敗したフックで操作を止める `onFailure`、Claude apps gateway のポリシーの `code` キー、セルフホストの Anthropic git proxy の対応範囲と手順、mod の `$.model.complete` のプロンプトキャッシュ、Agent SDK の `/usage` の構造化された報告が文書に加わりました。changelog には v2.1.296（79 項目）が積まれています**。新しいページはなく、ページ単位で数えると 221 ページ中 58 ページ（changelog を含む）が変わり、changelog を除く変更は 1,584 行（追加 1,290・削除 294）、9 ページが大幅更新です。総行数は 119,210 行から 120,369 行に増えました。

主要なものを以下に挙げます。

1. command と HTTP のフックに `"onFailure": "block"` を付けると、起動できない・時間切れなどで失敗したフックが操作を止めるようになり、終了コードと標準出力の組み合わせが表になった（v2.1.295 以降）
2. Claude apps gateway のポリシーの設定を `cli` ではなく `code` キーの下に置くと、条件を満たせばデスクトップアプリの Code タブにも届く（ゲートウェイに v2.1.296 以降が要る）
3. セルフホストの Anthropic git proxy は github.com のリポジトリだけを扱い、ランナーのユーザーのグローバルな git の設定を置き換えると明記され、オン・オフの手順と起動失敗の見分け方が加わった
4. mod の `$.model.complete` に `{ text, cache: true }` のブロックの配列を渡して、プロンプトキャッシュの区切りを置けるようになった（v2.1.292 以降）
5. Agent SDK で `/usage` を送ると、その報告が `SDKUsageReport` 型の `usage_report` としてメッセージに付くようになった（v0.3.273 以降）
```

## ハイライト

1. [**フックが失敗したときに操作を止める onFailure の節ができた**](./latest-detail.md#1-フックが失敗したときに操作を止める-onfailure-の節ができた):  
  command と HTTP のフックに `"onFailure": "block"` を付けると、起動できない・時間切れ・0 と 2 以外の終了コード・不正な出力で失敗したフックが操作を止めます（v2.1.295 以降）。「Exit code output」も標準出力と終了コードの組み合わせの表に書き直されました
2. [**Claude apps gateway の code キーでデスクトップの Code タブにも設定が届くようになった**](./latest-detail.md#2-claude-apps-gateway-の-code-キーでデスクトップの-code-タブにも設定が届くようになった):  
  ポリシーの Claude Code の設定を推奨の `code` キーの下に置くと、デスクトップアプリ 2.9939.2 以降などの条件を満たせば Code タブにも効きます。ゲートウェイには v2.1.296 以降が要り、`cli` と混ぜると起動しません
3. [**セルフホストの Anthropic git proxy の対応範囲と設定手順が全面的に書き直された**](./latest-detail.md#3-セルフホストの-anthropic-git-proxy-の対応範囲と設定手順が全面的に書き直された):  
  git proxy は github.com のリポジトリだけを扱い、ランナーのユーザーのグローバルな git の設定をバックアップなしに置き換えると明記されました。オン・オフの手順と、セッションが始まらないときの見分け方が加わっています
4. [**mod の $.model.complete でプロンプトキャッシュを使えるようになった**](./latest-detail.md#4-mod-の-modelcomplete-でプロンプトキャッシュを使えるようになった):  
  `prompt` か `system` を `{ text }` のブロックの配列で渡し、静的な内容の最後のブロックに `cache: true` を付けると区切りになります（v2.1.292 以降）。`$.model.fork` との違いの表と、キャッシュに当たったかの確かめ方も載りました
5. [**Agent SDK で /usage の報告を構造化して受け取れるようになった**](./latest-detail.md#5-agent-sdk-で-usage-の報告を構造化して受け取れるようになった):  
  claude.ai の資格情報のセッションで `/usage` を送ると、アシスタントのメッセージに `SDKUsageReport` 型の `usage_report` が付き、費用の累計とプランの使用量の行を読めます（Agent SDK v0.3.273 以降）

## 新規追加されたページ

（今回の対象期間に新規追加・削除されたドキュメントページはありません。`llms.txt` は変わらず、収録 URL は 232 のままです。`llms-full.txt` に展開されている固有のページも 221 のままで、`Source:` の行が 229 あり 8 ページが 2 回展開されている状態も前回と同じです）

## 大幅に更新されたページ

- [**Troubleshoot installation and login**](./latest-detail.md#1-troubleshoot-installation-and-login) ([日本語](https://code.claude.com/docs/ja/troubleshoot-install#verify-your-path) / [English](https://code.claude.com/docs/en/troubleshoot-install#verify-your-path)):  
  180 行（追加 167・削除 13）が変わりました。PATH の確かめ方が書き足され、エラーの早見表に 9 行が加わり、`errors` からインストールのエラーの 2 節が移ってきました
- [**Deploy self-hosted environments to production**](./latest-detail.md#2-deploy-self-hosted-environments-to-production) ([日本語](https://code.claude.com/docs/ja/self-hosted-environments-deploy#harden-your-deployment) / [English](https://code.claude.com/docs/en/self-hosted-environments-deploy#harden-your-deployment)):  
  143 行（追加 125・削除 18）が変わりました。大半は git proxy（ハイライト 3）で、ほかにホストの GitHub の資格情報の扱い、IP の許可リスト、オンデマンドのランナーの更新のしかたなどが改められました
- [**Customize sessions in self-hosted environments**](./latest-detail.md#3-customize-sessions-in-self-hosted-environments) ([日本語](https://code.claude.com/docs/ja/self-hosted-environments-configuration#keep-transient-failures-retryable-in-a-shell-hook) / [English](https://code.claude.com/docs/en/self-hosted-environments-configuration#keep-transient-failures-retryable-in-a-shell-hook)):  
  142 行（追加 117・削除 25）が変わりました。Slack のスレッドの環境変数、`spawn-runner` のフックで一時的な失敗を再試行可能に保つ書き方、最初のターンの前の MCP サーバーの待ち方などが加わりました
- [**Hooks reference**](./latest-detail.md#4-hooks-reference) ([日本語](https://code.claude.com/docs/ja/hooks#exit-code-output) / [English](https://code.claude.com/docs/en/hooks#exit-code-output)):  
  130 行（追加 103・削除 27）が変わりました。ほぼすべてがハイライト 1 の `onFailure` と終了コードの説明の書き直しです
- [**Agent SDK reference - TypeScript**](./latest-detail.md#5-agent-sdk-reference---typescript) ([日本語](https://code.claude.com/docs/ja/agent-sdk/typescript#sdktasknotificationmessage) / [English](https://code.claude.com/docs/en/agent-sdk/typescript#sdktasknotificationmessage)):  
  110 行（追加 100・削除 10）が変わりました。`SDKUsageReport`（ハイライト 5）のほか、タスクの通知の `reason`、貼り付けの項目の上限などが加わりました
- [**Error reference**](./latest-detail.md#6-error-reference) ([日本語](https://code.claude.com/docs/ja/errors#claude-code-couldnt-restart) / [English](https://code.claude.com/docs/en/errors#claude-code-couldnt-restart)):  
  102 行（追加 48・削除 54）が変わりました。インストールのエラーの節を `troubleshoot-install` へ移し、再起動の失敗と `/loop` の wakeup の取りこぼしの節が加わりました
- [**Use the mods API**](./latest-detail.md#7-use-the-mods-api) ([日本語](https://code.claude.com/docs/ja/plugins/mods/api#what-a-model-complete-hook-receives) / [English](https://code.claude.com/docs/en/plugins/mods/api#what-a-model-complete-hook-receives)):  
  91 行（追加 86・削除 5）が変わりました。すべて「Call a model」の書き直し（ハイライト 4）です
- [**Claude apps gateway configuration**](./latest-detail.md#8-claude-apps-gateway-configuration) ([日本語](https://code.claude.com/docs/ja/claude-apps-gateway-config#group-changes-during-an-open-session) / [English](https://code.claude.com/docs/en/claude-apps-gateway-config#group-changes-during-an-open-session)):  
  80 行（追加 75・削除 5）が変わりました。`code` キー（ハイライト 2）のほか、開いたセッションの間にグループが変わったときのテレメトリーの節が加わりました
- [**Troubleshoot plugins**](./latest-detail.md#9-troubleshoot-plugins) ([日本語](https://code.claude.com/docs/ja/plugins/troubleshooting#plugin-directory-does-not-exist) / [English](https://code.claude.com/docs/en/plugins/troubleshooting#plugin-directory-does-not-exist)):  
  64 行（追加 63・削除 1）が変わりました。マーケットプレイスの名前、読み込まれない設定ファイル、Windows でのアンインストール、`Plugin directory does not exist` の 4 節が加わりました

## 軽微な更新

今回の差分は **2 ファイル**（`llms-full.txt` と見出しマップ）で、`llms.txt` は変わっていません。`llms-full.txt` の生の差分は追加 1,458 行・削除 299 行で、ページ単位に切り出して数えると 221 ページ中 **58 ページ**が変わり、変更は 1,677 行（追加 1,383・削除 294）、うち changelog が 93 行、ほかのページが 1,584 行（追加 1,290・削除 294）でした。生の差分との差（追加 75・削除 5）は、2 回展開されている `plugins/troubleshooting`・`plugins/create`・`plugins/install` の変更が 2 度数えられたぶんです。大幅更新の 9 ページを除く **49 ページ**（changelog を含む）と、changelog に加わった **v2.1.296**（2026年10月09日、79 項目。Added 8・Changed 6・Improved 9・Fixed 56）を以下にまとめます。changelog の項目はすべて v2.1.296 のものです。`llms-full.txt` の総行数は **119,210 行から 120,369 行へ 1,159 行増え**ました（changelog の 93 行、ほかのページの 996 行、2 回展開された 3 ページの重複の 70 行）。

**新機能**

- Claude apps gateway の `managed.policies[]` に `code` キーを追加（詳細はハイライト 2 参照）
- サブエージェントの frontmatter と `--agents` の定義に `autoCompactWindow` を追加。サブエージェントが本体の会話のウィンドウより早く自動圧縮できます
- `CLAUDE_CODE_WORKFLOW_SUBAGENT_MODEL` を追加。ほかのサブエージェントのモデルはそのままで、すべてのワークフローのエージェントを 1 つのモデルで動かします
- 過負荷（529）の要求を再試行するときのバックオフの最大の待ち時間を長くする環境変数 `CLAUDE_CODE_OVERLOADED_RETRY_MAX_DELAY_MS` を追加
- 有効な別のプラグインが同じ名前を持つためにフックが外されたプラグインに、`/plugin` で注記を出すようにした
- Read ツールに `allow_large` の選択肢を追加。ファイル全体が要りコンテキストに余裕があるとき、Claude が通常の大きさの上限を超えるテキストファイルを 1 回で読めます
- [Cloud sessions] 管理設定のセルフホストの環境の Activity タブの Sessions と Runners の一覧に、状態の絞り込みを追加（複数の状態を同時に選べる）
- [Claude Tag] Claude Tag Admin の権限を持つメンバーが、Activity のページの Memory タブでワークスペースとチャンネルのメモリーのファイルを作成・編集・削除できるようにした
- **プロジェクトの設定では Chrome をオンにできないと載った**（`chrome` の「Project settings can't turn on Chrome」）。プロジェクトの `.claude/settings.json` か `.claude/settings.local.json` の `env` で `CLAUDE_CODE_ENABLE_CFC` を `1` にしても Claude Code は適用せず、`Claude Code ignored CLAUDE_CODE_ENABLE_CFC in this project's settings` の警告を出します。チェックアウトしたリポジトリが Claude をブラウザーにつなげてはならないためで、今すぐ使うなら `claude --chrome` で始め直し、以後のセッションなら `/chrome` で **Enabled by default** を選び、警告だけ消すならその行を外します。`env-vars` にも `CLAUDE_CODE_ENABLE_CFC`（`1` で Chrome の連携をオンに、`0` でオフにして始める。`claudeInChromeDefaultEnabled` より優先し、`--chrome`・`--no-chrome` が両方より優先）が載りました。同じページには、拡張機能が Claude Code と別の claude.ai の組織にサインインしていると「Browser extension is not connected」になる節（`/status` の `Organization` の行で確かめ、拡張機能でログアウトして選び直す。ログアウトすると拡張機能に保存したショートカットと予定のタスクを失う）、資格情報が置かれる名前（`.env`、`.pem` や `.key` のファイル、`.ssh` の下）のファイルのアップロードを断ること（v2.1.293 以降）、`/chrome` の `Status` が「Not connected」なら「Reconnect extension」で接続をやり直せること（v2.1.290 以降）も加わりました — [日本語](https://code.claude.com/docs/ja/chrome#project-settings-can’t-turn-on-chrome) / [English](https://code.claude.com/docs/en/chrome#project-settings-can’t-turn-on-chrome)
- **Remote Control のセッションでコネクタを認可し直す手順が載った**（`remote-control` の「Authorize a connector again from your shell」）。モバイルアプリやウェブからは `/mcp` のパネルが使えないので、セッションが動くマシンの端末で `claude mcp login "claude.ai Slack" --no-browser` のようにコネクタの名前を引用符で囲んで実行し、表示される claude.ai のリンクを使っている機器で開いて認可します。その後に始めたセッションはそのままつながり、動いているセッションでは `/mcp reconnect claude.ai Slack` を実行します（モバイルアプリやウェブから送った `!` で始まる行はシェルでは動かない）。`/mcp` の `reconnect`・`enable`・`disable` はセッションが対話の端末で動くときに使える、と改められ、`cli-reference`・`mcp` の `claude mcp login` の説明からも案内が加わりました — [日本語](https://code.claude.com/docs/ja/remote-control#authorize-a-connector-again-from-your-shell) / [English](https://code.claude.com/docs/en/remote-control#authorize-a-connector-again-from-your-shell)
- **途中で切れたストリームの扱いが載った**（`agent-sdk/streaming-output` の「Handle a stream that's cut off」）。ターンの中断や接続の切断でストリームがメッセージの途中で切れても、ターンが終わる前にそのメッセージの `message_stop` が届き、切れたテキストか思考のブロックには `content_block_stop` も届きます。切れたツールの呼び出しには届かないので、そのブロックが開いたまま `message_stop` が来たら入力は不完全とみなします。Claude Code v2.1.290 より前は `message_stop` なしにターンが終わりえたので、応答が進行中のまま表示され続けるなら SDK を更新します（TypeScript Agent SDK は v0.3.290 から、Python Agent SDK は v0.2.164 から v2.1.290 以降を同梱） — [日本語](https://code.claude.com/docs/ja/agent-sdk/streaming-output#handle-a-stream-that’s-cut-off) / [English](https://code.claude.com/docs/en/agent-sdk/streaming-output#handle-a-stream-that’s-cut-off)
- **セルフホストのランナーで、外から届く auto モードの規則の一覧を選べるようになった**（`self-hosted-environments-reference` の「Auto mode rule lists」）。`--server-auto-mode-lists`（`SELF_HOSTED_RUNNER_SERVER_AUTO_MODE_LISTS`）は、コントロールプレーンがセッションと一緒に送る分類器の規則の一覧（`environment`・`soft_deny`・`allow`）のどれをセッションに届けるかを決め、既定の `no-allow` は `allow` を除く 2 つを、`all` はすべてを届け、`none` はどれも届けません（不正な値ではランナーが起動しない。v2.1.295 以降）。サーバーが一覧の適用を求めなければ設定によらず届かず、`--log-level debug` で求めたかどうかを確かめられます。環境変数だけの設定に `CLAUDE_RUNNER_FETCH_SERVER_PROGRESS_CAP_MS`（git のサーバーの進捗が増えている間、取得が最初のデータを試行ごとに待つ時間。既定 600000、`0` か `off` で止め、ほかの値は 120000〜1800000 に丸める。v2.1.295 以降）も加わり、`--startup-timeout-min` にはクローンの時間を数えないことが加わりました — [日本語](https://code.claude.com/docs/ja/self-hosted-environments-reference#auto-mode-rule-lists) / [English](https://code.claude.com/docs/en/self-hosted-environments-reference#auto-mode-rule-lists)
- **`claude -p` がバックグラウンドの作業を待つ間に標準エラーへ行を出すと載った**（`headless` の「Background tasks at exit」）。標準エラーが端末で 5 秒待つと、`Waiting for background work to finish` で始まり待っている作業を挙げる行を出します。`json` か `stream-json` の出力では標準出力が端末でないときだけ出るので、スクリプトが読む JSON には入りません。バックグラウンドの作業が別のターンを始めると、既定の `text` の出力は各ターンの結果を、`json` は最後のターンの結果を出す（v2.1.295 より前は `text` も最後だけ）、とも加わりました。`goal` も、非対話の実行では最後の応答がループの終わりに出る、と改められています — [日本語](https://code.claude.com/docs/ja/headless#background-tasks-at-exit) / [English](https://code.claude.com/docs/en/headless#background-tasks-at-exit)
- **VS Code の拡張機能に、Claude が送ったファイルの行と `spinnerVerbs` が載った**（`vs-code`）。Remote Control につながったセッションで Claude が `SendUserFile` ツールでファイルを送ると、会話に **Sent report.md, chart.png** のような行が出て、ファイル名をクリックするとエディターで開きます。拡張機能の設定の表には、ターンの間にスピナーが巡る動詞を CLI の `spinnerVerbs` と同じ `mode` と `verbs` で決める `spinnerVerbs` が加わりました（v2.1.296 の修正と対応） — [日本語](https://code.claude.com/docs/ja/vs-code#extension-settings) / [English](https://code.claude.com/docs/en/vs-code#extension-settings)
- **mod の `tool.call` で、ツールが動いた後に結果を Claude から隠せると載った**（`plugins/mods/events` の「Guard or change a tool call」）。`await next(e)` の後に `{ deny: reason }` を返すと、Claude は `next` が返したものの代わりに理由を読み、ツールが動いて成功していれば、理由の前に `Bash ran, and a plugin withheld its result:` のような注記が付きます（ツールがしたことは取り消さない）。組み込みのツールの呼び出しに自分で答えるなら、`result` をそのツール自身の結果の形にする、とも加わりました。`prompt.submit` で `drop` を返すとテキストは入力欄に戻り、利用者には `Prompt dropped by a hook:` と理由が見えるので理由は利用者に向けて書く、書き換えたプロンプトはプロンプトの履歴にも出る、と改められています — [日本語](https://code.claude.com/docs/ja/plugins/mods/events#guard-or-change-a-tool-call) / [English](https://code.claude.com/docs/en/plugins/mods/events#guard-or-change-a-tool-call)
- **`headersHelper` のコマンドを VS Code の拡張機能でも受け入れられると載った**（`plugins/host-marketplace`）。プラグインを単独で入れる・更新するときのコマンドの承認は、端末のセッションの `/plugin`、シェルの `claude plugin install`・`update` に加え、VS Code の拡張機能の **Manage plugins** のダイアログ（拡張機能 2.1.290 以降）でもできます。表示したコマンドと URL が変わると断る規則の、クエリ文字列だけの変更は数えないという例外は、VS Code の拡張機能と `--accept-command` には当てはまりません — [日本語](https://code.claude.com/docs/ja/plugins/host-marketplace#how-users-accept-a-headershelper-command) / [English](https://code.claude.com/docs/en/plugins/host-marketplace#how-users-accept-a-headershelper-command)

**機能改善**

- 全画面モードで、マウスのポインターの下のリンクに下線を引き、開けることを示すようにした
- コードの多い会話で、構文の色付けをしたコードブロックをキャッシュし、トランスクリプトの切り替え（ctrl+o）の反応を速くした
- Claude apps gateway の後ろのデスクトップアプリの Code タブで、セッションを始められないとき（ゲートウェイの `code` の設定の準備がないマシンを含む）に、理由を返信として示すようにした（詳細はハイライト 2 参照）
- 断られたクラウドのセッションのエラーで、組織の方針を読み込めなかった理由と、claude.ai のログインより優先される API キーか認証トークンの名前を示すようにした
- `--debug` の出力で、カスタムのエージェントのファイルの認識できない frontmatter の項目を名指しし、ありそうな打ち間違いの助言を出すようにした
- auto モードで、auto モードの確認が使える答えを得られずに動かさなかったツールの呼び出しを、赤いエラーではなく薄い「Not run」の行で示すようにした
- フックの `--debug` の出力で、ツールの呼び出し・プロンプト・SessionStart・Stop の command のフックが終わったときにコマンド・プラグイン・結果・所要時間を記録し、遅いフックを見つけられるようにした
- `CLAUDE_CODE_TRANSCRIPT_LOCAL_GC` で、大きなトランスクリプトのファイルを書き直しても 10% 未満しか空かない場合は書き直さないようにした
- [Code Review] Code Review の管理設定で、設定を保存できなかった理由（方針による制限など）を、汎用の失敗のメッセージの代わりに示すようにした
- **ホットリロードを有効にするかの質問が出なくなる場合と、hooks モジュールの入れ子の上限が載った**（`plugins/mods/troubleshoot`・`plugins/mods/reference`）。質問が答えを選ばれないまま 3 回終わるとホットリロードはオフのままになり（`askUserQuestionTimeout` で時間切れになる場合など。自分で閉じたものは数えない）、mod を動かすにはそのディレクトリを mods のフォルダーの外へ写し、`--plugin-dir` で新しいセッションを始めます。hooks モジュールの 1 つのファイルで関数・ブロック・ループなどのスコープを入れ子にできるのは 2,000 段までで、超えると `code nested too deep to scan: more than 2000 scopes` で読み込まれません（`claude plugin validate` も同じ理由を報告）。`tool.describe` はツール検索で読み込んだ MCP のツールにもう一度発火し（`e.description` は読み込んだツールで Claude が読むテキスト）、`session.append` は行のテキストのブロックか `tool_result` のブロックの `content` を書き換えられる、とも改められました — [日本語](https://code.claude.com/docs/ja/plugins/mods/troubleshoot#claude-code-stops-asking-to-enable-hot-reloading) / [English](https://code.claude.com/docs/en/plugins/mods/troubleshoot#claude-code-stops-asking-to-enable-hot-reloading)
- **セルフホストのクイックスタートが、案内付きの設定と手作業の設定に分かれた**（`self-hosted-environments-quickstart`）。前提に、テストのセッション用の公開のリポジトリか、このホストが資格情報を聞かれずに HTTPS の URL でクローンできるリポジトリが加わりました。案内付きの設定（「Run the guided setup」。Owner のアカウントの `claude auth login` が要り、API キーやサードパーティのプロバイダーではセッションは始まるが組織の確認に失敗する。テストのセッションは自分で始め、最後の手順でランナーを止める）と手作業の設定（「Set up manually」。Owner が環境を作って秘密を渡してくれたなら手順 2 から）が分かれ、秘密のファイルを別のユーザーのランナーが読めないと `EACCES` で終わること、登録すると `Registered: runner_id=<runner-id>` が出ること、git のエラーに `could not read Username for` があればそのホストの HTTPS の資格情報がないこと、も加わりました。「If the runner exits」（作業が終わった `[runner:exit] account workload drained — exiting` と、連絡が途絶えた `runner record gone server-side`・`poll auth failed`）の節もできています — [日本語](https://code.claude.com/docs/ja/self-hosted-environments-quickstart#if-the-runner-exits) / [English](https://code.claude.com/docs/en/self-hosted-environments-quickstart#if-the-runner-exits)
- **セルフホストの環境のテストで、セッションを作るコマンドの出力が明記された**（`self-hosted-environments-testing`）。`claude -p "<prompt>" --environment <environment-id> --output-format json` は、作成できれば `{"ok":true,"session_id":"session_...",...}` の 1 行を、失敗すれば `{"ok":false,"error":"..."}` を出して終了コード 1 で終わり、クラウドのセッションが組織で使えない・プロンプトがないなどの一部の早いエラーでは JSON の行なしに標準エラーに出して終了コード 1 で終わります。例のスクリプトは `claude -p` に `< /dev/null` を渡すようになり、動かす前の準備が箇条書きになりました — [日本語](https://code.claude.com/docs/ja/self-hosted-environments-testing#run-the-test-loop) / [English](https://code.claude.com/docs/en/self-hosted-environments-testing#run-the-test-loop)
- **`decode-token` が鍵を取得できないか検証できないときの振る舞いが載った**（`self-hosted-environments-identity`）。理由を標準エラーに出し、クレームを何も出さずに終了コード 1 で終わります — [日本語](https://code.claude.com/docs/ja/self-hosted-environments-identity#verify-the-token-inside-the-session) / [English](https://code.claude.com/docs/en/self-hosted-environments-identity#verify-the-token-inside-the-session)
- **定期的なタスクの遅れの幅が表になった**（`scheduled-tasks` の「Jitter」）。定期的なタスクは作成時にタスクの ID から決まる固定の遅れを毎回足され、10 分ごとなら 0〜5 分、30 分ごとなら 0〜15 分、1 時間ごとか日ごとなどそれより間遠なら 0〜30 分です。`7,37 * * * *` で遅れが 14 分なら毎時 `:21` と `:51` に動く、という例が加わりました。1 回限りのタスクは `:00` か `:30` なら最大 90 秒早く動き、それ以外の分ならずらさない、という説明も小見出しに分かれています — [日本語](https://code.claude.com/docs/ja/scheduled-tasks#jitter) / [English](https://code.claude.com/docs/en/scheduled-tasks#jitter)
- **API のエラーのイベントの `attempt` の数え方が改められた**（`monitoring-usage`）。ストリーミングの失敗の後に要求をし直すたびに `attempt` は `1` から数え直すので、小さい値でも再試行を使い切ったことがあり、すべての再試行を使い切ったときの値は有効な上限に 1 を足した値以下（既定で 11 以下）、という書き方になりました。プロンプトを読むごとに `at_mention` のイベントは `mention_type` が `"agent"` と `"mcp_resource"` のものを各 100 件までしか記録しない（それを超える言及も解決はする）、とも加わっています — [日本語](https://code.claude.com/docs/ja/monitoring-usage#detect-retry-exhaustion) / [English](https://code.claude.com/docs/en/monitoring-usage#detect-retry-exhaustion)
- **vim モードの `f`・`F`・`t`・`T` と `df`・`dt` が今の行の中で動くと明記された**（`interactive-mode`）。約 1,000 行か 100,000 文字より長い返信の中の課題の参照（`owner/repo#123`）はリンクにならない、とも加わりました — [日本語](https://code.claude.com/docs/ja/interactive-mode#issue-reference-links) / [English](https://code.claude.com/docs/en/interactive-mode#issue-reference-links)
- **プロジェクトのスレッドに権限のルールが届くかが、環境の種類ごとに書き分けられた**（`claude-projects`）。リポジトリが 1 つならクラウドのスレッドはルールを適用し、複数で Anthropic がホストする環境なら届かず、複数でセルフホストの環境ならどのリポジトリの設定が効くかを `self-hosted-environments-configuration` で見ます。複数のリポジトリのクローンを追加のディレクトリとして付ける、という説明は外れました — [日本語](https://code.claude.com/docs/ja/claude-projects#what-threads-pick-up-from-your-repositories) / [English](https://code.claude.com/docs/en/claude-projects#what-threads-pick-up-from-your-repositories)
- **`claude attach` と `claude logs` に渡す名前の説明から「動いている」の限定が外れた**（`agent-view`・`cli-reference`）。ID の代わりにセッションの名前の一部を取れる（v2.1.290 以降）、という説明が「動いているセッションの名前」から「セッションの名前」になりました

**バグ修正**

- 管理設定の `PreToolUse` のフックが `"continue": false` で呼び出しを拒否したときと、管理設定の `prompt` のフックが呼び出しを止めたときに、呼び出しは断るがターンを終えない問題を修正
- 一部のセッションで、管理設定の PostToolUse のフックが `updatedMCPToolOutput` を適用しない問題を修正
- ヘッドレスのセッションで、ディレクトリを移るかプラグインを読み込み直した後、そのフォルダーでオフにしたフォルダーの `.mcp.json` かプラグインの MCP サーバーを始める問題を修正
- `allowedProviders` に `"gateway"` を含めて配る Claude apps gateway が、ユーザー設定でそのゲートウェイを指すノート PC を締め出す問題を修正
- 管理設定が `forceLoginMethod` を `gateway` にして `forceLoginGatewayUrl` を設定しないマシンで、保存した Claude apps gateway のサインインが無視される問題を修正（2.1.295 での退行）
- セッションの履歴を読めないとき、`--teleport` が空の会話を開く問題を修正
- Haiku 5.5 など適応型の思考だけを取るモデルのトークンの数え方を修正。一部のゲートウェイの後ろで失敗し、ほかでは予算型の思考で数えられていました
- セッションの停止が中断したツールの呼び出しを、利用者が拒否したと再開したサブエージェントに伝える問題を修正
- プラグインのヒントのタグに似たテキストを含むと、フックの出力が変えられる問題を修正
- 共有したトランスクリプトとデバッグのログの秘密の伏せ字で、値のないキーの後に続く一部の値（シェルの文字列の中に書いた JSON を含む）を見落とす問題を修正
- MATE Terminal など古い VTE ベースの端末で、コピーの後に `52;c;…` のエスケープシーケンスが画面に出る問題を修正
- `/diff` のパネルかダイアログを開いている間、トーストと通知が見えないまま待たされる問題を修正
- `UserPromptSubmit` のフックか mod の `prompt.submit` のフックの間の Esc か中断で、ヘッドレスのセッションが終わる、入力したプロンプトが消える、確認していないプロンプトが通る問題を修正
- ヘッドレスのセッションの開始後に読み込んだプラグインの SessionStart のフックが、同じ名前（または別の綴り）の別のプラグインがすでに動いていると飛ばされる問題を修正
- 登録を断られたときに `claude self-hosted-runner` が誤解を招くエラーを出す問題を修正。組織の管理設定を名指しするか、再起動したオンデマンドのランナーには新しい作業指示が要ると伝えます
- 同じリポジトリの別のセッションが `--capacity` 1 超のランナーで始まる間、セルフホストのランナーのセッションの git の fetch・pull・push が失敗する問題を修正
- ワークフローのスクリプトが、約 20,000 段より深く入れ子になった結果・エージェントの選択肢などの値を黙って切り詰め、深く入れ子になった結果が巨大なタスクの出力ファイルを書く問題を修正
- プラグインが提供する `$` のメソッドが、呼び出したエージェントではなく本体のセッションの作業ディレクトリで動き、呼び出したフックが持つターンを無視する問題を修正
- mod を読み込み直すか外した後も動いていた mod のフックから、`$.agent.register` が成功する問題を修正。その呼び出しは断ります
- 応答が 4 MiB の本文の上限を超える `Content-Length` を宣言すると、mod の `$.http.fetch` が `HEAD` の要求を断る問題を修正
- `constructor` のような名前のマーケットプレイスで、`claude plugin marketplace add`・`marketplace update`・`plugin install` が内部エラーで失敗する問題を修正。`add` はそのような名前をはっきり断ります
- `constructor` か `prototype` という名前のプラグインの秘密が、そのプラグインの選択肢の次の保存で消される問題を修正
- 機能フラグが読み込まれていないとき、保存した権限が許す Claude in Chrome の操作で、クラウドのセッションが auto モードの確認を飛ばす問題を修正
- MCP のツールの結果がターンを終えていたとき、再起動の後に `CLAUDE_CODE_RESUME_INTERRUPTED_TURN` が終わったターンを再実行する問題を修正
- シェル変数 `BASH_ARGV0` に代入してから使う一部のコマンドを、Bash の権限の確認が自動で承認する問題を修正。これらは承認を求めます
- 有効な UTF-8 でないファイル（Windows-1252・Shift-JIS・GBK）で、Edit と NotebookEdit がすべての非 ASCII 文字を置き換える問題を修正。そのような編集は断ります
- バックグラウンドのサービスの応答が遅いとき、`←` の直後に送ったプロンプトが 2 回（うち 1 回は前面で見えないまま）実行される問題を修正
- SessionStart のフックがまだ動いている間に送ったプロンプトが、`←` でセッションをバックグラウンドに移すと消える問題を修正。送られはしませんが、`↑` で戻せます
- ヘッドレスのセッションで、遅れて読み込んだプラグインの SessionStart のフックの出力が `/clear` の後の新しい会話に届く問題を修正
- フックが CLAUDE_ENV_FILE に書いた変数が PowerShell のコマンドに見えない問題を修正（ファイルが単純な代入だけを持つ場合）
- MCP サーバーが認証を要するとき、Claude がクラウドのセッションを非対話と呼び、`/mcp` か `claude mcp` を勧める問題を修正
- クラウドのセッション・Agent SDK・IDE の連携で、`/code-review` が生の JSON の配列で終わる問題を修正。指摘は番号付きの一覧で出ます
- auto モードが、共有の設定が変わっていないのに変わったとして、自分のアーティファクトへの更新を時々断る問題を修正
- 複数のセッションが設定のディレクトリを共有すると、claude.ai から同期したスキルのインストールが終わらず、同期のたびにまたダウンロードされる問題を修正
- 宣言したマーケットプレイスの依存も claude.ai から同期されると、claude.ai から同期したプラグインが無効になる問題を修正
- Linux のマシンからコピーしたプラグインのパスが /home の下を指すとき、macOS で起動が固まる問題を修正
- Windows でチェックアウトしたファイルのような CRLF の改行のスクリプトのファイルを、Workflow ツールが断る問題を修正
- `git commit -q` か `git -C <dir> commit` の後、OpenTelemetry の `tool_result` のイベントに `git_commit_id` がない問題を修正
- テキストが Unicode の行・段落の区切り文字（U+2028・U+2029）を含むと、`CLAUDE_CODE_TRANSCRIPT_LOCAL_GC` が保存したトランスクリプトからメッセージを落とす問題を修正
- テキストが Unicode の行・段落の区切り文字（U+2028・U+2029）を含むと、`claude purge` が履歴のファイルにプロンプトを残す問題を修正
- Windows: 約 1 KB より長い PowerShell のコマンドが常に許可を求める問題を修正。許可のルールと読み取り専用の判定が 32 KB まで効きます
- Windows: 終了時に stdio の MCP サーバーが強制終了される問題を修正。まず標準入力を閉じ、300 ミリ秒後もサーバーが動いているときだけプロセスツリーを止めます
- Windows: GitHub の SSH 鍵がないマシンで、GitHub の `owner/repo` のプラグインのソースの `claude plugin install` が失敗する問題を修正。クローンを HTTPS で再試行します
- Windows: バイパスの権限モードで、Git Bash の `rm -rf /c/Users/<name>` が尋ねない問題を修正
- [VSCode] 拡張機能の設定に `claudeCode.spinnerVerbs` がない問題を修正。settings.json で補完・検証され、不正な値でチャットのパネルが壊れなくなりました
- [VSCode] Windows で、C:\repo\file.ts や file:///C:/repo/file.ts のような Windows の完全なパスで書いたチャットのリンクがファイルを開かない問題を修正
- [VSCode] OS・VS Code・`prefersReducedMotion` の設定で動きを減らしても、作業中の表示が動き続ける問題を修正
- [VSCode] 画面がオフだった後やリモートのウィンドウが再接続した後など、パネルが遅れてメッセージに追いついたとき、プロンプトキャッシュの時計がまだ温かいと示す問題を修正
- [Cloud sessions] セルフホストのランナーを待つすべてのクラウドのセッションが同じ待ち順を示す問題を修正。各セッションが前に何件あるかを示します
- [Cloud sessions] クラウドのセッションで Claude がまだ返信している間に送ったメッセージが、返信の終わりにその上へ跳ぶ問題を修正。読み込み直した後も含めて下に留まります
- [Claude Tag] 括弧を含む URL へのリンクが、Claude の Slack の返信とタスクのチェックリストの一部で壊れ、余計な括弧のテキストを出して違うページを開く問題を修正
- [Claude Tag] 6 桁のプルリクエストの番号のように 16 進の色に見えるだけのコードの横に、Claude の Slack の返信が色見本を描く問題を修正
- [Claude Tag] Claude が Slack のチャンネルに投稿するプラグインの確認のカードが、プラグインの名前ではなく ID を示す問題を修正
- [Claude Tag] チャンネル自身の設定が含まないプラグインを外すカードを、Slack の Claude が投稿する問題を修正。代わりにプラグインの出どころを説明します
- [Claude Tag] セルフホストの環境のセッションが作業の途中で新しいランナーに移ると、Slack の Claude が返信を失うことがある問題を修正
- [Code Review] レビューが終わった後も、プルリクエストの Code Review のチェックが「進行中」のままになることがある問題を修正。レビューの結果を示します

**その他**

- `/cost`・ステータスライン・`--max-budget-usd`・SDK の費用の数字で、Sonnet 5.5 のキャッシュの読み取りの価格を 100 万トークンあたり 0.20 ドルから 0.10 ドルに変更
- 同梱の dataviz スキルを更新。ライトモードの 7 番目の系列を明るい紫に、ダークモードの主なテキストを柔らかくし、y 軸のラベルを 1K のように短くしました
- 先に送る MCP のツールの説明と MCP サーバーの指示の既定の上限を、2,048 文字から 4,096 文字に変更
- `←` を変更。セッションがバックグラウンドに移る間に始まったターンか `!` のコマンドは、見えないところで最後まで動かずに止まります
- [VSCode] `@browser` でつないだものを含むすべてのセッションで、端末と同じく Claude in Chrome がブラウザーの操作の前に尋ねるように変更。セッションでサイトを許可すると繰り返し尋ねません。`chrome` の「Permission prompts in VS Code sessions」も、プロンプトはチャットのパネルのカードで出て、許可していないサイトならそのサイトを許可する選択肢も出す、と改められ、`@browser` と打てば拡張機能が承認するという記述は外れました — [日本語](https://code.claude.com/docs/ja/chrome#permission-prompts-in-vs-code-sessions) / [English](https://code.claude.com/docs/en/chrome#permission-prompts-in-vs-code-sessions)
- [Claude Tag] Slack の Claude が、セッションのリンク・モデル・費用のフッターをスレッドの最新の返信にだけ出すように変更。その前の返信からはフッターが外れます
- **ハイライトに関わる言い換え**: `hooks-guide`（`onFailure`）はハイライト 1、`claude-apps-gateway`・`claude-apps-gateway-deploy`・`claude-apps-gateway-on-aws`・`managed-settings`（`cli` か `code` のブロック）はハイライト 2、`self-hosted-environments`・`self-hosted-environments-reference`（git proxy）はハイライト 3 のとおりです。`claude-apps-gateway` の開発者のログインの手順と `claude-apps-gateway-on-aws` の手順には、`forceLoginMethod`・`forceLoginGatewayUrl` に加えて `parentSettingsBehavior: "merge"` を設定する（配る）ことも加わりました
- **クラウドの VM の回収で戻らないもの**（`claude-code-on-the-web`）: 自分のペースの `/loop` の保留中の wakeup も戻らず、ループを再開するには `/loop` をもう一度実行します — [日本語](https://code.claude.com/docs/ja/claude-code-on-the-web#environment-expired) / [English](https://code.claude.com/docs/en/claude-code-on-the-web#environment-expired)
- **MCP のプロトコルの交渉**（`mcp`・`env-vars`）: v2 のランタイムは HTTP・stdio と claude.ai のコネクタのサーバーに新しい版に対応するかを尋ねる、という書き方になり、機能フラグを取得するセッションに限る、という条件が外れました。機能フラグの取得をオフにしたときにできないことの一覧からも、claude.ai のコネクタに版 2026-07-28 を尋ねる項目が外れています
- **HIPAA の設定の例**（`hipaa-setup`・`managed-settings`）: サンドボックス・ネットワークの許可リスト・資格情報の保護・ローカルのデータの保持を含む、より完全な `managed-settings.json` として、設定の例のリポジトリの `settings-hipaa.json` と `README-hipaa.md` への案内が加わりました — [日本語](https://code.claude.com/docs/ja/hipaa-setup#deploy-managed-settings) / [English](https://code.claude.com/docs/en/hipaa-setup#deploy-managed-settings)
- **サブエージェントが先に読み込むスキル**（`sub-agents`）: `skills` のフィールドに挙げたスキルは、異なる名前の最初の 32 個まで読み込む、と加わりました — [日本語](https://code.claude.com/docs/ja/sub-agents#preload-skills-into-subagents) / [English](https://code.claude.com/docs/en/sub-agents#preload-skills-into-subagents)
- **プラグインの細かな改訂**: `plugins/install`（まだ加えていないマーケットプレイスなら `Successfully added marketplace: <name> (declared in user settings)` を出してからプラグインを入れる）、`plugins/mods/create`（型の定義のファイルは対話のセッションで `--plugin-dir` から読み込んだ mod か Claude が書いた mod に書き、オンラインの `claude-code.d.ts` への案内は外れた）、`plugins/manifest-reference`（予約名を確かめるのはこれらのコマンドだけ、の文を削除）、`plugins/publish`（`claude plugin validate .` が確かめる内容への案内）
- **言い回しの調整**: `commands`（`-p` での `/mcp` の説明）、`cli-reference`（`claude mcp login` のコネクタへの案内、`--mcp-config` のセルフホストの環境での短い待ち）、`env-vars`（`CLAUDE_CODE_MCP_STARTUP_WAIT_MS` のセルフホストの環境での意味）、`glossary`（リンクの文言）、`troubleshooting`（ダウンロードの失敗の案内先を `troubleshoot-install` に）、`skills`・`cloud-environments`（claude.ai のアカウントのスキルへの案内）、`agent-sdk/python`（`CLAUDE_CODE_MAX_RETRIES` の説明の分割）
- **見出しの改称**: 「From …」「In …」「For …」のような短い見出しが、内容を表す見出しに改められました。`agent-sdk/mcp`（「Add a server in code」など）、`agent-sdk/migration-guide`（「Migrate a TypeScript or JavaScript project」など）、`agent-view`（「Dispatch an agent from agent view」など）、`claude-code-on-the-web`（「Start a cloud session from your terminal」「Continue a cloud session in your terminal」）、`env-vars`（「Set variables in your shell」など）、`jetbrains`、`mcp`（「Add a server from a URL」など）、`monitoring-usage`（「Backends for metrics」など）、`plugins/create`（「Load a plugin from a directory or `.zip`」など）、`security-guidance`（「Checks on each file edit」など）、`setup`（「Uninstall a native installation」など）です。多くは旧い見出しの id を残していますが、`plugins/create` の「Load a folder of plugins」と `hooks-guide` の「Check what a hook did」は id も新しくなりました
- **見出しマップ**: 75 行が加わり 37 行が外れました（各 1 行は自動生成のスタンプ）。新しい見出しが 39、改称が 33、`errors` から `troubleshoot-install` への移動が 2 で、`errors` の「Installation errors」が消えました
- **見出しマップ冒頭の自動生成スタンプが、2026年10月09日 00時59分51秒 UTC から 2026年10月10日 01時38分51秒 UTC へ進みました**

**参考リンクについて**: 日本語版は、changelog を除く変更のあった 57 ページをすべて取得して、リンクを付けた節の id と今回の内容（新しい節や書き換えた文）があるかを確かめました。今回も日本語版の追従が早く、`hooks`・`claude-apps-gateway-config`・`self-hosted-environments-deploy`・`self-hosted-environments-configuration`・`plugins/mods/api`・`agent-sdk/typescript`・`troubleshoot-install`・`errors`・`plugins/troubleshooting` をはじめ、リンクを付けたすべてのページの該当の節がすでに今回の内容になっていたため、すべて日本語版のリンクを付けています。changelog だけに載っていて対応する節のない項目にはリンクを付けていません。**changelog ページへのリンクは、本サマリの方針どおり付けていません。**

## 新着情報

**今回、`whats-new/` 配下のページに変更はありません。**

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-10-08.md](./archives/latest/2026-10-08.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-10-08.md](./archives/latest-detail/2026-10-08.md)

<!--
base_commit: f7270cc772c15a132c348d04599b3544e0e7722c
head_commit: 83613c64d38ac27f70c52d6b25167a2fa1f233f2
generated_at_full: 2026-10-10T15:13:30+09:00
-->
