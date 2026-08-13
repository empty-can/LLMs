---
対象期間: 2026年08月11日 〜 2026年08月12日
作成日: 2026-08-12
---

# Claude Code 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
今回の対象期間は 62 ページに差分がありました。新規ページと新着情報はありません。目立つのは Agent SDK 側の再整備で、トークンとコストの数え方、サブエージェントの上限、外部ストレージからの再開が相次いで書き直されています。CLI 側では、テレメトリ系の環境変数を設定すると何が使えなくなるかの一覧と、claude.ai から同期したスキルの扱いが新しく文書化されました。

主要なものを以下に挙げます。

1. フィーチャーフラグの取得を切ると使えなくなる機能の一覧が環境変数のページに新設され、十数ページからそこを参照するようになった
2. Agent SDK のトークンとコストの数え方が全面的に書き直され、アシスタントメッセージの出力トークンはプレースホルダーだと明記された
3. サブエージェントの深さ・同時実行数・支出に上限を設ける方法が新しい節としてまとまり、Opus 5 は委譲しやすいという注意が加わった
4. claude.ai から同期したスキルの読み込み場所・名前衝突・本文の扱いが 4 節にわたって文書化された
5. forceLoginOrgUUID が検証するのは claude.ai アカウントのログインだけで、Claude Console のログインは検証しないと明記された
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**フィーチャーフラグ取得を切ると使えなくなる機能が一覧化された**](#1-フィーチャーフラグ取得を切ると使えなくなる機能が一覧化された):  
  環境変数のページに新しい h2 が加わり、`DISABLE_TELEMETRY` などでフラグ取得を止めたセッションで使えない機能が列挙された。Remote Control・セッション間メッセージング・`claude import`・`/schedule`・advisor・`/loop` の自己ペーシングが対象で、インストール直後の初回セッションにも同じ影響が出る。
2. [**Agent SDK のトークンとコストの数え方が全面的に書き直された**](#2-agent-sdk-のトークンとコストの数え方が全面的に書き直された):  
  アシスタントメッセージの `output_tokens` は応答開始時点の値を写しただけのプレースホルダーであり、出力トークンは結果メッセージから読むべきだと明記された。ストリーミング入力モードでの集計方法と、セッションクラッシュ後の合計の復旧手順も新設された。
3. [**サブエージェントの増殖を抑える 3 つの上限が文書化された**](#3-サブエージェントの増殖を抑える-3-つの上限が文書化された):  
  ネストの深さ・同時実行数・クエリ全体の支出に上限を設ける方法が SDK のサブエージェントのページにまとまった。あわせて Claude Opus 5 は従来のモデルより委譲しやすいため、これらの上限が特に効いてくることが書かれている。
4. [**claude.ai から同期したスキルの扱いが文書化された**](#4-claudeai-から同期したスキルの扱いが文書化された):  
  `CLAUDE_CODE_SYNC_SKILLS` で落としたスキルがどこに読み込まれるか、名前が他のコマンドと衝突したらどうなるか、フロントマターと本文がどう扱われるかが 4 つの節に分かれて説明された。手元のセッションでは `!` コマンドも `@` 参照も実行・展開されない。
5. [**forceLoginOrgUUID が検証するのは claude.ai ログインだけだと明記された**](#5-forceloginorguuid-が検証するのは-claudeai-ログインだけだと明記された):  
  「指定した組織以外の資格情報なら起動時に終了する」という説明が書き直され、検証対象は claude.ai アカウントのログインに限られること、Claude Console のログインは組織を照合せず事前選択にしか使われないことが示された。
<!-- light:highlight-list:end -->

## 1. フィーチャーフラグ取得を切ると使えなくなる機能が一覧化された

環境変数のページに **フィーチャーフラグの取得が必要な機能** という h2 が新設されました。Claude Code は一部の機能を Anthropic から取得するフィーチャーフラグで有効化しており、`DISABLE_GROWTHBOOK` / `DISABLE_TELEMETRY` / `DO_NOT_TRACK` / `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` のいずれかを無効化側の値で設定するとその取得が止まります。取得が止まったセッションで使えなくなるのは、Remote Control、セッション間メッセージング、`claude import` と `/import`、ルーチンを作る `/schedule`、advisor ツール、`/loop` の自己ペーシング（間隔を省いた `/loop` は固定 10 分間隔になる）、`/loop` の組み込みメンテナンスプロンプト（プロンプトを省くと使い方メッセージが出るだけになる）です。加えて、自分で `/code-review` と打つことはできるものの Claude 自身がレビューを開始できず、スケジュールした `/code-review` はレビューを実行せずただのテキストとして届く、と説明されています。

配下の **インストールやアップグレード直後の初回セッション** では、変数を何も設定していなくても一覧の機能が欠けうることが書かれました。その初回セッション中にフラグを取得するため、次のセッションからは使えるようになります。ただし 2 つは挙動が異なり、セッション間メッセージングは取得が完了した時点で受信箱ソケットを bind して変数を export するため再起動を待たずに他セッションから届くようになり、`claude import` はセッション開始前にフラグを見るためインストール直後に実行すると新設のエラーになります。この一覧への参照は advisor・CLI リファレンス・コマンド・スケジュール実行・ツールリファレンス・dev container・セッション間メッセージング・Agent SDK TypeScript リファレンスなど十数ページに張られ、それまで「Remote Control とセッション間メッセージングが使えなくなる」とだけ書かれていた各所がこの節への参照に統一されました。

- [Environment variables - Claude Code Docs (English)](https://code.claude.com/docs/en/env-vars#features-that-need-feature-flag-fetching)
- [Error reference - Claude Code Docs (English)](https://code.claude.com/docs/en/errors#claude-import-is-not-yet-available-in-this-build)

## 2. Agent SDK のトークンとコストの数え方が全面的に書き直された

コスト追跡のページで最も大きい訂正は出力トークンの扱いです。Claude Code は API が応答開始時（`message_start`）に報告した使用量からアシスタントメッセージを組み立てるため、メッセージの `output_tokens` は応答が生成される前の値であり、1 つの API 応答から生まれる複数のアシスタントメッセージはいずれも同じプレースホルダーを持ちます。実際の出力数は応答の最後に報告されて結果メッセージに入るので、結果の `usage`（モデル別内訳が要るなら `modelUsage`）から読む必要があります。従来この位置にあった「ID で重複排除すればステップごとのトークン数が正確に得られる」という警告は撤回され、サンプルコードも入力トークンだけをステップごとに積み上げ、出力トークンは結果メッセージから取る形に差し替えられました。ストリーミング中に伸びていく出力数を見たい場合は `includePartialMessages` を立てて `message_delta` イベントの `usage` を読む、という案内も加わっています。

集計単位の説明も整理されました。`usage` はメインのエージェントループだけを対象とし、サブエージェントや補助的なモデル呼び出しを含まず、ストリーミング入力モードではターンごとの値になります。対して `modelUsage` と `total_cost_usd` は、メインループ・サブエージェント・コンパクションや Workflow エージェントといった内部呼び出しを含むクエリパイプライン全体を対象とし（権限分類器やトークン数計測などパイプライン外の呼び出しは除く）、ストリーミング入力モードでは呼び出し全体の累計になります。新設の **ストリーミング入力モードでのコスト追跡** では、累計が `/clear` `/reset` `/new` でリセットされること、呼び出し全体を出すには各 `/clear` の直前の結果と最終結果を足せばよいこと、TypeScript では `SDKConversationResetMessage` でリセットを検出できるが Python SDK はそのメッセージをアプリへ渡さないことが書かれました。もう 1 つの新設 **セッションクラッシュ後の合計の復旧** では、クラッシュ時の `error_during_execution` はコストのフィールドがゼロで届きうるため、直前ターンの結果を使うか、それが使えなければアシスタントメッセージの `usage` を足し合わせる（この方法ではメインループの入力とキャッシュのトークンしか復旧できない）という 2 段階が示されています。

- [Track cost and usage - Claude Code Docs (English)](https://code.claude.com/docs/en/agent-sdk/cost-tracking#read-output-tokens-from-the-result-message)
- [Track cost and usage - Claude Code Docs (English)](https://code.claude.com/docs/en/agent-sdk/cost-tracking#track-costs-in-streaming-input-mode)

## 3. サブエージェントの増殖を抑える 3 つの上限が文書化された

SDK のサブエージェントのページに **サブエージェントの深さ・同時実行数・支出に上限をかける** という節が新設されました。`allowedTools` に `Agent` を入れた時点で、いつ何個のサブエージェントを起動するかは Claude が決め、そのサブエージェントがさらにサブエージェントを起動しうるため、1 つのプロンプトがエージェントの木に育ちます。抑える手段は 3 つで、深さは `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH`（既定 3 層、`1` で入れ子を止める）、同時実行数は `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS`（既定 20。超えると `Concurrent subagent limit reached` を返して起動を拒否するが、ultracode が有効なセッションは拒否されない）、支出は TypeScript の `maxBudgetUsd` / Python の `max_budget_usd`（既定は無制限。`total_cost_usd` と比較され、超えると `Budget limit reached` で起動を拒否し、動作中のバックグラウンドサブエージェントを止め、`error_max_budget_usd` でクエリを終える）です。前 2 つは `env` オプション経由の環境変数で渡しますが、TypeScript の `env` はサブプロセスの環境を置き換えるため `process.env` を展開して `PATH` などを残す必要があり、Python は継承した環境にマージする、という違いも明記されました。これらの上限は TypeScript SDK v0.3.219・Python SDK v0.2.127（いずれも Claude Code v2.1.219 以降を同梱）以降が前提です。

配下の **Opus 5 でサブエージェントを使う** も新規です。Claude Opus 5 は以前のモデルより積極的に委譲するため、Opus 5 で走らせるクエリほどこれらの上限が効いてきます。システムプロンプトの選び方によって Claude Code 側の抑制が入るかどうかが変わり、`claude_code` プリセットを使っていてモデルが Opus 5 のときは「頼まれない限り Agent ツールを呼ばない」という 1 行がシステムプロンプトに足されます（Agent ツール自体は利用可能なまま）。カスタムのシステムプロンプトを渡した場合や `systemPrompt` を指定しない場合は Claude Code がシステムプロンプトを組み立てないためその行も入らないので、Opus 5 のプロンプトエンジニアリングガイドにある委譲の指示を自分のプロンプトに入れるよう案内されています。いずれの指示も Claude を誘導するだけなので、上限の設定は別途行うこと、とも念を押されています。

- [Subagents in the SDK - Claude Code Docs (English)](https://code.claude.com/docs/en/agent-sdk/subagents#cap-subagent-depth-concurrency-and-spend)

## 4. claude.ai から同期したスキルの扱いが文書化された

スキルのページに **claude.ai から同期されたスキル** という節が新設され、配下に 4 つの小節が付きました。Claude Code は同期スキルを「そのマシンで書いたファイル」ではなくアカウントからダウンロードしたものとして扱うため、通常のスキルには適用されない規則がかかります。読み込み場所は Cowork とクラウドセッションなら設定不要で、それ以外のマシン上のセッションでは `CLAUDE_CODE_SYNC_SKILLS=1` を立てた非対話実行（`-p`）で一度ダウンロードする必要があります。ダウンロード先は `~/.claude/skills/synced/` で、実行後もディスクに残るため以降の対話セッションからも読み込まれ、`/skills` メニューと `/context` では `claude.ai sync` の下にまとめて表示されます。claude.ai 側でスキルを増やしたり変えたりしたら、同じコマンドをもう一度実行します。

名前が衝突したときの規則も明文化されました。同期スキルは、組み込みコマンド・バンドルスキル・各レベルのローカルスキル・プラグインスキル・`.claude/commands/` のファイル・MCP プロンプトのいずれかと名前が一致するとスキップされ、そのコマンドの方が動きます。セッションで使えない組み込みコマンドやバンドルスキルの名前も予約されたままなので、それらと同名の同期スキルもスキップされます。名前の比較は大文字小文字・空白・不可視文字を無視し、全角英字やダッシュの異体といった互換形も素の文字と同一視するため、同期された `Commit` はローカルの `commit` と併存できません。一方、別の文字体系の似た文字だけが違う名前は別名として扱われるので、見分けは `claude.ai sync` のラベルで行います。フロントマターはどの種類のセッションでも尊重され（`allowed-tools` の付与も通常の権限フローを通る）、説明などの表示テキストは制御文字が除去され、Claude に渡るテキストでは山括弧もエスケープされます。本文の扱いはセッションの種類で分かれ、クラウドセッションではローカルスキルと同じ、デスクトップの Cowork セッションでは `!` コマンド行が `disableSkillShellExecution` のプレースホルダーに置換され、それ以外のマシン上のセッションでは `!` コマンドを実行せず、`@` 参照のファイルも添付せず、`${CLAUDE_PROJECT_DIR}` と `${CLAUDE_SESSION_ID}` の置換も行わないため、いずれもリテラルなテキストとして Claude に届きます。

- [Extend Claude with skills - Claude Code Docs (English)](https://code.claude.com/docs/en/skills#how-synced-skills-behave)
- [Extend Claude with skills - Claude Code Docs (English)](https://code.claude.com/docs/en/skills#where-synced-skills-load)

## 5. forceLoginOrgUUID が検証するのは claude.ai ログインだけだと明記された

認証のページの **組織へのログインを制限する** 節が書き直されました。従来は「両方のキーを設定すると Claude Code はログインを指定組織に制限し、別の組織の資格情報が有効なら起動時に終了する」と書かれていましたが、今回この説明の適用範囲が絞られ、`forceLoginOrgUUID` が検証するのは **claude.ai アカウントのログイン** であることが明記されました。他の組織への claude.ai ログインはエラーになり、使用中の claude.ai 資格情報が一覧にない組織のものなら起動時に終了します。一方 Claude Console のログインについては、単一の Console 組織 ID を設定したときに Console のサインインページで組織を事前選択するためだけに使われ、できあがった Console 資格情報がどの組織のものかはログイン時にも起動時にも確認されません。キーを配る前に Console アカウントでログイン済みだった開発者はそのままログイン状態が続くため、claude.ai のサインインへ誘導したい場合は `forceLoginMethod` に `"claudeai"` を設定するよう案内されています。

`forceLoginMethod` の方は従来どおり v2.1.212 以降すべてのログイン経路に適用されますが、こちらにも注意書きが加わりました。対話的な `/login` フローでは `claudeai` か `console` の方式を **事前選択するだけで強制はしない** ため、`forceLoginMethod: "claudeai"` を設定していても開発者はその場で Console ログインを完了できます。経路ごとの違いも整理され、ターミナル・VS Code 拡張・Agent SDK のログインは claude.ai アカウントについて `forceLoginOrgUUID` を検証、`claude setup-token` と `/install-github-app` は `forceLoginMethod` のみ適用（したがって別組織のトークンを発行しうる）、ゲートウェイのサインインは `forceLoginMethod` によって選択されるものであって制限されるものではなく Anthropic の組織に対して認証しないため `forceLoginOrgUUID` は適用外、となっています。設定・エンタープライズデプロイ・メモリ・Zero Data Retention の各ページの記述も、この整理に合わせて「制限（restrict）」から「適用（apply）」「検証（verify）」へ言い換えられました。

- [Authentication - Claude Code Docs (English)](https://code.claude.com/docs/en/authentication#restrict-login-to-your-organization)
- [Claude Code settings - Claude Code Docs (English)](https://code.claude.com/docs/en/settings#available-settings)

## 新規追加されたページ

<!-- light:new-pages:start -->
（今回の対象期間に新規追加されたページはありません）
<!-- light:new-pages:end -->

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
- [**SDK のサブエージェント**](#1-sdk-のサブエージェント) ([English](https://code.claude.com/docs/en/agent-sdk/subagents#cap-subagent-depth-concurrency-and-spend)):  
  変更行数は約 97 行で今回最多。上限 3 種と Opus 5 の委譲に関する節が新設された（詳細はハイライト 3 参照）。
- [**コストと使用量の追跡**](#2-コストと使用量の追跡) ([English](https://code.claude.com/docs/en/agent-sdk/cost-tracking#read-output-tokens-from-the-result-message)):  
  変更行数約 96 行。出力トークンの扱いが訂正され、ストリーミング入力とクラッシュ復旧の節が加わった（詳細はハイライト 2 参照）。
- [**MCP で外部ツールに接続する**](#3-mcp-で外部ツールに接続する) ([English](https://code.claude.com/docs/en/agent-sdk/mcp#connection-timeouts)):  
  stdio サーバーの例からタブ表示が外れ、接続のタイムアウトとツール呼び出しのタイムアウトの違いが明記された。
- [**スキルで Claude を拡張する**](#4-スキルで-claude-を拡張する) ([English](https://code.claude.com/docs/en/skills#how-synced-skills-behave)):  
  claude.ai 同期スキルの節が新設され（詳細はハイライト 4 参照）、名前解決の説明が例付きの箇条書きになった。
- [**Agent SDK TypeScript リファレンス**](#5-agent-sdk-typescript-リファレンス) ([English](https://code.claude.com/docs/en/agent-sdk/typescript#task-notification-subkinds)):  
  タスク通知のサブ種別が新設され、`SDKPermissionDeniedMessage` がどの拒否を報告するかが 3 通りに整理された。
- [**セルフホスト環境リファレンス**](#6-セルフホスト環境リファレンス) ([English](https://code.claude.com/docs/en/self-hosted-environments-reference#environment-variable-only-settings)):  
  変更行数 77 行のうち大半は表の桁揃え。実質はバックグラウンドタスクの猶予を決める環境変数 1 件の追加。
- [**エラーリファレンス**](#7-エラーリファレンス) ([English](https://code.claude.com/docs/en/errors#claude-import-is-not-yet-available-in-this-build)):  
  `claude import` 関連のエントリが 2 件新設され、非対話実行の auto mode が run を中断しなくなった。
- [**セッションを外部ストレージへ永続化する**](#8-セッションを外部ストレージへ永続化する) ([English](https://code.claude.com/docs/en/agent-sdk/session-storage#resume-from-the-store)):  
  ストアから再開する経路が新節として文書化され、その場合ローカルの写しが実行終了時に消えることが明記された。
- [**システムプロンプトを変更する**](#9-システムプロンプトを変更する) ([English](https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts#improve-prompt-caching-across-users-and-machines)):  
  「ユースケースとベストプラクティス」節が 4 小節ごと削除され、正味で 50 行短くなった。
<!-- light:updated-pages:end -->

## 1. SDK のサブエージェント

追加約 94 行・削除 3 行で、今回最大の変更です。中身はハイライト 3 のとおりで、深さ・同時実行数・支出の 3 つの上限を表にまとめた節と、Opus 5 での委譲を扱う小節が新設されました。各上限に達したときに何が観測できるかも整理され、支出上限に達すると `error_max_budget_usd` とその時点の見積もりコストが返って例外ハンドラーが動くこと、同時実行数に達するとメッセージストリームに `Concurrent subagent limit reached` を載せた `tool_result` ブロックが現れ Claude も同じブロックを Agent ツールの結果として受け取ること、が示されています。

ページ冒頭にあった入れ子の Note は削除され、新設節への参照 1 文に置き換えられました。従来の Note は `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` の意味だけを説明していましたが、新しい文は「深さ・同時実行数・支出をどこまで許すかは新設節を見よ」と 3 つまとめて誘導します。

- [Subagents in the SDK - Claude Code Docs (English)](https://code.claude.com/docs/en/agent-sdk/subagents#cap-subagent-depth-concurrency-and-spend)

## 2. コストと使用量の追跡

追加約 72 行・削除約 24 行。内容はハイライト 2 のとおりですが、既存節の書き換えも広範囲です。「クエリの合計コストを取得する」節では、成功結果とエラー結果のどちらも `total_cost_usd` を持つがセッションクラッシュ後の最終結果はゼロで届きうること、Python では省略可能型なので `None` かどうか確かめてから読むことが加わりました。「失敗した会話のコストを追跡する」節には、`usage` が実際の消費を下回るエラー結果として、クラッシュ後の `error_during_execution`（全フィールドがゼロになりうる）と `error_max_budget_usd`（予算を超えた応答が `usage` から漏れる一方 `total_cost_usd` と `modelUsage` には含まれる）の 2 つが挙げられ、選べるなら `usage` ではなく `total_cost_usd` か `modelUsage` から計上するよう案内されています。

「出力トークンの食い違いを解決する」という旧節は丸ごと置き換えられました。旧節は同一 ID のメッセージで `output_tokens` が食い違う稀なケースについて「最大値を使う」「結果メッセージを優先する」「不一致は GitHub へ報告する」と述べていましたが、今回それは食い違いではなくプレースホルダーであるという説明に改まり、報告を促す項目もなくなっています。あわせて、サブエージェントが `total_cost_usd` に足す分を抑えたい場合はサブエージェント側の 3 つの上限を設定するように、という誘導も加わりました。

- [Track cost and usage - Claude Code Docs (English)](https://code.claude.com/docs/en/agent-sdk/cost-tracking#recover-totals-after-a-session-crash)

## 3. MCP で外部ツールに接続する

追加約 36 行・削除約 53 行で、正味では短くなっています。最も行数が動いたのは stdio サーバーの節で、「コード内」と「.mcp.json」の 2 タブ構成をやめ、`.mcp.json` の書き方は設定ファイルの節を見るよう促したうえで、コード例だけを言語別のコードグループとして残す形になりました。

内容面では 2 つです。1 つは `init` メッセージのサーバー状態に関する説明が簡素化されたことで、「`connected` 以外を全て失敗として扱うのではなく `failed` と `needs-auth` を見る」という具体的な指示や、キャッシュ済みツールリストを持つサーバーが `pending` と表示される旨の詳細が削られ、エラーハンドリングの節への参照にまとめられました。もう 1 つはタイムアウトの区別で、既定 30 秒の上限は **接続の試行にのみ** 適用されること、実行中のツール呼び出しにかけられる時間を変えたいなら `MCP_TOOL_TIMEOUT` を設定することが加わっています。

- [Connect to external tools with MCP - Claude Code Docs (English)](https://code.claude.com/docs/en/agent-sdk/mcp#connection-timeouts)

## 4. スキルで Claude を拡張する

追加約 79 行・削除 7 行。中心は claude.ai 同期スキルの節（ハイライト 4 参照）ですが、既存節にも加筆があります。名前が衝突したときの解決順序は 1 段落の説明から例付きの箇条書きに書き換えられ、`~/.claude/skills/` とプロジェクトの `.claude/skills/` の双方に `deploy` があれば `/deploy` は personal の方が動く、といった具体例が各項目に付きました。最終項目として、どのソースのスキルやコマンドも同名の同期スキルを上書きすることも加わっています。

文字列置換の表には `${CLAUDE_PLUGIN_ROOT}`（プラグインのインストール先）と `${CLAUDE_PLUGIN_DATA}`（更新をまたいで残る永続データディレクトリ）の 2 行が追加され、プラグインスキルではこの 2 つもスキル本文と `allowed-tools` の Bash ルールの両方で置換されると明記されました。あわせて、引数プレースホルダー用のバックスラッシュエスケープは `${CLAUDE_*}` 変数には効かないという注意も加わっています。このほか `skillOverrides` の `"off"` の説明が「ターミナルの `/` メニューだけでなく」という排他的な言い回しから「ターミナルの `/` メニューに加えて」に直され、非対話セッションで `help` と `feedback` が予約されない話にも、同期スキルの方は実行可否に関わらず組み込みコマンドと同名ならスキップされる、という補足が入りました。

- [Extend Claude with skills - Claude Code Docs (English)](https://code.claude.com/docs/en/skills#where-skills-live)

## 5. Agent SDK TypeScript リファレンス

追加約 56 行・削除約 23 行。新設は **タスク通知のサブ種別** の節です。Anthropic のサーバーが通知の出どころを検証できたときにだけ `origin` に `subkind` が付き（v2.1.213 以降）、値は 2 つです。`scheduled-trigger` はルーチンの保存済みプロンプトがトリガー（スケジュール・API トリガー・GitHub トリガー・Run now）で配信されたもので、モデルにはそのセッションの割り当てタスクとして提示され、他のタスク通知に付く注意書きとは別の枠組みになります。`peer-send-message` は Claude Code on the web のセッション同士が使うサーバー側 `send_message` ツールで送られ、両セッションが同じプライベートグループに属するとサーバーが検証したものです（v2.1.224 以降）。自マシンで発火するスケジュール実行や PR アクティビティ、バックグラウンドタスクの完了には `subkind` は付かず、セッション間メッセージングの `SendMessage` はそもそもタスク通知ではなく `kind: "peer"` になる、という切り分けも書かれました。`SDKMessageOrigin` には `unclassified`（分類できなかった注入ターン。v2.1.223 以降。アプリ側が設定してはいけない）も加わっています。

`SDKPermissionDeniedMessage` の説明は、報告される拒否が実行構成で 3 通りに分かれる形に書き直されました。`canUseTool` コールバックがある場合は Claude Code が独自に決めた拒否だけ、コールバックも `permissionPromptToolName` も無い場合（素の `-p` 実行など）はプロンプトが出るはずだった呼び出しの拒否も含めて報告（v2.1.223 より前はコールバック無しの実行ではこのイベント自体が出なかった）、MCP のプロンプトツールを指定した場合はイベントを一切出さない、となっています。いずれの構成でも `PreToolUse` フック経路の拒否は対象外で、イベントはベストエフォートなので正式な記録は結果メッセージの `permission_denials` である、とも明記されました。このほか `resumeDropsTurn` オプション（v2.1.223 以降）、結果メッセージの `usage` / `modelUsage` / `total_cost_usd` の対象範囲、サブエージェント結果の `usage.output_tokens_details.thinking_tokens`（TypeScript SDK v0.3.228 以降）、`worktreePath` は worktree を残した場合に付くという言い換え、`SDKConversationResetMessage` は `query()` 内では `/clear` とその別名でのみ発生するという限定が加わりました。

- [Agent SDK reference - TypeScript - Claude Code Docs (English)](https://code.claude.com/docs/en/agent-sdk/typescript#task-notification-subkinds)

## 6. セルフホスト環境リファレンス

変更行数は 77 行ですが、その大半は 2 つの表の桁揃えによる整形で、内容が変わったのは数行です。実質的な追加は環境変数専用の設定に加わった `SELF_HOSTED_RUNNER_BG_RESULT_GRACE_MS`（既定 30000、v2.1.228 以降）で、バックグラウンドタスクが終わってから結果を読む後続ターンが始まるまでの間、ランナーがそのセッションをビジー扱いにする時間です。`0` や解釈できない値を渡すと既定値に戻るため、この保持を無効化することはできません。

この保持は既存の 2 つのフラグの説明にも書き足されました。`--drain-wait-sec` による待機中は、終わったばかりのバックグラウンドタスクをこのウィンドウの間まだ実行中として数えます。`--release-idle-session-min` によるアイドル解放でも、タスクが終わっていて後続ターンがまだ始まっていない場合はそのターンが始まるまでセッションを保持し、待つのはこのウィンドウまでです。このほか `--confine-repo-settings` の説明が、モードの列挙を先に置く形（`warn` は違反をログして起動、`enforce` は拒否、`off` はスキャン無効）に整理されました。

- [Self-hosted environments reference - Claude Code Docs (English)](https://code.claude.com/docs/en/self-hosted-environments-reference#environment-variable-only-settings)

## 7. エラーリファレンス

追加約 54 行・削除 8 行。コマンドラインエラーに 2 件が新設されました。**claude import is not yet available in this build** は、インポートのフローがフラグで無効になっている状態で `claude import` を実行した場合に終了コード 1 で出るもので（v2.1.222 より前は `import` をプロンプトとして扱い対話セッションを始めていた）、原因はインストール後にまだセッションを開いておらずフラグを取得していない・Amazon Bedrock など 4 つのクラウドプロバイダーを使っている・`DISABLE_TELEMETRY` などフラグ取得を止める変数を設定している、のいずれかだと説明されています。**Could not read Claude Code config** は `~/.claude.json` をパースできない状態で `claude import` を実行した場合で、サブコマンドは対話セッションのような復旧ダイアログを出さずに終了コード 1 で終わります（v2.1.222 より前は対話セッションが始まりダイアログが処理していました）。自動再試行の対象にも、Google Cloud's Agent Platform の資格情報の期限切れ・不在で出る `Could not load the default credentials` が加わり、キャッシュを捨てて最大 2 回まで再試行し `gcpAuthRefresh` があれば実行したうえでエラーを表示する（v2.1.228 より前は再試行予算を使い切るまで粘っていた）と書かれました。

**そして auto mode に関する記述が、前回サマリで紹介した内容から撤回されています。** 分類器のリクエストが安全機構に拒否された場合、非対話（`-p`）実行でも Claude Code は run を止めなくなりました。`Agent aborted: auto mode classifier request refused by the safety safeguard in headless mode` が返るのは `--input-format stream-json` なしの `-p` 実行でバックグラウンドサブエージェントが要求した場合だけで、それ以外（対話セッションや `-p` のメイン会話）では拒否がそのまま Claude に返ります。分類器のコンテキストウィンドウを会話が超えた場合も同様に 3 通りへ整理され、対話セッションは通常の権限プロンプトへフォールバック、`-p` のバックグラウンドサブエージェントは `Agent aborted: auto mode classifier transcript exceeded context window in headless mode` を含むエラー結果を受け取って run は続行、`--permission-prompt-tool` なしの `-p` のその他の箇所ではフォールバック先が無いのでアクションが実行されないまま run が続く、となりました。対処の箇条書きも、`/compact` の実行など対話セッション限定の項目に「対話セッションでは」と条件が付いています。ベストプラクティスと権限モードのページの記述もこれに合わせて書き換えられました。

- [Error reference - Claude Code Docs (English)](https://code.claude.com/docs/en/errors#auto-mode-cannot-determine-the-safety-of-an-action)
- [Choose a permission mode - Claude Code Docs (English)](https://code.claude.com/docs/en/permission-modes#when-auto-mode-falls-back)

## 8. セッションを外部ストレージへ永続化する

追加約 47 行・削除約 11 行。新設の **ストアから再開する** 節で、`resume` や `continue: true`（Python は `continue_conversation=True`）をストアと併用したときの流れが説明されました。SDK はサブプロセスを起動する前にストアへトランスクリプトを要求し（`resume` なら指定 ID、`continue` ならストアの最新セッション）、返ってきたら一時的な設定ディレクトリへ書き出して `CLAUDE_CONFIG_DIR` をそこへ向けたままサブプロセスを走らせ、実行終了時にそのディレクトリを削除します。一時ディレクトリには実際の設定ディレクトリからファイルが種として複製されますが、複製範囲は言語で異なり、TypeScript は資格情報・`.claude.json`・ユーザーの `settings.json`（一時ディレクトリ下で誤動作する `enabledPlugins` / `extraKnownMarketplaces` / `env` 内の `CLAUDE_CONFIG_DIR` は除去）まで、Python は資格情報と `.claude.json` のみです。そのため Python でユーザーの `settings.json` の `apiKeyHelper` を使って認証しているアプリは、ストアから再開すると `Not logged in` で失敗します。ストアに該当セッションが無い場合の挙動も、`resume` は両 SDK ともローカルのトランスクリプトを再開、TypeScript の `continue: true` は新規セッション、Python の `continue_conversation=True` は最新のローカルセッションを継続、と分かれることが示されました。

**二重書き込みのアーキテクチャ** の節も書き直され、どちらの写しが実行後に残るかが分岐することが明記されました。新規セッション、およびストアに該当セッションが無かった再開では、設定ディレクトリ下のローカルトランスクリプトが残ってストアには複製が届きます。対してストアから再開した実行では、ローカルの写しが実行終了時に削除されるため **ストアが唯一の永続的な写し** になります。この帰結として、ミラー書き込みが失敗して破棄されたバッチはストアから再開した実行では復旧手段が無くなること、ストアから再開した実行はローカルにトランスクリプトを残さないので保持ポリシーはストア側のものだけになること、が加筆されました。一時ディレクトリ運用時に OAuth 資格情報や `apiKeyHelper` を使っていると `Not logged in` になるため、ファイルを先にコピーするか `ANTHROPIC_API_KEY` を `env` で渡す、という注意も新しく入っています。

- [Persist sessions to external storage - Claude Code Docs (English)](https://code.claude.com/docs/en/agent-sdk/session-storage#dual-write-architecture)

## 9. システムプロンプトを変更する

追加 3 行・削除約 50 行で、今回唯一の「ほぼ削除のみ」のページです。ページ末尾にあった **ユースケースとベストプラクティス** という h2 が、配下の「CLAUDE.md を使うとき」「出力スタイルを使うとき」「`systemPrompt` の append を使うとき」「カスタム `systemPrompt` を使うとき」という 4 小節ごと削除されました。それぞれ「〜に最適」「例」という箇条書きで使い分けを助言していた部分で、いずれも本文前半の「出発点を決める」や「4 つのアプローチを比較する」と重なる内容でした。CLAUDE.md の使い分けについてはメモリのページの該当節への参照が残っています。

残った記述の書き換えは軽微です。CLAUDE.md の節では「SDK は内容をシステムプロンプトではなく会話へ注入する」という説明に「システムプロンプトには手を触れない」という言い方が足され、参照先もメモリのページの該当節を名指しする形になりました。プロンプトキャッシュの節とトレードオフの記述では `auto-memory` という表記が `auto memory` に統一されています。

- [Modifying system prompts - Claude Code Docs (English)](https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts#improve-prompt-caching-across-users-and-machines)

## 軽微な更新

<!-- light:minor-updates:start -->
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
<!-- light:minor-updates:end -->

## 新着情報

<!-- light:whats-new:start -->
（今回の対象期間に更新された新着情報ページはありません。前回の Week 32 以降、新しい週次ダイジェストは公開されていません）
<!-- light:whats-new:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-08-11.md](./archives/latest/2026-08-11.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-08-11.md](./archives/latest-detail/2026-08-11.md)

<!--
base_commit: 74a9f7d4d87a53478220a4bbf69fc28fa7c10294
head_commit: 6bb349f9c8d4ed9d313be35f06d8f5b1ff63f332
generated_at_full: 2026-08-13T15:10:03+09:00
-->
