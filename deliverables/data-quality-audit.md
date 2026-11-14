# Task 01 — Data Quality Audit Findings

**Scope:** Admin-approved Task 01 simulated workbook only. The clean user sheet is the analytical population; the messy sheet is a separate QA fixture and is excluded from KPI denominators.

## Clean user snapshot

| Check | Finding | Interpretation / action |
|---|---:|---|
| Rows | 1,000 | Clean analytical population |
| Unique non-null user IDs | 1,000 | Primary-key uniqueness passes |
| Null last-login values | 72 (7.2%) | Keep as unknown/no recorded login; do not impute without evidence |
| Negative days-since-registration | 4 (0.4%) | Validate as-of date, timezone and derivation logic |
| Email verified | 855 (85.5%) | Snapshot status only |
| Onboarding complete | 722 (72.2%) | Snapshot status, not time-based funnel conversion |

## Messy QA fixture

| Check | Finding | Interpretation / action |
|---|---:|---|
| Rows | 1,008 | Fixture only; do not use as KPI denominator |
| Unique non-null IDs | 1,000 | Eight excess duplicate rows across eight repeated IDs |
| Malformed/missing registration timestamps | 2 | Quarantine and correct upstream format/value; retain original for audit |
| Null required fields | 8 | Investigate requiredness and ingestion validation |

## Source documentation issue

The source workbook's Data_Dictionary sheet contains 25 documented entries, while the clean user table has 27 fields. `platform` and `country` appear in the source table but are absent from the source dictionary. This should be resolved by the dataset owner; the project-level dictionary documents both and flags the source-documentation gap.

## Control recommendations

- Enforce non-null, unique, immutable user IDs at ingestion.
- Validate timestamps, timezone conventions and plausible date boundaries.
- Validate categorical values against approved enumerations.
- Apply conditional validation to `referral_source_detail` only when acquisition source is Referral.
- Detect duplicate IDs and duplicate events using stable identifiers.
- Keep raw, quarantined and curated layers separate; preserve an audit trail for corrections.
- Apply role-based access and minimise exposure of `full_name` and `email`.
- Extend quality rules to task, reward, wallet, withdrawal, referral and feature-event domains only after those source datasets exist.

This audit does not claim to validate production data quality or prove the status of VELOOP's production controls.
