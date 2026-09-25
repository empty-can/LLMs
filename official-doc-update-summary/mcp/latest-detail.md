---
対象期間: 2026年09月23日 〜 2026年09月24日
作成日: 2026-09-24
---

# MCP 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
今回の対象期間の変更は 1 ページのみで、前回索引 `llms.txt` にだけ載っていた Scientific Computing Interest Group の憲章の本文が `llms-full.txt` に収録されました（追加 91 行・削除なし）。索引 `llms.txt` に変更はありません。

主要なものを以下に挙げます。

1. Scientific Computing Interest Group の憲章本文が収録され、科学・工学ワークフローでの MCP のユースケースを集めるというミッションと体制が明らかになった
2. 同憲章のスコープとして、物理量・単位・不確かさ、再現性と来歴、大規模配列・データセット、長時間計算、既存科学標準との相互運用などが示された
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**Scientific Computing Interest Group の憲章本文が収録**](#1-scientific-computing-interest-group-の憲章本文が収録):  
  前回は索引に 1 行加わっただけだった憲章ページの本文が `llms-full.txt` に入った。科学・工学ワークフローにおける MCP のユースケースを研究・産業の実務者から集め、拡張開発やプロトコル改善が必要なギャップを見極める Interest Group で、ファシリテーターは Cory Kinney 氏、会合の頻度・時間は未定（TBD）。
2. [**スコープは物理量・再現性・大規模データ・長時間計算・標準相互運用**](#2-スコープは物理量再現性大規模データ長時間計算標準相互運用):  
  対象範囲（In Scope）として、単位や不確かさを伴う物理量の表現、計算結果の再現性と来歴、コンテキストに収まらない配列・データセットの受け渡し、シミュレーションや HPC ジョブといった長時間計算と MCP の tasks との対応付け、既存の科学標準との相互運用、分野横断での要件収集の 6 項目が挙げられた。
<!-- light:highlight-list:end -->

## 1. Scientific Computing Interest Group の憲章本文が収録

前回の対象期間には、索引 `llms.txt` に `community/interest-groups/scientific-computing` のエントリが 1 行加わっただけで、本文は `llms-full.txt` に未収録でした。今回、その本文「Scientific Computing Charter」が Primitive Grouping Charter と Security Charter の間に 91 行（削除なし）で収録され、憲章の中身を確認できるようになりました。

グループ種別は **Interest Group** です。ミッションは、科学・工学ワークフローにおける MCP のユースケースを探ることとされています。研究や産業の実務者からユースケースを集め、拡張の開発やプロトコル改善が必要となるギャップを把握し、それが Working Group の結成につながる可能性もあると述べています。

体制面では、ファシリテーターが Cory Kinney 氏（[@corykinney](https://github.com/corykinney)、任期は Initial）です。会合は「Working Session」（ユースケースの共有と技術的議論）で、頻度・時間はいずれも TBD となっています。参加は誰でも可能で、MCP Contributors Discord の `#scientific-computing-ig` チャンネルが窓口です。Changelog には 2026年08月24日付の「Initial charter」が記録されています。

- [Scientific Computing Charter - MCP Docs](https://modelcontextprotocol.io/community/interest-groups/scientific-computing#mission-statement)
- [Scientific Computing Charter - MCP Docs](https://modelcontextprotocol.io/community/interest-groups/scientific-computing#leadership)

## 2. スコープは物理量・再現性・大規模データ・長時間計算・標準相互運用

**対象範囲（In Scope）** は次の 6 項目です。

- **物理量・単位・不確かさ**: 単位や次元情報、ツール入出力の不確かさ、量の種類を伴う物理量を表現し、エージェントやクライアントが物理的制約を守らせるガードレールを設けられるようにする
- **再現性と来歴**: MCP 経由で得た計算結果を再現するのに必要なパラメータ、ソフトウェアやソルバーのバージョンなどの入力を記録する
- **配列・数値データセット**: 配列、テンソル、表形式データ、モデルのコンテキストに収まらない大きなデータセットの受け渡しと、そのペイロードをどう参照してツールに渡すか
- **長時間計算**: シミュレーション、ソルバー実行、バッチや HPC のジョブ投入を、非同期実行・進捗・キャンセルを担う MCP の tasks アーキテクチャにどう対応付けるか
- **既存科学標準との相互運用**: 確立された分野のフォーマット・語彙・オントロジーを作り直さず、MCP がそれらとどう関わるべきか
- **分野横断のユースケース把握**: 物理学、化学、生物学、地球・気候科学、天文学、工学から要件を集め、繰り返し現れる要件を特定する

**対象外（Out of Scope）** は、科学データのフォーマットや語彙そのものの策定（既存の標準化団体・コミュニティが担うため、本グループは相互運用の方法を議論するにとどめる）、特定ソフトウェアやデータセット向けの個別 MCP サーバーの構築・保守（ユースケース収集の材料にはなるがプロトコル作業ではない）、認可・ID の仕組み（Authorization IG の担当）の 3 点です。

**関連グループ**としては、長時間シミュレーションやジョブ投入の土台となる Tasks を扱う Agents WG、クライアント・サーバー間での正しさの検証や単位の正規化の実装手段となりうる Interceptors WG、入力データセットやメッシュ・形状ファイルなど大きなファイルを扱う File Uploads WG、大規模で階層的なツール群の整理に関わる Primitive Grouping IG、共有科学ソフトウェアやデータセット向けサーバーの公開・発見に関わる Registry WG が挙げられています。初期議題（Discussion Topics）は、ツールスキーマでの単位・次元・意味を扱う Quantities 拡張、計算結果の来歴とバージョン管理メタデータ、既存の科学フォーマット・語彙との相互運用の 3 件で、いずれも Open（担当者未定）です。

- [Scientific Computing Charter - MCP Docs](https://modelcontextprotocol.io/community/interest-groups/scientific-computing#scope)
- [Scientific Computing Charter - MCP Docs](https://modelcontextprotocol.io/community/interest-groups/scientific-computing#discussion-topics)

## 新規追加されたページ

<!-- light:new-pages:start -->
- [**Scientific Computing Charter**](#1-scientific-computing-charter) ([MCP Docs](https://modelcontextprotocol.io/community/interest-groups/scientific-computing)):  
  MCP Scientific Computing Interest Group の憲章。前回は索引への追加のみだったが、今回 `llms-full.txt` に本文が収録された（詳細はハイライト 1・2 参照）。
<!-- light:new-pages:end -->

## 1. Scientific Computing Charter

`llms-full.txt` にとっては新規のページで、差分は 91 行の追加のみです。構成は Group Type・Mission Statement・Scope（In Scope / Out of Scope / Related Groups）・Leadership・Operations・Discussion Topics・Changelog の各節から成ります。索引 `llms.txt` のエントリは前回の対象期間に追加済みのため、今回の索引側の変更はありません。

内容の詳細はハイライト 1（ミッションと体制）とハイライト 2（スコープ・関連グループ・初期議題）を参照してください。

- [Scientific Computing Charter - MCP Docs](https://modelcontextprotocol.io/community/interest-groups/scientific-computing)

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
今回の対象期間に大幅な更新（本文 50 行以上の変更）があった既存ページはありません。
<!-- light:updated-pages:end -->

## 軽微な更新

<!-- light:minor-updates:start -->
今回の対象期間に軽微な更新はありません。
<!-- light:minor-updates:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-09-23_1500.md](./archives/latest/2026-09-23_1500.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-09-23_1500.md](./archives/latest-detail/2026-09-23_1500.md)

<!--
base_commit: 1cd5f92f259ae91504d3746edb8d0a386ce71bdd
head_commit: 9e4a9ca8dd012676f943d04b4ad641296ec601bb
generated_at_full: 2026-09-25T15:51:02+09:00
-->
