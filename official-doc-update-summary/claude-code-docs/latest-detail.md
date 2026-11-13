---
対象期間: 2026年11月11日 〜 2026年11月12日
作成日: 2026-11-12
---

# Claude Code 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
**今回は changelog に v2.1.323（2026年11月12日、294 項目）が積まれ、通常のページからは `subagentStatusLine` の設定とプラグインの既定の設定の記述が外れました。`claude remote-control --settings` の使い方とエラー、管理プラグインが読み込めないときのモデルの切り替え、Alpine と musl の要件、Amazon Bedrock と Agent Platform でモデルが使えなくなったときの説明も書き直されています**。新しいページはなく、`llms.txt` は 2 ページの説明文が替わりました（3 行。URL は 239 のまま）。`llms-full.txt` では 203 ページのうち 68 ページ（changelog を含む）が変わり、生の差分は 1,016 行（追加 628・削除 388）です。うち 251 行は `\_` のようなエスケープが外れた行などの書式だけの変更で、大幅更新は `errors` の 1 ページです。総行数は 127,223 行から 127,463 行に増えました。

主要なものを以下に挙げます。

1. `subagentStatusLine` の設定が `statusline`・`settings-reference` から、プラグインのルートの `settings.json` とマニフェストの `settings` キーの記述が `plugins/components`・`plugins/manifest-reference` から外れた。changelog の v2.1.323 は `subagentStatusLine` の削除と、プラグインの `agent` の設定の非推奨（引き続き効く）を述べている
2. `claude remote-control --settings <file>`（v2.1.321 以降）が `remote-control` のフラグの表に載り、`errors` には、このファイルに問題があるときと、起動後にファイルが変わったときの 2 つの節ができた
3. 管理プラグインかそのフックが読み込めなくても、モデルを切り替えられるようになった（v2.1.323 から）。そのプラグインの PreModelSwitch フックは動かず、読み込めたほかのフックは引き続き切り替えを止められる
4. Alpine と musl のディストリビューションでは、インストールのコマンドに `bash` と `curl`、Claude Code 自体に `bash` か `zsh` が要るだけになり、`libgcc`・`libstdc++`・`ripgrep` と `USE_BUILTIN_RIPGREP=0` の手順が外れた
5. Amazon Bedrock と Agent Platform でセッションのモデルが拒まれたときの説明が書き直され、`/model` で `s` を押して既定を変えずにモデルを替える方法が載った
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**subagentStatusLine の設定とプラグインの既定の設定の記述が外れた**](#1-subagentstatusline-の設定とプラグインの既定の設定の記述が外れた):  
  `statusline` の h2「Subagent status lines」と h3「Task fields」、`settings-reference` の h3「`subagentStatusLine`」が外れました。`plugins/components` からは h3「Default settings」が、`plugins/manifest-reference` からは `settings` キーと `settings.json` の行が外れています。changelog の v2.1.323 は `subagentStatusLine` の設定の削除と、プラグインの `agent` の設定の非推奨を述べ、後者は引き続き効くとしています
2. [**Remote Control に渡す設定ファイルの使い方とエラーが載った**](#2-remote-control-に渡す設定ファイルの使い方とエラーが載った):  
  `remote-control` のフラグの表に `--settings <file>`（v2.1.321 以降）の行ができ、`errors` には、ファイルに問題があって Remote Control が始まらないときと、起動後にファイルが変わってセッションが始まらないときの 2 つの h3 ができました。`claude-projects` には、この設定ファイルの `permissions.defaultMode` でスレッドを別のモードで動かす方法が載っています
3. [**管理プラグインが読み込めなくてもモデルを切り替えられるようになった**](#3-管理プラグインが読み込めなくてもモデルを切り替えられるようになった):  
  `model-config` の「Setting your model」で、管理プラグインかそのフックが読み込めなくてもモデルを切り替えられる、と改められました。そのプラグインの PreModelSwitch フックは動かず、読み込めたほかのフックは切り替えを止められます。v2.1.323 より前の Claude Code がこの場合に切り替えを拒むなら、更新します
4. [**Alpine と musl のディストリビューションで要るパッケージが減った**](#4-alpine-と-musl-のディストリビューションで要るパッケージが減った):  
  `setup` の「Alpine Linux and musl-based distributions」は、インストールのコマンドに `bash` と `curl`、Claude Code 自体に `bash` か `zsh` が要る、という説明になり、`libgcc`・`libstdc++`・`ripgrep` と `USE_BUILTIN_RIPGREP=0` の手順が外れました。`troubleshoot-install` の musl と glibc の取り違えの節も書き直されています
5. [**Bedrock と Agent Platform でモデルが使えなくなったときの説明が書き直された**](#5-bedrock-と-agent-platform-でモデルが使えなくなったときの説明が書き直された):  
  `amazon-bedrock` と `google-vertex-ai` の「When a model is disabled mid-session」が、フォールバックのモデルチェーンの有無で分けて書き直され、作業を続けるには `/model` で使えるモデルの上で `s` を押す（既定は変わらない）、という方法が載りました。`amazon-bedrock` の Mantle の節には、ゲートウェイを通す場合の扱いが加わっています
<!-- light:highlight-list:end -->

## 1. subagentStatusLine の設定とプラグインの既定の設定の記述が外れた

**changelog の v2.1.323 は、`subagentStatusLine` の設定を削除した、と述べています。** サブエージェントの行はいつも既定の見た目になり、このキーが残った設定ファイルもこれまでどおり読み込まれます。同じリリースは、プラグインの `agent` の設定を非推奨にした、とも述べています。この設定は引き続き効き、起動時と `claude plugin list`・`claude plugin validate` で警告を出すようになりました。通常のページからは、この 2 つを扱う記述がまとめて外れています。

- **`statusline`**: h2「Subagent status lines」と h3「Task fields」が外れた（40 行）。エージェントのパネルのサブエージェントの行を自分のコマンドで描き直す設定で、更新のたびに stdin に `tasks` の配列を受け取り、`{"id": "<task id>", "content": "<row body>"}` の行を書き戻す、という説明と、`id`・`agentType`・`tokenCount`・`contextWindowSize` などのフィールドの表が載っていた
- **`settings-reference`**: h3「`subagentStatusLine`」と、設定のインデックスの行が外れた。`allowManagedHooksOnly` の下で管理設定だけから読む設定と、「Status line and file suggestion gates」の対象も、`statusLine` と `fileSuggestion` の 2 つになった。`agent` の項目からは、プラグインの `settings.json` もこのキーを渡せる、という文が外れ、既定の説明も「unset, so the main thread runs as Claude Code's default agent」から「unset」になった
- **`hooks` の「Hook locations」**: `allowManagedHooksOnly` で管理設定に絞られる設定から `subagentStatusLine` が外れた
- **`plugins/components`**: h3「Default settings」が外れた。プラグインのルートの `settings.json` か、マニフェストの `settings` キーに同じオブジェクトを置き、`agent` と `subagentStatusLine` の 2 つのキーを既定にする、という節で、ファイルとマニフェスト・ユーザーの設定・2 つのプラグインのどちらが優先されるかの規則も載っていた。例のプラグインの部品の一覧から「Default settings」が、例の説明から `"agent": "security-reviewer"` の `settings.json` が外れ、「one of every kind of component」という言い方も「these components」に替わった。`llms.txt` のこのページの説明文も、「every other component type」から「other component types」になった
- **`plugins/manifest-reference`**: 「Fields」の表の `settings` の行と h3「`settings`」、「Standard layout」の表の Settings（`settings.json`）の行、例のディレクトリーの `settings.json` が外れた。表の説明と `llms.txt` の説明文も、「every field with its type and default」から「fields with types and defaults」のように、すべてを挙げるという言い方が外れた
- **`errors` の「Path escapes plugin directory」**: 飛ばしたファイルを報告するコンポーネントの名前の一覧から、`settings.json`: `settings` が外れた

プラグインの `agent` の設定について、通常のページからは記述が外れましたが、changelog はこの設定が引き続き効くと述べています。どのページも、日本語版はまだ外れる前の記述のままか、今回の内容になっていることを確かめられなかったので、英語版だけをリンクしています。

- [All settings - Claude Code Docs (English)](https://code.claude.com/docs/en/settings-reference#status-line-and-file-suggestion-gates)
- [Add components to a plugin - Claude Code Docs (English)](https://code.claude.com/docs/en/plugins/components#explore-the-plugin-directory)
- [Plugin manifest reference - Claude Code Docs (English)](https://code.claude.com/docs/en/plugins/manifest-reference#fields)

## 2. Remote Control に渡す設定ファイルの使い方とエラーが載った

**`remote-control` の「Start a Remote Control session」のフラグの表に、`--settings <file>` の行ができました。** サーバーのセッションに JSON の設定ファイルを、`claude --settings` と同じ優先順位で当てます。JSON の文字列ではなくファイルのパスを渡し、Claude Code v2.1.321 以降が要ります。表の後ろの、`remote-control` の前に置いたグローバルなフラグの段落も、`--verbose` や `--model` のような一部のフラグならサーバーは始まり、ほかのフラグでは始まらない、設定ファイルを渡すには `remote-control` の後に `--settings` を置く、という説明になりました（これまでは、`--settings` のようなフラグでは起動を拒み、外すフラグを名指す、としていました）。

**`errors` には 2 つの h3 ができました。**

- **「Remote Control did not start because of the `--settings` file」**: `claude remote-control --settings` に渡したファイルに問題がある場合で、`Error: Remote Control did not start, because sessions would skip part or all of the --settings file ./rc-settings.json: Invalid or malformed JSON` のように出る。メッセージが名指す問題を直し、`claude remote-control` のコマンドをもう一度実行する
- **「The settings file has changed since Remote Control started」**: `claude remote-control` を動かしているターミナルに ``Session failed: Error: The settings file /path/to/settings.json has changed since Remote Control started, so this session did not start. Restart `claude remote-control` to use it as it is now.`` が出たら、セッションは今のファイルからは始まらない。今のファイルを使うには、`claude remote-control` を止めて同じコマンドを実行し直す（それまでのセッションを戻すには「Resume sessions after stopping the server」を参照）。始めたときの設定を保つには、ファイルの中身を元に戻し、`claude remote-control` が終わっていれば実行し直す

「Find your error」の表にもこの 2 つの行が加わりました。`remote-control` の前のフラグを拒む「Not carried over to the sessions Remote Control starts」のメッセージの末尾にも、`` Pass settings with `claude remote-control --settings <file>`. `` が加わっています。

**`claude-projects` の「Run a thread on your own computer」にも、この設定ファイルの使い道が載りました。** スレッドを別のモードで動かすには、`--settings` を付けて `claude remote-control` を始めます。そのファイルか、そのコンピューターの設定の `permissions.defaultMode` で、別のモードを選べます（スレッドは既定では auto モードで動きます）。

changelog の v2.1.321 の、`claude remote-control` への `--settings <file>` の追加（2026年11月09日 版のサマリで changelog の項目として扱ったもの）に対応します。

- [Remote Control でどのデバイスからでもローカルセッションを続ける - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/remote-control#start-a-remote-control-session)
- [Continue local sessions from any device with Remote Control - Claude Code Docs (English)](https://code.claude.com/docs/en/remote-control#start-a-remote-control-session)
- [エラーリファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/errors#remote-control-did-not-start-because-of-the-settings-file)
- [Error reference - Claude Code Docs (English)](https://code.claude.com/docs/en/errors#remote-control-did-not-start-because-of-the-settings-file)
- [Projects で継続中の作業を Claude に調整させる - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/claude-projects#run-a-thread-on-your-own-computer)
- [Let Claude coordinate ongoing work with Projects - Claude Code Docs (English)](https://code.claude.com/docs/en/claude-projects#run-a-thread-on-your-own-computer)

## 3. 管理プラグインが読み込めなくてもモデルを切り替えられるようになった

**`model-config` の「Setting your model」で、管理プラグインと PreModelSwitch フックの段落が書き直されました。** これまでは、組織の管理プラグインがどの PreModelSwitch フックを渡すかを Claude Code が判断できないとき（管理プラグインが読み込めなかったときなど）、確かめないまま切り替えることはせず拒み、試すたびに確かめ直す、としていました。今回は次の説明になっています。

- **切り替えはできる**: 管理プラグインかそのフックが読み込めなくても、モデルを切り替えられる。そのプラグインの PreModelSwitch フックは動かないので、それが止めるはずだった切り替えも進むことがある。読み込めたほかの PreModelSwitch フックは引き続き動き、切り替えを止められる
- **古い版**: v2.1.323 より前の Claude Code が `so organization-managed PreModelSwitch hooks could not be checked` で切り替えを拒むなら、Claude Code を更新する
- **何が失敗したかを見る**: セッションで `/plugin` を実行し、**Errors** のタブを開く。何も挙がっていなければ、シェルから `claude --debug` で新しいセッションを始めて別のモデルに切り替え、debug のログを読む。プラグインを直すか、プラグインの更新で管理者の修正が届いたら、セッションで `/reload-plugins` を実行してフックを動かす

フックが切り替えを止めた理由と対処は「Model switch was blocked by a PreModelSwitch hook」を見る、という案内の文も加わりました。

**`errors` の「Model switch was blocked by a PreModelSwitch hook」も追従しました。** `so organization-managed PreModelSwitch hooks could not be checked` の項目は、v2.1.323 より前の Claude Code は、管理プラグインがどの PreModelSwitch フックを渡すかを判断できないと拒む、という説明になり、拒否を止めるには Claude Code を更新し、失敗したプラグインのフックも動かすにはプラグインを直すか管理者に頼む、詳しくはシェルで `claude --debug` を始めてモデルを切り替え、debug のログを読む、と改められました。これまでは、切り替えを試すたびに確かめ直すので、もう解消した失敗なら止めなくなる、としていました。

changelog の v2.1.323 の項目には、この変更を名指すものは見当たりません。

- [モデル設定 - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/model-config#setting-your-model)
- [Model configuration - Claude Code Docs (English)](https://code.claude.com/docs/en/model-config#setting-your-model)
- [エラーリファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/errors#model-switch-was-blocked-by-a-premodelswitch-hook)
- [Error reference - Claude Code Docs (English)](https://code.claude.com/docs/en/errors#model-switch-was-blocked-by-a-premodelswitch-hook)

## 4. Alpine と musl のディストリビューションで要るパッケージが減った

**`setup` の「Alpine Linux and musl-based distributions」が短くなりました。** Alpine とほかの musl ベースのディストリビューションでは、インストールのコマンドに `bash` と `curl` が、Claude Code 自体に `bash` か `zsh` が要ります。Alpine には `bash` も `curl` も既定で入っていないので、入れるまでインストールのコマンドは `not found` で失敗します。例のコマンドは `apk add bash curl` になりました。

- **外れた手順**: 実行時に `libgcc`・`libstdc++`・`ripgrep` が要る、という説明と、`ripgrep` のために community のリポジトリを `/etc/apk/repositories` に加える手順、`settings.json` の `env` で `USE_BUILTIN_RIPGREP` を `0` にする手順
- **パッケージマネージャーでのインストール**: 「Install with Linux package managers」の Alpine のコマンドが、`apk add claude-code` から `apk add bash claude-code` になった

**`troubleshoot-install` の「Linux musl or glibc binary mismatch」も書き直されました。** インストールの後に出る共有ライブラリのエラーの例が、`libstdc++.so.6`・`libgcc_s.so.1` から `ld-linux-x86-64.so.2`・`ld-linux-aarch64.so.1` になりました。glibc のシステムに musl のクロスコンパイルのパッケージがあるとインストーラーが musl と取り違える、という文は外れています。

- **手順 3**: 本当に musl なら `apk add libgcc libstdc++ ripgrep` を入れる、という手順から、musl なのに glibc のバイナリが入った場合の手順に替わった。インストールを削除し、Alpine では先に「Alpine Linux setup」が挙げるパッケージを入れてから、インストールのコマンドを実行すると、musl のバイナリが入る
- **「Verify the binary works」**: Alpine と musl のディストリビューションへの案内のリンク先が、この節になった

ほかに、`troubleshooting` の「Search and discovery issues」の Alpine のタブから、`apk` がパッケージを見つけられないときの案内が外れ、`claude-apps-gateway-deploy` の「Container image」の、musl のイメージには追加のパッケージが要る（Alpine のセットアップを参照）という説明も、musl のビルドの動的な依存は musl だけ、に改められました。changelog の v2.1.323 の項目には、この変更を名指すものは見当たりません。

- [高度なセットアップ - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/setup#alpine-linux-and-musl-based-distributions)
- [Advanced setup - Claude Code Docs (English)](https://code.claude.com/docs/en/setup#alpine-linux-and-musl-based-distributions)
- [インストールとログインのトラブルシューティング - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/troubleshoot-install#linux-musl-or-glibc-binary-mismatch)
- [Troubleshoot installation and login - Claude Code Docs (English)](https://code.claude.com/docs/en/troubleshoot-install#linux-musl-or-glibc-binary-mismatch)

## 5. Bedrock と Agent Platform でモデルが使えなくなったときの説明が書き直された

**`amazon-bedrock` の「When a model is disabled mid-session」が書き直されました。** Amazon Bedrock がセッションのモデルをアカウントで使えないと拒むと、Claude Code はセッションを別のモデルに切り替え、作業を続けられます。メッセージは `Switched to <fallback> because <model> is not available` で始まります。管理者がモデルを無効にしたときや、最新のモデルがまだアカウントで使えないときに起きます。

- **フォールバックのモデルチェーンがある場合**: 設定したフォールバックに切り替わる
- **チェーンがない場合に要求が失敗するとき**: セッションが固定したモデル・選んだ特定の版・アプリケーション推論プロファイルの ARN にあるとき、Claude Code が試すモデル（「Startup model checks」）がどれも使えないとき。auto モードでは、Amazon Bedrock で auto モードが対応するモデルにだけ切り替える
- **作業を続けるには**: セッションで `/model` を実行し、アカウントで使えるモデルの上で `s` を押す。既定は変わらない。`403` は「AWS authentication failed」として出る
- **切り替えず失敗させるには**: `CLAUDE_CODE_DISABLE_MODEL_ACCESS_FALLBACK=1` を設定する。フォールバックのモデルチェーンを設定しているなら、それも外す

これまでの、起動時のフォールバックと同じモデル（同じ段の前の版から試し、Opus がなければ既定の Sonnet）を試す、という説明と、`AWS authentication failed` にモデルを有効にするヒントが付く、という説明は外れました。changelog の v2.1.323 には、Amazon Bedrock がアカウントにモデルを拒んだときのエラーが、AWS の資格情報の更新ではなくモデルを有効にするよう述べるようになった、という修正があります。

**`google-vertex-ai` の同じ名前の節も同じ形になりました。** Agent Platform がモデルをプロジェクトかリージョンで使えないと拒むと切り替わり、管理者が Model Garden でモデルを無効にしたときや、リージョンでそのモデルが提供されていないときに起きます。作業を続けるには、`/model` でプロジェクトとリージョンで使えるモデルの上で `s` を押します。

**`amazon-bedrock` の Mantle の 2 つの節には、ゲートウェイの扱いが加わりました。**

- **「Run Mantle alongside the Invoke API」**: `CLAUDE_CODE_USE_BEDROCK` と `CLAUDE_CODE_USE_MANTLE` の両方を設定して 2 つのエンドポイントを使う方法が、ゲートウェイなしで接続する場合のもの、と限定された
- **「Mantle endpoint errors」**: モデル ID を名指す `400` の直し方が分かれ、ゲートウェイなしなら Mantle が提供する Mantle の形式の ID を使うか Invoke API と並べて使い、ゲートウェイを通すならどのモデル ID を使うかをその運用者に尋ねる、となった

- [Amazon Bedrock 上の Claude Code - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/amazon-bedrock#when-a-model-is-disabled-mid-session)
- [Claude Code on Amazon Bedrock - Claude Code Docs (English)](https://code.claude.com/docs/en/amazon-bedrock#when-a-model-is-disabled-mid-session)
- [Google Cloud の Agent Platform 上の Claude Code - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/google-vertex-ai#when-a-model-is-disabled-mid-session)
- [Claude Code on Google Cloud's Agent Platform - Claude Code Docs (English)](https://code.claude.com/docs/en/google-vertex-ai#when-a-model-is-disabled-mid-session)

## 新規追加されたページ

<!-- light:new-pages:start -->
（今回の対象期間に新規追加されたドキュメントページはありません。`llms.txt` の URL は 239 のまま、`llms-full.txt` の `Source:` の行も 206、固有のページも 203 のままです。changelog の v2.1.323 は Code Mode の説明のページとして `code-mode` を挙げていますが、このページは今回の `llms.txt`・`llms-full.txt` にはありません）
<!-- light:new-pages:end -->

## 大幅に更新されたページ

<!-- light:updated-pages:start -->
- [**Error reference**](#1-error-reference) ([日本語](https://code.claude.com/docs/ja/errors#stopped-an-oauth-request) / [English](https://code.claude.com/docs/en/errors#stopped-an-oauth-request)):  
  79 行（追加 61・削除 18）が変わりました。うち 18 行は見出しの `\_` のエスケープが外れただけです。OAuth の要求を止めたときと Remote Control の設定ファイルの 3 つの節が加わり、クラウドのセッションで拒まれたホストと、別のターミナルで開いている会話の説明が書き直されました
<!-- light:updated-pages:end -->

**行数の数え方**: `llms-full.txt` の生の差分のハンクを、追加行は head 側、削除行は base 側の `Source:` 行でページに振り分けた値です。ページの並びは変わっていません。今回は書式だけの変更（`\_` のようなエスケープが外れた行など）が多いので、それを除いた行数でも確かめました。`errors` は生の差分で 79 行、エスケープの 9 組（18 行）を除いても 61 行で、どちらでも 50 行を超えます。changelog（426 行）は新しい 1 リリースと、前のリリースの言い換え・エスケープの分なので、これまでどおり「軽微な更新」で扱います。次に多いのは `plugins/components` の 41 行（追加 3・削除 38）、`statusline` の 40 行（削除のみ）、`settings-reference` の 30 行（追加 5・削除 25）で、どれも 50 行に届きません。

## 1. Error reference

**新しい節が 3 つ加わりました。** Remote Control の設定ファイルの 2 つ（「Remote Control did not start because of the `--settings` file」と「The settings file has changed since Remote Control started」）はハイライト 2 のとおりです。もう 1 つは h3「Stopped an OAuth request」です。

- **「Stopped an OAuth request」**: OAuth のエンドポイントがリダイレクトしたので、Claude Code が MCP サーバーの OAuth の要求を止めた、という意味。メッセージは `Stopped an OAuth request, which can hold secrets: https://auth.example.com redirected it to https://other.example.com. Ask the owner of https://auth.example.com to remove that redirect.` と、`Stopped an OAuth request: https://auth.example.com redirected it more than 5 times. Ask the owner of https://auth.example.com to fix those redirects.` の 2 つの形で、どちらも最初のアドレスがリダイレクトを送ったもの。MCP サーバーの運用者のような最初のアドレスを動かす人にリダイレクトを外すか直すよう頼み、`/mcp` からやり直す

「Find your error」の表にも、この 3 つの節への行が加わりました。

**既存の節の変更**は次のとおりです。

- **「Host not allowed in a cloud session」**: 冒頭が、クラウドのセッションかクラウドのスケジュールしたタスクで、`403` か `ENOTFOUND` のような DNS のエラーは、要求したホストがクラウドの環境の許可リストにないことを意味しうる、という説明になった。確かめるにはホストをその一覧と照らし、このヘッダーの付いた `403` ならブロックと確定するが、ブロックされた要求の `403` がすべてこのヘッダーを持つわけではない。これまでは、環境のネットワークのポリシーが外向きの HTTP の要求をブロックした、とだけ述べていた。`routines` の「Environments and network access」も、ブロックされたホストへの要求は `403` と `x-deny-reason: host_not_allowed` で失敗する、から、`403` や `ENOTFOUND` のようなエラーで失敗する（この節へのリンク）、に替わった
- **「This session is running in another terminal」**: 2 つのメッセージの意味が改められた。`running in another terminal` は、バックグラウンドのセッション以外のプロセス（`claude -p` の実行や、`claude --resume` か `/resume` で再開したターミナル）が会話を持っていること、`already open in another running Claude session` は、別のバックグラウンドのセッションが持っていること。これまでは、前者はターミナルが持つ、後者はまだ終わっていないバックグラウンドのセッションのプロセスのような、ほかの非対話の Claude Code のプロセスが持つ、としていた。対処も、前者ならそのターミナルで続けるか、そのプロセスを終えるか終わるのを待ってからやり直す、後者ならそのセッションを使うか止めてからやり直す、と分かれた
- **「Unable to resize image」**: 出るエラーは、例の `2000x2000px` の代わりに `2576x2576px` のような別のピクセルの上限を名指すことがある、という文が加わった
- **auto モードの「`a hook changed this call's input after auto mode reviewed it`」**: 同じ応答の後の呼び出しが拒まれる理由の文が、`another call in this response was changed after auto mode reviewed it, or could not be confirmed unchanged` になった（これまでは `changed` の後に `by a hook` が入っていた）
- **「Model switch was blocked by a PreModelSwitch hook」**: ハイライト 3 のとおり
- **「Not carried over to the sessions Remote Control starts」**: ハイライト 2 のとおり
- **「Path escapes plugin directory」**: ハイライト 1 のとおり、`settings.json` の行が外れた。飛ばす条件の文も言い換えられている
- **書式**: `tool_use.name over 200 characters`・`subagent_type is required`・`CLAUDE_CODE_PROCESS_WRAPPER launcher errors` など 9 つの見出しの `\_` のエスケープが外れた（見出しの文言は同じ）

日本語版は、新しい 3 つの節と「Host not allowed in a cloud session」「Unable to resize image」「Model switch was blocked by a PreModelSwitch hook」「Not carried over to the sessions Remote Control starts」が今回の内容になっていることを確かめました。「Path escapes plugin directory」はまだ `settings.json` の行が残り、「This session is running in another terminal」は確かめられませんでした。

- [エラーリファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/errors#stopped-an-oauth-request)
- [Error reference - Claude Code Docs (English)](https://code.claude.com/docs/en/errors#stopped-an-oauth-request)
- [エラーリファレンス - Claude Code Docs (日本語)](https://code.claude.com/docs/ja/errors#host-not-allowed-in-a-cloud-session)
- [Error reference - Claude Code Docs (English)](https://code.claude.com/docs/en/errors#host-not-allowed-in-a-cloud-session)
- [Error reference - Claude Code Docs (English)](https://code.claude.com/docs/en/errors#this-session-is-running-in-another-terminal)

## 軽微な更新

<!-- light:minor-updates:start -->
今回の差分は **3 ファイル**（`llms.txt`・`llms-full.txt`・見出しマップ）です。`llms.txt` は `plugins/components` と `plugins/manifest-reference`（2 か所に載る）の説明文が替わった 3 行で、URL は 239 のままです。`llms-full.txt` では、203 ページのうち **68 ページ**（changelog を含む）が変わり、生の差分は 1,016 行（追加 628・削除 388）でした。2 回展開されている `plugins/create` と `plugins/mods/overview` は、両方の写しが同じように変わっています（下の行数は両方の写しを数えた値です）。大幅更新の `errors` を除く **67 ページ**と、changelog に加わった **v2.1.323（2026年11月12日、294 項目。Added 27・Changed 51・Improvements 21・Bug fixes 195）** を以下にまとめます。単一のリリースなので、各項目への版の併記は省いています。

`llms-full.txt` の総行数は **127,223 行から 127,463 行へ 240 行増え**ました（生の差分の差し引き 628 − 388 と一致）。生の差分 1,016 行をハンクの単位で分けると、changelog の新しいリリースが 310 行、書式だけのハンクが 251 行（`\_` などのエスケープが外れた行の置き換え 212 行、`&#xA;` が入った行の置き換え 25 行、`quickstart` の `theme={null}` の重複の解消 10 行、`cli-reference` の空白 4 行）、残りの 455 行が文面の変更を含むハンクです（changelog の前のリリースの 6 行と、changelog を除くページの 449 行。前者の 2 行はエスケープだけの行です）。書式だけの変更しかないページは 21 あります（下の「その他」）。changelog の収録リリースは 439 から 440 になり、先頭は v2.1.323 です。

コードフェンスの外の見出しは、引用の中の見出しも数えると 6,082 から 6,080 へ、行頭が `#` の見出しだけを数えると 6,071 から 6,069 へ、どちらも 2 減りました。加わったのは `errors` の 3 つ（「Stopped an OAuth request」「Remote Control did not start because of the `--settings` file」「The settings file has changed since Remote Control started」）、外れたのは 5 つ（`plugins/components` の「Default settings」、`plugins/manifest-reference` の「`settings`」、`settings-reference` の「`subagentStatusLine`」、`statusline` の「Subagent status lines」と「Task fields」）です。このほか 11 の見出し（`errors` の 9 つと、`agent-sdk/python` の「Why use setting_sources」、`agent-sdk/troubleshooting` の「structured_output is None but the result says success」）は `\_` のエスケープが外れただけで、文言は替わっていません。

**新機能**

- Remote Control に渡す設定ファイル `claude remote-control --settings <file>` の説明とエラー（`remote-control`・`errors`・`claude-projects`。詳細はハイライト 2 参照）
- OAuth の要求を止めたときのエラー「Stopped an OAuth request」（`errors`。詳細は大幅更新 1 参照）
- **`ctrl+x` の既定の組み合わせが 5 つ増えた**（`keybindings` の「Unbind default shortcuts」）。`Chat` のコンテキストの組み合わせに `ctrl+x ctrl+=`・`ctrl+x ctrl+-`・`ctrl+x ctrl+_`・`ctrl+x =`・`ctrl+x -` が加わり、`ctrl+x` を単独のキーとして取り戻す例でも、この 5 つを `null` にする行が加わりました。各組み合わせが何をするかは、このページには載っていません — [日本語](https://code.claude.com/docs/ja/keybindings#unbind-default-shortcuts) / [English](https://code.claude.com/docs/en/keybindings#unbind-default-shortcuts)
- Code Mode を追加。Claude がツールを呼ぶ JavaScript を書く、実験的なオプトインの機能です。オンにする方法と組織でオフにする方法は `code-mode` のページにある、としています（このページは今回の `llms.txt`・`llms-full.txt` にはありません）
- `plugin.json` に `engines["claude-code"]` を追加。記載した Claude Code の版の範囲から外れたプラグインはインストール・更新・読み込みされず、インストールと更新は範囲に合う最新の版を選びます
- `claude plugin validate` に、プラグインの TypeScript のフックモジュールの型検査を追加。各指摘は警告で、`--strict` では失敗になります
- `claude plugin validate` の対象に、mod の `engine.create` フックが追加・保留・置き換える `$` の名詞を追加
- サードパーティのプロバイダーの Claude Desktop のセッション向けに、managed settings の `CLAUDE_CODE_AUTO_MODE_MODEL` に対応（Claude Desktop がこの版を含むと効きます）
- モデルが要する使用量クレジットがオフか使い切ったとき、選択肢のメニュー（停止・使用量クレジットへの切り替え・アップグレード）を追加
- `claude -p` と SDK のセッションでフックが長く動く間、30 秒ごとの進捗のハートビートを追加。Claude Desktop のようなホストが、ターンを止まったものとして終わらせなくなります（ホストがこの版を含むと効きます）
- Artifact ツールのアセットのアップロードに `.docx` の対応を追加
- diff のパネルに `/diff to close` のヒントを、`?` のショートカットのガイドにパネルにフォーカスするキーと閉じるキーを追加
- `Bash(PORT=* npm run dev)` のように変数の値に `*` を含む Bash の allow ルールに、起動時の警告を追加
- プラグインの言語サーバーが起動できないとき、サーバーの名前と確かめることを示す警告を追加
- Perforce の設定が見つかり、モードがオフのとき、`CLAUDE_CODE_PERFORCE_MODE` を名指す 1 回だけの起動時の通知を追加
- `CLAUDE_CODE_DISABLE_AGENT_PROGRESS_SUMMARIES` を追加（2.1.318 から使えた）。`1` にすると、サブエージェントの進捗の要約と、それを書くための要求がオフになります（anthropics/claude-code#86879）
- `CLAUDE_CODE_RESUME_HINT_COMMAND` を追加。Claude Code を起動するプログラムがこれを設定すると、終了時のヒントにそのプログラム自身の再開のコマンドが出ます
- `claude plugin install --json` の結果に `unsetOptionCount` を追加。まだ設定されていない `userConfig` のオプションの数です
- mod のペインを描くときの props に `isPromptCovered` を追加。ダイアログかプロンプトの上の欄がプロンプトを覆っていることを伝えます
- [VSCode] まだ信頼していないフォルダーでの最初のセッションの前に、Claude Code の信頼の確認を追加。断ると、そのフォルダーの設定と MCP サーバーは使われません
- [VSCode] 実行中の Bash か PowerShell のコマンドのライブの出力を、チャットのコマンドのカードの下に追加
- [Claude Code on the web] スケジュールしたタスクの設定が実行する場所で使えないサンドボックスを要求するため実行を始められないときの、失敗の通知を追加
- [Claude Code on the web] セルフホストの環境の新しいセッションのリポジトリのピッカーに、No repository の選択肢を追加
- [Claude Code on the web] クラウドのセッションの削除のダイアログに、削除するとそのセッションで動くスケジュールしたタスクが一時停止するときの警告を追加
- [Remote Control] セッションを動かすコンピューターが Claude Code からサインアウトしているときに出るエラーに、Try again のボタンを追加
- [Claude Tag] Enterprise のプランで、Slack で始めた Claude Tag のセッションを Compliance API に追加（ベータ）。セッションを一覧し、トランスクリプトを読めます
- [Claude Tag] 管理者が組織の Claude Tag をオフにするときの確認の手順を追加。何が止まるかを述べるダイアログが出ます
- [Claude Tag] Slack のチャンネルの Configure のページに、設定の読み込みに失敗したときの Retry のボタンを追加
- [Claude Tag] Claude Tag の Activity のページの Network events のタブに Scope のフィルターを追加。管理者は組織全体ではなく 1 つのスコープのイベントをダウンロードできます
- [Code Review] Code Review の管理の設定に Download CSV のボタンを追加。レビューの費用を、リポジトリごとに月・週・日の単位で、1 つのリポジトリ・1 つの GitHub の組織・すべてについてエクスポートします

**機能改善**

- 管理プラグインが読み込めないときのモデルの切り替え（`model-config`・`errors`。詳細はハイライト 3 参照）
- Alpine と musl のディストリビューションの要件（`setup`・`troubleshoot-install`・`troubleshooting`・`claude-apps-gateway-deploy`。詳細はハイライト 4 参照）
- Amazon Bedrock と Agent Platform でモデルが使えなくなったときの扱いと、Mantle のゲートウェイの扱い（`amazon-bedrock`・`google-vertex-ai`。詳細はハイライト 5 参照）
- クラウドのセッションで拒まれたホスト・別のターミナルで開いている会話・画像の縮小のエラー（`errors`・`routines`。詳細は大幅更新 1 参照）
- **`ConfigChange` フックを動かさない変更が一覧になった**（`hooks` の「ConfigChange」・`settings` の「When edits take effect」）。フックを動かさずに効く変更に、**Yes, and don't ask again**・`/permissions`・`/model` で保存したルールと設定（保存したセッションの中で。同じファイルを読むほかの開いているセッションではフックが動く）が加わり、server-managed settings・macOS の managed preferences・Windows のレジストリのポリシーの更新と、WSL で `wslInheritsWindowsSettings` を使うときの Windows 側の managed settings のファイルの変更が、同じ一覧にまとまりました。`settings` でも、`ConfigChange` フックは、検出した設定ファイルの変更ごとにではなく、設定ファイルへの直接の編集で動く、と改められています — [日本語](https://code.claude.com/docs/ja/hooks#configchange) / [English](https://code.claude.com/docs/en/hooks#configchange)、[日本語](https://code.claude.com/docs/ja/settings#when-edits-take-effect) / [English](https://code.claude.com/docs/en/settings#when-edits-take-effect)
- **plan の承認の確認では `Shift+Tab` が計画を承認すると載った**（`interactive-mode` の「General controls」・`permission-modes` の「Analyze before you edit with plan mode」）。`Shift+Tab` の行に、plan の承認の確認では計画を承認する、と加わり、モードの巡回の説明も、`default`（表示は Manual）・`acceptEdits`・`plan` の後に、使える場合は `bypassPermissions` と `auto`、と書き直されました（`auto` から最初に押すと `default` になる、という文は外れています）。`permission-modes` でも、承認の確認が開いていなければ `Shift+Tab` で plan モードを抜け、承認の確認では `Shift+Tab` が計画を承認するので先に `Esc` を押す、となりました — [日本語](https://code.claude.com/docs/ja/interactive-mode#general-controls) / [English](https://code.claude.com/docs/en/interactive-mode#general-controls)、[日本語](https://code.claude.com/docs/ja/permission-modes#analyze-before-you-edit-with-plan-mode) / [English](https://code.claude.com/docs/en/permission-modes#analyze-before-you-edit-with-plan-mode)
- **Linux と WSL2 では、まだないパスの書き込みの許可は効かないと載った**（`sandboxing` の「Configure sandboxing」・`settings-reference` の「`sandbox.filesystem.allowWrite`」）。先にそのパスを作ります。`sandboxing` の「Which settings can disable it」では、`filesystem.disabled` を設定できる場所の説明から、チェックアウトしたプロジェクトがオフにできないように、のような理由の言葉が外れています。`settings-reference` は、日本語版がこの内容になっていることを確かめられなかったので、英語版だけをリンクしています — [日本語](https://code.claude.com/docs/ja/sandboxing#configure-sandboxing) / [English](https://code.claude.com/docs/en/sandboxing#configure-sandboxing)、[English](https://code.claude.com/docs/en/settings-reference#sandbox-filesystem-allowwrite)
- **Desktop のスケジュールしたタスクで、管理者が設定したモデルの表示が載った**（`desktop-scheduled-tasks` の「Create a scheduled task」と「Manage scheduled tasks」）。手順 8 が権限モードとモデルの 2 項目に分かれ、モデルのメニューが **Default · Set by admin** で、ほかのモデルを選ばなければ、実行は組織が managed settings で設定したモデルを使う、と加わりました。アプリを開いたときに始まる取りこぼしの実行は、アカウントの実行時の既定を使うことがあります。**Default · Set by admin** がどのモデルかは、詳細のページで **Run now** を押して実行し、その実行のセッションのプロンプトの欄の下の行で確かめます。ディスクの `SKILL.md` にないものの一覧からはモデルが外れました（スケジュール・フォルダー・有効かどうか） — [日本語](https://code.claude.com/docs/ja/desktop-scheduled-tasks#create-a-scheduled-task) / [English](https://code.claude.com/docs/en/desktop-scheduled-tasks#create-a-scheduled-task)
- **Microsoft Foundry の組み込みのロールの名前が `Foundry User` になった**（`microsoft-foundry` の「Azure RBAC configuration」・`github-actions-cloud-providers`・`claude-apps-gateway-config` の「Microsoft Foundry」）。Microsoft Entra ID かそれが発行したベアラートークンで認証するなら、Foundry のリソースで `Foundry User` か `Cognitive Services User` のロールを割り当てます。`Foundry User` は前の名前の `Azure AI User` で見えることもあります。`Microsoft.CognitiveServices/accounts/providers/*` のカスタムロールの JSON の例は外れ、カスタムロールは Microsoft の RBAC の文書（リンク先も替わった）を見る、となりました。`github-actions-cloud-providers` と `claude-apps-gateway-config` の RBAC の行も `Foundry User` になっています — [日本語](https://code.claude.com/docs/ja/microsoft-foundry#azure-rbac-configuration) / [English](https://code.claude.com/docs/en/microsoft-foundry#azure-rbac-configuration)、[日本語](https://code.claude.com/docs/ja/github-actions-cloud-providers#set-up-the-integration) / [English](https://code.claude.com/docs/en/github-actions-cloud-providers#set-up-the-integration)
- **Claude apps gateway で `fable` の別名を使うための `models` の項目が載った**（`claude-apps-gateway-config` の「`models`」）。`auto_include_builtin_models: false` で開発者に `fable` を使わせるには、`models` に `claude-fable-5` の項目を加えます。ゲートウェイにサインインした開発者では `fable` がこの ID に解決されるためで、ないとメッセージは `API Error: 400 model claude-fable-5 is not in the operator's model allowlist` で始まるエラーで失敗します。「`managed`」の、和集合を取る deny のリストとフックの配列は入れ子の一覧に書き直され、組織全体の deny や監査のフックが役割ごとの上書きで落ちないように、という理由の文は外れています — [日本語](https://code.claude.com/docs/ja/claude-apps-gateway-config#models) / [English](https://code.claude.com/docs/en/claude-apps-gateway-config#models)
- **ゲートウェイへのサインインとプロキシの条件が書き直された**（`claude-apps-gateway` の「Prerequisites」・`gateways` の「Configure separately from the gateway」）。表の Private-network address の行が短くなり、表の後ろに、`HTTPS_PROXY` か `HTTP_PROXY` がゲートウェイのホストに当たるとき、サインインには、ホスト名がプライベートのアドレスに解決されるプロキシか、開発者のマシンの `NO_PROXY` のゲートウェイのホストが要る、という段落ができました。それらのマシンが `no_proxy` も設定しているなら、そこにもゲートウェイのホストを加えないと、モデルの要求はプロキシを通り続けます。`gateways` の Corporate HTTP proxies の項目も同じ条件の言い方になりました — [日本語](https://code.claude.com/docs/ja/claude-apps-gateway#prerequisites) / [English](https://code.claude.com/docs/en/claude-apps-gateway#prerequisites)
- **LLM ゲートウェイの後ろの `/feedback` と、認証のエラーの見分け方が載った**（`llm-gateway-connect` の「Troubleshoot gateway errors」・`llm-gateway-rollout`）。`ANTHROPIC_BASE_URL` を使うセッションで `/feedback` がローカルのファイルを保存する、という行が加わりました。ゲートウェイの後ろの `ANTHROPIC_AUTH_TOKEN` と、Anthropic の API キーの形式でないキーは Anthropic の資格情報ではないので、Claude Code は報告を `~/.claude/feedback-bundles/` の下のローカルのアーカイブに書きます。そのファイルを Anthropic のアカウントの担当者に送るか、サポートの要求に添付します。「Conflicts with an existing login」と表の最初の行は短く言い換えられました。`llm-gateway-rollout` では、`Not logged in` の項目に、ゲートウェイのログに `api.anthropic.com` かプロバイダーのエンドポイントからの `401` があれば、ゲートウェイが持つプロバイダーの資格情報を直す、と加わり、「Verify the rollout」の症状の一覧も、`Please run /login · API Error: 401`・`Not logged in`・`Invalid API key` とゲートウェイのログの `401` から、誰が `401` を書いたかを確かめる、という形に書き直されています — [日本語](https://code.claude.com/docs/ja/llm-gateway-connect#troubleshoot-gateway-errors) / [English](https://code.claude.com/docs/en/llm-gateway-connect#troubleshoot-gateway-errors)、[日本語](https://code.claude.com/docs/ja/llm-gateway-rollout#test-claude-code-against-the-gateway) / [English](https://code.claude.com/docs/en/llm-gateway-rollout#test-claude-code-against-the-gateway)、[日本語](https://code.claude.com/docs/ja/llm-gateway-rollout#verify-the-rollout) / [English](https://code.claude.com/docs/en/llm-gateway-rollout#verify-the-rollout)
- **コンパクトの後はプロジェクトのコンテキストのキャッシュも作り直されると載った**（`prompt-caching` の「Compacting the conversation」）。プロジェクトのコンテキストは会話と一緒にキャッシュされるので、`/compact` か自動のコンパクトの後は、ファイルが変わっていなくてもそのキャッシュが作り直されます。これまでは、CLAUDE.md とメモリーがセッションの開始から変わっていなければキャッシュから読む、としていました。システムプロンプトとプロジェクトのコンテキストの層はキャッシュに残りうる、という導入の文も外れ、「How the cache is organized」の、会話の層への「変更」も「追加」に改められています — [日本語](https://code.claude.com/docs/ja/prompt-caching#compacting-the-conversation) / [English](https://code.claude.com/docs/en/prompt-caching#compacting-the-conversation)
- **表にない組み込みの mod の調べ方が載った**（`plugins/mods/overview` の「Mods built into Claude Code」、2 つの写し）。表は **Built-in** の項目の「一部」を挙げるものになり、表にない **Built-in** のプラグインは `/plugin` で詳細を開き、何をするかを読むか無効にします。表の最後の列が各 mod の止め方を述べる、という文は外れました — [日本語](https://code.claude.com/docs/ja/plugins/mods/overview#mods-built-into-claude-code) / [English](https://code.claude.com/docs/en/plugins/mods/overview#mods-built-into-claude-code)
- **フックの例のコマンドが、ファイルのパスを変数で受ける形になった**（`hooks-guide`・`best-practices` の「Enforce steps with hooks」・`plugins/create` の 2 つの写し・`hooks` の「WorktreeRemove」）。`hooks-guide` の `jq -r '.tool_input.file_path' | xargs npx prettier --write` や `plugins/create` の `jq -r '.tool_input.file_path' | xargs npm run lint:fix` のように `xargs` に渡していた例と、`best-practices` で `npx prettier --write --ignore-unknown \"$(jq -r '.tool_input.file_path')\"` のようにコマンドの中で置換していた例が、`f=$(jq -r '.tool_input.file_path') && npx prettier --write --ignore-unknown \"$f\"` のように変数に受けて引用符で渡す形になりました（JSON の中の表記。`plugins/create` は `npm run lint:fix -- \"$f\"`）。`hooks` の WorktreeRemove の例も、`bash -c 'p=$(jq -er .worktree_path) && rm -rf -- \"$p\"'` になっています。`hooks-guide` の「Audit configuration changes」では、監査のログに追記するものが「変更」から「イベント」に言い換えられました — [日本語](https://code.claude.com/docs/ja/hooks-guide#auto-format-code-after-edits) / [English](https://code.claude.com/docs/en/hooks-guide#auto-format-code-after-edits)、[日本語](https://code.claude.com/docs/ja/hooks#worktreeremove) / [English](https://code.claude.com/docs/en/hooks#worktreeremove)
- **`OTEL_RESOURCE_ATTRIBUTES` の値の中の `=` の書き方が載った**（`monitoring-usage` の「Multi-team organization support」）。値の中の `=` は `%3D` と書きます — [日本語](https://code.claude.com/docs/ja/monitoring-usage#multi-team-organization-support) / [English](https://code.claude.com/docs/en/monitoring-usage#multi-team-organization-support)
- **セッションの保存先の `append()` で、`uuid` のない項目を残すよう求められた**（`agent-sdk/session-storage` の「Mirror writes are best-effort」）。再試行したバッチは書けた項目を再び届けうるので、`entry.uuid` で重複を除き、`uuid` を持たない項目はすべて残します。バッチがそれでも失敗したときの `mirror_error` の段落は後ろの段落に移りました — [日本語](https://code.claude.com/docs/ja/agent-sdk/session-storage#mirror-writes-are-best-effort) / [English](https://code.claude.com/docs/en/agent-sdk/session-storage#mirror-writes-are-best-effort)
- **Linux の Desktop を Claude API キーで使う方法の案内が替わった**（`desktop-linux` の「Install」）。API キーの認証には CLI を使う、という文が外れ、Claude API キー・Amazon Bedrock・Agent Platform・Microsoft Foundry・LLM ゲートウェイで Desktop を使うには「Claude Desktop on 3P」を見る、となりました — [日本語](https://code.claude.com/docs/ja/desktop-linux#install) / [English](https://code.claude.com/docs/en/desktop-linux#install)
- Self-hosted runner: 作業の指示が置き換えられたオンデマンドのランナーの終了コードを 1 に戻した。2.1.321 と 2.1.322 では 0 に変えていました
- `/security-review` を、Claude が実行する前に尋ねるよう変更。スキルのインラインの git のコマンドも、auto モードと bypass の外では、ベアリポジトリのワークツリーのようなフォルダーで、許可するまで止まります
- 同じマシンの自分の各セッションが、利用者のプロンプトなしにほかのセッションへ送れるメッセージの数を、約 20 から 100,000 に変更
- Claude Desktop の Code タブのセッションが、利用者がまた入力するまで待つ前にほかのセッションへ送れるメッセージの数を、20 から 100,000 に変更
- 組織の設定とポリシーの要求が、`ALL_PROXY` だけで設定したプロキシを使わないよう変更。ネットワークがそれらにプロキシを要するなら `HTTPS_PROXY` を設定します
- Claude Code が認識しないモデル ID に想定するコンテキストウィンドウを、200K から 1M に変更。早めにコンパクトするには `/autocompact` を、200K のままにするには `CLAUDE_CODE_DISABLE_1M_CONTEXT=1` を使います（`model-config` は今回も 200K と述べています。「その他」参照）
- ほかのベンダーのモデルで、ウィンドウの小さいセッションの扱いを変更。いっぱいになると `/clear` まで毎ターン失敗することがあるので、いっぱいになる前に `CLAUDE_CODE_DISABLE_1M_CONTEXT=1` を設定します
- Claude Code 自身の ripgrep と、内部の git のコマンドのほとんどが、サインインのトークンと API キーのほとんどを持たずに動くよう変更。そうした git のコマンドの下の credential helper やフックは、それらを見つけられなくなります
- `MCP_SDK_GENERATION=v1` が、v2 の MCP クライアントを互換モード（以前のハンドシェイク、緩めた OAuth のサインインの検査）で動かすよう変更。v1 の MCP クライアントは削除されました
- MCP サーバーのサインインを終えるために Claude が使うツールが、bypass と auto のモードでも確認を求めるよう変更。`dontAsk` モードのように誰にも尋ねられない場面では `/mcp` を使います
- Self-hosted runner: コネクターの承認の確認か、実行中のツールの中のサインインで止まっているセッションを、アイドルか寿命の上限で一時停止として解放するよう変更。遅れて答えると、新しいクローンから再開します
- アーティファクトの更新を、組織の外の人がそのアーティファクトを見られるか、誰が見られるかを Claude が確かめられないときは、allow ルールの下でも先に尋ねるよう変更
- `--global` も `--host` もない `glab config set` と、`glab config edit --local` を、Bash のサンドボックスの中では読み取り専用で失敗するよう変更。サンドボックスの外で実行します
- macOS・Linux・WSL の Bash のサンドボックスが、書き込めるフォルダーの中のシンボリックリンクを通して与えた、ほかの場所か存在しないパスへの書き込みのアクセスを無視するよう変更。実際のパスを許可します
- 「don't ask again」を変更。秘密を含むように見える allow ルールや、git が追跡する `settings.local.json` に保存されることになるルールは、そのセッションの間だけ効き、保存されません
- macOS と Linux のサンドボックスを変更。`git worktree add`・`move`・`remove` は読み取り専用で失敗し、セッションを始めたのでも与えられたのでもないワークツリーでのコミットも、プロジェクトの中のものでも失敗します
- `--settings` のファイルが正しい JSON でなく、`sandbox` のキーを持つとき（サンドボックスをオフにするものでも）、起動を止めるよう変更
- `PreToolUse` フックが「allow」を返した後に、ツールの権限の確認がエラーで失敗したときの動きを変更。Claude Code は、どのフックも答えなかったものとして呼び出しを判断します
- `PermissionRequest` フックが書き換えた入力で、ツールの権限の確認が失敗したときの動きを変更。Claude Code はもう一度尋ねるか、誰も答えられない場面では呼び出しを拒みます
- GitLab のマージリクエストのバッジを、サンドボックスのセッションが開いたリポジトリでだけ出すよう変更
- `claude mcp add --help` の例を、ローカルのコマンドに変更
- mod を変更。`engine.create` の `*`・名前空間・否定のフックは観察だけになります。`$` の名詞を追加するか保留するには、`engine.create` を名前でフックします
- `engine.create` のフックが、受け付ける唯一の形で書かれていない mod を、`claude plugin validate` が失敗にするよう変更。インストール済みの mod は引き続き読み込まれます
- git のサブモジュールが、リポジトリが記録するコミットにないとき、マーケットプレイスとプラグインのインストールが失敗するよう変更
- プロジェクト（`.mcp.json`）の MCP サーバーの承認が、サーバーの正確な名前に一致するよう変更。別の綴りで書いた承認の項目では、また尋ねます
- `--trust-workspace false` のセルフホストのランナーと、信頼していないフォルダーの VS Code のセッションを変更。リポジトリの設定は、利用者のフックを無効にしたり、プラグインをオン・オフにしたりできなくなります
- `tool.list` のプラグインのフックが追加・削除するツールが、モデルとすべてのエージェントに当たるよう変更
- プラグインのインストールのコマンドが stderr に書くと、`claude plugin install` と `/plugin` が成功ではなく警告を出すよう変更
- claude.ai のチャットと Cowork のタスクが、プラグインのファイルを送る前に秘密鍵がないか確かめ、含まれるかもしれなければ先に尋ねるよう変更
- `claude rm` と agents view が、セッションを削除したではなく一覧から外した、と述べるよう変更。`claude rm` のヘルプは、会話は残り `claude --resume` が一覧に出す、と述べます
- `/stickers` が、ブラウザーでページを開かず、ステッカーのパックは今のところすべて配布済み、と述べるよう変更
- managed settings の `policyHelper` が、ユーザーや `--settings` のファイルから環境変数を受け取らないよう変更。必要なものは managed の `env` か起動するシェルで設定します
- claude.ai かデスクトップアプリで選んだ 2 つのファイルの間、または選んだファイルとリンクの後に打った `/skill` か `@file` が、効かないよう変更
- 分割ペインのエージェントの teammate が、要求がチームリーダーから来たかを確かめるよう変更。リーダーより長く残った teammate の求めは拒まれ、計画の承認は `/clear` か `/resume` の後に送り直す必要があります
- `.git` のフォルダーがリンクか、ハードリンクを含むチェックアウト（git-new-workdir の構成や `cp -al` のコピーなど）では、ワークツリーの作成を拒むよう変更。普通のクローンを使います
- フォークしたスキルかワークフローのエージェントをセーフガードが止めた後に、Claude に伝える内容を変更。自分で作業せず、狭いプロンプトで再試行するか利用者に伝えます
- ブラウザーのツールの呼び出し（Claude in Chrome、デスクトップのブラウザーのペイン）が、エスケープした入力か JSON のテキストの入力の一部を拒み、綴り直し方を Claude に伝えるよう変更
- アプリが入力されたものではないと印を付けたプロンプトが、ワークフローのエージェントに利用者の要求として届かないよう変更
- macOS のコンピューター操作が、Control か Option と一緒に Space を押したままにするキーの組み合わせと、利用者の許可が要るより多くのシステムのショートカットを拒むよう変更
- Terminal.app の初回のセットアップが、同意の前に「Use Option as Meta key」の設定と、Option で打てなくなるもの、元に戻す方法を示すよう変更
- `CLAUDE_CODE_OVERLOADED_RETRY_MAX_DELAY_MS` の上限を、64000 から 300000 に変更
- デスクトップアプリの Code タブのワークフローが、使用量の上限で一時停止し、リセットの後に続くよう変更
- クラウドのセッションと Remote Control の下の、支出の上限と 1M コンテキストのエラーと `/usage-credits` が、Web のアドレスを示さないよう変更
- OpenTelemetry のエクスポートで名前で報告する MCP サーバーを、現在のコネクターのディレクトリーに従うよう変更
- 効果のなかったバックグラウンドのセッションの `/logout` を変更。ターミナルと同じく、コンピューターのすべてのセッションをサインアウトし、保存した MCP のログインとプラグインの秘密を削除し、セッションを終えます
- macOS: Bash のサンドボックスを変更し、`lsof` のようなツールが、コマンドが始めていないプロセスについて示す情報が減ることがあります
- クラウドのスケジュールしたタスクを変更。利用者自身の設定の `PostToolUse` フックは、`ExitPlanMode` の結果の計画を置き換えられなくなります
- Anthropic がホストするクラウドのセッションの `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` が、自動メモリーの抽出と、一部のセッションでは `/btw` に当たらないよう変更。メインの会話は引き続き従います
- `subagentStatusLine` の設定を削除（詳細はハイライト 1 参照）
- プラグインの `agent` の設定を非推奨に（詳細はハイライト 1 参照）
- [VSCode] Claude Code のサンドボックスがオンのフォルダーで Claude Code on the web のセッションを開くときの動きを変更。拡張機能はセッションのブランチに切り替えなくなり、ダイアログがその理由を述べます
- `/login` と `claude setup-token` のサインインのエラーを改善。要求が拒まれた・届かない・時間切れのとき、何が起きたかと何を確かめるかを述べます
- Bash の権限の確認を改善。遅いか忙しいマシンでも、同じコマンドがより確実に同じ答えを得ます
- Bash の権限の確認を改善。確認したときとは違う動きをしうる一部のコマンドで、権限を尋ねるようになりました
- `/mcp` を改善。入力のスキーマを API が拒むために外したサーバーのツールの数と、その理由を示します
- セッションで書いた mod をオンにするか Claude Code が尋ねるときの「Not now」の選択を改善。いつ読み込まれるかを述べます
- コネクターの ID を 1〜2 文字打ち間違えた MCP のツールの呼び出しのエラーを改善。ホストのアプリケーションが登録したサーバーなら、呼ぶべきツールを名指します
- 2,000 を超えるプラグインをオンにした claude.ai のアカウントの Claude Desktop とクラウドのセッションを改善。起動時の待ちが短くなり、プラグインがない理由を Claude が言えるようになりました
- 多くのサブエージェントを使うときのメモリーの使い方を改善。終わったサブエージェントのトランスクリプトは、後のサブエージェントが動く間メモリーに残らず、早く解放されます
- インストールのスクリプトでのインストールを改善。最新の版を 2 回ダウンロードしなくなりました
- 深く入れ子になったページでの WebFetch の速度とメモリーの使い方を改善
- `cleanupPeriodDays` の片付けを改善。読めないフォルダーをエラーと数えます
- Claude apps gateway の `/v1/models` を改善。どの上流でもコンテキストウィンドウが確かなモデルについて、`max_input_tokens` を示します
- `ToolSearch` を改善。Claude が短い名前で探したツールがすでに使えるときは、一致なしとだけ報告せず、そう述べます
- `/home` が autofs のマップのときの Linux の起動を改善。Claude Code は `/home` 自体のファイルを調べなくなりました。`/` の 1 階層下より深いマップのルートには `CLAUDE_CODE_AUTOMOUNT_ROOTS` を設定します
- `-p`・SDK・IDE・クラウドのセッションの Fable の上限のメッセージを改善。続け方に加え、上限がいつリセットされるかを述べます
- [VSCode] TLS を検査するプロキシの後ろのサインインのエラーを改善。証明書の失敗は、ターミナルと同じく、何をすべきかを述べます
- [Claude Code on the web] クラウドか Remote Control のセッションへのファイルのアップロードが失敗したときのメッセージを改善。ページが多すぎる・パスワード・時間切れのような理由を示します
- [Claude Code on the web] Claude がアクセスできないリポジトリをクラウドのセッションに加えるときを改善。長いエラーの代わりに、短いメッセージと Reconnect GitHub のボタンが出ます
- [Claude Code on the web] 新しいクラウドの環境に一部のネットワークの秘密を加えられないときのメッセージを改善。各ホストを挙げ、分かる場合は理由を述べ、閉じるまで残ります
- [Claude Code on the web] GitHub のシングルサインオンが組織を隠すときの、新しいセッションのリポジトリのピッカーを改善。ほかのリポジトリが並んでいてもそう述べ、GitHub に接続し直すリンクを示します
- [Claude Code on the web] GitHub のサインインが切れたときの Git providers のページを改善。リンクできる組織を黙って隠さず、接続し直すよう求めます

**バグ修正**

- `/compact` をもう一度実行するか、`/context` のようなコマンドの後に実行すると、Claude がまだ答えていないメッセージを要約で消す問題を修正
- 再開したセッションが、次のメッセージを、再開しなかった古い中断したメッセージにつなげる問題を修正
- Claude がとても大きなファイルを変えた後、次のプロンプトでメモリーが急増する問題を修正
- 実行中のセッションで保存した設定が、直前に `settings.json` へ手で加えた編集を取り消す問題を修正。セッション中に削除した設定ファイルは、削除されたままになります
- トークンの更新中に終わると、`claude plugin` のコマンドと `claude mcp list` が Console のプロファイルからサインアウトさせる問題を修正
- 特定の `/proc` のファイルで Edit と Bash がメモリー不足になり、デバイスと名前付きパイプで Edit が止まるかメモリー不足になる問題を修正
- 設定ファイルの保存が「Out of memory」で失敗すると、Claude Code が起動できないか、サインアウト時に保存した資格情報を消せない問題を修正
- ストリーミングなしで送った要求が、拒まれた画像・thinking のブロック・ベータのヘッダーのように、ストリーミングの要求なら回復するエラーで失敗する問題を修正
- ワークツリーに入る前にシェルがいたフォルダーが削除されていると、`ExitWorktree`・ワークツリーの終了のダイアログ・`/resume` がセッションを違うフォルダーに残す問題を修正
- テキストが折り返すとき、アクセントなどの結合文字が文字の左に来る・古い写しが画面に残る・黙って消えることがある問題を修正
- キーの組み合わせ自身の操作がそこで使えないとき、組み合わせの最後のキー（ctrl+x enter の Enter など）がダイアログのテキスト欄に作用する問題を修正
- コマンドを止める前に Claude Code が実行するプロセスの一覧の取得が長くかかると、`ps` のプロセスが溜まる問題を修正
- `WorktreeCreate` フックが作ったか、入れ子のリポジトリに属するワークツリーに入った後、サブエージェントのトランスクリプトと大きなツールの結果がセッションのトランスクリプトと別に保存される問題を修正
- `/fork`・左矢印・`--bg` がバックグラウンドで続けると、名前付きの Anthropic のプロファイルのセッションが別のサインインに移る問題を修正。更新の間に開いていたセッションは開き直します
- 名前付きの Anthropic のプロファイルがない・変わった・上書きされたとき、バックグラウンドのセッションが別のサインインで会話を送る問題を修正。止まってそう述べます
- シェルの API キー・認証トークン・ワークロード ID（setup token ではない）のセッションが、バックグラウンドで別のサインインに移る問題を修正。止まってそう述べます
- MCP のツールの呼び出しが、もう一度サインインを求めず、`TOKEN_EXPIRED` のようなサインインのサーバーのエラーで終わる問題を修正
- claude.ai のログインが期限切れで、クレジットのない保存した Console のキーか `ant auth login` のプロファイルが代わりに使われたとき、「Credit balance too low」が出る問題を修正
- 名前付きの Anthropic のプロファイルのセッションが、サインインを保てない古いバックグラウンドのサービスに渡される問題を修正。サービスを再起動するよう述べます
- バックグラウンドのセッションのサインインが、前のアカウントのログインやほかの資格情報を残す問題を修正。コンピューターのすべてのセッションについてそれらを消し、拒まれたサインインではログインが残らないことがあります
- 更新で再起動したバックグラウンドのセッションが、プロファイルと保存したログインの間で移る問題を修正
- サインインの前に開いたセッションが、サインインの後もサインアウト時の機能フラグを保つ問題を修正
- Claude apps gateway のサインインが切れた後に失敗し続けるセッションを修正。ほかのターミナルで `/login` でサインインし直すと、次のメッセージから続きます
- カスタムの `X-Api-Key` ヘッダーを設定すると、課金の通知が `ant auth login` の組織を名指す問題を修正
- macOS: キーチェーンの応答が遅いとき、`/login` の成功やトークンの更新の直後に「Not logged in · Please run /login」が戻る問題を修正
- 組織のゲートウェイが期限切れのトークンに 403 で答えると、Claude Desktop でターンが失敗する問題を修正。Claude Code は Desktop に新しいトークンを求めて再試行します
- Amazon Bedrock がアカウントにモデルを拒んだときに出るエラーを修正。AWS の資格情報を更新するよう述べず、モデルを有効にするよう述べます（ハイライト 5 も参照）
- 3 つ以上のセッションが同時に新しいサインインを要するとき、`awsAuthRefresh` か `gcpAuthRefresh` のコマンドが 1 つの要求で 2 回動くことがある問題を修正
- 終わった claude.ai のログインについての `claude -p` の警告を修正し、`claude auth logout` は保存した MCP サーバーのログインとプラグインの秘密も消す、と述べるようにした
- `.git` や `.claude` のような機密のパスに書き込むコマンドの Bash の権限の確認が、保存しても次の確認を止めない「don't ask again」を提示する問題を修正
- 一部の `lsof` のコマンドが権限の確認なしに動いた場合を修正
- `cat > file <<EOF` でファイルを書く Bash のコマンドが「Read 1 file」と表示される問題を修正
- bypass permissions か Bash の allow ルールの下で、Bash の権限の確認が違うフォルダーからの `rm` として判断し、危険な削除の確認を飛ばした場合を修正
- auto モードが使えないとき、`--permission-mode auto` か設定の `defaultMode: auto` が、より多くを許しうるモードで始まる問題を修正。先に尋ねる Manual モードで始まります
- `plansDirectory` を設定すると、計画のファイルがプロジェクトの外に書かれることがある問題を修正。プロジェクトの中に留まると示せない書き込みは拒まれます
- ワークツリーに入った後、Claude が自分のバックグラウンドのコマンドかエージェントの出力を読むときに権限の確認が出る問題を修正
- Bash の権限の確認がコマンドの一部を見逃した場合を修正
- セッション中に Bash のサンドボックスがオフになりうる場合を修正
- `Bash(ls*)` のようなワイルドカードを付けた Bash の allow ルールが、場合によって権限の確認を飛ばす問題を修正。`Bash(NODE_ENV*)` のように変数を名指すルールでは尋ねるようになります
- `ANTHROPIC_BASE_URL` のゲートウェイの後ろで、ゲートウェイでの名前に「haiku」を含むモデルで auto モードが動く問題を修正。`claude-haiku-5-5` 以外のそうしたモデルは、Haiku 4.5 と同じく拒まれます
- `sudo`・`env` などのラッパーを通して実行する一部のコマンドを、Bash の deny と ask のルールが見逃す問題を修正
- まとめた `sudo` のフラグで書いた Bash の allow ルールが、場合によって権限の確認を飛ばす問題を修正
- `sandbox.excludedCommands` が、名指していないコマンドを場合によってサンドボックスの外で動かす問題を修正
- Write と Edit のツールが、`Read` の deny ルールが覆うパスに書き込めた場合を修正
- 特定の既定でないシェルのオプションを設定した zsh の利用者で、Bash のコマンドが権限の確認なしに動いた場合を修正
- まだ古い設定ファイルを使うインストールで、Bash のサンドボックスが Claude Code 自身の設定を完全には守らない問題を修正
- mod の `tool.check` フックからの権限の確認が、尋ねたプラグインではなく、そのツールにフックしたすべてのプラグインを名指す問題を修正
- サンドボックスのコマンドが、設定のディレクトリーの下の Claude Code のファイルのチェックポイントの写しを読めた問題を修正
- 巻き戻しが権限モードを変えることがある問題を修正
- Claude Code が確かめたのとは違うフォルダーにつながるシンボリックリンクを通して、プロジェクトの設定が読まれることがある問題を修正
- `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB` を設定し `sandbox.enabled` がオフのとき、Linux で HTTP フックが HTTP 500 で失敗する問題を修正
- サンドボックスをオンにする `--settings` か SDK の設定が検証に失敗すると、`claude -p` と Agent SDK がサンドボックスなしで Bash を動かす問題を修正。Claude Code は起動時に止まり、無効な設定を名指します
- もう読み込まれていない MCP のツールの呼び出しが長く続いた後、`/export` が黙って早く止まる問題を修正
- サーバーの接続が遅いとき、再開した会話から以前の MCP のツールの呼び出しが欠け、スクロールバックで行が繰り返す問題を修正
- 狭いターミナルとパイプで `claude mcp add --help` が長い例のコマンドを行に分け、貼り付けた例がヘッダーなしで動く問題を修正
- claude.ai でオンにした後も、`defaultEnabled: false` のプラグインが claude.ai のチャットのクラウドのセッションでオフのままになる問題を修正
- Vertex の `/fast on` と `/fast off` が、`/fast` のメニューと違ってプラグインの `config.set` フックに尋ねない問題を修正
- ターミナルで作業するとき、Claude Docs のコネクターで作った文書がブラウザーで開かない問題を修正
- リポジトリの設定だけがオンにするプラグインの、誤解を招く「not cached」のエラーを修正。インストールされていないと述べ、インストールのコマンドを示し、テキストと stream-json の `-p` の実行でも出ます
- mod が Claude Code 自身の確認の質問を言い換えられた問題を修正
- 失敗したリロードの直後に作ったファイルを、mod のホットリロードが無視することがある問題を修正
- `npm`・`pip`・`uv`・`cargo`・`github`・`gh` という名前のマーケットプレイスが、予約名として拒まれる問題を修正
- 折りたたんだツールのグループで、止めた MCP の呼び出しか、フルスクリーンで止めたシェルのコマンドが「Called」か「Ran」と読める問題を修正。結果が記録されていないと述べ、入力を示します
- SDK と Desktop のセッションで、managed settings がオンにしたプラグインの読み込みのエラーが debug のログにしか出ない問題を修正。`init.plugin_errors` に挙がります
- プラグインのインストールのコマンドが成功したとき、それが stderr に書いた内容（プラグインにまだスキルがない、という注記など）をプラグインのインストールが隠す問題を修正
- プラグインのマーケットプレイスの `renames` のマップの形式の誤った 1 項目で、Claude Code がマーケットプレイスのほかの名前の変更を無視する問題を修正
- `claude --bg --safe-mode` のセッションが、セーフモードでは起動しないプロジェクトの MCP サーバーについて尋ねるために起動時に止まる問題を修正
- http でないリンクで、MCP のリンクの確認が、リンクが開かないことを言わずに Accept を提示する問題を修正
- 認証が要るがサインインを保っているサーバーで、`/mcp` と `/plugins` が MCP サーバーのページをカーソルを「Disable」に置いて開く問題を修正。「Reconnect」を提示し、そこで開きます
- `enabledPlugins` に版の一覧があるプラグインが、メッセージなしにオフのままになる問題を修正。`/plugin` と `claude plugin list` が理由を述べます
- クローンしたファイルのパスが 260 文字に達すると、Windows でプラグインとマーケットプレイスのインストールが失敗する問題を修正
- `UserPromptSubmit` かプラグインのプロンプトのフックがまだ動いている間に、メッセージを送った直後に押した Stop が、リモートと SDK のセッションでエラーとして出る問題を修正
- Agent SDK のアプリか `claude -p` の呼び出し元が MCP サーバーを外して加え直し、その間にツールの呼び出しがそれに届こうとしていたとき、サーバーがツールなしで切断されたままになる問題を修正
- `--plugin-dir` の mod のフックが止まるかフックのワーカーをクラッシュさせると、テキスト出力の `claude -p` の実行が stderr に何も出さない問題を修正
- 起動後に設定が `CLAUDE_CODE_MCP_STARTUP_WAIT_MS` を下げると、SDK のセッションが、`--allowedTools` か `mcp_tool` フックが名指す MCP サーバーに、最初のターンの前に 2 秒未満しか与えない問題を修正
- SDK のホストが MCP サーバーのツールの一覧に null の項目を送ると、ヘッドレスのセッションが終わる問題を修正
- WebFetch が空の表のセルを落とし、後の値を 1 列左にずらす問題を修正
- `cleanupPeriodDays` で期限切れになったとき、ディレクトリーを変えたセッションの一時ファイルが残る問題を修正
- ほかのプログラムがファイルを書き直している間、起動時に managed settings（`managed-settings.json`・`managed-settings.d`）を見落とすことがある問題を修正。起動時にそうしたファイルを 2 回読みます
- フォルダーが後から git のリポジトリになったときか新しいマシンで、`.claude/settings.local.json` がグローバルに無視されない問題を修正
- フルスクリーンで、`/diff` が diff のパネルを閉じる前に Claude の終わりを待つ問題を修正
- 作業ディレクトリーかホームのフォルダーの名前で始まる名前のフォルダーで、`/memory` が間違ったか回りくどいパスを示し、Windows ではファイルのパスのスラッシュが失われる問題を修正
- ツールの呼び出しのパラメーター名の壊れた絵文字が後の要求で送り直され、厳密な JSON のパーサーに拒まれる問題を修正
- 理由を付けて拒んだ後、折りたたんだツールの呼び出しが実行されたように見える問題を修正。「Not run · rejected」と示します
- Claude Code が返信を捨てたとき、NFS か FUSE のファイルシステムで保存したセッションの一部が失われうる場合を修正
- WebFetch が呼び出しのたびに組織のポリシーと `CLAUDE_CODE_DISABLE_WEB_FETCH` を確かめ直さない問題を修正
- claude.ai とデスクトップアプリからの @ メンションのファイルのタイトル・アプリの名前・セッションの名前が、打ったテキストとして扱われることがある問題を修正
- フルスクリーンのレンダラーで、複数行のステータスラインが長いプロンプトに画面の外へ押し出される問題を修正
- プロキシ自体に `https://` で届く場合に、TLS を検査するプロキシの後ろの証明書のエラーが続いた場合を修正
- Pro と Max のアカウントに、組織が拒むフィードバックの下書きが提示される問題を修正
- どの管理の設定でもオンにできないのに、Claude in Chrome のポリシーのメッセージが管理者に連絡するよう伝える問題を修正
- アーティファクトのプレビューが、Claude が公開したばかりのものと違うアーティファクトを開くことがある問題を修正
- 証明書の名前の制約のエラーが数分にわたって再試行される問題を修正。すぐに失敗し、何を直すかを述べます
- サーバーがセッションの履歴を見つけられないとき `claude --teleport` が空のセッションを開き、再開が失敗したとき `claude -p --teleport` がエラーなしに終わる問題を修正
- `ctl+k` のように修飾キーを打ち間違えたキーバインドが、修飾なしのキーに割り当たる問題を修正。そのバインドは無視されます
- `/btw` の答えと要約に、会話の前の返信が含まれることがある問題を修正
- managed settings のファイルの読み取りが失敗したとき、起動時の要求が、組織の管理するプロキシと CA の設定から利用者が設定したものに切り替わる問題を修正
- 送っていたファイルを新しいメッセージが中断したとき、Claude が違う理由を述べる問題を修正
- フックの `continue: false` が止めたターンを、`CLAUDE_CODE_RESUME_INTERRUPTED_TURN` が再実行する問題を修正
- 切り替え先のモデルがないサブエージェントをセーフガードが止めたとき、自動のモデルの切り替えがオフだと Claude に伝えられる問題を修正
- 最初のコミットの前に `git add -N` で加えたファイルが、リモートのセッションの変更ファイルの一覧から欠ける問題を修正
- `browser_batch` など一部の Claude in Chrome のツールの呼び出しで、フルスクリーンのトランスクリプト（ctrl+o）やサブエージェントの進捗にツールの名前が出ない問題を修正
- 返信に 10〜20 秒かかったとき、サブエージェントの進捗の要約が更新を飛ばす問題を修正
- リンクした managed settings のファイルを読めなかったとき、`claude doctor` と `/status` がまだ読まれていると述べる問題を修正
- 組織のポリシーが Claude in Chrome をオフにしているとき、対話型の `--chrome` のセッションが Claude in Chrome なしで始まる理由を示さない問題を修正。その旨の 1 行が出ます
- ネットワーク上のパスと応答しないフォルダーでの `/rewind` の一覧を修正。すべての追跡ファイルを変更ありと名指し、ラベルを示すのが遅く、ファイルの読み取りが返らないと何も示さなかった
- `--debug` と `--debug-file` が、debug のログのフォルダーの `latest` という名前のファイルを置き換える問題を修正
- 時間切れになったフィードバックの送信が、大きすぎると報告される問題を修正。要求が時間切れになったと述べます
- スクリーンリーダーのモードで、読み上げ中にシステムの時計が進むと通知が途中で切れる問題を修正
- スクリーンリーダーのモードで、質問か権限の確認への答えに入れた音声入力か貼り付けのテキストと絵文字が落ちる問題を修正
- 権限と計画のダイアログの下の名前のラベルが、一部のエージェントの名前の一部を隠す問題を修正
- `claude update` が終わる瞬間に Ctrl+C を押すと `claude` のコマンドが消えた場合を修正
- 違うモデルで動くサブエージェントを見ているとき、フルスクリーンのヘッダーが、そのサブエージェントが使わないセッションの effort のレベルを名指す問題を修正
- `CLAUDE_CODE_EFFORT_LEVEL` が上書きしているのに、選んだ effort のレベルをモデルのピッカーと `/model` が示す問題を修正
- ワークツリーの作成が遅かった後のヒントが `.claude` を含まない `sparsePaths` の一覧を勧め、プロジェクトの設定とルールのないワークツリーができる問題を修正
- `/model` のピッカーから最新のモデルの強調表示が欠ける問題を修正
- ブラウザーを開けないとき、フルスクリーンの `/upgrade` と Ctrl+クリックしたリンクが黙って失敗する問題を修正。アドレスを示します
- Claude apps gateway の JSON のログが、メッセージの改行などの制御文字を 2 重にエスケープする問題を修正
- サブエージェントのメッセージを展開すると、その中の端末の制御シーケンスが平文として示されず効いてしまう問題を修正
- Claude in Chrome のセットアップが、`/chrome` で接続が終わると述べる問題を修正。`claude --chrome` で再起動するよう伝えます
- デンマーク語・ノルウェー語・フェロー語・ギリシャ語のキーボードの配列で、語の中で ø や π を打つと Option キーのヒントが出る問題を修正
- ほかの自分のセッションが同じメッセージを 2 回か多くのメッセージを一度に送ると、Claude Desktop のセッションが busy のまま止まる問題を修正
- `--no-session-persistence` で動かしたセッションの後、長いツールの結果がディスクに残る問題を修正。通常の終了・Ctrl+C・SIGTERM で消えます
- サブエージェントがコンパクトするとき、`PreCompact`・`PostCompact` とコンパクト後の `SessionStart` のフックが `agent_id` と `agent_type` を受け取らない問題を修正
- 削っている間にほかのプロセスがファイルを書き直すと、`CLAUDE_CODE_TRANSCRIPT_LOCAL_GC` が保存したトランスクリプトからメッセージを落とす問題を修正
- セッションの命名のように Claude Code が小さなモデルで短い副次の要求をすると、Fable の週の上限を超えた後の「Now using usage credits」の通知が繰り返すか出ない問題を修正
- ターミナルで、Fable の週の上限がリセットの時刻も選択肢のメニューも示さない問題を修正
- 使用量の上限のメニューで選んだ待ちが、要求が拒まれたときに黙って後のリセットに移る問題を修正。メニューが開きます
- 現在の上限を読み込めなかったとき、支出の上限のメニューがより低い上限を提示する問題を修正
- setup token と `CLAUDE_CODE_OAUTH_TOKEN` で `/usage` が上限のバーを隠す問題を修正。セッションと週のバーを残し、ほかがない理由を述べます
- `/usage` がサブエージェントの種類の名前の横にセッション全体の割合を示し、要求のあった時間だけを数えるのにセッションが 8 時間動いたと述べる問題を修正
- Remote Control: Wi-Fi の切り替えや VPN の再接続のようなネットワークの変化の後、セッションが 1 分以上切断と表示される問題を修正
- Claude Code が使用量クレジットを使うか尋ねている間、Remote Control が何も示さない問題を修正。質問は Claude のアプリにも出ます
- ターミナルでしか答えられない権限の確認を待っている間、Remote Control がセッションを実行中と示す問題を修正
- Remote Control: 止まってから 4 時間を超えて同じフォルダーで再起動すると、`claude remote-control` が新しいコンピューターとして接続し直す問題を修正。最大 30 日間 ID を保ちます
- Remote Control: ディスクが応答しなくなると、シャットダウン時にセッションが動いたまま残り、終わったセッションが枠を占める問題を修正
- Remote Control: `DISABLE_TELEMETRY` か `DO_NOT_TRACK` を設定すると、ほかのデバイスと電話の通知に、Claude が何の許可を求めているかが出ない問題を修正
- Remote Control: ツールの呼び出しの `command` が数値・真偽値・オブジェクトのとき、詳細か debug のモードでホストが終了するか、セッションの出力を読むのをやめる問題を修正
- Remote Control: 応答しなくなったファイルシステムのフォルダーでセッションの開始が失敗した後、ホストが止まることがある問題を修正
- Remote Control: バックグラウンドのサブエージェントがまだ動いている間、デスクトップアプリからのセッションが電話でアイドルと示される問題を修正
- Agent SDK の `managedSettings` が、Remote Control・agent view・Workflows・Artifact のオフのスイッチを無視する問題を修正
- `otlp` のエクスポーターにエンドポイントがあり `OTEL_EXPORTER_OTLP_PROTOCOL` がないとき、OpenTelemetry のエクスポートが黙って失敗する問題を修正。既定は `http/protobuf` になります
- 既定の `localhost:4318` のエンドポイントへの OpenTelemetry のエクスポートが、設定したプロキシを通る問題を修正
- 形式の誤った `OTEL_RESOURCE_ATTRIBUTES` の項目 1 つで、その変数のすべての属性が OpenTelemetry のリソースから落ちる問題を修正。ほかは残り、`/status` が外したものを名指します
- `OTEL_LOG_ASSISTANT_RESPONSES=0` のとき、OpenTelemetry の `user_prompt` のイベントとインタラクションのスパンが、バックグラウンドのエージェントの返信を記録する問題を修正
- プロキシがコレクターに届くのに 10 秒を超えると、OpenTelemetry のエクスポートが失敗する問題を修正。25 秒になり、これは `OTEL_EXPORTER_OTLP_TIMEOUT` で許せる最大でもあります（以前は 30）
- 公式のプラグインのスキルが起動したとき、OpenTelemetry の `agent.name` が `custom` ではなく利用者が定義したサブエージェントの名前を示す問題を修正
- セッションの再開の後、`claude agents` が前のターンの状態を示す問題を修正
- Linux で `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB` を設定すると、読み取り専用の git のコマンドが承認を要するか、`claude -p` の下で拒まれる問題を修正
- `claude agents` が打ったプロンプトを失う問題を修正。Esc で消すには 2 回目の押下が要り、ctrl+y で戻せます
- `claude attach` と `claude agents` のセッションで、バックグラウンドに移すキーが何もしない問題を修正。Ctrl+B d で切り離すには、Ctrl+B から 800 ms 以内に d を押します
- バックグラウンドのサービスが `DISABLE_ERROR_REPORTING` なしで始まったとき、バックグラウンドのセッションが、シェルだけで設定したそれを無視する問題を修正
- `claude agents` で、ブロックされたセッションに返信した後の誤った「needs input」の通知と、テキストがなく Bash や Read のような基本のツールだけでバックグラウンドのターンが終わった後の繰り返しの通知を修正
- 設定が求めたモデルを禁じると、テキスト出力の `claude -p` が黙って別のモデルを使う問題を修正。stderr で警告します
- `claude -p` が実行のたびに `deniedModels` と `availableModels` の項目についての注記を出す問題を修正。`/status` と `claude doctor` は引き続き一覧にします
- Windows: ワイルドカードかファイルの一覧を与えると、一部のファイルを読む Bash のコマンドが権限の確認なしに動く問題を修正
- Windows: Claude Code が、同じ PATH のフォルダーでプログラムの `.exe` の横にある `.cmd` か `.bat` のラッパー（`git.exe` の横の `git.cmd` など）を実行する問題を修正。`cmd.exe` と同じく `.exe` を実行します
- Windows: フォルダーの実際のパスを解決できないドライブで、シェルのコマンドが「Working directory was deleted」で失敗する問題を修正
- 履歴を書き直した直後にマシンが止まると、クラウドのセッションの履歴が読めなくなる問題を修正
- 同じフォルダーの別のセッションが `/clear`・`/resume`・`/branch` を使った後、終わったセッションのスケジュールしたタスクが動かないことがある問題を修正
- クラウド・セルフホストのランナー・SDK のセッションで、セッションのプロセスが再起動した後に承認が届くと、承認した計画に「You are not in plan mode」と答える問題を修正
- Cloud sessions: 長い会話で、再起動の後に Claude の質問への答えが失われる問題を修正
- Claude が返信する前にセッションが再起動すると、クラウドのセッションの会話からメッセージが落ちる問題を修正
- Cloud sessions: メッセージがファイルを名指すと、添付した画像がないと Claude が述べる問題を修正
- チャットの最初の返信の直後にファイルが届くと、再開したクラウドのセッションが、誰も頼んでいないモデルの呼び出しをする問題を修正
- 返信の途中でセッションのコンテナが止まると、クラウドのセッションのストリーミングの返信で途中のテキストが欠ける問題を修正
- Cowork のクラウドのセッションから送ったスキルのファイルが、最初の試みでアップロードに失敗することがある問題を修正
- [VSCode] ツールの呼び出しを解析できず捨てた返答が、Claude が再試行した後も表示される問題を修正
- [VSCode] コンパクトの要約の直後に続いた待機中のメッセージが、会話かフォークから欠ける問題を修正
- [VSCode] 使用量クレジットがオフの間、「Buy usage credits on claude.ai」のボタンが Fable への支払いの同意と数えられる問題を修正
- [VSCode] ウィンドウの再読み込みか再起動のたびに、開いているターミナルで「extensions want to relaunch the terminal」の警告が戻る問題を修正
- [VSCode] 最初のプロンプトの前に Claude のプロセスが再起動した新しいチャットで、「Couldn't load this conversation's saved history」が出る問題を修正
- [VSCode] コードを貼り付けた後、サインインの画面がまたログインの選択肢を示す問題を修正。サインインが終わるまで「Signing in…」と示します
- [VSCode] 別のモデルを選んだ後も、VS Code と JetBrains のパネルに「You've hit your Fable limit」の行が残る問題を修正
- [VSCode] 使用量クレジットがオフか使い切ったとき、VS Code と JetBrains のパネルの Fable の使用量の警告が使用量クレジットを名指す問題を修正
- [VSCode] CRLF の改行のファイルで、複数行の編集の diff のタブが開かない問題を修正
- [VSCode] セッションを切り替えた後も音声入力が録音し続ける問題を修正
- [Claude Code on the web] メッセージを送らずに一時停止したセッションを開き直すと、セルフホストのセッションが起動の後も「Starting Claude Code」のままになる問題を修正
- [Claude Code on the web] セルフホストの環境の一時停止したセッションで、「Session paused」のバナーの下に「Sending」と Stop のボタンがまだ出ることがある問題を修正
- [Claude Code on the web] クラウドのセッションで、GitHub Enterprise Server からのプルリクエストの更新が github.com にリンクする問題を修正。新しい更新は自分のサーバーにリンクします
- [Claude Code on the web] クラウドのセッションで、とても大きな GitHub Actions のジョブのログと実行のログのアーカイブが、ダウンロードに失敗するか途中で切れる問題を修正
- [Claude Code on the web] iOS のアプリからリポジトリ付きで始めた新しいクラウドのセッションが、自分のブランチを持たない問題を修正
- [Claude Code on the web] 数分の接続の失敗の後、開いているクラウドか Remote Control のセッションのページが「Disconnected」のままになる問題を修正。自分で接続し直そうとします
- [Claude Code on the web] 開いているクラウドか Remote Control のセッションの「Connection lost」のカードの Try again が、「Try again」をメッセージとして送る問題を修正。接続し直そうとします
- [Claude Code on the web] まだ何も示していない返信の 5 分後に、Claude がまだ作業しているのにクラウドのセッションから Stop のボタンが消える問題を修正
- [Claude Code on the web] 答えを待つ間にセルフホストのランナーがセッションを解放した後、開いたままのタブから承認の確認が消えることがある問題を修正
- [Claude Code on the web] スケジュールしたタスクからリポジトリを外すと、その GitHub のトリガーが黙って別のリポジトリに移る問題を修正。選ぶまで Save は待ちます
- [Claude Code on the web] クラウドのセッションで 10 分を超える git のクローンと fetch が、最後の最後で切られることがある問題を修正
- [Remote Control] 何も削除していないのに、自分のセッションが環境が削除されたと述べる問題を修正。コンピューターが接続されていないと述べます
- [Remote Control] Claude が始まる前にコンピューターが切断された後、一部のセッションがセッションの一覧で実行中と示され続ける問題を修正。エラーの印か、アイドルとして示されます
- [Claude Tag] Enterprise Grid のワークスペースの間で移した Slack のチャンネルのスケジュールしたタスクが、誰かがそこに投稿するまで Slack を使えない問題を修正
- [Claude Tag] Claude が投稿できない非公開か Slack Connect のチャンネルについて、Claude との DM に Approve and post のカードが出る問題を修正。Claude は理由を受け取り、カードは出ません
- [Claude Tag] アクセスのバンドルも資格情報を持っていると、Claude Tag の管理の設定の Remove connector が拒まれる問題を修正。コネクターに設定したものを外し、バンドル自身のものは残します
- [Claude Tag] Claude Tag の管理の設定の Channels のタブが、ワークスペースとそのチャンネルをページをまたいで分ける問題を修正。チャンネルはワークスペースのすぐ下に出ます
- [Claude Tag] Cloud environments の管理のページの Set for Claude Tag のリンクが、環境の設定に行かない問題を修正。設定する場所である Slack のページの Advanced のタブを開きます

**その他**

- `subagentStatusLine` の設定とプラグインの既定の設定の記述（`statusline`・`settings-reference`・`hooks`・`plugins/components`・`plugins/manifest-reference`・`errors`。詳細はハイライト 1 参照）
- **mod のテストキットの `expect` のアサーションの一覧が外れた**（`plugins/mods/test` の「Check a result with `expect`」）。2026年11月11日 版のサマリで載ったと扱った、等しさ・テキスト・数値・中身・有無と型・例外の 6 つに分けた一覧が、`expect` には `toEqual` や `toHaveLength` のような独自のアサーションがある、全部はビルドの型の `claude-code/index.d.ts` で `type Matchers` を探す、という案内に替わりました。promise が落ち着く値を調べるには、`expect(...)` のすぐ後に `.resolves` か `.rejects` を置き、`await expect(promise).rejects.toThrow()` のように行を `await` します — [日本語](https://code.claude.com/docs/ja/plugins/mods/test#check-a-result-with-expect) / [English](https://code.claude.com/docs/en/plugins/mods/test#check-a-result-with-expect)
- **`Shift+Enter` がそのまま使えるターミナルから Apple Terminal が外れた**（`interactive-mode` の「Multiline input」・`terminal-config` の「Enter multiline prompts」） — [日本語](https://code.claude.com/docs/ja/terminal-config#enter-multiline-prompts) / [English](https://code.claude.com/docs/en/terminal-config#enter-multiline-prompts)
- **fast mode の内訳を出す Console の選択肢の名前が「Speed」になった**（`fast-mode` の「See where fast mode spend appears」）。これまでの「Speed (research preview)」から替わりました — [日本語](https://code.claude.com/docs/ja/fast-mode#see-where-fast-mode-spend-appears) / [English](https://code.claude.com/docs/en/fast-mode#see-where-fast-mode-spend-appears)
- **外れた文**: `interactive-mode`（「Vim editor mode」の、`Ctrl+O` でトランスクリプトの表示を切り替えるか `/config` のようなパネルを開閉しても vim のモードとカーソルの位置が保たれる、という段落、「Reverse search with Ctrl+R」の、履歴の読み込み中でも一致の受け入れと取り消しはすぐ効く、という文、「What Claude Code underlines」の、テキストを変えることはない、という言葉）、`tools-reference`（「AskUserQuestion tool behavior」の、自分で打った答えは中立の言い方で伝えるので Claude はそのとおりに従う、という文、「Read tool behavior」の、Claude はいつも絶対パスを渡すよう指示されている、という文）、`workflows`（「Bundled workflows」の、`/deep-research` は呼び出したときだけ動く、という文）、`commands`（「All commands」の、`/verify` と `/deep-research` は呼び出したときだけ動く、という 2 つの補足）、`agent-sdk/agent-loop`（「What consumes context」の、CLAUDE.md は最初の要求だけが全額を払う、という補足）
- **自動コンパクトの節の言い換え**: `model-config` の「Correct the window for a gateway or custom model ID」の、「起動時の」警告が「警告」になりました。この節は、Claude Code が認識しないモデル ID には 200K トークンを想定する、と今回も述べています（changelog の v2.1.323 は、この想定を 200K から 1M に変えた、と述べています）
- **字句の小さな修正**: `plugins/create` の 2 つの写し・`plugins/overview`・`plugins/publish`（「every field」「every component type」のような、すべてを挙げるという言い方が外れた）、`claude-apps-gateway-config`（「`managed`」の一覧の書き方）
- **changelog の前のリリースの言い換え**: 2026年07月18日 と 2026年03月05日 のリリースの項目で、「GrowthBook」が「feature flag」の言い方になりました（「a GrowthBook feature evaluates to null」→「a feature flag evaluates to null」、「cold GrowthBook」→「feature flags not yet fetched」）
- **書式だけの変更**: 全体で `\_` のようなエスケープが外れ（`x86\_64` → `x86_64` など。`llms-full.txt` の `\_` は 206 から 5 になった）、見出し・表・本文の 107 組の行が置き換わりました（changelog の 56 組を含む）。`feature-availability` の脚注と、`agent-sdk/python`・`agent-sdk/typescript`・`agent-sdk/todo-tracking`・`agent-sdk/sessions` の注記の行には `&#xA;` が入っています。`quickstart` のインストールのコマンドの 5 つのフェンスに残っていた `theme={null}` の重複が解消し、`cli-reference` の `--name` と `--permission-prompt-tool` の説明の 2 つの空白が 1 つになりました。書式だけが変わったページは、`agent-sdk/cost-tracking`・`agent-sdk/python`・`agent-sdk/secure-deployment`・`agent-sdk/sessions`・`agent-sdk/structured-outputs`・`agent-sdk/subagents`・`agent-sdk/todo-tracking`・`agent-sdk/troubleshooting`・`agent-sdk/typescript`・`analytics`・`channels-reference`・`claude-apps-gateway-on-gcp`・`cli-reference`・`cloud-environments`・`corporate-launcher`・`desktop`・`env-vars`・`feature-availability`・`mcp`・`plugins/troubleshooting`・`quickstart` の 21 です
<!-- light:minor-updates:end -->

見出しマップ（`en/claude_code_docs_map.md`）は、更新時刻が 2026年11月12日 04:18:24 UTC から 2026年11月13日 05:45:38 UTC に替わり、4 行が加わり 6 行が外れました。加わったのは `llms-full.txt` に加わったのと同じ 3 つの見出しと新しいスタンプ、外れたのは `llms-full.txt` から外れたのと同じ 5 つの見出しと古いスタンプです。今回、見出しマップにだけ先に載った見出しはありません。

**参考リンクについて**: 日本語版は、今回取り上げたページのうち 37 ページを取得し、該当する節があるかと今回の内容になっているかを確かめました。多くは今回の内容になっていましたが、`subagentStatusLine` とプラグインの既定の設定の記述は、`settings-reference`・`plugins/components`・`plugins/manifest-reference`・`statusline`・`hooks` の「Hook locations」・`errors` の「Path escapes plugin directory」で日本語版にまだ残っていたか、確かめられませんでした。これらと、`settings-reference` の「`sandbox.filesystem.allowWrite`」、`errors` の「This session is running in another terminal」は英語版だけをリンクしています。`fast-mode` の日本語版は選択肢の名前を「速度」と訳していて、「(research preview)」に当たる言葉はありません。アンカーは、見出しから作った id か、ページ内・ページ間のリンクが使っている id です。`errors` の「The settings file has changed since Remote Control started」の id は、「Find your error」の表のリンクが使う `#settings-file-changed-since-remote-control-started` で、見出しから作る id とは違います。リンクを付けなかったページは、字句か書式だけの変更か、外れた文を述べるものです。**changelog ページへのリンクは、本サマリの方針どおり付けていません。**

## 新着情報

<!-- light:whats-new:start -->
（今回の差分に新着情報（`whats-new/`）のページはありません。head の `llms.txt`・`llms-full.txt`・見出しマップにも whats-new のページは載っていません）
<!-- light:whats-new:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2026-11-11.md](./archives/latest/2026-11-11.md)
- 前回サマリ(詳細版): [./archives/latest-detail/2026-11-11.md](./archives/latest-detail/2026-11-11.md)

<!--
base_commit: c85f1a228a539e3f1157cb0caf9aea01e5add4d1
head_commit: 77f196ce342a0c6130e111a1fa66ada14d87a243
generated_at_full: 2026-11-13T15:17:21+09:00
-->
