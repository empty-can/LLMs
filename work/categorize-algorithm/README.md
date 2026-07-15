# カテゴリ別サマリ生成の仕組み（ユーザーガイド）

公式ドキュメント更新サマリを「更新の性質」ではなく **「どの機能領域の話か」** で構造化し、読者が自分の業務に関係する差分の有無を数秒で判断できるようにする仕組み。本ディレクトリはその**検討・試作（PoC）一式**であり、まだ本番パイプライン（`.claude/skills/update-official-doc-summary/`）には組み込んでいない。

- 出自: `input/作業指示書.md`（Phase1 案出し → Phase2 手法決定 → Phase3 設計 → Phase4 実装 の 4 フェーズ）
- 現在地: **Phase2 の実証まで完了**。カテゴリ体系（taxonomy）と生成パイプラインの試作が動き、過去 10 日分の詳細版サマリを実データで生成済み

---

## 1. 何を解いているか

従来のサマリは `ハイライト / 新規追加 / 大幅更新 / 軽微な更新（新機能・機能改善・バグ修正・その他）/ 新着情報` という **更新の性質**でしか分類されていなかった。読者（開発チームの各メンバー）が知りたいのは「**自分が使っている機能に変更があったか**」なので、性質軸だけでは全項目を読むまで判断できない。

そこで:

1. Claude Code Docs 全体から「カテゴリとして使える語」を統計的に抽出し（→ §3）
2. 人がレビューして **13 カテゴリの taxonomy** を確定し（→ §4）
3. 日次の差分を機械で項目に分解し、LLM が意味的にカテゴリへ割り当て、カテゴリ別に並べた .md を生成する（→ §5）

出力サマリでは**ハイライトと新着情報のセクションを廃止**し、軽微なものも含む**全変更点をカテゴリの下に並列列挙**する。読者は自分のカテゴリだけを読み、「今回変更のなかったカテゴリ」の一行で無関係を即座に確認できる。

## 2. ディレクトリ構成

```
work/categorize-algorithm/
├── README.md                   # 本ファイル
├── input/
│   └── 作業指示書.md            # 依頼元（Phase1〜4 の定義）
├── scripts/
│   ├── term_scoring.py         # ① カテゴリ候補語のスコアリング（taxonomy 構築の材料を作る）
│   ├── categories.json         # ② 確定した taxonomy（13 カテゴリ＋語彙＋サブ区分）※単一の真実
│   ├── build_category_summary.py  # ③ サマリ生成パイプライン（prompt / extract / render）
│   ├── run-term-scoring.sh     # 🚀 ① のランチャー（人間が taxonomy 保守時に実行）
│   └── run-category-summary.sh # 🚀 ③ のランチャー（人間が手動でサマリ生成: prepare / render）
└── output/
    ├── phase1-proposals.md     # Phase1: サマライズ手法 11 案＋比較表
    ├── phase2-term-scoring-study.md  # Phase2: 手法サーベイ・スコアリング設計・実験結果
    ├── term-scores.md          # term_scoring.py の出力（候補語ランキング＋クラスタ素案）
    ├── trial-category-summary_2026-07-11.md      # 手動試作（1 日分・ライト版相当）
    ├── trial-category-summary-detail_2026-07-11/ # 試作生成した詳細版サマリ 10 日分
    │   └── 2026-07-01.md … 2026-07-11.md
    └── manual-runs/            # run-category-summary.sh の手動実行の作業場（gitignore）
```

**実行ランチャー（`.sh`）**: Python スクリプトを直接叩かなくても、人間が任意のタイミングで実行できるラッパー。`bash` から実行する。

| ランチャー | 何を起動するか | いつ人間が使うか |
|---|---|---|
| `run-term-scoring.sh` | `term_scoring.py` | taxonomy 保守（候補語の再計算）。§6-5 |
| `run-category-summary.sh` | `build_category_summary.py`（extract → prompt →〔Claude〕→ render） | 任意のコミット範囲のサマリを手動生成。§5 |

