---
name: update-official-doc-summary
description: official-llms-txts 配下の公式ドキュメント (llms.txt / llms-full.txt) の更新差分を、人間向けの changelog / リリースノート風 Markdown として生成する。対象サイトは --site で切り替える (claude-code-docs / mcp)。詳細版を LLM で生成し、ライト版は固定スクリプトで詳細版から機械的に抽出する。
allowed-tools: Read, Write, Edit, Grep, Bash(git diff:*), Bash(git log:*), Bash(git show:*), Bash(git rev-parse:*), Bash(mkdir -p:*), Bash(mv:*), Bash(git checkout:*), Bash(git clean:*), Bash(python:*), Bash(echo:*), Agent(doc-summary-reviewer)
argument-hint: "[--site <slug>] [--from <commit>] [--automated]"
disable-model-invocation: true
---

## 引数パース

- `--site <slug>`: 対象サイト。省略時は `claude-code-docs`(後方互換)。有効値は「サイト設定テーブル」の `slug` 列。値を `SITE` とする
- `--from <commit>`: 初版作成時の起点コミット。省略時は前回サマリの末尾フッタから `head_commit` を取得し `BASE_COMMIT` とする。前回サマリが無く `--from` も無ければエラー終了
- `--automated`: 無人（ヘッドレス/パイプライン）実行を示すフラグ。**本フラグがあれば `AUTOMATED=1`、無ければ `AUTOMATED=0`** とする（手順 13 の Phase 3 要否判定で使用）。ラッパー `run-doc-summary.ps1` が自動付与する。手動・対話起動では付けない

## サイト設定テーブル

`SITE`(`--site`)で以下を決定する。`<INPUT_BASE>` 配下に `llms.txt` / `llms-full.txt` がある前提。

| slug | `<INPUT_BASE>` | 出力slug | URL言語併記 | 新着情報カテゴリ | docs_map | テンプレート |
|---|---|---|---|---|---|---|
| `claude-code-docs` | `official-llms-txts/code.claude.com/docs/` | `claude-code-docs` | あり(ja/en) | あり | あり | `detail.md.tmpl` |
| `mcp` | `official-llms-txts/modelcontextprotocol.io/` | `mcp` | なし | なし | なし | `detail.mcp.md.tmpl` |

## 固定パス

サイト設定テーブルの選択行に基づき以下を決定する:

- `SUMMARY_DIR` = `official-doc-update-summary/<出力slug>/`
- `LATEST_DETAIL` = `${SUMMARY_DIR}latest-detail.md`
- `LATEST_LIGHT` = `${SUMMARY_DIR}latest.md`
- `ARCHIVES_DIR` = `${SUMMARY_DIR}archives/`
- `TEMPLATE` = `.claude/skills/update-official-doc-summary/templates/<テンプレート>`
- `DERIVE_SCRIPT` = `.claude/skills/update-official-doc-summary/scripts/derive_light.py`
- `INPUT_LLMS_TXT` = `<INPUT_BASE>llms.txt`
- `INPUT_LLMS_FULL` = `<INPUT_BASE>llms-full.txt`
- `INPUT_DOCS_MAP` = docs_map=あり のとき `<INPUT_BASE>en/claude_code_docs_map.md`。docs_map=なし のとき使用しない

## 主要処理

### 1. 前回サマリ参照と BASE_COMMIT 決定

Read tool で `$LATEST_DETAIL` を読み込む。

**BASE_COMMIT の決定**(引数 `--from` を最優先):

- 引数 `--from <commit>` がある場合: `BASE_COMMIT = <commit>`(既存ファイルの有無に関係なく優先)
- 引数 `--from` がない場合:
  - `$LATEST_DETAIL` が存在する: 末尾の HTML コメント `<!-- ... head_commit: <hash> ... -->` から `BASE_COMMIT` を抽出
  - 存在しない: 標準エラーに `初版作成には --from <commit> 指定が必要です` を出力して終了

