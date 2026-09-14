---
対象期間: 2026年09月08日 〜 2026年09月13日
作成日: 2026-09-13
---

# MCP 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
今回の対象期間の差分は索引 `llms.txt` に加わった 2 行だけで、削除行はなく、ページ本文を収める `llms-full.txt` には 1 行の変更もありません。加わった 2 行はいずれも Skills Extension に関するもので、拡張ページ `extensions/skills/overview` と `SEP-2640: Skills Extension` が同じ断面で索引に載りました。

主要なものを以下に挙げます。

1. Skills Extension の拡張ページと SEP-2640 の 2 件が索引に同時追加された。索引上では MCP Apps・Tasks と同じ extensions ブロックと SEP 一覧に並ぶが、本文は両ページとも `llms-full.txt` に未収録で、拡張の識別子・プロトコル仕様・対応クライアントは今回の入力からは確認できない
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**Skills Extension の拡張ページと SEP-2640 が索引に追加**](#1-skills-extension-の拡張ページと-sep-2640-が索引に追加):  
  `extensions/skills/overview`（説明文「Discover and read Agent Skills from MCP servers」）と `seps/2640-skills-extension`（同「Skills Extension」）の 2 行が索引に加わった。今回の差分はこの 2 行の追加のみで、削除行はない。索引のエントリ行数は 350 件から 352 件、ユニーク URL は 345 件から 347 件になっている。本文は両ページとも `llms-full.txt` に未収録で、拡張の中身は入力から確認できない。
<!-- light:highlight-list:end -->

## 1. Skills Extension の拡張ページと SEP-2640 が索引に追加

今回の対象期間で入力に生じた変更は索引 `llms.txt` に限られ、追加 2 行・削除 0 行という内訳です。索引のファイル行数は 352 行から 354 行、エントリ行数は 350 件から 352 件、ユニーク URL は 345 件から 347 件へ、いずれも 2 件ぶんだけ増えました。一方でページ本文を収める `llms-full.txt` には差分が 1 行もなく、42,465 行・収録ページ 148 件のまま変わっていません。つまり既存ページの記述は 1 文字も変わっておらず、今回の断面で観測できるのは「索引に 2 つのページが現れた」という事実だけです。

その 2 行は、いずれも **Skills Extension** ―― MCP サーバーが Agent Skills を提供する仕組み ―― に対応するものです。1 つは索引の extensions ブロックに加わった `- [Skills](https://modelcontextprotocol.io/extensions/skills/overview.md): Discover and read Agent Skills from MCP servers`、もう 1 つは SEP 一覧に加わった `- [SEP-2640: Skills Extension](https://modelcontextprotocol.io/seps/2640-skills-extension.md): Skills Extension` です。拡張の解説ページと、その根拠となる SEP のページが同じ断面で揃って索引に載った形で、これは既存の Tasks（`extensions/tasks/overview` と `SEP-2663: Tasks Extension`）と同じ組み合わせ方です。

ただし**本文はどちらも未収録**です。`llms-full.txt` には `extensions/skills/overview` と `seps/2640-skills-extension` のいずれについても `Source:` 行がなく、既存ページ側にも追随の形跡がありません。実際、収録済みの `Extensions Overview` 本文が節を立てて挙げている公式拡張は MCP Authorization Extensions・MCP Apps・MCP Tasks の 3 系統のままで Skills の節はなく、`Extension Support Matrix` の拡張一覧も MCP Apps・OAuth Client Credentials・Enterprise-Managed Authorization の 3 件のまま（Tasks もまだ載っていません）です。この「索引が先・本文が後」というパターンは過去にも起きており（Enterprise Interest Group Charter が索引のみで追加された 2026年08月30日 作成分など）、本文が後続の断面で収録されるかどうかは次回以降の差分を待つことになります。したがって現時点では、拡張の識別子（`io.modelcontextprotocol/...` 形式の文字列）・やり取りするメソッドやフィールド・対応クライアントといった実質的な内容は、今回の入力からは一切確認できません。

- [Skills - MCP Docs](https://modelcontextprotocol.io/extensions/skills/overview)
- [SEP-2640: Skills Extension - MCP Docs](https://modelcontextprotocol.io/seps/2640-skills-extension)

## 新規追加されたページ

<!-- light:new-pages:start -->
今回索引に増えたページは次の 2 件です。いずれも本文は `llms-full.txt` に未収録で、ここで述べられるのは索引エントリそのものと、既存の収録済みページから読み取れる周辺事情に限られます。

- [**Skills**](#1-skills) ([MCP Docs](https://modelcontextprotocol.io/extensions/skills/overview)):  
  索引の extensions ブロック末尾、`Tasks` の直後に加わった拡張ページ。説明文は「Discover and read Agent Skills from MCP servers」で、MCP サーバーから Agent Skills を発見し読み取る方向の機能として紹介されている。
- [**SEP-2640: Skills Extension**](#2-sep-2640-skills-extension) ([MCP Docs](https://modelcontextprotocol.io/seps/2640-skills-extension)):  
  SEP 一覧に SEP-2596 と SEP-2663 の間（番号順）で加わったエントリ。Skills Over MCP Working Group の charter が「現在の方向性」として名指ししてきた SEP で、これまで GitHub の PR としてしか参照されていなかったものに公式ドキュメント上のページが与えられた。
<!-- light:new-pages:end -->

## 1. Skills

索引に追加されたのはタイトル `Skills`・パス `extensions/skills/overview`・説明文「Discover and read Agent Skills from MCP servers」の 1 行です。挿入位置は extensions ブロックの末尾、`Tasks` と `The MCP Registry` の間でした。このブロックは `Extensions Overview` → `Extension Support Matrix` → MCP Apps 系 → Authorization 系 → `Tasks` という並びで、charter 群のようなアルファベット順ではなく公式サイトのナビゲーション順に従っているため、末尾への挿入はアルファベット順の結果ではありません。これにより `modelcontextprotocol.io/extensions/` 配下を指す索引エントリは 8 件から 9 件になりました。タイトルが `Skills` という短い名詞である点は、直前の `Tasks` と同じ付け方です。

説明文が「**Discover and read** Agent Skills from MCP servers」と読み取り方向の 2 語で書かれている点は、Skills Over MCP Working Group の charter（収録済み・今回の差分では未変更）が SEP-2640 を「Resources-based, Extensions Track」と説明していることと符合します。つまり Resources という既存のプリミティブの上に skill の発見と読み取りを載せる、という組み立てが索引の 1 行からも読み取れます。ただしこれはあくまで説明文と charter の記述の照合であり、実際の仕様は本文が収録されるまで確認できません。

なお、索引には以前から `Build with Agent Skills`（説明文「Use agent skills to guide AI coding assistants through MCP server design and implementation」）が仕様バージョンごとに並んでおり、そちらは本文も収録済みですが、**別の話題**です。既存ページは「MCP サーバーを作る開発者が、自分の AI コーディングアシスタントに skill を読ませる」話であるのに対し、今回追加された `extensions/skills/overview` は「MCP サーバーが skill を提供し、クライアント側がそれを発見・読み取る」話で、skill が流れる向きが逆です。両者を混同しないよう注意が要ります。

- [Skills - MCP Docs](https://modelcontextprotocol.io/extensions/skills/overview)
- [Extension Support Matrix - MCP Docs](https://modelcontextprotocol.io/extensions/client-matrix#extension-overview)

## 2. SEP-2640: Skills Extension

索引に追加されたもう 1 行は、タイトル `SEP-2640: Skills Extension`・パス `seps/2640-skills-extension`・説明文「Skills Extension」です。挿入位置は `SEP-2596: Specification Feature Lifecycle and Deprecation Policy` と `SEP-2663: Tasks Extension` の間で、SEP 一覧の既存の番号順に従っています。これで `SEP-` で始まる索引エントリは 41 件から 42 件になりました。説明文がタイトルの後半をそのまま繰り返す形式である点も、隣の `SEP-2663: Tasks Extension`（説明文「Tasks Extension」）と同じです。

この SEP 自体は、収録済みの `Skills Over MCP Charter` 本文（今回の差分では未変更）に以前から登場していました。charter はミッションの記述で「WG の現在の方向性は SEP-2640 — Skills Extension（Resources ベース・Extensions Track）に表れている」と述べ、Active Work Items の表では「Skills Extension SEP (Extensions Track)」をステータス `In Review`・champion [@pja-ant](https://github.com/pja-ant) として、その参照実装を同じく `In Review`・champion [@olaservo](https://github.com/olaservo) として挙げています。charter の changelog の最新エントリは 2026年04月25日 の「Linked SEP-2640 in Active Work Items」で、**これらのステータスはその時点の記載**である点に注意が要ります。今回の差分には charter の更新が含まれないため、現在のステータスがどうなったかは入力からは分かりません。

注目すべき違いは参照の形です。charter 内で SEP-2640 は `github.com/modelcontextprotocol/modelcontextprotocol/pull/2640` という **GitHub の PR リンク**として書かれており、今回の追加以前は公式ドキュメント側に対応するページが存在しませんでした。同じ WG の出発点となった SEP-2076（Agent Skills as a First-Class MCP Primitive）に至っては、今回の断面でも索引にエントリがなく、charter 内の PR リンクとしてしか現れません。つまり SEP-2640 は、Skills をめぐる一連の提案のうち初めて公式ドキュメントのページを与えられたものということになります。`Extensions Overview` 本文が説明する公式拡張のライフサイクル（Propose → Implement → Review → Publish → Adopt）に照らせば索引掲載は後段の工程に対応しそうですが、本文が未収録である以上どの段階に達したかを入力から断定することはできません。

- [SEP-2640: Skills Extension - MCP Docs](https://modelcontextprotocol.io/seps/2640-skills-extension)
- [Skills Over MCP Charter - MCP Docs](https://modelcontextprotocol.io/community/working-groups/skills-over-mcp#active-work-items)
- [Extensions Overview - MCP Docs](https://modelcontextprotocol.io/extensions/overview#creating-extensions)

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
今回の対象期間に大幅な更新（本文 50 行以上の変更）があったページはありません。ページ本文を収める `llms-full.txt` には差分が 1 行もなく、42,465 行・収録ページ 148 件のまま既存ページの記述内容は変わっていません。
<!-- light:updated-pages:end -->

## 軽微な更新

<!-- light:minor-updates:start -->
今回差分が出たファイルは索引 `llms.txt` の 1 件のみで、その内容は新規エントリ 2 行の追加（新規追加されたページ 1・2 参照）に尽きます。削除行や既存エントリの書き換え、リンク先 URL の変更、字句修正はなく、これとは別に挙げる軽微な更新はありません。
<!-- light:minor-updates:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-09-08.md](./archives/latest/2026-09-08.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-09-08.md](./archives/latest-detail/2026-09-08.md)

<!--
base_commit: b8993e0293f2b6b04fd7517ad897abdaa6e0f01b
head_commit: af4f9aea12060f28aec2b5eafd4af096eee2ec40
generated_at_full: 2026-09-14T15:25:42+09:00
-->
