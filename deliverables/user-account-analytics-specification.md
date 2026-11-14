# VELOOP Rewards — Task 01 User & Account Analytics Specification

**Prepared:** 10 November 2026  
**Source scope:** Admin-designated Task 01 workbook only

## 1. Scope and analytical basis

This specification is based exclusively on the approved Task 01 workbook. `Users_1000_Clean` is the 1,000-row analytical population; `Users_Messy_Audit` is a separate quality-audit fixture and is not included in KPI denominators.

The source README identifies all records as simulated/fictional, not actual VELOOP users or production records. All metrics below describe only the supplied simulated sample.

## 2. Identity and event identifiers

| Identifier | Source status | Specification |
|---|---|---|
| `user_id` | Present; unique in clean sheet | Stable user-level key within this Task 01 dataset |
| `event_id` | Not supplied | Propose a unique immutable identifier for each registration, login, onboarding and account-state event |
| `session_id` | Not supplied | Propose a session identifier to group ordered events; define session start/end and timeout rules before production use |
| `transaction_id` | Not supplied in this workbook | Do not fabricate transactions; include only when relevant transaction data exists in an approved source |

## 3. User/account field specification

The companion Excel Field Specification sheet maps all 27 fields from `Users_1000_Clean` to type, requiredness, purpose, source, validation and evidence status. Two fields—`platform` and `country`—exist in the source but are absent from its supplied `Data_Dictionary`; their definitions should be added to the source dictionary.

## 4. Lifecycle coverage

- **Registration:** `registration_datetime`, `acquisition_source`, `account_created_via` and device/platform support snapshot registration counts and source mix.
- **Login:** `last_login_datetime` and `lifetime_sessions` support latest-login and cumulative-count analysis only; login event history is absent.
- **Onboarding:** `onboarding_status` supports current-state counts; start/completion timestamps and milestone history are absent.
- **Account lifecycle:** `account_status` supports current-state distribution; status-transition history, reasons and timestamps are absent.
- **Consent:** `consent_status` and `marketing_opt_in` support current preference distributions; purpose-level consent and change history are absent.

## 5. Snapshot KPIs supported by the dataset

| KPI | Observed sample result | Interpretation |
|---|---:|---|
| Registered users | 1,000 | Distinct simulated users in clean sheet |
| Email verification rate | 85.5% | 855 verified / 1,000 |
| Onboarding completion rate | 72.2% | 722 completed / 1,000; snapshot status, not completion conversion over time |
| 7-day active rate | 7.8% | 78 / 1,000; source-provided derived flag |
| 30-day active rate | 32.5% | 325 / 1,000; source-provided derived flag |
| Referral acquisition share | 11.9% | 119 / 1,000 |
| Google Sign-In share | 33.9% | 339 / 1,000 |
| Suspended account share | 7.7% | 77 / 1,000 |
| Consent accepted share | 92.3% | 923 / 1,000; purpose/history unavailable |
| Marketing opt-in share | 44.2% | 442 / 1,000 |

Additional source-level onboarding completion rates and descriptive KPI formulas are in the Excel KPI Catalogue and Onboarding by Source sheets. Source association is descriptive and must not be interpreted as causal acquisition effectiveness.

## 6. KPIs not calculable from Task 01

- Time to onboarding completion: no `onboarding_completed_at` timestamp.
- Login frequency by day/week/month: no login event table; `lifetime_sessions` is a cumulative snapshot.
- Session duration and session funnels: no `session_id` or session start/end events.
- Account status transition rate: no status history.
- Registration-to-first-login conversion time: no `first_login_at` timestamp.
- Retention cohorts based on dated activity: only precomputed `is_active_7d`/`is_active_30d` flags are supplied; no dated activity history.

## 7. Data-quality caveats and controls

- Four clean records have negative `days_since_registration` values; verify the as-of timestamp, timezone and derivation logic before use.
- 72 clean records have null `last_login_datetime`; treat null as unknown/no recorded login rather than imputing a date.
- `referral_source_detail` is conditional and should be required only when `acquisition_source = Referral`.
- Protect `full_name` and `email`; dashboards should use aggregates and `user_id` or pseudonymous keys only where user-level analysis is necessary.
- Document the definitions of `active_days`, `lifetime_sessions` and the 7-day/30-day active flags.

## 8. Recommended event requirements

The following are proposed analytical requirements, not confirmed implementation:

| Event | Required properties |
|---|---|
| `registration_completed` | `event_id`, `user_id`, `event_timestamp`, `acquisition_source`, `account_created_via`, `primary_device`, `platform` |
| `login_succeeded` / `login_failed` | `event_id`, `user_id`, `session_id`, `event_timestamp`, device/platform, result/reason code |
| `onboarding_started` / `onboarding_completed` | `event_id`, `user_id`, `event_timestamp`, milestone/step, completion status |
| `account_status_changed` | `event_id`, `user_id`, `previous_status`, `new_status`, `changed_at`, reason code, actor type |
| `consent_updated` | `event_id`, `user_id`, `consent_purpose`, `previous_value`, `new_value`, policy version, `event_timestamp` |

The supplied workbook does not prove that these events are currently emitted.

## 9. Conclusion

Task 01 supports user/account snapshot analysis and a specification for the fields already supplied. It does not support event-level lifecycle analysis. Available fields and calculable snapshot KPIs must remain separate from proposed identifiers/events and KPIs that are not calculable from this dataset.
