#!/usr/bin/env python3
"""Check that every relative link and #anchor resolves, and that every
handbook page is reachable in the reading order.

    python3 scripts/check_links.py
"""

import os
import re
import sys

from handbook_order import ROOT, read, reading_order

LINK = re.compile(r"\]\(([^)\s]+)\)")
SKIP_DIRS = {".git", "node_modules", "build"}


def markdown_files():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS)
        for name in sorted(filenames):
            if name.endswith(".md"):
                yield os.path.relpath(os.path.join(dirpath, name), ROOT)


def slugify(heading):
    """GitHub's heading anchor: lowercase, punctuation dropped, spaces to dashes."""
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", heading)
    text = re.sub(r"[^\w\- ]", "", text.strip().lower())
    return text.replace(" ", "-")


def anchors(page):
    found, seen, fenced = set(), {}, False
    for line in read(page).split("\n"):
        if line.startswith("```"):
            fenced = not fenced
        match = None if fenced else re.match(r"^#{1,6} (.+)$", line)
        if match:
            slug = slugify(match.group(1))
            count = seen.get(slug, 0)
            seen[slug] = count + 1
            found.add(slug if count == 0 else f"{slug}-{count}")
    return found


def main():
    errors = []
    for page in markdown_files():
        text = re.sub(r"```.*?```", "", read(page), flags=re.S)
        for number, line in enumerate(text.split("\n"), 1):
            for target in LINK.findall(line):
                if re.match(r"^[a-z]+:", target):
                    continue
                path, _, anchor = target.partition("#")
                dest = os.path.normpath(os.path.join(os.path.dirname(page), path)) if path else page
                if os.path.isdir(os.path.join(ROOT, dest)):
                    dest = os.path.join(dest, "README.md")
                if not os.path.exists(os.path.join(ROOT, dest)):
                    errors.append(f"{page}:{number}: missing file {target}")
                elif anchor and dest.endswith(".md") and anchor not in anchors(dest):
                    errors.append(f"{page}:{number}: missing anchor {target}")

    ordered = {p for p, _ in reading_order()}
    for page in markdown_files():
        if page.startswith("handbook/") and page not in ordered:
            errors.append(f"{page}: not listed in any README, so readers cannot reach it")

    for error in errors:
        print(error)
    print(f"{len(errors)} problem(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
