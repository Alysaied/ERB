# Non-Functional Requirements Review Report

**Document Owner:** Senior Solution Architect  
**Purpose:** Consolidated quality review of all IMS non-functional requirements before system design  
**Audience:** Steering committee, product owner, solution architects, security, DevOps, QA, and delivery leads  
**Scope:** Analysis of nine NFR artifact sets — gaps, conflicts, risks, ambiguities, and unrealistic expectations  
**Review Date:** 2026-07-03  
**Status:** Pre–System Design Gate Review

---

## 1. Executive Summary

The IMS non-functional requirements suite comprises **nine documents** and **204 individual requirements** covering performance, scalability, availability, reliability, security, logging, monitoring, backup/DR, and compliance. The artifacts are well-structured, business-aligned, and traceable to functional requirements, KPIs, and business constraints.

**Overall assessment:** The NFR suite is **suitable as a design input** provided that **critical conflicts are resolved**, **blocking ambiguities are closed**, and **a phased compliance and capacity baseline program** is completed before architecture sign-off.

| Assessment Area | Rating | Summary |
|-----------------|--------|---------|
| **Completeness** | Amber | Strong operational coverage; gaps in integration, usability, data quality, and environment governance |
| **Consistency** | Amber | Several numeric conflicts between availability budgets and uptime percentages |
| **Testability** | Green | Most requirements have measurable success criteria |
| **Feasibility (MVP)** | Amber | Aggressive RPO/RTO, password policy, and audit retrieval targets need validation against budget and constraints |
| **Design Readiness** | Amber | Proceed after resolving items in Section 8 (Gate Checklist) |

### NFR Document Inventory

| # | Document | ID Prefix | Requirements | Must Have |
|---|----------|-----------|--------------|-----------|
| 1 | Performance Requirements | NFR-PERF | 27 | 11 |
| 2 | Scalability Requirements | NFR-SCAL | 22 | 0* |
| 3 | Availability & Reliability Requirements | NFR-AVL / NFR-REL | 25 | 14 |
| 4 | Security Requirements | NFR-SEC | 32 | 22 |
| 5 | Logging Requirements | NFR-LOG | 28 | 22 |
| 6 | Monitoring Requirements | NFR-MON | 26 | 18 |
| 7 | Backup & Disaster Recovery Requirements | NFR-BDR | 24 | 19 |
| 8 | Compliance Requirements | NFR-COM | 22 | 16 |
| | **Total** | | **204** | **~122** |

\*Scalability requirements do not assign MoSCoW priority per requirement — see Section 6.3.

---

## 2. Review Method

Each NFR document was reviewed for:

1. **Internal consistency** — numeric thresholds, terminology, and priority alignment  
2. **Cross-document consistency** — duplicate, conflicting, or orphaned requirements  
3. **Alignment with business constraints** — LC-01–LC-05, OC-01–OC-02, TEC-01–TEC-06, TC-03–TC-04  
4. **Alignment with functional requirements** — FR-081–FR-090 and phase tags (MVP / Phase 2 / Phase 3)  
5. **Design readiness** — whether requirements are actionable without implementation prescription  
6. **Feasibility** — given fixed budget (BC-01), no offline MVP (TEC-03), limited IT capacity (ORC-04), and missing baselines

---

## 3. Domain Analysis

### 3.1 Performance (NFR-PERF)

**Strengths**
- Clear percentile-based response time targets tied to user workflows
- Good linkage between concurrent users, throughput, and response time
- Baseline validation program (PA-01 – PA-05) before measurement

**Issues Identified**

