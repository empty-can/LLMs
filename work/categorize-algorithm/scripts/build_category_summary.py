#!/usr/bin/env python3
"""カテゴリ別詳細サマリの機械パイプライン（試作）。

サブコマンド:
  extract : base..head の llms-full.txt / llms.txt 差分から変更項目を機械抽出し、
            categories.json の語彙マッチでカテゴリを割り当てて items JSON を出力する。
            各項目には LLM 要約用の diff 抜粋を同梱する。
  render  : items JSON + 要約 JSON（{item_id: 日本語要約}）からサマリ .md を組み立てる。

分類・構成は全て決定的（機械）で、LLM が担うのは各項目の日本語要約文のみ。
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import datetime, timedelta
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
FULL = "official-llms-txts/code.claude.com/docs/llms-full.txt"
INDEX = "official-llms-txts/code.claude.com/docs/llms.txt"
DOCS_BASE = "https://code.claude.com/docs/en/"


def git(*args: str) -> str:
    r = subprocess.run(
        ["git", *args], cwd=REPO, capture_output=True, encoding="utf-8", errors="replace"
    )
    if r.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed: {r.stderr[:500]}")
    return r.stdout


# --- head 断面のページ/セクション索引 -----------------------------------------------

SOURCE_RE = re.compile(r"^Source:\s+https://code\.claude\.com/docs/en/(\S+)")


def page_index(head: str):
    """head 断面の llms-full.txt から (行番号→ページ/直近h2) を引ける索引を作る。"""
    lines = git("show", f"{head}:{FULL}").splitlines()
    pages = []  # {start, slug, title, sections: [(line, heading)]}
    in_fence = False
    for i, line in enumerate(lines, 1):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if line.startswith("# ") and i < len(lines):
            m = SOURCE_RE.match(lines[i])
            if m:
                pages.append(
                    {"start": i, "slug": m.group(1), "title": line[2:].strip(), "sections": []}
                )
                continue
        if pages and line.startswith("## "):
            pages[-1]["sections"].append((i, line[3:].strip()))
    return pages


def locate(pages, lineno: int):
    """新ファイル行番号 → (slug, title, 直近h2見出し or None)。"""
    cur = None
    for p in pages:
        if p["start"] <= lineno:
            cur = p
        else:
            break
    if cur is None:
        return None, None, None
    sec = None
    for ln, h in cur["sections"]:
        if ln <= lineno:
            sec = h
        else:
            break
    return cur["slug"], cur["title"], sec


def gfm_anchor(text: str) -> str:
    t = re.sub(r"[^\w\s\-]", "", text.lower())
    return re.sub(r"\s+", "-", t.strip())


# --- 差分 → 項目化 ------------------------------------------------------------------

HUNK_RE = re.compile(r"^@@ -\d+(?:,\d+)? \+(\d+)(?:,(\d+))? @@")


def extract_items(base: str, head: str):
    pages = page_index(head)
    diff = git("diff", "-U0", base, head, "--", FULL)
    groups: dict[tuple, dict] = {}
    new_start = None
    for line in diff.splitlines():
        m = HUNK_RE.match(line)
        if m:
            new_start = int(m.group(1))
            slug, title, sec = locate(pages, max(new_start, 1))
            key = (slug, sec)
            groups.setdefault(
                key,
                {"slug": slug, "page_title": title, "section": sec, "added": [], "removed": [], "hunks": 0},
            )["hunks"] += 1
            cur = groups[key]
            continue
        if new_start is None:
            continue
        if line.startswith("+") and not line.startswith("+++"):
            cur["added"].append(line[1:])
        elif line.startswith("-") and not line.startswith("---"):
            cur["removed"].append(line[1:])

    items = []
    for (slug, sec), g in groups.items():
        norm = lambda ls: re.sub(r"\s+", " ", " ".join(ls)).strip()
        g["cosmetic"] = bool(g["added"]) and norm(g["added"]) == norm(g["removed"])
        g["kind"] = "update"
        items.append(g)

    # llms.txt（インデックス）差分から新規/削除ページを検出
    idx_diff = git("diff", "-U0", base, head, "--", INDEX)
    for line in idx_diff.splitlines():
        m = re.match(r"^([+-])- \[([^\]]+)\]\((\S+?)\)(?::\s*(.*))?$", line)
        if m:
            sign, title, url, desc = m.groups()
            slug = url.split("/docs/en/")[-1].removesuffix(".md")
            items.append(
                {
                    "slug": slug,
                    "page_title": title,
                    "section": None,
                    "added": [desc or ""],
                    "removed": [],
                    "hunks": 1,
                    "cosmetic": False,
                    "kind": "new_page" if sign == "+" else "removed_page",
                }
            )
    return items


# --- カテゴリ分類（語彙マッチ・決定的） ----------------------------------------------


def load_taxonomy(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def classify(item, taxonomy):
    text = " ".join(item["added"] + item["removed"]).lower()
    text += " " + (item["section"] or "").lower() + " " + (item["page_title"] or "").lower()
    slug = item["slug"] or ""
    scores = {}
    matched: dict[str, list] = {}
    for cat in taxonomy["categories"]:
        s = 0
        hits = []
        for term in cat["vocab"]:
            n = len(re.findall(r"(?<![\w-])" + re.escape(term) + r"(?![\w-])", text))
            if n:
                s += n
                hits.append(f"{term}×{n}" if n > 1 else term)
        for pref in cat["slug_prefixes"]:
            if slug == pref or slug.startswith(pref):
                s += 8
                hits.append(f"slug:{pref}")
                break
        if s:
            scores[cat["key"]] = s
            matched[cat["key"]] = hits
    if not scores:
        return taxonomy["uncategorized"]["key"], [], [], 0
    ranked = sorted(scores.items(), key=lambda kv: -kv[1])
    primary, top = ranked[0]
    secondary = [k for k, v in ranked[1:] if v >= max(3, top * 0.5)][:2]
    return primary, secondary, matched[primary][:6], top


# --- render ------------------------------------------------------------------------


def commit_date(commit: str) -> datetime:
    return datetime.fromisoformat(git("show", "-s", "--format=%aI", commit).strip())


def render(items_path: Path, summaries_path: Path | None, taxonomy_path: Path, out_path: Path):
    data = json.loads(items_path.read_text(encoding="utf-8"))
    taxonomy = load_taxonomy(taxonomy_path)
    cats = {c["key"]: c for c in taxonomy["categories"]}
    cats[taxonomy["uncategorized"]["key"]] = taxonomy["uncategorized"]
    summaries = {}
    if summaries_path and summaries_path.exists():
        # sub-agent が BOM 付きで書く場合があるため utf-8-sig で読む
        summaries = json.loads(summaries_path.read_text(encoding="utf-8-sig"))

    period_start = (datetime.fromisoformat(data["base_date"]) - timedelta(days=1)).date()
    period_end = (datetime.fromisoformat(data["head_date"]) - timedelta(days=1)).date()

    by_cat: dict[str, list] = defaultdict(list)
    for it in data["items"]:
        by_cat[it["category"]].append(it)

    n_total = len(data["items"])
    n_cosmetic = sum(1 for i in data["items"] if i["cosmetic"])
    dist = sorted(
        ((k, len(v)) for k, v in by_cat.items()), key=lambda kv: -kv[1]
    )
    dist_txt = "、".join(f"「{cats[k]['name']}」{n}件" for k, n in dist)

    L = [
        "---",
        f"対象期間: {period_start:%Y年%m月%d日} 〜 {period_end:%Y年%m月%d日}",
        f"作成日: {period_end:%Y-%m-%d}",
        "形式: カテゴリ別詳細・試作版（ハイライト/新着情報セクション廃止、全変更点をカテゴリ下に並列列挙）",
        "---",
        "",
        "# Claude Code 公式ドキュメント更新サマリ（カテゴリ別詳細・試作）",
        "",
        "```markdown",
        f"今回の変更は {n_total} 項目"
        + (f"（うち書式のみの変更 {n_cosmetic} 件）" if n_cosmetic else "")
        + f"。内訳は {dist_txt}。",
        "```",
        "",
        "## カテゴリ別の変更点",
        "",
    ]

    order = [c["key"] for c in taxonomy["categories"]] + [taxonomy["uncategorized"]["key"]]
    empty = []
    for key in order:
        cat = cats[key]
        its = by_cat.get(key, [])
        if not its:
            empty.append(f"**{cat['icon']} {cat['name']}**")
            continue
        L.append(f"### {cat['icon']} {cat['name']} — {len(its)}件")
        L.append("")
        for it in its:
            summary = summaries.get(it["id"]) or _fallback_summary(it)
            url = DOCS_BASE + it["slug"] if it["slug"] else ""
            if it["section"]:
                url += "#" + gfm_anchor(it["section"])
            loc = it["page_title"] or it["slug"]
            if it["section"]:
                loc += f" › {it['section']}"
            badge = {"new_page": "🆕新規ページ ", "removed_page": "🗑削除 "}.get(it["kind"], "")
            cosmetic = "〔書式のみ〕" if it["cosmetic"] else ""
            rel = (
                "〔関連: " + ", ".join(cats[s]["name"] for s in it["secondary"]) + "〕"
                if it["secondary"]
                else ""
            )
            L.append(f"- {badge}**{loc}**: {summary}{cosmetic}{rel} — [English]({url})")
        L.append("")

    if empty:
        L += ["### 今回変更のなかったカテゴリ", "", " / ".join(empty), ""]

    L += [
        "## 分類の根拠（付録）",
        "",
        "| 項目 | 主カテゴリ | スコア | マッチした語彙 |",
        "|---|---|---:|---|",
    ]
    for it in data["items"]:
        loc = (it["slug"] or "?") + (f"#{it['section']}" if it["section"] else "")
        L.append(
            f"| {loc} | {cats[it['category']]['name']} | {it['match_score']} | {', '.join(it['matched_vocab']) or '—'} |"
        )
    L += [
        "",
        "<!--",
        f"base_commit: {data['base']}",
        f"head_commit: {data['head']}",
        "generator: build_category_summary.py (trial)",
        "-->",
        "",
    ]
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(L), encoding="utf-8", newline="\n")
    print(f"written: {out_path} ({n_total} items)")


def _fallback_summary(it):
    """LLM 要約が無い項目用の機械フォールバック。"""
    if it["kind"] == "new_page":
        first = it["added_excerpt"][0] if it["added_excerpt"] else ""
        return f"新規ページが追加された。{first.strip()}"
    if it["kind"] == "removed_page":
        return "ページがインデックスから削除された。"
    a, r = len(it["added_excerpt"]), len(it["removed_excerpt"])
    return f"本文が更新された（+{a}行 / -{r}行、機械フォールバック要約）。"


# --- render (エントリ形式・LLM 編集版) ----------------------------------------------
#
# entries JSON:
#   {"entries": [{
#      "item_ids": [...],                       # 統合: 1 エントリ = 複数 item
#      "categories": [<cat key>, ...],          # 複数カテゴリ掲載
#      "subcategories": {<cat key>: <sub key>}, # サブ区分を持つカテゴリごとの所属（任意）
#      "label": "...", "summary": "..."
#   }]}
# LLM（Opus）が意味的に分類・統合・要約した結果を受け取り、複数カテゴリ掲載・
# カテゴリ内統合・サブ区分・changelog のカテゴリ別分割をサポートして md を組み立てる。
#
# item_id は原則 1 エントリに属するが、1 つの変更（例: changelog への追記）が
# 複数カテゴリの内容を束ねている場合に限り、カテゴリごとに分割した複数エントリが
# 同じ item_id を共有してよい（各エントリの summary は当該カテゴリの内容のみを書く）。


def entry_subcategory(entry: dict, cat_key: str, subcats: list[dict]) -> str:
    """エントリの当該カテゴリにおけるサブ区分 key を返す（不正・未指定は先頭区分）。"""
    valid = {s["key"] for s in subcats}
    val = (entry.get("subcategories") or {}).get(cat_key)
    if val is None and cat_key == "enterprise":
        val = entry.get("enterprise_sub")  # 旧形式との後方互換
    return val if val in valid else subcats[0]["key"]


def render_entries(items_path: Path, entries_path: Path, taxonomy_path: Path, out_path: Path):
    data = json.loads(items_path.read_text(encoding="utf-8"))
    taxonomy = load_taxonomy(taxonomy_path)
    cats = {c["key"]: c for c in taxonomy["categories"]}
    unc_key = taxonomy["uncategorized"]["key"]
    cats[unc_key] = taxonomy["uncategorized"]
    entries = json.loads(entries_path.read_text(encoding="utf-8-sig"))["entries"]
    items_by_id = {i["id"]: i for i in data["items"]}

    # 検証: 全 item がいずれかのエントリに属すること。漏れは機械分類で単独エントリ化
    covered = set()
    for e in entries:
        covered.update(e["item_ids"])
    auto_added = 0
    for it in data["items"]:
        if it["id"] not in covered:
            entries.append(
                {"item_ids": [it["id"]], "categories": [it["category"]], "summary": _fallback_summary(it)}
            )
            auto_added += 1
    if auto_added:
        print(f"WARN: {auto_added} 項目がエントリ未包含のため機械分類で自動補完")

    for e in entries:
        e["categories"] = [c for c in e["categories"] if c in cats] or [unc_key]
        e["_items"] = [items_by_id[i] for i in e["item_ids"] if i in items_by_id]

    by_cat: dict[str, list] = defaultdict(list)
    for e in entries:
        for c in e["categories"]:
            by_cat[c].append(e)

    period_start = (datetime.fromisoformat(data["base_date"]) - timedelta(days=1)).date()
    period_end = (datetime.fromisoformat(data["head_date"]) - timedelta(days=1)).date()
    n_items = len(data["items"])
    n_entries = len(entries)
    dist = sorted(((k, len(v)) for k, v in by_cat.items()), key=lambda kv: -kv[1])
    dist_txt = "、".join(f"「{cats[k]['name']}」{n}件" for k, n in dist)

    def entry_line(e):
        locs, seen = [], set()
        for it in e["_items"]:
            key = (it["slug"], it["section"])
            if key not in seen:
                seen.add(key)
                locs.append(it)
        if len(locs) == 1:
            it = locs[0]
            fallback = (it["page_title"] or it["slug"]) + (f" › {it['section']}" if it["section"] else "")
            url = DOCS_BASE + it["slug"] + (("#" + gfm_anchor(it["section"])) if it["section"] else "")
            links = f"[English]({url})"
        else:
            n_pages = len({i["slug"] for i in locs})
            fallback = f"{n_pages}ページ・{len(locs)}セクション"
            parts = []
            for it in locs[:3]:
                url = DOCS_BASE + it["slug"] + (("#" + gfm_anchor(it["section"])) if it["section"] else "")
                parts.append(f"[{it['slug']}]({url})")
            links = " / ".join(parts) + (f" ほか{len(locs) - 3}箇所" if len(locs) > 3 else "")
        # 見出しは LLM の label（内容を表す短い日本語＝要約の更に要約）を優先。
        # 場所情報は末尾リンクが担う
        label = (e.get("label") or "").strip() or fallback
        badge = "🆕新規ページ " if any(i["kind"] == "new_page" for i in e["_items"]) else ""
        return f"- {badge}**{label}**: {e['summary']} — {links}"

    L = [
        "---",
        f"対象期間: {period_start:%Y年%m月%d日} 〜 {period_end:%Y年%m月%d日}",
        f"作成日: {period_end:%Y-%m-%d}",
        "形式: カテゴリ別詳細・試作版 v3（Opus 意味分類・カテゴリ内統合・複数カテゴリ掲載・内容ラベル見出し・エンタープライズサブ区分・ドキュメント改善分離）",
        "---",
        "",
        "# Claude Code 公式ドキュメント更新サマリ（カテゴリ別詳細・試作 v3）",
        "",
        "```markdown",
        f"今回の変更 {n_items} 項目を {n_entries} エントリに集約。カテゴリ別の掲載数は {dist_txt}"
        "（1 エントリが複数カテゴリに掲載される場合は重複計上）。",
        "```",
        "",
        "## カテゴリ別の変更点",
        "",
    ]
    order = [c["key"] for c in taxonomy["categories"]] + [unc_key]
    empty = []
    for key in order:
        cat = cats[key]
        es = by_cat.get(key, [])
        if not es:
            empty.append(f"**{cat['icon']} {cat['name']}**")
            continue
        L.append(f"### {cat['icon']} {cat['name']} — {len(es)}件")
        L.append("")
        subcats = cat.get("subcategories")
        if subcats:
            # サブ区分を持つカテゴリは区分順にグルーピング（未指定・不明値は先頭区分へ）
            by_sub: dict[str, list] = defaultdict(list)
            for e in es:
                by_sub[entry_subcategory(e, key, subcats)].append(e)
            for s in subcats:
                ses = by_sub.get(s["key"], [])
                if not ses:
                    continue
                L.append(f"**{s['name']}**")
                L.append("")
                L.extend(entry_line(e) for e in ses)
                L.append("")
        else:
            L.extend(entry_line(e) for e in es)
            L.append("")
    if empty:
        L += ["### 今回変更のなかったカテゴリ", "", " / ".join(empty), ""]

    # 同じ item を共有する複数エントリ = changelog のカテゴリ別分割
    id_uses = Counter(i for e in entries for i in e["item_ids"])
    n_split = sum(1 for e in entries if any(id_uses[i] > 1 for i in e["item_ids"]))

    L += [
        "## 分類の内訳（付録）",
        "",
        "LLM（Opus）による意味分類と、語彙マッチによる機械分類（参考）の対比。"
        + ("「分割」= 1 つの changelog 等をカテゴリ別に分けたエントリ。" if n_split else ""),
        "",
        "| エントリ | LLM 分類 | 機械分類（参考） | 統合項目数 | 分割 |",
        "|---|---|---|---:|:--:|",
    ]
    for e in entries:
        first = e["_items"][0] if e["_items"] else None
        loc = (first["slug"] + (f"#{first['section']}" if first["section"] else "")) if first else "?"
        if len(e["_items"]) > 1:
            loc += " ほか"
        llm_c = ", ".join(cats[c]["name"] for c in e["categories"])
        mech_c = ", ".join(sorted({cats.get(i["category"], cats[unc_key])["name"] for i in e["_items"]}))
        split = "✔" if any(id_uses[i] > 1 for i in e["item_ids"]) else ""
        L.append(f"| {loc} | {llm_c} | {mech_c} | {len(e['item_ids'])} | {split} |")
    L += [
        "",
        "<!--",
        f"base_commit: {data['base']}",
        f"head_commit: {data['head']}",
        "generator: build_category_summary.py render --entries (trial v3)",
        "-->",
        "",
    ]
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(L), encoding="utf-8", newline="\n")
    print(f"written: {out_path} ({n_items} items -> {n_entries} entries)")


# --- prompt（LLM 編集工程の指示文を taxonomy から自動生成） ---------------------------
#
# カテゴリ一覧を categories.json とプロンプトに二重管理すると、片方だけの編集が
# エラーにならず静かに壊れる（追加したカテゴリが永久に 0 件になる等）。
# ここで taxonomy から指示文を生成し、categories.json を単一の真実とする。

PROMPT_TEMPLATE = """あなたは Claude Code 公式ドキュメント更新サマリの編集者です。
{items_path} を Read で読んでください（大きい場合は offset/limit で分割し、**全件**読むこと）。

