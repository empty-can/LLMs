---
対象期間: 2026年10月15日 〜 2026年10月16日
作成日: 2026-10-16
---

# Claude Code 公式ドキュメント更新サマリ

```markdown
**今回は、changelog に v2.1.302（2026年10月16日、63 項目）が積まれ、フォークのサブエージェントが `claude -p`・Agent SDK・デスクトップアプリ・VS Code でも既定でオンになりました。VS Code のページは節の並びが組み替えられて「Security and privacy」の節が外れ、mod の `Text` には書体の 4 つの props が、`Box` には間隔のステップ名が載り（v2.1.299 以降）、Desktop の SSH セッションでは macOS と Linux ならサードパーティのプロバイダーでも終了後に実行中のタスクへ戻れるようになりました（Claude Desktop v2.42304.0 以降）**。新しいページはなく、ページ単位で数えると 228 ページ中 37 ページ（changelog を含む）が変わり、changelog を除く変更は 547 行（追加 327・削除 220）、大幅更新は `vs-code` の 1 ページです。総行数は 120,654 行から 120,838 行に増えました。

主要なものを以下に挙げます。

1. v2.1.302 でフォークのサブエージェントが `claude -p`・Agent SDK・デスクトップアプリ・VS Code でも既定でオンになり、サードパーティのプロバイダーの `-p` と SDK の開始モード、`CLAUDE_CODE_AUTO_MODE_MODEL`、`/config` の `Idle compaction` の行なども加わった
2. `vs-code` の節の並びが組み替えられ（「Run work in the background」の新しい h2 など）、Restricted Mode などを勧めていた「Security and privacy」の節が外れた
3. mod の `Text` に `size`・`weight`・`mono`・`tabular` の props が、`Box` の間隔の props に `'xs'`〜`'xl'` のステップ名が加わり（v2.1.299 以降）、`bold` は `weight` を勧めて非推奨になった
4. Desktop の SSH セッションで、macOS と Linux ではサードパーティのプロバイダーでも Claude Desktop v2.42304.0 以降で始めたタスクなら、終了して開き直した後に実行中のタスクへ戻れるようになった
5. Agent SDK のフックの例が `.env` を大文字・小文字を問わず断る形になり、`Write|Edit` の matcher では Bash の書き込みを防げないという警告と、サンドボックスの `denyWrite` の案内が加わった
```

## ハイライト

