---
対象期間: 2026年08月31日 〜 2026年09月01日
作成日: 2026-09-01
---

# Claude Code 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
今回も 1 日分の取り込みですが、46 ページに差分があり、差分行は 2 ファイル合計 935 行（`llms-full.txt` 924 行 / ページ見出しマップ 11 行）です。`llms.txt` は前後で完全に同一（収録 URL 202 件・展開ページ数 191）で、無差分は 4 回連続、ページの新規追加・削除もありません。内容の中心は 2026年09月01日 付の大型リリース v2.1.257 で、changelog だけで 112 行増えました（本サマリで数える中では過去最大の 1 リリース）。新モデルの追加、既存設定の効かなくなる箇所、機能の削除が同時に入っています。なお今回は `whats-new/` ページに差分がなく、新着情報はありません。

主要なものを以下に挙げます。

1. Claude Fable 5.1 が加わり、`fable` エイリアスの解決先が Fable 5.1 に変わった
2. `bypassPermissions` をプロジェクト設定・ローカル設定に書いても効かなくなった
3. サブエージェントのモデルを環境変数で強制する仕組みが加わった
4. 時刻表示を制御する `timeFormat` と `timeZone` が新設された
5. 権限プロンプトの Ctrl+E コマンド説明が機能ごと削除された
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**Claude Fable 5.1 が加わり fable エイリアスの解決先が変わった**](#1-claude-fable-51-が加わり-fable-エイリアスの解決先が変わった):  
  1M コンテキストの `claude-fable-5-1` が追加され、`ANTHROPIC_DEFAULT_FABLE_MODEL` を設定していなければ `fable` エイリアスは Fable 5.1 を指すようになった。ユーザー設定に保存済みの `claude-fable-5` は初回起動時に自動でエイリアスへ書き換えられる。モデル設定ページの節名も `Work with Fable 5` から `Work with Fable` へ改称され、20 ページ以上で「Fable 5」表記が「Fable」へ一般化された。
2. [**bypassPermissions をプロジェクト設定とローカル設定から指定しても効かなくなった**](#2-bypasspermissions-をプロジェクト設定とローカル設定から指定しても効かなくなった):  
  `permissions.defaultMode` に `bypassPermissions` を書いても、`.claude/settings.json` と `.claude/settings.local.json` では無視され、セッションは Manual モードで始まるようになった（v2.1.257）。従来この制限は `auto` だけに掛かっていた。リポジトリに置いた設定が権限チェックを自分で外せなくなる変更で、フック・セッション再開・Agent SDK の各ページにも同じ注記が入った。
3. [**サブエージェントのモデルを環境変数で強制できるようになった**](#3-サブエージェントのモデルを環境変数で強制できるようになった):  
  `CLAUDE_CODE_SUBAGENT_MODEL_FORCE=1` を設定すると、定義や呼び出しが指名したモデルを無視して `CLAUDE_CODE_SUBAGENT_MODEL` が全サブエージェント・チームメイト・ワークフローエージェントに適用される（v2.1.257 以降）。前回サマリのハイライト 2 で扱った「環境変数が解決順の 3 番目へ降格した」変更の後日談にあたる。
4. [**時刻表示を制御する timeFormat と timeZone が新設された**](#4-時刻表示を制御する-timeformat-と-timezone-が新設された):  
  ターン終了時の所要時間メッセージやトランスクリプトビューアの時刻表記を、12 時間制・24 時間制・UTC 24 時間制、または strftime パターンで指定できるキーが加わった。`timeZone` には IANA タイムゾーン名を指定でき、システムのタイムゾーンと違う表示にできる（どちらも v2.1.257 以降）。
5. [**権限プロンプトのコマンド説明機能が削除された**](#5-権限プロンプトのコマンド説明機能が削除された):  
  Bash / PowerShell の権限プロンプトで `Ctrl+E` を押すとコマンドの解説とリスク判定が出る機能が、設定キー `permissionExplainerEnabled` ごと v2.1.257 で削除された。権限ページからは説明が丸ごと消え、キーバインドの `confirm:toggleExplanation` も表から外れている。
<!-- light:highlight-list:end -->

## 1. Claude Fable 5.1 が加わり fable エイリアスの解決先が変わった

changelog の **v2.1.257**（2026年09月01日）に「**Claude Fable 5.1（`claude-fable-5-1`）を追加。これが既定の Fable モデルになった**」というエントリが入りました。1M コンテキスト、100 万トークンあたり入力 $10 / 出力 $50、キャッシュ読み取りは 100 万トークンあたり $0.25 と記載されています。ただしモデル設定ページ側の記述はバージョンが噛み合っておらず、「**`ANTHROPIC_DEFAULT_FABLE_MODEL` を設定していない限り `fable` エイリアスは Fable 5.1 に解決する。v2.1.255 より前は Fable 5 に解決していた**」「**Fable 5.1 には Claude Code v2.1.255 以降が必要**」と、いずれも v2.1.255 を境界として書かれています。changelog には v2.1.253 から v2.1.256 までのエントリが 1 つも無く（v2.1.252 の次が v2.1.257）、この差の理由は公式ドキュメントからは読み取れません。本サマリでは両方の記述をそのまま併記します。

モデル設定ページの節は **`Work with Fable 5` から `Work with Fable` へ改称**され、2 モデルを並べる構成に書き直されました。Fable 5.1 と Fable 5 は Claude Code で最も高性能なモデルで、1 回の作業では終わらない規模のタスクに向き、長時間の自律実行を維持し、行動する前に調査し、小さいモデルより頻繁に自分の作業を検証する、という説明はそのままに、**Fable 5.1 が新しいリリースである**と加わりました。どちらも**どのプランでもどのプロバイダーでもアカウント種別の既定モデルではない**ため、明示的に選ぶ必要があります。Fable 5.1 は `/model fable` または `claude --model fable`、Fable 5 はモデル ID での指定（Anthropic API なら `/model claude-fable-5`、他プロバイダーではプロバイダーの Fable 5 モデル ID か `ANTHROPIC_DEFAULT_FABLE_MODEL` でのピン留め）です。

**保存済み設定の自動書き換え**も新設されました。ユーザー設定にモデルとして `claude-fable-5` または `claude-fable-5[1m]` が入っていて（v2.1.255 より前に `/model` のピッカーで Fable を選んだ場合など）、かつ Anthropic API へ直接つないでいる場合、v2.1.255 以降を初めて実行したときに Claude Code がその保存値を `fable` / `fable[1m]` エイリアスへ書き換え、起動時のモデル行に `(auto-updated)` が 1 度だけ表示されます。プロジェクト設定・ローカル設定・管理設定に入っている `claude-fable-5` はそのまま残されます。バージョン要件の Note も「**Fable 5.1 は v2.1.255 以降が必要。古いバージョンからのリクエストが失敗した場合は `Claude Code does not support this model` を参照。Fable 5 は v2.1.170 以降**」に書き改められ、ZDR での可用性は独立した節への参照になりました。

その **`Claude Code does not support this model` がエラーリファレンスに新設**されました。選んだモデルがリクエストを送る Claude Code のバージョンより新しいバージョンを必要とする状態で、**サーバーがモデルごとにチェックする**と明記されています。メッセージは `API Error: 400 Claude Code 2.1.219 does not support this model; version 2.1.255 or newer is required. Run 'claude update', or update the Claude desktop app, then try again.` です。対処は `claude update` かデスクトップアプリの更新のうえで新しいセッションをそのモデルで始めること、現在のセッションで作業を続けたい場合は `/model` で別のモデルへ切り替えることです。既存の `Model is not a recognized model id` の節にも「`claude-` で始まる完全な ID はこの**ローカル**チェックを通るが、**サーバー側がそのモデルに最低バージョンを課すことはありうる**」という但し書きが加わり、この新しい節へ誘導しています。

エイリアスと許可リストの扱いも整理されました。**`best`** は「組織がアクセスできる場合は Fable 5、それ以外は最新の Opus」から「**利用できる場合は最新の Fable モデル、それ以外は `opus` と同じモデル**」になりました。`availableModels` では、**バージョンプレフィックスが、そのプレフィックスにもう 1 セグメント足した後発のモデル ID にも一致する**ことが明記され、`claude-fable-5` は Fable 5 と Fable 5.1 の両方を、`claude-fable-5-1` は Fable 5.1 のみを許可します。あわせて、エイリアスの解決も「常に許可リスト内の最新版へ解決する」から「**通常のモデルが許可されていればそれに解決し、ブロックされているときだけ許可された最新版へ置換して通知を出す**」という書き方に改まりました（組織のモデル制限の節も同様）。

周辺の挙動差も明文化されています。**努力レベルのモデル既定の保持**（初回実行時のモデル既定を設定より優先する仕組み）は Fable 5・Opus 4.8・Opus 4.7 が対象で、**Opus 5 と Fable 5.1 にはこの保持が無い**と加わりました。安全分類器による自動フォールバックは「**Fable 5.1 と Fable 5**: 生物学のフラグは Opus 5、サイバーセキュリティのフラグは Opus 4.8 で再実行」となり、第三者プロバイダー側でのモデル認識も「モデル ID に `claude-fable-5` を含む」条件で両方が拾われます。**ゼロデータ保持（ZDR）の扱いは根本から書き換わり**、従来の「Fable 5 は ZDR 組織では利用不可」から「**Fable 5.1 と Fable 5 は既定でデータ保持を必要とする Covered Models であり、ZDR 組織やワークスペースが使えるかは Claude Code ではなく Covered Models のポリシーが決める**」になりました。アドバイザーでは、**Fable 5.1 をメインモデルにすると Fable 5 のアドバイザーも拒否される**（受け付けるのは Fable 5.1 のみ）ことが表に加わっています。環境変数には `VERTEX_REGION_CLAUDE_FABLE_5_1`（v2.1.255 で追加）が 1 行増えました。

なお changelog には「**Claude apps gateway のセッションでは `fable` と `best` は当面 Fable 5 に解決したままにする**（Fable 5.1 向けに設定されていないゲートウェイが拒否するため。使いたい場合は `/model` で Fable 5.1 を選ぶ）」という変更も入っています。

- [モデル設定 - Claude Code Docs (English)](https://code.claude.com/docs/en/model-config#work-with-fable)
- [エラーリファレンス - Claude Code Docs (English)](https://code.claude.com/docs/en/errors#claude-code-does-not-support-this-model)

## 2. bypassPermissions をプロジェクト設定とローカル設定から指定しても効かなくなった

設定リファレンスの **`permissions.defaultMode`** のスコープ行が、「`auto` はプロジェクト設定・ローカル設定から効かない」から「**`auto` と `bypassPermissions` はプロジェクト設定・ローカル設定から効かないので、`~/.claude/settings.json` に設定せよ**」に変わりました。あわせて「**v2.1.257 より前は `bypassPermissions` はどのファイルからでも効いていた**」と明記されています。VS Code 拡張が開始する会話ではユーザー設定・管理設定・`--settings` の値しか読まない、という既存の記述も同じ行に整理されました。

権限モードのページでは、セッションが開始するモードの決定順の 2 番目（設定ファイルの `permissions.defaultMode`）が 1 行から独立した段落に分けられ、**`auto` を `.claude/settings.json` か `.claude/settings.local.json` に書いた場合はその値が効かず、`~/.claude/settings.json` の `defaultMode` ではなく組み込みの既定が使われる**という従来の説明に、「**同じ 2 ファイルに `bypassPermissions` を書いた場合も効かず、セッションは Manual モードで始まる**」が加わりました。「プロジェクトごとに既定を決める」表の行も「ターミナルで開始するセッションは `auto` **と `bypassPermissions`** を除く全ての値を尊重する」に更新されています。`Shift+Tab` のサイクルに `bypassPermissions` が現れる条件も、「設定の `permissions.defaultMode: "bypassPermissions"`」から「**ユーザー設定・`--settings`・管理設定の** `permissions.defaultMode: "bypassPermissions"`」に限定されました。

同じ限定が周辺ページにも波及しています。フックリファレンスとフックのガイドでは、`setMode` で `bypassPermissions` を指定できる前提条件が「設定の `permissions.defaultMode`」から「ユーザー設定・`--settings`・管理設定の `permissions.defaultMode`」に変わり、あわせて 1 つの Note に詰め込まれていた「`disableBypassPermissionsMode` で無効化されている場合」「restricted モードで起動した場合」も独立した文へ分けられました。セッション管理のページの、再開時に引き継がれないモードの表でも同じ限定が入っています。Agent SDK（TypeScript）の `resolveSettings()` の注記は、「スナップショットは全ティアの `permissions.defaultMode` をそのまま返すため、**ライブセッションが無視する `'auto'` と `'bypassPermissions'` がプロジェクト設定・ローカル設定から入りうる**」に書き改められました。設定ページの「設定した値が効かないとき」にも「**そのファイルではその値を設定できない**」という項目が新設され、この 2 値と `--permission-mode` での回避が案内されています。

- [Claude Code 設定リファレンス - Claude Code Docs (English)](https://code.claude.com/docs/en/settings-reference#permissions-defaultmode)
- [権限モードを選択する - Claude Code Docs (English)](https://code.claude.com/docs/en/permission-modes#which-mode-a-session-starts-in)

## 3. サブエージェントのモデルを環境変数で強制できるようになった

環境変数 **`CLAUDE_CODE_SUBAGENT_MODEL_FORCE`** が加わりました（v2.1.257 以降）。`1` に設定すると、サブエージェント・チームメイト・ワークフローエージェントに 1 つのモデルを強制します。サブエージェントのページの「モデルを選択する」には、**定義や呼び出しがどのモデルを指名していても `CLAUDE_CODE_SUBAGENT_MODEL` のモデルで動かす**こと、**組み込みの Explore と Plan の定義も対象になる**ことが書かれました。例外は 2 つで、`/fork` による会話のフォークと、`model: inherit` を持つスキルをサブエージェントで動かす場合は、これまでどおりメイン会話のモデルで動きます。また `CLAUDE_CODE_SUBAGENT_MODEL` 自体を設定していない状態でこのフラグを立てた場合は、サブエージェント・チームメイト・ワークフローエージェントがメイン会話のモデルで動き、**組み込み Explore のモデル上限はそのまま残ります**。

これは前回サマリのハイライト 2 で扱った変更の続きにあたります。v2.1.251 で `CLAUDE_CODE_SUBAGENT_MODEL` が 4 段の解決順の 1 番目から 3 番目へ降格し、「呼び出しごとの `model` にもフロントマターの `model` にも負ける既定値」になったため、全サブエージェントを 1 つのモデルに固定する手段が失われていました。今回の変数はその手段を明示的なオプトインとして戻すものです。changelog の記述も「`CLAUDE_CODE_SUBAGENT_MODEL`（または未設定ならメインのモデル）を全サブエージェントに適用し、spawn ごと・エージェント定義ごとのモデル指定を無視する」となっています。

組み込みサブエージェントの説明にも反映されました。Explore の「メイン会話から継承し、Claude API では Opus で上限が掛かる」に「**この変数で `CLAUDE_CODE_SUBAGENT_MODEL` を強制した場合を除く**」が付き、Plan の「メイン会話から継承」にも同じ但し書きが入りました。`general-purpose` の行は解決順への参照に「**変数をサブエージェントに強制する方法**」が加わっています。エージェントチームのページには「`CLAUDE_CODE_SUBAGENT_MODEL_FORCE` はサブエージェントと同じくチームメイトにも適用される」の 1 文が、モデル設定ページと環境変数ページの `CLAUDE_CODE_SUBAGENT_MODEL` の行には「それを変えたい場合は `CLAUDE_CODE_SUBAGENT_MODEL_FORCE` を設定せよ」という誘導がそれぞれ加わりました。

- [カスタムサブエージェントの作成 - Claude Code Docs (English)](https://code.claude.com/docs/en/sub-agents#choose-a-model)
- [環境変数 - Claude Code Docs (English)](https://code.claude.com/docs/en/env-vars#variables)

## 4. 時刻表示を制御する timeFormat と timeZone が新設された

設定リファレンスに **`timeFormat`** と **`timeZone`** の 2 キーが加わりました（どちらも v2.1.257 以降、スコープは任意の設定ファイル）。ページ見出しマップにも同じ 2 見出しが今回追加されています。

**`timeFormat`** は、インターフェースに表示される時刻の書き方を選ぶキーです。対象として挙げられているのは、各ターンの所要時間メッセージ末尾の `done 6:05 PM` のような表示と、トランスクリプトビューアのタイムスタンプです。プリセットを選ぶだけなら `/config` の **Time format** から設定できます。値は `"auto"`（未設定と同じ。各時刻が組み込みの書式を保ち、所要時間メッセージはロケールに従う）、`"12-hour"`、`"24-hour"`、`"24-hour-utc"`（UTC の 24 時間制で分の後ろに `Z` が付く。例: `18:05Z`。このプリセットでは `timeZone` は無視される）、そして `"%H:%M"` のような **strftime パターン**です。**`%` を含む値はパターンとして扱われ**、プリセット以外でパターンでもない値は `"auto"` として読まれます。既定は `"auto"` です。

`/config` はプリセットしか提示しないため、strftime パターンを使うには設定ファイルに直接キーを書きます。`"%H:%M"` なら所要時間メッセージもトランスクリプトビューアも `18:05` の形になります。**トランスクリプトビューアではパターンがタイムスタンプ全体を置き換える**ため、そこに日付も出したい場合は日付ディレクティブを自分で足す必要があり、`"%Y-%m-%d %H:%M"` と書くと `2026-09-01 18:05` のように表示される、という例が添えられています。

**`timeZone`** は、インターフェースの時刻をシステムのタイムゾーン以外で表示するキーです。`"UTC"` や `"Europe/Dublin"` のような **IANA タイムゾーン名**を指定すると、`timeFormat` が制御する時刻がそのゾーンで表示されます。`timeFormat` が `"24-hour-utc"` の場合は時刻が UTC のままになり、このキーは無視されます。`/config` にはこのキーの行が無いため設定ファイルに書く必要があり、**認識できない名前を指定した場合はシステムのタイムゾーンにフォールバック**します。既定は未設定です。

- [Claude Code 設定リファレンス - Claude Code Docs (English)](https://code.claude.com/docs/en/settings-reference#timeformat)
- [Claude Code 設定リファレンス - Claude Code Docs (English)](https://code.claude.com/docs/en/settings-reference#timezone)

## 5. 権限プロンプトのコマンド説明機能が削除された

Bash / PowerShell の権限プロンプトで `Ctrl+E` を押すと、そのコマンドが何をするか・なぜ Claude が実行しようとしているか・何が起こりうるかをモデルが生成して **Low risk** / **Med risk** / **High risk** のラベル付きで表示する機能が、**v2.1.257 で削除されました**。changelog にも「Bash と PowerShell の権限プロンプトから Ctrl+E のコマンド説明を削除」の 1 行が入っています。

設定リファレンスの **`permissionExplainerEnabled`** の項目は、説明本文が Warning ブロックに置き換わりました。「**v2.1.257 で、Bash と PowerShell の権限プロンプトの `Ctrl+E` コマンド説明とともに削除された。現行バージョンではこのキーを設定しても効果は無い**」と述べたうえで、「v2.1.256 までは `Ctrl+E` でコマンドの説明を表示でき、このキーを `false` にするとそのショートカットを切れた」と過去形で書かれています。スコープ行にも「v2.1.256 以前について」という但し書きが付き、`true` / `false` の各値の説明と JSON の設定例は削除されました。全設定一覧の表の説明文も「シェルの権限プロンプトの Ctrl+E コマンド説明を切る」から「**v2.1.257 で、Ctrl+E コマンド説明とともに削除**」に差し替わっています。

権限ページからは、この機能を説明していた 2 段落（`Ctrl+E` の挙動と、`~/.claude.json` の `permissionExplainerEnabled` を `false` にする方法）が**まるごと削除**されました。キーバインドのページでも、`Confirmation` コンテキストの表から `confirm:toggleExplanation` の行が消え、代わりに表の外へ「**v2.1.257 より前は、既定で `Ctrl+E` に割り当てられた `confirm:toggleExplanation` アクションが、Bash と PowerShell の権限プロンプトでコマンドのモデル生成説明を表示していた**」という 1 文が置かれています。

- [Claude Code 設定リファレンス - Claude Code Docs (English)](https://code.claude.com/docs/en/settings-reference#permissionexplainerenabled)
- [キーバインド - Claude Code Docs (English)](https://code.claude.com/docs/en/keybindings#confirmation-actions)

## 新規追加されたページ

<!-- light:new-pages:start -->
（今回の対象期間に新規追加・削除されたドキュメントページはありません。`llms-full.txt` に展開されているページ数は前後とも 191 で、`llms.txt` は前後で 1 バイトも変わらず収録 URL も 202 件のままです。`llms.txt` の無差分は 4 回連続で、本文だけが 924 行動いた形になります）
<!-- light:new-pages:end -->

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
- [**設定リファレンス**](#1-設定リファレンス) ([English](https://code.claude.com/docs/en/settings-reference#all-settings)):  
  実質 93 行（追加 72・削除 21）で今回最大。新キー `timeFormat` / `timeZone`（ハイライト 4）、`permissionExplainerEnabled` の削除（ハイライト 5）、`permissions.defaultMode` の制限追加（ハイライト 2）、`allowManagedPermissionRulesOnly` の書き直しが中心。
- [**エージェントビュー**](#2-エージェントビュー) ([English](https://code.claude.com/docs/en/agent-view#the-supervisor-process)):  
  実質 90 行（追加 27・削除 63）で、今回唯一の大幅な削除超過。`LLM gateway` 節が新設された一方、スーパーバイザープロセスの解説が 25 段落ほどから 6 段落へ畳まれた。
- [**Agent SDK の TypeScript リファレンス**](#3-agent-sdk-の-typescript-リファレンス) ([English](https://code.claude.com/docs/en/agent-sdk/typescript#sdkmcpresourcelink)):  
  実質 89 行（追加 76・削除 13）。MCP ツールが返すリソースリンクを受け取る `SDKMcpResourceLink` の新設、思考トークンの内訳、`updateSettings()` の追加が主。
- [**モデル設定**](#4-モデル設定) ([English](https://code.claude.com/docs/en/model-config#work-with-fable)):  
  実質 83 行（追加 46・削除 37）。大半が Fable 5.1 の追加（ハイライト 1）で、残りはモデル許可リストのエイリアス解決の書き直し。
<!-- light:updated-pages:end -->

## 1. 設定リファレンス

実質 93 行（追加 72・削除 21）で、今回の差分の中では最大のページです。新キー `timeFormat` / `timeZone` はハイライト 4、`permissionExplainerEnabled` の削除はハイライト 5、`permissions.defaultMode` の制限追加はハイライト 2、`advisorModel` と `dialogExpiry` の Fable 表記の一般化はハイライト 1 で扱いました。ここではそれ以外の変更を挙げます。

大きいのは **`allowManagedPermissionRulesOnly` の書き直し**です。説明が「管理設定を権限ルールの唯一の**ソース**にする」から「管理設定を権限ルールの唯一の**設定ソース**にする」に変わり、1 段落だったものが 3 段落に分けられました。3 段落目が新規で、「**`--disallowedTools` のルールと、現在のセッションの `deny` / `ask` ルールは引き続き適用される。セッション途中で Claude Code が設定を再読み込みしたあともである。これらは制限しかしないので、管理ルールが与えたものを広げることはできない**」と述べ、「**v2.1.257 より前は、最初の設定再読み込みでこれらのコマンドラインおよびセッションのルールを落としていた**」と明記されました。changelog にも対応する修正エントリがあります。埋め込みホストから来る親設定を管理ティアとして扱う話も独立した段落へ切り出され、`true` の値の説明は列挙をやめて「管理設定が権限ルールの唯一の設定ソースになる」の 1 行に圧縮されています。この言い換えは管理設定・管理者セットアップ・Claude apps gateway 設定・権限・設定例の各ページにも展開されました。

`advisorModel` の説明では、Fable をアドバイザーに選ぶ前提が「まず `/model fable` で使用クレジットの同意を受け入れよ」から「**アカウントが使用クレジットの同意を要求する場合は**、まず `/model fable` で受け入れよ」と条件付きになりました。同意前に `/advisor` で Fable を選んでも保存されず `/model fable` を案内される、という挙動自体は変わっていません。

- [Claude Code 設定リファレンス - Claude Code Docs (English)](https://code.claude.com/docs/en/settings-reference#allowmanagedpermissionrulesonly)

## 2. エージェントビュー

実質 90 行（追加 27・削除 63）で、今回唯一の**削除が追加を上回るページ**です。中身は新設 1 節と、既存の長大な節の畳み込みです。

**新設されたのは `LLM gateway` 節**で、ページ見出しマップにも「Permission mode, model, and effort」配下の「Settings and provider」の次に 1 行追加されました。内容は、LLM ゲートウェイ経由でルーティングする場合は**シェルでエクスポートするのではなく設定ファイルの `env` ブロックに置け**、そうすればバックグラウンドセッションが他の設定と一緒に読む、というものです。シェルにだけエクスポートした場合に `ANTHROPIC_BASE_URL`（および一緒にエクスポートした `ANTHROPIC_CUSTOM_HEADERS` と認証情報）がバックグラウンドセッションへ届く条件は、**スーパーバイザー自身が同じゲートウェイをエクスポートしたシェルから起動されていること**を前提に、次の 3 ケースに限られると整理されました。①`←` または `/background` で自分のセッションをバックグラウンドにした場合、②今いるディレクトリへセッションをディスパッチした場合、③今いるディレクトリで停止済みセッションにアタッチまたは返信して起こした場合です。クラウドプロバイダーの前段に置いたゲートウェイの転送（`CLAUDE_CODE_USE_VERTEX=1` と `ANTHROPIC_VERTEX_BASE_URL`・`CLAUDE_CODE_SKIP_VERTEX_AUTH=1` の組など）と、**転送したゲートウェイはそのセッションの実行中プロセスにのみ適用され、決してディスクへ書かれない**ことも同節に移されています。

隣の `Settings and provider` 節も書き直され、「**バックグラウンドセッションはディスパッチ元シェルの `PATH` で動く**ので、実行するコマンドはターミナルと同じツールを見つける」が本文へ格上げされました（従来はスーパーバイザーの節にあった記述）。クラウドプロバイダーの選択（`CLAUDE_CODE_USE_BEDROCK` など）、`ANTHROPIC_DEFAULT_*_MODEL` エイリアス、`CLAUDE_CODE_EXTRA_BODY` も同じシェルから引き継ぐ、と 1 文にまとめられています。

一方、**`The supervisor process` 節は 25 段落ほどから 6 段落へ圧縮されました**。残ったのは、スーパーバイザーがバックグラウンドセッションを動かし続けるバックグラウンドサービスであるという定義と、セッションの状態別に何が起きるかの 4 項目（**作業中・入力待ち・アタッチ中**はプロセスが動き続ける／**終了して約 1 時間アタッチされない**とプロセスが停止され、`Ctrl+T` のピン留めで免除される／**予期せず終了**したら再起動されるが、`←` や `/background` でバックグラウンドにしたセッションを自分で `kill` した場合は停止扱い／**自動更新後**はスーパーバイザーが新バージョンへ再起動し、アイドルのセッションをバックグラウンドで移す）、ハンドオフの 1 段落、そして認証情報と設定の参照先を上記 2 節へ委譲する 1 段落です。

**畳まれて消えたのは**、事前ウォームしたワーカーの仕組み、再起動時の 3 つのセーフガードの内訳、worktree へ移動したセッションのトランスクリプト探索と `.orphaned-` サフィックスへのリネーム、`←` で作られた空行が約 5 分で消える話、スーパーバイザーがバージョンを遡る再起動をしない規則、そして `claude attach` が再起動中に待つ挙動（`Agent is updating to the new Claude Code…` のステータス行と約 60 秒でのタイムアウト）です。**このうち `.orphaned-` の話は消えたのではなく、Claude ディレクトリのページの自動削除対象の表に `projects/<project>/<session>.orphaned-<timestamp>-<suffix>.jsonl` と `.jsonl.superseded-<timestamp>` の行として移りました**。またメモリ不足時の説明には「他を止めても解放できなければアイドルのピン留めセッションも止める」が追記され、`Could not resolve authentication method` のトラブルシュートは「事前ウォームしたワーカーに認証情報のスナップショットを渡す」から「**バックグラウンドセッションはスーパーバイザーから認証情報を受け取る**」に言い換えられました。ゲートウェイ関連のリンク先も、この節から新しい `LLM gateway` 節へ張り替えられています（ページ内の v2.1.251 の互換性表と、LLM ゲートウェイ接続ページの参照の 2 か所）。

- [バックグラウンドエージェント - Claude Code Docs (English)](https://code.claude.com/docs/en/agent-view#llm-gateway)
- [バックグラウンドエージェント - Claude Code Docs (English)](https://code.claude.com/docs/en/agent-view#the-supervisor-process)

## 3. Agent SDK の TypeScript リファレンス

実質 89 行（追加 76・削除 13）です。生 41 行・実質 17 行の Python リファレンスとも内容が対応しています。

最大の追加は **`SDKMcpResourceLink` 型の新設**で、ページ見出しマップにも同じ見出しが加わりました。MCP ツールの結果に含まれる `resource_link` ブロック、つまり**サーバーが参照で返したファイル 1 件**を表す型です。フィールドは `uri` と `name`（必須）、`title` / `description` / `mimeType` / `size` / `annotations`（任意）で、`uri` か `name` が文字列でないブロックは捨てられ、型の合わない任意フィールドは省かれます。受け取り口は 2 つで、通常の完了時は `SDKUserMessage.tool_use_result` の **`resourceLinks`** 配列、長い MCP ツール呼び出しがバックグラウンドへ移された場合は `SDKTaskNotificationMessage` の **`resource_links`** です。Claude 自身は各リンクを `tool_result` ブロック内の 1 行のテキストとして受け取るため、**そのテキストをパースするのではなくこの配列を読んでレンダリングせよ**と案内されています。制限は共通で、リンクが無い結果とサブエージェントからの結果では省略され、1 結果あたり最大 50 件、シリアライズした JSON が 64 KiB に達した時点で追加を止めます。いずれも Agent SDK v0.3.257 以降が必要です。Python 側は `UserMessage.tool_use_result` の辞書に `resourceLinks` キーとして現れ（Python Agent SDK 0.2.150 以降 + Claude Code v2.1.257 以降。その SDK に同梱される CLI が要件を満たす）、`TaskNotificationMessage` にはデータクラスのフィールドが無いため `message.data.get("resource_links")` で読む、と明記されています。**`tool()` でインプロセスに定義したツールは Python では `resourceLinks` を生成しません**（SDK が CLI に渡す前に `resource_link` ブロックをテキストへ平坦化するため）。この点はカスタムツールのページにも同趣旨の追記が入りました。

2 つ目は**思考トークンの内訳**です。`Usage` に **`output_tokens_details`**（`BetaOutputTokensDetails`、現時点では `thinking_tokens` の 1 フィールド）が加わり、請求には使わず観測用に読むこと（`output_tokens` が正の合計で、`output_tokens - thinking_tokens` が非推論出力の近似）、数えているのはモデルが生成した生の推論でありレスポンス本文に返る思考テキストより長くなりうること（API が再トークン化して算出するため数トークンずれうる）、ストリーミング中の値は `message_start` のプレースホルダーなので結果メッセージの `usage` から読むこと、Claude Code が合成するアシスタントメッセージ（API エラーなど）では `null` になること、が箇条書きで説明されました。`ModelUsage` にも **`thinkingTokens`** が加わり、`outputTokens` に既に含まれるので足し合わせないこと、記録するバージョンでターンが動くまで存在しないため以前のバージョンで始めたセッションを再開すると部分的な数になること（Agent SDK v0.3.257 以降）が書かれています。Python 側の `ModelUsage` は TypedDict に宣言が無いため `.get()` で読め、とされました。`SDKThinkingTokensMessage` の説明も、最終的な数を `usage.output_tokens` ではなく `usage.output_tokens_details.thinking_tokens` から読む形に改まっています。`AgentOutput` の `usage.output_tokens_details` には「**すべての階層が任意なので `usage.output_tokens_details?.thinking_tokens ?? 0` のように両方をガードせよ**」という注意が加わりました。

`Query` オブジェクトにもメソッドが増えました。**`updateSettings(source, settings)`** は、プロジェクトのローカル設定ファイル `.claude/settings.local.json` に設定をマージし、次のリクエストから有効になります。受け付けるのは `source: 'localSettings'` のみ、キーは許可リスト制で**現時点では `outputStyle` だけ**、値は文字列のみで、キーの削除には対応しません。リモートトランスポートと、`settingSources` が `local` を含まないセッションでは reject されます（TypeScript SDK v0.3.257 以降。同版が Claude Code v2.1.257 を同梱）。**`getContextUsage(opts?)`** には `detail?: 'summary' | 'full'` が加わり、既定の `'full'` は各カテゴリをトークンカウント API のリクエストで数え、`{ detail: 'summary' }` を渡すと直前のレスポンスの usage とローカルの推定から答えを作ります。後者では**トークンカウントのリクエストが一切出ない**代わりに、カテゴリごとの数値は概算になります（Agent SDK v0.3.257 以降）。

MCP サーバー操作の細部も詰められました。**`reconnectMcpServer()` と `toggleMcpServer()` の名前解決**が明文化され、名前が `.mcp.json` や `~/.claude.json` の設定ファイルエントリとも一致する場合は、**`mcpServers` オプションや `setMcpServers()` で設定したサーバーの方を優先**します（Claude Code v2.1.257 以降）。`setMcpServers()` の結果については、**`added` が接続に失敗したサーバーも含む**ようになり、そのサーバーは `errors` にも現れて `mcpServerStatus()` では `failed` 行になる、と加わりました（v2.1.257 より前は接続試行が例外を投げたサーバーが `errors` にしか現れませんでした）。

最後にウォッチドッグの既定値です。**`CLAUDE_ASYNC_AGENT_STALL_TIMEOUT_MS` の対象が `run_in_background` のサブエージェント限定ではなくなり**、全サブエージェントのストール監視になりました。既定値も、ストリームウォッチドッグが有効なら `CLAUDE_STREAM_IDLE_TIMEOUT_MS` + 5 分（同変数を上げていなければ `600000`）、無効なら `600000` に変わっています（v2.1.257 より前は常に `600000`）。ストール時はサブエージェントを中断して親へ報告し、**バックグラウンドサブエージェントの場合はさらにタスクを失敗としてマークし部分結果を添える**、と分けて書かれました。ストリームウォッチドッグ側には、`ANTHROPIC_BASE_URL` の先のゲートウェイがキープアライブでレスポンスを開いたままにしている間、`includePartialMessages` を設定したホストには **`ping` のストリームイベントが届き続ける**ので、沈黙とみなしてタイムアウトさせず生存信号として読め、という段落が加わりました（v2.1.257 より前は最後の実イベントから 5 分でフレームが止まっていました）。関連して `tool_progress` のハートビートも、**フォアグラウンドの Agent ツール呼び出しでも出るようになり**（v2.1.257 より前は出ませんでした）、`subagent_type` は「ハートビート以外の `tool_progress`」に付くと限定され、再試行インジケーターを消す条件も「`subagent_retry` **も `heartbeat: true` も無い**フレームが来たとき」に改められています。ホスティングのページの制約表からも「バックグラウンドサブエージェントに限り」という限定が外れました。

- [Agent SDK TypeScript リファレンス - Claude Code Docs (English)](https://code.claude.com/docs/en/agent-sdk/typescript#sdkmcpresourcelink)
- [Agent SDK TypeScript リファレンス - Claude Code Docs (English)](https://code.claude.com/docs/en/agent-sdk/typescript#usage)

## 4. モデル設定

実質 83 行（追加 46・削除 37）です。生の差分は 101 行ですが、差の一部は表の桁揃えでした。内容の大半は Fable 5.1 の追加とそれに伴う節の改称・表記の一般化で、ハイライト 1 で扱いました。ここではそれ以外を挙げます。

**モデル許可リストのエイリアス解決の説明が書き直されました**。従来は「Anthropic API と Claude Platform on AWS では、`opus` などのファミリーエイリアスは**許可リストが許す中で最新の版に解決する**」でしたが、今回は「**エイリアスは、許可リストがそのモデルを許していれば通常のモデルに解決する。許可リストがそれをブロックしている場合に限り、Claude Code はファミリーの中で許可された最新版に置換し、要求されたモデルと置換先の両方を挙げた通知を出す**」という 2 段階の書き方になりました。`["sonnet", "claude-opus-4-6"]` の例で `/model opus` と `--model opus` が Opus 4.6 を選ぶ、という結論は変わりません。組織のモデル制限の節にも同じ言い換えが入っています。あわせて、**バージョンプレフィックスが後発のモデル ID にも一致する**規則（ハイライト 1 参照）が `availableModels` の説明に加わりました。

組織デフォルトモデルの節では、アカウントで利用できないモデルが組織デフォルトに設定されている場合の例示から **ZDR での Fable 5 という具体例が外され**、「**そもそもアカウントで利用できない組織デフォルトはスキップされる**」という一般論だけが残りました。ZDR での Fable の扱いが Covered Models のポリシー側へ移ったことに対応する変更です。

拡張コンテキストの節では、Anthropic API での 1M ウィンドウの記述が「Fable 5・Sonnet 5・Opus 4.7 以降は**常に** 1M ウィンドウで動く」から「Fable 5.1・Fable 5・Sonnet 5・Opus 4.7 以降は**既定で** 1M ウィンドウで動く」に緩められました。環境変数の表では `CLAUDE_CODE_SUBAGENT_MODEL` の行に `CLAUDE_CODE_SUBAGENT_MODEL_FORCE` への誘導が加わっています（ハイライト 3 参照）。

- [モデル設定 - Claude Code Docs (English)](https://code.claude.com/docs/en/model-config#model-aliases)
- [モデル設定 - Claude Code Docs (English)](https://code.claude.com/docs/en/model-config#restrict-model-selection)

## 軽微な更新

<!-- light:minor-updates:start -->
今回も 1 日分の取り込みで、`llms-full.txt` に差分のあったページは 46、差分行は 2 ファイル合計 935 行（`llms-full.txt` 924 行 / ページ見出しマップ 11 行）です。**`llms.txt` には差分がなく**、収録 URL は 202 件、展開ページ数も前後とも 191 で、ページの新規追加・削除はありません（無差分は 4 回連続）。**大幅更新に入れる基準は前回同様「実質の差分 50 行以上 かつ 内容の変更を伴うこと」**とし、設定リファレンス（実質 93 行）、エージェントビュー（同 90 行）、Agent SDK の TypeScript リファレンス（同 89 行）、モデル設定（同 83 行）の 4 ページを該当としました。次点はエラーリファレンスの 26 行、VS Code の 25 行、環境変数の 23 行です。**実質最大は changelog の 112 行（全て追加）ですが、changelog は個別ページとして扱わず本節で扱います**（リンク不使用ポリシーのため）。本サマリで「実質 N 行」と書いた値は、各行の連続空白と連続ハイフンを潰したうえで数え直した概算です。表の桁揃えの差が大きいページでは生の差分と乖離し、たとえば VS Code は生 51 行に対し実質 25 行、Claude ディレクトリは生 39 行に対し実質 1 行でした。

**changelog には v2.1.257（2026年09月01日）と v2.1.258（同日）の 2 件が加わりました**。v2.1.257 は本体 94 件（追加 8・修正 63・改善 11・変更 11・削除 1）と VS Code 拡張分 10 件（追加 4・修正 4・変更 2）の計 104 件からなる大型リリースで、v2.1.258 はその回帰を含む 2 件の修正のみです。**なお changelog には v2.1.253 から v2.1.256 までのエントリが 1 件もありません**（v2.1.252 の次が v2.1.257）。一方でドキュメント本文は Fable 5.1 の要件などで v2.1.255 に繰り返し言及しており、この食い違いの理由は公式ドキュメントからは読み取れません。以下では 2 リリースを混在させるため、changelog 由来の項目には版を併記します。

**今回のページ見出しマップの差分は、生成時刻の更新（2026年09月01日 03:07 UTC から 2026年09月02日 02:03 UTC）と 5 件の見出し変更だけ**で、いずれも本文が同時に到着しています。前回サマリのような「見出しだけ先に現れて本文が届いていない」持ち越しは今回ありません。内訳は、エージェントビューへの `LLM gateway` 追加、エラーリファレンスへの `Claude Code does not support this model` 追加、設定リファレンスへの `timeFormat` / `timeZone` 追加、モデル設定の `Work with Fable 5` → `Work with Fable`（および配下の `Fable 5 and usage credits` → `Fable and usage credits`）改称、Agent SDK（TypeScript）への `SDKMcpResourceLink` 追加です。

なお本サマリの参考リンクは全て英語版のみです。今回の変更に日本語版が追従していないためで、本サマリの作成時点で公開中の日本語版ページを実際に取得して確認したところ（本リポジトリに取り込んである `ja/` のスナップショットではなく、`code.claude.com` のライブページを参照しています）、**日本語版のモデル設定ページには Fable 5.1 の記述が一切無く節見出しも `work-with-fable-5` のまま**、**日本語版の権限モードページには「セッションが開始するモード」の節自体が無く、`bypassPermissions` の制限も auto モードの対応モデルへの Fable 追加も反映されていない**、**日本語版のサブエージェントページには `CLAUDE_CODE_SUBAGENT_MODEL_FORCE` が存在しない**ことを確認しました。日本語版の設定リファレンスのページはそもそも存在せず（日本語版は旧構成の `settings` を参照しています）、こちらもリンクできません。他のページは個別には確認していませんが、いずれも直近 1〜2 日の変更であるため未追従とみなし、安全側に倒して英語版のみを載せています。

**新機能**

- Claude Fable 5.1（`claude-fable-5-1`）が既定の Fable モデルとして追加されました（詳細はハイライト 1 参照）— [English](https://code.claude.com/docs/en/model-config#work-with-fable)
- 時刻表示を制御する `timeFormat` と `timeZone` が新設されました（詳細はハイライト 4 参照）— [English](https://code.claude.com/docs/en/settings-reference#timeformat)
- `CLAUDE_CODE_SUBAGENT_MODEL_FORCE` が新設されました（詳細はハイライト 3 参照）— [English](https://code.claude.com/docs/en/sub-agents#choose-a-model)
- auto モードに **Containment Escape ルール**が加わり、クラウドのメタデータ認証情報の取得、エグレス回避、テナントをまたぐ到達が、環境で想定済みと示されていない限り自動承認されなくなりました（v2.1.257）
- auto モードで**作業ディレクトリ外のファイルを初めて読む前に 1 回だけ確認プロンプト**が出るようになり、そうした読み取り自体をブロックする選択肢（`permissions.blockReadsOutsideWorkingDirectories`）が加わりました（v2.1.257）
- `/effort` に `s` が加わり、`/model` と同じく**現在のセッションだけ**努力レベルを変えられるようになりました（v2.1.257）
- `/doctor` が、強制終了されたセッションが残した**古いサンドボックスのマスクファイル**について警告を出すようになりました（v2.1.257）
- ゲートウェイのモデル探索（`CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY`）で、**ゲートウェイが供給する `description`** を `/model` ピッカーのエントリに表示できるようになりました。`description` を持たないエントリは従来どおり `From gateway` と表示されます（v2.1.257）
- 環境変数 **`CLAUDE_CODE_DISABLE_CFC_PROMPT`** が加わりました。`1` に設定すると、[Claude in Chrome](https://code.claude.com/docs/en/chrome) のブラウザツールは使えるままで、システムプロンプトの Chrome 節と `/claude-in-chrome` バンドルスキルだけを外します。独自のブラウザ向け指示を持つ埋め込みホスト向けです（v2.1.257 以降）— [English](https://code.claude.com/docs/en/env-vars#variables)
- VS Code 拡張のプロンプトボックス下部に**モデルのピル**が加わり、クリックでモデルピッカーが開くようになりました。ピッカーには主要一覧に載らないモデルを集めた **More models** ページと、対応モデルでは **Effort** 行が付きます（v2.1.257 以降）— [English](https://code.claude.com/docs/en/vs-code#use-the-prompt-box)
- VS Code 拡張のコマンドメニューの Customize 節に **Slash commands** が加わりました。`/usage` や `/remote-control` などをフィルターボックス付きのダイアログで一覧・実行できます（プロンプトボックスで `/` を打つ従来のインライン補完も残ります。v2.1.257 以降）— [English](https://code.claude.com/docs/en/vs-code#use-the-prompt-box)
- VS Code 拡張の同じ Customize 節から **Output styles** で出力スタイル（カスタムスタイルを含む）を選べるようになりました。保存先はターミナルのメニューと同じ `.claude/settings.local.json` です（v2.1.257 以降）— [English](https://code.claude.com/docs/en/output-styles#change-your-output-style)
- VS Code 拡張に、アクティブなタブのセッションを対象とする 3 つのコマンド **Rename Session Tab** / **Add Session Tab to Group** / **Mark Session as Unread** が加わりました。いずれもタブの右クリックメニューにも出ます（v2.1.257 以降）— [English](https://code.claude.com/docs/en/vs-code#vs-code-commands-and-shortcuts)
- VS Code 拡張のセッション一覧パネルに、**ACCOUNT & USAGE** と **SESSION MANAGER** の折り畳み可能なセクション見出しが加わり、アカウントのメールアドレス、使用量メーター、使用量ダイアログを開く View details リンクが載りました（v2.1.257）
- VS Code 拡張のセッション一覧の **Ungrouped** 節にも折り畳みトグルが加わりました（v2.1.257）
- MCP ツールが参照で返したファイルを受け取る `SDKMcpResourceLink` 型と `resourceLinks` / `resource_links` が Agent SDK に加わりました（詳細は大幅更新 3 参照）— [English](https://code.claude.com/docs/en/agent-sdk/typescript#sdkmcpresourcelink)
- Agent SDK の `Query` に `updateSettings()` が加わり、`getContextUsage()` が `detail` オプションを受け取るようになりました（詳細は大幅更新 3 参照）— [English](https://code.claude.com/docs/en/agent-sdk/typescript#query-object)
- Agent SDK の使用量に思考トークンの内訳（`output_tokens_details.thinking_tokens` と `ModelUsage.thinkingTokens`）が加わりました（詳細は大幅更新 3 参照）— [English](https://code.claude.com/docs/en/agent-sdk/typescript#usage)
- 環境変数に `VERTEX_REGION_CLAUDE_FABLE_5_1`（Google Cloud の Agent Platform での Fable 5.1 のリージョン上書き、v2.1.255 で追加）が加わりました — [English](https://code.claude.com/docs/en/env-vars#variables)
- Claude ディレクトリの自動削除対象の表に、**Claude Code が上書き・削除せずに退避した過去のトランスクリプト**（`projects/<project>/<session>.orphaned-<timestamp>-<suffix>.jsonl` と `projects/<project>/<session>.jsonl.superseded-<timestamp>`）の行が加わりました。セッションピッカーには現れません — [English](https://code.claude.com/docs/en/claude-directory#cleaned-up-automatically)

**機能改善**

- `allowManagedPermissionRulesOnly` の説明が書き直され、`--disallowedTools` とセッションの `deny` / `ask` ルールが設定再読み込み後も残ることが明記されました（詳細は大幅更新 1 参照）— [English](https://code.claude.com/docs/en/settings-reference#allowmanagedpermissionrulesonly)
- `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB` が剥がす対象が広がりました。Anthropic とクラウドプロバイダーの認証情報に加え、**Claude Code が認証情報と認識するその他の変数**と、**パッケージレジストリの URL に埋め込まれた認証情報**も対象になります。サンドボックスのページの記述も同じく「Anthropic とクラウドプロバイダーの認証情報」から「認証情報」へ一般化されました — [English](https://code.claude.com/docs/en/env-vars#variables)
- MCP の `headersHelper` 実行時に環境から除去される変数の説明が、`TOKEN` / `SECRET` / `PASSWORD` / `PASSWD` / `PASSPHRASE` / `KEY` / `AUTH` / `COOKIE` / `PAT` / `DSN` / `CREDENTIAL` / `CREDENTIALS` のアンダースコア区切りパーツ一致という厳密な列挙から、「**認証情報らしい名前**（大文字小文字を問わず `TOKEN`・`SECRET`・`PASSWORD`・`KEY`・`AUTH` などを含む名前）」という要約的な書き方に改められました — [English](https://code.claude.com/docs/en/mcp#use-dynamic-headers-for-custom-authentication)
- ZDR での Fable の可用性が、Claude Code 側の一律禁止から **Covered Models のポリシー**による判断に書き換えられました（詳細はハイライト 1 参照）— [English](https://code.claude.com/docs/en/zero-data-retention#model-availability-under-zdr)
- `CLAUDE_ASYNC_AGENT_STALL_TIMEOUT_MS` が全サブエージェントのストール監視になり、既定値がストリームウォッチドッグの設定に連動するようになりました（詳細は大幅更新 3 参照）— [English](https://code.claude.com/docs/en/env-vars#variables)
- Agent SDK のホスティングのページの制約表からも、ストールウォッチドッグの「バックグラウンドサブエージェントに限り」という限定が外れました — [English](https://code.claude.com/docs/en/agent-sdk/hosting#known-limitations)
- Agent SDK のエージェントループのページで、`"xhigh"` の推奨対象が「Fable 5・Opus 4.7 以降・Sonnet 5」という列挙から「**対応するモデル**」への参照に置き換えられました — [English](https://code.claude.com/docs/en/agent-sdk/agent-loop#effort-level)
- アドバイザーの対応メインモデルの一覧が「Opus 4.6 以降・Sonnet 4.6 以降・Haiku 4.5。Fable 5 も v2.1.170 以降で該当」から「**Fable、Opus 4.6 以降、Sonnet 4.6 以降、Haiku 4.5**」に整理され、どのアドバイザーを受け付けるかは対応表への参照になりました — [English](https://code.claude.com/docs/en/advisor#choose-an-advisor-model)
- CLI リファレンスの `--model` の説明が、エイリアスの列挙から[モデルエイリアス](https://code.claude.com/docs/en/model-config#model-aliases)の節へのリンクに改まりました — [English](https://code.claude.com/docs/en/cli-reference#cli-flags)
- 設定ページの「設定した値が効かないとき」の導入が「同じキーを他の何かが設定しているか、ファイルが読み込まれていない」から「**同じキーを他の何かが設定しているか、そのファイルではその値を設定できないか**、ファイルが読み込まれていない」に広がり、対応する項目が 1 つ増えました（詳細はハイライト 2 参照）— [English](https://code.claude.com/docs/en/settings#a-value-you-set-is-ignored)
- VS Code 拡張のセッション履歴で、**Delete session が Archive session に変わりました**。アーカイブしたセッションは一覧の末尾の **Archived sessions** グループに移り、**Unarchive session** で戻せます。v2.1.257 より前の Delete session は復元手段が無く、当時削除したセッションはアップグレード後に Archived sessions に現れます — [English](https://code.claude.com/docs/en/vs-code#resume-past-conversations)
- VS Code 拡張の `/usage` について、**claude.ai へのサインインが必要なため第三者プロバイダーでは提供されない**ことが明記されました。あわせて、第三者プロバイダーでは使用量トラッキング・音声ディクテーション・クラウドセッションの Web タブといった claude.ai アカウントを要する機能を拡張が提示せず、以前の `/login` で残った claude.ai のサインインもどのリクエストにも使われない、という段落が新設されています — [English](https://code.claude.com/docs/en/vs-code#check-account-and-usage)
- VS Code 拡張の **Enable Remote Control for all sessions** トグルが、**既に開いているセッションにも適用される**ようになりました（オフにすると開いているセッションは切断されます）。v2.1.257 より前は変更後に開始したセッションにしか効きませんでした — [English](https://code.claude.com/docs/en/vs-code#use-the-prompt-box)
- VS Code 拡張のセッションのグループ化に、**エディタタブから追加する経路**（コマンドパレットの Claude Code: Add Session Tab to Group、またはタブの右クリック）が加わりました（v2.1.257 以降）— [English](https://code.claude.com/docs/en/vs-code#organize-sessions-into-groups)
- バックグラウンドセッションが設定・プロバイダー・`PATH`・ゲートウェイをどこから受け取るかの説明が再編されました（詳細は大幅更新 2 参照）— [English](https://code.claude.com/docs/en/agent-view#llm-gateway)
- Agent SDK の `setMcpServers()` の結果で、接続に失敗したサーバーも `added` に載るようになりました。`reconnectMcpServer()` / `toggleMcpServer()` の名前解決も明文化されています（詳細は大幅更新 3 参照）— [English](https://code.claude.com/docs/en/agent-sdk/typescript#query-object)
- `--effort` が、新しいモデルの**モデル既定の努力レベルの保持を解除する範囲**を「恒久的」から「そのセッションだけ」に変えました。あわせて、Remote Control セッションについて claude.ai 側で選んだ努力レベルが保持期間中も適用されるようになりました（v2.1.257）
- MDM や `managed-settings.json` に置いた `policyHelper` が、起動時にキャッシュ済みのサーバー管理設定に隠されていた場合、**取得がその設定の削除を報告した時点で**実行（または終了）するようになりました（従来は次回起動時。v2.1.257）
- `managedSourcesBehavior: "merge"` が、`sandbox.credentials.awsPairs` と `sandbox.ripgrep` については各ソースの値を合成せず、**それを設定している最上位の管理ソースからまるごと取る**ようになりました（v2.1.257）
- ゲートウェイのモデル探索（`CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY=1`）が、`CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` を設定していても実行されるようになりました。問い合わせ先が自分のゲートウェイだけであるためです（v2.1.257）
- `claude --resume <session-id> --bg` が、そのセッションを動かしているものが無い場合に**そのセッション自身の ID で継続**するようになりました。従来は黙ってコピーを開始していましたが、コピーになる場合はその旨が告知されます（v2.1.257）
- `/btw` の履歴のたどり方が `←` / `→` から **`Shift+←` / `Shift+→`（または `[` / `]`）**に変わり、最近の側面質問とライブの回答の間を行き来できるようになりました（v2.1.257）
- `--add-dir`・`/add-dir`・`additionalDirectories` が、**ネットワークパス（UNC 共有や `/net/<host>` の automount）を触る前にメッセージ付きで拒否**するようになりました。Windows ではマップされたドライブレターを使います（v2.1.257）
- Claude apps gateway のサインインとトークン更新のリクエストが、**ゲートウェイのピン留めされた TLS 証明書を検証**するようになりました（管理設定の取得では既に行っていた挙動。v2.1.257）
- Cowork と claude.ai のクラウドセッションで、**自分のものではないアーティファクトの読み取りは auto モードでも必ず確認を求める**ようになりました（v2.1.257）
- レンダリング性能が改善されました。長い会話でのターンごとの再描画作業が減り、返答が伸びてもストリーミングが遅くならず、バックグラウンドエージェントの更新が画面全体を再描画しなくなりました（v2.1.257）
- キー入力ごとの描画作業を減らし、プロンプト入力の応答性が改善されました（v2.1.257）
- ポリシーヘルパーの診断が改善されました。更新失敗が `/status` に出るようになり、管理設定のダイアログを拒否した場合に Claude Code が終了した理由が表示され、ヘルパーのタイムアウトがタイムアウトとして報告されます（v2.1.257）
- `/code-review --comment` が、GitLab のマージリクエストに対して `glab mr note` で指摘を投稿するようになりました（従来は対象が未対応と報告していました。v2.1.257）
- 他のダイアログの下に積まれた MCP のエリシテーションや権限確認も、表示されている確認と同じ遅延でアイドル時のデスクトップ通知を出すようになりました（v2.1.257）
- 同時に届いた非同期フックの完了通知が、フックごとに 1 行ではなく 1 行にまとめて出るようになりました（verbose / トランスクリプト出力。v2.1.257）
- `claude self-hosted-runner --configure-git` が git の push negotiation も有効にするようになり、古いクローンから新しいブランチを初めて push するときにツリー全体ではなく新しいコミットだけを送るようになりました（v2.1.257）
- ゲートウェイのキープアライブでレスポンスが開いたままの間の SDK ホストへの生存報告が改善され、`CLAUDE_STREAM_IDLE_TIMEOUT_MS` を上げた環境での長い待ちがハングと誤認されなくなりました（v2.1.257。詳細は大幅更新 3 参照）
- MCP の接続と OAuth のデバッグ／エラーログで、サーバーの URL やリクエストヘッダーに含まれる認証情報が伏せ字になりました（v2.1.257）
- `/fork` が、新しいバックグラウンドセッションで元の会話のプロンプトキャッシュを維持するようになりました。worktree の説明がシステムプロンプトの変更ではなくメッセージとして届くためです（v2.1.257）
- 絵文字の補完が、GitHub / Slack のショートコードの別名（`:satisfied:`・`:telephone:`・`:collision:` など）の残りも受け付けるようになりました（v2.1.257）

**バグ修正**

- macOS 12（Monterey）で Claude Code が起動しない問題を修正（v2.1.255 で入った回帰。v2.1.258）
- 再送された権限承認が適用できなかったあと、リモートセッションとスケジュール実行セッションが `user messages must have non-empty content` で失敗する問題を修正（v2.1.258）
- 起動後に作成された `.claude/` フォルダの設定が、再起動するまで拾われない問題を修正（v2.1.257）
- `←` で開いたエージェントビューからディスパッチしたセッションが、対象ディレクトリの `defaultMode` とエージェントの `permissionMode` を上書きして常に元セッションの権限モードで始まる問題を修正（v2.1.257）
- `claude agents` で `keybindings.json` による Ctrl+G の再割り当てが無視される問題を修正。同画面の Ctrl+S / Ctrl+T も新しい `Agents` コンテキストで再割り当てできるようになりました（v2.1.257）
- 自己更新中の macOS の npm インストール環境、および古いデーモンのロックファイルが再利用済みのプロセス ID を指していた Windows で、バックグラウンドセッションが開始できない問題を修正（v2.1.257）
- スラッシュコマンドのパネルの裏で応答がストリーミングされている間、作業中のスピナーが止まる問題を修正（v2.1.257）
- スケジュールされた起床のあと、バックグラウンドセッションの `state.json` の `detail` が自分のディスパッチプロンプトを繰り返す問題を修正（v2.1.257）
- 再度プロンプトを送ったバックグラウンドセッションが、完了後も `claude agents` の Completed の奥に埋もれたままになる問題を修正。Completed は最新の完了順に並ぶようになりました（v2.1.257）
- 削除直後のディレクトリからの `claude --bg` が「バックグラウンド化した」と報告してクラッシュ済みのセッション行を残す問題を修正。理由を表示して終了コード 1 で終わるようになりました（v2.1.257）
- セッションの途中で Remote Control が接続すると Bash ツールの定義が再送され、プロンプトキャッシュのミスを起こす問題を修正（v2.1.257）
- カスタムの `Authorization` ヘッダーが二重に列挙されると Bedrock・Mantle・Vertex・WIF で設定済みの認証情報を上書きする問題、および Vertex のセットアップウィザードが `~/.config/anthropic` に残った Anthropic プロファイルを拾う問題を修正（v2.1.257）
- Claude apps gateway が Foundry・Vertex・Bedrock へホストの `Authorization` やプロファイルのヘッダーを送ってしまう問題、および `ANTHROPIC_FOUNDRY_API_KEY` を設定していると Foundry の Entra ID アップストリームが開始しない問題を修正（v2.1.257）
- API キーモードで、残っていた Anthropic の API キーや認証トークンが Foundry のサブスクリプションキーと一緒に送られる問題を修正（v2.1.257）
- プロンプトがメッセージロール無しで保存された `/schedule` のルーチンが、実行しても何もしない状態になる問題を修正（v2.1.257）
- `claude agents` が、バックグラウンドセッションが他セッションからのメッセージの承認待ちであることと、その送信元を表示しない問題を修正（v2.1.257）
- 開いたバックグラウンドセッションの中で Ctrl+S により退避したプロンプトが、そのセッションがアイドルになるか停止して開き直すと失われる問題を修正（v2.1.257）
- サーバー管理設定で配信されたテレメトリ（OTEL）の設定が、デスクトップアプリの Code セッションを含むウォームスタートで無視される問題を修正（v2.1.257）
- リードのメールボックスへの書き込みが一時的にロックされていると、チームメイトの権限リクエストに 2 回応答してしまう問題を修正（v2.1.257）
- コマンドの自動継続の応答がストリーミングされている間、実行中のターンの下に幽霊のような重複したスラッシュコマンド行が描画される問題を修正（v2.1.257）
- `policyHelper` の `timeoutMs` と `refreshIntervalMs` にタイマーの上限（2147483647）を超える値を設定すると失敗するかミリ秒ごとに再実行される問題を修正。値がクランプされるようになりました（v2.1.257）
- 別のサブエージェントのトランスクリプトに切り替えるとトークンカウンターが凍結するか極端に遅くなる問題を修正。バックグラウンドのサブエージェントとチームメイトのカウンターも、応答のストリーミング中にライブ更新されるようになりました（v2.1.257）
- 末尾にドットが付くサンドボックスのネットワークホスト（`example.com.`）について、`deniedDomains` のエントリがサンドボックス内でそのホストをブロックせず、「今後確認しない」を選んでも確認され続ける問題を修正（v2.1.257）
- Remote Control の同意プロンプトを閉じる操作（Esc、または `claude remote-control` での `n`）が同意扱いになり、次のリクエストが確認なしで接続する問題を修正（v2.1.257）
- 起動後に読み込まれた管理 MCP の許可／拒否リストや `strictPluginOnlyCustomization` がブロックすべき設定ファイル由来の MCP サーバーに、`/mcp` の再接続と有効化が接続してしまう問題を修正（v2.1.257）
- `strictPluginOnlyCustomization` が MCP をプラグイン提供のサーバーのみに固定している状態で、`claude mcp remove` がリモートサーバーの保存済み OAuth 認証情報を残す問題を修正（v2.1.257）
- Claude アプリから開始した Remote Control（`claude remote-control`）のセッションが、選択したモデルを無視してマシンの既定モデルで動く問題を修正（v2.1.257）
- `allowManagedPermissionRulesOnly` が有効なとき、`--disallowedTools` とセッションの拒否ルールが最初の設定再読み込みで落ちる問題を修正（v2.1.257。詳細は大幅更新 1 参照）
- `--resume` がバックグラウンド化した会話を二重に列挙し、`--continue` がバックグラウンド化前の停止したコピーを開いてしまう問題を修正。`--continue` は完了したバックグラウンドセッションも開けるようになりました（v2.1.257）
- フルスクリーンモードで `!` のシェルコマンド出力をクリックしても展開できない問題を修正（v2.1.257）
- 自動更新をまたいで古い Claude Code バイナリで動き続けるバックグラウンドセッションが、退役せずに積み上がる問題を修正（v2.1.257）
- `claude agents --json` が一瞬ターミナルを raw モードに切り替え、終了時に他のプログラムのターミナル設定を元に戻してしまう問題を修正（v2.1.257）
- Proactive 出力スタイルのセッションが、自分で開始したバックグラウンドコマンドや Monitor の実行中にアイドルせず、埋め草メッセージとログの読み返しでビジーループする問題を修正（v2.1.257）
- コンピューターのスリープ・接続断・サーバーエラーで応答がストリーミング中に切れると、サブエージェントが停止する問題を修正。不完全な応答で終わらず自動的に継続するようになりました（v2.1.257）
- `claude agents` のセッション内の `/btw` パネルで `←` が何もしない問題を修正。回答の途中でもエージェント一覧へ戻れるようになり、セッションを開き直すとパネルも戻るようになりました（v2.1.257）
- アドバイザーモデルを設定したセッションが、バックグラウンドのリクエスト（コンパクション・`/recap`・プロンプト候補）でプロンプトキャッシュを外し、毎回会話全体をキャッシュ無しで再送する問題を修正（v2.1.257）
- モデルが起動した Monitor がまだ動いている間に、`claude -p` が最終結果の約 5 秒後に終了する問題を修正。ウォッチが発火するかタイムアウトするまで待つようになりました（v2.1.257）
- auto モードで、一致するコマンドが複合コマンドやサブシェルの中で実行される場合に `permissions.ask` ルールが飛ばされ、確認プロンプト無しで実行される問題を修正（v2.1.257）
- プラグインが、宣言したコマンド・エージェント・スキル・フックなどのコンポーネントのパスがシンボリックリンクである場合に、自分のディレクトリ外のファイルを読めてしまう問題を修正。そうしたパスはエラーで拒否されるようになりました（v2.1.257）
- `/add-dir` が現在の作業ディレクトリ内のディレクトリを拒否する問題を修正。起動時の `--add-dir` と同じく、そのディレクトリのスキル・コマンド・エージェントを読み込むようになりました（v2.1.257）
- トランスクリプトビューから停止したサブエージェントを再開したとき、メインエージェントにそれが伝わらない問題を修正（v2.1.257）
- ANSI カラー付きのテキスト（CI のログなど）を `/feedback` などのダイアログに貼り付けるとクラッシュする問題を修正（v2.1.257）
- プロジェクトの `.mcp.json` が FIFO やデバイスファイルへのシンボリックリンクである場合に `claude mcp add/remove` がハングするかメモリを食い潰す問題を修正。実行可能な対処を示して即座に失敗するようになりました（v2.1.257）
- `claude -p --input-format stream-json` に JSONL 以外のデータを流し込むとメモリが無制限に増える問題を修正。明確なエラーで即座に失敗するようになりました（v2.1.257）
- サブエージェントや他のツールの実行中にターンをバックグラウンド化（`←` または Ctrl+B）すると、バックグラウンドセッションがそのツールを再実行せず拒否扱いにすることがある問題を修正（v2.1.257）
- Bash の `Read()` / `Edit()` の拒否ルールが `< file` のリダイレクトや `tac`・`egrep` のような読み取りコマンドに適用されない問題を修正。引数またはリダイレクト先のいずれかに拒否ルールが掛かればコマンドを拒否するようになりました（v2.1.257）
- トランスクリプトが 5 MB を超えたサブエージェント（画像を多数読んだ場合など）を再開・メッセージ送信すると `No transcript found` で失敗する問題を修正（v2.1.257）
- worktree で隔離されたセッションが、git に一切触れない Bash のループ・`$VAR` の読み取り・`"$(…)"`・ヒアドキュメントを「worktree 内に留まることを検証するには複雑すぎる」として拒否する問題を修正（v2.1.257）
- 会話を空の状態まで巻き戻したあと、`/model` と `/effort` がプロンプトキャッシュの警告を表示する問題を修正（v2.1.257）
- スクリーンショットの多い長いセッションで、画像がリクエストごとのサイズ上限を超えると毎ターン プロンプトキャッシュを外す問題を修正（v2.1.257）
- Edit の権限プロンプトの差分表示で、絵文字や複数コードポイントの文字の幅が誤って描画される問題を修正（v2.1.257）
- WebSocket の MCP サーバーの接続失敗が、原因のエラーではなく `[object ErrorEvent]` としてログに出る問題を修正（v2.1.257）
- 別の Claude Code プロセスが npm の更新をダウンロードしている間、バックグラウンドセッションが `Couldn't start the background service` で開けない問題を修正。開始が完了を待つようになりました（v2.1.257）
- シェルから切り離されるバックグラウンドコマンド（`timeout` や `setsid` の下など）が、タスクの停止や Claude Code の終了後も生き残る問題を修正（v2.1.257）
- タスクパネルや接続中のクライアントからバックグラウンドコマンドを停止したことが Claude に伝わらない問題を修正（v2.1.257）
- バックグラウンドのサブエージェントを停止しても、その Monitor が動いたままになる問題を修正（v2.1.257）
- リンクされた worktree 内でサンドボックス化された git コマンドが、サブディレクトリへ `cd` したあとリポジトリ共通の `.git` ディレクトリへの書き込み権限を失う問題を修正（v2.1.257）
- Opus 4.7 以降での長い非表示の思考フェーズ中に Bedrock と Bedrock Mantle のリクエストが無音になり、アイドルタイムアウトで接続が切られる問題を修正。ストリームが進捗イベントを運ぶようになりました（v2.1.257）
- Claude apps gateway のセッションが期限切れまたは取り消されたあとに Claude Code を起動すると、ネットワークエラーとして報告される問題を修正。セッションが終了したと伝えて `/login` を提示するようになりました（v2.1.257）
- クラウドセッションで、起動時にセッションのネットワークプロキシが開始に失敗すると、そのセッションの残りの間ずっと git / GitHub の認証情報を失う問題を修正。バックグラウンドで再試行して復旧するようになりました（v2.1.257）
- バックグラウンドデーモンの開始が中断されるとシステムの一時ディレクトリに `cc-daemon-*` フォルダが残る問題を修正。`cleanupPeriodDays` の保持期間の掃除で削除されるようになりました（v2.1.257）
- zsh が bash と異なる解釈をする一部の `[[ ]]` 条件式を、Bash の権限チェックが自動承認してしまう問題を修正。これらのコマンドは承認を求めるようになりました（v2.1.257）
- 管理設定の承認プロンプトが、その設定が詳細トレーシングや生の API ボディのログ出力をオフにする、あるいはトレースのエクスポートをオンにする場合にも、テレメトリ向けの文言ではなく汎用の警告を表示する問題を修正（v2.1.257）
- tmux / iTerm2 のペインで動くエージェントチームのチームメイトが、シャットダウン要求を受け取ったあとも開いたままになることがある問題を修正（v2.1.257）
- API キーを作らない Console サインイン（Sign in with your Console account）が組織のサーバー管理設定を適用せず、`/status` がそのサインインの Organization を表示しない問題を修正（v2.1.257）
- VS Code 拡張で、第三者プロバイダー（Bedrock・Vertex など）のデプロイでも claude.ai 専用機能（リモートセッション・ディクテーション・使用量）が表示され、残ったログイン情報で claude.ai を呼んでしまう問題を修正（v2.1.257）
- VS Code 拡張のセッション一覧パネルの使用量メーターが、パネル読み込み後も空白のままになる問題を修正。直近の既知の使用量を即座に表示するようになりました（v2.1.257）
- VS Code 拡張のスクリーンリーダー向け読み上げを修正。コードフェンスや見出しの前の制御文字が読み上げから可視行を落とすことがなくなり、見出しをまたぐ太字マーカーの対応付けを誤らなくなりました（v2.1.257）

**その他**

- `Ctrl+E` のコマンド説明機能と `permissionExplainerEnabled` が削除されました（詳細はハイライト 5 参照）— [English](https://code.claude.com/docs/en/settings-reference#permissionexplainerenabled)
- 「Fable 5」という表記が「Fable」「Fable モデル」「Fable 5.1 と Fable 5」へ一般化される書き換えが、モデル設定・環境変数・権限モード・機能可用性・デスクトップ・ゼロデータ保持・アドバイザー・CLI リファレンス・コマンド・対話モード・用語集・コスト・コンテキストウィンドウ・プロンプトキャッシュ・Claude Security・LLM ゲートウェイプロトコル・Communications kit・Agent SDK のエージェントループなど 20 ページ近くに及びました（詳細はハイライト 1 参照）— [English](https://code.claude.com/docs/en/model-config#work-with-fable)
- Claude Security プラグインのトラブルシュートで、`Fable 5's safeguards flagged this message` という表示の説明が **`Fable 5.1's safeguards flagged this message` との 2 種類**に増えました — [English](https://code.claude.com/docs/en/claude-security#troubleshooting)
- LLM ゲートウェイプロトコルのページで、`/model` ピッカーで探索済み ID を捨てる条件が「両方が Fable に解決する場合」から「**探索済み ID と既存 ID が同じ Fable のバージョンの別表記である場合**」に精密化されました — [English](https://code.claude.com/docs/en/llm-gateway-protocol#picker-entries-and-caching)
- セッション間メッセージングの一覧の説明から、**スーパーバイザーが次のバックグラウンドセッション用に用意している事前ウォームのワーカープロセスに言及した 1 文が削除**されました（大幅更新 2 の畳み込みと対になる変更です）— [English](https://code.claude.com/docs/en/cross-session-messaging#see-which-sessions-claude-can-reach)
- 設定例のページで、`allowManagedPermissionRulesOnly` と `allowManagedMcpServersOnly` の説明にリファレンスへのリンクが付き、管理設定例の JSON のコメントも「管理された権限ルールのみが適用される」から「**ユーザー・プロジェクト・ローカル設定の権限ルールを無視する**」に書き改められました — [English](https://code.claude.com/docs/en/settings-example#an-organizations-managed-settings)
- サンドボックスのページで、`sandbox.credentials` に組み込みの拒否リストが無いという説明と、適用範囲の説明が別々の段落に分けられました — [English](https://code.claude.com/docs/en/sandboxing#protect-credentials)
- 権限ページの管理設定の節で、`allowManagedPermissionRulesOnly` の説明が本文中の列挙から独立した 1 段落へ切り出されました — [English](https://code.claude.com/docs/en/permissions#managed-settings)
- Agent SDK のカスタムツールのページで、`resource_link` ブロックの扱いが TypeScript と Python で分かれることが明記されました（詳細は大幅更新 3 参照）— [English](https://code.claude.com/docs/en/agent-sdk/custom-tools#return-images-and-resources)
- VS Code 拡張の `/btw` の説明から「コマンドメニューから選ぶ」経路が外れ、Remote Control の起動方法からも「`/` でコマンドメニューを開いて選ぶ」が外れました（いずれも Slash commands ダイアログへの再編に伴うものとみられます）— [English](https://code.claude.com/docs/en/remote-control#start-a-remote-control-session)
- VS Code 拡張のコマンドメニューの説明から `/usage` と `/remote-control` の例が外れ、代わりに Customize 節の項目として MCP サーバー・スラッシュコマンド・出力スタイル・フック・メモリ・権限・プラグインが列挙されるようになりました — [English](https://code.claude.com/docs/en/vs-code#use-the-prompt-box)
<!-- light:minor-updates:end -->

## 新着情報

<!-- light:whats-new:start -->
（今回の対象期間には `whats-new/` 配下のページに差分がありませんでした。最新の週間ダイジェストは前回サマリで扱った Week 34（2026年08月17日～21日）のままで、新しい週のダイジェストの追加も既存ページの訂正もありません）
<!-- light:whats-new:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-08-31.md](./archives/latest/2026-08-31.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-08-31.md](./archives/latest-detail/2026-08-31.md)

<!--
base_commit: e91ea8c5791ff294096b4c5eb5f6e51adac7736c
head_commit: 927fef660e077268108676555cca216ec51d2030
generated_at_full: 2026-09-02T15:07:30+09:00
-->
