#!/usr/bin/env python3
"""req4 ja-lag / page-creation link watch for the doc-summary pipeline.

Why this exists
---------------
By req3 every section-anchored official link is emitted **en-only** while the
Japanese translation lags (the ja heading does not yet carry the section). By
req4 a highlight whose official page does not exist yet is emitted **without**
a link. In both cases the missing Japanese/page link must be added later, once
the resource appears.

Key insight (confirmed with the maintainer, 2026-06-12): adding that link is a
purely *additive* edit that changes **no prose**. The target is fully
predetermined at authoring time:

  * ja URL  = en URL with ``/docs/en/`` -> ``/docs/ja/``
  * anchor  = the *same* Mintlify id (ja headings reuse the English slug id)
  * edit    = replace ``[English](<en>)`` with ``[日本語](<ja>) / [English](<en>)``
              in both the detail and the light file (count must be exactly 1).

Because nothing about the edit requires human judgement at injection time, we
automate **detection and injection**. The only thing ever in doubt is whether
the ja section/page is genuinely reflected, which we gate with a two-signal
check (anchor ``id`` present AND, when known, a non-translatable code token
present). The single human/CI boundary we keep is ``git push`` -- this script
never pushes; a maintainer pushes via the secure DPAPI path, or CI pushes with
its own token after ``inject --apply --commit``.

Subcommands
-----------
  scan    (re)seed the registry from en-only links in live + archive summaries.
          No network. Idempotent: existing items keep their status.
  check   re-check each pending/manual item against the live ja docs (network);
          flip to ``ready`` when reflected. No file edits.
  inject  apply ``ready`` items: insert the ja link beside the en link in the
          detail+light pair (exact string replace, count==1). ``--apply`` writes,
          ``--commit`` also commits. Push is intentionally out of scope.

Registry: ``official-doc-update-summary/claude-code-docs/watch/registry.json``
(committed to repo B so CI persists watch state across runs).

Exit codes: 0 ok, 1 runtime error, 2 usage error.
"""
from __future__ import annotations

import argparse
import datetime
import json
import re
import subprocess
import sys
import tempfile
import urllib.error
import urllib.request
from pathlib import Path

EN_PREFIX = "https://code.claude.com/docs/en/"
# en-only official link, capturing full url / slug (may contain '/') / optional anchor
EN_LINK_RE = re.compile(
    r"\[English\]\((" + re.escape(EN_PREFIX) + r"([^)#]+?)(?:#([^)]+))?)\)"
)
# inline-code tokens on a line, candidates for a non-translatable reflection probe
TERM_RE = re.compile(r"`([^`\s]{2,})`")
UA = "doc-summary-watch/1.0 (+https://github.com/empty-can/LLMs)"


def pick_probe(line: str):
    """Pick the most *distinctive* inline-code token on a line as a freshness probe.

    Returns ``(token, strong)``. ``strong`` means the token is identifier-like
    (contains ``_`` / ``.`` / ``-`` / ``/`` or an uppercase letter, or is >= 10
    chars) and so is unlikely to survive translation by coincidence. A strong
    token *present* in the ja page is good evidence the specific change is
    reflected; *absent* is good evidence it is not. A generic token (or none)
    means we cannot auto-confirm freshness -> the item is routed to manual.
    """
    toks = TERM_RE.findall(line)
    if not toks:
        return "", False
    strong = [t for t in toks
              if re.search(r"[._/\-]", t) or re.search(r"[A-Z]", t) or len(t) >= 10]
    if strong:
        return max(strong, key=len), True
    return max(toks, key=len), False


def repo_root() -> Path:
    # scripts -> update-official-doc-summary -> skills -> .claude -> <repo root>
    return Path(__file__).resolve().parents[4]


def summary_root(root: Path | None = None) -> Path:
    return (root or repo_root()) / "official-doc-update-summary" / "claude-code-docs"


def registry_path(sr: Path) -> Path:
    return sr / "watch" / "registry.json"


def today() -> str:
    return datetime.date.today().isoformat()


def read_text(p: Path) -> str:
    # binary read + decode so newlines (LF/CRLF) survive an in-place replace untouched
    return p.read_bytes().decode("utf-8")


def write_text(p: Path, s: str) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(s.encode("utf-8"))


def ja_url(en_url: str) -> str:
    return en_url.replace("/docs/en/", "/docs/ja/", 1)


