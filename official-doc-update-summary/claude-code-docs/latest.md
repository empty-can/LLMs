---
対象期間: 2026年09月09日 〜 2026年09月10日
作成日: 2026-09-10
---

# Claude Code 公式ドキュメント更新サマリ

```markdown
前回が「持ち越し 40 件を新たに積んだ回」だったのに対し、今回はその**持ち越しが 1 件残らず本文として届いた回**です。差分は 2 ファイル・2,929 行、本文が変わったページは 85 / 191 で、前回（33 / 191・481 行）の約 6 倍にあたる今期最大級の回でした。`llms-full.txt` は 93,952 行から 95,128 行へ 1,176 行増えています。中心にあるのは**システムプロンプトを会話の最初に「記録」して以後それを使い回す仕組み**で、出力スタイルの変更がキャッシュを壊さなくなったのも、v2.1.267 の再開まわりの修正が並ぶのも、すべてこの仕組みの話です。ページの新規追加・削除はなく、`whats-new/` は 8 回連続で差分がありません。

主要なものを以下に挙げます。

1. システムプロンプトの「記録」が明文化され、出力スタイルの変更が再びキャッシュを保つ側へ移った
2. エラーリファレンスに 16 節が一挙に到着し、今回最大の更新（実質 430 行）になった
3. `managedMcpServers` が Claude Code に開かれ、前回「本文未着」と書いた 9 節がすべて埋まった
4. `maxEffortLevel` が追加され、組織がどのプロバイダーでも努力レベルに上限をかけられるようになった
5. v2.1.267 が 53 項目の大型リリースとして載り、再開・再接続まわりのキャッシュ修正がその中心を占めた
```

## ハイライト

