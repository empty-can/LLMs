---
対象期間: 2026年09月04日 〜 2026年09月05日
作成日: 2026-09-05
---

# Claude Code 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
今回も 1 日分の取り込みで、差分があったのは `llms-full.txt` の 1 ファイルだけ、32 ページ・1,158 行（追加 671・削除 487）です。ただし生の行数の大半は表の桁揃えで、桁揃えノイズを潰した実質では 396 行（追加 290・削除 106）―― 前回の実質 387 行とほぼ同じ規模になります。ノイズ 762 行のうち 700 行が環境変数リファレンス 1 ページの桁揃えでした。今回の性格を一言でいうと「**前回サマリで「本文が届いていない持ち越し」と書いた 7 件が、そのまま全部届いた回**」で、エラーリファレンスの 3 節・設定リファレンスの 2 キー・TypeScript Agent SDK の 1 フィールド・インタラクティブモードの見出し改称がそれにあたります。ページの新規追加・削除はなく（展開ページ数は前後とも 191）、`llms.txt` とページ見出しマップは 2 回ぶりに無差分に戻ったため、**新たな持ち越しは 0 件**です。`whats-new/` は 5 回連続で差分がありません。

主要なものを以下に挙げます。

1. `Ctrl+W` などの単語編集キーが readline 準拠を既定にし、`keybindingFlavor` 設定が非推奨になった
2. Bash の入力リダイレクト `< file` も Read 権限ルールの検査対象になった
3. ネットワークパスを作業ディレクトリに追加できなくなり、専用のエラー節が新設された
4. strict sandbox mode が、利用者自身が `!` で打つコマンドを対象外にした
5. `bashOutputMaxChars` と `taskOutputMaxChars` で、Claude がインラインで受け取る出力量を上げられるようになった
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**単語編集キーが readline 準拠を既定にし、`keybindingFlavor` が非推奨になった**](#1-単語編集キーが-readline-準拠を既定にしkeybindingflavor-が非推奨になった):  
  インタラクティブモードの節が `Make editing keys follow readline conventions` から **`Word boundaries in editing shortcuts`（編集ショートカットの単語境界）** に改称され、**`Ctrl+W` は既定で「前の単語」ではなく「前の空白」まで削除する**ようになった。`Alt+F` と `Alt+D` も単語の終わりで止まる。設定でこれを有効にしていた `keybindingFlavor` は v2.1.261 で非推奨・無効となり、設定リファレンスの項目が丸ごと警告ブロックに置き換わっている。
2. [**Bash の入力リダイレクト `< file` も権限チェックの対象になった**](#2-bash-の入力リダイレクト--file-も権限チェックの対象になった):  
  権限のページの `Redirections` 節が全面的に書き直され、**出力リダイレクト（`>` `>>` `2>`）は `Edit` ルール、入力リダイレクト（`< file`）は `Read` ルールに照らして検査する**という 2 本立てになった。入力側の検査は v2.1.257 以降。あわせて「実体の無いターゲットは検査しない」対象（`/dev/null`・`2>&1` などの FD 形式・ヒアドキュメント）が明示された。
3. [**ネットワークパスを作業ディレクトリに追加できなくなった**](#3-ネットワークパスを作業ディレクトリに追加できなくなった):  
  エラーリファレンスに `Working directory is a network path` の節が新設された。**ネットワークパスの解決はそのパスが名指すホストに接触しうるし、Windows ではその接触で資格情報が送られうる**ため、Claude Code は解決を試みずにパスを拒む。UNC 共有・`/net/<host>` の automount・シンボリックリンク経由でネットワークに届くローカルパスが対象で、マップ済みのドライブレターと `\\wsl$` は対象外。
4. [**strict sandbox mode が `!` で打つコマンドを対象外にした**](#4-strict-sandbox-mode-が--で打つコマンドを対象外にした):  
  サンドボックスのページで、`allowUnsandboxedCommands: false` の説明が「すべてのコマンド」から「**Claude が実行するすべてのコマンド**」に限定された。**利用者自身がシェルモードで打つコマンドはサンドボックスの外で走る**（例外はバックグラウンドセッションと、Linux で `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB` を設定したセッションの 2 つ）。v2.1.260 より前は、strict sandbox mode がすべてのセッションでシェルモードのコマンドもサンドボックス化していた。
5. [**`bashOutputMaxChars` と `taskOutputMaxChars` が追加された**](#5-bashoutputmaxchars-と-taskoutputmaxchars-が追加された):  
  設定リファレンスに 2 つのキーが新設された（v2.1.261 以降）。**Claude がインラインで受け取る出力量を、コマンド出力は既定 30,000 文字から、バックグラウンドタスク出力は既定 32,000 文字から、それぞれ最大 128,000 文字まで引き上げられる**。設定すると対応する環境変数（`BASH_MAX_OUTPUT_LENGTH` / `TASK_MAX_OUTPUT_LENGTH`）は無視される。
<!-- light:highlight-list:end -->

## 1. 単語編集キーが readline 準拠を既定にし、`keybindingFlavor` が非推奨になった

インタラクティブモードのページで、**`Make editing keys follow readline conventions`（編集キーを readline 規約に従わせる）** 節が **`Word boundaries in editing shortcuts`（編集ショートカットの単語境界）** に改称され、内容も「設定でこう変えられる」から「**これが既定の挙動である**」に書き換わりました（このページの実質 29 行のうち大半がこの節）。従来 `keybindingFlavor` を `"readline"` にして初めて得られた挙動が、v2.1.261 で全員の既定になった形です。

キー表の 3 行が実際に書き換わっています。**`Ctrl+W` は「前の単語を削除」から「前の空白まで削除」へ** ―― 1 回押せばパスや `--flag=value` が丸ごと消えます。単語だけ消したい場合は macOS の `Option+Delete`、Windows の `Ctrl+Backspace` を使えと案内されました。**`Alt+F` は「次の単語の先頭へ」から「現在の単語の終わりへ」**（単語間にカーソルがあるときは次の単語の終わりへ）、**`Alt+D` は「単語の後ろの空白まで削除」から「現在の単語の終わりまで削除」** になり、あわせて削除内容が貼り付け用に保存されるようになりました。`Ctrl+Y` の説明からは `keybindingFlavor` への言及が消え、「単語・行の削除ショートカットで最後に消したテキストを貼り付ける」という一般的な書き方になっています。

新しい節の本文は 3 点にまとまりました。**単語は英数字の連続**で、`_`・`.`・`/` などの句読点が単語を区切ります（プロンプトに `src/utils/foo.ts` があるとき、`Alt+B` を繰り返すと `ts`・`foo`・`utils`・`src` の頭で止まる）。**`Ctrl+W` だけは別で、句読点を無視して前の空白まで消す**ため、1 回で `src/utils/foo.ts` 全体が消えます。そして **中国語や日本語のように空白で区切らない文章でも、単語ショートカットは 1 単語ずつ動く**という記述が新たに加わりました。これらのショートカットが `keybindings.json` で再マップできない点は従来どおりです。

設定リファレンス側では **`keybindingFlavor` の項目が丸ごと警告ブロックに置き換わりました**。「v2.1.261 以降は非推奨で効果を持たない。プロンプトの単語編集キーは常に readline 規約に従う。ただし `keybindingFlavor` は引き続き受け付けるので、これを設定した設定ファイルが無効になることはない」という内容です。値の一覧（`"classic"` が既定）と JSON の例、および解説へのリンクは削除され、代わりに「v2.1.238 から v2.1.260 では `"readline"` にすると `Ctrl+W` が前の単語ではなく前の空白まで削除した」という履歴の 1 文と、**型は `"classic"` または `"readline"`・既定は `unset`**（従来は既定 `"classic"`）という簡略な記述だけが残りました。全設定の一覧表でも、この行の説明が「`Ctrl+W` を Bash のように空白まで削除させる」から「非推奨で効果を持たない」に差し替わっています。

**この改称は前回サマリで「ページ見出しマップには現れているのに本文が届いていない」持ち越しとして挙げた 7 件のうちの 1 つ**です（前回は「キーバインドの改称」と書きましたが、実体はインタラクティブモードのページの節でした）。周辺 2 ページにも波及しており、ターミナル設定のページでは貼り付けプレースホルダを消したときの `Ctrl+Y` の案内が特定のキー名の列挙から「単語・行の削除ショートカットの後」に一般化され、アクセシビリティのページではスクリーンリーダーが読み上げる削除操作の一覧に `Alt+D` が加わりました。

- [Interactive mode - Claude Code Docs (English)](https://code.claude.com/docs/en/interactive-mode#make-ctrl-w-delete-back-to-whitespace)
- [Claude Code settings reference - Claude Code Docs (English)](https://code.claude.com/docs/en/settings-reference#keybindingflavor)

## 2. Bash の入力リダイレクト `< file` も権限チェックの対象になった

権限のページの **`Redirections`（リダイレクト）** 節が全面的に書き直されました。従来は「出力リダイレクトのターゲットをファイル書き込みとして検査する」という 1 段落でしたが、**「コマンドが出力または入力をリダイレクトするとき、Claude Code はそのターゲットを、Claude が直接そのファイルを書いた／読んだ場合と同じようにファイルルールに照らして検査する」** という前置きのもと、出力と入力の 2 項目に分かれています。

**出力リダイレクト**（`> file`・`>> file`・`2> file`）の扱いは従来どおりで、`Edit` の allow / deny ルール、[日本語](https://code.claude.com/docs/ja/permission-modes) / [保護パス](https://code.claude.com/docs/en/permission-modes)、作業ディレクトリを検査対象とします。`Bash(git commit *)` のようなルールはコマンドを許可するのであってターゲットを許可するものではない、`~` で始まるターゲットやグロブ文字を含むターゲットは承認が要る、という点も変わりません。

新しいのは**入力リダイレクト**（`< file`）で、こちらは **`Read` の allow / deny ルールと作業ディレクトリ**を検査します。作業ディレクトリの外にあるターゲットは、allow ルールでカバーされていない限り承認が要ります。さらに **グロブパターンを含むターゲットと、同じコマンド内の `cd` に続く相対パスは、allow ルールでカバーされていても承認が要る**とされました。**入力側のターゲットを検査するのは Claude Code v2.1.257 以降**です。あわせて、**実体としてのファイルが背後に無いターゲットは検査しない**ことが明示されました ―― `/dev/null`、`2>&1` や `<&3` のようなファイルディスクリプタ形式、ヒアドキュメントとヒア文字列がこれにあたります。

この変更は 3 ページに波及しています。権限のページ自身の「Read と Edit」節の警告文、設定リファレンスの `permissions.deny` の説明、大規模コードベースのページの deny ルールの説明が、いずれも「Claude の組み込みファイルツールと、Bash で認識するファイルコマンド（`cat`・`head`・`tail`・`sed`）に適用される」に **「および `> file` や `< file` のような Bash リダイレクトのターゲット」を足した形**に揃えられました。大規模コードベースのページでは同時に、`grep -r` や `find` でディレクトリを走査した場合の記述が「Claude は依然として拒否パスを見る」から「**拒否ファイルを含むディレクトリを走査すれば、その出力には依然としてそれらが含まれる**」に精密化されています。ツールリファレンスの側は逆に、これまで重複して書かれていた deny ルールの説明（認識されるコマンドの一覧と、read-before-edit のリストとは一致しないという注記）が丸ごと落ち、**権限のページの「Read と Edit の権限ルール」への参照 1 文に置き換わりました**。

なお同じ節の近くでは、**複合コマンドの入れ子にも deny / ask ルールが効くこと**が新たに明記されました。サブシェル、コマンド置換、`for` ループの本体など、どこにネストされたサブコマンドでもマッチすれば適用され、`Bash(git clean *)` の ask ルールは `cd /tmp && git clean -f` でも `echo "$(git clean -f)"` でも、**auto モードであってもプロンプトを出します**。権限ルール構文の節にも「**スペシファイア内の括弧はリテラルなので、括弧を含むコマンドやパスはエスケープ不要**」という 1 文が加わりました（後者はハイライトに挙げていない `Malformed Tool(content) rule` の新設と対になっています。詳細は大幅更新 1 参照）。

- [Configure permissions - Claude Code Docs (English)](https://code.claude.com/docs/en/permissions#redirections)
- [Claude Code settings reference - Claude Code Docs (English)](https://code.claude.com/docs/en/settings-reference#permissions-deny)

## 3. ネットワークパスを作業ディレクトリに追加できなくなった

エラーリファレンスに **`Working directory is a network path`（作業ディレクトリがネットワークパスである）** の節が新設されました。理由の説明が的確で、**ネットワークパスを解決しようとするとそのパスが名指すホストに接触することがあり、Windows ではその接触でホストに資格情報が送られうる。だから Claude Code は解決を試みずにパスを拒む**、というものです。`/add-dir` を実行したときに出るほか、起動時の警告としても出ます（起動時に出た場合、Claude Code はそのディレクトリ抜きで起動します）。

拒否されるパスは 3 種類挙げられました。**`\\server\share` のような UNC 共有**、**`/net/<host>` のような automount パス**（ただし、そのホストの automount 配下のディレクトリから Claude Code を起動した場合を除く）、**シンボリックリンクやジャンクションを経由してネットワーク上の場所に届くローカルパス**です。逆に **マップ済みのドライブレターと `\\wsl$` のパスはネットワークパスとして扱われません**。

対処は 3 つで、Windows では `net use Z: \\server\share` のように共有をドライブレターに割り当てたうえで、起動時に `claude --add-dir Z:\` として渡すこと（**セッションの途中で足したドライブレターはまだリモート読み取りの信頼を引き継がない**とエラーメッセージ自身が断っています）、macOS と Linux では共有をローカルパスにマウントしてそのパスを追加すること、そして `permissions.additionalDirectories` に書いてある場合はその設定ファイルから外すことです。**v2.1.257 より前は、到達可能なネットワークパスをそのまま作業ディレクトリとして受け入れていました**。

この制限は 3 ページに同じ趣旨で反映されました。権限のページの「作業ディレクトリ」節には「**ほとんどのネットワークパスは作業ディレクトリとして追加できない。ルックアップがホストに接触しうるため。Windows ではドライブレターに割り当てて起動時に `--add-dir` で渡せ**」という 1 段落が加わり、CLI リファレンスの `--add-dir` 行とコマンドリファレンスの `/add-dir` 行にも同じ制限の 1 文が入っています。**この節も前回の持ち越し 7 件のうちの 1 つ**でした。

- [Error reference - Claude Code Docs (English)](https://code.claude.com/docs/en/errors#working-directory-is-a-network-path)
- [Configure permissions - Claude Code Docs (English)](https://code.claude.com/docs/en/permissions#working-directories)

## 4. strict sandbox mode が `!` で打つコマンドを対象外にした

サンドボックスのページで、**strict sandbox mode（`sandbox.allowUnsandboxedCommands` を `false` にした状態）が何を対象にするか**が限定されました。従来の「無効化すると `dangerouslyDisableSandbox` パラメータは完全に無視され、**すべてのコマンド**がサンドボックス化されるか `excludedCommands` に明示されている必要がある」という 1 文が、「**Claude が実行するすべてのコマンド**が…」に書き換えられています（実質 17 行のうち大半がこの節）。

続けて新しい段落が加わりました。**strict sandbox mode は Claude が実行するコマンドに適用されるのであって、利用者自身が `!` シェルモードのプロンプトで打つコマンドはサンドボックスの外で走る**、というものです。例外は 2 つで、**バックグラウンドセッション**（strict sandbox mode がシェルモードのコマンドもカバーする）と、**Linux で [`CLAUDE_CODE_SUBPROCESS_ENV_SCRUB`](https://code.claude.com/docs/en/env-vars#variables) を設定したセッション**（シェルモードを含めすべてのコマンドがサンドボックス化される）です。そして **v2.1.260 より前は、strict sandbox mode がすべてのセッションでシェルモードのコマンドもサンドボックス化していた**と明記されました。つまり**対象が狭まった**方向の変更です。

インタラクティブモードのシェルモードの節にも、同じ内容が利用者視点で 1 段落追加されました ―― 「通常の対話セッションでは、サンドボックスを有効にしていてもシェルモードで打ったコマンドはサンドボックスの外で走る。サンドボックスは Claude が実行するコマンドに適用されるためである」。組織向けの節でも同じ整理が入り、「**この構成は Claude が実行するコマンドをサンドボックス化する。開発者は `!` プロンプトでコマンドを打てば、Claude Code の外のターミナルで持っているのと同じアクセス権のまま、サンドボックスの外で実行できる**」という但し書きが加わりました。設定例のページで管理設定のコメントが「Sandbox every command」から「**Sandbox every command Claude runs**」に直されたのも、この整合を取るためと読めます。

設定リファレンス側でも 4 か所が追随しました。`sandbox.allowUnsandboxedCommands` の説明が「すべてのコマンドがサンドボックス化されるか `excludedCommands` に現れる必要がある」から「**Claude が実行するすべてのコマンド**が…」になり（値の説明も同様）、**Strict sandbox mode という表示名の説明が同じ文の中から独立した 1 文に分けられ**、末尾に「利用者自身が `!` シェルモードで打つコマンドがいつサンドボックス化されるかは strict sandbox mode を参照せよ」という案内が加わりました。あわせて `sandbox.excludedCommands` の既定値の説明が「未設定なので、サンドボックス化できるコマンドはすべてサンドボックス化される」から「**未設定なので、どのコマンドも除外されない**」に改められています。サンドボックスのトラブルシューティングでは、`git` が `unable to unlink old` で失敗するケースの記述が 1 つの長い箇条書きから 2 段落に分割され、リンク先も総論的な「サンドボックスモード」から具体的な「サンドボックス化されていない再試行のエスケープハッチ」に直されました。

- [Configure the sandboxed Bash tool - Claude Code Docs (English)](https://code.claude.com/docs/en/sandboxing#the-unsandboxed-retry-escape-hatch)
- [Interactive mode - Claude Code Docs (English)](https://code.claude.com/docs/en/interactive-mode#shell-mode-with-prefix)

## 5. `bashOutputMaxChars` と `taskOutputMaxChars` が追加された

設定リファレンスに **`bashOutputMaxChars`** と **`taskOutputMaxChars`** の 2 キーが新設されました（いずれも「メモリとコンテキスト」分類・スコープは任意の設定ファイル・**Claude Code v2.1.261 以降**）。**これも前回の持ち越しで、前回時点ではページ見出しマップにキー名だけが現れて本文が届いていなかった 2 件**です。

**`bashOutputMaxChars`** は、成功した Bash / PowerShell コマンドの出力のうち **Claude がインラインで受け取る文字数**を決めます。上限を超えた分は Claude Code がファイルに保存し、Claude には短いプレビューとファイルのパスが渡ります。冗長なビルドやテストスイートの全ログのように常時あふれる出力を、ファイルを開かずに読ませたいときに引き上げる想定です。**型は正の整数で、`4000` から `128000` の範囲にクランプ**されます。**既定は未設定＝インライン 30,000 文字まで**。**このキーを設定すると、環境変数 `BASH_MAX_OUTPUT_LENGTH` は無視されます**。

**`taskOutputMaxChars`** は、Claude が `TaskOutput` ツールで[バックグラウンドタスク](https://code.claude.com/docs/en/tools-reference#background-commands)を読むときに **インラインで受け取る文字数**です。終了したタスクの出力がこれより長い場合、**Claude が受け取るのは最新の側の文字列**です。クランプ範囲は同じ `4000`〜`128000`、**既定は未設定＝32,000 文字**で、設定すると環境変数 `TASK_MAX_OUTPUT_LENGTH` が無視されます。

ツールリファレンスの「出力の上限」節では、この 2 キーと既存の環境変数の**役割の違い**が整理されました。`BASH_MAX_OUTPUT_LENGTH` が変えるのは「作業ファイルからコマンドの結果へ読み戻す窓」（および失敗時の抜粋を切り出す窓）だけで、**インラインの上限そのものは上がらない** ―― 30,000 文字を超える正常結果は、この変数をいくら上げてもファイルパス＋プレビューとして届きます。対して **`bashOutputMaxChars` はインラインの上限と読み戻し窓を一緒に動かす**ため、128,000 文字までなら本当にインラインで受け取れます。表の「正常」の行にも「既定では」という限定が入りました。

環境変数リファレンス側では、**`TASK_MAX_OUTPUT_LENGTH` の説明が意味ごと書き換わっている**点に注意が要ります。従来は「[日本語](https://code.claude.com/docs/ja/sub-agents) / [サブエージェント](https://code.claude.com/docs/en/sub-agents)の出力が切り詰められるまでの最大文字数。切り詰め時は全文をディスクに保存してパスを返す」でしたが、今回「**バックグラウンドタスクの出力のうち `TaskOutput` ツールが保持する最大文字数**」に変わり、切り詰め時の挙動の説明も落ちて、代わりに `taskOutputMaxChars` を設定すると無視される旨が加わりました。`BASH_MAX_OUTPUT_LENGTH` の行にも同じ「設定すると無視される」の 1 文が入っています。

- [Claude Code settings reference - Claude Code Docs (English)](https://code.claude.com/docs/en/settings-reference#bashoutputmaxchars)
- [Tools reference - Claude Code Docs (English)](https://code.claude.com/docs/en/tools-reference#output-limits)

## 新規追加されたページ

<!-- light:new-pages:start -->
（今回の対象期間に新規追加・削除されたドキュメントページはありません。`llms-full.txt` に展開されているページ数は前後とも 191 で、`llms.txt` も収録 URL 202 件・全体 356 行のまま無差分です。2 回連続で差分の出ていた `llms.txt` と、前回 52 行の差分があったページ見出しマップの双方が今回は無差分で、差分は `llms-full.txt` の 1 ファイルに閉じています）
<!-- light:new-pages:end -->

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
- [**エラーリファレンス**](#1-エラーリファレンス) ([English](https://code.claude.com/docs/en/errors#no-response-from-api)):  
  新しい節が 3 つ加わり、`No response from API` が全面的に書き直された。初回の試行と再試行で応答ヘッダーの待ち時間が別々になり、エラーメッセージが実際に待った時間を表示するようになっている。冒頭のメッセージ対応表にも 3 行が入った。今回の最大差分（実質 93 行 = 追加 83・削除 10）。
- [**設定リファレンス**](#2-設定リファレンス) ([English](https://code.claude.com/docs/en/settings-reference#bashoutputmaxchars)):  
  `bashOutputMaxChars` と `taskOutputMaxChars` が新設され、`keybindingFlavor` が非推奨の警告ブロックに置き換わった。サンドボックス系 4 か所と `permissions.deny` の記述も、対象を「Claude が実行するコマンド」に限定する方向へ揃えられている（実質 66 行 = 追加 48・削除 18）。
- [**TypeScript Agent SDK リファレンス**](#3-typescript-agent-sdk-リファレンス) ([English](https://code.claude.com/docs/en/agent-sdk/typescript#user_message_uuids)):  
  `user_message_uuids` フィールドが新設されたほか、割り込みレシートの意味・`ambient` フラグの定義・`permissionPrompts` オプションの記載が改まった。閾値を 1 行だけ超えた（実質 51 行 = 追加 37・削除 14）。
<!-- light:updated-pages:end -->

## 1. エラーリファレンス

エラーリファレンスは今回の最大差分です（実質 93 行 = 追加 83・削除 10。生の差分でも同じ 93 行で、桁揃えノイズはありません）。**加わった節は 3 つで、いずれも前回サマリで「持ち越し」として名指ししたもの**です。うち `Working directory is a network path` はハイライト 3 で扱ったので、残る 2 つを先に述べます。

**`MCP server is blocked by enterprise managed policy`**（設定の警告）は、`/mcp` でサーバーの **Reconnect** を選ぶ、または無効化していたサーバーを有効に戻したときに、[日本語](https://code.claude.com/docs/ja/managed-mcp) / [MCP サーバーを制限する設定](https://code.claude.com/docs/en/managed-mcp)がそのサーバーをブロックしていた場合のメッセージです。原因になりうる設定が 4 つ列挙されました ―― サーバーにマッチする `deniedMcpServers` エントリ（**自分の `~/.claude/settings.json` やプロジェクトの `.claude/settings.json` にあるものも含む**）、サーバーがマッチしない `allowedMcpServers` リスト、`mcp` をロックした `strictPluginOnlyCustomization`、そしてサーバーが claude.ai コネクタである場合の `disableClaudeAiConnectors` です。対処は「まず自分のユーザー設定とプロジェクト設定を確認し、それで説明がつかなければ管理者に尋ねる」。**v2.1.257 より前は、セッション中にポリシーが更新されてブロック対象になったサーバーでも、`/mcp` の Reconnect や再有効化で接続できてしまっていました**。管理 MCP のページ側にも、サーバー読み込み前の 3 段のチェックについて「**利用者が `/mcp` でサーバーを再接続する／無効化したものを戻すときにも再実行する**」という 1 文が加わり、利用者から見た挙動の表にもこのメッセージの行が入りました（従来は「ポリシーでブロックされたサーバーは警告なく `/mcp` と `claude mcp list` から消える」の 1 行だけでした）。

**`Malformed Tool(content) rule`**（設定の警告）は、権限ルールが `Tool` または `Tool(content)` の形をしていない場合 ―― 閉じ括弧の後ろに文字が続く、括弧の片方が無いなど ―― に出ます。Claude Code はそのルールを飛ばし、対話セッション開始時の不正設定ダイアログと `claude doctor` の出力に列挙します。メッセージ自身が対処を含んでおり、「ルールは `Tool` または `Tool(content)` の形を取り、閉じ括弧で終わらなければならない。**コンテンツ内の括弧はリテラルである**」と述べます。対処は「`Bash(ls) x` を `Bash(ls *)` のように書き直す」ことと「**コンテンツ内の括弧はそのままにする** ―― リテラルなので `Edit(./Finance (2024)/**)` のようなルールはエスケープ無しで妥当」の 2 点です。**v2.1.260 より前は、括弧が対応していないルールを `Mismatched parentheses` として報告していました**。権限のページ側でも、ルール構文の節に「スペシファイア内の括弧はリテラル」の 1 文が、パスパターンの節に「**パスの括弧はエスケープ不要**」と「**gitignore パターンとして使えないパスでも、deny / ask ルールならそのパスちょうどを守る。allow ルールで使えないパターンを書いた場合は何も承認しない**」の 2 文が加わりました。

**もう 1 つの大きな変更が `No response from API` の全面改稿**です。これは前回サマリで v2.1.261 の changelog 由来の「機能改善」として 1 行触れた項目（「レスポンスヘッダーを返さない場合の再試行が、もう 3 分ではなく `API_TIMEOUT_MS` まで待つ」）の本文化にあたります。要点は**初回の試行と再試行で待ち時間を別々に決めるようになった**ことです。**初回**は `CLAUDE_STREAM_FIRST_BYTE_TIMEOUT_MS` を設定していればその値（10 秒〜30 分にクランプ）、していなければ[ストリーミングのアイドル監視](https://code.claude.com/docs/en/network-config#streaming-idle-watchdogs)のバイト単位のタイムアウト値を使い、どちらの場合もリクエストボディ 32KB ごとに 1 秒を足します。**再試行**は `API_TIMEOUT_MS` から 1 秒引いた値、つまり既定では 10 分弱で、**生成が終わるまでレスポンスを握って離さないプロキシやゲートウェイを再試行の側で持ちこたえられるように**この設計になっている、と説明されました（Amazon Bedrock では再試行も初回と同じ期限を使い、メッセージには時間が 1 つだけ出ます）。

**エラーメッセージ自体も変わりました**。従来の `API Error: No response from API` だけだったものが、`API Error: No response from API (waited 3m, then 10m on the retry). If a proxy or gateway on your network holds responses until they complete, raise API_TIMEOUT_MS or CLAUDE_STREAM_FIRST_BYTE_TIMEOUT_MS to wait longer.` のように、**実際に待った時間と対処を含む形**になっています。対処の一覧も、従来の「遅いネットワークでは `CLAUDE_STREAM_FIRST_BYTE_TIMEOUT_MS` を設定するか `API_TIMEOUT_MS` を監視タイムアウトより上げる」の 1 項目が、「**プロキシやゲートウェイが応答を握る場合は `API_TIMEOUT_MS` を上げて再試行を長く待たせる**（Bedrock では `CLAUDE_STREAM_FIRST_BYTE_TIMEOUT_MS` も上げる）」と「**初回だけ毎回タイムアウトして再試行では成功する場合は `CLAUDE_STREAM_FIRST_BYTE_TIMEOUT_MS` を上げる**」の 2 項目に分かれました。末尾には「**v2.1.261 より前は、再試行も初回と同じ期限で待ち、メッセージに時間は出なかった**」が加わっています。「再試行の予算」の表では `API_TIMEOUT_MS` の説明が「first-byte deadline を境界づける」から「**応答ヘッダーをどれだけ待つかの上限にもなる**」に平易化されました。

この改稿は 2 ページに波及しています。ネットワーク設定のページでは `CLAUDE_STREAM_FIRST_BYTE_TIMEOUT_MS` の説明から「`API_TIMEOUT_MS` を監視タイムアウトより上に設定した場合はそちらから導出する」という分岐が消え、**未設定時はバイト単位の監視タイムアウトを使うという単一の規則**になり、参照先に「無応答での中断後に再試行がどれだけ待つか」が加わりました。非対話モードのページでは、API 再試行イベント `system/api_retry` に **`no_response` フィールド**が追加されました（この原因で失敗した試行のときだけ現れ、`waited_ms` にその試行が待った時間、`retry_wait_ms` に再試行が待つ時間が入る。**このイベントの `max_retries` はセッション全体の予算ではなく、この原因が通常 1 回だけ得る再試行を反映する**点が明記されています。v2.1.261 以降）。

このほか、既存の **`Path escapes plugin directory`** 節に **symlink の判定**が加わりました。Claude Code は `../shared-utils` のように**綴りの上でプラグイン外を指すパス**だけでなく、**プラグイン外へ導く symlink**（マーケットプレイスの symlink ルールが許すものを除く）も拒否します。symlink の場合はメッセージが解決先も示す（`commands path escapes plugin directory: ./commands/deploy.md — it resolves to /home/user/shared/deploy.md, outside the plugin directory`）、**v2.1.257 より前は綴りしか見ておらず symlink の行き先は見ていなかった**、対処に「プラグイン外へのシンボリックリンクならファイルの実体コピーに置き換える」を追加、という 3 点です。プラグインリファレンスの「パストラバーサルの制限」節にも同じ内容が反映され、拒否の説明と報告されるエラーが 2 段落に分けられました。

冒頭のメッセージ対応表には 3 行が追加されました。`is a network path, which cannot be added as a working directory`、`MCP server <name> is blocked by enterprise managed policy`、`Invalid permission rule "..." was skipped: Malformed Tool(content) rule` で、いずれも「設定の警告」の該当節を指しています。

- [Error reference - Claude Code Docs (English)](https://code.claude.com/docs/en/errors#no-response-from-api)
- [Control MCP server access for your organization - Claude Code Docs (English)](https://code.claude.com/docs/en/managed-mcp#how-a-server-is-evaluated)

## 2. 設定リファレンス

設定リファレンスは実質 66 行（追加 48・削除 18）で 2 番目の差分でした（生の差分も同じ 66 行）。変更は 4 つの塊に分けられ、**3 つはハイライトで扱った内容の設定側の受け皿**です ―― `bashOutputMaxChars` と `taskOutputMaxChars` の新設（ハイライト 5）、`keybindingFlavor` の非推奨化（ハイライト 1）、サンドボックス系 4 か所の書き換え（ハイライト 4）。ここでは残りと、ハイライトで触れきれなかった点を補います。

**`permissions.deny` の説明**に、Read と Edit の deny ルールが適用される範囲として「**`> file` や `< file` のような Bash リダイレクトのターゲット**」が加わりました（詳細はハイライト 2 参照）。「任意のサブプロセスには適用されないので、OS レベルの強制が要るならサンドボックスを有効にせよ」という結びは変わっていません。

**全設定の一覧表**には 3 行の変更が入りました。`bashOutputMaxChars` と `taskOutputMaxChars` の 2 行が「メモリとコンテキスト」分類で追加され、`keybindingFlavor` の行の説明が「`Ctrl+W` を Bash のように空白まで削除させる」から「**非推奨で効果を持たない。単語編集ショートカットは常に readline 規約に従う**」に差し替わっています。

サンドボックス系については、ハイライト 4 で述べた `sandbox.allowUnsandboxedCommands` と `sandbox.excludedCommands` の書き換えに加えて、**strict sandbox mode という表示名の説明が本文から独立した 1 文に分けられた**点が構成上の変更です。従来は「Claude Code がそのパラメータを完全に無視し、すべてのコマンドがサンドボックス化されるか `excludedCommands` に現れる必要がある（これを `/sandbox` の Overrides タブは Strict sandbox mode と表示する）」と 1 文に詰め込まれていたものが、挙動の説明と表示名の説明の 2 文になりました。**`sandbox.excludedCommands` の既定値の説明が「サンドボックス化できるコマンドはすべてサンドボックス化される」から「どのコマンドも除外されない」に変わった**のは、シェルモードのコマンドが対象外になった以上、前者の書き方が事実として成り立たなくなったためと読めます。

- [Claude Code settings reference - Claude Code Docs (English)](https://code.claude.com/docs/en/settings-reference#sandbox-allowunsandboxedcommands)

## 3. TypeScript Agent SDK リファレンス

TypeScript Agent SDK リファレンスは実質 51 行（追加 37・削除 14）で、**「実質 50 行以上」の閾値を 1 行だけ超えました**（生の差分は 55 行で、4 行が桁揃えノイズ）。前回インタラクティブモードを実質 48 行で本カテゴリから外した経緯があるので、同じ基準で今回はこちらを入れています。

**新設されたのは `user_message_uuids` フィールド**で、これも前回の持ち越し 7 件の 1 つです。**このターンで Claude Code が応答した、あなたが送ったすべてのメッセージの `uuid`** が入ります。短い間隔で複数のメッセージを送ると Claude Code はそれらを 1 ターンにまとめることがあり、そのとき既存の `user_message_uuid` は**最後の 1 通の `uuid` しか持ちません**。まとめられたどのメッセージに対する応答かを突き合わせるには、この配列の中を探すことになります。Claude Code はターンの最初の応答と結果の両方で `user_message_uuid` と同時にこの配列を設定し、**配列は必ず `user_message_uuid` を含み、最大 64 件まで**保持します。**ターンの実行中に送ってツール呼び出しの合間に拾われたメッセージは、結果の側の配列にのみ現れます**。最初の応答や結果が `user_message_uuid` だけを持って配列を持たない場合は、それが古いバージョンの Claude Code から来ていることを意味するので単一フィールドにフォールバックせよ、とも書かれています（Agent SDK v0.3.259 以降）。あわせて `SDKAssistantMessage` と `SDKPartialAssistantMessage` の型定義にもフィールドが追加され、既存の `user_message_uuid` の説明は「フレームは 2 種類」から「これらのフレーム」（3 種類）に、フィールドを省く条件の 1 つが「単一の起点メッセージを持たない結果」から「**あなたが送ったどのメッセージにも答えていない結果**」に書き直されました。

**割り込みレシートの意味が明確化されました**。`SDKControlInterruptResponse` の `still_queued` は従来「**割り込みを生き延びる**ユーザーメッセージの UUID 一覧」と説明されていましたが、今回「**割り込みが到着した時点で保留中だったユーザーメッセージの UUID 一覧**」に改められ、さらに **セッションの最初のターンが始まる前に割り込んだ場合は、そのターンは開始直後に中断され、一覧に載ったメッセージは応答を得ない**という条件が加わりました。**前回サマリで扱った v2.1.261 のバグ修正「最初のプロンプト直後・ターン開始前に送られた Stop や割り込みが無視される問題を修正」の、SDK 側から見た記述**にあたります。「レシートを使って再送の要否を判断せよ」の段落も分けられ、「**一覧に載っていてキャンセルしなかったメッセージは、応答を得るかどうかに関わらず会話に入る**ので、再送すると Claude に 2 回届く」と因果を明示する書き方になりました。CLI が広告する能力の表でも `interrupt_receipt_v1` と `interrupt_cancel_queued_v1` の 2 行が同じ用語に揃えられています。

**`ambient` フラグの定義が広がりました**。従来は「Claude Code が自分の運用のために起動し、あなたの作業として表示しないタスク（自動起動されるライブ更新の watcher など）で `true`」でしたが、「**セッションの作業の一部ではないタスク**で `true`。たとえば Claude Code が自分の運用のために走らせるタスク。**ライブ更新の watcher も ambient で、これには利用者が頼んだ watcher も含まれる**」に変わりました。「利用者が明示的に頼んだものまで ambient になる」という点が新しく、活動インジケータから除外せよという指示は変わりません。`SDKTaskNotificationMessage` 側の記述は定義の重複を避けて `SDKTaskStartedMessage` への参照 1 文に整理されました。`SDKBackgroundTasksChangedMessage` の発火条件にも **タスクの `description` の変化**が加わり（従来は `ambient` フラグの変化のみ）、段落が 2 つに分けられています。

**`permissionPrompts` オプションが `Options` の表に載りました**（`'host' | 'none'`・既定 `'host'`・Claude Code v2.1.259 以降）。**誰が権限プロンプトに答えるかを決める**もので、`'host'` は `canUseTool` コールバックまたは `permissionPromptToolName` のツールへ回し、`'none'` は**プロンプトを出すはずだった呼び出しを拒否**します。`SDKPermissionDeniedMessage` の説明にも 4 つ目の場合分けとして「**`permissionPrompts: 'none'` のとき**：`canUseTool` や MCP プロンプトツールを設定していても、プロンプトを出すはずだった呼び出しを拒否し、このイベントはその拒否も報告する」が加わり、既存の 2 項目にも「既定の `permissionPrompts: 'host'` のとき」という前提が明記されました。Agent SDK の権限のページでは評価順の最終段に、SDK の権限のページでは `canUseTool` の説明に、それぞれ「**`permissionPrompts: 'none'` を設定するとこの段でコールバックは呼ばれない。`PermissionRequest` フックにはまだ判断の機会があり、それも判断しなければ Claude Code は拒否する**」という趣旨の記述が加わりました。

- [Agent SDK reference - TypeScript - Claude Code Docs (English)](https://code.claude.com/docs/en/agent-sdk/typescript#user_message_uuids)
- [Configure permissions - Claude Code Docs (English)](https://code.claude.com/docs/en/agent-sdk/permissions#how-permissions-are-evaluated)

## 軽微な更新

<!-- light:minor-updates:start -->
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
<!-- light:minor-updates:end -->

## 新着情報

<!-- light:whats-new:start -->
（今回の対象期間には `whats-new/` 配下のページに差分がありませんでした。差分のあった 32 ページはいずれもリファレンス・ガイド系です。最新の週間ダイジェストは 5 回前のサマリで扱った Week 34（2026年08月17日～21日）のままで、新しい週のダイジェストの追加も既存ページの訂正もありません。`whats-new/` の無差分は 5 回連続です）
<!-- light:whats-new:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-09-04.md](./archives/latest/2026-09-04.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-09-04.md](./archives/latest-detail/2026-09-04.md)

<!--
base_commit: 3f57b81e5934ecd89be2d817677dfcfdba5da98f
head_commit: 79f96cfde0b383e61550570a0d780c890e54cf66
generated_at_full: 2026-09-06T15:00:28+09:00
-->