| ID | Type | Finding |
|----|------|---------|
| PERF-R-01 | Ambiguity | "Routine screen interactions" and "standard operational dashboard" are not defined in an observable register — UAT cannot test without a screen inventory |
| PERF-R-02 | Missing | No performance requirements for **bulk import** (FR-090 go-live) or **manual finance export** (TEC-05) — high-risk MVP activities |
| PERF-R-03 | Missing | No performance target for **notification delivery** beyond NFR-PERF-014 (5 minutes) — overlaps with monitoring but not load-tested under peak |
| PERF-R-04 | Unrealistic | NFR-PERF-026 (Could Have): 12-month full-catalog audit extract in **15 minutes** may be infeasible at medium-term SKU growth (NFR-SCAL-010: +50%) without archival tiering strategy |
| PERF-R-05 | Risk | NFR-PERF-017 requires 12-month history in **10 seconds** while NFR-SCAL-015 only mandates 12 months online near-term — performance target applies to online data only, but this is not stated |

**Recommendations**
- Publish an **Essential Screens and Reports Register** mapping each performance target to named UI views and report IDs
- Add NFR-PERF-028 (proposed): import job completion within agreed go-live window; export job within finance close SLA
- Clarify NFR-PERF-017 scope: "online operational store" vs. "archived retention store"

---

### 3.2 Scalability (NFR-SCAL)

**Strengths**
- Comprehensive growth dimensions with planning horizons (0–18 months, 18–36 months, 3–5 years)
- Growth Planning Reference table provides sizing inputs
- Explicit linkage to NFR-PERF at each tier

**Issues Identified**

| ID | Type | Finding |
|----|------|---------|
| SCAL-R-01 | Ambiguity | **No MoSCoW priority** on any of 22 requirements — delivery teams cannot phase scalability investments |
| SCAL-R-02 | Missing | No **absolute baseline numbers** — all growth is relative (%, multipliers) but Primary Locations Register and catalog size are not yet validated (per business discovery review) |
| SCAL-R-03 | Conflict | NFR-SCAL-015 (24–36 months online history) vs. NFR-COM-006 / NFR-BDR-005 (**7-year** retention) — scalability doc addresses online accessibility; compliance addresses retention — **tiered data architecture implied but not specified** |
| SCAL-R-04 | Unrealistic | NFR-SCAL-019 (cost grows ≤ 50% of order volume rate) is a **business outcome**, not a system NFR — depends on licensing, headcount, and process — should be reclassified as a KPI/business objective |
| SCAL-R-05 | Risk | NFR-SCAL-008 (250% daily volume at one location) combined with NFR-PERF-013 (200% peak day) — different multipliers for related concepts; harmonize "peak day" vs. "sustained high-volume day" |

**Recommendations**
- Add MoSCoW priority to each NFR-SCAL requirement
- Replace NFR-SCAL-019 with a system-scoped requirement (e.g., "license and infrastructure cost per transaction must not increase more than X% at 2× volume") or move to Success Metrics
- Publish **Capacity Baseline Workbook** with validated SKU count, transaction volumes, and location count before architecture sizing

---

### 3.3 Availability (NFR-AVL)

**Strengths**
- Location-aware business hours model
- Separate targets for essential functions vs. reporting
- Peak season elevation (99.7%) reflects business risk

**Issues Identified**

| ID | Type | Finding |
|----|------|---------|
| AVL-R-01 | **Conflict** | **NFR-AVL-001** requires **≥ 99.5% uptime** during business hours; **NFR-AVL-009** allows **≤ 3 hours** cumulative unplanned downtime per location per month. At minimum planning assumption of **60 business hours/month** (10 hrs × 6 days), 3 hours = **95.0% uptime** — **contradicts 99.5%** (which allows only ~18 minutes/month at 60 hours) |
| AVL-R-02 | **Conflict** | **NFR-AVL-003** requires **≥ 99.7%** peak uptime AND **zero peak days > 1 hour** downtime. A single 1-hour outage on one peak day at 10 business hours = **90% that day** — fails 99.7% if more than one such day occurs in peak period |
| AVL-R-03 | Ambiguity | "Essential functions" referenced across AVL, REL, MON, BDR but **Essential Function Register not yet published** (AA-05) |
| AVL-R-04 | Missing | No availability SLA for **notification delivery** as an essential adjacent function — outages may pass AVL-001 while alerts are undelivered (KPI-15) |
| AVL-R-05 | Risk | **TEC-03**: no offline MVP — availability requirements assume connectivity; **NFR-MON-019** covers network path but no business availability credit when location network fails vs. application fails |

