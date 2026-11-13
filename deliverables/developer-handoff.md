# Developer Analytics Handoff — Task 01

**Status:** Proposed engineering handoff; every contract requires VELOOP product/engineering confirmation before implementation.

## 1. Common event envelope

Every event should carry:
- `event_id` (UUID; unique and immutable)
- `event_name` (approved registry value)
- `event_schema_version` (semantic version)
- `event_timestamp` (occurred-at time in UTC)
- `ingested_at` (ingestion time in UTC)
- `source_system` and `environment`
- `user_id` when authenticated; anonymous identity only under an approved identity policy
- `session_id` when session-scoped
- `correlation_id` for cross-service tracing
- idempotency key for state-changing reward, wallet and withdrawal actions

## 2. Proposed event contract catalogue

| Domain | Event names | Producer preference | Required business identifiers |
|---|---|---|---|
| Account | `user_registered`, `user_logged_in`, `user_logged_out`, `onboarding_started`, `onboarding_completed`, `account_status_changed` | Backend for committed account/auth state; frontend for UI-only interaction | user_id, event_id; session_id for login/logout; onboarding_version for onboarding; old_status/new_status for state transitions |
| Tasks | `task_viewed`, `task_opened`, `task_started`, `task_completed`, `task_failed` | Frontend for views/opens; backend for attempt and validated terminal outcomes | task_id, task_activity_id for attempts, session_id for start, validation_status for completion, failure_category for failure |
| Rewards / engagement | `reward_pending`, `reward_credited`, `reward_reversed`, `daily_reward_claimed`, `streak_updated`, `mission_started`, `mission_completed`, `badge_earned`, `spin_started`, `spin_completed` | Backend authoritative for reward and award states | reward_transaction_id, source_activity_id, amount, unit, status; claim_id; streak_id; mission_attempt_id; badge award_id; spin_attempt_id |
| Referrals | `referral_created`, `referral_registered`, `referral_activated`, `referral_converted` | Backend attribution service | referral_id, referrer_user_id, referred_user_id, activation_rule_version, conversion_rule_version |
| Wallet | `wallet_transaction_created`, `wallet_transaction_completed`, `wallet_transaction_reversed` | Backend wallet ledger only | transaction_id, transaction_type, amount, unit, status, original_transaction_id where reversal |
| Withdrawals | `withdrawal_requested`, `withdrawal_processing`, `withdrawal_completed`, `withdrawal_rejected`, `withdrawal_reversed` | Backend withdrawal orchestrator plus verified provider callback for settlement | withdrawal_id, requested/completed amount, unit, status, provider_reference, reason_category, original transaction reference where reversed |
| Support / content | `help_article_viewed`, `support_ticket_created` | Frontend for content view; backend for ticket creation | content_id/content_type or ticket_id/category/channel |

The event catalogue has **35 proposed event names**; see the full payload-level field list and validations in [the event tracking plan](event-tracking-plan.csv).

## 3. Validation and ingestion rules

1. Reject or quarantine malformed required identifiers, timestamps, enums and payload types. Capture a reason code and make rejection counts observable.
2. Require UTC ISO-8601 timestamps. Preserve both occurred-at and ingested-at; define allowed clock skew and late-arrival window with engineering.
3. Deduplicate telemetry by immutable event_id. Use business idempotency keys for transactional commands and never suppress legitimate repeat user behaviour.
4. Validate foreign keys and lifecycle state transitions. Examples: task completion must resolve to a started task_activity_id; reward credit must resolve to a reward decision; withdrawal completion requires authoritative provider/settlement evidence.
5. Do not store raw credentials, full payment details, unrestricted free text or unnecessary personal identifiers in event payloads.
6. Keep the wallet/reward ledger append-only. Corrections and reversals are compensating records linked to the original; do not overwrite historical transactions.
7. Amount must always be paired with an explicit unit. XP, VE, Gems, Tokens, Spins and currency cannot be summed together without a formally approved conversion model.

## 4. Minimum acceptance tests

| Test ID | Scenario | Expected result |
|---|---|---|
| AT-01 | Valid account registration | One event with unique event_id, stable user_id and UTC timestamp |
| AT-02 | Duplicate delivery of same event_id | One analytical event after deduplication; delivery attempt logged |
| AT-03 | Repeated legitimate task view | Both separate valid views remain countable |
| AT-04 | Task completion without valid task_activity_id | Rejected/quarantined; no completion KPI increment |
| AT-05 | Reward credit retried after timeout | Idempotency prevents duplicate ledger credit |
| AT-06 | Reward reversal with missing original transaction | Rejected/quarantined and exception surfaced |
| AT-07 | Wallet credit in two different units | Kept in separate unit groups; no cross-unit sum |
| AT-08 | Withdrawal requested but provider not settled | Remains pending/processing; not counted as completed |
| AT-09 | Provider sends duplicate completion callback | One finalised withdrawal; duplicate callback logged |
| AT-10 | Event arrives late | Stored with occurred-at and ingested-at; late-arrival rule applied |
| AT-11 | Unknown event schema version | Quarantined or routed to compatible handler; alert raised |
| AT-12 | Payload contains credential or raw payout detail | Sensitive field excluded/rejected before analytics storage |

## 5. Delivery and release gates

- Product approves event meaning, trigger, state transitions and KPI dependency.
- Engineering approves producer, schema, ID, idempotency and retry behaviour.
- Data approves event registry, ingestion checks, curated grain and metric implementation.
- Finance/Operations approve wallet, reward and payout reconciliation.
- Privacy/Security approve purpose, field minimisation, access and retention.
- No dashboard KPI is certified until source ownership, denominator, event coverage, unit, timezone, deduplication and reconciliation tests pass.

## 6. Source boundary

The supplied Task 01 exercise workbook does not provide all timestamped transactional/event source records. The 35 contracts are proposals for future instrumentation and must not be described as already implemented in VELOOP production.
