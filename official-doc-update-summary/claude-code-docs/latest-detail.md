---
対象期間: 2026年08月22日 〜 2026年08月24日
作成日: 2026-08-24
---

# Claude Code 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
今回は 2 日分の取り込みで、44 ページに差分がありました。新規ページの追加も新着情報の更新も無く、changelog に新しいリリースエントリも加わっていません。実態は、v2.1.234〜v2.1.242 を要件とする機能を既存ページに書き込む作業で、プロンプトキャッシュ・使用量上限・プラグイン配布の 3 領域に集中しています。

主要なものを以下に挙げます。

1. プロンプトキャッシュの TTL が「メイン会話」と「それ以外」の 2 バケットに整理され、それぞれ別に選べるようになった
2. claude.ai の使用量上限に当たったとき、リセットを待って中断したタスクを自動で再開するようになった
3. プラグインのアーカイブをダウンロードするときの認証ヘッダを、コマンドで都度生成できるようになった
4. `/model` ピッカーに並ぶモデルとラベルを組織側で決められる `modelPicker` が加わった
5. 素の `WebFetch` 権限ルールとドメイン指定ルールが別物であることが明文化された
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**プロンプトキャッシュの TTL をメイン会話とそれ以外で選び分ける**](#1-プロンプトキャッシュの-ttl-をメイン会話とそれ以外で選び分けられるようになった):  
  TTL の決まり方が「認証方法で決まる」から「リクエストがどちらのバケットに属するかで決まる」に整理され、`promptCacheTtl` / `subagentPromptCacheTtl` の 2 設定と対応する環境変数が加わった。v2.1.242 以降が必要。
2. [**使用量上限のリセットを待って中断したタスクを自動再開する**](#2-使用量上限のリセットを待って中断したタスクを自動再開する):  
  claude.ai サブスクリプションの対話セッションで既定 ON。セッションを開いたまま待ち、リセット時に固定プロンプトを送って中断箇所から再開する。v2.1.234 以降。
3. [**プラグインアーカイブのダウンロードを認証する `headersHelper`**](#3-プラグインアーカイブのダウンロードを認証する-headershelper):  
  `archive` ソースのプラグインを資格情報が要るレジストリから落とすための仕組み。固定値の `headers` に加え、短命なトークンをコマンドで都度生成する `headersHelper` が使えるようになった。v2.1.238 以降。
4. [**`/model` ピッカーの並びとラベルを組織で決める `modelPicker`**](#4-model-ピッカーの並びとラベルを組織で決める-modelpicker):  
  管理設定・`--settings`・ユーザー設定から読む新キー。組み込みの一覧に足すことも、丸ごと置き換えることもできる。プロジェクト・ローカル設定では無視される。v2.1.242 以降。
5. [**素の `WebFetch` ルールとドメイン指定ルールが別物であることが明文化された**](#5-素の-webfetch-ルールとドメイン指定ルールが別物であることが明文化された):  
  従来「等価」と書かれていた記述が撤回され、専用の節が新設された。サンドボックス化コマンドが到達できるホストを変えるのはドメイン指定形だけ。
<!-- light:highlight-list:end -->

## 1. プロンプトキャッシュの TTL をメイン会話とそれ以外で選び分けられるようになった

プロンプトキャッシュのページで、TTL の説明が大きく組み替えられました。これまでは「サブスクリプションなら 1 時間、API キーやクラウドプロバイダなら 5 分」という**認証方法による場合分け**でしたが、今回から**リクエストのバケットによる場合分け**になっています。バケットは 2 つで、**メイン会話**（対話ターン・非対話の `-p` 実行・Agent SDK のターンと、それらとインラインで動くヘルパー）と、**それ以外**（[サブエージェント](https://code.claude.com/docs/en/sub-agents)・ワークフロー・プロセス内のチームメイト・fork・コンパクション・セッションタイトルなど、メイン会話の外で Claude Code が出すリクエスト）です。

既定値は次のとおりです。サブスクリプションでプラン内の使用に収まっている間は、メイン会話が 1 時間、それ以外は 5 分（ただし Anthropic 側がサーバーで制御する一部のヘルパーリクエストだけは 1 時間）。使用クレジットを引き出し始めた場合、API キー、クラウドプロバイダのいずれでも、両バケットとも 5 分です。従来「サブスクリプションでは 1 時間の TTL が自動でリクエストされる」と読めた記述が、メイン会話に限った話であることが明示された形です。サブエージェントの節も、「サブスクリプションでも 5 分」という結論はそのままに、その理由を「メイン会話のバケットに属さないから」と説明し直しています。

選び方は設定と環境変数の 2 系統で、いずれも `5m` か `1h` のみを受け付けます。メイン会話が [`promptCacheTtl`](https://code.claude.com/docs/en/settings-reference#promptcachettl) 設定と `CLAUDE_CODE_PROMPT_CACHE_TTL`、それ以外が [`subagentPromptCacheTtl`](https://code.claude.com/docs/en/settings-reference#subagentpromptcachettl) 設定と `CLAUDE_CODE_SUBAGENT_PROMPT_CACHE_TTL` です。設定・環境変数とも v2.1.242 以降が必要です。複数が効く場合の優先順位は、①`FORCE_PROMPT_CACHING_5M=1`（両バケットを 5 分に強制）②そのバケットの環境変数 ③そのバケットの設定 ④`ENABLE_PROMPT_CACHING_1H=1`（両バケットに 1 時間を要求）⑤バケットの既定値、の順です。

実用上の使い分けも書き足されました。長い TTL が効くのはセッションを放置して戻ってくる使い方で、期限切れのプリフィックスを再処理する分を省けます。逆に 5 分を超えて空かない短い作業の連続では、書き込みレートだけ高くついて長さを使い切れません。API キーやクラウドプロバイダで `promptCacheTtl` を `1h` にすればメイン会話だけ 1 時間になり、それ以外は自分で選ぶまで 5 分のままです。使用クレジットを引き出しているサブスクリプションでも、この設定で 1 時間を維持できます。なお 1 時間の TTL は [Claude apps ゲートウェイ](https://code.claude.com/docs/en/claude-apps-gateway)経由では使えず、Amazon Bedrock では対応がモデルによって異なります。

- [How Claude Code uses prompt caching - Claude Code Docs (English)](https://code.claude.com/docs/en/prompt-caching#choose-the-ttl-yourself)
- [Claude Code settings reference - Claude Code Docs (English)](https://code.claude.com/docs/en/settings-reference#promptcachettl)

## 2. 使用量上限のリセットを待って中断したタスクを自動再開する

インタラクティブモードのページに **Wait for a usage limit to reset** が新設されました。claude.ai の使用量上限がタスクの途中で Claude を止めたとき、Claude Code がセッションを開いたまま待機し、上限がリセットされた時点で自分でタスクを続ける機能です。claude.ai サブスクリプションでサインインした対話セッションでは既定で有効で、v2.1.234 以降が必要です。

待機中はセッション最下部に `Usage limit reached · continuing automatically at 3:45pm · esc to cancel` の 1 行が出ます。終わり方は 3 通りです。**リセット時**は表示が `continuing shortly`、続いて `Usage limit reset · continuing automatically` に変わり、Claude Code が固定のプロンプトを送って中断箇所からタスクを拾い直します。**あなたの直前のメッセージを再送するのではありません**。**コンピュータがスリープしていた場合**は、スリープが約 30 分を超えていて、その間にリセットが起きていたときに限り `Your usage limit has reset · press enter to continue` となり、`Enter` を押す必要があります。それより短いスリープなら自動で続きます。**早期に再開する**場合もあり、待機中に `/usage-credits` で[使用クレジット](https://code.claude.com/docs/en/costs#add-usage-credits-to-your-subscription)の追加を終えたとき、`/upgrade` の後にサインインし直したとき、`/model` でモデルを切り替えたときは、使用量が復活していないかを確認して復活していればすぐ続けます。ブラウザ側で自分で購入・アップグレードした場合は確認しません。`opusplan` のように plan mode を別のモデルで走らせるモデル設定では、この早期再開は行わずリセットを待ちます。

続行後のターンは通常のターンと同じ扱いです。[権限](https://code.claude.com/docs/en/permissions)の確認も普段どおり出るため、離席中に権限プロンプトで止まることがあります。再び上限に当たった場合、Claude Code は自分で待機を張り直すのを連続 2 回までに制限し、その後は `Automatic continue stopped after repeated usage-limit hits · /rate-limit-options to try again` を表示して止まります。

待機のキャンセルは、行が出ている間に空のプロンプトで `Esc` を押すか、`Ctrl+C`、または `/rate-limit-options` で **Don't continue automatically** を選びます。`Automatic continue cancelled` で始まる行が確認として出ます。キャンセル後はプロンプトを送るか、`/rate-limit-options` で **Wait here, then continue automatically** で始まる行を選び直すまで何も進みません。同じリセットウィンドウの間、Claude Code が自分から待機を始めることはなく、次のリセットウィンドウで再び有効になります。このほか、プロンプトを送った・Claude Code を終了した・`/login` でのアカウント切り替えや会話のクリア／巻き戻し、`/resume`・`/teleport`・`/tui`、Claude Desktop やバックグラウンドセッション・クラウドへの引き渡しといった会話の持ち主が変わる操作、`autoContinueAtUsageLimit` を切ったかリセットが 24 時間より先に動いた場合、[`UserPromptSubmit` フック](https://code.claude.com/docs/en/hooks#userpromptsubmit)などが続行プロンプトを止めた場合にも、タスクを続けずに待機が終わります。

- [Interactive mode - Claude Code Docs (English)](https://code.claude.com/docs/en/interactive-mode#wait-for-a-usage-limit-to-reset)
- [Claude Code settings reference - Claude Code Docs (English)](https://code.claude.com/docs/en/settings-reference#autocontinueatusagelimit)

## 3. プラグインアーカイブのダウンロードを認証する `headersHelper`

プラグインマーケットプレイスのページに **Authenticate archive downloads** が新設されました。`archive` ソースのプラグインをプライベートなレジストリから落とすとき、Claude Code が送る HTTP ヘッダを指定する仕組みです。固定値なら `headers`、レジストリが都度発行するトークンのように短命な値なら `headersHelper` にコマンドを書き、Claude Code がそれを実行して出力した JSON オブジェクトをヘッダとして送ります。いずれも v2.1.238 以降が必要です。

置き場所は 2 つあり、どちらに書くかでヘッダが付くダウンロードとコマンドの実行タイミングが変わります。**マーケットプレイスの `url` ソース**に書くと、マーケットプレイス URL と同じオリジン（スキーム・ホスト・ポートが同じ）のアーカイブダウンロード全部に付き、コマンドは `marketplace.json` の取得前と当該オリジンへの各ダウンロード前に走ります（1 回の出力を最大 60 秒再利用）。**プラグインエントリ**に書くと、そのエントリのダウンロードにだけ付き、コマンドはユーザーがそのプラグインを単独でインストール／更新して承諾したときにのみ走ります。同名のヘッダは、両方に書かれていればエントリ側の値が、同じ場所の中では `headers` よりコマンド出力が優先されます。`marketplace.json` のエントリに `headersHelper` を置く場合は `"strict": false` が必須で、これによりエントリ自体がプラグインの定義全部になり、ユーザーが承諾前に中身を確認できるようになっています。

コマンドの側にも要件が並びました。印字可能な ASCII 500 文字以内で 4 個以上連続する空白を含まないこと、stdout に文字列値の JSON オブジェクトを 1 つ出して 10 秒以内に終了コード 0 で終わること、実行は `sh`（Windows は `cmd.exe`）で設定ディレクトリ（`~/.claude` または `CLAUDE_CONFIG_DIR`）を作業ディレクトリとして行われるので相対パスは避け絶対パスか `PATH` 上のコマンドを書くこと、です。環境変数の扱いも決まっており、`marketplace.json` のエントリやプロジェクトの `.claude/settings.json` / `.claude/settings.local.json` に書かれたコマンドからは、`TOKEN`・`SECRET`・`KEY`・`AUTH` といった語を名前に含む変数が `ANTHROPIC_API_KEY` を含めて除去されます（ユーザー設定・`--settings`・管理設定のコマンドは対象外）。逆に Claude Code が渡すのは、`url` ソースなら `CLAUDE_CODE_MARKETPLACE_URL` と `CLAUDE_CODE_MARKETPLACE_NAME`、エントリなら `CLAUDE_CODE_PLUGIN_NAME` と `CLAUDE_CODE_PLUGIN_ARCHIVE_URL` です。

コマンドを走らせない・出力を捨てる場面も列挙されました。コマンドが非ゼロ終了・10 秒超過・JSON オブジェクト以外を出力した場合はそのフェッチやダウンロード自体を行わず、マーケットプレイス URL が `https://` で始まらない場合はコマンドを走らせず `headers` だけを送り、リダイレクトでオリジンを離れた場合は両方の `headers` とコマンド出力を落とします。エントリが `Host`・`Cookie`・`X-Forwarded-*` のようなルーティング／識別系のヘッダ名を出した場合はその名前だけ落とし（`Authorization` などの認証系は残す）、`--add-dir` で足したディレクトリの設定ファイルのコマンドは無視されます。管理設定側では [`disableCommandPluginSources`](https://code.claude.com/docs/en/settings-reference#disablecommandpluginsources) を `true` にすると `headersHelper` もブロックされ、[`allowManagedHooksOnly`](https://code.claude.com/docs/en/settings-reference#allowmanagedhooksonly) も `disableCommandPluginSources` を明示的に `false` にしていない限り同様にブロックします（管理設定自身が宣言したマーケットプレイスは例外）。

承諾の導線も定義されました。エントリのコマンドは、`/plugin` の当該プラグインのビュー、`claude plugin install`、`claude plugin update` から**そのプラグインを単独で**インストール／更新するたびに承諾を求められます。非対話シェルでは `--yes` を渡します。Claude Code は提示したコマンドを提示したアーカイブ URL に対してのみ実行し、間にどちらかが変わっていればインストール／更新を拒否します（クエリ文字列だけの変化は除く）。単独でない操作、つまり複数プラグインの一括インストール・プラグイン提案からのインストール・他プラグインの依存としてのインストールでは、当該プラグインを拒否して `/plugin` のビューへ誘導します（一括インストールの他のプラグインはそのまま入り、依存していたプラグインはそれを単独で入れるまで失敗します）。バックグラウンドの自動更新や、アーカイブを一度も落としていないプラグインのセッション開始時は、`/plugin` の Errors タブに並びます。

- [Create and distribute a plugin marketplace - Claude Code Docs (English)](https://code.claude.com/docs/en/plugin-marketplaces#authenticate-archive-downloads)
- [Claude Code settings reference - Claude Code Docs (English)](https://code.claude.com/docs/en/settings-reference#extraknownmarketplaces)

## 4. `/model` ピッカーの並びとラベルを組織で決める `modelPicker`

設定リファレンスに `modelPicker` が新設されました。`/model` ピッカーに出すモデルを、書いた順に、選んだラベルで並べるためのキーです。組み込みの一覧の後ろに足すことも、丸ごと置き換えることもできます。v2.1.242 以降が必要です。

値は `options` 配列と、任意の `replaceBuiltInOptions`（真偽値・既定 `false`）の 2 フィールドです。`options` の各行は `model` が必須で、`label` と `description` が任意です。`model` はそのまま渡されるため、`--model` が受け付けるものは全て使えます。`opus` のようなエイリアス、Anthropic のモデル ID、Amazon Bedrock・Google Cloud の Agent Platform・Microsoft Foundry・LLM ゲートウェイのプロバイダ形式 ID です。`label` が無ければ Claude Code が知っているモデルは組み込みの名前で、そうでなければモデル ID で見出しを付け、`description` が無ければ 2 行目を汎用の文言で埋めます。

スコープは `User or managed` で、管理設定・`--settings`・ユーザー設定から読み、**プロジェクト設定とローカル設定では無視されます**。clone したリポジトリがピッカーのラベルを書き換えられないようにするためです。この 3 つのうちキーを設定している最上位が一覧を丸ごと供給し、2 つのソースの一覧が混ざることはありません。管理層のマージでも、`fallbackModel` や `availableModels` と同様に、後のものが前のものを置き換えます。

`replaceBuiltInOptions` を `true` にすると、組み込みの一覧、`availableModels` のエントリのために足される行、[ゲートウェイのモデル検出](https://code.claude.com/docs/en/llm-gateway-protocol#model-discovery)が見つけたモデル、[`ANTHROPIC_CUSTOM_MODEL_OPTION`](https://code.claude.com/docs/en/model-config#add-a-custom-model-option) の行が全て隠れ、書いた行と **Default**、それにセッションが現在使っているモデルの行だけが残ります。`false` のままなら組み込みの後ろに足され、組み込みが既にカバーしているモデルは飛ばされます。ラベルはピッカーの表示を変えるだけで、実際に走るモデルは変えません。`availableModels` の許可リストは引き続き効くので、許可リストに足す前に[マージの挙動](https://code.claude.com/docs/en/model-config#merge-behavior)（個別のモデル ID がそのファミリのワイルドカードを狭める点）を確認するよう促されています。行はピッカーを出す前にセッションと照合され、提供できない行（引退したモデルや組織がアクセス権を持たないモデル）は落とし、まだ選べない行は理由付きでグレーアウトして末尾に回します。1 行も残らなければ組み込みの一覧に戻ります。パースできない行は落として残りを使います。

- [Claude Code settings reference - Claude Code Docs (English)](https://code.claude.com/docs/en/settings-reference#modelpicker)
- [Model configuration - Claude Code Docs (English)](https://code.claude.com/docs/en/model-config#available-models)

## 5. 素の `WebFetch` ルールとドメイン指定ルールが別物であることが明文化された

権限のページにあった「`WebFetch(domain:*)` は全ドメインに一致し、素の `WebFetch` ルールと等価」という記述が撤回され、**Allow or deny every fetch** という節が新設されました。どちらも全 URL をカバーする点は同じですが、Claude Code の適用の仕方が異なり、サンドボックスの許可／拒否ドメインリストにドメインを追加するのは `domain:` 形だけです。

`allow` に置いた場合、素の `WebFetch` は確認なしで fetch できるようになりますが、サンドボックス化されたコマンドが到達できるホストは変わりません。`WebFetch(domain:*)` は確認なしの fetch に加えて、サンドボックス化されたコマンドが任意のホストに到達できるようになります。`deny` に置いた場合、素の `WebFetch` は WebFetch ツール自体を取り除くので Claude は一切 fetch できなくなりますが、やはりサンドボックスの到達範囲は変えません。`WebFetch(domain:*)` はツールを残したまま各 fetch を拒否し、あわせてサンドボックス化されたコマンドはどのホストにも到達できなくなります。Claude には自由に fetch させつつサンドボックスの許可リストは触りたくない場合は素の形を使う、という使い分けが例とともに示されています。なお `WebFetch` ルールのワイルドカードが fetch に一致するには v2.1.172 以降が必要です。

サンドボックスのページ側も、ドメイン制御に関わるのが `WebFetch(domain:...)` ルールであることを示す表記に統一され、サンドボックスが尊重するワイルドカードの形が明記されました。先頭の `*.`（`*.example.com` など）と、素の `*` の 2 つだけで、素の `*` は v2.1.186 以降です。`WebFetch(domain:example.*)` のようにそれ以外の位置にワイルドカードを置いた場合、fetch には一致しますがサンドボックス化されたコマンドには効きません。同じ趣旨の表記の統一は設定リファレンスの `sandbox.filesystem` の説明にも入っています。

- [Configure permissions - Claude Code Docs (English)](https://code.claude.com/docs/en/permissions#allow-or-deny-every-fetch)
- [Configure the sandboxed Bash tool - Claude Code Docs (English)](https://code.claude.com/docs/en/sandboxing#network-isolation)

## 新規追加されたページ

<!-- light:new-pages:start -->
（今回の対象期間に新規追加されたページはありません。差分は `llms-full.txt` の既存 44 ページのみで、`llms.txt` のページ一覧に増減はありませんでした）
<!-- light:new-pages:end -->

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
- [**プラグインマーケットプレイスの作成と配布**](#1-プラグインマーケットプレイスの作成と配布) ([English](https://code.claude.com/docs/en/plugin-marketplaces#distribute-through-organization-settings)):  
  追加 144 行・削除 16 行で今回最大の差分。`headersHelper`（ハイライト 3 参照）のほか、組織設定経由の配布ルールが独立した節に昇格し、トップレベル `bin/` を含めてはいけないという制約が加わった。
- [**設定リファレンス**](#2-設定リファレンス) ([English](https://code.claude.com/docs/en/settings-reference#modelpicker)):  
  追加 140 行・削除 9 行。新規キーは `modelPicker`・`promptCacheTtl`・`subagentPromptCacheTtl`・`autoContinueAtUsageLimit` の 4 つ（いずれもハイライト参照）。既存キーでは `disableAllHooks` が Agent SDK のフックを残すようになった。
- [**インタラクティブモード**](#3-インタラクティブモード) ([English](https://code.claude.com/docs/en/interactive-mode#start-a-wait-yourself)):  
  追加 52 行・削除 0 行。使用量上限の待機の節（ハイライト 2 参照）が丸ごと足されただけで、既存の記述は 1 行も変わっていない。
<!-- light:updated-pages:end -->

## 1. プラグインマーケットプレイスの作成と配布

追加 144 行・削除 16 行。**Authenticate archive downloads** とその配下 5 節はハイライト 3 のとおりです。ここでは残りを扱います。

最も大きいのは、組織設定経由の配布ルールが独立した節 **Distribute through organization settings** に昇格したことです。従来は Plugin sources の下の `<Note>` ブロックに畳まれていて、他の節からは「Plugin sources の下の注記に全ルールがある」と参照されていました。今回、Private repositories の後ろに専用の節として置き直され、内容も具体化されています。マーケットプレイスのリポジトリがプライベートまたは internal であること、各プラグインソースが `github`・`url`・`git-subdir` か相対パスであること、といった条件は従来どおりですが、**相対パスは `./` で始めて書き下す必要がある**という要件が加わりました。`metadata.pluginRoot` の下に素のプラグイン名だけを書くと、組織同期がサポート外のソースとして拒否するため、`./plugins/deploy-tools` のようにパスを書くことになります。プライベートなプラグインをマーケットプレイスのリポジトリ内に置いて相対パスで参照する方法には、実際の `marketplace.json` エントリの例が添えられました。

新設のサブセクション **Keep executables out of the top-level bin directory** も要注意です。組織設定経由で配るプラグインにトップレベルの `bin/` ディレクトリを含めると、claude.ai がそのプラグインを拒否します。マーケットプレイス同期の場合はそのプラグインだけ拒否して残りは同期し、エラーコードは `marketplace_sync_bin_directory_not_allowed`、メッセージは `Plugin contains a top-level bin/ directory` で始まります。`/plugin` からの直接アップロードでも同じメッセージで拒否されます。実行ファイルは `scripts/` のような別のディレクトリに置き、スキル・フック・MCP サーバー設定から `${CLAUDE_PLUGIN_ROOT}/scripts/<name>` として参照するよう案内されています。

リリースチャネルの節も具体化されました。stable / latest の 2 マーケットプレイスをユーザーグループに割り当てる手段が、従来の「管理設定で割り当てる」の 1 文から 2 方式に分かれています。1 つはグループごとのエンドポイント管理設定（管理設定ファイルや MDM プロファイル）を各グループの端末に配る方式で、端末上ではキーを配る[最上位の管理ソースだけが適用される](https://code.claude.com/docs/en/managed-settings#precedence-within-the-managed-tier)ため、そのファイル／プロファイルが最上位になる場合にのみ成立します。もう 1 つは [Claude apps ゲートウェイのポリシー](https://code.claude.com/docs/en/claude-apps-gateway-config#managed)をグループごとに定義する方式で、ゲートウェイは最初にマッチしたポリシーを適用するため順序が重要になり、かつグループポリシーの `extraKnownMarketplaces` は catch-all ポリシーのマップとマージされず**置き換える**ので、グループが必要とするマーケットプレイスを全て列挙する必要があります。管理コンソールのサーバー管理設定は組織の全ユーザーに適用されるため、グループ別の割り当てには使えないことも明記されました。

このほか、`command` ソースの承諾の説明に「記録済みの同一コマンドで進められる `claude plugin update` は何も表示しない」が加わり、URL マーケットプレイスで相対パスが失敗する原因の説明が「`marketplace.json` しか落とさない」から「加えて Claude Code はそのサーバーから相対パスでプラグインファイルを取りに行かない」に書き換えられました。

- [Create and distribute a plugin marketplace - Claude Code Docs (English)](https://code.claude.com/docs/en/plugin-marketplaces#distribute-through-organization-settings)
- [Create plugins - Claude Code Docs (English)](https://code.claude.com/docs/en/plugins#plugin-structure-overview)

## 2. 設定リファレンス

追加 140 行・削除 9 行。新規キーは 4 つで、`modelPicker` がハイライト 4、`promptCacheTtl` と `subagentPromptCacheTtl` がハイライト 1、`autoContinueAtUsageLimit` がハイライト 2 に対応します。冒頭の索引表にも 4 行が加わりました。ここでは既存キーの変更を扱います。

[`disableAllHooks`](https://code.claude.com/docs/en/settings-reference#disableallhooks) の到達範囲が書き直されました。管理設定に置いた場合は「設定された全てのフックを、管理設定のものも含めて無効にする」一方で、**Agent SDK がプロセス内で登録したフックは動き続ける**ことが明記されました。他の設定ファイルに置いた場合も、管理設定のフックとマネージド `enabledPlugins` で強制有効化されたプラグインのフックに加えて、Agent SDK のフックが残ります。管理設定でこのキーを設定したときに Agent SDK のフックを残す挙動は v2.1.242 以降です。

`headersHelper` に伴う管理側の記述も入りました。[`disableCommandPluginSources`](https://code.claude.com/docs/en/settings-reference#disablecommandpluginsources) は、`command` ソースを塞ぐときには常に、つまり `true` にした場合も `allowManagedHooksOnly` の下で未設定のまま塞がれる場合も、マーケットプレイスの `headersHelper` コマンドをあわせて塞ぎます（管理設定自身が宣言したマーケットプレイスは例外）。`headersHelper` のブロックは v2.1.238 以降です。`allowManagedHooksOnly` の箇条書きにも同じ趣旨の項目が加わりました。`extraKnownMarketplaces` には、`url` ソースの `headersHelper` をいつ実行するか、`settings` ソース配下のプラグインエントリが `headers` / `headersHelper` を持てること、`--add-dir` のディレクトリの設定ファイルでは `headersHelper` を無視して固定の `headers` だけを送ること、ヘッダフィルタがどのファイルのエントリに適用されるかが書き足されています。

版に関する注記の整理もあります。`permissions.defaultMode` から「v2.1.142 より前はプロジェクト設定で `auto` を設定できた」という履歴の記述が、`worktree.bgIsolation` から「v2.1.143 以降が必要」が、`allowAllClaudeAiMcps` から「v2.1.149 以降が必要」が、それぞれ削除されました。あわせて `sandbox.filesystem` の説明が `WebFetch` から `WebFetch(domain:...)` に改められています（ハイライト 5 参照）。

- [Claude Code settings reference - Claude Code Docs (English)](https://code.claude.com/docs/en/settings-reference#disableallhooks)

## 3. インタラクティブモード

追加 52 行・削除 0 行。**Wait for a usage limit to reset** の節が Session recap と PR review status の間に丸ごと挿入されただけで、既存の記述は 1 行も変わっていません。機能そのものはハイライト 2 のとおりなので、ここでは Claude Code が自分から待機を始めない条件と、そもそも待機を提供しない条件を扱います。

**自分からは待たないが、その場の人が自分で始められる**のは 3 つの場合です。[Remote Control](https://code.claude.com/docs/en/remote-control) と[エージェントチーム](https://code.claude.com/docs/en/agent-teams)のチームメイトセッション、リセットが 24 時間より先の場合（週次上限は数日先にリセットすることがあります）、そして Opus または Sonnet の上限に当たったが今動かしているモデルがそのファミリの外である場合です。3 つ目は、次のターンがその上限に当たらない可能性があるためで、plan mode を制限されたファミリで走らせる `opusplan` などのモデル設定はこの例外に当たりません。これらの場合と、自動継続を切っている場合には、自分の端末で上限に当たるとリセットウィンドウごとに 1 回、使用量上限のオプションメニューが開き、**Wait here, then continue automatically** で始まる行を選べば待機が始まります。Remote Control やチームメイトのセッションでは `/rate-limit-options` を自分で実行してメニューを開きます。

**そもそも待機が提供されない**のは、バックグラウンドセッションと `-p` 実行（メニューの行自体が出ません）、API キー・クラウドプロバイダ・従量課金（使用量がリクエスト単位で計測されるためリセットが存在しません）、claude.ai のログインが保存されていない [LLM ゲートウェイ](https://code.claude.com/docs/en/llm-gateway)（保存済みの claude.ai ログインが有効な資格情報である間だけ提供されます）の 3 つです。

切り方は `/config` の **Continue automatically at usage limit** をオフにするか、ユーザー設定で [`autoContinueAtUsageLimit`](https://code.claude.com/docs/en/settings-reference#autocontinueatusagelimit) を `false` にします。`/config autoContinueAtUsageLimit=false` も使え、`-p` でも効きますが、この `key=value` 形式で**オンに戻すことはできません**。無人実行を許す設定であるためです。設定のスコープは `User or managed` で、ユーザー設定・`--settings`・管理設定から読みます。ただしこのキーには例外があり、これら 3 つのどれも設定していない場合に限り、プロジェクトやローカルの設定ファイルがこのキーを設定していると無視ではなく**機能をオフにする**扱いになります。

- [Interactive mode - Claude Code Docs (English)](https://code.claude.com/docs/en/interactive-mode#start-a-wait-yourself)

## 軽微な更新

<!-- light:minor-updates:start -->
今回は 2 日分の取り込みをまとめた対象期間で、差分のあったページは 44 です。差分は `llms-full.txt` のみで、`llms.txt` のページ一覧とページ見出しマップ（`claude_code_docs_map.md`）には差分がありません。changelog にも新しいリリースエントリは加わっておらず、前回の v2.1.241（2026年08月23日）が最新のままです。したがって本サマリで挙げるバージョンは全て、リリースの告知ではなく本文中の「v2.X.Y 以降が必要」という記述に由来します。**大幅更新に入れる基準は前回同様「差分 50 行以上 かつ 内容の変更を伴うこと」**とし、3 ページを大幅更新、残る 41 ページをここで扱います。表の桁揃えを除いた実質の差分で判定しており、たとえば Agent SDK の Python リファレンスは見かけ 134 行の差分ですが、空白を無視して数え直すと 22 行で、内容も既存フィールドへのバージョン注記の追加だけなのでここに回しています。なお本サマリの参考リンクは全て英語版のみです。今回の変更に日本語版が追従していないためで、プロンプトキャッシュとインタラクティブモードの 2 ページを実際に取得して確認したところ、前者は TTL の説明が旧構成（認証方法による場合分け）のままで新設の 2 節が無く、後者には使用量上限の待機の節がありませんでした。他のページは個別には確認していませんが、いずれも同時期に入った同じ機能群の記述であるため未追従とみなし、安全側に倒して英語版のみを載せています。

**新機能**

- `/rate-limit-options` がコマンド一覧に加わりました。claude.ai の使用量上限でリクエストが止まったときに、待って自動継続する・使用クレジットを足す・プランをアップグレードする、の選択肢を出すコマンドです。上限に当たったとき Claude Code が自分で開くこともあります。claude.ai サブスクリプションが必要で、コマンドメニューには出ないため全部打つ必要があります。待って継続する行は v2.1.234 以降です（詳細はハイライト 2 参照）— [English](https://code.claude.com/docs/en/commands#all-commands)
- Notification フックのマッチャに `quota_auto_resume_fired`・`quota_auto_resume_stale`・`quota_auto_resume_disabled` の 3 つが加わりました（v2.1.234 以降）。順に、リセット時または待機中の操作で使用量が復活して続行したとき、スリープが約 30 分を超えて `Enter` 待ちになったとき、待機がタスクを続けずに終わったときに発火します。最後の 1 つは `Esc` / `Ctrl+C` や **Don't continue automatically** による明示的なキャンセルでは発火しません。あわせて、待機中は `idle_prompt` を送らず、待機が自然に終わったときは代わりにこの 3 つのいずれかが発火することが明記されました — [English](https://code.claude.com/docs/en/hooks#notification)
- 同じ 3 マッチャがフックのガイドの一覧表にも追加されました — [English](https://code.claude.com/docs/en/hooks-guide#filter-hooks-with-matchers)
- 環境変数に `CLAUDE_CODE_PROMPT_CACHE_TTL` と `CLAUDE_CODE_SUBAGENT_PROMPT_CACHE_TTL` が加わりました（v2.1.242 以降、詳細はハイライト 1 参照）。あわせて `ENABLE_PROMPT_CACHING_1H` の説明が「サブスクリプションではメイン会話に 1 時間が自動適用される」という書き方に改められ、`FORCE_PROMPT_CACHING_5M` が上書きする対象に新しい 2 変数と 2 設定が加わりました — [English](https://code.claude.com/docs/en/env-vars#variables)
- `/usage` のプラン使用量の内訳に **Loops** の行が加わりました（v2.1.242 以降）。直近に走った `/loop` などのスケジュールタスクのうち重いものをトークン合計の多い順に並べ、残りは件数で示します。各行には発火頻度・実行回数・合計トークン・1 回あたりトークン・最終実行が出ます。行はタスクのプロンプトでキーされるので、止めて作り直しても 1 行のままです。VS Code 拡張の Account & usage ダイアログには Loops の行は出ません — [English](https://code.claude.com/docs/en/costs#plan-usage-breakdown)

**機能改善**

- プロンプトキャッシュのページで、TTL の説明が「認証方法による場合分け」から「リクエストのバケットによる場合分け」に全面的に書き直されました（詳細はハイライト 1 参照）— [English](https://code.claude.com/docs/en/prompt-caching#which-ttl-each-request-gets)
- 権限のページに、素の `WebFetch` ルールとドメイン指定ルールの違いを説明する節が新設されました（詳細はハイライト 5 参照）— [English](https://code.claude.com/docs/en/permissions#allow-or-deny-every-fetch)
- サンドボックスのページで、ドメイン制御に関わるルールの表記が `WebFetch(domain:...)` に統一され、サンドボックスが尊重するワイルドカードの形が明記されました（詳細はハイライト 5 参照）— [English](https://code.claude.com/docs/en/sandboxing#network-isolation)
- プロンプトキャッシュの TTL を用途別に選ぶ導線が、Amazon Bedrock・Google Cloud の Agent Platform・Microsoft Foundry・Claude Platform on AWS の 4 ページに 1 文ずつ加わりました（詳細はハイライト 1 参照）— [English](https://code.claude.com/docs/en/prompt-caching#choose-the-ttl-yourself)
- ワークフローのエージェントは、メイン会話の TTL バケットの外なのでサブスクリプションでも既定 5 分であり、1 時間にするには `subagentPromptCacheTtl` を `1h` にする、という説明が加わりました。プロセス内のチームメイトについても、エージェントチームのページに同じ趣旨の説明が入っています — [English](https://code.claude.com/docs/en/workflows#prompt-caching-in-a-fan-out)
- Agent SDK のコスト追跡のページも 2 バケット構成に追従しました。自分のターンはメイン会話のバケットに入ること、サブエージェントなどはバケットが別で TTL の制御も別であること、`promptCacheTtl` を `1h` にすれば使用クレジットを引き出している間もメイン会話の 1 時間キャッシュを維持できることが書き足されています — [English](https://code.claude.com/docs/en/agent-sdk/cost-tracking#extend-the-prompt-cache-ttl-to-one-hour)
- エラーリファレンスに `You've hit your Sonnet limit` が加わりました。Opus と Sonnet の上限はそれぞれそのモデルファミリへのリクエストにだけ効くので、`/model` でファミリ外のモデルに切り替えれば作業を続けられます。ただしモデルごとにプロンプトキャッシュが別なので、次のリクエストはキャッシュヒットなしで会話全体を読み直します。あわせて、対話セッションでリセットを待って自動継続できることと、その表示・キャンセル方法への導線が加わりました（v2.1.234 より前は待機が提供されませんでした）— [English](https://code.claude.com/docs/en/errors#youve-hit-your-session-limit)
- 組織のポリシーチェックが拒否したリクエストが、拒否メッセージを載せた `API Error:` 行として出ることが自動リトライの節に加わりました。管理者が Claude Enterprise の Inference hooks で設定するもので、メッセージ末尾は管理者が設定した指示（既定では管理者に連絡するよう促す文）になります。拒否はリクエストの内容に関するものなので、Claude Code は同じモデルにもフォールバックモデルにも再送しません。v2.1.239 より前は、ストリーミングなしやフォールバックモデルで再送してから拒否を表示することがありました。モデル設定のページのフォールバック条件にも同じ例外が加わっています — [English](https://code.claude.com/docs/en/errors#automatic-retries)
- 自己署名証明書のエラーメッセージに `Check your proxy or corporate SSL certificates` が付きました — [English](https://code.claude.com/docs/en/errors#ssl-certificate-errors)
- Desktop アプリの **Auto-continue when limits reset** チェックボックスと、CLI の `/config` にある **Continue automatically at usage limit** は別物なので個別にオフにする必要がある、と明記されました — [English](https://code.claude.com/docs/en/errors#youve-hit-your-session-limit)
- コスト管理のページに、管理者向けの案内として、開発者が v2.1.234 以降で自動継続を使えること、フリート単位で自動継続の開始可否を決めるには管理設定で `autoContinueAtUsageLimit` を設定することが加わりました。使用量上限の説明も、モデル切り替えが効く場合と効かない場合を整理する形に組み替えられています — [English](https://code.claude.com/docs/en/costs#plan-usage-breakdown)
- コンパクション後に何が残るかの表が書き直されました。plan mode で Claude が書いた計画はディスクから再注入され、`paths:` frontmatter を持つルールとサブディレクトリのネスト CLAUDE.md は「一致するファイルを読むたびに Claude Code が再読込する」となり、Claude が読んだ・編集したファイルを更新の新しい順に最大 5 件再読込する行が加わりました。5,000 トークンを超えるファイルは中身なしのパス参照として `Read` ではなく `Referenced file` の形で戻りますが、ルールは再読込されます。フックの行も「フックはコードなので該当なし」から、フックが以前に足したコンテキストは会話と一緒に要約される・`compact` ソースに一致する SessionStart フックは実行して出力を足す、の 2 行に分かれました。あわせて `/rewind` で **Summarize from here** / **Summarize up to here** を選び会話の一部だけコンパクトする導線も加わっています — [English](https://code.claude.com/docs/en/context-window#what-survives-compaction)
- ツールリファレンスの WebFetch の説明が書き直されました。Manual と `acceptEdits` モードで出るプロンプトの 3 択（**Yes** はこの 1 回だけ、**Yes, and don't ask again for `<domain>`** はそのリポジトリの `.claude/settings.local.json` に allow ルールを保存、**No, and tell Claude what to do differently** は拒否）が列挙され、`allowManagedPermissionRulesOnly` が設定されていると 2 番目が隠れること、`auto` と `bypassPermissions` は明示的な `ask` ルールに一致するドメインを除いてプロンプトを飛ばすこと、権限ルールが許可していても先に WebFetch のドメイン安全性チェックを通ることが加わりました。サンドボックス化されたコマンドは WebFetch の組み込み事前承認ドキュメントドメインを継承しない一方で、`WebFetch(domain:...)` の許可ルールはサンドボックスも尊重する、という関係も整理されています（詳細はハイライト 5 参照）— [English](https://code.claude.com/docs/en/tools-reference#webfetch-tool-behavior)
- セルフホスト環境のフックについて、運用者がランナーホストの `~/.claude/` から配ったフックに加えて、サーバー管理設定も MDM 配布の Claude Code ポリシーも管理層を供給しない場合に限り、ランナーイメージの管理設定ファイルのフックも実行されることが加わりました。同じ追記がフックリファレンスとクラウド環境の設定の両ページに入っています — [English](https://code.claude.com/docs/en/cloud-environments#what-carries-over-from-your-setup)
- 組織向けの MCP 制御のページで、用語が「設定ソース」から「設定スコープ」に統一され、管理スコープの許可／拒否リストは Claude Code が選んだ 1 つの管理ソースから取ることが明記されました — [English](https://code.claude.com/docs/en/managed-mcp#allow-claude-ai-connectors-alongside-the-managed-set)
- 設定のページで、リストキーのマージ規則の説明に `modelPicker` がモデル系リストキーの 3 つ目として加わりました。あわせて、リポジトリの設定ファイルでは無視されるキーの説明に `autoContinueAtUsageLimit` の例外が加わり、ユーザー設定・`--settings`・管理設定のどれもこのキーを設定していない間は、リポジトリのファイルがこの機能をオフにできることが示されました — [English](https://code.claude.com/docs/en/settings#where-settings-live)
- 管理設定のページで、管理層のマージ規則に `modelPicker`（後のものが丸ごと置き換える）が加わり、`disableCommandPluginSources` の一覧表に `headersHelper` のブロックが追記されました。組織向けセットアップのページでも、管理値が下位層を置き換えるキーに `modelPicker` が加わっています — [English](https://code.claude.com/docs/en/managed-settings#precedence-within-the-managed-tier)
- LLM ゲートウェイの接続とプロトコルの両ページに、`modelPicker` で `replaceBuiltInOptions` を使うとゲートウェイのモデル検出が見つけた名前もピッカーから消えること（現在のセッションが使っているモデルの行は残ります）が加わりました。トラブルシュートの「モデルがピッカーに出ない」の原因と対処にも同じ項目が入っています — [English](https://code.claude.com/docs/en/llm-gateway-connect#add-gateway-models-to-the-model-picker)
- モデル設定のページに `modelPicker` への導線が 3 か所加わりました。`availableModels` でピンした古いモデル ID が独立行として出る説明、複数モデルを並べたい場合の案内、`ANTHROPIC_CUSTOM_MODEL_OPTION` の行の並び順（組み込みの後、`modelPicker` の行はさらにその後）です。キャッシュ TTL への導線も 2 バケット版に差し替えられました — [English](https://code.claude.com/docs/en/model-config#available-models)
- プラグイン作成とプラグインリファレンスの `bin/` の説明に、組織設定経由で配るプラグインには含められない旨が加わりました（詳細は大幅更新 1 参照）。あわせて `claude plugin install` / `claude plugin update` の `-y, --yes` が、`command` ソースのコマンドだけでなくアーカイブダウンロードを認証する `headersHelper` の承諾もカバーすることが明記されました（`headersHelper` の承諾は v2.1.238 以降）— [English](https://code.claude.com/docs/en/plugins-reference#plugin-install)
- プラグイン依存のページに、`command` ソースまたは `headersHelper` を持つマーケットプレイスエントリの依存は自動インストールの対象外で、ユーザーが先に自分で入れる必要があることが加わりました。プラグインの探索のページにも、`headersHelper` を持つエントリはバックグラウンドの自動更新から外れ、`/plugin` の Errors タブに出ることが加わっています — [English](https://code.claude.com/docs/en/plugin-dependencies#declare-a-dependency-with-a-version-constraint)
- 権限モードのページで、`defaultMode` の JSON 例 2 つが別セクションへの導線に置き換えられ、`auto` がプロジェクト設定・ローカル設定で効かない説明から「Claude Code v2.1.142 以降」というバージョンの限定が外れました — [English](https://code.claude.com/docs/en/permission-modes#switch-permission-modes)
- ネットワーク設定のページで、GitHub まわりの記述が **GitHub allow lists and firewalls** という独立した見出しにまとめられました。GitHub Enterprise Cloud で IP 制限をかけている場合、GitHub App の IP 許可リスト継承を有効にするだけでなく、Anthropic の outbound IP アドレスを許可リストに追加する必要があることが加わっています。継承がカバーするのは Claude GitHub App がインストールとして出すリクエストだけで、ユーザーの代理で出すリクエストは対象外だからです。GitHub Enterprise Server のページでも、参照先が「Anthropic API IP addresses」から「outbound IP addresses」に改められました — [English](https://code.claude.com/docs/en/network-config#github-allow-lists-and-firewalls)
- VS Code のページで、ステータスバーの **✱ Claude Code** をクリックする導線に条件が付きました。`preferredLocation` を `sidebar` にしているか **Claude Code: Open in Side Bar** で開いた場合に出るもので、2 か所とも同じ書き足しです。Focus view については、Claude の保留中の質問が対象にしているテキストが残る挙動が v2.1.225 以降であることが分けて書かれ、Toggle Focus view のキーバインドにも v2.1.221 以降が必要である旨が追記されました — [English](https://code.claude.com/docs/en/vs-code#extension-settings)
- セッション管理のページに、セッションピッカーの復帰先の例外が加わりました。同じリポジトリの別 worktree のセッションはその場で再開しますが、そのセッションの worktree が既に無い場合は現在のディレクトリで再開します。無関係なプロジェクトのセッションは `cd` と再開コマンドをクリップボードにコピーしますが、そのディレクトリが既に無い場合は失敗する `cd` をコピーせず現在のディレクトリで再開します — [English](https://code.claude.com/docs/en/sessions#where-the-session-picker-looks)
- worktree のページで、`**/` で始まるパターンが、まるごと gitignore されたディレクトリの中身をコピーする条件が明記されました。そのディレクトリ自身がパターンに一致するか、`**/` の次の名前がディレクトリのパス上の名前と一致する場合に限ります（`**/.claude/skills/*.md` なら `.claude` が一致するのでコピーされます）。届かない場合は `vendor/**/config.json` のようにディレクトリ名を書きます。v2.1.239 より前は前者の場合しかコピーしませんでした — [English](https://code.claude.com/docs/en/worktrees#copy-gitignored-files-into-worktrees)
- Agent SDK のスキルのページで、プロジェクト・パーソナルスキルの `allowed-tools` frontmatter が SDK セッションでも適用されるようになりました。従来は CLI を直接使うときだけ効き、SDK では `allowedTools` オプションで管理するよう案内されていましたが、今回から frontmatter が効き、`allowedTools` は追加の事前承認手段という位置づけになっています。不正な形式やワイルドカード形式のスキル名を Claude Code の起動前に弾くチェックは、TypeScript Agent SDK 0.3.221 / Python Agent SDK 0.2.129 以降です — [English](https://code.claude.com/docs/en/agent-sdk/skills#pre-approve-tools-for-skills)
- Agent SDK の Python リファレンスで、既存フィールドに必要な SDK バージョンの注記が付きました。`parent_agent_id` と `forward_subagent_text` が 0.2.140 以降、`resume_session_at`・`resume_drops_turn`・`origin`・会話の差し替えイベントが 0.2.137 以降、`skills` の名前検証が 0.2.129 以降です。`resume_drops_turn` は従来「Claude Code v2.1.223 以降が必要、同梱の CLI は条件を満たす」と書かれていましたが、「Python Agent SDK 0.2.137 以降かつ Claude Code v2.1.223 以降が必要で、その SDK に同梱される CLI は Claude Code 側の条件を満たす」に改められました — [English](https://code.claude.com/docs/en/agent-sdk/python#claudeagentoptions)
- Agent SDK のツール検索で、コンパクション時の挙動が「以前に見つけたツールが外れることがあり、必要に応じて再検索する」から「SDK が古いメッセージをコンパクトしても、見つけたツールは読み込んだままにする」に変わりました — [English](https://code.claude.com/docs/en/agent-sdk/tool-search#how-tool-search-works)
- Claude apps ゲートウェイの設定で、`cli` に書く管理設定はサーバー管理設定の**代わりに**管理層へ適用されるため、`policyHelper` や `wslInheritsWindowsSettings` のように OS レベルのポリシーソースに限定された設定は無視されることが明記されました — [English](https://code.claude.com/docs/en/claude-apps-gateway-config#managed)
- コマンドリファレンスで、`/config` の `key=value` 形式はパネルでの確認が要る設定（`autoContinueAtUsageLimit` など）をオンにはできないがオフにはできる、と明記されました。`/config --help` の説明も「設定可能な全キーとその選択肢を列挙」から「受け付けるキーを列挙」に改められています。`/usage` の説明はプラン使用量の内訳への導線に簡潔化されました — [English](https://code.claude.com/docs/en/commands#all-commands)
- Google Cloud の Agent Platform のページで、レート制限の引き上げに関する案内が独立した段落に分けられました — [English](https://code.claude.com/docs/en/google-vertex-ai#additional-resources)

**その他**

- クイックスタートの表で、`claude "task"` の説明が「1 回限りのタスクを実行」から「最初のプロンプト付きで対話モードを開始」に訂正されました。実際の挙動に合わせた修正です — [English](https://code.claude.com/docs/en/quickstart#essential-commands)
- 今回も表の区切り行の桁揃えの入れ替えが差分行数を膨らませています。空白を無視して数え直すと、Agent SDK の Python リファレンスは 134 行から 22 行、フックリファレンスは 74 行から 18 行、フックのガイドは 67 行から 13 行、プラグインリファレンスは 52 行から 12 行、管理設定は 43 行から 5 行になります。実質 50 行を超えたのは大幅更新に挙げた 3 ページだけでした
- ページ見出しマップ（`claude_code_docs_map.md`）に差分がありません。`modelPicker`・`promptCacheTtl` などの新設節や、インタラクティブモードの使用量上限の待機の節がマップに反映されていないため、マップだけを見ていると今回の新設節を取りこぼします
<!-- light:minor-updates:end -->

## 新着情報

<!-- light:whats-new:start -->
（今回の対象期間に新着情報ページの追加・更新はありません。前回のサマリで扱った Week 34（2026年08月17日～21日）が最新のままです）
<!-- light:whats-new:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-08-22.md](./archives/latest/2026-08-22.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-08-22.md](./archives/latest-detail/2026-08-22.md)

<!--
base_commit: 38adb8c17987c2872a55345390bf77b43146ab00
head_commit: 961fa881bd3d4366c49a34b34508be3172b7c2fc
generated_at_full: 2026-08-25T15:13:17+09:00
-->
