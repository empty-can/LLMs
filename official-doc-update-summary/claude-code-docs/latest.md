---
対象期間: 2026年08月21日 〜 2026年08月22日
作成日: 2026-08-22
---

# Claude Code 公式ドキュメント更新サマリ

```markdown
今回は 1 日分の取り込みで、119 ページに差分がありました。新機能の追加は少なく、新着情報の 2 週分まとめ掲載と、サイト全体のリンク・見出しの整備が中心です。差分ページ数の割に中身が動いていないのが特徴で、119 ページのうち半数近くは表の桁揃えが入れ替わっただけです。changelog には v2.1.240 と v2.1.241 の 2 リリースが加わりましたが、いずれも本文は「バグ修正と信頼性の改善」の 1 行のみです。

主要なものを以下に挙げます。

1. auto モードの環境定義を Claude に下書きさせる `/auto-mode-setup` の解説が新設された
2. 新着情報が Week 33 と Week 34 の 2 週分まとめて掲載された
3. claude.ai から同期されるプラグイン `@synced` の扱いが正式に文書化された
4. `/docs` が抜けて別ページに飛んでいたリンク 171 本が一斉に修正された
5. 管理操作の主体が「Owner または admin」から「Owner」に統一された
```

## ハイライト

1. [**auto モードの環境定義を下書きする `/auto-mode-setup`**](./latest-detail.md#1-auto-モードの環境定義を下書きする-auto-mode-setup):  
  プロジェクトと最近のセッションを走査して `autoMode.environment` の下書きを作り、承諾すればユーザー設定に書き込むコマンド。auto モードが何度もブロックしたときに Claude Code 側から実行を持ちかけるようになった。
2. [**新着情報が Week 33 と Week 34 の 2 週分まとめて掲載された**](./latest-detail.md#2-新着情報が-week-33-と-week-34-の-2-週分まとめて掲載された):  
  8月10日〜14日と8月17日〜21日の 2 週が同時に公開された。`/design` スキル、Concise 出力スタイル、スマホからのローカルセッション開始、fork モードの既定 ON、GitLab 対応が主な内容。
3. [**claude.ai から同期されるプラグイン `@synced`**](./latest-detail.md#3-claudeai-から同期されるプラグイン-synced):  
  Cowork とクラウドセッションで、claude.ai アカウントで有効にしたプラグインが `<name>@synced` として読み込まれる仕組みが独立した節になった。同名の自前プラグインがある場合の優先順位も定義された。
4. [**`/docs` が抜けて別ページに飛んでいたリンク 171 本の一斉修正**](./latest-detail.md#4-docs-が抜けて別ページに飛んでいたリンク-171-本の一斉修正):  
  9 ページに残っていた `/en/...` 形式のリンクが `/docs/en/...` に直された。旧形式は 302 で製品紹介ページへ飛ばされており、参照先ドキュメントには到達できていなかった。
5. [**管理操作の主体が「Owner または admin」から Owner へ**](./latest-detail.md#5-管理操作の主体が-owner-または-admin-から-owner-へ):  
  11 ページ 20 箇所の「Owner または admin」が全て「Owner」になり、Remote Control ページの「admin」表記 2 箇所も同様に改められた。Admin ロールでは Cloud environments ページを開けないことが明記された。

## 新規追加されたページ

（今回の対象期間に新規追加されたリファレンス系ページはありません。`llms.txt` に加わった 2 ページはいずれも新着情報の週間ダイジェストのため、新着情報のセクションで扱います）

## 大幅に更新されたページ

- [**設定リファレンス**](./latest-detail.md#1-設定リファレンス) ([English](https://code.claude.com/docs/en/settings-reference#disablesideloadflags)):  
  追加 329 行・削除 327 行で今回最大の差分。その大半は 110 行のリンク修正（ハイライト 4 参照）と表の桁揃えで、内容の変更は `disableSideloadFlags` の 1 件。
- [**Agent SDK リファレンス TypeScript**](./latest-detail.md#2-agent-sdk-リファレンス-typescript) ([English](https://code.claude.com/docs/en/agent-sdk/typescript#tool-output-types)):  
  追加 123 行・削除 114 行。WebFetch の出力に `seeded` が加わり、アーティファクトの `force` 上書きの指針と、再 `initialize` 時のサブエージェント一覧の扱いが書き足された。
- [**コマンド**](./latest-detail.md#3-コマンド) ([English](https://code.claude.com/docs/en/commands#all-commands)):  
  追加 109 行・削除 108 行。`/auto-mode-setup` の行が新設され（ハイライト 1 参照）、`/claude-api` に `upgrade` サブコマンドが加わった。
- [**プラグインリファレンス**](./latest-detail.md#4-プラグインリファレンス) ([English](https://code.claude.com/docs/en/plugins-reference#synced-plugins)):  
  追加 90 行・削除 76 行。`@synced` プラグインの節が新設され（ハイライト 3 参照）、`pluginConfigs` の設定ソースを `--setting-sources` でどこまで外せるかが明確化された。
- [**エラーリファレンス**](./latest-detail.md#5-エラーリファレンス) ([English](https://code.claude.com/docs/en/errors#issuer-mismatch-in-authorization-response)):  
  追加 66 行・削除 81 行。MCP の OAuth サインインで発行者が一致しない場合と、起動ディレクトリが消えている場合の 2 節が新設された。
- [**エージェントビュー**](./latest-detail.md#6-エージェントビュー) ([English](https://code.claude.com/docs/en/agent-view#keyboard-shortcuts)):  
  追加 59 行・削除 58 行。vim エディタモードでの `Esc` がメインプロンプトと同じ挙動になり、入力を消さず NORMAL モードへ切り替えるようになった（v2.1.239）。
- [**.claude ディレクトリ**](./latest-detail.md#7-claude-ディレクトリ) ([English](https://code.claude.com/docs/en/claude-directory#cleaned-up-automatically)):  
  追加 55 行・削除 53 行。`uploads/<session>/` が自動掃除の対象表と手動削除の対象表の両方に加わった。
- [**クラウド環境の設定**](./latest-detail.md#8-クラウド環境の設定) ([English](https://code.claude.com/docs/en/cloud-environments#installed-tools)):  
  追加 34 行・削除 44 行。`gh` CLI がプリインストールに変わり、プリインストール一覧の PHP と Go の記載も訂正された。
- [**デスクトップアプリ**](./latest-detail.md#9-デスクトップアプリ) ([English](https://code.claude.com/docs/en/desktop#extend-claude-code)):  
  追加 34 行・削除 36 行。クラウドセッションでプラグインを使う手段に `@synced` が加わった（ハイライト 3 参照）。
- [**auto モードの設定**](./latest-detail.md#10-auto-モードの設定) ([English](https://code.claude.com/docs/en/auto-mode-config#generate-environment-entries)):  
  追加 57 行・削除 9 行。`/auto-mode-setup` の節が新設された（ハイライト 1 参照）。削除 9 行は表の桁揃えと既存節への導線追加。
- [**Claude apps ゲートウェイ**](./latest-detail.md#11-claude-apps-ゲートウェイ) ([English](https://code.claude.com/docs/en/claude-apps-gateway#connect-claude-desktop)):  
  追加 33 行・削除 31 行。Claude Desktop のどのタブがゲートウェイ経由になるかが明記され、Chat タブを有効にする `chatTabEnabled` が加わった。
- [**VS Code**](./latest-detail.md#12-vs-code) ([English](https://code.claude.com/docs/en/vs-code#work-with-git)):  
  追加 26 行・削除 38 行。`--worktree` の使い方を説明していた節が削除され、worktree の専用ページへの導線 1 文に置き換えられた。
- [**Claude Code の仕組み**](./latest-detail.md#13-claude-code-の仕組み) ([English](https://code.claude.com/docs/en/how-claude-code-works#work-effectively-with-claude-code)):  
  追加 13 行・削除 47 行。プロンプトの書き方に関する 3 節が削除され、ベストプラクティスのページへの導線に一本化された。

## 軽微な更新

今回は 1 日分の取り込みをまとめた対象期間で、差分のあったページは 119 です。changelog には v2.1.240（2026年08月22日）と v2.1.241（2026年08月23日）の 2 リリースが加わりましたが、いずれも本文は「バグ修正と信頼性の改善」の 1 行のみです。新規追加のリファレンス系ページは無く（新規の 2 ページはいずれも新着情報のため、そちらのセクションで扱います）、大幅更新として扱った 13 ページを除く 106 ページの変更をここで扱います。**大幅更新に入れる基準は「差分 50 行以上 かつ 内容の変更を伴うこと」**としました。50 行以上でも中身がリンク修正・見出しの書式変更・表の桁揃えだけのページ（環境変数・CLI リファレンス・Agent SDK の Python リファレンス・スキル・Hooks リファレンス・権限モードの選択など約 30 ページ）は、内容の変更が無いためここに回しています。なお本サマリの参考リンクは全て英語版のみです。今回変更のあったページは日本語版がまだ追従しておらず、auto モードの設定ページとプラグインリファレンスの 2 ページを実際に確認したところ、前者には `/auto-mode-setup` の節が無く（v2.1.211 で削除されたはずの「Default / protected branches」も残ったまま）、後者にも `@synced` の節がありませんでした。

**新機能**

- `/auto-mode-setup` がコマンド一覧に加わりました（詳細はハイライト 1 参照）— [English](https://code.claude.com/docs/en/commands#all-commands)
- `/claude-api` に `upgrade` 引数が加わりました。Python の `anthropic` パッケージを 0.x から 1.x へ、メジャーバージョンをまたいで移行するもので、v2.1.236 以降が必要です（詳細は大幅更新 3 参照）— [English](https://code.claude.com/docs/en/commands#all-commands)

**機能改善**

- クラウドセッションに `gh` CLI がプリインストールされるようになりました（詳細は大幅更新 8 参照）— [English](https://code.claude.com/docs/en/cloud-environments#installed-tools)
- Slack のルーティングに 2 つのモードがあることが明記されました。**Code + Chat** モードでは @Claude へのメンションがコーディングタスクかどうかを自動判定し、コーディングタスクだけを Claude Code on the web に回して他は通常のチャット返信になります。**Code only** モードでは全てのメンションが Claude Code に回ります — [English](https://code.claude.com/docs/en/slack#how-it-works)
- Chrome 拡張のタブグループの後始末が明文化されました。Claude が開いたタブはセッションに紐づくタブグループにまとめられ、ローカルセッションでは終わり方によって扱いが変わります。`/clear` の場合は開いているページごとグループを閉じます（`/clear` をまたいで残る作業が動いている場合を除く）。`/resume` などでのセッション切り替え・Claude Code の終了・作業が残っている状態での `/clear` では、空の新規タブしか無いときだけ閉じ、読みかけのページは残します — [English](https://code.claude.com/docs/en/chrome)
- モバイルアプリから添付した写真の扱いが箇条書きに整理されました。写真は従来どおりメッセージの一部として Claude が直接見るのに加え、`~/.claude/uploads/` 配下に保存され、そのパスが Claude に伝えられるようになりました。Claude が作るファイルに画像をコピーできます（保存先は大幅更新 7 参照）— [English](https://code.claude.com/docs/en/mobile#continue-a-local-session-with-remote-control)
- ルーティンのページに、Desktop のサイドバーに **Routines** が出ない場合はアカウントでルーティンが使えないことを示す、という案内が加わりました。組織ポリシーによる無効化の節へ導線が張られています — [English](https://code.claude.com/docs/en/routines#create-a-routine)
- Desktop のローカル定期タスクに、Claude Desktop 1.1.5368 より前のバージョンでは利用できない旨が加わりました。サイドバーに **Routines** が無い場合は Desktop アプリを更新し、組織側で無効化されていないか確認するよう案内されます — [English](https://code.claude.com/docs/en/desktop-scheduled-tasks#create-a-scheduled-task)
- 管理設定の階層で「サーバー管理設定が 1 つでもキーを配ればランナーイメージの管理設定ファイルは無視される」という説明に、**管理ソース全体から読まれるキーは例外**という但し書きが加わりました。`env` ブロックのほか、サンドボックスのロック、サンドボックスバイナリのパス、`forceRemoteSettingsRefresh` が挙げられています。同じ追記がクラウド環境の設定・デスクトップアプリ・管理設定・モデル設定・設定・組織向けセットアップ・セルフホスト環境の設定の各ページに入りました — [English](https://code.claude.com/docs/en/managed-settings#keys-read-from-every-admin-source)
- クリーンな設定で切り分けるときの注意に、管理設定が効き続ける理由が具体化されました。MDM プロファイル・レジストリポリシー・`managed-settings.json` は設定ディレクトリの外から読まれ、サーバー管理設定も資格情報が揃えばクリーンなセッションのために取得し直されます — [English](https://code.claude.com/docs/en/debug-your-config#test-against-a-clean-configuration)
- MCP のトークン更新が拒否されたときの案内が、`/mcp` を開いてサーバーの **Re-authenticate** を選ぶ、という操作手順の形に書き直されました — [English](https://code.claude.com/docs/en/mcp#authenticate-with-remote-mcp-servers)
- オンボーディングが **Default** クラウド環境を作る条件に「まだ環境を持っていなければ」という前提が加わりました。クラウド環境の設定・web のクイックスタート・Claude Code on the web の 3 ページで同じ書き足しです — [English](https://code.claude.com/docs/en/cloud-environments#the-default-environment)
- 音声ディクテーションの要件から、HIPAA コンプライアンスが有効でない組織では使えないという記述が外れました。トラブルシューティングの説明も「組織のコンプライアンス設定が無効にしている」から「組織の管理者ポリシーが無効にしている」という一般的な書き方に改められています — [English](https://code.claude.com/docs/en/voice-dictation#requirements)
- `MEMORY.md` の行数チェックの説明から、frontmatter とブロック HTML コメントが計測から除かれる旨の記述（v2.1.211 以降の挙動）が削除されました。CLAUDE.md の読み込み方の説明も、ディレクトリツリーを遡る手順の描写から「現在の作業ディレクトリとその上の全ディレクトリから読み込む」という結果の記述に簡潔化されています — [English](https://code.claude.com/docs/en/memory#how-claudemd-files-load)
- プロンプトキャッシュの `/model` 切り替え確認の説明が、経過時間の場合分けから「キャッシュが温かい間だけ確認を求める。温かさは最後のリクエストまたは応答から 1 TTL 続く」という 1 段落に整理されました — [English](https://code.claude.com/docs/en/prompt-caching#switching-models)
- コンピュータ使用のロックの説明が、ロックを取る主体を「Claude Code」から「セッション」に改め、2 つ目のセッションの試行は「ロックを持つセッションを名指ししたエラーで失敗する」と具体化されました — [English](https://code.claude.com/docs/en/computer-use#one-session-at-a-time)
- ディープリンクの `repo` パラメータの説明が、結論（最後に `claude` を実行したクローンまたは worktree を開く）を先に述べる形に組み替えられました — [English](https://code.claude.com/docs/en/deep-links#choose-between-cwd-and-repo)
- `--bare` を付けない `-p` セッションの説明が、主語を「Claude Code」から「`-p` セッション」に揃えて 2 文に整理されました。挙動そのものは変わりません — [English](https://code.claude.com/docs/en/headless#start-faster-with-bare-mode)
- ゲートウェイプロトコルの API 形式の説明で、形式を選ぶ主体がクライアントであることが明確化され、Google Cloud の Agent Platform に関する補足が独立した段落に分けられました — [English](https://code.claude.com/docs/en/llm-gateway-protocol)
- ステータスラインのスクリプトの説明が、stdin から JSON を受け取り stdout に出力する、という 1 文に簡潔化されました — [English](https://code.claude.com/docs/en/statusline)
- プルリクエスト作成の説明で、セッションと PR の紐づけの記述が、まず探し方（`claude --from-pr 1234`）を述べてから紐づく条件を挙げる順に組み替えられました — [English](https://code.claude.com/docs/en/common-workflows#create-pull-requests)
- クイックスタートで、資格情報の保存についての `<Tip>` ブロックがログイン手順の本文に統合されました — [English](https://code.claude.com/docs/en/quickstart)
- セッション管理のページの「関連ページ」に、セッションと並列実行の仕組みを扱うページ群である旨の導入文が加わりました — [English](https://code.claude.com/docs/en/sessions#see-also)

**バグ修正**

- v2.1.240（2026年08月22日）の changelog は「バグ修正と信頼性の改善」の 1 行のみで、個別の修正は挙げられていません
- v2.1.241（2026年08月23日）の changelog も同様に「バグ修正と信頼性の改善」の 1 行のみです

**その他**

- **`llms-full.txt` の生成方式が変わりました**。従来、明示的なアンカー ID を持つ見出しは `<h2>` / `<h3>` の生 タグ（ID 属性は落とされた状態）として出力されていましたが、今回から通常の Markdown 見出し（`##` / `###`）になりました。対象は 12 ページ 44 見出しで、エラーリファレンスの 25 個が最多、以下 権限モードの選択 5 個、クロスセッションメッセージング／ルーティン／設定ファイルの実例／インストールのトラブルシュートが各 2 個、Claude apps ゲートウェイ／フルスクリーン／インタラクティブモード／Remote Control／スキル／web のクイックスタートが各 1 個です。**公式ページ側は変わっていません**（実際に取得して確認したところ、ルーティンや権限モードのページは今も `<h3 id="...">` のままで、新設された文言も入っています）。したがってアンカーも変わっていませんが、`llms-full.txt` の見出し文字列から GFM 規則でアンカーを機械生成すると誤った値になる点には注意が要ります（例: 「Eliminate permission prompts with auto mode」の実際の ID は `eliminate-prompts-with-auto-mode`）
- **前回サマリの訂正**: 前回、インタラクティブモードの新設節について「ページ内から張られたリンクが旧名のアンカー `#make-ctrl-w-delete-back-to-whitespace` を指したままで、現在の見出しから生成されるアンカーと一致していない」と述べましたが、これは誤りでした。当該見出しは `<h3 id="make-ctrl-w-delete-back-to-whitespace">` という明示的な ID を持っており、リンクは正しく機能します（今回、公式ページを取得して確認しました）
- 表の区切り行（`| :--- | :--- |`）の桁揃えが全ページ規模で入れ替わりました。これが差分行数を実態より大きく見せています。区切り行を除外し空白を全て詰めて比べ直すと、差分のあった 119 ページのうち **54 ページは差分が完全に消え**、残る 65 ページも多くはリンク修正・見出しの書式変更だけです（正規化の仕方によっては 56 / 63 ページ程度に振れます）。環境変数（追加 323 行・削除 322 行）が典型で、内容としての変更はありません
- 本文中に残っていた空要素 `<a />` が 7 個削除されました（Hooks リファレンスに 3 個、デスクトップアプリに 2 個、VS Code と Claude apps ゲートウェイの設定に各 1 個）
- `llms.txt` の差分は 2 行で、Week 33 と Week 34 の追加のみです。ページの削除も説明文の変更もありません
- ページ見出しマップ（`claude_code_docs_map.md`）の差分は、Claude Code の仕組みから 3 節（大幅更新 13 参照）、VS Code から 1 節（大幅更新 12 参照）が消え、エラーリファレンスに 2 節（大幅更新 5 参照）、auto モードの設定に 4 節（ハイライト 1 参照）、プラグインリファレンスに 1 節（ハイライト 3 参照）が加わり、新着情報に 2 ページが加わったものです

## 新着情報

- [**2026年08月17日～21日(Week 34)**](./latest-detail.md#2026年08月17日21日week-34) ([English](https://code.claude.com/docs/en/whats-new/2026-w34)):  
  102 行の新規ページ。v2.1.234〜v2.1.239 が対象で、`/design` スキル、Concise 出力スタイル、スマホからのローカルセッション開始の 3 本立て。
- [**2026年08月10日～14日(Week 33)**](./latest-detail.md#2026年08月10日14日week-33) ([English](https://code.claude.com/docs/en/whats-new/2026-w33)):  
  84 行の新規ページ。v2.1.225〜v2.1.233 が対象で、Desktop の使用量上限後の自動継続、fork モードの既定 ON、GitLab 対応の 3 本立て。
- [**新着情報の索引ページ**](./latest-detail.md#2-新着情報が-week-33-と-week-34-の-2-週分まとめて掲載された) ([English](https://code.claude.com/docs/en/whats-new/index)):  
  追加 16 行。Week 34 と Week 33 のダイジェスト（各 3〜4 行の要約と各週ページへの導線）が先頭に加わった。
- [**Week 32 のページ**](./latest-detail.md#5-管理操作の主体が-owner-または-admin-から-owner-へ) ([English](https://code.claude.com/docs/en/whats-new/2026-w32)):  
  追加 2 行・削除 2 行。セルフホスト環境の有効化操作の主体が「Owner または admin」から「Owner」になった。

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-08-21.md](./archives/latest/2026-08-21.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-08-21.md](./archives/latest-detail/2026-08-21.md)

<!--
base_commit: bf6b02f6941da4409ac9203cdb36011f4383835c
head_commit: 38adb8c17987c2872a55345390bf77b43146ab00
generated_at_full: 2026-08-23T15:16:39+09:00
-->
