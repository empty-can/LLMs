---
対象期間: 2026年10月29日 〜 2026年10月30日
作成日: 2026-10-30
---

# Claude Code 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
**今回は changelog に v2.1.316（2026年10月31日）の 1 リリースが積まれ（v2.1.315 の項目はありません）、通常のページには、Max 20x の新しい名前の Ultra のプランが 50 ページにわたって書き加えられ、Claude Desktop のコマンドから作る SSH 接続で前のマシンを残したまま新しいマシンを作れるようになったことが載りました。`llms-full.txt` では、タブ・アコーディオン・カードが印付きの引用として出るようになっています**。新しいページはなく、228 ページ中 92 ページ（changelog を含む）に差分がありますが、そのうち 41 ページは書式の書き換えだけで、内容が変わったのは 51 ページ（changelog を含む）です。大幅更新は `desktop` の 1 ページです。見出しマップに加わった 5 の見出しは、すべて `llms-full.txt` にも入っています。総行数は 126,302 行から 126,426 行に増えました。

主要なものを以下に挙げます。

1. Max 20x の新しい名前として Ultra のプランが `feature-availability` に載り（Max は Max 5x の新しい名前で、Claude Code での機能は Max と同じ）、50 ページでプランを並べた箇所に Ultra が加わった
2. Claude Desktop のコマンドから作る SSH 接続で、「Replace the host」が「Create another machine」になって前のマシンのセッションが動き続けるようになり（Claude Desktop v4.4212.0 以降）、マシンを使うのをやめる手順とエントリを外したときの扱いの節もできた
3. `llms-full.txt` で、タブ・アコーディオン・カードが `> [tab]`・`> [accordion]`・`> [card]` の行で始まる引用のブロックになり、生の差分の大半と 41 ページの変更はこの書き換えだけだった
4. changelog の v2.1.316 で、Opus 4.8 の fast mode が非推奨になり（2026年11月30日に外される）、`CLAUDE_CODE_SUBAGENT_EFFORT` と `CLAUDE_CODE_DISABLE_ULTRATHINK` が加わった
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**Max 20x の新しい名前の Ultra プランが 50 ページに書き加えられた**](#1-max-20x-の新しい名前の-ultra-プランが-50-ページに書き加えられた):  
  `feature-availability` に h3「Ultra plan」ができ、Ultra は Max 20x の新しい名前で、Max は Max 5x の新しい名前、Claude Code では Max と Ultra の機能は同じ、と載りました。プラン別の表にも Ultra の列が加わり、ほかの 49 ページでも「Pro and Max」のようにプランを並べた箇所に Ultra が加わっています
2. [**Claude Desktop のコマンドから作る SSH 接続で前のマシンを残したまま新しいマシンを作れるようになった**](#2-claude-desktop-のコマンドから作る-ssh-接続で前のマシンを残したまま新しいマシンを作れるようになった):  
  `desktop` の h5「Replace the host」が外れて h5「Create another machine」になり、**Create another Dev box** を選んでも前のマシンのセッションは動き続ける（Claude Desktop v4.4212.0 より前は置き換え）と載りました。Desktop が自分で接続しないよう前のマシンを使うのをやめる h5 と、エントリを外したときの h5 もできています
3. [**llms-full.txt でタブとアコーディオンとカードが印付きの引用として出るようになった**](#3-llms-fulltxt-でタブとアコーディオンとカードが印付きの引用として出るようになった):  
  これまで太字の行で出ていたタブの名前・アコーディオンの題・カードが、`> [tab] …`・`> [accordion] …`・`> [card] …` の行で始まる引用のブロックになり、中身も引用の中に入りました。59 ページに及び、差分のあった 92 ページのうち 41 ページはこの書き換えだけです
4. [**changelog の v2.1.316 で Opus 4.8 の fast mode が非推奨になりサブエージェントの effort の環境変数が加わった**](#4-changelog-の-v21316-で-opus-48-の-fast-mode-が非推奨になりサブエージェントの-effort-の環境変数が加わった):  
  Opus 4.8 の fast mode は 2026年10月30日に非推奨になり、2026年11月30日に外されて、その後は通常の Opus 4.8 にフォールバックせずエラーを返します。サブエージェントの effort を決める `CLAUDE_CODE_SUBAGENT_EFFORT` と、`ultrathink` をオフにする `CLAUDE_CODE_DISABLE_ULTRATHINK` も加わりました。いずれも通常のページにはまだ載っていません
<!-- light:highlight-list:end -->

## 1. Max 20x の新しい名前の Ultra プランが 50 ページに書き加えられた

**`feature-availability` の「Availability by subscription plan」に h3「Ultra plan」ができました。** Ultra は Max 20x のプランの新しい名前で、Max は Max 5x の新しい名前です。どのプランかは claude.ai のサブスクリプションで確かめます。Claude Code では Max と Ultra の機能は同じで、プラン別の利用できる機能の表の Max と Ultra の列に載ります。使用量の上限と価格は、Claude の料金のページを見ます。表には Max の列の次に Ultra の列が加わり、15 の機能のどれも Max の列と同じ値です。同じページの「Claude subscription」の説明と、Claude Code in Slack・computer use・artifacts のプランの注記にも Ultra が加わりました。

ほかのページでも、「Pro and Max」「Pro or Max」「Pro, Max, Team, or Enterprise」のようにプランを並べた箇所に Ultra が加わり、Ultra の語は前回の 0 か所から 50 ページの 144 か所になりました（changelog と whats-new の過去の記述は前のまま）。主なものは次のとおりです。

- **`ultrareview`**: 「Pricing and free runs」の表に Ultra の行（無料の 3 回、その後は使用量クレジットとして課金）が加わり、無料の 3 回は Pro・Max・Ultra の、アカウントごとに 1 回限りの割り当てになった
- **`claude-code-on-the-web`**: 共有の h4 が「Share from a Max, Ultra, or Pro account」に改められ、その前置きの文（Max と Pro のアカウントでは共有は次のように働く）が外れた
- **`model-config`**: Opus 4.6 の 1M コンテキストがサブスクリプションに含まれるプランの文と表が「Max, Ultra, Team, and Enterprise」になり、Sonnet 4.6 の 1M コンテキストは Max と Ultra を含むどのサブスクリプションのプランでも使用量クレジットが要る、となった
- **`slack`**: 以前の Claude Code in Slack が答えるのは Pro・Max・Ultra のアカウントからのメンションだけ、と改められ、`llms.txt` の 1 行説明も「channel mentions」が「mentions」になって同じ書き方になった
- **そのほか**: computer use・Dispatch・Remote Control・クラウドのセッション・スケジュールしたタスク・artifacts・`/usage` の内訳・使用量クレジット・fast mode・`/restart`・`/privacy-settings`・データの利用（Free・Pro・Max・Ultra の消費者向けのユーザー）などのプランの条件に Ultra が並んだ

`costs` の「Add usage credits to your subscription」の 1 か所（Pro と Max のプランでは、使用量クレジットが残っているうちに使用の上限に達すると、CLI を離れずに上限を上げるか外すよう Claude Code が促す、という段落）は「Pro and Max plans」のままです。changelog に対応する項目はありません。

- [機能の利用可能性 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/feature-availability#ultra-plan)
- [Feature availability - Claude Code Docs (English)](https://code.claude.com/docs/en/feature-availability#ultra-plan)
- [ultrareview でバグを見つける - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/ultrareview#pricing-and-free-runs)
- [Find bugs with ultrareview - Claude Code Docs (English)](https://code.claude.com/docs/en/ultrareview#pricing-and-free-runs)

## 2. Claude Desktop のコマンドから作る SSH 接続で前のマシンを残したまま新しいマシンを作れるようになった

**`desktop` の「Create an SSH connection from a command」で、h5「Replace the host」が外れ、h5「Create another machine」「Stop using a machine」「Remove an entry」ができました。** `sshHostCommands` のエントリのコマンドでマシンを作る接続（Claude Desktop v3.6556.0 以降）の説明です。これまでは、各エントリは 1 つの接続で一度に 1 台のホストを持ち、**Create Dev box** は一度ホストを持つと **Replace Dev box's host** になり、置き換えると前のホストのセッションは前のホストに残って、Desktop はそのホストを加え直さない限り接続しない、という書き方でした。今は、各エントリは 1 つの接続で、エントリのコマンドから Desktop が最後に保存したホストを指す、となっています。

- **Create another machine**: **Create another Dev box** を選んだ後も前のマシンのセッションは動き続け、新しいセッションは新しいマシンを使う。環境のセレクターでこの項目を選ぶと、新しいマシンを作るか、なくなったマシンを置き換えられる（新しいセッションのページで、Desktop がホストに届かないと告げるメッセージからも選べる）。前のマシンのセッションは、セレクターが今のマシンしか載せないのでサイドバーから続ける。Desktop は起動時などに前のマシンにも自分で接続しうるので、使い終えたら次の h5 の手順でやめる。Claude Desktop v4.4212.0 より前は **Replace Dev box's host** と出て、置き換えたホストには接続しなくなる（そのホストのセッションを続けるには、セッションを開いて **Add SSH connection** を選び、Desktop が埋めた接続を保存する。別のホストを置き換える前に Desktop を更新する）。2 台で新しいセッションを動かすには `sshHostCommands` に 2 つ目のエントリを加え、新しいホストがまだ応答しないなら新しいセッションのページを最大 10 分開いたままにする（それでも応答しなければ、ページのメッセージの **Create another Dev box** を選ぶ）。1 時間のうちに何度かコマンドを動かした後は、さらに動かすたびに、コマンドを示すダイアログで確かめる
- **Stop using a machine**: コマンドが作ったマシンに Desktop が自分で接続しないようにするには、そのマシンのすべてのセッションをアーカイブする。手順は 6 つで、サイドバーでマシンのセッションを探し（セッションの詳細のパネルが動いているホストを示す）、それぞれアーカイブしたままにし、同じエントリから別のマシンを作っていなければ別のマシンを作るかエントリを外し（それまでは、そのマシンはエントリの保存された接続で、その接続を選んで新しいセッションのページを開くと Desktop が接続しうる）、アプリのほかの SSH 接続か `sshConfigs` のエントリも消し、Desktop を終了して開き直し（マシンへの接続を閉じて、届こうとするのを終わらせる）、最後にツールでマシンを消す
- **Remove an entry**: 設定ファイルからエントリを外すか `id` を変えても、そのマシンのセッションは残るので、Desktop はそのマシンに接続できる。誰もいなくても、セッションの動いているプロセスに入り直すときや送信待ちのメッセージを届けるときに接続しうるので、止めるには「Stop using a machine」のとおりセッションをアーカイブする。管理者が managed のエントリを外した場合もユーザーのセッションは残り、各ユーザーが自分のものをアーカイブする。管理者が自分でそのマシンを止めるには、ユーザーがまだ要るホストに一致し、マシンのホスト名には一致しない `sshHostAllowlist` を設定する（パターンで両者を見分けられる場合だけ）

「Connect to a new host」にも、名前の再利用は誰もいないときにも問題になる、という段落が加わりました。Desktop はこれらのホストに自分で接続するためで（たとえば、ホストに届かなかった間に送ったメッセージを、ホストが応答したときに届ける）、host key checking がオンでも次の場合はメッセージがその名前の新しいマシンに届きうるので、マシンを消す前に使うのをやめます。

- 自分かコマンドかほかのプログラムが、新しい鍵を `known_hosts` に加えたか古い鍵の行を消した（ホストの鍵を加えるコマンドならそうなる）
- ツールのマシンがホストの鍵を共有している
- ツールのマシンが、`known_hosts` が信頼する認証局を共有している
- 自分か管理者が `KnownHostsCommand` か `VerifyHostKeyDNS yes` を設定していて、SSH が `known_hosts` の外の鍵を受け付ける

ほかにも、Desktop はマシンを止めも消しもしないという警告の一覧の「置き換えたホスト」は「別のマシンを作る前にエントリが指していたマシン」に、フィールドの表の `id` の行は、変えると接続はホストなしでやり直し、そのマシンは動き続け、Desktop はそれらに接続できる、に改められました。「If a command is missing or gray」では、**Create another** は Desktop がホストを保存してから 1 分グレーになる（Claude Desktop v4.4212.0 より前は **Replace Dev box's host** が 10 分グレー）となり、これまでの「ホストは 10 分経てば置き換えられる」が改められています。**Create** か **Replace** の項目、という言い方も **Create** か **Create another** の項目、になりました。changelog に対応する項目はありません。

- [デスクトップアプリケーション - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/desktop#create-another-machine)
- [Desktop application - Claude Code Docs (English)](https://code.claude.com/docs/en/desktop#create-another-machine)
- [デスクトップアプリケーション - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/desktop#stop-using-a-machine)
- [Desktop application - Claude Code Docs (English)](https://code.claude.com/docs/en/desktop#stop-using-a-machine)

## 3. llms-full.txt でタブとアコーディオンとカードが印付きの引用として出るようになった

**`llms-full.txt` で、タブ・アコーディオン・カードの書き方が変わりました。** これまでは、タブの名前とアコーディオンの題は `**macOS/Linux**` のような太字の行で、その中身は印のない地の文として続き、番号付きの手順の `**1. ...**` などの太字の行と見分けられませんでした。カードは `**[Download for macOS](...)**` のような太字のリンクの行でした。今回からは、それぞれ `> [tab] macOS/Linux`・`> [accordion] Anthropic services`・`> [card] [Download for macOS](...)` の行で始まる引用のブロックになり、中身の行もすべて `> ` 付きで続きます（中のコールアウトは `> > [!NOTE]` のような二重の引用になる）。リストの項目の中のタブは、項目の字下げの後ろに `> ` が付きます。

- **数**: ファイル全体で `[tab]` が 270 行・`[accordion]` が 60 行・`[card]` が 31 行あり、固有のページでは 59 ページです（`[tab]` が 46 ページ・`[accordion]` が 15 ページ・`[card]` が 7 ページ。2 回展開されている `plugins/install` は両方の写しが変わり、変わった後も 2 つは同じ）
- **差分への影響**: `llms-full.txt` の生の差分の追加 4,722 行・削除 4,598 行のほとんどはこの書き換えで、差分のあった 92 ページのうち 41 ページはこの書き換えだけです（一覧は「軽微な更新」の「その他」）。書き換えを戻して数えると、内容が変わったのは 51 ページ（changelog を含む）・追加 264 行・削除 167 行です（空行を除く。方法は大幅更新の後の注記）
- **見出しの数への影響**: `gitlab-ci-cd` の「Prerequisites」「Setup instructions」の 2 組の h3 がタブの引用の中に入ったので、行頭が `#` の見出しだけを数えると 4 つ減って見えます（見出しそのものは変わっていない）
- **`setup` のコードブロック**: 前回 29 回に重なった「Install Claude Code」の 5 つのコードブロックの開始行の `theme={null}` は、1 回に戻りました

この 41 ページでは、文・表・コードの中身は変わっていません。changelog に対応する項目はありません。

## 4. changelog の v2.1.316 で Opus 4.8 の fast mode が非推奨になりサブエージェントの effort の環境変数が加わった

**changelog に v2.1.316（2026年10月31日）が加わりました**（v2.1.314 の次で、v2.1.315 の項目はありません）。55 項目のうち、次の 3 つを挙げます。いずれも通常のページにはまだ載っておらず、changelog でしか確かめられません。

- **Opus 4.8 の fast mode の非推奨**: 2026年10月30日に非推奨になり、2026年11月30日に外される。外された後は、Opus 4.8 での fast mode の要求はエラーを返し、通常の Opus 4.8 にはフォールバックしない。速さを保つには Opus 5.5 に移る。`fast-mode` のページは今回 Ultra が加わっただけで、料金（Opus 5 と Opus 4.8 は入力・出力 100 万トークンあたり 10 ドル／50 ドル）や、Console の組織が Opus 5 か Opus 4.8 で使うにはアクセスの用意が要るという記述はそのままです
- **`CLAUDE_CODE_SUBAGENT_EFFORT`**: ほかに何も effort のレベルを名指さないとき、サブエージェントが動く effort のレベルを、セッションのものを継承する代わりに設定する
- **`CLAUDE_CODE_DISABLE_ULTRATHINK`**: `ultrathink` のキーワードをオフにする

ほかの項目は「軽微な更新」で分類して挙げています。

## 新規追加されたページ

<!-- light:new-pages:start -->
（今回の対象期間に新規追加・削除されたドキュメントページはありません。`llms.txt` の URL は 275 のままで、`slack` の 1 行説明だけが変わりました。`llms-full.txt` に展開されている固有のページも 228 のままで、`Source:` の行が 231 あり 3 ページが 2 回展開されている状態も前回と同じです）
<!-- light:new-pages:end -->

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
- [**Desktop application**](#1-desktop-application) ([日本語](https://code.claude.com/docs/ja/desktop#create-another-machine) / [English](https://code.claude.com/docs/en/desktop#create-another-machine)):  
  書式の書き換えを戻して数えると 59 行（追加 40・削除 19）が変わりました。ハイライト 2 の SSH 接続の節のほか、`forceLoginOrgUUID` の警告の囲みと、Dispatch の要件の箇条書き化、7 か所の Ultra の追記があります
<!-- light:updated-pages:end -->

**行数の数え方**: 今回の生の差分はハイライト 3 の書き換えで膨らんでいます（`llms-full.txt` の追加 4,722 行・削除 4,598 行。差分のハンクを head 側の `Source:` 行でページに振り分けた合計は生の差分と一致し、`desktop` は追加 116 行・削除 86 行）。そのため、`llms-full.txt` をページ単位に切り出し、base と head の両方に同じ正規化をかけてから比べました。正規化は、①行頭の字下げの後ろの引用の印 `> ` を外す、②`[tab]`・`[accordion]`・`[card]` の行をこれまでの太字の行（`**名前**`）に戻す、③コードブロックの開始行で重なった ` theme={null}` を 1 つにする、④空行を除く、の 4 つで、比較は Python の difflib（`autojunk=False`）です。この方法で 50 行以上のページを挙げました。changelog（追加 61 行。空行を含めると 71 行）は新しい 1 リリースの分なので大幅更新には入れず、「軽微な更新」で扱っています。次点は `feature-availability` の 45 行（追加 24・削除 21。ハイライト 1）、`permission-modes` の 18 行（追加 11・削除 7）、`costs` の 18 行（追加 9・削除 9）です。

## 1. Desktop application

ページの差分のうち、SSH 接続の節はハイライト 2 のとおりで、プランの並びへの Ultra の追記（7 か所）はハイライト 1 のとおりです。そのほかは次のとおりです。

- **`forceLoginOrgUUID` の警告**（「Restrict sign-in to your organization」）: 前回加わった h4 に警告の囲みが加わりました。デプロイする前に `forceLoginOrgUUID` の値を確かめます。その ID が自分の組織のものでないと、組織の人は、その ID の組織にも属していない限り Claude Desktop を使えません。戻すには、正しい ID を配って Claude Desktop を再起動してもらいます
- **「Set up Dispatch」**: 1 段落が 2 項目の箇条書きになりました（Plans: Dispatch は Pro・Max・Ultra のプランが要り、Team と Enterprise のプランでは使えない／Setup, pairing, and Dispatch settings: Dispatch のヘルプの記事を見る）
- **書式**: 冒頭のダウンロードの 3 つのカード（macOS・Windows・Linux）と、2 つのアコーディオン（「When edits in a worktree keep working」と「If a jump host asks for a sign-in, the outage is long, output is missing, or the process is gone」）が、ハイライト 3 の書き方になりました（行数には数えていない）

- [デスクトップアプリケーション - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/desktop#restrict-sign-in-to-your-organization)
- [Desktop application - Claude Code Docs (English)](https://code.claude.com/docs/en/desktop#restrict-sign-in-to-your-organization)

## 軽微な更新

<!-- light:minor-updates:start -->
今回の差分は **3 ファイル**（`llms-full.txt`・`llms.txt`・見出しマップ）です。`llms.txt` は `slack` の 1 行説明だけが変わり（ハイライト 1）、URL は 275 のままです。`llms-full.txt` の生の差分は追加 4,722 行・削除 4,598 行で、ページの並びは変わっていません。228 ページ中 92 ページ（changelog を含む）に差分があり、41 ページはハイライト 3 の書式の書き換えだけ、51 ページ（changelog を含む）は内容が変わりました。大幅更新の 1 ページを除く **49 ページ**と、changelog に加わった **v2.1.316（2026年10月31日）**、書式の書き換えだけの 41 ページを以下にまとめます。

`llms-full.txt` の総行数は **126,302 行から 126,426 行へ 124 行増え**ました（生の差分の差し引き 4,722 − 4,598 と一致）。`Source:` の行は 231、固有のページは 228 のままで、2 回展開されている 3 ページ（`plugins/create`・`plugins/install`・`plugins/mods/overview`）も前回と同じです。コードフェンスの外の見出しは、引用の中の見出しも数えると 6,003 から 6,006 へ 3 増えました（加わった 5・外れた 2）。前回の 5,996 は行頭が `#` の見出しだけを数えた値で、その数え方では今回は 5,995 になります（ハイライト 3 のとおり、`gitlab-ci-cd` の 4 つの h3 が引用の中に入ったため）。changelog の収録リリースは 433 から 434 になりました。v2.1.316 は 55 項目（追加 10・変更 6・改善 5・バグ修正 34）で、単一のリリースなので各項目への版の併記は省いています。v2.1.316 の項目には今回の通常のページの変更に対応するものはなく、2 項目は既存のページに記述があります（その項目にリンクを付けています）。

**新機能**

- Max 20x の新しい名前の Ultra のプラン（`feature-availability` の h3「Ultra plan」と表の列。プランを並べた箇所への追記は `agents`・`artifacts`・`authentication`・`auto-mode-classifier-billing`・`auto-mode-config`・`best-practices`・`channels`・`chrome`・`claude-code-on-the-web`・`claude-projects`・`claude-tag`・`cloud-environments`・`commands`・`computer-use`・`costs`・`data-usage`・`desktop`・`desktop-ios-simulator`・`desktop-quickstart`・`env-vars`・`errors`・`fast-mode`・`feature-availability`・`github-actions`・`glossary`・`how-claude-code-works`・`jetbrains`・`legal-and-compliance`・`mobile`・`model-config`・`permission-modes`・`platforms`・`plugins/measure`・`plugins/publish`・`quickstart`・`remote-control`・`routines`・`security`・`self-hosted-environments`・`sessions`・`settings-reference`・`setup`・`skills`・`slack`・`statusline`・`tools-reference`・`troubleshoot-install`・`ultrareview`・`vs-code`・`web-quickstart` の 50 ページ。詳細はハイライト 1 参照）
- Claude Desktop のコマンドから作る SSH 接続の「Create another machine」「Stop using a machine」「Remove an entry」（`desktop`。詳細はハイライト 2 参照）
- `CLAUDE_CODE_DISABLE_ULTRATHINK` を追加（詳細はハイライト 4 参照）
- `CLAUDE_CODE_SUBAGENT_EFFORT` を追加（詳細はハイライト 4 参照）
- Claude apps gateway に、グループで共有する予算を追加。グループのメンバーが共有する月の予算 1 つを、各メンバー自身の上限に加えて設けられ、spend limits の管理者 API の `pooled_budget` で設定します
- `CLAUDE_CODE_DISABLE_LOOPED_CROSS_CERT_DROP` を追加。互いに認証し合うループになったシステムのクロス証明書を残します。プライベートの CA がそれを要するサーバー向けです
- Claude apps gateway に `managed.policy_mode: layered` を追加。開発者に一致する最初のポリシーだけでなく、一致するすべてのポリシーが、それぞれ下に並ぶものの上にマージされて適用されます
- Claude apps gateway の Bedrock の上流に `guardrail.input_tagging` を追加。Amazon Bedrock のガードレールの prompt attacks のフィルターが要る入力のタグでプロンプトを包み、`all_messages_and_system` ならシステムプロンプトにも付けます
- [VSCode] チャットパネルから、ターミナルなしで Claude apps gateway にサインインできるようにしました
- [Cloud sessions] クラウドのセッションにフォームのカードを追加。MCP サーバーが求めるフォームに、要求が見えないまま取り消されるのではなく、記入するか断れます
- [Cloud sessions] 「Catching up…」の行を追加。切り替えて戻ったクラウドか Remote Control のセッションが、まだメッセージを最新にしている間に出ます
- [Code Review] Code Review の分析のページに、重大度ごとの指摘のカードを追加。期間の指摘の合計、重大度で積み上げた日次のグラフ、重大度ごとの数を示します（`code-review-costs` の「View usage」の表には「Code Review findings」の行が前回から載っています） — [日本語](https://code.claude.com/docs/ja/code-review-costs#view-usage) / [English](https://code.claude.com/docs/en/code-review-costs#view-usage)

**機能改善**

- Opus 4.8 の fast mode を非推奨に変更（詳細はハイライト 4 参照）
- `"$defaults"` のない `autoMode.allow` の一覧が、スケジュールしたタスクのプロンプトについての組み込みのルールを外さないよう変更
- Team と Enterprise のログインの server-managed settings を変更。Anthropic の API から取得した設定は承認の確認なしに適用され、検証できない保存済みのコピーは拒まれます
- [VSCode] `ultrathink` が、ターミナルと同じく、そのターンを `xhigh` の effort で動かし、チャットボックスで虹色に表示されるよう変更
- [Cloud sessions] Enterprise のメンバーが、見るだけでなく、自分のクラウドの環境で network secrets を追加・削除できるよう変更（`cloud-environments` の「Requirements」には、どのプランでも自分の環境ではロールにかかわらず追加・削除できる、と前から載っています） — [日本語](https://code.claude.com/docs/ja/cloud-environments#requirements) / [English](https://code.claude.com/docs/en/cloud-environments#requirements)
- [Claude Tag] Slack のチャンネルの Respond automatically のスイッチを、チャンネルの Configure のページと Claude Tag の管理者の設定での「How Claude participates」の選択に変更
- Claude Desktop の Code タブか Web から始めた `/code-review` を改善。クラウドと `claude remote-control` のセッションでも、ただの文の一覧ではなく指摘のカードを示します
- 大きなリポジトリでの `/diff` を改善。更新のたびにリポジトリ全体の git のコマンドが通常 1 つ減り、git が遅いと更新の間隔を空けます
- `/ultrareview`・クラウドのセッション・クラウドのエージェントが GitHub のリモートを見つけられないときのメッセージを改善。https://github.com/new でリポジトリを作るよう示し、`/ultrareview` は `gh` が拒む `gh` のコマンドを勧めなくなりました
- SSL の証明書のエラーを改善。中間証明書を送らないサーバーなど、考えられる原因とそれぞれの直し方を示します
- [Cloud sessions] クラウドのセッションの Changes のペインを改善。一覧が省くものについての注記が、差分の上の行ではなく、ブランチ名の横のバッジになりました

**バグ修正**

- Claude Code が自分で終了したとき（資格情報が拒まれたときや、クラウドのセッションがアーカイブされたときなど）、macOS と Linux でシェルのコマンドが動いたまま残る問題を修正
- 値に改行のある bash のエイリアス（Git Bash を除く）と、名前がダッシュで始まる関数が、Bash ツールのシェルで崩れるか失われる問題を修正
- `SHELLOPTS` が export されていると、Bash ツールから始めた bash のスクリプトが最初のコマンドの後で止まる問題を修正
- コマンドが型のキャスト・`param`・`using`・属性で始まると、PowerShell のフックが終了コード 2 で止めない問題を修正
- 圧縮された応答が途中で切れるか壊れていると、一部のネットワークの要求が止まったままになる問題を修正
- Vertex AI と Amazon Bedrock で、最新のモデルがアカウントかリージョンでまだ使えないとき、`sonnet`・`opus`・`haiku` が古いモデルに切り替わらず、セッションの途中でエラーを示す問題を修正
- Claude apps gateway が、要求が名指すすべてのモデルを `availableModels`・`deniedModels`・`models` と照らさない問題を修正。止められたモデルを名指す要求は、そのフィールドを名指す 400 を受け取ります
- managed settings が Claude apps gateway を求める環境で、`claude auth login` が動こうとしない問題を修正。ターミナルではゲートウェイのサインインを示します
- Read の許可のルールが作業ディレクトリの外のファイルを覆っていると、`--restricted` のセッションがそれらをアップロードする問題を修正
- 見えない文字を含むプロンプトを送るのに 2 回目の Enter が要る問題を修正。ふつうのプロンプトは 1 回目の Enter で取り除いて送り、コマンドは引き続き確認を待ちます
- 親のサブエージェントのモデルを継承したサブエージェントが、バックグラウンドのジョブかメッセージで起こされるとメインのモデルに移る問題を修正
- `"$defaults"` のない managed の `autoMode.allow` の一覧が、ホストのアプリの `--settings`・`/permissions` で最初に加えたルール・`/auto-mode-setup` から組み込みの例外を取り戻す問題を修正
- サーバーが安全性の判定を返さなかったために auto モードがターンを止めたとき、クラウドのセッションとクラウドのスケジュールしたタスクが失敗と記録されない問題を修正
- バックグラウンドのエージェントがまだ動いているとき、auto モードがターンを止めた理由を `claude -p` の文の出力が言わないことがある問題を修正
- 実験的なベータをオフにしたプロキシか LLM ゲートウェイの後ろで、ホストのアプリケーション（Claude Desktop など）が始めたセッションで `CLAUDE_CODE_AUTO_MODE_SERVER=1` が無視される問題を修正
- 資格情報の名前の環境変数が `1` のようなスイッチの値に設定されていると、プラグインの MCP の `headersHelper` のスクリプトが壊れた `CLAUDE_PLUGIN_ROOT` とサーバーの URL を受け取る問題を修正
- SDK の `register_repo_root` の制御の要求が、作業ディレクトリの外のディレクトリの CLAUDE.md を読み込まない問題を修正（`CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1` のとき）
- Artifact ツールが、`self` のレベルのアーティファクトのデータベースのアクセスのルールに `?` を示し、それらを落とす再公開を断るときにそのルールを引用しない問題を修正
- このバージョンが知らないモデルで、自動圧縮が 20 万のコンテキストウィンドウを仮定するとき、`/model <id>` が警告しない問題を修正
- 「hold space to speak」のヒントが 3 回の表示を 1 つのセッションで使い切り、push-to-talk にキーが割り当てられていないと空のキーを示す問題を修正
- 検索のプロセスがタイムアウトで止められても終わらないとき、Grep と Glob が戻らない問題を修正（Windows で見られた）
- 会話の一部がまだ保存中の間に `/clear` か `/resume` を実行していると、その会話を再開しても plan が戻らない、まれな問題を修正
- 狭いターミナルで、初回のセットアップがセキュリティの注記とターミナルのセットアップの説明から語を落とす問題を修正
- Enterprise のアンケートのカードが、少し間を置いて入力した 1 か 0 を受け取る問題を修正。入力した答えには Enter が要ります
- セルフホストのランナー: セッションのプロセスが置き換わった後、Claude の作業中に送ったメッセージに Stop の後で答える問題を修正
- セルフホストのランナー: セッションが新しいマシンに移ると、MCP サーバーのオン・オフのスイッチが失われることがある問題を修正
- Windows: rc ファイルが errexit と pipefail を設定し、winpty のエイリアスだけが定義されているか何も定義されていないとき、Git Bash で Bash ツールがエイリアスと関数を失う問題を修正
- [VSCode] モデルの設定に `opus[1m]` のような `[1m]` の印があると、Effort のスライダー・Ultracode のスイッチ・モデル名が出ない問題を修正
- [VSCode] 設定ファイルにエラーがある間、保存した `/btw` の脇の質問の履歴が早すぎる時点で消される問題を修正
- [VSCode] 「Yes, and manually approve edits」で plan を承認した会話が、再読み込みか再起動の後に Auto モードで戻ってくる問題を修正
- [Cloud sessions] Claude がディレクトリを変えた後、クラウドのセッションの Files のペインのファイル検索がフォルダーを ../.. のパスで示す問題を修正。結果はプロジェクトのルートからのパスで出ます
- [Claude Tag] Slack のチャンネルで Claude が作ったキャンバスが別のチャンネルか DM にも共有されると、そのチャンネルから編集・追記するのを Claude が断る問題を修正
- [Claude Tag] 両方の組織が Claude を入れていて、Slack が返信を相手の組織のアプリに届けたとき、Slack Connect のスレッドのタグなしの返信に答えがない問題を修正
- [Claude Tag] クラウドのスケジュールしたタスクの、Slack のライブの状況のチェックリストが途中のまま残る問題を修正。実行は、その実行中に投稿した最上位のメッセージを編集できます

**その他**

- **書式の書き換えだけのページ**（詳細はハイライト 3 参照）: 次の 41 ページは、タブ・アコーディオン・カードの書き換えだけで、内容は変わっていません。`agent-sdk/agent-loop`・`agent-sdk/custom-tools`・`agent-sdk/file-checkpointing`・`agent-sdk/mcp`・`agent-sdk/permissions`・`agent-sdk/quickstart`・`agent-sdk/skills`・`agent-sdk/structured-outputs`・`agent-sdk/user-input`・`claude-apps-gateway-on-aws`・`claude-apps-gateway-on-gcp`・`code-review`・`common-workflows`・`communications-kit`・`debug-your-config`・`deep-links`・`devcontainer`・`features-overview`・`github-actions-cloud-providers`・`gitlab-ci-cd`・`hooks`・`hooks-guide`・`interactive-mode`・`llm-gateway-connect`・`llm-gateway-rollout`・`managed-mcp`・`mcp`・`mcp-quickstart`・`overview`・`plugins/install`・`plugins/mods/create`・`plugins/mods/interface`・`plugins/troubleshooting`・`sandboxing`・`self-hosted-environments-configuration`・`self-hosted-environments-identity`・`settings-example`・`sub-agents`・`terminal-config`・`troubleshooting`・`voice-dictation`。内容の変わった 51 ページのうち 18 ページ（`authentication`・`channels`・`cloud-environments`・`costs`・`desktop`・`desktop-quickstart`・`env-vars`・`feature-availability`・`how-claude-code-works`・`permission-modes`・`quickstart`・`remote-control`・`routines`・`setup`・`slack`・`statusline`・`troubleshoot-install`・`vs-code`）にも、この書き換えがあります。`setup` のコードブロックの開始行の `theme={null}` の重なりも 1 回に戻りました
- **VS Code の拡張機能のマーケットプレイスについての注記が載った**（`vs-code` の「Install the extension」）。拡張機能のマーケットプレイスはサードパーティのソフトウェアで、Anthropic は推奨・保守・監査をしない、Anthropic は Visual Studio Marketplace と Open VSX Registry に拡張機能を公開のために提出している、という注記です。同じページの「Open VSX registry」は「Open VSX Registry」に、トラブルシューティングの「VS Code Marketplace」は「Visual Studio Marketplace」に表記が改められました — [日本語](https://code.claude.com/docs/ja/vs-code#install-the-extension) / [English](https://code.claude.com/docs/en/vs-code#install-the-extension)
- **言い換えと箇条書き化**（内容は変わっていない）: Ultra の追記と同じ箇所かその近くで、文が分けられたり箇条書きになったりしました。`permission-modes`（「Server-side classifier review」のセッションの種類ごとの最低の版が 3 項目の箇条書きに、`defaultMode` の段落が 2 つに）、`glossary`（Auto mode の版ごとの既定の説明が箇条書きに）、`self-hosted-environments`（冒頭の段落が 3 項目の箇条書きと、「How self-hosted environments work」「Why self-host」へ案内する文に）、`claude-projects`（Claude Tag との違いの項目が 2 段落に、キャッシュの寿命の文の言い換え）、`slack`（冒頭の警告の書き直しと、「set up this version」へのリンク）、`agents`・`auto-mode-classifier-billing`・`claude-tag`・`cloud-environments`・`costs`・`desktop-quickstart`・`errors`・`fast-mode`・`how-claude-code-works`・`remote-control`・`statusline`・`tools-reference`・`vs-code`・`web-quickstart`
<!-- light:minor-updates:end -->

見出しマップ（`en/claude_code_docs_map.md`）は 6 行が加わり 3 行が外れました。加わったのは 5 の見出し（`claude-code-on-the-web` の「Share from a Max, Ultra, or Pro account」、`desktop` の「Create another machine」「Stop using a machine」「Remove an entry」、`feature-availability` の「Ultra plan」）と新しいスタンプ、外れたのは 2 の見出し（「Share from a Max or Pro account」と「Replace the host」）と古いスタンプで、`llms-full.txt` の見出しの増減と同じです。今回、見出しマップにだけ先に載った見出しはありません。

**参考リンクについて**: 日本語版は、ハイライト・大幅更新・軽微な更新でリンクした 6 ページ（`feature-availability`・`ultrareview`・`desktop`・`vs-code`・`cloud-environments`・`code-review-costs`）を取得し、該当する節があるかと今回の内容になっているかを、計 10 項目について確かめました（長いページは生の Markdown を区切って読み、`desktop` の SSH 接続の節と警告は取得した内容の要約で確かめています）。10 項目とも日本語版がすでに今回の内容になっていたので、リンクはすべて日本語版を併記しています。`feature-availability` の新しい h3「Ultra plan」は、ページ内外にこの id を使うリンクがまだないので、見出しから作った `#ultra-plan` を id として使いました。`desktop` の新しい h5 は、ページ内のリンクが使っている id です。Ultra の追記だけのページと changelog だけに載っている項目にはリンクを付けていません。**changelog ページへのリンクは、本サマリの方針どおり付けていません。**

## 新着情報

<!-- light:whats-new:start -->
**今回、新着情報（`whats-new/`）のページに変更はありません**（最新の週のダイジェストは前回と同じ Week 37 です）。
<!-- light:whats-new:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-10-29.md](./archives/latest/2026-10-29.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-10-29.md](./archives/latest-detail/2026-10-29.md)

<!--
base_commit: daf68aee10e1e23402b90d685734b8fa2df7beb5
head_commit: a900109552b6641cda7666a841e6800cad45d7ae
generated_at_full: 2026-10-31T15:15:44+09:00
-->
