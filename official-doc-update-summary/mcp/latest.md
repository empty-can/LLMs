---
対象期間: 2026年10月11日 〜 2026年10月12日
作成日: 2026-10-12
---

# MCP 公式ドキュメント更新サマリ

```markdown
今回の対象期間の変更は、チュートリアル「Build an MCP server」の TypeScript タブ 1 か所だけです。サンプルの天気サーバーが、新旧どちらのプロトコルのクライアントにも応答できる `serveStdio` ベースの構成に書き換えられ、その動作を確かめる手順も加わりました。

主要なものを以下に挙げます。

1. TypeScript 版の天気サーバーが、ファクトリ関数 `createServer()` を `serveStdio` に渡して起動する構成になり、`2026-07-28` のクライアントと 2025 年系のクライアントの両方に応答できるようになった
2. Inspector CLI を `--protocol-era modern` と `--protocol-era legacy` で 1 回ずつ実行し、どちらでもツール一覧が返るかを確かめる手順が加わった
```

## ハイライト

1. [**TypeScript 版サーバーの起動が serveStdio とファクトリ関数に移行**](./latest-detail.md#1-typescript-版サーバーの起動が-servestdio-とファクトリ関数に移行):  
  Build an MCP server の TypeScript タブで、サーバーインスタンスの生成とツールの登録を `createServer()` にまとめ、`serveStdio(createServer, …)` で起動する構成に変わった。`serveStdio` はクライアントごとにプロトコルのリビジョンを取り決めるため、`2026-07-28` のクライアントにも 2025 年系のクライアントにも応答できる。他の言語のタブは変わっていない。
2. [**Inspector CLI で新旧両プロトコルへの応答を確認する手順を追加**](./latest-detail.md#2-inspector-cli-で新旧両プロトコルへの応答を確認する手順を追加):  
  ビルド後のサーバーに対し、Inspector CLI で `--protocol-era modern` を指定してツール一覧を取得し、続けて `--protocol-era legacy` でも同じコマンドを実行する手順が加わった。原文では、どちらの実行でも `get_alerts` と `get_forecast` が一覧に出るとしている。

## 新規追加されたページ

今回の対象期間に新規追加されたページはありません。

## 大幅に更新されたページ

今回の対象期間に大幅な更新（本文 50 行以上の変更）があったページはありません。Build an MCP server は差分の行数をそのまま数えると 50 行を超えますが、空白の違いを無視すると 47 行のため、軽微な更新として扱います（詳細は「軽微な更新」参照）。

## 軽微な更新

変更があったのは既存 1 ページ（Build an MCP server）の TypeScript タブだけです。差分の行数は追加 149 行・削除 142 行ですが、大半はコードを `createServer()` の内側へ移したことによる字下げの変更で、空白の違いを無視して数えた行数（`git diff -w --numstat`）は追加 27 行・削除 20 行の計 47 行です。50 行に満たないため、軽微な更新に分類しました。`llms-full.txt` は 45,371 行から 45,378 行になり、収録ページは 157 件のままです。索引 `llms.txt` に変更はありません。

**機能改善**

- Build an MCP server の TypeScript タブで、サーバーの組み立てと起動を、ファクトリ関数 `createServer()` と `serveStdio` による構成に書き換え（詳細はハイライト 1 参照） — [MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-server#running-the-server)
- 同タブの「Running the server」節に、Inspector CLI で `modern` と `legacy` の両方のプロトコル世代に応答するかを確かめる手順を追加（詳細はハイライト 2 参照） — [MCP Docs](https://modelcontextprotocol.io/docs/2026-07-28/develop/build-server#running-the-server)

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-10-11.md](./archives/latest/2026-10-11.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-10-11.md](./archives/latest-detail/2026-10-11.md)

<!--
base_commit: 98d1f105aec298de4131f50d6044a9d5ea41da93
head_commit: a96f629ae39d1bbdbc8a90f79fba6100e8de16c0
generated_at_full: 2026-10-13T15:03:56+09:00
-->
