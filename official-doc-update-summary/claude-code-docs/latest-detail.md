---
対象期間: 2026年09月02日 〜 2026年09月03日
作成日: 2026-09-03
---

# Claude Code 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
今回も 1 日分の取り込みですが、差分は 27 ページ・3 ファイル合計 736 行（`llms-full.txt` 728 行 / ページ見出しマップ 6 行 / `llms.txt` 2 行）で、前回の 12 ページ・187 行から拡大しました。ただし `llms-full.txt` の生 728 行のうち 448 行は設定リファレンスの表の桁揃えで、実質は 280 行です。5 回続いていた `llms.txt` の無差分は今回途切れましたが、変わったのは 1 ページのタイトルと説明文だけで、収録 URL は 202 件・展開ページ数は 191 のまま、ページの新規追加・削除はありません。実質 50 行以上のページが 1 つも無いため、今回も大幅更新に該当するページがありません。内容は権限まわり（作業ディレクトリ外の読み取り・無人実行の権限プロンプト・管理設定のパース失敗）に集中しており、あわせて 2026年09月03日 付の v2.1.260（66 件）が入りました。なお今回も `whats-new/` ページに差分がなく、新着情報はありません。

主要なものを以下に挙げます。

1. 作業ディレクトリ外の読み取りを全モードで拒否する `permissions.blockReadsOutsideWorkingDirectories` が新設された
2. 管理設定の文書がパースできないと Claude Code が起動を拒否するようになった
3. 無人実行で権限プロンプトを止める `--permission-prompts none` が文書化された
4. サブエージェントの応答が途中で切れても継続を促すようになった
5. ゲートウェイのプロトコルリファレンスが「互換性ガイド」に改称された
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**作業ディレクトリ外の読み取りを全モードで拒否する設定が新設された**](#1-作業ディレクトリ外の読み取りを全モードで拒否する設定が新設された):  
  設定リファレンスに `permissions.blockReadsOutsideWorkingDirectories` の節が新設され、Read・Grep・Glob・LSP ツールが**作業ディレクトリ外のパスを読むことを `bypassPermissions` を含む全モードで拒否する**ようになった。あわせて権限モードのページには「作業ディレクトリ外の初回読み取り」節が加わり、**auto モードが初回だけ確認を出す**（その場で「今後はブロック」を選ぶとこの設定が書き込まれる）ことが説明された。
2. [**管理設定の文書がパースできないと起動を拒否するようになった**](#2-管理設定の文書がパースできないと起動を拒否するようになった):  
  管理設定のファイル・ドロップイン・macOS の MDM plist・HKLM のレジストリ値のいずれかが存在するのに JSON オブジェクトとして解釈できない場合、Claude Code は**他の管理ソースが有効なポリシーを配っていても終了コード 1 で起動を拒否する**。エラーリファレンスに専用の節が新設され、ソースごとの失敗条件と、拒否を起こさない 3 つの状態が整理された。
3. [**無人実行向けの `--permission-prompts none` が文書化された**](#3-無人実行向けの---permission-prompts-none-が文書化された):  
  前回サマリの軽微更新で v2.1.259 の changelog エントリとして触れた項目が、非対話実行ページの独立節と CLI リファレンスの一覧に載った。**権限ホスト（Agent SDK の `canUseTool` や `--permission-prompt-tool`）に問い合わせず待たずに拒否する**フラグで、Claude には「誰も承認できないので再試行するな」と伝えられる。
4. [**サブエージェントの応答が途中で切れても継続を促すようになった**](#4-サブエージェントの応答が途中で切れても継続を促すようになった):  
  応答途切れの通知をすぐ出さずに処理するケースが 3 通りから 4 通りに増え、4 つ目として**サブエージェント**が加わった。部分応答がテキストのみでツール呼び出しを含まなければ、**対話セッションでも**継続を促し、継続を使い切って初めてエラーで終わる。v2.1.257 より前は初回の切断で終わっていた。
5. [**ゲートウェイのプロトコルリファレンスが互換性ガイドに改称された**](#5-ゲートウェイのプロトコルリファレンスが互換性ガイドに改称された):  
  `Gateway protocol reference` が `Claude Code gateway compatibility guide` に改称され、説明文も書き換えられた。Claude apps gateway の `GET /protocol` は「本ガイドの機械可読版の superset」ではなく「**別文書**」と位置づけ直され、参照側 5 ページのリンクテキストも置き換わっている。今回 `llms.txt` に生じた唯一の差分がこれで、5 回続いた無差分が途切れた。
<!-- light:highlight-list:end -->

## 1. 作業ディレクトリ外の読み取りを全モードで拒否する設定が新設された

設定リファレンスに **`permissions.blockReadsOutsideWorkingDirectories`** の節が新設されました（実質 26 行の追加で、`permissions.additionalDirectories` と `permissions.defaultMode` の間に挿入されています）。冒頭のキー一覧表にも 1 行、`permissions` 自体の **Type** 行にもキー名が加わり、ページ見出しマップにも同じ 1 行が追加されました。この設定を `true` にすると、**Read・Grep・Glob・LSP ツールがセッションの作業ディレクトリ外のパスを読むことを、`bypassPermissions` を含むすべての権限モードで拒否します**。Claude Code が認識するファイル読み取りコマンド（`cat` など）を通じて該当パスを読む Bash コマンドは、**auto モードでも `bypassPermissions` モードでも確認を求められます**。Claude Code v2.1.257 以降が必要です。

スコープの扱いが特徴的です。**どの設定ソースが `true` にしてもブロックが適用される**ため、リポジトリにチェックインされたファイルはプロジェクトに対してブロックを**掛けることはできても、利用者が掛けたブロックを外すことはできません**。`false` は未設定と同じ扱いで、他の設定ファイルの `true` は依然としてブロックします。リポジトリのチェックイン設定だけがディレクトリを追加した場合も、そこへの読み取りにはブロックが効きます。例外として、**Claude Code 自身が必要とするファイル**（skills・plugins・rules・agents・commands、および `~/.claude/` 配下の `CLAUDE.md` メモリファイル）は読めるままです。

サンドボックスとの組み合わせも規定されました。**サンドボックスが有効なとき、この設定はサンドボックス化されたコマンドに対してもホームディレクトリとマウントボリュームのルートへの読み取りを拒否します**。`~/.gitconfig` のようにツールがホームディレクトリから読むファイルもまとめて拒否されるため、特定のパスだけ開け直したい場合は `sandbox.filesystem.allowRead` を使え、とされています。**サンドボックス外で動かすための承認が必要な再試行は `bypassPermissions` モードでも確認を求めます**。一方、セッションの作業ディレクトリがリンクされた git worktree の場合（セッション途中で Claude Code が入ったものを含む）は、**リポジトリ共通の `.git` ディレクトリはサンドボックス化されたコマンドから読み書きできるまま**なので、git はそこで動き続けます。

もう一方の入口が、権限モードのページに新設された **`The first read outside the working directories`（作業ディレクトリ外の初回読み取り）** 節です。ここは設定が**オフの間**の挙動を扱います。auto モードではファイル読み取りは作業ディレクトリ外も含めてプロンプトなしで走りますが、**Claude が Read・Grep・Glob ツールで作業ディレクトリ外のパスを初めて使ったとき、Claude Code はその種の読み取りを今後も許可するかを尋ねます**。このプロンプトは**非対話の `-p` 実行やバックグラウンドセッションでは出ません**（そこでの読み取りは従来どおりです）。選択肢は 3 つで、どれを選んでも Claude は作業を続けます。**Keep allowing** なら読み取りが実行され、以後の作業ディレクトリ外の読み取りも従来どおりで、回答が記録されて二度と尋ねられません。**Block from now on** なら読み取りは拒否され、**ユーザー設定に `permissions.blockReadsOutsideWorkingDirectories` が `true` として書き込まれます**（以後すべてのセッション・すべての権限モードで拒否されるので、後から読ませたいときは `/add-dir` でディレクトリを追加するか設定を消します）。**Ask again next time** なら読み取りは拒否され、次回また尋ねられます。

この 2 つの節に合わせて周辺ページも書き換わりました。権限モードのページの「どのモードでも自動承認しないもの」一覧に 1 項目が加わり、auto モードの判定順の step 2 にも「作業ディレクトリ外の初回読み取りは確認が出る」という例外が追記されています。権限ページでは、**組み込みの読み取り専用 Bash コマンドが全モードでプロンプトなしに走る**という説明に「この設定が囲うパスを除く」という条件が付き、作業ディレクトリの節にも 1 段落が加わりました。サンドボックスのページはフィルターシステム隔離の節に「パスルールを書く代わりにこの設定を使え」という案内が入っています。セキュリティページでは逆に、作業ディレクトリの境界の説明から「**auto モードでは尋ねずに読む**」という 1 文が削除されました。

- [Claude Code 設定リファレンス - Claude Code Docs (English)](https://code.claude.com/docs/en/settings-reference#permissions-blockreadsoutsideworkingdirectories)
- [権限モードを選択する - Claude Code Docs (English)](https://code.claude.com/docs/en/permission-modes#first-read-outside-the-working-directories)

## 2. 管理設定の文書がパースできないと起動を拒否するようになった

エラーリファレンスに **`Managed settings document could not be parsed`** の節が新設されました（実質 27 行の追加。エラーリファレンスは今回 changelog を除けば最大の差分で、実質 34 行のうち大半がこの新節です）。ページ見出しマップにも同じ 1 行が加わり、冒頭のメッセージ対応表にも 2 行（本文のメッセージと `Managed settings drop-in directory could not be read`）が追加されています。組織が管理設定を配っていて、配られた文書のいずれかが**存在するのに JSON オブジェクトとして解釈できない**場合、Claude Code はその文書が運ぶポリシー抜きで動くのではなく、**起動時に終了コード 1 で終了します**。出力行はメッセージの前に失敗したソースを名指しします。

名指しされるソースは 3 種類です。**`managed-settings.json` ファイルまたは `managed-settings.d` 配下のドロップインファイルのパス**、**macOS の管理プリファレンスプロファイル**（`per-user managed preferences` または `device-level managed preferences`）、**Windows のレジストリ値**（`Registry: HKLM\SOFTWARE\Policies\ClaudeCode\Settings`）です。**別の管理ソースが有効なポリシーを配っていても起動を拒否します**。このエラーは対話セッション・`claude -p`・Agent SDK セッション・バックグラウンドセッション、および `claude doctor` を含むほとんどのサブコマンドで出ます。ドキュメントはこの fail closed を意図的なものと明記しており、**パースできない文書の設定は強制しようがなく、そのまま起動すれば組織の統制が効かないままセッションが走ることになる**、というのが理由です。なお**パースできる文書のスキーマ違反ではこのエラーになりません**（従来どおり個別エントリの修復・トップレベルキーの破棄で処理されます）。`managed-settings.d/` ディレクトリが存在するのに一覧できない場合は、代わりに `Managed settings drop-in directory could not be read:` に元のエラーが続きます。対処としては、マシンの管理者であれば名指しされた文書を JSON オブジェクトとして解釈できるよう直すか、ファイル・プロファイル・レジストリ値ごと消すこと、そうでなければ管理者に依頼することが挙げられています（**空の `managed-settings.json` は `{}` と数えられ、起動を妨げません**）。自分の設定ファイルは原因にも解決にもなりません。

管理設定のデプロイページ側では **`Find entries Claude Code dropped`** 節が書き直され（実質 22 行）、従来 1 段落に詰め込まれていた内容が段落に分割されたうえで、**各ソースがこの失敗に至る条件**が 3 項目で列挙されました。**管理設定ファイル／ドロップインファイル**は有効な JSON でないか、トップレベルがオブジェクトでない場合。**MDM plist** は macOS の `plutil` が plist を malformed と報告するか、変換後の内容が JSON オブジェクトでない場合。**HKLM のレジストリ値**は `Settings` 値が文字列でない、空である、または JSON オブジェクトを保持していない場合です。あわせて**この拒否を起こさない 3 つの状態**も明示されました。ファイル・プロファイル・レジストリ値が**不在**なのは失敗ではなくそのソース無しで動くこと、**空の管理設定ファイル**は `{}` と数えられること、**ユーザーが書き込める HKCU のキーの不正な値は起動を止めない**（`/status` と `claude doctor` に通知として出るだけ）ことです。読み取り失敗時に claude.ai / Claude Console の資格情報でサインインしたセッションが起動時に終了する条件も、「読めないか解釈できない」から「**読めない**」に絞られ、対象に `managed-settings.d/` ディレクトリが加わりました。

トラブルシューティングの記述も整理されました。`Setting sources` 行が出ないときの確認項目から「**有効な JSON か確認せよ**」が外れ、代わりに「**有効な JSON でないファイルはこの状態を作らない。Claude Code は起動を拒否する**」という誘導に変わっています。設定ページの「壊れた設定ファイルを直す」節でも、管理設定の項に新しいエラーへの参照が加わり、`-p` 実行はダイアログを出さず壊れた値を飛ばして続行するという説明に「**管理設定の文書がパースできない場合を除く**」という条件が付きました。監視ページの保持スイープイベントの説明でも、`managed-settings.json` 自体の状態が「読めないか解釈できない」から「**読めない**」に絞られています。

- [エラーリファレンス - Claude Code Docs (English)](https://code.claude.com/docs/en/errors#managed-settings-document-could-not-be-parsed)
- [管理設定をデプロイする - Claude Code Docs (English)](https://code.claude.com/docs/en/managed-settings#find-entries-claude-code-dropped)

## 3. 無人実行向けの `--permission-prompts none` が文書化された

非対話実行のページに **`Turn off permission prompts in unattended runs`（無人実行で権限プロンプトをオフにする）** 節が新設されました（20 行すべて追加）。あわせて CLI リファレンスのフラグ表に `--permission-prompts` の行が加わり、ページ見出しマップにも同じ 1 行が入っています。**このフラグ自体は v2.1.259 で追加済みで、前回サマリでは changelog 由来の「新機能」として 1 行触れていました**。今回はそれが正式なドキュメントになった形です。

節の骨子は、**権限プロンプトに答えられる人がいないとき**（スケジュールジョブなど）に `--permission-prompts none` を渡す、というものです。特に効くのは**権限ホストがある実行**で、`canUseTool` コールバックを持つ Agent SDK アプリと、`--permission-prompt-tool` で渡す MCP ツールが挙げられています。**フラグが無いと、実行はそのホストが各権限リクエストに答えるのを待ちます**。フラグを付けると、実行はホストに問い合わせも待機もしません。プロンプトになるはずのものは `PermissionRequest` フックが許可しない限り拒否され、**Claude には「誰も承認できないので再試行するな」と伝えられ**、実行は続きます。ホストの無い `-p` 実行ではどちらにせよ拒否されますが、そこでもフラグは再試行を止める意味を持ちます。**権限ルール・`PermissionRequest` フック・設定した権限モードが先にすべての呼び出しを決めるのは変わらず、Claude Code が拒否するのは他の何も解決しなかったリクエストだけ**です。

実務上の副作用が 2 つ書かれています。1 つは**人の回答を必要とするツールが取り除かれる**ことで、`AskUserQuestion` などは Claude が呼べなくなります。`Elicitation` フックが答えない MCP の elicitation リクエストはキャンセルされます。もう 1 つは**出力への現れ方**で、`--output-format stream-json` では拒否が `permission_denied` のシステムメッセージとして現れ、最終の result メッセージの `permission_denials` に列挙されます。示された例は auto モードとの併用で、`claude -p "Update the dependency pins and run the tests" --permission-mode auto --permission-prompts none` のように書くと、分類器は普段どおり各アクションをレビューし、**プロンプトへフォールバックしていたはずのものを Claude Code が拒否します**。Note として **Claude Code v2.1.259 以降が必要**で、それ以前のバージョンは unknown-option エラーで拒否することが明記されました。CLI リファレンスの行では既定値が `host`（Agent SDK ホストか `--permission-prompt-tool` のツールに送る）であることも示されています。

- [Claude Code をプログラムで実行する - Claude Code Docs (English)](https://code.claude.com/docs/en/headless#turn-off-permission-prompts-in-unattended-runs)
- [CLI リファレンス - Claude Code Docs (English)](https://code.claude.com/docs/en/cli-reference#cli-flags)

## 4. サブエージェントの応答が途中で切れても継続を促すようになった

エラーリファレンスの **`The response above may be incomplete`** の節で、Claude Code が通知をすぐ出さずに処理するケースが **3 通りから 4 通りに増えました**。追加された 4 つ目が**サブエージェント**で、**セッションが対話・非対話のどちらであっても**、切れた応答がテキストを含みツール呼び出しを含まない場合、Claude Code はサブエージェントに続きを促します。通知がサブエージェントの最後のメッセージになるのは、その継続を使い切ってからです。**v2.1.257 より前は、サブエージェントは初回の切断で通知を出していました**。

サブエージェントのページの `API errors in subagents` 節にも、同じ内容が節の冒頭段落として加わりました。こちらでは「実行を終わらせるのではなく続きを促す」「**これは対話セッションでも起きる**」「実行がエラーで終わるのは継続を使い切ってから」と述べられ、既存の「v2.1.199 以降、API エラーで終わったサブエージェントはエラーテキストを調査結果のように返すのではなく失敗として Claude に報告する」という説明の前に置かれています。

同じ変更が 2 か所の周辺記述にも波及しています。エラーリファレンスの、リクエスト進行中に 20 秒データが届かなかった場合の説明では、続きを促す条件が「非対話セッションでは」から「**非対話セッションでは、そしてどのセッションでもサブエージェントの応答については**」に広がりました。エンタープライズネットワーク設定のページのストリームアイドル監視の節も同様で、こちらは 1 段落だった記述が 2 段落に分割され、後半が「非対話セッションと、どのセッションでもサブエージェントの応答について」続きを促す話にあてられています。

- [カスタムサブエージェントの作成 - Claude Code Docs (English)](https://code.claude.com/docs/en/sub-agents#api-errors-in-subagents)
- [エラーリファレンス - Claude Code Docs (English)](https://code.claude.com/docs/en/errors#the-response-above-may-be-incomplete)

## 5. ゲートウェイのプロトコルリファレンスが互換性ガイドに改称された

`llm-gateway-protocol` ページのタイトルが **`Gateway protocol reference` から `Claude Code gateway compatibility guide` へ**変わり、説明文も「Claude Code と LLM ゲートウェイの間の **API 契約**: エンドポイント、転送すべきヘッダーとボディフィールド、フィールドが剥がされたときの機能低下、コスト追跡用の帰属ヘッダー、モデル探索」から「**LLM ゲートウェイを Claude Code と互換に保つ**: Claude Code が呼ぶエンドポイント、転送すべきヘッダーとボディフィールド、それらが剥がされたときに壊れるもの」に書き換えられました。**今回 `llms.txt` に生じた差分はこの 1 行だけ**で、5 回続いていた `llms.txt` の無差分がこれで途切れています（収録 URL 数は 202 件のまま変わりません）。

内容面で実質的なのは、**Claude apps gateway の `GET /protocol` との関係の整理**です。従来は「動作中の Claude apps gateway がこの契約の**機械可読版**を `GET /protocol` で配信し、そこには同じ転送要件に加えて SSO サインイン・管理設定の配信・テレメトリという Claude apps gateway 固有のエンドポイントが載る」とされ、Claude apps gateway が同じ `claude` バイナリから動くのでクイックスタートが仕様を取得する最短経路だ、と続いていました。今回は「**Claude apps gateway（Anthropic 製のセルフホストゲートウェイ）は自身のエンドポイントリファレンスを `GET /protocol` で配信する。それはそのゲートウェイのサインイン・推論・管理設定・モデル探索・テレメトリの各エンドポイントを扱うもので、本ガイドとは別文書である**」に改められました。Claude apps gateway 側のページでも同じ書き換えが入り、「そのコントラクトの superset を配信する」だったところが「**自身のプロトコルリファレンスも配信する**」になっています。

参照側のページも一斉に置き換わりました。**Other LLM gateways**（3 か所）、**Roll out an LLM gateway for your organization**（3 か所）、**Connect Claude Code to an LLM gateway**（2 か所）、**Claude apps gateway**（1 か所）、**Run Claude Code through a gateway**（1 か所）の計 5 ページで、リンクテキストが「gateway protocol reference」から「gateway compatibility guide」へ変わっています。ゲートウェイ概要のページでは「組織が動かすゲートウェイには**実装すべきプロトコル**がある」が「**従うべき互換性ガイド**がある」になりました。ロールアウトのページでも「各 Claude Code リリースが何を送るかの**契約**として protocol reference を維持せよ」が「**リファレンス**として compatibility guide を維持せよ」になっており、いずれも「契約（contract）」という語を落として「互換性を保つための参照文書」という位置づけに寄せる方向で揃えられています。

- [Claude Code ゲートウェイ互換性ガイド - Claude Code Docs (English)](https://code.claude.com/docs/en/llm-gateway-protocol)
- [Amazon Bedrock、Claude Platform on AWS、Google Cloud、Microsoft Foundry 向けの Claude apps gateway - Claude Code Docs (English)](https://code.claude.com/docs/en/claude-apps-gateway#other-gateway-implementations)

## 新規追加されたページ

<!-- light:new-pages:start -->
（今回の対象期間に新規追加・削除されたドキュメントページはありません。`llms-full.txt` に展開されているページ数は前後とも 191 で、`llms.txt` の収録 URL も 202 件のままです。ただし `llms.txt` 自体は 5 回連続の無差分が途切れ、`llm-gateway-protocol` のタイトルと説明文が書き換わった 1 行分だけ変化しました（詳細はハイライト 5 参照）。ページの追加・削除ではないため、本カテゴリには該当がありません）
<!-- light:new-pages:end -->

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
（今回は大幅更新に該当するページがありません。前回同様「実質の差分 50 行以上 かつ 内容の変更を伴うこと」を基準としましたが、最大でもエラーリファレンスの実質 34 行にとどまりました。実質最大は changelog の 69 行ですが、changelog は個別ページとして扱わず「軽微な更新」で扱います。次点は設定リファレンスの実質 31 行、管理設定のデプロイの 22 行、非対話実行の 20 行、権限モードの 15 行です。**設定リファレンスは生の差分が 479 行と今回最大でしたが、そのうち 448 行は冒頭のキー一覧表の桁揃えで、内容の変更は実質 31 行分です**。分量が閾値に届かなかっただけで内容が乏しいわけではなく、設定リファレンスと権限モードはハイライト 1、エラーリファレンスはハイライト 2 と 4、管理設定のデプロイはハイライト 2、非対話実行はハイライト 3、サブエージェントはハイライト 4 で扱っています）
<!-- light:updated-pages:end -->

## 軽微な更新

<!-- light:minor-updates:start -->
今回も 1 日分の取り込みで、`llms-full.txt` に差分のあったページは 27、差分行は 3 ファイル合計 736 行（`llms-full.txt` 728 行 = 追加 460・削除 268 / ページ見出しマップ 6 行 = 追加 5・削除 1 / `llms.txt` 2 行 = 追加 1・削除 1）です。前回が 12 ページ・187 行だったのに対し、ページ数で 2 倍強、行数で約 4 倍の規模ですが、本サマリで「実質 N 行」と書いた各行の連続空白と連続ハイフンを潰して数え直した概算では `llms-full.txt` の 728 行が 280 行になります。差の大半は設定リファレンス 1 ページ分（生 479 行 → 実質 31 行）で、いずれも冒頭のキー一覧表の桁揃えです。**`llms.txt` は 5 回続いた無差分が途切れました**が、変化は 1 行のみで収録 URL は 202 件、展開ページ数も前後とも 191 で、ページの新規追加・削除はありません（詳細はハイライト 5 参照）。

**changelog には v2.1.260（2026年09月03日）が 1 件加わりました**（69 行すべて追加）。内訳は本体 59 件（追加 6・修正 33・取り消し 1・改善 9・更新 1・変更 8・削除 1）と VS Code 拡張分 7 件（追加 2・修正 5）の計 66 件です。前回扱った v2.1.259 の 37 件と比べて倍近い規模で、修正が半数を占めます。単一リリースのみのため、以下の changelog 由来の項目にはバージョンを個別に併記しません（すべて v2.1.260 です）。

**今回のページ見出しマップの差分は、生成時刻の更新（2026年09月03日 03:11 UTC から 2026年09月04日 00:25 UTC）と 4 件の見出し追加だけ**で、いずれも本文が同時に到着しています。内訳は、非対話実行への `Turn off permission prompts in unattended runs` 追加（ハイライト 3）、エラーリファレンスへの `Managed settings document could not be parsed` 追加（ハイライト 2）、設定リファレンスへの `permissions.blockReadsOutsideWorkingDirectories` 追加（ハイライト 1）、権限モードへの `The first read outside the working directories` 追加（ハイライト 1）です。見出しだけが先に現れて本文が届いていない持ち越しは今回もありません。

なお本サマリの参考リンクは前回に続き全て英語版のみです。今回の変更に日本語版が追従していないためで、本サマリの作成時点で公開中の日本語版ページを実際に取得して確認したところ（本リポジトリに取り込んである `ja/` のスナップショットではなく、`code.claude.com` のライブページを参照しています）、**そもそも日本語版には設定リファレンス（`settings-reference`）のページ自体が存在せず HTTP 404 を返す**（過去のサマリでも日本語版の設定リファレンスにリンクしたことはありません）、**日本語版の権限モードページには「作業ディレクトリ外の初回読み取り」に相当する節が無く、`blockReadsOutsideWorkingDirectories` も一度も登場せず、分類器の判定順の step 2 も旧記述のまま**、**日本語版の非対話実行ページには「無人実行で権限プロンプトをオフにする」に相当する節が無く、`--permission-prompts` も登場しない**、**日本語版のエラーリファレンスには「管理設定の文書をパースできない」に相当する節が無く、応答途切れの節も `Connection closed mid-response` / `Response stalled mid-stream` という旧名称のままで、ケースの列挙自体が無い**ことを確認しました。他のページは個別には確認していませんが、いずれも直近 1〜2 日の変更であるため未追従とみなし、安全側に倒して英語版のみを載せています。

**新機能**

- 作業ディレクトリ外の読み取りを全モードで拒否する `permissions.blockReadsOutsideWorkingDirectories` が加わりました（詳細はハイライト 1 参照）— [English](https://code.claude.com/docs/en/settings-reference#permissions-blockreadsoutsideworkingdirectories)
- フルスクリーンモードで会話の横に開く差分パネルが加わりました。Claude が編集する様子に合わせて未コミットの変更を表示し、`/diff` で切り替えます
- プロンプトキャッシュのミスの推定原因（ツール定義やシステムプロンプトの変更、TTL を超えるアイドルなど）が `/cost` とステータスラインの `prompt_cache` フィールドに加わりました
- `/reload-plugins` がヘッドレスセッションでも使えるようになり、Claude Code Desktop と SDK のコマンド一覧に現れるようになりました
- `/advisor` のテキスト形式（`/advisor`・`/advisor <model>`・`/advisor off`）が、デスクトップアプリ・Remote Control・その他のヘッドレス（`-p` / Agent SDK）セッション向けに加わりました
- Claude apps gateway に `oidc.scope_on_refresh` が加わりました。リフレッシュ時に `openid` を再度要求されたときだけ id\_token を返す IdP 向けです
- Claude apps gateway が `desktop` ポリシーブロックの新しい Claude Desktop キー（`userPluginMarketplacesEnabled` と `userPluginUploadsEnabled` を含む）に対応しました
- VS Code 拡張のフッターのモデルピルに、選択中の effort レベルが表示されるようになりました
- VS Code 拡張のセッション一覧のステータスフィルターメニューに Open と Closed が加わりました

**機能改善**

- 管理設定の文書がパースできない場合に起動を拒否する挙動が、専用のエラー節として文書化されました（詳細はハイライト 2 参照）— [English](https://code.claude.com/docs/en/errors#managed-settings-document-could-not-be-parsed)
- 管理設定のデプロイページで、各ソースがパース失敗と判定される条件と、拒否を起こさない 3 つの状態が整理されました（詳細はハイライト 2 参照）— [English](https://code.claude.com/docs/en/managed-settings#find-entries-claude-code-dropped)
- 設定ページの「壊れた設定ファイルを直す」節に、管理設定の文書がパースできない場合への参照が加わり、`-p` 実行がそれだけは飛ばさず終了することが明記されました（詳細はハイライト 2 参照）— [English](https://code.claude.com/docs/en/settings#fix-a-broken-settings-file)
- 監視ページの保持スイープイベントで、スイープを止める `managed-settings.json` の状態が「読めないか解釈できない」から「**読めない**」に絞られました（詳細はハイライト 2 参照）— [English](https://code.claude.com/docs/en/monitoring-usage#retention-sweep-event)
- 無人実行で権限プロンプトを止める手順が非対話実行ページの独立節になり、`--permission-prompts` が CLI リファレンスのフラグ表にも載りました。フラグ自体は v2.1.259 で追加済みで、前回サマリでは changelog 由来の新機能として 1 行触れていた項目です（詳細はハイライト 3 参照）— [English](https://code.claude.com/docs/en/headless#turn-off-permission-prompts-in-unattended-runs) / [English](https://code.claude.com/docs/en/cli-reference#cli-flags)
- サブエージェントの応答が途中で切れた場合も継続を促すことが、サブエージェント・エラーリファレンス・エンタープライズネットワーク設定の 3 ページに反映されました（詳細はハイライト 4 参照）— [English](https://code.claude.com/docs/en/network-config#streaming-idle-watchdogs)
- 権限ページで、組み込みの読み取り専用 Bash コマンドが全モードでプロンプトなしに走る説明に例外条件が付き、作業ディレクトリの節にも新しい設定への案内が加わりました（詳細はハイライト 1 参照）— [English](https://code.claude.com/docs/en/permissions#read-only-commands)
- サンドボックスのページで、サンドボックス外での再試行の権限フローの説明が整理され、ファイルシステム隔離の節に「パスルールを書く代わりに新しい設定を使え」という案内が加わりました（詳細はハイライト 1 参照）— [English](https://code.claude.com/docs/en/sandboxing#the-unsandboxed-retry-escape-hatch)
- セキュリティページの「作業ディレクトリの境界」の説明から「**auto モードでは尋ねずに読む**」の 1 文が削除されました（詳細はハイライト 1 参照）— [English](https://code.claude.com/docs/en/security#built-in-protections)
- **Claude Fable 5.1 で API キーまたは Claude のサブスクリプションを使っている場合、セッション途中の effort 変更がプロンプトキャッシュを無効にしなくなりました**。Claude Code は確認も求めずに新しいレベルを適用します。ただし Amazon Bedrock・Google Cloud の Agent Platform・Claude apps gateway では適用されず、`CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS` を設定した場合や組織が HIPAA 構成の場合も対象外です（v2.1.260 より前は Fable 5.1 でも無効化されていました）— [English](https://code.claude.com/docs/en/prompt-caching#changing-effort-level)
- 管理された CLAUDE.md（`claudeMd`）がセキュリティ承認ダイアログを要求しなくなりました。Claude Code が実行するコマンドではなく Claude 向けの指示テキストであるためで、その指示に従って Claude が使うツールには引き続き権限チェックが掛かります（v2.1.260 より前は承認が必要でした）— [English](https://code.claude.com/docs/en/server-managed-settings#security-approval-dialogs)
- フックリファレンスの `permission_suggestions` の説明が精緻化されました。この配列は Claude Code が提案する[権限の更新](https://code.claude.com/docs/en/hooks#permission-update-entries)であって、**権限ダイアログに実際に出る「常に許可」の選択肢と 1 対 1 ではない**と明示され、`allowManagedPermissionRulesOnly` がルール保存の選択肢を隠す例と、権限モードを直接変える **Yes, and switch to auto mode** のように提案エントリを持たない選択肢の例が加わりました — [English](https://code.claude.com/docs/en/hooks#permissionrequest-input)
- ゲートウェイ関連 5 ページのリンクテキストが「プロトコルリファレンス」から「互換性ガイド」へ置き換わり、Claude apps gateway の `GET /protocol` が別文書として位置づけ直されました（詳細はハイライト 5 参照）— [English](https://code.claude.com/docs/en/llm-gateway-protocol)
- Workflow の `agent({schema})` が、満たしようのない JSON Schema を事前に拒否するようになり、リトライ上限のエラーに最後の検証失敗が含まれるようになりました
- 未 push のコミットが残る worktree を持つバックグラウンドセッションを削除したときのメッセージが、ブランチ名とコミット数を挙げるようになりました。もう一度削除すると worktree を破棄します
- Claude apps gateway のリフレッシュ失敗のログが、失敗したステップを名指しするようになりました
- 非対話（`-p` / SDK）セッションのアイドル時 CPU 使用率が改善されました
- Amazon Bedrock 上の Claude apps gateway で、中断されたリクエストの入力トークンを 1 トークンのリクエストではなく AWS の無料 CountTokens API で数えるようになりました（`bedrock:CountTokens` の付与が必要です）
- `Edit(C:\dir\(name)\**)` のように `\(` がパス区切りではなくエスケープされた丸括弧として読まれるルールについて、設定エラーが曖昧さのない綴り方を提案するようになりました
- 1M コンテキストのモデルの自動コンパクトが改善され、Opus と Fable のセッションが 1M トークン上限の少し手前でコンパクトするようになり、非常に大きなコンテキストでの復旧コンパクションが 10 分でタイムアウトしなくなりました
- `/ultrareview` と `claude ultrareview` が、長時間かかるクラウドレビューを最大 45 分（従来 30 分）待つようになりました
- 同梱の `claude-api` スキルの Go・Java・C# のサンプルが現行世代のモデル ID を使うようになり、安価なワーカー用・サブエージェント用のモデルも現行世代であるべきことが明確化されました
- フルスクリーンモードの `ctrl+l` / `cmd+k` が、ターミナルの `clear` のようにトランスクリプト表示を消すようになりました（上にスクロールすれば以前のメッセージを見られます）
- 閉じ括弧の後ろに文字がある権限ルール（`Bash(ls) x` など。何にも一致していませんでした）が、黙って無視されるのではなく無効な設定として報告されるようになりました
- Claude in Chrome が組織の Claude in Chrome 管理設定に従うようになりました。管理者がオフにすると `--chrome`・`/chrome`・ブラウザツールが使えなくなります
- Claude apps gateway が `orgPluginSettings` を、Claude Desktop 1.15200.0 以降が読むリスト形式で送るようになりました（それ以前のデスクトップは無視します）
- Claude apps gateway が、`desktop` ポリシーの `managedMcpServers` または `orgPluginSettings` エントリの入れ子オブジェクトでフィールドを綴り間違えている場合にも、そのフィールドを名指しして起動を拒否するようになりました
- `!` の bash モードのプロンプトで打ったコマンドが、strict サンドボックスモード（`sandbox.allowUnsandboxedCommands: false`）が有効でもサンドボックス外で動くようになりました。自分のターミナルに打つのと同じ扱いです
- セルフホストランナーの `--kill-session-after-min` が、ユーザーを待っているだけのセッション（一時停止中で次のメッセージから再開可能）を、kill して失敗と報告するのではなく解放するようになりました
- サブエージェントが開始したバックグラウンドコマンドの 1 時間の制限時間が撤廃されました。メインセッションと同じく、終了するか停止されるまで動きます

**バグ修正**

- **v2.1.259 の変更（`Read()` の拒否ルールを Bash の引数に適用する）が取り消されました**。`Read(./**/build/**)` のルールの下で `npm run build` が全モードで拒否され、`cd … && grep` が auto モードでも確認を求めるようになっていたためです。**前回サマリのバグ修正で「Bash の `Read()` 拒否ルールが、オプションの値として渡されたファイル…を対象にしていなかった問題を修正」として紹介した項目が、これにあたります**
- パスに丸括弧を含む `Edit` / `Write` / `Read` の権限ルールが無効として捨てられる、または Bash のサンドボックスに無視され、「読み取り専用」のはずのフォルダが書き込み可能なままになる問題を修正
- コンパイルできないパターン（閉じていない `[` など）を持つファイル権限ルールが 1 つあると、すべてのファイル編集が `Invalid regular expression` で失敗する問題を修正。そうした拒否ルールは、綴られたリテラルのパスを守るようになりました
- zsh の `REPORTTIME` / `REPORTMEMORY` / `DIRSTACKSIZE` への代入にコマンド置換を隠したコマンドを、Bash の権限チェックが自動承認する問題を修正。承認を求めるようになりました
- 企業のルート CA が OS の証明書ストアにしか無い場合に、Bedrock のモデル探索・トークンカウント・AWS SSO/STS の資格情報呼び出しが `unable to get local issuer certificate` で失敗する問題を修正
- macOS で `permissions.blockReadsOutsideWorkingDirectories` が、サンドボックス化された git からユーザーの git 設定を隠し、worktree で隔離されたサブエージェント自身のチェックアウトも隠す問題を修正
- 以前の `/login` の API キーが残っている claude.ai の Enterprise / Team ユーザーで、管理設定が読み込まれない問題を修正
- `/status` が、サインイン済みの claude.ai アカウントと設定済みの API キーを両方とも有効であるかのように並べる問題を修正。使われていない方に印が付くようになりました
- 同梱スキルのエイリアス（`/doctor` に対する `checkup` など）をキーにした管理 `skillOverrides` のエントリが適用されない問題と、`<dir>:name` の形で列挙された入れ子のスキルを `Skill(name)` の拒否ルールが覆わない問題を修正
- `model: fable` のエージェントが、`ANTHROPIC_DEFAULT_FABLE_MODEL` のピンに付いた `[1m]` タグを無視して黙って 200K のコンテキストウィンドウで動く問題を修正
- `/model` のピッカーが、利用できる組織に対して Fable 5.1 を表示せず、`/model claude-fable-5-1` と打った場合しか受け付けない問題を修正
- Claude Fable 5.1 のプロンプトキャッシュがツール結果の後に付くコンテキストを覆わず、ツール呼び出しのターンごとに未キャッシュの入力として再送される問題を修正
- プラグインのフックの読み込みに失敗すると、以降そのセッション中ずっとモデル切り替えがブロックされる問題を修正。切り替えのたびに再チェックし、拒否するときは原因を名指しするようになりました
- 組織が管理するプラグインのマーケットプレイスが読み込めないと、そのセッション中モデル切り替えがブロックされる問題を修正
- SDK が提供する MCP サーバー（Desktop のコネクタなど）が最初のターンに現れず、次のターンで初めて現れることがある問題を修正
- クラウドホストの claude.ai セッションでコネクタを追加・削除すると、Claude in Chrome のツールがタスクの途中で "Not connected" で失敗する問題を修正
- 旗・結合絵文字・アクセント付き文字が折り返し行をまたいで分割される問題と、旗や結合絵文字がターミナルの最後の 2 桁に来ると古いテキストが画面に残る問題を修正（`…` として表示されるようになりました）
- Remote Control が、有効なモデル名ではないモデル選択を受け付ける問題を修正。次のメッセージで失敗するのではなく、エラーで拒否されるようになりました
- チェックポイントのバックアップファイルが無く実際には何も復元されていないのに、`/rewind` と `--rewind-files` が成功と報告する問題を修正
- `/rewind` が、巻き戻した分のターンのファイル読み取り追跡を残し、外部からの編集のあとに "File unchanged since last read" のスタブとファイル全体の再注入を引き起こす問題を修正
- セッションの worktree ディレクトリが git のメタデータを失うと、（デスクトップアプリが使う）`-p --resume` / `--continue` が再試行のたびに失敗する問題を修正。1 度失敗したあとは worktree 無しで再開するようになりました
- SendMessage で別のエージェントを再開したサブエージェントが、そのエージェントの完了で起こされない問題を修正（通知がメイン会話の方へ行っていました）
- エージェントチームで、長い API 再試行の待ち時間（`CLAUDE_CODE_RETRY_WATCHDOG` の下など）に再試行の通知が実メッセージを追い出し、in-process のチームメイトのトランスクリプトがメッセージを失う・空白になる問題を修正
- バックグラウンドへ移したセッションが ListAgents に 2 回（同名の幻の "interactive" の双子として）現れ、ビューアーで SendMessage の配信を受け取る問題を修正
- 多数のセッションが 1 つのプロジェクトディレクトリを共有するときに、"task output swap refused" エラーが断続的に出る問題を修正
- フルスクリーンでの Ctrl+Z が、一時停止したインターフェースの上に描画された代替スクリーンにシェルを残す問題を修正
- 長いコンテキストコンパクションの実行中に、Workflow ツールのサブエージェントが停止扱いで再起動される問題を修正
- ホストアプリ（Claude Desktop など）がディレクトリとして保存する場合に、URL マーケットプレイスのプラグインが "marketplace entry path does not stay inside the marketplace directory" でインストールに失敗する問題を修正
- claude.ai・デスクトップアプリ・モバイル（Remote Control）から操作しているセッションで Artifact を公開すると、余分なブラウザタブが開く問題を修正
- 一部の Cowork セッションで、Artifact ツールの最初の呼び出しが "Invalid tool parameters" の検証エラーで失敗する問題を修正
- スキルやスラッシュコマンドを実行すると IDE の行選択が落ちる問題を修正（"N lines selected" のコンテキストが Claude に届くようになりました）
- 入れ子のサブグループにある GitLab プロジェクト（`gitlab.com/group/subgroup/project` など）のリポジトリ検出を修正
- GitLab リポジトリで作業しているときに、描画された出力中の `owner/repo#123` というイシュー参照が github.com にリンクする問題を修正。gitlab.com のイシューにリンクするようになりました
- Glob / Grep で、権限チェックの前に検索パスがディスク上で調べられる問題を修正。Read と同様、パスが無いことは権限が決まったあとに報告されるようになりました
- 新しいセッションで Remote Control が自動的にオンになると、VS Code 拡張のウェルカム画面が消える問題を修正
- VS Code 拡張のセッション履歴ピッカーが、既に別のタブで開いているセッションを二度読み込む問題を修正。そのタブに切り替わるようになりました
- VS Code 拡張のセッションタブの Rename コマンドが、そのタブのビューがリロード中だと黙って何もしない問題を修正。常に適用されるようになりました
- 落ちた応答を Claude Code が再試行したあと、書きかけのメッセージ・空のツールカード・余分な "Thought for" 行が VS Code 拡張の画面に残る問題を修正
- 「Enable Remote Control for all sessions」が、トグルを切り替えた時点でまだ起動中だったセッションタブに適用されない問題を修正

**その他**

- advisor ページのリンク先アンカーが `#actions-that-invalidate-the-cache` から `#switching-models` に張り替えられ、文言も「モデルや effort レベルの変更とは違って」から「**モデルの切り替えとは違って**」になりました。effort 変更がキャッシュを保つ場合が生じたことと整合します — [English](https://code.claude.com/docs/en/advisor#impact-on-prompt-caching)
- TypeScript Agent SDK の `supportedCommands()` と `SlashCommand` の説明から「スラッシュ」が外れ、単に「利用可能なコマンド」になりました — [English](https://code.claude.com/docs/en/agent-sdk/typescript#query-object)
- Python Agent SDK の `terminal_reason` の説明で、クエリループを迂回する例が「ローカルのスラッシュコマンド」から「`/voice` や `/usage` などのローカルコマンド」に具体化されました — [English](https://code.claude.com/docs/en/agent-sdk/python#resultmessage)
- Claude apps gateway 設定ページのセキュリティ承認ダイアログの対象一覧から「managed CLAUDE.md content」が削除されました（`claudeMd` が承認不要になったことに対応します）— [English](https://code.claude.com/docs/en/claude-apps-gateway-config#what-goes-in-cli)
- server-managed settings の配信ペイロードの説明から「他の管理ソースと同じルールで寛容にパースされる」の 1 文が削除されました — [English](https://code.claude.com/docs/en/server-managed-settings#invalid-entries-in-delivered-settings)
- 権限ページのサンドボックスの節で、「組み込みの読み取り専用コマンド」に同一ページ内のリンクが付きました — [English](https://code.claude.com/docs/en/permissions#read-only-commands)
- ゲートウェイ概要ページの「次のページ」の案内が、「実装すべきプロトコルがある」から「従うべき互換性ガイドがある」に変わりました（詳細はハイライト 5 参照）— [English](https://code.claude.com/docs/en/gateways#next-steps)
<!-- light:minor-updates:end -->

## 新着情報

<!-- light:whats-new:start -->
（今回の対象期間には `whats-new/` 配下のページに差分がありませんでした。差分のあった 27 ページはいずれもリファレンス・ガイド系です。最新の週間ダイジェストは 3 回前のサマリで扱った Week 34（2026年08月17日～21日）のままで、新しい週のダイジェストの追加も既存ページの訂正もありません。`whats-new/` の無差分は 3 回連続です）
<!-- light:whats-new:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-09-02.md](./archives/latest/2026-09-02.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-09-02.md](./archives/latest-detail/2026-09-02.md)

<!--
base_commit: 2667e8110b59c2cec8b85dd866ec8f529a5fa572
head_commit: 1204f96c5d31ae446075090190d361a2063df414
generated_at_full: 2026-09-04T15:11:03+09:00
-->
