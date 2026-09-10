---
対象期間: 2026年09月08日 〜 2026年09月09日
作成日: 2026-09-09
---

# Claude Code 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
前回が「見出しだけが先に届いて本文がゼロだった回」だったのに対し、今回はその**本文が全部到着した回**です。前回の持ち越し 13 件（見出し 11・ページタイトル 2）はひとつ残らず本文が書かれ、あわせて **v2.1.265 という大型リリース（約 50 項目）と、その回帰を同日に潰した v2.1.266** が changelog に載りました。差分は 3 ファイル・481 行、本文が変わったページは 33 / 191 で、`llms-full.txt` は 93,967 行から 93,952 行へわずかに縮んでいます。一方で**新しい持ち越しも 40 件積まれました**（前回の 11 件から大幅増）。その大半はエラーリファレンスの 16 件と、管理設定から MCP サーバーを配る仕組みの 9 件です。ページの新規追加・削除はなく、`whats-new/` は 7 回連続で差分がありません。

主要なものを以下に挙げます。

1. 出力スタイルの変更が、セッション途中でも次のメッセージから効くようになった（前回の宿題に答えが出た）
2. v2.1.265 が約 50 項目の大型リリースとして載り、同日の v2.1.266 がその回帰を潰した
3. スキルのページが「どこに置くと、どのセッションで読み込まれるか」を軸に書き直された
4. `/model` ピッカーが、ピン留めした ID を認識できればモデル名で表示するようになった
5. 管理設定で MCP サーバーを配る `managedMcpServers` が Claude Desktop 限定から Claude Code へ広がることを示唆する見出しが届いた
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**出力スタイルの変更がセッション途中で効くようになった**](#1-出力スタイルの変更がセッション途中で効くようになった):  
  前回「分類だけが `Actions that keep the cache` から `Actions that invalidate the cache` へ移り、本文が追いついていない」と報告した件の**本文が到着**した。**`/config` や `outputStyle` でセッション途中に切り替えると、次のメッセージから新しいスタイルが適用され、その 1 回だけ会話履歴全体がキャッシュなしで読み直される**。**v2.1.251 より前は、キャッシュは保たれる代わりに変更も適用されなかった**。プロンプトキャッシング・出力スタイル・設定リファレンス・設定ファイルの 4 ページが揃って書き換わっている。
2. [**v2.1.265 の大型リリースと同日の v2.1.266 ホットフィックス**](#2-v21265-の大型リリースと同日の-v21266-ホットフィックス):  
  changelog に **57 行が追加**され、うち 55 行が **v2.1.265（2026年09月08日）の約 50 項目**。プロンプトキャッシュ再利用の修正が 3 件、プラグインの安全性・表示の修正が 5 件、Claude apps gateway 関連が 4 件と、範囲が広い。**同じ 2026年09月08日付の v2.1.266 は 1 項目だけで、v2.1.265 が入れてしまった回帰の修正**である ―― 未文書化の `CLAUDE_CODE_USE_GATEWAY` が単独で Cloud gateway サインインを強制するようになり、API キーや `apiKeyHelper` と併用していた構成が全リクエスト失敗していた。**なお v2.1.264 の項は changelog にない**。
3. [**スキルのページが読み込み先を軸に書き直された**](#3-スキルのページが読み込み先を軸に書き直された):  
  前回予告された構造変更の本文が届き、**今回唯一の大幅更新**（実質 115 行）になった。h3 `Where skills live` は **h2 `Choose where skills load` へ昇格**し、置き場所の表が **4 行から 7 行へ拡張**（ネスト・追加ディレクトリ・claude.ai アカウントが行として独立）。**名前衝突の解決は 6 行の表を持つ独立節に切り出され**、`Live change detection` は `Edit a skill during a session` に改称された。一方で `strictPluginOnlyCustomization` の 3 分類や `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD` の説明は**他ページへのポインタに畳まれ、正味 25 行減っている**。
4. [**`/model` ピッカーがピン留めしたモデルを名前で表示するようになった**](#4-model-ピッカーがピン留めしたモデルを名前で表示するようになった):  
  従来「サードパーティプロバイダーでピン留めすると、プロバイダー固有の ID がそのまま表示される」と書かれていた挙動が、**「Claude Code が ID を認識できればモデル名、できなければ生の ID」へ改められた**。`us.anthropic.claude-sonnet-4-5-20250929-v1:0` をピン留めすると行は `Sonnet 4.5` と読める。**Microsoft Foundry はデプロイメント名がユーザー定義なので、`modelOverrides` でマップしても認識されない**という例外も明記された。環境変数リファレンス側でも `_NAME` / `_DESCRIPTION` 系 9 行が同じ内容に揃えられている。
5. [**管理設定で MCP サーバーを配る仕組みが Claude Code へ広がる**](#5-管理設定で-mcp-サーバーを配る仕組みが-claude-code-へ広がる):  
  組織の MCP 制御ページに、**新しい h2 `Provide servers through managed settings` と配下 5 節、既存 h2 配下の 3 節、計 9 見出しが見出しマップに現れた**。`llms.txt` の同ページ説明文も「ユーザーが追加・接続できる MCP サーバーを制限する」から**「制限する、あるいは全ユーザーにサーバーを提供する」へ書き換えられている**。**`managedMcpServers` という設定自体は v2.1.259（2026年09月02日）で既に出荷済み**だが、**現行ドキュメントではサードパーティ Claude Desktop デプロイ限定**で、Claude apps gateway の設定リファレンスは今も「ポリシーの `cli` ブロック内の `mcpServers` はブート時に拒否する ―― グループ単位で Claude Code クライアントへ MCP サーバーを配布することはできない」と明記している。**今回の見出しは、この制限が Claude Code 側にも開かれることを示唆する**が、**本文は 5 節とも未着**である。
<!-- light:highlight-list:end -->

## 1. 出力スタイルの変更がセッション途中で効くようになった

前回のサマリでハイライト 1 として扱った「`Changing output style` がキャッシュを保持する側から無効にする側へ移った」件は、見出しマップの 2 行だけが届いた状態でした。今回、**その本文が 4 ページにわたって到着しました**。

プロンプトキャッシングのページには `### Changing output style` が `Actions that invalidate the cache`（キャッシュを無効にするアクション）の配下に**新設**され、`Actions that keep the cache`（キャッシュを保持するアクション）側の同名節は**削除**されました。新しい本文はこうです ―― 出力スタイルはシステムプロンプトの一部であり、`/config` または `outputStyle` 設定でセッション途中に切り替えると、**Claude は次のメッセージから新しいスタイルを使い、そのリクエストはキャッシュヒットなしで会話履歴全体を読み直す**。コストを小さく保つには、セッション最初のメッセージの前か、`/clear`・`/compact` の直後に切り替えるとよい。そして **「v2.1.251 より前は、セッション途中のスタイル切り替えはキャッシュを保ったが、`/clear` するか新しいセッションを始めるまで適用されなかった」**と、旧挙動がバージョン境界つきで明記されました。

前回「分類が反転した以上、少なくともキャッシュを無効にするようにはなったはずだが、**変更が途中でも適用されるようになったことまで含むのかは本文が来るまで断定できない**」と書きましたが、**答えは「含む」でした**。キャッシュが無効になる理由は、システムプロンプトが作り直されるからであり、作り直される以上は新しいスタイルも効く、という素直な形に落ち着いています。

波及は 4 ページです。

- **プロンプトキャッシング**: 上記の新設・削除に加え、冒頭のレイヤー表の「システムプロンプトが変更される場合」の欄に **「出力スタイルを切り替えるか」が追加**されました。あわせて表の直後の「3 列目は一般的なトリガーであり、以下のセクションが完全なセットを説明する」という文から、**「セッション開始時に固定される出力スタイルのようなコンテンツを含む」という但し書きが削除**されています。`Actions that keep the cache` の導入文も、代表例が「CLAUDE.md の編集や出力スタイルの変更」から **「CLAUDE.md の編集」だけ**に狭められました。
- **出力スタイル**: 「システムプロンプトの一部なのでセッション開始時に 1 回読まれる。変更は `/clear` か新しいセッションの後に有効になる」という記述が、**「セッション途中で切り替えると次のメッセージから新しいスタイルを使う。システムプロンプトの一部なので、その最初のメッセージがプロンプトキャッシュを 1 回作り直す」**に置き換わりました。カスタムスタイル作成手順の「スタイルに切り替える」ステップも同様に書き換わり、**「ターミナルではスタイルファイルを起動時に読むので、セッション中にファイルを作成・編集した場合は再起動が要る」**という、ファイル側の制約が新たに補われています。
- **設定リファレンス**: `outputStyle` キーの説明が「Claude Code は会話ごとに 1 回スタイルをシステムプロンプトへ組み込む。このキーの編集は `/clear` か新しいセッションの後に有効になる」から、**「セッション中にこのキーを変えると次のメッセージから新しいスタイルを使う」**に変わりました。
- **設定ファイルと優先順位**: 「セッション開始時に一度だけ読まれるキー」の一覧から **`outputStyle` の行が削除**され、残るのは `model` と `effortLevel` / `modelSettings` の 2 行になりました。

- [Claude Code がプロンプトキャッシングを使用する方法 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/prompt-caching#changing-output-style)
- [How Claude Code uses prompt caching - Claude Code Docs (English)](https://code.claude.com/docs/en/prompt-caching#changing-output-style)
- [Output styles - Claude Code Docs (English)](https://code.claude.com/docs/en/output-styles#change-your-output-style)

## 2. v2.1.265 の大型リリースと同日の v2.1.266 ホットフィックス

changelog ページには **57 行が追加**され、削除はありません。内訳は **v2.1.266 が 3 行（1 項目）、v2.1.265 が 52 行（約 50 項目）**、残りが空行です。前回・前々回の changelog 差分が「v2.1.263 の 1 行だけ」「差分なし」だったのに比べると、久しぶりの大きな山です。

**v2.1.265（2026年09月08日）**は範囲が広く、単一のテーマにまとめられません。傾向としては次の 4 つの塊が目につきます。

1. **プロンプトキャッシュの再利用を壊していた経路の修正が 3 件** ―― フォアグラウンドで起動したサブエージェントを再開するとツール一覧とシステムプロンプト接頭辞が変わってしまう問題、エージェントのチームメイトと再開したサブエージェントが `SubagentStart` フックのコンテキストとプリロードされたスキルを 2 ターン目以降に接頭辞の外へ動かしてしまう問題、そして advisor ツールとその指示がリクエストごとにモデルから決め直されていた問題です。いずれも「接頭辞が毎ターン変わる＝キャッシュが効かない」という同じ症状に効きます。
2. **プラグインの安全性と表示の修正が 5 件** ―― バックスラッシュを含むプラグインパスが macOS / Linux でシンボリックリンク封じ込めチェックを迂回していた件、名前が 2 つのドットで始まるディレクトリが誤って「プラグインルートの外」と拒否されていた件、OS が検査できない既定コンポーネントフォルダ（シンボリックリンクのループなど）が黙って飛ばされていた件、`/plugin` の Discover / Browse と `claude plugin list --json --available` がマーケットプレイス側にメタデータを持たないプラグインの説明を出せなかった件、そしてマーケットプレイスエントリを `plugin.json` より優先する表示メタデータの変更です。
3. **Claude apps gateway 関連が 4 件** ―― Claude Desktop と Cowork がゲートウェイ経由で送るテレメトリに `user.email` と `user.groups` が加わり、OTLP テレメトリ中継が不正なペイロードを数件拒否すると 30 秒すべての転送を止めてしまう問題が直り、ゲートウェイの管理設定が `OTEL_EXPORTER_OTLP_ENDPOINT` でコレクタを指定していればセッションが中継を介さず直接送るようになり、`forceLoginGatewayUrl` を管理設定に持つマシンは起動時点でゲートウェイセッションとして扱われるようになりました。
4. **プラットフォーム固有の修正** ―― **Windows では、AppContainer や制限付きトークンのサンドボックス内で Read / Write / Edit が「権限チェック後にシンボリックリンクの解決が変わった」と言ってすべてのファイルを拒否する問題**が直りました。VS Code 拡張では非アクティブなセッションの自動アーカイブ（既定 14 日）が加わっています。

**v2.1.266（同じく 2026年09月08日）は 1 項目のみで、v2.1.265 が持ち込んだ回帰の修正**です。未文書化の環境変数 `CLAUDE_CODE_USE_GATEWAY` は、従来 `ANTHROPIC_BASE_URL` と `ANTHROPIC_AUTH_TOKEN` の両方が設定されていなければ無視されていました。ところが v2.1.265 でこれ単独でも Cloud gateway サインインを強制するようになり、**API キー・`apiKeyHelper`・カスタム認証ヘッダーと併用していた LLM ゲートウェイ / プロキシ構成が、全リクエストを `Not signed in to the Cloud gateway` で失敗させていた**とのことです。v2.1.266 で単独指定は再び無視されるようになり、**設定の変更は不要**と明記されています。

**なお changelog に v2.1.264 の項はありません**（v2.1.265 の次は v2.1.263 が並びます）。前回・前々回にも v2.1.262 の欠番があり、番号の飛びは珍しくありません。

**このハイライトには参考リンクを付けていません。** 上記でまとめた挙動の大半は changelog にしか記述がなく、対応する通常ドキュメントページには今回書き下ろされていないためです（本サマリは changelog ページの URL を参考リンクに使わない方針です）。`Model not found` や `Couldn't save it as your default` のように、**エラーリファレンス側の見出しだけが今回の見出しマップに現れた項目もありますが、そちらも本文はまだ届いていません**（持ち越しの詳細は「軽微な更新」参照）。個別の項目のうち、既存の通常ドキュメントページに対応セクションがあるもの（`forceLoginGatewayUrl` と `--plugin-dir`）には「軽微な更新」でリンクを付けています。

## 3. スキルのページが読み込み先を軸に書き直された

前回、見出しマップの差分 17 行のうち 11 行がスキルのページに集中していると報告しました。**今回その本文が到着し、実質 115 行（追加 45・削除 70）で今回唯一の大幅更新になりました**。

**構造**は予告どおりです。h2 `Getting started`（はじめに）配下にあった h3 `Where skills live` が **h2 `Choose where skills load`（スキルの読み込み先を選ぶ）へ昇格**し、配下の h4 4 つがそれぞれ h3 へ 1 段上がって改称されました。h2 が 8 → 9、h3 が 22 → 26、h4 が 14 → 10 という増減も、この 1 段昇格と整合します。

**置き場所の表が 4 行から 7 行に増えました。** 従来は Enterprise / Personal / Project / Plugin の 4 行でしたが、今回 **Nested（サブディレクトリの `.claude/skills/`）・Additional directory（`--add-dir` で渡すディレクトリ）・claude.ai account（claude.ai で有効にしたスキル）が独立した行**になっています。列名も「Applies to」（適用対象）から **「Loads in」（どのセッションで読み込まれるか）**へ変わり、各行の記述が「誰が使えるか」から「どこで読み込まれるか」に揃えられました。この書き換えで**新しい事実も 2 つ明記されています** ―― Personal（`~/.claude/skills/`）は**このマシン上の全プロジェクトで読み込まれるが Cowork とクラウドセッションでは読み込まれない**こと、そして Enterprise のパスが「管理設定を参照」ではなく**管理設定ディレクトリ内の `.claude/skills/<skill-name>/SKILL.md`** と具体的に示されたことです。

**名前衝突の解決が独立した節になりました。** 従来 `Where skills live` の地の文に 6 つの箇条書きで埋もれていた優先順位（enterprise > personal > project、バンドルスキルの上書きとエイリアスの例外、プラグインの名前空間、コマンドファイルとの関係、claude.ai 同期スキルとの関係）が、**h3 `Resolve skills that share a name` の 6 行の表**に整理されました。ネストされたスキルとプロジェクトルートのスキルが「両方読み込まれる」ことも、この表の 1 行として明示されています。

**`Live change detection` は `Edit a skill during a session` に改称され、置き場所も移りました。** 前回「同じ内容の改称なのか別物なのかは見出しからは判断できない」と書きましたが、**中身は同じもの**でした ―― スキルディレクトリのファイル変更を監視し、追加・編集・削除が再起動なしで現在のセッションに効く、という説明と、`SKILL.md` のテキストのみが対象で `hooks/` や `.mcp.json` は `/reload-plugins` が要る、という但し書きの 2 段落がそのまま引き継がれています。**加わったのは「ベアモードを除く」という 1 語**だけです。位置は `Skills synced from claude.ai` の後・`Remove a skill` の前で、これも前回の見立てどおりでした。

**一方で減った記述もあります。** ページ全体は追加 45 行に対し削除 70 行で、**正味 25 行縮んでいます**。畳まれたのは主に次の 2 か所です。

- **`strictPluginOnlyCustomization` と bare mode の 3 分類**（スキル / コマンド / サブエージェントで挙動がどう違うか、という 3 つの箇条書き）が、**「それぞれのページが説明するとおり制限する」という 1 文と、権限ページの一覧表へのポインタ**に置き換わりました。
- **`CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD` の `<Note>`** と、追加ディレクトリから読み込まれない `.claude/` 設定を列挙した段落も、同じ一覧表へのポインタに吸収されました。

このほか、**Desktop のスケジュール済みタスクの記述が「他のローカルセッションと同じ場所からスキルを読み込む」から「ローカルで動くので `~/.claude/skills/` を読み込む」へ**、直接的な言い方に改められています。また `/skill-doctor` レポートの説明に **「オフにする場所を教えるスキルのうち、コンテキストコストが最も高いものから手を付けるとよい」**という 1 文が加わりました。

**リンクのアンカーについて注意があります。** 公式ドキュメント自身の相互参照は、**改称後も旧アンカーを指しています** ―― Agent SDK のスキルページは `Choose where skills load` というリンク文言で `/docs/en/skills#where-skills-live` を指し、スキルページ自身も `Edit a skill during a session` へのリンクに `#live-change-detection` を使っています。`#choose-where-skills-load` は `llms-full.txt` 全体で 1 度も現れません。**本サマリはこの実在するアンカーに合わせています。** 新設節だけは新しいアンカー `#resolve-skills-that-share-a-name` を持ち、機能一覧ページと Agent SDK 側の参照もそちらへ更新されています。

- [Extend Claude with skills - Claude Code Docs (English)](https://code.claude.com/docs/en/skills#where-skills-live)

## 4. `/model` ピッカーがピン留めしたモデルを名前で表示するようになった

サードパーティプロバイダーでモデルをピン留めしたときの `/model` ピッカーの見え方が変わりました。**従来は「プロバイダー固有の ID がそのまま表示される」**とだけ書かれていましたが、今回**認識できるかどうかで 2 通りに分かれる**と改められました。

- **認識される ID**: Claude Code が知っているモデルの正確な ID ―― Anthropic API の ID でも、プロバイダーやゲートウェイ側の形でもよく、`[1m]` サフィックスの有無も問いません。`us.anthropic.claude-sonnet-4-5-20250929-v1:0` をピン留めすると、行は **`Sonnet 4.5`** と読めます。
- **認識されない ID**: アプリケーション推論プロファイルの ARN や、Claude Code が知らないバージョンなど。ただし `modelOverrides` のエントリがその文字列にモデルをマップしていれば認識されます。**Microsoft Foundry だけは例外で、デプロイメント名がユーザー定義であるため、マップしてもピン留めした ID が認識されることはなく、行にはデプロイメント名が出ます**。

行がモデル名を表示する場合でも、**既定の説明文にはピン留めした ID が含まれる**ので、どの ID が効いているかは確認できます。同じ規則がカスタムモデルオプション（`ANTHROPIC_CUSTOM_MODEL_OPTION`）にも適用され、`_NAME` を省いたときの挙動が「モデル ID を使う」から「認識できればモデル名、できなければ ID」に変わりました。

**`_DESCRIPTION` 系の記述も整理されました。** 従来 Opus と Sonnet だけ「未設定なら `Custom Opus model`、ただし ID に `[1m]` サフィックスがあり `CLAUDE_CODE_DISABLE_1M_CONTEXT` がオフなら `Custom Opus model (1M context)`」という長い条件つきでしたが、今回**「`Custom Opus model` で始まる既定の説明を表示する」という共通の言い方に揃えられ**、Fable / Haiku を含む 4 ファミリーで表現が統一されました。**1M コンテキストの分岐そのものが無くなったのか、単に説明を丸めただけなのかは、この差分からは判断できません。**

環境変数リファレンス側でも同じ内容へ **9 行**（`ANTHROPIC_CUSTOM_MODEL_OPTION_NAME` と、Fable / Haiku / Opus / Sonnet 各 2 行）が書き換えられています。また**ゲートウェイ互換ガイドの「ピッカーのエントリとキャッシュ」**にも同じ規則が入り、ゲートウェイが `id` と異なる `display_name` を返したときだけそれを使い、それ以外は認識できれば名前・できなければ `id` を出す、と明記されました。**例**として、`id` が `my-gateway-claude-sonnet-4-6` で `display_name` が無いエントリは `Sonnet 4.6` と表示される、と挙げられています。

**この変更にバージョン番号は付いていません。** changelog にも該当項目はないため、どのリリースから効くのかは今回の差分からは分かりません。

- [Model configuration - Claude Code Docs (English)](https://code.claude.com/docs/en/model-config#customize-pinned-model-display-and-capabilities)
- [Claude Code gateway compatibility guide - Claude Code Docs (English)](https://code.claude.com/docs/en/llm-gateway-protocol#picker-entries-and-caching)

## 5. 管理設定で MCP サーバーを配る仕組みが Claude Code へ広がる

組織の MCP サーバーアクセスを制御するページに、**見出しマップ上で 9 件の見出しが現れました**。今回の持ち越し 40 件のうち、エラーリファレンスの 16 件に次いで多く、**構造としては最もまとまっています**。

新設されるのは h2 `Provide servers through managed settings`（管理設定を通じてサーバーを提供する）と、その配下の 5 節です。

| 新しい見出し | 想定される内容 |
|---|---|
| `What an entry can contain` | エントリに書ける項目 |
| `How provided servers load` | 提供されたサーバーの読み込まれ方 |
| `What users can see and change` | 利用者から見える範囲と変更可否 |
| `Where managedMcpServers applies` | この設定が適用される範囲 |
| `When provided servers connect` | 接続のタイミング |

あわせて、既存の h2 `Exclusive control with managed-mcp.json`（`managed-mcp.json` による排他制御）の配下にも 3 節 ―― `Deploy managed-mcp.json`、`` Servers passed with `--mcp-config` or `--strict-mcp-config` ``、`How allowlists and denylists apply to the managed set` ―― が加わります。

**ページの役割が変わることは、`llms.txt` の説明文が同時に書き換わっている点からも読めます。** 同ページの 1 行説明は今回、**「ユーザーが追加・接続できる MCP サーバーを、管理設定ファイル・アローリスト・denylist で制限する」から「制限する、**あるいは全ユーザーにサーバーを提供する**、管理設定ファイル・管理設定・アローリスト・denylist で」**へ変わりました。今回の `llms.txt` の差分はこの 1 行だけです。つまり**「制限する」だけだったページの役割に「配布する」が加わる**ことは、ページの要約レベルで既に宣言されています。

**ここで重要なのは、`managedMcpServers` という設定自体は新しくないということです。** changelog によれば **v2.1.259（2026年09月02日）**で「組織が全ユーザーに HTTP / SSE の MCP サーバーを提供できる管理設定 `managedMcpServers` を追加（エントリの形は `.mcp.json` と同じ。実行コマンドを指定するエントリはスキップされる）」として出荷済みで、**デスクトップアプリのページの管理設定表には既に完全な仕様が書かれています** ―― **サードパーティ（3P）Desktop デプロイ限定**であること、各エントリに `"http"` / `"sse"` / `"stdio"` のトランスポートと接続情報、任意で `toolPolicy` マップ（そのサーバーのどのツールを呼べるか）を書くこと、管理設定ファイル・MDM・Claude apps gateway のポリシーの `desktop` ブロックのいずれかで配信すること、ゲートウェイ経由の配信にはゲートウェイ側で Claude Code v2.1.232 以降が要ること、です。

**そして現行ドキュメントは、これが Claude Code には使えないことを明示しています。** Claude apps gateway の設定リファレンスは、ポリシーの `cli` ブロックの中の `mcpServers` を**ブート時に拒否する**と述べ、**「グループ単位で Claude Code クライアントへ MCP サーバーを配布することはできない。デバイスごとのファイルベースの `managed-mcp.json` で配るか、開発者にローカルで追加させること」**と書いています。`managedMcpServers` をポリシーの `desktop` ブロック経由で配れるのは Claude Desktop クライアント向けだけ、という但し書きつきです。

**今回届いた見出しは、この線引きが動くことを示唆します。** 組織の MCP 制御ページ（Claude Code 向けのページです）に「管理設定を通じてサーバーを提供する」節ができ、その配下に **`Where managedMcpServers applies`（この設定が適用される範囲）**という節が置かれること、設定リファレンスの MCP グループに `managedMcpServers` のキーが加わること、そして Claude apps gateway の設定リファレンスの `managed` > `` What goes in `cli` `` の配下に **`MCP servers in a policy`（ポリシー内の MCP サーバー）**という節が新設されること ―― この 3 つは同じ方向を指しています。

**ただし本文は 1 行も届いていません。** 新設 5 節の本文は `llms-full.txt` のどこにも見当たらず、設定リファレンスにも `managedMcpServers` のキー説明はまだありません（見出しマップに行が加わっただけです）。ゲートウェイ側の上記の警告文も、今回の差分では手つかずのままです。**したがって、Claude Code に対して何がどこまで配れるようになるのか、`managed-mcp.json` による排他制御とどう併用するのか、利用者が上書きできるのかは、いずれも次回以降の本文到着待ちです。**

- [Control MCP server access for your organization - Claude Code Docs (English)](https://code.claude.com/docs/en/managed-mcp)
- [Desktop application - Claude Code Docs (English)](https://code.claude.com/docs/en/desktop#managed-settings)
- [Claude apps gateway configuration - Claude Code Docs (English)](https://code.claude.com/docs/en/claude-apps-gateway-config#managed)

## 新規追加されたページ

<!-- light:new-pages:start -->
（今回の対象期間に新規追加・削除されたドキュメントページはありません。`llms.txt` の収録 URL は 202 件・全体 355 行のままで、差分はページ説明文 1 行のみです。`llms-full.txt` の展開ページ数も 191 のまま動いていません。ただし**見出しマップには 40 件の見出し変更が入っており、うち 39 件は本文がまだ無い持ち越し**です。詳細は「軽微な更新」を参照してください）
<!-- light:new-pages:end -->

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
- [**スキル**](#1-スキル) ([English](https://code.claude.com/docs/en/skills#where-skills-live)):  
  前回予告された構造変更の本文が到着し、置き場所の表が 7 行に拡張され、名前衝突の解決が独立した節に切り出された。**今回「実質の差分 50 行以上 かつ 内容の変更を伴うこと」を満たす唯一のページ**（実質 115 行 = 追加 45・削除 70。桁揃えや空要素のノイズはなし）。内容はハイライト 3 で詳述。
<!-- light:updated-pages:end -->

## 1. スキル

スキルのページは、**今回「実質の差分 50 行以上 かつ 内容の変更を伴うこと」という基準を満たした唯一のページ**です（実質 115 行 = 追加 45・削除 70。生の差分も同じ 115 行で、桁揃えや空要素によるノイズはありません）。前回の持ち越し 13 件のうち 8 件がこのページのもので、**その全部が今回本文として書き下ろされました**。変更の中身はハイライト 3 で詳しく扱っています。

次点以降は閾値に届きませんでした。

| ページ | 実質の差分 | 備考 |
|---|---|---|
| 設定ファイルと優先順位 | 22 行（追加 10・削除 12） | **生の差分は 83 行で 2 番目に大きいが、うち 61 行は本文を持たない `<span />` 行とそれに伴う空行**（`<span />` は 67 個から 36 個へ減少）。内容の変更は導入部の組み替えに限られる（ハイライト 1） |
| モデル設定 | 30 行（追加 22・削除 8） | ハイライト 4 |
| プロンプトキャッシング | 26 行（追加 14・削除 12） | ハイライト 1 |
| 環境変数 | 24 行（追加 12・削除 12） | ハイライト 4 と、バージョン注記の削除 3 件 |
| 設定リファレンス | 18 行（追加 10・削除 8） | ハイライト 1 と、バージョン注記の削除 4 件 |

**実質最大は changelog の 57 行ですが、changelog は個別ページとして扱わず「軽微な更新」で扱います**（前回・前々回と同じ扱いです）。分量が足りなかっただけで内容が乏しいわけではなく、上表の 5 ページはいずれもハイライトで扱っています。

- [Extend Claude with skills - Claude Code Docs (English)](https://code.claude.com/docs/en/skills#where-skills-live)

## 軽微な更新

<!-- light:minor-updates:start -->
今回の差分は **3 ファイル・481 行**（追加 252・削除 229）です。内訳は `llms-full.txt` が 437 行（追加 211・削除 226）、ページ見出しマップ（`en/claude_code_docs_map.md`）が 42 行（追加 40・削除 2）、`llms.txt` が 2 行（追加 1・削除 1）。`llms-full.txt` の総行数は **93,967 行から 93,952 行へ 15 行縮み**、展開ページ数は 191 のままです。見出しマップの 2 行は先頭の自動生成スタンプ（2026年09月08日 19時23分06秒 UTC → 2026年09月09日 22時56分21秒 UTC）なので、**見出しそのものの変更は 40 行（追加 39・削除 1）**になります。

本文が変わったページは **33 / 191**、見出しマップが変わったページは **13** です。**前回の持ち越し 13 件（見出し 11 件・ページタイトル 2 件）は、ひとつ残らず本文が到着しました** ―― 出力スタイルのキャッシュ分類（ハイライト 1）、スキルのページの構造変更 5 件と新設 2 件・削除 1 件（ハイライト 3）、セッションデータの削除節、設定ページ 2 つのタイトル、デスクトップアプリのクイックスタートからの h2 削除です。**前回はゼロから積み直した回でしたが、今回はそれを全部消化したうえで 40 件を新たに積んだ**ことになります。

**changelog に載ったのは v2.1.265 と v2.1.266 の 2 リリース**（どちらも原文の日付表記は 2026年09月08日）です。下記の分類では、**changelog 由来の項目には版を併記**しています。**changelog にしか記述がない項目には参考リンクを付けていません**（本サマリは changelog ページの URL を参考リンクに使わない方針で、対応する通常ドキュメントページに書き下ろされていない項目はリンクを省きます）。

**新機能**

- **セッションのページに `Delete session data`（セッションデータを削除する）の本文が届きました**。トランスクリプトは保持スイープのルールで期限切れになるが、プロジェクトのトランスクリプトと関連する状態を早く消すには `claude project purge` を実行する。`claude rm <id>` でバックグラウンドセッションを削除した場合、**そのトランスクリプトはディスクに残り `claude --resume` から使える**、という 3 文です。前回「削除の手段・対象・取り消し可否はいずれも未着」と書いた点が埋まりました — [日本語](https://code.claude.com/docs/ja/sessions#delete-session-data) / [English](https://code.claude.com/docs/en/sessions#delete-session-data)
- **オートモードの分類器が既定でブロックする対象に、v2.1.261 の 1 項目が書き下ろされました**。**URL 自体が共有内容を運ぶ形で、公開のペースト・図表・データ共有サービスへのリンクを、メッセージ・PR / イシュー本文・ドキュメントなど「そのリンクが開かれる・取得される場所」に投稿または記述すること**が、そのサービスを利用者が名指ししていない限りブロックされます。v2.1.261 自体は 2026年09月04日リリースで既に changelog に載っていたものです — [日本語](https://code.claude.com/docs/ja/permission-modes#what-the-classifier-blocks-by-default) / [English](https://code.claude.com/docs/en/permission-modes#what-the-classifier-blocks-by-default)
- Claude Desktop と Cowork が Claude apps gateway 経由で送るテレメトリに `user.email` と `user.groups` が加わり、ターミナルセッションと揃いました（v2.1.265）
- `--plugin-dir` にプラグインの入ったフォルダを指定できるようになりました。マニフェストを持つ子フォルダがそれぞれ読み込まれ、実行中に増減した子フォルダも拾われます（v2.1.265）。**CLI リファレンスのフラグ表は今のところ「1 つのディレクトリまたは `.zip` を読む」の記述のままで、フォルダ指定にはまだ触れていません** — [English](https://code.claude.com/docs/en/cli-reference#cli-flags)
- ディスクに保存するツール結果に 1 GB の上限が入り、保存ファイルが切り詰められた場合は会話中のプレビューがその旨を伝えます（v2.1.265）
- \[VS Code] 一定期間使われていないセッションを自動でアーカイブするようになりました（新設の「Archive inactive sessions」設定・既定 14 日）（v2.1.265）

**機能改善**

- 出力スタイルの変更が、セッション途中でも次のメッセージから適用されるようになりました。v2.1.251 より前はキャッシュを保つ代わりに適用もされませんでした（詳細はハイライト 1 参照） — [日本語](https://code.claude.com/docs/ja/prompt-caching#changing-output-style) / [English](https://code.claude.com/docs/en/prompt-caching#changing-output-style)
- スキルのページが「どこに置くと、どのセッションで読み込まれるか」を軸に書き直され、置き場所の表が 7 行に、名前衝突の解決が独立した節になりました（詳細はハイライト 3 参照） — [English](https://code.claude.com/docs/en/skills#where-skills-live)
- `/model` ピッカーが、ピン留めした ID を認識できればモデル名で表示するようになりました（詳細はハイライト 4 参照） — [English](https://code.claude.com/docs/en/model-config#customize-pinned-model-display-and-capabilities)
- **設定ファイルと優先順位のページの導入部が組み替えられました**。「特定のキーを調べるなら『すべての設定』へ」という `<Tip>` が新設されて冒頭近くに置かれ、対象範囲を述べる `<Note>` はその後ろへ移動。「このページの使い方」を 3 点挙げていた段落は、設定ファイルの説明段落に統合されました。**あわせて、本文を持たない `<span />` 行が 31 個削除されています** — [日本語](https://code.claude.com/docs/ja/settings) / [English](https://code.claude.com/docs/en/settings)
- **`/skill-doctor` のレポートの説明に 1 文が加わりました** ―― オフにする場所を教えてくれるスキルのうち、**コンテキストコストが最も高いものから手を付けるとよい**、という優先順位の指針です — [English](https://code.claude.com/docs/en/skills#skill-descriptions-are-cut-short)
- **クラウド環境のページで、セットアップスクリプトと `SessionStart` フックの実行順序の説明が畳まれました**。「①キャッシュ済み環境が無いときだけ、Claude Code 起動前にセットアップスクリプトが走る ②Claude Code が起動して SessionStart フックが走る」という番号付きリストが削除され、**直後の比較表へ誘導する 1 文**に置き換わっています — [English](https://code.claude.com/docs/en/cloud-environments#setup-scripts)
- **GitHub Actions のクラウドプロバイダーページから、Amazon Bedrock の入力例の YAML スニペットが削除されました**。「後述の完全なワークフロー例に各プロバイダーの入力が既に含まれている」という 1 文とセクションへのリンクに置き換わり、7 行減っています — [English](https://code.claude.com/docs/en/github-actions-cloud-providers#choose-your-provider)
- **オートモードで既定許可される push と PR の説明が言い換えられました**。「秘密や機微データがリポジトリの外へ出る場合、または PR が別のリポジトリ・組織を対象とする場合を除く」という個別列挙から、**「その push または PR がブロック一覧に該当する場合を除く（例えば秘密や機微データの流出、別リポジトリ・組織向けの PR）」**という、ブロック一覧を正とする書き方になりました。**内容の変更ではなく参照の付け替え**です — [日本語](https://code.claude.com/docs/ja/permission-modes#what-the-classifier-blocks-by-default) / [English](https://code.claude.com/docs/en/permission-modes#what-the-classifier-blocks-by-default)
- `--worktree` の起動が大きなリポジトリで速くなりました。新しい worktree のチェックアウトが並列化されています（git 2.32 以降）（v2.1.265）
- `/workflows` のエージェント詳細が拡充されました。ツール呼び出しに実行中 / 失敗 / 完了の印が付き、サブエージェントがタスクリストを持つ場合はそれも表示され、Enter で各呼び出しの入力と結果を展開できます（v2.1.265）
- プロンプト途中で入力したスラッシュコマンドの候補が、単一のサジェストではなくリストで表示されるようになりました（フルスクリーン外では Tab で開きます）。プラグインのスキルも素の名前で見つかります（v2.1.265）
- サインインが要るリモート MCP サーバーに対して、実際に認証するまで OAuth クライアントを登録しなくなりました（v2.1.265）
- 多数のファイルを読んだ長いセッションの再開が速くなりました（v2.1.265）
- サイズ上限を超えた画像がデコードできないときのエラーが、上限を挙げるだけでなく原因と対処を示すようになりました（v2.1.265）
- Artifact ツールが他人の書いたアーティファクトを読むとき、要約がそのページを信頼できないコンテンツとして扱い、埋め込まれた指示を中継せずフラグを立てるようになりました（v2.1.265）
- `.claude` フォルダの権限オプションの文言が、実際に許可する範囲（そのセッションの間、プロジェクトの `.claude` フォルダまたは `~/.claude` 内のファイルを編集できること）を述べるよう更新されました（v2.1.265）
- 管理設定に `forceLoginGatewayUrl` を持つマシンが、`forceLoginMethod: "gateway"` と同様に起動時点から Claude apps gateway セッションになりました。残っている claude.ai ログインや API キーは使われません（v2.1.265） — [English](https://code.claude.com/docs/en/settings-reference#forcelogingatewayurl)
- 画像処理がランタイム組み込みの画像サポートを使うようになり、CLI がネイティブ画像モジュールを一時ディレクトリへ展開しなくなりました（v2.1.265）
- プラグインの表示メタデータが、Installed タブと `claude plugin details` でマーケットプレイスのエントリを `plugin.json` より優先し、足りない項目を `plugin.json` で補うようになりました（v2.1.265）
- Claude apps gateway セッションが、ゲートウェイの管理設定が `OTEL_EXPORTER_OTLP_ENDPOINT` で指定するコレクタへ OpenTelemetry を直接エクスポートするようになりました。コレクタ指定の無いセッションは従来どおり中継を使います（v2.1.265）

**バグ修正**

- フォアグラウンドで起動したサブエージェントを再開するとツール一覧とシステムプロンプト接頭辞が変わり、そのエージェントのプロンプトキャッシュ再利用が壊れる問題を修正（v2.1.265）
- エージェントのチームメイトと再開したサブエージェントが、`SubagentStart` フックのコンテキストとプリロードされたスキルを 2 ターン目以降にプロンプト接頭辞の外へ動かし、キャッシュ再利用が壊れる問題を修正（v2.1.265）
- ツール実行中に前のプロセスが落ちた後の再開を修正。最後のプロンプトが書き換えられなくなり、中断されたツール呼び出しは中断済みとして残るようになりました（v2.1.265）
- `/model opusplan[1m]` が `Model not found` で拒否される問題を修正（v2.1.265）。**なお、この `Model not found` はエラーリファレンスの見出しとして今回の見出しマップに現れていますが、本文はまだ届いていません**
- 権限プロンプトとメッセージ内の構文ハイライトが、Ruby の `?`、Erlang の `$`、Perl の `$` シジルの直後の 1 文字を落とすことがある問題を修正（v2.1.265）
- スラッシュコマンドや @ ファイルのサジェストリストが開閉するたび、フルスクリーンのトランスクリプトが 1 行ぶん飛ぶ問題を修正（v2.1.265）
- バックスラッシュを含むプラグインパスが macOS と Linux でシンボリックリンクの封じ込めチェックを迂回する問題を修正（v2.1.265）
- 名前が 2 つのドットで始まるプラグインディレクトリが、誤ってプラグインルートの外として拒否される問題を修正（v2.1.265）
- トークン更新中にセッションが閉じられたとき、VS Code と SDK のセッションが再ログインを要求することがある問題を修正（v2.1.265）
- Remote Control のセッションが応答の最後のメッセージより先にターン終了シグナルを送り、最後の部分が届く前に Claude アプリ側で応答が完了したように見える問題を修正（v2.1.265）
- アイドルタイムアウトの直前にメッセージが届くと、バックグラウンド（`--bg`）セッションがターンの途中で終了させられることがある問題を修正（v2.1.265）
- Claude Code 自身の git ステータス / 差分の取得が、作業ツリー内のネストされたリポジトリが設定した clean フィルタを実行してしまう問題を修正（v2.1.265）
- advisor ツールとその指示がリクエストごとにそのリクエストのモデルから決め直されていた問題を修正。判断は 1 回だけ行われ、変わったときは会話中に告知されるようになりました（v2.1.265）
- アーティファクトの公開が、コネクタが公開していないコネクタツール名を受け付ける問題を修正。宣言されたツールが 1 つも存在しない場合は公開を拒否し、一部だけ存在しない場合は警告するようになりました（v2.1.265）
- 管理設定がスキルだけをプラグインに固定しているとき `/add-dir <subdirectory>` がそのサブディレクトリのエージェントを読み込まず、エージェントだけが固定されているときは逆にエージェントを約束してしまう問題を修正（v2.1.265）
- 2 打鍵のキーボードショートカットが、tmux 内などで 2 打目が 1 秒以上遅れると黙ってキャンセルされる問題を修正。3 秒待ち、タイムアウト時は通知を出すようになりました（v2.1.265）
- フォークされたスキル（`context: fork`）が、キックオフプロンプトと、`--forward-subagent-text` 指定時のテキストターンを stream-json の進捗イベントとして流さない問題を修正（v2.1.265）
- OS が検査できないプラグインの既定コンポーネントフォルダ（シンボリックリンクのループなど）が黙って飛ばされる問題を修正。`/plugin` にエラーコード付きで報告されるようになりました（v2.1.265）
- Claude apps gateway の OTLP テレメトリ中継が、不正または大きすぎるペイロードを数件拒否した後、コレクタへの転送を 30 秒すべて止めてしまう問題を修正（v2.1.265）
- `/plugin` の Discover / Browse と `claude plugin list --json --available` が、メタデータを `plugin.json` にしか持たないマーケットプレイスプラグインの説明・表示名を出せない問題を修正（v2.1.265）
- 管理設定が指定した Claude apps gateway にサインイン済みのセッションで `/login` を再実行すると「ゲートウェイ URL が設定されていない」と表示される問題を修正（v2.1.265）
- 設定ファイルに書き込めなかったのに `/model` が「デフォルトとして保存した」と主張する問題を修正。保存に失敗したことと理由を伝えるようになりました（v2.1.265）。**この `Couldn't save it as your default` もエラーリファレンスの見出しとして今回現れた持ち越しです**
- Remote Control からの `/clear` が、SessionStart フックとターミナル側の開いているダイアログを待ってから完了する問題を修正（v2.1.265）
- `/config` ダイアログがタブを切り替えると高さが変わる問題を修正（v2.1.265）
- コンテナ再起動後のワークフロー実行の再開を修正。実行ジャーナルが失われた再開は、全エージェントを再実行するのではなく明確なエラーで失敗するようになりました（v2.1.265）
- `claude-api` スキルのエラーコードリファレンスを修正。モデルアクセスの失敗は 404、利用不可のベータヘッダーは 400 であり、403 ではありません（v2.1.265）
- 非対話セッション（stream-json 入力の `-p`、Agent SDK、クラウドセッション）が新しいユーザーメッセージのたびにシェルの作業ディレクトリをリセットする問題を修正。`cd` がターンをまたいで持続するようになりました（v2.1.265）
- `http` として設定された MCP サーバーのうち、レガシーな HTTP+SSE トランスポートしか話さないものが接続できない問題を修正。MCP 仕様どおり SSE にフォールバックするようになりました（v2.1.265）
- claude.ai 側では接続済みのコネクタが、クラウドセッションでは認証が必要と表示される問題を修正（未対応リクエストに HTTP 401 を返すサーバーが該当）（v2.1.265）
- コネクタの承認やサインインのリンクが待機している間、リモートセッションがサンドボックスコンテナを起動したままにする問題を修正（v2.1.265）
- 再開したセッションの「バックグラウンドタスクが完了しなかった」通知に、短いステータス行ではなくモデル向けの長い復旧手順が表示される問題を修正（v2.1.265）
- **Windows: AppContainer や制限付きトークンのサンドボックス内で、Read・Write・Edit が「権限チェック後にシンボリックリンクの解決が変わった」としてすべてのファイルを拒否する問題を修正**（v2.1.265）
- \[VS Code] 会話を 10 分以上開いたままにしていると、Reload Window や再起動の後にサイドバーのチャットが空白になる問題を修正（v2.1.265）
- \[VS Code] 「Remote Control is active」メッセージのタイムラインのドットがテキストより下にずれる問題を修正（v2.1.265）
- **v2.1.265 が持ち込んだ回帰の修正**（v2.1.266）。未文書化の `CLAUDE_CODE_USE_GATEWAY` が単独で Cloud gateway サインインを強制するようになり、API キー・`apiKeyHelper`・カスタム認証ヘッダーと併用していた構成が全リクエスト失敗していました。単独指定は再び無視されます（詳細はハイライト 2 参照）

**その他**

- **持ち越しが 40 件積まれました**（追加 39・削除 1）。**本文は 1 件も届いていません**。ページ別の内訳は、エラーリファレンス 16 件、組織の MCP 制御 9 件（ハイライト 5）、アーティファクト 2 件（`Read an artifact shared with you` / `Offer a file download`）、設定リファレンス 2 件（`maxEffortLevel` / `managedMcpServers`）、キーボードショートカット 2 件（`Effort slider actions` / `Agents actions`）、インタラクティブモード 2 件（`Complete a command mid-prompt` / `Issue reference links`）、エージェントビュー 1 件（`Read session state from a script`）、Amazon Bedrock 1 件（`Certificate errors behind a TLS-inspecting proxy`）、Claude apps gateway の設定リファレンス 1 件（`MCP servers in a policy`・ハイライト 5）、権限 1 件（`What a Bash rule doesn't match`）、CLI リファレンス 1 件（`System prompt flags in resumed conversations`）、Agent SDK のシステムプロンプト変更 1 件（`Change the prompt of an existing session`）。**削除は Remote Control ページの 1 件**で、`"Remote Control isn't available for your organization due to its compliance policy"` というエラー文字列の項が見出しマップから消えました（本文にはまだ残っています）
- **エラーリファレンスの持ち越し 16 件**は、認証・ゲートウェイ系（`Administrator policy requires a Cloud gateway sign-in` / `Could not load AWS or Google Cloud credentials` / `Bedrock setup verification timed out waiting for AWS` / `Cloud gateway session expired`）、モデル系（`Model not found` / `Model switch was blocked by a PreModelSwitch hook` / `Couldn't save it as your default`）、設定・MCP 系（`Directory couldn't be resolved to a real location` / `Cannot add MCP server to the managed scope` / `Can't read .mcp.json` / `OAuth callback port is already in use` / `stream-json input carried over 256M characters with no newline`）、プラグイン系（`Path could not be checked` / `Marketplace entry path does not stay inside the marketplace directory`）、管理設定・サンドボックス系（`Managed settings were not approved` / `Stale sandbox mask files left by a killed session`）に分かれます。**このうち少なくとも 3 件は v2.1.265 の修正項目と対応が付きます** ―― `Model not found`、`Couldn't save it as your default`、`Path could not be checked` です — [English](https://code.claude.com/docs/en/errors)
- **古いバージョン注記が 16 か所（10 ページ・15 か所の書き換え）削除されました**。対象は **v2.1.154 / .157 / .160 / .161 / .162 / .163 / .166 / .169** で、`/cd` の「v2.1.169 以降が必要」（コマンド一覧・セッション・権限の 3 ページ）、`API_FORCE_IDLE_TIMEOUT` と `CLAUDE_CODE_TMPDIR` と `VERTEX_REGION_CLAUDE_4_8_OPUS`（環境変数）、`workflowKeywordTriggerEnabled` の 2 か所と `requiredMaximumVersion` / `requiredMinimumVersion`（設定リファレンス）、`/terminal-setup` の GPU アクセラレーション（ターミナル設定）、`task:background` の和音（キーボードショートカット）、`/mcp` の「v2.1.166 から」（Remote Control）、MCP のタイムアウトの「v2.1.162 より前」、ワークフローのキーワードの「v2.1.160 より前」です。**ただしこれは網羅的な掃除ではありません** ―― v2.1.169 への言及は依然として 11 か所残っており、v2.1.101 のようなさらに古い注記も手つかずです
- **設定ページのリネームに伴う相互参照の書き換えが 10 ページで発生しました**。リンク文言 `Settings reference` → `All settings` が 9 ページ（組織向けセットアップ / オートモード設定 / Web 版 / 管理設定のデプロイ / プラグイン推奨 / サーバー管理設定 / 権限 / サンドボックス / 音声入力）、`Claude Code settings` → `Settings files and precedence` が 1 ページ（エンタープライズネットワーク設定）です。あわせて**スキルページのリネームに伴うアンカー書き換えが 3 か所**（機能一覧ページの `#where-skills-live` → `#resolve-skills-that-share-a-name`、Agent SDK のスキルページで同じアンカーとリンク文言の更新が 2 か所）ありました — [日本語](https://code.claude.com/docs/ja/settings-reference) / [English](https://code.claude.com/docs/en/settings-reference)
- **リネームが行き渡っていない箇所が 2 つ残っています**。VS Code のページは依然として `Claude Code settings` というリンク文言で設定ページを指しており、設定リファレンス側の「索引へ戻る」ボタンは `href="#all-settings"` のままです（先頭 h2 は `Settings index` に改称済み）。実際、設定ページの「コミットしたキーがチームメイトに届かない」節だけが新しいアンカー `#settings-index` を指す一方、`llms-full.txt` 全体では `#all-settings` を指すリンクが 16 か所残っています。**本サマリが設定リファレンスへのリンクにアンカーを付けていないのはこのためです** — [English](https://code.claude.com/docs/en/vs-code)
- **デスクトップアプリのクイックスタートで、前回消えた `Coming from the CLI?` の h2 の行き先が判明しました**。節ごと削除されたのではなく、**「次のステップ」の箇条書きの 1 項目として、デスクトップアプリ本体ページの `#coming-from-the-cli` へのリンクに畳まれました**。前回「他ページへ移されたのか、内容ごと落とされたのかは本文が来るまで判断できない」と書いた点の答えです（3 段落 → 1 行） — [English](https://code.claude.com/docs/en/desktop-quickstart)
- **`ConfigChange` フックのリンク先が修正されました**。WSL の `wslInheritsWindowsSettings` の参照先が、設定ページの `#available-settings`（現在は存在しない見出し）から**設定リファレンスの `#wslinheritswindowssettings`** へ差し替えられています — [English](https://code.claude.com/docs/en/hooks#configchange)
- **`availableModels` アローリストの `<Note>` が 2 段落に分割されました**。マッチングの説明のうち「特定のモデルを許可するには、ピッカーが表示する同じプロバイダー形式 ID をリストする」が **「その完全なプロバイダー形式 ID をリストする」**に簡潔化されています。内容は同じです — [English](https://code.claude.com/docs/en/model-config#customize-pinned-model-display-and-capabilities)
- 見出しマップ先頭の自動生成スタンプが 2026年09月08日 19時23分06秒 UTC から 2026年09月09日 22時56分21秒 UTC へ進みました。**対象期間中に上流の再生成が 1 回だけ走った**ことを示しています

**参考リンクについて**: **今回は 6 回ぶりに日本語版のリンクを付けられるページがあります。** 作成時点で公開中の日本語版を実際に取得して確認したところ、**プロンプトキャッシング・セッション・権限モード・設定ファイルと優先順位の 4 ページは今回の変更を反映済み**でした（日本語版のプロンプトキャッシングでは「出力スタイルの変更」が「キャッシュを無効にするアクション」の一覧に移り、本文も「次のメッセージから新しいスタイルを使う」「v2.1.251 より前は…」に更新されています）。一方、**スキル・出力スタイル・モデル設定の 3 ページは未追従**です（日本語版のスキルのページは「スキルが存在する場所」が h3 のままで「ライブ変更検出」も残っており、出力スタイルは「変更は `/clear` または新しいセッション後に有効になります」の旧記述、モデル設定は「プロバイダー固有の ID は `/model` ピッカーにそのまま表示され」の旧記述のままです）。**確認していないページは安全側で英語版のみ**にしています。アンカーについては、**改称された見出しはドキュメント自身が旧アンカーを指し続けている**ため（スキルの `#where-skills-live`・`#live-change-detection`）、本サマリもそれに合わせています。**本文が未着の持ち越しにはアンカーを付けず、ページ URL のみ**としています。
<!-- light:minor-updates:end -->

## 新着情報

<!-- light:whats-new:start -->
（今回の対象期間には `whats-new/` 配下のページに差分がありませんでした。`llms-full.txt` で本文が変わった 33 ページはいずれもリファレンス・ガイド系と changelog です。最新の週間ダイジェストは 7 回前のサマリで扱った Week 34（2026年08月17日～21日）のままで、新しい週のダイジェストの追加も既存ページの訂正もありません。`whats-new/` の無差分は 7 回連続です）
<!-- light:whats-new:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-09-08.md](./archives/latest/2026-09-08.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-09-08.md](./archives/latest-detail/2026-09-08.md)

<!--
base_commit: b8993e0293f2b6b04fd7517ad897abdaa6e0f01b
head_commit: 3609917c5bd9971a8010d16470ca46a5c7c2c8cb
generated_at_full: 2026-09-10T15:17:35+09:00
-->