**Recommendations**
- **Resolve AVL-R-01 immediately:** Either tighten monthly budget to **≤ 18 minutes** at 99.5%, or relax uptime target to **≥ 95%** to align with 3-hour budget — recommended: **99.5% target with ≤ 0.5% monthly downtime budget (~18 min at 60 hrs)**
- Harmonize peak season: define peak period length and reconcile daily vs. period uptime math
- Publish Essential Function Register before UAT

---

### 3.4 Reliability (NFR-REL)

**Strengths**
- Strong data integrity requirements (zero silent loss, balance consistency, concurrent integrity)
- Recovery validation before operational release (NFR-REL-005)
- Business continuity procedure requirement bridges TEC-03 gap

**Issues Identified**

| ID | Type | Finding |
|----|------|---------|
| REL-R-01 | Ambiguity | NFR-REL-011 (location fault isolation) — business requirement assumes **one location's failure does not affect others**; achievable at application level for data but not if shared regional infrastructure fails — scope undefined |
| REL-R-02 | Conflict | NFR-REL-003 (all outage transactions recorded before next business day) vs. NFR-REL-007 (≤ 15 min data loss) — if RPO met, re-entry should be minimal; if not, next-day re-entry may violate movement compliance (KPI-23) — **recovery procedure priority unclear** |
| REL-R-03 | Duplicate | NFR-REL-009 (audit trail) duplicates NFR-SEC-013, NFR-LOG-010, NFR-COM-010 — consistent but quadruple-counted in compliance testing |
| REL-R-04 | Unrealistic | NFR-REL-010: **zero** double-allocation incidents per month — admirable but **not statistically measurable** at low volumes; define as "zero confirmed" with audit sample size |
| REL-R-05 | Missing | No reliability requirement for **scheduled job failure recovery** (reports, alerts, KPI calculation) — only logging (NFR-LOG-025) and monitoring (NFR-MON-012) |

**Recommendations**
- Define NFR-REL-011 scope: "other locations' essential functions unaffected by application-level failure at one location"
- Add NFR-REL-015 (proposed): failed scheduled jobs retried and cleared within 1 business hour
- Consolidate audit trail requirements into a **single authoritative NFR** with cross-references

---

### 3.5 Security (NFR-SEC)

**Strengths**
- Comprehensive RBAC, segregation of duties, and session management
- Password and authentication requirements clearly stated
- Privacy requirements aligned with LC-01

**Issues Identified**

| ID | Type | Finding |
|----|------|---------|
| SEC-R-01 | Risk | **NFR-SEC-010/011**: 12-character passwords, 90-day rotation — may **conflict with warehouse adoption** (KPI-22) and BA-05 (password usability validation) — shared terminals exacerbate lockout risk (NFR-SEC-003) |
| SEC-R-02 | Missing | No **enterprise identity integration** requirement (SSO/SAML) — TEC-06 requires company access policy; large user base across locations typically needs IdP federation |
| SEC-R-03 | Missing | No **separation of environments** requirement (production vs. UAT vs. training) — data leakage risk during rollout |
| SEC-R-04 | Ambiguity | NFR-SEC-004 re-authentication for high-risk actions is **Should Have** but NFR-SEC-008 approval limits and NFR-COM-009 segregation are **Must Have** — phased security gap for high-value transactions |
| SEC-R-05 | Conflict | NFR-SEC-031 (anonymize departed users in 90 days) vs. NFR-COM-020 (7-year log retention with user identity) — procedure referenced but **no authoritative conflict resolution rule** documented in NFR suite |
| SEC-R-06 | Missing | No **vulnerability / security patch** cadence requirement at business level (e.g., critical patches within X days) |

