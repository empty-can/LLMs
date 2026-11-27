---
対象期間: 2026年11月24日 〜 2026年11月26日
作成日: 2026-11-26
---

# MCP 公式ドキュメント更新サマリ

```markdown
今回の対象期間の取り込みは 2 回で、差分が出たのはそのうち 1 回です。仕様のリリースの周期を定める新しいページ Release Cycle が加わり、Roadmap・SEP Guidelines・Contributor Ladder・Governance and Stewardship の 4 ページがこの周期に合わせて書き換わりました。

主要なものを以下に挙げます。

1. 新しいページ Release Cycle が加わり、仕様のリリースは 6 か月ごと（おおむね 3 月と 9 月の最終火曜日）で、各リリースは 8 か月の周期を持ち、ソフトフリーズ・ハードフリーズなどの節目があると定められた
2. Roadmap に Next Release の節が加わり、次の仕様のリリースの目標は、これまでの 2026年12月から 2027年03月30日になった
3. SEP Guidelines で、SEP の審査がリリース周期のレビュー期間に行われ、採択は Core Maintainer の過半数が賛成する 7 日間の記録投票で決まるようになった
4. Contributor Ladder に、Maintainer から選ばれる主・副のリリースマネージャーの役割の節が加わった
5. Governance and Stewardship に、ガバナンスの改正の手続き（Lead Maintainer だけが提案でき、Core Maintainer の 3 分の 2 の承認で発効）の節が加わった
```

## ハイライト

