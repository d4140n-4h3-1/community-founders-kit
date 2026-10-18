[Handbook](../README.md) ›

# Automatic Checks

These two GitHub Actions workflows run the handbook's checks and build its PDFs. They are kept here because they could not be added to `.github/workflows/` automatically. To turn them on, a maintainer moves them there once:

```sh
mkdir -p .github/workflows
git mv ci/checks.yml ci/pdf.yml .github/workflows/
git commit -m "Turn on the handbook checks and PDF build"
git push
```

- **checks.yml** runs on every push and pull request: links and anchors, the Previous / Next footers, and Markdown formatting.
- **pdf.yml** builds the whole handbook and the Start Here packet as PDFs on every push to `main` and on demand, and attaches them to each published release.
