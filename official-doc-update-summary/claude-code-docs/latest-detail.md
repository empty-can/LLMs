---
対象期間: 2026年10月23日 〜 2026年10月24日
作成日: 2026-10-24
---

# Claude Code 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
**今回は changelog に新しいリリースがなく（最新は前回と同じ v2.1.310）、通常のページに、Code Review が `REVIEW.md` からスキルの `SKILL.md` を取り込む方法、スケジュールしたタスクの全ページのフォームと実行の結果・「The last run」の警告、セルフホストのランナーのメモリーとプロセスの上限・アイドルのセッションの解放・アラートのルール、VS Code とデスクトップアプリでのアイドルの圧縮、サンドボックスのパスのワイルドカードが Linux で効く場所が載りました**。新しいページはなく、228 ページ中 50 ページが変わり、変更はページ単位で 977 行（追加 828・削除 149）、大幅更新は `self-hosted-environments-deploy`・`self-hosted-environments-configuration`・`self-hosted-environments-reference`・`settings-reference`・`code-review-customize`・`errors`・`routines` の 7 ページです。前回 changelog に載った v2.1.309・v2.1.310 の変更の多くに、通常のページの記述が追いつきました。総行数は 123,638 行から 124,317 行に増えました。

主要なものを以下に挙げます。

