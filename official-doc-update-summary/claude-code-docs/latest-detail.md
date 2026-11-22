---
対象期間: 2026年11月20日 〜 2026年11月21日
作成日: 2026-11-21
---

# Claude Code 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
**今回は、Claude の代わりに Web ページを読む組み込みのサブエージェント `web-fetch` が `tools-reference` に載り、同じページの WebFetch の節が、ドメインの許可・ブロックと、うまくいかないときの対処の表を中心に組み直されました。`sub-agents`・`hooks`・`permission-modes` にも `web-fetch` の例外が書き加えられています**。新規ページ・新着情報（whats-new）のページはなく、changelog も `llms.txt` も変わっていません。`llms-full.txt` では 205 ページのうち 8 ページの内容が変わりました。生の差分は 242 行（追加 163・削除 79）で、50 行以上変わったのは `tools-reference`（127 行）と `sub-agents`（69 行）の 2 ページです。総行数は 130,625 行から 130,709 行に増えました。

主要なものを以下に挙げます。

1. 組み込みのサブエージェント `web-fetch` が `tools-reference` の新しい h3 に載った。claude.ai のアカウントでサインインした v2.1.287 以降のセッションで使え、Claude は Agent ツールでこのサブエージェントに URL と質問を渡してページを読ませる。動くモデル・ルールとフックの効き方・オフにする方法の h4 もある
2. `tools-reference` の WebFetch の節が組み直され、ドメインの許可・ブロック・オフの表と、フェッチでプロンプトが出る・失敗する・WebFetch がないときの 15 行の対処の表ができた
3. auto モードの分類器が終わったサブエージェントの作業を確かめるのは、エージェントチームのチームメイト以外のサブエージェント、と明記された。`web-fetch` は条件を満たすと最初の 2 つの確認を省いて `dontAsk` モードで始まる
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**組み込みの web-fetch サブエージェントが載った**](#1-組み込みの-web-fetch-サブエージェントが載った):  
  `tools-reference` に h3「The web-fetch subagent」と 3 つの h4 ができ、Claude のために Web ページを読むサブエージェントの使える条件・見分け方・動くモデル・ルールとフックの効き方・オフにする方法が載りました。`sub-agents` の組み込みのサブエージェントの表と、`hooks`・`permission-modes`・`agent-sdk/python` にも、このサブエージェントの扱いが加わっています
2. [**WebFetch の節が許可・ブロック・対処の表に組み直された**](#2-webfetch-の節が許可ブロック対処の表に組み直された):  
  `tools-reference` の「WebFetch tool behavior」が書き直され、h3「WebFetch availability」だけだった下位の見出しが 5 つの h3 になりました。サブドメインを許す `WebFetch(domain:*.example.com)` の行や、`Ctrl+O` で Claude が尋ねたことと答えを見る方法、現象ごとの対処の表が載っています
3. [**auto モードの分類器がサブエージェントを確かめる範囲が明記された**](#3-auto-モードの分類器がサブエージェントを確かめる範囲が明記された):  
  `permission-modes` の「How auto mode handles subagents」で、3 つの確認は Claude が Agent ツールで始めたサブエージェントが対象で、終わったときの確認はエージェントチームのチームメイトには当てはまらない、と明記されました。`web-fetch` が最初の 2 つの確認を省く条件も加わっています
<!-- light:highlight-list:end -->

## 1. 組み込みの web-fetch サブエージェントが載った

**`tools-reference` に h3「The web-fetch subagent」（id は `#web-fetch-subagent`）ができました。** `web-fetch` は、Claude のために Web ページを読む、Claude Code に組み込まれたサブエージェントです。Claude はページが要ると、Agent ツールで `web-fetch` に URL とページについての質問を渡し、サブエージェントが WebFetch を呼んでページを読み、答えを Claude に返します。

- **使える条件**: claude.ai のアカウントでサインインし、Claude Code が v2.1.287 以降なら、セッションでこのサブエージェントを使える。使えないときは Claude が自分で WebFetch を呼び、Claude Code がバックグラウンドのタスクに使うモデルがページを読む。サブエージェントがオフになる構成として、自分でオフにしたとき、v2.1.330 以降で LLM ゲートウェイ経由で接続するとき、Amazon Bedrock や `DISABLE_TELEMETRY` を設定したときのように Claude Code がフィーチャーフラグを取得しないときが挙がっている
- **見分け方**: ターミナルでは、許可のプロンプトの題が `Fetch · from the web-fetch agent` になり、`Received` で始まる行は `Received 87 bytes` のようにサイズだけを示す。VS Code では **Agent** の行、Desktop アプリと claude.ai/code ではサブエージェントのペインを開く行として出る。`claude -p` と Agent SDK では、`system/init` のイベントの `agents` に `web-fetch` が載り、`tools` に `WebFetch` が載らない
- **h4「Which model the web-fetch subagent runs on」**: 既定では `haiku` のモデルエイリアスが指すモデルで動く。`availableModels` の許可リストがそのモデルを外しているなど、そのモデルを使えなければ、サブエージェントを始めた会話と同じモデルで動く。自分で選ぶなら、`sub-agents` の「Run every subagent on one model」に従う
- **h4「Rules, hooks, and CLAUDE.md with the web-fetch subagent」**: `WebFetch` の権限のルールと、`WebFetch` に合う `PreToolUse`・`PostToolUse` のフックは、このサブエージェントが取るページにも効く。表は 4 つの場合を挙げる
  - CLAUDE.md の指示でフェッチするページを決めているなら、サブエージェントは組織の managed のものも含めて CLAUDE.md なしで始まるので、`WebFetch` の権限のルールで絞る
  - `SubagentStart`・`SubagentStop` のフックは、managed settings で定義したものだけがこのサブエージェントで動くので、ほかの設定ファイルでは `WebFetch` に合う `PreToolUse`・`PostToolUse` のフックを使う
  - `WebFetch` の結果を解析する `PostToolUse` のフックは、サブエージェントでは結果がページのテキスト、Claude が自分で WebFetch を呼ぶと Claude の質問への答えになるので、両方を扱う
  - `Agent` の呼び出しを止める `PreToolUse` のフックがあると、Claude がサブエージェントを Agent ツールで始めるのでページが取れない。この場合はサブエージェントをオフにする
- **h4「Turn off the web-fetch subagent」**: 設定ファイル（組織全体なら managed settings）の `permissions.deny` に `Agent(web-fetch)` を加える。確かめるには、新しいセッションでページを取らせ、上の見分け方の印が出ないことを見る。`system/init` のイベントでは `tools` に `WebFetch` が戻り、`agents` には `web-fetch` が残る。組織が `allowManagedPermissionRulesOnly` を設定していれば、自分の設定ファイルの deny のルールは無視されるので、管理者に managed settings へ加えてもらう

ほかのページにも、このサブエージェントの扱いが書き加えられました。

- **`sub-agents`**: 「Built-in subagents」の Other のタブの表に `web-fetch` の行（モデルは Haiku か、Haiku を使えなければ始めた会話のモデル。このサブエージェントを使うセッションで Claude が Web ページを読むときに使う）が加わった。「Available tools」には、`web-fetch` でページを読むセッションでは、メインの会話・フォーク・チームメイトが自分の `WebFetch` のツールを持たず、Claude が Agent ツールで始めるほかのサブエージェントは自分で `WebFetch` を呼べる、という注記が加わった。ほかの 5 か所でも `web-fetch` が例外として挙がっている（下の「大幅に更新されたページ」の 2）
- **`hooks`**: 「SubagentStart」と「SubagentStop」に、`web-fetch` には managed settings の `SubagentStart`・`SubagentStop` のフックだけが動き、ほかの場所に置くフックなら、代わりに `WebFetch` に合う `PreToolUse`（SubagentStart の代わり）か `PostToolUse`（SubagentStop の代わり）のフックを使う、という注記が加わった
- **`permission-modes`**: auto モードの分類器の確認を省く条件（ハイライト 3）
- **`agent-sdk/python`**: WebFetch の出力の `result` の注釈が、「内容にプロンプトを当てた処理済みの結果」から「プロンプトへの答えか、ページのテキスト」になった

changelog には `web-fetch` の語は出てきません（base・head とも 0 件）。

- [ツールリファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/tools-reference#web-fetch-subagent)
- [Tools reference - Claude Code Docs (English)](https://code.claude.com/docs/en/tools-reference#web-fetch-subagent)
- [カスタムサブエージェントの作成 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/sub-agents#built-in-subagents)
- [Create custom subagents - Claude Code Docs (English)](https://code.claude.com/docs/en/sub-agents#built-in-subagents)

## 2. WebFetch の節が許可・ブロック・対処の表に組み直された

**`tools-reference` の「WebFetch tool behavior」が書き直され、h3「WebFetch availability」だけだった下位の見出しが、「Allow a domain」「Block a site or turn WebFetch off」「When a fetch prompts, fails, or WebFetch is missing」「The web-fetch subagent」「Identify WebFetch requests to your site」の 5 つの h3 になりました。** 3 つ目は HTML の id が `#webfetch-availability` のままなので、「WebFetch availability」を改称したものです。冒頭の段落は、Claude は Web ページで何かを調べるのに WebFetch を使い、URL はユーザーからも Claude（たとえば WebSearch の結果）からも来る、ほとんどのページで Claude は全文を見ず、ページについて質問し、別のモデルの呼び出しがページを読んで答えを返す、という説明になりました。

- **Allow a domain**: ターミナルと VS Code のセッションは既定で auto モードで始まり、auto モードでは `ask` のルールに合うドメインを除いてフェッチの前にプロンプトが出ない。代わりに分類器がフェッチを確かめ、止めることがある。Manual と `acceptEdits` のモードでは許可を求める。前もって許可するには、設定ファイルに allow のルールを加えるか、プロンプトで **Yes, and don't ask again for `<domain>`** を選ぶ。`/permissions` でルールと、そのルールがどの設定から来るかを確かめられる。ルールの表は、1 つのドメインなら `WebFetch(domain:example.com)`、そのサブドメインなら `WebFetch(domain:*.example.com)`、すべてのサイトなら `WebFetch` か `WebFetch(domain:*)`（違いは `permissions` の「Allow or deny every fetch」）。`domain:` の allow のルールがあれば、サンドボックスの中の Bash のコマンドもそのドメインに届く（サンドボックスのロックがルールを無視させる場合を除く）
- **Block a site or turn WebFetch off**: ドメインを止めるなら `deny`、プロンプトを求めるなら `ask` に `WebFetch(domain:...)` のルールを加える。WebFetch をオフにするなら `deny` に `WebFetch` を加えるか、`CLAUDE_CODE_DISABLE_WEB_FETCH` を `1` にする。組織全体に当てはめるなら managed settings に置く。サンドボックスの外で Bash が許されていれば、Claude は `curl` や `wget` などでどの URL にも届く、という注意もある
- **When a fetch prompts, fails, or WebFetch is missing**: Claude の返答は、Claude が尋ねなかったページの内容を落とすことがあり、ターミナルでは `Ctrl+O` で Claude が尋ねたことと受け取った答えを見られる。続く 15 行の表が、気づいた現象ごとの対処を挙げる。これまでの箇条書きと段落にあった、localhost とドットのないホスト名の拒否・100,000 文字の上限・15 分のキャッシュ・5 分の期限・別のホストへのリダイレクト・ドメインの安全性チェック・サンドボックスの `allowedDomains`・事前承認のドメイン・claude.ai のアーティファクトのリンク・組織のポリシーの説明は、この表の行に移った
- **Identify WebFetch requests to your site**: `Claude-User` で始まる `User-Agent` と、HTML より Markdown を好む `Accept` のヘッダーの説明（これまでの本文の文がそのままこの h3 に移った）

対処の表で新しく載った説明には、次のものがあります。

- **長いページ**: `web-fetch` サブエージェントは約 48,000 文字までのページを全文読み、Claude が WebFetch を呼ぶと最初の 100,000 文字を読む（次の部分を取らせるのに v2.1.290 以降が要る、という点はこれまでと同じ）
- **リダイレクト**: ホストが `www.` を足すか外す以上に変わると、WebFetch は新しい URL を返し、ページの内容は返さない
- **クラウドのセッション**: ネットワークがドメインを止めていれば、allow のルールに加えて、クラウドの環境のネットワークアクセスにもドメインを加える
- **auto モード**: プロンプトなしにフェッチが止められたら、ドメインの allow のルールを加えるか、分類器が止めたものなら、ターミナルの `/permissions` の **Recently blocked** のタブで承認して Claude に再試行させる
- **`claude -p` と Agent SDK**: これらは Manual モードで始まり、承認の要る呼び出しは拒まれるので、allow のルールを加えるか auto モードで始める
- **自分の設定のルールが効かない**: 組織が `allowManagedPermissionRulesOnly` を設定していると無視されるので、管理者に managed settings へ加えてもらう
- **どのページも取れない**: `/status` の `Organization configuration` の行に `HIPAA` があれば WebFetch はオフ（`Organization policy` の行がポリシーを読めなかったと報告して web fetch を名指すときの説明は、これまでの段落から移ったもの）

一方、これまでの本文にあって、新しい節に見当たらない説明もあります。HTTP の URL を HTTPS に上げる、Markdown への変換は設定できない、許可のプロンプトの 3 つの選択肢（**Yes** はこのフェッチだけを許す、など）、明示の `WebFetch(domain:...)` のルールが事前承認のドメインより優先する、という文（表は、プロンプトを求めるなら `ask` のルールを加える、と述べる）、抽出の段階で API が混んでいれば間を置いて再試行する、Team か Enterprise の claude.ai のアカウントで組織のポリシーを `api.anthropic.com` から取得する、セッションの外では `claude doctor` が同じ行を出す、などです。キャッシュの長さ・ダウンロードの期限・WebFetch をオフにする変数が要る版（v2.1.233・v2.1.268・v2.1.285）もこの節から外れましたが、`env-vars` の各変数の行には残っています。

- [ツールリファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/tools-reference#allow-a-domain)
- [Tools reference - Claude Code Docs (English)](https://code.claude.com/docs/en/tools-reference#allow-a-domain)
- [ツールリファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/tools-reference#webfetch-availability)
- [Tools reference - Claude Code Docs (English)](https://code.claude.com/docs/en/tools-reference#webfetch-availability)

## 3. auto モードの分類器がサブエージェントを確かめる範囲が明記された

**`permission-modes` の「How auto mode handles subagents」（アコーディオン）で、分類器がサブエージェントの作業を 3 つの時点で確かめるのは、Claude が Agent ツールでサブエージェントを始めたとき、と明記されました。** 3 つ目の、サブエージェントの作業と最終の報告を親が読む前に確かめる時点も、「サブエージェントが終わると」から「エージェントチームのチームメイト以外のサブエージェントが終わると」になりました。分類器が作業か報告を指摘したとき、または別の API の安全性チェックがレビューを拒んだときは、報告にセキュリティの警告を前に付けて届け、分類器を使えないときは、作業を確かめるよう促すメモ付きで届ける、という説明は、別の段落に分かれて残っています。

新しい段落は、`web-fetch` サブエージェントについて、`WebFetch(domain:...)` の allow のルールか事前承認のドメインがタスクのすべての URL を覆っていれば、Claude Code は最初の 2 つの確認（始める前のタスクの説明の評価と、実行中の各アクションの評価）を省くことがある、とします。そのときサブエージェントは `dontAsk` モードで始まるので、承認の要るほかのフェッチは拒まれます。3 つ目の確認は引き続き動きます。

`sub-agents` の「Permission modes」でも、メインの会話が auto モードのときの説明が 2 つの段落に分かれ、Claude が Agent ツールで始めたサブエージェントが終わると、分類器が報告を届ける前にその作業と最終の報告も確かめ、このレビューはエージェントチームのチームメイト以外のサブエージェントに対して動く、となりました。

- [権限モードを選択する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/permission-modes#how-auto-mode-evaluates-actions)
- [Choose a permission mode - Claude Code Docs (English)](https://code.claude.com/docs/en/permission-modes#how-auto-mode-evaluates-actions)
- [カスタムサブエージェントの作成 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/sub-agents#permission-modes)
- [Create custom subagents - Claude Code Docs (English)](https://code.claude.com/docs/en/sub-agents#permission-modes)

## 新規追加されたページ

<!-- light:new-pages:start -->
（今回の対象期間に新規追加されたドキュメントページはありません。`llms.txt` は変わっておらず、`llms-full.txt` の `Source:` の行も 208、固有のページも 205 のままです）
<!-- light:new-pages:end -->

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
- [**Tools reference**](#1-tools-reference) ([日本語](https://code.claude.com/docs/ja/tools-reference#webfetch-tool-behavior) / [English](https://code.claude.com/docs/en/tools-reference#webfetch-tool-behavior)):  
  127 行（追加 99・削除 28）が変わりました。ほとんどは「WebFetch tool behavior」の書き直しと `web-fetch` サブエージェントの h3 で（詳細はハイライト 1・2 参照）、ほかに Agent ツール・バックグラウンドのコマンド・Monitor・WebSearch の節から 1 文ずつが外れました
- [**Create custom subagents**](#2-create-custom-subagents) ([日本語](https://code.claude.com/docs/ja/sub-agents#restrict-which-tools-a-subagent-can-use) / [English](https://code.claude.com/docs/en/sub-agents#restrict-which-tools-a-subagent-can-use)):  
  69 行（追加 35・削除 34）が変わりました。`web-fetch` を例外として挙げる記述が 7 か所に加わり、`tools` で Edit と Write を外しても Bash でファイルを変えられる、という注意が 2 か所に入りました。残りの多くは、節の導入や補足の文を外す推敲です
<!-- light:updated-pages:end -->

**行数の数え方**: `llms-full.txt` の生の差分のハンクを、追加行は head 側、削除行は base 側の `Source:` 行でページに振り分けた値です。ページの並びは変わっておらず、ページ単位の合計は生の差分（追加 163・削除 79）と一致します。大幅更新の 2 ページに次いで多いのは `hooks` の 28 行（追加 18・削除 10）で、ほかの 5 ページはどれも 8 行以下です。changelog は変わっていません。

## 1. Tools reference

**`tools-reference` は 127 行（追加 99・削除 28）が変わりました。** ほとんどは「WebFetch tool behavior」の節で、h3「WebFetch availability」だけだった下位の見出しが、5 つの h3 と、h3「The web-fetch subagent」の下の 3 つの h4 になりました（内容はハイライト 1・2）。見出しの文字列としては 8 つ加わり 1 つ外れましたが、「When a fetch prompts, fails, or WebFetch is missing」が「WebFetch availability」の id を引き継いでいるので、7 つの追加と 1 つの改称です。

ほかの節では、次の文が外れました。

- **「Agent tool behavior」**: サブエージェントが `maxTurns` の上限に達すると、Claude Code は返す結果を部分的な出力と印し、Claude はサブエージェントを再開して続けられる
- **「Foreground commands that move to the background」**: バックグラウンドへ移ったコマンドの時間の上限は移った時点から数え、フォアグラウンドのサブエージェントの移ったコマンドは、そのサブエージェントの実行が終わると止まる
- **「Monitor tool」**: 同じセッションで作業を続けられ、出来事が届くと Claude が割り込む
- **「WebSearch tool behavior」**: 1 回の呼び出しで最大 8 回の検索をする、という文から、結果を返す前に内部で検索を絞り込む、という部分

- [ツールリファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/tools-reference#webfetch-tool-behavior)
- [Tools reference - Claude Code Docs (English)](https://code.claude.com/docs/en/tools-reference#webfetch-tool-behavior)

## 2. Create custom subagents

**`sub-agents` は 69 行（追加 35・削除 34）が変わりました。** 見出しの増減はありません。

- **`web-fetch` の例外（7 か所）**: 「Built-in subagents」の Other のタブの表の行と「Available tools」の注記（ハイライト 1）に加え、次の 5 か所で `web-fetch` が例外として挙がった
  - 「When an allowlist blocks a subagent model」: 許可リストがモデルを止めたときに代わりのモデルを選ぶ順は、`web-fetch` 以外のサブエージェントのもの、となった
  - 「Project-level hooks for subagent events」: 節の末尾で、フックの設定の形式とともに、例外として `web-fetch` サブエージェントを見るよう案内する
  - 「Which subagents run in the background」: 何も設定しなければ、メインの会話から Claude が始める `web-fetch` 以外のサブエージェントはバックグラウンドで始まる
  - 「What loads at startup」: CLAUDE.md を読み込まない組み込みのエージェントが、Explore と Plan から Explore・Plan・`web-fetch` になった
  - 「Turn fork mode off」（id は `#turn-fork-mode-on-or-off`）: fork モードの間、手元のターミナル・VS Code・デスクトップのセッションで Claude が待てないのは、`web-fetch` 以外のサブエージェント、となった
- **Bash でファイルを変えられる**: 「Restrict which tools a subagent can use」の、Read・Grep・Glob・Bash だけを許す例の説明が、「ファイルの編集も書き込みも MCP のツールもできない」から「Edit・Write・MCP のツールはないが、Bash でファイルを変えられる」になった。「Code reviewer」の例の説明も、「コードを変えずにレビューする読み取り専用のサブエージェント」から「Edit と Write のツールなしでコードをレビューするサブエージェント。Bash でファイルを変えることはできる」になった
- **auto モード**: 「Permission modes」の auto モードの説明（ハイライト 3）
- **言い方の変化**: frontmatter の `background` で、既定でバックグラウンドで始まるのが「Claude がメインの会話から始めるサブエージェント」から「Claude がメインの会話から始めるカスタムのサブエージェント」になった。「Define hooks for subagents」で、サブエージェントの中でも効くのが「設定ファイル・managed policy の設定・プラグインのフック」から「それらのツールのイベントのフック」になった。「Project-level hooks for subagent events」の例は、片付けのスクリプトを「どのサブエージェントが止まっても」から「サブエージェントが止まると」動かす、となった
- **外れた文**
  - 「Built-in subagents」: Explore と Plan 以外の組み込みのサブエージェントとカスタムのサブエージェントは CLAUDE.md と git status を読み込み、カスタムのサブエージェントは `omitClaudeMd` で CLAUDE.md なしに始められる、という文と、Other のタブの、これらは普通は自動で呼ばれるので直接使う必要はない、という文
  - 「Define hooks for subagents」: `settings.json` の項目の、`SubagentStart` と `SubagentStop` はサブエージェントが始まるときと終わるときに発火する、という部分
  - 「Hooks in subagent frontmatter」: これらのフックはそのサブエージェントが動く間だけ動き、終わると片付けられる、という文と、サブエージェントとして呼ばれると frontmatter の `Stop` のフックは自動で `SubagentStop` のイベントに変わる、という文（後者は、同じページのイベントの表の `Stop` の行に「実行時に `SubagentStop` に変わる」として残っている）
  - 「API errors in subagents」: 応答が途中で切れ、その部分の応答にテキストがありツールの呼び出しがなければ、Claude Code はサブエージェントに続けるよう促す、という段落（`errors` の同じ説明は残っている）
  - 「Concurrent subagent limit」: 2 つの上限がそれぞれの変数を持つ、という冒頭の段落。セッションを通じたサブエージェントの総数に上限はない、という文は節の末尾へ移った
  - 「What loads at startup」: 組み込みのエージェントは決まったプロンプトを持つ、という文と、git status を省くのは Explore と Plan だけ、という文（同じ節の Git status の項目の、Explore と Plan はいずれにせよ省く、という記述は残っている）
  - 「Database query validator」: フックは標準入力で JSON を受け取り、Bash のコマンドは `tool_input.command` にあり、終了コード 2 で操作を止めてエラーのメッセージを Claude に返す、という説明
  - そのほか、節の導入や例の補足の文が外れた（「Built-in subagents」の末尾、「Quickstart: create your first subagent」「Configure subagents」「Scope MCP servers to a subagent」「Persistent memory tips」「Run parallel research」「Fork the current conversation」「Debugger」「Data scientist」）

- [カスタムサブエージェントの作成 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/sub-agents#restrict-which-tools-a-subagent-can-use)
- [Create custom subagents - Claude Code Docs (English)](https://code.claude.com/docs/en/sub-agents#restrict-which-tools-a-subagent-can-use)
- [カスタムサブエージェントの作成 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/sub-agents#which-subagents-run-in-the-background)
- [Create custom subagents - Claude Code Docs (English)](https://code.claude.com/docs/en/sub-agents#which-subagents-run-in-the-background)

## 軽微な更新

<!-- light:minor-updates:start -->
今回の差分は **2 ファイル**（`llms-full.txt`・見出しマップ）で、`llms.txt` は変わっていません。`llms-full.txt` では、205 ページのうち **8 ページ**の内容が変わりました。大幅更新の 2 ページを除く **6 ページ**（`hooks`・`permission-modes`・`env-vars`・`vs-code`・`agent-sdk/hooks`・`agent-sdk/python`）を以下にまとめます。changelog は変わっておらず（収録 446 リリース、先頭は v2.1.330）、新着情報（whats-new）のページもありません。

`llms-full.txt` の総行数は **130,625 行から 130,709 行へ 84 行増え**ました（生の差分の差し引き 163 − 79 と一致）。`llms-full.txt` に 2 回載っているページ（`plugins/create`・`plugins/install`・`plugins/mods/overview`）は変わっていません。

コードフェンスの外の見出しは、行頭が `#` の見出しだけを数えると 6,188 から 6,195 へ、引用の中の見出しも数えると 6,199 から 6,206 へ、どちらも 7 増えました。すべて `tools-reference` の WebFetch の節の変化で、文字列としては h3 の「Allow a domain」「Block a site or turn WebFetch off」「When a fetch prompts, fails, or WebFetch is missing」「The web-fetch subagent」「Identify WebFetch requests to your site」と h4 の「Which model the web-fetch subagent runs on」「Rules, hooks, and CLAUDE.md with the web-fetch subagent」「Turn off the web-fetch subagent」の 8 つが加わり、h3「WebFetch availability」が外れました。HTML の id で見ると、「When a fetch prompts, fails, or WebFetch is missing」は「WebFetch availability」の改称です（ハイライト 2）。

**新機能**

- 組み込みの `web-fetch` サブエージェント（`tools-reference`・`sub-agents`・`hooks`・`permission-modes`・`agent-sdk/python`。詳細はハイライト 1 参照）
- **`hooks` に `web-fetch` サブエージェントのフックの注記が載った**（「SubagentStart」「SubagentStop」）。`web-fetch` には managed settings で定義した `SubagentStart`・`SubagentStop` のフックだけが動きます。ほかの場所に置くフックなら、`SubagentStart` の代わりに `WebFetch` に合う `PreToolUse` のフックを、`SubagentStop` の代わりに `WebFetch` に合う `PostToolUse` のフックを使います — [日本語](https://code.claude.com/docs/ja/hooks#subagentstart) / [English](https://code.claude.com/docs/en/hooks#subagentstart)、[日本語](https://code.claude.com/docs/ja/hooks#subagentstop) / [English](https://code.claude.com/docs/en/hooks#subagentstop)

**機能改善**

- auto モードの分類器がサブエージェントを確かめる範囲と、`web-fetch` が最初の 2 つの確認を省く条件（`permission-modes`・`sub-agents`。詳細はハイライト 3 参照）
- **WebFetch の結果の説明が改められた**（`agent-sdk/python` の「WebFetch」）。出力の `result` の注釈が、「内容にプロンプトを当てた処理済みの結果」から「プロンプトへの答えか、ページのテキスト」になりました。`web-fetch` サブエージェントが呼ぶと結果がページのテキストになる、というハイライト 1 の説明と対応します — [日本語](https://code.claude.com/docs/ja/agent-sdk/python#webfetch) / [English](https://code.claude.com/docs/en/agent-sdk/python#webfetch)
- **`CLAUDE_CODE_FORK_SUBAGENT` の説明が改められた**（`env-vars`）。fork モードの間は手元のターミナル・VS Code・デスクトップのセッションで Claude がサブエージェントを待てない、という文が外れ、`0` にすると fork モードがオフになる（たとえば Claude にサブエージェントを待たせるため）、という書き方になりました。同じ表の `CLAUDE_CODE_WEBFETCH_CACHE_TTL_MS` も、キャッシュに保つのが「取得した各 URL の応答」から「取得した各ページ」になっています — [日本語](https://code.claude.com/docs/ja/env-vars#variables) / [English](https://code.claude.com/docs/en/env-vars#variables)
- **VS Code の Run in background のアクションの説明が改められた**（`vs-code` の「The Run in background action is missing under a subagent」）。VS Code で既定でこのアクションを出さないのが、「サブエージェント」から「ほとんどのサブエージェント」になりました — [日本語](https://code.claude.com/docs/ja/vs-code#the-run-in-background-action-is-missing-under-a-subagent) / [English](https://code.claude.com/docs/en/vs-code#the-run-in-background-action-is-missing-under-a-subagent)

**その他**

- **`hooks` の外れた文**: 「Notification」の、`elicitation_dialog` と `elicitation_url_dialog` は `permission_prompt` と同じ 6 秒の待ちを共有し、ダイアログが出たときから数え、キーを打つたびに延びる、という文（約 6 秒入力がなければ、という部分は残っている）。「Notification input」の、デスクトップの通知の例は `terminalSequence` に頼る、という部分と、Notification のフックは通知を外部のサービスへ転送するような副作用のためのもの、という文。「SubagentStart input」の、起動時に入れたコピーはそのまま残り、サブエージェントのプロンプトのキャッシュを保つ、という文。「SubagentStop input」の、`agent_type` がマッチャーの絞り込みに使う値、という文と、フックはトランスクリプトのファイルを解析せずに最後の応答を読める、という部分。同じ節の決定制御の説明の、終了コード 2 で止めるフックは標準エラーのメッセージを同じように渡す、という文。「StopFailure」の、レート制限や認証の問題などの API のエラーで、という部分と、「StopFailure input」の、通知とログのためだけに動く、という文。「PostCompact input」の、圧縮の結果には影響できないが後続の作業はできる、という文 — [日本語](https://code.claude.com/docs/ja/hooks#subagentstop-input) / [English](https://code.claude.com/docs/en/hooks#subagentstop-input)
- **言い方の変化**: `hooks` の「Notification」で、ほかのダイアログが出ている間に届いた要求も保つのが「同じ 6 秒のゲート」から「同じ 6 秒のタイミング」になり、「SubagentStop input」の、内部のエージェントでも SubagentStop が発火する、という段落は「すべての SubagentStop が Claude の始めたサブエージェントから来るわけではない」という前置きが外れた。`agent-sdk/hooks` の「Track subagent activity」の例は、要約をログに残すのが「サブエージェントが終わるたびに」から「サブエージェントが終わったときに」になった — [日本語](https://code.claude.com/docs/ja/agent-sdk/hooks#track-subagent-activity) / [English](https://code.claude.com/docs/en/agent-sdk/hooks#track-subagent-activity)
<!-- light:minor-updates:end -->

見出しマップ（`en/claude_code_docs_map.md`）は、更新時刻が 2026年11月21日 00:18:19 UTC から 2026年11月21日 17:01:04 UTC に替わり、9 行が加わり 2 行が外れました（6,666 行から 6,673 行）。加わったのは `tools-reference` の WebFetch の節の 8 つの見出しと新しいスタンプで、外れたのは「WebFetch availability」と古いスタンプです。`llms-full.txt` の見出しの増減と一致し、今回、見出しマップにだけ先に載った見出しはありません。

**参考リンクについて**: 日本語版は、今回リンクを付けたページの HTML を取得し、新しい節の id があるか、今回の差分で出入りしたコードの字句（`web-fetch`・`WebFetch(domain:*.example.com)`・`Fetch · from the web-fetch agent`・`Received 87 bytes`・版の数字・リンク先のアンカーなど。base と head の `llms-full.txt` で数が違うものだけ）が英語版と同じだけあるかで、今回の内容になっているかを確かめました。地の文だけが変わった箇所（`tools-reference` の対処の表、`sub-agents` の Bash でファイルを変えられる、という注意と「Permission modes」、`permission-modes` のアコーディオン、`hooks` の外れた文、`env-vars`・`vs-code`・`agent-sdk/hooks` の言い方、`agent-sdk/python` のコードの注釈）は、該当する箇所の訳文で確かめています。今回リンクを付けたページは、すべて今回の内容になっていました。アンカーは英語版・日本語版の HTML の見出しの id で確かめました。`tools-reference` の「When a fetch prompts, fails, or WebFetch is missing」は旧見出しの id `#webfetch-availability` を、「The web-fetch subagent」は `#web-fetch-subagent` を持ちます。`permission-modes` の「How auto mode handles subagents」は見出しではなくアコーディオンなので、それを含む h3「How auto mode evaluates actions」にリンクしています。**changelog ページへのリンクは、本サマリの方針どおり付けていません。**

## 新着情報

<!-- light:whats-new:start -->
（今回の差分に新着情報（`whats-new/`）のページはありません。head の `llms.txt`・`llms-full.txt`・見出しマップにも whats-new のページは載っていません）
<!-- light:whats-new:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-11-20.md](./archives/latest/2026-11-20.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-11-20.md](./archives/latest-detail/2026-11-20.md)

<!--
base_commit: 5f51174830a6109f6c27c1eeae6dd98de6f65dde
head_commit: 3279a161e968357548276a7baa091d6d6f481473
generated_at_full: 2026-11-22T15:14:02+09:00
-->
