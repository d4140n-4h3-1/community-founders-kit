#!/usr/bin/env bash
# Build printable PDFs of the handbook into build/.
#
#   scripts/build_pdf.sh
#
# Needs python3, pandoc, and Chrome or Chromium (set CHROME to its path if it
# is not on PATH). Writes:
#   build/community-founders-kit.pdf   the whole handbook
#   build/start-here-packet.pdf        Start Here plus every page it links to
set -euo pipefail

cd "$(dirname "$0")/.."
mkdir -p build

if [[ -z "${CHROME:-}" ]]; then
  for candidate in google-chrome chromium chromium-browser /opt/pw-browsers/chromium; do
    if command -v "$candidate" >/dev/null 2>&1; then CHROME="$candidate"; break; fi
  done
fi
if [[ -z "${CHROME:-}" ]]; then
  echo "Chrome or Chromium not found. Set CHROME to its path." >&2
  exit 1
fi

build() {
  local name="$1" title="$2"; shift 2
  python3 scripts/combine.py "build/$name.md" "$@"
  pandoc "build/$name.md" -f commonmark_x -t html5 \
    --standalone --embed-resources --toc --toc-depth=2 \
    --css scripts/print.css \
    --metadata title="$title" \
    --metadata date="$(date +%Y-%m-%d)" \
    -o "build/$name.html"
  "$CHROME" --headless --no-sandbox --disable-gpu --no-pdf-header-footer \
    --print-to-pdf="build/$name.pdf" "file://$PWD/build/$name.html" 2>/dev/null
  echo "build/$name.pdf"
}

build community-founders-kit "Community Founders Kit"
build start-here-packet "Community Founders Kit: Start Here Packet" --packet START_HERE.md
