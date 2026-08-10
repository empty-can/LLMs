---
対象期間: 2026年08月08日 〜 2026年08月09日
作成日: 2026-08-09
---

# Claude Code 公式ドキュメント更新サマリ

```markdown
今回の対象期間は changelog への追加がなく、検出された変更はプロンプト提案（プロンプト入力にグレー表示される予測）の制御手段に関する 1 件のみでした。これまで環境変数と /config のトグルだけだった無効化手段に設定ファイルのキーが加わり、管理設定と組み合わせて組織単位でオフにする手順も示されています。

主要なものを以下に挙げます。

1. プロンプト提案を設定ファイルから制御する promptSuggestionEnabled 設定が追加され、管理設定と併用することで組織全体でオフにできるようになった
```

## ハイライト

1. [**プロンプト提案を設定ファイルで制御する promptSuggestionEnabled 設定が追加された**](./latest-detail.md#1-プロンプト提案を設定ファイルで制御する-promptsuggestionenabled-設定が追加された):  
  設定一覧に `promptSuggestionEnabled`（既定 `true`）が追加され、プロンプト提案を `settings.json` から無効化できるようになった。環境変数 `CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION` は両方が設定されている場合にこの設定より優先される。組織全体でオフにする場合は、管理設定で本設定を `false` にしたうえで、管理設定の `env` キーでも環境変数を `false` にする手順が案内されている。

## 新規追加されたページ

（今回の対象期間に新規追加されたページはありません）

## 大幅に更新されたページ

（今回の対象期間に大幅更新されたページはありません）

## 軽微な更新

今回の対象期間は changelog への追加がなく、検出された変更は `promptSuggestionEnabled` 設定の追加に伴う通常ドキュメントページ 3 件のみです。なお 3 ページとも日本語版がまだこの変更を反映していないため、参考リンクは英語版のみを記載しています。

**新機能**

- 設定一覧に `promptSuggestionEnabled`（既定 `true`）が追加され、プロンプト提案を設定ファイルから無効化できるようになりました（詳細はハイライト 1 参照）— [English](https://code.claude.com/docs/en/settings#available-settings)

**機能改善**

- 「インタラクティブモード」ページのプロンプト提案の説明で、無効化手段が `/config` のトグル・設定ファイル・環境変数の 3 通りの箇条書きに整理され、組織全体でオフにするための管理設定の手順が追記されました（詳細はハイライト 1 参照）— [English](https://code.claude.com/docs/en/interactive-mode#prompt-suggestions)
- 環境変数 `CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION` の説明に、`promptSuggestionEnabled` 設定より優先される旨が追記されました。あわせて、プロンプト提案の説明から「Claude が応答したあとに」という限定が削除され、表示タイミングを限定しない記述になりました — [English](https://code.claude.com/docs/en/env-vars#variables)

## 新着情報

（今回の対象期間に新着情報ページの更新はありません）

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-08-08.md](./archives/latest/2026-08-08.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-08-08.md](./archives/latest-detail/2026-08-08.md)

<!--
base_commit: eefcc456a1f2c7dde2c95b399767a78ffc5e4bc9
head_commit: 66dc30f0152ca283a401532f5a6a6d3caa6b2f7f
generated_at_full: 2026-08-10T15:04:41+09:00
-->
