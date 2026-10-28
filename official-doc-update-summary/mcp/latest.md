---
対象期間: 2026年10月26日 〜 2026年10月27日
作成日: 2026-10-27
---

# MCP 公式ドキュメント更新サマリ

```markdown
今回の対象期間の取り込みは 1 回で、新規ページが 1 件（SEP-3398: Release Cycle Updates）、既存ページの小さな変更が 2 件ありました。中心は、仕様のリリースを年 2 回の定期サイクルにする Process SEP の追加です。

主要なものを以下に挙げます。

1. SEP-3398（Release Cycle Updates）が Accepted の状態で加わった。仕様のリリースを原則 3 月と 9 月の最終火曜日の年 2 回とし、8 か月のサイクルの中にソフトフリーズ・SDK ベータ・ハードフリーズを置く。2026年12月を目標としていたリリースは 2027年03月30日 へ移すことを提案している
2. 同じ SEP-3398 は、SEP が WG か Core Maintainer グループのスポンサーを得て公開の審査キューに入り、7 日間の記録投票で有権者全体の過半数の賛成を得て採択される手順を定めている
3. Extension Support Matrix の Support matrix に Tasks 拡張の列が加わった
```

## ハイライト

1. [**仕様のリリースを 3 月と 9 月の年 2 回にする SEP-3398 が Accepted になった**](./latest-detail.md#1-仕様のリリースを-3-月と-9-月の年-2-回にする-sep-3398-が-accepted-になった):  
  Process SEP の SEP-3398（Release Cycle Updates）が新規ページとして加わり、SEP の索引にも Accepted の 1 件として載った。仕様のリリースを原則 3 月と 9 月の最終火曜日に置き、リリースごとに 8 か月のサイクル（計画 2 か月・Core Maintainer の審査期間・安定化）を回す。リリースに入る SEP はソフトフリーズまでに Final でマージ済みであることが求められ、間に合わない提案は後のサイクルへ回してリリース日は動かさない。2026年12月を目標としていたリリースは 2027年03月30日 へ移すことを提案している。
2. [**SEP-3398 は SEP の審査にスポンサーと 7 日間の記録投票を求める**](./latest-detail.md#2-sep-3398-は-sep-の審査にスポンサーと-7-日間の記録投票を求める):  
  SEP は formal review の前に WG か Core Maintainer グループのスポンサーを得て、公開の SEP 審査キューに入る。審査は Core Maintainer の定例会議で行い、発表の後に 7 日間の記録投票を開く。採択には、投票開始時点の Core Maintainer グループ全体の過半数の賛成が要り、棄権や不在は賛成に数えない。
3. [**Extension Support Matrix に Tasks 列が加わった**](./latest-detail.md#3-extension-support-matrix-に-tasks-列が加わった):  
  Extension Support Matrix の Support matrix の表に、Tasks 拡張の列が 5 列目として加わった。ただし表のセルは Partial のリンクを除いてすべて空で、どのクライアントが Tasks に対応しているかは `llms-full.txt` からは読み取れない。

## 新規追加されたページ

- [**SEP-3398: Release Cycle Updates**](./latest-detail.md#1-仕様のリリースを-3-月と-9-月の年-2-回にする-sep-3398-が-accepted-になった) ([MCP Docs](https://modelcontextprotocol.io/seps/3398-release-cycle-updates)):  
  仕様のリリースを 3 月と 9 月の年 2 回とし、8 か月のサイクル・フリーズ・SEP のスポンサーと審査と投票の手順を定める Process SEP（Accepted）。索引 `llms.txt` にもエントリが加わった（詳細はハイライト 1・2 参照）。

## 大幅に更新されたページ

今回の対象期間に大幅な更新（本文 50 行以上の変更）があった既存ページはありません。既存ページで差分が最も大きいのは Extension Support Matrix の 16 行の書き換えで、「軽微な更新」で扱います。

## 軽微な更新

今回差分が出たファイルは `llms.txt` と `llms-full.txt` の 2 件で、新規ページのほかに次の変更がありました。

**機能改善**

- Extension Support Matrix の Support matrix に Tasks 拡張の列を追加（詳細はハイライト 3 参照） — [Extension Support Matrix](https://modelcontextprotocol.io/extensions/client-matrix#support-matrix)

**その他**

- Specification Enhancement Proposals (SEPs) の索引ページで、Summary に「Accepted: 1」の行を追加し、All SEPs の表の先頭に SEP-3398 の行を追加（詳細はハイライト 1 参照） — [Specification Enhancement Proposals (SEPs)](https://modelcontextprotocol.io/seps/index#all-seps)
- 索引 `llms.txt` の SEP の一覧で、SEP-2663: Tasks Extension の次に SEP-3398: Release Cycle Updates のエントリを追加 — [SEP-3398: Release Cycle Updates](https://modelcontextprotocol.io/seps/3398-release-cycle-updates)

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-10-26.md](./archives/latest/2026-10-26.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-10-26.md](./archives/latest-detail/2026-10-26.md)

<!--
base_commit: f43c40d31d95ea8ce1ef817f41d68a409f4e53f6
head_commit: 86d4f217654bd239db958544d6a55b7e3eb8a3e7
generated_at_full: 2026-10-28T15:34:18+09:00
-->
