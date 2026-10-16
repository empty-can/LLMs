---
対象期間: 2026年10月14日 〜 2026年10月15日
作成日: 2026-10-15
---

# Claude Code 公式ドキュメント更新サマリ

```markdown
**今回は、1 ページだった Code Review の文書が概要と 6 つの新しいページに分かれ、レビューのレベル（Quick・Standard・Deep）、GitHub の組織全体を対象にする設定、サブディレクトリの `REVIEW.md` と読むブランチの規則などが新たに載りました。mod が VS Code 拡張機能のチャットパネルにも描けるようになり（拡張機能 v2.1.299 以降）、VS Code では応答の LaTeX の数式が組版されるようになりました（v2.1.301 以降）。`errors` には 9 つの節が加わり、changelog には v2.1.301（2026年10月15日、51 項目）が積まれています**。新しいページは 6 つで、ページ単位で数えると 228 ページ中 39 ページ（新しい 6 ページと changelog を含む）が変わり、changelog を除く変更は 1,652 行（追加 1,227・削除 425）、4 ページが大幅更新です。総行数は 122,303 行から 120,654 行に減りました（2 回展開されていた 5 ページが 1 回になったため）。

主要なものを以下に挙げます。

1. Code Review の文書が概要と 6 つの新しいページ（`/code-review`・有効化・カスタマイズ・プルリクエスト・費用・トラブルシューティング）に分かれ、`llms.txt` に「Code review and pull requests」の分類ができた
2. Code Review に、レビューのレベル、GitHub の組織全体を対象にする設定、ヒントのコメント、サブディレクトリの `REVIEW.md` と読むブランチの規則、返信を読む後のレビューなどが載り、1 回 $15〜25 の目安などの記述が外れた
3. mod が VS Code 拡張機能のチャットパネルにも描けるようになり（拡張機能 v2.1.299 以降・機能フラグを取得するセッション）、描画の場所と要素の表に VS Code が加わった
4. `errors` に 9 つの節（読み込まれなかった指示ファイル、出力トークンの上限で切れた応答、管理された設定で無視されるサンドボックスの許可など）が、`model-config` に認識されないモデル ID の警告とウィンドウの正し方が載った
5. VS Code のチャットパネルが応答の LaTeX の数式を組版するようになり（v2.1.301 以降）、開くのに 2 回続けて失敗した会話を再読み込みで開き直さない動作が載った
```

## ハイライト

