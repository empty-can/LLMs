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

Machine-stable invariants
-------------------------
The following structural contracts are relied on by scan, check, and inject.
Future template or generator changes that violate them will silently break the
pipeline:

  Light block markers
    ``<!-- light:<section>:start -->`` / ``<!-- light:<section>:end -->``
    delimit named sections in latest.md. The watch pipeline does not parse
    these but the generator must keep them consistent with latest-detail.md.

  URL convention
    All official links use ``https://code.claude.com/docs/en/<slug>(#<anchor>)``.
    The en<->ja mapping is a literal prefix swap: ``/docs/en/`` -> ``/docs/ja/``.
    The anchor id is the same on both en and ja pages (Mintlify reuses the
    English slug id for Japanese headings).

  Highlight heading format
    ``## N. <title>`` (two hashes, a 1-or-more-digit number, a dot, the title).
    Used by HL_HEAD_RE and find_linkless_highlights.

  Injected form (Markdown only, no HTML)
    ``[日本語](<ja_url>) / [<label>](<en_url>)``
    Inject writes plain Markdown and never adds HTML attributes such as
    ``target="_blank"``. The exact label of the en link is preserved from the
    original. cmd_inject looks for ``[English](<en_url>)`` specifically, so
    long-label links injected by a future phase must be handled separately.
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
from dataclasses import dataclass
from pathlib import Path

EN_PREFIX = "https://code.claude.com/docs/en/"
# any Markdown link whose URL starts with the en prefix, capturing label / url / slug / anchor
_ANY_EN_LINK_RE = re.compile(
    r"\[([^\]]+)\]\((" + re.escape(EN_PREFIX) + r"([^)#]+?)(?:#([^)]+))?)\)"
)
# 日本語 link immediately before an en link in the same line (already-injected pair, form 3)
_JA_BEFORE_RE = re.compile(
    r"\[日本語\]\(https://code\.claude\.com/docs/ja/[^)]+\)\s*/\s*\Z"
)
# inline-code tokens on a line, candidates for a non-translatable reflection probe
TERM_RE = re.compile(r"`([^`\s]{2,})`")
UA = "doc-summary-watch/1.0 (+https://github.com/empty-can/LLMs)"
# a numbered highlight detail heading ("## 3. title"). Its section is expected to
# carry an official doc link; one with none is the req4 "page not created yet ->
# emitted link-less" case (see find_linkless_highlights / the scan WARNING).
HL_HEAD_RE = re.compile(r"^##\s+(\d+)\.\s+(.+?)\s*$")
DOC_LINK_RE = re.compile(r"code\.claude\.com/docs/(?:en|ja)/")
# req4 excludes changelog-derived highlights from the page-link watch. The generator
# marks such an intentional omission with BOTH a "changelog" mention and a
# "...リンクは省略します" note; a link-less highlight carrying both is permanently
# link-less by design (and recurs every run), so the guard skips it. A genuinely
# page-pending highlight lacks the changelog mention and is still flagged.
CHANGELOG_RE = re.compile(r"changelog", re.IGNORECASE)
LINK_OMIT_RE = re.compile(r"リンク[^。\n]{0,8}省略")


@dataclass
class DocLink:
    """A single Claude Code Docs en-link occurrence parsed from a summary file.

    Fields
    ------
    label       : anchor text of the Markdown link (e.g. "English" or the long title)
    en_url      : full en URL including anchor if present
    ja_url      : en_url with /docs/en/ -> /docs/ja/
    slug        : path segment after /docs/en/ WITHOUT the anchor
    anchor      : fragment id without the leading "#", or ""
    already_ja  : True when this occurrence is form 3 (a 日本語 link is paired
                  immediately before it on the same line)
    en_link_text: the exact matched en-link substring "[<label>](<en_url>)" so a
                  later phase can do a targeted string replacement
    """
    label: str
    en_url: str
    ja_url: str
    slug: str
    anchor: str
    already_ja: bool
    en_link_text: str


