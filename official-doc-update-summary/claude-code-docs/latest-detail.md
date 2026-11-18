---
対象期間: 2026年11月16日 〜 2026年11月17日
作成日: 2026-11-17
---

# Claude Code 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
**今回は changelog に v2.1.327（2026年11月17日、173 項目）が積まれ、auto mode の分類器がポリシーの名前で止めたときの直し方の節が `auto-mode-config` にできました。claude.ai のログインが切れた後に保存した別の認証情報が使われうること、プラグインが動く Claude Code の版を `engines` で宣言できること、HIPAA 構成の組織のセッションも v2.1.326 以降は auto mode で始まること、HTTP フックの許可リストの効く範囲の説明が改められたことも載っています**。新規ページと新着情報（whats-new）のページはありません。`llms.txt` は、カテゴリーの末尾に重ねて載っていた 36 件の再掲が外れてエントリが 241 から 205 になりました（一意な URL は 205 のままで、外れたページはありません）。`llms-full.txt` では 205 ページのうち 40 ページ（changelog を含む）の内容が変わり、ファイルの冒頭に見出しと案内の 6 行が加わりました。生の差分は 473 行（追加 358・削除 115）で、うち 189 行は changelog の新しいリリースです。大幅更新は `auto-mode-config` の 1 ページです。総行数は 129,371 行から 129,614 行に増えました。

主要なものを以下に挙げます。

