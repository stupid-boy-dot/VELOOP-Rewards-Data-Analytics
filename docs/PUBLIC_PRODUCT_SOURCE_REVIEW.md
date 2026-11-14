# VELOOP Rewards — Public Product Source Review

**Checked:** 14 November 2026  
**Purpose:** Supplement Task 01's simulated dataset evidence with official public product/help/legal documentation.

## Scope and method

Reviewed the official homepage, Help Center, withdrawal guidance, Level System guidance, Disclaimer and Privacy Policy. Only statements visible in those pages are recorded as public documentation. This review does not log into VELOOP, inspect the production app, query internal APIs, verify feature flags, test transactions or confirm backend implementation.

## What the public documentation supports

- The homepage promotes task, ad, survey, social, game, promo-code, captcha and app-task earning surfaces, and describes sign-up options including Google, Facebook, Apple or a crypto wallet.
- The Help Center documents Getting Started, Earning Rewards, Wallet & Exchange, Withdrawals and Safety & Account Rules. It lists watch ads, daily rewards, mining, tap-and-earn, captcha, streaks, spins, missions/badges, levels, leaderboard, follow-and-earn, wallet overview, Gems Exchange Center, Swap Center and referral rewards.
- The Help Center separates Lucky Draw, Referral Milestones, Team Battle, Collect Cards, Surprise Rewards and Mystery Rewards under Future Features. These preview items are not classified as current features here.
- The withdrawal page publishes a Rs.10 minimum, UPI/PayPal/Amazon Gift Card/Google Play Gift Card methods, and typical processing expectations of 24 hours (up to 72 hours in review cases). This is conditional guidance, not a guaranteed SLA or measured performance.
- The Level System page describes XP/levels as progression based on eligible activity and says thresholds and benefits may evolve. Task 01 has a snapshot XP balance, not XP event history or rule versions.
- The Disclaimer states rewards and displayed balances are not guaranteed cash ownership or unconditional withdrawal entitlement. Validation, delay, denial, reversal, correction or cancellation may apply under platform rules and review.
- The Privacy Policy describes categories of account, identity, device/technical, activity/transactional and tracking/analytics information. Policy disclosure is not proof that each field is captured by current systems.

## Analytics implications

1. Separate user actions, system state transitions and business outcomes. A provider callback, click or task event is not proof of reward credit or payout settlement.
2. Keep VE, XP, Gems, Tokens, Spins and fiat payout methods separate. Do not aggregate them without approved conversion rules and versioned owner sign-off.
3. Preserve financial lineage: immutable IDs, idempotency, status history, reversal links and reconciliation to authoritative ledgers.
4. Treat withdrawal thresholds/methods/timing as dated public guidance, not a KPI, target or guaranteed SLA.
5. Apply privacy-by-design. The policy is not an approved event payload, retention schedule or legal-basis approval.
6. Do not convert Future Features previews into current-state instrumentation requirements.

## Data boundary

Task 01 remains the only source for observed profiling and sample calculations. All input records are simulated/fictional. The workbook lacks task activity, rewards ledger, wallet transactions, withdrawal records, referral relationships and feature-event history. Public pages inform proposed specifications but cannot support cross-domain counts, joins, conversion rates, payout performance or live feature adoption.

**Public documentation is not production implementation evidence.** Feature availability, integrations, instrumentation, schemas, pipelines, dashboards, data quality, privacy enforcement and service levels remain To Be Verified.

## Official sources checked

| Source | URL | Use |
|---|---|---|
| VELOOP homepage | https://www.velooprewards.in/ | Publicly promoted features and account entry points |
| VELOOP Help Center | https://www.velooprewards.in/help-center | Public help/product categories and Future Features boundary |
| How Withdrawals Work | https://www.velooprewards.in/help-center/withdrawals/how-withdrawals-work | Published threshold, payout methods and conditional timing |
| Level System | https://www.velooprewards.in/help-center/earning/level-system | XP/level progression concepts and caveats |
| Disclaimer | https://www.velooprewards.in/disclaimer | Reward, payout and third-party caveats |
| Privacy Policy | https://www.velooprewards.in/privacy-policy | Public data categories and privacy caveats |

## Required confirmations

Product/Engineering must confirm feature availability, source-of-truth services, event contracts, state machines, provider callbacks/retries, ledger outcomes, timezones and retention. Finance/Product must approve unit conversion and reward accounting. Privacy/Legal must approve purpose, retention, access and processor controls. Until then, relevant specifications remain Proposed or To Be Verified.
