"""Archive the current latest summary pair into the per-kind archive layout,
rewriting the relative links that change because of the move.

Archive layout (since 2026-06-08):
    <archives_dir>/latest/<name>.md         (light version)
    <archives_dir>/latest-detail/<name>.md  (detail version)

The live files live at the site root (`latest.md` / `latest-detail.md`) and use
relative links that assume that location:
  - the light file links to the detail file as `./latest-detail.md#<anchor>`
    (emitted by derive_light.py), and
  - both files link to the previous summary as
    `./archives/latest/<date>.md` / `./archives/latest-detail/<date>.md`.

When a file is archived it descends two levels (into `archives/latest/` or
`archives/latest-detail/`), so those `./...` paths break. This script performs
the move and rewrites the links to the archived depth:
  - light: `./latest-detail.md#`        -> `../latest-detail/<name>.md#`
  - both:  `./archives/latest/`         -> `../latest/`
  - both:  `./archives/latest-detail/`  -> `../latest-detail/`

Usage:
    # Archive the current pair (used by the SKILL, step 10):
    python archive_summary.py <light> <detail> <archives_dir> <name>

    # Repair links in already-archived files in place (one-off / migration):
    python archive_summary.py --fix-existing <archives_dir>

Exit codes: 0 on success, 1 on missing input, 2 on usage error.
"""
import os
import sys
import glob


def _rewrite_prev_links(text: str) -> str:
    """Rewrite previous-summary links from the live form to the archived form.

    `./archives/latest-detail/` must be handled before `./archives/latest/`
    is irrelevant here (the latter never matches inside the former because a
    `/` follows `latest`), but we keep a stable order regardless.
    """
    text = text.replace('./archives/latest-detail/', '../latest-detail/')
    text = text.replace('./archives/latest/', '../latest/')
    return text


def rewrite_light(text: str, name: str) -> str:
    """Links a light file needs once it lives in `archives/latest/<name>.md`."""
    text = text.replace('](./latest-detail.md#', f'](../latest-detail/{name}.md#')
    # defensive: a bare (no `./`) form, should derive_light ever emit it
    text = text.replace('](latest-detail.md#', f'](../latest-detail/{name}.md#')
    return _rewrite_prev_links(text)


def rewrite_detail(text: str, name: str) -> str:
    """Links a detail file needs once it lives in `archives/latest-detail/<name>.md`.

    The detail file's own section links are same-file anchors (`#anchor`), which
    survive the move untouched; only the previous-summary links need rewriting.
    """
    return _rewrite_prev_links(text)


def _read(path: str) -> str:
    with open(path, encoding='utf-8') as fh:
        return fh.read()


def _write(path: str, text: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8', newline='') as fh:
        fh.write(text)


def move(light: str, detail: str, archives_dir: str, name: str) -> int:
    if not os.path.isfile(light) or not os.path.isfile(detail):
        print(f'ERROR: light/detail not found: {light} / {detail}', file=sys.stderr)
        return 1
    dst_light = os.path.join(archives_dir, 'latest', f'{name}.md')
    dst_detail = os.path.join(archives_dir, 'latest-detail', f'{name}.md')
    _write(dst_light, rewrite_light(_read(light), name))
    _write(dst_detail, rewrite_detail(_read(detail), name))
    os.remove(light)
    os.remove(detail)
    print(f'Archived -> {dst_light}')
    print(f'Archived -> {dst_detail}')
    return 0


def fix_existing(archives_dir: str) -> int:
    n = 0
    for path in glob.glob(os.path.join(archives_dir, 'latest', '*.md')):
        name = os.path.splitext(os.path.basename(path))[0]
        s = _read(path)
        ns = rewrite_light(s, name)
        if ns != s:
            _write(path, ns)
            n += 1
    for path in glob.glob(os.path.join(archives_dir, 'latest-detail', '*.md')):
        name = os.path.splitext(os.path.basename(path))[0]
        s = _read(path)
        ns = rewrite_detail(s, name)
        if ns != s:
            _write(path, ns)
            n += 1
    print(f'fixed {n} files under {archives_dir}')
    return 0


def main() -> int:
    args = sys.argv[1:]
    if len(args) == 2 and args[0] == '--fix-existing':
        return fix_existing(args[1])
    if len(args) == 4:
        light, detail, archives_dir, name = args
        return move(light, detail, archives_dir, name)
    print('Usage:\n'
          '  python archive_summary.py <light> <detail> <archives_dir> <name>\n'
          '  python archive_summary.py --fix-existing <archives_dir>',
          file=sys.stderr)
    return 2


if __name__ == '__main__':
    sys.exit(main())
