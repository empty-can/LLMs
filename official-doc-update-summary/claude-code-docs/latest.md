---
対象期間: 2026年07月10日 〜 2026年07月11日
作成日: 2026-07-11
---

# Claude Code 公式ドキュメント更新サマリ

```markdown
今回の対象期間は、changelog に新しいリリースが追加されず、代わりに「Claude Code は実際のところ何に対して確認を求めるのか」というドキュメント上の記述が、権限リファレンスからセキュリティページ・VS Code ページ・ロールアウト用資料まで一斉に見直された回です。従来の「読み取り専用ツールは確認なし / Bash は確認あり」という単純な二分法が、実挙動に合わせて条件つきの記述に改められました。新規ページと週刊ダイジェストの追加はなく、差分は `llms-full.txt` の本文のみです。

主要なものを以下に挙げます。

1. 権限設定ページとツールリファレンスが、Bash には確認なしで走る組み込みの読み取り専用コマンド（`ls`・`cat`・`git status` など）があり、逆に Read/Grep/Glob は作業ディレクトリの外では確認を求めることを明示するようになった
2. セキュリティページの防御項目「書き込みアクセス制限」が「作業ディレクトリの境界」に改称され、VS Code ページの Manual モードの説明も「各アクションの前に確認」から「ファイル編集とほとんどのシェルコマンドの前に確認」に修正された
3. Linux 版デスクトップアプリの `.deb` 直接インストール手順が、apt リポジトリのパッケージプールから最新版を引く curl コマンドに置き換えられた
```

## ハイライト

1. [**権限リファレンスが読み取り専用の境界を明示**](./latest-detail.md#1-権限リファレンスが読み取り専用の境界を明示):  
  権限設定ページの権限システム表で、「Bash コマンド」の承認要否が「はい、ただし組み込みの読み取り専用コマンドセットを除く」に、「読み取り専用」が「いいえ、作業ディレクトリと追加ディレクトリ内」に書き換えられた。ツールリファレンスにも、表の「権限が必要」列が何を意味するかを説明する段落が新設された。
2. [**権限記述の見直しがセキュリティページと各サーフェスの説明にも波及**](./latest-detail.md#2-権限記述の見直しがセキュリティページと各サーフェスの説明にも波及):  
  セキュリティページの組み込み保護の項目名が「書き込みアクセス制限」から「作業ディレクトリの境界」に変わり、境界外の読み取りは承認プロンプト後に可能であること、読み取り専用 Bash コマンドの広い読み取りは sandbox の `denyRead` ルールで絞れることが加わった。VS Code ページの Manual モードの説明も同じ趣旨に修正された。
3. [**Linux 版デスクトップアプリの手動インストール手順が刷新**](./latest-detail.md#3-linux-版デスクトップアプリの手動インストール手順が刷新):  
  apt リポジトリを使えない場合の案内が、`claude.com/download` からの `.deb` ダウンロードではなく、リポジトリのパッケージインデックスを引いて最新パッケージを直接取得する curl コマンドに置き換えられた。失敗時のエラー（`Remote file name has no length`）の読み解き方も添えられている。

## 新規追加されたページ

今回、新規追加されたページはありません。`llms.txt` とページ見出しマップ（`claude_code_docs_map.md`）にも変更はなく、差分は `llms-full.txt` の本文のみです。

## 大幅に更新されたページ

本文に 50 行以上の変更があったページはありません。本文の実体的な変更（権限システム表の書き換え、ツールリファレンスの段落新設、セキュリティページの項目差し替え、desktop-linux のインストール手順刷新）は、いずれも上記ハイライトで扱いました。

## 軽微な更新

今回の軽微な更新は、ハイライトで扱った権限記述の見直しがロールアウト用資料にも波及したものと、Agent SDK・セットアップ系ページのリンク追加・変更です。対象期間の差分に changelog の新規リリースは含まれないため、バージョン併記はありません。

**機能改善**

- Agent SDK の MCP ページの「関連リソース」に「MCP 出力制限と警告」への項目が追加された。`MAX_MCP_OUTPUT_TOKENS` を超えるツール結果を SDK がどう扱うか（ディスクへの永続化フォールバック、ツールごとの `anthropic/maxResultSizeChars` アノテーション）の参照先が示されている。 — [日本語](https://code.claude.com/docs/ja/agent-sdk/mcp#related-resources) / [English](https://code.claude.com/docs/en/agent-sdk/mcp#related-resources)
- コミュニケーションキット（Claude Code を組織にロールアウトするための文面集）の Shift+Tab 解説スニペットで、Manual モードの説明が「各アクションの前に尋ねる」から「ファイル編集とほとんどのシェルコマンドの前に尋ねる」に修正された（背景はハイライト 2 参照）。 — [日本語](https://code.claude.com/docs/ja/communications-kit#control-and-safety) / [English](https://code.claude.com/docs/en/communications-kit#control-and-safety)
- 同キットの FAQ「リポジトリ全体を見ることができますか？」の回答が拡充された。権限プロンプトがゲートするのは編集・読み取り専用以外のシェルコマンド・作業ディレクトリ外のファイルツール読み取りであること、`ls` や `cat` などの組み込みの読み取り専用シェルコマンドはプロンプトなしで走ること、それを sandbox の `denyRead` ルールで制限できることが加わった（背景はハイライト 1 参照）。 — [日本語](https://code.claude.com/docs/ja/communications-kit#faq-responses) / [English](https://code.claude.com/docs/en/communications-kit#faq-responses)

**その他**

- 高度なセットアップページの Tip で、デスクトップアプリの Linux 版ダウンロードリンクが `claude.com/download` から Linux インストール手順ページへ変更された（詳細はハイライト 3 参照）。 — [日本語](https://code.claude.com/docs/ja/setup#install-claude-code) / [English](https://code.claude.com/docs/en/setup#install-claude-code)
- インストールとログインのトラブルシューティングページの Tip も同様に変更され、「Linux では apt でアプリをインストールしてください」と Linux インストール手順へ誘導する 1 文が加わった（詳細はハイライト 3 参照）。 — [日本語](https://code.claude.com/docs/ja/troubleshoot-install#find-your-error) / [English](https://code.claude.com/docs/en/troubleshoot-install#find-your-error)

## 新着情報

今回の対象期間では、週刊ダイジェスト「新着情報」（`whats-new/`）の追加・更新はありません。直近の Week 27・Week 28 については前回サマリを参照してください。

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-07-10.md](./archives/latest/2026-07-10.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-07-10.md](./archives/latest-detail/2026-07-10.md)

<!--
base_commit: b0e62bddfff0079453cf5aec4c9e84b11f68c93f
head_commit: 7acfb2c1fd59240680f0797da7e72d0d9ead003e
generated_at_full: 2026-07-12T15:02:57+09:00
-->
