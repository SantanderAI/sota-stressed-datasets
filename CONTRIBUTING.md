# Contributing to Stressed SOTA Datasets

Thanks for your interest in this project. This repository is a **curated data
collection** maintained by Santander AI Lab. Because the datasets are *generated
artifacts* with a documented, reproducible methodology, the contribution model
is intentionally narrow.

## What we welcome

- **Issue reports** about data quality: malformed records, broken files,
  incorrect attribution, license questions, or a record that raises a privacy
  concern (for privacy, follow [`SECURITY.md`](.github/SECURITY.md) instead of a
  public issue).
- **Documentation fixes**: typos and clarifications in any `README.md`,
  `codebook.md`, or `CHANGELOG.md`.
- **New-dataset proposals**: suggestions for a benchmark dataset that would be a
  good candidate to republish in stressed form (open a *New dataset proposal*
  issue).

## What we generally do not accept

- **Direct edits to data files** (`datasets/*/data/*`). The datasets are
  regenerated from a fixed seed and documented parameters; they are not
  hand-edited. If you spot a data problem, open an issue so we can fix it at the
  source and regenerate.

We are a small team and **do not guarantee** that external feature pull requests
will be merged. When in doubt, **open an issue first** so we can align before
you invest time.

## How to open an issue

1. Search existing issues to avoid duplicates.
2. Use the appropriate template (data issue / documentation / new dataset).
3. Include the dataset name and, for data issues, the affected record `id`s.

## How to submit a pull request

1. Open or reference an issue describing the change.
2. Fork the repo and create a topic branch.
3. Keep the PR focused — one logical change.
4. Fill in the pull request template.
5. The **CLA Assistant** bot will ask you to sign the Contributor License
   Agreement on your first PR; this is required before we can merge.

## License of contributions

By contributing, you agree that your contributions are licensed under the same
license as the relevant dataset (by default **CC BY 4.0**; see [`LICENSE`](LICENSE)
and the per-dataset `LICENSE`). You confirm you have the right to contribute the
material and that it does not contain confidential, proprietary, or personal
data.

## Attribution

Every dataset here is derived from a public source dataset and must credit
**both** the original source **and** Santander AI Lab. Do not remove or weaken
existing attribution.
