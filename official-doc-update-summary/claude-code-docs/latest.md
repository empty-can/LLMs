---
対象期間: 2026年09月10日 〜 2026年09月11日
作成日: 2026-09-11
---

# Claude Code 公式ドキュメント更新サマリ

```markdown
前回が「持ち越し 40 件が一斉に本文として届いた回」だったのに対し、今回は**その逆 ―― 本文が届いた分と引き換えに、新しい持ち越しを 61 件積んだ回**です。差分は 3 ファイル・1,070 行、本文が変わったページは 53 / 191 で、前回（85 / 191・2,929 行）の約 3 分の 1 に落ち着きました。`llms-full.txt` は 95,128 行から 95,413 行へ 285 行増えています。**前回の持ち越し 6 件は 1 件残らず本文として着地**し、代わりに**見出しマップへ新設された 61 見出しは全件が本文未着**です。中心にあるのは v2.1.268 の**「Bedrock・Agent Platform・Foundry を first-party セッションと同じ扱いにする」**という一本の変更で、前回・前々回のサマリで報告した「プロバイダーによって挙動が分かれる」という記述がまとめて畳まれました。`whats-new/` は 9 回連続で差分がありません。

主要なものを以下に挙げます。

1. クラウド 3 プロバイダーが first-party セッションと同じ扱いになり、前回報告した分岐が消えた
2. タスク追跡ツールの既定が「拒否リスト」から「許可リスト」へ反転し、未知のモデル ID も対象外になった
3. `claude plugin eval` の新設ページが宣言だけ先に届き、今回唯一の新規ページになった
4. Claude apps gateway の持ち越し 3 節が到着し、今回最大のページ更新になった
5. v2.1.268 は 96 項目の大型リリースで、権限と秘匿情報まわりの修正が目立った
```

## ハイライト