各 item は公式ドキュメントの変更点 1 件です（slug / page_title / section / added_excerpt /
removed_excerpt。category と matched_vocab は語彙マッチによる機械分類の**参考値**）。

## 1. 意味分類

各変更点の内容を意味的に解釈し、以下のカテゴリ key を 1〜3 個割り当てる（機械分類は参考に留め、
内容で判断する）。変更が複数領域に本質的に関わる場合、複数カテゴリへの割当てはむしろ望ましい。

{category_list}
- uncategorized（どうしても当てはまらない場合のみ）

**docs-improvement の特別ルール**: 文体統一・表記や名称の統一・書式調整・単なるリンク張替え・
誤字修正など、**Claude Code の機能面の変更や仕様理解の実質的更新を伴わない差分**は
docs-improvement **単独**に分類する（他カテゴリと併記しない）。一方、記述変更でも挙動の明確化・
新情報の追加（仕様理解が変わる修正）は機能カテゴリへ入れる。

## 2. サブ区分

以下のカテゴリはサブ区分を持つ。該当カテゴリに分類したエントリには、"subcategories" に
{{"<カテゴリ key>": "<サブ区分 key>"}} を必ず付与する（複数の該当カテゴリがあれば各々に付与）。

{subcategory_list}

## 3. カテゴリ内統合

