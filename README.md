# LLMs

Claude Code 周辺の公式ドキュメントを LLM／人間の双方が扱いやすい形で集約・公開するリポジトリ。

> **現状**: `cc-relative-info` リポジトリで構築・検証した「公式ドキュメント更新サマリ自動生成パイプライン」を、本リポジトリへ移設して正式運用する移行の途上です。下記の構成は移行完了後の目標形を示します（移行設計は `cc-relative-info` 側の `LLMs/work/publish-migration/` 参照）。

## 何を公開するか

1. **公式 `llms.txt` / `llms-full.txt` の取り込み**: Claude Code 公式ドキュメント（`code.claude.com`）と Model Context Protocol 公式（`modelcontextprotocol.io`）が公開する `llms.txt` / `llms-full.txt` を定期取得して保存する。
2. **更新サマリ（人間向け changelog）**: 上記の更新差分を、人間が読みやすい changelog／リリースノート風の Markdown として自動生成・蓄積する（詳細版＋ライト版の 2 ファイル方式）。

> 📄 **公開中の更新サマリは [`official-doc-update-summary/`（トップページ）](./official-doc-update-summary/README.md) から閲覧できます。** 最新版・過去アーカイブへのリンクと読み方をまとめています。

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

## どう更新されるか

更新サマリは、日次でスケジュール実行される**無人パイプラインが自動生成**しています（取得 → サマリ生成 → 第三者レビュー → 人手レビュー → 公開）。利用者が手を動かす必要はありません。

> パイプラインの構成・ブランチ運用・スケジューラ・push 認証などの**メンテナー向け情報**は、リポジトリを保守する立場で作業するとき自動で参照される `.claude/CLAUDE.md`（および `.claude/scripts/README-doc-summary-bot.md`）に集約しています。
