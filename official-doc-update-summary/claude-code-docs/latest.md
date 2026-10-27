---
対象期間: 2026年10月25日 〜 2026年10月26日
作成日: 2026-10-26
---

# Claude Code 公式ドキュメント更新サマリ

```markdown
**今回は changelog に新しいリリースがなく（最新は前回と同じ v2.1.310）、通常のページに、Agent SDK のカスタムツールに承認を求めさせるか拒ませる `permission_policy`、実行中のセッションにプラグインのフォルダーを加える `reloadPlugins()` の `addPlugins`、`Dangerous rm operation not ruled out` のプロンプトと端末の外での危険な削除の扱い、バックグラウンドに移したときの動的ワークフローの続け方、組織の管理下で動かないユーザーの mod のフックが載りました**。新しいページはなく、228 ページ中 20 ページが変わり、変更はページ単位で 468 行（追加 403・削除 65）、大幅更新は `agent-sdk/typescript`・`agent-sdk/permissions`・`permission-modes` の 3 ページです。`best-practices` は `llms.txt` の説明文と見出しマップだけが新しい構成に変わり、`llms-full.txt` の本文は前の構成のままです。総行数は 124,774 行から 125,112 行に増えました。

主要なものを以下に挙げます。

1. Agent SDK の TypeScript で、カスタムツールの `permission_policy` を `always_ask` にすると `allowedTools` に挙げていてもその呼び出しを承認しなくなり（`canUseTool` に回りうる）、`always_deny` にすると拒まれるようになり（Agent SDK v0.3.301 以降）、その置き場所と `destructiveHint` の扱いが `agent-sdk/custom-tools` と `agent-sdk/typescript` に載った
2. Agent SDK の `reloadPlugins()` に、起動時になかったプラグインのフォルダーを実行中のセッションに加える `addPlugins` ができ（Agent SDK v0.3.301・Claude Code v2.1.301 以降）、読み込めないときの原因と、`disableSideloadFlags` がそれを拒むことが載った
3. `permission-modes` に `Dangerous rm operation not ruled out` のプロンプトの節ができ、VS Code・Desktop・`-p`・Agent SDK での `auto` と `bypassPermissions` の危険な削除の扱いと、`CLAUDE_CODE_DISABLE_DANGEROUS_RM_TIMEOUT` を VS Code のチャットパネルに効かせる方法が載った
4. 動的ワークフローはセッションをバックグラウンドに移しても自分では続かず、Claude が起動し直したときだけ続く、と `agent-view` と `workflows` が改められた
5. 組み込みのガードが読み込まれる場所では、ユーザーが入れた mod の `classic.<Event>`・`prompt.section`・`settings.read` などのフックが動かず `/plugin` が注記で伝えることと、それを動かすための managed settings の変え方が `plugins/mods/admin` に載った
```

## ハイライト

