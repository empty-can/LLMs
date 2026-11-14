---
対象期間: 2026年11月12日 〜 2026年11月13日
作成日: 2026-11-13
---

# Claude Code 公式ドキュメント更新サマリ

```markdown
**今回は Code Mode の新しいページ（`code-mode`）が加わり、changelog に v2.1.325（2026年11月13日、139 項目）が積まれました。サンドボックスの中の Bash コマンドをプロンプトなしで走らせる `sandbox.autoAllowBashIfSandboxed` の既定が `false` になり、サブエージェントのモデルの決まり方、mod の配色とプロンプトの上の欄、マーケットプレイスのコミットへの固定も書き直されています**。`llms.txt` は `code-mode` の 1 行が加わって URL が 239 から 240 になり、各言語の索引のページ数も 203 から 204 になりました。`llms-full.txt` では 204 ページのうち 72 ページ（新しい `code-mode` と changelog を含む）が変わり、生の差分は 2,130 行（追加 1,437・削除 693）です。うち 710 行は `agent-sdk/quickstart` の掲載位置の移動で、これを除くと 1,420 行（追加 1,082・削除 338）です。大幅更新は `plugins/mods/interface`・`sub-agents`・`agent-view`・`errors` の 4 ページです。総行数は 127,463 行から 128,207 行に増えました。

主要なものを以下に挙げます。

1. 実験的な機能 Code Mode のページ `code-mode` が加わった。Claude がツールを呼ぶ JavaScript を書き、Claude Code がそれをセッションの中で実行する。`CLAUDE_CODE_EXPERIMENTAL_CODE_MODE=1` でオンにし、v2.1.323 以降・対話のターミナル・Claude のサブスクリプションか Console のアカウントなどが要る
2. `sandbox.autoAllowBashIfSandboxed` の既定が `false` になり、サンドボックスの中の Bash コマンドも既定で通常の許可の流れを通るようになった（ページは v2.1.324 より前は `true` だったとし、changelog は v2.1.325 の Changed に載せている）。プロンプトなしで走らせるには `true` にする
3. `sub-agents` の「Choose a model」が書き直され、入れ子のサブエージェントは既定で起動したサブエージェントのモデルで動く、と載った。別名が選ぶ版と、許可リストがモデルを止めたときの置き換えも、それぞれ節に分かれた
4. mod で Desktop の Code タブの配色を変える方法（v2.1.324 以降）が載り、プロンプトの上の欄は mod ごとの行を積む形になった（v2.1.323 以降）。ほかの mod の描画と操作をフックするには `{ plugin }` のマッチャーを使う
5. マーケットプレイスの `ref` をコミットの完全な SHA で固定できるようになり（v2.1.324 以降）、managed settings で宣言・有効化し `prependPlugins` か `appendPlugins` に挙げたリモートのマーケットプレイスの mod が、組織のものとして扱われるようになった
```

## ハイライト

