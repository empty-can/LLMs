---
対象期間: 2026年11月12日 〜 2026年11月13日
作成日: 2026-11-13
---

# MCP 公式ドキュメント更新サマリ

```markdown
今回の対象期間の取り込みは 1 回で、MCP の差分は `llms-full.txt` の追加 94 行・削除 82 行（23 ページ）でした。新規ページも大幅更新もなく、文面が変わったのは Project Policies と Contributor Ladder の 2 ページ（追加 12 行）だけで、残る 21 ページは書式だけの変更です。

主要なものを以下に挙げます。

1. Project Policies に h2「EU Cyber Resilience Act (CRA) stewardship」が加わった。悪用されている脆弱性や重大なインシデントを知ったメンテナーは、Discord の `#security-disclosures` で Core Maintainer か Lead Maintainer にすぐ知らせ、その人が Linux Foundation の CRA steward と連絡を取る。報告する人は、こうした場合も private advisory を使う
2. 21 ページの 81 行で、英数字に挟まれた `\_` のエスケープ（105 か所）がすべて外れた（`claude\_desktop\_config.json` → `claude_desktop_config.json` など）。`\_meta` などの 120 か所は残っている
```

## ハイライト

1. [**悪用されている脆弱性と重大なインシデントの扱いが Project Policies に書かれた**](./latest-detail.md#1-悪用されている脆弱性と重大なインシデントの扱いが-project-policies-に書かれた):  
  Project Policies に h2「EU Cyber Resilience Act (CRA) stewardship」が新設された。悪用されている脆弱性や重大なインシデントを知ったメンテナーは、問題を直しながら Discord の `#security-disclosures` で Core Maintainer か Lead Maintainer にすぐ知らせ、その人が Linux Foundation の CRA steward に連絡する。Reporting a vulnerability には、こうした緊急の報告も private advisory で行うという段落が、Contributor Ladder の Escalation には、この規則に従うよう求める段落が加わった。
2. [**21 ページで英数字に挟まれたアンダースコアのエスケープが外れた**](./latest-detail.md#2-21-ページで英数字に挟まれたアンダースコアのエスケープが外れた):  
  `llms-full.txt` の 21 ページの 81 行で、英数字に挟まれた `\_` が `_` になった。base にあった 105 か所がすべて外れ、ほかの違いはない。語頭の `\_meta` などの 120 か所は残っている。SEP-1686 では強調の書き方が 1 行変わった。どちらも表示される文字は変わらない。

## 新規追加されたページ

今回の対象期間に新たに追加されたページはありません。索引 `llms.txt` に変更はなく、索引のエントリ数（365 件）と本文 `llms-full.txt` の収録ページ数（160 件。URL としては 159 件）はどちらも前回と同じです。

## 大幅に更新されたページ

今回の対象期間に大幅な更新（本文 50 行以上の変更）があったページはありません。生の差分の行数が最も多い Schema Reference も 42 行（21 組で、すべて `\_` のエスケープ）で、文面の変更が最も多い Project Policies も追加 10 行です。差分のあった 23 ページは、いずれも「軽微な更新」で扱います。

## 軽微な更新

今回差分が出たファイルは `llms-full.txt` の 1 件で、差分のあった 23 ページのうち、文面が変わったのは 2 ページ、残る 21 ページは書式だけの変更でした。

**新機能**

- Project Policies に h2「EU Cyber Resilience Act (CRA) stewardship」が加わった。悪用されている脆弱性や重大なインシデントを知ったメンテナーは、問題を直しながら Discord の `#security-disclosures` で Core Maintainer か Lead Maintainer にすぐ知らせ、その人が Linux Foundation の CRA steward に連絡して以後のやり取りを受け持つ（詳細はハイライト 1 参照） — [Project Policies](https://modelcontextprotocol.io/community/policies#eu-cyber-resilience-act-cra-stewardship)

**機能改善**

- Project Policies の Reporting a vulnerability に、private advisory は緊急のセキュリティ報告の仕組みでもあり、悪用されている脆弱性や重大なインシデントもそれで報告して、報告の冒頭にその旨を書く、という段落が加わった（詳細はハイライト 1 参照） — [Project Policies](https://modelcontextprotocol.io/community/policies#reporting-a-vulnerability)
- Contributor Ladder の Escalation に、悪用されている脆弱性や重大なインシデントを知ったメンテナーは Project Policies の CRA のエスカレーションの規則に従う、という段落が加わった（詳細はハイライト 1 参照） — [Contributor Ladder](https://modelcontextprotocol.io/community/contributor-ladder#escalation)

**その他**

- 21 ページの 81 行で、英数字に挟まれた `\_` のエスケープが外れた。表示は変わらない。ドキュメントが 4 ページ（Build an MCP server・Debugging・Protocol eras・Security Best Practices）、仕様が 3 ページ（Client Registration・Sampling・Schema Reference）、コミュニティが 4 ページ（Enterprise Interest Group Charter・Project Policies・Inspector V2 Working Group Charter・Registry Charter）、SEP が 10 ページ（SEP-985・986・991・1036・1577・1730・2164・2322・2468・2567）（詳細はハイライト 2 参照）
- SEP-1686: Tasks の Motivation で、Code Migration Workflows の行頭の強調の書き方が `***Challenge*:**` から `**_Challenge_:**` になった。表示は同じ（詳細はハイライト 2 参照） — [SEP-1686: Tasks](https://modelcontextprotocol.io/seps/1686-tasks#motivation)

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-11-12.md](./archives/latest/2026-11-12.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-11-12.md](./archives/latest-detail/2026-11-12.md)

<!--
base_commit: 77f196ce342a0c6130e111a1fa66ada14d87a243
head_commit: 1e8d14825866e74000053b24496de73f02e2e71f
generated_at_full: 2026-11-14T15:39:58+09:00
-->
