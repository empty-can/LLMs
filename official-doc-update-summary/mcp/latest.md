---
対象期間: 2026年11月19日 〜 2026年11月20日
作成日: 2026-11-20
---

# MCP 公式ドキュメント更新サマリ

```markdown
今回の対象期間の取り込みは 1 回で、新規ページが 1 件（Events 拡張の概要ページ）加わり、既存ページは 5 件で本文が変わりました。前回 SEP-3415 として収録された Events 拡張が、Beta の公式の拡張として拡張の一覧と対応表に載り、Financial Services Interest Group の憲章を書き直す提案も収録されています。

主要なものを以下に挙げます。

1. Events 拡張の概要ページが加わり、拡張の一覧に Beta の公式の拡張として載った。仕様は `ext-events` リポジトリにあり、配信方式は poll・push・webhook の 3 つ
2. 拡張の対応表（Extension Support Matrix）に Events の列が加わり、ChatGPT が Partial（webhook の配信だけ）とされた
3. Financial Services IG の憲章を、まず既存の MCP の仕組みで足りるかを確かめ、残った課題は WG へ持ち込む方針に書き直す提案が載った。会合は月 1 回になる（Core Maintainer の承認が条件）
4. SEP-3415 と Tasks and Events WG の憲章が Events 拡張の公開に追従した。Extension Maintainer は 4 人になり、WG の作業項目では Ideating だった Events の SEP の行が Final の SEP-3415 に置き換わった
```

## ハイライト

