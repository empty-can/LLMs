---
対象期間: 2026年07月06日 〜 2026年07月07日
作成日: 2026-07-07
---

# Claude Code 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
今回の対象期間は、公式ドキュメントのバージョンアップ（changelog エントリ）を伴わない、記述面の明確化・訂正が中心の回です。特に Agent SDK とフック／MCP まわりで、プラグイン同梱 MCP サーバの命名規則・権限モードの利用可否・ツールのエラーハンドリングに関する記述が整理されました。

主要なものを以下に挙げます。

1. プラグインが同梱する MCP サーバのツール名・サーバ名がスコープ付きになることが、フック（マッチャ・`mcp_tool` の `server` フィールド）と MCP のドキュメントで明文化された（`mcp__plugin_<plugin>_<server>__<tool>` / `plugin:<plugin>:<server>`。裸のサーバ名で書いたマッチャは発火しない）
2. Agent SDK の `auto` 権限モードから「TypeScript only」の但し書きが外れ、Python SDK でも利用可能としてドキュメント上に記載された（各表の可用性注記は従来どおり）
3. Agent SDK のカスタムツールで、ハンドラの未捕捉例外がエージェントループを止めるという記述が訂正され、実際には in-process MCP サーバが例外をエラー結果へ変換してループは継続する旨に書き換えられた
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**プラグイン同梱 MCP サーバのスコープ付き命名**](#1-プラグイン同梱-mcp-サーバのスコープ付き命名):  
  プラグインがバンドルする MCP サーバは、ツール名が `mcp__plugin_<plugin-name>_<server-name>__<tool>`、サーバ名が `plugin:<plugin-name>:<server-name>` というスコープ付きになる。フックのマッチャ・`if` フィールド・`mcp_tool` フックの `server` フィールド、および `docs/en/mcp` の各所でこれが明記され、裸のサーバキー（例: `mcp__database-tools__.*`）で書いたマッチャはプラグイン同梱サーバには発火しないと注意喚起された。
2. [**Agent SDK の auto 権限モードが Python でも利用可能に**](#2-agent-sdk-の-auto-権限モードが-python-でも利用可能に):  
  Agent SDK の権限モード表から `auto` に付いていた「(TypeScript only)」の但し書きが、agent-loop・permissions・quickstart の各権限モード表で一斉に削除され、Python SDK リファレンスの `PermissionMode` Literal にも `"auto"` が追加された。ドキュメント上は Python SDK でも `auto` が選べる扱いになった（各エントリに残る「See Auto mode for availability」の可用性注記は従来どおり）。
3. [**Agent SDK のツールエラーハンドリング記述の訂正**](#3-agent-sdk-のツールエラーハンドリング記述の訂正):  
  カスタムツールの「Handle errors」節が、ハンドラの未捕捉例外はエージェントループを止め `query` が失敗するという旧記述から、SDK の in-process MCP サーバが未捕捉例外を捕捉してエラー結果に変換するため**どちらの報告方法でもループは継続する**という記述へ訂正された。`isError: true` を返す意味は「ループを継続させること」ではなく「Claude が読むメッセージを自分で組み立てること」に整理された。
<!-- light:highlight-list:end -->

## 1. プラグイン同梱 MCP サーバのスコープ付き命名

フック（`docs/en/hooks`）と MCP（`docs/en/mcp`）の各ページで、プラグインがバンドルする MCP サーバのツール名・サーバ名がスコープ付きになることが明文化されました。プラグイン `my-plugin` が `db`（旧例では `database-tools`）というキーでサーバを同梱する場合、そのツールは `mcp__plugin_my-plugin_db__query` のように **`mcp__plugin_<plugin-name>_<server-name>__<tool>`** という命名になります。したがって、そのサーバの全ツールにマッチさせるフックマッチャは `mcp__plugin_my-plugin_db__.*` と書く必要があり、裸のサーバキー（`mcp__database-tools__.*`）で書いたマッチャは**プラグイン同梱サーバには一切発火しません**。この注意は「Match MCP tools」タブ・「Match MCP tools」リファレンス節の両方に加筆され、同じスコープ付きツール名をハンドラの `if` フィールドにも使う旨が示されました。

サーバ自体は **`plugin:<plugin-name>:<server-name>`**（例: `plugin:my-plugin:db`）というスコープ名で登録されるため、設定済みサーバ名が期待される箇所——具体的には `mcp_tool` フックの `server` フィールド——ではこのスコープ名を使います。`mcp_tool` フックフィールド表の `server` 行にも、プラグイン同梱サーバでは裸のサーバキーではなくスコープ名を渡す旨が追記されました。あわせて MCP ページの「Plugin-provided MCP servers」節では、フルなツール名を permission ルール・skill の `allowed-tools`・サブエージェントの `tools` フィールドに加えて**フックマッチャ**でも使えること、およびプラグイン側フックのドキュメント（plugins リファレンス）にも、プラグイン自身の同梱 MCP サーバを狙うフックはスコープ名を使わねばならない旨のクロスリンクが追加されました。

- [Connect Claude Code to tools via MCP (Plugin-provided MCP servers) - Claude Code Docs (English)](https://code.claude.com/docs/en/mcp#plugin-provided-mcp-servers)
- [Hooks reference (Match MCP tools) - Claude Code Docs (English)](https://code.claude.com/docs/en/hooks#match-mcp-tools)

> 本節の加筆は en 側のみで、日本語版 hooks / mcp ページが本サマリ作成時点で当該記述（プラグイン同梱サーバのスコープ付き命名）を反映しているか確認できないため、安全側で日本語リンクを省略しています。

## 2. Agent SDK の auto 権限モードが Python でも利用可能に

Agent SDK 各ページの権限モード表で、`auto` モードに付与されていた「**(TypeScript only)**」の但し書きが一斉に削除されました。対象は How the agent loop works（`agent-sdk/agent-loop`）・Configure permissions（`agent-sdk/permissions`）・Quickstart（`agent-sdk/quickstart`）の各権限モード表で、いずれも `auto`（モデル分類器が各ツール呼び出しを承認/拒否する）から言語限定の注記が外れています。あわせて Python SDK リファレンス（`agent-sdk/python`）の `PermissionMode` Literal にも `"auto"`（モデル分類器が各ツール呼び出しを承認/拒否する）が追加されました。

これにより、`auto` モードはドキュメント上 TypeScript 専用ではなく **Python SDK でも選択可能**な扱いになりました。ただし各表に残る「See [Auto mode](/docs/en/permission-modes#eliminate-prompts-with-auto-mode) for availability and behavior」という可用性注記はそのまま維持されており、実際に利用できるかは Auto mode 節の可用性条件に従います。無条件で有効化されるわけではない点は従来どおりです。

- [Configure permissions (Permission modes) - Claude Code Docs (English)](https://code.claude.com/docs/en/agent-sdk/permissions#permission-modes)

> 本変更は en 側のみで、日本語版 agent-sdk ページが本サマリ作成時点で `auto` の Python 対応記述を反映しているか確認できないため、安全側で日本語リンクを省略しています。

## 3. Agent SDK のツールエラーハンドリング記述の訂正

カスタムツール（`agent-sdk/custom-tools`）の「**Handle errors**」節が大きく書き換えられ、これまでの記述の誤りが訂正されました。旧記述は「ハンドラが未捕捉例外を投げるとエージェントループが停止し、Claude はエラーを見ることなく `query` 呼び出しが失敗する」としていましたが、実際には SDK の in-process MCP サーバが未捕捉例外を捕捉してエラー結果に変換するため、**例外を投げても `isError: true` を返しても、いずれの場合もエージェントループは継続します**。両者の違いは「ループが止まるかどうか」ではなく「**Claude が読むメッセージが何になるか**」です。

新しい表では、未捕捉例外を投げた場合は MCP サーバが生の例外メッセージを載せたエラー結果に変換して Claude に渡す（ループは継続）、`isError: true`（Python では `"is_error": True`）で返した場合は自分が組み立てたメッセージを Claude が読む（どのリクエストが失敗したか・次に何を試すか等、生の例外に無い文脈を足せる）、と整理されました。したがってエラーを自前で捕捉すべきなのは「ループを生かすため」ではなく「生の例外メッセージだけでは Claude が対処できないとき」だと明記されています。ページ冒頭の早見表の該当行も「Handle errors without stopping the loop」から「**Control the error message Claude reads**」に、コード例中のコメントも「捕捉がループを生かす」から「Claude が読むメッセージを組み立てる」に更新されました。

- [Give Claude custom tools (Handle errors) - Claude Code Docs (English)](https://code.claude.com/docs/en/agent-sdk/custom-tools#handle-errors)

> 本節の訂正は en 側のみで、日本語版 custom-tools ページが本サマリ作成時点で当該訂正を反映しているか確認できないため、安全側で日本語リンクを省略しています。

## 新規追加されたページ

<!-- light:new-pages:start -->
今回、リファレンス系で新規追加されたページ（新規ページファイル）はありません。`llms.txt`・ドキュメントマップにエントリの増減はなく、変更はいずれも既存ページ本文の改稿です。
<!-- light:new-pages:end -->

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
今回、上記ハイライト（hooks / mcp / plugins / agent-sdk の各ページ）以外に、本文の実体的な追加・改稿を独立して伴う大幅更新はありません。その他の変更はいずれもドキュメント記述の明確化・訂正の範囲です（軽微な更新に記載）。
<!-- light:updated-pages:end -->

## 軽微な更新

<!-- light:minor-updates:start -->
今回の軽微な更新は、公式ドキュメントのバージョンアップを伴わない記述面の明確化・訂正です（changelog エントリの追加はありません）。いずれも既存の挙動をより正確に説明し直したもので、機能追加やバグ修正ではありません。

**機能改善**

- `claude mcp add` の設定 Tips に、`--scope` に短縮形 `-s`、`--env` に短縮形 `-e` があること、および `--transport`・`--header` にもそれぞれ `-t`・`-H` の短縮形があることが明記された（例: `-e KEY=value`）。 — [English](https://code.claude.com/docs/en/mcp#installing-mcp-servers)
- Agent SDK のカスタムツールで、ツール結果の `content` 配列が扱うブロック種別の説明が言語別に精緻化された。audio ブロックは TypeScript ではディスクに保存されパスがテキストブロックとして Claude に渡るが、**Python SDK ではツール結果から破棄され警告がログ出力される**旨、および `resource.blob`（base64 のバイナリ）も **TypeScript 専用で Python SDK では破棄・警告**される旨が追記された。 — [English](https://code.claude.com/docs/en/agent-sdk/custom-tools#return-images-and-resources)
- Agent SDK（Python）で、フックに渡る `agent_id` / `agent_type` の対象が拡張された。従来 `PreToolUse` / `PostToolUse` / `PostToolUseFailure` のみだったのが、`PermissionRequest` では任意フィールドとして、`SubagentStart` / `SubagentStop` では必須フィールドとして利用可能になり、`PermissionRequestHookInput` の定義にも `agent_id` / `agent_type`（いずれもサブエージェント内でフックが発火したときに存在）が追加された。
- Agent SDK（Python）の `can_use_tool` に関する注記が精緻化された。`can_use_tool` はストリーミングモードを要するが、`query(prompt=generator)` や `ClaudeSDKClient.connect(prompt=async_iterable)` に有限のメッセージストリームを渡すと、フックや in-process MCP サーバが開いたままにしていない限り最後のメッセージ後に入力ストリームが閉じ、権限コールバックが呼ばれない。prompt なしで接続し `ClaudeSDKClient.query()` でメッセージを送る場合はストリームが自動で開いたままになりフック不要、という具体的条件が追記された。
- hooks リファレンスの共通入力フィールド表で、`transcript_path` の説明に、トランスクリプトファイルは非同期に書かれるためフック発火時点で当該ターンの最新メッセージをまだ含まない場合がある旨と、現ターンの最終アシスタントテキストが必要なフックは `transcript_path` を読むのではなく Stop / SubagentStop の `last_assistant_message` を使うべき旨が追記された。 — [English](https://code.claude.com/docs/en/hooks#common-input-fields)
- hooks リファレンスの Stop 節で、`last_assistant_message` の使いどころが補足された。読み上げ・通知など直近完了ターンに作用するフックは、バージョンによって Stop 時点でトランスクリプトが最終メッセージを含む保証がないため、`transcript_path` を読むのではなく本フィールドを使うべき旨が明記された。 — [English](https://code.claude.com/docs/en/hooks#stop)

**その他**

- 原文全文（llms-full）の setup ページ抽出で、Native Install／Homebrew／WinGet の `bash`／`powershell`／`batch` コードフェンス属性に付く `theme={null}` の重複が、5回連続から1回へと整理された（スクレイプ由来のノイズの変動であり、ドキュメント内容の変更ではない）。前回（2026年07月06日サマリ）に「1→5へ増加」と記録した箇所が、今回は逆に減少した形。
<!-- light:minor-updates:end -->

## 新着情報

<!-- light:whats-new:start -->
今回、週刊ダイジェスト「新着情報」（`whats-new/`）ページの新規追加・本文変更はありません（差分内に `whats-new/` を含む変更は 0 件。`llms.txt`・ドキュメントマップにも `whats-new/` の新規エントリはありません）。
<!-- light:whats-new:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-07-06.md](./archives/latest/2026-07-06.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-07-06.md](./archives/latest-detail/2026-07-06.md)

<!--
base_commit: eacae3b50bdabd388ec09e26647eca3a8ae25345
head_commit: 88368cb696a40602cde0d146a1705284bcfe43d2
generated_at_full: 2026-07-08T15:01:34+09:00
-->
