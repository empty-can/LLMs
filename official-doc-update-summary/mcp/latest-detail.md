---
対象期間: 2026年11月18日 〜 2026年11月19日
作成日: 2026-11-19
---

# MCP 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
今回の対象期間の取り込みは 1 回で、新規ページが 1 件（SEP-3415: Events Extension、1,284 行）加わり、既存ページの変更は SEP の索引ページ 1 件だけでした。MCP クライアントが外部のシステムで起きた出来事を購読し、ユーザーがいないときでもエージェントが反応できるようにする Events 拡張の SEP が、Final の状態で収録されています。

主要なものを以下に挙げます。

1. SEP-3415（Events Extension）が Final の状態で加わった。サーバーは `events/list` で購読できるイベントの種類を示し、クライアントは名前と引数で購読して、`{eventId, name, timestamp, data, cursor}` の形のイベントを受け取る
2. 配信方式は poll（`events/poll`）・push（`events/stream`）・webhook（`events/subscribe`）の 3 つで、イベントの種類ごとに対応する方式を示し、どれも必須ではない
3. webhook では、クライアントが渡す `whsec_` 形式の秘密鍵による Standard Webhooks の署名、期限（TTL）付きの購読、配信を始める前のエンドポイントの確認、SSRF 対策を定めている
4. サーバーが決める不透明なカーソルで切断後に再開でき、イベントが飛んだことは `truncated: true` で知らせる。順序と配信の保証は購読ごとの範囲にとどめている
5. 汎用のエラーコード 5 つ（`-32023`〜`-32027`。本文では採択までの暫定の番号）を求め、Streamable HTTP ではイベント名を `Mcp-Name` ヘッダーに入れる
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**外部の出来事を購読する Events 拡張の SEP-3415 が Final で加わった**](#1-外部の出来事を購読する-events-拡張の-sep-3415-が-final-で加わった):  
  Extensions Track の SEP-3415（Events Extension、作成 2026年10月05日）が Final の状態で新規ページとして加わった。Slack のメッセージ、GitHub への push、PagerDuty のインシデントのような外部のシステムでの出来事を MCP クライアントが購読し、ユーザーがいなくてもエージェントが反応できるようにする拡張で、識別子は `io.modelcontextprotocol/events`。サーバーは `events/list` でイベントの種類ごとに、購読の引数の `inputSchema`、届けるデータの `payloadSchema`、対応する配信方式を示す。プロトコルのリビジョン `2026-07-28` 以降を対象とする。
2. [**配信方式は poll と push と webhook の 3 つでどれも必須ではない**](#2-配信方式は-poll-と-push-と-webhook-の-3-つでどれも必須ではない):  
  poll は `events/poll` を繰り返す要求・応答型で、最初の `null` のカーソルで購読が始まり、サーバーはプロトコル上の状態を持たない。push は購読ごとに長く開いておく `events/stream` リクエストで、イベントを `notifications/events/event` の通知で届け、サーバーはハートビートを送らなければならない（MUST）。webhook は `events/subscribe` で `https` のコールバック URL を登録する。イベントの種類はこのうち 1 つ以上を `delivery` に挙げ、どれも必須ではない。
3. [**webhook は署名と TTL とエンドポイントの確認で守られる**](#3-webhook-は署名と-ttl-とエンドポイントの確認で守られる):  
  webhook の配信は Standard Webhooks のプロファイルで、署名の秘密鍵（`whsec_` 形式）はクライアントが必ず渡し、サーバーは生成しない。購読には TTL があり、クライアントが `ttlMs` を提案してサーバーが `refreshBefore` で期限を与える（クライアントが `ttlMs: null` を求めた場合に限り、`null` で期限なしを与えられる）。サーバーは、エンドポイントに受け取る意思があることを 4 つの方法のいずれかで確かめるまで配信を始めてはならず（MUST NOT）、コールバック URL の検証は配信の時点でも行い、リダイレクトをたどらない。webhook の購読には認証済みの主体（principal）が要る。
4. [**カーソルで再開でき欠落は truncated で知らせる**](#4-カーソルで再開でき欠落は-truncated-で知らせる):  
  カーソルはサーバーが管理する不透明な文字列で、切断やクラッシュのあとにクライアントがそこから再開できる。再生（replay）に対応するかはイベントの種類ごとに任意で、対応しない種類では `cursor: null` を返してよい（MAY）。`maxAgeMs` で再生の範囲を時間で絞れ、サーバーがクライアントのカーソルより後ろから配信を始めたときは `truncated: true` で知らせる。順序はプロトコルとしては保証せず、poll と push では購読の中での順序、webhook ではベストエフォートとしている。
5. [**汎用のエラーコード 5 つとルーティング用のヘッダーが盛り込まれた**](#5-汎用のエラーコード-5-つとルーティング用のヘッダーが盛り込まれた):  
  `NotFound`（`-32023`）・`Forbidden`（`-32024`）・`ResourceExhausted`（`-32025`）・`Unsupported`（`-32026`）・`CallbackEndpointError`（`-32027`）の 5 つを、イベントに限らない汎用のコードとして求めている。番号は、採択の時点で割り当て済みのコードが `-32020`〜`-32022` だけであることを前提にした、採択までの暫定のもの。Streamable HTTP では、`events/list` 以外の 4 つのリクエストでイベント名を `Mcp-Name` ヘッダーに入れなければならない（MUST）。
<!-- light:highlight-list:end -->

## 1. 外部の出来事を購読する Events 拡張の SEP-3415 が Final で加わった

今回の取り込みは 1 回で、差分は索引 `llms.txt` の追加 1 行と、本文 `llms-full.txt` の追加 1,286 行・削除 1 行です。`llms-full.txt` の総行数は 46,048 行から 47,333 行に、収録ページ数は 161 件から 162 件（`examples` が 2 回収録されているため、URL としては 160 件から 161 件）に、`llms.txt` のエントリ数は 362 件から 363 件になりました。追加行のうち 1,284 行は新規ページの SEP-3415 で、残りは SEP の索引ページ（追加 2 行・削除 1 行）です。既存のページで変わったのはこの索引ページだけです。

**SEP-3415 は、MCP に「イベント」を加える Extensions Track の SEP です。** 作成は 2026年10月05日、Status は Final で、著者とスポンサーはいずれも Peter Alexander 氏（[@poita](https://github.com/poita)）です。他の Final の SEP と同じく、冒頭には「Final に達した SEP は採択時の設計の歴史的な記録で、確定後のプロトコルの変更は反映されない」という注記があります。拡張の識別子は `io.modelcontextprotocol/events` で、プロトコルのリビジョン `2026-07-28` 以降を対象とします（リクエストごとのクライアントの機能宣言、`server/discover`、`subscriptions/listen` に依存するため）。この拡張が定める結果はすべて標準の `Result` で、`resultType: "complete"` を持ちます。

**機能の交渉**: サーバーは `server/discover` が返す capabilities の `extensions` に `io.modelcontextprotocol/events` を置いて対応を示します。設定オブジェクトのメンバーは `listChanged`（真偽値・省略可・既定は `false`）の 1 つで、`true` ならイベントの種類が変わったときに `notifications/events/list_changed` を送ります。クライアントは、リクエストの `_meta` の `io.modelcontextprotocol/clientCapabilities` に、空の設定オブジェクトで同じ識別子を宣言してよい（MAY）とされています。`events/*` のリクエストはすべてクライアントから送るもので、拡張を広告していないサーバーに送ってはならず（MUST NOT）、対応していないサーバーは `-32601`（Method not found）を返します。

**イベントの種類（`events/list`）**: 各種類は `name`・`description`・`delivery`・`inputSchema`・`payloadSchema`（と任意の `_meta`）を持ちます。`inputSchema` は購読の引数の JSON Schema で、引数はイベントを絞り込むフィルタ、データを加工する変換、そのほかサーバーが決める設定のいずれでもよく、ツールの `inputSchema` と `arguments` の組に倣っています。購読は作成元の `events/list` の応答より長く生きうるため、サーバーはスキーマを追加の形で変えるべき（SHOULD）で、互換性を壊す変更は新しいイベント名で公開し、移行期間のあいだ旧名と並べて提供すべきとされています。種類の一覧の変化を知らせる `notifications/events/list_changed` は、コアの `list_changed` 通知と同じく `subscriptions/listen` のストリームで、クライアントがフィルタの `eventsListChanged` で求めた場合にだけ届きます。

**届くイベント（`EventOccurrence`）**:

| フィールド | 必須 | 内容 |
|---|---|---|
| `eventId` | はい | 上流のイベントの安定した識別子。購読の中での重複排除に使う |
| `name` | はい | イベントの種類の名前 |
| `timestamp` | はい | 出来事が起きた時刻（ISO 8601） |
| `data` | はい | `payloadSchema` に従うデータ |
| `cursor` | いいえ | このイベントの後の購読の位置。push と webhook だけで、poll では応答の側に置く。再生に対応しない種類では `null` |
| `_meta` | いいえ | プロトコルと拡張のメタデータ用。`payloadSchema` の対象外 |

`eventId` は、上流に安定した識別子（Stripe の `evt_*`、GitHub の配信 GUID、Kafka のオフセット、Gmail のメッセージ ID など）があればそれを使うべき（SHOULD）とされ、webhook と poll のように別の経路で同じ出来事が届いても重複として除けます。重複排除の範囲は購読（`name` と `arguments`）ごとで、同じ `eventId` が 2 つの購読に届くのは重複ではありません。

**購読の状態はクライアントが持ちます。** サーバー上の購読を一覧するメソッドは無く、クライアントが自分の購読の一覧を管理し、webhook の冪等な `events/subscribe` や、保存したカーソルからの poll・push の再開で、いつでもサーバー側の状態を作り直せます。

**Working Group と育成の場**: 拡張は Triggers & Events Working Group が所有し、Extension Maintainer はその Lead（現在は Clare Liguori 氏と Peter Alexander 氏）とされています。拡張は `experimental-ext-triggers-events` リポジトリで育成（incubate）されており、本文には「この SEP が採択されたら、仕様は SEP-2133 のとおり公式の拡張リポジトリで公開される」とあります。なお、収録されている「Tasks and Events Charter」（今回は変更なし）の Changelog によると、この WG は 2026年10月16日 に Tasks and Events WG へ改称されており、SEP が張る WG の charter へのリンク（`/community/triggers-events/charter`）は、公式サイトでは現在の `community/working-groups/tasks-events` へ転送されます。同じ charter の Active Work Items では、「SEP: Events in MCP v1 RFC」が Ideating のまま据え置かれています。

- [SEP-3415: Events Extension - MCP Docs](https://modelcontextprotocol.io/seps/3415-events-extension#abstract)
- [SEP-3415: Events Extension - MCP Docs](https://modelcontextprotocol.io/seps/3415-events-extension#capability-negotiation)

## 2. 配信方式は poll と push と webhook の 3 つでどれも必須ではない

イベントの種類は、対応する配信方式を `delivery` に `"poll"`・`"push"`・`"webhook"` の空でない部分集合として挙げます。どの方式も必須ではなく、挙げられた方式をどれも使えないクライアントは、その種類を購読できません。方式を選んでループを回すのはクライアントの SDK で、モデルには届いたイベントだけが見えます。

| 方式 | 購読の始め方 | 終わらせ方 | サーバーの状態 |
|---|---|---|---|
| poll | 購読ごとに `events/poll` を繰り返す。別の購読手続きは無く、最初の `null` のカーソルで始まる | 呼ぶのをやめる | プロトコル上は持たない |
| push | 購読ごとに長く開いておく `events/stream` リクエスト | リクエストを閉じるか取り消す | リクエストが開いている間だけ |
| webhook | `events/subscribe` でコールバック URL を登録し、期限までに呼び直して延長する | `events/unsubscribe` か、延長をやめて期限切れにする | 購読ごとに期限（TTL）付きで保持 |

**poll（`events/poll`）**: 1 回のリクエストは 1 つの購読を運び、購読が複数あれば購読ごとにループを回します。リクエストは `name`・`arguments`・`cursor` と、任意の `maxAgeMs`・`maxEvents` で、応答は `events`・`cursor`・`truncated`・`hasMore`・`nextPollMs` です。`hasMore` が `true` なら `nextPollMs` を無視してすぐに次を呼ぶべき（SHOULD）で、`false` なら `nextPollMs` だけ待ちます。`nextPollMs` はサーバーの推奨で、クライアントはそれより間隔を空けてもよく、誤動作するサーバーに短い間隔で呼ばされないよう、設定できる下限（既定 1000 ms）を設けるべき（SHOULD）とされています。空の `events` は「何も起きていない」ことを表し、これが通常の場合だとしています。

**push（`events/stream`）**: Streamable HTTP では SSE の応答を返す POST、stdio では stdin に書くリクエストで、イベントは JSON-RPC の通知として届きます。サーバーは最初に `notifications/events/active`（カーソル・`truncated`・与えるハートビートの間隔）で購読を確認し、その後 `notifications/events/event` でイベントを届けます。一時的な失敗は `notifications/events/error` で知らせて購読は続き、購読を終わらせるのは `notifications/events/terminated` だけです。どの通知も `params._meta["io.modelcontextprotocol/subscriptionId"]` に元の `events/stream` の JSON-RPC の `id` を持つので、stdout を共有する stdio でも複数のストリームを振り分けられます。取り消しは、Streamable HTTP ではリクエストのストリームを中断し、stdio では `notifications/cancelled` を送ります。

- **ハートビート**: サーバーは push のストリームで定期的に `notifications/events/heartbeat` を送らなければならない（MUST）。これにはサーバーが確認済みの位置の `cursor` が入り、該当するイベントが無くてもクライアントのカーソルが進む。SSE のコメント形式（`: keepalive`）はカーソルを運べないので使わない
- **間隔**: クライアントが `heartbeatMs` で提案し、サーバーが `notifications/events/active` で与える値が優先される。提案が無ければサーバーが決め、推奨の既定は 30 秒。与えられた間隔の 3 倍のあいだ何も届かなければ、クライアントはストリームが切れたものとしてカーソルを持って接続し直すべき（SHOULD）
- **同時のストリーム**: 購読ごとに 1 本で、HTTP/1.1 では 1 本が TCP 接続を 1 つ使うため、購読の多いクライアントは事実上 HTTP/2 の多重化に頼る。サーバーの SDK は、同時リクエスト数の一般的な上限から `events/stream` を除外しなければならない（MUST）

webhook の詳細はハイライト 3 で扱います。

- [SEP-3415: Events Extension - MCP Docs](https://modelcontextprotocol.io/seps/3415-events-extension#delivery-modes)
- [SEP-3415: Events Extension - MCP Docs](https://modelcontextprotocol.io/seps/3415-events-extension#poll-based-delivery)
- [SEP-3415: Events Extension - MCP Docs](https://modelcontextprotocol.io/seps/3415-events-extension#push-based-delivery)

## 3. webhook は署名と TTL とエンドポイントの確認で守られる

webhook は、長く開いておく接続（push）や頻繁な poll が難しいリモートのサーバー向けの方式で、サーバーはクライアントが渡したコールバック URL へイベントを POST します。コールバック先はクライアント自身でなくてもよく、webhook を受けて poll や push でクライアントに渡すフォワードプロキシを置く構成が、よくある形として挙げられています。

**購読（`events/subscribe`）**: リクエストは `name`・`arguments`・`delivery`（`mode`・`url`・`secret`）・`cursor`・`maxAgeMs`・`ttlMs` で、応答は `id`・`refreshBefore`・`cursor`・`truncated` です。同じ購読キーで呼び直すと TTL が延び、変更できるフィールドが更新されます（冪等）。延長の応答には、配信の状況を示す `deliveryStatus`（`active`・`lastDeliveryAt`・`lastError` など）を含めてよい（MAY）とされています。

- **購読キー**: `(principal, delivery.url, name, arguments)` の 4 つで、どれも購読の間は変えられない。`events/subscribe` と `events/unsubscribe` は認証済みの主体で呼ばなければならず（MUST）、主体の無い呼び出しは `Forbidden` で拒否する。認証の無い MCP サーバーは poll と push を提供できるが、webhook は提供できない
- **`id`**: サーバーがキーから決定的に導く値で、配信の振り分けにだけ使う。すべての POST の `X-MCP-Subscription-Id` ヘッダーに入るが、どのメソッドの入力としても受け付けず、知っていても何の権限にもならない
- **秘密鍵**: `delivery.secret` は必須（REQUIRED）で、`whsec_` の後に 24〜64 バイトの乱数の base64 を続けた Standard Webhooks の形式でなければならない。サーバーはそれ以外を `InvalidParams` で拒否し、自分では生成しない。鍵の更新はクライアントが延長の際に新しい値を渡して行い、サーバーは短い猶予の間、新旧の両方で署名すべき（SHOULD）

**TTL**: クライアントは `ttlMs` で寿命を提案し（省略はサーバーの既定、`null` は期限なしの要求）、サーバーが `refreshBefore`（ISO 8601 の時刻、または `null`）で期限を与えます。与える期限は提案以下であるべき（SHOULD）ですが、短すぎる提案をサーバーの最小値まで引き上げることは認められています（MAY）。`refreshBefore: null`（期限なし）は、クライアントが `ttlMs: null` を提案した場合にしか返してはならず（MUST NOT）、期限なしを与えたサーバーは再起動をまたいで購読を保持しなければなりません（MUST）。有限の期限については、数分から 1 日程度でほとんどの配備をまかなえるとしています。

**配信**: POST には Standard Webhooks の `webhook-id`・`webhook-timestamp`・`webhook-signature` と、MCP 独自のヘッダーとしては唯一の `X-MCP-Subscription-Id` が付きます。署名は `HMAC-SHA256(secret, webhook-id + "." + webhook-timestamp + "." + body)` を base64 にして `v1,` を前置したもので、受信側は受け取ったままの本文のバイト列で計算しなければなりません（MUST）。受信側は処理の前に署名を検証しなければならず（MUST）、`webhook-timestamp` が 5 分より古い配信は拒否すべき（SHOULD）とされています。

- **再試行**: `2xx` 以外の応答には、イベントごとに独立して指数バックオフで再試行する。回数と期間の両方に上限を設けるべき（SHOULD）で、例として「3〜5 回を 10〜15 分以内」が挙がっている。受信側が再試行を望まないときは `410 Gone` を返し、サーバーはそれを再試行しない失敗として扱わなければならない（MUST）
- **本文のカーソル**: 配信の本文の `cursor` は、それ以前のイベントがすべて受け付けられたか見切られた位置（安全に保存できる水位線）で、イベント自身の位置ではない。そのため配信が順不同で届いても、クライアントが危険なカーソルを保存することはない
- **制御用の本文**: イベントのほかに、`type` を持つ制御用の本文 `gap`（カーソルの欠落を知らせる）・`terminated`（購読の終了）・`verification`（エンドポイントの確認）の 3 種類を POST する

**エンドポイントの確認**: クライアントが渡す HMAC の秘密鍵で偽の配信は見抜けますが、攻撃者が被害者の URL を自分の鍵で購読させれば、被害者は POST を浴び続けます。そこでサーバーは、エンドポイントに受け取る意思があることを次のいずれかで確かめるまで、そのコールバック URL への配信を始めてはなりません（MUST NOT）。

1. 一度きりの短命な `challenge` を載せた `verification` の本文を POST し、エンドポイントが `2xx` の本文でそれを返す
2. サーバーに設定した許可リスト（allowlist）に URL が合う
3. サーバー自身の仕組み（ダッシュボードでの登録と確認など）で URL を事前に確認済み
4. コールバック URL の `https` のオリジンが `/.well-known/mcp-webhook-receiver.json` を公開し、受け付けるパスの接頭辞を宣言している

確認の結果は `(principal, url)` ごとに保持されます。

**その他の安全策**: コールバック URL は `https://` でなければならず（MUST）、それ以外は `InvalidParams` で拒否します。SSRF を防ぐため、サーバーはコールバック URL を検証しなければならず（MUST）、解決した IP が IANA の特殊用途アドレスのレジストリに照らしてグローバルにルーティングできないものは拒否すべきです（SHOULD）。DNS rebinding を防ぐため、この検証は購読時だけでなく配信時にも行わなければならず（MUST）、配信のリクエストは HTTP のリダイレクトをたどってはなりません（MUST NOT）。`deliveryStatus.lastError` は 6 つの決まった分類（`connection_refused`・`timeout`・`tls_error`・`http_4xx`・`http_5xx`・`challenge_failed`）の文字列でなければならず、エンドポイントの応答の本文やヘッダーを含めてはなりません（MUST NOT）。任意で、ed25519 の非対称鍵による署名（`v1a,`）を HMAC の署名に添えてよく（MAY）、検証用の公開鍵はサーバーの Server Card で公開します（この置き場所は ext-server-card#55 に依存）。

**購読の解除（`events/unsubscribe`）**: 購読は延長をやめれば期限切れになるので、解除は正しさのためには必須ではなく、サーバーの資源をすぐに解放して配信を止めるためのものです。期限なしの購読では、クライアントから片付ける手段はこれだけです。

- [SEP-3415: Events Extension - MCP Docs](https://modelcontextprotocol.io/seps/3415-events-extension#webhook-based-delivery)
- [SEP-3415: Events Extension - MCP Docs](https://modelcontextprotocol.io/seps/3415-events-extension#subscription-ttl)
- [SEP-3415: Events Extension - MCP Docs](https://modelcontextprotocol.io/seps/3415-events-extension#webhook-security)

## 4. カーソルで再開でき欠落は truncated で知らせる

**カーソル**はサーバーが管理する不透明な文字列で、イベントの流れの中の位置を表します。どの方式でも `cursor: null` を渡すと「今から」の意味になり、過去のイベントは再生されません。`cursor` フィールドが無いことは、明示的な `null` と同じに扱わなければなりません（MUST）。

- **再生は種類ごとに任意**: 上流が push だけで履歴を持たない場合などは、サーバーはどの配信でも `cursor: null` を返してよい（MAY）。受け取ったクライアントはそれを保存したり、そこから再生しようとしたりしてはならず（MUST NOT）、切断中のイベントは取り戻せないものとして受け入れる。サーバーは種類ごとに一貫させるべき（SHOULD）とされる
- **イベントが無くてもカーソルが進む**: 上流の保持期間からカーソルが外れないよう、poll は空の結果でも、push はハートビートで、webhook は延長の応答で `cursor` を返す
- **`maxAgeMs` による再生の下限**: 3 つの方式とも、`cursor` と並べて任意の `maxAgeMs`（ミリ秒）を受け付ける。サーバーは「渡された `cursor`」と「現在 − `maxAgeMs`」の遅いほうから再生を始める。たとえば 1 週間オフラインだったホストも、`maxAgeMs: 300000` を付ければ直近 5 分ぶんだけを受け取れる。再生の範囲を件数で区切る仕組み（「最新の N 件」）は設けていない

**欠落と `truncated`**: `truncated: true` は、サーバーがクライアントのカーソルより後ろの位置から配信を始めた（イベントが飛んだ）ことを示す唯一の合図で、原因（上流の保持期間切れ、`maxAgeMs` の下限、サーバー自身の再生の上限）は区別しません。サーバーは配信できる位置に戻して新しいカーソルとともに返し、そのまま続けます。クライアントはこれを受けて接続し直したり購読し直したりはせず、欠落がありうるものとして扱い、必要ならツールで正しい状態を取り直すべき（SHOULD）とされています。

| 方式 | `truncated` が現れる場所 |
|---|---|
| poll | 結果の本文。JSON-RPC のエラーにはしない |
| push | `notifications/events/active`。最初と、途中で欠落が起きたときに送り、同じストリームで配信を続ける |
| webhook | 購読・延長の応答。延長の合間に欠落を見つけたときは `gap` の本文を POST する |

**購読の終了**: 主体のアクセス権が取り消されたときや、イベントの種類が削除されたり互換性を壊す形で変わったりしたとき、サーバーは購読を終わらせます。合図は、push では `notifications/events/terminated`、poll では次の `events/poll` への JSON-RPC のエラー、webhook では署名付きの `terminated` の本文で、どれも同じ形の `error` を持ちます。種類の削除では `NotFound`、互換性を壊す変更では `Unsupported` を使い、アクセス権は変わっていないので `Forbidden` にはしません。この場合、クライアントの SDK は認可の失敗とは扱わず、`events/list` を取り直して購読し直します。

**順序と配信の保証**: この拡張は、イベントの順序、ちょうど 1 回の配信、トランザクションの一貫性を、プロトコルとしては保証しません。用意するのは、再開のためのカーソル、購読の中での重複排除のための `eventId`、購読ごとの順序（poll と push はサーバーが生み出した順。webhook はイベントごとに再試行されるためベストエフォート）、そして上流が永続的でクライアントが最後のカーソルから再開する場合の「少なくとも 1 回」の配信です。カーソルで辿れる履歴が上流に無く、受け取ったイベントを `server.emit()` で流すだけの種類（emit-only）は、サーバーの再起動をまたぐと「高々 1 回」になります。購読をまたいだ順序は、どの方式でも保証されません。

- [SEP-3415: Events Extension - MCP Docs](https://modelcontextprotocol.io/seps/3415-events-extension#cursor-lifecycle)
- [SEP-3415: Events Extension - MCP Docs](https://modelcontextprotocol.io/seps/3415-events-extension#ordering-and-delivery-guarantees)

## 5. 汎用のエラーコード 5 つとルーティング用のヘッダーが盛り込まれた

**エラー処理**: SEP-3415 が使うエラーは次の 6 つで、`InvalidParams` 以外の 5 つが新しいコードです。

| 名前 | コード | 意味 |
|---|---|---|
| `InvalidParams` | `-32602` | リクエストが静的に不正。引数が `inputSchema` に合わない、`delivery.url` が不正か `https` でない、`delivery.secret` が正しい `whsec_` の値でない。標準の JSON-RPC のコード |
| `NotFound` | `-32023` | 参照先が無い。未知のイベント名や、`events/unsubscribe` でキーに合う購読が無い場合。`data.kind`（`"event"` か `"subscription"`）で区別してよい |
| `Forbidden` | `-32024` | 認証済みの主体に、このイベントと引数の組み合わせが許されていない、またはアクセス権が取り消された |
| `ResourceExhausted` | `-32025` | サーバーの上限や割り当てに達した。`data.limit` がその名前（例: `"subscriptions"`） |
| `Unsupported` | `-32026` | 形式は正しいが、求めた機能やオプション（イベントの種類が提供しない配信方式など）に対応していない |
| `CallbackEndpointError` | `-32027` | クライアントが渡したコールバックのエンドポイントが確認に失敗したか、到達できなかった（webhook だけ）。`data.reason` は `lastError` の分類のいずれか |

新しい 5 つはイベント専用ではなく、MCP 全体で使い回せる汎用のコードとして名付けられ、詳細は型付きの `data` で伝えます。Rationale によると、以前の草案ではイベント専用のコードを 7 つ作っていました。コードの割り当てについては、コア仕様が JSON-RPC の実装定義の範囲を分けており、`-32000`〜`-32019` は実装に任せて仕様では定義せず、`-32020`〜`-32099` は仕様が順に割り当てる、と説明しています。SEP-3415 はその次の 5 つを求めるもので、表の番号は、採択の時点で割り当て済みのコードが `-32020`〜`-32022` だけであることを前提にした、採択までの暫定のものとされています。新しいコードを割り当てるか、`InvalidParams` に型付きの `data` を付ける形にまとめるかは、Open Questions にも挙がっています。

**Streamable HTTP のルーティング用ヘッダー**: `events/poll`・`events/stream`・`events/subscribe`・`events/unsubscribe` を Streamable HTTP で送るとき、クライアントは `Mcp-Name` ヘッダー（SEP-2243 で定義）に `params.name`（イベント名）を入れなければなりません（MUST）。コアのプロトコルが `tools/call` や `prompts/get` に使うのと同じ扱いで、中継やロードバランサーが本文を解析せずにイベントの種類で振り分けや流量制限をできるようにするためです。`params.name` を持たない `events/list` には `Mcp-Name` を付けません。また、サーバーはイベントの種類の `inputSchema` のプロパティに、ツールの引数と同じ `x-mcp-header` の注釈を付けてよく（MAY）、Streamable HTTP のクライアントは、値のある注釈付きの引数ごとに `Mcp-Param-{Name}` ヘッダーを付けなければなりません（MUST）。ヘッダーが本文と合わなければ、サーバーは HTTP `400 Bad Request` と `HeaderMismatch`（`-32020`）で拒否します。

**予約**: `events/` のメソッドの接頭辞と `notifications/events/` の通知の接頭辞、`io.modelcontextprotocol/events` のラベル、`subscriptions/listen` の通知フィルタの `eventsListChanged` フィールド、HTTP ヘッダーの `X-MCP-Subscription-Id` と well-known のパス `/.well-known/mcp-webhook-receiver.json` が、この拡張のために予約されています。

- [SEP-3415: Events Extension - MCP Docs](https://modelcontextprotocol.io/seps/3415-events-extension#error-handling)
- [SEP-3415: Events Extension - MCP Docs](https://modelcontextprotocol.io/seps/3415-events-extension#streamable-http-routing-headers)
- [SEP-3415: Events Extension - MCP Docs](https://modelcontextprotocol.io/seps/3415-events-extension#reservations)

## 新規追加されたページ

<!-- light:new-pages:start -->
- [**SEP-3415: Events Extension**](#1-sep-3415-events-extension) ([MCP Docs](https://modelcontextprotocol.io/seps/3415-events-extension)):  
  MCP クライアントが外部のシステムの出来事を購読するための Events 拡張を定める Extensions Track の SEP（Final、作成 2026年10月05日、1,284 行）。索引 `llms.txt` にもエントリが加わった（詳細はハイライト 1〜5 参照）。
<!-- light:new-pages:end -->

## 1. SEP-3415: Events Extension

SEP-3415 は 1,284 行のページで、タイトルを除く見出しは 62 個（`##` が 10・`###` が 30・`####` が 22）です。Abstract・Motivation・Specification（Extension Identifier から Reservations まで 16 の節）・Rationale・Backward Compatibility・Security Implications・Reference Implementation・Open Questions と、付録の Appendix A（SDK の指針）・Appendix B（GitHub を例にした通しの例）から成ります。本文 `llms-full.txt` ではファイルの末尾（それまで最後だった SEP-3398 の後ろ）に、索引 `llms.txt` では SEP-3392 と SEP-3398 の間に、SEP の索引ページの表では先頭の行に置かれています。仕様の中身はハイライト 1〜5 で扱ったので、ここではそれ以外の要点をまとめます。

**動機（Motivation）**: MCP は要求駆動で、誰も尋ねていないときに起きること（新着メール、リポジトリへの push、本番のインシデントなど）にエージェントが応じる必要が増えているのに、サーバーが「何を監視でき、どの引数で、何が届くか」を示す標準の方法がありません。既存の通知は、URI やリストが変わったことを伝えるだけで引数もデータも持たず、開いた `subscriptions/listen` のストリームでしか届かず、カーソルが無いので切断中の出来事は失われる、と説明しています。また、接続を保てないステートレスなサーバー、公開のエンドポイントを持てない NAT の内側のクライアント、poll すべきでない電池やコストに敏感なクライアントと、イベントを必要とする配備がばらばらなので、配信方式を 3 つ定めたとしています。SEP-1686（Tasks）が将来の検討事項として webhook 形式の完了通知を挙げていたことにも触れています。

**設計の根拠（Rationale）**: 主な判断は次のとおりです。

- 配信方式を 3 つにするのは「1 つのことに 1 つのやり方」という MCP の通常の姿勢に反し、仕様と SDK の面がおよそ 3 倍になるが、どれを外しても実際の利用者を取り残すため、その費用を払う。1 つの方式だけを定めて残りをプロキシで合成する案は退けた
- push は `subscriptions/listen` のフィルタ（Tasks 拡張の `taskIds` のような形）ではなく、専用の `events/stream` にした。購読ごとに引数・カーソル・確認・欠落の合図・終了のエラーがあり、共有のストリームに載せると項目ごとのエラーの振り分けや部分的な失敗が戻ってくるため
- `events/poll` と `events/stream` は 1 リクエストに 1 購読で、まとめ送りは HTTP/2 の多重化などトランスポートに任せる
- リソースの購読を拡張するのではなく、新しい `events/*` のプリミティブにした
- プロトコルとしてのフロー制御は設けない。ボトルネックは LLM の推論で、TCP のフロー制御、サーバーによる頻度の制御、クライアント側の優先度付けで足りるとする。push で古いカーソルから再接続したときの大量の再生は、既知の課題として挙げている
- webhook は Standard Webhooks をプロファイルとして採用し、既製の検証ライブラリを使えるようにした

**既存の仕組みとの関係と対象外**: `notifications/resources/updated` は変えず、イベントとツールはアプリケーションの層で組み合わせ（イベントを受けたエージェントがツールを呼ぶなど）、イベントを受けてモデルを呼ぶかどうかはクライアントが決めます。SEP-2495（Event-Driven Tool Invocation）とは補い合う関係としています。この版で対象外とするのは、購読より前からの再生、個々のメッセージキュー（SQS・MQTT・Kafka・Pub/Sub など）との結び付け、引数の複雑な問い合わせ言語、サーバーをまたぐイベントの振り分け、イベントに結び付いたプロンプト、配信の保証、イベントのスキーマのバージョン管理の 7 つです。

**後方互換性**: 拡張は追加だけで、既存のメッセージは変えません。リビジョン `2025-11-25` 以前では定義されません。この SEP に先立つ設計の試作はトップレベルの `events` capability を広告しており、少なくとも 1 つの配備済みのクライアントがそれを読むが、そのキーはこの拡張の一部ではない、と明記しています。

**セキュリティ**: Threat model の表は 14 の脅威（イベントのデータを通じたプロンプトインジェクション、SSRF と DNS rebinding、被害者の URL を購読させる反射・増幅型の DDoS、配信の偽造、秘密鍵の漏洩、テナントをまたいだ購読の改ざんなど）と、それぞれへの対策を挙げています。イベントのデータはツールの結果と同じ注意で扱わなければならず（MUST）、サーバーはデータを最小限（送り主・件名・メッセージ ID のような仕分けに足る項目）に保つべき（SHOULD）とされています。認可は 3 段階で、購読時（呼び出しが認証されていれば権限を確かめなければならない。MUST）、配信時（定期的に確かめ直すべき。SHOULD）、行動時（イベントを受け取っても行動の権限にはならず、エージェントの応答は通常の MCP の認可を通る）です。

**参照実装（Reference Implementation）**: 次の 4 つが挙がっています。公式 TypeScript SDK の [typescript-sdk#3209](https://github.com/modelcontextprotocol/typescript-sdk/pull/3209)（サーバーとクライアントの両方を、3 つの配信方式すべてについて、実験的な `ext/events` のサブパスで実装。レビュー中）、Python SDK をフォークせずにその上で `events/list`・`events/subscribe`・署名付きの webhook 配信を加えた `mcp-webhook-events`（`modelcontextprotocol` の組織の外のリポジトリ）とその相互運用の報告、レビューを受け付けている conformance のスイート（[conformance#521](https://github.com/modelcontextprotocol/conformance/pull/521) のサーバーの 5 シナリオと、その上に積んだ [conformance#541](https://github.com/modelcontextprotocol/conformance/pull/541) のクライアントの 4 シナリオ）、stdio での再起動からの回復についての報告です。

**未解決の問い（Open Questions）**: 6 つあり、クライアントの SDK がイベントをエージェントのフレームワークにどう見せるか、リソースの購読と `list_changed` の通知をイベントとして表し直すか、1 つの購読で複数のイベント名を 1 つのカーソルで扱えるようにするか（採用すると通信上の互換性が壊れる）、タスクの状態の変化をイベントとして出すか、エラーコードを新しく割り当てるか、ストリームの生存確認をコアのプロトコルへ移すか、です。

**付録**: Appendix A（規範ではない SDK の指針）は、サーバーの作者が「カーソル以降の変化を調べる」関数を 1 つ書けば SDK が 3 つの方式すべての配信を受け持つ形を示し、Python の擬似コードで、`@server.event`、`server.emit()` による一斉配信（購読ごとの `match` と `transform` のフック）と特定の購読への配信、カーソルで辿れる履歴が上流に無い種類のためのメモリ上のリングバッファ（`emit_only=True`）、購読の追加と削除のフック（`on_subscribe` と `on_unsubscribe`）、poll の購読をリース（`poll_subscription_ttl`）として扱う方法などを説明しています。クライアントの SDK は、使える方式のうち webhook・push・poll の順に選び、どれも使えなければ `NoCompatibleDeliveryMode` を送出するとしています。Appendix B は、GitHub の API を包む MCP サーバーが、GitHub のリポジトリの webhook で受けたプルリクエストの出来事を MCP の webhook でフォワードプロキシへ届け、プロキシが poll か push でクライアントに渡す構成を、シーケンス図で通しで示しています（図の Redis は例示で、規範ではない）。

- [SEP-3415: Events Extension - MCP Docs](https://modelcontextprotocol.io/seps/3415-events-extension#motivation)
- [SEP-3415: Events Extension - MCP Docs](https://modelcontextprotocol.io/seps/3415-events-extension#rationale)

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
今回の対象期間に大幅な更新（本文 50 行以上の変更）があった既存ページはありません。既存ページで差分が出たのは SEP の索引ページ（追加 2 行・削除 1 行）だけで、「軽微な更新」で扱います。
<!-- light:updated-pages:end -->

## 軽微な更新

<!-- light:minor-updates:start -->
今回差分が出たファイルは `llms.txt` と `llms-full.txt` の 2 件で、新規ページ（SEP-3415）のほかに、次の変更がありました。

**その他**

- Specification Enhancement Proposals (SEPs) の索引ページで、Summary の Final を 44 件から 45 件にし、並びを Accepted・Final の順から Final・Accepted の順に変えた。All SEPs の表の先頭（SEP-3398 の前）に SEP-3415 の行（Events Extension・Final・Extensions Track・作成 2026年10月05日）を追加。表は 46 行（Final 45・Accepted 1）で、Summary の件数と一致する — [Specification Enhancement Proposals (SEPs)](https://modelcontextprotocol.io/seps/index#all-seps)
- 索引 `llms.txt` の SEP の一覧で、SEP-3392: Extension Lifecycle の次（SEP-3398: Release Cycle Updates の前）に SEP-3415: Events Extension のエントリを追加。エントリ数は 362 件から 363 件（一意の URL も 363 件）、ファイルは 367 行から 368 行になった（末尾に改行が無いため、改行の数では 366 から 367） — [SEP-3415: Events Extension](https://modelcontextprotocol.io/seps/3415-events-extension)
<!-- light:minor-updates:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-11-18.md](./archives/latest/2026-11-18.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-11-18.md](./archives/latest-detail/2026-11-18.md)

<!--
base_commit: 831f1678213f7b2708b300fbfd4e73aa7b6ac427
head_commit: 2864b8c8e49e5201a3575b16751cc5caf78f4b1c
generated_at_full: 2026-11-20T15:41:02+09:00
-->