**PREV_GENERATED_AT / ARCHIVE_NAME の決定**(アーカイブフォルダ名で使用):

- `$LATEST_DETAIL` が存在する: frontmatter から `作成日` を抽出して `PREV_GENERATED_AT` とする(= 前回サマリの作成日 = 前回対象期間の最終日。**起点日ではなく最終日を使う**)。あわせて末尾フッタ `generated_at_full` の時刻を `HHMM`(4 桁・24h) として抽出し `PREV_GENERATED_TIME` とする
- 存在しない: `PREV_GENERATED_AT` は空(手順 10 の旧版アーカイブをスキップ)
- **`ARCHIVE_NAME` の決定**(アーカイブのファイル名(拡張子なし)。手順 10 の退避先と手順 6 の `{{PREV_GENERATED_AT}}` の双方で使う):
  - 既定は `ARCHIVE_NAME = <PREV_GENERATED_AT>`
  - ただし `${ARCHIVES_DIR}latest-detail/<PREV_GENERATED_AT>.md` が **既に存在する** 場合(= 同一作成日のサマリが既にアーカイブ済み = 同日に複数回生成)は、そのまま退避すると既存アーカイブを上書き消失させるため、`ARCHIVE_NAME = <PREV_GENERATED_AT>_<PREV_GENERATED_TIME>`(例: `2026-06-02_1125`) とする

> `--from` 指定時に既存ファイルが存在しても、その既存ファイルは手順 10 で `${ARCHIVES_DIR}<ARCHIVE_NAME>/` へ通常通り退避される。`--from` は **新たな BASE_COMMIT を明示する** だけで、既存サマリの扱いは変えない。

### 2. HEAD_COMMIT 取得と差分検出

Bash で実行:
```
git rev-parse HEAD
```
結果を `HEAD_COMMIT` とする。

Bash で実行:
```
git diff <BASE_COMMIT> <HEAD_COMMIT> -- <INPUT_BASE>
```
出力が空なら標準出力に `差分なし、処理停止` を出して終了 (exit 0)。
非空ならその内容を `DIFF_CONTENT` とする。

> **scratch ファイルの置き場所**: 差分照合等で一時ファイルが必要な場合でも、`official-llms-txts/` や `official-doc-update-summary/` 配下には**書き込まない**(誤って `git add` で混入する)。`git diff` / `git show` の出力は直接変数・パイプで扱い、どうしてもファイルが要るなら gitignore 済みの `work/` 配下に置く。Windows 絶対パス(`C:\...`)を bash のリダイレクト先に渡すと名前が壊れた scratch が cwd に残るので避ける。

### 3. 入力ドキュメント読み込み

Read tool で以下を読む:
- `$INPUT_LLMS_TXT` (URL リスト・1 行説明)
- `$INPUT_LLMS_FULL` (全文展開) — 大ファイルなので、Grep tool で必要セクションだけ抽出する形でもよい
- `$INPUT_DOCS_MAP` (ページ見出しマップ) — docs_map=あり のサイトのみ。docs_map=なし のサイトでは読まない

### 4. ページ分類

`DIFF_CONTENT` を解析し、各変更ページを以下のいずれかに分類:

| カテゴリ | 判定条件 |
|---|---|
| 新規追加 | リファレンス系で完全に新規追加されたページ (URL パスに `whats-new/` を含まない、`+` のみ) |
| 大幅更新 | リファレンス系で既存ページ本文に 50 行以上の変更 |
| 軽微更新 | リファレンス系で上記以外の小規模変更 |
| 新着情報 | URL パスに `/whats-new/` を含むページ (新規追加・更新を問わずすべてこのカテゴリ)。**新着情報カテゴリ=なし のサイトでは本カテゴリを使わず、3 カテゴリ(新規追加/大幅更新/軽微更新)に分類する** |

