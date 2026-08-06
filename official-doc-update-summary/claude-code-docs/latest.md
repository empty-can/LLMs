---
対象期間: 2026年08月04日 〜 2026年08月05日
作成日: 2026-08-05
---

# Claude Code 公式ドキュメント更新サマリ

```markdown
今回は前回のサマリで「本文の取り込み待ち」としていた節がまとめて集約全文に入り、あわせて changelog に v2.1.222 が 1 本追加されました。自動コンパクトの設定、サンドボックスの認証情報マスク、Windows のフックまわりが中心です。

主要なものを以下に挙げます。

1. 自動コンパクトの発動位置を `/autocompact` コマンド・`--autocompact` フラグ・`autoCompactWindow` 設定で自分で決められるようになった
2. サンドボックスの認証情報ファイルのマスクが本文として解説され、`extract` の書き方や macOS での挙動、AWS の署名の扱いまで分かるようになった
3. v2.1.222 で worktree 分離セッションがメインのチェックアウトを壊せた問題が修正され、エージェント間のメッセージも自動モードの検査対象になった
4. フックが PowerShell ツールに正式対応し、Windows では `Bash` だけをマッチさせたフックが発火しないことが明記された
5. Bash の出力の上限が「出力の上限」という節に整理され、成功時と失敗時で Claude に渡る量が違うことが書かれた
```

## ハイライト