1. [**Events 拡張の概要ページが加わり公式の拡張として一覧に載った**](./latest-detail.md#1-events-拡張の概要ページが加わり公式の拡張として一覧に載った):  
  新しいページ Events（`extensions/events/overview`、248 行）が加わり、索引 `llms.txt` にもエントリが入った。ページは、公式の Events 拡張（`io.modelcontextprotocol/events`）の仕様一式が `ext-events` リポジトリにあり、SEP-3415 は Final、拡張は Beta で、Tasks and Events Working Group が保守している、と始まる。Extensions Overview の公式の拡張リポジトリの一覧にも「MCP Events」の小節が加わり、Stage は「Beta, destination not yet stated」とされた。概要ページは、既存の通知では足りない理由、6 段階の流れ、3 つの配信方式、カーソルと配信の保証、セキュリティモデル、クライアントとサーバーの実装の手引きをまとめている。
2. [**拡張の対応表に Events の列が加わり ChatGPT が Partial になった**](./latest-detail.md#2-拡張の対応表に-events-の列が加わり-chatgpt-が-partial-になった):  
  Extension Support Matrix の Extension overview の表に Events の行が、Support matrix の表の右端に Events の列が加わった。`llms-full.txt` で読める Events の対応は ChatGPT の `Partial`（OpenAI の MCP Events の解説へのリンク付き）だけ。新しい注記は、Events の Partial が webhook の配信だけへの対応を意味し、チェックの付いたクライアントは poll・push・webhook のすべてに対応すること、これらの実装のほとんどは SEP-3415 が Final になる前のもので草案の仕様に沿っていることを述べている。
3. [**Financial Services IG の憲章を問題の発見と WG への橋渡しを軸に改める提案が載った**](./latest-detail.md#3-financial-services-ig-の憲章を問題の発見と-wg-への橋渡しを軸に改める提案が載った):  
  Financial Services Charter（追加 67 行・削除 66 行）で、使命・対象範囲・関連グループ・運営・議題が書き直された。既定の進め方は、既存の MCP の仕組みと公開できる業界のパターンで問題に対処できるかを先に確かめ、残ったプロトコルの欠落を適切な WG へ持ち込むことになり、標準化トラックのプロトコル変更を FSIG が単独で受け持つこと（SEP を単独でスポンサーすることを含む）が対象外に加わった。会合は 2 週に 1 回から月 1 回（最長 60 分）になった。Changelog に加わった 2026年11月20日 の行は、これを Core Maintainer の承認を条件とする提案としている。
4. [**SEP-3415 と Tasks and Events WG の憲章が Events 拡張の公開に追従した**](./latest-detail.md#4-sep-3415-と-tasks-and-events-wg-の憲章が-events-拡張の公開に追従した):  
  SEP-3415 では、拡張を所有する WG の名前とリンク先が Tasks and Events Working Group（`community/working-groups/tasks-events`）になり、Extension Maintainer に Luca Chang 氏と Caitie McCaffrey 氏が加わって 4 人になった。「採択されたら公式の拡張リポジトリで公開される」という記述は、仕様は `ext-events` の `specification/beta/events/` で公開されている、という記述に変わった。Tasks and Events Charter では、Resources に `ext-events` と SEP-3415 へのリンクが加わり、Active Work Items の「SEP: Events in MCP v1 RFC」（Ideating）の行が SEP-3415（Final）の行に置き換わった。

## 新規追加されたページ

- [**Events**](./latest-detail.md#1-events) ([MCP Docs](https://modelcontextprotocol.io/extensions/events/overview)):  
  公式の Events 拡張（`io.modelcontextprotocol/events`）の概要ページ（248 行）。既存の通知では足りない理由、6 段階の流れ、poll・push・webhook の配信方式、使いどころ、カーソルと配信の保証、セキュリティモデル、クライアントとサーバーの実装の手引きをまとめている。索引 `llms.txt` にもエントリが加わった（位置づけはハイライト 1 参照）。

## 大幅に更新されたページ

- [**Financial Services Charter**](./latest-detail.md#1-financial-services-charter) ([MCP Docs](https://modelcontextprotocol.io/community/interest-groups/financial-services)):  
  Financial Services Interest Group の憲章（122 行から 123 行、追加 67 行・削除 66 行）。使命・対象範囲・関連グループ・運営・議題が書き直され、会合は月 1 回になり、議題の表は例示の問いの表になった。Changelog は、この変更を Core Maintainer の承認を条件とする提案としている（使命・対象範囲・関連グループはハイライト 3 参照）。

## 軽微な更新

今回差分が出たファイルは `llms.txt` と `llms-full.txt` の 2 件で、新規ページ（Events）と大幅更新（Financial Services Charter）のほかに、次の変更がありました。

**新機能**

- Extensions Overview の「Official Extension Repositories」の節に、`ext-events` リポジトリと Events 拡張（Stage は「Beta, destination not yet stated」）を載せた「MCP Events」の小節を追加（詳細はハイライト 1 参照） — [Extensions Overview](https://modelcontextprotocol.io/extensions/overview#mcp-events)
- Extension Support Matrix の 2 つの表に Events の行と列を加え、Events の Partial の意味を述べる注記を追加（詳細はハイライト 2 参照） — [Extension Support Matrix](https://modelcontextprotocol.io/extensions/client-matrix#support-matrix)

**機能改善**

- SEP-3415: Events Extension で、拡張を所有する WG の名前とリンク先、Extension Maintainer（4 人に）、仕様の公開先（`ext-events` の `specification/beta/events/`）を更新（詳細はハイライト 4 参照） — [SEP-3415: Events Extension](https://modelcontextprotocol.io/seps/3415-events-extension#working-group-and-extension-maintainers)
- Tasks and Events Charter の Resources に Events の拡張リポジトリと仕様へのリンクを加え、Active Work Items の Events の SEP の行を SEP-3415（Final）に差し替え（詳細はハイライト 4 参照） — [Tasks and Events Charter](https://modelcontextprotocol.io/community/working-groups/tasks-events#active-work-items)

**その他**

- 索引 `llms.txt` で、`extensions/` のエントリの末尾（Skills の次、The MCP Registry の前）に Events のエントリ（説明文「Subscribe to events in upstream systems and react when they happen」）を追加。エントリ数は 363 件から 364 件（一意の URL も 364 件）、ファイルは 368 行から 369 行になった（末尾に改行が無いため、改行の数では 367 から 368） — [Events](https://modelcontextprotocol.io/extensions/events/overview)
- SEP-1302: Formalize Working Groups and Interest Groups in MCP Governance（248 行）の、本文 `llms-full.txt` での収録位置が、SEP-1046 の直後（SEP-414 の前）から、Roadmap の直後（SEP-1303 の前）へ移った。移った 248 行は 1 行も変わっておらず、既定の行単位の差分では周りの 76 行を巻き込んで追加・削除とも 324 行に数えられるが（`git diff --histogram` では 248 行ずつ）、本文の変更ではない。索引 `llms.txt` での位置（SEP-1046 と SEP-1303 の間）も変わっていない。2026年11月18日のサマリで扱った SEP-1303 と SEP-1319 の移動と同じく、Roadmap の後ろへの移動 — [SEP-1302: Formalize Working Groups and Interest Groups in MCP Governance](https://modelcontextprotocol.io/seps/1302-formalize-working-groups-and-interest-groups-in-mc)

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-11-19.md](./archives/latest/2026-11-19.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-11-19.md](./archives/latest-detail/2026-11-19.md)

<!--
base_commit: 2864b8c8e49e5201a3575b16751cc5caf78f4b1c
head_commit: 5f51174830a6109f6c27c1eeae6dd98de6f65dde
generated_at_full: 2026-11-21T15:39:58+09:00
-->