## 3. カテゴリ候補語のスコアリング（`term_scoring.py`）

taxonomy を人の勘だけで決めないための土台。`llms-full.txt` を入力に、**「どの文書にも属さず、複数の文書を束ねる語」**＝カテゴリ適性の高い語を統計的に上位へ集める。

一般的なキーワード抽出（TF-IDF 等）は「その文書に特有な語」を上げるため、そのままでは**逆選択**になる。そこで特化度をペナルティ側、横断性・共起ハブ性を報酬側に置いた合成スコアを使う。

```
score(t) = ( C-value × 被覆バンドパス × 分散均一度 × 共起中心性 )^(1/4)
           + ページ名加算(最大 +0.25)      # h1/slug に現れる語 = カテゴリの最有力候補
           + 見出し加算  (最大 +0.12)      # h2〜h4 に現れる語
           + 固有名詞加算(最大 +0.10)      # 文頭以外での大文字始まり率（Bedrock/GitHub 等）
           × 降格率                        # 一般名詞・コード構文トークンを減点
```

| 成分 | 役割 |
|---|---|
| C-value | 「mcp server」を「server」と別の句として立てる（複合語の termhood） |
| 被覆バンドパス | ページ被覆率 30% をピークに、特化語（1 ページ専用）と遍在語（弁別力ゼロ）の両方を減点 |
| 分散均一度（1 − Gries DP） | 高頻度でも一部ページに偏る語を減点 |
| 共起中心性（NPMI） | 多くの語と共起する＝多話題に接続するハブ概念を加点 |
| 構造加算（ページ名・見出し） | 公式がページ／見出しを立てている概念を**加算**で確実に浮上させる（乗算だと統計の弱い語が沈んだままになる） |
| 降格 | `json` `bash` `server` `team` 等の一般語・構文トークンを減点（除外ではなく降格し、レビューで目視可能に） |

動詞・動名詞は候補から除外している（`connect` `manage` `install` 等。ただし `plan`（plan mode）・`review`（code review）のような**動詞同形の機能名詞は保護**）。

**使い方**（外部パッケージ不要・Python 3 のみ）。ランチャー経由が簡単（引数はそのまま渡る。どこから実行してもよい）:

```bash
bash work/categorize-algorithm/scripts/run-term-scoring.sh \
  --top 100 --probe "environment variable" "permission" "hook"
```

Python を直接叩く場合はリポジトリルートから（既定の入出力がルート相対のため）:

```bash
python work/categorize-algorithm/scripts/term_scoring.py \
  --top 100 --probe "environment variable" "permission" "hook"
```

出力 `output/term-scores.md` には、①候補語ランキング（各スコア成分つき）②包含併合後のカテゴリ候補グループ（`mode ← permission mode, auto mode, plan mode` のように統合しスコア合算）③セクション共起によるクラスタ素案 が入る。**この出力を人がレビューして `categories.json` を確定する**（全自動でカテゴリを確定はしない）。

再計算のトリガーは docs の大改編時など不定期でよい。詳細な設計背景・実験結果は `output/phase2-term-scoring-study.md` を参照。

## 4. taxonomy（`categories.json`）

13 カテゴリ。**表示順が定義順**。

| # | カテゴリ | 備考 |
|---|---|---|
| 1 | ⌨️ コマンド | スラッシュコマンド・CLI・キー操作・対話モード |
| 2 | 🧰 拡張機能（プラグイン・スキル・フック） | |
| 3 | 🔐 パーミッション・セキュリティ | |
| 4 | 📚 セッション・コンテキスト | |
| 5 | 🤝 サブエージェント | エージェントチーム・agent view |
| 6 | 🔁 ワークフロー | タスク自動化・worktree・headless・スケジュール実行 |
| 7 | ⚙️ 設定・環境変数 | |
| 8 | 🖥 アプリ・プラットフォーム | デスクトップ/IDE/Web/OS/インストール |
| 9 | 🤖 モデル・利用状況 | モデル・トークン・コスト |
| 10 | 🔌 MCP・外部連携 | |
| 11 | 🧩 Agent SDK | TypeScript/Python SDK によるアプリ開発 |
| 12 | 🏢 エンタープライズ基盤 | **サブ区分あり**（下記） |
| 13 | 📝 ドキュメント改善 | **特別カテゴリ**（下記） |

