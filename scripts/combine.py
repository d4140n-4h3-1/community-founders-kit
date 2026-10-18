#!/usr/bin/env python3
"""Join the handbook pages, in reading order, into one Markdown file for print.

    python3 scripts/combine.py OUT.md                      the whole handbook
    python3 scripts/combine.py OUT.md --packet START_HERE.md
        one page plus every page it links to, in reading order

Breadcrumbs, footers, and folder link lists are dropped, headings are nested
by depth, and links between pages become links within the document. Chapters
and printable forms get the "page" class, so each starts on a new sheet.
"""

import os
import re
import sys

from check_links import slugify
from handbook_order import read, reading_order, resolve, strip_nav

LINK = re.compile(r"(!?)\[([^\]]*)\]\(([^)\s]+)\)")
EXTRA_PAGES = ["REVISION_LOG.md"]


def page_id(page):
    return "p-" + re.sub(r"[^a-z0-9]+", "-", page.lower().removesuffix(".md")).strip("-")


def body(page):
    lines = strip_nav(read(page)).split("\n")
    if lines and lines[0].rstrip().endswith("›"):
        lines = lines[1:]
    out, skipping = [], False
    for line in lines:
        if line.startswith("## "):
            skipping = os.path.basename(page) == "README.md" and line[3:].strip() in ("Contents", "Sections")
        if not skipping:
            out.append(line)
    return out


def convert(page, level, included):
    out, seen, fenced = [], {}, False
    for line in body(page):
        if line.startswith("```"):
            fenced = not fenced
        match = None if fenced else re.match(r"^(#{1,6}) (.+)$", line)
        if match:
            depth = len(match.group(1))
            if depth == 1:
                anchor = page_id(page)
                if level <= 2 or not page.startswith("handbook/part-"):
                    anchor += " .page"
            else:
                slug = slugify(match.group(2))
                count = seen.get(slug, 0)
                seen[slug] = count + 1
                anchor = f"{page_id(page)}--{slug if count == 0 else f'{slug}-{count}'}"
            line = f"{'#' * min(6, depth + level - 1)} {match.group(2)} {{#{anchor}}}"
        elif not fenced:
            line = LINK.sub(lambda m: relink(page, m, included), line)
        out.append(line)
    return "\n".join(out).strip("\n")


def relink(page, match, included):
    image, text, target = match.groups()
    if image or re.match(r"^[a-z]+:", target):
        return match.group(0)
    path, _, anchor = target.partition("#")
    dest = resolve(page, path) if path else page
    if os.path.isdir(dest):
        dest = os.path.join(dest, "README.md")
    if dest not in included:
        return text
    if anchor:
        return f"[{text}](#{page_id(dest)}--{anchor})"
    return f"[{text}](#{page_id(dest)})"


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    out_path = sys.argv[1]
    pages = [(p, d) for p, d in reading_order() if p != "README.md"]
    pages += [(p, 0) for p in EXTRA_PAGES]
    if "--packet" in sys.argv:
        start = sys.argv[sys.argv.index("--packet") + 1]
        linked = {start}
        for _, _, target in LINK.findall(read(start)):
            path = target.partition("#")[0]
            if path and not re.match(r"^[a-z]+:", path):
                linked.add(resolve(start, path))
        pages = [(p, 0 if p == start else 2) for p, _ in pages if p in linked]
    included = {p for p, _ in pages}
    parts = [convert(p, max(1, d), included) for p, d in pages]
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n\n".join(parts) + "\n")
    print(f"{out_path}: {len(pages)} pages")
    return 0


if __name__ == "__main__":
    sys.exit(main())