1. Code Review が `REVIEW.md` の `@.claude/skills/<folder>/SKILL.md` の行でスキルの本文を取り込めるようになり、取り込む条件（保護されたブランチ・1 ファイル 30,000 バイト・8 行まで）、レビューに届かないもの（フロントマター・`!` のコマンド・`$ARGUMENTS`・補助ファイル）、書き換わる文字が `code-review-customize` に載った
2. スケジュールしたタスクの作成でダイアログの代わりに開く全ページのフォーム（**New routine** など）、実行の結果（Succeeded・Failed・Cancelled）の読み方、「The last run」で始まる 8 つの警告と対処が `routines` と `desktop-scheduled-tasks` に載った
3. セルフホストのランナーで、セッションごとのメモリーの上限、プロセスとスレッドの上限（`pids.max`）の設定場所と測り方、固定のフリートでアイドルのセッションを解放する `--release-idle-session-min` の判断、最初のメッセージに答えないときのプロキシの設定、ランナーの減少と待ちのセッションのアラートのルールが載った
4. アイドルの圧縮が、Anthropic が選んだアカウントでは VS Code の拡張機能のチャットパネルとデスクトップアプリの Code タブでも動き、次のメッセージが最後の要求から 1 時間以上後なら、離れている間に書いた要約で圧縮すると `settings-reference` に載った
5. サンドボックスのパスの一覧でワイルドカードが Linux と WSL2 で効く場所の表と角かっこを含むディレクトリ名の書き方が `settings-reference` に、作業ディレクトリのトップレベルの `HEAD`・`objects`・`refs` をサンドボックスが消す条件が `sandboxing` に載った
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**Code Review が REVIEW.md からスキルのファイルを取り込めるようになった**](#1-code-review-が-reviewmd-からスキルのファイルを取り込めるようになった):  
  `code-review-customize` に h3「Include a skill file」と 3 つの h4 ができ、ルートの `REVIEW.md` に `@.claude/skills/<folder>/SKILL.md` の行を書くと、レビューがそのスキルの本文に従うと載りました（Code Review はスキルを実行しない）。保護されたブランチから `REVIEW.md` を読むときだけ取り込み、1 ファイル 30,000 バイト・8 行までなどの規則、レビューに届かないもの、レビューで書き換わる文字が並びます。`code-review-troubleshooting` にも取り込みを飛ばした行のメッセージが加わっています
2. [**スケジュールしたタスクの全ページのフォームと、実行の結果・「The last run」の警告が載った**](#2-スケジュールしたタスクの全ページのフォームと実行の結果the-last-runの警告が載った):  
  `routines` と `desktop-scheduled-tasks` に h4・h3「Full-page form」ができ、ボタンが **New routine** と出るときや、デスクトップアプリで **Local** と **Cloud** のメニューが開くときに、ダイアログの代わりに開くページの入力の仕方が載りました。`routines` には、実行の一覧の **Error**・**Cancelled** と **Status** の絞り込みの Succeeded・Failed・Cancelled の意味と、「The last run」で始まる 8 つの警告と対処の表もできています
3. [**セルフホストのランナーのメモリーとプロセスの上限・アイドルの解放・アラートの節群が載った**](#3-セルフホストのランナーのメモリーとプロセスの上限アイドルの解放アラートの節群が載った):  
  `self-hosted-environments-deploy` に、1 セッションずつ自分のメモリーの上限の下で動かす h3、プロセスとスレッドの上限（`pids.max`）の設定場所と 1 セッションのピークの測り方の h3、固定のフリートでアイドルのセッションを解放する h3、ランナーがセッションを拾っても Claude が最初のメッセージに答えないときにプロキシを直す h3 ができました。`self-hosted-environments-reference` にはランナーの減少と待ちのセッションのアラートのルールの例が加わっています
4. [**アイドルの圧縮が VS Code とデスクトップアプリにも広がった**](#4-アイドルの圧縮が-vs-code-とデスクトップアプリにも広がった):  
  `settings-reference` の `idleCompaction` に h4「Idle compaction in VS Code and the desktop app」ができ、VS Code の拡張機能のチャットパネルとデスクトップアプリの Code タブでも、Anthropic が選んだアカウントでは、離れている間に要約を書き、次のメッセージが最後の要求から 1 時間以上後のときだけその要約で圧縮すると載りました。面ごとの通知の文も示されています
5. [**サンドボックスのパスのワイルドカードと、HEAD・objects・refs を消す条件が載った**](#5-サンドボックスのパスのワイルドカードとheadobjectsrefs-を消す条件が載った):  
  `settings-reference` に h5「Where wildcards work in sandbox paths」と「Directory names with brackets, braces, or parentheses」ができ、`sandbox.filesystem` の 4 つの一覧でワイルドカードが Linux と WSL2 のどこで効くかの表と、`./app/[slug]` のような名前のディレクトリの書き方が載りました。`sandboxing` には、コマンドの後でトップレベルの `HEAD`・`objects`・`refs` を消す条件の h4 と、`objects` か `refs` のフォルダーが消えるときの h3 ができています
<!-- light:highlight-list:end -->

## 1. Code Review が REVIEW.md からスキルのファイルを取り込めるようになった

**`code-review-customize` に h3「Include a skill file」ができました。** スキルに書いてある指針にレビューを従わせるには、ルートの `REVIEW.md` にそのスキルの `SKILL.md` を取り込みます。Code Review はスキルを実行しません。`@` に続けて `.claude/skills/<folder>/SKILL.md` の形のパスを 1 行に書き（例: `@.claude/skills/api-review/SKILL.md`）、`REVIEW.md` を読むブランチを保護します。Code Review は保護されたブランチから `REVIEW.md` を読むときにだけスキルのファイルを取り込むからです。スキルのファイルは 8 ファイル・150,000 バイトの上限に数えられ、さらに 1 ファイル 30,000 バイトの上限があります。3 つの h4 は次のとおりです。

- **「Write a skill line that Code Review includes」**: フォルダー名に空白を入れません（空白のあるパスの行は `REVIEW.md` にただの文として残り、チェックランも飛ばした取り込みとして報告しない）。そのほかの規則は、**Path**（リポジトリのルートからの `.claude/skills/<folder>/SKILL.md` で、フォルダーは `skills/` の直下。ルートのファイル名と違い、この形でファイルに一致しないパスは飛ばされて数えられる）、**Source**（`.claude/` のほかのファイルや、同梱・個人・プラグインのスキルは直接取り込めないので、`REVIEW.md` の横のファイルに写す）、**File**（通常のテキストファイルとしてコミットする。シンボリックリンクはたどらない）、**Size**（フロントマターを含めて 30,000 バイト以下）、**Count**（スキルの行は 8 行まで。同じ行を繰り返しても数える）、**Blocks**（`@` の行をコードフェンスの外に置き、その上の HTML コメントと `<pre>`・`<script>`・`<style>`・`<textarea>` のブロックを閉じる）です。File・Size・Count・Blocks の規則で飛ばした行は、保護されたブランチから `REVIEW.md` を適用したレビューでだけ、チェックランの飛ばした取り込みの行のメッセージに数えられます
- **「Check what a review gets from a skill」**: レビューが受け取るのは `SKILL.md` の本文だけです。フロントマター（`description` が示す使う条件など）は本文にも書き、`!` のコマンドが出すはずのものは書き出します（Code Review はコマンドを動かさず、その行かブロック全体をプレースホルダーに置き換える）。`$ARGUMENTS` などの置換は固定の文にし（レビューは引数を渡さず、書かれたまま残る）、スクリプト・リンク先のファイル・`@file` の参照は読み込まれないので要るものを `SKILL.md` に写し、リポジトリのファイルへのリンクは何を指すかを言葉で書きます。指摘の除外と Nit の上限は、スキルではなく `REVIEW.md` かその横のファイルに書きます（Code Review はスキルの文をその理由として受け付けない）。スキルの `!` のコマンド・`$ARGUMENTS`・リンクを書き換えると Claude Code でのスキルの動きも変わるので、チームがそれに頼っているなら、指針を `REVIEW.md` の横のファイルに写してそちらを取り込むよう勧めています
- **「Characters that Code Review changes in skill text」**: Code Review はスキルの文の一部の文字を変えます。例では、`` `items[0]` `` が `ˋitems(0)ˋ` に、`` `List<String>` `` が `ˋList< String>ˋ` に、`` `ps | grep api` `` が `ˋps ¦ grep apiˋ` に、`@alice` が `@ alice` になります。規則がそれらの文字に頼るなら、言葉でも書きます

**既存の節も追従しています。** h3「Include other files in REVIEW.md」の確認の一覧では、ルートに置く（**Location**）・1 段だけ（**One level**）の規則にスキルのファイルの例外が、リンクを 64 個までに保つ（**Links**）規則にスキルのファイルのリンクは数えないことが加わりました。h3「Which branch REVIEW.md is read from」にも、除外と Nit の上限は取り込んだスキルではなく `REVIEW.md` かその横のファイルに書く、と加わっています。`code-review-troubleshooting` の h2「The check run mentions REVIEW.md」は「3 つのメッセージ」から「4 つのメッセージ」になり、**「include line(s) in the root REVIEW.md were skipped on this review」**（ルートの `REVIEW.md` は適用されたが、その行が名指すファイルは適用されなかった。「Include other files in REVIEW.md」と、スキルなら「Include a skill file」の一覧を確かめる）が加わりました。changelog に対応する項目はありません。

- [Code Review をカスタマイズする - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/code-review-customize#include-a-skill-file)
- [Customize Code Review - Claude Code Docs (English)](https://code.claude.com/docs/en/code-review-customize#include-a-skill-file)
- [Code Review のトラブルシューティング - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/code-review-troubleshooting#the-check-run-mentions-review-md)
- [Troubleshoot Code Review - Claude Code Docs (English)](https://code.claude.com/docs/en/code-review-troubleshooting#the-check-run-mentions-review-md)

## 2. スケジュールしたタスクの全ページのフォームと、実行の結果・「The last run」の警告が載った

**`routines` の「Create from the web」に h4「Full-page form」ができました。** 作成の手順の 1 つ目は、続ける前に確かめる画面の一覧になりました。ボタンが **New task** ではなく **New routine** と出る場合、デスクトップアプリで **Local** と **Cloud** のメニューが開く場合、ダイアログの代わりに全ページが開く場合は「Full-page form」へ進み、**Create with Claude** と **Set up manually** のメニューが開く場合は **Set up manually** を選んでダイアログを開きます。全ページのフォームでは（デスクトップアプリのメニューでは **Cloud** を選ぶ）、**New routine** か **New scheduled task** という題のページで次を入力し、**Create** を押すとタスクの詳細のページが開きます（**Create** が押せないときは、カーソルを合わせると足りないものが出る）。

- **Name**: 名前
- **Instructions**: プロンプト。同じ箱でモデル・リポジトリ・環境も選ぶ
- **Select a trigger**: **Schedule**・**GitHub event**・**API** のどれか。API のトリガーは、**Create** の後に開く **API token** のダイアログからトークンを写す（表示は 1 回だけ）。複数を組み合わせるには **Add another trigger**
- **Connectors**: つないでいるコネクターは既定ですべて入るので、タスクに要らないものを外す

**`desktop-scheduled-tasks` にも h3「Full-page form」ができました。** **Local** と **Cloud** のメニューで **Local** を選ぶと、**New local routine** か **New local scheduled task** という題のページが開き、**Name**（タスクの間で一意）・**Description**・**Instructions**（同じ箱で権限モード・モデル・タスクを動かすフォルダーも選ぶ）・**Schedule** を入力します。このフォームでも 6 つのスケジュールの選択肢が使えます。ページの冒頭には、アプリが機能を前の名前で出すなら、このページの **Scheduled** を **Routines** に、**New task** を **New routine** に読み替える、という NOTE が加わり、`routines` の「Where the name routines still appears」にも、一部のアカウントではアプリのサイドバーとページの題が **Routines**、ボタンが **New routine** と出る、という **App** の項目が加わりました。

**`routines` の「View and interact with runs」では、実行の結果の読み方が改められました。** タスクの詳細のページの **History** で、終わった各実行の行は、失敗なら **Error**、取り消しなら **Cancelled** で終わり、成功ならどちらも付きません。**Status** の絞り込みは同じ 3 つを **Failed**・**Cancelled**・**Succeeded** と呼びます。これらはセッションがどう終わったかを示すもので、プロンプトの仕事を Claude が終えたかではありません。

- **Succeeded**: Claude Code が失敗を報告せずにセッションが終わった。ブロックされたネットワークの要求、欠けたコネクターのツール、Claude が終えられなかった仕事は、行ではなくトランスクリプトに出る
- **Failed**: セッションが正常に終わらなかった（予期せず止まった、エラーで終わった、実行が始まる前にアーカイブされた など）
- **Cancelled**: 実行は失敗せず、そのセッションがアーカイブされた。成功した実行のセッションをアーカイブすると **Cancelled** に変わるが、タスクを変える必要はない

これまでの「実行の一覧の緑の状態は、セッションが基盤のエラーなく始まり終わったことを示すだけ」という NOTE は外れました。

**トラブルシューティングには h3「"The last run" warnings」ができました。** **History** の下に「The last run」で始まる警告が出たら表の行のとおりに対処し、警告は後の実行が始まると消えます。8 つの警告は、組織の同時に動くクラウドのセッションの上限に達した（タスクの変更は要らず、後で **Run now** か次の実行を待つ）、クラウドの環境が見つからないか使えない（**Edit** で環境のセレクターが **Unavailable environment** なら別の環境を選んで保存する）、要るものにアクセスできないか組織のポリシーが許さない（GitHub のアクセスを確かめ、Owner にポリシーを尋ねる）、たいてい一時的な問題（**Run now**）、リポジトリかブランチが使えない（開始のブランチの有無と GitHub のアクセスを確かめ、切れていればつなぎ直す）、設定の一部が受け付けられなかった（**Edit** でどの設定かは示されないので、名前・プロンプト・モデル・リポジトリ・環境・コネクター・トリガーを確かめる）、使用上限に達した（「Usage and limits」を見る）、「The last run failed.」（**Run now** か次の実行を待つ。失敗した実行には開くセッションがない）です。changelog に対応する項目はありません。

- [スケジュールタスクで作業を自動化する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/routines#full-page-form)
- [Automate work with scheduled tasks - Claude Code Docs (English)](https://code.claude.com/docs/en/routines#full-page-form)
- [スケジュールタスクで作業を自動化する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/routines#the-last-run-didnt-start)
- [Automate work with scheduled tasks - Claude Code Docs (English)](https://code.claude.com/docs/en/routines#the-last-run-didnt-start)
- [Claude Code Desktop でスケジュール設定されたタスクを実行する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/desktop-scheduled-tasks#full-page-form)
- [Schedule recurring tasks in Claude Code Desktop - Claude Code Docs (English)](https://code.claude.com/docs/en/desktop-scheduled-tasks#full-page-form)

## 3. セルフホストのランナーのメモリーとプロセスの上限・アイドルの解放・アラートの節群が載った

**`self-hosted-environments-deploy` の「Size CPU and memory for sessions」に 2 つの h3 ができました。** ランナーは `--capacity` で同時に動かすセッションの数を絞るだけで CPU とメモリーを分けないので、1 つのセッションのメモリーの使用がほかを終わらせないようにするには、1 ランナー 1 セッションで自分のメモリーの上限を付けて動かす、と改められました（これまでは「1 セッションの取り分を絞るにはラッパースクリプトから上限をかける」）。1 つのホストで複数のランナーのコンテナーを動かすなら、ホストはランナーの容量の合計で見積もる（メモリーは 1 セッション分 × 合計 + ホスト自身のプロセス、CPU は要求 × 合計か、一斉にバーストさせるなら上限 × 合計）、各ランナーに自分のコンテナーを与え、同じ `--base-dir` のパスをほかのランナーのコンテナーがマウントしないストレージに置く、という項目も加わっています。

- **h3「Give each session its own memory limit」**: 各ランナーを `--capacity 1` で、1 セッション分のメモリーの上限の下で動かします。コンテナーなら 1 コンテナー 1 ランナーにして上限を付け（Kubernetes の `limits.memory`、Docker の `--memory`、Compose の `mem_limit`）、上限の合計をホストのメモリーより下に保ちます（ホスト自身が尽きるとカーネルはホストのどこのプロセスでも殺しうる）。コンテナーなしの systemd なら、ランナーのユニットに `MemoryMax` を設定し、1 ホスト 1 ランナーにします（同じ `--base-dir` のランナーは clone したリポジトリを共有するため）。`--capacity` が 1 を超えるとセッションは 1 つの上限を共有し、カーネルはセッションごとに殺すプロセスを選ばないので、Kubernetes の kubelet の `singleProcessOOMKill` のどちらの値でも、ラッパーのメモリーの `ulimit`（`ulimit -v` はプロセスごと）でも分けられない、と注意しています
- **h3「Leave room under process and thread limits」**: プロセスとスレッドの上限は、1 セッションの必要量 × 上限を共有するセッションの数で見積もります（達すると新しいプロセスとスレッドが `EAGAIN`・`Resource temporarily unavailable` で断られ、どのセッションのコマンド・ビルド・テストも失敗しうる）。例は、1 セッションのピーク 300 で 4 セッションなら 1,200、上限 2,400 なら 2 倍のビルドの余地が残る、です。h4「Where to set each limit」は、`pids.max` を Kubernetes ではランナーを動かすノードの kubelet の `podPidsLimit`（Pod の spec では設定できず、1 Pod のコンテナーが共有）、Docker では `--pids-limit` か Compose の `pids_limit`、systemd ではユニットの `TasksMax`（未設定なら `DefaultTasksMax`）で、`ulimit -u` はランナーのユーザー ID で動くホストのすべてが共有し root には効かない、という表です。h4「Measure one session's peak」は、1 つのランナーを `--capacity 1` で、ほかのランナーのないホストと環境で始め、ホストで `/proc/<pid>/cgroup` からランナーの cgroup のディレクトリ（cgroup v1 か v2）を見つけ、代表的なビルドを 1 セッション走らせて `pids.peak`（なければ毎秒の `pids.current` の最大で、低めの見積もり）を読み、共有するセッションの数を掛けて上に上限を置く、の 5 手順です。h4「Check a `pids.max` limit」は、カーネルのログの `cgroup: fork rejected by pids controller in` で上限に達したかを、cgroup の各階層の `pids.max` の最小値で効いている上限を確かめる方法です
- **h3「Release idle sessions on a fixed fleet」**（「Scale the fleet」の下）: 固定のフリートで、すべてのランナーがオンラインなのにセッションが待たされるなら、アイドルのセッションが原因かもしれません。既定ではセッションはターンが終わっても枠を保ち、ランナーはその所有者に固定されるので、実行のたびに新しいセッションを始めるチームのクラウドのスケジュールしたタスクがすべての枠を埋めうるためです。各ランナーの Prometheus の `claude_code_self_hosted_runner_session_idle_seconds`（忙しい間は `0`、それ以外はアイドルになってからの秒数）を、許すアイドルの時間（作業の途中の休みより長く、次の実行の前に解放される程度に短い）と比べ、超える系列があれば `--release-idle-session-min`（例: `--release-idle-session-min 30`）をすべてのランナーに付けます。すべて下回るならランナーを増やすか、アイドルにならないセッションに `--kill-session-after-min` を付けます。解放したセッションは次のメッセージでプッシュしていない作業なしで再開し、最後のセッションを解放したランナーは通常の終了を始めるので、監督のプロセスに新しいファイルシステムで再起動させる、と注意しています
- **h3「A session is picked up, but Claude never answers its first message」**（トラブルシューティング）: ランナーがセッションを拾っても Claude が最初のメッセージに答えず、ランナーがプロキシを通して `api.anthropic.com` に届くなら、プロキシが原因かもしれません。Anthropic はセッションのメッセージを開いたままの 1 本のストリーミングの応答（`GET https://api.anthropic.com/v1/code/sessions/<session-id>/worker/events/stream`）で送るので、プロキシがバッファーするか何も渡さず終えると最初のメッセージが届きません。応答（`text/event-stream`）を届いたとおりに通し、最長 1 時間開いたままにし、アイドルのタイムアウトは 15 秒より十分長くします（既定ではキープアライブが少なくともその間隔で来る）。ランナーのタイムアウトを上げても待ちが長くなるだけです。h4「Confirm the cause in the runner's log」は、v2.1.287 以降のランナーで `--startup-timeout-min`（既定 15 分）が過ぎて `no child output for` の行が出た後、`SDKStartup: SSE` を探し、`SSE connect failed (no response in 30s)`・`SSE liveness timeout`・`SSE stream ended by server` の繰り返しなどの行ごとの対処を示す表です。h4「Stop the session from trying again」によると、セッションはメッセージを保留したまま拾われ直すので、プロキシを直すまでは claude.ai/code でアーカイブします。トラブルシューティングの一覧と、`self-hosted-environments` のネットワークの節にも、この h3 への案内が加わりました

**`self-hosted-environments-reference` には h3「Alert on lost runners and waiting sessions」ができました。** 固定のフリートでは、登録されスクレイプされたランナーが下限を 10 分下回ると発火する `ClaudeRunnersBelowFloor`（下限はレプリカ数の半分を切り上げた程度。`namespace` のマッチャーとラベルを置き換え、ポーリングできないランナーも数えるので `ClaudeRunnerPollStale` と `ClaudeRunnerPollErrors` も残す）を、オンデマンドのランナーでは、ランナーを待つセッションが 10 分 0 を超える `ClaudeOrchestratorSessionsWaiting` と、直近 10 分のキューの待ちの 1% 超が 160 秒を超え、それが 5 分続く `ClaudeOrchestratorQueueWaitHigh`（`ClaudeOrchestratorDisconnected` も残す）を読み込みます。changelog に対応する項目はありません。

- [本番環境へのセルフホスト環境のデプロイ - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/self-hosted-environments-deploy#give-each-session-its-own-memory-limit)
- [Deploy self-hosted environments to production - Claude Code Docs (English)](https://code.claude.com/docs/en/self-hosted-environments-deploy#give-each-session-its-own-memory-limit)
- [本番環境へのセルフホスト環境のデプロイ - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/self-hosted-environments-deploy#release-idle-sessions-on-a-fixed-fleet)
- [Deploy self-hosted environments to production - Claude Code Docs (English)](https://code.claude.com/docs/en/self-hosted-environments-deploy#release-idle-sessions-on-a-fixed-fleet)
- [本番環境へのセルフホスト環境のデプロイ - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/self-hosted-environments-deploy#when-a-sessions-first-message-is-never-answered)
- [Deploy self-hosted environments to production - Claude Code Docs (English)](https://code.claude.com/docs/en/self-hosted-environments-deploy#when-a-sessions-first-message-is-never-answered)
- [セルフホスト環境リファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/self-hosted-environments-reference#alert-on-lost-runners-and-waiting-sessions)
- [Self-hosted environments reference - Claude Code Docs (English)](https://code.claude.com/docs/en/self-hosted-environments-reference#alert-on-lost-runners-and-waiting-sessions)

## 4. アイドルの圧縮が VS Code とデスクトップアプリにも広がった

**`settings-reference` の `idleCompaction` に h4「Idle compaction in VS Code and the desktop app」ができました。** VS Code の拡張機能のチャットパネルとデスクトップアプリの Code タブでは、Anthropic が選んだアカウントでアイドルの圧縮が動きます。Claude Code は離れている間に要約を書き、次のメッセージが最後の要求から 1 時間以上後のときだけ、その要約で圧縮します。`Compacted using a summary written while you were away · turn off with "idleCompaction": false in settings.json` のような通知は、前の会話が Claude がこれから使う要約に置き換わったことを示し、何もする必要はありません。止めるには `~/.claude/settings.json` などの設定ファイルで `idleCompaction` を `false` にします。

**`idleCompaction` の説明も改められました。** 「プロンプトキャッシュが切れる少し前に」という語が外れ、圧縮した後の通知が面ごとに示されています。

- **ターミナル**: `Compacted while idle, before the prompt cache expired` で始まる行
- **VS Code のチャットパネル**: `a summary written while you were away` を含む通知
- **デスクトップアプリ**: 同じ通知が、`Claude Code notice` を含むラベルの行の中に出る（行かその文が見えなければ Verbose の表示モードに切り替える）

既定でオンになる条件の **Session** は「対話的なターミナルのセッション」から、それに加えて Anthropic が選んだアカウントでの VS Code の拡張機能のチャットパネルかデスクトップアプリの Code タブ、に広がりました。`/config` の **Idle compaction** の行は「ターミナルのセッションの中から」切り替える、と限定され、設定の索引の説明も「ターミナルのセッションがアイドルの間」から「離れている長い会話」に言い換えられています。

**関連ページも追従しています。** `prompt-caching` の「Compacting the conversation」からは「ターミナルのセッションで」「キャッシュが切れる少し前に」が外れました。`llm-gateway-protocol` の `x-claude-code-compaction` の値 `auto` は対話的なターミナルのセッションのアイドルの圧縮に付くと限定され、圧縮の前にバックグラウンドで要約を書く要求には付かない、と加わりました。`monitoring-usage` の圧縮のイベントの `precompute_reuse` も、対話的なターミナルのセッションのアイドルの圧縮で `trigger` が `"auto"` のときに付く、と改められています。changelog に対応する項目はありません。

- [すべての設定 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/settings-reference#idle-compaction-in-vs-code-and-the-desktop-app)
- [All settings - Claude Code Docs (English)](https://code.claude.com/docs/en/settings-reference#idle-compaction-in-vs-code-and-the-desktop-app)
- [すべての設定 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/settings-reference#idlecompaction)
- [All settings - Claude Code Docs (English)](https://code.claude.com/docs/en/settings-reference#idlecompaction)

## 5. サンドボックスのパスのワイルドカードと、HEAD・objects・refs を消す条件が載った

**`settings-reference` の「Sandbox path prefixes」に h5「Where wildcards work in sandbox paths」ができました。** ワイルドカード `*`・`?`・`**` は、macOS では `sandbox.filesystem` の 4 つのパスの一覧のすべてで効き、Linux と WSL2 では効く場所が限られます。

| 一覧 | Linux と WSL2 で効くもの | 効かない例 → 代わりに書くもの |
| :- | :- | :- |
| `denyRead`・`allowRead` | 末尾の `/**`（`~/build/**` は `~/build` と同じ）と、エントリーの完全なパスの最初のディレクトリ名より後のワイルドカード | `denyRead` の `/**/*.pem` は何も覆わず読み取りを止めない → `/srv/**/*.pem` のようにトップレベルのディレクトリごとに 1 エントリー |
| `allowWrite`・`denyWrite` | 末尾の `/**` だけ | `./src/*` は `*` という名前のファイルかディレクトリだけを覆う → `./src`（その下すべて）か、パスごとに 1 エントリー |

例として、ホームディレクトリが `/home/alice` なら `~/keys/*.pem` の完全なパスは `/home/alice/keys/*.pem` で、最初のディレクトリ名は `home` です。Linux と WSL2 では、`/sandbox` の **Config** タブが、末尾の `/**` 以外のワイルドカードを含む `Edit` の権限ルールを警告し、それはサンドボックスのコマンドには効かないので、覆うパスかそれを含むディレクトリを、allow のルールなら `allowWrite` に、deny のルールなら `denyWrite` に加えます。これまでは「`allowWrite`・`denyWrite` では Linux と WSL2 で `*`・`?`・`[` を含むエントリーを飛ばす」「`denyRead`・`allowRead` ではワイルドカードがどのプラットフォームでも効く」と書かれ、**Config** タブは `Edit` と `Read` の権限ルールを警告するとされていました。

**h5「Directory names with brackets, braces, or parentheses」もできました。** 角かっこを含む名前のディレクトリは `./app/[slug]` のようにそのまま書き（その下すべてを覆うので末尾の `/**` は付けない）、そのディレクトリはサンドボックスのコマンドが始まるときに存在している必要があります。

- **`[slug]` のような角かっこ**: macOS のすべての一覧と Linux・WSL2 の `denyRead`・`allowRead` では、角かっこはパターンにもなり、`app/s` や `app/g` のように `slug` の 1 文字の名前のパスにも一致します。`allowRead`（macOS では `allowWrite` も）に入れると、サンドボックスのコマンドがそれらにも届くので、届かせたくないものは名前を変えます
- **`[user-id]` のように、ハイフンの左の文字が右の文字より後に並ぶ角かっこ**: どのプラットフォームのどの一覧でも、その名前のディレクトリだけを覆います。v2.1.304 より前の Linux と WSL2 では、`denyRead` か `allowRead` にこのエントリーがあるとサンドボックスのコマンドが始まりませんでした
- **波かっこと丸かっこ**: ふつうの文字なので、`~/data/{keys,tokens}` は `{keys,tokens}` という 1 つのディレクトリを覆います（これまでの波かっこの説明がここに移った）

**`sandboxing` の「Protected paths」には h4「When the sandbox deletes `HEAD`, `objects`, or `refs`」ができました。** サンドボックスのコマンドが終わった後、作業ディレクトリのトップレベルの新しい `HEAD`・`objects`・`refs` は、中身のあるフォルダーでない限り消されます。新しいとは、サンドボックスが前回設定を組んだとき（セッションの開始時か `/cd` などの変更の後）になかったことです。中身のある新しい `objects` か `refs` のフォルダーも、前回設定を組んだときに `HEAD` のファイルかシンボリックリンクがあれば、中身ごと消されます。保護するパスの一覧の、作業ディレクトリを bare リポジトリに変えるファイルの項目も、`HEAD` の横の `config` と `hooks` は `HEAD` がファイルかシンボリックリンクのとき、後から現れる `HEAD`・`objects`・`refs` は消されうる、Linux と WSL2 ではサンドボックスのコマンドがないところに作れる、と改められました（これまでは「Linux と WSL2 では、サンドボックスのコマンドの実行中に現れたトップレベルの `HEAD` か `objects`・`refs` をサンドボックスが消す」）。トラブルシューティングにも h3「A folder named `objects` or `refs` disappears after a command」ができ、セッション中に現れたトップレベルの `objects` か `refs` のフォルダーは、だれが作ったかによらず消されうるので、残すには中に何かを置き、セッション中にトップレベルに `HEAD` があったならそれを移して、そこで開いているすべての Claude Code のセッションを再起動する、v2.1.307 より前は中身があり `HEAD` がなくても消された、と載りました。changelog に対応する項目はありません。

- [すべての設定 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/settings-reference#where-wildcards-work-in-sandbox-paths)
- [All settings - Claude Code Docs (English)](https://code.claude.com/docs/en/settings-reference#where-wildcards-work-in-sandbox-paths)
- [サンドボックス化された Bash ツールを設定する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/sandboxing#when-the-sandbox-deletes-head-objects-or-refs)
- [Configure the sandboxed Bash tool - Claude Code Docs (English)](https://code.claude.com/docs/en/sandboxing#when-the-sandbox-deletes-head-objects-or-refs)

## 新規追加されたページ

<!-- light:new-pages:start -->
（今回の対象期間に新規追加・削除されたドキュメントページはありません。`llms.txt` は変わらず、URL は 275 のままで、`llms-full.txt` に展開されている固有のページも 228 のままです。`Source:` の行が 231 あり 3 ページが 2 回展開されている状態も前回と同じです）
<!-- light:new-pages:end -->

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
- [**Deploy self-hosted environments to production**](#1-deploy-self-hosted-environments-to-production) ([日本語](https://code.claude.com/docs/ja/self-hosted-environments-deploy#confirm-that-the-runner-uses-your-clone) / [English](https://code.claude.com/docs/en/self-hosted-environments-deploy#confirm-that-the-runner-uses-your-clone)):  
  174 行（追加 170・削除 4）が変わりました。ハイライト 3 のメモリーとプロセスの上限・アイドルの解放・最初のメッセージの節のほか、Claude Tag のチャンネルのセッションに github.com のリポジトリを加える h3 と、用意しておいた clone をランナーが使っているかを確かめる h3 ができ、clone の深さの説明と、セッションの開始が遅いときの対処が改められました
- [**Customize sessions in self-hosted environments**](#2-customize-sessions-in-self-hosted-environments) ([日本語](https://code.claude.com/docs/ja/self-hosted-environments-configuration#fix-re-opened-sessions-that-stay-queued-or-show-failed) / [English](https://code.claude.com/docs/en/self-hosted-environments-configuration#fix-re-opened-sessions-that-stay-queued-or-show-failed)):  
  88 行（追加 82・削除 6）が変わりました。開き直したセッションが Queued のままか Failed になるときに spawn-runner のフックを直す h4、server-managed settings の取得に失敗したセッションを止める h3、システムプロンプトの引数が長すぎてセッションが始まらないときの h4 ができ、Claude Tag のセッションの Slack のチャンネルの ID の変数が加わりました
- [**Self-hosted environments reference**](#3-self-hosted-environments-reference) ([日本語](https://code.claude.com/docs/ja/self-hosted-environments-reference#session-startup-timeout) / [English](https://code.claude.com/docs/en/self-hosted-environments-reference#session-startup-timeout)):  
  84 行（追加 76・削除 8）が変わりました。ハイライト 3 のアラートのルールの例のほか、`--startup-timeout-min` の数え方の h3「Session startup timeout」ができ、既存のアラートのルールの例が namespace ごとの集計に改められました
- [**All settings**](#4-all-settings) ([日本語](https://code.claude.com/docs/ja/settings-reference#disableallhooks) / [English](https://code.claude.com/docs/en/settings-reference#disableallhooks)):  
  73 行（追加 59・削除 14）が変わりました。ハイライト 4 のアイドルの圧縮とハイライト 5 のサンドボックスのパスのほか、`availableModelsMatch` の `"exact"` の日付付きの ID、Agent SDK の `managedSettings` で渡す `disableAllHooks` の効き方、`allowManagedHooksOnly` でのプラグインのモニターの扱いが改められました
- [**Customize Code Review**](#5-customize-code-review) ([日本語](https://code.claude.com/docs/ja/code-review-customize#include-other-files-in-review-md) / [English](https://code.claude.com/docs/en/code-review-customize#include-other-files-in-review-md)):  
  68 行（追加 65・削除 3）が変わりました。ほぼすべてがハイライト 1 のスキルのファイルの取り込みです
- [**Error reference**](#6-error-reference) ([日本語](https://code.claude.com/docs/ja/errors#mcp-server-is-disabled) / [English](https://code.claude.com/docs/en/errors#mcp-server-is-disabled)):  
  65 行（追加 61・削除 4）が変わりました。ゲートウェイの後ろで待機のバナーが出たり消えたりするときの h4、オフにした MCP サーバーのツールを呼んだときの h3、非対話のセッションで MCP サーバーの質問に答えがないままツールの呼び出しがタイムアウトしたときの h3、git の入っていない Mac の h3 ができました
- [**Automate work with scheduled tasks**](#7-automate-work-with-scheduled-tasks) ([日本語](https://code.claude.com/docs/ja/routines#add-a-github-trigger) / [English](https://code.claude.com/docs/en/routines#add-a-github-trigger)):  
  50 行（追加 44・削除 6）が変わりました。ハイライト 2 の全ページのフォームと実行の結果・警告のほか、GitHub のトリガーに Issue のイベントが、スケジュールのトリガーに cron の式の時間帯の説明が加わりました
<!-- light:updated-pages:end -->

**行数の数え方**: `llms-full.txt` をページ単位に切り出し、`git diff --no-index --numstat` で数えた値です。base と head はどちらも Markdown の書式なので、書式の正規化はしていません。この方法で 50 行以上のページを挙げました（`routines` はちょうど 50 行）。次点は `claude-code-on-the-web` の 40 行（追加 30・削除 10）、`hooks` の 38 行（追加 29・削除 9）、`fast-mode` の 32 行（追加 21・削除 11）です。

## 1. Deploy self-hosted environments to production

ページの差分の大半は、ハイライト 3 の h3「Give each session its own memory limit」「Leave room under process and thread limits」（と 3 つの h4）「Release idle sessions on a fixed fleet」「A session is picked up, but Claude never answers its first message」（と 2 つの h4）と、「Size CPU and memory for sessions」の書き換えです。そのほかは次のとおりです。

- **新しい h3「Add github.com repositories to Claude Tag channel sessions」**: Claude が Claude Tag のチャンネルのセッションに github.com のリポジトリを加えられないときは、ランナーがそれを clone できても、チャンネルにアクセスがあるかを確かめます。そのアクセスはランナーの git の資格情報ではなく、GitHub と Claude の組織の設定から来ます。手順は、① リポジトリを持つ GitHub の組織かアカウントに Claude GitHub App を入れ、そのリポジトリを含める、② **Organization settings > Git providers** でその組織かアカウントを Claude の組織にリンクする（GitHub の組織も持つ Claude の組織の Owner がリンクできる）、③ Claude Tag の管理者の設定で、チャンネルか、それを含む範囲（Slack のワークスペースかすべての Slack）にリポジトリを付与する（Owner か Claude Tag Admin の権限を持つ人ができ、GitHub アカウントがリポジトリの管理者であるチャンネルの管理者も自分のチャンネルに加えられる）、の 3 つで、その後チャンネルで新しいスレッドを始め、最初のメッセージでリポジトリを名指します
- **「Reuse a pre-warmed checkout」の clone の深さ**: 「どんな形の clone でも使える」という項目が **Clone depth** に改められました。clone は `--depth` なしで（`--single-branch` の有無は問わない）作ります。ランナーは `origin` のリモートを持つ clone に取得するとき、`CLAUDE_RUNNER_FETCH_DEPTH` を設定していても `--depth` を渡しません。完全な clone なら各セッションは足りないコミットだけを取得し、浅い clone では、clone の最も古いコミットより前に分かれたブランチのセッションがそのブランチの履歴全体を取得します
- **新しい h3「Confirm that the runner uses your clone」**: `--log-level debug` でランナーを始めてリポジトリのセッションを始めると、`Prefetched repo found at` と clone のパスが記録されます。代わりに `No prefetched repo, fresh init at` と出たら、その行のパスに clone があるか、ランナーのユーザーが所有しているか、`origin` という名前のリモートがあるかを確かめます。clone が見つかってもセッションの開始が遅いなら、clone が浅いかを確かめます
- **トラブルシューティングの「Sessions take minutes to start or resume」**（旧「Sessions take minutes to start」）: 原因の一つは新しい clone で、各ランナーを空のディスクで始め、`checkout` のフックがないフリートでは、ランナーが Claude Code を始める前にセッションのリポジトリを clone し直し、空のディスクで再開したセッションも同じ clone を待つ、と書き直されました。用意した clone を使い、すでに使っているならランナーが使っているかを確かめ、ランナーが自分で clone して 1 セッションで終わるなら `CLAUDE_RUNNER_FETCH_DEPTH` を既定の 50 コミットから下げます。フックを使うなら、それが clone の代わりに動くのでフックの処理を見ます
- **「Additional limitations」**: プッシュしていない作業を失う項目にあった「コミットしていない変更は失われる」が独立した項目になり、Claude が応答を終えたときにコミットしてプッシュするよう促す方法への案内が付きました。失ったランナーで途切れたコマンドがもう一度動きうる、という項目も加わり、別のランナーでセッションが再開すると、Claude は結果が不明だという結果の付いた途切れたツールの呼び出しを見る、と載っています（前回の changelog の v2.1.309 の改善に対応）

- [本番環境へのセルフホスト環境のデプロイ - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/self-hosted-environments-deploy#confirm-that-the-runner-uses-your-clone)
- [Deploy self-hosted environments to production - Claude Code Docs (English)](https://code.claude.com/docs/en/self-hosted-environments-deploy#confirm-that-the-runner-uses-your-clone)
- [本番環境へのセルフホスト環境のデプロイ - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/self-hosted-environments-deploy#additional-limitations)
- [Deploy self-hosted environments to production - Claude Code Docs (English)](https://code.claude.com/docs/en/self-hosted-environments-deploy#additional-limitations)

## 2. Customize sessions in self-hosted environments

- **新しい変数 `CLAUDE_CODE_REMOTE_SLACK_CHANNEL_ID`**: Claude Tag のセッションでは、セッションが受け持つか、そのスレッドがある Slack のチャンネルか DM の ID（例: `C0123ABCDE`）が入ります。Slack のタイムスタンプは 1 つのチャンネルの中のメッセージを示すので、`CLAUDE_CODE_REMOTE_SLACK_THREAD_TS` と一緒に記録します（ほかのセッションでは未設定で、Claude Tag のセッションでも未設定でありうる）。`CLAUDE_CODE_REMOTE_SLACK_*` の変数は、ラッパーか `command` のフックと、セッションが動かすもの（シェルのコマンド・git のフック・Claude Code のフック）で読め、`checkout`・`post-session`・`spawn-runner` のフックには渡りません。`set -u` のスクリプトで既定値付きで展開する変数の一覧にも加わりました
- **新しい h4「Fix `Argument list too long` at session start」**（「Pass the system prompt flags through」の下）: Linux で、コントロールプレーンのプロンプトと自分の文を 1 つの `--append-system-prompt` の引数につなぐと、引数が 128 KB に達したところで、ランナーが `child exited 126: ... Argument list too long` を含む行を記録します。Linux は 1 つの引数を 32 メモリーページ（ふつうの 4 KB のページで 128 KB）に制限し、`getconf ARG_MAX` の値（多くは 2 MB）は引数と環境の全体にかかる別の上限です。v2.1.283 以降では、ファイルのフラグを `"$@"` に残して自分の文だけを `--append-system-prompt` で渡すと、Claude Code はコントロールプレーンのプロンプト、自分の文の順に両方を使います。自分の文が 128 KB に達するなら、それも 1 つの引数なので、ランナーのイメージの `CLAUDE.md` に移します。v2.1.281・v2.1.282 ではそのコマンドが `Cannot use both --append-system-prompt and --append-system-prompt-file` で終わり、それより前の版ではエラーなしに自分の文がコントロールプレーンのプロンプトを置き換えるので、先に更新するか自分の文を `CLAUDE.md` に移します
- **spawn-runner のフックの約束**: 規則 1 の、セッションの ID で名付けたか重複を除いた workload は「そのセッションでは 1 回だけ作られ二度と作られない」が、「最初のものがある間は作り直されない」に改められました。規則 3 の終了コード 1（とタイムアウト）には、10 回続けて失敗すると、終了コード 2 以上のときと同じくブロックされる、と加わっています
- **新しい h4「Fix re-opened sessions that stay Queued or show Failed」**（これまでの 1 段落を置き換え）: ランナーが終わった後に利用者がメッセージを送ってセッションを開き直したとき、セッションが **Queued** のままか **Failed** になるか、フックがタイムアウトするなら、原因の一つは workload をセッションの ID で名付けるか重複を除くフックです。例の `name="runner-${CLAUDE_RUNNER_SESSION_ID}"` では、最初の要求で作った workload がランナーの終了後も残っていると、同じ名前になる次の要求で何も作られずランナーが始まりません。workload があるときにフックがどうするか（何も作らず 0 で終わる・1 で終わる・2 以上で終わる・`--hook-timeout` まで待つ）ごとに、**Failed** に変わるタイミング（10 回続いた後か、すぐ）と **Activity** タブのスポーンのエラー（`runner did not register within ETA after max attempts`、フックの stderr の末尾、`exit 1` か `exit 2`、`spawn-runner hook timed out after 60000ms`）の表があります。直すには、名前かキーを `CLAUDE_RUNNER_ORDER_ID` から作り（`name="runner-${CLAUDE_RUNNER_ORDER_ID}"`）、待つフックは workload を出したら終わるようにします（待つフックはそのオーケストレーターの次のフックを遅らせる）。直した後は、**Queued** のセッションは自分で次の要求を受け、**Failed** のセッションは Owner が **Retry** を選ぶか利用者が新しいメッセージを送ります
- **新しい h3「Stop sessions that fail to fetch server-managed settings」**: server-managed settings の取得に失敗したセッションを始めさせないには、ランナーのイメージの `managed-settings.json` で `forceRemoteSettingsRefresh` を `true` にします（組織に server-managed settings がないという Anthropic の API の答えは、取得の成功に数える）。Owner が Claude Tag のチャンネルを振り向ける環境のランナーではこのキーを入れません（Anthropic の API がそれらのセッションの server-managed settings の要求を断るので、キーがあると始まらない。規則はイメージの `managed-settings.json` に置き、ほかのセッションでキーを使うなら別の環境で動かす）。Bedrock か Agent Platform のセッションは server-managed settings を取得しないので、キーによらず始まります。管理コンソールで設定していてもファイルにも設定するのは、新しいセッションには server-managed settings のキャッシュがなく、コンソールだけではキーがまだ届かないためです。取得の失敗が原因かは、セッションの最後の出力かランナーのログの `Your organization requires remote managed settings to load, but they could not be loaded.` で確かめます
- **そのほか**: `checkout` のフックの `CLAUDE_RUNNER_REPO_REF` の例に `refs/heads/<branch>` が加わりました

- [セルフホストされた環境でセッションをカスタマイズする - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/self-hosted-environments-configuration#fix-re-opened-sessions-that-stay-queued-or-show-failed)
- [Customize sessions in self-hosted environments - Claude Code Docs (English)](https://code.claude.com/docs/en/self-hosted-environments-configuration#fix-re-opened-sessions-that-stay-queued-or-show-failed)
- [セルフホストされた環境でセッションをカスタマイズする - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/self-hosted-environments-configuration#stop-sessions-that-fail-to-fetch-server-managed-settings)
- [Customize sessions in self-hosted environments - Claude Code Docs (English)](https://code.claude.com/docs/en/self-hosted-environments-configuration#stop-sessions-that-fail-to-fetch-server-managed-settings)

## 3. Self-hosted environments reference

ハイライト 3 の h3「Alert on lost runners and waiting sessions」と 2 つの h4 のほかの主な変更は次のとおりです。

- **新しい h3「Session startup timeout」**: `/code-review` のようなターンの途中でセッションが枠を失ったなら、ランナーと子のバイナリを v2.1.309 以降に更新します。v2.1.299〜v2.1.308 のランナーは、`user` か `assistant` のメッセージがないまま起動のタイムアウトが過ぎると、ターンの途中でもセッションを解放していました（前回の changelog の v2.1.309 の修正に対応）。`--startup-timeout-min <n>` は、子が clone の後 `<n>` 分以内に初期化しないとセッションの枠を解放します。子が初期化する前に始まったターンの間は、子の activity channel に行のない時間が `<n>` 分続くまで枠を保ちます。子が初期化するとこの数えはなくなって `--release-idle-session-min` が解放を決め、生きているのに固まった子を絞るには `--kill-session-after-min` を使います。フラグの表の説明は、この h3 への案内に縮められました
- **オーケストレーターの `--hook-concurrency`**: オーケストレーターは、始めたフックがすべて終わってから新しいスポーンの要求を確かめるので、遅いフック 1 つがそのオーケストレーターの次のフックを遅らせる、と加わりました
- **アラートのルールの例**: 既存の例に h3「Sample alert rules」の見出しが付き、`ClaudeRunnerInitErrorsHigh` と `ClaudeRunnerSessionStartHookErrors` の式が `sum by (namespace) (increase(...[10m])) > 3` に、要約が Pod を名指さない文に改められました。`ClaudeOrchestratorCircuitBroken` の式も、つながっているオーケストレーター（`claude_code_self_hosted_orchestrator_connected`）に限って namespace ごとに最大を取る形になっています
- **`CLAUDE_RUNNER_FETCH_DEPTH`**: 「すでにワークスペースにあるリポジトリは今の深さを保つ」が、すでにある clone は「Reuse a pre-warmed checkout」を見る、という案内に改められました（大幅更新 1 参照）

- [セルフホスト環境リファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/self-hosted-environments-reference#session-startup-timeout)
- [Self-hosted environments reference - Claude Code Docs (English)](https://code.claude.com/docs/en/self-hosted-environments-reference#session-startup-timeout)

## 4. All settings

ハイライト 4 の `idleCompaction` の h4 と、ハイライト 5 の 2 つの h5 のほかの主な変更は次のとおりです。

- **`availableModelsMatch` の `"exact"`**: 「その版の日付付きの ID を含めて」が、`"claude-opus-4-5"` のようなエントリーは日付付きの Anthropic のモデルの ID `claude-opus-4-5-20251101` も許す、という例に改められました。`availableModels` には、サードパーティのプロバイダーの ID は「Pin models for third-party deployments」を見る、と加わっています（その節の変更は「軽微な更新」参照）
- **`disableAllHooks` を Agent SDK の `managedSettings` で渡したとき**: 「キーを `allowManagedHooksOnly: true` として扱う」という説明が外れ、管理者が managed settings を配るマシンでは、管理者が埋め込みのホストにポリシーの追加を許さない限り無視される、効く場合は、ユーザー・プロジェクト・ローカル・プラグインのフックと SDK の `settings` のオプションのフックが止まり、管理者の managed のフック・強制的に有効にしたプラグインのフック・SDK のフックのコールバックは動き続ける、と書き直されました（v2.1.309 以降）。`disableCommandPluginSources` の既定の説明にも、`managedSettings` で `disableAllHooks: true` を渡すだけでは `command` のソースのプラグインは無効にならない、と加わっています
- **`allowManagedHooksOnly` で動くもの**: プラグインのモニターは、そのプラグインが強制的に有効にされていなければ始まらない、という項目が加わりました（v2.1.310 以降）
- **`allowedHttpHookUrls`・`httpHookAllowedEnvVars`**: `managedSettings` では項目のある一覧が無視されるので SDK の `settings` のオプションで渡す、という文が言い換えられ、案内の先が「空の一覧が親の設定で何をするか」になりました

- [すべての設定 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/settings-reference#disableallhooks)
- [All settings - Claude Code Docs (English)](https://code.claude.com/docs/en/settings-reference#disableallhooks)
- [すべての設定 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/settings-reference#availablemodelsmatch)
- [All settings - Claude Code Docs (English)](https://code.claude.com/docs/en/settings-reference#availablemodelsmatch)

## 5. Customize Code Review

ページの差分はほぼすべて、ハイライト 1 の h3「Include a skill file」と 3 つの h4、それに合わせた h3「Include other files in REVIEW.md」の確認の一覧の 3 項目（**Location**・**One level**・**Links**）と、h3「Which branch REVIEW.md is read from」の 1 文です。ほかに変わった記述はありません。

- [Code Review をカスタマイズする - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/code-review-customize#include-other-files-in-review-md)
- [Customize Code Review - Claude Code Docs (English)](https://code.claude.com/docs/en/code-review-customize#include-other-files-in-review-md)

## 6. Error reference

- **新しい h4「The waiting banner comes and goes behind a gateway」**（「What you see while Claude Code retries or waits」の下）: ゲートウェイを通してつないでいて、Claude が考えている間に `Waiting for API response` のバナーが出たり消えたりするなら、v2.1.309 以降に更新します。`ANTHROPIC_BASE_URL` を Anthropic の API 以外のホスト（LLM ゲートウェイなど）にした接続、Claude apps gateway のセッション、`ANTHROPIC_AWS_BASE_URL` を設定した Claude Platform on AWS では、バナーはデータのない 45 秒の後に出ます（v2.1.309 より前は 20 秒）。前回の changelog の v2.1.309 の修正に対応します
- **新しい h3「MCP server is disabled」**（「Tool errors」の下）: オフにした MCP サーバーのツールを Claude が呼ぶと、Claude Code はサーバーにつながずツールも動かさず、結果の代わりに `MCP server "<name>" is disabled — re-enable it via /mcp to use its tools` を Claude に渡します。意図してオフにしたなら何もせず、Claude にツールが要るなら `/mcp` からオンに戻し、Agent SDK のアプリでは TypeScript の `toggleMcpServer()`（`enabled` を `true`）か Python の `toggle_mcp_server()`（`enabled` を `True`）で戻します
- **新しい h3「MCP tool call timed out with the server's question unanswered」**: 非対話のモードで、MCP サーバーがツールの呼び出しの間に elicitation で入力を求め、答えが来る前に呼び出しの時間の上限が尽きたときの結果です。メッセージは `... The server asked the user a question, and no answer came before the time limit. Do not call this tool again in this turn. Tell the user that the server's question got no answer, and wait for their reply.` と続き、v2.1.310 より前は `timed out after <N>s` で終わっていました。対処は、サーバーの要求に答える `Elicitation` のフックを用意する、TypeScript の Agent SDK のアプリでは `onElicitation` のコールバックが上限より前に答えを返すようにする、サーバーの設定のエントリーの `timeout`（ミリ秒。例: 10 分の `600000`）を延ばす、対話的なセッションで自分でダイアログに答える、です。前回のサマリで見出しマップにだけ載っていた節が、今回 `llms-full.txt` に入りました（前回の changelog の v2.1.310 の変更に対応）
- **新しい h3「git is not installed on this Mac」**: Claude Code の処理が git を必要とし、見つけた git が `/usr/bin/git` にある Apple の代わりのもので、git を提供する開発者ツールが入っていないことを示します。Claude Code はそれを起動せずにこの文を出す（長いメッセージの中に出ることもある）ので、ターミナルで `xcode-select --install` を実行し、始まったインストールを終えてから、Claude Code でしていたことをやり直します
- **そのほか**: 「Find your error」の表に上の 3 つの h3 への行が加わりました。「Disk full or disk quota used up」では、「ほかの 3 つのメッセージ」が `Disk full:`・`Disk quota used up:`・`Nearly out of inodes:` と名指され、`disk quota is used up (EDQUOT)` の対処が `Disk quota used up:` と `Disk full: a test write` の項目にまとめられています（空きが残って見えても自分のファイルを消す）。「Workspace not trusted when running claude ultrareview」の対処の文も、その実行だけフォルダーを信頼する、git と Claude Code がフォルダーの git の設定とプロジェクトの設定にあるプログラムを動かせるようになる、信頼していない PR は信頼するブランチからレビューを動かす、と言い換えられました

- [エラーリファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/errors#the-waiting-banner-comes-and-goes-behind-a-gateway)
- [Error reference - Claude Code Docs (English)](https://code.claude.com/docs/en/errors#the-waiting-banner-comes-and-goes-behind-a-gateway)
- [エラーリファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/errors#mcp-server-is-disabled)
- [Error reference - Claude Code Docs (English)](https://code.claude.com/docs/en/errors#mcp-server-is-disabled)
- [エラーリファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/errors#git-is-not-installed-on-this-mac)
- [Error reference - Claude Code Docs (English)](https://code.claude.com/docs/en/errors#git-is-not-installed-on-this-mac)

## 7. Automate work with scheduled tasks

ページの差分の大半は、ハイライト 2 の h4「Full-page form」、作成の手順の 1 つ目、実行の結果の読み方、h3「"The last run" warnings」、「Where the name routines still appears」の **App** の項目です。そのほかは次のとおりです。

- **GitHub のトリガーの Issue のイベント**: 「Supported events」の表に **Issue**（issue の作成・編集・クローズ・再オープン・ラベル付け・割り当てなどの更新）の行が加わり、前置きの「次の 2 つのカテゴリーのどちらか」が「次のどのカテゴリーからでも」に改められました
- **cron の式の時間帯**: 「Add a schedule trigger」に、5 つのフィールドだけの式は時を UTC で書く（`0 9 * * 1-5` は平日の UTC 9:00）、`CRON_TZ=` の接頭辞で始まるなら残してその時間帯で書くか、消して UTC で書く、という項目が加わりました
- **そのほか**: 冒頭の「前の名前 routines は Web のアドレス・CLI・API に残っている」から場所の列挙が外れました（場所は「Where the name routines still appears」に並ぶ）

- [スケジュールタスクで作業を自動化する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/routines#add-a-github-trigger)
- [Automate work with scheduled tasks - Claude Code Docs (English)](https://code.claude.com/docs/en/routines#add-a-github-trigger)
- [スケジュールタスクで作業を自動化する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/routines#add-a-schedule-trigger)
- [Automate work with scheduled tasks - Claude Code Docs (English)](https://code.claude.com/docs/en/routines#add-a-schedule-trigger)

## 軽微な更新

<!-- light:minor-updates:start -->
今回の差分は **2 ファイル**（`llms-full.txt` と見出しマップ）で、`llms.txt` は変わっていません。`llms-full.txt` の生の差分は追加 829 行・削除 150 行で、ページの並びは変わっていません。ページ単位に切り出すと 228 ページ中 **50 ページ**が変わり、計 977 行（追加 828・削除 149）です。生の差分のほうが 1 行ずつ多いのは、2 回展開されている `plugins/install` の同じ 1 行の差し替えが両方の展開に入り、ページ単位では 1 回に数えるためです。**changelog と新着情報（`whats-new/`）のページは変わっておらず、新しいリリースはありません**（最新は前回と同じ v2.1.310）。大幅更新の 7 ページを除く **43 ページ**（375 行。追加 271・削除 104）を以下にまとめます。前回の changelog の v2.1.309・v2.1.310 の項目に対応する記述が通常のページに加わったものは、その旨を付記しています。

`llms-full.txt` の総行数は **123,638 行から 124,317 行へ 679 行増え**ました（生の差分の差し引き 829 − 150 と一致）。`Source:` の行は 231、固有のページは 228 のままで、2 回展開されている 3 ページ（`plugins/create`・`plugins/install`・`plugins/mods/overview`）も前回と同じです。コードフェンスの外の見出しは 5,855 から 5,902 へ 47 増え、外れた見出しはありません。

**新機能**

- Code Review が `REVIEW.md` からスキルのファイルを取り込む（`code-review-customize`・`code-review-troubleshooting`。詳細はハイライト 1 参照）
- スケジュールしたタスクの全ページのフォームと、実行の結果・「The last run」の警告（`routines`・`desktop-scheduled-tasks`。詳細はハイライト 2 参照）
- セルフホストのランナーのメモリーとプロセスの上限・アイドルのセッションの解放・最初のメッセージに答えないときのプロキシ・アラートのルール（`self-hosted-environments-deploy`・`self-hosted-environments-reference`・`self-hosted-environments`。詳細はハイライト 3 参照）
- VS Code とデスクトップアプリでのアイドルの圧縮（`settings-reference`・`prompt-caching`・`llm-gateway-protocol`・`monitoring-usage`。詳細はハイライト 4 参照）
- GitHub のトリガーの Issue のイベント（`routines`。詳細は大幅更新 7 参照）
- Claude Tag のセッションの Slack のチャンネルの ID を渡す変数 `CLAUDE_CODE_REMOTE_SLACK_CHANNEL_ID`（`self-hosted-environments-configuration`。詳細は大幅更新 2 参照）
- **OpenTelemetry のイベントにサブエージェントの `agent_id`・`parent_agent_id` と、ツールのイベントに `request_id` が加わった**（`monitoring-usage`）。`agent_id` はイベントを出したサブエージェントの ID（例: `a3f2c1b4d5e6f7a80`）で、サブエージェントの API とツールのイベント、その `assistant_response`、終わったサブエージェントの `subagent_completed` に付き、メインのセッションとプロセス内のチームメイトのイベントには付きません（スパンの `agent_id` は同じ値か、先頭の `a` の後にラベルを足した `acompact-3f2c1b4d5e6f7a80` のような値）。`parent_agent_id` は、そのサブエージェントを起動したか最後に再開したエージェントの `agent_id` で、それがメインのセッションなら付きません。`tool_result` と `tool_decision` の `request_id` は、そのツールの呼び出しを含んだ API の応答の ID で、その応答の API のイベントと結び付けられます。いずれも v2.1.310 以降が要ります（前回の changelog の v2.1.310 に対応する項目はない）。`OTEL_LOGRECORD_ATTRIBUTE_COUNT_LIMIT` を下げたときに `tool_decision` から先に落ちる属性も、`parent_agent_id`・`agent_id`・`request_id`・`permission_mode`・`classifier_category`・`classifier_verdict` の順の番号付きの一覧になりました — [日本語](https://code.claude.com/docs/ja/monitoring-usage#standard-attributes) / [English](https://code.claude.com/docs/en/monitoring-usage#standard-attributes)

**機能改善**

- **Monitor ツールとプラグインのモニターが Bedrock などでも使えると改められた**（`tools-reference`・`plugins/components`・`plugins/manifest-reference`・`settings-reference`）。Amazon Bedrock・Claude Platform on AWS・Google Cloud の Agent Platform・Microsoft Foundry 上か、`DISABLE_TELEMETRY` か `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` を設定したときは、機能フラグの取得がオフなら v2.1.310 以降が要る、という最低の版の項目になりました（これまでは「これらでは使えない」）。`plugins/manifest-reference` の `experimental.monitors` の説明も、モニターは `-p` のフラグでは始まらない、とだけ書く形に改められています。前回の changelog の v2.1.310 の追加（Bedrock・Vertex・Foundry と、テレメトリーか不可欠でない通信をオフにしたときにも、Monitor ツールとプラグインのモニターを追加）に対応します — [日本語](https://code.claude.com/docs/ja/tools-reference#monitor-tool) / [English](https://code.claude.com/docs/en/tools-reference#monitor-tool)
- **mod の `Image` を tmux の中で描く条件が載った**（`plugins/mods/gallery` の新しい h4「Draw an `Image` inside tmux」・`terminal-config`・`env-vars`）。条件は、Claude Code v2.1.310 以降、tmux 3.3 以降、ポップアップではなくペインで動かす、tmux を kitty 0.28 以降・Ghostty・iTerm2 3.5 以降の中で動かす、tmux の `focus-events` と `allow-passthrough` を `on`（kitty と Ghostty では `allow-passthrough` は `all` も可）にする、iTerm2 では `-CC` なし・フルスクリーンの描画・`CLAUDE_CODE_ALT_SCREEN_FULL_REPAINT` 未設定で、tmux のウィンドウを iTerm2 のウィンドウより大きくしない（`tmux display-message -p '#{window_bigger}'` が `1` なら合わせて Claude Code を再起動する）、mod の作者が `file` のパスではなく `png` か `rgba` のバイトで渡す、です。オプションを設定したら tmux から detach して attach し直し、Claude Code を再起動します（別のターミナルから attach するたびに再起動する）。`alt` の文が出る場合の一覧は GNU screen と条件を欠く tmux に分かれ、`file` のソースで `alt` の文になるのは iTerm2 と tmux になりました。`CLAUDE_CODE_FORCE_TERMINAL_IMAGES` は、GNU screen・3.3 より古い tmux・tmux のポップアップ・`allow-passthrough` がオフの tmux の中では設定しない（絵が出ず、`alt` の文の代わりに箱が出る）、と改められています。`terminal-config` の `~/.tmux.conf` の例にも `set -g focus-events on` が加わりました。前回の changelog の v2.1.310 の改善に対応します — [日本語](https://code.claude.com/docs/ja/plugins/mods/gallery#draw-an-image-inside-tmux) / [English](https://code.claude.com/docs/en/plugins/mods/gallery#draw-an-image-inside-tmux)
- **ゲートウェイの後ろの高速モードの説明がメッセージごとに組み直された**（`fast-mode` の 3 つの新しい h4・`llm-gateway-connect`・`network-config`）。「Fast mode unavailable due to network connectivity issues」は利用可否の確認が失敗した場合（`api.anthropic.com` への直接の通信を許すか、`CLAUDE_CODE_SKIP_FAST_MODE_NETWORK_ERRORS=1`）、「Fast mode is currently unavailable」は、`ANTHROPIC_BASE_URL` をゲートウェイに向けて Anthropic の API キーの形式でないゲートウェイ発行のキーを `ANTHROPIC_API_KEY` に設定したか、`CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` を設定したために、Claude Code が確認を送らず、成功した確認のキャッシュもない場合（`CLAUDE_CODE_SKIP_FAST_MODE_NETWORK_ERRORS=1`）、「Fast mode has been disabled by your organization」は `ANTHROPIC_AUTH_TOKEN` だけで認証するか、プロキシが確認を横取りして自分のページを返す場合（`CLAUDE_CODE_SKIP_FAST_MODE_ORG_CHECK=1`）です。これまでは、ゲートウェイ発行のキーは確認に使われ、Anthropic に断られて接続の問題のメッセージになる、と書かれていました。`llm-gateway-connect` のトラブルシューティングの表にも「Fast mode is currently unavailable」の行が加わり、`network-config` では既存の段落に h3「Cloud provider and LLM gateway routing」の見出しが付き、高速モードの段落が、プロキシを通して `api.anthropic.com` に届くようにしておく、確認を送るときは設定した HTTP プロキシを通してそのホストに送り、ゲートウェイには送らない、と書き直されました — [日本語](https://code.claude.com/docs/ja/fast-mode#use-fast-mode-behind-proxies-and-llm-gateways) / [English](https://code.claude.com/docs/en/fast-mode#use-fast-mode-behind-proxies-and-llm-gateways)
- **クラウドのセッションの変更の確認と PR の作成が Changes のカードからになった**（`claude-code-on-the-web`・`web-quickstart`）。Claude が変更をブランチにプッシュすると、チャットの横のパネルの **Changes** のカードに追加と削除の行数（`+42 -18` など）が出て、それをクリックすると差分の表示が開きます（セッションの題のバーかその **⋮** のメニューの **Changes** からも開け、パネルが隠れていれば **Show session rail** で出す）。差分の表示では行にコメントし、別のブランチと比べられます。PR はカードの **Create PR** で作り、下書きにするには **Create PR** を右クリックして **Create draft PR** を選んでからボタンを押します。自動修正も、カードのプルリクエストの題の横の **⋮** のメニューで **Auto-fix** をオンオフする形になりました（これまでは CI の状態のバー）。デスクトップアプリから始めるときは、環境のセレクターの **Cloud** の下の環境を選ぶ、とも改められています — [日本語](https://code.claude.com/docs/ja/claude-code-on-the-web#review-changes) / [English](https://code.claude.com/docs/en/claude-code-on-the-web#review-changes)
- **クラウドのセッションのアーカイブと削除の操作が改められた**（`claude-code-on-the-web` の新しい h4「Find an archived session」・`remote-control`）。サイドバーのセッションの **⋯** のメニューの **Archive** でアーカイブし、アーカイブしたセッションは [claude.ai/code/sessions](https://claude.ai/code/sessions) の **Archived** タブにあり、**⋮** のメニューの **Unarchive** でサイドバーの一覧に戻します。削除はサイドバーの **⋯** のメニュー、セッションのメニュー、**Archived** タブの 3 か所からできます（これまではアーカイブしたセッションを絞り込んでアイコンを選ぶ）。`remote-control` のアーカイブされたセッションの探し方の案内も、この h4 を指すようになりました — [日本語](https://code.claude.com/docs/ja/claude-code-on-the-web#find-an-archived-session) / [English](https://code.claude.com/docs/en/claude-code-on-the-web#find-an-archived-session)
- **クラウドのセッションのトラブルシューティングに 2 つの h3 ができた**（`claude-code-on-the-web`）。「Your new session couldn't start」は、送ったプロンプトが送った元の入力の箱に戻り、**Connection lost** ならインターネットの接続と VPN かプロキシを確かめて送り直し、**Server error** なら少し待って送り直す（また出るなら status.claude.com を確かめる）、という節です。「Can't rewind to this message」は、Claude Code v2.1.246 より前のセルフホストのランナーで動くセッションでは、最新のもの以外のメッセージで **Rewind to here** がこのエラーで失敗するので、組織のランナーを運用する人に更新を頼む、という節です — [日本語](https://code.claude.com/docs/ja/claude-code-on-the-web#troubleshooting) / [English](https://code.claude.com/docs/en/claude-code-on-the-web#troubleshooting)
- **クラウドのセッションのカスタムロールの注記が改められた**（`claude-code-on-the-web` の冒頭）。カスタムロールがアクセスを決めるなら、ブラウザー・アプリ・ターミナルから Anthropic の基盤でセッションを始めるには、クラウドのセッションの権限を持つロールも要り、Owner に **Organization settings > Roles** でいずれかのロールに加えてもらう、と書き直されました（これまでは「Enterprise の組織がカスタムロールでアクセスを管理するなら」）。前回の changelog の v2.1.310 の追加（Enterprise のカスタムロールに Claude Code のクラウドのセッションと Remote Control の権限を追加）に対応します — [日本語](https://code.claude.com/docs/ja/claude-code-on-the-web) / [English](https://code.claude.com/docs/en/claude-code-on-the-web)
- **セルフホストのクイックスタートに、clone の失敗を直した後の手順が加わった**（`self-hosted-environments-quickstart` の「Set up manually」）。資格情報を用意するか SSH に切り替えた後は、新しいセッションを始めずにランナーを始め直して失敗したセッションを見守ります（何度も失敗していれば、ランナーが `Picked up session` を記録するまで数分待つ）。別のリポジトリを使うなら、失敗したセッションをアーカイブか削除してから、ランナーを始め直して新しいセッションを始めます（でないとランナーが新しいセッションの代わりに失敗したセッションを拾いうる） — [日本語](https://code.claude.com/docs/ja/self-hosted-environments-quickstart#set-up-manually) / [English](https://code.claude.com/docs/en/self-hosted-environments-quickstart#set-up-manually)
- **Remote Control の「Remote Control disconnected」と「Can't reach」の h3 ができた**（`remote-control` のトラブルシューティング）。claude.ai/code かデスクトップアプリのこれらの表示は、ブラウザーかアプリが手元のコンピューターの Claude Code との連絡を失ったことを示し、Claude や見ていたサブエージェントがまだ動いているかは示しません。コンピューターで Claude Code の状態を確かめ、対話的なセッションが `Remote Control disconnected` を出しているならその行の理由ごとのつなぎ直しの手順に従い、失敗を出さずに動いているなら、対話的なセッションはマシンが起きてオンラインになれば自分でつなぎ直し（`claude remote-control` なら「Limitations」の **Extended network outage** を見る）、動いていなければ始め直してセッションを戻します — [日本語](https://code.claude.com/docs/ja/remote-control#troubleshooting) / [English](https://code.claude.com/docs/en/remote-control#troubleshooting)
- **UserPromptSubmit のフックの確認中に `Esc` を押したときの扱いが載った**（`hooks` の新しい h4「`Esc` during a prompt check」）。フックがプロンプトを確かめている間に `Esc` を押すかセッションを中断すると、確認が止まり、プロンプトは Claude に届きません。ターミナルで打った文は入力に戻り、送り直すとフックがまた確かめます。中断と同時にフックがプロンプトを止めたときは止まったままで、そのフックのブロックのメッセージが出て、文は入力に戻りません — [日本語](https://code.claude.com/docs/ja/hooks#userpromptsubmit) / [English](https://code.claude.com/docs/en/hooks#userpromptsubmit)
- **プラグインの WorktreeCreate のフックが `--worktree` と `--tmux` では動かないと載った**（`hooks` の「WorktreeCreate」）。Claude Code はプラグインを読み込む前に worktree を作るので、`--worktree` と `--tmux` で起動したときの worktree ではプラグインの WorktreeCreate のフックは動かず、両方のフラグで動かすにはフックを設定ファイルに定義します。v2.1.300 より前は、`--worktree` だけでもプラグインのフックは動きませんでした — [日本語](https://code.claude.com/docs/ja/hooks#worktreecreate) / [English](https://code.claude.com/docs/en/hooks#worktreecreate)
- **VS Code の TLS を検査するプロキシの節に、ログの警告とリモートのウィンドウの注記が加わった**（`vs-code` の「Dictation or the Web tab fails behind a TLS-inspecting proxy」）。`an authority that Claude Code does not trust` を名指す警告は証明書のエラーを示し、TLS を検査するプロキシの後ろなら `~/.claude/settings.json` の `env` に `NODE_EXTRA_CA_CERTS` を設定します（v2.1.309 より前はこの警告を記録しない）。WSL・SSH のホスト・dev container などにつないだウィンドウでは、証明書のファイルの保存と `~/.claude/settings.json` の編集を、手元のコンピューターではなくその接続先のシステムで行う、という NOTE も加わりました。前回の changelog の v2.1.309 の追加（証明書の検証の失敗を伝えるログの警告）に対応します — [日本語](https://code.claude.com/docs/ja/vs-code#dictation-or-the-web-tab-fails-behind-a-tls-inspecting-proxy) / [English](https://code.claude.com/docs/en/vs-code#dictation-or-the-web-tab-fails-behind-a-tls-inspecting-proxy)
- **Agent SDK の `managedSettings` で渡すフックのキーの扱いが書き直された**（`claude-apps-gateway` の「How hook and skill keys in parent settings take effect」）。前回まとめた「`disableAllHooks: true` は `allowManagedHooksOnly: true` として扱われる」という表の行が外れ、`disableAllHooks: true` で止まるもの（ユーザー・プロジェクト・ローカルのフックと、エージェントのフロントマターか SDK の `settings` のオプションで宣言したフック）と、動き続けるもの（アプリの SDK のフックのコールバックと、管理者の managed settings のフック）の箇条書きになりました。表には、`hooks` のキーも、項目のある `allowedHttpHookUrls`・`httpHookAllowedEnvVars` と同じく無視される（SDK の `settings` のオプションを使う）、と加わっています（`settings-reference` の対応は大幅更新 4 参照） — [日本語](https://code.claude.com/docs/ja/claude-apps-gateway#how-hook-and-skill-keys-in-parent-settings-take-effect) / [English](https://code.claude.com/docs/en/claude-apps-gateway#how-hook-and-skill-keys-in-parent-settings-take-effect)
- **クラウドの環境のセットアップスクリプトの条件が 4 つになった**（`cloud-environments` の「Script requirements」）。スクリプトは、セッションが環境の環境変数を設定する前に動くので、スクリプトが要る値はスクリプトの中で設定する、と加わりました。ネットワークのシークレットの「追加した後は編集できない」という語が外れ、**Add secret** のボタンは管理者の設定では **Add** と表示される、とも加わっています — [日本語](https://code.claude.com/docs/ja/cloud-environments#script-requirements) / [English](https://code.claude.com/docs/en/cloud-environments#script-requirements)
- **プラグインのマーケットプレイスの clone で askpass のプログラムも動かさないと明記された**（`plugins/install`・`plugins/host-marketplace`・`plugins/troubleshooting`）。Claude Code は、git のプロンプトと、`GIT_ASKPASS` で設定したものを含む askpass のプログラムをオフにし、SSH をバッチモードで動かすので、git が資格情報を尋ねる必要があると clone は失敗し、エラーには `fatal: unable to get password from user` も含まれうる、と加わりました。HTTPS の確かめ方も、ターミナルで `GIT_ASKPASS` を外して `git -c core.askPass= ls-remote <url>` を動かす、に改められています — [日本語](https://code.claude.com/docs/ja/plugins/install#add-a-private-marketplace) / [English](https://code.claude.com/docs/en/plugins/install#add-a-private-marketplace)
- **モデルの許可リストで Agent Platform の日付付きの ID の書き方が載った**（`model-config` の「Pin models for third-party deployments」）。Google Cloud の Agent Platform で、Claude Code が求める ID に `claude-sonnet-4-5@20250929` のように `@` の日付が付くなら、許可リストのエントリーにも日付を入れます（`claude-sonnet-4-5` だけでは、`availableModelsMatch` のどちらの設定でも一致しない）。「Merge behavior」の、特定のモデルを名指すエントリーがファミリーのワイルドカードを無効にする例も、`["sonnet", "claude-sonnet-4-5"]` では `claude-sonnet-4-5` が一致するモデルの ID だけを選べる、と言い換えられました — [日本語](https://code.claude.com/docs/ja/model-config#pin-models-for-third-party-deployments) / [English](https://code.claude.com/docs/en/model-config#pin-models-for-third-party-deployments)
- **チャンネルでの権限の確認の返事が効かない原因が 1 つ加わった**（`channels-reference` の「Relay permission prompts」）。遠隔の返事が効かずターミナルのダイアログが開いたままのときの原因に、セッションの前の確認が同じ ID を持っていた場合が加わりました。ID が繰り返されると、一方の確認への返事が他方を承認しないよう、Claude Code はその ID の付いたチャンネルの判定をすべて捨てます。ID はランダムな 5 文字なので繰り返しはまれで、そのときはターミナルで答えます — [日本語](https://code.claude.com/docs/ja/channels-reference#relay-permission-prompts) / [English](https://code.claude.com/docs/en/channels-reference#relay-permission-prompts)
- **差分のパネルがマージなどの途中で表示を保つと載った**（`interactive-mode` の「Diff panel」）。終わっていないマージ・rebase・cherry-pick・revert の間、パネルは最後に git から読んだ変更を出し続け、操作が取り込む変更で埋まりません。操作が終わった後の最初の更新（Claude が次にファイルを編集したときなど）で更新されます — [日本語](https://code.claude.com/docs/ja/interactive-mode#diff-panel) / [English](https://code.claude.com/docs/en/interactive-mode#diff-panel)
- **WebSocket の MCP サーバーの最初の接続の試し直し方が載った**（`mcp` の「Automatic reconnection」）。対話的なターミナルのセッションでは、`/mcp` のサーバーのメニューの **Reconnect** で試し直します。`/mcp reconnect all` の説明も、対話的なターミナルのセッションの Claude Code のプロンプトで動かす（v2.1.284 以降）、と言い換えられました — [日本語](https://code.claude.com/docs/ja/mcp#automatic-reconnection) / [English](https://code.claude.com/docs/en/mcp#automatic-reconnection)
- **Code Review のプッシュの後のレビューが省いた指摘の数の読み方が分けて書かれた**（`code-review-pull-requests`・`code-review-troubleshooting`・`code-review`）。前回のレビューから変わっていないコードへの指摘は「outside the scope of this re-review and not posted」、nit と既存の指摘は「found and not posted」で終わる文で数えられます。`code-review-troubleshooting` の **Code review found no issues** の行は、最初のレビューでなければレビューの本文の省いた指摘の数を見る、と改められ、`code-review` の「何も見つからないとき」の項目は「指摘の代わりの注記」（チェックランの題が **Code review found no issues** のときに投稿される）に言い換えられています — [日本語](https://code.claude.com/docs/ja/code-review-pull-requests#what-a-later-review-covers) / [English](https://code.claude.com/docs/en/code-review-pull-requests#what-a-later-review-covers)
- **ターミナルのタブの題の状態のグリフの扱いが載った**（`terminal-config` の「See session status in your terminal」）。プロトコルへの対応を報告するターミナルでは、ターミナル自身がセッションの状態を示すので、Claude Code はほかのターミナルで題の前に付けるグリフを付けません — [日本語](https://code.claude.com/docs/ja/terminal-config#see-session-status-in-your-terminal) / [English](https://code.claude.com/docs/en/terminal-config#see-session-status-in-your-terminal)
- **ファイルを見た Bash のコマンドの後の編集の条件が言い換えられた**（`tools-reference` の「Edit tool behavior」）。`cat` や `grep` などでファイルを見た後は別の Read なしに編集できますが、コマンドがファイルの文を何も出さなかったとき（検索が何にも一致しないときなど）は、編集の前に読むチェックがかかる、と改められました（これまでは「一致を出さない検索とこの一覧の外のコマンドは読み取りに数えない」） — [日本語](https://code.claude.com/docs/ja/tools-reference#edit-tool-behavior) / [English](https://code.claude.com/docs/en/tools-reference#edit-tool-behavior)
- **複数の PreToolUse のフックが入力を書き換えるときの説明が改められた**（`hooks-guide` の「Limitations」）。「最後に終わったものが効き、フックは並列に動くので順序は決まらない」が、Claude Code は書き換えをまとめず、どの書き換えでツールが動くかも保証しない、に改められました — [日本語](https://code.claude.com/docs/ja/hooks-guide#limitations) / [English](https://code.claude.com/docs/en/hooks-guide#limitations)

**バグ修正**

- **Windows で引用符付きの文字列だけのフックのコマンドの直し方が載った**（`hooks` の新しい h4「PowerShell started no program」）。Git Bash がなく、`"command": "\"C:\\Tools\\guard.exe\""` のように引用符付きの文字列だけの `command` を持つフックは PowerShell で動き、PowerShell はそれを実行せずに出力します。直し方は、JSON などの文を出したいなら `"shell": "powershell"` にする（フックは 0 で終わる）、`.ps1`・`.cmd`・`.bat` か、パスに変数のある `.exe` を動かすなら `"shell": "powershell"` にして引用符付きのパスの前に `&` を置く（`$HOME` はそのまま、環境変数は `$env:CLAUDE_PROJECT_DIR` の形で書く）、`$` のないパスの `.exe` 1 つなら内側の引用符を外して exec 形式にする（引数がなければ `"args": []`）、Bash 向けのスクリプトなら Bash 向けの直し方に従う、です。「Failed hooks on Windows without Git Bash」も、エラーに `PowerShell started no program` もあればこの h4 から始める、と加わって組み直され（Git Bash がなければ 0 か 2 以外の終了コードは、拒否しない JSON を出しても失敗に数える、という既存の文は対処の一覧の前に移った）、既存の PowerShell のフックでパスを参照する段落に h3「Reference scripts by path in PowerShell hooks」の見出しが付きました。前回の changelog の v2.1.310 の修正（Git Bash がなく、フックのコマンドが引用符付きの文字列だけのとき、PreToolUse と PermissionRequest のフックがツールの呼び出しを通す問題）に対応します — [日本語](https://code.claude.com/docs/ja/hooks#powershell-started-no-program) / [English](https://code.claude.com/docs/en/hooks#powershell-started-no-program)
- **ゲートウェイが effort のベータの値を断ったときの再試行が載った**（`llm-gateway-protocol` の「Automatic retry and error forwarding」）。上流が `output_config.effort` かその `anthropic-beta` の値を断ると、Claude Code は再試行し、終了するまでそのモデルの要求にどちらも加えません。ゲートウェイが上流の `400` を手を加えずに返し、メッセージが `output_config.effort` と `Extra inputs are not permitted` を名指すか、モデルが effort のパラメーターに対応しないと言うか、`Unexpected value(s)` で始まり `anthropic-beta` のヘッダーについて `effort-2025-11-24` を挙げる（v2.1.310 以降）なら、ゲートウェイの変更は要りません。`ANTHROPIC_BETAS` にその値を入れている開発者は送り続けて `400` を受けるので、その項目を外してもらいます。前回の changelog の v2.1.310 の修正（`effort-2025-11-24` のベータの値を断る一部のゲートウェイや互換サーバーの後ろで要求が失敗する問題）に対応します — [日本語](https://code.claude.com/docs/ja/llm-gateway-protocol#automatic-retry-and-error-forwarding) / [English](https://code.claude.com/docs/en/llm-gateway-protocol#automatic-retry-and-error-forwarding)
- ゲートウェイの後ろで「Waiting for API response」のバナーが出たり消えたりする問題の修正（前回の changelog の v2.1.309）の説明（`errors`。詳細は大幅更新 6 参照）
- セルフホストのランナーの `--startup-timeout-min` が、最初のプロンプトがまだサブエージェントで動いているセッションを止める問題の修正（前回の changelog の v2.1.309）の説明（`self-hosted-environments-reference`。詳細は大幅更新 3 参照）

**その他**

- **`claude ultrareview` の終了コード 1 に、信頼の質問で Enter を押した場合が加わった**（`ultrareview`）。信頼していない PR を `--trust-workspace` でレビューする説明からは、「`y` と違ってフラグは何も保存しない」という文が外れました
- **`jetbrains` から、プラグインのない IDE を検出すると `/ide` がプラグインを入れて IDE の再起動を求める、という文が外れた**
- **Claude Docs のコネクターをオフにする案内が短くなった**（`artifacts`・`mcp`）。`deniedMcpServers` と `/mcp` のトグルの名指しが外れ、このコネクターだけをオフにするには「Disable claude.ai connectors」を見る、という文になりました
- **言い回しの調整**: `checkpointing`（**No code restore** の印の付いたメッセージの説明が縮められ、それを選ぶと **Restore conversation** が出るという文が外れた）、`desktop`（セッションの詳細のパネルを出す **⋮** のメニューの「ウィンドウが狭いとき」が外れ、`export` した変数の案内が言い換えられ、自分の手順を持つ変数の例に `API_TIMEOUT_MS` が加わった）、`large-codebases`（「API 向けのツールがフロントエンドの作業でコンテキストを使わない」「どちらのディレクトリのスキルも他方の作業では読み込まれない」が外れた）、`permission-modes`（claude.ai/code のモードのドロップダウンは「プロンプトの箱の横」から「プロンプトの箱の下の行」に）、`self-hosted-environments`（オンデマンドのランナーは仕事が終わると自分で終わる、という語が外れた）、`hooks`（Setup と CwdChanged の `CLAUDE_ENV_FILE` の文）、`keybindings`（vim モードとの関係の文）、`plugins/mods/troubleshoot`、`env-vars`（`CLAUDE_CODE_FORCE_TERMINAL_IMAGES` のリンクの文）
- **見出しマップ**: 47 行が加わり 1 行が外れました。加わったのは 46 見出しと新しいスタンプ、外れたのは古いスタンプです。46 見出しはすべて今回 `llms-full.txt` にも入った見出しです。`llms-full.txt` に加わった 47 見出しは、この 46 と、前回のサマリで見出しマップにだけ載っていた「MCP tool call timed out with the server's question unanswered」（`errors` の「Tool errors」の下）を合わせた数です
- **見出しマップ冒頭の自動生成スタンプが、2026年10月24日 03時07分20秒 UTC から 2026年10月24日 23時26分27秒 UTC へ進みました**

**参考リンクについて**: 日本語版は、ハイライト・大幅更新・軽微な更新で扱った 36 ページを取得し、該当する節があるかと今回の内容になっているかを、計 74 項目について確かめました（長いページは節を指定して読み、`hooks`・`monitoring-usage`・`mcp` の一部の項目は取得のツールの要約の引用で確かめています）。今回は 74 項目すべてで日本語版がすでに今回の内容になっていたので、すべての参考リンクに日本語版を併記しています。日本語版の `errors` は新しい 3 つの h3 の見出しを、`fast-mode` は 3 つの h4 の見出しを、`claude-code-on-the-web` と `remote-control` は新しいトラブルシューティングの h3 の見出しを英語のまま載せています。アポストロフィや引用符を含む新しい見出し（`claude-code-on-the-web` と `remote-control` のトラブルシューティングの h3）とコード片を含む新しい見出し（`hooks` の「`Esc` during a prompt check」）は id を確かめられないため、上位の節へのリンクにしました。カスタムロールの注記はページの冒頭にあり見出しがないため、アンカーなしのページへのリンクにしています。今回 changelog は変わっていないので、changelog だけに載っている項目はありません。**changelog ページへのリンクは、本サマリの方針どおり付けていません。**
<!-- light:minor-updates:end -->

## 新着情報

<!-- light:whats-new:start -->
**今回、新着情報（`whats-new/`）のページに変更はありません**（最新の週のダイジェストは前回と同じ Week 37 です）。
<!-- light:whats-new:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-10-23.md](./archives/latest/2026-10-23.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-10-23.md](./archives/latest-detail/2026-10-23.md)

<!--
base_commit: 5536db396725852afccd11c0a05e205b631b83fa
head_commit: 6b976faced99af3504551c0ea61a17476913b249
generated_at_full: 2026-10-25T15:20:22+09:00
-->
