# .claude/CLAUDE.md

このファイルは、本リポジトリ（`LLMs`）で Claude Code が**メンテナーとして**作業する際のガイドである。`.claude/` 配下のファイルを読み書きするときに自動ロードされる。利用者向けの概要はルート `README.md` を参照。

> **状態**: `cc-relative-info` から公式ドキュメント更新サマリ・パイプラインを移設して正式運用する移行の途上。本ガイドは移行完了後の運用前提で記述する。移行設計は `cc-relative-info` の `LLMs/work/publish-migration/migration-plan.md` 参照。

## CLAUDE.md 配置原則（本リポジトリ設計の根拠・最重要）

本リポジトリは「llms.txt 系成果物の**公開リポジトリ**」であり、成果物の**消費者**（人間／自律参照する Claude／自動投入パイプライン）が `official-llms-txts/` `official-doc-update-summary/` を読む。この前提から、メンテナー向け文書が消費者のコンテキストを汚染しないよう、CLAUDE.md の配置を以下に固定する。

| 配置 | 採否 | 理由 |
|---|---|---|
| ルート `CLAUDE.md` | **置かない** | セッション開始時に無条件 auto-load される。`claude -p`（cwd=B のパイプライン）にも、B を clone した消費者がルートでセッションを開いた場合にも、ブランチ運用・スケジューラ等のメンテナー文脈が混入する |
| `.claude/CLAUDE.md`（本ファイル） | **ここに集約** | `.claude/` 配下のファイル読み書き時のみロード＝**メンテナー作業時に限定**。消費者は `.claude/` を読まないため汚染されない |
| content dir（`official-llms-txts/` 等）の `CLAUDE.md` | **置かない** | nested CLAUDE.md は当該 dir 配下のファイルを読むと auto-load される。**消費者 Claude はまさにこの dir の llms.txt を読む**ため、CLAUDE.md を置くと確実に汚染する。特に同居非メンテナー（手元にファイルがある利用形態）で誤取り込みの害が大きい |
| content dir のナビ（人間向け索引） | **`README.md` を使う** | README.md は auto-load されない。消費者 Claude が llms.txt を読んでも巻き込まれず、人間／メンテナーは明示的に開いて読める |

> この原則は `cc-relative-info` の `LLMs/work/user-review/`（想定利用者・ユースケース整理）の成果物が設計インプット。7 シナリオ全てで「**利用者としての Claude には CLAUDE.md を読ませない**」と判定された（`_workspace/agent-c-synthesis.md`）。唯一の例外は Scenario 3 / 7 の**人間**利用者が What-is 理解のためルート README を読むケースのみで、これは README で充足する。

## このリポジトリの性質

`llms.txt` 系成果物の**公開リポジトリ**であり、かつ**自走するパイプラインを内包**する（B 自己完結方式）。`origin = https://github.com/empty-can/LLMs.git`。

- **コンテンツ**: `official-llms-txts/`（取り込んだ公式 llms.txt）と `official-doc-update-summary/`（生成した更新サマリ）。
- **パイプライン**: `.claude/` 配下に Skill / Agent / 設定、`.claude/scripts/` に取得・生成・運用スクリプトを置く。
- 翻訳・要約という「Claude の判断」が要る部分のみ Skill 経由で `claude -p` が担い、それ以外は全てスクリプト化されている。

## ブランチ運用ルール

| ブランチ | 役割 |
|---|---|
| `main` | 公開済みコンテンツ（人手レビュー済み）。**公開 = `main` への反映** |
| `bot/doc-summary` | bot（無人パイプライン）の未確定生成の push 先 |

- 無人パイプラインは `bot/doc-summary` にのみ push する（`main` へ直接 push しない）。
- 公開は **人手レビュー後に `bot/doc-summary` → `main` へマージ**して行う。
- 異常系（生成失敗で push 抑止 / レビュー打ち切り等）で `bot/doc-summary` に残る未マージコミットは、SessionStart の `notify-bot-branch.sh` が検出して通知する。

## タグ運用ルール

**タグは「アンカー保全」のためだけに使う。** 本リポジトリにリリースの概念は無く、semver 等のバージョンタグは打たない。

### 目的

外部の文書が本リポジトリの特定断面（commit）を出典として引用したとき、その commit を**ブランチの消滅・付け替えから独立して到達可能に保つ**ため。タグが無いと、引用先の commit が特定のブランチにしか無い場合、そのブランチの削除・rebase・squash で参照が壊れる。