> 新着情報 (`whats-new/...`) はリリースノート的性質を持ち、リファレンス・ガイドの新規ページとはインパクトが異なるため、別カテゴリとして扱う。新着情報カテゴリ=なし のサイト(例: `mcp`)では `whats-new/` 相当のページが存在しないため、`{{WHATS_NEW_*}}` placeholder と `## 新着情報` セクションを持たないテンプレートを使う。

### 5. 詳細版テンプレート読み込み

Read tool で `$TEMPLATE` を読み込む。

### 6. 詳細版生成 (英語)

テンプレートの各 placeholder を以下で埋める。出力先は一時的に変数として保持 (まだファイル書き出しはしない):

| Placeholder | 内容 |
|---|---|
| `{{PERIOD}}` | **PT 基準の対象期間**。`BASE_COMMIT`・`HEAD_COMMIT` の各コミット日付 (`git log -1 --format=%cs <commit>`) を取得し、**それぞれ 1 日前**にした日付を使う(後述「日付基準(PT -1日ルール)」参照) |
| `{{GENERATED_AT}}` | **作成日**。`GENERATED_AT_FULL` の日付の **1 日前**(= 実行日(JST)の前日, PT 基準。`YYYY-MM-DD`)(後述「日付基準」参照) |
| `{{OVERALL_SUMMARY_INTRO}}` | 全体要約の冒頭 1〜2 文(英語、項目数の言及程度) |
| `{{OVERALL_SUMMARY_BULLETS}}` | 主要項目の番号付き箇条書き(後述の選定ルール参照) |
| `{{HIGHLIGHT_BULLETS}}` | 主要 3〜5 件のハイライト bullet(英語、内部リンク付き、後述フォーマット厳守) |
| `{{HIGHLIGHT_DETAILS}}` | 各ハイライトに対応する `## <タイトル>` 見出し + 1〜2 段落 + 末尾の ja/en ページリンク(後述フォーマット厳守) |
| `{{NEW_PAGES_BULLETS}}` | 新規追加ページ bullet(英語、URL は ja/en 併記、内部リンク付き) |
| `{{NEW_PAGES_DETAILS}}` | 各新規ページの `## <タイトル>` 見出し + 2〜3 段落 + 末尾の ja/en ページリンク |
| `{{UPDATED_PAGES_BULLETS}}` | 大幅更新ページ bullet(英語、URL は ja/en 併記、内部リンク付き) |
| `{{UPDATED_PAGES_DETAILS}}` | 各更新ページの `## <タイトル>` 見出し + 1〜2 段落 + 末尾の ja/en ページリンク |
| `{{MINOR_UPDATES}}` | 軽微更新ページ bullet(英語、URL は ja/en 併記、bold title 無し) |
| `{{WHATS_NEW_BULLETS}}` | 新着情報ページ bullet(英語、URL は ja/en 併記、内部リンク付き)。**日付は日本語表記** |
| `{{WHATS_NEW_DETAILS}}` | 各新着情報ページの `## <タイトル>` 見出し + 1〜2 段落 + 末尾の ja/en ページリンク |
| `{{BASE_COMMIT}}` | 手順 1 で決定した値 |
| `{{HEAD_COMMIT}}` | 手順 2 で取得した値 |
| `{{GENERATED_AT_FULL}}` | **実際の生成時刻** (`YYYY-MM-DDTHH:MM:SS+09:00`、JST 実時刻)。**-1 日しない**(機械的 provenance は偽らない)。よって `作成日` はこの日付より 1 日前になる |
| `{{PREV_GENERATED_AT}}` | アーカイブのファイル名(拡張子なし) `<ARCHIVE_NAME>`(手順 1 で決定。通常は前回サマリの作成日、同日衝突時は `_<HHMM>` 付き)。関連リンクのパス `./archives/latest/<値>.md` ・ `./archives/latest-detail/<値>.md` に入る(初版時は `(none)` 等の placeholder、関連リンクは手動編集で削除) |

