# LLMs

Claude Code 周辺の公式ドキュメントを LLM／人間の双方が扱いやすい形で集約・公開するリポジトリ。

> **現状**: `cc-relative-info` リポジトリで構築・検証した「公式ドキュメント更新サマリ自動生成パイプライン」を、本リポジトリへ移設して正式運用する移行の途上です。下記の構成は移行完了後の目標形を示します（移行設計は `cc-relative-info` 側の `LLMs/work/publish-migration/` 参照）。

## 何を公開するか

1. **公式 `llms.txt` / `llms-full.txt` の取り込み**: Claude Code 公式ドキュメント（`code.claude.com`）と Model Context Protocol 公式（`modelcontextprotocol.io`）が公開する `llms.txt` / `llms-full.txt` を定期取得して保存する。
2. **更新サマリ（人間向け changelog）**: 上記の更新差分を、人間が読みやすい changelog／リリースノート風の Markdown として自動生成・蓄積する（詳細版＋ライト版の 2 ファイル方式）。

> **将来スコープ**: 任意リポジトリ向けに生成した `llms.txt`（現状 `cc-relative-info` の `gen-out`）と、それらに対する更新サマリも、将来は本リポジトリで公開する想定。命名の `official-*` は、将来の `generated-*` 系と併存させるための区別。

## 構成

```
LLMs/
├── official-llms-txts/            # 取り込んだ公式 llms.txt 等（入力）
│   ├── code.claude.com/docs/      # Claude Code 公式（llms.txt / llms-full.txt / docs map）
│   └── modelcontextprotocol.io/   # MCP 公式（llms.txt / llms-full.txt）
├── official-doc-update-summary/   # 生成した更新サマリ（出力）
│   ├── claude-code-docs/          # latest.md（ライト版）/ latest-detail.md（詳細版）/ archives/
│   └── mcp/                       # 同上
└── .claude/                       # 本リポジトリ内で自走するパイプライン一式（下記）
```

## どう更新されるか（自動運用）

日次でスケジュール実行される無人パイプラインが、取得 → サマリ生成 → 第三者レビュー → push までを自動で行います。

```
dl（公式 llms.txt 取得）
  → 更新サマリ生成（Claude による要約・翻訳）
  → 第三者レビュー（ハルシネーション／規約違反の機械検査・必須）
  → commit → bot ブランチへ push
  → 人手レビュー → main へマージ（＝公開）
```

- **ブランチ運用**: `main`（公開済みコンテンツ）/ `bot/doc-summary`（bot の未確定生成）。bot が `bot/doc-summary` へ push し、人手レビュー後に `main` へマージして公開する。
- パイプラインの実装・運用手順は `.claude/scripts/README-doc-summary-bot.md` を参照。

## 関連リポジトリ

- **`cc-relative-info`**: Claude Code 拡張（Skill / Rule / Agent）の開発サンドボックス。本リポジトリのパイプライン（Skill・Agent・スクリプト）の出自であり、汎用 `llms.txt` 生成ツール `generate-llms-txt` 等はあちらに残る。
