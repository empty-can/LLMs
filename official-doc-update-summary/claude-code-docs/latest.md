---
対象期間: 2026年11月25日 〜 2026年11月27日
作成日: 2026-11-27
---

# Claude Code 公式ドキュメント更新サマリ

```markdown
**今回は、Desktop アプリの管理者向けの記述が増えました。SSH とローカルセッションを制限する 3 つのキーは、サーバー管理設定（server-managed settings）と各コンピューターの管理設定の両方に置く、という節ができました。管理設定の `model` で、新しいセッションが始まるモデルを決める節も加わりました**。変わったのは `desktop`・`settings-reference`・`model-config` の 3 ページです。このうち `desktop` は 78 行（追加 62・削除 16）が変わった大幅更新です。changelog への追加、新規ページ、新着情報のページはなく、`llms.txt` も変わっていません（URL は 221 のまま）。`llms-full.txt` の生の差分は追加 75・削除 25 で、総行数は 137,484 行から 137,534 行になりました。

主要なものを以下に挙げます。

1. Claude Desktop v3.1623.0 以降は、`sshHostAllowlist`・`disableDesktopLocalSessions`・`disableSshSavedPasswords` を、サーバー管理設定と、コンピューター上の Claude Code の MDM ポリシーか管理設定ファイルの両方から読む。両方に同じ値を置き、コンピューター側は Desktop 自身のデバイス管理ポリシーではなく Claude Code のものに置く
2. Desktop の管理設定の表に `model` が加わり、モデルピッカーの **Set by admin** の意味と、開始時のモデルの設定をやめる手順が載った。`model-config` では、組織のデフォルトの上書きが有効でも `--model` などのモデルで始まるのは「ターミナルでは」と限定された
3. Linux か macOS のリモートマシンでは、Claude Desktop v6.6395.0 以降なら、フォルダーの制限があっても Desktop の切断中にファイルの読み取り・検索・編集を続けられる。新しいワークフローも、条件を満たせば前もって承認しておくことで切断中に始められる
```

## ハイライト

