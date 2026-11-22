---
対象期間: 2026年11月20日 〜 2026年11月21日
作成日: 2026-11-21
---

# MCP 公式ドキュメント更新サマリ

```markdown
今回の対象期間の取り込みは 1 回で、差分は本文 `llms-full.txt` の 7 ページで計 19 行（追加 10 行・削除 9 行）にとどまり、索引 `llms.txt` は変わりませんでした。コミュニティの連絡手段の案内で GitHub Discussions の用途が絞られ、Discord の招待リンクが差し替えられたほか、拡張の対応表にクライアントが 1 つ加わっています。

主要なものを以下に挙げます。

1. Communication ページの連絡手段の表で、GitHub Discussions の用途が会合の議題・議事録と告知に絞られた。ディスカッションを開けるのはこのリポジトリの書き込み権限を持つ人だけで、アイデア・機能の要望・質問は Discord から始める
2. Discord の招待リンクが、6 ページの 8 か所で `discord.gg/6CSzBmMkjX` から `discord.gg/modelcontextprotocol` に差し替えられた
3. Extension Support Matrix の対応表にクライアント mcp-use の行が加わり、クライアントは 18 になった
```

## ハイライト

1. [**Communication で GitHub Discussions の用途が会合の記録と告知に絞られた**](./latest-detail.md#1-communication-で-github-discussions-の用途が会合の記録と告知に絞られた):  
  連絡手段を定める Communication ページの Channels の表で、GitHub Discussions の行の用途が書き換わった。旧版は「アイデア、根拠を添えた機能の要望、質問、ロードマップの議論、告知とリリース、会合の議題と議事録（Meeting Notes のカテゴリ）」だった。新版は「会合の議題と議事録（Meeting Notes のカテゴリ群）と告知」で、ディスカッションを開けるのはこのリポジトリの書き込み権限を持つ人だけであること、アイデア・機能の要望・質問は Discord から始めることが明記された。
2. [**Discord の招待リンクが 6 ページ 8 か所で差し替えられた**](./latest-detail.md#2-discord-の招待リンクが-6-ページ-8-か所で差し替えられた):  
  Communication・Governance and Stewardship・Financial Services Charter・Transports Charter・Working Groups and Interest Groups・SEP-2149 の 6 ページで、Discord サーバーへの招待リンク計 8 か所が `https://discord.gg/6CSzBmMkjX` から `https://discord.gg/modelcontextprotocol` に変わった。`llms-full.txt` に旧リンクは残っていない。チャンネルを直接指す `discord.com/channels/…` 形式の 7 つのリンクは変わっていない。
3. [**拡張の対応表に mcp-use の行が加わった**](./latest-detail.md#3-拡張の対応表に-mcp-use-の行が加わった):  
  Extension Support Matrix の Support matrix の表の末尾に、クライアント mcp-use（リンク先は GitHub の `mcp-use/mcp-use`）の行が加わり、クライアントの行は 17 から 18 になった。`llms-full.txt` ではこの行の 6 つのセルはすべて空だが、この表では対応を示すチェックマークが出力されないため、どの拡張に対応するかは `llms-full.txt` からは読み取れない。

## 新規追加されたページ

今回の対象期間に新たに追加されたページはありません。本文 `llms-full.txt` の収録ページ数（163 件。URL としては 162 件）と、索引 `llms.txt`（エントリ 364 件）は前回と同じです。

## 大幅に更新されたページ

今回の対象期間に大幅な更新（本文 50 行以上の変更）があったページはありません。本文の変更は 7 ページで計 19 行（追加 10 行・削除 9 行）で、1 ページあたり最大 6 行（Communication）にとどまり、すべて軽微な更新に当たります（ハイライト 1 参照）。

## 軽微な更新

今回差分が出たファイルは `llms-full.txt` の 1 件で（`llms.txt` は変更なし）、7 ページに次の変更がありました。

**機能改善**

- Communication の Channels の表で、GitHub Discussions の用途を会合の議題・議事録と告知に絞り、ディスカッションを開けるのは書き込み権限を持つ人だけであること、アイデア・機能の要望・質問は Discord から始めることを明記した（詳細はハイライト 1 参照） — [Communication](https://modelcontextprotocol.io/community/communication#channels)
- Extension Support Matrix の Support matrix の表に、クライアント mcp-use の行を追加した（詳細はハイライト 3 参照） — [Extension Support Matrix](https://modelcontextprotocol.io/extensions/client-matrix#support-matrix)

**その他**

- Communication の Channels の表の Discord の行と、Discord の節の「MCP Contributor Discord」のリンクを、新しい招待リンク `discord.gg/modelcontextprotocol` に変更した（詳細はハイライト 2 参照） — [Communication](https://modelcontextprotocol.io/community/communication#discord)
- Governance and Stewardship の Communication Channels と Public Chat の Discord サーバーのリンクを、同じく新しい招待リンクに変更した（詳細はハイライト 2 参照） — [Governance and Stewardship](https://modelcontextprotocol.io/community/governance#communication-channels)
- Financial Services Charter の Operations の `#financial-services-ig` のリンクを、同じく新しい招待リンクに変更した（詳細はハイライト 2 参照） — [Financial Services Charter](https://modelcontextprotocol.io/community/interest-groups/financial-services#operations)
- Transports Charter の Operations の「MCP Discord」のリンクを、同じく新しい招待リンクに変更した（詳細はハイライト 2 参照） — [Transports Charter](https://modelcontextprotocol.io/community/working-groups/transports#operations)
- Working Groups and Interest Groups の Forming a group の Interest group の Discord のリンクを、同じく新しい招待リンクに変更した（詳細はハイライト 2 参照） — [Working Groups and Interest Groups](https://modelcontextprotocol.io/community/working-interest-groups#interest-group)
- SEP-2149: MCP Group Governance and Charter Template の 1.9 Lifecycle（Interest Group Formation）の Discord のリンクを、同じく新しい招待リンクに変更した（詳細はハイライト 2 参照） — [SEP-2149: MCP Group Governance and Charter Template](https://modelcontextprotocol.io/seps/2149-working-group-charter-template#1-9-lifecycle)

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-11-20.md](./archives/latest/2026-11-20.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-11-20.md](./archives/latest-detail/2026-11-20.md)

<!--
base_commit: 5f51174830a6109f6c27c1eeae6dd98de6f65dde
head_commit: 3279a161e968357548276a7baa091d6d6f481473
generated_at_full: 2026-11-22T15:23:29+09:00
-->