1. [**システムプロンプトの「記録」が明文化され、出力スタイルの変更がキャッシュを保つ側へ戻った**](./latest-detail.md#1-システムプロンプトの記録が明文化され出力スタイルの変更がキャッシュを保つ側へ戻った):  
  **Claude Code は会話の最初のリクエストでシステムプロンプトを組み立て、それをセッションに記録して以後のリクエストで使い回す** ―― この仕組みが今回 CLI リファレンスと Agent SDK に新設節として書き下ろされ、`--system-prompt-snapshot` という 5 つ目のシステムプロンプトフラグも表に載りました。波及として、**前回「キャッシュを無効にする」側へ移ったと報告した出力スタイルの変更が、今回は再び「キャッシュを保持する」側へ戻っています**。記録済みのシステムプロンプトを持つ会話（claude.ai / Console アカウントでサインインしたセッションの既定）では、新しいスタイルの指示が**会話中のメッセージとして届く**ため、システムプロンプトも過去の会話もキャッシュから読めます。ただし **Amazon Bedrock・Google Cloud の Agent Platform・Microsoft Foundry のようにフィーチャーフラグを取得しないセッションでは従来どおり全損**です。
2. [**エラーリファレンスに 16 節が一挙に到着した**](./latest-detail.md#2-エラーリファレンスに-16-節が一挙に到着した):  
  前回の持ち越し 40 件のうち最大の塊だったエラーリファレンスの 16 見出しが、**すべて本文とともに到着**しました。**実質 430 行（追加 406・削除 24）で今回最大の更新**です。認証・ゲートウェイ系 4 件、モデル系 3 件、設定・MCP 系 5 件、プラグイン系 2 件、管理設定・サンドボックス系 2 件で、**多くが「このバージョンより前はこう振る舞った」という版境界つき**です。エラーメッセージ索引表にも 28 行が追加され、`Model not found` や `Couldn't save it as your default` のように **v2.1.265 の修正項目と対応が付く項目**も本文が埋まりました。
3. [**`managedMcpServers` が Claude Code に開かれた**](./latest-detail.md#3-managedmcpservers-が-claude-code-に開かれた):  
  前回ハイライト 5 で「見出しだけ届いて本文は 1 行も無い」と報告した組織の MCP 制御ページの 9 節が、**全部本文として届きました**。管理設定に `managedMcpServers` を書けば、**排他的制御を取らずに全ユーザーへリモート MCP サーバーを配れます**（ユーザー自身のサーバーは残る）。**前回引用した「グループ単位で Claude Code クライアントへ MCP サーバーを配布することはできない」という Claude apps gateway 側の制限文は、今回の差分で丸ごと置き換わりました** ―― ゲートウェイは `cli` ブロックの `managedMcpServers` を受け付け、`.mcp.json` の綴り `mcpServers` を拒否するときは正しいキー名を案内します。**本サマリで今回唯一、日本語版も追従済みのページ**です。
4. [**`maxEffortLevel` で組織が努力レベルに上限をかけられるようになった**](./latest-detail.md#4-maxeffortlevel-で組織が努力レベルに上限をかけられるようになった):  
  v2.1.267 の新設定 `maxEffortLevel` は、`/effort`・`/model` ピッカー・`--effort`・環境変数・モデル既定のどれで指定された努力レベルも上限で頭打ちにします。**Claude Code がリクエストごとにクライアント側で適用するため、Amazon Bedrock・Agent Platform・Microsoft Foundry を含むすべてのプロバイダーで効きます**。複数スコープが上限を設けたときは**最も低いものが適用され**、あるスコープの上限を別のスコープから引き上げることはできません。**`ultracode` も上限が `xhigh` 未満なら上限側で走り、ultracode 自体はオフのまま**になります。あわせて努力レベルの操作体系が整理され、`/effort` スライダーの **`s` は「このセッションのみ」、`Enter` は「既定として保存」**と明記されました。
5. [**v2.1.267 の 53 項目は再開・再接続まわりのキャッシュ修正が中心**](./latest-detail.md#5-v21267-の-53-項目は再開再接続まわりのキャッシュ修正が中心):  
  changelog に **56 行が追加され、すべてが v2.1.267（2026年09月09日）の 53 項目**です。内訳は Fixed 28・Improved 7・Added 2 と、VS Code 8・Claude Code on the web 2・Claude Tag 4 の接頭辞付き。**目立つのはプロンプトキャッシュの安定化で 6 項目**あり、そのほとんどが**セッション再開時に接頭辞が書き換わる経路**を潰すものです ―― MCP コネクタの再接続タイミングのずれ、ツール説明の再描画、`-p` 会話を対話的に再開したときのシステムプロンプト変化など。**`ToolSearch` の無いセッションでセッション途中の MCP / プラグインツールを deferred 定義として渡す**ようになった点も、同じ狙いの変更です。

## 新規追加されたページ

（今回の対象期間に新規追加・削除されたドキュメントページはありません。`llms.txt` はまったく変化がなく、収録 URL は 202 件・全体 355 行のままです。`llms-full.txt` の展開ページ数も 191 で動いていません。**変化はすべて既存 85 ページの本文と、見出しマップの 9 行に収まっています**。なお**見出しだけ届いて本文が未着の持ち越しが今回も 6 件あります**。詳細は「軽微な更新」を参照してください）

## 大幅に更新されたページ

- [**エラーリファレンス**](./latest-detail.md#1-エラーリファレンス) ([English](https://code.claude.com/docs/en/errors#administrator-policy-requires-a-cloud-gateway-sign-in)):  
  前回の持ち越し 16 見出しがすべて本文とともに到着し、**実質 430 行（追加 406・削除 24）で今回最大**。索引表にも 28 行が加わった。内容はハイライト 2 で詳述。
- [**組織の MCP サーバーアクセス制御**](./latest-detail.md#2-組織の-mcp-サーバーアクセス制御) ([日本語](https://code.claude.com/docs/ja/managed-mcp#provide-servers-through-managed-settings) / [English](https://code.claude.com/docs/en/managed-mcp#provide-servers-through-managed-settings)):  
  `managedMcpServers` による提供が新しい h2 と 5 節として到着し、既存の排他的制御の節も 3 節に再編された（実質 155 行）。内容はハイライト 3 で詳述。
- [**すべての設定**](./latest-detail.md#3-すべての設定) ([English](https://code.claude.com/docs/en/settings-reference#maxeffortlevel)):  
  `maxEffortLevel` と `managedMcpServers` の 2 キーが新設され、努力レベル系の既存キーも軒並み書き直された（実質 152 行）。内容はハイライト 4 で詳述。
- [**エージェントビュー**](./latest-detail.md#4-エージェントビュー) ([English](https://code.claude.com/docs/en/agent-view#read-session-state-from-a-script)):  
  `claude agents --json` を外部から読むための契約が新設節として明文化され、`~/.claude/jobs/` は安定インターフェースではないと明記された（実質 87 行）。
- [**モデル設定**](./latest-detail.md#5-モデル設定) ([English](https://code.claude.com/docs/en/model-config#adjust-effort-level)):  
  努力レベルの保存とセッション限定の区別、Claude apps gateway での `fable` エイリアスの例外、1M コンテキストの判定条件が整理された（実質 81 行）。
- [**TypeScript SDK リファレンス**](./latest-detail.md#6-typescript-sdk-リファレンス) ([English](https://code.claude.com/docs/en/agent-sdk/typescript#sdkresultmessage)):  
  既存の `user_message_uuid` について「どの場合にエコーされるか」の条件と保証範囲が新たに規定され、エラー種別も列挙された（実質 55 行）。

## 軽微な更新

今回の差分は **2 ファイル・2,929 行**（追加 2,055・削除 874）です。内訳は `llms-full.txt` が 2,918 行（追加 2,047・削除 871）、ページ見出しマップ（`en/claude_code_docs_map.md`）が 11 行（追加 8・削除 3）。**`llms.txt` には差分がありません**（202 URL・355 行のまま）。`llms-full.txt` の総行数は **93,952 行から 95,128 行へ 1,176 行増え**、展開ページ数は 191 のままです。見出しマップの 3 行のうち 2 行は先頭の自動生成スタンプ（2026年09月09日 22時56分21秒 UTC → 2026年09月10日 22時57分12秒 UTC）なので、**見出しそのものの変更は 9 行（追加 7・削除 2）・4 ページ分**です。

本文が変わったページは **85 / 191**で、前回の 33 ページ・481 行と比べると約 6 倍の規模です。**前回の持ち越し 40 件（見出し 39 件・削除 1 件）は、ひとつ残らず決着しました** ―― エラーリファレンス 16 件（ハイライト 2）、組織の MCP 制御 9 件（ハイライト 3）、設定リファレンス 2 件（ハイライト 3・4）、アーティファクト 2 件、キーボードショートカット 2 件、インタラクティブモード 2 件、エージェントビュー 1 件、Amazon Bedrock 1 件、Claude apps gateway の設定リファレンス 1 件、権限 1 件、CLI リファレンス 1 件、Agent SDK のシステムプロンプト変更 1 件（ハイライト 1）。削除の 1 件（Remote Control のエラー文字列）も本文から消えました。

**changelog に載ったのは v2.1.267 の 1 リリース**（原文の日付表記は 2026年09月09日）だけです。下記の分類では **changelog 由来の項目に版を併記**しています。**changelog にしか記述がない項目には参考リンクを付けていません**（本サマリは changelog ページの URL を参考リンクに使わない方針です）。

**新機能**

- **`maxEffortLevel` が追加されました**。トップレベルにも `modelSettings` のモデル別エントリにも書け、**Bedrock・Vertex・Foundry を含むすべてのプロバイダーで努力レベルに上限をかけます**。利用者は上限より低いレベルなら選べます（v2.1.267。詳細はハイライト 4 参照） — [English](https://code.claude.com/docs/en/settings-reference#maxeffortlevel)
- **`--system-prompt-snapshot off` が追加されました**。会話に記録されたプロンプトを使い回す代わりに、**毎リクエストでシステムプロンプトを組み立て直します**（プロンプト文面を推敲する用途向け）（v2.1.267。詳細はハイライト 1 参照） — [English](https://code.claude.com/docs/en/cli-reference#system-prompt-flags-in-resumed-conversations)
- **インタラクティブモードに `Complete a command mid-prompt` の本文が届きました**。プロンプトの途中でも、**空白の後に `/` を打ってから名前の先頭数文字**を入れればコマンド補完が効きます（`run the tests, then /com` のように）。その文字で始まるコマンドだけが一致するので、`/tmp/notes.md` のようなファイルパスで候補リストが開きっぱなしになることはありません。**フルスクリーンでは行が選択されていないリストが開くので `Enter` はそのままプロンプトを送り**、`Tab` が先頭候補を挿入します。**フルスクリーン外ではカーソル位置にゴーストテキスト**で先頭候補が出て、複数一致なら `+2` のような件数が付きます — [English](https://code.claude.com/docs/en/interactive-mode#complete-a-command-mid-prompt)
- **インタラクティブモードに `Issue reference links` の本文が届きました**。Claude が `owner/repo#123` の形でイシューに言及すると、**ターミナルがハイパーリンクに対応していればクリックで開けます**。リンクになるのは 2 部構成の形式だけで、**素の `#123`・GitLab のネストしたパス（`group/subgroup/project#123`）・コードスパンやコードブロックの中は素のテキストのまま**です。**リンク先は参照が名指しするリポジトリではなく、git リモートから判定した自分のリポジトリのホスト**に組み立てられます。自動検出が効かないときは `FORCE_HYPERLINK` を `1`（有効化）または `0`（素のテキスト）に設定します — [English](https://code.claude.com/docs/en/interactive-mode#issue-reference-links)
- **アーティファクトに `Read an artifact shared with you` の本文が届きました**。共有されたアーティファクトは URL を渡すか `/artifacts` から添付すれば Claude に読ませられます。**Claude は他人が書いたページを WebFetch と同じ扱いで読む** ―― 生のページではなく尋ねた内容の要約を受け取り、**要約はページに書き込まれた指示を中継せず「そう書いてあった」と報告します**。ページの完全なソースはローカルファイルにも保存され、正確な内容が要るときに開けます — [English](https://code.claude.com/docs/en/artifacts#read-an-artifact-shared-with-you)
- **アーティファクトに `Offer a file download` の本文が届きました**。表の CSV エクスポートやグラフの PNG のように、**ページが生成したファイルを閲覧者に渡すボタンを置けます**。ただし**ダウンロードは claude.ai がアカウント単位で有効化するランタイム機能**で、Claude は公開前にアカウントがそれを持つか確認します。**`data:` や `blob:` へのリンクを含め、ページ自身が始めるダウンロードは claude.ai のビューアがブロックする**ので、その作りのボタンは作り直しを依頼する必要があります — [English](https://code.claude.com/docs/en/artifacts#offer-a-file-download)
- **キーボードショートカットに `Agents actions` と `Effort slider actions` の 2 節が届きました**。`Agents` コンテキスト（`claude agents` のエージェントビュー・v2.1.257 以降）では `agents:switchView`（`Ctrl+S`・状態とディレクトリで並び替えを切り替え）と `agents:togglePin`（`Ctrl+T`）が再割り当てできます。**エージェントビューが開いている間は `Agents` の割り当てが優先され、同じキーの `Chat` / `Global` の割り当ては無視されます**。`EffortSlider` コンテキストには `effortSlider:thisSessionOnly`（既定 `s`）だけがあり、**スライダーの Left / Right / Enter / Escape は再割り当てできません** — [English](https://code.claude.com/docs/en/keybindings#agents-actions)
- `hooks` に、**フックコマンドの代わりにプロンプトを走らせる `type: "agent"`** の記述が加わりました。`$ARGUMENTS` をフック入力 JSON のプレースホルダとして使い、**プロンプトフックより長い 60 秒の既定タイムアウト**を持ちます — [English](https://code.claude.com/docs/en/hooks#agent-hook-configuration)
- **`/code-review --comment` が GitLab のマージリクエストに対応しました**。GitHub の PR ならインラインコメント、**GitLab の MR なら単一のノート**として投稿します（v2.1.257 以降。`glab` CLI 経由で、未インストールならターミナルに出力）。MR は URL か `!123` の形で渡し、**素の番号やブランチ名が MR として扱われるのは origin が `gitlab.com` のときだけ**です — [English](https://code.claude.com/docs/en/code-review)
- **`--plugin-dir` にプラグインの入った親フォルダを渡せることが、プラグイン依存関係のページにも書かれました**。フォルダ自体がプラグインでなければ、`.claude-plugin/plugin.json` を持つ子フォルダがそれぞれ読み込まれます（v2.1.265 以降） — [English](https://code.claude.com/docs/en/plugin-dependencies)
- **`claude agents --json` が外部からセッション状態を読む公式の窓口として規定されました**（詳細は大幅更新 4 参照） — [English](https://code.claude.com/docs/en/agent-view#read-session-state-from-a-script)
- **フルスクリーンで `!` シェルコマンドの出力をクリックで展開できる**ようになりました。切り詰められた過去の結果も、実行中の進捗行もです（v2.1.257 以降） — [English](https://code.claude.com/docs/en/fullscreen)
- **VS Code 拡張に「非アクティブなセッションの自動アーカイブ」の設定（`archiveInactiveSessions`・既定 14 日）と、AI 生成のセッションタイトル、リネーム・アーカイブ操作が加わりました**。`/mcp` をチャットパネルで打てば MCP サーバーの追加・削除もできます — [English](https://code.claude.com/docs/en/vs-code#resume-past-conversations)

**機能改善**

- 出力スタイルの変更が、**記録済みシステムプロンプトを持つ会話ではキャッシュを壊さなくなりました**（詳細はハイライト 1 参照） — [English](https://code.claude.com/docs/en/prompt-caching#changing-output-style)
- **`managedMcpServers` で組織が全ユーザーへリモート MCP サーバーを配れるようになりました**（詳細はハイライト 3 参照） — [日本語](https://code.claude.com/docs/ja/managed-mcp#provide-servers-through-managed-settings) / [English](https://code.claude.com/docs/en/managed-mcp#provide-servers-through-managed-settings)
- **エラーリファレンスに 16 節が到着しました**（詳細はハイライト 2 参照） — [English](https://code.claude.com/docs/en/errors#administrator-policy-requires-a-cloud-gateway-sign-in)
- **努力レベルの「保存」と「このセッションのみ」の区別が明示されました**（詳細はハイライト 4 参照） — [English](https://code.claude.com/docs/en/model-config#adjust-effort-level)
- **権限ページに `What a Bash rule doesn't match` の本文が届きました**。Bash ルールは**複合コマンドを分割しラッパーを剥がした後の「Claude が書いたコマンドテキスト」に一致する**ので、**同じプログラムを別の形で呼ばれると素通りします**。`Bash(curl *)` は `/usr/bin/curl` や `sh -c 'curl …'` を、`Bash(rm *)` は `/bin/rm` や `bash -c 'rm …'` を、`Bash(git push *)` は `git -C . push` や `git -c key=value push` を止めません。**プログラムに対するセキュリティ境界ではない**と明記されました。オートモード設定・設定のデバッグ・設定リファレンスの 3 ページからこの節への参照が張られています — [English](https://code.claude.com/docs/en/permissions#what-a-bash-rule-doesnt-match)
- **Amazon Bedrock に `Certificate errors behind a TLS-inspecting proxy` の本文が届きました**。モデル検出・トークンカウント・STS / SSO の資格情報呼び出し・セットアップウィザードの検証に **CA 証明書ストアの設定がそのまま効く**ので、Bedrock 固有の設定は要りません。**v2.1.260 より前は、プロキシ経由のときだけ CA 設定が効き、直接接続ではランタイム既定のストアしか信頼しませんでした** — [English](https://code.claude.com/docs/en/amazon-bedrock#certificate-errors-behind-a-tls-inspecting-proxy)
- **サブエージェントの `permissionMode` の継承ルールが書き直されました**。**主会話が `bypassPermissions` / `acceptEdits` / オートモードのときは、サブエージェントもそのモードで走り、設定した `permissionMode` は無視されます**。主会話が `default` / `dontAsk` / `plan` のときだけ設定値が効き、**ただしサブエージェント側が `bypassPermissions` を宣言した場合は主会話のモードのまま**です。同じ整理が Agent SDK の TypeScript / Python / サブエージェントの各リファレンスにも入りました — [English](https://code.claude.com/docs/en/sub-agents#supported-frontmatter-fields)
- **`/reload-plugins` が対話型ターミナルの無いセッションでも動く**ことがプロンプトキャッシングのページに明記されました（デスクトップアプリ・Agent SDK・`-p` の非対話モード。v2.1.260 以降）。**そこではプラグイン MCP サーバーの変更以外がすべて適用され、MCP の変更は次のセッションに持ち越されるのでセッション途中の全再読み込みコストが発生しません** — [English](https://code.claude.com/docs/en/prompt-caching#when-plugin-changes-apply)
- **スキルやコマンドのフロントマターが `model` を指定すると、そのターンはモデル切り替えになる**と明記されました。次のリクエストはキャッシュヒットなしで会話履歴全体を読み、**セッションのモデルは次のプロンプトで戻ります**。`context: fork` のスキルは代わりにフォーク先サブエージェントのモデルを設定します — [English](https://code.claude.com/docs/en/prompt-caching#switching-models)
- **`--plugin-dir` で渡したフォルダ内のプラグインの増減が、対話セッションでは即座に反映される**ようになりました。適用すると全再読み込みになる場合は保留して `/reload-plugins` を促します（v2.1.265 以降） — [English](https://code.claude.com/docs/en/prompt-caching#when-plugin-changes-apply)
- **再開したサブエージェントが、元の実行が温めたキャッシュを読めるようになりました** — [English](https://code.claude.com/docs/en/prompt-caching#subagents-and-the-cache)
- **`SessionStart` フックが `/clear` の後にバックグラウンドで走る**ようになり、プロンプトはすぐ入力を受け付けます。**フックの `additionalContext` が 10,000 文字を超えるとセッションディレクトリのファイルに書き出され、Claude にはパスと短いプレビューが渡ります**。複数のフックが同じイベントに `additionalContext` を返した場合は全部が届きます。フック入力に `scratchpad_dir`（セッションのスクラッチパッドディレクトリ）も加わりました — [English](https://code.claude.com/docs/en/hooks#sessionstart)
- **管理設定の「無効なエントリ」の表が全面的に書き直されました**。`allowedMcpServers` / `allowedHttpHookUrls` / `httpHookAllowedEnvVars` / `allowedChannelPlugins` は**壊れていれば空の許可リストとして強制**され、`allowManagedHooksOnly` / `allowManagedMcpServersOnly` / `enforceAvailableModels` は `true` 扱い、`crossSessionInbound` は最も厳しい `refuse` 扱いになります。**v2.1.267 より前は、値やエントリが 1 つでも壊れていると鍵ごと捨てていました** — [English](https://code.claude.com/docs/en/managed-settings#invalid-entries-in-managed-settings)
- **サーバー管理設定の「フェッチとキャッシュ」に、`managedMcpServers` を待つ挙動が加わりました**。キャッシュ済みの `managedMcpServers` は**サーバーがペイロードを確認するまで適用されず、最大 30 秒待ちます** — [English](https://code.claude.com/docs/en/server-managed-settings#fetch-and-caching-behavior)
- **Remote Control のページで、接続デバイスからできることが整理されました**。モデルの選択（**そのセッション限定**。認識できない名前は拒否）、努力レベルの設定、`/teleport` でのセッション引き取り、`/advisor` にモデル引数を渡す形（v2.1.260 以降）などです。**`claude remote-control` には初回の `Enable Remote Control? (y/n)` 確認**が入りました — [English](https://code.claude.com/docs/en/remote-control#limitations)
- **`/workflows` のエージェント詳細とワークフローの再開が書き足されました**。`agent()` に `schema` を渡すと**開始前にスキーマを検査**し、**5 回試しても検証に通らなければ最後の検証失敗を含むエラーで失敗**します。停止した実行の再開は `p` キー、クラウドセッションでは実行結果が会話履歴とともに保存されます — [English](https://code.claude.com/docs/en/workflows#let-claude-decide-with-ultracode)
- **`/advisor` がターミナルのピッカーが無い場所でも動く**ようになりました（`-p`、Agent SDK、デスクトップアプリ、Remote Control）。引数なしで現在のモデルと使えるエイリアスを表示し、`/advisor opus` で設定、`/advisor off` で無効化します。**課金は advisor モデルのレートで、サブスクリプションではプランの上限に算入されます（Fable の advisor だけは使用クレジット）** — [English](https://code.claude.com/docs/en/advisor#choose-an-advisor-model)
- **`/compact` 関連のフックのマッチャーが表になりました**。`manual`（`/compact`）と `auto`（自動コンパクト）の 2 値です — [English](https://code.claude.com/docs/en/hooks#precompact)
- **クロスセッションメッセージで `offline` のセッションにも送れる**ことが明記されました。**送信自体は通るが、相手のマシンが再接続してから届きます**。バックグラウンドセッションにターミナルがアタッチされていない間は、ダイアログを期限を過ぎても開いたままにします — [English](https://code.claude.com/docs/en/cross-session-messaging#control-inbound-messages)
- **MCP の出力上限の説明が精密化されました**。**画像を含まない結果が上限を超えたときだけ**ファイルに保存されます。`MAX_MCP_OUTPUT_TOKENS` で引き上げられることが Agent SDK の MCP ページにも追記されました — [English](https://code.claude.com/docs/en/mcp#mcp-output-limits-and-warnings)
- **`settings.json` の編集が、セッション開始後にファイルやプロジェクトの `.claude/` フォルダ自体を作った場合でも反映される**ようになりました（v2.1.257 以降） — [English](https://code.claude.com/docs/en/debug-your-config)
- **Google Cloud の資格情報更新コマンドを走らせる前に、実際に期限切れかをアクセストークンの要求で確認する**ようになりました。**5 秒で終わらなければコマンドを飛ばし、リクエストが資格情報エラーで失敗してから実行します**（v2.1.261 より前はタイムアウトを期限切れとみなしてブラウザを開くことがありました） — [English](https://code.claude.com/docs/en/google-vertex-ai)
- **Glob と Grep の権限判定が、検索ディレクトリの存在確認より先に行われる**と明記されました。作業ディレクトリの外の存在しない `path` でも読み取り権限のプロンプトが出ます — [English](https://code.claude.com/docs/en/tools-reference#glob-tool-behavior)
- **`/install-github-app` が github.com のリポジトリ専用**であることが明記されました。リモートが gitlab.com や bitbucket.org なら通知して終了します — [English](https://code.claude.com/docs/en/github-actions)
- **Claude apps gateway on AWS の IAM ロールに `bedrock:CountTokens` が必要**になりました — [English](https://code.claude.com/docs/en/claude-apps-gateway-on-aws)
- **セルフホストランナーの `--kill-session-after-min` が、上限に達したセッションを即座に終了しなくなりました**。**v2.1.260 以降のランナーは既定 15 分の猶予枠**（`SELF_HOSTED_RUNNER_MAX_LIFETIME_GRACE_MS` で変更可）を与えます ―― 利用者待ちかバックグラウンドタスクだけを抱えている場合は即座に解放し、ターンが走っていれば終わるまで待ち、**猶予枠が尽きてもランナー上に残っていれば終了して実行中のターンの作業は失われます**。**v2.1.260 より前は上限で全セッションを終了していました**。あわせてランナーが設定する git の既定に **`push.negotiate = true`**（v2.1.257 以降）と、**`core.hooksPath` 経由でコミットに `Co-authored-by:` トレーラーを自動付与するフック**が加わり、`--use-anthropic-git-proxy` を選んだランナーは**登録時にその旨をサーバーへ報告して起動時にメッセージを出す**ようになりました。**コネクターを自己ホストセッションから外すには `allowedMcpServers` / `deniedMcpServers` でフィルタする**という既存の案内は、1 段落を 2 段落に割って書き直されました（対象が「設定したサーバー」から**「ランナーホストが配るサーバーとユーザーが追加したサーバー」へ明示化された**程度で、制御の中身は変わっていません） — [English](https://code.claude.com/docs/en/self-hosted-environments-deploy#some-sessions-dont-count-as-idle)
- **`ultrareview` の `--timeout` の既定が 30 分から 45 分に延びました** — [English](https://code.claude.com/docs/en/ultrareview)

**バグ修正**

以下はすべて v2.1.267（2026年09月09日）の項目です。**プロンプトキャッシュ関連の 6 件と再開関連の修正はハイライト 5 でまとめて扱っています。**

- Cowork のクラウドのスケジュール済みタスクが、**管理設定でサンドボックス化を要求する組織で起動時に失敗する**問題を修正
- `/context` などのローカルコマンドの出力が**モバイルクライアントで空白に描画される**問題を修正
- エージェントビュー内の tmux / ssh セッションに再接続した後、**shift+enter と option+backspace が効かない**問題を修正
- フルスクリーンで上にスクロールしたとき、**薄い直前プロンプトのヘッダーが会話の先頭に出ない**問題を修正
- **大きな出力スキーマを持つワークフローの `agent()` 呼び出しが、安全性分類器に判定されずオートモードで拒否される**問題を修正
- **マーケットプレイスのエントリパスにバックスラッシュが含まれると、macOS と Linux で取得済みマーケットプレイスの封じ込めチェックを迂回できる**問題を修正
- Claude Desktop のようなホストアプリの配下で **AWS / Google Cloud の資格情報が期限切れのとき、再認証エラーが出る前に汎用の「request failed」で 10 回リトライしていた**問題を修正
- **`effort:` フロントマターが、既定の努力レベルを保持中のモデル（Opus 4.7 / Opus 4.8 / Fable 5）で無視される**問題を修正
- **アーティファクトの公開で、ページファイルが UTF-8 でないか U+FFFD を含むときのエラーが不親切だった**問題を修正。**修正すべき行と列を示す**ようになりました。**なおこの `The source file is not valid UTF-8 text` はエラーリファレンスの見出しとして今回の見出しマップに現れていますが、本文はまだ届いていません**
- **接続が途中で切れて中断されたアーティファクトの公開が、完了していないと判断できる場合に 1 回だけ再試行する**ようになりました
- `claude agents` の `@` ディレクトリメニューが、**セッション開始後に作られたリポジトリを一覧しない**問題を修正
- Claude Desktop や VS Code のセッションに参加した Remote Control クライアントが、**古い権限モードを表示し続ける**問題を修正
- **`claude remote-control` がサーバー資格情報の期限切れ（開始からおよそ 30 日）で終了し、接続中の全セッションを落とす**問題を修正。ホストが再登録して継続するようになりました
- **使用量上限の警告が、モデルやモードごとに異なる上限ウィンドウを報告するとセッション中に点滅する**問題を修正
- **MCP サーバーの再送信や組み込みツールの再描画で、モデルが既に読み込んだツールが再提示されると過去の推論が落ちる**問題を修正
- **会話の途中で MCP サーバーの切断やアップグレードによりツールが消えると、ツール一覧が書き換わり過去の思考が捨てられる**問題を修正
- **`/diff` パネルが「0 files changed」とスピナーを一瞬出してから確定する**問題を修正。空の状態はパネル中央に表示されるようになりました
- **Bash ツールの説明ガイダンスを改善**し、Claude がコマンドをそのまま繰り返すのではなく**平易な言葉で何をするコマンドかを述べる**ようになりました
- **サンドボックス内で `pbcopy` などのクリップボードコマンドが失敗したとき、Claude が `/copy` を提案する**ようになりました
- **Bash ツール呼び出しの多いセッションの `--resume` の初回描画が速くなりました**
- **プロンプト入力の反応性が改善**し、キー入力がスピナーやストリーミングの再描画の 1 フレーム後ろに待たされることがなくなりました
- **`--system-prompt` / `--append-system-prompt` で開始したサブエージェントとセッションが、システムプロンプトとツール定義を 1 回だけ記録する**ようになりました（描画し直さない）
- **アーティファクトツールの公開エラーが、拒否された理由と対処を述べる**ようになりました
- セルフホストランナー: **`--use-anthropic-git-proxy` が登録時にサーバーへ報告され、レガシーな git プロキシ経由で clone するセッションごとに警告を出す**ようになりました
- ゲートウェイ: **`forward_user_identity` の上流が 429 を返したとき、次の上流へフェイルオーバーせずそのまま開発者へ返す**ようになりました（プロキシのユーザー単位の上限を成立させるため）
- \[VS Code] **循環した親リンクを含むトランスクリプトの会話でフォーク・過去メッセージの編集・巻き戻しをすると、拡張ホストが CPU 100% でハングする**問題を修正
- \[VS Code] **WSL2 / WSLg でスクリーンショットを貼り付けると生の画像バイトがチャット入力に入る**問題を修正
- \[VS Code] **チャットの差分ブロックが常にダークテーマで描画される**問題を修正（ハイコントラストを含む現在のテーマに従うようになりました）
- \[VS Code] **右横書きと英語が混在したテキストが入力中に誤った順序で描画される**問題を修正
- \[VS Code] **CRLF 改行のファイルで差分ビューの編集を受け入れると「String not found in file」で失敗する**問題を修正
- \[VS Code] **@ メンションがパスに空白を含むファイルを落とす**問題と、**Remote-SSH 接続のウィンドウでセッション一覧が読み込めない**問題、**大きなワークスペースで ripgrep プロセスが暴走する**問題を修正
- \[Claude Code on the web] **GitHub Enterprise Server のセッションで、トークンが期限切れになると GitHub アカウントが未接続と表示される**問題を修正（自動で更新されるようになりました）
- \[Claude Code on the web] **Claude GitHub App の無い組織で `gh` と GitHub API の呼び出しが失敗する**問題を修正
- **管理設定が Claude apps gateway のサインインを要求するマシンで `/login` を実行したとき、Esc がダイアログを閉じず何も起きない**問題を修正
- \[Claude Tag] **プリセットの接続フォームに「Use a custom connector」のリンクが加わりました**。最初からやり直さずにカスタム接続へ切り替えられます（区分としては Added ですが、接頭辞付きの項目なので上記「Added は 2 件だけです」の集計には含まれません）
- \[Claude Tag] **Claude がチャンネルのトップレベルに投稿したメッセージの編集・削除をスレッドから依頼すると、投稿したセッションに届かず訂正が返る**問題を修正
- \[Claude Tag] **組織が使用クレジットを使い切ったときに「The API rejected the request as invalid」と返す**問題を修正。**Admin settings > Review requests のツールアクセス要求で Connect が「Authorization failed」になる**問題も修正

**その他**

- **新しい持ち越しは 6 件で、前回の 40 件から大きく減りました**（追加 7 行のうち 1 行は出力スタイルの移動なので実質 6 件）。内訳は **エラーリファレンス 2 件**（`The source file is not valid UTF-8 text` / `Working directory no longer exists when starting a background session`）、**Claude apps gateway の設定リファレンス 3 件**（`pricing` 配下の `Send the rates to signed-in clients`、`telemetry` 配下の `Export directly to your collector` と `When a destination fails`）、**プロンプトキャッシング 1 件**（h2 `Resuming a session`）です。**いずれも本文は `llms-full.txt` のどこにも見当たりません**。プロンプトキャッシングの `Resuming a session` については、現在は「アップグレード」節の末尾に `<Note>` として置かれている内容（再開は異なるシステムプロンプトの後ろに履歴が並ぶのでキャッシュヒットなしで全処理される）が独立した h2 に昇格する見込みですが、**今回の v2.1.267 で再開まわりのキャッシュ挙動が大きく変わったことを踏まえると、内容も書き換わる可能性があります**
- **見出しマップからの削除は 2 件**です。1 件は出力スタイルの移動（「キャッシュを無効にする」側から「保持する」側へ。ハイライト 1）、もう 1 件は**分析ページの `Tagging criteria`**（PR 帰属の配下）です。**後者は本文には `#### Tagging criteria` として残っており**、見出しマップからだけ消えました。前回の Remote Control のエラー文字列と同じパターンです
- **「システムプロンプトを変更する」という言い回しの一掃が 6 ページに及びました**。出力スタイル（ハイライト 1）のほか、**用語集**（出力スタイルの定義が「Claude Code が Claude に与える指示を変更する設定」に、努力レベルの定義が「適応的推論を制御する設定」に）、**`.claude` ディレクトリリファレンス**（`output-styles/*.md` の説明が「カスタムシステムプロンプトセクション」から「Claude の働き方を調整するカスタム指示セット」へ）、**コンテキストウィンドウ**（コンパクト後の表で「システムプロンプトと出力スタイル」の行が「変更なし、メッセージ履歴の一部ではない」から「どちらも引き続き適用される」へ）、**設定リファレンス**、**メモリ**です — [English](https://code.claude.com/docs/en/glossary)
- **「Fable 5.1 と Fable 5」の個別列挙が「Fable モデル」へ一般化されました**。対象はモデル設定（適応的推論・思考の無効化）、コンテキストウィンドウ（1M 対応モデルの列挙）、用語集（努力レベルの対応モデル）、セキュリティ（`Fable 5.1 の safeguards が…` という固定文言が「モデル名を含む通知」という書き方へ）、コミュニケーションキットの 5 ページです。**Fable の系列が増えることを見込んだ書き換え**と読めます — [English](https://code.claude.com/docs/en/context-window)
- **コマンド一覧ページは表の桁揃えだけが変わりました**。生の差分は 228 行（追加 114・削除 114）で errors に次ぐ 2 番目の大きさですが、**空白幅の圧縮を揃えて比較すると差分は 0 行**になります。**内容の変更は一切ありません** — [English](https://code.claude.com/docs/en/commands)
- **`claude agents --json` の `state` を読む契約が明文化された一方で、`~/.claude/jobs/` は安定インターフェースではないと明記されました**（詳細は大幅更新 4 参照） — [English](https://code.claude.com/docs/en/agent-view#read-session-state-from-a-script)
- **オートモードで既定許可される push と PR の説明が、Bash ルールの限界に合わせて補われました**。人間のチェックポイントを置くレシピについて、**`git push` や `gh pr create` で始まるコマンドに一致するので、`git -C <dir> push` のように別の書き方をされたものはチェックポイントを通らない**と明記されています — [English](https://code.claude.com/docs/en/auto-mode-config)
- **`advisorModel` と `/advisor` の課金の説明が揃えられました**。advisor が使えないプロバイダーの列挙が「Bedrock / Agent Platform / Foundry」から**「Amazon Bedrock と Claude Platform on AWS」**へ変わっています — [English](https://code.claude.com/docs/en/advisor#requirements)
- **環境変数リファレンスに 13 行が追加されました**。`CLAUDE_CODE_ARTIFACT_AUTO_OPEN`・`CLAUDE_CODE_DISABLE_THINKING`・`CLAUDE_CODE_NONBLOCKING_STDOUT`・`CLAUDE_JOB_DIR`・`FORCE_HYPERLINK`・`MAX_STRUCTURED_OUTPUT_RETRIES`・`VERTEX_REGION_CLAUDE_FABLE_5_1` などです。**`CLAUDE_SUBAGENT_BG_SHELL_MAX_MS` は v2.1.260 で削除され no-op になった**と記載されました — [English](https://code.claude.com/docs/en/env-vars)
- 見出しマップ先頭の自動生成スタンプが 2026年09月09日 22時56分21秒 UTC から 2026年09月10日 22時57分12秒 UTC へ進みました。**対象期間中に上流の再生成が 1 回だけ走った**ことを示しています

**参考リンクについて**: **今回、日本語版のリンクを付けられるのは組織の MCP 制御ページだけです。** 作成時点で公開中の日本語版を実際に取得して確認したところ、**このページだけは新設の「マネージド設定を通じてサーバーを提供する」節が 5 小節とも翻訳済み**でした。一方、**プロンプトキャッシング・出力スタイル・CLI リファレンス・モデル設定・エージェントビューは未追従**です（日本語版のプロンプトキャッシングでは「出力スタイルの変更」が依然として「キャッシュを無効にするアクション」の一覧にあり本文も旧記述のまま、CLI リファレンスは「システムプロンプトをカスタマイズするための 4 つのフラグ」のまま、出力スタイルは「変更は `/clear` または新しいセッション後に有効になります」という v2.1.251 以前の記述が残っています）。**エラーリファレンスは今回の 16 節のうち一部しか届いておらず**、混在しているため安全側で英語版のみにしました。**設定リファレンスは日本語版の URL が 404 を返す**ため英語版のみです。**本文が未着の持ち越しにはアンカーを付けず、ページ URL のみ**としています。

## 新着情報

（今回の対象期間には `whats-new/` 配下のページに差分がありませんでした。`llms-full.txt` で本文が変わった 85 ページはいずれもリファレンス・ガイド系と changelog です。最新の週間ダイジェストは 8 回前のサマリで扱った Week 34（2026年08月17日～21日）のままで、新しい週のダイジェストの追加も既存ページの訂正もありません。**`whats-new/` の無差分は 8 回連続**で、本文が 85 ページ動いた今回の規模を考えると、リリースノート系の更新経路だけが止まっている状態が続いています）

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-09-09.md](./archives/latest/2026-09-09.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-09-09.md](./archives/latest-detail/2026-09-09.md)

<!--
base_commit: 3609917c5bd9971a8010d16470ca46a5c7c2c8cb
head_commit: de9cda17683da28d936a197650b1dab64d4d7341
generated_at_full: 2026-09-11T15:08:22+09:00
-->
