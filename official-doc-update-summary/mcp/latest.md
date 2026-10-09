---
対象期間: 2026年10月06日 〜 2026年10月08日
作成日: 2026-10-08
---

# MCP 公式ドキュメント更新サマリ

```markdown
今回の対象期間は MCP Inspector のドキュメントに更新が集中しました。新規ページが 2 件追加され、既存の Inspector ページ 8 件が更新されています（うち 4 件は 50 行以上の大幅更新）。

主要なものを以下に挙げます。

1. サーバーに一度接続し、その名前付き接続に対して多数のコマンドを実行できる実験的な接続クライアント `mcpdo` のページが追加された
2. OAuth トークン・クライアントシークレット・stdio の `env:` 値を設定ファイルから分離して保存する「シークレットストア」が導入され、キーチェーンが無い環境では暗号化されていないファイルへ自動でフォールバックすることが明記された
3. Web バックエンド・Docker・シークレット保存・stdio サーバー・mcpdo デーモンの脅威モデルを 1 か所にまとめた Inspector の Security ページが追加された
4. CLI に CI 向けのゲート（`--strict` / `--verify` / `--require-digests`、終了コード 6〜9）と、接続せずにカタログを書き換える `servers/add` / `servers/edit` / `servers/remove` が追加された
```

## ハイライト