**サブ区分**（メインカテゴリ内をさらに分ける仕組み。節内をこの順でグルーピングし、該当のない区分は非表示）。**任意のカテゴリに設定できる**（→ 追加手順は §6-3）。現在はエンタープライズ基盤のみが持つ:

> ベンダー非依存 / Anthropic のみ / サードパーティのみ（Anthropic 以外の共通話題）/ Bedrock・AWS / Foundry・Azure / Vertex・Google Cloud

**「ドキュメント改善」の特別ルール**: 文体統一・表記や名称の統一・書式調整・単なるリンク張替え・誤字修正など、**Claude Code の機能面の変更や仕様理解の実質的更新を伴わない差分**はここに**単独**分類する（他カテゴリと併記しない）。逆に、記述変更でも挙動の明確化や新情報の追加（仕様理解が変わる修正）は機能カテゴリへ入れる。

これにより「機能カテゴリに載っているものは機能面の変化がある」という意味論が保たれ、大規模な文体統一・名称改称の日でも機能カテゴリが汚染されない。実例として 2026-07-04（プロバイダ名一斉改称）は 150 項目が **3 エントリ**に収まり、うち機能カテゴリは 1 件だけになった。

**フィールドの役割**:

| フィールド | 使われ方 |
|---|---|
| `key` / `name` / `icon` | 識別子・見出し表示 |
| `prompt_hint` | **LLM プロンプトに載るカテゴリ説明**（`prompt` サブコマンドが自動で埋め込む） |
| `vocab` / `slug_prefixes` | **機械分類（参考値）用**。正の分類は LLM が行う（→ §5） |
| `subcategories` | サブ区分（任意） |

## 5. サマリ生成パイプライン（`build_category_summary.py`）

**設計方針**: 意味的解釈が要る工程だけを LLM に任せ、それ以外は決定的な機械処理にする（本リポジトリの既存パイプラインと同じ思想）。

```
                         categories.json（taxonomy = 単一の真実）
                                   │
              ┌────────────────────┴────────────────────┐
              │ prompt（機械: 指示文を自動生成）           │ 語彙・サブ区分・表示順
              ▼                                         ▼
[機械] extract              [LLM] 編集                     [機械] render
git diff (base..head)       各変更点を意味的に解釈し         entries JSON から
  ↓ ページ/セクション特定     ・カテゴリを 1〜3 個割当         カテゴリ別 .md を組立
  ↓ 変更点を項目に分解        ・サブ区分を付与                ・複数カテゴリへ展開
  ↓ 語彙マッチで機械分類       ・冗長項目を 1 エントリに統合    ・サブ区分で節内をグルーピング
  ↓  （＝参考値）             ・changelog をカテゴリ別に分割   ・「変更なしカテゴリ」を一行表示
  ↓                         ・内容ラベルと日本語要約を生成
items JSON  ──────────────→ entries JSON ─────────────────→ サマリ .md（＋分類根拠の付録）
```

### 5-1. extract（機械）

```bash
python work/categorize-algorithm/scripts/build_category_summary.py extract \
  --base <取り込みコミット> --head <次の取り込みコミット> \
  --out /path/to/items_YYYY-MM-DD.json
```

