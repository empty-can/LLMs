---
対象期間: 2026年08月02日 〜 2026年08月05日
作成日: 2026-08-05
---

# MCP 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
今回の対象期間は、Agents ワーキンググループの憲章が新規公開された 1 件が実質的な変更のすべてです。新規追加 1 ページ・大幅更新 0 ページ・軽微更新 1 ページで、残る 1 件はコアメンテナー一覧の異動にとどまります。

主要なものを以下に挙げます。

1. エージェントを背後に持つシステムとの相互運用を扱う Agents ワーキンググループが発足し、憲章が公開された
2. Tasks 拡張（SEP-2663）の安定化とコアプロトコルへの昇格が、この WG の第一の作業項目として明記された
3. Agents Extension を新設するかどうかは予断せず、既存プリミティブで足りるかを含めて評価する段階と位置づけられた
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**Agents ワーキンググループの新設**](#1-agents-ワーキンググループの新設):  
  エージェントを背後に持つシステムとのやり取りを MCP 上で相互運用可能にすることを目的とする Working Group が発足した。リードは Luca Chang（Amazon Web Services）と Caitie McCaffrey（Microsoft）の 2 名で、週 1 回 30 分の作業セッションと Discord の `#agents-wg` チャンネルを持つ。Roadmap が「Agent Communication」の担い手として名前を挙げていたグループが、憲章を伴って正式に立ち上がった形になる。
2. [**Tasks 拡張のコアプロトコル昇格が正式な作業項目に**](#2-tasks-拡張のコアプロトコル昇格が正式な作業項目に):  
  `io.modelcontextprotocol/tasks` 拡張の安定化と、それを MCP のコアプロトコルへ昇格させることがスコープの筆頭に置かれた。成功基準にも「拡張からコアプロトコルへ昇格していること」が明記され、実装フィードバックの収集・曖昧さの解消・ライフサイクル変更案の評価が具体的な作業として挙げられている。
3. [**Agents Extension は要否の評価から始める**](#3-agents-extension-は要否の評価から始める):  
  憲章は Agents Extension を作ると決めていない。agent-as-tool・remote-agent・supervisor/sub-agent という利用パターンを検討したうえで、Tasks を発展させるか、Agents Extension を導入するか、既存プリミティブの使い方を文書化するかを選ぶ建て付けになっている。エージェントフレームワークの内部（計画・記憶・モデル選択・オーケストレーション）は明示的に対象外とされた。
<!-- light:highlight-list:end -->

## 1. Agents ワーキンググループの新設

MCP コミュニティに Agents ワーキンググループが追加され、その憲章ページが公開されました。`llms.txt` のワーキンググループ憲章一覧にも `community/working-groups/agents` が加わり、既存の File Uploads / Inspector V2 / Interceptors / Registry / SDK / Server Card / Skills Over MCP / Triggers and Events に並ぶ 9 件目になっています。

ミッションは「エージェントを背後に持つシステムとのやり取りを MCP 上で相互運用可能にすること」です。憲章は現状認識として、この種のシステムが通常のツールとして公開されるか、フレームワーク固有の統合を通じて提供されるにとどまっており、永続的な実行・能力の発見・委譲・複数ターンのやり取りが場当たり的な取り決めに委ねられていると述べています。そのうえで WG は Tasks を「MCP における永続的な非同期実行の基盤」として管理し、残るギャップのうちどれがプロトコルの支援を必要とするかを見極める、という位置づけを取ります。

このグループの発足自体は Roadmap で予告されていました。Roadmap の優先領域「Agent Communication」は、Tasks 拡張が call-now / fetch-later のパターンを与えた一方で本番運用によりライフサイクル意味論のギャップ（一時的な失敗時の再試行の意味論、完了後に結果を保持する期間と失効の伝え方）が露呈したとし、それらを **Agents WG** が閉じるべき課題として挙げていました。今回の憲章公開は、その担い手が実体を伴って立ち上がったことにあたります。

運営面では、リードが Luca Chang（Amazon Web Services、@LucaButBoring）と Caitie McCaffrey（Microsoft、@CaitieM20）の 2 名で、いずれも Term は Initial です。会合は週 1 回 30 分の Working Session、連絡先は Discord の `#agents-wg`、リポジトリは `modelcontextprotocol/agents-wg` です。意思決定権限の表では、会合の運営・WG 内の提案の優先順位付け・スコープ内 SEP のトリアージと打ち切りがリードの裁量（SEP の打ち切りは根拠の文書化が条件）、技術設計は WG の合意、追加的な仕様変更は WG 合意＋コアメンテナー承認、破壊的・根本的な変更はそれに加えてさらに広範なレビュー、スコープ拡大はコアメンテナー承認が必要と整理されています。憲章の Changelog には 2026年08月04日付の初版のみが記載されています。

- [Agents Charter - MCP Docs](https://modelcontextprotocol.io/community/working-groups/agents#mission-statement)
- [Roadmap - MCP Docs](https://modelcontextprotocol.io/development/roadmap#2-agent-communication)

## 2. Tasks 拡張のコアプロトコル昇格が正式な作業項目に

スコープの筆頭は Tasks です。`io.modelcontextprotocol/tasks` 拡張を安定化させ、MCP のコアプロトコルへ昇格させることが明記され、その内訳として実装フィードバックの収集、曖昧さの解消、ライフサイクルに対する変更提案の評価が挙げられています。憲章のリソース節では、Tasks 拡張のリポジトリとして `modelcontextprotocol/ext-tasks` が、仕様として SEP-2663（Tasks Extension）が示されました。

成功基準にも同じ方向が繰り返されています。「Tasks が実装フィードバックに基づいて完全に安定化され、拡張からコアプロトコルへ昇格していること」「Tasks の安定化を妨げるライフサイクルの曖昧さと適合性のギャップが解消されるか、明示的に処理されていること」の 2 点が並び、作業項目の表でも「Tasks stabilization and core protocol promotion」が In Progress として @LucaButBoring をチャンピオンに立てています。

Tasks はもともと `2025-11-25` 仕様に実験的機能としてコアプロトコル側にあり、Draft 仕様でコアから外して `io.modelcontextprotocol/tasks` 拡張へ移された経緯があります（SEP-2663）。今回の憲章は、拡張として運用しながら安定化させ、そのうえで改めてコアへ組み入れるという道筋を、WG の目標として明文化したことになります。

- [Agents Charter - MCP Docs](https://modelcontextprotocol.io/community/working-groups/agents#in-scope)
- [Agents Charter - MCP Docs](https://modelcontextprotocol.io/community/working-groups/agents#success-criteria)

## 3. Agents Extension は要否の評価から始める

憲章は Agents Extension の新設を既定路線としていません。スコープ内の「Agents Extension Evaluation」は、agent-as-tool・remote-agent・supervisor/sub-agent といったエージェントを背後に持つ MCP の利用事例を評価し、Tasks を補完する Agents Extension が必要かどうかを判断する、という書き方です。「Prototypes and Proposals」も、Agents Extension を導入するか・Tasks を発展させるか・既存の MCP プリミティブに頼るかを見極める助けになる範囲で、狭くスコープを絞った実証を作ると限定しています。憲章は明示的に「推論やエージェントループがどこで動くか、ある能力が Tasks・Agents Extension・既存プリミティブのどれに属するかを予断しない」と述べ、それらは設計作業を通じて評価する問題だとしています。

スコープ外も明確です。汎用的なエージェントフレームワークとランタイムの構築・標準化は対象外で、そこには計画・記憶・モデル選択・オーケストレーションといった内部的な選択も含まれます。WG が標準化するのは MCP の相互運用境界における挙動であって、ホストやサーバーの実装内部ではない、という線引きです。トランスポートのワイヤフォーマットとセッションの仕組みは Transports WG が、一般的なイベント配送とコールバックの仕組みは Triggers and Events WG が所有するとして、それぞれ関連グループにも挙げられています。

作業項目の表には In Progress の項目が 3 つ並びます。Tasks の安定化とコアプロトコル昇格、Agents Extension の評価と勧告（チャンピオンは TBD）、そして「Two-level agent definition proof of concept」（@LucaButBoring と @madhaviai）です。成功基準の末尾も「提案されたエージェントプロトコルの表面は、前進させる前にプロトタイプと実装フィードバックを通じて評価される」となっており、評価を先行させる姿勢が一貫しています。

- [Agents Charter - MCP Docs](https://modelcontextprotocol.io/community/working-groups/agents#out-of-scope)
- [Agents Charter - MCP Docs](https://modelcontextprotocol.io/community/working-groups/agents#active-work-items)

## 新規追加されたページ

<!-- light:new-pages:start -->
- [**Agents Charter**](#1-agents-charter) ([MCP Docs](https://modelcontextprotocol.io/community/working-groups/agents)):  
  MCP Agents ワーキンググループの憲章。ミッション・スコープ・関連グループ・リーダーシップ・意思決定権限・メンバーシップ・運営・リソース・成果物と成功基準が、既存の憲章ページと同じ節構成で定義された（詳細はハイライト 1〜3 参照）。
<!-- light:new-pages:end -->

## 1. Agents Charter

Agents ワーキンググループの憲章ページです。Group Type は Working Group で、ミッション、スコープ（内・外・関連グループ）、リーダーシップ、意思決定権限、メンバーシップ、運営、リソース、成果物と成功基準、Changelog という、既存のワーキンググループ憲章と同じ節構成を取っています。ミッションと運営体制はハイライト 1、Tasks に関する作業項目はハイライト 2、Agents Extension の扱いとスコープ外の線引きはハイライト 3 で扱いました。

スコープ内の項目としては、そこで触れた Tasks・Agents Extension の評価・プロトタイプに加えて 3 つが挙がっています。実装調整（SDK と適合性テストのメンテナーと、グループが所有する仕様の実装フィードバック・サンプル・カバレッジについて連携する）、横断的関心事（Tasks や評価対象のエージェント利用事例がトランスポート・イベント・スキル・認可・メタデータ・外部との相互運用に関わる問題を生じたときに、関連グループと連携する）、ドキュメント（Tasks 仕様の維持と、エージェントを背後に持つ MCP の利用事例・知見・グループが採択した提案の文書化）です。

メンバーシップ表には現時点でリード 2 名（Luca Chang / Caitie McCaffrey）のみが載っており、Lead 以外の Level のメンバーはまだ登録されていません。WG メンバーの承認は「WG メンバーのスポンサー」によると意思決定権限の表に定められています。会合は meet.modelcontextprotocol.io で公開され、リソースとして WG リポジトリ `modelcontextprotocol/agents-wg`、Tasks 拡張リポジトリ `modelcontextprotocol/ext-tasks`、Tasks 仕様の SEP-2663 が示されています。

- [Agents Charter - MCP Docs](https://modelcontextprotocol.io/community/working-groups/agents)

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
既存ページ本文に 50 行以上の変更があったページはありません。新規ページ以外の変更は 1 行の異動のみで、下記「軽微な更新」に整理しています。
<!-- light:updated-pages:end -->

## 軽微な更新

<!-- light:minor-updates:start -->
新規ページ以外に変更のあったページは 1 件で、メンテナー一覧の異動です。

**その他**

- Governance and Stewardship ページで、Nick Aldridge が「Current Core Maintainers」の一覧から外れ、「Emeritus」へ `Core Maintainer Emeritus` として移った。Lead Maintainers（David Soria Parra / Den Delimarsky）と、残る 6 名のコアメンテナーに変更はない — [Governance and Stewardship](https://modelcontextprotocol.io/community/governance#emeritus)
<!-- light:minor-updates:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-08-02.md](./archives/latest/2026-08-02.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-08-02.md](./archives/latest-detail/2026-08-02.md)

<!--
base_commit: cd5d9d06955862d48e3c3baead8d13981f95665d
head_commit: 2d8e1c4da653076ba8407a1a3ad4fb3b54462e01
generated_at_full: 2026-08-06T15:30:35+09:00
-->
