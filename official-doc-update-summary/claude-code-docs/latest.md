---
対象期間: 2026年08月18日 〜 2026年08月19日
作成日: 2026-08-19
---

# Claude Code 公式ドキュメント更新サマリ

```markdown
今回は 1 日分の取り込みで、29 ページに差分がありました。changelog には v2.1.236 と v2.1.237 の 2 リリースが加わっています。新規ページ・削除ページはなく、既にある機能の解説を厚くする更新が中心です。

主要なものを以下に挙げます。

1. 新しいセッションが始まるモデルを指定する環境変数が加わった
2. ファイルの変更を書き手によらず捕捉する FileChanged フックの解説が大幅に増えた
3. スキル・サブエージェント・コマンドのフロントマターを検証する手順が整理された
4. プロジェクトディレクトリ名を自分で決める設定の解説が 7 ページに展開された
5. 出力リダイレクトの宛先がファイル書き込みとして検査されることが明記された
```

## ハイライト

1. [**新しいセッションの既定モデルを指定する環境変数**](./latest-detail.md#1-新しいセッションの既定モデルを指定する環境変数):  
  `ANTHROPIC_DEFAULT_MODEL` が v2.1.236 で加わった。`ANTHROPIC_MODEL` と違って `/model` の選択に上書きされるため、組織や個人が「始点」だけを決められる。
2. [**ファイルの変更を書き手によらず捕捉する FileChanged フックの拡充**](./latest-detail.md#2-ファイルの変更を書き手によらず捕捉する-filechanged-フックの拡充):  
  `Edit`・`Write` のマッチャーでは取りこぼす変更を拾う手段として FileChanged が位置づけ直され、実例・監視リストの動的更新・無限ループの避け方が加わった。
3. [**スキルやサブエージェントのフロントマターを検証する手順の整備**](./latest-detail.md#3-スキルやサブエージェントのフロントマターを検証する手順の整備):  
  `claude plugin validate` にマニフェストの無いディレクトリを指定できることが表で整理され、Claude Code が黙って読み飛ばすサブエージェントファイルの条件も明文化された。
4. [**プロジェクトディレクトリ名を自分で決める設定の全面的な解説**](./latest-detail.md#4-プロジェクトディレクトリ名を自分で決める設定の全面的な解説):  
  前回の対象期間に名前だけ登場した `CLAUDE_CODE_PROJECT_DIR_NAME` に専用の節ができ、Agent SDK 側を含む 7 ページに参照が張られた。
5. [**出力リダイレクトの宛先がファイル書き込みとして検査される**](./latest-detail.md#5-出力リダイレクトの宛先がファイル書き込みとして検査される):  
  `>`・`>>`・`2>` の宛先が Edit ルール・保護されたパス・作業ディレクトリの検査対象になることが明記された。

## 新規追加されたページ

（今回の対象期間に新規追加されたページはありません。削除されたページもなく、`llms.txt` 自体に差分はありませんでした）

## 大幅に更新されたページ

- [**モデル設定**](./latest-detail.md#1-モデル設定) ([English](https://code.claude.com/docs/en/model-config#set-a-default-model-for-new-sessions)):  
  追加 48 行・削除 17 行で今回唯一の大幅更新。`ANTHROPIC_DEFAULT_MODEL` の新設に伴って既定モデルの決まり方の記述が全体的に整理された（詳細はハイライト 1 参照）。

## 軽微な更新

今回は 1 日分の取り込みをまとめた対象期間で、差分のあったページは 29 です。changelog には v2.1.236（2026年08月19日）と v2.1.237（2026年08月20日）の 2 リリースが加わりました。上記の大幅更新 1 ページを除く 28 ページの変更をここで扱います。なお本サマリの参考リンクは全て英語版のみです。今回変更のあったページは日本語版がまだ追従していないためで、モデル設定・権限・セッションの管理・カスタムサブエージェントの 4 ページを実際に確認したところ、いずれも新設された節が無く、旧記述のままでした。

**新機能**

- `ANTHROPIC_DEFAULT_MODEL` が加わりました。新しいセッションが既定で始まるモデルを指定します（v2.1.236、詳細はハイライト 1 参照）— [English](https://code.claude.com/docs/en/env-vars#variables)
- 組み込みの出力スタイルに **Concise** が加わりました。前置きや実況を省いて結果から述べる一方、作業自体はこれまでと同じだけ丁寧に行うもので、`/config` の Output style から選べます（v2.1.237）
- クロスセッションの `SendMessage` に `notify_when_idle` が加わりました。同じマシンの別セッションに対して、次にアイドルへ入ったときに 1 度だけ知らせるよう頼めます。オプトインの 1 回限りでポーリングはせず、macOS と Linux が対象です（v2.1.236）
- `claude plugin validate` にマニフェストを持たないディレクトリを指定できることが表として整理されました（v2.1.233、詳細はハイライト 3 参照）— [English](https://code.claude.com/docs/en/plugin-marketplaces#validate-a-plugin-or-a-directory-without-a-manifest)
- VS Code 拡張のトランスクリプトにスクリーンリーダー対応が加わりました。返答・権限リクエスト・エラー・状態変化の読み上げと、ターンごとの見出しナビゲーションが使えます（v2.1.236）

**機能改善**

- macOS のサンドボックスで、`**/.env` のようなワイルドカードの読み取り拒否ルールが、読み取りを許可した領域の中でも優先されるようになりました。一致したディレクトリの中身も対象になり、拒否されたファイルの名前を変えても回避できません（v2.1.236）
- 出力リダイレクトの宛先がファイル書き込みとして検査されることが明記されました（詳細はハイライト 5 参照）— [English](https://code.claude.com/docs/en/permissions#redirections)
- 権限プロンプトに 1 回限りの承認しか出ない場合がある理由が加わりました（詳細はハイライト 5 参照）— [English](https://code.claude.com/docs/en/permissions#permission-system)
- `FileChanged` フックの解説が全面的に増補され、`PreToolUse` と `PostToolUse` からの誘導も加わりました（詳細はハイライト 2 参照）— [English](https://code.claude.com/docs/en/hooks#posttooluse)
- フックのガイドでも、編集後にフォーマットする例と `Edit|Write` マッチャーの注記の 2 箇所から `FileChanged` への誘導が加わりました — [English](https://code.claude.com/docs/en/hooks-guide#filter-hooks-with-matchers)
- Claude Code が黙って読み飛ばすサブエージェントファイルの条件が明文化されました（詳細はハイライト 3 参照）— [English](https://code.claude.com/docs/en/sub-agents#subagent-files-claude-code-skips)
- プラグインの有効・無効とプロンプトキャッシュの関係の節が 5 つの小節に分割され、code intelligence プラグインの扱いが加わりました。セッション中に有効にすると、一度でも言語サーバーが使えた時点で LSP ツールはそのセッションの間ずっとリクエストに残り、言語サーバーが落ちても再接続してもツールセットは変わりません — [English](https://code.claude.com/docs/en/prompt-caching#code-intelligence-plugins)
- 上記に対応して、LSP ツール側にも同じ挙動が書かれました。言語サーバーを起動できないファイルへの呼び出しは、ツールを外すのではなくエラー結果を返します。v2.1.235 より前は、全ての言語サーバーが落ちるたびにツールを外し、復旧すると戻していました — [English](https://code.claude.com/docs/en/tools-reference#lsp-tool-behavior)
- `ApiKeySource` 型が、実際に報告される 4 つの値（`ANTHROPIC_API_KEY`・`apiKeyHelper`・`/login managed key`・`none`）を列挙する形に書き換えられ、それぞれ何の鍵かを示す表が付きました。従来の `user`・`project`・`org`・`temporary`・`oauth` は古いコードが通るよう型には残りますが、Claude Code は報告しません（Agent SDK v0.3.234 以降）— [English](https://code.claude.com/docs/en/agent-sdk/typescript#apikeysource)
- `SDKSystemMessage` に `effort` が加わりました。次のリクエストで送るエフォート水準を示しますが、Claude Code が付けるのは Remote Control のクライアント宛ての init メッセージだけで、アプリケーションが読む init メッセージには入りません（Agent SDK v0.3.234 以降）— [English](https://code.claude.com/docs/en/agent-sdk/typescript#sdksystemmessage)
- `SDKMessageOrigin` の peer に `fromMode` が加わりました。デスクトップアプリのようにセッション間のメッセージを中継するホストが、送信側の権限の種別を `bypass` か `prompting` で申告するもので、受信側の受信制御で使われます（Agent SDK v0.3.234 以降）— [English](https://code.claude.com/docs/en/agent-sdk/typescript#peer-origin-fields)
- `ArtifactInput` に `capabilities` と `contract` が加わりました。前者は公開するページが使う実行時の能力の申告で、アカウントが使えない能力を挙げると公開が拒否されます。後者は実行時のバージョンで、省略すれば現状維持、`"latest"` で更新、特定のバージョンを渡せば固定や巻き戻しになります（Agent SDK v0.3.235 以降）— [English](https://code.claude.com/docs/en/agent-sdk/typescript#artifact)
- `BashOutput` の `gitOperation` に、コミットしたブランチを示す `commit.branch`（detached HEAD では付きません、Agent SDK v0.3.227 以降）と、`gh pr reopen` を表す PR の `reopened`（Agent SDK v0.3.234 以降）が加わりました — [English](https://code.claude.com/docs/en/agent-sdk/typescript#bash)
- Python の `ClaudeAgentOptions` に `forward_subagent_text` が加わりました。既定ではサブエージェントの `tool_use` と `tool_result` しか流れませんが、有効にするとテキストと thinking のブロックも流れます — [English](https://code.claude.com/docs/en/agent-sdk/python#claudeagentoptions)
- Python の `get_session_messages()` の戻り値 `SessionMessage` で、`parent_tool_use_id` の型が `None` 固定から `str | None` になり、サブエージェントのメッセージではそれを起動した `Agent` ツールの id が入ることが明記されました。入れ子のサブエージェントの親を示す `parent_agent_id` も加わっています — [English](https://code.claude.com/docs/en/agent-sdk/python#get_session_messages)
- チャンネルへ中継する `input_preview` で、安全に直列化できないフィールドの値が `(value unserializable)` というマーカーに置き換わるようになりました。循環参照や極端に大きな配列が対象で、キー自体と他のフィールドはそのままです（v2.1.234）— [English](https://code.claude.com/docs/en/channels-reference#permission-request-fields)
- Remote Control で接続したデバイスからエフォート水準を設定できるようになりました。`CLAUDE_CODE_EFFORT_LEVEL` で固定している場合はそちらが保たれ、エフォート操作からの変更は拒否されます。選んだ水準はそのセッション限りで、保存された既定は変わりません（v2.1.234）— [English](https://code.claude.com/docs/en/remote-control#what-connected-devices-see)
- 権限モードのページで、Remote Control セッションのモード表示の説明が 3 つの箇条書きに分割され、デスクトップアプリと VS Code 拡張がホストするセッションもターミナルと同じようにモード変更を claude.ai へ報告することが加わりました — [English](https://code.claude.com/docs/en/permission-modes#switch-permission-modes)
- プランモードの承認の選択肢で、bypass permissions を有効にして始めたセッションでの表記が「Yes, and bypass permissions」から「Yes, and switch to BYPASS PERMISSIONS (no further prompts) for this session」に変わりました — [English](https://code.claude.com/docs/en/permission-modes#switch-permission-modes)
- フルスクリーンで選択範囲が残るキーと消えるキーが箇条書きで整理されました。`Esc` や `PgUp` などでは残り、矢印キー・`Enter`・文字入力では消えます。`selection:clear` を割り当てたキーは `Esc` であっても消します — [English](https://code.claude.com/docs/en/fullscreen#use-the-mouse)
- `strictKnownMarketplaces` の `hostPattern` が git の URL の形ごとに整理されました。スキーム付きの URL は URL 中のホスト、`user@host:path` 形式は `@` と `:` の間のホストを使い、それ以外のスキーム無しの形にはホストが無いため `hostPattern` は一致しません。`blockedMarketplaces` の `hostPattern` はより広い形からホストを取るため、ブロックリスト側は一致し得ます。v2.1.234 より前は `strictKnownMarketplaces` 側も git が SSH と見なさない形の一部に一致していました — [English](https://code.claude.com/docs/en/settings#strictknownmarketplaces)
- 設定の `env` の説明が、Claude Code が起動する Bash コマンドやフックなどのプロセスに渡すもの、という書き方に整理されました。あわせて `CLAUDE_CODE_PROJECT_DIR_NAME` を無視する旨が加わっています（v2.1.234、詳細はハイライト 4 参照）— [English](https://code.claude.com/docs/en/settings#available-settings)
- 設定の `availableModels` と `enforceAvailableModels` の説明が、Default の扱いをモデル設定のページへ委ねる形に短くなりました（詳細は大幅更新 1 参照）— [English](https://code.claude.com/docs/en/settings#available-settings)
- 自動メモリの保存先の説明に `CLAUDE_CODE_PROJECT_DIR_NAME` の場合が加わりました（v2.1.234、詳細はハイライト 4 参照）— [English](https://code.claude.com/docs/en/memory#storage-location)
- Agent SDK のマルチテナント隔離・外部ストレージへの永続化・セッションの 3 ページにも、`CLAUDE_CODE_PROJECT_DIR_NAME` を併用した場合の扱いが加わりました（TypeScript Agent SDK v0.3.234 以降、詳細はハイライト 4 参照）— [English](https://code.claude.com/docs/en/agent-sdk/session-storage#the-sessionstore-interface)
- 環境変数のページで、フィーチャーフラグの取得が要る機能を初回セッションで取りこぼす話が、「この一覧の機能」から「フラグで制御される機能」への参照に直されました — [English](https://code.claude.com/docs/en/env-vars#first-session-after-an-install-or-upgrade)
- テレメトリーのツール決定イベントで、`user_temporary` を出す条件の書き方が「『… during this session』の選択肢を選んだとき」から「セッションの残りの間アクセスを許す選択肢を選んだとき」という一般的な表現に変わりました。サブエージェントのページの同趣旨の記述も同様です — [English](https://code.claude.com/docs/en/monitoring-usage#tool-decision-event)
- エラーリファレンスのモデル関連 3 箇所で、設定場所を確かめる案内の参照先が、エラーの節どうしの相互参照からモデル設定のページの優先順位の節へ張り替えられました — [English](https://code.claude.com/docs/en/errors#usage-credits-required-for-1m-context)
- 起動時のパフォーマンスが改善され、セッションカウンターがバックグラウンドで書かれるようになりました（v2.1.236）
- auto モードで、`Monitor` の allow ルールが auto モードの間は脇に置かれ、Monitor のコマンドが Bash のコマンドと同じように審査されるようになりました（v2.1.236）
- Amazon Bedrock・Vertex AI・Foundry の場合とテレメトリーを無効にしている場合の auto モードで、分類器が Claude API と同じ既定（重大度によるスコア付けを含む）を使うようになりました（v2.1.236）
- auto モードの git の状態確認が、リポジトリの `status.showUntrackedFiles=no` 設定によって「きれいな作業ツリー」と誤認させられなくなりました（v2.1.236）
- `/model` のピッカーで、最新モデルの名前だけが強調されるようになりました。強調が一覧の中の恣意的な一部ではなく新しいリリースを指すようにするためです（v2.1.236）
- `/goal` の様子見の間隔が段階的になりました。長く走るバックグラウンド作業の後ろにゴールが止められたままアイドルになったセッションは、30 分後、その後は 1 時間後・2 時間後に自動で確認しに行きます（v2.1.236）— [English](https://code.claude.com/docs/en/goal#background-work-defers-evaluation)
- `/usage` が、Team と Enterprise のメンバーにも利用クレジットの消費の行を表示するようになりました。何も使っていない段階では 0% の行が出ます（v2.1.236）
- print / SDK モードでの SIGTERM が、終了前に中断されたターンや見せかけのツール拒否を記録しなくなりました。実行中のコマンドは従来どおり止まり、終了コードも 143 のままです（v2.1.236）
- コマンドの打ち間違いや、そのセッションで使えないコマンドで `Enter` を押したときに、いちばん近いものを曖昧一致で実行せずその旨を伝えるようになりました。前方一致とエイリアスは従来どおり実行されます（v2.1.236）
- Remote Control が、CLI の終了や端末を閉じた場合に数秒でセッションをオフラインとして扱うようになりました（v2.1.236）
- `SendMessage` が、短時間に集中して送ると受信側の受信箱の許容量を超える場合に、その時点で以降のメッセージを断るようになりました。送信済みと報告しておいて実際には捨てる、ということがなくなります（v2.1.236）
- プロンプトの枠に出るセッションタイトルのチップがフッターの右端に揃えられ、右寄せのフッター項目（ゴールの表示・セッションの状態・バックグラウンドエージェントの状態）と省略された通知が、プロンプト領域と同じ右余白を共有するようになりました（v2.1.236）

**バグ修正**

以下は v2.1.236（2026年08月19日）と v2.1.237（2026年08月20日）の changelog に載った修正です。

- LLM ゲートウェイやカスタムの base URL を使うセッションでプロンプトキャッシュが効かない問題を修正（v2.1.237）
- セッションが移動した先のディレクトリが削除された後に、クリップボードへのコピー・バックグラウンドの整理処理・バックグラウンドセッション・ローカル MCP のログが壊れる問題を修正（v2.1.236、2.1.229 以降）
- フルスクリーンのレンダラーが一度起動に失敗すると以後ずっと失敗する問題を修正し、毎回終了する代わりに従来のレンダラーへ退避するようにした（v2.1.236）
- `/model` のピッカーが端末より高く描かれる問題を修正し、ウィンドウに収まる数だけ表示して残りはスクロールで辿れるようにした（v2.1.236）
- 閉じタグが壊れていてメッセージ本文が summary フィールドに入ってしまった場合に `SendMessage` が拒否される問題を修正（v2.1.236）
- サブプロセスの起動に失敗したとき（Windows 相互運用を無効にした WSL での `powershell.exe` など）に未処理の promise 拒否が出る問題を修正（v2.1.236、2.1.234 の退行）
- 端末をリサイズした後、フルスクリーンで新しく送ったメッセージが次の更新まで表示されないことがある問題を修正（v2.1.236）
- フルスクリーンで、複数行のプロンプトを消した後にプロンプトの上に空白の帯が残る問題と、端末のサイズを変えて戻したときにペインが再描画されない問題を修正（v2.1.236）
- 管理設定の承認プロンプトが起動時に出ないのに最初のキー入力を承認として受け取ってしまうことがある問題を修正（v2.1.236）
- tmux（iTerm の tmux 統合）で端末のタブのタイトルが飛び跳ねる問題を修正し、960 ミリ秒ごとにアニメーションさせるのをやめて文字列が変わったときだけ書くようにした（v2.1.236）
- クラウド環境の一覧が空だったり壊れていたりしたときのエラーが分かりにくい問題を修正（v2.1.236）
- Remote Control を使っている場合に、Fable 5 の初回の利用クレジットの確認が 60 秒無回答で代替モデルを自動選択してしまう問題を修正（v2.1.236）
- `~/.claude.json` にキャッシュされたゲストパスの特典が壊れていると、スピナーのヒントが一切出ずバックグラウンドのエラーが繰り返される問題を修正（v2.1.236）
- SDK / VS Code のセッションで、作業ディレクトリが削除された後にスキルのホットリロードがスキルの変更のたびにエラーを出す問題を修正（v2.1.236、2.1.229 以降）
- 自己ホストのランナーのセッションが、アイドル・退役・起動タイムアウトで解放されたとき、セッション後のフックが終わる前に別のランナーで再開されることがある問題を修正（v2.1.236）
- iTerm2 の一部のフォントサイズで、マスコットの Clawd の目と足が不揃いに描かれる問題を修正（v2.1.236）
- セッションのリキャップが際限なく長くなることがある問題を修正し、自動のものと `/recap` のどちらも 400 文字で単語の切れ目で打ち切るようにした（v2.1.236）

**その他**

- `llms.txt` 自体には差分がありませんでした。今回変わったのは `llms-full.txt` とページ見出しマップの 2 ファイルだけです
- ページ見出しマップの差分は、上記の新設節の追加が中心です。プロンプトキャッシュのプラグインの節の 5 小節、セッションの **Name the project directory yourself**、サブエージェントの **Subagent files Claude Code skips**、マーケットプレイスの **Validate a plugin or a directory without a manifest**、権限の **Redirections**、モデル設定の **Set a default model for new sessions** の 6 箇所です
- `selection:clear` のキーバインドアクションに、v2.1.234 以降が必要である旨が明記されました — [English](https://code.claude.com/docs/en/keybindings#scroll-actions)
- GitHub Actions・サンドボックス環境の選択・Agent SDK のシステムプロンプトの改変・Hooks リファレンスの導入文で、「上記のアプローチ」「これらのチェック」のような前方参照が具体的な語に置き換えられました。内容の変更はありません — [English](https://code.claude.com/docs/en/sandbox-environments#enforce-isolation-across-an-organization)
- プラグインのリファレンスの「よくある問題」の表で、`claude plugin validate` が何を調べるかの説明が具体化され、新設節への参照が付きました（詳細はハイライト 3 参照）— [English](https://code.claude.com/docs/en/plugins-reference#common-issues)

## 新着情報

（今回の対象期間に更新された新着情報ページはありません。前回に続き Week 32 が最新のままです）

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-08-18.md](./archives/latest/2026-08-18.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-08-18.md](./archives/latest-detail/2026-08-18.md)

<!--
base_commit: 32e6ee3566896a4f0a120a5c98b667aea98b22c6
head_commit: a4f51fbfe83670c58f484e3fb81935316a500138
generated_at_full: 2026-08-20T15:00:30+09:00
-->
