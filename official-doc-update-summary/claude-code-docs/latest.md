---
対象期間: 2026年09月15日 〜 2026年09月16日
作成日: 2026-09-16
---

# Claude Code 公式ドキュメント更新サマリ

```markdown
前回のサマリは「索引（`llms.txt` と見出しマップ）にだけ現れて本文に届いていない変更が 2 種類ある」と書いて締めました。**今回はその 2 種類が両方とも本文に着地し、加えて前回「本文に 1 回も現れない」と列挙した新規見出し 6 件も全て着地しました。** 差分は 2 ファイル・1,975 行（追加 1,360・削除 615）で、`llms-full.txt` は 96,896 行から 97,637 行へ 741 行増え、**本文が変わったページは 118 / 196**（前回は 48 / 195）と、2 倍以上に広がりました。**直近 7 回のサマリがこの数値を記録している範囲では、最大だった 85 / 191（2026年09月10日）を上回ります。** 広がりの主因は**クラウド用語への改称**で、`Claude Code on the web` という語が **174 か所から 52 か所へ減り**、リファレンス系ページに限れば **134 か所が 6 か所**になっています。一方で `llms.txt` は **1 行も変わらず**（前回は 13 行）、収録 URL は 207 件のままです ―― 索引が先に動いた前回と、本文だけが追いついた今回が、ちょうど対になっています。changelog には **v2.1.273（64 項目）** が 1 リリース積まれました。

主要なものを以下に挙げます。

1. クラウド用語への改称が本文へ一斉に着地し、118 ページが動いた
2. auto モードのネットワーク承認がコマンドごとの許可ドメインに置き換わった
3. 予告されていた 6 見出しが全て着地し、`errors` に 6 節が新設された
4. v2.1.273 が 64 項目で着地した
5. changelog が先に告知していた 3 つの設定が本文に書き下ろされた
```

## ハイライト