URL 併記ルール(サイト依存):
- URL言語併記=あり のサイト: en URL の `/docs/en/` を `/docs/ja/` に機械的置換して ja URL とし、ja/en を併記する
- URL言語併記=なし のサイト(例: `mcp`): 言語サブパスが無いため **単一 URL** を使う(`.md` 除去のみ)。bullet・末尾リンクの `([日本語](url-ja) / [English](url-en))` 形式は使わず、単一リンクにする。`{{WHATS_NEW_*}}` placeholder はテンプレートに存在しないためスキップする

#### 日付基準(PT -1日ルール)

本パイプラインは **JST 15:00** に実行され、これは常に太平洋時間(PT)の前日夜(PDT 前日 23:00 / PST 前日 22:00)にあたる。取得した公式ドキュメントの内容は「PT で前日まで」の断面なので、レポートの**表示日付は PT 基準(= 実行日(JST)の前日)に揃える**。JST 15:00 実行なら DST に関わらずオフセットは常に **-1 日固定**。

- **対象期間 `{{PERIOD}}`**: `BASE_COMMIT` / `HEAD_COMMIT` の各コミット日付を 1 日前にする
- **作成日 `{{GENERATED_AT}}`**: 実行日(JST)の前日(= `GENERATED_AT_FULL` の日付の前日)
- **`{{GENERATED_AT_FULL}}`**: 実時刻(JST, +09:00)のまま **-1 日しない**。よって `作成日` は `generated_at_full` の日付より 1 日前になる(意図的な差。整合チェックもこの前提)

日付計算は `date` コマンドが allowed-tools に無いため **python** で行う:
- 現在時刻(generated_at_full): `python -c "import datetime;print(datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S+09:00'))"`
- 日付の前日: `python -c "import datetime,sys;print((datetime.date.fromisoformat(sys.argv[1])-datetime.timedelta(days=1)).isoformat())" <YYYY-MM-DD>`

> **移行境界(2026-06-08 実行分から適用)**: 2026-06-07 までの claude-code-docs / mcp サマリは旧ルール(JST 当日基準・-1 なし)で作成済み。本 PT -1日ルールは **2026-06-08 実行分以降**に適用する。境界では前回サマリの対象期間末尾(旧=JST 当日)と今回の対象期間先頭(新=PT 前日)が 1 日重なる場合があるが、ルール変更の継ぎ目として許容する。

#### `{{OVERALL_SUMMARY_BULLETS}}` の選定ルール

- **ハイライトと同集合**: 概要は `{{HIGHLIGHT_BULLETS}}` で取り上げた項目**のみ**を、同じ順序で 1 行要約する。**追加候補は入れない**(軽微更新・新着情報の "Other wins" 等は概要に出さず、各カテゴリのセクション本文で扱う)
- **件数**: 必ずハイライトと**同数**(`概要件数 == ハイライト件数`)。これにより「概要件数 ≤ ハイライト件数」を保証する(読み手が概要とハイライトの件数差を不審に思うのを防ぐ)。`derive_light.py` も概要件数 > ハイライト件数 を検出するとエラー終了する
- **新着情報のみの差分で主要機能が乏しい場合**: 新着情報ページ本文の "主要機能" からハイライトを構成し、概要もそのハイライトと同集合にする
- **形式**: 各行を `> 1. <項目>` 〜 `> N. <項目>` の番号付き箇条書きで blockquote 内に記述。番号・順序はハイライト(`1.`〜`N.`)と一致させる

#### bullet フォーマット(厳守)

ライト版抽出スクリプト `derive_light.py` が、`(#anchor)` 形式の内部リンクを `(./latest-detail.md#anchor)` の外部リンクに自動変換する。詳細版時点では **bullet 内見出しを内部リンクで書く**。

**ハイライトのみ番号付き箇条書き**(`1.` 始まり、対応する h2 番号と一致させる)。他カテゴリは `-` の通常箇条書き。

