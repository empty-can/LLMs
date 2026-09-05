---
対象期間: 2026年09月03日 〜 2026年09月04日
作成日: 2026-09-04
---

# Claude Code 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
今回も 1 日分の取り込みで、差分は 33 ページ・3 ファイル合計 545 行（`llms-full.txt` 489 行 / ページ見出しマップ 52 行 / `llms.txt` 4 行）です。前回の 27 ページ・736 行と比べるとページ数は増え、生の行数は減りましたが、桁揃えのノイズを潰した実質では `llms-full.txt` が 387 行で前回の 280 行を上回ります（前回は生 728 行のうち 448 行が表の桁揃えでした）。今回の性格を一言でいうと「**前日 v2.1.260 の changelog に 1 行だけ載っていた変更が、まとめて正式なドキュメントページになった回**」で、差分パネル・`/rewind` の復元失敗・プロンプトキャッシュのミス原因・`Ctrl+L`・task output swap refused の 5 件がそれにあたります。ページの新規追加・削除はなく（展開ページ数は前後とも 191、`llms.txt` の収録 URL も 202 件のまま）、実質 50 行以上に達したのはエラーリファレンス 1 ページだけでした。`whats-new/` は 4 回連続で差分がありません。

主要なものを以下に挙げます。

1. `/diff` がフルスクリーンで会話の横に開く常駐パネルになり、専用の節・キーバインド・比較基準の切り替えが文書化された
2. `/skill-doctor` で未使用のスキルとそのコンテキストコストを洗い出せることが文書化された
3. `/rewind` が 1 つも復元できなかった場合にエラーで報告するようになり、バックアップの保持期限との関係が整理された
4. auto モードの分類器が、クラウドのインスタンスメタデータやホスト自身の資格情報など、ホスト基盤への到達を既定でブロックするようになった
5. クラウド環境の API 資格情報が Pro と Max のみの機能で、Team と Enterprise では未提供だと明記された
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**`/diff` がフルスクリーンで会話の横に開く差分パネルになった**](#1-diff-がフルスクリーンで会話の横に開く差分パネルになった):  
  インタラクティブモードのページに `Review changes with /diff` 節が新設され（実質 43 行の追加で、今回の単一節としては最大）、**フルスクリーンレンダリングでは `/diff` が会話の横にパネルを開き、Claude が編集するたびに更新されながら開いたままになる**ことが説明された。クラシックレンダラーでは従来どおりプロンプトの位置にビューアーが開く。あわせてフルスクリーン・キーバインド・コマンドリファレンスの各ページが書き換わっている。
2. [**`/skill-doctor` で未使用のスキルを洗い出せるようになった**](#2-skill-doctor-で未使用のスキルを洗い出せるようになった):  
  スキルのページに `Find unused skills` 節が新設され、**スキル一覧は使われなくても毎ターン分のコンテキストを食うため、`/skill-doctor` で各スキルのコストと呼び出し頻度を見て切るものを決める**という位置づけが示された。対話セッションでは `/plugin` の **Stats** タブに、`-p` の非対話実行ではテキストで出る。Remote Control 経由では出力されず、エラーリファレンスに専用の節が加わった。
3. [**`/rewind` が復元に失敗したことを報告するようになった**](#3-rewind-が復元に失敗したことを報告するようになった):  
  エラーリファレンスに `No files were restored` の節が新設された。**バックアップが消えている、または書き込めないためにチェックポイントのファイルを 1 つも復元できなかった場合、以前は黙ってスキップして成功したように見えていた**（v2.1.260 より前）。バックアップは保持スイープで既定およそ 30 日後に消えるため、古いセッションを再開して `/rewind` すると起こりうる。
4. [**auto モードの分類器がホスト基盤への到達を既定でブロックするようになった**](#4-auto-モードの分類器がホスト基盤への到達を既定でブロックするようになった):  
  権限モードのページに **v2.1.257 以降のブロック対象**として 4 項目が加わった。クラウドのインスタンスメタデータエンドポイント（`169.254.169.254` など）からの資格情報取得、トンネル・リバースシェル等の迂回経路での公開ホスト到達、ホスト自身の資格情報の読み取り、Claude が起動していない兄弟コンテナ・ノードへの接続である。許してよい環境は auto モード設定の新しい **Host containment** エントリで宣言する。
5. [**クラウド環境の API 資格情報が Pro と Max のみと明記された**](#5-クラウド環境の-api-資格情報が-pro-と-max-のみと明記された):  
  クラウド環境のページの 8 か所が「**Pro および Max プランでは**」という条件付きに書き換えられ、**API 資格情報は Team と Enterprise ではまだ利用できず、それらのプランでは環境ダイアログに `API credentials` セクション自体が現れない**ことが明示された。共有環境の説明も「そのダイアログから API 資格情報を追加せよ」から「Team と Enterprise では使えない」に反転している。
<!-- light:highlight-list:end -->

## 1. `/diff` がフルスクリーンで会話の横に開く差分パネルになった

インタラクティブモードのページに **`Review changes with /diff`（`/diff` で変更をレビューする）** 節が新設されました（実質 43 行の追加で、今回 1 つの節としては最大の追加です）。従来 `/diff` はプロンプトの位置に開いて閉じるまで居座る「ビューアー」でしたが、**フルスクリーンレンダリングでは会話の横にパネルとして開き、作業を続けている間ずっと開いたまま更新され続けます**。クラシックレンダラーでは従来どおりビューアーが開くため、節はこの 2 つを `Diff panel` と `Diff viewer` の 2 小節に分けて書き分けています。

**差分パネル**は、変更のあったファイルを追加・削除行数つきで一覧し、その下に各ファイルの差分を表示します。Claude がファイルを編集するかシェルコマンドを実行するたびに更新され、閉じるには `/diff` をもう一度実行するかヘッダーの `✕` を押します。利用条件は**フルスクリーンレンダリング・git リポジトリ・110 桁以上のターミナル幅・Claude Code v2.1.260 以降**の 4 つで、条件を満たさない場合は `/diff` が代わりにビューアーを開くか、理由を告げます。**ターミナル幅が 144 桁以上あれば、Claude がファイルを編集し始めた時点でパネルが自分から開きます**。一度自分で `/diff` を開いたあとは、以後のセッションでも十分な幅があれば編集開始と同時に開くようになり、逆に閉じればそのセッションでも以後のセッションでも `/diff` を実行するまで閉じたままになります。

パネルを開いている間にできることが 4 つ挙げられました。**ファイルへジャンプ**（一覧の行をクリック。パネルはマウスホイールでスクロールでき、一覧自体が入り切らないときは `Alt+Up` / `Alt+Down` または `Ctrl+Up` / `Ctrl+Down`）、**特定の行について Claude に尋ねる**（パネル内でマウス選択すると次のプロンプトに添付され、送るまで入力欄の横に行数が出る）、**除外されているファイルを表示する**（一覧はテストファイルと生成ファイルを飛ばし、このセッションより前の変更を最下部の 1 行にまとめる。どちらの件数行もクリックで展開できる）、**比較対象を変える**（`Ctrl+X B` で「このセッションの変更」→「未コミットの変更を 1 つの一覧に」→「既定ブランチから分岐して以降のすべて」を循環。選択はプロジェクトごとに記憶される）です。

キーバインドのページには **`Diff panel actions`** 節が新設され、`DiffPanel` コンテキストが追加されました。`app:cycleDiffBase`（既定 `Ctrl+X B`）だけがこのコンテキストで、`app:toggleReplTab`（`/diff` と同じ開閉。既定は未割り当て）・`app:diffFileListUp` / `Down`・`app:toggleDiffNoiseFilter`・`app:toggleDiffPreSession` は `Global` です。`ctrl+x` プレフィックスの既定コード一覧にも `ctrl+x b`（`DiffPanel`・v2.1.260 以降）が加わり、`ctrl+x` を単独キーとして取り戻すための解除例に `DiffPanel` のブロックが追記されました。フルスクリーンのページにも `Watch your changes in the diff panel` 節が新設され、コマンドリファレンスの `/diff` 行は**従来の長大な操作説明が丸ごと落ちて、新設節へのリンク 1 文に置き換わっています**。

なお**この差分パネル自体は v2.1.260 で追加済みで、前回サマリでは changelog 由来の「新機能」として 1 行触れていた項目です**。今回はそれが操作方法・利用条件・キーバインドまで含めた正式なドキュメントになった形で、同種の「昨日の changelog が今日ページになる」変更が今回はほかに 4 件あります（詳細はハイライト 3 と軽微な更新を参照）。

- [インタラクティブモード - Claude Code Docs (English)](https://code.claude.com/docs/en/interactive-mode#review-changes-with-%2Fdiff)
- [キーバインド - Claude Code Docs (English)](https://code.claude.com/docs/en/keybindings#diff-panel-actions)

## 2. `/skill-doctor` で未使用のスキルを洗い出せるようになった

スキルのページに **`Find unused skills`（未使用のスキルを見つける）** 節が新設されました（実質 8 行）。趣旨は明快で、**スキル一覧に載っているスキルは Claude が一度も使わなくても毎ターンのコンテキストを消費する**ため、`/skill-doctor` で各スキルのコストと利用頻度を見て、切るものを自分で決める、というものです。レポートの出し方はセッションの種類で変わり、**対話セッションでは `/plugin` マネージャーの Stats タブに開き、`-p` の非対話モードではテキストとして出力されます**。対象はセッション内のスキルのうち**同梱スキルとエンタープライズスキルを除いたもの**で、一覧にあって一度も呼ばれていないスキルを指摘し、どこで切ればよいかを示します。あわせて最近使っていないプラグインも列挙します。

制約が 3 つ書かれています。**Claude Code v2.1.252 以降が必要**なこと、[フィーチャーフラグの取得](https://code.claude.com/docs/en/env-vars#features-that-need-feature-flag-fetching)をスキップするセッションでは使えないこと、そして **Remote Control 経由（スマートフォンやブラウザ）では実行してもレポートが返らない**ことです。3 つ目についてはエラーリファレンスに **`Skill usage reports are not available on this connection`** の節が新設され、対処として「セッションが動いているマシンのターミナルで `/skill-doctor` を実行するか、そこで `claude -p "/skill-doctor"` を実行する」ことが示されました。エラーリファレンス冒頭のメッセージ対応表にも 1 行加わっています。

周辺ページも揃えられました。コマンドリファレンスに `/skill-doctor` の行が追加され、環境変数ページの「フィーチャーフラグ取得をオフにするとできなくなること」の一覧にも 1 項目が入りました。プラグイン検出のページでは `/plugin` の説明から「**4 つのタブ**」という数が外れ、タブの列挙に **Stats** が加わっています。スキルのページ内では「スキルの説明が短縮される」節にも、`/doctor` の案内に続けて「切る候補を探すなら `/skill-doctor`」という 1 文が挿入されました。

**バージョン要件については原文の 2 か所が食い違っています。** スキルのページは上記のとおり v2.1.252 以降を要求すると書いていますが、**今回入った changelog の v2.1.261 は `/skill-doctor` を「Added」として挙げています**。どちらが正しいかは原文からは決められないため、両方を併記するにとどめます。

- [スキルで Claude を拡張する - Claude Code Docs (English)](https://code.claude.com/docs/en/skills#find-unused-skills)
- [エラーリファレンス - Claude Code Docs (English)](https://code.claude.com/docs/en/errors#skill-usage-reports-are-not-available-on-this-connection)

## 3. `/rewind` が復元に失敗したことを報告するようになった

エラーリファレンスに **`No files were restored`（ファイルが 1 つも復元されなかった）** の節が新設されました（実質 19 行）。`/rewind` でコードを復元したときに、**そのチェックポイントのファイルを 1 つも復元できなかった場合**に出るメッセージで、原因はファイルごとに 2 通り ―― Claude Code が編集前に保存したバックアップが失われているか、Claude Code がそのファイルに書き込む・削除することができなかったかです。出力は `Failed to restore the code:` に続けて `No files were restored: 1 file failed (backup missing, or the file could not be updated)` のように出ます。

**このエラーが現実に起きる筋道として、保持スイープが名指しされました。** Claude Code はセッションのバックアップを保持スイープで削除し、既定では**そのセッションが最後にバックアップを保存してからおよそ 30 日後**に消えます。その後にセッションを再開すると `/rewind` はチェックポイントを一覧してくれるものの、いざ巻き戻すとこのエラーで失敗しうる、という説明です。対処は 3 つで、**別の方法で戻す**（Claude に編集を戻させる、またはバージョン管理から復元する。バックアップが消えている以上、`/rewind` をやり直しても同じように失敗する）、**書き込みを妨げているもの（ファイルのパーミッションなど）を直してから再実行する**、**今後のセッションのために `cleanupPeriodDays` を引き上げる**です。メッセージに `N paths were skipped for link safety` が併記されている場合は、既存の `Restored the code, but skipped files` 節を見るように案内されています。**v2.1.260 より前は、バックアップが失われたファイルは黙って飛ばされ、巻き戻しは成功したように見えていました**。

この節の追加に合わせて、`## Rewind warnings` という見出しが **`Rewind warnings and errors`（巻き戻しの警告とエラー）** に改称され、導入文も「この警告は…」から「**`Restored the code, but skipped N files` は一部のパスを飛ばしたという警告、`No files were restored` は何も復元しなかったというエラー**」と 2 種類を区別する書き方に変わりました。エラーリファレンス冒頭のメッセージ対応表にも新しい行が加わり、既存の行のリンク先セクション名も改称に追随しています。

**保持側のページも同時に書き換わりました。** チェックポイントのページでは「30 日後にセッションと一緒にチェックポイントを削除する」という記述が、「**セッションのファイルスナップショットを保持スイープで削除する。既定ではそのセッションが最後にスナップショットを保存してからおよそ 30 日後**」に改められ、スナップショットが消えたチェックポイントへの巻き戻しは新エラーで失敗しうる、という一文が加わりました。`~/.claude/` のページでも `file-history/` の位置づけは変わらないものの、**自動メモリの除外の書きぶりが「ディレクトリを丸ごとスイープから除外する」から「メモリファイルを削除しない」に**精緻化されています（同じ書き換えがメモリのページにも入りました）。

**この項目も、前日 v2.1.260 の changelog にバグ修正として 1 行だけ載っていたものです**（前回サマリでは「チェックポイントのバックアップファイルが無く実際には何も復元されていないのに、`/rewind` と `--rewind-files` が成功と報告する問題を修正」として紹介しました）。今回それが専用のエラー節と、保持期限との因果を含む説明になりました。

- [エラーリファレンス - Claude Code Docs (English)](https://code.claude.com/docs/en/errors#no-files-were-restored)
- [チェックポイント - Claude Code Docs (English)](https://code.claude.com/docs/en/checkpointing#automatic-tracking)

## 4. auto モードの分類器がホスト基盤への到達を既定でブロックするようになった

権限モードのページの「分類器がデフォルトでブロックするもの」に、**`Claude Code v2.1.257 以降はこれらもデフォルトでブロックします`** という新しい区切りが加わり、4 項目が並びました（実質 9 行）。内容はいずれも「タスクではなく**ホストや周囲のインフラ**に手を伸ばす行為」で、次のとおりです。

- **クラウドのインスタンスメタデータエンドポイント**（`169.254.169.254` など）からの資格情報の取得、または**マシン自身のサービスアカウント／ノード ID を明示的に使って**クラウド・クラスタ・レジストリを呼ぶこと
- **直接のリクエスト以外の経路で公開ホストに到達すること**。トンネル、リバースシェル、外部を向くよう書き換えたリゾルバやプロキシの設定など
- **タスクではなくホストに属する資格情報の読み取り**。ノードの証明書や、ノードのコンテナレジストリ認証など
- **Claude が起動していない兄弟のコンテナ・Pod・VM、またはコンテナの下のノード**への接続やスキャン

節の末尾には、**これらのいずれかを許すことが意図されている環境で Claude Code を動かしている場合は、`autoMode.environment` の Host containment エントリでその構成を書け**、という案内が付きました。その受け皿として auto モード設定のページのコンテキストスロット一覧に **Host containment** が追加されています（v2.1.257 以降）。既定は「エグレス制限のない、ふつうの開発マシンまたは CI ランナー」で、コンテナ・VM・Pod で動かしていてエグレス許可リストや触ってはならない隣接ノードがある場合は、**許可するホスト・クラウドのメタデータエンドポイントに到達してよいか・どのクラウドプロジェクト／クラスタ／レジストリをどの ID で使うか**を書くよう求められます。**このエントリがその ID を名指しするまで、分類器はホスト自身の資格情報を求めるリクエストをブロックします**。

同じ一覧の記述整理も入りました。コンテキストスロットの説明から「**他の 2 種類と違い、コンテキストスロットにはそれ自体を対象とするルールが無い**」という 1 文が削除されています。Host containment が「ブロックの解除条件として直接参照されるコンテキストスロット」であるため、その但し書きが成り立たなくなったものと読めます。

- [権限モードを選択する - Claude Code Docs (English)](https://code.claude.com/docs/en/permission-modes#what-the-classifier-blocks-by-default)
- [auto モードを設定する - Claude Code Docs (English)](https://code.claude.com/docs/en/auto-mode-config#define-trusted-infrastructure)

## 5. クラウド環境の API 資格情報が Pro と Max のみと明記された

クラウド環境のページで、**API 資格情報（環境に保存しておくと Claude に鍵を見せずにエージェントプロキシがリクエストへ付与してくれる仕組み）が Pro と Max のプラン限定である**ことが、ページ内 8 か所にわたって明記されました（実質 16 行 = 追加 9・削除 7 のすべてがこの書き換えで、既存 7 行の修正と新設 1 段落の内訳です）。中核は `Add API credentials` 節に加わった 1 段落で、「**API 資格情報は Pro と Max のプランで利用できる。Team と Enterprise ではまだ利用できないため、それらのプランでは環境ダイアログに API credentials セクションが現れない**」と述べています。

書き換えの方向が特徴的で、**従来「代わりに API 資格情報を使え」と勧めていた箇所が、条件付きか、逆向きの注意に変わりました**。ページ冒頭の機能列挙は「API 資格情報を保存できる」から「**Pro と Max では** API 資格情報を保存できる」になり、環境ダイアログの説明も「既存の環境を編集するとダイアログに API 資格情報も含まれる」から「**Pro または Max プランで**既存のクラウド環境を編集すると」に変わりました。環境変数の節の「環境を使う人は誰でも値を読めるので、代わりに API 資格情報を使え」も「**Pro と Max では**代わりに API 資格情報を使え」に条件が付いています。

最も反転が大きいのは**組織共有環境**の節です。従来は「共有環境は環境セレクターからも開け、**そのダイアログこそが API 資格情報を追加する場所である**」「共有環境の変数は全メンバーのセッションが読むのでシークレットを入れるな。読めない鍵を渡すには**そのダイアログから API 資格情報を追加せよ**」と書かれていましたが、今回はそれぞれ「オーナーはそこで編集できる」（API 資格情報への言及を削除）と「**セッションに読めない鍵を渡す API 資格情報は、Team と Enterprise ではまだ利用できない**」に置き換わりました。共有環境は Team と Enterprise の機能なので、**共有環境に対する API 資格情報の案内は事実上すべて取り下げられた**ことになります。「セットアップから引き継がれるもの」の表でも、API キーとトークンの行が「はい、API 資格情報として」から「**Pro と Max プランでは**、API 資格情報として」になり、備考に「エージェントプロキシが付与できない鍵、**または Team・Enterprise プランのあらゆる鍵**は環境変数に置いたままになる」が加わりました。

同じ制限が 2 ページに波及しています。ルーチンのページでは、環境変数の説明の「API 資格情報として保存せよ」に「**Pro と Max プランでは**」が付きました。Web 上の Claude Code のセキュリティと分離の節でも、「Anthropic ホスト環境では鍵がサンドボックス外に留まる」が「**Pro と Max プランの** Anthropic ホスト環境では」になり、末尾に「セルフホスト環境に API 資格情報は無く、**Team と Enterprise プランにもまだ無い**」が加わりました。

- [クラウド環境を設定する - Claude Code Docs (English)](https://code.claude.com/docs/en/cloud-environments#add-api-credentials)
- [Web 上の Claude Code - Claude Code Docs (English)](https://code.claude.com/docs/en/claude-code-on-the-web#security-and-isolation)

## 新規追加されたページ

<!-- light:new-pages:start -->
（今回の対象期間に新規追加・削除されたドキュメントページはありません。`llms-full.txt` に展開されているページ数は前後とも 191 で、`llms.txt` の収録 URL も 202 件・全体 356 行のまま変わりません。ただし `llms.txt` には 2 回連続で差分が出ており、今回は Agent SDK の「はじめに」グループに `Migrate to Claude Agent SDK` が移動し、`Troubleshooting` が `Troubleshoot the Agent SDK` に改称されました。ページの追加・削除ではなく並べ替えと改称のため、本カテゴリには該当がありません。詳細は軽微な更新を参照してください）
<!-- light:new-pages:end -->

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
- [**エラーリファレンス**](#1-エラーリファレンス) ([English](https://code.claude.com/docs/en/errors#no-files-were-restored)):  
  新しい節が 3 つ加わり、`Rewind warnings` の見出しが `Rewind warnings and errors` に改称された。冒頭のメッセージ対応表にも 4 行が入り、`Tool errors` の導入文が書き直された。今回、実質の差分が 50 行以上に達した唯一のページ（実質 56 行 = 追加 52・削除 4）。
<!-- light:updated-pages:end -->

## 1. エラーリファレンス

エラーリファレンスは今回、**changelog を除けば唯一「実質 50 行以上」の基準を満たしたページ**です（実質 56 行 = 追加 52・削除 4。生の差分でも 56 行で、桁揃えノイズはありません）。加わった節は 3 つで、いずれも既にハイライトで扱った内容です。

1. **`Skill usage reports are not available on this connection`**（コマンドラインエラー）―― Remote Control 越しに `/skill-doctor` を実行したときの応答（詳細はハイライト 2 参照）
2. **`Task output swap refused`**（ツールエラー）―― Bash コマンドの出力ファイルのパス上にシンボリックリンクや移動されたディレクトリがあるため、Claude Code が出力をそこへ書かずにコマンドの実行自体を拒否したことを示すメッセージ
3. **`No files were restored`**（巻き戻しの警告とエラー）―― `/rewind` がファイルを 1 つも復元できなかったときのエラー（詳細はハイライト 3 参照）

2 つ目の `Task output swap refused` は今回のハイライトに入れていないので補足します。Claude Code は各 Bash コマンドの出力を一時ディレクトリ配下のファイルに保存しますが、**そのファイルのパス上のディレクトリがシンボリックリンクになっている、または移動されている場合、Claude Code はそのパスを通して書くことを避けてコマンドを実行しません**。メッセージは Bash ツールの結果に現れ、対処は 3 つ挙げられています。**v2.1.260 以降へ上げること**（それ以前のバージョンは、リンクも移動されたディレクトリも無いのにこのメッセージを出すことがありました）、`CLAUDE_CODE_TMPDIR` に新しいディレクトリを指定して再起動すること、一時ディレクトリ配下のプロジェクト用ディレクトリを確認し、シンボリックリンクや不要なディレクトリであれば**リンク先ではなくリンク／ディレクトリそのものを消して**再起動すること、です。**これも前日 v2.1.260 の changelog にバグ修正として載っていた項目**で、前回サマリでは「多数のセッションが 1 つのプロジェクトディレクトリを共有するときに `task output swap refused` エラーが断続的に出る問題を修正」として紹介していました。

節の追加に伴う既存記述の整理も 2 か所あります。**`Tool errors` の導入文**が、「Claude はほとんどのツールエラーを自分で直す。**下の最初の 2 つ**はサブエージェント定義か権限ルールに由来するのであなたの変更が要る」から、「Claude はほとんどのツールエラーを自分で直す。**あなたの変更が要るものは、そのエラーの What to do 一覧が何を変えるべきかを述べる**」に書き換わりました。節が増えて「最初の 2 つ」という位置指定が維持できなくなったための一般化と読めます。**巻き戻しの節の改称**についてはハイライト 3 のとおりです。

冒頭のメッセージ対応表には 4 行の変更が入りました。追加は `Skill usage reports are not available on this connection.`、`task output swap refused (tasks dir moved or linked)`、`No files were restored: N files failed (backup missing, or the file could not be updated)` の 3 行で、既存の `Restored the code, but skipped N files` の行はリンク先セクション名が `Rewind warnings and errors` に差し替わっています。

- [エラーリファレンス - Claude Code Docs (English)](https://code.claude.com/docs/en/errors#no-files-were-restored)

## 軽微な更新

<!-- light:minor-updates:start -->
今回も 1 日分の取り込みで、`llms-full.txt` に差分のあったページは 33、差分行は 3 ファイル合計 545 行（`llms-full.txt` 489 行 = 追加 390・削除 99 / ページ見出しマップ 52 行 = 追加 36・削除 16 / `llms.txt` 4 行 = 追加 2・削除 2）です。前回は 27 ページ・736 行だったので、**ページ数は 2 割増える一方で生の行数は 3 割近く減っています**が、これは前回の 736 行のうち 448 行が設定リファレンスの表の桁揃えという「かさ」だったためです。本サマリで「実質 N 行」と書いた各行の連続空白と連続ハイフンを潰して数え直すと、`llms-full.txt` の 489 行は **387 行**（追加 339・削除 48）になり、**前回の実質 280 行を上回ります**。changelog の 70 行を除いた実質は 317 行です。ページの新規追加・削除はなく、展開ページ数は前後とも 191 のままです。

`llms.txt` は 2 回連続で差分が出ました。今回の 4 行はすべて Agent SDK の項で、**`Migrate to Claude Agent SDK` が末尾の「リファレンス」グループから冒頭の「はじめに」グループへ移動**し、同じ位置にある **`Troubleshooting` が `Troubleshoot the Agent SDK` に改称**されたものです。収録 URL は 202 件、ファイル全体も 356 行で変わりません。ページ見出しマップ側でも同じ移動が 13 行分の削除と追加として現れており、`llms-full.txt` の該当ページでは見出し `# Troubleshooting` が `# Troubleshoot the Agent SDK` に変わった 1 行だけが差分です。

**changelog には v2.1.261（2026年09月04日）が 1 件加わりました**（70 行すべて追加）。内訳は本体 41 件（追加 4・修正 27・改善 5・変更 5）と VS Code 拡張分 26 件（追加 5・修正 20・変更 1）の計 67 件で、前回扱った v2.1.260 の 66 件（本体 59・VS Code 7）とほぼ同規模ですが、**VS Code 拡張の比重が 7 件から 26 件へ大きく増えている**点が異なります。単一リリースのみのため、以下の changelog 由来の項目にはバージョンを個別に併記しません（すべて v2.1.261 です）。

今回の性格を一言でいうと、**前日 v2.1.260 の changelog に 1 行だけ載っていた変更が、まとめて正式なドキュメントページになった回**です。該当するのは、差分パネル（ハイライト 1）、`/rewind` の復元失敗（ハイライト 3）、`task output swap refused`（大幅更新 1）、プロンプトキャッシュのミス原因、`Ctrl+L` の画面クリアの 5 件で、後ろ 2 件は下記の「新機能」に挙げています。前回サマリの `--permission-prompts none` と同じ経路（changelog で先に出て、翌日ページ化される）が今回は 5 件同時に起きた形です。

**なお今回は、ページ見出しマップに現れているのに `llms-full.txt` の本文が届いていない「持ち越し」が 7 件あります**（前回はゼロでした）。内訳は、エラーリファレンスの `Working directory is a network path`・`MCP server is blocked by enterprise managed policy`・`Malformed Tool(content) rule` の 3 見出し、設定リファレンスの `bashOutputMaxChars`・`taskOutputMaxChars` の 2 キー、TypeScript Agent SDK リファレンスの `user_message_uuids`、キーバインドの `Make editing keys follow readline conventions` → `Word boundaries in editing shortcuts` の改称です。**うち設定リファレンスの 2 キーとキーバインドの改称は、今回入った v2.1.261 の changelog に対応するエントリがあります**（`bashOutputMaxChars` と `taskOutputMaxChars` の追加、単語編集キーを Bash に合わせる変更）ので、本文は次回以降の取り込みで届く見込みです。マップの `Last updated` は 2026年09月04日 00:25 UTC から 2026年09月05日 04:30 UTC に進み、見出しの新規追加は 20 件、改称は上記を含めて 2 件、それに `migration-guide` ブロックの移動 13 行が加わって 52 行の差分になっています。

本サマリの参考リンクは前回に続き**すべて英語版のみ**です。今回の変更に日本語版が追従していないためで、作成時点で公開中の日本語版ページを実際に取得して確認しました（本リポジトリに取り込んである `en/` のスナップショットではなく、`code.claude.com` のライブページを参照しています）。確認結果は次のとおりです。**日本語版のインタラクティブモードには「`/diff` で変更をレビューする」に相当する節が無く、`Ctrl+L` の説明も「画面を再描画」の旧記述のまま**、**日本語版のスキルのページには「未使用のスキルを見つける」に相当する節が無く、`/skill-doctor` が一度も登場しない**、**日本語版の権限モードのページには v2.1.257 以降のブロック一覧が無く（v2.1.205 以降の区切りで止まっている）、`169.254.169.254` も Host containment も登場しない**、**日本語版のエラーリファレンスには `No files were restored`・`Task output swap refused`・`Skill usage reports are not available on this connection` のいずれの節も無い**、**日本語版のクラウド環境のページには「API 資格情報を追加する」節自体が存在せず、API 資格情報という機能が丸ごと未反映**でした。他のページは個別には確認していませんが、いずれも直近 1〜2 日の変更であるため未追従とみなし、安全側に倒して英語版のみを載せています。

なお分類の基準は前回同様「実質の差分 50 行以上 かつ 内容の変更を伴うこと」としました。**インタラクティブモードは実質 48 行で閾値に 2 行足りず**、大幅更新ではなく本カテゴリの扱いですが、内容は今回最大の追加（`/diff` の新節 43 行）なのでハイライト 1 で本文を扱っています。次点以下は、キーバインド 26 行、`~/.claude/` ディレクトリ 25 行、ステータスライン 19 行、クラウド環境 16 行、トラブルシューティング 14 行です。

**新機能**

- `/diff` がフルスクリーンで会話の横に開く差分パネルになり、`Diff panel actions` のキーバインドと `Ctrl+X B` による比較基準の切り替えが加わりました（詳細はハイライト 1 参照）— [English](https://code.claude.com/docs/en/interactive-mode#review-changes-with-%2Fdiff) / [English](https://code.claude.com/docs/en/keybindings#diff-panel-actions)
- `/skill-doctor` で未使用のスキルとそのコンテキストコストを洗い出せることが文書化されました（詳細はハイライト 2 参照）— [English](https://code.claude.com/docs/en/skills#find-unused-skills)
- **フルスクリーンレンダリングで `Ctrl+L` が画面をクリアするようになりました**。以前のメッセージは上へスクロールアウトし、`PgUp` やマウスホイールで読み戻せます。`Cmd+K` はターミナルが Claude Code へ渡す場合に同じ動作をしますが、iTerm2 と Terminal.app はそれ自身が処理してしまうため、それらのターミナルでは `Ctrl+L` を使えとされました。v2.1.260 より前の `Ctrl+L` はクリアせず再描画するだけで、v2.1.238 より前は 2 秒以内に 2 回押すと `/clear` が走っていました — [English](https://code.claude.com/docs/en/fullscreen#clear-the-conversation)
- **プロンプトキャッシュのミスの推定原因が構造化されたデータとして取れるようになりました**。ステータスラインの `prompt_cache` に `last_miss_cause`（`causes` 配列に `tools_changed`・`system_prompt_changed`・`ttl_expired_5m`・`likely_server_side` などが入り、`tools_added` / `tools_removed` / `system_char_delta` の増減も付く）と `miss_causes`（原因ごとの件数）が加わり、専用の小節も新設されました。`/usage` の `Prompt cache (main)` 行にも `likely cause: tool definitions changed` のような形で出ます。プロンプトキャッシュのページにも同じ 1 文が追記されました。いずれも v2.1.260 以降が必要です — [English](https://code.claude.com/docs/en/statusline#last-miss-cause) / [English](https://code.claude.com/docs/en/costs#prompt-cache-statistics) / [English](https://code.claude.com/docs/en/prompt-caching#check-cache-performance)
- TypeScript Agent SDK の結果に `first_content_frame_ms`（thinking ブロックも content として数え、最初の `content_block_start` / `content_block_delta` までの時間）と `first_stream_post_ms` ほか 2 つのアップロード計測が加わりました。後者は claude.ai へストリームするセッション（クラウドセッションなど）でのみ記録され、`query()` が返す結果には載りません。いずれも Agent SDK v0.3.260 以降が必要です — [English](https://code.claude.com/docs/en/agent-sdk/typescript#sdkresultmessage)
- TypeScript Agent SDK の `SDKThinkingTokensMessage` に `user_message_uuid` が加わり、**ターン最初の応答を待たずに thinking の進捗を送信メッセージへ紐づけられる**ようになりました（Agent SDK v0.3.260 以降）— [English](https://code.claude.com/docs/en/agent-sdk/typescript#user_message_uuid)
- `/status` と `claude doctor` に「Organization policy」行が加わり、組織のポリシーを読み込めなかった理由（プロキシがエンドポイントを通していない等）が出るようになりました
- `bashOutputMaxChars` と `taskOutputMaxChars` の設定が加わり、コマンドとバックグラウンドタスクの出力をファイルへ退避する前に Claude がインラインで受け取る量を最大 128K 文字まで引き上げられるようになりました（設定リファレンス本文は未着で、ページ見出しマップにのみ現れています）
- `--append-subagent-system-prompt-file` が加わり、コマンドラインに渡すには大きすぎるサブエージェントのシステムプロンプトをファイルから読めるようになりました
- VS Code 拡張の Output styles メニューに「Build a custom style」ウォークスルーが加わり、カスタム出力スタイルのファイルを書いてその場で一覧に出すようになりました
- VS Code 拡張の MCP サーバーダイアログに Add server フォームと Remove アクションが加わり、IDE を離れずに MCP サーバーを追加・削除できるようになりました
- VS Code 拡張のセッション一覧で、ターミナル・別の VS Code ウィンドウ・Claude Desktop で開いているセッションに中空のリングが付き、閉じているように見えなくなりました
- VS Code 拡張の権限・質問プロンプトに折りたたみボタンが加わり、プロンプトを閉じずに後ろの会話を読めるようになりました。プロンプト脇のスペースで会話をスクロールできます
- VS Code 拡張のセッション一覧の右クリックメニューに「Archive session」が加わり、Unarchive に専用アイコンが付きました

**機能改善**

- `/rewind` が 1 つも復元できなかった場合の専用エラー節が新設され、チェックポイントのスナップショットが保持スイープで消える条件が明確化されました（詳細はハイライト 3 参照）— [English](https://code.claude.com/docs/en/errors#no-files-were-restored) / [English](https://code.claude.com/docs/en/checkpointing#automatic-tracking)
- Bash コマンドの出力ファイルのパスがリンク・移動されていた場合の `Task output swap refused` が専用のエラー節になりました（詳細は大幅更新 1 参照）— [English](https://code.claude.com/docs/en/errors#task-output-swap-refused)
- auto モードの分類器が v2.1.257 以降ブロックするホスト基盤系 4 項目が文書化され、その受け皿として Host containment のコンテキストスロットが加わりました（詳細はハイライト 4 参照）— [English](https://code.claude.com/docs/en/permission-modes#what-the-classifier-blocks-by-default) / [English](https://code.claude.com/docs/en/auto-mode-config#define-trusted-infrastructure)
- クラウド環境の API 資格情報が Pro と Max 限定であることがページ内 8 か所とルーチン・Web 上の Claude Code の各ページに反映されました（詳細はハイライト 5 参照）— [English](https://code.claude.com/docs/en/cloud-environments#add-api-credentials) / [English](https://code.claude.com/docs/en/routines#create-from-the-web)
- **`/model` で選んだモデルが次のセッションで別のものになる理由が、モデル設定のページに新しい小節としてまとまりました**。原因は 4 つで、①そのセッション限りの選択だった（ピッカーで `s` を押した、`--model` で起動した、非対話モードで `/model` を実行した）、②優先度の高いものがモデルを決めている（プロジェクト／管理設定の `model`、シェルの `ANTHROPIC_MODEL`、管理者が上書き指定した組織既定。保存自体はされていて順位で負けている）、③`~/.claude/settings.json` に書き込めなかった（別のツールが生成している・読み取り専用へのリンクなど）、④セッションを再開した、です — [English](https://code.claude.com/docs/en/model-config#a-new-session-starts-on-a-different-model-than-you-picked)
- 設定のページにも **`A change you made in Claude Code is lost in new sessions`** の小節が新設され、Claude Code の中から保存した選択はユーザー設定ファイルに書かれるため、そのファイルに書き込めないと次のセッションで消えることが説明されました — [English](https://code.claude.com/docs/en/settings#a-change-you-made-in-claude-code-is-lost-in-new-sessions)
- **バックグラウンドコマンドと Monitor の停止の扱いが整理されました**。`/tasks` や接続中のクライアント（デスクトップアプリなど）からバックグラウンドタスクを止めた場合、Claude はそれを待たずに先へ進みます（サブエージェントが起動したものなら、そのサブエージェントが先へ進みます）。**サブエージェントを止めると、そのサブエージェントが起動した Monitor も一緒に止まります**。macOS と Linux では、`/tasks` からの停止や Claude Code の終了時の停止で、`setsid` や `timeout` の下で起動してタスクのシェルから切り離されたプロセスも止まるようになりました — [English](https://code.claude.com/docs/en/tools-reference#background-commands) / [English](https://code.claude.com/docs/en/tools-reference#monitor-tool)
- **`claude -p` の終了待ちの説明が 1 段落から 4 段落に分割され、Monitor の扱いが加わりました**。バックグラウンドのサブエージェント・ワークフローを待つ点は変わりませんが、**10 分の待機上限に達した時点で Claude Code は残っているものを止めて部分的な結果を捨てる**ことが明記されました。Monitor の watch を起動した場合は、watch 自体のタイムアウト（既定は起動から 5 分）か 10 分の上限のいずれか早い方まで待ち、待っている間も Claude は watch の報告に応答し続けます。`CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS` の説明もこれに合わせて書き直されました — [English](https://code.claude.com/docs/en/headless#background-tasks-at-exit)
- **`~/.claude/` 配下で「消してはいけない state ファイル」が明示されました**。従来「その他の小さなキャッシュとロックファイルは消して安全」の 1 文だった箇所が、キャッシュとロックは安全としたうえで、`.credentials.json`（ログイン資格情報）・`agent-memory/`（サブエージェントのメモリ）・`jobs/` と `daemon/`（バックグラウンドセッションの状態）は残せ、という 3 項目に置き換わりました。あわせて `~/.claude/tasks/` が「ユーザーから見て失うものは無い」の行から独立し、「再開したセッションが拾うはずのタスクリスト」を失うと明記され、`history.jsonl` の用途にも `Ctrl+R` の履歴検索と `!` のシェルコマンド補完が追記されました — [English](https://code.claude.com/docs/en/claude-directory#kept-until-you-delete-them)
- Remote Control がポリシーで拒否される原因に 2 つ目が加わりました。**claude.ai のプランが Pro / Max なのに、以前のログインで Team / Enterprise 組織にサインインしたままになっている**場合で、Claude Code はその組織のポリシーを見にいきます。`/status` でどのプラン・組織のサインインを使っているか確認し、`claude auth logout` と `claude auth login` で入り直すよう案内されました — [English](https://code.claude.com/docs/en/remote-control#remote-control-is-disabled-by-your-organizations-policy)
- **サンドボックス内でクリップボードコマンドが届かない件がトラブルシューティングとサンドボックスの両ページに載りました**。`pbcopy` / `xclip` / `wl-copy` はサンドボックス化された Bash コマンドの中からシステムのクリップボードに届かないことがあり、Claude が流し込んだテキストが反映されません。対処は、Claude に応答へ内容を出させてから `/copy` を使う（`/copy` はサンドボックス化されたコマンドではなく Claude Code のプロセス自身から書くため妨げられず、コードブロック 1 つだけのコピーもでき、コピー内容をファイルにも書いてパスを出すので SSH 越しなどのフォールバックになる）か、`excludedCommands` に `pbcopy *` などを加えてサンドボックス外で動かすことです — [English](https://code.claude.com/docs/en/troubleshooting#clipboard-commands-such-as-pbcopy-fail-inside-the-sandbox) / [English](https://code.claude.com/docs/en/sandboxing#troubleshooting)
- フルスクリーンでマウスホイールが 1 行ずつしかスクロールしない場合の節がトラブルシューティングに新設されました。`/scroll-speed` で 1 ノッチあたりの行数を上げて保存するか `CLAUDE_CODE_SCROLL_SPEED` を設定します（JetBrains の IDE ターミナルでは Claude Code 独自のスクロール処理が効くためどちらも無効）。速度を変えずに速く動かすには `PgUp` / `PgDn` で半画面ずつ、ターミナル本来のスクロールバックに戻すには `/tui default` でクラシックレンダラーに切り替えます — [English](https://code.claude.com/docs/en/troubleshooting#mouse-wheel-scrolls-one-line-at-a-time-in-fullscreen-rendering)
- Agent SDK の移行ガイドが `llms.txt` とページ見出しマップの両方で「はじめに」グループへ移動し、Agent SDK 概要の「次のステップ」にもリンクが加わりました。本文には **OpenAI Agents SDK からの移行レシピ**（1 つの実例で各プリミティブを Claude Agent SDK に対応づけるクックブック）への案内が追加されています — [English](https://code.claude.com/docs/en/agent-sdk/migration-guide) / [English](https://code.claude.com/docs/en/agent-sdk/overview#next-steps)
- Fable モデルの説明で、`/model fable` やモデル ID を打った場合の挙動が「ピッカーが一覧に出す前でも選択が成功しうる」から「**ピッカーが一覧に出していなくても、打ち込んだ選択は成功しうる**」に書き改められました — [English](https://code.claude.com/docs/en/model-config#work-with-fable)
- `/model` ピッカーと VS Code のモデルピルが、Claude Code が認識できる場合に Bedrock・Vertex AI・LLM ゲートウェイの生の ID ではなくモデル名を表示するようになりました
- `GOOGLE_APPLICATION_CREDENTIALS` が設定されている場合の Google Vertex AI の起動が改善され、API クライアント生成時に Google Cloud のプロジェクト探索をやり直したり余分な `gcloud` プロセスを起こしたりしなくなりました
- ストリーミングの描画性能が改善され、描画済みのブロックが更新のたびにレイアウトで再チェックされなくなりました
- 危険な `rm` の安全プロンプトが、位置パラメータへの `rm -rf` と二重引用符で囲まれた `sh -c` スクリプト内の `rm -rf` も捕捉するようになりました
- API がレスポンスヘッダーを返さない場合の再試行が、もう 3 分ではなく `API_TIMEOUT_MS`（既定 10 分）まで待つようになり、メッセージも何を変えるべきかを述べるようになりました
- Claude apps gateway が管理設定の読み込み（起動時または `/login` 後）で 403 を返したときのメッセージが、サインインし直せという案内ではなく「組織で Claude Code が有効になっていない可能性がある」という内容に変わりました
- 管理設定で `forceLoginMethod: "gateway"` が固定されているマシンが、残っている API キーや claude.ai ログインを無視して `/login` を求めるようになりました（Bedrock・Vertex AI・Foundry のセッションは対象外）
- auto モードが、公開の図表レンダラーの URL に内容を詰め込むリンクをそのサイトへのアップロードとして扱うようになり、依頼していない限り自動承認しなくなりました
- プロンプトの単語編集キーが Bash に合わせられ、`Ctrl+W` は空白まで戻って削除、`Alt+F` と `Alt+D` は単語の終わりで止まり、句読点が単語を区切るようになりました。`keybindingFlavor` は効果を持たなくなりました（キーバインドのページ本文は未着で、ページ見出しマップにのみ改称が現れています）
- `/context` のトークン計数が、トークン計数 API を使えないときに小さいモデルへの追加リクエストではなくローカルの推定を使うようになりました

**バグ修正**

- 入力が速いときやキーリピート中に、打った文字や貼り付けた文字が順序を入れ替えて着いたり落ちたりする問題を修正
- 作業ディレクトリが `/net` の automount にある場合に `/add-dir <subdirectory>` が「解決できませんでした」という誤ったエラーを出す問題を修正
- Bedrock のセットアップウィザードが、AWS や AWS の資格情報ヘルパーが応答しないまま固まる問題を修正（タイムアウトして明確なエラーを出すようになりました）。TLS 検査プロキシの背後でモデルチェックが失敗する問題もあわせて修正
- 管理設定が `enabledPlugins` でプラグインを強制有効化している場合に、クラウドセッションが claude.ai から同期されたプラグインを捨て、失敗しうるマーケットプレイスのクローンにフォールバックする問題を修正
- プロンプト入力でインラインの `[Image #N]` チップの直前の文字を削除できない問題を修正
- セッションを再開すると並列ツール呼び出し周辺のフック出力やコンテキストが失われ、再開後のリクエストが変わってしまう問題を修正
- スマートフォン・ブラウザ・claude.ai アプリがターミナルセッションに接続したとき、またはターミナル側でモードが変わったあとに、Remote Control が古い権限モードを表示する問題を修正
- 接続中のスマートフォンやブラウザからターンを止めたあと、または `/clear` などのローカルスラッシュコマンドのあとに、Remote Control のセッションが作業中のまま（スピナーと Stop ボタンが残ったまま）に見える問題を修正
- SDK とクラウドのセッションで、最初のプロンプト直後・ターン開始前に送られた Stop や割り込みが無視される問題を修正。ターンが最後まで走り切らずに止まるようになりました
- Remote Control が `/teleport` で引き寄せたセッションを接続中のセッションへアップロードし、スマートフォンや Web で元のセッションに継ぎ足されたように見える問題を修正
- ネイティブ Windows で、TLS 検査を行う企業プロキシの背後だと Remote Control の受信イベントストリームが失敗する問題を修正
- 努力レベルが設定由来の場合に、Remote Control のセッションが claude.ai 上で既定の努力レベルを表示する問題を修正
- Google の資格情報チェックが遅いだけで資格情報自体は有効なときに、`gcpAuthRefresh` が起動時にブラウザを開いてしまう問題を修正
- 起動時のコネクタ取得がタイムアウトすると、claude.ai のコネクタがそのセッション中ずっと現れない問題を修正。CLI がバックグラウンドで再試行するようになりました
- バックグラウンドエージェントを再開できないときに、その起こし直しがタイトなループで再試行されて CPU 使用率が高止まりする問題を修正
- 新しいバージョン向けに絞られたフィーチャーフラグが、同じマシンで動いている古い Claude Code に適用されることがある問題を修正
- 使用状況エンドポイントがレート制限されているときや起動直後に開いたときに、`/usage` と VS Code の使用状況パネルがモデル別の週次上限の行を落とす問題を修正
- `claude -p --resume <file>` が、トランスクリプトに記録された不正なセッション ID を引き継ぐ問題を修正。新しいセッション ID で再開するようになりました
- バックグラウンドのワークフローやエージェントがまだ動いているのに、ターミナルの進捗インジケータ（iTerm2・Ghostty・ConEmu）がセッションを完了として表示する問題を修正
- コンテナが行方向と列方向を切り替えたあとに、ボックスが誤った高さで描画されることがある稀なレイアウトの不具合を修正
- 信頼するプロキシが `X-Forwarded-For` にポートを付ける場合の Claude apps gateway のクライアント IP を修正。アクセスリストを設定している場合、読み取れないエントリは 403 になります
- ターミナルの CLI が protobuf を使っていても Claude apps gateway が Claude Desktop に OpenTelemetry を JSON で送るよう指示し、protobuf のみのコレクタが Desktop のデータを拒否する問題を修正
- アーティファクトの更新を監視しているだけのセッションを、Desktop と Web が処理中として表示する問題を修正
- Claude Desktop アプリから実行するローカルの Cowork セッションで、Claude in Chrome の `file_upload` が "paths: expected array, received undefined" で失敗する問題を修正
- 別マシンのオフラインな Remote Control セッションへの `SendMessage` が配信済みとして読める問題を修正。そのマシンが再接続するまで配信が保留であると返すようになりました
- バックグラウンドの Bash コマンドで実行した CLI からのプラグインインストールのヒントを検出するようになり、生の `<claude-code-hint>` タグが会話に漏れなくなりました
- インプロセスのエージェントチームのチームメイトが、2 ターン目に初回ターンのツール・スキルの告知を再送し、リクエストの接頭辞が変わってプロンプトキャッシュを外す問題を修正
- **［VS Code］** Claude Code on the web からテレポートしたセッションで、クラウドセッションの終了時に打ち切られた質問が「拒否された」扱いになる問題を修正
- **［VS Code］** ウィンドウと一緒に復元したタブのセッションタブの Rename ボックスが空で開く問題を修正。現在の名前が入った状態で開くようになりました
- **［VS Code］** セッション一覧パネルの折りたたんだセクションが、パネルの読み込みのたびに一瞬展開して見える問題を修正
- **［VS Code］** 質問が回答待ちのときなど、Claude が先へ進んだあとも Focus ビューがツール呼び出しを実行中と表示する問題を修正
- **［VS Code］** フォーカスされていない Claude タブのセッション ID が訂正されたときに、セッション一覧のアクティブ行のハイライトが古いままになる問題を修正
- **［VS Code］** Claude タブにフォーカスがあるときに、`Cmd/Ctrl+Shift+T` の再オープンとディープリンクからの起動が Claude タブを Claude のエディタグループの外に置く問題を修正
- **［VS Code］** セッションタブの「Add to group」が、Claude Code on the Web から開いたセッションを 2 つのグループに入れる問題を修正。セッション一覧が表示しているエントリを移動するようになりました
- **［VS Code］** 組織がすでに無効化したモデルを、ウィンドウを 2 回リロードするまでモデルピッカーが表示する問題を修正
- **［VS Code］** VS Code がタブのビューをリロードしたあとに、セッション一覧から開いたタブがそのセッションへ戻ってしまう問題と、Web セッションから開いたタブがテレポートをやり直すか空のままになる問題を修正
- **［VS Code］** ウィンドウのリロード直後や設定ファイルにエラーがある状態で質問すると、以前のセッションの `/btw` サイドクエスチョンの履歴が上書きされる問題を修正
- **［VS Code］** Claude.ai または Console アカウントでサインインしている場合に、Claude パネルのリロード後に保留中の質問カードが再表示されない問題を修正
- **［VS Code］** 1 つのパネルが設定ファイルから第三者プロバイダーを拾ったあとも、同じウィンドウの他の Claude パネルに claude.ai 限定の機能が表示されたままになる問題を修正
- **［VS Code］** Claude Code がログイン無しと報告した場合やリクエストがログイン不足で失敗した場合に、Disable Login Prompt 設定があってもサインイン画面が出る問題を修正
- **［VS Code］** 次に控えている権限プロンプトが、前のプロンプトで入力したテキストを保持し、続けざまの 2 回目のクリックも受け付ける問題を修正
- **［VS Code］** セッション一覧しか表示していないウィンドウで、プラグインインストールのリンクが Claude サイドバーだけを開いてインストールダイアログを出さない問題を修正
- **［VS Code］** 新しいウィンドウで Account & usage ダイアログを開くまでサイドバーの使用量メーターが空のままになる問題と、0% の使用上限がメーターから漏れる問題を修正
- **［VS Code］** 「Start new session in this group」が New conversation のあとにグループを失う問題と、サイドバーの未読リストが読み込まれる前に終わったセッションの未読ドットが欠ける問題を修正
- **［VS Code］** 実行中のターンでエディタのタブバッジが未読を表示する問題、セッション一覧から開いたタブでバッジが出ない問題、アーカイブ済みセッションで「Add Session Tab to Group」が何もしない問題を修正
- **［VS Code］** 「Enable Remote Control for all sessions」の切り替えが、他の VS Code ウィンドウで開いているセッションにも即座に適用されるよう修正
- **［VS Code］** claude.ai から継続したセッションのタブが Web セッション側に記録されたままの場合に、セッション一覧の Open フィルターが正しく効かない問題を修正。あわせてフィルターメニューのセクションにスクリーンリーダー向けのラベルを付けました

**その他**

- VS Code 拡張のモデルピッカーが、すべてのモデルを 1 つのフラットな一覧にし、古い綴りのモデルの行を最後に回すようになりました
- 自動メモリの保持スイープの説明が「メモリディレクトリをスイープから除外する」から「**メモリディレクトリ内のメモリファイルを削除しない**」に精緻化されました（`~/.claude/` ディレクトリのページとメモリのページの 2 か所）— [English](https://code.claude.com/docs/en/memory#storage-location)
- 監視ページの保持スイープイベントで、`skip_reason` が `settings_unknowable` になる説明に `desktopSessionCleanupPeriodDays` が加わりました — [English](https://code.claude.com/docs/en/monitoring-usage#retention-sweep-event)
- `debug/` の説明が「`--debug` で起動するか `/debug` を実行したときだけ書かれる」から「**デバッグログが有効な間**書かれる。たとえば `--debug` で起動したときや `/debug` を実行したとき」に一般化され、`tasks/` の説明も「セッションごとのタスクリスト」から「**リストごとに 1 ディレクトリ**」に改められました — [English](https://code.claude.com/docs/en/claude-directory#cleaned-up-automatically)
- `/plugin` の説明から「4 つのタブ」という数が外れ、タブの列挙に **Stats** が加わりました（詳細はハイライト 2 参照）— [English](https://code.claude.com/docs/en/discover-plugins#try-it-add-the-demo-marketplace)
- Agent SDK のタスク追跡ページで、モデル可用性の注記が 1 文に詰め込まれていたのを「以下の制限が適用される」と本体の 2 段に分割しました — [English](https://code.claude.com/docs/en/agent-sdk/todo-tracking#model-availability)
- TypeScript Agent SDK の `user_message_uuid` の説明が「2 種類のフレーム」から「これらのフレーム」に改められ、`thinking_tokens` フレームの追加に追随しました — [English](https://code.claude.com/docs/en/agent-sdk/typescript#user_message_uuid)
- Agent SDK のトラブルシューティングページのタイトルが `Troubleshooting` から `Troubleshoot the Agent SDK` に改称されました。`llms.txt` の 4 行の差分のうち 2 行がこれです — [English](https://code.claude.com/docs/en/agent-sdk/troubleshooting)
- インタラクティブモードのキー表で `Ctrl+L` の説明が「画面を再描画」から「**画面を再描画またはクリア**」になりました（詳細は新機能の `Ctrl+L` の項を参照）— [English](https://code.claude.com/docs/en/interactive-mode#keyboard-shortcuts)
<!-- light:minor-updates:end -->

## 新着情報

<!-- light:whats-new:start -->
（今回の対象期間には `whats-new/` 配下のページに差分がありませんでした。差分のあった 33 ページはいずれもリファレンス・ガイド系です。最新の週間ダイジェストは 4 回前のサマリで扱った Week 34（2026年08月17日～21日）のままで、新しい週のダイジェストの追加も既存ページの訂正もありません。`whats-new/` の無差分は 4 回連続です）
<!-- light:whats-new:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-09-03.md](./archives/latest/2026-09-03.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-09-03.md](./archives/latest-detail/2026-09-03.md)

<!--
base_commit: 1204f96c5d31ae446075090190d361a2063df414
head_commit: 3f57b81e5934ecd89be2d817677dfcfdba5da98f
generated_at_full: 2026-09-05T15:00:30+09:00
-->
