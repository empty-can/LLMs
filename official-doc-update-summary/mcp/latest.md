---
対象期間: 2026年11月11日 〜 2026年11月12日
作成日: 2026-11-12
---

# MCP 公式ドキュメント更新サマリ

```markdown
今回の対象期間の取り込みは 1 回で、Registry の文書を中心に 17 ページに差分がありました（`llms-full.txt` は追加 362 行・削除 65 行、索引 `llms.txt` は変更なし）。50 行以上が変わったのは、Registry の認証・GitHub Actions・クイックスタートの 3 ページです。

主要なものを以下に挙げます。

1. GitHub 認証で組織の名前空間（`io.github.<orgname>/*`）に公開するには組織の Owner であることが要るようになり、`mcp-publisher login github` では今のところ組織の名前空間に公開できないと書かれた
2. GitHub Actions の 3 つのワークフロー例が `mcp-publisher` の版を `v1.8.1` に固定して Sigstore の署名を検証するようになり、CI で registry のトークンを守るための節が加わった
3. DNS 認証の TXT レコードはドメインの apex に置くこと、Ed25519 の鍵には OpenSSL 3.0 以降が要ることなどが書かれ、DNS 認証と HTTP 認証のトラブルシューティングが加わった
4. クイックスタートにパッケージを持たないリモートだけのサーバーの手順が加わり、Registry がリモート URL の所有を確かめないことが Publishing Remote Servers に書かれた
5. SEP Guidelines などが SEP-3398 に合わせて書き直され、SEP は working group（例外として Core Maintainers）が sponsor し、sponsor が付くまでは draft の PR のままになる形になった
```

## ハイライト

1. [**組織の名前空間への公開に組織の Owner 権限が要るようになった**](./latest-detail.md#1-組織の名前空間への公開に組織の-owner-権限が要るようになった):  
  How to Authenticate の GitHub 認証に、個人と組織の名前空間を説明する節が加わった。組織の名前空間（`io.github.<orgname>/*`）に公開するにはその組織の Owner でなければならず、ふつうのメンバーでは足りない。`mcp-publisher login github` は今のところ組織の名前空間に公開できないので、GitHub Actions（OIDC）か Personal Access Token を使う。
2. [**GitHub Actions の例が mcp-publisher の版を固定し署名を検証するようになった**](./latest-detail.md#2-github-actions-の例が-mcp-publisher-の版を固定し署名を検証するようになった):  
  3 つのワークフロー例が、`releases/latest` から取得してそのまま展開するのをやめ、`MCP_PUBLISHER_VERSION: v1.8.1` の版を取得して `cosign verify-blob` で検証してから展開するようになった。組織のトークンを Environment secret に置くことなどを勧める「Securing your registry token in CI」の節が加わった。
3. [**DNS 認証と HTTP 認証の注意点とトラブルシューティングが加わった**](./latest-detail.md#3-dns-認証と-http-認証の注意点とトラブルシューティングが加わった):  
  DNS 認証の TXT レコードは `_mcp-auth.` などのセレクタの下ではなくドメインの apex に置くこと、Ed25519 の鍵には OpenSSL 3.0 以降が要ること（macOS の LibreSSL では作れない）、ECDSA P-384 のログインには `--algorithm ecdsap384` を付けることが書かれた。Registry 側から見た HTTP 検証の要件と、DNS・HTTP 認証のトラブルシューティングの節が加わった。
4. [**リモートだけのサーバーの公開手順とリモート URL の扱いが書かれた**](./latest-detail.md#4-リモートだけのサーバーの公開手順とリモート-url-の扱いが書かれた):  
  クイックスタートに、`packages` を持たず `remotes` だけの `server.json` で公開する手順の節が加わった。Publishing Remote Servers には、Registry が確かめるのは `name` の名前空間の管理だけでリモート URL の管理は確かめないこと、複数のサーバー名が同じ URL を指せることが書かれた。
5. [**SEP は working group が sponsor する形になった**](./latest-detail.md#5-sep-は-working-group-が-sponsor-する形になった):  
  SEP Guidelines が sponsor の規則を SEP-3398 に合わせ、SEP を sponsor するのは working group（例外として Core Maintainers）になった。sponsor が付くまでの PR は、`proposal` ラベルの付いた PR から、`wg-support-needed` ラベルの付いた draft の PR に替わった。Contributing to MCP の手順も、working group に持ち込んで sponsor を得る流れに書き直された。

## 新規追加されたページ

*(新規追加されたページはありません)*

## 大幅に更新されたページ

- [**How to Authenticate When Publishing to the Official MCP Registry**](./latest-detail.md#1-how-to-authenticate-when-publishing-to-the-official-mcp-registry) ([MCP Docs](https://modelcontextprotocol.io/registry/authentication#troubleshooting-dns-and-http-authentication)):  
  278 行から 396 行になった。GitHub 認証に個人と組織の名前空間の節、DNS・HTTP 認証に注意書きと HTTP 検証のトラブルシューティングの節、末尾に DNS・HTTP 認証のトラブルシューティングの節が加わった（追加 120 行・削除 2 行。詳細はハイライト 1・3 参照）。
- [**How to Automate Publishing with GitHub Actions**](./latest-detail.md#2-how-to-automate-publishing-with-github-actions) ([MCP Docs](https://modelcontextprotocol.io/registry/github-actions#securing-your-registry-token-in-ci)):  
  217 行から 306 行になった。3 つのワークフロー例が `mcp-publisher` の版を固定して署名を検証するようになり、PAT のスコープの説明が書き直され、CI でトークンを守る節と「invalid audience」の対処が加わった（追加 97 行・削除 8 行。詳細はハイライト 1・2 参照）。
- [**Quickstart: Publish an MCP Server to the MCP Registry**](./latest-detail.md#3-quickstart-publish-an-mcp-server-to-the-mcp-registry) ([MCP Docs](https://modelcontextprotocol.io/registry/quickstart#remote-only-servers)):  
  285 行から 322 行になった。リモートだけのサーバーの節、npm 以外のパッケージの案内、`description` の 100 文字の上限、`mcp-publisher` の `status`・`validate` コマンドなどが加わった（追加 50 行・削除 13 行。詳細はハイライト 4 参照）。

## 軽微な更新

差分のあった 17 ページのうち、大幅更新で扱った 3 ページのほかに、14 ページで小さな変更がありました（いずれも追加・削除とも 30 行未満）。

**新機能**

- Frequently Asked Questions の「Can I delete/unpublish my server?」の答えが、「今のところできない」から「できる」になった — [Frequently Asked Questions](https://modelcontextprotocol.io/registry/faq#general)
  - `mcp-publisher status --status deleted` でステータスを `deleted` にする。バージョンを指定するか `--all-versions` で全バージョンを対象にし、`--message` で理由を付ける
  - 削除したサーバーは既定の API の一覧には出ないが、`include_deleted=true` で取得できる。ステータスを `active` に戻せば復元できる
  - サーバーのメタデータが Registry から完全に消えることはなく、`deleted` は発見から隠すだけで履歴は残る
- MCP Registry Supported Package Types の Docker/OCI Images で、対応するレジストリに Quay.io（`quay.io`）が加わり、`identifier` の例に `quay.io/myorg/my-mcp-server:1.0.0` が加わった — [MCP Registry Supported Package Types](https://modelcontextprotocol.io/registry/package-types#docker%2Foci-images)
- Working Groups Overview の表に Core Primitives の行が加わり、ワーキンググループは 14 件から 15 件になった — [Working Groups Overview](https://modelcontextprotocol.io/community/working-groups/overview)
  - Leads は Kurtis Van Gent と David Soria Parra、Discord は `#core-primitives-wg`、Focus は「ロードマップの Improved Primitives の領域のもとでの、ツールの結果の形・安定性・audience」
  - ほかの行と違い、リンク先は憲章のページではなく GitHub のリポジトリ `modelcontextprotocol/core-primitives-wg`。索引に Core Primitives の憲章のページは無い
  - Working Groups and Interest Groups の Current groups は 14 件のままで、Core Primitives は載っていない。2026年11月11日のサマリでは、この表と Current groups のグループは同じと書いたが、今回から一致しなくなった
  - ロードマップ（今回は変更なし）の Improved Primitives は、Tool result shape・Progressive discovery・Primitive annotations の担当を Core Primitives WG とし、Tool result shape の項では「このロードマップの期間に結成」と書いている

**機能改善**

- MCP Registry Aggregators の Consuming the MCP Registry REST API に、h3「Efficient synchronization」が加わった — [MCP Registry Aggregators](https://modelcontextprotocol.io/registry/registry-aggregators#efficient-synchronization)
  - 最初にページ送りで全件を取得した後は、Registry 全体を取り直さず、`updated_since` で差分を同期する
  - すべての `nextCursor` をたどる間は同じタイムスタンプを使い、全ページを反映し終えてから新しいチェックポイントを保存する
  - 同期の時間窓を少し重ね、サーバー名とバージョンで重複を除く（再試行やタイムスタンプの境目で更新を落とさないため）。差分の結果には削除されたサーバーも含まれるので、そのステータスの変化も手元に反映する
  - HTTP の圧縮を扱えるクライアントを使う（例: `curl --compressed`）。結果は手元に保存し、利用者のリクエストごとに全件を取り直さない。失敗したりレート制限を受けたりしたときは、全件の並行取得をやり直さず、バックオフ付きで再試行する
- MCP Registry Supported Package Types の PyPI と NuGet の所有確認に、README の `mcp-name: <サーバー名>` の後ろには区切り（改行・空白・HTML タグ・コメントの終わり `-->`）が要る、という説明が加わった。単独の行か `<!-- … -->` の中に置く。サーバー名の直後に文末のピリオドのような文字を続けると、一致しなくなる — [MCP Registry Supported Package Types](https://modelcontextprotocol.io/registry/package-types#pypi-packages)
- Publishing Remote Servers に、`remotes` だけのサーバーには Package Types の所有確認が当てはまらないという説明と、h2「Ownership Verification」が加わった（詳細はハイライト 4 参照） — [Publishing Remote Servers](https://modelcontextprotocol.io/registry/remote-servers#ownership-verification)

**その他**

- SEP Guidelines が sponsor の規則を SEP-3398 に合わせて書き直した。SEP を sponsor するのは working group（例外として Core Maintainers）で、sponsor が付くまでは `wg-support-needed` ラベルの付いた draft の PR になる（詳細はハイライト 5 参照） — [SEP Guidelines](https://modelcontextprotocol.io/community/sep-guidelines#sponsors)
- Contributing to MCP の Propose a protocol change の 4 段階が、ロードマップの確認・working group への持ち込み・グループが sponsor する SEP の作成・Core Maintainers への提出に書き直された（詳細はハイライト 5 参照） — [Contributing to MCP](https://modelcontextprotocol.io/community/contributing#propose-a-protocol-change)
- Working Groups and Interest Groups の冒頭と Working groups and interest groups の節で、SEP は working group が sponsor する、という書き方になった（詳細はハイライト 5 参照） — [Working Groups and Interest Groups](https://modelcontextprotocol.io/community/working-interest-groups#working-groups-and-interest-groups)
- Contributing to MCP の冒頭で、招待や役割が無くてもできることの列挙から「discussion を開く」がなくなり、「issue を開く」だけになった — [Contributing to MCP](https://modelcontextprotocol.io/community/contributing)
- SEP-2640: Skills Extension で、`skills/list`・`skills/get` の節へのページ内リンク（6 行・8 か所）のアンカーが、`#enumeration-via-skillslist`・`#retrieval-via-skillsget` から `#enumeration-via-skills%2Flist`・`#retrieval-via-skills%2Fget` になった — [SEP-2640: Skills Extension](https://modelcontextprotocol.io/seps/2640-skills-extension#enumeration-via-skills%2Flist)
- SEP-3398: Release Cycle Updates で、Working Groups and Interest Groups の意思決定の節へのリンクが `#decision-making-process` から `#making-decisions` に、Hard Freeze の節へのページ内リンクが `#hard-freeze--1-month-before-release` から `#hard-freeze-%E2%80%94-1-month-before-release` になった — [SEP-3398: Release Cycle Updates](https://modelcontextprotocol.io/seps/3398-release-cycle-updates#sponsorship-and-submission)
- SEP-3392: Extension Lifecycle で、Working Groups and Interest Groups の意思決定の節へのリンクが `#decision-making-process` から `#making-decisions` になった — [SEP-3392: Extension Lifecycle](https://modelcontextprotocol.io/seps/3392-extension-lifecycle#roles)
- SEP-2133: Extensions で、`_meta` のキーの規則へのリンクのアンカーが `#meta` から `#_meta` になった — [SEP-2133: Extensions](https://modelcontextprotocol.io/seps/2133-extensions#definition)
- SEP-2575: Make MCP Stateless で、Core Maintainers による sessions-vs-sessionless の決定へのリンク先が、`transports-wg` リポジトリの `docs/sessions-vs-sessionless-decision.md` から `proposals/stateless/session-removal-decision.md` になった。2026年11月11日のサマリで、`docs/` 配下の文書へのリンクが残っていると書いたもの — [SEP-2575: Make MCP Stateless](https://modelcontextprotocol.io/seps/2575-stateless-mcp#explicit-session-management)
- SEP-1577: Sampling With Tools で、参照実装の `toolLoopSampling.ts` へのリンクが、typescript-sdk のブランチ `ochafik/sep1577` からコミット `d372eff7…` を指すものになった — [SEP-1577: Sampling With Tools](https://modelcontextprotocol.io/seps/1577--sampling-with-tools#motivation)

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-11-11.md](./archives/latest/2026-11-11.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-11-11.md](./archives/latest-detail/2026-11-11.md)

<!--
base_commit: c85f1a228a539e3f1157cb0caf9aea01e5add4d1
head_commit: 77f196ce342a0c6130e111a1fa66ada14d87a243
generated_at_full: 2026-11-13T15:39:20+09:00
-->
