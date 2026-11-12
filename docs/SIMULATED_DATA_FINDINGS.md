# Simulated Data Findings

> **Important:** All figures below describe the fictional/simulated Task 01 dataset. They are not actual VELOOP production statistics.

## Clean user snapshot

- 1,000 rows and 27 columns
- 1,000 unique, non-null user identifiers
- 855 verified email records (85.5%)
- 722 completed onboarding records (72.2%)
- 78 users flagged active in the last 7 days (7.8%)
- 325 users flagged active in the last 30 days (32.5%)
- 72 missing last-login timestamps
- 4 negative values in the days-since-registration field, requiring review of the derivation/as-of boundary

## Messy user audit fixture

- 1,008 rows and 28 columns
- 1,000 unique user IDs, with 8 excess duplicate rows across 8 duplicated IDs
- 2 invalid or missing registration timestamps
- 8 required-field nulls across the identified required fields
- Referral-source detail is conditionally required for referral acquisition; nulls for non-referral acquisition are expected structurally

## Source coverage limitations

The supplied user snapshot supports descriptive analysis of user/account attributes and status flags. It does not provide a production transaction history or complete timestamped event stream. Therefore, actual daily activity trends, retention cohorts, earning conversion, wallet movements, payout outcomes and withdrawal success rates cannot be derived from the user snapshot alone.

## Interpretation rule

All percentages and counts above are sample metrics from the simulated assignment workbook. They must not be used as evidence of actual VELOOP business performance.