**Recommendations**
- Elevate NFR-SEC-004 to **Must Have** for high-value adjustments, bulk import, and role changes — or define compensating manual control until Phase 2
- Publish **Privacy vs. Audit Retention Decision Matrix** (Legal-owned) referenced by NFR-SEC-031 and NFR-COM-004
- Add NFR-SEC-033 (proposed): production data must not be used in non-production environments without anonymization
- Consider **phased password policy**: strict policy for admin/finance; pragmatic policy for warehouse shared terminals with compensating controls (short session timeout — already NFR-SEC-021)

---

### 3.6 Logging (NFR-LOG)

**Strengths**
- Comprehensive event taxonomy across business, security, and admin actions
- Standard log attributes and correlation requirements
- Master event logging register requirement (NFR-LOG-003)

**Issues Identified**

| ID | Type | Finding |
|----|------|---------|
| LOG-R-01 | Risk | **204+ requirements generate high log volume**; 7-year retention (NFR-LOG-027) — **no storage growth or cost NFR** — sustainability risk |
| LOG-R-02 | Duplicate | Extensive overlap with NFR-SEC-025–028 (security logging) and NFR-COM-010–011 (auditability) |
| LOG-R-03 | Ambiguity | NFR-LOG-009 sensitive data access logging is **Should Have** but NFR-COM-003 privacy minimization is **Should Have** — GDPR accountability may require access logging as Must Have where personal data processed |
| LOG-R-04 | Missing | No **log retention tiering** (hot/warm/cold) requirement — conflicts with 7-year retention and 15-minute audit export performance |
| LOG-R-05 | Missing | No **clock synchronization** requirement — correlation across locations (NFR-LOG-028) fails without time sync standard |

**Recommendations**
- Add NFR-LOG-029 (proposed): all log timestamps synchronized to agreed enterprise time source
- Define log retention tiers in architecture: hot (90 days, full query), warm (24 months), cold (7 years, export-only)
- Elevate NFR-LOG-009 to Must Have if GDPR applies to customer-linked fulfillment data

---

### 3.7 Monitoring (NFR-MON)

**Strengths**
- Layered monitoring model (health, performance, errors, KPIs, infrastructure)
- Alert severity taxonomy and escalation chain
- Location-specific connectivity monitoring (NFR-MON-019)

**Issues Identified**

| ID | Type | Finding |
|----|------|---------|
| MON-R-01 | Conflict | **NFR-MON-001** detects outage within **5 minutes**; **NFR-REL-004** requires business notification within **30 minutes** — aligned, but **NFR-MON-023** requires Critical alert acknowledgment within **15 minutes** — during outage, ops may be fixing before acknowledging — define acknowledgment vs. response |
| MON-R-02 | Ambiguity | NFR-MON-006 Tier 2 KPI monitoring is **Must Have** but many KPIs depend on **Phase 2/3 functional capabilities** (per project scope advanced analytics) — which KPIs are MVP-monitorable? |
| MON-R-03 | Missing | No **monitoring of manual finance reconciliation** process (TEC-05) — failure invisible until month-end |
| MON-R-04 | Risk | NFR-MON-004 peak monitoring at **30-second intervals** — operational burden; no requirement that monitoring itself must not degrade performance |
| MON-R-05 | Duplicate | Backup monitoring (NFR-MON-020) duplicates NFR-BDR-021 |

**Recommendations**
- Publish **MVP KPI Monitoring Subset** — minimum 8 KPIs monitorable from MVP features (suggest: KPI-01, 03, 11, 15, 22, 23, 24, plus transaction volume)
- Clarify alert acknowledgment: auto-ack on responder login acceptable
- Add synthetic monitoring duty cycle limit to avoid becoming a performance load source

---

### 3.8 Backup & Disaster Recovery (NFR-BDR)

**Strengths**
- Clear RPO/RTO table aligned with NFR-REL
- Critical data tier classification
- Quarterly recovery test requirement

**Issues Identified**

