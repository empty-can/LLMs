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
#       extract で変更点を項目化し、prompt で LLM 指示文を categories.json から
#       生成する(= プロンプトは毎回再生成されるので古い指示文の使い回しは起きない)。
#       生成された prompt.md を Claude(サブエージェント または claude -p)に渡すと、
#       Claude が items.json を読んで entries.json を書き出す。
#       prepare 時点の taxonomy 構造(カテゴリ/サブ区分の key)を記録しておく。
#
#   ./run-category-summary.sh render <ラベル> [--force]
#       Claude が書いた entries.json からカテゴリ別サマリ summary.md を組み立てる。
#       prepare 後に categories.json のカテゴリ/サブ区分 key が変わっていた場合、
#       entries は旧 taxonomy に対して生成されているため整合性ガードが停止する
#       (新設カテゴリが空になる/改名・削除カテゴリのエントリが未分類に落ちるのを防ぐ)。
#       変更が entries に影響しないと分かっている場合のみ --force で続行できる。
#
# 例(取り込みコミット b0e62bd → 7acfb2c を手動生成):
#   ./run-category-summary.sh prepare b0e62bd 7acfb2c
#   # → prompt.md を Claude に渡し、entries.json が書かれるのを待つ
#   ./run-category-summary.sh render 7acfb2c
#
# 中間ファイルの置き場:
#   work/categorize-algorithm/output/manual-runs/<ラベル>/
#     items.json / prompt.md / entries.json / summary.md / taxonomy.sig
#     (このディレクトリは gitignore。ラベル既定値は HEAD の短縮 SHA)
#
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)"
BCS="$SCRIPT_DIR/build_category_summary.py"
TAXONOMY="$SCRIPT_DIR/categories.json"   # extract/prompt/render の既定 taxonomy と同一
RUNS_DIR="$REPO_ROOT/work/categorize-algorithm/output/manual-runs"

PY="$(command -v python || command -v python3 || command -v py || true)"
if [ -z "$PY" ]; then
  echo "エラー: python が見つかりません(python / python3 / py のいずれも PATH に無い)。" >&2
  exit 1
fi

# 先頭のコメントブロック(3行目以降の連続する # 行)をヘルプとして表示する。
usage() { awk 'NR>2 { if (/^#/) { sub(/^# ?/, ""); print } else { exit } }' "$0"; }

# taxonomy の「構造シグネチャ」= カテゴリ key + サブ区分(cat,sub) の集合。
# entries はこの key を参照するため、これが変わると既存 entries が壊れうる。
# name/icon/vocab/prompt_hint/並び順の編集はシグネチャを変えない(= 誤検知しない)。
taxonomy_sig() {
  "$PY" - "$1" <<'PY'
import json, sys
d = json.load(open(sys.argv[1], encoding="utf-8"))
keys = sorted([c["key"] for c in d["categories"]] + [d["uncategorized"]["key"]])
subs = sorted((c["key"], s["key"]) for c in d["categories"] for s in c.get("subcategories", []))
print(json.dumps({"keys": keys, "subs": subs}, ensure_ascii=False, sort_keys=True))
PY
}

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
    # render 時の整合性ガード用に、いま使った taxonomy 構造を記録する
    taxonomy_sig "$TAXONOMY" > "$WORKDIR/taxonomy.sig"
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
    shift  # "render" を除去
    LABEL=""; FORCE=0
    while [ "$#" -gt 0 ]; do
      case "$1" in
        --force) FORCE=1 ;;
        -h|--help) usage; exit 0 ;;
        -*) echo "エラー: 不明なオプション '$1'。" >&2; exit 1 ;;
        *) if [ -z "$LABEL" ]; then LABEL="$1"; else echo "エラー: 引数が多すぎます: '$1'。" >&2; exit 1; fi ;;
      esac
      shift
    done
    if [ -z "$LABEL" ]; then echo "エラー: render には <ラベル> が必要です。" >&2; echo; usage; exit 1; fi

    WORKDIR="$RUNS_DIR/$LABEL"
    ITEMS="$WORKDIR/items.json"; ENTRIES="$WORKDIR/entries.json"; SUMMARY="$WORKDIR/summary.md"
    SIGFILE="$WORKDIR/taxonomy.sig"

    if [ ! -f "$ITEMS" ]; then
      echo "エラー: $ITEMS が無い。先に prepare を実行したか、ラベルが正しいか確認してください。" >&2
      exit 1
    fi
    if [ ! -f "$ENTRIES" ]; then
      echo "エラー: $ENTRIES が無い。Claude による LLM 編集(prepare の手順 A)がまだ完了していません。" >&2
      exit 1
    fi

    # 整合性ガード: prepare 後に taxonomy のカテゴリ/サブ区分 key が変わっていないか
    CUR_SIG="$(taxonomy_sig "$TAXONOMY")"
    if [ ! -f "$SIGFILE" ]; then
      echo "[render] 警告: prepare 時の taxonomy シグネチャ記録がありません(ガード導入前の作業フォルダの可能性)。整合性を検証できないまま続行します。" >&2
    elif [ "$(cat "$SIGFILE")" != "$CUR_SIG" ]; then
      echo "[render] エラー: categories.json のカテゴリ/サブ区分の構成が prepare 後に変更されています。" >&2
      echo "  entries.json は旧 taxonomy に対して Claude が生成したものです。このまま render すると" >&2
      echo "  新設カテゴリが空になる／改名・削除カテゴリのエントリが「未分類」に落ちる可能性があります。" >&2
      echo "  対処: prepare からやり直して Claude に再編集させてください:" >&2
      echo "    ./run-category-summary.sh prepare <BASE> <HEAD> $LABEL" >&2
      echo "  変更が entries に影響しないと分かっている場合のみ、--force で続行できます。" >&2
      if [ "$FORCE" -ne 1 ]; then
        exit 1
      fi
      echo "[render] --force 指定のため警告を無視して続行します。" >&2
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
