---
対象期間: 2026年06月23日 〜 2026年06月24日
作成日: 2026-06-24
---

# Claude Code 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
今回の対象期間は、先に changelog で告知されていた Claude Code v2.1.187 系の機能について、各リファレンスページの本文が大きく追記された更新が中心です。組織によるモデル制限の整備と、LLM ゲートウェイドキュメントの 3 ページ分割が目立ちます。

主要なものを以下に挙げます。

1. Claude Console で個別モデルを無効化する「組織レベルのモデル制限」が新設され、選択時の挙動と専用エラーメッセージが文書化された（v2.1.187）
2. availableModels 許可リストのドキュメントが大幅拡充され、各サーフェスへの配信経路を示す表や Default モデルの強制（enforceAvailableModels）の詳細が整理された
3. sandbox.credentials 設定が追加され、サンドボックス内のコマンドから認証情報ファイルの読み取りとシークレット環境変数を遮断できるようになった（v2.1.187）
4. サーバー管理設定の配信条件（組織 OAuth ログイン／直接設定の API キーが必要、apiKeyHelper は対象外、Claude Platform on AWS は非対応）が明確化された
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**Claude Console による組織レベルのモデル制限**](#1-claude-console-による組織レベルのモデル制限):  
  Claude Console で個々のモデルを無効化して、組織メンバーが実行できるモデルを制限する仕組みが「Organization model restrictions」として新設された。制限モデルは `/model` ピッカーから隠され、`--model` 等で指定すると許可モデルに置き換える旨の通知が出る。`availableModels` とは独立して認証時のエンタイトルメントで配信され、サーバー側でも独立して強制される（v2.1.187）。
2. [**availableModels 許可リストの適用範囲と Default モデル強制**](#2-availablemodels-許可リストの適用範囲と-default-モデル強制):  
  `availableModels` のドキュメントが大幅に拡充された。許可リストが CLI/IDE・Desktop・Web/モバイル/クラウド・Agent SDK・Cowork の各サーフェスへどの配信経路（サーバー管理設定 / MDM・管理設定ファイル）で届くかを示す「Surface coverage」表が追加され、適用先も skills・commands・サブエージェント・フォールバックチェーン等へ広がった旨が整理された。`enforceAvailableModels` による Default モデルの強制も詳細化された。
3. [**sandbox.credentials によるサンドボックスの認証情報保護**](#3-sandboxcredentials-によるサンドボックスの認証情報保護):  
  サンドボックス内のコマンドがアクセスしてはいけない認証情報ファイルと環境変数を宣言する `sandbox.credentials` 設定が追加された。`credentials.files` は `filesystem.denyRead` と同じ読み取り遮断を適用し、`credentials.envVars` は各コマンド実行前に変数を unset する。対応値は `deny` のみで全スコープからマージされる（v2.1.187）。
4. [**サーバー管理設定の配信条件の明確化**](#4-サーバー管理設定の配信条件の明確化):  
  サーバー管理設定が配信されるには、セッションが組織 OAuth ログインまたは直接設定された API キーで認証されている必要があり、`apiKeyHelper` スクリプトが返すキーでは配信トリガーにならない旨が明記された。非対応プロバイダーの一覧に Claude Platform on AWS が追加され、エンドポイント管理設定がクラウドセッションに届かない点も補足された。
<!-- light:highlight-list:end -->

## 1. Claude Console による組織レベルのモデル制限

「モデル設定」ページに「Organization model restrictions」セクションが新設されました。メンバーが Anthropic API で認証する組織向けに、設定ファイルを配布せずに 1 つの組織全体スイッチでモデルを制限したい場合の方法で、管理者が Claude Console で個別モデルを無効化することで、メンバーが実行できるモデルを制限します。この制限は Claude Code 認証時にアカウントのエンタイトルメントとともに配信され、設定内の `availableModels` リストとは別に扱われ、セッション作成時にサーバー側でも独立して同じ制限が強制されます。Claude Code v2.1.187 以降が必要です。

制限されたモデルは `/model` ピッカーから隠されます。`--model`・`ANTHROPIC_MODEL` 環境変数・`model` 設定で名前指定すると `Model "<name>" is restricted by your organization's settings. Using <model> instead.` という通知が表示され、許可モデルでセッションが開始されます。`/model <name>` で制限モデルを入力した場合は拒否され、セッションは現在のモデルを維持します。`availableModels` と組織制限は合成され、モデルは「`availableModels` に許可され、かつ組織に制限されていない」場合にのみ選択可能です。組織制限は Anthropic API と LLM ゲートウェイのデプロイメントには配信されますが、Bedrock・Vertex AI・Foundry・Claude Platform on AWS には配信されないため、それらのプロバイダーでは `availableModels` を使います。あわせてトラブルシューティングに「Model is restricted by your organization's settings」エラーの対処節も追加されました。

- [Model configuration - Claude Code Docs (English)](https://code.claude.com/docs/en/model-config#organization-model-restrictions)

## 2. availableModels 許可リストの適用範囲と Default モデル強制

`availableModels` 許可リストのドキュメントがこの期間に大きく拡充されました。許可リストが適用される場所として、メインセッションモデルに加えて skills・commands の `model` フロントマター、サブエージェント、アドバイザーモデルと `--advisor` フラグ、バックグラウンドエージェントのディスパッチピッカーが明示され、フォールバックチェーンや `opusplan` のプランモード昇格、自動モデルフォールバックといった自動的なモデル変更も同じく許可リストで検査される旨が整理されました。さらに、許可リストがどの配信経路（管理コンソールのサーバー管理設定／MDM・管理設定ファイル）で CLI・IDE・Desktop ローカル・Web/モバイル/クラウド・Agent SDK・Cowork の各サーフェスに届くかをまとめた「Surface coverage」表が追加されています。クラウドセッションには端末配布の設定が届かないためサーバー管理設定で配信する、といった注意も併記されました。

`enforceAvailableModels` による Default モデルの強制についても記述が詳細化されました。`availableModels` 単独では Default オプションは影響を受けず、`enforceAvailableModels: true` を空でない `availableModels` とともに管理設定に置くことで Default も許可リストに従わせられます（v2.1.175 以降）。アカウントタイプの既定モデルが許可リストにない場合、Default は許可リスト先頭の利用可能なエントリに解決されます。`availableModels` が空配列のときは強制が働かず Default は使える、許可リスト内に利用可能なエントリが 1 つも解決しない場合は `--debug` でのみ見える警告とともにアカウント既定へフォールバックする、といった縮退動作も明記されました。マージ動作も改められ、最高優先度の管理ソースが `availableModels` を定義するとそのリストがそのまま適用され、下位スコープは拡張できない旨が整理されています。

- [Model configuration - Claude Code Docs (English)](https://code.claude.com/docs/en/model-config#restrict-model-selection)
- [Model configuration - Claude Code Docs (English)](https://code.claude.com/docs/en/model-config#surface-coverage)

## 3. sandbox.credentials によるサンドボックスの認証情報保護

「サンドボックス化された Bash ツールを設定する」ページに「認証情報を保護する」セクションが追加されました。`sandbox.credentials` 設定は、サンドボックス化されたコマンドがアクセスしてはいけない認証情報ファイルと環境変数を宣言します。リストしたファイルパスにはサンドボックス内の読み取りに対して `filesystem.denyRead` と同じ遮断が適用され、リストした環境変数は各サンドボックスコマンドの実行前に unset されます。専用の `credentials` ブロックを設けることで、環境変数の unset とあわせて認証情報ルールを一般的なファイルシステムルールから分離してグループ化できます。Claude Code v2.1.187 以降が必要です。

各エントリは `"mode": "deny"` を持ち、これが唯一サポートされる値です（明示的な `mode` フィールドにより将来のモード追加にスキーマを前方互換に保ちます）。ファイルパスは `sandbox.filesystem.*` と同じプレフィックスルールに従い、全設定スコープのエントリがマージされます。モードが `deny` のみであるため、どのスコープも制限を追加できますが、削除はできません。組み込みの認証情報拒否リストは無く、リストしたファイルと変数だけが制限される点、影響対象はサンドボックス化された Bash コマンドのみである点も明記されました。設定リファレンスにも `credentials.files` / `credentials.envVars` の各キーが追加されています。

- [サンドボックス化された Bash ツールを設定する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/sandboxing#protect-credentials)
- [Configure the sandboxed Bash tool - Claude Code Docs (English)](https://code.claude.com/docs/en/sandboxing#protect-credentials)

## 4. サーバー管理設定の配信条件の明確化

「サーバー管理設定を構成する」ページで、設定が配信される条件が明確化されました。Claude Code クライアントがサーバー管理設定を受け取るには、セッションが組織の OAuth ログインまたは直接設定された API キーで認証されている必要があり、`apiKeyHelper` スクリプトが返すキーは設定フェッチをトリガーしません。キーをスクリプト経由でのみ生成するフリートでは、許可リストを MDM または管理設定ファイルで配信するよう案内されています。

あわせて、サーバー管理設定が利用できない非対応プロバイダーの一覧に Claude Platform on AWS が追加され、`CLAUDE_CODE_USE_ANTHROPIC_AWS` がサーバー管理設定をバイパスする条件にも加えられました。エンドポイント管理設定はクラウドセッション（Claude Code on the web 等）に届かないため、Web で Claude Code を使う組織はサーバー管理設定も構成する必要がある旨も補足されています。スコープ表も更新され、サーバー管理配信は全組織メンバー、plist・HKLM レジストリ・ファイル配信はマシンの全ユーザー、HKCU レジストリは現在のユーザー、と配信経路ごとの影響範囲が整理されました。

- [サーバー管理設定を構成する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/server-managed-settings#platform-availability)
- [Configure server-managed settings - Claude Code Docs (English)](https://code.claude.com/docs/en/server-managed-settings#platform-availability)

## 新規追加されたページ

<!-- light:new-pages:start -->
LLM ゲートウェイのドキュメントが再編され、従来の単一ページ（「LLM gateways」に改称）に加えて、用途別に 3 ページが新規追加されました。いずれも現時点では英語ページのみで、日本語ページは未提供です。

- [**LLM ゲートウェイへの接続**](#1-llm-ゲートウェイへの接続) ([English](https://code.claude.com/docs/en/llm-gateway-connect)):  
  組織の LLM ゲートウェイに Claude Code を向ける手順。管理者が既に設定済みかの確認方法、CLI・VS Code・GitHub Actions・Agent SDK でベース URL と認証情報を自分で設定する方法、接続の検証とゲートウェイエラーの修正を扱う。
- [**ゲートウェイプロトコルリファレンス**](#2-ゲートウェイプロトコルリファレンス) ([English](https://code.claude.com/docs/en/llm-gateway-protocol)):  
  Claude Code と LLM ゲートウェイ間の API 契約。転送すべきエンドポイント・ヘッダー・ボディフィールド、フィールド除去時の機能縮退、コスト追跡用の属性ヘッダー、モデルディスカバリーを規定する。
- [**組織向け LLM ゲートウェイの展開**](#3-組織向け-llm-ゲートウェイの展開) ([English](https://code.claude.com/docs/en/llm-gateway-rollout)):  
  Claude Code 向けにゲートウェイ製品をデプロイする方法。Claude Code の送信内容を転送するための設定、開発者向け認証情報の発行、管理設定を通じた構成配布、ロールアウトの検証を扱う。
<!-- light:new-pages:end -->

## 1. LLM ゲートウェイへの接続

組織の LLM ゲートウェイに Claude Code を向けるための手順をまとめた新規ページです。まず管理者が既にゲートウェイを設定済みかどうかを確認し、未設定なら CLI・VS Code・GitHub Actions・Agent SDK のそれぞれでベース URL と認証情報を自分で設定する方法を案内します。その後、接続が成立しているかの検証と、ゲートウェイ起因のエラーの修正までを扱います。

本ページの本文は現時点で `llms-full.txt`（全文展開）にはまだ取り込まれておらず、英語ページのみの提供です。日本語ページは未提供のため、リンクは英語のみとしています。

- [Connect Claude Code to an LLM gateway - Claude Code Docs (English)](https://code.claude.com/docs/en/llm-gateway-connect)

## 2. ゲートウェイプロトコルリファレンス

Claude Code と LLM ゲートウェイの間の API 契約を定めた新規リファレンスページです。ゲートウェイが転送すべきエンドポイント、ヘッダーおよびボディのフィールド、フィールドが除去された場合に発生する機能縮退、コスト追跡のための属性（attribution）ヘッダー、モデルディスカバリーの仕様を規定します。ゲートウェイ製品を実装・運用する側が参照する技術リファレンスにあたります。

本ページも全文展開にはまだ取り込まれておらず、英語ページのみの提供です。

- [Gateway protocol reference - Claude Code Docs (English)](https://code.claude.com/docs/en/llm-gateway-protocol)

## 3. 組織向け LLM ゲートウェイの展開

Claude Code 向けにゲートウェイ製品を組織展開する方法をまとめた新規ページです。Claude Code が送信する内容を転送するためのゲートウェイ設定、開発者へ配る認証情報の発行、管理設定を通じた構成の配布、そしてロールアウトの検証という運用フローを扱います。前述の「接続」ページがエンドユーザー視点なのに対し、こちらは管理者・運用者視点の展開手順という位置づけです。

本ページも全文展開にはまだ取り込まれておらず、英語ページのみの提供です。

- [Roll out an LLM gateway for your organization - Claude Code Docs (English)](https://code.claude.com/docs/en/llm-gateway-rollout)

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
今回の主要な大幅更新（モデル設定 / サーバー管理設定 / サンドボックス）は、いずれも上記ハイライトに整理しました。これら以外で単一ページ 50 行以上に該当する独立した大幅更新はありません。その他の小規模な変更は下記「軽微な更新」にまとめています。
<!-- light:updated-pages:end -->

## 軽微な更新

<!-- light:minor-updates:start -->
今回の軽微な更新は、changelog で先行告知されていた Claude Code v2.1.187 系の機能について、各リファレンスページ本文へ説明が追記されたものが中心です（多くは前回サマリで changelog 項目として既出のため、ここではドキュメント化された点を簡潔に挙げます）。以下に分類して整理します。

**新機能**

- リモート MCP ツール呼び出しのアイドルタイムアウトを制御する `CLAUDE_CODE_MCP_TOOL_IDLE_TIMEOUT` 環境変数が文書化された（HTTP/SSE/WebSocket/claude.ai コネクタ向け、既定 300000 ミリ秒＝5 分、`0` で無効化。v2.1.187） — [English](https://code.claude.com/docs/en/mcp)
- フルスクリーンレンダリングで、権限プロンプト・`/model`・`/config` などの選択メニューをマウスクリックで選べる旨が追記された（v2.1.187） — [English](https://code.claude.com/docs/en/fullscreen)
- 認証エラー「Model is restricted by your organization's settings」のトラブルシューティング節が追加された（詳細はハイライト 1 参照）

**機能改善**

- `/btw` の回答オーバーレイに ←/→ キーが追加され、セッション内の過去の `/btw` 回答をたどれる旨がキー一覧に明記された（v2.1.187） — [English](https://code.claude.com/docs/en/interactive-mode)
- `/plugin`（プラグイン一覧）の Installed タブに、自分で入れたが最近使っていないプラグインをまとめる「Not used recently」グループと各プラグインの「Last used」行の説明が追記された（v2.1.187） — [English](https://code.claude.com/docs/en/plugins)
- `/install-github-app` で GitHub Actions のセットアップが任意になり、App のインストールだけ行って「Skip for now」で止め、後から再実行できる旨が Quick setup に追記された（v2.1.187） — [English](https://code.claude.com/docs/en/github-actions#quick-setup)
- バックグラウンドサブエージェントの深さが初回スポーン時に固定され、後から再開しても深さが変わらない旨が追記された（v2.1.187） — [English](https://code.claude.com/docs/en/sub-agents)
- `Ctrl+R` のコマンド履歴検索が、選択スコープの「直近 100 件の一意なプロンプト」を読み込む（重複は最新のものに集約）旨が明記された — [English](https://code.claude.com/docs/en/interactive-mode)
- `availableModels` 許可リストの適用先が skills・commands・サブエージェントのモデル指定にも及ぶ旨が各ページに反映された（詳細はハイライト 2 参照）
- Claude Code Desktop の「Managed settings」節が更新され、ローカル/クラウド/SSH の各セッションへ管理設定がどの経路で届くかが箇条書きで整理された。あわせて `managedMcpServers` キーの説明に、サードパーティ（3P）デプロイメントでは管理設定ファイルまたは MDM 経由で配信する必要がある旨の注記が加わった（詳細はハイライト 4 参照） — [English](https://code.claude.com/docs/en/desktop#managed-settings)
- 管理コントロール一覧（admin-setup）に、`availableModels`・`enforceAvailableModels` を使う「Model restrictions」行が追加された（詳細はハイライト 2 参照） — [English](https://code.claude.com/docs/en/admin-setup)

**その他**

- changelog ページに v2.1.190（2026年06月24日）「バグ修正と信頼性の改善」のリリースエントリが追加された（changelog リンク不使用ポリシーによりリンクは付しません）。
- 音声入力ヘルプの表記が `Space` から小文字の `space` に統一されるなどの字句修正が入った。
- ドキュメントマップ上で「Eliminate prompts with auto mode」の見出しが「Eliminate permission prompts with auto mode」に改称された。
<!-- light:minor-updates:end -->

## 新着情報

<!-- light:whats-new:start -->
（今回の対象期間に新着情報ページの更新はありません）
<!-- light:whats-new:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-06-23.md](./archives/latest/2026-06-23.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-06-23.md](./archives/latest-detail/2026-06-23.md)

<!--
base_commit: a8b1232abacba9353171c44560e7a6a4bfd70a63
head_commit: 01b0ad7141ef8c6ea3006c5c4ecabc1e8aec69c0
generated_at_full: 2026-06-25T15:03:55+09:00
-->
