# Data Integrity and Evidence Policy

## Evidence labels
- **Source-observed:** directly present in the approved Task 01 workbook or an official public page.
- **Calculated:** reproducible aggregate derived from the approved Task 01 workbook; it inherits that workbook's simulated/fictional status.
- **Proposed:** recommended KPI, event, schema, rule, architecture, dashboard or control not proven to exist in production.
- **To Be Verified:** detail requiring confirmation from the accountable VELOOP owner or technical source.

## Non-negotiable scope
Only the Admin-approved Task 01 dataset is used for observed profiling. The Users_Messy_Audit sheet is a QA fixture, not an analytical population. Do not join unrelated simulated workbooks or invent missing operational events, wallet/reward transactions or referral records.

## Privacy boundary
The original Task 01 source workbook contains row-level identifiers and is excluded from public hosting and the public-safe review archive. A redacted/public-safe audit workbook and aggregate outputs are included. Use the authorised assignment copy for local reproduction.

## KPI interpretation
Supplied active_7d and active_30d flags are snapshot flags, not event-derived DAU/MAU or retention. Referral acquisition does not equal referral conversion. Snapshot onboarding status does not provide step-level funnel timestamps. Four negative days_since_registration observations require as-of/timezone validation.

## Product-source boundary
Official VELOOP public pages substantiate published descriptions and policy statements only. They do not verify production capability, provider availability, data capture, backend state transitions, analytics implementation, SLAs or live performance. Future Features previews must not be modelled as current features until approved for launch.

## Release and approval
All proposed analytics specifications require Product, Engineering, Finance, Operations and Privacy/Legal review. The initial evaluator result was 65% and not approved. This package does not claim VELOOP acceptance.