1. [**Desktop の SSH とローカルセッションの 3 つのキーをサーバー管理設定とコンピューターの両方に置くようになった**](./latest-detail.md#1-desktop-の-ssh-とローカルセッションの-3-つのキーをサーバー管理設定とコンピューターの両方に置くようになった):  
  `desktop` に h4「Keys that apply from server-managed settings and managed settings on a computer」と、その下の h5「Which SSH host allowlists apply」ができました。Claude Desktop v3.1623.0 以降が `sshHostAllowlist`・`disableDesktopLocalSessions`・`disableSshSavedPasswords` を両方から読むこと、どちらの値が効くか、なぜ同じ許可リストを両方に置くのかが載っています。`settings-reference` の 2 つのキーの説明と、`policyHelper` の h4「Keys that only Claude Desktop uses」もこれに合わせて改められました
2. [**管理設定の model で Desktop の新しいセッションが始まるモデルを決められることが載った**](./latest-detail.md#2-管理設定の-model-で-desktop-の新しいセッションが始まるモデルを決められることが載った):  
  `desktop` の管理設定の表に `model` の行が加わり、h4「Set the model that new sessions start on」ができました。モデルピッカーの **Set by admin** の意味、設定をやめる 3 つの手順、組織のデフォルトモデルが上書きする場合の扱いが載っています。`model-config` の「Organization default model」も、`--model` などのモデルで始まるのは「ターミナルでは」と書き直されました
3. [**Desktop の切断中も SSH のタスクでファイルの操作とワークフローを続けられる条件が載った**](./latest-detail.md#3-desktop-の切断中も-ssh-のタスクでファイルの操作とワークフローを続けられる条件が載った):  
  `desktop` の「Limits while Desktop is disconnected」で、フォルダーの制限があっても、Linux か macOS のリモートマシンで Claude Desktop v6.6395.0 以降ならファイルの読み取り・検索・編集を続けられる、となりました。新しいワークフローを切断中に始めるための事前の承認の手順と、それを試す「Test file work and workflows」も加わっています。Windows のリモートマシンでの MCP サーバーの扱いも v6.6395.0 に合わせて書き直されました

## 新規追加されたページ

（今回の対象期間に新規追加されたドキュメントページはありません。`llms.txt` は変わっておらず、URL は 221 のままです。`llms-full.txt` の `Source:` の行も 226、固有のページも 221 のままです）

## 大幅に更新されたページ

- [**Desktop application**](./latest-detail.md#1-desktop-application) ([English](https://code.claude.com/docs/en/desktop#keys-that-apply-from-server-managed-settings-and-managed-settings-on-a-computer)):  
  78 行（追加 62・削除 16）が変わりました。管理設定の 2 つの h4 と 1 つの h5 が加わり（詳細はハイライト 1・2 参照）、切断中のタスクの制限（ハイライト 3）と、SSH の接続のタイムアウトの再試行の条件が書き直されました

## 軽微な更新

今回の差分は **2 ファイル**（`llms-full.txt`・見出しマップ）で、`llms.txt` は変わっていません。対象期間の途中の取り込み（`479f813`）では Claude Code の入力ファイルは変わっておらず、差分はすべて `ff1331b` の取り込みのものです。`llms-full.txt` で内容が変わったのは **3 ページ**で、大幅更新の `desktop` が 78 行（追加 62・削除 16）、`settings-reference` が 18 行（追加 11・削除 7）、`model-config` が 4 行（追加 2・削除 2。`llms-full.txt` に 2 回載っているページの同じ変更が 2 か所に出たもの）です（合計で追加 75・削除 25 で、生の差分と一致します）。以下は、大幅更新の `desktop` を除く 2 ページの変更です。changelog への追加と、新着情報（whats-new）のページはありません。

**新機能**

- `settings-reference` の `policyHelper` の下に h4「Keys that only Claude Desktop uses」ができた。Desktop は自分だけが使うキーをヘルパーを走らせずに読むので、そうしたキーはヘルパーを指定する MDM ポリシーか管理設定ファイルに置く（詳細はハイライト 1 参照） — [English](https://code.claude.com/docs/en/settings-reference#keys-that-only-claude-desktop-uses)

**機能改善**

- `settings-reference` の `sshHostAllowlist` の Scope が、サーバー管理設定を配るならそこと各コンピューターに同じ一覧を置く、になり、Desktop はこのキーをポリシーヘルパーから読まない、と加わった。Default には、サードパーティのプロバイダーでは SSH セッションは既定でオフ、と加わった（詳細はハイライト 1 参照） — [English](https://code.claude.com/docs/en/settings-reference#sshhostallowlist)
- `settings-reference` の `disableDesktopLocalSessions` の Scope が、サーバー管理設定を配るならそこと各コンピューターに置く、になり、`false` に「もう一方の場所の `true` がローカルセッションをオフにしうる」と加わった（詳細はハイライト 1 参照） — [English](https://code.claude.com/docs/en/settings-reference#disabledesktoplocalsessions)
- `model-config` の「Organization default model」で、上書きが有効でも `--model` フラグ・`ANTHROPIC_MODEL`・管理設定・`--settings` のモデルで新しいセッションが始まるのは「ターミナルでは」と限定された（詳細はハイライト 2 参照） — [日本語](https://code.claude.com/docs/ja/model-config#organization-default-model) / [English](https://code.claude.com/docs/en/model-config#organization-default-model)

**その他**

- `settings-reference` の `disableDesktopLocalSessions` で、Type の「JSON の Boolean の `true` だけが効く」が「JSON の Boolean の `true` を使う」という言い方になった。ほかの値は無視し、文字列の `"true"` や `1` のような Boolean でない値には警告も記録する、という文と、「Local sessions on managed devices」へのリンクの文が外れた — [English](https://code.claude.com/docs/en/settings-reference#disabledesktoplocalsessions)
- `settings-reference` の `sshHostAllowlist` の、`managedSourcesBehavior` を `"merge"` にしたときの段落で、どれかに一致するホストを「許す」が、片方にしか一致しないホストも「許しうる」に、空の配列を置いても SSH セッションがほかのソースのホストで「オンのまま」が「オンのままでありうる」になった — [English](https://code.claude.com/docs/en/settings-reference#sshhostallowlist)

## 新着情報

（今回の差分に新着情報（`whats-new/`）のページはありません）

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-11-25.md](./archives/latest/2026-11-25.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-11-25.md](./archives/latest-detail/2026-11-25.md)

<!--
base_commit: 1fbf59d6a37ee0c078616ce1887005838b16c3ae
head_commit: ff1331b1ac08161c9abe13ea96b72c30b1a450ff
generated_at_full: 2026-11-28T15:05:59+09:00
-->
