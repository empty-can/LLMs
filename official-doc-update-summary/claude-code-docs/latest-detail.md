---
対象期間: 2026年07月01日 〜 2026年07月02日
作成日: 2026-07-02
---

# Claude Code 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
今回の対象期間は、Artifacts が Pro・Max プランへ拡大したことと、v2.1.198／v2.1.199 の 2 リリースによるサブエージェント・バックグラウンドエージェントの刷新、および Claude in Chrome の一般提供が中心です。動的ワークフローには実践的な「ワークフロープロンプト例」節が新設され、エラー処理・信頼性の改善も広く入りました。今回、週刊ダイジェスト「新着情報」の更新はありません。

主要なものを以下に挙げます。

1. Artifacts が Pro・Max プランでも利用可能になった（従来は Team／Enterprise 限定。Pro・Max では自分のみに非公開で、組織共有機能は使えない）
2. サブエージェントが v2.1.198 で既定のバックグラウンド実行として一般提供され、バックグラウンドエージェントは作業完了時に自動でコミット／push／ドラフト PR を作成し、完了・入力待ちで通知フックが発火するようになった
3. Claude in Chrome が v2.1.198 で一般提供（GA）となり、プランモードでの状態変更ブラウザツールの確認・読み取り専用ツールの自動許可も修正された
4. 動的ワークフローに「ワークフロープロンプト例」節が新設され、代表的なプロンプト例と、生成されるスクリプトの形が示された
5. v2.1.199 でサブエージェントの部分結果返却・API エラーの親への報告、ストリーミング応答の部分保持、スタックした slash-skill の複数ロードなど、エラー処理と信頼性が広く改善された
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**Artifacts が Pro と Max プランに対応**](#1-artifacts-が-pro-と-max-プランに対応):  
  Artifacts の利用可能プランが Team／Enterprise から Pro・Max を含む 4 プランに拡大された。Pro・Max では artifacts は「自分のみに非公開」で管理者管理の対象外となり、組織メンバーへの共有機能は従来どおり Team・Enterprise 限定。可用性表・機能可用性表の Artifacts 要件も Pro・Max を含む形に更新された。
2. [**サブエージェントとバックグラウンドエージェントの刷新**](#2-サブエージェントとバックグラウンドエージェントの刷新):  
  v2.1.198 でサブエージェントが既定でバックグラウンド実行になり（段階的ロールアウトから一般提供へ）、Claude は作業を続けながら完了時に通知を受け取る。`claude agents` から起動したバックグラウンドエージェントは、worktree でのコード作業完了時に停止して尋ねる代わりに自動でコミット・push・ドラフト PR を作成し、入力待ち・完了で `Notification` フック（`agent_needs_input`／`agent_completed`）が発火する。組み込み Explore はメインセッションのモデルを継承（opus 上限）、サブエージェント／コンパクションは拡張思考設定を継承するようになり、`/agents` ウィザードは廃止された。
3. [**Claude in Chrome の一般提供**](#3-claude-in-chrome-の一般提供):  
  v2.1.198 で Claude in Chrome が一般提供（GA）となり、`llms.txt` のページ説明・タイトルからも「(beta)」表記が外れた。あわせて、プランモードで状態変更を伴うブラウザツール呼び出しが確認を求めるようになり、読み取り専用の `browser_batch` 呼び出しは正しく自動許可される修正が入った（v2.1.199）。ドキュメントマップにも `chrome` へ「Browser tools in plan mode」節が追加されている。
4. [**動的ワークフローのワークフロープロンプト例**](#4-動的ワークフローのワークフロープロンプト例):  
  `workflows` に「ワークフローの実行例プロンプト」節が新設された。ワークフローが適する場面（1 エージェントのコンテキストに収まらない／同じ処理を多数アイテムへ）を説明し、多数ファイルの監査、チェックが通るまでの修正ループ、多数ファイルの並列移行、変更ファイルのレビューと単一サマリ化、多ソース横断リサーチ、リストが増えなくなるまでの問題探索という代表的なプロンプト例と、保存されるスクリプトの実例（`meta` ブロック＋`agent()`／`pipeline()` を使う JavaScript）を提示する。
5. [**エラー処理と信頼性の改善**](#5-エラー処理と信頼性の改善):  
  v2.1.199 は信頼性・エラー処理の改善が中心。サブエージェントがレート制限やサーバーエラーで中断された際に黙って失敗せず部分的な作業を親に返し、API エラー（使用制限到達など）を成功結果として報告していた不具合も修正して親エージェントへ報告するようになった。API が部分出力後にストリーム途中でエラーを出してもストリーミング応答を破棄せず部分結果を保持し、スタックした slash-skill 呼び出し（`/skill-a /skill-b do XYZ`）は先頭スキルを最大 5 個までロードするようになった。
<!-- light:highlight-list:end -->

## 1. Artifacts が Pro と Max プランに対応

Artifacts（セッション出力を claude.ai 上のプライベートページとして公開する機能）の利用可能プランが、従来の Team／Enterprise から **Pro・Max を含む 4 プラン**に拡大されました。可用性表の「プラン」要件は「Pro、Max、Team、または Enterprise」に更新され、Pro・Max プランでは artifacts は**自分のみに非公開**のままで、管理者による有効化・管理（claude.ai 管理設定のトグルや保持ポリシー等）は適用されません。組織メンバーへの**共有**（ページヘッダーの Share コントロールで特定の人や全員に公開する操作）は引き続き Team・Enterprise プラン限定で、Pro・Max にはこの共有 UI がありません。

認証（`/login` で claude.ai にサインイン必須。API キー・ゲートウェイトークン・クラウドプロバイダー認証情報では公開不可）、モデルプロバイダー（Anthropic API のみ。Bedrock／Vertex AI／Foundry では不可）、組織ポリシー（CMEK・HIPAA・Zero Data Retention が無効であること）といった他の要件は変わりません。あわせて機能可用性表（プラン別）の Artifacts 行が Pro・Max でも利用可（✓）に更新され、ツールリファレンスの `Artifact` ツール説明や、直接ログインが必要な機能一覧の記述も「Pro、Max、Team、Enterprise」に揃えられました。

- [セッション出力をアーティファクトとして共有する（利用可能性） - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/artifacts#availability)
- [Share session output as artifacts (Availability) - Claude Code Docs (English)](https://code.claude.com/docs/en/artifacts#availability)
- [セッション出力をアーティファクトとして共有する（アーティファクトを共有する） - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/artifacts#share-an-artifact)
- [Share session output as artifacts (Share an artifact) - Claude Code Docs (English)](https://code.claude.com/docs/en/artifacts#share-an-artifact)

## 2. サブエージェントとバックグラウンドエージェントの刷新

v2.1.198 で、サブエージェントとバックグラウンドエージェントの挙動が大きく変わりました。サブエージェントは**既定でバックグラウンド実行**になり（従来は段階的ロールアウト）、Claude は他の作業を続けながらサブエージェントの完了時に通知を受け取ります。`claude agents` から起動したバックグラウンドエージェントは、worktree 内でのコード作業を終えると、停止して確認を求める代わりに**自動でコミット・push・ドラフト PR を作成**するようになりました。さらに `claude agents` にバックグラウンドエージェント通知が追加され、入力待ちや完了時に `Notification` フック（`agent_needs_input`／`agent_completed`）が発火します。

品質面の変更も入りました。組み込みの Explore エージェントが haiku ではなく**メインセッションのモデルを継承**するようになり（opus 上限）、サブエージェントとコンテキストコンパクションが**セッションの拡張思考設定を継承**して委任タスクの出力品質が改善されます。また、別エージェントから届いたメッセージは通常のタスク指示として扱われる一方、ユーザーの承認としては決して扱われないという境界が明確化されました。運用面では `/agents` ウィザードが廃止され、サブエージェントの作成・管理は Claude への依頼か `.claude/agents/` の直接編集で行う形になっています（ドキュメントマップからも「Use the /agents command」が削除）。

- [Create custom subagents (Run subagents in foreground or background) - Claude Code Docs (English)](https://code.claude.com/docs/en/sub-agents#run-subagents-in-foreground-or-background)

> 上記の変更は主に changelog（v2.1.198）由来です。日本語版 `sub-agents` ページは本サマリ作成時点で「既定バックグラウンド実行」を反映していない（`background` フロントマターの既定は `false` のまま）ため、日本語リンクは省略しています。

## 3. Claude in Chrome の一般提供

v2.1.198 で **Claude in Chrome が一般提供（GA）** になりました。これに伴い `llms.txt` のページ説明・タイトルから「(beta)」表記が外れています（機能自体は Google Chrome・Microsoft Edge で動作し、Web アプリのテスト・コンソールログでのデバッグ・フォーム入力の自動化・データ抽出などをブラウザとコーディングを跨いで行えます）。あわせて v2.1.199 で、プランモード時に**状態変更を伴うブラウザツール呼び出しが確認を求める**ようになり、読み取り専用の `browser_batch` 呼び出しは正しく自動許可されるよう修正されました。ドキュメントマップには `chrome` ページへ「Browser tools in plan mode」節が追加されています。

- [Use Claude Code with Chrome - Claude Code Docs (English)](https://code.claude.com/docs/en/chrome)

> Chrome の GA・プランモード対応は changelog 由来です。日本語版 `chrome` ページは本サマリ作成時点でまだ「（ベータ版）」表記で GA・「Browser tools in plan mode」節を反映していないため、日本語リンクは省略しています。

## 4. 動的ワークフローのワークフロープロンプト例

`workflows`（動的ワークフロー）に「ワークフローの実行例プロンプト」節が新設されました。ワークフローが最も適するのは、タスクが 1 つのエージェントのコンテキストに収まらない場合、または同じステップを多数のアイテムに適用する場合であると説明した上で、代表的な 6 つのプロンプト例を示します。具体的には、同一問題での多数ファイル監査（ファイルごとにファンアウトして検出結果を対立的に検証）、チェックが通るまでの修正ループ、多数ファイルの並列移行（各ファイルを分離コピーで変換）、変更ファイルのレビューと単一サマリへの集約、複数ソースを横断するリサーチ、リストが増えなくなるまでの問題探索です。

各例は「Claude にそのタスク用のワークフローを作成・実行させる」形で、ユーザー自身がスクリプトを書く必要はありません。節末には、保存されるワークフローの実体（`.claude/workflows/` 内の `meta` ブロック＋`agent()`／`pipeline()` を使うトップレベル `await` の JavaScript）の小さな実例が添えられ、Claude が生成したスクリプトの形を把握できるようになっています。

- [動的ワークフローで大規模にサブエージェントをオーケストレーションする（ワークフローの実行例プロンプト） - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/workflows#example-workflow-prompts)
- [Orchestrate subagents at scale with dynamic workflows (Example workflow prompts) - Claude Code Docs (English)](https://code.claude.com/docs/en/workflows#example-workflow-prompts)

## 5. エラー処理と信頼性の改善

v2.1.199 は信頼性とエラー処理の改善が中心のリリースです。サブエージェントがレート制限やサーバーエラーで打ち切られた際に**黙って失敗せず部分的な作業を親に返す**ようになり、サブエージェントが API エラー（使用制限到達など）を成功結果として報告していた不具合も修正され、**エラーが親エージェントに報告**されるようになりました。API が部分出力の後にストリーム途中で overloaded／サーバーエラーを返した場合も、**ストリーミング応答を破棄せず部分結果を「不完全」注記付きで保持**します。

そのほか、スタックした slash-skill 呼び出し（`/skill-a /skill-b do XYZ`）が**先頭スキルを最大 5 個までロード**するようになり（従来は最初の 1 個のみ）、SSL 証明書エラー（TLS 検査プロキシ・`NODE_EXTRA_CA_CERTS` 未設定・期限切れ証明書）はリトライを消費する前に即座に失敗して修正ヒントを表示するようになりました。リトライ制御では、`CLAUDE_CODE_RETRY_WATCHDOG` が非容量の一時エラーの既定リトライ回数を 300 に引き上げ、`CLAUDE_CODE_MAX_RETRIES` の 15 上限を撤廃しています。

> 本セクションの内容は changelog（v2.1.199）由来で、対応する通常ドキュメントページ（エラーリファレンス等）への反映は原文全文（llms-full）・日本語ページともに本サマリ作成時点で未追従のため、参考リンクは省略しています。

## 新規追加されたページ

<!-- light:new-pages:start -->
今回、リファレンス系で新規追加されたページはありません。
<!-- light:new-pages:end -->

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
上記ハイライト以外で、既存ページの規模の大きい・意味のある更新は以下の 2 件です。

- [**組織のモデル制限に関する記述の整理**](#1-組織のモデル制限に関する記述の整理) ([日本語](https://code.claude.com/docs/ja/model-config#organization-model-restrictions) / [English](https://code.claude.com/docs/en/model-config#organization-model-restrictions)):  
  組織管理者がメンバーの利用モデルを制限する方法が「Claude Enterprise プランの組織管理者が claude.ai 管理コンソールで無効化する」ものとして明確化され、Console 側での制限（`availableModels`）との使い分けが整理された。
- [**タスクリストと実行中タスクビューの区別**](#2-タスクリストと実行中タスクビューの区別) ([日本語](https://code.claude.com/docs/ja/interactive-mode#task-list) / [English](https://code.claude.com/docs/en/interactive-mode#task-list)):  
  タスクリストが「Claude が多段作業を計画するために作る ToDo チェックリスト」であり、実行中のシェルやサブエージェントを見る `/tasks` のバックグラウンドタスクビューとは別物であることが明確化された。
<!-- light:updated-pages:end -->

## 1. 組織のモデル制限に関する記述の整理

`model-config` の「組織モデル制限」節が整理されました。組織管理者がメンバーの実行できるモデルを制限する手段が、「**Claude Enterprise プラン**の組織管理者が **claude.ai 管理コンソール**で個別モデルを無効化する」ものとして明確化されています。この制限はメンバーのサインインまたは自身の API キー利用時に適用され、組織サービスキーのようなユーザーに紐づかない組織スコープの認証情報には適用されません。制限は認証時にアカウントの権利として配信され、設定の `availableModels` とは別物で、セッション作成時にサーバー側でも独立に適用されます（要 v2.1.187 以降）。

あわせて、**Claude Console にはモデル制限機能が無い**ことが明記され、Enterprise プランを持たない組織（Anthropic API で認証するメンバーを含む）は管理設定の [`availableModels`] でモデルを制限し、Default オプションもカバーするには `enforceAvailableModels` を併用する、という使い分けが示されました。なお、ドキュメントマップには `model-config` へ「Organization default model」「Organization effort limits」の見出しも追加されていますが、これらの本文は原文全文（llms-full）には未収録です。

- [モデル設定（組織モデル制限） - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/model-config#organization-model-restrictions)
- [Model configuration (Organization model restrictions) - Claude Code Docs (English)](https://code.claude.com/docs/en/model-config#organization-model-restrictions)

## 2. タスクリストと実行中タスクビューの区別

`interactive-mode` の「タスクリスト」節と `Ctrl+T` の説明が刷新され、**タスクリストが「Claude の ToDo チェックリスト」**であることが明確になりました。これは Claude が多段作業を計画するために作成した項目（保留中・進行中・完了のインジケータ付き）で、**実行中のシェルやサブエージェントを見る `/tasks` のバックグラウンドタスクビューとは別物**です。`Ctrl+T` はこの ToDo チェックリストの表示切り替えで、Claude がまだチェックリスト項目を作っていない場合はトグルしても表示は変わりません。

キーボードショートカット表と、グローバルアクション表の `app:toggleTodos`（`Ctrl+T`）の説明も同様に「Claude の ToDo チェックリストの表示切り替え。これは `/tasks` のバックグラウンドタスクビューではない」と補足されています。

- [インタラクティブモード（タスクリスト） - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/interactive-mode#task-list)
- [Interactive mode (Task list) - Claude Code Docs (English)](https://code.claude.com/docs/en/interactive-mode#task-list)

## 軽微な更新

<!-- light:minor-updates:start -->
今回の軽微な更新は、v2.1.198／v2.1.199 の 2 リリースに伴う既存ページへの追記・修正と多数のバグ修正が中心です。以下に分類して整理します（複数リリースを含むため、識別が必要な項目にはバージョンを併記します）。

**新機能**

- `/dataviz` スキルが追加され、チャート・ダッシュボード設計のガイダンスと実行可能なカラーパレット検証ツールを提供するようになった（v2.1.198）。
- Claude apps ゲートウェイのアップストリームプロバイダーに「Claude Platform on AWS」（`anthropicAws`）が追加され、model-not-found 応答でフェイルオーバーチェーンが次へ進むようになった（v2.1.198）。ドキュメントマップの `claude-apps-gateway-config`（`upstreams`）にも該当エントリが追加されている。

**機能改善**

- サブエージェントの既定バックグラウンド化、Explore のモデル継承、拡張思考設定の継承（詳細はハイライト 2 参照）。
- ベストプラクティスの記述が複数明確化された。コンパクション指示を書く `CLAUDE.md` が「プロジェクトルートの `CLAUDE.md`」であること、拡張思考予算を下げる `MAX_THINKING_TOKENS` が環境変数であること、`filter-test-output` フックスクリプトの設置手順（`mkdir`／`chmod +x`）などが追記された — [English](https://code.claude.com/docs/en/best-practices)。
- `dontAsk` モードが有効な間、ステータスバーに `⏵⏵ don't ask on` を表示する旨が追記された — [English](https://code.claude.com/docs/en/permissions#allow-only-pre-approved-tools-with-dontask-mode)。
- Agent SDK ドキュメントで、自動メモリが専用ツールではなく `Write`／`Edit` ツールで書き込まれる旨や、チェックポイント例・SDK サンプルの実行前提が明確化された — [English](https://code.claude.com/docs/en/agent-sdk/typescript)。
- `CLAUDE_CODE_RETRY_WATCHDOG` の既定リトライ回数引き上げ・`CLAUDE_CODE_MAX_RETRIES` の上限撤廃（詳細はハイライト 5 参照）に加え、サブスクライバー向けに使用制限と無関係な一時的 429 を自動バックオフ再試行するようになった（v2.1.199）。
- API リトライの UX が改善され、2 回目試行後にエラー理由を表示し、API 過負荷時はスピナーのヒントをステータスページへのリンクに置き換えるようになった（v2.1.198）。
- コードブロック・差分・ファイルプレビューの構文ハイライトが highlight.js 11 へのアップグレードで改善された（v2.1.198）。
- `/login` が `claude agents` ビューから「利用不可」と表示する代わりにサインインダイアログを開くようになり、フォーカスモードでは 1 ターン内で起動したサブエージェントがその活動サマリに表示され、Mac から SSH 接続時のキーボードショートカットヒントが alt/super の代わりに opt/cmd を表示するようになった（v2.1.198）。
- そのほか、手順・前提を明確化する小規模な更新が複数ページで行われた。エージェントビューの「既存セッションの取り込み」手順とバックグラウンドサービス起動時のメッセージ（`agent-view`）、Linux 版デスクトップのサインイン方法（`desktop-linux`）、プラグインクイックスタートのディレクトリ配置（`plugins-quickstart`）など。

**バグ修正**

- 応答途中のネットワーク瞬断でターンが中断される不具合を修正し、ECONNRESET 等の一時エラーをバックオフ再試行するようにした（v2.1.198）。
- エージェントチームで、API エラーで死んだチームメイトがリードに「failed」を報告し、行き詰まったチームメイトへのメッセージが即時リトライを促すように修正（v2.1.198）。
- web／desktop／VS Code のタスクパネルが、完了後や再開後も「Running」のまま止まる不具合を修正（v2.1.198）。
- `claude --bg` を `--print`／`-p` と併用すると接続不能なセッションが黙って作られる不具合を、競合フラグの起動時拒否で修正（v2.1.198）。
- Claude Platform on AWS／Mantle セッションが STS トークン失効時に「Please run /login」で行き詰まる不具合を、`awsAuthRefresh` の自動実行で修正（v2.1.198）。
- macOS のバックグラウンドエージェントセッションでローカルネットワークホストへ「no route to host」になる不具合を、Local Network entitlements の宣言で修正（v2.1.198）。
- プランモードで開始したセッションが読み取り専用ツール呼び出しを自動許可しない不具合、および `.claude/rules/` の条件付きルールがシンボリックリンク経由のパスでロードされない不具合を修正（v2.1.198）。
- Linux のバックグラウンドエージェントデーモンが、不正終了後の破損ワーカー記録により約 50 秒ごとに自身と全エージェントを kill する不具合を修正（v2.1.199）。
- `claude stop` がバックグラウンドエージェントの再生成と競合して無効化される不具合、およびメモリ不足マシンでのバックグラウンドセッションが汎用エラーではなく低メモリを示すよう修正（v2.1.199）。
- `SessionStart`／`Setup`／`SubagentStart` フックが終了コード 2 で stderr を隠す不具合を修正し、エラーをトランスクリプトに表示するようにした（v2.1.199）。
- `SendMessage` が再生成で前のエージェント名を再利用した際に誤ルーティングする不具合を、不一致検出と再指定要求で修正（v2.1.199）。
- そのほか、macOS SSH でのコールドスタート失敗、バックグラウンドジョブ進捗の停滞、アイドルサブエージェントのパネル消失、破損 config リセット時のバックアップなど、多数の修正が含まれる（v2.1.198／v2.1.199）。

**その他**

- エラーリファレンス（`errors`）に新しいエラー節が複数追加された（応答が不完全な可能性、API エラーによるエージェントの早期終了、AWS 認証情報の失効・無効、AWS 認証失敗、`--bg` と `--print` の競合など）。いずれも changelog／ドキュメントマップ先行で、原文全文（llms-full）・日本語ページともに未反映のため参考リンクは省略する。
- ドキュメントマップに、本文が llms-full 未収録の新見出しが複数追加された（`chrome` の「Browser tools in plan mode」、`mcp` の「Tool input schemas with a root-level combinator」「Require approval for a specific tool」、`sandboxing` の「Mask environment variables」、`model-config` の「Organization default model」「Organization effort limits」、`sub-agents` の「API errors in subagents」など）。
- `llms.txt` のページ説明が更新された（`artifacts` の公開先を「claude.ai」に明記、`chrome` から「(beta)」を削除、ゲートウェイ系ページに「Claude Platform on AWS」を併記）。
<!-- light:minor-updates:end -->

## 新着情報

<!-- light:whats-new:start -->
今回、週刊ダイジェスト「新着情報」（`whats-new/`）ページの更新はありません。ドキュメントマップにも `whats-new/` の新規エントリ追加はありませんでした。
<!-- light:whats-new:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-07-01.md](./archives/latest/2026-07-01.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-07-01.md](./archives/latest-detail/2026-07-01.md)

<!--
base_commit: 0479bd37959b8b8592cf2b7e35df021189becc68
head_commit: 331621b2d46b6f0f04b5dc7868b469f76a64d0a4
generated_at_full: 2026-07-03T15:07:28+09:00
-->
