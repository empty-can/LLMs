---
対象期間: 2026年06月15日 〜 2026年06月16日
作成日: 2026-06-16
---

# Claude Code 公式ドキュメント更新サマリ

```markdown
今回は新規ページ・新着情報の追加はなく、既存リファレンスページの精緻化が中心です。前回の changelog で予告されていた v2.1.178 の機能群（権限の入力パラメータマッチ、ネストした設定ディレクトリなど）が各リファレンスページに正式記載されたほか、エージェントチームのワークフローが大きく刷新され、changelog に v2.1.179 のバグ修正が追加されました。主要な 5 件をハイライトとして整理します。

主要なものを以下に挙げます。

1. エージェントチームが刷新され、チーム作成・クリーンアップの明示手順が廃止された（チームメンバー生成だけで自動的にチームが形成され、セッション終了時に自動後片付け。タスクリストは再開のため永続化）（v2.1.178）
2. 権限ルールが `Tool(param:value)` 構文で入力パラメータにマッチできるようになり、権限リファレンスページに正式セクションとして記載された（deny/ask 専用。例: `Agent(model:opus)`）（v2.1.178）
3. 新設定 `footerLinksRegexes` で、ターン出力中の正規表現マッチに応じてフッターにクリック可能なバッジ（課題キー等のリンク）を表示できるようになった（v2.1.176）
4. ネストした `.claude/` 設定ディレクトリのサポートが拡大し、スキル・サブエージェント・出力スタイル・ワークフローのいずれも作業ディレクトリ直下のネスト定義をロードし、名前衝突時は最も近いものを優先するようになった（v2.1.178）
5. アドバイザーモデルのペアリング検証がサーバー（API）側からクライアント側へ移り、リクエスト送信前に検証されるようになった。サブエージェントは設定済みアドバイザーを継承し、自身のモデルで同じペアリング検査を行う
```

## ハイライト

