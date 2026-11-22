---
対象期間: 2026年11月20日 〜 2026年11月21日
作成日: 2026-11-21
---

# Claude Code 公式ドキュメント更新サマリ

```markdown
**今回は、Claude の代わりに Web ページを読む組み込みのサブエージェント `web-fetch` が `tools-reference` に載り、同じページの WebFetch の節が、ドメインの許可・ブロックと、うまくいかないときの対処の表を中心に組み直されました。`sub-agents`・`hooks`・`permission-modes` にも `web-fetch` の例外が書き加えられています**。新規ページ・新着情報（whats-new）のページはなく、changelog も `llms.txt` も変わっていません。`llms-full.txt` では 205 ページのうち 8 ページの内容が変わりました。生の差分は 242 行（追加 163・削除 79）で、50 行以上変わったのは `tools-reference`（127 行）と `sub-agents`（69 行）の 2 ページです。総行数は 130,625 行から 130,709 行に増えました。

主要なものを以下に挙げます。

1. 組み込みのサブエージェント `web-fetch` が `tools-reference` の新しい h3 に載った。claude.ai のアカウントでサインインした v2.1.287 以降のセッションで使え、Claude は Agent ツールでこのサブエージェントに URL と質問を渡してページを読ませる。動くモデル・ルールとフックの効き方・オフにする方法の h4 もある
2. `tools-reference` の WebFetch の節が組み直され、ドメインの許可・ブロック・オフの表と、フェッチでプロンプトが出る・失敗する・WebFetch がないときの 15 行の対処の表ができた
3. auto モードの分類器が終わったサブエージェントの作業を確かめるのは、エージェントチームのチームメイト以外のサブエージェント、と明記された。`web-fetch` は条件を満たすと最初の 2 つの確認を省いて `dontAsk` モードで始まる
```

## ハイライト

1. [**組み込みの web-fetch サブエージェントが載った**](./latest-detail.md#1-組み込みの-web-fetch-サブエージェントが載った):  
  `tools-reference` に h3「The web-fetch subagent」と 3 つの h4 ができ、Claude のために Web ページを読むサブエージェントの使える条件・見分け方・動くモデル・ルールとフックの効き方・オフにする方法が載りました。`sub-agents` の組み込みのサブエージェントの表と、`hooks`・`permission-modes`・`agent-sdk/python` にも、このサブエージェントの扱いが加わっています
2. [**WebFetch の節が許可・ブロック・対処の表に組み直された**](./latest-detail.md#2-webfetch-の節が許可ブロック対処の表に組み直された):  
  `tools-reference` の「WebFetch tool behavior」が書き直され、h3「WebFetch availability」だけだった下位の見出しが 5 つの h3 になりました。サブドメインを許す `WebFetch(domain:*.example.com)` の行や、`Ctrl+O` で Claude が尋ねたことと答えを見る方法、現象ごとの対処の表が載っています
3. [**auto モードの分類器がサブエージェントを確かめる範囲が明記された**](./latest-detail.md#3-auto-モードの分類器がサブエージェントを確かめる範囲が明記された):  
  `permission-modes` の「How auto mode handles subagents」で、3 つの確認は Claude が Agent ツールで始めたサブエージェントが対象で、終わったときの確認はエージェントチームのチームメイトには当てはまらない、と明記されました。`web-fetch` が最初の 2 つの確認を省く条件も加わっています

## 新規追加されたページ

（今回の対象期間に新規追加されたドキュメントページはありません。`llms.txt` は変わっておらず、`llms-full.txt` の `Source:` の行も 208、固有のページも 205 のままです）

## 大幅に更新されたページ

- [**Tools reference**](./latest-detail.md#1-tools-reference) ([日本語](https://code.claude.com/docs/ja/tools-reference#webfetch-tool-behavior) / [English](https://code.claude.com/docs/en/tools-reference#webfetch-tool-behavior)):  
  127 行（追加 99・削除 28）が変わりました。ほとんどは「WebFetch tool behavior」の書き直しと `web-fetch` サブエージェントの h3 で（詳細はハイライト 1・2 参照）、ほかに Agent ツール・バックグラウンドのコマンド・Monitor・WebSearch の節から 1 文ずつが外れました
- [**Create custom subagents**](./latest-detail.md#2-create-custom-subagents) ([日本語](https://code.claude.com/docs/ja/sub-agents#restrict-which-tools-a-subagent-can-use) / [English](https://code.claude.com/docs/en/sub-agents#restrict-which-tools-a-subagent-can-use)):  
  69 行（追加 35・削除 34）が変わりました。`web-fetch` を例外として挙げる記述が 7 か所に加わり、`tools` で Edit と Write を外しても Bash でファイルを変えられる、という注意が 2 か所に入りました。残りの多くは、節の導入や補足の文を外す推敲です

## 軽微な更新

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

## 新着情報

（今回の差分に新着情報（`whats-new/`）のページはありません。head の `llms.txt`・`llms-full.txt`・見出しマップにも whats-new のページは載っていません）

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-11-20.md](./archives/latest/2026-11-20.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-11-20.md](./archives/latest-detail/2026-11-20.md)

<!--
base_commit: 5f51174830a6109f6c27c1eeae6dd98de6f65dde
head_commit: 3279a161e968357548276a7baa091d6d6f481473
generated_at_full: 2026-11-22T15:14:02+09:00
-->