1. [**v2.1.302 でフォークのサブエージェントが既定でオンになる範囲が広がった**](./latest-detail.md#1-v21302-でフォークのサブエージェントが既定でオンになる範囲が広がった):  
  changelog に v2.1.302（2026年10月16日）の 63 項目が積まれました。フォークのサブエージェントがターミナルと同じく `claude -p`・Agent SDK・デスクトップアプリ・VS Code でも既定でオンになり、サードパーティのプロバイダーでの `-p` と SDK の開始モード、`CLAUDE_CODE_AUTO_MODE_MODEL`、`/config` の `Idle compaction` の行、単独の Claude Design の終了の通知などが加わっています。これらの変更は、対応する通常のページにはまだ反映されていません
2. [**VS Code のページの節が組み替えられ Security and privacy の節が外れた**](./latest-detail.md#2-vs-code-のページの節が組み替えられ-security-and-privacy-の節が外れた):  
  `vs-code` で、チェックポイントでの巻き戻しと端末の出力の参照が「Use the prompt box」の下へ移り、「Run work in the background」の h2 ができ、MCP の 2 節が h2 になりました。コードの扱いと、信頼できないコードでの Restricted Mode などの対策を述べていた「Security and privacy」の節は外れ、「Next steps」にセキュリティとデータの使用のページへのリンクが加わっています
3. [**mod の Text に書体の props と Box に間隔のステップ名が加わった**](./latest-detail.md#3-mod-の-text-に書体の-props-と-box-に間隔のステップ名が加わった):  
  `plugins/mods/reference` に「`Box` spacing steps」「`Text` typography props」「Replace `bold` with `weight`」の節ができました。`Box` の間隔の props は `'xs'`〜`'xl'` のステップ名も受け取り、`Text` は `size`・`weight`・`mono`・`tabular` で書体を求められます（いずれも v2.1.299 以降）。`bold` は非推奨で、`weight: 'semibold'` への置き換えを勧めています
4. [**Desktop の SSH タスクにサードパーティのプロバイダーでも戻れるようになった**](./latest-detail.md#4-desktop-の-ssh-タスクにサードパーティのプロバイダーでも戻れるようになった):  
  `desktop` の SSH セッションの節で、終了後に実行中のタスクへ戻れないのは、Windows の Desktop と、サードパーティのプロバイダーで Claude Desktop v2.42304.0 より前に始めたタスクだけになりました。macOS と Linux のそれ以外のタスクは、Desktop がプロセスに入り直せれば続きます
5. [**Agent SDK のフックの例に Bash の書き込みは防げないという警告が加わった**](./latest-detail.md#5-agent-sdk-のフックの例に-bash-の書き込みは防げないという警告が加わった):  
  `agent-sdk/hooks` の最初の例が `.env` を大文字・小文字を問わず断る形になり、`Write|Edit` の matcher では Bash による書き込みにフックが動かないという警告と、サンドボックスの設定への案内が加わりました。`agent-sdk/python` と `agent-sdk/typescript` には `denyWrite` に絶対パスを書く説明が載り、別のフックの deny がタイムアウトより優先されるという記述は外れています

## 新規追加されたページ

（今回の対象期間に新規追加・削除されたドキュメントページはありません。`llms.txt` は変わらず、`llms-full.txt` に展開されている固有のページも 228 のままで、`Source:` の行が 231 あり 3 ページが 2 回展開されている状態も前回と同じです）

## 大幅に更新されたページ

- [**Use Claude Code in VS Code**](./latest-detail.md#1-use-claude-code-in-vs-code) ([日本語](https://code.claude.com/docs/ja/vs-code#use-the-prompt-box) / [English](https://code.claude.com/docs/en/vs-code#use-the-prompt-box)):  
  323 行（追加 191・削除 132）が変わりました。節の並びの組み替えと「Security and privacy」の節の削除（詳細はハイライト 2）のほかは、長い段落を箇条書きや番号付きの手順に分ける書き換えが大半です

## 軽微な更新

今回の差分は **2 ファイル**（`llms-full.txt`・見出しマップ）で、`llms.txt` は変わっていません。`llms-full.txt` の生の差分は追加 404 行・削除 220 行で、ページの並びは変わっていないため、ページ単位に切り出して数えても同じ量です。228 ページ中 **37 ページ**が変わり、changelog が 77 行（追加のみ）、ほかの 36 ページが 547 行（追加 327・削除 220）です。大幅更新の `vs-code` を除く **36 ページ**（changelog を含む）と、changelog に加わった **v2.1.302**（2026年10月16日、63 項目。Added 4・Changed 9・Improved 7・Fixed 43）を以下にまとめます。changelog の項目はすべて v2.1.302 のもので、前回の v2.1.301 との間の版の項はありません。

`llms-full.txt` の総行数は **120,654 行から 120,838 行へ 184 行増え**ました。`Source:` の行は 231、固有のページは 228 のままで、2 回展開されている 3 ページ（`plugins/create`・`plugins/install`・`plugins/mods/overview`）も前回と同じです。

**新機能**

- `CLAUDE_CODE_AUTO_MODE_MODEL` を追加（詳細はハイライト 1 参照）
- `/config` にアイドル時の圧縮をオフ・オンにする `Idle compaction` の行を追加（詳細はハイライト 1 参照）
- `/design-sync` と `/design-login` に、単独の Claude Design が 2026年12月14日までに終了するという通知を追加（詳細はハイライト 1 参照）
- [Cloud sessions] ルーティンのページに、最後の実行が始まらなかった理由（組織が同時に動かせるクラウドのセッションの上限に達したなど）を示すバナーを追加
- **mod の `Text` に書体の props が、`Box` の間隔の props にステップ名が加わった**（`plugins/mods/reference`・`plugins/mods/interface`。詳細はハイライト 3 参照）
- **テーマに `composerSidebarBackground` のトークンが加わった**（`terminal-config` の「Fullscreen mode」）。差分のパネルや mod のペインのような、会話の横のパネルの背景の色で、`userMessageBackgroundHover`・`selectionBg` と同じくフルスクリーンの描画でだけ使われます — [日本語](https://code.claude.com/docs/ja/terminal-config#fullscreen-mode) / [English](https://code.claude.com/docs/en/terminal-config#fullscreen-mode)

**機能改善**

- 権限モードを指定しない `claude -p` と Agent SDK のセッションが、サードパーティのプロバイダーで、テレメトリがオフか新しいインストールのとき `default` モードで始まるよう変更（詳細はハイライト 1 参照）
- フォークのサブエージェントを `claude -p`・Agent SDK・デスクトップアプリ・VS Code でも既定でオンに変更（詳細はハイライト 1 参照）
- デスクトップアプリと VS Code が、メインの会話のサブエージェントを常にバックグラウンドで動かすよう変更（詳細はハイライト 1 参照）
- フッターの `← for agents` のヒントを、セッションを開いて 10 秒後に隠すよう変更。自分を待っているエージェントの数は出たままです
- Claude in Chrome の指示のシステムプロンプトの中の位置を変更。新しい会話が共有のプロンプトキャッシュから読めるようになります
- prompt と agent のフックが、1 つのイベントにつき同時に 12 個までしか動かないよう変更（詳細はハイライト 1 参照）
- 組織のポリシーが `/feedback` をオフにしているときのメッセージを変更。組織の管理者ではなく GitHub の issue を案内します
- [Claude Tag] Claude Tag の管理設定で、Claude のアクセスを Bundles・Connectors・Skills and plugins・Channels の 4 つのタブにまとめるよう変更
- [Claude Tag] 組織の設定の Roles のページで、Claude Tag のチャンネルの管理者のために作られたロールを、組織自身のロールの下の折りたたんだまとまりに入れるよう変更
- 多くのプラグインを有効にしたときの起動の時間を改善。プラグインのコマンドとエージェントのファイルの読み込みに要るファイルシステムの呼び出しがずっと減り、特に Windows で効きます
- サーバー側の分類器を使う auto モードを改善。安全確認に長すぎる会話を圧縮するようになり、確認するツールの呼び出しがすべて断られることはなくなります（詳細はハイライト 1 参照）
- 別のフォルダーから開き直したバックグラウンドのセッションに LLM ゲートウェイがないときのメッセージを改善。「Not logged in」ではなく理由を示します
- [Cloud sessions] クラウドのセッションが始まらないときのエラーを改善。「Something went wrong」ではなく「Connection lost」か「Server error」と示します
- [Claude Tag] Claude Tag の管理設定のリポジトリの検索を改善。接続した GitHub のアカウント 100 個までを対象にし、GitHub App のインストールの最初の 5,000 個より後のプライベートのリポジトリも見つけます
- [Claude Tag] Claude Tag の管理設定の Add place を改善。入力か貼り付けたチャンネルを、組織のチャンネルの一覧が読み込み終わるのを待たずにすぐ挙げます
- [Claude Tag] Claude Tag の管理設定のワークスペースかチャンネルのページの Add > Domain を改善。すべてのチャンネルの読み込みを待たず、そのページが読み込まれれば使えます
- **Desktop の SSH タスクの終了の後の扱いが改められた**（`desktop`。詳細はハイライト 4 参照）
- **Agent SDK のフックの例とサンドボックスの `denyWrite` の説明が改められた**（`agent-sdk/hooks`・`agent-sdk/python`・`agent-sdk/typescript`・`hooks`。詳細はハイライト 5 参照）
- **スキルを重ねて呼べるのはターミナルのプロンプトだけと明記された**（`skills` の新しい小見出し「Stack several skills in one message」）。ターミナルの Claude Code のプロンプトでは 1 つのメッセージの頭に複数のスキルを重ねられますが、Agent SDK か `claude -p` では最初のスキルだけを読み込み、行の残りをその引数にします。`commands` の冒頭も「ターミナルのプロンプトでは」と改められ、`code-review-local` のリンク先がこの小見出しに、`agent-sdk/skills` の案内から「skill stacking」の語が外れました。v2.1.218 より前は `/code-review` がインラインで動いて重ねられた、という文は `skills` から外れています — [日本語](https://code.claude.com/docs/ja/skills#stack-several-skills-in-one-message) / [English](https://code.claude.com/docs/en/skills#stack-several-skills-in-one-message)
- **応答のヘッダーが届かない要求の終わり方と `API_TIMEOUT_MS` の役割が載った**（`network-config` の「Streaming idle watchdogs」・`env-vars`・`errors`）。レスポンスヘッダーがまったく届かない要求は、ファーストバイトの期限が動く接続ではその期限で最初の試行が終わり（変えるには `CLAUDE_STREAM_FIRST_BYTE_TIMEOUT_MS`）、ほかの接続ではボディのアイドルのタイムアウトが働く 5〜6 分後に終わる（早めるには `API_TIMEOUT_MS` を下げる）、と冒頭にまとめられました。ファーストバイトの期限は Claude apps gateway のセッションでも動かず、ボディのアイドルのタイムアウトはヘッダーを待つ時間も数えます。`API_TIMEOUT_MS` はヘッダーを待つ時間を限るので、ファーストバイトの期限が動かない場合は `300000`（5 分）より小さくすると応答のない要求を早く再試行できる一方、最も長いヘッダーの待ちや非ストリーミングの要求より大きくしておく、という項目も加わっています。`env-vars` のこの変数の説明は「ストリーミングの要求はこの時間内にレスポンスヘッダーを受け取る必要がある」になり、上限を超える値はタイマーがあふれて要求がすぐ失敗する、の文が外れました。`errors` の「Automatic retries」の項目からも、ほかの接続では要求が `API_TIMEOUT_MS` まで待つ、の文が外れています — [日本語](https://code.claude.com/docs/ja/network-config#streaming-idle-watchdogs) / [English](https://code.claude.com/docs/en/network-config#streaming-idle-watchdogs)
- **エージェントチームのタスクの一覧はセッションの後も残ると明記された**（`agent-teams` の「Architecture」）。チームの設定のディレクトリはセッションの終わりに消え、タスクの一覧のディレクトリはセッションの後もディスクに残り、保つ期間は `cleanupPeriodDays` で変える、とそれぞれの項目に書かれました。タスクの一覧は「アップロードされず、再開したセッションがタスクを保つ」の文は外れています — [日本語](https://code.claude.com/docs/ja/agent-teams#architecture) / [English](https://code.claude.com/docs/en/agent-teams#architecture)
- **プラグインが見つからないときの案内が、マーケットプレイスのカタログの更新を勧める形になった**（`channels`・`claude-security`・`large-codebases`・`mcp`・`security-guidance`・`skills`）。`Plugin "<name>" not found in marketplace "claude-plugins-official"` と出たら、手元のカタログの写しが古いことがあるので `/plugin marketplace update claude-plugins-official` で更新して再試行し、同じメッセージなら `plugins/troubleshooting` の「Plugin not found in marketplace」を見ます（これまでは「プラグインの名前を確かめる」だけ） — [日本語](https://code.claude.com/docs/ja/claude-security#install-the-plugin) / [English](https://code.claude.com/docs/en/claude-security#install-the-plugin)
- **ほかの mod のバンドだけが出るときの調べ方が載った**（`plugins/mods/troubleshoot` の「Another mod's band shows and yours doesn't」）。プロンプトの上のバンドは 1 つで全 mod が共有し、先に動く mod が `next(e)` の結果を含まない木を返すと後の mod のバンドを置き換えます。両方を出すには、その mod の木で `await next(e)` の結果を `Box` の子に入れ、その `Box` と外側の `Box` に `width`・`height`・`position` などの props を付けないようにします。デバッグログで `answered ui.render without next()` を探せばその mod が分かり、変更の後に何も出ないなら `ui.render (AbovePrompt) refused:` か `does not validate` の行で理由を確かめます — [日本語](https://code.claude.com/docs/ja/plugins/mods/troubleshoot#another-mods-band-shows-and-yours-doesnt) / [English](https://code.claude.com/docs/en/plugins/mods/troubleshoot#another-mods-band-shows-and-yours-doesnt)
- **トークンの数の `cacheCreation` は 2 つのキャッシュの寿命を合わせて数えると明記された**（`monitoring-usage` の「Token counter」）。`"cacheCreation"` の種類は、5 分と 1 時間のキャッシュの寿命での書き込みを合わせて数えます — [日本語](https://code.claude.com/docs/ja/monitoring-usage#token-counter) / [English](https://code.claude.com/docs/en/monitoring-usage#token-counter)
- **サンドボックスの自動許可でも効くチェックの書き方が改められた**（`sandboxing` の「Auto-allow mode」・`permissions`）。「明示的な deny ルールは常に守られる」が「`Bash` の deny ルールが一致する形のコマンドは引き続き断られる」（`permissions#bash-rule-limits` へリンク）に、`rm` と `rmdir` の項目が「重要なパスを対象とすると認識された」コマンドに改められました。`permissions` の「How permissions interact with sandboxing」の plan モードの段落の後の一覧からは、明示的な deny ルールと `rm`/`rmdir` の 2 項目が外れています — [日本語](https://code.claude.com/docs/ja/sandboxing#auto-allow-mode) / [English](https://code.claude.com/docs/en/sandboxing#auto-allow-mode)

**バグ修正**

- ターンを止めたとき、会話の圧縮中だと「Prompt is too long」のエラーが出る問題を修正
- セッションの途中で Vertex か Bedrock に切り替えた後、要求が「diagnostics: Extra inputs are not permitted」で失敗する問題を修正
- Read ツールが、どんな大きさの画像ファイルも、画像のような名前のパイプやデバイスも、まるごとメモリに読み込む問題を修正。128 MB を超える画像のソースは断ります
- ゲートウェイが `anthropic/claude-opus-4-1` のように接頭辞を付けて Opus 4 か 4.1 を名付けると、`/autocompact` と `/effort` が違うモデルに保存する問題を修正
- セッションの途中で加わったツールが ToolSearch で、または圧縮の後に読み込み直されると、プロンプトキャッシュが外れる問題を修正
- `claude plugin` などのサブコマンドが、キューに入った設定の書き込みが終わる前に終了することがあり、変更が失われるか `.tmp` ファイルが残る問題を修正
- git の既定の ref の形式が reftable のとき、プラグインのマーケットプレイスが更新のたびにクローンし直され、新しく入れた git のプラグインの版が「unknown」と出る問題を修正
- PowerShell ツールがプラグインの `bin/` フォルダーのコマンドを見つけない問題と、何も見つからない検索（rg・grep・findstr・git grep）を `Select-Object` などの書式設定のコマンドレットにパイプするとエラーと報告する問題を修正
- デスクトップアプリの Claude が、その選択肢がない場面で、MCP サーバーの認可や再接続に claude.ai の設定や `/mcp` を案内する問題を修正
- Claude が空の編集の一覧を送るとアーティファクトの公開が失敗することがある問題と、アーティファクトの新しい版に断られた後に Claude が誤った方法で更新を再試行する問題を修正
- auto モードの分類器のブロックの大半で OpenTelemetry の `tool_decision` のイベントに `classifier_category` がない問題と、`OTEL_LOGRECORD_ATTRIBUTE_COUNT_LIMIT` が小さいと新しい `tool_decision` の属性が `tool_use_id`・`tool_source`・`tool_parameters` を押し出す問題を修正
- エージェントのビューで、長い一覧を下へ移動するかセクションを折りたたんだ後に行が空のままになる問題を修正
- サインインしていないとき、`claude remote-control --help` が使い方を出さずに終了する問題を修正
- クラウドのセッションで `/design consent` と `/design revoke` が失敗したとき、そこでは使えない `/design-login` を勧める問題を修正。claude.ai/design/settings を案内します
- サーバーがプロトコルの版 2026-07-28 で合意しながら `resultType`・`ttlMs`・`cacheScope` を省くと、MCP サーバーのツールが出ないか、ツールの呼び出しがすべて失敗する問題を修正
- プランがクレジットでしか払わないモデルで、プロンプトの候補が使用量のクレジットを使う問題を修正。クレジットに課金された返答の後は候補を飛ばします
- 折り返されるバッククォートの中の URL が最初の行でしかクリックできない問題を修正。ハイパーリンクに対応する端末では URL 全体が 1 つのリンクになります
- プラグインが見つからないとき、`claude plugin details <name>@builtin` が組み込みのプラグインを出さない `claude plugin list` を勧める問題を修正。`/plugin` を案内します
- リンクがその中で始まる絵文字が 1 列広く折り返され、質問のプレビューで隠れたり、表がリストになったりする問題を修正
- 存在しないディレクトリを指す迷子の `.git` ファイルがあると、git 2.56 以降で worktree の分離が worktree の作成や再開を断る問題を修正
- セッションが新しいプロセスで再開した後、クラウドのセッションの費用と使用量がゼロから数え直される問題を修正
- セルフホストのランナー: git の reftable の形式で保存したチェックアウトを再利用するセッションで、git の fetch が「bad object refs/heads」で失敗する問題を修正
- Windows: exFAT か FAT32 のドライブのプロジェクトで、`--plugin-dir` で始めたセッションを含め、すべてのファイルの書き込みが断られるか確認を求められる問題を修正
- [VSCode] 返答のストリーミング中に、リストの中の閉じていないコードブロックの後の文字が素の文字で出てからコードに変わる問題を修正
- [VSCode] サーバーの URL にクエリ文字列があると、パネルからの MCP サーバーのサインインが壊れた認可のページを開く問題を修正
- [VSCode] Claude の拡張機能のあるブラウザに届かないのに、`@browser` のバナーが「Browser connected」と出る問題を修正
- [Cloud sessions] クラウドのセッションで、最新以外のすべてのメッセージで「Rewind to here」が失敗する問題を修正。セルフホストのランナーには Claude Code v2.1.246 以降が要ります
- [Cloud sessions] GitHub が確かめ直す間、クラウドのセッションのプルリクエストの状態のバーが、マージの衝突のあるプルリクエストを ready に戻す問題を修正
- [Cloud sessions] クラウドのセッションが予期せず止まったルーティンの実行が Completed と、始まる前にアーカイブされた実行が Cancelled と、失敗ではなく表示される問題を修正
- [Cloud sessions] セッションの GitHub のリポジトリの名前が変わるか移った後、クラウドのセッションの差分のビューが変更を欠くか読み込めない問題を修正
- [Cloud sessions] 途中で失敗したスケジュールのルーティンの実行が 1 時間以上後に最初からやり直され、同じレポートを 2 回投稿するような作業の繰り返しが起こりうる問題を修正
- [Cloud sessions] 開いているクラウドのセッションに、別の端末から送ったメッセージが、ページを再読み込みするか別の場所をクリックして戻るまで出ないことがある問題を修正
- [Remote Control] コンピューターがオフラインになった後、Remote Control のセッションでサブエージェントのペインがずっと回り続ける問題を修正。Remote Control が切断されたと示します
- [Claude Tag] Claude が前のメッセージの 1 つを編集して答えた後も、Slack のチャンネルか DM のメンションの下に「is thinking…」が残る問題を修正
- [Claude Tag] Claude の Slack の返信の番号付きか箇条書きの手順の下にあるコードブロックの URL が山括弧で囲まれ、コピーしたコマンドが壊れる問題を修正
- [Claude Tag] Slack で添付した HEIC・SVG・TIFF・BMP の画像が Claude に届かない問題を修正。ほかの種類のファイルと同じく、作業ファイルの中のファイルとして届きます
- [Claude Tag] ロールで Claude Tag を制限する組織で、新しいチャンネルの管理者が Slack の Claude へのアクセスを失う問題を修正。管理者のロールが Slack の Claude Tag も与えます
- [Claude Tag] MCP サーバーが 1 つのホストを共有するカスタムのコネクターが、Claude Tag の管理設定で 1 つのコネクターとして出る問題を修正。サーバーごとに 1 つのコネクターになります
- [Claude Tag] Slack の照会が 1 つ止まったとき、Slack の Claude が DM に「DMs are temporarily unavailable」と答えてそれを捨てることがある問題を修正。先に再試行します
- [Claude Tag] Slack Enterprise Grid での Claude との DM が Slack のワークスペースのドロップダウンを無視する問題を修正。最後に Claude を開いた接続済みのワークスペースで動きます
- [Claude Tag] チャンネルの月の支出上限についての Slack の Claude の通知が、チャンネルの管理者が上げられると言う問題を修正。組織のオーナーを名指しし、使用量のページにリンクします
- [Claude Tag] Claude の Slack の返信のリンクが、直後の太字・斜体の閉じの記号や全角の句読点を取り込み、リンクと書式が壊れる問題を修正
- [Code Review] GitHub の接続のために離れた後、Code Review のセットアップが再開しない問題を修正。管理設定に戻るとリポジトリの選択から開き直します

**その他**

- **セッションを要約から再開するダイアログの説明が外れた**（`sessions`・`costs`・`prompt-caching`）。Pro と Max のプランで、約 1 時間より長く使われず 100,000 トークンを超えるセッションを再開すると **Resume from summary**・**Resume full session as-is**・**Don't ask me again** のダイアログが出る、と述べていた `sessions` の「Resume from a summary」の節が外れ、`costs` の「Why usage climbs in a long session」と `prompt-caching` の「Cache lifetime」からもこのダイアログへの言及が外れました（`prompt-caching` の古いセッションを再開するリンクは `sessions#resume-a-session` へ）。changelog に対応する項目はありません
- **ZDR で使えない機能に「Chat and Cowork unified」が加わった**（`zero-data-retention` の「Features disabled under ZDR」）。クラウドのセッションが要るため、と理由が書かれています — [日本語](https://code.claude.com/docs/ja/zero-data-retention#features-disabled-under-zdr) / [English](https://code.claude.com/docs/en/zero-data-retention#features-disabled-under-zdr)
- **`--debug` の除外の例が `--debug='!1p'` から `--debug='!mcp'` に改められた**（`cli-reference` の「CLI flags」） — [日本語](https://code.claude.com/docs/ja/cli-reference#cli-flags) / [English](https://code.claude.com/docs/en/cli-reference#cli-flags)
- **フックとスキルの比較の「Determinism」の行が改められた**（`features-overview` の「Compare similar features」）。フックは「イベントで必ず発火し、きっかけは保証される」から「Claude の判断なしにイベントで発火する」になりました — [日本語](https://code.claude.com/docs/ja/features-overview#compare-similar-features) / [English](https://code.claude.com/docs/en/features-overview#compare-similar-features)
- **言い回しの調整**: `auto-mode-classifier-billing` の冒頭の段落から「Nothing is broken:」が外れて 2 つの段落に分かれ、`agent-view` の「トランスクリプトは常にローカルに残る」から「常に」が外れ、`plugins/mods/gallery` の `Text` のサンプルの説明が「素の文字と 8 つのスタイルを 1 行ずつ」になりました
- **見出しマップ**: 26 行が加わり 13 行が外れました。加わったのは、ハイライト 2 の `vs-code` の組み替えによる 13 見出し（移った見出し、改めた「Resume cloud sessions from claude.ai」、新しい「Run work in the background」「Interrupted steps after a reload」「Turn off continuation after a reload」）、`skills` の「Stack several skills in one message」、`plugins/mods/reference` の 3 見出し、`plugins/mods/troubleshoot` の「Another mod's band shows and yours doesn't」、新しいスタンプと、次の 7 見出しです。`sub-agents` の「Restrict which tools a subagent can use」、`permissions` の「Precedence among rules, hooks, and mods」「Hook approvals in plan mode」、`sandboxing` の「`/sandbox` prints `Sandbox settings not changed`」、`hooks` の「Failed hooks on Windows without Git Bash」「PreModelSwitch timeouts and other exit codes」、`agent-sdk/permissions` の「Auto mode (`auto`)」の 7 つは、今回の `llms-full.txt` にはまだ見出しがなく、本文の更新は今回の取り込みに入っていません。外れたのは、`vs-code` の移る前の 11 見出し（「Security and privacy」を含む）、`sessions` の「Resume from a summary」、古いスタンプです
- **見出しマップ冒頭の自動生成スタンプが、2026年10月15日 20時03分17秒 UTC から 2026年10月17日 01時28分06秒 UTC へ進みました**

**参考リンクについて**: 日本語版は、ハイライト・大幅更新・軽微な更新で取り上げたページのうち次の 23 ページ（`vs-code`・`plugins/mods/reference`・`plugins/mods/interface`・`plugins/mods/troubleshoot`・`desktop`・`agent-sdk/hooks`・`agent-sdk/python`・`skills`・`commands`・`sessions`・`network-config`・`env-vars`・`errors`・`agent-teams`・`terminal-config`・`zero-data-retention`・`sandboxing`・`permissions`・`monitoring-usage`・`claude-security`・`hooks`・`cli-reference`・`features-overview`）を取得し、該当する節があるかと今回の内容（新しい節や書き換えた文）になっているかを確かめました。今回も日本語版の追従が早く、`vs-code` の日本語版も新しい節の並びになって「Security and privacy」の節がなく、`sessions` の日本語版にも「Resume from a summary」の節がないなど、ほぼすべての節がすでに今回の内容でした。例外は `agent-sdk/python` の `SandboxSettings` で、日本語版には `denyWrite` に絶対パスを書く段落はあるものの、`.env` や `./.env` と書くと作業ディレクトリの `.env` に書き込めてしまう、という最後の注意がまだないため、ハイライト 5 のこのページのリンクは英語版だけにしています。取得して確かめていないページ（`channels`・`large-codebases`・`mcp`・`security-guidance`・`costs`・`prompt-caching`・`auto-mode-classifier-billing`・`agent-view`・`security`・`code-review-local`・`plugins/mods/gallery`・`agent-sdk/typescript`・`agent-sdk/skills`）と、changelog だけに載っていて対応する節のない項目にはリンクを付けていません。**changelog ページへのリンクは、本サマリの方針どおり付けていません。**

## 新着情報

**今回、`whats-new/` 配下のページに変更はありません。**

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-10-15.md](./archives/latest/2026-10-15.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-10-15.md](./archives/latest-detail/2026-10-15.md)

<!--
base_commit: 23d4d90c662169bb09c107096793481648358905
head_commit: 954ed4f3b5d84b7a8a63fa77f4b496af355f42d6
generated_at_full: 2026-10-17T15:13:48+09:00
-->
