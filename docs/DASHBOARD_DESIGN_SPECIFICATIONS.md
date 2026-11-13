# Seven Dashboard Wireframes — Design Specifications

The seven dashboards are design specifications, not deployed reports. Every view should show an as-of timestamp, filter state, data freshness, metric definition and a caveat banner where the domain is not certified.

## Shared interaction rules

- Apply date, platform, acquisition cohort and account-state filters only where the source supports them.
- Every KPI should expose numerator, denominator, grain, source, date basis and exclusions.
- Drill-through is role-gated; avoid personal identifiers by default.
- Missing source history must display “Not available / not instrumented”, never zero.
- Show freshness, completeness and reconciliation state.

## 01 — Executive Overview

**Audience:** Product leadership and Operations. **Purpose:** high-level cross-domain view of acquisition, engagement and value flow.  
**Panels:** registrations; verified/onboarded status; supplied activity flags; task/reward flow; wallet/withdrawal status; referral milestones; freshness/quality strip.  
**Decision:** identify the domain requiring investigation.  
**Readiness:** only user snapshot metrics are reproducible now; transaction and time-series panels remain placeholders until certified event/ledger sources exist.

## 02 — User Analytics

**Audience:** Product and Growth. **Purpose:** registration, acquisition, verification, onboarding and lifecycle cohorts.  
**Panels:** registrations by period; source mix; verification/onboarding ratios; account-state distribution; onboarding by source; cohort matrix after event history exists.  
**Decision:** prioritise acquisition and onboarding investigations.  
**Readiness:** current snapshot supports status distribution and cross-sectional source table, not step timing or retention cohorts.

## 03 — Engagement

**Audience:** Product and Engagement Operations. **Purpose:** feature adoption, sessions, task activity, streaks, missions and repeat use.  
**Panels:** DAU/WAU/MAU only after qualifying event history; feature usage; task starts/completions; streak and mission activity; engagement trend.  
**Decision:** prioritise features and engagement interventions.  
**Readiness:** events are proposed; timestamped event stream is not evidenced in Task 01 data.

## 04 — Rewards

**Audience:** Product, Rewards Operations and Finance. **Purpose:** reward lifecycle, units, source, pending/credited/reversed states and ageing.  
**Panels:** reward decisions by state; units by source; approval-to-credit lag; pending ageing; reversals; reconciliation.  
**Decision:** investigate reward processing and reconciliation exceptions.  
**Readiness:** requires reward decision history and ledger; XP, VE and Gems remain separate units.

## 05 — Wallet

**Audience:** Wallet Operations and Finance. **Purpose:** posted ledger movement, credits, redemptions, reversals and closing balances.  
**Panels:** transaction mix; posted credits/debits; redemption; reversals/adjustments; balance by unit; reconciliation status.  
**Decision:** investigate ledger anomalies and reconciliation gaps.  
**Readiness:** requires immutable posted transactions; unlike units must never be summed.

## 06 — Withdrawals

**Audience:** Payments Operations and Finance. **Purpose:** requests, queues, completion/rejection outcomes, payout methods and processing duration.  
**Panels:** request state; completion/rejection; processing duration; method mix; requested vs settled amounts; ageing queue and exceptions.  
**Decision:** identify provider/method bottlenecks.  
**Readiness:** requires request, provider-attempt and settlement events; a request is not proof of payout.

## 07 — Referrals

**Audience:** Growth and Product. **Purpose:** referral creation, registration, activation and conversion by channel/cohort.  
**Panels:** referral funnel; created-to-converted funnel; cohort quality; activation/referrer performance; reward qualification; attribution exceptions.  
**Decision:** identify channels/cohorts producing activated users.  
**Readiness:** requires referral IDs, milestone timestamps and approved conversion/reward rules.

## Visual inventory

The companion Package M report contains 39 visual specifications with metric logic, sources, filters, dimensions, date range, refresh recommendation, business question, decision supported and readiness note.
