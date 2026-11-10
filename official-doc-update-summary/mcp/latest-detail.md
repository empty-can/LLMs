---
対象期間: 2026年11月07日 〜 2026年11月09日
作成日: 2026-11-09
---

# MCP 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
今回の対象期間の取り込みは 2 回で、MCP で差分が出たのは 2 回目だけでした。変わったのはほぼコミュニティ文書（`community/` 配下）で、8 ページで 50 行以上が書き換わり、2 ページが加わり、1 ページがなくなりました（`llms-full.txt` は追加 618 行・削除 1,647 行）。

主要なものを以下に挙げます。

1. コミュニティ文書の 13 ページが変わり、書き直したページは冒頭でそのページを定めた SEP を示す形にそろい、4 ページが改称された
2. Contributing to MCP が 568 行から 118 行になり、仕様リポジトリへの変更は、書き込み権限が無ければメンテナーに PR を開いてもらう手順に書き直された
3. 新しい Project Policies のページが行動規範・ライセンス・AI 支援の開示・脆弱性の報告などの方針をまとめ、Security Policy のページがなくなった
4. SEP Guidelines が書き直され、sponsor の定義に WG Lead が加わり、collaborator でない作者の進め方や `npm run generate:seps` などが書き込まれた
5. Working Groups and Interest Groups に現行のグループの一覧と会議の要件が加わり、Group Charter Template に憲章の提出手順ができ、MCP Apps Working Group の憲章が収録された
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**コミュニティ文書が大きく再編された**](#1-コミュニティ文書が大きく再編された):  
  差分のあった 14 ページのうち 13 ページがコミュニティ文書で、8 ページで 50 行以上が書き換わり、2 ページが加わり、1 ページがなくなった。書き直したページは冒頭でそのページを定めた SEP を示し、変更には Process SEP が要ると述べる形にそろい、4 ページが改称された。
2. [**Contributing to MCP が短くなり変更を出す手順が書き直された**](#2-contributing-to-mcp-が短くなり変更を出す手順が書き直された):  
  568 行から 118 行になり、環境構築やトラブルシューティングの説明がなくなった。仕様リポジトリに PR を開くには書き込み権限が要り、権限が無ければブランチを push してメンテナーに PR を開いてもらう。Inspector とリファレンスサーバーは issue だけを受け付ける。
3. [**Project Policies のページが加わり Security Policy のページがなくなった**](#3-project-policies-のページが加わり-security-policy-のページがなくなった):  
  行動規範・独占禁止・ライセンス・AI 支援の開示・脆弱性の報告・コミュニケーションの 6 つの方針をまとめたページが加わった。AI 支援はその程度とともに開示し、AI が書いたレビューへの返答やコメントも対象になる。Security Policy のページは索引と本文からなくなった。
4. [**SEP Guidelines の手順と sponsor の定義が詳しくなった**](#4-sep-guidelines-の手順と-sponsor-の定義が詳しくなった):  
  手順が 9 段階に組み直され、collaborator でない作者は sponsor に PR を開いてもらうこと、番号付け後の `npm run generate:seps`、`proposal` ラベル、差し戻しや `superseded` への遷移が書き込まれた。sponsor の定義に WG Lead が加わり、sponsor が付かないまま dormant になるまでの期間は 180 日と書かれた。
5. [**グループの運営ルールと憲章の手順が整理された**](#5-グループの運営ルールと憲章の手順が整理された):  
  Working Groups and Interest Groups に現行の working group 14 件と interest group 8 件の一覧が加わり、会議はアジェンダから Project Policies にリンクすることになった。Group Charter Template に憲章の提出手順の節ができ、MCP Apps Working Group の憲章ページが収録された。
<!-- light:highlight-list:end -->

## 1. コミュニティ文書が大きく再編された

今回の対象期間の取り込みは 2 回で、MCP の入力ファイルに差分が出たのは 2 回目だけです。索引 `llms.txt`（追加 12 行・削除 11 行）と本文 `llms-full.txt`（追加 618 行・削除 1,647 行）の両方が変わりました。`llms-full.txt` の総行数は 46,038 行から 45,009 行に、収録ページ数は 159 件から 160 件（`examples` が 2 回収録されているため、URL としては 158 件から 159 件）に、索引のエントリ数は 364 件から 365 件になっています。差分のあったページは 14 件で、The MCP Registry（画像の URL だけ）を除く 13 件がコミュニティ文書（`community/` 配下）です。

| ページ | 行数 | 追加 | 削除 | 扱い |
|---|---|---|---|---|
| Contributing to MCP | 568 → 118 | 57 | 507 | 大幅更新（ハイライト 2） |
| Contributor Ladder | 381 → 162 | 86 | 305 | 大幅更新 |
| Working Groups and Interest Groups（旧 Working and Interest Groups） | 294 → 152 | 97 | 239 | 大幅更新（ハイライト 5） |
| SEP Guidelines | 279 → 138 | 83 | 224 | 大幅更新（ハイライト 4） |
| Feature Lifecycle and Deprecation（旧 Feature Lifecycle and Deprecation Policy） | 156 → 146 | 61 | 71 | 大幅更新 |
| Communication（旧 Contributor Communication） | 112 → 34 | 18 | 96 | 大幅更新 |
| SDK Tiers（旧 SDK Tiering System） | 146 → 109 | 34 | 71 | 大幅更新 |
| Group Charter Template | 157 → 122 | 34 | 69 | 大幅更新（ハイライト 5） |
| MCP Apps Working Group Charter | 新規 126 | 126 | 0 | 新規追加（ハイライト 5） |
| Project Policies | 新規 38 | 38 | 0 | 新規追加（ハイライト 3） |
| Security Policy | 69 → 削除 | 0 | 69 | ページの削除（ハイライト 3） |
| Design Principles | 50 → 44 | 7 | 13 | 軽微な更新 |
| Antitrust Policy | 64 → 58 | 1 | 7 | 軽微な更新 |
| The MCP Registry | 93 → 93 | 1 | 1 | 軽微な更新 |

行数は、ページのタイトルの行（`# `）から次のページの直前までを数えたものです。追加・削除の行数は、ページごとに新旧の本文を突き合わせて数えました。ページの境目をまたいだ行の対応づけが起きない数え方のため、14 ページの合計（追加 643 行・削除 1,672 行）は、ファイル全体の差分より追加・削除とも 25 行多くなります。

**書き直したページの冒頭がそろいました。** 書き直されたページの多くは、冒頭でそのページを定めた SEP を挙げ、変更には Process SEP が要ると述べる形になりました。Contributor Ladder は SEP-2148、Working Groups and Interest Groups と Group Charter Template は SEP-2149、Communication は SEP-994、Feature Lifecycle and Deprecation は SEP-2596、SDK Tiers は SEP-1730 です。SEP Guidelines は、手続きを定めた SEP-1850 と、Conformance の要件を加えた SEP-2484 を挙げています。

**改称と索引の並びが変わりました。** 4 ページが改称されました（Contributor Communication → Communication、Feature Lifecycle and Deprecation Policy → Feature Lifecycle and Deprecation、SDK Tiering System → SDK Tiers、Working and Interest Groups → Working Groups and Interest Groups）。索引 `llms.txt` ではコミュニティ文書の並びが変わり、Project Policies・Communication・Feature Lifecycle and Deprecation・SDK Tiers・Antitrust Policy が末尾にまとまりました。説明文は 7 ページで書き換わっています。

**一般的な案内の節が削られました。** 各ページから、Troubleshooting（Contributing to MCP）、Guiding Principles・Contribution Pathways・Recognition and Visibility（Contributor Ladder）、When to Use Which・FAQ（Working Groups and Interest Groups）、Copyright（SEP Guidelines）などの節がなくなりました。各ページは、規則そのものと、関連するページの節へのリンクを中心とした構成になっています。

- [Contributing to MCP - MCP Docs](https://modelcontextprotocol.io/community/contributing#where-to-start)

## 2. Contributing to MCP が短くなり変更を出す手順が書き直された

Contributing to MCP は 568 行から 118 行に短くなり、見出し（h2・h3。コードフェンスの外で数えた値）は 32 個から 8 個になりました。これまでのページは、次の内容を載せていました。

- Node.js 24 以上などの前提と、リポジトリの一覧表
- フォーク・クローン・`npm install`・`npm run check` から PR を出すまでの手順
- スキーマとドキュメントを変更する手順
- SDK リポジトリのカード
- Troubleshooting

新しいページは Where to start・Report a problem・Change the specification or docs・Work on an SDK or tool・Propose a protocol change・Other ways to help・Growing your role・Ground rules の 8 節で、セットアップとチェックの詳細はリポジトリの CONTRIBUTING.md に任せています。

**仕様リポジトリへの変更の出し方が書き直されました。** これまでは仕様リポジトリをフォークし、ブランチを作って自分で PR を開く手順でした。新しいページは、仕様リポジトリに PR を開くには書き込み権限が要るとし、issue から始めることを勧めています。手順は次の 3 段階です。

1. バグなら issue で、それ以外はグループのチャンネルか `#general` で変更を持ち出す
2. フォーク（または書き込める working group のリポジトリ）にブランチを push する。仕様の修正は `draft/` に入れ、1 つの変更は 1 つの関心事に絞る
3. その issue かチャンネルでブランチを示し、メンテナーに、自分をクレジットした PR を開いてもらう

なお SEP Guidelines には、このリポジトリが collaborator からの PR しか受け付けないという記述が以前からありました。

**SDK・ツール・提案・報告の窓口も書かれています。**

- Inspector とリファレンスサーバーは issue だけを受け付ける
- SDK などのリポジトリはそれぞれ独自の規則を持ち、割り当てられた issue の無い PR を閉じるところもある
- 小さなバグ修正より大きな変更は、コードを書く前に issue で進め方を合わせる
- プロトコルの変更は SEP で行い、アイデアの議論・プロトタイプ・sponsor 探し・SEP を書く、の 4 段階を SEP Guidelines の該当節へ案内する。書き込み権限が無ければ、sponsor に PR を開いてもらう
- 使い方の質問はスパムのため、リポジトリでは受け付けなくなった

Other ways to help は、SEP と仕様の draft の PR のレビュー、報告されたバグの再現、SDK のリリース候補を draft の仕様で試すこと、適合性テストのシナリオを書くことを挙げています。

**Ground rules** は次の 4 点です。行動規範・AI の開示・ライセンスの各項目は、Project Policies の該当する節へリンクしています（ハイライト 3）。

- 行動規範は、すべてのリポジトリ・チャンネル・会議に適用される
- AI の支援を受けたら、PR か issue で開示する
- AI エージェントは AGENTS.md に従わなければならない。AGENTS.md は、エージェントが issue や PR を開ける場合を制限している
- 貢献は、コードと仕様が Apache-2.0、それ以外のドキュメントが CC-BY-4.0 でライセンスされる

これまでの AI Contributions の節は、AI の使い方を PR か issue で「一言知らせてくれればよい」という書き方でした。

- [Contributing to MCP - MCP Docs](https://modelcontextprotocol.io/community/contributing#change-the-specification-or-docs)
- [Contributing to MCP - MCP Docs](https://modelcontextprotocol.io/community/contributing#work-on-an-sdk-or-tool)

## 3. Project Policies のページが加わり Security Policy のページがなくなった

新しいページ Project Policies（38 行）は、MCP の会議・Discord・`modelcontextprotocol` 組織のすべてのリポジトリで、参加者全員に適用される方針を 6 つの節で示しています。グループの Lead と Facilitator は、会議のアジェンダからこのページにリンクします。

- **Code of Conduct**: 行動規範はすべてのチャンネル・リポジトリ・会議に適用される。報告は専用のアドレスへ送る。Community Moderators が Contributor Ladder に従って扱い、必要なら Core Maintainers へエスカレーションする
- **Antitrust**: MCP は Model Context Protocol a Series of LF Projects, LLC として組織されている。そのため、LF Projects の方針（独占禁止の方針を含む）が全参加者に適用される。会議と標準化の議論の進め方は、プロジェクト自身の Antitrust Policy が定める
- **Licensing and intellectual property**: コードと仕様は Apache License 2.0、その他のドキュメントは CC-BY-4.0 で、著作権の譲渡は無い。正式な文面は Governance の General Project Policies にある
- **AI-assisted contributions**: 貢献に使った AI の支援は、その程度とともに PR か issue で開示しなければならない。AI が書いたレビューへの返答やコメントも対象で、例外は些細な空白や誤字の修正だけ。全文は AI_POLICY.md で、組織のすべてのリポジトリに適用される
- **Reporting a vulnerability**: 公開の issue・discussion・PR で報告しないよう WARNING で求めている。報告は、影響を受けるリポジトリで `github.com/modelcontextprotocol/<repo>/security/advisories/new` から非公開のアドバイザリを開いて行う。報告の前に SECURITY.md を読むよう求めており、SECURITY.md は次の 3 点を説明している
  - 報告に含めるもの
  - 信頼モデルと、脆弱性ではなく意図された挙動（stdio のコマンド実行、stdio の相手によるサービス拒否、サーバーの副作用、LLM によるツールの呼び出し）
  - 対象範囲

  報告を受けたメンテナーは、影響を受けるすべての SDK にまたがって修正とアドバイザリを調整し、同時に公開する。根本原因が仕様にあれば、仕様のメンテナーと協議する。CVE は GitHub の CNA で採番する。どのリポジトリに出すかなど、報告そのものではない質問は、Security Interest Group の `#security-ig` で扱う
- **Communication and records**: どのチャンネルを何に使うか、いつ非公開にできるか、決定をどこに記録するかは Communication のページに書かれている

**Security Policy（`community/security`、69 行）は、索引と本文の両方からなくなりました。** 報告の手順と SDK 間の調整は、Project Policies の Reporting a vulnerability の節に同じ趣旨の記述があります。ただし旧ページの次の 2 節の本文は引き継がれず、SECURITY.md へのリンクに替わりました。

- Scope: 脆弱性とみなすものの一覧
- Stdio transport trust boundary: stdio の相手を落とす・止めるだけの報告は対象外で、通常の issue として出す、など

また、本文に残る SEP-3398 のページは、旧ページの URL へのリンクを残しています。

脆弱性の窓口への案内は、ほかのページでも Project Policies の節に替わりました。Contributing to MCP の Report a problem、Communication のチャンネルの表、Contributor Ladder の Escalation の注記が、いずれも Project Policies の Reporting a vulnerability にリンクしています。

- [Project Policies - MCP Docs](https://modelcontextprotocol.io/community/policies#reporting-a-vulnerability)
- [Project Policies - MCP Docs](https://modelcontextprotocol.io/community/policies#ai-assisted-contributions)

## 4. SEP Guidelines の手順と sponsor の定義が詳しくなった

SEP Guidelines は 279 行から 138 行になり、見出しは 24 個から 10 個に減りました。SEP Format の 8 つの h3 は Template and tooling の 1 段落にまとまり、Copyright の節はなくなっています。手順は 10 段階から 9 段階に組み直され、次の点が新たに書かれました。

- **When you need a SEP**: 対象に「コア仕様の外でサポートされる相互運用の慣行」が独立した項目として加わった。テストは通常の PR で出せる、と明記された。ガバナンス文書そのものの改訂は、この手続きではなく SEP-2085 の手順に従う
- **Before you write**: まず、その領域を担当する working group か interest group にアイデアを持ち込む。事前の議論が必須で PR の説明にリンクする点と、ロードマップや設計原則との整合を確かめる点は以前と同じ。新たに、形が許せばまず拡張として試すこと、プロトタイプを作ってから SEP を書くことが書かれた
- **Workflow（手順）**: 次のように進む
  1. `seps/TEMPLATE.md` を `seps/0000-<slug>.md` にコピーして書く
  2. PR を開く。リポジトリは collaborator からの PR しか受け付けないので、collaborator でなければ先に sponsor を見つけ、PR を開いて自分を作者として記してもらう
  3. PR 番号が SEP 番号になる。ファイル名を変えたら `npm run generate:seps` を実行する（しないと CI の `check:seps` が失敗する）
  4. PR に付く `proposal` ラベルは sponsor 待ちを表す PR ラベルで、SEP の `Status` ヘッダーは空のまま
  5. sponsor が付くと `draft` になる
  6. 準備ができたら、sponsor が事前の議論のリンクを確かめて `in-review` にし、Core Maintainer の会議の議題に載せる
  7. Core Maintainers が決定し、sponsor が結果を記録する
  8. 採択されたら、作者が同じ PR に仕様の本文、`schema.ts` の変更と再生成物、changelog、必要なドキュメントの修正（非推奨化なら Feature Lifecycle and Deprecation の 4 つの修正）を加える
  9. sponsor が確かめて `final` にし、PR がマージされる
- **Workflow（フロー図と表）**: フロー図に次の遷移が加わった
  - dormant から draft（sponsor が見つかり PR を再開）
  - draft から withdrawn
  - Core Maintainers の決定から draft（フィードバック付きの差し戻し）
  - final から superseded

  sponsor 待ちの期間の表記は「最大 6 か月」から「180 日」になった。8 つの状態の表には、誰が設定するかを示す Set by の列が加わった
- **Sponsors**: sponsor の定義が「Core Maintainer か Maintainer」から、その working group の範囲の SEP については WG Lead も含む形に広がった（Contributor Ladder には以前から、WG Lead が SEP の sponsor になれるという記述があった）。PR を開ける人は、PR とプロトタイプをチャンネルに投稿して Maintainer を最大 2 人タグ付けする。開けない人は、SEP の草稿とプロトタイプを投稿し、Maintainer に sponsor と PR の作成を頼む
- **Review and acceptance**: 採択の基準に、ロードマップと設計原則に合っていることが加わった。結果は `accepted`・`rejected`、または PR に記録した具体的なフィードバック付きの `draft` への差し戻しになる
- **After the decision**: Final の SEP が採択時の設計の記録で、仕様と食い違ったら仕様が優先する点は以前と同じ。新たに、問題は SEP の編集ではなく仕様への issue として報告すること、ほかの SEP を置き換える SEP はヘッダーに `Supersedes:` の行を持つことが書かれた
- **Template and tooling**: SEP の構成の参照先が `seps/README.md` から `seps/TEMPLATE.md` になった。`npm run generate:seps` と `npm run check:seps` の役割を説明し、最近 Final になった Standards Track の SEP として SEP-2567 を実例に挙げる

- [SEP Guidelines - MCP Docs](https://modelcontextprotocol.io/community/sep-guidelines#workflow)
- [SEP Guidelines - MCP Docs](https://modelcontextprotocol.io/community/sep-guidelines#sponsors)

## 5. グループの運営ルールと憲章の手順が整理された

Working and Interest Groups は Working Groups and Interest Groups に改称され、294 行から 152 行に、見出しは 22 個から 13 個になりました。冒頭には、SEP の PR を開く前に、関係する working group との事前の議論と、その承認が要ると書かれています（SEP Guidelines 側は、事前の議論とそのリンクを求めるだけで、承認には触れていません）。加わった主な内容は次のとおりです。

- **Current groups**: 現行の working group 14 件（MCP Apps を含む）と interest group 8 件の一覧。これまでのページにはグループの一覧が無く、FAQ で Discord と `docs/community/` を案内していた
- **Joining a group**: グループの Discord のチャンネルに入り、会議に出て、アジェンダとノートのスレッドを追う。Participant として載るには Lead に頼む。メンバーの一覧は access リポジトリにあり、GitHub のチームと Discord のロールに反映される
- **Leadership**: WG Lead の務めに、グループのロードマップ（憲章の Active Work Items）を最新に保ってプロジェクトのロードマップに反映することが書かれた
- **Making decisions**: どの決定をどのレベルで行うかは、各 working group の憲章の Authority and Decision Rights の表が記録する。この表は憲章とともに承認される
- **Meetings and channels**: すべての会議の要件に、次の 2 つが加わった
  - 行動規範と Antitrust Policy のもとで行うこと。Antitrust Policy の Conduct of Meetings の節は、アジェンダと議事録を求めている
  - アジェンダから Project Policies にリンクすること

  アジェンダを会議の前に GitHub Discussion（Meeting Notes カテゴリ）に投稿し、ノートを 48 時間以内に同じ discussion へ載せる要件は以前と同じ
- **Forming a group / Amending or retiring a group**: working group を作るには、トピックに近い Discord のチャンネルか `#wg-ig-group-creation` で sponsor を探し、sponsor を得てから憲章を提出する。憲章の変更は Lead・Facilitator・Core Maintainer が提案し、Core Maintainers が承認して、憲章の Changelog に記録する

**Group Charter Template には Submitting a charter の節が加わり、提出の手順が箇条書きになりました。**

- グループが Forming a group のとおり sponsor を得ていること
- テンプレートをコピーしてプレースホルダーを置き換えること。`{/* */}` のガイドのコメントは、消すか書かれたままにする。HTML のコメントは MDX のビルドを壊し、`npm run format` は複数行にわたる `{/* */}` のコメントを壊すため
- `npm run prep` を実行してから push すること
- 憲章のファイル、`docs/docs.json` のナビゲーションの項目、Current groups の 1 行を加える PR を開くこと
- 後の変更は、憲章の Changelog に行を加えること

**MCP Apps Working Group の憲章ページが、索引と本文に加わりました。** 対話的なユーザーインターフェースのための公式の拡張（MCP Apps）を定義・発展・保守する working group の憲章です。憲章の Changelog では最初の憲章が 2026年05月21日付なので、新しいグループの発足ではなく、憲章ページが今回収録されたものです（詳細は新規追加ページ 2 参照）。これにより、索引の working group の憲章は 13 件から 14 件になりました。

- [Working Groups and Interest Groups - MCP Docs](https://modelcontextprotocol.io/community/working-interest-groups#current-groups)
- [Working Groups and Interest Groups - MCP Docs](https://modelcontextprotocol.io/community/working-interest-groups#meetings-and-channels)
- [Group Charter Template - MCP Docs](https://modelcontextprotocol.io/community/charter-template#submitting-a-charter)

## 新規追加されたページ

<!-- light:new-pages:start -->
- [**Project Policies**](#1-project-policies) ([MCP Docs](https://modelcontextprotocol.io/community/policies#reporting-a-vulnerability)):  
  MCP の参加者全員に適用される方針（行動規範・独占禁止・ライセンス・AI 支援の開示・脆弱性の報告・コミュニケーション）を 1 ページにまとめ、それぞれの正本へ案内するページ（詳細はハイライト 3 参照）。
- [**MCP Apps Working Group Charter**](#2-mcp-apps-working-group-charter) ([MCP Docs](https://modelcontextprotocol.io/community/working-groups/apps#mission-statement)):  
  MCP Apps の拡張を担う working group の憲章。範囲、Lead 3 人と WG Member 3 人、決定権限、会議、7 件の作業項目、2025年11月21日からの経緯を記している。
<!-- light:new-pages:end -->

## 1. Project Policies

ハイライト 3 で取り上げたページです（38 行、h2 が 6 個）。索引での説明は「MCP プロジェクトに参加するすべての人に適用される常設の方針と、それぞれが定められている場所」です。各節は短い要約にとどめ、正本（GitHub の CODE_OF_CONDUCT.md・AI_POLICY.md・SECURITY.md、LF Projects の方針、Governance の General Project Policies、Antitrust Policy、Communication）へリンクしています。Working Groups and Interest Groups の Meetings and channels は、すべての会議のアジェンダからこのページにリンクするよう求めています。

- [Project Policies - MCP Docs](https://modelcontextprotocol.io/community/policies#code-of-conduct)

## 2. MCP Apps Working Group Charter

MCP Apps Working Group の憲章（126 行）です。Mission Statement は、この working group が対話的なユーザーインターフェースのための公式の拡張を定義・発展・保守すると述べています。あわせて、拡張の仕様・SDK・リファレンス実装・セキュリティモデル・適合性の作業・ガイダンスを監督し、アプリが独立した複数の MCP ホストで安全かつ一貫して動くようにする、としています。

- **範囲（In Scope）**: 次の 9 項目
  - `io.modelcontextprotocol/ui` の名前空間の拡張仕様と関連する SEP
  - アプリのライフサイクル
  - ユーザー・アプリ・ホストの間のやり取り
  - コンテンツの種類と描画先（生成 UI、A2UI や AG-UI との相互運用）
  - セキュリティモデル（脅威モデル、サンドボックス、権限、UI から起きた操作の監査）
  - `@modelcontextprotocol/ext-apps` の SDK とリファレンスホスト
  - 適合性
  - ほかのグループとの調整（Registry WG・Agents IG・SDK WG）
  - ドキュメント
- **範囲外（Out of Scope）**: 次の 4 つ
  - コアプロトコルの変更（SEP の手続きで、担当のグループか Core Maintainers が扱う）
  - ホストごとの製品とデザインの判断
  - 個々のアプリの実装
  - エージェントのオーケストレーション全般（Agents IG と Tasks and Events WG が扱う）
- **体制**: Lead は 3 人（所属は MCP-UI、MCP-UI / Ora、Anthropic）。WG Member は Anthropic・OpenAI・Google から 1 人ずつ
- **会議**: Working Session を Tri-weekly（水曜 8 時、太平洋時間、60 分）で開く。Discord のチャンネルは `#mcp-apps-wg`
- **決定権限**: Authority & Decision Rights の表は、仕様の追加的な変更を「WG の合意 → Core Maintainer の承認」、破壊的・根本的な変更を「それに加えて広いレビュー」としている
- **作業項目**: 7 件。次のものなどがある
  - 仕様と SDK の発展
  - ツールやサーバーにまたがるビューの乱立への対処
  - セキュリティモデルの形式化
  - アプリのツールのやり取りの実験（WebMCP の方式）
  - 動的なリソースの内容と HTML 以外のホストへの対応（Draft）
  - 適合性とホスト間の相互運用
  - 開発者体験と普及

  成功の基準には「MCP Apps が主要な複数のホストで変更なしに動く」などを挙げる
- **経緯（Changelog）**: 次のとおり
  - 2025年11月21日: MCP-UI と OpenAI Apps SDK の方式を統合する SEP-1865 の提案
  - 2025年12月17日: 最初の会議
  - 2026年01月26日: 最初の安定版の拡張仕様の公開
  - 2026年01月28日: SEP-1865 が Final
  - 2026年05月21日: 最初の憲章

- [MCP Apps Working Group Charter - MCP Docs](https://modelcontextprotocol.io/community/working-groups/apps#mission-statement)
- [MCP Apps Working Group Charter - MCP Docs](https://modelcontextprotocol.io/community/working-groups/apps#active-work-items)

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
- [**Contributing to MCP**](#1-contributing-to-mcp) ([MCP Docs](https://modelcontextprotocol.io/community/contributing#change-the-specification-or-docs)):  
  568 行から 118 行になり、8 つの節で入口を案内する形になった。仕様リポジトリへの変更は、書き込み権限が無ければメンテナーに PR を開いてもらう手順に書き直された（追加 57 行・削除 507 行。詳細はハイライト 2 参照）。
- [**Contributor Ladder**](#2-contributor-ladder) ([MCP Docs](https://modelcontextprotocol.io/community/contributor-ladder#advancement-process)):  
  381 行から 162 行になった。各役割を要件・sponsor と承認・務め・権限・最低期間の段落で書く形にそろえ、昇格の手順を 5 段階に、非活動・辞任・解任を 1 つの節にまとめた（追加 86 行・削除 305 行）。
- [**Working Groups and Interest Groups**](#3-working-groups-and-interest-groups) ([MCP Docs](https://modelcontextprotocol.io/community/working-interest-groups#current-groups)):  
  旧 Working and Interest Groups。294 行から 152 行になった。現行のグループの一覧と参加の方法が加わり、運営ルールを Leadership から Amending or retiring a group までの節に組み直した（追加 97 行・削除 239 行。詳細はハイライト 5 参照）。
- [**SEP Guidelines**](#4-sep-guidelines) ([MCP Docs](https://modelcontextprotocol.io/community/sep-guidelines#workflow)):  
  279 行から 138 行になった。手順を 9 段階に組み直し、collaborator でない作者の進め方、`proposal` ラベル、`npm run generate:seps`、sponsor への WG Lead の追加などを書き込んだ（追加 83 行・削除 224 行。詳細はハイライト 4 参照）。
- [**Feature Lifecycle and Deprecation**](#5-feature-lifecycle-and-deprecation) ([MCP Docs](https://modelcontextprotocol.io/community/feature-lifecycle#deprecating-a-feature)):  
  旧 Feature Lifecycle and Deprecation Policy。非推奨化の SEP が採択されたら作者が SEP の PR で 4 つの修正を加え、sponsor が確かめてから `final` にする流れを明記し、Roles の表を 1 段落にした（追加 61 行・削除 71 行）。
- [**Communication**](#6-communication) ([MCP Docs](https://modelcontextprotocol.io/community/communication#decision-records)):  
  旧 Contributor Communication。112 行から 34 行になった。チャンネルの表・Discord・決定の記録の 3 節にまとめ、チャンネルの命名規則と、Discord は記録の場ではないことを明記した（追加 18 行・削除 96 行）。
- [**SDK Tiers**](#7-sdk-tiers) ([MCP Docs](https://modelcontextprotocol.io/community/sdk-tiers#conformance-testing)):  
  旧 SDK Tiering System。日程の NOTE と Overview の節を削った。各公式 SDK が既定のブランチで適合性テストを実行して結果を公開すること、非推奨を示さない Tier 1 の SDK の降格を書き加えた（追加 34 行・削除 71 行）。
- [**Group Charter Template**](#8-group-charter-template) ([MCP Docs](https://modelcontextprotocol.io/community/charter-template#submitting-a-charter)):  
  Submitting a charter の節を新設して提出手順を箇条書きにし、テンプレートのガイドのコメントを MDX の `{/* */}` 形式に替えた（追加 34 行・削除 69 行。詳細はハイライト 5 参照）。
<!-- light:updated-pages:end -->

## 1. Contributing to MCP

変更の中心はハイライト 2 のとおりです。これまでの節は、次のように整理されました。

| これまでの節 | 今回 |
|---|---|
| Before You Begin（Join the Community・Prerequisites・Repository Structure・Project Roles） | 冒頭と Where to start に短くまとめた。前提のツールとリポジトリの表、役割の説明はなくなった |
| Your First Contribution（Step 1〜4・What Makes a Good Contribution） | Change the specification or docs の 3 段階に替わり、フォークから自分で PR を開く手順はなくなった。「メンテナーは通常 1〜5 営業日で応答する」という記述もなくなった |
| Types of Contributions・Working with the Specification Repository | Change the specification or docs と Propose a protocol change に替わった。スキーマとドキュメントの変更手順は CONTRIBUTING.md に任せている |
| Working with the SDK Repositories | Work on an SDK or tool に替わった。SDK のカードはなくなった |
| Getting Help | Report a problem に替わった。Discussions と Issues の使い分けは Communication のページに書かれている |
| Troubleshooting・Out of Scope | なくなった。サーバーやクライアントを作る人への案内は冒頭の 1 文に残った |
| AI Contributions・Code of Conduct・License | Ground rules にまとまり、Project Policies へリンクする |
| （なし） | Other ways to help と Growing your role を新設 |

- [Contributing to MCP - MCP Docs](https://modelcontextprotocol.io/community/contributing#where-to-start)

## 2. Contributor Ladder

381 行から 162 行になり、見出しは 19 個から 16 個になりました。各役割の説明は、要件・sponsor と承認・務め・権限・最低期間を太字の見出し付きの段落で書く形にそろいました。内容が変わった主な点は次のとおりです。

- **Roles at a glance**: 表の列が「概要・主な権限・最低期間」から「何か・付与されるアクセス・最低期間」になった。Core Maintainer には「全リポジトリの管理権限」、Lead Maintainer には「全リポジトリとインフラの管理権限」と書かれた。表の下には、コード・仕様の本文・ドキュメント・トリアージ・セキュリティの作業・コミュニティの作業・モデレーションが、どの役割に対しても等しく数えられる、という一文が加わった
- **Member**: 権限から「制限のあるリポジトリで PR を作れる」がなくなり、仕様リポジトリでの PR の作成は Contributing to MCP に従う、となった。名簿は access リポジトリのメンバーのリストで、別の一覧は公開しない（これまでは community membership roster に載る、という書き方だった）
- **Maintainer**: sponsor できる対象が「新しい Maintainer」から「Member・Maintainer・SEP」になった
- **Core Maintainer**: 解任は Lead Maintainers が行う、と Core Maintainer の節にも書かれた（これまでは Lead Maintainer の務めとしてだけ書かれていた）。務めとして、2 週ごとの Core Maintainer の会議と Steering Group の会合に出ることが書かれた
- **WG Lead と IG Facilitator**: 要件と務めの詳細（SEP の sponsor とトリアージを含む）は Working Groups and Interest Groups へ移った
- **Advancement process**: 5 段階になった
  1. 仕様リポジトリで、推薦のテンプレートを使って issue を開く
  2. sponsor がそのスレッドで支持を表明する
  3. 7 日間のコメント期間を設ける
  4. 承認者が決定し、スレッドに記録する
  5. access リポジトリでアクセスを付与し、オンボーディングを行う

  表には Sponsors の列が加わった。Member の承認は「7 日以内に既存の Member から異議が無いこと」、Community Moderator の承認は「sponsor した Core または Lead Maintainer」と書かれた
- **Escalation**: 表の 8 行の内容は同じ。脆弱性はまず非公開のアドバイザリで報告し、表のセキュリティの行は報告の後のメンテナー内のエスカレーションだ、という注記が加わった。グループ内の紛争の参照先は、SEP-2149 の §1.5 から Working Groups and Interest Groups の Escalation の節に替わった
- **Inactivity, stepping down and removal**: 各役割に分かれていた非活動の規定と、辞任・emeritus・解任を 1 つの節にまとめた
- **削除された節**: Guiding Principles、Contribution Pathways、Recognition and Visibility

- [Contributor Ladder - MCP Docs](https://modelcontextprotocol.io/community/contributor-ladder#advancement-process)
- [Contributor Ladder - MCP Docs](https://modelcontextprotocol.io/community/contributor-ladder#escalation)

## 3. Working Groups and Interest Groups

内容の変化はハイライト 5 のとおりです。節の対応は次のとおりです。

| これまでの節 | 今回 |
|---|---|
| Quick Reference | Working groups and interest groups の表。例は、Transports WG と Security IG の憲章へのリンクになった |
| When to Use Which・Interest Groups (IGs)・Working Groups (WGs) | なくなった。「interest group が問題を整理し、新しい working group か既存のグループか直接の SEP が解く」という 1 文が残った |
| （なし） | Current groups と Joining a group を新設 |
| Governance 配下の Leadership・Participation Levels・Decision-Making Process・Escalation Path | h2 の Leadership・Participation levels・Making decisions・Escalation になった。Escalation は、一般的な手順と応答期限を Contributor Ladder に任せている |
| Meeting Requirements・Communication Channels | Meetings and channels にまとまった。チャンネルの表はなくなり、命名の規則は Communication のページに移った |
| Reporting | 内容は同じ |
| Lifecycle・Charter Amendments | Forming a group と Amending or retiring a group になった。憲章の提出の手順は Group Charter Template に移った |
| Charters・FAQ | なくなった |

なお、今回変わっていない Governance Working Group の憲章は、なくなった節のアンカー `#charter-amendments` へのリンクを残しています。

- [Working Groups and Interest Groups - MCP Docs](https://modelcontextprotocol.io/community/working-interest-groups#forming-a-group)
- [Working Groups and Interest Groups - MCP Docs](https://modelcontextprotocol.io/community/working-interest-groups#amending-or-retiring-a-group)

## 4. SEP Guidelines

内容の変化はハイライト 4 のとおりです。節の対応は次のとおりです。

| これまでの節 | 今回 |
|---|---|
| What is a SEP? | 冒頭の段落にまとまった。SEP-1850 と SEP-2484 への言及が加わった |
| When to Write a SEP | When you need a SEP |
| SEP Types | 4 種類は同じ |
| SEP Workflow（Step-by-Step Process・SEP Statuses） | Before you write と Workflow に分かれた |
| SEP Format（8 つの h3） | Template and tooling の 1 段落にまとまった |
| Prototype Requirements | 箇条書きを 1 段落にまとめた（内容は同じ） |
| The Sponsor Role・Status Management | Sponsors にまとまった |
| SEP Review & Resolution | Review and acceptance |
| Conformance Test Requirement | 要件は同じで、箇条書きを文章に替えた。SEP-2484 へのリンク先が `/seps/2484-conformance-tests-required-for-final-seps` から `/seps/2484` になった |
| After Rejection・Reporting SEP Bugs or Updates・Transferring SEP Ownership | After the decision にまとまった |
| Copyright | なくなった |

- [SEP Guidelines - MCP Docs](https://modelcontextprotocol.io/community/sep-guidelines#before-you-write)
- [SEP Guidelines - MCP Docs](https://modelcontextprotocol.io/community/sep-guidelines#review-and-acceptance)

## 5. Feature Lifecycle and Deprecation

タイトルから「Policy」が外れました。見出しは 9 個のまま変わらず、12 か月以上の最低の非推奨期間と、セキュリティ上のリスクがある場合に 90 日まで縮められる規定も変わっていません。差分の多くは文の折り返しと言い回しの整理で、内容に関わる変更は次のとおりです。

- **冒頭**: SEP-2596 へのリンクが、GitHub の PR から `/seps/2596` に替わった。現在 Deprecated か削除予定の機能は Deprecated registry に載っている、と案内している
- **Deprecating a Feature**: 非推奨化に伴う 4 つの変更を書き直した。4 つの変更は、`schema.ts` の `@deprecated`、仕様の本文の告知、`changelog.mdx` の "Deprecated" 見出し、deprecated registry への記載
  - これまで: 「SEP が採択されて Final になると非推奨化が予定される」として、4 つの変更を受け身で書いていた
  - 今回: 採択されたら作者が SEP の PR で draft の仕様にこれらを加え、sponsor が確かめてから `final` にする、と書いた

  最低の非推奨期間を、SEP が Final になった日ではなく、その改訂が Current としてリリースされた時点から数える点は同じ。非推奨化の SEP の実例として SEP-2577 を挙げている
- **Removing a Feature**: 番号付きの 3 項目を 1 段落にした。期間が過ぎた後、Core Maintainers がリリースの準備のときに削除できる。削除は `changelog.mdx` の "Removed" 見出しと registry に記録する。また機能は無期限に Deprecated のままでもよい、と書いた（これまでは「最低期間よりずっと長く Deprecated のままでもよい」）
- **Roles**: 6 行の表を 1 段落にした。Lead Maintainer の拒否権は同じ

- [Feature Lifecycle and Deprecation - MCP Docs](https://modelcontextprotocol.io/community/feature-lifecycle#deprecating-a-feature)
- [Feature Lifecycle and Deprecation - MCP Docs](https://modelcontextprotocol.io/community/feature-lifecycle#removing-a-feature)

## 6. Communication

Contributor Communication から改称され、112 行から 34 行に、見出しは 8 個から 3 個（Channels・Discord・Decision records）になりました。

- **冒頭**: SEP-994 で採択され、変更には Process SEP が要る、と述べる
- **Channels**: 表の 5 行は Discord・会議のカレンダー（旧 Live calls）・GitHub Discussions・GitHub Issues・Security advisories になった
  - GitHub Discussions: アイデア、根拠付きの機能要望、質問、ロードマップ、告知とリリース、会議のアジェンダとノート（Meeting Notes カテゴリ）
  - GitHub Issues: issue フォームで出す再現可能なバグ、範囲の決まったドキュメントの作業、CI とリリースの作業
  - Security advisories: 脆弱性の報告。Project Policies の節へリンクする

  各 SDK とプロジェクトのリポジトリはそれぞれ issue トラッカーと Discord のチャンネルを持ち、多くは Discussions を無効にして Issues を使う（例外は仕様のリポジトリとレジストリ）、と書かれた
- **Discord**: サポートの場ではなく、再現できるバグは影響するリポジトリの issue に、使い方の質問はドキュメントから、と案内している。チャンネル名の規則として、`#general`、各グループの `#<name>-wg`・`#<name>-ig`、各 SDK の `#<lang>-sdk-dev`、`#inspector-dev` などを挙げ、新しいグループの提案は `#wg-ig-group-creation` で行う。非公開のチャンネルに入れる人に、指定されたメンテナーに加えて Community Moderators が加わった
- **Decision records**: Discord は記録の場ではないとし、決定に向かう Discord の議論は GitHub Discussion に移す。SEP に関する Core Maintainer の結論を含むすべての技術・ガバナンスの決定は、`notes` ラベルの Discussion か SEP の PR に書く。これまでは、Discussions または Issues に記録すること、決定の種類ごとの記録先の表が書かれていた
- **削除された節**: Security Issues の節（SECURITY.md の手順に従う、Lead か Core Maintainers に直接連絡する、など）はなくなった。脆弱性の報告は Project Policies の節が案内する

- [Communication - MCP Docs](https://modelcontextprotocol.io/community/communication#decision-records)
- [Communication - MCP Docs](https://modelcontextprotocol.io/community/communication#discord)

## 7. SDK Tiers

SDK Tiering System から改称され、146 行から 109 行に、見出しは 9 個から 8 個になりました。

- **冒頭**: SEP-1730 で採択され、SDK Working Group が運用し、各 SDK の現在の tier は SDKs のページに示される、と述べる。日程を示す NOTE（2026年01月23日に適合性テストが利用可能になり、2026年02月23日に公式の tier 付けを公開する）と、Overview の節がなくなった。3 つの tier の説明は Tier requirements の冒頭の段落に移った
- **Tier requirements**: 要件の表（適合性テストの合格率 100%・80%・最低なし など）は変わらない
- **Conformance testing**: tier ごとの合格率の箇条書きを削り、「各公式 SDK は既定のブランチでテストスイートを実行し、結果を公開する」と書いた
- **Tier advancement**: 手順の 3 つ目が「自動の適合性テストに合格する」から「最新の安定版で、求める tier の合格率に達する」になった。SDK Working Group は、決定と理由を自分たちの憲章のとおり記録する
- **Tier relegation**: 4 週間続けて失敗した場合の基準と、2 か月放置された issue による降格は同じ。Tier 1 の SDK が非推奨を利用者に示し続けない場合も SDK Working Group が降格できる、という段落が加わった。この規定は Feature Lifecycle and Deprecation の Tier 1 SDK Obligations の節に以前からある
- **Issue triage labels**: 文言の整理だけ

- [SDK Tiers - MCP Docs](https://modelcontextprotocol.io/community/sdk-tiers#conformance-testing)
- [SDK Tiers - MCP Docs](https://modelcontextprotocol.io/community/sdk-tiers#tier-relegation)

## 8. Group Charter Template

157 行から 122 行になり、見出し（コードフェンスの外）は Example Mission Statements の 1 個から Submitting a charter と Template の 2 個になりました。Submitting a charter の内容はハイライト 5 のとおりです。テンプレート自体の変更は次のとおりです。

- コードフェンスの言語が `markdown` から `mdx` になり、各節のガイドのコメントが HTML コメントから `{/* */}` になった
- Group Type の節には「どちらかを残し、もう一方を消す」と、Mission Statement の節には書き出しの例文が書かれた
- Authority & Decision Rights の節のコメントに、表の各行は通常の割り当てで憲章とともに承認されること、変更は Amending or retiring a group に従って Changelog に行を加えることが書かれた
- Active Work Items の例が `SEP-XXXX` と、状態 `draft / in-review / accepted` になった（これまでは `SEP-XXX` と `Draft / Review / Approved`）
- 末尾の Example Mission Statements の節（Transport WG と Enterprise IG の例文）がなくなり、記入済みの例として Transports の WG と Security の IG の憲章を示す NOTE に替わった

- [Group Charter Template - MCP Docs](https://modelcontextprotocol.io/community/charter-template#template)

## 軽微な更新

<!-- light:minor-updates:start -->
差分のあった 14 ページのうち、ハイライトと新規追加・大幅更新で扱った 10 ページのほかに、次の変更がありました。

**機能改善**

- Design Principles の冒頭に、原則の適用範囲と使い方の説明が加わった — [Design Principles](https://modelcontextprotocol.io/community/design-principles)
  - これらの原則は SEP と拡張に適用され、サーバーとクライアントの作り方を述べる仕様の architecture の設計原則とは別のもの
  - Core Maintainers は SEP の採否の理由にこれらの原則を挙げる
  - 原則に反する提案は、そのことを明示して理由を述べる
  - 2 つの原則がぶつかるときは、順位ではなく比較して判断する
- Design Principles の Demonstration over deliberation に、SEP は採択の前に動くプロトタイプが要るという一文が加わった（SEP Guidelines の Prototype Requirements へのリンク付き） — [Design Principles](https://modelcontextprotocol.io/community/design-principles#demonstration-over-deliberation)
- Design Principles の Stability over velocity に、削除は Feature Lifecycle and Deprecation に従うという一文が加わった。速い出荷に慣れた人には歯がゆいかもしれない、という文はなくなった — [Design Principles](https://modelcontextprotocol.io/community/design-principles#stability-over-velocity)
- Antitrust Policy の冒頭で、NOTE が 1 文に替わった。旧 NOTE には、コードやドキュメントに取り組む個々のコントリビューターは日常の作業でこの方針を気にする必要はほぼない、という説明もあった。新しい文は、この方針が MCP の会議・working group・interest group など、競合他社が居合わせうるすべての場に適用される、と述べ、Meetings and channels へのリンクを添えている — [Antitrust Policy](https://modelcontextprotocol.io/community/antitrust)

**その他**

- Security Policy（`community/security`）のページが、索引と本文から削除された（69 行。詳細はハイライト 3 参照）
- 索引 `llms.txt` で、コミュニティ文書の並びが変わった。4 ページの改称と 7 ページの説明文の書き換え、2 ページの追加と 1 ページの削除があった（詳細はハイライト 1 参照）
- Design Principles で文言を整理した。Convergence over choice と Capability over compensation ではダッシュ（—）をカンマとコロンに替えた。Composability over specificity と Standardization over innovation では 2 段落を 1 段落にまとめた — [Design Principles](https://modelcontextprotocol.io/community/design-principles#composability-over-specificity)
- The MCP Registry の The MCP Registry Ecosystem の節で、エコシステムの図の画像 URL が変わった（URL 内のハッシュのみ） — [The MCP Registry](https://modelcontextprotocol.io/registry/about#the-mcp-registry-ecosystem)
<!-- light:minor-updates:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-11-07.md](./archives/latest/2026-11-07.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-11-07.md](./archives/latest-detail/2026-11-07.md)

<!--
base_commit: 0b52aad1c2858e15e1387c14baa0116109fe73bd
head_commit: a8f23232a803b4b46f1561458d9a33dd135a159b
generated_at_full: 2026-11-10T15:36:37+09:00
-->
