---
対象期間: 2026年10月20日 〜 2026年10月23日
作成日: 2026-10-23
---

# MCP 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
今回の対象期間の差分は本文 `llms-full.txt` の追加 64 行・削除 6 行だけで、索引 `llms.txt` には変更がありません。変更のあった 11 ページのうち 8 ページは画像の直後に説明文（キャプション）が入ったもの、残る 3 ページは Peter Alexander の GitHub アカウントの表記が変わったものです。

主要なものを以下に挙げます。

1. Inspector の 6 ページの画像 24 枚と、MCP Apps の 2 ページの画像 5 枚の直後に、キャプションの文が入った。Inspector の画像は代替テキストが空だったため、何を示す画面かが本文から読めるようになった。MCP Apps の 5 件のうち 3 件は、既存の代替テキストと同じ文
2. Skills Over MCP WG・Tasks and Events WG の憲章と Roadmap で、Peter Alexander の GitHub アカウントが `@pja-ant` から `@poita` に変わり、両憲章の Organization の列から Anthropic の表記が外れた。SEP 4 件の Author(s)・Sponsor の欄は `@pja-ant` のまま
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**画像 29 枚にキャプションが付き Inspector の画面の説明が読めるようになった**](#1-画像-29-枚にキャプションが付き-inspector-の画面の説明が読めるようになった):  
  Inspector の 6 ページ（MCP Inspector・Authorization・Protocol eras・Recipes・TUI client・Web client）で、代替テキストが空の画像 24 枚の直後に、何を示す画面かを説明する文が入った。Protocol eras では legacy と modern の画面の違いや、各機能が画面にどう現れるかが書かれている。MCP Apps の 2 ページ（Build an MCP App・MCP Apps）でも画像 5 枚にキャプションが付いたが、うち 3 件は既存の代替テキストと同じ文。
2. [**憲章と Roadmap で Peter Alexander の GitHub アカウントの表記が変わった**](#2-憲章と-roadmap-で-peter-alexander-の-github-アカウントの表記が変わった):  
  Skills Over MCP WG と Tasks and Events WG の憲章の Leadership・Membership の表、Roadmap の優先領域 2 つの Core Maintainers の行で、Peter Alexander の GitHub アカウントが `@pja-ant` から `@poita` に変わった。両憲章では Organization の列も「Anthropic / Core Maintainer」が「Core Maintainer」に、「Anthropic」が「-」になった。SEP 4 件の Author(s)・Sponsor の欄は `@pja-ant` のまま据え置かれている。
<!-- light:highlight-list:end -->

## 1. 画像 29 枚にキャプションが付き Inspector の画面の説明が読めるようになった

今回の差分は本文 `llms-full.txt` だけで、追加 64 行・削除 6 行という内訳です。索引 `llms.txt` には 1 行の変更もなく、`llms-full.txt` の総行数は 45,069 行から 45,127 行になりました。収録ページ数は 157 件（`examples` が 2 回収録されているため、URL としては 156 件）のままです。対象期間中には取り込みが 3 回ありましたが、MCP 側の入力が変わったのは最後の 1 回だけです。追加 64 行のうち 58 行は、8 ページの画像 29 枚の直後に置かれたキャプションの文（29 行）と、区切りの空行（29 行）です。画像の行そのものは、どれも変わっていません。

**Inspector の画像 24 枚に、画面の説明が付きました。** 2026-07-28 版の Inspector のドキュメント 6 ページにある画像は、どれも代替テキストが空（`![](…)`）です。このため、これまで `llms-full.txt` からは画像の URL しか読めませんでした。今回、それぞれの画像の下に、何を示す画面かを述べる文が加わっています。

- **Protocol eras（11 枚）**: The `Protocol Era` setting の節の画像は、Server Settings にある Protocol Era の選択肢（3 つ）を示すものと説明されています。残る 10 枚は、Logging・Resource subscriptions・Tasks・Multi-round tool results (MRTR)・Tools: mirrored headers and excluded tools・Network and Protocol: headers and the error taxonomy の各節のものです。Logging では、legacy の Logs タブにはセッション単位の「Set Active Level」の操作があり、`send_notification` を呼ぶとログが届く一方、modern では同じタブに「Log Level per Request」があり、レベルは送信するすべてのリクエストに付けられ、ログはそのリクエストのストリームに乗って届く、と書かれています。Tasks では、legacy の Tasks タブは `tasks/list` から一覧を作り、ペイロードはブロッキングの `tasks/result` で取得する一方、modern ではクライアントが既に持っているハンドルに対して `tasks/get` をポーリングし、完了したタスクは結果をインラインで持つ（タスクのオブジェクト全体に `resultType: complete` がある）と説明されています。MRTR の 2 枚は、`input_required` が付いた保留中のリクエストのモーダル（応答すると元のリクエストが再試行される）と、`mrtr_confirm` の完了後に 2 回の `tools/call` が 1 つの MRTR の会話にまとまっている Protocol タブです。Network and Protocol の節では、厳格なサーバーが返した 400 Bad Request を Network タブが HTTP の層として示し、同じ失敗を Protocol タブが型付きの仕様のエラー `-32022 UnsupportedProtocolVersion` として、サーバーが対応するバージョンとともに示すことが書かれています
- **Web client（8 枚）**: The tab bar・The monitoring sidebar・Server Settings・Tools・Resources・Prompts・Apps・Protocol, Network, and Console の各節の画像です。タブバーにどのタブが出るかはサーバーが報告した capability で決まること、Server Settings で Advertised Extensions のチェックを外すと接続時に Inspector が宣言する内容が変わること、ツールを呼び出して結果が返ると引数のフォームが結果のパネルの中に折りたたまれること、などが書かれています
- **TUI client（2 枚）**: ページ冒頭の、サーバーに接続して Tools タブでツールの入力スキーマを表示している画面と、Authorizing an HTTP server の節の Auth タブです。Auth タブについては、Web クライアントの Connection Info と同じ OAuth の項目を表示し、まだ認可していなければ OAuth の情報がまだ無い旨を表示する、と説明されています
- **MCP Inspector・Authorization・Recipes（各 1 枚）**: MCP Inspector のページ冒頭は、ツールを呼び出した後の Web クライアントで、モニタリングのサイドバーを固定して広げ、JSON-RPC のやり取りを読みやすくした画面です。Authorization の The flow, end to end の節は、OAuth のフローを終えた後の Connection Info（認可の状態、動的に登録されたクライアント、付与されたスコープ）です。Recipes の Importing an existing client config の節は、既存のクライアントの設定ファイルか、レジストリの `server.json` から取り込める Add Servers の画面です

なお、MCP Inspector のページ冒頭の画像と、Web client の The monitoring sidebar の節の画像は同じファイル（`web-monitor-sidebar.png`）ですが、キャプションはページごとに別の文になっています。

**MCP Apps の 2 ページでは、5 件のうち 3 件が既存の代替テキストの繰り返しです。** Build an MCP App の画像 4 枚のうち、「Creating a new MCP App with Claude Code」「Testing the color picker in Claude」「Adding a custom connector in Claude」の 3 件は、画像の代替テキストと同じ文がキャプションとして繰り返されたもので、新しい情報ではありません。残る 1 枚、Testing with the basic-host の節の画像には、代替テキスト「Example of the QR code MCP App running with the basic host」とは別の「Testing the QR code MCP App with the basic host」が付いています。MCP Apps（`extensions/apps/overview`）のページ冒頭の画像にも、代替テキスト「An Excalidraw MCP App drawing a sequence diagram inside a Claude conversation」とは別の「Excalidraw MCP App, running in Claude」が付きました。

**キャプションの出どころは、`llms-full.txt` からは判別できません。** 代替テキストと同じ 3 件を除く 26 件の文は、前回の `llms-full.txt` にも、書式が Markdown に変わる前の MDX 版（commit `df8be8b`）にも、どの形でも含まれていません。ただし MDX 版は、57 個の `<Frame>` をすべて属性なしで、`<img>` を `src` なしで出力していました。このため、これらの文がページの原稿に新しく書かれたものなのか、以前から原稿にあって `llms-full.txt` に出力されていなかっただけなのかは区別できません。同じ取り込みでは Claude Code の `llms-full.txt` にも、ほかの更新とは別に、既存の画像の直後の説明文が 2 件加わっています。`llms-full.txt` を生成する側が、画像のキャプションを出力するようになった可能性があります。

- [Protocol eras - MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/protocol-eras#logging)
- [Web client - MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/web#the-tab-bar)

## 2. 憲章と Roadmap で Peter Alexander の GitHub アカウントの表記が変わった

残る 6 行の変更（追加 6 行・削除 6 行）は、いずれも Peter Alexander の記載です。3 ページで、GitHub アカウントの表記とリンク先が `@pja-ant`（`https://github.com/pja-ant`）から `@poita`（`https://github.com/poita`）に変わりました。

- **Skills Over MCP WG の憲章**: Leadership と Membership の表の Peter Alexander の行で、アカウントが変わり、Organization の列が「Anthropic / Core Maintainer」から「Core Maintainer」になりました。Lead が Ola Hungerford・Peter Alexander・Sambhav Kothari の 3 名である構成は変わっていません
- **Tasks and Events WG の憲章**: Leadership と Membership の表の Peter Alexander の行で、アカウントが変わり、Organization の列が「Anthropic」から「-」になりました。Clare Liguori・Peter Alexander・Luca Chang・Caitie McCaffrey の 4 名が Lead である体制（2026年10月20日 作成のサマリで報告した改称後のもの）は変わっていません
- **Roadmap**: 優先領域「1. Agentic Messaging Primitives」と「4. Improved Primitives」の Core Maintainers の行で、Peter Alexander のリンク先が変わりました。表示名と、各行での並び順は同じです

一方、SEP のページでは表記が据え置かれています。SEP-2133（Extensions）と SEP-2164（Standardize Resource Not Found Error Code）の Author(s) の欄、SEP-2567（Sessionless MCP via Explicit State Handles）と SEP-2640（Skills Extension）の Author(s) と Sponsor の欄、計 6 行は `@pja-ant` のままです。`llms-full.txt` 全体では、`pja-ant` の出現は 22 箇所から 12 箇所に減り、`poita` が新たに 10 箇所に現れました。Governance and Stewardship のページの「Current Core Maintainers」には、Peter Alexander の名前がリンク無しで載っており、今回は変わっていません。

- [Tasks and Events Charter - MCP Docs](https://modelcontextprotocol.io/community/working-groups/tasks-events#leadership)
- [Skills Over MCP Charter - MCP Docs](https://modelcontextprotocol.io/community/working-groups/skills-over-mcp#leadership)

## 新規追加されたページ

<!-- light:new-pages:start -->
今回の対象期間に新たに追加されたページはありません。索引 `llms.txt` に変更はなく、索引側のエントリ数（362 件）と本文 `llms-full.txt` の収録ページ数（157 件）はどちらも前回と同じです。
<!-- light:new-pages:end -->

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
今回の対象期間に大幅な更新（本文 50 行以上の変更）があったページはありません。差分が出た 11 ページで最も大きいのは Protocol eras の追加 22 行（キャプション 11 件と区切りの空行）で、いずれも「軽微な更新」で扱います。
<!-- light:updated-pages:end -->

## 軽微な更新

<!-- light:minor-updates:start -->
今回差分が出たファイルは `llms-full.txt` の 1 件のみで、変更のあったページは次の 11 件です。

**機能改善**

- Protocol eras の画像 11 枚の直後にキャプションを追加。Logging・Tasks などの節で、legacy と modern の画面の違いを説明している（詳細はハイライト 1 参照） — [Protocol eras](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/protocol-eras#logging)
- Web client の各節の画像 8 枚の直後にキャプションを追加（詳細はハイライト 1 参照） — [Web client](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/web#the-tab-bar)
- TUI client のページ冒頭と Authorizing an HTTP server の節の画像 2 枚の直後にキャプションを追加（詳細はハイライト 1 参照） — [TUI client](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/tui#authorizing-an-http-server)
- MCP Inspector のページ冒頭の画像 1 枚の直後にキャプションを追加（詳細はハイライト 1 参照） — [MCP Inspector](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector)
- Authorization の The flow, end to end の節の画像 1 枚の直後にキャプションを追加（詳細はハイライト 1 参照） — [Authorization](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/authorization#the-flow-end-to-end)
- Recipes の Importing an existing client config の節の画像 1 枚の直後にキャプションを追加（詳細はハイライト 1 参照） — [Recipes](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/recipes#importing-an-existing-client-config)
- Build an MCP App の画像 4 枚の直後にキャプションを追加。うち 3 件は既存の代替テキストと同じ文（詳細はハイライト 1 参照） — [Build an MCP App](https://modelcontextprotocol.io/extensions/apps/build#using-an-ai-coding-agent)
- MCP Apps のページ冒頭の Excalidraw の画像の直後に、代替テキストとは別のキャプションを追加（詳細はハイライト 1 参照） — [MCP Apps](https://modelcontextprotocol.io/extensions/apps/overview)

**その他**

- Skills Over MCP WG の憲章の Leadership と Membership の表で、Peter Alexander の GitHub アカウントを `@pja-ant` から `@poita` に、Organization を「Anthropic / Core Maintainer」から「Core Maintainer」に変更（詳細はハイライト 2 参照） — [Skills Over MCP Charter](https://modelcontextprotocol.io/community/working-groups/skills-over-mcp#leadership)
- Tasks and Events WG の憲章の Leadership と Membership の表で、Peter Alexander の GitHub アカウントを `@pja-ant` から `@poita` に、Organization を「Anthropic」から「-」に変更（詳細はハイライト 2 参照） — [Tasks and Events Charter](https://modelcontextprotocol.io/community/working-groups/tasks-events#leadership)
- Roadmap の優先領域「1. Agentic Messaging Primitives」と「4. Improved Primitives」の Core Maintainers の行で、Peter Alexander のリンク先を `https://github.com/pja-ant` から `https://github.com/poita` に変更（詳細はハイライト 2 参照） — [Roadmap](https://modelcontextprotocol.io/development/roadmap#1-agentic-messaging-primitives)
<!-- light:minor-updates:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-10-20.md](./archives/latest/2026-10-20.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-10-20.md](./archives/latest-detail/2026-10-20.md)

<!--
base_commit: 9a810fc542230f7d1d5e0e958b239a460a6d260f
head_commit: 5536db396725852afccd11c0a05e205b631b83fa
generated_at_full: 2026-10-24T15:54:14+09:00
-->
