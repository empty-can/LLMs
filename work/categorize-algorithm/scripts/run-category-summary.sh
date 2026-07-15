#!/usr/bin/env bash
#
# run-category-summary.sh — カテゴリ別サマリ生成パイプライン(build_category_summary.py)のランチャー
#
# 人間が任意のコミット範囲に対してサマリを手動生成するためのラッパー。
# パイプラインは extract(機械) → LLM 編集(Claude) → render(機械) の3工程で、
# 中間の LLM 編集だけはスクリプト化できない(Claude=Opus が担当)。そのため
# 本ランチャーは Claude への手渡し境界で prepare / render の2段に分ける
# (README §5)。
#
# 使い方:
#   ./run-category-summary.sh prepare <BASE> <HEAD> [ラベル]
#       extract で変更点を項目化し、prompt で LLM 指示文を生成する。
#       生成された prompt.md を Claude(サブエージェント または claude -p)に渡すと、
#       Claude が items.json を読んで entries.json を書き出す。
#
#   ./run-category-summary.sh render  <ラベル>
#       Claude が書いた entries.json からカテゴリ別サマリ summary.md を組み立てる。
#
# 例(取り込みコミット b0e62bd → 7acfb2c を手動生成):
#   ./run-category-summary.sh prepare b0e62bd 7acfb2c
#   # → prompt.md を Claude に渡し、entries.json が書かれるのを待つ
#   ./run-category-summary.sh render 7acfb2c
#
# 中間ファイルの置き場:
#   work/categorize-algorithm/output/manual-runs/<ラベル>/
#     items.json / prompt.md / entries.json / summary.md   (このディレクトリは gitignore)
#   ラベル既定値は HEAD の短縮 SHA。
#
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)"
BCS="$SCRIPT_DIR/build_category_summary.py"
RUNS_DIR="$REPO_ROOT/work/categorize-algorithm/output/manual-runs"

PY="$(command -v python || command -v python3 || command -v py || true)"
if [ -z "$PY" ]; then
  echo "エラー: python が見つかりません(python / python3 / py のいずれも PATH に無い)。" >&2
  exit 1
fi

usage() { sed -n '3,33p' "$0" | sed 's/^# \{0,1\}//'; }

CMD="${1:-}"
case "$CMD" in
  prepare)
    if [ "$#" -lt 3 ]; then echo "エラー: prepare には <BASE> <HEAD> が必要です。" >&2; echo; usage; exit 1; fi
    BASE="$2"; HEAD="$3"
    LABEL="${4:-$(git -C "$REPO_ROOT" rev-parse --short "$HEAD")}"
    WORKDIR="$RUNS_DIR/$LABEL"
    mkdir -p "$WORKDIR"
    ITEMS="$WORKDIR/items.json"; PROMPT="$WORKDIR/prompt.md"; ENTRIES="$WORKDIR/entries.json"

    echo "[prepare] 範囲: $BASE..$HEAD  ラベル: $LABEL"
    echo "[prepare] 1/2 extract(差分→項目化→機械分類)"
    "$PY" "$BCS" extract --base "$BASE" --head "$HEAD" --out "$ITEMS"
    echo "[prepare] 2/2 prompt(LLM 指示文を categories.json から生成)"
    "$PY" "$BCS" prompt --items "$ITEMS" --entries-out "$ENTRIES" --out "$PROMPT"
    echo "----------------------------------------"
    echo "[prepare] 完了。次にやること(LLM 編集は Claude の担当):"
    echo "  A) prompt.md を Claude に渡す(いずれか):"
    echo "     - Claude Code のサブエージェントに prompt.md を読ませて実行させる"
    echo "     - もしくは:  claude -p \"\$(cat '$PROMPT')\""
    echo "     Claude は items.json を読み、entries.json を書き出す:"
    echo "       items   : $ITEMS"
    echo "       prompt  : $PROMPT"
    echo "       entries : $ENTRIES  (Claude がここに書く)"
    echo "  B) entries.json が書かれたら仕上げ:"
    echo "       ./run-category-summary.sh render $LABEL"
    ;;

  render)
    if [ "$#" -lt 2 ]; then echo "エラー: render には <ラベル> が必要です。" >&2; echo; usage; exit 1; fi
    LABEL="$2"
    WORKDIR="$RUNS_DIR/$LABEL"
    ITEMS="$WORKDIR/items.json"; ENTRIES="$WORKDIR/entries.json"; SUMMARY="$WORKDIR/summary.md"

    if [ ! -f "$ITEMS" ]; then
      echo "エラー: $ITEMS が無い。先に prepare を実行したか、ラベルが正しいか確認してください。" >&2
      exit 1
    fi
    if [ ! -f "$ENTRIES" ]; then
      echo "エラー: $ENTRIES が無い。Claude による LLM 編集(prepare の手順 A)がまだ完了していません。" >&2
      exit 1
    fi

    echo "[render] ラベル: $LABEL"
    "$PY" "$BCS" render --items "$ITEMS" --entries "$ENTRIES" --out "$SUMMARY"
    echo "----------------------------------------"
    echo "[render] 完成: $SUMMARY"
    ;;

  -h|--help|"")
    usage
    [ "$CMD" = "" ] && exit 1 || exit 0
    ;;

  *)
    echo "エラー: 不明なサブコマンド '$CMD'(prepare または render)。" >&2
    echo; usage; exit 1
    ;;
esac
