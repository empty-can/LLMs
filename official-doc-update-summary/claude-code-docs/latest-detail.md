---
対象期間: 2026年07月14日 〜 2026年07月15日
作成日: 2026-07-15
---

# Claude Code 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
今回の対象期間は、changelog にリリース v2.1.211（多数の修正・改善を含む）が加わり、reference/ガイド系ページに MCP コネクタとゲートウェイまわりの新機能が集中して追記された回です。新規ページはありませんが、アーティファクトが公開後もライブデータを取得できるようになったこと、組織が claude.ai コネクタのツール単位に承認/ブロックを課せるようになったことなど、権限とデータの流れに関わる中核的な追加が目立ちます。

主要なものを以下に挙げます。

1. アーティファクトが、閲覧のたびに MCP コネクタを呼んでライブデータを表示できるようになった（各閲覧者自身の接続を使用）
2. 組織が claude.ai コネクタのツールを単位ごとに「承認要求（ask）」または「ブロック」に設定でき、Claude Code がローカルで全権限モードにわたって強制するようになった
3. ゲートウェイ経路の外へ出る非必須トラフィック（更新チェック・テレメトリ等）を一括で止める `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` が明文化された
4. 依存関係だけを持つプラグインマニフェストで、キュレーション済みのプラグイン集合を 1 回のインストールで配れるようになった
5. テレメトリの記述がメトリクスとエラーレポートに再編され、エラーレポートは Pro/Max・v2.1.198 以降・Claude API 直結の条件下でのみ有効と明記された
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**アーティファクトが MCP コネクタでライブデータを取得**](#1-アーティファクトが-mcp-コネクタでライブデータを取得):  
  アーティファクト（claude.ai 上のプライベートページ）が、ビルド時のスナップショットではなく、閲覧されるたびに claude.ai の MCP コネクタを呼んで現在のデータを表示できるようになった。コネクタ呼び出しは各閲覧者自身のアカウント接続を通り、閲覧者ごとに見えるデータが変わる。Pro/Max/Team/Enterprise、v2.1.209 以降が必要。
2. [**コネクタツールに組織が承認要求とブロックを強制**](#2-コネクタツールに組織が承認要求とブロックを強制):  
  組織は claude.ai コネクタのツール単位に制御を設定でき、Claude Code は起動時に読み込んでローカルで強制する。`ask` のツールは `acceptEdits`・`auto`・`bypassPermissions` でも毎回プロンプトを出し「今後聞かない」を提供せず、allow ルールでもスキップされない（`dontAsk` では拒否）。`blocked` のツールは Claude に見える前に除外される。v2.1.129 以降が必要。
3. [**ゲートウェイ経路外の非必須トラフィックを止める設定**](#3-ゲートウェイ経路外の非必須トラフィックを止める設定):  
  ゲートウェイはモデルリクエストを運ぶが、Claude Code はバージョンチェック・テレメトリ・エラーレポート・リリースノートなどの非必須トラフィックを Anthropic や GitHub 等へ別途送る。egress をゲートウェイのみに絞ったネットワーク向けに、`CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1` でこれらを止められることが llm-gateway-connect に新設された。
4. [**チーム向けにプラグインをバンドル**](#4-チーム向けにプラグインをバンドル):  
  プラグインマニフェストは必須の `name` と `dependencies` 配列だけでも成立し、インストールすると全依存を引き込むため、キュレーション済みのプラグイン集合を 1 回のインストールで配布する手段になる。ロール別バンドルを内部マーケットプレイスで配り、`enabledPlugins`（managed 設定）で組織展開できる。
5. [**テレメトリ再編とエラーレポートの Pro と Max 限定化**](#5-テレメトリ再編とエラーレポートの-pro-と-max-限定化):  
  data-usage のテレメトリ記述が「メトリクス」と「エラーレポート」に分割され、それぞれ `DISABLE_TELEMETRY`／`DISABLE_ERROR_REPORTING` で個別無効化できることが整理された。エラーレポートは Pro/Max サインイン・v2.1.198 以降・Claude API 直結・ZDR/HIPAA 契約なし、の全条件を満たす場合にのみ有効と明記された。
<!-- light:highlight-list:end -->

## 1. アーティファクトが MCP コネクタでライブデータを取得

アーティファクトは、セッションが構築した時点のデータを固定したページでしたが、公開後も外部データを取得できるようになりました。アーティファクトは、誰かがページを開くたびに [MCP コネクタ](https://code.claude.com/docs/en/mcp#use-mcp-servers-from-claude-ai)を呼び、そのときの現在値を表示できます。コネクタ呼び出しは Pro/Max/Team/Enterprise で利用でき、Claude Code v2.1.209 以降が必要です。それ以前のバージョンでは、従来どおりビルド時に集めたデータで公開されます。コネクタ連携ページを作るには、プロンプトでコネクタ名と欲しいデータを指定します（例:「GitHub コネクタからオープン PR のライブ一覧を取得するダッシュボードアーティファクトを作って」）。Claude は公開時にページが呼べるコネクタを宣言し、ページはその宣言外のコネクタを呼べません。使えるのは自分の claude.ai アカウントのコネクタだけで、`.mcp.json` などローカルの MCP サーバーはビルド時にデータを供給できますが、公開後のページからは呼べません。

閲覧者側の重要な性質として、公開ページがコネクタを呼ぶとき、その呼び出しは**公開者ではなく閲覧者自身のアカウント**を使います。二人が同じダッシュボードを開いても、各自のアカウントがアクセスできる範囲に応じて見えるデータが異なり、ページが誰かの認証情報を見ることはありません（claude.ai がページの代わりに呼び出す）。各閲覧者は最初のコネクタ呼び出しの前に許可を求められ、拒否した閲覧者や必要なコネクタを接続していない閲覧者は、ライブ部分のないページを見ます。副作用を持つコネクタツール（メッセージ投稿や issue 更新など）を呼ぶコントロールも、それを選んだ人のアカウントを通ります。共有時は各ライブ部分に必要なコネクタ名を示すフォールバックメッセージを入れておくと、未接続の閲覧者が何を接続すべきか分かります。コネクタを呼ぶアーティファクトはどのプランでも公開リンクにできず、Team/Enterprise では非公開または組織内共有に、Pro/Max では作成者のみに留まります。

あわせて「ページの制約」表の「外部リクエストなし」「バックエンドなし」の記述にコネクタ呼び出しが唯一の例外として追記され、管理者向けには claude.ai 管理設定に**アーティファクトコネクタ専用のトグル**（`Enable artifact connectors`。アーティファクト自体の有効/無効とは別）が加わりました。ライブ部分が空になる場合の切り分け（閲覧者が未接続／許可を拒否／組織でコネクタ呼び出しが無効）も新設されています。

- [Share session output as an artifact (Pull live data with MCP connectors) - Claude Code Docs (English)](https://code.claude.com/docs/en/artifacts#pull-live-data-with-mcp-connectors)

## 2. コネクタツールに組織が承認要求とブロックを強制

claude.ai コネクタのツールに、組織がツール単位の制御をかけられるようになりました。Claude Code は起動時にこの設定を読み込み、ローカルで強制します。どのツールにどの設定が効いているかは `/mcp` で確認できます。ツールが `ask` に設定されている場合、Claude Code は毎回「Your organization requires approval for this tool」という理由でプロンプトを出します。このプロンプトは `acceptEdits`・`auto`・`bypassPermissions` の各[日本語](https://code.claude.com/docs/ja/permissions#permission-modes) / [権限モード](https://code.claude.com/docs/en/permissions#permission-modes)でも表示され、選択を記憶するオプションは提供されず、ツールに一致する allow ルールでもスキップされません。プロンプトを一切出さない `dontAsk` モードでは、代わりにその呼び出しを拒否します。ツールが `blocked` に設定されている場合、Claude Code はそのツールを Claude が見る前に除外するため、ツール一覧に現れません。

この制御の強制には Claude Code v2.1.129 以降が必要で、それ以前のバージョンは設定を無視して標準の権限フローを適用します。この挙動は権限・権限モード・フック・サンドボックス・スケジュールタスク・ヘッドレス・Agent SDK など多数のページに横断的に反映され、いずれも「コネクタツールの `ask` と、MCP ツールの `requiresUserInteraction` 指定は、フックが `allow` を返してもプロンプトを出す」という一貫した記述になっています（大幅更新 6 参照）。

- [Connect Claude Code to tools with MCP (Organization controls on connector tools) - Claude Code Docs (English)](https://code.claude.com/docs/en/mcp#organization-controls-on-connector-tools)

## 3. ゲートウェイ経路外の非必須トラフィックを止める設定

LLM ゲートウェイ接続ページに、ゲートウェイ経路の外へ出るトラフィックを止める節が新設されました。ゲートウェイはモデルリクエストを運びますが、Claude Code はそれとは別に、バージョンチェック・テレメトリ・エラーレポート・リリースノートなどの非必須なバックグラウンド通信を Anthropic や GitHub のような第三者サービスへ送ります。egress をゲートウェイのみに許可したネットワークでは、これらのリクエストが失敗し、egress 監視でブロックされた接続として現れます。このトラフィックを止めるには、ゲートウェイ変数と同じシェルエクスポートまたは設定ファイルの `env` ブロックで `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1` を設定します。

設定すると次の効果と制限があります。自動更新が無効になるため、パッケージマネージャや managed 配布など別の更新経路を用意する必要があります。[日本語](https://code.claude.com/docs/ja/fast-mode) / [fast mode](https://code.claude.com/docs/en/fast-mode) の可用性チェックが抑制され、以前のチェックで有効化済みでない限り `/fast` は利用不可と表示します。ゲートウェイ自身に問い合わせる[ゲートウェイモデル検出](https://code.claude.com/docs/en/llm-gateway-connect#add-gateway-models-to-the-model-picker)も止まり、既検出モデルはローカルキャッシュから使えますが一覧は更新されません。WebFetch のドメイン安全性チェックは影響を受けず引き続き `api.anthropic.com` を呼ぶため、そのホストがブロックされる場合は `skipWebFetchPreflight: true` で別途無効化します。

- [Connect Claude Code to an LLM gateway (Turn off traffic outside the gateway path) - Claude Code Docs (English)](https://code.claude.com/docs/en/llm-gateway-connect#turn-off-traffic-outside-the-gateway-path)

## 4. チーム向けにプラグインをバンドル

プラグイン依存関係ページに、依存だけを束ねるプラグインの作り方が加わりました。プラグインマニフェストは、必須の `name` のほかに `dependencies` 配列だけを持つ形でも成立します。それをインストールすると全依存が引き込まれるため、キュレーション済みのプラグイン集合を 1 回のインストールで配布する手段になります。たとえばプラットフォームチームが内部マーケットプレイスにロール別バンドル（`backend-standard` など、`secrets-vault`・`deploy-kit`・`db-migrate`・`oncall-runbook` を依存に持つ）を公開すれば、エンジニアは各ツールを個別に入れる代わりに `claude plugin install` を 1 回実行するだけで済みます。

後からツールを標準セットに足すには、依存を追加した新バージョンを公開します。非 Anthropic マーケットプレイスは自動更新が既定オフなので、エンジニアは `/plugin` でそのマーケットプレイスの自動更新を有効にするか、`claude plugin update backend-standard` の後 `/reload-plugins` で追加依存を入れます。組織全体へ展開するには、バンドルプラグインを [managed 設定](https://code.claude.com/docs/en/settings#enabledplugins)の `enabledPlugins` に加えます。

- [Constrain plugin dependency versions (Bundle plugins for a team) - Claude Code Docs (English)](https://code.claude.com/docs/en/plugin-dependencies#bundle-plugins-for-a-team)

## 5. テレメトリ再編とエラーレポートの Pro と Max 限定化

data-usage の「テレメトリサービス」の記述が、送られる 2 種類の運用テレメトリ（使用メトリクスとエラーレポート）に整理され、それぞれ個別に無効化できることが明確化されました。**メトリクス**はレイテンシ・信頼性・使用パターンで、Anthropic と第三者ロギング基盤へ TLS で送られ、コード・プロンプト・ファイルパスを含みません（`DISABLE_TELEMETRY=1` でオプトアウト）。**エラーレポート**は Claude Code 内部のエラーメッセージとスタックトレースで、第三者のエラートラッキングサービスへ TLS で送られ、既知の秘密・ファイルパス・メールアドレス等のパターンはマシンを出る前に伏せられます（`DISABLE_ERROR_REPORTING=1` でオプトアウト）。

重要な条件として、エラーレポートは次のすべてを満たす場合にのみ有効です: Pro または Max サブスクリプションでサインインしている／Claude Code v2.1.198 以降を実行している／Claude API に直結している／組織が ZDR や HIPAA 契約を持たない。API プロバイダー別のデフォルト動作表でも、エラーレポートの Claude API 列が「Pro/Max サインイン・v2.1.198 以降でオン、それ以外はオフ」に更新され、Sentry という固有名の記載がメトリクス/エラーレポートの一般名に置き換えられました。

- [Data usage (Telemetry services) - Claude Code Docs (English)](https://code.claude.com/docs/en/data-usage#telemetry-services)

## 新規追加されたページ

<!-- light:new-pages:start -->
今回の対象期間では、新規に追加されたリファレンス・ガイドページはありません。
<!-- light:new-pages:end -->

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
- [**アーティファクト**](#1-アーティファクト) ([日本語](https://code.claude.com/docs/ja/artifacts) / [English](https://code.claude.com/docs/en/artifacts)):  
  MCP コネクタでのライブデータ取得（ハイライト 1 参照）が中心。あわせて「アーティファクトとは何でないか」「ページの制約」表がコネクタ呼び出しを唯一の外部データ経路として書き直され、管理者向けにアーティファクトコネクタ専用トグルが加わった。
- [**MCP**](#2-mcp) ([日本語](https://code.claude.com/docs/ja/mcp) / [English](https://code.claude.com/docs/en/mcp)):  
  コネクタツールへの組織制御（ハイライト 2 参照）に加え、MCP ツール出力が既定で 25,000 トークンに制限されるようになり（従来は 10,000 トークン超で警告のみ）、ツール検索の対応モデルが明確化された（Haiku 4.5 が `tool_reference` に対応、`CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS` はツール検索を強制的にオフにする）。
- [**LLM ゲートウェイ接続**](#3-llm-ゲートウェイ接続) ([日本語](https://code.claude.com/docs/ja/llm-gateway-connect) / [English](https://code.claude.com/docs/en/llm-gateway-connect)):  
  非必須トラフィックの停止（ハイライト 3 参照）に加え、デスクトップアプリが「サードパーティ推論設定」をアプリ内フォームからローカルに設定できるようになった（Developer メニューの Configure Third-Party Inference。管理者配布があればそちらが優先し読み取り専用になる）。
- [**データ使用**](#4-データ使用) ([日本語](https://code.claude.com/docs/ja/data-usage) / [English](https://code.claude.com/docs/en/data-usage)):  
  テレメトリ記述の再編とエラーレポートの Pro/Max・v2.1.198 以降限定化（ハイライト 5 参照）。
- [**機能の可用性**](#5-機能の可用性) ([日本語](https://code.claude.com/docs/ja/feature-availability) / [English](https://code.claude.com/docs/en/feature-availability)):  
  「すべてのプロバイダーで同一」という記述が「プロバイダー固有の差異あり」に緩められ、MCP サーバー・サブエージェント・コマンドの差異が明記された。`/design-sync`・`/radio` が 3P プロバイダーで不可、`/voice` が claude.ai 必須。Claude Platform on AWS では `/loop` の自己ペーシングが不可（明示的間隔のみ）に変わった。
- [**権限**](#6-権限) ([日本語](https://code.claude.com/docs/ja/permissions) / [English](https://code.claude.com/docs/en/permissions)):  
  コネクタツールの `ask` と MCP ツールの `requiresUserInteraction` が全権限モード・フック `allow`・`--dangerously-skip-permissions` を貫いてプロンプトを出す（`dontAsk` では拒否）ことが横断的に記述され、macOS のバックグラウンドセッションが保護フォルダへのアクセスを別途要求する挙動が追記された。
<!-- light:updated-pages:end -->

## 1. アーティファクト

アーティファクトページの中心的な追加は、公開後のページが閲覧のたびに MCP コネクタを呼んでライブデータを表示できるようになったことです（ハイライト 1 参照）。これに伴い「アーティファクトとは何でないか」の説明が、「表示時に外部データを得る唯一の経路はコネクタ呼び出し」と書き直され、「ページの制約」表の「外部リクエストなし」「バックエンドなし」の各行にも、コネクタ呼び出しだけが例外（ページが claude.ai に渡し、claude.ai がネットワーク呼び出しを行う）である旨が加わりました。

管理者向けには、「アーティファクトコネクタを制御する」節が新設され、アーティファクト自体の有効/無効トグルとは別に `Enable artifact connectors` トグルが `Settings > Capabilities` に置かれることが説明されました（claude.ai の会話で作られたアーティファクトのコネクタ呼び出しも同じトグルが支配するため、`Settings > Claude Code` ではなく `Settings > Capabilities` にある）。関連リソースの MCP への言及も「ビルド中にライブデータを取得」から「ページ構築中にデータを取得」に微修正されています。

- [Share session output as an artifact (Pull live data with MCP connectors) - Claude Code Docs (English)](https://code.claude.com/docs/en/artifacts#pull-live-data-with-mcp-connectors)

## 2. MCP

MCP ページには、組織によるコネクタツール制御（ハイライト 2 参照）のほか、出力上限とツール検索の挙動が加わりました。**MCP 出力制限**は、従来「10,000 トークン超で警告」だけでしたが、既定で 25,000 トークンに出力を制限するよう変わりました。上限を上げるには `MAX_MCP_OUTPUT_TOKENS` を設定します（警告閾値は固定）。**ツール検索**では、対応モデルの記述が更新され、`tool_reference` ブロックをサポートするモデルとして Claude Sonnet 4.5・Haiku 4.5・Opus 4.5 以降が明示されました（従来「Haiku モデルは非対応」とされていた点が変わりました）。あわせて、`CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS` を設定するとツール検索はオフのままになり、`ENABLE_TOOL_SEARCH` でも上書きできない（`defer_loading`／`tool_reference` に必要なベータヘッダーが外れるため）ことが加わりました。

このほか、claude.ai の MCP サーバーが[コネクタ](https://claude.com/docs/connectors)と呼ばれることの明記など、細かな追記が入っています。

- [Connect Claude Code to tools with MCP (Organization controls on connector tools) - Claude Code Docs (English)](https://code.claude.com/docs/en/mcp#organization-controls-on-connector-tools)
- [Connect Claude Code to tools with MCP (MCP output limits and warnings) - Claude Code Docs (English)](https://code.claude.com/docs/en/mcp#mcp-output-limits-and-warnings)

## 3. LLM ゲートウェイ接続

LLM ゲートウェイ接続ページの主変更は、非必須トラフィックを止める `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` の新設（ハイライト 3 参照）です。あわせて、デスクトップアプリの「サードパーティ推論設定」の入手経路が広がりました。従来は管理者配布の設定からのみゲートウェイルーティングを読み取っていましたが、管理者配布がないデバイスでは、Help → Troubleshooting → Enable Developer Mode でアプリを再起動して Developer メニューを出し、Developer → Configure Third-Party Inference でゲートウェイのベース URL を入力できるようになりました。管理者配布の設定があればそちらが優先し、このフォームは読み取り専用になります。

導入部・追加設定の案内文も、これらの設定を「管理者の指示に加えてネットワークの egress ルールでも設定しうる」と補足する形に更新されています。

- [Connect Claude Code to an LLM gateway (Turn off traffic outside the gateway path) - Claude Code Docs (English)](https://code.claude.com/docs/en/llm-gateway-connect#turn-off-traffic-outside-the-gateway-path)
- [Connect Claude Code to an LLM gateway (Desktop app) - Claude Code Docs (English)](https://code.claude.com/docs/en/llm-gateway-connect#desktop-app)

## 4. データ使用

データ使用ページの中心的な変更は、テレメトリ記述の再編とエラーレポートの有効条件の明記（ハイライト 5 参照）です。「テレメトリサービス」節がメトリクスとエラーレポートの 2 本立てに書き直され、API プロバイダー別のデフォルト動作表でもエラーレポートの Claude API 列が条件付き（Pro/Max・v2.1.198 以降でオン）に更新されました。あわせて、Remote Control が ZDR 有効組織で自動無効化される機能一覧に加わっている点（前回サマリのハイライト参照）と整合する形で、`data-access` まわりの記述にも Claude Platform on AWS などの追記が入っています。

- [Data usage (Telemetry services) - Claude Code Docs (English)](https://code.claude.com/docs/en/data-usage#telemetry-services)

## 5. 機能の可用性

機能の可用性ページは、「Claude Code の CLI とローカルで動くものはすべてのプロバイダーで**同一に**動く」という断定が「動く」に緩められ、プロバイダー固有の差異を明示する方向で整理されました。すべてのプロバイダーで使える機能のうち 3 つに差異があるとして、MCP サーバー（claude.ai コネクタは claude.ai サブスクリプションがアクティブな認証のときだけロードされ、ツール検索は Google Cloud の Agent Platform 等で既定オフ）、サブエージェント（組み込み Explore は Claude API では Opus に上限、他プロバイダーではメイン会話のモデルを継承）、コマンド（`/design-sync` と `/radio` は Amazon Bedrock・Google Cloud の Agent Platform・Microsoft Foundry・Claude Platform on AWS で不可、`/voice` は claude.ai 必須）が挙げられました。

各プロバイダーの「Summary by provider」タブにも `/design-sync` と `/radio` の不可が追記され、特に Claude Platform on AWS では `/loop` の自己ペーシングが不可（明示的間隔のみ、引数なし `/loop` は使い方表示）に変わりました。脚注 3 の該当プロバイダー一覧にも Claude Platform on AWS が加わっています。プラン別可用性表では Compliance API のリンク先 URL が更新されました。

- [Feature availability (Features available on every provider) - Claude Code Docs (English)](https://code.claude.com/docs/en/feature-availability#features-available-on-every-provider)

## 6. 権限

権限ページでは、コネクタツールと対話必須 MCP ツールの扱いが各所に一貫して追記されました。権限モード表の `dontAsk` 行には、`AskUserQuestion`・組織が `ask` にしたコネクタツール・`requiresUserInteraction` 指定の MCP ツールは allow していても拒否されることが、`bypassPermissions` 行にはこれらが依然プロンプトを出すことが加わりました。MCP ルールの節にも、組織が `ask` にしたコネクタツールは allow ルールが効かず `auto`/`bypassPermissions` でも毎回プロンプトが出る（`dontAsk` では拒否）こと、コネクタツールは `mcp__claude_ai_<server>__<tool>` として現れることが明記されました。PreToolUse フックが `allow` を返しても、これらのツールのプロンプトは抑制できません。

作業ディレクトリの節には、macOS のバックグラウンドセッションが `~/Desktop`・`~/Documents`・`~/Downloads` のような保護フォルダへのアクセスを、ターミナルとは別にセッションホストが要求する挙動と、`Operation not permitted` で読み取りが失敗する場合の対処への参照が加わりました。

- [日本語](https://code.claude.com/docs/ja/permissions#permission-modes) / [Configure permissions (Permission modes) - Claude Code Docs (English)](https://code.claude.com/docs/en/permissions#permission-modes)

## 軽微な更新

<!-- light:minor-updates:start -->
今回の軽微な更新は、changelog に追加されたリリース **v2.1.211**（2026年07月15日）の内容と、上記大幅更新に含まれない各ページの小規模な改訂です。changelog 由来の項目は 1 リリースのみのため、原則としてバージョン併記は省きます。

**新機能**

- `--forward-subagent-text` フラグと `CLAUDE_CODE_FORWARD_SUBAGENT_TEXT` 環境変数が追加され、stream-json 出力にサブエージェントのテキストと thinking を含められるようになった。
- managed 設定 `disableBrowserExternalNavigation` が追加された。Browser ペインの外部ブラウジングを完全に止め、組織の allowlist 上のサイトも含めてブロックする（localhost 開発サーバーとファイルプレビューは動作。値は JSON ブール値 `true` のみ有効で文字列 `"true"` は無視）。ユーザーにも Claude にも外部サイトを見せたくない場合に、`browserExternalPageTools`（Claude のツールだけ止める）と使い分ける。 — [日本語](https://code.claude.com/docs/ja/settings#available-settings) / [English](https://code.claude.com/docs/en/settings#available-settings)
- managed 設定 `pluginSuggestionMarketplaces` が追加され、どのマーケットプレイスのプラグインを文脈的インストール提案に出せるか allowlist できるようになった。 — [English](https://code.claude.com/docs/en/plugin-marketplaces#managed-marketplace-restrictions)
- GitHub の `owner/repo` 短縮ソースは既定で SSH でクローンされるが、`CLAUDE_CODE_PLUGIN_PREFER_HTTPS=1` で HTTPS クローンに切り替えられるようになった。 — [English](https://code.claude.com/docs/en/plugin-marketplaces#private-repositories)
- ログイン時のプロンプトで「3rd-party platform」を選ぶと、Bedrock と Vertex AI 向けの対話セットアップウィザードが起動するようになった（認証ページに追記）。あわせて managed 設定 `forceLoginMethod`/`forceLoginOrgUUID` が設定されている場合、`ANTHROPIC_API_KEY`・`ANTHROPIC_AUTH_TOKEN`・`apiKeyHelper` で認証したセッションは起動時にブロックされることが明記された（クラウドプロバイダーのセッションは非対象）。 — [日本語](https://code.claude.com/docs/ja/authentication) / [English](https://code.claude.com/docs/en/authentication)

**機能改善**

- `UserPromptSubmit` フックで文脈を注入する `additionalContext` は `hookSpecificOutput` の内側にネストする必要があり、トップレベルに置くと黙って無視されることが、例つきで明記された。あわせて `"Edit|Write"` のようなマッチャーは v2.1.191 以降カンマ区切り `"Edit, Write"` でも同義になった。 — [日本語](https://code.claude.com/docs/ja/hooks-guide) / [English](https://code.claude.com/docs/en/hooks-guide)
- サンドボックスの読み取りルールが重なった場合、より限定的なパスが勝つことが表で示された（`denyRead: ["~/"]` + `allowRead: ["~/projects"]` は projects だけ読める、`allowRead: ["~/"]` + `denyRead: ["~/.env"]` は .env だけブロックのまま）。 — [日本語](https://code.claude.com/docs/ja/sandboxing) / [English](https://code.claude.com/docs/en/sandboxing)
- シェルで `CLAUDE_CODE_USE_*` プロバイダー変数や非既定の `ANTHROPIC_BASE_URL` をエクスポートすると、server-managed 設定のフェッチがスキップされ、その `env` ブロックではエクスポートを打ち消せない（フェッチ前に適格性が判定されるため）ことが明記された。復旧はシェルからエクスポートを外すか、ユーザー設定 `env` で当該変数を `""` にする。 — [日本語](https://code.claude.com/docs/ja/server-managed-settings) / [English](https://code.claude.com/docs/en/server-managed-settings)
- Web の Claude Code で、`GH_TOKEN`/`GITHUB_TOKEN` を自分で設定するとコンテナへそのまま渡り、未設定だと両変数がプレースホルダ `proxy-injected` になり GitHub プロキシが実認証情報を差し込む挙動が明記された（`GITHUB_TOKEN` を直接読むスクリプトはプレースホルダを受け取る）。 — [日本語](https://code.claude.com/docs/ja/claude-code-on-the-web) / [English](https://code.claude.com/docs/en/claude-code-on-the-web)
- `/setup-bedrock` はモデルピン工程を現在のピンから始め、`~/.claude/settings.json`（`CLAUDE_CONFIG_DIR` 設定時はそちら）へ書き込むことが明記された。SSO プロファイル手順のプレースホルダ表記も整理された。 — [日本語](https://code.claude.com/docs/ja/amazon-bedrock) / [English](https://code.claude.com/docs/en/amazon-bedrock)
- managed 設定に検証失敗エントリがある場合、`/doctor` でソースファイルとフィールド付きで除去されたエントリを一覧できるようになった。 — [English](https://code.claude.com/docs/en/settings#invalid-entries-in-managed-settings)
- Agent SDK のツール検索リファレンスに「Tool output exceeds maximum allowed tokens」のトラブルシューティング節が追加された。 — [日本語](https://code.claude.com/docs/ja/agent-sdk/tool-search) / [English](https://code.claude.com/docs/en/agent-sdk/tool-search)
- Agent SDK のコスト追跡の説明で、最終的な output トークン表示はトップレベルのエージェントループ分で、サブエージェントのトークンは含まれないことが明記された。 — [日本語](https://code.claude.com/docs/ja/agent-sdk/cost-tracking) / [English](https://code.claude.com/docs/en/agent-sdk/cost-tracking)
- managed-mcp の allowlist/denylist が `--mcp-config` CLI フラグで渡したサーバーにも適用される（`--strict-mcp-config` は読み込む設定ファイルを絞るだけで、どちらのリストもバイパスしない）ことが明記され、`allowedMcpServers`/`deniedMcpServers` 表にはエントリがスキーマ検証に失敗した場合の挙動（settings の Invalid entries）への参照が加わった。 — [日本語](https://code.claude.com/docs/ja/managed-mcp) / [English](https://code.claude.com/docs/en/managed-mcp)
- auto モード設定で、`environment`/`allow`/`soft_deny`/`hard_deny` を `"$defaults"` なしで上書きした場合に失われる組み込みルールの内訳が整理され、auto-mode bypass ルールが `soft_deny` 側に、データ持ち出しルールのみが `hard_deny` 側に明記された。 — [日本語](https://code.claude.com/docs/ja/auto-mode-config) / [English](https://code.claude.com/docs/en/auto-mode-config)
- Claude in Chrome で、利用可能なブラウザツールの一覧は `/mcp` → `claude-in-chrome` → **View tools** で見ることが案内され、最初のブラウザ操作で `claude-in-chrome` スキルの使用許可を求める旨が追記された。 — [日本語](https://code.claude.com/docs/ja/chrome) / [English](https://code.claude.com/docs/en/chrome)
- セッション/週次の使用枠は同時に消費されるため、大きなワークフローのファンアウトのような一時的な大量利用が、セッション枠のリセット前に週次枠を使い切りうることが追記された。 — [English](https://code.claude.com/docs/en/errors#usage-limits)
- プラグインマーケットプレイスの更新で、ブランチ/タグ `ref` で追加したマーケットプレイスはその ref の最新コミットに更新される（リポジトリの既定ブランチではない）ことが明記された。 — [English](https://code.claude.com/docs/en/plugin-marketplaces#plugin-marketplace-update)

**バグ修正**

- Bedrock/Vertex/Mantle/Foundry で、末尾のシステムコンテキストブロックを毎リクエスト新規 input トークンとして課金していた prompt-caching のリグレッションを修正。
- チャットチャネルへ中継される権限プレビューが、双方向オーバーライド・ゼロ幅・類似の引用文字を無害化しておらず、ツール入力が承認メッセージを視覚的に改変できた問題を修正。
- auto モードが、サンドボックス外 Bash に対する PreToolUse フックの `ask` 判定を上書きしていた問題を修正（フックの `ask` が最低でもプロンプトになる）。
- スリープ復帰後、多数のセッションが 1 つの認証情報ストアを共有していると並行セッションが一斉ログアウトする問題を修正。
- アイドルな Web セッション復帰後にプラグイン MCP サーバーが再接続せず、次のメッセージまで MCP 呼び出しが失敗し続ける問題を修正。
- Vertex/Bedrock で、モデルを明示設定していても起動時に既定 Opus を試して余計なフォールバック通知を出す問題を修正。
- 明示的なモデル上書きで起動したサブエージェントが、resume やフォローアップで親のモデルに戻る問題を修正。
- ネストした `.claude/rules/*.md` が、設定ソースがプロジェクト設定を除外していても読み込まれる問題を修正。
- `/clear` がセッションのコストカウンタをリセットせず、statusline のコストが `/clear` 後も 0 に戻らない問題を修正。
- `/loop` が一度使うとセッションを `/resume` から隠す問題、スケジュールのないルーチンが次回実行を西暦 1 年と報告する問題、Windows のヘッドレス print モードで stdin が読めないとクラッシュ/無音終了する問題を修正。
- ユーザーが kill したバックグラウンドエージェントが自動再生成され、復活したエージェントが古いセッションの stale なプロンプトを再実行する問題を修正。あわせて、まだ実行中のエージェントの状態を Claude が正しく報告し、結果を捏造せず実完了を待つよう改善。
- このほか v2.1.211 では、Chrome 拡張が有効でも Chrome 未起動時の起動ハング、非同期コンテンツ表示の 300ms 遅延、直前に停止したバックグラウンドセッションを再度開くと同一 ID で空会話になる問題、`/terminal-setup` 後にスクリーンリーダー利用者が端末ベルを失う問題、Windows での Claude in Chrome セットアップページがブラウザで開かない問題など、多数の修正が入っている。

**その他**

- 「always allow」権限ルールがリポジトリルートに保存されるよう変更され、git worktree で与えた承認がセッションと worktree をまたいで持続するようになった。
- `/usage-credits` が組織管理者へリクエストを送る前に確認を求めるよう変更された。
- Vim モードの `s`・`S`（文字/行の置換）が vim 同様 NORMAL モードで効くよう変更された。
- 整数の環境変数（タイムアウト・トークン予算・リトライ回数）が `1e6` や `64_000` のような指数表記・桁区切り表記を受け付けるようになった。
- Compliance API と context management のドキュメントリンク先 URL が現行のものに更新された（表示内容の実質変化なし）。
- 多数のページのドキュメントリンクが現行のドキュメントサイトに更新された。
<!-- light:minor-updates:end -->

## 新着情報

<!-- light:whats-new:start -->
今回の対象期間では、週刊ダイジェスト「新着情報」（`whats-new/`）の**変更はありません**（新規追加・更新ともになし）。
<!-- light:whats-new:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-07-14.md](./archives/latest/2026-07-14.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-07-14.md](./archives/latest-detail/2026-07-14.md)

<!--
base_commit: 991b037c23024d28c04a58fcaebe2c1862fc912d
head_commit: fa4c4c546b211cf29cac5e7c4dcc5b3e95008594
generated_at_full: 2026-07-16T15:00:33+09:00
-->
