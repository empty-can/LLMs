---
対象期間: 2026年09月26日 〜 2026年09月27日
作成日: 2026-09-27
---

# Claude Code 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
**今回、本文が変わったのは `cross-session-messaging`（Message your other Claude Code sessions）の 1 ページだけで、差分は 69 行（追加 16・削除 53）の「削る」方向の書き直しです**。古い版の注記や他ページと重なる案内が外れ、送信側への通知などの説明も一部消えました。changelog・`llms.txt`・`whats-new/` に変更はなく、総行数は 104,099 行から 104,062 行へ 37 行減っています。見出しマップには、本文にまだない見出しが 23 件先に載りました。

主要なものを以下に挙げます。

1. クロスセッションメッセージングのページから古い版の注記と重複した案内が外れた
2. 保留したメッセージを送信側に知らせる通知などの説明も消えた
3. 見出しマップに本文にまだない 23 の見出しが先に載った
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**クロスセッションメッセージングのページから古い版の注記と重複した案内が外れた**](#1-クロスセッションメッセージングのページから古い版の注記と重複した案内が外れた):  
  `cross-session-messaging` から「v2.1.2xx より前は…」という注記が **7 か所**消え、冒頭の `ListAgents`・`SendMessage` の説明段落と、「用途ごとに専用の機能を使う」という 5 項目の案内も外れました。`channels` への案内は「関連リソース」に移っています
2. [**保留したメッセージを送信側に知らせる通知などの説明も消えた**](#2-保留したメッセージを送信側に知らせる通知などの説明も消えた):  
  受信側がメッセージを保留・拒否したときに同じマシンの送信側へ届く通知、自分自身の名前あての送信の拒否、クラウドセッションの `cloud` ラベルなど、**挙動を説明する記述も削られました**。changelog に対応する項目はなく、機能自体が変わったのかは本文からは判断できません
3. [**見出しマップに本文にまだない 23 の見出しが先に載った**](#3-見出しマップに本文にまだない-23-の見出しが先に載った):  
  `permissions` のシンボリックリンクの 4 見出し、`hooks` の MCP ツールフックの 3 見出し、`agent-sdk/modifying-system-prompts` のシステムプロンプト外のコンテキストの 4 見出しなど、**11 ページに 23 の見出し**が加わりました。いずれも本文（`llms-full.txt`）にはまだありません
<!-- light:highlight-list:end -->

## 1. クロスセッションメッセージングのページから古い版の注記と重複した案内が外れた

**`cross-session-messaging` の差分は 69 行（追加 16・削除 53）で、ページは 368 行から 331 行になりました。** 見出しの追加・削除・改称はありません。このページが本文に入った 2026年08月08日以降の取り込み（46 回分）と照合しましたが、どの版とも一致せず、以前の版にそのまま戻ったものではなく新しい書き直しです。

外れた「古い版の注記」は次の 7 か所です（下限の要件そのものは残っています）。

| 節 | 外れた注記 |
|---|---|
| Message delivery | v2.1.251 より前は、新しいターンを始めたメッセージの `@` メンションが受信側でファイルや MCP リソースを添付していた |
| See which sessions Claude can reach | v2.1.239 より前は、チームメイトが一覧に出なかった（名前でのメッセージはできた） |
| See which sessions Claude can reach | v2.1.239 より前は、一覧にこのセッションの名前が出ず、自分あてのメッセージは「見つからないエージェント」として報告された |
| Message sessions on other machines | v2.1.225 より前は、他のマシンのセッションから届いたメッセージに返信することしかできなかった（「会話を始めるには v2.1.225 以降」の要件は残る） |
| What a message looks like | v2.1.247 より前は、届いたメッセージをプレビューではなく全文で表示していた |
| Non-interactive sessions | v2.1.225 より前は、`-p` セッションで保留したメッセージに期限がなかった |
| Limitations | v2.1.236 より前は、短時間に集中した送信を「送信済み」と報告し、受信側が捨てていた |

**他のページと重なる案内も整理されました。**

- **冒頭の段落**: 「Claude は到達できるエージェントを探す `ListAgents` と、名前で届ける `SendMessage` の 2 つのツールを使う。同じ `SendMessage` でサブエージェントやエージェントチームのチームメイトにも送れる」という段落が消えました（2 つのツールの名前は「Message another session」の節に残っています）
- **「When to use cross-session messaging」の後半**: 会話の続行はセッションの再開、Claude が起動・監督するチームはエージェントチーム、多数のセッションの監視はエージェントビュー、別の端末からの操作は Remote Control、外部イベントの投入はチャネル、という 5 項目の使い分けの案内が消えました。**チャネルは「Related resources」に 1 行加わりました**
- **相互参照**: 「Availability」の確認リストの「Starting a conversation」の項目、古いセッションが一覧から漏れる項目の節内リンク、inbox socket の節の「own-child のルールは下記」という前置きなどが外れました

- [Message your other Claude Code sessions - Claude Code Docs (English)](https://code.claude.com/docs/en/cross-session-messaging#see-which-sessions-claude-can-reach)

## 2. 保留したメッセージを送信側に知らせる通知などの説明も消えた

**削除の中には、注記の整理にとどまらず、挙動そのものを説明していた記述も含まれます。** changelog には今回変更がなく（新しいリリースの追加なし）、これらに対応する「削除」「変更」の項目もないため、**機能が廃止されたのか、説明を省いただけなのかは本文からは判断できません**。

| 節 | 消えた説明 |
|---|---|
| Control inbound messages | **同じマシンの送信側への通知**: 受信側がメッセージを保留したとき、その後で配信・拒否・期限切れにしたときに、送信側の Claude に通知が届く。対話セッションではトランスクリプトに、`claude -p` の送信側ではストリーム出力の informational な `system` メッセージとして届く（v2.1.271 以降）。拒否のときは「待たず、再送しない」よう伝える |
| Control inbound messages | 設定の変更で保留中に `refuse` が効くと、保留中のメッセージをすべて捨て、届けられる送信側に拒否を報告する。保留の上限 100 件が「配信キューとは別」という説明も消えた（上限 100 件と、超えたら古いものから捨てることは残る） |
| Message delivery / See which sessions Claude can reach | **自分自身の名前あての送信を拒否する**こと（拒否する場合の一覧からも外れた） |
| See which sessions Claude can reach | クラウドセッションが一覧で **`cloud` とラベル付けされる**こと。クラウドと Remote Control のセッション一覧を新しい順に一定ページ数まで読み、漏れたときは一覧と送信時に知らせること（Availability の確認リストには短い形で残る）。`/rename` で共有レコードを更新できないと警告し、`--debug` で原因を記録すること |
| Get a notice when another session goes idle（Limits） | 通知が 1 回限りでポーリングしないこと。サブエージェントやチームメイトが `notify_when_idle` を指定しても購読しないこと。拒否を Claude に伝えて要求なしで送り直せるようにすること（「呼び出し全体を拒否する」ことは残る） |
| Message sessions on other machines | 同じマシンでの配信はディスク上のファイルでセッションを登録・発見するしくみであること、Remote Control 接続中に他のマシンへ送ると相手側にこのセッションの Remote Control 名で表示されること、`offline` のセッションや返信先のない一方向のメッセージを送ったときに Claude にそう伝えること |
| What a message looks like | サブエージェントが書いたメッセージは送信側セッションの名前で届き、返信はそのセッションのメインの会話に届くこと |
| Non-interactive sessions | 保留したまま終了した `-p` セッションが、届けられる送信側に期限切れを報告すること（期限後に捨てて期限切れを報告する箇条は残る） |
| The session's inbox socket | 各セッションは自分のソケットを書き出し、親セッションから引き継いだものは使わないこと |
| Limitations | レート制限・重複チェック・キューの上限でメッセージを捨てたとき、対話セッションにどれが捨てたかを伝え、すぐに送り直さないよう伝えること |

コンテナの中と外、WSL 2 とネイティブ Windows のセッションが互いに届かないという結論は残り、理由（別のファイルシステム、別のホームディレクトリとソケットの種類）の説明だけが外れています。

- [Message your other Claude Code sessions - Claude Code Docs (English)](https://code.claude.com/docs/en/cross-session-messaging#control-inbound-messages)

## 3. 見出しマップに本文にまだない 23 の見出しが先に載った

**見出しマップ（`en/claude_code_docs_map.md`）の差分は 27 行（追加 25・削除 2）です。** 自動生成スタンプの更新と 1 見出しの改称を除く 23 行が新しい見出しで、**いずれも本文（`llms-full.txt`）にはまだありません**。前回サマリで扱ったとおり、マップに先に載った見出しは、これまで後の取り込みで本文に入っています。

| ページ | マップに加わった見出し |
|---|---|
| `permissions` | 「Read and Edit」の下に `Symlinks`・`How rules match a symlinked path`・`Writes through a symlink`・`Paths that can't be resolved or that change` |
| `hooks` | 「MCP tool hook fields」の下に `How the tool's result is read`・`When the server is still connecting`・`Events that fire before MCP servers are available` |
| `agent-sdk/modifying-system-prompts` | `Context Claude Code adds outside the system prompt` と、その下の `Reminders Claude Code adds to the conversation`・`Turn off the context your agent replaces`・`See what Claude received` |
| `agent-sdk/typescript` | `SDKControlReloadPluginsResponse`・`SDKControlReloadOutputStylesResponse`、`SDKResultMessage` の下の `resume_reason` |
| `errors` | `Claude Code refuses the marketplace name`・`Plugin was not uninstalled` |
| `glossary` | `System prompt`・`System reminder` |
| `how-claude-code-works` | 「The context window」の下に `Context Claude Code adds on its own` |
| `plugins/troubleshooting` | `A plugin hook blocks a tool call or prompt` |
| `plugins/cli-reference` | 「plugin uninstall」の下に `What an uninstall deletes and keeps` |
| `managed-settings` | 「Find entries Claude Code dropped」の下に ``Invalid values inside `sandbox` `` |
| `gateways` | 「Outage behavior」の下に `Readiness grace period` |

このほか、`agent-sdk/examples` の見出しが `Explore a TypeScript application` から `Explore a demo application` に改称されましたが、本文の見出しは旧名のままです。

`how-claude-code-works`・`glossary`・`agent-sdk/modifying-system-prompts` の 3 ページが、そろって「Claude Code がシステムプロンプトの外で会話に加えるコンテキスト（システムリマインダーなど）」を扱う見出しを持つことになります。本文が入った段階で、内容を確認して取り上げます。

- [Configure permissions - Claude Code Docs (English)](https://code.claude.com/docs/en/permissions#read-and-edit)
- [Hooks reference - Claude Code Docs (English)](https://code.claude.com/docs/en/hooks#mcp-tool-hook-fields)

## 新規追加されたページ

<!-- light:new-pages:start -->
今回、新しく追加されたページはありません（`llms-full.txt` の展開ページは前回と同じ 210 ページで、`llms.txt` にも変更はありません）。
<!-- light:new-pages:end -->

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
- [**Message your other Claude Code sessions**](#1-message-your-other-claude-code-sessions) ([English](https://code.claude.com/docs/en/cross-session-messaging#control-inbound-messages)):  
  古い版の注記 7 か所と、他ページと重なる案内が外れ、送信側への保留通知などの説明も削られました。ページは 368 行から 331 行になっています
<!-- light:updated-pages:end -->

**ここでは、`llms-full.txt` で差分が 50 行（追加と削除の合計）以上あった既存ページを挙げています。** 今回、本文が変わったのはこの 1 ページだけです。

## 1. Message your other Claude Code sessions

**差分は 69 行（追加 16・削除 53）です。** 追加の 16 行は、削った文を含む段落や箇条を短く書き直した行と、「Related resources」のチャネルの 1 行です。内容はハイライト 1（古い版の注記と重複した案内の整理）とハイライト 2（挙動の説明の削除）のとおりです。

節ごとの変化をまとめると次のとおりです。

| 節 | 主な変化 |
|---|---|
| 冒頭・When to use cross-session messaging | ツールの説明段落と、5 項目の使い分けの案内を削除 |
| Message delivery | `@` メンションの v2.1.251 の注記と、自分あての送信の拒否を削除 |
| Get a notice when another session goes idle | 「1 回限り」の説明と、サブエージェント・チームメイトの扱い、拒否後の送り直しの案内を削除 |
| See which sessions Claude can reach | v2.1.239 の注記 2 か所、`cloud` ラベル、自分あての拒否、一覧のページ数の制限、他のマシンへの送り方の案内、`/rename` の警告を削除 |
| Message sessions on other machines | v2.1.225 の注記、ファイルによる登録のしくみ、Remote Control 名での表示、「Claude にそう伝える」という説明を削除 |
| What a message looks like | v2.1.247 の注記、受信側が得るのはテキストだけという補足、サブエージェントが書いたメッセージの扱いを削除 |
| Control inbound messages | 送信側への保留・拒否の通知（`claude -p` の送信側は v2.1.271 以降）と、保留中に `refuse` が効いたときの扱いを削除 |
| Non-interactive sessions | 終了時の期限切れ報告と v2.1.225 の注記を削除 |
| The session's inbox socket | ソケットを親から引き継がないことと、own-child のルールへの前置きを削除 |
| Availability | 確認リストの「Starting a conversation」を削除し、一覧の漏れの項目から節内リンクを外した |
| Limitations | v2.1.236 の注記と、捨てたメッセージを対話セッションに知らせる説明を削除 |
| Related resources | `channels` への 1 行を追加 |

日本語版のページは、今回削られた段落・注記がすべて残った旧版の内容でした。

- [Message your other Claude Code sessions - Claude Code Docs (English)](https://code.claude.com/docs/en/cross-session-messaging#control-inbound-messages)

## 軽微な更新

<!-- light:minor-updates:start -->
今回の差分は **2 ファイル**です。`llms-full.txt` は 69 行（追加 16・削除 53）で、すべて `cross-session-messaging` の 1 ページの変更です。見出しマップ（`en/claude_code_docs_map.md`）は 27 行（追加 25・削除 2）でした。`llms-full.txt` の総行数は **104,099 行から 104,062 行へ 37 行減り**、展開ページは前回と同じ **210 ページ**です。`llms.txt` と changelog に変更はなく、新しいリリースは積まれていません。

**機能改善**

- **`cross-session-messaging` から古い版の注記 7 か所と、他ページと重なる案内が外れました**（詳細はハイライト 1）— [English](https://code.claude.com/docs/en/cross-session-messaging#see-which-sessions-claude-can-reach)

**その他**

- **`cross-session-messaging` から、送信側への保留通知や自分あての送信の拒否など、挙動の説明の一部も消えました**。changelog に対応する項目はありません（詳細はハイライト 2）— [English](https://code.claude.com/docs/en/cross-session-messaging#control-inbound-messages)
- **見出しマップに、本文にまだない見出しが 11 ページで 23 件加わりました**（詳細はハイライト 3）
- **見出しマップで `agent-sdk/examples` の `Explore a TypeScript application` が `Explore a demo application` に改称されました**。本文の見出しは旧名のままです
- **見出しマップ冒頭の自動生成スタンプが、2026年09月26日 05時25分36秒 UTC から 2026年09月28日 00時44分20秒 UTC へ進みました**

**参考リンクについて**: **日本語版の `cross-session-messaging` を実測したところ、今回削られた段落・注記がすべて残る旧版の内容だったため、英語版だけにしています。** 見出しマップにだけある見出しは本文に節がないため、親の節（`permissions` の「Read and Edit」、`hooks` の「MCP tool hook fields」）を英語版で示しています（新しい見出しは英語版の本文にもまだないため、日本語版の反映も確認できません）。**changelog ページへのリンクは、本サマリの方針どおり付けていません。**
<!-- light:minor-updates:end -->

## 新着情報

<!-- light:whats-new:start -->
**`whats-new/` 配下のページに変更はありません。** Week 38 のダイジェストも、まだ追加されていません。
<!-- light:whats-new:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-09-26.md](./archives/latest/2026-09-26.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-09-26.md](./archives/latest-detail/2026-09-26.md)

<!--
base_commit: 4b44c61fdbb75b9b84fdaf00a4bdaded9af968af
head_commit: 969d4e66e660e1486e6cd6678a61708db04c3953
generated_at_full: 2026-09-28T15:02:37+09:00
-->