def iter_doc_links(text: str):
    """Yield a DocLink for EVERY Claude Code Docs en-link in *text*.

    Recognises all three link forms produced by the summary generator:

      Form 1 - short label:
        ``[English](https://code.claude.com/docs/en/<slug>(#<anchor>))``
      Form 2 - long label (highlight / new-page / updated-page sections):
        ``[<any title text> (English)](https://code.claude.com/docs/en/<slug>(#<anchor>))``
      Form 3 - already-injected pair (already_ja=True):
        ``[日本語](<ja_url>) / [<label>](<en_url>)``

    Yields one DocLink per occurrence. For form 3 the occurrence is yielded with
    already_ja=True so callers can skip it when seeding new registry items.
    """
    for line in text.split("\n"):
        for m in _ANY_EN_LINK_RE.finditer(line):
            label = m.group(1)
            en = m.group(2)
            slug = m.group(3)
            anchor = m.group(4) or ""
            en_link_text = m.group(0)  # full "[<label>](<en_url>)" substring

            # form 3: a 日本語 link appears immediately before this match on the line
            prefix = line[: m.start()]
            already_ja = bool(_JA_BEFORE_RE.search(prefix))

            yield DocLink(
                label=label,
                en_url=en,
                ja_url=ja_url(en),
                slug=slug,
                anchor=anchor,
                already_ja=already_ja,
                en_link_text=en_link_text,
            )


def _gh_slug(heading_text: str) -> str:
    """GitHub-style anchor slug from a Markdown heading text (no leading #)."""
    s = heading_text.lower()
    s = re.sub(r"[^\w\s-]", "", s)   # drop chars other than word chars, spaces, hyphens
    s = re.sub(r"\s+", "-", s.strip())
    return s


def section_body(body: str, anchor: str) -> str:
    """Return the slice of *body* belonging to the section identified by *anchor*.

    Handles both shapes that ``fetch_ja`` may return:

    * **Rendered HTML**: locates ``id="<anchor>"`` or ``id='<anchor>'``; the section
      runs from that point to the next ``<h1``..``<h6`` tag (exclusive), or end-of-body.
    * **Raw Markdown**: locates the heading line whose GitHub-style slug equals
      *anchor*; the section runs from that heading line to the next Markdown
      heading line (``^#{1,6} ``), exclusive.

    Falls back to returning *body* unchanged if the anchor cannot be located in
    either shape (prevents false-negative regression -- the item routes to manual
    rather than being stuck at pending forever).
    """
    # --- HTML shape ---
    # find id="anchor" or id='anchor'
    html_id_re = re.compile(
        r"""id=(?:"(?P<dq>[^"]*?)"|'(?P<sq>[^']*?)')""", re.IGNORECASE
    )
    for m in html_id_re.finditer(body):
        found = m.group("dq") if m.group("dq") is not None else m.group("sq")
        if found == anchor:
            start = m.start()
            # find the next heading tag after this point
            next_h = re.search(r"<h[1-6][\s>]", body[start + 1:], re.IGNORECASE)
            end = (start + 1 + next_h.start()) if next_h else len(body)
            return body[start:end]

    # --- Markdown shape ---
    lines = body.split("\n")
    in_section = False
    section_lines: list[str] = []
    heading_re = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
    for line in lines:
        hm = heading_re.match(line)
        if hm:
            if in_section:
                # hit the next heading -> section ends
                break
            slug = _gh_slug(hm.group(2))
            if slug == anchor:
                in_section = True
                section_lines.append(line)
        elif in_section:
            section_lines.append(line)
    if section_lines:
        return "\n".join(section_lines)

    # --- fallback: anchor not found in either shape ---
    return body


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


