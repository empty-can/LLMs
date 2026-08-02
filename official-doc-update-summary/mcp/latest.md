---
対象期間: 2026年07月27日 〜 2026年07月28日
作成日: 2026-07-28
---

# MCP 公式ドキュメント更新サマリ

```markdown
MCP 仕様の新リビジョン `2026-07-28` が公開され、これまでの `2025-11-25` に代わって現行版になりました。プロトコル自体をステートレスにする破壊的変更が中心で、`initialize` ハンドシェイクとセッションの廃止、サーバー起点リクエストの置き換え、通知配信の一本化が一度に入っています。あわせてドキュメントの URL もバージョン付きパス（`/docs/2026-07-28/...`）に変わり、仕様側は 16 ページが新設・20 ページが大幅改稿されました。

主要なものを以下に挙げます。

1. MCP 仕様 2026-07-28 が公開され、仕様・ドキュメントの URL がバージョン付きパスに変わった
2. `initialize` ハンドシェイクとセッションが廃止され、全リクエストが自己完結する形になった
3. サーバーからの追加入力要求が MRTR パターンに置き換わり、全 result に `resultType` が必須化された
4. 変更通知の配信が `subscriptions/listen` の 1 本のストリームに統合された
5. Roots・Sampling・Logging が非推奨になり、Tasks は公式拡張へ移された
```

## ハイライト

