---
対象期間: 2026年08月30日 〜 2026年08月31日
作成日: 2026-08-31
---

# MCP 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
今回の対象期間の差分はページ本文を収める `llms-full.txt` のみで、索引 `llms.txt` には変更がありません（エントリは 349 件のまま）。内訳は追加 163 行・削除 1 行で、Cargo（Rust）パッケージ対応の追記・Enterprise Interest Group charter 本文の収録・SEP の誤字修正の 3 件です。

主要なものを以下に挙げます。

1. MCP Registry の対応パッケージ種別に Cargo が加わり、`server.json` で `"registryType": "cargo"` を指定できるようになった。対応レジストリは crates.io のみで、`npx` / `uvx` / `dnx` に相当する都度実行ランナーが無いため、`cargo install` で 1 回インストールした後はバイナリ名で直接起動する
2. Cargo の所有権検証では `mcp-name:` トークンを README に可視テキストとして書く必要がある。crates.io は markdown→HTML 変換で HTML コメントを除去するため、PyPI / NuGet で使える `<!-- mcp-name: ... -->` の隠しコメント形式は cargo では通らない
3. 前回索引にだけ現れていた Enterprise Interest Group の charter 本文が収録された。企業が MCP を本番投入する際に残るプロトコルレベルの要件ギャップを洗い出し、該当 Working Group へ渡すことを役割とする Interest Group で、SEP の執筆自体はスコープ外
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**MCP Registry が Cargo パッケージに対応**](#1-mcp-registry-が-cargo-パッケージに対応):  
  `registry/package-types` に `## Cargo (Rust) Packages` セクションが新設され、`server.json` の `packages` で `"registryType": "cargo"` を使えるようになった。対応レジストリは公式の crates.io のみ。Rust 著者向けの配布経路は cargo（ソース配布・利用者に Rust ツールチェーンが必要）と mcpb（ビルド済みバイナリ・ツールチェーン不要）の 2 本立てとして整理されている。
2. [**Cargo の所有権検証は可視テキストのトークンが必須**](#2-cargo-の所有権検証は可視テキストのトークンが必須):  
  検証は README を HTML 化したものに `mcp-name: $SERVER_NAME` 文字列が存在するかで行われる。crates.io は markdown→HTML 変換で HTML コメントを除去するため、PyPI / NuGet で通用する `<!-- mcp-name: ... -->` の隠しコメント形式は cargo では機能しない。可視の markdown テキストとして書く必要がある。
3. [**Enterprise Interest Group charter の本文が公開**](#3-enterprise-interest-group-charter-の本文が公開):  
  前回は索引の 1 行だけだった charter の本文 111 行が `llms-full.txt` に収録された。認証統合・アイデンティティ伝播・監査・ゲートウェイ挙動といった領域で、企業導入時に残るプロトコルレベルの要件ギャップを問題提起と推奨にまとめ、該当 Working Group へ渡すことを中核の役割としている。
<!-- light:highlight-list:end -->

## 1. MCP Registry が Cargo パッケージに対応

`registry/package-types` ページに `## Cargo (Rust) Packages` セクションが 51 行追加されました。対応するのは公式の crates.io レジストリ（`https://crates.io`）のみで、`server.json` の `packages` エントリに `"registryType": "cargo"` を指定します。ドキュメントの例では identifier に crate 名 `widget-mcp`、version に `0.3.0`、transport に `stdio` を置いた最小構成が示されています。この追加により、本ページが列挙する対応パッケージ種別は npm / PyPI / NuGet / Cargo / Docker・OCI / MCPB の 6 種になりました。

新設された `### Runtime Model` 小節は、Cargo のランタイムモデルが npm / PyPI / NuGet と異なる点を明示しています。`cargo install <crate>` はコンパイル済みバイナリを `~/.cargo/bin` に置いて PATH に通し、以降 MCP クライアントはバイナリ名で直接起動します。`npx`（npm）・`uvx`（PyPI）・`dnx`（NuGet、.NET 10 SDK Preview 6 以降）のような呼び出しごとのランナーに相当するものが無く、インストールは 1 回きり・実行はバイナリ名という形になります。上記の例が `runtimeHint` を持たないのはこの理由によるもので、意図的な省略であると本文に断りがあります。

そのうえで、Rust 製 MCP サーバーの配布には 2 つの一級の経路があると整理されています。ひとつは `registryType: cargo` による crates.io 経由のソース配布で、利用者側に `cargo install` を実行するための Rust ツールチェーン（`rustup`）が必要になる代わりに、Rust の CLI が通常公開される形と揃い、エコシステムの慣習に沿います。もうひとつは `registryType: mcpb` による GitHub / GitLab Releases 経由のビルド済みバイナリ配布で、利用者にツールチェーンを要求しません。「ツールチェーン不要」を優先するならこちらが適切で、どちらを選ぶかは著者の判断とされています。Cargo のネイティブ対応が用意されたのは、ソース配布を好む Rust 著者が MCPB でバイナリを固める回避策を強いられないようにするため、と説明されています。

- [MCP Registry Supported Package Types - MCP Docs](https://modelcontextprotocol.io/registry/package-types#cargo-rust-packages)

## 2. Cargo の所有権検証は可視テキストのトークンが必須

MCP Registry は Cargo パッケージの所有権を、パッケージの README に `mcp-name: $SERVER_NAME` という文字列が存在するかどうかで検証します。README は HTML にレンダリングされて crates.io の静的 CDN から配信されるため、検証器はその HTML を見ます。`$SERVER_NAME` の部分は `server.json` のサーバー名と一致していなければなりません（**MUST**）。

ここに Cargo 固有の落とし穴があるとして、本文が明示的に警告しています。PyPI と NuGet は README のレンダリング時に HTML コメントを保持するのに対し、crates.io は markdown から HTML への変換時に HTML コメントを除去します。したがって PyPI / NuGet では機能する `<!-- mcp-name: ... -->` という隠しコメント形式は cargo では機能せず、検証器が調べる HTML にトークンが現れません。Cargo の著者は `mcp-name:` トークンを可視の markdown テキストとして含める必要があり、推奨パターンとして Links セクションに「MCP Registry name:」に続けて `mcp-name: io.github.username/widget-mcp` を書いた単純な箇条書きを置く形が示されています。既存の npm / PyPI / NuGet / Docker・OCI / MCPB 各節の記述には変更がないため、この非対称性は Cargo 節の側にだけ注記されている状態です。

- [MCP Registry Supported Package Types - MCP Docs](https://modelcontextprotocol.io/registry/package-types#cargo-rust-packages)

## 3. Enterprise Interest Group charter の本文が公開

前回の対象期間（2026年08月26日〜30日）には索引 `llms.txt` に `community/interest-groups/enterprise` の 1 行が加わっただけで、本文は `llms-full.txt` に未収録でした。今回その本文 111 行が収録され、charter の中身が入力から確認できるようになりました。前回サマリで Transports Charter の前例として挙げた「索引が先・本文が後」というパターンが、このページでも同じように成立した形です。

グループ種別は Interest Group です。ミッションは、企業が MCP を本番環境に展開する際にぶつかる要件ギャップを特定し文書化することとされています。規制産業や大規模組織へ MCP の採用が広がるなかで、認証統合、アイデンティティ伝播、監査とコンプライアンス、ゲートウェイ挙動、スケーラビリティと回復性、構成管理といった領域に、まだプロトコルレベルで手当てされていないギャップが繰り返し現れている、というのが出発点です。企業の実務者を集めてこれらのギャップを問題提起と構造化された推奨として捉え、仕様策定を担う該当 Working Group へ流すことを役割とします。ガバナンスやベストプラクティスのパターンは議論から派生しうるものの、中核の任務はあくまでプロトコルレベルの要件を surfacing することであり、汎用のベストプラクティス集を維持することではないと明記されています。あわせて、議論とセッションはプロトコル中心かつベンダー中立であり、製品の売り込みやベンダー固有のマーケティングの場ではないこと、参加者は商用ソリューションを推す代表者としてではなく展開経験と要件を共有する実務者として貢献することが述べられています。

- [Enterprise Interest Group Charter - MCP Docs](https://modelcontextprotocol.io/community/interest-groups/enterprise#mission-statement)

## 新規追加されたページ

<!-- light:new-pages:start -->
今回本文が収録されたページは次の 1 件です。

- [**Enterprise Interest Group Charter**](#1-enterprise-interest-group-charter) ([MCP Docs](https://modelcontextprotocol.io/community/interest-groups/enterprise#scope)):  
  MCP Enterprise Interest Group の charter。スコープ・関連グループ・体制・運営・意思決定プロセス・成果物の各節を備え、ファシリテーター 2 名と参加者 11 名が名を連ねる。SEP の執筆自体はスコープ外で、成果は問題提起・ユースケース・推奨までとされる（ミッションの詳細はハイライト 3 参照）。
<!-- light:new-pages:end -->

## 1. Enterprise Interest Group Charter

In Scope として最上位に置かれているのは、包括的な焦点である「Enterprise Requirements Gaps」です。今日 MCP のプロトコルレベルで手当てされていない企業導入要件を特定し、該当 Working Group 向けの問題提起と推奨に変えることを主たる任務とし、各要件は痛点だけでなくそれが表す企業側の機会とセットで記録するとされています。ギャップを埋めることこそが企業導入の裾野と価値を広げる、という理由づけです。以下の個別領域はいずれもこのレンズを通して扱われ、ガバナンスやベストプラクティスのパターンはプロトコルレベルのギャップが浮かび上がる範囲でのみ文書化されます。

個別領域は次のように並びます。**Enterprise Authentication and Identity** では IdP 統合（SSO・SAML・OIDC）、トークンのライフサイクル管理、On-Behalf-Of（OBO）トークン交換フロー、細粒度認可（Rich Authorization Requests）を扱い、要件を Auth WG と関連 SEP への入力としてまとめます。**Identity Propagation and Session Context** は、検証済みのアイデンティティをクライアント・サーバー・下流サービスにまたがってどう提示・伝達し、ポリシー適用と監査に使うかを定義する領域で、spawned-agent / delegated-agent のユースケース（アイデンティティの系譜、子エージェントへの最小権限、子孫の失効、マルチエージェント連鎖での監査可能性）を含みます。認証に隣接しつつ焦点は別だと位置づけられています。**Audit, Observability, and Compliance** は MCP のツール呼び出しに対する監査証跡フォーマットの標準化、企業の SIEM・可観測性基盤との統合、コンプライアンス枠組（SOC 2・HIPAA・GDPR・EU AI Act）向けの証跡生成を対象とし、医療環境における PHI の取り扱いや BAA スコープのデータフローといった業種固有のパターンも含みます。

インフラ寄りの領域では、2026年07月28日リリース（仕様リビジョン識別子 `2026-07-28`）でプロトコルコアがステートレスへ移行したことが焦点の置き換えとして反映されています。**Gateway and Proxy Behavior** は API ゲートウェイ・ロードバランサー・リバースプロキシ・セキュリティプロキシを MCP トラフィックが経由する展開パターンを扱いますが、関心はセッションアフィニティからステートレスモデルでも残るギャップ、すなわちヘッダとコンテキストの伝播、プロキシをまたぐ認可の受け渡し、ゲートウェイでのポリシー適用へ移ったとされます。**Scalability and Resilience** も同様に、ステートレスコアによってスティッキーセッション無しでの水平スケールが可能になったため、フェイルオーバー・負荷分散・ミッションクリティカルな展開の信頼性に焦点があると整理されています。残る領域は、既存ミドルウェア・データ基盤・エージェントオーケストレーション層との統合を含む **MCP in Enterprise Architecture**、異種クライアント環境への展開やマルチテナント構成を扱う **Configuration Portability and Deployment**、PII のマスキング・コンプライアンス検証・コンテンツフィルタ・ハルシネーション検出といった要求／応答の傍受ユースケースを扱う **Interceptors and Middleware**、匿名化した本番障害シナリオを証拠として蓄積する **Problem Statements and Use Cases**、そして **Recommendations to Working Groups** です。

Out of Scope も明示されています。SEP を書くことと所有することは範囲外で、本グループが出すのは問題提起・ユースケース・推奨までとし、具体的な仕様変更は該当 Working Group が駆動します。製品固有・ベンダー固有の解決策の議論、一般的な MCP サポートやオンボーディングも範囲外です。Auth WG の仕様策定と直接重なることも避け、企業側の認証要件を集めて Auth WG へ渡す立場に徹するとされています。関連グループとしては、Working Group 側に Auth WG（IdP 統合・OBO・RAR の要件を入力）、Transport WG（レイテンシや水平スケールといった非機能要件を入力）、Extensions WG（認可以外の拡張の要件を入力）が挙げられ、Interest Group 側には Security IG（組織・ガバナンス面を Enterprise IG、脅威モデルとプロトコルレベルの緩和策を Security IG が担当）、Gateways IG（企業側の展開文脈を Enterprise IG、技術的なゲートウェイ仕様を Gateways IG が担当）、Financial Services IG（コンプライアンス・監査・規制環境で関心が重なるため相互投稿と合同セッションを調整）が並びます。

体制はファシリテーター 2 名（Raghu Chandra / Independent、Yannj_Fr / MCPApps Builders、いずれも任期 6 か月）と参加者 11 名で、所属には Saxo Bank・Silex Data Solutions・Blue Shield of California・Nordstrom・TraceForce・Boomi・Okta・GNS-Foundation・EmpowerID・Solo.io・Archestra が並びます。運営は月次 60 分の Working Session 1 種類のみで、ユースケースの議論・ペインポイントのカタログ化・グループ横断の調整を目的とし、Discord は `#enterprise-ig` です。意思決定については、問題提起とユースケースは GitHub Discussions や Discord スレッドで非同期に寄せて月次会議でレビューし、Working Group への推奨は参加者間の lazy consensus で確定させるとされています。推奨は GitHub 上で 7 日間のレビュー期間を設け、異議が出なければ承認扱いです。承認された推奨をまとめて該当グループへ届けるのはファシリテーターの責任と定められています。

Interest Group であるため拘束力のある成果物は無く、議論のアウトプットとして 4 件が予定されています。Enterprise Pain Points Catalog（目標 Q2 2026・Champion は Raghu Chandra）、Healthcare & Compliance Use Cases (PHI, BAA)（目標 Q3 2026・Champion は Aman s）、Auth WG への入力となる Enterprise Auth Requirements（目標 Q3 2026・Champion は TBD）、Gateway Deployment Patterns Document（目標 Q3 2026・Champion は TBD）で、状態はいずれも Planned です。最初の 1 件は目標時期を過ぎていますが状態は据え置かれています。なお changelog に記録された初版 charter の提出は 2026年04月13日で、索引に載ったのが 2026年08月30日、本文が収録されたのが今回にあたります。

- [Enterprise Interest Group Charter - MCP Docs](https://modelcontextprotocol.io/community/interest-groups/enterprise#scope)
- [Enterprise Interest Group Charter - MCP Docs](https://modelcontextprotocol.io/community/interest-groups/enterprise#leadership)

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
本文に 50 行以上の変更があったページは次の 1 件です。

- [**MCP Registry Supported Package Types**](#1-mcp-registry-supported-package-types) ([MCP Docs](https://modelcontextprotocol.io/registry/package-types#cargo-rust-packages)):  
  Cargo（Rust）パッケージの節が新設され、51 行が追加された。対応パッケージ種別は 5 種から 6 種になり、既存 5 種の記述に変更はない（詳細はハイライト 1・2 参照）。
<!-- light:updated-pages:end -->

## 1. MCP Registry Supported Package Types

このページへの変更は 1 か所への 51 行の追加に集中しており、削除行はありません。追加されたのは `## Cargo (Rust) Packages` の節と、その配下の `### Runtime Model`・`### Ownership Verification` の 2 小節です。挿入位置は NuGet Packages と Docker/OCI Images の間で、`server.json` の例・ランタイムモデルの説明・所有権検証という、既存の各パッケージ種別と同じ構成を踏襲しています。ただし `### Runtime Model` 小節を持つのは 6 種のうち Cargo だけで、ランナーの有無という差異を説明するために追加された節です。

結果として、本ページが列挙する対応パッケージ種別は npm・PyPI・NuGet・Cargo・Docker/OCI・MCPB の 6 種になりました。既存 5 種の節（対応レジストリの範囲、`server.json` の例、所有権検証の方法）には一切変更が入っていないため、今回の更新は純粋な新種別の追加として読めます。追加内容の詳細はハイライト 1・2 を参照してください。

- [MCP Registry Supported Package Types - MCP Docs](https://modelcontextprotocol.io/registry/package-types#cargo-rust-packages)

## 軽微な更新

<!-- light:minor-updates:start -->
上記 2 ページ以外に本文差分が出たのは 1 ページで、内容は綴り誤りの修正 1 行のみです。索引 `llms.txt` には差分が無く、エントリ件数・記載内容とも前回から変わっていません。

**その他**

- SEP-2549「TTL for List Results」の Security Implications 節で、`serer` という綴り誤りが `server` に修正された。置換はこの 1 語のみで、TTL のヒントとしての位置づけやクライアント側の扱いに関する記述内容は変わっていない — [MCP Docs](https://modelcontextprotocol.io/seps/2549-TTL-for-list-results#security-implications)
<!-- light:minor-updates:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-08-30.md](./archives/latest/2026-08-30.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-08-30.md](./archives/latest-detail/2026-08-30.md)

<!--
base_commit: e1ec6a5c1026e78db9ebf5bb0158a1e894a769ad
head_commit: e91ea8c5791ff294096b4c5eb5f6e51adac7736c
generated_at_full: 2026-09-01T15:30:01+09:00
-->
