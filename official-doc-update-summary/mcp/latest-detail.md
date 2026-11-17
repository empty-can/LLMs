---
対象期間: 2026年11月15日 〜 2026年11月16日
作成日: 2026-11-16
---

# MCP 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
今回の対象期間の取り込みは 1 回で、入力の 2 ファイルとも差分がありました（`llms-full.txt` は追加 12 行・削除 11 行で 2 ページ、`llms.txt` は末尾への 3 行の追加）。本文の変更は仕様の Architecture と Overview の 2 ページで、非推奨の Sampling・Roots・ログを機能の例として挙げていた記述が書き換えられました。

主要なものを以下に挙げます。

1. 仕様の Architecture と Overview で、サーバーがクライアントに求める入力の例が Elicitation になり、Sampling・Roots・ログは非推奨と明記されるか例から外れた。Architecture のシーケンス図の `InputRequiredResult` の例も、`sampling/createMessage` から `elicitation/create` に替わった
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**仕様の Architecture と Overview で非推奨の機能が例から外れた**](#1-仕様の-architecture-と-overview-で非推奨の機能が例から外れた):  
  仕様の Architecture（追加 9 行・削除 8 行）と Overview（`basic`。追加 3 行・削除 3 行）で、Sampling・Roots・ログを機能の例として挙げていた記述が書き換えられた。サーバーがクライアントに求める入力の例は Elicitation になり、Sampling と Roots の要求も `InputRequiredResult` で届くが非推奨だ、という脚注が加わった。Overview の構成要素の一覧では、Sampling・Roots・ログが非推奨と明記され、Utilities の例にページネーションが加わった。
<!-- light:highlight-list:end -->

## 1. 仕様の Architecture と Overview で非推奨の機能が例から外れた

今回の対象期間の取り込みは 1 回で、入力の 2 ファイルとも差分がありました。本文 `llms-full.txt` は追加 12 行・削除 11 行で、総行数は 45,524 行から 45,525 行になり、変更のあったページは仕様の Architecture と Overview（`basic`）の 2 件です。どちらも 50 行未満の変更なので、軽微な更新に当たります。収録ページ数（160 件。`examples` が 2 回収録されているため、URL としては 159 件）は変わっていません。索引 `llms.txt` の変更は末尾への 3 行の追加だけで、エントリ数（365 件）は変わっていません（軽微な更新の「その他」参照）。

| ページ | 行数 | 追加 | 削除 | 主な変更 |
|---|---|---|---|---|
| Architecture（仕様） | 173 → 174 | 9 | 8 | 導入文、Host・Servers・Capability Negotiation の記述と図 |
| Overview（仕様、`basic`） | 498 → 498 | 3 | 3 | 構成要素の一覧、Message Patterns の MRTR の説明 |

行数は、ページのタイトルの行（`# `）から次のページの直前までを数えたものです。どちらのページも見出し（Architecture は 6 個、Overview は 24 個）は変わっていません。

Sampling・Roots・プロトコル経由のログは、base の時点でもプロトコルのバージョン `2026-07-28` で非推奨とされ、Deprecated Features のページ（`/specification/2026-07-28/deprecated`）の一覧に載っていました。今回は仕様の 2 ページで、これらを機能の例として挙げていた記述が書き換えられています。

**Architecture（仕様）。** 次の 4 か所が変わりました。

- **導入文**: MCP は JSON-RPC の上に作られ、クライアントとサーバーの間の「コンテキストの交換とサンプリングの調整」に焦点を当てたプロトコルを提供する、という文から「サンプリングの調整」が外れ、「コンテキストの交換」だけになった
- **Host**: ホストの役割の一覧で、「AI/LLM の統合とサンプリングを調整する」が「AI/LLM の統合を調整する」になった
- **Servers**: サーバーの役割の一覧で、返信の中の `InputRequiredResult` でクライアントに入力を求める、という項目の入力の例が「sampling・elicitation・roots」から「たとえば elicitation」になり、脚注が加わった。脚注は、Sampling と Roots の要求も `InputRequiredResult` で届くが、どちらもプロトコルのバージョン `2026-07-28` で非推奨で、新しい実装では使うべきでない、とし、Deprecated Features のページへリンクしている
- **Capability Negotiation**: クライアントが宣言する capability の例が、「sampling への対応と elicitation の処理」から「elicitation の処理」になった。シーケンス図の「Server requires client input」の分岐では、サーバーが返す `InputRequiredResult` の例が `sampling/createMessage` から `elicitation/create` に替わり、続く 2 つの矢印も、クライアントからホストへの「AI に転送する」とホストからの「AI の応答」から、「ユーザーに入力を求める」と「ユーザーの応答」に替わった

**Overview（仕様、`basic`）。** 次の 2 か所が変わりました。

- **冒頭の構成要素の一覧**: Client Features が「クライアントが提供する Elicitation・Sampling・ルートのディレクトリの一覧」から「クライアントが提供する Elicitation。Sampling とルートのディレクトリの一覧は非推奨」に、Utilities が「ログや引数の補完のような横断的な関心事」から「引数の補完やページネーションのような横断的な関心事。ログは非推奨」になった。2 つの「非推奨」は、どちらも Deprecated Features のページへのリンク
- **Message Patterns**: 一覧の Multi Round-Trip Requests（MRTR）の説明で、サーバーが要求を完了するために必要とするクライアントの追加の入力が、「sampling・elicitation・roots」から「たとえば elicitation」になった

なお、Overview からリンクされている Message Patterns のページ（`basic/patterns`）の Multi Round-Trip Requests の節には、サーバーがクライアントの入力（sampling, elicitation, or roots）を必要とするとき、という記述が今回も残っています。

- [Architecture - MCP Docs](https://modelcontextprotocol.io/specification/2026-07-28/architecture/index#servers)
- [Architecture - MCP Docs](https://modelcontextprotocol.io/specification/2026-07-28/architecture/index#capability-negotiation)
- [Overview - MCP Docs](https://modelcontextprotocol.io/specification/2026-07-28/basic/index#message-patterns)

## 新規追加されたページ

<!-- light:new-pages:start -->
今回の対象期間に新たに追加されたページはありません。索引 `llms.txt` には末尾に 3 行が加わりましたが、エントリ（365 件）は増えておらず、本文 `llms-full.txt` の収録ページ数（160 件。URL としては 159 件）も前回と同じです。
<!-- light:new-pages:end -->

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
今回の対象期間に大幅な更新（本文 50 行以上の変更）があったページはありません。本文の変更は 2 ページで計 23 行（追加 12 行・削除 11 行）にとどまり、どちらも軽微な更新に当たります（ハイライト 1 参照）。
<!-- light:updated-pages:end -->

## 軽微な更新

<!-- light:minor-updates:start -->
今回差分が出たファイルは `llms-full.txt` と `llms.txt` の 2 件で、本文の 2 ページの変更と、索引の末尾への追加がありました。

**機能改善**

- Architecture（仕様）の導入文と Host の役割の一覧から、サンプリングの調整を外した（詳細はハイライト 1 参照） — [Architecture](https://modelcontextprotocol.io/specification/2026-07-28/architecture/index#host)
- 同ページの Servers で、クライアントに求める入力の例を elicitation だけにし、Sampling と Roots の要求も `InputRequiredResult` で届くが非推奨だという脚注を加えた（詳細はハイライト 1 参照） — [Architecture](https://modelcontextprotocol.io/specification/2026-07-28/architecture/index#servers)
- 同ページの Capability Negotiation で、クライアントの capability の例を elicitation の処理だけにし、シーケンス図の `InputRequiredResult` の例を `elicitation/create` とユーザーへの入力の要求に替えた（詳細はハイライト 1 参照） — [Architecture](https://modelcontextprotocol.io/specification/2026-07-28/architecture/index#capability-negotiation)
- Overview（仕様、`basic`）の冒頭の構成要素の一覧で、Client Features の Sampling とルートのディレクトリの一覧、Utilities のログを非推奨と明記し、Utilities の例にページネーションを加えた（詳細はハイライト 1 参照） — [Overview](https://modelcontextprotocol.io/specification/2026-07-28/basic/index)
- 同ページの Message Patterns で、MRTR でクライアントに求める追加の入力の例を「sampling・elicitation・roots」から「たとえば elicitation」に改めた（詳細はハイライト 1 参照） — [Overview](https://modelcontextprotocol.io/specification/2026-07-28/basic/index#message-patterns)

**その他**

- 索引 `llms.txt` の末尾に、空行 2 行と `This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.` という 1 文が加わった。ファイルは 367 行から 370 行になった（末尾の改行が無くなったため、改行の数では 367 から 369）。エントリではないので、エントリ数（365 件）は変わらない
<!-- light:minor-updates:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-11-15.md](./archives/latest/2026-11-15.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-11-15.md](./archives/latest-detail/2026-11-15.md)

<!--
base_commit: 080ef492a175aad917a584b345b6ed85c63c5b84
head_commit: 819daa7cd17307570b2a672fc258fafc61fd2cb2
generated_at_full: 2026-11-17T15:31:44+09:00
-->