def find_linkless_highlights(text: str):
    """Return [(num, title)] for numbered highlight sections that warrant an en link
    but carry none -- the req4 "page not created yet -> emitted link-less" case that
    this watch does NOT automate (scan seeds only from existing en links, inject
    anchors on an existing en fragment). Surfacing them keeps an unattended run from
    dropping them silently.

    Changelog-derived highlights are link-less *by design* (req4 excludes them) and
    recur every run; the generator marks them with both a "changelog" mention and a
    "...リンクは省略します" note, so a section carrying both is skipped to avoid crying
    wolf. A genuinely page-pending highlight lacks the changelog mention -> flagged.
    """
    out: list[tuple[str, str]] = []
    cur = None                      # [num, title]
    has_link = has_cl = has_omit = False
    for line in text.split("\n"):
        m = HL_HEAD_RE.match(line)
        if m or (line.startswith("## ") and cur):
            if cur and not has_link and not (has_cl and has_omit):
                out.append((cur[0], cur[1]))
            cur = [m.group(1), m.group(2)] if m else None
            has_link = has_cl = has_omit = False
            continue
        if cur:
            if DOC_LINK_RE.search(line):
                has_link = True
            if CHANGELOG_RE.search(line):
                has_cl = True
            if LINK_OMIT_RE.search(line):
                has_omit = True
    if cur and not has_link and not (has_cl and has_omit):
        out.append((cur[0], cur[1]))
    return out


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
    # 一時ファイルへ書いてから置換する。registry.json は 600KB を超えるため、宛先を直接
    # truncate + write すると書き込み中の中断（kill / 電源断 / ディスク満杯）で壊れた JSON が
    # 残り、以後 load_registry が毎回 JSONDecodeError で落ち続ける（復旧は git 履歴からの
    # 手作業）。Path.replace は同一ディレクトリなら原子的に差し替わる。
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_name(p.name + ".tmp")
    tmp.write_bytes(s.encode("utf-8"))
    tmp.replace(p)


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
    n_revived = 0
    n_linkless = 0
    linkless: list[str] = []   # registry keys of link-less highlights seen this run
    for name, detail, _light in iter_pairs(sr):
        if not detail.is_file():
            continue
        text = read_text(detail)
        for line in text.split("\n"):
            for lnk in iter_doc_links(line):
                if lnk.already_ja:
                    # form 3: already injected -- not a new watch target
                    continue
                n_seen += 1
                key = f"{name}::{lnk.en_url}"
                if key in items:
                    # G1: latest-detail.md is regenerated each period. If a
                    # previously injected en link reappears in the LIVE file WITHOUT
                    # its ja link (the regenerated live re-surfaced it un-injected,
                    # i.e. already_ja is False here), revive it so check/inject
                    # reprocess it. Archives are frozen snapshots -> never revived.
                    it = items[key]
                    if name == "live" and it["status"] == "injected":
                        it["status"] = "pending"
                        it["injected_at"] = None
                        it["last_checked"] = None
                        n_revived += 1
                    continue
                term, strong = pick_probe(line)
                items[key] = {
                    "name": name,
                    "en_url": lnk.en_url,
                    "ja_url": lnk.ja_url,
                    "slug": lnk.slug,
                    "anchor": lnk.anchor,
                    "kind": "ja-section" if lnk.anchor else "ja-page",
                    "term": term,
                    "strong": strong,
                    "status": "pending",
                    "first_seen": today(),
                    "last_checked": None,
                    "injected_at": None,
                }
                n_new += 1
        for num, title in find_linkless_highlights(text):
            # persist the link-less highlight so it survives across runs and can be
            # resolved later (its official page does not exist yet, so there is no URL
            # to predict -- a maintainer attaches it via 'resolve' once it appears).
            key = f"{name}::linkless::{num}::{title}"
            if key not in items:
                items[key] = {
                    "name": name,
                    "kind": "linkless-highlight",
                    "hl_num": num,
                    "title": title,
                    "en_url": None,
                    "ja_url": None,
                    "slug": None,
                    "anchor": None,
                    "term": None,
                    "strong": False,
                    "status": "linkless",     # awaiting human 'resolve'
                    "first_seen": today(),
                    "last_checked": None,
                    "injected_at": None,
                }
                n_linkless += 1
            linkless.append(key)
    save_registry(rp, reg)
    print(f"scan: +{n_new} new, +{n_linkless} linkless, {n_revived} revived, "
          f"{n_seen} en-only links seen, {len(items)} in registry")
    print(f"      registry: {rp}")
    unresolved = [k for k in linkless if items[k]["status"] == "linkless"]
    if unresolved:
        print(f"\nWARNING: {len(unresolved)} link-less highlight(s) -- official page not")
        print("         created yet. When a page appears, attach it with:")
        print("           watch.py resolve --key <KEY> --url <en-url> [--probe <token>]")
        for k in unresolved:
            it = items[k]
            print(f"  ! {it['name']:>12}  #{it['hl_num']} {it['title']}")
            print(f"      key: {k}")
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
            if term in section_body(body, anchor):
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


