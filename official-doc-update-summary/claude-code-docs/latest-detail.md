---
対象期間: 2026年07月08日 〜 2026年07月09日
作成日: 2026-07-09
---

# Claude Code 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
今回の対象期間は、公式 changelog に v2.1.206（2026年07月09日）が追加されるとともに、前回 changelog で予告されていた v2.1.205 の変更が各リファレンスページ本文へ大規模に反映された回です。目玉は Desktop の Browser ペインによる外部サイト閲覧で、そのほかモデルエイリアスの解決規則、非対話モードのスラッシュコマンド、Agent SDK の interrupt レシートなど、前回は触れられていなかった実体が文書化されました。

主要なものを以下に挙げます。

1. Desktop の Code タブに Browser ペインが導入され、実行中アプリのプレビューに加えて外部サイトをタブブラウザとして開けるようになった（安全分類器と管理設定つき）
2. changelog に v2.1.206 が追加され、`/cd` のディレクトリ補完、`/doctor` の CLAUDE.md 圧縮提案、バックグラウンドエージェントの先行アップグレードなどが入った
3. モデルファミリーエイリアス（`opus` / `sonnet` / `haiku` / `fable`）が、許可リストや組織制限のもとで「許可された最新版」に解決されるようになった（v2.1.205）
4. 非対話モード（`-p`）やクラウド／Remote Control セッションで `/model` `/effort` `/fast` `/color` `/rename` `/mcp` が引数つきで使えるようになった（v2.1.205）
5. Agent SDK の `interrupt()` が中断後も残るキュー済みメッセージを返すレシート型を得て、`SDKSystemMessage.capabilities` による機能検出が導入された（v2.1.205）
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**Desktop の Browser ペインと外部サイト閲覧**](#1-desktop-の-browser-ペインと外部サイト閲覧):  
  Desktop の Code タブのプレビューペインが「Browser ペイン」に改称・拡張され、タブブラウザとして外部サイトを開けるようになった。Claude が外部ページを読む・操作する際は権限モードを問わず安全分類器が書き込み操作を審査し、サイトごとの承認カードが出る。管理者は `browserExternalPageTools` 管理設定で外部ページ上のツール利用を無効化できる。
2. [**v2.1.206 リリース**](#2-v21206-リリース):  
  2026年07月09日付で v2.1.206 が changelog に追加された。`/cd` のディレクトリパス補完、checked-in な `CLAUDE.md` の圧縮を提案する `/doctor` チェック、`/commit-push-pr` が `remote.pushDefault` への push も自動許可、`EnterWorktree` がプロジェクト外 worktree への進入時に確認、バックグラウンドエージェントが更新直後に先行アップグレードするようになった。
3. [**モデルファミリーエイリアスが許可された最新版に解決されるように**](#3-モデルファミリーエイリアスが許可された最新版に解決されるように):  
  `opus` / `sonnet` / `haiku` / `fable` が「そのファミリーの最新版の要求」ではなく「ファミリーの要求」として扱われ、`availableModels` 許可リストや組織のモデル制限のもとでは許可された最新版に解決されるようになった（v2.1.205）。`opusplan` のプラン時アップグレードも同様に、許可された最新の Opus を使う。
4. [**非対話モードで使えるスラッシュコマンドの拡大**](#4-非対話モードで使えるスラッシュコマンドの拡大):  
  `/model` `/effort` `/fast` `/color` `/rename` が値を引数として受け取る形で非対話モード（`-p`）・クラウドセッション・Remote Control から使えるようになり、`/mcp` は引数なしでサーバ状態のテキスト要約を出すようになった（v2.1.205）。ただし非対話で設定した値はセッション限定で既定として保存されない。
5. [**Agent SDK の interrupt レシートと capabilities による機能検出**](#5-agent-sdk-の-interrupt-レシートと-capabilities-による機能検出):  
  `interrupt()` が新しい `SDKControlInterruptResponse`（`still_queued`）で解決するようになり、中断後も生き残るキュー済みユーザーメッセージの UUID を返す（v2.1.205）。`SDKSystemMessage` には `capabilities` 配列が追加され、バージョン文字列比較ではなく `interrupt_receipt_v1` のような能力名で機能検出できる。
<!-- light:highlight-list:end -->

## 1. Desktop の Browser ペインと外部サイト閲覧

Desktop（`docs/en/desktop`）の Code タブで、これまで「preview ペイン／埋め込みブラウザ」と呼ばれていた領域が **Browser ペイン**に改称され、単なるアプリプレビューを超えたタブブラウザになりました。**Cmd+Shift+B**（Windows は **Ctrl+Shift+B**）または **Views** メニューから開き、実行中アプリの隣にドキュメントや issue トラッカーなど任意のサイトを並べられます。チャット内の外部リンクをクリックすると「Open in app（Browser ペイン）」と「Default browser」の選択肢が出て、**Cmd**（Windows は **Ctrl**）クリックならシステムブラウザで直接開きます。Google OAuth のようなポップアップ型サインインを含め、ペイン内でサイトにログインすることもできます。キーボードショートカット表も `Cmd+Shift+P`（Toggle preview pane）から `Cmd+Shift+B`（Toggle Browser pane）へ更新され、ペイン一覧の「preview」も「browser」になりました。

外部ページの取り扱いには 2 つの安全チェックが加わります。1 つはクリックや入力といった**書き込み操作を審査する安全分類器**で、これは auto mode が使うものと同じ分類器であり、フラグが立てば権限モードに関わらず確認プロンプトが出ます。もう 1 つは、Auto と Bypass permissions 以外の権限モードで新規サイトへ遷移する前に働く**ドメイン許可リストチェック**です。Claude が外部サイトで初めて操作するときは **Allow once / Always allow / Deny** の権限カードが出て、承認はサイト単位（サブドメインも別扱い）で保存されます。ローカル dev サーバとプロジェクトファイルは承認不要なので auto-verify は従来どおり動きます。承認済みサイトでも、購入・アカウント作成・CAPTCHA 回避は Claude が勝手に行いません。Browser ペインはクリーンなブラウザプロファイルを使うため、ログイン状態を伴う操作をさせたい場合は [日本語](https://code.claude.com/docs/ja/chrome) / [Claude in Chrome 拡張](https://code.claude.com/docs/en/chrome)を使う、という使い分けが示されています。組織向けには Chrome 拡張と同じサイト許可／ブロックリストが適用され、管理者は `browserExternalPageTools` 管理設定を `"disabled"` にすることで、外部ページ上での Claude のツール利用（読み取り・操作）だけを止められます（ユーザー自身の遷移とローカルプレビューは影響を受けません）。

- [Desktop application (Browse external sites) - Claude Code Docs (English)](https://code.claude.com/docs/en/desktop#browse-external-sites)

> 本節は en 側のみで、日本語版 desktop ページは本サマリ作成時点で旧記述（「埋め込みブラウザで実行中のアプリをプレビュー」、外部サイト閲覧の節なし）のままである（WebFetch で確認）ため、日本語リンクを省略しています。

## 2. v2.1.206 リリース

公式 changelog に v2.1.206（2026年07月09日）のエントリが追加されました。新機能・改善としては、`/cd` に `/add-dir` と同じディレクトリパス補完が付いたこと、`/doctor` に「codebase から導出できる内容を削ることで checked-in の `CLAUDE.md` を圧縮する」提案チェックが加わったこと、`/commit-push-pr` が `origin` に加えてリポジトリの設定済み push リモート（`remote.pushDefault`、またはリモートが 1 つだけならそれ）への `git push` を自動許可するようになったことが挙げられます。ゲートウェイ利用者向けには `/login` が Anthropic 運営のパブリックゲートウェイエンドポイントに対応しました。

安全性・運用面では、`EnterWorktree` がプロジェクトの `.claude/worktrees/` の外にある git worktree へ入る前に確認を求めるようになり、バックグラウンドエージェントは Claude Code 更新直後にバックグラウンドで新バージョンへアップグレードするようになりました（従来は attach 時に遅い stale セッションのアップグレード費用を払っていました）。品質面では `/code-review` の指摘品質が claude-opus-4-8 の全 effort レベルで改善され、agents view のステータス列が 64 文字で切り詰めず端末幅いっぱいを使うようになり、`Ctrl+X` で完了セッションを恒久的に削除できるようになりました。多数の不具合修正も含まれます（「軽微な更新」のバグ修正を参照）。

> 本リリースの内容は changelog ページにのみ記載され、対応する通常ドキュメントページに個別の節が無いため、参考リンクは省略しています（changelog リンク不使用ポリシー）。

## 3. モデルファミリーエイリアスが許可された最新版に解決されるように

モデル設定ページ（`docs/en/model-config`）の「Restrict model selection」節が書き直され、`opus` / `sonnet` / `haiku` / `fable` の**ファミリーエイリアス**が「そのファミリーの最新版を指す名前」ではなく「そのファミリーの要求」として解釈されるようになりました（v2.1.205）。Anthropic API と Claude Platform on AWS では、エイリアスは `availableModels` 許可リストが許す**最新版**に解決されます。たとえば許可リストが `["sonnet", "claude-opus-4-6"]` のとき、`/model opus` も `--model opus` も許可された最新の Opus である Claude Opus 4.6 を選び、要求モデルと代替モデルの双方を示す通知が出ます。v2.1.205 より前は、最新版がリストの外にあれば、より古い版が許可されていてもブロック扱いで拒否・置換されていました。組織のモデル制限側（Console / claude.ai admin console）でも同様で、`/model <alias>` が拒否されるのはそのファミリーの**全ての版**が制限されている場合だけになりました。

同じ規則がプランモードのアップグレードにも及びます。`availableModels` が最新の Opus を除外していても古い版を許可していれば、`opusplan` はプランモードで許可された最新の Opus を使い、Opus が全て除外されている場合にのみ Sonnet に留まります。Haiku セッションのプランモード時 Sonnet 昇格も同様です。ただしこの「許可された古い版への代替」が効くのは Anthropic API と Claude Platform on AWS のみで、プロバイダ固有のデプロイ ID を使う Amazon Bedrock / Google Cloud's Agent Platform / Microsoft Foundry / Mantle では、従来どおりエイリアスは拒否・置換の扱いになり、プランモードもセッションのモデルに留まります。あわせて、ブロックされた選択の扱い（`/model` はエラー、`--model` / `ANTHROPIC_MODEL` / `model` 設定は起動時に警告つきで置換、subagent・skill・command のオーバーライドは継承モデルにフォールバック、`advisorModel` は advisor を無効化、`--advisor` は起動時エラー）が箇条書きに整理されました。

- [Model configuration (Restrict model selection) - Claude Code Docs (English)](https://code.claude.com/docs/en/model-config#restrict-model-selection)

> 本節の変更は en 側のみで、日本語版 model-config ページが本サマリ作成時点で当該変更を反映しているか確認できないため、安全側で日本語リンクを省略しています。

## 4. 非対話モードで使えるスラッシュコマンドの拡大

コマンドリファレンス（`docs/en/commands`）・headless・Remote Control・Claude Code on the web の各ページに、非対話モード（`-p`）とリモート面で使えるコマンドの範囲が明記されました（v2.1.205）。従来「対話ダイアログを開くコマンドは `-p` で使えない」とだけ書かれていた箇所が、「**ターミナル UI でしか動かないコマンド**（`/plugin` や `/resume` など）は使えないが、`/model` `/effort` `/fast` `/color` `/rename` は**値を引数として渡す形**で使える」に改められています（例: `/model sonnet`、`/effort high`）。`/mcp` は引数なしでもピッカーを開かずサーバ状態のテキスト要約を返します。`/config` は従来どおり `key=value` で設定を書き換えられます。

ただし挙動には制約があります。非対話モードで `/model` が設定したモデルは**現在のセッション限定**で既定として保存されず、`/effort` も同様にセッション限定です。さらに Fable 5・Opus 4.8・Opus 4.7 では「モデル既定 effort の保持（launch-default effort hold）」が効いているため、非対話の `/effort` は `Not applied` を報告してモデル既定に留まります。この hold を外すには起動時に `--effort` を渡す必要があります。`/fast` は `--settings '{"fastMode": true}'` を付けて起動したセッションでのみ動作し、その切り替えもセッション限定で既定には保存されません。クラウドセッションと Remote Control でも同じ引数形式が使え、いずれも Claude Code v2.1.205 以降を必要とします。

- [Commands (All commands) - Claude Code Docs (English)](https://code.claude.com/docs/en/commands#all-commands)

> 本節の追記は en 側のみで、日本語版 commands / headless / remote-control ページが本サマリ作成時点で当該追記を反映しているか確認できないため、安全側で日本語リンクを省略しています。

## 5. Agent SDK の interrupt レシートと capabilities による機能検出

Agent SDK の TypeScript リファレンス（`docs/en/agent-sdk/typescript`）に `SDKControlInterruptResponse` 型が新設されました（v2.1.205）。`interrupt()` の戻り値が `Promise<void>` から `Promise<SDKControlInterruptResponse | undefined>` になり、CLI が `interrupt_receipt_v1` 能力を持つ場合は `still_queued: string[]`（中断後も生き残るユーザーメッセージの UUID 群）を返します。ここに載るのは、キューに残っているメッセージと、次ターン用に取り出し済みで abort が届かなかったバッチです。各メッセージは中断後にそれぞれ独自のターンとして走るため、レシートを読まずに再送すると重複ターンになります。リストの解釈には注意点があり、UUID つきで enqueue されたメッセージのみが載る（空配列＝他に何も走らない、ではない）、メインスレッド宛のみでサブエージェント宛は対象外、スケジュールドタスクのトリガなど自分が送っていない UUID が混ざりうる（未知の UUID は無視する）、とされています。レシートは中断処理時点のスナップショットで、クリーンな中断では中断されたターンの `SDKResultMessage` より前に届くため、結果を待ってからキューを覗くのでは間に合いません。v2.1.205 より前の CLI は空の成功ペイロードを返すので `interrupt()` は `undefined` で解決します。

これに伴い `SDKSystemMessage` に省略可能な `capabilities?: string[]` が追加されました。この配列は CLI が実装しているプロトコル挙動の名前を並べたもので、`claude_code_version` の文字列比較ではなく能力名で機能検出することが推奨されます。開いた集合なので未知の値は無視し、依存する挙動の能力名を個別に確認します。現時点で定義されているのは `interrupt_receipt_v1` のみです。同じ `capabilities` 配列は headless（`docs/en/headless`）の `system/init` イベントにも現れると明記されました。あわせて `SDKMessageOrigin` の `peer` バリアントに `name` と `body` が追加され（送信者の表示名は Unicode 制御文字などを除去して 64 コードポイントで打ち切り、`body` は peer エンベロープを剥がしたモデルが見るままの本文）、`ExitPlanModeInput.allowedPrompts` は非推奨・無視となりました（既存の呼び出し元とトランスクリプトが検証を通るよう受理はされます）。

- [Agent SDK reference - TypeScript (SDKControlInterruptResponse) - Claude Code Docs (English)](https://code.claude.com/docs/en/agent-sdk/typescript#sdkcontrolinterruptresponse)

> 本節の追加は en 側のみで、日本語版 agent-sdk/typescript ページが本サマリ作成時点で当該追加を反映しているか確認できないため、安全側で日本語リンクを省略しています。

## 新規追加されたページ

<!-- light:new-pages:start -->
今回、リファレンス系で新規追加されたページ（新規ページファイル）はありません。`llms.txt` にエントリの増減はなく、変更はいずれも既存ページ本文の改稿と changelog へのリリース追加です。ページ見出しマップ（`claude_code_docs_map.md`）には、desktop ページの「Browse external sites」節、errors ページの「Plugin errors」節などが新しい見出しとして追加されています。
<!-- light:new-pages:end -->

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
上記ハイライト以外に、以下のページで本文の実体的な追加を伴う更新がありました（いずれも v2.1.205 の変更がドキュメント本文へ反映されたものです）。

- [**`/doctor` がセットアップ点検スキルに**](#1-doctor-がセットアップ点検スキルに):  
  `/doctor` が読み取り専用の診断画面から、問題を検出して修正まで提案する bundled skill の「セットアップ点検」になり、`/checkup` がそのエイリアスになった。読み取り専用の診断はターミナルの `claude doctor` に分離。commands / skills / cli-reference / env-vars / keybindings ほか多数のページが追随。
- [**エラーリファレンス: コマンドラインエラーとプラグインエラーの節を新設**](#2-エラーリファレンス-コマンドラインエラーとプラグインエラーの節を新設):  
  `--json-schema` の無効スキーマ、`claude mcp add-from-claude-desktop` のインポート失敗、予約名マーケットプレイスの信頼性エラーの 3 節が追加され、ダウンロードのタイムアウトとモデルファミリーエイリアス制限の説明も加わった。
- [**agent view: 行サマリとプルリクエストリンクの刷新**](#3-agent-view-行サマリとプルリクエストリンクの刷新):  
  行サマリが生のツール呼び出しではなくセッション自身の一行報告を表示し、モデル呼び出しなしの 15 秒更新とターン中の再生成が分離された。既存 PR を編集・コメント・クローズしたセッションも PR にリンクされ、peek パネルは完全なステータス文から開くようになった。
- [**MCP: 予約サーバ名の拡大と接続失敗のモデルへの通知**](#4-mcp-予約サーバ名の拡大と接続失敗のモデルへの通知):  
  予約サーバ名が `workspace` に加えて `claude-in-chrome` / `computer-use` / `Claude Preview` / `Claude Browser` に拡大。設定済みサーバが接続に失敗すると、その事実と接続エラーが Claude に伝えられるようになった。
- [**auto mode の既定ブロック追加とドキュメント反映**](#5-auto-mode-の既定ブロック追加とドキュメント反映):  
  権限モードページに「v2.1.205 以降も既定でブロックする」項が追加され、セッショントランスクリプトへの書き込みと、会話中に代入が見えない変数を対象とする `rm -rf "$VAR"` 系の再帰強制削除が既定ブロックに加わった。
<!-- light:updated-pages:end -->

## 1. `/doctor` がセットアップ点検スキルに

前回のサマリでは changelog 由来の一行として報告していた `/doctor` の刷新が、今回ドキュメント本文へ全面的に反映されました。`/doctor` は状態アイコン付きの読み取り専用診断画面（`f` で Claude に修正させる）ではなくなり、[bundled skill](https://code.claude.com/docs/en/skills#bundled-skills) の「セットアップ点検」になりました。インストールの健全性（重複・残存インストール、`PATH` の問題、パースできない設定ファイル）を検査し、未使用の skill / MCP サーバ / プラグインをそのコンテキストコストと突き合わせ、ローカルの `CLAUDE.md` を checked-in のものと重複排除し、常時ロードされる指示を skill や必要時ロードのネスト `CLAUDE.md` へ移し、遅い hook を指摘し、新バージョンの有無を確認します。auto mode を既定にすることや、頻繁に拒否している読み取り専用コマンドの事前承認も提案します。いずれも**まず検出結果を報告し、変更前に確認を求める**設計です。エイリアスは `/checkup`。

ターミナル側には読み取り専用の `claude doctor` が CLI サブコマンド表に明記され、セッションを起動せずにインストール診断・設定ファイル検証エラー・Remote Control 適格性を出力します。この分離に伴い、多数のページで `/doctor` への参照が書き換えられました。設定ファイルのエラー詳細（`/status` からの案内）、hook のスキーマエラー報告、SSL 証明書エラーのメッセージ内案内、WSL 検索の Note などは `claude doctor` を指すようになり、`apiKeyHelper` のエラー報告先は `/doctor` から `/status` へ、sandbox の `tlsTerminate` 未設定の報告からは `/doctor` の記述が消えました。プラグイン依存関係のスキップや keybindings の警告も `/doctor` からは案内されなくなり、キーバインドリファレンスからは `Doctor` コンテキストと `doctor:fix` アクションが削除されています。`disableBundledSkills` を有効にしても `/doctor` だけは打鍵可能なままで、隠すには `DISABLE_DOCTOR_COMMAND` 環境変数か `skillOverrides` の `"doctor": "off"` を使います。

- [Extend Claude with skills (Bundled skills) - Claude Code Docs (English)](https://code.claude.com/docs/en/skills#bundled-skills)

> 本節の各更新は en 側のみで、日本語版 skills / commands ページが本サマリ作成時点で当該記述を反映しているか確認できないため、安全側で日本語リンクを省略しています。

## 2. エラーリファレンス: コマンドラインエラーとプラグインエラーの節を新設

エラーリファレンス（`docs/en/errors`）に 3 つの節が新設されました（v2.1.205）。「The --json-schema value is not a valid JSON Schema」は、非対話モードで `--json-schema` に渡したスキーマが JSON Schema としてコンパイルに失敗し、プロンプトを実行せず終了コード 1 で終わるケースです。コロン以降がバリデータの診断で、失敗したキーワードや位置を示します。`"format": "email"` のように `format` キーワードを使うスキーマは**有効**で、Claude Code は `format` を注釈として受理し強制はしません。スキーマコンパイル前に 2 つの検査（パースできない値は `--json-schema is not valid JSON`、オブジェクトでない値は `--json-schema must be a JSON object`）が走ることも明記されました。「Could not import a server from Claude Desktop」は `claude mcp add-from-claude-desktop` で一部サーバの追加に失敗した場合で、失敗したサーバごとに 1 行を出力しつつ**残りのサーバは取り込む**ようになりました（v2.1.205 より前は最初の失敗で取り込み全体が停止していました）。最も多い原因はサーバ名の文字種で、Claude Desktop が許すスペースやピリオドを `claude mcp` は許しません。

さらに「Plugin errors」というカテゴリ節ごと新設され、その配下に「Marketplace is registered from an untrusted source」が置かれました。公式 Anthropic マーケットプレイス向けに予約された名前で登録されているのに、登録元が `anthropics` の GitHub リポジトリでない場合に出るエラーです。Claude Code は**マーケットプレイスをロード／リフレッシュするたびに**予約名を再検査するようになったため、名前が予約される前に登録されたエントリもロードされなくなります（v2.1.205 より前は追加時にのみ検査していました）。マーケットプレイスの予約名リストには `first-party-plugins` と `healthcare` が追加されています。エラーメッセージ対応表にも、`Download timed out: exceeded the total deadline`（接続は維持しつつ 10 分以内に終わらないダウンロード。リトライしない）と上記 3 件の行が加わりました。

- [Error reference (Marketplace is registered from an untrusted source) - Claude Code Docs (English)](https://code.claude.com/docs/en/errors#marketplace-is-registered-from-an-untrusted-source)

> 本節の追加は en 側のみで、日本語版 errors ページが本サマリ作成時点で当該追加を反映しているか確認できないため、安全側で日本語リンクを省略しています。

## 3. agent view: 行サマリとプルリクエストリンクの刷新

agent view ページ（`docs/en/agent-view`）の行サマリ・PR ステータス・peek パネルの記述が v2.1.205 に合わせて書き換えられました。作業中の行は、モデルへリクエストを送らずセッション自身の直近出力から最大 15 秒に 1 回テキストを更新し、ターン終了時に Haiku 級モデルが新しいサマリを書きます。長いターンの途中でもモデルは約 1 分ごと（再生成のたびに待機を倍増させ最大 4 分まで）にサマリを書き直すため、忙しい行が古いサマリを表示し続けることがありません。テキストは 64 桁で切り詰められ、全文は peek パネルで読みます。ディレクトリでグループ化しているときは行頭に色付きの状態語（例: `Needs input · double jump or wall climb?`）が付きます。v2.1.205 より前は、作業中の行が報告ではなく生のツール呼び出しを表示することがあり、並列作業がある行には `2/5` のような `done/total` が付いていました。文字も数字も含まないターン（`/loop` が記号だけを出力した回など）は行の以前のサマリと状態を保つようになり、入力待ちのセッションが `Working` に戻ってしまう問題が解消されています。

プルリクエストのリンク付けも拡張されました。既存の PR に対して `gh` で編集・コメント・クローズ・ready 化を行ったセッションも、そのコマンドの出力が名指しした PR にリンクされます（出力が PR を名指ししない `gh pr merge` などは対象外）。`gh pr checkout` や、オープンな PR を持つブランチへの push は `gh pr view` でそのブランチを引いてリンクします。インライン上限（約 30,000 文字）を超えてファイルへ保存された出力からも PR を読み取るようになりました。peek パネルは、行が切り詰めたステータス文の全文とその経過時間から開き、続いてリンク済み PR を並べ、入力待ちのセッションでは返信欄の上に実際の質問を表示します。加えて `claude attach` は、supervisor がセッションを再起動している最中（更新・ストール・マイグレーション）に失敗せず、`Agent is updating to the new Claude Code…` のようなステータス行を出して約 60 秒まで待つようになりました。

- [Manage multiple agents with agent view (Row summaries) - Claude Code Docs (English)](https://code.claude.com/docs/en/agent-view#row-summaries)

> 本節の各更新は en 側のみで、日本語版 agent-view ページが本サマリ作成時点で当該記述を反映しているか確認できないため、安全側で日本語リンクを省略しています。

## 4. MCP: 予約サーバ名の拡大と接続失敗のモデルへの通知

MCP ページ（`docs/en/mcp`）で、Claude Code 組み込みサーバ向けの予約名が `workspace` だけでなく `claude-in-chrome` / `computer-use` / `Claude Preview` / `Claude Browser` に広がったことが明記されました（v2.1.205）。予約名のサーバが設定にあるとロード時にスキップされ、改名を促す警告が出ます。`claude mcp add` は予約名をエラーで拒否します。`Claude Preview` と `Claude Browser` はどちらも Desktop アプリのプレビューペインが使う組み込みサーバを指す名前で、v2.1.205 より前は `Claude Browser` が予約されておらずユーザー定義サーバが登録できてしまっていました。Claude Desktop からのインポートについても、`claude mcp` 経由で追加するサーバ名は英数字・ハイフン・アンダースコアのみである旨と、拒否した名前を報告しつつ残りは取り込む挙動が追記されています。

接続失敗の扱いも変わりました。設定済みサーバが接続に失敗した場合、Claude Code は**どのサーバが失敗し何のエラーだったかを Claude に伝える**ようになり、マッチするツールが見つからなかった `ToolSearch` の結果にもそれが含まれます。これにより Claude は応答内で接続失敗を報告できます。この挙動には既定で有効な tool search が必要で、tool search が無い構成（カスタム `ANTHROPIC_BASE_URL`、`ENABLE_TOOL_SEARCH=false`、Haiku モデル）や Amazon Bedrock / Google Cloud's Agent Platform / Microsoft Foundry では失敗が Claude に伝わりません。v2.1.205 より前は接続エラーが Claude に渡されず、失敗したサーバのツールが最初から設定されていなかったかのように応答することがありました。

- [Connect Claude Code to tools via MCP (Managing your servers) - Claude Code Docs (English)](https://code.claude.com/docs/en/mcp#managing-your-servers)

> 本節の各更新は en 側のみで、日本語版 mcp ページが本サマリ作成時点で当該記述を反映しているか確認できないため、安全側で日本語リンクを省略しています。

## 5. auto mode の既定ブロック追加とドキュメント反映

権限モードページ（`docs/en/permission-modes`）の「What the classifier blocks by default」に、「Claude Code v2.1.205 以降も既定でブロックする」項が新設されました。1 つ目は **Claude Code のセッショントランスクリプトへの書き込み**です。`~/.claude/projects/` 配下（または設定した config ディレクトリ）の `.jsonl` 履歴ファイルへ、直接またはシェルコマンド経由で書き込む行為が対象で、Claude Code が各エントリに付けるメタデータ行も含みます。トランスクリプトは作業ファイルではなく Claude Code が書くセッション状態であり、改竄されたエントリはセッション再開後の全チェックに影響するため、多層防御としてブロックされます。読み取りはブロックされません。2 つ目は、**会話中のどこにも代入が見えない変数を対象とする再帰強制削除**（`rm -rf "$VAR"` や `Remove-Item -Recurse -Force $dir`、およびそれを起点とする glob）です。値がコマンド出力からしか来ておらず、分類器はコマンド出力を受け取らない設計であるため削除対象を検証できず、推測せずブロックします。削除対象の正確なパスを名指しするか、Claude が解決済みのリテラルパスで再実行すればブロックは解けます。

同ページの auto mode 分類器の入力についても記述が精緻化されました。リポジトリの可視性は、リモートのホストと名前が示すか、**分類器が読める会話中の可視性チェック**が公開であることを示さない限りプライベートとみなされます。分類器が読むのはユーザーのメッセージと Claude が実行したコマンドであって**その出力ではない**ため、`gh repo view` を実行しただけではその結果は分類器に届かず、「このリポジトリは公開だ」というユーザー自身のメッセージのような、分類器が読める形の根拠が必要です。あわせて権限モード表の `plan` の説明から "Plan Mode" というラベルが外れ、CLI と VS Code 拡張での表示名が「Plan」であることが明記されました。

- [Choose a permission mode (What the classifier blocks by default) - Claude Code Docs (English)](https://code.claude.com/docs/en/permission-modes#what-the-classifier-blocks-by-default)

> 本節の変更は en 側のみで、日本語版 permission-modes ページが本サマリ作成時点で当該変更を反映しているか確認できないため、安全側で日本語リンクを省略しています。

## 軽微な更新

<!-- light:minor-updates:start -->
今回の軽微な更新は、changelog に追加された v2.1.206 由来の修正群と、v2.1.205 の変更が各リファレンスページ本文に反映されたことによる小規模な追記が中心です。ハイライト・大幅更新で扱った項目は再掲せず、それ以外を分類して挙げます。バージョンは項目ごとに併記します。

**新機能**

- 非対話モード専用のフラグ `--append-subagent-system-prompt` が追加され、ネストしたものを含む全サブエージェントのシステムプロンプト末尾に任意のテキストを追記できるようになった。フラグが環境変数 `CLAUDE_CODE_ENABLE_APPEND_SUBAGENT_PROMPT` を自動で設定する（v2.1.205）。 — [日本語](https://code.claude.com/docs/ja/cli-reference#cli-flags) / [English](https://code.claude.com/docs/en/cli-reference#cli-flags)
- `claude doctor` が CLI サブコマンド表に追加され、セッションを起動せずインストール診断・設定ファイル検証エラー・Remote Control 適格性を出力することが明記された（v2.1.205）。 — [English](https://code.claude.com/docs/en/cli-reference#cli-commands)
- プラグイン LSP サーバ設定に `restartOnCrash`（既定 `true`）と `shutdownTimeout` が使えるようになった。v2.1.205 より前はスキーマ上は受理されつつ、いずれかを設定するとそのサーバが起動時に丸ごとスキップされていた（v2.1.205）。
- サブエージェント用ステータスライン hook の各タスクに `model`（解決済みモデル ID）と `contextWindowSize`（そのモデルのコンテキストウィンドウ）が渡るようになり、行ごとの使用率を描画できるようになった（v2.1.205）。
- 管理設定に `browserExternalPageTools` が追加され、Desktop の Browser ペインでの外部ページ上のツール利用を無効化できるようになった（詳細はハイライト 1 参照）。 — [日本語](https://code.claude.com/docs/ja/settings#available-settings) / [English](https://code.claude.com/docs/en/settings#available-settings)
- `/usage-credits` が、SSH 経由などブラウザを開けない環境では課金ページの URL をテキストで表示するようになった。v2.1.205 より前はその場合に何も表示されなかった（v2.1.205）。 — [English](https://code.claude.com/docs/en/commands#all-commands)

**機能改善**

- モデル既定 effort の保持がセッションを跨いで維持され、`/effort` の実行や `--effort` 付き起動といった明示的な選択があるまで解除されないことが明記された（v2.1.205）。 — [日本語](https://code.claude.com/docs/ja/model-config#adjust-effort-level) / [English](https://code.claude.com/docs/en/model-config#adjust-effort-level)
- 構造化出力で、無効な JSON Schema は起動時にエラーで失敗するようになり、`format` キーワードは注釈として受理され SDK のバリデータでは強制されなくなった。v2.1.205 より前は無効なスキーマが黙って無視され非構造化テキストが返っていた（v2.1.205）。 — [English](https://code.claude.com/docs/en/headless#get-structured-output)
- ストリーミング入力で、ターンが `--max-turns` 上限で終わるときに送信済みのメッセージがキューに残り、自身の上限を持つ独自のターンとして走るようになった。v2.1.205 より前は最終イテレーションに届いたメッセージが取り込まれ、モデルに届かないまま失われていた（v2.1.205）。
- `WorktreeCreate` hook の出力規約が精緻化された。command hook は stdout の最後の非空行にパスを出力し、Claude Code は ANSI エスケープを除去してから読む。相対パスは hook の実行ディレクトリを基準に解決され、ディレクトリとして入れなければパスを示すエラーを出して終了コード 1 で終わる。v2.1.205 より前はセッションがクラッシュし、`-p` では約 30 秒停止したのち終了コード 0 で終わっていた（v2.1.205）。
- Windows で worktree を削除する前に、内部の任意の深さにある NTFS ジャンクションやディレクトリシンボリックリンクをリンクエントリとして除去するようになり、worktree 外のファイルを消さなくなった。v2.1.205 より前はトップレベルのリンクしか扱わなかった（v2.1.205）。
- LSP サーバの重複解決が変わり、同じ拡張子を宣言する有効なサーバが複数あるときは最初に登録されたものが担当し、`/plugin` が有効なプラグイン名を示す警告を出すようになった。初期化に失敗したサーバは拡張子を占有しなくなり、同じ拡張子を扱う別の正常なサーバが処理する（v2.1.205）。
- スキル一覧のコンテキスト予算に関する記述が刷新され、`/doctor` が一覧のコンテキストコストと主な寄与要素を見積もるようになった。予算超過時はデバッグログにも警告が書かれる（v2.1.205）。 — [日本語](https://code.claude.com/docs/ja/skills#skill-descriptions-are-cut-short) / [English](https://code.claude.com/docs/en/skills#skill-descriptions-are-cut-short)
- `SendMessage` で再開したサブエージェントは同一 ID の下で新しい実行として走り、タスク一覧と Agent SDK のタスクイベントで再び running として表示されるようになった。v2.1.205 より前は再開した実行が動いている間も以前の failed / completed のままだった（v2.1.205）。
- 同一 `.claude/agents/` ディレクトリ（サブフォルダ含む）で名前が重複する場合、どれがロードされるかはファイルシステムの読み取り順であり、文書化された優先順位はないことが明記された。`/doctor` の点検が重複を報告し、1 つを残すリネーム・削除を提案する（v2.1.205）。
- npm インストーラが FreeBSD を非対応プラットフォームとして報告するようになった。v2.1.205 より前は Linux として扱い、実行できないバイナリをダウンロードしていた（v2.1.205）。
- `apiKeyHelper` の失敗・出力不正の報告先が `/doctor` 出力から `/status` 出力に変わった（v2.1.205）。
- サンドボックスのクレデンシャルマスキングで `network.tlsTerminate` 未設定時の誤設定報告から `/doctor` の記述が削除され、起動時報告のみになった。あわせて説明文が「HTTPS を終端」から「TLS を終端」に修正された（v2.1.205）。
- `/code-review` の指摘品質が claude-opus-4-8 の全 effort レベルで改善され、agents view のステータス列が 64 文字で切り詰めず端末幅いっぱいを使うようになり、`Ctrl+X` で完了セッションを恒久的に削除できるようになった（セッションの二重描画も解消。v2.1.206。詳細はハイライト 2 参照）。
- プラグインの警告先が `/doctor` から移った。依存関係の解決スキップは `/plugin` の Errors タブに、マニフェストと既定フォルダの重複による無視フォルダの警告は `claude plugin list` と `/plugin` の詳細ビューに、それぞれ集約された（v2.1.205）。

**バグ修正**

- 期限切れのログインが、`/login` を促さず全モデルで `There's an issue with the selected model` という誤解を招くエラーになる問題を修正（v2.1.206）。
- `claude --resume` / `--continue` が起動時にキーボード入力へ反応しない問題、および Windows で `claude --resume` の前にセットアッププロンプトが出るとエージェントビューで入力が無視される問題を修正（v2.1.206）。
- `--mcp-config` や `.mcp.json` で設定した per-server の `request_timeout_ms` が無視され、長時間の MCP ツール呼び出しが新規セッションで 60 秒の既定値でタイムアウトする問題を修正（v2.1.206）。
- シェルでエクスポートした `CLAUDE_CODE_EXTRA_BODY` が `claude agents` / `--bg` のバックグラウンドワーカーで黙って無視される問題を修正（ディスパッチ元セッションに追従するように。v2.1.206）。
- OAuth の MCP サーバが 1 度のトークン更新失敗で手動再認証を要求する問題、および `--permission-prompt-tool` が MCP サーバを指すときサーバ接続完了前のコールドスタートで `MCP tool not found` としてクラッシュする問題を修正（v2.1.206）。
- `/model` ピッカーが行の名前と異なるモデルの価格を表示する問題を修正し、一次課金されないプロバイダでの定価表示をやめた。エンタイトルメントや許可リストで基準行が落ちたときにサーバ提供のモデル行が誤配置される問題も修正（v2.1.206）。
- デスクトップセッションがターン中に送られたスラッシュコマンドの後に `running` 表示のまま固まる問題を修正（v2.1.206）。
- `claude rm` が削除済みジョブを daemon の roster に残し、`claude agents` に行が再出現する問題を修正（v2.1.206）。
- ログアウト状態で `/remote-control` が `Unknown command` を表示する問題（サインイン方法を案内するように）、左矢印がワークフロー詳細ビューでフェーズやエージェントから戻れない問題、`/status` が同じ壊れたインストール警告を 2 度並べる問題を修正（v2.1.206）。
- LSP プラグインに対する誤った「未使用プラグイン」ヒントと歪んだ未使用テレメトリを修正（v2.1.206）。
- `/doctor` の更新チェックが Homebrew インストールを設定チャンネルではなく cask のチャンネルと比較するよう修正（v2.1.206）。
- フルスクリーンの jump-to-bottom ピルが macOS で `Ctrl+End` を提案する、再割り当てしたコードを表示しない、トランスクリプトの上に折り返す問題を修正（v2.1.206）。
- Bedrock で `awsCredentialExport` ヘルパーを使うとき、egress が制限されたネットワークで数分間の起動ハングが起きる問題を修正（v2.1.206）。

**その他**

- Desktop の 3P 実行環境の呼称が「Cowork on 3P research preview」から「Claude Desktop on 3P」に変わり、URL が `claude.com/docs/cowork/3p/...` から `claude.com/docs/third-party/claude-desktop/...` へ移った。desktop / llm-gateway / llm-gateway-rollout / third-party-integrations など複数ページで一括置換されている。
- 権限モードの表示ラベルが整理され、Desktop・VS Code 拡張・claude.ai・Remote Control の各面で `Ask permissions` → `Manual`、`Auto accept edits` → `Accept edits`、`Plan mode` → `Plan`、`Auto mode` → `Auto` に統一された（v2.1.205）。旧ラベルを使っていた quickstart・desktop-quickstart・claude-code-on-the-web・interactive-mode などの記述も追随している。
- ページ見出しマップ（`claude_code_docs_map.md`）から keybindings の `Doctor actions` が削除され、desktop に `Browse external sites`（および配下 3 節）、errors に `The --json-schema value is not a valid JSON Schema` / `Could not import a server from Claude Desktop` / `Plugin errors` / `Marketplace is registered from an untrusted source`、agent-sdk/typescript に `SDKControlInterruptResponse` が追加された。
- 公式 changelog ページに v2.1.206（2026年07月09日）のリリースエントリが追加された（changelog ページ自体へのリンクは方針により張らない）。
<!-- light:minor-updates:end -->

## 新着情報

<!-- light:whats-new:start -->
今回、週刊ダイジェスト「新着情報」（`whats-new/`）ページの新規追加・本文変更はありません（差分内に `whats-new/` を含む変更は 0 件。`llms.txt` にも `whats-new/` の新規エントリはありません）。今回 changelog に追加された v2.1.206 の内容と、本文へ反映された v2.1.205 の変更は、ハイライト・大幅更新・軽微な更新に振り分けています。
<!-- light:whats-new:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-07-08.md](./archives/latest/2026-07-08.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-07-08.md](./archives/latest-detail/2026-07-08.md)

<!--
base_commit: c5b9ea9f9b938819036015f5beec69baf4c1cbc7
head_commit: 191b578e6d5aaae6bbcc47aa5f1ddd0d3e85ea4a
generated_at_full: 2026-07-10T15:02:05+09:00
-->
