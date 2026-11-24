---
対象期間: 2026年11月22日 〜 2026年11月23日
作成日: 2026-11-23
---

# Claude Code 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
**今回は、GitHub のプルリクエスト向けのエージェントの組「Claude Ship」の 16 ページが加わりました。修正をプッシュする PR Steward（5 ページ）、ポリシーファイルで承認者の数を決める Claude Approvals（7 ページ）、手元のセッションで同じ仕事をする `/ship`・`/steward` のコマンド（2 ページ）に、Claude Ship の総覧とセッションの共有のページです。Code Review の設定の置き場所も「Organization settings > Claude Ship」になりました**。`llms.txt` の URL は 205 から 221 になり、changelog には v2.1.331 が加わりました。新規ページ以外に 50 行以上変わったページはありません。`llms-full.txt` ではページの並びと重複して載るページが替わったので、生の差分（追加 69,617・削除 64,134）は実際の変更よりずっと大きく見えます。総行数は 130,779 行から 136,262 行になりました。

主要なものを以下に挙げます。

1. Code Review・PR Steward・Claude Approvals の 3 つのエージェントが「Claude Ship」としてまとめて載り、Code Review の設定が「Organization settings > Claude Ship」に移った。リポジトリに `.claude/approvals.yml` があると、Code Review の自動のレビューが止まることがある
2. PR Steward が、チームの GitHub のプルリクエストで、落ちたチェック・マージの競合・レビューのコメントに修正のコミットをプッシュする。承認とマージはしない設計で、組織の usage credits に課金される（Team と Enterprise のパブリックベータ）
3. Claude Approvals は、`.claude/approvals.yml` のルールに従って、誰がまだ承認しなければならないかを「Claude Approvals」のチェックで示す。observe モードから始めてから強制に切り替え、Code Review の結果や自分で定義した分類器の答えで、必要な人数を変えられる
4. `/ship` は、手元の Claude Code の CLI でコミット・プッシュ・プルリクエストを作ってレビューし、その後フィードバックと落ちたチェックに対応し続ける（watch）。`/steward` はレビューを省いて watch だけを始める。v2.1.330 以降が要る
5. `claude-code-on-the-web` にあったセッションの共有の説明が、新しいページ `share-sessions` に移って広がった。共有を受けた人に見える内容、共有をやめる方法、リンクが開かなくなる場合が載っている
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**GitHub のプルリクエスト向けのエージェントの組 Claude Ship が載った**](#1-github-のプルリクエスト向けのエージェントの組-claude-ship-が載った):  
  新しいページ `claude-ship` が、Code Review・PR Steward・Claude Approvals の 3 つのエージェントと、オンにする順・課金・オフにする順をまとめます。Code Review の設定の置き場所は「Admin settings > Claude Code」の「Code review」の節から「Organization settings > Claude Ship」になり、`code-review-setup` などの手順もそれに合わせて書き直されました
2. [**修正をプッシュするエージェント PR Steward が載った**](#2-修正をプッシュするエージェント-pr-steward-が載った):  
  PR Steward は、落ちたチェック・マージの競合・人とレビューボットのコメントに対して、クラウドセッションで修正を作ってプッシュします。リポジトリごとに **Manual (@claude steward)**・**On**・**On (including drafts)**・**Off** から始まり方を選び、開発者は自分のプルリクエストでの動きを設定で絞れます。概要・セットアップ・プルリクエストでの使い方・アクセスできる範囲・トラブルシューティングの 5 ページです
3. [**ポリシーファイルで承認者の数を決める Claude Approvals が載った**](#3-ポリシーファイルで承認者の数を決める-claude-approvals-が載った):  
  Claude Approvals は、既定のブランチの `.claude/approvals.yml` のルールに従って、パスごとに何人の承認が要るか、Claude が承認してよいかを決め、「Claude Approvals」のチェックで示します。条件では、プルリクエストの事実（変わった行の数・作者・向け先のブランチなど）や、`claude/code_review` などの分類器の答えを読めます。概要・セットアップ・プルリクエストでの扱い・GitHub のルールとの関係・ポリシーファイルのリファレンス・分類器・トラブルシューティングの 7 ページです
4. [**`/ship` と `/steward` のコマンドが載った**](#4-ship-と-steward-のコマンドが載った):  
  `/ship` は、手元のクローンで変更をコミット・プッシュしてプルリクエストを開き、`/code-review` でレビューした後、セッションの中でプルリクエストを見守り（watch）、フィードバックと落ちたチェックに修正をプッシュします。`/steward` はレビューを省いて watch だけを始めます。`commands`・`skills`・`env-vars` にも載りました
5. [**セッションの共有が独立したページになった**](#5-セッションの共有が独立したページになった):  
  新しいページ `share-sessions` が、クラウドと Remote Control のセッションをリンクで共有したときに受けた人に見えるもの、共有の仕方、共有のやめ方、うまくいかないときの対処をまとめます。`claude-code-on-the-web` の「Share sessions」はこのページへの案内の 1 文になりました
<!-- light:highlight-list:end -->

## 1. GitHub のプルリクエスト向けのエージェントの組 Claude Ship が載った

**新しいページ `claude-ship` は、チームの GitHub のプルリクエストをマージできる状態にするためのエージェントの組として、Claude Ship を紹介します。** 組になっているのは次の 3 つです。

- **Code Review**: ロジックの誤り・セキュリティの脆弱性・壊れたエッジケースのような問題を探し、該当する行へのインラインのコメントで、重大度の順に知らせる（一般提供）
- **PR Steward**: レビューのフィードバックと落ちたチェックに取り組み、修正のコミットをプッシュする。プルリクエストを承認もマージもしない設計（パブリックベータ。ハイライト 2）
- **Claude Approvals**: 自分で書いた承認のポリシーに照らしてプルリクエストを確かめるチェック（パブリックベータ。ハイライト 3）

3 つを合わせると、プルリクエストをレビュー・修正・承認の判断まで運べますが、何がマージされるかは設定と GitHub のブランチのルールが決めます。Team と Enterprise のプラン向けで、Zero Data Retention をオンにした組織、HIPAA の構成を当てた組織、顧客管理の暗号鍵を使う組織では使えません。各エージェントはトークンの使用量に応じて組織の usage credits に課金され、プランに含まれる使用量とは別です。**Organization settings > Usage** で usage credits をオフにしても、オンのエージェントは動き続けて課金を続けます。

オンにするのは、1 つのリポジトリで 1 つずつ、Code Review → PR Steward（始まり方はまず **Manual (@claude steward)** にし、自分で設定するまで PR Steward 自身の支出の上限はない）→ Claude Approvals（observe モードから始める。observe モードも課金される）の順です。オフにするのは逆に Approvals → PR Steward → Code Review の順で、これは Code Review がオフのところでもポリシーが課金されるレビューを始められるからです。この手順では `/ship` と `/steward` のコマンドは残ります（ハイライト 4）。

**Code Review の設定の置き場所が替わりました。** `claude-ship` の「If you already use Code Review」は、Code Review の設定が **Organization settings > Claude Ship** に移った、と述べ、`code-review-setup` も次のように書き直されました（リンク先の URL は `claude.ai/admin-settings/claude-code#code-review` のまま。Claude Ship のページ自身は `claude.ai/admin-settings/claude-ship` にリンクしています）。

- **オンにする手順**: 1 の「**Allow code review** のスイッチをクリックする」が「**Review** の下のスイッチをオンにし、**Turn on Code review** のダイアログで **Turn on** をクリックする」に、5 の「**Finish** をクリックする」が「**Turn on** をクリックする」になった。5 の **Choose what Claude does on these repositories** のダイアログでは **Code review** を選んだままにし、**Steward** が選ばれていれば、PR Steward もオンにしたいのでなければ外す。ほかの閉じ方をすると、リポジトリは加わるが何もオンにならない
- **リポジトリを加える**: **Add** の先に **Connect GitHub** のダイアログが出たときの項目と、組織の最初のリポジトリなら **Choose what Claude does on these repositories** のダイアログが続く、という項目が加わった
- **レビューをいつ走らせるか**: **Edit** のダイアログの **Review runs** のメニューの画像が加わり、表の列の名前が **Review runs** から **Code review** になった
- **止める**: 「Everything」が「**Review** の下のスイッチをオフにする」になり、リポジトリの **Code review** のスイッチか **Review** の下のスイッチがオフでも、Claude Approvals のポリシーは課金されるレビューを始められる（止めるにはポリシーを変えるか Approvals をオフにする。Code Review の支出の上限はそれらにも効く）、という段落が加わった

`code-review-costs`・`code-review-troubleshooting`・`github-enterprise-server` の手順の場所も **Organization settings > Claude Ship** になりました。`code-review-costs` の「Estimate your spend」では、平均の費用を読むのが **Repositories** の表の **Average cost** の列から、各リポジトリの行の **Edit** の **Cost** の下になっています。

**Claude Approvals のポリシーファイルは Code Review の自動のレビューを変えます。** `.claude/approvals.yml` が既定のブランチに入ると、observe モードでも強制でも、合うルールが `claude/code_review` を名指さないところでは自動のレビューがふつう止まります。残すには、ルールの `advisory` に `claude/code_review` を加えます。Code Review の側のページにも、これに合わせた文が加わりました。

- **`code-review`・`code-review-pull-requests`**: レビューはそれだけではプルリクエストを承認もブロックもしない（これまでは「決して承認もブロックもしない」）。Claude Approvals のポリシーファイルが使うリポジトリでは、レビューの結果が承認の数に入り、ポリシーは自動のレビューを受けるプルリクエストを変えることもある
- **`code-review-pull-requests` の「Respond to findings」**: スレッドを自分で解決しても、プルリクエストに Claude Approvals のチェックがあれば、そのチェックがその解決を数えないことがある。PR Steward が働くプルリクエストでは、Important の指摘に PR Steward が自分の修正をプッシュすることがあるので、作業を始める前にブランチをプルする。「Code review not repeated — earlier findings still open」には、Claude Approvals がスレッドを開き直したときの対処が加わった
- **`code-review-troubleshooting`**: 表に「**Code review not run: no policy rule uses it**」の行と、同名の h3 ができた。ポリシーがこのプルリクエストにレビューを求めていないという意味で、`@claude review` とコメントすればレビューを受けられ、自動のレビューを戻すには、`verdict` を持ち変わったファイルに合うルールで Code Review を名指す。Code Review がオンでないリポジトリでも、Claude のレビューを読むポリシーがあれば、`@claude review` だけの新しいコメントでレビューが始まることがある、という文も加わった
- **`code-review-costs`・`code-review-setup`**: Claude Approvals のポリシーファイルのあるリポジトリでは、**Review runs** の設定なら始まらないレビューが始まることがあり、自動のレビューが止まることもある

`llms.txt` の「Code review and pull requests」も組み替えられました。`code-review-local` と `ultrareview` の 2 行が外れて「Claude Ship」の行が先頭に来て、小見出し「Code Review」の後ろに「PR Steward」「Claude Approvals」「/ship and /steward」「On-demand reviews」の小見出しができています。`code-review-local` と `ultrareview` は「On-demand reviews」に移っただけで、`llms-full.txt` の本文は変わっていません。`feature-availability` の、Claude のサブスクリプションが要る機能の一覧とプランごとの表にも、PR Steward と Claude Approvals（どちらも Team と Enterprise）が加わりました。

- [Claude Ship - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/claude-ship#claude-ship-agents)
- [Claude Ship - Claude Code Docs (English)](https://code.claude.com/docs/en/claude-ship#claude-ship-agents)
- [Code Review を設定する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/code-review-setup#turn-on-code-review)
- [Set up Code Review - Claude Code Docs (English)](https://code.claude.com/docs/en/code-review-setup#turn-on-code-review)

## 2. 修正をプッシュするエージェント PR Steward が載った

**PR Steward は、チームの開いている GitHub のプルリクエストで働くエージェントです。** 落ちたチェック・マージの競合・レビューのフィードバックを GitHub で拾い、クラウドセッションで修正を作り、コミットとコメントでプルリクエストに報告します。Claude GitHub App として動き、組織に課金されます。Team と Enterprise のプランのパブリックベータで、github.com と、ポート 443 でつないだ GitHub Enterprise Server のリポジトリで動きます。

- **取り組むもの**: プルリクエストが触れたコードに原因がある落ちたチェック、ベースのブランチを取り込んで解く競合、人のレビューのコメント（小さく具体的な変更。大きな依頼や設計の話にはプッシュせずに返事をすることがある）、Code Review が **Important** とした指摘（ほかのボットなら lint の指摘とバグ）、コミットで直せるものを待っている Claude Approvals のチェック
- **始まり方**: リポジトリが **On** なら、プルリクエストを開く・開き直す・ドラフトをレビューの準備ができたにすると始まる。ドラフト・フォークからのもの・ボットが開いたもの・書き込みの権限のない作者のものは飛ばす。**Manual (@claude steward)** なら、書き込みの権限のある人が `@claude steward` とコメントするか `claude-pr-steward-watching` のラベルを付けると始まる
- **止め方**: ラベルを外すか `@claude stop` とコメントする。自分がこれから開くプルリクエストについては、claude.ai の **Settings > Code**（または **Settings > Claude Code**）の **PR Steward** で、**Off**・**Only when tagged**・**Act on its own**・**Customize** から選ぶ
- **承認とマージ**: PR Steward はプルリクエストを承認もマージもしない設計で、Anthropic がホストする環境では、承認・ブランチの保護やルールセットの変更・ブランチの削除・タグのプッシュの要求を Anthropic のサービスが拒む。マージ・auto-merge・force-push は GitHub のブランチのルールに任されるので、ブランチのルールでレビューを求め、Claude GitHub App をバイパスの一覧に入れない

クラウドセッションの auto-fix や `/steward` のコマンドとの違いは、それらが自分のセッションで自分として動き、自分の使用量に数えられる点です。PR Steward が見守るプルリクエストに auto-fix を頼むと失敗し、`claude-code-on-the-web` の「Auto-fix pull requests」にも、PR Steward が働くリポジトリでは **Auto-fix** のトグルが使えない、という段落が加わりました。`cloud-environments`・`self-hosted-environments-configuration` にも、PR Steward のセッションが読み込むリポジトリの構成は少なく、セルフホストのランナーからは `CLAUDE.md` やルールのファイルを読み込まない（既定のブランチのものを読む）、という注記が加わっています。各ページの内容は新規ページ 3〜7 にまとめました。

- [PR Steward - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/pr-steward#what-pr-steward-fixes)
- [PR Steward - Claude Code Docs (English)](https://code.claude.com/docs/en/pr-steward#what-pr-steward-fixes)

## 3. ポリシーファイルで承認者の数を決める Claude Approvals が載った

**Claude Approvals は、GitHub のプルリクエストに「Claude Approvals」のチェックを加え、誰がまだ承認しなければならないかを示します。** 従うのはリポジトリのポリシーファイル `.claude/approvals.yml` で、パスごとに何人の承認が要るか、どこで Claude が承認してよいかを決められます。たとえば、課金のコードには 2 人、テストのフィクスチャーには Code Review が通れば 1 人、といった具合です。チェックがマージを止めるのは、GitHub で必須のチェックにしたところだけで、observe モードではふつう止めません。

- **ルール**: `paths` で対象のファイルを決め、`verdict` で `claude`（`approves`・`comments`・`blocks`）と `seats`（承認する人の数か、人の組）を決める。`if` と `override` の条件では、`pr/files_changed` や `pr/authors` のようなプルリクエストの事実と分類器の答えを読める。CI の結果は条件で読めないので、CI は GitHub の別の必須のチェックにしておく
- **分類器**: `claude/code_review`（Code Review が通ったか）と `claude/diff`（承認の後にどれだけ変わったか）を Anthropic が用意し、`.claude/classifiers/<name>/def.yml` で自分の分類器も定義できる。分類器の実行は組織の usage credits に課金される
- **始め方**: ポリシーファイルを既定のブランチにマージした人が誰でも Approvals をオンにできる（Owner は組織全体でオフにできる）。まず observe モードで、チェックの題がレビュアーの判断と合うのを確かめてから、`mode: observe` の行を消して強制し、GitHub で必須のチェックにする
- **人が見ないマージ**: `seats: 1`（作者が 1 席を埋められる）や `seats: 0`、`claude: approves`、GitHub の auto-merge やマージキューでは、作者のほかに誰も見ずにマージされうる。全パスで作者でない 1 人を求めるルールの例が `approvals-github-rules` にある

Claude Approvals は Team と Enterprise のプランのパブリックベータで、github.com（GitHub Enterprise Cloud を含む）で動きます。Zero Data Retention・HIPAA の構成・CMEK では使えず、FERPA か Access Transparency の設定では始められません。各ページの内容は新規ページ 8〜14 にまとめました。

- [Claude Approvals - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/approvals#example-policy)
- [Claude Approvals - Claude Code Docs (English)](https://code.claude.com/docs/en/approvals#example-policy)
- [Claude Approvals ポリシーファイルリファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/approvals-policy#how-a-policy-file-works)
- [Claude Approvals policy file reference - Claude Code Docs (English)](https://code.claude.com/docs/en/approvals-policy#how-a-policy-file-works)

## 4. `/ship` と `/steward` のコマンドが載った

**`/ship` は、手元の Claude Code の CLI から、変更をプルリクエストにしてマージできる状態に近づけるコマンドです。** ブランチにプルリクエストがなければ、コミット・プッシュ・プルリクエストの作成を自分として行い、`/code-review` でレビューした後、セッションの中でプルリクエストを見守り続けます（この続く仕事を watch と呼びます）。watch では、落ちたチェック・マージの競合・レビュアーのコメント・自分のレビューの指摘に取り組み、修正をプッシュします。マージは自分で行います。`/steward` は、すでに開いている自分のプルリクエストで、レビューを省いて watch だけを始めます。

- **前提**: Claude Code v2.1.330 以降、`gh auth login` でサインインした GitHub CLI 2.63 以降、git 2.38 以降。ターミナルの CLI で、リポジトリの手元のクローンから実行し、クラウドセッションにはない。無人で任せるなら auto モードを選び、`bypassPermissions` モードと native Windows では watch が始まらない
- **watch の制限**: Claude があなたからのメッセージなしに動くとき、Claude Code はプルリクエストをマージ・承認する、auto-merge をオンにする、force-push する `gh` と `git` のコマンドを止め、`gh` と `git` のコマンドを短い一覧に絞り、コネクター・`WebFetch`・`WebSearch` のような要らないツールを拒む。ただし `gh` と `git` は自分のサインインで動くので、ブランチのルールが自分だけでのマージを許すなら、マージされうる
- **任せてよい場所**: ベースのブランチへマージできる人と自分のブランチへプッシュできる人を全員信頼できるところだけで watch を動かす。その人たちは自分のコンピューターで自分の資格情報でプログラムを動かせる
- **組織でオフにする**: managed settings の `skillOverrides` で `ship-local`（`/ship` の裏のスキル）と `steward` を `"off"` にする

ほかのページにも載りました。`commands` の表には `/ship [level] [pr] [+bot]`・`/ship:review`（`/code-review` の別名）・`/steward [pr] [+bot]`（別名 `/ship:steward`）の行が加わり、`skills` の「Resolve skills that share a name」には、`ship`・`ship-local`・`steward` という名前の自分のスキルかコマンドは、`/ship` が使えるところでは読み込まれない、という行が加わりました。`env-vars` の「Features that need feature-flag fetching」には `/ship` と `/steward` を実行する、が加わっています（フィーチャーフラグの取得をオフにしたセッションでは使えない）。`champion-kit` と `communications-kit` のスキルの例の名前は、`/ship` から `/precommit` に替わりました。各ページの内容は新規ページ 15・16 にまとめました。

- [/ship と /steward でプルリクエストをマージ可能な状態にする - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/ship-command#what-claude-code-blocks-during-a-watch)
- [Get a pull request ready with /ship and /steward - Claude Code Docs (English)](https://code.claude.com/docs/en/ship-command#what-claude-code-blocks-during-a-watch)
- [コマンド - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/commands#all-commands)
- [Commands - Claude Code Docs (English)](https://code.claude.com/docs/en/commands#all-commands)

## 5. セッションの共有が独立したページになった

**`claude-code-on-the-web` の「Share sessions」にあった共有の説明（h4「Share from an Enterprise or Team account」「Share from a Max, Ultra, or Pro account」を含む）が、新しいページ `share-sessions` に移りました。** 元の節は、リンクでセッションを共有する方法・受けた人が読めるもの・共有のやめ方は `share-sessions` を見る、という 1 文になっています。`remote-control` の「What connected devices see」の共有のリンクのリンク先も、`claude-code-on-the-web#share-sessions` から `share-sessions` になりました。

新しいページは、クラウドのセッションと Remote Control のセッションの両方を扱い、これまでの内容に次のことが加わっています（ページの詳細は新規ページ 1）。

- **受けた人に見えるもの**: メッセージ・コードとコマンドの出力・メッセージやファイルに出た鍵やトークン・GitHub の検索の結果（受けた人が開けない非公開のリポジトリも含みうる）・コネクターの結果・Web の内容・使ったコネクターとスキルとプラグインの名前。Remote Control のセッションでは、セッションを始めたフォルダーの外のファイルの中身や、Claude in Chrome で開いたページも見える
- **見え方の更新**: 受けた人の画面はリアルタイムでは更新されないが、読み込み直すと、共有をやめるまでに加わったメッセージが見える
- **リポジトリへのアクセス**: Enterprise と Team では、共有したクラウドのセッションを開くには、その非公開のリポジトリのそれぞれに、つないだ GitHub のアカウントでアクセスできることが要る（これまでの「確かめる設定が既定でオン」から変わった書き方）。Max・Ultra・Pro では **Require repository access** が既定でオフ。どちらも、Remote Control のセッションのリンクは、リポジトリにアクセスできない人でも開けることがある
- **共有をやめる**: 表示範囲を **Private** に戻す。セッションをアーカイブしても、Remote Control をオフにしても、組織を離れても、リンクは開けるままになる
- **うまくいかないとき**: 組織で共有がオフ（Owner が **Organization settings > Data and privacy** の **Share cloud sessions** をオンにする。Remote Control のセッションの共有にもこの設定が要る）、共有できないセッション（Enterprise と Team でアップロードしたコードのクラウドのセッションなど）、リンクが開かなくなる原因と、リンクを戻せない場合

これまでの節の、Team の表示範囲は claude.ai の組織のほかのメンバーに見せる、Public は claude.ai にログインしたどのユーザーにも見せる、という説明は、新しいページでは各プランの節の冒頭の「開けることがある（may be able to）」という書き方になりました。表示名がすべての受けた人に見える、という項目は「What recipients see」に移っています。Claude in Slack のセッションは自動で Team の表示範囲で共有される、という項目は、`share-sessions` には引き継がれていません。`slack` のページには、Enterprise と Team のアカウントで Claude in Slack から作ったセッションは組織から自動で見える、という文が残っていて、その案内のリンクは 1 文の案内になった `claude-code-on-the-web#share-sessions` を指したままです。

- [クラウドセッションまたは Remote Control セッションを共有する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/share-sessions#what-recipients-see)
- [Share a cloud or Remote Control session - Claude Code Docs (English)](https://code.claude.com/docs/en/share-sessions#what-recipients-see)

## 新規追加されたページ

<!-- light:new-pages:start -->
- [**Share a cloud or Remote Control session**](#1-share-a-cloud-or-remote-control-session) ([日本語](https://code.claude.com/docs/ja/share-sessions) / [English](https://code.claude.com/docs/en/share-sessions)):  
  クラウドと Remote Control のセッションをリンクで共有したとき、受けた人に何が見えるか、誰が開けるか、共有のやめ方、うまくいかないときの対処をまとめたページです（詳細はハイライト 5 参照）
- [**Claude Ship**](#2-claude-ship) ([日本語](https://code.claude.com/docs/ja/claude-ship) / [English](https://code.claude.com/docs/en/claude-ship)):  
  Code Review・PR Steward・Claude Approvals の 3 つのエージェントの役割、オンにする順、プランと課金、オフにする順をまとめた総覧のページです（詳細はハイライト 1 参照）
- [**PR Steward**](#3-pr-steward) ([日本語](https://code.claude.com/docs/ja/pr-steward) / [English](https://code.claude.com/docs/en/pr-steward)):  
  プルリクエストに修正をプッシュするエージェントの概要です。いつ始まるか、何を直すか、止め方、auto-fix と `/steward` との違い、使える組織、費用を述べます（詳細はハイライト 2 参照）
- [**Set up PR Steward**](#4-set-up-pr-steward) ([日本語](https://code.claude.com/docs/ja/pr-steward-setup) / [English](https://code.claude.com/docs/en/pr-steward-setup)):  
  Owner が PR Steward をオンにする手順です。ブランチのルールでレビューを求める、リポジトリを加える、支出の上限を決める、始まり方と対象の作者を選ぶ、ビルドの環境を用意する、オフにする、を扱います
- [**Work with PR Steward on a pull request**](#5-work-with-pr-steward-on-a-pull-request) ([日本語](https://code.claude.com/docs/ja/pr-steward-pull-requests) / [English](https://code.claude.com/docs/en/pr-steward-pull-requests)):  
  PR Steward がプルリクエストに加えるラベル・コメント・コミット、既定の指示、指示の与え方（コメント・自分の設定・リポジトリの `.claude/skills/steward/SKILL.md`）、始め方と止め方をまとめた開発者向けのページです
- [**What PR Steward can access**](#6-what-pr-steward-can-access) ([日本語](https://code.claude.com/docs/ja/pr-steward-security) / [English](https://code.claude.com/docs/en/pr-steward-security)):  
  PR Steward の GitHub の ID・権限・トークン、セッションの環境、承認とマージへの制限（Anthropic のサービスが拒む要求と、GitHub のブランチのルールに任される要求）をまとめたページです
- [**Troubleshoot PR Steward**](#7-troubleshoot-pr-steward) ([日本語](https://code.claude.com/docs/ja/pr-steward-troubleshooting) / [English](https://code.claude.com/docs/en/pr-steward-troubleshooting)):  
  PR Steward が始まらない・止まった・一時停止したときの原因と、PR Steward のコメントの文言ごとの対処、auto-fix が使えないとき、セットアップ中のメッセージをまとめたページです
- [**Claude Approvals**](#8-claude-approvals) ([日本語](https://code.claude.com/docs/ja/approvals) / [English](https://code.claude.com/docs/en/approvals)):  
  ポリシーファイルに従って承認者を数えるチェックの概要です。プルリクエストでの見え方、ポリシーの例、使える組織、人が見ないマージ、自動のレビューへの影響、課金を述べます（詳細はハイライト 3 参照）
- [**Set up Claude Approvals**](#9-set-up-claude-approvals) ([日本語](https://code.claude.com/docs/ja/approvals-setup) / [English](https://code.claude.com/docs/en/approvals-setup)):  
  2 つの初めのポリシー、observe モードでオンにする手順、強制への切り替えと必須のチェックの設定、支出の抑え方、オフにする順をまとめたページです
- [**Work with Claude Approvals on a pull request**](#10-work-with-claude-approvals-on-a-pull-request) ([日本語](https://code.claude.com/docs/ja/approvals-pull-requests) / [English](https://code.claude.com/docs/en/approvals-pull-requests)):  
  「Claude Approvals」のチェックの題ごとの意味と次にすること、observe モードでの扱い、コメントのコマンド、Claude・フォーク・外部の貢献者のプルリクエストの扱いをまとめたページです
- [**Claude Approvals and your GitHub rules**](#11-claude-approvals-and-your-github-rules) ([日本語](https://code.claude.com/docs/ja/approvals-github-rules) / [English](https://code.claude.com/docs/en/approvals-github-rules)):  
  人が見ずにマージされうる場合、GitHub の必須のレビューと CODEOWNERS、auto-merge とマージキュー、誰がポリシーを変えられるか、をまとめた管理者向けのページです
- [**Claude Approvals policy file reference**](#12-claude-approvals-policy-file-reference) ([日本語](https://code.claude.com/docs/ja/approvals-policy) / [English](https://code.claude.com/docs/en/approvals-policy)):  
  `.claude/approvals.yml` のキー、ルールが 1 つの判定にまとまる仕組み、承認の数え方、保護されたファイル、大きさと数の上限のリファレンスです
- [**Claude Approvals classifiers**](#13-claude-approvals-classifiers) ([日本語](https://code.claude.com/docs/ja/approvals-classifiers) / [English](https://code.claude.com/docs/en/approvals-classifiers)):  
  ルールが読む分類器（Anthropic が用意する `claude/code_review`・`claude/diff` と、`.claude/classifiers/` で定義する自分の分類器）の書き方・読み方・動き方・費用をまとめたページです
- [**Troubleshoot Claude Approvals**](#14-troubleshoot-claude-approvals) ([日本語](https://code.claude.com/docs/ja/approvals-troubleshooting) / [English](https://code.claude.com/docs/en/approvals-troubleshooting)):  
  チェックが出ない・通らない、ポリシーファイルが拒まれる、分類器が答えない、ときの原因と対処をまとめたページです
- [**Get a pull request ready with /ship and /steward**](#15-get-a-pull-request-ready-with-ship-and-steward) ([日本語](https://code.claude.com/docs/ja/ship-command) / [English](https://code.claude.com/docs/en/ship-command)):  
  手元のセッションでプルリクエストを開いてレビューし、watch でフィードバックと落ちたチェックに対応する 2 つのコマンドの使い方・制限・引数のページです（詳細はハイライト 4 参照）
- [**Troubleshoot /ship and /steward**](#16-troubleshoot-ship-and-steward) ([日本語](https://code.claude.com/docs/ja/ship-command-troubleshooting) / [English](https://code.claude.com/docs/en/ship-command-troubleshooting)):  
  `/ship` と `/steward` が出ない・始まらない、何もコミットもプッシュもしない、watch が始まらない・止まった、ときのメッセージと対処をまとめたページです
<!-- light:new-pages:end -->

**新規ページの数え方**: `llms.txt` の URL は 205 から 221 に、`llms-full.txt` の固有のページも 205 から 221 になりました。外れたページはありません。`llms.txt` では、`share-sessions` が「Claude Code in the cloud」の `claude-code-on-the-web` の後ろに、残る 15 ページが「Code review and pull requests」（ハイライト 1）に入っています。以下の行数は、`llms-full.txt` の中の各ページの行数です（16 ページで 2,733 行）。日本語版は 16 ページともあり、本文も訳されていました。

## 1. Share a cloud or Remote Control session

**`share-sessions`（114 行）は、クラウドのセッションか Remote Control のセッションをリンクで共有し、ほかの人に会話を読ませる方法のページです。** claude.ai のチャットの共有は別の記事を見る、という注記から始まり、h2「What recipients see」「Share a session」「Stop sharing a session」「Troubleshoot sharing」が続きます。

- **What recipients see**: 受けた人は、それまでの会話と Claude のツールの呼び出しとその結果を見る。メッセージ（プロンプト・加えた画像・添付したファイルの名前・Claude の返答と思考）、コードとコマンド、資格情報、ほかのリポジトリ（GitHub の検索の結果）、コネクターの結果（メール・文書・Slack のメッセージなど）、Web の内容（読んだページとスクリーンショット）、自分の構成（使ったコネクターの名前と、調べたコネクター・スキル・プラグインの名前と説明）の 7 つ。h3「What recipients see in a Remote Control session」では、自分のコンピューターで読んだファイル（始めたフォルダーの外のものも）と、Claude in Chrome で開いたページ（サインインしているサイトも）の文字とスクリーンショットが加わる
- **Share a session**: まずセッションを確かめ（h3「Check a session before you share」）、セッションの上の **Share** で **Team** か **Public** を選び、**Copy link** でリンクを送る。サーバーは一部の場合に共有を止めるが、共有を許したセッションにも機密の内容はありうる。Enterprise と Team の節（**Private** と **Team**）と、Max・Ultra・Pro の節（**Private** と **Public**、**Require repository access** は既定でオフ、**Show your name** をオフにすると名前を隠せる）がある
- **Stop sharing a session**: 表示範囲を **Private** に戻す。アーカイブしても、Remote Control をオフにするかターミナルを閉じても、組織を離れても（**Team** で共有したリンク）、リンクは開けるまま
- **Troubleshoot sharing**: h3「Sharing is turned off for your organization」（**Share** が「Sharing is disabled by your organization.」で薄くなっていたら、Owner に **Share cloud sessions** をオンにしてもらう）、「Sessions you can't share」（「This session can't be shared.」は再試行しても効かない）、「Links that stop opening」（表示範囲・Free プラン・リポジトリへのアクセス・アップロードしたコードか GitHub 以外のコード・無効なリンク・組織の設定・プランのアップグレードの 7 つの原因と、セッションの削除や Anthropic がリンクをオフにした場合など、リンクを戻せない 4 つの場合）

見出しの id には、見出しの文字列と違うものがあります。「Share from a Max, Ultra, or Pro account」は `#share-from-a-max-or-pro-account`、「Sessions you can't share」は `#unshareable-sessions` です。

- [クラウドセッションまたは Remote Control セッションを共有する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/share-sessions#links-that-stop-opening)
- [Share a cloud or Remote Control session - Claude Code Docs (English)](https://code.claude.com/docs/en/share-sessions#links-that-stop-opening)

## 2. Claude Ship

**`claude-ship`（103 行）は、Code Review・PR Steward・Claude Approvals の 3 つのエージェントの総覧です。** h2「Claude Ship agents」「Set up Claude Ship」「Plans and billing」「Turn off Claude Ship」があり、内容はハイライト 1 のとおりです。

「Claude Ship agents」には、プルリクエストでの各エージェントの役割と、自分と GitHub に残る役割の図があり、Claude Ship は AI を使うのでバグやセキュリティの脆弱性を見落とすことがある、という注記と、ポリシーが人の承認を求めないまま GitHub の auto-merge かマージキューを使うと、誰も手を出さずに変更がマージされうる、という警告が付いています。「Plans and billing」には、条件を満たす Enterprise の組織は Claude Ship の販促のクレジットを受け取れる、という注記もあります。自分のプルリクエストでレビューと修正を手元で得るなら `/ship` を使う、という案内も冒頭にあります。

- [Claude Ship - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/claude-ship#set-up-claude-ship)
- [Claude Ship - Claude Code Docs (English)](https://code.claude.com/docs/en/claude-ship#set-up-claude-ship)

## 3. PR Steward

**`pr-steward`（71 行）は、PR Steward の概要のページです。** h2「What PR Steward does on a pull request」（h3「When PR Steward starts」「What PR Steward fixes」「Stop or limit PR Steward」）と「Decide whether PR Steward fits your team」（h3「How PR Steward differs from auto-fix and /steward」「Availability」「What PR Steward costs」）があり、内容はハイライト 2 のとおりです。

見守っている間、PR Steward は尋ねずにコミットをプッシュしてコメントに返事をし、プルリクエストには `claude-pr-steward-watching` のラベルが付きます。費用はトークンで組織の usage credits に課金され、Owner が設定するまで PR Steward 自身の支出の上限はありません。

- [PR Steward - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/pr-steward#when-pr-steward-starts)
- [PR Steward - Claude Code Docs (English)](https://code.claude.com/docs/en/pr-steward#when-pr-steward-starts)

## 4. Set up PR Steward

**`pr-steward-setup`（210 行）は、Owner が組織と各リポジトリで PR Steward をオンにする手順のページです。** 前提は、Claude の組織の Owner の役割・usage credits・オンにした GitHub のコネクターと、GitHub の側の、Claude GitHub App を入れる組織の Owner・ブランチのルールを加えるリポジトリの Admin（非公開のリポジトリには有料の GitHub のプランも要る）・Claude につなぐアカウントのプッシュの権限です。

- **Require reviews with branch rules**: PR Steward をオンにする前に、既定のブランチで 1 人以上の承認を求めるルールを加え、新しいプッシュで古い承認を外すか最新のプッシュの承認を求め、Claude GitHub App（セルフホストならランナーの git の ID）をルールセットのバイパスの一覧に入れず、ほかのブランチも守る。Claude Approvals のポリシーが Claude の承認を許すところでは、Claude のレビューがその 1 人の承認になりうる
- **Turn on PR Steward and add repositories**: **Organization settings > Claude Ship** の **Repositories** の表から、リポジトリを加え、**Runs for** で対象の作者（**All eligible authors** か **Listed users only**）を決め、**Steward** のスイッチで組織にオンにし、**Organization settings > Usage** の **Services** の **PR Steward** の行で月の上限を決め、リポジトリの **Edit** で **Manual (@claude steward)** と **Steward spend cap**（米ドル）を設定して、`@claude steward` で試す、の 6 つの手順。リポジトリを加えると課金される Code Review が始まりうる、という警告がある
- **Roll out PR Steward to more pull requests**: 修正がレビュアーのものと合うようになったら **On** にする。始まり方の 4 つの選択肢の表と、**Excluded users** で作者を外す方法。PR Steward をオンにできるのは 256 リポジトリまで
- **Control what PR Steward spends**: マージしたプルリクエストあたりの平均は **Edit** のダイアログで、組織の 30 日の合計は `claude.ai/analytics/pr-steward` で見る。月の上限か組織の usage credits の上限に届くと一時停止し、上限（spend cap）に届くとそのプルリクエストで止まる（止まる前に上限を超えることがある）
- **Set up PR Steward's build environment**: 組織で共有する環境を **Where it runs** の **Default environment** に選ぶか、リポジトリごとに **Environment** で替える。セルフホストの環境も選べるが、承認とマージへの制限は Anthropic がホストするセッションについてのもので、セッションが読める GitHub の資格情報での承認は Anthropic のサービスが拒めない。資格情報は Claude Tag のバンドルで渡し、`denied by policy: this host's bundle of logins and rules isn't turned on for PR Steward` の 403 が出たら、そのバンドルの **PR Steward** のスイッチをオンにする
- **Turn off PR Steward**: オフにしても、`claude-pr-steward-watching` のラベルが付いたプルリクエストではしばらく働き続ける（作者 1 人をオフにしたときは約 1 週間）ので、先にラベルを外す

- [PR Steward をセットアップする - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/pr-steward-setup#turn-on-pr-steward-and-add-repositories)
- [Set up PR Steward - Claude Code Docs (English)](https://code.claude.com/docs/en/pr-steward-setup#turn-on-pr-steward-and-add-repositories)

## 5. Work with PR Steward on a pull request

**`pr-steward-pull-requests`（246 行）は、プルリクエストを開く開発者向けのページです。** github.com では PR Steward は `claude[bot]` としてコメントし、見守る間の `claude-pr-steward-watching` と働く間の `claude-pr-steward-is-working` の 2 つのラベル、最初の **Claude PR Steward** のコメント、仕事の前後の進捗のコメント、`Claude <noreply@anthropic.com>` のコミットを加えます。落ちたテストを直す例で、それぞれのコメントの文面も示します。

- **Default instructions for PR Steward**: 指示がなければ、プルリクエストが触れたコードの失敗は直してプッシュする、不安定なチェックは条件を満たせば 1 回だけ再実行する、競合があればベースのブランチを取り込む、ロックファイルと生成されたファイルは生成し直す、小さなレビューの依頼は変更をプッシュしてスレッドを解決する、大きな依頼や設計の依頼には返事だけをする、Code Review の任意の指摘には返事をして解決する、やり方は自分で選ぶ
- **指示の与え方**: 1 つのプルリクエストでは `@claude` で始まるコメント、自分が開くすべてのプルリクエストでは claude.ai の **PR Steward** の設定（**Off**・**Only when tagged**・**Act on its own**・**Customize** と、**Customize** のトグル、**Updating my branch from the base branch**、1,000 文字までの **My instructions for Steward**）、リポジトリのすべての人には既定のブランチの `.claude/skills/steward/SKILL.md`（例あり）。PR Steward はルートの `CLAUDE.md`・`.claude/CLAUDE.md`・`.claude/rules/`・`AGENTS.md` も既定のブランチから読む
- **Which PR Steward instructions take priority**: 始まるかどうかは、選んだ選択肢と **Include my draft PRs** で、指示を読む前に決まる。始まった後は、自分の設定とリポジトリのファイルが食い違えばファイルが勝ち、プルリクエストのコメントは自分の設定より勝ち、止める・待つように頼むコメントはファイルにも勝つ
- **Start or stop PR Steward**: `@claude stop`・`@claude steward stop`・`@claude unwatch` で止め、`@claude steward` で始める（`@claude babysit`・`@claude watch` などの綴りもある）。止めた後はプッシュやコメントでは戻らない。押された修正を戻すには、先に止めてから `Claude <noreply@anthropic.com>` のコミットを revert する。初めから入れないなら説明に `<!-- claude-pr-steward-disable -->` を入れる。コメントとラベルで始めるには書き込みの権限が要り、ラベルを外して止めるのは GitHub がラベルを外すのを許す人なら誰でもできる

- [プルリクエストで PR Steward を使用する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/pr-steward-pull-requests#default-instructions-for-pr-steward)
- [Work with PR Steward on a pull request - Claude Code Docs (English)](https://code.claude.com/docs/en/pr-steward-pull-requests#default-instructions-for-pr-steward)

## 6. What PR Steward can access

**`pr-steward-security`（68 行）は、Anthropic がホストする環境での PR Steward のアクセスと制限のページです。** GitHub Enterprise Server では、組織が作ったアプリとして動きます。

- **PR Steward's GitHub access**: セッションはプルリクエスト自身のリポジトリを読み書きし、github.com の GitHub の検索は PR Steward に加えた組織のほかのリポジトリの結果も返しうる。権限は contents・pull requests・issues の読み書きと、インストールが与えれば checks と statuses の読み取りと Actions の書き込み（github.com では workflows の書き込みも）。アプリのトークンはセッションのサンドボックスの外に置かれ、`gh` と `git` の要求は既定で Anthropic のサービスを通り、そこでトークンが付く
- **PR Steward's session environment**: セッションは auto モードで始まり、許可の要求は拒まれる。Anthropic のサービスがセッションに渡すのは、作者・書き込みの権限のある人・ボットのコメントとレビューで、セッションがプルリクエストを直接読めばほかの人の書いたものも見える
- **Requests that Anthropic's service refuses**: プルリクエストの承認、ブランチの保護・ルールセット・ステータスの変更とチェックランの書き込み、ブランチの削除、タグのプッシュ
- **Requests left to GitHub's branch rules**: マージ・auto-merge のオン・force-push（パーミッションのルールが通常のコマンドを拒み、ルールに合わないものは auto モードの確認が判断するが、別の書き方のコマンドはどちらも通りうる）、プルリクエストのもの以外のブランチへのプッシュ、レビューの却下

- [PR Steward がアクセスできる範囲 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/pr-steward-security#limits-on-approvals-and-merges)
- [What PR Steward can access - Claude Code Docs (English)](https://code.claude.com/docs/en/pr-steward-security#limits-on-approvals-and-merges)

## 7. Troubleshoot PR Steward

**`pr-steward-troubleshooting`（102 行）は、PR Steward が思ったとおりに動かないときのページです。** まずプルリクエストに PR Steward のコメントがあるかを見て、あればその文言を表で探し、なければ始まらなかった原因を確かめます。

- **PR Steward didn't start on a pull request**: `@claude steward` に 👀 のリアクションがなければ、編集ではない新しいコメントか、書き込みの権限があるかを確かめる。飛ばすプルリクエスト（ドラフト・フォーク・ボット・`<!-- claude-pr-steward-disable -->`、auto-fix のクラウドセッションのようにほかの Claude のセッションがすでに見守っているもの）、始まりを止める設定（**Manual** や自分の **Off**・**Only when tagged**、リポジトリや作者がオフ）、短い間に多くのプルリクエストが開かれた場合
- **PR Steward posted a comment that says why**: 始まれないときのコメント（書き込みの権限がない、usage credits がない、PR Steward の課金が用意されていない、始まれなかった、セットアップのスクリプト、複数の Claude のワークスペースでオン）と、止まった・一時停止したときのコメント（usage credits が切れた、上限に届いた、組織の設定が外れた、`<N>` 日のあいだ人がコメントもレビューもしていない）の表
- **Auto-fix is unavailable**: PR Steward が働くリポジトリでは、claude.ai/code で `PR Steward is already watching this PR.` が出る。auto-fix を使うには、自分の PR Steward の選択肢を **Off** にし、すでに見守られているプルリクエストでは止める
- **Messages while you set up PR Steward**: **Claude Ship** のページに出る 6 つのメッセージと対処

- [PR Steward のトラブルシューティング - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/pr-steward-troubleshooting#auto-fix-is-unavailable)
- [Troubleshoot PR Steward - Claude Code Docs (English)](https://code.claude.com/docs/en/pr-steward-troubleshooting#auto-fix-is-unavailable)

## 8. Claude Approvals

**`approvals`（109 行）は、Claude Approvals の概要のページです。** Approvals はポリシーを読み、当てはまるルールを見つけ、承認を数えて、チェックとコメント（ポリシーが許せば承認のレビューも）をプルリクエストに残します。チェックの題は **Waiting on human review from any person (1/2)** のように残りを示し、**(observe mode)** で始まる題は、チェックが走ったときポリシーが強制されていなかったことを示します。

「Example policy」は、すべての変更に 2 人を求め Claude は承認しない 1 つのルール（`mode: observe`・`purpose`・`paths: ["**"]`・`verdict: { claude: comments, seats: 2 }`・`advisory: [claude/code_review]`）を示し、各行の意味を述べます。「Before you turn on Approvals」には、使える組織、オンとオフにできる人、人が見ないマージ、自動の Code Review を残す方法（`advisory` に `claude/code_review` を挙げる）、課金（ポリシーが始めた Code Review と分類器の実行がトークンで課金される）の h3 があります。Claude Code のセッションの許可のプロンプトは別の話で `permissions` を見る、という注記もあります。

- [Claude Approvals - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/approvals#keep-automatic-code-reviews)
- [Claude Approvals - Claude Code Docs (English)](https://code.claude.com/docs/en/approvals#keep-automatic-code-reviews)

## 9. Set up Claude Approvals

**`approvals-setup`（197 行）は、リポジトリで Approvals をオンにして強制するまでの手順のページです。** ルートの既定のブランチに `.claude/approvals.yml` を置くとオンになり、課金も始まりえます。前提は、条件を満たす組織と usage credits、リポジトリに入れて組織にリンクした Claude GitHub App、既定のブランチへマージする権限、必須のチェックを設定するリポジトリの Admin の権限、書き込みの権限のある 2 人（1 人だけだと `.claude/` の下の変更などでチェックが通れない）です。

- **Plan your first policy**: 初めのポリシーが 2 つある。「Let Claude approve when Code Review passes」は、2 人を求め、`claude/code_review = pass` の `override` で 1 人に減らして Claude に承認させ、`**/.claude/**` の変更には 2 人を求める（プッシュのたびに課金される Code Review を始めうる）。「Keep two people on each change」は、どちらのルールも 2 人で、`advisory` に `claude/code_review` を挙げるのでレビューは Code Review の設定に従う
- **Turn on Approvals in observe mode**: ポリシーファイルだけのプルリクエストを出し、Claude が「found the policy file in this change valid」とコメントしたらマージし、別のプルリクエストで **(observe mode)** のチェックを見る
- **Enforce your policy and require Claude Approvals**: 守るファイルとブランチを決め、`mode: observe` の行を消してマージし、5 分後に開いているプルリクエストで `@claude approvals rerun` とコメントし、GitHub の必須のチェックに **Claude Approvals** を加え（ソースは報告した Claude のアプリ。API ならアプリの ID `1236702`）、`.claude/` の下を変えるプルリクエストでマージが止まるのを確かめる
- **Control what Approvals spends**: `if` の条件の `claude/code_review` は、プルリクエストを開くたび・プッシュのたびに課金される Code Review を始めうるので、止めたければ `advisory` に移す。上限は、組織の usage credits の上限、Code Review の上限（ポリシーのレビューを含む）、分類器の実行の上限の 3 つ
- **Turn off Approvals**: GitHub で古い承認を外す設定を確かめ、必須のチェックを外し、Approvals をオフにし、Claude の承認のレビューを却下する、の順。Claude GitHub App の停止やアンインストールは Approvals をオフにした後で行う。オフにする範囲は、1 つのリポジトリ（ポリシーファイルを消す）、GitHub の組織（**Edit** で **Claude Approvals** をオフ）、Claude の組織全体（**Approve** の行の **Block globally**）

- [Claude Approvals をセットアップする - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/approvals-setup#switch-from-observe-mode-to-enforcement)
- [Set up Claude Approvals - Claude Code Docs (English)](https://code.claude.com/docs/en/approvals-setup#switch-from-observe-mode-to-enforcement)

## 10. Work with Claude Approvals on a pull request

**`approvals-pull-requests`（133 行）は、プルリクエストの作者とレビュアー向けのページです。** Approvals は、プッシュや承認のような出来事の後にプルリクエストを評価し、「Claude Approvals」のチェックの題と Claude のコメント（結果が変わると同じコメントを書き換える）で結果を示します。

- **Find your approval status and what to do next**: 題ごとの表が 4 つある。人を待つ（**Waiting on human review from any person (1/2)**・**Changes requested**・**Claude's approval still stands; dismiss it**）、Code Review か分類器を待つ（**Waiting for Code Review** など、**A classifier had no result** など）、ルールかポリシーファイルが止める（**Held by Code Review's findings**・**Held by**・**No rule applies to**・**This change breaks a policy file** など）、通ったか何も走らなかった（**Passed; no approval from Claude**・**Nothing ran, not blocking: no file is covered**・**Observe mode ended: not evaluated yet**）
- **Approvals in observe mode**: チェックは neutral（GitHub は通ったとみなす）で終わるが、ポリシーか分類器のファイルを変えるプルリクエスト、既定のブランチのポリシーファイルが使えないとき、**Withheld** の題、既定でないブランチへのプルリクエストでは違う
- **Comment commands for Approvals**: `@claude approvals rerun`（最新のコミットを評価し直す。分類器は課金されて走り直しうる）、`@claude approve`（Claude Approvals のチェックにとって自分の承認になりうる）、`@claude approvals resolve <ids>`（`findings` の一覧に自分がいれば、指摘を閉じる）。書き込みの権限が要り、😕 のリアクションは全部は実行されなかったことを示す
- **Pull requests from Claude, forks, and outside contributors**: `claude[bot]` が開いたプルリクエストを Claude が承認するには、Claude Approvals GitHub App という 2 つ目のアプリを入れて組織にリンクする。フォークのプルリクエストでは、書き込みの権限のある人が変更を読んで `@claude approvals rerun` と最新のコミットの完全な SHA でコミットを保証するまで、分類器の答えは数えられない

- [プルリクエストで Claude Approvals を扱う - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/approvals-pull-requests#find-your-approval-status-and-what-to-do-next)
- [Work with Claude Approvals on a pull request - Claude Code Docs (English)](https://code.claude.com/docs/en/approvals-pull-requests#find-your-approval-status-and-what-to-do-next)

## 11. Claude Approvals and your GitHub rules

**`approvals-github-rules`（105 行）は、ポリシーと GitHub の設定がどう組み合わさるかのページです。** ポリシーを強制する前に、リポジトリの管理者やセキュリティのレビュアーが確かめることを 4 つの h2 にまとめています。

- **Merges without human review**: GitHub がチェックを求めていないとき、またはチェックが作者のほかに誰もいないまま通るとき（`seats: 0`、作者が埋める `seats: 1`、ボットを許す `from`、人として数えられるマシンユーザー、プッシュの後も席を残す `reuse`、どのルールも覆わないファイル、分類器の答えを読む条件）に、作者しか見ないマージが起きうる。既定のブランチへの直接のプッシュにはチェックが付かない。h3「Ask for a person who isn't an author」は、すべてのパスで作者でない 1 人を求めるルール（`seats: [{ count: 1, from: [humans, "!pr/authors"] }]`・`nested: inherit`・`claude: comments`）と各部分の意味を示す
- **Required reviews and CODEOWNERS**: GitHub は Claude の承認のレビューを 1 つの承認として数えうるが、席を埋めた作者や `@claude approve` のコメントは数えない。チェックを求めるなら GitHub の必須の承認は 1 以下にし、人数は `seats` で求める。古い承認を外す設定をオンにする
- **Auto-merge and merge queues**: Approvals はマージキューが作るコミットを評価せず、ふつう **Stamped for merge queue** の題で通ったとする。Claude GitHub App の **Merge queues** の権限が要る
- **Who can change or loosen a policy**: 既定のブランチへマージできる人はポリシーファイルを変えられ、リポジトリの admin は必須のチェックを外せ、Claude の組織の Owner は Approvals をオフにできる。プルリクエストの作者の文は分類器の答えを動かしうる

- [Claude Approvals と GitHub のルール - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/approvals-github-rules#merges-without-human-review)
- [Claude Approvals and your GitHub rules - Claude Code Docs (English)](https://code.claude.com/docs/en/approvals-github-rules#merges-without-human-review)

## 12. Claude Approvals policy file reference

**`approvals-policy`（407 行）は、`.claude/approvals.yml` のリファレンスで、新規 16 ページでいちばん大きいページです。** 初めのポリシーを例に各行の意味を述べた後、置き場所（ルートの `.claude/approvals.yml`。なければ `.claude/approvals.yaml`。サブディレクトリにも置ける）、変更が効くとき（既定のブランチにマージされてから。開いたプルリクエストでは誤りだけを確かめる）、キーの一覧が続きます。

- **Top-level keys**: `version`（必須・`1`）・`rules`（必須）・`mode`（`enforce` が既定、`observe`）・`nested`（`overwrite` が既定、`inherit`）・`run`（`sequential` が既定、`parallel`）・`locals`。知らないキーがあるとファイルは拒まれる
- **Rule keys**: `purpose`・`paths`（`**` や `"!docs/**"` のパターン）・`verdict`（`claude` と `seats`（`0`〜`16` か 8 つまでの組）と `max_age`）・`if`（`=`・`!=`・`<` などと `AND`・`OR`、`ANY`・`ALL`。事実は `pr/files_changed`・`pr/diff_lines`・`rule/files_changed`・`pr/authors`・`pr/opened_by`・`pr/approved_by`・`pr/base` など）・`override`・`advisory`・`reuse`・`findings`・`use`・`mode`・`nested`・`run`。人の一覧は `humans`・`bots`・`everyone`・`nobody`・ログイン・チーム・`bot:<name>`・`"!pr/authors"`
- **How rules combine into one verdict**: 当てはまる判定のうちいちばん厳しいものを取る（`blocks` > `comments` > `approves`、各ルールの席はすべて埋める）。ルールがファイルに「合う」「当てはまる」「覆う」の区別と、どのルールも覆わないファイル・どれも当てはまらないファイルの扱い
- **How people's approvals are counted**: 書き込みの権限のある作者は、承認しなくても自分を許す組の 1 席を埋められる（フォークのものを除き、`seats: 1` は作者だけで満たせる）。作者を外すには `"!pr/authors"` を使う。差分の文字列が変わるプッシュの後は、`reuse` がない限り前の承認はふつう数えられなくなる
- **Protected files**: ポリシーと分類器のファイル、ルートの `REVIEW.md`、`.gitmodules`・`.gitattributes`・シンボリックリンク・サブモジュールのポインター、`CODEOWNERS` を変える変更には、ふつう人が要る（作者でもよい）。`.github/`・`CLAUDE.md`・`AGENTS.md`・`.mcp.json` などは守られないので、自分でルールを書く
- **Policy file size and count limits**: 1 ファイル 448 KiB、リポジトリで 1,024 ファイル・合計 8 MiB、1 ファイルのルール 512 などの上限の表。プルリクエストにも、変わったファイルが 2,000 以上（**Change too large to evaluate**）、`"!pr/authors"` の組があるときのコミットが 250 より多い（**Too many commits to tell who wrote it**）、の上限がある

- [Claude Approvals ポリシーファイルリファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/approvals-policy#how-rules-combine-into-one-verdict)
- [Claude Approvals policy file reference - Claude Code Docs (English)](https://code.claude.com/docs/en/approvals-policy#how-rules-combine-into-one-verdict)

## 13. Claude Approvals classifiers

**`approvals-classifiers`（290 行）は、ルールが変更についての判断（Code Review が通ったか、どれだけ危ういか）に頼れるようにする分類器のページです。** 分類器には名前・問い・答えがあり、ルールの条件で名前を書くと、Approvals がプルリクエストで実行し、その答えが誰が承認するかの判断に使われます。

- **Example classifier definition**: `.claude/classifiers/change_risk/def.yml` に `version`・`description`・`model: opus`・`prompt`・`outputs`（`risk` を `low`・`medium`・`high` の `ordinal` で）を書く例。ルールでは `repo/change_risk` と書き、`if: "repo/change_risk = low"` のように比べる
- **Classifiers Anthropic provides**: `claude/code_review` は `pass`（Important の指摘が開いていない）か `fail`。`.severity` は `none`・`minimal`・`high`。`claude/diff` は `trivial`・`same_intent`・`different` で、`reuse` の条件で読む
- **Add a custom classifier**: フォルダーと `def.yml` を作り、まずルールの `advisory` に挙げて（答えは数えず、実行は課金される）、答えを Claude のコメントの **Classifier results** で確かめてから、`override` の `if` に移す
- **Classifier definition file keys**: `version`・`description`・`model`（`opus` や `sonnet` の系列名か、一般提供のモデルの正確な ID。auto モードに対応している必要がある）・`prompt` か `prompt.md`・`outputs`（`criteria`・`ordinal`・`numeric`）・`inputs`（`merge` で、ルールが違う値を求めたときの扱いを決める）・`tools`（`findings`・`comment`・`code`・`labels`・`reviewers`）・`budget`（`time` は既定 600 秒・最大 3600 秒、`cost` は既定・最大とも 10 ドル）
- **How a classifier run behaves**: 既定のブランチの定義が走り、プルリクエスト自身の定義は走らない。実行は Anthropic の基盤の Claude Code のクラウドセッションで、GitHub へのアクセスは読み取りだけ。答えがなければ条件は `incomplete` か `error` を読む
- **What a classifier run costs**: 自分の分類器は observe モードや `advisory` の下の実行、答えのない実行も含めて実行ごとに課金され、エラーの後に Approvals が自動で何度か走らせ直すと、そのたびに課金される

- [Claude Approvals の分類器 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/approvals-classifiers#add-a-custom-classifier)
- [Claude Approvals classifiers - Claude Code Docs (English)](https://code.claude.com/docs/en/approvals-classifiers#add-a-custom-classifier)

## 14. Troubleshoot Claude Approvals

**`approvals-troubleshooting`（101 行）は、Approvals の問題の対処のページです。**

- **No Claude Approvals check appeared**: 自分で確かめる原因（ドラフト、ポリシーファイルの場所、マージ後に何も起きていない、observe モードで既定でないブランチ、どのルールもファイルを覆わない）、Claude がコメントだけを残したとき（「did not run on this change」・複数の Claude の組織がつながっている・「Claude Approvals can't start in this repository yet」）、Owner に確かめてもらうこと
- **Approvals doesn't pass after you resolve a review thread** と **Approvals passed and GitHub still blocks merging**: `findings` の一覧に自分がいるか確かめる。GitHub のブランチのルールがポリシーにないレビューを求めているなら、作者でない人に GitHub のレビューで承認してもらう
- **Fix a policy file that Approvals refuses**: 題ごとの、誤りのある写し（プルリクエストのものか既定のブランチのものか）と直し方の表と、拒まれたときのメッセージ（「no key of this name is read at this place」「this names no fact and no usable classifier」「a condition has no NOT」「no local has this name」「this is not YAML」）の表
- **A classifier gave no answer or its definition is refused**: Claude のコメントの **Classifier results** で状態を見て、題ごとに対処する（**Cannot evaluate: classifier outside advisory** なら `advisory` に移す、実行の上限に届いたなら差分を変えるプッシュか `@claude approvals rerun`）

- [Claude Approvals のトラブルシューティング - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/approvals-troubleshooting#fix-a-policy-file-that-approvals-refuses)
- [Troubleshoot Claude Approvals - Claude Code Docs (English)](https://code.claude.com/docs/en/approvals-troubleshooting#fix-a-policy-file-that-approvals-refuses)

## 15. Get a pull request ready with /ship and /steward

**`ship-command`（264 行）は、`/ship` と `/steward` の使い方のページです。** `/ship` の後は、プルリクエスト → `/code-review` のレビュー → watch → 自分でマージ、の順に進み、`/steward` は最初の 2 つを飛ばします。内容はハイライト 4 のとおりで、ほかに次のことを述べます。

- **When to use /ship and /steward**: どちらも自分のセッションで動き、自分の使用量に数えられる。レビューだけなら `/code-review`、クラウドセッションからの修正なら auto-fix か `/autofix-pr`、組織に課金されるリポジトリ全体のエージェントなら Claude Ship を使う
- **What /ship commits and pushes**: フォークでない github.com のリポジトリでは、コミットしていない変更をコミットし、既定のブランチにいれば新しいブランチを作って切り替える。確認のプロンプトはなく、コミットとプッシュの前に `Esc to cancel` で終わる行が出て、何もしなければ数秒で進む。プルリクエストが開いている、公開のリポジトリ、`.env` のように秘密を思わせる名前のファイル、のときはコミットしない
- **What Claude does during a watch**: auto モードでは、問題とみたレビューの指摘への対応、レビューをまとめた 1 つのコメント、ブランチへのプッシュ、ベースのブランチの取り込み、落ちたチェックへの対応と再実行、レビューのコメントへの返事・スレッドの解決・レビューの再依頼を尋ねずに行う。読むのは自分と書き込みの権限のある人のコメント（github.com では Claude のボットも）で、ほかのボットは `/steward +my-lint-bot` のように加える。リポジトリの `.claude/skills/steward/SKILL.md` は PR Steward と同じファイルで、watch では手元のクローンの写しに従う
- **Check, stop, or restart a watch**: `/tasks` で `/steward --tend` で始まる名前のスケジュールされたタスクとして見える。マージかクローズ、PR Steward のラベル、7 日の経過、`Esc` か `Ctrl+C`、ブランチの切り替え、git の設定の変更、セッションの終了やバックグラウンドへの移動、`/clear`・`/resume`・`/branch` などで終わる。止めるのは `/ship stop`、始め直すのは `/steward`
- **Decide where to run a watch**: watch の間に自分のコンピューターで動きうるコード（ベースのブランチ、ほかの人のプッシュ、自分のブランチのテストなどのプログラム、Claude Code のフック、`.claude/skills/steward/SKILL.md`）、マージにつながりうる場合（auto-merge がオン、Claude が待っているときにメッセージを打った、セッションをバックグラウンドに送った）、パーミッションのルールとフックの効き方の表（watch の間、Claude の fetch・merge・commit・push は `git -c core.hooksPath=/dev/null push` の形で書かれ、`Bash(git push *)` の ask のルールには合わない）
- **Arguments for /ship and /steward**: `low`〜`max` のレビューの effort（既定は `high`。`/ship` だけ）、プルリクエストの番号か URL、`+botname`、`stop`、`terms`（watch の間にしてよいことと制限を示す）

- [/ship と /steward でプルリクエストをマージ可能な状態にする - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/ship-command#what-claude-does-during-a-watch)
- [Get a pull request ready with /ship and /steward - Claude Code Docs (English)](https://code.claude.com/docs/en/ship-command#what-claude-does-during-a-watch)

## 16. Troubleshoot /ship and /steward

**`ship-command-troubleshooting`（213 行）は、`/ship` と `/steward` のメッセージや症状を引くページです。** 冒頭に、起きたことから節を探す表があります。

- **/ship or /steward is missing or doesn't start**: `/ship` が `/` のメニューにない・`/code-review` が始まる・`Unknown command: /ship` なら、`claude update` して起動し直し（新しい機能は 2 回目の起動で出ることがある）、自分の設定の `disableBundledSkills` と `skillOverrides` の `ship-local` を外し、フィーチャーフラグの取得を飛ばすセッション（`DISABLE_TELEMETRY` やサードパーティのプロバイダー）でないか確かめる。始まらずに出るメッセージ（`Nothing started. /ship starts only from a line that you type` など）と、GitHub CLI の準備のメッセージの表
- **/ship committed or pushed nothing**: 公開のリポジトリ、秘密を思わせる名前のファイル、サンドボックスが残す空のファイル（`.bashrc` など）、git・CI・コーディングエージェントを設定するファイル（`.gitignore`・`CLAUDE.md`・`.github/` の下）、コミットやプッシュのできないブランチ、deny のルール、GitHub Enterprise とフォーク（`/ship` はプルリクエストを開かない）
- **No watch started**: プルリクエストかブランチの準備（ブランチのチェックアウト、PR Steward のラベル）、セッションの設定（`bypassPermissions`、Remote Control、`PATH` の相対か空の項目、チェックアウトの中のフォルダーを含む `PATH`）、ツール・ルール・フック、watch がまったく始まれない場合（native Windows、ほかの人が開いたプルリクエストなど）
- **A watch stopped**: `Stopped watching pull request` の行の「because」の後の理由ごとの表と、watch が頼るファイル（git の設定、`.claude/settings.local.json`）が変わったとき
- **Messages during a watch**・**Pull request results that you didn't expect**・**A custom /ship or /steward command stopped loading**: `Claude Code did not run this`（Claude のメッセージでは watch の制限を「the fence」と呼ぶ）、`In this session there's a way around my limits` などのメッセージと、`ship`・`ship-local`・`steward` の名前の自分のスキルかコマンドは読み込まれないので名前を変える、という対処（リポジトリの `.claude/skills/steward/SKILL.md` はそのままにする）

- [/ship と /steward のトラブルシューティング - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/ship-command-troubleshooting#no-watch-started)
- [Troubleshoot /ship and /steward - Claude Code Docs (English)](https://code.claude.com/docs/en/ship-command-troubleshooting#no-watch-started)

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
（今回の対象期間に、既存のページで 50 行以上変わったページはありません。いちばん多いのは `code-review-setup` の 37 行（追加 24・削除 13）で、内容はハイライト 1 にまとめました）
<!-- light:updated-pages:end -->

**行数の数え方**: 今回は、生の差分のハンクをページに振り分ける、これまでの数え方が使えません。`llms-full.txt` のページの並びが替わり（両方にあるページ 205 のうち 29 ページの位置が替わった。`plugin-evals` から `plugins/security` までの `plugins/` 系の 17 ページと、`channels-reference`・`checkpointing`・`cli-reference`・`commands`・`env-vars`・`glossary`・`hooks`・`interactive-mode`・`keybindings`・`statusline`・`tools-reference`・`voice-dictation` の 12 ページ）、2 回載るページも替わった（下の軽微な更新の導入を参照）ので、生の差分（追加 69,617・削除 64,134）のほとんどは、ページの移動と 2 回載るページの入れ替わりによるものです。そこで、base と head の `llms-full.txt` をそれぞれ `Source:` の行でページに切り分け、同じページの 1 つ目の写しどうしを行単位で比べ（difflib、autojunk なし）、その追加と削除の行数を数えました。この数え方で、新規 16 ページと changelog を除く既存のページの変化は、合計で追加 222 行・削除 200 行です。`code-review-setup` に次いで多いのは `claude-code-on-the-web` の 26 行（追加 4・削除 22）、`claude-apps-gateway-deploy` の 16 行で、ほかのページはどれも 15 行以下です。changelog は 151 行が加わりました（v2.1.331 の 1 リリース）。

## 軽微な更新

<!-- light:minor-updates:start -->
今回の差分は **3 ファイル**（`llms.txt`・`llms-full.txt`・見出しマップ）です。`llms.txt` は、新規 16 ページの行（URL は 205 から 221）、「Code review and pull requests」の小見出しの組み替え（ハイライト 1）、8 ページの説明文の「Complete reference for …」から「Reference for …」への書き換え、末尾の「Indexes」の 11 言語の索引のページ数の 205 から 221 への変化で、49 行が加わり 21 行が外れました（413 行から 441 行）。`llms-full.txt` では、新規の 16 ページのほかに、既存の **82 ページ**（changelog を含む）の内容が変わりました。大幅更新はないので、changelog を除く **81 ページ**と、changelog に加わった **v2.1.331（2026年11月23日、135 項目。Added 14・Changed 8・Improvements 18・Bug fixes 95）** を以下にまとめます。単一のリリースなので、changelog の各項目への版の併記は省いています。changelog の収録リリースは 446 から 447 になり、先頭は v2.1.331 です。新着情報（whats-new）のページはありません。

`llms-full.txt` の総行数は **130,779 行から 136,262 行へ 5,483 行増え**ました（生の差分の差し引き 69,617 − 64,134 と一致）。内訳は、新規 16 ページが 2,733 行、新しく 2 回載るようになった 4 ページ（`cloud-environments`・`model-config`・`permissions`・`terminal-config`）の 2 つ目の写しが 3,226 行、2 回載らなくなった 2 ページ（`plugins/create`・`plugins/mods/overview`）の 2 つ目の写しが −649 行、changelog が 151 行、そのほかの既存のページの差し引きが 22 行です。2 回載るページは、`plugins/install` が引き続き 2 回で、両方が同じように変わりました。新しく 2 回載る 4 ページも、2 つの写しは同じ内容です。`Source:` の行は 208 から 226 になりました（固有のページは 221）。ほかに、`voice-dictation` の末尾に 2 行の空行が加わり、`legal-and-compliance` の末尾から 2 行の空行が外れていますが、ページの並びが替わった境目の空行で、内容の変更ではありません（上の 81 ページにも数えていません）。

コードフェンスの外の見出しは、同じページの 2 つ目の写しを除いて数えると、行頭が `#` の見出しは 6,129 から 6,370 へ、引用の中の見出しも数えると 6,140 から 6,381 へ、どちらも 241 増えました。新規 16 ページの 242 と、既存のページの 3 つの変化（`code-review-troubleshooting` の h3「Code review not run: no policy rule uses it」が加わり、`claude-code-on-the-web` の h4「Share from an Enterprise or Team account」「Share from a Max, Ultra, or Pro account」が外れた）の差し引きです。`claude-projects` の h3「Claude hasn't responded」は「Claude's replies aren't getting through」に改称され、HTML の id は旧見出しの `#claude-hasnt-responded` のままです。2 つ目の写しも数えると、6,198 から 6,572 へ、6,209 から 6,590 へ増えています。

**新機能**

- Claude Ship と、Code Review の設定の置き場所の変化・Approvals との関係（`code-review`・`code-review-setup`・`code-review-pull-requests`・`code-review-troubleshooting`・`code-review-costs`・`github-enterprise-server`・`feature-availability`。詳細はハイライト 1 参照）
- PR Steward と auto-fix・クラウドの環境・セルフホストの環境の関係（`claude-code-on-the-web`・`cloud-environments`・`self-hosted-environments-configuration`。詳細はハイライト 2 参照）
- `/ship` と `/steward`（`commands`・`skills`・`env-vars`・`champion-kit`・`communications-kit`。詳細はハイライト 4 参照）
- セッションの共有のページ（`claude-code-on-the-web`・`remote-control`。詳細はハイライト 5 参照）
- **mod の組み込みのガードのメッセージが 2 行増えた**（`plugins/mods/troubleshoot` の「Messages from the built-in guard」）。`tried to lift a deny rule in your settings` の行が、`tried to lift` か `tried to reword` の行になり、`tool.check` のような mod のフックが、メッセージが名指す判定を緩めるか書き換えようとした（判定はそのまま。`await next(e)` が返すものか、より厳しい判定を返す）、という説明になりました。ガードが拒む環境変数を mod が変えようとしたときの `is not for plugins outside policy to change`（`$.env.set` の呼び出しを外す）と、プラグインの名前が組織の MCP サーバーかプラグインの名前と同じときなどの `would be named as a tool of one of the organization's servers`（プラグインの名前を変える。消えなければ `managed-mcp.json` が読めて正しいかを管理者に尋ねる。`$.tool.register` が投げる）の 2 行が加わっています。冒頭の文も、ガードが mod か「その答え」を拒む、から「その答えか呼び出し」を拒む、になりました — [日本語](https://code.claude.com/docs/ja/plugins/mods/troubleshoot#messages-from-the-built-in-guard) / [English](https://code.claude.com/docs/en/plugins/mods/troubleshoot#messages-from-the-built-in-guard)
- **`classic.PreToolUse` の `e` の中身が書かれた**（`plugins/mods/events` の「Handle the settings hook events」・`plugins/mods/reference`）。設定のフックのイベントを扱うには名前に `classic.` を付ける、と短くなり、`classic.PreToolUse` では `e` はツールの呼び出しだけを表し、ツールの名前が `e.tool` に、組み込みのツールの引数がフィールド（Bash なら `e.command` など）に入り、ほかのイベントでは設定のフックが標準入力から読むフィールドを持つ、という段落が加わりました。これまでの、`e` は設定のフックが標準入力で受け取る JSON（`transcript_path` を含む）、という説明は外れています。`plugins/mods/reference` の同じ説明も、`e` のフィールドは「Handle the settings hook events」を見る、になりました — [日本語](https://code.claude.com/docs/ja/plugins/mods/events#hook-the-settings-hook-events) / [English](https://code.claude.com/docs/en/plugins/mods/events#hook-the-settings-hook-events)
- **ultracode のキーワードをバッククォートで囲む例が加わった**（`workflows` の「Dismiss or turn off the keyword」）。`` find every file that mentions `ultracode` `` という、ファイルを探すふつうの依頼になるプロンプトの例が加わりました。同じページの「What a workflow script looks like」の前置きからは、ふつうは編集しなくてよい、という部分が外れています — [日本語](https://code.claude.com/docs/ja/workflows#dismiss-or-turn-off-the-keyword) / [English](https://code.claude.com/docs/en/workflows#dismiss-or-turn-off-the-keyword)
- Amazon Bedrock・Google Cloud の Agent Platform・Microsoft Foundry・Claude Platform on AWS のターミナルのセッションで、Code Mode に対応
- Claude apps gateway に `oidc.groups_jsonpath` を追加。JSONPath（RFC 9535）の小さな部分集合で、オブジェクトの一覧の合う項目からグループを読みます
- `claude doctor` に API の接続性の節を追加。API に届くか（HTTP のステータスかエラー付き）、または試さなかった理由を報告します
- タップのモードの音声入力が、認識できる発話のないまま 15 秒たったとき、または 2 分の上限で自分で止まったときの通知を追加
- 圧縮した応答を途中で切るプロキシの裏で、圧縮しないモデルの応答を求める `CLAUDE_CODE_DISABLE_RESPONSE_COMPRESSION` を追加。セルフホストのランナーと Remote Control にはまだ勧めません
- Claude apps gateway に `CLAUDE_GATEWAY_IDP_CONNECT_BY_HOSTNAME=1` を追加。`oidc.use_proxy: true` のとき、`NO_PROXY` が設定されていても、サインインの要求が `https` の IdP のホスト名をプロキシに渡します
- `claude_code.llm_request` のトレースのスパンに `gen_ai.usage.*`・`gen_ai.response.model`・`gen_ai.operation.name` を追加。`gen_ai.usage.input_tokens` はプロンプトキャッシュのトークンを含みます
- プラグインのマニフェストに `optionalDependencies` を追加。それを挙げるプラグインと一緒にインストールされ、個別に無効化やアンインストールができるプラグインです
- [VSCode] ログアウトのときに claude.ai のログインを取り消す要求が確認されなかった場合の警告と、取り消しのページへのリンクを追加
- [VSCode] とても大きな選択範囲か添付したテキストファイルを送る前の通知と、「Prompt is too long」の下に、大きな部分と次にすることを名指す助言を追加
- [VSCode] ノートブックのセルのメニューに、出力かエラーごとセルを添付する「Add Cell to Chat」を追加
- [VSCode] エラーと警告のクイックフィックスと、テストのピークと Test Results のビューの失敗したテストに、問題をチャットの欄に入れる「Fix with Claude Code」を追加
- [VSCode] Source Control のビューの変更したファイルの右クリックのメニューに「Add to Chat」を追加
- [VSCode] マージの競合のあるファイルのエディターのタイトルと、Source Control の Merge Changes のグループに「Resolve Merge Conflicts」を追加

**機能改善**

- **クラウドセッションでプラグインを使う方法が、claude.ai のアカウントで加える形になった**（`plugins/install`・`plugins/loading`・`claude-projects`・`cloud-environments`・`desktop`・`plugins/troubleshooting`・`claude-code-on-the-web`・`self-hosted-environments-configuration`）。`plugins/install` の「Install a plugin」のクラウドセッションのタブの注記は、クラウドセッションにはプラグインのブラウザーがなく、ユーザーかローカルのスコープで入れたプラグインを読み込まない、から、クラウドセッションでプラグインを使うには `claude.ai/customize/plugins` で claude.ai のアカウントに加えて新しいセッションを始める（一覧のプラグインを選ぶ、マーケットプレイスを加える、プラグインをアップロードする、のいずれか。Team と Enterprise では Owner が使えるものを決める）、になりました（2 回載るページの 2 か所とも）。ユーザーかローカルのスコープで自分のコンピューターに入れたプラグインはクラウドセッションで使えない、という文は残っています。ほかのページも合わせて変わりました。
  - `plugins/loading` の「Plugins synced from claude.ai」: 同期したプラグインが読み込まれるのが、Cowork とターミナルのセッションに加えてクラウドセッションにもなり、セッションを始めたときか、プロジェクトで Claude がスレッドを始めたときにダウンロードされる、という項目が加わった
  - `claude-projects` の「Get skills, plugins, connectors, and tools into threads」: claude.ai のアカウントで有効にしたプラグインを読み込むのが、Claude が用意したスケジュールされたタスクを除くクラウドのスレッド、から、Claude が始めるクラウドのスレッド、になり、`claude.ai/customize/plugins` へのリンクが付いた
  - `self-hosted-environments-configuration` の「What differs from sessions on the Anthropic API」: これらのセッションがダウンロードしないものが、claude.ai のアカウントで有効にしたスキル、からスキルとプラグインになった
  - `cloud-environments` の「What carries over from your setup」の表の、ユーザーの設定だけで有効にしたプラグインの行と、`desktop` の「Install plugins」の注記（デスクトップアプリからユーザーのアカウント向けかローカルだけで入れたプラグイン、が、自分のコンピューターにユーザーかローカルのスコープで入れたプラグイン、になり、クラウドセッションにはプラグインのブラウザーがない、という部分が外れた）に、「Install a plugin」のクラウドセッションのタブへの案内が付いた
  - `plugins/troubleshooting` の「`/plugin isn't available in this environment`」: この返事が出る場所の例から、デスクトップアプリの Code タブと claude.ai/code が外れ、対処の一覧からデスクトップアプリの項目と、クラウドセッションにはプラグインのブラウザーがない、という項目が外れた。`claude-code-on-the-web` の、ターミナルでしか動かずクラウドセッションで使えないコマンドの例からも `/plugin` が外れ、`/resume` だけになった
  - `desktop` の「Extend Claude Code」: claude.ai のアカウントで有効にしたスキルとプラグインは、同じアカウントでサインインしたターミナルのセッションでも読み込まれる、という文が、ほかにどこで読み込まれるかはスキルとプラグインの同期の節を見る、という文になった

  リンクは `plugins/install` と `plugins/loading` の該当の節です — [日本語](https://code.claude.com/docs/ja/plugins/install#install-a-plugin) / [English](https://code.claude.com/docs/en/plugins/install#install-a-plugin)、[日本語](https://code.claude.com/docs/ja/plugins/loading#synced-plugins) / [English](https://code.claude.com/docs/en/plugins/loading#synced-plugins)
- **`.trash/` のフォルダーが期限より前に消される場合が書かれた**（`claude-directory`・`skills`）。`claude-directory` の「Cleaned up automatically」の表の `skills/.trash/`・`plugins/.trash/` の行で、消されるまで取り戻せる、という説明が、ここから取り戻す、になり、7 日より古く 3 つの新しい写しがあるフォルダーと、`.trash/` のフォルダーが 1,024 を超えたときは、期限より前に消されることがある、という文が加わりました。`skills` の「Where synced skills load」と「Personal skills disappeared」の該当の段落は注記（NOTE と TIP）になり、保持の掃除（retention sweep）が消すまで（「Personal skills disappeared」では、ごみ箱に移ってから既定で 30 日）、が、Claude Code が消すまで、になりました — [日本語](https://code.claude.com/docs/ja/claude-directory#cleaned-up-automatically) / [English](https://code.claude.com/docs/en/claude-directory#cleaned-up-automatically)
- **長い思考でプロキシがタイムアウトするときの説明が、長い要求が 1 つか 2 つ、になった**（`claude-apps-gateway-deploy` の「Troubleshooting」の表と「Long thinking ends in proxy timeouts」「Long thinking on an Anthropic API upstream」）。プロキシのログに残る約 12.5 分（`provider: anthropic` では約 20 分）の要求が、1 つから「1 つか 2 つ」になりました。240 秒のアイドルのタイムアウトの例は、10 の要求がそれぞれ 240 秒で切られる、から、ストリーミングなしで送り直した要求のそれぞれが 240 秒で終わる、という書き方になり、ゲートウェイが ping を送り続けたまま上流が止まったときは、その長さのストリームが 2 つまで続くことを見込む、という文になっています — [日本語](https://code.claude.com/docs/ja/claude-apps-gateway-deploy#long-thinking-ends-in-proxy-timeouts) / [English](https://code.claude.com/docs/en/claude-apps-gateway-deploy#long-thinking-ends-in-proxy-timeouts)
- **フックの説明が改められた**（`hooks`）。「Exit code 2 behavior per event」の表の `PermissionRequest` の行と「PermissionRequest decision control」で、終了コード 2 は決定として読まれない、という短い書き方になりました（終了コード 2 の stderr が捨てられる、という部分は外れた）。「PostToolUse decision control」の `updatedToolOutput` で、Cowork のクラウドセッションでこのフィールドを無視するツールが「`AskUserQuestion` か `ExitPlanMode` のとき」から「`AskUserQuestion` や `ExitPlanMode` のような一部のツール」になり、`updatedMCPToolOutput` も無視される、と書かれました。プロンプトのフックの `PermissionRequest` での `ok: false` は、「効果がない」から「要求を拒まない」になっています — [日本語](https://code.claude.com/docs/ja/hooks#posttooluse-decision-control) / [English](https://code.claude.com/docs/en/hooks#posttooluse-decision-control)
- **組み込みの MCP サーバーの許可リストの扱いが絞られた**（`managed-mcp`・`settings-reference`）。`managed-mcp` の「Servers that skip the allowlist check」で、許可リストを飛ばす組み込みのサーバーが、「Claude in Chrome・IDE の `ide` サーバー・CLI 自身が構成するサーバーのような組み込みのサーバー」から「IDE の `ide` サーバーや、ターミナルのセッションの Claude in Chrome のような、一部の組み込みのサーバー」になりました。`settings-reference` の `allowedMcpServers` の 2 つの段落は、許可リストを飛ばすサーバーがある（`managedMcpServers` の項目など。Claude Tag の Slack のツールは v2.1.268 以降）、managed か user の設定の拒否リストはそれらにも効く、`type: "sdk"` のサーバーはどちらのリストからも外れる、という短い段落になり、`managed-mcp` の該当の節へのリンクになりました（v2.1.259 より前は `managed-mcp.json` のサーバーも合う必要があった、という文は外れた） — [日本語](https://code.claude.com/docs/ja/managed-mcp#servers-that-skip-the-allowlist-check) / [English](https://code.claude.com/docs/en/managed-mcp#servers-that-skip-the-allowlist-check)
- **モデルを絞る例が Sonnet 5 になった**（`model-config` の「Control the model users run on」）。利用者を Sonnet で始めさせ、ピッカーを Sonnet と Haiku に絞る例が、Sonnet 4.5（`claude-sonnet-4-5`）から Sonnet 5（`claude-sonnet-5`）になり、説明も「Sonnet 5.x と Haiku」に替わりました（2 回載るページの 1 つ目で確かめた内容。2 つ目も同じです） — [日本語](https://code.claude.com/docs/ja/model-config#control-the-model-users-run-on) / [English](https://code.claude.com/docs/en/model-config#control-the-model-users-run-on)
- **auto モードと bypass permissions の説明が改められた**（`permission-modes`・`auto-mode-config`・`permissions`・`desktop`）。`permission-modes` の「Eliminate permission prompts with auto mode」で、分類器が止めるのが「要求を超えて広がる・認識しない基盤を狙う・読んだ敵対的な内容に動かされたように見えるものすべて」から「危ういと判断したもの」（「What the classifier blocks by default」へのリンク）になり、明示的な ask のルールが引き続きプロンプトを出す、という文が外れました。「Skip all checks with bypassPermissions mode」では、bypass permissions が使える対話のターミナルのセッションでは plan モードの止めに頼らない、と書かれ、Claude は引き続き編集せずに計画するよう指示される、という部分が外れています。`auto-mode-config` の冒頭からも、deny と明示的な ask のルールは分類器より先に評価される、という文が外れました。`permissions` の、`disableBypassPermissionsMode` と `disableAutoMode` は「どの設定ファイルでも」設定できる、という部分が外れて、`settings-reference` の各キーへのリンクが付き、`desktop` の同じ趣旨の文も、利用者に上書きさせないには managed settings に置く、という書き方になりました — [日本語](https://code.claude.com/docs/ja/permission-modes#eliminate-prompts-with-auto-mode) / [English](https://code.claude.com/docs/en/permission-modes#eliminate-prompts-with-auto-mode)
- **managed settings のキーの例外の書き方が改められた**（`server-managed-settings` の「Per-key exceptions across managed sources」）。「これらのキーはマージしない規則の例外」が、Claude Code は既定でほとんどのキーを 1 つの managed のソースから読み、例外には次のものがある、という書き方になりました — [English](https://code.claude.com/docs/en/server-managed-settings#per-key-exceptions-across-managed-sources)
- **スケジュールされたタスクの作成の画面の説明が改められた**（`routines` の「Create from the web」など）。リポジトリを選ぶのが、**Advanced settings** を開いて **General** のタブの **Repository** から、**Trigger** の下の **Repository** の行から（なければ **Advanced settings** の **General** のタブ）、になり、**Cloud environment** も **Trigger** の下（なければ **Advanced settings > General**）で探す、となりました。コネクターは **Advanced settings** を開いて **Connectors** のタブで扱います — [English](https://code.claude.com/docs/en/routines#create-from-the-web)
- **フィーチャーフラグの取得の説明が改められた**（`env-vars` の「First session after an install or upgrade」）。Anthropic が機能をオンにした後の最初のセッションでも、フラグで制御される機能がないことがある、という文が加わりました。`CLAUDE_CODE_FULL_SIGN_IN_LINK` の説明は、claude.ai のログインの完全な URL を出す、から、完全なログインの URL を出す、になっています — [日本語](https://code.claude.com/docs/ja/env-vars#first-session-after-an-install-or-upgrade) / [English](https://code.claude.com/docs/en/env-vars#first-session-after-an-install-or-upgrade)
- **デスクトップアプリのメニューの項目がないときの探し方が書かれた**（`desktop` の「Browse external sites」と、**Auto-verify changes** の段落）。Browser のペインの **⋮** のメニューに **Open links in built-in browser** や **Auto-verify changes** がなければ、そのメニューの **More settings** を開く、という文が加わりました — [日本語](https://code.claude.com/docs/ja/desktop#browse-external-sites) / [English](https://code.claude.com/docs/en/desktop#browse-external-sites)
- **セルフホストの構成の書き方が改められた**（`self-hosted-environments-configuration` の「How each session's config is assembled」）。`settings.json`・`CLAUDE.md`・フック・エージェント・コマンド・スキルが「すべてのセッションに」当てはまる、が「セッションに」になり、プロジェクトのスレッドの外では、Claude Code が各リポジトリの `.claude/settings.json` から `enabledPlugins` と `extraKnownMarketplaces` を読む、が、それらのキーが各リポジトリの `.claude/settings.json` から来ることもある、になりました — [日本語](https://code.claude.com/docs/ja/self-hosted-environments-configuration#how-each-session’s-config-is-assembled) / [English](https://code.claude.com/docs/en/self-hosted-environments-configuration#how-each-session’s-config-is-assembled)
- **サブエージェントと worktree の書き方に「次のような場合」が入った**（`sub-agents`・`worktrees`）。`sub-agents` の、サブエージェントがメインの会話の許可のモードを保つ場合と、`worktrees` の、掃除が worktree を残す場合の一覧が、「次の場合」から「次のような場合」になり、一覧がすべてではないという書き方になりました。`sub-agents` では、完了したサブエージェントが `SendMessage` でバックグラウンドで再開「する」が「しうる」になっています — [日本語](https://code.claude.com/docs/ja/sub-agents#permission-modes) / [English](https://code.claude.com/docs/en/sub-agents#permission-modes)
- **フルスクリーンのモードのクリックの説明が改められた**（`fullscreen` の「Use the mouse」）。選択のメニューの選択肢をクリックして選ぶ、の対象の例が「許可のプロンプト・`/model`・`/config`・選択肢の一覧を示すほかのダイアログ」から「`/model` や許可のプロンプト」になり、クリックで選べなければもう一度クリックするかキーボードを使う、という文が加わりました — [日本語](https://code.claude.com/docs/ja/fullscreen#use-the-mouse) / [English](https://code.claude.com/docs/en/fullscreen#use-the-mouse)
- **mod のガードがフックを飛ばす場合の例が減った**（`plugins/mods/admin` の「Know which hooks of a user's mod don't run」）。ガードがユーザーのフックを飛ばすほかの場合の例から、スキルの文を収めた行が外れ、組織のツールの説明（`tool.describe`）の 1 つになりました — [日本語](https://code.claude.com/docs/ja/plugins/mods/admin#hooks-the-guard-passes-over) / [English](https://code.claude.com/docs/en/plugins/mods/admin#hooks-the-guard-passes-over)
- **Projects の再起動の h3 が改称された**（`claude-projects`）。h3「Claude hasn't responded」が「Claude's replies aren't getting through」になり、バナーの文言も「Claude hasn't responded」から「Claude's replies aren't getting through」になりました。Claude は動いているが返答がプロジェクトに届いていないとき、という説明は外れています。HTML の id は旧見出しの `#claude-hasnt-responded` のままです — [日本語](https://code.claude.com/docs/ja/claude-projects#claude-hasnt-responded) / [English](https://code.claude.com/docs/en/claude-projects#claude-hasnt-responded)
- `/ide` の自動接続を止める質問と、サブエージェントのビューでの `/clear`・`/compact`・`/rewind` の質問で、Yes を先に並べるよう変更。始まりは No のままなので、Down を押して Enter で No と答えることになります
- `PermissionDenied` のフックの `retry: true` が Claude に伝える内容を、拒まれた呼び出しは、自分がその呼び出しを頼んだ場合だけ、もう一度行う、に変更
- 今後のリリース（2026年11月30日以降）での変更の予告: managed の `extraKnownMarketplaces` のプラグインのマーケットプレイスが既定で自動更新されるようになります。外すには、その項目に `"autoUpdate": false` を設定します
- Windows: レジストリの managed settings での起動を変更。`HKLM` のポリシーは `managed-settings.json` より優先され、壊れた値は起動を止めうるので、アップグレードの前に確かめます
- [VSCode] 提案された diff を保存して受け入れるのが、提案の（右の）側をクリックするか打った後だけになるよう変更。保存が拒まれたとき、または Save で閉じても何も当たらなかったときは通知が出ます
- [VSCode] ターミナルのセッションからの diff が、キーボードのフォーカスを動かさずに、保存していない変更のあるファイルの隣に開くよう変更。答えるには Accept をクリックするかターミナルを使います
- [VSCode] `allowManagedPermissionRulesOnly` が設定され、カードが allow のルールを申し出るはずのとき、許可のカードが Yes と No だけを示すよう変更。それらのカードでは、キーの 2 が No と答えます
- [VSCode] Find の欄がキーボードを失った Claude のタブで、Enter を無視して通知を出すよう変更
- スクリーンリーダーのモードでの入力の速さを改善（長いセッションほど効きます）
- 起動の時間を改善。別のセッションのすぐ後に始めたセッションはモデルの一覧を待たなくなり、`.claude/settings.local.json` のない git のリポジトリの外のセッションは git を待たなくなりました
- Windows: カスタムのシェルの起動ファイルのないマシンで、セッションの最初の Bash のコマンドの速さを改善
- プラグインの自動更新の通知を改善。依存として新しく入れたプラグインを、更新したプラグインと分けて名指します
- Code Mode のツールの検索を改善。MCP のツールの説明の、上限・形式・既定の値を含む部分をより多く示します
- `/login` と `claude auth login --console` が示す Console のサインインのリンクを改善。大幅に短くなりました
- Claude が持つ自分のアーティファクトの一覧を改善。Web のページに印が付き、Claude が Claude Docs のコネクターでそれを開こうとすることが減ります
- 短いターミナルでのフォルダーの信頼のプロンプトを改善。フルスクリーンの `/cd` と `/add-dir` が少ない行で選択肢を示し、起動時のプロンプトは警告が多くてもフォルダーのパスを見せ続けます
- [VSCode] Python の拡張機能が入っているとき、Python のない新しいフォルダーで最初の返答が出るまでの時間を改善
- [VSCode] 要求が拒まれたために開いたとき、サインインの画面がそう述べるよう改善
- [VSCode] 長い会話を開く・戻す・切り替えて戻る速さを改善（ファイルの編集が多いときと git が遅いときほど効きます）
- [VSCode] 長いチャットの応答性を改善。返答の流れている間の入力と大きなファイルの書き込みが滑らかになり、許可のプロンプトが速くなり、アクセシビリティの支援がオンのときの送信での固まりが大幅に減りました
- [VSCode] 起動とメモリーの使用を改善。パネルと新しいチャットのタブが速く開き、新しいタブの最初のメッセージが早く答えられ、Pro と Max のプランではフォルダーの信頼のダイアログが早く出ます
- [VSCode] リモートのウィンドウ（SSH・WSL・コンテナー）での速さを改善。パネルが始まり、返答が出て、セッションが開き直るのが速くなりました
- [VSCode] メモリーの少ないマシンで、チャットが数分使われていなかった後の最初のメッセージの応答までの時間を改善
- [VSCode] 遅いディスクやウイルス対策がスキャンするディスクで、チャットが始まる・履歴から開く・再起動の後に戻る速さを改善
- [VSCode] 開き直した会話で diff が出る速さを改善し、動かなかった diff のメニューの項目を外しました
- [VSCode] @ のファイルのメニューで、開いているエディターのタブのファイルを先に、いちばん最近使ったものを上に並べるよう改善

**バグ修正**

- ローカルか WebSocket のサーバーからの一部の不正な返答で、MCP のツールの呼び出しが最大 30 分止まる問題を修正
- スケジュールされた実行のようなヘッドレスの実行に、PushNotification が、モバイルへのプッシュを求めたかどうかではなく、最初の 1 分はターミナルが使われていたと伝える問題を修正
- リポジトリが見つからないとき、セットアップの警告の後に `/install-github-app` がリポジトリの手順を飛ばし、そのワークフローの一覧とサインインの手順で Esc が戻らない問題を修正
- 狭いウィンドウで 1 行のツールの結果が省略記号なしに切られる、`/permissions` の Auto mode のタブに Markdown の星が出る、フォークしたスキルを止めるフックの理由が 2 回出る、の問題を修正
- 24〜26 行のウィンドウで `/diff` がキーのヒントを隠してファイルを選べない問題と、コミットのないリポジトリで `git add -N` で加えたファイルを外す問題を修正
- 短いウィンドウで、初回のテーマの一覧が少なすぎるテーマを示し、`/usage` などの縦に長い画面が崩れる問題を修正
- フルスクリーンの `/bug` が、長い報告の後ろに Yes と No の答えを隠し、とても短いウィンドウで Yes が見えないままになる問題を修正
- 要約が特定の XML のタグを引用したとき、`/compact` と自動のコンパクションが会話の要約の一部を失うことがある問題を修正
- すでに終わったサブエージェントへのキューのメッセージを Agent のツールのパーミッションのルールが落としたとき、Claude に知らされない問題を修正
- Remote Control のメッセージが、送ったときに終わりかけていた返答の上に出ることがある問題を修正
- Claude Desktop で、トランスクリプトを読む Stop のフックが最後の返答を取り逃す問題を修正。SubagentStop のフックもそれを待つようになりました
- Claude がまだ思考している間に返答が黙ったとき、クラウドセッションでターンとサブエージェントが失敗し、ほかの場所では長い返答でタイムアウトする問題を修正。Claude Code がもう 1 回要求を試すようになりました
- Claude が読んでいるクラウドかネットワークのファイルの中身が止まったとき、Esc と Stop が 1 分以上待つ問題を修正
- `--resume` か `--continue` で別の許可のモードで再開した Code Mode のセッションが、思考とプロンプトキャッシュを失う問題を修正。尋ねるモードで始めたものは、スクリプトへのそのモードの制限を保ちます
- スクリプトの実行中に `!` かスラッシュのコマンドを打つと、Code Mode が約 1 秒ごとに要求を送る問題を修正
- 中断したか失敗したプラグインの更新が、中途半端なプラグインのフォルダーを残し、後でスキルなどの部品が欠けたまま読み込まれる問題を修正（anthropics/claude-code#102186）
- Windows: 一部のプラグインのセッションで、FAT32 と exFAT のドライブへのファイルの書き込みが毎回許可を求める問題を修正
- null の出力か、トレースバックのないエラーの出力を持つノートブックを Claude が読めない問題を修正
- 復元が失敗した後に rewind がファイルを消す問題を修正
- `/loop` を止める Claude の呼び出しを auto モードが拒むことがあり、次の起動が発火してしまう問題を修正
- Workflow のエージェントが報告を返した後も、そのバックグラウンドのシェルと MCP のサーバーが動いたまま残ることがある問題を修正
- Windows: `/desktop` が古い Claude Desktop のインストーラーをダウンロードし、古いインストールのフォルダーが残っていると更新を求める問題を修正
- managed settings が尋ねられない承認を要したとき、`claude plugin install`・`marketplace add` などのコマンドが何も出さずに止まる問題を修正
- `Agent(model:*)` のようなサブエージェントのモデルへのパーミッションのルールが、この版でモデルを名指さずに始めたサブエージェントへの Claude の続きのメッセージを止める問題を修正
- PermissionRequest のフックが、ローカルの設定の外に `Skill(name:*)` の allow のルールを保存しない問題を修正
- チームでまとめたグループの予算に止められたとき、「Ask your admin」が自分の上限を上げるよう頼み、数分以内に管理者が要求を承認していたときに「Request sent」と言う問題を修正
- Code Mode が長いスクリプトの出力の中ほどを失う問題を修正。Claude は切っていないテキストへのパスを受け取るようになりました（anthropics/claude-code#111373）
- Claude Code が忙しいとき、押して話す音声入力が早く止まって言葉を失う問題を修正
- `--bare` の Code Mode が、スクリプトが何を呼べるかを Claude に伝えない問題を修正
- カスタムの API のエンドポイントがツールの名前のないツールの呼び出しを返したときに落ちる問題を修正。その呼び出しはエラーで失敗し、セッションは続きます
- Windows: マシンのメモリーがほとんど尽きたときに落ちることがある問題を修正
- 一部の返答で CLI が固まり、引用したテキストが欠けるか 2 回出ることがある問題を修正
- Windows: レジストリの managed settings が日本語のような ASCII でない文字を含むとき、Claude Code が起動を拒む問題を修正（anthropics/claude-code#93280）
- Windows: Remote Control のクライアントが、新しいサブエージェントの手順を示さない問題を修正
- `@file#10-12` と書いた @-メンションが、その行ではなくファイル全体を添付する問題を修正
- 貼り付けたアーティファクトの招待のリンクを Claude が読み違える問題を修正。招待を受けてからアーティファクト自身のリンクを貼るよう求めるようになりました
- ファイルのルールでコマンドを一時ディレクトリから外すサンドボックスで、一時のディスクがいっぱいのとき、サンドボックスの Bash のコマンドが始まらないことがある問題を修正
- [VSCode] 言い換えたプロンプトの下の選択したコードの生のタグ、モードのボタンの Manual の点滅、スラッシュのメニューがハイライトした行を隠す、壊れたサインインの画像、点滅する Accept/Reject のバー、の問題を修正
- [VSCode] フォークした会話が元の会話の計画のファイルを上書きする問題を修正。計画を写せないフォークか rewind は警告を出すようになりました
- [VSCode] 接続が閉じたか開かなかったとき、音声入力が発話を認識できなかったと言う問題を修正。接続が失われた、またはつなげなかった、と言うようになりました
- [VSCode] パネルが閉じると、送っていないサイドクエスチョンが失われる問題を修正
- [VSCode] セッションの名前を変えた後に Escape で Claude が止まり、Escape でセッションの履歴を閉じた後に入力がどこにも行かない問題を修正
- [VSCode] 履歴からセッションを再開したタブで、Rename・Mark as Unread・Add to Group が「still connecting」と言う問題を修正
- [VSCode] 幅の広い表と長いパスが切れる、長いエラーが閉じるボタンを隠す、Add MCP server のフォームと Chrome のダイアログでエラーが見えない、プラグインの画像がエディターのテーマを無視する、の問題を修正
- [VSCode] 後のプロンプトとメッセージの欄が Rewind code のダイアログを覆い、ファイルの確認が終わるとフォーカスが「Never mind」から「Rewind」に飛ぶ問題を修正
- [VSCode] フィルターにさらに打つ間、コマンドのメニューが前の一致をハイライトしたままで、Enter で違う行が実行されうる問題を修正
- [VSCode] @ のメニューが、最初の検索の結果が届く前や、とても大きなワークスペースのすべてのファイルを検索できないときに「No files found」と示す問題を修正。検索できないときはそう言うようになりました
- [VSCode] MCP・Hooks・Memory のダイアログの Remove か Delete の確認、サイドクエスチョンのパネルのボタンかリンク、パネルを開いた Bookmarks のボタンで、Escape が Claude を止める問題を修正
- [VSCode] diff で + と − の記号の代わりに空の四角が出る問題を修正（anthropics/claude-code#73069）
- [VSCode] パネルの大きさを変えるか、隠して出し直した後、チャットが Claude の返答を追わなくなる問題を修正
- [VSCode] 設定が bypass を無効にしているとき、bypass permissions のモードのまま残したチャットが、初めの許可のモードではなく Auto のモードで開き直る問題を修正
- [VSCode] 一部の CSS のコードブロックと diff で、チャットのパネルが固まる問題を修正
- [VSCode] API のエラー、「Prompt is too long」、スラッシュのコマンドの後に、コンテキストの使用の表示が消える問題を修正
- [VSCode] キューの `/clear` の後ろにキューしたメッセージが失われる問題を修正
- [VSCode] Manage Plugins が検索の欄を失うか、一致のない検索でメッセージを出さず、使えるプラグインの一覧の読み込みに失敗したと言わない問題を修正
- [VSCode] ノートブックとカスタムのエディターのファイルへの提案された変更が、Accept と Reject のないタブに開き、答えた後も開いたままになる問題を修正
- [VSCode] 支出の上限のメッセージが、Team と Enterprise のメンバーに、パネルから管理者に要求を送れない `/usage-credits` を実行するよう言う問題を修正
- [VSCode] 「/」のボタンのメニューのコマンドで Tab を押すか、オンボーディングの提案をクリックすると、書いたメッセージが消える問題を修正
- [VSCode] Claude の作業中にコードを rewind した後も、Claude がファイルを編集し続ける問題を修正
- [VSCode] `/tasks`・`/copy`・`/export`・飛ばした `/feedback`・すでに plan モードのときの `/plan` の後に、打ったテキストが失われる問題を修正
- [VSCode] 質問のカードが、Ctrl/Cmd+Enter で打った「Other」の答えを落とし、何も打っていないときに「Other」の語を送る問題を修正
- [VSCode] ゲートウェイが名前のないツールの呼び出しを送った会話で、パネルが「Something went wrong」を示す問題を修正
- [VSCode] シンボリックリンク経由で開いたフォルダーで、保存していない変更が見落とされ、Claude の編集が次の保存で上書きされる問題を修正
- [VSCode] Claude が `cd` でフォルダーを変えた後、@-メンションが何も添付しないか、同じ名前の別のファイルを添付する問題を修正
- [VSCode] 選択している間に矢印キーが打ったテキストを古いプロンプトで置き換え、呼び出したプロンプトへの編集を落とす問題を修正
- [VSCode] 許可のプロンプトが開いている間に加えた @-メンションが失われる問題を修正
- [VSCode] Ctrl+1・Alt+1・Ctrl+Space のようなショートカットが開いているダイアログに答えてしまい、rewind の確認でファイルを戻したり git のブランチを切り替えたりしうる問題を修正
- [VSCode] ファイルのパスかコードのコメントで始まるプロンプトが、選択したコードなしに送られ、フォークと rewind のメニューを持たない問題を修正
- [VSCode] チャットのファイルのリンクが、ノートブックを除くワークスペースのファイルについて、エディターの関連付けを無視する問題を修正（anthropics/claude-code#81482）
- [VSCode] ファイルのタブを閉じた後も、選択した行が次のメッセージに添付されたままになる問題を修正
- [VSCode] Shift+Tab で Edit を通って Plan モードに移った後、新しいセッションが自動で Edit で始まる問題を修正
- [VSCode] 許可のプロンプトで編集したコマンドが、打ったか貼った改行なしに実行される問題を修正
- [VSCode] 新しく開いた Claude のタブがメッセージの欄にフォーカスしないか、ターミナルかコマンドパレットから遅れてキーボードを取り、打ったテキストをプロンプトとして送る問題を修正
- [VSCode] `@app.ts#5-10` のような Alt+K の行の範囲が、選んだ行ではなくファイル全体か最初の 2,000 行を送る問題を修正
- [VSCode] 複数のサブエージェントが承認を待つとき diff のタブが順不同に開き、同じファイルへの後の編集が前の編集を取り消す問題を修正
- [VSCode] パスの `/api` のような `/word` がほかのテキストの隣にあるとき、Enter がメッセージを書き換えるかメニューの操作を実行し、打ったスラッシュのコマンドを引数なしに実行する問題を修正
- [VSCode] Claude・フック・MCP のサーバーから Electron のアプリと拡張機能のテストが始まらない問題を修正。VS Code を Node として動かすラッパー・フック・サーバーは `ELECTRON_RUN_AS_NODE=1` を設定する必要があります
- [VSCode] 提案された編集の一部を拒むか、受け入れる前に diff のビューで変えたとき、Claude に知らされない問題を修正
- [VSCode] 許可のプロンプトでの Escape が、取り消す代わりに打ちかけの指示を Claude に送る問題を修正
- [VSCode] Windows と Linux で、チャットの Ctrl+J と Ctrl+O が VS Code のターミナルか Open File のダイアログも開く問題を修正
- [VSCode] 素早い Tab か Enter で @ のメニューが違うファイルを入れ、合うファイルのない @word で終わるプロンプトを Enter が送らない問題を修正
- [VSCode] Claude の起動中にタブを閉じた後、新しい Claude のタブが空のままになり、サイドバーが読み込みに失敗する問題を修正
- [VSCode] パネルでの素早いダブルクリックが、1 回目のクリックの後に出たボタンか行を押し、コンテキストの使用の円から 2 回目のコンパクションを始める問題を修正
- [VSCode] settings.json が空か、バイト順マークで始まるとき、モデルの切り替えが「Settings file is not valid JSON」で失敗する問題を修正
- [VSCode] 長い会話のフォークか rewind のたびに、ウィンドウを読み込み直すまでメモリーが増える問題を修正
- [VSCode] Focus のビューで、計画の承認のカードに計画のコメントが出ない問題を修正
- [VSCode] 行番号のないファイルのリンクが、開いているファイルのカーソルを 1 行目に動かす問題を修正
- [VSCode] 同じパネルで別の会話の裏で動く会話が許可か答えを要するとき、通知が出ない問題を修正
- [VSCode] Claude Code の起動が遅いか失敗するとき Manage Plugins が読み込まれない問題を修正。起動を止めるプラグインをオフにできるようになりました
- [VSCode] `files.encoding` が UTF-8 でないとき、提案された diff が ASCII でないテキストを崩して示し、保存する問題を修正
- [VSCode] ヘブライ語・アラビア語・ペルシア語のテキストのある行で、承認した編集と書き込みが右から左への印を文字どおりの `‏` のエスケープとして保存する問題を修正
- [VSCode] Claude のプロセスが終わっていたか、まだ起動中だったとき、次のメッセージでモデルの選択が無視される問題を修正
- [VSCode] Claude のプロセスが終わった後、Rewind が「No active session」を示す問題を修正
- [VSCode] ブラウザーがつながっていないとき、@ を打つとタブごとに補助のプロセスが動いたまま残る問題を修正（Claude in Chrome のサービスに届かないときを除く）
- [VSCode] セッションの一覧がすべてのトランスクリプトを一度に開き、エディターの拡張機能を止め、セッションの多いプロジェクトでセッションを一覧から漏らすことがある問題を修正

**その他**

- **リファレンスのページの説明文**: `cli-reference`・`commands`・`interactive-mode`・`tools-reference`・`settings-reference`・`plugins/manifest-reference`・`plugins/marketplace-reference`・`self-hosted-environments-reference` の 8 ページの冒頭の説明文（と `llms.txt` の説明文）が、「Complete reference for …」から「Reference for …」になりました。`settings-reference` では「すべてのキー」「すべてのキーの索引」の「すべての」も外れています
- **外れた記述**: `analytics` から、Claude Code の助けを受けた行を含むマージ済みのプルリクエストに GitHub で `claude-code-assisted` のラベルが付く、という文と、GitHub でそのラベルのプルリクエストを探して貢献のデータを問い合わせる、という文が外れました。`artifacts` の「Update an artifact」から、ページを開いている人には更新がその場で見え、公開のたびに版ができ、ヘッダーの **Share** で見せる版を選べる、という段落が、`chrome` から、VS Code で許していないサイトへの操作のときにカードがそのサイトを許すよう申し出る、という文が、`costs` から、Claude Enterprise の消費のガイドが利用者 1 人あたりの予算の目安の金額を示す、という部分が、`agent-sdk/user-input` から、入力を変えても Claude には知らされない、という文が外れています — [English](https://code.claude.com/docs/en/analytics#attribution-process)、[English](https://code.claude.com/docs/en/artifacts#update-an-artifact)
- **言い回しの削り込み**: 約 40 ページで、「ほかに設定しなくてよい」「再起動は要らない」「別のインストールのコマンドは要らない」のような念押しの部分や、言い直しの文が外れました。たとえば `agent-teams`・`agent-view`（スーパーバイザーを自分で管理しなくてよい、スリープだけではセッションは止まらない、など）・`deep-links`・`desktop-linux`（ほかのディストリビューションへの対応は将来来る）・`desktop-quickstart`・`errors`・`features-overview`・`how-claude-code-works`（ブランチを切り替えても話したことを覚えている）・`large-codebases`・`mcp`・`memory`・`plugins/install`・`plugins/overview`・`plugins/mods/gallery`（入力の欄は空でも決めた行数を取る、の「空でも」）・`prompt-caching`・`remote-control`・`skills`・`troubleshooting`・`vs-code`・`workflows`・`worktrees`・`channels-reference`・`claude-apps-gateway`・`code-mode`・`fullscreen`・`glossary`・`hooks`（`Setup` のイベント）・`interactive-mode`・`llm-gateway-protocol`・`model-config`（`-p` での `/effort`）・`output-styles`・`plugins/marketplace-reference`・`self-hosted-environments-quickstart`・`self-hosted-environments-reference`・`settings`・`settings-reference`（フッターのバッジ）・`statusline`・`terminal-config`・`third-party-integrations` です。`security-guidance` の「Install the plugin」は、Claude が `/plugin` は使えないと返したら、から、ターミナルの外では、という書き方になりました。どれも機能の変化を伴いません — [English](https://code.claude.com/docs/en/agent-view)
- **言い方の変化**: `desktop` の「Review your code」のボタンの名前が **Walk through in Changes** から **Walk through in changes** に、`agent-sdk/python` の `TaskNotificationMessage` の `outputFile` のコメントが「エージェントの出力が書かれるファイルのパス」から「タスクの出力ファイルへのパス」になりました — [日本語](https://code.claude.com/docs/ja/desktop#review-your-code) / [English](https://code.claude.com/docs/en/desktop#review-your-code)
- **書式の変化**: `setup` の「Install Claude Code」で、引用の中のコードフェンスの 5 つの開始行の `theme={null}` が 19 回の重なりから 1 回に戻りました（2026年11月22日のサマリで 1 回から 19 回に重なったと書いた箇所）。内容の変更ではありません

見出しマップ（`en/claude_code_docs_map.md`）は、更新時刻が 2026年11月23日 05:28:13 UTC から 2026年11月23日 20:47:12 UTC に替わり、312 行が加わり 31 行が外れました（6,676 行から 6,957 行）。加わったのは新規 16 ページの見出しと、`code-review-troubleshooting` の h3 と `claude-projects` の改称後の h3 で、外れたのは `claude-code-on-the-web` の 2 つの h4 と `claude-projects` の旧見出しです。`code-review-local` と `ultrareview` の見出しは、「On-demand reviews」の下へ移っただけで、どちらも外れてから同じ形で加わっています。どのページでも、見出しマップの項目は head の `llms-full.txt` の見出しと合っていて（違いは、以前からあるアンダースコアのエスケープの有無だけ）、今回、見出しマップにだけ先に載った見出しはありません。

**参考リンクについて**: 日本語版は、今回リンクを付けたページの HTML を取得して確かめました。新規 16 ページは日本語版がすべてあり、見出しの id が英語版と同じで、本文も訳されていました（英語版の地の文が日本語版の HTML に残っていないことで確かめています）。既存のページは、今回の差分で出入りしたコードの字句・リンク先のアンカー・画像のファイル名（`approvals-setup#what-approvals-costs`・`/ship:review`・`ship-local`・`claude.ai/customize/plugins`・`1,024`・`claude-sonnet-5`・`$.tool.register`・`updatedMCPToolOutput` など、base と head の `llms-full.txt` で数が違うもの）が英語版と同じだけあるかで、今回の内容になっているかを確かめました。地の文だけが変わった節（`claude-projects`・`managed-mcp`・`claude-apps-gateway-deploy`・`fullscreen`・`plugins/mods/admin`・`env-vars`・`code-review` の冒頭）は、該当する節の訳文で確かめています。今回はどれも日本語版が今回の内容でした。確かめていない節（`server-managed-settings`・`routines`・`analytics`・`artifacts`、言い回しの削り込みの各ページ）は、英語版だけにリンクしています。アンカーは英語版・日本語版の HTML の見出しの id で確かめました。見出しの文字列の GFM スラッグと違う id を持つものがあり、`claude-projects` の改称した見出しは旧見出しの id `#claude-hasnt-responded`、`plugins/mods/admin` の「Know which hooks of a user's mod don't run」は `#hooks-the-guard-passes-over`、`plugins/loading` の「Plugins synced from claude.ai」は `#synced-plugins`、`share-sessions` の「Share from a Max, Ultra, or Pro account」は `#share-from-a-max-or-pro-account` です。`ship-command` と `ship-command-troubleshooting` の見出しの id は、`#run-/ship-or-/steward` のように `/` をそのまま含みます。**changelog ページへのリンクは、本サマリの方針どおり付けていません。** v2.1.331 の項目は、`claude doctor` の API の接続性・`oidc.groups_jsonpath`・`CLAUDE_CODE_DISABLE_RESPONSE_COMPRESSION`・`CLAUDE_GATEWAY_IDP_CONNECT_BY_HOSTNAME`・`optionalDependencies`・`gen_ai.response.model` を含め、changelog のほかのページにまだ載っていないので、リンクを付けていません。

## 新着情報

<!-- light:whats-new:start -->
（今回の差分に新着情報（`whats-new/`）のページはありません。head の `llms.txt`・`llms-full.txt`・見出しマップにも whats-new のページは載っていません）
<!-- light:whats-new:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-11-22.md](./archives/latest/2026-11-22.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-11-22.md](./archives/latest-detail/2026-11-22.md)

<!--
base_commit: 6a68e6de41597850d1e2183445a9fc2df1e65fdf
head_commit: 6b8844c93bee3ab36c9d7bb656a2476fb661c469
generated_at_full: 2026-11-24T15:21:26+09:00
-->
