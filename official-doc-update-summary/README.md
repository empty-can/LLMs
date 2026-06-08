# 公式ドキュメント更新サマリ

Claude Code 公式ドキュメントと Model Context Protocol（MCP）公式ドキュメントの**更新差分を、人間が読みやすい changelog／リリースノート風の Markdown** に要約して公開しています。日次の無人パイプラインで自動生成・更新されます。

各サイトについて、**ライト版**（ハイライト中心の概要）と**詳細版**（ページ単位の詳しい解説）の 2 ファイルを提供します。過去に公開したサマリは各サイトの `archives/latest/<作成日>.md`（ライト版）・`archives/latest-detail/<作成日>.md`（詳細版）に退避しています。

## 最新サマリ

### Claude Code 公式ドキュメント（claude-code-docs）

- [ライト版 `latest.md`](./claude-code-docs/latest.md) — 今回の更新ハイライトと概要
- [詳細版 `latest-detail.md`](./claude-code-docs/latest-detail.md) — 新規追加／大幅更新／軽微更新／新着情報をページ単位で詳述
- 過去サマリ: [ライト版 `archives/latest/`](./claude-code-docs/archives/latest/) ／ [詳細版 `archives/latest-detail/`](./claude-code-docs/archives/latest-detail/)（作成日名のファイル）

### MCP 公式ドキュメント（mcp）

- [ライト版 `latest.md`](./mcp/latest.md) — 今回の更新ハイライトと概要
- [詳細版 `latest-detail.md`](./mcp/latest-detail.md) — 新規追加／大幅更新／軽微更新／新着情報をページ単位で詳述
- 過去サマリ: [ライト版 `archives/latest/`](./mcp/archives/latest/) ／ [詳細版 `archives/latest-detail/`](./mcp/archives/latest-detail/)（作成日名のファイル）

> 各サマリの**対象期間・作成日**はファイル冒頭の frontmatter に記載しています（`latest.*` は常に最新回を指します）。

## 読み方

- **ライト版（`latest.md`）**: まずこちらで全体像をつかめます。更新ハイライトと概要を列挙し、本文中のリンクから詳細版の該当セクションへ直接ジャンプできます。
- **詳細版（`latest-detail.md`）**: 各変更をページ単位で詳述します。原文（公式 `llms.txt`）への参照リンク付きで、一次情報まで辿れます。
- **アーカイブ（`archives/latest/<作成日>.md`・`archives/latest-detail/<作成日>.md`）**: 過去に公開したサマリ。ライト版・詳細版を種別ごとのフォルダに作成日名のファイルとして退避します（日付フォルダを個別に開かずに種別ごとに一覧できます）。`latest.*` が新しい回に更新されるたび、旧版がここへ移ります。
