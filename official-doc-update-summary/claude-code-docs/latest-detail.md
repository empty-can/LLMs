---
対象期間: 2026年11月23日 〜 2026年11月24日
作成日: 2026-11-24
---

# Claude Code 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
**今回は、MCP サーバーがツールと一緒にスキルを配れるようになり（パブリックベータ）、スキルの読み込み時に走るシェルコマンドを止める新しいフックのイベント `PreSkillShellCommand` が加わりました。Claude Security プラグインには、ほかのスキャナーの結果のトリアージ・脅威モデル・攻撃面の分析と、シェルや GitHub Actions からのスキャンが加わり、`/ship` と `/steward` は GitLab などのホストのブランチも見守れるようになりました。以前の Claude Code in Slack は終了し、そのページは代わりの手段を案内する短いページになりました**。changelog には v2.1.332（150 項目）が加わりました。新規ページと新着情報のページはなく、`llms.txt` の URL は 221 のままです。changelog を除いて 50 行以上変わったのは 10 ページで、`llms-full.txt` の生の差分は追加 1,919・削除 745、総行数は 136,262 行から 137,436 行になりました。

主要なものを以下に挙げます。

1. MCP サーバーのスキルが `<server>:<skill>` の名前で `/` のメニューに出るようになった（v2.1.331 以降・パブリックベータ）。auto モードでは分類器が読み込みを決め、Team と Enterprise では組織がオンにするまで使えない
2. スキルやコマンドの読み込み時に走るシェルコマンド（injected commands）には `PreToolUse` が発火しないため、それを記録・ブロックする `PreSkillShellCommand` のイベントができた（v2.1.332 以降）。ブロックしかできず、許可や書き換えはできない
3. Claude Security プラグインに、SARIF などの既存の結果のトリアージ、脅威モデルの作成、攻撃面の分析、Linux のサンドボックスで動く `claude-security` コマンド、プルリクエストをスキャンする GitHub Actions のジョブが加わった
4. `/ship` と `/steward` が、GitLab・Bitbucket・Azure DevOps のブランチを git だけで最長 7 日見守れるようになった。v2.1.331 からは、watch の間はセッションをバックグラウンドへ送れず、plan モードでは `/ship` が始まらない
5. 以前の Claude Code in Slack が終了した。`slack` のページは、Team と Enterprise には Claude Tag を、Pro・Max・Ultra にはプロジェクトかクラウドセッションを案内するだけになり、ほかのページからのリンクも外れた
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**MCP サーバーのスキルが使えるようになった**](#1-mcp-サーバーのスキルが使えるようになった):  
  `mcp` に「Use skills from MCP servers」の節ができ、claude.ai のコネクター・自分で加えたサーバー・プラグインのサーバーが配るスキルを、`/docs:pdf` のような `<server>:<skill>` の名前で使えるようになりました（v2.1.331 以降のパブリックベータ）。承認の流れ、パーミッションのルール、Anthropic のスキャン、使える環境、組織でのオンとオフの仕方が載っています
2. [**スキルの読み込み時のシェルコマンドを止めるフック PreSkillShellCommand が加わった**](#2-スキルの読み込み時のシェルコマンドを止めるフック-preskillshellcommand-が加わった):  
  スキルの `` !`<command>` `` のような injected command には `PreToolUse` のフックが発火しません。新しいイベント `PreSkillShellCommand` は、パーミッションの確認を通った injected command が走る前に呼ばれ、終了コード 2 か `deny` でそのコマンドだけを止めます（v2.1.332 以降）
3. [**Claude Security プラグインの仕事が大きく増えた**](#3-claude-security-プラグインの仕事が大きく増えた):  
  既存の脆弱性の一覧のトリアージ、脅威モデルの作成、攻撃面の分析の 3 つの仕事と、セッションの外でスキャンする `claude-security` コマンド・GitHub Actions のジョブが加わりました。スキャンの実況の表示、止まったスキャンの続行、より念入りな変更のスキャンも載っています
4. [**/ship と /steward が GitHub 以外のホストのブランチも見守れるようになった**](#4-ship-と-steward-が-github-以外のホストのブランチも見守れるようになった):  
  GitLab・Bitbucket・Azure DevOps では、GitHub CLI なしに git だけでブランチを見守ります。v2.1.331 からの挙動の変化（開いている自分のプルリクエストへのコミット、バックグラウンドと plan モードでの扱い、`CLAUDE_CODE_DISABLE_SHIP`）も、`ship-command` とトラブルシューティングのページに加わりました
5. [**以前の Claude Code in Slack が終了した**](#5-以前の-claude-code-in-slack-が終了した):  
  `slack` のページの本文は、以前の Claude Code in Slack は終了した、という案内と、プランごとの代わりの手段の 2 項目だけになりました。`overview` などのほかのページからも、`slack` のページへのリンクがすべて外れています
<!-- light:highlight-list:end -->

## 1. MCP サーバーのスキルが使えるようになった

**`mcp` に h2「Use skills from MCP servers」ができました。** Skills over MCP では、サーバーがツールと一緒にスキルを配れます。対象は claude.ai のコネクター、自分で加えたサーバー、プラグインのサーバーで、自分のサーバーでスキルを配るには MCP の Skills extension を実装します。パブリックベータで、Claude Code v2.1.331 以降が要ります（changelog では v2.1.332 の Added に「Added skills from MCP servers (beta)」とあります）。

- **見つけ方と呼び方**: ターミナル・VS Code・Desktop の Code タブで `/` を打つと出ます（ターミナルと VS Code では `/skills` でも）。名前は `<server>:<skill>` で、`docs` というサーバーの `pdf` なら `/docs:pdf report.pdf` のように打ちます。コネクターとプラグインのサーバーには接頭辞が付きます（`claude_ai_Docs:pdf`、`plugin_my-plugin_docs:pdf`）
- **承認**: 既定の auto モードではプロンプトは出ず、分類器がスキルを読まずに読み込むかどうかを決めます。Manual と `acceptEdits` のモードではプロンプトが出て、**Allow this version** を選ぶと、サーバーがスキルのファイルを変えるまでプロンプトと分類器を飛ばします。`ask` のルールか、コネクターの **Restrict to Ask** があると、auto と `bypassPermissions` のモードでも毎回承認が要ります。コマンドとして自分で打つときは承認は要りません
- **ルール**: `deny` の `Skill(mcp__docs__*)` は打ったコマンドも含めてそのサーバーのスキルを止め、`Skill(docs:pdf)` は 1 つだけ、`mcp__docs` はスキルとツールの両方を止めます。`allow` の `Skill(mcp__docs__*)` はユーザーか managed の設定に置き、ユーザーかローカルのスコープで加えたサーバーと managed のサーバーにだけ効きます（コネクター・`.mcp.json`・プラグインのサーバーには効かない）。スキルの名前への `allow` ではプロンプトを飛ばせません
- **スキャン**: Anthropic がスキャンするのは、claude.ai で加えたサードパーティの Directory のコネクターと、Enterprise の組織が **Skill and plugin security scanning** をオンにしている間のカスタムコネクターのスキルだけで、`claude mcp add` で加えた Directory のサーバーを含むほかのサーバーはスキャンしません
- **使える環境**: ターミナル（JetBrains の IDE を含む）と Desktop のローカルのセッションで使え、VS Code の拡張機能には順に展開中です。Fable のモデルか Claude Opus 4.8・Sonnet 5・Haiku 5.5 以降と、フィーチャーフラグを取得する Anthropic への直接の接続が要ります。クラウドセッション、`claude -p`、`claude remote-control` のサーバーモード、GitHub Actions、Agent SDK、クラウドプロバイダー・独自の `ANTHROPIC_BASE_URL`・`apiKeyHelper`・`ANTHROPIC_AUTH_TOKEN`、HIPAA やゼロデータ保持の組織では使えません
- **プランと組織**: `/login` でサインインした Pro・Max・Ultra ではオン、Team と Enterprise では組織がオンにするまでオフです。コネクターは Owner が **Organization settings > Connectors** の **Skills over MCP** をオンにし、ほかのサーバーは managed settings の `disableDirectMcpSkills` を `false` にします。管理する端末では、`disableDirectMcpSkills` と `disableClaudeAiConnectors` を `true` にしてオフにできます

ほかに、1 つのサーバーが示すスキルは 100 まで、スキャンされるスキルは 1 つのテキストファイルが 100 KB・1 つのスキルが 400 KB まで、といった制限と、トラブルシューティングの表が載っています。

`skills` にも h3「Skills from MCP servers」ができ、MCP のスキルでは `allowed-tools`・`disallowed-tools`・`hooks`・`model`・`effort`・`context`・`agent`・`background`・`shell`・`paths`・`metadata` のフロントマターが無視され、`!` のコマンドは走らず、`@` の参照は添付されず、`${CLAUDE_PROJECT_DIR}` と `${CLAUDE_SESSION_ID}` も置き換えられない、と述べます。`settings-reference` には `disableDirectMcpSkills` の項目が加わり（managed のみ。Windows の HKCU のレジストリの `false` は無視される）、`strictPluginOnlyCustomization` の `skills` のロックでは、ユーザー・プロジェクト・`--mcp-config` が加えたサーバーのスキルは読み込まれず、コネクターのスキルは読み込まれる、という文が加わりました。`feature-availability` の HIPAA の構成の表、`managed-settings`、`headless`（`-p` では使えない）、`env-vars`（フィーチャーフラグの取得をオフにすると使えない）、`tools-reference` の Skill の行、mod のページ（`session.append` では MCP のスキルの行を書き換えられず、`skill.prompt` で書き換える）にも載っています。

- [MCP を使用して Claude Code をツールに接続する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/mcp#use-skills-from-mcp-servers)
- [Connect Claude Code to tools via MCP - Claude Code Docs (English)](https://code.claude.com/docs/en/mcp#use-skills-from-mcp-servers)
- [Claude をスキルで拡張する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/skills#skills-from-mcp-servers)
- [Extend Claude with skills - Claude Code Docs (English)](https://code.claude.com/docs/en/skills#skills-from-mcp-servers)

## 2. スキルの読み込み時のシェルコマンドを止めるフック PreSkillShellCommand が加わった

**`hooks` に h3「PreSkillShellCommand」とその下の 3 つの h4 ができました。** injected command は、スキルや `/security-review` のようなコマンドが読み込まれるときに走るシェルコマンドで、スキルのファイルでは `` !`<command>` `` か ` ```! ` のブロックで書かれます。これには `PreToolUse` のフックが発火しないため、`PreToolUse` で使っているスクリプトでそれを記録・ブロックしたいときは、このイベントにも加えます。Claude Code v2.1.332 以降（Desktop アプリと VS Code の拡張機能を含む）が要り、先に設定ファイルに書くと、v2.1.331 のような以前の版では対話のターミナルのセッションごとに `Unknown hook event "PreSkillShellCommand" was ignored` という警告のダイアログが出ます（以前の版は、フックを呼ばずに injected command を走らせる）。

- **ブロックに使うときの設定**: matcher は `Bash|PowerShell`、型は async でない `command`・`http`・`mcp_tool`（`prompt` と `agent` のフックはこのイベントでは走れず、合うコマンドをすべてブロックする）、置き場所は設定ファイルかプラグイン（スキル自身のフロントマターのフックは、セッションでの最初の読み込みとサブエージェントの中では効かない）、失敗に備えて `onFailure: "block"`
- **届くコマンド**: injected command のパーミッションの確認を通ったものだけが届き、`bypassPermissions` モードでも走ります。auto モードで承認が要るコマンドは読み込みのときには走らず、後で Claude がツールの呼び出しとして走らせると `PreToolUse` が発火するので、両方のイベントにスクリプトを置きます
- **入力**: 共通のフィールドに加えて `tool_name`（`Bash` か `PowerShell`）・`tool_input.command`・`tool_use_id`・`command_name`・`command_source`・`invoked_by`（`user`・`claude`・`other`）
- **判定**: 終了コード 2・`permissionDecision: "deny"`・トップレベルの `decision: "block"` でコマンドは走らず、スキルは読み込まれて、Claude はコマンドの出力の代わりに `[not run: blocked by hook: <reason>]` を読みます。`ask`・`defer`・`updatedInput` も `deny` と同じく止めるので、許可や書き換えはできません。`continue: false` ではスキルの呼び出し自体が `Operation stopped by hook: <stopReason>` で失敗します。フックが失敗かタイムアウトしたときは、`onFailure` で止めない限りコマンドは走ります（Claude がコードを走らせた後の Code Mode のセッションでは、タイムアウトは既定で止める）
- **見え方**: 自分でスキルの名前を打ったときは、止めたコマンドが `Not run in /<name>`、フックが失敗しても走ったコマンドが `Ran anyway in /<name>` の行で示されます。Remote Control がつながっている間は理由が見えないので、デバッグのログで確かめます

`hooks` のイベントの一覧・matcher の表・終了コード 2 の表・JSON での判定の表や、`if` の欄が効くイベント、`prompt` と `agent` のフックが使えないイベントの一覧、Git Bash のない Windows での失敗の扱いにも `PreSkillShellCommand` が加わりました。`hooks-guide`（matcher が配列だと、同じファイルのほかのフックも読み込まれないイベントの 1 つ）、`skills`（injected command には `PreToolUse` が発火しないので、このフックを使う）、`errors`（`Not run in /<name>` などのメッセージの行）にも載っています。日本語版の `hooks` には、まだこの節がありません。

- [Hooks reference - Claude Code Docs (English)](https://code.claude.com/docs/en/hooks#preskillshellcommand)

## 3. Claude Security プラグインの仕事が大きく増えた

**`claude-security` は、セッションの中でのスキャンに加えて、シェルや GitHub Actions からもスキャンでき、仕事の種類も増えたページになりました。** 冒頭の、既定のスキャンの手順から脅威モデルの作成が外れ（`low` のスキャンの説明も、アーキテクチャーの地図を飛ばす、だけになった）、自分のものか試す許可のあるコードだけをスキャンする、という文が加わりました。`/security-review` は、ほかのツールとの比べ方の段落と表から外れています。新しい h2・h3 は次のとおりです。

- **Triage findings you already have**: ほかのスキャナーの SARIF 2.1.0 のファイルや、以前のスキャンの `CLAUDE-SECURITY-<timestamp>/` のディレクトリにある指摘が、コードに照らして成り立つかを確かめます（`/claude-security triage results.sarif`）。報告は `FINDINGS-TRIAGE.md` で、退けた指摘は **Not validated** の下に並ぶので、自分で確かめます
- **Create a threat model**: `/claude-security:threat-model` が、コードとスキャンの報告を読み、システムについて尋ねて脅威モデルの下書きを作り、`.claude-security/threat-model.md` に保存します。報告があれば、各指摘の前提条件が満たされているかを `CLAUDE-SECURITY-PRECONDITIONS.md` に書けます。コネクターを読ませると検索の語がマシンの外に出る、という警告付きです
- **Analyze your attack surface**: `/claude-security:attack-surface-analysis` が、既定の構成で届くのにどの既定の機能も使わないコード、ログイン前に届く機密のコード、セキュリティの機能を黙ってオフにするオプションの組み合わせを探し、攻撃面を縮める変更を提案します
- **Scan from your shell**: `claude-security` コマンドが、走らせたフォルダーをプラグインのサンドボックスの中でスキャンします。サンドボックスは Linux だけで（カーネル 5.19 以降・Python 3.10 以降・root 以外のユーザー。Ubuntu 24.04 以降は `--sudo`）、Windows は `--no-sandbox` が要り、macOS と WSL 2 には対応しません。リポジトリの `.claude/` の設定とフックを読み込まず、サンドボックスでは server-managed settings も効かない、という警告があります。`/claude-security:install-cli` で `PATH` に加えます
- **Scan pull requests in GitHub Actions**: プルリクエストの変更をスキャンし、レビューと修正の提案を投稿して、マージを止めることもできるジョブです。GitHub.com の GitHub ホストの Linux のランナーと、Anthropic の API かサードパーティのプロバイダーが要り、有料プランではサインインできません。プッシュできる人を全員信頼できるリポジトリでだけ使う、パブリックなリポジトリでは見つかった脆弱性が公開されうる、という警告付きで、版 0.13.0 のコミット `d0d514288960e7a78e1a76e4a3ec694416458726` が示されています
- **そのほかの h3**: 「Watch a running scan」（ターミナルでは mod の実況の表示が開く。v2.1.292 以降）・「Continue a stopped scan」（`/claude-security continue the scan`）・「Run a more thorough change scan」（`--change-scan-effort high`。費用は数倍で、変更より古い脆弱性も報告する）・「Tell a scan about your system」（10 までのファイルかメモを渡す）・「Patch from an older report」（スキャンしたコミットが今の履歴にあれば古い報告からもパッチを作れる）

パッチを作るなら作業ツリーをきれいにしてから始める（`git stash -u`）、パッチの仕事が終わったら `git status` で確かめる、パッチはメモ `F<n>.md` のコマンドでリポジトリのルートから当てる、といった手順の変化と、マネージドの Claude Security の指摘をセッションに出す `/claude-security:hosted` も加わりました。

- [コードベースの脆弱性をスキャンする - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/claude-security#triage-findings-you-already-have)
- [Scan your codebase for vulnerabilities - Claude Code Docs (English)](https://code.claude.com/docs/en/claude-security#triage-findings-you-already-have)

## 4. /ship と /steward が GitHub 以外のホストのブランチも見守れるようになった

**`ship-command` に h3「Watch a branch on another host」と h4「Checks and comments on GitLab, Bitbucket, and Azure DevOps」ができました。** GitLab・Bitbucket・Azure DevOps のようなホストでは、Claude は最長 7 日、ブランチを見守ります（watch）。git 2.38 以降が要り、GitHub CLI は要りません。`/ship` と `/steward` は始めるときに何もコミット・プッシュ・作成しないので、変更をコミットし、`git push -u origin <branch>` でブランチをプッシュし（gitlab.com・bitbucket.org・dev.azure.com ならマージリクエストかプルリクエストも開き）、それから `/ship` か `/steward` を打ちます。v2.1.331 より前は、`/ship` は変更をレビューするだけで watch は始まりませんでした。

- **できること**: 自分の git のサインインで、ベースのブランチを取り込んで競合を解く、ほかの人のプッシュを取り込む、ブランチにコミットをプッシュする。コメントへの返事、チェックの再実行、CI のログを読むコマンドはありません
- **ホストの API を読む**: ターミナルのセッションでは、プッシュ先のリモートについて git が持つサインインを、gitlab.com・bitbucket.org・dev.azure.com の API への `GET` 要求に使い、マージリクエストやチェック・コメントを読みます。先に尋ねられることはなく、最初の読み取りの前に `It only reads.` で終わる 1 行が出ます。リモートを SSH にするか、ホストを `sandbox.network.deniedDomains` に入れると防げます
- **ベースの指定**: `origin/main` のようなリモートとブランチを引数で渡して、変更の入る先を示せます（v2.1.331 以降）。watch を始め直すときも `/steward origin/main` のように付けます

v2.1.331 からの挙動の変化もまとめて書き込まれています。

- **開いている自分のプルリクエスト**: `/ship` が、コミットしていない変更をコミットし、まだプッシュしていないコミットと一緒にプッシュできるようになった（パブリックなリポジトリや auto-merge がオンのときなどはコミットしない）。ほかの人のプルリクエストならコミットもプッシュもせず、watch も始まらない。既定のブランチにだけコミットがあるときは、新しいブランチを作ってプッシュし、プルリクエストを開く
- **バックグラウンドと plan モード**: watch の間は `/background` や `←` でセッションをバックグラウンドへ送れず、バックグラウンドのセッションでは watch が始まらない（以前は送ると watch が終わった）。`/ship` は plan モードでは始まらず、次にプルリクエストを確かめるときに plan モードだと watch が終わる
- **そのほか**: GitHub CLI が 2.63 より古いと watch が始まらない（以前は始まってプッシュできなかった）。環境変数 `CLAUDE_CODE_DISABLE_SHIP` を `1` にすると `/ship` と `/steward` の両方がオフになる

`ship-command-troubleshooting` には、h3「Your pull request is already open」と h4「Keep a custom /ship or /steward without renaming」（同じ名前の自分のコマンドを残すには `CLAUDE_CODE_DISABLE_SHIP` を使う）ができ、新しいメッセージの行が多数加わりました。`agent-view` と `commands` の `/background` の説明にも、watch の間はセッションを前に残す、という注記が加わっています。

- [/ship と /steward でプルリクエストをマージ可能な状態にする - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/ship-command#watch-a-branch-on-another-host)
- [Get a pull request ready with /ship and /steward - Claude Code Docs (English)](https://code.claude.com/docs/en/ship-command#watch-a-branch-on-another-host)

## 5. 以前の Claude Code in Slack が終了した

**`slack` のページは、見出しをすべて失い、代わりの手段の案内だけになりました。** 説明文（`llms.txt` も同じ）は「Team・Enterprise・Pro・Max・Ultra のプランで、以前の Claude Code in Slack の代わりに使うもの」になり、本文は、以前の Claude Code in Slack は終了し、Claude Tag につながっていないワークスペースでは `@Claude` が、ワークスペースが Claude Tag 用に設定されていない、と返事をする、と述べます。

- **Team と Enterprise**: チャンネルにいれば Claude Tag を使う。いなければ Claude Tag のセットアップの案内を、以前の版からワークスペースを移すには移行のガイドを見る
- **Pro・Max・Ultra**: Claude Tag は個人のプランでは使えないので、アカウントにあればプロジェクトで、なければクラウドセッションで仕事を始める

これまでの、使い道・前提条件・セットアップの手順・ルーティングのモード・アクセスと権限・トラブルシューティングなどの節はすべて外れました。ほかのページでも、`slack` のページへのリンク（base の 15 か所）がすべて外れています。`overview` の使い方の例と「Use Claude Code everywhere」の表は Claude Tag（Team と Enterprise）に差し替わり、連携の表・手元を離れて働く方法の表・関連のリストからは Slack の行が外れました（`platforms` の同じ表からも）。`claude-tag` からは、Pro・Max・Ultra では Claude Code in Slack を設定する、という文が、`feature-availability` の claude.ai のアカウントが要る機能の一覧からは Claude Code in Slack の行が外れ、`channels` の表の行は Claude Tag に、`llm-gateway-connect` の h3「Slack, cloud sessions, and Remote Control」は「Cloud sessions, Claude Tag, and Remote Control」になりました。`how-claude-code-works`・`mobile`・`quickstart` の一覧からも Slack が外れています。

- [Slack での Claude Code - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/slack)
- [Claude Code in Slack - Claude Code Docs (English)](https://code.claude.com/docs/en/slack)

## 新規追加されたページ

<!-- light:new-pages:start -->
（今回の対象期間に新規追加されたドキュメントページはありません。`llms.txt` の URL は 221 のままで、`llms-full.txt` の `Source:` の行も 226、固有のページも 221 のままです）
<!-- light:new-pages:end -->

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
- [**Draw in the interface with a mod**](#1-draw-in-the-interface-with-a-mod) ([English](https://code.claude.com/docs/en/plugins/mods/interface#animate-a-backdrop-with-a-shader)):  
  323 行（追加 317・削除 6）が変わりました。Desktop アプリの Code タブ向けに、GPU のシェーダーで動く背景、メッセージの吹き出しと書体のスタイル、テーマの音の 3 つの h3 が加わりました
- [**Claude Code in Slack**](#2-claude-code-in-slack) ([日本語](https://code.claude.com/docs/ja/slack) / [English](https://code.claude.com/docs/en/slack)):  
  249 行（追加 4・削除 245）が変わりました。以前の Claude Code in Slack の終了に伴い、本文が代わりの手段の案内だけになりました（詳細はハイライト 5 参照）
- [**Scan your codebase for vulnerabilities**](#3-scan-your-codebase-for-vulnerabilities) ([日本語](https://code.claude.com/docs/ja/claude-security#scan-from-your-shell) / [English](https://code.claude.com/docs/en/claude-security#scan-from-your-shell)):  
  243 行（追加 208・削除 35）が変わりました。Claude Security プラグインの h2 が 5 つ、h3 が 5 つ加わりました（詳細はハイライト 3 参照）
- [**Connect Claude Code to tools via MCP**](#4-connect-claude-code-to-tools-via-mcp) ([日本語](https://code.claude.com/docs/ja/mcp#mcp-tasks-in-the-cloud) / [English](https://code.claude.com/docs/en/mcp#mcp-tasks-in-the-cloud)):  
  240 行（追加 222・削除 18）が変わりました。MCP のスキルの h2（ハイライト 1）のほかに、VS Code・Desktop アプリ・クラウドセッション・claude.ai のチャットでの MCP タスクの h4 が 5 つ加わりました
- [**Troubleshoot /ship and /steward**](#5-troubleshoot-ship-and-steward) ([日本語](https://code.claude.com/docs/ja/ship-command-troubleshooting#your-pull-request-is-already-open) / [English](https://code.claude.com/docs/en/ship-command-troubleshooting#your-pull-request-is-already-open)):  
  104 行（追加 77・削除 27）が変わりました。v2.1.331 と GitHub 以外のホストでの watch に合わせて、メッセージの行と h3・h4 が加わりました（詳細はハイライト 4 参照）
- [**Hooks reference**](#6-hooks-reference) ([English](https://code.claude.com/docs/en/hooks#preskillshellcommand-decision-control)):  
  100 行（追加 89・削除 11）が変わりました。ほとんどは `PreSkillShellCommand` のイベントの追加です（詳細はハイライト 2 参照）
- [**Get a pull request ready with /ship and /steward**](#7-get-a-pull-request-ready-with-ship-and-steward) ([日本語](https://code.claude.com/docs/ja/ship-command#what-ends-a-watch) / [English](https://code.claude.com/docs/en/ship-command#what-ends-a-watch)):  
  89 行（追加 67・削除 22）が変わりました。GitHub 以外のホストでの watch の h3・h4 と、v2.1.331 からの挙動の変化です（詳細はハイライト 4 参照）
- [**Error reference**](#8-error-reference) ([日本語](https://code.claude.com/docs/ja/errors#claude-code-needs-a-recent-sign-in) / [English](https://code.claude.com/docs/en/errors#claude-code-needs-a-recent-sign-in)):  
  79 行（追加 73・削除 6）が変わりました。Desktop の Code タブで再サインインを求められたときの h3、リトライの watchdog が止まる場合の h4、メッセージの索引の表の 32 行が加わりました
- [**Run tool calls from code with Code Mode**](#9-run-tool-calls-from-code-with-code-mode) ([日本語](https://code.claude.com/docs/ja/code-mode#requirements) / [English](https://code.claude.com/docs/en/code-mode#requirements)):  
  72 行（追加 48・削除 24）が変わりました。Amazon Bedrock などのクラウドプロバイダーで Code Mode が使えるようになり（v2.1.331 以降）、サブエージェントで使う方法と、フックが失敗した後に呼び出しが走る場合の h3 が加わりました
- [**Tools reference**](#10-tools-reference) ([日本語](https://code.claude.com/docs/ja/tools-reference#fix-unexpected-webfetch-prompts-and-denials) / [English](https://code.claude.com/docs/en/tools-reference#fix-unexpected-webfetch-prompts-and-denials)):  
  69 行（追加 48・削除 21）が変わりました。WebFetch の対処の表が 4 つの h3 に分かれ、Code Mode の `REPL` ツールの行と、PowerShell のコマンドの作業ディレクトリの h3 が加わりました
<!-- light:updated-pages:end -->

**行数の数え方**: `llms-full.txt` の生の差分のハンクを、追加行は head 側、削除行は base 側の `Source:` 行でページに振り分けた値です。ページの並びと 2 回載るページ（`cloud-environments`・`model-config`・`permissions`・`plugins/install`・`terminal-config`）は変わっておらず、ページ単位の合計は生の差分（追加 1,919・削除 745）と一致します。2 回載るページの行数は 2 つの写しの合計で、変わったのは `permissions`（28 行。1 つの写しあたり 14 行）・`cloud-environments`・`model-config`（どちらも 8 行。同じく 4 行）で、2 つの写しは同じように変わりました。50 行以上のページにはほかに changelog（172 行。追加 169・削除 3）があり、v2.1.332 の追加は軽微な更新にまとめました。大幅更新の 10 ページに次いで多いのは `plugin-evals` の 38 行、`plugins/mods/reference` の 37 行、`skills` の 36 行です。

## 1. Draw in the interface with a mod

**`plugins/mods/interface` には、Desktop アプリの Code タブで効く 3 つの h3 が加わりました。** どれも `$.theme.set` で設定するテーマの一部で、1 つのセッションのテーマは 1 つなので、背景・色・メッセージのスタイル・音は 1 回の呼び出しでまとめて渡します。

- **Animate a backdrop with a shader**（h4「Fix a backdrop that shows only the `Svg`」付き）: `Svg` を `Shader` の要素で包むと、GPU で画素ごとの色を計算するシェーダーのファイルの結果が `Svg` の上に描かれ、ポインターに合わせて動く背景になります。Code タブの Claude Code v2.1.326 以降が要ります。ポインターの下に光を描き、背景のクリックで色を変える `glow` という mod の例（`claude-code/shader` を読み込む `glow.ts` と、`ui.render` と `ui.pointer` のフックを持つ `register.js`）と、`claude plugin validate` が `runs on any GPU` と出すかで確かめる手順が載っています。クリックは 1 秒に 2 回まで、`values` で渡せる数は 8 つまで、シェーダーのファイルは `while` のループ・再帰・ほかのファイルからの読み込みのない TypeScript の部分集合、といった決まりと、動きを減らす設定や重すぎるシェーダーで `Svg` だけが出る場合の対処もあります
- **Style messages in the Desktop app**（h4 が 4 つ）: `style` を渡すと、メッセージの吹き出し・書体・文字の大きさを変えられます。Code タブの v2.1.329 以降が要り、ターミナル・VS Code の拡張機能・モバイルアプリには効きません。キーは `Text`・`Heading`・`UserMessage`・`AssistantMessage`・`ToolUse` で、`fontFamily` は `sans`・`serif`・`mono`・`cursive`・`code` のどれか 1 つの一覧で書き、メッセージは `-3` から `3` 度まで傾けられます。ライトとダークのモードで色を分けるには `makeColors` のテーマに `bg-user-message` などを加えます。文字と背景のコントラストが 3:1 に満たないと、そのメッセージはアプリの色のまま出ます
- **Add sound to a theme**（h4 が 2 つ）: `sound` を渡すと、背景の音（`ambience`）と、メッセージの送信・ツールの呼び出し・ターンの終わりなどで鳴る短い音（`cues`）を付けられます（v2.1.329 以降）。音は音声ファイルでなく、音色とノイズの層で記述し、Desktop アプリが音を作ります。ユーザーがセッションのタイトルバーのスピーカーのボタンでオンにするまで鳴らず、mod から鳴らすことはできません

ほかに、「Change what Claude Code already draws」の導入が短くなり、`AskUserQuestion` は `ui.render` のフックで置き換えられない、と明記され、ターミナル・Desktop・VS Code で効く描画の場所に `AbovePrompt` が加わりました。`plugins/mods/reference` にも、`Shader` の要素、`ui.pointer` のイベント、`tool.offer` のイベント（Claude に見せるツールの一覧を変える。v2.1.328 以降）、`BesidePrompt` と `Underlay` の描画の場所（v2.1.331 以降）、`$.session.redact`（v2.1.331 以降）が加わっています。日本語版の `plugins/mods/interface` には、まだ 3 つの h3 がありません。

- [Draw in the interface with a mod - Claude Code Docs (English)](https://code.claude.com/docs/en/plugins/mods/interface#animate-a-backdrop-with-a-shader)

## 2. Claude Code in Slack

**`slack` は 249 行（追加 4・削除 245）が変わりました。** 29 の見出しを持つ説明のページが、以前の Claude Code in Slack は終了した、という案内と、プランごとの代わりの手段の 2 項目だけになりました。内容はハイライト 5 にまとめました。

- [Slack での Claude Code - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/slack)
- [Claude Code in Slack - Claude Code Docs (English)](https://code.claude.com/docs/en/slack)

## 3. Scan your codebase for vulnerabilities

**`claude-security` は 243 行（追加 208・削除 35）が変わりました。** h2「Triage findings you already have」「Create a threat model」「Analyze your attack surface」「Scan from your shell」「Scan pull requests in GitHub Actions」と、h3「Watch a running scan」「Continue a stopped scan」「Run a more thorough change scan」「Tell a scan about your system」「Patch from an older report」が加わりました。内容はハイライト 3 にまとめました。

手順の書き方も変わっています。「Scan and fix your codebase」の手順は、作業ツリーをきれいにする段階が先頭に加わって 6 段から 7 段になり、報告の置き場所は「リポジトリの中」から「Claude Code を始めたフォルダーの中」になりました。報告のディレクトリの `.gitignore` を読まないパッケージングやデプロイのツールがあるので、その間は報告を外へ移す、という注意も加わっています。インストールではユーザーのスコープを選ぶとどのプロジェクトでも使えること、コマンドかオプションが効かなければ版 0.13.0 以降かを確かめること、スキャンの費用はリポジトリの大きさ・スキャンの努力・モデルで増えること、が加わりました。

- [コードベースの脆弱性をスキャンする - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/claude-security#scan-from-your-shell)
- [Scan your codebase for vulnerabilities - Claude Code Docs (English)](https://code.claude.com/docs/en/claude-security#scan-from-your-shell)

## 4. Connect Claude Code to tools via MCP

**`mcp` は 240 行（追加 222・削除 18）が変わりました。** 半分ほどは h2「Use skills from MCP servers」とその下の h3・h4 で（ハイライト 1）、残りは MCP タスクを使える場所が広がったことによるものです。MCP タスクの注記からは「パブリックベータ」が外れました。

- **MCP tasks in VS Code and the desktop app**: VS Code の拡張機能と Desktop アプリのローカルのセッションでも、v2.1.331 以降とフィーチャーフラグの取得があれば MCP タスクが働きます。Desktop の claude.ai のコネクターと `claude_desktop_config.json` のサーバーにはタスクがなく、どちらのアプリもタスクの質問を示さないので、質問するタスクはターミナルで使います。タスクは VS Code の `/tasks` か Desktop の **Background tasks** の枠で見て止められます
- **MCP tasks in cloud sessions and claude.ai chats**: プロトコルのリビジョン `2026-07-28` の claude.ai のコネクターなら、自分で始めた Anthropic ホストの環境のクラウドセッションと、Pro・Max・Ultra・Team のプランの新しいチャットでタスクになります（Free と Enterprise、Cowork、スケジュールした作業は一部のアカウントだけ）。クラウドセッションでは `.mcp.json` やプラグインのサーバーにタスクはなく、プロジェクトのスレッド・シークレットのチャット・クラウドのスケジュールタスクでもタスクになりません。サブエージェントの呼び出しもタスクになり、2 分以内に終われば結果をサブエージェントが受け取ります
- **クラウドでの質問・確認と停止・結果**: h4「Answer an MCP task's question in the cloud」「Check or stop an MCP task in the cloud」「Get an MCP task's result in the cloud」が、許可のプロンプトで **Allow** を選んでフォームで答える、`stop the export task` のように Claude に頼んで止める、結果が届かなければメッセージを送って確かめさせる（7 日の追跡の上限に達した場合などの対処付き）、を述べます

「What a call needs to become an MCP task」の条件も変わりました。フィーチャーフラグを取得しないセッション（Amazon Bedrock やテレメトリーをオフにしたとき）でも、対話のターミナルのセッションで v2.1.317 以降ならタスクになり、メインの会話が始めたフォークでないサブエージェントの呼び出しも、フィーチャーフラグを取得する対話のターミナルのセッションで v2.1.331 以降ならタスクになります（サブエージェントのファイルで定義したサーバーを除く）。サーバーの作者向けには、クラウドでは状態の確認が `pollIntervalMs` より間遠になることがある（新しいタスクでは 1,000 から 30,000 ミリ秒、省くと最長 10 秒ごと、古いタスクでは 10 秒・30 秒ごとまで遅くなる）といった注記が加わっています。

- [MCP を使用して Claude Code をツールに接続する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/mcp#mcp-tasks-in-the-cloud)
- [Connect Claude Code to tools via MCP - Claude Code Docs (English)](https://code.claude.com/docs/en/mcp#mcp-tasks-in-the-cloud)

## 5. Troubleshoot /ship and /steward

**`ship-command-troubleshooting` は 104 行（追加 77・削除 27）が変わりました。** 表の行が 35 加わり 16 外れています（書き換えを含む）。h3「Your pull request is already open」（`/ship didn't commit your uncommitted work` や、`password.txt` のような名前のファイルを含むコミットを `/ship` が出さなかったときの対処）と、h4「Keep a custom /ship or /steward without renaming」（ユーザーの設定かプロジェクトの `.claude/settings.json` の `env` で `CLAUDE_CODE_DISABLE_SHIP` を `1` にし、組み込みの 2 つのコマンドをオフにする）ができました。

- **始まらないときのメッセージ**: プロンプトの提案を受け入れたとき（`Nothing started. This line counts only if you type it yourself`）、`CLAUDE_CODE_DISABLE_SHIP` が設定されているとき、`claude -p` で打ったとき、プラグインなどに同じ名前のコマンドがあるとき（同じ行をもう一度打つと組み込みのほうが走る）の行が加わりました。`/ship` が見つからないときの手順にも、サードパーティのプロバイダーか Claude apps gateway のセッションでは v2.1.331 以降が要る、`CLAUDE_CODE_DISABLE_SHIP` を確かめる、の 2 つが加わっています
- **watch が始まらない・止まった**: `I can't watch the branch with git alone`、`this session runs in the background`、`PATH` の空か相対の項目、`this gh is too old for a watch` の行と、止まった理由の `this session is in plan mode`・`you asked`・GitHub 以外のホストでの `a file that git or /steward relies on changed` が加わりました。理由のいくつかは言い方が変わり、2 つの言い方を並べた行は、後ろが v2.1.331 より前の言い方だ、という注記が付いています
- **watch の間のメッセージ**: `←` や `/background` を押したときの `A watch is on` などの行が加わり、`gh couldn't say where the pull request's head and base stand` は、Claude Code が Claude のプッシュの 1 つを拒んだ、という意味に変わりました（GitHub CLI が古いのは v2.1.331 より前の原因）

- [/ship と /steward のトラブルシューティング - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/ship-command-troubleshooting#your-pull-request-is-already-open)
- [Troubleshoot /ship and /steward - Claude Code Docs (English)](https://code.claude.com/docs/en/ship-command-troubleshooting#your-pull-request-is-already-open)

## 6. Hooks reference

**`hooks` は 100 行（追加 89・削除 11）が変わりました。** ほとんどは h3「PreSkillShellCommand」と、その下の h4「Commands that reach a PreSkillShellCommand hook」「PreSkillShellCommand input」「PreSkillShellCommand decision control」、各表への追加です（ハイライト 2）。ほかに次の変化があります。

- **`PreToolUse` の警告**: `PreToolUse` は Claude がツールを呼んだときに走り、injected command には発火しない、という段落が先頭に加わった
- **外れた段落**: 内容の書き換えのためには、外へ出るツールの入力を `PreToolUse` で、成功した呼び出しの結果を `PostToolUse` で受ける（`PostToolUseFailure` は結果を書き換えられない）、という段落
- **`SessionStart` の例**: 共有のスキルのリポジトリを clone する例が `git -c protocol.file.allow=never clone` になり、フォルダーのパスからは clone できない、と注記された
- **言い方の変化**: 「Bash のコマンドの前に」が「Bash のツールの呼び出しの前に」に、プラグインだけのロックの説明が「組織にいるなら、管理者が」に、`if` の欄の「決して走らない」が「走らない」になった

日本語版の `hooks` には、まだ `PreSkillShellCommand` の節がありません。

- [Hooks reference - Claude Code Docs (English)](https://code.claude.com/docs/en/hooks#preskillshellcommand-decision-control)

## 7. Get a pull request ready with /ship and /steward

**`ship-command` は 89 行（追加 67・削除 22）が変わりました。** h3「Watch a branch on another host」と h4「Checks and comments on GitLab, Bitbucket, and Azure DevOps」が加わり、「What /ship commits and pushes」の場合分けが、ほかの人のプルリクエスト・自分のプルリクエスト・既定のブランチにだけコミットがある場合に分かれました（ハイライト 4）。「What ends a watch」の表には、GitHub 以外のホストの行（リモートからブランチが消えた、ベースに足すものがなくなった、7 日たった）と、plan モードで終わる場合が加わり、バックグラウンドへ送ると終わる、は v2.1.331 より前のこととされました。引数の表には `origin/main` の行が、組織でオフにする方法には `CLAUDE_CODE_DISABLE_SHIP` が加わっています。

- [/ship と /steward でプルリクエストをマージ可能な状態にする - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/ship-command#what-ends-a-watch)
- [Get a pull request ready with /ship and /steward - Claude Code Docs (English)](https://code.claude.com/docs/en/ship-command#what-ends-a-watch)

## 8. Error reference

**`errors` は 79 行（追加 73・削除 6）が変わりました。** 新しい h3 と h4 が 1 つずつと、メッセージの索引の表の 32 行です。

- **Claude Code needs a recent sign-in**（h3）: Desktop の Code タブのローカル・WSL・SSH のセッションが新しい保存済みのサインインを要るときに出る `For security, Claude Code needs a recent sign-in.` の対処です。アカウントと組織ごとに、コンピューターごとに月に 1 回ほど求められるのは通常で、カードかバナーの **Sign in again** でサインインします。同じ条件で 3 週間以内にまた求められたら、Claude Desktop が v5.11492.0 より古くないかを確かめて更新します（それより前は、会社のプロキシかゲートウェイがバックグラウンドの更新に JSON のエラーを返すと、保存したサインインを失うことがあった）。`desktop` の「403 or authentication errors in the Code tab」からもこの節へ案内されます
- **When the retry watchdog stops retrying**（h4）: `CLAUDE_CODE_RETRY_WATCHDOG` を設定しても、使用量のクレジットの支出の上限かゲートウェイの支出の上限の `429`、使い切ったクレジットの `429`、`x-should-retry: false` のヘッダーの付いた `429` か `529` では、リトライを止めます（支出の上限とクレジットの場合は v2.1.239 以降、`x-should-retry` の場合は v2.1.311 以降）。`CLAUDE_CODE_MAX_RETRIES` と `CLAUDE_CODE_RETRY_WATCHDOG` の表の行も短く書き直されました（`env-vars` と Agent SDK のページも同じ）
- **索引の表の新しい行**: クラウドセッションの `Authentication error · This may be a temporary network issue`、エージェントビューの `login required — run /login`、`Your authentication token belongs to organization`、`Failed to resolve base branch "HEAD"`、`Cannot use PR/MR #<number>`、`GH_HOST names a host other than github.com`、`PreSkillShellCommand` の `Not run in /<name>`、プラグインと mod の読み込み・フックのメッセージ（9 行）、VS Code のメッセージ（6 行）、`-p` の実行での壊れた設定、ファイルのツールの `(*)` のルールの警告など

- [エラーリファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/errors#claude-code-needs-a-recent-sign-in)
- [Error reference - Claude Code Docs (English)](https://code.claude.com/docs/en/errors#claude-code-needs-a-recent-sign-in)

## 9. Run tool calls from code with Code Mode

**`code-mode` は 72 行（追加 48・削除 24）が変わりました。** 「Requirements」の「Account」が「Account or provider」になり、Claude のサブスクリプションと Console のアカウントに加えて、Amazon Bedrock・Google Cloud の Agent Platform・Microsoft Foundry のようなクラウドプロバイダーでも、v2.1.331 以降なら Code Mode を使えるようになりました。ゲートウェイ経由と Claude for Government では使えず、Enterprise Admin Console のサインインでクラウドプロバイダーに届くときは、Agent Platform か Mantle のエンドポイントでない Amazon Bedrock が要ります。`feature-availability` のプロバイダーごとの表でも、Code Mode の 5 つの列が ✗ から ✓（実験的）になり、各プロバイダーのタブの「使えない」の一覧から Code Mode が外れました。

- **新しい h3「Use Code Mode in subagents」**: サブエージェントに `tools` の一覧があれば、`REPL` を加えると Code Mode を使う
- **新しい h3「Tool call ran after a hook failed」**: `command` か `http` の `PreToolUse` フックの `onFailure` が未設定・`"block"`・`"continue"` のとき、タイムアウトとほかの失敗でそれぞれ呼び出しがどうなるかの表（未設定では、タイムアウトは拒まれ、ほかの失敗はパーミッションの確認へ進む）
- **要件の追加**: mod がツールの呼び出しをフックするなら v2.1.327 以降。モデルをデプロイの名前か推論プロファイルで選ぶなら、それがどのモデルを指すかを管理者に尋ねる
- **始まらないときの表**: `it isn't offered yet through a gateway or proxy`（2 行）と `couldn't read your organization's settings or policy` の行が加わり、モデルの行は `--model claude-opus-5-5` のような完全な名前を渡し、プロバイダーによって古いモデルを選ぶ `sonnet` のような別名は避ける、になった
- **そのほか**: 再開の制限に、サブスクリプションか Console で走ったセッションはクラウドプロバイダーで再開できない、が加わった。クラウドプロバイダーで使える利用者がいるなら、Code Mode を止める設定は MDM か managed settings のファイルで配る（server-managed settings を受け取らないため）。フックで出力を隠すときは `imagePagesFailed` と（v2.1.331 以降）`uncutOutputNote` も扱う

`desktop` の Desktop で使えない機能の一覧にも Code Mode が加わり、`tools-reference` には `REPL` の行が加わりました。

- [Code Mode でコードからツール呼び出しを実行する - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/code-mode#requirements)
- [Run tool calls from code with Code Mode - Claude Code Docs (English)](https://code.claude.com/docs/en/code-mode#requirements)

## 10. Tools reference

**`tools-reference` は 69 行（追加 48・削除 21）が変わりました。** 「WebFetch tool behavior」の h3「When a fetch prompts, fails, or WebFetch is missing」の 1 つの表が、「Fix unexpected WebFetch prompts and denials」「Fix a failed WebFetch request」「Fix missing or outdated page content」「Find out why WebFetch is unavailable」の 4 つの h3 に分かれました。4 つ目は HTML の id が `#webfetch-availability` のままなので、元の h3 を改称したものです。4 つ目には、`/status` にどちらの行も出なければ、設定ファイルの `deny` の `WebFetch` か、`1` の `CLAUDE_CODE_DISABLE_WEB_FETCH` を探す、という段落が加わりました。

- **新しい行**: ツールの表に、Code Mode で Claude が書いた JavaScript を走らせる `REPL` の行が加わり、Skill の行には MCP のスキルでもプロンプトが出る、が加わった
- **作業ディレクトリ**: メインのセッションで Claude の `cd` が後の Bash のコマンドに引き継がれるのは、終了コード 0 で終わったフォアグラウンドのコマンドからだけ、と明記された。PowerShell では h3「Working directory and variables in PowerShell commands」ができた
- **バックグラウンド**: 対話のセッションでは、バックグラウンドのサブエージェントのコマンドがタイムアウトの前の 3 分でバックグラウンドへ移ることがあり、結果に `Command was moved to the background (ID: <id>) after running for 180s` が入る

- [ツールリファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/tools-reference#fix-unexpected-webfetch-prompts-and-denials)
- [Tools reference - Claude Code Docs (English)](https://code.claude.com/docs/en/tools-reference#fix-unexpected-webfetch-prompts-and-denials)

## 軽微な更新

<!-- light:minor-updates:start -->
今回の差分は **3 ファイル**（`llms.txt`・`llms-full.txt`・見出しマップ）です。`llms.txt` は `slack` の説明文の 1 行だけが変わりました（441 行のまま）。`llms-full.txt` では既存の **110 ページ**（changelog を含む）の内容が変わりました。大幅更新の 10 ページと changelog を除く **99 ページ**と、changelog に加わった **v2.1.332（2026年11月25日、150 項目。Added 11・Changed 27・Improvements 19・Bug fixes 93）** を以下にまとめます。単一のリリースなので、changelog の各項目への版の併記は省いています。新着情報（whats-new）のページはありません。

**新機能**

- MCP サーバーのスキル（`skills`・`settings-reference`・`managed-settings`・`feature-availability`・`headless`・`env-vars`・`tools-reference`・`plugins/mods/admin`・`plugins/mods/reference`。詳細はハイライト 1 参照）
- `PreSkillShellCommand` のフック（`hooks-guide`・`debug-your-config`・`skills`・`errors`。詳細はハイライト 2 参照）
- GitHub 以外のホストでの `/ship` と `/steward` の watch と、`CLAUDE_CODE_DISABLE_SHIP`（`env-vars`・`agent-view`・`commands`。詳細はハイライト 4 参照）
- クラウドプロバイダーでの Code Mode と `REPL` ツール（`feature-availability`・`desktop`・`sub-agents`・`tools-reference`。詳細は大幅更新 9 参照）
- **Desktop アプリの Code タブで全ユーザーにスキルを配る h4 ができた**（`desktop` の「Deploy skills for all users」）。ローカルと SSH のセッションのすべての利用者に同じスキルを渡すには、セッションが走るマシン（ローカルなら各利用者のコンピューター、SSH なら各リモートのホスト）に enterprise のスキルとして入れる、という説明と、macOS・Linux・Windows のパス（Linux は `/etc/claude-code/.claude/skills/<skill-name>/SKILL.md`）の表、`name` と `description` だけのスキルで読み込みを確かめる手順が載っています — [日本語](https://code.claude.com/docs/ja/desktop#deploy-skills-for-all-users) / [English](https://code.claude.com/docs/en/desktop#deploy-skills-for-all-users)
- **作業ディレクトリの外のファイルにツールを許す h4 ができた**（`permissions` の「Allow a file tool outside the working directories」。2 回載るページの 2 か所とも）。`Edit(*)`・`Write(*)`・`NotebookEdit(*)` の `allow` のルールは作業ディレクトリの中だけを事前に許すので、外も許すにはツールの名前だけ（`Edit` など）を書く、`Read(*)` のルールに `adds nothing to Read's default` の警告が出たら消してよい、という説明です。v2.1.317 より前の版はこのルールを名前だけと同じに扱うので、作業ディレクトリの外を止めるのにこのルールに頼らない、という警告付きです。`errors` の索引にもこの警告の行が加わりました — [日本語](https://code.claude.com/docs/ja/permissions#allow-a-file-tool-outside-the-working-directories) / [English](https://code.claude.com/docs/en/permissions#allow-a-file-tool-outside-the-working-directories)
- **plugin の evals で組み込みのツールを外せるようになった**（`plugin-evals` の h3「Remove a built-in tool from runs」・`plugins/cli-reference`）。`--disallow-tools` で全ケースから、`prompt.md` か `case.yaml` の `disallowed_tools` で 1 ケースから組み込みのツールを外せます（v2.1.299 以降。`allowed_tools` から `Agent` を省いても Claude は呼べる）。h4「Pre-approve reads from another path」も加わり、`/data` の下を読ませるには `--allow-tools "Read(//data/**)"` のように `//` で始まる `Read` のルールを与える、`Read` などを並べただけではマシンのすべてのパスを許さない、と述べます。読み取り専用のツールは「付与される」から「事前に許される」という言い方になりました — [日本語](https://code.claude.com/docs/ja/plugin-evals#disallow-tools) / [English](https://code.claude.com/docs/en/plugin-evals#disallow-tools)
- **`-p` の実行で壊れた設定が標準エラーに出るようになった**（`settings` の h4「Broken settings in a `-p` run」）。既定の `text` の出力形式では、読み込まれなかった設定のファイル（フック・パーミッションのルール・サンドボックスの設定を含めて効かない）と、飛ばした項目が、`These settings did not load` と `These settings entries were skipped` に続けて並ぶ、という例が加わりました — [日本語](https://code.claude.com/docs/ja/settings#broken-settings-in-a-p-run) / [English](https://code.claude.com/docs/en/settings#broken-settings-in-a-p-run)
- **Claude Approvals のポリシーファイル全体の決まりの h2 ができた**（`approvals-policy` の「Rules for the whole file」）。キーと固定の値は小文字、目的・`paths` の型・条件は二重引用符、`!` の項目は条件の外では二重引用符・条件の中では単一引用符（引用符のない `!` の項目は拒まれる）、YAML は 1 つの文書でスペースで字下げ、という決まりを 1 か所にまとめました。`infra/` は拒まれる、空の一覧を調べるには `ANY` も `ALL` も付けずに `"pr/approved_by = empty"` と書く、人の一覧の `!` の項目は条件の中では `'!acme/interns'` のように単一引用符で囲む、も加わりました — [日本語](https://code.claude.com/docs/ja/approvals-policy#rules-for-the-whole-file) / [English](https://code.claude.com/docs/en/approvals-policy#rules-for-the-whole-file)
- **`/claude-approvals` のスキルが載った**（`approvals-setup`・`commands`・`env-vars`）。リポジトリで `/claude-approvals` に続けて望みを打つと、Claude がポリシーファイルを書くか変える、という TIP が「Plan your first policy」に加わりました（v2.1.331 以降。フィーチャーフラグの取得が要る）。同じ節の 2 つの最初のポリシーの説明は、作者だけで足りる・作者のほかに 1 人が要り Claude はコメントだけ、という言い方になっています — [日本語](https://code.claude.com/docs/ja/approvals-setup#plan-your-first-policy) / [English](https://code.claude.com/docs/en/approvals-setup#plan-your-first-policy)
- **Claude Approvals の問題の対処が増えた**（`approvals-troubleshooting`・`approvals`）。h4「Check for a GitHub IP allow list」（組織の IP の許可リストにない Anthropic のアドレスからの要求を GitHub が拒むと、チェックもコメントも出ないことがある）と、`a login goes in single quotes inside a condition` のメッセージの行、分類器の 1 回の実行で読み切れない大きな差分には小さなプルリクエストを試す、が加わり、`Claude Approvals can't start in this repository yet` の行が外れました。`approvals` には、承認のレビューを github.com では `claude[bot]` が、`claude[bot]` が開いたプルリクエストでは `claude-approvals[bot]` が出す、と書き分けられました — [日本語](https://code.claude.com/docs/ja/approvals-troubleshooting#check-for-a-github-ip-allow-list) / [English](https://code.claude.com/docs/en/approvals-troubleshooting#check-for-a-github-ip-allow-list)
- **コマンドの表に `/motion` と `/whiteboard` が加わった**（`commands`）。どちらもバンドルのスキルで、`/motion` は説明から Claude Motion のアニメーションのアーティファクトを（Desktop アプリのローカルのセッションと Anthropic ホストのクラウドセッションだけ）、`/whiteboard` は Claude Whiteboards のアーティファクトを作ります。どちらも v2.1.323 以降と、テンプレートを使えるアカウントが要ります。`/claude-approvals` の行も加わり、`/privacy-settings` は claude.ai の設定へのリンクを出すこともある、になりました — [日本語](https://code.claude.com/docs/ja/commands#all-commands) / [English](https://code.claude.com/docs/en/commands#all-commands)
- **VS Code の拡張機能のコマンドと設定が加わった**（`vs-code`）。ノートブックのセルとその出力をプロンプトの欄に加える「Add Cell to Chat」、競合の解消を頼む「Resolve Merge Conflicts」のコマンドと、エディターのエラーや失敗したテストに **Fix with Claude Code** を出す設定 `showFixActions` で、どれも v2.1.331 以降です。トラブルシューティングの表には `Failed to set model: Settings file is not valid JSON` の行が加わりました — [日本語](https://code.claude.com/docs/ja/vs-code#extension-settings) / [English](https://code.claude.com/docs/en/vs-code#extension-settings)
- **ツールで送ったメッセージも `assistant_response` のイベントになった**（`monitoring-usage`）。`SendUserMessage` か Cowork の `mcp__cowork__send_user_message` の呼び出しが成功すると、`tool_use_id` の付いた `assistant_response` のイベントが記録されます（v2.1.332 以降。応答のテキストを含める設定のときだけ）。`request_id` と `message.uuid` の説明も、これに合わせて書き分けられました — [日本語](https://code.claude.com/docs/ja/monitoring-usage#assistant-response-event) / [English](https://code.claude.com/docs/en/monitoring-usage#assistant-response-event)
- **mod の API が増えた**（`plugins/mods/reference`・`plugins/mods/create`・`plugins/mods/events`・`plugins/mods/test`・`plugins/mods/troubleshoot`）。`tool.offer` のイベントと h4「Send a changed tool list」（v2.1.331 以降）、`BesidePrompt`・`Underlay` などの描画の場所、`$.session.redact`、`$.ui.view` の説明、ほかの mod が加えたメソッドの 10 秒の制限が加わりました。`plugins/mods/create` の h4「Pass `$` to your functions」は、v2.1.299 以降なら別のファイルから読み込んだ `function` の関数にも `$` を渡せる、と述べ、`tol.call` のような綴りの誤りは検証を通ってしまう、という例も加わりました。テストのツールには `drawn()` が、トラブルシューティングには h3「`call refused` or `result withheld`」が加わっています — [日本語](https://code.claude.com/docs/ja/plugins/mods/troubleshoot#call-refused-or-result-withheld) / [English](https://code.claude.com/docs/en/plugins/mods/troubleshoot#call-refused-or-result-withheld)
- **Agent SDK の起動失敗の理由が 1 つ加わった**（`agent-sdk/typescript`）。managed の `disableSideloadFlags` に反するフラグか起動オプションのときの `sideload_flags_disabled` です（TypeScript の Agent SDK v0.3.331 以降と Claude Code v2.1.331 以降）。`agent-sdk/python` の Monitor の入力の型には `keptInSandboxByCheck` が加わりました
- Added: MCP サーバーのスキル（ベータ）。`/` のメニューに `server:skill` で出て、ほかのスキルは名前を保ちます（詳細はハイライト 1 参照）
- Added: スキルやコマンドの読み込み時に、その中のシェルのコマンドを拒める `PreSkillShellCommand` のフックのイベント。2.1.331 以前では、このイベントを書いた設定ファイルがあると起動時にダイアログが開きます（詳細はハイライト 2 参照）
- Added: ほかのセッションからの保留したメッセージのプロンプトに「Always deliver」
- Added: 指摘されたメッセージのためにセッションが別のモデルで動いている間、`/model` で選ぶまで残るフッターの行
- Added: 応答の記録がオンのとき、Claude が SendUserMessage か Cowork のメッセージのツールで送るテキストの OpenTelemetry の `assistant_response` のイベント
- Added: VS Code と Desktop の Code タブで、セッションの一部を保存できなかったときに `/compact` で保存する方法を述べる警告
- Added: VS Code と Desktop の Code タブで、再開したセッションの以前のメッセージが読み込まれなかったときの通知（ターミナルではすでに出ていたもの）
- Added: 起動時のヘッダーに Cyber Verification Program のアクセスの段階（その段階がモデルに当てはまり、claude.ai のアカウントでサインインしているとき、モデルの名前の隣）
- [VSCode] Added: 提案された diff を閉じて編集が当たらないままになる場合の通知を増やし、答えた diff の分割した写しでは diff の通知を出さないように
- [VSCode] Added: サイドバーの `/rewind` で会話を戻すと自分のペースの `/loop` が止まるときの警告
- [VSCode] Added: Manage plugins の行にインストールした版

**機能改善**

- **繰り返しのタスクの期限が 7 日から 30 日になった**（`scheduled-tasks` の h3「Seven-day expiry」→「Recurring task expiry」）。セッションのスコープの繰り返しのタスクは作ってから 30 日で期限が来ます。v2.1.330 より前は 7 日で、その版で `CronCreate` で作ったタスクは 7 日のままです。自分のペースの `/loop` と決まった間隔の `/loop` も、始めてから 30 日で終わる、になりました（HTML の id は新旧の両方がある）— [日本語](https://code.claude.com/docs/ja/scheduled-tasks#recurring-task-expiry) / [English](https://code.claude.com/docs/en/scheduled-tasks#recurring-task-expiry)
- **クラウドのスケジュールタスクの警告の h3 が改称された**（`routines` の「"The last run" warnings」→「Warnings under History」）。同時に動かせるタスクの上限で走らなかった回の警告が「This didn't run」で始まる 2 つの文面になり、環境が見つからないときの文面は「its cloud environment」から「its environment」になりました（HTML の id は `#the-last-run-didnt-start` のまま）— [日本語](https://code.claude.com/docs/ja/routines#the-last-run-didnt-start) / [English](https://code.claude.com/docs/en/routines#the-last-run-didnt-start)
- **worktree のセッションの再開の節が分かれた**（`worktrees`・`best-practices`）。「Resume a worktree session」の冒頭に、残した worktree に戻るには本体のチェックアウトから `claude --worktree <name> --resume <session-id>` を走らせる（`<name>` は `.claude/worktrees/` の下のフォルダーの名前で、`+` は `/` に置き換える）という段落ができ、以前の内容は h3「Resume without `--worktree`」と「Transcript location」に分かれました。サブエージェントの worktree は、git が変更・未追跡のファイル・新しいコミットを示せば残す、`.claude/worktrees/` の外に `git worktree add` で作った worktree は掃除で残す、と書き直され、`--worktree` に渡した URL のホストとリポジトリは無視され、GitHub と GitLab 以外のホストでは URL の種類で `pull/` か `merge-requests/` を選ぶ（`#` の番号で両方が別のコミットにあれば `Cannot use PR/MR #<number>` に従う）、になりました — [日本語](https://code.claude.com/docs/ja/worktrees#resume-a-worktree-session) / [English](https://code.claude.com/docs/en/worktrees#resume-a-worktree-session)
- **スキルの `model` のフロントマターの効く範囲が明記された**（`skills`・`prompt-caching`）。`model` は `/name` でスキルを走らせたターンのモデルで、Claude がスキルを走らせたときはセッションのモデルのままです。`prompt-caching` には h4「Skills and commands that set a model」ができ、`model` の値が効いてセッションのモデルと違うときだけそのターンがモデルの切り替えになる、`context: fork` では値がサブエージェントに行き、そのキャッシュは別、と述べます。引数のプレースホルダーの説明も、位置に引数がないとき番号のもの（`$1`）は文字どおりに残り、名前のもの（`$issue`）は空になる、と箇条書きになりました — [日本語](https://code.claude.com/docs/ja/prompt-caching#skills-and-commands-that-set-a-model) / [English](https://code.claude.com/docs/en/prompt-caching#skills-and-commands-that-set-a-model)
- **`claude -p` の stream-json の `result` の読み方が変わった**（`headless`）。ストリームの最後の行が `result` だ、という説明が、タスクの通知のようなメッセージが `result` の後に続いて次のターンを始めることがあるので、`result` のメッセージは `type` で探す、になりました — [日本語](https://code.claude.com/docs/ja/headless#get-structured-output) / [English](https://code.claude.com/docs/en/headless#get-structured-output)
- **PR Steward の環境とコメントの行が増えた**（`pr-steward-setup`・`pr-steward-troubleshooting`）。組織の既定の環境がセルフホストなら、PR Steward 用に **Where it runs** で環境を選ぶまで始まらないことがあり、セルフホストのランナーには Claude Code v2.1.317 以降が要ります。トラブルシューティングには、環境が選ばれていない・使えない・ランナーが古い、の 3 つのコメントの行が加わりました。支出は「平均」から「見積もり」の言い方になっています — [日本語](https://code.claude.com/docs/ja/pr-steward-setup#choose-the-environment-pr-steward-runs-in) / [English](https://code.claude.com/docs/en/pr-steward-setup#choose-the-environment-pr-steward-runs-in)
- **セッションの共有の設定の場所が 1 つになった**（`share-sessions`）。**Require repository access** と **Show your name** を変えるのは、Settings のメニューの形によらず **Settings > Privacy** の **Shared Code sessions** の隣の **Manage** になりました。リンクが開かない原因からは Free プランの行が外れ、**Public** のリンクを共有した後に Free プランへ移った場合（Max・Ultra・Pro へ上げると同じリンクが開く）の行が加わっています — [日本語](https://code.claude.com/docs/ja/share-sessions#share-a-session) / [English](https://code.claude.com/docs/en/share-sessions#share-a-session)
- **アーティファクトの説明が削られた**（`artifacts`・`permissions`・`env-vars`・`permission-modes`）。場所を名指さなければ一時ディレクトリにページを書く、ページを HTML の殻で包む、他人のページは WebFetch のように要約で読む、といった仕組みの説明が外れ、Claude Code が読む前に承認を求めるのは「Artifact ツールが読む前」と書き直されました。公開の前の承認は `bypassPermissions` モードの外のこと、と明記され、見守りが終わったときのメッセージは `(idle)`・`(connection lost)`・`(made room for a newer watch)` を並べて、アーティファクトを公開し直すよう頼む、にまとまりました — [日本語](https://code.claude.com/docs/ja/artifacts#read-an-artifact-shared-with-you) / [English](https://code.claude.com/docs/en/artifacts#read-an-artifact-shared-with-you)
- **Desktop アプリの Code タブの設定への案内が加わった**（`amazon-bedrock`・`google-vertex-ai`・`microsoft-foundry`）。各ページの冒頭に、Code タブでこのプロバイダーを使うには、組織が入れたアプリなら管理者に設定を頼み、自分で入れたなら単一のマシンのセットアップの手順に従う、という注記と、claude.com の設定のページへのリンクが加わりました — [日本語](https://code.claude.com/docs/ja/amazon-bedrock) / [English](https://code.claude.com/docs/en/amazon-bedrock)
- **セルフホストの環境の Stop フックのスクリプトがブランチの名前を出さなくなった**（`self-hosted-environments-configuration`）。プッシュしていないコミットを知らせるメッセージは、ブランチの名前の代わりに「プロジェクトのディレクトリでチェックアウトしているブランチ」と言うようになり、以前の写しは `checked out in the project directory` の文字列の有無で見分けて、すぐ置き換えるよう求めます — [日本語](https://code.claude.com/docs/ja/self-hosted-environments-configuration#replace-an-earlier-copy-of-the-stop-hook-script) / [English](https://code.claude.com/docs/en/self-hosted-environments-configuration#replace-an-earlier-copy-of-the-stop-hook-script)
- **そのほかのページの補足**: `agent-view` に、セッションの行に `∙` が出たら選んで `Enter` で再起動する、が、`claude-code-on-the-web` に、組織を通してサインインしているなら Owner にクラウドセッションがオンかを尋ねる、と、作り直した VM でもコネクターで動いている MCP タスクの追跡は戻る、が、`claude-projects` に、別のモードでスレッドを走らせるには `--settings` のファイルで `disableAutoMode` を `"disable"` にする、が加わりました。`sub-agents` では、インラインの MCP サーバーは最後に使うエージェントが終わったときに切れる、になり、ほかのエージェントからのメッセージは承認の代わりにならない、という注記から、設定や `CLAUDE.md` を変えられない、という部分が外れました。`troubleshoot-install` には `That code wasn't accepted` の行と、macOS の Keychain の警告ごとの手順が、`plugins/troubleshooting` にはフックの読み込みの失敗とブロックされたプラグインのメッセージが、`claude-apps-gateway-deploy` にはフィールドのパスで始まる `400` の行が、`desktop-ios-simulator` にはシミュレーターへのアクセスをオフにする節へのリンクが加わっています。`settings-reference` のファイルのチェックポイントのキーは、managed settings が `false` にしていれば `-p` と SDK でもオフのまま、になりました（v2.1.331 以降）
- Changed: macOS のコンピューターの使用を新しい安全の決まりに更新したので、一部の操作が拒まれ、打つのが遅くなることがあります
- Changed: Bedrock Mantle・Agent Platform・Foundry で Sonnet 5 か 5.5 に移ったターミナルと VS Code のセッションは、モードの設定がなければ auto モードで始まるように。止めるには `disableAutoMode` を `"disable"` に
- Changed: Google Cloud の Agent Platform と Microsoft Foundry の `sonnet` の別名を Sonnet 5.5 に、Foundry の `opus` の別名を Opus 5.5 に。Amazon Bedrock の `sonnet` は Sonnet 4.5 のまま
- Changed: Microsoft Foundry の既定のモデルを Sonnet 5.5 に。`claude-sonnet-5-5` をデプロイするか、デプロイしたモデルを `ANTHROPIC_DEFAULT_SONNET_MODEL` に設定します
- Changed: Google Cloud の Agent Platform の `sonnet` とバックグラウンドの要求が `VERTEX_REGION_CLAUDE_5_5_SONNET` を読むように。`4_5` の変数だけなら `CLOUD_ML_REGION` か `us-east5` へ行きます
- Changed: `--model default` と Default の選択が、そのモデルを使えないときにエラーで止まらず古いモデルへ移るように（auto モードでは、auto モードが受け付けるモデルへだけ）
- Changed: Microsoft Foundry で Claude Sonnet 4・Opus 4・Opus 4.1 を引退扱いに。段階的な切り下げはその手前で止まり、それへの固定は引退した、と警告します
- Changed: Claude apps gateway の組み込みのモデルの一覧で、2 つ目のモデルを Sonnet 4.5 から Sonnet 5.5 に。ポリシーが Opus 4.6 を許さないところでは Claude Desktop がそれで始まります
- Changed: フィーチャーフラグを取得しないところ（クラウドやテレメトリーがオフのとき）で、SDK と `claude -p` のターンの途中のメッセージを Opus 4.8 からはユーザーのものとして数えるように。中継したテキストは `isSynthetic: true` と印します
- Changed: コンピューターの使用がオンの Mac で `computer-use` を予約されたスキルの名前に。同じ名前の自分のスキルかコマンドは読み込まれなくなり、起動時の通知が名前を変えるよう言います
- Changed: Desktop の Code タブのセッションの OpenTelemetry の既定の `service.name` を `claude-code-desktop` に。`claude-code` で絞るフィルターを直すか、`OTEL_SERVICE_NAME` で古い名前を保ちます
- Changed: OpenTelemetry の `tool_input` で、SendUserMessage か Cowork のメッセージのツールで送るテキストは、応答の記録がオン（`OTEL_LOG_ASSISTANT_RESPONSES=1`）でなければ長さだけを示すように
- セルフホストのランナー: Changed: `CLAUDE_CODE_OAUTH_TOKEN` の接頭辞が `oat01-` に加えて `oat02-` で終わりうるように。`oat01-` に合わせたプロキシのルールとログの消し込みを直し、値の全体を隠します
- Changed: macOS と Linux で引数なしの `claude self-hosted-runner setup` が、Claude の起動前にターミナルで環境のキーを尋ね、貼り付けを隠すように
- Changed: Anthropic の API の Claude Desktop の Code タブで、ゲートウェイのアドレスの隣の自分の設定にある、`claude` で始まらない既定・サイドの要求・別名・サブエージェントのモデルの ID を無視するように
- Changed: Anthropic の API の Claude Desktop の Code タブで、ゲートウェイのアドレスの隣の自分の設定にある 200K 未満の `CLAUDE_CODE_AUTO_COMPACT_WINDOW` を無視するように。代わりに `/autocompact` を使います
- Changed: Desktop アプリの Code タブと VS Code の plan モードで、auto モードの安全の確認がコマンドを判断できないとき、Manual か Accept edits から入った計画なら拒まずに承認を求めるように
- Changed: エージェントのビューからの `/clear` のような破壊的な質問で、PgUp と Home が No へ行くように
- Changed: ターミナルの `/feedback` の下書きが Not now で開き、報告だけか会話の記録付きで送る別々の行がその上に並ぶように
- Changed: タップのモードの音声入力が、新しい言葉なしに 60 秒か 10 分（これまでは 15 秒と 2 分）までマイクをオンに保ち、テキストを送らずに残すように。次のタップでそれに足します
- Changed: タップのモードの音声入力が、プロンプトを送ると止まり、編集したとき・パネルが覆ったとき・接続か別の録音のプログラムを失ったときは、止まって理由を言うように
- Changed: `/schedule`・パーミッションのプロンプト・`/loop` のクラウドの提案が「routine」や「cloud schedule」の代わりに「cloud scheduled task」と言うように。`/routines` も引き続き使えます
- Changed: Claude のモバイルアプリか claude.ai からのモデルの切り替えで、新しいモデルに保存した努力の度合いがなければ、前のモデルに保存した度合いを保つように
- Changed: フルスクリーンのフッターの右にラベルがあるとき、mod の `PromptHint` のフックが受け取る `hint` から、選んだテキストのヒントを省くように
- Changed: `awsCredentialExport` が、いつまでも待たずに 10 分でタイムアウトするように
- [VSCode] Changed: 音声入力が、認識した発話なしに 60 秒か 10 分（これまでは 15 秒と 2 分）たつと自分で止まり、マイクを長くオンにできるように
- [VSCode] Changed: マイクが音声を送らなくなったとき、またはパネルが隠れたままのとき、音声入力が止まって理由を言うように
- Improved: Windows の `claude plugin marketplace add` が、ウイルススキャナーのようなほかのプログラムがダウンロードしたファイルを少しの間つかんでいるときに、待って試し直すように
- Windows: Improved: 起動の直後に何も出さずに終わることがあった一部の会社の PC での安定性
- Improved: コンピューターの使用のセットアップで、画面収録の許可のプロンプトが Claude Code を再起動して会話を再開できるように
- Improved: コンピューターの使用が、Claude が使うまでコンテキストを少なく取るように
- Improved: プロキシかゲートウェイが圧縮した応答を切るか壊したときのエラーが、生の「ZlibError fetching」ではなくふつうの言葉でターンを終えるように
- Improved: `/context` のフルスクリーンでの出力を短くし、短いウィンドウで合計がスクロールで消えにくく、凡例が単位を 1 回だけ名指すように
- Improved: 最近のセッションの多いマシンでの `/usage` のメモリーの最大の使用量と速さ
- Improved: `/permissions` が、次の起動で飛ばされるルール（ツールの名前のない `rm -rf` など）を拒み、理由を示すように
- Improved: Code Mode でのセッションの再開で、以前のスクリプトの変数がなくなったことを最初に Claude に伝えるように
- Improved: Code Mode の Claude が、worktree の変更を捨てる前に確かめ、公開の前にアーティファクトのファイルを読み、2 つ目を作らずに既存のアーティファクトを更新するように
- Improved: Code Mode のツールの検索が、長い MCP のツールの説明を、収まるところでは切らずに示すように（切った説明は誤った呼び出しにつながりうる）
- Linux: Improved: クリップボードから画像を読めないとき、Ctrl+V のメッセージが入れるパッケージ（`wl-clipboard` か `xclip`）を名指すように
- Improved: 要求の大きさに上限のあるプロキシかゲートウェイの裏で、すべてのメッセージと `/compact` が 413 で失敗していた長い会話の回復
- Improved: CPU が 6 つ以上の Windows のマシンの大きなローカルのフォルダーでの Glob の速さ。フォルダーを並列にたどり、時間の上限で止まった検索は見つけたものを挙げます
- Improved: 長い会話を再開するときのメモリーの使用量
- Improved: ツールを多く挙げる MCP サーバーのある起動時のメモリーの使用量
- Improved: `claude -p` と SDK が動かすセッションの会話の始めのメモリーの使用量
- [VSCode] Improved: Claude のパネルと長いセッションを開く時間、長い返答を流す間の性能、とても大きなワークスペースでの診断の読み取りの速さ
- [VSCode] Improved: プレーンテキストのタブで開いたコマンドと 1 行の出力が折り返すように

**バグ修正**

- claude.ai のログインを保存できなかったのに `claude auth login` が `Login successful.` と報告する問題を修正。終了コード 1 で終わり、残ったロックのファイルや満杯のディスクのような確かめるものを言います
- 鍵のかかった秘密の管理のツールがマウントした `.env` のような、誰も書き込まない名前付きパイプで、Read・@-メンション・コンパクションが止まる問題を修正。読み取りは 20 秒で失敗します
- 自動のコンパクションの失敗が続いた後、コンテキストの上限でもう 1 回コンパクションすれば続けられたのに、ターンが「Prompt is too long」で終わる問題を修正
- 要約が出力の上限を超えて続くときにコンパクションが失敗する問題を修正。切れた返答が 3 回続くと、最後の試みで短い要約を求めます
- ワイルドカードの多いパーミッションのルールかフックの条件を長いコマンドに当てると固まる問題を修正
- フックが終わりなく出力する間に固まり、メモリーを使い続ける問題を、ほとんどの場合で修正
- ターンの間か `/compact` の後に、フックがとても大きなログでブロックか失敗すると固まり、コンテキストがあふれる問題を修正。約 50,000 文字を超えるテキストは短くします
- ローカルの MCP サーバーが標準出力をあふれさせる間、ターミナルが固まって Ctrl+C を無視する問題を修正
- プロンプトかパイプの入力に、`@` に続くとても長い切れ目のない文字列（フォントを埋め込んだ縮めた CSS など）があると固まる問題を修正
- 大きな追跡しているファイルが書き直された後、rewind の地点を開くと長く固まる問題を修正
- SSE の MCP サーバーが、イベントのストリームが切れて新しいエンドポイントで戻るか戻らなかった後、手で再接続するまで止まるか、すべてのツールの呼び出しを拒む問題を修正
- Desktop アプリ・VS Code・Agent SDK のセッションが、ダイアログか MCP サーバーの質問で待っている間、Remote Control に動いていると示される問題を修正
- 使用量の上限がリセットされた後に、Remote Control・IDE・SDK のクライアントへ上限に達したと報告される問題を修正
- EnterWorktree で `.claude/worktrees` の下の worktree に移るかそこで再開した後、CLAUDE.md とルールのファイルがモデルに 2 回送られる問題を、ほとんどの場合で修正
- 再起動したセッションでパーミッションのプロンプトを断った後、claude.ai のチャットの要約の行で、走らなかったツールの呼び出しが済んだと数えられる問題を修正
- Linux: Claude がシンボリックリンクを通してファイルを読んだ後、Bash の編集の diff が変わっていないシンボリックリンクを編集したと示す問題を修正
- 会話の記録に壊れた行が多いと、セッションの再開と `/stats` が数秒固まる問題を修正
- `availableModels` がその古い版だけを許すとき、`--fallback-model` の `sonnet` のようなファミリーの名前が落ちる問題を修正
- `/stats` が大きなセッションの記録を読む間（ダイアログを閉じた後も）や、デバッグのログがオンで言語サーバーが stderr をあふれさせる間、キーが数秒遅れる問題を修正
- クラウドが既定のモデルを拒み、強制されていない `availableModels` の一覧がそれもそのファミリーの古いモデルも名指さないとき、セッションが失敗する問題を修正
- Google Cloud の Agent Platform と Foundry で、強制された古いモデルの一覧の最初のものが拒まれると失敗する問題を修正。新しい順に並べてあれば、そのファミリーの次のものへ切り下げます
- 自分の言葉でモデルを拒むゲートウェイの裏の Bedrock・Google Cloud の Agent Platform・Foundry で `opus` が失敗する問題を修正。答える古いモデルへ切り下げます
- Bedrock と Google Cloud の Agent Platform の起動時のモデルの更新の提案が、`availableModels` の一覧にないモデルを名指す問題を修正
- 親のリージョンにそのモデルのプロファイルがアカウントにないとき、Bedrock のサブエージェントが失敗する問題を修正。そのリージョンの外でありうるモデル自身のプロファイルを使います
- `sonnet`・`opus`・`haiku` が指す版を管理者の一覧が止めると、Foundry のセッションがモデルのファミリーを離れる問題を修正。組み込みかマップした名前で、許された最新の版を使います
- Bedrock Mantle の `sonnet` の別名が Haiku 4.5 になる問題を修正。Sonnet 5.5 ではなく Sonnet 5 を指し、Sonnet 5 のないアカウントはエラーになるので、先に有効にします
- 止めたバックグラウンドのエージェントに読んでいないサブエージェントの報告があるとき、プロンプトでの Ctrl+C が新しいターンを始め、2 回の Ctrl+C で終わらない問題を修正
- `/install-github-app` が、Esc で戻った後にワークフローにまた印を付ける問題を修正
- 10,000 文字を超える口述のテキストが失われる問題を修正
- ストリーミングでないリトライが壊れた応答を受けたか中断されたとき、生の「JSON Parse error」と「The operation was aborted.」の API のエラーが出る問題を修正
- macOS で、Claude Code のウィンドウか許したアプリが前にあるとき、操作の合間の Esc でコンピューターの使用が止まらない問題を修正。そのアプリのポップアップに向けた Esc も、コンピューターの使用を止めるようになりました
- API キーのヘルパーのような補助のコマンドが時間の上限を超えたとき、まれに止まる問題を修正
- フルスクリーンでテキストを選ぶとフッターの右のラベルが 2 行目に押し出され、マウスの下のテキストが動いて違う行をコピーしうる問題を修正
- ターミナルの Read・Grep・Glob・Edit・Write のプロンプトに、PreToolUse のフックが尋ねる理由が出ない問題を修正（anthropics/claude-code#102892、anthropics/claude-code#105343）
- ダウンロードしたプラグインを所定の場所へ写せなかったとき、`~/.claude/plugins/cache` に `temp_*` のフォルダーがたまる問題を修正
- `CLAUDE_CODE_EFFORT_LEVEL` が同じ度合いに設定されているとき、`--environment` で対話のセッションを始めると `--effort` が無視される問題を修正
- ヘッドレスとクラウドのセッションが、フォアグラウンドのフォークの Agent の呼び出しを、フォークが始まった瞬間に終わったと報告する問題を修正
- Remote Control のセッションのプロセスが再起動した後、ローカルの MCP サーバーに新しいセッションの ID が見える問題を修正
- 週の上限をまだ十分に下回る購読者で、アイドルのときのコンパクションが飛ばされる問題を修正
- 拡張子のある @-メンションしたテキストファイルが、最初の 2,000 行でも読み取りの上限を超えると黙って落ちる問題を修正。Claude にその大きさと読み方を伝えます
- プラグインの「not cached」のエラーが、プラグインを読み込み直すコマンドの `/reload-plugins` ではなく `/plugin` を指す問題を修正
- マシンの git の設定に `includeIf "gitdir:"` か（git 2.44 から 2.46 では）`"onbranch:"` の節があると、Anthropic が管理する git の下でセルフホストのランナーのセッションが最初の clone に失敗する問題を修正
- 「You've used」や「You've hit your」のような言葉で始まる返答が、赤い使用量の上限のエラーとして示される問題を修正
- Bedrock・Google Cloud の Agent Platform・Foundry などのサードパーティのプロバイダーで、クラッシュか kill の後に再開した会話の最後のメッセージが欠けることがある問題を修正
- 編集がセルの種類を変えると NotebookEdit が無効なノートブックを保存する問題を修正。添付のあるセルをコードにするのは拒まれます
- 単独の Claude Design から移したデザインシステムの長い README が、Claude がデッキかデザインを始めるときに読み込むファイルの一覧を失う問題を修正
- サーバーのタスクの ID が 128 文字を超えると、MCP のツールの呼び出しが「malformed task handle」で失敗する問題を修正。1,024 文字までの ID が使えます
- セルフホストのランナー: `--configure-git` が、止まった `git --version` を PATH にない git と報告することがある問題を修正
- 複数のタスクを一度に消すか更新したとき、タスクの ID が使い回され、消したタスクが戻り、TaskGet が完了したタスクを妨げとして挙げる問題を修正
- プロンプトのタイムスタンプが同じとき、フルスクリーンの Ctrl+R の履歴の選択に古い行と重複した行が出る問題を修正
- 入力に 4,096 を超える項目の一覧があるツールの呼び出しを Code Mode が黙って飛ばし、ツールの入力のとても大きな型付き配列で固まる問題を修正。後者は拒まれます
- コマンドの間に打ったメッセージが、Claude が返事をする前に Esc を押すと、Code Mode で答えられないまま残る問題を修正。メッセージは新しいターンを始め、2 回目の Esc がそれを止めます
- 遅いコマンドがバックグラウンドへ移ってスクリプトの出力が空になったことや、`claude -p` と Agent SDK のバックグラウンドのコマンドの時間の上限を、Code Mode が Claude に伝えない問題を修正
- Code Mode が、すでに止められたコマンドを数分待つことがある問題を修正
- バックグラウンドのスクリプトの出力が届いた後、打ったスラッシュのコマンドのインラインのシェルのコマンドが Code Mode で走らない問題を修正
- スクリプトの実行中に止めた後、Agent SDK と `claude -p` の Code Mode のセッションが再開で Claude の最後の返答を失うことがある問題を修正
- Remote Control: Desktop アプリか VS Code が動かすセッションが、/compact の間アイドルと示される問題を修正
- Claude Desktop で、バックグラウンドのタスクの報告の後、セッションが「needs input」の状態を失うことがある問題を修正
- Grep の問題を修正: 最後の改行のないファイルの終わりの空の一致を -o が落とす、multiline の -o が UTF-8 でないファイルで空の行を加えるか行番号を誤る、-C が 0 のとき -A と -B が無視される
- `meta` と綴って `alt` として割り当てた（またはその逆の）コードを `keybindings.json` で外しても、最初のキーが 2 つ目を待ち続ける問題を修正
- 空のセッションをバックグラウンドへ移すと「Couldn't load transcript from file」で失敗することがある問題を修正
- アカウントでオンでない組み込みのサーバーについて、起動のたびに OpenTelemetry が失敗した `mcp_server_connection` のイベントを報告する問題を修正
- 大きいか遅い git のリポジトリで、ファイルの diff を待つ間の Bash のコマンドを Esc が止めず、次のメッセージが待たされる問題を修正
- 画像ファイルの名前で終わる貼り付けたリンクと相対パスが遅れて出て、直後に押した Enter を飲み込む問題を修正
- `/mcp reconnect all` と `/mcp disable all` が、アカウントでオンでない組み込みのサーバーを数える問題を修正
- mod の `turn.step` のフックが待っている間にターンを中断すると、「Interrupted」ではなく「user-cancel」がエラーとして出る問題を修正
- 別のセッションが `~/.claude.json` を保存している途中のとき、それが壊れていると報告される問題を修正
- Claude の許可かブロックするドメインの一覧が空か重複を含むとき、Web の検索が API のエラーで失敗する問題を修正
- ほかのバックグラウンドの作業が動いている間、Code Mode で一時停止したワークフローの再開が数分待つ問題を修正
- スクリプトが 10 分を超えて動くと、Code Mode のサブエージェントが「Agent stalled」で失敗してコマンドを失う問題を修正
- [VSCode] Claude のプロセスが起動時に止まっている間、Rewind が「Checking code changes…」のままになる問題を修正
- [VSCode] 開いた直後にモデルの選択の矢印キーが違う行から始まり、`/model` かコマンドのメニューで開くとスクリーンリーダーがハイライトしたモデルを読み上げない問題を修正
- [VSCode] diff のビューの「Copy deleted line」と「Copy changed line」が名前と違う行をコピーし、下の近くのダブルクリックが頼まないのにコピーする問題を修正
- [VSCode] ブロックされたマイクのツールチップが切れる、長いアドレスが Web Fetch の行からはみ出す、High Contrast で使用量のバーが満杯に見える、Thinking の行がクリックで飛ぶ、の問題を修正
- [VSCode] 同じウィンドウの 2 回目の Logout が、1 回目がまだ動いているのに成功を報告する問題を修正し、ログアウトの失敗のエラーに Show logs のボタンを追加
- [VSCode] Claude がアイドルの間にバックグラウンドのコマンド・エージェント・ワークフロー・モニターが終わったとき、チャットに通知が出ない問題を修正
- [VSCode] Windows 11 24H2 以降の VS Code 1.101 と 1.102 で、NTFS のドライブで会話のフォーク・メモリーを開いて保存する・プロジェクトの出力スタイルの作成が失敗する問題を修正
- [VSCode] サイトがエラーか、たどらなかったリダイレクトを返したとき、Web Fetch が成功の点付きで「Fetched from」と示す問題を修正
- [VSCode] コンパクションした会話を読み込み直す・再開する・フォークすると、コンパクションの要約が自分のプロンプトとして、Rewind とプロンプトの履歴にも出る問題を修正
- [VSCode] Claude Code のユーザーと managed の設定の `spinnerVerbs` が無視される問題を修正
- [VSCode] mod の右から左のテキストの句読点が逆の側に出る、パネルの書体に罫線の文字がないと mod の帯か枠が幅の一部しか埋めない、の問題を修正
- [VSCode] 最後の Claude のタブを閉じた後、空の鍵のかかったエディターの枠が次のファイルか Claude のタブの隣に残る問題を修正
- [VSCode] 保存できないセッションの名前の変更が黙って戻る、スクリーンリーダーがセッションの状態・開いているセッション・畳んだグループを聞き取れない、の問題を修正
- [VSCode] 隠れたパネルの通知が待っているセッションを名指さない、ヘブライ語とアラビア語の質問が順を乱して読まれる、Claude のプロセスが終わって切れた質問が赤い点だけを示す、の問題を修正
- [VSCode] エラーのメッセージなしに失敗したサインインが何も示さずにサインインの画面に戻る、そのタブで再びサインインした後も認証のエラーが今のことのように見える、の問題を修正
- [VSCode] 一部のバナーの上にメニューが開くとチャットが動く、長いセッションでエージェントのツールの呼び出しの数が減る、の問題を修正。挙げている呼び出しの数を示すようになりました
- [VSCode] 拡張子のないファイル・フォルダー・行と列の付いたリンクのほとんどが何もしない問題を修正
- [VSCode] 会話を開き直した後、キューのメッセージと添付したファイルが逆の順に出る問題を修正
- [VSCode] 保存した結果にテキストのない、エラーで終わった質問が「Something went wrong」と示す問題を修正
- [VSCode] 伏せた思考が「Unsupported content type」と示される問題を修正
- [VSCode] 入力方式（IME）が組み立てている語に、メッセージの欄が下線を引かない問題を修正
- [VSCode] 上のキーを押し続けると送っていないメッセージが以前のプロンプトで置き換わり、呼び出したプロンプトに改行が入るか消した後に下のキーでメッセージが戻らない問題を修正
- [VSCode] Tab で補った `/model` がモデルを切り替えることがあり、何も動いていないとモデルの選択がすぐ閉じる問題を修正

**その他**

- **Slack への言及が外れた**（`overview`・`platforms`・`claude-tag`・`feature-availability`・`channels`・`llm-gateway-connect`・`how-claude-code-works`・`mobile`・`quickstart`。詳細はハイライト 5 参照）
- **Claude.ai の設定の場所の書き方**: `claude-code-on-the-web`・`settings`・`remote-control` の `/config` と、`pr-steward`・`pr-steward-pull-requests` の PR Steward の設定の場所が、「**Settings > Code** か **Settings > Claude Code**」から「**Settings > Code**」だけになりました（`claude-projects`・`desktop`・`output-styles` などには両方の書き方が残っています）。`admin-setup`・`managed-settings`・`server-managed-settings` の **Organization settings > Desktop 3P**、`plugins/host-marketplace` の **Organization settings > Plugins & skills**、`plugins/publish` の **Organization settings > Roles**、`artifacts` の **Organization settings > Artifacts**、`admin-setup` の Spend controls の行の Organization settings には、claude.ai の設定のページへのリンクが付きました
- **Desktop アプリのダウンロードのリンク**: `desktop`・`desktop-quickstart`・`setup`・`troubleshoot-install` のダウンロードのリンクが、`claude.ai/api/desktop/.../redirect` の形から `claude.ai/claude-code/desktop-download?platform=…` の形になりました（`overview` には古い形が残っています）
- **組織やチームを前提にしない言い方**: `availableModels` の許可リストを「組織の」と書いていた箇所が「何らかの」「設定にある」に（`agent-teams`・`sub-agents`・`workflows`・`advisor`・`permission-modes`）、「チームと共有する」が「共有する」に（`claude-directory`・`memory`・`plugins/overview`・`plugins/create`・`settings`・`routines`）、「管理者が」「組織の」がより一般的な言い方に（`model-config`・`authentication`・`vs-code`・`code-review`・`code-review-setup`・`code-review-local`・`admin-setup`・`network-config`・`plugins/mods/troubleshoot`・`plugins/mods/events`・`plugins/host-marketplace`・`desktop`・`artifacts`・`hooks`）なりました。機能の変化は伴いません
- **言い回しの削り込み**: `best-practices`（モデルが指示に従わないこともある、の後半）・`features-overview`（CLAUDE.md はどのスタイルでも読み込まれたまま）・`how-claude-code-works`・`large-codebases`・`champion-kit`・`claude-projects`・`web-quickstart`・`fast-mode`・`desktop-ios-simulator`・`checkpointing`（VS Code の拡張機能が diff の基準に使う、の部分）・`cloud-environments`（Owner でなければ Owner に頼む）などで、念押しや補足の文が外れました。`costs`・`settings-example`・`hooks` の「Bash のコマンドの前に」は「Bash のツールの呼び出しの前に」に、`permission-modes`・`cli-reference`・`permissions` の一部の「走る」「許される」は「走りうる」「許されうる」になっています
- **そのほかの書き直し**: `approvals-pull-requests` では、チェックの題の表の「Nothing yet」が「Wait for the result」に、題が表にないときの言い方が「For any other title」に、中立にならない場合の表の導入が「待つ・失敗する・差し止められる・出ない場合」になり、フォークのプルリクエストの節から、書き込みの権限のある人がフォークのコミットをプッシュしたかを Approvals は確かめられない、という文が外れました。`claude-apps-gateway-config` の `mantle` の上流では、Mantle の IAM のアクションを与える先が、`assume_role` を設定していればそのロール、なければ上流の AWS の ID、と書き直されました。`plugins/mods/overview` の mod でできることの例からは、Claude が質問するダイアログが外れ（`AskUserQuestion` は `ui.render` で置き換えられないため）、`agent-sdk/configuration` のストリーミングの入力では、ターンの数え直しが「キューに入ったメッセージごとに」から単に「数え直す」に、`agent-sdk/observability` の `OTEL_LOG_RAW_API_BODIES` の行は、本文が会話の履歴の全体を「含む」から「含みうる」になりました。`plugins/loading` の「メンテナーに尋ねる」は「プロジェクトのメンテナーに尋ねる」になっています
- **例の値**: `claude-platform-on-aws` のワークスペースの API キーの例が `sk-ant-xxxxx` から `your-workspace-api-key` になりました
- **書式の変化**: `code-review-customize` の 6 つの見出し・`code-review-troubleshooting`・changelog の 3 か所の `REVIEW\.md` と、`cloud-environments` の `raw\.githubusercontent.com`（2 回載るページの 2 か所）から、ピリオドの前のバックスラッシュが外れました。base の 13 か所の `REVIEW\.md` は head ではなくなっています。内容の変更ではありません
<!-- light:minor-updates:end -->

見出しマップ（`en/claude_code_docs_map.md`）は、更新時刻が 2026年11月23日 20:47:12 UTC から 2026年11月25日 05:00:49 UTC に替わり、70 行が加わり 34 行が外れました（6,957 行から 6,993 行）。外れたのは `slack` の 29 の見出し（「(No headings found)」の 1 行に替わった）と、改称前の見出し（`routines` の「"The last run" warnings」、`scheduled-tasks` の「Seven-day expiry」、`llm-gateway-connect` の「Slack, cloud sessions, and Remote Control」、`tools-reference` の「When a fetch prompts, fails, or WebFetch is missing」）です。加わったのは、上で述べた新しい h2・h3・h4 と改称後の見出しです。見出しマップの項目は、どのページでも head の `llms-full.txt` の見出しと合っていて（違いは、マップに残るアンダースコアとピリオドのエスケープの有無だけ）、今回、見出しマップにだけ先に載った見出しはありません。

**参考リンクについて**: 日本語版は、今回リンクを付けたページの HTML を取得し、見出しの id があるかと、今回の差分で出入りしたコードの字句・メッセージ・リンク先のアンカー（`Skill(mcp__docs__*)`・`/claude-security triage results.sarif`・`dev.azure.com`・`CLAUDE_CODE_DISABLE_SHIP`・`v5.11492.0`・`it isn't offered yet through a gateway or proxy`・`Command was moved to the background (ID: <id>) after running for 180s`・`--disallow-tools`・`CronCreate`・`claude-approvals[bot]` など、base と head の `llms-full.txt` で数が違うもの）が英語版と同じだけあるかで、今回の内容になっているかを確かめました。今回の内容になっていなかったのは、`hooks` の `PreSkillShellCommand` の節（日本語版に id がない）、`plugins/mods/interface` の 3 つの新しい h3（同じく id がない）、`plugins/mods/reference` の `Shader` と `ui.pointer` の行、`skills` と `errors` の `PreSkillShellCommand` に触れる箇所、`network-config` のアーティファクトのホストの行で、これらは英語版だけにリンクするか、リンクを付けていません。`amazon-bedrock` の冒頭の注記は見出しの下にないので、アンカーなしのページへのリンクにしています（日本語版にも同じ注記とリンク先があることを確かめています）。アンカーは英語版・日本語版の HTML の見出しの id と目次で確かめました。見出しの文字列の GFM スラッグと違う id を持つものがあり、`mcp` の「Find and call MCP skills by name」は `#run-an-mcp-skill`、「Security scanning for MCP skills」は `#safety-of-mcp-skills`、「MCP skill availability」は `#requirements-for-skills-from-mcp-servers`、「MCP tasks in cloud sessions and claude.ai chats」は `#mcp-tasks-in-the-cloud`、`tools-reference` の「Find out why WebFetch is unavailable」は旧見出しの id `#webfetch-availability`、`plugin-evals` の「Remove a built-in tool from runs」は `#disallow-tools`、`routines` の「Warnings under History」は `#the-last-run-didnt-start` です。`scheduled-tasks` の「Recurring task expiry」は、新しい id `#recurring-task-expiry` と旧い id `#seven-day-expiry` の両方を持ちます。**changelog ページへのリンクは、本サマリの方針どおり付けていません。** v2.1.332 の項目のうち、changelog のほかのページにまだ載っていないもの（`computer-use` の予約名、`claude-code-desktop` の `service.name`、`oat02-` の接頭辞など）には、リンクを付けていません。

## 新着情報

<!-- light:whats-new:start -->
（今回の差分に新着情報（`whats-new/`）のページはありません。head の `llms.txt`・`llms-full.txt`・見出しマップにも whats-new のページは載っていません）
<!-- light:whats-new:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-11-23.md](./archives/latest/2026-11-23.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-11-23.md](./archives/latest-detail/2026-11-23.md)

<!--
base_commit: 6b8844c93bee3ab36c9d7bb656a2476fb661c469
head_commit: 1c6dc5c3f6d9261729fd5a8dbb3dd2389c542149
generated_at_full: 2026-11-25T15:09:31+09:00
-->
