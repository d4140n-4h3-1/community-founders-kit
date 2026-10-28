[Handbook](README.md) ›

# Contributing

This handbook gets better when groups who use it report what worked and what didn't. Anyone may propose a change. The text is public domain ([CC0](LICENSE)), so by contributing you agree that your contribution is too.

## Ways to Help

- **Report a problem:** open an issue for anything wrong, unclear, unsafe, or out of date. Say which page, what is wrong, and what you suggest.
- **Share a lesson:** if your community found a trigger too easy or too strict, or a rule that failed in practice, open an issue with the entry from your [revision log](REVISION_LOG.md).
- **Propose an edit:** open a pull request. Small, focused changes are easiest to review.

## Writing Style

- **Plain words, short sentences.** Write for a tired person reading a printout by a lantern.
- **Rules first, reasons after.** Lead with the rule in bold, then explain it.
- **Checklists over paragraphs** wherever a reader has to do something.
- **Name the tier** for anything that depends on scale ("Tier 2 and up").
- **No legal, tax, medical, or structural advice for one place.** Say what to check and who to ask.
- **Neutral and equal.** Nothing that favors or targets any belief, group, or person.
- **Both units** for measurements people will build to (feet and meters, mph and m/s).
- Use American spelling and the serial comma, to match the existing text.

## Keeping the Tier Rules in Agreement

A rule that depends on a tier usually appears in several places. When you change one, change them all in the same pull request:

1. The chapter that explains the rule
2. The standing rules and the adoption table in [Chapter 3](handbook/part-1-core-chapters/03-charter-and-decision-making.md)
3. The [tier summary](handbook/part-4-tiers/tier-summaries/README.md) for that tier
4. The [unlock trigger](handbook/part-4-tiers/unlock-triggers/README.md) that checks it
5. [Start Here](START_HERE.md), if it affects a Tier 0 group
6. Any checklist, template, or log in the appendices that uses it
7. The [glossary](handbook/appendices/appendix-f-glossary.md), if you add a new term

Add a line to the [changelog](CHANGELOG.md) under **Unreleased**.

## Releases

When a set of changes is ready for groups to use, a maintainer renames **Unreleased** in the [changelog](CHANGELOG.md) to the date of the edition, with a one-line summary, starts a new empty **Unreleased** section, and tags the commit with the same date (for example, `git tag -a 2026-10-28`). Groups record the edition they adopted in their [revision log](REVISION_LOG.md), so they can report problems against it.

## File Layout

- Each page starts with a breadcrumb line linking up to its parents, and ends with an automatic Previous / Next footer. Do not edit the footer by hand.
- Each folder has a `README.md` listing its sections. Add new pages there, and to the contents in the main [README](README.md).
- Use relative links, and link to the exact page rather than a whole chapter where you can.

## Checks

Every pull request runs these checks once the [workflows](ci/README.md) are turned on. Run them yourself before you open one (you need Python 3, and Node.js for the formatting check):

```sh
python3 scripts/nav.py          # rebuild the Previous / Next footers
python3 scripts/check_links.py  # every relative link and #anchor resolves
npx markdownlint-cli2           # consistent Markdown formatting
```

To build the printable PDFs (needs [pandoc](https://pandoc.org) and Chrome or Chromium):

```sh
scripts/build_pdf.sh            # writes the whole handbook and the Start Here packet to build/
```
