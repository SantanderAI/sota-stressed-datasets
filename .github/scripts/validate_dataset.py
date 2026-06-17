# Copyright (c) 2026 Santander Group
# SPDX-License-Identifier: Apache-2.0
"""Integrity validator for the Stressed SOTA Datasets collection.

This is CI tooling (not part of the published data). It walks every dataset
under ``datasets/<name>/data/*.jsonl`` and asserts basic structural invariants:

* each line is a valid JSON object,
* required top-level keys are present,
* ``label`` is 0 or 1,
* record ``id`` values are unique within a file,
* if a ``*_metadata.json`` sibling declares ``total_samples`` / a label
  distribution, the data matches it (within tolerance).

Pure standard library; no third-party dependencies. Exit code 0 = OK.
"""
from __future__ import annotations

import glob
import json
import os
import sys

REQUIRED_KEYS = ("id", "version", "label", "metadata", "value")
DISTRIBUTION_TOLERANCE = 0.05  # 5 percentage points


def _load_metadata(jsonl_path: str) -> dict:
    base = jsonl_path[: -len(".jsonl")]
    meta_path = f"{base}_metadata.json"
    if os.path.isfile(meta_path):
        with open(meta_path, encoding="utf-8") as fh:
            return json.load(fh)
    return {}


def validate_file(path: str) -> list[str]:
    errors: list[str] = []
    ids: set[str] = set()
    labels: list[int] = []

    with open(path, encoding="utf-8") as fh:
        for lineno, raw in enumerate(fh, start=1):
            raw = raw.strip()
            if not raw:
                continue
            try:
                rec = json.loads(raw)
            except json.JSONDecodeError as exc:
                errors.append(f"{path}:{lineno}: invalid JSON ({exc})")
                continue
            if not isinstance(rec, dict):
                errors.append(f"{path}:{lineno}: line is not a JSON object")
                continue
            for key in REQUIRED_KEYS:
                if key not in rec:
                    errors.append(f"{path}:{lineno}: missing key '{key}'")
            label = rec.get("label")
            if label not in (0, 1):
                errors.append(f"{path}:{lineno}: label must be 0 or 1, got {label!r}")
            else:
                labels.append(label)
            rid = rec.get("id")
            if rid is not None:
                if rid in ids:
                    errors.append(f"{path}:{lineno}: duplicate id '{rid}'")
                ids.add(rid)

    meta = _load_metadata(path)
    total = meta.get("total_samples")
    if total is not None and len(labels) != total:
        errors.append(
            f"{path}: record count {len(labels)} != metadata total_samples {total}"
        )

    # Optional distribution check, e.g. "70/30" meaning 70% label==1.
    dist = meta.get("label_distribution")
    if dist and "/" in str(dist) and labels:
        try:
            good_pct = int(str(dist).split("/")[0]) / 100.0
        except ValueError:
            good_pct = None
        if good_pct is not None:
            actual = sum(1 for x in labels if x == 1) / len(labels)
            if abs(actual - good_pct) > DISTRIBUTION_TOLERANCE:
                errors.append(
                    f"{path}: label==1 ratio {actual:.3f} differs from declared "
                    f"{good_pct:.3f} by more than {DISTRIBUTION_TOLERANCE}"
                )

    return errors


def main() -> int:
    paths = sorted(glob.glob("datasets/*/data/*.jsonl"))
    if not paths:
        print("FAIL: no dataset files found under datasets/*/data/*.jsonl")
        return 1

    all_errors: list[str] = []
    for path in paths:
        errs = validate_file(path)
        if errs:
            all_errors.extend(errs)
        else:
            print(f"OK: {path}")

    if all_errors:
        print("\nValidation failed:")
        for err in all_errors:
            print(f"  - {err}")
        return 1

    print(f"\nOK: validated {len(paths)} dataset file(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