### 命名

`anchor/<取り込み日 YYYY-MM-DD>`

- 同日に複数回の取り込みがあり両方にアンカーが要る場合のみ `-2` `-3` を付す（実例: 2026-06-21 は `fd2ef0a` と `1a7d39c` の 2 回取り込みがある）。
- **どの文書が引用しているかはタグ名に入れない**。同じ断面を複数の文書が引用しうるため。依存関係は注釈メッセージ側に記録する。
- `anchor` という名前のタグは作らない（`anchor/...` と ref パスが衝突して両立できない）。

### 作成条件

**外部文書が本リポジトリの commit を出典として引用したときだけ**作成する。定期取り込みのたびに打つものではない。

### 🚫 リモートへの push 厳禁（最重要）

**anchor タグはローカル限定で運用する。`origin` へ push してはならない。**

本リポジトリは成果物の**消費者が clone する公開リポジトリ**であり、タグは GitHub の Tags / Releases UI に露出する。リリースの概念が無いリポジトリにリリースらしき見た目のタグが並ぶのは、消費者にとって明確なノイズになる（ルート `CLAUDE.md` を置かない方針と同じ理由 ―― 消費者の視界にメンテナー都合の情報を出さない）。

したがって以下を禁止する。

- `git push origin <tag>` / `git push --tags` / `git push --follow-tags` / `git push --mirror`
- `push.followTags = true` の設定

> **⚠ この制約で失うもの・失わないもの**（2026-09-05 実測）
>
> タグは ref なので、**タグが指す commit は到達可能とみなされ `gc` の刈り取り対象にならない**。隔離リポジトリでの実測では、対象 commit を**どのブランチからも外し・rebase を実施し・`reflog expire --expire-unreachable=now` ＋ `gc --prune=now` を実行**しても、タグ経由で内容を完全に取り出せた。対照としてタグを削除してから同じ `gc` を回すと、その commit は消滅した ―― **タグだけが生存要因**である。
>
> したがってローカル限定でも、**この clone が存在する限りアンカーの内容は保全される**。仮にリモートの `bot/doc-summary` が削除・書き換えされても、手元の clone は完全な記録として残り、必要なら push し直せる。
>
> **失うのは「リモート単独での自己完結性」**である。他者が clone してもタグは付いてこないため、リモートだけを見た場合はブランチ履歴上に在る commit しか辿れない。よってアンカーは次の 3 つで支える。
>
> 1. 当該 commit が `origin/main` または `origin/bot/doc-summary` の履歴上に在ること（リモート側の担保）
> 2. **`main` への反映を必ず merge で行う**という下記の禁止事項（リモート履歴を書き換えない）
> 3. **ローカルの `anchor/*` タグを単独判断で削除しないこと**（手元の clone を最後の砦として維持する。文書側の更新と対で整理する場合の手順は下記）
>
> **`anchor/2026-06-06`（BASE-A）は `origin/main` 到達可能なので 1 で堅い。`anchor/2026-06-21`・`anchor/2026-08-19`（BASE-C・BASE-B）は `origin/bot/doc-summary` にしか無く、同ブランチが `main` に合流するまでは 2 と 3 が頼り**である点に注意する。

### 作成手順

必ず**注釈タグ**（`-a`）で作成する。push はしない（上記）。

```bash
git tag -a anchor/<YYYY-MM-DD> <commit> -F <メッセージファイル>
```

注釈メッセージは、下記「現行の anchor タグ」表の該当行を指す 1 行で足りる（タグは push されず消えうるため、**依存関係の詳細は表側に書く**。表が正本）。表には次を必ず記載する。

| 項目 | 記載例 |
|---|---|
| 何の断面か | 公式ドキュメント定期取り込み（CLI v2.1.235 相当・84,016 行） |
| 引用元の文書 | `empty-can/cc-relative-info` の `claude-dir-sharing-governance/reports/01.配布・統制方針調査/結論・構成案_ポータブルな.claude共有_v1.2.md` |
| 依存している出典 | 出典 `[76]`〜`[97]`（同文書での呼称 BASE-B） |
| 対象ファイルと blob | `official-llms-txts/code.claude.com/docs/llms-full.txt` = `f6f26436…` |

### 禁止事項