1. [**Code Review の文書が 7 ページに分かれた**](./latest-detail.md#1-code-review-の文書が-7-ページに分かれた):  
  386 行の 1 ページだった `code-review` が 123 行の概要になり、`/code-review` コマンド・有効化・カスタマイズ・プルリクエストでの読み方と依頼の仕方・費用・トラブルシューティングの 6 ページ（計 759 行）が新しくできました。`llms.txt` では「Code review & CI/CD」が「Code review and pull requests」の分類に替わり、その下に「Code Review」「Security scans」「Run Claude in your own CI」ができています
2. [**Code Review にレビューのレベルと REVIEW.md を読むブランチの規則などが載った**](./latest-detail.md#2-code-review-にレビューのレベルと-reviewmd-を読むブランチの規則などが載った):  
  レビューのレベル（Quick・Standard・Deep）、新しい有効化の手順、GitHub の組織全体を対象にする設定、ヒントのコメント、サブディレクトリの `REVIEW.md` と、どのブランチの `REVIEW.md` を読むか（ブランチ保護による違い）、返信を読んで範囲を絞る後のレビューなどが文書になりました。research preview の注記、👍/👎 での評価、1 回平均 $15〜25・平均 20 分の目安の記述は外れています
3. [**mod が VS Code 拡張機能のチャットパネルにも描けるようになった**](./latest-detail.md#3-mod-が-vs-code-拡張機能のチャットパネルにも描けるようになった):  
  `plugins/mods/interface` に「Draw in the VS Code extension」の節ができ、拡張機能 v2.1.299 以降・機能フラグを取得するセッションで、mod の描いたものがチャットパネルに出るようになりました（`e.surface` は `vscode`）。`plugins/mods/reference` の描画の場所と要素の表に VS Code が加わり、`vs-code` にはパネルに描くプラグインのラベルの説明が載りました
4. [**errors に 9 つの節が加わり認識されないモデル ID の扱いが載った**](./latest-detail.md#4-errors-に-9-つの節が加わり認識されないモデル-id-の扱いが載った):  
  `errors` に、読み込まれなかった指示ファイル、出力トークンの上限で切れた応答、管理された設定のロックで無視されるサンドボックスの許可、読み込まれない管理された設定のフック、予約された MCP サーバーの名前などの 9 節が加わりました。`model-config` には、モデル ID を認識できず 200K のウィンドウと仮定したときの起動時の警告と、正し方の 4 つの方法が載りました
5. [**VS Code のチャットパネルが LaTeX の数式を組版するようになった**](./latest-detail.md#5-vs-code-のチャットパネルが-latex-の数式を組版するようになった):  
  `vs-code` に「LaTeX math in responses」の節ができ、v2.1.301 以降のチャットパネルは応答の `$$ … $$`・`\[ … \]`・`$…$`・`\(…\)` の数式を組版します。組版されないときの調べ方の節と、開くのが 2 回続けて終わらなかった会話を再読み込みで開き直さない動作（「A conversation was not reopened」）も加わりました

## 新規追加されたページ

- [**Review locally with /code-review**](./latest-detail.md#1-review-locally-with-code-review) ([日本語](https://code.claude.com/docs/ja/code-review-local#choose-what-to-review) / [English](https://code.claude.com/docs/en/code-review-local#choose-what-to-review)):  
  旧 `code-review` の「Review a diff locally」を独立させた、`/code-review` コマンドのページです。レビューの対象の指定の表や、レビューを置き換える方法が加わりました（170 行。詳細はハイライト 1）
- [**Set up Code Review**](./latest-detail.md#2-set-up-code-review) ([日本語](https://code.claude.com/docs/ja/code-review-setup#turn-on-code-review) / [English](https://code.claude.com/docs/en/code-review-setup#turn-on-code-review)):  
  Owner が Code Review を有効にし、組織の既定とリポジトリを管理するページです。新しい有効化の手順、レビューのレベル、GitHub の組織全体を対象にする設定が載っています（160 行。詳細はハイライト 2）
- [**Customize Code Review**](./latest-detail.md#3-customize-code-review) ([日本語](https://code.claude.com/docs/ja/code-review-customize#which-branch-review-md-is-read-from) / [English](https://code.claude.com/docs/en/code-review-customize#which-branch-review-md-is-read-from)):  
  `CLAUDE.md` と `REVIEW.md` でレビューの指摘を調整するページです。サブディレクトリの `REVIEW.md` と、どのブランチの `REVIEW.md` を読むかの規則が加わりました（128 行。詳細はハイライト 2）
- [**Read and request reviews on a pull request**](./latest-detail.md#4-read-and-request-reviews-on-a-pull-request) ([日本語](https://code.claude.com/docs/ja/code-review-pull-requests#respond-to-findings) / [English](https://code.claude.com/docs/en/code-review-pull-requests#respond-to-findings)):  
  開発者がプルリクエストで指摘を読み、応じ、レビューを依頼するためのページです。後のレビューの範囲やスクリプトでの結果の読み方が詳しくなりました（144 行。詳細はハイライト 2）
- [**Code Review costs and usage**](./latest-detail.md#5-code-review-costs-and-usage) ([日本語](https://code.claude.com/docs/ja/code-review-costs#estimate-your-spend) / [English](https://code.claude.com/docs/en/code-review-costs#estimate-your-spend)):  
  Code Review の課金、費用を左右するもの、見積もり、支出の上限、使用量の確かめ方をまとめたページです（71 行）
- [**Troubleshoot Code Review**](./latest-detail.md#6-troubleshoot-code-review) ([日本語](https://code.claude.com/docs/ja/code-review-troubleshooting#check-how-far-the-review-got) / [English](https://code.claude.com/docs/en/code-review-troubleshooting#check-how-far-the-review-got)):  
  check run のタイトルからレビューの進み具合を見分け、始まらない・失敗した・予算で飛ばされたレビューや、設定の問題に対処するページです（86 行）

## 大幅に更新されたページ

- [**Code Review**](./latest-detail.md#1-code-review) ([日本語](https://code.claude.com/docs/ja/code-review#availability) / [English](https://code.claude.com/docs/en/code-review#availability)):  
  422 行（追加 78・削除 344）が変わりました。説明の大半が新しい 6 ページへ移り、利用の条件・レビューの進み方・レビューのレベル・アクセスできる範囲・レビューの受け方の比較をまとめた概要のページになりました（詳細はハイライト 1・2）
- [**Error reference**](./latest-detail.md#2-error-reference) ([日本語](https://code.claude.com/docs/ja/errors#response-exceeded-the-output-token-maximum) / [English](https://code.claude.com/docs/en/errors#response-exceeded-the-output-token-maximum)):  
  188 行（追加 181・削除 7）が変わりました。9 つの節と表の 12 行が加わり、画像のエラーとサイバーセキュリティの安全対策のメッセージの節が改められました（詳細はハイライト 4）
- [**Mods reference**](./latest-detail.md#3-mods-reference) ([日本語](https://code.claude.com/docs/ja/plugins/mods/reference#render-sites) / [English](https://code.claude.com/docs/en/plugins/mods/reference#render-sites)):  
  57 行（追加 33・削除 24）が変わりました。描画の場所と要素の表に VS Code 拡張機能が加わり、拡張機能が無視する props が載りました（詳細はハイライト 3）
- [**Use Claude Code in VS Code**](./latest-detail.md#4-use-claude-code-in-vs-code) ([日本語](https://code.claude.com/docs/ja/vs-code#a-formula-shows-as-raw-latex) / [English](https://code.claude.com/docs/en/vs-code#a-formula-shows-as-raw-latex)):  
  56 行（追加 56・削除 0）が変わりました。LaTeX の数式、開き直さない会話、パネルに描くプラグインの節と、トラブルシューティングの 2 節が加わりました（詳細はハイライト 3・5）

## 軽微な更新

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

## 新着情報

**`whats-new/` 配下では 3 ページが動きましたが、いずれもリンク先の張り替えだけです。** 2026年の Week 30・32・33 の各ダイジェストで、`/code-review` の項目のリンク先が `code-review#review-a-diff-locally` から新しい `code-review-local` に置き換わりました。ダイジェストの本文に変更はなく、新しい週のダイジェストは加わっていません。

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-10-14.md](./archives/latest/2026-10-14.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-10-14.md](./archives/latest-detail/2026-10-14.md)

<!--
base_commit: eeed0d5ebbc9b23608e5903e7bc33bb6c996a581
head_commit: 23d4d90c662169bb09c107096793481648358905
generated_at_full: 2026-10-16T15:11:43+09:00
-->
