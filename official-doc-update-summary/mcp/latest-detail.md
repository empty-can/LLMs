---
対象期間: 2026年09月23日 〜 2026年09月23日
作成日: 2026-09-23
---

# MCP 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
今回の対象期間の変更は小規模で、本文 `llms-full.txt` では入門ページ「What is the Model Context Protocol (MCP)?」の 1 ページだけに差分があり（追加 13 行・削除 1 行）、索引 `llms.txt` には Scientific Computing Interest Group の憲章が 1 件加わりました。

主要なものを以下に挙げます。

1. 入門ページ末尾の「Learn more」にセキュリティのベストプラクティスへのカードが加わり、新設の「Community」節から Contributing ガイドへ案内されるようになった
2. Scientific Computing Interest Group の憲章ページが索引に加わった（本文は `llms-full.txt` に未収録）
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**入門ページの案内カードを拡充し Security と Community への導線を追加**](#1-入門ページの案内カードを拡充し-security-と-community-への導線を追加):  
  「What is the Model Context Protocol (MCP)?」ページ末尾の「Learn more」で、既存カードの表題が「Understand concepts」から「Architecture」に改められ、Security Best Practices へのカードが追加された。さらに「Community」節が新設され、Contributing ガイドへのカードが置かれた。
2. [**Scientific Computing Interest Group の憲章ページが索引に追加**](#2-scientific-computing-interest-group-の憲章ページが索引に追加):  
  `community/interest-groups/scientific-computing`（説明文「Charter for the MCP Scientific Computing Interest Group.」）が索引に加わり、エントリは 353 件から 354 件になった。本文は `llms-full.txt` に未収録で、憲章の中身は今回の入力からは確認できない。
<!-- light:highlight-list:end -->

## 1. 入門ページの案内カードを拡充し Security と Community への導線を追加

本文 `llms-full.txt` で今回差分があったのは、仕様 2026-07-28 版の入門ページ「What is the Model Context Protocol (MCP)?」（`docs/2026-07-28/getting-started/intro`）の末尾だけです。本文の説明部分（MCP の概要、What can MCP enable?、Why does MCP matter?、Broad ecosystem support、Start Building）には変更がありません。

「Learn more」節のカード群は、これまで Architecture ページへの 1 枚だけでした。今回、そのカードの表題が「Understand concepts」から「Architecture」に変わり（リンク先と説明文「Learn the core concepts and architecture of MCP」はそのまま）、2 枚目として **Security** カードが加わりました。Security カードは Security Best Practices ページ（`docs/2026-07-28/tutorials/security/security_best_practices`）を指し、「MCP のセキュリティ上の考慮事項とベストプラクティスを理解する」と説明されています。

続けて **「Community」** 節が新設され、Contributing to MCP ページ（`community/contributing`）へのカード「Contributing」（「MCP に参加し貢献する方法を学ぶ」）が置かれました。これにより入門ページの読み手は、構築（Start Building）・理解（Learn more）に加えて、セキュリティの考慮事項とコミュニティ参加の入口にも直接たどり着けるようになっています。

- [What is the Model Context Protocol (MCP)? - MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro#learn-more)
- [What is the Model Context Protocol (MCP)? - MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro#community)

## 2. Scientific Computing Interest Group の憲章ページが索引に追加

索引 `llms.txt` に `- [Scientific Computing Charter](https://modelcontextprotocol.io/community/interest-groups/scientific-computing.md): Charter for the MCP Scientific Computing Interest Group.` の 1 行が追加されました。Interest Group 憲章群のうち Primitive Grouping Charter と Security Charter の間、つまり既存エントリと同じアルファベット順の位置に挿入されており、削除行はありません。索引のエントリは 353 件から 354 件になりました。

ページ本文は `llms-full.txt` に収録されていないため、この Interest Group のミッション・スコープ・体制といった憲章の中身は、今回の入力からは確認できません。`llms-full.txt` 全体を見ても「Scientific Computing」という語は 1 か所も現れず、既存ページからの言及もまだありません。過去にも Transports WG 憲章のように、索引が先に更新され本文が後から収録された例があります。

- [Scientific Computing Charter - MCP Docs](https://modelcontextprotocol.io/community/interest-groups/scientific-computing)

## 新規追加されたページ

<!-- light:new-pages:start -->
- [**Scientific Computing Charter**](#1-scientific-computing-charter) ([MCP Docs](https://modelcontextprotocol.io/community/interest-groups/scientific-computing)):  
  MCP Scientific Computing Interest Group の憲章ページ。今回の差分は索引へのエントリ 1 行の追加だけで、本文は `llms-full.txt` に未収録のため中身は確認できない（詳細はハイライト 2 参照）。
<!-- light:new-pages:end -->

## 1. Scientific Computing Charter

索引に追加されたのは、タイトル `Scientific Computing Charter`・パス `community/interest-groups/scientific-computing`・説明文「Charter for the MCP Scientific Computing Interest Group.」の 1 行です。タイトルは既存の Interest Group 憲章の多くと同じ「話題名 + `Charter`」の形で、説明文も「Charter for the MCP <名称> Interest Group.」という定型に沿っています。

本文が今回の入力に含まれていないため、憲章の内容についてここで述べられることはありません（詳細はハイライト 2 参照）。

- [Scientific Computing Charter - MCP Docs](https://modelcontextprotocol.io/community/interest-groups/scientific-computing)

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
今回の対象期間に大幅な更新（本文 50 行以上の変更）があったページはありません。
<!-- light:updated-pages:end -->

## 軽微な更新

<!-- light:minor-updates:start -->
今回の軽微な更新は、本文に差分があった入門ページ 1 件です。

**機能改善**

- 入門ページ「What is the Model Context Protocol (MCP)?」の「Learn more」で、カード表題を「Understand concepts」から「Architecture」に改め、Security Best Practices へのカードを追加。あわせて「Community」節を新設し Contributing ガイドへのカードを配置（詳細はハイライト 1 参照） — [What is the Model Context Protocol (MCP)?](https://modelcontextprotocol.io/docs/2026-07-28/getting-started/intro#learn-more)
<!-- light:minor-updates:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-09-23.md](./archives/latest/2026-09-23.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-09-23.md](./archives/latest-detail/2026-09-23.md)

<!--
base_commit: 68860adc30f5a3b9e46aeef4cd6db8b1ccdc288e
head_commit: 1cd5f92f259ae91504d3746edb8d0a386ce71bdd
generated_at_full: 2026-09-24T15:00:22+09:00
-->
