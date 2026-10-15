---
対象期間: 2026年10月13日 〜 2026年10月14日
作成日: 2026-10-14
---

# MCP 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
今回の対象期間の差分は本文 `llms-full.txt` の追加 134 行・削除 134 行だけで、索引 `llms.txt` には変更がありません。前回索引に加わった Progressive Disclosure Working Group の憲章本文が収録され、入れ替わりに Primitive Grouping Interest Group の憲章本文が外れました。

主要なものを以下に挙げます。

1. Progressive Disclosure WG の憲章本文が収録され、Primitive Grouping IG が 2026年09月21日 に改称し、Working Group へ移行していたことが確認できた。前回サマリで「入力からは確認できない」としていた両グループの関係が、これで判明した
2. 旧 Primitive Grouping IG の憲章本文が `llms-full.txt` から外れた。既存ページの参照は、Skills Over MCP WG の憲章が新しい WG へのリンクに追従した一方、Scientific Computing IG の憲章は旧ページへのリンクを残したまま
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**Primitive Grouping IG が Progressive Disclosure WG に改称して Working Group へ移行**](#1-primitive-grouping-ig-が-progressive-disclosure-wg-に改称して-working-group-へ移行):  
  前回索引にだけ載っていた `community/working-groups/progressive-disclosure` の本文が収録された。その Changelog に、2026年09月21日 付けで「Primitive Grouping から Progressive Disclosure へ改称し、Interest Group から Working Group へ移行した」旨の行がある。前回サマリで保留していた、新しい WG と Primitive Grouping IG の関係はこれで確定した。
2. [**旧 Primitive Grouping 憲章の本文削除と既存ページの参照の追従状況**](#2-旧-primitive-grouping-憲章の本文削除と既存ページの参照の追従状況):  
  索引から外れた後も残っていた旧憲章の本文が `llms-full.txt` から削除され、索引と本文の両方で旧ページが新ページに置き換わった。Skills Over MCP WG の憲章は言及 2 箇所を新しい WG へのリンクに書き換えたが、Scientific Computing IG の憲章は旧パスへのリンクを残している。
<!-- light:highlight-list:end -->

## 1. Primitive Grouping IG が Progressive Disclosure WG に改称して Working Group へ移行

今回の差分は本文 `llms-full.txt` だけで、追加 134 行・削除 134 行という内訳です。索引 `llms.txt` には 1 行の変更もありません。追加分のうち 132 行（区切りの空行を含む）は `Progressive Disclosure Charter`（`community/working-groups/progressive-disclosure`）の本文で、収録位置は Interceptors Charter と Registry Charter の間です。索引と同じくアルファベット順に並んでいます。

前回のサマリでは、このページが索引に追加されたものの本文が未収録であることを記しました。あわせて、同じ取り込みで Primitive Grouping Interest Group の憲章ページが索引から外れたこと、ただし両者の関係（後継・改称・統合などにあたるかどうか）は入力からは確認できないことも記していました。今回収録された本文の Changelog には、2026年09月21日 付けで「Renamed from Primitive Grouping to Progressive Disclosure and converted from Interest Group to Working Group」という行があり、GitHub Discussions の会議メモへのリンクが添えられています。つまり、Primitive Grouping Interest Group は Progressive Disclosure へ改称され、同時に Interest Group から Working Group へ移行していました。Changelog のもう 1 行は、旧憲章の初版制定を示す 2026年06月18日 付けの「Initial charter」で、旧憲章の行がそのまま引き継がれています。

新しい名称の「Progressive Disclosure」は、Skills Over MCP Working Group の憲章が Primitive Grouping IG との連携テーマとして挙げていた「Progressive disclosure patterns」と同じ語です。本文の多くは旧憲章と同じ文面で、ミッション・In Scope・Out of Scope・Problem Statement・Goals・Discussion Topics は、グループ名の変更と「IG」→「WG」の置き換え以外は変わっていません。Working Group への移行に伴って変わったのは主に体制と運営で、その内容は「新規追加されたページ」で扱います。

- [Progressive Disclosure Charter - MCP Docs](https://modelcontextprotocol.io/community/working-groups/progressive-disclosure#changelog)

## 2. 旧 Primitive Grouping 憲章の本文削除と既存ページの参照の追従状況

Progressive Disclosure Charter の収録と同時に、旧 `Primitive Grouping Charter`（`community/interest-groups/primitive-grouping`）の本文 132 行（区切りの空行を含む）が `llms-full.txt` から削除されました。前回の取り込みで索引から外れた後も、本文だけは残っていました。それが今回解消し、索引と本文の両方で旧ページが新ページに置き換わったことになります。削除と追加が同じ行数のため、`llms-full.txt` の総行数（45,378 行）と収録ページ数（157 件）は変わっていません。本文に収録されたページの内訳は、`community/working-groups/` 配下が 13 件から 14 件に、`community/interest-groups/` 配下が 8 件から 7 件になり、索引側の件数（14 件・7 件）とそろいました。

既存ページからの参照は、追従したものと追従していないものに分かれます。Skills Over MCP Working Group の憲章では、リンクの無い「Primitive Grouping IG」という言及 2 箇所が、どちらも `/community/working-groups/progressive-disclosure` を指すサイト内リンク「Progressive Disclosure WG」に書き換えられました。1 箇所は In Scope の Cross-Cutting Concerns（Registry WG・Agents WG などとの連携を並べた項目）、もう 1 箇所は Related Groups です。添えられた連携テーマ「Progressive disclosure patterns」はどちらも変わっていません。今回の削除 134 行のうち、憲章本文の 132 行を除く 2 行は、この書き換えによるものです。

一方、Scientific Computing Interest Group の憲章は、Related Groups 節で引き続き「Primitive Grouping IG」の名前と旧パス `/community/interest-groups/primitive-grouping` へのリンクを掲げており、今回の差分でも変更されていません。このパスのページは、今回の入力では索引にも本文にもありません。この参照は、新しい Working Group を指すようにはまだ更新されていない状態です。

- [Skills Over MCP Charter - MCP Docs](https://modelcontextprotocol.io/community/working-groups/skills-over-mcp#related-groups)
- [Scientific Computing Charter - MCP Docs](https://modelcontextprotocol.io/community/interest-groups/scientific-computing#related-groups)

## 新規追加されたページ

<!-- light:new-pages:start -->
今回本文が新たに収録されたページは次の 1 件です。索引 `llms.txt` には前回すでにエントリが載っていたため、索引側のエントリ数（362 件）は変わっていません。

- [**Progressive Disclosure Charter**](#1-progressive-disclosure-charter) ([MCP Docs](https://modelcontextprotocol.io/community/working-groups/progressive-disclosure)):  
  旧 Primitive Grouping IG を改称・移行した Progressive Disclosure Working Group の憲章本文 132 行が収録された。ミッションや In Scope・Out of Scope は旧憲章と同じ文面のまま、Core Maintainer の Kurtis Van Gent（Google）を含む 4 名のリーダーシップ、意思決定権限の表、週次の会議が加わった。
<!-- light:new-pages:end -->

## 1. Progressive Disclosure Charter

Progressive Disclosure Working Group のミッションは、MCP のプリミティブ（ツール・リソース・プロンプト・タスク）を、プロトコルが持つフラットな一覧を超えてどう整理できるか、またその整理が MCP サーバーとクライアントの双方にどう役立つかを探ることと定義されています。クライアント・サーバー・ゲートウェイの多様な要件を文書化し、さまざまな整理戦略のリファレンス拡張を支援して、早い段階で 1 つの正準パターンを選ぶのではなく、SEP プロセスに提言を送るという進め方です。In Scope は要件の収集、パターンの探索、概念実証（リファレンス実装と実験結果の共有リポジトリの維持）の 3 項目です。Out of Scope は、仕様変更の承認（提言は SEP プロセスを通す）と、特定のクライアント・サーバーの挙動の義務付けの 2 項目です。Problem Statement では、フラットな一覧が LLM のコンテキストを圧迫して選択を誤らせること（Context overload）、トークンを消費して処理コストと応答レイテンシを増やすこと（Inefficient operations）、整理の手段が無く管理・保守しにくいこと（Poor developer experience）の 3 点をスコープ内としています。権限レベルに基づくプリミティブの整理・開示と、MCP サーバー自体の整理（Registry WG の担当）はスコープ外です。Goals には、要件と経験の文書化、grouping・tool-search・code-mode といった多様な整理戦略のリファレンス拡張の支援、大規模な MCP サーバーとクライアントに独自実装から標準化された拡張への移行を促すこと、の 3 つが挙がっています。

旧 Primitive Grouping IG の憲章と比べると、ここまでの内容はグループ名と「IG」→「WG」の置き換え以外は同じ文面で、違いは体制と運営に集中しています。Leadership には、ファシリテーターの Tapan Chugh（University of Washington）と Sam Morrow（GitHub）に加え、Maintainer として Cliff Hall（Futurescale）、Core Maintainer として Kurtis Van Gent（Google）が並び、4 名になりました。旧憲章にあったメンバー表（Membership）は無くなり、代わりに意思決定権限の表（Authority & Decision Rights）が 8 行で新設されています。会議のロジスティクスとスケジューリング・WG 内の提案の優先順位付け・スコープ内の SEP のトリアージとクローズ（根拠の文書化が条件）は WG リードの裁量です。スコープ内の技術設計は WG のコンセンサス、追加的な仕様変更は WG のコンセンサスに加えて Core Maintainer の承認、破壊的・根本的な仕様変更ではさらに広範なレビューも必要です。スコープの拡大には Core Maintainer の承認が必須で、WG メンバーの承認は WG メンバーのスポンサーによる、という構成です。

運営面では、会議の頻度が「TBD」から「Weekly」（週次）に決まり、会議が meet.modelcontextprotocol.io に掲載されることが追記されました（所要時間は TBD のまま）。Discord のチャンネル名は `#primitive-grouping-ig` から `#progressive-disclosure-wg` に変わりましたが、リンク先のチャンネル ID は旧憲章と同じです。リポジトリは実験用の `experimental-ext-grouping` から Working Group 用の `progressive-disclosure-wg` に移り、Organization Strategies 節が参照する Approaches 文書もこちらのリポジトリを指すようになりました。Lifecycle の状態は「Active Exploration」のままですが、IG から WG への移行条件を定めていた「Graduation Criteria (IG → WG)」節は削除され、Retirement Criteria だけが残っています。Success Criteria は短期・中期・長期の中身はそのままで、新設された「Deliverables & Success Metrics」節の下に移りました。Related Groups からは Registry WG と Security IG が外れ、Tool Annotations IG と Skills Over MCP WG の 2 件になっています（Registry WG には Problem Statement のスコープ外の項目で引き続き言及しています）。

- [Progressive Disclosure Charter - MCP Docs](https://modelcontextprotocol.io/community/working-groups/progressive-disclosure)

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
今回の対象期間に大幅な更新（本文 50 行以上の変更）があった既存ページはありません。Primitive Grouping Charter の本文 132 行の削除は、改称に伴って別の URL へ移ったことによるもので（ハイライト 1・2 参照）、ページの更新ではなく削除として「軽微な更新」で扱います。
<!-- light:updated-pages:end -->

## 軽微な更新

<!-- light:minor-updates:start -->
今回差分が出たファイルは `llms-full.txt` の 1 件のみです。Progressive Disclosure Charter 本文の収録は「新規追加されたページ」で扱い、ここでは残る 2 点を挙げます。

**その他**

- Primitive Grouping Interest Group の憲章本文 132 行（区切りの空行を含む）を `llms-full.txt` から削除。前回の取り込みで索引から外れた後も残っていた本文で、Progressive Disclosure Charter に置き換わった（詳細はハイライト 1・2 参照）
- Skills Over MCP Working Group の憲章で、In Scope の Cross-Cutting Concerns と Related Groups にあった「Primitive Grouping IG」の言及 2 箇所を、Progressive Disclosure WG へのサイト内リンクに書き換え（詳細はハイライト 2 参照） — [Skills Over MCP Charter](https://modelcontextprotocol.io/community/working-groups/skills-over-mcp#related-groups)
<!-- light:minor-updates:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-10-13.md](./archives/latest/2026-10-13.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-10-13.md](./archives/latest-detail/2026-10-13.md)

<!--
base_commit: fff3c0a4cd3191932565fb654f66a1d7539bbc49
head_commit: eeed0d5ebbc9b23608e5903e7bc33bb6c996a581
generated_at_full: 2026-10-15T15:24:11+09:00
-->