#### 🚫 単独でのタグ削除は厳禁（許されるのはアンカー更新作業の一部としてのみ）

**「不要そうだから」「掃除のため」といった単独判断での削除を禁止する。** 理由は上記の実測結果にある ―― **タグは、それが指す commit を履歴書き換え（rebase・ブランチ削除・`gc --prune=now`）から守る要因**であり、削除した瞬間にその commit は刈り取り対象へ落ちうる。また「もう誰も引用していない」という推測は誤りうる（引用元は本リポジトリの外にあり、増えることもある）。

**一方、引用元文書のアンカーを更新する作業の一部としてタグを整理することは、正当な保守であり許可する。** アンカーはタグと文書の対で成立するので、文書側だけ更新してタグを残すと表と実体が食い違っていく。

##### 削除してよい条件（全て満たすこと・順序も守る）

1. **引用元の文書側で、当該断面への参照が全て解消されていること**（別断面への再アンカー、または該当記述ごとの削除）。推測ではなく、文書を実際に確認する
2. **その文書側の変更が、引用元リポジトリで commit 済みかつ push 済みであること**（差し戻せる状態を作ってから進める）
3. **削除前に、当該 commit がブランチから到達可能かを確認すること**

   ```bash
   git branch -a --contains <commit>
   ```

   - **到達可能**: タグを消しても commit は残る（低リスク）
   - **どのブランチからも到達不能**: **タグを消すと commit は失われる**。この場合は削除せず、下記「削除済みアンカー」へ移すに留める
4. **下記「現行の anchor タグ」表から該当行を外し、「削除済みアンカー」へ移して commit すること**。commit ハッシュ・blob・いつ・なぜ外したか・文書側の対応 commit を必ず残す（**記録を消してはならない。将来その断面に戻る必要が生じたときの唯一の手がかりになる**）
5. **表の更新を commit した後で**タグを削除する（順序を逆にしない）

   ```bash
   git tag -d anchor/<YYYY-MM-DD>
   ```
6. **到達性検証の `EXPECTED` を新しい本数に更新する**

##### 削除済みアンカー

過去にアンカーとして使い、文書側の更新に伴って外したもの。**この記録は削除しない。**

| タグ（削除済み） | commit | blob | 外した日 | 理由・文書側の対応 |
|---|---|---|---|---|
| （なし） | | | | |

#### その他の禁止事項

- **既存の anchor タグを移動しない**（`-f` での付け替え）。引用先が変わり、引用元文書の行番号が無効になる。
- **anchor タグが指す commit を含むブランチを rebase / squash / filter しない**。`main` への反映は必ず **merge**（fast-forward または `--no-ff`）で行う。

### 到達性の検証

`main` へのマージ前後、および履歴に触れる操作の後に実行する。

```bash
# 1. タグが消えていないか（削除は厳禁。本数は「現行の anchor タグ」表と一致すること）
EXPECTED=3
n=$(git tag -l 'anchor/*' | wc -l)
[ "$n" -eq "$EXPECTED" ] || { echo "anchor タグ本数が不正: ${n}（期待 ${EXPECTED}）"; exit 1; }

# 2. 各タグが現在の履歴から到達可能か
for t in $(git tag -l 'anchor/*'); do
  git merge-base --is-ancestor "$t" HEAD || { echo "到達不能: $t"; exit 1; }
done
```

> **本数チェックを省略しないこと。** タグを消してしまった場合、到達性ループは対象ゼロで素通りし「異常なし」に見えてしまう。アンカーを追加したら `EXPECTED` も更新する。
>
> 将来 `bot/doc-summary` → `main` の合流をスクリプト化する際は、この 2 つを合流スクリプトの事前チェックとして組み込む。

### 強制力の限界

**タグを push しないため、GitHub の ruleset による `anchor/**` 保護は成立しない。** 本ルールに git 側の強制機構は無く、遵守は文書上の取り決めに依存する。

ただし**タグが存在する限り、ローカルでは git の仕組みそのものが commit を守る**（上記実測）。つまり注意を払うべき点は「タグが意図せず消えていないか」の一点に集約される ―― **残ってさえいれば、rebase や `gc` に対する保護は git が自動的に効かせてくれる**。