1. auto mode の分類器がポリシーの名前（`[Destructive or Unwanted Actions]` など 4 つ）で止めたときの直し方の節が `auto-mode-config` にできた。ポリシーの名前は分類にすぎず、`claude auto-mode defaults` にはその文面が出ない。その呼び出しだけを頼む・`autoMode.environment` に書く・`autoMode.allow` に書く、の 3 つの対処が載った
2. claude.ai のログインが切れた後の扱いが改められた。ほかに認証情報がなければ `Login reached its time limit` か `Login expired` で失敗し、`ant auth login` のプロファイルのような別の認証情報があれば、その組織への課金でそちらが使われうる
3. プラグインが動く Claude Code の版を、`plugin.json` とマーケットプレイスのエントリの `engines` に semver の範囲で書けるようになった（v2.1.323 以降）。v2.0.15〜v2.1.75 はこのフィールドがあるとマニフェストを拒む
4. HIPAA 構成の組織のターミナルと VS Code のセッションも、v2.1.326 以降は既定で auto mode で始まる、と改められた（v2.1.285〜v2.1.325 は Manual mode）。auto mode に入ると外れる広い許可ルールの例も増えた
5. HTTP フックの許可リスト（`allowedHttpHookUrls`・`httpHookAllowedEnvVars`）は、managed settings に置けば組織が配るフックに、どの設定ファイルに置いてもそれ以外のフックに効く、という説明になった
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**auto mode のポリシーによる拒否の直し方の節ができた**](#1-auto-mode-のポリシーによる拒否の直し方の節ができた):  
  `auto-mode-config` に h3「Fix `Destructive or Unwanted Actions` and other policy denials」ができ、サーバー側の分類器がポリシーの名前で止めたときの読み方と 3 つの対処が載りました。`hooks` の `PermissionDenied` の `reason` と、`monitoring-usage` の `classifier_category` も、ポリシーの名前を含む説明になっています
2. [**claude.ai のログインが切れた後の扱いが改められた**](#2-claudeai-のログインが切れた後の扱いが改められた):  
  `authentication` に h4「After the login expires」ができ、ほかに認証情報がなければ要求は失敗し、別の認証情報があればそちらが使われうる、と分けて書かれました。`errors` の「Find your error」には、ログインが時間の上限に達したときなどの 3 行が加わっています
3. [**プラグインが動く Claude Code の版を `engines` で宣言できるようになった**](#3-プラグインが動く-claude-code-の版を-engines-で宣言できるようになった):  
  `plugins/manifest-reference` と `plugins/marketplace-reference` に `engines` のフィールドが加わりました。`claude-code` のキーに semver の範囲を書き、v2.1.323 以降が要ります。検証のメッセージも 2 つ加わっています
4. [**HIPAA 構成の組織のセッションも v2.1.326 以降は auto mode で始まるようになった**](#4-hipaa-構成の組織のセッションも-v21326-以降は-auto-mode-で始まるようになった):  
  `permission-modes` の「Permission modes with the HIPAA configuration」が書き直されました。あわせて、auto mode に入ると外れる広い許可ルールの例・`SendMessage` の確認を飛ばす条件・サーバー側の確認を待つファイルの編集も加わっています
5. [**HTTP フックの許可リストが効く範囲の説明が改められた**](#5-http-フックの許可リストが効く範囲の説明が改められた):  
  `hooks` に h4「Limit HTTP hooks」ができ、`settings-reference` の `allowedHttpHookUrls` と `httpHookAllowedEnvVars` も、置く設定ファイルで効くフックが分かれる、という説明になりました。changelog の v2.1.326 にある変更に追従したものです
<!-- light:highlight-list:end -->

## 1. auto mode のポリシーによる拒否の直し方の節ができた

**`auto-mode-config` の「Review denials」に h3「Fix `Destructive or Unwanted Actions` and other policy denials」ができました（詳細は大幅更新 1 参照）。** 拒否に次の 4 つのいずれかの名前が出ていれば、サーバー側の分類器が呼び出しを止め、理由として広いポリシーを挙げたことを示します。

- **ポリシーの名前**: `[Destructive or Unwanted Actions]`・`[Unauthorized Access]`・`[Undermining Oversight]`・`[Unsanctioned Communication]`
- **読み方**: ポリシーの名前は分類にすぎず、`claude auto-mode defaults` はその文面を出さない。会話の中で止められた呼び出しを読むか、ターミナルのセッションで `/permissions` を実行して **Recently blocked** を見る
- **対処**: Claude にさせるつもりだったなら、分類器にもっと文脈を与える。この呼び出しだけなら、操作と対象を名指して頼む（例: 「overwrite `data/seed.json`」）。パッケージのレジストリのような信頼する宛先なら `autoMode.environment` に加える。今後も許したい日常の操作なら `autoMode.allow` のエントリに書く。エントリを加えたら、分類器がもう一度確かめるよう Claude に再試行を頼む

同じページの「Fix a denial with an allow rule, an environment entry, or a retry」では、角括弧の中の文字列は分類器が当てたものを名指し、Claude Code に組み込まれたルールなら、角括弧を外した名前を `claude auto-mode defaults --label` に渡せば全文が読める、となりました（これまでは、角括弧の中は分類器が当てたルールの名前で、文面は「Inspect the defaults and your effective config」で読む、としていました）。「Inspect the defaults and your effective config」には、auto mode の `/status` が `Auto mode server` を `Enabled` と示している間は、サーバーの組み込みのルールがこの出力と違うことがあり、それを出す `claude auto-mode` のサブコマンドはない、という注記が加わっています。

ほかのページもポリシーの名前を扱うようになりました。

- **`hooks` の「PermissionDenied input」**: `reason` の説明は「The denial reason」だけになり、ログに残すときに `reason` に出る文字列が別の一覧になった。分類器の判定なら、ほとんどのセッションで当てたポリシーかルールの名前が `[Destructive or Unwanted Actions]` のように角括弧で出る（これまでの例は `[Data Exfiltration]`）。判定がなければ `Auto mode could not evaluate this action and is blocking it for safety` で始まる。分類器のモデルが使えないときに加えて、サーバーの確認が失敗したか時間切れになったときも `Classifier unavailable` になる
- **`monitoring-usage` の `classifier_category`**: 分類器が名指した「組み込みのルール」は「ポリシーか組み込みのルール」になった。属性が付くのは、分類器が名前を 1 つだけ挙げ、それを Claude Code がポリシーか組み込みのルールと認めたとき（これまでは、ルールを 1 つだけ挙げ、それがユーザーの書いたものではなく組み込みのとき）で、v2.1.323 より前はポリシーを名指した拒否には付かなかった、と加わった。Safety のイベントの `classifier_category` も、`tool_decision` と同じ条件で付く、となった
- **`permission-modes` の「How auto mode evaluates actions」**: 分類器が止めたときに Claude が受け取る理由は、ほとんどのセッションで当てたポリシーかルールの名前（`[Destructive or Unwanted Actions]` など）になる、となった

- [auto モードの設定 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/auto-mode-config#fix-a-policy-denial)
- [Configure auto mode - Claude Code Docs (English)](https://code.claude.com/docs/en/auto-mode-config#fix-a-policy-denial)
- [Hooks リファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/hooks#permissiondenied-input)
- [Hooks reference - Claude Code Docs (English)](https://code.claude.com/docs/en/hooks#permissiondenied-input)

## 2. claude.ai のログインが切れた後の扱いが改められた

**`authentication` の「Renew an expiring login」に h4「After the login expires」ができました。** 保存したログインが切れて更新できなくなったら `/login` でサインインし直します。それまでの要求は、失敗するか、保存してある別の認証情報を使います。

- **ほかに認証情報がない**: モデルへの要求は `Login reached its time limit` か `Login expired` で失敗する
- **別の認証情報がある**（`ant auth login` のプロファイルなど）: 要求は代わりにその認証情報を使うことがあり、その組織に課金される
- **無人のセッション**: ログインより長く動く Remote Control のセッションは、サインインし直すまで切断される。agent view のバックグラウンドのセッションは、ほかに保存した認証情報がなければ進まなくなる（これまでは、どちらも認証情報が切れると進まなくなり、サインインし直すまで回復しない、としていた）

`/status` の `Login` の行が `Expired — log in again` と示すことは残り、そこに保存した組織とメールアドレスも出ること、この行に v2.1.210 以降が要ることは外れました。期限が近いときの警告についても、要求を止めることはない、という文と、クラウドのプロバイダー・`ANTHROPIC_API_KEY`・`ANTHROPIC_AUTH_TOKEN`・`apiKeyHelper` が認証情報を出すときは出ない、という文が外れ、claude.ai のログインが有効な認証情報のときだけ出る、という文だけになっています。

**`errors` の「Login expired」も改められました。** ほかに保存した認証情報がないときにこのメッセージで止まる、となり、ログインが時間の上限に達したなら、v2.1.318 以降ではどちらのメッセージも代わりに `reached its time limit` と述べる、と加わりました。v2.1.206 より前の動き・v2.1.210 より前の `/status`・「OAuth token revoked or expired」との違いの説明と、サインインせずに再試行すると要求ごとに同じメッセージが出る、という文は外れています。「Find your error」の表には次の 3 行が加わりました。

- `Login reached its time limit · Please run /login` / `Failed to authenticate: this login reached its time limit`（同じページの「Login expired」へ）
- `Failed to authenticate: your claude.ai login expired`（`authentication` の「After the login expires」へ）
- `claude.ai login ended · usage now billed to` / `Warning: the claude.ai login on this machine has ended`（同じく「After the login expires」へ）

changelog の v2.1.318 には、保存した claude.ai のログインが時間の上限に達したときのサインインの失敗を、そうと述べるよう直した項目があります。

- [認証 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/authentication#after-the-login-expires)
- [Authentication - Claude Code Docs (English)](https://code.claude.com/docs/en/authentication#after-the-login-expires)
- [エラーリファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/errors#login-expired)
- [Error reference - Claude Code Docs (English)](https://code.claude.com/docs/en/errors#login-expired)

## 3. プラグインが動く Claude Code の版を `engines` で宣言できるようになった

**`plugins/manifest-reference` の「Fields」の表に `engines`（Object）が加わりました。** プラグインが動く Claude Code の版を、`claude-code` のキーの下に semver の範囲で書きます（例: `"engines": { "claude-code": ">=2.1.400" }`）。Claude Code v2.1.323 以降が要ります。v2.0.15〜v2.1.75 では、このフィールドがあるとマニフェストが `Unrecognized key` のエラーで拒まれるので、それらの版でも動かしたいなら `engines` を書きません。

- **`plugins/marketplace-reference` の「Plugin entries」**: エントリにも同じ `engines` が書ける。v2.0.15〜v2.1.75 は、どれか 1 つのエントリにこのフィールドがあると `marketplace.json` 全体を拒むので、それらの版でもマーケットプレイスを使わせたいなら、すべてのエントリから外す
- **検証のメッセージ**: 「Validation messages」の表に、`plugins[i].engines.claude-code` が範囲として読めないときのエラー `Must be a version range such as ">=2.1.0"; got "<value>". It will be ignored at load time.` と、`plugins[i].engines` がオブジェクトでないときの警告 `'engines' must be an object such as { "claude-code": ">=2.1.0" }; got <type>. It will be ignored at load time.` が加わった
- **`plugins/troubleshooting`**: 「`claude plugin validate` reports errors」の表に同じ `Must be a version range …` の行が加わった。値を `">=2.1.0"` のような Claude Code の版の範囲にする

changelog の v2.1.323 の Added には、`plugin.json` に `engines["claude-code"]` を加え、宣言した範囲の外のプラグインはインストール・更新・読み込みされず、インストールと更新は範囲に合う最新の版を選ぶ、という項目があります。

- [プラグインマニフェストリファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/plugins/manifest-reference#fields)
- [Plugin manifest reference - Claude Code Docs (English)](https://code.claude.com/docs/en/plugins/manifest-reference#fields)
- [マーケットプレイスリファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/plugins/marketplace-reference#plugin-entries)
- [Marketplace reference - Claude Code Docs (English)](https://code.claude.com/docs/en/plugins/marketplace-reference#plugin-entries)

## 4. HIPAA 構成の組織のセッションも v2.1.326 以降は auto mode で始まるようになった

**`permission-modes` の h3「Permission modes with the HIPAA configuration」が書き直されました。** 組織に HIPAA 構成が適用されていれば、Claude Code v2.1.326 以降のターミナルと VS Code のセッションは既定で auto mode で始まり、v2.1.285〜v2.1.325 では対象のセッションが既定で Manual mode で始まります（これまでは、組み込みの `auto` の既定は当てはまらず Manual mode で始まる、としていました）。Manual mode で始め続けるには「Start in a different permission mode」を見ます。組織で auto mode か `bypassPermissions` をオフにするには、managed settings で `permissions.disableAutoMode` か `permissions.disableBypassPermissionsMode` を `"disable"` にします。ターミナルに出ていた `Auto mode isn't the default for your organization · Shift+Tab to switch` の通知と、auto mode に切り替える・auto mode で始める、の 2 項目は外れました。「Which mode a session starts in」の表の HIPAA の行も、v2.1.285〜v2.1.325 は `default`、ほかの版は次の行（ターミナルと VS Code では `auto`）に従う、となっています。changelog の v2.1.326 の Changed にある、HIPAA 構成の組織のターミナルと VS Code のセッションが既定で auto mode で始まるようにした変更に追従したものです。

**同じページの auto mode の説明もいくつか改められました。**

- **外れる広い許可ルール**: auto mode に入ると外れる、任意のコードの実行を許す広い許可ルールの一覧が「次のものを含む」となり、後ろにワイルドカードだけが続くラッパー（`Bash(timeout *)`）、ワイルドカードで始まるシェルのルール（`Bash(* --version)`）、一部のワイルドカードのパス（`Bash($HOME/bin/*)` や `PowerShell(C:\tools\x.exe *)`）が加わった。`auto-mode-config` の「Suspend shell allow rules」は、auto mode では `Bash(*)` のような広い許可ルールを外す、とこの一覧にリンクする形になり、`Monitor` を名指すルールを止める説明はそちらから外れた
- **`SendMessage` の確認**: Code Mode の外では、Claude が `SendMessage` でほかのエージェントに送るメッセージを、届ける前に分類器が確かめる。`SendMessage` に一致する許可ルールがあるか、`PreToolUse` のフックが `"allow"` を返すと、メッセージはこの確認を飛ばしうる、と加わった（v2.1.222 以降）。`agent-teams` の「Messages between agents」も、この確認に頼る前に、どのメッセージが確認を飛ばすかを確かめる、となった
- **サーバー側の確認を待つもの**: サーバー側の分類器の確認があるセッションでは、読み取り専用のシェルのコマンドとサンドボックスの中のシェルのコマンドに加えて、ファイルの編集もその確認を待ち、印が付けば止められる、となった。分類器の呼び出しがトークンの使用量に数えられる、という注記からは、読み取りと保護されたパスの外の作業ディレクトリーの編集は分類器を通らない、という文が外れ、`errors` の「Auto mode cannot determine the safety of an action」からも、作業ディレクトリーの中の読み取り・検索・編集は分類器を通らないので動き続ける、という文が外れている
- **PowerShell のコマンド**: 「Actions no mode auto-approves」に、`could not fully check your permission rules` の印が付いた PowerShell のコマンドもどのモードでも自動で承認しない、と加わった。信頼できるならプロンプトで承認し、拒まれたら Claude に書き直しを頼む。`errors` の「Find your error」にもこの行が加わった
- **会話の中の承認**: 動詞だけを名指した場合（「you can force-push」）、止めたままに「なりうる」という言い方になった（これまでは、何も解かない、としていた）

- [権限モードを選択する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/permission-modes#hipaa-configuration)
- [Choose a permission mode - Claude Code Docs (English)](https://code.claude.com/docs/en/permission-modes#hipaa-configuration)
- [権限モードを選択する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/permission-modes#how-auto-mode-evaluates-actions)
- [Choose a permission mode - Claude Code Docs (English)](https://code.claude.com/docs/en/permission-modes#how-auto-mode-evaluates-actions)

## 5. HTTP フックの許可リストが効く範囲の説明が改められた

**`hooks` の「Hook locations」に h4「Limit HTTP hooks」ができました。** HTTP フックの許可リストは、managed settings に置けば組織が配るフックに、どの設定ファイルに置いてもそれ以外のフックに効く、となりました。これまでは、managed policy settings を含むすべての出どころのフックに当てはまる、としていました。`allowedHttpHookUrls` の項目からも「どの設定のレベルで定義しても」が外れています。

`settings-reference` の 2 つのキーも同じ言い方になりました。

- **`allowedHttpHookUrls`**: managed settings に置けば組織が配るフックに、どの設定ファイルに置いてもそれ以外のフックに効き、Claude Code は対象のフックを、設定ファイルをまたいでマージした一覧のパターンに URL が一致するときだけ実行する。これまでの、一致しないものは実行せずに止め、空の配列はすべての HTTP フックを止める、という文と、managed settings を含むすべての出どころのフックに当てはまる、という文は外れた
- **`httpHookAllowedEnvVars`**: 同じく置き場所で対象が分かれ、対象のフックは、自身の `allowedEnvVars` と、設定ファイルをまたいでマージしたこのキーの一覧の両方が名指す変数だけを使える。定義が求めても読むべきでない秘密をフックに読ませないために使う、という文と、すべての出どころのフックに当てはまる、という文は外れた

changelog の v2.1.326 の Changed にある、`allowedHttpHookUrls` と `httpHookAllowedEnvVars` が managed settings のフックにどう当てはまるかを変えた項目に、ページが追従した形です。

- [Hooks リファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/hooks#limit-http-hooks)
- [Hooks reference - Claude Code Docs (English)](https://code.claude.com/docs/en/hooks#limit-http-hooks)
- [すべての設定 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/settings-reference#allowedhttphookurls)
- [All settings - Claude Code Docs (English)](https://code.claude.com/docs/en/settings-reference#allowedhttphookurls)

## 新規追加されたページ

<!-- light:new-pages:start -->
（今回の対象期間に新規追加されたドキュメントページはありません。`llms.txt` の一意な URL は 205 のまま、`llms-full.txt` の `Source:` の行も 208、固有のページも 205 のままです）
<!-- light:new-pages:end -->

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
- [**Configure auto mode**](#1-configure-auto-mode) ([日本語](https://code.claude.com/docs/ja/auto-mode-config#override-the-block-and-allow-rules) / [English](https://code.claude.com/docs/en/auto-mode-config#override-the-block-and-allow-rules)):  
  52 行（追加 33・削除 19）が変わりました。ポリシーによる拒否の直し方の h3 ができ（詳細はハイライト 1 参照）、`"$defaults"` を外して組み込みのルールを置き換える使い方の説明が外れ、すべてのリストに `"$defaults"` を含める、という案内になりました
<!-- light:updated-pages:end -->

**行数の数え方**: `llms-full.txt` の生の差分のハンクを、追加行は head 側、削除行は base 側の `Source:` 行でページに振り分けた値です。ページの並びは変わっていません。changelog（189 行）は新しい 1 リリースの分なので、これまでどおり「軽微な更新」で扱います。大幅更新の 1 ページに次いで多いのは `permission-modes` の 34 行（追加 19・削除 15）、`errors` の 25 行（追加 12・削除 13）、`settings-reference` の 18 行（追加 10・削除 8）で、どれも 50 行に届きません。

## 1. Configure auto mode

**`auto-mode-config` は 52 行（追加 33・削除 19）が変わり、`llms-full.txt` の中のページは 427 行から 441 行になりました。** 見出しは h3「Fix `Destructive or Unwanted Actions` and other policy denials」が 1 つ加わり、外れたものはありません。ページの説明文（`llms.txt` も同じ）は、組織が信頼するリポジトリ・バケット・ドメインを分類器に伝える、という前半はそのままで、後半が「環境の文脈を設定し、既定のブロックと許可のルールを上書きし、auto-mode の CLI のサブコマンドで実際の設定を確かめる」から「独自のブロックと許可のルールを設定し、設定を確かめる」になりました。

- **「Override the block and allow rules」**: 冒頭は「3 つの追加のフィールドで分類器の組み込みのルールの一覧を置き換えられる」から「分類器の組み込みのルールに加えるには、3 つの追加のフィールドのいずれかを設定し、その一覧にリテラルの文字列 `"$defaults"` を含める」になった。`"$defaults"` の位置に既定のルールが差し込まれ、独自のルールをその前後に置けて、組み込みの一覧の更新もリリースをまたいで受け継ぐ、という段落は外れた。一般的な依頼は明示的な意図に数えない、という段落は、優先順位の一覧の「明示的なユーザーの意図」の項目の下に字下げして入った
- **注意書き**: `"$defaults"` なしで `environment`・`allow`・`soft_deny`・`hard_deny` を設定すると、その節の既定の一覧全体が置き換わる（`soft_deny` では force push・`curl | bash`・本番へのデプロイ・auto mode の回避を含む組み込みの soft block のルールを、`hard_deny` では組み込みのデータの持ち出しのルールを失う）、という警告は、「設定するすべての一覧に `"$defaults"` を含め、それが持つ組み込みのルールを失わないようにする」という 1 文になった。一覧を完全に引き受けるときだけ `"$defaults"` を外し、`claude auto-mode defaults` で組み込みのルールを出して設定ファイルに写し、各ルールを見直す、という段落も外れた。`settings-reference` の `autoMode` も、すべての配列に `"$defaults"` を含めれば独自のルールが組み込みのものに加わり、外すと置き換わり「うる」となり、`best-practices` も「置き換える」が「置き換えうる」になっている
- **「Suspend shell allow rules」**: auto mode では Claude Code が `Bash(*)` のような広い許可ルールを外す、で始まる段落になった（ハイライト 4 参照）
- **「Inspect the defaults and your effective config」**: `claude auto-mode defaults` の説明は「組み込みの `environment`・`allow`・`soft_deny`・`hard_deny` のルールを JSON で出す」から「Claude Code に組み込まれた `environment`・`allow`・`soft_deny`・`hard_deny` のルールを出す」に、`claude auto-mode config` は「分類器が実際に使うものを JSON で出す」から「4 つの一覧を、設定したところは設定を当てて出す」になった。サーバーの組み込みのルールについての注記が加わった（ハイライト 1 参照）。`cli-reference` の `claude auto-mode defaults` の行と、`permission-modes` の「What the classifier blocks by default」も「Claude Code に組み込まれた」という言い方になり、ページの中の「実際の（effective）ルール」「実際の結果」という言い方も「ルール」「結果」になっている
- **「Fix a denial with an allow rule, an environment entry, or a retry」**: 会話から呼び出しを探す項目から、`Ran 3 shell commands` の例と、トランスクリプトビューアーが展開する、という部分が外れた。「今後は確認なしに実行したいコマンド」は「今後は許したいコマンド」になった。角括弧の中の名前の読み方は改められた（ハイライト 1 参照）
- **新しい h3**: 「Fix `Destructive or Unwanted Actions` and other policy denials」（詳細はハイライト 1 参照）

- [auto モードの設定 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/auto-mode-config#override-the-block-and-allow-rules)
- [Configure auto mode - Claude Code Docs (English)](https://code.claude.com/docs/en/auto-mode-config#override-the-block-and-allow-rules)

## 軽微な更新

<!-- light:minor-updates:start -->
今回の差分は **3 ファイル**（`llms.txt`・`llms-full.txt`・見出しマップ）です。`llms.txt` は 145 行が外れ 1 行が加わりました。外れたのは再掲の 36 件の h3 とエントリで、置き換わったのは `auto-mode-config` の説明文です（下の「その他」）。`llms-full.txt` では、205 ページのうち **40 ページ**（changelog を含む）の内容が変わりました。大幅更新の 1 ページを除く **38 ページ**と、changelog に加わった **v2.1.327（2026年11月17日、173 項目。Added 9・Changed 38・Improvements 26・Bug fixes 100）** を以下にまとめます。単一のリリースなので、各項目への版の併記は省いています。changelog の収録リリースは 442 から 443 になり、先頭は v2.1.327 です。新着情報（whats-new）のページはありません。

`llms-full.txt` の総行数は **129,371 行から 129,614 行へ 243 行増え**ました（生の差分の差し引き 358 − 115 と一致）。生の差分 473 行の内訳は、changelog の新しいリリースが 189 行、`auto-mode-config` が 52 行（追加 33・削除 19）、ファイルの冒頭の見出しと案内が 6 行、残りの 38 ページが 226 行（追加 130・削除 96）です。この 226 行のうち 10 行は、`setup` のインストールのコマンドの 5 つのフェンスで `theme={null}` がまた重なった行の置き換えです（下の「その他」）。

コードフェンスの外の見出しは、行頭が `#` の見出しだけを数えると 6,149 から 6,154 へ、引用の中の見出しも数えると 6,160 から 6,165 へ、どちらも 5 増えました。加わったのは、ファイルの冒頭の `# Claude Code Docs` と、`desktop` の h3「Claude Code is "newer than the maximum version allowed by your organization"」、`authentication` の h4「After the login expires」、`auto-mode-config` の h3「Fix `Destructive or Unwanted Actions` and other policy denials」、`hooks` の h4「Limit HTTP hooks」です。外れた見出しはありません。

**新機能**

- auto mode のポリシーによる拒否の直し方の節（`auto-mode-config`。詳細はハイライト 1 参照）
- claude.ai のログインが切れた後の節（`authentication`。詳細はハイライト 2 参照）
- プラグインの `engines` のフィールド（`plugins/manifest-reference`・`plugins/marketplace-reference`。詳細はハイライト 3 参照）
- **Desktop アプリの Claude Code が組織の上限の版より新しいときの節ができた**（`desktop` の新しい h3「Claude Code is "newer than the maximum version allowed by your organization"」・`settings-reference` の `requiredMaximumVersion`・`setup`）。デスクトップアプリが持つ Claude Code のコピーが、組織が `requiredMaximumVersion` で設定した上限より新しいと、ローカルのセッションは失敗し、エラーの詳細にこのメッセージが出ます。上限をメッセージにある Claude Code の版以上に上げるか、上限を外すよう管理者に頼みます。`settings-reference` では、バックグラウンドの自動更新と `claude update` が上限を超える版を飛ばすのは native と npm のインストールでのこと、となりました。デスクトップアプリが更新されるとそのコピーが上限より新しくなり、Code タブのローカルのセッションが始まらないこと、macOS と Windows でそのコピーを変えないにはデスクトップアプリの自動更新をオフにすること（Microsoft Store から入れたものは引き続きストアが更新する）も加わっています。`setup` の「Set version limits for your organization」からは、更新も `requiredMaximumVersion` の上限に従う、という文が外れました — [日本語](https://code.claude.com/docs/ja/desktop#version-above-your-organizations-limit) / [English](https://code.claude.com/docs/en/desktop#version-above-your-organizations-limit)、[日本語](https://code.claude.com/docs/ja/settings-reference#requiredmaximumversion) / [English](https://code.claude.com/docs/en/settings-reference#requiredmaximumversion)
- **実行済みの単発のタスクを一覧に出す方法が載った**（`desktop-scheduled-tasks` の「Manage scheduled tasks」）。実行済みのローカルの単発のタスクが **Scheduled tasks** のページにないときは、一覧の上の並べ替えのアイコンをクリックして **Include completed** を選びます — [日本語](https://code.claude.com/docs/ja/desktop-scheduled-tasks#manage-scheduled-tasks) / [English](https://code.claude.com/docs/en/desktop-scheduled-tasks#manage-scheduled-tasks)
- **セッション中に `managed-mcp.json` が効いたときの通知が表に載った**（`managed-mcp` の「How restrictions appear to users」「Disable MCP entirely」）。ターミナルのセッションを開いている間に `managed-mcp.json` が効くと、`Your organization now manages MCP servers on this computer` で始まる通知が出ます。「Disable MCP entirely」では、ユーザーが前に設定したサーバーは、次にセッションを始めると（ポリシーが理由だという警告なしに）読み込まれなくなる、から、各ユーザーの次のセッションまでに読み込まれなくなる、になりました。changelog の v2.1.326 には、セッション中に管理者が `managed-mcp.json` を加えたときに MCP サーバーの読み込みが止まる理由を説明するメッセージの追加と、セッションの途中で加えた `managed-mcp.json` が次の確認で適用されうるようにした変更があります — [日本語](https://code.claude.com/docs/ja/managed-mcp#how-restrictions-appear-to-users) / [English](https://code.claude.com/docs/en/managed-mcp#how-restrictions-appear-to-users)
- **プラグインのアンインストールが MCP バンドルの展開ファイルも消すことが載った**（`plugins/cli-reference` の「What an uninstall deletes and keeps」）。Claude Code はオプションとシークレットを消すとき、v2.1.326 以降がプラグインの MCP バンドルから `~/.claude/plugins/mcpb/` に展開したファイルも消します。別のプラグインが同じバンドルを使っている間は残し、そこに残っている展開ファイルは、どのセッションも `cleanupPeriodDays` の期間使わなければ自動で片付けられます。changelog の v2.1.326 にこの変更があります — [日本語](https://code.claude.com/docs/ja/plugins/cli-reference#what-an-uninstall-deletes-and-keeps) / [English](https://code.claude.com/docs/en/plugins/cli-reference#what-an-uninstall-deletes-and-keeps)
- **Agent SDK の Grep の出力に `timedOut` が加わった**（`agent-sdk/typescript`・`agent-sdk/python` の Grep の出力）。検索が時間切れになり、結果が不完全かもしれないときに `true` になるフィールドで、Claude Code v2.1.317 以降が要ります。changelog の v2.1.317 には、検索が時間の上限に達したときの Grep と Glob の部分的な結果を、Claude が完全なものとして扱う問題の修正があります — [日本語](https://code.claude.com/docs/ja/agent-sdk/typescript#grep-2) / [English](https://code.claude.com/docs/en/agent-sdk/typescript#grep-2)、[日本語](https://code.claude.com/docs/ja/agent-sdk/python#grep) / [English](https://code.claude.com/docs/en/agent-sdk/python#grep)
- **Discord のボットに要る権限に「Create Public Threads」が加わった**（`channels` の「Supported channels」） — [日本語](https://code.claude.com/docs/ja/channels#supported-channels) / [English](https://code.claude.com/docs/en/channels#supported-channels)
- `/install-github-app` がリポジトリを変更する前の確認を追加
- サーバーの JSON を標準入力から読む `claude mcp add-json <name> -` を追加。トークンをコマンドラインに出さずに済みます。Claude Code のセッションの中では使えません
- 再開したセッションの以前のメッセージを読み込めないときに、それを示す行を追加
- 壊れたエージェント・スキル・コマンド・出力スタイルのファイル、キーバインドのエラー、使えないサンドボックス、無視された権限の設定、決して一致しないフックのマッチャーの一覧を `/status` に追加
- ほかの設定が `/config` の行を上書きしているとき、その注記を追加
- ゲートウェイのヒントのヘッダーに `x-claude-code-managed-settings-checksum` を追加。managed settings が `CLAUDE_CODE_GATEWAY_HINT_HEADERS=1` を設定しているところで送られます（すでに設定しているところを含む）
- `admin.billing_group_tag` を設定した Claude apps gateway 向けに、`attributionProject` の設定でセッションの課金グループに名前を付けられるよう対応
- フルスクリーンでないレンダラーの名前として `/tui classic` を追加（`/tui default` も引き続き使えます）
- [VSCode] エクスプローラーの右クリックのメニューに「Claude Code: Add to Chat」を追加。選んだファイルとフォルダーをチャットで @-メンションします

**機能改善**

- auto mode の拒否の名前の扱い（`hooks`・`monitoring-usage`・`permission-modes`。詳細はハイライト 1 参照）
- ログインが切れたときのエラーの説明（`errors`。詳細はハイライト 2 参照）
- HIPAA 構成の組織の開始のモードと auto mode の許可の説明（`permission-modes`・`agent-teams`・`errors`。詳細はハイライト 4 参照）
- HTTP フックの許可リストの説明（`hooks`・`settings-reference`。詳細はハイライト 5 参照）
- `"$defaults"` の案内と `claude auto-mode` のサブコマンドの説明（`auto-mode-config`・`settings-reference`・`best-practices`・`cli-reference`。詳細は大幅更新 1 参照）
- **シードのマーケットプレイスの扱いが改められた**（`plugins/org` の「Seed containers and CI」）。「シードの項目が優先される（起動ごとに、シードで宣言したマーケットプレイスがユーザーの同名の項目を上書きする）」という項目が外れ、ユーザーか managed の設定がシードのマーケットプレイスの名前を `extraKnownMarketplaces` で宣言しているなら、そのソースと `ref` からシードを作る、という項目が加わりました。シードのプラグインをやめるにはマーケットプレイスを外すのではなく `claude plugin disable` を使う、という項目には、リポジトリの設定がシードのプラグインを有効にしているとき、という条件が付いています — [日本語](https://code.claude.com/docs/ja/plugins/org#seed-containers-and-ci) / [English](https://code.claude.com/docs/en/plugins/org#seed-containers-and-ci)
- **読み取り専用のコマンドのグロブとパスのパターンの説明が改められた**（`permissions` の「Read-only commands」「Special characters and `!` negation」）。すべてのフラグが読み取り専用のコマンドにはクォートしないグロブを許す、という段落は外れ、書き込みか実行のできるフラグを持つコマンドの項目の後ろに、`ls *.ts` や `head src/*.py` のようなコマンドはクォートしないグロブがあってもプロンプトなしで実行される、と加わりました（例の `wc -l src/*.py` は `head src/*.py` に替わっています）。パスのパターンは、書いたパスを gitignore のパターンとして読む、という前置きの下に、括弧と使えないパターンの 2 項目が並ぶ形になり、gitignore のパターンとして使えないパスの deny か ask のルールもそのパスそのものは守る、という文は外れました — [日本語](https://code.claude.com/docs/ja/permissions#read-only-commands) / [English](https://code.claude.com/docs/en/permissions#read-only-commands)
- **MCP の出力の警告と `claude -p` でのリソースの扱い**（`mcp` の「MCP output limits and warnings」「Use MCP resources」）。10,000 トークンを超える MCP のツールの出力の警告は、トランスクリプトビューアーが出すもので、閾値は固定、となりました。ヒントの一覧にあった、警告と上限の値・`MAX_MCP_OUTPUT_TOKENS`・50,000 文字を超える結果のファイルへの保存の説明は、この節へのリンクだけになっています。「Use MCP resources」には、`claude -p` ではリソースのメンションはただのテキストのまま、と加わりました — [日本語](https://code.claude.com/docs/ja/mcp#mcp-output-limits-and-warnings) / [English](https://code.claude.com/docs/en/mcp#mcp-output-limits-and-warnings)
- **パス別のルールで `[` をエスケープする書き方が改められた**（`memory` の「Path-specific rules」）。ファイル名のリテラルの `[` は、単一引用符の中でエスケープする（`'photos \[2024/**'`）、となりました（これまでは `photos \[2024/**`）。この段落は節の前のほうに移っています — [日本語](https://code.claude.com/docs/ja/memory#path-specific-rules) / [English](https://code.claude.com/docs/en/memory#path-specific-rules)
- **サブエージェントの永続メモリーの例が、好みと訂正を残すものに替わった**（`sub-agents` の「Enable persistent memory」「Persistent memory tips」）。ディレクトリーに積む知識の例は「コードベースのパターン・デバッグの知見・アーキテクチャーの決定」から「あなたの好み・あなたの訂正・プロジェクトの決定」に替わりました。例のプロンプトも、見つけたパターンや慣習や繰り返す問題ではなく、与えられたレビューの好みと訂正をメモリーに書く、という内容になり、ヒントのプロンプトも、コードのパスやライブラリーの場所ではなく、チームの好み・プロジェクトの制約・主な決定の理由を覚える、という内容になっています — [日本語](https://code.claude.com/docs/ja/sub-agents#enable-persistent-memory) / [English](https://code.claude.com/docs/en/sub-agents#enable-persistent-memory)
- **Microsoft Foundry の Hosted on Azure のデータの説明が外れた**（`data-usage` の「Local Claude Code: Data flow and dependencies」）。Hosted on Azure のデプロイメントでは、プロンプトと応答は Azure の中に留まり、Anthropic に出るのは利用のメタデータと Anthropic の安全のシステムが印を付けた内容だけ、という説明が外れ、データが処理・保存される場所を Claude Platform のドキュメントで見る、というリンクに替わりました — [日本語](https://code.claude.com/docs/ja/data-usage#local-claude-code-data-flow-and-dependencies) / [English](https://code.claude.com/docs/en/data-usage#local-claude-code-data-flow-and-dependencies)
- **mod が始めたモニターのイベントの扱いが改められた**（`plugins/mods/api` の「Work your mod started before the interruption」）。ユーザーが中断した後、mod が始めたモニターは動き続け、その間にモニターが上げるイベントは Claude Code が落とす、となりました（これまでは、ユーザーの次の入力の前に上がったイベントは落ちるが、モニターが終わったという通知だけはその入力の後に届く、としていました） — [日本語](https://code.claude.com/docs/ja/plugins/mods/api#work-your-mod-started-before-the-interruption) / [English](https://code.claude.com/docs/en/plugins/mods/api#work-your-mod-started-before-the-interruption)
- **設定の一覧のマージの説明が改められた**（`glossary` の「Settings layers」・`admin-setup` の「Decide how settings reach devices」）。`glossary` は「配列は層をまたいでマージし、上の層のスカラーが下の層を上書きする」から「`permissions.allow` のようなほとんどの一覧はファイルをまたいでマージする」に、`admin-setup` は「すべてのソースのエントリをマージする」から「優先度の低い設定のエントリを、当てはまる managed settings にマージする」になりました — [日本語](https://code.claude.com/docs/ja/glossary#settings-layers) / [English](https://code.claude.com/docs/en/glossary#settings-layers)、[日本語](https://code.claude.com/docs/ja/admin-setup#decide-how-settings-reach-devices) / [English](https://code.claude.com/docs/en/admin-setup#decide-how-settings-reach-devices)
- **作業ディレクトリーの外のパスの確認に例外が加わった**（`tools-reference` の冒頭の注記）。`Read`・`Grep`・`Glob` のような「No」のファイルのツールも、作業ディレクトリーと追加のディレクトリーの外のパスでは確認を求める、という文に、Claude Code 自身が要るファイルを除く、と加わりました — [日本語](https://code.claude.com/docs/ja/tools-reference) / [English](https://code.claude.com/docs/en/tools-reference)
- アカウントの変更後に、事前に始めてあった一部のバックグラウンドのセッションを破棄するよう変更
- ターミナルで利用上限に達して一時停止したワークフローが、ログイン後も、以前のログインが戻るかプロンプトを入力するまで一時停止したままになるよう変更
- `ExitWorktree` が、保存されていない作業を含むかもしれないワークツリーを削除する前に確認するよう変更。don't-ask モードや答える人がいないところでは、allow ルール・auto モード・bypass permissions モードが許さない限り拒まれます
- `.mcp.json` が `mcpServers` のキーなしに最上位にサーバーを並べているとき、`claude mcp add --scope project` がファイルを上書きせずに止まるよう変更
- ほとんどの許可のプロンプトで、矢印キーが一周せずに No で止まるよう変更。最後の答えより大きい番号は No に移ります
- パスの確認が一部のシンボリックリンクを拒むよう変更
- 作業ディレクトリーの内側とみなす範囲を変更。一部のパスで許可を求めるようになりました
- `permissions.blockReadsOutsideWorkingDirectories` が、bypass と auto のモードでより多くの Bash のコマンドについて確認を求め、auto モードでは一部を拒むよう変更
- `permissions.blockReadsOutsideWorkingDirectories` が、Read か Edit の deny ルールの下のパスを名指す Bash のコマンドを、確認を求める代わりにより多く拒むよう変更
- 課金される分類器の要求へのフォールバックについての auto モードの通知が、今後のリリースでフォールバックがなくなり、確認するはずだった各操作は確認を求めるか拒まれる、と述べるよう変更
- auto モードが、`Bash(pnpm dlx *)` のような任意のパッケージを実行する allow ルールと、すでに無視していたもののパスや版の形（`/usr/bin/npm run:*`）をより多く無視するよう変更。それらは安全の確認が判断します
- スクリーンリーダーのモード以外では、`/sandbox` とほとんどの `/config` の値の一覧に番号を付けないよう変更。矢印キーと Enter を使います
- 変数が非常に長いテキストに展開される Bash のコマンドを拒み、短い値かファイルを使うよう述べるメッセージを出すよう変更
- PowerShell のツールが、それを名指すルールがあっても、もう 1 つのコマンドの前に確認するよう変更。答えるものがなければ、ツール全体のルール・auto モード・bypass permissions モードが許さない限り拒まれます
- 兄弟のサブエージェントのメッセージで再開したサブエージェントが、セッションの権限の設定に従うよう変更。確認を求めたり、答える人がいないところでは拒まれたりすることがあります
- 起動フォルダーの隣を指す相対パスの `--add-dir` を `--worktree` と使うと、Bash のサンドボックスに、ワークツリーの隣ではなくそのフォルダーを与えるよう変更
- 起動フォルダーより上（`..` など）を指す相対パスの `--add-dir` を伴う一部の `--worktree` の起動で、Bash のサンドボックスと `--bg` のセッションにワークツリーだけを与えるよう変更
- Claude in Chrome が一部の認証情報のファイルのアップロードを拒むよう変更。それらは自分でページに添付します
- 新しいアーティファクトごとに承認を求める組織で、プラグインだけが作成したか許可したアーティファクトを拒みうるよう、アーティファクトの承認を変更
- 新しいアーティファクトごとに承認を求める組織で、尋ねる相手がいないセッションが、許可のプロンプトなしに新しいアーティファクトをすぐ拒むよう変更
- 設定がアーティファクトをオフにすると、すでに実行中のセッションでも Artifact のツールが呼び出しを拒むよう変更
- サブエージェントの中と、バックグラウンドのタスクの結果・ほかの人のメッセージ・コンパクションの後では、Artifact の公開のプロンプトが「don't ask again」を出さないよう変更
- `claude plugin eval` が、プラグインの許可のフックより自身の deny ルールを保ち、フックが通した呼び出しに印を付けるよう変更
- MCP サーバーのログが、エリシテーションの要求とフックの答えの全内容ではなく、モード・アクション・フィールド名を記録するよう変更
- `fg` で再開した直後のしばらくの間、ほとんどのプロンプトが Esc 以外の答えを無視するよう変更
- ツールの呼び出しをフックする mod がインストールされていても、Code Mode が起動を拒まないよう変更。管理者は引き続き managed settings で Code Mode をオフにしておけます
- モデルを指定せずに起動したサブエージェントが、再開したとき（`/model` の後を含む）に始めたときのモデルのままになるよう変更
- あるモデルの最初のサブエージェントが、そのモデルの設定なしに始める代わりに、Anthropic からの設定を最大 1.5 秒（`claude -p` では 10 秒）待つよう変更
- 再起動したバックグラウンドのサブエージェントと、自ら始まるターンが、プラグインの読み込みを待つよう変更
- Claude が実行した `claude --bg` のように、別の Claude Code のセッションが始めたセッションの起動プロンプトのほとんどを、プロンプトの履歴から除くよう変更
- Amazon Bedrock・Google Vertex AI・Microsoft Foundry のターミナルのセッションで、サブエージェントの進捗の要約を会話全体ではなく短いメモから書き、トークンを大幅に減らすよう変更
- 非対話（`-p`）モードで、最初の要求の前に実行する git のコマンドを減らすよう変更
- 初回のセットアップが、設定を変えられないリモートの VS Code・Cursor・Devin Desktop のセッションでターミナルの設定を飛ばすよう変更
- フルスクリーンのテキストの選択で、システム・思考・受信メッセージの行のグリフを除くよう変更
- Anthropic がホストするクラウドのセッションが、リポジトリのフラグとプラグインの配信の設定をより多く無視するよう変更。リポジトリの `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` は、最大でも `DISABLE_TELEMETRY` として働きます
- [VSCode] 同じウィンドウのターミナルのセッションがプロンプトを送ったとき、チャットの編集の diff が開いたまま承認を求め続けるよう変更
- [VSCode] IDE の接続から使われていないツール（openFile・saveDocument・getOpenEditors など）を削除
- セッションの最初の Bash のコマンドの速さを改善。シェルの起動ファイルが、承認の前に（拒まれる場合でも）実行されることがあります。`CLAUDE_CODE_DISABLE_SHELL_HEAD_START=1` でオフにできます
- 新しいモデルと PowerShell でのコミットを改善。秘密を含みそうなファイルをコミットしないよう Claude に伝えるようになりました
- サンドボックスの中のシェルのコマンドを改善。サンドボックスの除外の対象のコマンドが、許可の確認がサンドボックスに頼っていたためにサンドボックスに留まったとき、Claude がそれを知るようになりました
- 危険な `rm` の確認が解析できない、`rm` を含まないシェルのコマンドの拒否を改善。Claude は無害なものを、あきらめずに平易な構文で送り直せます
- 非常に長いセッションの再開を改善。途中で終わったトランスクリプトの読み込みを 1 回再試行するので、メッセージが失われにくくなりました
- 出力トークンの上限に 2 回達したサブエージェントの答えを改善。完全な形で返るか、一部だけだと最初に述べることが増えました
- 認識できないモデルでの長い返答を改善。32,000 出力トークンで切れた返答が、上限 128,000 で続くようになりました
- コンパクションの後の、完了したサブエージェントについてのリマインダーを改善。Claude がエージェントの出力ファイルを読めなければ、`SendMessage` でエージェントに尋ねるよう伝えられます
- API キーと Anthropic のプロファイルの両方が設定されているときの警告を改善。どちらを使っているかと、プロファイルへの切り替え方を述べます
- `/plugin` を改善。マーケットプレイスを外す前の質問が、そのプラグインの設定と保存したデータが消えると述べ、マーケットプレイスのページに別のマーケットプレイスのエラーが出なくなりました
- Windows: Git Bash も `pwsh` も PATH にないときの起動時間を、PowerShell の標準のインストール先をすぐ確かめることで改善。System32 の `powershell.exe` が、PATH の前のほうにあるものより優先されるようになりました
- Windows で PATH が Git for Windows の bin フォルダーを指すときの起動時間を、ランチャーを通さずに git.exe を直接起動することで改善
- Windows: PowerShell のツールの速さを、コマンドあたり最大で約 0.5 秒改善
- auto と bypass permissions のモードで、Bash のツールの変更ファイルの diff が用意されるまでの時間を改善
- macOS と Linux での、非常に深く入れ子になった存在しないパスに対する Bash の許可の確認と、URL を含む非常に長いテキストの秘密のマスクの速さを改善
- トランスクリプトの検索が、編集と書き込んだファイルの中のテキストを見つけるよう改善
- 大きな PNG の画像の読み込みの速さと、代わりに送る JPEG の品質を改善
- Artifact のツールが、アーティファクトのページが示すアドレスでアップロードしたファイルを読めるよう改善。ほかの形は引き続き失敗し、ほとんどはアップロードを 1 回の呼び出しに 1 つずつ ID で読むよう述べるメッセージが出ます
- Artifact のツールが、`prompt`・`limit`・`label` を使わない一部の呼び出しで、呼び出しを失敗させずにそれらを無視するよう改善
- `/mcp` の MCP サーバーのページを改善。ローカル・リモート・エージェントのサーバーが 1 つのレイアウトを共有し、メニューは Back で終わり、スクリーンリーダーのモード以外では操作に番号が付かなくなりました（矢印キーと Enter を使います）
- 狭いターミナルを改善。`/status`・フォーム・詳細の画面の配置がよくなり、`/model` と `/effort` は約 40 桁に収まり、`←/→ to adjust` のようなキーのヒントが残ります
- `/install-github-app` を改善。リポジトリ・シークレット・API キーの手順が標準の一覧とキーを使い、メッセージが短くなり、スピナーが付き、エラーが明確になりました
- `/desktop` を改善。ダウンロードの質問が y/n ではなく標準の一覧になりました
- [VSCode] Claude が続けて複数の編集をするときの速さを改善。キューに入った編集は新しい問題の待ちを共有します（問題が後の編集で報告されることがあります）
- [VSCode] `rg` が `PATH` にあるとき、大きなワークスペースでの @-メンションのファイル検索の速さを改善。結果の順位はターミナルとほぼ同じになり、タイプミスへの許容は小さくなりました
- [VSCode] 起動を改善。初めて開いたフォルダー・空のウィンドウ・ワークツリーで、モデルの選択がすぐ使えるようになりました（サードパーティのプロバイダーを除く）

**バグ修正**

- Remote Control: ワークツリーのモードでサーバーを止めると、実行中のセッションの `.env` のような git が無視するファイルが消える問題を修正
- `--use-anthropic-git-proxy` のセルフホストのランナーが、起動時に `GIT_CONFIG_GLOBAL` が名指す空でないディレクトリーを消す問題を修正。ランナーはそれを残し、変数を無視して警告します
- プロジェクトのスコープの `claude mcp add` と `claude mcp remove` が、`.mcp.json` の `$schema` やほかのツールの `servers` のような最上位のほかのキーを消す問題を修正
- `/export` が既存のファイルを尋ねずに上書きする問題を修正。ダイアログが尋ねるようになり、`/export <name>` はファイルを残して `/export` を実行するよう述べます
- 機能フラグを読み込んでいないクラウドとセルフホストのランナーのセッションで、承認が再起動の後に届いたとき、Stop を押した後も許可したコマンドが実行される問題を修正
- Enter で `/teleport` の読み込みエラーの画面が閉じる問題を修正
- `/plugin` でクリックの後に Enter を押すと、プラグインがインストールされるか無効になる問題を修正
- 利用上限のメニューの後の余分な Enter で、入力途中の `!` のコマンドが実行される問題を修正
- 内容に括弧を含む一部の `--disallowedTools` のルールを修正
- auto モードが、`PowerShell(.\scripts\build.ps1 *)` のように `.\` でスクリプトを名指す一部のワイルドカードの PowerShell の allow ルールを無視する問題を修正
- auto モードで、auto モードが許した 2 つ目のスクリプトを Claude が始めると、実行中の Code Mode のスクリプトが許可のプロンプトと拒否を受ける問題を修正
- 自分のトークンを持つ入れ子の `claude` が `forceLoginOrgUUID` で拒まれる問題を修正。セッションのトークンを受け取らないコマンドは、その `CLAUDE_CODE_OAUTH_SCOPES` も受け取らなくなりました（必要なものには設定します）
- プロセスが強制終了された後に同じ UUID でメッセージを送り直したとき、ヘッドレスのセッションが再開で保存したメッセージを失う問題を修正
- 空の返答か強制終了されたコマンドの後に再開したセッションが、再びのクラッシュかバックグラウンドへの移動の後に、答えを失うか巻き戻したプロンプトを戻す場合を修正
- 再起動中に Stop を押した後に送ったメッセージを、その後 Claude Code がクラッシュするとリモートのセッションが忘れる問題を修正
- 機能フラグを読み込んでいないクラウドかセルフホストのランナーのセッションを後で再開したとき、`/clear` の後に作ったタスクが失われ、消したタスクが戻る問題を修正
- 出力トークンの上限で切れた返答の直後のコンパクションが、その返答のツールの呼び出しと結果を失う問題を修正
- `/config` などのコマンドからの設定の変更が、警告なしに保存に失敗する問題を修正。プロンプトの下の行がそれを述べるようになりました
- 一部のファイルを復元できなかったとき、`/rewind` が何も言わずに閉じる問題を修正
- プロンプトが `/tmp/a.txt` のようなファイルのパスで始まるとき、貼り付けた画像が落ちる問題を修正
- `--agents` で渡したエージェントが、プラグインの読み込みか再読み込みで失われる問題を修正
- `--resume` のピッカーからセッションを再開すると、プラグインのエージェントが落ちる問題を修正
- `https_proxy` か `HTTPS_PROXY` が単なる `host:port` で、入力も出力もターミナルでない（デスクトップアプリ・SDK・cron）とき、Claude Code が起動を拒む問題を修正
- Linux の Claude Code が、起動時に自身を再起動する間に（Claude apps gateway への最初のサインインの後や、Code Mode をオンにしたときなど）シェルに戻ることがある問題を修正
- モデルの設定の取得がプロキシなどで止まったとき、`claude -p` が最初の要求の前にハングする問題を修正。10 秒後に設定なしで進みます
- 短時間のメモリー不足のエラーの後、画面が空白か固まったままになる問題を修正
- 画面を固めるかセッションを終わらせることがある、まれな表示の不具合を修正
- プログラムがセッションのネットワークプロキシへの接続を数千開いたままにすると、クラウドのセッションが壊れる問題を修正
- mod の `$.model.complete` か `$.model.classify` の呼び出しが利用上限に達したとき、ターンがハングする問題を修正。呼び出しはすぐ API のエラーを受け取るので、mod はそのエラーを扱う必要があります
- 閉じていないタグが数千あるコンパクションの返答と、一部の非常に長い WebFetch の URL での停止を修正。WebFetch は 2,000 文字を超える URL を、許可のプロンプトの前に拒むようになりました
- 数千の `@` メンションを含むメッセージで、Claude が答える前に止まる問題を修正。ファイルとして調べるのは最初の 100 のメンションだけになりました
- 非常に大きなファイルへの書き込みを拒んだ後にプロンプトが固まる問題を修正。拒んだ書き込みは短いプレビューを示すようになりました
- `/plugin` の検索の欄に一度に多くのキーが届くとクラッシュする問題を修正
- Linux のセキュリティのポリシーがプロセスの自分自身へのシグナルを止めるところで、中断したセッションの再開時か終了時に、誤ったクラッシュの報告と終了コードが出る問題を修正
- VPN の切断のような長めの障害の後、リモートの MCP サーバーが切断されたままになる問題を修正。ほかのマシンにホスト名と https で届くほとんどのサーバーは、約 1 日バックグラウンドで再試行されます
- Claude がすでに全体を読んだ、プロジェクトの外の変わっていないファイルについて、コンパクションの後に Edit が「File has not been read yet」で拒む問題を修正
- `head_limit` と `offset` でページを送るとき、Grep が結果を繰り返すか飛ばす問題を修正。content と count の結果はファイルのパスで並べられるようになりました
- 不明な種類の出力を含む Jupyter のノートブックで Read が失敗する問題を修正
- NotebookEdit がノートブックのファイルの最後の改行を消す問題を修正
- 10 MB 以上のファイルが一度に読むには大きすぎるとき、Read のツールが実際の大きさではなく 512KB と報告する問題を修正
- Bash のツールの変更ファイルの diff が、バイナリ・大きすぎる・多すぎて示せないファイルを名指さない問題を修正
- 同期かリモートに裏付けられたフォルダーがファイルのタイムスタンプだけを変えたとき、アーティファクトの公開が「the source file changed between approval and publish」で失敗する問題を修正
- 新しいアーティファクトごとに承認を求める組織で、承認した新しいアーティファクトがクラウドのスケジュールされたタスクのセッションで拒まれる問題を修正
- 新しいアーティファクトごとに承認を求める組織で、Agent SDK で作ったアプリが承認した新しいアーティファクトが拒まれる問題を修正
- 一覧の続きの要求が失敗したとき、`/artifacts` が一覧の一部か「No artifacts yet」を示す問題を修正。再試行し、一覧全体を読み込めなければ警告します
- リードと別のモデルの in-process のエージェントチームのチームメイトが、リードのコンテキストの上限で、間違ったモデルでコンパクションする問題を修正。自分の上限とモデルを（そのモデルの料金で）使うようになりました
- 終わったサブエージェントが、メッセージを送ってきた兄弟のサブエージェントのモデルと effort で再開する問題を修正
- auto モード以外で、バックグラウンドのエージェントを始めたサブエージェントが結果を読まずに自ら終わったとき、そのエージェントが終わったことがメインの会話に伝わらない問題を修正
- デスクトップアプリ・Web・SDK で、許可のプロンプトで 30 秒以上待ったバックグラウンドのエージェントを、Claude がまだ実行中と報告する問題を修正
- auto モードで、フォローアップのメッセージへのバックグラウンドのエージェントの返答が落ちたことが Claude に伝わらない問題を修正し、バックグラウンドのコマンドを待つエージェントによる繰り返しの起こしを減らしました
- バックグラウンドのタスクがサブエージェントを起こした後、デスクトップアプリ・Claude Code on the web・VS Code が、生のタスクの通知をサブエージェントのプロンプトとして示す問題を修正
- Remote Control と Claude Desktop のセッションで、別のセッションから「later」の優先度で送ったメッセージが、実行中のターンの終わりを待たずにそのターンに加わる問題を修正
- タイムアウトかレート制限の後、クラウドと Remote Control のセッションへのメッセージが古いアドレスで失敗と報告される問題を修正。メッセージが届いたかもしれないときは Claude がそう述べます
- Claude の作業中に送ったメッセージを `UserPromptSubmit` のフックが止めたとき、クラウドのセッションがエラーを出さない問題を修正
- 失敗したフックが何も示さない問題を修正（バックグラウンドのエージェントの SubagentStop、`/clear` と `/resume` での SessionEnd、フルスクリーンでの CwdChanged と FileChanged）
- 実行に失敗した Stop のフックが、問題を報告したように示される問題を修正
- Stop のフックの実行中に、フォーカスビューが終わった返答を隠したままにする問題を修正
- mod がツールの呼び出しにコンテキストを加えたとき、Claude が長い managed の PostToolUse のフックの出力を 2 回受け取る問題を修正
- プロジェクトの `.claude/settings.json` が `ANTHROPIC_BASE_URL` を LLM ゲートウェイに設定しているとき、一部のターミナルのセッションで `/model` が間違ったモデルを並べる問題を修正
- `CLAUDE_CONFIG_DIR` が別のフォルダーを指しているとき、`/statusline` が `~/.claude/settings.json` に書き込む問題を修正
- Windows で、ドライブレターの大文字と小文字が違う書き方のパスに `claudeMdExcludes` のパターンが一致しない問題を修正
- ワークツリーの最上位に `HEAD` という名前のファイルかフォルダーがあるとき、`claude agents` と `claude rm` が、完全にプッシュ済みのセッションの削除を（「The worktree has unpushed commits」で）拒む問題を修正
- クラウドか Remote Control のセッションが多いアカウントで、長い ListAgents の結果がほとんどのセッションを隠す問題を修正。長い一覧はページに分かれて届きます
- 数万のコネクターのツールの許可を持つ組織で、再開したセッションのターンが遅い問題を修正
- セルフホストのランナー: セッションのスクリプトかフックが始めた `claude -p` が、セッション自身の再試行の設定を引き継いだために、レート制限を待ち続ける問題を修正
- サーバーが拒んだのに、支出の上限のメニューが上限を変えたと報告する問題を修正
- `/tasks` のタスクの詳細で 2 回目の `x` が次のタスクも止める問題を修正
- 現れたばかりの許可のプロンプトで Esc が無視される問題を修正
- 行を後から読み込む一覧が、Enter と矢印キーを無視することがある問題を修正
- `/autofix-pr` がクラウドのセッションを止める間、Esc の後もキーボードを占有する問題を修正。ダイアログはすぐ閉じ、止めるのに失敗したときは後でリンク付きで報告されます
- ← でエージェントビューを開いた直後に ctrl+c で終了すると、シェルに空白の画面と迷子のマウスのコードが出る問題を修正
- 信頼の質問の直後の Ctrl+C で、ターミナルがフルスクリーンのままになる問題を修正
- フルスクリーンのモードで ← でエージェントビューを開くと、シェルが画面に一瞬出る問題を修正
- ターミナルの表示の不具合を修正（Ghostty でのリサイズ時のスクロールバックの乱れのほとんど、古い tmux の下の Windows Terminal と VTE 0.50.0 でリンクのアドレスが隠れる問題、16 色で選択のハイライトが出ない問題）
- kitty・Ghostty・iTerm2 の中で `allow-passthrough` をオンにした tmux で、一部の行が乱れる問題を修正
- セッション中にサーバーを加えたか拒んだ後、`/mcp` がサーバーが設定されていないと述べる問題を修正。何をすればよいかを述べるようになりました
- `/hooks` が `--settings` で与えたフックを除く問題を修正
- `/` のメニューが同じ名前の各スキルに行を並べるのに、どの行も最初のものを実行する問題を修正
- 選んだセッションの再開に失敗したとき、`/teleport` がメッセージを示さない問題を修正
- トランスクリプトの検索で n と N が一致を飛ばす問題を修正
- 長いセッションでトランスクリプトの検索（ctrl+o の後に /）を取り消すと、検索を始めた場所から遠くに着く問題を修正
- 短い行か空の行をまたぐと、上下のキーでカーソルの桁が失われる問題を修正
- シェルのモードで、`&&`・`;`・`|` の後のコマンドが来る位置で Tab がファイル名を補完する問題を修正
- ブランチ名かフォルダーのパスが長いとき、`claude --resume` と `/resume` で選んだセッションが画面から外れる問題を修正
- ツールから戻るとき、`/mcp` と `/plugin` の MCP のツールの一覧が位置を失う問題を修正
- `/resume` がウィンドウに収まる数より 1 つ少ないセッションを並べる問題と、送り直しても役に立たないほとんどの支出の上限の後に「Resend your message」のヒントが出る問題を修正
- MCP サーバーの長い質問が 1 行で切れる問題、テキストの欄が長い貼り付けを何の印もなく隠す問題、`/plugin` のオプションと `/login` の Bedrock と Vertex の手順で区切りの線が二重になる問題を修正
- リンクか色を含むコマンドの出力で「+N lines」の数が多すぎる問題と、短いウィンドウでトランスクリプトの `?` のヘルプが終わり方を隠す問題を修正
- ブラウザーの一覧から Ctrl+C を 2 回押しても `/chrome` が閉じない問題を修正
- スクリーンリーダーのモードで、エージェントの計画の承認に早すぎるタイミングで番号と Enter を入力すると、次の番号も落ちる問題を修正
- デッキかデザインを始めるとき、Claude が存在しないデザインシステムのトークンのファイルを読もうとする問題を修正
- 終了時にワークツリーを残したことを述べない問題を修正
- `/hooks` のヘルプが存在しない入力のフィールドを名指す問題を修正
- 外部エディターのキーを割り当て直した後も、質問のダイアログが ctrl+g を名指す問題を修正
- `forceLoginMethod` が `console` に設定されたコンピューターで、Claude のサブスクリプションの選択肢を指す 2 つのサインインのエラーメッセージを修正
- テーマを変えた後、`/config` が「Set theme to …」ではなくダイアログが閉じられたと述べる問題を修正
- [VSCode] PreToolUse のフックが確認を求めるときに示す理由を、許可のプロンプトが示さない問題を修正（anthropics/claude-code#85950）
- [VSCode] 許可のプロンプトのタイトルで長いツール名とファイル名が切れる問題を修正
- [VSCode] ターミナルのセッションの diff に入力した後、Claude が同じファイルを再び編集すると、前の提案した編集が示される問題を修正
- [VSCode] フィードバックや「Build a custom style」のダイアログ、@-メンションのメニュー、モデル・モード・「+」のメニュー、そのほかのポップアップを閉じる Escape が、Claude の応答も止める問題を修正

**その他**

- **`llms.txt` の再掲が外れた**: 9 つのカテゴリー（h2）のうち 7 つの末尾に、ページを 1 つずつ載せた h3 が計 36 個あり（Getting started 5・Build with Claude Code 6・Plugins 7・Administration 5・Configuration 4・Reference 1・Agent SDK 8）、どれもほかの場所にも載っているページの再掲でした。これらが外れ、エントリは 241 から 205 に、h3 は 44 から 8 に、行数は 557 から 413 になりました。一意な URL は 205 のままで、外れたページはありません。ほかに `auto-mode-config` の説明文が 1 行替わっています（大幅更新 1 参照）
- **`llms-full.txt` の冒頭に見出しと案内が加わった**: ファイルの先頭に、`# Claude Code Docs` の見出しと 2 つの引用（このファイルはとても大きく切り詰められることがあるので、索引には `https://code.claude.com/docs/llms.txt` を見る、という案内と、Claude Code の公式ドキュメントの説明）が、空行を含めて 6 行加わりました。これまでは最初のページ（`agent-teams`）の題から始まっていました
- **書式の崩れが再発した**: `setup` の「Install Claude Code」の 5 つのコードフェンスの開始行で、`theme={null}` が 1 回から 14 回に重なりました（`setup` の生の差分 12 行のうち 10 行）。前回のサマリで、23 回の重なりが 1 回に戻ったと書いた箇所です
- **外れた文**: `common-workflows`（`@server:resource` の形で接続した MCP サーバーからデータを取る、という文と、標準入力と標準出力はほかの Unix のツールと同じように働く、という文）、`plugins/publish`（ほかのプラグインが版の範囲を宣言していなければタグは要らない）、`plugins/host-marketplace`（1 つのマーケットプレイスは各プラグインの版を一度に 1 つだけ出す、Claude Code にリリースのチャネルという概念はない）、`troubleshooting`（`--safe-mode` はセッションのすべてのカスタマイズを無効にする）、`keybindings`（検証の一覧の、文字列か `null` でない値のような不正な操作の値）、`errors`（「Couldn't share the transcript」の、共有から先に落とす部分の順番）、`agent-sdk/typescript`（`client_composed` で展開しないものからの `@server:resource` のメンション）、`env-vars`（`CLAUDE_CODE_SIMPLE` の、自動の検出を無効にするものの一覧と、`--add-dir` で渡したディレクトリーのスキルは読み込まれる、という文）
- **字句の小さな修正**: `cli-reference`（`--bare` は「フック・スキル…の自動の検出を飛ばす」から「あなたのフックと、スキル…の自動の検出を飛ばす」に）、`env-vars`（`CLAUDE_CODE_SIMPLE` の Anthropic API の認証の言い方）、`headless`（`Bash(git diff *)` は「`git diff` で始まるあらゆるコマンドを許す」から「引数の有無にかかわらず `git diff` に一致する」に。標準入力を読む説明からも「ほかのコマンドラインのツールと同じように」が外れた）、`keybindings`（検証の一覧の「解析のエラー（不正な JSON か構造）」が「不正な JSON」に）、`plugins/mods/troubleshoot`（`hooks module did not load` の理由がファイルと行を示すのは「問題がコードにあるとき」から「構文のエラーのとき」に）、`errors`（「Credit balance is too low」のメッセージの例に `Credit balance too low · Add funds: https://platform.claude.com/settings/billing` が加わり、「OAuth token revoked or expired」と「There's an issue with the selected model」の言い方が整えられた）
- **changelog の汎用の項目**: v2.1.327 の Changed には「Bug fixes and reliability improvements」という汎用の 1 行もあります
<!-- light:minor-updates:end -->

見出しマップ（`en/claude_code_docs_map.md`）は、更新時刻が 2026年11月17日 02:33:28 UTC から 2026年11月18日 01:22:40 UTC に替わり、5 行が加わり 1 行が外れました（6,629 行から 6,633 行）。加わったのは、`llms-full.txt` に加わった 4 つの見出し（ファイルの冒頭の `# Claude Code Docs` を除く）と新しいスタンプで、外れたのは古いスタンプです。今回、見出しマップにだけ先に載った見出しはありません。

**参考リンクについて**: 日本語版は、今回リンクを付けたページの HTML を取得し、新しい節の id があるか、今回の差分で出入りしたコードの字句（変数名・版の数字・パス・リンク先・メッセージの文字列。base と head の `llms-full.txt` で数が違うものだけ）が英語版と同じだけあるかで、今回の内容になっているかを確かめました。`allow` や `reason` のような訳文の中にも出る一般的な語は数が合わないので、該当する箇所の訳文で確かめています。字句で判定できない地の文だけの変更（`tools-reference`・`plugins/org`・`plugins/mods/api`・`sub-agents` など）も、該当する箇所の訳文で確かめました。今回リンクを付けたページは、すべて今回の内容になっていました。アンカーは英語版・日本語版の HTML の見出しの id で確かめました。見出しの文字列から作るスラッグと違う明示の id が付いているものがあり、`auto-mode-config` の「Fix `Destructive or Unwanted Actions` and other policy denials」は `#fix-a-policy-denial`、`desktop` の「Claude Code is "newer than the maximum version allowed by your organization"」は `#version-above-your-organizations-limit`、`permission-modes` の「Permission modes with the HIPAA configuration」は `#hipaa-configuration` です。`agent-sdk/typescript` には Grep の見出しが入力と出力の 2 つあり、出力のほうは `#grep-2` です。`tools-reference` の冒頭の注記の変更は、ページを指しています。**changelog ページへのリンクは、本サマリの方針どおり付けていません。**

## 新着情報

<!-- light:whats-new:start -->
（今回の差分に新着情報（`whats-new/`）のページはありません。head の `llms.txt`・`llms-full.txt`・見出しマップにも whats-new のページは載っていません）
<!-- light:whats-new:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-11-16.md](./archives/latest/2026-11-16.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-11-16.md](./archives/latest-detail/2026-11-16.md)

<!--
base_commit: 819daa7cd17307570b2a672fc258fafc61fd2cb2
head_commit: ab0340993aa5987d27a891141698d57dc355b88b
generated_at_full: 2026-11-18T15:13:22+09:00
-->
