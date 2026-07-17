---
対象期間: 2026年07月12日 〜 2026年07月16日
作成日: 2026-07-16
---

# MCP 公式ドキュメント更新サマリ

```markdown
今回の対象期間の原文差分は、SEP-2549「TTL for List Results」仕様ページ 1 ページのみで、いずれもリスト結果キャッシュ用フィールド（`ttlMs` / `cacheScope`）の仕様本文に対する軽微な文書修正でした。プロトコルの型・挙動・SDK 要件に実体的な変更はなく、今回取り上げるべきハイライトはありません。
```

## ハイライト

（今回の対象期間に取り上げるべきハイライトはありません）

## 新規追加されたページ

（今回の対象期間に新規追加されたページはありません）

## 大幅に更新されたページ

（今回の対象期間に大幅更新されたページはありません）

## 軽微な更新

今回の対象期間に更新されたのは SEP-2549「TTL for List Results」の 1 ページで、いずれも仕様本文の文言に関する軽微な修正です。

**機能改善**

- 「Error handling」節に、後方互換に関する記述が追記されました。`ttlMs` フィールドが欠落している場合、クライアントは既定の `ttlMs` を 0（即時に陳腐化とみなす）と仮定し、独自のキャッシュ判断やサーバー通知に依拠すべき（SHOULD）、という内容です。従来この記述は末尾の「Backward Compatibility」節にのみ書かれていましたが、`ttlMs` 欠落時の挙動を扱う「Error handling」節にも明示され、負値が指定された場合の既存記述と並べて参照できるようになりました。 — [SEP-2549: TTL for List Results](https://modelcontextprotocol.io/seps/2549-TTL-for-list-results#error-handling)

**その他**

- 「Backward Compatibility」節で、`ttlMs` 欠落時の挙動を述べる記述にあった綴り誤り「heuristincs」が「heuristics」に修正されました。記述の意味に変更はありません。 — [SEP-2549: TTL for List Results](https://modelcontextprotocol.io/seps/2549-TTL-for-list-results#backward-compatibility)

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-07-12.md](./archives/latest/2026-07-12.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-07-12.md](./archives/latest-detail/2026-07-12.md)

<!--
base_commit: ad04427077fcdb5fbb719e1ab9462aa953c5ca81
head_commit: 5cf373da86d5703c50540e7e49df4d79e33d4c76
generated_at_full: 2026-07-17T15:21:54+09:00
-->