その一点を機械的に検知するのが下記の到達性検証であり、これを `main` 合流の手順に組み込むことが最も費用対効果の高い担保になる（タグが消えていれば検証ループが `git tag -l` で 0 本を返すため、**タグ本数の期待値チェックも併せて行う**）。**手順どおりにアンカーを整理して減らした場合は `EXPECTED` を更新すること**。更新を忘れた検知は「意図しない削除」と区別がつかないので、表・`EXPECTED`・タグの 3 つを常に揃える。

### 現行の anchor タグ（**この表が正本**）

タグを push しない以上、**clone しただけではタグは存在しない**。したがって**この表がアンカーの正本**であり、タグは各 clone で表から再生成するローカルの実体である。**アンカーを追加・変更したら必ずこの表を更新して commit すること。**

**新しい clone を作ったら、まず下記を実行してタグを再作成する。**

```bash
git tag -a anchor/2026-06-06 980975cf497b0cce6847425a0787fccd839be1ae -m "BASE-A: cc-relative-info v1.2 出典 [1]-[75] の基準"
git tag -a anchor/2026-06-21 1a7d39cab3539583157847db90f343550a8fe42e -m "BASE-C: cc-relative-info v1.2 出典 [75] の版境界の基準"
git tag -a anchor/2026-08-19 32e6ee3566896a4f0a120a5c98b667aea98b22c6 -m "BASE-B: cc-relative-info v1.2 出典 [76]-[97] の基準"
```

いずれも `empty-can/cc-relative-info` の `claude-dir-sharing-governance/reports/01.配布・統制方針調査/結論・構成案_ポータブルな.claude共有_v1.2.md` が引用元。同文書はこれらを BASE-A / BASE-B / BASE-C と呼ぶ。

対象ファイルはいずれも `official-llms-txts/code.claude.com/docs/llms-full.txt`。

| タグ | commit | 断面 | 対象ファイルの blob | 依存している出典 |
|---|---|---|---|---|
| `anchor/2026-06-06` | `980975cf497b0cce6847425a0787fccd839be1ae` | 正式運用リポジトリ初期化（CLI v2.1.165 相当・63,719 行） | `2650e77c624f274f11af6dc4223efe623a05e840` | `[1]`〜`[75]`（BASE-A・行番号で参照） |
| `anchor/2026-06-21` | `1a7d39cab3539583157847db90f343550a8fe42e` | 定期取り込み（v2.1.178+ 反映・65,371 行） | `c7c620cb201328ba440f97a45624929b5b3684ac` | `[75]` の版境界（BASE-C・行番号で参照） |
| `anchor/2026-08-19` | `32e6ee3566896a4f0a120a5c98b667aea98b22c6` | 定期取り込み（CLI v2.1.235 相当・84,016 行） | `f6f26436ea1725abdbd042c99ddda9f545107ef4` | `[76]`〜`[97]`（BASE-B・見出し＋行番号で参照） |

> blob ハッシュは**内容だけから決まる**（リポジトリ・パス・commit に非依存）ため、`git cat-file -p <blob>` で「照合に使っているファイルが確かにこの断面か」を独立に検証できる。

### 現状の確認結果（2026-09-05）

- `.claude/scripts/` 配下のスクリプトは**履歴を書き換えず、タグにも触れない**。`run-doc-summary.ps1` の `rebase --abort` は中断状態の後始末であって履歴書き換えではない。
- `main` は `bot/doc-summary` に対して **0 ahead / 229 behind**（分岐なしの直線）。したがって将来の反映は fast-forward で済み、anchor commit は無傷で `main` の履歴に入る。**この直線関係を壊さないことが最も安価な保全策**。
- BASE-A（`anchor/2026-06-06`）は既に `main` 到達可能。**BASE-B・BASE-C は `bot/doc-summary` にしか無い**ため、保全の必要性が高いのはこの 2 本。

### ⚠ 本リポジトリ自身も commit ハッシュに依存している（別課題）

anchor タグは外部文書（cc-relative-info の v1.2）のために設けたものだが、**本リポジトリの生成サマリも同種の依存を持つ**。各サマリのフッタに差分起点が埋め込まれているためである。

```
<!--
base_commit: 2667e8110b59c2cec8b85dd866ec8f529a5fa572
head_commit: 1204f96c5d31ae446075090190d361a2063df414
-->
```

