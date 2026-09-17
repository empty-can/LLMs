---
対象期間: 2026年09月15日 〜 2026年09月16日
作成日: 2026-09-16
---

# MCP 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
今回の対象期間の差分は本文 `llms-full.txt` の 1 ページ・14 行（追加 7 行・削除 7 行）のみで、索引 `llms.txt` は 1 行も変わっていません。内容は SEP-2640「Skills Extension」ページが引用する外部リンクのパス書き換えだけで、仕様本文の記述・プロトコル定義・クライアント対応に関わる変更はありません。

主要なものを以下に挙げます。

1. SEP-2640 が引用する Working Group 資料 5 文書（problem-statement / experimental-findings / related-work / open-questions / skill-meta-keys）のリンク先が、`ext-skills` リポジトリの `docs/` 直下から `docs/archive/` 配下へ変わった。書き換えは同ページ内の 7 箇所で、`rationale.md`・`decisions.md` を指す残り 3 リンクは従来パスのまま
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**SEP-2640 が参照する Working Group 資料 5 件のリンク先が docs 直下から archive 配下へ移動**](#1-sep-2640-が参照する-working-group-資料-5-件のリンク先が-docs-直下から-archive-配下へ移動):  
  `SEP-2640: Skills Extension` ページの Motivation・Backward Compatibility・Security Implications・References の 4 セクションで、`modelcontextprotocol/ext-skills` リポジトリの資料を指す 7 本のリンクが `docs/<file>.md` から `docs/archive/<file>.md` へ書き換えられた。変更はパス文字列の挿入のみで、リンクテキスト・説明文・アンカーはいずれも変わっていない（増加バイト数 56 = `archive/` 8 バイト × 7 とも整合する）。同ページに残る `rationale.md`（2 本）・`decisions.md`（1 本）へのリンクは書き換えられておらず、ページ内の ext-skills 資料リンク 10 本のうち 7 本だけが移動先を指す状態になっている。
<!-- light:highlight-list:end -->

## 1. SEP-2640 が参照する Working Group 資料 5 件のリンク先が docs 直下から archive 配下へ移動

今回の対象期間で差分が出たのは本文 `llms-full.txt` の 1 ファイル・1 ページのみで、変更量は追加 7 行・削除 7 行です。索引 `llms.txt` は 354 行・エントリ 352 件・ユニーク URL 347 件のまま 1 行も変わっていません。`llms-full.txt` も 43,589 行のままで行数の増減はなく、収録ページ数も 150 件で変わりません。差分が出た `SEP-2640: Skills Extension`（`seps/2640-skills-extension`）自体もページ全体で 673 行のままです。前回が WG の運営体制を 1 箇所書き換えただけの静かな断面でしたが、今回はそれに輪をかけて、参照先パスの機械的な置換だけという断面になりました。

書き換えられたのは、`modelcontextprotocol/ext-skills` リポジトリに置かれた Working Group の補助資料を指すリンクです。対象は **5 文書・計 7 リンク**で、内訳は次のとおりです。**Motivation** では「Fragmented distribution」の根拠として挙げられている `problem-statement.md` と、「Instruction size limits」で 875 行の mcpGraph skill の例に添えられている `experimental-findings.md`（アンカー `#mcpgraph-skills-in-mcp-server-repo` 付き）の 2 本。**Backward Compatibility** では、他の `skill://` URI 構造を採る既存実装のカタログとして参照されている related-work survey（`related-work.md`）の 1 本。**Security Implications** では、skill コンテンツがプロンプトインジェクション面であることの背景資料として置かれた `open-questions.md`（アンカー `#10-how-should-skills-handle-security-and-trust-boundaries` 付き）の 1 本。そして **References** の一覧で `experimental-findings.md`・`related-work.md`・`skill-meta-keys.md` の 3 本です。いずれも `docs/<file>.md` の部分が `docs/archive/<file>.md` に変わっただけで、リンクテキストも後続の説明文も変わっていません。

差分の 7 行を 1 行ずつ照合すると、変わっているのは各 URL の `docs/` と `<file>.md` の間に `archive/` が入った箇所だけで、同じ行のリンクテキストも前後の説明文も一致しています。アンカー（`#mcpgraph-...` / `#10-how-should-...`）もそのまま維持されています。ファイルサイズの変化もこれと整合しており、`llms-full.txt` は 2,487,785 バイトから 2,487,841 バイトへ **56 バイト**増えていて、`archive/` の 8 バイト × 7 箇所とちょうど一致します。

一方で、**同じページに残る ext-skills 資料へのリンク 3 本は書き換えられていません**。設計判断の根拠をまとめた `rationale.md` は Directory Listing の小節と Rationale セクションの計 2 箇所で、WG の決定ログ `decisions.md` は References で、いずれも `docs/` 直下のパスのままです。つまりページ内の ext-skills 資料リンク 10 本は、7 本が `docs/archive/` 配下・3 本が `docs/` 直下という混在状態になりました。また References に並ぶ各資料の説明文は今回いずれも書き換えられておらず、たとえば `Experimental Findings` は「results from implementations (WIP)」のまま、参照先パスだけが `archive/` 配下になっています。

実務上の影響としては、SEP-2640 の引用元として旧 URL（`docs/problem-statement.md` など）を控えている場合、その参照の更新が要る可能性がある点が挙げられます。ただし本サマリは公式ドキュメントの差分のみを根拠にしており、GitHub 側で実ファイルがどう配置されているか（旧パスが残っているか、リダイレクトがあるか）までは確認していません。仕様本体の記述 ―― `skills/list` / `skills/get` / `resources/directory/read` の 3 メソッドの定義、Security Implications の各 MUST 要件、Backward Compatibility が述べる互換性の扱い ―― は今回いずれも変わっていません。差分に現れた 7 行はすべて URL の一部だけが置き換わったもので、同じ行の説明文も含め、リンク以外の字句は一切動いていません。

- [SEP-2640: Skills Extension - MCP Docs](https://modelcontextprotocol.io/seps/2640-skills-extension#motivation)
- [SEP-2640: Skills Extension - MCP Docs](https://modelcontextprotocol.io/seps/2640-skills-extension#references)

## 新規追加されたページ

<!-- light:new-pages:start -->
今回本文に新たに収録されたページはありません。`llms-full.txt` の収録ページ数は 150 件で前回から増減がなく、索引 `llms.txt` のエントリ数も 352 件のまま変わっていません。
<!-- light:new-pages:end -->

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
今回の対象期間に大幅な更新（本文 50 行以上の変更）があった既存ページはありません。差分があったのは `SEP-2640: Skills Extension` の 1 ページのみで、変更量は追加 7 行・削除 7 行です（詳細はハイライト 1 参照）。
<!-- light:updated-pages:end -->

## 軽微な更新

<!-- light:minor-updates:start -->
今回差分が出たファイルは本文 `llms-full.txt` の 1 件、ページは `SEP-2640: Skills Extension` の 1 件のみです。内容は同ページが引用する外部資料のパス変更 5 文書ぶんで、いずれも `modelcontextprotocol/ext-skills` リポジトリの `docs/` 直下から `docs/archive/` 配下への書き換えです（詳細はハイライト 1 参照。以下は文書単位の内訳です）。新機能・機能改善・バグ修正に該当する変更はありません。

**その他**

- Motivation の「Fragmented distribution」が参照する問題提起文書のリンク先が `docs/problem-statement.md` から `docs/archive/problem-statement.md` へ変更 — [SEP-2640: Skills Extension](https://modelcontextprotocol.io/seps/2640-skills-extension#motivation)
- Motivation の「Instruction size limits」と References が参照する実験結果文書のリンク先が `docs/experimental-findings.md` から `docs/archive/experimental-findings.md` へ変更（2 箇所。Motivation 側はアンカー `#mcpgraph-skills-in-mcp-server-repo` 付きのまま） — [SEP-2640: Skills Extension](https://modelcontextprotocol.io/seps/2640-skills-extension#motivation)
- Backward Compatibility と References が参照する既存実装調査（related-work survey）のリンク先が `docs/related-work.md` から `docs/archive/related-work.md` へ変更（2 箇所） — [SEP-2640: Skills Extension](https://modelcontextprotocol.io/seps/2640-skills-extension#backward-compatibility)
- Security Implications がプロンプトインジェクションの背景として参照する未解決論点文書のリンク先が `docs/open-questions.md` から `docs/archive/open-questions.md` へ変更（アンカー `#10-how-should-skills-handle-security-and-trust-boundaries` 付きのまま） — [SEP-2640: Skills Extension](https://modelcontextprotocol.io/seps/2640-skills-extension#security-implications)
- References が参照する skill `_meta` キー規約文書のリンク先が `docs/skill-meta-keys.md` から `docs/archive/skill-meta-keys.md` へ変更 — [SEP-2640: Skills Extension](https://modelcontextprotocol.io/seps/2640-skills-extension#references)
<!-- light:minor-updates:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-09-15.md](./archives/latest/2026-09-15.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-09-15.md](./archives/latest-detail/2026-09-15.md)

<!--
base_commit: ebe595356470a094a294bd32d86870726c81d33b
head_commit: fa697d25e355bcd2486c2c9abb1263f94646b401
generated_at_full: 2026-09-17T15:28:35+09:00
-->
