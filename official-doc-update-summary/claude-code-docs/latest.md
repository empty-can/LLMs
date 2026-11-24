---
対象期間: 2026年11月22日 〜 2026年11月23日
作成日: 2026-11-23
---

# Claude Code 公式ドキュメント更新サマリ

```markdown
**今回は、GitHub のプルリクエスト向けのエージェントの組「Claude Ship」の 16 ページが加わりました。修正をプッシュする PR Steward（5 ページ）、ポリシーファイルで承認者の数を決める Claude Approvals（7 ページ）、手元のセッションで同じ仕事をする `/ship`・`/steward` のコマンド（2 ページ）に、Claude Ship の総覧とセッションの共有のページです。Code Review の設定の置き場所も「Organization settings > Claude Ship」になりました**。`llms.txt` の URL は 205 から 221 になり、changelog には v2.1.331 が加わりました。新規ページ以外に 50 行以上変わったページはありません。`llms-full.txt` ではページの並びと重複して載るページが替わったので、生の差分（追加 69,617・削除 64,134）は実際の変更よりずっと大きく見えます。総行数は 130,779 行から 136,262 行になりました。

主要なものを以下に挙げます。

1. Code Review・PR Steward・Claude Approvals の 3 つのエージェントが「Claude Ship」としてまとめて載り、Code Review の設定が「Organization settings > Claude Ship」に移った。リポジトリに `.claude/approvals.yml` があると、Code Review の自動のレビューが止まることがある
2. PR Steward が、チームの GitHub のプルリクエストで、落ちたチェック・マージの競合・レビューのコメントに修正のコミットをプッシュする。承認とマージはしない設計で、組織の usage credits に課金される（Team と Enterprise のパブリックベータ）
3. Claude Approvals は、`.claude/approvals.yml` のルールに従って、誰がまだ承認しなければならないかを「Claude Approvals」のチェックで示す。observe モードから始めてから強制に切り替え、Code Review の結果や自分で定義した分類器の答えで、必要な人数を変えられる
4. `/ship` は、手元の Claude Code の CLI でコミット・プッシュ・プルリクエストを作ってレビューし、その後フィードバックと落ちたチェックに対応し続ける（watch）。`/steward` はレビューを省いて watch だけを始める。v2.1.330 以降が要る
5. `claude-code-on-the-web` にあったセッションの共有の説明が、新しいページ `share-sessions` に移って広がった。共有を受けた人に見える内容、共有をやめる方法、リンクが開かなくなる場合が載っている
```

## ハイライト

