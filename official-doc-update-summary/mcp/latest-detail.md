---
対象期間: 2026年10月12日 〜 2026年10月13日
作成日: 2026-10-13
---

# MCP 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
今回の対象期間の変更は索引 `llms.txt` の 2 行だけで、本文 `llms-full.txt` には差分がありません。Working Group の憲章ページが 1 件加わり、Interest Group の憲章ページが 1 件外れました。

主要なものを以下に挙げます。

1. Progressive Disclosure Working Group の憲章ページが索引に加わった（本文は `llms-full.txt` に未収録）
2. Primitive Grouping Interest Group の憲章ページが索引から外れた（本文は `llms-full.txt` に残ったまま）
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**Progressive Disclosure Working Group の憲章ページが索引に追加**](#1-progressive-disclosure-working-group-の憲章ページが索引に追加):  
  `community/working-groups/progressive-disclosure`（説明文「Charter for the MCP Progressive Disclosure Working Group.」）が、Working Group 憲章群の Interceptors Charter と Registry Charter の間に加わった。本文は `llms-full.txt` に未収録で、憲章の中身は今回の入力からは確認できない。
2. [**Primitive Grouping Interest Group の憲章ページが索引から削除**](#2-primitive-grouping-interest-group-の憲章ページが索引から削除):  
  `community/interest-groups/primitive-grouping` のエントリが索引から外れた。一方、今回差分の無い `llms-full.txt` には本文がそのまま残っており、他の憲章ページからの参照も残っている。
<!-- light:highlight-list:end -->

## 1. Progressive Disclosure Working Group の憲章ページが索引に追加

索引 `llms.txt` の Working Group 憲章群に、タイトル `Progressive Disclosure Charter`・パス `community/working-groups/progressive-disclosure`・説明文「Charter for the MCP Progressive Disclosure Working Group.」の 1 行が追加されました。既存エントリと同じアルファベット順で Interceptors Charter と Registry Charter の間に挿入されており、索引に並ぶ Working Group 憲章は 13 件から 14 件になりました。

ページ本文は `llms-full.txt` に収録されていないため、この Working Group のミッション・スコープ・リーダーシップといった憲章の中身は、今回の入力からは確認できません。`llms-full.txt` には `/community/working-groups/progressive-disclosure` を指すリンクも無く、既存ページからの参照もまだありません。過去にも Transports WG 憲章や Enterprise IG 憲章のように、索引が先に更新され、本文が後から収録された例があります。

参考までに、「progressive disclosure」という語は既存の収録ページにも現れます。Skills Over MCP Working Group の憲章は、連携するグループの一つに Primitive Grouping IG を挙げ、その連携テーマを「Progressive disclosure patterns」としています。また Primitive Grouping IG 自身の憲章も、Skills Over MCP WG との関係について「skill discovery and progressive disclosure overlap with grouping」と記しています。同じ取り込みでこの Primitive Grouping IG の憲章が索引から外れていますが（ハイライト 2 参照）、新しい Working Group と Primitive Grouping IG の関係（後継・改称・統合などにあたるかどうか）は、今回の入力からは確認できません。

- [Progressive Disclosure Charter - MCP Docs](https://modelcontextprotocol.io/community/working-groups/progressive-disclosure)

## 2. Primitive Grouping Interest Group の憲章ページが索引から削除

索引 `llms.txt` の Interest Group 憲章群から、タイトル `Primitive Grouping Charter`・パス `community/interest-groups/primitive-grouping`・説明文「Charter for the MCP Primitive Grouping Interest Group.」の 1 行が削除されました。Financial Services Charter と Scientific Computing Charter の間にあったエントリで、索引に並ぶ Interest Group 憲章は 8 件から 7 件になりました。ハイライト 1 の追加と相殺され、索引のエントリ数は 362 件のまま変わっていません。

これまでの憲章ページの追加では、索引が先に更新されて本文が後から収録される例がありましたが、今回は逆に、索引からは外れたものの本文が残っている状態です。今回の取り込みでは `llms-full.txt` に差分が無く、Primitive Grouping Charter の本文はそのまま収録されています。それによると、この Interest Group は、ツール・リソース・プロンプト・タスクといった MCP のプリミティブを、プロトコルが持つフラットな一覧を超えてどう整理できるかを探るグループとされています。状態は「Active Exploration」と記され、Working Group への移行を提案できる条件を定めた「Graduation Criteria (IG → WG)」節もあります。Changelog に記録された初版の制定日は 2026年06月18日 です。

既存ページからの参照も残っています。Scientific Computing Interest Group の憲章は「Related Groups」節で Primitive Grouping IG のページへリンクしており、Skills Over MCP Working Group の憲章も、連携するグループとして Primitive Grouping IG の名前を挙げています。

今回のエントリ削除が、グループの活動終了・Working Group への移行・改称のいずれによるものかは、今回の入力からは確認できません。

- [Scientific Computing Charter - MCP Docs](https://modelcontextprotocol.io/community/interest-groups/scientific-computing#related-groups)
- [Skills Over MCP Charter - MCP Docs](https://modelcontextprotocol.io/community/working-groups/skills-over-mcp#related-groups)

## 新規追加されたページ

<!-- light:new-pages:start -->
- [**Progressive Disclosure Charter**](#1-progressive-disclosure-charter) ([MCP Docs](https://modelcontextprotocol.io/community/working-groups/progressive-disclosure)):  
  MCP Progressive Disclosure Working Group の憲章ページ。今回の差分は索引へのエントリ 1 行の追加だけで、本文は `llms-full.txt` に未収録のため中身は確認できない（詳細はハイライト 1 参照）。
<!-- light:new-pages:end -->

## 1. Progressive Disclosure Charter

索引に追加されたのは、タイトル `Progressive Disclosure Charter`・パス `community/working-groups/progressive-disclosure`・説明文「Charter for the MCP Progressive Disclosure Working Group.」の 1 行です。タイトルは既存の Working Group 憲章の多くと同じ「話題名 + `Charter`」の形で、説明文も「Charter for the MCP <名称> Working Group.」という定型に沿っています。

本文が今回の入力に含まれていないため、憲章の内容についてここで述べられることはありません（詳細はハイライト 1 参照）。

- [Progressive Disclosure Charter - MCP Docs](https://modelcontextprotocol.io/community/working-groups/progressive-disclosure)

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
今回の対象期間に大幅な更新（本文 50 行以上の変更）があったページはありません。
<!-- light:updated-pages:end -->

## 軽微な更新

<!-- light:minor-updates:start -->
今回の差分は索引 `llms.txt` の追加 1 行・削除 1 行のみで、本文 `llms-full.txt` には差分がありません。追加の 1 行は「新規追加されたページ」で扱い、ここでは削除の 1 行を挙げます。

**その他**

- 索引から Primitive Grouping Interest Group の憲章ページ（`community/interest-groups/primitive-grouping`）のエントリを削除。本文は `llms-full.txt` に残っている（詳細はハイライト 2 参照）
<!-- light:minor-updates:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-10-12.md](./archives/latest/2026-10-12.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-10-12.md](./archives/latest-detail/2026-10-12.md)

<!--
base_commit: a96f629ae39d1bbdbc8a90f79fba6100e8de16c0
head_commit: fff3c0a4cd3191932565fb654f66a1d7539bbc49
generated_at_full: 2026-10-14T15:28:59+09:00
-->
