---
対象期間: 2026年09月24日 〜 2026年09月25日
作成日: 2026-09-25
---

# Claude Code 公式ドキュメント更新サマリ

```markdown
**前回「索引にだけ載り、本文はまだ」と書いたプラグインの新しい 20 ページに、今回は本文が入りました**。`llms-full.txt` の展開ページは 197 から 210 に増え、索引の 210 件とそろいました。総行数は 100,393 行から 103,108 行へ **2,715 行増えています**。changelog には **v2.1.282（86 項目）** が積まれ、前回「changelog に項目がない」と書いた AGENTS.md の制約解除も、v2.1.281 の項目として後から加わりました。

主要なものを以下に挙げます。

1. プラグインの新しい 20 ページに本文が入り、旧 7 ページが本文から消えた
2. v2.1.282 の 86 項目が積まれ、v2.1.281 に AGENTS.md の項目が後から加わった
3. OpenTelemetry の変数がプロジェクト設定とローカル設定から無視されるようになった
4. auto モードのサーバー側レビューの説明が書き直された
5. プロジェクトのスレッドを自分のマシンで動かせるようになった
```

## ハイライト

1. [**プラグインの新しい 20 ページに本文が入り、旧 7 ページが本文から消えた**](./latest-detail.md#1-プラグインの新しい-20-ページに本文が入り旧-7-ページが本文から消えた):  
  前回、`llms.txt` と見出しマップにだけ載っていた `/docs/en/plugins/` 配下の **20 ページの本文が、今回 `llms-full.txt` に入りました**（計 6,999 行）。索引から外れていた**旧 7 ページ**（`discover-plugins`・`plugins`・`plugins-reference`・`plugin-marketplaces`・`plugin-dependencies`・`plugin-hints`・`plugin-relevance`、計 4,705 行）の本文は消えました。既存の **53 ページでも、プラグイン関連のリンク先が新しい URL に張り替えられています**。前回「404」と書いた `plugins/overview` の日本語版も、今回は日本語で公開されていました
2. [**v2.1.282 の 86 項目が積まれ、v2.1.281 に AGENTS.md の項目が後から加わった**](./latest-detail.md#2-v21282-の-86-項目が積まれv21281-に-agentsmd-の項目が後から加わった):  
  changelog に **v2.1.282（2026年09月24日）** が積まれました。**修正 59・変更 11・追加 8・改善 6・更新 2** の計 86 項目です。あわせて、既存の **v2.1.281 に「AGENTS.md を Amazon Bedrock・Google Vertex AI・Microsoft Foundry・LLM ゲートウェイ・テレメトリ無効のセッションでも使えるようにした」という項目が追加**され、v2.1.277 の項目からは「（Bedrock・Vertex・Foundry ではまだ使えない）」の但し書きが消えました。前回ハイライト 2 で「changelog に該当項目が見当たらない」と書いた点が、これで解消しました
3. [**OpenTelemetry の変数がプロジェクト設定とローカル設定から無視されるようになった**](./latest-detail.md#3-opentelemetry-の変数がプロジェクト設定とローカル設定から無視されるようになった):  
  **v2.1.282 から、リポジトリの `.claude/settings.json` と `.claude/settings.local.json` の `env` に書いた `CLAUDE_CODE_ENABLE_TELEMETRY`・エクスポーターの選択・送信先・内容を記録する `OTEL_LOG_*` などが無視されます**。例外は、`none` や `0` のようにテレメトリを止める値だけです。`settings-reference` に一覧が加わり、`env-vars`・`monitoring-usage`・`settings`・`settings-example` も同じ方針に書き換わりました
4. [**auto モードのサーバー側レビューの説明が書き直された**](./latest-detail.md#4-auto-モードのサーバー側レビューの説明が書き直された):  
  `permission-modes` の「サーバー側の分類器レビュー」が、**Anthropic API 直結・クラウドプロバイダーや LLM ゲートウェイ・Claude apps gateway の 3 種類の接続ごと**の説明になりました。**v2.1.282 からは、テレメトリを切ったセッションでも既定でサーバーに問い合わせます**。サーバーが判定を返さなかった操作は拒否され、**判定なしが 10 回続くとターンが止まる**ことも明記され、`errors` にこの状況の新しい節が加わりました
5. [**プロジェクトのスレッドを自分のマシンで動かせるようになった**](./latest-detail.md#5-プロジェクトのスレッドを自分のマシンで動かせるようになった):  
  `claude-projects` で、スレッドの説明が「各スレッドはクラウドセッション」から「**各スレッドは通常はクラウドセッション**」に変わりました。**自分のコンピューターにしかないものが要るタスクは、Remote Control 経由でそのスレッドを自分のマシンで動かすよう Claude に頼めます**。そのマシンには **Claude Code v2.1.280 以降**が必要で、claude.ai の設定で **Require trusted devices** がオンだと使えません

## 新規追加されたページ

- [**プラグインの新しい 20 ページ**](./latest-detail.md#1-プラグインの新しい-20-ページ) ([日本語](https://code.claude.com/docs/ja/plugins/overview) / [English](https://code.claude.com/docs/en/plugins/overview)):  
  前回は索引と見出しマップにだけあった `/docs/en/plugins/` 配下の 20 ページに、本文が入りました。**概要・インストール・作成・マーケットプレイス運用・組織管理・トラブルシューティング・リファレンス**の 7 グループです。ここでは本文の実際の構成をもとに、各ページの範囲をまとめています

## 大幅に更新されたページ

- [**Environment variables**](./latest-detail.md#1-environment-variables) ([English](https://code.claude.com/docs/en/env-vars#variables)):  
  差分 746 行の大半は表の桁揃えです。実質的な変更は、テレメトリ変数がプロジェクト設定とローカル設定で無視されることの追記、`CLAUDE_CODE_AUTO_MODE_SERVER` の説明の更新、`CLAUDE_CODE_RESUME_PROMPT` の適用範囲の拡大などです
- [**Test plugins with evals**](./latest-detail.md#2-test-plugins-with-evals) ([日本語](https://code.claude.com/docs/ja/plugin-evals#troubleshooting) / [English](https://code.claude.com/docs/en/plugin-evals#troubleshooting)):  
  段落の多くが箇条書きに組み直されました。`CI` 環境変数が真のときは信頼の確認ができずに拒否されること、ベースライン実行でプラグインのエージェントが見つからないときの節などが加わりました
- [**All settings**](./latest-detail.md#3-all-settings) ([English](https://code.claude.com/docs/en/settings-reference#variables-claude-code-ignores-in-env)):  
  `env` で無視される変数にテレメトリのグループが加わったほか、`attribution` に `false` を書けること、マーケットプレイスの `hostPattern`・`pathPattern` の照合方法などが更新されました
- [**Error reference**](./latest-detail.md#4-error-reference) ([日本語](https://code.claude.com/docs/ja/errors#the-server-returned-no-safety-verdict) / [English](https://code.claude.com/docs/en/errors#the-server-returned-no-safety-verdict)):  
  前回、見出しマップにだけあった 5 項目の本文が入りました
- [**Let Claude coordinate ongoing work with Projects**](./latest-detail.md#5-let-claude-coordinate-ongoing-work-with-projects) ([日本語](https://code.claude.com/docs/ja/claude-projects#limitations) / [English](https://code.claude.com/docs/en/claude-projects#limitations)):  
  スレッドを Remote Control 経由で自分のマシンで動かせるようになりました（ハイライト 5）
- [**Deploy managed settings**](./latest-detail.md#6-deploy-managed-settings) ([English](https://code.claude.com/docs/en/managed-settings#let-an-embedding-host-add-policy)):  
  埋め込みホストから渡される `strictKnownMarketplaces` と `blockedMarketplaces` の扱いが加わりました。残りは表の桁揃えとリンクの張り替えです
- [**Explore the .claude directory**](./latest-detail.md#7-explore-the-claude-directory) ([English](https://code.claude.com/docs/en/claude-directory)):  
  差分 52 行はすべて表の桁揃えとリンクの張り替えで、内容の変更はありません
- [**Customize keyboard shortcuts**](./latest-detail.md#8-customize-keyboard-shortcuts) ([日本語](https://code.claude.com/docs/ja/keybindings#text-fields) / [English](https://code.claude.com/docs/en/keybindings#text-fields)):  
  新しい節「Text fields」が加わり、`chat:sendNow` の説明が v2.1.281 の挙動に合わせて書き換わりました

## 軽微な更新

今回の差分は **3 ファイル**です。`git diff` の行数では `llms-full.txt` が 106,481 行（追加 54,598・削除 51,883）と大きく出ますが、これはページの差し替えで行の対応がずれたためで、**ページ単位で比べると追加 8,386 行・削除 5,697 行**です。見出しマップ（`en/claude_code_docs_map.md`）は 43 行（追加 38・削除 5）、`llms.txt` は 26 行（追加 13・削除 13）でした。`llms-full.txt` の総行数は **100,393 行から 103,108 行へ 2,715 行増え**、展開ページ数は **197 から 210** になりました（20 ページ追加・7 ページ削除）。既存のページで本文が変わったのは **79 ページ**で、そのうち 19 ページはリンクの張り替えだけです。changelog に積まれたのは **v2.1.282 の 1 本**です（詳細はハイライト 2）。

**新機能**

- **プラグインのドキュメント 20 ページの本文が公開されました**（詳細はハイライト 1 と新規追加ページ 1 を参照）
- **テキストフィールドでは、裸の文字にバインドを割り当てていても文字を入力できる**ことが、新しい節として説明されました（詳細は大幅更新ページ 8 を参照）— [日本語](https://code.claude.com/docs/ja/keybindings#text-fields) / [Customize keyboard shortcuts](https://code.claude.com/docs/en/keybindings#text-fields)
- **Claude apps gateway に `load_test_mode` ブロックが加わりました**。モデルプロバイダーを呼ばずにゲートウェイを負荷試験するモードで、プロバイダーへのリクエストを組み立てて署名したうえで送らずに捨て、定型の応答をストリームで返します。`reply_tokens`（既定 750）と `reply_seconds`（既定 9.5）で応答の大きさと長さを決め、`x-load-test-user` ヘッダーで開発者を最大 7 桁の番号で分けて数えられます。**必要な版は v2.1.283 以降と書かれていますが、今回の changelog の最新は v2.1.282 です**。開発者が使うゲートウェイでは決して有効にしないよう警告されています — [Claude apps gateway configuration](https://code.claude.com/docs/en/claude-apps-gateway-config#load_test_mode)
- **Agent SDK のトラブルシューティングページに、症状から該当ページを引く表が加わりました**。スキル・MCP・プラグイン・サブエージェント・ファイルのチェックポイント・フック・デプロイ・認証エラーごとに参照先が示され、ページ自体は CLI の起動・CLI プロセスの終了・構造化出力のエラーに範囲を絞りました（`llms.txt` の説明文は前回すでに変わっていました）— [Troubleshoot the Agent SDK](https://code.claude.com/docs/en/agent-sdk/troubleshooting)
- **フルスクリーン表示で、選択メニューをマウスホイールでスクロールできる**ようになりました（v2.1.280 以降）。短いウィンドウでの `/model` の一覧などが対象です — [Fullscreen rendering](https://code.claude.com/docs/en/fullscreen)

**機能改善**

- **OpenTelemetry の変数がプロジェクト設定とローカル設定から無視されるようになりました**（詳細はハイライト 3 を参照）— [All settings](https://code.claude.com/docs/en/settings-reference#variables-claude-code-ignores-in-env)
- **auto モードのサーバー側レビューが、接続の種類ごとに説明し直され、テレメトリを切ったセッションでも既定で使われるようになりました**（詳細はハイライト 4 を参照）— [日本語](https://code.claude.com/docs/ja/permission-modes#server-side-classifier-review) / [Choose a permission mode](https://code.claude.com/docs/en/permission-modes#server-side-classifier-review)
- **プロジェクトのスレッドを Remote Control 経由で自分のマシンで動かせるようになりました**（詳細はハイライト 5 を参照）— [日本語](https://code.claude.com/docs/ja/claude-projects#limitations) / [Let Claude coordinate ongoing work with Projects](https://code.claude.com/docs/en/claude-projects#limitations)
- **送信の即時実行（`Ctrl+Enter` / `Ctrl+X Ctrl+S`）の本文が、v2.1.281 の挙動に更新されました**。新しい節「When Claude Code sends what you queued」によると、キューの先頭に `!` のシェルコマンドがあればターンを中断します。それ以外は、Claude がシェルコマンドやサブエージェントなどバックグラウンドへ移せる作業をしていればそれを移してそのターンでメッセージを読み、応答を書いているだけかバックグラウンドへ移せない作業なら、ターンを中断して次にメッセージを送ります。「v2.1.281 より前は、どちらの場合も中断していた」と書かれています — [日本語](https://code.claude.com/docs/ja/interactive-mode#when-claude-code-sends-what-you-queued) / [Interactive mode](https://code.claude.com/docs/en/interactive-mode#when-claude-code-sends-what-you-queued)
- **`Ctrl+S` での退避と復元が、入力モードも戻す**ようになりました。退避した `!` のシェルコマンドは、シェルモードのまま戻ります — [日本語](https://code.claude.com/docs/ja/interactive-mode) / [Interactive mode](https://code.claude.com/docs/en/interactive-mode)
- **Remote Control の Trusted Devices が Pro・Max プランでも使えるようになりました**。Team・Enterprise では Owner が組織に対して有効にし、Pro・Max では各自が Cowork またはアカウントの設定ページで **Require trusted devices** をオンにします。組織での有効化の場所も、Claude Code の管理設定から **Organization settings > Capabilities > Remote sessions** に変わりました（見出しも「Team または Enterprise 組織で Trusted Devices を有効にする」に改称）— [日本語](https://code.claude.com/docs/ja/remote-control#trusted-devices) / [Continue local sessions from any device with Remote Control](https://code.claude.com/docs/en/remote-control#trusted-devices)
- **Amazon Bedrock の Mantle エンドポイントに必要な IAM アクションが明記されました**。Mantle には `bedrock-mantle:` プレフィックスの独自アクションがあり、`bedrock:` のアクションでは足りません。推論には `bedrock-mantle:CreateInference`、トークン数の計測には `bedrock-mantle:CountTokens` を付与します。`403` の読み方も、エラーが `bedrock-mantle:` のアクションを名指ししていればそのアクションを付与する、名指ししていなければモデルへのアクセスが許可されていない、の 2 通りに分けられました — [日本語](https://code.claude.com/docs/ja/amazon-bedrock#use-the-mantle-endpoint) / [Claude Code on Amazon Bedrock](https://code.claude.com/docs/en/amazon-bedrock#use-the-mantle-endpoint)
- **`/batch` が、各サブエージェントに「プルリクエストを開く」ではなく「変更を公開する」と書かれるようになり、git リポジトリの外でも `WorktreeCreate` フックがあれば動く**ことが本文に入りました（git リポジトリの外では v2.1.281 以降）。プルリクエストを開けないときは、何を公開したかを報告します（`commands`・`worktrees`・`best-practices`・`agents`）— [Run parallel sessions with worktrees](https://code.claude.com/docs/en/worktrees)
- **中断されたツール呼び出しの再開時の扱いが更新されました**。前のプロセスが終わったときに実行中だったツールは、「結果が記録される前に打ち切られた」と Claude に示され、もう一度実行する前に効果があったかを確かめるよう伝えられます（`CLAUDE_CODE_RESUME_INTERRUPTED_TURN` を設定していない場合）。v2.1.281 より前は、その呼び出しを会話から落とすか、ユーザーが中断したものとして見せていました — [Manage sessions](https://code.claude.com/docs/en/sessions)
- **プロンプト候補（prompt suggestions）のコストの説明が詳しくなりました**。候補を作るリクエストはセッションと同じモデルに送られ、プランの使用量上限か API コストに数えられます。プロンプトキャッシュを再利用するので大半はキャッシュ読み取りと少しの出力トークンで、`costs` にも同じ説明と、止める方法へのリンクが加わりました — [Manage costs effectively](https://code.claude.com/docs/en/costs)
- **テレメトリの帰属属性の伏せ字が、`OTEL_LOG_TOOL_DETAILS=1` で外せる**ことが明記されました。`agent.name`・`skill.name`・`plugin.name`・`mcp_server.name` が対象です — [Monitoring](https://code.claude.com/docs/en/monitoring-usage)
- **Agent SDK（Python）の説明が更新されました**。`user` は「ユーザー識別子」から「POSIX で Claude Code のサブプロセスを実行する OS ユーザー」に、`debug_stderr` は「SDK はこの値を無視する」に、`env` には `CLAUDE_AGENT_SDK_CLIENT_APP` で User-Agent にアプリを示せることが加わりました。`agent-sdk/permissions` には、Linux と macOS では認識されたサンドボックスの外で root や `sudo` のもと `bypassPermissions` で起動すると、最初のターンの前にクエリが失敗することが加わりました — [Agent SDK reference - Python](https://code.claude.com/docs/en/agent-sdk/python)
- **Claude apps gateway の IdP 停止時の説明が変わりました**。停止中のセッション更新は「失敗する」から「再試行を促す応答を受け、IdP が戻れば通る」になりました — [Claude apps gateway for Amazon Bedrock, Claude Platform on AWS, Google Cloud, and Microsoft Foundry](https://code.claude.com/docs/en/claude-apps-gateway)

**バグ修正**

- **v2.1.282 の修正 59 件のうち、本文ページに対応する記述が今回の差分で見つかったものは、ほぼありません。** 影響の大きいものを挙げます
- **API が復号できない Web 検索結果を履歴に持つ会話で、すべてのリクエストが 400 で失敗する問題を修正しました**（サードパーティのゲートウェイ経由で答えたターンなど）。`errors` の新しい節「Invalid encrypted_content in search_result block」はこの状況を説明しています
- **`Invalid data in redacted_thinking block` の API エラーで毎ターン失敗するセッションを修正しました**。Claude Code は会話の思考ブロックを落として 1 回だけ再試行します
- **`--continue`・`--resume` で続けた会話が、以前のメッセージを形を変えて送り直すケースをさらに修正しました**。API が Claude の以前の推論を捨てる原因になっていました。`/model` などのスラッシュコマンドを作業中に使ったときや、以前に提供した組み込みツールを外した `--tools` で再起動したときに、拡張思考が失われる問題も直りました
- **別の Claude Code プロセスがログインの更新中に閉じられたり強制終了されたりすると、最大 1 分間「another Claude Code process is refreshing it」でリクエストが失敗する問題を修正しました**
- **設定ファイルで、パターン途中に `:*` を含む Bash の許可ルールが読み飛ばされていた問題を修正しました**（`--allowedTools` では効いていました）。どこから設定しても効くようになり、起動時にどう一致するかの警告が出ます
- **管理設定の `permissions`・`autoMode`・`worktree`・`attribution` が、入れ子の値が 1 つ不正なだけで丸ごと無視されていた問題を修正しました**。残りの値は適用されます
- **Bash と PowerShell が、ディスククォータの満杯を「Exit code 1」の陰に隠し、一時領域に大きな出力ファイルを残していた問題を修正しました**
- **要約リクエストが拒否されると圧縮（compaction）が失敗していた問題を修正しました**。代替モデルで再試行します
- **vim モードの不具合をまとめて修正しました**。`>>` が空行をインデントする、回数付きの `r` が行より長いと文字を変える、`2J` が 1 行多く連結する、`.` の前の回数を無視する、などです

**その他**

- **v2.1.153〜v2.1.191 の古い版の注記 30 か所が、14 ページから外されました**。`mcp`（`claude mcp login` の v2.1.186・v2.1.191 など）、`sub-agents`（v2.1.153・v2.1.178・v2.1.186・v2.1.191）、`settings-reference`（`sandbox.credentials` の v2.1.187 など）、`cli-reference`・`commands`・`agent-teams`・`hooks`・`hooks-guide`・`checkpointing`・`github-actions`・`fullscreen`・`sandboxing`・`server-managed-settings`・`claude-platform-on-aws` です
- **クラウドセッションでプラグインを使う方法として「claude.ai アカウントで有効にすれば同期プラグインとして読み込まれる」と書いていた案内が、`cloud-environments`・`desktop`・`hooks`・`security-guidance` から削除されました**。`security-guidance` では代わりに、組織が管理設定で配布するプラグインの案内（`plugins/org`）へのリンクが置かれています
- **Claude Tag へのリンクが、`/docs/en/claude-tag` から `https://claude.com/docs/claude-tag` に変わりました**（`platforms`・`zero-data-retention`）
- **`channels-reference` から「承認済み許可リストは Anthropic が選定する」という記述が外れました**。研究プレビュー中は自作のチャネルが許可リストに載らないので開発フラグのままにする、という説明に変わっています
- **`github-enterprise-server` と `monitoring-usage` の組織設定のリンク先が、「Organization settings > Plugins」から「Organization settings > Plugins & skills」に変わりました**
- **`llms.txt` では、`desktop-quickstart` と `plugins/publish` の説明文が書き換わりました**。前者は「Claude デスクトップアプリをインストールし、Code タブを開いて、コンピューター上のプロジェクトフォルダーで最初の Claude Code セッションを始める」に、後者は公開先が「Anthropic のコミュニティマーケットプレイス」から「**Anthropic's directory**」になりました（本文はまだ旧名。ハイライト 1 を参照）
- **`llms.txt` の言語別インデックスのページ数が、おおむね 197 から 209 に増えました**（日本語は 196 → 209）。中国語は「Chinese（`cn.md`）」が「Simplified Chinese（`zh-cn.md`・210 ページ）」に、繁体字中国語は `zh-hant.md` が `zh-tw.md` に変わっています
- **見出しマップにだけ新しい見出しが入り、本文にはまだないものが約 35 件あります**。`settings-reference` の `availableModelsMatch`・`deniedModels`・`maxProseWidth`、`model-config` の `Block specific models or versions`、`terminal-config` の `Cap response width in wide terminals`、`agent-sdk/typescript` の `prewarm()`・`SpareProcess`、`mcp` の `Images in tool results`、`skills` の `Names reserved for synced skills`、`remote-control` の `"Couldn't verify your organization's policy for remote control"`、`errors` の 12 件、`troubleshoot-install` の 2 件（`claude.exe` missing after an update on Windows など）などです。逆に、マップから消えた `remote-control` の `Session URL reminders`・`Choose the right approach` は、**本文にはまだ残っています**
- **見出しマップ冒頭の自動生成スタンプが、2026年09月25日 03時24分49秒 UTC から 2026年09月26日 05時25分36秒 UTC へ進みました**

**参考リンクについて**: **日本語版の追従状況は、リンクするページごとに実測しました。反映を確認できたページにだけ日本語リンクを付けています。** 確認できたのは、`plugins/overview`（前回は 404）、`permission-modes`（v2.1.282 の記述まで反映）、`errors`（新しい 5 節あり）、`claude-projects`（制限事項に Remote Control の記述あり）、`interactive-mode`（`#when-claude-code-sends-what-you-queued` と v2.1.281 の注記あり）、`keybindings`（`#text-fields` あり）、`remote-control`（Trusted Devices の Pro・Max 対応あり）、`amazon-bedrock`（`bedrock-mantle:` の記述あり）、`plugin-evals`（`CI` 環境変数とエージェントが見つからない件の節あり）です。`claude-apps-gateway-config` の日本語版には `load_test_mode` がまだなく、`settings-reference` は取得した内容が途中で切れて確認できなかったため、いずれも英語版だけにしています。そのほかの未確認ページも英語版だけです。**changelog ページへのリンクは、本サマリの方針どおり付けていません。**

## 新着情報

**`whats-new/` 配下では 7 ページが動きましたが、いずれもリンク先の張り替えだけです。** 2026年の Week 14・17・19・23・32・33・37 の各ダイジェストで、`/docs/en/plugins`・`/docs/en/plugins-reference` などへのリンクが `/docs/en/plugins/` 配下の新しい URL に置き換わりました（たとえば Week 37 の「`--plugin-dir` にプラグインのフォルダーを渡す」のリンク先は `plugins/create#load-a-directory-or-archive-for-one-session` になりました）。ダイジェストの本文に変更はなく、**Week 38 はまだ追加されていません**。

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-09-24.md](./archives/latest/2026-09-24.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-09-24.md](./archives/latest-detail/2026-09-24.md)

<!--
base_commit: 9e4a9ca8dd012676f943d04b4ad641296ec601bb
head_commit: df1f117ca1144390ad3e12cf43bbdea20661d7d4
generated_at_full: 2026-09-26T15:07:47+09:00
-->
