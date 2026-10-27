---
対象期間: 2026年10月23日 〜 2026年10月26日
作成日: 2026-10-26
---

# MCP 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
今回の対象期間の差分は本文 `llms-full.txt` の追加 7 行・削除 1 行だけで、索引 `llms.txt` には変更がありません。変更のあったページは File Uploads Charter と Working and Interest Groups の 2 件で、どちらもコミュニティの運営に関する文書です。

主要なものを以下に挙げます。

1. File Uploads WG の憲章で、JSON-RPC のメッセージに収まらないほど大きいファイルや、取得に認可が要るファイルをツールが返す方法が、副次的なスコープとして加わった。Out of Scope は小さなファイルの配送だけに狭まった
2. Working and Interest Groups のページで、すべての WG・IG の会議が満たすべき要件に、自動の記録は Google Meet の公式の文字起こしだけとし、サードパーティの AI ノートテイカーや会議ボットは認めないという項目が加わった
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**File Uploads WG の憲章にファイルのダウンロードが副次的なスコープとして加わった**](#1-file-uploads-wg-の憲章にファイルのダウンロードが副次的なスコープとして加わった):  
  File Uploads WG の憲章の Mission Statement と In Scope に、JSON-RPC のメッセージに収まらないほど大きいファイルや、取得に認可が要るファイルを、ツールがどう返すかを扱う副次的な目標が加わった。アップロードの作業が優先される。Out of Scope は、サーバーからクライアントへのファイルの配送全般から、小さなファイルの配送だけに狭まった。
2. [**WG と IG の会議の自動記録が Google Meet の公式文字起こしに限られた**](#2-wg-と-ig-の会議の自動記録が-google-meet-の公式文字起こしに限られた):  
  Working and Interest Groups の Meeting Requirements で、すべての会議が満たすべき要件が 4 項目から 5 項目になった。加わったのは、Google Meet の公式の文字起こしを会議の唯一の自動の記録とし、サードパーティの AI ノートテイカーや会議ボットは Code of Conduct に従い認めない、という項目。
<!-- light:highlight-list:end -->

## 1. File Uploads WG の憲章にファイルのダウンロードが副次的なスコープとして加わった

今回の差分は本文 `llms-full.txt` だけで、追加 7 行・削除 1 行という内訳です。索引 `llms.txt` には 1 行の変更もなく、`llms-full.txt` の総行数は 45,127 行から 45,133 行になりました。収録ページ数は 157 件（`examples` が 2 回収録されているため、URL としては 156 件）のままです。対象期間中には取り込みが 3 回ありましたが、MCP 側の入力が変わったのは最後の 1 回だけです。変更のうち追加 6 行・削除 1 行が、File Uploads Charter のものです。

**スコープにファイルのダウンロードが加わりました。** File Uploads WG は、ツールや elicitation のリクエストがファイルの入力を宣言し、ホストがネイティブのファイルピッカーを表示して、ユーザーが選んだファイルの内容をサーバーに渡せるようにする仕組みを定める WG です（SEP-2356 を軸にしています）。今回、Mission Statement の末尾に、副次的な目標として「JSON-RPC のメッセージには大きすぎるファイルや、取得に認可が要るファイルを、ツールがどう返すか」を扱うという 1 文が加わりました。In Scope にも同じ内容の項目「File Downloads (secondary)」が Specification Work と Reference Implementations の間に入り、アップロードの作業が優先される（Upload work takes priority）と明記されています。

**Out of Scope は小さなファイルの配送に絞られました。** これまでの Out of Scope の項目は「サーバーからクライアントへのファイルの配送。Resources と `BlobResourceContents` で既に扱われている」で、サーバーからクライアントへの方向は丸ごと対象外でした。今回これが「サーバーからクライアントへの小さなファイルの配送。Resources と `BlobResourceContents` が既に扱っている」に書き換わり、対象外は小さなファイルに限られました。In Scope に入った副次的な項目と対になる書き換えです。transport の層やセッションのモデルの変更が対象外であることは変わっていません。

**変わっていない部分もあります。** Leadership（Lead は Den Delimarsky）・Membership・Active Work Items・Success Criteria は変わっておらず、Active Work Items にダウンロードに関する項目は加わっていません。Out of Scope の後ろにある、streaming・chunked transfer・presigned upload URL などの方式を設計の中で検討してよいとする段落も、以前からあるものです。憲章の Changelog には、2026年10月21日 付で「Add file downloads to scope as a secondary item」の行が加わりました。ただし `llms-full.txt` にこの変更が現れたのは対象期間中の 3 回の取り込みのうち最後の 1 回で、前回サマリの時点（head `5536db3`）の `llms-full.txt` にはまだ含まれていませんでした。

- [File Uploads Charter - MCP Docs](https://modelcontextprotocol.io/community/working-groups/file-uploads#in-scope)

## 2. WG と IG の会議の自動記録が Google Meet の公式文字起こしに限られた

残る 1 行の追加は、Working and Interest Groups のページの Governance 配下にある Meeting Requirements の節です。このページは、MCP の Working Group（WG）と Interest Group（IG）に共通する運営のルールを定めたものです。Meeting Requirements の節では、会議の頻度・形式・時間は Lead がグループの状況に応じて決めるとしたうえで、形式や頻度にかかわらずすべての会議が満たすべき要件を箇条書きで挙げています。

これまでの要件は次の 4 項目でした。コミュニティの参加者全員に開かれていること（非公開の会議や組織内部の会議にしない）、少なくとも 7 日前に meet.modelcontextprotocol.io で公開すること、議題を公開し GitHub Discussions の Meeting Notes カテゴリに Discussion として載せること、48 時間以内に同じ Discussion にメモを公開すること、です。今回、5 項目目として「Google Meet の公式の文字起こしを、会議の唯一の自動の記録として使う。サードパーティの AI ノートテイカーや会議ボットは、Code of Conduct（`CODE_OF_CONDUCT.md` の `#community-meetings` の節）に従い認めない」が加わりました。

同じ Meeting Requirements の一覧は、SEP-2149（MCP Group Governance and Charter Template）の「1.6 Meeting Requirements」にもありますが、こちらは 4 項目のまま据え置かれています。SEP-2149 は Final の状態で、採択時点の設計を記録として残すものと冒頭に注記されています。

- [Working and Interest Groups - MCP Docs](https://modelcontextprotocol.io/community/working-interest-groups#meeting-requirements)

## 新規追加されたページ

<!-- light:new-pages:start -->
今回の対象期間に新たに追加されたページはありません。索引 `llms.txt` に変更はなく、索引側のエントリ数（362 件）と本文 `llms-full.txt` の収録ページ数（157 件）はどちらも前回と同じです。
<!-- light:new-pages:end -->

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
今回の対象期間に大幅な更新（本文 50 行以上の変更）があったページはありません。差分が出た 2 ページで大きいほうは File Uploads Charter の追加 6 行・削除 1 行で、いずれも「軽微な更新」で扱います。
<!-- light:updated-pages:end -->

## 軽微な更新

<!-- light:minor-updates:start -->
今回差分が出たファイルは `llms-full.txt` の 1 件のみで、変更のあったページは次の 2 件です。

**機能改善**

- File Uploads Charter の Mission Statement と In Scope に、大きなファイルや取得に認可が要るファイルをツールが返す方法を副次的な項目として追加し、Out of Scope を小さなファイルの配送に限定（詳細はハイライト 1 参照） — [File Uploads Charter](https://modelcontextprotocol.io/community/working-groups/file-uploads#in-scope)

**その他**

- Working and Interest Groups の Meeting Requirements に、Google Meet の公式の文字起こしを唯一の自動の記録とし、サードパーティの AI ノートテイカーや会議ボットを認めない要件を追加（詳細はハイライト 2 参照） — [Working and Interest Groups](https://modelcontextprotocol.io/community/working-interest-groups#meeting-requirements)
<!-- light:minor-updates:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-10-23.md](./archives/latest/2026-10-23.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-10-23.md](./archives/latest-detail/2026-10-23.md)

<!--
base_commit: 5536db396725852afccd11c0a05e205b631b83fa
head_commit: f43c40d31d95ea8ce1ef817f41d68a409f4e53f6
generated_at_full: 2026-10-27T15:24:21+09:00
-->
