# Publication Inventory — 21 Final Deliverables

This page maps each required deliverable to files that are directly accessible in the public GitHub repository. It distinguishes the public source representation from the formatted PDF/XLSX/PPTX handover files, which are not currently attached to the GitHub release.

For the reviewer-ready route, use the [Reviewer Access Guide](REVIEWER_ACCESS_GUIDE.md). A downloadable 52-file [public source bundle](https://github.com/stupid-boy-dot/VELOOP-Rewards-Data-Analytics/releases/download/task01-review-v2/VELOOP_Task01_Public_Source_Bundle_Revision4.zip) is attached to the release.

| # | Required deliverable | Direct public evidence |
|---:|---|---|
| 01 | Executive Summary | [Executive summary](../deliverables/executive-summary.md) |
| 02 | Product Data Audit | [Audit report](../deliverables/product-data-readiness-audit.md) · [Audit schedule](../deliverables/product-data-audit.csv) |
| 03 | Data Coverage Matrix | [Coverage matrix](../deliverables/data-coverage-matrix.csv) · [Gap assessment](../deliverables/gap-assessment.csv) |
| 04 | User and Account Analytics | [Data dictionary](../deliverables/data-dictionary.csv) · [Observed metrics](../analysis/observed_metrics.csv) · [Coverage matrix](../deliverables/data-coverage-matrix.csv) |
| 05 | Earning and Reward Analytics | [Earning/reward specification](../deliverables/earning-reward-spec.csv) |
| 06 | Wallet and Withdrawal Analytics | [Wallet/withdrawal specification](../deliverables/wallet-withdrawal-spec.csv) |
| 07 | Referral and Engagement Analytics | [Referral/engagement specification](../deliverables/referral-engagement-spec.csv) |
| 08 | Event Tracking Plan | [Event tracking plan](../deliverables/event-tracking-plan.csv) · [Event classification](../deliverables/event-classification-guide.csv) |
| 09 | Data Dictionary | [Data dictionary](../deliverables/data-dictionary.csv) |
| 10 | Logical Data Model / ERD | [Rendered ERD](LOGICAL_DATA_MODEL.md) · [Mermaid source](../diagrams/LOGICAL_MODEL.mmd) |
| 11 | KPI Catalogue | [KPI catalogue](../deliverables/kpi-catalogue.csv) |
| 12 | Simulated Data Profiling | [Observed metrics](../analysis/observed_metrics.csv) · [Onboarding breakdown](../analysis/onboarding_by_acquisition_source.csv) · [QA counts](../analysis/messy_audit_quality_counts.csv) · [Reproduction script](../analysis/reproduce_metrics.py) · [Reproducibility guide](REPRODUCIBILITY.md) |
| 13 | Data Quality Audit | [Data quality issue register](../deliverables/data-quality-issue-register.csv) · [Quality controls](../deliverables/quality-control-framework.csv) · [QA counts](../analysis/messy_audit_quality_counts.csv) |
| 14 | Dashboard Blueprint | [Seven dashboard wireframes](../dashboard-wireframes.html) · [39 visual specifications](../deliverables/dashboard-visual-specifications.csv) · [Design explanations](DASHBOARD_DESIGN_SPECIFICATIONS.md) |
| 15 | Developer Analytics Handoff | [Developer handoff](../deliverables/developer-handoff.md) · [Event tracking plan](../deliverables/event-tracking-plan.csv) |
| 16 | Data Pipeline and Operating Model | [Implementation playbook](ANALYTICS_IMPLEMENTATION_PLAYBOOK.md) · [Pipeline proposal](../deliverables/pipeline-proposal.csv) |
| 17 | Privacy, Access and Governance | [Privacy/governance schedule](../deliverables/privacy-governance.csv) · [Third-party dependency controls](../deliverables/third-party-dependency-controls.csv) |
| 18 | Analytics Readiness Assessment | [Readiness scorecard](../deliverables/readiness-scorecard.csv) · [Gap assessment](../deliverables/gap-assessment.csv) |
| 19 | Assumption and Verification Register | [Assumption register](../deliverables/assumption-register.csv) · [Source verification register](../deliverables/source-verification-register.csv) |
| 20 | Prioritised Implementation Backlog | [Implementation backlog](../deliverables/implementation-backlog.csv) |
| 21 | Final Consolidated Report | [Final consolidated report](../deliverables/final-consolidated-report.md) |

## Format boundary

The public repository and source bundle expose the analytical source files in Markdown, CSV, HTML, Mermaid and Python formats. The separate formatted PDF reports, Excel workbooks and PowerPoint deck are **not currently attached as GitHub release assets**. The original row-level Task 01 source workbook is excluded from public hosting because it contains identifiers; use the authorised assignment copy for local reproduction.

All Task 01 values are simulated/fictional. Proposed events, dashboards, pipelines and controls are designs requiring owner approval; they are not proof of production implementation.