同一カテゴリ内で並べると冗長になる項目（同一ページ／同趣旨の調整の繰り返し、同一リリースの
バージョン表記追記の繰り返し等）は 1 エントリに統合する（item_ids を複数持たせる）。
意味の異なる実質的変更を 1 つに潰さないこと。

## 4. changelog のカテゴリ別分割（統合の逆操作）

1 つの変更（典型的には changelog やリリースノート、バージョン履歴表への追記）が、**複数カテゴリ
の内容を単に束ねて記載しているだけ**の場合は、**カテゴリごとに別エントリへ分割**する。
このときに限り、同じ item_id を複数のエントリが共有してよい。

分割した各エントリの summary には、**そのカテゴリに対応する変更内容だけ**を書く（他カテゴリの
内容を混ぜない）。label は共通でよい。

悪い例（1 エントリを 3 カテゴリに掲載し、要約に全部を混ぜる）:
  {{"item_ids": ["item48"], "categories": ["permission-security", "session-context", "apps-platform"],
    "label": "v2.1.200/201 更新ログ追加",
    "summary": "AskUserQuestion の自動継続廃止、パーミッションモードの改称、バックグラウンド
    セッションの修正、スクリーンリーダー出力の改善などが含まれる。"}}

良い例（カテゴリごとに分割し、各要約は当該カテゴリの内容のみ）:
  {{"item_ids": ["item48"], "categories": ["permission-security"],
    "label": "v2.1.200/201 更新ログ追加",
    "summary": "パーミッションモード「default」が「Manual」へ改称された。"}}
  {{"item_ids": ["item48"], "categories": ["session-context"],
    "label": "v2.1.200/201 更新ログ追加",
    "summary": "バックグラウンドセッションの各種修正が入った。"}}
  {{"item_ids": ["item48"], "categories": ["apps-platform"],
    "label": "v2.1.200/201 更新ログ追加",
    "summary": "AskUserQuestion のデフォルト自動継続が廃止され、スクリーンリーダー出力が改善された。"}}

**判断基準**: その変更が「1 つの話題が複数領域に波及している」なら分割せず複数カテゴリ掲載
（同じ要約でよい）。「複数の独立した話題が 1 箇所にまとめて記載されている」なら分割する。

## 5. label（内容ラベル）

各エントリに "label" = 変更内容を一言で表す日本語見出し（10〜20 字目安・体言止め）。
ページ名の直訳ではなく**内容の要約**にする。例: "auto mode の信頼設定", "プロバイダ名称の一斉統一"

## 6. 要約

各エントリに日本語 1〜3 文の "summary"（常体「〜された。」）。差分から「何がどう変わり、
読者にとって何が変わるか」が分かる自然で具体的な文にする。excerpt から読み取れないことは
推測で書かない。新規ページ（kind=new_page）は「新規ページ。<内容説明>」とする。

## 出力

Write ツールで {out_path} に以下の JSON を書く:

{{"entries": [
  {{"item_ids": ["item01"], "categories": ["permission-security"],
    "label": "…", "summary": "…"}},
  {{"item_ids": ["item02"], "categories": ["enterprise"],
    "subcategories": {{"enterprise": "bedrock-aws"}}, "label": "…", "summary": "…"}}
]}}

**制約**: 全 item_id を最低 1 つのエントリの item_ids に含める（漏れ厳禁）。同一 item_id の
複数エントリへの重複は、上記 4（changelog のカテゴリ別分割）の場合に限り許可。
最終メッセージは「done: <エントリ数> entries / <項目数> items」のみ。
"""


def build_prompt(taxonomy_path: Path, items_path: str, out_path: str) -> str:
    taxonomy = load_taxonomy(taxonomy_path)
    cat_lines, sub_lines = [], []
    for c in taxonomy["categories"]:
        desc = c.get("prompt_hint") or c["name"]
        cat_lines.append(f"- {c['key']}（{desc}）")
        if c.get("subcategories"):
            subs = " / ".join(f"{s['key']}（{s['name']}）" for s in c["subcategories"])
            sub_lines.append(f"- **{c['key']}**: {subs}")
    return PROMPT_TEMPLATE.format(
        items_path=items_path,
        out_path=out_path,
        category_list="\n".join(cat_lines),
        subcategory_list="\n".join(sub_lines) or "（サブ区分を持つカテゴリは現在ない）",
    )


# --- main --------------------------------------------------------------------------


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)

    ex = sub.add_parser("extract")
    ex.add_argument("--base", required=True)
    ex.add_argument("--head", required=True)
    ex.add_argument("--taxonomy", default=str(Path(__file__).parent / "categories.json"))
    ex.add_argument("--out", required=True)
    ex.add_argument("--excerpt-lines", type=int, default=30)

    rd = sub.add_parser("render")
    rd.add_argument("--items", required=True)
    rd.add_argument("--summaries", default=None)
    rd.add_argument("--entries", default=None, help="LLM 編集済みエントリ JSON（--summaries より優先）")
    rd.add_argument("--taxonomy", default=str(Path(__file__).parent / "categories.json"))
    rd.add_argument("--out", required=True)

    pr = sub.add_parser("prompt", help="LLM 編集工程の指示文を taxonomy から生成")
    pr.add_argument("--items", required=True, help="LLM に読ませる items JSON のパス")
    pr.add_argument("--entries-out", required=True, help="LLM に書かせる entries JSON のパス")
    pr.add_argument("--taxonomy", default=str(Path(__file__).parent / "categories.json"))
    pr.add_argument("--out", default=None, help="省略時は標準出力")

    args = ap.parse_args()
    if args.cmd == "extract":
        taxonomy = load_taxonomy(Path(args.taxonomy))
        items = extract_items(args.base, args.head)
        out_items = []
        for n, it in enumerate(items, 1):
            primary, secondary, hits, score = classify(it, taxonomy)
            out_items.append(
                {
                    "id": f"item{n:02d}",
                    "slug": it["slug"],
                    "page_title": it["page_title"],
                    "section": it["section"],
                    "kind": it["kind"],
                    "cosmetic": it["cosmetic"],
                    "hunks": it["hunks"],
                    "category": primary,
                    "secondary": secondary,
                    "matched_vocab": hits,
                    "match_score": score,
                    "added_excerpt": it["added"][: args.excerpt_lines],
                    "removed_excerpt": it["removed"][: args.excerpt_lines // 2],
                }
            )
        payload = {
            "base": args.base,
            "head": args.head,
            "base_date": commit_date(args.base).isoformat(),
            "head_date": commit_date(args.head).isoformat(),
            "items": out_items,
        }
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out).write_text(
            json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n"
        )
        print(f"extracted: {args.out} ({len(out_items)} items)")
    elif args.cmd == "prompt":
        text = build_prompt(Path(args.taxonomy), args.items, args.entries_out)
        if args.out:
            Path(args.out).parent.mkdir(parents=True, exist_ok=True)
            Path(args.out).write_text(text, encoding="utf-8", newline="\n")
            print(f"written: {args.out}")
        else:
            print(text)
    elif args.entries:
        render_entries(Path(args.items), Path(args.entries), Path(args.taxonomy), Path(args.out))
    else:
        render(
            Path(args.items),
            Path(args.summaries) if args.summaries else None,
            Path(args.taxonomy),
            Path(args.out),
        )


if __name__ == "__main__":
    sys.exit(main())