やっていること:
- `llms-full.txt` の diff hunk を、head 断面の `Source:` 行索引と突き合わせて **どのページ・どの h2 セクションの変更か**を特定
- 同一（ページ, セクション）の hunk をまとめて **1 項目**にする
- `llms.txt`（インデックス）の diff から**新規／削除ページ**を検出
- 追加行と削除行が空白差のみの項目に `cosmetic` フラグを立てる
- `categories.json` の語彙・slug 前方一致で**機械分類（参考値）**とマッチ語彙・スコアを付ける
- 各項目に LLM 用の diff 抜粋（`added_excerpt` / `removed_excerpt`）を同梱

### 5-2. LLM 編集（Opus）

**指示文（プロンプト）は `categories.json` から自動生成する**。手書きせず、必ずこのサブコマンドを使う（taxonomy を単一の真実にするため。§6-4）:

```bash
python work/categorize-algorithm/scripts/build_category_summary.py prompt \
  --items   /path/to/items_YYYY-MM-DD.json \
  --entries-out /path/to/entries_YYYY-MM-DD.json \
  --out     /path/to/prompt_YYYY-MM-DD.md
```

生成された指示文を Claude（Opus）に渡す（試作では sub-agent を日ごとに並列起動した）。LLM がやることは 6 つ:

1. **意味分類** — 変更内容を読んでカテゴリを 1〜3 個割当。機械分類は参考に留める。複数領域に本質的に関わる変更の**複数カテゴリ掲載はむしろ望ましい**（各カテゴリを単独で読んで完結させるため）
2. **サブ区分** — サブ区分を持つカテゴリ（§4・§6-3）に分類したエントリへ `subcategories` マップで区分を付与
3. **カテゴリ内統合** — 同一カテゴリ内で並べると冗長な項目（同趣旨の調整の繰り返し等）を 1 エントリに統合（`item_ids` を複数持たせる）。意味の異なる実質的変更は潰さない
4. **changelog のカテゴリ別分割**（統合の逆操作）— 下記
5. **内容ラベル** — 各エントリに「何が変わったか」を一言で表す日本語見出し（10〜20 字目安）。ページ名の直訳ではなく内容の要約
6. **要約** — 日本語 1〜3 文。「何がどう変わり、読者にとって何が変わるか」を書く

**changelog のカテゴリ別分割**: changelog・リリースノート・バージョン履歴表への追記のように、**1 つの変更が複数カテゴリの内容を単に束ねて記載しているだけ**の場合は、カテゴリごとに別エントリへ分割し、**各エントリの要約には当該カテゴリの内容だけ**を書く。

> 判断基準: 「1 つの話題が複数領域に波及している」なら**分割せず複数カテゴリ掲載**（同じ要約でよい）。「複数の独立した話題が 1 箇所にまとめて記載されている」なら**分割**する。

出力する entries JSON:

```json
{"entries": [
  {"item_ids": ["item04", "item05"],
   "categories": ["permission-security", "apps-platform"],
   "label": "read-only コマンドの承認不要化の明文化",
   "summary": "組み込みの読み取り専用シェルコマンド（`ls`・`cat` 等）が確認なしで実行される挙動が…"},

  {"item_ids": ["item12"],
   "categories": ["enterprise"],
   "subcategories": {"enterprise": "bedrock-aws"},
   "label": "…", "summary": "…"},

  {"item_ids": ["item48"], "categories": ["permission-security"],
   "label": "v2.1.200/201 更新ログ追加",
   "summary": "パーミッションモード「default」が「Manual」へ改称された。"},
  {"item_ids": ["item48"], "categories": ["session-context"],
   "label": "v2.1.200/201 更新ログ追加",
   "summary": "バックグラウンドセッションの各種修正が入った。"}
]}
```

**制約**: 全 `item_id` を**最低 1 つ**のエントリに含める（漏れ厳禁）。同一 `item_id` の複数エントリへの重複は、**changelog のカテゴリ別分割の場合に限り**許可（付録の「分割」列で識別できる）。