| placeholder | bullet 形式(改行は半角スペース 2 個 + 改行を意味する) |
|---|---|
| `{{HIGHLIGHT_BULLETS}}` | `N. [**<機能タイトル>**](#<anchor>):  ⏎`<br>`  <要約>` |
| `{{NEW_PAGES_BULLETS}}` | `- [**<ページタイトル>**](#<anchor>) ([日本語](url-ja) / [English](url-en)):  ⏎`<br>`  <要約>` |
| `{{UPDATED_PAGES_BULLETS}}` | `- [**<ページタイトル>**](#<anchor>) ([日本語](url-ja) / [English](url-en)):  ⏎`<br>`  <要約>` |
| `{{WHATS_NEW_BULLETS}}` | `- [**2026年MM月DD日～EE日(Week N)**](#<anchor>) ([日本語](url-ja) / [English](url-en)):  ⏎`<br>`  <要約>` |
| `{{MINOR_UPDATES}}` | `- [日本語](url-ja) / [English](url-en):  ⏎`<br>`  <要約>` (bold 無し、詳細セクション無しのため anchor 化なし)。**通常ページが無い変更(changelog のみ)はリンクを置かず `- <要約>` のみ**(changelog ページの URL は使わない) |

`<anchor>` は対応する `## <番号と本体>` 見出しから GFM 規則(小文字化・スペース→ハイフン・非英数字非ハイフン除去、Unicode 保持)で生成。**h2 が番号付き(`## 1. <title>`)の場合、anchor も番号を含む**(例: `#1-claude-opus-48-リリース`)。

> **軽微更新で 1 ページが複数リリースを含む場合(重要)**: changelog のように 1 ページへ複数のリリースエントリ(例: `v2.1.166`・`v2.1.167`・`v2.1.168`)が追加されたときは、ページ単位 1 bullet に潰さず**リリース単位にネスト分割**する。トップ bullet をページリンク(+ リリース数・日付の一言)にし、その下に `  - **<バージョン>**: <要約>` をリリースごとに置く。各リリース配下の個別の変更項目は、**読点(、)で連結した長大な 1 文にせず、1 項目 1 bullet**(`    - <変更>`)で列挙する。ハイライトに昇格済みの項目はリリース要約行で「ハイライト参照」と示し、配下の個別 bullet では再掲しない。リリース本文が「Bug fixes and reliability improvements」等の汎用文のみのときはその 1 行で可。

#### h2 見出しの番号付け規約

固定 category 見出し(以下)は**番号なし**:

- `## ハイライト`
- `## 新規追加されたページ`
- `## 大幅に更新されたページ`
- `## 軽微な更新`
- `## 新着情報`
- `## 関連リンク`

それ以外の個別テーマ h2 は **`## N. <タイトル>`** 形式で番号付け:

| カテゴリ | 番号付け対象 h2 | 番号採番 |
|---|---|---|
| ハイライト配下 | 各機能 h2 | 1, 2, 3...(カテゴリ内で 1 から) |
| 新規追加されたページ配下 | 各ページ h2 | 1, 2, 3...(カテゴリ内で 1 から) |
| 大幅に更新されたページ配下 | 各ページ h2 | 1, 2, 3...(カテゴリ内で 1 から) |
| 新着情報配下 | 各週間ダイジェスト h2 | **番号なし**(日付表記で識別可能なため) |

#### 日付表記の規約

- 共通: ファイル内に登場する全ての年月日表現は **日本語表記**(例: `2026年05月18日`)
- 週間ダイジェスト(`whats-new/2026-wXX`): `2026年MM月DD日～EE日(Week N)`(`Week N` は英語のまま、対応する日本語表現がないため例外)