1. [**仕様のリリース周期を定める Release Cycle のページが加わった**](./latest-detail.md#1-仕様のリリース周期を定める-release-cycle-のページが加わった):  
  新しいページ Release Cycle（`community/release-cycle`、127 行）が加わり、索引 `llms.txt` にもエントリが入った。仕様のリリースは 6 か月ごと、おおむね 3 月と 9 月の最終火曜日に出し、各リリースは 8 か月の周期（前後の周期は 2 か月重なる）を持つ。節目は、計画の開始（リリースの 8 か月前）、Core Maintainer のレビューの開始（6 か月前）、ソフトフリーズ（2.5 か月前）、SDK のベータ（1.5 か月前）、ハードフリーズ（1 か月前）など。SEP の審査キュー、審査の順序、3 週間の正式な審査、Tier 1 の SDK の期限、ハードフリーズ後の重大な修正の手続きも定めている。
2. [**次の仕様のリリースの目標が 2027年03月30日になった**](./latest-detail.md#2-次の仕様のリリースの目標が-2027年03月30日になった):  
  Roadmap の最終更新日が `2026-08-22` から `2026-11-16` になり、冒頭に Next Release の節が加わった。次の仕様のリリースは 2027年03月30日が目標で、これまでの 2026年12月の目標を置き換える。6 か月のリリース周期での最初のリリースで、2026年08月に済ませた計画を使う。2027年09月のリリースの計画は 2027年01月下旬から、2028年03月のリリースの計画は 2027年07月下旬から始まる。周期の導入より前に開かれた SEP のプルリクエストは有効なままだが、次の正式な審査の前に、スポンサーと SEP の審査キューへの登録が要る。
3. [**SEP の審査がリリース周期のレビュー期間と記録投票に移った**](./latest-detail.md#3-sep-の審査がリリース周期のレビュー期間と記録投票に移った):  
  SEP Guidelines（追加 25 行・削除 11 行）で、Review and acceptance の節が 1 段落から 7 段落に書き直された。Core Maintainer は、`in-review` の SEP を 2 週ごとの会合で審査するのではなく、リリース周期のレビュー期間（リリースの 6 か月前からソフトフリーズまで）に審査する。採択は、発表の後にスポンサーが開く 7 日間の記録投票で、Core Maintainer の過半数が賛成したときに決まる。あわせて、スポンサーには Working Group のほか Core Maintainer の集団もなれることが冒頭の手順や図に書き加えられ、`in-review` にした SEP は SEP の審査キューに登録するようになった。
4. [**Contributor Ladder にリリースマネージャーの役割が加わった**](./latest-detail.md#4-contributor-ladder-にリリースマネージャーの役割が加わった):  
  Contributor Ladder の Maintainer の節の下に、Release managers の小節（追加 33 行）が加わった。主・副のリリースマネージャーは Maintainer から選ばれ、自薦した候補が Core Maintainer の過半数の賛成で選ばれる。副は次のリリースで主になる。主はリリースの日程、SEP の審査の日程、ソフトフリーズとハードフリーズ、SDK の準備、リリースの公開と告知をまとめる。リリースの後には振り返りを公開する。
5. [**ガバナンスの文書に改正の手続きの節が加わった**](./latest-detail.md#5-ガバナンスの文書に改正の手続きの節が加わった):  
  Governance and Stewardship の Technical Governance の節に、Amendments の小節（追加 13 行）が加わった。ガバナンスの構成の改正を提案できるのは Lead Maintainer だけで、改正は Core Maintainer 全員の 3 分の 2 が承認したときに発効する。提案は、理由を添えた書面であること、変更する文言を具体的に含むこと、投票の前に 5 日以上の意見募集の期間を置くこと、Core Maintainer の記録投票で決めることが求められ、承認された改正には LF Projects, LLC の承認も要る。SEP Guidelines の改正の手続きへのリンクも、SEP-2085 からこの節に替わった。

## 新規追加されたページ

- [**Release Cycle**](./latest-detail.md#1-release-cycle) ([MCP Docs](https://modelcontextprotocol.io/community/release-cycle)):  
  仕様のリリースの節目と、SEP の作者・SDK の保守者向けの期限を定めるページ（127 行）。6 か月ごとのリリースと 8 か月の周期、7 つの節目、ソフトフリーズとハードフリーズ、SEP の審査キューと審査の順序、正式な審査の流れ、リリースへの収録の条件、SDK の期限、ハードフリーズ後の重大な修正の手続きをまとめている。索引 `llms.txt` にもエントリが加わった（位置づけはハイライト 1 参照）。

## 大幅に更新されたページ

今回の対象期間に大幅な更新（本文 50 行以上の変更）があったページはありません。既存ページの変更は 4 ページで計 98 行（追加 83 行・削除 15 行）で、1 ページあたり最大 39 行（Contributor Ladder）にとどまり、すべて軽微な更新に当たります（ハイライト 1 参照）。

## 軽微な更新

今回差分が出たファイルは `llms.txt` と `llms-full.txt` の 2 件で、新規ページ（Release Cycle）のほかに、既存の 4 ページに次の変更がありました。

**新機能**

- Roadmap に Next Release の節を追加し、次の仕様のリリースの目標を 2027年03月30日（これまでの 2026年12月の目標を置き換え）とした（詳細はハイライト 2 参照） — [Roadmap](https://modelcontextprotocol.io/development/roadmap#next-release)
- Contributor Ladder の Maintainer の節に、主・副のリリースマネージャーの選び方と役割を定める Release managers の小節を追加（詳細はハイライト 4 参照） — [Contributor Ladder](https://modelcontextprotocol.io/community/contributor-ladder#release-managers)
- Governance and Stewardship の Technical Governance に、ガバナンスの改正の手続きを定める Amendments の小節を追加（詳細はハイライト 5 参照） — [Governance and Stewardship](https://modelcontextprotocol.io/community/governance#amendments)

**機能改善**

- SEP Guidelines の Review and acceptance を、リリース周期のレビュー期間での審査と、Core Maintainer の過半数の賛成を要する 7 日間の記録投票による採択に書き直した（詳細はハイライト 3 参照） — [SEP Guidelines](https://modelcontextprotocol.io/community/sep-guidelines#review-and-acceptance)
- SEP Guidelines の Workflow で、`in-review` にした SEP を SEP の審査キューに登録し、リリースマネージャーが審査の日程を組む流れにし、Status の表の `in-review` の意味も審査キューを含む形にした（詳細はハイライト 3 参照） — [SEP Guidelines](https://modelcontextprotocol.io/community/sep-guidelines#workflow)
- SEP Guidelines の Before you write と Workflow の図・手順で、スポンサーを Working Group か Core Maintainer の集団とした（詳細はハイライト 3 参照） — [SEP Guidelines](https://modelcontextprotocol.io/community/sep-guidelines#before-you-write)

**その他**

- 索引 `llms.txt` で、Roadmap の次、Governance and Stewardship の前に Release Cycle のエントリ（説明文「Release milestones and deadlines for SEP authors and SDK maintainers.」）を追加。エントリ数は 365 件から 366 件（一意の URL も 366 件）、ファイルは 370 行から 371 行になった（末尾に改行が無いため、改行の数では 369 から 370） — [Release Cycle](https://modelcontextprotocol.io/community/release-cycle)
- SEP Guidelines の冒頭の説明を短くし、SEP-1850・SEP-2484・SEP-3398 への言及を外して、「SEP の手続きの変更には Process SEP が要る」という 1 文にした — [SEP Guidelines](https://modelcontextprotocol.io/community/sep-guidelines)
- SEP Guidelines の When you need a SEP で、ガバナンスの文書自体の改正が従う手続きのリンク先を、SEP-2085 から Governance and Stewardship の Amendments の節に替えた — [SEP Guidelines](https://modelcontextprotocol.io/community/sep-guidelines#when-you-need-a-sep)
- SEP Guidelines の Workflow の手順 3 で、PR の名前の付け替えの文の `;` を `.` に替えて 2 文に分けた — [SEP Guidelines](https://modelcontextprotocol.io/community/sep-guidelines#workflow)
- Contributor Ladder の Roles at a glance の表の 3 行（Core Maintainer・Lead Maintainer・Community Moderator）で、`;` を `.` または `,` に替えた — [Contributor Ladder](https://modelcontextprotocol.io/community/contributor-ladder#roles-at-a-glance)
- Roadmap の冒頭の注記の最終更新日を `2026-08-22` から `2026-11-16` にした — [Roadmap](https://modelcontextprotocol.io/development/roadmap)

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-11-24.md](./archives/latest/2026-11-24.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-11-24.md](./archives/latest-detail/2026-11-24.md)

<!--
base_commit: 1c6dc5c3f6d9261729fd5a8dbb3dd2389c542149
head_commit: 479f8136ffd1756a957a6892afc01a4896b6be77
generated_at_full: 2026-11-27T15:00:29+09:00
-->
