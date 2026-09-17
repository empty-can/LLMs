---
対象期間: 2026年09月15日 〜 2026年09月16日
作成日: 2026-09-16
---

# MCP 公式ドキュメント更新サマリ

```markdown
今回の対象期間の差分は本文 `llms-full.txt` の 1 ページ・14 行（追加 7 行・削除 7 行）のみで、索引 `llms.txt` は 1 行も変わっていません。内容は SEP-2640「Skills Extension」ページが引用する外部リンクのパス書き換えだけで、仕様本文の記述・プロトコル定義・クライアント対応に関わる変更はありません。

主要なものを以下に挙げます。

1. SEP-2640 が引用する Working Group 資料 5 文書（problem-statement / experimental-findings / related-work / open-questions / skill-meta-keys）のリンク先が、`ext-skills` リポジトリの `docs/` 直下から `docs/archive/` 配下へ変わった。書き換えは同ページ内の 7 箇所で、`rationale.md`・`decisions.md` を指す残り 3 リンクは従来パスのまま
```

## ハイライト

1. [**SEP-2640 が参照する Working Group 資料 5 件のリンク先が docs 直下から archive 配下へ移動**](./latest-detail.md#1-sep-2640-が参照する-working-group-資料-5-件のリンク先が-docs-直下から-archive-配下へ移動):  
  `SEP-2640: Skills Extension` ページの Motivation・Backward Compatibility・Security Implications・References の 4 セクションで、`modelcontextprotocol/ext-skills` リポジトリの資料を指す 7 本のリンクが `docs/<file>.md` から `docs/archive/<file>.md` へ書き換えられた。変更はパス文字列の挿入のみで、リンクテキスト・説明文・アンカーはいずれも変わっていない（増加バイト数 56 = `archive/` 8 バイト × 7 とも整合する）。同ページに残る `rationale.md`（2 本）・`decisions.md`（1 本）へのリンクは書き換えられておらず、ページ内の ext-skills 資料リンク 10 本のうち 7 本だけが移動先を指す状態になっている。

## 新規追加されたページ

今回本文に新たに収録されたページはありません。`llms-full.txt` の収録ページ数は 150 件で前回から増減がなく、索引 `llms.txt` のエントリ数も 352 件のまま変わっていません。

## 大幅に更新されたページ

今回の対象期間に大幅な更新（本文 50 行以上の変更）があった既存ページはありません。差分があったのは `SEP-2640: Skills Extension` の 1 ページのみで、変更量は追加 7 行・削除 7 行です（詳細はハイライト 1 参照）。

## 軽微な更新

今回差分が出たファイルは本文 `llms-full.txt` の 1 件、ページは `SEP-2640: Skills Extension` の 1 件のみです。内容は同ページが引用する外部資料のパス変更 5 文書ぶんで、いずれも `modelcontextprotocol/ext-skills` リポジトリの `docs/` 直下から `docs/archive/` 配下への書き換えです（詳細はハイライト 1 参照。以下は文書単位の内訳です）。新機能・機能改善・バグ修正に該当する変更はありません。

**その他**

- Motivation の「Fragmented distribution」が参照する問題提起文書のリンク先が `docs/problem-statement.md` から `docs/archive/problem-statement.md` へ変更 — [SEP-2640: Skills Extension](https://modelcontextprotocol.io/seps/2640-skills-extension#motivation)
- Motivation の「Instruction size limits」と References が参照する実験結果文書のリンク先が `docs/experimental-findings.md` から `docs/archive/experimental-findings.md` へ変更（2 箇所。Motivation 側はアンカー `#mcpgraph-skills-in-mcp-server-repo` 付きのまま） — [SEP-2640: Skills Extension](https://modelcontextprotocol.io/seps/2640-skills-extension#motivation)
- Backward Compatibility と References が参照する既存実装調査（related-work survey）のリンク先が `docs/related-work.md` から `docs/archive/related-work.md` へ変更（2 箇所） — [SEP-2640: Skills Extension](https://modelcontextprotocol.io/seps/2640-skills-extension#backward-compatibility)
- Security Implications がプロンプトインジェクションの背景として参照する未解決論点文書のリンク先が `docs/open-questions.md` から `docs/archive/open-questions.md` へ変更（アンカー `#10-how-should-skills-handle-security-and-trust-boundaries` 付きのまま） — [SEP-2640: Skills Extension](https://modelcontextprotocol.io/seps/2640-skills-extension#security-implications)
- References が参照する skill `_meta` キー規約文書のリンク先が `docs/skill-meta-keys.md` から `docs/archive/skill-meta-keys.md` へ変更 — [SEP-2640: Skills Extension](https://modelcontextprotocol.io/seps/2640-skills-extension#references)

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-09-15.md](./archives/latest/2026-09-15.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-09-15.md](./archives/latest-detail/2026-09-15.md)

<!--
base_commit: ebe595356470a094a294bd32d86870726c81d33b
head_commit: fa697d25e355bcd2486c2c9abb1263f94646b401
generated_at_full: 2026-09-17T15:28:35+09:00
-->
