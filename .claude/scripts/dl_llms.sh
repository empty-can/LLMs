#!/bin/bash
# .claude/scripts/dl_llms.sh
#
# download_list.csv に定義された URL から llms.txt 等を取得し、
# official-llms-txts/ 配下の指定フォルダに保存する。
#
# 実行方法（リポジトリルートから）:
#   bash .claude/scripts/dl_llms.sh
#
# 注意: CSV の DL先フォルダ列は official-llms-txts/ からの相対パス。

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
TSV_FILE="${SCRIPT_DIR}/download_list.tsv"
# スクリプトは .claude/scripts/ にあるため、リポジトリルートは ../../。
OUTPUT_BASE="${SCRIPT_DIR}/../../official-llms-txts"

# 1 ファイルあたりの保存上限（95 MiB）。GitHub は 100 MiB 超のファイルを含む push を
# 拒否し、一度コミットされると履歴を書き換えない限り bot の push が毎日失敗し続ける
# （anchor 保全のため履歴の書き換えは禁止）。上限を超えたら既存ファイルを残して保存しない。
MAX_BYTES=$((95 * 1024 * 1024))

# 一時ファイルへ取得し、成功かつ上限以下のときだけ置き換える。転送が途中で切れても
# 前日のファイルを壊さない（切り詰めたファイルが commit+push されるのを防ぐ）。
# 失敗時は一時ファイルを消す（残すと手順 4 の git add に混入する。.gitignore でも除外済み）。
# 戻り値は curl の終了コード、上限超過は 1。スクリプト全体の終了コードは従来どおり変えない
# （終了コードの正常化はフロー再設計で commit 順序とあわせて扱う）。
download_atomic() {
    local url="$1" dest="$2" tmp="$2.tmp" rc size
    curl -L -f --retry 3 --retry-delay 5 "$url" -o "$tmp"
    rc=$?
    if [ $rc -ne 0 ]; then
        rm -f "$tmp"
        return $rc
    fi
    size=$(wc -c < "$tmp")
    if [ "$size" -gt "$MAX_BYTES" ]; then
        echo "WARN: size limit exceeded (${size} bytes > ${MAX_BYTES}). Keeping existing file: $dest"
        rm -f "$tmp"
        return 1
    fi
    mv -f "$tmp" "$dest"
}

# TSV の相対パス解決のため出力ベースに cd
cd "$OUTPUT_BASE" || { echo "ERROR: cannot cd to $OUTPUT_BASE"; exit 1; }

# ヘッダ行をスキップして読み込み（タブ区切り）
tail -n +2 "$TSV_FILE" | while IFS=$'\t' read -r url filename folder overwrite_flag
do
    # 空行スキップ
    [ -z "$url" ] && continue

    echo "----------------------------------------"
    echo "Downloading: $url"

    # 保存先フォルダ作成
    mkdir -p "$folder"

    # 保存先ファイルパス
    filepath="$folder/$filename"

    # 上書きフラグを小文字化
    flag=$(echo "$overwrite_flag" | tr '[:upper:]' '[:lower:]')

    # TRUE または 1 の場合
    if [[ "$flag" == "true" || "$flag" == "1" ]]; then

        echo "Overwrite mode: ENABLED"

        # 強制上書きダウンロード（一時ファイル経由・サイズ上限つき）
        download_atomic "$url" "$filepath"

    else

        echo "Overwrite mode: DISABLED"

        # 既存ファイルが存在する場合
        if [ -e "$filepath" ]; then

            # archive フォルダ作成
            archive_dir="$folder/archive"
            mkdir -p "$archive_dir"

            # タイムスタンプ生成
            timestamp=$(date +"%Y%m%d_%H%M")

            # ファイル名と拡張子分離
            base="${filename%.*}"
            ext="${filename##*.}"

            # 拡張子なし対応
            if [ "$base" = "$ext" ]; then
                archive_name="${base}_${timestamp}"
            else
                archive_name="${base}_${timestamp}.${ext}"
            fi

            archive_path="$archive_dir/$archive_name"

            echo "Existing file found."
            echo "Move to archive:"
            echo "  $filepath"
            echo "  -> $archive_path"

            # archiveへ移動
            mv "$filepath" "$archive_path"
        fi

        # ダウンロード
        curl -L -f "$url" -o "$filepath"

    fi

    # 実行結果確認
    if [ $? -eq 0 ]; then
        echo "Success: $filepath"
    else
        echo "Failed: $url"
    fi

done
