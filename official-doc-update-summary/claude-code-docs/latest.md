---
対象期間: 2026年09月04日 〜 2026年09月05日
作成日: 2026-09-05
---

# Claude Code 公式ドキュメント更新サマリ

```markdown
今回も 1 日分の取り込みで、差分があったのは `llms-full.txt` の 1 ファイルだけ、32 ページ・1,158 行（追加 671・削除 487）です。ただし生の行数の大半は表の桁揃えで、桁揃えノイズを潰した実質では 396 行（追加 290・削除 106）―― 前回の実質 387 行とほぼ同じ規模になります。ノイズ 762 行のうち 700 行が環境変数リファレンス 1 ページの桁揃えでした。今回の性格を一言でいうと「**前回サマリで「本文が届いていない持ち越し」と書いた 7 件が、そのまま全部届いた回**」で、エラーリファレンスの 3 節・設定リファレンスの 2 キー・TypeScript Agent SDK の 1 フィールド・インタラクティブモードの見出し改称がそれにあたります。ページの新規追加・削除はなく（展開ページ数は前後とも 191）、`llms.txt` とページ見出しマップは 2 回ぶりに無差分に戻ったため、**新たな持ち越しは 0 件**です。`whats-new/` は 5 回連続で差分がありません。

主要なものを以下に挙げます。

1. `Ctrl+W` などの単語編集キーが readline 準拠を既定にし、`keybindingFlavor` 設定が非推奨になった
2. Bash の入力リダイレクト `< file` も Read 権限ルールの検査対象になった
3. ネットワークパスを作業ディレクトリに追加できなくなり、専用のエラー節が新設された
4. strict sandbox mode が、利用者自身が `!` で打つコマンドを対象外にした
5. `bashOutputMaxChars` と `taskOutputMaxChars` で、Claude がインラインで受け取る出力量を上げられるようになった
```

## ハイライト

