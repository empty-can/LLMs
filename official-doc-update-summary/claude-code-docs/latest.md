---
対象期間: 2026年08月24日 〜 2026年08月25日
作成日: 2026-08-25
---

# Claude Code 公式ドキュメント更新サマリ

```markdown
今回は 2 日分の取り込みで、26 ページに差分がありました。差分行 502 のうち 131 行は changelog で、v2.1.243・v2.1.245・v2.1.246 の 3 リリースが一度に加わっています。ページの新規追加・削除はありませんが、`llms.txt` の構成そのものが「Docs」1 本の平坦なリストからカテゴリ別の 46 見出しに組み替えられ、11 言語の翻訳版インデックスへの導線も加わりました。

主要なものを以下に挙げます。

1. Bash 許可ルールの `*` の効き方が全面的に書き直され、サブコマンドより前に `*` を置いた許可ルールに起動時警告が出るようになった
2. `/permissions` に Auto mode タブが加わり、auto モード分類器のルールを設定ファイルを開かずに編集できるようになった
3. Claude が自分から `/code-review` を始められる範囲が、クラウドプロバイダ・ゲートウェイ・テレメトリオフのセッションにも広がった
4. 組織がデスクトップアプリの「端末上で動くセッション」だけを止められる `disableDesktopLocalSessions` が加わった
5. Linux デスクトップ版に Cowork の動作要件（QEMU / KVM）と、動かないときの切り分けが明記された
```

## ハイライト

