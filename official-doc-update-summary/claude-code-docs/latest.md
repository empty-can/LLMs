---
対象期間: 2026年09月23日 〜 2026年09月24日
作成日: 2026-09-24
---

# Claude Code 公式ドキュメント更新サマリ

```markdown
**今回は取り込み 1 回ぶんの断面です**（前回は 7 日ぶんの集約でした）。差分は 3 ファイル・1,130 行（追加 810・削除 320）で、`llms-full.txt` は 100,218 行から 100,393 行へ **175 行増えました**。本文の変更はほぼ changelog の **v2.1.281（176 項目）** です。一方で `llms.txt` と見出しマップでは、**プラグインのドキュメントが独立したセクションに組み替えられ、索引の収録 URL が 197 件から 210 件に増えました**。ただし**新しいプラグインページの本文は、今回の `llms-full.txt` にはまだ入っていません**。

主要なものを以下に挙げます。

1. プラグインのドキュメントが独立した「Plugins」セクションに組み替えられた
2. AGENTS.md が Bedrock やテレメトリ無効のセッションでも読まれるようになった
3. v2.1.281 の 176 項目が積まれた
4. クラウドセッションの「research preview」表記が外れた
```

## ハイライト

1. [**プラグインのドキュメントが独立した「Plugins」セクションに組み替えられた**](./latest-detail.md#1-プラグインのドキュメントが独立したpluginsセクションに組み替えられた):  
  `llms.txt` で、これまで「Build with Claude Code」配下の h3 `Plugins`（3 ページ）、Administration 配下の h3 `Plugin distribution`（4 ページ）、Reference 配下の `plugins-reference` に分かれていたプラグイン関連ページが、**h2 `Plugins` という独立したセクションにまとめられました**。**7 つの h3 グループ・21 ページ**からなり、うち **20 ページは `/docs/en/plugins/` 配下の新しい URL** です。**旧 URL 7 件は索引から外れました**。**新しい 20 ページの本文は、今回の `llms-full.txt` にはまだ入っていません**（詳しくは新規追加ページ 1 を参照）
2. [**AGENTS.md が Bedrock やテレメトリ無効のセッションでも読まれるようになった**](./latest-detail.md#2-agentsmd-が-bedrock-やテレメトリ無効のセッションでも読まれるようになった):  
  前回ハイライト 3 で「`AGENTS.md` を直接読めない条件」として挙げた **「feature flag を取得しないセッション（Amazon Bedrock などのサードパーティプロバイダー、テレメトリ無効）」が、`memory`・`env-vars`・`feature-availability`・`glossary` の 4 ページから削除されました**。代わりに「**v2.1.281 より前は**、Bedrock 上やテレメトリ無効のセッションなど一部のセッションが `CLAUDE.md` しか読まなかった」という書き方になり、**該当する環境では v2.1.281 以降に更新するよう**案内されています。「インストール直後の初回セッション」という条件も、**「一部の場合に、v2.1.276 以前からアップグレードした直後の初回セッション」**へ狭まりました
3. [**v2.1.281 の 176 項目が積まれた**](./latest-detail.md#3-v21281-の-176-項目が積まれた):  
  changelog に積まれたリリースは **v2.1.281（2026年09月23日）の 1 本**で、項目数は **176** です。内訳は**修正 112・改善 33・変更 17・追加 13・削除 1**です。タグ付きは **`[Claude Tag]` 13・`[VSCode]` 6・`[Claude Code on the web]` 6・`Windows:` 2・`[Code Review]` 1**、残る **148 件が CLI 本体**です。**`"attribution": false` による帰属表示の一括非表示**、**Claude apps gateway の Bedrock アップストリームに `assume_role` と `guardrail` を追加**、**送信の即時実行（send now）がターンを中断しなくなった**こと、**セルフホストランナーでは `--system-prompt-file` への移行が必要**になったことなどが含まれます
4. [**クラウドセッションの「research preview」表記が外れた**](./latest-detail.md#4-クラウドセッションのresearch-preview表記が外れた):  
  `claude-code-on-the-web`・`web-quickstart`・`cloud-environments` の 3 ページ冒頭にある Note が、「クラウドセッションは Pro・Max・Team ユーザー向けの **research preview** です」から「クラウドセッションは Pro・Max・Team プランで **利用できます**」に書き換わりました。**Enterprise のプレミアムシート／Chat + Claude Code シートが対象**である点は変わっていません。head の `llms-full.txt` で、**クラウドセッションを research preview と呼ぶ箇所はなくなりました**

## 新規追加されたページ

- [**新しいプラグインページ 20 件は、索引と見出しマップにだけ載り、本文はまだ届いていない**](./latest-detail.md#1-新しいプラグインページ-20-件は索引と見出しマップにだけ載り本文はまだ届いていない) ([English](https://code.claude.com/docs/en/plugins/overview)):  
  `/docs/en/plugins/` 配下の **20 ページ**が `llms.txt` と見出しマップに加わりました。**`llms-full.txt` にはまだ 1 ページも入っていません**。そのため、ここでは**索引の説明文と見出しマップの見出し構成だけ**をもとに、各ページの範囲を一覧にしています。組み替えの全体像はハイライト 1 を参照してください

## 大幅に更新されたページ

*(今回の対象期間に大幅に更新されたリファレンス系ページはありません)*

**`llms-full.txt` で 50 行以上動いたのは `changelog`（179 行）だけ**で、その内容はハイライト 3 で扱っています。**changelog 以外で最も大きく動いたのは `memory` の 12 行**です（ハイライト 2）。

## 軽微な更新

今回の差分は **3 ファイル・1,130 行**（追加 810・削除 320）です。内訳は、見出しマップ（`en/claude_code_docs_map.md`）が 869 行（追加 577・削除 292）、`llms-full.txt` が 201 行（追加 188・削除 13）、`llms.txt` が 60 行（追加 45・削除 15）です。`llms-full.txt` の総行数は **100,218 行から 100,393 行へ 175 行増え**、展開ページ数は **197 のまま**、**本文が変わったページは 8 ページ**（`changelog`・`memory`・`claude-code-on-the-web`・`web-quickstart`・`cloud-environments`・`env-vars`・`feature-availability`・`glossary`）でした。changelog に積まれたのは **v2.1.281 の 1 本**です（詳細はハイライト 3）。

**新機能**

- **プラグインのドキュメントに 20 ページが新設されました**（詳細はハイライト 1 と新規追加ページ 1 を参照）
- **`"attribution": false` で、コミットと PR の帰属表示をすべて隠せるようになりました**（詳細はハイライト 3 を参照）
- **Claude apps gateway の Bedrock アップストリームに `assume_role` と `guardrail` が加わりました**（詳細はハイライト 3 を参照）
- **`claude plugin validate` が MCP サーバーの設定を検査するようになりました**（詳細はハイライト 3 を参照）
- **フルスクリーンモードの `/skills`・`/mcp`・`/plugin` の Installed 一覧にスクロールバーが付きました**。マウスが一覧の上にあるあいだ表示され、クリックやドラッグで操作できます
- **`[VSCode]` VS Code と JetBrains のパネルで、auto モードが課金される分類器リクエストにフォールバックしたときに Continue / Stop のプロンプトが出る**ようになりました。応答できなかった警告行を置き換えるものです
- **`[Claude Code on the web]` クラウドセッションのコンポーザーのモデルメニューに Fast mode のスイッチが付きました**。プランに fast mode が含まれ、選んだモデルが対応しているときに表示されます

**機能改善**

- **`AGENTS.md` の直接読み込みから、feature flag を取得するセッションに限るという制約が外れました**（詳細はハイライト 2 を参照）— [日本語](https://code.claude.com/docs/ja/memory#when-agents-md-support-is-unavailable) / [How Claude remembers your project](https://code.claude.com/docs/en/memory#when-agents-md-support-is-unavailable)
- **`env-vars` の「feature flag の取得を切ると使えない機能」から、`AGENTS.md` の行が削除されました**（ハイライト 2 に対応）— [Environment variables](https://code.claude.com/docs/en/env-vars#features-that-need-feature-flag-fetching)
- **`feature-availability` の「プロバイダーによって差がある機能」から、`CLAUDE.md memory` の行が削除されました**（ハイライト 2 に対応）— [Feature availability](https://code.claude.com/docs/en/feature-availability#features-available-on-every-provider)
- **`glossary` の `AGENTS.md` 項目から、「feature flag を取得するセッションで」という条件が外れました**（ハイライト 2 に対応）— [日本語](https://code.claude.com/docs/ja/glossary#agents-md) / [Glossary](https://code.claude.com/docs/en/glossary#agents-md)
- **クラウドセッションの位置づけが「research preview」から「利用可能」に変わりました**（詳細はハイライト 4 を参照）— [日本語](https://code.claude.com/docs/ja/claude-code-on-the-web) / [Use Claude Code in the cloud](https://code.claude.com/docs/en/claude-code-on-the-web)
- **送信の即時実行が、ターンを中断せず実行中のツールをバックグラウンドへ移すようになりました**（詳細はハイライト 3 を参照）
- **auto モードのサーバー側分類器が、読み取り専用やサンドボックス内のシェルコマンドもレビューするようになり、`CLAUDE_CODE_AUTO_MODE_SERVER` が Anthropic API 直結でも効くようになりました**（詳細はハイライト 3 を参照）
- **危険な `rm` の確認が、無人実行では 2 分でタイムアウトして拒否されるようになりました**（詳細はハイライト 3 を参照）
- **危険な `rm` の検査対象が広がりました**。シェル変数の後にトップレベルのディレクトリ名が続く削除、作業ディレクトリから導いた変数での削除、バックスラッシュだけの対象が加わりました
- **`--agents` が、`-p` と組み合わせたときに JSON ファイルのパスも受け付ける**ようになりました（インラインの JSON に加えて）。空の `prompt` も許されます
- **`/batch` が、git リポジトリの中でなくても、WorktreeCreate フックがエージェント用の worktree を用意する環境なら動く**ようになりました
- **起動と再開が速くなりました**。最初の画面が出る前に git の読み取り・起動時テレメトリ・Bedrock/Vertex のモデル更新チェックを行わなくなり、多数のファイルを読んだ長いセッションや、圧縮済みの非常に長いセッションの再開も速くなりました
- **「Prompt is too long」からの回復が改善されました**。非常に大きな最初のプロンプトが大半を占めるセッションでは、そのプロンプトを要約から外さず、単独で要約するようになりました
- **大きな CLAUDE.md に関する起動時の通知が、指示ファイルの合計も数える**ようになりました。中くらいのファイルが多数ある場合や @-インポートも検出されます
- **claude.ai から同期したスキルが、他のコマンドと名前がぶつからなければ短い名前で表示される**ようになりました（`anthropic-skills:<name>` ではなく）
- **auto モードの拒否メッセージが改善されました**。Claude が、拒否を正確なコマンドだけでなく、そのコマンドで得ようとした結果全体に及ぶものとして扱うようにしました

**バグ修正**

- **v2.1.281 の修正 112 件のうち、今回の差分で本文ページに対応する記述が見つかったものはありません。** 影響の大きいものを以下に挙げます。
- **`rm -rf "$(pwd)"` のように、コマンド置換の出力だけを対象にする再帰的な `rm` が、auto モードと `--dangerously-skip-permissions` モードで確認なしに実行されていた問題を修正しました**。Bash の許可ルールがあっても確認するようになりました（`CLAUDE_CODE_DISABLE_SUBSTITUTION_RM_PROMPT=1` で従来の挙動に戻せます）
- **NUL バイトを含む権限ルールがワイルドカードとして展開されていた問題を修正しました**。こうしたルールは何にも一致しなくなりました
- **`--setting-sources`（SDK の `settingSources`）が起動されるセッションに引き継がれていなかった問題を修正しました**。チームメイト、`/bg`、`claude agents` のセッション、`--worktree --tmux` が親と同じ制限で始まるようになりました
- **`claude --bg` が、ワークスペースの信頼確認を通っていないディレクトリでバックグラウンドセッションを始め、プロジェクトのフックを実行していた問題を修正しました**
- **再開したセッションが、以前のターンを形を変えて送り直していた問題を修正しました**。API が会話のそれまでの推論を捨てる原因になっていました。**非常に大きなセッションの再開で最後の数メッセージしか戻らない**問題や、**ツール呼び出し中に終わったセッションの再開**の扱いも直りました
- **プロキシやゲートウェイ経由のストリームの問題をまとめて修正しました**。ストリームがきれいに閉じられて応答が途中で切れたのに完了扱いになる、ストリームイベントの重複でツール呼び出しが 2 回走る、イベントが欠けて「Content block not found」で失敗する、の各問題です
- **`--max-turns` を無視してターンが無限に再試行される場合があった問題を修正しました**。モデルが解析できないツール呼び出しと出力上限での打ち切りを交互に繰り返したときに起きていました
- **Windows で、`$TMPDIR/…` に書き込む Bash コマンドが「Permission denied」で失敗する問題を修正しました**。同時に更新中の複数のセッションが互いの `claude.exe` のバックアップを消し、`claude.exe` が残らなくなることがあった競合も直りました
- **`[Claude Tag]` Slack のスレッド内の返信に Claude が恒久的に反応しなくなることがあったチャンネルの問題を修正しました**。影響を受けたチャンネルは、Claude への次の新しいメッセージで自動的に回復します

**その他**

- **見出しマップにだけ新しい見出しが入り、`llms-full.txt` の本文にはまだないものがあります。** `errors` の 5 項目（`The server returned no safety verdict`・`role 'system' must precede an 'assistant' message`・`Invalid encrypted_content in search_result block`・`Temp directory refused or cannot be created`・`Marketplace name is another spelling of a reserved name`）、`claude-apps-gateway-config` の `` `load_test_mode` ``、`keybindings` の `Text fields`、`remote-control` の見出し改称（`Enable Trusted Devices for your organization` → `Enable Trusted Devices for a Team or Enterprise organization`）、`agent-sdk/plugins` の見出し改称（`Using plugin skills` → `Use plugin skills`）です。このうち `role 'system' must precede` は、v2.1.280 の修正項目として changelog には既に出ていますが、`errors` の見出しとしてはまだ本文にありません
- **`llms.txt` の `agent-sdk/troubleshooting` の説明文が書き換わりました**。「エラーメッセージごとに原因と対処を引く」から「**Claude Code CLI が起動しない、CLI プロセスが終了する、成功した結果に構造化出力が付かない**ときに Agent SDK のエラーを直す」になりました。本文は今回動いていません
- **見出しマップの Administration 配下から h2 `Plugin distribution`（`plugin-marketplaces` など 4 ページ）が、Reference 配下から `plugins-reference` が、それぞれ見出し構成ごと消えました**（ハイライト 1 の組み替えに伴うもの）
- **見出しマップ冒頭の自動生成スタンプが、2026年09月23日 02時04分02秒 UTC から 2026年09月25日 03時24分49秒 UTC へ進みました**。**約 2 日 1 時間ぶん**です

**参考リンクについて**: **日本語版の追従状況は、リンクする節ごとに実測しました。反映を確認できた節にだけ日本語リンクを付けています。** 確認できたのは、`memory`（`#when-agents-md-support-is-unavailable`。「v2.1.281 より前は」の記述まで反映済み）、`glossary`（`#agents-md`。feature flag の条件が外れた版）、`claude-code-on-the-web`（冒頭 Note が「利用できます」に更新済み）の 3 ページです。**`plugins/overview` の日本語版は 404 でした**。`web-quickstart`・`cloud-environments`・`env-vars`・`feature-availability` と、ほかの新しいプラグインページ 19 件は未確認のため、安全側に倒して英語版だけにしています。**changelog ページへのリンクは、本サマリの方針どおり付けていません。**

## 新着情報

*(今回の対象期間に新着情報（週間ダイジェスト）の更新はありません)*

**`whats-new/` 配下のページは 1 行も動いていません。** `llms-full.txt` の差分に `whats-new` は一度も現れず、**Week 38 もまだ追加されていません**。

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-09-23.md](./archives/latest/2026-09-23.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-09-23.md](./archives/latest-detail/2026-09-23.md)

<!--
base_commit: 68860adc30f5a3b9e46aeef4cd6db8b1ccdc288e
head_commit: 9e4a9ca8dd012676f943d04b4ad641296ec601bb
generated_at_full: 2026-09-25T15:05:13+09:00
-->