1. [**単語編集キーが readline 準拠を既定にし、`keybindingFlavor` が非推奨になった**](./latest-detail.md#1-単語編集キーが-readline-準拠を既定にしkeybindingflavor-が非推奨になった):  
  インタラクティブモードの節が `Make editing keys follow readline conventions` から **`Word boundaries in editing shortcuts`（編集ショートカットの単語境界）** に改称され、**`Ctrl+W` は既定で「前の単語」ではなく「前の空白」まで削除する**ようになった。`Alt+F` と `Alt+D` も単語の終わりで止まる。設定でこれを有効にしていた `keybindingFlavor` は v2.1.261 で非推奨・無効となり、設定リファレンスの項目が丸ごと警告ブロックに置き換わっている。
2. [**Bash の入力リダイレクト `< file` も権限チェックの対象になった**](./latest-detail.md#2-bash-の入力リダイレクト--file-も権限チェックの対象になった):  
  権限のページの `Redirections` 節が全面的に書き直され、**出力リダイレクト（`>` `>>` `2>`）は `Edit` ルール、入力リダイレクト（`< file`）は `Read` ルールに照らして検査する**という 2 本立てになった。入力側の検査は v2.1.257 以降。あわせて「実体の無いターゲットは検査しない」対象（`/dev/null`・`2>&1` などの FD 形式・ヒアドキュメント）が明示された。
3. [**ネットワークパスを作業ディレクトリに追加できなくなった**](./latest-detail.md#3-ネットワークパスを作業ディレクトリに追加できなくなった):  
  エラーリファレンスに `Working directory is a network path` の節が新設された。**ネットワークパスの解決はそのパスが名指すホストに接触しうるし、Windows ではその接触で資格情報が送られうる**ため、Claude Code は解決を試みずにパスを拒む。UNC 共有・`/net/<host>` の automount・シンボリックリンク経由でネットワークに届くローカルパスが対象で、マップ済みのドライブレターと `\\wsl$` は対象外。
4. [**strict sandbox mode が `!` で打つコマンドを対象外にした**](./latest-detail.md#4-strict-sandbox-mode-が--で打つコマンドを対象外にした):  
  サンドボックスのページで、`allowUnsandboxedCommands: false` の説明が「すべてのコマンド」から「**Claude が実行するすべてのコマンド**」に限定された。**利用者自身がシェルモードで打つコマンドはサンドボックスの外で走る**（例外はバックグラウンドセッションと、Linux で `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB` を設定したセッションの 2 つ）。v2.1.260 より前は、strict sandbox mode がすべてのセッションでシェルモードのコマンドもサンドボックス化していた。
5. [**`bashOutputMaxChars` と `taskOutputMaxChars` が追加された**](./latest-detail.md#5-bashoutputmaxchars-と-taskoutputmaxchars-が追加された):  
  設定リファレンスに 2 つのキーが新設された（v2.1.261 以降）。**Claude がインラインで受け取る出力量を、コマンド出力は既定 30,000 文字から、バックグラウンドタスク出力は既定 32,000 文字から、それぞれ最大 128,000 文字まで引き上げられる**。設定すると対応する環境変数（`BASH_MAX_OUTPUT_LENGTH` / `TASK_MAX_OUTPUT_LENGTH`）は無視される。

## 新規追加されたページ

（今回の対象期間に新規追加・削除されたドキュメントページはありません。`llms-full.txt` に展開されているページ数は前後とも 191 で、`llms.txt` も収録 URL 202 件・全体 356 行のまま無差分です。2 回連続で差分の出ていた `llms.txt` と、前回 52 行の差分があったページ見出しマップの双方が今回は無差分で、差分は `llms-full.txt` の 1 ファイルに閉じています）

## 大幅に更新されたページ

- [**エラーリファレンス**](./latest-detail.md#1-エラーリファレンス) ([English](https://code.claude.com/docs/en/errors#no-response-from-api)):  
  新しい節が 3 つ加わり、`No response from API` が全面的に書き直された。初回の試行と再試行で応答ヘッダーの待ち時間が別々になり、エラーメッセージが実際に待った時間を表示するようになっている。冒頭のメッセージ対応表にも 3 行が入った。今回の最大差分（実質 93 行 = 追加 83・削除 10）。
- [**設定リファレンス**](./latest-detail.md#2-設定リファレンス) ([English](https://code.claude.com/docs/en/settings-reference#bashoutputmaxchars)):  
  `bashOutputMaxChars` と `taskOutputMaxChars` が新設され、`keybindingFlavor` が非推奨の警告ブロックに置き換わった。サンドボックス系 4 か所と `permissions.deny` の記述も、対象を「Claude が実行するコマンド」に限定する方向へ揃えられている（実質 66 行 = 追加 48・削除 18）。
- [**TypeScript Agent SDK リファレンス**](./latest-detail.md#3-typescript-agent-sdk-リファレンス) ([English](https://code.claude.com/docs/en/agent-sdk/typescript#user_message_uuids)):  
  `user_message_uuids` フィールドが新設されたほか、割り込みレシートの意味・`ambient` フラグの定義・`permissionPrompts` オプションの記載が改まった。閾値を 1 行だけ超えた（実質 51 行 = 追加 37・削除 14）。

## 軽微な更新

今回も 1 日分の取り込みで、**差分があったのは `llms-full.txt` の 1 ファイルだけ**です（前回は `llms-full.txt`・ページ見出しマップ・`llms.txt` の 3 ファイル）。差分のあったページは 32、生の差分行は 1,158 行（追加 671・削除 487）で、前回の 3 ファイル合計 545 行の 2 倍以上に見えます。しかし**生の行数の大半は表の桁揃えです**。本サマリで「実質 N 行」と書いた各行の連続空白と連続ハイフンを潰して数え直すと **396 行（追加 290・削除 106）** となり、**前回の実質 387 行とほぼ同規模**に落ち着きます。潰れた 762 行のうち **700 行が環境変数リファレンス 1 ページの桁揃え**（生 708 行 = 追加 354・削除 354 → 実質 8 行）で、残りは非対話モード 22 行、インタラクティブモード 18 行、管理 MCP 12 行、ツールリファレンス 6 行、TypeScript Agent SDK 4 行です。ページの新規追加・削除はなく、展開ページ数は前後とも 191、`llms-full.txt` の総行数は 93,784 行から 93,968 行に増えました。

**`llms.txt` とページ見出しマップは今回いずれも無差分**でした。`llms.txt` は 2 回連続で出ていた差分が止まり、収録 URL 202 件・全体 356 行のまま。ページ見出しマップは前回 52 行の差分がありましたが今回はゼロです。

**changelog に加わったのは v2.1.263（原文の日付表記は 2026年09月06日）の 1 件のみ**で、内容も「バグ修正と信頼性の改善」の 1 行だけです（4 行すべて追加）。前回扱った v2.1.261 の 67 件とは対照的な小ささで、**changelog に v2.1.262 の項はありません**（v2.1.263 の次は v2.1.261 が並びます）。したがって今回の差分の中身は、changelog に新しく載った変更ではなく、**すでに changelog に出ていた v2.1.257 〜 v2.1.261 の各変更が通常ドキュメントページに書き下ろされたもの**です。バージョンの内訳は次のとおりで、各項目にはこの区別が分かるようバージョンを併記しています。

- **v2.1.257**: ネットワークパスの拒否、`/mcp` 再接続時のポリシー再評価、入力リダイレクトの検査、ゲートウェイのモデル検出（不要不急トラフィック停止時も走る・`description` 表示）、プラグインの symlink 判定、`/add-dir` によるサブディレクトリの設定読み込み
- **v2.1.259**: `permissionPrompts` オプション
- **v2.1.260**: strict sandbox mode がシェルモードのコマンドを対象外に、括弧が対応していない権限ルールの報告メッセージが `Mismatched parentheses` から変更
- **v2.1.261**: 単語編集キーの readline 既定化と `keybindingFlavor` 非推奨、`bashOutputMaxChars` / `taskOutputMaxChars`、`--append-subagent-system-prompt-file`、`Organization policy` 行、`No response from API` の再試行待ち時間

**今回の性格を一言でいうと、前回サマリで「持ち越し」として名指しした 7 件が、そのまま全部届いた回**です。前回は「ページ見出しマップに現れているのに `llms-full.txt` の本文が届いていない」ものが 7 件あると書きました ―― エラーリファレンスの `Working directory is a network path`・`MCP server is blocked by enterprise managed policy`・`Malformed Tool(content) rule` の 3 見出し、設定リファレンスの `bashOutputMaxChars`・`taskOutputMaxChars` の 2 キー、TypeScript Agent SDK リファレンスの `user_message_uuids`、そして `Make editing keys follow readline conventions` → `Word boundaries in editing shortcuts` の改称（前回は「キーバインドのページ」と書きましたが、実体はインタラクティブモードのページの節でした）。**見出しの差分を突き合わせた結果、この 7 件はすべて本文つきで到着しています**。そして今回はページ見出しマップ自体に差分が無いため、**新たな持ち越しは 0 件**です。

分類の基準は前回同様「実質の差分 50 行以上 かつ 内容の変更を伴うこと」としました。閾値を超えたのはエラーリファレンス 93 行、設定リファレンス 66 行、TypeScript Agent SDK リファレンス 51 行の 3 ページです。次点以下はインタラクティブモード 29 行、権限 25 行、LLM ゲートウェイ互換ガイド 24 行、サンドボックス 17 行で、いずれも本カテゴリの扱いですが、内容はハイライト 1・2・4 で本文を扱っています。

本サマリの参考リンクは前回に続き**すべて英語版のみ**です。今回の変更に日本語版が追従していないためで、作成時点で公開中の日本語版ページを実際に取得して確認しました（本リポジトリに取り込んである `en/` のスナップショットではなく、`code.claude.com` のライブページを参照しています）。確認結果は次のとおりです。**日本語版のインタラクティブモードには「編集ショートカットの単語境界」に相当する節が無く、`Ctrl+W` の説明も「前の単語を削除」の旧記述のまま、シェルモードの節にもサンドボックスの但し書きが無い**、**日本語版のエラーリファレンスには今回の 3 節どころか `No response from API` の節自体が存在しない**、**日本語版のサンドボックスのエスケープハッチの段落は「すべてのコマンドはサンドボックス化されるか `excludedCommands` にリストされている必要があります」の旧文のまま**、**日本語版の権限のページにはリダイレクトの節が無く、ネットワークパスへの言及も、括弧がリテラルである旨の記述も無い**、**そもそも `https://code.claude.com/docs/ja/settings-reference` は 404 を返す**（日本語版は `/docs/ja/settings` に相当ページがある）でした。他のページは個別には確認していませんが、いずれも直近数日の変更であるため未追従とみなし、安全側に倒して英語版のみを載せています。

**新機能**

- **`bashOutputMaxChars` と `taskOutputMaxChars` の 2 設定が加わりました**（v2.1.261）。Claude がインラインで受け取る出力量を、コマンド出力は既定 30,000 文字から、バックグラウンドタスク出力は既定 32,000 文字から、それぞれ最大 128,000 文字まで引き上げられます（詳細はハイライト 5 参照）— [English](https://code.claude.com/docs/en/settings-reference#bashoutputmaxchars) / [English](https://code.claude.com/docs/en/tools-reference#output-limits)
- **`--append-subagent-system-prompt-file` が文書化されました**（v2.1.261）。コマンドラインに渡すには長すぎるサブエージェントのシステムプロンプトをファイルから読み込むフラグで、`--append-subagent-system-prompt` との併用はできません。非対話モード（`-p`）でのみ有効です。環境変数 `CLAUDE_CODE_ENABLE_APPEND_SUBAGENT_PROMPT` の説明にも、この新フラグが自動でこの変数を立てる旨が追記されました — [日本語](https://code.claude.com/docs/ja/cli-reference#cli-flags) / [English](https://code.claude.com/docs/en/cli-reference#cli-flags) / [English](https://code.claude.com/docs/en/sub-agents#write-subagent-files)
- **`claude doctor` の `Organization policy` 行が文書化されました**（v2.1.261）。管理設定のページに「**組織の設定がそのマシンに届いているかを確認するには `claude doctor` を実行してこの行を読め。ポリシーをどこから読み込んだか、または読み込めなかった理由が出る**。実行中のセッションでは、読み込めなかった場合に限り `/status` が同じ行を表示する」という段落が加わりました — [English](https://code.claude.com/docs/en/managed-settings#keys-only-a-managed-source-can-set)
- **ゲートウェイのモデル検出が `description` を表示するようになりました**（v2.1.257）。Claude Code はゲートウェイの応答から `id` と `display_name` に加えて `description` を読み、`/model` ピッカーの各エントリに 1 行に畳んで表示します。`description` を返さないエントリは従来どおり `From gateway` と表示されます。エントリの名前も、`display_name` があればそれを、無ければモデルの `id` を使うと明記されました — [日本語](https://code.claude.com/docs/ja/llm-gateway-protocol#picker-entries-and-caching) / [English](https://code.claude.com/docs/en/llm-gateway-protocol#picker-entries-and-caching) / [English](https://code.claude.com/docs/en/llm-gateway-connect#add-gateway-models-to-the-model-picker)
- **TypeScript Agent SDK に `permissionPrompts` オプションが載りました**（`'host' | 'none'`・既定 `'host'`・v2.1.259 以降）。`'none'` はプロンプトを出すはずだった呼び出しを拒否します（詳細は大幅更新 3 参照）— [English](https://code.claude.com/docs/en/agent-sdk/typescript#options) / [English](https://code.claude.com/docs/en/agent-sdk/permissions#how-permissions-are-evaluated)
- **TypeScript Agent SDK に `user_message_uuids` が加わりました**（Agent SDK v0.3.259 以降）。複数メッセージが 1 ターンにまとめられたとき、そのすべてに応答を突き合わせられます（詳細は大幅更新 3 参照）— [English](https://code.claude.com/docs/en/agent-sdk/typescript#user_message_uuids)
- **`/add-dir` にサブディレクトリを渡すと、その配下のスキル・コマンド・サブエージェントを読み込めるようになりました**（v2.1.257）。主たる作業ディレクトリのサブディレクトリであれば、**そのディレクトリはすでに読める以上、プロンプトも作業ディレクトリの追加も伴わずに、セッションの残りのあいだ設定だけが読み込まれます**。従来は「入れ子の `.claude/skills/` は Claude がそのサブディレクトリ内のファイルを読み書きするまで読み込まれない」だけでしたが、その手前で明示的に読み込む手段ができた形です — [日本語](https://code.claude.com/docs/ja/permissions#additional-directories-grant-file-access-not-configuration) / [English](https://code.claude.com/docs/en/permissions#additional-directories-grant-file-access-not-configuration) / [English](https://code.claude.com/docs/en/skills#discovery-from-parent-and-nested-directories)

**機能改善**

- 単語編集キーが readline 準拠を既定にし、`keybindingFlavor` が非推奨になりました（v2.1.261。詳細はハイライト 1 参照）— [English](https://code.claude.com/docs/en/interactive-mode#make-ctrl-w-delete-back-to-whitespace) / [English](https://code.claude.com/docs/en/settings-reference#keybindingflavor)
- Bash の入力リダイレクト `< file` も `Read` 権限ルールの検査対象になりました（v2.1.257。詳細はハイライト 2 参照）— [English](https://code.claude.com/docs/en/permissions#redirections) / [日本語](https://code.claude.com/docs/ja/large-codebases#block-reads-of-generated-and-vendored-code) / [English](https://code.claude.com/docs/en/large-codebases#block-reads-of-generated-and-vendored-code)
- ネットワークパスを作業ディレクトリに追加できなくなり、専用のエラー節が新設されました（v2.1.257。詳細はハイライト 3 参照）— [English](https://code.claude.com/docs/en/errors#working-directory-is-a-network-path) / [English](https://code.claude.com/docs/en/commands#all-commands)
- strict sandbox mode が、利用者自身が `!` で打つコマンドを対象外にしました（v2.1.260。詳細はハイライト 4 参照）— [English](https://code.claude.com/docs/en/sandboxing#the-unsandboxed-retry-escape-hatch)
- `No response from API` が初回の試行と再試行で別々の待ち時間を使うようになり、メッセージが実際に待った時間を表示するようになりました（v2.1.261。詳細は大幅更新 1 参照）— [English](https://code.claude.com/docs/en/errors#no-response-from-api) / [English](https://code.claude.com/docs/en/network-config#streaming-idle-watchdogs)
- `/mcp` での再接続・再有効化のたびにサーバーのポリシー評価をやり直すようになり、ブロックされている場合は専用のエラーになりました（v2.1.257。詳細は大幅更新 1 参照）— [English](https://code.claude.com/docs/en/errors#mcp-server-is-blocked-by-enterprise-managed-policy) / [日本語](https://code.claude.com/docs/ja/managed-mcp#how-restrictions-appear-to-users) / [English](https://code.claude.com/docs/en/managed-mcp#how-restrictions-appear-to-users)
- 権限ルールが `Tool` / `Tool(content)` の形をしていない場合の専用のエラー節が新設され、**コンテンツ内の括弧がリテラルである**ことが権限のページにも明記されました（v2.1.260 より前は `Mismatched parentheses` として報告されていました。詳細は大幅更新 1 参照）— [English](https://code.claude.com/docs/en/errors#malformed-tool-content-rule) / [English](https://code.claude.com/docs/en/permissions#permission-rule-syntax)
- プラグインのコンポーネントパスの検査が、綴りだけでなく **symlink の行き先**も見るようになりました（v2.1.257。詳細は大幅更新 1 参照）— [English](https://code.claude.com/docs/en/errors#path-escapes-plugin-directory) / [English](https://code.claude.com/docs/en/plugins-reference#path-traversal-limitations)
- **複合コマンドの入れ子にも deny / ask ルールが効くことが明記されました**。サブシェル、コマンド置換、`for` ループの本体など、どこにネストされたサブコマンドでもマッチすれば適用され、`Bash(git clean *)` の ask ルールは `cd /tmp && git clean -f` でも `echo "$(git clean -f)"` でも、**auto モードであってもプロンプトを出します** — [English](https://code.claude.com/docs/en/permissions#compound-commands)
- **`cd` と組み合わせたときにプロンプトが出るケースの項目名が「`cd` と出力リダイレクト」から「`cd` とリダイレクト」に一般化されました**。入力リダイレクトも検査対象になったことに追随した変更で、`/dev/null` だけがターゲットのコマンドはプロンプトを出さない点は変わりません — [English](https://code.claude.com/docs/en/permissions#read-only-commands)
- **gitignore パターンとして使えないパスの扱いが明記されました**。deny / ask ルールならそのパスちょうどを守り、allow ルールの場合は何も承認しません。あわせて `Edit(./Finance (2024)/**)` のように括弧を含むパスはエスケープ不要であることが示されました — [English](https://code.claude.com/docs/en/permissions#read-and-edit)
- **不要不急トラフィックを止めてもゲートウェイのモデル検出は走るようになりました**（v2.1.257）。リクエストがあなたのゲートウェイにしか行かないためで、`CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` の説明からも検出が停止対象の一覧から外れ、代わりに「**モデル検出には影響しない。あちらには独自のオプトインがある**」が末尾に加わりました。以前は「検出はゲートウェイ自身に問い合わせるにもかかわらず停止し、キャッシュのモデル一覧が使われ続ける」と書かれていたので、記述の向きが反転しています — [日本語](https://code.claude.com/docs/ja/llm-gateway-protocol#when-discovery-runs) / [English](https://code.claude.com/docs/en/llm-gateway-protocol#when-discovery-runs) / [English](https://code.claude.com/docs/en/llm-gateway-connect#turn-off-traffic-outside-the-gateway-path)
- **ゲートウェイのモデル検出でカスタムヘッダーが組み込みヘッダーを差し替えることが明記されました**。`ANTHROPIC_CUSTOM_HEADERS` のヘッダーに空でない値があれば、同名の組み込みヘッダーの代わりに送られます（名前の一致は大文字小文字を区別しません）。ただし**資格情報を `ANTHROPIC_CUSTOM_HEADERS` だけで渡した場合、Claude Code は依然として検出をスキップします**。ピッカーで既存の行に畳まれる条件も、1 段落だった説明が「同じ ID の場合」「組み込みエイリアスと同じモデルの場合」の 2 項目に整理されました — [日本語](https://code.claude.com/docs/ja/llm-gateway-protocol#request-and-response) / [English](https://code.claude.com/docs/en/llm-gateway-protocol#request-and-response)
- **クラウド環境のドメイン許可リストで、アーティファクトのホストが原則不要になりました**。従来は「セッションがアーティファクトを扱うなら `*.frame.claudeusercontent.com` を含めよ。含めないとアーティファクトを読めない」でしたが、今回「**含めなくてもセッションはアーティファクトを読める。Claude Code は Anthropic へのセッション接続経由でアーティファクトの内容を読むため**」に反転しました。許可リストに残すべき場合として、**他組織の公開アーティファクトを開くとき**（この場合は直接ホストから取得する）と、**ローカル CLI やセルフホストのランナーを設定しているとき**の 2 つが挙げられています — [English](https://code.claude.com/docs/en/cloud-environments#allow-specific-domains)
- **リモートコントロールがポリシーで無効になる原因に「そもそもポリシーを読み込めていない」場合が加わりました**。導入文にも「ポリシーがブロックしている、**または Claude Code がこのマシンで組織のポリシーを読み込めず、その間リモートコントロールを切ったままにしている**」が追記され、原因の 2 番目として「`claude doctor` を実行して `Organization policy` の行を読め。ポリシーが読み込まれていないと出ていれば、それがリモートコントロールを切っている原因である」が挿入されました（v2.1.261 より前の `claude doctor` はこの行を出しません）— [English](https://code.claude.com/docs/en/remote-control#remote-control-is-disabled-by-your-organizations-policy)
- **リモート MCP サーバーを削除すると、そのサーバー用に保存していた OAuth トークンとクライアント登録も削除されるようになりました** — [English](https://code.claude.com/docs/en/mcp#managing-your-servers)
- 割り込みレシートの `still_queued` の意味が「割り込みを生き延びるメッセージ」から「**割り込みが到着した時点で保留中だったメッセージ**」に改められ、最初のターンが始まる前に割り込んだ場合の挙動が加わりました（詳細は大幅更新 3 参照）— [English](https://code.claude.com/docs/en/agent-sdk/typescript#sdkcontrolinterruptresponse)
- `ambient` フラグの定義が「Claude Code が自分の運用のために起動するタスク」から「**セッションの作業の一部ではないタスク**」に広がり、**利用者が頼んだライブ更新の watcher も ambient に含まれる**ことが明記されました。`SDKBackgroundTasksChangedMessage` の発火条件にもタスクの `description` の変化が加わっています（詳細は大幅更新 3 参照）— [English](https://code.claude.com/docs/en/agent-sdk/typescript#sdktaskstartedmessage)
- **worktree の分離チェックのうち「コマンドの形」の判定の説明が絞り込まれました**。従来の「git をまったく実行しないコマンドであっても、worktree の中に留まると検証できないコマンドはブロックする」が、「**コマンドのテキストから、そのコマンドが実行する git が worktree の中に留まると検証できない場合にブロックする。たとえばコマンド名が実行時に決まる場合や、構文が解析できない場合**」に変わりました。同じ書き換えがサブエージェントのページの worktree 分離の説明にも入っています — [English](https://code.claude.com/docs/en/worktrees#how-claude-code-enforces-isolation) / [English](https://code.claude.com/docs/en/sub-agents#write-subagent-files)
- **`DirectoryAdded` フックが発火しない条件に「すでに作業ディレクトリの配下にあるディレクトリを追加した場合」が加わりました**。従来は「すでに作業ディレクトリであるディレクトリを追加した場合（追加はエラーで失敗する）」でしたが、上記の「サブディレクトリを渡すと設定だけ読み込む」挙動が入ったことで、エラーにならず発火もしない経路ができたためと読めます — [English](https://code.claude.com/docs/en/hooks#directoryadded)
- **ディープリンクの `cwd` パラメータが `..` セグメントを含むパスも拒否するようになりました**（従来はネットワーク／UNC パスと、不可視文字・双方向制御文字を含むパスのみ）— [English](https://code.claude.com/docs/en/deep-links#build-a-link)
- **非対話モードの API 再試行イベントに `no_response` フィールドが加わりました**（v2.1.261。詳細は大幅更新 1 参照）— [English](https://code.claude.com/docs/en/headless#handle-api-retries)
- ターミナル設定のページで、貼り付けプレースホルダを削除したあとに `Ctrl+Y` で戻せる条件が、特定のキー名の列挙から「**単語または行の削除ショートカットの後**」に一般化されました（詳細はハイライト 1 参照）— [English](https://code.claude.com/docs/en/terminal-config#paste-large-content)
- アクセシビリティのページで、スクリーンリーダーが読み上げる削除操作の一覧に `Alt+D` が加わりました（詳細はハイライト 1 参照）— [English](https://code.claude.com/docs/en/accessibility#what-your-screen-reader-hears)
- 環境変数 `TASK_MAX_OUTPUT_LENGTH` の説明が「サブエージェント出力の切り詰め上限」から「**バックグラウンドタスクの出力のうち `TaskOutput` ツールが保持する最大文字数**」に変わりました（詳細はハイライト 5 参照）— [English](https://code.claude.com/docs/en/env-vars#variables)

**バグ修正**

- v2.1.263（原文の日付表記は 2026年09月06日）が加わりましたが、内容は「バグ修正と信頼性の改善」の 1 行のみで、個別の修正は列挙されていません

**その他**

- 管理設定の例のコメントが「Sandbox every command」から「**Sandbox every command Claude runs**」に直されました（詳細はハイライト 4 参照）— [English](https://code.claude.com/docs/en/settings-example#an-organizations-managed-settings)
- ツールリファレンスの「Edit ツールの挙動」節から、deny ルールが適用される Bash コマンドの重複説明が丸ごと落ち、権限のページの「Read と Edit の権限ルール」への参照 1 文に置き換わりました（詳細はハイライト 2 参照）— [English](https://code.claude.com/docs/en/tools-reference#edit-tool-behavior)
- スキルのページで、入れ子の `.claude/skills/` が読み込まれる条件の記述が「そのサブディレクトリ内のファイル」から「**それらを含むサブディレクトリ内のファイル**」に精密化され、末尾の言い回しも「名前で呼び出せない」から「あなたが名前で呼び出せない」に整えられました。注入コマンドの出力サイズの節でも、参照先の説明が「どの変数がどの境界を調整するか」から「**各境界をどう調整するか**」に改められています（`bashOutputMaxChars` が環境変数以外の調整手段として加わったことへの追随と読めます）— [English](https://code.claude.com/docs/en/skills#discovery-from-parent-and-nested-directories)
- SDK の `canUseTool` の説明が 2 段落に分けられ、「**`dontAsk` モードなど、Claude Code がコールバックを呼ばない構成がある**。どれがそれにあたるかと、その場合に呼び出しがどう扱われるかは「権限の評価順」の最終段が述べる」という案内が挿入されました — [日本語](https://code.claude.com/docs/ja/agent-sdk/user-input#handle-tool-approval-requests) / [English](https://code.claude.com/docs/en/agent-sdk/user-input#handle-tool-approval-requests)

## 新着情報

（今回の対象期間には `whats-new/` 配下のページに差分がありませんでした。差分のあった 32 ページはいずれもリファレンス・ガイド系です。最新の週間ダイジェストは 5 回前のサマリで扱った Week 34（2026年08月17日～21日）のままで、新しい週のダイジェストの追加も既存ページの訂正もありません。`whats-new/` の無差分は 5 回連続です）

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-09-04.md](./archives/latest/2026-09-04.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-09-04.md](./archives/latest-detail/2026-09-04.md)

<!--
base_commit: 3f57b81e5934ecd89be2d817677dfcfdba5da98f
head_commit: 79f96cfde0b383e61550570a0d780c890e54cf66
generated_at_full: 2026-09-06T15:00:28+09:00
-->
