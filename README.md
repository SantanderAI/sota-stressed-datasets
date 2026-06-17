# Stressed SOTA Datasets

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-blue.svg)](https://creativecommons.org/licenses/by/4.0/)

**Open source by Santander AI Lab.** A benchmark **dataset** collection for evaluating the
robustness of **machine learning** and **LLM** systems: well-known datasets republished in
**stressed** form — controlled, documented input degradation ("shocks": noise, missingness,
ambiguity, formatting changes, contradictions) applied to a subset of the records. We publish
the stressed versions so the community can freely reuse them.

Part of [Santander AI open source](https://github.com/SantanderAI) · [santander.com](https://www.santander.com).

This is an **evolving collection**; more stressed datasets will be added over time. For
now it contains the first one.

## Datasets

| Dataset | Source (mother dataset) | Version | Status | Link |
|---------|-------------------------|---------|--------|------|
| Stressed German Credit Dataset | UCI German Credit | SGCD-v0.1 | Released | [`datasets/stressed_german_credit_dataset/`](datasets/stressed_german_credit_dataset/) |

## Layout

Each dataset is self-contained under `datasets/<dataset_name>/`, with its own `README.md`,
`CHANGELOG.md`, `CITATION.cff`, `LICENSE`, and a `data/` folder holding the data and
metadata. The shocks/stresses applied are specific to each dataset and documented inside
its own folder.

## Usage, license & citation

- The community is **free to use** these datasets under each dataset's stated license.
- Each dataset uses the **same license as its mother (source) dataset** (default for this
  collection: **CC BY 4.0**), and the citation author is always **Santander AI Lab** (see
  each dataset's `CITATION.cff` and the collection-level [`CITATION.cff`](CITATION.cff)).
- Always attribute **both** the original source dataset **and** Santander AI Lab.

To cite the collection, see [`CITATION.cff`](CITATION.cff); to cite an individual dataset,
use the `CITATION.cff` inside its folder.

## Contributing & security

This collection is **curated by Santander AI Lab**; data files are regenerated from a
documented method, not hand-edited. We welcome **issue reports** (data problems,
attribution, documentation) and **new-dataset proposals** — see
[`CONTRIBUTING.md`](CONTRIBUTING.md). For a **privacy concern** about any record, follow
[`SECURITY.md`](.github/SECURITY.md) (report privately — do not open a public issue).

Please also read our [Code of Conduct](CODE_OF_CONDUCT.md).
