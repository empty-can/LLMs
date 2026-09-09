---
対象期間: 2026年09月05日 〜 2026年09月08日
作成日: 2026-09-08
---

# Claude Code 公式ドキュメント更新サマリ

```markdown
今回は 3 回ぶんの定期取り込みをまとめた差分ですが、**`llms-full.txt` は 1 バイトも変わっていません**（blob が前回と同一）。差分はページ見出しマップの 19 行（追加 10・削除 9）と `llms.txt` の 4 行だけで、**ページ本文は 1 行も届いていません**。したがって今回わかるのは「見出しの構造が変わったこと」と「ページのタイトルが変わったこと」までで、その中身は次回以降の本文到着を待つことになります。前回が「見出しだけ先に来ていた 7 件に本文が全部追いついた回」だったのに対し、今回はその正反対で、**新たな持ち越しだけが積まれた回**です。持ち越しは見出しで数えて 11 件（移動 1・追加 3・削除 2・改称 5）、これにページタイトルの変更 2 件が加わります。ページの新規追加・削除はなく、`whats-new/` は 6 回連続で差分がありません。

主要なものを以下に挙げます。

1. 「出力スタイルの変更」が、キャッシュを保持する操作の側から無効にする操作の側へ移った
2. スキルのページに「スキルの読み込み先を選ぶ」節が新設され、配下が全面的に改称された
3. 設定ページと設定リファレンスのタイトルが入れ替わり、`All settings` がページタイトルへ移った
4. セッションのページに「セッションデータの削除」の節が新設された
```

## ハイライト