1. [**MCP 仕様 2026-07-28 が公開**](./latest-detail.md#1-mcp-仕様-2026-07-28-が公開):  
  前リビジョン `2025-11-25` に代わる現行仕様として `2026-07-28` が公開された。仕様ページの URL が `/specification/2026-07-28/` に切り替わったほか、これまでバージョンを持たなかったドキュメント側も `/docs/2026-07-28/` というバージョン付きパスに変わっている。
2. [**プロトコルのステートレス化**](./latest-detail.md#2-プロトコルのステートレス化):  
  `initialize` / `notifications/initialized` のハンドシェイクと Streamable HTTP の `Mcp-Session-Id` が廃止され、各リクエストが `_meta` でプロトコルバージョンとクライアント能力を自ら申告する形になった。サーバー情報の取得には新設の必須 RPC `server/discover` を使う。
3. [**多段リクエスト MRTR への移行**](./latest-detail.md#3-多段リクエスト-mrtr-への移行):  
  `sampling/createMessage` などのサーバー起点リクエストが廃止され、サーバーは `resultType: "input_required"` の中間結果で追加入力を要求し、クライアントが元のリクエストを再送する方式に変わった。あわせて全ての result に `resultType` フィールドが必須化された。
4. [**通知ストリームの一本化**](./latest-detail.md#4-通知ストリームの一本化):  
  HTTP GET エンドポイントと `resources/subscribe` / `resources/unsubscribe` が廃止され、クライアントが受け取りたい通知種別を明示して開く長寿命ストリーム `subscriptions/listen` に統合された。SSE の再送・再開機能（`Last-Event-ID`）も削除されている。
5. [**主要機能の非推奨化と Tasks の拡張への移出**](./latest-detail.md#5-主要機能の非推奨化と-tasks-の拡張への移出):  
  機能ライフサイクル方針の導入にあわせ、Roots・Sampling・Logging と動的クライアント登録が非推奨になった。実験的機能だった Tasks はコアプロトコルから外れ、公式拡張 `io.modelcontextprotocol/tasks` として再設計されている。

## 新規追加されたページ

- [**Versioning and Compatibility**](./latest-detail.md#1-versioning-and-compatibility) ([MCP Docs](https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning)):  
  ハンドシェイク廃止後のバージョン交渉・拡張交渉・旧リビジョンとの相互運用をまとめた新設ページ。「modern」「legacy」「dual-era」の用語と、クライアント／サーバーの組み合わせ 7 通りの互換性マトリクスが示された。
- [**Discovery**](./latest-detail.md#2-discovery) ([MCP Docs](https://modelcontextprotocol.io/specification/2026-07-28/server/discover)):  
  新設された必須 RPC `server/discover` の仕様。対応プロトコルバージョン・能力・識別情報を 1 リクエストで返し、結果はキャッシュ可能。
- [**Multi Round-Trip Requests**](./latest-detail.md#3-multi-round-trip-requests) ([MCP Docs](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/mrtr)):  
  サーバー起点リクエストを置き換える MRTR パターンの仕様。`InputRequests` / `InputResponses` / `InputRequiredResult` の型定義と、`requestState` の完全性保護要件が定義された。
- [**Subscriptions**](./latest-detail.md#4-subscriptions) ([MCP Docs](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/subscriptions)):  
  `subscriptions/listen` による通知ストリームの仕様。通知フィルタ・確認応答・購読 ID による多重化・正常終了の手順が定義された。
- [**Caching**](./latest-detail.md#5-caching) ([MCP Docs](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/caching)):  
  結果キャッシュのユーティリティ仕様。`ttlMs` と `cacheScope` の意味、キャッシュキーの決め方、通知・ページネーションとの相互作用が定義された。
- [**Deprecated Features**](./latest-detail.md#6-deprecated-features) ([MCP Docs](https://modelcontextprotocol.io/specification/2026-07-28/deprecated)):  
  非推奨状態の機能を一覧する登録簿。機能ごとに根拠 SEP・非推奨化されたリビジョン・移行先・最短の削除時期が表で示される。
- [**メッセージパターン概要**](./latest-detail.md#7-メッセージパターン概要) ([MCP Docs](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/index)):  
  コアプロトコルが備える 3 つのメッセージパターン（リクエスト・レスポンス／MRTR／購読・通知）の索引ページ。
- [**Cancellation**](./latest-detail.md#8-cancellation) ([MCP Docs](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/cancellation)):  
  `basic/utilities/` から `basic/patterns/` 配下へ移動したキャンセル通知の仕様。
- [**Progress**](./latest-detail.md#9-progress) ([MCP Docs](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/progress)):  
  `basic/utilities/` から `basic/patterns/` 配下へ移動した進捗通知の仕様。
- [**トランスポート概要**](./latest-detail.md#10-トランスポート概要) ([MCP Docs](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/index)):  
  1 ページだった Transports を分割してできた索引ページ。トランスポート共通のメッセージ形式・リクエストメタデータ・キャンセルを扱う。
- [**stdio**](./latest-detail.md#11-stdio) ([MCP Docs](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/stdio)):  
  stdio トランスポート単独のページ。`server/discover` をプローブに使う後方互換の判定手順が加わった。
- [**Streamable HTTP**](./latest-detail.md#12-streamable-http) ([MCP Docs](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http)):  
  Streamable HTTP 単独のページ。標準リクエストヘッダー `Mcp-Method` / `Mcp-Name` の必須化と、ツールパラメーターを HTTP ヘッダーへ写す `x-mcp-header` が加わった。
- [**Authorization**](./latest-detail.md#13-authorization) ([MCP Docs](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/index)):  
  1 ページだった Authorization を分割してできた本体ページ。役割・認可フロー・トークン利用・エラー処理を扱う。
- [**Authorization Server Discovery**](./latest-detail.md#14-authorization-server-discovery) ([MCP Docs](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/authorization-server-discovery)):  
  保護対象リソースメタデータからの認可サーバー探索手順を独立させたページ。
- [**Client Registration**](./latest-detail.md#15-client-registration) ([MCP Docs](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/client-registration)):  
  クライアント登録の 3 方式（CIMD／事前登録／DCR）と優先順位を独立させたページ。CIMD が第一選択として位置づけられた。
- [**Authorization Security Considerations**](./latest-detail.md#16-authorization-security-considerations) ([MCP Docs](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization/security-considerations)):  
  認可まわりのセキュリティ考慮事項を独立させたページ。CIMD 固有の項目（認可サーバー悪用対策・信頼ポリシー）が加わった。

## 大幅に更新されたページ

- [**Key Changes**](./latest-detail.md#1-key-changes) ([MCP Docs](https://modelcontextprotocol.io/specification/2026-07-28/changelog)):  
  `2026-07-28` リビジョンの変更点一覧に全面的に書き換えられた。破壊的変更 9 件・小規模変更 12 件・非推奨化 4 件が列挙されている。
- [**Overview（基本プロトコル）**](./latest-detail.md#2-overview基本プロトコル) ([MCP Docs](https://modelcontextprotocol.io/specification/2026-07-28/basic/index)):  
  ライフサイクル管理の節が消え、ステートレス性・`resultType`・エラーコード割り当て方針・`_meta` の予約キー一覧が新設された。
- [**Schema Reference**](./latest-detail.md#3-schema-reference) ([MCP Docs](https://modelcontextprotocol.io/specification/2026-07-28/schema)):  
  スキーマ参照が新リビジョンの内容に置き換わった。差分規模が最大のページ。
- [**Tools**](./latest-detail.md#4-tools) ([MCP Docs](https://modelcontextprotocol.io/specification/2026-07-28/server/tools)):  
  `InputRequiredResult` を返す節と `x-mcp-header` が追加され、`execution.taskSupport` が削除された。一覧の決定的な順序付けが推奨に加わった。
- [**Resources**](./latest-detail.md#5-resources) ([MCP Docs](https://modelcontextprotocol.io/specification/2026-07-28/server/resources)):  
  `subscribe` 能力の意味が `subscriptions/listen` 前提に改められ、一覧結果に `resultType` とキャッシュヒントが加わった。
- [**Prompts**](./latest-detail.md#6-prompts) ([MCP Docs](https://modelcontextprotocol.io/specification/2026-07-28/server/prompts)):  
  一覧結果への `resultType`・キャッシュヒントの追加と、変更通知が購読ストリーム経由になったことの反映。
- [**Logging**](./latest-detail.md#7-logging) ([MCP Docs](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/logging)):  
  非推奨の告知が加わり、`logging/setLevel` が削除されてリクエスト単位のログレベル指定に置き換わった。
- [**Sampling**](./latest-detail.md#8-sampling) ([MCP Docs](https://modelcontextprotocol.io/specification/2026-07-28/client/sampling)):  
  非推奨の告知が加わり、リクエストの受け渡しが MRTR 経由に、能力宣言が `_meta` 経由に改められた。
- [**Elicitation**](./latest-detail.md#9-elicitation) ([MCP Docs](https://modelcontextprotocol.io/specification/2026-07-28/client/elicitation)):  
  MRTR 経由の受け渡しに改められ、`notifications/elicitation/complete` と `elicitationId` が削除された。
- [**Roots**](./latest-detail.md#10-roots) ([MCP Docs](https://modelcontextprotocol.io/specification/2026-07-28/client/roots)):  
  非推奨の告知が加わり、`listChanged` 能力と変更通知が削除された。アクセス制御ではなく情報提供である旨が明示された。
- [**Architecture**](./latest-detail.md#11-architecture) ([MCP Docs](https://modelcontextprotocol.io/specification/2026-07-28/architecture/index)):  
  ステートフルなセッション前提の記述がリクエスト単位の記述に置き換えられ、能力交渉の説明が `server/discover` ベースになった。
- [**Architecture overview**](./latest-detail.md#12-architecture-overview) ([MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture)):  
  学習ガイド側の解説とサンプル JSON が刷新され、初期化シーケンスの例が `server/discover` の例に差し替えられた。
- [**Understanding MCP clients**](./latest-detail.md#13-understanding-mcp-clients) ([MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/learn/client-concepts)):  
  Roots・Sampling に非推奨の警告が付き、Elicitation にフォームモードと URL モードの説明が加わった。
- [**Build an MCP client**](./latest-detail.md#14-build-an-mcp-client) ([MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-client)):  
  Python は SDK 2.0.0 以上が必須になり `Client` クラス中心の実装へ、TypeScript は `@modelcontextprotocol/client` パッケージへ全面的に書き換えられた。
- [**Build an MCP server**](./latest-detail.md#15-build-an-mcp-server) ([MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-server)):  
  Python は SDK 2.0.0 以上が必須になり、`FastMCP` が `MCPServer` に、`httpx` が `httpx2` に置き換わった。
- [**Debugging**](./latest-detail.md#16-debugging) ([MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/tools/debugging)):  
  ログの推奨手段が `notifications/message` から stderr・OpenTelemetry に改められ、互換性確認の手順が `server/discover` ベースになった。
- [**Understanding Authorization in MCP**](./latest-detail.md#17-understanding-authorization-in-mcp) ([MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/authorization)):  
  Python の実装例が `FastMCP` から `MCPServer` に置き換わり、設定クラスから不要になった項目が整理された。
- [**Security Best Practices**](./latest-detail.md#18-security-best-practices) ([MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices)):  
  セッションハイジャックの節が状態ハンドルハイジャックの節に置き換わり、認可サーバーに対する SSRF の節が追加された。
- [**Extensions Overview**](./latest-detail.md#19-extensions-overview) ([MCP Docs](https://modelcontextprotocol.io/extensions/overview)):  
  拡張の宣言方法が `initialize` から、リクエストごとの `_meta` と `server/discover` の応答に改められた。
- [**OAuth Client Credentials**](./latest-detail.md#20-oauth-client-credentials) ([MCP Docs](https://modelcontextprotocol.io/extensions/auth/oauth-client-credentials)):  
  能力宣言の例が新方式に更新され、Python のサンプルコードがトークン保存の実装込みで書き直された。

## 軽微な更新

今回の差分は仕様リビジョン `2026-07-28` の公開に伴うもので、上記以外にも 19 ページに小規模な変更が入っています。あわせて、再編により一覧から無くなったページもあります。

**新機能**

- Client Best Practices に「Caching」の節が新設され、一覧結果・`server/discover`・`resources/read` が返す `ttlMs` と `cacheScope` に従うこと、`list_changed` 通知が届いたら TTL 満了前でもキャッシュを陳腐とみなすことが示された — [Client Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/develop/clients/client-best-practices#caching)
- Specification に「Extensions」の節が新設され、Tasks・Skills over MCP・MCP Apps が主な拡張として紹介された — [Specification](https://modelcontextprotocol.io/specification/2026-07-28/index#extensions)

**機能改善**

- Specification の基本プロトコルの説明が「ステートフルな接続」「サーバー・クライアントの能力交渉」から「ステートレスで自己完結したリクエスト」「リクエストごとの能力交渉」に改められ、クライアント機能の一覧から Sampling と Roots が外れた（詳細はハイライト 2 参照） — [Specification](https://modelcontextprotocol.io/specification/2026-07-28/index#base-protocol)
- Versioning の「Negotiation」節が、初期化時の交渉からリクエストごとのバージョン宣言と `UnsupportedProtocolVersionError` による再試行の説明に書き換えられた — [Versioning](https://modelcontextprotocol.io/docs/2026-07-28/learn/versioning#negotiation)
- Understanding MCP servers のリソース操作一覧で `resources/subscribe` が `subscriptions/listen` に置き換わり、`resourceSubscriptions` フィルタで監視対象を指定する説明が追記された — [Understanding MCP servers](https://modelcontextprotocol.io/docs/2026-07-28/learn/server-concepts#resources)
- Client Best Practices の動的サーバー管理のシーケンス図が、接続の初期化から `server/discover` と `tools/list` の 2 段構成に更新された — [Client Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/develop/clients/client-best-practices#dynamic-server-management)
- Completion のリクエスト例に `_meta` 省略の注記が加わり、結果に `resultType` が追加された — [Completion](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/completion#protocol-messages)
- Completion の参照型が `ResourceReference` から `ResourceTemplateReference` に改められ、`uri` が URI または URI テンプレートを取ることが明記された — [Completion](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/completion#reference-types)
- Pagination のリクエスト例に `_meta` 省略の注記が加わり、結果例に `resultType` とキャッシュヒントが追加された — [Pagination](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/pagination#pagination-model)
- Pagination のカーソル取り扱い指針が「セッションをまたいで永続化しない」から「非 null かどうか以外の判断材料にしない（空文字列も有効なカーソルであり終端とみなしてはならない）」に改められた — [Pagination](https://modelcontextprotocol.io/specification/2026-07-28/server/utilities/pagination#pagination-model)
- Enterprise-Managed Authorization の能力宣言例が、`initialize` の `capabilities` からリクエストごとの `_meta` に置く形に更新された — [Enterprise-Managed Authorization](https://modelcontextprotocol.io/extensions/auth/enterprise-managed-authorization#implementation-guide)
- Authorization Extensions の拡張宣言の説明が、初期化時の宣言からリクエストごとの `_meta` と `server/discover` 応答に改められた — [Authorization Extensions](https://modelcontextprotocol.io/extensions/auth/overview#specification)
- Extension Support Matrix の拡張宣言手順が同様に更新され、サーバー側の `extensions` は `server/discover` 応答から読む旨が追記された — [Extension Support Matrix](https://modelcontextprotocol.io/extensions/client-matrix#adding-extension-support-to-your-client)
- Publishing Remote Servers で、SSE トランスポートが非推奨であることが明示され、Streamable HTTP を使い `"sse"` の公開は既存クライアント対応に限る旨に改められた — [Publishing Remote Servers](https://modelcontextprotocol.io/registry/remote-servers#transport-type)
- Design Principles の基本プリミティブの列挙から tasks が外れ、Tasks が MCP Apps と並ぶ拡張の例として挙げられるようになった — [Design Principles](https://modelcontextprotocol.io/community/design-principles#composability-over-specificity)
- Roadmap のエージェント間通信の項が、Tasks プリミティブ（SEP-1686）から Tasks 拡張（SEP-2663）への言及に更新された — [Roadmap](https://modelcontextprotocol.io/development/roadmap)
- SDK Tiering System の記述が「実験的機能（Tasks など）とプロトコル拡張（MCP Apps など）」から「実験的機能とプロトコル拡張（Tasks や MCP Apps など）」に整理された — [SDK Tiering System](https://modelcontextprotocol.io/community/sdk-tiers)
- Connect to local MCP servers で、`mcp-server-SERVERNAME.log` はエラーだけでなく stderr 出力全般を含む旨が補足された — [Connect to local MCP servers](https://modelcontextprotocol.io/docs/2026-07-28/develop/connect-local-servers)
- Tasks（拡張）の能力宣言例が、リクエストごとの `_meta` と `server/discover` 応答に置く形に更新され、コード例が注釈付きの `jsonc` 表記に変わった — [Tasks](https://modelcontextprotocol.io/extensions/tasks/overview#implementation-guide)
- SEP-1686 の冒頭に、本 SEP は `2025-11-25` で出荷された実験的 tasks の歴史的記録であり、現行の設計は拡張として SEP-2663 に移った旨の注記が追加された — [SEP-1686: Tasks](https://modelcontextprotocol.io/seps/1686-tasks#abstract)

**その他**

- 仕様の再編に伴い、`basic/lifecycle`（Lifecycle）・`basic/utilities/ping`（Ping）・`basic/utilities/tasks`（Tasks）の 3 ページが一覧から無くなった。ライフサイクル管理は Versioning and Compatibility とメッセージパターンに、Ping は機能ごと削除、Tasks は拡張として再編されている（詳細はハイライト 2・5 参照）
- Build with Agent Skills 内の仕様への参照リンクが `draft` から現行リビジョンのパスに更新された — [Build with Agent Skills](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-with-agent-skills)
- Frequently Asked Questions の表記が `PyPi` から `PyPI` に修正された — [Frequently Asked Questions](https://modelcontextprotocol.io/registry/faq)
- Example Servers は本文の変更ではなく、`llms-full.txt` 上で同一ページが二重に出力されている（取り込み元の生成に由来する差分） — [Example Servers](https://modelcontextprotocol.io/examples)

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-07-27_1500.md](./archives/latest/2026-07-27_1500.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-07-27_1500.md](./archives/latest-detail/2026-07-27_1500.md)

<!--
base_commit: acb98138d56384b7f41664f8d0657385c8d5f56a
head_commit: 37f111d9d0c49fa9fd2ab79826f803c7de899551
generated_at_full: 2026-07-29T15:32:03+09:00
-->
