---
対象期間: 2026年07月14日 〜 2026年07月15日
作成日: 2026-07-15
---

# Claude Code 公式ドキュメント更新サマリ

```markdown
今回の対象期間は、changelog にリリース v2.1.211（多数の修正・改善を含む）が加わり、reference/ガイド系ページに MCP コネクタとゲートウェイまわりの新機能が集中して追記された回です。新規ページはありませんが、アーティファクトが公開後もライブデータを取得できるようになったこと、組織が claude.ai コネクタのツール単位に承認/ブロックを課せるようになったことなど、権限とデータの流れに関わる中核的な追加が目立ちます。

主要なものを以下に挙げます。

1. アーティファクトが、閲覧のたびに MCP コネクタを呼んでライブデータを表示できるようになった（各閲覧者自身の接続を使用）
2. 組織が claude.ai コネクタのツールを単位ごとに「承認要求（ask）」または「ブロック」に設定でき、Claude Code がローカルで全権限モードにわたって強制するようになった
3. ゲートウェイ経路の外へ出る非必須トラフィック（更新チェック・テレメトリ等）を一括で止める `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` が明文化された
4. 依存関係だけを持つプラグインマニフェストで、キュレーション済みのプラグイン集合を 1 回のインストールで配れるようになった
5. テレメトリの記述がメトリクスとエラーレポートに再編され、エラーレポートは Pro/Max・v2.1.198 以降・Claude API 直結の条件下でのみ有効と明記された
```

## ハイライト

