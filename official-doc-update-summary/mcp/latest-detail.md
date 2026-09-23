---
対象期間: 2026年09月16日 〜 2026年09月23日
作成日: 2026-09-23
---

# MCP 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
今回の対象期間では本文 `llms-full.txt` の 9 ページに差分があり（追加 215 行・削除 72 行）、索引 `llms.txt` には Infrastructure Working Group の憲章が 1 件加わりました。中心は、SEP-2640「Skills Extension」が Final 済みであることを前提にした関連ページの書き換えと、コミュニティ運営まわりの整備です。

主要なものを以下に挙げます。

1. Skills 拡張（`io.modelcontextprotocol/skills`）が Final 済みの公開仕様であることを前提に、Skills 概要ページ・Skills Over MCP WG 憲章・Filesystems WG 憲章・Primitive Grouping IG 憲章の 4 ページが書き換えられた
2. MCP の共有インフラと管理作業の自動化を担う Infrastructure Working Group の憲章が新設された（Lead 3 名）
3. Contributing ガイドに「Join the Community」節が新設され、SEP のスポンサー探しの節が「Getting Help」配下から仕様リポジトリの作業手順（Major Protocol Changes の直後）へ移された
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**Skills 拡張が Final 済みの前提で関連 4 ページを一斉に書き換え**](#1-skills-拡張が-final-済みの前提で関連-4-ページを一斉に書き換え):  
  Skills 概要ページが ext-skills リポジトリを「公開済みの公式 Skills 拡張（`io.modelcontextprotocol/skills`）の仕様」と位置づけ直し、SEP-2640 が Final であると明記した。Skills Over MCP WG 憲章は進行中の作業項目表を廃して「Completed Milestones」「Current Work」に組み替え、Filesystems WG・Primitive Grouping IG の両憲章も Skills 拡張への言及を公開版前提の記述に改めた。
2. [**Infrastructure Working Group の憲章を新設**](#2-infrastructure-working-group-の憲章を新設):  
  組織への招待・権限管理、GitHub 管理、グループ立ち上げ、会議・連絡基盤、ホスティングや公開などの定型的な管理作業を、メンテナーや貢献者がセルフサービスで行えるようにすることを使命とする WG が発足した。Lead は David Soria Parra・Den Delimarsky（Anthropic）と Sambhav Kothari（Bloomberg）の 3 名。
3. [**Contributing ガイドを再編し SEP スポンサー探しの節を仕様リポジトリの作業手順へ移動**](#3-contributing-ガイドを再編し-sep-スポンサー探しの節を仕様リポジトリの作業手順へ移動):  
  「Before You Begin」の冒頭に、変更を用意していなくても MCP Contributor Discord などで参加できると案内する「Join the Community」節が新設された。「Finding a Sponsor for SEPs」節は内容を変えずに Major Protocol Changes の直後へ移り、手順とトラブルシューティングの 2 箇所から同節への相互参照が張られた。
<!-- light:highlight-list:end -->

## 1. Skills 拡張が Final 済みの前提で関連 4 ページを一斉に書き換え

今回の差分でいちばん広い範囲に及んだのは、Skills 拡張の位置づけの更新です。なお `SEP-2640: Skills Extension` のページ自体は今回の差分に含まれていません。同ページは今回の断面でも Final バッジを掲げていますが、今回の変更は、SEP-2640 が Final 済みであるという事実に合わせて**周辺の 4 ページが記述を追従させた**ものです。

**Skills 概要ページ**（`extensions/skills/overview`）では、冒頭の説明が「ext-skills リポジトリには Skills over MCP の仕様がある」という 1 文から、「ext-skills リポジトリには公式 Skills 拡張（`io.modelcontextprotocol/skills`）の公開済み仕様がある。SEP-2640 は Final である」という記述に置き換わりました。続けて、この拡張を Skills Over MCP Working Group が保守していること、SDK とホストでの対応はまだ実装途上であることが述べられ、現在の対応状況の確認先として client support matrix（`extensions/client-matrix`）と ext-skills リポジトリの implementations list が示されています。

**Skills Over MCP WG 憲章**（`community/working-groups/skills-over-mcp`）は、WG の現況を表す部分が全面的に書き直されました。Mission Statement では、WG の方向性を「SEP-2640（Resources ベース、Extensions Track）に集約されている」としていた記述が削られ、代わりに「SEP-2640 は Final。WG は公式 Skills 拡張を ext-skills リポジトリで保守し、現在は実装支援・相互運用性・公開済み拡張の発展に注力している」と記されています。In Scope の Specification Work も「Skills 拡張の保守と発展（変更は ext-skills の decision log で追跡）、関連するコアプロトコル変更は SEP プロセスで提案」に改められました。Deliverables では、SEP・参照実装などの状況と champion を並べていた Active Work Items の表（4 項目）が廃止され、次の 3 点を挙げる **Completed Milestones** に置き換わりました。

- SEP-2640 が 2026年09月13日にマージされ **Final** になったこと
- 公式仕様が ext-skills の `specification/stable/skills.mdx` として公開され、Web サイトにも概要ページがあること
- Skills の conformance シナリオ（modelcontextprotocol/conformance の PR #330）が 2026年09月11日にマージされたこと

以降の作業追跡は **Current Work** として ext-skills リポジトリの issue に一本化され、担当者・進捗・優先度は憲章ではなく issue 側で管理すると明記されています。Success Criteria も短期・中期・長期の 3 段階から、**Specification**（Resources ベースの Skills 拡張を公開する ―― Final SEP-2640 で達成済み）・**Implementation**（該当する conformance シナリオに合格する SDK／ホスト実装）・**Interoperability**（独立した MCP サーバーとクライアントが skill を一貫して発見・読み込みできること）の 3 観点に組み替えられました。Resources 欄からは project board と experimental-ext-skills リポジトリへのリンクが外れ、Skills 拡張の概要、Final SEP-2640、ext-skills リポジトリ、implementations とクライアント対応状況、decision log とアーカイブ済みの設計資料へのリンクに入れ替わっています。

**Filesystems WG 憲章**の Related Groups では、Skills Over MCP WG との関係が「ファイルシステム依存（書き込みアクセスの問題を含む）は 2026年03月24日のオフィスアワーの議題になり、未解決のまま」という記述から、「公開済みの Skills 拡張はファイル読み込みに Resources を使い、ディレクトリ読み込みを任意機能として定義している。ファイルシステムの書き込み操作には依存しない。skill に影響する今後のリソース操作について調整する」という記述に更新されました。**Primitive Grouping IG 憲章**でも、Related Groups の Skills Over MCP WG の説明が「公開済み Skills 拡張を保守しており、skill の発見と段階的開示（progressive disclosure）がグルーピングと重なる」に改められ、Beyond Scope の「MCP サーバーの整理」は、サーバー発見とレジストリスキーマの決定は Registry WG が担い、Skills Over MCP WG は skill 配布の要件を提供する、という役割分担の記述に変わりました。

- [Skills - MCP Docs](https://modelcontextprotocol.io/extensions/skills/overview)
- [Skills Over MCP Charter - MCP Docs](https://modelcontextprotocol.io/community/working-groups/skills-over-mcp#completed-milestones)

## 2. Infrastructure Working Group の憲章を新設

新しい Working Group として **Infrastructure Working Group** の憲章（`community/working-groups/infrastructure`）が追加され、索引 `llms.txt` にもエントリが 1 件加わりました。憲章の変更履歴には 2026年09月22日付の初稿として記録されています。

Mission Statement によれば、この WG は MCP の共有インフラと自動化を構築・保守し、日常的な管理作業をメンテナーや貢献者がセルフサービスで行えるようにすることを目的とします。「誰が何をできるか」を決めるのは Governance であり、Infra はその決定を標準的なツールとワークフローで実装する、という役割分担が明示されています。In Scope には、組織への招待・チームメンバーシップ・権限・アカウント発行（WG の Lead が、まだ PR を出せない貢献者も含めて自グループのメンバーを招待・管理できるようにすることを含む）、GitHub 管理、承認済みグループの立ち上げ、会議と連絡（Google Workspace、メーリングリスト、カレンダー、Discord 連携など）、planning・voting・meeting の各共有サービスの改善、Web サイトやドキュメントのホスティング・CI/CD・パッケージ公開・ドメイン・DNS・証明書、そして監視・更新・復旧・不要リソースの撤去までが挙げられています。一方で、ガバナンス方針や投票ルールの策定、プロトコルと SDK の設計、他グループのサービスを所有者の合意なく引き取ることなどは Out of Scope とされています。

Lead は David Soria Parra（Anthropic）、Den Delimarsky（Anthropic）、Sambhav Kothari（Bloomberg）の 3 名です。初期の成果物としては、WG の Lead が自グループのメンバーを招待・管理できる仕組み、アカウント・メール・権限発行の改善、会議設定や通知の自動化、重要イベントの Discord 通知と MCP ブリッジ、既存インフラとその所有者・残る手作業の文書化などが並びます。詳しくは「新規追加されたページ」の項を参照してください。

- [Infrastructure Charter - MCP Docs](https://modelcontextprotocol.io/community/working-groups/infrastructure#mission-statement)

## 3. Contributing ガイドを再編し SEP スポンサー探しの節を仕様リポジトリの作業手順へ移動

`Contributing to MCP` ページ（`community/contributing`）は追加 52 行・削除 42 行と行数上は大きく動きましたが、その大半は既存の節の移動です。

新設されたのは **「Join the Community」** 節で、「Before You Begin」の先頭（Prerequisites の前）に置かれています。変更を用意していなくても参加できるとして MCP Contributor Discord への参加を勧め、コントリビューターやメンテナーとの交流、質問、手が必要な箇所の把握に使えると案内しています。あわせて、ライブコールや GitHub Discussions を含む全チャネルとその使い分けは Contributor Communication ガイドを、すぐに助けが要る場合はページ後半の「Getting Help」を参照するよう示しています。

**「Finding a Sponsor for SEPs」** 節（スポンサーの役割、6 か月スポンサーが付かない SEP は dormant 扱いになる旨の警告、4 ステップの探し方）は、「Getting Help」配下から「Working with the Specification Repository」内の「Major Protocol Changes」の直後へ移されました。移動前後の本文 39 行は完全に一致しており、内容の変更はありません。移動にあわせて、Major Protocol Changes の手順「Find a sponsor」と、トラブルシューティング「I can't find a sponsor for my SEP」の末尾から同節への相互参照リンクが追加されました。また「Getting Help」直下にあった「Communication Channels」の小見出しが削除され、チャネル一覧は「Getting Help」の本文として直接続く形になっています。

- [Contributing to MCP - MCP Docs](https://modelcontextprotocol.io/community/contributing#join-the-community)
- [Contributing to MCP - MCP Docs](https://modelcontextprotocol.io/community/contributing#finding-a-sponsor-for-seps)

## 新規追加されたページ

<!-- light:new-pages:start -->
- [**Infrastructure Charter**](#1-infrastructure-charter) ([MCP Docs](https://modelcontextprotocol.io/community/working-groups/infrastructure)):  
  MCP の共有インフラと管理作業の自動化を担う Infrastructure Working Group の憲章。スコープ、Lead 3 名、意思決定権限、運営方法、初期の成果物と成功基準を定める（詳細はハイライト 2 参照）。
<!-- light:new-pages:end -->

## 1. Infrastructure Charter

Infrastructure Working Group の憲章として新たに収録されたページで、全 114 行です。構成は他の WG 憲章と同じく、Group Type、Mission Statement、Scope（In Scope／Out of Scope／Related Groups）、Leadership、Authority & Decision Rights、Membership、Operations、Deliverables & Success Metrics、Changelog から成ります。

スコープについては、まず「隙間」と「繰り返される手作業」から着手し、うまく機能しているインフラはそのまま残すこと、既存の構成や所有権を変える場合はその所有者と合意することが原則として掲げられています。既存のリポジトリとツールの上に構築し、設定と変更はレビュー・再現できるよう記録するとされています。Related Groups では、SDK WG と SDK メンテナーにはリポジトリ設定・アクセス・CI・公開のための共有ツールを提供しつつ、SDK とそのリリースの責任は SDK メンテナー側に残ること、他の WG／IG についても同様に各グループが自らの作業とサービスに責任を持つことが明記されています。

意思決定権限の表では、会議の運営と WG の優先順位は Lead が自律的に決め、スコープ内のインフラと自動化の設計は WG の合意、WG 所有インフラの定常保守は合意済みの方針の範囲でインフラメンテナーが行い、他チームのインフラの変更には責任者との合意が、WG のスコープ拡大には Core Maintainer の承認が必要とされています。メンバーシップは初期 Lead 以外は参加に応じて記録していくとし、アクセスは `modelcontextprotocol/access` リポジトリで管理されます。運営面では、タスクは関連リポジトリの GitHub issue で追跡し、優先度・担当者・状況・目標日を管理する共有 GitHub Project ボードを作成予定であること、当面の作業セッションは必要に応じて開催し、調整は MCP の Discord 上の Infrastructure Working Group の議論から始めることが記されています。

成功基準としては、定型的な管理作業をプロジェクトのガバナンスが定める承認のもとセルフサービスで完了できること、自動化の前後で所要時間と手作業の手順数を測定して削減すること、同じロールと承認ルールを対象システム全体で一貫して適用すること、WG が管理するリソースには名前付きの所有者・記録された設定・保守／復旧／撤去の手順を備えることなどが挙げられています。

- [Infrastructure Charter - MCP Docs](https://modelcontextprotocol.io/community/working-groups/infrastructure#scope)
- [Infrastructure Charter - MCP Docs](https://modelcontextprotocol.io/community/working-groups/infrastructure#success-criteria)

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
- [**Contributing to MCP**](#1-contributing-to-mcp) ([MCP Docs](https://modelcontextprotocol.io/community/contributing)):  
  「Join the Community」節を新設し、「Finding a Sponsor for SEPs」節を内容はそのまま Major Protocol Changes の直後へ移動した（追加 52 行・削除 42 行。詳細はハイライト 3 参照）。
- [**Skills Over MCP Charter**](#2-skills-over-mcp-charter) ([MCP Docs](https://modelcontextprotocol.io/community/working-groups/skills-over-mcp)):  
  SEP-2640 が Final 済みである前提で Mission Statement・Scope・Resources・Deliverables を書き換え、参加者 1 名を追加した（追加 32 行・削除 21 行。詳細はハイライト 1 参照）。
<!-- light:updated-pages:end -->

## 1. Contributing to MCP

追加 52 行・削除 42 行の変更ですが、そのうち 39 行は「Finding a Sponsor for SEPs」節の移動（削除した 39 行と追加した 39 行が完全に一致）によるものです。実質的な追加は、「Before You Begin」冒頭の「Join the Community」節（9 行）と、同節への相互参照 2 箇所（Major Protocol Changes の「Find a sponsor」ステップ、トラブルシューティング「I can't find a sponsor for my SEP」）です。削除は、移動元の節と「Getting Help」直下の「Communication Channels」小見出しです。

この再編により、SEP のスポンサー探しは「困ったときの相談先」ではなく「大きなプロトコル変更を提案する手順」の一部として読める位置に置かれました。一方で「Getting Help」には Discord などの連絡チャネルの一覧が残り、冒頭の「Join the Community」から同セクションへ案内する導線が加わっています（詳細はハイライト 3 参照）。

- [Contributing to MCP - MCP Docs](https://modelcontextprotocol.io/community/contributing#finding-a-sponsor-for-seps)

## 2. Skills Over MCP Charter

追加 32 行・削除 21 行の変更です。主な内容は、Mission Statement と In Scope の Specification Work を SEP-2640 が Final 済みである前提の記述に改めたこと、Resources 欄のリンクを入れ替えたこと、Deliverables の Active Work Items 表を Completed Milestones と Current Work に置き換えたこと、Success Criteria を Specification・Implementation・Interoperability の 3 観点に組み替えたことです（詳細はハイライト 1 参照）。

このほか、Scope の Cross-Cutting Concerns と Related Groups にあった「Primitive Grouping WG」の表記が、同グループの実際の区分に合わせて「Primitive Grouping IG」に訂正されました。Membership には Nate Barbettini（Arcade.dev）が Participant として追加されています。Changelog に新たに加わった行は 2026年09月15日付の「@nbarbettini（Arcade.dev）を Participant に追加」の 1 件のみで、上記の構成の書き換えは Changelog には記載されていません。

- [Skills Over MCP Charter - MCP Docs](https://modelcontextprotocol.io/community/working-groups/skills-over-mcp#mission-statement)
- [Skills Over MCP Charter - MCP Docs](https://modelcontextprotocol.io/community/working-groups/skills-over-mcp#current-work)

## 軽微な更新

<!-- light:minor-updates:start -->
今回の軽微な更新は 6 ページで、うち 3 ページはハイライト 1 の Skills 拡張に関する追従、残る 3 ページは例示や字句・リンクの修正です。

**機能改善**

- Skills 概要ページの冒頭で、ext-skills リポジトリを公開済みの公式 Skills 拡張（`io.modelcontextprotocol/skills`）の仕様と位置づけ、SEP-2640 が Final であること、保守担当の WG、SDK／ホスト対応状況の確認先を明記（詳細はハイライト 1 参照） — [Skills](https://modelcontextprotocol.io/extensions/skills/overview)
- Filesystems WG 憲章の Related Groups で、Skills Over MCP WG との関係を「未解決の議題」から「公開済み Skills 拡張は書き込み操作に依存しない」という記述に更新（詳細はハイライト 1 参照） — [Filesystems Charter](https://modelcontextprotocol.io/community/working-groups/filesystems#related-groups)
- Primitive Grouping IG 憲章の Related Groups と Beyond Scope で、Skills Over MCP WG の役割を公開済み Skills 拡張の保守者として書き改め、MCP サーバーの整理は Registry WG の担当と明記（詳細はハイライト 1 参照） — [Primitive Grouping Charter](https://modelcontextprotocol.io/community/interest-groups/primitive-grouping#related-groups)

**バグ修正**

- SEP-1330 の「Legacy Single Select With Titles」の JSON 例で、`enumNames` キーを囲む全角引用符（`“ ”`）を ASCII の `"` に修正し、`default` の値を `enum` に含まれない `"Green"` から `enum` の値 `"#00FF00"` に修正 — [SEP-1330: Elicitation Enum Schema Improvements and Standards Compliance](https://modelcontextprotocol.io/seps/1330-elicitation-enum-schema-improvements-and-standards#legacy-single-select-with-titles)

**その他**

- 仕様 2026-07-28 版 Resources ページの Capabilities で、「Serves that support neither `listChanged` or `subscribe`」を「Servers that support neither `listChanged` nor `subscribe`」に字句修正 — [Resources](https://modelcontextprotocol.io/specification/2026-07-28/server/resources#capabilities)
- Financial Services IG 憲章の Operations で、Discord チャネル `#financial-services-ig` のリンク先を `discord.gg/NzkBHsrGf` から `discord.gg/6CSzBmMkjX`（Contributing ガイドが案内する MCP Contributor Discord と同じ招待リンク）に変更 — [Financial Services Charter](https://modelcontextprotocol.io/community/interest-groups/financial-services#operations)
<!-- light:minor-updates:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-09-16.md](./archives/latest/2026-09-16.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-09-16.md](./archives/latest-detail/2026-09-16.md)

<!--
base_commit: fa697d25e355bcd2486c2c9abb1263f94646b401
head_commit: 68860adc30f5a3b9e46aeef4cd6db8b1ccdc288e
generated_at_full: 2026-09-24T02:58:07+09:00
-->
