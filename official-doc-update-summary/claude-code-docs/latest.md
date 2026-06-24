---
対象期間: 2026年06月22日 〜 2026年06月23日
作成日: 2026-06-23
---

# Claude Code 公式ドキュメント更新サマリ

```markdown
今回の対象期間は Claude Code v2.1.187（2026年06月23日）のリリースを中心に、エージェントビュー（バックグラウンドセッション）と Slack 連携のドキュメント更新がありました。新規ページの追加はありません。

主要なものを以下に挙げます。

1. Team / Enterprise ワークスペース向けに、Slack 版 Claude Code が組織管理の共有 ID で動く Claude Tag へ置き換えられる旨が案内された
2. エージェントビューの入力欄で `/model <モデル名>` を打つと、以降ディスパッチするセッションのモデルを切り替えられるようになった（v2.1.172）
3. バックグラウンドセッションがプロバイダー設定・認証情報をどこから読むかが整理され、`ANTHROPIC_BASE_URL` 等のゲートウェイ変数はシェルから継承しなくなった（v2.1.174）
4. バックグラウンドディスパッチが `Could not resolve authentication method` で失敗する場合のトラブルシューティング節が追加された（v2.1.174）
```

## ハイライト

1. [**Claude Tag による Slack 版 Claude Code の置き換え**](./latest-detail.md#1-claude-tag-による-slack-版-claude-code-の置き換え):  
  Team / Enterprise ワークスペース向けに、Slack 版 Claude Code が Claude Tag へ置き換えられる旨が案内された。Claude Tag は管理者が設定したアクセス権を持つ組織共有の @Claude で、既存の Claude for Slack アプリと同じアプリ上で動くため再インストール不要で、既存セットアップも移行期間中は機能し続ける。
2. [**エージェントビューでのディスパッチモデル切り替え**](./latest-detail.md#2-エージェントビューでのディスパッチモデル切り替え):  
  エージェントビューのディスパッチ入力に `/model <モデル名>` を入力すると、以降ディスパッチするセッションのモデルを切り替えられるようになった。`/model default` で解除でき、設定ファイルには書き込まれず現在の `claude agents` 実行中のみ有効（v2.1.172）。
3. [**バックグラウンドセッションのプロバイダー設定とゲートウェイ変数**](./latest-detail.md#3-バックグラウンドセッションのプロバイダー設定とゲートウェイ変数):  
  バックグラウンドセッションがプロジェクト設定の `env` 値・プロバイダー選択変数・認証情報をどこから読むかが明文化された。`ANTHROPIC_BASE_URL` 等のゲートウェイ変数はシェルから継承されなくなり、プロジェクトの `.claude/settings.json` の `env` で指定する形になった（v2.1.174）。
4. [**認証エラー Could not resolve authentication method のトラブルシューティング**](./latest-detail.md#4-認証エラー-could-not-resolve-authentication-method-のトラブルシューティング):  
  バックグラウンドディスパッチがこのエラーで失敗する場合の対処法が追加された。スーパーバイザーが事前ウォームしたワーカーを割り当てる仕組みの説明とあわせ、`claude daemon stop --any --keep-workers` で復旧する手順が示された（v2.1.174）。

## 新規追加されたページ

（今回の対象期間に新規追加されたリファレンスページはありません）

## 大幅に更新されたページ

（今回の対象期間に、単一ページで 50 行以上の大幅更新に該当したページはありません。主要な更新はハイライト、その他はいずれも下記「軽微な更新」に整理しています）

## 軽微な更新

今回の軽微な更新は、Claude Code v2.1.187（2026年06月23日）の changelog 追加と、Slack・エージェントビュー等のドキュメント加筆が中心です。以下に分類して整理します（バージョンは単一リリースのため、各 bullet への併記は省略します）。

**新機能**

- `sandbox.credentials` 設定が追加された。サンドボックスで実行されるコマンドが認証情報ファイルやシークレットの環境変数を読み取るのをブロックする。
- 組織が設定したモデル制限が、モデルピッカー・`--model`・`/model`・`ANTHROPIC_MODEL` に反映されるようになった。制限対象のモデルを選ぶと「組織の設定により制限されています」というメッセージが表示される。
- フルスクリーンモードの選択メニュー（権限プロンプト・`/model`・`/config` など）で、マウスクリックによる選択がサポートされた。
- Slack 連携のトラブルシューティングに「Claude Code がアカウントで有効になっていません」の節が追加された。管理者の有効化操作は不要で、claude.ai/code に一度サインインすればクラウド環境が作成されエラーが解消する旨を案内する — [日本語](https://code.claude.com/docs/ja/slack#claude-code-is-not-enabled-for-your-account) / [English](https://code.claude.com/docs/en/slack#claude-code-is-not-enabled-for-your-account)
- エージェントビューの入力欄で `/model` がディスパッチモデルの切り替えコマンドとして扱われるようになった（詳細はハイライト 2 参照） — [日本語](https://code.claude.com/docs/ja/agent-view#set-the-model) / [English](https://code.claude.com/docs/en/agent-view#set-the-model)

**機能改善**

- バックグラウンドセッションのプロバイダー設定・ゲートウェイ変数の解決方法が整理された（詳細はハイライト 3 参照） — [日本語](https://code.claude.com/docs/ja/agent-view#the-supervisor-process) / [English](https://code.claude.com/docs/en/agent-view#the-supervisor-process)
- スーパーバイザーが事前ウォームしたワーカーを 1 つ保持して起動遅延を抑えるようになり、認証エラーのトラブルシューティングも追加された（詳細はハイライト 4 参照）
- Slack 連携で、各セッションが自分の Claude アカウントで実行され、接続済みリポジトリと自分のプラン上限を使う点が本文に明記された — [日本語](https://code.claude.com/docs/ja/slack) / [English](https://code.claude.com/docs/en/slack)
- `/install-github-app` が改善され、GitHub Actions ワークフローのセットアップが任意になった。GitHub App のインストールだけ行い、ワークフロー／シークレットの手順をスキップできる。
- `/btw` で ←/→ の矢印キーによるナビゲーションが追加され、過去の回答をたどれるようになった。
- `/plugin` が、最近使っていないプラグインを表に出して整理を促すようになった。

**バグ修正**

v2.1.187 で多数のバグ修正が行われました。主なものは以下のとおりです（いずれも changelog のみの言及で、対応する通常ドキュメントページはないためリンクは付しません）。

- `--resume` が、元の `-p` 実行がモデルのターンを生成しなかった場合に「No conversation found」で失敗する問題を修正
- `--json-schema` と Workflow の `agent({schema})` の構造化出力で、成功後もモデルが `StructuredOutput` を無限に再呼び出しできてしまう問題を修正し、後続ターンが確実に構造化出力を返すようにした
- リモート MCP ツール呼び出しが応答なしで 5 分間ハングする問題を修正し、無期限にブロックせずエラーで中断するようにした（`CLAUDE_CODE_MCP_TOOL_IDLE_TIMEOUT` で調整可）
- エージェントプロキシの CA システム信頼インストール追加後、Claude Code Remote セッションの起動が約 2.7 秒遅くなる問題を修正
- per-byte の拡張キーイベントとして貼り付けを受け取るターミナルで、貼り付けた韓国語／CJK テキストが文字化けする問題を修正
- リモートコントロール経由の `/update` が、起動時の信頼ダイアログが表示されるべき場面でハングする問題を修正
- エージェントがターンを構造化出力なしで終えたとき、エージェントビューのバックグラウンドジョブが「working」のまま止まる問題を修正
- エージェントビューへ移動して戻った後、および `/bg`・`/tui`・`/update` の後にチャンネル接続が切れる問題を修正
- エージェント停止通知が誰が停止したかを正しく示さない問題を修正し、文言も改善した（"came to rest" の代わりに "finished"／"stopped"）
- サブエージェントの深さ追跡を修正（再開したサブエージェントは元の生成深さを復元し、フォークしたサブエージェントは深さ上限にカウントされる）
- 強制終了したエージェントの worktree 登録のリークを修正（ロックされた `.git/worktrees/` エントリを自動でクリーンアップ）
- macOS の Ghostty でフルスクリーンモード時に Cmd+クリックで URL が開かない問題を修正
- `claude --help` が `--bg`／`--background` フラグを一覧表示しない問題を修正
- `/share` のアップロード中に Esc・Ctrl-C・Ctrl-D が効かない問題を修正
- [VSCode] 大きなセッションの再開時に拡張機能が応答しなくなる問題を修正

**その他**

- changelog ページに v2.1.187（2026年06月23日）のリリースエントリが追加された（changelog リンク不使用ポリシーによりリンクは付しません）。
- 「ウェブ上の Claude Code」ページの関連リソースに、同じクラウド環境で動く Claude Tag への外部リンクが追加された — [日本語](https://code.claude.com/docs/ja/claude-code-on-the-web) / [English](https://code.claude.com/docs/en/claude-code-on-the-web)
- 「スキル」ページの関連リソースに、リポジトリにコミットしたプロジェクトスキルが Claude Tag チャンネルでも読み込まれる旨の Claude Tag skills への外部リンクが追加された — [日本語](https://code.claude.com/docs/ja/skills) / [English](https://code.claude.com/docs/en/skills)

## 新着情報

（今回の対象期間に新着情報ページの更新はありません）

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-06-22.md](./archives/latest/2026-06-22.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-06-22.md](./archives/latest-detail/2026-06-22.md)

<!--
base_commit: db1b606290c053b1530a48339df97fa7fdaba745
head_commit: a8b1232abacba9353171c44560e7a6a4bfd70a63
generated_at_full: 2026-06-24T15:00:50+09:00
-->