def iter_pairs(sr: Path):
    """Yield (name, detail_path, light_path) for live + every archive."""
    yield ("live", sr / "latest-detail.md", sr / "latest.md")
    ad = sr / "archives" / "latest-detail"
    if ad.is_dir():
        for p in sorted(ad.glob("*.md")):
            yield (p.stem, p, sr / "archives" / "latest" / f"{p.stem}.md")


def load_registry(rp: Path) -> dict:
    if rp.is_file():
        return json.loads(read_text(rp))
    return {"version": 1, "items": {}}


def save_registry(rp: Path, reg: dict) -> None:
    write_text(rp, json.dumps(reg, ensure_ascii=False, indent=2) + "\n")


# --------------------------------------------------------------------------- scan
def cmd_scan(args) -> int:
    sr = summary_root(Path(args.root) if args.root else None)
    rp = registry_path(sr)
    reg = load_registry(rp)
    items = reg["items"]
    n_new = 0
    n_seen = 0
    for name, detail, _light in iter_pairs(sr):
        if not detail.is_file():
            continue
        for line in read_text(detail).split("\n"):
            if "日本語" in line:  # already has a ja link -> not a watch target
                continue
            for m in EN_LINK_RE.finditer(line):
                en, slug, anchor = m.group(1), m.group(2), m.group(3) or ""
                key = f"{name}::{en}"
                n_seen += 1
                if key in items:
                    continue
                term, strong = pick_probe(line)
                items[key] = {
                    "name": name,
                    "en_url": en,
                    "ja_url": ja_url(en),
                    "slug": slug,
                    "anchor": anchor,
                    "kind": "ja-section" if anchor else "ja-page",
                    "term": term,
                    "strong": strong,
                    "status": "pending",
                    "first_seen": today(),
                    "last_checked": None,
                    "injected_at": None,
                }
                n_new += 1
    save_registry(rp, reg)
    print(f"scan: +{n_new} new, {n_seen} en-only links seen, {len(items)} in registry")
    print(f"      registry: {rp}")
    return 0


# -------------------------------------------------------------------------- check
def http_get(url: str, timeout: int = 25):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return getattr(r, "status", 200), r.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, ""
    except Exception:
        return 0, ""


def fetch_ja(ja: str):
    """Prefer raw markdown (``<slug>.md``); fall back to the rendered page."""
    for u in (ja + ".md", ja):
        status, body = http_get(u)
        if status == 200 and len(body) > 200:
            return u, body
    return None, ""


def cmd_check(args) -> int:
    sr = summary_root(Path(args.root) if args.root else None)
    rp = registry_path(sr)
    reg = load_registry(rp)
    items = reg["items"]
    keys = [k for k, v in items.items() if v["status"] in ("pending", "manual")]
    if args.only:
        keys = [k for k in keys if args.only in k]
    ready, manual, pending = [], [], []
    for k in keys:
        it = items[k]
        used, body = fetch_ja(it["ja_url"])
        it["last_checked"] = today()
        if not body:
            it["status"] = "pending"
            pending.append((k, "absent"))
            continue
        if it["kind"] == "ja-page":
            it["status"] = "ready"          # page existence is unambiguous (GET 200)
            ready.append((k, "ja page exists"))
            continue
        anchor = it["anchor"]
        id_ok = (f'id="{anchor}"' in body) or (f"id='{anchor}'" in body)
        term, strong = it["term"], it.get("strong", False)
        if not id_ok:
            it["status"] = "pending"
            pending.append((k, "section heading not present yet"))
        elif strong and term:
            if term in body:
                it["status"] = "ready"      # distinctive token present -> change reflected
                ready.append((k, f"reflected (`{term}`)"))
            else:
                it["status"] = "pending"    # distinctive token absent -> not yet reflected
                pending.append((k, f"probe `{term}` absent (heading exists, content stale)"))
        else:
            it["status"] = "manual"         # no distinctive probe -> human glance needed
            manual.append((k, "section exists; no distinctive probe"))
    save_registry(rp, reg)
    print(f"check: {len(ready)} ready, {len(manual)} manual, {len(pending)} still pending "
          f"(of {len(keys)} checked)\n")
    if ready:
        print("READY (inject candidates):")
        for k, why in ready:
            it = items[k]
            print(f"  + {it['name']:>12}  {it['slug']}"
                  f"{('#' + it['anchor']) if it['anchor'] else ''}  [{why}]")
    if manual:
        print("\nMANUAL (needs a human decision):")
        for k, why in manual:
            it = items[k]
            print(f"  ? {it['name']:>12}  {it['slug']}#{it['anchor']}  ({why})")
    if args.verbose and pending:
        print("\npending:")
        for k, why in pending:
            it = items[k]
            print(f"  . {it['name']:>12}  {it['slug']}"
                  f"{('#' + it['anchor']) if it['anchor'] else ''}  ({why})")
    return 0


