---
対象期間: 2026年06月25日 〜 2026年06月26日
作成日: 2026-06-26
---

# MCP 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
今回の対象期間の差分は 1 件のみで、前回は llms.txt インデックスへの追加だけが検出されていた金融サービス向けインタレストグループ（Financial Services Interest Group）の憲章ページについて、その本文全体が取得データに反映されました。

主要なものを以下に挙げます。

1. 規制下の金融機関向けに MCP のコンプライアンス・監査性・データ来歴・ガードレール等を扱う金融サービス向けインタレストグループの憲章（ミッション・スコープ・体制・運営方針）が全文公開された
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**金融サービス向けインタレストグループ憲章が全文公開**](#1-金融サービス向けインタレストグループ憲章が全文公開):  
  規制対象の金融機関のステークホルダーが集い、コンプライアンス・監査性・データ来歴・ガードレール等の観点で MCP に必要な適応を特定するインタレストグループの憲章。前回はインデックス追加のみだった本ページの本文（ミッション・スコープ・関連グループ・体制・運営）が今回取得データに反映された。
<!-- light:highlight-list:end -->

## 1. 金融サービス向けインタレストグループ憲章が全文公開

MCP コミュニティに新設された **金融サービス向けインタレストグループ（Financial Services Interest Group, FSIG）** の憲章ページが、前回（インデックスへの 1 行追加のみ）に続いて本文全体まで取得データ（`llms-full.txt`）に反映され、グループの目的・活動範囲・体制が確認できるようになりました。ミッションとして、規制対象の金融機関のステークホルダーが集まり、コンプライアンス・監査性・リスク統制下のデプロイの観点で MCP がどこを適応させる必要があるかを特定すること、金融セクターのユースケースと要件を収集してドメイン固有の拡張を開発・検証すること、広く適用可能な課題を [SEP](https://modelcontextprotocol.io/community/sep-guidelines) やワーキンググループへとスコープ化し、規制環境で実証されたイノベーションを MCP エコシステム全体に還元することを掲げています。

スコープ（In Scope）には、ツール呼び出しが「何を・どの権限で・どのポリシーに照らして」行ったかを改ざん検知可能かつ可搬な形で記録するコンプライアンス・監査性、データの出所・引用・同意メタデータを扱うデータ来歴（lineage / provenance）、サーバー同一性やツール挙動・応答の完全性を実行前に保証するためのガードレールと暗号学的アテステーション、ツール利用とデータ取り扱いに関する宣言的ポリシーの強制、FSIG リポジトリでの金融特化拡張の開発・保守、機関横断の相互運用、コア仕様への SEP 昇格、規制当局・業界団体との連絡（regulatory liaison）が含まれます。一方、価格・コスト・顧客リスト等の競争上機微な非公開情報（[MCP Antitrust Policy](https://modelcontextprotocol.io/community/antitrust) に基づく）、MCP 全体の脅威モデリング（[Security IG](https://modelcontextprotocol.io/community/interest-groups/security) の担当）、OAuth フロー等の認可プロトコルの機構（[Authorization IG](https://modelcontextprotocol.io/community/interest-groups/auth) の担当）、製品固有のコンプライアンスガイド、非技術的なビジネス議論は Out of Scope として明確に切り分けられています。

体制面では、ファシリテーターを Bloomberg の Sambhav Kothari 氏と Saxo Bank の Peder Holdgaard Pedersen 氏が務め、参加は誰でも可能で Discord の `#financial-services-ig` チャンネルで活動します。運営は隔週 60 分のワーキングセッション（ロンドン時間 16:00–17:00, BST/GMT）で、規制監査・アテステーション、データ来歴・引用、ガードレール・セキュリティ、ポリシー強制の 4 つが現在のアジェンダ項目（いずれも Open）として挙げられています。憲章の Changelog には 2026年06月25日 に Initial charter が記録されています。

- [Financial Services Charter - MCP Docs](https://modelcontextprotocol.io/community/interest-groups/financial-services)

## 新規追加されたページ

<!-- light:new-pages:start -->
- [**Financial Services 憲章（Financial Services Charter）**](#1-金融サービス向けインタレストグループ憲章が全文公開) ([MCP Docs](https://modelcontextprotocol.io/community/interest-groups/financial-services)):  
  前回はインデックス追加のみだった金融サービス向けインタレストグループの憲章ページの本文が取得データに反映された（詳細はハイライト1参照）。
<!-- light:new-pages:end -->

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
（今回の対象期間に大幅更新されたページはありません）
<!-- light:updated-pages:end -->

## 軽微な更新

<!-- light:minor-updates:start -->
（今回の対象期間に軽微な更新はありません）
<!-- light:minor-updates:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-06-25.md](./archives/latest/2026-06-25.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-06-25.md](./archives/latest-detail/2026-06-25.md)

<!--
base_commit: 5c948aaefc1e28588e1f2e87aacec146ee8128ac
head_commit: f8479a4b550c9535b7213945696494c0dca75fc8
generated_at_full: 2026-06-27T15:18:41+09:00
-->