#### 各テーマセクションの末尾フォーマット(`{{HIGHLIGHT_DETAILS}}` / `{{NEW_PAGES_DETAILS}}` / `{{UPDATED_PAGES_DETAILS}}` / `{{WHATS_NEW_DETAILS}}`)

各 `## N. <タイトル>` セクションの本文の最後に、以下の形式でページリンクを記載(**「参考リンク:」の見出しは付けない**、リンク行を直接置く):

```
- [<日本語タイトル> - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/<path>)
- [<English title> - Claude Code Docs (English)](https://code.claude.com/docs/en/<path>)
```

- リンク先タイトルは `$INPUT_LLMS_TXT` の各エントリ `[<Title>](<URL>): <Description>` から取得した `<Title>` を使う。日本語タイトルは LLM が `<Title>` を翻訳する
- **両 URL とも `.md` 拡張子を付けない**(`.md` 付き URL は raw ファイルが表示されるため、人間向けには拡張子なし URL が正しい)。`$INPUT_LLMS_TXT` の URL は `.md` 付きなので、`.md` を除去した上で記載する
- ja URL は en URL の `/docs/en/` を `/docs/ja/` に機械的置換し、かつ `.md` 拡張子を除去したもの

ハイライトテーマ(機能単位)では、その機能を主に解説しているページの URL を 1〜2 ページ分記載。

> **changelog ページへのリンクは原則しない(重要)**: `changelog` ページ(`/docs/<lang>/changelog`)は巨大で閲覧性が低いため、末尾参考リンク・bullet いずれにも **changelog ページの URL を置かない**。changelog でしか確認できない変更(新機能・修正)であっても、対応する**通常ドキュメントページに記載(修正加筆)があるか**を `$INPUT_LLMS_FULL` で確認し、**該当ページがあればその ja/en をリンク**、**無ければリンクを省略する**(changelog の URL で代替しない)。changelog ページ自体の更新(タイトル改称・リリースエントリ追加)を述べる軽微更新 bullet も、リンクを付けずテキストのみとする。

#### 新着情報ページ独自情報の検出(セルフレビュー観点)

`/whats-new/<page>.md` の本文と、`$INPUT_LLMS_FULL` 内の対応ページ展開を比較し、**新着情報ページにしか記載されていない内容があれば** `{{WHATS_NEW_DETAILS}}` の該当セクションに反映する。両者に差がなければ通常通り要約する。

### 7. Phase 1 セルフレビュー (英語段階)

以下を順次確認し、NG があれば該当箇所を Edit tool で修正する。新規 NG が出なくなるまで反復:

- [ ] リンク実在性: 末尾参考リンクの全 URL の `.md` 除去前形(en パスに対応する `.md` 付き URL)が `$INPUT_LLMS_TXT` 内に実在する
- [ ] URL 拡張子: 末尾参考リンクの ja URL / en URL いずれにも `.md` が付いていない
- [ ] changelog リンク不使用: 末尾参考リンク・bullet に changelog ページ(`/docs/<lang>/changelog`)の URL が無い。changelog 由来の変更は対応する通常ページがあればそれを、無ければリンク省略(changelog の URL で代替しない)
- [ ] 本文整合性: ハイライト・大幅更新の記述が `$INPUT_LLMS_FULL` の対応ページ本文と矛盾しない
- [ ] 網羅性: `DIFF_CONTENT` で検出された全ページが新規 / 大幅更新 / 軽微更新 / 新着情報のいずれかに分類されている
- [ ] カテゴリ整合性: `whats-new/` ページは全て新着情報カテゴリに分類されている
- [ ] 構成・展開: 概要 → 詳細の順、1 セクションが極端に短い・長いがない、用語が一貫
- [ ] h2 番号整合性: ハイライト / 新規追加 / 大幅更新 配下の個別テーマ h2 に `## N. <title>` 形式で番号が付与されている。新着情報配下と固定 category 見出しには番号がない
- [ ] ハイライト bullet 番号整合性: `{{HIGHLIGHT_BULLETS}}` が `N.` 始まりの番号付き箇条書きになっていて、対応する `## N.` 見出しと番号が一致
- [ ] 概要・ハイライト件数整合性: `{{OVERALL_SUMMARY_BULLETS}}` の項目数が `{{HIGHLIGHT_BULLETS}}` と**一致**し、各項目がハイライトの同順の項目に対応している(`概要件数 ≤ ハイライト件数` の保証。超過していると `derive_light.py` がエラー終了する)
- [ ] 内部リンク整合性: bullet 内の `(#anchor)` が対応する `## N. <タイトル>` の GFM アンカー(番号含む)と一致する
- [ ] 末尾参考リンクのテキスト: `[<タイトル> - Claude Code Docs (日本語 or English)]` 形式で空タイトルなし
- [ ] 新着情報ページ独自情報: `whats-new/` ページに `$INPUT_LLMS_FULL` の同セクションには無い内容がある場合、それも反映済み
- [ ] メタデータ整合性(PT -1日ルール): frontmatter の `対象期間` は `base_commit` / `head_commit` の各コミット日付の **前日**、`作成日` は `generated_at_full` の日付の **前日**。末尾フッタの `base_commit` / `head_commit` は実 hash、`generated_at_full` は実時刻(JST, -1 しない)
- [ ] 日付表記: 全ての年月日が日本語表記(`YYYY年MM月DD日`、ただし `Week N` は例外で英語のまま)

