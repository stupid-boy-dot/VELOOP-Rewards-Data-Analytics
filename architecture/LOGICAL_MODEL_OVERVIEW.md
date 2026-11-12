# Logical Data Model — Overview

The model is a proposed analytical design. It does not assert that these entities or keys already exist in VELOOP production systems.

## Core entities

- Users
- Tasks
- Task Activity
- Rewards
- Wallet Transactions
- Withdrawals
- Referrals
- Feature Events

Additional justified subject areas include missions, badges, levels, XP activity, support tickets and content.

## Grain distinctions

- **Task** describes the configured earning opportunity; **Task Activity** describes one user's attempt or participation.
- **Reward decision/state** should be distinguishable from the wallet ledger credit.
- **Withdrawal request** should be distinct from provider processing attempts and final settlement evidence.
- **Referral creation, registration, activation and conversion** are separate milestones.
- **Feature Event** records an event occurrence; it should have a unique event ID and an appropriate user/session/context reference where applicable.

## Key design requirements

- Stable primary keys for each entity.
- Explicit foreign-key relationships and documented cardinality.
- Transaction identifiers and idempotency controls for financial/reward movements.
- Timestamp semantics and timezone conventions.
- Amount and unit stored together; unlike units must not be summed.
- Reversals/corrections linked to their original transactions instead of overwriting history.
- Support for schema/version evolution.

## Verification boundary

The assignment asks for a logical data model and ER diagram. It does not provide evidence that this proposed model is the live VELOOP database schema.
