---
対象期間: 2026年11月20日 〜 2026年11月21日
作成日: 2026-11-21
---

# MCP 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
今回の対象期間の取り込みは 1 回で、差分は本文 `llms-full.txt` の 7 ページで計 19 行（追加 10 行・削除 9 行）にとどまり、索引 `llms.txt` は変わりませんでした。コミュニティの連絡手段の案内で GitHub Discussions の用途が絞られ、Discord の招待リンクが差し替えられたほか、拡張の対応表にクライアントが 1 つ加わっています。

主要なものを以下に挙げます。

1. Communication ページの連絡手段の表で、GitHub Discussions の用途が会合の議題・議事録と告知に絞られた。ディスカッションを開けるのはこのリポジトリの書き込み権限を持つ人だけで、アイデア・機能の要望・質問は Discord から始める
2. Discord の招待リンクが、6 ページの 8 か所で `discord.gg/6CSzBmMkjX` から `discord.gg/modelcontextprotocol` に差し替えられた
3. Extension Support Matrix の対応表にクライアント mcp-use の行が加わり、クライアントは 18 になった
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**Communication で GitHub Discussions の用途が会合の記録と告知に絞られた**](#1-communication-で-github-discussions-の用途が会合の記録と告知に絞られた):  
  連絡手段を定める Communication ページの Channels の表で、GitHub Discussions の行の用途が書き換わった。旧版は「アイデア、根拠を添えた機能の要望、質問、ロードマップの議論、告知とリリース、会合の議題と議事録（Meeting Notes のカテゴリ）」だった。新版は「会合の議題と議事録（Meeting Notes のカテゴリ群）と告知」で、ディスカッションを開けるのはこのリポジトリの書き込み権限を持つ人だけであること、アイデア・機能の要望・質問は Discord から始めることが明記された。
2. [**Discord の招待リンクが 6 ページ 8 か所で差し替えられた**](#2-discord-の招待リンクが-6-ページ-8-か所で差し替えられた):  
  Communication・Governance and Stewardship・Financial Services Charter・Transports Charter・Working Groups and Interest Groups・SEP-2149 の 6 ページで、Discord サーバーへの招待リンク計 8 か所が `https://discord.gg/6CSzBmMkjX` から `https://discord.gg/modelcontextprotocol` に変わった。`llms-full.txt` に旧リンクは残っていない。チャンネルを直接指す `discord.com/channels/…` 形式の 7 つのリンクは変わっていない。
3. [**拡張の対応表に mcp-use の行が加わった**](#3-拡張の対応表に-mcp-use-の行が加わった):  
  Extension Support Matrix の Support matrix の表の末尾に、クライアント mcp-use（リンク先は GitHub の `mcp-use/mcp-use`）の行が加わり、クライアントの行は 17 から 18 になった。`llms-full.txt` ではこの行の 6 つのセルはすべて空だが、この表では対応を示すチェックマークが出力されないため、どの拡張に対応するかは `llms-full.txt` からは読み取れない。
<!-- light:highlight-list:end -->

## 1. Communication で GitHub Discussions の用途が会合の記録と告知に絞られた

今回の対象期間の取り込みは 1 回で、差分が出たのは本文 `llms-full.txt` だけでした（追加 10 行・削除 9 行）。総行数は 47,601 行から 47,602 行になり、収録ページ数（163 件。`examples` が 2 回収録されているため、URL としては 162 件）は変わっていません。索引 `llms.txt` には差分がありません（エントリ 364 件のまま）。変更のあった 7 ページはいずれも 50 行未満の変更で、軽微な更新に当たります。

| ページ | 行数 | 追加 | 削除 | 主な変更 |
|---|---|---|---|---|
| Communication | 34 → 34 | 3 | 3 | GitHub Discussions の行の書き換え（このハイライト）、Discord の招待リンク 2 か所（ハイライト 2） |
| Governance and Stewardship | 130 → 130 | 2 | 2 | Discord の招待リンク 2 か所（ハイライト 2） |
| Financial Services Charter | 123 → 123 | 1 | 1 | Discord の招待リンク 1 か所（ハイライト 2） |
| Transports Charter | 151 → 151 | 1 | 1 | Discord の招待リンク 1 か所（ハイライト 2） |
| Working Groups and Interest Groups | 151 → 151 | 1 | 1 | Discord の招待リンク 1 か所（ハイライト 2） |
| SEP-2149: MCP Group Governance and Charter Template | 438 → 438 | 1 | 1 | Discord の招待リンク 1 か所（ハイライト 2） |
| Extension Support Matrix | 63 → 64 | 1 | 0 | mcp-use の行の追加（ハイライト 3） |
| 計 | | 10 | 9 | |

行数は、ページのタイトルの行（`# `）から次のページの直前までを数えたものです。

**Communication（`community/communication`）**: プロジェクトの連絡手段、非公開にしてよい場合、決定の記録先を定めたページです。冒頭の Channels の表は、Discord・Meeting calendar・GitHub Discussions・GitHub Issues・Security advisories の 5 つの手段と、それぞれの用途を並べています。このうち GitHub Discussions の行の用途が、次のように書き換わりました。

| | 用途（原文） |
|---|---|
| 旧 | Ideas, feature requests with rationale, questions, roadmap discussion, announcements and releases, and meeting agendas and notes (Meeting Notes category) |
| 新 | Meeting agendas and notes, in the Meeting Notes categories, and announcements. Only people with write access to this repository can open a discussion. Ideas, feature requests and questions start on Discord |

- **用途**: 会合の議題と議事録、告知（announcements）の 2 つになった。会合の記録の置き場所は、旧版の単数の「Meeting Notes category」から、複数形の「Meeting Notes categories」になっている
- **開ける人の制限（新設）**: ディスカッションを開けるのは、このリポジトリ（リンク先の `modelcontextprotocol/modelcontextprotocol`）の書き込み権限を持つ人だけと明記された
- **Discord への振り分け（新設）**: アイデア・機能の要望・質問は Discord から始める、とされた。旧版の用途にあったロードマップの議論とリリース（「announcements and releases」の releases）は、新版の行には挙がっていない

Discord の行の用途（コントリビューターどうしのリアルタイムの調整。WG・IG・SDK の議論を含む）は、招待リンクのほかは変わっていません。表の直後の段落（各 SDK とプロジェクトのリポジトリはそれぞれ課題の管理と Discord のチャンネルを持ち、ほとんどは Discussions を無効にして Issues を使う。このリポジトリと registry が主な例外）と、Decision records の節（技術や統治の決定に向かう Discord の議論は GitHub Discussion へ移さなければならず、決定は `notes` ラベルの Discussion か SEP のプルリクエストに記録する）も変わっていません。

- [Communication - MCP Docs](https://modelcontextprotocol.io/community/communication#channels)

## 2. Discord の招待リンクが 6 ページ 8 か所で差し替えられた

本文中の Discord サーバーへの招待リンク 8 か所が、すべて `https://discord.gg/6CSzBmMkjX` から `https://discord.gg/modelcontextprotocol` に変わりました。リンクの文言と前後の文は変わっておらず、head の `llms-full.txt` に旧リンクは残っていません。

| ページ | 箇所 |
|---|---|
| Communication | Channels の表の Discord の行と、Discord の節の冒頭の「MCP Contributor Discord」（2 か所） |
| Governance and Stewardship | Technical Governance の Communication Channels の、メンテナー全員で共有する Discord サーバーと、Communication の Public Chat の、公開の Discord サーバー（2 か所） |
| Financial Services Charter | Operations の末尾の `#financial-services-ig` のリンク |
| Transports Charter | Operations の、`#transports-wg` で非同期に議論するとした文の「MCP Discord」 |
| Working Groups and Interest Groups | Forming a group の Interest group の、`#wg-ig-group-creation` のチャンネルがある Discord |
| SEP-2149: MCP Group Governance and Charter Template | Specification の 1.9 Lifecycle の Interest Group Formation の、同じく `#wg-ig-group-creation` のチャンネルがある Discord |

Financial Services Charter の `#financial-services-ig` のリンクは、チャンネルではなくサーバーの招待リンクを指しているため、これも新しい招待リンクに変わりました。一方、チャンネルを直接指す `discord.com/channels/…` 形式のリンク 7 つ（`#auth-ig`・`#scientific-computing-ig`・`#security-ig`・`#tool-annotations-ig`・`#progressive-disclosure-wg`・`#server-card-wg`・`#skills-over-mcp-wg`）は変わっていません。

- [Communication - MCP Docs](https://modelcontextprotocol.io/community/communication#discord)
- [Governance and Stewardship - MCP Docs](https://modelcontextprotocol.io/community/governance#public-chat)

## 3. 拡張の対応表に mcp-use の行が加わった

Extension Support Matrix（63 行から 64 行、追加 1 行）の Support matrix の表で、末尾（Glean の後）にクライアント mcp-use の行が加わり、クライアントの行は 17 から 18 になりました。リンク先は GitHub の `mcp-use/mcp-use` リポジトリです。

`llms-full.txt` では、この行の 6 つのセル（MCP Apps・OAuth Client Credentials・Enterprise Auth・Skills・Tasks・Events）はすべて空です。2026年10月20日のサマリで書いたとおり、`llms-full.txt` の書式が変わってから、この表では対応を示すチェックマークが出力されていません。空のセルが非対応を意味するとは限らず、mcp-use がどの拡張に対応するかは `llms-full.txt` からは読み取れません。Extension overview の表と、Support matrix の表の後の 2 つの注記は変わっていません。

- [Extension Support Matrix - MCP Docs](https://modelcontextprotocol.io/extensions/client-matrix#support-matrix)

## 新規追加されたページ

<!-- light:new-pages:start -->
今回の対象期間に新たに追加されたページはありません。本文 `llms-full.txt` の収録ページ数（163 件。URL としては 162 件）と、索引 `llms.txt`（エントリ 364 件）は前回と同じです。
<!-- light:new-pages:end -->

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
今回の対象期間に大幅な更新（本文 50 行以上の変更）があったページはありません。本文の変更は 7 ページで計 19 行（追加 10 行・削除 9 行）で、1 ページあたり最大 6 行（Communication）にとどまり、すべて軽微な更新に当たります（ハイライト 1 参照）。
<!-- light:updated-pages:end -->

## 軽微な更新

<!-- light:minor-updates:start -->
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
<!-- light:minor-updates:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-11-20.md](./archives/latest/2026-11-20.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-11-20.md](./archives/latest-detail/2026-11-20.md)

<!--
base_commit: 5f51174830a6109f6c27c1eeae6dd98de6f65dde
head_commit: 3279a161e968357548276a7baa091d6d6f481473
generated_at_full: 2026-11-22T15:23:29+09:00
-->