### 8. 日本語化

英語版の本文 (frontmatter と末尾フッタ HTML コメント以外) を日本語に翻訳する。Edit tool で各セクションを翻訳。

### 9. Phase 2 セルフレビュー (日本語化後)

- [ ] 自然な日本語: 直訳的・不自然な表現がない (必要に応じて `$INPUT_LLMS_FULL` を再参照して再翻訳可)
- [ ] 誤訳: 英語サマリと日本語訳の意味が一致
- [ ] 誤字・脱字: 文字レベルの誤りなし

新規 NG が出なくなるまで反復。

### 10. 旧版アーカイブ (前回サマリが存在する場合のみ)

`ARCHIVE_NAME` は手順 1 で決定済み(通常は `<PREV_GENERATED_AT>`、同日衝突時は `<PREV_GENERATED_AT>_<PREV_GENERATED_TIME>`)。アーカイブはライト版・詳細版を**種別ごとのフォルダ**に日付名ファイルとして退避する(`archives/latest/<日付>.md` / `archives/latest-detail/<日付>.md`。過去回を辿る際に日付フォルダを個別に開かずに種別ごとに一覧できる構成)。Bash で実行:
```
mkdir -p ${ARCHIVES_DIR}latest/ ${ARCHIVES_DIR}latest-detail/
mv ${LATEST_LIGHT} ${ARCHIVES_DIR}latest/<ARCHIVE_NAME>.md
mv ${LATEST_DETAIL} ${ARCHIVES_DIR}latest-detail/<ARCHIVE_NAME>.md
```

> 手順 6 の `{{PREV_GENERATED_AT}}` placeholder(関連リンクのパス)にも同じ `<ARCHIVE_NAME>` を使い、アーカイブ実体(`archives/latest/<ARCHIVE_NAME>.md` / `archives/latest-detail/<ARCHIVE_NAME>.md`)とリンク先を一致させる。

### 11. 詳細版書き出し

Write tool で手順 6〜9 の最終結果を `$LATEST_DETAIL` に書き出す。**手順 10 の旧版アーカイブを必ず先に済ませること**（先に `$LATEST_DETAIL` を上書きすると旧版が失われ、アーカイブのため `git show HEAD:` からの復元が必要になる）。

### 12. ライト版生成

Bash で実行:
```
python ${DERIVE_SCRIPT} ${LATEST_DETAIL}
```

