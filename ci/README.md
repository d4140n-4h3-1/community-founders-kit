[Handbook](../README.md) ›

# Automatic Checks

This GitHub Actions workflow runs the handbook's checks. It is kept here because it could not be added to `.github/workflows/` automatically. To turn it on, a maintainer moves it there once:

```sh
mkdir -p .github/workflows
git mv ci/checks.yml .github/workflows/
git commit -m "Turn on the handbook checks"
git push
```

- **checks.yml** runs on every push and pull request: links and anchors, the Previous / Next footers, and Markdown formatting.