### 5-3. render（機械）

```bash
python work/categorize-algorithm/scripts/build_category_summary.py render \
  --items /path/to/items_YYYY-MM-DD.json \
  --entries /path/to/entries_YYYY-MM-DD.json \
  --out output/trial-category-summary-detail_.../YYYY-MM-DD.md
```

- エントリを `categories` の数だけ各カテゴリ節へ展開（複数カテゴリ掲載）
- エンタープライズ節はサブ区分でグルーピング
- 統合エントリは代表リンクを最大 3 件＋「ほか N 箇所」で表示
- 冒頭にカテゴリ分布の概要、末尾に**分類根拠の付録**（LLM 分類 vs 機械分類の対比表）
- エントリに含まれない項目があれば機械分類で**自動補完**する安全網つき（LLM の取りこぼし対策）

`--entries` の代わりに `--summaries`（`{item_id: 要約文}` の単純形式）も受け付ける。この場合は機械分類がそのまま使われ、統合・複数カテゴリ掲載は行われない（v1 互換）。

### 5-4. ランチャー（人間が手動で 1 回まわす）

`run-category-summary.sh` が上記 3 工程のパスの受け渡しを肩代わりする。中間の LLM 編集だけは Claude の担当なので、**prepare（extract + prompt）→〔Claude が entries を書く〕→ render** の 2 段に分かれる:

```bash
# 1. 差分を項目化し、LLM 指示文を生成（BASE..HEAD は取り込みコミット）
bash work/categorize-algorithm/scripts/run-category-summary.sh prepare b0e62bd 7acfb2c
#    → output/manual-runs/<HEAD 短縮 SHA>/ に items.json と prompt.md を生成

# 2. prompt.md を Claude に渡す（サブエージェント、または claude -p）。
#    Claude が items.json を読み、同じフォルダに entries.json を書く。

# 3. entries.json からサマリ .md を組み立てる
bash work/categorize-algorithm/scripts/run-category-summary.sh render 7acfb2c
#    → 同フォルダに summary.md
```

中間ファイルは `output/manual-runs/<ラベル>/`（gitignore）に置かれる。ラベル既定値は HEAD の短縮 SHA。

## 6. 人間が行う作業とメンテナンス

スクリプトの実行を除けば、人間の担当は **taxonomy（`categories.json`）の設計と保守**にほぼ集約される。以下は「何を、いつ、どうやるか」。

### 6-1. `categories.json` は直接編集してよい（それが正規の手順）

**スクリプトが `categories.json` を書き換えることはない。** `term_scoring.py` が出力するのは `output/term-scores.md`（＝人が読むための候補材料）だけで、taxonomy そのものは生成しない。`build_category_summary.py` は `categories.json` を**読むだけ**である。

> 設計上の境界: **機械が候補を出す → 人が確定する**。その確定結果を置く場所が `categories.json` であり、手編集が前提。再計算で上書きされる心配はない。

### 6-2. カテゴリの追加・削除・並べ替え

`categories.json` の `categories` 配列を編集する。**配列の順序がそのまま出力順**になる（並べ替えは要素を移動するだけ）。

1 カテゴリのフィールド:

| フィールド | 必須 | 内容 |
|---|---|---|
| `key` | ✅ | 一意な識別子（LLM が返す値。英小文字ケバブ） |
| `name` | ✅ | 見出しに出る日本語名 |
| `icon` | ✅ | 見出し先頭の絵文字 |
| `vocab` | ✅ | 機械分類（参考値）用のマッチ語彙。**空配列 `[]` でもよい**（実際「ドキュメント改善」は空） |
| `slug_prefixes` | ✅ | 機械分類用の slug 前方一致規則。同じく空でよい |
| `subcategories` | 任意 | サブ区分（§6-3） |