1. [**アーティファクトが MCP コネクタでライブデータを取得**](./latest-detail.md#1-アーティファクトが-mcp-コネクタでライブデータを取得):  
  アーティファクト（claude.ai 上のプライベートページ）が、ビルド時のスナップショットではなく、閲覧されるたびに claude.ai の MCP コネクタを呼んで現在のデータを表示できるようになった。コネクタ呼び出しは各閲覧者自身のアカウント接続を通り、閲覧者ごとに見えるデータが変わる。Pro/Max/Team/Enterprise、v2.1.209 以降が必要。
2. [**コネクタツールに組織が承認要求とブロックを強制**](./latest-detail.md#2-コネクタツールに組織が承認要求とブロックを強制):  
  組織は claude.ai コネクタのツール単位に制御を設定でき、Claude Code は起動時に読み込んでローカルで強制する。`ask` のツールは `acceptEdits`・`auto`・`bypassPermissions` でも毎回プロンプトを出し「今後聞かない」を提供せず、allow ルールでもスキップされない（`dontAsk` では拒否）。`blocked` のツールは Claude に見える前に除外される。v2.1.129 以降が必要。
3. [**ゲートウェイ経路外の非必須トラフィックを止める設定**](./latest-detail.md#3-ゲートウェイ経路外の非必須トラフィックを止める設定):  
  ゲートウェイはモデルリクエストを運ぶが、Claude Code はバージョンチェック・テレメトリ・エラーレポート・リリースノートなどの非必須トラフィックを Anthropic や GitHub 等へ別途送る。egress をゲートウェイのみに絞ったネットワーク向けに、`CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1` でこれらを止められることが llm-gateway-connect に新設された。
4. [**チーム向けにプラグインをバンドル**](./latest-detail.md#4-チーム向けにプラグインをバンドル):  
  プラグインマニフェストは必須の `name` と `dependencies` 配列だけでも成立し、インストールすると全依存を引き込むため、キュレーション済みのプラグイン集合を 1 回のインストールで配布する手段になる。ロール別バンドルを内部マーケットプレイスで配り、`enabledPlugins`（managed 設定）で組織展開できる。
5. [**テレメトリ再編とエラーレポートの Pro と Max 限定化**](./latest-detail.md#5-テレメトリ再編とエラーレポートの-pro-と-max-限定化):  
  data-usage のテレメトリ記述が「メトリクス」と「エラーレポート」に分割され、それぞれ `DISABLE_TELEMETRY`／`DISABLE_ERROR_REPORTING` で個別無効化できることが整理された。エラーレポートは Pro/Max サインイン・v2.1.198 以降・Claude API 直結・ZDR/HIPAA 契約なし、の全条件を満たす場合にのみ有効と明記された。

## 新規追加されたページ

今回の対象期間では、新規に追加されたリファレンス・ガイドページはありません。

## 大幅に更新されたページ

- [**アーティファクト**](./latest-detail.md#1-アーティファクト) ([日本語](https://code.claude.com/docs/ja/artifacts) / [English](https://code.claude.com/docs/en/artifacts)):  
  MCP コネクタでのライブデータ取得（ハイライト 1 参照）が中心。あわせて「アーティファクトとは何でないか」「ページの制約」表がコネクタ呼び出しを唯一の外部データ経路として書き直され、管理者向けにアーティファクトコネクタ専用トグルが加わった。
- [**MCP**](./latest-detail.md#2-mcp) ([日本語](https://code.claude.com/docs/ja/mcp) / [English](https://code.claude.com/docs/en/mcp)):  
  コネクタツールへの組織制御（ハイライト 2 参照）に加え、MCP ツール出力が既定で 25,000 トークンに制限されるようになり（従来は 10,000 トークン超で警告のみ）、ツール検索の対応モデルが明確化された（Haiku 4.5 が `tool_reference` に対応、`CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS` はツール検索を強制的にオフにする）。
- [**LLM ゲートウェイ接続**](./latest-detail.md#3-llm-ゲートウェイ接続) ([日本語](https://code.claude.com/docs/ja/llm-gateway-connect) / [English](https://code.claude.com/docs/en/llm-gateway-connect)):  
  非必須トラフィックの停止（ハイライト 3 参照）に加え、デスクトップアプリが「サードパーティ推論設定」をアプリ内フォームからローカルに設定できるようになった（Developer メニューの Configure Third-Party Inference。管理者配布があればそちらが優先し読み取り専用になる）。
- [**データ使用**](./latest-detail.md#4-データ使用) ([日本語](https://code.claude.com/docs/ja/data-usage) / [English](https://code.claude.com/docs/en/data-usage)):  
  テレメトリ記述の再編とエラーレポートの Pro/Max・v2.1.198 以降限定化（ハイライト 5 参照）。
- [**機能の可用性**](./latest-detail.md#5-機能の可用性) ([日本語](https://code.claude.com/docs/ja/feature-availability) / [English](https://code.claude.com/docs/en/feature-availability)):  
  「すべてのプロバイダーで同一」という記述が「プロバイダー固有の差異あり」に緩められ、MCP サーバー・サブエージェント・コマンドの差異が明記された。`/design-sync`・`/radio` が 3P プロバイダーで不可、`/voice` が claude.ai 必須。Claude Platform on AWS では `/loop` の自己ペーシングが不可（明示的間隔のみ）に変わった。
- [**権限**](./latest-detail.md#6-権限) ([日本語](https://code.claude.com/docs/ja/permissions) / [English](https://code.claude.com/docs/en/permissions)):  
  コネクタツールの `ask` と MCP ツールの `requiresUserInteraction` が全権限モード・フック `allow`・`--dangerously-skip-permissions` を貫いてプロンプトを出す（`dontAsk` では拒否）ことが横断的に記述され、macOS のバックグラウンドセッションが保護フォルダへのアクセスを別途要求する挙動が追記された。

## 軽微な更新

今回の軽微な更新は、changelog に追加されたリリース **v2.1.211**（2026年07月15日）の内容と、上記大幅更新に含まれない各ページの小規模な改訂です。changelog 由来の項目は 1 リリースのみのため、原則としてバージョン併記は省きます。

**新機能**

- `--forward-subagent-text` フラグと `CLAUDE_CODE_FORWARD_SUBAGENT_TEXT` 環境変数が追加され、stream-json 出力にサブエージェントのテキストと thinking を含められるようになった。
- managed 設定 `disableBrowserExternalNavigation` が追加された。Browser ペインの外部ブラウジングを完全に止め、組織の allowlist 上のサイトも含めてブロックする（localhost 開発サーバーとファイルプレビューは動作。値は JSON ブール値 `true` のみ有効で文字列 `"true"` は無視）。ユーザーにも Claude にも外部サイトを見せたくない場合に、`browserExternalPageTools`（Claude のツールだけ止める）と使い分ける。 — [English](https://code.claude.com/docs/en/settings#available-settings)
- managed 設定 `pluginSuggestionMarketplaces` が追加され、どのマーケットプレイスのプラグインを文脈的インストール提案に出せるか allowlist できるようになった。 — [English](https://code.claude.com/docs/en/plugin-marketplaces#managed-marketplace-restrictions)
- GitHub の `owner/repo` 短縮ソースは既定で SSH でクローンされるが、`CLAUDE_CODE_PLUGIN_PREFER_HTTPS=1` で HTTPS クローンに切り替えられるようになった。 — [English](https://code.claude.com/docs/en/plugin-marketplaces#private-repositories)
- ログイン時のプロンプトで「3rd-party platform」を選ぶと、Bedrock と Vertex AI 向けの対話セットアップウィザードが起動するようになった（認証ページに追記）。あわせて managed 設定 `forceLoginMethod`/`forceLoginOrgUUID` が設定されている場合、`ANTHROPIC_API_KEY`・`ANTHROPIC_AUTH_TOKEN`・`apiKeyHelper` で認証したセッションは起動時にブロックされることが明記された（クラウドプロバイダーのセッションは非対象）。 — [English](https://code.claude.com/docs/en/authentication)

**機能改善**

- `UserPromptSubmit` フックで文脈を注入する `additionalContext` は `hookSpecificOutput` の内側にネストする必要があり、トップレベルに置くと黙って無視されることが、例つきで明記された。あわせて `"Edit|Write"` のようなマッチャーは v2.1.191 以降カンマ区切り `"Edit, Write"` でも同義になった。 — [English](https://code.claude.com/docs/en/hooks-guide)
- サンドボックスの読み取りルールが重なった場合、より限定的なパスが勝つことが表で示された（`denyRead: ["~/"]` + `allowRead: ["~/projects"]` は projects だけ読める、`allowRead: ["~/"]` + `denyRead: ["~/.env"]` は .env だけブロックのまま）。 — [English](https://code.claude.com/docs/en/sandboxing)
- シェルで `CLAUDE_CODE_USE_*` プロバイダー変数や非既定の `ANTHROPIC_BASE_URL` をエクスポートすると、server-managed 設定のフェッチがスキップされ、その `env` ブロックではエクスポートを打ち消せない（フェッチ前に適格性が判定されるため）ことが明記された。復旧はシェルからエクスポートを外すか、ユーザー設定 `env` で当該変数を `""` にする。 — [English](https://code.claude.com/docs/en/server-managed-settings)
- Web の Claude Code で、`GH_TOKEN`/`GITHUB_TOKEN` を自分で設定するとコンテナへそのまま渡り、未設定だと両変数がプレースホルダ `proxy-injected` になり GitHub プロキシが実認証情報を差し込む挙動が明記された（`GITHUB_TOKEN` を直接読むスクリプトはプレースホルダを受け取る）。 — [English](https://code.claude.com/docs/en/claude-code-on-the-web)
- `/setup-bedrock` はモデルピン工程を現在のピンから始め、`~/.claude/settings.json`（`CLAUDE_CONFIG_DIR` 設定時はそちら）へ書き込むことが明記された。SSO プロファイル手順のプレースホルダ表記も整理された。 — [English](https://code.claude.com/docs/en/amazon-bedrock)
- managed 設定に検証失敗エントリがある場合、`/doctor` でソースファイルとフィールド付きで除去されたエントリを一覧できるようになった。 — [English](https://code.claude.com/docs/en/settings#invalid-entries-in-managed-settings)
- Agent SDK のツール検索リファレンスに「Tool output exceeds maximum allowed tokens」のトラブルシューティング節が追加された。 — [English](https://code.claude.com/docs/en/agent-sdk/tool-search)
- Agent SDK のコスト追跡の説明で、最終的な output トークン表示はトップレベルのエージェントループ分で、サブエージェントのトークンは含まれないことが明記された。 — [English](https://code.claude.com/docs/en/agent-sdk/cost-tracking)
- managed-mcp の allowlist/denylist が `--mcp-config` CLI フラグで渡したサーバーにも適用される（`--strict-mcp-config` は読み込む設定ファイルを絞るだけで、どちらのリストもバイパスしない）ことが明記され、`allowedMcpServers`/`deniedMcpServers` 表にはエントリがスキーマ検証に失敗した場合の挙動（settings の Invalid entries）への参照が加わった。 — [English](https://code.claude.com/docs/en/managed-mcp)
- auto モード設定で、`environment`/`allow`/`soft_deny`/`hard_deny` を `"$defaults"` なしで上書きした場合に失われる組み込みルールの内訳が整理され、auto-mode bypass ルールが `soft_deny` 側に、データ持ち出しルールのみが `hard_deny` 側に明記された。 — [English](https://code.claude.com/docs/en/auto-mode-config)
- Claude in Chrome で、利用可能なブラウザツールの一覧は `/mcp` → `claude-in-chrome` → **View tools** で見ることが案内され、最初のブラウザ操作で `claude-in-chrome` スキルの使用許可を求める旨が追記された。 — [English](https://code.claude.com/docs/en/chrome)
- セッション/週次の使用枠は同時に消費されるため、大きなワークフローのファンアウトのような一時的な大量利用が、セッション枠のリセット前に週次枠を使い切りうることが追記された。 — [English](https://code.claude.com/docs/en/errors#usage-limits)
- プラグインマーケットプレイスの更新で、ブランチ/タグ `ref` で追加したマーケットプレイスはその ref の最新コミットに更新される（リポジトリの既定ブランチではない）ことが明記された。 — [English](https://code.claude.com/docs/en/plugin-marketplaces#plugin-marketplace-update)

**バグ修正**

- Bedrock/Vertex/Mantle/Foundry で、末尾のシステムコンテキストブロックを毎リクエスト新規 input トークンとして課金していた prompt-caching のリグレッションを修正。
- チャットチャネルへ中継される権限プレビューが、双方向オーバーライド・ゼロ幅・類似の引用文字を無害化しておらず、ツール入力が承認メッセージを視覚的に改変できた問題を修正。
- auto モードが、サンドボックス外 Bash に対する PreToolUse フックの `ask` 判定を上書きしていた問題を修正（フックの `ask` が最低でもプロンプトになる）。
- スリープ復帰後、多数のセッションが 1 つの認証情報ストアを共有していると並行セッションが一斉ログアウトする問題を修正。
- アイドルな Web セッション復帰後にプラグイン MCP サーバーが再接続せず、次のメッセージまで MCP 呼び出しが失敗し続ける問題を修正。
- Vertex/Bedrock で、モデルを明示設定していても起動時に既定 Opus を試して余計なフォールバック通知を出す問題を修正。
- 明示的なモデル上書きで起動したサブエージェントが、resume やフォローアップで親のモデルに戻る問題を修正。
- ネストした `.claude/rules/*.md` が、設定ソースがプロジェクト設定を除外していても読み込まれる問題を修正。
- `/clear` がセッションのコストカウンタをリセットせず、statusline のコストが `/clear` 後も 0 に戻らない問題を修正。
- `/loop` が一度使うとセッションを `/resume` から隠す問題、スケジュールのないルーチンが次回実行を西暦 1 年と報告する問題、Windows のヘッドレス print モードで stdin が読めないとクラッシュ/無音終了する問題を修正。
- ユーザーが kill したバックグラウンドエージェントが自動再生成され、復活したエージェントが古いセッションの stale なプロンプトを再実行する問題を修正。あわせて、まだ実行中のエージェントの状態を Claude が正しく報告し、結果を捏造せず実完了を待つよう改善。
- このほか v2.1.211 では、Chrome 拡張が有効でも Chrome 未起動時の起動ハング、非同期コンテンツ表示の 300ms 遅延、直前に停止したバックグラウンドセッションを再度開くと同一 ID で空会話になる問題、`/terminal-setup` 後にスクリーンリーダー利用者が端末ベルを失う問題、Windows での Claude in Chrome セットアップページがブラウザで開かない問題など、多数の修正が入っている。

**その他**

- 「always allow」権限ルールがリポジトリルートに保存されるよう変更され、git worktree で与えた承認がセッションと worktree をまたいで持続するようになった。
- `/usage-credits` が組織管理者へリクエストを送る前に確認を求めるよう変更された。
- Vim モードの `s`・`S`（文字/行の置換）が vim 同様 NORMAL モードで効くよう変更された。
- 整数の環境変数（タイムアウト・トークン予算・リトライ回数）が `1e6` や `64_000` のような指数表記・桁区切り表記を受け付けるようになった。
- Compliance API と context management のドキュメントリンク先 URL が現行のものに更新された（表示内容の実質変化なし）。
- 多数のページのドキュメントリンクが現行のドキュメントサイトに更新された。

## 新着情報

今回の対象期間では、週刊ダイジェスト「新着情報」（`whats-new/`）の**変更はありません**（新規追加・更新ともになし）。

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-07-14.md](./archives/latest/2026-07-14.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-07-14.md](./archives/latest-detail/2026-07-14.md)

<!--
base_commit: 991b037c23024d28c04a58fcaebe2c1862fc912d
head_commit: fa4c4c546b211cf29cac5e7c4dcc5b3e95008594
generated_at_full: 2026-07-16T15:00:33+09:00
-->