| ID | Type | Finding |
|----|------|---------|
| BDR-R-01 | **Conflict** | **NFR-BDR-010** (RTO ≤ 2 hours, Must Have) vs. **NFR-BDR-014** (geographic DR, Should Have) — **2-hour RTO is unlikely achievable without pre-built DR capability** that is only Should Have in Phase 2 |
| BDR-R-02 | Unrealistic | **15-minute RPO** (NFR-BDR-001, Must Have) implies near-continuous protection — **significant cost**; may conflict with **BC-01 fixed budget** and **BC-03 capex/opex caps** |
| BDR-R-03 | Ambiguity | Tier 3 governance data has **RPO ≤ 24 hr** in critical data table but **7-year retention** — recovery test must clarify tier-specific RPO |
| BDR-R-04 | Missing | No **recovery communication** integration with NFR-REL-004 / NFR-MON-026 during DR scenario |
| BDR-R-05 | Risk | Pre-change backup (NFR-BDR-003) required before every release — **may conflict with agile delivery frequency** if not automated |

**Recommendations**
- Split RTO requirements: **Infrastructure failure (2 hr)** vs. **Site disaster (8–24 hr)** with explicit scenarios
- Validate 15-minute RPO cost against BC-01 budget in architecture options analysis — present **business choice**: accept 1-hour RPO at lower cost vs. 15-minute at premium
- Automate pre-release backup as release pipeline gate

---

### 3.9 Compliance (NFR-COM)

**Strengths**
- Maps regulations to required controls clearly
- Conditional applicability table for SOX, GDPR, lot traceability
- Strong financial and audit alignment

**Issues Identified**

| ID | Type | Finding |
|----|------|---------|
| COM-R-01 | Ambiguity | GDPR stated as Must Have but **operating jurisdictions not confirmed** (CA-01) — may be over-scoped or under-scoped |
| COM-R-02 | Conflict | **NFR-COM-007** (finance reconciliation Must Have) vs. **TEC-05** (manual finance export MVP) — compliance requires capability but integration is manual — **control is procedural, not systemic** |
| COM-R-03 | Gap | **NFR-COM-018** (lot traceability) is Could Have but **domain knowledge** flags regulated products as potential gap — trigger condition unclear |
| COM-R-04 | Missing | No **regulatory breach notification** requirement (e.g., GDPR 72-hour notification) |
| COM-R-05 | Missing | No **data processing agreement** requirement for subprocessors/hosting providers at business level |

**Recommendations**
- Legal to confirm jurisdiction and applicability matrix before design
- Add NFR-COM-023 (proposed): personal data breach assessment and notification procedure within statutory deadlines
- Define NFR-COM-018 trigger: "applies if > X% of catalog is expiry-dated or lot-controlled"

---

## 4. Cross-Cutting Findings

### 4.1 Critical Conflicts (Resolve Before Design)

| # | Conflict | Documents | Resolution Options |
|---|----------|-----------|-------------------|
| C-01 | **99.5% uptime vs. 3 hr/month downtime budget** | NFR-AVL-001 vs. NFR-AVL-009 | Align math: 99.5% ≈ 18 min/month at 60 business hours |
| C-02 | **2-hour RTO Must Have vs. geographic DR Should Have** | NFR-BDR-010 vs. NFR-BDR-014 | Define scenario-based RTOs |
| C-03 | **15-minute RPO Must Have vs. fixed budget** | NFR-BDR-001 vs. BC-01 | Cost-options analysis; business sign-off |
| C-04 | **7-year retention vs. 10-second/15-minute query performance** | NFR-COM-020, NFR-PERF-017, NFR-PERF-026 | Define tiered data architecture |
| C-05 | **GDPR erasure vs. 7-year audit retention** | NFR-SEC-031 vs. NFR-COM-020 | Legal decision matrix (referenced but not published) |
| C-06 | **Peak uptime 99.7% vs. zero days > 1 hr downtime** | NFR-AVL-003 | Reconcile daily vs. period metrics |

