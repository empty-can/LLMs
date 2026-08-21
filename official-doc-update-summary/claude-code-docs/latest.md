---
対象期間: 2026年08月19日 〜 2026年08月20日
作成日: 2026-08-20
---

# Claude Code 公式ドキュメント更新サマリ

```markdown
今回は 1 日分の取り込みで、60 ページに差分がありました。changelog には v2.1.238 の 1 リリースが加わっています。新規ページ・削除ページはなく、v2.1.238 で入った挙動変更を各ページに書き下ろす更新が中心です。

主要なものを以下に挙げます。

1. アーティファクトにコメントが付けられるようになり、Claude が自分で返信できるようになった
2. 権限プロンプトの Yes / No に一言添えて答えられるようになった
3. MCP の接続が新しいクライアントランタイム v2 に切り替わった
4. MCP の `headersHelper` がトラスト済みフォルダでしか動かなくなった
5. 別セッションがアイドルになったら 1 度だけ知らせてもらえるようになった
```

## ハイライト

1. [**アーティファクトのコメントと Claude の自動返信**](./latest-detail.md#1-アーティファクトのコメントと-claude-の自動返信):  
  組織内で共有したアーティファクトにコメントスレッドが付き、`@claude` を付けたコメントは Claude が読んで返信できる。公開したセッションが動いている間は、Claude が自分から返信・編集するところまで解説された。
2. [**権限プロンプトにコメントを添えて答える**](./latest-detail.md#2-権限プロンプトにコメントを添えて答える):  
  Yes / No にカーソルを合わせて `Tab` を押すとコメント欄が開き、承認・拒否の理由を Claude に渡せる。`Esc` はコメント無しの No と同じ扱いになった。
3. [**MCP クライアントランタイム v2 への切り替え**](./latest-detail.md#3-mcp-クライアントランタイム-v2-への切り替え):  
  v2.1.232 以降は MCP TypeScript SDK 2.0 ベースの v2 ランタイムが既定になり、プロトコル改定 `2026-07-28` の打診・通知ストリーム・チャネルの制約が新設節としてまとまった。
4. [**headersHelper はトラスト済みフォルダでしか動かない**](./latest-detail.md#4-headershelper-はトラスト済みフォルダでしか動かない):  
  プロジェクトの `.mcp.json` やローカルスコープの `headersHelper` は、そのフォルダのトラストダイアログを受け入れるまで実行されなくなった。作業ディレクトリの決まり方と、資格情報の環境変数が除去される条件も明文化された。
5. [**別セッションがアイドルになったら 1 度だけ知らせてもらう**](./latest-detail.md#5-別セッションがアイドルになったら-1-度だけ知らせてもらう):  
  前回 changelog だけで告知された `notify_when_idle` に専用の節ができた。同じマシンの別セッションが次にアイドルへ入るか終了したときに、1 度だけ通知が返る。

## 新規追加されたページ

（今回の対象期間に新規追加されたページはありません。削除されたページもなく、`llms.txt` の差分は Agent SDK の Todo 追跡ページのタイトルと説明が変わった 1 行だけでした）

## 大幅に更新されたページ

- [**Agent SDK の Todo 追跡ページの全面改稿**](./latest-detail.md#1-agent-sdk-の-todo-追跡ページの全面改稿) ([English](https://code.claude.com/docs/en/agent-sdk/todo-tracking#model-availability)):  
  追加 218 行・削除 193 行で今回最大の差分。ページ名が「Todo Lists」から「Track todos」に変わり、`TodoWrite` からの移行節が消えて Task ツール前提の解説に一本化された。
- [**MCP**](./latest-detail.md#2-mcp) ([English](https://code.claude.com/docs/en/mcp#server-status-detail)):  
  追加 80 行・削除 17 行。クライアントランタイム v2 と `headersHelper` の 2 つの新設群（ハイライト 3・4 参照）に加え、ディスカバリキャッシュが既定オフに変わった。
- [**ツールリファレンス**](./latest-detail.md#3-ツールリファレンス) ([English](https://code.claude.com/docs/en/tools-reference)):  
  追加 46 行・削除 46 行。ただし内容が変わったのは `SendMessage` の行だけで、残りはツール表の桁揃えの引き直し。
- [**エラーリファレンス**](./latest-detail.md#4-エラーリファレンス) ([English](https://code.claude.com/docs/en/errors#the-proxy-refused-the-connection)):  
  追加 82 行・削除 5 行。プロキシが接続を拒否した場合と、セッションをホストするアプリがサインアウト・アカウント切り替えした場合の節が新設された。
- [**Agent SDK の MCP**](./latest-detail.md#5-agent-sdk-の-mcp) ([English](https://code.claude.com/docs/en/agent-sdk/mcp#httpsse-servers)):  
  追加 29 行・削除 50 行。HTTP / SSE サーバーの例からタブ切り替えが外れ、`.mcp.json` の書き方は同ページ内の別節へ委ねる形に整理された。
- [**セルフホスト環境リファレンス**](./latest-detail.md#6-セルフホスト環境リファレンス) ([English](https://code.claude.com/docs/en/self-hosted-environments-reference#runner-cli-flags)):  
  追加 33 行・削除 30 行。v2.1.238 の新フラグ 3 つが CLI フラグ表に加わり、既存のドレイン系フラグの説明もそれに合わせて書き直された。
- [**セルフホスト環境のデプロイ**](./latest-detail.md#7-セルフホスト環境のデプロイ) ([English](https://code.claude.com/docs/en/self-hosted-environments-deploy#defer-the-drain-past-the-first-signal)):  
  追加 54 行・削除 3 行。最初のシグナルでドレインせず稼働を続ける設定と、送出プロキシへの認証の 2 節が新設された。
- [**キーボードショートカットのカスタマイズ**](./latest-detail.md#8-キーボードショートカットのカスタマイズ) ([English](https://code.claude.com/docs/en/keybindings#chat-actions)):  
  追加 29 行・削除 27 行。`Ctrl+L` / `Cmd+K` の二度押しによる `/clear` が廃止され、`confirm:cycleMode` にコメント欄との関係が加わった。
- [**権限の設定**](./latest-detail.md#9-権限の設定) ([English](https://code.claude.com/docs/en/permissions#when-your-local-settings-file-needs-trust)):  
  追加 43 行・削除 11 行。権限プロンプトのコメント欄（ハイライト 2 参照）に加え、`settings.local.json` のトラスト判定とトラスト前の挙動の表が書き直された。

## 軽微な更新

今回は 1 日分の取り込みをまとめた対象期間で、差分のあったページは 60 です。changelog には v2.1.238（2026年08月20日）の 1 リリースが加わりました。上記の大幅更新 9 ページを除く 51 ページの変更をここで扱います。なお本サマリの参考リンクは全て英語版のみです。今回変更のあったページは日本語版がまだ追従していないためで、MCP とアーティファクトの 2 ページを実際に確認したところ、いずれも新設された節が無く、旧記述のままでした。

**新機能**

- `keybindingFlavor` 設定が加わりました。`"readline"` にするとプロンプトの Ctrl+W が Bash と同じく直前の空白まで削除します。既定の `"classic"` は変わりません（v2.1.238）
- `CLAUDE_CODE_BS_AS_CTRL_BACKSPACE` が加わり、ターミナル設定のページにも Windows で Backspace が単語ごと消える場合の対処が新設されました。Windows では `^H` を Ctrl+Backspace として読むため（`TERM_PROGRAM` が `mintty`、`TERM` が `cygwin` の場合を除く）、プレーンな Backspace で `^H` を送るターミナルではこの変数を `0` にします — [English](https://code.claude.com/docs/en/terminal-config#fix-backspace-deleting-a-whole-word-on-windows)
- 組み込みの出力スタイルに **Concise** が加わったことがページ側にも記載されました。結果から述べて前置きと実況を省き、既定では短く返しますが、説明や詳細を求めれば省略せずに答え、エラー報告・セキュリティ警告・破壊的な操作の確認は常に全文を保ちます（v2.1.237）— [English](https://code.claude.com/docs/en/output-styles#built-in-output-styles)
- VS Code 拡張のスクリーンリーダー対応が新設節としてまとまりました。設定は不要で、返答（完成時に 1 度）・権限リクエストや質問・状態変化・エラーとモデル関連のプロンプトを読み上げます。ターンごとに視覚的に隠された見出しが付くため見出しナビゲーションで移動でき、`Tab` でトランスクリプトへフォーカスも移せます。セッションを開き直したときは何も読み上げません（v2.1.236）— [English](https://code.claude.com/docs/en/vs-code#use-a-screen-reader)
- `/goal` にアイドル時のチェックインが加わりました。対話セッションでは、次のプロンプトを待たずに Claude Code が自分でターンを開始してチェックインを届けます。最初のチェックインの後は待ち時間が倍々になり、間隔の 4 倍が上限です（既定なら 1 時間後、以降 2 時間ごと）。`-p` のような非対話セッションではターン終了時のみです（v2.1.236）— [English](https://code.claude.com/docs/en/goal#background-work-defers-evaluation)
- セルフホストランナーに `--defer-shutdown-max-min` と `--proxy-authorization-command` / `--proxy-authorization-file` が加わりました（v2.1.238、詳細は大幅更新 6・7 参照）— [English](https://code.claude.com/docs/en/self-hosted-environments-reference#runner-cli-flags)
- プラグインマーケットプレイスの `headersHelper` が加わりました。url マーケットプレイスやカタログエントリで、カタログと同一オリジンのアーカイブ取得用に HTTP ヘッダ（短命トークンなど）を作るコマンドを走らせます。カタログエントリの `headersHelper` はそのプラグインをインストール・更新するときだけ、コマンドを表示したうえで `[y/N]` を尋ねてから動きます（v2.1.238）
- `SDKControlInitializeResponse` に `hooks_applied` が加わりました。`initialize` リクエストが運んだ `hooks` を登録したかを示すもので、セッション最初の initialize と、CLI の標準入力経由で送った再度の initialize では `true`（後者は登録済みのフックを置き換えます）、リモートセッションへ送った再度の initialize では `false` になり、後から参加したクライアントが先のフックを置き換えられないようになっています（Agent SDK v0.3.238 以降）— [English](https://code.claude.com/docs/en/agent-sdk/typescript#sdkcontrolinitializeresponse)
- `SDKTaskStartedMessage` に `is_backgrounded` と `spawn_depth` が加わりました。前者は `"local_agent"` と `"local_bash"` のタスクに付き、フォアグラウンドで動く場合は `false`（開始したツール呼び出しはタスクが終わるかバックグラウンドへ移るまでブロックされます）。後者は `"local_agent"` のみで、メインスレッドが起動したサブエージェントが `1`、その入れ子が `2` と続きます。再開したサブエージェントは常に `is_backgrounded: true` です（Agent SDK v0.3.238 以降）— [English](https://code.claude.com/docs/en/agent-sdk/typescript#sdktaskstartedmessage)
- 環境変数の一覧に `CLAUDE_CODE_ARTIFACT_COMMENTS` と `CLAUDE_CODE_ARTIFACT_COMMENTS_AUTOREACT` が加わりました（v2.1.221 / v2.1.228、詳細はハイライト 1 参照）— [English](https://code.claude.com/docs/en/env-vars#variables)
- 環境変数の一覧に `MCP_PROTOCOL_NEGOTIATION` が新設され、`MCP_SDK_GENERATION` の説明も v1 / v2 の実体を明記する形に書き直されました。フィーチャーフラグの取得が要る機能の一覧にも、v2 ランタイムとプロトコル打診の項目が加わっています（詳細はハイライト 3 参照）— [English](https://code.claude.com/docs/en/env-vars#features-that-need-feature-flag-fetching)
- 環境変数の一覧にディスカバリキャッシュの `MCP_DISCOVERY_CACHE_TTL_S`・`MCP_DISCOVERY_CACHE_MAX_STALE_S`・`MCP_DISCOVERY_CACHE_STRIKES` の 3 つが加わりました（v2.1.238、詳細は大幅更新 2 参照）— [English](https://code.claude.com/docs/en/env-vars#variables)

**機能改善**

- フルスクリーンで `Ctrl+L` / `Cmd+K` を 2 秒以内に二度押ししても `/clear` が走らなくなりました。会話を消すには `/clear` を実行します。iTerm2 と Terminal.app では `Cmd+K` をターミナル自身が処理して画面を消しますが、Claude Code はそれを検知して会話を描き直します（v2.1.238、詳細は大幅更新 8 参照）— [English](https://code.claude.com/docs/en/fullscreen#clear-the-conversation)
- フルスクリーンの起動に失敗した場合の節が新設されました。最初のフレームを描いた後 10 秒持ちこたえるか `/exit`・Ctrl+C・Ctrl+D で終えれば「起動成功」で、そこに至る前にクラッシュすると次のセッションは従来のレンダラーで始まり、1 回目と 2 回目で別のメッセージが出ます。2 回目以降は Claude Code を更新するか `/tui fullscreen` を実行するまで従来のレンダラーのままです。失敗回数は Claude Code のバージョンごとに数え、成功でリセットされます。`CLAUDE_CODE_NO_FLICKER=1` を設定したセッションは失敗後もフルスクリーンで描かれ、回数にも数えません（v2.1.236）— [English](https://code.claude.com/docs/en/fullscreen#fullscreen-renderer-didnt-finish-starting)
- `/tui fullscreen` の再起動が引き継ぐものに `--agent`・`--agents`・`--append-system-prompt` が加わりました。起動時のダイアログを受け入れた場合の `tui` 設定の保存も、再起動したセッションが起動に成功してからになりました — [English](https://code.claude.com/docs/en/fullscreen#enable-fullscreen-rendering)
- `/model` でモデルを切り替えるときの確認ダイアログが、キャッシュがまだ生きているときだけ出るようになりました。会話で最後にリクエストを送ったか Claude が応答してからキャッシュ TTL 未満なら確認し、TTL 以上たっていれば確認せずに切り替えます。エフォートの変更も同じ確認に従い、既に有効な水準に解決される変更ではキャッシュを保ったまま確認なしで適用されます。v2.1.238 より前は TTL を見ずに、キャッシュが切れていても確認していました（v2.1.238）— [English](https://code.claude.com/docs/en/prompt-caching#switching-models)
- プロンプト候補が出ない条件に「アカウントが利用上限に近いか達している」が加わりました。上限に達するまで出し続けたい場合は `CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION` を `true` にします。v2.1.238 より前は、この変数を `true` にしていても上限付近では候補を出しませんでした（v2.1.238）— [English](https://code.claude.com/docs/en/interactive-mode#when-claude-code-skips-suggestions)
- サンドボックスの重なりの表に、ワイルドカードの `denyRead`（`~/**/.env` など）が広い `allowRead` の内側でも維持される行が加わりました。設定のページ側でも、ワイルドカードが一致したディレクトリの中身も読めなくなること、v2.1.236 より前の macOS では広い `allowRead` に覆われた場所で再開放されていたことが明記されています（v2.1.236）— [English](https://code.claude.com/docs/en/sandboxing#configure-sandboxing)
- `policyHelper` が他の管理設定を置き換える条件が 6 ページにわたって書き直されました。従来は「`policyHelper` が設定されていれば管理ソースをすべて置き換える」でしたが、「管理階層の優先順位で勝ったソースが MDM またはファイルベースで、それが `policyHelper` を設定している場合に、ヘルパーの出力がそのソースを置き換える」に変わりました。サーバー管理設定が空でない構成を配っている間は、MDM やファイルの `policyHelper` は動きません。設定・サーバー管理設定・Claude apps gateway とその構成リファレンス・組織向けセットアップ・Agent SDK の `managedSettings` の各記述がこれに合わせて直っています — [English](https://code.claude.com/docs/en/settings#precedence-within-the-managed-tier)
- `--bare`（`CLAUDE_CODE_SIMPLE`）が自動検出を飛ばす対象に、カスタムコマンドとサブエージェントが明記されました。一方で `--add-dir` で渡したディレクトリの `.claude/skills/` のスキルは読み込まれる（`.claude/commands/` と `.claude/agents/` は飛ばす）という例外も加わっています — [English](https://code.claude.com/docs/en/headless#start-faster-with-bare-mode)
- `claude -p` を SIGTERM で止めたときの挙動が独立した節になり、内容も精密になりました。進行中のターンは中断されず結果も記録されないため、走っていたコマンドは kill 済みとして、回答待ちの権限プロンプトは未回答として記録され、終了処理が始まった後は `SessionEnd` 以外のツール・モデルリクエスト・フックは開始されません。セッションを再開するとその地点から続きます。SDK ホストがセッションを閉じる場合は入力を先に閉じるためシグナルの前に待機中のプロンプトが取り消されます。ターンをきれいに終えたい場合は、プロセスを止める前に SIGINT（SDK なら `interrupt()`）を送ります — [English](https://code.claude.com/docs/en/headless#stop-a-run-with-sigterm)
- Hooks リファレンスと worktree のページの双方に、worktree に入った後の `${CLAUDE_PROJECT_DIR}` の扱いが注記として加わりました。この変数はセッションを開始したプロジェクトルートを指したまま動かず、Claude が今いるディレクトリはフック入力 JSON の `cwd` から読みます（`cd` にも追随します）— [English](https://code.claude.com/docs/en/hooks#reference-scripts-by-path)
- クロスセッションメッセージで、受信側が拒否・ドロップしたときに送信側へ伝わるようになりました。受信側が `refuse` の場合は「クロスセッションメッセージを受け付けていない」という通知が出て、待つな・送り直すなと送信側の Claude に伝えられます。レート制限・重複判定・キュー上限（1 セッションあたり 50 件）でメッセージが落ちた場合も、どれが落としたかが送信側に伝わります（v2.1.238）— [English](https://code.claude.com/docs/en/cross-session-messaging#control-inbound-messages)
- クロスセッションの一覧に、エージェントビューのスーパーバイザプロセスが次のバックグラウンドセッション用に温めているワーカーが、作業を割り当てた後にだけ現れる旨が加わりました — [English](https://code.claude.com/docs/en/cross-session-messaging#see-which-sessions-claude-can-reach)
- Remote Control で接続したデバイスからできることが増えました。バックグラウンドで動いているサブエージェントやワークフローをデバイスから止めると手元のマシンでも止まり、ターンの途中で送ったプロンプトはキューに入りターン終了後もデバイスのトランスクリプトに残ります。デバイスからモデルを選ぶとセッションがそのモデルで動き、ターミナルの `/model`・`/status`・`/config` にも反映されます（デバイスのモデルコントロールからの選択は現在のセッション限り、`/model <name>` を送った場合は新規セッションの既定にもなります）。`claude remote-control` が提供するセッションがクラッシュしても、デバイスからメッセージを送れば提供し直されます。接続後の HTTP 403 は最大 3 分再試行し、それ以上続く場合は何が拒否したか（ネットワークエッジか、自分のネットワークのプロキシ・VPN・ファイアウォールか）を示して切断します（v2.1.238）— [English](https://code.claude.com/docs/en/remote-control#what-connected-devices-see)
- Remote Control が「研究プレビュー」ではなく全プラン提供として書かれ、`Remote Control is not yet enabled for your account` のエラーが `Remote Control isn't enabled for this account` に改称されました（v2.1.239 で改称）。原因の説明も「ロールアウトが届いていない」から「アカウントレベルの可用性チェックがオフを返した。よくある原因はプラン変更後の古いキャッシュ」に変わり、`claude auth logout` / `login` に加えて古いバージョンなら更新するよう案内が付いています — [English](https://code.claude.com/docs/en/remote-control#remote-control-isnt-enabled-for-this-account)
- サブエージェントのページに、エージェントファイルのインライン MCP サーバーがフォルダのトラストを要する旨が加わりました。プロジェクトや `--add-dir` の `.claude/agents/` にあるファイルのインラインサーバーは、そのフォルダをトラストするまで読み込まれず、`~/.claude.json` に書くべきキーがデバッグログに出ます。名前で既存サーバーを参照する場合や、`~/.claude/agents/`・`--agents`・SDK の `agents` オプション・管理設定由来のエージェントファイルは対象外です（v2.1.238、詳細はハイライト 4 参照）— [English](https://code.claude.com/docs/en/sub-agents#scope-mcp-servers-to-a-subagent)
- `claude plugin validate` の節が 4 つの小節（指定するディレクトリの選び方 / ルートの `SKILL.md` を持つプラグイン / シンボリックリンクの先 / 検証結果の読み方）に再編されました。内容は前回の対象期間に入ったものと同じで、読み進めやすさのための再構成です — [English](https://code.claude.com/docs/en/plugin-marketplaces#validate-a-plugin-or-a-directory-without-a-manifest)
- Agent SDK のサブエージェントのページで、利点を並べた 4 つの h3 が 1 つの箇条書きにまとめられ、あわせてフォークしたサブエージェントの場合はコンテキストが新規に始まるわけではない旨が加わりました — [English](https://code.claude.com/docs/en/agent-sdk/subagents#benefits-of-using-subagents)
- `REVIEW.md` の効き方の説明が書き直されました。従来の「全エージェントのシステムプロンプトに最優先で注入される」から、「検出・検証を行うエージェントがリポジトリのレビュー指示として受け取り、順位付けと報告を行うエージェントは重大度を決めてレビューを書く前に参照する」という書き方になっています。あわせて関連リンクに Anthropic のセキュア開発ライフサイクルの記事が加わりました — [English](https://code.claude.com/docs/en/code-review#reviewmd)
- 用語集の 3 項目が更新されました。auto モードの分類器は「ツール結果を一切見ない」から「ツール結果を取り除いた状態で見る」に、`--bare` は上記の対象追加に、出力スタイルはカスタムスタイルが `keep-coding-instructions: true` を設定しない限り組み込みのソフトウェアエンジニアリング指示を外すこと・組み込みスタイルに Concise が加わったことに、それぞれ直っています — [English](https://code.claude.com/docs/en/glossary#output-style)
- コマンド一覧とモデル設定のページで、`/model` の確認に関する記述がプロンプトキャッシュのページへの参照に置き換えられました。`/run`・`/run-skill-generator`・`/verify` からは v2.1.145 以降が必要という注記が外れています — [English](https://code.claude.com/docs/en/model-config#setting-your-model)
- Amazon Bedrock と Google Cloud の Agent Platform のページに、`ANTHROPIC_DEFAULT_MODEL` でセッションを開始した場合はバックグラウンドタスクもそのモデルを使う旨が加わりました — [English](https://code.claude.com/docs/en/amazon-bedrock#4-pin-model-versions)
- セルフホスト環境の概要とライフサイクル設定にも v2.1.238 の変更が反映されました。ポーリング要求は 10 秒でタイムアウトし、失われた場合は 1〜2 秒後に再試行して以降は最大 20 秒まで間隔を倍にする（リースの期限が近いときは短縮する）ことと、`post-session` フックがセッション解放の前に走るか後に走るかがターンの状態で決まること（v2.1.236 以降）が加わっています — [English](https://code.claude.com/docs/en/self-hosted-environments-configuration#post-session)
- デスクトップアプリの受信制御で、拒否した場合にその旨が Claude デスクトップアプリへ報告されるようになりました — [English](https://code.claude.com/docs/en/desktop#work-across-sessions)
- ルーティンとデスクトップの定期タスクのページで、サイドバーの **Routines** に至る導線が「デスクトップアプリの **Code** タブで」と明示されました — [English](https://code.claude.com/docs/en/routines#create-a-routine)
- Agent SDK の `promptSuggestions` オプションと `prompt_suggestion` メッセージの説明に、ターンによっては候補が生成されないこと（利用上限付近など）と、その条件を示すページへの参照が加わりました — [English](https://code.claude.com/docs/en/agent-sdk/typescript#options)
- Agent SDK の `task_started` の説明から「バックグラウンドの」という限定が外れ、フォアグラウンドのタスクでも発行されることが読み取れるようになりました — [English](https://code.claude.com/docs/en/agent-sdk/typescript#sdktaskstartedmessage)
- Agent SDK の Hooks のページで、MCP ツール名の付き方（`mcp__<server>__<action>` の `<server>` は `mcpServers` 設定のキー）の説明が Tip から `matcher` の表と本文に移されました — [English](https://code.claude.com/docs/en/agent-sdk/hooks#matchers)
- プラグインのヒントで、インストールを促すプロンプトを出すのはユーザーが打ち込んでいるメインの対話セッションだけであることが明記されました。サブエージェントのコマンドや `-p` / Agent SDK では出ませんが、コマンド出力からヒント行を取り除く処理はいずれの場合も行われます — [English](https://code.claude.com/docs/en/plugin-hints#what-the-user-sees)
- コスト管理のページに、ゴールのアイドル時チェックインが（セッションが待機していてもターンを開始してコンテキスト全文を送るため）コストに効く旨と、`CLAUDE_CODE_GOAL_CHECKIN_MINUTES=0` で切れることが加わりました（v2.1.236）— [English](https://code.claude.com/docs/en/costs#background-token-usage)
- スクリーンリーダーのページに、スクリーンリーダーモードはターミナルの UI にだけ効くもので VS Code 拡張のチャットパネルでは不要である旨が加わりました — [English](https://code.claude.com/docs/en/accessibility#turn-on-screen-reader-mode)
- ディープリンクのページで、GitHub がカスタム URL スキームを剥がす話が冒頭の注記からトラブルシューティングの節への参照 1 文に集約されました — [English](https://code.claude.com/docs/en/deep-links#the-link-renders-as-plain-text-instead-of-being-clickable)
- アーティファクトの共有で、作成者名が誰に見えるかが整理されました。組織内で共有したアーティファクトではタイトルメニューに、公開したアーティファクトではサインイン済みの同じ組織のビューアに対してページヘッダーに名前が出ます。サインインせずに公開リンクを開いた場合や組織外のビューアには、名前の代わりに `Content is user-generated and unverified.` というラベルが表示されます — [English](https://code.claude.com/docs/en/artifacts#share-an-artifact)
- 起動時のパフォーマンスが改善され、素の `claude` が macOS でより早く起動するようになりました（v2.1.238）
- シェルの条件式に含まれる zsh 固有の構文について、Bash ツールの権限チェックが改善されました（v2.1.238）
- 自動更新チェックが起動から約 10 秒後に走るようになり、起動時の CPU を奪わなくなりました（v2.1.238）
- 同梱の `claude-api` スキルが、Managed Agents の 8 月 19 日リリース（ウェブ検索・取得のドメイン設定、セルフホストサンドボックスのメモリストア）に合わせて更新されました（v2.1.238）
- `claude mcp list` と `claude mcp get` が、無効化されたサーバーにヘルスチェックのために接続せず `⊘ Disabled` と表示するようになりました（v2.1.238）

**バグ修正**

以下は v2.1.238（2026年08月20日）の changelog に `Fixed` として載った修正です。

- 長い対話セッションでメモリが際限なく増える問題を修正し、表示ウィンドウから外れたサブエージェントのツール結果を解放するようにした
- カスタム・プロジェクト・プラグインの出力スタイルが、セッションの途中で既定の文体に戻ってしまう問題を修正
- `CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION=true` が、アカウントが利用上限の手前（超過はしていない）にあるときにプロンプト候補を保てない問題を修正
- worktree の隔離による Bash の拒否が、リダイレクトの無いコマンドに対して「リダイレクトを外せ」と告げる問題を修正
- セルフホストランナーが、遅い／失われたポーリング要求 1 回でサーバーから除去され、正常なセッションが別のランナーへ渡ってしまう問題を修正
- MCP のエリシテーションダイアログが 4,096 文字を超える URL で何も表示しない問題と、権限プロンプトがプロジェクトパスの幅に収まらないときに「今後は聞かない」の選択肢を落とす問題を修正
- Bash コマンドが kill・タイムアウト・中断されたときに `/tmp/claude-*-cwd` が残る問題を修正
- Backspace として Ctrl+H を送るターミナルで、キー入力がまとめて届く（遅い SSH / mosh 回線）と Backspace の長押しが無視される問題を修正
- 権限プロンプトの差分表示で、絵文字のような複数コードポイントの文字やタブを含む行が切れてしまう折り返しの問題を修正
- Ctrl+Z でサスペンドしたセッションを kill すると、ターミナルがブラケットペーストモードのままカーソルが隠れた状態になることがある問題を修正
- stdio の MCP サーバーが `initialize` の前に `server/discover` を受け取り、遅延起動のサーバーがセッションを開くたびにバックエンドを起動させられる問題を修正
- プロキシによる接続拒否が、プロキシを名指しせず汎用のネットワークエラーとして報告される問題を修正（詳細は大幅更新 4 参照）
- `/model` と `/effort` のキャッシュミス警告が、プロンプトキャッシュが既に切れているときにも出る問題を修正
- Remote Control のタスクパネルからのタスク単位の Stop が、CLI がホストするセッションで何も起きない問題を修正
- クライアントが有効な role の無いユーザーメッセージを渡したときにリモートセッションが終了する問題を修正
- `claude remote-control` で開始した Remote Control セッションが、起動したシェルのセッションスコープの環境変数を引き継いでしまう問題を修正
- プロセスがクラッシュした Remote Control セッションが、`claude remote-control` を再起動するまで使えないままになる問題を修正（次にメッセージを送れば再利用できるようになった）
- ターンの途中に web やデスクトップから送った Remote Control のメッセージが、ターン終了後にトランスクリプトから消える問題を修正
- 電話や web で選んだ Remote Control のモデルが、ターミナル側の表示に反映されない問題を修正
- 短いネットワークの不調でサインインの更新が遅れたときに、Remote Control が「login expired」で切断する問題を修正（再試行して接続を保つようになった）
- サインアウト時に Remote Control が再接続の失敗を報告する問題を修正（サインアウトで明確なメッセージとともにセッションを終えるようになった）
- `claude remote-control`（サーバーモード）やデスクトップ／IDE がホストするセッションで、`ListAgents` / `SendMessage` が「Remote Control is not connected」と報告する問題を修正
- `ListAgents` と `SendMessage` が、エージェントビューが次のバックグラウンドセッション用に温めているアイドルワーカーを露出させる問題を修正（タスクが割り当てられてから現れるようになった）

**その他**

- `llms.txt` の差分は 1 行だけで、Agent SDK の Todo 追跡ページのタイトルが「Todo Lists」から「Track todos」に、説明も新しいものに変わりました（詳細は大幅更新 1 参照）
- ページ見出しマップには、今回の `llms-full.txt` にはまだ現れていない見出しが 2 つあります。インタラクティブモードの **Make Ctrl+W delete back to whitespace**（`keybindingFlavor` の解説と思われます）と、Hooks リファレンスの PostToolUse 配下の **Annotate a result for the auto mode classifier** です。次回以降の取り込みで本文が入る見込みです
- Agent SDK のカスタムツール・ファイルチェックポイント・ワークフローの 3 ページで、内容の重複していた末尾の節（関連ドキュメントの箇条書き、チェックポイントが追跡する対象の再掲、`/workflows` のコードブロック）が削除されました
- スキルのページ冒頭から、スキルのディレクトリ構成を示すツリーと `SKILL.md` の説明が削除され、同ページ内の **Add supporting files** への参照に置き換えられました — [English](https://code.claude.com/docs/en/skills#add-supporting-files)
- 認証・LLM ゲートウェイの接続とロールアウトの 3 ページ、およびセキュリティガイダンスから、`v2.1.146` / `v2.1.144` 以降という古いバージョン条件の注記が削除されました — [English](https://code.claude.com/docs/en/llm-gateway-rollout#distribute-through-managed-settings)

## 新着情報

（今回の対象期間に更新された新着情報ページはありません。前回に続き Week 32 が最新のままです）

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-08-19.md](./archives/latest/2026-08-19.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-08-19.md](./archives/latest-detail/2026-08-19.md)

<!--
base_commit: a4f51fbfe83670c58f484e3fb81935316a500138
head_commit: 374b2af0b3a3dbc0f997d926da13c0fbf25fa843
generated_at_full: 2026-08-21T15:10:21+09:00
-->
