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
from collections import defaultdict
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
    rd.add_argument("--taxonomy", default=str(Path(__file__).parent / "categories.json"))
    rd.add_argument("--out", required=True)

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
    else:
        render(
            Path(args.items),
            Path(args.summaries) if args.summaries else None,
            Path(args.taxonomy),
            Path(args.out),
        )


if __name__ == "__main__":
    sys.exit(main())