スクリプトは `$LATEST_DETAIL` を読み、`$LATEST_LIGHT` を生成する。
終了コードが非ゼロならエラー内容を標準エラーに出力して終了。

### 13. Phase 3 第三者レビュー (doc-summary-reviewer)

執筆 Agent 自身では気づけない確信的誤り(ハルシネーション)とフォーマット規約違反を、別 Agent で多層検出する。

#### 実行要否の判定

`AUTOMATED` は冒頭「引数パース」で決定済み（`--automated` 引数があれば `1`、無ければ `0`）。ツール実行は不要。

- `AUTOMATED` が `1` (無人・ヘッドレス/パイプライン実行): 本 Phase は**必須**。スキップ不可
- `AUTOMATED` が `0` (手動・対話実行): 本 Phase は**任意**。ユーザーから明示指示がある場合のみ実行し、無ければ手順 14 へ進む

> 理由: ハルシネーションは執筆者が確信的に書くため Phase 1/2 セルフレビューでは捕捉できない。人が成果物を見ない無人実行時のみ機械レビューを必須化する。

#### レビューループ (最大 3 回)

カウンタ `N=1` から開始し、以下を反復:

1. Agent tool で `doc-summary-reviewer` (subagent_type) を起動。プロンプトに以下を渡す:
   - `SITE` / `INPUT_BASE` / `BASE_COMMIT` / `HEAD_COMMIT` / `LATEST_DETAIL` / `LATEST_LIGHT`
   - `URL_LANG`: URL言語併記=あり のサイトは `あり`、なし のサイトは `なし`
2. reviewer 出力から `判定:` で始まる行を探し、`判定: PASS` または `判定: FAIL` を解釈する（reviewer は 1 行目に置く規約）
3. `判定: PASS` の場合: ループを抜けて手順 14 へ
4. `判定: FAIL` の場合:
   - 各 `[CRITICAL]` / `[IMPORTANT]` 指摘の修正案を Edit tool で `$LATEST_DETAIL` に反映する (`[SUGGESTION]` は任意反映)
   - Bash で `python ${DERIVE_SCRIPT} ${LATEST_DETAIL}` を再実行し `$LATEST_LIGHT` を再生成する
   - `N` を +1 してループ先頭へ戻る
5. `N` が 3 を超えても `判定: FAIL` の場合 (打ち切り):
   - `AUTOMATED` が `1`: 残存指摘を標準エラーに出力する。さらに、レビュー FAIL の生成物が commit・push されるのを**決定論的に防ぐ**ため、Bash で当該サイトの生成物を HEAD 状態へ戻す:
     ```
     git checkout -- ${SUMMARY_DIR}
     git clean -fd ${SUMMARY_DIR}
     ```
     これで `${SUMMARY_DIR}` の追跡ファイルは HEAD に戻り、手順 10 で退避した未追跡コピーも除去されるため、ラッパーの add 対象に差分が残らず push されない (`claude -p` の終了コード挙動に依存せず push を抑止できる)。
   - `AUTOMATED` が `1` 以外: 残存指摘をユーザーに提示し判断を仰ぐ (手順 14 の完了報告は行わない。生成物は破棄せず人手判断に委ねる)

### 14. 完了報告

以下の情報を含む完了メッセージを出力:
- 生成パス: `$LATEST_LIGHT` / `$LATEST_DETAIL`
- 旧版アーカイブ先 (該当する場合): `${ARCHIVES_DIR}latest/<ARCHIVE_NAME>.md` ・ `${ARCHIVES_DIR}latest-detail/<ARCHIVE_NAME>.md`
- 統計: ハイライト件数 / 新規追加件数 / 大幅更新件数 / 軽微更新件数 / 新着情報件数
- 期間: `<BASE_COMMIT short> .. <HEAD_COMMIT short>` (各 7 桁)
- Phase 3 結果: 実行した場合は `判定: PASS` (N 回目で合格) / スキップした場合は `Phase 3: スキップ (手動実行)`
