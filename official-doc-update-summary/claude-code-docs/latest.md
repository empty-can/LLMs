---
対象期間: 2026年07月04日 〜 2026年07月06日
作成日: 2026-07-06
---

# Claude Code 公式ドキュメント更新サマリ

```markdown
今回の対象期間は v2.1.202（2026年07月06日）リリースを起点に、新機能の追加・エラーリファレンスの新設・GHES 関連ドキュメントの大幅改稿・テレメトリ属性の追加が入った、実体的な更新の多い回です。前回までのプロバイダ名正規化のような字句変更中心の回とは性質が異なります。

主要なものを以下に挙げます。

1. 動的ワークフローが生成するエージェント数の目安を `/config` の「Dynamic workflow size」（設定キー `workflowSizeGuideline`）で設定できるようになった（強制上限ではなく助言。small/medium/large/unrestricted）
2. ダウンロード切断で install/update が失敗する事象に対する新しいエラーリファレンス節が追加され、切断・停滞・チェックサム失敗時は最大3回まで自動リトライするようになった
3. GHES 上のプラグインマーケットプレイスのドキュメントが大幅改稿され、サーフェス別の認証要件表・`extraKnownMarketplaces` によるプリレジスト節・claude.ai 追加失敗のトラブルシュート節が新設された
4. ワークフローが spawn したエージェントのテレメトリに `workflow.run_id` / `workflow.name` 属性が追加され、1つのワークフロー実行を OpenTelemetry データから再構成できるようになった
```

## ハイライト