1. [**Code Mode のページが加わった**](./latest-detail.md#1-code-mode-のページが加わった):  
  新しいページ `code-mode` は、Claude がツールの呼び出しを JavaScript で書き、Claude Code がそれをセッションで実行する実験的な機能を説明します。要件・オンにする手順・組織でのブロック・許可の確認のされ方・長く動くコードの扱い・トラブルシューティングがまとまり、`auto-mode-config`・`permission-modes`・`hooks`・`env-vars`・`settings-reference`・`feature-availability` にも Code Mode の記述が加わりました
2. [**サンドボックス内の Bash コマンドの自動許可が既定でオフになった**](./latest-detail.md#2-サンドボックス内の-bash-コマンドの自動許可が既定でオフになった):  
  `settings-reference` の `sandbox.autoAllowBashIfSandboxed` の既定が `false` になり、v2.1.324 より前は `true` だった、と載りました。サンドボックスの中の Bash コマンドも通常の許可の流れを通ります。`sandboxing`・`permissions`・`permission-modes`・`security` と、SDK の `SandboxSettings` の既定も追従しています
3. [**サブエージェントのモデルの決まり方が書き直された**](./latest-detail.md#3-サブエージェントのモデルの決まり方が書き直された):  
  `sub-agents` の「Choose a model」が書き直され、入れ子のサブエージェントは既定で起動したサブエージェントのモデルで動く、と載りました。別名が選ぶ版と、許可リストがモデルを止めたときの置き換えはそれぞれ h4 になり、拡張思考は h3「Extended thinking in subagents」に移っています
4. [**Desktop の配色を変える mod とプロンプトの上の mod ごとの行が載った**](./latest-detail.md#4-desktop-の配色を変える-mod-とプロンプトの上の-mod-ごとの行が載った):  
  `plugins/mods/interface` に、Desktop の Code タブの配色を mod で変える節と、配色が出ないとき・外すときの節ができました（v2.1.324 以降）。プロンプトの上の欄は、mod ごとの行を積む形になっています（v2.1.323 以降）。ほかの mod の描画と操作をフックする `{ plugin }` のマッチャーと、背景の `scene` への改名も載りました
5. [**マーケットプレイスのコミットへの固定とリモートの mod を組織のものにする方法が載った**](./latest-detail.md#5-マーケットプレイスのコミットへの固定とリモートの-mod-を組織のものにする方法が載った):  
  `plugins/marketplace-reference` の `ref` に、コミットの完全な SHA を書けるようになりました（v2.1.324 以降）。`plugins/mods/admin` には、リモートのマーケットプレイスの mod を組織のものとして扱う条件（v2.1.324 以降）と、ユーザーの mod が管理の MCP サーバーの接続を止めうること（v2.1.323 以降）が載っています

## 新規追加されたページ

- [**Run tool calls from code with Code Mode**](./latest-detail.md#1-run-tool-calls-from-code-with-code-mode) ([日本語](https://code.claude.com/docs/ja/code-mode) / [English](https://code.claude.com/docs/en/code-mode)):  
  実験的な機能 Code Mode の仕組み・使いどころと制約・要件・試す手順とオフにする方法・許可の確認と長く動くコード・トラブルシューティングをまとめた 223 行のページです（詳細はハイライト 1 参照）

## 大幅に更新されたページ

- [**Draw in the interface with a mod**](./latest-detail.md#1-draw-in-the-interface-with-a-mod) ([日本語](https://code.claude.com/docs/ja/plugins/mods/interface#change-the-colors-of-the-desktop-app) / [English](https://code.claude.com/docs/en/plugins/mods/interface#change-the-colors-of-the-desktop-app)):  
  125 行（追加 109・削除 16）が変わりました。Desktop の配色を変える mod の 3 つの h3 が加わり、プロンプトの上の欄は mod ごとの行になり、背景の `id` は `scene` に替わりました
- [**Create custom subagents**](./latest-detail.md#2-create-custom-subagents) ([日本語](https://code.claude.com/docs/ja/sub-agents#choose-a-model) / [English](https://code.claude.com/docs/en/sub-agents#choose-a-model)):  
  101 行（追加 59・削除 42）が変わりました。「Choose a model」が書き直されて 4 つの h4 と h3「Extended thinking in subagents」ができ、入れ子のサブエージェントは起動したサブエージェントのモデルで動く、と載りました
- [**Manage multiple agents with agent view**](./latest-detail.md#3-manage-multiple-agents-with-agent-view) ([日本語](https://code.claude.com/docs/ja/agent-view#what-deleting-a-session-removes) / [English](https://code.claude.com/docs/en/agent-view#what-deleting-a-session-removes)):  
  75 行（追加 34・削除 41）が変わりました。セッションの削除を拒まれたときの説明が、メッセージごとの 3 つの h5 に整理され、細かい条件の一覧は外れました
- [**Error reference**](./latest-detail.md#4-error-reference) ([English](https://code.claude.com/docs/en/errors#subprocess-initialization-did-not-complete-within-60000ms)):  
  68 行（追加 54・削除 14）が変わりました。VS Code と Agent SDK の起動のタイムアウトと、クラウドのセッションの履歴を読み込めないときの 2 つの h3 が加わり、使用上限・再試行の上限・押されていないコミットの節が書き直されました

## 軽微な更新

今回の差分は **3 ファイル**（`llms.txt`・`llms-full.txt`・見出しマップ）です。`llms.txt` は `code-mode` の行が 1 行加わり（URL は 239 から 240）、末尾の「Indexes」の 11 言語の索引のページ数が 203 から 204 になりました（12 行追加・11 行削除）。`llms-full.txt` では、204 ページのうち **72 ページ**（新しい `code-mode` と changelog を含む）が変わりました。新規の `code-mode` と大幅更新の 4 ページを除く **67 ページ**と、changelog に加わった **v2.1.325（2026年11月13日、139 項目。Added 6・Changed 31・Improvements 14・Bug fixes 88）** を以下にまとめます。単一のリリースなので、各項目への版の併記は省いています。changelog の収録リリースは 440 から 441 になり、先頭は v2.1.325 で、その次は v2.1.323 です（v2.1.324 の項目はありません。通常のページは「v2.1.324 or later」のような要件を 10 ページ 11 か所で使っています）。

`llms-full.txt` の総行数は **127,463 行から 128,207 行へ 744 行増え**ました（生の差分の差し引き 1,437 − 693 と一致）。生の差分 2,130 行の内訳は、`agent-sdk/quickstart` の掲載位置の移動が 710 行（削除 355・追加 355。このページの実際の変更は追加 2 行で、それを含めると 712 行）、新しい `code-mode` が 223 行、changelog の新しいリリースが 155 行、残りの 69 ページが 1,040 行（追加 702・削除 338）です。この 1,040 行のうち 10 行は、`setup` のインストールのコマンドの 5 つのフェンスで `theme={null}` が 1 回から 23 回に重なった行の置き換えです（下の「その他」）。前回の `\_` のエスケープの外れのような、ほかの書式だけの変更は見当たりません。

コードフェンスの外の見出しは、行頭が `#` の見出しだけを数えると 6,069 から 6,112 へ、引用の中の見出しも数えると 6,080 から 6,123 へ、どちらも 43 増えました。加わったのは 44 で、`code-mode` の 17（ページの題を含む）と、既存のページの 27 です（`sub-agents` 5・`plugins/mods/interface` 5・`agent-view` 3・`agent-sdk/typescript` 3・`errors` 2、`artifacts`・`headless`・`plugins/mods/create`・`plugins/mods/events`・`plugins/mods/reference`・`vs-code`・`claude-apps-gateway-config`・`setup`・`tools-reference` が各 1）。外れたのは `artifacts` の「Review the audit log」の 1 つで、`artifacts` の加わった 1 つはその改称です。

**新機能**

- Code Mode のページと関連の記述（`code-mode` ほか。詳細はハイライト 1 参照）
- Desktop の配色を変える mod（`plugins/mods/interface`。詳細はハイライト 4 参照）
- マーケットプレイスの `ref` のコミットの SHA での固定（`plugins/marketplace-reference` ほか。詳細はハイライト 5 参照）
- **VS Code のパネルにプロンプトの提案が載った**（`vs-code` の新しい h3「Use or turn off suggested prompts」）。Claude の返信の後、空のプロンプトの欄に次のプロンプトの提案が灰色の斜体で出ることがあります。提案ごとに短いバックグラウンドの要求が使われ、プランの使用上限か API の費用に数えられます。`Tab` で編集できるテキストにしてから送り（受け入れる前の `Enter` では送られない）、入力を始めると隠れます。オフにするには `~/.claude/settings.json` で `promptSuggestionEnabled` を `false` にし、開いている会話では **Developer: Reload Window** の後に効きます。`CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION` を `true` にしているなら `false` に替えます — [日本語](https://code.claude.com/docs/ja/vs-code#use-or-turn-off-suggested-prompts) / [English](https://code.claude.com/docs/en/vs-code#use-or-turn-off-suggested-prompts)
- **mod が Claude Code 自身の `http.fetch` の要求をフックできると載った**（`plugins/mods/reference` の「Mods API calls」と新しい h4「Fields on Claude Code's own `http.fetch` requests」）。一部のイベントは Claude Code 自身の動作でも発火するので、拒む前に `next.origin.plugin` が `engine` かを確かめます。`http.fetch` のフックでは、`next.origin` の `{ plugin: 'engine', tier: 'core' }` がモデルの要求のような Claude Code 自身の要求を表し、組み込みのガードが読み込まれている所では、組織のものとして扱われる mod だけがこのイベントを受け取ります。`e.init.compress`（フックの後で本文を圧縮するときに付く）と `value.isStreaming`（Claude Code が応答の本文を自分で読むので `value.text` は空）のフィールドの表もあり、v2.1.321 以降が要ります — [日本語](https://code.claude.com/docs/ja/plugins/mods/reference#http-fetch-own-requests) / [English](https://code.claude.com/docs/en/plugins/mods/reference#http-fetch-own-requests)
- **mod のテストに `keepsBeneath()` が載った**（`plugins/mods/test` の「Test a drawing」）。`ui.render` のスタブのないテストで、描画が `next(e)` の返したものを含むと `true` になります（v2.1.321 以降）。「Follow the test kit's rules」も、`next(e)` を返すフックはスタブなしでもマウントできる（v2.1.321 より前は `no implementation for ui.render` で失敗）、スタブは `next(e)` が返す要素を選ぶために登録する、という説明に替わりました — [日本語](https://code.claude.com/docs/ja/plugins/mods/test#test-a-drawing) / [English](https://code.claude.com/docs/en/plugins/mods/test#test-a-drawing)
- **環境変数が 2 つ載った**（`env-vars` の「Variables」）。`CLAUDE_CODE_AUTOMOUNT_ROOTS` は、`CLAUDE.md`・スキル・`.mcp.json` などを作業ディレクトリーより上のフォルダーで探すときに飛ばすオートマウントのルートで、探索がオートマウンターを待つときに設定します（区切りは Unix で `:`、Windows で `;`。シンボリックリンクを含まない絶対パス）。`CLAUDE_CODE_RESUME_HINT_COMMAND` は、Claude Code を起動するラッパーのスクリプトで設定すると、終了時のヒントが `claude --resume <session-id>` ではなく `mytool --resume <session-id>` のようになります（`^\w[\w-]*$` に合わない名前と設定ファイルの `env` の値は無視）。どちらも v2.1.323 以降が要り、前回のサマリで扱った changelog の v2.1.323 で触れられていた変数です — [日本語](https://code.claude.com/docs/ja/env-vars#variables) / [English](https://code.claude.com/docs/en/env-vars#variables)
- [VSCode] ターミナルが提案を出すところでプロンプトの提案を追加。Tab で次のプロンプトの提案を受け入れ、Claude Code の settings.json の `promptSuggestionEnabled: false` でオフにする（上の `vs-code` の項目に対応）
- VS Code など統合ターミナルで、Claude が Jupyter ノートブックを読むか編集した後に、ノートブックのセルの再実行についてのスピナーのヒントを追加
- 組織のポリシーが要求を止めたときのエラーの下に、続け方（`/rewind` してメッセージを変えるか、`/clear` する）を述べる行を追加
- サンドボックスの中の `git checkout`・`git stash`・autostash の pull が `.claude` の中のような保護されたファイルを更新できないとき、Claude への注記を追加
- [VSCode] API キーを作らない Console のサインインを追加
- [VSCode] SSH・WSL・コンテナーのウィンドウで、パネルから MCP サーバーにサインインするとき、リダイレクトの URL を貼り付ける欄を追加

**機能改善**

- サンドボックスの中の Bash コマンドの自動許可が既定でオフ（`settings-reference`・`sandboxing`・`permissions`・`permission-modes`・`security`・`sandbox-environments`・`glossary`・`agent-sdk/python`・`agent-sdk/typescript`。詳細はハイライト 2 参照）
- サブエージェントのモデルの決まり方（`sub-agents`・`agent-sdk/subagents`・`agent-sdk/typescript`・`feature-availability`・`model-config`・`workflows`。詳細はハイライト 3 参照）
- プロンプトの上の mod ごとの行・背景の `scene`・ほかの mod をフックするマッチャー（`plugins/mods/interface`・`plugins/mods/events`・`plugins/mods/reference`・`plugins/mods/troubleshoot`・`plugins/mods/test`・`plugins/mods/admin`。詳細はハイライト 4 参照）
- リモートのマーケットプレイスの mod を組織のものにする条件と、管理の MCP サーバーを止めうるユーザーの mod（`plugins/mods/admin`・`plugins/marketplace-reference`・`settings-reference`・`plugins/cli-reference`。詳細はハイライト 5 参照）
- セッションの削除を拒まれたときの説明（`agent-view`・`cli-reference`。詳細は大幅更新 3 参照）
- VS Code と Agent SDK の起動のタイムアウト・クラウドのセッションの履歴・使用上限・再試行の上限・押されていないコミット（`errors`・`vs-code`・`env-vars`。詳細は大幅更新 4 参照。`vs-code` の「Fix common issues」の表にも起動のタイムアウトの行が加わった）
- **Claude が書いた mod を尋ねずに読み込むセッションが載った**（`plugins/mods/create` の新しい h3「Sessions that load a mod without asking」）。`auto` と `bypassPermissions` のモードでは、Claude Code は尋ねずにホットリロードをオンにでき、mod はターンの終わりに読み込まれます。セッションを再開すると（対話でも `claude -p` でも）、その mods のフォルダーに既にある mod は尋ねずに読み込まれうるので、読み込ませないにはそのディレクトリーを消します。「Ask Claude for a mod」は、先に尋ねてほしければ `default` か `acceptEdits` のモードで新しいセッションを始めるか、セッションの最初の mod を頼む前にどちらかへ切り替える、という説明になり、読み込めないセッションの一覧も、`dontAsk` モードか、mod を書く `claude -p` の実行（`default` か `acceptEdits` のモードでホットリロードの質問を出せない）、信頼していないワークスペースの対話のセッション、に改められました — [日本語](https://code.claude.com/docs/ja/plugins/mods/create#sessions-that-skip-the-approval) / [English](https://code.claude.com/docs/en/plugins/mods/create#sessions-that-skip-the-approval)
- **mod のツールの呼び出しと再読み込みの説明が改められた**（`plugins/mods/reference`・`env-vars`・`skills`）。`$.tool` の `call` が人の承認を要するとき（フックか組織が `ask` と答えるときなど）は、`{ deny: "<tool> wasn't run: this call needs a person's approval, and a mod's own call can't ask for it." }` で解決します。`CLAUDE_CODE_PLUGIN_DIR_WATCH` は、既定でスキルのディレクトリーの mod が 2 つ以上のプロンプトを受けるセッション（非対話を含む）で再読み込みされ、`--plugin-dir` の mod は対話のターミナルのセッションでだけ再読み込みされる、`1` でスキルのディレクトリーと同じにし、`0` でどこでもオフ、という説明になりました。`skills` の「Edit a skill during a session」の注記も、`hooks/` の変更には `/reload-plugins` が要るが、自分で再読み込みする mod のモジュールのファイルは除く、と改められています — [日本語](https://code.claude.com/docs/ja/env-vars#variables) / [English](https://code.claude.com/docs/en/env-vars#variables)、[日本語](https://code.claude.com/docs/ja/plugins/mods/reference#mods-api-methods) / [English](https://code.claude.com/docs/en/plugins/mods/reference#mods-api-methods)
- **agent teams の分割ペインを手順で設定するようになった**（`agent-teams` の「Choose a display mode」）。①tmux か iTerm2 を用意する（iTerm2 は `it2` の CLI を入れ、**iTerm2 > Settings > General > Magic > Enable Python API** を有効にする）、②`~/.claude/settings.json` で `teammateMode` を `"auto"` にする（tmux か iTerm2 の中で動かすと分割ペインになり、ほかのターミナルでは in-process のまま）、③その中で `claude` を始めてチームメイトを起動する（iTerm2 で `it2` のセットアップの確認が出たら **Install it2 now** を選ぶ）。tmux と iTerm2 の外では `"tmux"` にすると別の tmux のセッションでペインが開き、Claude Code のプロンプトの `View teammates` の行のコマンドを 2 つ目のターミナルで実行して見ます。iTerm2 の窓でペインが開かなければ `"iterm2"` にします。「Limitations」からは、分割ペインは VS Code の統合ターミナル・Windows Terminal・Ghostty では使えない、という文が外れました — [日本語](https://code.claude.com/docs/ja/agent-teams#choose-a-display-mode) / [English](https://code.claude.com/docs/en/agent-teams#choose-a-display-mode)
- **SDK のファイルのチェックポイントは「ターンを始めるプロンプト」のユーザーメッセージだと明記された**（`agent-sdk/file-checkpointing`）。ツールの結果を運ぶユーザーメッセージにも UUID はありますが、チェックポイントではありません。例のコードも、Python は `tool_use_result` と `parent_tool_use_id` が `None` のユーザーメッセージだけ、TypeScript は `isReplay` のユーザーメッセージだけを記録する形になり、「"No file checkpoint found for this message" error」の原因に、ツールの結果を運ぶユーザーメッセージの UUID を使った場合が加わりました — [日本語](https://code.claude.com/docs/ja/agent-sdk/file-checkpointing#how-checkpointing-works) / [English](https://code.claude.com/docs/en/agent-sdk/file-checkpointing#how-checkpointing-works)
- **Agent SDK の `startup()` と `prewarm()` の初期化の時間が載った**（`agent-sdk/typescript`）。`startup()` の「Parameters」に、`initializeTimeoutMs` を未設定にしたときだけ、遅い SessionStart と Setup のコマンドフックが追加の時間を得る（これらのフックの時間は 60 秒の既定に最大 10 分まで数えないので、初期化は最大 11 分）、値を設定すると（`60000` でも）それが上限になる、と加わりました（TypeScript の Agent SDK v0.3.304 以降）。`prewarm()` は「Parameters」「Returns」「How a spare works」の h4 に分かれ、`prewarm()` では Setup のフックの時間を未設定でも `initializeTimeoutMs` に数える、と加わっています — [日本語](https://code.claude.com/docs/ja/agent-sdk/typescript#how-a-spare-works) / [English](https://code.claude.com/docs/en/agent-sdk/typescript#how-a-spare-works)
- **カスタムツールの `always_deny` は、ツールを Claude のコンテキストから外すようになった**（`agent-sdk/typescript` の「`permission_policy` values」・`agent-sdk/custom-tools`・`agent-sdk/permissions`）。`bypassPermissions` を含むすべての権限モードで外し、Claude Code v2.1.324 以降が要ります。これまでは、呼び出しは拒まれるが、読み込んだプラグインの mod は承認できる、としていました。`agent-sdk/permissions` からは、`always_deny` のツールの呼び出しはこの段階で拒まれる、という文が外れています。日本語版はまだこの内容になっていなかったので、英語版だけをリンクしています — [English](https://code.claude.com/docs/en/agent-sdk/typescript#permission-policy-values)
- **SDK のクイックスタートに `tools` と `allowedTools` の違いが加わった**（`agent-sdk/quickstart` の「Key concepts」）。組み込みのツールをその組に絞るには `tools` に渡し、`allowedTools` に挙げると事前承認になるだけで、ほかのツールも権限モードに従って呼べます — [日本語](https://code.claude.com/docs/ja/agent-sdk/quickstart#key-concepts) / [English](https://code.claude.com/docs/en/agent-sdk/quickstart#key-concepts)
- **安定版のチャネルへの切り替えと最低の版の固定が書き直された**（`setup` の「Configure release channel」「Pin a minimum version」と新しい h4「Set version limits for your organization」・`settings-reference` の「`minimumVersion`」）。ネイティブのインストールは、安定版が今の版より古くてもそこへ更新されるので、ダウングレードを避けるには `minimumVersion` を今の版にします。`/config` では **Auto-update channel** を stable にして **Stay on current version** を選び、設定ファイルでは `claude --version` の版を `minimumVersion` に、`autoUpdatesChannel` を `"stable"` にします。例の版は 2.1.100 から 2.1.323 になり、組織の最低の版を managed settings で強制する説明は新しい h4 に移りました — [日本語](https://code.claude.com/docs/ja/setup#pin-a-minimum-version) / [English](https://code.claude.com/docs/en/setup#pin-a-minimum-version)
- **Claude apps gateway が新しい Claude Desktop のキーを知らなくても起動するようになった**（`claude-apps-gateway-config` の新しい h5「Keys the gateway doesn't know」ほか）。Claude Code v2.1.295 以降のゲートウェイでは、新しい Claude Desktop のリリースのキーの多くにゲートウェイの更新が要らず、v2.1.321 以降では既知のキーの中の新しいサブキーの多くも同じです。既知のキーの決まった値の一覧にない新しい値と、`desktop` のブロックに書けるキーの綴り違いらしいもの（`disableAutoUpdates` に対する `disable_auto_updates` など。エラーが名前を提案する）は、引き続き起動で失敗します。v2.1.300 からは `selfHosted` で始まるキーも起動で失敗し、ゲートウェイを更新する前に外します。「File structure」の、未知のキーは起動で失敗する、という文は外れました。「Per-developer AWS cost attribution」には、`aws_bearer_token` を使う `bedrock` と `mantle` の上流は `assume_role` を取れず要求が 1 つのプリンシパルに残る、という注記が、「Context window in terminal sessions」には、Claude Code は別名の `upstream_model` からコンテキストウィンドウを決めない、という注記が加わっています — [日本語](https://code.claude.com/docs/ja/claude-apps-gateway-config#claude-desktop-overlay) / [English](https://code.claude.com/docs/en/claude-apps-gateway-config#claude-desktop-overlay)
- **Desktop の Cowork は `allowedProviders` で `"anthropic"` に当たると載った**（`settings-reference` の「`allowedProviders`」・`llm-gateway` の「Roll out a gateway」・`third-party-integrations` の「Configure security policies」）。claude.ai にサインインした Desktop のユーザーのマシンの Cowork のセッションは `"anthropic"` として扱われ、MDM のポリシーか managed settings のこの一覧から外すと拒まれます。入れると、Anthropic に直接送るセッションもこの一覧を通ります — [日本語](https://code.claude.com/docs/ja/settings-reference#allowedproviders) / [English](https://code.claude.com/docs/en/settings-reference#allowedproviders)、[日本語](https://code.claude.com/docs/ja/llm-gateway#roll-out-a-gateway) / [English](https://code.claude.com/docs/en/llm-gateway#roll-out-a-gateway)
- **プッシュ通知の設定はキーだけでは届かないと載った**（`settings-reference` の「`agentPushNotifEnabled`」「`inputNeededNotifEnabled`」）。通知を受けるには「Mobile push notifications」の手順に従う、と加わり、`agentPushNotifEnabled` からは `/config` で変えるとアカウントにも保存される、という文が外れました — [日本語](https://code.claude.com/docs/ja/settings-reference#agentpushnotifenabled) / [English](https://code.claude.com/docs/en/settings-reference#agentpushnotifenabled)
- **フックの `onFailure` の既定の書き方が改められた**（`hooks` の「HTTP hook fields」・`hooks-guide` の「HTTP hooks」）。`onFailure` の説明から「`"continue"`, the default」が外れ、`"block"` と未設定の場合はリンク先を見る、となりました。`hooks-guide` の HTTP フックも、失敗が操作を止めるフックでない限り操作は続く、と改められています — [日本語](https://code.claude.com/docs/ja/hooks#block-the-action-when-a-hook-fails) / [English](https://code.claude.com/docs/en/hooks#block-the-action-when-a-hook-fails)
- **保護したファイルへの編集を止めるフックの限界が載った**（`hooks-guide` の「Block edits to protected files」）。この例が止めるのは `Edit` と `Write` のツールで、Claude はシェルのコマンドでファイルを変えられます。一部のコマンドを止めるには `.claude/settings.json` の `permissions.deny` にパスごとの `Edit` の deny ルール（プロジェクトのルートの `.env` なら `Edit(/.env)`）を加え、それでも変えうるので、コマンドが書き込めるファイルを絞るにはサンドボックスを見る、と加わりました — [日本語](https://code.claude.com/docs/ja/hooks-guide#block-edits-to-protected-files) / [English](https://code.claude.com/docs/en/hooks-guide#block-edits-to-protected-files)
- **MCP タスクの質問を後で答えられるようになった**（`mcp` の「Answer a question from an MCP task」・`hooks` の「Elicitation output」）。結果を待つよう設定していない限り、ダイアログで `Esc` を押すと後で答えることになり、`/tasks` でタスクの詳細を開いて `Enter` を押すと質問がまた出ます（v2.1.324 以降）。これまでは、断ることも `Esc` もサーバーへの答えになる、としていました。`hooks` からも、ダイアログの **Decline** は `decline`、`Esc` は `cancel` を送る、という文が外れています。日本語版はまだこの内容になっていなかったので、英語版だけをリンクしています — [English](https://code.claude.com/docs/en/mcp#answer-a-question-from-an-mcp-task)
- **`--strict-mcp-config` の説明が言い換えられた**（`cli-reference`・`agent-view`・`mcp` の「Project scope」・`agent-sdk/python`・`agent-sdk/typescript`）。「`--mcp-config` のサーバー「だけ」を使う」から、「`.mcp.json`・`~/.claude.json`・プラグインなどで設定したサーバーを飛ばし、`--mcp-config` で渡したものを読み込む」という言い方になりました。`mcp` からは、v2.1.246 より前は厳格なセッションでも承認を待った、という文が外れています — [English](https://code.claude.com/docs/en/cli-reference#cli-flags)
- **Desktop の Code タブの MCP の重複の扱いの記述が外れた**（`desktop` の「MCP servers from the Claude Desktop chat app」・`mcp` の「Scope hierarchy and precedence」）。同じサーバー名を `claude_desktop_config.json` と `~/.claude.json` か `.mcp.json` に定義したときと、`~/.claude.json` と `.mcp.json` に同じ stdio サーバー名があるときに、Code タブがどちらの定義を使うか、という段落が外れました — [日本語](https://code.claude.com/docs/ja/desktop#mcp-servers-from-the-claude-desktop-chat-app) / [English](https://code.claude.com/docs/en/desktop#mcp-servers-from-the-claude-desktop-chat-app)
- **組織へのサインインの制限とサードパーティのプロバイダーの関係が載った**（`desktop` の「Restrict sign-in to your organization」）。確かめるケースが 3 つになり、アプリの中で自分のサードパーティの推論の構成を設定した人は、このキーを配ると次の起動からその構成が無視されるので、Amazon Bedrock・Agent Platform・Microsoft Foundry・LLM ゲートウェイを使わせ続けるには、同じ Claude Desktop のポリシーで構成を配る、と加わりました — [日本語](https://code.claude.com/docs/ja/desktop#restrict-sign-in-to-your-organization) / [English](https://code.claude.com/docs/en/desktop#restrict-sign-in-to-your-organization)
- **`CLAUDE_CODE_MAX_CONTEXT_TOKENS` が認識されない `claude-` の ID にも効くようになった**（`model-config` の「Which IDs `CLAUDE_CODE_MAX_CONTEXT_TOKENS` applies to」）。認識されない ID（`[1m]` なし）では変数がそのまま効き、`claude-sonnet-latest` のような ID には v2.1.324 以降が要ります。これまでの、プロバイダーかカスタムの綴りとみなす条件と、接尾辞のない裸の `claude-` の名前は `DISABLE_COMPACT` が要る、という区別は外れました。日本語版はまだこの内容になっていなかったので、英語版だけをリンクしています — [English](https://code.claude.com/docs/en/model-config#which-ids-claude_code_max_context_tokens-applies-to)
- **529 の再試行の間隔の上限を 300000 まで上げられるようになった**（`env-vars` の `CLAUDE_CODE_OVERLOADED_RETRY_MAX_DELAY_MS`・`errors` の「Tune retry behavior」）。32000〜300000 のミリ秒を受け付け、64000 を超える値には v2.1.323 以降が要ります。`CLAUDE_CODE_OVERLOADED_RETRY_BASE_DELAY_MS` と合わせて、効かない場合の説明は `errors` へのリンクになりました — [日本語](https://code.claude.com/docs/ja/env-vars#variables) / [English](https://code.claude.com/docs/en/env-vars#variables)
- **`CLAUDE_CODE_SYNC_SKILLS` が対話のセッションでも使えるようになった**（`env-vars`）。`1` で claude.ai のアカウントで有効なスキルをダウンロードし、`-p` の非対話のモードでは最初のクエリの前にスキルの一覧を待ちます。対話のセッションでは v2.1.323 以降が要ります。`CLAUDE_CODE_DISABLE_LEGACY_MODEL_REMAP` の「古いモデルを固定したいときに使う」という文も外れました — [日本語](https://code.claude.com/docs/ja/env-vars#variables) / [English](https://code.claude.com/docs/en/env-vars#variables)
- **注入するコマンドの許可の確認で `allowed-tools` が効かない場合が載った**（`skills` の「Permission checks on injected commands」）。事前承認の限界として、deny と ask のルール、管理のルールだけが効く場合（`/status` が `allowed-tools ignored this session` の下にスキルを挙げる）、bare リポジトリらしいフォルダー（`HEAD` のファイルが `refs` か `commondir` のすぐ横にある）の 3 つが箇条書きになりました。最も近いリポジトリが bare に見えると、`git` を含むか解析できない Bash コマンドには `allowed-tools` が無視されるので、信頼するなら `/permissions` で許可します。「Bundled skills」からは、`/verify` などは呼び出したときだけ動く、という言葉が外れています。日本語版はまだこの内容になっていなかったので、英語版だけをリンクしています — [English](https://code.claude.com/docs/en/skills#permission-checks-on-injected-commands)
- **バックグラウンドのサブエージェントの長いコマンドに時間を与える方法が載った**（`headless` の「Background tasks at exit」と新しい h4「Give a long subagent command more time」）。終了時のバックグラウンドのサブエージェントとワークフローは、それぞれ終わるか 10 分の上限が待ちを終えるまで実行を開いたままにする、と改められました（これまでは完了するまで）。サブエージェントの長いコマンドがタイムアウトでバックグラウンドへ移ると、`claude -p` はそれが終わる前に終了コード 0 で終わりうるので、`BASH_DEFAULT_TIMEOUT_MS`（例: `BASH_DEFAULT_TIMEOUT_MS=300000 claude -p "<prompt>"`）で既定のタイムアウトをコマンドの時間より長くします。「Create a commit」の `/config` の例は `/config verbose=true` になりました — [日本語](https://code.claude.com/docs/ja/headless#give-a-long-subagent-command-more-time) / [English](https://code.claude.com/docs/en/headless#give-a-long-subagent-command-more-time)
- **OTLP のプロトコルの既定と、mod のモデルの要求の計測が載った**（`monitoring-usage`）。`OTEL_EXPORTER_OTLP_PROTOCOL` は有効な `http://` か `https://` のエンドポイントで既定が `http/protobuf` になり、`http://localhost:4317` のような gRPC のエンドポイントでは `grpc` にします（v2.1.323 以降）。これまでは既定のプロトコルはない、としていました — [日本語](https://code.claude.com/docs/ja/monitoring-usage#common-configuration-variables) / [English](https://code.claude.com/docs/en/monitoring-usage#common-configuration-variables)。費用とトークンのカウンターの `query_source` には、mod の `$.model.complete` と `$.model.classify` の要求を表す `plugin_model_complete` と `plugin_model_classify` が加わり、v2.1.324 から数えるので更新の後に合計が増えうる、`plugin.name` もその `$.model` の呼び出しをしたプラグインを含む、となりました（この部分は日本語版がまだ追従していないので英語版だけ） — [English](https://code.claude.com/docs/en/monitoring-usage#cost-counter)。「Attribute telemetry to Desktop SSH sessions」には、値に空白があるときはリモートのマシンのセッションで `/status` を実行するとどの値か分かる、と加わっています
- **server-managed settings の取得にプロキシが要るときの設定が整理された**（`server-managed-settings` の「Fetch and caching behavior」）。エンドポイントの managed の `env`（v2.1.223 以降）・シェルの環境・ユーザー設定のいずれかで `HTTPS_PROXY` を設定し、`ALL_PROXY` がプロキシを名指していても `HTTPS_PROXY` を設定する、と改められました — [日本語](https://code.claude.com/docs/ja/server-managed-settings#fetch-and-caching-behavior) / [English](https://code.claude.com/docs/en/server-managed-settings#fetch-and-caching-behavior)
- **リモートの MCP サーバーへのサインインにもプロキシと証明書の変数が当たると載った**（`network-config`）。プロキシ・CA・クライアント証明書の変数はリモートの MCP サーバーへのサインインの要求にも当たり、`claude mcp login` では、シェル・`~/.claude/settings.json`・managed settings のファイルで設定し、プロジェクトとローカルの設定では設定しません。冒頭の説明は短くなりました。日本語版はまだこの内容になっていなかったので、英語版だけをリンクしています — [English](https://code.claude.com/docs/en/network-config#proxy-configuration)
- **セルフホストのランナーのアイドルの判定が細かくなった**（`self-hosted-environments-deploy` の「Some sessions don't count as idle」）。ターンが終わったかユーザーを待っている間はアイドルですが、ターンが終わってもバックグラウンドのタスクが動いている場合、MCP でないツールが動作中に求めた承認をターンが待っている場合、MCP サーバーの `elicitation/create` の要求をターンが待っている場合は、アイドルになりません。プロキシの認証のトークンを替えたとき、既に開いている接続は古いトークンのまま使える、とも加わりました — [日本語](https://code.claude.com/docs/ja/self-hosted-environments-deploy#some-sessions-don’t-count-as-idle) / [English](https://code.claude.com/docs/en/self-hosted-environments-deploy#some-sessions-don’t-count-as-idle)
- **サンドボックスを使うと worktree の名前を再利用できない条件が載った**（`worktrees` の「Reuse a worktree name」）。名前を再利用する条件に、セッションでサンドボックスがファイルの書き込みを制限しておらず、worktree とメインのチェックアウトの `.claude` の設定ファイルがサンドボックスを有効にしていないこと、が加わりました。サンドボックスと `"fresh"` の起点を使うなら、`git fetch origin` を実行して `--worktree` に新しい名前を渡します — [日本語](https://code.claude.com/docs/ja/worktrees#reuse-a-worktree-name) / [English](https://code.claude.com/docs/en/worktrees#reuse-a-worktree-name)
- **Perforce の読み取り専用のファイルを守る節ができた**（`tools-reference` の新しい h3「Protect read-only files in Perforce」）。`CLAUDE_CODE_PERFORCE_MODE` を `1` にすると、Edit・Write・NotebookEdit は Perforce のワークスペースの読み取り専用のファイルを変えず、先に `p4 edit` を実行するよう Claude に伝えます（変数自体は以前から `env-vars` にあります）。「Time limit for background commands」からは、`-p` の実行が結果の後でバックグラウンドのコマンドを待つから、という理由の言葉が外れました。日本語版はまだこの節がなかったので、英語版だけをリンクしています — [English](https://code.claude.com/docs/en/tools-reference#protect-read-only-files-in-perforce)
- **プラグインの MCP バンドルの展開先が替わった**（`plugins/manifest-reference` の「`mcpServers`」・`plugins/loading` の「Find plugins on disk」・`claude-directory` の「Cleaned up automatically」）。`.mcpb` か `.dxt` のバンドルは、プラグインのルートの `.mcpb-cache/` ではなく、プラグインのディレクトリーの `mcpb/` に展開されます（v2.1.324 以降）。`plugins/mcpb/` は自動の掃除の対象になり、バンドルの古さは最後に使ったセッションから数えます。日本語版はまだこの内容になっていなかったので、英語版だけをリンクしています — [English](https://code.claude.com/docs/en/plugins/manifest-reference#mcpservers)、[English](https://code.claude.com/docs/en/plugins/loading#find-plugins-on-disk)
- **mod が加えるツールの MCP サーバーは managed-mcp.json の排他の制御でも読み込まれると載った**（`managed-mcp` の「Exclusive control with managed-mcp.json」）。mod がツールを加えるときに Claude Code が作るサーバーもこの一覧に入り、ユーザーの mod が加えるツールを止めるには、ユーザーがインストールした mod の読み込みを止めます。「Choose a pattern」の Fixed deployment は、ユーザーが設定したサーバーは読み込まれない、という言い方になりました — [日本語](https://code.claude.com/docs/ja/managed-mcp#exclusive-control-with-managed-mcp-json) / [English](https://code.claude.com/docs/en/managed-mcp#exclusive-control-with-managed-mcp-json)
- **VS Code の拡張機能も同じフォルダーの信頼を求めると載った**（`permissions` の「Project allow rules and workspace trust」）。拡張機能はセッションを始める前に `Trust this folder in Claude Code?` のダイアログで信頼を求めます — [日本語](https://code.claude.com/docs/ja/permissions#project-allow-rules-and-workspace-trust) / [English](https://code.claude.com/docs/en/permissions#project-allow-rules-and-workspace-trust)
- **アーティファクトの監査が Compliance API の Activity Feed になった**（`artifacts` の「Review the audit log」→「Audit artifact activity with the Compliance API」）。Enterprise のプランでは、Compliance API の Activity Feed で誰がアーティファクトを公開・共有・削除したかを見ます。絞り込む活動の種類は、Activity Feed のリファレンスの `activity_types` で `artifact` を含む名前を探します。これまでの、組織の監査ログの `claude_artifact_*` のイベントに出る、という説明は外れました — [日本語](https://code.claude.com/docs/ja/artifacts#audit-artifact-activity-with-the-compliance-api) / [English](https://code.claude.com/docs/en/artifacts#audit-artifact-activity-with-the-compliance-api)
- **Remote Control が `/resume` と `/teleport` で切断する場合が載った**（`remote-control` の「What connected devices see」・`errors` の「Find your error」）。接続したセッションに共有リンクがあるか、それを確かめられないとき、どちらかのコマンドが別の会話を開くと Remote Control は切断します（リンクを持つ人にその会話が見えてしまうため）。新しい会話をつなぐにはターミナルで `/remote-control` を実行し、共有リンクの確認には v2.1.324 以降が要ります。「Limitations」の `/usage-credits` は、ブラウザーを開く代わりに課金の URL を出す、から、使用量クレジットの管理の場所などをテキストで答える、になりました。日本語版はまだこの内容になっていなかったので、英語版だけをリンクしています — [English](https://code.claude.com/docs/en/remote-control#what-connected-devices-see)
- **ブラウザーを開けないときに `/upgrade` が URL を出すようになった**（`commands` の「All commands」）。SSH の上などでページを開けないときは、サインインのプロンプトの上にページの URL を出します（v2.1.323 以降）。`/usage-credits` の説明は短い文に分かれ、`/stickers` は「Order Claude Code stickers」から「Check Claude Code sticker availability」になりました — [日本語](https://code.claude.com/docs/ja/commands#all-commands) / [English](https://code.claude.com/docs/en/commands#all-commands)
- **プレリリースの機能の一覧に auto モードのサーバー側の審査が加わった**（`llm-gateway-protocol` の「Disable pre-release capabilities」）。審査が続くセッション（`/status` の **Auto mode server** が `Enabled`）での `anthropic-beta` の値と `safeguards` のフィールドが一覧に加わり、セッションの前に `CLAUDE_CODE_AUTO_MODE_SERVER=0` にすると審査がオフになる（ターミナルの `/status` では `Disabled`）、とされています — [日本語](https://code.claude.com/docs/ja/llm-gateway-protocol#disable-pre-release-capabilities) / [English](https://code.claude.com/docs/en/llm-gateway-protocol#disable-pre-release-capabilities)
- **GitHub App の権限に Dependabot alerts が加わった**（`github-actions` の「GitHub App permissions」）。読み取りの権限です — [日本語](https://code.claude.com/docs/ja/github-actions#github-app-permissions) / [English](https://code.claude.com/docs/en/github-actions#github-app-permissions)
- **安全な配置の例のプロセス数の上限が 600 になった**（`agent-sdk/secure-deployment` の「Containers」）。`--pids-limit 100` が `--pids-limit 600` になり、説明もプロセスとスレッドを制限する、となりました — [日本語](https://code.claude.com/docs/ja/agent-sdk/secure-deployment#containers) / [English](https://code.claude.com/docs/en/agent-sdk/secure-deployment#containers)
- **プラグインの信頼の警告の文が替わった**（`plugins/security` の「Trust warning before you install」）。警告の先頭に「Plugins can run code on your computer, with access to your files and shell.」が加わりました。日本語版はまだこの内容になっていなかったので、英語版だけをリンクしています — [English](https://code.claude.com/docs/en/plugins/security#trust-warning-before-you-install)
- **キーバインドの修飾キーの綴り違いの扱いが改められた**（`keybindings` の「Validation」）。`ctl+k` のような綴り違いでは、Claude Code はその組み合わせ全体を無視するので、`ctrl+k` に直します。これまでは、認識しない部分を捨てて残りのキー（この例では `k`）に当てる、としていました — [日本語](https://code.claude.com/docs/ja/keybindings#validation) / [English](https://code.claude.com/docs/en/keybindings#validation)
- **チェックポイントの冒頭に `/rewind` と `/undo` が載った**（`checkpointing`）。編集を元に戻すには、セッションで `/rewind` かその別名 `/undo` を実行して巻き戻しのメニューを開きます。日本語版はまだこの内容になっていなかったので、英語版だけをリンクしています — [English](https://code.claude.com/docs/en/checkpointing#rewind-and-summarize)
- **フックとスキルの組み合わせの説明が改められた**（`features-overview` の「Compare similar features」）。「Hook output lands in context.」が「Pair a hook with a skill.」になり、`PostToolUse` フックでリンターを走らせてエラーを Claude に送り（終了コード 2 の挙動へのリンク）、直し方の自分の規則は `/fix-lint` のようなスキルに書く、という説明になりました — [日本語](https://code.claude.com/docs/ja/features-overview#compare-similar-features) / [English](https://code.claude.com/docs/en/features-overview#compare-similar-features)
- 出力トークンの上限で切れたサブエージェントは、答えの末尾だけを返す代わりに、答え全体をより短く求め直されるようになった
- キーのない Console のサインインかほかの Anthropic のプロファイルのログインでの起動で、まだ有効なトークンを資格情報のロックを待たずに読むようになった
- アカウントのメールアドレスの確認が、コマンドが実行するスクリプト・ファイルの書き込み・Web の取得・MCP の呼び出しでも、自分のメールアドレスをクライアントの識別子として使うことを拒むようになった
- 非公開のプラグインのマーケットプレイスの `HTTPS authentication failed` のメッセージが、git のターミナルのプロンプトと askpass のプログラムがオフになっていると述べ、新しい git でも出るようになった
- マーケットプレイスの追加の確認・プラグインの推奨のプロンプト・プラグインのインストールの警告が、プラグインはファイルとシェルにアクセスしてコンピューターでコードを実行できる、と述べるようになった（上の `plugins/security` の項目に対応）
- `claude --desktop` のサインインのエラーが、Claude のアカウントでのサインインを妨げる API キー・プロバイダー・設定を名指すようになった
- macOS と Windows の `/voice` の「No audio detected」のメッセージが、マイクを選ぶ場所を述べるようになった
- MCP タスクが答えを待っていると Claude に伝わり、Claude が `/tasks` を案内できるようになった
- `claude remote-control` が、自分で止まったときは終了ステータス 4（単一セッションの実行は引き続き 0）、登録できないときは 69 で終わるようになり、サービスマネージャーが起動し直せる
- バックグラウンドのセッションがそのセッションの API キーかトークンを使えないときのメッセージが、設定にキーを加えるよう勧めなくなった
- 同梱の dataviz スキルの、静止画と、年齢帯のような自然な順序のある部分についての、部分と全体の助言を改善
- [VSCode] 信頼していないフォルダーの注記が、拡張機能がオフの理由とオンにする方法を述べるようになった
- [VSCode] システムが Claude Code の実行を拒んだときのエラーが、IT チームがブロックされたプログラムを許可できると述べるようになった
- [VSCode] ブラウザーが localhost の接続のエラーを出したときにすることを、サインインのカードが述べるようになった
- サンドボックスの中の Bash コマンドが既定で通常の許可の流れに従うよう変更。プロンプトなしで走らせ続けるには `sandbox.autoAllowBashIfSandboxed: true` にする（詳細はハイライト 2 参照）
- サンドボックスをオンにする managed settings では、プロンプトなしで走らせ続けるには最上位の managed のソースで `sandbox.autoAllowBashIfSandboxed: true` にするよう変更（詳細はハイライト 2 参照）
- プロジェクトのものでも信頼したものでもないリポジトリでは、読み取り専用の git コマンドも先に尋ねるよう変更。プロンプトなしで走らせるには、`additionalDirectories` の設定ではなく `--add-dir` でそのリポジトリを名指す
- スケジュールしたタスクと `/loop` が、`allowed-tools` かフックを宣言するスキルを実行する前に尋ねるよう変更。無人で走らせるには `permissions.allow` に `Skill(name)` を加える
- Desktop・IDE・SDK のホストの「Always allow」で、保存すればそのコマンドを再び許可する場合にだけルール単独を提示するよう変更。それに頼っていたスケジュールしたタスクは待つことがある
- 追加したディレクトリーの `.claude` の設定・スキル・エージェント・コマンド・フックへのサンドボックスの中の書き込みを、起動したフォルダーと同じく拒むよう変更
- 分離した worktree のセッションかエージェントで、`git bisect run`・`git maintenance register|start`・`scalar` のセットアップのコマンドを拒み、まだ使えるものを伝えるよう変更
- プラグインの MCP バンドル（`.mcpb`・`.dxt`）を、プラグインのフォルダーの `.mcpb-cache` ではなくプラグインのディレクトリーの下に展開するよう変更。読み取り専用のプラグインのフォルダーも読み込め、URL で取得したものは一度だけ再ダウンロードされる（上の MCP バンドルの項目に対応）
- managed settings が宣言・有効化し `prependPlugins` か `appendPlugins` に挙げたリモートのマーケットプレイスのプラグインを、組織のものとして扱うよう変更。`pluginDigests` は非推奨になり無視される（詳細はハイライト 5 参照）
- プラグインの読み込みが、プラグインのフォルダーの一部の安全でないパスとリンクを飛ばし、`claude plugin validate` がそれを報告するよう変更
- `--plugin-dir` のプラグインの `.claude/skills` のフォルダーを、それより上で始めたセッションからは読み込まないよう変更。プラグインのフォルダーで Claude Code を始める
- EnterWorktree が、プロジェクトの中のシンボリックリンクを通る `WorktreeCreate` フックのパスを拒むよう変更。フックには実際のパスを出力させる
- tmux と iTerm2 のチームメイトと、agents のビューで ← で開いた新しいセッションが、シェルが最後に `cd` した場所ではなくセッションのフォルダーで始まるよう変更
- バックグラウンドかスケジュールしたタスクが始めたターンが 8 回続いた後、ターミナルのプロンプトの提案の更新を減らすよう変更。キーを押すかターミナルに戻るまで使用量を節約する
- バックグラウンドの MCP タスクの質問での Esc を「後で答える」に変更。サーバーには何も送られず、質問は `/tasks` に残る（上の MCP タスクの項目に対応）
- `CLAUDE_CODE_MAX_CONTEXT_TOKENS` が、`claude-` で始まる認識されないモデル ID（ゲートウェイの `claude-sonnet-latest` など）のコンテキストウィンドウも設定するよう変更（上の `model-config` の項目に対応）
- `/login` がプライバシーの設定を変える許可を求めるよう変更
- `/cost`・`$.session.usage()`・`--max-budget-usd` と費用・トークンのメトリクスが、mod の `$.model.complete` と `$.model.classify` の呼び出しを数えるよう変更（上の `monitoring-usage` の項目に対応）
- Claude Code のサンドボックスが自分のために始めるプログラム（ネットワークのブリッジなど）を、環境に Claude Code のサインインのトークンと API キーを持たせずに動かすよう変更
- ripgrep・ローカルの git コマンド・サンドボックスのランタイムの補助のプログラムを、環境に mTLS のクライアントの鍵のパスフレーズを持たせずに動かすよう変更
- Remote Control: 接続したセッションに共有リンクがあるか、それを確かめられないとき、`/resume` と `/teleport` が先に切断するよう変更。もう一度つなぐには `/remote-control` を実行する（上の `remote-control` の項目に対応）
- Claude Code on the web・クラウドのスケジュールしたタスク・Cowork のクラウドのセッションが、`sandbox.failIfUnavailable` があっても始まるよう変更。ホストされたコンテナーにはコマンドのサンドボックスがない
- クラウドかセルフホストのセッションの接続を通じた、設定・許可のルール・フック・状態の要求が、返すものを減らすか拒まれるよう変更。セッションで適用されるものは変わらない
- キャッシュしたアカウントのデータがない `claude -p` が、最初の要求の前にそのデータを待つよう変更。きれいな環境での最初の実行は数秒遅れて始まることがある
- 残したいファイルは、消されうる一時的なスクラッチパッドのフォルダーに置かないよう、Claude への指示を変更
- マーケットプレイスの `ref` が、ブランチかタグにある任意のコミットの完全な ID を受け付けるよう変更。この版より前のクライアントはその固定をクローンできず、そこではそう固定したマーケットプレイスが読み込まれなくなる（詳細はハイライト 5 参照）
- `ALL_PROXY` だけがプロキシとして設定されているとき、プラグインのマーケットプレイスとプラグインのダウンロードが CONNECT のトンネルを使うよう変更。CONNECT を拒むプロキシではこれらが失敗するようになった
- コンテナーにマウントした worktree かサブモジュールでの `-p` と SDK の実行が、フォルダーを信頼してから `.claude/settings.local.json` の allow ルールを適用するよう変更
- セルフホストのランナーが、セッションのフォルダーかリポジトリのパスがシンボリックリンクであるセッション（`checkout` フックのチェックアウトを除く）を拒むよう変更
- クラウドのセッションと Remote Control の下での使用上限と共有の予算のエラーから、「ask your admin to raise it」を削除（`errors` の「You've hit your monthly spend limit」に対応）
- [VSCode] インストールのリンクのマーケットプレイスの確認のボタンを「Trust marketplace and continue」に変更

**バグ修正**

- zstd で圧縮された応答の復号のセキュリティの問題を修正
- bare リポジトリの worktree・`--separate-git-dir` のチェックアウト・Android の `repo` のチェックアウトで、`/security-review` とスキルのインラインの git コマンドがエラーで止まる問題を修正
- モデルの設定が `opusplan` か `haiku` のとき、自分のモデルを持つサブエージェントが plan モードのモデルに移される問題を修正
- 別のモデルのサブエージェントが、ファイルの読み取りと MCP の結果の大きさをメインのセッションのモデルで決める問題を修正
- 多くのサードパーティのゲートウェイと Foundry のセッションが、コンパクトせずに毎ターンのコンテキスト長のエラーで止まる問題を修正
- Claude Code がきれいに終了しなかった後、再開したセッションから最近のターンが欠けることがある問題を修正
- 作業ディレクトリーが削除された後、シェルのコマンドが起動したディレクトリーで実行される問題を修正。コマンドはメッセージとともに失敗し、出し直せる
- `plansDirectory` のフォルダーが受け付けられないとき、承認した計画の編集が失われる問題を修正。計画は既定の計画のフォルダーに保存され、警告が場所と理由を述べる
- 保存した `sonnet[1m]` のモデルの設定が、新しいインストールで API が拒むモデル ID に書き換えられる問題を修正
- スケジュールしたタスクが後から返信したとき、フォーカスビューがプロンプトへの返信を隠す問題を修正
- フルスクリーンがオフのとき、バックグラウンドのサブエージェントのビューからプロンプトが欠けることがある問題を修正
- 一覧と許可のプロンプトの長い選択肢が折り返すと一部が上書きされる問題と、狭いターミナルで初回の画面が行を失う問題を修正
- 許可のルールについての起動時の警告と「N MCP servers need authentication」の通知が、表示の外にスクロールされていたのに既読として記録される問題を修正
- エージェントの名前か作業フォルダーが制御文字か改行を含むとき、ウェルカムのヘッダーが制御文字を表示するか行をまたいで分かれる問題を修正
- Claude がユーザーにしか実行できないコマンドを試したときの赤いエラーを修正。プロンプトで入力したときだけ実行される、という薄い行が出る
- `/stats` の Active days の合計が 1 日多い問題を修正
- 分析に該当するセッションがないのに `/insights` がレポートの準備ができたと言う問題と、HTML のレポートに 2 つの値をエスケープせずに書く問題を修正
- managed settings・`--settings`・プロジェクトの `.claude/settings.json` か `.claude/settings.local.json` が voice mode を元のままに保ったのに、`/voice` が変わったと言う問題を修正。何が保っているかを述べる
- Windows と Linux で、IDE のウェルカムのダイアログが Quick Launch に Cmd+Esc を表示する問題を修正
- 組織のポリシーがクラウドのセッションを拒むとき、Slack のアプリのヒントが出る問題を修正
- キーを読むターミナルがないとき `claude purge` が黙って止まる問題と、stdin がパイプのとき、そのプロジェクトのピッカーと `-i` のプロンプトがキーボードを無視する問題を修正
- `claude plugin eval --output-dir ''` がレポートを現在のフォルダーに書く問題を修正。エラーで終了する
- ターミナルでの `claude -p` のテキストの出力が、テキストの装飾以外の制御シーケンスを通す問題を修正。パイプとファイルへの出力は変わらない
- 残った `.oauth_refresh.lock.owner.tmp.*` のファイルが設定ディレクトリーにたまる問題を修正
- キーのない Console のサインインで、Claude Code がサーバーに尋ねていないのに `/fast` が「Fast mode has been disabled by your organization」と言う問題を修正
- ネットワークがないときのように Claude Code が確かめられなかったとき、`/model` が組織がモデルを制限していると言う問題を修正
- ブラウザーの手順の直後に Esc を押すと、`/login` の「Sign in with your Console account」が既存のログインを置き換える問題を修正
- サインインが失敗したか取り消されたのに、ブラウザーがサインインの成功のページを表示することがある問題を修正
- `claude auth status` などの短いコマンドが Console のプロファイルにロックを残し、次のセッションが約 1 分止まる問題を修正
- claude.ai のログインで始めたバックグラウンドのセッションが、バックグラウンドのサービスを始めたシェルの API キーかトークンを使う（そちらに課金される）問題を修正
- セッションがバックグラウンドで別のサインインに移るケースをさらに修正。これらの移動は拒まれ、何が使えるかをメッセージが述べる
- バックグラウンドへの移動が拒まれた後、終了のダイアログでの 2 回目の Enter がバックグラウンドの作業を止める問題を修正
- `allowedProviders` の managed setting が許していないのに、Amazon Bedrock でのトークンの計数が会話を Bedrock に送る問題を修正
- `HOME` の環境変数なしで Claude Code を始めたとき、AWS の `credential_process` の補助と Google Cloud の既定の資格情報が失敗する問題を修正
- サブエージェントの計画が承認された後、セッションが前の権限モードに戻ることがある問題を修正
- Agent SDK の `applyFlagSettings()` の呼び出しの無効な値 1 つが、前の呼び出しのすべての設定を黙って捨てる問題を修正。そうなる呼び出しはエラーで拒まれる
- 終わったプルリクエストが自分のレビューかマージだけを要するとき、セッションが入力待ちと示される問題を修正
- 認識されない `teammateMode` の設定値が警告なしに無視される問題を修正。`claude -p`・起動時の警告・`claude doctor` が飛ばした項目として挙げる（引き続き適用はされない）
- 新しいホームディレクトリーでの最初の実行で、`--worktree` が `CLAUDE_CODE_PLUGIN_SEED_DIR` のプラグインの `WorktreeCreate` フックを飛ばす問題を修正
- Dispatch のような brief モードのセッションが、ターンが既に返信した後にもう一度返信を送る問題を修正
- プラグインが別の URL で挙げていたとき、クラウドのセッションで、動いている Atlassian・Asana・Sentry のコネクターが失敗したと Claude が言う問題を修正
- フォルダーの移動か事前に温めた起動の後、Claude Desktop と SDK のセッションが、フォルダー自身の MCP サーバー（`.mcp.json`・local）をホストが加えたものとして挙げるか挙げず、WebSocket のものに接続しない問題を修正
- 接続中にプラグインの再読み込みがプラグインの MCP サーバーを外した後も、`/mcp` がそれを挙げ続ける問題を修正
- 一時的に拒まれただけのトークンの更新の後、MCP サーバーが「needs authentication」のままになり、その `mcp_tool` フックが飛ばされる問題を修正
- ツールの呼び出し中にサーバーの接続が置き換えられた後、headless モードで MCP の elicitation の要求が尋ねずに取り消される問題を修正
- ツールの呼び出しが MCP サーバーに再接続した後も、SDK のホストからの MCP のツールの呼び出しが「Not connected」と答える問題を修正
- 質問が Esc で閉じられたか再び尋ねられた後、MCP タスクが止まる問題を修正。フッターが入力が要ると述べ、`/tasks` での Enter が質問を再び表示する
- 同じサーバーへの別の呼び出しが接続を失った後、後の呼び出しが再接続しても、バックグラウンドの MCP タスクが更新を止めたままになる問題を修正
- バックグラウンドの MCP タスクの質問が、まだ入力中のメッセージの上に開く問題を修正。下書きを送るか消すまで待ち、スピナーとターンのタイマーは動き続ける
- 2.34 のような古い git で、`worktree.sparsePaths` と、スパースのプラグインとマーケットプレイスのクローンが、リポジトリのルートのファイルを外す問題を修正
- 複数のリポジトリを持つセルフホストのランナーのセッションが、セッションの途中で加えたリポジトリを使えない問題を修正
- 自分のアーティファクトかそのデータを読む前に、Claude が許可を求める問題を修正
- 一部のクラウドのセッションで、Artifact ツールの deny と ask の許可のルールとフックが適用されない問題を修正
- Code Mode のスクリプトが `EnterWorktree` で入った worktree を無視する問題、`~` のパスをプロジェクトに書く問題、サインインの期限が切れた後も `/mcp` が MCP サーバーを接続済みと示す問題を修正
- Code Mode で、許可のダイアログか計画の承認で Yes と一緒に入力した言葉が Claude に届かない問題を修正
- Code Mode のスクリプトの途中で終わったセッションを再開したとき、Claude が自分で作業を始める問題を修正。次のプロンプトを待つ
- ツールの呼び出しの実行中に送ったメッセージについて、OpenTelemetry の `user_prompt` のイベントが欠ける問題を修正。イベントは `delivery.mode: "mid_turn"` と実行中のターンの `prompt.id` を持つ
- VS Code でキューに入ったメッセージが 1 つのターンにまとまったとき、または 1 つのメッセージが画像を持っていたとき、OpenTelemetry の `user_prompt` のイベントが前のメッセージのテキストを外す問題を修正
- スラッシュコマンドの `allowed-tools` の許可が、そのターンの間か後に起こされたバックグラウンドのエージェントに当たる問題を修正
- `/feedback` と `/bug` が、サインインしたアカウントか組織が記録したほかのセッションだけをアップロードするよう修正
- 相対の deny と ask の許可のルール（`Read(./.env)` など）が、`cd` の後にプロジェクトをカバーしなくなる問題を修正。追加したディレクトリーにも当たる
- `mcp__plugin_*_` で始まる deny と ask の許可のルールが、大文字小文字の違う綴りのプラグインの MCP サーバーかツールを取りこぼす問題を修正
- セルフホストのランナーと `claude remote-control` のセッションで、Claude Code の再起動後に届いた許可の承認に deny ルールが適用されない問題を修正
- リポジトリの特定のサブフォルダーで Claude Code を始めたとき、コミットされた `.claude/settings.local.json` がユーザー自身のものとして扱われうるケースを修正
- 一部の deny と ask のルールが特定の Bash コマンドに適用されない問題を修正
- 一部の複合コマンドが尋ねずに実行できた、Bash の許可の確認の穴を修正。これらは許可を求める
- Bash の allow ルールが、名指すものと別のプログラムを実行しうるケースを修正
- クラウドのセッションで、プラグインの読み込み中に、コネクターのツールの承認のプロンプトが自動で答えられる問題を修正
- allow ルールが設定されているか以前にアップロードが承認されていたとき、一部のサブエージェントが、組織外の人が見られるアーティファクトを先に尋ねずに変えるかファイルをアップロードする問題を修正
- Artifact に「don't ask again」を選んでいたとき、一部のアーティファクトの公開が、組織外の人が見られるページの確認を飛ばす問題を修正
- auto モードが、組織外の人が見られるアーティファクトへの最初の変更だけを判断する問題を修正。その yes はその変更だけをカバーする
- 管理の `strictPluginOnlyCustomization` のエージェントとスキルへのロックが、既に実行中のセッションで効かない問題を修正
- 一部のケースで、サンドボックスの中のコマンドがネイティブのアップデーターのダウンロードのフォルダーに書き込めた問題を修正
- Bash のサンドボックスが worktree の設定とフックを完全には守らないケースを修正
- Bash のサンドボックスが、リンクした worktree の共有の git のフォルダーを完全には守らないケースを修正
- 一部の通常でない git の状態での `/teleport` の stash の選択を修正。止まって、何をするかを述べる
- Windows: アカウントが開けないフォルダーの下に PATH の項目があるとき、約 1 秒続きうる起動の停止を修正
- Windows で、別のドライブ文字の大文字小文字かスラッシュでフォルダーが記録されたセッションを、`/resume` が拒むか隠す問題を修正
- Windows で、セッションが別のドライブ文字の大文字小文字で記録されていたとき、セッションの中の `/resume` がプロジェクトの保存した信頼を落とす問題を修正
- Linux: 作業ディレクトリーが `denyRead` の中の `allowRead` のフォルダーの下にあるとき（シンボリックリンクのホームディレクトリーの下など）、サンドボックスの中の Bash コマンドが `bwrap: Can't create file` で失敗する問題を修正
- Claude Desktop のサードパーティのデプロイが、トークンの更新が終わるまで「Stopping」のままになる問題を修正（Claude Desktop がこの版を含むと効く）
- [VSCode] Claude Code が別のモデルで再起動した後か、Remote Control でモデルが切り替えられた後、モデルのピッカーのチェックマークが古いモデルに残る問題を修正
- [VSCode] 組織か `maxEffortLevel` の設定が定める effort の上限を超えるレベルを、effort のセレクターが提示する問題を修正
- [VSCode] 管理の `allowedProviders` の設定が拒むサインインを、サインインの画面が提示する問題を修正
- [VSCode] 安全の確認が質問を出したとき、MCP のツールの許可のプロンプトが、Claude Code が尋ねる理由を述べない問題を修正
- [VSCode] 読み込めなかった組織の設定のメッセージが、コマンドをもう一度実行するよう述べる問題を修正。タブの Retry のリンクに合わせて、もう一度試すよう述べる
- [Claude Code on the web] 新しいクラウドのセッションが、ツールの検索で読み込んだ MCP のツールの説明を 4,096 文字で切る問題を修正。上限はほかの Claude Code のセッションと同じ 16,384 文字になった
- [Claude Tag] 組織が管理しないワークスペースで投稿者の Claude のサインインの期限が切れていたとき、Slack に貼ったアーティファクトのリンクにカードが付かない問題を修正。簡素なカードが出る

**その他**

- **`agent-sdk/quickstart` の掲載位置が移った**。`llms-full.txt` の中で `agent-sdk/overview` の後ろから `agent-sdk/python` の後ろへ移りました（710 行の削除と追加はこの移動の分で、内容の変更は上の `tools` と `allowedTools` の 2 行だけです）。`llms.txt` の並びは変わっていません
- **Projects のスレッドのカードの記述が外れた**（`claude-projects` の「Send work and read results」ほか）。新しいスレッドは「タイトルと状態の箱のカード」ではなく会話に出る、と言い換えられ、「Review a thread's pull request」からは、カードの **Resolve conflicts**・**Fix CI**・**Address comments**・**Merge it**・**Review PR**・**Create PR** のボタンの一覧が外れました — [日本語](https://code.claude.com/docs/ja/claude-projects#send-work-and-read-results) / [English](https://code.claude.com/docs/en/claude-projects#send-work-and-read-results)
- **Desktop のスケジュールしたタスクの管理の 3 つの方法が箇条書きになった**（`desktop-scheduled-tasks` の「Manage scheduled tasks」）。Claude に頼む・タスク自身に更新させる・ディスクのプロンプトを編集する、の 3 つに分かれ、`CLAUDE_CONFIG_DIR` を設定したときのパスが `scheduled-tasks/<task-name>/SKILL.md` と明記されました — [日本語](https://code.claude.com/docs/ja/desktop-scheduled-tasks#manage-scheduled-tasks) / [English](https://code.claude.com/docs/en/desktop-scheduled-tasks#manage-scheduled-tasks)
- **npm のインストールのコマンドが `@latest` 付きになった**（`setup` の「Install with npm」・`troubleshoot-install` の 3 か所）。`npm install -g @anthropic-ai/claude-code` が `npm install -g @anthropic-ai/claude-code@latest` になりました。`troubleshoot-install` の「npm install errors in WSL」からは、WSL が Windows の `npm` を拾っている、という推定の言葉が外れています
- **サンドボックスの説明の言い換え**: `security` の「Built-in protections」の項目が短くなり（「Sandboxed bash tool」→「Sandboxed Bash tool」）、`sandbox-environments` の表と `glossary` の「Sandboxing」も auto-allow モードに合わせて言い換えられました（ハイライト 2 に関連）
- **例の値の差し替え**: `claude-code-on-the-web` の `--remote` の出力の例のセッション ID が `session_01HJKLMNOPQRSTUVWXYZ` の形になりました。`agent-view` の画面の画像の URL も替わっています
- **字句の小さな修正**: `agent-sdk/modifying-system-prompts`（比較の表の「Default tools」の行が「Tool guidance」に）、`agent-sdk/python`・`agent-sdk/typescript`（Bash のプロンプトは `localSettings` の提案を「含む」から「含むことがある」に）、`plugins/mods/gallery`（「Two more elements」→「`Image` and `Client`」）、`plugins/mods/create`（`hooks:` の行の言い方）、`hooks`（`UserPromptSubmit` で終了コード 2 で止めたときの stderr の扱いの言い方）、`settings-reference`（「How `env` values interact with your shell」の例外の一覧の言い方）、`network-config`・`checkpointing`（冒頭の文が短くなった）、`workflows`（許可リストの置き換えのリンク先が「When an allowlist blocks a subagent model」に）
- **書式の崩れ**: `setup` の「Install Claude Code」の 5 つのコードフェンスの開始行で、`theme={null}` が 1 回から 23 回に重なりました（`setup` の生の差分 33 行のうち 10 行。前回の取り込みでは `quickstart` の同じ 5 つのフェンスの重複が解消していました）。内容の変更ではなく、出力の書式の崩れと見られます

## 新着情報

（今回の差分に新着情報（`whats-new/`）のページはありません。head の `llms.txt`・`llms-full.txt`・見出しマップにも whats-new のページは載っていません）

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-11-12.md](./archives/latest/2026-11-12.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-11-12.md](./archives/latest-detail/2026-11-12.md)

<!--
base_commit: 77f196ce342a0c6130e111a1fa66ada14d87a243
head_commit: 1e8d14825866e74000053b24496de73f02e2e71f
generated_at_full: 2026-11-14T15:18:43+09:00
-->
