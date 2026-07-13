# カテゴリ適性スコアリング結果（プロトタイプ）

入力: `official-llms-txts/code.claude.com/docs/llms-full.txt`（148 ページ） / 候補語数: 3938

スコア = ( 幾何平均(C-value, 被覆バンド, 分散均一度, 共起中心性) + ページ名加算(最大0.25) + 見出し加算(最大0.12) + 固有名詞加算(最大0.1) ) × 降格率

## 上位 5 語

| # | term | TF | DF | C-val | band | even | cent | ページ名p | 見出しp | 大文字率 | 降格 | score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | plugin | 2239 | 67 | 0.53 | 0.86 | 0.44 | 0.81 | 8 | 25 | 0.02 | 1.00 | 1.006 |
| 2 | mcp | 1517 | 93 | 0.35 | 0.62 | 0.60 | 0.64 | 4 | 21 | 0.88 | 1.00 | 0.997 |
| 3 | hook | 1853 | 77 | 0.44 | 0.76 | 0.48 | 0.82 | 3 | 20 | 0.02 | 1.00 | 0.973 |
| 4 | subagent | 1239 | 69 | 0.29 | 0.84 | 0.48 | 0.75 | 3 | 17 | 0.00 | 1.00 | 0.916 |
| 5 | mode | 1510 | 95 | 0.35 | 0.60 | 0.60 | 0.67 | 5 | 25 | 0.01 | 1.00 | 0.913 |

## 包含併合後のカテゴリ候補（上位 40 グループ）

併合規則: トークン部分列（mcp ⊂ mcp server）と既知接頭辞複合語（sub+agent）。スコアはグループ合計。

| # | 代表語 | Σscore | 併合された語 |
|---:|---|---:|---|
| 1 | mode | 2.403 | permission mode, auto mode, plan mode |
| 2 | mcp | 2.361 | mcp server, mcp tool |
| 3 | agent | 2.097 | subagent, agent team |
| 4 | permission | 1.694 | permission prompt, permission rule |
| 5 | tool | 1.619 | bash tool, tool name |
| 6 | command | 1.554 | bash command, shell command |
| 7 | cloud | 1.516 | google cloud |
| 8 | sdk | 1.467 | agent sdk |
| 9 | bedrock | 1.430 | amazon bedrock |
| 10 | environment | 1.387 | environment variable |
| 11 | plugin | 1.379 | plugin marketplace |
| 12 | platform | 1.358 | agent platform |
| 13 | window | 1.343 | context window |
| 14 | control | 1.325 | remote control |
| 15 | settings | 1.261 | settings file |
| 16 | gateway | 1.258 | llm gateway |
| 17 | microsoft | 1.231 | microsoft foundry |
| 18 | output | 1.219 | output style |
| 19 | prompt | 1.217 | system prompt |
| 20 | desktop | 1.168 | desktop app |
| 21 | code | 1.085 | code v2 |
| 22 | session | 1.077 | code session |
| 23 | api | 1.034 | api key |
| 24 | view | 0.978 | preview |
| 25 | status | 0.977 | status line |
| 26 | hook | 0.973 | — |
| 27 | effort | 0.881 | effort level |
| 28 | skill | 0.863 | — |
| 29 | cli | 0.833 | — |
| 30 | configuration | 0.772 | — |
| 31 | usage | 0.745 | — |
| 32 | organization | 0.734 | — |
| 33 | enterprise | 0.728 | — |
| 34 | task | 0.727 | — |
| 35 | config | 0.726 | — |
| 36 | marketplace | 0.720 | — |
| 37 | input | 0.713 | — |
| 38 | github | 0.713 | — |
| 39 | workflow | 0.700 | — |
| 40 | response | 0.692 | — |

## 指定語の順位確認

- `environment variable`: **36 位** (TF=411, DF=75, score=0.692)
- `permission`: **10 位** (TF=1195, DF=107, score=0.820)
- `hook`: **3 位** (TF=1853, DF=77, score=0.973)

## カテゴリ素案クラスタ（上位60語・ページ共起ベース）

1. **plugin** — skill, marketplace, directory
2. **mcp** — hook, subagent, mcp server, tool
3. **mode** — permission, prompt, config, plan
4. **cli** — desktop, terminal
5. **settings** — configuration, environment, environment variable
6. **output** — input, response, error, behavior
7. **sdk** — agent, agent sdk
8. **cloud** — platform, gateway, organization, enterprise, google cloud, bedrock, amazon bedrock, aws, microsoft foundry, api
9. **control** — remote, web
10. **window** — task, context, action
11. **usage** — model, data, cost
12. **github** — workflow
13. **custom** — (単独)
14. **command** — (単独)
15. **security** — (単独)
16. **session** — (単独)
17. **code** — (単独)
18. **worktree** — background
