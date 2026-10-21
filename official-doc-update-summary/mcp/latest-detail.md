---
対象期間: 2026年10月17日 〜 2026年10月20日
作成日: 2026-10-20
---

# MCP 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
今回の差分の大半は、本文 `llms-full.txt` の生成形式が MDX のコンポーネントから GitHub 風の Markdown に変わったことによるもので、157 ページ中 136 ページに差分が出ました（追加 9,821 行・削除 10,130 行）。内容が変わったのは、コミュニティのグループ再編で新しい URL に移った 2 つの憲章と、それを参照する 6 ページだけです。Agents Working Group が Interest Group に転換し、Tasks の所管は Triggers and Events Working Group 改め Tasks and Events Working Group に移りました。

主要なものを以下に挙げます。

1. `llms-full.txt` の書式が MDX から Markdown に変わり（コールアウトは `> [!NOTE]` など）、カードのリンク先や画像の URL が読めるようになった。一方、Extensions の Support matrix ではチェックマーク 15 個が消え、対応状況が読めなくなった
2. Agents WG が 2026年10月16日 付けで Interest Group に転換し、憲章の URL が `community/interest-groups/agents` に移った。Tasks の所管が外れ、リード 2 名はファシリテーター 1 名になり、WG 専用の意思決定権限の表なども無くなった
3. Triggers and Events WG が同じ日付で Tasks and Events WG に改称し（URL は `community/working-groups/tasks-events`）、Tasks の安定化とコアプロトコルへの昇格を引き継いだ。リードは 4 名になり、他の 6 ページの参照も新しい名称に追従した
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**llms-full.txt の書式が MDX から Markdown に変わり Support matrix のチェックマークが消えた**](#1-llms-fulltxt-の書式が-mdx-から-markdown-に変わり-support-matrix-のチェックマークが消えた):  
  `llms-full.txt` の生成形式が変わり、`<Note>`・`<Steps>`・`<Tabs>`・`<Card>`・`<Badge>` などの MDX のコンポーネントが GitHub 風の Markdown（`> [!NOTE]` のコールアウト、太字の行、リンク、URL 付きの画像）に置き換わった。157 ページ中 136 ページに差分が出たが、正規化して比べると内容の変更ではない。ただし `extensions/client-matrix` の Support matrix では `<CHECK />` が 15 個とも消え、対応を示すセルが空になった。
2. [**Agents WG が Interest Group に転換し Tasks の所管を手放した**](#2-agents-wg-が-interest-group-に転換し-tasks-の所管を手放した):  
  Agents の憲章が `community/working-groups/agents` から `community/interest-groups/agents` に移り、Group Type が Interest Group になった。Changelog には 2026年10月16日 付けで「Interest Group に転換し、Tasks の所管を Tasks and Events WG に移した」旨の行が加わった。In Scope から Tasks の項目が外れ、Lead 2 名はファシリテーター 1 名（Luca Chang）になり、WG 専用の節は Interest Group 向けの構成に改められた。
3. [**Triggers and Events WG が Tasks and Events WG に改称し Tasks を引き継いだ**](#3-triggers-and-events-wg-が-tasks-and-events-wg-に改称し-tasks-を引き継いだ):  
  Triggers and Events の憲章が `community/working-groups/tasks-events` に移り、グループは Tasks and Events Working Group に改称した。旧 Agents WG の憲章にあった Tasks の安定化とコアプロトコルへの昇格、Tasks 拡張のリポジトリと SEP-2663 への参照、関連する作業項目と成功基準がこちらに移り、Luca Chang と Caitie McCaffrey が加わってリードは 4 名になった。Transports WG・Roadmap など 6 ページの参照も新しい名称に追従した。
<!-- light:highlight-list:end -->

## 1. llms-full.txt の書式が MDX から Markdown に変わり Support matrix のチェックマークが消えた

**今回の差分の大半は、ドキュメントの内容ではなく `llms-full.txt` の生成形式の変更です。** これまで `llms-full.txt` は、各ページを MDX のソースに近い形（`<Note>`・`<Steps>`・`<Tabs>` などのコンポーネントのタグと、その中の字下げ）で展開していましたが、今回からは GitHub 風の Markdown に変換して展開しています。ファイル全体の差分は追加 9,821 行・削除 10,130 行で、総行数は 45,378 行から 45,069 行になりました。収録ページ 157 件（`examples` が 2 回収録されているため、URL としては 156 件）のうち、136 ページに差分が出ています。索引 `llms.txt` の変更は 2 行の差し替えだけです（ハイライト 2・3 参照）。対象期間中の取り込みは 3 回ありましたが、MCP 側の入力が変わったのは最後の 1 回だけです。

- **コールアウト**: `<Note>`（138）と `<Info>`（6）が `> [!NOTE]`（144）に、`<Warning>`（49）が `> [!WARNING]`（49）に、`<Tip>`（10）が `> [!TIP]`（10）になりました。SEP-990 のページでバックスラッシュでエスケープされていた `> \[!IMPORTANT]` も、エスケープが外れて `> [!IMPORTANT]` になっています
- **手順・タブ・折りたたみ**: `<Step title="…">`（96）は `**1. タイトル**` のような番号付きの太字の行に、`<Tab title="…">`（41）はタイトルの太字の行に、`<Accordion title="…">`（8）は引用ブロックの中の太字のタイトルになり、中身の字下げは外れました。`<CodeGroup>`（52）と `<Frame>`（57）は、タグだけが外れています
- **カード**: `<Card title="…" href="…">`（81）がタイトルのリンク（例: `> **[Build a Server](/docs/2026-07-28/develop/build-server)**`）になり、これまでタグの属性にしかなかったリンク先が本文で読めるようになりました
- **バッジ・アイコン**: `<Badge>`（147）は中の文字列だけが残り（SEP の索引の `Final`、SDKs の一覧の `Tier 1` など）、`<Icon>`（10）は何も残さず外れました
- **画像**: `src` を持たない `<img>`（69。うち 33 に代替テキスト）が、URL 付きの Markdown の画像（69）になりました
- **その他の展開**: `docs/2026-07-28/learn/architecture` の `<Tooltip>`（2）は、旧版の `llms-full.txt` には無かった説明文が括弧書きで本文に入りました（「stateless protocol (Every request contains all the information needed to process it, …)」など）。`extensions/apps/build` の `<Tree>` は、フォルダとファイルの名前（`my-mcp-app`・`package.json` など 8 件）の並びになっています
- **schema のページ**: `specification/2026-07-28/schema` は、`<div>`・`<span>`・`<a>`・`<br />` で組まれていた型定義が、素の Markdown（リンクと、行末のバックスラッシュによる改行）になりました。空のリンク `[ ](#…)` だったパーマリンクは `[Permalink](#…)`（580）という文字列に、`<aside>`（214）で囲まれていた「Inherited from …」「Overrides …」の注記はタグの無い文になっています

**変換で失われたもの・崩れたものもあります。**

- **Extensions の Support matrix**: `extensions/client-matrix` の Support matrix で、対応を示す `<CHECK />` が 15 個とも消え、該当するセルが空になりました。旧版では、MCP Apps の列に 11 クライアント（Claude (web)・Claude Desktop・VS Code GitHub Copilot・Microsoft 365 Copilot・Goose・Postman・MCPJam・ChatGPT・Cursor・Archestra.AI・PostHog Code）、Enterprise Auth の列に 2 クライアント（Archestra.AI・mcpc MCP CLI）、OAuth Client Credentials と Skills の列に各 1 クライアント（mcpc MCP CLI）の印がありました。新版の表に残っているのは、Skills の列にある「Partial」へのリンク 3 件（ChatGPT・fast-agent・MCP Inspector）だけです。**対応状況は `llms-full.txt` からは読み取れなくなっており**、今後のサマリでもこの表の変化は追えません
- **schema のコード例**: `<pre>` で示されるコード例 126 件すべてで、末尾にコピー用ボタンの文字列「Copy」が残っています。また、型定義の閉じ括弧の直後に説明文が区切りなく続き（例: `}A response to a request that indicates an error occurred.`）、項目の末尾には `&#x20;` が 92 件残っています

**数え方**: 書式の変換で生の差分が意味を失っているため、`llms-full.txt` をページ単位に切り出し、両側（base と head）を同じ規則で正規化してから比べました。規則は、MDX のコンポーネントのタグを外し（`title` は文字列として、`<Card>` の `href` はリンクとして残す）、HTML のタグ・エンティティ・バックスラッシュのエスケープ・行頭の引用記号と箇条書きの記号・太字の記号・字下げを除いたうえで、行の分割や連結の違いを吸収するため、差分のかたまりの両側を英数字だけに縮めて一致するものを書式の差とみなす、というものです。schema のパーマリンクと「Copy」の文字列もここで除きました。この方法で残った差分は 11 ページで、うち 3 ページ（Support matrix のチェックマーク、architecture の Tooltip、SEP-990 のエスケープ）は上記の変換によるものでした。残る 8 ページが、ハイライト 2・3 で扱うグループ再編に関わる内容の変更です。生の差分で最大の schema（追加 1,406 行・削除 1,065 行）は、正規化すると変化がありません。なお、SEP-2260 と SEP-2577 のページに残る `<Warning>`（7）は、仕様の文書に加える文面の例としてコードフェンスの中に書かれたもので、変換漏れではありません。

- [Extension Support Matrix - MCP Docs](https://modelcontextprotocol.io/extensions/client-matrix#support-matrix)

## 2. Agents WG が Interest Group に転換し Tasks の所管を手放した

Agents の憲章（Agents Charter）が、`community/working-groups/agents` から `community/interest-groups/agents` に移りました。索引 `llms.txt` でもエントリが Working Group の並びから Interest Group の並び（Authorization Charter の前）に移り、説明文は「Charter for the MCP Agents Interest Group.」になっています。Group Type は **Interest Group** になり、Changelog では初版の行が「Initial charter (as the Agents WG)」に改められたうえで、2026年10月16日 付けの「Converted to an Interest Group. Tasks scope moved to the Tasks and Events WG.」が加わりました。

**Tasks の所管が外れました。** ミッションから「The WG stewards Tasks as MCP's foundation for durable asynchronous execution」の部分が消え、グループの役割は、プロトコルの対応が要る残りの課題を評価したうえで、プロトコルの発展のさせ方を提言する・追加の拡張を作る・既存の MCP のプリミティブの一貫した使い方を文書化する、のいずれかを行う形になりました。In Scope からは、`io.modelcontextprotocol/tasks` 拡張の安定化とコアプロトコルへの昇格を扱う「Tasks」と、SDK・conformance のメンテナーと連携する「Implementation Coordination」の 2 項目が外れています。Out of Scope には、Tasks・一般的なイベント配信・コールバックの仕組みは Tasks and Events WG の所管と書かれ、Related Groups の Tasks and Events WG の項も、Tasks とタスクの状態・完了の通知は同 WG の所管で、IG はユースケースと要件を提供する、という書き方になりました。「The group standardizes behavior at MCP interoperability boundaries」は「focuses on」に、「through its design work」は「through its discussions」に改められています。

**体制と構成も Interest Group 向けに改められました。** Leadership は、Lead の Luca Chang（Amazon Web Services）と Caitie McCaffrey（Microsoft）の 2 名から、Facilitator の Luca Chang 1 名になり、Membership の表も同じ変更を受けています。WG の意思決定権限を定めた Authority & Decision Rights の表（8 行）は削除されました。charter-template はこの節を「(WG only)」とし、「IGs do not make binding decisions and do not need this section」と記しています。Deliverables & Success Metrics の節は「Discussion Topics」になり、作業項目から「Tasks stabilization and core protocol promotion」が外れて、Agents Extension の評価と提言、two-level agent definition の概念実証の 2 件が残りました。Success Criteria は「Planned Outputs」に改められ、Tasks の安定化に関する 2 項目が外れたほか、評価の後の行動が「evolves Tasks, proposes an Agents Extension」から「recommends evolving Tasks, recommends an Agents Extension」に変わっています。Resources からは Tasks 拡張のリポジトリ（`ext-tasks`）と SEP-2663 への参照が外れ、グループのリポジトリ `modelcontextprotocol/agents-wg` と Discord の `#agents-wg` は名前を変えずに残っています。

- [Agents Charter - MCP Docs](https://modelcontextprotocol.io/community/interest-groups/agents#changelog)

## 3. Triggers and Events WG が Tasks and Events WG に改称し Tasks を引き継いだ

Triggers and Events の憲章が `community/working-groups/triggers-events` から `community/working-groups/tasks-events` に移り、グループは Tasks and Events Working Group に改称しました。索引のエントリも「Tasks and Events Charter」（説明文は「Charter for the MCP Tasks and Events Working Group.」）に差し替えられ、並びは Skills Over MCP Charter と Transports Charter の間です。Changelog では初版の行が「Initial charter (as the Triggers and Events WG)」に改められたうえで、2026年10月16日 付けの「Renamed to Tasks and Events WG. Tasks scope and its leads moved here from the Agents WG.」が加わりました。

**旧 Agents WG から Tasks の所管が移ってきました。** ミッションは、MCP の永続的な非同期実行の基盤として既にある Tasks の開発を続けることと、サーバーが状態の変化をクライアントへ能動的に通知する方法を定めることの 2 本立てになりました。In Scope の先頭には、旧 Agents WG の憲章にあった「Tasks」の項目（`io.modelcontextprotocol/tasks` 拡張の安定化とコアプロトコルへの昇格）が同じ文面で加わり、Documentation にも Tasks の仕様が入りました。Cross-Cutting Concerns の連携先は、Agents WG（タスク完了の通知とイベントのトリガーが交わるところ）から、Tasks やイベントのトリガーに依存するエージェントのユースケースについての Agents IG に変わっています。Out of Scope には、エージェントを背後に持つユースケースと Agents Extension の評価は Agents IG の担当、という項目が加わりました。Related Groups の Agents の項は、SEP-1686（Tasks）の issue への言及から、Agents IG へのリンクと「IG がユースケースと要件を出し、この WG がプロトコルの表面を担う」という分担に書き換えられています。

**リードと作業項目も移ってきました。** Leadership は、Clare Liguori（Amazon Web Services）と Peter Alexander（Anthropic）の 2 名に、旧 Agents WG のリードだった Luca Chang（Amazon Web Services）と Caitie McCaffrey（Microsoft）が加わって 4 名になり、4 名を Lead とする Membership の表が新設されました。Operations には会議が meet.modelcontextprotocol.io に掲載される旨が加わり、Resources には Tasks 拡張のリポジトリ（`modelcontextprotocol/ext-tasks`）と Tasks の仕様（SEP-2663: Tasks Extension）への参照が加わりました。インキュベーション用のリポジトリ `experimental-ext-triggers-events` は名前を変えずに残っています。Active Work Items の先頭には「Tasks stabilization and core protocol promotion」（In Progress、Champion は @LucaButBoring）が、Success Criteria の先頭には Tasks の安定化に関する 2 項目が、いずれも旧 Agents WG の憲章と同じ文面で加わりました。イベント側の作業項目（「SEP: Events in MCP v1 RFC」など、目標時期は End April）は変わっていません。

**他のページの参照も追従しました。** Transports WG の憲章の Related Groups では、Agents WG と Triggers and Events WG の 2 項目が Tasks and Events WG の 1 項目にまとめられ、Tasks と durable execution、イベントのコールバック・購読・アプリケーションレベルの配信のいずれも同 WG の所管と書かれています。Roadmap の「Agentic Messaging Primitives」では、サーバー起点のイベントの担当が Tasks & Events WG に、コンポジションのレビューが「Tasks & Events and Transports WGs, with the Agents IG」になりました（ページ冒頭の更新日 2026年08月22日 は変わっていません）。Scientific Computing IG の憲章は Tasks に関する連携先のリンクを Agents WG から Tasks and Events WG へ、Authorization IG・Filesystems WG・Skills Over MCP WG（2 箇所）の憲章はリンクの無い「Agents WG」の表記を「Agents IG」に改めています。今回の `llms-full.txt` には、旧 URL へのリンクも「Agents WG」「Triggers and Events WG」の表記も、両憲章の Changelog の行を除いて残っていません。

- [Tasks and Events Charter - MCP Docs](https://modelcontextprotocol.io/community/working-groups/tasks-events#changelog)
- [Transports Charter - MCP Docs](https://modelcontextprotocol.io/community/working-groups/transports#related-groups)

## 新規追加されたページ

<!-- light:new-pages:start -->
今回の対象期間に新しい URL で収録されたページは次の 2 件です。いずれも既存の憲章が改称・転換に伴って URL を移したもので、旧 URL の本文は同時に削除されました（「軽微な更新」参照）。索引 `llms.txt` のエントリ数（362 件）と `llms-full.txt` の収録ページ数（157 件）は変わっていません。

- [**Agents Charter**](#1-agents-charter) ([MCP Docs](https://modelcontextprotocol.io/community/interest-groups/agents)):  
  Agents Interest Group の憲章（111 行、区切りの空行を含む）。旧 `community/working-groups/agents` の Agents WG の憲章を Interest Group に転換したもので、Tasks の所管が外れ、ファシリテーター 1 名と、Discussion Topics・Planned Outputs の構成になった（変更点はハイライト 2 参照）。
- [**Tasks and Events Charter**](#2-tasks-and-events-charter) ([MCP Docs](https://modelcontextprotocol.io/community/working-groups/tasks-events)):  
  Tasks and Events Working Group の憲章（115 行、区切りの空行を含む）。旧 `community/working-groups/triggers-events` の Triggers and Events WG を改称したもので、Tasks の安定化を引き継ぎ、リード 4 名と Membership の表が加わった（変更点はハイライト 3 参照）。
<!-- light:new-pages:end -->

## 1. Agents Charter

Agents Interest Group は、エージェントを背後に持つシステムとのやり取りを MCP 上で相互運用できるようにすることを目的とするグループです。ミッションでは、こうしたシステムが通常のツールとして、あるいはフレームワーク固有の統合を通じて公開されており、永続的な実行・能力の発見・委任・複数ターンのやり取りが場当たり的な慣習に任されている現状を挙げています。In Scope は、agent-as-tool・remote-agent・supervisor/sub-agent の各パターンを含むユースケースを評価して Tasks を補う Agents Extension が要るかを判断する「Agents Extension Evaluation」、その判断に役立つ範囲に絞った概念実証を作る「Prototypes and Proposals」、関連グループとの連携（Cross-Cutting Concerns）、ユースケース・知見・提言の文書化（Documentation）の 4 項目です。Out of Scope は、汎用のエージェントフレームワーク・ランタイムの構築や標準化、トランスポートのワイヤーフォーマットとセッション（Transports WG の所管）、Tasks・一般的なイベント配信・コールバック（Tasks and Events WG の所管）の 3 項目です。

運営は、Facilitator の Luca Chang（Amazon Web Services）が 1 名で務め、週 1 回 30 分の Working Session を開きます。Discussion Topics には「Agents Extension evaluation and recommendation」（In Progress、Champion は TBD）と「Two-level agent definition proof of concept」（In Progress、@LucaButBoring と @madhaviai）の 2 件が並びます。Planned Outputs には、Agents Extension の要否の評価を公表すること、その評価に基づいて Tasks の発展・Agents Extension・既存のプリミティブで足りることの文書化のいずれかを提言すること、提案するプロトコルの表面をプロトタイプと実装のフィードバックで評価してから進めること、の 3 項目が挙がっています。

- [Agents Charter - MCP Docs](https://modelcontextprotocol.io/community/interest-groups/agents)

## 2. Tasks and Events Charter

Tasks and Events Working Group のミッションは、MCP の永続的な非同期実行の基盤として既にある Tasks の開発を続けることと、サーバーが状態の変化をクライアントへ能動的に通知する方法を定めることです。現状ではクライアントはポーリングか SSE 接続の維持でサーバー側の更新を知るしかないため、新しいデータがあるときにサーバーが通知をプッシュできる標準のコールバックの仕組み（Webhook など）を、すべてのトランスポートで成り立つ順序保証とともに仕様化するとしています。In Scope は、Tasks（`io.modelcontextprotocol/tasks` 拡張の安定化とコアプロトコルへの昇格）、トリガー／コールバックの仕組み・購読のライフサイクル・配信の意味論・イベントの順序保証を定める SEP（Specification Work）、SDK のリファレンス実装、Transports WG・Agents IG との連携、Tasks の仕様とイベント駆動のパターン・ポーリングからの移行ガイドの文書化の 5 項目です。

体制は、Clare Liguori（Amazon Web Services）・Peter Alexander（Anthropic）・Luca Chang（Amazon Web Services）・Caitie McCaffrey（Microsoft）の 4 名のリードで、WG としての意思決定権限の表（8 行）を持ち、週 1 回 30 分の Working Session を開きます。Active Work Items は「Tasks stabilization and core protocol promotion」（In Progress）、「SEP: Events in MCP v1 RFC」（Ideating、目標は End April）、Tier 1 の SDK でのリファレンス実装（目標は End April）の 3 件です。Success Criteria は、Tasks の安定化とコアプロトコルへの昇格、Tasks の安定化を阻むライフサイクルの曖昧さと conformance の欠落の解消、トリガー／コールバックの仕組みを定める SEP の承認、2 つ以上の Tier 1 の SDK でのリファレンス実装、新しいプリミティブの conformance テストの 5 項目です。

- [Tasks and Events Charter - MCP Docs](https://modelcontextprotocol.io/community/working-groups/tasks-events)

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
今回の対象期間に大幅な更新（本文 50 行以上の変更）があった既存ページはありません。生の差分では `specification/2026-07-28/schema`（追加 1,406 行・削除 1,065 行）をはじめ多くのページが 50 行を超えますが、いずれも書式の変換によるもので、正規化すると本文に変化はありません（ハイライト 1 参照）。旧 URL の 2 ページの本文削除は、新しい URL へ移ったことによるもので、「軽微な更新」で扱います。
<!-- light:updated-pages:end -->

## 軽微な更新

<!-- light:minor-updates:start -->
今回差分が出たファイルは `llms-full.txt` と `llms.txt` の 2 件です。新しい URL の 2 ページは「新規追加されたページ」で扱い、ここでは残る変更を挙げます。

**その他**

- `llms-full.txt` の書式を MDX のコンポーネントから GitHub 風の Markdown に変更。157 ページ中 136 ページに差分が出たが、内容の変更ではない。Extensions の Support matrix のチェックマーク 15 個は失われた（詳細はハイライト 1 参照） — [Extension Support Matrix](https://modelcontextprotocol.io/extensions/client-matrix#support-matrix)
- 旧 Agents Charter（`community/working-groups/agents`）の本文 146 行（区切りの空行を含む）を削除。Interest Group への転換に伴い `community/interest-groups/agents` へ移った（詳細はハイライト 2 参照）
- 旧 Triggers and Events Charter（`community/working-groups/triggers-events`）の本文 85 行（区切りの空行を含む）を削除。改称に伴い `community/working-groups/tasks-events` へ移った（詳細はハイライト 3 参照）
- 索引 `llms.txt` で、Agents Charter のエントリを Interest Group の並びへ移し、Triggers and Events Charter のエントリを Tasks and Events Charter に差し替え（追加 2 行・削除 2 行）。エントリ数は 362 件のままで、`community/working-groups/` 配下は 14 件から 13 件に、`community/interest-groups/` 配下は 7 件から 8 件になった。`llms-full.txt` の内訳も同じく 13 件・8 件になっている
- Transports WG の憲章の Related Groups で、Agents WG と Triggers and Events WG の 2 項目を Tasks and Events WG の 1 項目に統合（詳細はハイライト 3 参照） — [Transports Charter](https://modelcontextprotocol.io/community/working-groups/transports#related-groups)
- Roadmap の「Agentic Messaging Primitives」で、サーバー起点のイベントの担当を Tasks & Events WG に、コンポジションのレビューを Tasks & Events・Transports の両 WG と Agents IG に改めた。ページ冒頭の更新日（2026年08月22日）は据え置き（詳細はハイライト 3 参照） — [Roadmap](https://modelcontextprotocol.io/development/roadmap#1-agentic-messaging-primitives)
- Scientific Computing IG の憲章の Related Groups で、Tasks に関する連携先のリンクを Agents WG から Tasks and Events WG に変更 — [Scientific Computing Charter](https://modelcontextprotocol.io/community/interest-groups/scientific-computing#related-groups)
- Authorization IG の憲章の Related Groups で、「Agents WG」の表記を「Agents IG」に変更 — [Authorization Charter](https://modelcontextprotocol.io/community/interest-groups/auth#related-groups)
- Filesystems WG の憲章の Related Groups で、「Agents WG」の表記を「Agents IG」に変更 — [Filesystems Charter](https://modelcontextprotocol.io/community/working-groups/filesystems#related-groups)
- Skills Over MCP WG の憲章の In Scope（Cross-Cutting Concerns）と Related Groups の 2 箇所で、「Agents WG」の表記を「Agents IG」に変更 — [Skills Over MCP Charter](https://modelcontextprotocol.io/community/working-groups/skills-over-mcp#related-groups)
<!-- light:minor-updates:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-10-17.md](./archives/latest/2026-10-17.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-10-17.md](./archives/latest-detail/2026-10-17.md)

<!--
base_commit: df8be8b99ca6342f63f7c7b52da55b4609b1c128
head_commit: 9a810fc542230f7d1d5e0e958b239a460a6d260f
generated_at_full: 2026-10-21T15:42:08+09:00
-->
