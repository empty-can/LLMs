---
対象期間: 2026年10月08日 〜 2026年10月09日
作成日: 2026-10-09
---

# Claude Code 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
**今回は、失敗したフックで操作を止める `onFailure`、Claude apps gateway のポリシーの `code` キー、セルフホストの Anthropic git proxy の対応範囲と手順、mod の `$.model.complete` のプロンプトキャッシュ、Agent SDK の `/usage` の構造化された報告が文書に加わりました。changelog には v2.1.296（79 項目）が積まれています**。新しいページはなく、ページ単位で数えると 221 ページ中 58 ページ（changelog を含む）が変わり、changelog を除く変更は 1,584 行（追加 1,290・削除 294）、9 ページが大幅更新です。総行数は 119,210 行から 120,369 行に増えました。

主要なものを以下に挙げます。

1. command と HTTP のフックに `"onFailure": "block"` を付けると、起動できない・時間切れなどで失敗したフックが操作を止めるようになり、終了コードと標準出力の組み合わせが表になった（v2.1.295 以降）
2. Claude apps gateway のポリシーの設定を `cli` ではなく `code` キーの下に置くと、条件を満たせばデスクトップアプリの Code タブにも届く（ゲートウェイに v2.1.296 以降が要る）
3. セルフホストの Anthropic git proxy は github.com のリポジトリだけを扱い、ランナーのユーザーのグローバルな git の設定を置き換えると明記され、オン・オフの手順と起動失敗の見分け方が加わった
4. mod の `$.model.complete` に `{ text, cache: true }` のブロックの配列を渡して、プロンプトキャッシュの区切りを置けるようになった（v2.1.292 以降）
5. Agent SDK で `/usage` を送ると、その報告が `SDKUsageReport` 型の `usage_report` としてメッセージに付くようになった（v0.3.273 以降）
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**フックが失敗したときに操作を止める onFailure の節ができた**](#1-フックが失敗したときに操作を止める-onfailure-の節ができた):  
  command と HTTP のフックに `"onFailure": "block"` を付けると、起動できない・時間切れ・0 と 2 以外の終了コード・不正な出力で失敗したフックが操作を止めます（v2.1.295 以降）。「Exit code output」も標準出力と終了コードの組み合わせの表に書き直されました
2. [**Claude apps gateway の code キーでデスクトップの Code タブにも設定が届くようになった**](#2-claude-apps-gateway-の-code-キーでデスクトップの-code-タブにも設定が届くようになった):  
  ポリシーの Claude Code の設定を推奨の `code` キーの下に置くと、デスクトップアプリ 2.9939.2 以降などの条件を満たせば Code タブにも効きます。ゲートウェイには v2.1.296 以降が要り、`cli` と混ぜると起動しません
3. [**セルフホストの Anthropic git proxy の対応範囲と設定手順が全面的に書き直された**](#3-セルフホストの-anthropic-git-proxy-の対応範囲と設定手順が全面的に書き直された):  
  git proxy は github.com のリポジトリだけを扱い、ランナーのユーザーのグローバルな git の設定をバックアップなしに置き換えると明記されました。オン・オフの手順と、セッションが始まらないときの見分け方が加わっています
4. [**mod の $.model.complete でプロンプトキャッシュを使えるようになった**](#4-mod-の-modelcomplete-でプロンプトキャッシュを使えるようになった):  
  `prompt` か `system` を `{ text }` のブロックの配列で渡し、静的な内容の最後のブロックに `cache: true` を付けると区切りになります（v2.1.292 以降）。`$.model.fork` との違いの表と、キャッシュに当たったかの確かめ方も載りました
5. [**Agent SDK で /usage の報告を構造化して受け取れるようになった**](#5-agent-sdk-で-usage-の報告を構造化して受け取れるようになった):  
  claude.ai の資格情報のセッションで `/usage` を送ると、アシスタントのメッセージに `SDKUsageReport` 型の `usage_report` が付き、費用の累計とプランの使用量の行を読めます（Agent SDK v0.3.273 以降）
<!-- light:highlight-list:end -->

## 1. フックが失敗したときに操作を止める onFailure の節ができた

**`hooks` に「Block the action when a hook fails」の節ができました。** ほとんどのイベントでは、フックが失敗したり時間切れになったりしても Claude Code は操作を続けるため、パスを間違えた方針のフックや落ちるスクリプトはすべてを通してしまいます。`command` か `http` のフックに `"onFailure": "block"` を付けると、代わりに操作を止めます（既定は `"continue"`。Claude Code v2.1.295 以降）。command と HTTP のフックの項目の表にも `onFailure` の行が加わりました。

- **例**: `.claude/settings.json` の `PreToolUse` のフックが、各 Bash のコマンドの前に `node` で `${CLAUDE_PROJECT_DIR}/.claude/hooks/check-command.js` を動かし、失敗すれば止めます。スクリプトを置かずに `ls` を頼むと呼び出しが止まり、エラーに `failed; blocking because onFailure is "block"` と node のエラーが続きます（時間切れなら `failed` が `timed out` になる）。`onFailure` がなければ同じ状況は止めない失敗で、`ls` は動きます
- **失敗に数えるもの**: 起動できない（スクリプトや実行ファイルがない）、0 と 2 以外の終了コード（`permissionDecision: "allow"` のように許す JSON を出していても数えるので、JSON で判断を返すなら終了コード 0 にする）、HTTP のエラー（接続の失敗か 2xx 以外の状態）、`timeout` に達した、出力の JSON が解析できないかスキーマの検証に通らない（HTTP のフックでは、空でも JSON のオブジェクトでもない 2xx の本文も）、の 5 つです。command のフックの平文の標準出力は失敗ではありません
- **止めたときの振る舞い**: そのイベントで終了コード 2 がすることをします。ただし `PermissionRequest` では要求を拒否します。例えば `PreToolUse` ならツールの呼び出しを、`UserPromptSubmit` ならプロンプトを止めます
- **効かないフック**: `Stop`・`SubagentStop`・`TaskCompleted`・`TeammateIdle` のフック（これらで終了コード 2 は Claude に作業を続けさせるが、動かないフックを Claude は直せない）と、`async` か `asyncRewake` のバックグラウンドの command のフックです
- **時間切れの記述からも案内**: `PreToolUse` で時間切れになった command・http のフックは呼び出しを止めない、という箇所と、`UserPromptSubmit` の時間切れの箇所に、止めたいなら `onFailure: "block"` を付ける、と加わりました

**「Exit code output」も書き直されました。** 終わったフックの結果を「成功（終了コード 0。JSON の項目を適用し、それが止めない限り操作は進む）」「止める失敗（終了コード 2。止められるイベントでは操作を止める）」「止めない失敗（それ以外の終了コードか、起動しない・不正な JSON を出すなどの失敗）」の 3 つに整理し、標準出力の中身（検証に通る JSON・解析できないか検証に通らない JSON・平文か空）と終了コード（0・2・それ以外）の組み合わせごとの結果が表になりました。例えば、検証に通る JSON を出して終了コード 1 で終わる `PreToolUse` のフックは成功で、項目だけで結果が決まります（`onFailure: "block"` なら失敗に数える）。イベント独自の規則（`WorktreeCreate`・`WorktreeRemove`、標準出力なしで終了コード 2 で終わり標準エラーがファイルがないと言う `Stop`・`SubagentStop`・`TaskCompleted` とプラグインの `UserPromptSubmit` のフック、`Elicitation`・`ElicitationResult`、`StopFailure` のように出力を捨てるイベント）は箇条書きにまとめられました。終了コード 2 で止めたときに Claude が受け取るエラー（`PreToolUse:Bash hook error: [...]: Blocked: rm commands are not allowed`）と、ほかの終了コードの通知（`Failed with non-blocking status code: something broke`）の例も載っています。

`hooks-guide` も合わせて改められ、HTTP のフックは 2xx 以外の状態や失敗した要求が止めない失敗になり、失敗で止めたいなら `onFailure: "block"` を付ける、と加わりました。「Debug techniques」の節は「Check what a hook did」に改称されています。

- [Hooks リファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/hooks#block-the-action-when-a-hook-fails)
- [Hooks reference - Claude Code Docs (English)](https://code.claude.com/docs/en/hooks#block-the-action-when-a-hook-fails)
- [Hooks リファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/hooks#exit-code-output)
- [Hooks reference - Claude Code Docs (English)](https://code.claude.com/docs/en/hooks#exit-code-output)

## 2. Claude apps gateway の code キーでデスクトップの Code タブにも設定が届くようになった

**`claude-apps-gateway-config` に「Choose `cli` or `code`」の節ができました。** ポリシーの Claude Code の設定（`.env` の読み取りを拒むルールなど）は `cli` か `code` のキーの下のブロックに置き、どちらも中身は同じで、`code` が推奨、`cli` が従来のキーです。キーによって設定が効く場所が変わります。

- **`cli`**: 端末、VS Code と JetBrains の拡張機能、Agent SDK。デスクトップアプリの Code タブには導出した設定しか届かないので、`Read(./.env)` のような範囲を限ったルールはそこでは利用者を止めません
- **`code`**: 同じ場所に加え、デスクトップアプリの Code タブも対象にできます。例は `code` の下に `permissions: { deny: ["Read(./.env)"] }` を置き、空の `desktop: {}` を添えたポリシーです
- **警告**: `code` にはゲートウェイのサーバーに Claude Code v2.1.296 以降が要り、それより前のゲートウェイはこのキーを見つけると起動しません。キーを加える前にすべてのレプリカを上げ、前の版に戻す前に `code` を `cli` に戻します。`code` と `cli`（または以前の綴りの `settings`）が同じファイルにあっても起動が止まるので、1 回の編集ですべてのブロックを 1 つのキーの下にそろえます
- **移行**: `cli` を使うファイルはこれまでどおり動き、`desktop` のキーを持つポリシーで `cli` を見つけたゲートウェイは起動時に警告を出して起動します。切り替えるときは、ブロックを改名する同じ編集で `serve_to_desktop` の行を消します。`cli` の以前の名前 `settings` の注記も、新しい導入では `code` を使う、と改められました

**「Apply `code` settings in the Code tab」の節は、Code タブで `code` の設定が効く条件を挙げています。** ポリシーが `desktop` のキーを持つ（空の `desktop: {}` でもよい）、デスクトップアプリが 2.9939.2 以降、マシンの Claude Code の管理設定がこのゲートウェイを指している、そのマシンがプライベートなネットワークの HTTPS でゲートウェイに届く、の 4 つで、後の 2 つはセッションの Claude Code を動かすマシン（ローカルのセッションなら利用者のコンピューター、SSH の Code タブのセッションならリモートのホスト）に当てはまります。`cli` を `code` に改名する前に、それらのマシンにクライアント側の管理設定を配るよう求めています。

- **条件を満たさないとき**: 前の 2 つを満たし後のどちらかを欠くと、HTTPS でデスクトップアプリが v2.1.296 以降の Claude Code を同梱していれば Code タブは始まらず、プロンプトへの返信が理由を示します。それより前の版を同梱していれば `code` の設定なしで始まり、セッションの中では何も示されません。平文の HTTP なら同梱の版によらず設定なしで始まります。ゲートウェイの前のプロキシが `/managed/settings` に自分の 404 を返す場合も、4 つの条件を満たすマシンを含めて設定なしで始まります
- **WebSearch**: `desktop` のキーを持つポリシーで、設定を持つ `code` のブロックは、Cowork・Chat・Code タブの WebSearch ツールを止めます
- **関連ページ**: `claude-apps-gateway` では、ブロックのほかのキー（フック・`env`・範囲を限った権限のルール）は `/login` でサインインするクライアントに届き、`code` の下なら条件を満たす Code タブのセッションにも届くが、Cowork と Chat には届かない、と改められました。`managed-settings` のリモートの設定を取得する条件にも、設定を届けるゲートウェイの後ろの Code タブで動く場合が加わっています。承認のダイアログを出せない非対話の実行の例にも Code タブのセッションが加わりました

changelog の v2.1.296 にも、`managed.policies[]` の `code` キー（`cli` と同じ設定を Code タブにも適用し、`desktop` と並べるとデスクトップアプリのゲートウェイモードをオンにする）と、Code タブのセッションが始まらないときに理由を返信として示す改善が載っています。

- [Claude apps gateway 設定 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/claude-apps-gateway-config#choose-cli-or-code)
- [Claude apps gateway configuration - Claude Code Docs (English)](https://code.claude.com/docs/en/claude-apps-gateway-config#choose-cli-or-code)
- [Claude apps gateway 設定 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/claude-apps-gateway-config#apply-code-settings-in-the-code-tab)
- [Claude apps gateway configuration - Claude Code Docs (English)](https://code.claude.com/docs/en/claude-apps-gateway-config#apply-code-settings-in-the-code-tab)

## 3. セルフホストの Anthropic git proxy の対応範囲と設定手順が全面的に書き直された

**`self-hosted-environments-deploy` の「Use the Anthropic git proxy」が書き直されました。** Anthropic git proxy（Anthropic-managed git とも呼ぶ）では、ランナーのイメージにセッションのための SSH の鍵・認証情報ヘルパー・`.netrc` などの git の資格情報が要らず、ランナーはセッションの git を Anthropic に任せます。Anthropic が扱う利用者のセッションでは、ランナーのクローンとセッション自身の取得・プッシュが Anthropic を通り、セッションの作成者の GitHub の OAuth トークンを使います（ボットとエージェントのセッションは組織の GitHub App のインストールトークン）。git proxy はオンにしない限りオフで、自分の資格情報で git のホストに届くランナーには要りません。その代わり次の制約があります。

- **github.com だけ**: Anthropic がセッションを扱うのはすべてのリポジトリが github.com にあるときだけで、GitHub Enterprise Server にはまだ対応しません。ほかの git のホストのリポジトリを 1 つでも含むセッションは、github.com のリポジトリも含めて扱われず、起動に失敗します。これまでの記述は「利用者のセッションでは GitHub か GitHub Enterprise の OAuth トークンを使う」でした
- **GitHub の接続**: 利用者のセッションの作成者が claude.ai で GitHub を接続していないと、セッションは始まりません
- **グローバルな git の設定の置き換え**: ランナーは、起動時と各セッションの前に、自分が動くユーザーのグローバルな git の設定をバックアップなしに消して置き換えます。そこに置いたログインや認証情報ヘルパーは失われる（`--configure-git` が書く設定は残る）ので、専用のユーザーかコンテナーで動かし、自分のユーザーでは決して動かさないよう警告しています。ID や `safe.directory` のような秘密でない設定は、システムの git の設定に置きます
- **ホストからのプッシュ**: `--push-outcome-on-release` のプッシュと `post-session` のフックのプッシュは、引き続きランナーのホスト自身の資格情報と `github.com` への経路を使います
- **オンにする**: Claude Code v2.1.267 以降（それより前はフラグを受け付けても要求を報告せず、Anthropic はそのセッションを扱わない）、`--capacity 1`（既定）、Git 2.32 以降が要ります。起動時に `Registering as opted in to Anthropic-managed git (--use-anthropic-git-proxy)` が出て、Anthropic が扱う各セッションでは `governed git ACTIVE` を含む `[runner:session]` の行が記録されます
- **起動に失敗したとき**: ランナーのログの、`/git_proxy/` を含む `api.anthropic.com` のアドレスを名指す git のエラーで見分けます。`the server withheld Anthropic-managed git for this session` の行は扱われなかったことを示し、github.com 以外のリポジトリがあるならその環境のランナーの git proxy をオフにし、すべて github.com ならセッション ID を添えて Anthropic のアカウントチームに報告します。`remote: access denied by the git proxy` は組織の方針などによる拒否、`GitHub authentication required. Please reconnect your GitHub account.` は作成者の GitHub の接続がないことを示します
- **オフにする**: フラグか `CLAUDE_RUNNER_USE_GIT_PROXY` を外し、github.com を含むすべての git のホストの資格情報を与え（グローバルな設定にあった資格情報は消えている）、git のホストへの経路を開け、ランナーを再起動する、の 4 つの手順が載りました

同じ趣旨で、`self-hosted-environments-reference` の `--use-anthropic-git-proxy` は「github.com のリポジトリを git proxy でクローンする」に改められ、`self-hosted-environments` のネットワークの経路には、Anthropic-managed git のセッションの子プロセスが github.com への `git` と `gh` の通信を `api.anthropic.com` への WebSocket で送る、と加わりました（オーケストレーターの SCM コネクタは使えず、そのトンネルは開かない、とも書かれています）。ネットワークの要件の表も、git proxy を使うランナーは `github.com` への経路が要らないが、`--push-outcome-on-release` か `post-session` のフックからプッシュするなら要る、という書き方になっています。

- [本番環境へのセルフホスト環境のデプロイ - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/self-hosted-environments-deploy#use-the-anthropic-git-proxy)
- [Deploy self-hosted environments to production - Claude Code Docs (English)](https://code.claude.com/docs/en/self-hosted-environments-deploy#use-the-anthropic-git-proxy)
- [本番環境へのセルフホスト環境のデプロイ - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/self-hosted-environments-deploy#when-anthropic-doesnt-serve-a-session)
- [Deploy self-hosted environments to production - Claude Code Docs (English)](https://code.claude.com/docs/en/self-hosted-environments-deploy#when-anthropic-doesnt-serve-a-session)

## 4. mod の $.model.complete でプロンプトキャッシュを使えるようになった

**`plugins/mods/api` の「Call a model」が書き直されました。** `$.model.complete` はプロンプトだけを、`$.model.fork({ prompt })` は今の会話の末尾にプロンプトを付けて送る、と並べ、要求に含まれるものが表になりました。

| 要求の中身 | `$.model.complete` | `$.model.fork` |
| - | - | - |
| モデル | 渡した `model` | セッションのモデル |
| システムプロンプト | 短い帰属のブロックの後に、渡せば自分の `system` | セッションのシステムプロンプト |
| メッセージ | 自分の `prompt` の 1 つのユーザーメッセージ | これまでの会話の後に、自分の `prompt` |
| CLAUDE.md などのプロジェクトの文脈 | 含まない | 会話の最後の要求と同じく含む |
| ツール | なし | Claude のツール（モデルは呼べない） |

fork は会話の最後の要求を繰り返すので、会話がまだキャッシュにある間は Claude API が大半をプロンプトキャッシュから返します。どちらもセッションの資格情報を使い、利用者のプラン・API キー・クラウドのプロバイダーに請求されます。

- **「Use prompt caching」**: `prompt` を文字列ではなく `{ text }` のブロックの配列で渡し、毎回同じ長い静的な内容の最後のブロックに `cache: true` を付けると、Claude Code はそのブロックを API の `cache_control` 付きで送ります。`system` も同じ配列の形を取れます。配列には Claude Code v2.1.292 以降が要り、それより前は `prompt` の配列を `takes { model, prompt } (host check)` で終わるエラーで断り、`system` の配列は要求から外します。例は、`/triage` のフックが長いラベル付けの規則 `RULES` の後に区切りを置き、毎回変わる `e.args` をその後に続けるものです
- **TTL と区切りの数**: キャッシュは最後に使ってから 5 分もちます。TTL は呼び出しではなく利用者の Claude Code の設定で決まり、1 時間にするには `subagentPromptCacheTtl` を `1h` にします。区切りは API が 4 つまで受け付け、5 つ目は `r.reason` の `api-error` で返ります
- **「Choose between `prompt` and `system`」**: Claude API に直接（API キーか Claude のサブスクリプションで）送るならどちらでもよく、Amazon Bedrock・Claude Platform on AWS・Agent Platform・Microsoft Foundry・LLM ゲートウェイを通すなら `prompt` に置きます。Claude Code はシステムプロンプトの先頭に、ユーザーメッセージの始まりから作る指紋を持つ帰属のブロックを置き、`api.anthropic.com` はキャッシュの前にそれを外しますが、ほかのエンドポイントはそのまま受け取るため、`system` の区切りは `prompt` の始まりが違うと外れうるからです。ほかの人が動かす mod でも `prompt` を使います
- **「Check for cache hits」**: 結果の `usage` の `cache_creation_input_tokens` と `cache_read_input_tokens` で確かめます。毎回書き込むだけで読まないなら、前置きが呼び出しごとに違うか、呼び出しの間隔が TTL より長いことを疑います。どちらも 0 のままなら、前置きがモデルの最小の長さより短い、`DISABLE_PROMPT_CACHING` の変数が効いている、ゲートウェイが `cache_control` を外している、ほかの mod がテキストの始まりを書き換えている、のどれかです
- **「What a `model.complete` hook receives」**: ほかの mod の要求を見るフックでは、`e.prompt` は常に文字列（配列ならブロックのテキストを順につないだもの）で、`e.promptBlocks` と `e.systemBlocks` に呼び出し元の配列が入ります。`next` に渡した文字列の始まりと一致する先頭のブロックは区切りごと保たれるので、`e.prompt + NOTE` のように末尾に足すなら区切りは残り、始まりを変えると外れます

- [mods API を使用する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/plugins/mods/api#use-prompt-caching)
- [Use the mods API - Claude Code Docs (English)](https://code.claude.com/docs/en/plugins/mods/api#use-prompt-caching)
- [mods API を使用する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/plugins/mods/api#call-a-model)
- [Use the mods API - Claude Code Docs (English)](https://code.claude.com/docs/en/plugins/mods/api#call-a-model)

## 5. Agent SDK で /usage の報告を構造化して受け取れるようになった

**`agent-sdk/typescript` の `SDKAssistantMessage` に `usage_report?: SDKUsageReport` が加わりました（Agent SDK v0.3.273 以降）。** `/usage` をプロンプトとして送ると、Claude Code は報告のテキストを `message.content` に持つアシスタントのメッセージを返し、次のすべてを満たすセッションでだけ、同じメッセージに構造化した写しを付けます。

- claude.ai の資格情報で認証している
- 資格情報が既知のプランの種類を示すか、`user:profile` のスコープを持つ
- アカウントが使用量に応じた請求ではない

`CLAUDE_CODE_OAUTH_TOKEN` に渡した `claude setup-token` のトークンは `user:inference` のスコープしか持たないので、既定では当てはまりません。API キーのセッションなどと以前の版はフィールドなしでテキストだけを返すので、フィールドがあれば読み、なければテキストに戻るよう求めています。

**新しい `SDKUsageReport` の型**は実験的で、形が変わりうるとされています。

- **`session`**: Claude Code の累計の費用と使用量（`total_cost_usd`・`total_api_duration_ms`・`total_duration_ms`・`total_lines_added`・`total_lines_removed` と、モデルごとの `ModelUsage` の `model_usage`）。`SDKResultMessage` の `total_cost_usd` と `modelUsage` と同じ記録から読み、`total_cost_usd` はトークンの数から手元で計算した見積もりで、プランの請求額ではありません
- **`rate_limits`**: プランの使用量の行の `limits` と、使用量クレジットの支出の `extra_usage`。セッションの OAuth トークンが `user:profile` のスコープを欠く場合など、プランの使用量を得られないときは `null` です
- **`limits` の各行**: `kind`（`session`・`weekly_all`・`weekly_scoped` など。行の分類はラベルではなくこれで行う）、`group`、`percent`（0〜100）、`resets_at`、`scope`（モデルか利用面）、`severity`（`normal`・`warning`・`critical` など）、`is_active`（1 つの値を示す表示に使う行で `true`）。行はサーバーが送ったとおりに描き、空の配列はメーターがないこと、`null` は報告する行がないことを示します。Agent SDK v0.3.277 より前は、`severity` と `is_active` が省略可能で `null` になりえました
- **`extra_usage`**: 請求期間の使用量クレジットの支出と上限で、金額は `currency` の補助単位（米ドルならセント）です。`monthly_limit` はそのアカウントに自分の上限がないとき `null` で、Team と Enterprise のプランでは `null` を無制限と表示しないよう求めています。`is_enabled` は使用量クレジットで要求を払えない間 `false` です

- [Agent SDK リファレンス - TypeScript - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/agent-sdk/typescript#sdkusagereport)
- [Agent SDK reference - TypeScript - Claude Code Docs (English)](https://code.claude.com/docs/en/agent-sdk/typescript#sdkusagereport)
- [Agent SDK リファレンス - TypeScript - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/agent-sdk/typescript#sdkassistantmessage)
- [Agent SDK reference - TypeScript - Claude Code Docs (English)](https://code.claude.com/docs/en/agent-sdk/typescript#sdkassistantmessage)

## 新規追加されたページ

<!-- light:new-pages:start -->
（今回の対象期間に新規追加・削除されたドキュメントページはありません。`llms.txt` は変わらず、収録 URL は 232 のままです。`llms-full.txt` に展開されている固有のページも 221 のままで、`Source:` の行が 229 あり 8 ページが 2 回展開されている状態も前回と同じです）
<!-- light:new-pages:end -->

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
- [**Troubleshoot installation and login**](#1-troubleshoot-installation-and-login) ([日本語](https://code.claude.com/docs/ja/troubleshoot-install#verify-your-path) / [English](https://code.claude.com/docs/en/troubleshoot-install#verify-your-path)):  
  180 行（追加 167・削除 13）が変わりました。PATH の確かめ方が書き足され、エラーの早見表に 9 行が加わり、`errors` からインストールのエラーの 2 節が移ってきました
- [**Deploy self-hosted environments to production**](#2-deploy-self-hosted-environments-to-production) ([日本語](https://code.claude.com/docs/ja/self-hosted-environments-deploy#harden-your-deployment) / [English](https://code.claude.com/docs/en/self-hosted-environments-deploy#harden-your-deployment)):  
  143 行（追加 125・削除 18）が変わりました。大半は git proxy（ハイライト 3）で、ほかにホストの GitHub の資格情報の扱い、IP の許可リスト、オンデマンドのランナーの更新のしかたなどが改められました
- [**Customize sessions in self-hosted environments**](#3-customize-sessions-in-self-hosted-environments) ([日本語](https://code.claude.com/docs/ja/self-hosted-environments-configuration#keep-transient-failures-retryable-in-a-shell-hook) / [English](https://code.claude.com/docs/en/self-hosted-environments-configuration#keep-transient-failures-retryable-in-a-shell-hook)):  
  142 行（追加 117・削除 25）が変わりました。Slack のスレッドの環境変数、`spawn-runner` のフックで一時的な失敗を再試行可能に保つ書き方、最初のターンの前の MCP サーバーの待ち方などが加わりました
- [**Hooks reference**](#4-hooks-reference) ([日本語](https://code.claude.com/docs/ja/hooks#exit-code-output) / [English](https://code.claude.com/docs/en/hooks#exit-code-output)):  
  130 行（追加 103・削除 27）が変わりました。ほぼすべてがハイライト 1 の `onFailure` と終了コードの説明の書き直しです
- [**Agent SDK reference - TypeScript**](#5-agent-sdk-reference---typescript) ([日本語](https://code.claude.com/docs/ja/agent-sdk/typescript#sdktasknotificationmessage) / [English](https://code.claude.com/docs/en/agent-sdk/typescript#sdktasknotificationmessage)):  
  110 行（追加 100・削除 10）が変わりました。`SDKUsageReport`（ハイライト 5）のほか、タスクの通知の `reason`、貼り付けの項目の上限などが加わりました
- [**Error reference**](#6-error-reference) ([日本語](https://code.claude.com/docs/ja/errors#claude-code-couldnt-restart) / [English](https://code.claude.com/docs/en/errors#claude-code-couldnt-restart)):  
  102 行（追加 48・削除 54）が変わりました。インストールのエラーの節を `troubleshoot-install` へ移し、再起動の失敗と `/loop` の wakeup の取りこぼしの節が加わりました
- [**Use the mods API**](#7-use-the-mods-api) ([日本語](https://code.claude.com/docs/ja/plugins/mods/api#what-a-model-complete-hook-receives) / [English](https://code.claude.com/docs/en/plugins/mods/api#what-a-model-complete-hook-receives)):  
  91 行（追加 86・削除 5）が変わりました。すべて「Call a model」の書き直し（ハイライト 4）です
- [**Claude apps gateway configuration**](#8-claude-apps-gateway-configuration) ([日本語](https://code.claude.com/docs/ja/claude-apps-gateway-config#group-changes-during-an-open-session) / [English](https://code.claude.com/docs/en/claude-apps-gateway-config#group-changes-during-an-open-session)):  
  80 行（追加 75・削除 5）が変わりました。`code` キー（ハイライト 2）のほか、開いたセッションの間にグループが変わったときのテレメトリーの節が加わりました
- [**Troubleshoot plugins**](#9-troubleshoot-plugins) ([日本語](https://code.claude.com/docs/ja/plugins/troubleshooting#plugin-directory-does-not-exist) / [English](https://code.claude.com/docs/en/plugins/troubleshooting#plugin-directory-does-not-exist)):  
  64 行（追加 63・削除 1）が変わりました。マーケットプレイスの名前、読み込まれない設定ファイル、Windows でのアンインストール、`Plugin directory does not exist` の 4 節が加わりました
<!-- light:updated-pages:end -->

`llms-full.txt` から切り出したページ単位の差分（`git diff --no-index --numstat`）が 50 行以上の既存ページを挙げています。changelog（93 行）は、これまでどおり「軽微な更新」で扱います。次点は `self-hosted-environments-quickstart` の 46 行、`chrome` の 44 行、`remote-control` の 33 行で、いずれも「軽微な更新」で扱います。`troubleshoot-install` と `errors` の行数には、「Installation errors」の 2 節が `errors` から `troubleshoot-install` へ移った分が両方に数えられています。

## 1. Troubleshoot installation and login

- **エラーの早見表**: 9 行が加わりました。インストーラーが PATH にないと報告する `Native installation exists but ... is not in your PATH`、`where.exe claude` の `INFO: Could not find files for the given pattern(s).`、シェルの設定ファイルへの `permission denied`、CMD の `< was unexpected at this time`、PowerShell の `The term 'System.Xml.XmlDocument' is not recognized`、`CRYPT_E_NO_REVOCATION_CHECK` と `CRYPT_E_REVOCATION_OFFLINE`、更新のダウンロードの切断と時間切れ、`Cask 'claude-code@latest' is not installed`、それに `Killed` の行から分けた `Installation was killed before it could finish` です
- **「Verify your PATH」**: インストーラーがこの場合を `Setup notes:` の下に報告する（直し方を示すが PATH は自分では変えない）ことが加わり、各タブ（macOS/Linux・Windows PowerShell・Windows CMD）で、まずプログラムがあるか（`ls -la ~/.local/bin/claude`・`Test-Path`・`dir`）を確かめてから PATH を見る手順になりました。`echo` は新しい端末のために設定を保存し `source` は今の窓に適用する、という説明と、それでも `claude` が見つからないときの原因（開いていた端末やエディターの中の端末が古い PATH のまま、行が保存されていない、別のシェルのファイルに書いた）も加わっています
- **新しい節**: 「`permission denied` when adding to your PATH」（`ls -l` で所有者を見て、別のユーザーなら `sudo chown $(whoami) ~/.zshrc`、自分なら `chmod u+w ~/.zshrc`）と、「`Cask 'claude-code@latest' is not installed`」（`brew list --cask | grep claude-code` で入っている方の cask を確かめて上げる）ができました
- **HTML が返るとき**: PowerShell で `irm` が応答を XML として解析し、`iex` が `System.Xml.XmlDocument` という型の名前を実行しようとする場合と、CMD で `< was unexpected at this time.` の後にページの HTML が続く場合が加わりました。解決策は「数分待って再試行」が先になり、Homebrew と WinGet のインストールは既定で自分を更新しない、と加わっています
- **TLS**: `CRYPT_E_NO_REVOCATION_CHECK` と `CRYPT_E_REVOCATION_OFFLINE` は手順 4 へ進むよう案内し、TLS 1.2 を有効にする手順は Windows PowerShell 5.1 のものと明記され、その後に同じ窓でインストーラーを動かす手順が分けられました
- **`errors` から移った節**: 「Installation was killed before it could finish」と「The connection dropped while downloading the update」が、本文を変えずにこのページへ移りました
- 「Check for conflicting installations」にも、`claude` が PATH に見つからないときに、ネイティブのインストールがあるか（なければインストールし、あれば PATH を直す）を見分ける説明が加わりました

- [インストールとログインのトラブルシューティング - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/troubleshoot-install#verify-your-path)
- [Troubleshoot installation and login - Claude Code Docs (English)](https://code.claude.com/docs/en/troubleshoot-install#verify-your-path)

## 2. Deploy self-hosted environments to production

git proxy の書き直しはハイライト 3 のとおりです。このほか次の変更がありました。

- **ホストの GitHub の資格情報**: 「Harden your deployment」に、セッションが読める GitHub の資格情報は何でも Claude が使えるので、ランナーのホスト自身の広い範囲の資格情報（個人用アクセストークン、`gh auth login` が保存するトークン、ランナーの環境の `GH_TOKEN`）をセッションが読める場所に置かない、という項目が加わりました。Anthropic-managed git ではそうした資格情報があると Claude が git proxy を通らずに直接 GitHub に届き、使わない場合はクローンの資格情報を狭く絞ればイメージに残せます。最初のクローンに `--use-anthropic-git-proxy` を使えるのは、セッションのリポジトリがすべて github.com にあるとき、とも改められています
- **IP の許可リスト**: 「組織の IP の許可リストは既定ではセルフホストのランナーの通信を対象にしない」という注記が、「IP の許可リストを有効にしている組織は、起動の前にランナーとセッションのコンテナーの公開の送信元のアドレス（オンデマンドのランナーならオーケストレーターのホストも）を加える」に替わりました。許可リストをランナーの通信の制御として頼らないこと、という点は変わりません
- **ネットワークの要件**: 許可リストに要らないホストと、`claude.ai` に届くホスト側の流れ（ワンラインのインストーラー、対話の `claude auth login`）が箇条書きになり、サインインのブラウザーが `hcaptcha.com`・`*.hcaptcha.com`・`challenges.cloudflare.com` からブラウザーの確認を読み込むことが加わりました
- **コミットの帰属**: `--configure-git` の有無によらず、Claude はコミットのメッセージを `Claude-Session: <url>` の行で、プルリクエストの説明をセッションの URL で終えるよう指示され、両方を省くにはランナーのホストの `~/.claude/settings.json` で `attribution.sessionUrl` を `false` にしてランナーを再起動する、と加わりました。`core.hooksPath` を既に設定したイメージでランナーがフックを入れない扱いも、Anthropic-managed git を使わない場合に限る、と改められています
- **版の更新**: 固定のランナーは changelog を読んでから入れ替えて再起動し、オンデマンドのランナーは `spawn-runner` のフックが起動するイメージを変える（動いているランナーは作業指示が 1 回限りなので再起動しない）、と分かれました
- **そのほか**: 例の Dockerfile に `jq` が加わり、`--capacity` が 2 以上のときは事前に温めたクローンからセッションごとに worktree を切り出す（ダウンロードは省けるがチェックアウトは省けない）、`--push-outcome-on-release` は環境のすべてのランナーに付ける（`checkout` のフックのリポジトリはプッシュしない）、と加わりました。連絡が途絶えて環境から外されたランナーは再接続すると終了し（ログに `runner record gone server-side` か `poll auth failed`）、自分では登録し直さないので再起動する、という項目も「When the runner exits」に加わっています

- [本番環境へのセルフホスト環境のデプロイ - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/self-hosted-environments-deploy#harden-your-deployment)
- [Deploy self-hosted environments to production - Claude Code Docs (English)](https://code.claude.com/docs/en/self-hosted-environments-deploy#harden-your-deployment)

## 3. Customize sessions in self-hosted environments

- **Slack のスレッドの変数**: ラッパーの環境に、1 つの Slack のスレッドに属する Claude Tag のセッションでそのスレッドのリンクを持つ `CLAUDE_CODE_REMOTE_SLACK_THREAD_URL` と、スレッドのタイムスタンプ（`1700000000.000100` など）を持つ `CLAUDE_CODE_REMOTE_SLACK_THREAD_TS` が加わりました。どちらも未設定のことがあり、ラッパーか `command` のフックと、セッションが動かすもの（シェルのコマンド・git のフック・Claude Code のフック）に届き、`checkout`・`post-session`・`spawn-runner` のフックには届きません
- **「Give a default to variables that can be unset」**: `CCR_SESSION_ACCOUNT_EMAIL`（組織のサービスの ID が作るセッションなどで未設定）・`CLAUDE_RUNNER_CLIENT_PLATFORM` と Slack の 2 つの変数は、`set -u` のスクリプトでは `${CCR_SESSION_ACCOUNT_EMAIL:-}` のように既定値付きで展開します。Slack のリンクは `?` や `&` を含みうるので引用符で囲み、`eval` や `sh -c` の文字列に値を埋め込まず変数を参照させます
- **標準エラー**: ラッパーか子が 0 以外で終わると、ランナーは標準エラーの最後の行をセッションに投稿して自分のログにも出すので、秘密を標準エラーに出さず、デプロイ前に `set -x` を外すよう加わりました。標準出力はリダイレクトしてよく、標準エラーをリダイレクトすると、ランナーは終了コードだけで失敗を報告します
- **`checkout` のフック**: `CLAUDE_RUNNER_REPO_REF` は `refs/pull/<number>/head` のような完全な参照名もありうる、と加わり、資格情報の得方（「Get git credentials in the hook」。発行する資格情報は `act.sub` で結びつけ、`act.email` を必須にしない）と失敗したとき（「When the hook fails」）が小見出しに分かれました
- **`post-session` のフック**: `completed` と `interrupted` の説明に、アーカイブか削除の後の終了の扱いが加わり、例のスクリプトに git を HTTPS・HTTP・SSH のリモートに限る `GIT_ALLOW_PROTOCOL` の行が加わりました
- **`spawn-runner` のフック**: `CLAUDE_RUNNER_ATTEMPT` は再試行や要求の回数ではなく、ログに使うセッションごとのカウンター、とされました。終了コード 2 以上で止まったセッションは、利用者が新しいメッセージを送るか Owner が **Retry** を選ぶまで止まり、`--expected-spawn-seconds` はプラットフォームの容量の待ちを含めた、スポーンの要求からランナーの登録までの p99 にする、と改められました
- **「Keep transient failures retryable in a shell hook」**: `set -e` のシェルのフックは失敗したコマンド自身の終了コード（コマンドがないときの `127`、`curl --fail` の HTTP のエラーの `22` など）で終わるので、再試行で直る失敗でもセッションを止めてしまいます。`#!` の直下に置く `set -e`・`permanent()` の関数・`EXIT` の `trap` の 3 行でそうした失敗を終了コード 1 に変える例と、加えた後に見直すべき書き方（素の `exit 2`、`exec`、2 つ目の `EXIT` の trap、失敗してよいコマンド）、`no-such-command` を呼ぶ行を足して `echo $?` が `1` になるか確かめる方法が載りました
- **「Wait for MCP servers before the first turn」**: セルフホストのセッションは、起動時に `alwaysLoad: true` の HTTP・SSE のサーバー（`MCP_CONNECTION_NONBLOCKING=0` ならすべて）を既定で 5 秒まで（`MCP_CONNECT_TIMEOUT_MS` で変更）、最初のターンで接続中の stdio のサーバーを 2 秒まで待ちます。`CLAUDE_CODE_MCP_STARTUP_WAIT_MS` は後者の長さだけを変え、`alwaysLoad` は `claude mcp add-json` で設定します。`cli-reference`・`headless`・`env-vars` からも、セルフホストの環境では短い待ちが代わりに効く、と案内が加わりました
- **アカウントのスキル**: 人が自分で始めたセッションには claude.ai のアカウントで有効にしたスキルが設定のディレクトリにダウンロードされますが、ルーティンの実行と、Bedrock・Agent Platform にモデルの要求を送るセッションには届かない、と加わりました（`skills`・`cloud-environments` からも案内）。Bedrock・Agent Platform のセッションのモデルの選び方の説明も箇条書きに組み替わっています

- [セルフホストされた環境でセッションをカスタマイズする - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/self-hosted-environments-configuration#keep-transient-failures-retryable-in-a-shell-hook)
- [Customize sessions in self-hosted environments - Claude Code Docs (English)](https://code.claude.com/docs/en/self-hosted-environments-configuration#keep-transient-failures-retryable-in-a-shell-hook)

## 4. Hooks reference

`onFailure` と「Exit code output」の書き直しはハイライト 1 のとおりです。このほか、`PermissionRequest` のフックで要求を許可・拒否するには `decision` のオブジェクトを返す、`TaskCreated` のフックは終了コード 2 か JSON の判断で作成を止められる、`PreModelSwitch` 以外のイベントの時間切れは「Timeouts」を見る、`PreModelSwitch` で 0 と 2 以外の終了コードで判断を出さないフックは止めない失敗、という言い回しの整理がありました。

- [Hooks リファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/hooks#exit-code-output)
- [Hooks reference - Claude Code Docs (English)](https://code.claude.com/docs/en/hooks#exit-code-output)

## 5. Agent SDK reference - TypeScript

`usage_report` と `SDKUsageReport` はハイライト 5 のとおりです。このほか次の変更がありました。

- **タスクの通知の `reason`**: `SDKTaskNotificationMessage` に `reason?: "worker_restart"` が加わりました（Agent SDK v0.3.273 以降）。タスクが自身の完了・失敗・停止以外の原因で終わったときに付き、claude.ai を通してつなぐセッション（セルフホストのランナーを含むクラウドのセッションと Remote Control のセッション）だけで設定され、ローカルの `query()` では付きません。`worker_restart` はタスクを動かしていた Claude Code のプロセスが再起動したことを示し、状態は `"stopped"` なので、完了とも失敗とも扱わないよう求めています
- **貼り付けの上限**: `pasted_content` はエントリとその中のコンテンツブロックが 1,000 を超えるとフィールド全体を無視し、`inline_pastes` は空でない最初の 100 エントリだけを使います
- **再開したターン**: `resume_reason` などの説明が、再起動で中断したターンを「再実行する」から「続ける」という書き方に改められました（値の説明からも「なぜ再実行したか」が外れた）
- **そのほか**: Workflow ツールの `scriptPath` は、前の実行が返した `scriptPath` などのパスで、セッションのツールに `Read` がなければエラーで断る、と改められました。`CLAUDE_CODE_MAX_RETRIES` の説明からは最悪の経過時間の目安（`API_TIMEOUT_MS × (CLAUDE_CODE_MAX_RETRIES + 1)`）の文が外れています（`agent-sdk/python` も同じ）

- [Agent SDK リファレンス - TypeScript - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/agent-sdk/typescript#sdktasknotificationmessage)
- [Agent SDK reference - TypeScript - Claude Code Docs (English)](https://code.claude.com/docs/en/agent-sdk/typescript#sdktasknotificationmessage)

## 6. Error reference

- **インストールのエラーの移動**: 「Installation errors」の節（「Installation was killed before it could finish」と「The connection dropped while downloading the update」）がなくなり、`troubleshoot-install` へ移りました。早見表の 3 行もそちらを指し、`troubleshooting` の案内も改められています
- **「Claude Code couldn't restart」**: `/tui` で全画面の描画に切り替えるときなどの再起動で、セッションを閉じたのに新しいプロセスを始められなかったとき、`Claude Code couldn't restart. Your conversation is saved. Start Claude Code again and run /resume to pick it up.` を出して終了コード 1 で終わります（開き直す会話がないときは `Claude Code couldn't restart. Start Claude Code again.`）。同じディレクトリで `claude` を動かして `/resume` で選び、繰り返し失敗するなら `claude --debug-file claude-debug.log` で始めると、`Failed to relaunch:` の行に OS のエラーが残ります
- **「This session restarted after its next /loop wakeup was due」**: バックグラウンドのセッションの自分のペースの `/loop` で、次の wakeup を待つ間にプロセスが終わり、次のプロセスが始まる前に wakeup の時刻が過ぎると、ループは止まり、その wakeup は遅れても発火しません。通知はどれだけ遅れたかを示し（v2.1.295 より前は通知なしに止まった）、続けるにはセッションに返信してそう伝えます
- **早見表**: このほか、`Cannot add marketplace "<name>": ...`・`does not load (...), so Claude Code ignores the whole file`・`Plugin directory does not exist: <path>`（いずれも `plugins/troubleshooting` の新しい節）の行が加わりました
- **worktree の隔離**: Bash と Monitor に加え PowerShell のコマンドも対象と明記され、コマンドがメインのチェックアウトか別の worktree で動く場合（メッセージは `resolved to the shared checkout` か `is in a different worktree`）が理由に加わりました
- **保存されたトランスクリプトがないセッション**: 別の会話からバックグラウンドに移し、自分のターンを 1 つも動かさずに止まったセッションを開くと、Claude Code はその会話を再開し、会話が見つからないときだけ断る、と書き直されました（`agent-view` も同じ）。元の会話は無傷なので `claude --resume` で再開する、という案内は外れています
- **再試行**: 「Tune retry behavior」の表に `CLAUDE_CODE_RETRY_WATCHDOG_MAX_WAIT_MS`（`CLAUDE_CODE_RETRY_WATCHDOG` を設定したとき、各 API リクエストが 429 と 529 のエラーを待つ最大の時間。未設定なら無制限。v2.1.295 以降）が加わり、止まった応答のストリームは「10 回の予算の外で 1 回だけ要求をし直す」から「1 回だけストリームし直す」になりました

- [エラーリファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/errors#claude-code-couldnt-restart)
- [Error reference - Claude Code Docs (English)](https://code.claude.com/docs/en/errors#claude-code-couldnt-restart)

## 7. Use the mods API

「Call a model」の書き直しはハイライト 4 のとおりで、このページの変更はこれだけです。`$.model.complete` の基本の使い方を述べる「Send one prompt」、キャッシュの「Use prompt caching」とその下の 2 つの小見出し、フックが受け取るものを述べる「What a `model.complete` hook receives」の 5 つの見出しが加わりました。API の失敗では呼び出しが拒否されずに `r.isAnswered` が `false` になる、という説明は「Send one prompt」に移っています。

- [mods API を使用する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/plugins/mods/api#what-a-model-complete-hook-receives)
- [Use the mods API - Claude Code Docs (English)](https://code.claude.com/docs/en/plugins/mods/api#what-a-model-complete-hook-receives)

## 8. Claude apps gateway configuration

`code` キーはハイライト 2 のとおりです。このほか、**「Group changes during an open session」の節**ができました。端末のセッションは `user.groups` を OTLP のリソースと、各メトリクスのデータポイント・イベントの両方に載せます。開いたセッションの間に開発者のグループが変わると、次のサイレントな更新の後の使用量のデータポイントとイベントは新しいグループを持つ一方、リソースは Claude Code を再起動するまで古いグループのままなので、データポイントかイベントの属性でグループ化するよう求めています。OpenTelemetry Collector の Prometheus remote write exporter で `resource_to_telemetry_conversion` をオンにすると、各データポイントの `user.groups` がリソースの値で置き換わるため、その exporter の前で `resource` プロセッサー（`resource/drop-user-groups`）を使ってリソースから `user.groups` を消す例が載りました。テレメトリーの節からもこの節へ案内が加わっています。

- [Claude apps gateway 設定 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/claude-apps-gateway-config#group-changes-during-an-open-session)
- [Claude apps gateway configuration - Claude Code Docs (English)](https://code.claude.com/docs/en/claude-apps-gateway-config#group-changes-during-an-open-session)

## 9. Troubleshoot plugins

- **「`Cannot add marketplace "<name>": Claude Code cannot install plugins from a marketplace with this name`」**: `marketplace.json` の `name` がプラグイン ID の `@` の後の部分として使えない（例は `_` で始まる `_internal`）と、追加を断って何も登録しません。持ち主なら `internal-tools` などに直し、ほかの人のものなら持ち主に頼みます（v2.1.295 より前は成功と報告した）。`plugins/marketplace-reference` の `name` の説明からも案内が加わりました
- **「`does not load (...), so Claude Code ignores the whole file`」**: `claude plugin install`・`enable`・`disable`・`claude plugin marketplace add` の成功の行の後に出る警告で、コマンド自体は動いたものの、名前の挙がった設定ファイルに誤りがあり、コマンドが書いた内容も含めてファイル全体が無視されます。括弧の中は `its "<key>" is not valid` か `it is not a JSON object` です
- **「A plugin stays installed after `plugin uninstall` on Windows」**: プロジェクトかローカルのスコープでアンインストールが成功しても一覧に残るのは、`installed_plugins.json` に同じフォルダーのパスを違う綴り（`c:\work\app` と `C:\work\app` など）で書いた 2 つの記録があるためで、同じフォルダーから同じ `--scope` でもう一度実行します（v2.1.295 より前は 2 回目が失敗するので、`claude update` してから）
- **「`Plugin directory does not exist: <path>`」**: セッションがフックを読み込んだディレクトリがディスクから消えたときに出るもので、メッセージは再インストールを勧めますが、まず `/reload-plugins` を実行し、その出力（`Reloaded:` だけ・`N errors during load. Run /plugin for details.`・`Run /reload-plugins --force to apply.`）で結果を確かめます。失敗の表示はフックのイベントとコマンドごとにセッションで 1 回なので、静かになっても直ったとは限りません
- **検証**: `claude plugin validate` は、プラグインとマーケットプレイスの両方のマニフェストを持つディレクトリでは両方を読みます（v2.1.289 より前はマーケットプレイスとしてだけ検証した）

- [プラグインのトラブルシューティング - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/plugins/troubleshooting#plugin-directory-does-not-exist)
- [Troubleshoot plugins - Claude Code Docs (English)](https://code.claude.com/docs/en/plugins/troubleshooting#plugin-directory-does-not-exist)

## 軽微な更新

<!-- light:minor-updates:start -->
今回の差分は **2 ファイル**（`llms-full.txt` と見出しマップ）で、`llms.txt` は変わっていません。`llms-full.txt` の生の差分は追加 1,458 行・削除 299 行で、ページ単位に切り出して数えると 221 ページ中 **58 ページ**が変わり、変更は 1,677 行（追加 1,383・削除 294）、うち changelog が 93 行、ほかのページが 1,584 行（追加 1,290・削除 294）でした。生の差分との差（追加 75・削除 5）は、2 回展開されている `plugins/troubleshooting`・`plugins/create`・`plugins/install` の変更が 2 度数えられたぶんです。大幅更新の 9 ページを除く **49 ページ**（changelog を含む）と、changelog に加わった **v2.1.296**（2026年10月09日、79 項目。Added 8・Changed 6・Improved 9・Fixed 56）を以下にまとめます。changelog の項目はすべて v2.1.296 のものです。`llms-full.txt` の総行数は **119,210 行から 120,369 行へ 1,159 行増え**ました（changelog の 93 行、ほかのページの 996 行、2 回展開された 3 ページの重複の 70 行）。

**新機能**

- Claude apps gateway の `managed.policies[]` に `code` キーを追加（詳細はハイライト 2 参照）
- サブエージェントの frontmatter と `--agents` の定義に `autoCompactWindow` を追加。サブエージェントが本体の会話のウィンドウより早く自動圧縮できます
- `CLAUDE_CODE_WORKFLOW_SUBAGENT_MODEL` を追加。ほかのサブエージェントのモデルはそのままで、すべてのワークフローのエージェントを 1 つのモデルで動かします
- 過負荷（529）の要求を再試行するときのバックオフの最大の待ち時間を長くする環境変数 `CLAUDE_CODE_OVERLOADED_RETRY_MAX_DELAY_MS` を追加
- 有効な別のプラグインが同じ名前を持つためにフックが外されたプラグインに、`/plugin` で注記を出すようにした
- Read ツールに `allow_large` の選択肢を追加。ファイル全体が要りコンテキストに余裕があるとき、Claude が通常の大きさの上限を超えるテキストファイルを 1 回で読めます
- [Cloud sessions] 管理設定のセルフホストの環境の Activity タブの Sessions と Runners の一覧に、状態の絞り込みを追加（複数の状態を同時に選べる）
- [Claude Tag] Claude Tag Admin の権限を持つメンバーが、Activity のページの Memory タブでワークスペースとチャンネルのメモリーのファイルを作成・編集・削除できるようにした
- **プロジェクトの設定では Chrome をオンにできないと載った**（`chrome` の「Project settings can't turn on Chrome」）。プロジェクトの `.claude/settings.json` か `.claude/settings.local.json` の `env` で `CLAUDE_CODE_ENABLE_CFC` を `1` にしても Claude Code は適用せず、`Claude Code ignored CLAUDE_CODE_ENABLE_CFC in this project's settings` の警告を出します。チェックアウトしたリポジトリが Claude をブラウザーにつなげてはならないためで、今すぐ使うなら `claude --chrome` で始め直し、以後のセッションなら `/chrome` で **Enabled by default** を選び、警告だけ消すならその行を外します。`env-vars` にも `CLAUDE_CODE_ENABLE_CFC`（`1` で Chrome の連携をオンに、`0` でオフにして始める。`claudeInChromeDefaultEnabled` より優先し、`--chrome`・`--no-chrome` が両方より優先）が載りました。同じページには、拡張機能が Claude Code と別の claude.ai の組織にサインインしていると「Browser extension is not connected」になる節（`/status` の `Organization` の行で確かめ、拡張機能でログアウトして選び直す。ログアウトすると拡張機能に保存したショートカットと予定のタスクを失う）、資格情報が置かれる名前（`.env`、`.pem` や `.key` のファイル、`.ssh` の下）のファイルのアップロードを断ること（v2.1.293 以降）、`/chrome` の `Status` が「Not connected」なら「Reconnect extension」で接続をやり直せること（v2.1.290 以降）も加わりました — [日本語](https://code.claude.com/docs/ja/chrome#project-settings-can’t-turn-on-chrome) / [English](https://code.claude.com/docs/en/chrome#project-settings-can’t-turn-on-chrome)
- **Remote Control のセッションでコネクタを認可し直す手順が載った**（`remote-control` の「Authorize a connector again from your shell」）。モバイルアプリやウェブからは `/mcp` のパネルが使えないので、セッションが動くマシンの端末で `claude mcp login "claude.ai Slack" --no-browser` のようにコネクタの名前を引用符で囲んで実行し、表示される claude.ai のリンクを使っている機器で開いて認可します。その後に始めたセッションはそのままつながり、動いているセッションでは `/mcp reconnect claude.ai Slack` を実行します（モバイルアプリやウェブから送った `!` で始まる行はシェルでは動かない）。`/mcp` の `reconnect`・`enable`・`disable` はセッションが対話の端末で動くときに使える、と改められ、`cli-reference`・`mcp` の `claude mcp login` の説明からも案内が加わりました — [日本語](https://code.claude.com/docs/ja/remote-control#authorize-a-connector-again-from-your-shell) / [English](https://code.claude.com/docs/en/remote-control#authorize-a-connector-again-from-your-shell)
- **途中で切れたストリームの扱いが載った**（`agent-sdk/streaming-output` の「Handle a stream that's cut off」）。ターンの中断や接続の切断でストリームがメッセージの途中で切れても、ターンが終わる前にそのメッセージの `message_stop` が届き、切れたテキストか思考のブロックには `content_block_stop` も届きます。切れたツールの呼び出しには届かないので、そのブロックが開いたまま `message_stop` が来たら入力は不完全とみなします。Claude Code v2.1.290 より前は `message_stop` なしにターンが終わりえたので、応答が進行中のまま表示され続けるなら SDK を更新します（TypeScript Agent SDK は v0.3.290 から、Python Agent SDK は v0.2.164 から v2.1.290 以降を同梱） — [日本語](https://code.claude.com/docs/ja/agent-sdk/streaming-output#handle-a-stream-that’s-cut-off) / [English](https://code.claude.com/docs/en/agent-sdk/streaming-output#handle-a-stream-that’s-cut-off)
- **セルフホストのランナーで、外から届く auto モードの規則の一覧を選べるようになった**（`self-hosted-environments-reference` の「Auto mode rule lists」）。`--server-auto-mode-lists`（`SELF_HOSTED_RUNNER_SERVER_AUTO_MODE_LISTS`）は、コントロールプレーンがセッションと一緒に送る分類器の規則の一覧（`environment`・`soft_deny`・`allow`）のどれをセッションに届けるかを決め、既定の `no-allow` は `allow` を除く 2 つを、`all` はすべてを届け、`none` はどれも届けません（不正な値ではランナーが起動しない。v2.1.295 以降）。サーバーが一覧の適用を求めなければ設定によらず届かず、`--log-level debug` で求めたかどうかを確かめられます。環境変数だけの設定に `CLAUDE_RUNNER_FETCH_SERVER_PROGRESS_CAP_MS`（git のサーバーの進捗が増えている間、取得が最初のデータを試行ごとに待つ時間。既定 600000、`0` か `off` で止め、ほかの値は 120000〜1800000 に丸める。v2.1.295 以降）も加わり、`--startup-timeout-min` にはクローンの時間を数えないことが加わりました — [日本語](https://code.claude.com/docs/ja/self-hosted-environments-reference#auto-mode-rule-lists) / [English](https://code.claude.com/docs/en/self-hosted-environments-reference#auto-mode-rule-lists)
- **`claude -p` がバックグラウンドの作業を待つ間に標準エラーへ行を出すと載った**（`headless` の「Background tasks at exit」）。標準エラーが端末で 5 秒待つと、`Waiting for background work to finish` で始まり待っている作業を挙げる行を出します。`json` か `stream-json` の出力では標準出力が端末でないときだけ出るので、スクリプトが読む JSON には入りません。バックグラウンドの作業が別のターンを始めると、既定の `text` の出力は各ターンの結果を、`json` は最後のターンの結果を出す（v2.1.295 より前は `text` も最後だけ）、とも加わりました。`goal` も、非対話の実行では最後の応答がループの終わりに出る、と改められています — [日本語](https://code.claude.com/docs/ja/headless#background-tasks-at-exit) / [English](https://code.claude.com/docs/en/headless#background-tasks-at-exit)
- **VS Code の拡張機能に、Claude が送ったファイルの行と `spinnerVerbs` が載った**（`vs-code`）。Remote Control につながったセッションで Claude が `SendUserFile` ツールでファイルを送ると、会話に **Sent report.md, chart.png** のような行が出て、ファイル名をクリックするとエディターで開きます。拡張機能の設定の表には、ターンの間にスピナーが巡る動詞を CLI の `spinnerVerbs` と同じ `mode` と `verbs` で決める `spinnerVerbs` が加わりました（v2.1.296 の修正と対応） — [日本語](https://code.claude.com/docs/ja/vs-code#extension-settings) / [English](https://code.claude.com/docs/en/vs-code#extension-settings)
- **mod の `tool.call` で、ツールが動いた後に結果を Claude から隠せると載った**（`plugins/mods/events` の「Guard or change a tool call」）。`await next(e)` の後に `{ deny: reason }` を返すと、Claude は `next` が返したものの代わりに理由を読み、ツールが動いて成功していれば、理由の前に `Bash ran, and a plugin withheld its result:` のような注記が付きます（ツールがしたことは取り消さない）。組み込みのツールの呼び出しに自分で答えるなら、`result` をそのツール自身の結果の形にする、とも加わりました。`prompt.submit` で `drop` を返すとテキストは入力欄に戻り、利用者には `Prompt dropped by a hook:` と理由が見えるので理由は利用者に向けて書く、書き換えたプロンプトはプロンプトの履歴にも出る、と改められています — [日本語](https://code.claude.com/docs/ja/plugins/mods/events#guard-or-change-a-tool-call) / [English](https://code.claude.com/docs/en/plugins/mods/events#guard-or-change-a-tool-call)
- **`headersHelper` のコマンドを VS Code の拡張機能でも受け入れられると載った**（`plugins/host-marketplace`）。プラグインを単独で入れる・更新するときのコマンドの承認は、端末のセッションの `/plugin`、シェルの `claude plugin install`・`update` に加え、VS Code の拡張機能の **Manage plugins** のダイアログ（拡張機能 2.1.290 以降）でもできます。表示したコマンドと URL が変わると断る規則の、クエリ文字列だけの変更は数えないという例外は、VS Code の拡張機能と `--accept-command` には当てはまりません — [日本語](https://code.claude.com/docs/ja/plugins/host-marketplace#how-users-accept-a-headershelper-command) / [English](https://code.claude.com/docs/en/plugins/host-marketplace#how-users-accept-a-headershelper-command)

**機能改善**

- 全画面モードで、マウスのポインターの下のリンクに下線を引き、開けることを示すようにした
- コードの多い会話で、構文の色付けをしたコードブロックをキャッシュし、トランスクリプトの切り替え（ctrl+o）の反応を速くした
- Claude apps gateway の後ろのデスクトップアプリの Code タブで、セッションを始められないとき（ゲートウェイの `code` の設定の準備がないマシンを含む）に、理由を返信として示すようにした（詳細はハイライト 2 参照）
- 断られたクラウドのセッションのエラーで、組織の方針を読み込めなかった理由と、claude.ai のログインより優先される API キーか認証トークンの名前を示すようにした
- `--debug` の出力で、カスタムのエージェントのファイルの認識できない frontmatter の項目を名指しし、ありそうな打ち間違いの助言を出すようにした
- auto モードで、auto モードの確認が使える答えを得られずに動かさなかったツールの呼び出しを、赤いエラーではなく薄い「Not run」の行で示すようにした
- フックの `--debug` の出力で、ツールの呼び出し・プロンプト・SessionStart・Stop の command のフックが終わったときにコマンド・プラグイン・結果・所要時間を記録し、遅いフックを見つけられるようにした
- `CLAUDE_CODE_TRANSCRIPT_LOCAL_GC` で、大きなトランスクリプトのファイルを書き直しても 10% 未満しか空かない場合は書き直さないようにした
- [Code Review] Code Review の管理設定で、設定を保存できなかった理由（方針による制限など）を、汎用の失敗のメッセージの代わりに示すようにした
- **ホットリロードを有効にするかの質問が出なくなる場合と、hooks モジュールの入れ子の上限が載った**（`plugins/mods/troubleshoot`・`plugins/mods/reference`）。質問が答えを選ばれないまま 3 回終わるとホットリロードはオフのままになり（`askUserQuestionTimeout` で時間切れになる場合など。自分で閉じたものは数えない）、mod を動かすにはそのディレクトリを mods のフォルダーの外へ写し、`--plugin-dir` で新しいセッションを始めます。hooks モジュールの 1 つのファイルで関数・ブロック・ループなどのスコープを入れ子にできるのは 2,000 段までで、超えると `code nested too deep to scan: more than 2000 scopes` で読み込まれません（`claude plugin validate` も同じ理由を報告）。`tool.describe` はツール検索で読み込んだ MCP のツールにもう一度発火し（`e.description` は読み込んだツールで Claude が読むテキスト）、`session.append` は行のテキストのブロックか `tool_result` のブロックの `content` を書き換えられる、とも改められました — [日本語](https://code.claude.com/docs/ja/plugins/mods/troubleshoot#claude-code-stops-asking-to-enable-hot-reloading) / [English](https://code.claude.com/docs/en/plugins/mods/troubleshoot#claude-code-stops-asking-to-enable-hot-reloading)
- **セルフホストのクイックスタートが、案内付きの設定と手作業の設定に分かれた**（`self-hosted-environments-quickstart`）。前提に、テストのセッション用の公開のリポジトリか、このホストが資格情報を聞かれずに HTTPS の URL でクローンできるリポジトリが加わりました。案内付きの設定（「Run the guided setup」。Owner のアカウントの `claude auth login` が要り、API キーやサードパーティのプロバイダーではセッションは始まるが組織の確認に失敗する。テストのセッションは自分で始め、最後の手順でランナーを止める）と手作業の設定（「Set up manually」。Owner が環境を作って秘密を渡してくれたなら手順 2 から）が分かれ、秘密のファイルを別のユーザーのランナーが読めないと `EACCES` で終わること、登録すると `Registered: runner_id=<runner-id>` が出ること、git のエラーに `could not read Username for` があればそのホストの HTTPS の資格情報がないこと、も加わりました。「If the runner exits」（作業が終わった `[runner:exit] account workload drained — exiting` と、連絡が途絶えた `runner record gone server-side`・`poll auth failed`）の節もできています — [日本語](https://code.claude.com/docs/ja/self-hosted-environments-quickstart#if-the-runner-exits) / [English](https://code.claude.com/docs/en/self-hosted-environments-quickstart#if-the-runner-exits)
- **セルフホストの環境のテストで、セッションを作るコマンドの出力が明記された**（`self-hosted-environments-testing`）。`claude -p "<prompt>" --environment <environment-id> --output-format json` は、作成できれば `{"ok":true,"session_id":"session_...",...}` の 1 行を、失敗すれば `{"ok":false,"error":"..."}` を出して終了コード 1 で終わり、クラウドのセッションが組織で使えない・プロンプトがないなどの一部の早いエラーでは JSON の行なしに標準エラーに出して終了コード 1 で終わります。例のスクリプトは `claude -p` に `< /dev/null` を渡すようになり、動かす前の準備が箇条書きになりました — [日本語](https://code.claude.com/docs/ja/self-hosted-environments-testing#run-the-test-loop) / [English](https://code.claude.com/docs/en/self-hosted-environments-testing#run-the-test-loop)
- **`decode-token` が鍵を取得できないか検証できないときの振る舞いが載った**（`self-hosted-environments-identity`）。理由を標準エラーに出し、クレームを何も出さずに終了コード 1 で終わります — [日本語](https://code.claude.com/docs/ja/self-hosted-environments-identity#verify-the-token-inside-the-session) / [English](https://code.claude.com/docs/en/self-hosted-environments-identity#verify-the-token-inside-the-session)
- **定期的なタスクの遅れの幅が表になった**（`scheduled-tasks` の「Jitter」）。定期的なタスクは作成時にタスクの ID から決まる固定の遅れを毎回足され、10 分ごとなら 0〜5 分、30 分ごとなら 0〜15 分、1 時間ごとか日ごとなどそれより間遠なら 0〜30 分です。`7,37 * * * *` で遅れが 14 分なら毎時 `:21` と `:51` に動く、という例が加わりました。1 回限りのタスクは `:00` か `:30` なら最大 90 秒早く動き、それ以外の分ならずらさない、という説明も小見出しに分かれています — [日本語](https://code.claude.com/docs/ja/scheduled-tasks#jitter) / [English](https://code.claude.com/docs/en/scheduled-tasks#jitter)
- **API のエラーのイベントの `attempt` の数え方が改められた**（`monitoring-usage`）。ストリーミングの失敗の後に要求をし直すたびに `attempt` は `1` から数え直すので、小さい値でも再試行を使い切ったことがあり、すべての再試行を使い切ったときの値は有効な上限に 1 を足した値以下（既定で 11 以下）、という書き方になりました。プロンプトを読むごとに `at_mention` のイベントは `mention_type` が `"agent"` と `"mcp_resource"` のものを各 100 件までしか記録しない（それを超える言及も解決はする）、とも加わっています — [日本語](https://code.claude.com/docs/ja/monitoring-usage#detect-retry-exhaustion) / [English](https://code.claude.com/docs/en/monitoring-usage#detect-retry-exhaustion)
- **vim モードの `f`・`F`・`t`・`T` と `df`・`dt` が今の行の中で動くと明記された**（`interactive-mode`）。約 1,000 行か 100,000 文字より長い返信の中の課題の参照（`owner/repo#123`）はリンクにならない、とも加わりました — [日本語](https://code.claude.com/docs/ja/interactive-mode#issue-reference-links) / [English](https://code.claude.com/docs/en/interactive-mode#issue-reference-links)
- **プロジェクトのスレッドに権限のルールが届くかが、環境の種類ごとに書き分けられた**（`claude-projects`）。リポジトリが 1 つならクラウドのスレッドはルールを適用し、複数で Anthropic がホストする環境なら届かず、複数でセルフホストの環境ならどのリポジトリの設定が効くかを `self-hosted-environments-configuration` で見ます。複数のリポジトリのクローンを追加のディレクトリとして付ける、という説明は外れました — [日本語](https://code.claude.com/docs/ja/claude-projects#what-threads-pick-up-from-your-repositories) / [English](https://code.claude.com/docs/en/claude-projects#what-threads-pick-up-from-your-repositories)
- **`claude attach` と `claude logs` に渡す名前の説明から「動いている」の限定が外れた**（`agent-view`・`cli-reference`）。ID の代わりにセッションの名前の一部を取れる（v2.1.290 以降）、という説明が「動いているセッションの名前」から「セッションの名前」になりました

**バグ修正**

- 管理設定の `PreToolUse` のフックが `"continue": false` で呼び出しを拒否したときと、管理設定の `prompt` のフックが呼び出しを止めたときに、呼び出しは断るがターンを終えない問題を修正
- 一部のセッションで、管理設定の PostToolUse のフックが `updatedMCPToolOutput` を適用しない問題を修正
- ヘッドレスのセッションで、ディレクトリを移るかプラグインを読み込み直した後、そのフォルダーでオフにしたフォルダーの `.mcp.json` かプラグインの MCP サーバーを始める問題を修正
- `allowedProviders` に `"gateway"` を含めて配る Claude apps gateway が、ユーザー設定でそのゲートウェイを指すノート PC を締め出す問題を修正
- 管理設定が `forceLoginMethod` を `gateway` にして `forceLoginGatewayUrl` を設定しないマシンで、保存した Claude apps gateway のサインインが無視される問題を修正（2.1.295 での退行）
- セッションの履歴を読めないとき、`--teleport` が空の会話を開く問題を修正
- Haiku 5.5 など適応型の思考だけを取るモデルのトークンの数え方を修正。一部のゲートウェイの後ろで失敗し、ほかでは予算型の思考で数えられていました
- セッションの停止が中断したツールの呼び出しを、利用者が拒否したと再開したサブエージェントに伝える問題を修正
- プラグインのヒントのタグに似たテキストを含むと、フックの出力が変えられる問題を修正
- 共有したトランスクリプトとデバッグのログの秘密の伏せ字で、値のないキーの後に続く一部の値（シェルの文字列の中に書いた JSON を含む）を見落とす問題を修正
- MATE Terminal など古い VTE ベースの端末で、コピーの後に `52;c;…` のエスケープシーケンスが画面に出る問題を修正
- `/diff` のパネルかダイアログを開いている間、トーストと通知が見えないまま待たされる問題を修正
- `UserPromptSubmit` のフックか mod の `prompt.submit` のフックの間の Esc か中断で、ヘッドレスのセッションが終わる、入力したプロンプトが消える、確認していないプロンプトが通る問題を修正
- ヘッドレスのセッションの開始後に読み込んだプラグインの SessionStart のフックが、同じ名前（または別の綴り）の別のプラグインがすでに動いていると飛ばされる問題を修正
- 登録を断られたときに `claude self-hosted-runner` が誤解を招くエラーを出す問題を修正。組織の管理設定を名指しするか、再起動したオンデマンドのランナーには新しい作業指示が要ると伝えます
- 同じリポジトリの別のセッションが `--capacity` 1 超のランナーで始まる間、セルフホストのランナーのセッションの git の fetch・pull・push が失敗する問題を修正
- ワークフローのスクリプトが、約 20,000 段より深く入れ子になった結果・エージェントの選択肢などの値を黙って切り詰め、深く入れ子になった結果が巨大なタスクの出力ファイルを書く問題を修正
- プラグインが提供する `$` のメソッドが、呼び出したエージェントではなく本体のセッションの作業ディレクトリで動き、呼び出したフックが持つターンを無視する問題を修正
- mod を読み込み直すか外した後も動いていた mod のフックから、`$.agent.register` が成功する問題を修正。その呼び出しは断ります
- 応答が 4 MiB の本文の上限を超える `Content-Length` を宣言すると、mod の `$.http.fetch` が `HEAD` の要求を断る問題を修正
- `constructor` のような名前のマーケットプレイスで、`claude plugin marketplace add`・`marketplace update`・`plugin install` が内部エラーで失敗する問題を修正。`add` はそのような名前をはっきり断ります
- `constructor` か `prototype` という名前のプラグインの秘密が、そのプラグインの選択肢の次の保存で消される問題を修正
- 機能フラグが読み込まれていないとき、保存した権限が許す Claude in Chrome の操作で、クラウドのセッションが auto モードの確認を飛ばす問題を修正
- MCP のツールの結果がターンを終えていたとき、再起動の後に `CLAUDE_CODE_RESUME_INTERRUPTED_TURN` が終わったターンを再実行する問題を修正
- シェル変数 `BASH_ARGV0` に代入してから使う一部のコマンドを、Bash の権限の確認が自動で承認する問題を修正。これらは承認を求めます
- 有効な UTF-8 でないファイル（Windows-1252・Shift-JIS・GBK）で、Edit と NotebookEdit がすべての非 ASCII 文字を置き換える問題を修正。そのような編集は断ります
- バックグラウンドのサービスの応答が遅いとき、`←` の直後に送ったプロンプトが 2 回（うち 1 回は前面で見えないまま）実行される問題を修正
- SessionStart のフックがまだ動いている間に送ったプロンプトが、`←` でセッションをバックグラウンドに移すと消える問題を修正。送られはしませんが、`↑` で戻せます
- ヘッドレスのセッションで、遅れて読み込んだプラグインの SessionStart のフックの出力が `/clear` の後の新しい会話に届く問題を修正
- フックが CLAUDE_ENV_FILE に書いた変数が PowerShell のコマンドに見えない問題を修正（ファイルが単純な代入だけを持つ場合）
- MCP サーバーが認証を要するとき、Claude がクラウドのセッションを非対話と呼び、`/mcp` か `claude mcp` を勧める問題を修正
- クラウドのセッション・Agent SDK・IDE の連携で、`/code-review` が生の JSON の配列で終わる問題を修正。指摘は番号付きの一覧で出ます
- auto モードが、共有の設定が変わっていないのに変わったとして、自分のアーティファクトへの更新を時々断る問題を修正
- 複数のセッションが設定のディレクトリを共有すると、claude.ai から同期したスキルのインストールが終わらず、同期のたびにまたダウンロードされる問題を修正
- 宣言したマーケットプレイスの依存も claude.ai から同期されると、claude.ai から同期したプラグインが無効になる問題を修正
- Linux のマシンからコピーしたプラグインのパスが /home の下を指すとき、macOS で起動が固まる問題を修正
- Windows でチェックアウトしたファイルのような CRLF の改行のスクリプトのファイルを、Workflow ツールが断る問題を修正
- `git commit -q` か `git -C <dir> commit` の後、OpenTelemetry の `tool_result` のイベントに `git_commit_id` がない問題を修正
- テキストが Unicode の行・段落の区切り文字（U+2028・U+2029）を含むと、`CLAUDE_CODE_TRANSCRIPT_LOCAL_GC` が保存したトランスクリプトからメッセージを落とす問題を修正
- テキストが Unicode の行・段落の区切り文字（U+2028・U+2029）を含むと、`claude purge` が履歴のファイルにプロンプトを残す問題を修正
- Windows: 約 1 KB より長い PowerShell のコマンドが常に許可を求める問題を修正。許可のルールと読み取り専用の判定が 32 KB まで効きます
- Windows: 終了時に stdio の MCP サーバーが強制終了される問題を修正。まず標準入力を閉じ、300 ミリ秒後もサーバーが動いているときだけプロセスツリーを止めます
- Windows: GitHub の SSH 鍵がないマシンで、GitHub の `owner/repo` のプラグインのソースの `claude plugin install` が失敗する問題を修正。クローンを HTTPS で再試行します
- Windows: バイパスの権限モードで、Git Bash の `rm -rf /c/Users/<name>` が尋ねない問題を修正
- [VSCode] 拡張機能の設定に `claudeCode.spinnerVerbs` がない問題を修正。settings.json で補完・検証され、不正な値でチャットのパネルが壊れなくなりました
- [VSCode] Windows で、C:\repo\file.ts や file:///C:/repo/file.ts のような Windows の完全なパスで書いたチャットのリンクがファイルを開かない問題を修正
- [VSCode] OS・VS Code・`prefersReducedMotion` の設定で動きを減らしても、作業中の表示が動き続ける問題を修正
- [VSCode] 画面がオフだった後やリモートのウィンドウが再接続した後など、パネルが遅れてメッセージに追いついたとき、プロンプトキャッシュの時計がまだ温かいと示す問題を修正
- [Cloud sessions] セルフホストのランナーを待つすべてのクラウドのセッションが同じ待ち順を示す問題を修正。各セッションが前に何件あるかを示します
- [Cloud sessions] クラウドのセッションで Claude がまだ返信している間に送ったメッセージが、返信の終わりにその上へ跳ぶ問題を修正。読み込み直した後も含めて下に留まります
- [Claude Tag] 括弧を含む URL へのリンクが、Claude の Slack の返信とタスクのチェックリストの一部で壊れ、余計な括弧のテキストを出して違うページを開く問題を修正
- [Claude Tag] 6 桁のプルリクエストの番号のように 16 進の色に見えるだけのコードの横に、Claude の Slack の返信が色見本を描く問題を修正
- [Claude Tag] Claude が Slack のチャンネルに投稿するプラグインの確認のカードが、プラグインの名前ではなく ID を示す問題を修正
- [Claude Tag] チャンネル自身の設定が含まないプラグインを外すカードを、Slack の Claude が投稿する問題を修正。代わりにプラグインの出どころを説明します
- [Claude Tag] セルフホストの環境のセッションが作業の途中で新しいランナーに移ると、Slack の Claude が返信を失うことがある問題を修正
- [Code Review] レビューが終わった後も、プルリクエストの Code Review のチェックが「進行中」のままになることがある問題を修正。レビューの結果を示します

**その他**

- `/cost`・ステータスライン・`--max-budget-usd`・SDK の費用の数字で、Sonnet 5.5 のキャッシュの読み取りの価格を 100 万トークンあたり 0.20 ドルから 0.10 ドルに変更
- 同梱の dataviz スキルを更新。ライトモードの 7 番目の系列を明るい紫に、ダークモードの主なテキストを柔らかくし、y 軸のラベルを 1K のように短くしました
- 先に送る MCP のツールの説明と MCP サーバーの指示の既定の上限を、2,048 文字から 4,096 文字に変更
- `←` を変更。セッションがバックグラウンドに移る間に始まったターンか `!` のコマンドは、見えないところで最後まで動かずに止まります
- [VSCode] `@browser` でつないだものを含むすべてのセッションで、端末と同じく Claude in Chrome がブラウザーの操作の前に尋ねるように変更。セッションでサイトを許可すると繰り返し尋ねません。`chrome` の「Permission prompts in VS Code sessions」も、プロンプトはチャットのパネルのカードで出て、許可していないサイトならそのサイトを許可する選択肢も出す、と改められ、`@browser` と打てば拡張機能が承認するという記述は外れました — [日本語](https://code.claude.com/docs/ja/chrome#permission-prompts-in-vs-code-sessions) / [English](https://code.claude.com/docs/en/chrome#permission-prompts-in-vs-code-sessions)
- [Claude Tag] Slack の Claude が、セッションのリンク・モデル・費用のフッターをスレッドの最新の返信にだけ出すように変更。その前の返信からはフッターが外れます
- **ハイライトに関わる言い換え**: `hooks-guide`（`onFailure`）はハイライト 1、`claude-apps-gateway`・`claude-apps-gateway-deploy`・`claude-apps-gateway-on-aws`・`managed-settings`（`cli` か `code` のブロック）はハイライト 2、`self-hosted-environments`・`self-hosted-environments-reference`（git proxy）はハイライト 3 のとおりです。`claude-apps-gateway` の開発者のログインの手順と `claude-apps-gateway-on-aws` の手順には、`forceLoginMethod`・`forceLoginGatewayUrl` に加えて `parentSettingsBehavior: "merge"` を設定する（配る）ことも加わりました
- **クラウドの VM の回収で戻らないもの**（`claude-code-on-the-web`）: 自分のペースの `/loop` の保留中の wakeup も戻らず、ループを再開するには `/loop` をもう一度実行します — [日本語](https://code.claude.com/docs/ja/claude-code-on-the-web#environment-expired) / [English](https://code.claude.com/docs/en/claude-code-on-the-web#environment-expired)
- **MCP のプロトコルの交渉**（`mcp`・`env-vars`）: v2 のランタイムは HTTP・stdio と claude.ai のコネクタのサーバーに新しい版に対応するかを尋ねる、という書き方になり、機能フラグを取得するセッションに限る、という条件が外れました。機能フラグの取得をオフにしたときにできないことの一覧からも、claude.ai のコネクタに版 2026-07-28 を尋ねる項目が外れています
- **HIPAA の設定の例**（`hipaa-setup`・`managed-settings`）: サンドボックス・ネットワークの許可リスト・資格情報の保護・ローカルのデータの保持を含む、より完全な `managed-settings.json` として、設定の例のリポジトリの `settings-hipaa.json` と `README-hipaa.md` への案内が加わりました — [日本語](https://code.claude.com/docs/ja/hipaa-setup#deploy-managed-settings) / [English](https://code.claude.com/docs/en/hipaa-setup#deploy-managed-settings)
- **サブエージェントが先に読み込むスキル**（`sub-agents`）: `skills` のフィールドに挙げたスキルは、異なる名前の最初の 32 個まで読み込む、と加わりました — [日本語](https://code.claude.com/docs/ja/sub-agents#preload-skills-into-subagents) / [English](https://code.claude.com/docs/en/sub-agents#preload-skills-into-subagents)
- **プラグインの細かな改訂**: `plugins/install`（まだ加えていないマーケットプレイスなら `Successfully added marketplace: <name> (declared in user settings)` を出してからプラグインを入れる）、`plugins/mods/create`（型の定義のファイルは対話のセッションで `--plugin-dir` から読み込んだ mod か Claude が書いた mod に書き、オンラインの `claude-code.d.ts` への案内は外れた）、`plugins/manifest-reference`（予約名を確かめるのはこれらのコマンドだけ、の文を削除）、`plugins/publish`（`claude plugin validate .` が確かめる内容への案内）
- **言い回しの調整**: `commands`（`-p` での `/mcp` の説明）、`cli-reference`（`claude mcp login` のコネクタへの案内、`--mcp-config` のセルフホストの環境での短い待ち）、`env-vars`（`CLAUDE_CODE_MCP_STARTUP_WAIT_MS` のセルフホストの環境での意味）、`glossary`（リンクの文言）、`troubleshooting`（ダウンロードの失敗の案内先を `troubleshoot-install` に）、`skills`・`cloud-environments`（claude.ai のアカウントのスキルへの案内）、`agent-sdk/python`（`CLAUDE_CODE_MAX_RETRIES` の説明の分割）
- **見出しの改称**: 「From …」「In …」「For …」のような短い見出しが、内容を表す見出しに改められました。`agent-sdk/mcp`（「Add a server in code」など）、`agent-sdk/migration-guide`（「Migrate a TypeScript or JavaScript project」など）、`agent-view`（「Dispatch an agent from agent view」など）、`claude-code-on-the-web`（「Start a cloud session from your terminal」「Continue a cloud session in your terminal」）、`env-vars`（「Set variables in your shell」など）、`jetbrains`、`mcp`（「Add a server from a URL」など）、`monitoring-usage`（「Backends for metrics」など）、`plugins/create`（「Load a plugin from a directory or `.zip`」など）、`security-guidance`（「Checks on each file edit」など）、`setup`（「Uninstall a native installation」など）です。多くは旧い見出しの id を残していますが、`plugins/create` の「Load a folder of plugins」と `hooks-guide` の「Check what a hook did」は id も新しくなりました
- **見出しマップ**: 75 行が加わり 37 行が外れました（各 1 行は自動生成のスタンプ）。新しい見出しが 39、改称が 33、`errors` から `troubleshoot-install` への移動が 2 で、`errors` の「Installation errors」が消えました
- **見出しマップ冒頭の自動生成スタンプが、2026年10月09日 00時59分51秒 UTC から 2026年10月10日 01時38分51秒 UTC へ進みました**

**参考リンクについて**: 日本語版は、changelog を除く変更のあった 57 ページをすべて取得して、リンクを付けた節の id と今回の内容（新しい節や書き換えた文）があるかを確かめました。今回も日本語版の追従が早く、`hooks`・`claude-apps-gateway-config`・`self-hosted-environments-deploy`・`self-hosted-environments-configuration`・`plugins/mods/api`・`agent-sdk/typescript`・`troubleshoot-install`・`errors`・`plugins/troubleshooting` をはじめ、リンクを付けたすべてのページの該当の節がすでに今回の内容になっていたため、すべて日本語版のリンクを付けています。changelog だけに載っていて対応する節のない項目にはリンクを付けていません。**changelog ページへのリンクは、本サマリの方針どおり付けていません。**
<!-- light:minor-updates:end -->

## 新着情報

<!-- light:whats-new:start -->
**今回、`whats-new/` 配下のページに変更はありません。**
<!-- light:whats-new:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-10-08.md](./archives/latest/2026-10-08.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-10-08.md](./archives/latest-detail/2026-10-08.md)

<!--
base_commit: f7270cc772c15a132c348d04599b3544e0e7722c
head_commit: 83613c64d38ac27f70c52d6b25167a2fa1f233f2
generated_at_full: 2026-10-10T15:13:30+09:00
-->
