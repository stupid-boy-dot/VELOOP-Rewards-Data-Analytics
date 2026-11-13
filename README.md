# VELOOP Rewards — Task 01 Data Analytics

**Review status:** Initial evaluation 65%; Task 01 was **not approved**. This repository contains the Revision 2 evidence prepared for VELOOP re-review. Final acceptance remains with VELOOP.

**Assignment:** Product Analytics, Data Readiness & Data Management Blueprint.

## Start here

1. [Review response and requirement-to-evidence map](public/docs/REVIEW_RESPONSE.md)
2. [Executive summary](public/deliverables/executive-summary.md)
3. [Product data readiness audit](public/deliverables/product-data-readiness-audit.md)
4. [Final consolidated report](public/deliverables/final-consolidated-report.md)
5. [Reproducibility guide](public/docs/REPRODUCIBILITY.md)
6. [Seven-dashboard viewer](public/dashboard-wireframes.html)
7. [Analytics implementation playbook](public/docs/ANALYTICS_IMPLEMENTATION_PLAYBOOK.md)

## Direct links to review deliverables

| Required evidence | Direct file |
|---|---|
| Executive summary | [Executive summary](public/deliverables/executive-summary.md) |
| Product data audit | [Audit report](public/deliverables/product-data-readiness-audit.md) · [Product-area audit schedule](public/deliverables/product-data-audit.csv) |
| Data coverage and gaps | [Product-area mapping](public/deliverables/product-area-mapping.csv) · [Gap register](public/deliverables/gap-assessment.csv) |
| Simulated data profiling / calculations | [Reproducibility guide](public/docs/REPRODUCIBILITY.md) · [Observed metrics](public/analysis/observed_metrics.csv) · [Onboarding by source](public/analysis/onboarding_by_acquisition_source.csv) |
| Data-quality audit | [Quality audit report](public/deliverables/data-quality-audit-report.md) · [Issue register](public/deliverables/data-quality-issue-register.csv) · [Messy-fixture counts](public/analysis/messy_audit_quality_counts.csv) |
| Reproduction code | [Python script](public/analysis/reproduce_metrics.py) · [Run instructions](public/analysis/README_REPRODUCIBILITY.md) |
| Data dictionary | [84-field data dictionary CSV](public/deliverables/data-dictionary.csv) |
| KPI catalogue | [42 KPI definitions](public/deliverables/kpi-catalogue.csv) |
| Event tracking plan | [35 event contracts](public/deliverables/event-tracking-plan.csv) · [Event classification guide](public/deliverables/event-classification-guide.csv) |
| Developer analytics handoff | [35 implementation requirements](public/deliverables/developer-handoff.csv) |
| Logical model / ERD | [ERD SVG](public/diagrams/LOGICAL_MODEL.svg) · [Mermaid source](public/diagrams/LOGICAL_MODEL.mmd) · [Entity model](public/deliverables/entity-model.csv) |
| Seven dashboard wireframes | [7-screen viewer](public/dashboard-wireframes.html) · [Design explanations](public/docs/DASHBOARD_DESIGN_SPECIFICATIONS.md) · [Dashboard visual schedule](public/deliverables/dashboard-blueprint.csv) |
| Pipeline and operating model | [Implementation playbook](public/docs/ANALYTICS_IMPLEMENTATION_PLAYBOOK.md) · [Pipeline proposal](public/deliverables/pipeline-proposal.csv) |
| Privacy and governance | [Governance schedule](public/deliverables/privacy-governance.csv) · [Third-party controls](public/deliverables/third-party-dependency-controls.csv) |
| Implementation backlog | [Prioritised backlog](public/deliverables/implementation-backlog.csv) |
| Assumptions and verification | [Assumption register](public/deliverables/assumption-register.csv) · [Source verification](public/deliverables/source-verification-register.csv) |
| Final documentation | [Consolidated report](public/deliverables/final-consolidated-report.md) · [Review response](public/docs/REVIEW_RESPONSE.md) |

## Analytical calculations and limits

The clean sample contains 1,000 records and 1,000 unique non-null user IDs. Calculated sample results include verified email 855/1,000 (85.5%), onboarding complete 722/1,000 (72.2%), supplied Active 7d flag 78/1,000 (7.8%), Active 30d flag 325/1,000 (32.5%), Referral acquisition share 119/1,000 (11.9%), consent accepted 923/1,000 (92.3%) and marketing opt-in 442/1,000 (44.2%). The separate 1,008-row messy QA fixture contains 8 excess duplicate rows and is not the KPI population.

All source data is marked **SIMULATED / FICTIONAL**. These figures describe only the Task 01 exercise sample, not VELOOP production users or performance. Snapshot flags are not event-derived DAU/MAU or retention. Referral acquisition is not referral conversion. Transactional and time-series KPIs require the corresponding history tables.

## Data protection and evidence boundary

The public repository intentionally excludes the original row-level source workbook and the original user-level profiling workbook because they contain name/email-style fields. Aggregate counts, formulas, methodology and review-safe specifications are published instead. The messy sheet is an audit fixture only. Proposed events, architecture, data controls and dashboards are designs—not verified production implementations.

The live GitHub Pages site is a static project showcase and wireframe viewer, not a deployed VELOOP application or interactive production BI dashboard.

## Current status

Revision 2 responds to the review requirements and is prepared for independent review. It does **not** claim Task 01 approval or internship completion. See [current progress](docs/CURRENT_PROGRESS.md) and [review response](public/docs/REVIEW_RESPONSE.md).
