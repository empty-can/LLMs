---
対象期間: 2026年08月11日 〜 2026年08月12日
作成日: 2026-08-12
---

# Claude Code 公式ドキュメント更新サマリ

```markdown
今回の対象期間は 62 ページに差分がありました。新規ページと新着情報はありません。目立つのは Agent SDK 側の再整備で、トークンとコストの数え方、サブエージェントの上限、外部ストレージからの再開が相次いで書き直されています。CLI 側では、テレメトリ系の環境変数を設定すると何が使えなくなるかの一覧と、claude.ai から同期したスキルの扱いが新しく文書化されました。

主要なものを以下に挙げます。

1. フィーチャーフラグの取得を切ると使えなくなる機能の一覧が環境変数のページに新設され、十数ページからそこを参照するようになった
2. Agent SDK のトークンとコストの数え方が全面的に書き直され、アシスタントメッセージの出力トークンはプレースホルダーだと明記された
3. サブエージェントの深さ・同時実行数・支出に上限を設ける方法が新しい節としてまとまり、Opus 5 は委譲しやすいという注意が加わった
4. claude.ai から同期したスキルの読み込み場所・名前衝突・本文の扱いが 4 節にわたって文書化された
5. forceLoginOrgUUID が検証するのは claude.ai アカウントのログインだけで、Claude Console のログインは検証しないと明記された
```

## ハイライト

