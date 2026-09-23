---
対象期間: 2026年09月16日 〜 2026年09月23日
作成日: 2026-09-23
---

# Claude Code 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
**今回は 7 日ぶんをまとめた断面です。** 前回サマリは 2026年09月17日 の取り込みで作られており、そこから今回の取り込み（2026年09月24日）までに**取り込みコミットが 6 本**積まれました（2026年09月21日 ぶんだけ欠けています）。差分は 3 ファイル・5,436 行（追加 4,062・削除 1,374）で、`llms-full.txt` は 97,637 行から 100,218 行へ **2,581 行増え**、**本文が変わったページは 116 / 197** です。changelog には **v2.1.274・275・276・277・278・280 の 6 リリース・407 項目**が積まれました（**v2.1.279 は欠番**）。日数ぶん量が多いだけでなく、**新モデル Opus 5.5 の投入・Projects という新しい入れ物・`AGENTS.md` の直読み・claude.ai アカウント同期のターミナル展開**という、性質の異なる 4 つの大きな変更が同じ期間に重なっています。

主要なものを以下に挙げます。

1. Opus 5.5 が既定の Opus になり、既定の努力レベルが medium になった
2. Projects が公開ベータで登場し、Claude が並列クラウドセッションを束ねるようになった
3. AGENTS.md をそのまま読むようになった
4. claude.ai アカウントのスキルとプラグインがターミナルにも同期されるようになった
5. 6 リリース・407 項目が一挙に積まれた（v2.1.279 は欠番）
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**Opus 5.5 が既定の Opus になり、既定の努力レベルが medium になった**](#1-opus-55-が既定の-opus-になり既定の努力レベルが-medium-になった):  
  **`claude-opus-5-5` が v2.1.280 で入り、`opus` エイリアスと `default` の解決先が Opus 5.5 になりました。** 影響が大きいのは **Pro と Team Standard** で、`default` の解決先が **Sonnet 5 から Opus 5.5 へ変わりました**。**既定の努力レベルは Opus 5.5 だけ `medium`**（他は `high`、Opus 4.7 は `xhigh`）で、**ユーザー設定のトップレベル `effortLevel` は Opus 5.5 には効きません**。あわせて **Fable 5・Opus 4.8・Opus 4.7 にあった「モデル既定努力の hold」という仕組みが丸ごと削除**され、努力レベルの解決順序が 4 段から 3 段に減りました。Opus 5.5 は **Fable と同じく思考をオフにできず**、Anthropic API では **Pro を含む全プランで 1M コンテキストが既定**です。**17 ページに 55 か所**波及しています。
2. [**Projects が公開ベータで登場し、Claude が並列クラウドセッションを束ねるようになった**](#2-projects-が公開ベータで登場しclaude-が並列クラウドセッションを束ねるようになった):  
  **`claude-projects` が 459 行の新規ページとして加わりました。** プロジェクトは**「コーディネーターとしての Claude との 1 本の長い会話」＋「Claude が起こすスレッド」**という構造で、**各スレッドは独立したクラウドセッション**です。作業を 1 か所に投げ込めば Claude が振り分け、**Overview ペイン**がレビュー待ち・返答待ち・実行中を束ねて見せます。**Pro と Max の公開ベータ**で段階ロールアウト中、Team / Enterprise は未対応です。**強制上限はプロジェクト横断で 1 日 200 スレッド**、**スレッドは auto モードで動き**、**`/web-setup` のトークンでは足らず Claude GitHub App が必須**です。**changelog には Projects の項目が 1 つもありません** ―― CLI 側の機能ではなく claude.ai 側の機能だからです。
3. [**AGENTS.md をそのまま読むようになった**](#3-agentsmd-をそのまま読むようになった):  
  **v2.1.277 以降、リポジトリに `CLAUDE.md` が無ければ Claude Code は `AGENTS.md` をプロジェクト指示として直接読みます。** インポートもシンボリックリンクも設定も不要になり、`memory` に **h2 `AGENTS.md` と 8 つの h3 が新設**されました（200 行・追加 164／削除 36）。既定は `claude-md-or-agents-md` で、`/config` の **Project instructions** で 4 値から選べます。**判定に数えるのは作業ディレクトリ以上の `CLAUDE.md` / `.claude/CLAUDE.md` / `CLAUDE.local.md` だけ**で、`~/.claude/CLAUDE.md`・管理 `CLAUDE.md`・`.claude/rules/` は数えません。設定ファイルから指定する場合は**組み込みプラグインの ID 経由**（`pluginConfigs["agents-md@builtin"]`）で、**プロジェクト設定とローカル設定では無視**されます。`AGENTS.md` の言及は **8 か所から 92 か所へ、13 ページ**に広がりました。
4. [**claude.ai アカウントのスキルとプラグインがターミナルにも同期されるようになった**](#4-claudeai-アカウントのスキルとプラグインがターミナルにも同期されるようになった):  
  これまで claude.ai アカウントのスキルは **Cowork とクラウドセッション限定**で、ターミナルでは `-p` 実行に `CLAUDE_CODE_SYNC_SKILLS=1` を付けたときだけダウンロードされていました。**今回、claude.ai アカウントでサインインしたターミナルセッションが起動時に背景ダウンロードし、実行中も約 10 分ごとに再チェックする**ようになり、**プラグインも同じ仕組みに乗りました**（`~/.claude/plugins/synced/`・`<name>@synced`）。停止用に **`syncClaudeAiPlugins`** が新設され、**組織が必須指定したプラグインは無効化できません**。あわせて **claude.ai がホストするマーケットプレイス**を `--claudeai` で追加できるようになりました。一方で**リポジトリの `enabledPlugins` はクラウドセッションで読まれなくなり**、クラウドでプラグインを使う経路はアカウント同期に一本化されています。
5. [**6 リリース・407 項目が一挙に積まれた（v2.1.279 は欠番）**](#5-6-リリース407-項目が一挙に積まれたv21279-は欠番):  
  **収録リリースは 396 から 402 になり、積まれたのは v2.1.274・275・276・277・278・280 の 6 本です** ―― **v2.1.279 は欠番**です。**407 項目の内訳は修正 258・改善 57・追加 49・変更 36・削除 5・差し戻し 1・更新 1**。**v2.1.276 は 1 項目だけ**で、**v2.1.275 が自ら入れた `advisor` ツールの回帰を翌日塞ぐ修正**です。**v2.1.278 も 2 項目だけ**ですが、**auto モードのサーバー側分類器が再び既定に戻る**という重い変更を含みます。セクションタグ付きは **`[VSCode]` 67・`[Claude Tag]` 32・`[Claude Code on the web]` 24・`[Code Review]` 7・Self-hosted runner 3・Windows 1** の計 134 件で、残る **273 件が CLI 本体**です。
<!-- light:highlight-list:end -->

## 1. Opus 5.5 が既定の Opus になり、既定の努力レベルが medium になった

**`model-config`（90 行・追加 44／削除 46）を中心に、`Opus 5.5` が 17 ページ・55 か所へ入りました。** changelog の追加項目は 1 行だけです ―― 「Claude Opus 5.5（`claude-opus-5-5`）を追加。既定の Opus モデルになり、1M コンテキスト、MTok あたり $4/$20、キャッシュ読み取りは MTok あたり $0.20」。

### エイリアスと既定の解決先

| 項目 | base | head |
|---|---|---|
| `opus`（Anthropic API・Claude Platform on AWS・Bedrock・Agent Platform） | Opus 5 | **Opus 5.5** |
| `opus`（Microsoft Foundry） | Opus 4.6 | Opus 4.6（変更なし） |
| `default`（Pro・Team Standard） | **Sonnet 5** | **Opus 5.5** |
| `default`（Max・Team Premium・Enterprise・Anthropic API） | Opus 5 | **Opus 5.5** |
| `default`（Microsoft Foundry） | Sonnet 4.5 | Sonnet 4.5（変更なし） |
| fast mode の既定 | Opus 5 | **Opus 5.5** |

**アカウント種別の区別が消えたのが目を引きます。** base では「Max・Team Premium・Enterprise・Anthropic API は Opus 5、**Pro と Team Standard は Sonnet 5**」と 3 行に分かれていた記述が、head では「**Pro・Max・Team・Enterprise・Anthropic API は Opus 5.5**」の 1 行になりました。

### 努力レベルの既定が medium になり、hold 機構が消えた

**Opus 5.5 は、努力レベルをサポートするモデルの中で唯一「既定が `medium`」**です（他は `high`、Opus 4.7 だけ `xhigh`）。原文は理由まで書いていませんが、挙動の書き分けは細かいです。

- **ユーザー設定のトップレベル `effortLevel` は Opus 5.5 に効きません。** このキーは「`/effort` がモデル別保存を始める前に書いていた古い形式」であり、**Opus 5・Fable 5.1 とそれ以前のモデルには従来どおり効き続ける**一方、**Opus 5.5 以降のモデルは自分の既定から始まる**と明記されました。
- **プロジェクト設定・ローカル設定・管理設定・`--settings` のトップレベル `effortLevel` は全モデルに効きます。** 効かないのはユーザー設定のものだけです。
- **`Fable 5`・`Opus 4.8`・`Opus 4.7` の「モデル既定努力の hold」が丸ごと削除されました。** 努力レベルの解決順序は **4 段から 3 段**（明示指定 → 設定 → モデル既定）に縮み、「どの操作が hold を解くか」という箇条書きも、`-p` 実行で `Not applied` になるという但し書きも、フロントマター努力と hold の関係の段落も消えています。v2.1.280 の変更項目に対応します。

### 思考・コンテキスト・フォールバック

| 観点 | Opus 5.5 の扱い |
|---|---|
| 思考のオフ | **できない。** `Option+T` / `alwaysThinkingEnabled` / `MAX_THINKING_TOKENS=0` / `CLAUDE_CODE_DISABLE_THINKING` のいずれも効かない（Fable モデルと同じ扱いに並べられた） |
| 1M コンテキスト | **Anthropic API では Pro を含む全プランで既定**。`[1m]` バリアントの選択も usage credits も不要。`[1m]` 経由が要るのは **Opus 4.6 と Sonnet 4.6 だけ**になった |
| 安全分類器のフォールバック | biology は **Opus 5 へ**、cybersecurity は **Opus 4.8 へ**再実行（Fable 5.1 / Fable 5 と同じ組）。Opus 5 自身は biology に控えが無く拒否で終わる |
| プロンプトキャッシュ | **努力レベルを変えてもキャッシュが残る**（API キーまたは Claude サブスクリプション利用時。Fable 5.1 と同じ扱い） |
| advisor | Opus 5.5 / Opus 5 が主モデルのとき、受理されるのは **Fable と Opus 5 以降**のみ |
| fast mode | 対応。**価格は MTok あたり $8/$40**（Opus 5 / Opus 4.8 は $10/$50） |

**`opusplan` の説明も書き換わりました。** 「プランフェーズは `opus` 設定と同じコンテキストウィンドウを使う」に**「実行フェーズは `sonnet` と同じウィンドウを使う」**が加わり、「自動 1M アップグレード対象のサブスク階層では」という条件が「**`opus` と `sonnet` が既定で 1M で動くモデルに解決されるなら（現行モデルは Anthropic API 上でそうなる）両フェーズとも 1M で動く**」に一般化されています。

- [Model configuration - Claude Code Docs (English)](https://code.claude.com/docs/en/model-config#model-aliases)
- [日本語](https://code.claude.com/docs/ja/fast-mode#understand-the-cost-tradeoff) / [Speed up responses with fast mode - Claude Code Docs (English)](https://code.claude.com/docs/en/fast-mode#understand-the-cost-tradeoff)

## 2. Projects が公開ベータで登場し、Claude が並列クラウドセッションを束ねるようになった

**`claude-projects` は今回の差分で唯一の新規ページで、459 行あります。** `llms.txt` の収録 URL は 207 件から 208 件になり、**索引と本文が同じ取り込みで揃いました**（前回までは索引が 1 回先行するのが常でした）。

### 構造

| 部分 | 役割 |
|---|---|
| **プロジェクト会話** | Claude がコーディネーターとして動く長時間セッション。送られたものを受け取り、何をスレッドにするか決め、起こしたスレッドを全部追跡する。**スレッドが報告した内容は見るが、各ステップは見ない** |
| **スレッド** | 実作業をする側。**それぞれ独立したクラウドセッション**で、自分のコンテキストウィンドウと自分のブランチを持ち、必要ならプルリクエストを開き、終わったら会話へ報告する |
| **Overview ペイン** | スレッドを **Ready for review / Waiting on you / Working / Landing / Idle / Resolved** の 6 状態に束ねる。他タブは **Library**（ファイル）・**Pull requests**・**Routines** |

**すべての新しいスレッドが引き継ぐもの**は、プロジェクトのリポジトリとファイル、プロジェクト指示（**最大 16,000 文字**）、プロジェクトメモリ、各リポジトリの `CLAUDE.md` とスキル、claude.ai アカウントのコネクタ、クラウド環境です。**自分のマシンの Claude Code 設定は何も引き継ぎません。**

### 前提と上限

- **プラン**: Pro または Max。**Team / Enterprise はまだ不可**で、ベータ中は組織レベルの制御も無い
- **GitHub**: github.com のみ（GitHub Enterprise Server・GitLab・Bitbucket は不可）。**`/web-setup` で渡したトークンでは足りず、Claude GitHub App のインストールが必須**
- **スレッド数**: 「一度に 2 本まで」と会話で頼んでも**それは指示であって上限ではない**。**強制される上限はプロジェクト横断で 1 日 200 スレッド**
- **権限**: スレッドは **auto モード**で動く。承認プロンプトはスレッドの中に出るので、**プロジェクト会話で「進めていい」と言っても届かない**
- **モデル**: 新規プロジェクトは**スレッドを Opus・高 effort、会話を Opus・低 effort**で動かす。原文は「プランを最も速く消費する設定」と書いている

### 1 リポジトリと複数リポジトリで挙動が変わる

**スレッドは全リポジトリをクローンして全部の `CLAUDE.md` とスキルを読みますが、権限ルール・フック・`env` は「スレッドが起動したディレクトリの `.claude/settings.json`」からしか取りません。**

| | 1 リポジトリ | 複数リポジトリ |
|---|---|---|
| `CLAUDE.md` | 起動時に読む | 全リポジトリから読む |
| `.claude/` のスキル・エージェント・コマンド | 読む | 全リポジトリから読む |
| `.claude/settings.json` のプラグイン | **読まない**（Project settings > Plugins で追加する） | **読まない** |
| `.claude/settings.json` の権限ルール・フック・`env` | **効く** | **効かない**（クローンの上で起動するため） |

複数リポジトリのときは各クローンが**`CLAUDE.md` 読み込みを有効にした追加ディレクトリ**として接続される、という実装の説明まで書かれています。

### プロジェクトメモリはローカルの auto memory とは別物

**Project settings > Memory は「Auto memory」という見出しでメモリファイルを並べますが、これはマシン上の [auto memory](https://code.claude.com/docs/en/memory) とは別**です（どちらも `MEMORY.md` を索引に使う点だけが共通）。**リポジトリの `CLAUDE.md` とも別**で、原文は「リポジトリについての指示はその `CLAUDE.md` に、プロジェクトについてのメモはプロジェクトメモリに」と書き分けています。

- [Let Claude coordinate ongoing work with Projects - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/claude-projects#how-a-project-is-organized)
- [Let Claude coordinate ongoing work with Projects - Claude Code Docs (English)](https://code.claude.com/docs/en/claude-projects#how-a-project-is-organized)

## 3. AGENTS.md をそのまま読むようになった

**`memory` は今回 200 行（追加 164・削除 36）動き、h2 `AGENTS.md` と 8 つの h3 が新設されました。** これまで同ページには「Claude Code は `CLAUDE.md` を読み、`AGENTS.md` は読まない。`@AGENTS.md` でインポートするかシンボリックリンクを張れ」という h3 が 1 つあっただけです。その h3 は**同名の h2 へ格上げされ**、中身は全面的に書き直されました。

### 既定の読み分け

| リポジトリの状態 | Claude が読むもの |
|---|---|
| `AGENTS.md` があり、作業ディレクトリ以上に `CLAUDE.md` / `CLAUDE.local.md` が無い | **`AGENTS.md`** |
| `AGENTS.md` と `CLAUDE.md`（または `CLAUDE.local.md`）の両方がある | `CLAUDE.md` のみ |
| `CLAUDE.md` が既に `AGENTS.md` をインポートしている | `CLAUDE.md`（インポート経由で `AGENTS.md` を含む） |

**判定に数えるファイルの線引きが明示されました** ―― 数えるのは作業ディレクトリとその上位の `CLAUDE.md` / `.claude/CLAUDE.md` / `CLAUDE.local.md` だけで、**`~/.claude/CLAUDE.md`・組織の管理 `CLAUDE.md`・`.claude/rules/` は数えず、`AGENTS.md` と一緒に読み込まれ続けます**。原文は Note で「**`CLAUDE.local.md` も数えるので、`AGENTS.md` 頼みのプロジェクトに個人用の `CLAUDE.local.md` を置くと `AGENTS.md` が読まれなくなる**」という落とし穴まで挙げています。

### `/config` の Project instructions

| 値 | 読むもの |
|---|---|
| `claude-md-or-agents-md` | 既定。`CLAUDE.md`、無ければ `AGENTS.md` |
| `claude-md-and-agents-md` | 両方。**各ディレクトリで `CLAUDE.md` が先、`AGENTS.md` が後**。すでに読んだ `AGENTS.md` は二重に読まない |
| `claude-md` | `CLAUDE.md` のみ |
| `managed-only` | 組織の管理 `CLAUDE.md` と auto memory のみ（サブディレクトリの `CLAUDE.md` とパススコープルールは引き続き読む） |

**設定ファイルから指定する場合は、組み込みプラグインの ID 配下に書きます** ―― `pluginConfigs` の `agents-md@builtin` の `options.instructionFiles`。置けるのは `~/.claude/settings.json`・`--settings`・管理設定で、**プロジェクト設定とローカル設定では無視されます**。`settings-reference` の `pluginConfigs` 項目にも「**組み込みプラグインは `@builtin` 接尾辞で同じキーに入る**」という説明が加わりました。

### 読まないもの・効かないもの

- **読まないファイル**: `AGENTS.local.md`、`AGENTS.override.md`、`.agents/` 配下のすべて
- **`InstructionsLoaded` フックは発火しません**（設定経由で直読みした `AGENTS.md` の場合）。`CLAUDE.md` がインポート／シンボリックリンクしている場合は従来どおり発火します
- **`--add-dir` の追加ディレクトリからは `AGENTS.md` を読みません**（`CLAUDE.md` は `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD` で読める）
- **作業ディレクトリ外への `@path` インポート**は、すでに外部インポートを承認済みのプロジェクトでのみ**プロンプト無しで**読み込まれます
- **利用できない条件**: v2.1.277 より前／feature flag を取得しないセッション（Bedrock 等・テレメトリ無効）／インストール直後の初回セッション／`agents-md` 組み込みプラグインを `/plugin` で無効化した場合
- **v2.1.280 より前は `/memory` と `/context` が直読みの `AGENTS.md` を一覧しません**。その版では「Claude にプロジェクト指示の内容を尋ねる」よう案内されています

### 周辺への波及

`glossary` に **`AGENTS.md` 項目**と、**`F` セクションごと新設された `Frontmatter` 項目**が加わりました。`claude-directory` は `AGENTS.md` の行を追加し、**h2「ファイル別フロントマターフィールド」**を新設して、スキル・コマンド・サブエージェント・出力スタイル・ルールのフロントマターフィールドを 1 表にまとめています。`memory` 側にも **h4「ルール frontmatter リファレンス」**（`paths` のみ）が新設され、`skills`・`sub-agents`・`output-styles` の該当節も「Frontmatter リファレンス」に揃えられました ―― **フロントマター記述の集約が今回の横断テーマの 1 つ**です。

- [How Claude remembers your project - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/memory#agents-md)
- [How Claude remembers your project - Claude Code Docs (English)](https://code.claude.com/docs/en/memory#agents-md)
- [Glossary - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/glossary#agents-md) / [Glossary - Claude Code Docs (English)](https://code.claude.com/docs/en/glossary#agents-md)

## 4. claude.ai アカウントのスキルとプラグインがターミナルにも同期されるようになった

**`skills`（63 行）と `plugins-reference`（180 行）の両方で、claude.ai アカウント同期の説明が書き換わりました。** 本文は**ターミナルセッションでの同期を v2.1.273 以降**と記載し、changelog はこれを **v2.1.275 の追加項目**として告知しています。

### 何が変わったか

| | base | head |
|---|---|---|
| スキルの同期先 | Cowork・クラウドセッションのみ。ターミナルは **`-p` 実行＋`CLAUDE_CODE_SYNC_SKILLS=1` のときだけ**ダウンロード | **claude.ai アカウントでサインインしたターミナルセッションすべて**。起動時に背景ダウンロードし、**実行中も約 10 分ごとに再チェック**して追加・更新・削除を**再起動なしで**反映 |
| プラグインの同期先 | Cowork・クラウドセッションのみ。「**自分のターミナルで開いたセッションでは読み込まない**」と明記 | 上記に加え**ターミナルセッションでも**。起動ごとに 1 回アカウントを確認し、背景でダウンロード／削除 |
| 停止手段 | `syncClaudeAiSkills` | `syncClaudeAiSkills` ＋ **`syncClaudeAiPlugins`**（どちらも `false` だけが有効。`true` は未設定と同じ） |
| `CLAUDE_CODE_SYNC_SKILLS` の位置づけ | 同期そのものを有効にする変数 | **`-p` 実行で「最初のクエリ前に一覧を待たせたい」ときだけ設定する変数**へ後退 |

**同期されたプラグインはマーケットプレイス経由のものと同じ信頼で動きます** ―― スキル・エージェント・フック・MCP サーバー・LSP サーバーがすべて読み込まれます。**対話セッション中に追加・更新・削除が起きると `Plugins changed. Run /reload-plugins to activate.` が出ます。**

### 同期しない条件

- `/login` の保存済みサインインを使わないセッション（API キー認証、`ANTHROPIC_AUTH_TOKEN` / `CLAUDE_CODE_OAUTH_TOKEN` / `apiKeyHelper` 由来の認証情報）
- feature flag を取得しないセッション（Bedrock、`CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`）
- bare mode（`--bare`）、`--safe-mode`
- 管理設定が**スキルをプラグインソースにロック**している場合（`strictPluginOnlyCustomization`）、`--setting-sources` から `user` を外した場合

**セッション中に `/login` した場合は再起動が要ります。** 古い版のサインインは「背景で更新されるとき（数時間以内）、または `/login` をやり直したとき」にプラグインアクセスを得ます。

### 組織が必須にしたプラグインは無効化できない

`errors` に **`Plugin "<name>@synced" is required by your organization and can't be disabled here.`** という節が新設されました。`claude plugin disable` も `/plugin` の **Installed** タブも何も保存せず、**必須プラグインが依存しているプラグインを無効化しようとしても同じ理由で拒否**されます。`claude plugin list` では `required by your org` と印が付きます。

### claude.ai ホストのマーケットプレイス

`discover-plugins` に **「claude.ai から追加する」**節が新設されました。`claude plugin marketplace list` の出力末尾に **`From claude.ai:` セクション**が付き、そこに並ぶ名前を `--claudeai` で追加できます（**v2.1.273 以降**）。ローカル名は **`claudeai-` 接頭辞**付きで登録され（`Organization library` → `claudeai-organization-library`）、**`--scope` と `--sparse` は拒否**されます。`--json` 出力は追加済みマーケットプレイスだけを扱い、このセクションを含みません。あわせて **`/plugin install <plugin> --marketplace <source>`**（マーケットプレイス追加とインストールを 1 コマンドで・**v2.1.275 以降**）も加わりました。

### クラウドセッションのプラグイン経路が一本化された

**`cloud-environments` の「何が引き継がれるか」表で、リポジトリの `.claude/settings.json` の `enabledPlugins` が「Yes（セッション開始時にマーケットプレイスからインストール）」から「No」へ反転しました。** `extraKnownMarketplaces` のマーケットプレイスも同様です。**クラウドセッションでプラグインを使う経路は「claude.ai アカウントで有効にして同期させる」に一本化**され、`desktop`・`security-guidance`・`discover-plugins` の該当記述も揃えられています。

- [Extend Claude with skills - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/skills#where-synced-skills-load) / [Extend Claude with skills - Claude Code Docs (English)](https://code.claude.com/docs/en/skills#where-synced-skills-load)
- [Plugins reference - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/plugins-reference#synced-plugins) / [Plugins reference - Claude Code Docs (English)](https://code.claude.com/docs/en/plugins-reference#synced-plugins)
- [All settings - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/settings-reference#syncclaudeaiplugins) / [All settings - Claude Code Docs (English)](https://code.claude.com/docs/en/settings-reference#syncclaudeaiplugins)

## 5. 6 リリース・407 項目が一挙に積まれた（v2.1.279 は欠番）

**`changelog` ページの差分は 427 行（追加 426・削除 1）**で、収録リリース数は **396 から 402** になりました。

| リリース | 日付 | 項目数 |
|---|---|---|
| v2.1.280 | 2026年09月22日 | **114** |
| v2.1.278 | 2026年09月19日 | **2** |
| v2.1.277 | 2026年09月18日 | **87** |
| v2.1.276 | 2026年09月18日 | **1** |
| v2.1.275 | 2026年09月17日 | **95** |
| v2.1.274 | 2026年09月17日 | **108** |

**v2.1.279 は存在しません。** 欠番の理由は changelog に書かれていません。

| 種別 | 件数 |
|---|---|
| Fixed（修正） | **258** |
| Improved（改善） | **57** |
| Added（追加） | **49** |
| Changed（変更） | **36** |
| Removed（削除） | 5 |
| Reverted（差し戻し） | 1 |
| Updated（更新） | 1 |

**修正が 258 件で全体の 63%** を占めます。セクションタグ付きは **`[VSCode]` 67・`[Claude Tag]` 32・`[Claude Code on the web]` 24・`[Code Review]` 7・`Self-hosted runner:` 3・`Windows:` 1** の計 134 件で、残る **273 件が CLI 本体**です。**タグ付き項目があるのは 4 リリースだけ**（v2.1.276 と v2.1.278 は全項目が無印の CLI 本体）で、**その 4 リリースすべてで `[VSCode]` が最多タグ**です（v2.1.280 が 14・v2.1.277 が 9・v2.1.275 が 26・v2.1.274 が 18）。

### 1 項目リリースと 2 項目リリース

**v2.1.276 の唯一の項目は、前日の v2.1.275 が入れた回帰の修正**です ―― 「`ANTHROPIC_BASE_URL` がプロキシまたはゲートウェイを指しているとき、全リクエストが `400 … Input tag 'advisor_20260301'` で落ちる問題を修正（2.1.275 の回帰）」。`llm-gateway-connect` のトラブルシューティング表と `llm-gateway-protocol` の自動リトライ節の両方に対応する記述が入り、**v2.1.275 では advisor をオフにしていてもリクエストに advisor ツールのエントリが乗っていた**こと、**回避策は `CLAUDE_CODE_DISABLE_ADVISOR_TOOL=1`** であることが書かれました。

**v2.1.278 は 2 項目ですが、中身は重い**です。**auto モードの分類器レビューが、Claude API / Enterprise ユーザーおよび Bedrock・Agent Platform・Foundry・ゲートウェイでサーバー側既定に戻りました**（詳細は「軽微な更新」の該当項目参照）。もう 1 項目は `/status` に **`Auto mode server` 行**を足すものです。

### 差し戻し 1 件と削除 5 件

**差し戻されたのは、v2.1.260 で入った「フルスクリーンモードの `ctrl+l` / `cmd+k` がトランスクリプト表示を消す」変更**です。**再び画面の再描画だけを行う**ようになり、`fullscreen` と `keybindings` と `interactive-mode` の 3 ページで記述が書き換わりました。

削除は次の 5 件です。

- **`TaskOutput` ツールの削除**（v2.1.277）。**`taskOutputMaxChars` 設定と `TASK_MAX_OUTPUT_LENGTH` 環境変数も無効化**され、Claude はバックグラウンドタスクの出力ファイルを `Read` で読みます — [日本語](https://code.claude.com/docs/ja/settings-reference#taskoutputmaxchars) / [All settings](https://code.claude.com/docs/en/settings-reference#taskoutputmaxchars)
- **`claude -p` の背景タイトル生成リクエストの削除**（v2.1.277・SDK / IDE 外から起動した実行のみ）
- **一度きりのルーティンが前回セッション以降に走ったことを知らせる起動通知の削除**（v2.1.275）
- **`[Claude Code on the web]`** 組織で管理者が GitHub をオフにしている場合にセルフホスト環境のセッション開始時に出ていた空のリポジトリピッカーの削除（v2.1.280）
- **`[Claude Tag]`** ゲスト帰属の注記が Slack canvas 編集ごとに繰り返し付く問題の解消（v2.1.274）

**本サマリは方針として changelog ページの URL を掲載しません**（巨大で閲覧性が低いため）。個々の項目のうち通常ドキュメントに対応記述があるものは、以下のセクションと「軽微な更新」でそのページへリンクしています。

## 新規追加されたページ

<!-- light:new-pages:start -->
- [**Projects のページは 40 見出しで構成され、周辺 10 ページから導線が張られた**](#1-projects-のページは-40-見出しで構成され周辺-10-ページから導線が張られた) ([日本語](https://code.claude.com/docs/ja/claude-projects) / [English](https://code.claude.com/docs/en/claude-projects)):  
  **`claude-projects` は 459 行・見出し 40 件（h1 1・h2 11・h3 28）**で、今回の差分で最大の単一追加です。**機能そのものはハイライト 2 で扱っています**。ここでは**ページの構成**と、**Projects への導線を受け取った周辺 10 ページ**を扱います。`llms.txt` の説明文も 1 行追加され、**索引と本文が同じ取り込みで揃いました**
<!-- light:new-pages:end -->

## 1. Projects のページは 40 見出しで構成され、周辺 10 ページから導線が張られた

**`llms-full.txt` の展開ページ数は 196 から 197 へ 1 件増え、増えた 1 件がこのページです。** 前回までは「`llms.txt` に登録されてから本文が届くまでに 1 回の取り込みを要する」のが常でしたが、**今回は索引・見出しマップ・本文が同じ取り込みで揃いました**。

### 11 の h2

| h2 | 扱う内容 |
|---|---|
| `When to use a project` | 向く 4 パターン（多リポジトリ横断の 1 目標・供給し続ける領域・セッションを超えるビルドや移行・コード以外の作業）と、**向かない 4 パターン**（1 セッションで済むタスク・マシンだけが届くツールが要る作業・会話が要らない定期実行・Slack で複数人が操る場合） |
| `How a project is organized` | 会話・スレッド・Overview ペインの 3 部構成と、スレッドが起動時に引き継ぐもの |
| `Create a project` | ゼロから作る／既存クラウドセッションから作る（**Continue as a project** / **Move to project**）。前提確認と GitHub アクセスの手順 |
| `Work in a project` | 最初のバッチ、作業の送り方と結果の読み方、プルリクエストのレビュー、Overview の 6 状態、スレッドを開いて操る、モデル選択、**会話で Claude に頼める調整の言い回し 8 例**、承認待ちの解消 |
| `Give a project standing context` | プロジェクトメモリ・プロジェクト指示・リポジトリとファイルと環境の 3 種。指示の書き方の雛形（実例つき） |
| `Project settings reference` | 12 行の設定表（`settings.json` ではなく claude.ai / デスクトップアプリで変える）と、一時停止・アーカイブ・削除 |
| `Usage and cost` | プラン制限に何が乗るか。**1 日 200 スレッド**の強制上限、使用量を下げる 3 手 |
| `How projects relate to other Claude Code features` | Claude Tag・クラウドセッション・ルーティン・ローカルセッションとエージェントビュー・worktree・エージェントチーム・claude.ai チャットと Cowork の旧 Projects との住み分け |
| `Limitations` | 6 件（ターミナル CLI とサードパーティプロバイダ不可、スレッドはクラウドセッション、ローカルセッションは参加不可、サンドボックスの再開失敗で未コミット変更が失われうる、**1 ユーザー専有で共有不可**、スレッドは他プロジェクトへ移せない） |
| `Troubleshooting` | 5 節＋「その他のメッセージ」7 行の表 |
| `Related resources` | 4 ページ＋ローンチ告知ブログ |

### 周辺 10 ページが Projects への導線を受け取った

| ページ | 加わったもの |
|---|---|
| `agents` | 比較表に **Projects の行**が追加され、ページ冒頭が「4 つの並列化手段」から「**5 つ**」に。`llms.txt` の説明文も `and projects` が追記された |
| `platforms` | 「どこから始めるか」の一覧に Projects の行 |
| `mobile` | 到達先の表に Projects の行。冒頭も「クラウドセッションと **projects** に到達する」へ |
| `overview` | ブラウザ実行の説明に「長い作業なら project を作って Claude に並列セッションを束ねさせる」 |
| `desktop` | サイドバーの **Projects**、および**プロジェクト所属セッションではプロジェクトの通知に切り替わる**という但し書き |
| `claude-code-on-the-web` | 冒頭に Projects への導線、GitHub 認証表に「**スレッドはどの接続方法でも Claude GitHub App が必要**」 |
| `web-quickstart` | `/web-setup` トークンの説明に「**project のスレッドは Claude GitHub App が要る**」 |
| `cloud-environments` | 環境セレクタの説明に「**project のスレッドはプロジェクト設定の環境を使う**」。引き継ぎ表も**複数リポジトリのセッション（project のスレッドを含む）はクローンの `.claude/settings.json` を読まない**へ書き換え |
| `routines` | 関連機能に Projects。**プロジェクトから作られたルーティンはその Routines タブに出る** |
| `agent-view` | 「エージェントビューは自分のマシンで自分が配る。Claude に束ねさせたいなら Projects」 |

- [Let Claude coordinate ongoing work with Projects - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/claude-projects#project-settings-reference)
- [Let Claude coordinate ongoing work with Projects - Claude Code Docs (English)](https://code.claude.com/docs/en/claude-projects#project-settings-reference)

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
- [**`errors` に 17 節が新設され、認証エラーがプロバイダごとに書き分けられた**](#1-errors-に-17-節が新設され認証エラーがプロバイダごとに書き分けられた) ([日本語](https://code.claude.com/docs/ja/errors#google-cloud-authentication-failed) / [English](https://code.claude.com/docs/en/errors#google-cloud-authentication-failed)):  
  **`errors` は今回のリファレンス系で最大の 425 行（追加 393・削除 32）**で、**17 の `###` 節が新設**され、エラー索引表に **28 行が追加・2 行が差し替え**られました。中心は **Google Cloud・Microsoft Foundry・Claude apps gateway の認証エラーがプロバイダごとに独立した節を得た**ことで、**v2.1.273 より前はこれらが汎用の `Please run /login` に丸められていた**と各節が明記しています
- [**Agent SDK に MCP Apps 連携が入り、`TaskOutput` と `REPL` が消えた**](#2-agent-sdk-に-mcp-apps-連携が入りtaskoutput-と-repl-が消えた) ([English](https://code.claude.com/docs/en/agent-sdk/typescript#mcpserverprovenance)):  
  `agent-sdk/typescript` は **288 行（桁揃えを除くと 266 行）**動き、`agent-sdk/python` も 85 行（同 69 行）動きました。**`readMcpResource()` と `McpServerProvenance` と `startup_failure_reason` の 3 つが新設**され、**`REPL`（v2.1.275）と `TaskOutput`（v2.1.277）が型ごと削除**されました。**`REPL` は今回の差分で唯一「真に消えた見出し」**です
- [**`output-styles` が全面改稿され、`/output-style` コマンドが復活した**](#3-output-styles-が全面改稿されoutput-style-コマンドが復活した) ([日本語](https://code.claude.com/docs/ja/output-styles#built-in-output-styles) / [English](https://code.claude.com/docs/en/output-styles#built-in-output-styles)):  
  **147 行（追加 109・削除 36）**動き、**組み込み 5 スタイルがそれぞれ h3 を得て実例つきで書き下ろされました**。最も目を引くのは **`/output-style` コマンドの復活**です ―― base には「**v2.1.73 で非推奨・v2.1.91 で削除**」という Note があり、head では **v2.1.269 以降で使える正規の切り替え手段**として先頭に置かれています
- [**VS Code 拡張に 2 リリース分のダイアログが増えた**](#4-vs-code-拡張に-2-リリース分のダイアログが増えた) ([English](https://code.claude.com/docs/en/vs-code#use-the-prompt-box)):  
  `vs-code` は **156 行（桁揃えを除くと 118 行）**動きました。**v2.1.280 で `/status`・`/sandbox`・`/chrome`・`/export`・`/skills`・`/plan` の 6 つの打ち込みコマンドとダイアログが一挙に入り**、v2.1.274〜277 では **Memory / Instructions メニュー、変更単位のレビュー、`/copy`、`/tasks`、`lockEditorGroups`** が入っています
- [**`llm-gateway-protocol` に接続方法別の章とレスポンスヘッダーの章が増えた**](#5-llm-gateway-protocol-に接続方法別の章とレスポンスヘッダーの章が増えた) ([日本語](https://code.claude.com/docs/ja/llm-gateway-protocol#gateway-hint-headers) / [English](https://code.claude.com/docs/en/llm-gateway-protocol#gateway-hint-headers)):  
  **84 行（追加 82・削除 2）**が入り、**h2 が 2 つ（`How the connection method changes client behavior` と `Response headers`）新設**されました。**前回サマリが「changelog に載っただけ」として挙げた 5 つのゲートウェイヒントヘッダーが、ここに独立した節として着地**しています
- [**Claude apps gateway に大規模ロールアウトと無停止再起動の節が入った**](#6-claude-apps-gateway-に大規模ロールアウトと無停止再起動の節が入った) ([日本語](https://code.claude.com/docs/ja/claude-apps-gateway-deploy#large-rollouts) / [English](https://code.claude.com/docs/en/claude-apps-gateway-deploy#large-rollouts)):  
  `claude-apps-gateway-deploy` が **140 行**、`claude-apps-gateway-config` が **122 行**動きました。**数千人規模のロールアウトでサインインのレート制限に当たる 2 つの原因とその見積り方**、**レプリカ 1 台が同時に上流へ流す 256 リクエストという上限**、**`SIGTERM` 後 25 秒のドレイン窓**、**`CLAUDE_GATEWAY_PROXY_IS_EGRESS_BOUNDARY=1`** が加わっています
- [**`monitoring-usage` に管理設定の解決結果を吐く OTel イベントが加わった**](#7-monitoring-usage-に管理設定の解決結果を吐く-otel-イベントが加わった) ([日本語](https://code.claude.com/docs/ja/monitoring-usage#managed-settings-resolved-event) / [English](https://code.claude.com/docs/en/monitoring-usage#managed-settings-resolved-event)):  
  **138 行（追加 108・削除 12）**動きました。**`claude_code.managed_settings_resolved` イベント**が 55 行ぶんの節として新設され、**「どのマシンがどの管理ソースで動いているか」「ポリシーヘルパーが健全か」「なぜ起動を拒否したか」**を 1 イベントで見られるようになりました。あわせて **`tool.output` スパンイベント**が「どのツールがどの条件で記録するか」まで書き下ろされています
- [**`plugin-marketplaces` の背景更新が認証情報ヘルパーを使うようになった**](#8-plugin-marketplaces-の背景更新が認証情報ヘルパーを使うようになった) ([English](https://code.claude.com/docs/en/plugin-marketplaces#private-repositories)):  
  **151 行（桁揃えを除くと 99 行）**動きました。**v2.1.280 で、背景のマーケットプレイス更新が設定済みの git 認証情報ヘルパーを使うようになり**、これまで推奨されていた**グローバル git URL 書き換えの手順（トークンを平文で gitconfig に埋める回避策）がページから丸ごと削除**されました
<!-- light:updated-pages:end -->

> **50 行以上動いたページは 21 ページ（changelog と新規ページを除く）です。** うち `model-config`（90 行）・`memory`（200 行）・`plugins-reference`（180 行）・`skills`（63 行）・`claude-directory`（105 行）はハイライトで、`errors`（425 行）・`agent-sdk/typescript`（288 行）・`vs-code`（156 行）・`plugin-marketplaces`（151 行）・`output-styles`（147 行）・`claude-apps-gateway-deploy`（140 行）・`monitoring-usage`（138 行）・`claude-apps-gateway-config`（122 行）・`agent-sdk/python`（85 行）・`llm-gateway-protocol`（84 行）はこの節で扱っています。**残る 6 ページは「軽微な更新」へ回しました** ―― `cli-reference`（166 行だが**表のセル幅を揃え直したぶんを除くと実質 8 行**）、`settings-reference`（138 行・内容はハイライト 1 と 4 に分解される）、`keybindings`（72 行・同 40 行）、`features-overview`（60 行・同 22 行）、`managed-settings`（60 行・同 26 行）、`env-vars`（52 行）です。

## 1. errors に 17 節が新設され、認証エラーがプロバイダごとに書き分けられた

**`errors` の差分は 425 行（追加 393・削除 32）**で、今回のリファレンス系で最大です。エラー索引表には **28 行が追加され 2 行が差し替え**られ、本文には **17 の `###` 節**が新設されました。

### プロバイダごとに独立した認証エラー節

**base では Google Cloud・Microsoft Foundry・Claude apps gateway の認証失敗が汎用の `Please run /login` / `Failed to authenticate` に丸められていました。** 今回、**それぞれに専用節が付き、すべての節が「v2.1.273 より前は汎用メッセージだった」と明記**しています。

| 新設された節 | 何のエラーか |
|---|---|
| `Google Cloud credentials expired or invalid` | Agent Platform からの 401。`gcpAuthRefresh`・`gcloud auth application-default login`・`GOOGLE_APPLICATION_CREDENTIALS`・ゲートウェイ経由（`CLAUDE_CODE_SKIP_VERTEX_AUTH`）の 4 経路で対処を書き分け |
| `Google Cloud authentication failed` | Agent Platform からの 403（認可拒否）。IAM ロールとモデルアクセスを確認 |
| `Microsoft Foundry authentication failed` | Foundry からの 401 / 403。**`/login` では Azure の認証情報を発行できない**と明記 |
| `Gateway refused the request` | ゲートウェイまたはその上流からの 403。**サインインし直しても変わらない**ので管理者へ。管理者向けに監査ログの読み方も併記 |
| `Sign-in timed out while waiting for you to continue` | Claude apps gateway のサインインで、アカウント確認を開いたまま期限切れになった場合 |

**Amazon Bedrock 側の 2 節も書き換わりました** ―― 「この節は `awsAuthRefresh` を設定しているときだけ出る」という前提が外れ、**設定していなくても出る**ようになった（v2.1.273 以降）ほか、**「認証情報はこの環境が管理している」というヒントが出た場合は他の手順が当てにならない**という分岐が加わっています。

### MCP の再サインインが 4 通りに書き分けられた

`MCP server needs you to sign in again` の 1 節で、**4 つのメッセージが原因ごとに書き分け**られました ―― Claude Code からサインインするサーバー（期限切れ・失効）、`headersHelper` スクリプト（**Claude Code が既にヘルパーを再実行して 1 回リトライ済み**）、設定の静的な `Authorization` ヘッダー、HTTP 403 `insufficient_scope` によるスコープ要求です。**v2.1.273 より前は前 3 者が `requires re-authorization (token expired)` に丸められ**、**スコープ要求は v2.1.274 より前は `needs you to sign in again` に丸められていた**という版の履歴まで残されています。**`oauth.scopes` をピン留めしている場合、Claude Code はサーバーが名指ししたスコープではなくピン留めしたスコープを要求する**ため、足りないスコープをリストに足さないと認証し直しても取れない、という注意も入りました。

### 残る 12 節

- **`Claude login not accepted`**（クラウドセッション作成時の 401）、**`Artifacts need a claude.ai login`**（認証方式ごとに 5 通りの対処）
- **`Single sign-on authorization needed`**（`/install-github-app` で SAML SSO 強制組織を選んだ場合。**v2.1.273 より前は `Admin permissions required` が出ていた**）
- **`Couldn't open Claude Desktop`**（`/desktop` の失敗。**v2.1.275 より前は何が失敗したか言わなかった**）
- **`Custom output styles can't be selected over Remote Control`** と **`Output styles are saved to local settings which this session doesn't load`**（出力スタイル関連の 2 節）
- **`Marketplace is already added from a different source`**、**`Plugin is required by your organization`**（プラグイン関連 2 節）
- **`Command blocked by the worktree isolation checks`**（worktree 隔離の拒否。`${!name}` のような変数間接参照や `${ command; }` が**実行時にコマンドを生みうる**ため、git を名指ししないコマンドでも拒否される）
- **`The connection to Claude Code ended before this message completed`**（VS Code 拡張）、**`otelHeadersHelper failed`**（テレメトリのサイレント停止を知らせる。**`-p` では stderr に出る**）

- [Errors and troubleshooting - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/errors#google-cloud-authentication-failed)
- [Errors and troubleshooting - Claude Code Docs (English)](https://code.claude.com/docs/en/errors#google-cloud-authentication-failed)

## 2. Agent SDK に MCP Apps 連携が入り、TaskOutput と REPL が消えた

**`agent-sdk/typescript` は 288 行（追加 199・削除 89）動き、表のセル幅を揃え直したぶんを除くと 266 行です。** `agent-sdk/python` は 85 行（同 69 行）。

### 入ったもの

| 追加 | 内容 |
|---|---|
| **`readMcpResource()` と `SDKControlMcpReadResourceResponse`** | **MCP Apps の `ui://` リソースを 1 つ読み、アプリ側でツールのウィジェットを描く**（アルファ）。**`_meta` が `McpServerStatus` のツールエントリに乗り**、`ui.resourceUri` / `ui.csp` / `ui.permissions` が通る。**内容は信頼できない第三者の HTML なのでサンドボックスで描く**よう明記。TS SDK v0.3.280 以降 |
| **`McpServerProvenance`** | `mcp__*` ツールを提供したサーバーの `name` と、その定義の出どころ `source`（`sdk` / `plugin` / 設定スコープ）。**フック 5 種（`PreToolUse`・`PostToolUse`・`PostToolUseFailure`・`PermissionRequest`・`PermissionDenied`）と `CanUseTool` が受け取る**。原文は「**信頼判断は `source` で行い、`name` や `mcp__<server>__` 接頭辞で判断するな。`sdk` 以外の `name` は信頼できないテキストなので表示前にエスケープせよ**」と踏み込んでいる。SDK v0.3.274 以降 |
| **`startup_failure_reason`** | **Claude Code が起動を拒否した理由 16 値**を `error_during_execution` 結果に載せる。既定で載るのは worktree 関連 2 値と `session_held_by_background` だけで、**全 16 値を受け取るには `CLAUDE_CODE_STARTUP_FAILURE_RESULTS=1`**。SDK v0.3.274 以降 |
| **`projectConfigRoot`** | `cwd` が worktree のとき、**プロジェクト設定・`.mcp.json`・`.claude/` のコマンドやスキルを読む元のチェックアウト**を指す。`CLAUDE.md` と `.claude/rules/` は `cwd` から読む。v2.1.275 以降 |
| **`updateSettings()` の `"userSettings"`** | **`effortLevel` をモデル別にユーザー設定へ保存**（`max` は書かれない）。実行中セッションの努力は変わらない。TS SDK v0.3.277 以降 |
| **貼り付けの明示** | `SDKUserMessage` に **`pasted_content`**（SDK v0.3.277 以降）と **`inline_pastes`**（TS SDK v0.3.280 以降）。**Claude Code が `<pasted_content>` タグで囲み、貼り付けられた素材とユーザー自身の言葉を区別できるようにする** |
| **`SystemPromptCustom`（Python）** | `{"type": "custom", "prompt": ..., "snapshot": ...}`。**文字列で渡すのと等価だが `snapshot` を付けられる**。`claude-agent-sdk` v0.2.153 以降 |

### 消えたもの

- **`REPL`（v2.1.275 で削除）**: `REPLInput` / `REPLOutput` の型定義ごと消え、「v2.1.274 までは `CLAUDE_CODE_REPL=1` で有効にできる実験的ツールだった」という 1 行に置き換わりました。**今回の差分で `REPL` の h3 が唯一「真に消えた見出し」**です
- **`TaskOutput`（v2.1.277 で削除）**: `TaskOutputInput` / `TaskOutputOutput` も削除。**`disallowedTools` や deny ルールに名前が残っていても警告なしで無視**されます。`permissions` にも「**Claude Code が削除したツールの名前は起動時警告の対象外**」という但し書きが加わりました

### `applyFlagSettings(null)` の挙動が 3 キーだけ特別扱いになった

`null` を渡してフラグ層からキーを消したとき、**ほとんどのキーは「`query()` の `settings` が起動時に置いた値 → 下位ソース」へ落ちます**が、**`effortLevel`・`agent`・`ultracode` の 3 キーはセッション状態をリセットするだけで下位に落ちません**。`model` も従来どおり Claude Code の既定モデルへ戻ります。

- [Agent SDK reference - TypeScript - Claude Code Docs (English)](https://code.claude.com/docs/en/agent-sdk/typescript#mcpserverprovenance)
- [Agent SDK reference - Python - Claude Code Docs (English)](https://code.claude.com/docs/en/agent-sdk/python#systempromptcustom)

## 3. output-styles が全面改稿され、/output-style コマンドが復活した

**`output-styles` の差分は 147 行（追加 109・削除 36）**で、ページ説明文まで書き換わりました（`llms.txt` の 1 行も「Adapt Claude Code for uses beyond software engineering」から「Concise や Explanatory などの組み込みスタイルでロール・トーン・応答形式を変える」へ）。

### `/output-style` が戻ってきた

**base には「標準の `/output-style` コマンドは v2.1.73 で非推奨になり v2.1.91 で削除された。`/config` かキーを直接編集せよ」という Note がありました。** head ではこの Note が消え、**`/output-style <style>` が切り替え手段の先頭**に置かれています（**v2.1.269 以降**）。

- 引数なしで実行すると**選べるスタイルを並べて現在のスタイルに印を付ける**
- **非対話モード・Agent SDK セッション・Remote Control 経由（モバイル／Web）でも動く**。ただし Remote Control では**組み込みスタイルのみ**
- **コマンドはスタイル名の大文字小文字を区別しない**（一方で `outputStyle` 設定の値は区別し、`explanatory` と書くと既定スタイルになる）

`commands`・`headless`・`remote-control`・`prompt-caching`・`agent-sdk/modifying-system-prompts` の各ページにも `/output-style` の記述が加わり、`output-style` という語は **61 か所から 115 か所**に増えました。

### 組み込み 5 スタイルがそれぞれ節を得た

base では 4 スタイルが 1 行ずつの箇条書きでしたが、head では **`Default`・`Proactive`・`Concise`・`Explanatory`・`Learning` がそれぞれ h3** になり、**`Insight` ブロックと `Learn by Doing` リクエストの実例が本文に入りました**。

- **`Default` は「出力スタイルが選ばれていない状態」**であり、`/output-style` の一覧には他と並んで出る
- **`Proactive`** の説明から「auto モードより強い自律実行の指示」という比較が消え、代わりに**「データを消す／共有・本番システムを変える操作の前には会話で確認する、という指示がスタイル側に入っている。これは権限プロンプトとは別物」**という書き方になった
- 新設の **h2「出力スタイルと他の機能の選択」**が、base の「関連機能との比較」表を置き換えた。**6 行（出力スタイル・CLAUDE.md・スキル・フック・サブエージェント・`--append-system-prompt`）に増え、「なぜそれが向くか」の列が付いた**

**`How output styles work` から 1 行消えています** ―― 「既定以外のスタイルを選んだとき、Claude Code は会話中にもスタイルを Claude に再通知する」という記述です。

- [Output styles - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/output-styles#built-in-output-styles)
- [Output styles - Claude Code Docs (English)](https://code.claude.com/docs/en/output-styles#built-in-output-styles)

## 4. VS Code 拡張に 2 リリース分のダイアログが増えた

**`vs-code` の差分は 156 行（追加 121・削除 35）**で、表の桁揃えを除くと 118 行です。`[VSCode]` タグ付き changelog 項目は 6 リリースで **67 件**あり、今回最多のタグです。

### v2.1.280 で入った 6 つの打ち込みコマンド

| コマンド | ダイアログ |
|---|---|
| `/status` | セッションのバージョン・アカウント・モデル・MCP サーバーの詳細 |
| `/sandbox` | サンドボックスモード・非サンドボックスのフォールバック・除外コマンド。**その場でモード変更と除外コマンド追加ができる** |
| `/chrome` | Claude in Chrome の接続状態。**claude.ai アカウントでのサインインが必要** |
| `/export` | 会話を平文でコピーまたは保存。**`/export notes.txt` のようにファイル名を付けるとダイアログを飛ばせる** |
| `/skills` | スキル一覧。**各行に可視性（`On` / `Name only`）が出て、クリックで変更できる**（プラグインスキルなど `locked` の行は除く） |
| `/plan` | プランモードへ切り替え。**`/plan fix the auth bug` のようにタスクを付けるとそのまま計画を始め、`/plan open` はプランファイルをエディタで開く** |

### v2.1.274〜277 で入ったもの

- **Customize メニューの `Memory` と `Instructions`**（v2.1.274）。Memory は auto memory のオン／オフに加え、**保存済みメモリの閲覧・編集・削除とファイルを開く操作**（v2.1.275）まででき、Instructions は **`CLAUDE.md` を選んで開く**（無ければ作る）
- **変更単位のレビュー**（v2.1.275）。差分の各変更に **Accept this change / Reject this change** が付き、カーソル位置に対する Command Palette コマンドも増えた。**変更が 100 件を超える差分ではボタンが出ない**
- **`/copy`**（v2.1.277）で直前の応答をコピー（`/copy 2` で 2 つ前）、**`/logout`**（同）でサインアウト、**`/tasks`**（同）でエージェントマップを開いて**背景シェルなどのバックグラウンドタスクも一覧・停止**
- **`lockEditorGroups`**（v2.1.274）。Claude が開くエディタグループをロックし、**Claude のタブにフォーカスがある間に開いたファイルが隣に並ばない**ようにする。オフにもできる
- **`continueAfterReload`**（v2.1.274）。ウィンドウ再読み込みで中断されたステップを**チャットに注記を出して継続**する。**1 時間以上前に中断された場合や他で開かれている場合はアイドルで戻る**
- **`scrollToBottomOnSend`**（v2.1.275）

### 選択テキストの取り扱いが絞られた

**ワークスペース内のファイルが `files.exclude` / `search.exclude` に一致する場合、Claude が受け取るのは最大でもファイルパスだけになり、選択したテキストは渡りません。** git が無視するファイルも（VS Code の `search.useIgnoreFiles` と拡張の `respectGitIgnore` が両方オンなら）同様です。**この絞り込みはチャットパネル限定**で、統合ターミナルで CLI を走らせた場合は従来どおり選択テキストが送られるため、**`Read` の deny ルールを足せ**と案内されています。

### アクセシビリティ

新設の **h3「キーボードからチャットパネルを使う」**に、**スクリーンリーダーが読み上げる話者ラベル 4 種**（`You` / `Claude` / `Claude, Bash` / `Claude, thinking`）と、**権限プロンプトの選択肢が「どこに保存されるか」を読み上げ、左右キーで保存先を変えられる**（v2.1.268 以降）という記述が入りました。**`Focus last message`** コマンドも表に加わっています。

- [Use Claude Code with VS Code - Claude Code Docs (English)](https://code.claude.com/docs/en/vs-code#use-the-prompt-box)

## 5. llm-gateway-protocol に接続方法別の章とレスポンスヘッダーの章が増えた

**`llm-gateway-protocol` の差分は 84 行（追加 82・削除 2）**で、**h2 が 2 つ新設**されました。

### 接続方法でクライアントの振る舞いが変わることが表になった

新設の **`How the connection method changes client behavior`** は、ゲートウェイが見る 3 つのクライアント挙動を並べます ―― **Bedrock / Agent Platform 形式**、**Anthropic Messages 形式**、**Claude apps gateway サインイン**。5 行の比較表で、既定のモデル ID の形・送る `anthropic-beta` 値・**Claude Code が認識しないモデル ID（ゲートウェイエイリアス）に対するリクエストフィールド**・1 時間プロンプトキャッシュ TTL の要求方法・バックグラウンドタスクのモデルを書き分けています。

**要点は「Claude apps gateway サインインは Anthropic Messages 形式で話すが、任意の上流へルーティングしうるので、Bedrock と Agent Platform も受け入れる部分集合しか送らない」**という一段です。

### ゲートウェイヒントヘッダーが着地した

**前回サマリが「changelog に載ったが本文に対応記述が無い」として挙げた 5 つのヘッダーが、独立した h3 として着地しました**（**v2.1.273 以降**）。

| ヘッダー | 内容 |
|---|---|
| `x-claude-code-request-class` | `main` / `subagent` / `workflow` / `compaction` / `auxiliary`。**全リクエストに付く** |
| `x-claude-code-agent-type` | `Explore`・`Plan`・`general-purpose` などの組み込み型名、`custom` / `teammate` / `fork`。**ユーザーが付けたエージェント名は送らない** |
| `x-claude-code-compaction` | 圧縮要求に付き、`auto` / `manual` / `reactive` で引き金を示す |
| `x-claude-code-context-compacted` | 圧縮後の最初のメイン会話リクエストに 1 回。**それ以前のプレフィックスを鍵にしたキャッシュは捨てられる** |
| `x-claude-code-prev-tool-durations` | `Bash=742;Read=9` の形でツール実行時間。**最大 32 エントリ・4 KB**、ツール名はパーセントエンコード。**権限プロンプトとフックの時間は除外**され、並列呼び出しは各自の時間を報告するのでリクエスト間のギャップには足し合わない |

**送信条件はバックエンドで異なります** ―― Anthropic API 直結は既定オン、カスタムベース URL は**既定オフ**（未知のヘッダーを拒否するプロキシがあるため）、その他のバックエンドは `CLAUDE_CODE_GATEWAY_HINT_HEADERS=1` のときだけ。`0` で全接続とも停止します。

### レスポンスヘッダーの節が新設された

**`Response headers`** は、**Claude Code が読む 4 つのレスポンスヘッダー**（`content-type`・`retry-after`・`x-should-retry`・`anthropic-ratelimit-unified-*`）について「何を返すべきか」と「なぜか」を書いています。**`retry-after` は HTTP 日付ではなく整数秒で返す**、`CLAUDE_CODE_RETRY_WATCHDOG` セッション外では**60 を超える値はリトライを止めて即時エラー表示になる**という具体まで入りました。

あわせて、**advisor ツールのエントリを上流が「認識できないツール型」として拒否したときのリトライ**（v2.1.280 以降。`Input tag 'advisor_20260301'` で認識する）と、**思考署名の `bound to a different conversation` 拒否**の扱いが追加されています。

- [Keep an LLM gateway compatible with Claude Code - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/llm-gateway-protocol#gateway-hint-headers)
- [Keep an LLM gateway compatible with Claude Code - Claude Code Docs (English)](https://code.claude.com/docs/en/llm-gateway-protocol#gateway-hint-headers)

## 6. Claude apps gateway に大規模ロールアウトと無停止再起動の節が入った

**`claude-apps-gateway-deploy` が 140 行（追加 104・削除 36）、`claude-apps-gateway-config` が 122 行（追加 112・削除 10）**動き、`claude-apps-gateway` 本体も 27 行動きました。

### 大規模ロールアウト

新設の **`Large rollouts`** は、サインインのレート制限（**クライアント IP ごとに 10 分あたりサインイン開始 30 回・コード送信 10 回**）に数千人規模のロールアウトが初日で当たる 2 つの原因を挙げます。

1. **ロードバランサの向こうが見えていない** ―― `listen.trusted_proxies` が無いと全員が LB のアドレスに見えて 1 つの枠を共有する。**`X-Forwarded-For` を無視した初回にゲートウェイが警告を出す**
2. **多数の開発者が少数の NAT / VPN 出口を共有している**

**サイズの見積り方まで書かれています** ―― 開発者数を出口アドレス数で割り、10 分窓に何人がサインインするか見て、**リトライと「Claude Code と Claude Desktop の両方にサインインする人」を見込んで倍にする**。1 万人・出口 4 つ・1 時間で均等なら 1 アドレス 2,500 人、10 分あたり約 420 人、倍にして切り上げて 1,000 という実例つきです。**`device_verify` は他人のサインインコードの推測を止めているものなので、見積りを超えては上げるな**と念押しされています。

### 同時上流リクエストとドレイン

| 項目 | 内容 |
|---|---|
| 同時上流リクエスト | **レプリカごとに既定 256**。ストリーミング応答はストリームが終わるまで枠を占める。**枠が埋まっている間に来たリクエストはゲートウェイ内で待ち**、開発者からは「応答が始まらない／固まった」ように見える。`provider: anthropic` 上流では `timeouts.upstream_ttfb_ms` を超えて待つとその上流を諦め、後続が無ければ 502 |
| 上げ方 | レプリカを増やすか、**`BUN_CONFIG_MAX_HTTP_REQUESTS`（1〜65535）**を設定してコンテナを再起動 |
| CPU オートスケールの罠 | **枠が埋まったレプリカはリクエストを待たせるだけでスケールアウトを誘発しない**ので、`client requests are open` 警告が出るときの CPU 水準より低い目標値にする |
| ドレイン | `SIGTERM` で新規接続を止め、**進行中のリクエストとストリームを最大 25 秒待って**終了（**ゲートウェイ v2.1.274 以降**）。`CLAUDE_GATEWAY_DRAIN_TIMEOUT_MS` で延ばせるが、**オーケストレータの猶予期間をドレイン窓より 5 秒以上長く**する必要がある |
| プラットフォーム上限 | **Amazon ECS on Fargate の `stopTimeout` は最大 120 秒**、**Cloud Run は `SIGTERM` の 10 秒後にインスタンスを止める**（ドレイン窓に関わらず 10 秒） |

### プロキシだけが出口の環境と上流への静的ヘッダー

**`CLAUDE_GATEWAY_PROXY_IS_EGRESS_BOUNDARY=1`**（**v2.1.277 以降**）で、**ゲートウェイは名前解決を自分でせずホスト名をプロキシに渡す**ようになります。**`gateway.yaml` のキーではなく環境変数にしたのは「設定ファイルの中身でアドレス検査を緩められないようにするため」**と明記されています。有効化には **`HTTPS_PROXY` または `HTTP_PROXY` が設定済み・`NO_PROXY` と `no_proxy` が空・`CLAUDE_GATEWAY_ALLOW_LOOPBACK` が無効**の 3 条件すべてが必要で、**満たさない場合は起動時に「どの変数が止めたか」を警告して既定動作を続けます**。原文は Warning で「**プロキシの許可リストがゲートウェイ自身の検査と同等以上に厳しいときだけ使え。クラウドメタデータやリンクローカルやプロキシ自身のループバックを、名前ではなく解決先のアドレスで拒否できなければ SSRF ガードが外れる**」と釘を刺しています。

もう 1 つの新節 **`Static headers on upstream requests`**（**v2.1.277 以降**）は、上流ごとに固定ヘッダーを付ける `headers:` マップです。**`authorization`・`x-api-key`・`host`・`content-type`・`user-agent`、および `anthropic-` / `x-goog-` / `x-amz-` / `x-amzn-` で始まる名前は予約**されており、使うと起動に失敗します。**Bedrock / Claude Platform on AWS では SigV4 署名の一部になるのでプロキシが素通しする必要がある**、という但し書きも入りました。

- [Deploy and operate the Claude apps gateway - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/claude-apps-gateway-deploy#large-rollouts)
- [Deploy and operate the Claude apps gateway - Claude Code Docs (English)](https://code.claude.com/docs/en/claude-apps-gateway-deploy#large-rollouts)

## 7. monitoring-usage に管理設定の解決結果を吐く OTel イベントが加わった

**`monitoring-usage` の差分は 138 行（追加 117・削除 21）**です。

### `claude_code.managed_settings_resolved`

新設された 55 行ぶんの節が、**セッションが解決した管理設定を吐くイベント**を定義します（**v2.1.274 以降**）。出るタイミングは**セッション開始時**、**セッション中に管理設定かポリシーヘルパーの状態が変わったとき**、**管理設定が原因で起動を拒否／セッションを終了したとき**の 3 つで、`managed_settings.trigger` が `startup` / `change` / `refused` を示します。

用途として原文が挙げるのは、**「想定外の管理ソースで動いているマシンを見つける」「ポリシーヘルパーが失敗しているマシンを見つける」「マシンが起動を拒否した理由を知る」**の 3 つです。`refused` の `error.type` は 7 値（`helper_failed` / `policy_invalid` / `consent_rejected` / `force_refresh_failed` / `gateway_rejected` / `version_below_minimum` / `_OTHER`）。

**既定では設定の中身を出しません。** `OTEL_LOG_MANAGED_SETTINGS=1` を付けると**伏せ字化した設定と、伏せ字化前の SHA-256 ダイジェスト**が乗ります。伏せ字化の規則が細かく書かれています ―― **スキーマが宣言する設定名は出し、宣言しないキーは落とす**／真偽値・数値・選択肢固定の文字列はそのまま／**それ以外の文字列（`model`・`apiKeyHelper`・`env` の値・URL・コマンド）は `"[REDACTED]"`**／マップのエントリ名はそのまま／**権限ルールはツール名だけ残して中身を伏せる**（`Read([REDACTED])`）／**8 KB で切るので切れた値は妥当な JSON ではない**。

**ダイジェストを既定で出さない理由も書かれています** ―― 「**短いポリシーはハッシュを推測して復元できるため**」。また**信頼していないフォルダの対話セッションでは拒否イベントを送りません**（プロジェクト設定やローカル設定が送信先を書き換えうるため）。

### `tool.output` スパンイベントが条件ごとに書き分けられた

base では「`OTEL_LOG_TOOL_CONTENT=1` のとき、このスパンはツールの入出力を持つ `tool.output` イベントも記録する」の 1 行でした。head では **21 行**に増え、**記録される条件が明示**されました。

- **Read と Bash は `OTEL_LOG_TOOL_CONTENT=1` だけで記録**、**Edit と Write は `OTEL_LOG_TOOL_DETAILS=1` も必要**
- **エラーで終わった呼び出しは何も記録しない**
- **Read がファイルテキスト以外（画像・PDF・内容が変わっていないファイルの再読み込み）を返した場合も記録しない**
- **それ以外のツール（MCP ツール・WebFetch を含む）は対象外**
- 属性は 5 つ（`content` / `output` / `diff` / `file_path` / `bash_command`）で、**それぞれ 60 KB で切られ、切られたものには `<attribute>_truncated` と `<attribute>_original_length` が付く**

**`new_context` 属性のゲートがスパンごとに違う**ことも新設の段落で明記されました ―― `claude_code.tool` では `OTEL_LOG_TOOL_CONTENT=1`、`claude_code.interaction` と `claude_code.llm_request` では `OTEL_LOG_USER_PROMPTS=1`。プライバシーの節にも「**`OTEL_LOG_USER_PROMPTS` はプロンプト本文より広く、`llm_request` スパンのツール結果にも及ぶ**」という警告が入りました。

そのほか、**`api_request_body` と `api_response_body` を `request_body_id` で対応付けられるようになり**、ファイルモード（`OTEL_LOG_RAW_API_BODIES=file:<dir>`）では **`index.jsonl` に 1 行ずつ索引が書かれる**ようになりました（**v2.1.274 以降**）。

- [Monitoring - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/monitoring-usage#managed-settings-resolved-event)
- [Monitoring - Claude Code Docs (English)](https://code.claude.com/docs/en/monitoring-usage#managed-settings-resolved-event)

## 8. plugin-marketplaces の背景更新が認証情報ヘルパーを使うようになった

**`plugin-marketplaces` の差分は 151 行（追加 84・削除 67）**で、桁揃えを除くと 99 行です。**削除が 67 行と多いのは、これまで推奨されていた回避策が丸ごと消えたため**です。

### 消えた回避策

base は「背景の `git pull` は認証情報ヘルパーを無効にするので HTTPS でプライベートリポジトリに認証できない」という前提に立ち、**グローバル git URL 書き換え**（`git config --global url."https://x-access-token:YOUR_TOKEN@github.com/..."` でトークンを埋める）を案内していました。プロバイダ別の URL 形式表（GitHub / GitLab / Bitbucket）と、**「トークンが gitconfig に平文で入るので読み取り専用トークンを使え」**という注意まで付いていました。

**head ではこの一連の記述が丸ごと削除されました。** **v2.1.280 で、背景チェックが設定済みの git 認証情報ヘルパーを使う**ようになり、回避策が不要になったためです。

| | base | head |
|---|---|---|
| 背景チェックの認証 | **認証情報ヘルパーを無効化**。HTTPS のプライベートリポジトリに認証できない | **設定済みヘルパーを使う**。ただし**非対話で走る**（git の端末プロンプトと askpass を切り、ヘルパーにも尋ねるなと伝える） |
| 保存済み認証情報を出せるヘルパー | ―― | **認証できる**（Git Credential Manager・macOS Keychain ヘルパー・`git-credential-store`） |
| 尋ねる必要があるヘルパー | ―― | **背景では答えられず、更新は静かに失敗して既存のチェックアウトが残る**。`/plugin marketplace update <name>` を手で実行する |
| 最新だったとき | 再クローンをスキップ | **そのまま**（変更なし） |
| 新しいコミットがあった／到達も認証もできなかったとき | 再クローン | **再クローン**（失敗すれば既存のチェックアウトが残る） |

**オフライン環境のトラブルシューティングも書き換わりました** ―― **v2.1.274 より前は「既存チェックアウトで `git pull` し、失敗したらチェックアウトを退避して再クローンし、あとでベストエフォートで戻す」**という手順だったのが、**「リモートを覗いて新しいコミットを探し、覗けなければ再クローンを試みる。失敗すれば既存のチェックアウトがそのまま残る」**に整理されています。

### そのほか

- **Git LFS のコンテンツはクローン時に一切ダウンロードしなくなりました**（LFS 追跡ファイルはポインタで届く）。`settings-reference` 側では **`skipLfs` フィールドが「受け付けるが効果なし」**になり、**v2.1.274 より前は `"skipLfs": true` を設定しないと LFS を落としていた**と明記されました
- **npm ソースの取得方法が書き下ろされました** ―― `npm install` ではなく**「npm クライアントで解決してtarball を落とし、プラグインキャッシュへ展開する」**方式で、**パッケージ自身の `preinstall` / `postinstall` は一切走りません**
- **マーケットプレイス名に `npm`・`pip`・`uv`・`cargo`・`github`・`gh` を使えなくなりました**（大文字小文字を問わず・**v2.1.275 以降**）
- **ローカルディレクトリのマーケットプレイスが列挙する相対パスのプラグインは、キャッシュにコピーされず元の場所から読まれる**ようになりました。**バージョンを上げなくても次のセッション開始または `/reload-plugins` で編集が効き**、`CLAUDE_PLUGIN_ROOT` は安定したソースディレクトリを指します

- [Create and distribute plugin marketplaces - Claude Code Docs (English)](https://code.claude.com/docs/en/plugin-marketplaces#private-repositories)

## 軽微な更新

<!-- light:minor-updates:start -->
今回の差分は **3 ファイル・5,436 行**（追加 4,062・削除 1,374）です。内訳は `llms-full.txt` が 5,285 行（追加 3,933・削除 1,352）、見出しマップ（`en/claude_code_docs_map.md`）が 122 行（追加 114・削除 8）、`llms.txt` が 29 行（追加 15・削除 14）。`llms-full.txt` の総行数は **97,637 行から 100,218 行へ 2,581 行増え**、展開ページ数は **196 から 197**、**本文が変わったページは 116 / 197**（前回は 118 / 196）でした。**h2 以下の見出しは 4,320 件から 4,427 件**になり、**新規 114 件・消失 7 件**です ―― **消失 7 件のうち 6 件は改称または格上げ**（`memory` の `AGENTS.md` が h3→h2、`permission-modes` の `Server-side classifier review` が h4→h3、`output-styles` の 2 件、`sub-agents` の `Supported frontmatter fields` が h4→`Frontmatter reference` h3、`security-guidance` の 1 件）で、**真に消えたのは `agent-sdk/typescript` の `REPL` 1 件だけ**です。

**今回 changelog に積まれたのは v2.1.274・275・276・277・278・280 の 6 リリース・407 項目**です（詳細はハイライト 5 参照）。**本文に書き下ろされた項目には v2.1.268〜v2.1.273 で既に告知済みだったものも含まれます**（必要バージョンは各項目に併記しています）。**本文側に対応記述が見つからない項目にはリンクを付けていません**（changelog ページの URL は方針どおり使いません）。

**新機能**

- **Opus 5.5 が入りました**（`claude-opus-5-5`・v2.1.280 以降・詳細はハイライト 1 参照）— [Model configuration](https://code.claude.com/docs/en/model-config#model-aliases)
- **`AGENTS.md` をプロジェクト指示として直接読めるようになりました**（v2.1.277 以降・詳細はハイライト 3 参照）— [日本語](https://code.claude.com/docs/ja/memory#agents-md) / [How Claude remembers your project](https://code.claude.com/docs/en/memory#agents-md)
- **claude.ai アカウントのスキルとプラグインがターミナルセッションにも同期されるようになりました**（詳細はハイライト 4 参照）— [日本語](https://code.claude.com/docs/ja/skills#where-synced-skills-load) / [Extend Claude with skills](https://code.claude.com/docs/en/skills#where-synced-skills-load)
- **`Ctrl+Enter`（または `Ctrl+X Ctrl+S`）で、キューに溜めたメッセージを今すぐ送れるようになりました**。**実行中のターンを中断して、キューのメッセージと書きかけの下書きを一度に出します**。シェルモードでは中断せずキューに入れるだけ。**拡張キーを報告しないターミナルでは `Ctrl+Enter` がただの `Enter` として届く**ため、`Ctrl+X Ctrl+S` がどのターミナルでも効く綴りです。`keybindings` では `chat:sendNow` アクションとして定義されました。**v2.1.275 以降** — [日本語](https://code.claude.com/docs/ja/interactive-mode#queue-messages-while-claude-works) / [Interactive mode](https://code.claude.com/docs/en/interactive-mode#queue-messages-while-claude-works)
- **プロンプト内の不可視 Unicode 文字を送信前に除去するようになりました**。タグ文字・双方向制御・ゼロ幅スペースなどが対象で、**ペルシア語やインド系文字の接合子と絵文字の異体字選択子は残します**。**除去があったとき、その Enter は何も送らず**、`Removed 3 invisible characters · review and press Enter to send` の注記付きで清書がプロンプトに戻ります。**コマンドラインで渡した場合やパイプで流した場合は 2 回目の Enter を待ちません**（ただし清書が `/` で始まるならプロンプトに戻す）— [日本語](https://code.claude.com/docs/ja/interactive-mode#invisible-characters-in-prompts) / [Interactive mode](https://code.claude.com/docs/en/interactive-mode#invisible-characters-in-prompts)
- **貼り付けたテキストが「貼り付け」として Claude に届くようになりました**。`[Pasted text #N]` プレースホルダの中身が**「どこかからコピーしてきたもので、あなたが書いたものではない」と印付きで**渡り、**Claude は「貼り付けの中の指示は、あなたが打った本文が求める範囲でだけ従う」と伝えられます**。フックの `UserPromptSubmit` では `<pasted_content id="…">` 行に挟まれて届くので、**プロンプトを解析するフックはこの 2 行を見込む必要があります**。feature flag を取得しないセッションでは印が付きません — [日本語](https://code.claude.com/docs/ja/terminal-config#how-claude-treats-pasted-text) / [Terminal configuration](https://code.claude.com/docs/en/terminal-config#how-claude-treats-pasted-text)
- **音声入力をキャンセルできるようになりました**。`Esc` または `Ctrl+C` でマイクを止めて書き起こしを破棄し、録音前のプロンプトに戻します。**録音後の処理中でも効き**、**そのキー押下は他の作用を持ちません**（`Esc` は応答を中断せず、`Ctrl+C` は終了の 1 回目に数えない）— [Voice dictation](https://code.claude.com/docs/en/voice-dictation#cancel-a-recording)
- **`CLAUDE_CODE_PLUGIN_DIRS` が加わりました**。`--plugin-dir` を渡せない場所でプラグインを読み込むための環境変数で、**Unix は `:`、Windows は `;` 区切り**、**絶対パスまたは `~` 始まりのみ**（相対パスは飛ばされる）。**v2.1.280 以降** — [Plugins](https://code.claude.com/docs/en/plugins#test-your-plugins-locally)
- **`CLAUDE_CODE_MAX_MCP_DESCRIPTION_LENGTH` が加わりました**。MCP ツール説明とサーバー指示の 2,048 文字上限を変えます。**v2.1.280 以降** — [日本語](https://code.claude.com/docs/ja/mcp#for-mcp-server-authors) / [Connect Claude Code to tools via MCP](https://code.claude.com/docs/en/mcp#for-mcp-server-authors)
- **`CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS` が加わりました**（1〜256・既定 16）。**各エージェントのトランスクリプトが Claude Code のメモリに載るので、上げるとメモリ使用量が増える**と明記されています。**v2.1.269 以降** — [Dynamic workflows](https://code.claude.com/docs/en/workflows#let-claude-decide-with-ultracode)
- **`CLAUDE_CODE_MCP_STARTUP_WAIT_MS` が加わりました**。非対話セッションの最初のターンが接続中の MCP サーバーを待つ時間で、**設定すると待ちが全ペンディングサーバーに及び**、`0` で待たない。**`--permission-prompt-tool` のサーバーは値に関わらず自前の `MCP_TIMEOUT` を保ちます**。**v2.1.274 以降** — [Agent SDK MCP](https://code.claude.com/docs/en/agent-sdk/mcp#connection-timing)
- **`CLAUDE_CODE_STARTUP_FAILURE_RESULTS`**（起動拒否理由を全 16 値ぶん結果メッセージに載せる・v2.1.274 以降）、**`CLAUDE_CODE_BG_TASKS_REPORT_RUNNING`**（背景作業が生きている間ターン終了後も running を報告する既定の opt-out・v2.1.269 以降）、**`CLAUDE_CODE_DISABLE_WINDOWS_SHELL_LAUNCHER`**（Windows の PowerShell コマンドを `cmd.exe` ランチャ経由にしない・v2.1.269 以降）、**`CLAUDE_CODE_GATEWAY_MODEL_DISCOVERY_TIMEOUT_MS`**（既定 3000・v2.1.269 以降）、**`OTEL_LOG_MANAGED_SETTINGS`**（v2.1.274 以降）、**`VERTEX_REGION_CLAUDE_5_5_OPUS`**（v2.1.280 で追加）が `env-vars` に加わりました — [Environment variables](https://code.claude.com/docs/en/env-vars#variables)
- **カスタムシステムプロンプトをキャッシュ境界で分割できるようになりました**。`--system-prompt` / `--system-prompt-file` で渡す文字列に **`__SYSTEM_PROMPT_DYNAMIC_BOUNDARY__` だけの行**を置くと、Claude Code は最初のその行でプロンプトを分割して行自体を削り、**上側はキャッシュされたまま下側だけが毎回変わる**ようになります。SDK では配列形式のほうが推奨です。**v2.1.275 以降** — [CLI reference](https://code.claude.com/docs/en/cli-reference#system-prompt-flags)
- **プラグインの `userConfig` フィールドを固定の選択肢に絞れるようになりました**（`options`・v2.1.271 以降）。`type` は `string` 必須、`multiple` と `sensitive` は不可、`default` は選択肢のいずれか、**1〜64 文字・前後の空白不可・制御文字や不可視文字や書字方向を変える文字は不可・大文字小文字違いの重複も不可**。**破ると読み込みに失敗**し、`claude plugin validate` がどのフィールドがどの規則を破ったか示します — [Plugins reference](https://code.claude.com/docs/en/plugins-reference#user-configuration)
- **プラグインの `agents/` サブフォルダがエージェント名の一部になりました**。`agents/review/security.md` は `my-plugin:review:security` として読み込まれ、**フロントマターの `name` はファイル名部分だけを置き換え**、**マニフェストの `agents` フィールドに列挙したファイルはサブフォルダ名を含まない名前**になります — [Plugins reference](https://code.claude.com/docs/en/plugins-reference#plugin-agent-frontmatter)
- **Claude apps gateway のサインインで、ゲートウェイがアカウント名を返せるようになりました**（トークンレスポンスの任意 `email` フィールド）。**開発者が確認してから認証情報が保存され**、`/status` に出ます。**v2.1.275 以降**。あわせて **`/logout` がゲートウェイ側のセッションも終わらせる**ようになりました（discovery に `revocation_endpoint` を出しているゲートウェイのみ・ベストエフォート）— [Claude apps gateway](https://code.claude.com/docs/en/claude-apps-gateway#connect-developers)
- **セルフホストランナーに `SELF_HOSTED_RUNNER_POST_TURN_SETTLE_MS` が加わりました**（既定 7000）。`--drain-wait-sec` のドレイン中、ターン終了をランナーが「まだ忙しい」と数える上限で、**`0` や不正値では既定に戻るので保持をオフにはできません**。**v2.1.275 以降** — [Self-hosted environments reference](https://code.claude.com/docs/en/self-hosted-environments-reference#runner-cli-flags)

**機能改善**

- **auto モードのサーバー側分類器が再び既定になりました。** 前回サマリは「**v2.1.271 と v2.1.272 では既定だったが、v2.1.273 で `CLAUDE_CODE_AUTO_MODE_SERVER=1` のオプトインに戻された**」と書きました。**今回、v2.1.278 で再び既定に戻り、対象も広がっています** ―― **Enterprise プランと Claude API のアカウント、Claude Platform on AWS、Amazon Bedrock、Google Cloud's Agent Platform、Microsoft Foundry、そして `ANTHROPIC_BASE_URL` を LLM ゲートウェイやプロキシに向けた場合**。**オプトアウトは `CLAUDE_CODE_AUTO_MODE_SERVER=0`** になり（Anthropic API 直結では読まれない）、**`CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS=1` を設定して本変数を未設定にすると尋ねるのを止めます**。フォールバックがセッション中ずっと続く場合は**分類器リクエストの課金に関する注意が出ます**。`/status` にも `Auto mode server` 行が付きました — [Permission modes](https://code.claude.com/docs/en/permission-modes#server-side-classifier-review)
- **会話で述べた承認が分類器に届くようになりました**。`permission-modes` に新設された節で、**「動作と、危険にしている具体（force push ならどのブランチか）を名指しする必要がある」「動詞だけでは何も解けない」「承認は名指しした 1 回ぶんで、常設として与えない限り次は再びブロックされる」「解けないブロックもある」**の 4 点が示されました — [Permission modes](https://code.claude.com/docs/en/permission-modes#eliminate-prompts-with-auto-mode)
- **キューに溜めたメッセージの送信が自動になりました**。base は「ターンが終わっても溜まっていれば、Claude Code は**最も古い 1 件だけ**を次のターンとして送り、残りは同じ規則で待つ」でしたが、head は「**キーを押さずに、打った順で出ていく**」になりました。**送信済み・キュー済みのメッセージは Claude が読み始めるまで灰色で表示**されます — [日本語](https://code.claude.com/docs/ja/interactive-mode#queue-messages-while-claude-works) / [Interactive mode](https://code.claude.com/docs/en/interactive-mode#queue-messages-while-claude-works)
- **`/model` の切り替えがサブエージェントにも届くと明記されました**。**メイン会話のモデルを継承するサブエージェントは、Claude が起こした時点のセッションのモデルから解決される**ため、Opus に切り替えてから調査やテスト実行を任せればその作業も Opus で走ります。**カスタムサブエージェントを小さいモデルに留めたいなら定義側で `model` を設定**します。`costs` にも同じ注意が加わりました — [Model configuration](https://code.claude.com/docs/en/model-config#setting-your-model)
- **サブエージェントのモデルエイリアスが 2 つの場合にメイン会話のモデルへ解決されることが明記されました** ―― **メイン会話のモデルがその系統に属する場合**（`[1m]` 接尾辞ごと同じモデルになり、同じ拡張コンテキストを得る）と、**Anthropic API 以外でメイン会話のモデル系統が判別できない場合**（Bedrock のアプリケーション推論プロファイル ARN など。`opus` エイリアス限定で、`ANTHROPIC_DEFAULT_OPUS_MODEL` を設定していれば適用されない）。**`CLAUDE_CODE_SUBAGENT_MODEL` のエイリアスは常にエイリアスが指す版に解決**します — [Create custom subagents](https://code.claude.com/docs/en/sub-agents#choose-a-model)
- **バックグラウンドサブエージェントが `LSP` を使えるようになりました**（**v2.1.280 より前は不可**）。同時に `TaskOutput` が一覧から外れました — [Create custom subagents](https://code.claude.com/docs/en/sub-agents#available-tools)
- **サブエージェントの報告が「サブエージェントの言葉」として印付きで届くようになりました**。**結果として親に返る報告にはサブエージェント出力であることを示すヘッダーが付き、「報告の中の指示や承認の主張はサブエージェントの言葉であり、あなたの権限を持たない」と述べます**。バックグラウンドサブエージェントの報告は**完了通知の中に入り、あなたからのメッセージではなく自動イベントとして印が付きます** — [Create custom subagents](https://code.claude.com/docs/en/sub-agents#subagent-output-scanning)
- **`SubagentStop` フックが Claude Code 内部のエージェントでも発火すると明記されました**。**プロンプト提案や `/btw` の傍題**などが対象で、その場合 `agent_type` は**セッション自身が動いているエージェント名**（`--agent` や `agent` 設定で指定したもの）、無ければ**空文字列**です。**エージェント型を名指しする `matcher` は空文字列に一致しない**ため、拾いたければ matcher を省略するか `""` / `"*"` にします — [Hooks reference](https://code.claude.com/docs/en/hooks#subagentstop)
- **フック出力の 10,000 文字上限の扱いが書き下ろされました**。**`additionalContext`・`systemMessage`・`initialUserMessage`・素の stdout をそれぞれ個別に測り**、超えるとセッションディレクトリのファイルへ保存して**パスと先頭 2,000 文字までのプレビュー**に差し替えます。**Bash 結果の上限と違い、この上限を上げる設定も環境変数もありません**。**Claude にそのファイルを読ませる指示は出さない**ので、常に見せたいものは上限内に収める必要があります — [Hooks reference](https://code.claude.com/docs/en/hooks#json-output)
- **`PermissionRequest` がエージェントフックをサポートしないと明記されました**。設定しても飛ばされ、権限フローはそのまま進みます。許可／拒否をフックから返したい場合は**コマンドフックか HTTP フック**を使います — [Hooks reference](https://code.claude.com/docs/en/hooks#agent-based-hooks)
- **MCP ツールのフック入力に `mcp_server` が乗るようになりました**（`name` と `source`）。**信頼判断は `source` で行い、`name` や `mcp__<server>__` 接頭辞で判断するな**と明記されています。**v2.1.274 以降** — [Hooks reference](https://code.claude.com/docs/en/hooks#pretooluse-input)
- **worktree がメインチェックアウトと共有するものに「追跡されていないスキル・エージェント・コマンド」が加わりました**。**worktree のルートに `.claude/skills` が無ければ**（`.claude/skills` を gitignore している場合など）**メインチェックアウトのプロジェクトスキルを読みます**。`.claude/agents` と `.claude/commands` も同じ読み抜け。**スキルについては v2.1.277 以降** — [日本語](https://code.claude.com/docs/ja/worktrees#what-worktrees-share-with-the-main-checkout) / [Run parallel sessions with git worktrees](https://code.claude.com/docs/en/worktrees#what-worktrees-share-with-the-main-checkout)
- **worktree の後片付けがサブモジュールまで見るようになりました**（**v2.1.274 以降**）。**チェックアウト済みサブモジュールに変更や未追跡ファイルがある場合、またはサブモジュールを検査できない場合はプロンプトを出します**。**worktree の状態を数えられないときも自動削除せずプロンプト**を出し、**何を確認できなかったかをメッセージが名指し**します。作成を止める理由も 3 通りから 4 通りに増え、**`lfs.customtransfer.<name>.path` や `lfs.standalonetransferagent` のようにリポジトリの git 設定が外部プログラムを指している場合**が加わりました — [Run parallel sessions with git worktrees](https://code.claude.com/docs/en/worktrees#git-lfs-files-are-pointer-files-in-a-worktree-claude-code-created)
- **組織共有のクラウド環境の作り方が 2 通りになりました**。管理設定の **Cloud environments** ページで作るほかに、**自分の個人環境を環境セレクタの「Who can use it」行から共有**できます。**環境 ID が変わらないので、既に使っているセッションやルーティンに影響しません**。共有環境はセレクタで **Organization** 見出しの下に並び、**設定アイコンからは Owner を含む全員に読み取り専用の要約が出ます** — [日本語](https://code.claude.com/docs/ja/cloud-environments#organization-shared-environments) / [Configure cloud environments](https://code.claude.com/docs/en/cloud-environments#organization-shared-environments)
- **MCP の v2 ランタイムが feature flag を取得しないセッションでも既定になりました**（**v2.1.274 以降**）。Bedrock・Claude Platform on AWS・Agent Platform・Foundry、Claude apps gateway サインイン、テレメトリや feature flag 取得を切ったセッションが対象です。**プロトコル改訂 2026-07-28 の打診は HTTP サーバーには常に行い、claude.ai コネクタには feature flag を取得するセッションでのみ行う**ようになりました — [日本語](https://code.claude.com/docs/ja/mcp#mcp-client-runtimes) / [Connect Claude Code to tools via MCP](https://code.claude.com/docs/en/mcp#mcp-client-runtimes)
- **MCP サーバーが切断されて再接続を諦めたときに通知が出るようになりました**（`MCP server "<name>" disconnected · open /mcp to reconnect`）— [日本語](https://code.claude.com/docs/ja/mcp#automatic-reconnection) / [Connect Claude Code to tools via MCP](https://code.claude.com/docs/en/mcp#automatic-reconnection)
- **マッチしない `/` 名の扱いが対話ターミナル以外で変わりました**。**対話ターミナルでは従来どおり名前を報告**しますが、**それ以外のセッション（`-p` 実行・Agent SDK・デスクトップアプリの Code タブ・VS Code のチャットパネル・クラウドセッションとルーティン）ではプロンプトを普通のメッセージとして Claude に送り**、「コマンドは走らなかった」という注記と、そのセッションで走らせられるコマンドの一覧を添えます。**v2.1.274 より前はクラウドセッションとルーティンだけがこの挙動で、v2.1.273 より前はそれらも `Unknown command` を返していました** — [日本語](https://code.claude.com/docs/ja/errors#unknown-command) / [Errors and troubleshooting](https://code.claude.com/docs/en/errors#unknown-command)
- **圧縮の最後の手段が書き下ろされました**。**やり取りを 1 つも丸ごと要約できない場合、Claude Code は最新のプロンプトを一語一句残して残りを要約**し、**会話がプロンプトで終わっていない場合は会話全体を要約**します。**持ち越す内容にモデルの返答が無く、自分の文章も 1,000 トークン未満（巨大な貼り付けの後に送った短い再試行など）なら、この回復を飛ばします**。**v2.1.269 より前は、丸ごと要約できる時点が無いと毎ターン同じエラーに当たっていました** — [日本語](https://code.claude.com/docs/ja/errors#context-exceeds-the-token-limit) / [Errors and troubleshooting](https://code.claude.com/docs/en/errors#context-exceeds-the-token-limit)
- **クリティカルなメモリ使用量の警告が入りました**。**ヒープが 2.5GB を超えると警告が出て**、`claude --continue` で新しいプロセスに会話を引き継ぐか、フルスクリーン以外では `/compact` でも解放できると案内されます。**2.5GB を下回ると警告は消えます** — [Troubleshooting](https://code.claude.com/docs/en/troubleshooting#high-cpu-or-memory-usage)
- **`--max-budget-usd` が「その呼び出し自身の支出」だけを数えると明記されました**。**`--continue` / `--resume` で戻ったときに復元される過去の合計は上限に数えません**。逆に **`total_cost_usd` は復元ぶんを含む**ようになったため（**v2.1.277 以降**）、**セッションを再開した呼び出しの結果を足し合わせると二重計上**になります — [日本語](https://code.claude.com/docs/ja/agent-sdk/cost-tracking#accumulate-costs-across-multiple-calls) / [Track cost and usage](https://code.claude.com/docs/en/agent-sdk/cost-tracking#accumulate-costs-across-multiple-calls)
- **管理設定の MCP ロックが管理ソース横断で効くようになりました**（**v2.1.273 以降**）。**`allowManagedMcpServersOnly` はどの管理ソースの `true` でも効き**、ロック中の `allowedMcpServers` は**最上位の管理ソースが出したもの**になります。`deniedMcpServers` と `disableClaudeAiConnectors` も**どのソースのエントリ／`true` でも適用**されます。**`/status` と `claude doctor` が「効いていない値を出しているソースとキー」を名指し**するようになりました — [Managed settings](https://code.claude.com/docs/en/managed-settings#keys-read-from-every-admin-source)
- **不正な値でも落とさず厳しい側に倒す管理設定キーが 3 つ増えました**（**v2.1.277 以降**）。**`strictKnownMarketplaces`**（空の許可リストとして強制）、**`disableSideloadFlags`**（`true` として扱う）、**`syncClaudeAiPlugins`**（`false` として扱う）。**`blockedMarketplaces`** は**不正なエントリだけ剥がして有効な部分集合を強制**し、**丸ごと不正な値は落とす**（全マーケットプレイスを塞ぐと名指ししていないソースまで塞ぐため）という書き分けです — [Managed settings](https://code.claude.com/docs/en/managed-settings#keys-that-fail-closed)
- **`sandbox.excludedCommands` の効く条件が絞られました**。base は「常にサンドボックス外で走る」でしたが、head は **「呼び出しの中の全コマンドを覆っていて初めてサンドボックスから外れる」**ようになり、**それでもサンドボックスに留まる呼び出しの形が 5 つ列挙**されました ―― `sudo` / `eval` / `xargs` 始まり、位置を問わず `cd` / `pushd` / `popd` を含む、コマンド置換やサブシェルや `if` `for` などの制御構文、（`2>&1` のような複製以外の）リダイレクト、コマンド名が変数から来る場合。**`docker *` エントリだけでは `npm ci && docker build .` は外れず、`cd build && docker compose up` は `cd` エントリを足しても外れません** — [All settings](https://code.claude.com/docs/en/settings-reference#sandbox-excludedcommands)
- **`permissions.blockReadsOutsideWorkingDirectories` が auto memory にも及ぶようになりました**。**リポジトリ提供の設定ファイルが選んだ `autoMemoryDirectory` からは、そのディレクトリがどこにあっても auto memory を読まず、保存もしません** — [日本語](https://code.claude.com/docs/ja/memory#storage-location) / [How Claude remembers your project](https://code.claude.com/docs/en/memory#storage-location)
- **`attribution` の扱いに 1 行加わりました**。**あなた自身の指示（CLAUDE.md やメモリのルール）がコミット／PR の帰属行より優先されると Claude に伝える**ようになりました。ただし**管理設定で設定されている場合は除きます** — [All settings](https://code.claude.com/docs/en/settings-reference#attribution-commit)
- **`fastModePerSessionOptIn` が管理設定で設定されているとき、`/fast on` が対話ターミナル以外で拒否されるようになりました**（非対話モード・VS Code 拡張・クラウドセッション）。`fast-mode` の「fast mode をブロックする組織設定」は **2 つから 4 つ**に増えました — [日本語](https://code.claude.com/docs/ja/fast-mode#require-per-session-opt-in) / [Speed up responses with fast mode](https://code.claude.com/docs/en/fast-mode#require-per-session-opt-in)
- **ルーティンのアーティファクト再公開が条件付きで無確認になりました**。**編集可能・自組織所有・公開共有でない・最新版指定の共有でない・ページ単体の公開・ページ外へ届く権限を含まない**をすべて満たすときだけ確認を省きます。**新規公開は必ず確認**なので、「ページを最新に保つ」ルーティンには**既に公開済みのアーティファクトを渡せ**と案内されています。あわせて**GitHub 接続が切れているときは最大 72 時間スキップして待ち、それを過ぎるとルーティン自体がオフになる**、**サブスクリプション停止中はルーティンが保留される**という記述が加わりました — [日本語](https://code.claude.com/docs/ja/routines#create-a-routine) / [Automate work with routines](https://code.claude.com/docs/en/routines#create-a-routine)
- **ultrareview の比較起点にコミット ID とタグを渡せるようになりました**。**リポジトリの最初のコミット**も（起動ダイアログで確認すれば）全ファイルレビューの対象になり（**v2.1.277 以降**）、**`claude ultrareview` サブコマンドと `claude -p` は確認を伴わないので拒否**します。**Claude が Bash 経由でサブコマンドを走らせた場合も全リポジトリレビューは拒否**されます。投稿の結果も **Posted / Already posted / Failed** の 3 通りに書き分けられました — [Ultrareview](https://code.claude.com/docs/en/ultrareview#post-findings-to-the-pull-request)
- **セルフホストランナーが「読むだけのリポジトリ」のアクセス拒否でセッションを落とさなくなりました**（**v2.1.274 以降**）。**明確な拒否（見つからない・認証情報が無い・認証失敗）のときだけ飛ばし**、ネットワーク障害やタイムアウトや HTTP 403、**結果をプッシュする側のリポジトリの拒否では従来どおり失敗**します。**モデル呼び出しの 401 / 403 でトークンを取り直すようにもなり**、取得失敗時は**セッションが走る限り再試行し続ける**ようになりました — [Deploy self-hosted environments](https://code.claude.com/docs/en/self-hosted-environments-deploy#troubleshooting)
- **LLM ゲートウェイのロールアウトに「Claude Code の版上げを計画する」節が加わりました**。**ゲートウェイ設定を変えていなくても、開発者が版を上げるとデプロイ全体の挙動が変わりうる**という観点で、**feature flag の既定値・認識されないモデル ID に対する能力の仮定・既定モデルとエイリアスの解決先**の 3 領域と、それぞれを固定する設定が表になりました — [Roll out an LLM gateway for your organization](https://code.claude.com/docs/en/llm-gateway-rollout#plan-claude-code-version-upgrades)
- **ワークフローの `agent()` に渡したプロンプトが「あなたからの要求」として数えられなくなりました**。auto モードの分類器がそのサブエージェントの動作をレビューするとき、**Claude Code は「スクリプトが計算したテキスト」と印を付けます**。あわせて base にあった「分類器が `agent()` をブロックしうる」という記述はこの書き方に置き換わりました — [Dynamic workflows](https://code.claude.com/docs/en/workflows#let-claude-decide-with-ultracode)
- **Claude Desktop の表示モードに `Thinking` が加わりました**（ツール呼び出しは折りたたみつつ思考を出す）。**`Summary` モードは無くなり**、**1.46388.1 より前の版では一覧に残る**、**`Summary` のままのセッションは更新後 `Normal` で開く**と書かれました。**`Thinking` モードは Claude が思考を出したセッションでのみ一覧に出ます** — [Claude Code in the desktop app](https://code.claude.com/docs/en/desktop#switch-view-modes)
- **`Teams` プランの位置づけが変わりました**。`authentication` と `third-party-integrations` の両方で、**SSO とサーバー管理設定が Enterprise 専用から Teams にも含まれる**ものへ移りました — [Authentication](https://code.claude.com/docs/en/authentication#claude-for-teams-or-enterprise)
- **Anthropic Academy のリンクが `academy.claude.com` に移りました**（`overview`・`quickstart`・`admin-setup`・`communications-kit`）。**`Claude Code 101` と `Claude Code in Action` の 2 コースが名前で挙げられています** — [Claude Code overview](https://code.claude.com/docs/en/overview#next-steps)

**バグ修正**

- **v2.1.274〜v2.1.280 の修正項目 258 件のうち、本文ページに対応する記述を持つものはごく一部です**（大半は changelog にしか現れません）。対応が確認できたものを以下に挙げます。
- **`ANTHROPIC_BASE_URL` がプロキシまたはゲートウェイを指していると全リクエストが `400 … Input tag 'advisor_20260301'` で落ちる問題が修正されました**（v2.1.276・v2.1.275 の回帰）。**v2.1.275 では advisor をオフにしていてもリクエストに advisor ツールのエントリが乗っていた**ためで、その版に留まる場合は `CLAUDE_CODE_DISABLE_ADVISOR_TOOL=1` で外せます — [Connect Claude Code to an LLM gateway](https://code.claude.com/docs/en/llm-gateway-connect#troubleshoot-gateway-errors)
- **フルスクリーンモードの `ctrl+l` / `cmd+k` がトランスクリプト表示を消す挙動が差し戻されました**（v2.1.280・v2.1.260 で入ったもの）。**再び画面の再描画だけを行います**。iTerm2 と Terminal.app は `Cmd+K` を自分で処理して画面を消すので、**Claude Code はそれを検知して会話を描き直します** — [Fullscreen rendering](https://code.claude.com/docs/en/fullscreen#clear-the-conversation)
- **`~/.claude/skills/` に置いた `manifest.json` が、そこに列挙されたスキルフォルダを `.trash/` へ動かしてしまう問題が修正されました**（v2.1.280）。`skills` に「**個人スキルが消えた**」節が新設され、**タイムスタンプ付きフォルダから戻す手順**と、**retention sweep（既定 30 日）で消える前にやること**が書かれました — [Extend Claude with skills](https://code.claude.com/docs/en/skills#personal-skills-disappeared)
- **worktree セッションでメインリポジトリのプロジェクトスキルが読まれない問題が修正されました**（v2.1.277・`.claude/skills` が未追跡の場合）— [日本語](https://code.claude.com/docs/ja/worktrees#what-worktrees-share-with-the-main-checkout) / [Run parallel sessions with git worktrees](https://code.claude.com/docs/en/worktrees#what-worktrees-share-with-the-main-checkout)
- **macOS でプロンプトにドラッグしたスクリーンショットなど、誰も書き換えていないファイルの読み取りがシンボリックリンク検査で拒否される問題が修正されました**（v2.1.273 以降へ更新）。あわせて**書き込み拒否の種類が 2 つ増え**、`CLAUDE.md` が `AGENTS.md` へのシンボリックリンクである場合にリンク先を編集するよう促す例が入りました — [日本語](https://code.claude.com/docs/ja/errors#refusing-after-a-symlink-changed) / [Errors and troubleshooting](https://code.claude.com/docs/en/errors#refusing-after-a-symlink-changed)
- **Windows のネイティブビルドがターン直後に終了コード `4294967295` で落ちた際、VS Code 拡張がエラーを出していた問題が修正されました**（v2.1.273 以降）。**ターン境界でメッセージ待ちもバックグラウンドタスクも無ければ静かに閉じ**、次のメッセージで会話を再開します — [日本語](https://code.claude.com/docs/ja/errors#claude-code-process-exited-with-code-n) / [Errors and troubleshooting](https://code.claude.com/docs/en/errors#claude-code-process-exited-with-code-n)
- **`apiKeyHelper` の失敗が `/status` から見えるようになりました**（v2.1.274 以降）。**`apiKeyHelper` 行に `Failing` と直近の失敗の詳細（終了コードとエラー出力）が出て、次に成功すると消えます**。**v2.1.274 より前は認証情報のソースしか出ていませんでした** — [日本語](https://code.claude.com/docs/ja/errors#your-apikeyhelper-script-is-failing) / [Errors and troubleshooting](https://code.claude.com/docs/en/errors#your-apikeyhelper-script-is-failing)
- **保存済みトランスクリプトに読めないエントリがあると再開が失敗する問題が修正されました**（v2.1.275 以降）。**同じ失敗を繰り返す場合は `claude update` を実行してから再開する**よう案内が加わりました — [日本語](https://code.claude.com/docs/ja/errors#failed-to-resume-the-conversation) / [Errors and troubleshooting](https://code.claude.com/docs/en/errors#failed-to-resume-the-conversation)
- **フォークしたセッションにバックアップをコピーできなかった場合、そのチェックポイントへの巻き戻しが失敗しうると明記されました**（ディスクフルなど）— [日本語](https://code.claude.com/docs/ja/errors#no-files-were-restored) / [Errors and troubleshooting](https://code.claude.com/docs/en/errors#no-files-were-restored)
- **バックグラウンドシェルのメモリ圧迫による停止が「critical」に限定されました**。base は「メモリ圧迫のシグナル」、head は「**OS が critical なメモリ圧迫を報告し、かつセッションが 30 分アイドルで、ターンもサブエージェントも走っていない**とき」。**デバッグログに「なぜ止めたか／なぜ圧迫イベントで止めなかったか」が出る**ようになりました — [日本語](https://code.claude.com/docs/ja/interactive-mode#background-bash-commands) / [Interactive mode](https://code.claude.com/docs/en/interactive-mode#background-bash-commands)
- **`/btw` の傍題でツール呼び出しを文字として書いてしまった場合、応答の末尾に「何も実行されていない」という注記が付くようになりました** — [日本語](https://code.claude.com/docs/ja/interactive-mode#side-questions-with-btw) / [Interactive mode](https://code.claude.com/docs/en/interactive-mode#side-questions-with-btw)
- **クリップボードへのパイプが `excludedCommands` だけではサンドボックスから外れないと訂正されました**。`troubleshooting` の記述が「`pbcopy *` などを `excludedCommands` に足せばサンドボックス外で走る」から「**それだけではその呼び出しはサンドボックスから外れない**」に反転しています（上記 `sandbox.excludedCommands` の絞り込みと対応）— [Troubleshooting](https://code.claude.com/docs/en/troubleshooting#clipboard-commands-such-as-pbcopy-fail-inside-the-sandbox)
- **`plugin eval` の読み取り専用ツール一覧から `TaskOutput` が外れました**（削除に伴う追随）— [Evaluate plugin skills](https://code.claude.com/docs/en/plugin-evals#run-evals)
- **プラグイン関連性シグナルの `filesRead` と `manifestDeps` が、Claude Code 自身の設定ディレクトリと一時ディレクトリ配下のパスを除外するようになりました** — [Plugin relevance](https://code.claude.com/docs/en/plugin-relevance#relevance-signals)
- **Windows のインストールエラーの文言が更新されました**（`The token '&&' is not valid` → `The token '&&' is not a valid statement separator`）— [Troubleshoot installation](https://code.claude.com/docs/en/troubleshoot-install#wrong-install-command-on-windows)

**その他**

- **前回サマリが「見出しマップに載ったが本文に 1 回も現れない」として挙げた 4 件は、今回 4 件とも本文に着地しました** ―― `settings-reference` の **`syncClaudeAiPlugins`**（ハイライト 4 参照）、`agent-sdk/python` の **`SystemPromptCustom`**、`agent-sdk/modifying-system-prompts` の **`Update Claude's instructions mid-session`** と **`Turn recording off while you iterate on wording`**。**4 回連続で「予告から 1 回の取り込みで解消」**という流れが続いています（今回は 7 日ぶんの集約なので「翌日」とは言えません）
- **前回サマリが「changelog に載っただけ」として挙げた 5 つのゲートウェイヒントヘッダーも本文に着地しました**（大幅更新 5 参照）
- **`50 行以上動いたページのうち、軽微な更新へ回した 6 ページ**の内訳は次のとおりです。`cli-reference`（166 行だが**表のセル幅を揃え直したぶんを除くと実質 8 行**。`__SYSTEM_PROMPT_DYNAMIC_BOUNDARY__` と `--max-budget-usd` の 2 項目が実質）、`settings-reference`（138 行・Opus 5.5 と `syncClaudeAiPlugins` と `taskOutputMaxChars` 削除と `sandbox.excludedCommands` に分解される）、`keybindings`（72 行・実質 40 行。`chat:sendNow` の追加、`confirm:yes` / `confirm:no` の既定から `y` / `n` が外れたこと、`select:first` / `select:last` が `/model` ピッカーでも効くようになったこと）、`features-overview`（60 行・実質 22 行。出力スタイルを拡張機能の一覧・比較タブ・読み込み表に組み込んだ）、`managed-settings`（60 行・実質 26 行。上記 MCP ロックとフォールバックキー）、`env-vars`（52 行・上記の新変数群）
- **`confirm:yes` と `confirm:no` の既定バインドから `y` と `n` が外れました**（**v2.1.280 より前は既定**）。**ダイアログは「はい／いいえ」を訊いていない場面でもこの 2 アクションで確定・取り消しをするため、`y` のような裸の文字を割り当てると、その文字をキーとして表示していないダイアログにも効いてしまう**という理由が書かれています。**v2.1.280 より前に `/keybindings` でファイルを作った人のファイルには 2 行が残っており、消すまで効き続けます** — [Keybindings](https://code.claude.com/docs/en/keybindings#confirmation-actions)
- **`~/.claude/image-cache/` が現行版で使われなくなりました**（**v2.1.274 まで**が使用）。**貼り付け・添付した画像は `CLAUDE_CODE_TMPDIR` 配下のセッション別 `images/` ディレクトリへ**移り、**`claude project purge` では消えません**（retention sweep が `cleanupPeriodDays` 後に消す）— [The `.claude` directory](https://code.claude.com/docs/en/claude-directory#cleaned-up-automatically)
- **`~/.claude/skills/.trash/` と `~/.claude/plugins/.trash/` が retention sweep の対象に加わりました**。claude.ai 同期が外したスキル・プラグインの退避先で、**sweep が消すまでは戻せます** — [日本語](https://code.claude.com/docs/ja/claude-directory#cleaned-up-automatically) / [The `.claude` directory](https://code.claude.com/docs/en/claude-directory#cleaned-up-automatically)
- **アーティファクトが読み込める CDN が 4 ホストから 5 ホストへ増えました**（`unpkg.com` を追加）。`artifacts`・`desktop`・`network-config` の 3 ページで同じ表記が更新されています。あわせて **`/design` の必要バージョンが v2.1.234 から v2.1.265 へ改められ**、「研究プレビューのエディタを動かす」という書き方が「**Design アーティファクトとして公開する**」に、「保存が有効なアカウントでは」という条件が「**デスクトップブラウザで開いて編集すれば自動保存される**」に変わりました — [Share session output as artifacts](https://code.claude.com/docs/en/artifacts#allowlist-the-viewer-domain)
- **アーティファクトの可否が組織ポリシー由来であると明記されました**。**`api.anthropic.com` からポリシーを読めないとアーティファクトは使えず**、Claude が理由を述べます。**背景で再試行し続け、ポリシーが読めて許可されれば使えるようになります** — [Share session output as artifacts](https://code.claude.com/docs/en/artifacts#availability)
- **`network-config` の許可 URL 一覧に `github.com` が加わりました**（GitHub ホストのマーケットプレイスとプラグインのクローン用）— [Network configuration](https://code.claude.com/docs/en/network-config#network-access-requirements)
- **`accessibility` から「スクリーンリーダーモードには v2.1.181 以降が必要」という段落が消えました**（`settings-reference` の `axScreenReader` 側でも同じ 1 文が削除）。**バージョン注記の棚卸しが入ったと読めます**
- **`agent-teams` から「v2.1.178 時点の記述である」という Note が丸ごと消えました**。**`TeamCreate` / `TeamDelete` が存在しないこと、`team_name` が無視されることの説明ごと削除**され、代わりに**「稼働していない in-process チームメイトに Claude がメッセージを送ると、同じセッション内で復帰させて保存済みの会話を復元する」**という挙動が書き下ろされました。**セッション再開後は復帰させない**、**プロジェクトの `.claude/agents/` 由来の定義はフォルダを信頼していなければ再適用しない**（親フォルダの信頼は数えない）という条件つきです — [Orchestrate teams of Claude Code sessions](https://code.claude.com/docs/en/agent-teams#use-subagent-definitions-for-teammates)
- **`settings-example` の個人設定サンプルが `effortLevel` から `modelSettings` へ書き換わりました**（`"claude-sonnet-5": { "effortLevel": "xhigh" }`）。ハイライト 1 の「ユーザー設定のトップレベル `effortLevel` は新しいモデルに効かない」という変更に合わせたものと読めます
- **`v2.1.278` の変更項目がリンクしている `/docs/en/auto-mode-classifier-billing` は、`llms.txt` に収録されていません**。`llms-full.txt` 内で 3 回参照されているものの、**索引にも本文にも無いページ**です
- **Projects は changelog に 1 項目も現れません**。`claude-projects` ページと周辺 10 ページの導線だけが入っており、**CLI のリリースノートには出てこない claude.ai 側の機能**であることが読み取れます
- **見出しマップ先頭の自動生成スタンプが 2026年09月16日 19時54分20秒 UTC から 2026年09月23日 02時04分02秒 UTC へ**進みました。**約 6 日 6 時間ぶん**です
- **`llms.txt` の変更は 29 行（追加 15・削除 14）**で、内容のある変更は 4 か所だけです ―― `claude-projects` の 1 行追加、`memory` の説明に `or AGENTS.md files` を追記、`agents` の説明に `and projects` を追記、`output-styles` の説明の全面書き換え。**残る 11 行は言語別索引のページ数**（フランス語・ドイツ語・イタリア語・スペイン語・韓国語・中国語・繁体中国語・ロシア語・ブラジルポルトガル語の 9 言語が 192 → 197、**インドネシア語だけ 191 → 197**、**日本語は 192 → 196**）です
- **細かな言い換えが広く入っています**。`(e.g.,` → `(for example,`（`slack`・`statusline`・`plugins-reference`・`agent-sdk/user-input`・`agent-sdk/typescript`・`agent-sdk/python` など）、`or higher` → `or later`（`vs-code`・`self-hosted-environments-deploy`・`self-hosted-environments-reference`）、`newer` → `later`（同）。**変更が 2 行以下のページは 21 ページ**でした

**参考リンクについて**: **今回は日本語版の追従状況を、リンクする節ごとに実測し、その節が反映済みのものにだけ日本語リンクを付けました**（ページ全体の追従を保証するものではありません）。**節単位で追従を確認できたのは次の 14 ページの該当節**です ―― `memory`（`#agents-md` 一式）・`claude-projects`（全体）・`plugins-reference`（`#synced-plugins`）・`skills`（`#where-synced-skills-load`）・`output-styles`（全体）・`llm-gateway-protocol`（`#gateway-hint-headers`・`#response-headers`）・`claude-directory`（`#frontmatter-fields-by-file`）・`fast-mode`（Opus 5.5 対応と価格表）・`errors`（新設 17 節のうち `otelHeadersHelper failed` 以外）・`settings-reference`（`#syncclaudeaiplugins`・`#taskoutputmaxchars`）・`monitoring-usage`（`#managed-settings-resolved-event`・`#tool-output-span-event`）・`interactive-mode`（`#invisible-characters-in-prompts` ほか）・`glossary`（`#agents-md`・`#frontmatter`）・`claude-apps-gateway-deploy`（`#large-rollouts`・`#concurrent-upstream-requests`）。**同じページでも別の節（特に v2.1.280 ぶんの内容）は未反映または未確認のため、そちらは en 単独にしています** ―― 例えば `skills` の `#personal-skills-disappeared`（v2.1.280）は日本語版に存在せず、`plugins-reference` の `#user-configuration` と `settings-reference` の `#sandbox-excludedcommands` は未確認です。**ページ全体の未追従を確認したのは `model-config`（Opus 5 すら登場せず Opus 4.8 世代のまま）・`agent-sdk/typescript`・`vs-code`（v2.1.280 ぶんが未反映）・`plugin-marketplaces`（v2.1.280 の背景更新の変更が未反映。`--claudeai` の部分は反映済み）**の 4 ページで、これらは en 単独にしました。**上記以外のページは未確認のため、安全側に倒して en 単独にしています。changelog ページへのリンクは本サマリの方針どおり付けていません。**
<!-- light:minor-updates:end -->

## 新着情報

<!-- light:whats-new:start -->
*(今回の対象期間に新着情報（週間ダイジェスト）の更新はありません)*

**7 日ぶんを集約した断面ですが、`whats-new/` 配下のページは 1 行も動いていません。** `llms-full.txt` の差分に `whats-new` は 1 度も現れず、収録されている週間ダイジェストは **24 ページ（Week 13 から Week 37 まで、Week 31 は欠番）**のままです。**Week 38 は追加されていません。**
<!-- light:whats-new:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-09-16.md](./archives/latest/2026-09-16.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-09-16.md](./archives/latest-detail/2026-09-16.md)

<!--
base_commit: fa697d25e355bcd2486c2c9abb1263f94646b401
head_commit: 68860adc30f5a3b9e46aeef4cd6db8b1ccdc288e
generated_at_full: 2026-09-24T02:53:53+09:00
-->
