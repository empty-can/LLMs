---
対象期間: 2026年10月14日 〜 2026年10月15日
作成日: 2026-10-15
---

# Claude Code 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
**今回は、1 ページだった Code Review の文書が概要と 6 つの新しいページに分かれ、レビューのレベル（Quick・Standard・Deep）、GitHub の組織全体を対象にする設定、サブディレクトリの `REVIEW.md` と読むブランチの規則などが新たに載りました。mod が VS Code 拡張機能のチャットパネルにも描けるようになり（拡張機能 v2.1.299 以降）、VS Code では応答の LaTeX の数式が組版されるようになりました（v2.1.301 以降）。`errors` には 9 つの節が加わり、changelog には v2.1.301（2026年10月15日、51 項目）が積まれています**。新しいページは 6 つで、ページ単位で数えると 228 ページ中 39 ページ（新しい 6 ページと changelog を含む）が変わり、changelog を除く変更は 1,652 行（追加 1,227・削除 425）、4 ページが大幅更新です。総行数は 122,303 行から 120,654 行に減りました（2 回展開されていた 5 ページが 1 回になったため）。

主要なものを以下に挙げます。

1. Code Review の文書が概要と 6 つの新しいページ（`/code-review`・有効化・カスタマイズ・プルリクエスト・費用・トラブルシューティング）に分かれ、`llms.txt` に「Code review and pull requests」の分類ができた
2. Code Review に、レビューのレベル、GitHub の組織全体を対象にする設定、ヒントのコメント、サブディレクトリの `REVIEW.md` と読むブランチの規則、返信を読む後のレビューなどが載り、1 回 $15〜25 の目安などの記述が外れた
3. mod が VS Code 拡張機能のチャットパネルにも描けるようになり（拡張機能 v2.1.299 以降・機能フラグを取得するセッション）、描画の場所と要素の表に VS Code が加わった
4. `errors` に 9 つの節（読み込まれなかった指示ファイル、出力トークンの上限で切れた応答、管理された設定で無視されるサンドボックスの許可など）が、`model-config` に認識されないモデル ID の警告とウィンドウの正し方が載った
5. VS Code のチャットパネルが応答の LaTeX の数式を組版するようになり（v2.1.301 以降）、開くのに 2 回続けて失敗した会話を再読み込みで開き直さない動作が載った
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**Code Review の文書が 7 ページに分かれた**](#1-code-review-の文書が-7-ページに分かれた):  
  386 行の 1 ページだった `code-review` が 123 行の概要になり、`/code-review` コマンド・有効化・カスタマイズ・プルリクエストでの読み方と依頼の仕方・費用・トラブルシューティングの 6 ページ（計 759 行）が新しくできました。`llms.txt` では「Code review & CI/CD」が「Code review and pull requests」の分類に替わり、その下に「Code Review」「Security scans」「Run Claude in your own CI」ができています
2. [**Code Review にレビューのレベルと REVIEW.md を読むブランチの規則などが載った**](#2-code-review-にレビューのレベルと-reviewmd-を読むブランチの規則などが載った):  
  レビューのレベル（Quick・Standard・Deep）、新しい有効化の手順、GitHub の組織全体を対象にする設定、ヒントのコメント、サブディレクトリの `REVIEW.md` と、どのブランチの `REVIEW.md` を読むか（ブランチ保護による違い）、返信を読んで範囲を絞る後のレビューなどが文書になりました。research preview の注記、👍/👎 での評価、1 回平均 $15〜25・平均 20 分の目安の記述は外れています
3. [**mod が VS Code 拡張機能のチャットパネルにも描けるようになった**](#3-mod-が-vs-code-拡張機能のチャットパネルにも描けるようになった):  
  `plugins/mods/interface` に「Draw in the VS Code extension」の節ができ、拡張機能 v2.1.299 以降・機能フラグを取得するセッションで、mod の描いたものがチャットパネルに出るようになりました（`e.surface` は `vscode`）。`plugins/mods/reference` の描画の場所と要素の表に VS Code が加わり、`vs-code` にはパネルに描くプラグインのラベルの説明が載りました
4. [**errors に 9 つの節が加わり認識されないモデル ID の扱いが載った**](#4-errors-に-9-つの節が加わり認識されないモデル-id-の扱いが載った):  
  `errors` に、読み込まれなかった指示ファイル、出力トークンの上限で切れた応答、管理された設定のロックで無視されるサンドボックスの許可、読み込まれない管理された設定のフック、予約された MCP サーバーの名前などの 9 節が加わりました。`model-config` には、モデル ID を認識できず 200K のウィンドウと仮定したときの起動時の警告と、正し方の 4 つの方法が載りました
5. [**VS Code のチャットパネルが LaTeX の数式を組版するようになった**](#5-vs-code-のチャットパネルが-latex-の数式を組版するようになった):  
  `vs-code` に「LaTeX math in responses」の節ができ、v2.1.301 以降のチャットパネルは応答の `$$ … $$`・`\[ … \]`・`$…$`・`\(…\)` の数式を組版します。組版されないときの調べ方の節と、開くのが 2 回続けて終わらなかった会話を再読み込みで開き直さない動作（「A conversation was not reopened」）も加わりました
<!-- light:highlight-list:end -->

## 1. Code Review の文書が 7 ページに分かれた

**これまで 1 ページにまとめられていた `code-review`（386 行）の内容が、概要のページと 6 つの新しいページに分かれました。** `code-review` は 123 行の概要になり（追加 78・削除 344）、旧ページの節は次の新しいページへ移っています。各ページの中身は「新規追加されたページ」にまとめました。

| 旧 `code-review` の節 | 移った先 |
|---|---|
| Review a diff locally（`/code-review` コマンド） | `code-review-local`（Review locally with /code-review） |
| Set up Code Review | `code-review-setup`（Set up Code Review） |
| Customize reviews（`CLAUDE.md`・`REVIEW.md`） | `code-review-customize`（Customize Code Review） |
| Severity levels・Rate and reply to findings・Check run output・Manually trigger reviews・Review pull requests from forks | `code-review-pull-requests`（Read and request reviews on a pull request） |
| View usage・Pricing | `code-review-costs`（Code Review costs and usage） |
| Troubleshooting | `code-review-troubleshooting`（Troubleshoot Code Review） |

**`llms.txt` では、「Platforms and integrations」の下の「Code review & CI/CD」が「Code review and pull requests」の分類に替わりました。** 直下に `code-review-local`、`ultrareview`（「Claude Code in the cloud」から移動）、`github-enterprise-server`（同じ分類の中で移動）が並び、その下に次の 3 つの小分類ができています。

- **Code Review**: `code-review` と新しい 5 ページ（`code-review-setup`・`code-review-customize`・`code-review-pull-requests`・`code-review-costs`・`code-review-troubleshooting`）
- **Security scans**: `security-guidance`・`claude-security`
- **Run Claude in your own CI**: `github-actions`・`github-actions-cloud-providers`・`gitlab-ci-cd`

`code-review` の説明文も「Set up automated PR reviews that catch logic errors, security vulnerabilities, and regressions using multi-agent analysis of your full codebase」から「Catch bugs in GitHub pull requests with Code Review: Claude reviews each change, verifies its findings, and comments inline. For Team and Enterprise plans」に変わり、各分類の代表のページを並べる後半の一覧にも「Code review and pull requests」（`code-review`）が加わりました。ほかのページの `code-review#review-a-diff-locally` などへのリンクも、`commands`・`skills`・`desktop`・`checkpointing`・`github-enterprise-server` などで新しいページへ張り替えられています。

- [Code Review - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/code-review#set-up-and-use-code-review)
- [Code Review - Claude Code Docs (English)](https://code.claude.com/docs/en/code-review#set-up-and-use-code-review)
- [Code Review - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/code-review#compare-ways-to-get-a-review)
- [Code Review - Claude Code Docs (English)](https://code.claude.com/docs/en/code-review#compare-ways-to-get-a-review)

## 2. Code Review にレビューのレベルと REVIEW.md を読むブランチの規則などが載った

**分かれたページには、旧ページになかった内容が多く加わっています。** 主なものは次のとおりです。

- **レビューのレベル**（`code-review` の「Review levels」・`code-review-setup` の「Set the default review level」）: **Quick**（軽い確認。最も速く最も安い）・**Standard**（深さ・速さ・費用の釣り合いをとる既定）・**Deep**（最も丁寧。時間も費用も最もかかる）の 3 つです。Owner が **Review level** で組織の既定を選んで **Change level** で確定し、リポジトリの行の **Edit** から個別に変えられます（最初の選択肢 **Default** は組織に従う）。新しいレベルは変更の後に始まるレビューから効きます。レビューのモデルは Code Review が選び、管理設定にモデルの選択はありません
- **利用の条件**（`code-review` の「Availability」）: Team と Enterprise のプランで、GitHub のリポジトリ（GitHub Enterprise Server と、データレジデンシーのある GitHub Enterprise Cloud を含む。後者は Owner が GHES の管理者の手順で `ghe.com` のホスト名を入れる）が対象です。ZDR と HIPAA の構成では使えず BAA の対象外で、**CMEK を使う組織ではまだ使えません**。開発者が Amazon Bedrock などで Claude Code を使っていても、これらのプランの Claude の組織が要ります
- **有効化と組織全体**（`code-review-setup`）: 管理設定の **Allow code review** のスイッチから始める手順になり、追加したリポジトリは **After every push** から始まります。GitHub の組織の行で **Review runs** を設定すると、Claude GitHub App がアクセスできるその組織のすべてのリポジトリ（後から加わるものも）が対象になります。接続した GitHub アカウントがその組織のオーナーであること、github.com の組織であること（GHES と個人のアカウントは対象外）、月の支出上限を設定してあることが条件です。レビューが始まらない理由と次にすることを伝える**ヒントのコメント**（**Show tips on pull requests**、既定でオン）も載りました
- **`REVIEW.md` の置き場所と読むブランチ**（`code-review-customize`）: ルートに加えて**サブディレクトリにも `REVIEW.md` を置け**、その配下の変更へのチェックを足せます。`REVIEW.md` は PR の base のブランチか既定のブランチから読み、PR 自身の変更からは読みません。重大度を下げる・パスや問題の種類を除く・nit の数を抑える指示に従うのは、**保護された既定のブランチ**のルートのファイルを読んだときです。保護の有無で、読む写し（既定のブランチ・base のブランチ・なし）と読むファイル（ルートとサブディレクトリ・ルートだけ・なし）が変わる 4 行の表も載りました
- **`CLAUDE.md` の違反の重大度**: これまでの「新しく入った違反は nit として扱う」から、「その問題に合う重大度の指摘になる」に改められました。読むのはルートの `CLAUDE.md` と、変更したファイルの親ディレクトリの `CLAUDE.md` です
- **プルリクエストでの動き**（`code-review-pull-requests`）: 指摘への返信は、次のレビューが読み、スレッドを解決するか 1 回だけ返信を投稿しうる、と載りました（これまでは「返信しても Claude は応じない」だけ）。push の後などに自動で始まる後のレビューは前回からの変更に絞り、nit と既存の問題を減らします（要約に "found and not posted" などの行）。`@claude review` は PR 全体を見直します。最新のコミットでレビューが動いていれば、新しい依頼で 2 つ目は始まりません（これまでは、終わるまでキューに入るとしていた）
- **外れた記述**: research preview の注記、各指摘に付く 👍/👎 で評価する説明（「Rate and reply to findings」）、1 回のレビューが平均 $15〜25、平均 20 分で終わるという目安は、新しいどのページにもありません

- [Code Review - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/code-review#review-levels)
- [Code Review - Claude Code Docs (English)](https://code.claude.com/docs/en/code-review#review-levels)
- [Code Review をカスタマイズする - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/code-review-customize#which-branch-review-md-is-read-from)
- [Customize Code Review - Claude Code Docs (English)](https://code.claude.com/docs/en/code-review-customize#which-branch-review-md-is-read-from)

## 3. mod が VS Code 拡張機能のチャットパネルにも描けるようになった

**`plugins/mods/interface` に「Draw in the VS Code extension」の節ができました。** 拡張機能 v2.1.299 以降で、機能フラグを取得するセッションでは、mod が描いたものがチャットパネルに出ます。パネル向けの `ui.render` フックでは `e.surface` が `vscode` です。ターミナルとパネルの両方で動かすときの違いとして、次が挙がっています。

- **ペイン**: 800 ピクセル以上の幅のパネルでは会話の横にドックし（`e.props.placement` は `'dock'`、`e.viewport.isFullscreen` は `true`）、狭いパネルではプロンプトボックスの上に描かれます（`'inline'`。12 行を超えるとスクロール）。`$.ui.open` の `rows` と `columns` は無視され、パネルが大きさを決めます
- **トーストとステータス行**: プロンプトボックスの真上の 1 つの積み重ねに入り（狭いパネルではペインも一緒）、ステータス行は mod ごとに 1 行です。権限の要求やダイアログが出ている間は隠れます
- **ラベル**: パネルは mod が描いたものや書き換えたものを囲み、**From the token-chart plugin**・**Edited by the token-chart plugin** のようにプラグインの名前で示します
- **キーボード**: ボタンにホットキーはなく、クリックするか、フォーカスがあるときに Enter を押します。ペインの `focus: true` は、パネルにフォーカスがあり、Claude がアイドルで質問待ちがなく、プロンプトボックスが空のときだけ認められます
- **そのほか**: `AskUserQuestion` ではパネル自身の質問のカードを残してその上に要素を描き（`next` に渡す props はカードを変えない）、`$.prompt.suggest` は `isShown: false` で何も出しません。ステータス行は 200 文字か 2 行、トーストは 500 文字で切られます

`plugins/mods/reference` では、描画の場所の表で `Pane`・`UserMessage`・`AssistantMessage`・ツールの呼び出しの場所・`AskUserQuestion`・`Spinner` に VS Code が加わり、要素の表に VS Code の列ができました（詳細は大幅更新 3）。`vs-code` には「Plugins that draw in the panel」の節ができ、利用者の側から見えるもの（会話の横かプロンプトボックスの上のペイン、トーストやステータス行、プラグイン独自に描いたメッセージやツールの呼び出し）と、**From the token-chart plugin**・**Edited by the token-chart plugin**・**Prompt from the token-chart plugin** のラベルの意味、描かせないにはプラグインのダイアログでそのプラグインをオフにすることが載りました。

ほかのページも追従しています。`plugins/mods/overview` は対応先に VS Code 拡張機能を加え、「Where mods run」の表の VS Code のチャットパネルの描画を「No」から「Yes」（拡張機能 v2.1.299 以降・機能フラグを取得するセッション）に改めました。`plugins/mods/troubleshoot` には、VS Code ではホットキーがないこと、パネルで描かれない原因として拡張機能が 2.1.299 より古いことと、機能フラグを取得しないセッション（Amazon Bedrock・Google Cloud's Agent Platform・Microsoft Foundry・Claude apps gateway など。そのときは VS Code の統合ターミナルなどで `claude` を動かす）が加わりました。`plugins/mods/gallery`（VS Code では `Code` が色も行番号もない素の文字になり、`Svg` は描かれる）、`plugins/mods/api`（ステータス行とトーストはプロンプトボックスの上に、ログの行は会話に出る）、`env-vars`（機能フラグの取得をオフにすると VS Code のパネルで mod の描画が見えない。フックは動く）も改められています。changelog の v2.1.301 にも、VS Code・デスクトップ・モバイルのアプリでは質問のダイアログの上に描く木が Markdown と最大 48 行を持てる（ターミナルは 12 の素の行のまま）という改善が載りました。

- [mod でインターフェイスに描画する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/plugins/mods/interface#draw-in-the-vs-code-extension)
- [Draw in the interface with a mod - Claude Code Docs (English)](https://code.claude.com/docs/en/plugins/mods/interface#draw-in-the-vs-code-extension)
- [VS Code で Claude Code を使用する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/vs-code#plugins-that-draw-in-the-panel)
- [Use Claude Code in VS Code - Claude Code Docs (English)](https://code.claude.com/docs/en/vs-code#plugins-that-draw-in-the-panel)

## 4. errors に 9 つの節が加わり認識されないモデル ID の扱いが載った

**`errors` に次の 9 つの節が加わりました。** メッセージから節を引く表にも、これらを含む 12 行が加わっています。

- **Instruction file not loaded**: 対話のセッションの会話の表示に出る通知で、存在するメモリファイルが読み取りの制限で読み込まれなかったことを示します。理由は括弧の中に、`a Read deny rule covers it`（`Read` の deny ルールがパスかリンクの先に一致）、`it's read from outside your working directories, where reads are blocked`（`permissions.blockReadsOutsideWorkingDirectories` がオン）、`where it leads couldn't be worked out`（自分に戻るリンクなど）のように出ます。サブディレクトリのメモリファイルならターンの途中で出て、名前を挙げきれない分は `and 3 more instruction files not loaded` のように数えます。v2.1.292 より前は、同じ行の理由の後にファイル名が出ていました（`memory` のトラブルシューティングにもこの節への案内が加わった）
- **Response exceeded the output token maximum**: 応答が要求の出力トークンの上限に達して切れたことを示します。`a request sent without streaming` を含む形は、ストリーミングの要求が失敗して Claude Code がストリーミングなしで送り直したもので、応答は 64,000 トークンまでに限られ、`CLAUDE_CODE_MAX_OUTPUT_TOKENS` でも上げられません。v2.1.299 より前は、送り直した要求で切れた応答がこのメッセージなしに完了したかのようにターンを終えていました。対処は `continue` と返して続きを頼む、変数を設定する、出力を小分けに頼む、です
- **Sandbox allow entries are ignored under a managed lock**: 管理された設定が `allowManagedReadPathsOnly` か `allowManagedDomainsOnly` を設定しているため、名指しされたファイルの `allowRead`・`allowedDomains` が効かないという、`/status` と `claude doctor` の警告です。対処は不要で、要るなら管理者に管理された設定へ足してもらい、警告を消すにはファイルからその項目を外します（共有のファイルなら残してもよい）
- **Managed settings contain invalid entries, including PreToolUse/PermissionRequest hooks that are NOT loaded**: `-p` の実行の stderr に出るまとまりで、管理された設定のフックの項目を読み込めないことを示します（`hooks` のフィールドが無視と出れば、そのソースのフックはすべて動かない）。ソースが `parent managed settings` なら、Claude Code を起動したアプリの開発者に報告します。v2.1.300 より前は `Managed settings failed to load; policies from the failed source are NOT in effect:` の見出しの下に出ていました
- **MCP server name is reserved**: `"workspace" is a reserved MCP server name and was not loaded` のように、組み込みのサーバーなどの予約された名前の MCP サーバーは読み込まれません。定義した場所で `my-workspace` のように名前を変えます
- **No shell command in a skill or command was run**: スキルかカスタムコマンドのファイルの `` !`<command>` `` の動的コンテキストのコマンドに、タブと改行以外の生の制御文字があると、ファイルのどのコマンドも動かずに呼び出しが断られます。メッセージは Bash か PowerShell のツールを示し、断ったコマンドの該当の文字を `�` で示します（`skills` にも「Control characters in injected commands」の節ができた）
- **`--sandbox` or `--no-sandbox` is not supported by claude remote-control**: 効果のなかった両フラグは v2.1.300 で `claude remote-control` から外れ、渡すとサーバーは終了コード 1 で終わります。サンドボックスで動かすには設定の `sandbox.enabled` を `true` にします（`remote-control` のフラグの表にも「v2.1.300 で削除」の行が加わった）
- **Couldn't tell whether `--bg` is a flag or text**: `--bg` か `--background` が、フラグか文字かを判別できない位置にあると、何も始めずに終了コード 1 で終わります。`claude --bg --name nightly-audit "<task>"` のようにフラグを先に置きます
- **Remote Control could not renew this computer's connection**: `claude remote-control` のサーバーが claude.ai のログインで接続の資格情報を期限前に更新できないときの警告で、最後の文が残りの時間（例: 約 26 時間）か期限切れを示します。別の端末で `claude /login` し、期限が切れてもサインインできなければ `Poll: Authentication failed (401)` を含むエラーで止まります

**`model-config` の「Correct the window for a gateway or custom model ID」には、起動時の 2 つの警告とその対処が載りました。** `⚠ Model "my-gateway-opus" isn't recognized · context assumed to be 200k tokens · ...` と `Claude Code doesn't recognize the model "my-gateway-opus", so it assumes a context window of 200k tokens. ...` は、セッションのモデル ID を認識できず 200K トークンと仮定したことを示します。Claude Code はその 200K で自動圧縮するので、本当のウィンドウが 200K なら直すことはありません。そうでなければ次のどれかで本当のウィンドウを伝えます。

- **Claude Code より新しいモデル**: シェルで `claude update` を動かす
- **Claude Code が知っているモデルの、ゲートウェイやプロバイダーでの名前**: `modelOverrides` で `"claude-opus-4-8": "my-gateway-opus"` のように対応づけるか、`modelPicker` の行に `behavesAs` を付けて挙げる
- **1M のウィンドウのモデル**: `claude --model 'my-gateway-opus[1m]'` のように ID に `[1m]` を付ける
- **そのほかのウィンドウ**: `CLAUDE_CODE_MAX_CONTEXT_TOKENS=400000` のように変数を設定する（`claude-` で始まらず `[1m]` もない認識されない ID ならそれだけで効き、ほかの ID は新しくできた小見出し「Which IDs `CLAUDE_CODE_MAX_CONTEXT_TOKENS` applies to」で確かめる）

ID を認識するか伝えたウィンドウを使えば、その ID でセッションを始めても警告は出なくなります。`errors` にも 2 つの警告の行と、受け付けるトークンがもっと多いモデルで 200K 付近でコンテキストの超過のエラーが出るなら、認識されないモデル ID が原因のことがある、という案内が加わりました。

- [エラーリファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/errors#instruction-file-not-loaded)
- [Error reference - Claude Code Docs (English)](https://code.claude.com/docs/en/errors#instruction-file-not-loaded)
- [モデル設定 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/model-config#correct-the-window-for-a-gateway-or-custom-model-id)
- [Model configuration - Claude Code Docs (English)](https://code.claude.com/docs/en/model-config#correct-the-window-for-a-gateway-or-custom-model-id)

## 5. VS Code のチャットパネルが LaTeX の数式を組版するようになった

**`vs-code` に「LaTeX math in responses」の節ができました。** Claude Code v2.1.301 以降のチャットパネルは、Claude の応答の LaTeX を組版した数式として表示します（ターミナルモードでは組版しない）。

- **ディスプレイ数式**: 独立した行の `$$ … $$` か `\[ … \]` のブロックと、言語を `math` にしたフェンスのコードブロック
- **インライン数式**: `$E = mc^2$` や `\(a^2 + b^2 = c^2\)` のように、同じ行で開いて閉じる `$…$` か `\(…\)`
- **組版しないもの**: パネルは同じ文字のほかの使い方と区別しようとし、`$HOME`、`$5` のような値段、`sed 's/\(foo\)/\1/'` は組版しません。コードスパンの中と、`math` 以外のコードブロックの中も組版しません
- **コピー**: 組版した数式を含む文字を選んでコピーすると、描いた記号ではなく `$…$` か `$$…$$` で囲んだ TeX のソースになります。**Copy response** と `/copy` は、Claude が書いたまま（TeX のソースを含む）を返します

トラブルシューティングの「A formula shows as raw LaTeX」では、どの数式も組版されないなら拡張機能の版（2.1.301 以降が要る）を確かめ、ターミナルモードなら Use Terminal の設定を外す、としています。一部だけそのまま出るなら、語に見える `$…$`（`$O(n log n)$`）や数字で始まり `=`・`+`・`^` のような印のない `$30$`・`$1/N$`、内側に空白のある `$ x^2 $`、60 文字を超えるか 2 行に分かれた `$…$`・`\(…\)`、構文の誤り・`\newcommand` や `\def` のようなマクロの定義・エスケープしない `%`、8,192 文字を超える式、1 つのブロックの上限を超えた後の式、が原因として挙がっています（多くは独立した行の `$$` のブロックを頼むよう勧める）。

**再読み込みでの会話の開き直しにも安全策が載りました。** 「A conversation was not reopened」によると、再読み込みの後、最後の 2 回の開くのが終わらなかった会話はパネルが開き直さず、新しいチャットのプロンプトボックスの上に `“Fix the login bug” was not reopened. It did not finish opening the last 2 times, ...` のような通知を出します。開くのが終わらないのは、会話の読み込み中にパネルがクラッシュするか応答しなくなったときと、開いて約 3 秒以内に再読み込みするかウィンドウを閉じたときです。会話は変わらず Session history に残り、**Open it anyway** か Session history から開けます（プロンプトを送ると通知は消える）。トラブルシューティングにも、再読み込みで会話が戻るたびにパネルがクラッシュする・固まる・`Something went wrong` だけを出すなら v2.1.301 以降に更新する、という節が加わりました。changelog の v2.1.301 にも、LaTeX の数式の描画の追加と、パネルをクラッシュさせるか固まらせる会話が再読み込みのたびに開き直される問題の修正が載っています。

- [VS Code で Claude Code を使用する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/vs-code#latex-math-in-responses)
- [Use Claude Code in VS Code - Claude Code Docs (English)](https://code.claude.com/docs/en/vs-code#latex-math-in-responses)
- [VS Code で Claude Code を使用する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/vs-code#a-conversation-was-not-reopened)
- [Use Claude Code in VS Code - Claude Code Docs (English)](https://code.claude.com/docs/en/vs-code#a-conversation-was-not-reopened)

## 新規追加されたページ

<!-- light:new-pages:start -->
- [**Review locally with /code-review**](#1-review-locally-with-code-review) ([日本語](https://code.claude.com/docs/ja/code-review-local#choose-what-to-review) / [English](https://code.claude.com/docs/en/code-review-local#choose-what-to-review)):  
  旧 `code-review` の「Review a diff locally」を独立させた、`/code-review` コマンドのページです。レビューの対象の指定の表や、レビューを置き換える方法が加わりました（170 行。詳細はハイライト 1）
- [**Set up Code Review**](#2-set-up-code-review) ([日本語](https://code.claude.com/docs/ja/code-review-setup#turn-on-code-review) / [English](https://code.claude.com/docs/en/code-review-setup#turn-on-code-review)):  
  Owner が Code Review を有効にし、組織の既定とリポジトリを管理するページです。新しい有効化の手順、レビューのレベル、GitHub の組織全体を対象にする設定が載っています（160 行。詳細はハイライト 2）
- [**Customize Code Review**](#3-customize-code-review) ([日本語](https://code.claude.com/docs/ja/code-review-customize#which-branch-review-md-is-read-from) / [English](https://code.claude.com/docs/en/code-review-customize#which-branch-review-md-is-read-from)):  
  `CLAUDE.md` と `REVIEW.md` でレビューの指摘を調整するページです。サブディレクトリの `REVIEW.md` と、どのブランチの `REVIEW.md` を読むかの規則が加わりました（128 行。詳細はハイライト 2）
- [**Read and request reviews on a pull request**](#4-read-and-request-reviews-on-a-pull-request) ([日本語](https://code.claude.com/docs/ja/code-review-pull-requests#respond-to-findings) / [English](https://code.claude.com/docs/en/code-review-pull-requests#respond-to-findings)):  
  開発者がプルリクエストで指摘を読み、応じ、レビューを依頼するためのページです。後のレビューの範囲やスクリプトでの結果の読み方が詳しくなりました（144 行。詳細はハイライト 2）
- [**Code Review costs and usage**](#5-code-review-costs-and-usage) ([日本語](https://code.claude.com/docs/ja/code-review-costs#estimate-your-spend) / [English](https://code.claude.com/docs/en/code-review-costs#estimate-your-spend)):  
  Code Review の課金、費用を左右するもの、見積もり、支出の上限、使用量の確かめ方をまとめたページです（71 行）
- [**Troubleshoot Code Review**](#6-troubleshoot-code-review) ([日本語](https://code.claude.com/docs/ja/code-review-troubleshooting#check-how-far-the-review-got) / [English](https://code.claude.com/docs/en/code-review-troubleshooting#check-how-far-the-review-got)):  
  check run のタイトルからレビューの進み具合を見分け、始まらない・失敗した・予算で飛ばされたレビューや、設定の問題に対処するページです（86 行）
<!-- light:new-pages:end -->

6 ページとも `llms.txt` の新しい「Code review and pull requests」の分類に載り、`llms-full.txt` に本文が入りました（行数は `git diff --no-index --numstat` で数えた本文の行数）。日本語版も 6 ページとも公開されており、確かめた節はすべて英語版と同じ内容でした。

## 1. Review locally with /code-review

旧 `code-review` の「Review a diff locally」を独立させた、Claude Code のセッションで `/code-review` を動かすページです。どのプランでも使え、レビューは自分のセッションで動くので、ほかの作業と同じくプランの使用量か API の課金に数える、と冒頭で示しています。節は「Choose what to review」「What the review reads and edits」「How findings are reported」「Tune effort and arguments」（「Post findings to a GitLab merge request」「Text after the effort level and flags」）「Run in the foreground」「Let Claude start the review」「Escalate to ultrareview」「Change or build on the review」です。

旧ページの内容に加わったのは次の点です。「Choose what to review」に、今のブランチ（`/code-review`）・直近の 15 のコミット（`/code-review HEAD~15..HEAD`）・ブランチどうし（`/code-review main...my-feature`）・1 つのコミット（`/code-review abc1234^..abc1234`）・プルリクエストの番号（`/code-review 1234`）・パス（`/code-review src/auth`）の対象の指定の表ができ、ブランチに upstream がなければ `main` か一つ前のコミットと比べる、とされました。`--fix` なしではレビューの指示は報告だけを求め、`--fix` の編集もそうでない編集も権限モードを通る（承認を求められうる）こと、`-p` の実行でも `CLAUDE.md` に従うこと、バックグラウンドのレビューの `--fix` の後の `/rewind` は会話で Claude がすでに編集していたファイルだけを戻すこと、`--max-findings` の上限は findings のツールで報告するときは 32 で、`-p` で渡した値は記憶されないこと、CMEK を使う組織では ultrareview を動かせないことも載っています。

新しい「Change or build on the review」では、`/code-review` は組み込みのスキルでディスクに `SKILL.md` はなく、すべてのレビューに守らせる規則は `CLAUDE.md` に書く、としています。`code-review` という名前のプロジェクトか個人のスキルを作ると組み込みのものの代わりに動き（`/review` の別名は組み込みのレビューのまま）、自分のレビュー用のサブエージェントかスキルを書くこともでき、近いコマンドとして片付けだけの `/simplify` と、アプリを動かして確かめる `/verify` が挙がっています。

- [/code-review でローカルにレビューする - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/code-review-local#choose-what-to-review)
- [Review locally with /code-review - Claude Code Docs (English)](https://code.claude.com/docs/en/code-review-local#choose-what-to-review)
- [/code-review でローカルにレビューする - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/code-review-local#change-or-build-on-the-review)
- [Review locally with /code-review - Claude Code Docs (English)](https://code.claude.com/docs/en/code-review-local#change-or-build-on-the-review)

## 2. Set up Code Review

Claude の組織の Owner が claude.ai の **Admin settings > Claude Code** で Code Review を有効にするページです。レビューは Anthropic のインフラで動くので、リポジトリにワークフローのファイルは足さない、と冒頭にあります。「What you need to turn on Code Review」では、Claude の組織の Owner のロール（管理のページのすべての手順）、GitHub の組織のオーナー（Claude GitHub App のインストールと Claude の組織へのリンク）、接続する GitHub アカウントから追加する各リポジトリへの書き込み権限、の 3 つを表にしています（旧ページは「Owner か Primary Owner のロール」としていた）。

「Turn on Code Review」の手順は、**Allow code review** のスイッチを押す → **Connect GitHub** のダイアログで **Connect**（GHES ならインスタンスを先に選ぶ）→ **Add a repository** に目的のリポジトリが出なければ **Install GitHub App** から Claude GitHub App を入れる（終わって **Finish connecting GitHub** が出れば押す）→ リポジトリを選んで **Continue** → **Code review is set up** のダイアログで **Finish**（ほかの方法で閉じるとリポジトリは追加されたまま **Allow code review** はオフ）→ draft でないテストのプルリクエストで **Claude Code Review** の check run を確かめる、の 6 段です。旧ページの **Review Behavior** は **Review runs** の名前になり、**Once after PR creation**（開いた・開き直した・ready for review にしたとき）・**After every push**・**Manual (@claude review)** から選びます。

「Set defaults for your organization」にはレビューのレベル（ハイライト 2）、**Review runs**、ヒントのコメント（リポジトリが Manual・fork からのプルリクエスト・ボットか書き込み権限のない人の `@claude review`・GitHub の組織が Claude の組織にリンクされていない、の 4 つの場合に投稿）、開発者が Owner のロールなしにできること（`@claude review`・`@claude review always`・`REVIEW.md` と `CLAUDE.md` のコミット）が並びます。「Manage repositories」では、リポジトリの追加、GitHub の組織全体を対象にする設定（**Off** を含む 4 つの選択肢。個別に設定したリポジトリも上書きし、後で違う設定にしたリポジトリは **Custom** と出る）、リポジトリのオフ・削除（削除すると別の Claude の組織がそのリポジトリを設定できる。組織全体の対象の間は削除できない）、組織の行の **Off**、**Allow code review** のオフ（リポジトリの一覧は残る）の使い分けを示しています。

- [Code Review をセットアップする - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/code-review-setup#turn-on-code-review)
- [Set up Code Review - Claude Code Docs (English)](https://code.claude.com/docs/en/code-review-setup#turn-on-code-review)
- [Code Review をセットアップする - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/code-review-setup#cover-a-whole-github-organization)
- [Set up Code Review - Claude Code Docs (English)](https://code.claude.com/docs/en/code-review-setup#cover-a-whole-github-organization)

## 3. Customize Code Review

リポジトリにコミットした指示で、Code Review が何を指摘するかを変えるページです。`CLAUDE.md`（レビューを含むすべての作業のためのプロジェクトの指示）と `REVIEW.md`（レビューだけの指示）の 2 つを使い分け、`REVIEW.md` をルートに置いてマージしたら既定のブランチを保護する、という流れで書かれています。Code Review のサービスは両方を読み、ローカルの `/code-review` コマンドは `CLAUDE.md` だけを読む、という注記もあります。

「Use REVIEW.md for review-only rules」には、ルートの `REVIEW.md` と `services/billing/REVIEW.md` のようなサブディレクトリのファイルの配置の例が載り、問題を見つけるエージェントと確かめるエージェントがその内容を受け取り、最終的なレビューを書く段階が重大度と要約を決める前に参照する、とされています。「Choose what to write in REVIEW.md」は、旧ページの「What you can tune」を「見えている問題 → 足す指示」の形に組み替え、Important の付け方・多すぎる nit・生成ファイルや CI がすでに確かめていることへの指摘・確かめられていないチームの規則・誤りだと分かる指摘の 5 つを挙げます。旧ページにあった「Re-review convergence」（再レビューで nit を抑える）と「Summary shape」（要約の冒頭の集計）は外れ、`REVIEW.md` はレビューで見つけて報告するものを変えるがレビューの形式は変えない、と明記されました。例の `REVIEW.md` の nit の上限の節も「Report at most five Nits per review.」だけになっています。

「Which branch REVIEW.md is read from」では、ブランチ保護として数えるもの（既定のブランチは classic のブランチ保護のルールか ruleset、ほかのブランチは ruleset だけ。ruleset は更新を制限するか、1 件以上の承認つきのプルリクエストを求め、その場合は新しい push で承認を外すか最後の push の後の承認を求める）と、ブランチの設定ごとに読む写しとファイルの表を示しています。保護を確認できない場合（保護されていない既定のブランチと、classic のルールだけの base のブランチの組み合わせを含む）は `REVIEW.md` を読みません。

- [Code Review をカスタマイズする - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/code-review-customize#use-review-md-for-review-only-rules)
- [Customize Code Review - Claude Code Docs (English)](https://code.claude.com/docs/en/code-review-customize#use-review-md-for-review-only-rules)
- [Code Review をカスタマイズする - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/code-review-customize#what-a-review-reads-for-each-branch-setup)
- [Customize Code Review - Claude Code Docs (English)](https://code.claude.com/docs/en/code-review-customize#what-a-review-reads-for-each-branch-setup)

## 4. Read and request reviews on a pull request

プルリクエストの作者とレビュアーのためのページです。節は「Severity levels」「Respond to findings」「Check run output」（「Read the result from a script」）「Request a review」（「Comment commands」「What a later review covers」「Review drafts and pull requests from forks」「Use Code Review alongside the Claude Code GitHub Action」）です。重大度の 3 段階（🔴 Important・🟡 Nit・🟣 Pre-existing）は旧ページと同じで、**Why this was flagged** の折りたたみは、レビューが理由を記録したときに付く、と改められました。

「Respond to findings」では、ブランチ保護が会話の解決を求めていなければ指摘に応じずにマージでき、指摘を消すにはスレッドを解決するか修正を push する、としています。「Check run output」では、**Files changed** の注釈は、行があるのにインラインのコメントとして投稿されなかった指摘に付き（旧ページは各指摘が注釈にもなるとしていた）、check run は neutral か、push がファイルを変えず自動のレビューが動かなかったときは skipped で終わり、失敗では終わらない、とされました。「Read the result from a script」は手順の形になり、出力の JSON のキーはアルファベット順（`{"nit": 1, "normal": 2, "pre_existing": 0}`）で、まだ開いている前のスレッドの指摘も数え、機械で読む行がない（失敗・タイムアウト・取り消し・より新しいレビューへの置き換え、完了した一部のレビュー）ときは指摘ゼロではなく「判定なし」として扱う、と加わりました。

「Request a review」には、開く・ready にする、コメントのコマンド、push、**Re-run**、中断したセッションの 1 回の自動の再試行、の 5 つの方法が並びます。コメントのコマンドは新しいトップレベルのコメントだけが対象で（インラインのコメント・レビューの本文・前のコメントの編集は数えない）、大文字と小文字は区別せず、書き込み権限は人ごとに GitHub に確かめ、ボットのコメントではレビューは始まりません。受け付けると **Claude Code Review** の check run が **Code review queued...** のタイトルで出て、始まると **Code review in progress...** に変わります（👀 の反応はレビューが始まらなくても付きうる）。draft への push は `@claude review always` の後でも始まらず、ready にしてから購読が効きます。リポジトリが Claude Code GitHub Action を既定の `@claude` の起動語で動かしていると、`@claude review` で Action も動くので、Action の `trigger_phrase` を変えるよう勧めています。

- [プルリクエストでレビューを読み、依頼する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/code-review-pull-requests#what-a-later-review-covers)
- [Read and request reviews on a pull request - Claude Code Docs (English)](https://code.claude.com/docs/en/code-review-pull-requests#what-a-later-review-covers)
- [プルリクエストでレビューを読み、依頼する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/code-review-pull-requests#read-the-result-from-a-script)
- [Read and request reviews on a pull request - Claude Code Docs (English)](https://code.claude.com/docs/en/code-review-pull-requests#read-the-result-from-a-script)

## 5. Code Review costs and usage

Code Review には 1 回あたりの定額の料金はなく、支出は各レビューの費用（レビューのレベル、変更の大きさ、周りのコードの複雑さ、確かめる候補の数で増える）とレビューの回数で決まる、と冒頭で示すページです。旧ページにあった「1 回あたり平均 $15〜25」の目安は載っていません。「Pricing」では、使用量のクレジットでトークンの使用量に応じて課金し、プランに含まれる使用量とは別で、プルリクエストを開いた開発者やレビューを依頼した開発者ではなく組織に課金される、と明記しています。他の機能で Amazon Bedrock・Google Cloud's Agent Platform・Microsoft Foundry を使っていても請求は Anthropic から届く点も、旧ページの 2 つのプロバイダーに Microsoft Foundry が加わりました。「How often reviews run」は各 **Review runs** の設定と、コメントのコマンド・draft・fork からのプルリクエストによる増減を整理しています。

新しい「Estimate your spend」は、広く展開する前に試験運用で月の支出を見積もる 4 段の手順です。試験用に月の支出上限を設定し、代表的ないくつかのリポジトリで **Once after PR creation** か **Manual (@claude review)** で有効にし、何回かレビューが動いたら **Repositories** の表の **Average cost** の列で 1 回の平均を読み、月に開くプルリクエストの数を掛けます（**After every push** なら 1 つのプルリクエストあたりの push の数をさらに掛ける）。

「Limit your spend」では、claude.ai/admin-settings/usage で Claude Code Review のサービスの月の上限を組織全体に設定すること、Code Review の支出上限・組織の使用量のクレジットの月の支出上限・使用量のクレジットの残高のどれかが尽きるとレビューを飛ばすこと、残りが 1 回のレビューの見込みの費用を下回った時点でも飛ばすことを示しています。「View usage」の claude.ai/analytics/code-review のダッシュボードの表は旧ページと同じです（`analytics` にも、Code Review は専用のダッシュボードを持つという案内が加わった）。

- [Code Review のコストと使用量 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/code-review-costs#estimate-your-spend)
- [Code Review costs and usage - Claude Code Docs (English)](https://code.claude.com/docs/en/code-review-costs#estimate-your-spend)
- [Code Review のコストと使用量 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/code-review-costs#limit-your-spend)
- [Code Review costs and usage - Claude Code Docs (English)](https://code.claude.com/docs/en/code-review-costs#limit-your-spend)

## 6. Troubleshoot Code Review

Code Review が思いどおりに動かないとき、まず **Claude Code Review** の check run のタイトルで進み具合を見分けるページです。「Check how far the review got」の表は、**Code review queued...**・**Code review in progress...**（待つ）、**Code review found no issues**（何もしない）、指摘があったというタイトル、**Code review skipped — no new changes**（最新の push で自動のレビューが動かなかった。`@claude review` で頼める）、**Code review failed**・**Code review timed out**、**Code review declined**（要約が予算か支出上限を挙げていれば予算の節へ）、check run がない、の 7 行です。

「A review didn't start」では、コメントのコマンドで始まらない原因として、そのリポジトリで Code Review がオンでない（コメントも check run も返らない）、コメントが条件に合わない、書き込み権限がない（ヒントがオンなら「No review was started: manual reviews can only be requested by someone with write access to this repository.」と返る）、予算が尽きた、の 4 つを挙げています。予算のメッセージは「⚠️ Code review skipped」で始まり、"has reached its monthly code review spending cap"（Code Review の月の上限）、"has no extra usage available to pay for this review"（クレジットの残高が空か組織の月の上限）、"is too low to start another review"（残りが 1 回の見込みの費用に足りない）の言い回しで尽きた上限が分かります。予算が戻ったら `@claude review` で飛ばされたレビューを頼みます。

ほかに、失敗かタイムアウトの再実行（要約が「The review session was interrupted before it could finish. A new review of this commit has been queued automatically.」なら 1 回の自動の再試行を待つ。**Re-run** は今の head のコミットを対象にする）、インラインに出ない指摘の探し方（インラインの場所がないか今の差分の外の指摘は、レビュー本文の **Additional findings** の見出しの下）、`REVIEW.md` についての check run の 2 つのメッセージ（保護されていない既定のブランチから読んだのでルートのファイルだけを使った／保護を確認できず `REVIEW.md` を使わなかった）、設定の問題（**Add a repository** にリポジトリが出ないときは名前で検索する、テストのプルリクエストに check run が出ないときの確認）の節があります。

- [Code Review のトラブルシューティング - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/code-review-troubleshooting#check-how-far-the-review-got)
- [Troubleshoot Code Review - Claude Code Docs (English)](https://code.claude.com/docs/en/code-review-troubleshooting#check-how-far-the-review-got)

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
- [**Code Review**](#1-code-review) ([日本語](https://code.claude.com/docs/ja/code-review#availability) / [English](https://code.claude.com/docs/en/code-review#availability)):  
  422 行（追加 78・削除 344）が変わりました。説明の大半が新しい 6 ページへ移り、利用の条件・レビューの進み方・レビューのレベル・アクセスできる範囲・レビューの受け方の比較をまとめた概要のページになりました（詳細はハイライト 1・2）
- [**Error reference**](#2-error-reference) ([日本語](https://code.claude.com/docs/ja/errors#response-exceeded-the-output-token-maximum) / [English](https://code.claude.com/docs/en/errors#response-exceeded-the-output-token-maximum)):  
  188 行（追加 181・削除 7）が変わりました。9 つの節と表の 12 行が加わり、画像のエラーとサイバーセキュリティの安全対策のメッセージの節が改められました（詳細はハイライト 4）
- [**Mods reference**](#3-mods-reference) ([日本語](https://code.claude.com/docs/ja/plugins/mods/reference#render-sites) / [English](https://code.claude.com/docs/en/plugins/mods/reference#render-sites)):  
  57 行（追加 33・削除 24）が変わりました。描画の場所と要素の表に VS Code 拡張機能が加わり、拡張機能が無視する props が載りました（詳細はハイライト 3）
- [**Use Claude Code in VS Code**](#4-use-claude-code-in-vs-code) ([日本語](https://code.claude.com/docs/ja/vs-code#a-formula-shows-as-raw-latex) / [English](https://code.claude.com/docs/en/vs-code#a-formula-shows-as-raw-latex)):  
  56 行（追加 56・削除 0）が変わりました。LaTeX の数式、開き直さない会話、パネルに描くプラグインの節と、トラブルシューティングの 2 節が加わりました（詳細はハイライト 3・5）
<!-- light:updated-pages:end -->

`llms-full.txt` から切り出したページ単位の差分（`git diff --no-index --numstat`）が 50 行以上の既存ページを挙げています。changelog（65 行）は、これまでどおり「軽微な更新」で扱います。次点は `plugins/mods/interface` の 47 行、`cloud-environments` の 23 行、`model-config` の 18 行で、いずれもハイライトか「軽微な更新」で扱います。

## 1. Code Review

ページの変更の大半はハイライト 1 の分割です。残った概要のページは次の節からなります。

- **冒頭**: 複数のエージェントが周りのコードとともに各変更を読み、確かめる段階が報告の前に指摘をコードと突き合わせる、指摘は重大度の順にインラインのコメント・要約・check run で届き、レビューはプルリクエストを承認もブロックもしない、と説明しています。レビューの 4 段階の図と、AI によるレビューは問題を見逃しうるので指摘がなくてもコードに誤りがない・安全だという意味ではない、という注記が加わりました
- **「Availability」と「Set up and use Code Review」**: 利用の条件（ハイライト 2）と、新しい 5 ページへのカードの一覧です
- **「How reviews work」**: Find（複数のエージェントが並行して差分と周りのコードを調べる）・Verify（候補を確かめて誤検知を除く）・Rank（重複を除き重大度で並べる）・Post（結果をプルリクエストに投稿する）の 4 段階と、レビューが残すもの（インラインの指摘と要約、**Claude Code Review** の check run、何もなければ **Code review found no issues** のタイトルと同じ短い注記）を示し、「Review levels」が続きます
- **「What a review can access」**: レビューは Anthropic のインフラの管理された環境で動き、セルフホストの環境では動かない。レビューの中のリポジトリへのアクセスは読み取りだけで、コミットを push しない。プルリクエストにはコメントと check run を投稿し、自分の前のスレッドを解決し、コメントのコマンドに 👀 で反応しうる。コードはビルドも実行もせず、差分と周りのコードを読んで調べる、としています
- **「Who controls a review」**: 自動のレビューは draft と fork からのプルリクエストを除き、コメントのコマンドは書き込み権限のある人からだけ受け付け、`REVIEW.md` は base か既定のブランチから読む、とまとめています
- **「Compare ways to get a review」**: Code Review・`/code-review`・Ultrareview・自分の CI の Claude（GitHub Actions・GitLab CI/CD）・自分のサブエージェントかスキルのレビュアーの 5 つを、始まり方・動く場所・使える人で比べる表です

本文には、同じ図の代替テキストの行が 2 回続き、`<span />` だけの行が 7 つあります。日本語版でも旧ページの `review-a-diff-locally` などの id が空の要素として残っているので、移した節へのリンクを壊さないためのものとみられます。

- [Code Review - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/code-review#availability)
- [Code Review - Claude Code Docs (English)](https://code.claude.com/docs/en/code-review#availability)

## 2. Error reference

新しい 9 つの節はハイライト 4 のとおりです。このほか次の節が改められました。

- **「Image was too large」**: 示すメッセージに `API Error: an image in the conversation could not be processed and was removed.` が加わり、これは API がサイズや寸法の上限を超える画像などを会話から断ったことを示す、とされました。同じエラーが繰り返すなら Claude Code を更新するよう求め、古い版での原因として、v2.1.299 より前は画像の多い長い会話で上限を超えた画像ではなく最後に添付した画像を外すことがあった（`was removed` の行が毎ターン出て、Claude は新しい画像を見ない）、v2.1.299 より前の VS Code・デスクトップアプリ・Agent SDK では Claude の作業中に添付した画像がサイズ変更されずに届いた、v2.1.166 より前は貼り付けた画像が会話に残って同じエラーを繰り返した（これまでの版の書き方は「2.1.142 より前」）、の 3 つを挙げています
- **サイバーセキュリティの安全対策の節**: 今のメッセージの例から「Apply to the Cyber Verification Program to reduce these interruptions.」の文が外れました。古い版の言い回しは対処の後の一覧にまとめられ、v2.1.219 から v2.1.296 まではこの文が閉じの文の前に入りえた、という項目が加わっています（「安全対策そのものはサーバー側で v2.1.203 より前からある」の文は外れた）
- **そのほか**: コンテキストの超過の節に、受け付けるトークンがもっと多いモデルで 200K 付近でこのエラーが出るなら、認識されないモデル ID のことがあるので `model-config` の方法で本当のウィンドウを伝える、という項目が、スキルの注入したコマンドの失敗の節の兄弟の文字列に `No shell command in <name> was run` が加わりました

- [エラーリファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/errors#response-exceeded-the-output-token-maximum)
- [Error reference - Claude Code Docs (English)](https://code.claude.com/docs/en/errors#response-exceeded-the-output-token-maximum)
- [エラーリファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/errors#image-was-too-large)
- [Error reference - Claude Code Docs (English)](https://code.claude.com/docs/en/errors#image-was-too-large)

## 3. Mods reference

変更の大半は、ハイライト 3 の VS Code 拡張機能への対応を表に反映したものです。

- **対象の版**: 冒頭が「Claude Code CLI と Desktop アプリの v2.1.290 時点」から、それに「VS Code 拡張機能の v2.1.299 時点」を加えた書き方になりました
- **「Render sites」**: `e.surface` は `terminal`・`desktop`・`vscode` のように描いているアプリを示す、と改められ、VS Code での描画には拡張機能 v2.1.299 以降と機能フラグを取得するセッションが要る、という段落が加わりました。表では `Pane`・`UserMessage`・`AssistantMessage`・`ToolUse`/`ToolResult`/`ToolGroup`・`AskUserQuestion`・`Spinner` の対応アプリに VS Code が加わっています（`AbovePrompt`・`CommandOutput` は Terminal と Desktop のまま）。`e.viewport` は、ターミナルとデスクトップではウィンドウを測るまでなく、VS Code では常にある、とされました
- **「Elements」**: 表に VS Code の列ができ、`Box`・`Text`・`Button`・`Link`・`Code`・`Markdown`・`Input`・`Select`・`Svg` は対応、`Client`・`Raster`・`Image` は非対応です。拡張機能が無視して省いたように描く props として、`Box` の `position`・`hover`、`Button` の `hotkey`・`plain`・`autoFocus`・`action`（ボタンはクリックか、フォーカスがあるときの Enter で押す）、`Code` の `language`・`path`・`startLine`・`format`・`wrap`（色も行番号もなく、`format: 'diff'` は差分の生の文字）、`Input`・`Select` の `autoFocus` が載りました

`plugins/mods/interface` も同じ対応で 47 行が変わり、「Draw in the VS Code extension」の節（ハイライト 3）のほか、`Link` の節の見出しが「`Link` in the Desktop app and VS Code」になり、ボタンのホットキーの表示の表に VS Code の列（ラベルだけが出てホットキーは効かない）、`autoFocus` は VS Code では何もしない、という説明が加わっています。

- [Mods リファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/plugins/mods/reference#render-sites)
- [Mods reference - Claude Code Docs (English)](https://code.claude.com/docs/en/plugins/mods/reference#render-sites)
- [Mods リファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/plugins/mods/reference#elements)
- [Mods reference - Claude Code Docs (English)](https://code.claude.com/docs/en/plugins/mods/reference#elements)

## 4. Use Claude Code in VS Code

56 行はすべて追加で、5 つの見出しが加わりました。

- **「LaTeX math in responses」**と**「A formula shows as raw LaTeX」**: ハイライト 5 のとおりです
- **「A conversation was not reopened」**と**「The panel stops responding each time a reload reopens a conversation」**: 再読み込みで会話を開き直す動作の安全策と、そのための v2.1.301 以降への更新の案内です（ハイライト 5）
- **「Plugins that draw in the panel」**: mod を含むプラグインがパネルに描くものと、そのラベルの意味です（ハイライト 3）

- [VS Code で Claude Code を使用する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/vs-code#a-formula-shows-as-raw-latex)
- [Use Claude Code in VS Code - Claude Code Docs (English)](https://code.claude.com/docs/en/vs-code#a-formula-shows-as-raw-latex)
- [VS Code で Claude Code を使用する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/vs-code#plugins-that-draw-in-the-panel)
- [Use Claude Code in VS Code - Claude Code Docs (English)](https://code.claude.com/docs/en/vs-code#plugins-that-draw-in-the-panel)

## 軽微な更新

<!-- light:minor-updates:start -->
今回の差分は **3 ファイル**（`llms-full.txt`・`llms.txt`・見出しマップ）です。`llms-full.txt` の生の差分は追加 13,591 行・削除 15,240 行ですが、これはページの並びが変わったためで、内容の変更の量ではありません。新しい 6 ページが前のほうに入り、9 ページ（`plugins/host-marketplace`・`plugins/loading`・`plugins/mods/admin`・`plugins/relevance`・`agent-sdk/claude-code-features`・`agent-sdk/examples`・`agent-sdk/migration-guide`・`agent-sdk/sessions`・`agent-sdk/troubleshooting`）の掲載位置が後ろへ移り、2 回展開されていた 5 ページの前のほうの写しが消えています。ページ単位に切り出して数えると 228 ページ中 **39 ページ**（新しい 6 ページを含む）が変わり、changelog が 65 行（追加のみ）、ほかの 38 ページが 1,652 行（追加 1,227・削除 425。うち新しい 6 ページが追加 759 行）です。大幅更新の 4 ページと新しい 6 ページ、`whats-new` の 3 ページ（「新着情報」で扱う）を除く **26 ページ**（changelog を含む）と、changelog に加わった **v2.1.301**（2026年10月15日、51 項目。Added 8・Changed 2・Improved 4・Fixed 37）を以下にまとめます。changelog の項目はすべて v2.1.301 のもので、前回の v2.1.300 との間の版の項はありません。

`llms-full.txt` の総行数は **122,303 行から 120,654 行へ 1,649 行減り**ました。内訳は、2 回展開されていた 5 ページ（`plugins/create-marketplace`・`plugins/org`・`plugins/troubleshooting`・`agent-sdk/agent-loop`・`agent-sdk/configuration`）が 1 回になった分の −2,540 行、新しい 6 ページの +783 行（タイトルと `Source:` の行を含む）、既存のページの差し引き +108 行です。`Source:` の行は 230 から 231 に、固有のページは 222 から 228 になり、2 回展開されているページは 8 から 3（`plugins/create`・`plugins/install`・`plugins/mods/overview`。2 つの写しはいずれも同じ内容）に減りました。

**新機能**

- `CLAUDE_CODE_RETRY_WATCHDOG_MAX_USAGE_LIMIT_WAIT_MS` を追加。無人の再試行モード（`CLAUDE_CODE_RETRY_WATCHDOG`）で、リセットが遠すぎる使用量の上限に当たった要求を、待たずに終わらせます
- `claude-api` スキルに OpenTelemetry のトレースの案内を追加（`ant` CLI でのトレースの送り先の設定を含む）
- vim モードに `%` のモーションを追加。対応する括弧に飛び、単独でも d/c/y とも使えます。`interactive-mode` の NORMAL モードの表にも、`()`・`[]`・`{}` の対応する括弧に飛ぶ（カーソルが括弧の上になければ今の行の次の括弧から）`%` と、そこまでを削除・変更・ヤンクする `d%`/`c%`/`y%` の行が加わりました（v2.1.301 以降） — [日本語](https://code.claude.com/docs/ja/interactive-mode#navigation-normal-mode) / [English](https://code.claude.com/docs/en/interactive-mode#navigation-normal-mode)
- mod の `Input` に `rows` を追加。端末で複数行の入力欄になり、Enter で送信、Shift+Enter か Enter の前のバックスラッシュで改行します
- OpenTelemetry の `tool_decision` のイベントに `classifier_verdict` と `permission_mode` を追加。auto モードの分類器の判断を権限ルールと区別できます
- `OTEL_LOG_TOOL_DETAILS=1` のとき、OpenTelemetry の `tool_decision` のイベントに、分類器のブロックが一致した組み込みのルールを示す `classifier_category` を追加
- [VSCode] Claude の応答の LaTeX の数式の描画を追加（詳細はハイライト 5 参照）
- [VSCode] VS Code と JetBrains のパネルの、Pro と Max のプランの使用量の上限のバナーに「Get more usage」のリンクを追加
- **mod の描画が VS Code 拡張機能に広がった**（`plugins/mods/interface`・`plugins/mods/reference`・`plugins/mods/overview`・`plugins/mods/troubleshoot`・`plugins/mods/gallery`・`plugins/mods/api`・`env-vars`・`vs-code`。詳細はハイライト 3 参照） — [日本語](https://code.claude.com/docs/ja/plugins/mods/overview#where-mods-run) / [English](https://code.claude.com/docs/en/plugins/mods/overview#where-mods-run)
- **`errors` に 9 つの節が加わった**（詳細はハイライト 4 参照）。このうち `--sandbox`・`--no-sandbox` の削除は `remote-control` のフラグの表にも「v2.1.300 で削除。渡すとサーバーはエラーで終わる」の行として、制御文字の拒否は `skills` の「Control characters in injected commands」としても載りました — [日本語](https://code.claude.com/docs/ja/skills#control-characters-in-injected-commands) / [English](https://code.claude.com/docs/en/skills#control-characters-in-injected-commands)

**機能改善**

- コンテキストウィンドウの小さいモデルへの切り替えを改善。新しいモデルには長すぎる会話を、先に前のモデルが要約します
- 長く動くサブエージェントの間の描画の性能を改善。進捗の表示を描画のたびに全部処理し直さず、少しずつ更新します
- アーティファクトを改善。Claude が書くページが固定のヘッダーの上の帯を塗るので、モバイルのアプリでスクロールした文字がそこに見えなくなります
- mod を改善。VS Code とデスクトップとモバイルのアプリでは、質問のダイアログの上に描く木が Markdown と最大 48 行を持てます（ターミナルは 12 の素の行のまま）（詳細はハイライト 3 参照）
- **認識されないモデル ID の警告と、本当のウィンドウの伝え方が載った**（`model-config`・`errors`。詳細はハイライト 4 参照） — [日本語](https://code.claude.com/docs/ja/model-config#which-ids-claude_code_max_context_tokens-applies-to) / [English](https://code.claude.com/docs/en/model-config#which-ids-claude_code_max_context_tokens-applies-to)
- **クラウドの SessionStart のフックの例が、変わっていなければ `npm install` を飛ばす形になった**（`cloud-environments` の「Install dependencies with a SessionStart hook」）。`scripts/install_pkgs.sh` は `$CLAUDE_PROJECT_DIR` に移り、`package.json`・`package-lock.json`・スクリプト自身のハッシュを `node_modules/.install_pkgs.sha256` に保存して、`sha256sum --check` が通れば `npm install` を飛ばします（失敗したときに次回やり直すよう、先に古いハッシュを消す）。成功の確かめ方（クラウドのセッションで Claude にそのファイルを見せてもらう）と、`npm install` がほかのファイル（ワークスペースの `package.json`・`.npmrc`・`postinstall` の入力など）を読むならハッシュの対象に足す、という注記も加わりました — [日本語](https://code.claude.com/docs/ja/cloud-environments#install-dependencies-with-a-sessionstart-hook) / [English](https://code.claude.com/docs/en/cloud-environments#install-dependencies-with-a-sessionstart-hook)
- **バックグラウンドのサブエージェントの編集の後の `/rewind` の説明が改められた**（`checkpointing` の「Subagent edits not restored」・`skills`・`agent-sdk/file-checkpointing`・`code-review-local`）。「巻き戻しは編集を戻さない」から、「会話の中で Claude がすでに編集していたファイルだけを戻し、ほかのファイルへの編集は残るので git で戻す」になりました — [日本語](https://code.claude.com/docs/ja/checkpointing#subagent-edits-not-restored) / [English](https://code.claude.com/docs/en/checkpointing#subagent-edits-not-restored)
- **WebFetch を止めても mod の `$.http.fetch` は止まらないと明記された**（`plugins/mods/admin` の「Know which controls still apply」）。`CLAUDE_CODE_DISABLE_WEB_FETCH` や `WebFetch` の deny ルールで WebFetch のツールをオフにしても、mod は `$.http.fetch` で要求できます。すべての利用者の mod で止めるには、利用者が入れた mod を読み込ませないか、ポリシーの mod で `http.fetch` をフックして利用者の mod の要求を断ります（失敗したフックは飛ばされて要求が通るので、`.catch` のハンドラーでも断る）。インストールできるプラグインを制限するだけでは、許した mod は要求できます。設定のフックについての「何も非推奨になっていない」の文は外れました — [日本語](https://code.claude.com/docs/ja/plugins/mods/admin#know-which-controls-still-apply) / [English](https://code.claude.com/docs/en/plugins/mods/admin#know-which-controls-still-apply)
- **Anthropic がホストする一部の MCP サーバーの説明は切り詰めないと明記された**（`mcp` の「Tool search for MCP server authors」）。`api.anthropic.com` で Anthropic がホストする一部の MCP サーバーの説明と指示は全文が Claude に届き、`CLAUDE_CODE_MAX_MCP_DESCRIPTION_LENGTH` はそれ以外のサーバーの上限を変える、と改められました（`env-vars` のこの変数の説明からも「長い文は切り詰める」の文が外れた） — [日本語](https://code.claude.com/docs/ja/mcp#tool-search-for-mcp-server-authors) / [English](https://code.claude.com/docs/en/mcp#tool-search-for-mcp-server-authors)
- **HTTP の MCP サーバーの起動時のタイムアウトについての注記が加わった**（`mcp-quickstart` の「Troubleshooting」）。v2.1.299 より前は、動いている HTTP のサーバーへの一部の接続が `MCP_TIMEOUT` によらず起動時にタイムアウトしたので、上限を上げても続くなら Claude Code を更新します — [日本語](https://code.claude.com/docs/ja/mcp-quickstart#troubleshooting) / [English](https://code.claude.com/docs/en/mcp-quickstart#troubleshooting)

**バグ修正**

- `WorktreeCreate` フックが作った worktree を、まだプッシュしていないコミットを持ちうるのに、終了時に尋ねずに削除する問題を修正
- 組織が最新の Fable のモデルを使えないとき、`fable`（と `best`）の別名が Anthropic API でエラーになる問題を修正。一つ前の Fable のモデルで 1 回再試行します
- ディスクがいっぱいでログインを更新できないとき、「Please run /login」という誤解を招くエラーが出る問題を修正。ディスクを名指しし、ファイルを消すよう伝えます
- 検索のプログラムが結果を返す前に予期せず失敗したとき、Grep と Glob が一致なしと報告する問題を修正。検索が失敗したというエラーを返します
- タスクの文に利用者の権限がないというハーネスの注記を読んだ後、ワークフローのエージェントが自分のステップを飛ばし、実行は成功と報告されることがある問題を修正
- Edit か Write を対象にする PreToolUse のフックがあると、アーティファクトの更新が断られる問題を修正。公開の呼び出しの中で変えずに、ファイルを編集してから公開し直します
- 引数の名前がとても多いか長いスキルとコマンドが、呼び出すと数秒止まる問題を修正。最初の 64 の名前（それぞれ 64 文字まで）だけを埋めます
- 引数が多くのプレースホルダーを埋めると、スキル・コマンド・フックが非常に多くのメモリを使う問題を修正
- RHEL 8 の MATE Terminal のような VTE 0.53 より古い端末で、フォルダーの信頼の確認に `>0q` のような文字が重なり、終了時にシェルのプロンプトの前に `>4m` が出る問題を修正
- 一部の版の iTerm2 で、起動時にプロンプトに `GOK` という文字が出る問題を修正
- プロバイダーが Bedrock でないのに、名前に `application-inference-profile` を含むモデルに切り替えると `awsAuthRefresh` のコマンドが動き、モデルの切り替えのフックが遅れる問題を修正
- `claude auth status` や `claude plugin list` のような短いコマンドがトークンの更新の途中で終わった後、サインインの更新のタイムアウトや予期しないサインアウトが起きる問題を修正
- 権限の確認の間にターンの途中で送ったメッセージで切られたツールの呼び出しが、利用者に拒否されたとモデルに伝わる問題を修正
- コンテキストウィンドウの小さいモデルへの切り替えで、前のモデルによる要約に、尋ねずに使用量のクレジットを使うことがある問題を修正
- 要求したのと違うモデルの名前を応答に書く LLM ゲートウェイの後ろで、選んでいないモデルで会話が何度も圧縮される問題を修正
- 遅いか忙しいマシンで、vim モードが Escape の後も INSERT のままになることがある問題を修正
- vim モードで、打った AskUserQuestion の答えを Esc が捨てる問題を修正。自由入力の欄が vim の NORMAL モードに対応し、Esc は NORMAL からだけ取り消します
- Read ツールが .xlsm・.parquet・.epub・.heic のようなバイナリのファイルを文字として読む問題を修正
- ヘッダーの行だけの Markdown の表が、端末に対して広すぎると何も描かれない問題を修正（プランの承認のカードのプランを含む）
- `/claude-api` スキルが、CMEK の外部キーのエンドポイントは Claude Platform on AWS で使えないと言う問題を修正
- `/rewind` の後、スキルがモデルに一覧されなくなる問題を修正
- 再開したセッションの圧縮の行が、読み込まれていない履歴に ctrl+o を示す問題を修正。前のメッセージの保存先を示し、全画面でも出ます
- 返答を中断した直後に「new task? /clear to save tokens」のヒントがまた出る問題を修正
- プラグインかスキルのフックの `ask` の判断による権限の確認に、どのプラグインかスキルのフックかが出ない問題を修正
- reftable のリポジトリで、git の確認の 1 つがタイムアウトか失敗したとき、`/diff` が衝突した cherry-pick や revert に気づかない問題を修正
- 同じセッションで Bash の `cd` の後、ワークフローのスクリプトを読む・編集する・実行し直すときに権限を求められるか断られる問題を修正
- 暗い ANSI のテーマと 16 色の端末の dim の文字を修正。塗りつぶしたボックスの中ではかすれ、選択と検索の強調の下ではかすれず、一覧の説明はほかの補助の文字と同じく dim になります
- `claude -p` の実行やクラウドのセッションのように、新しい Claude Code のプロセスの最初の返答が終わる前に呼ぶと、mod の `$.model.fork` が `nothing-to-fork` を返す問題を修正
- 全画面モード: 見えているトランスクリプトを作り直す間、`/compact` と自動圧縮が UI を少し固める問題を修正
- セルフホストのランナー: 管理された設定が MCP サーバーを制限していると、Slack から始めたセッションがリポジトリを見つけることも付けることもできない問題を修正。それらのツールを外しておくには `deniedMcpServers` を使います
- セルフホストのランナー: 関係のないセットアップかセッションの失敗が git の missing-ref の文言を引いたとき、セッションが元のブランチを削除されたと報告され、再試行されない問題を修正
- セルフホストのランナー: 終わろうとしているセッションについて、失敗したか断られたセッションの解放の再試行をログが約束する問題を修正。繰り返す失敗は回数を示します
- Windows: 止めたバックグラウンドの PowerShell のコマンドの出力ファイルに、最後の `[killed]` の行がない問題を修正
- [VSCode] パネルをクラッシュさせるか固まらせる会話が、再読み込みのたびに開き直される問題を修正（詳細はハイライト 5 参照）
- [VSCode] 長く考える間、チャットパネルが遅くなる問題を修正。更新のたびに考えている文全体を解析し直しません
- [VSCode] 一部の言語サーバーで、診断がルールのコード（例: MD013）ではなく「[object Object]」と出る問題を修正
- [VSCode] 音声入力を提供しない場所（claude.ai 以外のサインイン、リモートのウィンドウ）で、マイクの権限を確かめるためにネイティブの音声入力のモジュールを読み込む問題を修正

**その他**

- mod のフックの `.catch` のハンドラーを、フックが例外を投げるかタイムアウトしたときだけ動くように変更。フック自身の呼び出しの下で起きたイベントは、その `.catch` に尋ねずにそのフックを飛ばします
- mod の `$.env.set` を、変数を設定か解除すると `{}` で、書き込まないときは理由を示す `{ deny }` で解決するように変更
- **CMEK を使う組織の制限が各ページに加わった**（`web-quickstart`・`claude-code-on-the-web`・`ultrareview`・`code-review-local`）。CMEK を使う組織はクラウドのセッションを始められず、ultrareview も動かせない（ローカルで `/code-review` を動かす）と注記されました — [日本語](https://code.claude.com/docs/ja/ultrareview) / [English](https://code.claude.com/docs/en/ultrareview)
- **機能フラグの取得をオフにしたときのアーティファクトの確認が外れた**（`artifacts`）。公開の前に尋ねる場合の表から機能フラグの取得をオフにした行が、他人のアーティファクトを読む前に尋ねる場合から機能フラグの取得の条件が外れ、plan モードだけになりました
- **`analytics` に Code Review の使用量への案内が加わった**: Code Review には専用のダッシュボードがあり、レビューの活動と支出は `code-review-costs` の「View usage」を見る、とされました — [日本語](https://code.claude.com/docs/ja/analytics) / [English](https://code.claude.com/docs/en/analytics)
- **`memory` のトラブルシューティング**（「Claude isn't following my CLAUDE.md」）: `Instruction file not loaded` の通知が出たら `errors` の新しい節を見る、という項目が加わりました — [日本語](https://code.claude.com/docs/ja/errors#instruction-file-not-loaded) / [English](https://code.claude.com/docs/en/errors#instruction-file-not-loaded)
- **リンクの張り替え**: `commands`（`/code-review` と `/review` の行。`--fix` は「Claude に指摘を適用させる」の言い回しに）、`skills`、`desktop`、`github-enterprise-server`、`checkpointing` の `code-review` へのリンクが、`code-review-local` か `code-review-setup` に置き換わりました
- **`llms.txt`**: 新しい 6 ページの行が加わり、「Code review & CI/CD」の分類が「Code review and pull requests」とその下の 3 つの小分類に組み替わりました（ハイライト 1）。en のページの行は 257 から 264 に（新しい 6 ページと、後半の一覧に載った `code-review`）、固有のページは 222 から 228 になり、Indexes の 11 言語の行も「222 pages」から「228 pages」になりました
- **見出しマップ**: 149 行が加わり 69 行が外れました。加わったのは、新しい 6 ページ（見出し 58）、新しい分類「Code review and pull requests」とその小分類の見出し、そこへ移った `ultrareview`・`github-enterprise-server` の見出しのまとまり、`code-review` の新しい 6 見出し、`errors`（9）・`vs-code`（5）・`plugins/mods/interface`・`skills`・`model-config`（各 1）の新しい見出し、改称した 2 見出し（`plugins/mods/interface` の「`Link` in the Desktop app and VS Code」、`plugins/mods/troubleshoot` の「A drawing works in the terminal and not in the Desktop app or VS Code」）と新しいスタンプです。外れたのは、`code-review` の 25 見出し、移る前の `ultrareview`・`github-enterprise-server` のまとまり、古い分類「Code review & CI/CD」の見出し、改称前の 2 見出しと古いスタンプです
- **見出しマップ冒頭の自動生成スタンプが、2026年10月15日 04時55分03秒 UTC から 2026年10月15日 20時03分17秒 UTC へ進みました**

**参考リンクについて**: 日本語版は、新しい 6 ページと、ハイライト・大幅更新・軽微な更新で取り上げたページのうち次のページ（`code-review`・`plugins/mods/interface`・`plugins/mods/reference`・`plugins/mods/overview`・`plugins/mods/admin`・`plugins/mods/troubleshoot`・`vs-code`・`errors`・`model-config`・`cloud-environments`・`interactive-mode`・`skills`・`checkpointing`・`remote-control`・`mcp`・`mcp-quickstart`・`ultrareview`・`memory`・`analytics`）を取得し、該当する節があるかと今回の内容（新しい節や書き換えた文）になっているかを 52 か所で確かめました。今回も日本語版の追従が早く、Code Review の 6 つの新しいページの日本語版がすでに公開され、`code-review` の日本語版も新しい構成になっていたほか、確かめたすべての節がすでに今回の内容になっていたため、すべて日本語版のリンクを付けています。取得して確かめていないページ（`artifacts`・`env-vars`・`commands`・`plugins/mods/gallery`・`plugins/mods/api`・`web-quickstart`・`claude-code-on-the-web`・`agent-sdk/file-checkpointing` など）と、changelog だけに載っていて対応する節のない項目にはリンクを付けていません。**changelog ページへのリンクは、本サマリの方針どおり付けていません。**
<!-- light:minor-updates:end -->

## 新着情報

<!-- light:whats-new:start -->
**`whats-new/` 配下では 3 ページが動きましたが、いずれもリンク先の張り替えだけです。** 2026年の Week 30・32・33 の各ダイジェストで、`/code-review` の項目のリンク先が `code-review#review-a-diff-locally` から新しい `code-review-local` に置き換わりました。ダイジェストの本文に変更はなく、新しい週のダイジェストは加わっていません。
<!-- light:whats-new:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-10-14.md](./archives/latest/2026-10-14.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-10-14.md](./archives/latest-detail/2026-10-14.md)

<!--
base_commit: eeed0d5ebbc9b23608e5903e7bc33bb6c996a581
head_commit: 23d4d90c662169bb09c107096793481648358905
generated_at_full: 2026-10-16T15:11:43+09:00
-->
