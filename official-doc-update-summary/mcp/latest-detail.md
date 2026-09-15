---
対象期間: 2026年09月13日 〜 2026年09月14日
作成日: 2026-09-14
---

# MCP 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
今回の対象期間の差分は本文 `llms-full.txt` に限られ、索引 `llms.txt` には 1 行の変更もありません。前回索引にだけ現れて本文が未収録だった Skills 拡張の 2 ページ（拡張ページと SEP-2640）が本文として収録され、これに合わせて既存 3 ページも追従しました。

主要なものを以下に挙げます。

1. Skills 拡張（識別子 `io.modelcontextprotocol/skills`）の仕様本文が収録され、`skills/list`・`skills/get` が必須メソッド、`resources/directory/read` が `directoryRead` 宣言時のみ呼べる任意メソッドと定まった。スキルは既存の Resources プリミティブの上に載り、1 スキルあたり 512 ファイル・16 MiB が上限
2. SEP-2640 の本文がステータス `Final` として収録され、Python・C#・Go 各 SDK の PR や conformance テスト、プロトタイプ実装の所在が明記された。一方で Skills Over MCP WG の charter ページは今回未更新で、Active Work Items のステータスは `In Review` のまま
3. `Extension Support Matrix` に Skills の行と列が加わり、ChatGPT・fast-agent・MCP Inspector の 3 クライアントが `Partial` として掲載された。うち fast-agent と MCP Inspector は表に行そのものが新設されている
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**Skills 拡張の仕様本文が収録され 3 つのメソッドが確定**](#1-skills-拡張の仕様本文が収録され-3-つのメソッドが確定):  
  拡張ページ `extensions/skills/overview` の本文が収録され、前回の断面では確認できなかった識別子・メソッド・宣言方法が明らかになった。サーバーは `server/discover` で `resources` capability と `io.modelcontextprotocol/skills` 拡張の双方を宣言し、`skills/list` と `skills/get` を実装する。ファイル本体の取得は既存の `resources/read` を使い、ディレクトリ列挙の `resources/directory/read` だけが `directoryRead: true`（既定 `false`）を宣言したサーバーに限られる任意機能である。
2. [**SEP-2640 が Final ステータスで本文収録**](#2-sep-2640-が-final-ステータスで本文収録):  
  SEP ページの本文が収録され、ステータスが `Final`・種別が Extensions Track・作成日が 2026年04月23日 であることが確認できるようになった。参照実装として Python・C#・Go 各 SDK の PR、conformance テスト、4 つのプロトタイプホストと 1 つのプロトタイプサーバーが列挙されている。`seps/index` の Final 件数も 41 件から 42 件へ更新された。ただし Skills Over MCP WG の charter ページは今回の差分に含まれず、Active Work Items のステータス表記は `In Review` のまま据え置かれている。
3. [**クライアント対応表に Skills 列が追加**](#3-クライアント対応表に-skills-列が追加):  
  `Extension Support Matrix` の拡張一覧に `Skills over MCP` の行が加わり、対応表には Skills 列が新設された。この列に印が付いたのは ChatGPT・fast-agent・MCP Inspector の 3 件で、いずれも `<CHECK />` ではなく外部ドキュメントへリンクした `Partial` 表記である。fast-agent と MCP Inspector は対応表に初めて現れたクライアントで、`Extensions Overview` にも `Skills over MCP` の節が新設された。
<!-- light:highlight-list:end -->

## 1. Skills 拡張の仕様本文が収録され 3 つのメソッドが確定

今回の対象期間で差分が出たのは本文 `llms-full.txt` の 1 ファイルのみで、索引 `llms.txt` は 354 行・エントリ 352 件・ユニーク URL 347 件のまま 1 行も変わっていません。前回が「索引だけが動き、本文は無変更」だったのに対し、今回はちょうどその逆の断面です。`llms-full.txt` は 42,465 行から 43,588 行へ、収録ページは 148 件から 150 件へ増え、変更があったのは新規 2 ページ・既存 3 ページの計 5 ページでした。前回サマリで「拡張の識別子・プロトコル仕様・対応クライアントは今回の入力からは確認できない」と留保した点は、いずれも今回の本文収録で埋まっています。

拡張の識別子は **`io.modelcontextprotocol/skills`** です。サーバーは [`server/discover`](https://modelcontextprotocol.io/extensions/skills/overview#capabilities) の capabilities で `resources` と `extensions` の双方を宣言する必要があり、`resources` capability なしにこの拡張だけを宣言することはできません。拡張オブジェクトに置ける設定は `directoryRead`（boolean・既定 `false`）の 1 つだけで、空オブジェクトは「ディレクトリ読み取りなしで拡張に対応」を意味します。拡張を宣言したサーバーは `skills/list` と `skills/get` の実装が必須で、クライアントはサーバーの宣言を見てから初めてこれらを呼びます。

プロトコルとして新設されるメソッドは 3 つです。`skills/list` はサーバーが提供するスキルを列挙し、ページネーションと、プロトコルリビジョン `2026-07-28` 以降ではリスト用のキャッシュ属性 `ttlMs` / `cacheScope` に対応します。`skills/get` は URI を指定して 1 件のスキルエントリを取得するもので、一覧に現れないスキルについてもサーバーは応答しなければなりません（カタログが大きい・動的生成などの理由で一覧が空または部分的でもよいことが明示されており、ホストは空の一覧を「スキルが無い」証拠として扱ってはなりません）。3 つ目の `resources/directory/read` はディレクトリ直下の子を列挙する任意メソッドで、子ディレクトリは `mimeType: "inode/directory"` で表されます。スキルのファイル本体を読むのは既存の `resources/read` で、読み取り専用の新メソッドは設けられていません。

スキルエントリは `uri`（スキルの `SKILL.md` のリソース URI）・`frontmatter`（`SKILL.md` の YAML フロントマターを改変せず JSON 化したもの）・`resources`（全ファイルを `{uri, digest, size}` で列挙した配列、または動的生成を示す文字列 `"dynamic"`）の 3 フィールドで構成されます。ホストは読み取ったファイルのバイト数と SHA-256 ダイジェストを使用前に必ず検証し、`SKILL.md` のフロントマターはエントリ側の `frontmatter` とフィールド単位で突き合わせます。ユーザーの承認はこの `resources` の集合（全 `uri` と `digest`）に束縛され、ファイルが 1 つでも差し替え・追加・削除されると承認は失効して再取得が必要になります。また `SKILL.md` を `resources/read` で読んだだけではスキルは有効化されず、ホスト自身のスキル読み込み経路を通って初めて有効になる、という切り分けも明記されました。1 スキルあたりの上限は **512 ファイル・16 MiB**（16,777,216 バイト）で、ホストはこの範囲までの対応が必須、サーバーはこれを超えるスキルを提供すべきでないとされています。

- [Skills - MCP Docs](https://modelcontextprotocol.io/extensions/skills/overview#capabilities)
- [Skills - MCP Docs](https://modelcontextprotocol.io/extensions/skills/overview#protocol-messages)

## 2. SEP-2640 が Final ステータスで本文収録

SEP ページ `seps/2640-skills-extension` の本文も同じ断面で収録されました。冒頭のバッジは `Final` と `Extensions Track` の 2 つで、続く注記は「この SEP は Final に達したため、承認された時点の設計の歴史的記録として保存されている。確定後にプロトコルへ加えられた変更は反映されないので、規範的な要件は現行仕様とその changelog を参照すること」と述べています。メタ情報の表からは、作成日が 2026年04月23日、スポンサーが [@pja-ant](https://github.com/pja-ant)、PR が本家リポジトリの #2640 であること、著者が Skills Over MCP Working Group を代表する 4 名（Peter Alexander・Ola Hungerford・Sambhav Kothari・Aditya Kumar）であることが読み取れます。この更新に合わせて SEP 索引ページの Summary も **Final: 41 から 42** へ増え、一覧表には `SEP-2663: Tasks Extension` と `SEP-2596` の間に SEP-2640 の行が挿入されました。

参照実装の所在が節として明示されたのも今回からです。SEP-2133 が Extensions Track の SEP にレビュー前の参照実装を求めていることを受け、SDK 側は Python（python-sdk#3485）・C#（csharp-sdk#1856）・Go（go-sdk#1238）の 3 件、conformance テストは SEP トレーサビリティファイル `sep-2640.yaml` を伴う conformance#330 が挙げられています。プロトタイプのホスト実装は gemini-cli・fast-agent・codex の 3 件が PR リンク付きで並び、Claude Code については「Anthropic 社内でプロトタイプ済み・未公開」と書かれています。サーバー側のプロトタイプは GitHub MCP Server（github-mcp-server#3046）の 1 件です。

一方で注意が要るのは、ステータスに関するページ間の食い違いです。SEP ページが `Final` を掲げるのに対し、Skills Over MCP WG の charter ページは今回の差分に含まれておらず、Active Work Items の表では「Skills Extension SEP (Extensions Track)」も「Skills Extension reference implementation」も依然 `In Review` のままです。charter の changelog の最新エントリは 2026年04月25日 の「Linked SEP-2640 in Active Work Items」で、この記載はその時点のものです。前回サマリでも同じ留保を付けましたが、SEP 側が Final に進んだ今回もなお charter 側は追従していません。charter の記述だけを見て現在のステータスを判断しないようにしてください。

- [SEP-2640: Skills Extension - MCP Docs](https://modelcontextprotocol.io/seps/2640-skills-extension#reference-implementation)
- [Skills Over MCP Charter - MCP Docs](https://modelcontextprotocol.io/community/working-groups/skills-over-mcp#active-work-items)

## 3. クライアント対応表に Skills 列が追加

`Extension Support Matrix` は今回の既存ページの中で最も変更が大きく、追加 21 行・削除 18 行でした。まず拡張一覧の表に 4 行目として `Skills over MCP`（識別子 `io.modelcontextprotocol/skills`、説明「Discover skills and read their instructions and supporting files」）が加わりました。これで一覧は MCP Apps・OAuth Client Credentials・Enterprise-Managed Authorization・Skills over MCP の 4 件になります。なお前回サマリで触れた「Tasks がこの一覧にまだ載っていない」状態は今回も変わっておらず、Skills だけが先に掲載された形です。

対応表には 4 列目として Skills 列が新設されました。この列に記載が入ったのは 3 クライアントで、いずれも他列で使われている `<CHECK />` ではなく、外部ドキュメントへリンクした `Partial` という表記です。**ChatGPT** は OpenAI の開発者ドキュメント（MCP サーバーからの skill 取り込みの節）へ、**fast-agent** は同プロジェクトの `skills-over-mcp.md` へ、**MCP Inspector** は CLI クライアントの README にある skill 検証（`--verify`）の節へリンクしています。このうち fast-agent と MCP Inspector は行そのものが今回新設されたクライアントで、どちらも MCP Apps 列は空欄、Skills 列だけに記載がある状態です。これにより対応表のクライアントは 11 件から 13 件になりました。既存 11 クライアントのうち Skills 欄に記載が入ったのは ChatGPT のみで、残る 10 件は空欄のままです。対応表全体としては MCP Apps に印が集中する構図に変わりはありません。

`Extensions Overview` 側にも追従がありました。Tasks の節の後ろに `### Skills over MCP` の節が新設され、ext-skills リポジトリへの Card、`Skills over MCP` 1 行だけの表（説明は「Discover workflow instructions and read supporting files through MCP resources.」）、そして Skills overview ページと client matrix への誘導文が置かれています。これで同ページが節を立てて紹介する公式拡張は、MCP Authorization Extensions・MCP Apps・MCP Tasks・Skills over MCP の 4 系統になりました。

- [Extension Support Matrix - MCP Docs](https://modelcontextprotocol.io/extensions/client-matrix#support-matrix)
- [Extensions Overview - MCP Docs](https://modelcontextprotocol.io/extensions/overview#skills-over-mcp)

## 新規追加されたページ

<!-- light:new-pages:start -->
今回本文が新たに収録されたページは次の 2 件です。いずれも索引には前回の断面で既に載っており、本文が 1 回遅れて追いついた形になります。

- [**Skills**](#1-skills) ([MCP Docs](https://modelcontextprotocol.io/extensions/skills/overview)):  
  Skills 拡張の解説ページ。capability 宣言・3 つのプロトコルメッセージ・メッセージフロー・整合性検証・実装要件・エラー処理・クライアント対応という構成で、規範的な仕様の正本は ext-skills リポジトリ側にあると明記している。
- [**SEP-2640: Skills Extension**](#2-sep-2640-skills-extension) ([MCP Docs](https://modelcontextprotocol.io/seps/2640-skills-extension)):  
  提案そのものの全文。動機として挙げられた 3 つの問題、`skill://` URI の設計、入れ子スキルの扱い、後方互換性、セキュリティ上の含意、そしてレビュー中に削除された機能を記録する付録までを含む。
<!-- light:new-pages:end -->

## 1. Skills

索引には前回の断面で既に `- [Skills](https://modelcontextprotocol.io/extensions/skills/overview.md): Discover and read Agent Skills from MCP servers` という 1 行が載っていましたが、今回その本文が `Source:` 行を除いて 430 行ぶん収録されました。ページは冒頭で ext-skills リポジトリへの Card を置き、「Skills 拡張は MCP サーバーがワークフローの指示と補助ファイルをクライアントへ公開できるようにするもので、クライアントは既存の Resources プリミティブを使って利用可能なスキルを発見し、メタデータを取得し、内容を読む」と要約しています。スキルの実体は `SKILL.md` を含むディレクトリで、その形式自体は [Agent Skills 仕様](https://agentskills.io/specification)（agentskills.io）に委ねられ、本拡張が定めるのは MCP 上での発見と取得だけである、という線引きが明示されています。

ページの構成は User Interaction Model・Capabilities・Protocol Messages・Message Flow・Integrity and Verification・Implementation Requirements・Error Handling・Client Support・Specification の順です。Message Flow には mermaid のシーケンス図が置かれ、カタログの発見からスキルの選択、ユーザー承認、`SKILL.md` の取得と検証、補助ファイルの遅延読み込みまでが 1 枚で追えるようになっています。Error Handling は 3 行の表で、未知のスキル・ファイルや不正なディレクトリ URI は `-32602`（Invalid params）、サーバー内部の失敗は `-32603`（Internal error）、ダイジェスト・サイズ・フロントマター・マニフェストの不一致はプロトコルエラーではなくホスト側の条件としてエントリの再取得で処理する、と整理されています。最後の Specification 節は「完全な仕様は ext-skills リポジトリにあり、開発は Skills Over MCP Working Group が調整している」と述べており、**このページ自体は正本ではなく要約**である点に注意が要ります。

表記について 1 点補足があります。索引エントリとページ見出しはどちらも短く `Skills` ですが、`Extension Support Matrix` と `Extensions Overview` では同じものが `Skills over MCP` と呼ばれています。どちらも同じ `extensions/skills/overview` を指すので、検索時は両方の呼び方を当たるのが確実です。また前回サマリで「既存の `Build with Agent Skills` とは skill が流れる向きが逆で別の話題」と注意した点は、今回収録された本文が「MCP サーバーがスキルを公開し、クライアントが発見して読む」方向をはっきり述べたことで裏づけられました。ホストアプリケーションがスキルをモデルやユーザーにどう見せるかは本拡張では規定せず、モデルによる選択もユーザーによる明示的な選択も許容されます。

- [Skills - MCP Docs](https://modelcontextprotocol.io/extensions/skills/overview#specification)
- [Skills - MCP Docs](https://modelcontextprotocol.io/extensions/skills/overview#error-handling)

## 2. SEP-2640: Skills Extension

もう 1 件の新規収録は SEP-2640 の全文で、`Source:` 行を除いて 670 行と今回最大のページです。Motivation は 3 つの問題を挙げます。第 1 に**配布の分断** ―― サーバーと、その使い方をエージェントに教えるスキルとが別々にバージョン管理・発見・インストールされ、レジストリからサーバーを入れたユーザーには対になるスキルの存在が伝わりません。第 2 に**指示サイズの限界** ―― サーバーの指示は `server/discover` 結果の `instructions` フィールドで届くため実質的に大きさが制限され、875 行に及ぶ mcpGraph のスキルのような複雑なワークフローは収まりません。第 3 に**場当たり的な実装の乱立** ―― 規約が無いために複数の実装がそれぞれ独自の `skill://` URI 構造を考案し、authority・パス・サブリソースの指定方法が食い違っている、という指摘です。

仕様面で拡張ページより踏み込んでいるのが URI 設計です。リソース URI は `skill://<skill-path>/<file-path>` の形を取り、`<skill-path>` は 1 つ以上のセグメントからなり、その**最終セグメントは `SKILL.md` フロントマターの `name` と一致しなければならない**と定められています。先行するセグメントはサーバーが選ぶ組織的な接頭辞で、`skill://acme/billing/refunds/SKILL.md` なら接頭辞が `acme/billing`、`name` は `refunds` です。RFC 3986 上は最初のセグメントが authority 成分を占めますが、これに特別な意味は無く、クライアントが DNS 解決やネットワークアクセスを試みてはならない旨が明記されています。スキルの入れ子も認められており、内側のスキルは外側から見れば通常の補助ファイルに過ぎず、入れ子の `SKILL.md` を読んだだけではそのフロントマターを働かせてはならない、有効化には改めて明示的なユーザー同意が要る、という 3 点で整理されています。名前は識別子ではなくラベルであり、スキルの同一性は「サーバーの識別子と URI の組」で決まる、という原則も繰り返し述べられています。

後方互換性の節には移行の実務に関わる記述があります。3 つのメソッドはいずれも拡張を宣言したサーバーにしか呼ばれないため既存のクライアントは影響を受けませんが、**独自の `skill://` URI 構造を使っている既存実装は適合のための調整が必要**で、なかでも広く使われている FastMCP の SkillsProvider は URI 構造・発見方法（スキルごとの `_manifest` か中央索引か）・メタデータの対応付けで食い違っており、その移行の調整が Working Group の近い時期の優先事項である、とされています。末尾の付録 Appendix: Deferred Features には、レビュー中に Core Maintainers が削除した **Archive Distribution**（スキルディレクトリ全体を tar.gz / ZIP でまとめて配布する案）が、削除理由とともに記録されています。理由は 2 点で、リモートサーバー由来のアーカイブを安全に展開するには解凍爆弾・パストラバーサル・シンボリックリンク・setuid ビットなどへの防御を全ホストが正しく実装せねばならず利得に見合わないこと、そして 1 つのスキルに 2 通りの提供形式があると互換性の下限が崩れることです。今後この機能を再提案する場合はこれらの反論から出発できるよう、あえて記録を残す方針が示されています。

- [SEP-2640: Skills Extension - MCP Docs](https://modelcontextprotocol.io/seps/2640-skills-extension#motivation)
- [SEP-2640: Skills Extension - MCP Docs](https://modelcontextprotocol.io/seps/2640-skills-extension#resource-mapping)

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
今回の対象期間に大幅な更新（本文 50 行以上の変更）があった既存ページはありません。既存ページで最も変更が大きかった `Extension Support Matrix` でも追加 21 行・削除 18 行で、その内訳は表への行・列の追加と、列幅を揃えるための既存行の書き換えです（詳細はハイライト 3 参照）。
<!-- light:updated-pages:end -->

## 軽微な更新

<!-- light:minor-updates:start -->
今回差分が出たファイルは本文 `llms-full.txt` の 1 件のみで、新規 2 ページの収録を除くと、既存ページ側の変更は 3 件です。いずれも Skills 拡張の追加に伴う追従で、これと無関係な字句修正やリンク先の変更はありません。

**機能改善**

- `Extension Support Matrix` に、拡張一覧の `Skills over MCP` 行と対応表の Skills 列が加わり、ChatGPT・fast-agent・MCP Inspector の 3 クライアントが `Partial` として掲載された。fast-agent と MCP Inspector は行そのものが新設（詳細はハイライト 3 参照） — [Extension Support Matrix](https://modelcontextprotocol.io/extensions/client-matrix#support-matrix)
- `Extensions Overview` に `### Skills over MCP` の節が新設され、ext-skills リポジトリへの Card・1 行の拡張表・Skills overview と client matrix への誘導が加わった（詳細はハイライト 3 参照） — [Extensions Overview](https://modelcontextprotocol.io/extensions/overview#skills-over-mcp)

**その他**

- SEP 索引ページの一覧表に SEP-2640 の行が SEP-2663 と SEP-2596 の間（番号順）で挿入され、Summary の Final 件数が 41 から 42 に更新された。差分としては追加 2 行・削除 1 行のみ（詳細はハイライト 2 参照） — [Specification Enhancement Proposals (SEPs)](https://modelcontextprotocol.io/seps/index#all-seps)
<!-- light:minor-updates:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-09-13.md](./archives/latest/2026-09-13.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-09-13.md](./archives/latest-detail/2026-09-13.md)

<!--
base_commit: af4f9aea12060f28aec2b5eafd4af096eee2ec40
head_commit: a19a359d88d83c75d535255e4c3dd79daa4f181f
generated_at_full: 2026-09-15T15:40:05+09:00
-->
