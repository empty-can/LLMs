---
対象期間: 2026年10月06日 〜 2026年10月08日
作成日: 2026-10-08
---

# MCP 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
今回の対象期間は MCP Inspector のドキュメントに更新が集中しました。新規ページが 2 件追加され、既存の Inspector ページ 8 件が更新されています（うち 4 件は 50 行以上の大幅更新）。

主要なものを以下に挙げます。

1. サーバーに一度接続し、その名前付き接続に対して多数のコマンドを実行できる実験的な接続クライアント `mcpdo` のページが追加された
2. OAuth トークン・クライアントシークレット・stdio の `env:` 値を設定ファイルから分離して保存する「シークレットストア」が導入され、キーチェーンが無い環境では暗号化されていないファイルへ自動でフォールバックすることが明記された
3. Web バックエンド・Docker・シークレット保存・stdio サーバー・mcpdo デーモンの脅威モデルを 1 か所にまとめた Inspector の Security ページが追加された
4. CLI に CI 向けのゲート（`--strict` / `--verify` / `--require-digests`、終了コード 6〜9）と、接続せずにカタログを書き換える `servers/add` / `servers/edit` / `servers/remove` が追加された
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**mcpdo 接続クライアントを追加**](#1-mcpdo-接続クライアントを追加):  
  `@modelcontextprotocol/inspector` パッケージに同梱される 2 つ目のコマンド `mcpdo` のページが追加された。一度 `connect` した接続をバックグラウンドデーモン `mcpdod` が保持し、どのシェルからでも `@name` で同じ接続にコマンドを送れる。タスク・サブスクリプション・エリシテーションのように 1 セッションにまたがる操作や、エージェントからのツール利用を想定している。
2. [**シークレットストアの導入**](#2-シークレットストアの導入):  
  資格情報を `mcp.json` / `client.json` / `oauth.json` から分離し、OS キーチェーン → ファイル → メモリの順で選ばれるシークレットストアへ保存するようになった。キーチェーンが無い環境では、鍵を与えない限り暗号化されない `secrets.json` へ自動で保存される。
3. [**Inspector の Security ページを新設**](#3-inspector-の-security-ページを新設):  
  Inspector の脅威モデルを 1 ページに集約した。Web バックエンドの API トークンが防ぐもの・防がないもの、Docker のポート公開、ファイルストアの保護範囲、stdio サーバーの権限、mcpdo デーモンの認証と寿命を扱う。
4. [**CLI に CI ゲートとカタログ編集を追加**](#4-cli-に-ci-ゲートとカタログ編集を追加):  
  `--strict`・`--verify`・`--require-digests` がそれぞれ固有の終了コード（6〜9）で失敗を返すようになり、`servers/add` / `servers/edit` / `servers/remove` で接続せずにカタログを編集できるようになった。
<!-- light:highlight-list:end -->

## 1. mcpdo 接続クライアントを追加

**mcpdo connection client**（`tools/inspector/mcpdo`）のページが新たに追加されました。`mcpdo` は `@modelcontextprotocol/inspector` パッケージに `mcp-inspector` と並んで同梱される**実験的**なコマンドラインクライアントです。接続して `--method` を 1 回実行し切断する CLI クライアントとは異なり、`mcpdo` は**一度接続したら接続を開いたまま**にし、`ssh-agent` が鍵を保持するのと同じ要領で、どのシェルからでもその接続に多数のコマンドを実行できます。CI のアサーションには従来の CLI、サーバーの探索・エージェントによるツール利用・1 セッションにまたがる複数ステップの操作（タスク、サブスクリプション、エリシテーション）には `mcpdo`、という使い分けが表で示されています。

接続はローカルのバックグラウンドデーモン `mcpdod` が保持します。デーモンは必要になった時点で `mcpdo` が自動起動し、最後の接続が閉じてから約 1 分後に終了します。接続はカタログのエントリ名またはアドホックなターゲット（URL や stdio コマンド）で開き、各コマンドでは `@name` または `--connection`（短縮形 `--conn`）で接続を指定します。名前を省略すると直近に使った接続が使われますが、これは対話的な TTY の場合のみで、スクリプトやエージェントからの名前なしコマンドはエラーになります（`MCP_ALLOW_DEFAULT_CONNECTION=1` で許可可能）。切れたトランスポートは次回の利用時に保存済みの資格情報で自動的に再接続され、1 つの接続では一度に 1 つの呼び出しだけが実行されます。

このほか、`--task` によるタスク拡張呼び出し（完了までブロック）、OAuth を接続時に実行する認可（`--relogin`、`--clear-auth`、`auth/list` など）、非対話時にエリシテーションをデーモン上に保留して `elicitation/respond` で後から回答する仕組み（10 分で取り消し）、`connect --era` による protocol era の指定、`mcpdo private` によるシェル単位のデーモン分離、信頼できない stdio サーバーをコンテナで隔離する方法が解説されています。また、パッケージには `mcpdo` を操作するためのエージェントスキルが同梱され、`mcpdo agent-help` でガイドや `CLAUDE.md` / `AGENTS.md` に追記するための指示ブロックを出力できます。

あわせて Inspector の索引ページ・Configuration and flags・CLI client・Recipes に mcpdo への案内が追加されました。Recipes には「Keeping a connection open with mcpdo」節が新設されています。なお、索引 `llms.txt` には 2026-07-28 版と draft 版の両方のエントリが追加されましたが、`llms-full.txt` に収録された本文は 2026-07-28 版のみです。

- [mcpdo connection client - MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/mcpdo#quickstart)
- [Recipes - MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/recipes#keeping-a-connection-open-with-mcpdo)

## 2. シークレットストアの導入

Configuration and flags ページに「Where secrets are stored」節が新設されました。Inspector は `mcp.json`・`client.json`・`oauth.json` を共有・コミット・同期しても資格情報が漏れないよう、取得した OAuth トークン（アクセス・リフレッシュ・IdP セッショントークン）、各サーバーの OAuth クライアントシークレットとエンタープライズ IdP のクライアントシークレット、stdio サーバーの `env:` 値を**シークレットストア**へ保存します。`env:` のキーは `mcp.json` に空の値で残り、実際の値がストアに入ります。一方、`headers` は移動されず、`mcp.json` に書いたとおり保存される点が注意として明記されています。

ストアはプロセスごとに一度だけ、次の順で選ばれます。

1. `MCP_INSPECTOR_SECRET_STORE` が `keyring` / `file` / `memory` に設定されていればそれを使う
2. OS キーチェーン（macOS の Keychain、Windows の Credential Manager、Linux の Secret Service）に届けばそれを使う
3. それ以外はフォールバック: ボリューム未マウントのコンテナでは `memory`、それ以外では `file`

キーチェーンが無いホスト（libsecret や Secret Service の無い Linux、D-Bus セッションの無いヘッドレスサーバーや SSH セッション、Android/Termux）では、何も指定しなくても `~/.mcp-inspector/secrets.json` へ**自動的に**保存され、鍵を与えない限り**暗号化されない**ことが警告されています。対処として、キーチェーンを復活させる（次回起動時にファイルの内容がキーチェーンへ移され、ファイルは削除される）、`MCP_INSPECTOR_SECRET_KEY_FILE`（推奨）または `MCP_INSPECTOR_SECRET_KEY` で鍵を与えて暗号化する（AES-256-GCM、scrypt で鍵を伸長）、`MCP_INSPECTOR_SECRET_STORE=memory` でディスクに書かない、の 3 つが挙げられています。どのトークンを永続化するかは `MCP_INSPECTOR_PERSIST_TOKENS`（`all` / `access` / `none`）で制限できます。使用中のストアは起動時の stderr と、Web クライアントの設定ダイアログのフッターに表示されます。

この変更に合わせ、Authorization ページでは `oauth.json` の説明が「トークンとクライアント情報」から「非機密の OAuth 状態」に改められ、Recipes の Docker 節にはボリュームのマウント有無で保存先が変わること、鍵は環境変数ではなくファイル（Docker / Compose secrets）で渡すべきことが追記されました。

- [Configuration and flags - MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/configuration#where-secrets-are-stored)

## 3. Inspector の Security ページを新設

**Security**（`tools/inspector/security`）のページが新たに追加されました。実際の資格情報を保持し実際のプロセスを起動する開発ツールとして、Inspector が何を守り、何を信頼し、境界がどこにあるかを 1 か所にまとめたもので、設定やレシピのページは理由の説明をこのページに委ねる構成になりました。

- **Web バックエンドと API トークン**: バックエンドは stdio プロセスを起動できるため、`/api/*` は起動ごとのベアラートークンを要求します。ただし `GET /` が返す HTML にはトークンが埋め込まれるため、ページを読めれば誰でもトークンを読めます。トークンの値よりバインドアドレスが重要だと説明しています。`DANGEROUSLY_OMIT_AUTH` は `true` または `1` のときだけ認証を無効化し、非ループバックへのバインドとは決して併用しないよう警告しています。
- **Docker**: コンテナ内では `0.0.0.0` にバインドする必要がありますが、ホスト側でどのインターフェースに公開されるかは `-p` の書き方で決まります。`-p 127.0.0.1:6274:6274` のように `127.0.0.1:` を付けるよう求めています。また、データボリュームをマウントするとシークレットがディスク上のファイルに書かれます。
- **ファイルストアの保護範囲**: 鍵なし・鍵ありのそれぞれで、どの脅威を防げるかを表にしています。暗号化は「ファイルが漏れた」を「ファイル**と**鍵が漏れた」に変えるだけで、root や同一ユーザーで動くコードには無力であり、暗号化しても中程度のリスクとして扱うよう述べています。
- **stdio サーバー**: stdio サーバーはユーザーの権限で動き、`secrets.json` や `oauth.json` を自分で開けるため、環境変数の許可リストは衛生対策であって隔離ではない、としています。
- **mcpdo 接続デーモン**: TCP ポートを持たず、Unix ではモード `0700` のディレクトリ内のソケット、Windows では名前付きパイプで待ち受けます。すべてのリクエストにベアラートークンが必要であること、プライベートモードはセキュリティ境界ではないこと、メモリ上に保持する情報、起動・停止・クラッシュ時の挙動、ディスクに書くファイル（`mcpdod.sock` / `mcpdod.lock` / `mcpdod.token` / `mcpdod.log`）も記載されています。

この追加に合わせて Web client・Configuration and flags・Recipes の関連箇所に Security ページへのリンクが張られました。こちらも `llms-full.txt` に収録された本文は 2026-07-28 版のみです。

- [Security - MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/security#what-the-file-store-protects-against)

## 4. CLI に CI ゲートとカタログ編集を追加

CLI client ページに「CI gates」節が新設され、チェック結果を非ゼロの終了コードに変える 3 つのフラグが説明されています。

- `--strict`（`tools/list` と併用）: ツールスキーマの移植性の問題を stderr に詳しく出力し、エラー重大度の問題があれば終了コード `6` を返す
- `--verify`（`skills/list` / `skills/get` と併用）: SEP-2640 の適合性とダイジェストを検査し、違反があれば `7`、読み取り上限のためすべてのスキルを検査できなければ `8` を返す（上限は `--skill-catalog-max-skills` / `--skill-catalog-max-bytes` で設定）
- `--require-digests`（`--verify` と併用）: ダイジェストを公開していないスキルがあれば `9` を返す

あわせて「Editing the catalog」節が新設され、`servers/add`・`servers/edit`・`servers/remove` で接続せずにカタログを書き換えられるようになりました。Web クライアントのサーバー一覧と同じコードを通るため、`env` 値やクライアントシークレットは UI から保存した場合と同様にシークレットストアへ入ります。書き込めるのは書き込み可能なカタログのみで、`--config` で指定したファイルへの書き込みは拒否されます。

Methods の表には、このほか `resources/directory/read`（`--cursor` で 1 ページずつ）と `skills/list` / `skills/get` も追加されています。

- [CLI client - MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/cli#ci-gates)

## 新規追加されたページ

<!-- light:new-pages:start -->
- [**mcpdo connection client**](#1-mcpdo-接続クライアントを追加) ([MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/mcpdo#quickstart)):  
  一度接続した名前付き接続に対して多数のコマンドを実行できる、実験的な接続クライアント `mcpdo` の解説ページ（詳細はハイライト 1 参照）。
- [**Security**](#3-inspector-の-security-ページを新設) ([MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/security#what-the-file-store-protects-against)):  
  Web バックエンド・Docker・シークレット保存・stdio サーバー・mcpdo デーモンにわたる Inspector の脅威モデルをまとめたページ（詳細はハイライト 3 参照）。
<!-- light:new-pages:end -->

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
- [**Configuration and flags**](#1-configuration-and-flags) ([MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/configuration#where-secrets-are-stored)):  
  シークレットストアの節と環境変数を追加したほか、`--server` や `--` セパレータの扱いがクライアントごとに異なる点を訂正した（追加 126 行・削除 22 行）。
- [**Recipes**](#2-recipes) ([MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/recipes#docker)):  
  Docker 節をループバック公開・データボリュームとシークレット・ヘルスチェックの観点で書き直し、リバースプロキシ配下の MCP Apps 設定と mcpdo の節を追加した（追加 127 行・削除 19 行）。
- [**CLI client**](#3-cli-client) ([MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/cli#exit-codes-and-error-envelopes)):  
  CI ゲートとカタログ編集に加え、`--tool-arg` の型変換規則、エラーエンベロープの項目、`--advertise-apps` などを追記した（追加 66 行・削除 14 行）。
- [**Protocol eras**](#4-protocol-eras) ([MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/protocol-eras#cancellation)):  
  `--protocol-era` フラグ、キャンセルの節を追加し、`Mcp-Param-*` ヘッダーのミラーリングに関する記述を訂正した（追加 41 行・削除 23 行）。
<!-- light:updated-pages:end -->

## 1. Configuration and flags

シークレットストア関連（ハイライト 2 参照）として、「Secret store variables」と「Where secrets are stored」の 2 節が追加されました。そのほか、クライアントごとのフラグの扱いを実態に合わせて訂正・追記しています。

- `--server <name>` で名前付きサーバーを選択できるのは **CLI のみ**。Web クライアントは受理するものの注記を出して無視し、TUI では未定義のため不明なオプションとしてエラーになる（旧記述は「Web と CLI のみ」）
- `--` 以降を対象コマンドの引数として渡すのは **Web と TUI**（旧記述は「Web と CLI」）。CLI は逆で、`--` より**前**が対象、後ろが Inspector 自身のオプションになる
- Web クライアントは、ファイル指定時に `--header` と `--protocol-era` も拒否する
- 共有フラグに `--protocol-era` と `--skill-catalog-max-skills` / `--skill-catalog-max-bytes` を追加。CLI 専用フラグには `--cursor`、`--rename`、`-q` / `--quiet`、`--output`、`--advertise-apps`、`--strict`、`--verify`、`--require-digests`、`--completion`、`--no-revoke` などを追加
- `--callback-url` に使えるループバックホストとして、`127.x.x.x` の任意のアドレスと `[::1]` を明記
- 環境変数の表に「どのクライアントが読むか」を示す列を追加。Web バックエンドの既定バインドホストを `127.0.0.1` とし、`MCP_SANDBOX_PORT` の既定を `6275` と明記。`MCP_APP_ORIGIN_PORT`（既定 `6278`）、`MCP_SANDBOX_FULL_ADDRESS`、`MCP_APP_ORIGIN_FULL_ADDRESS`、`MCP_LOG_FILE`、非推奨の `MCP_PROXY_AUTH_TOKEN` と `SERVER_PORT` を追加
- Web バックエンドが初回起動時に投入するサンプルサーバーを 2 件から 3 件に変更（MCP 公式がホストする Streamable HTTP の example server を追加）

- [Configuration and flags - MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/configuration#shared-server-selection-flags)

## 2. Recipes

Docker 節が大きく書き直されました。

- 例示コマンドを `-p 127.0.0.1:6274:6274` に変更し、`127.0.0.1:` を付けずに公開するとホストのすべてのインターフェースに公開されると警告
- Apps タブを使う場合はサンドボックスのポート `6275`（`_meta.ui.domain` を宣言するアプリでは `6278` も）を同じ番号で公開するよう追記
- 新設の「Keeping your servers and secrets」節で、`/home/node/.mcp-inspector` にボリュームをマウントしないと `--rm` でサーバー一覧・OAuth 状態・シークレットが失われること、マウントするとシークレットがボリューム上の `secrets.json` に書かれ、鍵が無ければ平文になることを説明。鍵は `MCP_INSPECTOR_SECRET_KEY_FILE` で**ファイルとして**渡し（`docker run` と Compose secrets の例を掲載）、`-e MCP_INSPECTOR_SECRET_KEY=…` は `docker inspect` / `docker exec` で読めるため避けるよう求めている
- 新設の「Health checks and other modes」節で、`--cli` / `--tui` 実行時に必要だった `--no-healthcheck` の記述を削除。イメージの `HEALTHCHECK` がこれらのモードを自動判定して正常と報告し、外部のオーケストレーター向けにはトークン不要の `GET /healthz` を使えるとした

「Hosting on a network」節では既定のバインドを `127.0.0.1` と明記し、TLS やリバースプロキシの配下では `MCP_SANDBOX_FULL_ADDRESS` / `MCP_APP_ORIGIN_FULL_ADDRESS` で MCP Apps の公開アドレスを与えるよう追記しました（Inspector と同じオリジンは拒否）。従来の「MCP Apps は TLS では描画できない」という制約は、IPv6 リテラルの制約のみに改められています。このほか、アドホックなターゲットに `--protocol-era` を渡せること、インポート時に既存 ID と衝突した場合は上書き・スキップ・改名を選べること、アプリを持つツールの検査に `--advertise-apps` を付けることが追記され、mcpdo の節（ハイライト 1 参照）が追加されました。

- [Recipes - MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/recipes#docker)

## 3. CLI client

CI ゲートとカタログ編集の追加（ハイライト 4 参照）のほか、次の変更がありました。

- `--tool-arg` の値は JSON として解釈できる場合のみ変換され、解釈できない値（`zip=012` など）は文字列として送られる。その後、文字列はツールの入力スキーマが宣言する型へ変換される。`--tool-args-json` も `key=value` の解析を省くだけでスキーマによる変換は適用される、と記述を訂正
- 終了コード `1` に「シークレットストアや OAuth 状態ファイルを読めない場合」を含めるよう追記し、`6`〜`9` を追加
- エラーエンベロープが `code` / `message` のほか、`cause` / `status` / `url` を持ちうること、URL のクエリ文字列中のシークレットは伏せられること、`code` の取りうる値（`auth_required`、`unreachable`、`tool_not_found`、`schema_unportable`、`store_unavailable` など）を追記
- CLI は App を描画できないため、既定では `initialize` 時に MCP Apps 拡張を宣言しない。App 対応クライアントにだけ App ツールを見せるサーバーを検査するには `--advertise-apps` を付ける
- CLI には `roots/set` メソッドが無い、と記述を訂正（旧記述は「`--method roots/set` はその短命な接続にのみ適用される」）
- `--use-stored-auth` は URL でトークンを引くため `--server-url` が必要
- 冒頭に、同一サーバーへの連続コマンドやセッションをまたぐ操作には mcpdo を勧める案内を追加

- [CLI client - MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/cli#exit-codes-and-error-envelopes)

## 4. Protocol eras

CLI と TUI は、ファイルの `protocolEra` を 1 回の実行に限って `--protocol-era <legacy|auto|modern>` で上書きできるようになりました。テストサーバーの再現手順は、リポジトリのルートから `node test-servers/build/server-composable.js --config ...` で起動し、stderr に表示された URL を使う形に具体化されています（ポートが使用中なら次の空きポートを使うため）。

主な追加・訂正は次のとおりです。

- **Cancellation 節を新設**: legacy 接続では `notifications/cancelled` を送り、modern の Streamable HTTP 接続ではそのリクエストの SSE レスポンスストリームを閉じる（2026-07-28 版のキャンセルシグナル）。stdio では引き続き `notifications/cancelled`
- **`Mcp-Param-*` ヘッダーの訂正**: 旧版の「ブラウザでは SDK がミラーリングを省くため Web クライアントでは `-32020` になる」という警告を削除し、modern 接続では Inspector 自身が 3 クライアントすべてでミラーリングする（Web では Node バックエンドが付与する）と改めた
- **`-32602` エラーパネル**: modern 限定ではなく、どちらの era でも専用パネルで表示するように記述を変更
- **サブスクリプションのストリーム状態**: バッジの状態として `Reconnecting...`・`Stream ended`・`Not acknowledged` を追記
- **Sessions 節**: legacy 接続が `initialize` 後に開くスタンドアロンの `GET` 通知ストリームと、それを抑止する legacy 専用の「Suppress Notification Stream」設定を追記
- MRTR のテストプリセットに `mrtr_empty` を追加

- [Protocol eras - MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/tools/inspector/protocol-eras#cancellation)

## 軽微な更新

<!-- light:minor-updates:start -->
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
<!-- light:minor-updates:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-10-06.md](./archives/latest/2026-10-06.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-10-06.md](./archives/latest-detail/2026-10-06.md)

<!--
base_commit: 4732026713f96a1268695ab6d1e2f0fc2a78d528
head_commit: f7270cc772c15a132c348d04599b3544e0e7722c
generated_at_full: 2026-10-09T15:18:43+09:00
-->