### 4.2 Significant Duplication (Consolidate for Test Efficiency)

| Topic | Duplicate IDs | Recommendation |
|-------|---------------|----------------|
| Immutable audit trail | NFR-REL-009, NFR-SEC-013, NFR-LOG-010, NFR-COM-010 | Single source: NFR-REL-009; others cross-reference |
| Authentication logging | NFR-SEC-025, NFR-LOG-014 | Cross-reference |
| Backup job monitoring | NFR-MON-020, NFR-BDR-021 | Cross-reference |
| Recovery validation | NFR-REL-005, NFR-BDR-016, NFR-BDR-023 | Single checklist document |
| 7-year retention | NFR-SEC-015, NFR-LOG-027, NFR-BDR-005/006, NFR-COM-019/020 | Unified retention schedule |

### 4.3 Missing NFR Domains (Recommend Adding)

| Proposed Domain | Rationale | Suggested Owner |
|-----------------|-----------|-----------------|
| **Integration & data exchange** | TEC-04, TEC-05 manual processes have no performance, reliability, or monitoring NFRs | Solution Architect |
| **Data quality & master data** | OC-04 catalog scale; no NFR for duplicate SKU prevention, identifier integrity | Inventory Controller / SA |
| **Usability & accessibility** | BC-02 no new headcount; warehouse adoption (KPI-22) depends on UX | Product Owner |
| **Environment governance** | No prod/non-prod separation, test data masking | Security Engineer |
| **Maintainability & release** | NFR-BDR-003 pre-release backup; no release frequency or rollback NFR | DevOps Engineer |
| **Unified NFR traceability matrix** | 204 requirements across 9 files | Solution Architect |

### 4.4 Dependencies on Unvalidated Artifacts

| Artifact | Referenced By | Status | Risk if Missing |
|----------|-------------|--------|-----------------|
| Primary Locations Register | NFR-AVL-005, NFR-MON-019, PA-01 | Not published | Cannot size or test |
| Essential Function Register | NFR-AVL, NFR-REL, NFR-MON, AA-05 | Not published | Availability testing blocked |
| Capacity Baseline Workbook | NFR-PERF, NFR-SCAL, SA-01 | Not validated | All numeric targets are assumptions |
| Peak Season Calendar | NFR-AVL-003, NFR-MON-004, TC-04 | Not published per discovery review | Peak NFRs untestable |
| Month-End Close Report Set | NFR-PERF-025, PA-04 | Not defined | Close performance untestable |
| Data Classification Register | NFR-SEC-017, NFR-LOG-009 | Not published | Security scope incomplete |
| Privacy vs. Audit Retention Matrix | NFR-SEC-031, NFR-COM-004 | Not published | Compliance conflict unresolved |

---

## 5. Risk Register

| Risk ID | Risk | Likelihood | Impact | Mitigation |
|---------|------|------------|--------|------------|
| RK-01 | Availability math conflict causes false pass/fail in acceptance testing | High | High | Resolve C-01 before test plan |
| RK-02 | 15-minute RPO unaffordable within BC-01 — silent descoping at implementation | Medium | High | Business decision on RPO tiers in architecture options |
| RK-03 | Warehouse password policy drives low adoption (KPI-22) | Medium | High | Phased policy; compensating controls |
| RK-04 | 7-year log/data retention exceeds storage budget | Medium | Medium | Tiered archival strategy in design |
| RK-05 | Location network outage counted as application outage — SLA disputes | Medium | Medium | NFR-MON-019 split reporting; SLA credit rules |
| RK-06 | No offline mode (TEC-03) + connectivity failure = fulfillment stop | Medium | High | Strengthen NFR-REL-013 continuity procedures; consider Phase 2 offline queue |
| RK-07 | Manual finance export (TEC-05) fails compliance expectations for BO-18/BO-20 | Medium | Medium | Document as interim control; Phase 2 integration roadmap |
| RK-08 | Scalability requirements without priority cause over-engineering or under-delivery | High | Medium | Add MoSCoW to NFR-SCAL |
| RK-09 | 204 Must/Should requirements create untestable UAT scope | High | Medium | MVP NFR subset for go-live gate |
| RK-10 | Regulated product handling (lot traceability) discovered post-design | Low | High | Product category assessment before design |

