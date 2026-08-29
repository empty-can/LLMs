---
対象期間: 2026年08月27日 〜 2026年08月28日
作成日: 2026-08-28
---

# Claude Code 公式ドキュメント更新サマリ

```markdown
今回は 1 日分の取り込みで、83 ページに差分がありました。差分行は 3 ファイル合計 2849 行（うち `llms-full.txt` が 2687 行）ですが、その多くは表の桁揃えを整えただけの再フォーマットで、桁揃えの差を除いた実質 50 行以上の変更は 7 ページに留まります。ページの新規追加・削除はなく、収録 URL は前後とも 202 件で同じです。前回報告した `llms.txt` の見出し組み替えは一部が巻き戻り、`## English` を頂点とする構成が解けて全体が 1 段上がりました。changelog に加わったのは v2.1.251（2026年08月28日、71 項目）の 1 リリースで、権限チェックの穴を塞ぐ修正が目立ちます。

主要なものを以下に挙げます。

1. プロンプトキャッシュが効いているかどうかを `/usage` とステータスラインで確認できるようになった
2. 組織の契約単価を管理設定に書くと、開発者に見えるコスト表示がその単価に変わるようになった
3. ファイルを開く直前・検索を始める直前にパスの解決を確認し直し、承認した場所を指さなくなっていたら拒否するようになった
4. 拡張思考を切ったまま高い effort を使ったときの API エラーを、Claude Code 側で吸収するようになった
5. ストリーミング応答の「最初の 1 バイトが返るまで」に専用の期限ができ、10 分待たされなくなった
```

## ハイライト

1. [**プロンプトキャッシュの効き具合が `/usage` とステータスラインで見えるようになった**](./latest-detail.md#1-プロンプトキャッシュの効き具合が-usage-とステータスラインで見えるようになった):  
  `/usage` の Session ブロックに `Prompt cache (main)` 行が加わり、リクエスト数・入力トークンのうちキャッシュから読まれた割合・ミス数・キャッシュが今 warm かどうかが並ぶ。ステータスラインのスクリプトも `prompt_cache` オブジェクトから同じ数値を読める。API 応答のキャッシュトークン欄から計算するのでどのプロバイダーでも動く。v2.1.251 以降。
2. [**契約レートでコストを表示する管理設定 `modelPricing` が入った**](./latest-detail.md#2-契約レートでコストを表示する管理設定-modelpricing-が入った):  
  組織が定価と違う単価で契約している場合、`/usage`・ステータスライン・Agent SDK の `total_cost_usd`・`--max-budget-usd`・OpenTelemetry のコスト値が請求と合わない。管理設定に `multiplier`（定価からの一律割引）と `overrides`（モデルごとの単価）を書くと、Claude Code の表示がその単価に変わる。請求額そのものは変わらない。v2.1.242 以降。
3. [**権限チェック後にパスの解決が変わったらファイル操作を拒否するようになった**](./latest-detail.md#3-権限チェック後にパスの解決が変わったらファイル操作を拒否するようになった):  
  権限ルールを検査した後、ツールが実際にファイルを開く・検索を始める時点でパスの解決をもう一度確認し、承認した場所を指していなければ拒否する。v2.1.251 より前は書き込みしか再確認しておらず、途中で差し替えられたリンクが読み取りや検索を別の場所へ向けても何も出なかった。プラグインのコンポーネントパスがプラグインディレクトリの外へ出るケースも塞がれた。
4. [**拡張思考を切ったまま高い effort を使ったときのエラーを Claude Code が吸収するようになった**](./latest-detail.md#4-拡張思考を切ったまま高い-effort-を使ったときのエラーを-claude-code-が吸収するようになった):  
  Opus 5 は拡張思考を切った状態で `xhigh` や `max` の effort を受け付けず、API が 400 を返していた。v2.1.251 以降、Claude Code はこの組み合わせを拒否すると分かっているモデルには effort `high` に落として送る。それでも届くエラーのために専用の節が新設された。
5. [**ストリーミング応答の「最初の 1 バイト」に専用の期限ができた**](./latest-detail.md#5-ストリーミング応答の最初の-1-バイトに専用の期限ができた):  
  応答ヘッダーが返ってこないまま期限を過ぎるとリクエストを打ち切り、1 度だけ再送する。4 本目のタイマーとして `network-config` の表に加わり、`CLAUDE_STREAM_FIRST_BYTE_TIMEOUT_MS` で直接指定できる。v2.1.242 より前は `API_TIMEOUT_MS`（既定 10 分）まで待っていた。

## 新規追加されたページ

（今回の対象期間に新規追加・削除されたドキュメントページはありません。`llms-full.txt` に展開されているページ数は前後とも 191 で、`llms.txt` の収録 URL も前後とも 202 件で同一です。ただし `llms.txt` の見出し構成は前回から一部巻き戻りました。詳細は軽微な更新の冒頭を参照してください）

## 大幅に更新されたページ

- [**エラーリファレンス**](./latest-detail.md#1-エラーリファレンス) ([English](https://code.claude.com/docs/en/errors#find-your-error)):  
  差分 642 行（実質 258 行）で今回最大。新設セクションが 11 本、削除が 1 本で、冒頭の検索表も全面的に書き直された。
- [**Agent SDK（Python）**](./latest-detail.md#2-agent-sdkpython) ([English](https://code.claude.com/docs/en/agent-sdk/python#error-types)):  
  差分 278 行（実質 252 行）。末尾の長いコード例群が整理され、`ToolAnnotations` の説明が実体を持つ節に書き改められた。今回唯一の純減ページ。
- [**設定リファレンス**](./latest-detail.md#3-設定リファレンス) ([English](https://code.claude.com/docs/en/settings-reference#all-settings)):  
  差分 78 行。新キー `modelPricing`（ハイライト 2）が中心で、`crossSessionInbound` の不正値の扱いや `forceRemoteSettingsRefresh` の待ち時間も改訂された。
- [**Agent SDK 移行ガイド**](./latest-detail.md#4-agent-sdk-移行ガイド) ([English](https://code.claude.com/docs/en/agent-sdk/migration-guide#migration-steps)):  
  差分 74 行。3 か所のコード例が散文と参照リンクに置き換わり、内容の追加はない純粋な圧縮。
- [**Agent SDK トラブルシューティング**](./latest-detail.md#5-agent-sdk-トラブルシューティング) ([English](https://code.claude.com/docs/en/agent-sdk/troubleshooting#cli-process-exit)):  
  差分 73 行（すべて追加）。CLI が起動できない場合・途中で終了した場合のエラーを、メッセージ単位で引ける 6 節が新設された。
- [**ステータスライン**](./latest-detail.md#6-ステータスライン) ([English](https://code.claude.com/docs/en/statusline#prompt-cache-fields)):  
  差分 60 行。`prompt_cache` オブジェクト（ハイライト 1）と `rate_limits.spend_limit` の追加、再実行トリガーの追加。
- [**Agent SDK（TypeScript）**](./latest-detail.md#7-agent-sdktypescript) ([English](https://code.claude.com/docs/en/agent-sdk/typescript#sdkresultmessage)):  
  差分 199 行（実質 57 行）。`ModelUsage` の `costBasis`、`createSdkMcpServer()` の `timeout`、`ScheduleWakeup` の `noop` が加わった。

## 軽微な更新

今回は 1 日分の取り込みで、`llms-full.txt` に差分のあったページは 83、差分行は 3 ファイル合計 2849 行（`llms-full.txt` 2687 行 / `llms.txt` 104 行 / ページ見出しマップ 58 行）です。ページの新規追加・削除はなく、展開されているページ数は前後とも 191 です。ただし**差分行の多くは表の桁揃えを整えただけの再フォーマット**で、桁揃えの差を無視して数え直すと実質の変更は大きく減ります。本サマリで「実質 N 行」と書いた値は、各行の連続空白と連続ハイフンを潰したうえで数え直した概算です。例えば `tools-reference` は差分 94 行に対して実質 1 桁行（変わったのは `SendMessage` の説明文だけ）、`interactive-mode` は 81 行のうち実質 21 行、`hooks` は 52 行のうち実質 22 行です。**大幅更新に入れる基準は前回同様「実質の差分 50 行以上 かつ 内容の変更を伴うこと」**とし、今回は上記 7 ページが該当しました。実質 47 行の**コスト管理**のページは基準にわずかに届きませんが、新設 2 節がそれぞれハイライト 1・2 の中心なので、そちらで扱っています。changelog は差分 74 行ですが、リンク不使用ポリシーのため大幅更新には入れず本節で扱います。

`llms.txt` の収録 URL は前後とも 202 件で同一ですが、**前回報告した見出しの組み替えが一部巻き戻りました**。前回は `## English` と `## Indexes` の 2 本を頂点に `### 大分類` → `#### 中分類` → `##### 小分類` という階層になっていましたが、今回は **`## English` が無くなり、その配下が丸ごと 1 段上がって `## 大分類` → `### 中分類` → `#### 小分類`** になっています。`## Indexes` は末尾に残っており、フラットだった 2 回前の構成に完全に戻ったわけではありません。エントリ自体（URL と 1 行説明）に変更はありません。