def inject_ja_into_text(text: str, en_url: str, ja_url: str):
    """Prefix ``[日本語](ja_url) / `` before EVERY un-injected occurrence of the en
    link ``[<label>](en_url)`` in *text*, preserving each occurrence's own label.

    Returns ``(new_text, n_inserted)``. Safe against double-injection: an occurrence
    already preceded by a 日本語 link (form 3) is left untouched. Replacement is done
    per line via ``re.sub`` with a callback, so only original match spans are
    considered and inserted text is never re-processed (a blind ``str.replace`` would
    corrupt an already-injected occurrence whose ``[label](en_url)`` substring is
    identical to a not-yet-injected one).
    """
    n = 0

    def repl(m: "re.Match") -> str:
        nonlocal n
        if m.group(2) != en_url:
            return m.group(0)                       # a different page -> leave as-is
        if _JA_BEFORE_RE.search(m.string[: m.start()]):
            return m.group(0)                       # already injected -> leave as-is
        n += 1
        return f"[日本語]({ja_url}) / {m.group(0)}"

    # per line so _JA_BEFORE_RE's end-anchored prefix check cannot span lines
    out = [_ANY_EN_LINK_RE.sub(repl, line) for line in text.split("\n")]
    return "\n".join(out), n


def insert_link_in_highlight(text: str, hl_num: str, link_line: str):
    """Insert *link_line* at the end of the ``## <hl_num>. <title>`` highlight section.

    A resolved link-less highlight has no existing ``[English](url)`` to anchor to, so
    the link is appended after the section's last non-blank line (mirroring where a
    normal highlight carries its trailing reference link), preceded by a blank line.
    Returns ``(new_text, inserted)``; *inserted* is False if the section is not found
    or the exact link_line is already present in it (idempotent).
    """
    lines = text.split("\n")
    head_re = re.compile(r"^##\s+" + re.escape(hl_num) + r"\.\s")
    start = next((i for i, ln in enumerate(lines) if head_re.match(ln)), None)
    if start is None:
        return text, False
    end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")),
               len(lines))
    if any(lines[i].strip() == link_line.strip() for i in range(start, end)):
        return text, False
    last = end - 1
    while last > start and lines[last].strip() == "":
        last -= 1
    new_lines = lines[: last + 1] + ["", link_line] + lines[last + 1:]
    return "\n".join(new_lines), True


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
        # resolved link-less highlight: no existing en link -> INSERT a new link line
        # into the highlight section (detail only; light highlight bullets carry no
        # official link). Normal items fall through to the replace-all path below.
        if it.get("insert_hl"):
            detail = pairs[name][0]
            label = f"{name} #{it['hl_num']} {it['title']}"
            if not detail.is_file():
                skipped.append((k, "detail file missing"))
                continue
            link_line = f"- [日本語]({it['ja_url']}) / [English]({it['en_url']})"
            new_txt, ins = insert_link_in_highlight(read_text(detail), it["insert_hl"],
                                                    link_line)
            if not ins:
                it["status"] = "injected"          # section gone or already inserted
                it["injected_at"] = it["injected_at"] or today()
                applied.append(label + "  (already present / no-op)")
                continue
            if args.apply:
                write_text(detail, new_txt)
                changed.add(detail)
                it["status"] = "injected"
                it["injected_at"] = today()
            verb = "applied" if args.apply else "would apply"
            applied.append(f"{label}  ({verb} insert)")
            continue
        en_url, ja_u = it["en_url"], it["ja_url"]
        edits = []            # (fp, new_text) for files that gained a ja link
        n_total = 0           # occurrences newly prefixed across both files
        present = False       # the en link exists in at least one file
        for fp in pairs[name]:
            if not fp.is_file():
                continue
            txt = read_text(fp)
            if any(l.en_url == en_url for l in iter_doc_links(txt)):
                present = True
            new_txt, n = inject_ja_into_text(txt, en_url, ja_u)
            if n:
                edits.append((fp, new_txt))
                n_total += n
        label = f"{name} {it['slug']}{('#' + it['anchor']) if it['anchor'] else ''}"
        if not present:
            skipped.append((k, "en link not in current files (regenerated?)"))
            continue
        if not edits:
            # en link present but every occurrence already carries a ja link
            it["status"] = "injected"
            it["injected_at"] = it["injected_at"] or today()
            applied.append(label + "  (already present)")
            continue
        if args.apply:
            for fp, newtxt in edits:
                write_text(fp, newtxt)
                changed.add(fp)
            it["status"] = "injected"
            it["injected_at"] = today()
        verb = "applied" if args.apply else "would apply"
        applied.append(f"{label}  ({verb} x{n_total})")

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
        # 末尾の "(applied x2)" / "(applied insert)" / "(already present)" を落とす。
        # 旧実装はリテラル "  (applied)" を replace していたが、2974519 の inject 刷新で
        # 出力形式が変わって以降どれにも一致せず no-op になっていた。
        body = "\n".join("- " + re.sub(r"\s*\([^)]*\)\s*$", "", s) for s in applied)
        msg = (
            "refactor(official-docs): ja 翻訳追従リンクを自動注入 "
            f"({len([s for s in applied if 'applied' in s])}件)\n\n"
            "req4 watch: live ja ドキュメントへの反映を検出した en 単独リンクへ\n"
            "[日本語] リンクを追加。本文は不変（リンク注入のみ・元ラベル保持・全出現置換）。\n\n"
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


# ------------------------------------------------------------------------ promote
def cmd_promote(args) -> int:
    """Flip ``manual`` items to ``ready`` after a human has verified the ja section.

    ``check`` parks an item as ``manual`` when the ja section heading exists but no
    distinctive code token is available to auto-confirm the content is reflected
    (so a human must glance). Once verified, this promotes it so ``inject`` applies
    it. ``--list`` shows candidates without changing anything; ``--only`` filters by
    a substring of the item key (default: all ``manual`` items).
    """
    sr = summary_root(Path(args.root) if args.root else None)
    rp = registry_path(sr)
    reg = load_registry(rp)
    items = reg["items"]
    manual = [k for k, v in items.items() if v["status"] == "manual"]
    if args.only:
        manual = [k for k in manual if args.only in k]
    if not manual:
        print("promote: no matching 'manual' items")
        return 0

    def line(k: str) -> str:
        it = items[k]
        anc = ("#" + it["anchor"]) if it["anchor"] else ""
        return f"{it['name']:>12}  {it['slug']}{anc}  ->  {it['ja_url']}"

    if args.list:
        print(f"promote: {len(manual)} manual item(s) (no change; pass without --list to promote):")
        for k in manual:
            print(f"  ? {line(k)}")
        return 0
    for k in manual:
        items[k]["status"] = "ready"
    save_registry(rp, reg)
    print(f"promote: {len(manual)} item(s) manual -> ready (run 'inject --apply' to write)")
    for k in manual:
        print(f"  + {line(k)}")
    return 0


# ------------------------------------------------------------------------ resolve
def cmd_resolve(args) -> int:
    """Attach a now-published official URL to a link-less highlight item.

    Link-less items (seeded by scan with status='linkless') have no predicted URL --
    their official page does not exist at generation time. Once the maintainer sees
    the page/section appear, they supply its en URL here; the item becomes a normal
    'pending' item so ``check`` validates the ja reflection and ``inject`` inserts the
    link line into the highlight section. ``--list`` shows candidates; ``--ready``
    skips ``check`` and marks the item ready for ``inject`` immediately.
    """
    sr = summary_root(Path(args.root) if args.root else None)
    rp = registry_path(sr)
    reg = load_registry(rp)
    items = reg["items"]
    linkless = [k for k, v in items.items() if v["status"] == "linkless"]

    if args.list or not args.key:
        if not linkless:
            print("resolve: no 'linkless' items")
        else:
            print(f"resolve: {len(linkless)} linkless item(s):")
            for k in linkless:
                it = items[k]
                print(f"  ? {it['name']:>12}  #{it['hl_num']} {it['title']}")
                print(f"      key: {k}")
        if not args.key:
            return 0

    if args.key not in items:
        print(f"resolve: key not found: {args.key}")
        return 2
    it = items[args.key]
    if it["status"] != "linkless":
        print(f"resolve: item is not linkless (status={it['status']}): {args.key}")
        return 2
    if not args.url:
        print("resolve: --url is required to resolve a key")
        return 2
    en = args.url
    if not en.startswith(EN_PREFIX):
        print(f"resolve: --url must start with {EN_PREFIX}")
        return 2
    slug, _, anchor = en[len(EN_PREFIX):].partition("#")
    it["en_url"] = en
    it["ja_url"] = ja_url(en)
    it["slug"] = slug
    it["anchor"] = anchor
    it["kind"] = "ja-section" if anchor else "ja-page"
    if args.probe:
        it["term"], it["strong"] = args.probe, True
    it["insert_hl"] = it["hl_num"]      # tells inject to INSERT (no existing en link)
    it["status"] = "ready" if args.ready else "pending"
    save_registry(rp, reg)
    nxt = "inject --apply" if args.ready else "check"
    print(f"resolve: {args.key}\n  -> {en}\n  status -> {it['status']} (run '{nxt}' next)")
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
    pp = sub.add_parser("promote", help="flip 'manual' items to 'ready' after human review")
    pp.add_argument("--only", help="substring filter on item key (default: all manual)")
    pp.add_argument("--list", action="store_true", help="list manual items without changing them")
    pr = sub.add_parser("resolve", help="attach a published URL to a link-less highlight")
    pr.add_argument("--key", help="registry key of the linkless item (omit to list)")
    pr.add_argument("--url", help="now-published en URL (https://code.claude.com/docs/en/...)")
    pr.add_argument("--probe", help="distinctive token to gate ja reflection (optional)")
    pr.add_argument("--ready", action="store_true", help="skip check; mark ready for inject now")
    pr.add_argument("--list", action="store_true", help="list linkless items and exit")
    args = ap.parse_args()
    try:
        if args.cmd == "scan":
            return cmd_scan(args)
        if args.cmd == "check":
            return cmd_check(args)
        if args.cmd == "inject":
            return cmd_inject(args)
        if args.cmd == "promote":
            return cmd_promote(args)
        if args.cmd == "resolve":
            return cmd_resolve(args)
    except KeyboardInterrupt:
        return 1
    return 2


if __name__ == "__main__":
    sys.exit(main())
