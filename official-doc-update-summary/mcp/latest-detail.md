---
対象期間: 2026年08月15日 〜 2026年08月21日
作成日: 2026-08-21
---

# MCP 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
今回の対象期間に本文が変わったのは 6 ページで、その中心は Authorization Interest Group の再チャーターをはじめとするコミュニティ運営文書の改訂です。認可まわりの Discord チャンネル 6 本と Enterprise-Managed Authorization IG が `#auth-ig` 1 本に集約され、あわせて SEP の Final 化要件の見直し、Rust SDK の Tier 1 昇格、Subscriptions の応答記述の修正が入りました。

主要なものを以下に挙げます。

1. Authorization Interest Group が再チャーターされ、`#auth-wg-*` の 6 チャンネルと Enterprise-Managed Authorization IG が `#auth-ig` 1 本に統合された（定例コールもアジェンダ駆動に変更）
2. SEP の Final 化要件が見直され、仕様変更（スキーマ・仕様本文・changelog エントリ）は SEP の PR 自体に含める形になり、SDK 実装は Final の要件から外れた
3. Rust SDK が Tier 2 から Tier 1 に昇格し、Tier 1 は TypeScript / Python / C# / Go / Rust の 5 つになった
4. Subscriptions のグレースフルクローズで返す応答の記述が「空の結果」から「完了結果」に改められ、標準の result フィールドとサブスクリプションのメタデータを含むことが明示された
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**Authorization Interest Group の再チャーターと認可関連チャンネルの統合**](#1-authorization-interest-group-の再チャーターと認可関連チャンネルの統合):  
  Authorization IG の charter が 2026年08月17日付で全面改訂され、「問題を育てて Working Group を切り出す」インキュベーター型から「認可作業の唯一のチャーター済みの場」へ位置づけが変わった。`#auth-wg-*` の 6 チャンネルは読み取り専用でアーカイブされ、Enterprise-Managed Authorization IG も同じ形で吸収されて、議論はすべて `#auth-ig` のトピック別スレッドに集約される。隔週 45 分の定例はアジェンダ駆動になり、アジェンダが集まらない回は中止される。
2. [**SEP の Final 化要件が見直され SDK 実装は不要に**](#2-sep-の-final-化要件が見直され-sdk-実装は不要に):  
  SEP Guidelines の Finalization 手順が書き換えられ、受理後に著者が仕様変更（スキーマ変更・仕様本文・changelog エントリ）を SEP の PR そのものに追加する形になった。SDK 実装は SEP が `final` になるための要件ではないと明記され、作業が完了した時点でスポンサーがステータスを `final` に更新し PR をマージできる。conformance test の要件自体は従来どおりで変更はない。
3. [**Rust SDK が Tier 1 に昇格**](#3-rust-sdk-が-tier-1-に昇格):  
  SDKs ページの一覧で Rust SDK のバッジが Tier 2 から Tier 1 になり、表内の位置も Tier 1 グループの末尾（Go の下）へ移動した。これで Tier 1 は TypeScript / Python / C# / Go / Rust の 5 つになり、Java と Ruby が Tier 2、Swift / PHP / Kotlin が Tier 3 という構成になる。
4. [**Subscriptions のグレースフルクローズ応答の記述修正**](#4-subscriptions-のグレースフルクローズ応答の記述修正):  
  サーバー側からサブスクリプションを終了する際に返す応答が、「空の結果（empty result）」から「完了結果（completion result）」という表現に改められ、標準の result フィールドとサブスクリプションのメタデータ以外にメソッド固有のデータを持たない、という説明が加わった。同じ節のサンプル JSON は変更前から `"resultType": "complete"` と `_meta` を含んでおり、本文の記述をその実体に合わせた修正となる。
<!-- light:highlight-list:end -->

## 1. Authorization Interest Group の再チャーターと認可関連チャンネルの統合

MCP の認可を扱う Authorization Interest Group の charter が 2026年08月17日付で全面改訂されました。旧版のミッションは「実装者・IdP ベンダー・セキュリティ実務者が実世界の認可課題を持ち寄る場を提供し、ユースケースを集め、現行の OAuth 2.1 ベース認可仕様のギャップを文書化し、検証済みの問題を十分にスコープが固まるまで温めたうえで、標準のグループ作成プロセスを通じて focused な Working Group を提案する」というインキュベーター型のものでした。新版では「MCP の認可作業における唯一のチャーター済みの場（the single chartered venue）」と定義され、実世界の問題を洗い出し、それが解く価値のある問題か・MCP に属する問題かを判断し、著者が SEP や [ext-auth](https://github.com/modelcontextprotocol/ext-auth) のドラフト・プロトタイプ・デプロイ結果を持ち込んで横断的なフィードバックを受けられる場にする、という役割になっています。charter 本文は「議論とラフコンセンサスは 1 つのチャンネルと 1 つの定例コールで行い、成果物は新しい常設グループではなくドラフトとデモである」と明言しています。

もっとも目に見える変更が Discord チャンネルの統合です。`#auth-wg-client-registration`（動的クライアント登録）、`#auth-wg-mixup-protection`（認可サーバーの mix-up・トークンオーディエンス混同の緩和）、`#auth-wg-profiles`（Client Credentials・Enterprise-Managed Authorization・DPoP・Workload Identity Federation の各拡張）、`#auth-wg-tool-scopes`（ツール単位のスコープ提示・ステップアップ認可）、`#auth-wg-fine-grained-authz`（Rich Authorization Requests・構造化された拒否・修復ヒント）、`#auth-wg-improve-devx`（規範仕様の外側のベストプラクティスとチュートリアル）の 6 チャンネルが、この再チャーターをもって読み取り専用でアーカイブされました。旧版が「Working Group」の一覧表（Status と Charter の列を持ち、Tool Scopes と Fine-Grained Authorization が Active、他は Completed）だったのに対し、新版は「Former channel / Topic / State at consolidation / Continues as」の対照表になっており、統合時点で Active だった Tool Scopes は `#auth-ig` のスレッドへ、Fine-Grained Authorization は `#auth-ig` の SEP-2643 / fine-grained authorization スレッドへ、Profiles は DPoP と Workload Identity Federation のスレッドへ引き継がれると記載されています。Improve DevX の状態は旧表の Completed から Dormant に改められました。Enterprise-Managed Authorization IG も同じ扱いで吸収され、`#enterprise-managed-auth-ig` はアーカイブ、EMA の相互運用・デプロイの進捗は Auth IG コールの発表枠として持ち込む形になります。

運用ルールも書き換わりました。定例は「Discussion Call」から「Auth IG Call」に改称され、隔週 45 分という枠は据え置きですが、目的が「ユースケース共有・問題のトリアージ・WG 提案の決定」からアジェンダ駆動（問題の売り込み、SEP やドラフトの進捗、デモ、デプロイ報告）に変わりました。ファシリテーターが各コールの前に `#auth-ig` にアジェンダスレッドを立て、参加者はトピック・求めるもの（フィードバック / 決定 / 周知）・所要時間を返信して枠を要求します。アジェンダが薄ければその回は中止し、枠は次回に回されます。スコープ面では In Scope に「拡張の相互運用レポート」と「SEP およびドラフトへのフィードバック」が加わった一方、旧版にあった「Working Group の提案」が削除され、代わりに Out of Scope の先頭に「SEP や拡張の受理」が置かれました（IG はフィードバックと支持の表明までで、スポンサーシップと受理は Maintainers・Core Maintainers に残る）。問題の持ち込みに対しては「これは解く価値のある問題か」「その居場所はここか（コア仕様か、ext-auth の公式拡張か、非公式拡張か、上流の標準化団体か）」の 2 つの定型質問が必ず問われ、両方が Yes のときに通常の SEP プロセスへ進みます。トピックごとにサブグループやチャンネル、会議シリーズを作ることはせず、独自の意思決定権が本当に必要な成果物についてのみ、例外として別途 Working Group を提案できる、という位置づけです。

- [Authorization Charter - MCP Docs](https://modelcontextprotocol.io/community/interest-groups/auth#consolidated-channels)
- [Enterprise-Managed Authorization Charter - MCP Docs](https://modelcontextprotocol.io/community/interest-groups/enterprise-managed-authorization#changelog)

## 2. SEP の Final 化要件が見直され SDK 実装は不要に

SEP（Specification Enhancement Proposal）が `final` に到達するまでの要件が書き換えられました。旧版の Step-by-Step Process の第 9 段階「Finalization」は「受理されたらリファレンス実装を完成させなければならない。観測可能なプロトコル挙動を持つ Standards Track SEP では conformance test のマージも必要。完成して仕様に取り込まれたら、スポンサーがステータスを `final` に更新する」という記述でした。新版では、リファレンス実装と conformance test の要件はそのままに、「著者が仕様変更（スキーマ変更・仕様本文・changelog エントリ）を SEP のプルリクエストに追加する」「SDK 実装は SEP が `final` になるための要件ではない」「この作業が完了した時点でスポンサーがステータスを `final` に更新し、SEP の PR をマージできる」という 3 点が加わっています。

同じ内容が「SEP Review & Resolution」節にも反映されました。旧版は「受理された後はリファレンス実装を完成させなければならず、完成してメインリポジトリに取り込まれた時点でステータスが Final に変わる」という 1 文でしたが、新版は「受理された後、著者が仕様変更（スキーマ変更・仕様本文・changelog エントリ）を SEP の PR に追加する。リファレンス実装は、必要な conformance test とあわせて完成させなければならない。SDK 実装は不要である。この作業が完了した時点でステータスが Final に変わり、PR をマージできる」と展開されています。受理の判定基準（プロトタイプ実装があること・MCP エコシステムへの明確な利益・コミュニティの支持とコンセンサス）自体は変わっていません。

要点は、仕様変更を別の PR に切り出すのではなく SEP の PR そのものが仕様変更の PR を兼ねること、そして SDK 実装の完了を待たずに SEP を Final にできることが明示された点です。なお conformance test の要件（観測可能なプロトコル挙動を持つ Standards Track SEP は conformance リポジトリへのシナリオのマージが必要、Process / Informational SEP と観測可能な挙動を持たないものは免除）は従来から存在するもので、今回の差分では変更されていません。

- [SEP Guidelines - MCP Docs](https://modelcontextprotocol.io/community/sep-guidelines#step-by-step-process)
- [SEP Guidelines - MCP Docs](https://modelcontextprotocol.io/community/sep-guidelines#sep-review--resolution)

## 3. Rust SDK が Tier 1 に昇格

SDKs ページの「Available SDKs」の一覧で、Rust SDK のバッジが Tier 2 から Tier 1 に変わりました。表内の行も移動しており、旧版では Tier 2 グループの Java と Ruby の間にあったものが、新版では Tier 1 グループの末尾（TypeScript / Python / C# / Go に続く 5 番目）に置かれています。この結果、Tier 1 は TypeScript / Python / C# / Go / Rust の 5 つ、Tier 2 は Java と Ruby の 2 つ、Tier 3 は Swift / PHP / Kotlin の 3 つという構成になりました。Java は Tier 2 のままで、今回動いたのは Rust の 1 行だけです。

SDK Tiering System によれば、Tier 1 は「非実験的な全機能と、sampling・elicitation のようなオプション機能を含む完全なプロトコル実装を備えた、フルサポートの SDK」と定義され、conformance test の 100% パス、新しいプロトコル機能への新仕様バージョンのリリース前の追従、2 営業日以内の issue トリアージ、7 日以内の重大バグ修正が求められます。Tier 2 は「完全なプロトコル仕様サポートに向けて作業中の、活発にメンテナンスされている SDK」で、conformance test は 80% パス、新機能への追従は 6 か月以内という水準です。今回の昇格は、Rust SDK がこの Tier 1 の水準を満たすと判断されたことを意味します。なお、今回の差分は SDKs ページの一覧表のみで、SDK Tiering System ページ側の Tier の定義や要件表には変更がありません。

- [SDKs - MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/sdk#available-sdks)
- [SDK Tiering System - MCP Docs](https://modelcontextprotocol.io/community/sdk-tiers#overview)

## 4. Subscriptions のグレースフルクローズ応答の記述修正

仕様 2026-07-28 の Subscriptions ページで、サーバーが自分の判断でサブスクリプションを終了する際（たとえばシャットダウン時）に返す応答の記述が修正されました。「Graceful Closure」節は、旧版では「元の `subscriptions/listen` リクエストに対して**空の結果（an empty result）**を返してからストリームを閉じる**べき（SHOULD）**」となっていましたが、新版では「**完了結果（a completion result）**を返してからストリームを閉じるべき」に変わり、「その結果は、標準の result フィールドとサブスクリプションのメタデータを超えるメソッド固有のデータを持たない」という 1 文が加わりました。あわせて「Cancellation」節の箇条書きも、サーバーがサブスクリプションを畳む場合の説明が「**空の** `subscriptions/listen` レスポンスを送るべき」から「**成功した** `subscriptions/listen` レスポンスを送るべき」に書き換えられています。

これは新しい機構の追加ではなく、記述と実体の食い違いの解消です。同じ節に置かれたサンプル JSON は変更前から `"result"` の中に `"resultType": "complete"` と `_meta` の `io.modelcontextprotocol/subscriptionId` を含んでおり、本文が言う「空の結果」とは整合していませんでした。今回の修正で本文がサンプルの実体に合わせられた形になります。SHOULD という規範性の強さ、応答が長命リクエストの `id` で対応付けられる JSON-RPC レスポンスであること、応答を伴わない突然のトランスポート切断と対比してグレースフルな終了を示すという位置づけ、そしてサンプル JSON 自体は変更されていません。

- [Subscriptions - MCP Docs](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/subscriptions#graceful-closure)
- [Subscriptions - MCP Docs](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/subscriptions#cancellation)

## 新規追加されたページ

<!-- light:new-pages:start -->
今回の対象期間に新規追加されたページはありません。掲載ページ数は対象期間の前後とも 144 件で変わっていません。
<!-- light:new-pages:end -->

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
- [**Authorization Charter**](#1-authorization-charter) ([MCP Docs](https://modelcontextprotocol.io/community/interest-groups/auth)):  
  Authorization Interest Group の charter が再チャーターされ、ミッション・スコープ・運営ルール・成果物の定義が全面的に書き換えられた。差分は 53 行の追加と 26 行の削除で、今回の対象期間で 50 行を超えた唯一のページ（詳細はハイライト 1 参照）。
<!-- light:updated-pages:end -->

## 1. Authorization Charter

MCP の認可 Interest Group の charter ページです。今回の再チャーターで変更が入ったのはページのほぼ全域にわたるため、ここではどのセクションが何に変わったかを整理します。各変更の意味と背景はハイライト 1 で扱っています。

- **Mission Statement**: 「問題を集めてギャップを文書化し、focused な Working Group を提案する」インキュベーター型の記述から、「認可作業における唯一のチャーター済みの場」であり「成果物は新しい常設グループではなくドラフトとデモ」という記述へ全面書き換え
- **Scope / In Scope**: 「拡張の相互運用レポート」（ext-auth 拡張の独立実装同士を IdP・クライアント・認可サーバーで突き合わせた結果）と「SEP およびドラフトへのフィードバック」の 2 項目を追加。「Working Group の提案」を削除。「スコープと権限の粒度」にスコープ文字列を超えた粒度（Rich Authorization Requests・構造化された拒否・修復ヒント）を追記し、「問題提起と要件」の共有先を GitHub Discussions への公開から `#auth-ig` スレッドと SEP のプルリクエストへ変更
- **Scope / Out of Scope**: 「SEP や拡張の受理」を先頭に追加。IdP ベンダーが報告する制約もデプロイ経験としてスコープ内である旨の記述を、認可サーバーに加えて IdP にも広げる形で調整
- **Scope / Related Groups**: Enterprise-Managed Authorization IG のエントリを削除し、代わりに Security IG（トークンオーディエンスの混同・issuer 検証・アカウント連携のリスクが両グループの境界にある）を追加。SDK Maintainers の項目に、SDK 横断の認可まわりのエルゴノミクスに加えて「デフォルト」も含める旨を追記
- **Membership**: IdP ベンダー・認可対応を出荷しているクライアント／サーバー実装者・エンタープライズ IdP と統合する運用者を特に求めている、という 1 文を追加。参加導線は Discord のトピック別スレッド中心に整理され、GitHub Discussions の Authorization カテゴリと該当 WG チャンネルへの直接投稿の案内を削除
- **Operations**: 定例の名称を「Discussion Call」から「Auth IG Call」へ改称し、目的をアジェンダ駆動の内容に変更。「One channel, threads per topic」「Agenda-driven calls」「From problem to SEP」の 3 セクションを新設し、旧「Working Group Incubation」セクションを削除
- **Deliverables & Success Metrics**: 成果物の定義を「WG を提案する」型から「通過したドラフトとデモ（IG のフィードバックが記録された SEP・ext-auth 仕様、リファレンス実装と conformance シナリオ、相互運用とデプロイのレポート、公開された議事録）」型へ書き換え。配下の Working Group 一覧表を「Consolidated channels」節とアーカイブ済みチャンネルの対照表に差し替え
- **Changelog**: 2026年08月17日付で「Re-charter: single venue and channel for authorization work; agenda-driven calls; SEP feedback in scope; `#auth-wg-*` channels and the Enterprise-Managed Authorization IG folded in」の行を追加

Leadership 節のファシリテーター 3 名（Aaron Parecki / Darin McAdams / Paul Carleton）と Group Type（Interest Group）、Discord チャンネル `#auth-ig` の URL は変更されていません。定例の頻度（隔週）と所要時間（45 分）も据え置きです。

- [Authorization Charter - MCP Docs](https://modelcontextprotocol.io/community/interest-groups/auth#mission-statement)

## 軽微な更新

<!-- light:minor-updates:start -->
今回差分が出たファイルは `llms-full.txt` の 1 件のみで、索引ファイル `llms.txt` は掲載 144 件のエントリ・並び順とも変更がありません。本文が変わった 6 ページのうち、上記の Authorization Charter を除く 5 ページは以下のとおりです。

**機能改善**

- SDKs: Rust SDK の Tier バッジが Tier 2 から Tier 1 になり、表内の並びも Tier 1 グループへ移動した（詳細はハイライト 3 参照） — [SDKs - MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/sdk#available-sdks)
- Subscriptions: サーバー主導でサブスクリプションを終了する際に返す応答の記述が、「空の結果」から「完了結果」に修正された（詳細はハイライト 4 参照） — [Subscriptions - MCP Docs](https://modelcontextprotocol.io/specification/2026-07-28/basic/patterns/subscriptions#graceful-closure)
- SEP Guidelines: Final 化の手順が書き換えられ、仕様変更を SEP の PR に含めること・SDK 実装は不要であることが明記された（詳細はハイライト 2 参照） — [SEP Guidelines - MCP Docs](https://modelcontextprotocol.io/community/sep-guidelines#step-by-step-process)
- Working and Interest Groups: Working Group の設立要件が、`docs/community/working-groups/<name>/overview.mdx` を追加する PR（Maintainers 承認）と charter を追加する PR（Core Maintainers 承認）の 2 本立てから、charter を `docs/community/working-groups/<name>.mdx` として追加する PR 1 本に一本化された。この PR は Group Charter Template に沿って書き、`docs/docs.json` への対応するナビゲーションエントリを含める必要があり、CODEOWNERS で Core Maintainers の承認が必須となる。Interest Group 側も、スポンサーが付いた後にファシリテーターが charter を作る手順が「charter を作成する」だけの記述から、同じテンプレートに沿った `docs/community/interest-groups/<name>.mdx` を追加する PR として提出し、ナビゲーションエントリを含め Core Maintainers の承認を得る、という具体的な手順に置き換えられた — [Working and Interest Groups - MCP Docs](https://modelcontextprotocol.io/community/working-interest-groups#lifecycle)

**その他**

- Enterprise-Managed Authorization Charter: ページ冒頭に、2026年08月17日をもって当 Interest Group が Authorization IG に統合された旨の注記が追加された。EMA の相互運用とデプロイの進捗は Auth IG コールのアジェンダ枠で発表し、議論は `#auth-ig` のスレッドで継続、`#enterprise-managed-auth-ig` はアーカイブされる。ページ自体は参照用として残される。あわせて changelog に 2026年08月17日「Folded into the Authorization IG; channel archived」の行が追加された（詳細はハイライト 1 参照） — [Enterprise-Managed Authorization Charter - MCP Docs](https://modelcontextprotocol.io/community/interest-groups/enterprise-managed-authorization#changelog)
<!-- light:minor-updates:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-08-15.md](./archives/latest/2026-08-15.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-08-15.md](./archives/latest-detail/2026-08-15.md)

<!--
base_commit: eda93f08dd15ec44722c9febe8803506e487e524
head_commit: d2a47b6c691946fa1f35bf733b795510e9048022
generated_at_full: 2026-08-22T15:45:02+09:00
-->
