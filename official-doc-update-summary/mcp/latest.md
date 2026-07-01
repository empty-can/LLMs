---
対象期間: 2026年06月26日 〜 2026年06月30日
作成日: 2026-06-30
---

# MCP 公式ドキュメント更新サマリ

```markdown
今回の対象期間の原文差分は、大半が複数の SEP ページにおける TypeScript union 型定義の記法整形（複数行→単一行）で、実体的な変更は Streamable HTTP トランスポートのヘッダ標準化を定める SEP-2243 に対する 2 件の規範的な精緻化のみでした。

主要なものを以下に挙げます。

1. SEP-2243 で、クライアントは `Mcp-Param-*` ヘッダを「最も新しく取得した `inputSchema`」で構築することが MUST として明文化され、サーバーの再送要求条件に「本文と一致しない場合」が追加された
2. SEP-2243 の適合テストで、Base64 値ラッパーのプレフィックスは小文字 `base64` のみ有効となり、大文字 `BASE64` はリテラル値として扱う（デコードしない）ことに変更された
```

## ハイライト

1. [**Mcp-Param ヘッダの構築規則を厳格化**](./latest-detail.md#1-mcp-param-ヘッダの構築規則を厳格化):  
  クライアントは最新の `inputSchema` を用いて `Mcp-Param-*` ヘッダを構築することが MUST 化され、サーバー拒否のトリガーに「必須ヘッダの欠落」に加え「本文との不一致」が明記された。
2. [**Base64 プレフィックスの大小文字扱いを厳格化**](./latest-detail.md#2-base64-プレフィックスの大小文字扱いを厳格化):  
  値の Base64 ラッパー `=?base64?...?=` のプレフィックスは小文字のみ有効となり、`=?BASE64?...?=` のような大文字プレフィックスはリテラル値として扱われる（従来は大小文字非依存で受理）よう適合テストが更新された。

## 新規追加されたページ

（今回の対象期間に新規追加されたページはありません）

## 大幅に更新されたページ

（今回の対象期間に大幅更新されたページはありません）

## 軽微な更新

**その他**

- 複数の SEP ページで、コード例中の TypeScript union 型定義の記法が複数行表記（各メンバーを先頭 `|` で列挙）から単一行へ整形されました（意味上の変更はありません）。対象は [SEP-1330](https://modelcontextprotocol.io/seps/1330-elicitation-enum-schema-improvements-and-standards) / [SEP-1577](https://modelcontextprotocol.io/seps/1577--sampling-with-tools) / [SEP-2322](https://modelcontextprotocol.io/seps/2322-MRTR) / [SEP-2663](https://modelcontextprotocol.io/seps/2663-tasks-extension) です。

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-06-26.md](./archives/latest/2026-06-26.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-06-26.md](./archives/latest-detail/2026-06-26.md)

<!--
base_commit: f8479a4b550c9535b7213945696494c0dca75fc8
head_commit: 270e6fa0b7efe4f16ebdd47a4e8f6edbcfc9f585
generated_at_full: 2026-07-01T15:03:32+09:00
-->
