---
対象期間: 2026年11月06日 〜 2026年11月07日
作成日: 2026-11-07
---

# Claude Code 公式ドキュメント更新サマリ

```markdown
**今回は通常のページ 3 つに小さな変更があり、`hooks-guide` で `ExitPlanMode` を自動承認するフックの例が `updatedInput` を返す形に直り、`mcp` には MCP タスクの答えで省ける項目が載りました**。新しいページはなく、228 ページ中 3 ページが変わり、変更はページ単位で 28 行（追加 10・削除 18）です。50 行以上変わったページはないので、大幅更新はありません。changelog・`llms.txt`・見出しマップは変わっていません。総行数は 127,986 行から 127,978 行に減りました。取り上げる項目が 2 つなので、ハイライトも 2 件です。

主要なものを以下に挙げます。

1. `hooks-guide` の「Auto-approve specific permission prompts」に、`ExitPlanMode` のようにユーザーの操作を要するツールでは `"allow"` に `updatedInput` も要り、なければ許可は無視されプロンプトが出る、と載り、例のコマンドが `jq` で `tool_input` を返す形になった（`hooks` の表にも同じ注記が加わった）
2. `mcp` の「Answer the call with a task」に、`createdAt`・`lastUpdatedAt`・`ttlMs` を省いた答えや `pollIntervalMs` が `null` の答えも Claude Code が受け付け、v2.1.317 より前は失敗していた、と載った
```

## ハイライト

1. [**ExitPlanMode の自動承認の例が updatedInput を返す形に直った**](./latest-detail.md#1-exitplanmode-の自動承認の例が-updatedinput-を返す形に直った):  
  `hooks-guide` の「Auto-approve specific permission prompts」に、`ExitPlanMode` のようにユーザーの操作を要するツールでは `"allow"` に `updatedInput` も要り、なければ Claude Code は許可を無視してプロンプトを出す、という文が加わりました。例のコマンドは、`echo` で決まった JSON を書く形から、`jq -c` で入力の `tool_input` を `updatedInput` として返す形になっています。`hooks` の「PermissionRequest decision control」の表の `updatedInput` の行にも、`AskUserQuestion` と `ExitPlanMode` にはこのフィールドが要る、と加わりました
2. [**MCP タスクの答えに createdAt などがなくても通るようになった**](./latest-detail.md#2-mcp-タスクの答えに-createdat-などがなくても通るようになった):  
  `mcp` の「Answer the call with a task」で、タスクの答えの中身が原因で呼び出しが `Unsupported result type 'task' for tools/call` のエラーになるのは、答えに `taskId` がないか有効な `status` がないとき、に改められました。`createdAt`・`lastUpdatedAt`・`ttlMs` を省いた答えや、`pollIntervalMs` を `null` にした答えも、Claude Code は受け付けます。ページは、v2.1.317 より前はこうした答えが `Unsupported result type` のエラーで失敗したとし、その版でも動かすには 3 つのフィールドを送り、`pollIntervalMs` は数値で送るか送らないよう勧めています

## 新規追加されたページ

（今回の対象期間に新規追加・削除されたドキュメントページはありません。`llms.txt` は変わっておらず、`llms-full.txt` に展開されている固有のページも 228 のままで、`Source:` の行が 231 あり 3 ページが 2 回展開されている状態も前回と同じです）

## 大幅に更新されたページ

（今回の対象期間に、50 行以上変わったページはありません。最も多いのは `hooks-guide` の 18 行です）

## 軽微な更新

今回の差分は **`llms-full.txt` の 1 ファイル**で、`llms.txt` と見出しマップは変わっていません。`llms-full.txt` の生の差分は追加 10 行・削除 18 行で、ページの並びは変わっていません。228 ページ中 **3 ページ**（`hooks-guide`・`mcp`・`hooks`）が変わり、ページ単位の合計は 28 行（追加 10・削除 18）で生の差分と一致します（2 回展開されている 3 ページはどれも変わっていません）。changelog は変わっておらず、収録リリースは 437 のまま、最新は前回と同じ v2.1.319（2026年11月06日）です。大幅更新はないので、**3 ページ**すべてを以下にまとめます。

`llms-full.txt` の総行数は **127,986 行から 127,978 行へ 8 行減り**ました（生の差分の差し引き 10 − 18 と一致）。`Source:` の行は 231、固有のページは 228 のままで、2 回展開されている 3 ページ（`plugins/create`・`plugins/install`・`plugins/mods/overview`）も前回と同じです。コードフェンスの外の見出しは、引用の中の見出しも数えると 6,070、行頭が `#` の見出しだけを数えると 6,059 で、どちらも変わっていません（加わった見出しも、外れた見出しも、改称された見出しもありません）。

**機能改善**

- `ExitPlanMode` を自動承認するフックの例と、PermissionRequest の `updatedInput` の行の注記（`hooks-guide`・`hooks`。詳細はハイライト 1 参照）
- MCP タスクの答えで省ける項目（`mcp`。詳細はハイライト 2 参照）

## 新着情報

**今回、新着情報（`whats-new/`）のページに変更はありません**（最新の週のダイジェストは前回と同じ Week 37 です）。

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-11-06.md](./archives/latest/2026-11-06.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-11-06.md](./archives/latest-detail/2026-11-06.md)

<!--
base_commit: b3f45341023a7453d8b8e8e11e025447ef991a24
head_commit: 0b52aad1c2858e15e1387c14baa0116109fe73bd
generated_at_full: 2026-11-08T15:06:50+09:00
-->