1. [**フィーチャーフラグ取得を切ると使えなくなる機能が一覧化された**](./latest-detail.md#1-フィーチャーフラグ取得を切ると使えなくなる機能が一覧化された):  
  環境変数のページに新しい h2 が加わり、`DISABLE_TELEMETRY` などでフラグ取得を止めたセッションで使えない機能が列挙された。Remote Control・セッション間メッセージング・`claude import`・`/schedule`・advisor・`/loop` の自己ペーシングが対象で、インストール直後の初回セッションにも同じ影響が出る。
2. [**Agent SDK のトークンとコストの数え方が全面的に書き直された**](./latest-detail.md#2-agent-sdk-のトークンとコストの数え方が全面的に書き直された):  
  アシスタントメッセージの `output_tokens` は応答開始時点の値を写しただけのプレースホルダーであり、出力トークンは結果メッセージから読むべきだと明記された。ストリーミング入力モードでの集計方法と、セッションクラッシュ後の合計の復旧手順も新設された。
3. [**サブエージェントの増殖を抑える 3 つの上限が文書化された**](./latest-detail.md#3-サブエージェントの増殖を抑える-3-つの上限が文書化された):  
  ネストの深さ・同時実行数・クエリ全体の支出に上限を設ける方法が SDK のサブエージェントのページにまとまった。あわせて Claude Opus 5 は従来のモデルより委譲しやすいため、これらの上限が特に効いてくることが書かれている。
4. [**claude.ai から同期したスキルの扱いが文書化された**](./latest-detail.md#4-claudeai-から同期したスキルの扱いが文書化された):  
  `CLAUDE_CODE_SYNC_SKILLS` で落としたスキルがどこに読み込まれるか、名前が他のコマンドと衝突したらどうなるか、フロントマターと本文がどう扱われるかが 4 つの節に分かれて説明された。手元のセッションでは `!` コマンドも `@` 参照も実行・展開されない。
5. [**forceLoginOrgUUID が検証するのは claude.ai ログインだけだと明記された**](./latest-detail.md#5-forceloginorguuid-が検証するのは-claudeai-ログインだけだと明記された):  
  「指定した組織以外の資格情報なら起動時に終了する」という説明が書き直され、検証対象は claude.ai アカウントのログインに限られること、Claude Console のログインは組織を照合せず事前選択にしか使われないことが示された。

## 新規追加されたページ

（今回の対象期間に新規追加されたページはありません）

## 大幅に更新されたページ

- [**SDK のサブエージェント**](./latest-detail.md#1-sdk-のサブエージェント) ([English](https://code.claude.com/docs/en/agent-sdk/subagents#cap-subagent-depth-concurrency-and-spend)):  
  変更行数は約 97 行で今回最多。上限 3 種と Opus 5 の委譲に関する節が新設された（詳細はハイライト 3 参照）。
- [**コストと使用量の追跡**](./latest-detail.md#2-コストと使用量の追跡) ([English](https://code.claude.com/docs/en/agent-sdk/cost-tracking#read-output-tokens-from-the-result-message)):  
  変更行数約 96 行。出力トークンの扱いが訂正され、ストリーミング入力とクラッシュ復旧の節が加わった（詳細はハイライト 2 参照）。
- [**MCP で外部ツールに接続する**](./latest-detail.md#3-mcp-で外部ツールに接続する) ([English](https://code.claude.com/docs/en/agent-sdk/mcp#connection-timeouts)):  
  stdio サーバーの例からタブ表示が外れ、接続のタイムアウトとツール呼び出しのタイムアウトの違いが明記された。
- [**スキルで Claude を拡張する**](./latest-detail.md#4-スキルで-claude-を拡張する) ([English](https://code.claude.com/docs/en/skills#how-synced-skills-behave)):  
  claude.ai 同期スキルの節が新設され（詳細はハイライト 4 参照）、名前解決の説明が例付きの箇条書きになった。
- [**Agent SDK TypeScript リファレンス**](./latest-detail.md#5-agent-sdk-typescript-リファレンス) ([English](https://code.claude.com/docs/en/agent-sdk/typescript#task-notification-subkinds)):  
  タスク通知のサブ種別が新設され、`SDKPermissionDeniedMessage` がどの拒否を報告するかが 3 通りに整理された。
- [**セルフホスト環境リファレンス**](./latest-detail.md#6-セルフホスト環境リファレンス) ([English](https://code.claude.com/docs/en/self-hosted-environments-reference#environment-variable-only-settings)):  
  変更行数 77 行のうち大半は表の桁揃え。実質はバックグラウンドタスクの猶予を決める環境変数 1 件の追加。
- [**エラーリファレンス**](./latest-detail.md#7-エラーリファレンス) ([English](https://code.claude.com/docs/en/errors#claude-import-is-not-yet-available-in-this-build)):  
  `claude import` 関連のエントリが 2 件新設され、非対話実行の auto mode が run を中断しなくなった。
- [**セッションを外部ストレージへ永続化する**](./latest-detail.md#8-セッションを外部ストレージへ永続化する) ([English](https://code.claude.com/docs/en/agent-sdk/session-storage#resume-from-the-store)):  
  ストアから再開する経路が新節として文書化され、その場合ローカルの写しが実行終了時に消えることが明記された。
- [**システムプロンプトを変更する**](./latest-detail.md#9-システムプロンプトを変更する) ([English](https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts#improve-prompt-caching-across-users-and-machines)):  
  「ユースケースとベストプラクティス」節が 4 小節ごと削除され、正味で 50 行短くなった。

## 軽微な更新

対象期間には changelog へのリリース追加 1 件（v2.1.229）と、上記 9 ページ以外に 52 ページの更新がありました。なお本サマリの参考リンクは全て英語版のみです。今回変更のあったページは日本語版がまだ追従していないためで、環境変数・スキル・SDK のサブエージェントの 3 ページを実際に確認したところ、いずれも今回の新設セクションが存在しませんでした。

**新機能**

- セッション間メッセージングに `CLAUDE_CODE_MESSAGING_TOKEN` が加わりました（v2.1.228 以降）。受信箱ソケットを bind するセッションが、ソケットのパスと並べてフックや Bash コマンドへ export するセッション単位のトークンで、ソケットへ書き込むスクリプトは接続の 1 行目に `{"type":"auth","token":"<token>"}` を送って同一セッションの子であることを示せます。プロセスによる裏付けが取れない環境（投稿プロセスが終了した後の macOS、Claude Code が PID 1 のコンテナ）ではこのトークンが検証手段になります — [English](https://code.claude.com/docs/en/cross-session-messaging#the-sessions-inbox-socket)
- advisor に Fable 5 を選べるようになりました。「Claude Code は Fable 5 を advisor として提供しない」という注記と、ピッカーで淘汰表示になる・`/advisor fable` を拒否するといった記述が一斉に削除され、`fable` は `opus` / `sonnet` と並ぶエイリアスとして `/advisor`・`--advisor`・`advisorModel` のいずれでも受け付けられます（Fable 5 アクセスが前提）— [English](https://code.claude.com/docs/en/advisor#choose-an-advisor-model)
- Remote Control に **接続中のデバイスに何が見えるか** の節が新設されました。コンパクションと `/clear` は進捗も結果もデバイスに出ること、`/resume` で会話を切り替えても切り替え先のタイトルや履歴はデバイスに届かないが以後のメッセージは双方向に流れること、セッション間メッセージも同じ接続を通ること、接続失敗後に `/remote-control` で再接続する際に会話が書き換わっていればサーバー側セッションはアーカイブされることが整理されています — [English](https://code.claude.com/docs/en/remote-control#what-connected-devices-see)
- Claude apps gateway で、`model` の値が欠けているか空の場合に `model is required` の `400` を返す検証が加わりました（サーバー側 v2.1.228 以降）。Claude Desktop 向けポリシーには Chat タブを出す `chatTabEnabled` と、添付ファイル分析のためにローカルサンドボックスでコードを実行させる `chatAdvancedFileAnalysisEnabled` の 2 キーが追加されています（いずれも既定は無効、サーバー側 v2.1.227 以降）— [English](https://code.claude.com/docs/en/claude-apps-gateway-config#managed)
- v2.1.229 では次の追加もありました。Remote Control の直近セッションを再開する `claude remote-control --continue` の文書化、セルフホストランナーのセッションでサーバー供給の Claude Code フックをサポート、長い思考の間もアイドルタイムアウトで切れないようゲートウェイのストリーミング応答に SSE キープアライブ ping を追加、プラグインマーケットプレイスの `command` ソース（ローカルコマンドがプラグインディレクトリを出力し、セッションごとに再解決されて再起動なしに反映。`mode: "link"` ならその場で使う）、`ListAgents` が切断済み Remote Control セッションを `offline`、自分のクラウドセッションを `cloud` とラベル付け

**機能改善**

- auto memory が保持期間スイープの対象外になりました（v2.1.228 以降）。プロジェクトの `projects/<project>/memory/` はスイープから除外され、ディレクトリ自体も保持期間いっぱい空だった場合にのみ削除されます。それより前はメモリディレクトリ内のフォルダをセッションデータとして扱い、配下の古いファイルを消しうる状態でした。`.claude` ディレクトリのページではこのスイープの例外が 4 つ（`sessions/`・auto memory・bare モード・一時停止）の箇条書きに整理されています — [English](https://code.claude.com/docs/en/claude-directory#cleaned-up-automatically)
- 複数の設定ファイルが同名のマーケットプレイスエントリを定義した場合、Claude Code は最優先のファイルのエントリを丸ごと使うようになりました（v2.1.228 以降）。下位のエントリのフィールドは一切継承しないため、あるファイルの `source.headers` の資格情報が別のファイルが管理する URL と組み合わさることはありません。管理設定のドロップインディレクトリの説明にも、`fallbackModel` のチェーンは後のファイルが置き換える・`extraKnownMarketplaces` の同名エントリも丸ごと置き換わる、という 2 点が加わりました — [English](https://code.claude.com/docs/en/settings#extraknownmarketplaces)
- プラグインキャッシュの掃除の説明に、フォルダの中にディレクトリやシンボリックリンクが 1 つも残っていない場合にのみ削除するという条件が加わりました。開発用チェックアウトをキャッシュのバージョンエントリとしてシンボリックリンクしている場合、Claude Code はそのリンクを孤立扱いにせず、リンクも上位のフォルダも削除せず、バージョン追跡ファイルをリンク先のチェックアウト内に書き込むこともありません — [English](https://code.claude.com/docs/en/plugins-reference#plugin-caching-and-file-resolution)
- Windows で Git Bash を探す順序が明文化されました。`CLAUDE_CODE_GIT_BASH_PATH` が未設定なら、まず既定のインストール先 2 か所、次に `PATH` 上の `git` からその `bin\bash.exe` を使います。ただし Claude Code を起動したフォルダ自体や、その配下で `node_modules` や `.venv` / `env` といった仮想環境フォルダを含むパスにある `git` はスキップされるため、そこに Git があるなら変数で明示します — [English](https://code.claude.com/docs/en/troubleshoot-install#claude-code-on-windows-requires-either-git-for-windows-for-bash-or-powershell)
- fast mode の提供条件が厳密化されました。Console（API 利用者）は管理者が Claude Code preferences で有効化するだけでなく、research preview のため組織にアクセスがプロビジョニングされている必要があり、未プロビジョニングだと API が各リクエストを `429` で拒否し続けます（Claude Code はこれを fast mode のレート制限として扱いますが、クールダウンと違ってアクセスが付くまで解消しません）。claude.ai の Team / Enterprise は Owner による有効化が必要である点も冒頭の要約に加わり、機能可用性のページの表も追従しました — [English](https://code.claude.com/docs/en/fast-mode#enable-fast-mode-for-your-organization)
- `.claude/commands/` が「レガシーフォーマット」ではなくなりました。SDK のコマンドのページの注記は「カスタムコマンドはスキルにマージされた。`.claude/commands/` のファイルと `.claude/skills/<name>/SKILL.md` はどちらも `/name` を作り同じように動く」という説明に書き換えられ、SDK のプラグインのページでもディレクトリ構成図の `commands/` の注釈が「レガシー：代わりに skills/ を使う」から「スキルをフラットな .md ファイルとして置く場所」に改まりました — [English](https://code.claude.com/docs/en/agent-sdk/slash-commands#creating-custom-slash-commands)
- セッション間メッセージングで、Remote Control に接続中のセッションから他マシンのセッションへ送ると、相手の会話にはこちらの Remote Control 名（例: `laptop-graceful-unicorn`）で表示され、相手の Claude はその名前へ返信できることが書かれました。届いたメッセージが送信者名のもとに会話へ残るようになり、「Claude が読んだ後は `Message from` の 1 行に畳まれ `Ctrl+O` で展開する」という記述は削除されています。受信箱ソケットの節では、フラグ取得前に始まったセッションでは取得完了時点で bind と export が行われるため、それ以前に起動したフックには変数が渡らないことも明記されました — [English](https://code.claude.com/docs/en/cross-session-messaging#message-sessions-on-other-machines)
- Claude apps gateway のホストプロセスが Anthropic へ何も送らなくなりました。`claude gateway` は Amazon Bedrock や Google Cloud's Agent Platform のデプロイと同じサードパーティ扱いになります。v2.1.227 より前は製品バージョンやプラットフォームといった起動時テレメトリを送っており、`CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1` で止められました。それらのリリースは起動時に `/api/hello` へ本文も資格情報も無い `HEAD` リクエストを 1 回送っていましたが、応答は無視していたためエグレスファイアウォールで塞いでも影響はありません — [English](https://code.claude.com/docs/en/claude-apps-gateway-deploy#compliance-posture)
- `/tui` でレンダラーを切り替えた際に、直前に `/model` で選んだモデルが引き継がれるようになりました — [English](https://code.claude.com/docs/en/fullscreen#enable-fullscreen-rendering)
- サンドボックス環境のページで Docker Sandboxes の位置づけが変わりました。「Docker Desktop のサンドボックス機能」ではなく Docker の無償の単体製品として紹介され、Docker Desktop を必要とせず Docker Sandboxes を入れた任意のホストで Claude Code を動かせる、と書かれています — [English](https://code.claude.com/docs/en/sandbox-environments#virtual-machine)
- agent view のバージョン履歴に v2.1.227 の行が加わりました。削除しようとしたセッションの worktree ディレクトリで別の Claude Code セッションが動いている場合、セッションも worktree も残され、一覧の行に `not deleted`、フッターに理由（相手のプロセス ID を含む）が出ます。`claude rm` は `kept <id>` と理由を表示します — [English](https://code.claude.com/docs/en/agent-view#what-deleting-a-session-removes)
- 許可リストで弾かれたモデルの代替について、対話セッションで警告が出るのは通常のフォールバックだけでなく、許可された最新版への置換が起きたときも同様であることが明記されました — [English](https://code.claude.com/docs/en/model-config#restrict-model-selection)
- 非対話実行で `acceptEdits` をベースラインにした場合の説明に、読み取り専用コマンド集合は例外である旨と、自動承認される範囲の一覧への参照が加わりました。「そうでないコマンドを試みると run が中断する」という記述は外れています — [English](https://code.claude.com/docs/en/headless#auto-approve-tools)
- プラグインのバージョン解決の説明がマーケットプレイスのページからプラグインリファレンスの該当節への参照に集約されました。git 系ソースで `version` を省くと解決されたコミット SHA が使われる、という要点だけが残っています。オフライン環境の項からは、`git pull` 失敗時に古いクローンを保持し続けるという 1 文も削除されました — [English](https://code.claude.com/docs/en/plugin-marketplaces#version-resolution-and-release-channels)
- セルフホスト環境のランナーのライフサイクルとデプロイの案内が整理されました。退役時にバックグラウンドタスクが残っているセッションは最大 60 秒待って解放し、タスクは終わったが後続ターンが始まっていない場合はそのターンが始まるまで保持することが箇条書きになり、停止猶予の設定方法も `SIGTERM` の猶予期間を持つ環境と `--retire-at` を使う環境の 2 通りに分けて示されています。「セルフホスト環境はセッションの実行を自社ネットワークへ移すのであってコントロールプレーンは移さない」という説明も、Anthropic 側に残るものを先に述べる形に書き換えられました — [English](https://code.claude.com/docs/en/self-hosted-environments#runner-lifecycle)
- v2.1.229 では次の改善も入りました。ワークフローのファンアウトで同じ接頭辞を共有する兄弟エージェントの起動をずらしてプロンプト接頭辞のキャッシュを再利用させる変更（`CLAUDE_CODE_WORKFLOW_PREFIX_STAGGER_MS=0` で無効化）、`prompt is too long` エラーで `/compact` を勧めるだけでなく自動コンパクションが復旧できなかった理由を説明するよう変更、サンドボックスでネットワークドメイン一覧の IPv6 リテラルを角括弧付き（`[::1]:443`）にし曖昧な綴りは fail-closed で強制して `/doctor` が指摘するよう変更、`/login` の成功後にも `CLAUDE_CODE_OAUTH_TOKEN` の上書き警告を再表示、`/commit-push-pr` で `--force` や `--amend` など危険なフラグを伴う git / gh コマンドの自動承認を廃止、Windows のセルフホストランナーは `--base-dir` の明示を必須化（Windows には既定のチェックアウト先が無いため）、VS Code 側では「Report a problem」と `/bug` が組み込みのフィードバックダイアログを開くよう変更・`/btw` のサイド質問パネルを境界のドラッグでリサイズ可能に・サイドバーにセッショングループを追加

**バグ修正**

- 長い応答がストリーミング中に部分的に消え、ターミナルに二重出力される問題が修正されました（v2.1.229）
- ツール呼び出しの `glob` / `file_path` / `command` が文字列以外の値だった場合にエラー画面へクラッシュする問題が修正されました（v2.1.229。該当セッションの `--resume` でも起きていました）
- 非常に狭いターミナルウィンドウでプログレスバーや Markdown テーブルを描画すると RangeError でクラッシュする問題が修正されました（v2.1.229。起動時の `claude --continue` / `--resume` でも起こりえました）
- Windows で、ツール呼び出しやメッセージが拡張長パス（`\\?\`）や UNC パスでファイルを参照するとクラッシュする問題が修正されました（v2.1.229）
- `CLAUDE_CODE_ATTRIBUTION_HEADER` で帰属ヘッダーを無効にしている利用者（Anthropic API への直接接続）で、auto mode が全てのツール呼び出しに失敗する問題が修正されました（v2.1.229）
- カスタムの `ANTHROPIC_BASE_URL` ゲートウェイを使う claude.ai 購読者に対して `/model` が Sonnet / Opus の 1M を拒否する問題が修正されました（v2.1.229）
- 厳格な認可サーバーでの MCP OAuth が、リダイレクト URI に `localhost` ではなく `127.0.0.1` を使うことで修正されました（v2.1.229）
- ノート PC 側のターミナルでスラッシュコマンドを打った後、Remote Control クライアントに作業中スピナーが残る問題が修正されました（v2.1.229）
- `/install-github-app` が生成する Claude Code Review ワークフローが、プルリクエストにレビューを投稿しないまま完了する問題が修正されました（v2.1.229）
- IDE 拡張の接続中に数千件の診断があるファイルを編集した後、UI が数秒間停止する問題が修正されました（v2.1.229）
- 単発の `claude plugin` コマンドが liveness ファイルを残し、古いプラグインバージョンの掃除を妨げうる問題が修正されました（v2.1.229）
- CPU 制限のあるコンテナ内の動的ワークフローが、コンテナの CPU 上限ではなくホストのコア数を使う問題が修正されました（v2.1.229）
- アトミックなファイル置換の後にファイルウォッチャーのハンドルがリークする問題と、Windows でスケジュール実行のウォッチャーがネットワークや仮想ファイルシステム上で失敗した際の未捕捉エラーが修正されました（v2.1.229）
- SDK および `--input-format stream-json` のセッションで、空白のみのメッセージを送ると 400 エラーになる問題が修正されました（v2.1.229）
- メッセージだけで API の 32 MB リクエスト上限を超える会話が、剥がせる画像も文書も無いのにコンパクションを再試行し続ける問題が修正されました（v2.1.229。以後は明確なメッセージとともに 1 度で失敗します）
- Claude Desktop セッションからの OpenTelemetry エクスポートが、Desktop 管理のゲートウェイをテレメトリ送信先にも使っている場合に拒否される問題が修正されました（v2.1.229）
- `managed-mcp.json` を配布したうえでサーバーが MCP サーバーを配信する構成で、セルフホストランナーなどのリモートセッションが起動時に終了する問題が修正されました（v2.1.229。以後は警告付きでスキップされます）
- セルフホストランナーのリポジトリ準備が Git Credential Manager のプロンプトでハングする問題が修正されました（v2.1.229。資格情報が無ければ git が即座に失敗します）

**その他**

- **前回サマリの記述が 1 件撤回されました。** 前回「非対話実行では `Agent aborted: auto mode classifier request refused by the safety safeguard in headless mode` で中断します」と書いた挙動は、今回の更新で run を止めない形に改められています。詳細は本サマリのエラーリファレンスの節を参照してください
- `llms.txt` で変わったのは Agent SDK のセッション永続化ページの 1 行説明のみで（「any host can resume them」→「other hosts can resume your sessions」）、エントリの増減はありませんでした
- 前回サマリで「ページ見出しマップにあるが `llms-full.txt` に未反映」と挙げた 5 項目は、今回すべて本文に反映されました。SDK のコスト追跡の `Track costs in streaming input mode`、SDK のセッションストレージの `Resume from the store`、SDK の TypeScript リファレンスの `Task-notification subkinds`、エラーリファレンスの `claude import is not yet available in this build` と `Could not read Claude Code config` が該当します
- 多数のページで `auto-memory` という表記が `auto memory` に統一されました。環境変数（`CLAUDE_CODE_DISABLE_CLAUDE_MDS` / `CLAUDE_CODE_SAFE_MODE`）、CLI リファレンスの `--safe-mode`、プロンプトキャッシュ、SDK のシステムプロンプトと Python リファレンスが対象です
- いくつかの注記・補足が削除されました。フックリファレンスからは `terminalSequence` が `/dev/tty` 直書きの代替である旨の Note と、`--init` / `--maintenance` が `-p` との併用時のみ Setup フックを発火するという記述、`ConfigChange` の入力に `source` と `file_path` があるという説明が落ちています。権限のページからは `Write(docs/**)` を拒否ルールに書いた場合の警告文の実例と「全ファイルへのアクセスを許可するにはツール名のみを使う」という案内、チェックポイントからは v2.1.216 より前の `/rewind` の挙動、プラグインのページからは「次のステップ」の Note、セキュリティガイダンスとプラグイン依存関係からは各 1 文が削除されました
- `/reload-plugins` の説明から、MCP サーバーを持つプラグインの場合は警告を出してリロードを適用せず `--force` が必要、という記述が削除されました。ultrareview の費用の項からも「無料実行の期間が終わった後」という条件が外れています
- ルーチンのページで、トリガー発火時のプロンプトの扱いが変わったバージョンが v2.1.214 から v2.1.213 に訂正されました。権限モードのページからは、v2.1.203 より前は既定ブランチへの直接 push が一律ブロックされていたという経緯説明が削除されています

## 新着情報

（今回の対象期間に更新された新着情報ページはありません。前回の Week 32 以降、新しい週次ダイジェストは公開されていません）

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-08-11.md](./archives/latest/2026-08-11.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-08-11.md](./archives/latest-detail/2026-08-11.md)

<!--
base_commit: 74a9f7d4d87a53478220a4bbf69fc28fa7c10294
head_commit: 6bb349f9c8d4ed9d313be35f06d8f5b1ff63f332
generated_at_full: 2026-08-13T15:10:03+09:00
-->
