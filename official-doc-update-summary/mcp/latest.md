---
対象期間: 2026年09月02日 〜 2026年09月08日
作成日: 2026-09-08
---

# MCP 公式ドキュメント更新サマリ

```markdown
今回の対象期間の差分は、新設された Working Group の charter ページ 1 件の追加に尽きます。索引 `llms.txt` に 1 行、本文を収める `llms-full.txt` に 119 行が加わり、削除行は 0 行です。既存ページの記述には 1 行の変更もありません。

主要なものを以下に挙げます。

1. Resources を読み取り専用から双方向へ広げることを掲げた Filesystems Working Group の charter が追加された。create / update / delete と、本文を取得せずに存在・サイズ・最終更新を返すメタデータ読み取り `stat` を Extensions Track の SEP 1 本にまとめる方針で、楽観的並行性制御と、書き込みが `notifications/resources/updated`・`ttlMs`・`cacheScope`・`lastModified` とどう噛み合うかまでを射程に含む
```

## ハイライト

1. [**Resources を双方向化する Filesystems Working Group の charter が追加**](./latest-detail.md#1-resources-を双方向化する-filesystems-working-group-の-charter-が追加):  
  MCP Resources を読み取り専用から書き込み可能へ広げることを狙う新 Working Group の charter が収録された。エージェントが入力を読んだのと同じサーバーへ結果を書き戻せるようにするのが目的で、成果物は Extensions Track の SEP 1 本。Resources と並ぶ `files/*` プリミティブを別に立てる案（SEP-1708 が提案し 2026年01月23日 にクローズ済み）は明確に対象外とされ、あくまで Resources の拡張として進む。今回の差分はこのページの追加だけで、索引のエントリは 349 件から 350 件になった。

## 新規追加されたページ

今回索引に増えたページは次の 1 件です。

- [**Filesystems Charter**](./latest-detail.md#1-filesystems-charter) ([MCP Docs](https://modelcontextprotocol.io/community/working-groups/filesystems)):  
  MCP Filesystems Working Group の charter ページ。Resources への書き込み操作（create / update / delete / `stat`）と楽観的並行性制御、変更通知・キャッシュとの噛み合わせを 1 本の Extensions Track SEP にまとめることを目標に掲げる。索引・本文とも今回の差分で同時に追加された。

## 大幅に更新されたページ

今回の対象期間に大幅な更新（本文 50 行以上の変更）があった既存ページはありません。`llms-full.txt` の差分 119 行はすべて新規ページ 1 件の追加によるもので、既存ページの本文には追加・削除とも 1 行もありません。

## 軽微な更新

今回差分が出たファイルは索引 `llms.txt` と本文 `llms-full.txt` の 2 件ですが、その内容はいずれも新規ページ 1 件の追加（新規追加されたページ 1 参照）に尽きます。既存エントリの書き換え・リンク先の変更・字句修正はなく、これとは別に挙げる軽微な更新はありません。

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-09-02.md](./archives/latest/2026-09-02.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-09-02.md](./archives/latest-detail/2026-09-02.md)

<!--
base_commit: 2667e8110b59c2cec8b85dd866ec8f529a5fa572
head_commit: b8993e0293f2b6b04fd7517ad897abdaa6e0f01b
generated_at_full: 2026-09-09T15:27:42+09:00
-->