1. [**出力スタイルの変更がキャッシュ無効化の側へ移った**](./latest-detail.md#1-出力スタイルの変更がキャッシュ無効化の側へ移った):  
  見出しマップ上で `Changing output style` が **`Actions that keep the cache`（キャッシュを保持する操作）から `Actions that invalidate the cache`（キャッシュを無効にする操作）へ移動**した。ただし本文は届いておらず、現行の `llms-full.txt` は依然として「セッション途中で変えてもキャッシュは無効にならないが、変更も適用されない」と述べている。**分類が反転した以上この記述は書き換わるはずだが、どう変わるかは本文が来るまで判断できない**。
2. [**スキルの読み込み先を選ぶ節が新設され配下が全面改称された**](./latest-detail.md#2-スキルの読み込み先を選ぶ節が新設され配下が全面改称された):  
  「はじめに」の配下にあった h3 `Where skills live` が、**h2 `Choose where skills load` として 1 段階昇格**した。配下の 4 節はいずれも `Load skills in…` `Use skills in…` のような**動詞始まりの名前に改称**され、**`Resolve skills that share a name` と `Edit a skill during a session` の 2 節が新設**、**`Live change detection` が見出しから消えた**。今回の見出し差分 17 行のうち 11 行がこのページに集中している。
3. [**設定ページと設定リファレンスのタイトルが入れ替わった**](./latest-detail.md#3-設定ページと設定リファレンスのタイトルが入れ替わった):  
  `llms.txt` 上で `settings` のタイトルが `Claude Code settings` から **`Settings files and precedence`** に、`settings-reference` のタイトルが `Claude Code settings reference` から **`All settings`** になった。あわせて **`settings-reference` の先頭 h2 だった `All settings` は `Settings index` に改称**されており、`All settings` という呼称が節からページへ繰り上がった形になっている。
4. [**セッションデータの削除の節が新設された**](./latest-detail.md#4-セッションデータの削除の節が新設された):  
  セッションのページの `Export and locate session data`（セッションデータの書き出しと在り処）配下に、**`Delete session data` の節**が `Where transcripts are stored` と `Name the project directory yourself` の間へ挿入された。現行本文にこの節は無く、**削除の手段・対象・取り消し可否はいずれも未着**である。

## 新規追加されたページ

（今回の対象期間に新規追加・削除されたドキュメントページはありません。`llms.txt` の収録 URL は 202 件・全体 355 行のままで、差分はページタイトル 2 行のみです。`llms-full.txt` は前回と blob が同一のため、展開ページ数も 191 のまま動いていません）

## 大幅に更新されたページ

（本カテゴリの該当はありません。分類の基準は前回同様「実質の差分 50 行以上 かつ 内容の変更を伴うこと」ですが、**今回は `llms-full.txt` が完全に無差分**で、本文が 1 行も変わったページがありません。見出しの変更が最も多いスキルのページでも 11 行です）

## 軽微な更新

今回の差分は **2 ファイル・23 行**です。内訳はページ見出しマップ（`en/claude_code_docs_map.md`）が 19 行（追加 10・削除 9）、`llms.txt` が 4 行（追加 2・削除 2）で、**`llms-full.txt` は前回と blob が同一**（`a399f1b3…`）―― 総行数 93,967 行・展開ページ数 191 のいずれも動いていません。見出しマップの 19 行のうち 2 行は先頭の自動生成スタンプ（2026年09月05日 04時30分57秒 UTC → 2026年09月08日 19時23分06秒 UTC）なので、**見出しそのものの変更は 17 行（追加 9・削除 8）**になります。

今回の差分は**前回の起点から 3 回ぶんの定期取り込みを束ねたもの**ですが、**中間の 2 回は取得結果が前回と完全に同一**で、コミットもサマリ生成も発生していません（実行ログもいずれも「原文差分なし、生成スキップ」で終わっています）。見出しマップのスタンプが最後の 1 回の直前まで進んでいないことも、この 2 回が実際に無差分だったことと整合します。**したがって「取り込みが飛んだ 2 日ぶんの変更を取りこぼしている」という状態ではありません**が、その 2 日のあいだに変更されて元に戻された内容があれば、集約された差分には現れない点は原理的な限界として残ります。

差分のあったページは **6 ページ**（プロンプトキャッシング / スキル / セッション / 設定リファレンス / 設定 / デスクトップアプリのクイックスタート）で、**閾値に届くページは 1 つもなく、全件が軽微更新**です。ただし**いずれも本文が伴っていない ―― 次回以降に本文が届くのを待つ持ち越し**である点に注意してください。**持ち越しを見出しの単位で数えると 11 件**（移動 1・追加 3・削除 2・改称 5）で、これに `llms.txt` のページタイトル変更 2 件が加わります。**前回サマリの時点では持ち越しが 0 件だった**ので、今回はゼロから積み直した形になります。

なお **changelog ページには今回の差分がありません**（`llms-full.txt` が無差分であるため）。したがって上記の変更はいずれも、**リリースノートに現れる前に見出しの構造だけが先行して届いたもの**です。バージョンの対応づけは今回の差分からは行えません。

**新機能**

- **セッションのページに `Delete session data`（セッションデータを削除する）の節が現れました**。`Export and locate session data` の配下、`Where transcripts are stored` と `Name the project directory yourself` の間に入っています（詳細はハイライト 4 参照）— [Manage sessions - Claude Code Docs (English)](https://code.claude.com/docs/en/sessions#export-and-locate-session-data)
- **スキルのページに `Resolve skills that share a name`（名前が衝突するスキルを解決する）の節が現れました**。相当する内容は現行本文では `Where skills live` の地の文に埋もれており、独立した節に切り出されるものと見られます（詳細はハイライト 2 参照）— [Extend Claude with skills - Claude Code Docs (English)](https://code.claude.com/docs/en/skills)
- **スキルのページに `Edit a skill during a session`（セッション中にスキルを編集する）の節が現れました**。削除された `Live change detection` と入れ替わる格好ですが、同内容の改称か別物かは見出しからは判断できません（詳細はハイライト 2 参照）— [Extend Claude with skills - Claude Code Docs (English)](https://code.claude.com/docs/en/skills)

**機能改善**

- 出力スタイルの変更が、キャッシュを保持する操作の側から無効にする操作の側へ移りました。本文は未着で、現行の記述は 2 か所とも旧分類を前提にしたままです（詳細はハイライト 1 参照）— [How Claude Code uses prompt caching - Claude Code Docs (English)](https://code.claude.com/docs/en/prompt-caching#changing-output-style)
- スキルのページで `Where skills live` が h2 `Choose where skills load` へ昇格し、配下 4 節が動詞始まりの名前へ全面的に改称されました（詳細はハイライト 2 参照）— [Extend Claude with skills - Claude Code Docs (English)](https://code.claude.com/docs/en/skills)
- 設定ページと設定リファレンスのタイトルが入れ替わり、`settings-reference` の先頭 h2 も `All settings` から `Settings index` に改称されました。両ページとも `llms.txt` の説明文は無変更です（詳細はハイライト 3 参照）— [All settings - Claude Code Docs (English)](https://code.claude.com/docs/en/settings-reference)

**その他**

- **デスクトップアプリのクイックスタートから `Coming from the CLI?`（CLI から来た方へ）の h2 が消えました**。同ページの見出しは `Install` / `Start your first session` / `Now what?` / `What's next` の 4 つになります。**削除だけで、置き換わる見出しはありません**。CLI 利用者向けの案内が他ページへ移されたのか、内容ごと落とされたのかは本文が来るまで判断できません — [Get started with the desktop app - Claude Code Docs (English)](https://code.claude.com/docs/en/desktop-quickstart)
- **スキルのページから `Live change detection`（ライブ変更検出）の h4 が消えました**。現行本文では「スキルディレクトリのファイル変更を監視し、追加・編集・削除が再起動なしで現在のセッションに効く」ことと、その適用範囲が `SKILL.md` のテキストに限られる（プラグインを兼ねるスキルフォルダの `hooks/` `.mcp.json` などは `/reload-plugins` が要る）ことを述べている節です。**この内容が新設の `Edit a skill during a session` に引き継がれるのか、別の節に吸収されるのかは未確定**です（詳細はハイライト 2 参照）— [Extend Claude with skills - Claude Code Docs (English)](https://code.claude.com/docs/en/skills)
- 見出しマップ先頭の自動生成スタンプが 2026年09月05日 04時30分57秒 UTC から 2026年09月08日 19時23分06秒 UTC へ進みました。**対象期間中に上流の再生成が 1 回だけ走った**ことを示しており、無差分だった 2 回の取り込みの説明になっています

**参考リンクについて**: 本サマリの参考リンクは前回に続き**すべて英語版のみ**です。今回の変更は**英語版の `llms-full.txt` にすら本文が届いていない**ため、日本語版が追従していないことは論理的に確実ですが、念のため作成時点で公開中の日本語版ページを実際に取得して確認しました。**日本語版のプロンプトキャッシングでは「出力スタイルの変更」が依然として「キャッシュを保持するアクション」の一覧に載っており、本文も「キャッシュは無効になりませんが、変更も適用されません」の旧記述のまま**、**日本語版のスキルのページは「スキルが存在する場所」が h3 のままで、「ライブ変更検出」も残っており、`Choose where skills load` や `Edit a skill during a session` に相当する見出しは存在しません**。加えて**リンク先のアンカーについても注意が要ります** ―― 新設・改称された見出し（`#delete-session-data`・`#choose-where-skills-load`・`#settings-index` など）は `llms-full.txt` に存在しないため、本サマリでは**アンカー無しのページ URL、または現行本文にも実在する親セクションのアンカー**のみを使っています。

## 新着情報

（今回の対象期間には `whats-new/` 配下のページに差分がありませんでした。`llms-full.txt` が完全に無差分であるため、差分のあった 6 ページはいずれもリファレンス・ガイド系の見出し変更のみです。最新の週間ダイジェストは 6 回前のサマリで扱った Week 34（2026年08月17日～21日）のままで、新しい週のダイジェストの追加も既存ページの訂正もありません。`whats-new/` の無差分は 6 回連続です）

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-09-05.md](./archives/latest/2026-09-05.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-09-05.md](./archives/latest-detail/2026-09-05.md)

<!--
base_commit: 79f96cfde0b383e61550570a0d780c890e54cf66
head_commit: b8993e0293f2b6b04fd7517ad897abdaa6e0f01b
generated_at_full: 2026-09-09T15:07:34+09:00
-->