1. [**動的ワークフローのサイズガイドライン設定**](./latest-detail.md#1-動的ワークフローのサイズガイドライン設定):  
  `/config` の「Dynamic workflow size」（設定キー `workflowSizeGuideline`）で、Claude が生成する動的ワークフローのエージェント数の目安を制御できるようになった。unrestricted（既定）/ small / medium / large の4値で、強制上限ではなく Claude への助言として送られる。
2. [**ダウンロード切断エラーの新規リファレンスと自動リトライ**](./latest-detail.md#2-ダウンロード切断エラーの新規リファレンスと自動リトライ):  
  エラーリファレンスに「The connection dropped while downloading the update」節が新設され、install/update のバイナリ取得中に接続が切れた場合の挙動が明文化された。切断・停滞・チェックサム失敗は合計最大3回まで自動リトライする（v2.1.202 以前は1回の切断で即失敗）。
3. [**GHES プラグインマーケットプレイスの登録方式と認証要件の刷新**](./latest-detail.md#3-ghes-プラグインマーケットプレイスの登録方式と認証要件の刷新):  
  github-enterprise-server ページの「Plugin marketplaces on GHES」が大幅改稿。追加サーフェス別の認証要件表、`extraKnownMarketplaces` によるプリレジスト節（旧 Allowlist 節から分離・改称）、HTTPS URL 推奨化、claude.ai 追加失敗のトラブルシュート節が加わった。
4. [**ワークフロー由来エージェントの OpenTelemetry 属性追加**](./latest-detail.md#4-ワークフロー由来エージェントの-opentelemetry-属性追加):  
  ワークフローが spawn したエージェントのテレメトリに `workflow.run_id`（`wf_` 前置の実行識別子）と `workflow.name` が追加された。1つの `workflow.run_id` で絞り込めば、そのワークフロー実行の API リクエストとツール結果を再構成できる。

## 新規追加されたページ

今回、リファレンス系で新規追加されたページ（新規ページファイル）はありません。上記ハイライトはいずれも既存ページへの節追加・改稿です。

## 大幅に更新されたページ

今回、上記ハイライト（workflows / errors / github-enterprise-server / monitoring の各ページ）以外に、本文の実体的な追加・改稿を独立して伴う大幅更新はありません。その他の変更はいずれも v2.1.202 リリースに付随する軽微な加筆・修正です（軽微な更新に記載）。

## 軽微な更新

今回の軽微な更新は、v2.1.202（2026年07月06日）リリースに付随する多数の機能追加・改善・バグ修正と、その反映によるドキュメント各ページの加筆が中心です。特記なきバージョンは v2.1.202 です。

**新機能**

- 自動ペース（self-paced）の `/loop` を、`ScheduleWakeup` ツールを `stop: true` で呼ぶことで明示的に終了できるようになった。リスケジュールも stop もしないままイテレーションが終わると、Claude Code は約20分後に fallback wakeup を1回だけスケジュールし、そのイテレーションでもリスケジュールされなければループを終了する（v2.1.202 以前は「リスケジュールしない」ことだけが自走終了の手段だった）。tools-reference の `ScheduleWakeup` の説明にも `stop` フィールドの追加が反映された。
- Agent SDK の `getSessionMessages` が返す `SessionMessage` 型に、`parent_agent_id`（ネストされたサブエージェントを spawn した親サブエージェントの `agentId`。メインセッション・トップレベルのサブエージェント・旧セッションでは `null`）が追加された。

**機能改善**

- background セッションで `/rename` または `Ctrl+R` で設定したセッション名が、スーパーバイザのプロセス停止・再起動をまたいで保持されるようになり、`claude --resume <name>` が引き続き解決するようになった（v2.1.202 以前は dispatch 時の名前に戻り、新しい名前で解決できなくなっていた）。 — [English](https://code.claude.com/docs/en/agent-view#permission-mode-model-and-effort)
- Remote Control セッションが自身の権限モードを claude.ai・モバイルアプリへ報告するようになり、ドロップダウンがターミナル側を含むモード変更に追従するようになった。唯一の例外は bypassPermissions で、このモードは claude.ai へ報告されない。v2.1.202 以前は `/remote-control`・`claude --remote-control` で接続したセッションがモードを全く報告せず、表示が実モードと食い違うことがあった（不一致はラベルのみで、権限プロンプトは実モードから生成され従来通り表示された。`/remote-control` セッションが誤った権限モードを表示する不具合の修正も同根）。 — [日本語](https://code.claude.com/docs/ja/permission-modes#switch-permission-modes) / [English](https://code.claude.com/docs/en/permission-modes#switch-permission-modes)
- MCP 設定で `url` があり `type` が無いエントリを設定エラーとして扱い、誤解を招く `command: expected string` ではなく `type: http`（または `sse`/`ws`）の追加を促す明確なメッセージ（`MCP server "<name>" has a "url" but no "type"; ...`）を表示するようになった。 — [English](https://code.claude.com/docs/en/mcp#option-1-add-a-remote-http-server)
- 「Yes, don't ask again」でファイルパスを許可する際、`[` `]` `*` などの gitignore パターン文字をエスケープし、生成ルールが許可したリテラルパスにのみ一致するようになった（自分で書くルールはエスケープされない）。v2.1.202 以前は未エスケープで保存され、`[2024-06] Reports` のようなディレクトリ向けの生成ルールが自身に一致しなかったり、意図しない兄弟ディレクトリに一致する恐れがあった。 — [English](https://code.claude.com/docs/en/permissions#read-and-edit)
- `cd` と `git` を1つの複合コマンドで組み合わせた場合のプロンプト条件が精緻化され、`cd` が別ディレクトリへ移動するとき（そのディレクトリの hooks が実行され得るため）のみプロンプトするようになった。cwd に解決される no-op の `cd` はプロンプトを誘発しない。 — [English](https://code.claude.com/docs/en/permissions#read-only-commands)
- mTLS クライアント証明書の in-place ローテーションに対応。Claude Code は証明書・鍵ファイルを起動時および設定適用のたびに再読込するため、同じパスにファイルを差し替えるだけでローテーションできる（あわせて、設定再適用時＝証明書 in-place ローテーション中の一時的な mTLS ハンドシェイク失敗も修正された）。
- skill を再 invoke した際、レンダリング内容が既にコンテキストにあるコピーと同一なら、instructions の2つ目のコピーではなく「already loaded」の短い注記を追加するようになった（引数変更や動的コンテキストで内容が異なる場合は従来通り全文を再追加）。v2.1.202 以前は再 invoke ごとに全文を重複追加していた。
- `/workflows` のエージェント一覧レイアウトが改善された（タイトル幅の拡大・専用の時刻列・短いモデル名表示・行ごとのツール呼び出し数の削除）。
- Debian/Ubuntu の apt インストール手順に、`curl` 未導入環境向けの `sudo apt install curl` ステップと、`.deb` 手動インストール時のパターン不一致エラー（`E: Unsupported file ...`）への対処注記が追加された。
- errors ページの「Installation errors」節の導入文が、対象を「install script（起動前）」から「install/update 中（install script・`claude install`・`claude update`）」へと一般化された。

**バグ修正**

- `Ctrl+R` のインライン履歴検索で、履歴ファイルの走査中に確定・キャンセルするとクラッシュ/内部エラーになる不具合を修正。走査中でも確定・キャンセルが即座に効くようになった。
- Remote Control（モバイル/web）から対話セッションに送ったコマンドが「Unknown command」で失敗する不具合を修正。
- Remote Control のモバイル/web アプリからキャプション無しで送った画像・ファイルが黙って破棄される不具合を修正（添付は `@` ファイル参照として渡されるようになった）。 — [日本語](https://code.claude.com/docs/ja/remote-control) / [English](https://code.claude.com/docs/en/remote-control)
- `claude auth login` と `claude mcp login --no-browser` が表示するサインイン URL が、SSH 越しに折り返すと確実にクリックできない不具合を修正（単一のハイパーリンクとして出力）。
- `claude agents` からチャットを開くと「currently running as a background agent」で失敗し、worker のクラッシュ/再生成ループになる不具合を修正。
- 文字列内に unicode のクォートエスケープを含むワークフロースクリプトがパース前に壊れる不具合を修正。ワークフローのパースエラーは常に TypeScript のせいにするのではなく、該当行を表示するようになった。
- 音声ディクテーションがマイク/録音の失敗時に無限リトライする不具合を修正（capture 失敗の連続で音声入力を一時停止）。voice の一時停止判定が、start-up 失敗だけでなく「録音開始後に音声を得られず停止した」capture 失敗も数えるようになった。
- 多数の git worktree があるリポジトリで、名前によるセッション resume や resume picker の表示が数分かかり大量のメモリを消費する不具合を修正。
- installer/updater のダウンロードがプロキシ/ネットワークの途中切断で即座に「aborted」で失敗する不具合を修正（一時的切断はリトライ。詳細はハイライト2参照）。
- 非同期（async）hook の JSON 出力を同期 hook と同じ出力スキーマで検証し、型が不正なフィールド（例: 文字列でない `systemMessage`）を配信せず破棄するようになった。`--debug` で破棄されたフィールドを警告表示する。v2.1.202 以前は async hook の不正 JSON 出力でセッションがクラッシュし、resume のたびに再発し得た。

**その他**

- changelog ページに v2.1.202（2026年07月06日）のリリースエントリが追加された（changelog ページ自体へのリンクは方針により付さない）。
- `/review` が高速な単一パスレビューに戻され、多エージェントレビューは `/code-review <level> <pr#>` を使うよう変更された。これに伴い commands ページの「Before you ship」記述・`/review` のコマンド表・`/code-review ultra` の比較表（Depth/Duration 列、"medium-effort" 表現の削除）・ultrareview ページの記述が更新された。
- errors ページの応答品質の項に、「Claude Code v2.1.200 以前で Sonnet 5 が prompt injection を疑って拒否したら `claude update` で v2.1.201 の修正を取得する」旨の注記が追加された（changelog の v2.1.201＝2026年07月03日エントリに対応）。
- `Esc` キーの挙動注記が更新され、権限プロンプト等のダイアログが開いているときは `Esc` が（Claude を中断するのではなく）ダイアログを閉じるようになった旨が明記された（v2.1.202 以前は一部ダイアログで Claude を中断しダイアログが残った）。
- `workflow.name` を含む OTel 属性は `OTEL_LOG_TOOL_DETAILS` でゲートされる（詳細はハイライト4参照）。
- 原文全文（llms-full）の setup ページ抽出で、Native Install／Homebrew／WinGet の `bash`／`powershell`／`batch` コードフェンス属性に付く `theme={null}` が、単一から最大5回連続へと重複した（スクレイプ由来のノイズの変動であり、ドキュメント内容の変更ではない）。前回（07-04 サマリ）に「6→1へ整理」と記録した箇所で、再び重複が増えた形。

## 新着情報

今回、週刊ダイジェスト「新着情報」（`whats-new/`）ページの新規追加・本文変更はありません（差分内に `whats-new/` を含む変更は 0 件。`llms.txt`・ドキュメントマップにも `whats-new/` の新規エントリはありません）。

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-07-04.md](./archives/latest/2026-07-04.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-07-04.md](./archives/latest-detail/2026-07-04.md)

<!--
base_commit: a036140d77a0f23cf530861a4b172aad2422a5a2
head_commit: eacae3b50bdabd388ec09e26647eca3a8ae25345
generated_at_full: 2026-07-07T15:02:04+09:00
-->
