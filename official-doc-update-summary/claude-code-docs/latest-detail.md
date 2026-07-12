---
対象期間: 2026年07月10日 〜 2026年07月11日
作成日: 2026-07-11
---

# Claude Code 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
今回の対象期間は、changelog に新しいリリースが追加されず、代わりに「Claude Code は実際のところ何に対して確認を求めるのか」というドキュメント上の記述が、権限リファレンスからセキュリティページ・VS Code ページ・ロールアウト用資料まで一斉に見直された回です。従来の「読み取り専用ツールは確認なし / Bash は確認あり」という単純な二分法が、実挙動に合わせて条件つきの記述に改められました。新規ページと週刊ダイジェストの追加はなく、差分は `llms-full.txt` の本文のみです。

主要なものを以下に挙げます。

1. 権限設定ページとツールリファレンスが、Bash には確認なしで走る組み込みの読み取り専用コマンド（`ls`・`cat`・`git status` など）があり、逆に Read/Grep/Glob は作業ディレクトリの外では確認を求めることを明示するようになった
2. セキュリティページの防御項目「書き込みアクセス制限」が「作業ディレクトリの境界」に改称され、VS Code ページの Manual モードの説明も「各アクションの前に確認」から「ファイル編集とほとんどのシェルコマンドの前に確認」に修正された
3. Linux 版デスクトップアプリの `.deb` 直接インストール手順が、apt リポジトリのパッケージプールから最新版を引く curl コマンドに置き換えられた
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**権限リファレンスが読み取り専用の境界を明示**](#1-権限リファレンスが読み取り専用の境界を明示):  
  権限設定ページの権限システム表で、「Bash コマンド」の承認要否が「はい、ただし組み込みの読み取り専用コマンドセットを除く」に、「読み取り専用」が「いいえ、作業ディレクトリと追加ディレクトリ内」に書き換えられた。ツールリファレンスにも、表の「権限が必要」列が何を意味するかを説明する段落が新設された。
2. [**権限記述の見直しがセキュリティページと各サーフェスの説明にも波及**](#2-権限記述の見直しがセキュリティページと各サーフェスの説明にも波及):  
  セキュリティページの組み込み保護の項目名が「書き込みアクセス制限」から「作業ディレクトリの境界」に変わり、境界外の読み取りは承認プロンプト後に可能であること、読み取り専用 Bash コマンドの広い読み取りは sandbox の `denyRead` ルールで絞れることが加わった。VS Code ページの Manual モードの説明も同じ趣旨に修正された。
3. [**Linux 版デスクトップアプリの手動インストール手順が刷新**](#3-linux-版デスクトップアプリの手動インストール手順が刷新):  
  apt リポジトリを使えない場合の案内が、`claude.com/download` からの `.deb` ダウンロードではなく、リポジトリのパッケージインデックスを引いて最新パッケージを直接取得する curl コマンドに置き換えられた。失敗時のエラー（`Remote file name has no length`）の読み解き方も添えられている。
<!-- light:highlight-list:end -->

## 1. 権限リファレンスが読み取り専用の境界を明示

権限設定ページ（`docs/en/permissions`）冒頭の「権限システム」表が書き換えられました。従来は「読み取り専用 = 承認不要（いいえ）」「Bash コマンド = 承認必要（はい）」という単純な二分法でしたが、今回そこに条件が付きました。「読み取り専用」行の承認要否は **「いいえ、作業ディレクトリと追加ディレクトリ内」**（同ページの「作業ディレクトリ」節へのリンク付き）になり、「Bash コマンド」行は **「はい、読み取り専用コマンドの組み込みセットを除く」**（同ページの「読み取り専用コマンド」節へのリンク付き）になりました。リンク先の「読み取り専用コマンド」節（`ls`・`cat`・`echo`・`grep`・`git` の読み取り専用形式などが全モードで確認なしに走る、という説明）は以前から存在していたもので、今回の変更はそれを表の側から可視化したものです。

同じ趣旨の説明が、ツールリファレンス（`docs/en/tools-reference`）のツール一覧表の直前にも段落として新設されました。「権限が必要」列は**既定の権限モードで、かつ作業ディレクトリ内のパスに対して**プロンプトを出すかどうかを示すこと、`Read`・`Grep`・`Glob` は「いいえ」と書かれているが作業ディレクトリと追加ディレクトリの**外**のパスに対しては確認を求めること、`Bash` は「はい」と書かれているが組み込みの読み取り専用コマンドセットは確認なしで走ること、が明記されています。表そのものは変わっておらず、表の読み方を補う位置づけです。

- [権限を設定する（権限システム） - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/permissions#permission-system)
- [Configure permissions (Permission system) - Claude Code Docs (English)](https://code.claude.com/docs/en/permissions#permission-system)
- [ツール リファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/tools-reference)
- [Tools reference - Claude Code Docs (English)](https://code.claude.com/docs/en/tools-reference)

## 2. 権限記述の見直しがセキュリティページと各サーフェスの説明にも波及

セキュリティページ（`docs/en/security`）の「組み込み保護機能」で、項目名が **「書き込みアクセス制限」から「作業ディレクトリの境界」** に改められ、本文も差し替えられました。旧版は「Claude Code は起動フォルダとその配下にしか書き込めない。作業ディレクトリ外のファイルを読むことはできる（システムライブラリや依存関係の参照に有用）が、書き込みはプロジェクトスコープに厳密に閉じている」という書き方でした。新版は、境界外のパスを Read・Grep・Glob で読むこと自体は**承認プロンプトを経れば可能**であると述べたうえで、プロンプトを省きたければ[追加ディレクトリ](https://code.claude.com/docs/ja/permissions#working-directories)で境界を広げる、逆に読み取り専用 Bash コマンドが持つ広い読み取りアクセスを絞りたければ sandbox の `denyRead` ルール（サンドボックス有効時にのみ適用）を使う、という 2 方向の調整手段を案内しています。同ページの「パーミッションベースのアーキテクチャ」節でも、`ls`・`cat`・`git status` といった読み取り専用コマンドの組み込みセットに触れる一文が、権限設定ページの該当節へのリンクになりました。

Claude Code を利用する各サーフェスの説明も同じ表現に揃えられました。VS Code ページ（`docs/en/vs-code`）のプロンプトボックスの権限モード一覧では、**Manual** の説明が「Claude は各アクションの前に権限を求めます」から **「Claude はファイル編集とほとんどのシェルコマンドの前に権限を求めます」** に変わりました。「各アクションの前」という旧表現は、読み取り専用コマンドが確認なしで走る実挙動と食い違っていたため、それを正した形です。同じ文言の修正はロールアウト用資料であるコミュニケーションキットにも入っています（「軽微な更新」参照）。

- [セキュリティ（組み込み保護機能） - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/security#built-in-protections)
- [Security (Built-in protections) - Claude Code Docs (English)](https://code.claude.com/docs/en/security#built-in-protections)
- [VS Code で Claude Code を使用する（プロンプトボックスを使用する） - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/vs-code#use-the-prompt-box)
- [Use Claude Code in VS Code (Use the prompt box) - Claude Code Docs (English)](https://code.claude.com/docs/en/vs-code#use-the-prompt-box)

## 3. Linux 版デスクトップアプリの手動インストール手順が刷新

Claude Desktop on Linux（beta）ページ（`docs/en/desktop-linux`）の「ダウンロードしたファイルからインストールする」節が書き直されました。従来は「apt リポジトリが使えない場合は [claude.com/download](https://claude.com/download) から自分のアーキテクチャ（x64 または arm64）向けの `.deb` をダウンロードする」という案内でしたが、新版は **apt リポジトリのパッケージプールから直接取得する 1 行の curl コマンド** を提示します。このコマンドはリポジトリのパッケージインデックス（`dists/stable/main/binary-$(dpkg --print-architecture)/Packages`）を引き、`claude-desktop_` で始まる `Filename:` 行をバージョン順に並べて最新のものを選び、そのパスを現在のディレクトリにダウンロードします。

失敗時の読み解き方も添えられました。コマンドが `Remote file name has no length` で落ちた場合は検索がパッケージパスを返さなかったということで、原因はリポジトリインデックスを取得できなかった（例: ネットワークが `downloads.claude.ai` をブロックしている）か、そのアーキテクチャ向けのパッケージが存在しないかのいずれかです。`downloads.claude.ai` に到達できること、`dpkg --print-architecture` が `amd64` か `arm64` を返すことを確認するよう案内されています。ダウンロード後の導線には GNOME Software のような GUI インストーラで開く選択肢が例示され、更新を受け取る方法の説明も「上記のようにリポジトリを追加する」から「『Anthropic の apt リポジトリを追加する』ステップからリポジトリを登録する（パッケージが書き込むコメントアウト済みエントリの `deb` 行を外すのと同等）」という書き方に整理されました。この変更に合わせて、高度なセットアップページとインストールのトラブルシューティングページの Tip も、Linux 版デスクトップアプリのダウンロード先を `claude.com/download` から本ページへ差し替えています（「軽微な更新」参照）。

- [Claude Desktop on Linux (beta)（ダウンロードしたファイルからインストールする） - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/desktop-linux#install-from-a-downloaded-file)
- [Claude Desktop on Linux (beta) (Install from a downloaded file) - Claude Code Docs (English)](https://code.claude.com/docs/en/desktop-linux#install-from-a-downloaded-file)

## 新規追加されたページ

<!-- light:new-pages:start -->
今回、新規追加されたページはありません。`llms.txt` とページ見出しマップ（`claude_code_docs_map.md`）にも変更はなく、差分は `llms-full.txt` の本文のみです。
<!-- light:new-pages:end -->

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
本文に 50 行以上の変更があったページはありません。本文の実体的な変更（権限システム表の書き換え、ツールリファレンスの段落新設、セキュリティページの項目差し替え、desktop-linux のインストール手順刷新）は、いずれも上記ハイライトで扱いました。
<!-- light:updated-pages:end -->

## 軽微な更新

<!-- light:minor-updates:start -->
今回の軽微な更新は、ハイライトで扱った権限記述の見直しがロールアウト用資料にも波及したものと、Agent SDK・セットアップ系ページのリンク追加・変更です。対象期間の差分に changelog の新規リリースは含まれないため、バージョン併記はありません。

**機能改善**

- Agent SDK の MCP ページの「関連リソース」に「MCP 出力制限と警告」への項目が追加された。`MAX_MCP_OUTPUT_TOKENS` を超えるツール結果を SDK がどう扱うか（ディスクへの永続化フォールバック、ツールごとの `anthropic/maxResultSizeChars` アノテーション）の参照先が示されている。 — [日本語](https://code.claude.com/docs/ja/agent-sdk/mcp#related-resources) / [English](https://code.claude.com/docs/en/agent-sdk/mcp#related-resources)
- コミュニケーションキット（Claude Code を組織にロールアウトするための文面集）の Shift+Tab 解説スニペットで、Manual モードの説明が「各アクションの前に尋ねる」から「ファイル編集とほとんどのシェルコマンドの前に尋ねる」に修正された（背景はハイライト 2 参照）。 — [日本語](https://code.claude.com/docs/ja/communications-kit#control-and-safety) / [English](https://code.claude.com/docs/en/communications-kit#control-and-safety)
- 同キットの FAQ「リポジトリ全体を見ることができますか？」の回答が拡充された。権限プロンプトがゲートするのは編集・読み取り専用以外のシェルコマンド・作業ディレクトリ外のファイルツール読み取りであること、`ls` や `cat` などの組み込みの読み取り専用シェルコマンドはプロンプトなしで走ること、それを sandbox の `denyRead` ルールで制限できることが加わった（背景はハイライト 1 参照）。 — [日本語](https://code.claude.com/docs/ja/communications-kit#faq-responses) / [English](https://code.claude.com/docs/en/communications-kit#faq-responses)

**その他**

- 高度なセットアップページの Tip で、デスクトップアプリの Linux 版ダウンロードリンクが `claude.com/download` から Linux インストール手順ページへ変更された（詳細はハイライト 3 参照）。 — [日本語](https://code.claude.com/docs/ja/setup#install-claude-code) / [English](https://code.claude.com/docs/en/setup#install-claude-code)
- インストールとログインのトラブルシューティングページの Tip も同様に変更され、「Linux では apt でアプリをインストールしてください」と Linux インストール手順へ誘導する 1 文が加わった（詳細はハイライト 3 参照）。 — [日本語](https://code.claude.com/docs/ja/troubleshoot-install#find-your-error) / [English](https://code.claude.com/docs/en/troubleshoot-install#find-your-error)
<!-- light:minor-updates:end -->

## 新着情報

<!-- light:whats-new:start -->
今回の対象期間では、週刊ダイジェスト「新着情報」（`whats-new/`）の追加・更新はありません。直近の Week 27・Week 28 については前回サマリを参照してください。
<!-- light:whats-new:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-07-10.md](./archives/latest/2026-07-10.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-07-10.md](./archives/latest-detail/2026-07-10.md)

<!--
base_commit: b0e62bddfff0079453cf5aec4c9e84b11f68c93f
head_commit: 7acfb2c1fd59240680f0797da7e72d0d9ead003e
generated_at_full: 2026-07-12T15:02:57+09:00
-->
