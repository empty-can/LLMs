---
対象期間: 2026年10月10日 〜 2026年10月11日
作成日: 2026-10-11
---

# MCP 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
今回の対象期間の中心は、前回索引 `llms.txt` にだけ載っていた Governance Working Group の憲章の本文が `llms-full.txt` に収録されたことです（追加 185 行）。ほかに、Claude Desktop の対応 OS に Linux が加わった記述修正 2 ページと、Financial Services Interest Group のメンバー追加 1 行があります。

主要なものを以下に挙げます。

1. Governance Working Group の憲章本文が収録され、ガバナンス文書の管理とコミュニティの声を Core Maintainers へ届ける役割、暫定 Lead の体制、月 1 回の運営形態が明らかになった
2. 対象範囲（ガバナンス文書・意思決定の記録・行動規範・コミュニティの価値観など 7 項目）と対象外 6 項目、および「編集上の修正」と「実質的な改訂」を分ける意思決定権限の区分が定められた
3. 2027 年 1〜5 月を期限とする 6 件の作業項目と、6 か月・12 か月の成功基準が示された（憲章は 2026 年 11 月の承認を想定し、現時点では未承認）
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**Governance Working Group の憲章本文が収録**](#1-governance-working-group-の憲章本文が収録):  
  前回は索引への追加のみだった Governance WG 憲章の本文が収録された。ガバナンス文書の管理と、コミュニティの懸念を Core Maintainers へ届ける助言的な窓口を担う。暫定 Lead は Sarah Novotny（任期 1 年以内）で、月 1 回 60 分の作業セッションで運営する。
2. [**対象範囲と意思決定権限の区分**](#2-対象範囲と意思決定権限の区分):  
  ガバナンス文書の管理・意思決定の記録・行動規範の文面・コミュニティの価値観など 7 項目を担い、仕様の策定やメンテナーの選任、個別の行動規範違反の裁定などは対象外とする。字句修正などの「編集上の修正」は Lead が自律的に反映でき、意味を変える「実質的な改訂」は WG の合意と Core Maintainers の承認を要する。
3. [**作業項目と成功基準**](#3-作業項目と成功基準):  
  意思決定記録の規約（2027年01月31日）から「コード以外の貢献方法」ページ（2027年05月31日）まで 6 件の作業項目を掲げる。成功基準は 2026 年 11 月の憲章承認を前提に 6 か月・12 か月の節目で定められている。
<!-- light:highlight-list:end -->

## 1. Governance Working Group の憲章本文が収録

前回の対象期間には、索引 `llms.txt` に `community/working-groups/governance` のエントリが 1 行加わっただけで、本文は `llms-full.txt` に未収録でした。今回、その本文「Governance Working Group Charter」が Filesystems Charter と Infrastructure Charter の間に 185 行（削除なし）で収録され、憲章の中身を確認できるようになりました。これにより `llms-full.txt` は 45,185 行から 45,371 行に、収録ページは 156 件から 157 件になりました。索引 `llms.txt` に変更はありません。

**ミッション**として、この WG は MCP のガバナンスプロセスとコミュニティの価値観を整備・文書化・維持し、プロジェクトの成長に合わせてガバナンス文書を改訂する一元的な場となることを掲げています。あわせて、コミュニティの懸念を Core Maintainers へ届ける助言的な窓口（advisory voice channel）を担い、参加者が contributor ladder を上がっていけるような貢献の文化を育てます。将来的には、意見が割れるガバナンス上の決定について常設の協議の場となり、さらに長期的には MCP 組織全体への代表制によるコミュニティ参加を支えることを目指すとしています。

**体制**は、Lead（暫定）が Sarah Novotny（Independent、Anthropic と契約）で、任期は 1 年以内（NTE 1-year）です。スポンサーは David Soria Parra（@dsp-ant）です。メンバー表には Lead を含む 4 名（ほかに Andreas Schlapbach、Lin Sun（Solo.io）、Peder Holdgaard Pedersen（Saxo Bank / MCP Maintainer & Community Moderator））が載っています。Lead の席が空いた場合は、WG メンバーによる自薦・他薦を受け、WG の合意（lazy consensus、まとまらなければ正式な投票）で選び、Leadership 表は憲章の一部であるため Core Maintainers が憲章改訂として承認します。構造上の規則として「同一組織から Lead は 2 名まで」が定められ、選任時に適用されます。WG メンバーになる要件は標準の WG モデルに従い、3 か月以上の継続的な参加、意味のある貢献（この WG ではガバナンス文書の起草・レビュー・議論の進行）、既存メンバーまたは Lead による推薦、7 日以内に Lead・Core Maintainers・Lead Maintainers から異議が出ないことです。

**運営**は月 1 回 60 分の作業セッション（Working Session）が中心です。議題が無いことを理由に中止しない常設の枠で、議題が決まっていれば Lead が 48 時間前までに `#governance-wg` に掲示します。3 回続けて出席者も議題も無い場合は、Lead が開催頻度の引き下げか WG の解散を Core Maintainers に提案します。オフィスアワーは設けず、質問は `#governance-wg` とプロジェクト全体の Core Maintainer オフィスアワーで受け付けます。議事録用の GitHub Discussions カテゴリ「Meeting Notes - Governance WG」は憲章のセットアップ時に作成予定です。

憲章は v0.1 の位置づけで、Changelog には 2026年05月06日の初版、2026年10月08日の「2026 年 9 月の WG/IG モデルへの整合」に続き、「Core Maintainers による承認」が日付未定（TBD）として記載されています。つまり、本文は公開されたものの憲章自体はまだ承認前です。

- [Governance Working Group Charter - MCP Docs](https://modelcontextprotocol.io/community/working-groups/governance#mission-statement)
- [Governance Working Group Charter - MCP Docs](https://modelcontextprotocol.io/community/working-groups/governance#leadership)

## 2. 対象範囲と意思決定権限の区分

**対象範囲（In Scope）** は次の 7 項目です。

- **ガバナンス文書の管理**: `docs/community/` 配下のガバナンス、contributor ladder、SEP ガイドライン、WG/IG、コミュニケーション、独占禁止法（antitrust）、プロジェクトポリシーの各文書。この WG 以外にオーナーがいるページや、CODEOWNERS で Core Maintainers の承認が必須とされる WG・IG 憲章ページについては、変更を提案するにとどめ、自ら反映はしない
- **意思決定の記録**: 何をプロジェクトの決定とみなすか、誰が承認するか、議事録・GitHub Discussions・SEP の記録にどう残すかを定める
- **行動規範（Code of Conduct）の管理**: 行動規範の文面と、それに付随する報告・エスカレーションの文書の起草・改訂・維持
- **コミュニティの価値観**: 進行中の価値観ワークショップの成果を、公開文書として `docs/community/` に収めることを含む
- **貢献の文化とメンタリング**: メンタリングを文化として奨励し（v0.1 では正式なペアリング制度は設けない）、[SEP-2148](https://modelcontextprotocol.io/seps/2148-contributor-ladder) と連携して contributor ladder の段階間の移行を支える
- **コミュニティの声を届ける窓口**: 貢献者や外部の観察者の懸念を、拘束力のない助言として Core Maintainers に届ける。懸念は `#governance-wg` か月例セッションで受け付け、Lead が月 1 回の「Core Maintainers と WG/IG Lead の会議」に持ち込む
- **横断的な調整**: 他の WG・IG に影響するガバナンスプロセスの調整。枠組みはこの WG が定め、各グループの運営は各グループに委ねる

**対象外（Out of Scope）** は、仕様の策定（プロトコル変更は SEP プロセスと担当の WG が扱う。ただしガバナンスプロセスを変える SEP のスポンサーにはなりうる）、メンテナーの選任と後継（Lead Maintainers が Core Maintainers を任命し、Core Maintainers が Maintainers を承認する。WG はプロセス改善の提案にとどめる）、個別の行動規範違反の受理・調査・裁定（WG は当面、対応主体から集計・匿名化された傾向報告を受け取ることを目指す）、SDK ごとのガバナンス（SDK WG の担当）、各 WG・IG の内部運営、行動規範の範囲外のメンテナー間の紛争や対人関係の調停（v0.1 では明示的に対象外。将来のエスカレーション経路の検討は成果物候補）の 6 点です。

**意思決定権限**は表形式で定められています。会議の日程調整、ロードマップ、WG 内の提案の優先順位付け、既存ガバナンス文書への編集上の修正（誤字・明確化・リンク修正。理由の記録が条件）は Lead が自律的に決められます。既存ガバナンス文書の実質的な改訂、`docs/community/` への新しいポリシーや文書の追加、行動規範の文面の改訂、この憲章の改訂は「WG の合意 → Core Maintainers の承認」が必要で、contributor ladder の構造変更にはさらにコミュニティのコメント期間が加わります。対象範囲の拡大には Core Maintainers の承認が必要です。この WG 以外がオーナーのページはオーナーに提案し、オーナーが決めます。「編集上の修正」と「実質的な改訂」の境界は意図的に狭く取られており、既存ルールの意味・範囲・適用対象を変えるものはすべて実質的な改訂とされます。

また、仕様リポジトリでのプルリクエスト作成はメンテナーに限られるため、メンテナーでない WG メンバーはフォークや WG 所有のリポジトリで文書の変更を起草し、WG 内のメンテナーが作成者名を明記してプルリクエストを出す運用です。

- [Governance Working Group Charter - MCP Docs](https://modelcontextprotocol.io/community/working-groups/governance#scope)

## 3. 作業項目と成功基準

**進行中の作業項目（Active Work Items）** は次の 6 件です。

| 項目 | 状態 | 期限 | 担当 |
|---|---|---|---|
| 意思決定記録の規約（何を決め、誰が承認し、どこに記録するか） | Planning | 2027年01月31日 | Sarah Novotny |
| コミュニティの価値観文書を `docs/community/` で公開 | In progress | 2027年02月28日 | Sarah Novotny |
| 行動規範の報告・対応経路の正式化 | Planning | 2027年03月31日 | TBD |
| オンボーディングとメンタリングの文化に関する文書 | Planning | 2027年04月30日 | TBD |
| 「State of MCP Community」の定期発信と初回の投稿 | Planning | 2027年05月31日 | TBD |
| 「コード以外の貢献方法（Ways to contribute beyond code）」ページ | Planning | 2027年05月31日 | TBD |

**成功基準（Success Criteria）** は Changelog に記録される憲章承認日を起点とし、2026 年 11 月の承認を想定しています。

- **6 か月（2027 年 Q2 まで）**: 意思決定記録の規約を採用し、記録された会議 3 回以上に適用する／価値観文書を `docs/community/` に収め、事前に草案へ実質的なコミュニティコメントを 3 件以上受ける／Discussions の「Meeting Notes - Governance WG」カテゴリを開設し、開催した月例セッションすべての議事録を投稿する／任期中「同一組織から Lead は 2 名まで」を維持する／Lead が月例の「Core Maintainers と WG/IG Lead の会議」に 4 回以上出席する
- **12 か月（2027 年 Q4 まで）**: 2 回目の「State of MCP Community」投稿を公開する／オンボーディングとメンタリングの取り組みが、WG の活動に言及した段階昇格を 3 件以上生む／意見が割れたガバナンス上の決定 1 件以上で、Core Maintainers への WG の助言が記録に残る／直近 6 か月に議題不足による中止が無い（または開催頻度の変更が記録されている）
- **ストレッチ目標（成功の必須条件ではないが追跡する）**: 正式化された行動規範の対応主体から、集計・匿名化された傾向報告を受け取り、ポリシー改訂に生かす

これらの基準は v0.1 として意図的に控えめに設定されており、グループの成熟に応じて見直し、改訂は Changelog に記録するとしています。

- [Governance Working Group Charter - MCP Docs](https://modelcontextprotocol.io/community/working-groups/governance#active-work-items)
- [Governance Working Group Charter - MCP Docs](https://modelcontextprotocol.io/community/working-groups/governance#success-criteria)

## 新規追加されたページ

<!-- light:new-pages:start -->
- [**Governance Working Group Charter**](#1-governance-working-group-charter) ([MCP Docs](https://modelcontextprotocol.io/community/working-groups/governance)):  
  MCP Governance Working Group の憲章。前回は索引への追加のみだったが、今回 `llms-full.txt` に本文が収録された（詳細はハイライト 1〜3 参照）。
<!-- light:new-pages:end -->

## 1. Governance Working Group Charter

`llms-full.txt` にとっては新規のページで、差分は 185 行の追加のみです。構成は Group Type・Mission Statement・Scope（In Scope / Out of Scope / Related Groups）・Leadership（Lead Selection & Succession）・Authority & Decision Rights・Membership・Operations・Deliverables & Success Metrics（Active Work Items / Success Criteria）・Charter Updates・Changelog の各節から成ります。索引 `llms.txt` のエントリは前回の対象期間に追加済みのため、今回の索引側の変更はありません。

内容の詳細は、ハイライト 1（ミッションと体制・運営）、ハイライト 2（対象範囲と意思決定権限）、ハイライト 3（作業項目と成功基準）を参照してください。

- [Governance Working Group Charter - MCP Docs](https://modelcontextprotocol.io/community/working-groups/governance)

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
今回の対象期間に大幅な更新（本文 50 行以上の変更）があった既存ページはありません。
<!-- light:updated-pages:end -->

## 軽微な更新

<!-- light:minor-updates:start -->
新規ページ以外では、`llms-full.txt` の既存 3 ページに計 3 か所の変更（追加 3 行・削除 2 行）がありました。索引 `llms.txt` に変更はありません。

**機能改善**

- Connect to local MCP servers の前提条件で、Claude Desktop の対応 OS を「macOS and Windows」から「macOS, Windows, and Linux」に修正 — [MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/develop/connect-local-servers#claude-desktop)
- Debugging の「Debugging in Claude Desktop」節で、Claude Desktop の対応 OS を同様に「macOS, Windows, and Linux」に修正 — [MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/tools/debugging#debugging-in-claude-desktop)

**その他**

- Financial Services Interest Group 憲章のメンバー表に、King Yew Choo（True Primary、@kychooo）を Participant として追加 — [MCP Docs](https://modelcontextprotocol.io/community/interest-groups/financial-services#membership)
<!-- light:minor-updates:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-10-10.md](./archives/latest/2026-10-10.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-10-10.md](./archives/latest-detail/2026-10-10.md)

<!--
base_commit: 096d54cbb316fc19ca321240fcef28dc6ea22401
head_commit: 98d1f105aec298de4131f50d6044a9d5ea41da93
generated_at_full: 2026-10-12T15:10:12+09:00
-->
