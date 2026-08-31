---
対象期間: 2026年08月29日 〜 2026年08月30日
作成日: 2026-08-30
---

# Claude Code 公式ドキュメント更新サマリ

```markdown
今回は 1 日分の取り込みで、18 ページに差分がありました。差分行は 2 ファイル合計 165 行（`llms-full.txt` 158 行 / ページ見出しマップ 7 行）で、`llms.txt` は前後で完全に同一（収録 URL 202 件）、展開ページ数も前後とも 191 でページの新規追加・削除はありません。今回も changelog に差分がなく、新機能の追加ではなく既存ページの記述を直す 1 日でした。ページ単位の差分も最大 38 行で、大幅更新に分類できるページはありません。目立つのは「これまで回避策として案内していたものを取り下げる」種類の訂正が 2 件あったことです。

主要なものを以下に挙げます。

1. Bedrock をゲートウェイ越しに使うときの環境変数が「エラーを消すだけで遅くなる」と位置づけを変え、回避策ではなくなった
2. 管理設定のポリシーヘルパーが失敗する条件と、そのとき Claude Code が何をするかが独立した節にまとまった
3. auto モードが使えない理由に「Anthropic がサーバー側で切っている」が加わり、「一時的な障害ではない」という断定が消えた
4. Claude Code がコマンドを構文的に分解できないと、許可ルールの照合も自動バックグラウンド化も効かなくなることが 2 ページで明記された
5. クラウド環境に API 認証情報を追加できるロールが、Team・Enterprise では Owner のみ（Admin は不可）に訂正された
```

## ハイライト