1. [**クラウド用語への改称が本文へ一斉に着地し、118 ページが動いた**](./latest-detail.md#1-クラウド用語への改称が本文へ一斉に着地し118-ページが動いた):  
  前回サマリが「`llms.txt` と見出しマップでは改称されたのに、`llms-full.txt` の本文にはこの改称が 1 か所も入っていない」と書いた状態は、**今回の取り込みで解消**しました。`Claude Code on the web` は **174 か所から 52 か所へ**減り、残る 52 か所は **changelog に 33・`whats-new/` の過去ダイジェストに 13**、つまり**書き換えてはいけない過去記録が 46 か所**を占めます。**現行のリファレンス系ページに残るのは 6 か所だけ**（改称前は 134 か所）です。改称は語の置換に留まらず、`claude-code-on-the-web` は**「クラウドセッション」を概念として定義し、ブラウザ・モバイル・デスクトップ・ターミナル・ルーティンの 5 つの起動元を並べる**構成に書き換えられ、用語集にも `Cloud session` の項目が新設されました。
2. [**auto モードのネットワーク承認がコマンドごとの許可ドメインに置き換わった**](./latest-detail.md#2-auto-モードのネットワーク承認がコマンドごとの許可ドメインに置き換わった):  
  サンドボックス内のコマンドが許可リスト外のホストへ接続するとき、auto モードはこれまで**接続のたびに分類器へ問い合わせ、その判定をホスト単位でキャッシュ**していました。**この仕組みの説明は今回まるごと削除され**、代わりに **Claude がコマンド自身に必要なホストを書き添え、分類器がコマンドと一緒に 1 回で審査する**方式（`Per-command allowed domains in auto mode`）になりました。**承認されたリストはそのコマンド 1 回限りで、セッションの許可ホストにも設定にも何も残りません。** 許可ルールで承認済みのコマンドでも、ホストを伴えば分類器へ回されます。あわせて **Bedrock・Google Cloud's Agent Platform・Microsoft Foundry では、プラットフォーム側のサーバー分類器に任せる挙動が既定から外れ**、`CLAUDE_CODE_AUTO_MODE_SERVER=1` のオプトインになりました（**v2.1.271 と v2.1.272 の 2 リリースだけが既定だった**と明記されています）。
3. [**予告されていた 6 見出しが全て着地し、`errors` に 6 節が新設された**](./latest-detail.md#3-予告されていた-6-見出しが全て着地しerrors-に-6-節が新設された):  
  前回サマリが「見出しマップに載ったが本文に 1 回も現れない」と列挙した **6 見出しは、今回 6 件とも本文に着地**しました。**予告から着地までの間隔は 1 日**で、**3 回連続で翌日の取り込みで解消**したことになります。着地先で最も重いのが **`errors`（144 行・追加 129／削除 15）** で、**6 つの節が一度に新設**されました ―― 組織ポリシーによるクラウドセッションの無効化、OAuth リダイレクト用ポートの枯渇、GitHub 未接続、エージェントチームのチームメイト定義が復元されなかった場合、Cowork セッションでの接続外ファイル読み取り、`WebFetch` が localhost を取得できない件です。エラー索引表にも 9 行が追加されました。
4. [**v2.1.273 が 64 項目で着地した**](./latest-detail.md#4-v21273-が-64-項目で着地した):  
  changelog に **v2.1.273（2026年09月15日）が 1 リリースだけ**追加され、67 行増えました。**64 項目の内訳は修正 35・改善 16・変更 6・追加 4・差し戻し 1・削除 1・Windows 個別 1** です。セクションタグ付きは **`[Claude Tag]` 10・`[Claude Code on the web]` 6・`[Code Review]` 6・`[VSCode]` 2** の計 24 件で、残る 40 件が CLI 本体です。**差し戻されたのは v2.1.268 の変更**で、権限チェッカが解析できない Bash 行（`eval`、`env -C`）に Read / Edit の拒否ルールを適用していたものが撤回され、`time -p make build` のようなコマンドは**拒否ではなく再びプロンプト**に戻りました。
5. [**changelog が先に告知していた 3 つの設定が本文に書き下ろされた**](./latest-detail.md#5-changelog-が先に告知していた-3-つの設定が本文に書き下ろされた):  
  `bashEditDiffEnabled`・`gatewayInternalNetworks`・`--remove-session-state` の 3 つは、**前回時点では changelog に 1 行ずつ載っているだけ**で、リファレンスページに項目がありませんでした。今回**3 つとも本文に書き下ろされ**、`bashEditDiffEnabled` は **Bash コマンドが変更したファイルを PostToolUse フックが `tool_response.bashEditDiff` で受け取れる**仕組みとして `hooks` に 1 節ぶん、`gatewayInternalNetworks` は **自社保有のパブリック IPv4 空間にゲートウェイを置く**ための節として `claude-apps-gateway` に、`--remove-session-state` はセルフホストランナーのフラグ表に、それぞれ加わりました。**`bashEditDiff` は公開ベータで、取りこぼしも他プロセスの変更の混入もありうると明記**されています。

## 新規追加されたページ

- [**Agent SDK の設定オプションが 1 ページにまとまった**](./latest-detail.md#1-agent-sdk-の設定オプションが-1-ページにまとまった) ([English](https://code.claude.com/docs/en/agent-sdk/configuration)):  
  前回サマリが「`llms.txt` に登録され見出しマップに 9 見出しが載ったのに、本文は `llms-full.txt` に 1 行もない」と書いた `agent-sdk/configuration` が、**今回 292 行の本文ごと着地**しました。**今回の差分で最大の単一追加**で、`options` オブジェクトの組み立て方、設定ファイルの読み込み、モデル選択とフォールバック、環境変数、作業ディレクトリ、ターン数と予算の上限、セッション実行中の設定変更を **9 つの h2** に整理し、個別機能は各ページへ送る「入口ページ」の作りになっています

## 大幅に更新されたページ

- [**クラウドとローカルの比較表が 2 列に再編された**](./latest-detail.md#1-クラウドとローカルの比較表が-2-列に再編された) ([English](https://code.claude.com/docs/en/web-quickstart#compare-ways-to-run-claude-code)):  
  `web-quickstart` は **50 行（追加 28・削除 22）**動きました。中心は比較表で、**「On the web / Remote Control / Terminal CLI / Desktop app」という 4 サーフェスの列が「クラウドセッション / ローカルセッション」の 2 列へ**まとめ直され、**「どこから起動するか」という行が新設**されています。ハイライト 1 の改称を、表の構造まで含めて反映した形です
- [**Agent SDK Python リファレンスの変更は実質 2 か所だけだった**](./latest-detail.md#2-agent-sdk-python-リファレンスの変更は実質-2-か所だけだった) ([English](https://code.claude.com/docs/en/agent-sdk/python#claudeagentoptions)):  
  `agent-sdk/python` は **126 行（追加 63・削除 63）**動き、**新規ページを除けば `errors` に次ぐ規模**ですが、**表の桁揃えを除くと実質 24 行**、内容の変更は 2 か所だけです。`set_model(None)` の戻り先が「デフォルト」から「**Claude Code の既定モデル**」へ、`input_schema` の説明が「（下記参照）」から**該当セクションへの明示リンク**へ変わりました
- [**Agent SDK TypeScript リファレンスも桁揃えが大半を占めた**](./latest-detail.md#3-agent-sdk-typescript-リファレンスも桁揃えが大半を占めた) ([English](https://code.claude.com/docs/en/agent-sdk/typescript#applyflagsettings)):  
  `agent-sdk/typescript` は **56 行（追加 28・削除 28）**動き、**桁揃えを除くと 28 行**です。内容としては `setModel()` の戻り先が Python 側と同じく「Claude Code の既定モデル」に統一され、**`applyFlagSettings()` に `null` を渡したときの説明が「下位ソースへフォールバックする」から「ほとんどのキーは下位ソースへ落ちる」へ緩められました**

## 軽微な更新

今回の差分は **2 ファイル・1,975 行**（追加 1,360・削除 615）です。内訳は `llms-full.txt` が 1,969 行（追加 1,355・削除 614）、見出しマップ（`en/claude_code_docs_map.md`）が 6 行（追加 5・削除 1）で、**`llms.txt` は 1 行も変わっていません**（前回は 13 行）。`llms-full.txt` の総行数は **96,896 行から 97,637 行へ 741 行増え**、展開ページ数は **195 から 196**、**本文が変わったページは 118 / 196**（前回は 48 / 195）でした。

**今回 changelog に積まれたリリースは v2.1.273（2026年09月15日・64 項目）の 1 本だけ**なので、以下のうち changelog 由来の項目はすべて v2.1.273 のものです。ただし**本文に書き下ろされた項目には、v2.1.268〜v2.1.271 で既に告知済みだったものが多く含まれます**（必要バージョンは各項目に併記しています）。**本文側に対応記述が見つからない項目にはリンクを付けていません**（changelog ページの URL は方針どおり使いません）。

**新機能**

- **サブエージェントの最終報告を届ける `SubagentHandback` ツールが本文に書き下ろされました**。**auto モードでのみ、Agent ツールがローカルで動かすサブエージェント（フォークを除く）に提供**され、ターミナル CLI・IDE 拡張・クラウドセッション等で使えます。**`tools` に書いていなくても、`disallowedTools` に入れていても、条件が揃えば Claude Code が付与**します。フックから報告本文を読むには `PreToolUse` / `PostToolUse` を `SubagentHandback` にマッチさせて `tool_input.message` を見ます。**Claude Code v2.1.271 以降** — [Tools reference](https://code.claude.com/docs/en/tools-reference#agent-tool-behavior) / [Hooks reference](https://code.claude.com/docs/en/hooks#posttooluse)
- **auto モードでコマンドごとに許可ドメインを添えられるようになりました**（詳細はハイライト 2 参照）— [Configure the sandboxed Bash tool](https://code.claude.com/docs/en/sandboxing#per-command-allowed-domains-in-auto-mode)
- **Bedrock・Google Cloud's Agent Platform・Microsoft Foundry で、プラットフォーム側のサーバー分類器に auto モードの審査を任せる `CLAUDE_CODE_AUTO_MODE_SERVER=1` が説明されました**（詳細はハイライト 2 参照）— [Permission modes](https://code.claude.com/docs/en/permission-modes#server-side-classifier-review)
- **Bash コマンドが変更したファイルを PostToolUse フックが受け取れるようになりました**（`bashEditDiffEnabled` / `CLAUDE_CODE_BASH_EDIT_DIFF`・詳細はハイライト 5 参照）— [Hooks reference](https://code.claude.com/docs/en/hooks#bash)
- **自社保有のパブリック IPv4 ブロックにゲートウェイを置けるようになりました**（`gatewayInternalNetworks`・詳細はハイライト 5 参照）— [Claude apps gateway](https://code.claude.com/docs/en/claude-apps-gateway#allow-a-gateway-on-public-address-space-you-own)
- **セルフホストランナーに `--remove-session-state` が加わりました**（既定オフ）。**結果に関わらず、セッション終了時に `<base-dir>/_sessions/` 配下のセッション別ディレクトリを削除**します — [Self-hosted environments reference](https://code.claude.com/docs/en/self-hosted-environments-reference#runner-cli-flags)
- **LLM ゲートウェイ向けのヒントヘッダーが 5 つ加わりました**。`x-claude-code-request-class`・`x-claude-code-agent-type`・`x-claude-code-prev-tool-durations`・`x-claude-code-compaction`・`x-claude-code-context-compacted` で、**`CLAUDE_CODE_GATEWAY_HINT_HEADERS=1` でのオプトイン**です
- **MCP サーバーがセッション中に切断され、自動再接続を諦めたときに通知が出るようになりました**。`/mcp` へ誘導します
- **`claude --remote-control` や `/remote-control` で開始したセッションを Claude アプリからフォークできるようになりました**。フォークは**自分のコンピュータ上のバックグラウンドセッションとして動きます**
- **ルーティンの新規作成ページと編集ダイアログに「Discard unsaved changes?」の確認が入りました**（`[Claude Code on the web]`）

**機能改善**

- **`SessionStart` フックの待ち合わせの説明が書き換わりました**。**対話セッションの起動時、`--continue` / `--resume` での起動時再開、`/clear` ではフックがバックグラウンドで走り、すぐ入力でき、再開した会話はフックを待たずに表示されます**。一方**セッション内で `/resume` して会話を切り替える場合はフックの完了を待ちます**。バックグラウンド実行中に `/clear` や会話切り替えをした場合、**フックの戻り値はそのセッションに適用されません** — [Hooks reference](https://code.claude.com/docs/en/hooks#sessionstart)
- **`SessionEnd` フックのタイムアウトの説明が 2 つの手段に整理されました**。`CLAUDE_CODE_SESSIONEND_HOOKS_TIMEOUT_MS` は**全体予算だけでなく、自前の `timeout` を持たない各フックのタイムアウトにもなります**。**v2.1.268 より前は全体予算しか上がらず、自前の `timeout` の無いフックは 1.5 秒で打ち切られていました**。逆に per-hook の `timeout` で予算を上げた場合は、**自前の `timeout` が無いフックは既定のままです** — [Hooks reference](https://code.claude.com/docs/en/hooks#sessionend) / [Environment variables](https://code.claude.com/docs/en/env-vars)
- **`tee` が Read / Edit ルールの検査対象に加わりました**。**`make | tee build.log` のようなパイプラインでも書き込み先を検査**し、`Edit` の許可・拒否ルール、保護パス、作業ディレクトリが効きます。**`Bash(tee *)` のような許可ルールがあっても検査は外れません** — [Manage permissions](https://code.claude.com/docs/en/permissions#redirections)
- **`!` で始まる拒否・確認パターン（gitignore 記法の否定）の仕様が書き下ろされました**。**同じ設定ファイル内の先行ルールからパスを切り出す**もので、**別ソースのルールには届きません**（プロジェクト設定の `Read(!.env)` は管理設定の `Read(./.env)` を取り消せない）。制限も 2 つ明記され、**`/`・`~/`・`//` が続いても `!` パターンは常にカレントディレクトリ基準で読まれる**ため `Read(!~/notes/public/**)` は `Read(~/notes/**)` から何も切り出せず、**ディレクトリごと塞いだルールの内側のファイルを開け直すこともできません** — [Manage permissions](https://code.claude.com/docs/en/permissions#read-and-edit)
- **サンドボックスの OS レベル強制の対象が「Bash コマンド」から「Bash・PowerShell・Monitor の各コマンドとその子プロセス」へ広がりました** — [Configure the sandboxed Bash tool](https://code.claude.com/docs/en/sandboxing#how-sandboxing-relates-to-permissions-and-permission-modes)
- **`bypassPermissions` とプランモードの緩和が「対話ターミナルのセッション」に限定されました**。`permission-modes` の複数箇所に「interactive terminal」という限定が入り、**`-p` の非対話実行・Agent SDK セッション・VS Code 拡張のチャットパネルでは、プランモードのブロックがそのまま効く**と新しい段落で明記されています — [Permission modes](https://code.claude.com/docs/en/permission-modes#skip-all-checks-with-bypasspermissions-mode)
- **サブエージェントの帰り検査の説明が具体化されました**。従来は「完了時に分類器が全アクション履歴をレビューし、懸念があれば結果の先頭に警告を付ける」でしたが、**親が報告を読む前に作業と最終報告の両方をレビューする**ことが明示され、**分類器が利用できなかった場合は「作業を検証してから使うように」という注記付きで報告が届く**という分岐が加わりました — [Permission modes](https://code.claude.com/docs/en/permission-modes#eliminate-permission-prompts-with-auto-mode) / [Create custom subagents](https://code.claude.com/docs/en/sub-agents#permission-modes)
- **入れ子サブエージェントの待ち合わせが対話／非対話で書き分けられました**。**対話セッションではバックグラウンドのサブエージェントを起こした親が、その結果を待ってから終了**します — [Create custom subagents](https://code.claude.com/docs/en/sub-agents#let-subagents-spawn-their-own-subagents)
- **Agent SDK のフックコールバックがタイムアウトしたときの挙動が書き分けられました**。**`Stop` / `SubagentStop` は「判断なしを返した」扱いになり、他のフックの判断は依然として効きます**。**`SessionStart` は「出力なし」扱い**で、他の `SessionStart` フックの出力でセッションが続きます。**メインセッションで `Stop` か `SessionStart` が初めてタイムアウトしたときは、`SDKInformationalMessage` がメッセージストリームに追加されます** — [Agent SDK hooks](https://code.claude.com/docs/en/agent-sdk/hooks#hook-timeout)
- **`agent-sdk/session-storage` が特定プロダクト名から一般化されました**。「S3、Redis、または独自バックエンド」という導入が「**独自のオブジェクトストア、キーバリューストア、またはデータベース**」になり、参考実装の表も**アダプタ名の列からストレージ種別の列へ組み替え**られて、**Python 側の参考実装へのリンクが併記**されました — [Session storage](https://code.claude.com/docs/en/agent-sdk/session-storage#reference-implementations)
- **MCP の変数展開の説明が 5 つの小見出しに分割されました**。`Supported syntax`・`Expansion locations`・`Example with variable expansion` が太字ラベルから h4 に格上げされ、**`Unset variables without a default` と `How references appear in /mcp and CLI output` の 2 節が新設**されています。後者では、**ローカル・プロジェクト・ユーザースコープのサーバーは `/mcp` 詳細表示と `claude mcp list` / `get` で `${VAR}` を解決値ではなく名前のまま見せる**（`/mcp` 詳細表示は **v2.1.268 以降**）ことと、**`managedMcpServers` 由来のサーバーは URL のホストだけを見せる**ことが書かれました — [Connect Claude Code to tools via MCP](https://code.claude.com/docs/en/mcp#how-references-appear-in-mcp-and-cli-output)
- **MCP のサインイン要求通知が繰り返さなくなりました**。**各サーバーについて 1 度だけ告知し、以後の起動では、そのサーバーが一度接続してから再びサインインを要するまで件数から外れます**。`/mcp` は従来どおり全件を並べます — [Connect Claude Code to tools via MCP](https://code.claude.com/docs/en/mcp#authenticate-with-remote-mcp-servers)
- **圧縮直後のファイル再読み込みとパススコープルールの説明が分離されました**。**5,000 トークンを超えるファイルは内容なしのパス参照として戻り、`Read` ではなく `Referenced file` と表示される**ことが明示され、**圧縮を越えて残したいルールは `paths:` frontmatter を外すかプロジェクトルートの CLAUDE.md へ移す**という助言が加わりました — [Manage the context window](https://code.claude.com/docs/en/context-window#what-survives-compaction)
- **`/usage-credits` の案内に再起動が加わりました**。1M コンテキストのエラーメッセージが「**有効化は Claude Code の再起動後に効く**」と述べるようになり、**再起動するまでセッションは標準コンテキストの上限のまま**だと明記されました。**v2.1.268 より前のメッセージには再起動の言及がありません** — [Errors and troubleshooting](https://code.claude.com/docs/en/errors#usage-credits-required-for-1m-context)
- **管理者がモデルを無効化したときの置換通知が、セッション途中でも出ると明記されました** — [Errors and troubleshooting](https://code.claude.com/docs/en/errors#model-is-restricted-by-your-organizations-settings)
- **`origin/HEAD` が無い場合の説明が箇条書きに組み替えられました**。単一ブランチ／CI チェックアウト、誰もプッシュしていないブランチを指すサーバー側 HEAD、`origin` リモートが無いか一度も fetch していないリポジトリ、の 3 通りに分かれています — [Errors and troubleshooting](https://code.claude.com/docs/en/errors#security-review-fails-without-originhead)
- **プラグインの既定コンポーネント配置の例が増えました**。「`skills/` や `commands/` などのフォルダ」から「**`skills/` フォルダ、`monitors/monitors.json` ファイル、プラグインルートの `SKILL.md`**」へ — [Errors and troubleshooting](https://code.claude.com/docs/en/errors#path-could-not-be-checked)
- **`/schedule` が隠れる条件の説明が整理されました**。**`Unknown command` を返すのが既定で、別の応答を返すケースだけを注記する**書き方になり、`/schedule` の認証エラーを扱っていた見出しが 1 件削除されました — [Routines](https://code.claude.com/docs/en/routines#schedule-returns-unknown-command)
- **`REVIEW.md` の説明が簡潔になり、指摘の却下方法が加わりました**。**コード変更なしで指摘を却下するにはスレッドを解決する**（返信しても却下にならない）ことが明示されています — [Code review](https://code.claude.com/docs/en/code-review#reviewmd)
- **Agent SDK の `allowDangerouslySkipPermissions` とプランモードの併用が説明されました**。**併用してもファイル編集とファイルを変えるシェルコマンドは `canUseTool` コールバックに届き**、後から `setPermissionMode()` で `bypassPermissions` に切り替えられるようになるだけ、という位置づけです — [Agent SDK permissions](https://code.claude.com/docs/en/agent-sdk/permissions)
- **`agent-view` に v2.1.268 の `←` キーの挙動が追記されました**。最初の `←` の後、**1 秒以上あけた次の押下でエージェント一覧に切り替わります** — [Agent view](https://code.claude.com/docs/en/agent-view#switch-sessions-without-leaving-the-terminal)
- **プラグインの `defaultEnabled` の説明で、優先されるものが「2 つ」から「ユーザーの設定と依存関係の要求」へ具体化されました** — [Plugins reference](https://code.claude.com/docs/en/plugins-reference#plugin-manifest-schema)
- **自動修正・エラーメッセージまわりの改善が多数入りました**。IP 許可リスト・停止中のアプリインストール・SAML SSO によるクラウドセッションの GitHub エラーが原因を示すようになり、`/autofix-pr` が `gh` 自身のエラーと webhook 設定失敗の理由を出すようになり、`/web-setup` が拒否されたトークンの理由とプロキシ・TLS 証明書の問題を名指しするようになりました。SSL 証明書とプロキシの接続エラーも**エラーコードと直すべき対象（社内 CA なら `NODE_EXTRA_CA_CERTS` など）を示す**ようになっています
- **Artifact ツールの挙動が 4 点改善されました**。配信されないファイル種別を含む公開時のエラーが**配信される種別と代替手段を Claude に伝える**ようになり、ページ読み取りが**そのページに対して artifact サービスが持つ機能とデータベース規則を示す**ようになり、**更新でドキュメント全体を書き直さず 1 フィールドだけ削除できる**ようになり、**claude.ai に到達した後で接続が切れた公開は安全に再送される**ようになりました
- **長いセッションの応答性が改善されました**。**フックの進捗とサブエージェントの動きが、更新のたびに会話全体を処理し直さなくなりました**
- **`OTEL_LOG_TOOL_DETAILS=1` が、コストとトークンのメトリクスにも実際のエージェント名・スキル名・プラグイン名・MCP サーバー名を含めるようになりました**
- **`/bug` と `/feedback` の送信内容が絞られました**。直前の API リクエストから**モデル挙動に関わるパラメータ（モデル・システムプロンプト・ツール）だけ**を含め、リクエストメタデータと `CLAUDE_CODE_EXTRA_BODY` のフィールドは外します
- **Claude アカウントでのサインインが、claude.ai のプラグインへのアクセスも要求するようになりました**（見出しマップに `syncClaudeAiPlugins` 設定が現れたのと対応します）

**バグ修正**

- **v2.1.273 の 35 件の修正項目のうち、本文ページに対応する記述を持つものはごく一部です**（大半は changelog にしか現れません）。対応が確認できたものを以下に挙げます。
- **`permissions.blockReadsOutsideWorkingDirectories` が有効なとき、権限チェッカが完全に解析できない Bash コマンドがプロンプトを飛ばす問題が修正されました**。**ディレクトリを 2 回以上変えるコマンドやサブシェルを走らせるコマンドは、作業ディレクトリ外のパスを名指ししていなくてもプロンプトを出します**（サンドボックス内でサンドボックスがブロックを強制する場合を除く）— [Permission modes](https://code.claude.com/docs/en/permission-modes#eliminate-permission-prompts-with-auto-mode) / [All settings](https://code.claude.com/docs/en/settings-reference#permissionsblockreadsoutsideworkingdirectories)
- **サブエージェントとバックグラウンドエージェントが、最終ストリーム応答にトークン使用量やモデル ID が無いというだけで「失敗」と報告され、結果が届かなくなる問題が修正されました**（本文側に対応する記述はありません）
- **MDM や `managed-settings.json` で設定した `allowManagedMcpServersOnly` / `deniedMcpServers` / `disableClaudeAiConnectors` が、サーバー管理設定も同時に存在するときに無視される問題が修正されました**（`managed-mcp` ページの本文は今回 `Claude.ai` → `claude.ai` の表記統一 1 行しか動いていないため、リンクは付けていません）
- **コンテキストメーターと自動圧縮が、advisor ツールのターンを実際の約 2 倍のコンテキストサイズで数えていた問題が修正されました**。自動圧縮が実質的な上限の約半分で発火していました
- **`.claude/scheduled_tasks.json` を別フォルダ（新しい worktree など）へコピーすると、保存済みスケジュールタスクが違うセッションで走る問題が修正されました**（`scheduled-tasks` ページの本文は今回 1 行の言い換えのみで、この修正には触れていません）

**その他**

- **前回サマリの記載を 3 件訂正しました**。前回「本文に現れない新規見出し」として挙げた 6 件のうち、`Permission checks on injected commands`・`Teammate's agent definition was not restored`・`WebFetch cannot fetch localhost` の掲載ページを `permissions` / `agent-teams` / `tools-reference` と書きましたが、**見出しマップ上の掲載ページは base の時点から `skills` / `errors` / `errors`** でした（詳細はハイライト 3 参照）
- **見出しマップに新しい「索引だけ先行」が 4 件積まれました**。**`settings-reference` の `syncClaudeAiPlugins`**、**`agent-sdk/python` の `SystemPromptCustom`**、**`agent-sdk/modifying-system-prompts` の `Update Claude's instructions mid-session` と `Turn recording off while you iterate on wording`** です。**いずれも `llms-full.txt` の本文には 1 回も現れません。** `syncClaudeAiPlugins` は v2.1.273 の「サインインが claude.ai のプラグインへのアクセスも要求する」項目と対応して読めますが、本文が未着のため内容は確認できません
- **見出しマップ先頭の自動生成スタンプが 2026年09月15日 23時28分38秒 UTC から 2026年09月16日 19時54分20秒 UTC へ**進みました。約 20 時間ぶんです
- **`llms.txt` は 1 行も変わりませんでした**。収録 URL は 207 件のままで、**前回 1 件登録された `agent-sdk/configuration` の本文が今回届いた**ことで、索引と本文の件数差が解消しています
- **プランモードとサンドボックスの相互作用の但し書きが一般化されました**。「プランモードという 1 つの例外を除いて」という書き方が、「**`Sandbox modes` に列挙された例外を除いて**」へ変わり、コマンドごとの許可ドメインを伴うコマンドが 2 つ目の例外として加わりました — [Permission modes](https://code.claude.com/docs/en/permission-modes#eliminate-permission-prompts-with-auto-mode)
- **重なるサンドボックス読み取りルールの説明が言い換えられました**。「より具体的なパスが勝つ」から「**より狭いパスのルールが適用される**」へ — [Configure the sandboxed Bash tool](https://code.claude.com/docs/en/sandboxing#filesystem-isolation)
- **細かな字句修正が 50 ページ以上に広く入りました**。`Claude.ai` → `claude.ai`（表記統一・46 → 28 か所）、`bash` → `Bash` と `zsh` → `Zsh`（`checkpointing`・`jetbrains`・`troubleshoot-install`）、`Navigate to` → `Go to`（`amazon-bedrock`・`google-vertex-ai`・`microsoft-foundry`・`slack`）、`lands in` → `appears in` / `is written to`（`goal`・`claude-directory`・`workflows`）、「the example above」→ 具体名（`agent-sdk/custom-tools`・`plugin-dependencies`・`discover-plugins`）などです。**1 ページあたり 1〜2 行の書き換えが大半で、118 ページのうち 37 ページは変更が 2 行以下**でした
- **`agent-sdk/hosting` と `agent-sdk/session-storage` のコード例コメントから S3 / Redis / Postgres の具体名が外れました**。「オブジェクトストア、キーバリューストア、データベース、または独自アダプタ」という一般的な表現になっています

**参考リンクについて**: **今回は日本語リンクを 1 つも付けていません。** 作成時点で公開中の日本語版を実際に取得して確認した結果、**今回の変更内容はいずれも未反映**でした。確認したのは次の 6 ページです ―― `claude-code-on-the-web`（H1 が「ウェブ上の Claude Code を使用する」のままで、見出しも `#move-tasks-between-web-and-terminal` の旧表記。クラウドセッションの 5 つの起動元を並べる箇条書きも無い）・`sandboxing`（`Per-command allowed domains in auto mode` に相当する節が無く、OS レベル強制の対象も「すべての Bash コマンドとその子プロセス」のまま）・`errors`（新設された 6 節がいずれも存在しない）・`hooks`（`bashEditDiff` / `bashEditDiffEnabled` の語が無い）・`settings-reference`（`bashEditDiffEnabled` と `gatewayInternalNetworks` の項目が無い）・`agent-sdk/configuration`（**日本語版は HTTP 404 で存在しない**）。今回の本文変更はすべて 2026年09月16日 の断面のもので、日本語版の追従はまだ届いていないと判断しました。**changelog ページへのリンクは本サマリの方針どおり付けていません。**

## 新着情報

- [**新着情報の索引ページ**](./latest-detail.md#新着情報の索引ページ) ([English](https://code.claude.com/docs/en/whats-new/index)):  
  **今回 `whats-new/` 配下で動いたのは 3 ページで、いずれも 1 行の字句修正だけ**です。索引ページでは **Week 33（2026年08月10日～14日）のダイジェスト要約 1 行**が書き換わり、フォークモードの説明が「サイドタスクを subagent に **hand**（渡す）」から「**delegate**（委譲する）」に変わりました。**新しい週のダイジェストの追加はありません**
- [**2026年05月11日～15日(Week 20)**](./latest-detail.md#2026年05月11日15日week-20) ([English](https://code.claude.com/docs/en/whats-new/2026-w20)):  
  過去ダイジェストの 1 行が、**`Claude.ai` から `claude.ai` への表記統一**に合わせて書き換わりました。内容（API キー設定時に Remote Control・`/schedule`・MCP コネクタ・通知設定が無効になる件）に変更はありません
- [**2026年03月30日～04月03日(Week 14)**](./latest-detail.md#2026年03月30日04月03日week-14) ([English](https://code.claude.com/docs/en/whats-new/2026-w14)):  
  同じく過去ダイジェストの 1 行で、`disableSkillShellExecution` の説明にある「**slash commands**」が「**custom commands**」へ書き換わりました

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-09-15.md](./archives/latest/2026-09-15.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-09-15.md](./archives/latest-detail/2026-09-15.md)

<!--
base_commit: ebe595356470a094a294bd32d86870726c81d33b
head_commit: fa697d25e355bcd2486c2c9abb1263f94646b401
generated_at_full: 2026-09-17T15:00:23+09:00
-->