`vocab` / `slug_prefixes` は付録の「機械分類（参考値）」列に効くだけで、**正の分類には影響しない**（正の分類は LLM）。カテゴリを増やすだけなら空配列で始めて構わない。

### 6-3. サブカテゴリの追加（どのカテゴリでも可）

**任意のメインカテゴリにサブ区分を設けられる**（エンタープライズ基盤に限らない）。手順は 1 つだけ:

`categories.json` の対象カテゴリに `subcategories`（`key` / `name` の配列）を足す。

```json
{
  "key": "extensions",
  "name": "拡張機能（プラグイン・スキル・フック）",
  "prompt_hint": "拡張機能: プラグイン・スキル・フック",
  "icon": "🧰",
  "vocab": [ ... ],
  "slug_prefixes": [ ... ],
  "subcategories": [
    {"key": "plugin", "name": "プラグイン"},
    {"key": "skill",  "name": "スキル"},
    {"key": "hook",   "name": "フック"}
  ]
}
```

これだけで:

- **レンダラー**がその節をサブ区分ごとにグルーピングする（配列順が表示順。該当エントリのない区分は非表示。未指定・不正値のエントリは先頭区分に落ちる）
- **LLM プロンプト**（`prompt` サブコマンドが生成）に当該カテゴリのサブ区分一覧が自動で載り、LLM が `subcategories` マップで区分を付与するようになる

エントリ側の指定形式は **`"subcategories": {"<カテゴリ key>": "<サブ区分 key>"}`** のマップ。複数のサブ区分持ちカテゴリに分類された場合は、各カテゴリ分をマップに並べる。

```json
{"item_ids": ["item12"],
 "categories": ["enterprise", "extensions"],
 "subcategories": {"enterprise": "bedrock-aws", "extensions": "plugin"},
 "label": "…", "summary": "…"}
```

> 旧形式の `"enterprise_sub": "bedrock-aws"` も後方互換で読める（過去の entries JSON を再レンダリングできるようにするため）。新規に書くときはマップ形式を使う。

### 6-4. taxonomy を編集したら LLM プロンプトを再生成する

カテゴリ一覧は `categories.json` を**単一の真実**とし、LLM 編集工程の指示文は `prompt` サブコマンドで**そこから自動生成**する（§5-2）。プロンプトを手書き・手修正しないこと。

```bash
python work/categorize-algorithm/scripts/build_category_summary.py prompt \
  --items <items JSON> --entries-out <entries JSON> --out <prompt.md>
```

`categories.json` を編集したら、**生成し直したプロンプトで LLM 編集をやり直す**。プロンプトを再生成せずに古い指示文を使うと、次のように**エラーにならず静かに壊れる**:

| ずれの方向 | 起きること |
|---|---|
| taxonomy に追加したが、LLM が古い一覧しか知らない | **そのカテゴリは永久に 0 件**（見出しすら出ない） |
| LLM が taxonomy に無い `key` を返した | レンダラーが黙って捨て、カテゴリが空になれば**「未分類」送り** |

> レンダラーの該当ロジック: `e["categories"] = [c for c in e["categories"] if c in cats] or [unc_key]`

編集後は 1 日分を再生成し、付録の「LLM 分類」列に新カテゴリが実際に現れるか、未分類が急増していないかを目視で確認するとよい。

なお `prompt_hint`（LLM に渡すカテゴリ説明）も `categories.json` のフィールドである。カテゴリの意味を調整したいときは、プロンプトではなくここを直す。

### 6-5. 定例メンテナンス