1. [**Bash 許可ルールのワイルドカードの効き方が書き直され起動時警告が加わった**](./latest-detail.md#1-bash-許可ルールのワイルドカードの効き方が書き直され起動時警告が加わった):  
  `*` が何を代入するのかが 3 つの規則にまとめられ、「書いたルール / マッチするコマンド / マッチしないコマンド」の一覧表が新設された。`Bash(git * main)` のようにサブコマンドより前に `*` を置いた **allow ルール**には、起動時に警告が出るようになった。v2.1.246 以降。
2. [**`/permissions` の Auto mode タブで分類器ルールを編集する**](./latest-detail.md#2-permissions-の-auto-mode-タブで分類器ルールを編集する):  
  `allow` / `soft_deny` / `hard_deny` / `environment` をダイアログから追加・編集・削除でき、変更は `~/.claude/settings.json` に保存される。組み込みルールの ON/OFF も `"$defaults"` の出し入れとして記録される。v2.1.246 以降。
3. [**Claude が自分から `/code-review` を始められる範囲が広がった**](./latest-detail.md#3-claude-が自分から-code-review-を始められる範囲が広がった):  
  従来は Anthropic から取得する feature flag が有効なセッションに限られていた。クラウドプロバイダ・Claude apps ゲートウェイ・テレメトリを切ったセッションで自発起動できなかった制限が撤廃された。v2.1.246 以降。
4. [**デスクトップの端末上セッションを組織で止める `disableDesktopLocalSessions`**](./latest-detail.md#4-デスクトップの端末上セッションを組織で止める-disabledesktoplocalsessions):  
  管理設定専用の新キー。**Local** はドロップダウンに残るがグレーアウトし、新規セッションは設定済みの SSH 接続にフォールバックする。SSH とクラウドのセッションは影響を受けない。
5. [**Linux デスクトップ版に Cowork の動作要件と切り分けが明記された**](./latest-detail.md#5-linux-デスクトップ版に-cowork-の動作要件と切り分けが明記された):  
  Cowork は QEMU + KVM の仮想マシン上で動くため、ハードウェア仮想化・QEMU/UEFI パッケージ・`kvm` グループ参加の 3 つが要る。表示されるメッセージ別の対処も新設された。

## 新規追加されたページ

（今回の対象期間に新規追加されたドキュメントページはありません。`llms.txt` のエントリは 191 件から 202 件に増えていますが、増えた 11 件は新設の `## Indexes` セクションに並ぶ翻訳版ドキュメントの索引ファイル（`https://code.claude.com/docs/_llms/<lang>.md`）であり、ドキュメントページそのものではないため、ここには数えていません。詳細は軽微な更新の導入文を参照）

## 大幅に更新されたページ

（今回、大幅更新の基準に達した通常ページはありません。最大の差分は changelog の 131 行ですが、これはリリースエントリの追加なので軽微な更新で扱います。通常ページの最大は権限の設定の 46 行、次いでエラーリファレンスの 40 行、Linux デスクトップの 35 行で、いずれも 50 行に届いていません。この 3 ページの内容はハイライト 1・5 で扱っています）

## 軽微な更新

今回は 2 日分の取り込みで、`llms-full.txt` に差分のあったページは 26 です。ページの新規追加・削除はありません。差分行は合計 502 行で、うち 131 行は changelog です。**大幅更新に入れる基準は前回同様「実質の差分 50 行以上 かつ 内容の変更を伴うこと」**とし、今回は該当なしとしました（判定は表の桁揃え等の空白を無視した実質の差分で行っています）。

changelog には **v2.1.243・v2.1.245・v2.1.246 の 3 リリース**が一度に加わりました。いずれも 2026年08月25日 付です。前回時点の最新は v2.1.241（2026年08月23日）で、v2.1.242 と v2.1.244 のエントリは公開されていません。3 リリースの項目数は v2.1.246 が 61、v2.1.245 が 1、v2.1.243 が 60 の計 122 件です。以下では各項目を独立した bullet として、バージョンを併記して並べます。**changelog ページへのリンクは張りません**。

`llms.txt` は今回、構成そのものが変わりました。従来は `## Docs` という 1 つの見出しの下に全エントリが平坦に並んでいましたが、`## Getting started`・`## Core concepts`・`## Reference` のようなカテゴリ見出し 46 個に分割されました。見出しには重複があり（`Platforms and integrations` が 3 回、`Core concepts` と `Deployment` が 2 回ずつ）、ユニークなカテゴリ名は 42 です。エントリ数は 191 件から 202 件に増えていますが、増えた 11 件は末尾に新設された `## Indexes` セクションの、フランス語・ドイツ語・イタリア語・日本語・スペイン語・韓国語・中国語・繁体字中国語・ロシア語・インドネシア語・ブラジルポルトガル語の各インデックス（`https://code.claude.com/docs/_llms/<lang>.md`、いずれも 166 ページと表示）です。セクションの直前には「以下のリンクはドキュメントの索引を指す。各 `/_llms/` 索引をドキュメントページに行き着くまで再帰的に辿ること」という案内文が置かれています。**これらは翻訳版ドキュメントの索引ファイルであってドキュメントページそのものではないため、新規追加ページには数えていません。**英語ドキュメントページの増減はゼロです。

ページ見出しマップ（`claude_code_docs_map.md`）は前回「差分なし」でしたが、今回は前回分の新設節（`modelPicker`・`promptCacheTtl`・`subagentPromptCacheTtl`・`autoContinueAtUsageLimit`、使用量上限の待機、`headersHelper` とその配下、組織設定経由の配布）と今回分の新設節（Auto mode タブ関連、`disableDesktopLocalSessions`、Cowork 要件、Bash ワイルドカード警告、Bedrock のストリーミングエラー）をまとめて取り込みました。生成時刻の表記も 2026年08月22日 18:29 UTC から 2026年08月26日 02:08 UTC に進んでいます。

なお本サマリの参考リンクは全て英語版のみです。今回の変更に日本語版が追従していないためで、権限の設定と auto モードの設定の 2 ページを実際に取得して確認したところ、前者の「ワイルドカードパターン」節は旧記述のまま（`Bash(git * main)` を含む JSON 例が残り、警告ブロックも一致表もありません）で、後者には `/permissions` からルールを編集する節そのものがありませんでした。他のページは個別には確認していませんが、いずれも同じリリース群（v2.1.243〜v2.1.246）に対応する記述であるため未追従とみなし、安全側に倒して英語版のみを載せています。

**新機能**

- サブコマンドより前に `*` を置いた Bash の allow ルールに、起動時警告が出るようになりました（v2.1.246、詳細はハイライト 1 参照）— [English](https://code.claude.com/docs/en/errors#has-a-wildcard-before-the-rest-of-the-command)
- `/permissions` に **Auto mode** タブが加わり、分類器ルールを設定ファイルなしで編集できるようになりました（v2.1.246、詳細はハイライト 2 参照）— [English](https://code.claude.com/docs/en/auto-mode-config#edit-rules-from-permissions)
- 管理設定に `disableDesktopLocalSessions` が加わりました（詳細はハイライト 4 参照。必要バージョンの記載はありません）— [English](https://code.claude.com/docs/en/settings-reference#disabledesktoplocalsessions)
- Linux デスクトップ版に Cowork の動作要件の節と、Cowork が使えないときの対処の節が新設されました（詳細はハイライト 5 参照）— [English](https://code.claude.com/docs/en/desktop-linux#cowork-requirements)
- 環境変数に `CLAUDE_CODE_DISABLE_BEDROCK_CONTENT_TYPE_DEFAULT` が加わりました（v2.1.239 以降）。Amazon Bedrock は `Content-Type` ヘッダを必ず送るため、ヘッダが無い／空のストリーミング応答は「プロキシがヘッダを剥がした」とみなして既定ではバイナリのイベントストリーム形式として復号します。プロキシがヘッダを剥がしたうえで本文を server-sent events として出し直す場合にだけ、この変数を `1` にして本文を server-sent events として読ませます — [English](https://code.claude.com/docs/en/env-vars#variables)
- エラーリファレンスに `Streaming response ended before any complete data was received` が加わりました。ストリーミング応答が使えるデータを 1 つも返さずに終わったためストリーミング無しで送り直した、という警告で、対話セッションでセッションにつき 1 回だけ出ます。リクエストは 2 回送られ、原因はたいてい戻りのストリーミング本文を食う／変換するプロキシやゲートウェイです。v2.1.239 より前は黙って再送していました — [English](https://code.claude.com/docs/en/errors#streaming-response-ended-before-any-complete-data-was-received)
- キーバインドのキー名に `wheelup` と `wheeldown` が加わり、`scroll:lineUp` / `scroll:lineDown` の既定バインドが「未割り当て」からこの 2 つになりました — [English](https://code.claude.com/docs/en/keybindings#special-keys)
- `/usage` のプラン使用量の内訳に **Loops** の行が加わりました（v2.1.243）。1 ループあたりの実行回数・合計トークン・1 回あたりトークン・最終実行が出るため、暴走した／おしゃべりな `/loop` タスクを見つけやすくなります。ドキュメント側の記述は前回サマリで扱っており、今回はそれに対応するリリースエントリです — [English](https://code.claude.com/docs/en/costs#plan-usage-breakdown)
- `modelPicker` 設定が加わりました（v2.1.243）。順序とラベルを指定したモデル一覧で `/model` ピッカーを整えるもので、Vertex / Bedrock 形式を含む任意の ID 表記が使え、組み込みの並びに足すことも置き換えることもできます。なおドキュメント本文は「v2.1.242 以降が必要」と書いており、changelog のリリース番号とは一致しません — [English](https://code.claude.com/docs/en/settings-reference#modelpicker)
- `promptCacheTtl` と `subagentPromptCacheTtl` 設定が加わりました（v2.1.243）。API キー・クラウドプロバイダの利用者がメイン会話のプロンプトキャッシュを 1 時間に保ちつつ、サブエージェントを 5 分のままにできます。こちらもドキュメント本文の記述は「v2.1.242 以降」です — [English](https://code.claude.com/docs/en/settings-reference#promptcachettl)
- `modelPricing` 管理設定が加わりました（v2.1.243）。組織が契約したモデル別レートと割引係数が、`/cost`・ステータスライン・テレメトリのコスト表示で定価の代わりに使われます
- `/login` の Anthropic Console に「Sign in with your Console account」というキーレスのサインインが加わりました（v2.1.243）。API キーの作成と並ぶ推奨の選択肢で、API キーを許可しない組織でもサインインできます
- `/status` に `Skipped sources` 行が加わりました（v2.1.243）。存在するが優先度の高い管理ソースが有効なために適用されていない管理設定ソース（`managed-settings.json` など）を挙げます
- `/mcp` と `/plugins` で、認証を組織が管理している claude.ai コネクタに `managed` マーカーが付くようになりました（v2.1.243）
- Claude Code on the web 向けに GitHub をつないでいない claude.ai 利用者へ `/web-setup` を案内するヒントが加わりました（v2.1.243）
- `/status` に、Claude Code on the web 向けの GitHub 接続の有無を示す行が加わりました（v2.1.243、Pro / Max）。つないでいない場合は `/web-setup` を案内します
- `/tasks` とエージェント詳細ダイアログに、各サブエージェントが動いたモデル（と effort レベル）が出るようになりました（v2.1.243）
- ターン終了時の所要時間の行に、そのターンが終わった時刻が付くようになりました（v2.1.246）。例: `✻ Sautéed for 23s · done 6:05 PM`

**機能改善**

- 権限のページのワイルドカードの解説が全面的に書き直され、`*` の効き方が 3 つの規則と一致表に整理されました（詳細はハイライト 1 参照）— [English](https://code.claude.com/docs/en/permissions#wildcard-patterns)
- Claude が自分から `/code-review` を始められる範囲が広がり、例外リストが削除されました（v2.1.246、詳細はハイライト 3 参照）— [English](https://code.claude.com/docs/en/code-review#let-claude-start-the-review)
- 機能の可用性のページで、Amazon Bedrock・Claude Platform on AWS・Google Cloud の Agent Platform・Microsoft Foundry の 4 タブから `/code-review` の制限行が削除されました（詳細はハイライト 3 参照）— [English](https://code.claude.com/docs/en/feature-availability#summary-by-provider)
- 環境変数のページで、feature flag 取得がオフになる条件に「Claude apps ゲートウェイ経由の接続」と「Amazon Bedrock・Claude Platform on AWS・Google Cloud の Agent Platform・Microsoft Foundry（ホスト側が `CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST` を設定している場合を除く）」が明記されました。あわせて、取得オフでできないことの一覧から `/code-review` の行が削除されています — [English](https://code.claude.com/docs/en/env-vars#features-that-need-feature-flag-fetching)
- 環境変数のページの「インストール／アップグレード後の初回セッション」の節が書き直されました。flag 依存の機能が欠けることに加え、本来なら auto モードで始まるプランでも Manual で始まりうることが明記され、真新しいインストール直後でも `claude -p`・Agent SDK・VS Code 拡張のような非対話セッションは起動モードを決める前に flag を間に合わせられる（対話的なターミナルセッションは間に合わない）ことが加わりました。従来ここに書かれていたクロスセッションメッセージングと `claude import` の 2 例は削除されています — [English](https://code.claude.com/docs/en/env-vars#first-session-after-an-install-or-upgrade)
- 権限モードのページで、起動時のモードを決める表の「feature flag 取得がオフ」と「インストール／アップグレード後の初回セッション」が別々の行に分けられ、後者に「非対話セッションが flag を間に合わせた場合を除く」という条件が付きました。VS Code 拡張が全設定ファイルを無視する条件の記述も、同じ 2 つの場合として書き直されています — [English](https://code.claude.com/docs/en/permission-modes#which-mode-a-session-starts-in)
- サーバー管理設定のページで、Claude apps ゲートウェイ経由でサインインしたクライアントは設定をゲートウェイから取得し、その取得を待ってからセッションを開始することが明記されました。取得に失敗した場合は `forceRemoteSettingsRefresh` を設定していなくても終了します（`claude auth` サブコマンドは従来のフェイルクローズ判定と同様にこの終了からも除外されます）— [English](https://code.claude.com/docs/en/server-managed-settings#enforce-fail-closed-startup)
- サーバー管理設定の適用タイミングの記述が具体化されました。従来「OpenTelemetry 設定のような高度な設定を除き再起動なしで反映」だったのが、「多くは実行中のセッションに再起動なしで反映され、一部は次回起動時にのみ反映される。次回起動組は OpenTelemetry エクスポーター設定・`model` キー・`env` ブロックからの変数の削除」に改められました。管理コンソールで設定を消してエンドポイント側にフォールバックする場合、これらのキーは各クライアントが起動し直すまで効き続ける旨も加わっています — [English](https://code.claude.com/docs/en/server-managed-settings#fetch-and-caching-behavior)
- サーバー管理設定のバイパス表が書き直されました。キャッシュファイルを書き換えた場合に「次回起動時にのみ効くキー」は再取得後も起動し直すまで残ること、キャッシュが無い場合でもデバイス上のエンドポイント管理設定は適用されること、ゲートウェイ経由のクライアントは設定なしで起動時に終了することが加わりました。あわせて `ConfigChange` フックが MDM プロファイルやレジストリポリシーの変更でも走らない旨が明記されています — [English](https://code.claude.com/docs/en/server-managed-settings#security-considerations)
- 管理設定のページで、承認が要る変更の説明に「次回起動を待つ更新は除く」という但し書きが加わり、管理設定でしか設定できないキーの一覧に「Desktop のローカルセッション」が追加されました — [English](https://code.claude.com/docs/en/managed-settings#where-and-when-a-policy-applies)
- デスクトップのページで、SSH セッションを作るときにローカルマシンの管理設定から読むキーに `disableDesktopLocalSessions` が加わりました（詳細はハイライト 4 参照）— [English](https://code.claude.com/docs/en/desktop#local-sessions-on-managed-devices)
- `/goal` のアイドル中の check-in が、1 つのゴールにつきユーザーのプロンプトの間に最大 3 回までになりました（v2.1.246）。3 回目の check-in で「次のプロンプトを送るまで一時停止する」と告げます。v2.1.246 より前は上限がありませんでした。コスト管理のページの「長いセッションで使用量が増える理由」にも同じ上限が加わっています — [English](https://code.claude.com/docs/en/goal#background-work-defers-evaluation)
- ステータスラインが再実行される条件に「`statusLine` 設定の `command` を変えたとき」が加わりました。`command` 自体の変更は 300ms のデバウンスを飛ばして即座に新しいコマンドを走らせます。セットアップ手順の記述も「次に Claude Code とやり取りするまで反映されない」から「ファイルを保存した時点でスクリプトを走らせる」に改まりました — [English](https://code.claude.com/docs/en/statusline#how-status-lines-work)
- ステータスラインの入力フィールドの説明が整理されました。`worktree.*` と `workspace.git_worktree` の対比が「`--worktree` セッションのみ」から「worktree セッションにいる間のみ」に改められ、`cost.total_cost_usd` に「v2.1.211 より前は `/clear` 後も合計が引き継がれていた」という注記が加わりました — [English](https://code.claude.com/docs/en/statusline#available-data)
- ステータスラインの通知の扱いが、レンダリングモードで分けて書かれました。fullscreen レンダリングでは通知が独立した行を持ち、それ以外ではステータスラインと同じ行を共有します — [English](https://code.claude.com/docs/en/statusline#troubleshooting)
- キーバインドの大文字の扱いが変わりました。従来は「単独の大文字は Shift を含意する（`K` は `shift+k`）が、修飾キー付きの大文字は含意しない」でしたが、「キー名は大文字小文字を区別しないので `K` は `k` と同じ、`ctrl+K` は `ctrl+k` と同じ。Shift と文字を組むには `shift+k` と書く」に改められました — [English](https://code.claude.com/docs/en/keybindings#uppercase-letters)
- キーバインドの検証で警告が出る項目に「文字列でも `null` でもないアクション値」が加わり、「ターミナルマルチプレクサの競合」が外れました — [English](https://code.claude.com/docs/en/keybindings#validation)
- 音声入力の `hold space to speak` ヒントが、有効にしてから最初の 3 セッションだけ出るようになりました — [English](https://code.claude.com/docs/en/voice-dictation#enable-voice-dictation)
- 音声入力の録音中の表示が具体化されました。hold モードはウォームアップ中の `keep holding…` に続いて `listening…` になり、録音中はプロンプトのカーソルがマイクレベルに合わせて上下するバーになります（`prefersReducedMotion` を有効にしている場合を除く）。tap モードは `● REC · tap to send` を出します。従来はどちらも「波形が出る」という記述でした — [English](https://code.claude.com/docs/en/voice-dictation#hold-to-record)
- 音声入力が繰り返し失敗して一時停止する条件が「10 秒以内に 3 回の取り込み失敗。最初の失敗から 10 秒経つまで一時停止」と具体化されました。Linux で SoX が見つからないときのメッセージも `No audio recording tool found` から `Voice mode requires SoX for audio recording` に改称されています — [English](https://code.claude.com/docs/en/voice-dictation#troubleshooting)
- `/terminal-setup` が書き込むのは Shift+Enter のキーバインドのみであることが明記され（従来は「Shift+Enter とその他のキーバインド」）、GPU アクセラレーションの変更が v2.1.157 以降であることが加わりました — [English](https://code.claude.com/docs/en/terminal-config#enter-multiline-prompts)
- カスタムテーマの色トークンで、メッセージ背景の適用範囲が書き直されました。`userMessageBackground`・`bashMessageBackgroundColor`・`memoryBackgroundColor` は既定と fullscreen の両レンダラーで塗られ、`userMessageBackgroundHover` と `selectionBg` だけが fullscreen 専用です。従来はこのグループ全体が fullscreen 専用と書かれていました — [English](https://code.claude.com/docs/en/terminal-config#create-a-custom-theme)
- コマンドリファレンスで、`/cd` のパス候補表示に v2.1.206 以降が必要であること、`/clear` した会話を rewind メニューから戻す導線に v2.1.191 以降が必要であることが加わりました — [English](https://code.claude.com/docs/en/commands#all-commands)
- コマンドリファレンスで、`/skills` の可視性切り替えの説明から「`Enter` で保存」が外れ、`Space` で切り替えるだけになりました。bundled skill の説明からも「Claude が関連するときに自動で呼び出せる」が削除されています — [English](https://code.claude.com/docs/en/commands#all-commands)
- コマンドメニューの絞り込みの説明に、ハイライト規則が v2.1.236 以降であることと、v2.1.236 より前は `Enter` で最も近い候補が実行されていたことが加わりました — [English](https://code.claude.com/docs/en/commands#how-the-command-menu-matches-what-you-type)
- OpenTelemetry のプラグインイベントで、`plugin.scope` に `"community"` が、`enabled_via` に `"admin-install"` が加わりました。`"admin-install"` は組織の **Organization settings > Plugins** で必須または自動インストールに設定されたプラグインを指し、v2.1.246 より前は `"user-install"` または `"seed-mount"` として報告されていました。claude.ai から同期されたプラグインの `plugin_id_hash` の計算方法（claude.ai が報告するマーケットプレイス名、無ければ `synced` と組み合わせる）も明記され、MCP サーバー接続イベントとフックイベントの `plugin_id_hash` の説明はこの節への参照になりました — [English](https://code.claude.com/docs/en/monitoring-usage#plugin-loaded-event)
- Amazon Bedrock で `awsAuthRefresh` コマンドを走らせる前に、STS の `GetCallerIdentity` で本当に資格情報が切れているかを確認し、まだ使えるならコマンドを飛ばすようになりました。この確認はプロキシ設定（`HTTPS_PROXY` / `NO_PROXY`）を経由します。v2.1.239 より前は直接送っていたため、プロキシ経由の egress しか許さないネットワークで起動時にハングしていました — [English](https://code.claude.com/docs/en/amazon-bedrock#advanced-credential-configuration)
- fast モードが VS Code 拡張でも使えるようになりました。従来「VS Code 拡張では非対応」と書かれていた箇所が、`fastMode` 設定に追従し、選んだモデルが fast モードに対応していれば **Toggle fast mode** コマンドが出る、という記述に置き換わりました。非対話モードでの通知が v2.1.221 以降であることも加わっています — [English](https://code.claude.com/docs/en/fast-mode#toggle-fast-mode)
- 概要のページのデスクトップアプリの説明に、アプリには Claude Code が同梱されるので CLI を別途入れる必要がない旨が加わりました — [English](https://code.claude.com/docs/en/overview#get-started)
- アーティファクトのページで、インストール／アップグレード後の初回セッションについての記述が「コメントを読めません」から「読めないことがあります」に緩められました — [English](https://code.claude.com/docs/en/artifacts#collect-comments-on-an-artifact)
- Linux デスクトップ版の要件に、Debian 系でないディストリビューションでは CLI を使うこと、Windows の WSL 2 では Windows 版デスクトップアプリを使うことが加わりました。apt リポジトリの鍵の取得手順と `E: Unable to locate package claude-desktop` の切り分けにも 1 項目ずつ追記されています（詳細はハイライト 5 参照）— [English](https://code.claude.com/docs/en/desktop-linux#requirements)
- `/cd` が改善され、移動先ディレクトリのプロジェクト設定・フック・`.mcp.json` サーバー（通常の承認プロンプトを経ます）・スキル・エージェントが、`--resume` を待たず移動直後に効くようになりました（v2.1.246）
- bash シェルでの Bash ツールのレイテンシが改善されました。関数ごとに base64 のサブシェルを起動せずスナップショット関数を再生します（v2.1.246）
- サブエージェントが `maxTurns` の上限で止まったとき、完了したように見せるのではなく、出力を「途中まで」と印を付けて返し、`SendMessage` で続けられるというヒントを添えるようになりました（v2.1.246）
- 非対話セッション（`-p`・SDK・クラウドセッション）で、サーバーエラー・接続断・停滞によって途中で切れた応答を、エラーで終わらせずに自動で続けるようになりました（v2.1.246）
- 使用量テレメトリの組織への帰属が改善されました（v2.1.246）。ワークロード ID フェデレーションのセッション、起動時に `apiKeyHelper` が走っている間に送られるイベント、アイドル中にログイントークンが切れた後が対象です
- `claude install` と `claude update` が、保留中の管理設定の同意プロンプトをコマンドの途中で出さず、次の対話セッションに送るようになりました（v2.1.246）
- claude.ai から同期されたプラグインの OpenTelemetry イベントで、`plugin_id_hash` が実際のマーケットプレイスを反映し、管理者がインストールしたプラグインの `enabled_via` が `admin-install` になりました（v2.1.246）
- 起動時間が改善されました（v2.1.243）。サンドボックスと MCP の立ち上げが最初のフレームを待たせなくなり、素の起動はサブコマンド登録を飛ばし、ワークフローの探索・設定・トラストストアの処理が軽くなりました
- ネイティブインストールと自動更新のダウンロードサイズが改善されました（v2.1.243）。バイナリが zstd 圧縮になり、Linux x64 で 340 MB から約 75 MB になりました
- `ANTHROPIC_AUTH_TOKEN` で Anthropic API に直接認証するセッションについて、使用量テレメトリの組織への帰属が改善され、その組織のデータ取り扱い設定が適用されるようになりました（v2.1.243）
- ネイティブバイナリのサイズが約 2 MB 小さくなりました（v2.1.243）。同梱のスキルとプロンプトのテキストをより詰めて格納しています
- ネイティブビルドのメモリ使用量が改善されました（v2.1.243）。バンドル全体を常駐させず必要に応じて読み込む方式になり、セッションあたり約 40〜70 MB 減ります
- 長時間セッションのピークメモリ使用量が改善されました（v2.1.243）。ヒープが大きくなるほど早めにガベージコレクトします
- SSH 越しの `/login` が改善されました（v2.1.243）。サインイン URL がすぐ出るようになり、`c` を押すと常に成功と言う代わりにどうコピーしたかを報告し、fullscreen でのテキスト選択方法のヒントが出ます
- 思考をオフにした状態で effort `xhigh` / `max` を使ったときのエラーが改善され、レベル名・思考を無効にしている設定・`/effort high` という直し方を挙げるようになりました（v2.1.243）
- `/loop` で、Claude にやることが無い連続した wake-up が、1 件ずつ表示される代わりにターミナル上で 1 行にまとまるようになりました（v2.1.243）
- \[VSCode] 長いセッションの履歴の切り詰めが改善され、古いツール操作の行から先に落とすことで自分のメッセージと Claude の返答が残るようになりました（v2.1.243）
- \[VSCode] Claude アカウントでサインインしているとき、拡張機能自身の使用量テレメトリの組織への帰属が改善され、その組織のデータ取り扱い設定が適用されるようになりました（v2.1.243）
- サンドボックス化された Bash ツールのプロンプトが、許可されたネットワークホストを列挙しなくなりました（v2.1.243）。Claude が「一覧に無いホストはブロックされる」と決めつけず、リクエストを試みる（そしてユーザーが新しいホストを承認できる）ようにするためです
- `/model` ピッカーと同梱の `claude-api` スキルで、Sonnet 5 の $2/$10 per Mtok が期間限定のプロモーションではなく標準の定価として表示されるようになりました（v2.1.243）
- macOS の computer use で、デスクトップ・Dock・Finder ウィンドウをクリックするには、他のアプリと同様にアクセスダイアログで Finder を許可することが必要になりました（v2.1.243）
- `/model`・`/fast`・`/effort` が、Bedrock・Vertex・Foundry とテレメトリを切った環境でも、ターンの終わりまでキューされずに即座に実行されるようになりました（v2.1.243）
- クロスセッションメッセージングの受信ソケットが、30 秒以内に 1 行も完結して送ってこない接続を閉じるようになりました（v2.1.243）。投稿するスクリプトはデータが揃ってから接続してください
- Remote Control を別のターミナルが握っている会話を再開したときの案内が改善され、他のマシンのセッションはこちらからは見えず、こちらにも届かないことを説明するようになりました（v2.1.243）

**バグ修正**

- ターミナルをリサイズしてから一番下へ飛んだとき、次のキー入力まで fullscreen モードのトランスクリプトが空白のままになる問題を修正（v2.1.246）
- 差分に非常に長い 1 行（base64 文字列など）が含まれるとトランスクリプトが極端に遅くなる問題を修正。そうした行は印付きで切り詰めて表示されます（v2.1.246）
- 前のメッセージの位置にいるときの fullscreen のスクロールが不安定になり、一番下へ飛ぶ操作がトランスクリプトの途中で止まることがある問題を修正（v2.1.246）
- Claude Code の起動ディレクトリが消えていた・マシンがスリープしていた・ホストのプロセス起動が遅い場合に、バックグラウンドセッションが 45 秒後に開けなくなる問題を修正（v2.1.246）
- 別の Claude Code プロセスが npm パッケージを再インストールしている最中に、バックグラウンドセッションが `Couldn't start the background service … EACCES` で開けない問題を修正（v2.1.246）
- 先頭 500 文字に markdown が無いとメッセージ全体で markdown の描画が無効になる問題と、`+` / `N)` のリストおよび setext 見出しが描画されない問題を修正（v2.1.246）
- ヘッドレス／リモートのセッションで、届いたメッセージに割り込まれた MCP ツール呼び出しが、明示的な中断エラーではなく「出力なしで完了」としてモデルに報告される問題を修正（v2.1.246）
- パラメータのスキーマが空（`{}`）のとき、MCP ツールの引数が本来の型ではなく JSON 文字列として送られる問題を修正（v2.1.246）
- 実行中に中断されたコマンドが、切られた形跡なく「Ran 1 shell command」と表示される問題を修正（v2.1.246）
- ダイナミックワークフローの実行中に ← を押す／`/background` を実行すると、終わったサブエージェントが再起動される問題を修正。先に確認を求め、何体が再起動されるかを伝えます（v2.1.246）
- ワーカーの起動中（Windows でよく起きます）に `claude agents` で開始直後のセッションを開くと、`was stopped while the respawn was in flight` で止まる問題を修正（v2.1.246）
- `claude agents` が、バックグラウンドに回した名前付きセッションを二重に表示する問題を修正。同じ会話を再びバックグラウンドに回すと新しい行に番号が付きます（例: `my-session (2)`）（v2.1.246）
- バックグラウンドの保持期間の掃除が、古いバックグラウンドセッションの記録が指していたために `.claude/worktrees/` 配下の自分で作った git worktree を消してしまう問題を修正（v2.1.246）
- 非常に大きなセッションで auto モードのツール呼び出しが「一時的に利用できない」として拒否される問題を、安全チェックの締め切りをプロンプトのサイズに応じて伸ばすことで修正（v2.1.246）
- プラグインキャッシュが同じプラグインに対して SHA 名のディレクトリを重複して作る問題を修正（v2.1.246）
- frontmatter の `name` に既に `<plugin>:` プレフィックスが入っているプラグインスキルが、スラッシュメニューで二重に表示される問題を修正（例: `/plugin:plugin:skill`）（v2.1.246）
- インストール済みプラグインを素の名前で指定すると `claude plugin update` が失敗する（完全修飾名でしか動かない）問題を修正（v2.1.246）
- `plugin.json` が UTF-8 の BOM 付きで保存されているとプラグインのインストールが失敗する問題を修正（v2.1.246）
- `skills/*/SKILL.md` の形でスキルを定義するプラグインについて、`/reload-plugins` がスキル 0 件と報告する問題を修正（v2.1.246）
- フックのエラーメッセージが、解決済みのプラグインパスではなくリテラルの `${CLAUDE_PLUGIN_ROOT}` を表示する問題を修正（v2.1.246）
- `/rename` がテーマのプロンプト枠線の色（カスタムテーマの `promptBorder` を含む）を既定のシアンに置き換える問題を修正。`/color` で選ばない限りテーマの色を保ちます（v2.1.246）
- カスタムテーマの差分の色（`diffAdded` / `diffRemoved` とその薄い版）が、差分表示と `/theme` のプレビューで無視される問題を修正（v2.1.246）
- `keybindings.json` に未知のアクション名を書くとそのキーが黙って死ぬ問題を修正。そのバインドを飛ばして既定のバインドが効き続け、`--debug` で警告がログに出ます（v2.1.246）
- UTC より東のタイムゾーンで、`/stats` の活動ヒートマップが 1 セットずつずれる（日曜の件数が月曜の下に出る）問題を修正（v2.1.246）
- 既に fork した／バックグラウンドに回したセッションから `/fork` すると、新しいセッションが空の会話で始まる問題を修正（v2.1.246）
- `/--` で始まるプロンプト（Lean のドキュメントコメントなど）が、Claude に送られず未知のスラッシュコマンドとして弾かれる問題を修正（v2.1.246）
- 打ち込んだ文字列が実在のパスに一致しなくなっても `@` のファイルピッカーが開いたままになる問題を修正（v2.1.246）
- エージェントビューに移動して戻ると、ステータスラインのコストと所要時間がゼロにリセットされる問題を修正（v2.1.246）
- ターミナルウィンドウを前面に戻すためにクリックしただけで、fullscreen モードがポインタの下のコントロールにキーボードフォーカスを移す問題を修正（v2.1.246）
- 補完対象のトークンまたは作業ディレクトリにヌルバイトが含まれるとパス補完が失敗する問題を修正（v2.1.246）
- Windows / macOS: 異常終了したセッションが `~/.claude/sessions` に残した古いエントリを、ヘッドレスセッションが掃除しない問題を修正（v2.1.246）
- Anthropic 互換のサードパーティエンドポイント（`ANTHROPIC_BASE_URL`）が `id` の無い `tool_use` ブロックをストリーミングしたとき、最初のツール呼び出しで UI が描画エラーで止まる問題を修正（v2.1.246）
- 非常に大きな既存ファイルを上書きした後、書き込みは終わっているのに Write ツールが「Out of memory」と報告する／長時間フリーズする問題を修正（v2.1.246）
- `~/.claude/plugins/known_marketplaces.json` が空または壊れているときに、`claude plugin install <name>` がエラーを報告せず黙って終了する（ターミナルではハングする）問題を修正（v2.1.246）
- 保存された履歴に Anthropic API が受け付けないツールブロック（多くはサードパーティの API プロキシが書いたもの）が含まれると、再開したセッションが毎ターン 400 で失敗する問題を修正（v2.1.246）
- サーバー管理設定を使う一部の Team / Enterprise 利用者で、`curl -fsSL https://claude.ai/install.sh | bash` が `Raw mode is not supported` で失敗する問題を修正（v2.1.246）
- 権限モードを指定していない場合に、plan モードで終わったセッションが VS Code 拡張と、権限プロンプトツールを使う `claude -p --continue` / `--resume` で plan モードの外で再開する問題を修正（v2.1.246）
- サンドボックスの「Network request outside of sandbox」の権限プロンプトが待機している間、`Notification` フックが発火しない問題を修正（v2.1.246）
- 末尾に `&&` や `||` が残った不正なコマンドについて、Bash の権限チェックが必ず承認を求めるよう修正（v2.1.246）
- `--strict-mcp-config` のセッションが、読み込むことのない `.mcp.json` のサーバーの承認を求め、バックグラウンドセッションを起動時に待たせる問題を修正（v2.1.246）
- Anthropic 宛てのテレメトリ・メトリクスのリクエストが、サードパーティのゲートウェイ（`ANTHROPIC_BASE_URL`）向けに設定した API キーを運ぶ問題を修正。資格情報はその持ち主のホストにしか送られません（v2.1.246）
- `apiKeyHelper` が短命の JWT を返す構成で、アイドル後の最初のプロンプトで API エラーが見える問題を修正。期限切れのキャッシュトークンは送信前に更新され、401 / 403 の認証エラーは静かにリトライされます（v2.1.246）
- fullscreen と Ctrl+O のトランスクリプト表示で、セッションが長くなるほどメモリが増える問題を修正。描画される各メッセージ行がトランスクリプト全体のツール検索表のコピーを抱えなくなりました（v2.1.246）
- 1 つのリポジトリから（複数の worktree などで）同時に起動した `/ultrareview` の実行とクラウドセッションが、別の起動の未コミット変更を持って始まることがある問題を修正（v2.1.246）
- `/autofix-pr` のようなバックグラウンドのクラウドセッションに表示されるタスク進捗の件数（`3/5` など）が、タスクを 1 つ取りこぼすことがある問題を修正（v2.1.246）
- Remote Control のセッションが、claude.ai と Claude アプリで 2 通目のプロンプトまで仮の名前のままになる問題を修正。自動生成のタイトルが最初のプロンプトの後に出ます（v2.1.246）
- `requiresUserInteraction` が付いた MCP ツールの権限プロンプトが「Yes, and don't ask again」を出す問題を修正。その選択肢はツールが無視する allow ルールを書いていました（v2.1.246）
- 作業のポーリングへの応答が壊れている（間に入ったプロキシの HTML ページなど）ときに、セルフホストのランナーが実行中のセッションを終わらせる／自分が終了する問題を修正。ポーリングをリトライします（v2.1.246）
- コマンドサンドボックスのファイルシステム設定が `--setting-sources` を尊重しない問題を修正（v2.1.246）
- glibc 2.44 を採用した Linux ディストリビューション（Arch Linux・CachyOS・Fedora Rawhide など）での起動時クラッシュを修正（v2.1.245）
- 非対話（`-p`）と SDK のセッションで、接続が切れたリモート MCP サーバーが二度と復帰しない問題を修正。自動で再接続するか、失敗として報告します（v2.1.243）
- クライアント ID メタデータドキュメントに対応したサーバー（Linear など）で、デスクトップアプリから始めた MCP サーバーのサインインが `Invalid redirect URI` で失敗する問題を修正（v2.1.243）
- サーバー側の一時的な無効化がキャッシュされ、その後の flag 取得が失敗したときに、auto モードが起動時に使えないままになる問題を修正（v2.1.243）
- API が一時的に過負荷でクライアントにリトライを求めたとき、約 1 分待った後に auto モードのツール呼び出しが「一時的に利用できない」として拒否される問題を修正（v2.1.243）
- `/model` ピッカーが Ultracode の選択を黙って無視する問題を修正。選ぶと現在のセッションに適用されます（v2.1.243）
- `/resume` が直近 50 セッションしか列挙しない問題を修正。スクロールに応じて追加で読み込みます（v2.1.243）
- ターンの途中で再起動したクラウドセッションが、保留中のフックやバックグラウンドタスクの通知を通常の継続メッセージの代わりにプロンプトとして再送する問題を修正（v2.1.243）
- 2.1.232 のソケットディレクトリの強化以降、ユーザー名前空間と rootless コンテナの中でクロスセッションメッセージングが黙って無効になる問題を修正（v2.1.243）
- 画面の他の部分が再描画されると、コンテナの外にはみ出すテキスト（`/login` のサインイン URL など）の先頭の桁が失われる問題を修正（v2.1.243）
- 絵文字の直後に打った綴り間違いの単語に `spellcheck` の下線が引かれない問題を修正（v2.1.243）
- 最後のバックグラウンド Bash タスクが終わったときに、バックグラウンドのサブエージェントが起きない問題を修正（v2.1.243）
- Anthropic API が応答を始めないままセッションが 10 分以上沈黙する問題を修正。リクエストは約 3 分でタイムアウトし、1 回リトライしてから `API Error: No response from API` を表示します（v2.1.243）
- 認証・モデルの可用性などクライアント側で生成されるエラーメッセージが、エラー行ではなくモデルの出力のように描画される問題を修正（v2.1.243）
- CI でのワークロード ID フェデレーションを修正。1 つのジョブ内のプロセスは使い捨てトークンを交換し直さず共有し、交換が拒否された場合はサーバーのメッセージを添えて即座に失敗します（v2.1.243）
- サインインから始まったセッション（`/logout` 後の最初の起動など）で、サーバー管理の `companyAnnouncements` が起動時に表示されない問題を修正（v2.1.243）
- コマンドに `$()` やバッククォートのコマンド置換とその後の引数が含まれるとき、`Bash(cat *)` のようなフックの `if` 条件が無関係な Bash コマンドで発火する問題を修正（v2.1.243）
- 両方のプラグインを `--plugin-dir` で一緒に読み込んだとき、`marketplace` フィールドで宣言したプラグイン依存が解決されない問題を修正（v2.1.243）
- 最後の LSP プラグインを無効にしても `/reload-plugins` が LSP ツールを残す問題を修正。会話を読み直すことになる LSP プラグインの変更の前に警告も出ます（v2.1.243）
- `--agents` が不正な JSON や不正なエージェント定義を黙って無視する問題を修正。`--mcp-config` と同様に明確なエラーで終了します（v2.1.243）
- `~/.claude.json` に不正な MCP サーバーのエントリがあるとき、`/status` がファイル名なしで「Found invalid entries in: .」と表示する問題を修正（v2.1.243）
- `/clear` が、新しいセッションには引き継がれている `/rename` のセッション名をプロンプトバーから消す問題を修正（v2.1.243）
- `~/.claude/history.jsonl` に不正なエントリがあると、Ctrl+R の履歴検索と ↑ キーの履歴が壊れる問題を修正（v2.1.243）
- 修飾キー付きのキーをエンコードするターミナル（modifyOtherKeys / kitty プロトコル）で、Ctrl+\[ が vim の INSERT モードを抜けない問題を修正（v2.1.243）
- `NO_PROXY` に `localhost` が入っていて小文字の `no_proxy` には入っていないとき、ローカルの IDE 接続が `HTTPS_PROXY` を経由してしまう（そして失敗することがある）問題を修正。両方の大文字小文字を尊重します（v2.1.243）
- ブロックされたコマンドが 0 で終了した場合（`curl` がプロキシの 403 ページを出力したときなど）に、サンドボックスのネットワーク違反の詳細が Bash ツールの結果から落ちる問題を修正（v2.1.243）
- セッションがアイドルの間にレート制限のウィンドウがリセットされた後も、ステータスラインの `rate_limits` フィールドと `/usage` がリセット前の使用率を表示し続ける問題を修正（v2.1.243）
- `claude --teleport <session>` が、未コミットの変更があるときにセッションピッカーのように stash を提案せず終了する問題を修正（v2.1.243）
- `gh auth token` を持たない古い GitHub CLI で既に認証済みのとき、`/web-setup` が何度もログインを求める問題を修正（v2.1.243）
- 自動更新がセットアップ時のバージョンを片付けた後、Chrome の Claude が Claude Code との接続を失う問題を修正。ネイティブホストは安定した `claude` ランチャー経由で起動します（v2.1.243）
- \[VSCode] feature flag が最初に取得される前に始めたセッション（インストール直後など）が、auto モードや設定した既定モードではなく既定の権限モードで開く問題を修正（v2.1.243）
- \[VSCode] 展開した Focus view のセクションが、サブエージェントのツール操作中に勝手に畳まれる問題を修正（v2.1.243）
- `claude remote-control` が、サーバーがセッションの途中で環境を落としたときに終了し、つないでいた Remote Control セッションを取り残す問題を修正。復帰するようになりました（v2.1.243）
- 管理者・オーナーのロールを持たない Team / Enterprise のメンバーで、`claude remote-control` が提供する Remote Control セッションが、停止・再起動の後に固まることがある問題を修正（v2.1.243）

**その他**

- クイックスタートと概要のページで、コードブロックの言語指定の後に `theme={null}` が 34〜37 回繰り返されるようになりました。クイックスタートは 5 か所で 37 回、概要は 5 か所で 34 回で、いずれも従来は 1 回でした。上流の生成の不具合とみられ、この 2 ページの差分行（各 12 行）は、この 5 行と本文 1 文の変更だけで占められています
- クイックスタートで、初回セッション後に auto モードが既定になるプランの説明から「and VS Code」が外れ、「対話的なターミナルセッション」だけになりました。一方で権限モードのページの表は VS Code 拡張を `auto` の行に残しているため、2 ページの記述が食い違っています
- `llms.txt` のカテゴリ見出しには重複があり、`Platforms and integrations` が 3 回、`Core concepts` と `Deployment` が 2 回ずつ現れます。カテゴリ別に読む場合は見出し名だけでは一意に定まりません
- ステータスラインのセットアップ手順で、`workspace.git_worktree` の説明の対比先が `worktree.*` のままリンクの張り先だけ worktree のページに変わるなど、リンクの張り替えが数か所含まれています
- コマンドリファレンスで、`/bug` や `/claude-api` など複数のエントリで表の桁揃えが変わっており、差分行数を膨らませています
- 管理設定・サーバー管理設定・auto モードの設定の 3 ページでも、表の区切り行の桁揃えの入れ替えが差分に含まれます。空白を無視して数え直すと、サーバー管理設定は 38 行から 24 行、権限モードは 21 行から 7 行、`/goal` は 12 行から 6 行になります

## 新着情報

（今回の対象期間に新着情報ページの追加・更新はありません。Week 34（2026年08月17日～21日）が最新のままです）

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-08-24.md](./archives/latest/2026-08-24.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-08-24.md](./archives/latest-detail/2026-08-24.md)

<!--
base_commit: 961fa881bd3d4366c49a34b34508be3172b7c2fc
head_commit: 9183e5fb58ed21ba3079f4e0f6a528c4e46d1ea7
generated_at_full: 2026-08-26T15:19:34+09:00
-->
