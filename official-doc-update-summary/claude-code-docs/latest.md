---
対象期間: 2026年08月22日 〜 2026年08月24日
作成日: 2026-08-24
---

# Claude Code 公式ドキュメント更新サマリ

```markdown
今回は 2 日分の取り込みで、44 ページに差分がありました。新規ページの追加も新着情報の更新も無く、changelog に新しいリリースエントリも加わっていません。実態は、v2.1.234〜v2.1.242 を要件とする機能を既存ページに書き込む作業で、プロンプトキャッシュ・使用量上限・プラグイン配布の 3 領域に集中しています。

主要なものを以下に挙げます。

1. プロンプトキャッシュの TTL が「メイン会話」と「それ以外」の 2 バケットに整理され、それぞれ別に選べるようになった
2. claude.ai の使用量上限に当たったとき、リセットを待って中断したタスクを自動で再開するようになった
3. プラグインのアーカイブをダウンロードするときの認証ヘッダを、コマンドで都度生成できるようになった
4. `/model` ピッカーに並ぶモデルとラベルを組織側で決められる `modelPicker` が加わった
5. 素の `WebFetch` 権限ルールとドメイン指定ルールが別物であることが明文化された
```

## ハイライト

1. [**プロンプトキャッシュの TTL をメイン会話とそれ以外で選び分ける**](./latest-detail.md#1-プロンプトキャッシュの-ttl-をメイン会話とそれ以外で選び分けられるようになった):  
  TTL の決まり方が「認証方法で決まる」から「リクエストがどちらのバケットに属するかで決まる」に整理され、`promptCacheTtl` / `subagentPromptCacheTtl` の 2 設定と対応する環境変数が加わった。v2.1.242 以降が必要。
2. [**使用量上限のリセットを待って中断したタスクを自動再開する**](./latest-detail.md#2-使用量上限のリセットを待って中断したタスクを自動再開する):  
  claude.ai サブスクリプションの対話セッションで既定 ON。セッションを開いたまま待ち、リセット時に固定プロンプトを送って中断箇所から再開する。v2.1.234 以降。
3. [**プラグインアーカイブのダウンロードを認証する `headersHelper`**](./latest-detail.md#3-プラグインアーカイブのダウンロードを認証する-headershelper):  
  `archive` ソースのプラグインを資格情報が要るレジストリから落とすための仕組み。固定値の `headers` に加え、短命なトークンをコマンドで都度生成する `headersHelper` が使えるようになった。v2.1.238 以降。
4. [**`/model` ピッカーの並びとラベルを組織で決める `modelPicker`**](./latest-detail.md#4-model-ピッカーの並びとラベルを組織で決める-modelpicker):  
  管理設定・`--settings`・ユーザー設定から読む新キー。組み込みの一覧に足すことも、丸ごと置き換えることもできる。プロジェクト・ローカル設定では無視される。v2.1.242 以降。
5. [**素の `WebFetch` ルールとドメイン指定ルールが別物であることが明文化された**](./latest-detail.md#5-素の-webfetch-ルールとドメイン指定ルールが別物であることが明文化された):  
  従来「等価」と書かれていた記述が撤回され、専用の節が新設された。サンドボックス化コマンドが到達できるホストを変えるのはドメイン指定形だけ。

## 新規追加されたページ

（今回の対象期間に新規追加されたページはありません。差分は `llms-full.txt` の既存 44 ページのみで、`llms.txt` のページ一覧に増減はありませんでした）

## 大幅に更新されたページ

- [**プラグインマーケットプレイスの作成と配布**](./latest-detail.md#1-プラグインマーケットプレイスの作成と配布) ([English](https://code.claude.com/docs/en/plugin-marketplaces#distribute-through-organization-settings)):  
  追加 144 行・削除 16 行で今回最大の差分。`headersHelper`（ハイライト 3 参照）のほか、組織設定経由の配布ルールが独立した節に昇格し、トップレベル `bin/` を含めてはいけないという制約が加わった。
- [**設定リファレンス**](./latest-detail.md#2-設定リファレンス) ([English](https://code.claude.com/docs/en/settings-reference#modelpicker)):  
  追加 140 行・削除 9 行。新規キーは `modelPicker`・`promptCacheTtl`・`subagentPromptCacheTtl`・`autoContinueAtUsageLimit` の 4 つ（いずれもハイライト参照）。既存キーでは `disableAllHooks` が Agent SDK のフックを残すようになった。
- [**インタラクティブモード**](./latest-detail.md#3-インタラクティブモード) ([English](https://code.claude.com/docs/en/interactive-mode#start-a-wait-yourself)):  
  追加 52 行・削除 0 行。使用量上限の待機の節（ハイライト 2 参照）が丸ごと足されただけで、既存の記述は 1 行も変わっていない。

## 軽微な更新

今回は 2 日分の取り込みをまとめた対象期間で、差分のあったページは 44 です。差分は `llms-full.txt` のみで、`llms.txt` のページ一覧とページ見出しマップ（`claude_code_docs_map.md`）には差分がありません。changelog にも新しいリリースエントリは加わっておらず、前回の v2.1.241（2026年08月23日）が最新のままです。したがって本サマリで挙げるバージョンは全て、リリースの告知ではなく本文中の「v2.X.Y 以降が必要」という記述に由来します。**大幅更新に入れる基準は前回同様「差分 50 行以上 かつ 内容の変更を伴うこと」**とし、3 ページを大幅更新、残る 41 ページをここで扱います。表の桁揃えを除いた実質の差分で判定しており、たとえば Agent SDK の Python リファレンスは見かけ 134 行の差分ですが、空白を無視して数え直すと 22 行で、内容も既存フィールドへのバージョン注記の追加だけなのでここに回しています。なお本サマリの参考リンクは全て英語版のみです。今回の変更に日本語版が追従していないためで、プロンプトキャッシュとインタラクティブモードの 2 ページを実際に取得して確認したところ、前者は TTL の説明が旧構成（認証方法による場合分け）のままで新設の 2 節が無く、後者には使用量上限の待機の節がありませんでした。他のページは個別には確認していませんが、いずれも同時期に入った同じ機能群の記述であるため未追従とみなし、安全側に倒して英語版のみを載せています。

**新機能**

- `/rate-limit-options` がコマンド一覧に加わりました。claude.ai の使用量上限でリクエストが止まったときに、待って自動継続する・使用クレジットを足す・プランをアップグレードする、の選択肢を出すコマンドです。上限に当たったとき Claude Code が自分で開くこともあります。claude.ai サブスクリプションが必要で、コマンドメニューには出ないため全部打つ必要があります。待って継続する行は v2.1.234 以降です（詳細はハイライト 2 参照）— [English](https://code.claude.com/docs/en/commands#all-commands)
- Notification フックのマッチャに `quota_auto_resume_fired`・`quota_auto_resume_stale`・`quota_auto_resume_disabled` の 3 つが加わりました（v2.1.234 以降）。順に、リセット時または待機中の操作で使用量が復活して続行したとき、スリープが約 30 分を超えて `Enter` 待ちになったとき、待機がタスクを続けずに終わったときに発火します。最後の 1 つは `Esc` / `Ctrl+C` や **Don't continue automatically** による明示的なキャンセルでは発火しません。あわせて、待機中は `idle_prompt` を送らず、待機が自然に終わったときは代わりにこの 3 つのいずれかが発火することが明記されました — [English](https://code.claude.com/docs/en/hooks#notification)
- 同じ 3 マッチャがフックのガイドの一覧表にも追加されました — [English](https://code.claude.com/docs/en/hooks-guide#filter-hooks-with-matchers)
- 環境変数に `CLAUDE_CODE_PROMPT_CACHE_TTL` と `CLAUDE_CODE_SUBAGENT_PROMPT_CACHE_TTL` が加わりました（v2.1.242 以降、詳細はハイライト 1 参照）。あわせて `ENABLE_PROMPT_CACHING_1H` の説明が「サブスクリプションではメイン会話に 1 時間が自動適用される」という書き方に改められ、`FORCE_PROMPT_CACHING_5M` が上書きする対象に新しい 2 変数と 2 設定が加わりました — [English](https://code.claude.com/docs/en/env-vars#variables)
- `/usage` のプラン使用量の内訳に **Loops** の行が加わりました（v2.1.242 以降）。直近に走った `/loop` などのスケジュールタスクのうち重いものをトークン合計の多い順に並べ、残りは件数で示します。各行には発火頻度・実行回数・合計トークン・1 回あたりトークン・最終実行が出ます。行はタスクのプロンプトでキーされるので、止めて作り直しても 1 行のままです。VS Code 拡張の Account & usage ダイアログには Loops の行は出ません — [English](https://code.claude.com/docs/en/costs#plan-usage-breakdown)

**機能改善**

- プロンプトキャッシュのページで、TTL の説明が「認証方法による場合分け」から「リクエストのバケットによる場合分け」に全面的に書き直されました（詳細はハイライト 1 参照）— [English](https://code.claude.com/docs/en/prompt-caching#which-ttl-each-request-gets)
- 権限のページに、素の `WebFetch` ルールとドメイン指定ルールの違いを説明する節が新設されました（詳細はハイライト 5 参照）— [English](https://code.claude.com/docs/en/permissions#allow-or-deny-every-fetch)
- サンドボックスのページで、ドメイン制御に関わるルールの表記が `WebFetch(domain:...)` に統一され、サンドボックスが尊重するワイルドカードの形が明記されました（詳細はハイライト 5 参照）— [English](https://code.claude.com/docs/en/sandboxing#network-isolation)
- プロンプトキャッシュの TTL を用途別に選ぶ導線が、Amazon Bedrock・Google Cloud の Agent Platform・Microsoft Foundry・Claude Platform on AWS の 4 ページに 1 文ずつ加わりました（詳細はハイライト 1 参照）— [English](https://code.claude.com/docs/en/prompt-caching#choose-the-ttl-yourself)
- ワークフローのエージェントは、メイン会話の TTL バケットの外なのでサブスクリプションでも既定 5 分であり、1 時間にするには `subagentPromptCacheTtl` を `1h` にする、という説明が加わりました。プロセス内のチームメイトについても、エージェントチームのページに同じ趣旨の説明が入っています — [English](https://code.claude.com/docs/en/workflows#prompt-caching-in-a-fan-out)
- Agent SDK のコスト追跡のページも 2 バケット構成に追従しました。自分のターンはメイン会話のバケットに入ること、サブエージェントなどはバケットが別で TTL の制御も別であること、`promptCacheTtl` を `1h` にすれば使用クレジットを引き出している間もメイン会話の 1 時間キャッシュを維持できることが書き足されています — [English](https://code.claude.com/docs/en/agent-sdk/cost-tracking#extend-the-prompt-cache-ttl-to-one-hour)
- エラーリファレンスに `You've hit your Sonnet limit` が加わりました。Opus と Sonnet の上限はそれぞれそのモデルファミリへのリクエストにだけ効くので、`/model` でファミリ外のモデルに切り替えれば作業を続けられます。ただしモデルごとにプロンプトキャッシュが別なので、次のリクエストはキャッシュヒットなしで会話全体を読み直します。あわせて、対話セッションでリセットを待って自動継続できることと、その表示・キャンセル方法への導線が加わりました（v2.1.234 より前は待機が提供されませんでした）— [English](https://code.claude.com/docs/en/errors#youve-hit-your-session-limit)
- 組織のポリシーチェックが拒否したリクエストが、拒否メッセージを載せた `API Error:` 行として出ることが自動リトライの節に加わりました。管理者が Claude Enterprise の Inference hooks で設定するもので、メッセージ末尾は管理者が設定した指示（既定では管理者に連絡するよう促す文）になります。拒否はリクエストの内容に関するものなので、Claude Code は同じモデルにもフォールバックモデルにも再送しません。v2.1.239 より前は、ストリーミングなしやフォールバックモデルで再送してから拒否を表示することがありました。モデル設定のページのフォールバック条件にも同じ例外が加わっています — [English](https://code.claude.com/docs/en/errors#automatic-retries)
- 自己署名証明書のエラーメッセージに `Check your proxy or corporate SSL certificates` が付きました — [English](https://code.claude.com/docs/en/errors#ssl-certificate-errors)
- Desktop アプリの **Auto-continue when limits reset** チェックボックスと、CLI の `/config` にある **Continue automatically at usage limit** は別物なので個別にオフにする必要がある、と明記されました — [English](https://code.claude.com/docs/en/errors#youve-hit-your-session-limit)
- コスト管理のページに、管理者向けの案内として、開発者が v2.1.234 以降で自動継続を使えること、フリート単位で自動継続の開始可否を決めるには管理設定で `autoContinueAtUsageLimit` を設定することが加わりました。使用量上限の説明も、モデル切り替えが効く場合と効かない場合を整理する形に組み替えられています — [English](https://code.claude.com/docs/en/costs#plan-usage-breakdown)
- コンパクション後に何が残るかの表が書き直されました。plan mode で Claude が書いた計画はディスクから再注入され、`paths:` frontmatter を持つルールとサブディレクトリのネスト CLAUDE.md は「一致するファイルを読むたびに Claude Code が再読込する」となり、Claude が読んだ・編集したファイルを更新の新しい順に最大 5 件再読込する行が加わりました。5,000 トークンを超えるファイルは中身なしのパス参照として `Read` ではなく `Referenced file` の形で戻りますが、ルールは再読込されます。フックの行も「フックはコードなので該当なし」から、フックが以前に足したコンテキストは会話と一緒に要約される・`compact` ソースに一致する SessionStart フックは実行して出力を足す、の 2 行に分かれました。あわせて `/rewind` で **Summarize from here** / **Summarize up to here** を選び会話の一部だけコンパクトする導線も加わっています — [English](https://code.claude.com/docs/en/context-window#what-survives-compaction)
- ツールリファレンスの WebFetch の説明が書き直されました。Manual と `acceptEdits` モードで出るプロンプトの 3 択（**Yes** はこの 1 回だけ、**Yes, and don't ask again for `<domain>`** はそのリポジトリの `.claude/settings.local.json` に allow ルールを保存、**No, and tell Claude what to do differently** は拒否）が列挙され、`allowManagedPermissionRulesOnly` が設定されていると 2 番目が隠れること、`auto` と `bypassPermissions` は明示的な `ask` ルールに一致するドメインを除いてプロンプトを飛ばすこと、権限ルールが許可していても先に WebFetch のドメイン安全性チェックを通ることが加わりました。サンドボックス化されたコマンドは WebFetch の組み込み事前承認ドキュメントドメインを継承しない一方で、`WebFetch(domain:...)` の許可ルールはサンドボックスも尊重する、という関係も整理されています（詳細はハイライト 5 参照）— [English](https://code.claude.com/docs/en/tools-reference#webfetch-tool-behavior)
- セルフホスト環境のフックについて、運用者がランナーホストの `~/.claude/` から配ったフックに加えて、サーバー管理設定も MDM 配布の Claude Code ポリシーも管理層を供給しない場合に限り、ランナーイメージの管理設定ファイルのフックも実行されることが加わりました。同じ追記がフックリファレンスとクラウド環境の設定の両ページに入っています — [English](https://code.claude.com/docs/en/cloud-environments#what-carries-over-from-your-setup)
- 組織向けの MCP 制御のページで、用語が「設定ソース」から「設定スコープ」に統一され、管理スコープの許可／拒否リストは Claude Code が選んだ 1 つの管理ソースから取ることが明記されました — [English](https://code.claude.com/docs/en/managed-mcp#allow-claude-ai-connectors-alongside-the-managed-set)
- 設定のページで、リストキーのマージ規則の説明に `modelPicker` がモデル系リストキーの 3 つ目として加わりました。あわせて、リポジトリの設定ファイルでは無視されるキーの説明に `autoContinueAtUsageLimit` の例外が加わり、ユーザー設定・`--settings`・管理設定のどれもこのキーを設定していない間は、リポジトリのファイルがこの機能をオフにできることが示されました — [English](https://code.claude.com/docs/en/settings#where-settings-live)
- 管理設定のページで、管理層のマージ規則に `modelPicker`（後のものが丸ごと置き換える）が加わり、`disableCommandPluginSources` の一覧表に `headersHelper` のブロックが追記されました。組織向けセットアップのページでも、管理値が下位層を置き換えるキーに `modelPicker` が加わっています — [English](https://code.claude.com/docs/en/managed-settings#precedence-within-the-managed-tier)
- LLM ゲートウェイの接続とプロトコルの両ページに、`modelPicker` で `replaceBuiltInOptions` を使うとゲートウェイのモデル検出が見つけた名前もピッカーから消えること（現在のセッションが使っているモデルの行は残ります）が加わりました。トラブルシュートの「モデルがピッカーに出ない」の原因と対処にも同じ項目が入っています — [English](https://code.claude.com/docs/en/llm-gateway-connect#add-gateway-models-to-the-model-picker)
- モデル設定のページに `modelPicker` への導線が 3 か所加わりました。`availableModels` でピンした古いモデル ID が独立行として出る説明、複数モデルを並べたい場合の案内、`ANTHROPIC_CUSTOM_MODEL_OPTION` の行の並び順（組み込みの後、`modelPicker` の行はさらにその後）です。キャッシュ TTL への導線も 2 バケット版に差し替えられました — [English](https://code.claude.com/docs/en/model-config#available-models)
- プラグイン作成とプラグインリファレンスの `bin/` の説明に、組織設定経由で配るプラグインには含められない旨が加わりました（詳細は大幅更新 1 参照）。あわせて `claude plugin install` / `claude plugin update` の `-y, --yes` が、`command` ソースのコマンドだけでなくアーカイブダウンロードを認証する `headersHelper` の承諾もカバーすることが明記されました（`headersHelper` の承諾は v2.1.238 以降）— [English](https://code.claude.com/docs/en/plugins-reference#plugin-install)
- プラグイン依存のページに、`command` ソースまたは `headersHelper` を持つマーケットプレイスエントリの依存は自動インストールの対象外で、ユーザーが先に自分で入れる必要があることが加わりました。プラグインの探索のページにも、`headersHelper` を持つエントリはバックグラウンドの自動更新から外れ、`/plugin` の Errors タブに出ることが加わっています — [English](https://code.claude.com/docs/en/plugin-dependencies#declare-a-dependency-with-a-version-constraint)
- 権限モードのページで、`defaultMode` の JSON 例 2 つが別セクションへの導線に置き換えられ、`auto` がプロジェクト設定・ローカル設定で効かない説明から「Claude Code v2.1.142 以降」というバージョンの限定が外れました — [English](https://code.claude.com/docs/en/permission-modes#switch-permission-modes)
- ネットワーク設定のページで、GitHub まわりの記述が **GitHub allow lists and firewalls** という独立した見出しにまとめられました。GitHub Enterprise Cloud で IP 制限をかけている場合、GitHub App の IP 許可リスト継承を有効にするだけでなく、Anthropic の outbound IP アドレスを許可リストに追加する必要があることが加わっています。継承がカバーするのは Claude GitHub App がインストールとして出すリクエストだけで、ユーザーの代理で出すリクエストは対象外だからです。GitHub Enterprise Server のページでも、参照先が「Anthropic API IP addresses」から「outbound IP addresses」に改められました — [English](https://code.claude.com/docs/en/network-config#github-allow-lists-and-firewalls)
- VS Code のページで、ステータスバーの **✱ Claude Code** をクリックする導線に条件が付きました。`preferredLocation` を `sidebar` にしているか **Claude Code: Open in Side Bar** で開いた場合に出るもので、2 か所とも同じ書き足しです。Focus view については、Claude の保留中の質問が対象にしているテキストが残る挙動が v2.1.225 以降であることが分けて書かれ、Toggle Focus view のキーバインドにも v2.1.221 以降が必要である旨が追記されました — [English](https://code.claude.com/docs/en/vs-code#extension-settings)
- セッション管理のページに、セッションピッカーの復帰先の例外が加わりました。同じリポジトリの別 worktree のセッションはその場で再開しますが、そのセッションの worktree が既に無い場合は現在のディレクトリで再開します。無関係なプロジェクトのセッションは `cd` と再開コマンドをクリップボードにコピーしますが、そのディレクトリが既に無い場合は失敗する `cd` をコピーせず現在のディレクトリで再開します — [English](https://code.claude.com/docs/en/sessions#where-the-session-picker-looks)
- worktree のページで、`**/` で始まるパターンが、まるごと gitignore されたディレクトリの中身をコピーする条件が明記されました。そのディレクトリ自身がパターンに一致するか、`**/` の次の名前がディレクトリのパス上の名前と一致する場合に限ります（`**/.claude/skills/*.md` なら `.claude` が一致するのでコピーされます）。届かない場合は `vendor/**/config.json` のようにディレクトリ名を書きます。v2.1.239 より前は前者の場合しかコピーしませんでした — [English](https://code.claude.com/docs/en/worktrees#copy-gitignored-files-into-worktrees)
- Agent SDK のスキルのページで、プロジェクト・パーソナルスキルの `allowed-tools` frontmatter が SDK セッションでも適用されるようになりました。従来は CLI を直接使うときだけ効き、SDK では `allowedTools` オプションで管理するよう案内されていましたが、今回から frontmatter が効き、`allowedTools` は追加の事前承認手段という位置づけになっています。不正な形式やワイルドカード形式のスキル名を Claude Code の起動前に弾くチェックは、TypeScript Agent SDK 0.3.221 / Python Agent SDK 0.2.129 以降です — [English](https://code.claude.com/docs/en/agent-sdk/skills#pre-approve-tools-for-skills)
- Agent SDK の Python リファレンスで、既存フィールドに必要な SDK バージョンの注記が付きました。`parent_agent_id` と `forward_subagent_text` が 0.2.140 以降、`resume_session_at`・`resume_drops_turn`・`origin`・会話の差し替えイベントが 0.2.137 以降、`skills` の名前検証が 0.2.129 以降です。`resume_drops_turn` は従来「Claude Code v2.1.223 以降が必要、同梱の CLI は条件を満たす」と書かれていましたが、「Python Agent SDK 0.2.137 以降かつ Claude Code v2.1.223 以降が必要で、その SDK に同梱される CLI は Claude Code 側の条件を満たす」に改められました — [English](https://code.claude.com/docs/en/agent-sdk/python#claudeagentoptions)
- Agent SDK のツール検索で、コンパクション時の挙動が「以前に見つけたツールが外れることがあり、必要に応じて再検索する」から「SDK が古いメッセージをコンパクトしても、見つけたツールは読み込んだままにする」に変わりました — [English](https://code.claude.com/docs/en/agent-sdk/tool-search#how-tool-search-works)
- Claude apps ゲートウェイの設定で、`cli` に書く管理設定はサーバー管理設定の**代わりに**管理層へ適用されるため、`policyHelper` や `wslInheritsWindowsSettings` のように OS レベルのポリシーソースに限定された設定は無視されることが明記されました — [English](https://code.claude.com/docs/en/claude-apps-gateway-config#managed)
- コマンドリファレンスで、`/config` の `key=value` 形式はパネルでの確認が要る設定（`autoContinueAtUsageLimit` など）をオンにはできないがオフにはできる、と明記されました。`/config --help` の説明も「設定可能な全キーとその選択肢を列挙」から「受け付けるキーを列挙」に改められています。`/usage` の説明はプラン使用量の内訳への導線に簡潔化されました — [English](https://code.claude.com/docs/en/commands#all-commands)
- Google Cloud の Agent Platform のページで、レート制限の引き上げに関する案内が独立した段落に分けられました — [English](https://code.claude.com/docs/en/google-vertex-ai#additional-resources)

**その他**

- クイックスタートの表で、`claude "task"` の説明が「1 回限りのタスクを実行」から「最初のプロンプト付きで対話モードを開始」に訂正されました。実際の挙動に合わせた修正です — [English](https://code.claude.com/docs/en/quickstart#essential-commands)
- 今回も表の区切り行の桁揃えの入れ替えが差分行数を膨らませています。空白を無視して数え直すと、Agent SDK の Python リファレンスは 134 行から 22 行、フックリファレンスは 74 行から 18 行、フックのガイドは 67 行から 13 行、プラグインリファレンスは 52 行から 12 行、管理設定は 43 行から 5 行になります。実質 50 行を超えたのは大幅更新に挙げた 3 ページだけでした
- ページ見出しマップ（`claude_code_docs_map.md`）に差分がありません。`modelPicker`・`promptCacheTtl` などの新設節や、インタラクティブモードの使用量上限の待機の節がマップに反映されていないため、マップだけを見ていると今回の新設節を取りこぼします

## 新着情報

（今回の対象期間に新着情報ページの追加・更新はありません。前回のサマリで扱った Week 34（2026年08月17日～21日）が最新のままです）

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-08-22.md](./archives/latest/2026-08-22.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-08-22.md](./archives/latest-detail/2026-08-22.md)

<!--
base_commit: 38adb8c17987c2872a55345390bf77b43146ab00
head_commit: 961fa881bd3d4366c49a34b34508be3172b7c2fc
generated_at_full: 2026-08-25T15:13:17+09:00
-->
