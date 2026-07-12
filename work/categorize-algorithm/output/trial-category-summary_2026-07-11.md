---
対象期間: 2026年07月10日 〜 2026年07月11日
作成日: 2026-07-11
形式: カテゴリ別グルーピング試作版（ハイライトセクション廃止）
---

# Claude Code 公式ドキュメント更新サマリ（カテゴリ別・試作）

```markdown
今回の変更 10 件のうち 6 件は「パーミッション・セキュリティ」に集中しています。Claude Code が実際に何に対して確認を求めるのか（組み込み read-only コマンドは確認なし、Read/Grep/Glob も作業ディレクトリ外では確認あり）という記述が、権限リファレンス・セキュリティ・ツールリファレンス・VS Code・ロールアウト資料まで一斉に見直されました。残りは Linux デスクトップアプリの導線整理（3 件）と Agent SDK の参照追加（1 件）です。新規ページ・changelog リリースはありません。
```

## カテゴリ別の変更点

### 🔐 パーミッション・セキュリティ — 6件

- 権限設定ページの権限システム表が精緻化された。「読み取り専用」は*作業ディレクトリと追加ディレクトリの内側なら*承認不要、「Bash コマンド」は*組み込みの read-only コマンドセット（`ls`・`cat` 等）を除き*承認要、と条件付きの記述に改められた。 — [English](https://code.claude.com/docs/en/permissions#permission-system)
- セキュリティページの組み込み保護の項目「書き込みアクセス制限」が「作業ディレクトリの境界」に改称・全面改稿された。境界外の読み取りは Read/Grep/Glob では承認プロンプト後に可能なこと、追加ディレクトリで境界を拡張できること、read-only Bash コマンドの広い読み取りは sandbox の `denyRead` ルール（sandbox 有効時のみ）で制限できることが明記された。 — [English](https://code.claude.com/docs/en/security#built-in-protections)
- ツールリファレンスに、ツール表の「Permission required」列の意味を定義する段落が新設された。この列は既定モード・作業ディレクトリ内での挙動を示すもので、「No」の Read/Grep/Glob も境界外ではプロンプトし、「Yes」の Bash も組み込み read-only コマンドはプロンプトなしで走る。 — [English](https://code.claude.com/docs/en/tools-reference)
- VS Code 拡張ページの Manual モードの説明が「各アクションの前に確認」から「ファイル編集とほとんどのシェルコマンドの前に確認」へ修正された（実挙動に合わせた記述修正）。〔関連: 🖥 アプリ・プラットフォーム〕 — [English](https://code.claude.com/docs/en/vs-code#use-the-prompt-box)
- コミュニケーションキット（組織ロールアウト用文面集）の Shift+Tab 解説スニペットでも、Manual モードの説明が同趣旨に修正された。 — [日本語](https://code.claude.com/docs/ja/communications-kit#control-and-safety) / [English](https://code.claude.com/docs/en/communications-kit#control-and-safety)
- 同キットの FAQ「リポジトリ全体を見ることができますか？」の回答が拡充された。プロンプトがゲートする操作の正確な範囲と、組み込み read-only シェルコマンドがプロンプトなしで走ること、`denyRead` での制限方法が加わった。 — [日本語](https://code.claude.com/docs/ja/communications-kit#faq-responses) / [English](https://code.claude.com/docs/en/communications-kit#faq-responses)

### 🖥 アプリ・プラットフォーム — 3件

- Linux 版デスクトップアプリの手動インストール手順が刷新された。apt リポジトリを使えない場合の案内が、`claude.com/download` からの `.deb` ダウンロードではなく、リポジトリのパッケージプールから最新版を直接取得する curl コマンドに置き換えられ、失敗時エラー（`Remote file name has no length`）の切り分け方も添えられた。 — [English](https://code.claude.com/docs/en/desktop-linux#install-from-a-downloaded-file)
- 高度なセットアップページの Tip で、デスクトップアプリの Linux 版リンクが `claude.com/download` から上記 Linux インストール手順ページへ変更された。 — [日本語](https://code.claude.com/docs/ja/setup#install-claude-code) / [English](https://code.claude.com/docs/en/setup#install-claude-code)
- インストールとログインのトラブルシューティングページの Tip も同様に変更され、「Linux では apt でアプリをインストール」と Linux インストール手順へ誘導するようになった。 — [日本語](https://code.claude.com/docs/ja/troubleshoot-install#find-your-error) / [English](https://code.claude.com/docs/en/troubleshoot-install#find-your-error)

### 🧩 Agent SDK・サブエージェント — 1件

- Agent SDK の MCP ページの「関連リソース」に「MCP 出力制限と警告」への参照が追加された。`MAX_MCP_OUTPUT_TOKENS` を超えるツール結果の SDK での扱い（ディスク永続化フォールバック、ツール毎の `anthropic/maxResultSizeChars` アノテーション）の参照先が示されている。〔関連: 🔌 MCP・外部連携〕 — [日本語](https://code.claude.com/docs/ja/agent-sdk/mcp#related-resources) / [English](https://code.claude.com/docs/en/agent-sdk/mcp#related-resources)

### 今回変更のなかったカテゴリ

**🔌 MCP・外部連携**（SDK 経由の関連 1 件のみ → 上記参照） / **🧰 拡張機能（プラグイン・スキル・フック）** / **⚙️ 設定・環境変数** / **🤖 モデル・利用状況** / **🏢 エンタープライズ基盤（Bedrock / Google Cloud / Foundry / ゲートウェイ）** / **📚 セッション・コンテキスト** / **⌨️ コマンド・ワークフロー**

## 分類の根拠（付録）

カテゴリは `term_scoring.py`（v3）の包含併合後スコア上位グループを土台に試作用へ仮確定した 10 分類。各項目は変更テキスト・対象ページ slug とカテゴリ語彙のマッチで分類した。

| 項目（対象ページ） | 主カテゴリ | マッチした語彙 |
|---|---|---|
| permissions（権限システム表） | パーミッション | permission, read-only, working directory |
| security（作業ディレクトリの境界） | パーミッション | security, permission, sandbox, denyRead |
| tools-reference（Permission required 列） | パーミッション | permission, read-only command |
| vs-code（Manual モード） | パーミッション | permission mode, manual |
| communications-kit（Shift+Tab） | パーミッション | permission mode, acceptEdits, plan |
| communications-kit（FAQ） | パーミッション | permission prompt, read-only, sandbox |
| desktop-linux（.deb 取得手順） | アプリ・プラットフォーム | desktop, apt, install |
| setup（Linux リンク） | アプリ・プラットフォーム | desktop app, install |
| troubleshoot-install（Linux リンク） | アプリ・プラットフォーム | desktop app, install |
| agent-sdk/mcp（出力制限の参照） | Agent SDK | agent-sdk/（slug prefix）, sdk ＋副: mcp |

**試作上の注記**

- ページ単位でなく**内容単位**で分類している。communications-kit（ロールアウト資料）の 2 件も、変更内容がパーミッション仕様の記述であるためパーミッションに分類された（ページ見出し粒度のカテゴリでは実現しない挙動）
- ハイライト（3〜5 件選抜）と概要=ハイライト同数制約は廃止し、概要はカテゴリ分布の要約に置き換えた
- 既存パイプラインのテンプレート契約（`light:*` マーカー、`## N.` 見出し、derive_light.py、ja-follow watch の錨）は本試作には未適用。正式採用時は Phase3 で設計する
- ja リンクは本日 bot 生成サマリ（Phase 3 レビュー済）で検証済みのもののみ付与し、未検証ページは English のみとした

<!--
base_commit: b0e62bddfff0079453cf5aec4c9e84b11f68c93f
head_commit: 7acfb2c1fd59240680f0797da7e72d0d9ead003e
generated_at_full: 2026-07-12T15:40:00+09:00 (trial)
-->
