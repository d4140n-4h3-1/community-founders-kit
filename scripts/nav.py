#!/usr/bin/env python3
"""Add or refresh the Previous / Next footer on every page in reading order.

    python3 scripts/nav.py          rewrite the footers
    python3 scripts/nav.py --check  fail if any footer is missing or stale
"""

import os
import re
import sys

from handbook_order import NAV_MARKER, ROOT, read, reading_order, strip_nav, title


def short_title(page):
    # Drop a trailing note such as "*(monthly)*" to keep the footer short.
    return re.sub(r"\s*\*\([^)]*\)\*$", "", title(page))


def link(page, target):
    rel = os.path.relpath(target, os.path.dirname(page) or ".")
    return f"[{short_title(target)}]({rel})"


def footer(page, prev, nxt):
    parts = []
    if prev:
        parts.append(f"← **Previous:** {link(page, prev)}")
    if nxt:
        parts.append(f"**Next:** {link(page, nxt)} →")
    return f"\n{NAV_MARKER}\n\n---\n\n{' · '.join(parts)}\n"


def main():
    check = "--check" in sys.argv
    pages = [p for p, _ in reading_order()]
    stale = []
    for i, page in enumerate(pages):
        prev = pages[i - 1] if i > 0 else None
        nxt = pages[i + 1] if i + 1 < len(pages) else None
        old = read(page)
        new = strip_nav(old) + footer(page, prev, nxt)
        if new != old:
            stale.append(page)
            if not check:
                with open(os.path.join(ROOT, page), "w", encoding="utf-8") as f:
                    f.write(new)
    if check and stale:
        print("Previous / Next footers are out of date. Run: python3 scripts/nav.py")
        for page in stale:
            print(f"  {page}")
        return 1
    print(f"{len(pages)} pages, {len(stale)} {'stale' if check else 'updated'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
