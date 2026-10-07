---
対象期間: 2026年10月05日 〜 2026年10月06日
作成日: 2026-10-06
---

# Claude Code 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
**今回は新しいページも大幅に更新されたページもなく、HIPAA 設定の組織向けの説明と監視の手順が書き足され、changelog には v2.1.291 と v2.1.292（いずれも2026年10月06日、計 94 項目）が積まれました**。ページ単位で数えると 221 ページ中 28 ページが変わり、変更は 298 行（追加 252・削除 46）です。総行数は 112,678 行から 112,884 行に増えました。

主要なものを以下に挙げます。

1. HIPAA 設定を適用した組織では、セッションが auto モードではなく Manual モードで始まるようになった
2. ゲートウェイの背後のセッションに向けて、データが外に出る経路と管理設定・イベントの対応表ができた
3. 保持の掃除が設定どおりに動いているかを、retention_sweep イベントで確かめる手順が載った
4. セッションピッカーや /resume で再開したセッションで plan モードが戻り、ピッカーに k・j と数字キーが加わった
5. セルフホストのランナーが停止に要する時間の説明が書き直され、オーケストレーターの停止タイムアウトの決め方が先に来た
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**HIPAA 設定の組織ではセッションが Manual モードで始まるようになった**](#1-hipaa-設定の組織ではセッションが-manual-モードで始まるようになった):  
  HIPAA 設定を適用した組織では組み込みの `auto` の既定が効かず、ほかに開始のモードを決めるものがなければ、端末と VS Code のセッションは Manual モードで始まります。auto モードと `bypassPermissions` は引き続き使えます
2. [**ゲートウェイの背後のセッションに向けて送信経路と管理設定の対応表ができた**](#2-ゲートウェイの背後のセッションに向けて送信経路と管理設定の対応表ができた):  
  ゲートウェイを通るセッションは HIPAA 設定の対象外です。その代わりに機能を絞るための管理設定のキーと、記録に使うイベントを、経路ごとに並べた表が `monitoring-usage` にできました
3. [**保持の掃除が設定どおりに動いているかを確かめる手順が載った**](#3-保持の掃除が設定どおりに動いているかを確かめる手順が載った):  
  `retention_sweep` イベントの値の読み方を表にした節ができました。`claude purge` の成功の見分け方と、`/heapdump` が書くヒープスナップショットの削除も加わっています
4. [**再開したセッションで plan モードが戻るようになりセッションピッカーに数字キーが加わった**](#4-再開したセッションで-plan-モードが戻るようになりセッションピッカーに数字キーが加わった):  
  セッションピッカーや `/resume` で再開しても、plan モードで終わったセッションは plan モードで再開します。ピッカーでは `k`・`j` で移動し、`1`〜`9` でその位置のセッションを再開できます
5. [**セルフホストのランナーの停止にかかる時間の説明が書き直された**](#5-セルフホストのランナーの停止にかかる時間の説明が書き直された):  
  ランナーが起動時に記録する所要時間（既定で 80 秒）以上にオーケストレーターの停止タイムアウトを設定するよう、冒頭で求める形になりました。ドレインは 3 段階の手順として示されています
<!-- light:highlight-list:end -->

## 1. HIPAA 設定の組織ではセッションが Manual モードで始まるようになった

**`permission-modes` に「Permission modes with the HIPAA configuration」の節ができました。** HIPAA 設定を適用した組織では、組み込みの `auto` の既定は効きません。ほかに開始の権限モードを決めるものがなければ、端末と VS Code のセッションは Manual モードで始まります。端末では `Auto mode isn't the default for your organization · Shift+Tab to switch` と表示され、VS Code の拡張には通知が出ません。対象になるセッションは `hipaa-setup` の「Check how developers sign in and connect」に従います。

auto モードと `bypassPermissions` は引き続き使えます。

- **auto モードに切り替える**: `Shift+Tab` を押すか、使っているインターフェースの切り替えの操作を使います
- **auto モードで始める**: `--permission-mode auto` を渡すか、ユーザーの設定（組織全体なら管理設定）で `permissions.defaultMode` を `auto` にします
- **auto モードをなくす**: 管理設定で `permissions.disableAutoMode` を `"disable"` にします
- **`bypassPermissions` を禁じる**: 管理設定で `permissions.disableBypassPermissionsMode` を `"disable"` にします

HIPAA 設定の最低の版と同じく、Claude Code v2.1.285 以降が要ります。セッションが始まるモードを決める表にも、「組織に HIPAA 設定が適用され、セッションがその対象である」場合は v2.1.285 以降で `default` になり、auto モードには切り替えられる、という行が加わりました。

- [権限モードを選択する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/permission-modes#permission-modes-with-the-hipaa-configuration)
- [Choose a permission mode - Claude Code Docs (English)](https://code.claude.com/docs/en/permission-modes#permission-modes-with-the-hipaa-configuration)

## 2. ゲートウェイの背後のセッションに向けて送信経路と管理設定の対応表ができた

**`monitoring-usage` に「Map egress paths to managed controls and events」の節ができました。** セッションの内容をマシンの外へ運びうる経路とローカルでの保持について、それを制限する管理設定のキーと、それを記録するイベントを並べた表です。

| 経路 | 管理設定のキー | イベント |
| - | - | - |
| Bash と PowerShell のコマンド | `sandbox.enabled`・`sandbox.failIfUnavailable`・`sandbox.allowUnsandboxedCommands`・`sandbox.network.allowManagedDomainsOnly`・`sandbox.network.allowedDomains` | `tool_decision`・`tool_result` |
| MCP サーバー | `allowedMcpServers`・`allowManagedMcpServersOnly`・`deniedMcpServers`・`managed-mcp.json` | `mcp_server_connection`・`tool_decision`・`tool_result` |
| フック | `allowManagedHooksOnly`・`allowedHttpHookUrls` | `hook_registered`・`hook_execution_start`・`hook_execution_complete` |
| プラグイン | `strictKnownMarketplaces`・`disableSideloadFlags`・`syncClaudeAiPlugins`・`syncClaudeAiSkills` | `plugin_installed`・`plugin_loaded` |
| WebFetch | `permissions.deny`・`allowManagedPermissionRulesOnly` | `tool_decision`・`tool_result` |
| Artifact など claude.ai にアップロードするツール | `permissions.deny`・`enableArtifact` | `tool_decision`・`tool_result` |
| Remote Control | `disableRemoteControl` | 専用のイベントなし |
| ローカルのトランスクリプトの保持 | `cleanupPeriodDays` | `retention_sweep` |

表の下には注意が並びます。`allowedHttpHookUrls` は設定ファイルをまたいで合わさるので、空の管理のリストに開発者が足せます（どのフックが動くかは `allowManagedHooksOnly` が決める）。フックのイベントはフックのイベントごとに 1 回記録され、`OTEL_LOG_TOOL_DETAILS=1` だけでは HTTP フックの URL は記録されません。`OTEL_LOG_TOOL_DETAILS=1` はコマンドの文字列やツールの入力を加えるので、その内容を保持してよいコレクターでだけ有効にするよう求めています。

**この表を使う場面として、`llm-gateway-rollout` に「The HIPAA configuration behind a gateway」の節ができました。** ゲートウェイを通るセッションは HIPAA 設定の対象外で、表のキーで機能を絞っても対象にはならず、HIPAA 設定が変えるものすべてを覆えるわけでもありません。例として、クラウドのセッションをオフにする管理設定のキーはなく、Claude Code が起動するプロセスから Anthropic の資格情報だけを取り除く設定のキーもありません。`CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` は一部の機能を止める一方で自動更新も止め、WebFetch は残すので、これらのキーの代わりに使わないよう書かれています。`llm-gateway-protocol` にも、ゲートウェイを通るセッションは HIPAA 設定の対象外とする段落が加わりました。

- [モニタリング - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/monitoring-usage#map-egress-paths-to-managed-controls-and-events)
- [Monitoring - Claude Code Docs (English)](https://code.claude.com/docs/en/monitoring-usage#map-egress-paths-to-managed-controls-and-events)
- [組織向けの LLM ゲートウェイをロールアウトする - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/llm-gateway-rollout#the-hipaa-configuration-behind-a-gateway)
- [Roll out an LLM gateway for your organization - Claude Code Docs (English)](https://code.claude.com/docs/en/llm-gateway-rollout#the-hipaa-configuration-behind-a-gateway)

## 3. 保持の掃除が設定どおりに動いているかを確かめる手順が載った

**`monitoring-usage` に「Check the retention sweep」の節ができました。** すべてのマシンで同じ保持期間にするには管理設定で `cleanupPeriodDays` を設定し、マシンがその値で掃除しているかは `retention_sweep` イベントを集めて確かめます。`period_days` と各カウンターは文字列なので、比べる前に数値に変換します。

| マシンが報告するもの | 意味 |
| - | - |
| `result` が `"skipped"` | 掃除が一時停止された。原因は `skip_reason` |
| `used_default` が `"true"`、または `period_days` が管理の値と違う | そのマシンは管理の `cleanupPeriodDays` を適用していない |
| `error_count` が 0 より大きい | 一覧や削除でエラーが起き、保持期間を過ぎたデータが残りうる |
| `files_past_cutoff` が 0 より大きい | 保持期間を過ぎたファイルの削除に失敗したか、古い同期済みのスキル・プラグインのフォルダーが見つかった。`error_count` と合わせて読む |
| イベントがない | それだけでは失敗ではない |

イベントがない理由として、誰も Claude Code を起動していない（次の起動まで掃除されない）、セッションが開いたまま（掃除は 1 セッションに 1 回まで）、掃除が終わる前にセッションが終わった、が挙がっています。掃除がすべてのパスを覆うわけではないことも書かれ、`claude-directory` の「Kept until you delete them」と「Clear local data」を案内しています。

関連して次の変更もありました。

- **`files_past_cutoff` の定義**: `skills/synced/` や `plugins/synced/` の下で見つけた古いフォルダーも、ゴミ箱に移したかどうかにかかわらず数える、と加わりました
- **`claude purge` の成功の見分け方**（`claude-directory`）: スクリプトでは終了ステータスだけでなく出力を確かめ、計画のすべてを消した実行の最後の `Purged N item(s)` の行を成功の印とするよう書かれました
- **ヒープスナップショット**（`claude-directory`）: マシンで誰かが `/heapdump` を実行していたら、書かれた `.heapsnapshot` ファイルも消すよう加わりました。会話全体とプロセスが持っていた資格情報が入っており、保持の掃除も purge も触れません
- `claude-directory` の掃除を飛ばす場合の説明の後にも、「Check the retention sweep」への案内が加わっています

- [Monitoring - Claude Code Docs (English)](https://code.claude.com/docs/en/monitoring-usage#check-the-retention-sweep)
- [.claude ディレクトリを探索する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/claude-directory#clear-local-data)
- [Explore the .claude directory - Claude Code Docs (English)](https://code.claude.com/docs/en/claude-directory#clear-local-data)

## 4. 再開したセッションで plan モードが戻るようになりセッションピッカーに数字キーが加わった

**`sessions` の「Permission mode on resume」で、plan モードで終わったセッションの扱いが変わりました。**

- **起動時のセッションピッカー**（`claude --resume` だけ・`claude --from-pr`・複数に一致する名前）: これまでは保存された権限モードを戻しませんでした。今後は plan モードで終わったセッションなら、`--permission-mode`・`--dangerously-skip-permissions`・`--fork-session` を渡さない限り plan モードで再開します。それ以外の保存されたモードは引き続き戻りません
- **セッション内の `/resume`**: 切り替えた会話は今のセッションのモードで続きますが、plan モードで終わった会話は、`--permission-mode` や `--dangerously-skip-permissions` で起動していても plan モードで再開します。ただし、この Claude Code の実行中にすでに開いていた会話（始めの会話や、`/clear`・`/resume` で離れた会話）は今のモードで続きます
- **端末での再開の表**: `plan` で終わったセッションを端末で再開した場合が「新しいセッションと同じモード」から「plan モード（`--fork-session` なら新しいセッションと同じモード）」に改められました

changelog の v2.1.292 にも、`claude --resume` のセッションピッカーや `/resume` で再開したときに plan モードが戻らない問題の修正が載っています。

**「Use the session picker」のショートカットの表も変わりました。** `↑`/`↓` に加えて `k`/`j` でセッションを移動でき、`1`〜`9` でその位置のセッションを再開できます。これに合わせて、検索モードに入る文字から `Space` のほかに `j`・`k`・数字が除かれました。

- [セッションの管理 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/sessions#permission-mode-on-resume)
- [Manage sessions - Claude Code Docs (English)](https://code.claude.com/docs/en/sessions#permission-mode-on-resume)
- [セッションの管理 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/sessions#use-the-session-picker)
- [Manage sessions - Claude Code Docs (English)](https://code.claude.com/docs/en/sessions#use-the-session-picker)

## 5. セルフホストのランナーの停止にかかる時間の説明が書き直された

**`self-hosted-environments-deploy` の「Shutdown timing」が組み直されました**（ページ単位の差分で 36 行。追加 25・削除 11）。中身の数値は変わらず、読む順序と言い回しが整理されています。

- **冒頭**: `SIGTERM` の後、ランナーはオーケストレーターに止められる前にセッションをきれいに終える時間が要り、その時間を起動時に `This runner needs up to 80s`（既定の設定の場合）を含む行で記録します。オーケストレーターの停止タイムアウト（Kubernetes の `terminationGracePeriodSeconds`、Docker Compose の `stop_grace_period` など）を少なくともその秒数にするよう求めます。Kubernetes の既定は 30 秒で、設定しないとランナーが終わる前にポッドが止まりえます
- **ドレインの 3 段階**: 新しいセッションの受け付けをやめた後、①`--drain-wait-sec`（既定 0）秒まで実行中のターンを待つ、②各セッションのプロセスツリーを終える（シェルのコマンドが終わった後も動き続けるプロセスは除く）、③`post-session` のフックを動かす、の順に進みます。ドレイン中もランナーは Anthropic へのポーリングを続けるので、フックが未コミットの作業を保存している間に別のランナーにセッションが移りません
- **記録される時間の内訳**: `--drain-wait-sec`（既定 0 秒）、`--session-stop-grace-sec`（既定 5 秒）、`--post-session-hook-timeout-sec`（既定 60 秒）、固定の 15 秒、`--push-outcome-on-release` を設定すればさらに 30 秒で、既定では 0 + 5 + 60 + 15 = 80 秒です。`--capacity` を上げても増えません
- `--retire-at` や `--defer-shutdown-max-min` を設定した場合に余分に見込む時間の説明も、同じ言い回しに揃えられました

**「Harden your deployment」の使い捨てのコンテナの項目には、** ランナーがセッションを止めるとき、シェルのコマンドが終わった後も動いているプロセス（デーモン化したサービスなど）にはシグナルを送らず、コンテナや VM を壊すことでそれが終わる、という補足が加わっています。

- [本番環境へのセルフホスト環境のデプロイ - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/self-hosted-environments-deploy#shutdown-timing)
- [Deploy self-hosted environments to production - Claude Code Docs (English)](https://code.claude.com/docs/en/self-hosted-environments-deploy#shutdown-timing)

## 新規追加されたページ

<!-- light:new-pages:start -->
（今回の対象期間に新規追加・削除されたドキュメントページはありません。`llms-full.txt` に展開されているページ数は前後とも 221 で、`llms.txt` の収録 URL も変わっていません。`llms.txt` の差分は `plugins/cli-reference` の説明文の 1 行だけです）
<!-- light:new-pages:end -->

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
（今回は大幅更新に該当するページがありません。`llms-full.txt` から切り出したページ単位の差分（`git diff --no-index --numstat`）で 50 行以上変わったのは changelog（100 行、すべて追加）だけで、changelog はこれまでどおり「軽微な更新」で扱います。次点は `monitoring-usage` の 45 行、`self-hosted-environments-deploy` の 36 行で、それぞれハイライト 2・3 とハイライト 5 で扱っています）
<!-- light:updated-pages:end -->

## 軽微な更新

<!-- light:minor-updates:start -->
今回の差分は **3 ファイル**（`llms-full.txt`・`llms.txt`・見出しマップ）です。`llms-full.txt` をページ単位に切り出して数えると、221 ページ中 **28 ページ**（changelog を含む）が変わり、変更は 298 行（追加 252・削除 46）でした。ハイライトで扱ったページを含め、changelog に加わった **v2.1.292**（2026年10月06日、92 項目。Fixed 64・Improved 13・Added 8・Changed 7）と **v2.1.291**（2026年10月06日、Fixed 2 項目）と、ドキュメントページの変更を以下にまとめます。`llms-full.txt` の総行数は **112,678 行から 112,884 行へ 206 行増え**ました。

**新機能**

- `claude plugin install` に `--marketplace <source>` を追加。必要ならマーケットプレイスを（`claude plugin marketplace add` と同じポリシーの確認のもとで）追加し、そこからプラグインを入れます（v2.1.292）
- Agent ツールに `effort` パラメーターを追加。Claude が求められた effort でサブエージェントを動かします（v2.1.292）
- 環境変数 `CLAUDE_CODE_OVERLOADED_RETRY_BASE_DELAY_MS` を追加。過負荷（529）のリクエストを再試行するバックオフの基本の遅延を長くできます（v2.1.292）
- mod がプロンプトボックスの補完の一覧に自分の行を加えるためのイベント `prompt.autocomplete` を追加（v2.1.292）
- mod の `$.model.complete` にプロンプトキャッシュを追加。`prompt` と `system` がテキストのブロックを取り、ブロックに `cache: true` を付けるとそこまでのリクエストをキャッシュします（v2.1.292）
- mod の `agent.spawn` フックにワークフローのエージェントを実行と index 付きで加え、mod が拒否できるようにした（v2.1.292）
- [Claude Tag] チャンネルの Configure ページの Allowed domains のカードに Edit ボタンを追加。Enterprise の管理者が、チャンネルのドメインを決めるアクセスバンドルを開けます（v2.1.292）
- [Code Review] Code Review の分析の PRs reviewed のグラフに、期間の合計と前の期間からの変化、リポジトリ別の内訳を追加（v2.1.292）
- **mod のリファレンスに `prompt.mention` イベントが載った**。プロンプトが @メンションしたファイルを Claude Code が読む直前に発火し、`next({ ...e, path })` で別のファイルを読ませるか `{ deny: reason }` で拒めます。Claude Code v2.1.290 以降が要ります — [English](https://code.claude.com/docs/en/plugins/mods/reference#prompts-and-what-claude-reads)

**機能改善**

- `claude -p` と SDK のセッションの起動を改善。最初のターンが HTTP・SSE の MCP サーバーの `resources/list` の応答を待たなくなりました（v2.1.292）
- 長い箇条書き・番号付きの返信の描画を改善。ストリーミング・リサイズ・トランスクリプト（ctrl+o）での開き直しがずっと速くなりました（v2.1.292）
- Ctrl+C の下書きの復元を改善。スラッシュコマンドやメッセージの送信の後も、クリアしたプロンプトに Up で戻れます（v2.1.292）
- フックの出力の扱いを改善。フックの出力に書かれた `<system-reminder>` タグは、Claude に届く前にエスケープされます（v2.1.292）
- ツールの入力の扱いを改善。Grep が `path` の代わりに `file_path` を受け付け、Write・WebFetch・Read はいくつかの余分なパラメーターで失敗せずに無視します（v2.1.292）
- 設定ファイルで宣言したマーケットプレイスの名前が Anthropic 公式のマーケットプレイスに見えるときに示す手順を改善（v2.1.292）
- サンドボックスの自動許可を改善。ユーザー・管理・`--settings` の設定で厳格なサンドボックスモードにしていると、`FOO=bar python3 app.py` のような環境変数の接頭辞付きのインタープリターのコマンドがプロンプトなしで動きます（v2.1.292）
- Artifact ツールの一覧を改善。公開済みのアーティファクトの数が Claude に見え、一度に 50 件ではなく 200 件まで一覧できます（v2.1.292）
- 再起動後のクラウドのセッションを改善。止まったバックグラウンドのエージェントのうちどれを ID で再開できるかが Claude に伝わります（v2.1.292）
- claude.ai のクラウドのセッションでブラウザーに届かないときの Claude in Chrome のメッセージを改善。ユーザーが望めば代わりの方法で続けてよいと Claude に伝わります（v2.1.292）
- /focus のヒントを改善。ターンの途中で focus ビューを試すよう誘い、戻し方を示します（v2.1.292）
- 新しいプロトコルの確認を無視するローカル（stdio）の MCP サーバーでの起動を改善。一度遅く接続すると 7 日間記憶され、待たずに古い方法で接続します（v2.1.292）
- [Claude Tag] チャンネルでの `@Claude !status` を改善。Claude がタグなしのメッセージを読むのをやめたこと、その理由、@メンションでまた読み始めることを示します（v2.1.292）
- **Claude apps gateway が対応する PostgreSQL が「14 以降」から「11 以降」になった**（`claude-apps-gateway`）。11〜13 はゲートウェイのサーバーで v2.1.290 以降が要り、PostgreSQL のプロジェクトがもう保守していないので、できれば新しい版を使うよう添えられています。`claude-apps-gateway-on-aws` の RDS の手順からも「最低の版 14 を満たす」の記述が外れました — [日本語](https://code.claude.com/docs/ja/claude-apps-gateway#prerequisites) / [English](https://code.claude.com/docs/en/claude-apps-gateway#prerequisites)
- **Claude apps gateway のデータベースの条件が加わった**（`claude-apps-gateway-deploy`・`claude-apps-gateway-config`）。PostgreSQL そのもの（セルフホストでもマネージドでも）が対象で、Postgres のプロトコルだけを実装する分散 SQL などのデータベースは対象外です。`store.postgres_url` はカンマ区切りのリストではなく 1 つのホストを取り、複数のノードがあるならマネージドサービスのエンドポイント・ロードバランサー・仮想 IP など前に立つアドレスを使い、フェイルオーバーより長い readiness の猶予を設定します。トラブルシューティングにも、URL を読めずに起動が終わる場合（ホストが複数、パスワードにエンコードしていない `/`・`?`・`#`・`%` がある）の行が加わりました — [English](https://code.claude.com/docs/en/claude-apps-gateway-deploy#postgres)
- **IdP に提示する証明書のローテーションの手順に、複数のレプリカの場合が加わった**（`claude-apps-gateway-config`）。ローリング再起動でよく、古い証明書を IdP から外すのはすべてのレプリカが再起動した後です
- **サンドボックスの範囲の説明に 2 項目が加わった** — [日本語](https://code.claude.com/docs/ja/sandboxing#scope) / [English](https://code.claude.com/docs/en/sandboxing#scope)
  - バックグラウンドのセッションは自分のプロセスで動き、その設定でサンドボックスが有効なら Bash のコマンドがサンドボックス化されます
  - サンドボックスの外で動くプロセスも境界の内側に置くには、承認したホストだけのネットワークの許可リストを付けて sandbox runtime の中で Claude Code（ローカルモード）を動かすか、ファイアウォールのスクリプトのある dev container で動かします。`security` のおすすめも同じ表現に改められています
- **サブエージェントの `effort` は `CLAUDE_CODE_EFFORT_LEVEL` 環境変数を上書きしない、と明記された**（`sub-agents`）。`statusline` のサブエージェントの行の `effort` のフィールドも、「セッションの effort を継承するとき」ではなく「サブエージェントに level が設定されていないとき」に省かれる、と改められました — [日本語](https://code.claude.com/docs/ja/sub-agents#supported-frontmatter-fields) / [English](https://code.claude.com/docs/en/sub-agents#supported-frontmatter-fields)
- **mod のリファレンスの制限と描画の記述が改められた**（`plugins/mods/reference`）。`Code` と `Markdown` の 10,000 文字の上限が表から外れ、制限の表の「`Text` の 1 つの文字列の子は 10,000 文字」が「1 つのツリーのテキストは最初の 100,000 文字が描かれる」に替わりました。プロンプトの上のインラインの `Pane` では `bodyRows` が「今見えている行数」ではなく「その上限」を示し、`engine.create` で名前空間を差し控えられるのは `user` 以外の tier の mod だけになりました。対象の版の表記も v2.1.289 から v2.1.290 に進んでいます
- **サブプロセスの環境のスクラブの例の表から、`CLAUDE_CONFIG_DIR` の「v2.1.251 以降が要る」が外れた**（`env-vars`）。代わりに、v2.1.251 より前のスクラブは `ANTHROPIC_API_KEY` と `AWS_SECRET_ACCESS_KEY` だけを消し、表のほかの例の変数には触れなかった、と段落が加わりました。シェルの展開を通じて読めるもの、という限定も外れています
- **`plugins/cli-reference` の表は各サブコマンドのよく使うオプションだけを挙げる、と明記された**。`claude plugin <subcommand> --help` で全オプションを見るよう案内し、ページの説明（`llms.txt` も）から「Complete」が外れました。`plugins/install` と `plugins/troubleshooting` のリンクの文言もこれに合わせています
- **Amazon Bedrock の SSO の認証のループの説明が改められた**（`amazon-bedrock`）。後のリクエストが資格情報をまだ期限切れと見ると `awsAuthRefresh` が再実行されて別のタブが開く、という仕組みが書かれました

**バグ修正**

- `permissionMode: auto` のサブエージェントの定義が、auto モードを使えないとき（設定での無効化・サーキットブレーカー・対応しないモデル）にも auto モードに入る問題を修正（v2.1.292）
- サンドボックスのコマンドが、`~/.claude/seed-admin` の下にある `/ultrareview` のアップロード用にステージしたファイルのコピーを読めた問題を修正（v2.1.292）
- セッションの途中で現れたり指し先が変わったりした管理設定のサンドボックスの読み取り拒否のパス（とその横のユーザーのパス）が、内側のプロジェクトの許可を外さず、そこのファイルからの資格情報の注入も止めない問題を修正（v2.1.292）
- macOS と Windows で、読み取りの途中にすり替えたリンクを通じて、ノートブックや PDF の読み取りが承認の範囲外のファイルを返せた問題を修正（v2.1.292）
- 設定の取得に失敗している間、改ざんされたサーバー管理の設定のディスク上のキャッシュが、組み込みのポリシーのプラグインをオフにしたり差し替えたりできた問題を修正（v2.1.292）
- ホームフォルダーやドライブの 8.3 形式の短い名前など Windows での別の綴りへの `rm -rf` が、それを消す操作として扱われない問題を修正（v2.1.292）
- [セキュリティ] PreToolUse フックの承認と auto モードが、ネットワーク（UNC）パスからのファイルの読み取りで権限のプロンプトを飛ばす問題を修正（v2.1.292）
- ターンの途中で auto モードや plan モードを抜けると、スキルやスラッシュコマンドの `allowed-tools` のルールが後のターンで戻ってくる問題を修正（v2.1.292）
- `HTTPS_PROXY` が設定されていると、Claude Code 自身の API リクエスト（サインイン・ポリシー・フィードバック・アーティファクト）で `NO_PROXY` が無視される問題を修正（v2.1.292）
- 名前が 128 文字を超える MCP のツールがあると、すべてのリクエストが失敗する問題を修正。そのツールは外され、MCP のエラーで名前が示されます（v2.1.292）
- 初回の実行で、組織の管理設定が読み込まれる前に `marketplace add` や `install` などの `claude plugin` のコマンドが動く問題を修正（v2.1.292）
- 1 回限りの `claude -p` と Agent SDK の実行が最終結果の 5 秒後にバックグラウンドのコマンドを止め、1 回限りの `claude -p` が予定した wakeup を落とす問題を修正。どちらも待つようになりました（v2.1.292）
- `claude --resume` のセッションピッカーや `/resume` で再開したとき、plan モードが戻らない問題を修正（詳細はハイライト 4 参照）（v2.1.292）
- `/resume`・`/branch`・`/clear` の後に作った保存済みの予定のタスクが発火せず、タスクのファイルへの数ミリ秒差の 2 回の書き込みの後、保存済みのタスクがその後の作成・削除を無視する問題を修正（v2.1.292）
- セッションのプロセスが（クラッシュの後などに）再起動すると、保留中の wakeup が失われてバックグラウンドのセッションの `/loop` が黙って止まる問題を修正（v2.1.292）
- 渡したファイルやフォルダーを読めないとき、Grep と Glob が一致なしと報告する問題を修正。1 回再試行するか、読めないことを伝えます（v2.1.292）
- PDF の `pages` が "6,9,15" のようなリストのとき、Read ツールがエラーなしに最初の項目だけを返す問題を修正。ページや範囲ごとに読むよう伝えるエラーを返します（v2.1.292）
- 256KB を超える @メンションしたテキストファイルが黙って外される問題を修正。Claude にファイルのサイズと、分けて読むことが伝わります（v2.1.292）
- メインの会話をすでに止めた上限でエージェントが失敗すると、使用上限の警告がバックグラウンドのエージェントごとに繰り返される問題を修正（v2.1.292）
- デスクトップアプリや IDE がホストするセッションで、Remote Control の閲覧者にバックグラウンドのサブエージェントのペインが空で見える問題を修正（v2.1.292）
- セッション間の配送の通知で似た名前の 2 つのセッションが 1 つの宛先として示され、端末のセッションがメッセージを期限切れにしたのに期限切れの通知がデスクトップアプリのせいにする問題を修正（v2.1.292）
- 別のメッセージがすでにキューにあるとき、デスクトップアプリの Send now が、ターンが待っていたサブエージェントを終わらせる問題を修正（v2.1.292）
- 報告の送信中に Ctrl+O や Ctrl+Z を押すと `/bug`・`/share`・`/feedback <text>` がやり直しになり、送信後に取り消し扱いで閉じる問題を修正（v2.1.292）
- すぐに Enter を押すと `/remote-env` が保存済みの既定の環境を置き換える問題を修正。一覧は既定の環境から開き、既定がないときはどの行にもチェックが付きません（v2.1.292）
- 1 つのプロンプトで複数の貼り付けが重なると、一部の貼り付けたテキストが入力したテキストとして Claude に届く問題を修正（v2.1.292）
- vim モードで、カーソルが行末を越え、短い行で j/k が列を失い、`f`/`t`/`F`/`T`/`;`/`,` がプロンプトの別の行の一致へ飛んだりそこまで削除したりする問題を修正（v2.1.292）
- `/add-dir` のパスの欄で Shift+Enter や貼り付けで改行が入り、速く入力した "tab"・"up"・"down" がそのキーとして扱われる問題を修正（v2.1.292）
- プロンプトのフッターの行を選んでいる間に、速い入力・入力メソッドの文字・分解したアクセントが落ち、`!` で行が選ばれたままになる問題を修正（v2.1.292）
- iTerm2 を検出したとき、フルスクリーンモードがウィンドウのリサイズと Ctrl+L のたびに全画面のクリアを送る問題を修正。iTerm2 のスクロールバックが古いページで埋まる原因だった可能性があります（v2.1.292）
- Read の deny ルールがあり作業ディレクトリがシンボリックリンクの下にあるとき、ファイルを指さない @ の語に「could not be examined」の不要な注記が出る問題を修正（v2.1.292）
- `/cd` や権限の変更の後に「instruction file not loaded」の行が古くなったり欠けたりする問題を修正し、入れ子の指示ファイルが読み込まれないときにトランスクリプトに行を加えた（v2.1.292）
- `/name` を繰り返したコンパクションの要約によって、ユーザー専用のスキルを Claude が呼び出せた問題を修正（v2.1.292）
- Write・Edit・NotebookEdit・LSP の行と、単独の Read・Grep・Glob の行が、mod が呼び出しを拒んだ理由を隠す問題を修正。行に理由を示します（v2.1.292）
- ターンが終わる瞬間にワーカーが止められると、クラウドのセッションに終わらないターンが表示される問題を修正（v2.1.292）
- トランスクリプトの大きなクラウドのセッションで、承認した権限をまた求めることがある問題を修正（v2.1.292）
- Claude が読んでいる間にメッセージが再試行・編集されると、クラウドのセッションで予定のタスクやほかのキューの通知が失われる問題を修正（v2.1.292）
- セッションのコンテナが再起動すると、クラウドのセッションがクライアントで選んだ思考の設定を忘れる問題を修正（v2.1.292）
- Anthropic が組織の設定を確認できないとき、Cowork のクラウドのセッションがプロキシがアーティファクトをブロックしたと示す問題を修正（v2.1.292）
- hooks モジュールが 1 つの const を通じて `$.state` を何度も呼ぶプラグインの読み込みや検証に数分かかる問題を修正（v2.1.292）
- `claude plugin validate` が、エンジンが別の場所から読む hooks モジュールの matcher や state の値を一覧する問題を修正（v2.1.292）
- `claude plugin validate` が、再宣言・再代入されたトップレベルの `var` を通じて読む `$.state` の値を一覧する問題を修正。そうしたモジュールは拒否されます（v2.1.292）
- プラグインが提供する `$` のメソッドがフックの起点を再起動し、上に `.catch` のあるガードのフックを延々と再実行しうる問題を修正（v2.1.292）
- プラグインのフックのワーカーの再起動中に行ったプラグインのインターフェースの呼び出しが、ほかのプラグインのフックなしで動く問題を修正（v2.1.292）
- `next(e)` を呼んだ後に拒否する mod の `config.set`・`state.set`・`env.set`・`agent.spawn` のフックが拒否として扱われる問題を修正。フックを名前付きで失敗として報告します（v2.1.292）
- `/theme`・`/config` の Theme メニュー・初回のテーマの手順が、プラグインの `config.set` フックに尋ねる前にテーマを保存する問題を修正（v2.1.292）
- プラグインの `tool.check` フックが allow と答えると、答えが要るツール（質問・プランの承認）がダイアログを出さずに動く問題を修正（v2.1.292）
- フックのワーカーが置き換わると、mod の起動時のプロンプト・コマンド・サブエージェントが 2 回キューに入る問題を修正（v2.1.292）
- `next(e)` を呼んだ後、ターンの中断中に失敗した mod のフックが呼び出しを通す問題を修正。呼び出しは拒否されます（v2.1.292）
- 理由が 4,096 文字を超えると、プラグインのプロンプトの破棄や設定の拒否が無視される問題を修正（v2.1.292）
- ユーザーが入れた mod が加えた `$` の名前を組織のプラグインが返すと、組織のプラグインが自身の再読み込みやほかのプラグインのクラッシュの後にアンロードされる問題を修正。mod の方をアンロードします（v2.1.292）
- プラグインのフックのワーカーの再起動中に行ったツール呼び出しが、プラグインの権限のフックなしで答えられる問題を修正（v2.1.292）
- プラグインの `tool.call` フックが、誤った名前のパラメーターが直される前のツール呼び出しを見る問題を修正。ツールが実際に使う引数を見ます（v2.1.292）
- 別の mod のフックがガード自身の `$` の呼び出しの下で行う呼び出しで、`.catch` のある mod のガードのフックが黙って飛ばされる問題を修正。`.catch` に尋ねます（v2.1.292）
- [クラウドセッション] ルーティンの実行が、終わった後も何時間も実行中と表示されることがある問題を修正（v2.1.292）
- [クラウドセッション] 通知の設定を保存していないルーティンを編集・複製すると、プッシュ通知がオフになる問題を修正（v2.1.292）
- [クラウドセッション] SVG・HEIC・TIFF などのあまり一般的でない画像ファイルの添付に失敗する問題を修正。通常のファイルとして添付します（v2.1.292）
- [クラウドセッション] 組織が承認を必須にしたコネクタのツールに、効果のない「Always allow」を承認のプロンプトが示す問題を修正（v2.1.292）
- [Remote Control] claude.ai/code から始めた新しい Remote Control のセッションの最初のメッセージが画像しか受け付けない問題を修正。後のメッセージと同じく PDF などのファイルも受け付けます（v2.1.292）
- [Claude Tag] Claude がスレッドで最初の要求を処理している間に送った返信が、その要求が終わるまで保留され、数秒差で送ると見落とされる問題を修正（v2.1.292）
- [Claude Tag] GitHub の PR の活動やルーティンだけで起こされた Slack のスレッドが、管理者がチャンネルやワークスペースの既定のモデルを変えた後も元のモデルのままになる問題を修正（v2.1.292）
- [Claude Tag] 本当の原因が組織の使用クレジットの枯渇なのに、Claude が Slack に支出上限の通知を投稿することがある問題を修正（v2.1.292）
- [Claude Tag] Slack から答えられない権限のプロンプトが自動で拒否されると、中断するまでセッションが止まる問題を修正（v2.1.292）
- [Code Review] PR が新しいベースブランチに移り古いブランチが削除されると、キューのレビューが失敗する問題を修正。コミットをレビューのキューに入れ直します（v2.1.292）
- [Code Review] PR が CLAUDE.md を編集すると、レビューがその規則を無視する問題を修正。ベースブランチの版を使います（v2.1.292）
- 2.1.290 の退行で、クラウドのセッションが権限のプロンプトへの答えを落とすことがある問題を修正（v2.1.291）
- 2.1.288 の退行で、終了時にセッションの最後のメッセージが失われることがある問題を修正（v2.1.291）

**その他**

- ローカル（stdio）の MCP サーバーの接続が、Bedrock・Vertex・Foundry を含むすべてのインストールで、既定でプロトコル版 2026-07-28 を交渉するように変更。`MCP_PROTOCOL_NEGOTIATION=legacy` で外せます（v2.1.292）
- `claude plugin test` を変更。テストが登録したフックの中の `expect` の失敗や、エンジンが拒むスタブの答えが、黙って合格せずテストを失敗させます（v2.1.292）
- 使用上限のメッセージが claude.ai の設定へのリンクを https:// 付きで書くように変更。端末やアプリでクリックできます（v2.1.292）
- 予定のルーティンと Run now のルーティンの実行が、承認を求めずに自分だけが見られる新しいアーティファクトを公開するように変更。コネクタなどのアクセスを求めるアーティファクトは引き続き尋ねます（v2.1.292）
- エージェントの名前を最大 256 文字に変更。長い名前は拒否され、スキルやプラグインのファイルの `name` がそれより長ければ無視されます（v2.1.292）
- [Claude Tag] `!fork` で続けた Slack のスレッドの最初のメッセージを、出所・要求・依頼者を示し元のスレッドへのリンクのあるカードに変更（v2.1.292）
- [Claude Tag] 管理設定の Claude Tag の支出上限のページで、組織全体と既定の支出上限の欄を、ほかをクリックしたときではなく Save か Enter を押したときだけ保存するように変更（v2.1.292）
- **`errors` の「Could not load AWS or Google Cloud credentials」から、「キャッシュした資格情報を消して 2 回再試行してからこのメッセージを出す」の一文が外れた**
- **`hooks` の「What a blocked prompt leaves behind」から、「JSON を出さずに終了コード 2 で終わるフックでは、ブロックのメッセージに必ずプロンプトの文が入る」の一文が外れた**
- **`remote-control` と `costs` に Claude ヘルプセンターへの案内が加わった**。Remote Control は Claude Code の機能で、ほかの Claude の製品の会話はヘルプセンターを見るよう、`costs` は Claude Code の使用量だけを扱い、ほかの製品の使用上限はヘルプセンターを見るよう書かれています
- **`hipaa-setup`・`admin-setup` の言い回しが改められた**。「Check how developers sign in and connect」が挙げるものを、「接続」から「サインインと接続の方法」と言い換えています
- **`llms.txt` の `plugins/cli-reference` の説明文が「Complete reference for…」から「Reference for…」になった**
- **見出しマップに 5 見出しが加わった**。`monitoring-usage` の「Map egress paths to managed controls and events」「Check the retention sweep」、`llm-gateway-rollout` の「The HIPAA configuration behind a gateway」、`permission-modes` の「Permission modes with the HIPAA configuration」と、`plugins/mods/reference` の「Elements」の下の「`Box` border styles」です。最初の 4 つは本文にありますが、「`Box` border styles」は `llms-full.txt` の本文にまだ見出しがありません
- **見出しマップ冒頭の自動生成スタンプが、2026年10月06日 01時40分57秒 UTC から 2026年10月07日 05時48分48秒 UTC へ進みました**

**参考リンクについて**: 日本語版は、`permission-modes`・`monitoring-usage`（「Map egress paths to managed controls and events」）・`llm-gateway-rollout`・`claude-directory`・`sessions`・`self-hosted-environments-deploy`・`claude-apps-gateway`・`sandboxing`・`sub-agents` の 9 ページを実測し、今回の内容に更新されていたためリンクを付けています。**`monitoring-usage` の「Check the retention sweep」は日本語版で節を確かめられなかったため、英語版だけにしています。** `plugins/mods/reference`・`claude-apps-gateway-deploy` は日本語版を確かめていないため、英語版だけにしています。changelog だけに載っていて対応する節のない項目にはリンクを付けていません。 **changelog ページへのリンクは、本サマリの方針どおり付けていません。**
<!-- light:minor-updates:end -->

## 新着情報

<!-- light:whats-new:start -->
**今回、`whats-new/` 配下のページに変更はありません。**
<!-- light:whats-new:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-10-05.md](./archives/latest/2026-10-05.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-10-05.md](./archives/latest-detail/2026-10-05.md)

<!--
base_commit: c3f00327d040ed4b125f7bfb47f07adb2a4785cc
head_commit: 4732026713f96a1268695ab6d1e2f0fc2a78d528
generated_at_full: 2026-10-07T15:00:21+09:00
-->
