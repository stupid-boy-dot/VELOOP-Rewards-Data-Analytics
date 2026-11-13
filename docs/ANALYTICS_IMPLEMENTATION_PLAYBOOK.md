# VELOOP Rewards — Analytics Implementation Playbook

## Objective

Translate Task 01's proposed analytics design into an implementation sequence for VELOOP product, engineering, data, operations and privacy owners. This is a proposal, not confirmation that these components exist today.

## Target architecture

1. **Product/source systems:** identity and account, task/mission, reward engine, wallet ledger, withdrawal/payment, referral, support and content. Owners must confirm authoritative state and identifiers.
2. **Event collection:** approved client/server SDK or gateway. Prefer backend-authoritative events for credits, reversals, withdrawal state changes and referral qualification; client events record UI exposure and interaction.
3. **Raw immutable landing:** append-only records with event ID/name/schema version, occurred/received timestamps, source, user/session context and idempotency key where applicable.
4. **Validation and quarantine:** schema/type, required-field, timestamp, identity, enum, duplicate and late-arrival checks. Invalid records are quarantined with reason codes; source history is not silently overwritten.
5. **Curated models:** user/account, activity, task attempts, rewards, wallet ledger, withdrawals, referral milestones, feature events and support.
6. **Semantic/KPI layer:** versioned metric definitions, governed units, certified dimensions, approved as-of rules and limitations.
7. **Dashboards/alerts:** publish only after source coverage, reconciliation, access control, metric ownership and refresh monitoring pass release gates.

## Non-negotiable modelling controls

- A start event is not a business outcome: task started ≠ completed; reward approved ≠ credited; withdrawal requested ≠ settled.
- Use unique transaction IDs and idempotency for retry-safe credits/debits.
- Preserve append-only ledger entries; link reversals/adjustments to originals.
- Store amount and currency/unit together; never sum unlike units (VE, XP, Gems, Tokens).
- Store UTC event time and ingestion time separately; document reporting timezone and late-arrival policy.
- Define lifecycle states and denominator population for every KPI.
- Version event schemas; document breaking changes.
- Restrict row-level data to purpose-bound roles; aggregate by default.

## Phased rollout

| Phase | Work | Exit evidence |
|---|---|---|
| 0 — Source confirmation | Confirm owners, states, IDs, triggers, units, as-of dates, legal basis and provider status. | Signed source-to-event map; unknowns tracked as blockers. |
| 1 — Identity foundations | Implement account lifecycle, identity mapping, consent states, source metadata and schema registry. | Contract tests, duplicate/late-event tests and privacy review. |
| 2 — Engagement and earning | Instrument task, mission, feature, XP/VE and reward lifecycle. | Reconciled task attempts and reward decisions; replay tests. |
| 3 — Wallet and withdrawals | Implement authoritative ledger and provider attempt/settlement callbacks. | Ledger/provider reconciliation and reversal acceptance tests. |
| 4 — Referral and support | Implement invite, registration, activation, qualification, reward and support milestones. | Cohort/attribution tests and approved duplicate/self-referral rules. |
| 5 — Certified reporting | Build semantic metrics, seven dashboard views, freshness alerts and access controls. | KPI sign-off, quality SLOs, reconciliation and RBAC tests. |

## Standard event envelope

Common fields: `event_id`, `event_name`, `schema_version`, `occurred_at_utc`, `ingested_at_utc`, `source_system`, `environment`, `user_id` when known, `anonymous_id` when applicable, `session_id` when applicable, `correlation_id`, and idempotency key for state-changing transactions.

## Source-of-truth gates

| Domain | Authoritative source | Reconciliation |
|---|---|---|
| Users | Identity/account service | Registration/verification vs identity history |
| Tasks | Task and task-attempt service | Eligible attempts, starts, completions, approvals and rejects |
| Rewards | Reward decision service | Approved decision vs ledger credit/reversal |
| Wallet | Wallet ledger | Opening + credits - debits +/- adjustments = closing by unit |
| Withdrawals | Withdrawal orchestrator and provider settlement | Requests, attempts, provider status and settled amount |
| Referrals | Referral attribution service | Invite → attributed registration → activation → qualification → reward |
| Feature engagement | Client events plus server confirmation where needed | Coverage, identity match and session attribution |

## Dashboard publication gates

Do not publish a metric until its source, grain, event history, denominator, unit, timezone, deduplication, late-arrival policy, owner and reconciliation test are documented. Current Task 01 data supports sample-level status ratios only; temporal/transactional dashboards remain proposed.

## Ownership

Product owns definitions; engineering owns instrumentation/contracts; data owns ingestion/models/quality; finance and operations own transaction reconciliation; privacy/security/legal approve purpose/access/retention; the programme/reviewer owner approves acceptance.

## Initial priority backlog

1. Confirm authoritative source systems, lifecycle states and owners.
2. Approve event naming and common schema envelope.
3. Implement identity/account events and data contracts.
4. Implement server-authoritative reward and ledger events.
5. Reconcile wallet and withdrawal settlement history.
6. Implement referral milestone attribution.
7. Build validated marts and certified KPIs.
8. Release dashboards only after data-quality and privacy gates.
