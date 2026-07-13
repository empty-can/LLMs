---
対象期間: 2026年07月10日 〜 2026年07月12日
作成日: 2026-07-12
---

# MCP 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
今回の対象期間の原文差分は、リモート MCP サーバー／ローカル MCP サーバーへの接続手順を、現行の Claude Desktop・ブラウザ版 Claude の UI に合わせて書き直した記述のみでした。プロトコル仕様・SDK・設定ファイルの書式に実体的な変更はなく、今回取り上げるべきハイライトはありません。
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
（今回の対象期間に取り上げるべきハイライトはありません）
<!-- light:highlight-list:end -->

## 新規追加されたページ

<!-- light:new-pages:start -->
（今回の対象期間に新規追加されたページはありません）
<!-- light:new-pages:end -->

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
（今回の対象期間に大幅更新されたページはありません）
<!-- light:updated-pages:end -->

## 軽微な更新

<!-- light:minor-updates:start -->
今回の対象期間に更新されたのは 2 ページで、いずれも Claude 側の UI 変更にドキュメントの手順記述を追従させるものです。

**機能改善**

- 「Connect to remote MCP Servers」ページの「Connecting to a Remote MCP Server」節で、設定画面（Connectors）を開くまでの手順が、Claude Desktop とブラウザ版に分けて記述されるようになりました。Desktop はキーボードショートカット `Ctrl+Comma`、またはウィンドウ左上のメニューアイコンから「File」→「Settings」を選択、ブラウザ版はキーボードショートカット `⌘⇧,`（macOS）、またはプロフィールアイコンから「Settings」を選択し、そのうえでサイドバーの「Connectors」を開く、という流れです。従来はブラウザ版のプロフィールアイコン経由の手順のみが書かれていました。 — [Connect to remote MCP Servers](https://modelcontextprotocol.io/docs/develop/connect-remote-servers#connecting-to-a-remote-mcp-server)
- 同節の「Add a Custom Connector」手順で、カスタムコネクタの追加方法が現行 UI に合わせて改められました。従来は「Connectors セクションの最下部までスクロールして『Add custom connector』ボタンを押す」でしたが、新しい記述では「ウィンドウ右上の『Add』ボタンを押し、ドロップダウンから『Add custom connector』を選ぶ」となっています。あわせて、読者が手順をそのまま試せるように、例示用のリモートサーバー URL `https://example-server.modelcontextprotocol.io/mcp` が手順内に追加されました。 — [Connect to remote MCP Servers](https://modelcontextprotocol.io/docs/develop/connect-remote-servers#connecting-to-a-remote-mcp-server)
- 同節の「Access Resources and Prompts」手順で、接続済みリモートサーバーのリソース・プロンプトを会話に取り込む導線が更新されました。従来は「メッセージ入力欄のクリップ（paperclip）アイコンをクリックして添付メニューを開く」でしたが、新しい記述では「メッセージ入力欄の左下にある『Add files, connectors, and more /』インジケーターをクリックし、『Connectors』にカーソルを合わせ、さらに『Add to Example Remote Server』にカーソルを移動すると添付メニューが表示される」に変わっています。 — [Connect to remote MCP Servers](https://modelcontextprotocol.io/docs/develop/connect-remote-servers#connecting-to-a-remote-mcp-server)

**その他**

- 「Connect to local MCP servers」ページの「Installing the Filesystem Server」節で、Claude Desktop 再起動後に押すインジケーターの表記が、現行 UI のラベルに合わせて「Add files, connectors and more」から「Add files, connectors, and more /」に修正されました。あわせて操作の言い回しが「scroll over『Connectors』」から「move the mouse over『Connectors』」に改められ、「view the the Filesystem Server's available tools」という語の重複によるタイポも修正されています。手順そのもの（インジケーター → Connectors → Manage connectors → filesystem を選択）に変更はありません。 — [Connect to local MCP servers](https://modelcontextprotocol.io/docs/develop/connect-local-servers#installing-the-filesystem-server)
<!-- light:minor-updates:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-07-10.md](./archives/latest/2026-07-10.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-07-10.md](./archives/latest-detail/2026-07-10.md)

<!--
base_commit: ffddd087c516310fe994c988f8b0ffd8fba71e59
head_commit: ad04427077fcdb5fbb719e1ab9462aa953c5ca81
generated_at_full: 2026-07-13T15:01:12+09:00
-->
