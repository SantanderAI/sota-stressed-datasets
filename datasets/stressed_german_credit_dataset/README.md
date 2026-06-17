# Stressed German Credit Dataset (SGCD)

A stressed variant of the classic **German Credit** dataset: the same underlying credit
records, republished with controlled, documented **input degradation** ("shocks") applied
to a subset of the examples.

- **Version:** `SGCD-v0.1`
- **Records:** 1,000 (one JSON object per line)
- **Author:** Santander AI Lab

## Mother (source) dataset

Derived from the **Statlog (German Credit Data)** dataset from the UCI Machine Learning
Repository:

- **Where to find it:** https://archive.ics.uci.edu/dataset/144/statlog+german+credit+data

The original 20 attributes and the binary credit-risk label are preserved; SGCD only adds
controlled perturbations to the *observed* inputs — the underlying record is never changed.

## At a glance

- **1,000 records**, each with the original **20 attributes** (7 numeric, 13 categorical).
- **Label** (`label`): `1` = Good (low risk), `0` = Bad (high risk). Distribution ~70/30.
- Records are organized into **20 ordered batches of 50** examples each (fixed 35 Good /
  15 Bad per batch).
- A documented fraction of records carry exactly one **semantic shock** (plus optional
  cosmetic noise); the rest are clean.

## Files

| File | Description |
|------|-------------|
| `data/SGCDataset.jsonl` | The dataset — one JSON object per line. |
| `data/SGCDataset_metadata.json` | Generation parameters (seed, ratios, shock settings, structure). |
| `data/codebook.md` | Attribute code → human-readable label mapping. |
| `data/SGCDataset_report.html` | Self-contained report (description, charts, validation, sample browser). |

## Record schema

Each line of `data/SGCDataset.jsonl` is a JSON object:

| Field | Description |
|-------|-------------|
| `id` | Stable record identifier, e.g. `SGCD-0000`. |
| `version` | Dataset version (`SGCD-v0.1`). |
| `label` | `0` = Bad / high risk, `1` = Good / low risk. |
| `metadata.batch` | Batch identifier within the ordered sequence (`S1`–`S4`, `A1`–`A10`, `T1`–`T6`). |
| `metadata.stage` | `setup`, `adaptation`, or `test`. |
| `metadata.shock_semantic` | Semantic shock applied (`F0`–`F4`; `F0` = none). |
| `metadata.shock_cosmetic` | Whether surface/formatting noise was applied. |
| `metadata.shock_field` | The field affected by the semantic shock (if any). |
| `value.json_view` | Structured record (raw attribute codes + numeric values). |
| `value.text_view` | Natural-language rendering of the same record. |

Attribute codes (e.g. `A11`) are decoded in [`data/codebook.md`](data/codebook.md).

## Stresses / shocks applied

| Code | Name | What it does |
|------|------|--------------|
| `F0` | Clean | Faithful, unmodified record. |
| `F1` | Missingness | One field is dropped (`null` in the structured view, omitted from text). |
| `F2` | Ambiguity | A precise value is replaced with vague/coded wording in the text (structured view intact). |
| `F3` | Cosmetic | Surface formatting noise (reordering, delimiters, raw codes). |
| `F4` | Contradiction | The text states a different but domain-valid value than the structured view. |

In addition, light **numeric noise** is applied to `duration` and `credit_amount` in a
small fraction of records, producing vague phrasings such as *"roughly 13 months"* or
*"around 12 months"*. At most one semantic shock is applied per record, and shocks are
applied independently of the label.

The batches are ordered: early batches are clean, later batches carry an increasing rate
of perturbation, and the final batches include both previously seen shock types
(`F1`, `F2`) and a held-out type (`F4`).

## License & citation

- **License:** released under the same license as the source dataset — **Creative Commons
  Attribution 4.0 International (CC BY 4.0)**. See [`LICENSE`](LICENSE).
- **Citation:** see [`CITATION.cff`](CITATION.cff). Author: **Santander AI Lab**.

## Limitations & ethics

This dataset inherits the well-known limitations and biases of the original German Credit
data, including sensitive attributes such as `personal_status_sex`, `foreign_worker`, and
`age`. It is provided for **research and benchmarking only** and must **not** be used for
real-world credit scoring or any production decision-making about individuals.