1. [**エージェントチームのワークフロー刷新**](./latest-detail.md#1-エージェントチームのワークフロー刷新):  
  エージェントチームが v2.1.178 で大きく刷新された。事前のチーム作成や終了時の「クリーンアップ」操作が不要になり、最初のチームメンバーを生成した時点でメインセッションをリーダーとするチームが自動的に形成される。`TeamCreate` / `TeamDelete` ツールは廃止。チームはセッション由来名（`session-` + セッション ID 先頭 8 文字）で保存され、チーム設定はセッション終了時に削除される一方、タスクリストはローカルに永続化され再開セッションに引き継がれる。
2. [**権限ルールが入力パラメータにマッチ可能に**](./latest-detail.md#2-権限ルールが入力パラメータにマッチ可能に):  
  権限ルールが `Tool(param:value)` 構文でツールの最上位入力パラメータにマッチできるようになり、前回 changelog のみの記載だった機能が権限リファレンスページに正式セクションとして加わった。`Agent(model:opus)`・`Bash(run_in_background:true)` のように指定でき、`*` ワイルドカードも使える。安全側の設計として **deny / ask ルール専用**で、allow ルールには使えない。
3. [**フッターリンクバッジの追加**](./latest-detail.md#3-フッターリンクバッジの追加):  
  新設定 `footerLinksRegexes`（v2.1.176）で、ターン出力に正規表現がマッチしたときに入力欄下のフッターへクリック可能なバッジを描画できる。課題トラッカーのキーなどをセッションリンク化する用途で、`pattern`・`url`（`{name}` プレースホルダ）・任意の `label` を指定する。URL は出自オリジンの固定や 2048 文字上限、スキーム許可リスト、最大 5 個などの制約がある。
4. [**ネストした設定ディレクトリのサポート拡大**](./latest-detail.md#4-ネストした設定ディレクトリのサポート拡大):  
  v2.1.178 で、スキル・サブエージェント（`.claude/agents/`）・出力スタイル・ワークフローのいずれも、作業ディレクトリとリポジトリルートの間にあるネストした `.claude/` ディレクトリからロードされるようになった。同名定義が複数あるときは作業ディレクトリに最も近いものが優先され、ネストしたスキルは `<dir>:<name>` の修飾名で併存できる。
5. [**アドバイザーのペアリング検証がクライアント側に**](./latest-detail.md#5-アドバイザーのペアリング検証がクライアント側に):  
  アドバイザーモデルとメインモデルのペアリング検証が、従来の API（サーバー）側強制からクライアント側のリクエスト前検証へ変わった。アドバイザーがメインモデルより非力な場合はリクエストに添付されず、`/advisor` の出力と通知で示される。サブエージェントは設定済みアドバイザーを継承し、自身のモデルで同じペアリング検査を適用する。

## 新規追加されたページ

*(今回の対象期間に新規追加されたページはありません)*

## 大幅に更新されたページ

- [**エージェントチーム（agent-teams）の刷新**](./latest-detail.md#1-エージェントチームのワークフロー刷新) ([English](https://code.claude.com/docs/en/agent-teams#architecture)):  
  チーム作成・クリーンアップの明示手順の廃止、`TeamCreate` / `TeamDelete` の削除、セッション由来名での保存とタスクリストの永続化など、ページ全体にわたる大幅な書き換えが入りました（詳細はハイライト1参照）。

## 軽微な更新

今回の対象期間は、新規ページ・新着情報の追加はなく、既存リファレンスページの記述精緻化と changelog（v2.1.179）の追加が中心です。ハイライトに挙げた以外の更新を分類別に示します。

**新機能**
- Amazon Bedrock の認証情報ヘルパー出力に任意の `Expiration` フィールドが追加された。v2.1.176 以降、コマンドが有効な ISO 8601 の `Expiration` を返すと、その 5 分前まで認証情報がキャッシュされる（無い場合や旧バージョンでは従来どおり 1 時間キャッシュ）。 — [English](https://code.claude.com/docs/en/amazon-bedrock#2-configure-aws-credentials)
- サブエージェント定義の `tools` / `disallowedTools` が、正確なツール名に加えて MCP サーバーレベルのパターンを受け付けるようになった。`mcp__<server>` や `mcp__<server>__*` でそのサーバーの全ツールを付与/除去でき、`disallowedTools` の `mcp__*` は任意サーバーの全 MCP ツールを除去する（subagents ページおよび Python/TypeScript SDK の `AgentDefinition` リファレンスに反映）。 — [English](https://code.claude.com/docs/en/sub-agents#available-tools)
- Agent SDK に 2 つのメッセージ型が追加された。`SDKInformationalMessage`（ループからの非エラーのステータスバナーや hook フィードバックを `level` 付きで運ぶ）と `SDKWorkerShuttingDownMessage`（ホスト終了や Remote Control 切断によるワーカーの正常終了理由 `reason` を通知）。あわせて `SystemMessage` の `subtype` に `informational` / `worker_shutting_down` が加わった。 — [English](https://code.claude.com/docs/en/agent-sdk/typescript#sdkmessage)

**機能改善**
- `availableModels` アローリストの適用範囲が明文化・拡張された。メインセッション/サブエージェント/アドバイザー/フォールバックチェーンに加え、エイリアス解決（`ANTHROPIC_DEFAULT_*_MODEL` でアローリスト外へ転送できない）と fast mode（`/fast` がリスト外の Opus へ暗黙切替する場合は「is not in your organization's allowed models」で拒否）も対象になった。 — [日本語](https://code.claude.com/docs/ja/model-config#restrict-model-selection) / [English](https://code.claude.com/docs/en/model-config#restrict-model-selection)
- Remote Control に「Check connection status」節が追加され、フッターの `/rc active` インジケータ（クリックで claude.ai のセッションを開く）と、接続失敗時の赤い `/rc failed` インジケータが整理された。自動生成タイトルが会話の言語（または `language` 設定）に一致するようになり（v2.1.176）、新たなエラーメッセージ「Couldn't verify Remote Control eligibility」（フィーチャーフラグサービスへ到達できない場合、v2.1.178 追加）と、「Remote Control is not yet enabled for your account」の文面整理も入った。 — [English](https://code.claude.com/docs/en/remote-control#check-connection-status)
- 権限ルールの評価順序の説明が補強され、`Bash(aws *)` のような広い deny ルールが、より狭い allow ルール（`Bash(aws s3 ls)` 等）にマッチする呼び出しも含めてブロックする＝deny ルールは allowlist 例外を持てないことが明記された。 — [English](https://code.claude.com/docs/en/permissions#manage-permissions)
- auto mode の分類器がサブエージェントを評価する 3 段階のうち、spawn 時にタスク説明を事前評価する「ステップ 1」が v2.1.178 以降であることが注記された（旧バージョンはステップ 2・3 のみ）。
- `--add-dir` で追加したディレクトリ内の `.claude/agents/` のサブエージェントもロードされるようになり、`--add-dir` から読み込まれる設定タイプの表に「Subagents」が追加された。 — [日本語](https://code.claude.com/docs/ja/permissions#additional-directories-grant-file-access-not-configuration) / [English](https://code.claude.com/docs/en/permissions#additional-directories-grant-file-access-not-configuration)
- 「Verify active settings」節が書き直され、`/status` の **Status** タブの `Setting sources` 行（管理設定では `(remote)` / `(plist)` / `(HKLM)` 等の配信チャネルを併記）が読み込まれたソースを示すこと、**Config** タブはトグル編集用であって `settings.json` の内容ビューではないことが明確化された。 — [日本語](https://code.claude.com/docs/ja/settings#verify-active-settings) / [English](https://code.claude.com/docs/en/settings#verify-active-settings)
- PostToolUse の `resolvedModel`（サブエージェントが実際に動くモデル）が、`availableModels` などの override が効いた場合に `tool_input` の `model` と異なりうる旨が補足された。
- SDK の Todo 移行ガイドに、ストリームの `tool_use` 入力は生のキー名であり、Claude Code が実行前に `id`/`task_id`→`taskId`、`active_form`→`activeForm` と一部修復するがストリームには反映されない、という注意（サンプルも防御的読み取りに更新）が追加された。
- WebFetch の `domain:` ワイルドカードの説明が、先頭 `*.` または単独 `*` 以外の位置ではワイルドカードが 2 つのドット間のテキストにのみマッチする（`example.*` は `example.org` にマッチするが `example.evil.com` にはマッチしない）という形に書き直された。
- プラグインの skills ローディングについて、`source` がマーケットプレースルート（`source: "./"` 等）の場合は `skills` 配下に列挙したサブディレクトリがそのエントリの完全集合になる、という挙動が追記された。
- `CLAUDE_CODE_FORK_SUBAGENT` と `/fork` の説明が「fork をモデルの既定にする」から「Claude が `fork` サブエージェントタイプを明示要求して fork を生成できる」へ整理され、サブエージェントタイプ無しの spawn は引き続き general-purpose を使う旨が明確化された。あわせて `CLAUDE_CODE_SCROLL_SPEED` の小数値（1 未満）挙動の説明など、環境変数表のいくつかの記述が精緻化された。

**バグ修正**

changelog に v2.1.179（2026年06月16日）が追加された。主な修正は以下のとおり。

- ストリーム途中の接続切断時に部分応答を保持するようになり、生のエラー表示やスピナーが「running tool」で固まる問題が解消された。
- WSL2（Windows Terminal / VS Code）でのマウスホイールスクロールが修正された（v2.1.172 のリグレッション）。
- sandbox の `denyRead`/`allowRead` グロブが大きなディレクトリツリーに対して Bash ツールの説明を肥大化させ、Linux でセッションが使えなくなる問題が修正された。
- フィードバック調査が、ターン完了直後の 1 桁の返信をセッション評価として誤って取り込む問題が修正された。
- ウェルカム画面で複数のプロモバナーが積み重なる問題が修正された（1 セッションあたり最大 1 つ）。
- サブエージェント閲覧時に Ctrl+O でトランスクリプトが表示されない問題が修正された。
- プロンプト入力欄のクリックでサブエージェント/フッターパネルからフォーカスが戻らない問題が修正された。
- リモートセッションのバックグラウンドタスクがターン間で「still running」のまま見える問題が修正され、リモートセッションのプラグインロード性能も改善された。

**その他**
- `SDKMessageOrigin` の `peer` に `senderTaskId`（メッセージを送ったインプロセスのバックグラウンドサブエージェントのタスク ID。クロスセッションのピアでは省略）が追加された。

## 新着情報

*(今回の対象期間に新着情報（whats-new）ページの更新はありません)*

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-06-15.md](./archives/latest/2026-06-15.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-06-15.md](./archives/latest-detail/2026-06-15.md)

<!--
base_commit: 045e333d0dbf9f1ed09cfee6e2ec61227aa03027
head_commit: 903188279ac643213af8353f48bbc9b9c6dff390
generated_at_full: 2026-06-17T15:06:02+09:00
-->