1. [**クラウド 3 プロバイダーが first-party セッションと同じ扱いになった**](./latest-detail.md#1-クラウド-3-プロバイダーが-first-party-セッションと同じ扱いになった):  
  **v2.1.268 で、Amazon Bedrock・Google Cloud の Agent Platform・Microsoft Foundry のセッションが first-party セッションと同じ振る舞いをするようになりました**。システムプロンプトの「記録」がこれらのプロバイダーでも効くようになり（**前回「効かない」と報告した箇所です**）、環境・モデル・設定の情報はシステムプロンプトではなく**添付として届く**ようになり、ツール一覧も会話を通じてバイト単位で安定します。波及として、**前回「フラグを取得しないセッションでは全損」と書いた出力スタイルの切り替えが、今回は無条件でキャッシュを保つ側へ移りました** ―― プロンプトキャッシングのページでは節そのものが「無効にするアクション」から「保持するアクション」へ物理的に移動し、プロバイダー別の例外段落が削除されています。ただし**ベアモード（`--bare` / `CLAUDE_CODE_SIMPLE=1`）は依然として記録の対象外**です。
2. [**タスク追跡ツールの既定が拒否リストから許可リストへ反転した**](./latest-detail.md#2-タスク追跡ツールの既定が拒否リストから許可リストへ反転した):  
  これまでの記述は「**Opus 4.8・Sonnet 5・Fable 5・Mythos 5 とその後継では既定で提供しない**」という**拒否リスト**でした。今回それが「**Claude 3.x・Opus 4〜4.7・Sonnet 4〜4.6・Haiku 4.5 でのみ既定で提供する**」という**許可リスト**に反転しています（v2.1.268）。**実質的な変化は、リストに載っていないモデルすべてが既定で対象外になったこと**で、原文は **「Claude Code が認識しないモデル ID ―― LLM ゲートウェイ越しのカスタムモデル名など ―― にも同じことが当てはまる」**と明記しました。`TaskCreate` / `TaskGet` / `TaskUpdate` / `TaskList` / `TodoWrite` の 5 つが対象で、同じ書き換えが**ツールリファレンス・インタラクティブモード・環境変数・Agent SDK の 3 ページ**の計 6 ページに及んでいます。
3. [**`claude plugin eval` の新設ページが宣言だけ先に届いた**](./latest-detail.md#3-claude-plugin-eval-の新設ページが宣言だけ先に届いた):  
  `llms.txt` に **`plugin-evals`（Test plugins with evals）が 1 件追加**され、見出しマップには**このページだけで 50 見出し**が現れました。プラグインを eval ケースの集合に対して走らせ、グレーダーで採点し、**プラグインを読み込まない「ベースライン」と比較して差分（Δ）を出し、CI でスコアをゲートする**ためのハーネスです。**ただし `llms-full.txt` には本文が 1 行も届いていません**。公開サイトを直接確認したところ、**英語版・日本語版ともすでに公開されており、要件として「Claude Code v2.1.269 以降」**が挙げられていました ―― **changelog の最新エントリ（v2.1.268）より 1 つ先の版**です。
4. [**Claude apps gateway の持ち越し 3 節が到着した**](./latest-detail.md#4-claude-apps-gateway-の持ち越し-3-節が到着した):  
  前回「本文未着」と報告した Claude apps gateway 設定リファレンスの 3 節が、**すべて本文として到着しました** ―― `Send the rates to signed-in clients`・`Export directly to your collector`・`When a destination fails` です。**実質 101 行（追加 81・削除 20）で今回最大のページ更新**になりました。`pricing` に書いた契約レートが **`modelPricing` 管理設定としてクライアントへ配られる**ようになり（v2.1.268）、ポリシーで**コレクターを名指しすればリレーを迂回して直接エクスポートできる**ようになり（クライアント側 v2.1.265 以降）、**宛先が 5 回連続で失敗すると 30 秒刻みで転送を止める**バックオフが明文化されました。あわせて `forward_user_identity` を立てたアップストリームでは**開発者のメールを載せたリクエストへの `429` がフェイルオーバーしなくなる**（ゲートウェイ側 v2.1.267）ことも書かれています。
5. [**v2.1.268 は 96 項目で、権限と秘匿情報まわりの修正が目立つ**](./latest-detail.md#5-v21268-は-96-項目で権限と秘匿情報まわりの修正が目立つ):  
  changelog に **99 行が追加され、すべてが v2.1.268（2026年09月10日）の 96 項目**です。前回の v2.1.267（53 項目）から**ほぼ倍増**しました。内訳は接頭辞なしが 63 件（Fixed 38・Improved 11・Added 7・Changed 7）、接頭辞つきが 33 件。**最も注意を要するのは `ANTHROPIC_BASE_URL` を使う構成で v2.1.265 以降すべてのターンが HTTP 400 で失敗していた回帰の修正**で、原因は Artifact ツールの入力スキーマに入った正規表現でした。**権限と秘匿情報の漏れを塞ぐ 4 件のまとまり**（シンボリックリンク先に書いた拒否ルール、`env -C` / `eval` を挟んだ迂回、git ソース URL 中のトークン露出、`${VAR}` から解決したシークレットの露出）が、このリリースの性格をよく表しています。

## 新規追加されたページ

- [**evals でプラグインをテストする**](./latest-detail.md#1-evals-でプラグインをテストする) ([日本語](https://code.claude.com/docs/ja/plugin-evals#requirements) / [English](https://code.claude.com/docs/en/plugin-evals#requirements)):  
  `claude plugin eval` によるプラグインの eval ハーネス。`llms.txt` と見出しマップには届いたが、**`llms-full.txt` には本文が未着**。内容はハイライト 3 で詳述。

## 大幅に更新されたページ

- [**Claude apps gateway 設定**](./latest-detail.md#1-claude-apps-gateway-設定) ([English](https://code.claude.com/docs/en/claude-apps-gateway-config#send-the-rates-to-signed-in-clients)):  
  前回の持ち越し 3 節（`pricing` のクライアント配信・コレクターへの直接エクスポート・宛先失敗時のバックオフ）がすべて到着し、**実質 101 行（追加 81・削除 20）で今回最大**。内容はハイライト 4 で詳述。
- [**フック**](./latest-detail.md#2-フック) ([English](https://code.claude.com/docs/en/hooks#worktreeremove)):  
  `WorktreeRemove` が終了コードで削除を止められるようになり、`mcp_tool` フックが `SessionStart` / `Setup` でいつ走るかが書き下ろされた（実質 92 行）。拒否理由・`stopReason`・`Write` の出力形の記述も変わった。

## 軽微な更新

今回の差分は **3 ファイル・1,070 行**（追加 710・削除 360）です。内訳は `llms-full.txt` が 981 行（追加 633・削除 348）、ページ見出しマップ（`en/claude_code_docs_map.md`）が 66 行（追加 65・削除 1）、`llms.txt` が 23 行（追加 12・削除 11）。`llms-full.txt` の総行数は **95,128 行から 95,413 行へ 285 行増え**、展開ページ数は 191 のままです。

本文が変わったページは **53 / 191** で、前回の 85 ページ・2,929 行と比べると約 3 分の 1 の規模です。**今回は 53 ページすべてに桁揃え以外の実質的な変更があり、「表の再描画だけ」のページはありません**（前回はコマンド一覧ページが実質 0 行でした）。ただし**生の差分と実質の差が大きいページはいくつかあり**、CLI リファレンスは生 76 行に対して実質 6 行、プラグインリファレンスは生 55 行に対して実質 15 行、エージェントビューは生 35 行に対して実質 7 行です。

**前回の持ち越し 6 件は、1 件残らず本文として着地しました** ―― エラーリファレンス 2 件（`The source file is not valid UTF-8 text` / `Working directory no longer exists when starting a background session`）、Claude apps gateway 設定リファレンス 3 件（ハイライト 4）、プロンプトキャッシング 1 件（`Resuming a session`・ハイライト 1）です。前回「本文には残っているが見出しマップからだけ消えた」と書いた**分析ページの `Tagging criteria` も、今回は本文から削除されました**（見出しマップ・本文の双方に無くなり、決着しています）。

**一方、新しい持ち越しは 61 件で、前回の 6 件から 10 倍に増えました。** **見出しマップに追加された 61 見出しは、1 件も本文が届いていません**（`llms-full.txt` を実際に検索して全件確認しました）。内訳は **`plugin-evals` の新設ページが 50 件**（ハイライト 3）、残る 11 件が既存 9 ページへの追加です。

| ページ | 本文未着の見出し |
|---|---|
| プラグインリファレンス | `plugin eval` / `plugin eval init` |
| エラーリファレンス | `You've hit your monthly spend limit` / `plugin eval is currently in early access` |
| VS Code 拡張 | `Share a plugin install link` |
| Web クイックスタート | `` Remove the `/web-setup` token `` |
| トラブルシューティング | `Copied text doesn't reach your local clipboard over SSH` |
| 使用状況の監視 | `Repository attributes`（`Standard attributes` 配下） |
| すべての設定 | `` `copyOnSelect` ``（`Global config settings` 配下） |
| チェックポイント | `Messages sent mid-turn not checkpointed` |
| TypeScript SDK リファレンス | `` What `readFile()` can read ``（`SDKControlReadFileResponse` 配下） |

**changelog に載ったのは v2.1.268 の 1 リリース**（原文の日付表記は 2026年09月10日）だけです。下記の分類では **changelog 由来の項目に版を併記せず**、単一リリースなのでこの導入文で 1 度述べるに留めます。**changelog にしか記述がない項目には参考リンクを付けていません**（本サマリは changelog ページの URL を参考リンクに使わない方針です）。

**新機能**

- **`plugin-evals` ページが新設されました**。`claude plugin eval` でプラグインを eval ケースの集合に対して走らせ、グレーダーで採点し、**プラグインなしのベースラインと比較して CI でスコアをゲートする**ためのハーネスです（詳細はハイライト 3 参照） — [日本語](https://code.claude.com/docs/ja/plugin-evals#requirements) / [English](https://code.claude.com/docs/en/plugin-evals#requirements)
- **`claude rm` に `--force-remove-worktree <worktree-id>` が追加されました**。git や `WorktreeRemove` フックが削除できなかった worktree ディレクトリを、**ブランチはリポジトリに残したまま**消します。**拒否メッセージが渡すべき値をそのまま印字**し、`--discard-unpushed` と並ぶ 2 つ目の解決手段になりました — [日本語](https://code.claude.com/docs/ja/cli-reference#cli-commands) / [English](https://code.claude.com/docs/en/cli-reference#cli-commands)
- **`claude plugin install` / `uninstall` / `update` / `enable` / `disable` に `--json` が追加されました**。**標準出力の最終行に 1 つの JSON オブジェクト**を出します（マーケットプレイスが宣言したコマンドがその前に印字されうるので、**最終行だけを解析せよ**と明記）。常に在るのは `command` / `outcome`（`ok` または `failed`）/ `message` の 3 つで、`pluginId`・`scope`・`failureCode` は該当時のみ。**`--scope` が不正といった使い方の誤りでは結果行を出さず、理由を stderr に出して 1 で終了**します。`uninstall` では `--prune` と併用できません — [English](https://code.claude.com/docs/en/plugins-reference#plugin-install)
- **`claude plugin list --json` の各行に `errorDetails` と `noteDetails` が加わりました**。既存の `errors` / `notes` 文字列配列と並行して、**各項目の診断 `type` と、それが指すプラグイン・マーケットプレイス・サーバー・ファイルの名前**を持ちます — [English](https://code.claude.com/docs/en/plugins-reference#plugin-list)
- **WebFetch に 300 秒のダウンロード期限が入り、`CLAUDE_CODE_WEBFETCH_DEADLINE_MS` で変更できるようになりました**。**追従するリダイレクトも含めた合計**で、期限までに終わらなければ期限エラーになります。`0` で無制限。**平の数字のみを受け、小数など他の綴りは既定のまま**です — [日本語](https://code.claude.com/docs/ja/tools-reference#webfetch-tool-behavior) / [English](https://code.claude.com/docs/en/tools-reference#webfetch-tool-behavior)
- **エラーリファレンスに `The source file is not valid UTF-8 text` の本文が届きました**。アーティファクトの公開元ファイルがテキストとしてデコードできないか、既に `U+FFFD` を含むときに、**アップロードの前に公開を拒む**エラーです。**最初に直すべき行と列を名指し**し、後続があれば `(+2 more)` のように件数を添えます。UTF-8、または**リトルエンディアンの UTF-16 BOM で始まる場合は UTF-16 としてデコード**し、後者が失敗したときはメッセージが `UTF-16` を名指ししつつ**UTF-8 で書き直せ**と告げます。**意図した `U+FFFD` を出したいなら HTML で `&#xFFFD;` と書け**、という案内付き。**v2.1.267 より前は、検査せずアップロードしてサーバー側が拒んでいました** — [English](https://code.claude.com/docs/en/errors#the-source-file-is-not-valid-utf-8-text)
- **エラーリファレンスに `Working directory no longer exists when starting a background session` の本文が届きました**。エージェントビューからのディスパッチや `/background` で、**作業していたディレクトリが削除・移動された後**に起きます。**プロセスが終了したセッションにアタッチし直す／再起動する場合も、新しいプロセスが同じディレクトリで始まるため**同様です。**v2.1.257 より前は、セッションが始まったように見えた後でエージェントビューに失敗行として現れていました** — [English](https://code.claude.com/docs/en/errors#working-directory-no-longer-exists-when-starting-a-background-session)
- **`pricing` のレートが `modelPricing` 管理設定としてクライアントへ配られるようになりました**（詳細はハイライト 4 参照） — [English](https://code.claude.com/docs/en/settings-reference#modelpricing)
- **マネージドポリシーでコレクターを名指しすれば、リレーを迂回して直接エクスポートできるようになりました**（詳細はハイライト 4 参照） — [English](https://code.claude.com/docs/en/claude-apps-gateway-config#export-directly-to-your-collector)
- **`gatewayInternalNetworks` 管理設定が追加されました**。**組織が持つ自前のパブリック IPv4 ブロック上の Claude apps gateway への `/login` を、管理者が許可できる**ようになります（changelog のみ。対応する設定リファレンスの項はまだ在りません）
- **ゲートウェイに 2 つの警告が追加されました**。`access_control.allow_cidrs` が空のときの**起動時警告**と、**パブリックアドレスから最初にリクエストが届いたときの 1 回限りの警告**です
- **`claude self-hosted-runner --remove-session-state`（既定オフ）が追加されました**。セッション終了時に `<base-dir>/_sessions/` 配下のセッションごとのディレクトリを削除します
- **`claude auth status --json` の出力に `configDirectory` が加わりました**
- **公開したアーティファクトにブラウザタブのアイコンが付くようになりました**。**Claude がページの内容に合わせて選びます** ―― グラフやカレンダーのように、ページが何であるかを表すものです。タイトル・絵文字と同様に**指定して依頼できます** — [English](https://code.claude.com/docs/en/artifacts#create-an-artifact)
- **スキルのコマンド名の表に、`.claude/commands/` のサブディレクトリに置いたファイルの行が加わりました**。**`commands/` からの相対パスの `/` を `:` に置き換え、拡張子なしのファイル名を続けます**（`.claude/commands/frontend/component.md` → `/frontend:component`） — [English](https://code.claude.com/docs/en/skills#how-a-skill-gets-its-command-name)
- \[VSCode] **always-allow の権限ルールの保存先を `←` `→` で変えられるようになりました**。キーボードとスクリーンリーダーの利用者向けです。**最新のメッセージへフォーカスを移す「Claude Code: Focus last message」コマンド**も同じ趣旨で追加されました
- \[Claude Tag] **Slack チャンネルの configure ページから、組織の Claude in Slack の管理設定へ戻るリンクが加わりました**
- \[Code Review] **追跡レビューの「未解決の指摘」一覧の下に注記が加わりました** ―― **返信するだけでなくスレッドを resolve しないと、以後のレビューがその指摘を未解決として数え続ける**という内容です

**機能改善**

- **クラウド 3 プロバイダーが first-party セッションと同じ扱いになりました**（詳細はハイライト 1 参照） — [English](https://code.claude.com/docs/en/prompt-caching#changing-output-style)
- **タスク追跡ツールの既定が許可リスト方式に反転しました**（詳細はハイライト 2 参照） — [日本語](https://code.claude.com/docs/ja/tools-reference#task-tool-availability) / [English](https://code.claude.com/docs/en/tools-reference#task-tool-availability)
- **`/plugin` メニューを閉じると Claude Code が `/reload-plugins` を代行するようになりました**。インストール・有効化・無効化・アンインストールがメニューを閉じた時点で適用され、**リロードがプロンプトキャッシュを無効にする場合は警告して保留し、`/reload-plugins --force` で適用**します。**Claude が応答中に閉じた場合は応答の終了後にリロードが走ります**。メニューの外で起きた変更（別ターミナルの `claude plugin` コマンド、`--plugin-dir` で読んだプラグインの編集、自動更新の通知、キャッシュ都合で保留された `--plugin-dir` フォルダの変更）には従来どおり自分で `/reload-plugins` を実行します。**v2.1.268 より前は、メニューで有効化・無効化・アンインストールしたものとインストール時に有効化されなかったものが、`/reload-plugins` を実行するまで保留のままでした** — [日本語](https://code.claude.com/docs/ja/discover-plugins#apply-plugin-changes-without-restarting) / [English](https://code.claude.com/docs/en/discover-plugins#apply-plugin-changes-without-restarting)
- **上記に合わせて、プラグインのリロードを促していた 8 ページの記述が書き換わりました** ―― プロンプトキャッシング・スキル・MCP・プラグイン作成・プラグインマーケットプレイス・チャンネル・`security-guidance`・`claude-security` です。多くは「`/reload-plugins` を実行せよ」という手順が**「変更が適用されるタイミング」の節への参照**に置き換わり、`security-guidance` と `claude-security` では**コードブロックごと参照 1 行に縮められました** — [English](https://code.claude.com/docs/en/prompt-caching#when-plugin-changes-apply)
- **`WorktreeRemove` フックが終了コードで worktree の削除を止められるようになりました**（詳細は大幅更新 2 参照） — [English](https://code.claude.com/docs/en/hooks#worktreeremove)
- **エージェントビューに、worktree を消せなかったときの説明が加わりました**。**git かフックが失敗すると worktree とセッションの両方が残り、メッセージが原因を名指しします**（フックなら `exited 1` のような終わり方と stderr の先頭）。**`Ctrl+X` をもう一度押すか `claude rm <id> --force-remove-worktree <worktree-id>` でディレクトリを消せる**のは、**リポジトリの `.claude/worktrees/` 配下のリンクされた worktree であり、追跡ファイルに未コミットの変更が無く、内部に入れ子のリポジトリが無く、他のセッションの記録がそれを指していない**と確認できたときだけです — [English](https://code.claude.com/docs/en/agent-view#what-deleting-a-session-removes)
- **オートモードの拒否理由が、分類器の一致したルール名を角括弧で示すようになりました**（`[Data Exfiltration]` / `[Production Deploy]` など。詳細は大幅更新 2 参照）。**「Claude Code v2.1.208 以降はほとんどのセッションで固定文の `Blocked by classifier`」という版境界の説明は削除されました** — [English](https://code.claude.com/docs/en/auto-mode-config#review-denials)
- **`mcp_tool` フックが `SessionStart` / `Setup` でいつ走るかが書き下ろされました**（詳細は大幅更新 2 参照） — [English](https://code.claude.com/docs/en/hooks#mcp-tool-hook-fields)
- **プロバイダー別ゲートウェイ構成の説明が大幅に補強されました**。**Amazon Bedrock と Agent Platform のルートでは、Claude Code が送る beta ヘッダーとリクエストフィールドをそのプロバイダーが受け付ける集合に絞る**ことが明記され、ゲートウェイ互換ガイドへの参照が加わりました。ゲートウェイ自身のトークンの置き場所も**プロバイダー別に整理**され、Bedrock / Agent Platform / Claude Platform on AWS では `ANTHROPIC_AUTH_TOKEN` を `Authorization: Bearer` として送る（別スキームなら `ANTHROPIC_CUSTOM_HEADERS`）、**skip-auth 変数を外すと `Authorization` ヘッダーごと取り除かれる**、**`AWS_BEARER_TOKEN_BEDROCK` を設定すると `CLAUDE_CODE_SKIP_BEDROCK_AUTH` があってもそちらが `Authorization` になる**、と警告されました。Agent Platform 側には**モデル別リージョン（`VERTEX_REGION_CLAUDE_*`）・モデル版のピン留め・`..._SUPPORTED_CAPABILITIES` による能力宣言**がゲートウェイ越しでも効くことが追記されています — [English](https://code.claude.com/docs/en/llm-gateway-connect#route-to-a-cloud-provider-through-a-gateway)
- **`--effort ultracode` が「`xhigh` で開始する」から「`xhigh` を要求する」へ改められ、ultracode が使えない条件が 3 つに整理されました** ―― ワークフローがオフ、モデルが `xhigh` を持たない、**`xhigh` 未満の努力レベル上限が効いている**。この場合 **ultracode はオフで、モデルと上限が許す最も高いレベル（最大 `xhigh`）で開始**します。`/effort` メニューが ultracode を提示する条件もこの節への参照に変わりました — [English](https://code.claude.com/docs/en/model-config#adjust-effort-level)
- **スキル・サブエージェントの `effort` フロントマターが、努力レベル上限の対象であることが明記されました**。`maxEffortLevel` と組織の上限は**フロントマターで指定したレベルも頭打ちにします**。あわせて **Fable 5・Opus 4.8・Opus 4.7 では、モデル既定の努力レベルの「保持」が効いている間もフロントマターのレベルが適用される**ようになりました（**v2.1.267 より前は保持が優先され、フロントマターのレベルは無視されていました**） — [English](https://code.claude.com/docs/en/settings-reference#maxeffortlevel)
- **`allowedChannelPlugins` のエントリに文字列形式が加わりました**。`{marketplace, plugin}` のオブジェクトの代わりに **`"telegram@claude-plugins-official"` のような `"plugin@marketplace"` 文字列**を書けます（**v2.1.267 以降が必要。それより前のバージョンは文字列を含む値を丸ごと拒否します**） — [English](https://code.claude.com/docs/en/settings-reference#allowedchannelplugins)
- **`.claude/rules/` のシンボリックリンクの扱いが厳格化されました**。**作業ディレクトリの外を指すシンボリックリンクは外部インポートと同じ扱い**になり、**プロジェクトで外部インポートを承認するまで読み込まれず、承認後も `paths` フィールドを持たないものだけが読み込まれます**。承認を求めるのはプロジェクトのメモリファイルが `@path` で外部のファイルをインポートしたときだけで、**シンボリックリンク単独では求めません**。承認なしで共有ルールを読み込ませたいなら `~/.claude/rules/` に置け、という案内付きです — [English](https://code.claude.com/docs/en/memory#share-rules-across-projects-with-symlinks)
- **エージェントチームの生成条件に例外が 2 つ明示されました**。`name` 付きの Agent ツール呼び出しはチームメイトになりますが、**フォークである場合と、呼び出し自体が `isolation` を渡している場合は除きます**。**権限モードの継承からは `dontAsk` モードが外れました**（チームメイトはリードの `dontAsk` を継承しません）。**サブエージェント定義の参照範囲も「プロジェクト / ユーザー / プラグイン / CLI 定義」から「プロジェクト / ユーザー / managed」へ書き換わり、表示モードを問わないことが明記されました** — [English](https://code.claude.com/docs/en/agent-teams#permissions)
- **Bash コマンドの自動バックグラウンド化の除外が 3 種類から 1 種類に減りました**。前回までは **`sleep` 始まり・`git` を含む・完全に解析できない複合コマンド**の 3 つがタイムアウトで停止されていましたが、今回は **`sleep` 始まりのみ**になりました（`${VAR}` を解析不能とみなす旨の記述ごと削除されています） — [日本語](https://code.claude.com/docs/ja/tools-reference#background-commands) / [English](https://code.claude.com/docs/en/tools-reference#background-commands)
- **TypeScript SDK の `pending_permission_requests` の保証が強まりました**。「**走行中のセッションに `initialize` を送ったときに付く任意の配列**」から、「**成功した `initialize` の応答ラッパーには常に在り、未解決の権限リクエストが無ければ空**」へ変わりました（**Claude Code v2.1.268 以降が必要。それより前は省略されうるので、ワイヤープロトコルを自分で解析するなら欠落を『何も保留していない証拠』ではなく『古い CLI』と扱え**）。配列の内容も「クライアント接続前に発行され未応答のもの」から「**このプロセスが発行し未解決のもの**」へ定義が変わりました — [English](https://code.claude.com/docs/en/agent-sdk/typescript#sdkcontrolinitializeresponse)
- **`Unable to resize image` に 3 つのメッセージが追加されました** ―― **CMYK の JPEG**、**アニメーション WebP の先頭フレームがデコードできない場合**、**ピクセルがデコードできない（破損、または Claude Code が読めない符号化）場合**です。原因を名指しし、RGB の PNG / JPEG や先頭フレームの PNG / JPEG として保存し直せと案内します。**寸法の検証が「画像プロセッサなしで可能」から「ファイルヘッダーから、画像をデコードせずに可能」へ**具体化されました — [English](https://code.claude.com/docs/en/errors#unable-to-resize-image)
- **セッションスコープのスケジュール済みタスクの復元条件が整理されました**。「未期限の再帰タスクと時刻未到来のワンショットを復元する」から、「**`CronCreate` で作ったタスクを復元する。期限切れの再帰タスクと時刻を過ぎたワンショットは除く**」へ。**自分でペースを決める `/loop` は復元されない**ので `/loop` を再実行せよ、と明記されました（バックグラウンド Bash とモニタータスクが復元されないのは従来どおり）。比較表の該当セルも 2 ページで「例外あり」への参照に変わりました — [English](https://code.claude.com/docs/en/scheduled-tasks#limitations)
- **Remote Control のインジケーターの位置が、フルスクリーン描画では起動ヘッダーの作業ディレクトリ行末尾になりました**（フルスクリーンでない場合は従来どおりフッター）。**接続失敗時は、通知に加えて理由を述べる警告行が会話にも入る**ようになりました。**`claude remote-control` のサーバーは登録用の資格情報が切れると Anthropic API へ再登録してセッションを提供し続けます** — [English](https://code.claude.com/docs/en/remote-control#start-a-remote-control-session)
- **クラウド環境の管理が Desktop アプリからもできるようになりました**。プロンプトボックスの環境ドロップダウンから**追加（Add cloud environment）と、自分の環境の編集・アーカイブ（歯車アイコン）**ができます。`/remote-env` の説明も「claude.ai/code で管理せよ」から**環境セレクターの節への参照**に変わりました — [English](https://code.claude.com/docs/en/desktop#cloud-sessions)
- **VS Code 拡張の細部が 4 点改善されました** ―― セッション一覧のクリックが**設定した「優先する場所」で開く**、**モデル名ボタンが選択中の努力レベルを表示する**、**クリップボードから貼り付けて画像を添付できる**ことの明記、**現在のウィンドウの別タブで既に開いている会話をクリックするとそのタブへ切り替わる**。プラグインダイアログの案内も「変更後は再起動を促すバナーが出る」から「**そのウィンドウで開いている Claude Code セッションに即座に適用され、リロードできないセッションではやり直しか再起動を提案する**」へ変わりました — [English](https://code.claude.com/docs/en/vs-code#manage-plugins)
- **管理設定の「無効なエントリ」の記述が精密化されました**。`allowedHttpHookUrls` と `httpHookAllowedEnvVars` が強制するのは「**空の許可リスト**」ではなく「**空のマネージド許可リスト**」であり、**これらのキーは設定ファイル間でマージされるので、マネージド側が空でもユーザー / プロジェクト / ローカルのエントリは効き続ける**と明記されました。**版境界の書き方も「v2.1.267 より前は鍵ごと捨てていた」から「これら 3 キーのフォールバックには v2.1.267 以降が必要」へ**整理されています — [English](https://code.claude.com/docs/en/managed-settings#where-each-mechanism-stores-the-policy)
- **サーバー管理設定の承認の効き方に 1 段落が加わりました**。**`sandbox.credentials` または `sandbox.network.tlsTerminate` への承認は、同じ配信設定の `sandbox.network.allowedDomains` のエントリもカバーします**（両者が同じ許可リストに作用するため）。**`sandbox.network.allowedDomains` 単独では承認を要さないにもかかわらず、管理者がそのエントリを追加・削除するとダイアログが再度出ます** — [English](https://code.claude.com/docs/en/server-managed-settings#security-approval-dialogs)
- **OpenTelemetry の `user.email` の出所が広がりました**。「OAuth 認証時」から「**サインイン、またはクラウドセッションではそのセッション自身の資格情報から**」へ。監査イベントの identity 属性も同じ条件が加わり、**この属性が行くのは組織が設定した OTel エンドポイントだけで Anthropic へは行かない**と明記されました — [English](https://code.claude.com/docs/en/monitoring-usage#standard-attributes)
- **リトライ回数の説明に「独自の小さい再試行予算を持つ原因」が加わりました**。`attempt` が実効上限より小さい値になるのは `400` のような再試行不可のエラーだけでなく、**AWS / Google Cloud の資格情報の読み込み失敗のように最大 2 回しか再試行しないもの**もあるためです。`CLAUDE_CODE_RETRY_WATCHDOG` の記述も「v2.1.199 時点で」から「**v2.1.199 以降で設定できる**」へ整理されました — [English](https://code.claude.com/docs/en/monitoring-usage#detect-retry-exhaustion)
- **クラウド環境のエージェントプロキシの用語が統一されました**。「エージェントプロキシがスキップするホスト」という言い方が「**資格情報が付かないホスト**」へ 4 か所で揃えられ、**セキュリティのページからネットワークアクセスの各節への参照**も加わりました — [English](https://code.claude.com/docs/en/cloud-environments#requests-that-never-get-the-credential)
- **アーティファクトの制約の記述が整理されました**。「フォームの入力を保存できない」「自前の API を呼べない」といった記述が削られ、**`No backend` の行は「静的ページであり、閲覧者を自分で認証できない」の 1 文**になりました。代わりに **`Source file types` の行に「UTF-8、または BOM によるリトルエンディアン UTF-16 としてデコードできなければならない」**という条件と、エラーリファレンスの新設節への参照が入りました — [English](https://code.claude.com/docs/en/artifacts#page-constraints)
- **MCP の接続失敗メッセージに出る origin の扱いが変わりました**。「**`${VAR}` 展開の後の origin を取るので、変数由来のホストは展開されて現れる**」から、「**local / project / user スコープと管理 MCP 設定のサーバーでは、設定に書かれたままのホストを表示するので `${VAR}` 参照は展開されない**」へ ―― 秘匿情報の露出を塞ぐ changelog の項目と対になる変更です — [English](https://code.claude.com/docs/en/mcp#mcp-installation-scopes)
- **ワークフローの `agent()` が `null` になる原因に、オートモードの分類器による事前ブロックが加わりました**。**サブエージェントが始まる前にブロックされた呼び出しは `null` に解決され、実行の進捗ビューに理由付きで現れます** — [English](https://code.claude.com/docs/en/workflows#let-claude-decide-with-ultracode)
- **フルスクリーンで上にスクロール中、ビューの上へ流れた直近のプロンプトが薄いヘッダー行として出るようになりました**。**クリックでそのプロンプトへ飛べます** — [English](https://code.claude.com/docs/en/fullscreen#scroll-the-conversation)
- **`ctrl+x` 配下の既定チョードが 2 つ増えました** ―― `Chat` コンテキストの **`ctrl+x ctrl+a` と `ctrl+x tab`**（いずれも v2.1.260 以降）。`ctrl+x` を単独キーとして取り戻すための解除例にも 2 行追加されました — [English](https://code.claude.com/docs/en/keybindings#chords)
- **シェルモードのサンドボックスの説明が、例外を先に置く形へ書き換わりました**。「通常の対話セッションでは外で走る」から「**strict sandbox mode の一覧に該当するセッションでなければ外で走る**」へ — [English](https://code.claude.com/docs/en/interactive-mode#shell-mode-with-prefix)
- **Amazon Bedrock のリージョン解決から「v2.1.172 以降」「v2.1.171 以前は AWS 設定ファイルを読まない」という版境界が削除されました**。Mantle エンドポイントの説明からも同じ版の記述が消え、**現在の挙動だけを述べる形**になりました — [English](https://code.claude.com/docs/en/amazon-bedrock#3-configure-claude-code)
- **チャンネルプラグインのデバッグ手順が具体化されました**。`failed` 状態の stderr トレースを見るには、**`claude --debug --dangerously-load-development-channels server:webhook` で起動し直せ**と明示されました — [English](https://code.claude.com/docs/en/channels-reference#test-during-the-research-preview)
- \[Claude Tag] **ブロックされた動作の説明が改善されました**。**権限チェック・Claude 自身が先に確認すると決めたこと・アクセス権の不足のどれが止めたのか**を述べるようになりました。**読み取り専用の照会（Slack の検索、スレッドの読み取り、人物の検索）を順番ではなく並列に実行して応答が速くなり**、**文章 1 文ぶんの比較は横スクロールする幅広の表ではなくリストで返す**ようになりました
- \[Claude Code on the web] **会話からのルーチン作成が改善されました**。**新しいルーチンにコネクターが無い場合、確認だけで済ませず「無いこと」と追加方法を述べます**

**バグ修正**

以下はすべて v2.1.268 の項目です。**`ANTHROPIC_BASE_URL` の回帰と、権限・秘匿情報の 4 件はハイライト 5 でまとめて扱っています。**

- **`ANTHROPIC_BASE_URL` のサードパーティ互換エンドポイントで、v2.1.265 以降すべてのターンが HTTP 400 で失敗する**問題を修正（原因は Artifact ツールの入力スキーマの正規表現）
- **WebFetch が、応答を開いたまま終えないサーバーで無限に待つ**問題を修正（300 秒で失敗。`CLAUDE_CODE_WEBFETCH_DEADLINE_MS` で変更可）
- **再生成したプロセス内チームメイトが、信頼していないフォルダの同名エージェントファイルからツールやシステムプロンプトを拾う**問題を修正
- **CPU 使用率が高止まりする**問題を修正（長時間アイドルのセッションのビジーループ、セッションリキャップ中の高頻度なターミナルフォーカス報告）
- **MCP ツール呼び出しの後で Claude が「あなたのメッセージは空で届いた」と答える**ことがある問題を修正
- **シンボリックリンクされたディレクトリ（macOS の `/etc`・`/tmp`・`/var`、Linux の `/bin`）への deny / ask ルールが、実体のパスで指定されたときに効かない**問題を修正。**Bash コマンドがシンボリックリンク側の綴りの拒否ルールを無視する**件も同時に修正
- **`env -C` や `eval` のように権限チェッカーが解析できないコマンドが同じ行に在ると、Read / Edit の拒否ルールが効かない**問題を修正
- **プラグインとマーケットプレイスのエラーが、git ソース URL のトークンやパスワードを表示する**問題を修正
- **`/mcp` と `/plugin` のサーバー詳細、`claude mcp list` / `get`、MCP のログインエラーが、`${VAR}` から解決したシークレットを表示する**問題を修正
- **`excludeDynamicSections` を使う SDK セッションで、最初のメッセージが毎リクエスト再描画され、プロンプトキャッシングと拡張思考がセッション途中で壊れる**問題を修正
- **モデルアクセスの拒否がキャッシュされたまま古くなり、権利のある利用者が再起動後や Desktop の Code タブで「制限されている」と告げられる**問題を修正
- **別の Claude Code プロセスが古いモデルアクセス項目を更新したとき、実行中のセッションが黙って組織の既定モデルへ切り替わる**問題を修正
- **Fable モデルの長コンテキストの 429 が、Pro / Team プランで 1M コンテキストの案内ではなく使用クレジットの同意プロンプトを出す**問題を修正
- **プロファイル経由のワークロード ID 連携（claude-code-action が設定する形）で、プロファイルを共有するプロセスが実行中に `401 … jti reused` で失敗しうる**問題を修正
- **ローカルのコールバックポート範囲をバインドできないときに、MCP サーバーの OAuth サインインが「No available ports for OAuth redirect」で失敗する**問題を修正
- **`/compact` と自動コンパクトの会話要約が、`$` 列を含むテキストを壊す**問題を修正
- **`/compact` で終わった会話を再開すると、復元ファイルのノートの読み込み順が毎回変わる**問題を修正
- **SDK のプロンプト候補・サイド質問・`/rename` が、コンパクト前の会話を送る**問題を修正
- **上矢印で以前のプロンプトを呼び出して編集した後、`@` のファイル候補と `/` のコマンド候補が出ない**問題を修正
- **`claude agents` で、エージェント一覧へ戻るために `←` を自然な速さで続けて押すと、1 秒以上止まるまで無視される**問題を修正
- **`claude agents` のセッション削除が、worktree を消せないときに詰まる**問題を修正。**メッセージが原因と次の一手を名指しし、git の worktree なら `Ctrl+X` をもう一度押すとディレクトリを消せる**ようになりました
- **エージェントパネルのバックグラウンドエージェント行とワークフロー行が、テキストに改行を含むと何行にも広がる**問題を修正
- **組織の管理設定が MCP 許可リストを設定していると、Claude in Slack のセッションが Slack のツールを失う**問題を修正
- **Claude in Chrome が、スキームは在るがホストを解析できない遷移先 URL に対してホスト「https」の許可を求める**問題を修正
- **現在のタスクのラベルが長いとスピナーが何行にも折り返す**問題を修正（ラベルと「Next:」の行が 1 行に収まるようになりました）
- **ターミナルのネイティブカーソルが有効なとき、`/bug` と `/feedback` の説明欄にカーソルが出ない**問題を修正
- **`claude remote-control` が提供する Remote Control セッションが、`ListAgents` でセッションタイトルではなく生成名で出る**問題を修正
- **`claude plugin validate` が、プラグインローダーは受け付けるドット 2 つで始まるディレクトリ名のパスを拒む**問題を修正
- **プラグインが、検査できない既定のモニターファイルやルートの `SKILL.md` を黙って飛ばす**問題を修正
- **WebFetch の localhost やドットなしホスト名に対するエラーが、URL を拒む理由を説明し curl を提案する**ようになりました
- **`--print` モードで PermissionRequest フックが発火しない**問題を修正
- **ヘッドレス（`-p`）実行でポリシーヘルパーの警告が出力されない**問題を修正
- **`/resume` が `/fork` のバックグラウンドセッションを、自身の `⑂` フォーク名ではなく親の名前で一覧する**問題を修正
- **サインアウト状態で `/remote-control` などの claude.ai ゲート付きコマンドを打つと、Claude for Enterprise への移行メッセージが出る**問題を修正（`/login` を提案するようになりました）
- **`CLAUDE_CODE_SESSIONEND_HOOKS_TIMEOUT_MS` が、フックごとの `timeout` を持たない SessionEnd フックを延長しない**問題を修正（従来は 1.5 秒でキャンセルされていました）
- **GitHub アカウントが未接続のときに `/autofix-pr` などのクラウドセッション系コマンドが、再試行や Claude GitHub App のインストールを勧める**問題を修正（`/web-setup` か Web の接続ページを案内するようになりました）
- **`/teleport` や `/remote-env` などのクラウドセッション系コマンドが、組織のポリシーで無効化されているときに「Unknown command」と答える**問題を修正
- **Bash のサンドボックスの説明が封じ込めを過大に述べていた**問題を修正（ファイルシステム分離がオフのときに強制されないパス一覧を出さず、strict モードでも「決してサンドボックス外では走らない」と主張しなくなりました）
- \[VSCode] **`CLAUDE_CONFIG_DIR` を設定ファイルや `environmentVariables` 設定で指定すると、セッション一覧・設定トグル・チャットタブが壊れる**問題を修正。**同じ設定経路のときにカスタムスタイルビルダーが CLI の読まないフォルダに User レベルのスタイルを保存する**件も修正
- \[VSCode] **ログイン・ログアウト・アカウント切り替えの直後に、開いているタブでモデルピル・モデルピッカー・コマンドメニューが数秒空白になる**問題を修正
- \[VSCode] **プロジェクトまたはローカルの設定が `~/.claude/settings.json` のモデルを上書きしていると、新規タブやリロード直後の会話でモードピッカーから Auto が消える**問題を修正
- \[VSCode] **SessionStart フックを設定していると、ウィンドウのリロード後にセッション名が直前のプロンプトへ戻る**問題を修正
- \[VSCode] **同じウィンドウの別タブが既に起動しているのに、フッターのモデルピルと Remote Control ピルが新規タブの Claude プロセスの起動を待つ**問題を修正。**セッションタブの起動が設定読み取りより 0.5 秒以上遅れて届くと 2 つ目の Claude プロセスが完全な起動処理を走る**件も修正
- \[VSCode] **セッション一覧からの再開が `claudeCode.preferredLocation: "sidebar"` を無視して常にパネルで開く**問題と、**プログラムからの open がその設定を "panel" に戻す**問題を修正
- \[VSCode] **WSL 未インストールのマシンで WSL インストールの案内が出る**問題と、**WSL インストール済み環境で Windows のファイルの IDE 診断が正しく返らない**問題を修正
- \[Claude Code on the web] **約 6 時間を超えるクラウドセッションが、永続セッションフォルダに保存したファイルを黙って失う**問題を修正（**最大 1 日保持される**ようになりました）
- \[Claude Code on the web] **管理者がモデルの努力レベルに上限をかけている組織で、ルーチンがセッションを再開したときや努力レベル未設定でセッションを開始したときに「Invalid effort level」エラーになる**問題を修正
- \[Claude Tag] **管理設定ページが読み込みスケルトンで固まる／一時的な読み込み失敗の後で空白になる**問題を修正（**読み込みに失敗した区画に Retry ボタンが出る**ようになりました）
- \[Claude Tag] **Slack 管理者が Enterprise Grid のチャンネルを別ワークスペースへ移すと、そのチャンネルの Claude 設定（リポジトリ・環境・アクセス）が失われる**問題を修正
- \[Claude Tag] **独自のセッションを持つスレッドで `@Claude !restart` すると、「このスレッドはチャンネルセッションが扱う」という矛盾した通知も投稿されることがある**問題を修正
- \[Claude Tag] **チャンネルの長時間セッションが会話の途中で新しいものに差し替わる**問題を修正（**定期更新がチャンネルとスレッドが静かになるまで待つ**ようになりました）
- \[Claude Tag] **チャンネル設定のカードを 2 回以上クリックすると、既に適用済みなのに提案したセッションへ「拒否された」と伝わる**問題を修正（結果が 1 度だけ送られるようになりました）
- \[Claude Tag] **URL を山括弧で囲んだ Markdown リンクが、Slack でクリックできるリンクにならず角括弧の素のテキストとして出る**問題を修正
- \[Claude Tag] **ゲストが Claude を使えるチャンネルで、ワークスペースのゲストのトップレベル @メンションが「Slack アカウントが接続されていません」と返される**ことがある問題を修正
- \[Claude Tag] **公開チャンネルのメモリが変わりました** ―― **各チャンネルが自分のノートを持ち、他の公開チャンネルで保存したノートを Claude が思い出さなくなりました**（ワークスペースのノートは共有のまま）
- \[Code Review] **指摘を検証するエージェントの 1 つが途中で失敗すると、レビューが未完了として終わる**ことがある問題を修正（**そのエージェントを差し替えて判定に到達する**ようになりました）
- \[Code Review] **実行中のレビューの後ろに積まれた push 起点のレビューが、プルリクエストがドラフトに変換された後でも投稿する**問題を修正
- \[Code Review] **PR がルートのファイル（`README.md` など）を編集したとき、CLAUDE.md が列挙するファイルと名前が一致するだけなのにディレクトリの CLAUDE.md の規約を無視する**問題を修正

**その他**

- **今回の見出しマップの変更は「追加だけ」です** ―― 65 行の追加のうち 1 行は先頭の自動生成スタンプなので、**実質 64 行（ページ見出し 1・空行 2・見出し 61）**。**削除された見出しは 1 件もありません**（前回は 2 件）。**追加された 61 見出しはすべて本文未着**で、これが今回の持ち越しになります
- **`llms.txt` の差分 23 行のうち 22 行は翻訳インデックスのページ数表示です**（`## Indexes` に並ぶのは非英語の 11 言語だけで、英語の行はありません）。**11 言語すべてが 166 ページから増え、フランス語・ドイツ語・イタリア語・スペイン語・中国語・繁体中国語・ロシア語・ブラジルポルトガル語の 8 言語が 192 ページ、日本語・韓国語・インドネシア語が 191 ページ**になりました。前回まで 11 言語が横並びの 166 ページだったので、**26 ページぶんの増加と、3 言語が 1 ページだけ遅れている状態**が同時に現れた形です。残る 1 行が `plugin-evals` の追加です
- **プラグインリファレンスの新設 `--json` は 5 か所から `#plugin-json-result` を参照していますが、`llms-full.txt` にその見出しはありません**。該当箇所は `<span />` から始まる段落として展開されており、**見出し要素が平坦化で落ちたためにアンカー先だけが本文から辿れない**状態です。見出しマップ側にも現れていません
- **分析ページの `Tagging criteria` が本文から削除されました**。前回「見出しマップからだけ消え、本文には `#### Tagging criteria` として残っている」と報告した 1 件で、**今回、見出しと本文 3 行がまとめて消えて決着しました**（PR 帰属の判定基準を述べていた節です） — [English](https://code.claude.com/docs/en/analytics#pr-attribution)
- **`Mythos 5` という名前の登場箇所が 9 か所から 3 か所へ減りました**。タスク追跡ツールの既定が許可リスト方式に変わり（ハイライト 2）、**そこでモデルを名指しで除外する必要がなくなった**ためです — [日本語](https://code.claude.com/docs/ja/tools-reference#task-tool-availability) / [English](https://code.claude.com/docs/en/tools-reference#task-tool-availability)
- **バンドルスキルの無効化の説明から `/doctor` の例外が消えました**。`disableBundledSkills` の説明が「**`/doctor` を除くすべてのバンドルスキルを無効にする**」から「**バンドルスキルを無効にする**」へ 2 か所で書き換わりました — [English](https://code.claude.com/docs/en/skills#bundled-skills)
- **claude.ai から同期したスキルの扱いに、版境界が 4 か所追加されました**。名前の比較と `claude.ai sync` ラベル、フロントマターのサニタイズ、本文の扱い（`!` コマンドを走らせない・`@` 参照を添付しない・プレースホルダを展開しない）のいずれも、**Claude Code v2.1.228 以降が必要**と明記されました — [English](https://code.claude.com/docs/en/skills#skills-synced-from-claudeai)
- **スキルの `description` を省略したときのフォールバックが変わりました**。「**markdown コンテンツの最初の段落**」から「**最初の空でない行**」へ。フロントマターが壊れたときの説明も「Claude が突き合わせる `description` を持たない」から「**あなたの `description` に突き合わせられない**」へ書き換わりました — [English](https://code.claude.com/docs/en/skills#frontmatter-reference)
- **マーケットプレイスのエントリパスの制約が 1 つ増えました**。**macOS と Linux では、先頭の `./` より後ろにバックスラッシュを含むエントリパスを拒む**ので、**どのプラットフォームでも区切りは `/` で書け**と明記されました。changelog の「バックスラッシュで封じ込めチェックを迂回できた」修正と対になる記述です — [English](https://code.claude.com/docs/en/plugin-marketplaces#plugin-entries)
- **サードパーティ連携ページの CLAUDE.md 配置の説明が、メモリページへの参照 2 本に置き換わりました**。組織全体・リポジトリレベルの具体的なパスを列挙していた 6 行が、**「CLAUDE.md をどこに置けるか」と「組織全体の CLAUDE.md をどう配るか」への参照**になりました — [English](https://code.claude.com/docs/en/third-party-integrations#invest-in-documentation-and-memory)
- **Claude apps gateway のテレメトリ保証の記述が、箇条書きの入れ子に組み替えられました**。「ローカルの `OTEL_EXPORTER_OTLP_ENDPOINT` に関わらずゲートウェイへ送る」に**「ポリシーがコレクターを名指ししている場合を除く」**という例外が加わり、Desktop 埋め込みセッション・宛先未設定時・既にコレクターを持っている場合の 3 点が入れ子の箇条書きになりました — [English](https://code.claude.com/docs/en/claude-apps-gateway#whats-enforced-on-developers)
- **`plugin-hints` と `fullscreen` から版境界が 1 つずつ削除されました** ―― `CLAUDE_CODE_CHILD_SESSION` の「v2.1.172 以降が必要なので古い版のセッションはヒントを取りこぼす」、`/scroll-speed` の「4 分の 1 刻みには v2.1.172 以降が必要」です。**`advisor` と `model-config` からも「Fable 5 は v2.1.170 以降が必要」が消え**、Fable 5.1 の版要件（v2.1.257 以降）だけが残りました — [English](https://code.claude.com/docs/en/advisor#choose-an-advisor-model)
- **`agents` ページの worktree の説明が具体化されました**。「エージェントビューはディスパッチした各セッションを自動で自分の worktree へ移す」から「**エージェントビューからディスパッチしたセッションは、ファイルを編集する前に自分の worktree へ移る**」へ、ファイル編集の分離の節への参照付きで書き換わりました — [English](https://code.claude.com/docs/en/agents#check-on-running-work)
- **Web のクラウドセッションの分離の説明に、環境側の参照が加わりました**。ネットワークアクセス制御の箇条書きから、**アクセスレベル・既定の許可ドメイン・許可リストを通らないトラフィック**の各節へ辿れるようになりました — [English](https://code.claude.com/docs/en/claude-code-on-the-web#security-and-isolation)
- **見出しマップ先頭の自動生成スタンプが 2026年09月10日 22時57分12秒 UTC から 2026年09月12日 02時23分32秒 UTC へ進みました**。**これまで 22 時台で揃っていた時刻が 02 時台に変わっています**
- **`whats-new/` の無差分は 9 回連続になりました**。最新の週間ダイジェストは 9 回前のサマリで扱った Week 34（2026年08月17日～21日）のままで、新しい週の追加も既存ページの訂正もありません。`llms-full.txt` に収録されている `whats-new/` 配下のページは索引を含めて 22 件で変わっていません

**参考リンクについて**: **今回、日本語版のリンクを付けられるのは 4 ページです** ―― CLI リファレンス・ツールリファレンス・プラグイン発見ページ・新設の `plugin-evals` です。作成時点で公開中の日本語版を実際に取得して確認したところ、**この 4 ページは今回の変更をすべて反映済み**でした（CLI リファレンスは `--force-remove-worktree` と「v2.1.268 より前は」の記述、ツールリファレンスは許可リスト方式の列挙と `CLAUDE_CODE_WEBFETCH_DEADLINE_MS`、プラグイン発見ページは `/plugin` メニューを閉じたときのリロード、`plugin-evals` は全節が翻訳済み）。**一方、プロンプトキャッシング・フック・Claude apps gateway 設定は未追従**です（プロンプトキャッシングは「出力スタイルの変更」が依然として「キャッシュを無効にするアクション」の一覧にあり `Resuming a session` の節も無く、フックは `WorktreeRemove` の決定制御が「いいえ」のまま、gateway 設定は新設 3 節と `modelPricing` への言及がありません）。**エラーリファレンスは新設 2 節の反映を断定できなかったため、安全側で英語版のみ**にしました。**その他のページは日本語版の確認を行っていないため英語版のみ**とし、**本文が未着の持ち越しにはアンカーを付けていません**。

## 新着情報

（今回の対象期間には `whats-new/` 配下のページに差分がありませんでした。本文が変わった 53 ページはいずれもリファレンス・ガイド系と changelog です。最新の週間ダイジェストは 9 回前のサマリで扱った Week 34（2026年08月17日～21日）のままで、新しい週のダイジェストの追加も既存ページの訂正もありません。**`whats-new/` の無差分は 9 回連続**です。本文側が 53 ページ動き、96 項目の changelog が載り、新設ページまで宣言された今回の規模を考えると、リリースノート系の更新経路だけが 2 週間以上止まっている状態が続いています）

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-09-10.md](./archives/latest/2026-09-10.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-09-10.md](./archives/latest-detail/2026-09-10.md)

<!--
base_commit: de9cda17683da28d936a197650b1dab64d4d7341
head_commit: 49baf315f926d9366d24e87daff4bb29ba022a17
generated_at_full: 2026-09-12T15:12:25+09:00
-->
