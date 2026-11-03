# official-llms-txts

各公式サイトからダウンロードした `llms.txt` / `llms-full.txt` 等を格納するフォルダ（入力）。日次の無人パイプラインが上流から定期取得して更新する。保存先は原則として取得元 URL のホスト名とパスに対応する。GitHub の raw ファイル（`raw.githubusercontent.com` から取得するもの）は、配信サーバのドメインではなく、そのファイルが属する公式サイトのフォルダに置く（例: `anthropics/claude-code` の `CHANGELOG.md` → `code.claude.com/docs/CHANGELOG.md`）。対応するサイトが無いものは `<owner>/<repo>/` のフォルダにリポジトリ内のパスのまま置く。

## llms.txt と llms-full.txt について

[llms.txt 仕様（llmstxt.org）](https://llmstxt.org/) に基づく。

- **`llms.txt`**: サイト名（H1）・概要（blockquote）・ページリスト（URL＋1行説明）で構成された軽量なインデックスファイル。コンテキスト消費を抑えたい場合や「どのページがあるか」を把握したいときに参照する（約 100〜150 行）。
- **`llms-full.txt`**: `llms.txt` にリストされた各 URL の全文を展開・結合した完全版。特定機能の詳細仕様・設定値・コード例を検索したいときに参照する（数万行になる場合あり）。

## サブフォルダ

| フォルダ | サイト | 内容 |
|---|---|---|
| `code.claude.com/docs/` | Claude Code 公式ドキュメント | Claude Code の設定・機能・SDK・hooks・skills・MCP 連携等。GitHub `anthropics/claude-code` の `CHANGELOG.md` と、その Atom フィード `feed.xml` もここに置く |
| `modelcontextprotocol.io/` | MCP 公式ドキュメント | Model Context Protocol の仕様・クライアント/サーバー実装・認証等 |
| `claude.com/docs/` | Claude.ai 公式ドキュメント | コネクタ・skills・plugins、Slack／デスクトップ／Microsoft 365 での利用等（`llms.txt` / `llms-full.txt`） |
| `claude.com/` | claude.com | サイト全体の `sitemap.xml` |
| `platform.claude.com/` | Anthropic 開発者ドキュメント | Claude API・SDK・Claude Developer Platform（`llms.txt` のみ。`llms-full.txt` は約 49 MB あるため取り込んでいない） |
| `agentskills.io/` | Agent Skills | Agent Skills 形式の仕様・クライアント一覧・作成手順（`llms.txt` / `llms-full.txt`） |
| `anthropics/claude-plugins-official/` | GitHub `anthropics/claude-plugins-official` | 公式プラグイン Marketplace の `.claude-plugin/marketplace.json` |
| `anthropics/skills/` | GitHub `anthropics/skills` | Anthropic のサンプル skills Marketplace の `.claude-plugin/marketplace.json` |

## llms.txt 以外のファイル

### `code.claude.com/docs/en/claude_code_docs_map.md`

Claude Code 全ドキュメントページの見出し構造を階層的にまとめたマップファイル（上流の GitHub Actions で自動生成、最終更新日時がファイル内に記載）。`llms.txt` の各リンクに対応するページの **内部見出し構成** を事前に把握できるため、`llms-full.txt` から目当てのセクションを探す前の絞り込みに有効。

セクション構成: Getting started / Core concepts / Use Claude Code / Platforms and integrations / Agents and parallel work / Tools and plugins / Automation / Troubleshooting / Setup and access / Deployment 他。

### `code.claude.com/docs/en/changelog.md`

Claude Code のリリースノートページ（`https://code.claude.com/docs/en/changelog.md`）。同じページは `llms-full.txt` にも収録されている（`# Claude Code changelog` の節）。GitHub 側の原本は同じフォルダの `../CHANGELOG.md`（`code.claude.com/docs/CHANGELOG.md`）。

### `code.claude.com/docs/ja/`

日本語ページのローカルミラー（2026-06-12 時点で固定。翻訳ラグ検証用で、定期取得の対象ではない）。

### `claude.com/sitemap.xml`・`code.claude.com/docs/feed.xml`・`anthropics/*/.claude-plugin/marketplace.json`

ドキュメント本文ではなく、ページ一覧（sitemap）・リリース通知（Atom フィード）・Marketplace のプラグイン一覧（JSON）。新しいページ・リリース・プラグインの出現を差分で追うために取り込んでいる。

> 更新サマリ（下記）の入力は `code.claude.com/docs/` の `llms.txt` / `llms-full.txt` / `en/claude_code_docs_map.md` と `modelcontextprotocol.io/` の `llms.txt` / `llms-full.txt` だけ。それ以外のファイルは日次で取り込んで履歴に残すのみで、要約には使っていない。

## 更新サマリ

これらの差分を人間向け changelog にまとめたものが `../official-doc-update-summary/`（claude-code-docs / mcp）にある。
