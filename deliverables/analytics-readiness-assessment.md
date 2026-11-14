# VELOOP — Analytics Readiness Assessment

**VELOOP Rewards | Data Analyst Internship — Task 01 | Version 1.0 | 10 November 2026**

This assessment evaluates evidence available in the approved Task 01 dataset and distinguishes observed coverage from proposed future capability. It does not assess unverified internal production implementation.

**Evidence boundary:** Proposed design based on the assignment brief and the approved Task 01 simulated user dataset. The Task 01 workbook does not contain relevant production fact tables for several product domains. This document does not claim that proposed events, tables, controls or infrastructure are implemented.

| Dimension | Evidence rating | Evidence | Impact | Priority | Next action |
|---|---|---|---|---|---|
| Event coverage | Not evidenced | No timestamped feature-event stream in Task 01 workbook | Cannot calculate event-derived DAU/MAU, feature adoption, funnels or repeat usage | Critical | Approve and implement event catalogue; validate event delivery |
| Data model | Partially specified | User entity available; task/reward/wallet/withdrawal/referral fact entities absent | Cross-domain joins and transaction lineage unavailable | Critical | Implement stable PK/FK contracts and immutable transaction IDs |
| Data dictionary | Partial | Source dictionary has 25 rows; platform and country omitted despite appearing in clean sheet; proposed model extends to 84 fields | Ambiguous fields and ownership risk | High | Approve canonical dictionary and schema owner |
| KPI definitions | Specified in blueprint | 42 KPIs defined; many require absent fact/event datasets | KPI availability depends on instrumentation | High | Approve metric contracts; do not populate unsupported metrics |
| Data quality | Assessed for user workbook | Clean/messy user sheets profiled; no task/ledger data available to test | Quality status beyond user data unknown | High | Apply quality controls to each new data domain |
| Dashboard readiness | Blueprint only | User snapshot supports limited descriptive views; domain dashboards lack fact tables | Operational dashboards would be empty or misleading now | High | Build after data contracts and pipeline validation |
| Engineering instrumentation | Not evidenced | No implementation logs, source code or event samples provided in Task 01 data | Cannot confirm any proposed event is currently emitted | Critical | Engineering review and instrumentation implementation |
| Access control | Not evidenced | No role/access matrix or policy evidence in supplied dataset | Privacy/access posture cannot be rated as implemented | High | Approve least-privilege access and sanitised data products |
| Documentation | Partially evidenced | Assignment, Task 01 README and source dictionary available; source dictionary omissions observed | Definitions and governance need owner approval | Medium | Maintain versioned source register and change log |
| Reporting operations | Not evidenced | No refresh/pipeline/dashboard evidence in supplied dataset | Freshness and reliability cannot be assessed | High | Define pipeline ownership, monitoring and failure runbooks |

## Interpretation and control notes

Ratings describe only the evidence available in the supplied Task 01 workbook. **Not evidenced** means absent from this dataset, not proof that a capability does not exist inside VELOOP.

All observed values are simulated/fictional. Proposed designs require product, engineering and relevant owner approval before implementation.
