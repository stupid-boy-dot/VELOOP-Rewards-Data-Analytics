# Data Integrity & Evidence Policy

## Mandatory source rule

The supplied Task 01 assignment states that the dataset is fictional/simulated. It must never be described as actual VELOOP users, earnings, withdrawals, revenue, retention, conversion rates, performance or company statistics.

## Evidence classifications

| Classification | Meaning |
|---|---|
| Source-observed | Directly present in the supplied workbook or assignment text |
| Calculated | Reproducibly calculated from the supplied simulated records |
| Proposed | Recommended analytics requirement, event, schema, metric, control or design |
| To Be Verified | Product or implementation detail that the available evidence does not confirm |

## Handling unknowns

Important product facts must be recorded with the information found, source, source type, date checked, status and limitations. Assumptions must not silently become facts.

Example: a session identifier may be proposed because it enables session-level analysis, but the current implementation status requires engineering verification.

## Privacy and publication

The public repository excludes the original user-level workbook because it contains name/email-style columns. Those fields are in a fictional dataset, but excluding them is a prudent public-publication control. Aggregate findings and documented methodology may be published with the simulated-data caveat.

Do not publish passwords, API keys, tokens, authentication secrets, payment credentials or private security controls.

## Interpretation controls

- A registration is not automatically a successful referral conversion.
- An earning activity is not proof that a reward was credited.
- A withdrawal request is not proof of a successful payout.
- Current XP/balance snapshots do not provide complete transaction histories.
- Snapshot activity flags do not substitute for event-level daily activity records.
- A designed dashboard is not a deployed production dashboard.
