# Reproducing the Task 01 observed metrics

All counts in this folder describe the supplied **SIMULATED / FICTIONAL** Task 01 workbook only. They are not actual VELOOP Rewards production metrics.

## Source and populations

- Source workbook: `VELoop_Rewards_Data_01 (1).xlsx` supplied for Task 01.
- Clean analytical population: `Users_1000_Clean` (1,000 rows, 27 columns).
- Messy QA population: `Users_Messy_Audit` (1,008 rows, 28 columns). This sheet is an audit fixture and must not be included in KPI denominators.
- The original workbook contains direct identifiers (e.g. name and email columns), so it is not copied into this public repository.

## Reproduce

1. Open the original supplied workbook.
2. Export `Users_1000_Clean` to `Users_1000_Clean.csv` and `Users_Messy_Audit` to `Users_Messy_Audit.csv` using UTF-8 CSV.
3. Place both CSVs in this folder or pass their paths to the script.
4. Run: `python reproduce_metrics.py Users_1000_Clean.csv Users_Messy_Audit.csv`.
5. Compare the output with `observed_metrics.csv`, `onboarding_by_acquisition_source.csv` and the `Observed Metrics` / `Onboarding by Source` sheets in `VELOOP_Task01_Reproducible_Analysis_v2.xlsx`.

The script uses only the Python standard library. It does not upload or transmit the input data.

## Calculation definitions

- Snapshot rate = count meeting the supplied categorical/flag condition / all clean user rows.
- Onboarding-by-source rate = Completed status / all clean rows for that acquisition source.
- Excess duplicate rows = messy audit row count - distinct non-null user IDs.
- Negative `days_since_registration` = count of numeric values below zero.

## Interpretation controls

- `is_active_7d` and `is_active_30d` are supplied snapshot flags, not event-derived DAU/MAU.
- Onboarding status is a point-in-time state; it does not expose step timing, drop-off or time-to-complete.
- Referral acquisition is a registration source, not referral activation/conversion.
- The messy audit sheet is only for QA and must not be used as the clean analytical base.
