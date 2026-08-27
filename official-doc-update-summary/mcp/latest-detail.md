---
対象期間: 2026年08月25日 〜 2026年08月26日
作成日: 2026-08-26
---

# MCP 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
今回の対象期間に差分が出たのはページ本文を収める `llms-full.txt` の 1 件のみで、索引ファイル `llms.txt` には変更がありません。追加 159 行・削除 6 行のうち 153 行は、前回索引に加わったばかりの Transports Charter の本文です。

主要なものを以下に挙げます。

1. MCP Transports Working Group の charter 本文 153 行が `llms-full.txt` に収録された。前回時点では索引にエントリがあるだけで本文が欠けていたが、今回それが解消し、スコープ・リーダーシップ・意思決定権限・運営方法が確認できるようになった。charter 自体の初版制定は 2026年08月23日
2. 既存 6 ページ（Authorization / Security / Agents / Interceptors / SDK / Triggers and Events の各 charter）の `Related Groups` で、Transports WG への言及がサイト内リンクに書き換えられた。うち Agents Charter の 1 件は外部 GitHub リポジトリ URL からサイト内パスへの切り替え
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**Transports WG charter の本文が収録**](#1-transports-wg-charter-の本文が収録):  
  `community/working-groups/transports` の本文 153 行が `llms-full.txt` に加わった。前回サマリの時点では索引 `llms.txt` にエントリがあるだけで本文が未収録という状態だったが、今回この欠落が解消した。ミッション・スコープ・リーダーシップ・意思決定権限・運営が確認でき、charter の Changelog には 2026年08月23日 に初版が制定されたと記録されている。
2. [**既存 charter からの Transports WG 参照がリンク化**](#2-既存-charter-からの-transports-wg-参照がリンク化):  
  6 つの charter ページの `Related Groups` にあった Transports WG への言及が、いずれもサイト内リンク `/community/working-groups/transports` になった。今回の削除 6 行はすべてこの書き換えによるもので、5 件は太字プレーンテキストからのリンク化、Agents Charter の 1 件は外部 GitHub リポジトリ URL からサイト内パスへの切り替え。
<!-- light:highlight-list:end -->

## 1. Transports WG charter の本文が収録

今回の差分はページ本文を収める `llms-full.txt` に限られ、追加 159 行・削除 6 行という内訳です。索引 `llms.txt` には 1 行の変更もありません。追加分の大半にあたる 153 行が `Transports Charter`（`community/working-groups/transports`）の本文で、収録位置は Skills Over MCP Charter と Triggers and Events Charter の間、つまり索引と同じアルファベット順の並びです。

前回のサマリでは、このページが索引 `llms.txt` に追加された一方で本文が `llms-full.txt` に未収録であること、そのためミッション・スコープ・リーダーシップといった charter の中身が入力からは確認できないことを記していました。今回の差分はその欠落を解消するもので、索引が先に更新され本文が翌日追いついた形になります。charter 本文の Changelog に記録された初版制定日は 2026年08月23日 で、索引に載った日より前です。charter の具体的な中身は次の「新規追加されたページ」で扱います。

- [Transports Charter - MCP Docs](https://modelcontextprotocol.io/community/working-groups/transports)

## 2. 既存 charter からの Transports WG 参照がリンク化

charter 本文の収録と同時に、既存 6 ページの `Related Groups` セクションにあった Transports WG への言及がサイト内リンクへ書き換えられました。対象は Authorization Charter（Auth IG、認可が現状 HTTP トランスポート層で規定されているため資格情報の運搬先がトランスポート変更の影響を受けるという文脈）、Security Charter（Security IG、stdio のプロセス分離と未認証のメソッド面）、Agents Charter（タスクのポーリング・複数往復のリクエスト・ステートレス動作・リクエスト紐付けがトランスポートとメッセージフローのセマンティクスに依存するという文脈）、Interceptors Charter（インターセプターが動作する MCP メッセージフローの配送挙動はトランスポートに依存する）、SDK Working Group Charter（トランスポート実装は各 SDK の相当部分を占めるため transport SEP 着地時のロールアウト順序を調整する）、Triggers and Events Charter（配送・順序の保証はトランスポート能力に依存し、コールバックのセマンティクスは stdio・Streamable HTTP・将来のトランスポートで一貫している必要がある）の 6 件です。周辺の説明文はいずれも変更されておらず、変わったのは参照の表記だけです。

6 件のうち 5 件は `**Transports WG**` という太字のプレーンテキスト（リンクなし）からの変更で、参照先ページが存在しなかったこれまでの状態に対応しています。残る Agents Charter の 1 件だけは、もともと上流リポジトリ `https://github.com/modelcontextprotocol/transports-wg` を指す外部リンクになっており、これがサイト内パス `/community/working-groups/transports` へ差し替えられました。なお、新設された Transports Charter 側の `Related Groups` が挙げているのは SDK WG・Agents WG・Triggers and Events WG・Auth IG・Security IG の 5 つで、Interceptors Charter からの参照だけは片方向のままです。

- [Agents Charter - MCP Docs](https://modelcontextprotocol.io/community/working-groups/agents#related-groups)
- [Authorization Charter - MCP Docs](https://modelcontextprotocol.io/community/interest-groups/auth#related-groups)

## 新規追加されたページ

<!-- light:new-pages:start -->
今回本文が新たに収録されたページは次の 1 件です。索引 `llms.txt` には前回すでにエントリが載っていたため、索引側の件数（348 件）に変化はありません。

- [**Transports Charter**](#1-transports-charter) ([MCP Docs](https://modelcontextprotocol.io/community/working-groups/transports)):  
  MCP Transports Working Group の charter 本文 153 行が `llms-full.txt` に収録された。トランスポートバインディング・スケーラビリティと信頼性・トランスポート隣接のプロトコルアーキテクチャ・トランスポートセキュリティを扱い、WG リードは Kurtis Van Gent。上流の GitHub リポジトリに詳細を委ねつつ、境界の定義はこの charter 側に留保する構成になっている。
<!-- light:new-pages:end -->

## 1. Transports Charter

Transports Working Group のミッションは、ローカル／リモート双方の配備で実装が相互運用可能・スケーラブル・信頼でき運用しやすい状態を保てるよう、MCP のトランスポートバインディングとトランスポート隣接のプロトコルアーキテクチャを進化させることと定義されています。成果物はトランスポート提案・SEP・実装エビデンス・ガイダンスの 4 種です。In Scope は 6 項目で、**Transport Bindings**（フレーミング、配送、リクエストとエンベロープのメタデータ、キャンセルと終了、接続ライフサイクル、後方互換性。バインディングとコアプロトコルのセマンティクスの境界は仕様の transport overview が定める）、**Scalability and Reliability**（接続管理、リソース効率、多重化、負荷分散、エラー処理、再接続、再開、配送と順序の保証）、**Transport-Adjacent Protocol Architecture**（リクエスト紐付け、リクエスト単位のメタデータ、ステートレス動作、レガシーな初期化・トランスポートセッションモデルからの移行）、**Transport Security**（Origin 検証・TLS・mTLS・証明書の扱い。Security IG と協調し、資格情報の運搬は Auth IG と協調）、**Validation and Guidance**（リファレンス実装・実験・実装エビデンス・ドキュメント。適合性テストにはシナリオと要件を提供するが、スイート自体はその保守担当が所有する）、**Cross-Cutting Coordination**（他グループの作業がトランスポートに与える影響の調整。アプリケーション層の機能自体は引き取らない）が挙がっています。

Out of Scope も明示的で、ツール・リソース・プロンプト・タスク・エージェント・イベントといった MCP プリミティブのアプリケーション層挙動（アプリケーション状態、アプリケーションセッションの意味、タスクのライフサイクル、イベント／サブスクリプションのセマンティクスを含む）、ドメイン固有の拡張と製品・ビジネス上の関心事、トランスポートと無関係な SDK API、認可プロトコルの機構・資格情報とトークンのセマンティクス・アプリケーション identity・認可ポリシー、そして適合性スイートの所有権が除外されています。特徴的なのは上流ドキュメントとの関係の扱い方で、技術的な焦点や提案戦略の詳細は上流リポジトリ `modelcontextprotocol/transports-wg` の `CHARTER.md` に委ねる一方、上流の scope statement はあくまで補足的な文脈を与えるもので、この charter が定める境界を拡大することはできないと釘を刺しています。

運営面では、WG リードは Kurtis Van Gent です。意思決定権限は 8 行の表で整理されており、会議のロジスティクスとスケジューリング・WG 内の提案優先順位付け・スコープ内 SEP のトリアージとクローズ（根拠の文書化が条件）は WG リードの裁量、スコープ内の技術設計は WG コンセンサス、追加的な仕様変更は WG コンセンサスに加えてコアメンテナー承認、破壊的・根本的な仕様変更にはさらに広範なレビューが必要、スコープ拡大はコアメンテナー承認必須、という段階構成です。会議は週次で、時刻と参加方法は meet.modelcontextprotocol.io に掲載され、非同期の議論は MCP Discord の `#transports-wg` で行われます。作業手順は問題定義を先に置くワークフローで、①WG リポジトリに core problem statement を作成して問題と要件について合意する、②関心のある参加者と解決策を定義する、③WG のフィードバックを踏まえてレビューと反復を行う、④WG が意思決定プロセスに沿って合意に達した後、SEP プロセスを通じてコアメンテナーへ提示する、の 4 段階です。Changelog は 2026年08月23日 の「Initial charter」1 行のみで、今回が初版の公開にあたります。

- [Transports Charter - MCP Docs](https://modelcontextprotocol.io/community/working-groups/transports)

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
今回の対象期間に大幅な更新（本文 50 行以上の変更）があった既存ページはありません。既存ページに対する変更は 6 ページで各 1 行のみです（詳細はハイライト 2 参照）。
<!-- light:updated-pages:end -->

## 軽微な更新

<!-- light:minor-updates:start -->
今回差分が出たファイルは `llms-full.txt` の 1 件のみで、Transports Charter 本文の収録（ハイライト 1 参照）を除くと、既存ページ側の変更は次の 1 点にまとまります。

**その他**

- 6 つの charter ページ（Working Group 4 件・Interest Group 2 件）の `Related Groups` で、Transports WG への言及がサイト内リンクに書き換えられた。削除 6 行・追加 6 行はすべてこの変更によるもの（詳細はハイライト 2 参照）
<!-- light:minor-updates:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-08-25.md](./archives/latest/2026-08-25.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-08-25.md](./archives/latest-detail/2026-08-25.md)

<!--
base_commit: 9183e5fb58ed21ba3079f4e0f6a528c4e46d1ea7
head_commit: 1178d4a1adaaa1829aeb0ab27ac4940eb1bd90bb
generated_at_full: 2026-08-27T15:33:42+09:00
-->