2026-09-05 時点の実測: **216 ファイル / 一意な commit 86 件**が参照されており、**うち 8 件は本リポジトリの HEAD から到達不能**。到達不能な 8 件は**すべて `cc-relative-info`（repo A）のコミット**で、A→B 移行前にパイプラインが repo A で動いていた時代のアーカイブサマリが repo A の履歴を指しているもの（repo A の `origin/develop` からは全件到達可能なので、壊れてはいない）。

> **したがって「履歴を書き換えない」規律は、外部文書のためだけでなく本リポジトリ自身のためにも要る。** ただし 86 件すべてにタグを打つのは非現実的であり、扱いは別途検討する（未着手）。**repo A の履歴に手を入れる場合は、上記 8 件が失われることを事前に確認すること。**

## ディレクトリ構成

```
LLMs/  (= リポジトリルート)
├── README.md                               # 利用者・人間向けの唯一のルート文書（ルート CLAUDE.md は置かない）
├── .claude/
│   ├── CLAUDE.md                           # 本ファイル（メンテナー向けガイド）
│   ├── settings.json                       # 権限 + SessionStart notify hook
│   ├── skills/update-official-doc-summary/ # 更新サマリ生成 Skill（SKILL.md / templates / derive_light.py）
│   ├── agents/doc-summary-reviewer.md      # Phase 3 第三者レビュー Agent（sonnet）
│   └── scripts/
│       ├── run-doc-summary.ps1             # 無人実行ラッパー（dl→生成→Phase3→commit→bot push）
│       ├── dl_llms.sh / download_list.tsv  # 公式 llms.txt 取得
│       ├── notify-bot-branch.sh            # SessionStart 通知
│       ├── register-doc-summary-task.ps1   # スケジューラ登録ヘルパー
│       └── README-doc-summary-bot.md       # 運用手順の集約
├── official-llms-txts/                     # 入力（ナビは同 dir の README.md。CLAUDE.md は置かない）
└── official-doc-update-summary/            # 出力（claude-code-docs / mcp、各 latest・latest-detail・archives）
```

## パイプラインの要点

- **実行**: `pwsh -NoProfile -File .claude/scripts/run-doc-summary.ps1 -Site all`（リポジトリルートから。スクリプトは `$PSScriptRoot\..\..` で本リポジトリルートを解決し自分で `Set-Location` する）。`-DryRun` は push のみ抑止、`-SkipDownload` は dl をスキップ。
- **`claude -p` の前提**: ラッパーは `cwd=本リポジトリ（B）` で `claude -p "/update-official-doc-summary --site <slug> --automated"` を起動する。Skill は本リポジトリの `.claude/skills/` からロードされる。
- **差分検出**: 各サマリ末尾フッタの `head_commit` を起点に `git diff <BASE> <HEAD> -- official-llms-txts` で原文差分を取得する。フッタの運用メタ（`base_commit` / `head_commit` / `generated_at_full`）が次回実行の差分起点。
- **第三者レビュー（Phase 3）**: 無人実行（`--automated`）では `doc-summary-reviewer` Agent によるレビューを必須化し、PASS まで反復（最大 3 回）。打ち切り時は生成物を破棄して push を抑止。
- **アーカイブ命名**: 旧版は `archives/<作成日=対象期間の最終日>/` へ退避。同一作成日のサマリを同日に複数生成した場合は衝突回避のため `<YYYY-MM-DD>_<HHMM>` を使う。

## 運用メタ

- **bot push 認証**: GCM を一時無効化し、inline credential helper で DPAPI 暗号化トークン（`~/.claude/doc-summary-bot-token.xml`、user-level・同一ユーザー／同一マシンでのみ復号可）を 1 回だけ git に渡す。
- **スケジューラ**: Windows タスク `CC-DocSummaryBot`（毎日・`InteractiveToken`＝ログオン中のみ実行＝DPAPI 復号可）。確認/テスト/削除は `schtasks /Query|/Run|/Delete /TN CC-DocSummaryBot`。
- **公開の定義**: 正式運用では `main` への反映が公開。bot push は `bot/doc-summary` 限定。

## 関連

- **`cc-relative-info`**: 本パイプライン（Skill / Agent / スクリプト）の出自。Claude Code 拡張の開発サンドボックスで、汎用 `llms.txt` 生成ツール `generate-llms-txt` や rules・cross-review 等のメタ開発資産はあちらに残る。本リポジトリの Skill を改修する際の作法（責務 3 層・記述原則）は `cc-relative-info` の `.claude/rules/skill-creation-guide.md` 系に準ずる。