1. [**自動コンパクトのウィンドウを自分で決められるようになった**](./latest-detail.md#1-自動コンパクトのウィンドウを自分で決められるようになった):  
  `/autocompact 500k` のように、コンテキストウィンドウがどこまで埋まったら自動コンパクトを走らせるかを指定できる。コマンド・CLI フラグ・環境変数・設定キーの 4 経路が用意され、優先順位も明文化された。
2. [**サンドボックスの認証情報ファイルのマスクが本文として解説された**](./latest-detail.md#2-サンドボックスの認証情報ファイルのマスクが本文として解説された):  
  `extract` 正規表現でファイルの一部だけをセンチネルに差し替える書き方、`onExtractNoMatch` と `maskDuplicates`、macOS では `deny` 相当になること、AWS の SigV4 署名を守るために 2 つの変数を一緒にマスクすべきことまで書かれた。
3. [**worktree 分離セッションが持っていた穴が塞がれた**](./latest-detail.md#3-worktree-分離セッションが持っていた穴が塞がれた):  
  v2.1.222 で、worktree に分離したセッションとそのサブエージェントがメインのチェックアウトに対して破壊的な git コマンドを実行できた問題が修正された。あわせて自動モードでは `SendMessage` の送信内容も分類器の検査を通る。
4. [**フックが PowerShell ツールに対応した**](./latest-detail.md#4-フックが-powershell-ツールに対応した):  
  `PreToolUse` のマッチ対象に `PowerShell` が加わり、入力スキーマの節も新設された。Windows では `Bash` だけをマッチさせたフックが一切発火しないことが明記された。
5. [**Bash の出力の上限が整理された**](./latest-detail.md#5-bash-の出力の上限が整理された):  
  出力は作業ファイルへ流し込まれ、5 GB を超えるとコマンドが打ち切られる。Claude に渡るのは成功なら約 30,000 文字、失敗なら約 10,000 文字で、どのコマンドの終了コード 1 を成功扱いにするかの一覧も載った。

## 新規追加されたページ

- [**Claude Tag**](./latest-detail.md#1-claude-tag) ([English](https://code.claude.com/docs/en/claude-tag)):  
  Slack のチャンネルに組織共有の `@Claude` を置く Team / Enterprise 向け機能の入口。実際の手順は claude.com 側のドキュメントへ送る 1 画面のページ。
- [**クラウドプロバイダーで GitHub Actions を動かす**](./latest-detail.md#2-クラウドプロバイダーで-github-actions-を動かす) ([English](https://code.claude.com/docs/en/github-actions-cloud-providers)):  
  Amazon Bedrock / Google Cloud の Agent Platform / Microsoft Foundry 経由で GitHub Actions を動かす手順を本体ページから分離。OIDC 連携で長期資格情報を置かない構成。

## 大幅に更新されたページ

- [**Claude Code GitHub Actions**](./latest-detail.md#1-claude-code-github-actions) ([English](https://code.claude.com/docs/en/github-actions)):  
  全面改稿。クラウドプロバイダー編を別ページへ出し、組織展開・アンインストール・GitHub App 権限・起動できる人の条件といった節が新たに立った。
- [**サンドボックス化された Bash ツールを設定する**](./latest-detail.md#2-サンドボックス化された-bash-ツールを設定する) ([English](https://code.claude.com/docs/en/sandboxing)):  
  認証情報ファイルのマスク（ハイライト 2 参照）に加えて、設定を保護する対象に `.mcp.json` が加わり、ファイルシステム分離を切ったときに何が残るかが表に整理された。
- [**フックリファレンス**](./latest-detail.md#3-フックリファレンス) ([English](https://code.claude.com/docs/en/hooks)):  
  PowerShell 対応（ハイライト 4 参照）のほか、クラウドセッションでのフックの出どころと、非同期フックが `-p` の終了時にどうなるかが加わった。
- [**サンドボックス環境を選ぶ**](./latest-detail.md#4-サンドボックス環境を選ぶ) ([English](https://code.claude.com/docs/en/sandbox-environments)):  
  sandbox runtime の節が 3 つに分かれ、必要なパッケージ、許可すべき書き込み先とドメイン、ランタイムが設定なしでブロックするものが具体的に書かれた。
- [**エージェントビューで複数のエージェントを管理する**](./latest-detail.md#5-エージェントビューで複数のエージェントを管理する) ([English](https://code.claude.com/docs/en/agent-view)):  
  バックグラウンドセッションの後始末の方針が箇条書きに整理され、コミットとプッシュは必ず、ドラフト PR はタスクが求めるときだけ、という形になった。

## 軽微な更新

今回の対象期間には changelog に v2.1.222（2026年08月04日）が 1 本追加され、あわせて前回のサマリで「本文の取り込み待ち」としていた節の多くが集約全文に入りました。以下ではハイライトと上記カテゴリに含めなかった変更を挙げます。バージョンの記載がないものは通常ドキュメントページ側の変更です。

**新機能**

- 自動コンパクトのウィンドウを設定する経路として `/autocompact` コマンド、`--autocompact` フラグ、`autoCompactWindow` 設定が加わりました（詳細はハイライト 1 参照）（v2.1.221） — [English](https://code.claude.com/docs/en/cli-reference#cli-flags)
- 認証情報ファイルの `mask` に付随する `extract` / `onExtractNoMatch` / `maskDuplicates` / `injectHosts` の 4 キーが設定リファレンスに載りました（詳細はハイライト 2 参照）（v2.1.221） — [English](https://code.claude.com/docs/en/settings#sandbox-settings)
- VS Code 拡張の Focus view が拡張機能側のドキュメントにも載りました。ツール呼び出し・ツール結果・思考をターンごとの展開可能な 1 行の裏に隠し、あなたのプロンプトと Claude の返答だけを残します。切り替えは設定パネル、`Ctrl+Option+F`（Mac）/ `Ctrl+Alt+F`（Windows・Linux）、コマンドパレットの「Claude Code: Toggle Focus view」のいずれかで、拡張設定のキーは `focusView` です（v2.1.221） — [English](https://code.claude.com/docs/en/vs-code#use-the-prompt-box)
- `disableAutoMode` を `permissions` の下（`permissions.disableAutoMode`）にも書けるようになりました — [English](https://code.claude.com/docs/en/settings#permission-settings)

**機能改善**

- Google Cloud の Agent Platform でのツール検索の既定が、モデル世代で決まるようになりました。Claude Opus 4.5 / Sonnet 4.5 / Haiku 4.5 以降では Anthropic API と同じく既定で有効、それより前のモデルはサービング側がベータヘッダーを拒否するため常に一括読み込みで、`ENABLE_TOOL_SEARCH=true` でも覆せません。従来は全モデルで既定無効でした（v2.1.221） — [English](https://code.claude.com/docs/en/mcp#configure-tool-search)
- `/plugin` からのインストールが、その場でプラグインを有効化できるようになりました。インストールのサマリが `Plugin is now active.` か `Run /reload-plugins to activate.` のどちらを出すかで、`/reload-plugins` が要るかどうかが分かります（後者になるのは、有効化がプロンプトキャッシュを無効化する場合か、有効化の試行が失敗した場合）。カタログにプラグインが無いときも、マーケットプレイスの自動更新が有効ならカタログを 1 度更新してから再試行します（v2.1.221） — [English](https://code.claude.com/docs/en/discover-plugins#install-plugins)
- `/reload-plugins` は、再読み込みがプロンプトキャッシュの全再読み込みを引き起こす場合に警告して止まり、`--force` を付けて再実行すると適用されます — [English](https://code.claude.com/docs/en/prompt-caching#enabling-or-disabling-a-plugin)
- ストリームが途中で切れたときの扱いが書き足されました。Claude がテキストブロックかツール呼び出しを完了させたあとに切れた場合、Claude Code は完了した内容を保持したうえで**完了していたツール呼び出しを実行し、その結果からターンを継続**します（従来は不完全レスポンスの通知を出して終わる、とだけ書かれていました） — [English](https://code.claude.com/docs/en/errors#socket-is-closed)
- fast mode の使用クレジットを使い切ったときの挙動が書かれました。拒否された fast mode のリクエストは標準速度・標準価格で再試行されるためクールダウンはありません。対話セッションでは「Fast mode disabled · usage credits exhausted」の通知が出てそのセッションの間は fast mode が切れます（保存された設定は変わらず、`/fast` で戻せます）。`--output-format stream-json` の非対話モードと Agent SDK では、同じ文言が `notification` サブタイプの `system` メッセージとしてターンごとに 1 回流れ、fast mode は有効なままです（v2.1.221） — [English](https://code.claude.com/docs/en/fast-mode#handle-rate-limits)
- fast mode 非対応モデルへの切り替えの説明が整理され、Opus 4.7 も他の非対応モデルと同じく「切り替えると fast mode がオフになる」に変わりました。従来は Opus 4.7 でだけ fast mode が残り、API がリクエストを拒否する状態でした（v2.1.221） — [English](https://code.claude.com/docs/en/fast-mode#switch-models-while-fast-mode-is-on)
- 組織向け MCP 制御に「ポリシーのエントリがどう展開されるか」の節が加わりました。サーバー側の設定値は生きているプロセス環境から展開されますが、ポリシーのエントリは固定された環境から展開されるため、プロジェクトやユーザーの設定ファイルが設定した変数で許可リストの意味を変えられません。URL エントリのスキーム・ホスト・パス範囲が変わるような展開になった場合、`allowedMcpServers` はエントリを無視し、`deniedMcpServers` はマッチしたままにする（拒否は広がる方向にしか動かない）という非対称も表になっています — [English](https://code.claude.com/docs/en/managed-mcp#how-policy-entries-expand)
- Agent SDK の MCP 接続タイミングが表に整理されました。stdio サーバーとツール一覧のキャッシュがない HTTP/SSE サーバーは接続まで最初のターンを待たせ（タイムアウトは `MCP_TIMEOUT`、既定 30 秒）、キャッシュ済みのリモートサーバーは待たせずキャッシュされたツールを使い、インプロセスの SDK サーバーは決して待たせません。設定ファイル（`.mcp.json` など）から読まれたサーバーはこの待機の対象外で、init メッセージの時点で `pending` に見えるのが普通だ、という注意も加わりました — [English](https://code.claude.com/docs/en/agent-sdk/mcp#connection-timing)
- Agent SDK が同梱バイナリを持たないケースが明記されました。pip がプラットフォームホイールではなくソース配布を入れた場合（ARM64 Windows など）と、TypeScript SDK で `npm ci --omit=optional` のように optional dependencies を飛ばした場合です — [English](https://code.claude.com/docs/en/agent-sdk/quickstart#setup)
- TypeScript SDK の `skills` オプションが、正確なスキル名のみを受け付けることが明記されました。空文字・括弧やカンマや制御文字を含む名前・前後に空白のある名前・`*` や `:*` のようなワイルドカード形は、Claude Code のプロセスを起動する前に `query()` が例外を投げます。すべてのスキルを有効にするならワイルドカードではなく `skills: "all"` を使います — [English](https://code.claude.com/docs/en/agent-sdk/skills#using-skills-with-the-sdk)
- 管理設定の無効エントリの扱いが変わりました。`sandbox.credentials` の `files` / `envVars` で、`path` または `name` と `mask` か `deny` の `mode` が有効なまま `extract` にキャプチャグループが無いといった不備があるエントリは、除去ではなく `mode: "deny"` へ**格下げ**され、直すまで「マスクされない代わりに読めない」状態になります（v2.1.221 より前はすべて除去されていました） — [English](https://code.claude.com/docs/en/settings#invalid-entries-in-managed-settings)
- claude.ai や Claude アプリ、デスクトップアプリでのセッション名の変更が CLI 側の名前にも反映されるようになりました。プロンプトバーの表示と `claude agents` の一覧に同じ名前が出ます（v2.1.221） — [English](https://code.claude.com/docs/en/sessions#name-your-sessions)
- `acceptEdits` モードの PowerShell の説明に、引用符を含む位置指定引数（`Set-Content .\notes.txt "It's done"` のアポストロフィなど）は範囲内のパスでも確認を求める旨が加わりました。引用の有無で読みが変わる引数は静的に検証できないためで、`-Value` のような名前付きパラメータで渡せば確認は出ません — [English](https://code.claude.com/docs/en/permission-modes#auto-approve-file-edits-with-acceptedits-mode)
- 権限モードを切り替えたときに保留中だった分類器の判定は、新しいモードなら要求しなかったはずのものであれば破棄され、代わりに承認を求める（`dontAsk` モードでは自動的に拒否する）ようになりました — [English](https://code.claude.com/docs/en/permission-modes#when-auto-mode-falls-back)
- 非対話セッションでは `help` と `feedback` がターミナル専用の組み込みコマンド名として予約されなくなり、この名前のプラグインスキルがそのままのコマンド名で使えるようになりました（`/login` など他のターミナル専用組み込みの名前は引き続き予約されます） — [English](https://code.claude.com/docs/en/skills#how-a-skill-gets-its-command-name)
- Claude apps gateway が親から渡された `sandbox.credentials` を剥ぎ落として転送することが明記されました。`deny` は `path` / `name` とモードだけ、ファイルの `mask` は `injectHosts` を空にしたファイル全体マスクとして（＝プロキシは親由来のエントリで実値を差し込まない）、`envVars` の `mask` は転送しない、という扱いです — [English](https://code.claude.com/docs/en/claude-apps-gateway#settings-the-locks-dont-cover)
- コードレビューの結果の出しかたの条件が整理されました。ターミナルセッションでの `/code-review`（フォークされたサブエージェントとして走る）と、テキストまたは JSON 出力の `-p` 実行では、ホストアプリが一覧形式を要求していても本文テキストとして報告されます — [English](https://code.claude.com/docs/en/code-review#review-a-diff-locally)
- Claude Code on the web の差分表示が、リポジトリに設定された diff ドライバや `textconv` フィルタを通さず、生の git blob から計算されることが明記されました — [English](https://code.claude.com/docs/en/claude-code-on-the-web#review-changes)
- セキュリティのページの参考文献に「CISO's guide to agentic AI」が加わり、大規模移行の解説（common-workflows）には Anthropic 自身のコード移行事例のブログへのリンクが加わりました — [English](https://code.claude.com/docs/en/security#related-resources)

**バグ修正**

以下はすべて v2.1.222 での修正です。

- worktree に分離したセッションとそのサブエージェントが、メインのチェックアウトに対して破壊的な git コマンドを実行できた問題（詳細はハイライト 3 参照）
- `PreToolUse` の自動許可フックが、バックグラウンドのエージェントタスク（サマリ・コンパクション・リネーム）でツール制限をすり抜ける問題（詳細はハイライト 3 参照）
- Team / Enterprise の `/usage-credits` で、以前の申請が却下されたメンバーに「すでに使用クレジットの申請を送っている」と表示され、新しい申請を送れない問題
- HTTPS プロキシの背後で、起動時の接続チェックがハングしたのちに失敗する問題。API リクエストと同じプロキシ対応のトランスポートを使い、明確なメッセージとともにタイムアウトするようになりました
- 実際には完了していたレスポンスに「Connection closed mid-response」エラーが報告される問題
- `/usage` が MCP サーバーへ使用量を過剰に割り当てる問題。サーバーの取り分は、そのツール結果を実際に消費したリクエストだけを反映するようになりました（従来は 1 度呼んだあとの全ターンが対象でした）
- ブランチをプッシュしたあとに作られたプルリクエスト（GitHub REST API 経由を含む）にセッションがリンクしない問題
- 組織が制限しているとき、`model: opus` のようなサブエージェント・チームメイトのファミリーエイリアスが親のモデルに落ちてしまう問題。同じファミリーで組織が許可している最新のモデルへ段階的に落ちるようになりました
- カスタムの `ANTHROPIC_BASE_URL` を使うゲートウェイで、サーバーの keep-alive ping が届いているのにストリームのアイドルタイムアウトが発火する問題
- セッショントークンが無効なときに、claude.ai のコネクタが「認可が必要」と誤表示される問題。代わりに `/login` のヒントが出るようになりました
- ローカルで使えなくなったツール（MCP サーバーを外したあとなど）のツールエラーが表示されない問題
- `SendMessage` が長いサマリを拒否する問題。文字数上限で送信が失敗せず、切り詰められるようになりました
- サブエージェントのトランスクリプトビューで、スピナーの effort ラベルがサブエージェント自身の `effort:` ではなくセッションの effort を表示する問題
- ファイルウォッチャーがファイルシステムのエラーに当たったときと、ウォッチャーの破棄中に起こるまれなクラッシュ
- `--ax-screen-reader` モードで、バックスペースのたびにスクリーンリーダーが入力行全体を読み直す問題。行末での削除は削除された文字だけをエコーするようになりました
- `CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST` が設定されているとき、ホスト側のモデル選択キーがディスク上の古い `managed-settings.json` に優先されない問題

**その他**

- ultraplan の撤去が集約全文にも及びました。前回のサマリの時点では索引と見出しマップからの削除だけでしたが、今回は本文そのものが集約全文から消え、changelog にも「Removed ultraplan feature」（v2.1.222）が載りました。権限モードのプラン承認の選択肢、Remote Control のトラブルシュート、ターミナル設定のレインボー表示の対象キーワード、機能提供状況の一覧、Claude Code on the web と ultrareview の関連リンク、`remote.defaultEnvironmentId` の説明文からも言及が外れ、コマンド一覧の `/ultraplan` は「Removed. 代わりにプランモードを使う」という記述になりました — [English](https://code.claude.com/docs/en/commands#all-commands)
- 前回のサマリで新規追加ページとして扱った Agent SDK のトラブルシューティングは、今回そのページ本文が集約全文に取り込まれました。内容は前回の記述（公開ページで確認したもの）と一致しています — [English](https://code.claude.com/docs/en/agent-sdk/troubleshooting)
- エラーリファレンスに「Your checkout has no branches」が新設されました。`git init` のあと `git fetch <url>` と `git checkout FETCH_HEAD` を実行したような、コミットはあるがブランチが 1 つも無いチェックアウトは git バンドルにできないため、`/code-review ultra` と `claude ultrareview` はクラウドセッションを始める前にレビューを拒否し、`git checkout -b <name>` を勧めます（v2.1.221 より前は全追跡ファイルをレビューしようとしてアップロードが失敗していました） — [English](https://code.claude.com/docs/en/errors#your-checkout-has-no-branches)
- 環境変数のページは 300 以上の行が再整形されましたが、記述が実際に変わったのは 6 件です。`BASH_MAX_OUTPUT_LENGTH` と `BASH_MAX_TIMEOUT_MS`（ハイライト 5 参照）、`CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` と `CLAUDE_CODE_AUTO_COMPACT_WINDOW`（ハイライト 1 参照）、`CLAUDE_CODE_RESUME_INTERRUPTED_TURN`（v2.1.221 以降は `0` などの falsy 値が尊重されることを追記）、`ENABLE_TOOL_SEARCH`（Google Cloud の Agent Platform の条件をモデル世代で限定）です — [English](https://code.claude.com/docs/en/env-vars#variables)
- ゲートウェイの `model` フィールドが文字列でない場合、`model must be a string` というメッセージとともに 400 で拒否され、上流に届かないことが明記されました（v2.1.221 以降のゲートウェイが必要）— [English](https://code.claude.com/docs/en/claude-apps-gateway-config#managed)
- サブエージェントの組み込みエージェント表で、前回のサマリで指摘した `claude` 行の重複が解消され、1 行に統合されました — [English](https://code.claude.com/docs/en/sub-agents#built-in-subagents)
- プラグインのインストール手順を含む各ページ（プラグインの発見、プラグインマーケットプレイスの作成、スキル、チャンネル、セキュリティガイダンス、Claude Security、大規模コードベース）が、いずれも「インストール後に `/reload-plugins`」から「インストールのサマリが `Run /reload-plugins to activate.` を出したら実行する」という書き方に揃えられました — [English](https://code.claude.com/docs/en/discover-plugins#apply-plugin-changes-without-restarting)
- 見出しマップに現れた以下の新しい節は、本文がまだ集約全文（`llms-full.txt`）に取り込まれていないため、内容の確認は次回以降になります: worktree の「Claude Code がどう分離を強制するか」と 2 つのトラブルシュート項目（「Claude Code が worktree の使用を拒否する」「セッションが自分の worktree の外で再開される」。ハイライト 3 参照） — [English](https://code.claude.com/docs/en/worktrees#how-claude-code-enforces-isolation) 、エージェントビューの「ターミナルを離れずにセッションを切り替える」「セッションを削除すると何が消えるか」、エージェントチームの「エージェント間のメッセージ」、スキルの「Claude Code の外でスキルの frontmatter を使う」、エラーリファレンスの「claude.ai がセッショントークンを拒否した」「Anthropic のサービスに接続できない」「ベースブランチとのマージベースが見つからない」、ネットワーク設定の「ストリームのアイドル監視」、コストの「プランごとの使用量の内訳」「使用量リクエストが失敗したとき」、Remote Control の「組織のコンプライアンスポリシーにより Remote Control を利用できない」
- 見出しマップ上での削除・改称も 2 件あります。サブエージェントのトラブルシュートから「Windows での長いプロンプトの失敗」が消え、Agent SDK のチェックポイントのエラー見出しが `"No file checkpoint found for message"` から `"No file checkpoint found for this message"` に変わりました

## 新着情報

（今回の対象期間では、新着情報ページ（`whats-new/`）に差分がありません。最新は Week 29（2026年07月13日～17日）のままで、Week 30 以降は本サマリ作成時点で未公開です。）

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-08-04.md](./archives/latest/2026-08-04.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-08-04.md](./archives/latest-detail/2026-08-04.md)

<!--
base_commit: 3c3772d127ab7222f3faca08df16f43de88a31fa
head_commit: 2d8e1c4da653076ba8407a1a3ad4fb3b54462e01
generated_at_full: 2026-08-06T15:07:25+09:00
-->
