---
対象期間: 2026年11月15日 〜 2026年11月16日
作成日: 2026-11-16
---

# MCP 公式ドキュメント更新サマリ

```markdown
今回の対象期間の取り込みは 1 回で、入力の 2 ファイルとも差分がありました（`llms-full.txt` は追加 12 行・削除 11 行で 2 ページ、`llms.txt` は末尾への 3 行の追加）。本文の変更は仕様の Architecture と Overview の 2 ページで、非推奨の Sampling・Roots・ログを機能の例として挙げていた記述が書き換えられました。

主要なものを以下に挙げます。

1. 仕様の Architecture と Overview で、サーバーがクライアントに求める入力の例が Elicitation になり、Sampling・Roots・ログは非推奨と明記されるか例から外れた。Architecture のシーケンス図の `InputRequiredResult` の例も、`sampling/createMessage` から `elicitation/create` に替わった
```

## ハイライト

1. [**仕様の Architecture と Overview で非推奨の機能が例から外れた**](./latest-detail.md#1-仕様の-architecture-と-overview-で非推奨の機能が例から外れた):  
  仕様の Architecture（追加 9 行・削除 8 行）と Overview（`basic`。追加 3 行・削除 3 行）で、Sampling・Roots・ログを機能の例として挙げていた記述が書き換えられた。サーバーがクライアントに求める入力の例は Elicitation になり、Sampling と Roots の要求も `InputRequiredResult` で届くが非推奨だ、という脚注が加わった。Overview の構成要素の一覧では、Sampling・Roots・ログが非推奨と明記され、Utilities の例にページネーションが加わった。

## 新規追加されたページ

今回の対象期間に新たに追加されたページはありません。索引 `llms.txt` には末尾に 3 行が加わりましたが、エントリ（365 件）は増えておらず、本文 `llms-full.txt` の収録ページ数（160 件。URL としては 159 件）も前回と同じです。

## 大幅に更新されたページ

今回の対象期間に大幅な更新（本文 50 行以上の変更）があったページはありません。本文の変更は 2 ページで計 23 行（追加 12 行・削除 11 行）にとどまり、どちらも軽微な更新に当たります（ハイライト 1 参照）。

## 軽微な更新

今回差分が出たファイルは `llms-full.txt` と `llms.txt` の 2 件で、本文の 2 ページの変更と、索引の末尾への追加がありました。

**機能改善**

- Architecture（仕様）の導入文と Host の役割の一覧から、サンプリングの調整を外した（詳細はハイライト 1 参照） — [Architecture](https://modelcontextprotocol.io/specification/2026-07-28/architecture/index#host)
- 同ページの Servers で、クライアントに求める入力の例を elicitation だけにし、Sampling と Roots の要求も `InputRequiredResult` で届くが非推奨だという脚注を加えた（詳細はハイライト 1 参照） — [Architecture](https://modelcontextprotocol.io/specification/2026-07-28/architecture/index#servers)
- 同ページの Capability Negotiation で、クライアントの capability の例を elicitation の処理だけにし、シーケンス図の `InputRequiredResult` の例を `elicitation/create` とユーザーへの入力の要求に替えた（詳細はハイライト 1 参照） — [Architecture](https://modelcontextprotocol.io/specification/2026-07-28/architecture/index#capability-negotiation)
- Overview（仕様、`basic`）の冒頭の構成要素の一覧で、Client Features の Sampling とルートのディレクトリの一覧、Utilities のログを非推奨と明記し、Utilities の例にページネーションを加えた（詳細はハイライト 1 参照） — [Overview](https://modelcontextprotocol.io/specification/2026-07-28/basic/index)
- 同ページの Message Patterns で、MRTR でクライアントに求める追加の入力の例を「sampling・elicitation・roots」から「たとえば elicitation」に改めた（詳細はハイライト 1 参照） — [Overview](https://modelcontextprotocol.io/specification/2026-07-28/basic/index#message-patterns)

**その他**

- 索引 `llms.txt` の末尾に、空行 2 行と `This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.` という 1 文が加わった。ファイルは 367 行から 370 行になった（末尾の改行が無くなったため、改行の数では 367 から 369）。エントリではないので、エントリ数（365 件）は変わらない

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-11-15.md](./archives/latest/2026-11-15.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-11-15.md](./archives/latest-detail/2026-11-15.md)

<!--
base_commit: 080ef492a175aad917a584b345b6ed85c63c5b84
head_commit: 819daa7cd17307570b2a672fc258fafc61fd2cb2
generated_at_full: 2026-11-17T15:31:44+09:00
-->
