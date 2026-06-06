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
