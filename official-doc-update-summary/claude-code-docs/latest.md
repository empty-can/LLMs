---
対象期間: 2026年09月13日 〜 2026年09月14日
作成日: 2026-09-14
---

# Claude Code 公式ドキュメント更新サマリ

```markdown
前回が「差分 10 行・本文の変わったページ 1 / 192」という極小の回だったのに対し、今回は**changelog が 1 行も動かないまま本文だけが 24 ページ分書き換わった回**です。差分は 3 ファイル・300 行（追加 163・削除 137）で、`llms-full.txt` は 96,353 行から 96,360 行へ 7 行増えました。**新規ページも削除ページもなく（192 のまま）、50 行を超えるページも無い**代わりに、**変更は 24 ページに薄く広がり、うち 12 ページが Agent SDK** です。changelog が無変更なのは 82 回の取り込みで 22 回目ですが、**本文側に v2.1.269 を要件として挙げる記述が 6 行新設された**ことから、今回はリリースではなく**前日までに出たリリースを文書が追いかけた回**と読めます。とりわけ **advisor のモデルペアリング表は、拒否されるだけだった組み合わせに「API エラーで失敗する」という第 2 の層が加わり、受理範囲が実質的に狭まりました**。前回「見出しマップだけ先に届いた」と書いた `goal` の 2 見出しは**1 日で本文として着地**し、代わりに**別の 4 見出しと新着情報 3 ページが新たな持ち越し**になっています。

主要なものを以下に挙げます。

1. goal ページの失敗ハンドリングが本文として着地し、前回の持ち越し 2 件が 1 日で解消した
2. advisor のペアリング表に Opus 5 と Fable 5.1 が入り、拒否と API エラーの 2 層になった
3. claude.ai 同期スキルが完全名を得て、名前が衝突してもスキップされなくなった
4. VS Code 拡張の Customize に Hooks と Permissions が入り、エージェントマップが加わった
5. 新着情報が 3 週分まとめて登録されたが、本文は 1 行も届いていない
```

## ハイライト

