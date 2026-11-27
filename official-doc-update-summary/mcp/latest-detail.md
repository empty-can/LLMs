---
対象期間: 2026年11月24日 〜 2026年11月26日
作成日: 2026-11-26
---

# MCP 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
今回の対象期間の取り込みは 2 回で、差分が出たのはそのうち 1 回です。仕様のリリースの周期を定める新しいページ Release Cycle が加わり、Roadmap・SEP Guidelines・Contributor Ladder・Governance and Stewardship の 4 ページがこの周期に合わせて書き換わりました。

主要なものを以下に挙げます。

1. 新しいページ Release Cycle が加わり、仕様のリリースは 6 か月ごと（おおむね 3 月と 9 月の最終火曜日）で、各リリースは 8 か月の周期を持ち、ソフトフリーズ・ハードフリーズなどの節目があると定められた
2. Roadmap に Next Release の節が加わり、次の仕様のリリースの目標は、これまでの 2026年12月から 2027年03月30日になった
3. SEP Guidelines で、SEP の審査がリリース周期のレビュー期間に行われ、採択は Core Maintainer の過半数が賛成する 7 日間の記録投票で決まるようになった
4. Contributor Ladder に、Maintainer から選ばれる主・副のリリースマネージャーの役割の節が加わった
5. Governance and Stewardship に、ガバナンスの改正の手続き（Lead Maintainer だけが提案でき、Core Maintainer の 3 分の 2 の承認で発効）の節が加わった
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**仕様のリリース周期を定める Release Cycle のページが加わった**](#1-仕様のリリース周期を定める-release-cycle-のページが加わった):  
  新しいページ Release Cycle（`community/release-cycle`、127 行）が加わり、索引 `llms.txt` にもエントリが入った。仕様のリリースは 6 か月ごと、おおむね 3 月と 9 月の最終火曜日に出し、各リリースは 8 か月の周期（前後の周期は 2 か月重なる）を持つ。節目は、計画の開始（リリースの 8 か月前）、Core Maintainer のレビューの開始（6 か月前）、ソフトフリーズ（2.5 か月前）、SDK のベータ（1.5 か月前）、ハードフリーズ（1 か月前）など。SEP の審査キュー、審査の順序、3 週間の正式な審査、Tier 1 の SDK の期限、ハードフリーズ後の重大な修正の手続きも定めている。
2. [**次の仕様のリリースの目標が 2027年03月30日になった**](#2-次の仕様のリリースの目標が-2027年03月30日になった):  
  Roadmap の最終更新日が `2026-08-22` から `2026-11-16` になり、冒頭に Next Release の節が加わった。次の仕様のリリースは 2027年03月30日が目標で、これまでの 2026年12月の目標を置き換える。6 か月のリリース周期での最初のリリースで、2026年08月に済ませた計画を使う。2027年09月のリリースの計画は 2027年01月下旬から、2028年03月のリリースの計画は 2027年07月下旬から始まる。周期の導入より前に開かれた SEP のプルリクエストは有効なままだが、次の正式な審査の前に、スポンサーと SEP の審査キューへの登録が要る。
3. [**SEP の審査がリリース周期のレビュー期間と記録投票に移った**](#3-sep-の審査がリリース周期のレビュー期間と記録投票に移った):  
  SEP Guidelines（追加 25 行・削除 11 行）で、Review and acceptance の節が 1 段落から 7 段落に書き直された。Core Maintainer は、`in-review` の SEP を 2 週ごとの会合で審査するのではなく、リリース周期のレビュー期間（リリースの 6 か月前からソフトフリーズまで）に審査する。採択は、発表の後にスポンサーが開く 7 日間の記録投票で、Core Maintainer の過半数が賛成したときに決まる。あわせて、スポンサーには Working Group のほか Core Maintainer の集団もなれることが冒頭の手順や図に書き加えられ、`in-review` にした SEP は SEP の審査キューに登録するようになった。
4. [**Contributor Ladder にリリースマネージャーの役割が加わった**](#4-contributor-ladder-にリリースマネージャーの役割が加わった):  
  Contributor Ladder の Maintainer の節の下に、Release managers の小節（追加 33 行）が加わった。主・副のリリースマネージャーは Maintainer から選ばれ、自薦した候補が Core Maintainer の過半数の賛成で選ばれる。副は次のリリースで主になる。主はリリースの日程、SEP の審査の日程、ソフトフリーズとハードフリーズ、SDK の準備、リリースの公開と告知をまとめる。リリースの後には振り返りを公開する。
5. [**ガバナンスの文書に改正の手続きの節が加わった**](#5-ガバナンスの文書に改正の手続きの節が加わった):  
  Governance and Stewardship の Technical Governance の節に、Amendments の小節（追加 13 行）が加わった。ガバナンスの構成の改正を提案できるのは Lead Maintainer だけで、改正は Core Maintainer 全員の 3 分の 2 が承認したときに発効する。提案は、理由を添えた書面であること、変更する文言を具体的に含むこと、投票の前に 5 日以上の意見募集の期間を置くこと、Core Maintainer の記録投票で決めることが求められ、承認された改正には LF Projects, LLC の承認も要る。SEP Guidelines の改正の手続きへのリンクも、SEP-2085 からこの節に替わった。
<!-- light:highlight-list:end -->

## 1. 仕様のリリース周期を定める Release Cycle のページが加わった

今回の対象期間の取り込みは 2 回で、2026年11月26日の実行分では入力の 2 ファイルとも差分がなく、2026年11月27日の実行分で 2 ファイルとも差分が出ました。本文 `llms-full.txt` は追加 210 行・削除 15 行で、総行数は 47,779 行から 47,974 行に、収録ページ数は 164 件から 165 件（`examples` が 2 回収録されているため、URL としては 163 件から 164 件）になりました。索引 `llms.txt` は追加 1 行で、エントリ数は 365 件から 366 件になっています（軽微な更新の「その他」参照）。

`llms-full.txt` の差分の内訳は次のとおりです。行数は、ページのタイトルの行（`# `）から次のページの直前までを数えたものです。

| ページ | 行数 | 追加 | 削除 | 扱い |
|---|---|---|---|---|
| Release Cycle（新規ページ） | — → 127 | 127 | 0 | 新規追加（このハイライト） |
| Contributor Ladder | 164 → 197 | 36 | 3 | 軽微な更新（ハイライト 4） |
| SEP Guidelines | 148 → 162 | 25 | 11 | 軽微な更新（ハイライト 3） |
| Governance and Stewardship | 130 → 143 | 13 | 0 | 軽微な更新（ハイライト 5） |
| Roadmap | 101 → 109 | 9 | 1 | 軽微な更新（ハイライト 2） |
| 計 | | 210 | 15 | |

既存の 4 ページの変更はどれも 50 行未満で、軽微な更新に当たります。5 ページの変更は、いずれも新しいリリース周期の導入に関わるものです。SEP 一覧（変更なし）で Status が Accepted の Process SEP、SEP-3398: Release Cycle Updates（ページは変更なし）は、2026年12月の目標を 2027年03月30日へ移すこと、主・副のリリースマネージャー、公開の SEP の審査キューなどを提案しており、今回の各ページの記述はこの提案と対応しています。

新しいページは Release Cycle（`community/release-cycle`）で、索引の説明文は「Release milestones and deadlines for SEP authors and SDK maintainers.」です。本文 `llms-full.txt` では Project Policies と SDK Tiers の間に、索引 `llms.txt` では Roadmap の後、Governance and Stewardship の前に置かれています。

ページは、MCP の仕様のリリースは 6 か月ごとに、おおむね 3 月と 9 月の最終火曜日に公開する、と始まります。各リリースは 8 か月の周期を持ち、次のリリースの計画は今のリリースの公開の 2 か月前に始まるので、前後の周期は 2 か月重なります。節目の間隔は暦の月で数え、各リリースの正確な日付は、計画の始めにリリースマネージャーがリリースのページ（`voting.modelcontextprotocol.io/p/releases`）で公開します。各節の内容は「新規追加されたページ」で扱います。

- [Release Cycle - MCP Docs](https://modelcontextprotocol.io/community/release-cycle#schedule)
- [Release Cycle - MCP Docs](https://modelcontextprotocol.io/community/release-cycle#milestones)

## 2. 次の仕様のリリースの目標が 2027年03月30日になった

Roadmap（101 行から 109 行、追加 9 行・削除 1 行）では、冒頭の注記の最終更新日（Last updated）が `2026-08-22` から `2026-11-16` になり、2 つの注記の後、SEP Prioritization の節の前に、Next Release の節が加わりました。節は 3 段落です。

- **次のリリース**: 次の仕様のリリースは **2027年03月30日** が目標で、これまでの 2026年12月の目標を置き換える。6 か月の[リリース周期](https://modelcontextprotocol.io/community/release-cycle)での最初のリリースで、2026年08月に済ませた計画を使う。Core Maintainer のレビュー期間は、リリースの **2.5 か月前** のソフトフリーズの日に閉じる。正確な節目の日付と、このリリースが目標とする SEP は `2027-03-30` のリリースのページに、予定されたレビューの会合はレビューの議題のページ（いずれも `voting.modelcontextprotocol.io`）に載っている
- **その先の計画**: 2027年09月のリリースの計画は 2027年01月下旬に、2028年03月のリリースの計画は 2027年07月下旬に始まる
- **既存の SEP の扱い**: リリース周期の導入より前に開かれた SEP のプルリクエストは有効なままで、番号・議論・済んだ決定を保ち、作者は閉じて作り直す必要はない。ただし次の正式な審査の前に、それぞれ Working Group か Core Maintainer の集団の[スポンサー](https://modelcontextprotocol.io/community/sep-guidelines#sponsors)と、[SEP の審査キュー](https://modelcontextprotocol.io/community/release-cycle#sep-review-queue)への登録が要る。すでに採択された提案は採択のままだが、このリリースに含まれるには、ソフトフリーズの日までに Final になってマージされていなければならない

直近の仕様のリリースは `2026-07-28` 版で、2027年03月30日はその次の版に当たります（2027年03月の最終火曜日です）。

- [Roadmap - MCP Docs](https://modelcontextprotocol.io/development/roadmap#next-release)

## 3. SEP の審査がリリース周期のレビュー期間と記録投票に移った

SEP Guidelines（148 行から 162 行、追加 25 行・削除 11 行）では、審査と採択の進め方がリリース周期に合わせて書き換わり、スポンサーになれる集団の書き方も改まりました。

**Review and acceptance**: 旧版は「Core Maintainer は `in-review` の SEP を、2 週ごとの会合で意思決定の手続き（decision process）に沿って審査する。基準は動く試作、MCP のエコシステムへの明確な利点、コミュニティの支持と合意、ロードマップと設計の原則への適合。結果は `accepted`・`rejected`、または PR に記録した具体的なフィードバックを添えた `draft` への差し戻し」という 1 段落でした。新版は次の 7 段落です。

- **審査の時期**: Core Maintainer は `in-review` の SEP を、[リリース周期のレビュー期間](https://modelcontextprotocol.io/community/release-cycle#milestones)、つまりリリースの **6 か月前** からソフトフリーズの日までに審査する。リリースマネージャーが各会合の **2 週間前** に議題と提案へのリンクを公開する。審査で考慮するのは、動く試作、エコシステムへの利点、コミュニティの支持と合意、ロードマップと設計の原則への適合
- **審査の順序**: リリースマネージャーは SEP の審査キューを、ロードマップとの合致、次に各提案が審査の準備を整えた日の順に並べる
- **投票**: 発表の後、スポンサーが 7 暦日の記録投票を開き、その記録を SEP の PR から張る。採択には Core Maintainer の過半数の賛成が要る。投票は 7 日間ずっと開いたままで、ソフトフリーズの日より前に終わらなければならない
- **結果の記録**: スポンサーは、票数・決定・理由・フォローアップを PR と SEP の審査キューに記録する。Core Maintainer の過半数が反対すれば `rejected` になり、今の形では先に進まない。作者はフィードバックをもとに改めて再提出できる。どちらの基準にも届かなければ `draft` に戻る
- **投票の資格**: Lead Maintainer を含む現在の Core Maintainer 全員に資格があり、名誉（emeritus）のメンバーには無い。投票の記録には資格のある投票者と投票の対象の版を載せる。棄権と欠席は賛成に数えず、会合の出席者の過半数だけでは足りない
- **投票中の変更**: 投票中に提案が実質的に変われば審査に戻り、前の版への票は引き継がれない。レビュー期間が閉じるまでに終われない投票は、次のレビュー期間に回す
- **Lead Maintainer の権限**: Lead Maintainer は既存の権限を保つ。ガバナンスを改正する提案は、より厳しい[ガバナンスの改正の手続き](https://modelcontextprotocol.io/community/governance#amendments)の要件も満たさなければならない（ハイライト 5 参照）

**スポンサーと Workflow**: 冒頭の Before you write の節の「SEP は正式な審査の前に、スポンサーになる Working Group が要る」が、「Working Group か Core Maintainer の集団のスポンサーが要る。ほとんどの提案は Working Group から始まる」になりました。Core Maintainer がスポンサーになれること自体は、Sponsors の節（変更なし）に既にありました。Workflow の節では次の箇所が変わっています。

| 箇所 | 旧 | 新 |
|---|---|---|
| 図の 2 本の矢印のラベル | Working group agrees to sponsor | Working group or Core Maintainers agree to sponsor |
| 手順 4 | Working Group がスポンサーに同意するまでは draft の PR のまま | Working Group か Core Maintainer がスポンサーに同意するまでは draft の PR のまま |
| 手順 5 | Working Group がスポンサーに同意したら PR を ready for review にする | 集団（a group）がスポンサーに同意したら PR を ready for review にする |
| 手順 6 | スポンサーは、事前の議論があって PR の説明に張られていることを確かめ、`in-review` にして Core Maintainer の会合の議題に載せる | スポンサーは、スポンサーの決定と事前の議論が PR の説明に張られていることを確かめてから `in-review` にする。WG の Lead かスポンサーの Core Maintainer が、SEP を [SEP の審査キュー](https://voting.modelcontextprotocol.io/p/seps)に登録し、リリースマネージャーがリリース周期のレビュー期間に審査の日程を組む |
| Status の表の `in-review` | 正式な審査のために Core Maintainer の議題に載っている | SEP の審査キューにあるか、正式な審査のために Core Maintainer の議題に載っている |

ほかに、冒頭の説明が短くなり、SEP の手続きを定めた SEP-1850、適合性の関門を定めた SEP-2484、スポンサーの規則の根拠の SEP-3398 への言及が外れました（SEP-2484 は Conformance Test Requirement の節に残っています）。When you need a SEP の節では、ガバナンスの文書自体の改正が従う手続きのリンク先が、SEP-2085 から Governance and Stewardship の Amendments の節に替わっています（軽微な更新の「その他」参照）。

- [SEP Guidelines - MCP Docs](https://modelcontextprotocol.io/community/sep-guidelines#review-and-acceptance)
- [SEP Guidelines - MCP Docs](https://modelcontextprotocol.io/community/sep-guidelines#workflow)

## 4. Contributor Ladder にリリースマネージャーの役割が加わった

Contributor Ladder（164 行から 197 行、追加 36 行・削除 3 行）では、Maintainer の節の末尾（Minimum time の後、Core Maintainer の節の前）に、`###` の小節 Release managers（追加 33 行）が加わりました。

- **選び方**: 主（primary）と副（secondary）のリリースマネージャーは、プロジェクトの Maintainer から選ぶ。Maintainer は自薦でき、候補は [Core Maintainer](https://modelcontextprotocol.io/community/contributor-ladder#core-maintainer) の過半数が賛成したときに選ばれる。投票する集団には Lead Maintainer を含み、名誉のメンバーは含まない。リリースマネージャーが務められなくなったら、Core Maintainer が同じ推薦と投票で後任を選べる
- **引き継ぎ**: 副は次のリリースで主になり、Core Maintainer はそのリリースの計画が始まる前に新しい副を選ぶ。最初のリリースの主は、副を務めた経験がなくてよい
- **主の役割**: リリースの日程、SEP の審査の日程、ソフトフリーズとハードフリーズ、SDK の準備、リリースの公開、リリースの告知の 6 つをまとめる
- **副の役割**: [SEP の審査キュー](https://modelcontextprotocol.io/community/release-cycle#sep-review-queue)と引き継ぎのメモの保守を助けながら、次のリリース周期を率いる準備をする
- **周期の重なり**: リリース周期は 2 か月重なり、その間、副は次の周期の主も兼ね、新しい副とともにその計画を率いる。退く主は、今のリリースが公開されるまで責任を持ち、リリースの日にリリースマネージャーたちが、残った課題とその担当者を引き継ぎのメモにまとめる
- **振り返り**: 各リリースの後、リリースマネージャーは振り返りを公開する。SEP の審査キューの待ち時間、ソフトフリーズ時点の準備の度合い、SDK のベータの提供状況、ハードフリーズ後の重大な修正、周期が重なる間のリリースマネージャーの負荷を扱う
- **Core Maintainer との関係**: 行き詰まったリリースマネージャーは、決定を Core Maintainer に上げられる。SEP の採否とハードフリーズ後のあらゆる変更の承認は Core Maintainer が行い、Core Maintainer はリリースマネージャーに必要なアクセスと資源を用意して、Core Maintainer の会合に招く
- **参照先**: 日程と期限は [Release Cycle](https://modelcontextprotocol.io/community/release-cycle) のページが定め、現在のリリースマネージャーは `MAINTAINERS.md` の名簿に載っている

同じページの Roles at a glance の表では、Core Maintainer・Lead Maintainer・Community Moderator の 3 行で、句読点だけが変わりました（`;` が `.` に、`Member status; parallel track` が `Member status, parallel track` に。軽微な更新の「その他」参照）。

- [Contributor Ladder - MCP Docs](https://modelcontextprotocol.io/community/contributor-ladder#release-managers)

## 5. ガバナンスの文書に改正の手続きの節が加わった

Governance and Stewardship（130 行から 143 行、追加 13 行）では、Technical Governance の節の Decision Process の小節の後、Processes の節の前に、`###` の小節 Amendments が加わりました。

- **提案と発効**: このガバナンスの構成の改正を提案できるのは Lead Maintainer だけで、改正は Core Maintainer 全員の 3 分の 2 が承認したときに発効する
- **提案の要件**: 改正の提案は、(1) 変更の明確な理由を添えて書面で出すこと、(2) 既存のガバナンスの規定を変える具体的な文言を含むこと、(3) 投票の前に 5 日以上の意見募集の期間を置くこと、(4) Core Maintainer の記録投票で決めること、の 4 つを満たさなければならない
- **LF Projects の承認**: 承認された改正には、[General Project Policies](https://modelcontextprotocol.io/community/governance#general-project-policies) にあるとおり、LF Projects, LLC の承認も要る

SEP Guidelines では、ガバナンスの文書自体の改正が SEP の手続きではなくこの手続きに従うことを示すリンクの先が、SEP-2085（Governance Succession and Amendment Procedures。SEP 一覧では Final で、ページは変更なし）からこの節に替わり、Review and acceptance の節にも、ガバナンスを改正する提案はこの手続きの要件も満たす必要があるという文が加わりました（ハイライト 3 参照）。

- [Governance and Stewardship - MCP Docs](https://modelcontextprotocol.io/community/governance#amendments)

## 新規追加されたページ

<!-- light:new-pages:start -->
- [**Release Cycle**](#1-release-cycle) ([MCP Docs](https://modelcontextprotocol.io/community/release-cycle)):  
  仕様のリリースの節目と、SEP の作者・SDK の保守者向けの期限を定めるページ（127 行）。6 か月ごとのリリースと 8 か月の周期、7 つの節目、ソフトフリーズとハードフリーズ、SEP の審査キューと審査の順序、正式な審査の流れ、リリースへの収録の条件、SDK の期限、ハードフリーズ後の重大な修正の手続きをまとめている。索引 `llms.txt` にもエントリが加わった（位置づけはハイライト 1 参照）。
<!-- light:new-pages:end -->

## 1. Release Cycle

Release Cycle は 127 行のページで、タイトルを除く見出しは 11 個（`##` が 5・`###` が 6）です。図が 2 つ（リリース周期の時間軸と、正式な SEP の審査の時間軸）と、表が 1 つあります。各節の要点は次のとおりです。

**日程（Schedule）**: 各リリースは 8 か月の周期を持ち、次のリリースの計画は今のリリースの公開の **2 か月前** に始まります。リリースマネージャー（Contributor Ladder の Release managers の節へのリンク。ハイライト 4 参照）が、計画の始めに各リリースの正確な節目の日付をリリースのページで公開し、節目の間隔は暦の月で数えます。仕様の版の名前にはリリースの日付（`YYYY-MM-DD` の形式）を使います。図は、3 月と 9 月のリリース周期がそれぞれ計画・Core Maintainer のレビュー・安定化の段階を持ち、2 か月重なって、6 か月おきにリリースされる様子を示しています。

**節目（Milestones）**: 7 つの節目を表にしています。

| 節目 | リリースの何か月前 | 結果 |
|---|---|---|
| Planning begins | 8 | Core Maintainer がロードマップを提案し、Maintainer と Working Group から意見を集める |
| Core Maintainer review opens | 6 | 優先事項が公開され、予定した SEP の審査が始まる |
| Soft freeze | 2.5 | 審査が閉じる。含める SEP は Final でマージ済みでなければならない |
| Next-cycle planning begins | 2 | 次のリリースの計画が始まる |
| SDK beta | 1.5 | Tier 1 の SDK が、凍結した仕様に対応するベータを出す |
| Hard freeze | 1 | 仕様の変更は重大な修正に限られる |
| Release | 0 | 仕様、リリースノート、実装と移行の手引き、SDK の準備の概要が公開される |

計画の間、Core Maintainer は今後 6〜12 か月の優先事項を、Working Group と SDK をまたぐ依存関係とともに Roadmap に公開します。ロードマップに沿う提案は審査で優先されますが、ロードマップに載っていても採択や特定のリリースへの収録は保証されません。

- **ソフトフリーズ（Soft freeze）**: リリースの **2.5 か月前** にリリースの範囲が固まる。リリースマネージャーは凍結した範囲と見送った提案の一覧を公開し、ハードフリーズまでは、その範囲の中のバグ修正・磨き上げ・明確化だけをマージできる。新しい機能と大きな設計のやり直しは後の周期に回る
- **ハードフリーズ（Hard freeze）**: リリースの **1 か月前** から、仕様は重大な修正のためだけに変わる。重大な修正とは、重大なセキュリティの脆弱性か、リリースを妨げる正しさや相互運用性の欠陥に対処するもので、それぞれ後述の重大な修正の手続きに従い、記録投票で Core Maintainer の過半数の承認を得なければならない

**SEP の審査と収録（SEP review and inclusion）**: スポンサー・提出・Final への移行は SEP Guidelines の Workflow に従います。Working Group の Lead か Core Maintainer が、提案を SEP の審査キュー（`voting.modelcontextprotocol.io/p/seps`）に出します。キューは一年中受け付けますが、出しても審査の時間やリリースへの収録は保証されません。

- **SEP の審査キュー（SEP review queue）**: リリースマネージャーが保守し、各項目には、提案へのリンク、スポンサーの集団とその代表、割り当てられていればスポンサー、正式な審査（formal review）か事前の審査（pre-review）か、準備が整った日・ロードマップとの合致・目標とする審査の周期、を記録する。正式な審査の項目は仕様のリポジトリの SEP の PR に張る（拡張のリポジトリではなく仕様のリポジトリで提案される Extensions Track の SEP も含む）。事前の審査の項目は、Working Group や拡張のリポジトリなど、どこにある初期の提案に張ってもよく、SEP の番号やスポンサーの集団の承認はまだ要らない。事前の審査は、提案が仕上がる前に方向性・依存関係・大きな懸念を議論するためのもので、作者はフィードバックを得るが、承認やリリースの枠の確保にはならない
- **審査の日程（Review scheduling）**: 正式な審査は、レビュー期間の中の通常の Core Maintainer の会合で行う。リリースマネージャーは各会合の議題を、(1) 正式な審査の準備が整った提案を事前の審査より先に、(2) それぞれの中でロードマップに沿う提案を先に、(3) 合致の度合いが同じなら準備が整った日の古い順に、の順で組む。この順序の例外は理由をキューに記録する。議題が埋まっていただけで見送られた提案は準備が整った日を保ち、大きな手直しのために差し戻された提案は、再提出のときに新しい日付を受け取る
- **正式な審査（Formal review）**: 議題の公開から投票の終わりまで 3 週間かかる。会合の **2 週間前** に、リリースマネージャーが Core Maintainer とともに準備の整った提案を選んで議題とリンクを公開し、作者と、Working Group の Lead またはスポンサーの Core Maintainer を会合に招く。会合の前の 1 週間に、審査者が PR にコメントし、作者とスポンサーが応じて議論の要る問いを洗い出す。会合では作者・Working Group の Lead・スポンサーの Core Maintainer のいずれかが提案と残った問いと実装のフィードバックを発表し、その後スポンサーが採択の投票を開く。投票は **7 暦日** 開いたままにする
- **リリースへの収録（Inclusion in a release）**: SEP は、スポンサーが仕様の変更・参照実装・必要な適合性試験を含むすべての成果物を確かめたときに Final になる。リリースに含まれるには、ソフトフリーズの日までに Final になって PR がマージされていなければならない。未完の提案のためにリリースの日は動かず、ソフトフリーズに間に合わなかった SEP は後のリリースで検討される。採択済みの SEP は、大きな設計のやり直しで再審査が要らない限り Status を保ち、決定待ちの提案も Status を保って審査キューに戻る。将来のリリース向けの変更は、今のリリースが公開されるまで提案のブランチや PR に置いておく。フリーズは始まった時点でマージされていないものすべてにかかり、採択済みの SEP や投票中の SEP も例外ではない。レビュー期間はすべての種類の SEP に適用されるが、Process と Informational の SEP は仕様の公開とは関係なく採択と実施の後に効力を持ち、拡張はその公開のライフサイクルに従う

**SDK の期限（SDK deadlines）**: SDK の保守者は SEP が採択されたらすぐ実装を始め、仕様のあいまいな点を、修正をまだマージできるうちに作者とスポンサーに伝えるよう求めています。SEP が Final になるのに SDK の実装は要りません。Tier 1 の SDK は、リリースの **1.5 か月前** にベータを、仕様の公開前に安定版を出します。ベータは、クライアントとサーバーの開発者がハードフリーズの前に問題を報告できる半月を生みます。この期限は階層づけのポリシーが求める機能に限り、実験的な機能や拡張は含みません。ほかの階層の SDK も同じ日程でベータを出すことが勧められています。ベータのリリースノートには、目標の仕様のリリース、使える機能、既知の不足、フィードバックの送り先を書きます。SDK の保守者はリリースマネージャーと協力して、公開の準備の概要（SDK の版、適合性の結果、不足、担当者、解決の見込みの日付）を最新に保ちます。ベータや安定版の期限に遅れたら、リリースマネージャーが Core Maintainer と SDK Working Group に上げてリリースの手引きで報告しますが、SDK の遅れで仕様のリリースが延びたり、SDK の階層が自動で変わったりはしません。

**重大な修正（Critical fixes）**: ハードフリーズの後、主のリリースマネージャーが、通常の PR を通じて重大な修正のそれぞれをまとめます。別の SEP、スポンサー、会合での発表は要りません。手順は次の 4 つです。

1. 主のリリースマネージャーが、変更がハードフリーズの基準を満たすことを確かめる。PR には、欠陥、次のリリースまで待てない理由、欠陥を直す最小の変更、SDK とリリースの成果物への影響を書く
2. 主のリリースマネージャーが、資格のある Core Maintainer 全員の記録投票を開く。投票はレビュー期間の外でもよい。7 日間の投票期間を縮めることもできるが、資格のある Core Maintainer 全員に締め切りと理由を知らせなければならない
3. 影響を受ける実装の保守者が変更を見直し、関係する回帰試験と適合性の確認を行う。変更がプロトコルの観察できる挙動を変えるなら、適合性試験を更新する
4. 承認と検証の後に PR をマージする。主のリリースマネージャーは投票・決定・検証の結果を記録し、影響を受ける SDK の保守者に知らせ、準備の概要とリリースノートを更新する

欠陥をリリースの前に安全に直せないときは、その機能とそれに依存する変更を、同じ手続きと投票でリリースから外せます。仕様の残りは予定どおりリリースされます。セキュリティに関わる詳細はセキュリティの開示の手続きに従い、決定と検証の記録は、公表の禁止期間（embargo）の間は限られたチャンネルに置かれ、開示が許されたときに公開されます。

- [Release Cycle - MCP Docs](https://modelcontextprotocol.io/community/release-cycle#milestones)
- [Release Cycle - MCP Docs](https://modelcontextprotocol.io/community/release-cycle#sep-review-queue)
- [Release Cycle - MCP Docs](https://modelcontextprotocol.io/community/release-cycle#formal-review)
- [Release Cycle - MCP Docs](https://modelcontextprotocol.io/community/release-cycle#sdk-deadlines)
- [Release Cycle - MCP Docs](https://modelcontextprotocol.io/community/release-cycle#critical-fixes)

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
今回の対象期間に大幅な更新（本文 50 行以上の変更）があったページはありません。既存ページの変更は 4 ページで計 98 行（追加 83 行・削除 15 行）で、1 ページあたり最大 39 行（Contributor Ladder）にとどまり、すべて軽微な更新に当たります（ハイライト 1 参照）。
<!-- light:updated-pages:end -->

## 軽微な更新

<!-- light:minor-updates:start -->
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
<!-- light:minor-updates:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-11-24.md](./archives/latest/2026-11-24.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-11-24.md](./archives/latest-detail/2026-11-24.md)

<!--
base_commit: 1c6dc5c3f6d9261729fd5a8dbb3dd2389c542149
head_commit: 479f8136ffd1756a957a6892afc01a4896b6be77
generated_at_full: 2026-11-27T15:00:29+09:00
-->