---

## 6. Unrealistic or Aggressive Expectations

| Requirement | Concern | Recommended Adjustment |
|-------------|---------|------------------------|
| NFR-AVL-001 + NFR-AVL-009 | Mathematically inconsistent | Fix downtime budget (see C-01) |
| NFR-BDR-001 (15-min RPO) | Premium infrastructure cost for mid-sized distributor | Offer tiered RPO: 15 min Tier 1 data, 1 hr acceptable with business sign-off |
| NFR-BDR-010 (2-hr RTO all disasters) | Site-loss disaster needs DR site | Scenario-based RTO: 2 hr app recovery; 8–24 hr site disaster |
| NFR-SEC-010/011 (password policy) | Warehouse shared-terminal friction | Role-differentiated policy |
| NFR-PERF-026 (15-min full audit extract) | Grows with catalog and history | Tier by data age: online 15 min; archive 4 hr acceptable |
| NFR-REL-010 (zero double-allocation) | Unmeasurable at low volume | "Zero confirmed in audit sample of N transactions" |
| NFR-SCAL-019 (cost ratio) | Not a system requirement | Move to business KPI |
| NFR-MON-004 (30-sec checks peak) | Monitoring load | 60-sec peak with business approval |
| 99.7% peak uptime + zero >1hr days | Inconsistent | Single peak metric: 99.5% with max 30 min/day |

---

## 7. Ambiguities Requiring Clarification

| # | Ambiguity | Owner | Decision Needed By |
|---|-----------|-------|-------------------|
| A-01 | Definition of "essential functions" | Product Owner + Operations Director | Before UAT |
| A-02 | Definition of "routine screens" and "standard reports" | Product Owner | Before UAT |
| A-03 | MoSCoW priority for all scalability requirements | Product Owner | Before architecture |
| A-04 | Online vs. archived data for performance and retention | Solution Architect + Legal | Before data design |
| A-05 | Application outage vs. location network outage in SLA | DevOps + Operations Director | Before go-live |
| A-06 | MVP-monitorable KPI subset | Product Owner + Finance | Before MVP gate |
| A-07 | GDPR applicability and jurisdictions | Legal | Before compliance design |
| A-08 | Lot traceability trigger (NFR-COM-018) | Inventory Controller + Legal | Before catalog design |
| A-09 | Peak season dates per location | Operations Director | Before rollout calendar |
| A-10 | Acknowledgment vs. response for alerts | DevOps + Operations support | Before runbook |

---

## 8. Recommendations Before System Design

### 8.1 Immediate Actions (Gate Blockers)

1. **Resolve availability math conflict (C-01)** — update NFR-AVL-009 or NFR-AVL-001 so uptime percentage and downtime budget are consistent  
2. **Publish Essential Function Register** — stock lookup, transaction types, reservations, approvals, notifications (in/out of essential scope)  
3. **Complete Capacity Baseline Workbook** — replace all planning assumptions with validated numbers per location  
4. **Legal sign-off on retention and privacy matrix (C-05)** — reconcile 7-year audit hold vs. GDPR erasure  
5. **Business decision on RPO tiers (C-03)** — 15-minute vs. alternative with cost trade-off documented  

### 8.2 Short-Term Actions (During Architecture Phase)

6. **Add MoSCoW priority to NFR-SCAL requirements**  
7. **Define tiered data architecture** — hot/warm/cold aligning NFR-PERF, NFR-SCAL-015, NFR-COM, NFR-BDR  
8. **Create MVP NFR Test Subset** — ~40 Must Have requirements testable at first go-live (see Section 8.4)  
9. **Add missing NFR domains** — integration exchange, environment governance, data quality (minimum)  
10. **Consolidate duplicate audit trail requirements** into single authoritative requirement with cross-refs  
11. **Define scenario-based RTO/RPO** — application failure, data corruption, site disaster (resolve C-02)  
12. **Role-differentiated security policy** for warehouse vs. administrative users  

