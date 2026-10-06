---
対象期間: 2026年10月04日 〜 2026年10月05日
作成日: 2026-10-05
---

# Claude Code 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
**今回は HIPAA 設定のもとで Claude Code をローカルで使うための準備ページが新しく加わり、changelog には v2.1.290（2026年10月05日、190 項目）が積まれました**。以前の Claude Code in Slack が Pro・Max だけのものになったことや、デスクトップアプリのコードレビューの仕組みの変更も載っています。ページ単位で数えると 221 ページ中 83 ページが変わり、変更は 1,139 行（追加 900・削除 239）です。総行数は 112,013 行から 112,678 行に増えました。

主要なものを以下に挙げます。

1. HIPAA 設定のもとで Claude Code をローカルで使うための準備ページができ、関連する十数ページにも反映された
2. 以前の Claude Code in Slack が Pro と Max のアカウントにだけ応答するようになり、2026年10月05日付の廃止の通知が載った
3. Agent SDK で、セッションの状態を知らせる session_state_changed メッセージが使えるようになった
4. Claude の推論の再現を求めたとして API に断られた場合（reasoning_extraction）の対処が載った
5. デスクトップアプリのコードレビューが、/code-review とレビュー結果のカードに替わった
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**HIPAA 設定のもとで Claude Code をローカルで使うための準備ページができた**](#1-hipaa-設定のもとで-claude-code-をローカルで使うための準備ページができた):  
  Claude Enterprise の HIPAA 設定に向けて、接続方法の確認・版の更新・ネットワーク・管理設定・ローカルデータの扱いをまとめた管理者向けのページです。ZDR・Remote Control・Code Review などのページにも、HIPAA 設定のもとでの扱いが加わりました
2. [**以前の Claude Code in Slack が Pro と Max だけの応答になり廃止の通知が載った**](#2-以前の-claude-code-in-slack-が-pro-と-max-だけの応答になり廃止の通知が載った):  
  以前の Claude Code in Slack は、Claude Tag に接続していないワークスペースで Pro・Max のアカウントにだけ応答します。Claude Tag に接続したワークスペースでは「2026年10月05日付で廃止」の通知が返ります
3. [**Agent SDK でセッションの状態を知らせる session_state_changed メッセージが加わった**](#3-agent-sdk-でセッションの状態を知らせる-session_state_changed-メッセージが加わった):  
  `CLAUDE_CODE_EMIT_SESSION_STATE_EVENTS=1` を設定すると、`running`・`idle`・`requires_action` のいずれかを運ぶメッセージがストリームに加わります
4. [**Claude の推論の再現を求めたとして断られた場合の対処が載った**](#4-claude-の推論の再現を求めたとして断られた場合の対処が載った):  
  拒否のメッセージに `` Details: `[reasoning_extraction]` `` の行があれば、思考をそのまま書き出させる指示を CLAUDE.md・スキルなどから外します
5. [**デスクトップアプリのコードレビューが /code-review とレビューのカードに替わった**](#5-デスクトップアプリのコードレビューが-code-review-とレビューのカードに替わった):  
  差分ビューの **Review code** ボタンの代わりに、プロンプトボックスで `/code-review` を使います。ローカル・SSH・WSL のセッションでは結果がファイルごとのカードにまとまり、差分の中で 1 件ずつ直せます
<!-- light:highlight-list:end -->

## 1. HIPAA 設定のもとで Claude Code をローカルで使うための準備ページができた

**新しいページ `hipaa-setup` が加わりました**（詳しくは新規追加 1）。HIPAA 設定は、保護対象医療情報（PHI）を扱い Anthropic と BAA を結んだ Claude Enterprise の組織向けの組織設定で、Claude Code（ローカルモード）と Cowork（ローカルモード）に適用され、両方の機能を制限します。設定を適用するのは Primary Owner で、このページは開発者のコンピューターを準備する IT・セキュリティの管理者向けです。

**ほかのページにも、HIPAA 設定のもとでの扱いが書き加えられました。**

- **BAA の対象**: `legal-and-compliance` の「Healthcare compliance (BAA)」は、BAA が Claude Code に及ぶ形を「HIPAA 設定」（Claude for Enterprise のアカウントで使う CLI か Claude Desktop の Code タブ）と「Zero Data Retention」の 2 つに分けました。HIPAA 設定では、クラウドのセッション・Remote Control・モバイルアプリの Claude Code・サードパーティのクラウドプロバイダーやゲートウェイを経由する Claude Code は対象外です。`zero-data-retention` にも、HIPAA 設定を適用すれば ZDR なしで CLI と Code タブを BAA の対象にできる、と加わりました
- **使えなくなるもの**: クラウドのセッションと `/web-setup`（`claude-code-on-the-web`・`web-quickstart`）、Remote Control（`remote-control`。`/status` の `Organization configuration` の行に `HIPAA` と出る）、Code Review と ultrareview（`code-review`・`ultrareview`。Code Review は BAA の対象外とも明記）、セルフホストの環境（`self-hosted-environments`）、フィードバックのツール（`tools-reference`）が、HIPAA 設定を適用した組織では使えないと書かれました。`feature-availability` にも、HIPAA 設定を適用した Enterprise の組織では表の一部の機能がオフになる、と加わっています
- **既定でオフになるもの**: Claude in Chrome は HIPAA を有効にした Enterprise の組織では既定でオフで、Owner がオンにできますが、Chrome から第三者のサイトに送るデータは BAA の対象外です（`chrome`）。デスクトップアプリの **Desktop** のトグルも既定でオフで、HIPAA 設定を適用するとオンでもオフに戻ります（`desktop`）
- **ローカルのデータ**: HIPAA 設定が適用されるセッションでは、Desktop と Cowork のトランスクリプトも `cleanupPeriodDays` で消え、`history.jsonl` も掃除のたびに `cleanupPeriodDays` より古い項目が消えます（`claude-directory`）
- **フックの環境**: HIPAA 設定が適用されるセッションでは、フックの環境からも Anthropic の資格情報が取り除かれます（`hooks`）
- `admin-setup` の組織の制御の表にも「HIPAA configuration」の行が加わり、ゲートウェイを通るセッションは HIPAA 設定の対象にならないことが加わりました

- [HIPAA 対応組織向けに Claude Code（ローカルモード）をセットアップする - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/hipaa-setup#check-how-developers-sign-in-and-connect)
- [Set up Claude Code (local mode) for a HIPAA-ready organization - Claude Code Docs (English)](https://code.claude.com/docs/en/hipaa-setup#check-how-developers-sign-in-and-connect)
- [法的および規制対応 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/legal-and-compliance#healthcare-compliance-baa)
- [Legal and compliance - Claude Code Docs (English)](https://code.claude.com/docs/en/legal-and-compliance#healthcare-compliance-baa)

## 2. 以前の Claude Code in Slack が Pro と Max だけの応答になり廃止の通知が載った

**`slack` の冒頭の説明が「Team と Enterprise では廃止予定」から、応答する相手の条件に変わりました。** 以前の Claude Code in Slack は、どの組織も Claude Tag に接続していない Slack のワークスペースで、Pro と Max のアカウントからのチャンネルでのメンションにだけ応答します。前提条件の表も、Claude のプランが「Pro, Max, Team, or Enterprise」から「Pro or Max」になり、「Slack workspace」の行（どの組織にも Claude Tag に接続されていないこと）が加わりました。`llms.txt` の説明文も同じ内容に改められています。

トラブルシューティングには、@Claude が回答の代わりに返す 2 つの通知の節ができました。

- **「This workspace isn't set up for Claude Tag yet」**: ワークスペースが Claude Tag に接続されておらず、かつ Slack でリンクした Claude のアカウントが Pro・Max でない場合に返ります。Claude Tag は Team と Enterprise で使えるので、通知にある `@Claude connect` のコマンドから接続を始めます
- **「The legacy Claude in Slack bot is retired」**: 通知は `The legacy Claude in Slack bot is retired effective October 5, 2026 and no longer responds in channels.` で始まります。ワークスペースが Claude の組織に接続されているのに、その組織の Claude Tag の設定で、チャンネル・ワークスペース・組織の既定のどこかに以前の版がまだ選ばれている場合です。自分のプランに関係なく、Pro・Max のアカウントにも返ります。Owner なら Claude の管理設定でチャンネルの Claude Tag をオンにし、設定を継承するチャンネルをまとめて直すにはワークスペースか組織の既定で変えます

`platforms`・`remote-control`・`feature-availability`・`claude-tag` でも、Slack の行や説明に「Pro と Max のプラン」「Claude Tag に接続していないワークスペース」の条件が加わりました。

- [Slack での Claude Code - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/slack#the-legacy-claude-in-slack-bot-is-retired)
- [Claude Code in Slack - Claude Code Docs (English)](https://code.claude.com/docs/en/slack#the-legacy-claude-in-slack-bot-is-retired)

## 3. Agent SDK でセッションの状態を知らせる session_state_changed メッセージが加わった

**TypeScript の SDK のリファレンスに `SDKSessionStateChangedMessage` の節ができました。** `CLAUDE_CODE_EMIT_SESSION_STATE_EVENTS=1` を設定すると、Claude Code がセッションの状態を報告するたびに `type: "system"`・`subtype: "session_state_changed"` のメッセージが届きます。同じ状態を何度も報告することがあるので、遷移ではなく「今の状態」として読むよう案内しています。

- **`running`**: セッションが作業中
- **`idle`**: Claude Code が次のプロンプトを待っている
- **`requires_action`**: 権限のプロンプトなど、セッションがホストに送った要求への答えを待って止まっている

ターンの `idle` と `result` のメッセージはどちらが先に届くこともあります。`idle` がバックグラウンドのサブエージェントやワークフローの実行を待つかどうかは `CLAUDE_CODE_BG_TASKS_REPORT_RUNNING` で変えられます。

**Python の SDK では、専用のデータクラスのないサブタイプとして `SystemMessage` で届きます。** `message.data["state"]` を読み、`receive_response()` は `ResultMessage` で止まって後から来る `session_state_changed` を取りこぼすので、`receive_messages()` で回すよう書かれています。`env-vars` の表にも変数が加わり、Agent SDK か、`--print`・`--output-format stream-json`・`--verbose` の組み合わせが必要とされています。

- [Agent SDK リファレンス - TypeScript - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/agent-sdk/typescript#sdksessionstatechangedmessage)
- [Agent SDK reference - TypeScript - Claude Code Docs (English)](https://code.claude.com/docs/en/agent-sdk/typescript#sdksessionstatechangedmessage)

## 4. Claude の推論の再現を求めたとして断られた場合の対処が載った

**`errors` に「Safeguards flagged a request for Claude's reasoning」の節ができました。** モデルに内部の推論を応答の中で再現させようとしているとセーフガードが判断すると、API はリクエストを断ります。API はこの拒否のカテゴリを `reasoning_extraction` と呼び、拒否のメッセージには `` Details: `[reasoning_extraction]` `` の行が入ります（v2.1.234 より前の拒否のメッセージには `Details` の行がありませんでした）。メッセージから節を引く表と、Usage Policy の拒否・サイバーセキュリティの話題の拒否の節からも、この行があればこちらを見るよう案内が加わっています。

対処は次のとおりです。

- 思考や推論を逐語的に、または `<thinking>` の節・スクラッチパッドの節・JSON の `reasoning` フィールドのような決まった形で書き出させる指示を外すか言い換えます。指示はプロンプトだけでなく、CLAUDE.md・スキル・サブエージェントのプロンプト・出力スタイル・MCP のツールの説明など、Claude Code が一緒に読み込むものにある場合もあります
- どのカスタマイズが原因かは、`claude --safe-mode` でカスタマイズを外したセッションを始めて同じプロンプトを送ると確かめられます。カスタマイズを変えたら新しいセッションを始め、送ったプロンプトの言い換えには巻き戻しを使います
- 答えの説明自体は求められます。短い説明・結果の根拠・行った操作の要約を頼むか、思考の要約を見るには `showThinkingSummaries` を使います

- [エラーリファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/errors#safeguards-flagged-a-request-for-claudes-reasoning)
- [Error reference - Claude Code Docs (English)](https://code.claude.com/docs/en/errors#safeguards-flagged-a-request-for-claudes-reasoning)

## 5. デスクトップアプリのコードレビューが /code-review とレビューのカードに替わった

**`desktop` の「Review your code」が書き直されました。** これまでは差分ビューの右上の **Review code** をクリックすると、Claude が差分にコメントを残す仕組みでした。今後はプロンプトボックスに `/code-review` と入力し、レビューが終わると結果が会話に届きます。

- ローカル・SSH・WSL のセッションでは、結果がファイルごとにまとまった **Code review** のカードとして出ます。**Walk through in diff** で差分ビューを開いて 1 件ずつたどり、今の差分にある指摘はその行で **Fix this one** を押すか却下できます。**Apply fixes** は、まだ残っている指摘を Claude に直させます
- どのセッションでも、プロンプトボックスで Claude にレビューの指摘を直すよう頼めます。`/code-review` が何を見るかと引数は `code-review` の「Review a diff locally」を参照、とされ、「重大な問題だけを見てスタイルなどは指摘しない」という説明は消えました
- `desktop-quickstart` の「コミット前に変更を確かめる」も、**Review code** から `/code-review` に改められています

デスクトップアプリのそのほかの変更は大幅更新 2 にまとめています。

- [デスクトップアプリケーション - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/desktop#review-your-code)
- [Desktop application - Claude Code Docs (English)](https://code.claude.com/docs/en/desktop#review-your-code)

## 新規追加されたページ

<!-- light:new-pages:start -->
- [**Set up Claude Code (local mode) for a HIPAA-ready organization**](#1-set-up-claude-code-local-mode-for-a-hipaa-ready-organization) ([日本語](https://code.claude.com/docs/ja/hipaa-setup) / [English](https://code.claude.com/docs/en/hipaa-setup)):  
  HIPAA 設定に向けて開発者のコンピューターを準備する管理者向けのページです。対象になる接続、必要な版（Claude Code v2.1.285 以降・Claude Desktop v2.19675.0 以降）、許可するホスト、管理設定の例、適用後の確認、ローカルのセッションデータの扱いをまとめています
<!-- light:new-pages:end -->

## 1. Set up Claude Code (local mode) for a HIPAA-ready organization

**`llms.txt` の「Security and data」と見出しマップに加わり、`llms-full.txt` にも本文が入りました**（ページ単位の差分で 267 行、すべて追加）。「(local mode)」はクラウドのセッションではないローカルのセッション、つまり端末の Claude Code、Claude Desktop の Code タブ、Claude Desktop の Cowork を指します。VS Code と JetBrains の拡張は含まれず、HIPAA 設定のもとでも動きますが BAA の対象外です。

- **準備（適用前）**: HIPAA 設定が効くのは、Claude Enterprise のアカウントでサインインして Claude API に直接つなぐセッションだけです。Amazon Bedrock・Agent Platform・Foundry・Claude Platform on AWS・Claude apps gateway、LLM ゲートウェイやほかの `ANTHROPIC_BASE_URL`、Enterprise のサインインのない `ANTHROPIC_AUTH_TOKEN`・`apiKeyHelper`、Console の API キーやフェデレーションの資格情報は対象外です（企業の HTTPS プロキシを通すのは対象のまま）。接続は `/status` の `Login method`・`Organization`・`API provider`・`Anthropic base URL` の行で確かめます
- **版**: Claude Code v2.1.285 以降と Claude Desktop v2.19675.0 以降が要ります。古い版では、Claude Code はリクエストごとに `API Error` になり、Desktop には **Update required** のダイアログが出ます
- **ネットワーク**: `api.anthropic.com`（API・テレメトリ・HIPAA 設定を伝える組織のポリシー）、`claude.ai`・`claude.com`・`platform.claude.com`（サインイン）、`downloads.claude.ai`（ネイティブのインストーラー）、`mcp-proxy.anthropic.com`（claude.ai のコネクタ）を 443 で許可します。ポリシーは起動時と、使用中は約 1 時間ごとに取得されます
- **管理設定の例**: `forceLoginMethod: "claudeai"`・`forceLoginOrgUUID`・`allowedProviders: ["anthropic"]`・`cleanupPeriodDays` の 4 つのキーです。`forceLoginOrgUUID` が組織 ID と違うと全員が起動時に終了するので、配る前に確かめるよう警告しています。Console のサインイン、サーバー管理の設定、v2.1.285 より前の版（`requiredMinimumVersion` に `"2.1.285"` を足せば v2.1.163〜v2.1.284 は起動を拒む）は、これらのキーでは止まりません
- **適用後の確認**: 起動時の `Per your organization's policy, some features are limited · /status for details`、フッターの `HIPAA configured`（v2.1.286 より前は `HIPAA`）、`/status` の `Organization configuration` の `HIPAA` を確かめます。Code タブはオフになるので、使うなら Owner が **Desktop** のトグルをオンに戻します。出ない場合は、アカウントや接続、ポリシーの取得（`Organization policy` の行と `claude doctor`）、まだ適用されていない可能性、の順に調べます
- **開発者から見た変化**: WebFetch が使えない（Web 検索は使える）、`--cloud`・`/teleport`・Remote Control が拒否される、`/feedback`・`/bug` がない、アーティファクトを公開できない、Claude Code が起動するシェルのコマンド・フック・MCP サーバーの環境から `ANTHROPIC_API_KEY`・`ANTHROPIC_AUTH_TOKEN` などが消える（クラウドプロバイダーと GitHub の資格情報は残る）、別の組織に `/login` しても再起動まで制限が残る、などです
- **ローカルのデータ**: データの保護と削除は組織の責任です。保持の掃除は誰かが Claude Code を起動したときだけ動きます。HIPAA 設定のもとでは Claude Desktop が `cleanupPeriodDays` より長く使われていない Code タブのセッションを（スター付きも含めて）消します。すぐ消すには v2.1.288 以降で `claude purge --all --yes`（v2.1.126〜v2.1.287 は `claude project purge`）を使い、残る `paste-cache/` などは手で消すか、コンピューターをワイプします

- [HIPAA 対応組織向けに Claude Code（ローカルモード）をセットアップする - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/hipaa-setup#deploy-managed-settings)
- [Set up Claude Code (local mode) for a HIPAA-ready organization - Claude Code Docs (English)](https://code.claude.com/docs/en/hipaa-setup#deploy-managed-settings)

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
- [**Give Claude custom tools**](#1-give-claude-custom-tools) ([日本語](https://code.claude.com/docs/ja/agent-sdk/custom-tools#make-a-parameter-optional) / [English](https://code.claude.com/docs/en/agent-sdk/custom-tools#make-a-parameter-optional)):  
  88 行（追加 76・削除 12）が変わりました。フィールドに説明を付ける方法と、パラメーターを省略可能にする節ができ、Python の例が JSON Schema の形になりました
- [**Desktop application**](#2-desktop-application) ([日本語](https://code.claude.com/docs/ja/desktop#monitor-pull-request-status) / [English](https://code.claude.com/docs/en/desktop#monitor-pull-request-status)):  
  55 行（追加 31・削除 24）が変わりました。コードレビュー（ハイライト 5）のほか、ペインを開くボタンがタイトルバーに移り、CI の自動修正がレビューのコメントにも対応しました
<!-- light:updated-pages:end -->

`llms-full.txt` から切り出したページ単位の差分（`git diff --no-index --numstat`）が 50 行以上の既存ページを挙げています。`agent-sdk/custom-tools` の行数には `<Tabs>` の枠組みの行も含まれますが、連続する空白とハイフンを潰して数え直しても 88 行で変わりません。changelog（193 行、すべて追加）は、これまでどおり「軽微な更新」で扱います。`slack`（30 行）と `agent-view`（29 行）は閾値に届かないため、それぞれハイライト 2 と「軽微な更新」で扱います。

## 1. Give Claude custom tools

- **入力のスキーマの説明**: 言語ごとの書き方に分かれました。TypeScript は Zod のフィールドで `.describe()` を呼ぶと、Claude が見る説明が付きます。Python は `{"latitude": Annotated[float, "Latitude coordinate"]}` のように型を `Annotated` で包むと説明が付きます。天気のツールの例も `Annotated` を使う形になりました
- **「Make a parameter optional」**: ヒントだった内容が小節になり、クイックリファレンスの表にも行が加わりました。TypeScript は Zod のフィールドに `.optional()` を付けます。Python の dict のスキーマはすべてのキーを必須にするので、JSON Schema の形を使って `required` から外し、`args.get()` で読みます（これまでは「スキーマから外して説明文で触れる」方法でした）。省略可能なキーのある型付きのスキーマは、Python のリファレンスの TypedDict の形を見るよう案内しています
- **`get_precipitation_chance` の例**: Python 版が JSON Schema の形になり、`hours` に `integer`・`minimum: 1`・`maximum: 24`・`description` が付いて `required` からは外れました
- **実行の手順**: HTTP を使う Python の例は httpx を使うので、`uv add httpx` か `pip install httpx` で追加するタブが加わりました。例の実行も `npx tsx weather.ts`・`uv run weather.py`・（SDK を入れた仮想環境を有効にしてから）`python weather.py` のタブになっています

**Python の SDK のリファレンス（`agent-sdk/python`）の「Input schema options」**にも 3 つ目の形「TypedDict class」が加わりました。`NotRequired` のキーは `required` から外れます。Python 3.11 以降は `typing` から、3.10 は SDK が入れる `typing_extensions` から `TypedDict` と `NotRequired` を読み込みます。単純な対応付けと TypedDict の形では、`Annotated[type, "description"]` で説明を付けます。

- [Claude にカスタムツールを提供する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/agent-sdk/custom-tools#make-a-parameter-optional)
- [Give Claude custom tools - Claude Code Docs (English)](https://code.claude.com/docs/en/agent-sdk/custom-tools#make-a-parameter-optional)
- [Agent SDK リファレンス - Python - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/agent-sdk/python#input-schema-options)
- [Agent SDK reference - Python - Claude Code Docs (English)](https://code.claude.com/docs/en/agent-sdk/python#input-schema-options)

## 2. Desktop application

コードレビューはハイライト 5 のとおりです。このほか次の変更がありました。

- **PR の CI の監視**: トグルの名前が **Auto-fix CI & address comments** と **Auto-merge when ready** になりました。前者はローカルのセッションでは、自分以外の人が残した新しいレビューのコメントにも対応します（書いた人がリポジトリのオーナー・組織のメンバー・コラボレーター・GitHub App の場合）。オンにするにはステータスバーの **CI** をクリックします
- **ペインの開き方**: セッションのツールバーの **Views** メニューの代わりに、セッションのタイトルバーの **Terminal**・**Changes**・**Browser** のボタンでターミナル・差分・Browser のペインを開きます。横の **⋮** メニューからは **Files** などほかのペインを開け、ウィンドウが狭いときはボタンもここに入ります。タスクのペインは、バックグラウンドの作業があるときに **⋮** の **Background tasks** から開きます。`desktop-ios-simulator` でも、iOS のアプリの作業を検出するとタイトルバーに **iOS Simulator** のボタンが出る、と改められました
- **Browser のペイン**: 開発サーバーの開始・停止はペインの見出しの **Dev servers** メニューに、Cookie を残すかは **⋮** の **Keep cookies** に、保存したデータの消去は **⋮** の **Clear browsing data** に、自動の検証のオフは **⋮** の **Auto-verify changes** に移りました。Browser を完全に止めるには **Settings > Claude Code** の **Browser tools** をオフにします。チャットの外部のリンクを初めてクリックしたときに開き先を尋ね、後から **⋮** の **Open links in built-in browser** で変えられます
- **SSH の接続の追加**: プロンプトボックスの環境のドロップダウンから **SSH > Add SSH connection…** を選びます。欄の名前が **SSH host**・**SSH port**・**SSH key (optional)** になり、鍵の例は `~/.ssh/id_ed25519`、空欄なら SSH の設定か SSH エージェントを使います
- **管理画面の設定**: トグルの名前が **Desktop** と **Cloud sessions** になり、「Disable Bypass permissions mode」の項目は一覧から消えました。HIPAA を有効にした組織での既定は、ハイライト 1 のとおりです
- クラウドのセッションが作ったブランチは、ブランチ名をクリックして **Copy branch name** で写します

- [デスクトップアプリケーション - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/desktop#monitor-pull-request-status)
- [Desktop application - Claude Code Docs (English)](https://code.claude.com/docs/en/desktop#monitor-pull-request-status)

## 軽微な更新

<!-- light:minor-updates:start -->
今回の差分は **3 ファイル**（`llms-full.txt`・`llms.txt`・見出しマップ）です。`llms-full.txt` をページ単位に切り出して数えると、221 ページ中 **83 ページ**（新規 1 ページを含む）が変わり、変更は 1,139 行（追加 900・削除 239）でした。新規の 1 ページと大幅更新の 2 ページを除く **80 ページ**（changelog を含む）と、changelog に加わった **v2.1.290**（2026年10月05日、190 項目。Fixed 131・Changed 25・Improved 19・Added 15）を以下にまとめます。changelog の項目は単一のリリースなので、各項目への版の併記は省きます。`llms-full.txt` の総行数は **112,013 行から 112,678 行へ 665 行増え**ました。

**新機能**

- **mod の `turn.step` フックの結果に `serverToolUses` を追加**。API 自身が実行したツール呼び出し（advisor）を、ID・名前・入力・開始と終了付きで示します
- **プラグインのフックの `tool.check` イベントに `agentId` を追加**。サブエージェントの権限の確認とメインのセッションの確認を見分けられます
- **mod の `tool.check` フックが読む質問と判定に `ceiling` を追加**。組織がそのツールに求める承認を示します
- **プラグインのフックの型定義に `ThemeKey` と `Color` の型を追加**。mod の描画が使えるテーマの色をエディターが一覧できます
- **`claude plugin validate` で、mod がゲートの箇所に登録した各フックと `.catch` の有無を一覧するようにした**（`--json` では `gatingHooks`）
- **Claude apps gateway のサインインの承認ページに Deny ボタンを追加**。保留中のサインインを終わらせ、待っている端末は数秒で止まります
- **`claude attach <name>` と `claude logs <name>` を追加**。ID の代わりに実行中のセッションの名前の一部を使えます（`agent-view`・`cli-reference` にも追記） — [日本語](https://code.claude.com/docs/ja/agent-view#manage-sessions-from-the-shell) / [English](https://code.claude.com/docs/en/agent-view#manage-sessions-from-the-shell)
- **`/claude-api managed-agents-onboard <url>` を追加**。ページが説明する Managed Agents のパターンを `ant apply` のファイルとして用意します
- **`/claude-api managed-agents-onboard <quickstart-name>` を追加**。`deep-researcher` などの Console のクイックスタートのテンプレートを `ant` CLI で組み立てます
- **管理設定のファイルが管理設定のフォルダーの外を指すリンクのとき、警告を出すようにした**
- **管理設定がユーザーの設定したサンドボックスの `allowRead` のパスや許可したドメインを無視するとき、/status と doctor で警告を出すようにした**
- **[VS Code] Claude の作業中にメッセージを送ると、スクリーンリーダーに「Message queued.」と読み上げるようにした**
- **[VS Code] Manage plugins のダイアログから、マーケットプレイスのインストール・更新のコマンドを確かめて実行できるようにした**
- **[Claude Tag] Slack に fast モードを追加**。`!fast` でスレッドを fast モードに切り替え（必要なら Opus に移る）、`!fast off` で戻します。オンの間は返信に (fast) と出ます
- **[Claude Tag] アクセスバンドルのカスタムの接続に、任意の Path prefixes の欄を追加**。許可ルールをホスト全体ではなく、そのパスだけにできます
- **`CLAUDE_CODE_GZIP_REQUEST_BODIES` が載った**。`0` にすると `api.anthropic.com` に送る Claude API・テレメトリ・アーティファクトの公開のリクエストの本文の gzip 圧縮を止めます。既定では直接の接続で大きな本文を圧縮し、プロキシ・クライアント証明書・`NODE_EXTRA_CA_CERTS` があるときは圧縮しません。Claude Code が検出できない TLS 検査のプロキシが圧縮を扱えない場合に使います（`network-config` にも追記） — [日本語](https://code.claude.com/docs/ja/env-vars#variables) / [English](https://code.claude.com/docs/en/env-vars#variables)

**機能改善**

- **ネットワークのプロキシの背後での MCP の起動を改善**。プロキシがブロックする（HTTP 403）サーバーを 3 回再試行しなくなりました
- **バックグラウンドのエージェントからの権限のプロンプトに、バックグラウンドのエージェントをすべて止める Ctrl+X Ctrl+K を表示するようにした**
- **組み込みの `plugin-authoring` スキルを改善**。作った mod を別の人が入れるための 1 つのコマンドを示し、README のインストールの節に書きます
- **デスクトップアプリの Code タブでの `/plugin` への返答が、そこでのプラグインのインストールと管理の場所を示すようにした**
- **Bash の変更ファイルの表示を改善**。git の merge・pull・checkout を含む連結したコマンドでは、完全な差分なしでファイルを一覧します
- **Claude apps gateway のログを改善**。上流のクラウドの資格情報や接続が失敗したとき、警告の末尾に原因を付けます
- **claude.ai にサインインせずにクラウドのセッションを始めたときのエラーを改善**。`claude auth login` と /login を示し、API キーの認証のせいにしなくなりました
- **Read ツールのバイナリファイルへのメッセージが、その形式を読めるスキルかシェルのコマンドを示すようにした**
- **git の設定ファイルが `/ultrareview` のアップロードを止めたときのエラーを、約半分の長さにし、問題のファイルの種類を示すようにした**
- **`/ultrareview` のアップロードがチェックアウトを拒むときのエラーを、既知の原因ごとに直し方付きのメッセージにした**
- **Claude apps gateway が、IdP に提示する証明書の期限切れまでの 30 日間に警告をログに出すようにした**
- **Claude in Chrome の `browser_batch` の呼び出しがタイムアウトとされるまでの時間を、60 秒から 90 秒にした**
- **Claude apps gateway のブラウザーのサインインのページを改善**。ブランドのフォント、中央寄せの配置、ダークモードに対応しました
- **大きなセッションの再開中の応答性を改善**。トランスクリプトの読み込み中もタイマー・入力・描画が動きます
- **/ と @ の候補の一覧で、選択中の行の先頭に ❯ を付けた**。色がなくても選択が分かります
- **[VS Code] Continue After Reload を改善**。VS Code が拡張を再起動した後に開き直したタブが、再起動で中断したステップも終えます
- **[VS Code] メッセージのファイルのピルで、ホバーするとプロジェクトのフォルダーからのパスを示すようにした**。同じ名前のファイルを見分けられます
- **[Claude Tag] 自分の Claude のプランの使用上限に達したときの DM の通知が、数秒以内に出てリセットの時刻を示すようにした**
- **[Claude Tag] 以前の Claude in Slack のアプリがセッションを始められないときの返信が、何が失敗し誰が直せるかを示すようにした**（全文はスレッドで 1 回だけ）
- **サブディレクトリの CLAUDE.md が読み込まれる条件が書き直された**。Claude がそのサブディレクトリのファイルに Read・Write・Edit のツールを使ったときに含まれ、サブディレクトリの `CLAUDE.md` そのものにこれらのツールを使っていた場合は、すでに会話にあるとしてこの方法では読み込まれません。トラブルシューティングにも、サブディレクトリの CLAUDE.md は `/context` の **Memory files** に出ず、読み込まれると端末に `Loaded` の行が出ること、試すにはシェルからファイルを作って Claude にそのサブディレクトリのファイルを読ませることが加わりました。`large-codebases`・`context-window`・`prompt-caching`・`debug-your-config`・`agent-sdk/claude-code-features` の説明も「Claude がそこを読むとき」から「オンデマンドで」に揃えられています — [日本語](https://code.claude.com/docs/ja/memory#how-claude-md-files-load) / [English](https://code.claude.com/docs/en/memory#how-claude-md-files-load)
- **`AGENTS.md` を読む組み込みのプラグインの ID が `cc-plugin-agents-md@builtin` と書かれた**。`pluginConfigs` の例のキーもこれに替わり、v2.1.285 より前の ID は `agents-md@builtin` で、v2.1.285 以降はどちらの ID のエントリも読む、と加わりました（`settings-reference` も同様） — [日本語](https://code.claude.com/docs/ja/memory#choose-which-instruction-files-load) / [English](https://code.claude.com/docs/en/memory#choose-which-instruction-files-load)
- **保護されたパスの `.claude` の例外が一覧になった**。Claude のワークツリー（`.claude/worktrees/`）と自動メモリの markdown に加え、今のセッションのプランのファイル（`~/.claude/plans/` か `plansDirectory`）、バックグラウンドのセッションの作業用ディレクトリ（`~/.claude/jobs/<id>/tmp/`）、`--restricted` なしのセッションでのサブエージェントのメモリ（`.claude/agent-memory/` など）の markdown が並びました — [日本語](https://code.claude.com/docs/ja/permission-modes#protected-paths) / [English](https://code.claude.com/docs/en/permission-modes#protected-paths)
- **`--max-budget-usd` は Claude Code のクライアント側の費用の見積もりと比べるので請求とは違いうる、と加わった**（`cli-reference`）。`agent-sdk/cost-tracking` にも、複数の呼び出しを合算した値もクライアント側の見積もりだと加わっています — [日本語](https://code.claude.com/docs/ja/cli-reference#cli-flags) / [English](https://code.claude.com/docs/en/cli-reference#cli-flags)
- **`--dangerously-load-development-channels` は確認のプロンプトを出すので対話型のセッションで効き、`-p` や Agent SDK では無視されてチャンネルが登録されない、と加わった**（`cli-reference`・`channels-reference`） — [English](https://code.claude.com/docs/en/channels-reference#test-during-the-research-preview)
- **mod は Desktop アプリでは v2.1.286 から動く、と加わった**。端末では v2.1.287 以降、Desktop では Code タブのローカルのセッションで `/status` の **Claude Code** の行で版を確かめます。`plugins/mods/admin` の既定でオンになる版も v2.1.286 に、`plugins/mods/troubleshoot` の見出しは「Your version is older than 2.1.287」から「Your version is too old」になりました — [日本語](https://code.claude.com/docs/ja/plugins/mods/overview#turn-mods-on-or-off) / [English](https://code.claude.com/docs/en/plugins/mods/overview#turn-mods-on-or-off)
- **フルスクリーンで Cmd・Ctrl を押してツールの出力のファイルのパスをクリックすると、ファイルを選んだ状態でファイルマネージャーが開く、と改められた**。Linux と WSL では `org.freedesktop.FileManager1` の D-Bus のインターフェースを持つファイルマネージャーが要ります。選択メニューの行にホバーするとポインターが出る、の記述は消えました — [日本語](https://code.claude.com/docs/ja/fullscreen#use-the-mouse) / [English](https://code.claude.com/docs/en/fullscreen#use-the-mouse)
- **`keybindings` の `Confirmation` のアクションの説明が改められた**。`confirm:nextField`（Tab）は `/fast` のダイアログで fast モードを切り替え、`confirm:previousField` と `permission:toggleDebug` は Claude Code が反応しないアクション（書いてある `keybindings.json` は有効なまま）、`confirm:cycleMode` の説明から「権限モードを切り替える」が外れました — [日本語](https://code.claude.com/docs/ja/keybindings#confirmation-actions) / [English](https://code.claude.com/docs/en/keybindings#confirmation-actions)
- **`/workflows` は実行が 1 つだけなら一覧を飛ばしてその実行を開く、と加わった**。進行状況の画面の説明からはトークンの合計と経過時間が外れ、実行の確認のプロンプトでは **Yes, run it** か **No** を選んで Tab を押すと答えにコメントを付けられる、と改められました（`workflows`）
- **エージェントビューの説明が改められた**（`agent-view`）。アイコンの `✻`・`✽` の形は「プロセスが動いている、またはセッションが入力を待っている」の意味に、`Ready for review` に移るのは「レビューが要るか失敗しているチェックのある PR があるとき」に、音声の入力は保持モードのときだけ（`voice-dictation` も同様）になりました。失敗と PR のあるセッションは常に表示する、の記述は消えています
- **Windows で更新の直後に `claude` が見つからなくなった場合は `claude.exe` をバックアップから戻す節を見る、と `troubleshoot-install` の「command not found」に加わった**。`plugins/troubleshooting` のリンク先も「Verify your PATH」に替わりました
- **巻き戻しのメニューの説明から「ターンの途中で加わったメッセージは並ばない」が外れた**（`checkpointing`。changelog の `/rewind` の修正に対応）
- **`interactive-mode` の vim の `G` の説明が「入力の末尾」から「最後の行の先頭」に改められた**
- **`env-vars` の `BETA_TRACING_ENDPOINT`・`ENABLE_BETA_TRACING_DETAILED` で、エンドポイントは OTLP/HTTP だと明記された**
- **`settings-reference` の `desktopSessionCleanupPeriodDays` は、`cleanupPeriodDays` が代わりに効く場合を `claude-directory` の「Cleaned up automatically」に任せる形になった**

**バグ修正**

- 1 つの beta のヘッダーを 400 以外のステータスで、または 2 つ目の beta と一緒に拒むプロキシやゲートウェイの背後でリクエストが失敗する問題を修正
- 画像が数百枚ある長いセッションが「Request rejected as unprocessable by the model」のエラーで止まる問題を修正
- Claude の思考中に API の出力のコンテンツフィルターが返信を止めると、ターンがすぐ終わる問題を修正。エラーを出す前に 1 回再試行します
- 再開したサブエージェントやチームメイトが実行中にメッセージを受け取ると、以前の思考とプロンプトキャッシュを失う問題を修正
- WebFetch が 100,000 文字を超えるページのテキストを黙って捨てる問題を修正。読み残した量を示し、`offset` で続きを読めます
- 応答がリストや引用を数千段に入れ子にするとクラッシュする（「Maximum call stack size exceeded」）問題を修正
- Claude の作業中に送ったプロンプトが `/rewind` の一覧に出ない問題を修正
- 会話をコンパクションすると、予定のタスク（間隔付きの `/loop`、リマインダー）が再開時に黙って戻らない問題を修正（この版以降のコンパクションが対象）
- フォアグラウンドで設定した予定のタスクが ← や `/background` の引き渡しの後に発火せず、繰り返しのタスクが再開・respawn・fork のたびに 1 回余分に動く問題を修正
- 構造化出力を届けた後に接続が切れると、ヘッドレスの `--json-schema` の実行が `success` の結果なのに `is_error: true` で 0 以外で終了する問題を修正
- plan モードで、サーバーが ask のポリシーを付けた読み取り専用でないコネクタのツールを auto モードの分類器が承認できた問題を修正
- 作業ディレクトリの外にシンボリックリンクしたプロジェクトの `CLAUDE.md`・ルール・`AGENTS.md` が、`permissions.blockReadsOutsideWorkingDirectories` や `Read` の deny ルールのもとでも読み込まれる問題を修正
- `xn--` のホストのラベルの中にワイルドカードがある URL の allow・deny のパターンが、プロセスごとに違う一致をする問題を修正
- 組織が提供する MCP サーバーが、サインインや再接続の後に自分のものとして一覧し直される問題を修正（ヘッドレスと SDK のセッションの遅れて届く結果も含む）
- Windows で `git stash create` が失敗すると `/ultrareview` が未コミットの変更を警告なしに落とし、`git add -N` のファイルを削除・移動した後は変更を拒む問題を修正
- macOS と Linux で、バックスラッシュを含むパスについての `plansDirectory` のプロジェクトルートの確認を修正
- 非常に長い Remote Control とクラウドのセッションで、返信がストリーミングではなく塊ごとに出ることがある問題を修正
- `claude daemon run` と `claude daemon logs` で、バックグラウンドのデーモンのログが端末の制御文字を画面に渡す問題を修正。`\uXXXX` のエスケープで表示します
- [セルフホストのランナー] 細工した非常に長いセッションのエラー出力の行で、ランナーが数秒固まる問題を修正
- `.catch` のあるプラグインのフックが、プロンプトやツール呼び出しでフックのワーカーを塞ぎ続けると、アンロードされて `.catch` も飛ばされる問題を修正
- 応答の途中のモデルのフォールバックで捨てられたツール呼び出しが、mod の `turn.step` の結果に並ぶ問題を修正
- Claude がメッセージやファイルを送った直後にコンテナが再起動すると、Cowork のクラウドのセッションの返信が終わらないことがある問題を修正
- トップレベルの関数と同じ名前のオプションを分割代入する hooks モジュールを、`claude plugin validate` とプラグインの読み込みが拒む問題を修正
- git の設定に `core.safecrlf=true` があると、`/ultrareview` が未コミットの変更のアップロードに失敗する問題を修正
- フラグが付いたメッセージを、設定に別の effort を保存したフォールバックのモデルで再試行すると、effort が変わる問題を修正
- [Windows] CRLF の改行で保存したスキルとコマンドの、複数行の `!` のシェルのブロックが失敗する問題を修正
- フルスクリーンでの検索中に `/permissions` のタブをクリックすると、強制終了するまで固まる問題を修正
- 会話のコンパクションが「null is not an object」のエラーで失敗することがある問題を修正
- auto モードで報告を返すサブエージェントについて、プラグインのフックが `turn.complete` で空の `answer` を読む問題を修正
- 再読み込みの失敗の後に更新すると、mod が何のメッセージもなくアンロードされる問題を修正。失敗の行に、前に読み込んだ版がアンロードされることを示します
- `next(e)` を呼んだ後にプロンプトを捨てる mod の `prompt.submit` フックが黙って無視される問題を修正。そのフックを名前付きで失敗として報告します
- 描画のたびに高さが変わるツリーで末尾を追う mod のペインや帯が、延々と再描画される問題を修正
- macOS と Windows で、読み取りの途中にすり替えたリンクを通じて、画像の読み取りが承認の範囲外のファイルを返せた問題を修正
- ユーザーが入れた mod が組織のプラグインをアンロードさせられる場合がある問題を修正。その mod の方をアンロードします
- `.mcp.json`・プラグイン・エージェントで宣言した一部の MCP のエントリに、`disableClaudeAiConnectors` と `allowedMcpServers` の URL のルールが効かない問題を修正
- 描画のたびにツリーの高さが変わる mod のインラインのペインが、延々と再描画される問題を修正
- 読み取りのブロックや `--restricted` のもとで、`@` メンションが読み取りの途中に変えたリンクを通じて作業ディレクトリの外のファイルを読めた問題を修正
- エージェントビューで Esc が「Press enter again to restart this session — it isn't responding」を確定してしまう問題を修正。Esc はセッションを開き直すだけになりました
- バックグラウンドのセッションが自分で作ったワークツリーに入ると、エージェントビューがそのセッションの `/loop` の実行回数・カウントダウン・ステータスの行を失う問題を修正
- 手動の権限モードの `claude agents` のセッションが、返信や新しいエージェントのプロンプトに貼った画像を読むのに承認を求める問題を修正
- `declare`・`typeset`・`export`・`readonly` に接頭辞として付けた変数から名前が来るコマンドやパスを、deny・ask ルールが見落とす問題を修正
- プロンプトに貼り付け・ドラッグした画像のパスや、@メンションしたフォルダーの一覧のファイル名に、Read の deny ルールが効かない問題を修正
- ユーザーが入れた mod が組織のガードの確認を飛ばさせられる場合がある問題を修正。そうした mod はアンロードします
- 非ラテン文字を含む長い複数行のテキストを mod が描くと、プラグインのフックが再描画のたびに止まる問題を修正
- エージェントビューでセクションの最下段のセッションを削除した後に Ctrl+X を繰り返すと、次のセクションをまるごと削除する問題を修正
- 「You should know」が `language` の設定にかかわらず英語でメモを書く問題を修正
- 非常に長いメッセージを送った後に固まる問題を修正
- 矢印・ダッシュ・罫線などの非 ASCII の文字を含む大きなツールの出力で、トランスクリプトの展開（ctrl+o）やリサイズが遅くなる問題を修正
- 保存されたトランスクリプトのないバックグラウンドのセッションに、`claude respawn` が以前のメッセージを送り直す問題を修正。空の会話で始めます
- エージェントビューで `n:` か Ctrl+F の検索の後に Esc を押すとフォーカスがセクションの見出しに移り、Ctrl+X を 2 回でセクションのすべてのセッションを削除できた問題を修正
- 停止中のセッションに届けられなかったスラッシュコマンドを `claude agents` が保存し、そのセッションの次の再起動時に勝手に実行する問題を修正
- git のフィルタードライバーの名前が `unset` か `unspecified` のファイルを、`/ultrareview` がフィルターせずにアップロードする問題を修正。アップロードを止め、ドライバーの名前を変えるよう求めます
- auto モードの拒否が、ツール全体の分類器を飛ばすルールや Claude Code が無視するルールを提案する問題を修正
- 追跡しているファイルを同じ名前のフォルダーで置き換えた場合に stash を選ぶと、`claude --teleport` と `/teleport` がそのフォルダーのファイルを削除する問題を修正。stash を拒み、理由を示します
- Esc がエージェントビューの「Press enter again to restart this session fresh」の確認を確定してしまう問題を修正
- `/clear` の後、エージェントビューの `/loop` の実行回数が止まりカウントダウンが消える問題を修正。新しい会話で数え直します
- `--channels` の権限の中継で、セッション内で繰り返された返信の ID が別のプロンプトを承認していた問題を修正。繰り返しは無視します
- Chrome への接続の失敗の後、`/chrome` の「Reconnect extension」がブラウザーのツールを戻さない問題を修正し、戻せない場合の説明を加えました（anthropics/claude-code#98135）
- Anthropic のアカウントを持たずゲートウェイ（`ANTHROPIC_BASE_URL` と `ANTHROPIC_AUTH_TOKEN`）経由で Claude を使う人で、mod がオフのままになる問題を修正
- バックグラウンドのセッションのクラッシュ直後に `claude agents` から送った返信が 2 秒で拒まれる問題を修正。セッションの再起動の間、最大 12 秒再試行します
- `claude agents` が実行中のセッションに届けられなかったスラッシュコマンドと選択式の質問への回答が保存され、次の再起動時に勝手に送られる問題を修正
- ヒアドキュメントを別のコマンドにパイプするサンドボックスのコマンド（`cat <<EOF | python3`）が、毎回承認を求める問題を修正
- Homebrew のアップグレードの後に `claude agents` が「Couldn't restart the background service」で失敗し、バックグラウンドのセッションが止まる問題を修正（この版の次のアップグレードから有効）
- エージェントビューの「restart this session fresh」が、空の会話で始めずにセッションの以前のメッセージを送り直す問題を修正
- シェルがまだワイルドカードとして展開する引数を持つ一部の読み取り専用のコマンド（`rg`・`git grep` など）を、Bash の権限の確認が自動で承認する問題を修正。承認を求めるようにしました
- アップグレードの後、古い保存済みの設定のせいで `claude plugin test` が実行を拒む問題を修正
- zsh が bash と違って読む変数名を持つ一部のコマンドを、Bash の権限の確認が自動で承認する問題を修正。承認を求めるようにしました
- `git clone` のオプションの短い形が、`sandbox.excludedCommands` の `git *` のようなパターンによるサンドボックスの除外を保つ問題を修正。長い形と同じに扱います
- セッションの最初の機能フラグの要求が、プロジェクトの設定のプロキシや API のエンドポイントを無視する問題を修正
- ブランチを `.git` の外に置くリポジトリ（git 2.54 以降）で、ローカルのブランチの `/ultrareview` が未コミットの作業を黙ってアップロードから外す問題を修正。説明付きで拒むようにしました
- コンテナの再起動で保留中の `/loop` の wakeup や予定のタスクが失われると、クラウドのセッションが眠ったままになる問題を修正。Claude に伝わり、予定し直せます
- 2025年11月の修正を含まない PostgreSQL の版で、Claude apps gateway の保持期間の掃除が、同時に更新された戻ってきた開発者の ID の行を削除する問題を修正
- サンドボックスの自動許可のもとで、サンドボックスの Monitor ツールのコマンドが権限のプロンプトを飛ばす問題を修正。権限ルールに従います
- IdP に提示する証明書の subject が空だと、Claude apps gateway が起動に失敗する問題を修正
- `store.postgres_url` を解析できないと Claude apps gateway が「Invalid URL」だけで終了する問題を修正。設定の名前と、URL に書けるものを示します
- Mac がスリープから復帰すると、バックグラウンドのエージェントが「Agent stalled」で失敗し、Workflow ツールのサブエージェントがプロンプトからやり直す問題を修正
- 遅いファイルシステム（特に WSL の Windows のドライブ）で管理設定が多くのパスの読み取りを拒むとき、VS Code の拡張などの SDK のホストのもとで 2.1.285 以来起動が遅い・失敗する問題を修正
- Bedrock・Vertex・Foundry・カスタムのゲートウェイで、コンピューターのスリープで中断した応答が止まったストリームとして扱われる問題を修正
- Linux と WSL で、`~/**/.env` のようなサンドボックスの読み取りのルールが大きなフォルダーを覆うと、最初の要求の前と `/sandbox` の Config タブで固まる問題を修正
- フォルダーの名前が SKILL.md の名前と違う（英語以外の名前など）スキルを、SKILL.md の名前で頼んでも見つからない問題を修正。スキルの一覧に両方の名前を出します
- プランを提示する前にクラウドのセッションのコンテナが再起動すると、plan モードで書いたプランが失われる問題を修正
- 新しい設定ディレクトリで起動の数秒後に最初のコマンドが動くと、Bash ツールがセッション全体でシェルのエイリアス・関数・プラグインの PATH を失うことがある問題を修正
- HTTP の MCP サーバーが非常に大きな応答を送ると、メモリを際限なく使う問題を修正
- クラウドのセッションの中から始めた Claude Code の実行（Bash ツールから実行した `claude -p` など）で、アーティファクトの操作が失敗する問題を修正
- リモートのセッションから 4 つ以上のファイルを同時に送ると「not the one approved」として拒まれることがある問題を修正
- 端末で `--continue` か `--resume <session-id>` で再開すると、plan モードが戻らない問題を修正
- 別の GitHub のマーケットプレイスのダウンロードフォルダーと同じ名前のマーケットプレイスが、そのマーケットプレイスのダウンロードを止める問題を修正
- 自動コンパクションの実行中に Mac がスリープすると、「Prompt is too long」で諦める問題を修正
- 非常に大きなスタックトレースやソースファイルを貼った会話で、巻き戻しのメニュー（Esc Esc / `/rewind`）がキーを押すたびに数百ミリ秒固まる問題を修正
- サブディレクトリの下のファイルを @メンションしても、そのサブディレクトリの AGENTS.md が付かない問題を修正
- セッションのフォルダーが相対のシンボリックリンクのとき、止まったランナーの後に再開したセルフホストのランナーのセッションが「missing but already registered worktree」で失敗する問題を修正
- シークレットのスキャンや権限のプロンプトが、トークンのような長いテキストに当たると固まる問題を修正
- 読み取り専用のコマンドの一部のオプションの値にあるワイルドカードに、Bash の権限の確認が Read の deny ルールやディレクトリの外の読み取りのブロックを適用しない問題を修正
- `CLAUDE_CODE_USER_DIALOG_TIMEOUT_MS=5m` が 5 ミリ秒と読まれ、リモートのダイアログがすぐ取り消される問題を修正。単位の付いた値は `dialogExpiry` にフォールバックします
- MCP サーバーのツールの一覧に結合文字の非常に長い並びがあると止まる問題を修正
- 1 つのプロンプトで重なる 2 つの貼り付けが、1 つの貼り付けのブロックではなく一部を入力したテキストとしてモデルに送られる問題を修正
- 選んだブラウザーが接続していないとき Claude in Chrome のブラウザーの選択画面に Claude 向けのメッセージが出る問題と、切り替えの後に VS Code のダイアログの一覧が古くなる問題を修正
- メインのセッションが別のワークツリーに出入りした後、バックグラウンドのサブエージェントが自分のワークツリーで書き込みと Bash のアクセスを失う問題を修正
- マシンの管理設定がゲートウェイのログインを強制していないとき、Claude apps gateway の背後でバックグラウンドのコマンド・エージェントビュー・デーモンのワーカーが Anthropic にテレメトリと機能フラグの要求を送る問題を修正
- `--restricted`（と `CLAUDE_CODE_RESTRICTED=1`）のセッションが、セッション間のメッセージのソケットを開く問題を修正
- アイドル中にバックグラウンドに移したセッションが、再起動やアイドルの掃除の後に「no saved transcript」として開き直される問題を修正。会話を再開します
- バイパスの権限の免責事項に同意していないのに、バックグラウンドのワーカーが respawn 時に `--allow-dangerously-skip-permissions` に従う問題を修正
- プラグインの非同期の Stop フックが、空白を含むフォルダー（Application Support など）の下のスクリプトのパスを引用せずに渡すと、Claude が延々と返信する問題を修正
- シークレットのマスクが非常に長い途切れのないテキストに当たると、数秒固まる問題を修正
- PreToolUse フックが入力を書き換えた後のツール呼び出しに、一部の権限ルールと安全の確認が適用されない問題を修正
- `claude auth login` の後や、設定ディレクトリに資格情報のファイルがすでにあるときに、初回の起動でログインの方法を選ばせ直す問題を修正
- 改行を含むファイル名が、ファイルのツールのエラーと権限のプロンプトで正しく表示されない問題を修正
- アクセントを別の文字として保存したテキスト（macOS のファイル名など）を含む大きな貼り付けをその場で展開すると、次のキー入力の後に入力したテキストとしてモデルに送られる問題を修正
- macOS で、キーチェーンが新しいログインを拒み、消せない古いログインを残したのに、`/login` が成功と報告する問題を修正
- `--include-partial-messages` を使う SDK のホストで、ストリームが切れる・中断される・非ストリーミングにフォールバックすると、ターンの終了後も返信が開いたままに見える問題を修正
- Linux で `.claude/settings.json` や `.claude/settings.local.json` がないとき、サンドボックスの Bash のコマンドがコマンドの途中で `ConfigChange` フックを動かし、設定を読み直す問題を修正
- git や gh など Claude Code が動かすツールが入っていないとき、エラーが欠けたプログラムを示さず「Premature close」になる問題を修正（macOS・Linux）
- Linux でのサンドボックスの Bash のコマンドの後や `.claude/scheduled_tasks.json` の削除の後に、`/loop` などのセッション限りの繰り返しの予定のタスクが 1 回余分に動く問題を修正
- シンボリックリンクの設定ファイルが指す先のファイルの編集が、設定ファイルについての権限の質問なしに動く問題を修正
- [VS Code] 一度も入力していない空のチャットが、その場所で保存済みの会話を開いた後もバックグラウンドの Claude のプロセスを動かし続ける問題を修正
- [VS Code] 保存中に Claude Code が予期せず止まったとき、設定のダイアログがタイムアウトのせいにする問題を修正
- [VS Code] 未コミットの変更を確かめられなかったのに、ブランチの切り替えのダイアログが切り替えを勧める問題を修正
- [VS Code] 開いているダイアログの後ろに届いた権限のプロンプトがキーボードのフォーカスを取り、ダイアログで押したキーがその答えになりえた問題を修正
- [VS Code] Claude Code がそのプログラムを見つけられない・起動できないとき、サインインと新しいセッションが明確な理由を示さない問題を修正
- [VS Code] エージェントのマップで、入れ子のサブエージェントが「Tool calls (0)」と表示され、それが始めたエージェントがメインのエージェントの下に置かれる問題を修正
- [クラウドセッション] クラウドの環境の環境変数でプロンプトの提案をオフにしても、新しいクラウドのセッションで効かない問題を修正
- [クラウドセッション] Claude の返信が終わった後も、作業中の表示が数秒回り続ける問題を修正。返信と同時に止まります
- [クラウドセッション] 一度も実行していないルーティンのページで Run now を押しても、History が「No runs yet」のままになる問題を修正
- [クラウドセッション] アーカイブを解除したクラウドのセッションが、次のメッセージを送るまで Claude が作業中のように見える問題を修正
- [Remote Control] Remote Control を始めたばかりのコンピューターが、新しいセッションの Remote Control のメニューに出るまで最大 1 分かかる問題を修正。数秒で出ます
- [Claude Tag] Claude Tag Admin の権限を持つメンバーが、Activity ページの Memory タブで「Couldn't load memory files」になる問題を修正。ワークスペースとチャンネルのメモリーを読めます
- [Claude Tag] ワークスペースのゲストが Slack の Claude の設定のカードで Confirm を押すと、全員のボタンが消える問題を修正。拒否はゲストにだけ表示されます
- [Claude Tag] Slack のチャンネルの予定のルーティンが、チャンネルの既定以外のモデルで動く問題を修正
- [Claude Tag] チャンネル名のルールで付けたアクセスバンドルの GitHub のリポジトリが、そのルールが対象とするチャンネルで拒まれる問題を修正
- [Code Review] ブロックするレビューのコメントが、重大度と矛盾する「nit」のラベルで始まることがある問題を修正
- [Code Review] Code Review をオフにした組織で、フォークと Manual モードの PR に「@claude review」とコメントするよう勧めるヒントが投稿される問題を修正

**その他**

- **`CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` で、起動時の接続のウォームアップも飛ばすように変更**
- **Claude in Chrome を、プロジェクトの設定ファイルではオンにできないように変更**。`--chrome`・`/chrome`・ユーザーの設定を使います
- **Bash ツールが `pyright` を実行する前に許可を求めるように変更**。読み取り専用のコマンドとして扱わなくなりました
- **mod の `$.process.spawn` が、子プロセスの実行後に別の mod が拒んだ場合の拒否の内容を変更**。呼び出しは実行され、プラグインが結果を差し止めた、と示します
- **バックグラウンドのデーモンのログで、複数行のメッセージを JSON で引用した 1 行に書くように変更**
- **スキルとカスタムコマンドで、タブと改行以外の生の制御文字を含む `!` のシェルのコマンドを、場所を示すメッセージ付きで拒むように変更**
- **`/artifacts` で、アーティファクトをブラウザーで開くと一覧を閉じるように変更**
- **Bash の権限の確認で、より多くの形の `ps` のコマンドが、確認なしに動くのではなく承認を求めるように変更**
- **プラグインのフックで、長いテキストを拒んだり黙って捨てたりせず、切り詰めてログに書くように変更**
- **予定のタスクがなくなったバックグラウンドのセッションが、約 20 秒後に Completed に移り、アイドル時に更新や停止ができるように変更**
- **クリアしたばかりのプロンプトでの「Press ← again」の確認を変更**。2 回目の ← が 1 秒待たずに切り替わり、← の長押しでも切り替わります
- **`/ultrareview` のアップロードが git の段階で失敗したときのエラーを変更**。段階と試すことを示し、git 自身のエラーの文を繰り返しません
- **medium の effort の `/code-review` が、調整したレビューの設定のないモデル（Opus 5.5 と Sonnet 5.5 を含む）でも、整理と CLAUDE.md の規約の指摘を報告するように変更**
- **インプロセスのチームメイトの Agent の結果の `agent_id` を、そのエージェントの ID に変更**（`name@team` のアドレスは `teammate_id` に残る）。TeammateIdle フックはそのサブエージェントやフォークからは発火しなくなりました
- **スケジュールした wakeup（`/loop`）を待つバックグラウンドのセッションを、更新やメモリー不足のときも動かし続けるように変更**。再起動や停止で wakeup を黙って失うことがありました
- **`claude agents` から忙しいバックグラウンドのセッションに送った `/model`・`/effort`・`/rename` を、ターンの終わりではなく確認なしにすぐ適用するように変更**
- **Claude apps gateway が対応する PostgreSQL の最小の版を、14 から 11 に変更**
- **対話型のセッションの WebSearch の予算を、200 回で終わるのではなく時間で回復するように変更**。1 時間に 100 回で、`CLAUDE_CODE_WEB_SEARCH_REFILLS_PER_HOUR` で回復の速さを決め、0 で回復を止めます
- **`CLAUDE_CODE_DISABLE_ATTACHMENTS` を、リポジトリの `.claude/settings.json`・`.claude/settings.local.json` では設定できないように変更**。シェル・ユーザー・管理の設定では引き続き設定できます
- **ディレクトリから読み込んだプラグインへの `claude plugin update` が、組み込みのプラグインと同じく「Failed to update plugin」の接頭辞なしに理由だけを出すように変更**
- **クラウドのセッションの組み込みの `gh api` を変更**。`GH_HOST`・`GH_REPO` に設定した github.com 以外のホストを拒み（`--hostname` か完全な URL を使う）、ほかのホストへの要求を stderr に注記します
- **`claude-api` スキルの Managed Agents の例を、エージェントが必要としない限り web のツールをオフにし、`auto` の権限ポリシーを使う形に変更**
- **[セルフホストのランナー] `claude --environment <id>` が、現行の Sessions API でセッションを作るように変更**。表示や JSON のセッション ID は `session_…` の形のままです
- **[VS Code] メッセージのタイムスタンプを既定で表示するように変更**（Claude Code: Show Message Timestamps の設定でオフにできる）
- **[Claude Tag] チャンネルの指示の上限を、バイトではなく 8,192 文字に変更**。英語以外のテキストも同じだけ書け、Configure ページの Save の横に文字数を出します
- **`Run /reload-plugins to activate.` の表記が `Run /reload-plugins to apply.` になった**（`channels`・`skills`・`plugins/troubleshooting`（見出しも）・`plugins/install`・`mcp`・`security-guidance`・`claude-security`）。`plugins/troubleshooting` には、同時にプロンプトの上に `Plugins changed. Run /reload-plugins to activate.` の通知が出ることもある、と加わりました
- **claude.ai の管理画面で GitHub の連携の場所が「Organization settings > Git providers」になった**（`admin-setup`・`github-enterprise-server`）。GitHub Enterprise Server の接続は **Connect** か、接続済みなら **Add instance** を押し、**Set up automatically** か **Add manually** を選ぶ手順になり、有効にする機能の一覧から Claude Security が外れました。`self-hosted-environments-deploy` の参照も「claude.ai」の表記になっています
- **v2.1.146〜v2.1.239 の版についての「Requires」「As of」「Before」などの注記が多くのページで削除された**（`tools-reference`・`permission-modes`・`permissions`・`settings-reference`・`hooks`・`monitoring-usage`・`interactive-mode`・`skills`・`statusline`・`sub-agents`・`commands`・`costs`・`keybindings`）
- **このほか、言い回しの修正があった**。「comprehensive」「just」「we recommend」「Let's」「Please」などの表現や、`strongly-typed`・`frequently-used` などのハイフンが改められています（`quickstart`・`third-party-integrations`・`sandboxing`・`github-actions`・`common-workflows`・`glossary`・`headless`・`deep-links`・`desktop-scheduled-tasks`・`settings`・`best-practices`・`large-codebases`・`self-hosted-environments-deploy`・`agent-sdk/typescript`・`agent-sdk/python`・`agent-sdk/subagents`・`agent-sdk/skills`・`agent-sdk/structured-outputs`・`agent-sdk/secure-deployment`・`agent-sdk/quickstart`・`agent-sdk/migration-guide` など）。`fullscreen` と `commands` の `/scroll-speed` の説明からは「ダイアログに目盛りが出る」が外れ、`quickstart` のインストールのコードブロックには `theme={null}` が 4 回重なって付いています
- **`llms.txt` に HIPAA のページが加わり、Slack のページの説明が改められ、言語別の索引のページ数がすべて 220 から 221 になった**
- **見出しマップに 25 見出しが加わり、2 見出しが改称された**。`hipaa-setup` の 20 見出し、`slack` の 2 見出し、`errors` の「Safeguards flagged a request for Claude's reasoning」、`agent-sdk/custom-tools` の「Make a parameter optional」、`agent-sdk/typescript` の `SDKSessionStateChangedMessage` などで、すべて本文にあります。改称は `plugins/mods/troubleshoot` の「Your version is too old」と `plugins/troubleshooting` の `Run /reload-plugins to apply.` です
- **見出しマップ冒頭の自動生成スタンプが、2026年10月04日 15時59分42秒 UTC から 2026年10月06日 01時40分57秒 UTC へ進みました**

**参考リンクについて**: 日本語版は、`hipaa-setup`・`legal-and-compliance`・`slack`・`agent-sdk/typescript`・`agent-sdk/python`・`errors`・`desktop`・`agent-sdk/custom-tools`・`agent-view`・`env-vars`・`memory`・`permission-modes`・`cli-reference`・`plugins/mods/overview`・`fullscreen`・`keybindings` の 16 ページを実測し、今回の内容に更新されていたためリンクを付けています。**`channels-reference` は日本語版を確かめていないため、英語版だけにしています。** changelog だけに載っていて対応する節のない項目にはリンクを付けていません。 **changelog ページへのリンクは、本サマリの方針どおり付けていません。**
<!-- light:minor-updates:end -->

## 新着情報

<!-- light:whats-new:start -->
**今回、`whats-new/` 配下のページに変更はありません。**
<!-- light:whats-new:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-10-04.md](./archives/latest/2026-10-04.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-10-04.md](./archives/latest-detail/2026-10-04.md)

<!--
base_commit: 39d4fa8afc2b6111b66fec97040194774d7ecd80
head_commit: c3f00327d040ed4b125f7bfb47f07adb2a4785cc
generated_at_full: 2026-10-06T15:09:15+09:00
-->
