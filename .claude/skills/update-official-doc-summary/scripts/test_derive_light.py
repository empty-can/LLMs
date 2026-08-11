"""Regression tests for derive_light.py (Phase 7: template-driven headings).

Self-contained: the core tests run against an embedded synthetic detail fixture,
so they do not depend on the daily-changing live summary files. An optional smoke
test additionally checks the live latest-detail.md / latest.md pair when present.

Run (from anywhere):
    python .claude/skills/update-official-doc-summary/scripts/test_derive_light.py

Exit code 0 = all pass, 1 = a failure. Run this after editing derive_light.py.
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import derive_light as dl  # noqa: E402

# Repo root is five levels up: <root>/.claude/skills/update-official-doc-summary/scripts/
ROOT = HERE.parents[3]

# --- synthetic detail fixture (mirrors the real template's structure) ------------
FIXTURE = """\
---
対象期間: 2026年01月01日 〜 2026年01月01日
作成日: 2026-01-01
---

# テスト 公式ドキュメント更新サマリ - 詳細版

<!-- light:summary:start -->
```markdown
これはテスト用の概要です。全体傾向を 1 文で述べます。

主要なものを以下に挙げます。

1. [**機能A**](#1-機能a): 機能Aの 1 行要約。
```
<!-- light:summary:end -->

## ハイライト

<!-- light:highlight-list:start -->
1. [**機能A**](#1-機能a):
  機能Aの説明要約。
<!-- light:highlight-list:end -->

## 1. 機能a

機能Aの詳細本文。

- [機能A - Docs (日本語)](https://code.claude.com/docs/ja/x#a)
- [機能A - Docs (English)](https://code.claude.com/docs/en/x#a)

## 新規追加されたページ

<!-- light:new-pages:start -->
（今回の対象期間に新規追加されたページはありません）
<!-- light:new-pages:end -->

## 軽微な更新

<!-- light:minor-updates:start -->
（今回の対象期間に軽微な更新はありません）
<!-- light:minor-updates:end -->

## 関連リンク

- 前回サマリ(ライト版): [./archives/latest/2025-12-31.md](./archives/latest/2025-12-31.md)

<!--
base_commit: abc123
head_commit: def456
generated_at_full: 2026-01-02T15:00:00+09:00
-->
"""

# guide + intro-style comments as they appear at the top of the real template.
GUIDE_BLOCK = """\
<!-- ============================================================
メンテナー編集ガイド ｜ test
● 自由に変えてよい
  - 各セクションの見出し文言（例: 行頭の「ハイライト」見出しを別名に）
  - light マーカー（light:NAME:start / light:NAME:end）は変更不可
============================================================ -->

<!-- intro-style: test 文体指示。常体可。 -->
"""

results: list[tuple[str, bool]] = []


def check(name: str, cond: bool) -> None:
    results.append((name, bool(cond)))


def first_h2(text: str) -> str:
    m = re.search(r"^## .+$", text, re.MULTILINE)
    return m.group(0) if m else ""


# --- core tests (fixture-based, deterministic) -----------------------------------
out = dl.derive(FIXTURE)

check("title strips ' - 詳細版'", out.splitlines()[2 if out.startswith("---") else 0].startswith("# テスト") or "# テスト 公式ドキュメント更新サマリ\n" in out)
check("light title has no '詳細版'", "詳細版" not in out)
check("summary has NO inherited heading (first h2 is ハイライト)", first_h2(out) == "## ハイライト")
check("summary text carried into light", "これはテスト用の概要です" in out)
check("highlight heading inherited", "## ハイライト" in out)
check("new-pages heading inherited", "## 新規追加されたページ" in out)
check("minor-updates heading inherited", "## 軽微な更新" in out)
check("internal link rewritten to detail file", "](./latest-detail.md#1-機能a)" in out)
check("related links block carried", "## 関連リンク" in out)
check("footer carried", "base_commit: abc123" in out)

# section order follows file order: ハイライト < 新規追加 < 軽微
check(
    "section order follows file order",
    0 <= out.find("## ハイライト") < out.find("## 新規追加されたページ") < out.find("## 軽微な更新"),
)

# guide/intro comments are transparent: inserting them must not change light output
ti = FIXTURE.index("# テスト")
te = FIXTURE.index("\n", ti) + 1  # end of title line
fixture_with_guide = FIXTURE[:te] + "\n" + GUIDE_BLOCK + FIXTURE[te:]
check("guide/intro comments transparent", dl.derive(fixture_with_guide) == out)

# heading rename in detail propagates to light
renamed = FIXTURE.replace("## ハイライト", "## 主要な変更点", 1)
out_renamed = dl.derive(renamed)
check("heading rename propagates", "## 主要な変更点" in out_renamed and first_h2(out_renamed) == "## 主要な変更点")

# summary marker removed -> no crash, no summary content, highlights still present
no_summary = re.sub(
    r"<!--\s*light:summary:start\s*-->.*?<!--\s*light:summary:end\s*-->\n?",
    "", FIXTURE, flags=re.DOTALL,
)
try:
    out_ns = dl.derive(no_summary)
    check("summary deletion tolerated", "主要なものを以下に挙げます" not in out_ns and "## ハイライト" in out_ns)
except SystemExit:
    check("summary deletion tolerated", False)

# 概要件数 > ハイライト件数 must still be rejected (guard intact)
too_many = FIXTURE.replace(
    "1. [**機能A**](#1-機能a): 機能Aの 1 行要約。",
    "1. [**機能A**](#1-機能a): a。\n2. [**機能B**](#2-機能b): b。",
    1,
)
try:
    dl.derive(too_many)
    check("概要>ハイライト rejected", False)
except SystemExit:
    check("概要>ハイライト rejected", True)

# --- optional live smoke test ----------------------------------------------------
for site in ("claude-code-docs", "mcp"):
    d = ROOT / "official-doc-update-summary" / site / "latest-detail.md"
    l = ROOT / "official-doc-update-summary" / site / "latest.md"
    if d.is_file() and l.is_file():
        same = dl.derive(d.read_text(encoding="utf-8")) == l.read_text(encoding="utf-8")
        check(f"[live] {site}: derive(latest-detail) == latest", same)
        # 上の比較は改行コードに盲目。read_text は universal newlines で CRLF を \n に潰すため、
        # latest.md が CRLF でも PASS してしまう（実際に 2026-08-11 まで 2 か月間、
        # derive_light.py の write_text が newline 未指定で CRLF を書いていたのを見逃した）。
        # バイト列で明示的に確認する。
        check(f"[live] {site}: latest.md の改行が LF のみ", b"\r\n" not in l.read_bytes())
        check(f"[live] {site}: latest-detail.md の改行が LF のみ", b"\r\n" not in d.read_bytes())

# --- report ----------------------------------------------------------------------
print("=== derive_light.py regression tests ===")
allok = True
for name, ok in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    allok = allok and ok
print("=== ALL PASS ===" if allok else "=== SOME FAILED ===")
sys.exit(0 if allok else 1)
