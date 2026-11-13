# Product Data Readiness Audit — Task 01

## Scope

This audit assesses evidence supplied for the Task 01 exercise only. It does not make claims about the completeness or implementation state of VELOOP's actual production systems.

## Observed source coverage

| Product area | Evidence in supplied Task 01 material | Readiness interpretation |
|---|---|---|
| User/account | Clean and messy user snapshots, source data dictionary | Baseline snapshot profiling possible; lifecycle/event history is limited |
| Acquisition/onboarding | Acquisition-source labels and onboarding status | Cross-sectional status breakdown possible; ordered funnel timing unavailable |
| Engagement | Active 7d/30d flags in user snapshot | Snapshot flags available; event-derived sessions/DAU/retention unavailable |
| Tasks/earning | Product concepts and proposed event/design schedules | Requires authoritative task definitions and attempts |
| Rewards | Proposed lifecycle and metric schedule | Requires reward decision and posting history |
| Wallet | Proposed transaction model and checks | Requires immutable ledger data and unit/transaction history |
| Withdrawals | Proposed request/attempt/settlement lifecycle | Requires provider attempt and settlement records |
| Referrals | Acquisition-source label; proposed milestone design | Source attribution snapshot only; referral qualification and reward conversion unavailable |
| Feature usage/support | Product concepts and proposed events | Requires event/ticket-level source data |

## Key data quality observations

- Clean sheet: 1,000 rows; 1,000 unique non-null IDs.
- Email verified: 855/1,000 (85.5%).
- Onboarding completed: 722/1,000 (72.2%).
- Active 7d flag: 78/1,000 (7.8%); Active 30d flag: 325/1,000 (32.5%).
- Null last-login values: 72/1,000.
- Negative days-since-registration: 4/1,000, requiring as-of-date/timezone review.
- Messy fixture: 1,008 rows, 1,000 unique IDs and 8 excess duplicate rows; use for QA only.
- `platform` and `country` appear in the clean source but are absent from the supplied data dictionary; dictionary alignment is a governance task.

## Readiness conclusion

The exercise data is adequate for demonstrative user snapshot profiling and proposed analytical design. It is not sufficient to certify transactional/reward/withdrawal outcomes or temporal engagement metrics. Each such domain requires a source owner, stable grain and key, event timestamps, state transitions, idempotency/deduplication, unit handling and a reconciliation rule.

## Required next actions

1. Confirm authoritative systems and lifecycle states with product and engineering.
2. Reconcile supplied fields against the canonical data dictionary and add missing field definitions.
3. Approve event contracts and state-transition definitions.
4. Obtain and validate timestamped source events and ledger/settlement records through authorised VELOOP channels.
5. Publish dashboards only after reconciliation, privacy and access gates pass.
