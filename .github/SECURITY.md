# Security Policy

## Reporting a concern

This repository publishes **data only** (no executable code). The most likely
"security" concerns here are **data-integrity** or **privacy** issues — for
example, a record that looks like it could identify a real person, a corrupted
or malformed data file, or a licensing/attribution problem.

**Do not open a public GitHub issue for a privacy concern.** Instead:

1. **Email**: send a detailed report to **opensource@gruposantander.com**
2. **GitHub Security Advisories**: alternatively, use [GitHub Security Advisories](../../security/advisories/new) to report privately.

### What to include

- Which dataset and which record(s) are affected (e.g. `id: SGCD-0123`).
- A description of the concern (privacy, integrity, license, attribution).
- Why you believe it is a problem and any supporting context.

### Response SLA

| Stage | SLA |
|:---|:---|
| Acknowledgment of report | < 48 hours |
| Initial assessment | < 7 days |
| Remediation for privacy/integrity issues | < 30 days |

## Privacy & data provenance

All datasets in this collection are **derived from publicly available, already
de-identified source datasets** (e.g. the UCI Machine Learning Repository). The
records do **not** contain Santander customer data, internal data, or newly
collected personal data. The "stresses" applied are controlled, documented
perturbations of the *observed inputs* — the underlying source record is never
altered.

If you believe any published record could nonetheless identify a real
individual, report it privately using the channels above and we will
investigate and, if needed, withdraw the affected records.

## Scope

This policy covers **only** the data and documentation in this repository. It
does not cover Santander's internal infrastructure, other Santander products,
or the original upstream source datasets (report those to their respective
maintainers).

## Best practices for contributors

- Never commit secrets, API keys, tokens, or credentials.
- Never commit internal URLs, IP addresses, or corporate email addresses.
- Never add records derived from non-public or personally identifiable data.

## Disclosure policy

We follow a coordinated disclosure process and ask that you give us reasonable
time to remediate before any public disclosure.
