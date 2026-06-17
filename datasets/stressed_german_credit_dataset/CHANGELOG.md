# Changelog — Stressed German Credit Dataset

All notable changes to this dataset are documented here. Versions are dataset-scoped.

## SGCD-v0.1 — 2026-06-12

- Initial public release.
- 1,000 records derived from the UCI German Credit (Statlog) dataset.
- 20 ordered batches of 50 (fixed 35 Good / 15 Bad per batch).
- Shock catalogue: `F0` (clean), `F1` (missingness), `F2` (ambiguity), `F3` (cosmetic),
  `F4` (contradiction); plus light numeric noise on `duration` and `credit_amount`.
- Includes `SGCDataset.jsonl`, `SGCDataset_metadata.json`, `codebook.md`, and a
  self-contained `SGCDataset_report.html`.