changelog に加わったのは **v2.1.251（2026年08月28日）の 71 項目**だけで、差分は 74 行です。内訳は Added 5・Fixed 40・Improved 10・Changed 13・Removed 1 に、`[VSCode]` 印の 2 件（Fixed 1・Changed 1）を加えたものです。今回は単一リリースのみなので、以下の changelog 由来の項目に版の併記はしません。**changelog ページへのリンクは張りません**。

ページ見出しマップ（`claude_code_docs_map.md`）は、上記の新設セクション（エラーの 11 節、`modelPricing` の 3 節、プロンプトキャッシュ統計、契約レートでの支出報告、ステータスラインのプロンプトキャッシュフィールド、Agent SDK トラブルシューティングの 6 節、ホスティングの配備障害、セルフホスト環境の CPU / メモリ見積もり、クラウドセッションの権限モード、保存済みワークフロースクリプトの編集）を取り込みました。あわせて **Leverage MCP for integrations** が **Use MCP for integrations** に改称され、Agent SDK の `troubleshooting` が `## Build agents` の下から `## Agent SDK` 側へ移動し、削除された見出し（`agent-sdk/python` の例示 6 節、`streaming-vs-single-mode` の `How It Works`、エラーの `The remote sent a reply this version can't display`）が落ちています。生成時刻の表記は 2026年08月28日 03:56 UTC から 2026年08月29日 04:34 UTC に進みました。

