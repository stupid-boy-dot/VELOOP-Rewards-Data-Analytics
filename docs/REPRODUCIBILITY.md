# Reproducibility and Analytical Evidence

## Scope and population

The supplied Task 01 workbook labels its records **SIMULATED / FICTIONAL / FOR ANALYTICAL WORK ONLY** and covers a snapshot dated 01 April–15 September 2026. The clean analytical base is `Users_1000_Clean` (1,000 rows, 27 fields). `Users_Messy_Audit` (1,008 rows, 28 fields) is a separate quality-testing fixture and must not be mixed into KPI denominators.

## Reproduced snapshot metrics

| Measure | Numerator | Denominator | Result | Formula / meaning |
|---|---:|---:|---:|---|
| Clean rows | 1,000 | 1,000 | 100.0% | Row count |
| Unique non-null user IDs | 1,000 | 1,000 | 100.0% | Distinct non-null IDs / clean rows |
| Email verified | 855 | 1,000 | 85.5% | Verified / clean rows |
| Onboarding completed | 722 | 1,000 | 72.2% | Completed / clean rows |
| Active 7-day flag | 78 | 1,000 | 7.8% | Yes / clean rows |
| Active 30-day flag | 325 | 1,000 | 32.5% | Yes / clean rows |
| Referral acquisition share | 119 | 1,000 | 11.9% | Referral source / clean rows |
| Consent accepted | 923 | 1,000 | 92.3% | Accepted / clean rows |
| Marketing opt-in | 442 | 1,000 | 44.2% | Yes / clean rows |
| Null last-login values | 72 | 1,000 | 7.2% | Blank last-login / clean rows |
| Negative days-since-registration | 4 | 1,000 | 0.4% | Values below zero |

## Onboarding by acquisition source

| Source | Users | Completed | Completion rate |
|---|---:|---:|---:|
| Direct | 217 | 159 | 73.3% |
| Organic Search | 244 | 180 | 73.8% |
| Other | 102 | 78 | 76.5% |
| Referral | 119 | 87 | 73.1% |
| Social Media | 160 | 114 | 71.3% |
| Telegram | 55 | 40 | 72.7% |
| WhatsApp | 103 | 64 | 62.1% |

These are cross-sectional status ratios, not a step-level funnel or time-to-complete measure.

## Messy QA fixture

The messy sheet has 1,008 rows, 1,000 unique non-null IDs, 8 excess duplicate rows across 8 repeated IDs. It is a quality-testing fixture only.

## Reproduce locally

1. Use the original Admin-designated Task 01 workbook supplied with the assignment. It is not mirrored publicly because it contains row-level identifiers.
2. Export `Users_1000_Clean` and `Users_Messy_Audit` to UTF-8 CSV, preserving original headers.
3. Run: `python analysis/reproduce_metrics.py Users_1000_Clean.csv Users_Messy_Audit.csv`.
4. The script prints metrics and writes `reproduced_metrics.json` in the working directory.
5. Compare with `analysis/observed_metrics.csv`, `analysis/onboarding_by_acquisition_source.csv` and `analysis/messy_audit_quality_counts.csv`.

Only Python standard-library modules are required. The script does not transmit input data.

## Interpretation constraints

- Snapshot activity flags are not event-derived DAU/WAU/MAU or retention.
- Referral acquisition is channel attribution, not successful referral conversion.
- A state snapshot is not a timestamped journey or funnel.
- Negative derived day counts require as-of-date/timezone review.
- Missing last-login values do not prove inactivity.
- The audit fixture is never a business KPI base.