1. [**goal ページの失敗ハンドリングが本文として着地し、前回の持ち越し 2 件が 1 日で解消した**](./latest-detail.md#1-goal-ページの失敗ハンドリングが本文として着地し前回の持ち越し-2-件が-1-日で解消した):  
  前回サマリのハイライト 2 で「見出しマップにだけ届き、本文には 3 つとも来ていない」と書いた `When a turn fails`（ターンが失敗したとき）と `Other errors retry or pause the goal`（その他のエラーはゴールを再試行または一時停止する）が、**翌日の取り込みで本文として着地しました**。内容は前回の推測どおり、旧来 1 文で済ませていた「その他の失敗の後はゴールをアクティブなままにする」を独立した節へ格上げしたもので、**`Goal still active` と `Goal paused` という 2 種類の通知、自動再試行は 3 回まででその後は一時停止、`CLAUDE_CODE_GOAL_CHECKIN_MINUTES` を `0` にすると再試行もチェックインも止まる**、という具体が書き下ろされています。**v2.1.269 以降の対話型セッション限定**と明記され、前回「v2.1.269 の changelog 項目と対応して読める」とした対応づけも裏づけられました。**日本語版は取り込み当日の時点で既に全訳済み**で、英語版に遅れていません。
2. [**advisor のペアリング表に Opus 5 と Fable 5.1 が入り、拒否と API エラーの 2 層になった**](./latest-detail.md#2-advisor-のペアリング表に-opus-5-と-fable-51-が入り拒否と-api-エラーの-2-層になった):  
  メインモデルとアドバイザーの対応表が **6 行から 8 行**になり、`Opus 4.7 or later` が `Opus 4.7 または Opus 4.8` と `Opus 5` に、`Fable 5.1 or Fable 5` が `Fable 5` と `Fable 5.1` に分かれました。**これは行の整理ではなく受理範囲の変更**です ―― 旧表では `Opus 4.7 以降` のメインが `Opus 4.7 以降` のアドバイザーを受け入れたので Opus 5 メインは Opus 4.7/4.8 を使えましたが、**新表の Opus 5 は `Fable, Opus 5` だけで、Opus 4.7/4.8 を指定したリクエストは API エラーで失敗**します。同様に **Fable 5.1 メインは Fable 5 アドバイザーで、Sonnet 5 メインは Opus 4.6 アドバイザーで API エラー**になります。検証の記述も「Claude Code がリクエスト送信前に検証する」から「**Claude Code が検証し、API が再度検証する**」へ変わり、**添付されずに済む「拒否」と、添付された上で API に蹴られる「エラー」**が区別されました。エラー文字列 `'<advisor model>' cannot be used as an advisor when the request model is '<main model>'` も原文に追加されています。
3. [**claude.ai 同期スキルが完全名を得て、名前が衝突してもスキップされなくなった**](./latest-detail.md#3-claudeai-同期スキルが完全名を得て名前が衝突してもスキップされなくなった):  
  claude.ai アカウントから同期したスキルは、**v2.1.269 より前は短い名前しか持たず、他のコマンドと名前が衝突すると読み込まれませんでした**。今回の更新で **`/anthropic-skills:<name>` という完全名が付き、短名が取られている場合でも完全名でなら実行できる**ようになりました。原文は「ローカルの `deploy` スキルと同期された `deploy` があるとき、`/deploy` はローカル側を、`/anthropic-skills:deploy` は同期側を実行する」と例示し、**`Before v2.1.269, a synced skill had only its short name.`** と旧挙動を明記しています。これに伴い「スキップする」という表現が**スキル名の比較規則の説明・非対話セッションの `help` / `feedback` の扱い・優先順位表**から一斉に書き換えられ、**コマンド名の由来を示す表にも同期スキルの行が 1 行追加**されました。
4. [**VS Code 拡張の Customize に Hooks と Permissions が入り、エージェントマップが加わった**](./latest-detail.md#4-vs-code-拡張の-customize-に-hooks-と-permissions-が入りエージェントマップが加わった):  
  `vs-code` ページは今回**最も行数が動いたページ（45 行）**で、**v2.1.269 を要件とする UI が 4 つ**書き足されました ―― Customize セクションの **Hooks**（セッションに読み込まれた hooks をイベント別に一覧し、ユーザー／プロジェクト／ローカル設定のものは編集可、管理設定とプラグイン由来は読み取り専用）、同 **Permissions**（権限ルールを Allow / Ask / Deny に分けて一覧、同様に編集可否が分かれる）、**Focus view でのサブエージェント進行行**、そして**エージェントマップ**（プロンプトボックス下部の `2 agents` のような表示をクリックするとサブエージェントがツリーで開き、各々のステータス・経過時間・トークン数が見え、読み取り専用トランスクリプトを開いたり停止したりできる）です。あわせて**選択範囲インジケータの操作が「目隠しトグル」から「X で除去」へ変わり**、**「タブの右クリックメニューにも出る」という記述が 4 か所から消えました**。
5. [**新着情報が 3 週分まとめて登録されたが、本文は 1 行も届いていない**](./latest-detail.md#5-新着情報が-3-週分まとめて登録されたが本文は-1-行も届いていない):  
  `llms.txt` に **Week 35・Week 36・Week 37 の 3 ページが一度に追加**され、収録 URL は **203 件から 206 件**になりました。見出しマップにも 3 ページ分のエントリが入っています。**しかし `llms-full.txt` にはこの 3 ページの本文が 1 行も含まれていません** ―― 全文中の週間ダイジェストは **Week 34 が最後のまま**で、索引ページ（`whats-new/index`）も Week 34 止まりです。**週間ダイジェストの本文が最後に追加されたのは 2026年08月23日 の取り込みで、以後 20 回連続で追加がありません**。つまり今回動いたのは**索引側だけ**で、本文レベルでは無差分の連続が途切れていません。

## 新規追加されたページ

（今回の対象期間に新規追加・削除されたリファレンス系ドキュメントページはありません。`llms-full.txt` の展開ページ数は **192 のまま**で、増減がありません。`llms.txt` の収録 URL は 203 件から 206 件へ増えていますが、**増えた 3 件はすべて新着情報（`whats-new/`）で、本文はまだ届いていない**ため、新着情報カテゴリで扱います）

## 大幅に更新されたページ

（本カテゴリの該当はありません。分類の基準は従来どおり「実質の差分 50 行以上 かつ 内容の変更を伴うこと」ですが、**今回の最大は `vs-code` ページの 45 行**で閾値に届きません。しかもその 45 行のうち 32 行はショートカット表の桁揃えであり、内容の変更はさらに小さい規模です。**今回の特徴は 1 ページの大改訂ではなく、24 ページへの薄い広がり**にあります）

## 軽微な更新

今回の差分は **3 ファイル・300 行**（追加 163・削除 137）です。内訳は `llms-full.txt` が 275 行（追加 141・削除 134）、`llms.txt` が 7 行（追加 5・削除 2）、ページ見出しマップ（`en/claude_code_docs_map.md`）が 18 行（追加 17・削除 1）です。`llms-full.txt` の総行数は **96,353 行から 96,360 行へ 7 行増え**、展開ページ数は **192 のまま**、**本文が変わったページは 24 / 192**（前回は 1 / 192）でした。

**今回の際立った点は、changelog ページが 1 行も変わっていないことです。** 入力ディレクトリに触れた隣接コミット間 82 回のうち **changelog が無変更だったのは 22 回**で、直近は **2026年09月09日 の取り込み**なので珍しくはありません。ただし**本文側には v2.1.269 を要件として挙げる記述が 6 行新設**されており（`vs-code` に 4 行、`goal` と `skills` に 1 行ずつ）、**今回はリリースが出た回ではなく、前日までに出たリリースを文書が追いかけた回**だと読めます。追加行に現れるバージョンは v2.1.219・v2.1.221・v2.1.225・v2.1.228・v2.1.234・v2.1.257・v2.1.269 の 7 つですが、**削除行に対応が無い（＝今回新しく持ち込まれた）のは v2.1.269 の 6 行と v2.1.219 の 1 行だけ**で、残りは既存記述の移動に伴って追加行にも削除行にも同数現れているだけです。

**変更ページ 24 のうち 12 が Agent SDK 配下**でした。行数の多い順に `vs-code`(45)・`agent-sdk/python`(39)・`skills`(32)・`goal`(29)・`agent-sdk/streaming-output`(29)・`advisor`(23)・`claude-code-on-the-web`(18)・`agent-sdk/hooks`(9)・`chrome`(7) と続き、残る 15 ページは 6 行以下、うち 11 ページは 2 行（1 行差し替え）です。

**新機能**

- **claude.ai から同期したスキルに `/anthropic-skills:<name>` の完全名が付きました**（v2.1.269）。短名が他のコマンドと衝突しても、完全名でなら実行できます（詳細はハイライト 3 参照）— [Extend Claude with skills](https://code.claude.com/docs/en/skills#when-a-synced-skill-name-matches-another-command)
- **VS Code 拡張の Customize セクションに Hooks と Permissions が加わり、エージェントマップが新設されました**（v2.1.269）。Focus view にはサブエージェントのライブ進行行も表示されます（詳細はハイライト 4 参照）— [VS Code で Claude Code を使用する](https://code.claude.com/docs/ja/vs-code#use-the-prompt-box) / [Use Claude Code in VS Code](https://code.claude.com/docs/en/vs-code#use-the-prompt-box)
- **`/goal` が、修正を要しない失敗の後に自動再試行または一時停止するようになりました**（v2.1.269 以降の対話型セッション）。`Goal still active` / `Goal paused` の通知と、3 回で一時停止へ切り替わる挙動が本文に書き下ろされています（詳細はハイライト 1 参照）— [Claude をゴールに向かって動作させ続ける](https://code.claude.com/docs/ja/goal#other-errors-retry-or-pause-the-goal) / [Keep Claude working toward a goal](https://code.claude.com/docs/en/goal#other-errors-retry-or-pause-the-goal)

**機能改善**

- **advisor のペアリング表が 8 行に増え、「拒否」と「API エラーで失敗」の 2 層に整理されました**。Opus 5 メインが Opus 4.7 / 4.8 アドバイザーを、Fable 5.1 メインが Fable 5 アドバイザーを、Sonnet 5 メインが Opus 4.6 アドバイザーを使えないことが明記されています（詳細はハイライト 2 参照）— [advisor ツールで難しい判断をエスカレートする](https://code.claude.com/docs/ja/advisor#choose-an-advisor-model) / [Escalate hard decisions with the advisor tool](https://code.claude.com/docs/en/advisor#choose-an-advisor-model)
- **`settings-reference` の `advisorModel` から「能力が足りないときはアドバイザーなしで送る」という結果の説明が外れ**、advisor ページの表と「受理されない組み合わせを選んだときに何が起きるか」を参照する形になりました。上記の 2 層化に合わせた変更です — [All settings](https://code.claude.com/docs/en/settings-reference#advisormodel)
- **プランモードでのブラウザツールの権限説明が全面的に差し替えられました**。従来の「読み取り専用呼び出しはプロンプトなし／状態変更呼び出しは承認を求める」という二分法と、各々の具体例の列挙が削除され、**GIF の記録・新しいタブを開く・ショートカットの実行の 3 つでプロンプトが出る**という記述に変わりました。さらに**バイパス権限モードが利用可能でフィーチャーフラグ取得がオフのセッションではプロンプトなしで実行される**という条件が新設されています。`tabs_context_mcp` の `createIfEmpty` と、これらのアクションを含む `browser_batch` もプロンプト対象である点だけが残りました — [Use Claude Code with Chrome](https://code.claude.com/docs/en/chrome#browser-tools-in-plan-mode)
- **クラウドセッションの進捗確認手段としての `/tasks` への言及が 3 か所から削除されました**（`claude-code-on-the-web` で 2 か所、`github-enterprise-server` で 1 か所）。いずれも claude.ai・Claude モバイルアプリで確認するという記述だけが残っています。**`/tasks` からテレポートする手順は別の節に残っている**ので、コマンド自体が無くなったわけではありません — [ウェブ上の Claude Code を使用する](https://code.claude.com/docs/ja/claude-code-on-the-web#from-terminal-to-web) / [Use Claude Code on the web](https://code.claude.com/docs/en/claude-code-on-the-web#from-terminal-to-web)
- **コンピュータ使用の macOS 通知が出るタイミングの記述が変わりました**。「Claude がロックを取得したとき」から「**各ターンで Claude が最初にコンピュータを使うとき**」になり、あわせてロックの説明から「マシン全体の（machine-wide）」という限定が外れました — [Claude に CLI からコンピュータを使用させる](https://code.claude.com/docs/ja/computer-use#stop-at-any-time) / [Let Claude use your computer from the CLI](https://code.claude.com/docs/en/computer-use#stop-at-any-time)
- **Agent SDK のインプロセス MCP サーバーの扱いが反転しました**。接続タイミング表の該当行が「**いいえ。最初のターンを遅延させない**」から「**はい。接続してツールをリストするまで**」に変わり、タイムアウト欄も「なし」から「接続とツールリスティングのリクエストがそれぞれ独自のタイムアウトを持つ」になりました — [MCP を使用して外部ツールに接続する](https://code.claude.com/docs/ja/agent-sdk/mcp#connection-timing) / [Connect to external tools with MCP](https://code.claude.com/docs/en/agent-sdk/mcp#connection-timing)
- **Python SDK で出力スタイルをプログラムから選べることが明記されました**。従来は「Python SDK にはプログラムで出力スタイルを選ぶオプションがない」と書かれていましたが、**`settings` オプションに `'{"outputStyle": "Explanatory"}'` のような JSON 文字列か設定ファイルのパスを渡す**方法に置き換わっています — [システムプロンプトの変更](https://code.claude.com/docs/ja/agent-sdk/modifying-system-prompts#activate-an-output-style) / [Modifying system prompts](https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts#activate-an-output-style)
- **Python SDK リファレンスで型と既定の記述が 5 か所直りました**。`ContentBlock` の union に **`ServerToolUseBlock` と `ServerToolResultBlock` が追加**され、`set_permission_mode` の引数型が `str` から `PermissionMode` になり、`SandboxNetworkConfig` の `allowUnixSockets` に「**macOS のみ。Linux では無視される**」が付き、`SDKSessionInfo` の `custom_title` が「ユーザー設定のタイトル、無ければ自動生成のタイトル」に、`get_server_info()` が「利用可能なコマンドと出力スタイルを含む初期化情報」に変わりました — [Agent SDK reference - Python](https://code.claude.com/docs/en/agent-sdk/python#contentblock)
- **`effort` を指定しなかったときの解決先が変わりました**。`agent-sdk/agent-loop` では「両 SDK ともパラメータを未設定のままモデル既定に委ねる」から「**Claude Code が自分で努力レベルを解決する**（`Adjust effort level` の順序に従う）」へ、`agent-sdk/typescript` の `Options` 表では既定値の表記が `Model default` から `undefined` へ変わっています — [How the agent loop works](https://code.claude.com/docs/en/agent-sdk/agent-loop#effort-level) / [Agent SDK reference - TypeScript](https://code.claude.com/docs/en/agent-sdk/typescript#options)
- **SDK の `skills` 配列に載る条件が明示されました**。「定義したユーザー呼び出し可能スキル」から「**`description` または `when_to_use` フロントマターフィールドを持つ**ユーザー呼び出し可能スキル」へ絞られています。同ページでは `slash_commands` の説明も整理され、「ユーザー呼び出し可能スキルはこのリストと `skills` 配列の両方に現れる」「`slash_commands` はセッションで使える残りのコマンドを足す」という 2 文が削られて、`user-invocable: false` のスキルがどちらにも出ないという記述に一本化されました — [Extend agents with skills](https://code.claude.com/docs/en/agent-sdk/skills#confirm-skills-loaded)
- **`agent-sdk/streaming-output` から型定義のインライン掲載が外れました**。`StreamEvent` と `SDKPartialAssistantMessage` のコードブロック（約 26 行）が削除され、それぞれ Python / TypeScript リファレンスの該当アンカーへのリンクに置き換わっています。二重管理を解消する整理です — [Stream responses in real-time](https://code.claude.com/docs/en/agent-sdk/streaming-output#streamevent-reference)
- **`agent-sdk/plugins` で相対パスの基準が変わりました**。「現在の作業ディレクトリからの相対」から「**`cwd` オプションからの相対**」になっています — [Plugins in the SDK](https://code.claude.com/docs/en/agent-sdk/plugins#path-specifications)
- **ローカルバンドルのサイズ超過時の記述が 1 語変わりました**。100 MB 超のリポジトリのフォールバック説明で「スナップショットがまだ大きすぎる**場合のみ**失敗する」から「**場合は**失敗する」へ、`only` が削除されています。あわせてテレポート要件の表に「**v2.1.219 より前では、エラーはチェックアウト側のリポジトリ名を示さなかった**」という注記が加わりました — [Use Claude Code on the web](https://code.claude.com/docs/en/claude-code-on-the-web#send-local-repositories-without-github)

**バグ修正**

- **該当する項目はありません。** 今回の対象期間に changelog ページは 1 行も変わっておらず、修正を伝えるリリースエントリが届いていません。

**その他**

- **`agent-sdk/hooks` から、サブエージェントの無限ループ対策の項目が 1 つ削除されました**（「スポーンする前にフック入力にサブエージェント指標がないか確認する」）。残る 2 つ（共有変数やセッション状態で追跡する／最上位セッションにのみ hooks をスコープする）はそのままです。あわせて、Webhook の例から「未処理例外はエージェントを中断しうる」「失敗した Webhook がエージェントを止めるべきではない」といった理由説明が削られ、コメントが簡潔になりました — [Intercept and control agent behavior with hooks](https://code.claude.com/docs/en/agent-sdk/hooks#make-http-requests-from-hooks)
- **`agent-sdk/user-input` から Python の `can_use_tool` に関する注記（約 4 行）が削除されました**。有限メッセージストリームを渡すと権限コールバック実行前に入力ストリームが閉じる、という説明です。あわせてコールバックの説明から「クエリ自体がキャンセルされたときのみ SDK が待機を打ち切る」という一文が外れました — [Handle approvals and user input](https://code.claude.com/docs/en/agent-sdk/user-input#respond-to-tool-requests)
- **`agent-sdk/claude-code-features` から、`settingSources: ["project"]` を設定すればプロジェクトの `.claude/settings.json` の hooks が SDK で自動的に動く、という段落が削除されました** — [Use Claude Code features in the SDK](https://code.claude.com/docs/en/agent-sdk/claude-code-features#hooks)
- **`agent-sdk/agent-loop` で 2 か所の説明が簡潔化されました**。`worker_shutting_down` から「現在のターンの後にループが終わる」が外れてホスト終了・Remote Control 切断という条件だけになり、`error_during_execution` の例から `API failure` が外れて「キャンセルされたリクエスト」だけになっています — [How the agent loop works](https://code.claude.com/docs/en/agent-sdk/agent-loop#handle-the-result)
- **`mobile`・`desktop`・`web-quickstart`・`agent-sdk/overview` で 1 行ずつの字句修正がありました**。「セッション QR コード」→「QR コード」、「リポジトリピルの隣の **+**」→「選択したリポジトリの隣の **+**」、「ブラウザを開かずに」→「ターミナルから」、Agent SDK の説明文の語順整理です
- **見出しマップに 4 つの見出しが先行して届きました**。`workflows` の `When a run hits your usage limit`（h3）、`mcp` の `Credential variables that read as empty`（h4）、`gateways` の `Mark prices up`（h4）、`fast-mode` の `Use fast mode in cloud sessions`（h3）で、**4 つとも `llms-full.txt` の本文には 1 回も現れません**。前回の `goal` の 2 件が今回着地したのと入れ替わりに、**新しい持ち越しが 4 件**積まれた形です
- **`llms.txt` で日本語版と韓国語版の収録ページ数が 191 から 192 へ増えました**。`_llms/` の言語索引には **11 言語**が並んでおり、フランス語・ドイツ語・イタリア語・スペイン語・中国語（簡体／繁体）・ロシア語・ブラジルポルトガル語は従来から 192 です。**今回の 2 言語が追いついた結果、192 で揃ったのは 11 言語中 10 言語**になりました ―― **インドネシア語だけは 191 のまま**で、今回の差分にも含まれていません
- **見出しマップ先頭の自動生成スタンプが 2026年09月13日 20時22分28秒 UTC から 2026年09月15日 01時26分23秒 UTC へ**進みました。約 1 日 5 時間ぶんで、対象期間中に上流の再生成が走ったことを示します

**参考リンクについて**: **今回は日本語リンクを付けたものと付けなかったものが混在しています。** 作成時点で公開中の日本語版を実際に取得して確認した結果は次のとおりです。**反映済み（日本語リンクあり）**: `goal`（新設の 2 見出しとも全訳済み）・`advisor`（8 行の表と API エラーの記述を反映）・`vs-code`（Hooks / Permissions / エージェントマップ / 選択インジケータの変更をすべて反映）・`computer-use`（通知タイミングの変更を反映）・`agent-sdk/mcp`（接続タイミング表の反転を反映）・`agent-sdk/modifying-system-prompts`（Python の `settings` 経由の記述に差し替え済み）・`claude-code-on-the-web` の `/tasks` 削除箇所。**未反映または未確認（英語のみ）**: `skills`（claude.ai 同期スキルの節そのものが日本語版に存在しない）・`chrome`（プランモードの節が旧来の二分法のまま）・`claude-code-on-the-web` のバンドル制限とテレポート要件（`only` の削除も v2.1.219 の注記も未反映）・`agent-sdk/python`（`custom_title` の説明が旧版のまま）・Agent SDK のその他のページと `settings-reference`（未確認のため安全側で英語のみ）。**新着情報 3 ページの日本語版は HTTP 404 で存在しません。** **changelog ページへのリンクは本サマリの方針どおり付けていません**（今回は無変更のため、そもそも参照すべき変更がありません）。

## 新着情報

- [**2026年09月07日～11日(Week 37)**](./latest-detail.md#2026年09月07日11日week-37) ([English](https://code.claude.com/docs/en/whats-new/2026-w37)):  
  `llms.txt` に登録されたのみで、`llms-full.txt` に本文は届いていません。1 行説明は「`claude plugin eval` でプラグインをテストし、Claude Code デスクトップのペインを独立したウィンドウへ切り出す」で、**前者は 2 回前のサマリで扱った `plugin-evals` ページに対応**します
- [**2026年08月31日～09月04日(Week 36)**](./latest-detail.md#2026年08月31日09月04日week-36) ([English](https://code.claude.com/docs/en/whats-new/2026-w36)):  
  同じく登録のみ。1 行説明は「Claude Fable 5.1 へ切り替え、デスクトップでコンピュータ使用をバックグラウンド実行させ、Claude の編集をライブ `/diff` パネルで見る」で、**先頭の Fable 5.1 は今回の advisor ページの変更（ハイライト 2）と重なります**
- [**2026年08月24日～28日(Week 35)**](./latest-detail.md#2026年08月24日28日week-35) ([English](https://code.claude.com/docs/en/whats-new/2026-w35)):  
  同じく登録のみ。1 行説明は「Claude Code デスクトップアプリでターミナルセッションを再開し、Claude が下書きするフィードバックレポートを確認し、制限モードでセッションを開始する」で、**対象期間の 3 週間前**にあたる回です

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-09-13.md](./archives/latest/2026-09-13.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-09-13.md](./archives/latest-detail/2026-09-13.md)

<!--
base_commit: af4f9aea12060f28aec2b5eafd4af096eee2ec40
head_commit: a19a359d88d83c75d535255e4c3dd79daa4f181f
generated_at_full: 2026-09-15T15:09:06+09:00
-->