1. [**mcpdo 接続クライアントを追加**](./latest-detail.md#1-mcpdo-接続クライアントを追加):  
  `@modelcontextprotocol/inspector` パッケージに同梱される 2 つ目のコマンド `mcpdo` のページが追加された。一度 `connect` した接続をバックグラウンドデーモン `mcpdod` が保持し、どのシェルからでも `@name` で同じ接続にコマンドを送れる。タスク・サブスクリプション・エリシテーションのように 1 セッションにまたがる操作や、エージェントからのツール利用を想定している。
2. [**シークレットストアの導入**](./latest-detail.md#2-シークレットストアの導入):  
  資格情報を `mcp.json` / `client.json` / `oauth.json` から分離し、OS キーチェーン → ファイル → メモリの順で選ばれるシークレットストアへ保存するようになった。キーチェーンが無い環境では、鍵を与えない限り暗号化されない `secrets.json` へ自動で保存される。
3. [**Inspector の Security ページを新設**](./latest-detail.md#3-inspector-の-security-ページを新設):  
  Inspector の脅威モデルを 1 ページに集約した。Web バックエンドの API トークンが防ぐもの・防がないもの、Docker のポート公開、ファイルストアの保護範囲、stdio サーバーの権限、mcpdo デーモンの認証と寿命を扱う。
4. [**CLI に CI ゲートとカタログ編集を追加**](./latest-detail.md#4-cli-に-ci-ゲートとカタログ編集を追加):  
  `--strict`・`--verify`・`--require-digests` がそれぞれ固有の終了コード（6〜9）で失敗を返すようになり、`servers/add` / `servers/edit` / `servers/remove` で接続せずにカタログを編集できるようになった。

## 新規追加されたページ

- [**mcpdo connection client**](./latest-detail.md#1-mcpdo-接続クライアントを追加) ([MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/mcpdo#quickstart)):  
  一度接続した名前付き接続に対して多数のコマンドを実行できる、実験的な接続クライアント `mcpdo` の解説ページ（詳細はハイライト 1 参照）。
- [**Security**](./latest-detail.md#3-inspector-の-security-ページを新設) ([MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/security#what-the-file-store-protects-against)):  
  Web バックエンド・Docker・シークレット保存・stdio サーバー・mcpdo デーモンにわたる Inspector の脅威モデルをまとめたページ（詳細はハイライト 3 参照）。

## 大幅に更新されたページ

- [**Configuration and flags**](./latest-detail.md#1-configuration-and-flags) ([MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/configuration#where-secrets-are-stored)):  
  シークレットストアの節と環境変数を追加したほか、`--server` や `--` セパレータの扱いがクライアントごとに異なる点を訂正した（追加 126 行・削除 22 行）。
- [**Recipes**](./latest-detail.md#2-recipes) ([MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/recipes#docker)):  
  Docker 節をループバック公開・データボリュームとシークレット・ヘルスチェックの観点で書き直し、リバースプロキシ配下の MCP Apps 設定と mcpdo の節を追加した（追加 127 行・削除 19 行）。
- [**CLI client**](./latest-detail.md#3-cli-client) ([MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/cli#exit-codes-and-error-envelopes)):  
  CI ゲートとカタログ編集に加え、`--tool-arg` の型変換規則、エラーエンベロープの項目、`--advertise-apps` などを追記した（追加 66 行・削除 14 行）。
- [**Protocol eras**](./latest-detail.md#4-protocol-eras) ([MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/protocol-eras#cancellation)):  
  `--protocol-era` フラグ、キャンセルの節を追加し、`Mcp-Param-*` ヘッダーのミラーリングに関する記述を訂正した（追加 41 行・削除 23 行）。

## 軽微な更新

50 行未満の本文変更があった既存ページは 4 件です。

**新機能**

- TUI に Subscriptions（`u`）・Skills（`k`）・Tasks（`s`）タブを追加。対応するサーバーに接続したときだけ表示される。あわせてリストの絞り込み（`/`）、詳細の全画面表示（`+`）、コピー・保存（`y` / `w`）、キーバインドのヘルプ（`?`）を追加し、`Tab` / `Shift+Tab` でペイン間のフォーカスを移動する形に変更 — [MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/tui#tabs)
- Web クライアントに Skills タブ（SEP-2640 の Skills 拡張を宣言するサーバー向け）を追加 — [MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/web#the-tab-bar)
- Web クライアントの Server Settings に OAuth Settings（読み取り専用の Redirect URI、Scopes、Revoke tokens on clear、Insufficient-scope response など）と、使用中のシークレットストアを示すフッターを追加 — [MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/web#server-settings)
- `--relogin` が保存済み OAuth を削除するだけでなく認可サーバー側でグラントを失効させるようになった（`--no-revoke` で抑止） — [MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/authorization#handing-off-from-the-web-client-to-the-cli)

**機能改善**

- Inspector の索引ページに mcpdo の紹介と、シークレットがキーチェーンの無い環境では暗号化されないファイルに保存されるという警告を追加し、「Where to go next」に mcpdo と Security のカードを追加（詳細はハイライト 1・3 参照） — [MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector#inspecting-published-servers)
- Authorization ページで、Web の OAuth コールバック URL が Inspector を開いたオリジンに従う（既定 `http://127.0.0.1:6274/oauth/callback`）ことを明記し、`--callback-url` による上書きは CLI と TUI のみと整理 — [MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/authorization#callback-urls)
- Authorization ページで、Web クライアントの再認可（Re-authentication required バナー）とステップアップ（Additional permissions required ダイアログ）の UI を具体化し、ミッドセッションのチャレンジで拒否されたリクエストを自動で再試行するのは CLI のみ、Web は再試行を促す形と訂正 — [MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/authorization#mid-session-re-authorization)
- TUI が共有のサーバー選択フラグ・`--protocol-era`・OAuth クライアントフラグを受け付けることを明記 — [MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/tui#choosing-servers)
- Web クライアントの Apps タブで、サンドボックスのポートが既定 `6275`、`_meta.ui.domain` 用のアプリオリジンが既定 `6278` であること、TLS リバースプロキシ配下では `MCP_SANDBOX_FULL_ADDRESS` / `MCP_APP_ORIGIN_FULL_ADDRESS` を設定することを追記 — [MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/web#apps)

**その他**

- Web client・Configuration and flags・Recipes で、既定のバインド先の表記を `localhost` から `127.0.0.1` に統一
- Web client で、初回起動時のサンプルサーバーが 3 件になったこと、Network ビューのみシークレットを伏せること（Protocol と Console は送信どおり表示）などの記述を更新
- 索引 `llms.txt` に mcpdo connection client と Security のエントリを 2026-07-28 版・draft 版の両方で追加し、Recipes の説明文に「mcpdo による永続接続」を追記。draft 版の本文は `llms-full.txt` に収録されていない
- `llms-full.txt` 内で SEP-1330・SEP-1577・SEP-1613・SEP-1686 の収録位置が移動した。ページ本文に変更はない

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-10-06.md](./archives/latest/2026-10-06.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-10-06.md](./archives/latest-detail/2026-10-06.md)

<!--
base_commit: 4732026713f96a1268695ab6d1e2f0fc2a78d528
head_commit: f7270cc772c15a132c348d04599b3544e0e7722c
generated_at_full: 2026-10-09T15:18:43+09:00
-->
