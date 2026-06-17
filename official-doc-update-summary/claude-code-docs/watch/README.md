# ja 追従リンク watch（req4）

公式ドキュメント更新サマリの **en 単独リンク**（req3 で ja 翻訳ラグのため en のみにした
セクションアンカー、および en ページは在るが ja ページが未作成のページリンク）を監視し、
ja セクション／ja ページが出現したら **`[日本語]` リンクを後追い注入**する仕組み。

> **追従するのは日本語側のみ。** 各項目は既に en リンクを持つ前提で、その ja を後追いする。
> req4 のもう一方のケース（**en ページ自体が未作成でリンク無し生成**したハイライトに、en
> ページ出現後にリンクを足す）は自動化していない。下の「既知のギャップ」を参照。

機構本体: [`.claude/skills/update-official-doc-summary/scripts/watch.py`](../../../.claude/skills/update-official-doc-summary/scripts/watch.py)

## 設計の要（なぜ注入まで自動化できるか）

ja 追従の注入は **本文を 1 文字も変えない純粋な追記**で、貼るリンクは生成時点で完全に確定している:

- ja URL = en URL の `/docs/en/` → `/docs/ja/` 置換
- アンカー `#id` = Mintlify が ja 見出しにも付与する **en と同一の id**
- 編集 = detail / light 両ファイルで `[English](<en>)` を
  `[日本語](<ja>) / [English](<en>)` に差し替え（**置換数 == 1 を検証**）

注入時に人の判断は不要。唯一の不確実性は「ja セクション／ページが**本当に反映されたか**」で、
これを二信号で自動判定する。判定が確実な分だけ自動注入し、曖昧な分は人の目視に回す。

## 3 ティア（`check` の判定）

| status | 条件 | 扱い |
|---|---|---|
| `ready` | ページトップ型: ja ページが GET 200 ／ セクション型: アンカー `id` 存在 **かつ** 弁別 probe が本文に存在 | **自動注入対象** |
| `manual` | セクション `id` は存在するが**弁別 probe が無い**（散文のみの変更など） | 人が ja セクションを目視し `inject --apply --only <key>` で個別注入 |
| `pending` | セクション `id` 未出現、または弁別 probe が**不在**（見出しはあるが内容が古い＝未翻訳） | 監視継続。次回 `check` で自動的に昇格 |

**弁別 probe** = その行の inline-code トークンのうち最も識別子的なもの（`_` `.` `-` `/` か大文字を含む、
または 10 字以上）の最長。翻訳されても字面が残る識別子（例 `Co-Authored-By` / `claude-plugins-official` /
`CLAUDE_CODE_SYNC_SKILLS_INSTALL_TIMEOUT_MS`）を選ぶことで「セクション存在」と「内容鮮度」を区別する。
汎用語（`curl` `if` `events` 等）しか無い行は鮮度を自動確認できないため `manual` に回す。

> この弁別ゲートは実測で偽陽性を 1 件捕捉して導入した: `troubleshoot-install#check-network-connectivity`
> は ja に見出しはあるが PowerShell の `Invoke-WebRequest` 注記が未翻訳。汎用 probe `curl` なら誤って
> `ready` になるが、強 probe `Invoke-WebRequest` 不在で正しく `pending` に留まる。

## 使い方

```bash
# 1) en 単独リンクからレジストリを seed（ネットワーク不要・冪等）
python watch.py scan

# 2) live ja ドキュメントへの反映を再チェック（ネットワーク）。status を更新
python watch.py check          # -v で pending も表示, --only <substr> で絞り込み

# 3) ready 項目を注入。--apply で書き込み, --commit でコミットまで
python watch.py inject                     # dry-run（差分プレビュー）
python watch.py inject --apply --commit    # detail+light に注入してコミット
```

## push 境界（重要）

`watch.py` は **push しない**。外向き・不可逆な push だけを人／CI の手綱に残す:

- **ローカル保守**: `inject --apply --commit` まで自走 → push は DPAPI bot token のセキュア経路で人が実行
  （`Higashi-no-Gensokyo` identity は `empty-can/LLMs` に 403。bot token のみ push 可）
- **CI（GitHub Actions bot）**: 定期実行で `scan` → `check` → `inject --apply --commit` → 後段ステップで
  bot token により `git push`。新規サマリ生成と同じ自律フローに乗せる

## レジストリ `registry.json`

`{"version": 1, "items": { "<name>::<en_url>": { ... } }}`。key の `<name>` は `live` または
archive 日付（`2026-06-09` 等）。1 項目 = 1 つの en 単独リンク。主なフィールド:

| field | 意味 |
|---|---|
| `name` / `en_url` / `ja_url` | 所属サマリ（live/日付）と en→ja リンク |
| `slug` / `anchor` / `kind` | ページ slug・アンカー id・`ja-section`／`ja-page` |
| `term` / `strong` | 弁別 probe とそれが強 probe か |
| `status` | `pending` / `manual` / `ready` / `injected` |
| `first_seen` / `last_checked` / `injected_at` | 監視メタ |

注入済み（`injected`）項目はその行が `日本語` を含むため `scan` の再検出対象外になり、冪等。
live 項目はサマリが archive へ移動すると key が `<日付>::…` に振り直される（旧 `live::…` key は
無害に残置。ja_url は不変なので `check` は引き続き有効）。

## 既知のギャップ: en ページ新規作成の追従（未自動化）

この watch は **ja 側の後追い専用**で、en ページ自体の新規作成には追従しない。実装がすべて
「既存 en リンク」前提のため:

- `scan` は `[English](…/en/…)` のリテラル en リンクを持つ行しか seed しない
- `check` は ja URL だけを GET する（en URL は見に行かない）
- `inject` は既存 `[English]` 断片を起点に `[日本語]` を差し込む（起点が無いと注入不可）

`watch.py` docstring の "page-creation" も **ja ページ作成**（`kind="ja-page"`: en ページは在り
ja を待つ）を指す。req4 当初の「ハイライトのページ未作成時はリンク無し生成 → en ページ出現で
リンク追加」のうち、**en ページ出現の追従だけが未実装**。

実害は現状ゼロ（非 changelog ハイライトは en doc 差分由来で en ページが必ず存在し、changelog
由来は req4 対象外）。ただし将来 link-less ハイライトが出た場合に静かに取りこぼさないよう、
**`scan` が「リンク無しハイライト」（`## N.` セクションに `code.claude.com/docs/` リンクが 1 つも
無いもの）を検出して `WARNING:` を出力する**検出ガードを入れてある。これは registry には書かず
exit code も変えない（ja 追従の妨げにしない・bot ログに残るだけ）。警告が出たら en ページの有無を
人が確認し、必要なら手動でリンクを追記する。フル自動化（en 用の seed / check / 注入ロジック追加）は
入力が発生してから判断する。
