#!/usr/bin/env bash
#
# run-term-scoring.sh — カテゴリ候補語スコアリング(term_scoring.py)のランチャー
#
# 人間が taxonomy(categories.json)を保守するとき、任意のタイミングで実行する。
# 公式 docs の大改編後や「未分類」が増えたと感じたときに走らせ、出力
# term-scores.md の候補語ランキング・クラスタ素案を見て categories.json を
# 手編集する(README §3 / §6-5)。Claude は不要(純粋な統計処理)。
#
# 使い方:
#   ./run-term-scoring.sh                                  # 既定(上位100語)で再計算
#   ./run-term-scoring.sh --top 150                        # 上位語数を変える
#   ./run-term-scoring.sh --probe permission hook mcp      # 指定語の順位を確認
#   ./run-term-scoring.sh --out /tmp/scores.md --top 5     # 別ファイルへ試し出力
#   (--input/--out/--top/--probe は term_scoring.py にそのまま渡る)
#
# 既定の出力先 work/categorize-algorithm/output/term-scores.md は git 追跡下。
# 既定のまま実行するとこの追跡ファイルを更新する(= 定例メンテナンスの想定動作)。
# 上書きしたくない試し実行では --out で別パスを指定する。
#
set -euo pipefail

case "${1:-}" in
  -h|--help)
    sed -n '3,22p' "$0" | sed 's/^# \{0,1\}//'
    exit 0
    ;;
esac

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)"

PY="$(command -v python || command -v python3 || command -v py || true)"
if [ -z "$PY" ]; then
  echo "エラー: python が見つかりません(python / python3 / py のいずれも PATH に無い)。" >&2
  exit 1
fi

# term_scoring.py の既定入出力は REPO ルート相対のため、ルートで実行する
cd "$REPO_ROOT"

echo "[run-term-scoring] リポジトリ: $REPO_ROOT"
echo "[run-term-scoring] 実行: term_scoring.py $*"
echo "----------------------------------------"
"$PY" work/categorize-algorithm/scripts/term_scoring.py "$@"
echo "----------------------------------------"
echo "[run-term-scoring] 次にやること:"
echo "  1) 出力(既定: work/categorize-algorithm/output/term-scores.md)の上位語・クラスタ素案を確認"
echo "  2) 追加/変更したい概念があれば scripts/categories.json を手編集(README §6-2 / §6-3)"
echo "  3) categories.json を編集したら LLM プロンプトを再生成して再実行(README §6-4)"
