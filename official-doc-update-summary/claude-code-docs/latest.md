---
対象期間: 2026年10月29日 〜 2026年10月30日
作成日: 2026-10-30
---

# Claude Code 公式ドキュメント更新サマリ

```markdown
**今回は changelog に v2.1.316（2026年10月31日）の 1 リリースが積まれ（v2.1.315 の項目はありません）、通常のページには、Max 20x の新しい名前の Ultra のプランが 50 ページにわたって書き加えられ、Claude Desktop のコマンドから作る SSH 接続で前のマシンを残したまま新しいマシンを作れるようになったことが載りました。`llms-full.txt` では、タブ・アコーディオン・カードが印付きの引用として出るようになっています**。新しいページはなく、228 ページ中 92 ページ（changelog を含む）に差分がありますが、そのうち 41 ページは書式の書き換えだけで、内容が変わったのは 51 ページ（changelog を含む）です。大幅更新は `desktop` の 1 ページです。見出しマップに加わった 5 の見出しは、すべて `llms-full.txt` にも入っています。総行数は 126,302 行から 126,426 行に増えました。

主要なものを以下に挙げます。

1. Max 20x の新しい名前として Ultra のプランが `feature-availability` に載り（Max は Max 5x の新しい名前で、Claude Code での機能は Max と同じ）、50 ページでプランを並べた箇所に Ultra が加わった
2. Claude Desktop のコマンドから作る SSH 接続で、「Replace the host」が「Create another machine」になって前のマシンのセッションが動き続けるようになり（Claude Desktop v4.4212.0 以降）、マシンを使うのをやめる手順とエントリを外したときの扱いの節もできた
3. `llms-full.txt` で、タブ・アコーディオン・カードが `> [tab]`・`> [accordion]`・`> [card]` の行で始まる引用のブロックになり、生の差分の大半と 41 ページの変更はこの書き換えだけだった
4. changelog の v2.1.316 で、Opus 4.8 の fast mode が非推奨になり（2026年11月30日に外される）、`CLAUDE_CODE_SUBAGENT_EFFORT` と `CLAUDE_CODE_DISABLE_ULTRATHINK` が加わった
```

## ハイライト

1. [**Max 20x の新しい名前の Ultra プランが 50 ページに書き加えられた**](./latest-detail.md#1-max-20x-の新しい名前の-ultra-プランが-50-ページに書き加えられた):  
  `feature-availability` に h3「Ultra plan」ができ、Ultra は Max 20x の新しい名前で、Max は Max 5x の新しい名前、Claude Code では Max と Ultra の機能は同じ、と載りました。プラン別の表にも Ultra の列が加わり、ほかの 49 ページでも「Pro and Max」のようにプランを並べた箇所に Ultra が加わっています
2. [**Claude Desktop のコマンドから作る SSH 接続で前のマシンを残したまま新しいマシンを作れるようになった**](./latest-detail.md#2-claude-desktop-のコマンドから作る-ssh-接続で前のマシンを残したまま新しいマシンを作れるようになった):  
  `desktop` の h5「Replace the host」が外れて h5「Create another machine」になり、**Create another Dev box** を選んでも前のマシンのセッションは動き続ける（Claude Desktop v4.4212.0 より前は置き換え）と載りました。Desktop が自分で接続しないよう前のマシンを使うのをやめる h5 と、エントリを外したときの h5 もできています
3. [**llms-full.txt でタブとアコーディオンとカードが印付きの引用として出るようになった**](./latest-detail.md#3-llms-fulltxt-でタブとアコーディオンとカードが印付きの引用として出るようになった):  
  これまで太字の行で出ていたタブの名前・アコーディオンの題・カードが、`> [tab] …`・`> [accordion] …`・`> [card] …` の行で始まる引用のブロックになり、中身も引用の中に入りました。59 ページに及び、差分のあった 92 ページのうち 41 ページはこの書き換えだけです
4. [**changelog の v2.1.316 で Opus 4.8 の fast mode が非推奨になりサブエージェントの effort の環境変数が加わった**](./latest-detail.md#4-changelog-の-v21316-で-opus-48-の-fast-mode-が非推奨になりサブエージェントの-effort-の環境変数が加わった):  
  Opus 4.8 の fast mode は 2026年10月30日に非推奨になり、2026年11月30日に外されて、その後は通常の Opus 4.8 にフォールバックせずエラーを返します。サブエージェントの effort を決める `CLAUDE_CODE_SUBAGENT_EFFORT` と、`ultrathink` をオフにする `CLAUDE_CODE_DISABLE_ULTRATHINK` も加わりました。いずれも通常のページにはまだ載っていません

## 新規追加されたページ

（今回の対象期間に新規追加・削除されたドキュメントページはありません。`llms.txt` の URL は 275 のままで、`slack` の 1 行説明だけが変わりました。`llms-full.txt` に展開されている固有のページも 228 のままで、`Source:` の行が 231 あり 3 ページが 2 回展開されている状態も前回と同じです）

## 大幅に更新されたページ

- [**Desktop application**](./latest-detail.md#1-desktop-application) ([日本語](https://code.claude.com/docs/ja/desktop#create-another-machine) / [English](https://code.claude.com/docs/en/desktop#create-another-machine)):  
  書式の書き換えを戻して数えると 59 行（追加 40・削除 19）が変わりました。ハイライト 2 の SSH 接続の節のほか、`forceLoginOrgUUID` の警告の囲みと、Dispatch の要件の箇条書き化、7 か所の Ultra の追記があります

## 軽微な更新

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

## 新着情報

**今回、新着情報（`whats-new/`）のページに変更はありません**（最新の週のダイジェストは前回と同じ Week 37 です）。

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-10-29.md](./archives/latest/2026-10-29.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-10-29.md](./archives/latest-detail/2026-10-29.md)

<!--
base_commit: daf68aee10e1e23402b90d685734b8fa2df7beb5
head_commit: a900109552b6641cda7666a841e6800cad45d7ae
generated_at_full: 2026-10-31T15:15:44+09:00
-->