### 8.3 Design Phase Deliverables (Derived from NFRs)

| Deliverable | Source NFRs | Owner |
|-------------|-------------|-------|
| Capacity Model | NFR-PERF, NFR-SCAL | Solution Architect |
| Availability & DR Target Architecture | NFR-AVL, NFR-REL, NFR-BDR | Solution Architect + DevOps |
| Security Control Matrix | NFR-SEC, NFR-COM | Security Engineer |
| Logging & Retention Architecture | NFR-LOG, NFR-COM-019/020 | Solution Architect |
| Monitoring & Alerting Runbooks | NFR-MON | DevOps Engineer |
| Compliance Control Mapping (COSO) | NFR-COM | Internal Audit + Security |
| NFR Traceability Matrix (all 204) | All documents | Solution Architect |

### 8.4 Proposed MVP NFR Test Subset (First Go-Live)

The following **Must Have** requirements form the minimum acceptance gate for first location go-live:

| Domain | MVP Gate Requirements |
|--------|----------------------|
| **Performance** | NFR-PERF-001, 002, 003, 007, 011, 012, 019, 020 |
| **Availability** | NFR-AVL-001, 005, 008, 011 |
| **Reliability** | NFR-REL-001, 003, 006, 007, 008, 009, 013 |
| **Security** | NFR-SEC-001, 002, 003, 005, 006, 007, 010, 013, 021, 024, 025, 029 |
| **Logging** | NFR-LOG-001, 002, 007, 010, 013, 018, 026 |
| **Monitoring** | NFR-MON-001, 002, 013, 021, 022, 023 |
| **Backup** | NFR-BDR-001, 002, 009, 010, 021, 022 |
| **Compliance** | NFR-COM-001, 006, 008, 009, 010, 011, 014, 015, 019 |

*Remaining Should Have and Could Have NFRs are validated at subsequent location rollouts or phase gates.*

---

## 9. Overall Conclusion

The non-functional requirements suite provides a **solid foundation** for system design. Requirements are business-justified, measurable in most cases, and well-aligned with the initiative's KPIs and constraints.

**Proceed to system design** once the six gate blockers in Section 8.1 are resolved and the MVP NFR Test Subset is agreed with QA and the Product Owner. Without resolving the **availability math conflict (C-01)**, **RPO cost decision (C-03)**, and **unvalidated baselines**, architecture sizing and acceptance testing will be built on inconsistent assumptions — creating rework risk during UAT and go-live.

The highest-value pre-design activities are:

1. Fix numeric conflicts  
2. Validate baselines  
3. Publish missing registers  
4. Define data tiering for retention vs. performance  
5. Right-size MVP test scope  

---

## 10. Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-07-03 | Senior Solution Architect | Initial consolidated NFR review |

---

## Appendix A: NFR Document Index

| Document | Path |
|----------|------|
| Performance Requirements | `Non-functional Requirements/performance-requirements.md` |
| Scalability Requirements | `Non-functional Requirements/scalability-requirements.md` |
| Availability & Reliability Requirements | `Non-functional Requirements/availability-reliability-requirements.md` |
| Security Requirements | `Non-functional Requirements/security-requirements.md` |
| Logging Requirements | `Non-functional Requirements/logging-requirements.md` |
| Monitoring Requirements | `Non-functional Requirements/monitoring-requirements.md` |
| Backup & Disaster Recovery Requirements | `Non-functional Requirements/backup-disaster-recovery-requirements.md` |
| Compliance Requirements | `Non-functional Requirements/compliance-requirements.md` |

---

*This review analyzes business-level NFRs only. System design, technology selection, and implementation estimates are explicitly out of scope and should address the findings herein.*