| タイミング | 作業 | 目安 |
|---|---|---|
| **公式 docs の大改編後**（新カテゴリ級の概念が登場した、ページ構成が大きく変わった） | `term_scoring.py` を再実行し、`term-scores.md` の上位語・併合グループを眺めて taxonomy に追加すべき概念がないか確認 | 不定期。四半期ごと程度の点検でも足りる |
| **「未分類」が増えてきたと感じたとき** | 生成物の「❓ 未分類」節と付録を見て、未分類に落ちた項目に共通する概念があればカテゴリまたは `vocab` を追加 | 随時 |
| **チームの関心が変わったとき**（新しい機能を使い始めた／使わなくなった） | カテゴリの粒度・並び順を見直す。よく見るカテゴリを上に、関心の薄いものを下に | 随時。**メンバープロファイルは持たない設計なので、追従はこの並べ替えで行う** |
| **カテゴリ内が冗長・肥大化してきたとき** | サブカテゴリを設ける（§6-3）か、カテゴリを分割する | 随時 |

### 6-6. 人間が「やらなくてよい」こと

- **メンバーごとの購読設定・プロファイル管理** — 意図的に持たない設計。読者はカテゴリ見出しを見て自分で取捨選択する
- **個々の変更点の分類** — LLM の担当（機械分類は参考値として付録に出るのみ）
- **カテゴリ候補語の手作業での洗い出し** — `term_scoring.py` が候補とクラスタ素案まで出す。人はそれを承認・命名するだけ

## 7. 試作結果（2026-07-01 〜 07-11 の 10 日分）

`output/trial-category-summary-detail_2026-07-11/` に格納。実データ 596 項目 → 263 エントリ。

| 日 | 項目 → エントリ | 特徴 |
|---|---|---|
| 07-03 | 193 → 92 | v2.1.195 リリース＋文体統一の大規模改稿日 |
| 07-04 | **150 → 3** | プロバイダ名一斉改称。ドキュメント改善へ集約され、機能カテゴリは 1 件のみ |
| 07-09 | 78 → 51 | 実質的変更が多くカテゴリが広く分散 |
| 07-11 | 10 → 5 | read-only パーミッション記述の 4 ページ横断見直しが 1 エントリに統合 |

**機械分類だけの精度**（LLM を使わない場合の参考値）: 未分類率 **1.0%（6/596）**。語彙マッチだけでも大半は正しく当たるが、「ページの所在」ではなく「内容」で判断すべきケース（例: ロールアウト用資料に書かれたパーミッション仕様の変更）は LLM の意味解釈が要る。

## 8. 既知の限界

- **taxonomy は人手確定が前提**: スコアリングは候補を出すところまで。品詞情報のない純統計では一般語の混入が残るため、最終確定は人（または LLM 補助＋人の承認）が行う
- **プロンプト再生成の忘れ**: taxonomy を編集してもプロンプトを再生成しなければ古い指示文が使われ、**エラーにならず静かに壊れる**（§6-4）。生成は `prompt` サブコマンドに一本化してあるが、実行忘れ自体は防げない（本番組込み時はラッパーで強制する）
- **語形のゆれ**: `sandbox` / `sandboxing` のような派生形は簡易レンマ化では統合されない
- **接頭辞規則の誤併合**: `pre+view` により `preview → view` のような誤りが出る。機械併合はあくまで種
- **新概念への追従**: docs に新カテゴリ相当の概念が現れた直後は語彙が無く「未分類」に落ちる。`term_scoring.py` の再計算で追従する
- **本番未組込**: 既存パイプラインのテンプレート契約（`light:*` マーカー、`## N.` 見出しが ja 追従 watch の錨、`derive_light.py`、Phase 3 レビューア）とは未接続。正式採用時は Phase3 で設計する

## 9. 関連ドキュメント

- `input/作業指示書.md` — 依頼元
- `output/phase1-proposals.md` — サマライズ手法 11 案と比較（本方式＝A1 グルーピング系を採用）
- `output/phase2-term-scoring-study.md` — 手法サーベイ、スコアリング設計の根拠、実験結果（v1→v3 の変遷）
- `output/term-scores.md` — 候補語ランキング（`term_scoring.py` の最新出力）
- `.claude/skills/update-official-doc-summary/` — 現行の本番サマリ生成 Skill（接続先）