1. [**Agent SDK のカスタムツールに、呼び出しに承認を求めるか拒むかを決める permission_policy ができた**](./latest-detail.md#1-agent-sdk-のカスタムツールに呼び出しに承認を求めるか拒むかを決める-permission_policy-ができた):  
  `agent-sdk/custom-tools` に h3「Require approval for specific tools」ができ、TypeScript の SDK でカスタムツールの `permission_policy` を `always_ask` にすると、`allowedTools` に挙げていてもその呼び出しを承認しなくなって `canUseTool` に回りうるようになり、`always_deny` にすると拒まれる、と載りました（Agent SDK v0.3.301 以降）。`agent-sdk/typescript` には `McpServerToolPolicy` の h4 と、値ごとの扱い・`always_ask` の呼び出しを先に承認しうる権限モードの 2 つの h5 ができ、`agent-sdk/permissions`・`hooks`・`hooks-guide` の記述も合わせて改められています
2. [**Agent SDK の reloadPlugins に、実行中のセッションへプラグインのフォルダーを加える addPlugins ができた**](./latest-detail.md#2-agent-sdk-の-reloadplugins-に実行中のセッションへプラグインのフォルダーを加える-addplugins-ができた):  
  `agent-sdk/typescript` に h4「Load more plugin folders with `addPlugins`」と、読み込めないときの h5 ができ、起動時の `plugins` オプションになかったフォルダーを `reloadPlugins()` に絶対パスで渡すと、既存のプラグインと一緒に読み込まれる、と載りました（Agent SDK v0.3.301・Claude Code v2.1.301 以降）。`agent-sdk/plugins` には例の h3 ができ、`settings-reference` と `plugins/org` の `disableSideloadFlags` も `addPlugins` を拒むと改められています
3. [**Dangerous rm operation not ruled out のプロンプトの節ができ、端末の外での危険な削除の扱いが場所ごとに載った**](./latest-detail.md#3-dangerous-rm-operation-not-ruled-out-のプロンプトの節ができ端末の外での危険な削除の扱いが場所ごとに載った):  
  `permission-modes` に、シェルがコマンドを Claude Code と違うように読みうるときの `Dangerous rm operation not ruled out` のプロンプトの h3 ができ、`Bash(*)` の allow ルールや `PreToolUse` のフックの `"allow"` では承認できないと載りました。時間制限と拒否の h3 には、VS Code のチャットパネル・Desktop・`-p` の実行・Agent SDK のセッションでの `auto` と `bypassPermissions` の扱いと、`CLAUDE_CODE_DISABLE_DANGEROUS_RM_TIMEOUT` を VS Code に設定する方法が加わっています
4. [**バックグラウンドに移したセッションの動的ワークフローは、Claude が起動し直したときだけ続くと改められた**](./latest-detail.md#4-バックグラウンドに移したセッションの動的ワークフローはclaude-が起動し直したときだけ続くと改められた):  
  `agent-view` の「What carries over when you background」が、引き継がれる・Claude が起動し直したときだけ続く・止まる、の 3 つに書き直され、動的ワークフローの h5 ができました。`workflows` の「Resume after you leave the session」も、実行は自分では続かず Claude が `Workflow` の呼び出しで起動し直したときだけ続く、と改められています（changelog の v2.1.300 の変更に対応）
5. [**組織が管理する環境で動かない、ユーザーが入れた mod のフックと、その注記が載った**](./latest-detail.md#5-組織が管理する環境で動かないユーザーが入れた-mod-のフックとその注記が載った):  
  `plugins/mods/admin` に h3「Know which hooks of a user's mod don't run」ができ、組み込みのガードが読み込まれる場所では、ユーザーの mod の `classic.<Event>`・`prompt.section`・`settings.read`・一部の `session.append` などのフックが動かず、`/plugin` が注記で伝える（v2.1.299 以降）と載りました。フックを動かすための managed settings の 2 つの変え方と、`server-managed-settings` のキャッシュした設定でのガードの扱いも加わっています

## 新規追加されたページ

（今回の対象期間に新規追加・削除されたドキュメントページはありません。`llms.txt` の URL は 275 のままで（変わったのは `best-practices` の説明文の 1 行だけ）、`llms-full.txt` に展開されている固有のページも 228 のままです。`Source:` の行が 231 あり 3 ページが 2 回展開されている状態も前回と同じです）

## 大幅に更新されたページ

- [**Agent SDK reference - TypeScript**](./latest-detail.md#1-agent-sdk-reference---typescript) ([日本語](https://code.claude.com/docs/ja/agent-sdk/typescript#mcpserverstatus) / [English](https://code.claude.com/docs/en/agent-sdk/typescript#mcpserverstatus)):  
  175 行（追加 169・削除 6）が変わりました。ハイライト 1 の `McpServerToolPolicy` とハイライト 2 の `addPlugins` のほか、`McpServerStatus` の `_meta` が届く条件、`setMcpServers()` の規則、ツール名を確かめる 2 つの定数の h3 が加わりました
- [**Configure permissions**](./latest-detail.md#2-configure-permissions) ([日本語](https://code.claude.com/docs/ja/agent-sdk/permissions#how-permissions-are-evaluated) / [English](https://code.claude.com/docs/en/agent-sdk/permissions#how-permissions-are-evaluated)):  
  67 行（追加 48・削除 19）が変わりました。評価の順序に `always_deny` と `always_ask` が入り、`plan` モードで `touch` や `rm` がコールバックに届くという記述が外れて分類器が見ると改められ、`canUseTool` が呼ばれない警告と allow ルールが承認しない呼び出しの扱いが書き直されました
- [**Choose a permission mode**](./latest-detail.md#3-choose-a-permission-mode) ([日本語](https://code.claude.com/docs/ja/permission-modes#auto-approve-file-edits-with-acceptedits-mode) / [English](https://code.claude.com/docs/en/permission-modes#auto-approve-file-edits-with-acceptedits-mode)):  
  53 行（追加 47・削除 6）が変わりました。ハイライト 3 の h3 と端末の外での扱いのほか、`acceptEdits` モードの `touch` の例外と、`--settings`・`--mcp-config`・`--agents` に渡したファイルが保護されたパスに加わりました

## 軽微な更新

今回の差分は **3 ファイル**（`llms-full.txt`・`llms.txt`・見出しマップ）です。`llms-full.txt` の生の差分は追加 403 行・削除 65 行で、ページの並びは変わっていません。ページ単位に切り出すと 228 ページ中 **20 ページ**が変わり、計 468 行（追加 403・削除 65）で、生の差分と一致します（2 回展開されている 3 ページはどれも変わっていない）。**changelog と新着情報（`whats-new/`）のページは変わっておらず、新しいリリースはありません**（最新は前回と同じ v2.1.310）。大幅更新の 3 ページを除く **17 ページ**（173 行。追加 139・削除 34）を以下にまとめます。changelog に既に載っている過去のリリースの項目に対応する記述が加わったものは、その旨を付記しています。

`llms-full.txt` の総行数は **124,774 行から 125,112 行へ 338 行増え**ました（生の差分の差し引き 403 − 65 と一致）。`Source:` の行は 231、固有のページは 228 のままで、2 回展開されている 3 ページ（`plugins/create`・`plugins/install`・`plugins/mods/overview`）も前回と同じです。コードフェンスの外の見出しは 5,931 から 5,943 へ 12 増え、外れた見出しも改題もありません。

**新機能**

- Agent SDK のカスタムツールの `permission_policy`（`agent-sdk/custom-tools`・`hooks`・`hooks-guide`。詳細はハイライト 1 参照）
- 実行中のセッションにプラグインのフォルダーを加える `addPlugins`（`agent-sdk/plugins`・`settings-reference` の `disableSideloadFlags`・`plugins/org` の「Control matrix」。詳細はハイライト 2 参照）
- 組織の管理下で動かないユーザーの mod のフック（`plugins/mods/admin`・`plugins/mods/events`・`server-managed-settings`。詳細はハイライト 5 参照）
- **エージェントビューのピークパネルに `safe mode` の行が出ると載った**（`agent-view` の「Peek and reply」）。ピークパネルでセッションにつながるプルリクエストの下に出る 1 行が、あなたを待っているセッションに加えて、セーフモードで動くセッションにも出るようになりました。`safe mode · customizations are off` は、シェルから `claude --bg --safe-mode` で始めたので、カスタマイズをオフにして動いていることを示します。そのままでもよく、カスタマイズを戻して会話を続けるには、シェルで `claude stop <id>` を実行してから `claude --resume` を実行します。`waiting 3m` のような待ち時間の行（行の右端の経過時間はセッションの開始からの時間で別物）の説明も箇条書きに移りました。changelog の v2.1.299 の追加（`--safe-mode` で始めたバックグラウンドのセッションに、エージェントビューのピークパネルで「safe mode」の行を出す）に対応します — [日本語](https://code.claude.com/docs/ja/agent-view#peek-and-reply) / [English](https://code.claude.com/docs/en/agent-view#peek-and-reply)

**機能改善**

- `Dangerous rm operation not ruled out` のプロンプトと、端末の外での危険な削除の扱い（`permission-modes`・`env-vars` の `CLAUDE_CODE_DISABLE_DANGEROUS_RM_TIMEOUT`。詳細はハイライト 3 参照）
- バックグラウンドに移したときの動的ワークフロー（`agent-view`・`workflows`・`env-vars` の `CLAUDE_CODE_DISABLE_BG_EXIT_HANDOFF`。詳細はハイライト 4 参照）
- **トランスクリプトが、モデルに送った要求の中身も持つと載った**（`claude-directory` の「Application data」・`sessions` の「Where transcripts are stored」）。トランスクリプトには、メッセージと一緒に Claude Code がモデルに送るもの（システムプロンプト、ツールの定義、要求のパラメーター、CLAUDE.md のような読み込んだ指示のファイル）も入りうる、という箇条書きが加わり、自動で消すファイルの表の `projects/<project>/<session>.jsonl` も、「すべてのメッセージ・ツールの呼び出し・ツールの結果の完全なトランスクリプト」から、メッセージ・ツールの呼び出し・ツールの結果に加えて、Claude Code がモデルに送った要求のシステムプロンプト・ツールの定義・パラメーター、に改められました。サブエージェントのトランスクリプトも、セッションのトランスクリプトと同じ形式、と書かれています。`sessions` も、各行はメッセージ・ツールの使用か結果・Claude Code がモデルに送った要求の記録・メタデータのエントリーのどれか、になりました。changelog の v2.1.300 の変更（手元のセッションのトランスクリプトに API の要求ごとのシステムプロンプト・ツール・パラメーターも記録し、共有したトランスクリプトで要求をそのまま再現できるようにした）に対応します — [日本語](https://code.claude.com/docs/ja/claude-directory#application-data) / [English](https://code.claude.com/docs/en/claude-directory#application-data)
- **Agent SDK の権限モードの表が言い換えられた**（`agent-sdk/agent-loop` の「Permission mode」）。`"dontAsk"` の行は、ネットワークのパスからの読み取りのような一部の呼び出しは許していても拒まれ、一覧は `agent-sdk/permissions` の「Don't ask mode」にある、となり（これまでは `AskUserQuestion` などを並べていた）、用途も「承認する人のいないヘッドレスのエージェント」になりました。`"bypassPermissions"` の行も、`allowedTools` に挙げていないツールの呼び出しも含めて承認を求めずに動かし、一部の呼び出しはまだ `canUseTool` のコールバックに回る（一覧は `agent-sdk/permissions` の「Bypass permissions mode」）、に改められました — [日本語](https://code.claude.com/docs/ja/agent-sdk/agent-loop#permission-mode) / [English](https://code.claude.com/docs/en/agent-sdk/agent-loop#permission-mode)
- **apps gateway のポリシーの例から `Bash` の事前承認が外れた**（`claude-apps-gateway-config` の「What goes in `cli`」と「Complete example」）。`permissions.allow` / `.deny` の行の参照先に、Bash のルールが一致しないもの（`permissions` の Bash のルールの限界）が加わり、完全な例で全員に当たる `match: {}` のポリシーの `allow` が `[Read, Grep, Bash, Edit]` から `[Read, Grep, Edit]` になりました — [日本語](https://code.claude.com/docs/ja/claude-apps-gateway-config#what-goes-in-cli) / [English](https://code.claude.com/docs/en/claude-apps-gateway-config#what-goes-in-cli)
- **`worktree.sparsePaths` に `.claude` を含めるよう勧めるようになった**（`settings-reference` の「`worktree.sparsePaths`」）。リストに `.claude` を入れると、各 worktree にリポジトリの `.claude/settings.json` と `.claude/rules/` も入ります。例も `[".claude", "packages/my-app", "shared/utils"]` になりました — [日本語](https://code.claude.com/docs/ja/settings-reference#worktree-sparsepaths) / [English](https://code.claude.com/docs/en/settings-reference#worktree-sparsepaths)

**その他**

- **`allowMachLookup` の例の大文字・小文字**（`settings-reference` の「`sandbox.network.allowMachLookup`」）: 例のサービス名の接頭辞が `com.apple.coresimulator.` から `com.apple.CoreSimulator.` に改められました — [日本語](https://code.claude.com/docs/ja/settings-reference#sandbox-network-allowmachlookup) / [English](https://code.claude.com/docs/en/settings-reference#sandbox-network-allowmachlookup)
- **デモのマーケットプレイスの例から `security-guidance` が外れた**（`plugins/anthropic-marketplaces` の「The demo marketplace in `anthropics/claude-code`」）: デモのマーケットプレイスと公式のマーケットプレイスの両方にあるプラグインの例が、`code-review`・`feature-dev`・`commit-commands` の 3 つになりました
- **`best-practices` の説明文**: `llms.txt` の `Best practices for Claude Code` の説明が、「環境の設定から並列のセッションへの拡大まで、Claude Code を活かすためのヒントとパターン」から「Claude に見えないものを伝え、走らせる確認を与え、例外を許さないルールを強制して、Claude Code をもっと活かす」に変わりました。`llms-full.txt` の `best-practices` の本文は変わっておらず、前の構成のままです
- **見出しマップ**: 57 行が加わり 31 行が外れました。加わったのは 56 見出しと新しいスタンプ、外れたのは 30 見出しと古いスタンプです。加わった 56 見出しのうち、今回 `llms-full.txt` にも入ったのは 12 で、残りの 44 はマップにだけ載り、`llms-full.txt` には見出しも本文もありません。うち 26 は `best-practices` の新しい構成の見出し（「Tell Claude what it can't see」「Give Claude a check to run」「Enforce the rules that can't have exceptions」など）で、外れた 30 見出しはすべて `best-practices` の前の構成の見出しです（`llms-full.txt` にはまだ残っている）。ほかの 18 は `vs-code`（5）・`claude-code-on-the-web`（3）・`claude-security`（2）・`model-config`（2）と、`mcp`・`errors`・`plugins/mods/troubleshoot`・`claude-apps-gateway-config`・`self-hosted-environments-deploy`・`self-hosted-environments-reference`（各 1）の見出しです。本文の更新がまだ取り込みに入っていないので、本サマリではこれらの内容を扱っていません
- **見出しマップ冒頭の自動生成スタンプが、2026年10月26日 05時13分33秒 UTC から 2026年10月27日 01時23分44秒 UTC へ進みました**

**参考リンクについて**: 日本語版は、変更のあった 20 ページと `best-practices` の計 21 ページを取得し、該当する節があるかと今回の内容になっているかを、計 36 項目について確かめました（長いページは区切って読んでいます）。今回は 36 項目すべてで日本語版がすでに今回の内容になっていたので、すべての参考リンクに日本語版を併記しています。`best-practices` は、公式サイトでは英語版・日本語版とも見出しマップの新しい構成になっていましたが、今回取り込んだ `llms-full.txt` の本文は前の構成のままなので、内容は扱っていません。`plugins/mods/admin` の「Know which hooks of a user's mod don't run」は、ページ内外のリンクが使っている `#hooks-the-guard-passes-over` を id として使いました。コード片やアポストロフィを含み id を確かめられない新しい見出し（`agent-sdk/typescript` の「When a tool's `_meta.ui` holds only `visibility`」「`BUILTIN_TOOL_NAMES` and `LEGACY_TOOL_NAME_ALIASES`」、`plugins/anthropic-marketplaces` の「The demo marketplace in `anthropics/claude-code`」）へは直接リンクせず、上位の節へのリンクにするか、リンクを省きました。今回 changelog は変わっていないので、changelog だけに載っている項目はありません。**changelog ページへのリンクは、本サマリの方針どおり付けていません。**

## 新着情報

**今回、新着情報（`whats-new/`）のページに変更はありません**（最新の週のダイジェストは前回と同じ Week 37 です）。

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-10-25.md](./archives/latest/2026-10-25.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-10-25.md](./archives/latest-detail/2026-10-25.md)

<!--
base_commit: ed2bfc53997fa88f3cdffff0e44276b91e32ded7
head_commit: f43c40d31d95ea8ce1ef817f41d68a409f4e53f6
generated_at_full: 2026-10-27T15:16:06+09:00
-->