1. [**GitHub のプルリクエスト向けのエージェントの組 Claude Ship が載った**](./latest-detail.md#1-github-のプルリクエスト向けのエージェントの組-claude-ship-が載った):  
  新しいページ `claude-ship` が、Code Review・PR Steward・Claude Approvals の 3 つのエージェントと、オンにする順・課金・オフにする順をまとめます。Code Review の設定の置き場所は「Admin settings > Claude Code」の「Code review」の節から「Organization settings > Claude Ship」になり、`code-review-setup` などの手順もそれに合わせて書き直されました
2. [**修正をプッシュするエージェント PR Steward が載った**](./latest-detail.md#2-修正をプッシュするエージェント-pr-steward-が載った):  
  PR Steward は、落ちたチェック・マージの競合・人とレビューボットのコメントに対して、クラウドセッションで修正を作ってプッシュします。リポジトリごとに **Manual (@claude steward)**・**On**・**On (including drafts)**・**Off** から始まり方を選び、開発者は自分のプルリクエストでの動きを設定で絞れます。概要・セットアップ・プルリクエストでの使い方・アクセスできる範囲・トラブルシューティングの 5 ページです
3. [**ポリシーファイルで承認者の数を決める Claude Approvals が載った**](./latest-detail.md#3-ポリシーファイルで承認者の数を決める-claude-approvals-が載った):  
  Claude Approvals は、既定のブランチの `.claude/approvals.yml` のルールに従って、パスごとに何人の承認が要るか、Claude が承認してよいかを決め、「Claude Approvals」のチェックで示します。条件では、プルリクエストの事実（変わった行の数・作者・向け先のブランチなど）や、`claude/code_review` などの分類器の答えを読めます。概要・セットアップ・プルリクエストでの扱い・GitHub のルールとの関係・ポリシーファイルのリファレンス・分類器・トラブルシューティングの 7 ページです
4. [**`/ship` と `/steward` のコマンドが載った**](./latest-detail.md#4-ship-と-steward-のコマンドが載った):  
  `/ship` は、手元のクローンで変更をコミット・プッシュしてプルリクエストを開き、`/code-review` でレビューした後、セッションの中でプルリクエストを見守り（watch）、フィードバックと落ちたチェックに修正をプッシュします。`/steward` はレビューを省いて watch だけを始めます。`commands`・`skills`・`env-vars` にも載りました
5. [**セッションの共有が独立したページになった**](./latest-detail.md#5-セッションの共有が独立したページになった):  
  新しいページ `share-sessions` が、クラウドと Remote Control のセッションをリンクで共有したときに受けた人に見えるもの、共有の仕方、共有のやめ方、うまくいかないときの対処をまとめます。`claude-code-on-the-web` の「Share sessions」はこのページへの案内の 1 文になりました

## 新規追加されたページ

- [**Share a cloud or Remote Control session**](./latest-detail.md#1-share-a-cloud-or-remote-control-session) ([日本語](https://code.claude.com/docs/ja/share-sessions) / [English](https://code.claude.com/docs/en/share-sessions)):  
  クラウドと Remote Control のセッションをリンクで共有したとき、受けた人に何が見えるか、誰が開けるか、共有のやめ方、うまくいかないときの対処をまとめたページです（詳細はハイライト 5 参照）
- [**Claude Ship**](./latest-detail.md#2-claude-ship) ([日本語](https://code.claude.com/docs/ja/claude-ship) / [English](https://code.claude.com/docs/en/claude-ship)):  
  Code Review・PR Steward・Claude Approvals の 3 つのエージェントの役割、オンにする順、プランと課金、オフにする順をまとめた総覧のページです（詳細はハイライト 1 参照）
- [**PR Steward**](./latest-detail.md#3-pr-steward) ([日本語](https://code.claude.com/docs/ja/pr-steward) / [English](https://code.claude.com/docs/en/pr-steward)):  
  プルリクエストに修正をプッシュするエージェントの概要です。いつ始まるか、何を直すか、止め方、auto-fix と `/steward` との違い、使える組織、費用を述べます（詳細はハイライト 2 参照）
- [**Set up PR Steward**](./latest-detail.md#4-set-up-pr-steward) ([日本語](https://code.claude.com/docs/ja/pr-steward-setup) / [English](https://code.claude.com/docs/en/pr-steward-setup)):  
  Owner が PR Steward をオンにする手順です。ブランチのルールでレビューを求める、リポジトリを加える、支出の上限を決める、始まり方と対象の作者を選ぶ、ビルドの環境を用意する、オフにする、を扱います
- [**Work with PR Steward on a pull request**](./latest-detail.md#5-work-with-pr-steward-on-a-pull-request) ([日本語](https://code.claude.com/docs/ja/pr-steward-pull-requests) / [English](https://code.claude.com/docs/en/pr-steward-pull-requests)):  
  PR Steward がプルリクエストに加えるラベル・コメント・コミット、既定の指示、指示の与え方（コメント・自分の設定・リポジトリの `.claude/skills/steward/SKILL.md`）、始め方と止め方をまとめた開発者向けのページです
- [**What PR Steward can access**](./latest-detail.md#6-what-pr-steward-can-access) ([日本語](https://code.claude.com/docs/ja/pr-steward-security) / [English](https://code.claude.com/docs/en/pr-steward-security)):  
  PR Steward の GitHub の ID・権限・トークン、セッションの環境、承認とマージへの制限（Anthropic のサービスが拒む要求と、GitHub のブランチのルールに任される要求）をまとめたページです
- [**Troubleshoot PR Steward**](./latest-detail.md#7-troubleshoot-pr-steward) ([日本語](https://code.claude.com/docs/ja/pr-steward-troubleshooting) / [English](https://code.claude.com/docs/en/pr-steward-troubleshooting)):  
  PR Steward が始まらない・止まった・一時停止したときの原因と、PR Steward のコメントの文言ごとの対処、auto-fix が使えないとき、セットアップ中のメッセージをまとめたページです
- [**Claude Approvals**](./latest-detail.md#8-claude-approvals) ([日本語](https://code.claude.com/docs/ja/approvals) / [English](https://code.claude.com/docs/en/approvals)):  
  ポリシーファイルに従って承認者を数えるチェックの概要です。プルリクエストでの見え方、ポリシーの例、使える組織、人が見ないマージ、自動のレビューへの影響、課金を述べます（詳細はハイライト 3 参照）
- [**Set up Claude Approvals**](./latest-detail.md#9-set-up-claude-approvals) ([日本語](https://code.claude.com/docs/ja/approvals-setup) / [English](https://code.claude.com/docs/en/approvals-setup)):  
  2 つの初めのポリシー、observe モードでオンにする手順、強制への切り替えと必須のチェックの設定、支出の抑え方、オフにする順をまとめたページです
- [**Work with Claude Approvals on a pull request**](./latest-detail.md#10-work-with-claude-approvals-on-a-pull-request) ([日本語](https://code.claude.com/docs/ja/approvals-pull-requests) / [English](https://code.claude.com/docs/en/approvals-pull-requests)):  
  「Claude Approvals」のチェックの題ごとの意味と次にすること、observe モードでの扱い、コメントのコマンド、Claude・フォーク・外部の貢献者のプルリクエストの扱いをまとめたページです
- [**Claude Approvals and your GitHub rules**](./latest-detail.md#11-claude-approvals-and-your-github-rules) ([日本語](https://code.claude.com/docs/ja/approvals-github-rules) / [English](https://code.claude.com/docs/en/approvals-github-rules)):  
  人が見ずにマージされうる場合、GitHub の必須のレビューと CODEOWNERS、auto-merge とマージキュー、誰がポリシーを変えられるか、をまとめた管理者向けのページです
- [**Claude Approvals policy file reference**](./latest-detail.md#12-claude-approvals-policy-file-reference) ([日本語](https://code.claude.com/docs/ja/approvals-policy) / [English](https://code.claude.com/docs/en/approvals-policy)):  
  `.claude/approvals.yml` のキー、ルールが 1 つの判定にまとまる仕組み、承認の数え方、保護されたファイル、大きさと数の上限のリファレンスです
- [**Claude Approvals classifiers**](./latest-detail.md#13-claude-approvals-classifiers) ([日本語](https://code.claude.com/docs/ja/approvals-classifiers) / [English](https://code.claude.com/docs/en/approvals-classifiers)):  
  ルールが読む分類器（Anthropic が用意する `claude/code_review`・`claude/diff` と、`.claude/classifiers/` で定義する自分の分類器）の書き方・読み方・動き方・費用をまとめたページです
- [**Troubleshoot Claude Approvals**](./latest-detail.md#14-troubleshoot-claude-approvals) ([日本語](https://code.claude.com/docs/ja/approvals-troubleshooting) / [English](https://code.claude.com/docs/en/approvals-troubleshooting)):  
  チェックが出ない・通らない、ポリシーファイルが拒まれる、分類器が答えない、ときの原因と対処をまとめたページです
- [**Get a pull request ready with /ship and /steward**](./latest-detail.md#15-get-a-pull-request-ready-with-ship-and-steward) ([日本語](https://code.claude.com/docs/ja/ship-command) / [English](https://code.claude.com/docs/en/ship-command)):  
  手元のセッションでプルリクエストを開いてレビューし、watch でフィードバックと落ちたチェックに対応する 2 つのコマンドの使い方・制限・引数のページです（詳細はハイライト 4 参照）
- [**Troubleshoot /ship and /steward**](./latest-detail.md#16-troubleshoot-ship-and-steward) ([日本語](https://code.claude.com/docs/ja/ship-command-troubleshooting) / [English](https://code.claude.com/docs/en/ship-command-troubleshooting)):  
  `/ship` と `/steward` が出ない・始まらない、何もコミットもプッシュもしない、watch が始まらない・止まった、ときのメッセージと対処をまとめたページです

## 大幅に更新されたページ

（今回の対象期間に、既存のページで 50 行以上変わったページはありません。いちばん多いのは `code-review-setup` の 37 行（追加 24・削除 13）で、内容はハイライト 1 にまとめました）

## 新着情報

（今回の差分に新着情報（`whats-new/`）のページはありません。head の `llms.txt`・`llms-full.txt`・見出しマップにも whats-new のページは載っていません）

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-11-22.md](./archives/latest/2026-11-22.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-11-22.md](./archives/latest-detail/2026-11-22.md)

<!--
base_commit: 6a68e6de41597850d1e2183445a9fc2df1e65fdf
head_commit: 6b8844c93bee3ab36c9d7bb656a2476fb661c469
generated_at_full: 2026-11-24T15:21:26+09:00
-->