1. [**Bedrock ゲートウェイ経由のストリーミングで回避策の環境変数が推奨されなくなった**](./latest-detail.md#1-bedrock-ゲートウェイ経由のストリーミングで回避策の環境変数が推奨されなくなった):  
  トラブルシュートの節が「ヘッダーを書き換えられた」「落とされた」「落としたうえで SSE に変換した」の 3 分岐に書き直された。従来は 1 番目の場合に `CLAUDE_CODE_DISABLE_BEDROCK_CONTENT_TYPE_GUARD=1` でチェックを飛ばせると案内していたが、今回「エラーが消えるだけで、書き換えられたヘッダーの下ではバイナリボディをデコードしないので遅い非ストリーミング経路に落ちる」と改まった。
2. [**ポリシーヘルパーの失敗条件と挙動が独立した節にまとまった**](./latest-detail.md#2-ポリシーヘルパーの失敗条件と挙動が独立した節にまとまった):  
  設定リファレンスの `policyHelper` 配下に **Helper failures** が新設され、失敗と見なす 5 条件が列挙された。起動時の失敗は Claude Code の起動そのものを拒否し、バックグラウンド更新の失敗は直前に成功したポリシーを保つ、という非対称も明文化されている。
3. [**auto モードが使えない理由にサーバー側の一時停止が加わった**](./latest-detail.md#3-auto-モードが使えない理由にサーバー側の一時停止が加わった):  
  従来「auto モードが使えないと出たら要件のどれかが満たされていない。これは一時的な障害ではない」と書かれていた箇所から、後半の断定が消えた。代わりに Anthropic がサーバー側で切っている場合とサーバーがアカウントに対して拒否した場合が加わり、どちらもセッションが終わるまで戻らないので新しいセッションを開き直せ、と案内される。
4. [**パースできない複合コマンドは許可ルールにも自動バックグラウンド化にも乗らない**](./latest-detail.md#4-パースできない複合コマンドは許可ルールにも自動バックグラウンド化にも乗らない):  
  `npm test &&` のように `&&` や `||` の後ろが空だと許可ルールの照合用にサブコマンドへ分割されず、`Bash(npm *)` では承認されない。`${VAR}` のようなパラメータ展開も同じくパース不能扱いで、`; exit "${PIPESTATUS[0]}"` で終わるコマンドは自動バックグラウンド化されずタイムアウトで止まる。
5. [**クラウド環境の API 認証情報を追加できるのは Owner だけと訂正された**](./latest-detail.md#5-クラウド環境の-api-認証情報を追加できるのは-owner-だけと訂正された):  
  前回サマリで「Admin / Owner が保持する管理者ロールが必要」と報じた要件が、**Team と Enterprise では Owner が持ち Admin は持たない**に訂正された。環境セレクタから共有環境を編集できるロールも「Admin か Owner」から「Owner」に直っている。

## 新規追加されたページ

（今回の対象期間に新規追加・削除されたドキュメントページはありません。`llms-full.txt` に展開されているページ数は前後とも 191 で、`llms.txt` は前後で 1 バイトも変わらず収録 URL も 202 件のままです。`llms.txt` に差分が無いのは前回に続いて 2 回連続です）

## 大幅に更新されたページ

（今回は大幅更新に分類したページがありません。前回同様「実質の差分 50 行以上 かつ 内容の変更を伴うこと」を基準にしていますが、最大の**設定リファレンス**でも 38 行（追加 31・削除 7）で閾値に届きませんでした。同ページの内容はハイライト 2 で扱っています。次点の**権限モード**は差分 30 行ですが、表の桁揃えの差を除いた実質は 14 行で、内容はハイライト 3 のとおりです）

## 軽微な更新

今回は 1 日分の取り込みで、`llms-full.txt` に差分のあったページは 18、差分行は 2 ファイル合計 165 行（`llms-full.txt` 158 行 / ページ見出しマップ 7 行）です。**`llms.txt` には差分がなく**、収録 URL は 202 件、展開ページ数も前後とも 191 で、ページの新規追加・削除はありません。本サマリで「実質 N 行」と書いた値は、各行の連続空白と連続ハイフンを潰したうえで数え直した概算です。

**今回も changelog に差分がありません**。バージョン番号は、各ページの本文が自ら述べているものだけを引いています。

差分のあった 18 ページのうち 12 ページは、ハイライト 1〜5 で扱った変更が中心です。残る 6 ページ（クイックスタート・サンドボックス・フックのガイド・コンピュータ使用・非対話モード・コマンド）の変更と、ハイライトに含めなかった細部を、以下の 4 分類に整理しました。**新機能**に入れた 3 件も、既存の仕組みに条件や節が足されたもので、新しいコマンドやフラグの追加ではありません。

なお本サマリの参考リンクは全て英語版のみです。今回の変更に日本語版が追従していないためで、実際に取得して確認したところ、**日本語版の Amazon Bedrock ページのストリーミングエラーの節は旧記述のまま**（`CLAUDE_CODE_DISABLE_BEDROCK_CONTENT_TYPE_GUARD` を回避策として案内しており、LLM ゲートウェイへの切り替えの段落も無い）、**日本語版の権限モードページには「これは一時的な停止ではありません」がそのまま残っており**サーバー側の言及が無い、**日本語版の権限ページの複合コマンドの節には `&&` の後ろが空の場合の記述が無い**、**日本語版のクラウド環境ページには API 認証情報の節自体が存在しない**（共有環境の節も「オーナーと管理者は」の旧記述のまま）ことを確認しました。他のページは個別には確認していませんが、いずれも直近 1〜2 日の変更であるため未追従とみなし、安全側に倒して英語版のみを載せています。

**新機能**

- 通知フックの `agent_needs_input` の発火条件が広がりました。従来は[エージェントビュー](https://code.claude.com/docs/en/agent-view)を開いている間にバックグラウンドセッションが入力待ちに入ったときだけでしたが、**現在のセッションがエージェントチームのチームメイトの端末セットアップの質問を尋ねていて、6 秒ほど入力が無い**ときにも発火するようになりました（v2.1.248 以降）。フックリファレンスとフックのガイドの双方に同じ追記が入っています — [English](https://code.claude.com/docs/en/hooks#notification)
- コンピュータ使用のページに、**Finder を承認すると Claude がデスクトップ・Dock・Finder ウィンドウをクリックできる**という 1 文が加わりました。アプリのカテゴリによって制御の度合いが変わる（ブラウザと取引プラットフォームは閲覧のみ、ターミナルと IDE はクリックのみ、それ以外は完全な制御）という既存の説明の手前に置かれています — [English](https://code.claude.com/docs/en/computer-use#approve-apps-per-session)
- 設定リファレンスの `policyHelper` 配下に **Helper failures** の節が新設されました（詳細はハイライト 2 参照）— [English](https://code.claude.com/docs/en/settings-reference#helper-failures)

**機能改善**

- `PreToolUse` フックの `updatedInput` の説明に、**Claude Code が権限ルールと Bash コマンドの自動バックグラウンド化の適格性を、Claude が送った入力ではなくフックが返した入力に対して評価する**ことが加わりました（詳細はハイライト 4 参照）— [English](https://code.claude.com/docs/en/hooks#pretooluse-decision-control)
- `CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS` の意味が明確になりました。「最終ターン後の最大待ち時間」ではなく「**連続したアイドル待機の上限**」で、**キューに溜まったバックグラウンド結果を処理するターンが走るたびにカウントは数え直されます**。上限に達した時点で残りのバックグラウンドタスクを待つのをやめて終了します。あわせて v2.1.182 以降が必要である旨も加わり、非対話モードのページ側の説明も「10 分の連続したアイドル待機」に揃いました — [English](https://code.claude.com/docs/en/env-vars#variables)
- サンドボックスの既定の書き込み先の列挙に **`permissions.additionalDirectories` が加わりました**。従来は作業ディレクトリ・`--add-dir` / `/add-dir` で足したディレクトリ・セッションの一時ディレクトリの 3 つを挙げていましたが、設定ファイルの `permissions.additionalDirectories` に書いたディレクトリも同じ扱いだと、サンドボックスのページ 3 か所と設定リファレンス 2 か所で明記されています。列挙の順序も「作業ディレクトリ → 一時ディレクトリ → 追加ディレクトリ」に揃えられました — [English](https://code.claude.com/docs/en/sandboxing#filesystem-isolation)
- ゲートウェイプロトコルの Streaming の節が書き直され、**クライアントが Amazon Bedrock 形式を話す場合は `InvokeModelWithResponseStream` のレスポンスボディと `Content-Type: application/vnd.amazon.eventstream` ヘッダーをそのまま中継し、ストリームを SSE に変換しないこと**が加わりました（詳細はハイライト 1 参照）— [English](https://code.claude.com/docs/en/llm-gateway-protocol#streaming)
- `policyHelper.path` の型が具体化され、**Windows ではドライブレターか UNC のパスで `.exe` で終わる**必要があると明記されました（詳細はハイライト 2 参照）— [English](https://code.claude.com/docs/en/settings-reference#policyhelper-path)
- 管理設定ページの `policyHelper` の箇条書きが、失敗時の挙動を自前で述べる形から **Helper failures 節への参照**に置き換わりました（詳細はハイライト 2 参照）— [English](https://code.claude.com/docs/en/managed-settings#compute-the-policy-with-a-helper-program)
- クイックスタートの初回セッションの説明が緩められました。「**インストール後の最初のセッションでは変更のたびに確認する**」という断定が「**確認された場合は Yes を選ぶ**」になり、インストール直後のセッションの扱いについては環境変数ページの該当節へ誘導する形になっています。auto モードが Pro・Max・Team のターミナルセッションの組み込み既定である（それ以外のプランは Manual）という記述自体は変わっていません — [English](https://code.claude.com/docs/en/quickstart#step-5-make-your-first-code-change)
- 環境変数ページの「インストールやアップグレード後の最初のセッション」の説明が 2 段落に分かれ、**新規インストール直後は `claude -p`・Agent SDK・VS Code 拡張のような非対話セッションなら、開始時の権限モードを決める前に機能フラグを取得できることがある**という書き方に変わりました。「対話ターミナルセッションでは間に合わない」という言い切りは外れています。権限モードのページの開始モード表の該当行も同じ言い回しに揃いました — [English](https://code.claude.com/docs/en/env-vars#first-session-after-an-install-or-upgrade)
- コマンドのページとエラーリファレンスの双方に、**組織のポリシーで無効化されたコマンドは `Unknown command` ではなく独自のメッセージを返すことがある**、と加わりました。従来はプラットフォーム・プラン・認証方法が要件を満たさない場合だけを挙げていました — [English](https://code.claude.com/docs/en/commands#how-the-command-menu-matches-what-you-type)
- **`/` で始まるプロンプトを全てコマンドとして扱うわけではない**ことが明記されました。`/` の次の語が記号で始まる場合（Lean の doc comment を開く `/--` など）やパスの場合（`/var/log/syslog` など）は、通常のメッセージとして Claude に送られます — [English](https://code.claude.com/docs/en/errors#unknown-command)
- auto モードがモードの選択肢に現れる条件の言い回しが「アカウントが要件を満たすとき」から「**auto モードが利用可能なとき**」に、CLI・VS Code・Desktop の各タブと Desktop ページの権限モード表の計 4 か所で統一されました（詳細はハイライト 3 参照）— [English](https://code.claude.com/docs/en/permission-modes#switch-permission-modes)

**その他**

- 使用ポリシー違反の拒否メッセージの説明から、**非対話モード（`-p`）では末尾が `Learn more:` とリンクだけになり `/feedback` の案内が出ない**、という記述が 2 か所とも削除されました。サイバーセキュリティ関連のフラグの節では「見え方はプロバイダーとモードによる」という導入と箇条書き自体が外れ、Amazon Bedrock・Google Cloud の Agent Platform・Microsoft Foundry では使用ポリシー拒否のメッセージになる、という 1 文だけが残っています — [English](https://code.claude.com/docs/en/errors#safety-measures-flagged-a-cybersecurity-topic)
- Amazon Bedrock ページから「**v2.1.208 より前は、同じ設定ミスがレスポンス全体をバッファリングした後の `API Error: Truncated event message received` として現れた**」という注記が外れました。同じ注記はエラーリファレンス側には残っています — [English](https://code.claude.com/docs/en/amazon-bedrock#streaming-errors-behind-a-gateway-or-proxy)
- クイックスタートのインストール手順で、コードフェンス 5 か所の `theme={null}` 属性がそれぞれ **12 個に重複**しました。表示に影響しないメタ属性で、コマンド自体は変わっていません — [English](https://code.claude.com/docs/en/quickstart#step-1-install-claude-code)
- ページ見出しマップ（`claude_code_docs_map.md`）は `llms-full.txt` より新しい断面（生成時刻は 2026年08月29日 18:03 UTC から 2026年08月31日 05:54 UTC へ）を取り込んでおり、**本文がまだ届いていない見出しが 4 つ先行して現れています**。アーティファクトの `Draft a design canvas`、認証の `Sign in without an API key`（`Claude Console authentication` 配下）、設定リファレンスの `modelSettings`、Agent SDK のシステムプロンプト改変ページの `Cache the static part of a custom prompt` です。今回の `llms-full.txt` にはこれらの本文が無いため、内容には触れません（同時に検出された 5 つ目の `Helper failures` だけは本文も届いており、ハイライト 2 で扱いました）

## 新着情報

（今回の対象期間に新着情報ページの追加・更新はありません。Week 34（2026年08月17日～21日）が最新のままです）

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-08-29.md](./archives/latest/2026-08-29.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-08-29.md](./archives/latest-detail/2026-08-29.md)

<!--
base_commit: 7d00c86bee78637a4cc97f3c3affae6dc053ee2d
head_commit: e1ec6a5c1026e78db9ebf5bb0158a1e894a769ad
generated_at_full: 2026-08-31T15:09:45+09:00
-->