# ------------------------------------------------------------------------- inject
def git(*a) -> None:
    subprocess.run(["git", "-C", str(repo_root()), *a], check=True)


def cmd_inject(args) -> int:
    sr = summary_root(Path(args.root) if args.root else None)
    rp = registry_path(sr)
    reg = load_registry(rp)
    items = reg["items"]
    pairs = {name: (d, l) for name, d, l in iter_pairs(sr)}
    ready = [k for k, v in items.items() if v["status"] == "ready"]
    if not ready:
        print("inject: nothing in 'ready' state (run check first)")
        return 0

    changed: set[Path] = set()
    applied: list[str] = []
    skipped: list[tuple[str, str]] = []
    for k in ready:
        it = items[k]
        name = it["name"]
        if name not in pairs:
            skipped.append((k, "no file pair (live archived?)"))
            continue
        en_frag = f"[English]({it['en_url']})"
        new_frag = f"[日本語]({it['ja_url']}) / {en_frag}"
        edits = []
        ambiguous = False
        for fp in pairs[name]:
            if not fp.is_file():
                continue
            txt = read_text(fp)
            if new_frag in txt:  # already injected here -> idempotent no-op
                continue
            c = txt.count(en_frag)
            if c == 0:
                continue
            if c > 1:
                ambiguous = True
                break
            edits.append((fp, txt.replace(en_frag, new_frag, 1)))
        if ambiguous:
            skipped.append((k, "ambiguous (en link appears >1x in a file)"))
            continue
        label = f"{name} {it['slug']}{('#' + it['anchor']) if it['anchor'] else ''}"
        if not edits:
            it["status"] = "injected"          # both files already carry the ja link
            it["injected_at"] = it["injected_at"] or today()
            applied.append(label + "  (already present)")
            continue
        if args.apply:
            for fp, newtxt in edits:
                write_text(fp, newtxt)
                changed.add(fp)
            it["status"] = "injected"
            it["injected_at"] = today()
        applied.append(label + ("  (applied)" if args.apply else "  (would apply)"))

    if args.apply:
        save_registry(rp, reg)
        changed.add(rp)

    print(f"inject: {len(applied)} item(s) "
          f"{'applied' if args.apply else 'planned (dry-run; pass --apply)'}, "
          f"{len(skipped)} skipped")
    for s in applied:
        print(f"  + {s}")
    for k, why in skipped:
        print(f"  - {items[k]['name']} {items[k]['slug']}: {why}")

    if args.apply and args.commit and changed:
        files = sorted(str(p) for p in changed)
        git("add", *files)
        body = "\n".join(f"- {s.replace('  (applied)', '')}" for s in applied)
        msg = (
            "refactor(official-docs): ja 翻訳追従リンクを自動注入 "
            f"({len([s for s in applied if 'applied' in s])}件)\n\n"
            "req4 watch: live ja ドキュメントへの反映を検出した en 単独リンクへ\n"
            "[日本語] リンクを追加。本文は不変（リンク注入のみ・置換数==1検証済）。\n\n"
            f"{body}\n\n"
            "Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>\n"
        )
        with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False,
                                         encoding="utf-8", newline="\n") as fh:
            fh.write(msg)
            msgfile = fh.name
        try:
            git("commit", "-F", msgfile)
        finally:
            Path(msgfile).unlink(missing_ok=True)
        print("  committed. push is intentionally NOT performed by this script.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--root", help="repo root override (default: inferred)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("scan", help="seed registry from en-only links (no network)")
    pc = sub.add_parser("check", help="re-check ja reflection (network)")
    pc.add_argument("--only", help="substring filter on item key")
    pc.add_argument("-v", "--verbose", action="store_true", help="also list pending")
    pi = sub.add_parser("inject", help="apply ready items (detail+light)")
    pi.add_argument("--apply", action="store_true", help="write files (default: dry-run)")
    pi.add_argument("--commit", action="store_true", help="git commit applied changes")
    args = ap.parse_args()
    try:
        if args.cmd == "scan":
            return cmd_scan(args)
        if args.cmd == "check":
            return cmd_check(args)
        if args.cmd == "inject":
            return cmd_inject(args)
    except KeyboardInterrupt:
        return 1
    return 2


if __name__ == "__main__":
    sys.exit(main())