なお本サマリの参考リンクは全て英語版のみです。今回の変更に日本語版が追従していないためで、実際に取得して確認したところ、**日本語版の設定リファレンス（`/docs/ja/settings-reference`）は 404 を返し**、**日本語版のコスト管理ページにはプロンプトキャッシュ統計・契約レートでの支出報告のどちらの節も無く**（`/usage` の説明も「トークン数から局所的に計算された推定値」という旧記述のまま）、**日本語版のステータスラインページには `prompt_cache` も `rate_limits.spend_limit` も無く**、**日本語版のエラーリファレンスには今回新設された 11 節がいずれも存在しません**。他のページは個別には確認していませんが、いずれも直近 1〜2 日の変更であるため未追従とみなし、安全側に倒して英語版のみを載せています。

**新機能**

- ステータスラインに `prompt_cache` オブジェクトが、`/usage` に `Prompt cache (main)` 行が加わりました（詳細はハイライト 1 参照。changelog 側の表記は `/cost`）— [English](https://code.claude.com/docs/en/costs#prompt-cache-statistics)
- 管理設定キー `modelPricing` が加わりました（詳細はハイライト 2 参照）— [English](https://code.claude.com/docs/en/settings-reference#modelpricing)
- `PreModelSwitch` と `PostModelSwitch` のフックイベントが加わり、モデルの切り替えをブロック・確認・注釈できるようになりました。あわせて `SessionStart` の resume フックが、セッションがどれだけ古いかと再キャッシュ費用の見積もりを受け取るようになりました（対応する通常ページの記述がまだ無いためリンクを省略します）
- Claude apps gateway の支出上限が設定されている開発者に、`/usage` の **Spend limit** バーとステータスラインの `rate_limits.spend_limit` が出るようになりました。どちらも金額ではなくパーセンテージで表示します — [English](https://code.claude.com/docs/en/claude-apps-gateway-spend-limits#usage-warnings-in-claude-code)
- `claude --help` に `attach`・`logs`・`stop`・`respawn`・`rm` が載るようになり、実行中のバックグラウンドセッションに対する `--resume` のメッセージが `claude attach <id>` のコマンドをそのまま示すようになりました（対応する通常ページの記述が無いためリンクを省略します）
- Remote Control のクライアントに、フォアグラウンドのサブエージェントのツール呼び出しと結果がライブでストリーミングされるようになりました（既定であるバックグラウンドのサブエージェントは従来どおりステータスのみ）— [English](https://code.claude.com/docs/en/remote-control#start-a-remote-control-session)
- 保存済みワークフロースクリプトを手で編集するための `/workflow-authoring` バンドルスキルが加わりました（v2.1.248 以降。編集後は `/reload-skills` で読み直します）— [English](https://code.claude.com/docs/en/workflows#edit-a-saved-script)
- サブエージェントの frontmatter に `experimental` マップが加わり、その `cacheTtl` キーで当該サブエージェントのリクエストのプロンプトキャッシュ TTL を `5m` / `1h` から選べるようになりました（v2.1.248 以降。使用クレジットを使っている購読では `1h` は無視されます）— [English](https://code.claude.com/docs/en/sub-agents#supported-frontmatter-fields)
- Manual と `acceptEdits` モードで、Bash コマンドの権限プロンプトに **Yes, and switch to auto mode** が加わりました（v2.1.247 以降。`ask` ルールやフックが強制したプロンプトには出ません）— [English](https://code.claude.com/docs/en/permission-modes#eliminate-permission-prompts-with-auto-mode)
- クラウドセッションの権限モードをモード切り替えのドロップダウンから選べることが明記され、環境の期限切れやランナーの解放から再開したときは元のモードに戻ることも書かれました — [English](https://code.claude.com/docs/en/claude-code-on-the-web#permission-modes-in-cloud-sessions)
- `claude doctor` に `Managed settings (remote)` の行が加わり、サーバー管理設定の取得結果（読み込み成功 / 未設定 / 失敗 / スキップ）を 4 通りで報告するようになりました（v2.1.248 以降）— [English](https://code.claude.com/docs/en/server-managed-settings#verify-settings-delivery)
- セルフホストランナーに `--client-label` フラグが加わり、登録時に送るラベルと Prometheus メトリクスのラベルを指定できるようになりました（v2.1.248 以降）— [English](https://code.claude.com/docs/en/self-hosted-environments-reference#runner-cli-flags)
- セルフホスト環境の配備ページに **Size CPU and memory for sessions** 節が新設され、1 セッションあたりメモリ 4 GiB（request と limit を同値）・CPU は request 2 / limit 4 という出発点と、`--capacity` に応じた掛け算の考え方が示されました — [English](https://code.claude.com/docs/en/self-hosted-environments-deploy#size-cpu-and-memory-for-sessions)
- vim モードに `df{char}` / `dt{char}`（指定文字まで削除）が加わり、`Ctrl+[` でも NORMAL モードに入れることが明記されました（Kitty キーボードプロトコルを使う端末では v2.1.242 以降）— [English](https://code.claude.com/docs/en/interactive-mode#editing-normal-mode)
- ターミナル設定のカラートークンに `effortUltra`（ultracode 有効時に入力ボックスの枠に出る `ultracode` タグ）が加わりました — [English](https://code.claude.com/docs/en/terminal-config#create-a-custom-theme)
- `claude mcp list` のステータスに `⊘ Disabled for this project (re-enable via /mcp)` が加わりました — [English](https://code.claude.com/docs/en/mcp-quickstart#add-and-verify-a-server)
- `/claude-api` に `cost-optimize` サブコマンドが加わりました — [English](https://code.claude.com/docs/en/commands#all-commands)

**機能改善**

- **クロスセッションメッセージングが第三者プロバイダーでも使えるようになりました**。Amazon Bedrock・Claude Platform on AWS・Google Cloud の Agent Platform・Microsoft Foundry、および機能フラグの取得を切ったセッションでも、**同一マシン内のセッション間**なら利用できます（v2.1.248 以降）。マシンを越える相手を見つけるには従来どおり Remote Control 接続が必要です — [English](https://code.claude.com/docs/en/cross-session-messaging#availability)
- Remote Control に接続している間、`/list-agents` の出力からローカルセッションの**作業ディレクトリ**と、人に帰属できない**セッション名**（`(unnamed session)` と表示）と、**自分自身の名前の行**が伏せられるようになりました。Claude 自身が送信先を探すときに見える情報は変わりません — [English](https://code.claude.com/docs/en/cross-session-messaging#see-which-sessions-claude-can-reach)
- `@` メンションで、空白などを含む名前を `@"release notes"` のように二重引用符で囲めるようになりました（タイプアヘッドから選ぶと引用符は自動で入ります）— [English](https://code.claude.com/docs/en/cross-session-messaging#message-another-session)
- 他セッションから届いたメッセージ内の `@` は、新しいターンを始める場合でも**ファイルや MCP リソースを添付しなくなりました**（v2.1.251 以降）。サブエージェントが書いたメッセージは送信元セッション名で届き、返信はそのセッションのメイン会話に入ります — [English](https://code.claude.com/docs/en/cross-session-messaging#message-delivery)
- エージェントチームのチームメイトのモデル決定順が 4 段階で明記され、`CLAUDE_CODE_SUBAGENT_MODEL` が `inherit` 以外に設定されている場合が最優先になりました。サブエージェント定義のどの部分が表示モード別にどう効くかも `tools` / `model` / 本文 / `skills` / `mcpServers` の 5 項目に整理されています — [English](https://code.claude.com/docs/en/agent-teams#specify-teammates-and-models)
- チームメイトのアイドル通知に**最終回答が含まれる**ようになりました。従来は「停止した」ことしか伝わらず、結果はメッセージや共有タスクリスト経由で受け取る必要がありました — [English](https://code.claude.com/docs/en/agent-teams#use-subagent-definitions-for-teammates)
- フォールバックモデルチェーンが**サブエージェントにも適用される**ようになりました（v2.1.247 以降）。それより前は、チェーンが対象とする失敗でサブエージェントが終了していました — [English](https://code.claude.com/docs/en/model-config#fallback-model-chains)
- `/model`・`/effort`・`/fast` は**キューに入らず即座に実行される**ことと、実行中のターンへの反映のされ方がコマンドごとに違うことが明記されました。`/model` と `/effort` はキャッシュ警告を確認した後そのターンの次のリクエストから効き、`/fast` は速度の変更が次のターンからになります（v2.1.242 より前は機能フラグ次第でキューに入っていました）— [English](https://code.claude.com/docs/en/interactive-mode#when-claude-code-sends-what-you-queued)
- キューの送出規則が改まりました。**ターンがキューを残したまま終わった場合、Claude Code が次のターンとして送るのは最も古い 1 通だけ**で、残りはキューに留まって同じ規則に従います。従来は「まだキューにある分をそれぞれ別メッセージとして送る」と書かれていました — [English](https://code.claude.com/docs/en/interactive-mode#when-claude-code-sends-what-you-queued)
- **会話の途中で足されるシステムコンテキストが、全てのプロバイダー・全ての接続でキャッシュ対象としてマークされる**ようになりました。ゲートウェイ経由で何が起きるかは、`cache_control` マーカーをそのまま転送する / `400` で拒否する（Claude Code がマーカーを最後の会話メッセージに移して再送する）/ 成功を返しつつマーカーを落とす（会話全体が毎ターン未キャッシュ入力として課金される）の 3 通りに整理されました — [English](https://code.claude.com/docs/en/prompt-caching#where-the-cache-lives)
- LLM ゲートウェイのプロトコルリファレンスに **Prompt caching** の行が加わり、`cache_control` を落とすゲートウェイでは「エラーは出ないが `usage` のキャッシュ活動がほぼゼロのまま `input_tokens` が高い」という症状で気づけることが示されました。モデル探索リクエストが `Authorization` と `x-api-key` の**両方のヘッダーを送る**ようになったこと（v2.1.248 以降）も加わっています — [English](https://code.claude.com/docs/en/llm-gateway-protocol#model-discovery)
- フックのハンドラは、**現在のディレクトリが消えている場合**（別のシェルが消した worktree や一時ディレクトリなど）に、セッション開始ディレクトリ → プロジェクトルート → ホームディレクトリ → システム一時ディレクトリの順で存在するものから実行され、フォールバック先がデバッグログに記録されるようになりました — [English](https://code.claude.com/docs/en/hooks#hook-handler-fields)
- フックの stdout を JSON と見なす条件が「`{` で始まる」から「**`{` で始まり `}` で終わる**」に厳格化され、JSON として読もうとして失敗した場合は終了コード 2 以外で非ブロッキングエラーを報告するようになりました（v2.1.248 より前はプレーンテキストとして扱っていました）— [English](https://code.claude.com/docs/en/hooks#exit-code-output)
- フックの `if` パターンの Bash マッチ表に 2 行が加わり、`$()` がどの引数位置にも来うるため全体と置換の両方を照合すること、コマンド名が変数（`$TOOL git push`）の場合はフックを実行することが示されました。`PreToolUse` のマッチ対象も「**`EndConversation` 以外の全ツール**」という書き方に改まり、`Workflow` が例示に加わりました — [English](https://code.claude.com/docs/en/hooks#pretooluse)
- サンドボックスの既定の書き込み先に `--add-dir` / `/add-dir` で追加したディレクトリが含まれることが全体を通して明記され、サンドボックス外で走るコマンドの権限プロンプトのタイトルが **Bash command (unsandboxed)** になったことも加わりました — [English](https://code.claude.com/docs/en/sandboxing#configure-sandboxing)
- MCP のツール呼び出しのリクエスト単位タイマーの決まり方が「60 秒・そのサーバーに適用されるツールタイムアウト・`MCP_TIMEOUT` の**最大値**」と明確化されました。`headersHelper` が `Authorization` を供給しているサーバーは、認証エラーでも再試行されます（ヘルパーが毎回走るため新しい資格情報を拾えるため）— [English](https://code.claude.com/docs/en/mcp#use-dynamic-headers-for-custom-authentication)
- MCP プロンプトの一覧表記が `/servername:promptname (MCP)` になりました（従来の `/mcp__servername__promptname` でも実行できます）。引数は空白で分割されて 1 トークンずつ渡ります — [English](https://code.claude.com/docs/en/mcp#use-mcp-prompts-as-commands)
- サーバー管理設定の起動時の挙動が具体化され、**サインインを伴う起動では最大 5 秒だけ取得を待つ**こと、その間に届けば最初の画面からポリシーと `companyAnnouncements` が効くこと、失敗時は対話セッションで警告することが加わりました。`API_FORCE_IDLE_TIMEOUT` は真値なら承認なしで適用されるようになっています（v2.1.248 以降）— [English](https://code.claude.com/docs/en/server-managed-settings#fetch-and-caching-behavior)
- Artifacts が `cdnjs.cloudflare.com`・`cdn.jsdelivr.net`（`/npm/` など一部パス）・`cdn.tailwindcss.com`・`code.jquery.com` の 4 ホストから JavaScript ライブラリを読み込めることが明記されました。これらをブロックするとライブラリ依存の部分が動かず、フォントと違ってフォールバックがありません — [English](https://code.claude.com/docs/en/artifacts#allowlist-the-viewer-domain)
- ワークフローの `parallel()`（複数のエージェントタスクを同時に走らせて全て待つ）が本文に加わり、1 回の `parallel()` / `pipeline()` は最大 4,096 項目でそれを超えるとエラーになること、スクリプトはセッションが既に読める場所にある必要があることが加わりました — [English](https://code.claude.com/docs/en/workflows#edit-a-saved-script)
- スキルのバンドルスキルは「**ほとんどが**全セッションで使える」に改まり、`/workflow-authoring` のように特定機能に依存するものがあることが示されました。frontmatter は**開いている `---` がファイルの 1 行目にある場合のみ**読まれることも明記されています — [English](https://code.claude.com/docs/en/skills#bundled-skills)
- `/doctor` と `claude doctor` の役割分担が明記されました。設定ファイルの不正を見つけるのはターミナルの `claude doctor`、修正案の提示と適用の確認まで行うのはセッション内の `/doctor` です。`/context` のスキル欄には `/skills` に出ないバンドルスキルも含まれます — [English](https://code.claude.com/docs/en/debug-your-config#check-resolved-settings)
- 機能提供状況の表で、**クロスセッションメッセージングが 5 つの第三者プロバイダー列すべてで「✓（same machine）」**になり、脚注 5 に v2.1.248 以降という条件が加わりました。LLM ゲートウェイ経由の可否も、「`ANTHROPIC_BASE_URL` が `api.anthropic.com` 以外を指す限り Remote Control とサーバー管理設定は Claude Code 自身が切る」と具体化されています — [English](https://code.claude.com/docs/en/feature-availability#cli-capabilities-that-vary-by-provider)
- Agent SDK のコスト追跡ページに、`inference_geo: "us"` のレスポンスは定価を 1.1 倍する（データレジデンシー価格。TypeScript v0.3.239 / Python v0.2.144 以降）ことと、`modelUsage` の各エントリの `costBasis` が加わりました。コスト管理ページ側にも、Claude API の 1.1 倍レートを v2.1.239 以降はセッションコストに反映していることが加わっています — [English](https://code.claude.com/docs/en/agent-sdk/cost-tracking#break-down-usage-per-model)
- `/radio` が Amazon Bedrock・Vertex AI・Microsoft Foundry・Claude Platform on AWS、およびテレメトリ無効時にも使えるようになりました — [English](https://code.claude.com/docs/en/commands#all-commands)
- Claude in Chrome のブラウザ操作が、テレメトリ無効のセッションを含めて**常に Claude Code の権限チェックを通る**ようになりました（従来は Chrome 拡張自身のプロンプトを使っていました）
- `CLAUDE_CODE_SUBAGENT_MODEL` が「全てを上書きする」設定から「**既定のサブエージェントモデルを決める**」設定に変わり、エージェント定義の `model:` と生成時の明示指定が優先されるようになりました — [English](https://code.claude.com/docs/en/agent-teams#specify-teammates-and-models)
- `/effort` が**モデルごとに既定の effort レベルを保存**するようになり、モデルを切り替えても各モデルの設定が保たれるようになりました
- シート制 Enterprise サブスクリプションの既定モデルが Opus 5 になりました（対応する通常ページの記述が無いためリンクを省略します）
- サンドボックス内で走る Bash コマンドの出力ファイルの作り方・読み戻し方が変わり、**サンドボックス内のコマンドがそれをリダイレクト・置換できない**ようになりました
- サンドボックスの TLS 終端・自前プロキシ経由のルーティング・資格情報の注入・分離の弱体化を行うサーバー管理設定は、適用前に承認を求めるようになりました。管理設定・プロジェクト設定からの `ANTHROPIC_CUSTOM_HEADERS` も、資格情報・組織／テナント・ルーティング・API 挙動に関わるヘッダー（`Authorization`・`Host` など）を設定する場合は承認が必要です — [English](https://code.claude.com/docs/en/server-managed-settings#security-approval-dialogs)
- プロジェクトの `.claude/settings.json` の `env` から `CLAUDE_CONFIG_DIR`・`CLAUDE_CODE_TMPDIR`・`TMPDIR`/`TMP`/`TEMP` を設定できなくなりました。シェル・ユーザー設定・管理設定で設定します
- 管理設定の承認ダイアログが、**前回承認したときから変わった設定だけを列挙**するようになりました。同じ Claude apps gateway に再サインインしても、設定が変わっていなければ再表示されません
- プラグイン／LSP のインストール提案と auto mode 既定化の提案が、**入力中の内容を送信するか消すまで待つ**ようになりました。プロンプトを送る Enter がそれらに答えてしまわないためです
- モデルのツール呼び出しが壊れているときの再試行で、**壊れた出力を再試行のコンテキストから落とす**ようになりました（Amazon Bedrock・Vertex・Microsoft Foundry を含む）（対応する通常ページの記述が無いためリンクを省略します）
- Bedrock セッションの起動が改善され、`CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST` の下で Bedrock のモデル ID や ARN を渡されたセッションは推論プロファイルの探索を待たなくなりました
- 対話セッションのターン中の CPU 使用率が、冗長な UI 再描画を減らすことで改善されました。ネイティブバイナリのインストールサイズも約 5 MB 小さくなっています（対応する通常ページの記述が無いためリンクを省略します）
- クラウドセッションで Bash コマンド中にセッションのネットワークプロキシが接続を切った場合、ツール結果が「connection reset」だけでなく**ホスト名と理由**を示すようになりました
- `/schedule` が「Claude Code に設定した MCP サーバーはクラウドルーチンに接続できない」ことを説明するようになりました（従来は「No MCP connectors」とだけ出ていました）
- 自分のサブエージェントから届くメッセージの枠付けが改善され、送信者が**無関係な Claude セッションではなく本セッション内のワーカー**であることが Claude に伝わるようになりました。サブエージェントやフォークのトランスクリプトを開いている間、入力欄のプレースホルダが `Message @name…` になります
- エラーメッセージ・メニュー・コマンド結果に出る MCP サーバー名のサニタイズが改善されました。`/mcp__servername__promptname` 形式では、サーバー名の `A-Z`・`a-z`・`0-9`・`_`・`-` 以外の文字が `_` に置き換わります — [English](https://code.claude.com/docs/en/mcp#use-mcp-prompts-as-commands)
- セルフホストランナーが、**work poll の応答が想定の JSON でない場合**（間に入ったプロキシが自分のページを返した場合など）に、それを拒否して `transport` 種別のメトリクスに数え、稼働中のセッションを維持したまま再試行するようになりました（v2.1.246 より前は空のキューと読んでいました）— [English](https://code.claude.com/docs/en/self-hosted-environments-deploy#troubleshooting)
- セルフホストランナーの `SIGTERM` 時と `--kill-session-after-min` 到達時の終了対象が、セッションのプロセス単体から**プロセスツリー全体**（Claude が走らせたままのコマンドを含む）に改まりました — [English](https://code.claude.com/docs/en/self-hosted-environments-reference#runner-cli-flags)
- Claude apps gateway 配下では、Claude Code が Anthropic 宛のクライアントアナリティクスもエラーレポートも送らないことが明記され、サインイン前（`forceLoginMethod: "gateway"` の初回起動を含む）は起動イベントと機能フラグのリクエストだけが Anthropic に届くことが加わりました。TLS 証明書のフィンガープリントを `/login` の表示形式で出す `openssl` のワンライナーも追加されています — [English](https://code.claude.com/docs/en/claude-apps-gateway-deploy#data-flow)

**バグ修正**

- 権限チェック後に差し替えられた symlink をファイルツール（Read / Write / Edit）が追ってしまい、承認外の場所を読み書きしうる問題を修正（詳細はハイライト 3 参照）— [English](https://code.claude.com/docs/en/errors#refusing-to-read-write-or-search-a-path)
- Grep と Glob が、symlink を経由した検索パスの先のファイルに `Read(...)` の deny ルールを適用していなかった問題を修正（詳細はハイライト 3 参照）— [English](https://code.claude.com/docs/en/permissions#read-and-edit)
- マーケットプレイスのエントリで宣言したプラグインコマンドが、プラグインディレクトリの外を指せた問題を修正（詳細はハイライト 3 参照）— [English](https://code.claude.com/docs/en/errors#path-escapes-plugin-directory)
- Workflow ツールが、権限チェックの前にセッションが読んでよい範囲外の `scriptPath` を読み（エラーメッセージに引用し）ていた問題を修正 — [English](https://code.claude.com/docs/en/workflows#how-a-workflow-runs)
- プロジェクト設定が詳細なベータトレースや生の API ボディのログを有効にできた問題と、下位スコープのベータトレースのエンドポイントが管理設定・ホストアプリの固定した OTLP コレクタを迂回できた問題を修正
- Opus 5 で effort が `xhigh` / `max` かつ拡張思考がオフのときにリクエストが失敗する問題を修正（詳細はハイライト 4 参照）— [English](https://code.claude.com/docs/en/errors#effort-isnt-available-with-thinking-turned-off)
- GitHub 接続が一時的に失敗しただけの場合にも、クラウドセッションの作成が「GitHub をセットアップせよ」と案内していた問題を修正 — [English](https://code.claude.com/docs/en/errors#the-github-app-preflight-failed-transiently)
- モデルが思考だけを出力したターンの後、会話が `text content blocks must be non-empty` で止まる問題を修正
- 新規インストールの初回起動が、起動時の既定が auto mode のアカウントでも default モードで始まる問題を修正
- Claude Desktop が別セッションから配送したメッセージに返信するとき、そのセッション ID への `SendMessage` が `not reachable` で失敗する問題を修正 — [English](https://code.claude.com/docs/en/desktop#work-across-sessions)
- サブエージェントを多数並列実行したときの TUI の遅延を修正。毎秒の進捗ティックがトランスクリプトに積み上がらず、直前のものを置き換えるようになりました
- エージェントチームで、チームメイトの最終回答がリードに届かない問題を修正（内容の無い「available」通知ではなくアイドル通知に載るようになりました）— [English](https://code.claude.com/docs/en/agent-teams#use-subagent-definitions-for-teammates)
- バックグラウンドのサブエージェントが、名前の無い兄弟エージェントや親エージェントからのメッセージに返信できない問題を修正（`from` がアドレスではなくエージェント種別になっていました）
- 管理設定の `disableAutoMode` がセッション途中に届いても、既に auto mode で走っているセッションが default モードに戻らない問題を修正 — [English](https://code.claude.com/docs/en/permission-modes#eliminate-permission-prompts-with-auto-mode)
- 現在の Opus が既に 1M コンテキストを持っている場合にも「Opus 1M に切り替えれば 5 倍のコンテキスト」というヒントが出る問題を修正
- Claude apps gateway のセッションが、保存済みの Anthropic プロファイル（Console のサインインなど）をアクティブ扱いして `/status` に載せ、ゲートウェイの 401 でそれを使って再試行する問題を修正（実際のリクエストでは使われていません）— [English](https://code.claude.com/docs/en/claude-apps-gateway#whats-enforced-on-developers)
- クラウドセッションで、ホストがセッションの初期モデルを設定しただけなのに「モデルが変わった」と Claude に伝える問題を修正
- 組織のポリシーで Remote Control が無効になっている場合に、失敗として報告していた問題を修正（静かな通知 1 つになりました）— [English](https://code.claude.com/docs/en/remote-control#start-a-remote-control-session)
- Remote Control 上の `/mcp reconnect` で、サーバーが別のセッションで無効化されている場合に、実際の対処法ではなく詳細を伏せた汎用エラーが出る問題を修正
- `--input-format stream-json` で、メッセージ ID なしに送られたクライアント注入のアシスタントツール呼び出しが最初の 1 つにマージされ、結果が失われる問題を修正（古いセッションを再開した場合を含む）
- ディレクトリの変更によってセッションが同一 ID の既存トランスクリプト上に移されたとき、トランスクリプトが黙って上書きされる問題を修正
- バックグラウンドセッションとそのサブエージェントが、自分で `git worktree add` して作った worktree 内のファイルを編集できない問題を修正 — [English](https://code.claude.com/docs/en/agent-view#how-file-edits-are-isolated)
- 別の Claude Code プロセスがプラグインマーケットプレイスを更新している最中に起動したバックグラウンドセッションが、そのマーケットプレイスのプラグインスキルを 1 つも持たないまま動き続ける問題を修正 — [English](https://code.claude.com/docs/en/agent-view#version-history)
- SSH 越しの tmux でバックグラウンドセッションのテキスト選択が OSC 52 にフォールバックする問題を修正（フォアグラウンドと同じく tmux バッファにコピーされます）
- SDK MCP サーバーのハンドシェイクの受領確認が失われたとき、SDK・クラウドセッションが無期限に待つ問題を修正（70 秒でタイムアウトし、そのサーバーだけを失敗扱いにします）
- セルフホストランナーが、強制停止したセッションの Bash ツールのプロセスを残したままにする問題を修正 — [English](https://code.claude.com/docs/en/self-hosted-environments-reference#runner-cli-flags)
- 組織の使用クレジット上限が \$0 に設定された Team / Enterprise メンバーに対して、`/usage-credits` が「上限に達した」と表示する問題を修正（管理者への依頼を案内するようになりました）
- gitlab.com が origin のリポジトリで `--worktree --tmux` にマージリクエスト番号を渡すと、GitLab の ref を直接取らずに GitHub 形式の fetch を先に試す問題を修正
- `/dev/tty` を開くエディタ（`emacs -nw`・`micro` など）で、バックグラウンドセッションの Ctrl+G が `Emacs quit unexpectedly` で失敗する問題を修正
- `additionalDirectories` の項目にヌルバイトが含まれると起動がクラッシュする問題、および SDK ホスト・IDE・フック由来の場合に `/add-dir` や以降の設定更新が壊れる問題を修正（該当項目をスキップするようになりました）
- MCP サーバーメニューのコピーショートカットが、常に成功したと表示する問題を修正（サインイン URL をどうコピーしたかを示すようになりました）
- GNU screen と `screen` 端末型を使う tmux セッションで、斜体（セッションのおさらい行など）がハイライトブロックとして描画される問題を修正
- `claude mcp add --header` と `claude mcp add-json` のヘルプが、誤ったトランスポートを挙げる問題を修正
- クラウドセッションが起動しないときに `claude ultrareview` と `/ultrareview` が 30 分待ち切る問題を修正（早く止めて理由を報告します）
- 整数のシェル変数に算術式を代入するコマンド（`OPTIND=1/0`・`RANDOM=2+2` など）が Bash の権限チェックで自動承認される問題を修正
- シェルで export した Vertex / Bedrock のゲートウェイ（`ANTHROPIC_*_BASE_URL` と `CLAUDE_CODE_SKIP_*_AUTH`）を、バックグラウンド化したセッション（`←`・`/background`・`--bg`）が失って全リクエストが失敗する問題を修正 — [English](https://code.claude.com/docs/en/agent-view#the-supervisor-process)
- Max プランで `claude --bg --model fable` が、同じアカウントの対話セッションにまだ Fable の割り当てが残っているのに使用クレジットを求めて止まる問題を修正
- 無人セッション（エージェントチームのチームメイトのペインなど）で「auto mode を既定にしませんか」という一回限りの提案が出て、誤打鍵で受け入れられうる問題を修正
- 無効化された `/bug` と `/share` が「`/feedback` が無効です」と報告する問題を修正（組織のポリシーや環境変数で `/feedback` が切られている場合、ヒント・`/help`・拒否メッセージがそれを勧めなくなりました）
- コンテナ内で bubblewrap が新しい `/proc` をマウントできないときに出る `bwrap` のエラー例が明示され、`enableWeakerNestedSandbox` への案内が引きやすくなりました — [English](https://code.claude.com/docs/en/sandboxing#troubleshooting)

**その他**

- 使用頻度の低い 6 言語（1c、gml、isbl、mathematica、maxima、sqf）のシンタックスハイライトが削除され、バイナリが 2.5 MB 小さくなりました
- \[VSCode] サインイン画面の「Bedrock, Foundry, or Vertex」ボタンが、第三者プロバイダーのセットアップ節ではなくドキュメントの先頭を開く問題を修正
- \[VSCode] Remote Control のバナーが、フッターのピル（Remote Control が有効か失敗している間に表示され、クリックで claude.ai/code のセッションを開く）に変わりました。オン・オフは `/remote-control` で切り替えます — [English](https://code.claude.com/docs/en/remote-control#start-a-remote-control-session)
- 管理者セットアップのページで、セクション名が **Leverage MCP for integrations** から **Use MCP for integrations** に改称されました — [English](https://code.claude.com/docs/en/admin-setup)
- Agent SDK の「Streaming Input」ページから **How It Works** のシーケンス図が削除されました — [English](https://code.claude.com/docs/en/agent-sdk/streaming-vs-single-mode)
- 構造化出力ページと承認・ユーザー入力ページの JSON コードブロックが、コメント付きを許す `jsonc` に変更されました — [English](https://code.claude.com/docs/en/agent-sdk/structured-outputs)
- インストール手順のページ（`setup`）で、5 つのコードブロックの言語指定に `theme={null}` が 9 個ずつ重複して出力される不具合が入りました（表示上の実害はありませんが、原文の生成側の問題です）— [English](https://code.claude.com/docs/en/setup#install-claude-code)
- 開発コンテナのページで、`init-firewall.sh` の説明が「許可ドメイン以外の全ての外向き通信をブロックする」から「**スクリプトが許可した宛先に外向き通信を限定する**」に改められました — [English](https://code.claude.com/docs/en/devcontainer)
- コスト管理ページの `PreToolUse` フックの例が、文字列連結ではなく `jq` で JSON を組み立てる形に書き直され、検証手順も `--debug` から `--debug-file ./claude-debug.txt` に改められました — [English](https://code.claude.com/docs/en/costs#track-your-costs)
- `/simplify` と `/code-review` の説明、プラグインの `defaultEnabled`、プラグイン推奨の表示面、`skipLfs`、Chrome のブラウザ選択、Claude Security の前提条件などから、既に十分に古くなった版番号の注記が一斉に外れました — [English](https://code.claude.com/docs/en/commands#all-commands)
- プラグイン名とマーケットプレイス名に、**制御文字と双方向テキスト整形文字を含められない**ことが明記され、専用のエラーメッセージが追加されました（v2.1.247 より前は別のエラーになるか、プラグイン名では検査されていませんでした）— [English](https://code.claude.com/docs/en/plugin-marketplaces#plugin-entries)
- `/btw` の説明から「サブエージェントの逆」という言い回しが外れ、フォークしたサブエージェントは会話のコピーから始まることを含む書き方に改められました — [English](https://code.claude.com/docs/en/interactive-mode#side-questions-with-btw)

## 新着情報

（今回の対象期間に新着情報ページの追加・更新はありません。Week 34（2026年08月17日～21日）が最新のままです）

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-08-27.md](./archives/latest/2026-08-27.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-08-27.md](./archives/latest-detail/2026-08-27.md)

<!--
base_commit: f3e684155b58c715cf4ea6f2ef92628176bf96e0
head_commit: f5de441e788b355b2a85c43da6cf29f85d714c19
generated_at_full: 2026-08-29T15:15:52+09:00
-->
