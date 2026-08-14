---
対象期間: 2026年08月12日 〜 2026年08月13日
作成日: 2026-08-13
---

# Claude Code 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
今回の対象期間は 76 ページに差分がありました。新規ページと新着情報はありません。中心は v2.1.232 のリリースで、サブエージェントのフォークが対話セッションの既定になり、他のセッションをメンションで名指しできるようになりました。あわせて「まだ信頼していないフォルダで何が動くか」を一覧にした表が権限のページに新設され、そこへの参照が十数ページに張られています。

主要なものを以下に挙げます。

1. フォークモードが対話セッションで既定 ON になり、環境変数の意味も反転した
2. 信頼していないフォルダでリポジトリの何が動くかが、セッション種別ごとの表にまとまった
3. ローカルコマンドが出力したディレクトリからプラグインを入れる command ソースが文書化された
4. 設定の優先順位の説明が、例外・管理階層内の順位・親設定の 3 つの節に分けて書き直された
5. 入力欄で他のセッションをメンションでき、同名セッションは自動で別名に変わるようになった
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**フォークが対話セッションの既定になった**](#1-フォークが対話セッションの既定になった):  
  対話セッションではフォークモードが既定で有効になり、Claude が自分でフォークを起動できるようになった。`CLAUDE_CODE_FORK_SUBAGENT` は「有効にする変数」ではなく既定を上書きする変数に変わり、`1` は `-p` と SDK でも有効化、`0` は全セッションで無効化を意味する。
2. [**信頼していないフォルダで何が動くかが表で一覧化された**](#2-信頼していないフォルダで何が動くかが表で一覧化された):  
  権限のページに、リポジトリが供給しうる内容ごとに「親フォルダだけ信頼した場合」「`-p`/SDK で一度も信頼していない場合」の 2 列で挙動を示す表が新設された。設定ファイルのフックは `-p` では動き、サブエージェントのフロントマターのフックは動かない、といった差が明示されている。
3. [**コマンド出力からプラグインを入れる command ソースが追加された**](#3-コマンド出力からプラグインを入れる-command-ソースが追加された):  
  マーケットプレイスのエントリにローカルコマンドを書き、そのコマンドが標準出力に印字したディレクトリをプラグインとして扱う `command` ソースが文書化された。セッションごとに 1 度再実行され、出力が変われば新バージョンとして入り直す。
4. [**設定の優先順位が 3 つの節に分けて書き直された**](#4-設定の優先順位が-3-つの節に分けて書き直された):  
  1 つの長い箇条書きだった「設定の優先順位」が、管理設定の例外・管理階層内の順位・埋め込みホストの親設定という 3 つの節に分割され、例外キーは表になった。参照していた十数ページのアンカーも一斉に張り替えられている。
5. [**他のセッションをメンションで名指しできるようになった**](#5-他のセッションをメンションで名指しできるようになった):  
  入力欄で `@` に続けて 1 文字以上打つと同一マシンの他セッションが候補に出て、選ぶとその宛先が Claude に伝わる。あわせて、既に使われている名前で対話セッションを起動・改名すると自動で別名の変種が付くようになった。
<!-- light:highlight-list:end -->

## 1. フォークが対話セッションの既定になった

サブエージェントのページに **フォークモードのオン/オフを切り替える** という節が新設され、既定値が明記されました。フォークモードは対話セッションでは既定で有効、`-p` の非対話モードと Agent SDK では既定で無効です。対話セッションでの既定 ON は Claude Code v2.1.232 以降が前提で、それより前のバージョンでは `CLAUDE_CODE_FORK_SUBAGENT` を `1` にする必要があります。有効かどうかは Agent ツールの扱いで見分けられ、有効なときは Claude が `fork` サブエージェントタイプを要求してフォークを起動でき（タイプを指定しなければ従来どおり general-purpose、Explore などの名前付きサブエージェントもそのまま）、Claude が起動したサブエージェントはフォークも名前付きも一律バックグラウンドで動き、Agent ツールから `run_in_background` パラメータ自体が取り除かれるためフォアグラウンドを要求できなくなります。

環境変数の意味も変わりました。従来 `CLAUDE_CODE_FORK_SUBAGENT` は「フォークを許可する変数」でしたが、今回からは既定を上書きする変数として説明され、`1` は非対話モードと Agent SDK でも有効化、`0` は全セッションで無効化を意味します。フォークモードは残したまま Claude にフォークを起動させたくない場合は、`Agent(fork)` の拒否ルールで `fork` タイプだけを拒否できる（サブエージェントはバックグラウンドで動いたままになる）とも書かれました。フォアグラウンドとバックグラウンドの判定も、先に当てはまったものが勝つ 4 つの場合に整理されています。`CLAUDE_CODE_DISABLE_BACKGROUND_TASKS` が `1` ならセッション種別とフォークモードに関係なくフォアグラウンド、エージェントチームのチームメイトが起動したものもフォアグラウンド、フォークモードが有効ならバックグラウンド固定、無効なら従来どおり既定はバックグラウンドで Claude が結果を先に必要とするときだけフォアグラウンド、という順です。フロントマターの `background` フィールドも「Claude がフォアグラウンドを要求してもバックグラウンドに留める」という位置づけに書き直され、フォークはさらにフォークを生成できないという制約が「会話をフォークする」節の本文へ移りました。

- [Create custom subagents - Claude Code Docs (English)](https://code.claude.com/docs/en/sub-agents#turn-fork-mode-on-or-off)
- [Create custom subagents - Claude Code Docs (English)](https://code.claude.com/docs/en/sub-agents#run-subagents-in-foreground-or-background)

## 2. 信頼していないフォルダで何が動くかが表で一覧化された

権限のページの **プロジェクトの許可ルールとワークスペーストラスト** が 3 つに分けられ、配下に **ローカル設定ファイルがトラストを必要とする場合** と **フォルダを信頼する前に何が動くか** が新設されました。後者は、リポジトリが供給しうる内容を行に、信頼していない 2 つの状況（親フォルダだけを信頼した場合と、トラストダイアログが出ない `-p`/SDK でそのフォルダを一度も信頼していない場合）を列に取った表です。設定ファイル内のフック・`env` ブロック・`apiKeyHelper` などのヘルパーコマンド・プロジェクトスキルのフックと `allowed-tools` は**どちらの状況でも使われ**（スキルの `allowed-tools` はどのセッションでもワークスペーストラストの対象外）、`.claude/settings.json` の `permissions.allow` と `additionalDirectories` はどちらでも使われません（`-p` では `this workspace has not been trusted` が標準エラーに出ます）。プロジェクトのサブエージェントのフロントマターのフック・プロジェクトの `@skills-dir` プラグイン・リポジトリや `--add-dir` 由来の `extraKnownMarketplaces` は、どちらの状況でも使われずダイアログも出ません。`.mcp.json` のサーバーは、親フォルダだけ信頼した場合は接続前に確認され（リポジトリが自分の設定で承認していても数えられない）、`-p` では承認の有無に関わらず確認なしで接続されます。ダイアログが出ない行を手で信頼するには `~/.claude.json` の `projects["<path>"].hasTrustDialogAccepted` を `true` にする、という手順も添えられました。

フックのページにも **ワークスペーストラスト** の節が新設され、対話セッションでは自分の `~/.claude/settings.json` を含むあらゆる設定ファイルのフックがダイアログ受諾まで保留されるのに対し、`-p`/SDK セッションではダイアログが出ずフォルダは信頼済みとして扱われる、と明記されました。書いた覚えのないリポジトリで `claude -p` を回す前の選択肢として、`--setting-sources user`（SDK なら `settingSources` からプロジェクト設定を外す）、`--bare` での起動、`--settings '{"disableAllHooks": true}'`、`disabledMcpjsonServers` の 4 つが挙げられています。`disableAllHooks` は設定の優先順位を適用した後の値を読むため、ユーザー設定に `true` を書いてもプロジェクト設定の `false` に上書きされうる、という注意も加わりました。`.claude/settings.local.json` の扱いも整理され、git で追跡されているか `.claude` がシンボリックリンクのときにリポジトリ由来として保留されること、その判定の git 実行自体がトラスト受諾後（`-p`/SDK は受諾扱い）にしか走らないこと、自分の設定ホームだけは git を使わないため即座に適用されることが述べられています。この整理に合わせて、スキル・ステータスライン・メモリ・`/goal`・`gcpAuthRefresh`・MCP の `headersHelper` など各所の「トラストダイアログを受け入れた後に」という記述が、新設節への参照に置き換えられました。

- [Configure permissions - Claude Code Docs (English)](https://code.claude.com/docs/en/permissions#what-runs-before-you-trust-a-folder)
- [Hooks reference - Claude Code Docs (English)](https://code.claude.com/docs/en/hooks#workspace-trust)

## 3. コマンド出力からプラグインを入れる command ソースが追加された

プラグインマーケットプレイスのページに **コマンドソース** の節と 3 つの小節が新設されました。`command` は、ローカルにインストールされたツールがプラグインディレクトリを生成する場合に使うソースで、Claude Code v2.1.229 以降が必要です（v2.1.120〜v2.1.228 ではインストールがサポート外エラーになり、それ以前ではマーケットプレイス全体の読み込みに失敗します）。コマンドはプラットフォームのシェル（macOS/Linux は `sh`、Windows は `cmd.exe`）でユーザーのホームディレクトリから実行され、標準出力にちょうど 1 行、終了時点で完全なプラグインを含むディレクトリの絶対パスを印字して終了コード 0 で終わる必要があります。パスは実行ごとに変わって構いません。`timeout`（既定 60 秒・最大 600 秒）を超えるとインストールは失敗し、印字されたパスがトップレベルにプラグインらしい中身を持たない場合、Claude Code を起動したディレクトリかその親だった場合、Windows で UNC パスだった場合も拒否されます。`command` フィールド自体にも制約があり、ユーザーが受け入れる前に全文を読めるよう、印字可能な ASCII・500 文字以内・4 つ以上連続する空白を含まないことが求められます。

配下の 3 小節は、コピーとリンク・受け入れ・再実行を扱います。既定の `"mode": "copy"` では印字されたディレクトリをバージョン付きキャッシュへ複製し、内容のハッシュをプラグインのバージョンにします（256 MiB 超または 20,000 エントリ超は拒否）。`"mode": "link"` はトップレベルの各エントリへのリンクをキャッシュエントリに置いてその場のファイルを使うため、複製もハッシュ計算もサイズ上限もなく、Node.js の依存インストールも省かれます。代わりに印字先のディレクトリを置いたままにする必要があり、バージョンは実パスとトップレベルのエントリから導かれ、印字先ディレクトリ配下で始めたセッションではプラグインが読み込まれません（Windows は link 非対応）。受け入れは、`/plugin` の詳細画面や対話ターミナルでの `claude plugin install` / `claude plugin update` でコマンド文字列そのものを提示して記録する方式で、非対話シェルでは `--yes` を渡します。それ以外の経路は受け入れ済みのコマンドしか実行せず、他プラグインの依存として自動導入されることもありません。マーケットプレイス側で `command` や `mode` を変えると再実行は止まり、ユーザーが `claude plugin update` で確認するまで従来のバージョンが使われます。再実行の契機はインストール・更新のたび、セッション開始直後のバックグラウンドで 1 回、キャッシュに該当バージョンが無い起動時と `/reload-plugins` 時で、バックグラウンドの 2 つは `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` で止まります。出力のハッシュが変われば新バージョンとして導入され、実行中の対話セッションでもリロードされます（プロンプトキャッシュが無効化される場合は `/reload-plugins` の実行を促す形に切り替わります）。管理者は `disableCommandPluginSources` で組織全体を止められ、`allowManagedHooksOnly` を設定した組織では既定でコマンドソースが無効になります。

- [Create and distribute a plugin marketplace - Claude Code Docs (English)](https://code.claude.com/docs/en/plugin-marketplaces#command-sources)
- [Create and distribute a plugin marketplace - Claude Code Docs (English)](https://code.claude.com/docs/en/plugin-marketplaces#when-claude-code-re-runs-the-command)

## 4. 設定の優先順位が 3 つの節に分けて書き直された

設定のページの **設定の優先順位** は、管理設定から順に 5 段を並べた 1 つの長い箇条書きでしたが、今回 5 段の一覧を素直な列挙に戻したうえで、細部を 3 つの小節へ切り出しました。**管理設定の優先順位の例外** は、管理設定を上書きできないはずのスコープからの制限的な値を尊重するキーを表にしたもので、`disableClaudeAiConnectors` と `isolatePeerMachines` はどのスコープの `true` も、`remoteControlAtStartup` は `.claude/settings.json` / `.claude/settings.local.json` の `false` を、`crossSessionInbound` は同 2 ファイルの `accept` < `hold` < `refuse` の梯子でより厳しい値を尊重する、と整理されています。`CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST` を立てる埋め込みホストが例外である旨も、この節の末尾へ移りました。

**管理階層内の優先順位** は、リモート設定 → MDM/OS ポリシー → 管理設定ファイル → HKCU レジストリ（Windows のみ）の順で、空でない設定を配ってきた最初のソースだけを使い残りはマージせず無視する、という順位を番号付きで示します。どの管理ソースが設定しても尊重される横断キー（サンドボックスのロックキー・`allowAllClaudeAiMcps`・サンドボックスのバイナリパス・`forceRemoteSettingsRefresh`・変数ごとにマージされる `env`）も同じ節にまとまりました。**埋め込みホストからの親設定** は、管理ソースがある場合に既定で親設定を無視すること、`parentSettingsBehavior` を最上位の管理ソースで `"merge"` にしたときの制限的フィルタと、`allowManaged*Only` を立てない限り許可方向の設定が通ってしまうという穴を扱います。`policyHelper` の説明にも加筆があり、`managedSettings` を出力したときはそれが唯一の管理ソースになって横断キーもそこからだけ読み、親設定は一切マージされないこと、`managedSettings` を出さずに 0 で終了したヘルパーは管理設定に何も寄与しないことが明記されました。

このほか設定キーも増えました。コマンドソースを組織的に止める `disableCommandPluginSources`（管理設定専用。未設定なら `allowManagedHooksOnly` に従う）と、サブエージェントのタスク表示の行を書き換える `subagentStatusLine` が追加され、`dialogExpiry` と `crossSessionInbound` は `/config` の行（**Dialog expiry** / **Messages from your other sessions**）から書けるようになりました（v2.1.232 以降。`--settings` や管理設定がそのキーを設定している間は行が隠れます）。フック設定の節も広がり、`allowManagedHooksOnly` はローカルのフックもブロックすること、コマンドソースのプラグインを無効化すること、`statusLine` / `fileSuggestion` / `subagentStatusLine` を管理設定だけに絞ることが加わっています。

- [Claude Code settings - Claude Code Docs (English)](https://code.claude.com/docs/en/settings#exceptions-to-managed-settings-precedence)
- [Claude Code settings - Claude Code Docs (English)](https://code.claude.com/docs/en/settings#precedence-within-the-managed-tier)

## 5. 他のセッションをメンションで名指しできるようになった

セッション間メッセージングのページに、宛先を自分で指定する方法が加わりました。プロンプトで `@` に続けてセッション名の先頭を打つと、サブエージェントのメンションと同じ要領で同一マシンの他の稼働中セッションが候補に出ます（`@` だけではセッション行は出ず、1 文字以上打つと出ます）。選ぶと Claude Code が `@api-worker` のようなメンションを挿入し、それがどのセッションを指すかを Claude に伝えるため、Claude はセッション一覧を取らずにそのセッションへ送れます。クラウドセッションや Remote Control 経由のセッションは、Claude がこのマシンの外まで一覧・送信を済ませた後にだけ候補へ現れます。メンションされた名前に複数の稼働セッションが該当する場合は、送る前に Claude がどれかを尋ねます。Claude Code v2.1.232 以降が前提です。

名前そのものの扱いも変わりました。既に他の稼働セッションが使っている名前で対話セッションを起動・再開・改名すると、名前は先にいたセッションに残り、こちらには `auth-refactor-graceful-unicorn` のような 2 語の接尾辞が付いた変種が割り当てられて通知されます（v2.1.232 より前は両方が同じ名前を保持していました）。ただし AI 生成のタイトルや既定の表示名、バックグラウンド／`-p` セッションの `--name`、古いバージョンで動いているセッションは改名対象外なので、一覧に同名が並ぶことは依然あります。宛先の解決も、名前に該当するセッションが 1 つなら名前だけで配送し、複数該当するか全ての場所を確認できなかった場合は Claude が一覧の各行に短い識別子を付けてそれをアドレスに使う、と 2 通りに整理されました。一覧のラベルも増え、クラウドセッションには `cloud`、Remote Control の接続が切れたセッションには `offline` が付きます。

- [Message your other Claude Code sessions - Claude Code Docs (English)](https://code.claude.com/docs/en/cross-session-messaging#message-another-session)
- [Manage sessions - Claude Code Docs (English)](https://code.claude.com/docs/en/sessions#name-your-sessions)

## 新規追加されたページ

<!-- light:new-pages:start -->
（今回の対象期間に新規追加されたページはありません）
<!-- light:new-pages:end -->

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
- [**環境変数**](#1-環境変数) ([English](https://code.claude.com/docs/en/env-vars#variables)):  
  変更行数は 649 行で今回最多だが、大半は表の桁揃え。実質は 8 項目の書き換えとワークフロー用の新変数 1 件。
- [**Claude Code の設定**](#2-claude-code-の設定) ([English](https://code.claude.com/docs/en/settings#exceptions-to-managed-settings-precedence)):  
  変更行数 418 行。優先順位の節が 3 分割され（詳細はハイライト 4 参照）、設定キーとフック設定の説明も増えた。
- [**プラグインマーケットプレイスの作成と配布**](#3-プラグインマーケットプレイスの作成と配布) ([English](https://code.claude.com/docs/en/plugin-marketplaces#command-sources)):  
  `command` ソースの節が新設された（詳細はハイライト 3 参照）ほか、既存の記述もコピーされない例外に合わせて修正された。
- [**セルフホスト環境のセッションをカスタマイズする**](#4-セルフホスト環境のセッションをカスタマイズする) ([English](https://code.claude.com/docs/en/self-hosted-environments-configuration#how-each-sessions-config-is-assembled)):  
  コントロールプレーンが配るフックの置き場所が明記され、`managed-mcp.json` があるランナーの挙動も変わった。
- [**権限を設定する**](#5-権限を設定する) ([English](https://code.claude.com/docs/en/permissions#what-runs-before-you-trust-a-folder)):  
  ワークスペーストラストの節が 3 つに分かれ、セッション種別ごとの表が新設された（詳細はハイライト 2 参照）。
- [**プラグインリファレンス**](#6-プラグインリファレンス) ([English](https://code.claude.com/docs/en/plugins-reference#version-management)):  
  バージョン解決が `command` ソースとそれ以外に分かれ、`claude plugin install` / `update` に `--yes` が加わった。
- [**MCP で外部ツールに接続する**](#7-mcp-で外部ツールに接続する) ([English](https://code.claude.com/docs/en/mcp#use-pre-configured-oauth-credentials)):  
  Sentry の例が削除され、v2.1.229 のリダイレクト URI 不一致とその復旧手順が加わった。
- [**Agent SDK TypeScript リファレンス**](#8-agent-sdk-typescript-リファレンス) ([English](https://code.claude.com/docs/en/agent-sdk/typescript#sdkcontrolreadfileresponse)):  
  セッションのファイルを読む `readFile()` とその戻り値型が新設され、ターミナル専用コマンドの一覧も加わった。
- [**セルフホスト環境リファレンス**](#9-セルフホスト環境リファレンス) ([English](https://code.claude.com/docs/en/self-hosted-environments-reference#runner-cli-flags)):  
  変更行数 60 行のうち大半は表の桁揃え。実質は `--base-dir` の Windows での既定なしと、メトリクスのラベル値の訂正。
- [**組織の MCP サーバーアクセスを制御する**](#10-組織の-mcp-サーバーアクセスを制御する) ([English](https://code.claude.com/docs/en/managed-mcp#exclusive-control-with-managed-mcp-json)):  
  `managed-mcp.json` があるクラウドセッションが起動時に終了しなくなり、VS Code 拡張の例外も明記された。
- [**カスタムサブエージェントの作成**](#11-カスタムサブエージェントの作成) ([English](https://code.claude.com/docs/en/sub-agents#turn-fork-mode-on-or-off)):  
  フォークモードの既定が変わり、前面／背面の判定が 4 つの場合に整理された（詳細はハイライト 1 参照）。
- [**エラーリファレンス**](#12-エラーリファレンス) ([English](https://code.claude.com/docs/en/errors#input-contained-only-whitespace)):  
  空白のみの入力のエントリが新設され、auto モード・リクエスト超過・コンパクション失敗の文面が細分化された。
<!-- light:updated-pages:end -->

## 1. 環境変数

追加 325 行・削除 324 行で今回最大の変更ですが、その大半は表の桁揃えによる整形で、内容が変わったのは 9 行です。新設は `CLAUDE_CODE_WORKFLOW_PREFIX_STAGGER_MS`（既定 5000、v2.1.229 以降）で、ワークフローのファンアウトで同じプロンプトキャッシュ接頭辞を共有するエージェントが、先行するエージェントの応答開始をどれだけ待つかの上限をミリ秒で決めます。`0` で待機を無効化でき、`DISABLE_PROMPT_CACHING` が設定されているときは待機しません。

既存行では 3 つが挙動の訂正です。`CLAUDE_CODE_ATTRIBUTION_HEADER` には、直接接続の一部の構成では `0` を設定しても auto モードの分類器リクエストには帰属ブロックが残る、という但し書きが加わりました。`CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` は、ネットワークトラフィックではないものの依存インストールを誘発しうるとして、プラグインの `command` ソースのバックグラウンド実行も止めるようになりました。`DISABLE_GROWTHBOOK` は `1` だけでなく `true` も受け付け、`0` や `false` では取得が有効なままだと明記されています。`CLAUDE_CODE_FORK_SUBAGENT` の説明はハイライト 1 のとおり全面的に書き換えられました。残りは細かい修正で、`CLAUDE_CODE_OAUTH_TOKEN` は表記が `claude.ai` に統一されたうえで「`/login` を実行しない限り」という条件が付き、`CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST` のテレメトリ自動オプトアウトの説明にサードパーティ提供元として Claude Platform on AWS が加わり、`CLAUDE_CODE_DISABLE_ADMIN_ENV_UNION` のリンク先は設定ページの新設節へ張り替えられました。

- [Environment variables - Claude Code Docs (English)](https://code.claude.com/docs/en/env-vars#variables)

## 2. Claude Code の設定

追加 221 行・削除 197 行。中心は優先順位の節の 3 分割（ハイライト 4 参照）ですが、周辺の加筆も広範囲です。フック設定の節には、`allowManagedHooksOnly` がユーザー・プロジェクト・ローカル・その他プラグインのフックをブロックすることに加え、`command` ソースのプラグインを（管理設定の `enabledPlugins` で強制有効にしたものも含めて）無効化すること、`statusLine` / `fileSuggestion` / `subagentStatusLine` を管理設定に絞ることが加わりました。この 3 つには **ステータスラインとファイル候補のゲート** という段落が付き、管理設定が `disableAllHooks` を立てたときとフォルダが未信頼のときは機能ごと無効、`allowManagedHooksOnly` のときと管理設定以外で `disableAllHooks` が `true` のときは管理設定の値だけに絞られ、管理設定に値が無ければ警告なくスキップされる、と 2 段階で説明されています。

設定キーの表では、`disableCommandPluginSources` と `subagentStatusLine` が追加されたほか、`allowAllClaudeAiMcps` の説明が「Claude Code 自身が取得する claude.ai コネクタ」に限定され、クラウドセッションへ配られるコネクタは抑制されたままだと明記されました。`disableAllHooks` はカスタムのファイル候補コマンドも止めること、`autoMemoryDirectory` はフックと同じワークスペーストラスト規則に従うことが加わり、サンドボックス設定では `network.allowedDomains` / `deniedDomains` の IPv6 リテラルをブラケット表記で書くこと（v2.1.229 以降）と、`injectHosts` は逆にブラケット無しの正規圧縮形で書くことが対比されています。管理設定の不正値の扱いにも `allowManagedHooksOnly` と `disableCommandPluginSources` の行が加わり、いずれも `true` として扱われます。`extraKnownMarketplaces` の説明は「信頼したら別途プロンプトが出る」形から「ワークスペーストラストを受け入れた時点で追加され、別のプロンプトは出ない。未信頼のフォルダでは無言で無視する」形に書き換えられました。

- [Claude Code settings - Claude Code Docs (English)](https://code.claude.com/docs/en/settings#hook-configuration)

## 3. プラグインマーケットプレイスの作成と配布

追加 93 行・削除 26 行。中心は `command` ソースの新設（ハイライト 3 参照）ですが、既存の記述も「プラグインは必ずキャッシュへ複製される」という前提が崩れたことに合わせて各所が直されました。プラグインのインストール方法の Note、プラグインソースの導入文、キャッシュとファイル解決のトラブルシューティングには、いずれも「link モードの `command` ソースだけはその場で使う」という例外が入っています。`version` の説明も、プラグインエントリ・`plugin.json`・バージョン管理の警告の 3 か所で「`command` ソースは `version` では固定されない」と補われました。

このほか、組織同期の要件が「`github` / `url` / `git-subdir` のみ対応、`npm` と `archive` は非対応」から「`github` / `url` / `git-subdir`、またはマーケットプレイスリポジトリ内の相対パスのいずれか」に書き換えられ、URL ベースのマーケットプレイスで相対パスが解決できない場合の代替も、ソースを列挙する形から「相対パス以外の任意のプラグインソース」へ一般化されました。管理マーケットプレイス制限には、`strictKnownMarketplaces` はプラグインの出所のマーケットプレイスを見るだけでエントリの中身は見ないため、許可されたマーケットプレイスからなら `command` ソースのプラグインも入れられる、だから止めたいなら `disableCommandPluginSources` を使う、という 1 段落が加わっています。チーム向けにマーケットプレイスを必須化する節も、「フォルダを信頼するとインストールを促される」から「信頼した時点で別プロンプトなしに追加される」に改まりました。

- [Create and distribute a plugin marketplace - Claude Code Docs (English)](https://code.claude.com/docs/en/plugin-marketplaces#plugin-sources)

## 4. セルフホスト環境のセッションをカスタマイズする

追加 44 行・削除 34 行。新しい内容は 3 つです。1 つ目は、Anthropic のコントロールプレーンがセッションに Claude Code のフックを供給する場合の扱いで（v2.1.229 以降）、ランナーは供給されたフックスクリプトをセッションの設定ディレクトリ配下の予約サブディレクトリ `hooks/.ccr-launcher/` に書き、それを登録した別の設定ファイルを `--settings` でセッションへ渡すため、シードした `settings.json` と `hooks/<name>` にある自前のスクリプトには触れません。スクリプトはコントロールプレーン自身のデプロイに固定された定数から生成され、セッション単位の入力や第三者の入力からは作られない、とも明記されています。`--settings` 経由のフックは通常のマージされたフック設定に入るので管理設定はそのまま効き、`disableAllHooks` で無効化でき、`allowManagedHooksOnly` が読み込みを維持するカテゴリには含まれません。

2 つ目は、ランナーホストにエンタープライズスコープの `managed-mcp.json` がある場合の挙動で、コントロールプレーンがセッションへ配る MCP サーバー（claude.ai コネクタを含む）をスキップし、その名前をセッション子プロセスの標準エラーへ警告として出す（ランナーは `debug` レベルで記録する）ようになりました。v2.1.229 より前はこうしたセッションが起動時に `You cannot dynamically configure MCP servers when an enterprise MCP config is present` で終了していました。3 つ目は環境変数 `CLAUDE_RUNNER_CLIENT_PLATFORM` の追加で、セッションを作ったクライアント面（`web_claude_ai` / `desktop_app` / `ios` / `claude_code_cli` / `scheduled_trigger` など）をラッパー・リポジトリ準備フック・セッション終了フック・spawn-runner フックに渡します。値はセッション作成時に 1 度記録されるため全フックで同じで、用途は採用状況の分析とラベル付けに限られ、認可の判断材料にしてはいけない、と念を押されています。

- [Customize sessions in self-hosted environments - Claude Code Docs (English)](https://code.claude.com/docs/en/self-hosted-environments-configuration#how-each-sessions-config-is-assembled)
- [Customize sessions in self-hosted environments - Claude Code Docs (English)](https://code.claude.com/docs/en/self-hosted-environments-configuration#mcp-servers)

## 5. 権限を設定する

追加 45 行・削除 32 行。中身はハイライト 2 のとおりで、ワークスペーストラストの節が本文・ローカル設定ファイル・信頼前に動くものの 3 つに分かれ、後者 2 つが新しい h3 になりました。管理のみの設定の表には `disableCommandPluginSources` の行が加わり、`allowManagedHooksOnly` の説明は効果の列挙をやめて設定ページのフック設定への参照に置き換えられています。`allowAllClaudeAiMcps` も設定ページと同じく「Claude Code 自身が取得するコネクタ」に限定されました。

サンドボックスとの関係を述べた節では、plan モードでの挙動の記述が簡素化されました。従来は「ask ルールが無ければプロンプト、auto モードが使えて `useAutoModeDuringPlan` が有効なら分類器へ」「v2.1.212〜v2.1.217 では auto モードが使えてもプロンプトした」と場合分けしていましたが、今回は「通常の権限フローを通る」とし、詳細は権限モードのページを見る形になりました。`rm` / `rmdir` が重要なシステムパスを対象にしたときの記述も、同様に「通常の権限フローを通る」に統一されています。

- [Configure permissions - Claude Code Docs (English)](https://code.claude.com/docs/en/permissions#when-your-local-settings-file-needs-trust)

## 6. プラグインリファレンス

追加 40 行・削除 36 行。バージョン管理の節が `command` ソースとそれ以外に分けられ、`command` ソースでは常にコマンドが生成した内容の 12 文字のハッシュ（`plugin.json` にバージョンがあれば `<version>-<hash>`）をバージョンにし、マーケットプレイスエントリの `version` は無視する、と書かれました。link モードではハッシュの対象がファイルの中身ではなく印字先の実パスとトップレベルのエントリになります。`claude plugin install` と `claude plugin update` には `-y, --yes` が追加され、コマンドを提示したうえで確認プロンプトを省く（stdin/stdout が TTY でないときは必須、Claude Code のセッション内では効かないので自分のターミナルから実行する）と説明されています。

プラグインキャッシュとファイル解決の節も、複製されるプラグインと link モードの区別に合わせて「コピーされたプラグイン」という限定が随所に加わりました。プロジェクトスコープのプラグインの説明では、読み込みのゲートが `.claude/settings.json` のプロジェクト許可ルールと同じもので、親フォルダを信頼しても `-p` で実行しても足りない、と明示されています。

- [Plugins reference - Claude Code Docs (English)](https://code.claude.com/docs/en/plugins-reference#version-management)

## 7. MCP で外部ツールに接続する

追加 19 行・削除 50 行で、正味では短くなっています。最も大きいのは実用例の削除で、**例: Sentry でエラーを監視する** の節が丸ごと無くなりました（`sentry` サーバーは認証が必要なリモートサーバーの手順で引き続き登場し、参照先は MCP クイックスタートへ張り替えられています）。次に多いのが「v2.1.19x 以降」といった履歴注記の削除で、接続失敗の Claude への通知、機能検出リクエストの再試行、トークン更新失敗時の通知、ルートレベルのコンビネータを持つスキーマの平坦化、`headersHelper` の 401/403 時の再実行、未使用コネクタの折りたたみなど、各所の「As of v2.1.x」が現在形の記述に置き換えられました。

内容の追加は 3 点です。1 つ目は MCP OAuth のリダイレクト URI で、v2.1.229 は `http://127.0.0.1:PORT/callback` を送っていたため登録済みリダイレクト URI を厳密照合するサーバーで不一致になり、v2.1.231 で `localhost` 形式に戻ったこと、v2.1.229 のままなら暫定的に `127.0.0.1` 形式を登録して回避することが書かれました。2 つ目はプロジェクトスコープのサーバー承認で、`skipDangerousModePermissionPrompt` を設定した `bypassPermissions` セッションもプロンプトを飛ばすことが加わり、リポジトリがコミットした承認とワークスペーストラストの関係は新設の表への参照になりました。3 つ目はツール検索の `auto` の意味の明確化で、「ツール定義がコンテキストウィンドウの 10% に収まれば前もって読み込む」ではなく「遅延できる定義の合計が 10% に達するまでは全て前もって読み込み、達した時点でそれらを全て遅延する」と書き直されています（Agent SDK のツール検索ページも同じ書き換えを受け、コアの組み込みツールは閾値に数えないことが明記されました）。

- [Connect Claude Code to tools via MCP - Claude Code Docs (English)](https://code.claude.com/docs/en/mcp#use-pre-configured-oauth-credentials)
- [Connect Claude Code to tools via MCP - Claude Code Docs (English)](https://code.claude.com/docs/en/mcp#scale-with-mcp-tool-search)

## 8. Agent SDK TypeScript リファレンス

追加 45 行・削除 22 行。新設は `Query` オブジェクトの `readFile(path, options?)` と、その戻り値型 `SDKControlReadFileResponse` です。パスはセッションの `cwd` を基準に解決され、Read ツールと同じ読み取り権限のルールが適用されます。`maxBytes` で上限を変えられ（既定 1 MB・上限 10 MB）、`encoding: 'base64'` で画像などのバイナリを読めます。権限拒否・ファイル不在・トランスポートエラーでは `null` を返します。応答は `contents`（テキストまたは base64）、`absPath`、`maxBytes` で切られたときに立つ `truncated`、base64 を要求したときの `encoding` を持ちます。ドキュメント上の必要バージョンは TypeScript SDK v0.2.121 以降と記載されています。

`SDKSystemMessage` には `terminal_slash_commands` が加わりました。`slash_commands` のうち `exit` のようにローカルのターミナルにインターフェースが結び付いているものを列挙する省略可能なフィールドで、他と同じように送れますが、リモートやモバイルのクライアントがコマンドメニューから隠せるように用意されています。空でないときだけ現れ、Agent SDK v0.3.229 以降が必要です。

- [Agent SDK reference - TypeScript - Claude Code Docs (English)](https://code.claude.com/docs/en/agent-sdk/typescript#sdkcontrolreadfileresponse)

## 9. セルフホスト環境リファレンス

変更行数は 60 行ですが、その大半は 2 つの表の桁揃えで、内容が変わったのは 2 行です。`--base-dir` の既定値は `/workspace` のままですが、Windows では既定が無く、フラグか環境変数を渡さないとランナーが起動時に終了する、と加わりました（Windows はサポート対象のランナーホストではありません）。もう 1 つは Prometheus メトリクス `claude_code_self_hosted_runner_sessions_started_total` のラベル値の訂正で、CLI 由来のセッションの値がハイフン区切りの `claude-code-cli` からアンダースコア区切りの `claude_code_cli` に直されました。

- [Self-hosted environments reference - Claude Code Docs (English)](https://code.claude.com/docs/en/self-hosted-environments-reference#runner-cli-flags)

## 10. 組織の MCP サーバーアクセスを制御する

追加 31 行・削除 22 行。**managed-mcp.json による排他的制御** の節に、`--mcp-config` でサーバーが渡されたときにユーザーが何を見るかが、セッションの実行場所別に整理されました。ワークステーションでは従来どおり起動時に `You cannot dynamically configure MCP servers when an enterprise MCP config is present` で終了しますが、claude.ai コネクタなどサーバー配信のサーバーを `--mcp-config` で受け取るクラウドセッションでは、管理サーバーだけで起動するようになりました。どのサーバーが除かれたかはセッション内では分からず、標準エラーの警告に名前が出る（セルフホストランナーは `debug` レベルで記録する）だけです。v2.1.229 より前はこうしたセッションもワークステーションと同じエラーで終了していました。ユーザーが `--strict-mcp-config` を渡した場合は管理セットの置き換えを求めることになるため、どちらの環境でも起動時に終了します。

もう 1 つの変更は VS Code 拡張の扱いで、`managed-mcp.json` を配っても拡張が起動したセッションでは拡張自身のインプロセスサーバーだけは読み込まれる、という例外が制限レベルの表・排他的制御の節・MCP を完全に無効化する手順の 3 か所に明記されました。`allowAllClaudeAiMcps` も、効くのは Claude Code 自身が取得するコネクタだけで、クラウドセッションが `--mcp-config` として受け取るコネクタは設定の有無に関わらず抑制される、と限定されています。

- [Control MCP server access for your organization - Claude Code Docs (English)](https://code.claude.com/docs/en/managed-mcp#exclusive-control-with-managed-mcp-json)

## 11. カスタムサブエージェントの作成

追加 28 行・削除 22 行。中身はハイライト 1 のとおりで、「制限」という節が **フォークモードのオン/オフを切り替える** に置き換わり、フォアグラウンドとバックグラウンドの判定が 4 つの場合の箇条書きになりました。会話をフォークする節の冒頭 Note からは、v2.1.212 より前のコマンド名の経緯と、staged rollout に関する実験的機能である旨の断りが削除され、`/subtask` の説明だけが残っています。

フロントマターの説明にも変更が入りました。サブエージェントのフロントマターのフックがワークスペーストラストを要する話には、これが設定ファイルのフックより厳しい規則で、親フォルダを信頼しても `-p` セッションでも足りない、という比較が加わり、権限ページの新設表へ誘導されています。

- [Create custom subagents - Claude Code Docs (English)](https://code.claude.com/docs/en/sub-agents#turn-fork-mode-on-or-off)

## 12. エラーリファレンス

追加 40 行・削除 10 行。新設のコマンドラインエラーは **Input contained only whitespace** で、非対話モードで空白・タブ・改行だけのプロンプトを API に送らず拒否するようになりました（v2.1.229 以降。それより前は API に送って 400 で弾かれていました）。`claude -p` の引数やパイプ入力なら終了コード付きのエラー、`--input-format stream-json` や Agent SDK の稼働中セッションへ送った場合はモデルを呼ばずにターンを終え、`Blank prompt — the message was only whitespace, so nothing was sent to the model.` が結果テキストとして返ります。

既存エントリの文面も細かく分かれました。auto モードの分類器が使えないときのメッセージは、失敗の分類が判別できる場合に `(rate-limited)` `(overloaded)` `(server error)` `(timed out)` `(connection failed)` のいずれかを括弧書きで添えるようになり、前 3 つは一時的なので再試行が効き、後 2 つが続くなら接続を確認する、という読み分けが付きました。`Request too large` は、Claude API が直接拒否した場合に会話を計測して 2 通りに書き分けるようになり、画像や文書が原因なら剥がして再試行、メッセージだけで超過しているなら `compacting cannot make it fit` として再試行しない、と示されます。自動コンパクションが下位のエラーで失敗した場合は `Prompt is too long · automatic compaction failed: <原因>` の形で原因が出るようになりました（v2.1.229 より前は素の `Prompt is too long` だけでした）。1M コンテキストの使用クレジットのエントリには、この確認は `/model` での選択時に、しかも Anthropic API への直接接続でのみ走り、`ANTHROPIC_BASE_URL` がゲートウェイを指す場合は `/model` が `[1m]` の選択を通してゲートウェイ側が可否を決める、と加わっています。

- [Error reference - Claude Code Docs (English)](https://code.claude.com/docs/en/errors#input-contained-only-whitespace)
- [Error reference - Claude Code Docs (English)](https://code.claude.com/docs/en/errors#request-too-large)

## 軽微な更新

<!-- light:minor-updates:start -->
対象期間には changelog へのリリース追加 2 件（v2.1.232 / v2.1.231）と、上記 12 ページ以外に 63 ページの更新がありました。複数リリースを含むため、各項目にはバージョンを併記します。なお本サマリの参考リンクは全て英語版のみです。今回変更のあったページは日本語版がまだ追従していないためで、サブエージェントと権限の 2 ページを実際に確認したところ、いずれも今回の新設セクションが存在せず旧記述のままでした。

**新機能**

- ワークフローのファンアウトでプロンプトキャッシュの接頭辞を共有する仕組みが文書化されました（v2.1.229）。モデル・エフォート・エージェントタイプ・ツール・出力スキーマ・作業ディレクトリが同じエージェントは同じ接頭辞を作るため、Claude Code は同時に起動した同型エージェントのうち先頭以外を先頭の応答開始まで待たせ、まとめて解放します。待ちの上限は `CLAUDE_CODE_WORKFLOW_PREFIX_STAGGER_MS`（既定 5000 ミリ秒、`0` で無効）で、制約の表にもこの項目が加わりました — [English](https://code.claude.com/docs/en/workflows#prompt-caching-in-a-fan-out)
- Remote Control のサーバーを止めた後にセッションを呼び戻せることが節として文書化されました。同じディレクトリで `claude remote-control` を実行すれば配下の全セッション、`--continue` なら起動時のセッション、`--session-id <id>` なら指定したセッションが戻ります（後者 2 つはそのセッションの終了で終わります）。使えるのは停止からおよそ 4 時間で、`--no-create-session-in-dir` で起動したサーバーのセッションは停止時にアーカイブされるため戻せません — [English](https://code.claude.com/docs/en/remote-control#resume-sessions-after-stopping-the-server)
- VS Code 拡張のセッション一覧を、名前付きの折りたたみ可能なグループにまとめられるようになりました（v2.1.229）。右クリックでグループの作成・移動・解除、`Cmd`/`Ctrl` クリックや `Shift` クリックで複数選択ができ、グループはワークスペースフォルダ単位で保存されます。同拡張では **Report a problem** と `/bug` / `/feedback` が拡張自身のフィードバックダイアログを開くようにもなりました（CLI と違い、ローカルへのアーカイブ書き出しは行いません）— [English](https://code.claude.com/docs/en/vs-code#organize-sessions-into-groups)
- TypeScript SDK にセッションのファイルシステムからファイルを読む `readFile()` が加わりました（詳細は大幅更新 8 参照）。Python SDK にも `resume_session_at` / `resume_drops_turn` オプション、`UserMessage` と `ResultMessage` の `origin` フィールド、`/clear` などで会話が差し替わったときの `ConversationResetMessage` が追加されています — [English](https://code.claude.com/docs/en/agent-sdk/python#conversationresetmessage)
- GitHub Actions のレビューワークフローが、レビュー結果をプルリクエスト自身へ投稿するようになりました（v2.1.229。それ以前はワークフローの実行ログにだけ書いていました）。指摘ごとのインラインコメント、指摘が無ければ 1 件の要約コメントになります。既存のワークフローファイルを更新するには `/install-github-app` をもう一度実行して **Update workflow file with latest version** を選ぶか、`--comment` 引数と `claude_args` の行を自分で足します — [English](https://code.claude.com/docs/en/github-actions#run-a-skill)
- サンドボックスのドメインリストで IPv6 リテラルをブラケット表記で書けるようになりました（v2.1.229）。`"[::1]"` は全ポート、`"[::1]:443"` は 443 番のみに一致します。コロンが 2 つ以上ある括弧なしの表記は曖昧なため、拒否リストでは解釈しうる全ての読み方を拒否し、許可リストでは書いた以上に広げず、場合によってはエントリごと落とします。`/doctor` が該当エントリを一覧します — [English](https://code.claude.com/docs/en/sandboxing#ipv6-addresses-in-domain-lists)
- セルフホスト環境のフックに `CLAUDE_RUNNER_CLIENT_PLATFORM` が加わりました（v2.1.229、詳細は大幅更新 4 参照）。設定側では `subagentStatusLine` キーが追加され、サブエージェントのタスク表示の行をカスタムコマンドで書き換えられるようになっています — [English](https://code.claude.com/docs/en/statusline#subagent-status-lines)
- GitLab のトークン系（`glrt-` `gloas-` `glptt-` `glagent-` `glimt-` `glsoat-` `glcbt-` `glft-` `glffct-`）の秘匿と、ルーティング可能な `glpat-` / `gldt-` トークンの全文秘匿が加わりました（v2.1.232）
- `glab` CLI の設定ストアが、`gh` と同じサンドボックスと資格情報パスの保護を受けるようになりました（v2.1.232）
- プラグインマーケットプレイスが GitLab に対応しました（v2.1.232）。ネストしたサブグループを含む素の `gitlab.com` リポジトリ URL が `github.com` の URL と同様に clone され、clone の認証失敗時のヒントも実際の git ホスト名を挙げるようになりました
- 設定で `additionalMarketplaces` と `allowedMarketplaces` が、`extraKnownMarketplaces` と `strictKnownMarketplaces` の分かりやすい別名として受け付けられるようになりました（v2.1.232）
- Claude apps gateway の `desktop:` オーバーレイが、手で列挙した 11 キーではなくリリース済みの Desktop 設定を全て受け付けるようになりました（v2.1.232）。起動時に Desktop 自身のスキーマで検証され、未知のキーや不正な値は起動を失敗させます
- `/advisor` で Fable 5 を再び選べるようになりました（v2.1.232）。Fable アクセスのある組織向けで、使用クレジットの同意は `/model fable` で設定します

**機能改善**

- プロンプト候補の提供条件が明文化されました。対話モードでは既定でオフになり `/config` のトグルも隠れるのは、フィーチャーフラグを評価しない場合、すなわち Amazon Bedrock・Claude Platform on AWS・Google Cloud's Agent Platform・Microsoft Foundry を使っている場合（ホストが `CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST` を立てている場合を除く）、Claude apps gateway にサインインしている場合、フラグ評価を止める環境変数を設定している場合です。個別にスキップされる状況も、キャッシュが冷たいとき・会話の最初のターンの後・直前の応答がエラーで終わったとき・plan モード・エージェントチームのチームメイトのセッション、と列挙されました — [English](https://code.claude.com/docs/en/interactive-mode#when-claude-code-skips-suggestions)
- マーケットプレイス名まで指定したプラグインのインストールでは、Claude Code が先にそのマーケットプレイスを更新してから検索するようになりました（v2.1.232）。自動更新の設定や `DISABLE_AUTOUPDATER` に関わらず走り、Git/リモート URL 由来でない場合・シードディレクトリ由来の場合・直近 30 秒以内に更新済みの場合・`CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` を設定している場合のみスキップします。プラグイン名だけを指定した `/plugin install` は、検索が外れた後に背景更新の対象マーケットプレイスだけを更新します — [English](https://code.claude.com/docs/en/discover-plugins#install-plugins)
- mTLS のクライアント証明書のローテーション手順が具体化されました。Claude Code は起動時と設定を適用するたびに証明書と鍵を読み直しますが、セッション中にパスを監視はしないため、実行中のセッションではファイルを置き換えたうえで再起動するのが確実です。リモート管理設定の同期や `/login` などの設定適用が起きれば読み直されますが、旧証明書の失効前に起きる保証はありません — [English](https://code.claude.com/docs/en/network-config#mtls-authentication)
- Claude apps gateway が、静かなストリームに SSE の `ping` を送るようになりました（v2.1.229）。`provider: anthropic` 以外の上流ではストリームが約 15 秒無音になると自ら ping を書き、`provider: anthropic` では上流の ping をそのまま流します。AWS の構成例では、ALB の既定 60 秒のアイドルタイムアウトでも静かなストリームが切れなくなり、`idle_timeout.timeout_seconds=3600` は余裕を持たせる設定という位置づけに変わりました。ゲートウェイのプロトコルリファレンスにも、Bedrock のバイナリイベントストリームのように ping を送らない上流から変換する場合は自分で `ping` を出すように、という案内が加わっています — [English](https://code.claude.com/docs/en/claude-apps-gateway-on-aws#troubleshooting)
- Claude apps gateway が、`managed.policies[].match.groups` と `admin.admin_groups` の空エントリ、および不正な `email_domain`（空、または `@`・空白・カンマを含むもの）で起動に失敗するようになりました（v2.1.232）。それまでは誰にも一致しないまま、あるいは管理者権限を与えたまま無言で通っていました
- 帰属ブロックの位置づけが整理されました。`CLAUDE_CODE_ATTRIBUTION_HEADER` はゲートウェイやサードパーティのキャッシュ互換のための変数であってプライバシー制御ではなく、`api.anthropic.com` への直接接続で、かつ資格情報が Anthropic のプロファイル／フェデレーション資格情報でない場合は、`0` を設定しても auto モードの分類器リクエストにはブロックが残ります。分類器リクエストはシステムプロンプトの残りを省くため、ブロックだけが Claude Code のトラフィックだと分かる目印になるからです。v2.1.229 より前はこの例外が無く、API が正体不明のリクエストを断ると auto モードが全て失敗していました — [English](https://code.claude.com/docs/en/llm-gateway-protocol#system-prompt-attribution-block)
- OpenTelemetry の設定の説明が精緻化されました。シグナル別のエンドポイントやプロトコルの変数は汎用の変数を置き換える一方、シグナル別のヘッダー変数は汎用の `OTEL_EXPORTER_OTLP_HEADERS` とマージされること、`grpc` プロトコルでは動的ヘッダーが使えず静的なヘッダー変数のみが使われることが明記され、メトリクス・ログ・トレースのヘッダー変数も表に追加されました — [English](https://code.claude.com/docs/en/monitoring-usage#common-configuration-variables)
- セルフホストランナーのリポジトリ準備が、プロンプトを出しうる経路を全て塞いでいることが文書化されました。ランナーは `GIT_TERMINAL_PROMPT=0`、SSH の `BatchMode=yes`、`GCM_INTERACTIVE=never` を設定し、`core.askPass` をクリアします（askpass ヘルパーを使うなら `GIT_ASKPASS` で渡します）。資格情報が拒否されるか未設定なら、数回再試行した後にリポジトリ準備が失敗します — [English](https://code.claude.com/docs/en/self-hosted-environments-deploy#configure-git)
- Claude Code on the web が、クラウドセッションで `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` を自分で設定していることが明記されました。この値はユーザーが環境変数に足した値を上書きするため、そこに同じキーを書いてもコンパクションのタイミングは変わりません。ウィンドウ自体を変えたい場合は `CLAUDE_CODE_AUTO_COMPACT_WINDOW` か `/autocompact` を使います — [English](https://code.claude.com/docs/en/claude-code-on-the-web#manage-context)
- ステータスラインが管理設定で消える条件が明示されました。`allowManagedHooksOnly` が設定されていると、警告なくカスタムのステータスラインが消え、管理設定の `statusLine` からしか出せなくなります。`disableAllHooks` についても、設定の優先順位を適用した後に管理設定以外で `true` なら管理設定の値だけが動く、という書き方に変わりました — [English](https://code.claude.com/docs/en/statusline#troubleshooting)
- フルスクリーンのリンククリックの説明が箇条書きに整理され、Windows の UNC パス（`\\server\share\file.ts`）は開くと資格情報が相手ホストへ送られうるためリンクにせず平文で描画する、という項目が加わりました — [English](https://code.claude.com/docs/en/fullscreen#enable-fullscreen-rendering)
- JetBrains の診断共有の説明が、常時共有ではなく「Claude がファイルを編集した後にそのファイルの新しい診断を取り込む」という書き方に改まりました。編集が持ち込んだエラーに Claude が気付けるようにするための挙動です — [English](https://code.claude.com/docs/en/jetbrains#features)
- `CLAUDE_CODE_OAUTH_TOKEN` を設定したまま `/login` を実行すると、現在のセッションは新しいログインに切り替わるものの、シェルのプロファイルや設定の `env` ブロックから変数を消すまで新しいセッションでは再び読まれることが明記されました — [English](https://code.claude.com/docs/en/authentication#authentication-precedence)
- `/loop` の提供差分が 1 か所にまとまりました。Amazon Bedrock・Claude Platform on AWS・Google Cloud's Agent Platform・Microsoft Foundry、およびフィーチャーフラグ取得を切った場合は、間隔を省いた `/loop` が固定 10 分間隔になり、プロンプトを省いた `/loop` は使い方メッセージを出すだけ（`loop.md` も読まれない）という 2 点が同じ Note に統合されています — [English](https://code.claude.com/docs/en/scheduled-tasks#let-claude-choose-the-interval)
- プロンプトキャッシュのページで、サブエージェントの初回リクエストが親のキャッシュを読まない理由が「接頭辞が異なるため」と明示され、ワークフローのファンアウトでの接頭辞共有への参照が加わりました — [English](https://code.claude.com/docs/en/prompt-caching#subagents-and-the-cache)

**バグ修正**

- 厳密照合するリダイレクト URI を持つ事前登録済み OAuth クライアント（Slack など）で MCP の OAuth サインインが不一致で失敗する問題が修正されました（v2.1.231）— [English](https://code.claude.com/docs/en/mcp#use-pre-configured-oauth-credentials)
- PowerShell で、変数を書き込むパラメータが `$PSDefaultParameterValues` を無言で上書きし、後続コマンドのファイルアクセスを付け替えられる権限バイパスが修正されました（v2.1.232）
- Windows で、Git Bash が Cygwin 形式のシンボリックリンクを辿るのにパス検証はそれを通常ファイルと見なす権限バイパスが修正され、リンク経由の書き込みにも権限承認が必要になりました（v2.1.232）
- ネストした git リポジトリが親ディレクトリの信頼を引き継ぐ問題が修正され、各リポジトリで個別に信頼の確認が必要になりました（v2.1.232）
- MCP サーバーがプロトコルバージョンの探索に応答しないか不正な応答を返したとき、接続タイムアウトの 30 秒間ハングする問題が修正されました（v2.1.232）
- Remote Control で、クラウドセッション内のブリッジがホストするセッションが、そのクラウドセッションのトランスクリプトや資格情報を引き継ぐ問題が修正されました（v2.1.232）
- Remote Control で、Claude Desktop や IDE から始めたセッションが、ローカルセッションを再開するたびに claude.ai 側では新規セッションとして現れる問題が修正され、既存のセッションに再接続するようになりました（v2.1.232）
- Remote Control で、アイドル中のセッションが新しく接続したクライアントから到達不能に見える問題と、セッションワーカーの再起動時にブリッジセッションの会話履歴が復元されない問題が修正されました（v2.1.232）
- Remote Control で、claude.ai やアプリ側から削除された会話を再開しようとするとログイン関連のメッセージで失敗する問題（v2.1.227 での退行）が修正され、代わりのセッションが始まるようになりました（v2.1.232）
- Cloud gateway の `/login` が、管理設定の読み込みに失敗したときに無言で終了したり「Press Enter to continue」の後に端末が応答しなくなったりする問題が修正され、理由が表示されるようになりました（v2.1.232）
- mTLS のクライアント証明書のローテーションに再起動が必要だった問題が修正され、接続エラー時に自動で読み直すようになりました（v2.1.232）
- 不正な AWS / Vertex のリージョン値がそのままリクエスト URL の組み立てに使われる問題が修正され、既定のリージョンにフォールバックするようになりました（v2.1.232）
- Bedrock・Vertex・ゲートウェイのデプロイで、ストリームのアイドルタイムアウトエラーが回復せずリクエストごと失敗する問題が修正されました（v2.1.232）
- ネイティブビルドの音声モードが、音声サービスに接続を拒否されたときに「listening…」のまま固まる問題が修正され、拒否が即座に表示されるようになりました（v2.1.232）
- 切り詰めたテキストを含む内容サイズのオーバーレイが 1 桁広く描画され、先頭を切り詰めたテキストが省略記号に潰れる問題が修正されました（v2.1.232）
- 長いシェルコマンドやエージェントの説明のプレビューが絵文字の途中で切れ、文字化けした 1 文字が残る問題が修正されました（v2.1.232）
- `known_marketplaces.json` への同時書き込みにより、起動時のレースでプラグインマーケットプレイスが無言で登録解除される問題が修正されました（v2.1.232）
- 再起動をまたいで残る作業の実行中に、`/update` と `/tui` が再起動を拒否する問題が修正されました（v2.1.232）
- SDK やリモートセッションで、使用量上限の案内がそこでは使えないスラッシュコマンドを勧める問題が修正されました（v2.1.232）
- 対話的な `--advisor fable` の起動時に、直前に終了した対話セッションで `/model fable` を実行するよう促す同意メッセージが出る問題が修正されました（v2.1.232）

**その他**

- **前回サマリの記述が 1 件更新されました。** 前回「TypeScript では `SDKConversationResetMessage` でリセットを検出できるが Python SDK はそのメッセージをアプリへ渡さない」と書きましたが、今回の更新で Python SDK も `ConversationResetMessage` を発行するようになり、記述は「Python SDK v0.2.137 より前のバージョンではイテレータが握り潰していたので、そのバージョンでは `/clear` のターンを自分で数える」に改められています
- `llms.txt` には変更がなく、今回差分があったのは `llms-full.txt` とページ見出しマップの 2 ファイルのみでした。見出しマップでは、今回新設された節（フォークモードの切り替え、コマンドソースとその 3 小節、設定の優先順位の 3 小節、信頼前に何が動くか、ドメインリストの IPv6、ファンアウトのプロンプトキャッシュ、サーバー停止後のセッション復帰、セッションのグループ化、プロンプト候補の 2 節、フックのワークスペーストラスト、`SDKControlReadFileResponse`、`ConversationResetMessage`、空白のみの入力）が追加され、MCP の Sentry の例と、サブエージェントの「制限」が消えています
- 「As of v2.1.x」「Before v2.1.x」といった履歴注記が多数のページで一斉に削除されました。MCP・ワークフロー・スキル・スケジュール実行・エージェントチーム・エージェントビュー・worktree・フックなどが対象で、いずれも現在の挙動を現在形で述べる記述に置き換えられています
- プロバイダーの列挙が「Amazon Bedrock、Google Cloud's Agent Platform、Microsoft Foundry」と数え上げる形から「サードパーティのプロバイダーやゲートウェイ」と一般化する形へ、複数ページで書き換えられました。モデル設定・クラウドセッション・エージェントビュー・デスクトップなどが該当し、データ利用のページでは逆にテレメトリ既定オンの一覧に Claude Platform on AWS が加わっています
- マーケットプレイスの検索失敗時の案内が、各所で「自動更新が切れているなら手動で更新して再試行」という長い説明から、インストール手順への 1 リンクに置き換えられました。チャネル・スキル・セキュリティガイダンス・大規模コードベース・Claude Security など 7 ページが同じ書き換えを受けています
- Claude apps gateway で、テレメトリの送信先が「サインイン済みの全セッション」から「`/login` でサインインしたセッション」に限定され、Claude Desktop が起動する埋め込みセッションは設定された `OTEL_EXPORTER_OTLP_ENDPOINT` へ送る（ゲートウェイ自身を指す場合にだけセッショントークンを添える）と書き分けられました
<!-- light:minor-updates:end -->

## 新着情報

<!-- light:whats-new:start -->
（今回の対象期間に更新された新着情報ページはありません。前回の Week 32 以降、新しい週次ダイジェストは公開されていません）
<!-- light:whats-new:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-08-12.md](./archives/latest/2026-08-12.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-08-12.md](./archives/latest-detail/2026-08-12.md)

<!--
base_commit: 6bb349f9c8d4ed9d313be35f06d8f5b1ff63f332
head_commit: d837a95ef745893def1444471ab9e621cc930a85
generated_at_full: 2026-08-14T15:08:17+09:00
-->
