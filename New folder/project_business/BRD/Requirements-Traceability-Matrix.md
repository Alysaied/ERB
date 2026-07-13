# Requirements Traceability Matrix (RTM)
## Inventory Management System

---

## Document Information

| Attribute | Detail |
|-----------|--------|
| **Document ID** | RTM-IMS-001 |
| **Version** | 1.0 |
| **Status** | For Stakeholder Review |
| **Document Owner** | Senior Business Analyst |
| **Date** | July 3, 2026 |
| **Based On** | BRD-IMS-001, Functional Requirements (FR-001–FR-090), User Stories (US-001–US-090), Acceptance Criteria, SMART Business Objectives (BO-01–BO-24), Business Processes (BP-01–BP-32), User Roles (UR-01–UR-19) |

### Traceability Convention

| Identifier | Layer |
|------------|-------|
| BO-xx | Business Objective (SMART) |
| BP-xx | Business Process |
| FR-xxx | Functional Requirement |
| US-xxx | User Story (1:1 with FR) |
| AC-xxx-* | Acceptance Criteria (4 categories per story: H, V, E, X) |
| UR-xx | User Role |

**Trace direction:** BO → BP → FR → US → AC ← UR (role executes story)

---

## 1. Executive Summary

### Traceability Health Dashboard

| Traceability Link | Source Count | Target Count | Coverage | Status |
|-------------------|-------------|--------------|----------|--------|
| FR → US | 90 | 90 | **100%** | Complete (1:1) |
| US → AC | 90 | 90 story sections (~360 criteria) | **100%** | Complete |
| FR → BP | 90 | 32 processes | **100%** | All BPs referenced by ≥1 FR |
| FR → BO (explicit in FR doc) | 90 | 24 objectives | **29%** | **Gap — only 7 BOs explicitly cited** |
| FR → BO (derived/analyst mapping) | 90 | 24 objectives | **96%** | 23/24 BOs mapped (see Section 4) |
| US → UR (formal catalog) | 90 | 19 roles | **94%** | System Administrator not in UR catalog |
| BO → AC (direct) | 24 | — | **0%** | No KPI thresholds in AC (indirect via FR only) |
| BP → BO (direct) | 32 | 24 | **Partial** | Not documented in source artifacts |

### Overall Assessment

| Dimension | Rating | Summary |
|-----------|--------|---------|
| **Vertical traceability (FR→US→AC)** | Strong | Complete 1:1:1 chain; every FR has testable acceptance criteria |
| **Horizontal traceability (BO→BP→FR)** | Moderate | BP coverage complete; BO linkage mostly implicit, not authored in FR text |
| **Role traceability (UR→US→FR)** | Moderate | Story roles defined; 3 stories use roles outside UR catalog |
| **Release traceability (MoSCoW vs Phase)** | Weak | 4 FR conflicts between phase tags and MoSCoW priority |
| **Gap remediation readiness** | Conditional | 10 orphan/deferred items and 8 duplicate pairs require errata before sprint 1 |

---

## 2. Gap Analysis

### 2.1 Missing Traceability

| Gap ID | Missing Link | Detail | Severity | Recommendation |
|--------|--------------|--------|----------|----------------|
| MT-01 | **BO → FR (explicit)** | Only BO-01, BO-03, BO-04, BO-05, BO-06, BO-07 appear in FR Business Value fields; BO-08–BO-24 lack explicit FR citations | High | Add BO reference column to all FR records; update RTM as living document |
| MT-02 | **BO → AC (KPI thresholds)** | SMART targets (e.g., ≥95% accuracy, ≥92% fill rate) absent from acceptance criteria | High | Add Acceptance Test Plan appendix linking BO/KPI to E2E scenarios |
| MT-03 | **BO → BP (direct matrix)** | No authored BO-to-process mapping in discovery artifacts | Medium | Add BO-BP matrix to BRD Appendix |
| MT-04 | **BP → US (direct)** | Traceability passes through FR only; no BP column on user stories | Low | Acceptable if FR→BP maintained; optional BP tag on US |
| MT-05 | **UR → PERM (permissions)** | RBAC matrix exists separately; not linked in RTM | Medium | Cross-reference UR-xx to PERM groups in permissions artifacts |
| MT-06 | **External system boundary** | Order intake, finance sync, channel feeds have no FR/US/AC | High | Add integration boundary FR (order data contract, export format) |
| MT-07 | **NFR → BO/FR** | 204 NFRs not traced to business objectives in RTM | Medium | Add NFR traceability matrix in separate artifact |
| MT-08 | **E2E scenario → multi-US** | No golden-path AC spanning receive→ATP→reserve→pick | Medium | Create E2E scenario catalog referencing US-015, US-018, US-024, US-042, US-044 |

### 2.2 Orphan Requirements

*Orphans are requirements with no upstream business justification, no downstream test artifact, or no committed release slot.*

| Orphan ID | Requirement | Orphan Type | Explanation |
|-----------|-------------|-------------|-------------|
| OR-01 | **FR-057, US-057, AC-057** | Release orphan | MoSCoW = Won't Have (current release) but fully specified with AC — risks wasted build/test effort |
| OR-02 | **FR-062, US-062, AC-062** | Release orphan | MoSCoW = Won't Have; network rebalancing deferred but backlog-ready |
| OR-03 | **FR-080, US-080, AC-080** | Release orphan | MoSCoW = Won't Have; tied to deferred FR-057 |
| OR-04 | **FR-050, US-050, AC-050** | Dependency orphan | Could Have / Phase 3; depends on undefined substitute master (no FR for alternate SKU relationships) |
| OR-05 | **FR-022, US-022, AC-022** | Data orphan | Phase 3 supplier performance; no supplier master entity (FR-013 references supplier without maintenance FR) |
| OR-06 | **US-081, US-082, US-085** | Role orphan | Stories assign **System Administrator** — not in UR-01–UR-19 business role catalog |
| OR-07 | **BO-22** | Objective orphan | "Retire parallel manual tools" is organizational; no FR directly validates retirement — only enables replacement |
| OR-08 | **BO-21** | Objective orphan | "90% user adoption" measured operationally; no FR defines adoption tracking (monitoring NFR only) |
| OR-09 | **Integration stories** | Story orphan | No US for external order system, finance export consumer, or supplier actor (A-20) |
| OR-10 | **BP-05, BP-06 (MVP window)** | Process orphan at MVP | Purchase order placement and inbound planning have no MVP FR (FR-013/014 are Phase 2) — process partially manual at go-live |

### 2.3 Duplicate Requirements

*Duplicates are overlapping requirements that may cause double-build, conflicting behavior, or redundant test effort.*

| Dup ID | Requirements | Relationship | Risk | Resolution |
|--------|-------------|--------------|------|------------|
| DUP-01 | **FR-019 ↔ FR-065** | Same business capability (return receipt) at MVP vs Phase 2 | Double implementation | FR-019 = MVP interim; FR-065 supersedes when F-21 ships |
| DUP-02 | **FR-057 ↔ FR-080** | Readiness review vs readiness alert — same evaluation | Redundant logic | Merge or make FR-080 notification wrapper on FR-057 |
| DUP-03 | **FR-016 ↔ FR-020** | Receipt discrepancy vs tolerance evaluation | Overlapping variance handling | FR-020 = automated pre-check; FR-016 = human resolution workflow |
| DUP-04 | **FR-029 ↔ FR-015/044/035/060** | Umbrella movement history vs process-specific movements | Misread as separate feature | Reframe FR-029 as cross-cutting quality attribute |
| DUP-05 | **FR-039 ↔ FR-040 ↔ FR-070** | Shrinkage, obsolescence, overstock analytics | Reporting overlap | FR-039 = loss by reason; FR-040 = aging; FR-070 = threshold breach |
| DUP-06 | **FR-074** | Listed in features F-20 and F-22 | Planning duplication | Single owner: F-20 Reports; F-22 consumes output |
| DUP-07 | **F-26 ↔ domain notification FRs** | FR-076–080 in F-26 plus domain features | Sprint double-count | F-26 = capability layer, not separate increment |
| DUP-08 | **US-019 ↔ US-065 AC** | Nearly identical acceptance criteria for return receipt paths | Redundant test cases | Tag MVP vs Phase 2 cutover in AC |

### 2.4 Uncovered Business Objectives

| BO ID | Objective (Short) | Priority | FR Coverage | Coverage Level | Gap Notes |
|-------|-------------------|----------|-------------|----------------|----------|
| BO-01 | Single trusted inventory view | P1 | FR-023, FR-024, FR-027, FR-068 | **Strong** | Explicit in FR doc |
| BO-02 | Inventory record accuracy ≥95% | P1 | FR-030–FR-034, FR-031, FR-071 | **Strong** | Explicit in FR doc |
| BO-03 | 100% standardized movement recording | P1 | FR-029, FR-015, FR-044, FR-060, FR-035 | **Strong** | Explicit in FR doc |
| BO-04 | 60% reduction in manual reconciliation | P2 | FR-023–FR-027, FR-068, FR-069 | **Moderate** | Explicit in FR doc; no KPI in AC |
| BO-05 | Order fill rate ≥92% | P2 | FR-041–FR-045, FR-047 | **Strong** | Explicit in FR doc |
| BO-06 | 30% faster fulfillment cycle time | P2 | FR-044, FR-049 | **Moderate** | Explicit in FR doc; no cycle-time AC |
| BO-07 | 50% fewer priority SKU stockouts | P2 | FR-051, FR-008, FR-070 | **Moderate** | Explicit in FR doc (note: FR-075 cites BO-07 erroneously — should be BO-18) |
| BO-08 | 40% fewer stock-related cancellations | P2 | FR-041, FR-024, FR-045 | **Moderate** | Derived mapping only; no explicit FR citation |
| BO-09 | 20% reduction in excess inventory | P3 | FR-070, FR-040, FR-053 | **Moderate** | Phase 2/3 FRs; weak at MVP |
| BO-10 | 15% inventory turnover improvement | P3 | FR-073, FR-075, FR-040 | **Weak** | Depends on Phase 3 FR-073; finance data external |
| BO-11 | 25% reduction in write-offs/shrinkage | P2 | FR-035, FR-036, FR-039, FR-011 | **Strong** | Derived mapping |
| BO-12 | 30% reduction in emergency procurement | P2 | FR-051, FR-053, FR-054 | **Moderate** | Phase 2 replenishment FRs |
| BO-13 | 90% replenishment within 2 days | P2 | FR-051, FR-052, FR-054, FR-076 | **Moderate** | Phase 2 FR-054; alert only at MVP |
| BO-14 | 40% fewer cross-location imbalances | P2 | FR-058–FR-063, FR-028, FR-070 | **Moderate** | FR-062 Won't Have weakens automation |
| BO-15 | 90% on-time delivery rate | P2 | FR-044, FR-049, FR-041 | **Moderate** | Delivery tracking partially manual (TEC-04) |
| BO-16 | 90% sales self-service availability | P1 | FR-024, FR-027, FR-023 | **Strong** | Derived; supports P1 objective |
| BO-17 | 40% faster CS resolution | P2 | FR-049, FR-024, FR-025 | **Moderate** | Derived mapping |
| BO-18 | ≤2% valuation variance | P3 | FR-075, FR-089 | **Moderate** | Phase 2; manual finance bridge at MVP |
| BO-19 | 100% audit trail coverage | P1 | FR-086, FR-083, FR-011, FR-029, FR-035 | **Strong** | Derived mapping |
| BO-20 | Month-end close ≤3 days | P3 | FR-089, FR-075, FR-071 | **Moderate** | Phase 2 finance reconciliation |
| BO-21 | 90% active user adoption | P1 | FR-081–FR-085 (enablers) | **Weak** | No FR measures adoption; organizational metric |
| BO-22 | Zero parallel manual tracking tools | P1 | — (no direct FR) | **Uncovered** | Change management objective; system enables but does not enforce retirement |
| BO-23 | Management growth confidence ≥4.0 | P3 | FR-068, FR-073 | **Weak** | Primarily survey-based; FR-073 Phase 3 |
| BO-24 | 95% promotional launch readiness | P3 | FR-057, FR-080 | **Uncovered (current release)** | Both FRs = Won't Have; objective not achievable in committed scope |

**Summary:** 2 objectives uncovered or weak for current release (**BO-22**, **BO-24**); 1 objective with no direct FR (**BO-22**); 17 objectives rely on derived (implicit) FR mapping not authored in source documents.

---

## 3. Business Objective Traceability Matrix

*Primary FR paths supporting each business objective. Full FR detail in Section 5.*

| BO ID | Objective | Priority | Primary BP(s) | Primary FR(s) | Primary US | AC Range | Primary UR |
|-------|-----------|----------|---------------|---------------|------------|----------|------------|
| BO-01 | Single trusted inventory view | P1 | BP-10 | FR-023, FR-024, FR-027, FR-068 | US-023, US-024, US-027, US-068 | AC-023–AC-068 | UR-04, UR-05, UR-12 |
| BO-02 | Inventory accuracy ≥95% | P1 | BP-11, BP-13 | FR-030–FR-034, FR-071 | US-030–US-034, US-071 | AC-030–AC-071 | UR-05, UR-06, UR-09 |
| BO-03 | Standardized movement recording | P1 | BP-07, BP-18, BP-25 | FR-029, FR-015, FR-044, FR-060 | US-029, US-015, US-044, US-060 | AC-029, AC-015, AC-044, AC-060 | UR-07, UR-08, UR-06 |
| BO-04 | Reduce manual reconciliation 60% | P2 | BP-10, BP-29 | FR-023–FR-027, FR-069 | US-023–US-027, US-069 | AC-023–AC-069 | UR-04, UR-05, UR-17 |
| BO-05 | Order fill rate ≥92% | P2 | BP-16–BP-19 | FR-041–FR-045 | US-041–US-045 | AC-041–AC-045 | UR-12, UR-04, UR-08 |
| BO-06 | Fulfillment cycle time −30% | P2 | BP-18 | FR-044, FR-049 | US-044, US-049 | AC-044, AC-049 | UR-08, UR-13 |
| BO-07 | Priority SKU stockouts −50% | P2 | BP-21, BP-03 | FR-051, FR-008, FR-070 | US-051, US-008, US-070 | AC-051, AC-008, AC-070 | UR-05, UR-15 |
| BO-08 | Stock cancellations −40% | P2 | BP-16, BP-19 | FR-041, FR-024, FR-045 | US-041, US-024, US-045 | AC-041, AC-024, AC-045 | UR-12, UR-13 |
| BO-09 | Excess inventory −20% | P3 | BP-26, BP-29 | FR-070, FR-040, FR-053 | US-070, US-040, US-053 | AC-070, AC-040, AC-053 | UR-15, UR-03 |
| BO-10 | Turnover +15% | P3 | BP-29, BP-30 | FR-073, FR-075 | US-073, US-075 | AC-073, AC-075 | UR-03, UR-17 |
| BO-11 | Write-offs/shrinkage −25% | P2 | BP-14, BP-15 | FR-035, FR-036, FR-039, FR-011 | US-035, US-036, US-039, US-011 | AC-035, AC-036, AC-039, AC-011 | UR-06, UR-05 |
| BO-12 | Emergency procurement −30% | P2 | BP-21, BP-22 | FR-051, FR-053, FR-054 | US-051, US-053, US-054 | AC-051, AC-053, AC-054 | UR-15, UR-16 |
| BO-13 | Replenishment within 2 days | P2 | BP-21, BP-22 | FR-051, FR-052, FR-054, FR-076 | US-051, US-052, US-054, US-076 | AC-051, AC-052, AC-054, AC-076 | UR-15, UR-16 |
| BO-14 | Cross-location imbalance −40% | P2 | BP-24–BP-26 | FR-058–FR-063, FR-028 | US-058–US-063, US-028 | AC-058–AC-063, AC-028 | UR-04, UR-10 |
| BO-15 | On-time delivery ≥90% | P2 | BP-18 | FR-044, FR-049, FR-041 | US-044, US-049, US-041 | AC-044, AC-049, AC-041 | UR-08, UR-13 |
| BO-16 | Sales self-service availability | P1 | BP-16 | FR-024, FR-027 | US-024, US-027 | AC-024, AC-027 | UR-12, UR-11 |
| BO-17 | CS handle time −40% | P2 | BP-16, BP-18 | FR-049, FR-024, FR-025 | US-049, US-024, US-025 | AC-049, AC-024, AC-025 | UR-13 |
| BO-18 | Valuation variance ≤2% | P3 | BP-30 | FR-075, FR-089 | US-075, US-089 | AC-075, AC-089 | UR-17, UR-03 |
| BO-19 | 100% audit trail | P1 | BP-32 | FR-086, FR-083, FR-011, FR-029 | US-086, US-083, US-011, US-029 | AC-086, AC-083, AC-011, AC-029 | UR-18, UR-05 |
| BO-20 | Month-end close ≤3 days | P3 | BP-30 | FR-089, FR-075, FR-071 | US-089, US-075, US-071 | AC-089, AC-075, AC-071 | UR-17 |
| BO-21 | 90% user adoption | P1 | All BPs | FR-081–FR-085 | US-081–US-085 | AC-081–AC-085 | All UR |
| BO-22 | Zero parallel manual tools | P1 | All BPs | *(No direct FR)* | *(Indirect via all US)* | *(No AC)* | All UR |
| BO-23 | Growth confidence ≥4.0 | P3 | BP-29 | FR-068, FR-073 | US-068, US-073 | AC-068, AC-073 | UR-01, UR-02 |
| BO-24 | Promotional readiness 95% | P3 | BP-31 | FR-057, FR-080 *(Won't Have)* | US-057, US-080 | AC-057, AC-080 | UR-14 |

---

## 4. Business Process Coverage Matrix

| BP ID | Process Name | Supporting FR(s) | MVP FR? | US | BO(s) Supported | Coverage |
|-------|--------------|------------------|---------|-----|-----------------|----------|
| BP-01 | Product Master Data Management | FR-001–FR-004, FR-040, FR-090 | Yes | US-001–004, US-040, US-090 | BO-01, BO-02, BO-03 | Full |
| BP-02 | Location & Warehouse Setup | FR-005–FR-007, FR-010, FR-082, FR-090 | Yes | US-005–007, US-010, US-082, US-090 | BO-01, BO-23 | Full |
| BP-03 | Stock Policy & Threshold Definition | FR-008, FR-012, FR-056, FR-070 | Yes | US-008, US-012, US-056 | BO-07, BO-13 | Full |
| BP-04 | ABC Product Classification | FR-009 | Phase 2 | US-009 | BO-07 | Full |
| BP-05 | Purchase Order Placement | FR-013, FR-021, FR-054 | **Phase 2 only** | US-013, US-021, US-054 | BO-12, BO-13 | **Partial at MVP** |
| BP-06 | Inbound Shipment Planning | FR-014 | Phase 2 | US-014 | BO-13 | Partial at MVP |
| BP-07 | Goods Receipt & Verification | FR-015–FR-017, FR-019–FR-020 | Yes | US-015–017, US-019–020 | BO-03, BO-11 | Full |
| BP-08 | Receipt Discrepancy Resolution | FR-016, FR-020, FR-022 | Yes/Ph2/Ph3 | US-016, US-020, US-022 | BO-11 | Full |
| BP-09 | Stock Put-Away & Storage | FR-018 | Yes | US-018 | BO-03, BO-05 | Full |
| BP-10 | Inventory Status Monitoring | FR-023–FR-029 | Yes | US-023–029 | BO-01, BO-04, BO-16 | Full |
| BP-11 | Cycle Counting | FR-030, FR-031, FR-071 | Yes | US-030, US-031, US-071 | BO-02 | Full |
| BP-12 | Full Physical Inventory Count | FR-032, FR-010 | Yes | US-032, US-010 | BO-02 | Full |
| BP-13 | Count Variance Investigation | FR-033, FR-034, FR-071, FR-077 | Yes | US-033, US-034, US-071, US-077 | BO-02, BO-19 | Full |
| BP-14 | Stock Adjustment & Write-Off | FR-035–FR-038, FR-011, FR-077 | Yes | US-035–038, US-011, US-077 | BO-11, BO-19 | Full |
| BP-15 | Shrinkage & Loss Management | FR-036, FR-039 | Yes/Ph2 | US-036, US-039 | BO-11 | Full |
| BP-16 | Order Availability Confirmation | FR-024, FR-041, FR-048 | Yes | US-024, US-041, US-048 | BO-05, BO-08, BO-16 | Full |
| BP-17 | Inventory Reservation | FR-025, FR-042, FR-043, FR-046 | Yes/Ph2 | US-025, US-042, US-043, US-046 | BO-05, BO-08 | Full |
| BP-18 | Pick, Pack & Ship | FR-044, FR-049 | Yes | US-044, US-049 | BO-05, BO-06, BO-15 | Full |
| BP-19 | Partial Fulfillment & Backorder | FR-045, FR-046 | Yes/Ph2 | US-045, US-046 | BO-05, BO-08 | Full |
| BP-20 | Outbound Exception Handling | FR-047, FR-050, FR-078 | Yes/Ph3 | US-047, US-050, US-078 | BO-05 | Full |
| BP-21 | Low-Stock Alert Review | FR-051, FR-052, FR-070, FR-076 | Yes | US-051, US-052, US-070, US-076 | BO-07, BO-12, BO-13 | Full |
| BP-22 | Replenishment Planning | FR-053, FR-054, FR-074 | Ph2 | US-053, US-054, US-074 | BO-12, BO-13 | Partial at MVP |
| BP-23 | Inbound Supply Tracking | FR-013, FR-014, FR-021, FR-022, FR-028, FR-055, FR-079 | Ph2/Ph3 | US-013, US-014, US-021, US-022, US-028, US-055, US-079 | BO-13 | Partial at MVP |
| BP-24 | Inter-Location Transfer Request | FR-058, FR-059, FR-063, FR-077 | Yes/Ph2 | US-058, US-059, US-063, US-077 | BO-14 | Full |
| BP-25 | Inter-Location Transfer Execution | FR-060, FR-061, FR-078 | Yes/Ph2 | US-060, US-061, US-078 | BO-03, BO-14 | Full |
| BP-26 | Network Stock Rebalancing | FR-028, FR-062, FR-070 | Ph2/Ph3/WNH | US-028, US-062, US-070 | BO-09, BO-14 | Partial (FR-062 deferred) |
| BP-27 | Customer Return Intake | FR-064, FR-067 | Yes/Ph2 | US-064, US-067 | BO-03 | Full |
| BP-28 | Return-to-Stock or Disposal | FR-019, FR-065, FR-066 | Yes/Ph2 | US-019, US-065, US-066 | BO-03, BO-11 | Full (see DUP-01) |
| BP-29 | Inventory Performance Reporting | FR-068–FR-073, FR-040 | Yes/Ph3 | US-068–US-073, US-040 | BO-01, BO-04, BO-09, BO-23 | Full |
| BP-30 | Inventory Valuation & Reconciliation | FR-075, FR-089 | Phase 2 | US-075, US-089 | BO-10, BO-18, BO-20 | Partial at MVP |
| BP-31 | Promotional Stock Readiness | FR-057, FR-080 | **Won't Have** | US-057, US-080 | BO-24 | **Deferred** |
| BP-32 | Inventory Audit & Control Review | FR-081–FR-088, FR-086 | Yes/Ph2 | US-081–US-088, US-086 | BO-19, BO-21 | Full |

**WNH** = Won't Have (current release)

---

## 5. Full Requirements Traceability Matrix

*One row per functional requirement. AC format: `AC-{US}-[H|V|E|X]n` (typically 10 criteria per story across 4 categories).*

### Domain 1: Master Data & Governance

| FR | Requirement (Short) | Phase | BP | BO | US | Role (Story) | UR | AC IDs | MoSCoW |
|----|---------------------|-------|-----|-----|-----|--------------|-----|--------|--------|
| FR-001 | Create/maintain product master | MVP | BP-01 | BO-01, BO-02 | US-001 | Inventory Controller | UR-05 | AC-001-H1…X2 | Must |
| FR-002 | Product status lifecycle | MVP | BP-01 | BO-02 | US-002 | Inventory Controller | UR-05 | AC-002-H1…X2 | Must |
| FR-003 | Product identifier lookup | MVP | BP-01,07,11,18 | BO-03 | US-003 | Warehouse Operator | UR-07/08 | AC-003-H1…X2 | Must |
| FR-004 | Detect duplicate products | MVP | BP-01 | BO-01 | US-004 | Inventory Controller | UR-05 | AC-004-H1…X2 | Must |
| FR-005 | Configure locations | MVP | BP-02 | BO-01, BO-23 | US-005 | Operations Director | UR-04 | AC-005-H1…X2 | Must |
| FR-006 | Location hierarchy | MVP | BP-02 | BO-01 | US-006 | Operations Director | UR-04 | AC-006-H1…X2 | Must |
| FR-007 | Location closure/disposition | Ph2 | BP-02 | BO-23 | US-007 | Operations Director | UR-04 | AC-007-H1…X2 | Should |
| FR-008 | Stock policy/thresholds | MVP | BP-03 | BO-07, BO-13 | US-008 | Inventory Controller | UR-05 | AC-008-H1…X2 | Must |
| FR-009 | ABC classification | Ph2 | BP-04 | BO-07 | US-009 | Inventory Controller | UR-05 | AC-009-H1…X2 | Should |
| FR-010 | Opening stock balance | MVP | BP-02,12 | BO-02 | US-010 | Inventory Controller | UR-05 | AC-010-H1…X2 | Must |
| FR-011 | Standard reason codes | MVP | BP-14,08,13 | BO-11, BO-19 | US-011 | Inventory Controller | UR-05 | AC-011-H1…X2 | Must |
| FR-012 | Governance policies | Ph2 | BP-03,32 | BO-19 | US-012 | Operations Director | UR-04 | AC-012-H1…X2 | Should |

### Domain 2: Inbound & Receiving

| FR | Requirement (Short) | Phase | BP | BO | US | Role (Story) | UR | AC IDs | MoSCoW |
|----|---------------------|-------|-----|-----|-----|--------------|-----|--------|--------|
| FR-013 | Record purchase orders | Ph2 | BP-05,23 | BO-12, BO-13 | US-013 | Buyer | UR-16 | AC-013-H1…X2 | Should |
| FR-014 | Expected inbound deliveries | Ph2 | BP-06,23 | BO-13 | US-014 | Warehouse Manager | UR-06 | AC-014-H1…X2 | Should |
| FR-015 | Receive/verify inbound goods | MVP | BP-07 | BO-03 | US-015 | Receiving Clerk | UR-07 | AC-015-H1…X2 | Must |
| FR-016 | Receipt discrepancy resolution | MVP | BP-08 | BO-11 | US-016 | Receiving Clerk | UR-07 | AC-016-H1…X2 | Must |
| FR-017 | Enforce PO reference | MVP | BP-07,05 | BO-11 | US-017 | Receiving Clerk | UR-07 | AC-017-H1…X2 | Must |
| FR-018 | Put-away/availability timing | MVP | BP-09 | BO-03, BO-05 | US-018 | Warehouse Staff | UR-09 | AC-018-H1…X2 | Must |
| FR-019 | Return/non-PO inbound *(interim)* | MVP | BP-07,28 | BO-03 | US-019 | Receiving Clerk | UR-07 | AC-019-H1…X2 | Must |
| FR-020 | Receipt tolerance evaluation | Ph2 | BP-07,08 | BO-11 | US-020 | Receiving Clerk | UR-07 | AC-020-H1…X2 | Should |
| FR-021 | Cancel/amend open POs | Ph2 | BP-05,23 | BO-12 | US-021 | Buyer | UR-16 | AC-021-H1…X2 | Should |
| FR-022 | Supplier delivery performance | Ph3 | BP-08,23 | BO-12 | US-022 | Purchasing Manager | UR-15 | AC-022-H1…X2 | Could |

### Domain 3: Inventory Visibility & Status

| FR | Requirement (Short) | Phase | BP | BO | US | Role (Story) | UR | AC IDs | MoSCoW |
|----|---------------------|-------|-----|-----|-----|--------------|-----|--------|--------|
| FR-023 | On-hand quantity display | MVP | BP-10 | BO-01, BO-04, BO-16 | US-023 | Operations Manager | UR-04 | AC-023-H1…X2 | Must |
| FR-024 | ATP quantity display | MVP | BP-10,16 | BO-01, BO-08, BO-16 | US-024 | Sales Representative | UR-12 | AC-024-H1…X2 | Must |
| FR-025 | Reserved/committed stock | MVP | BP-10,17 | BO-05, BO-17 | US-025 | Customer Service Rep | UR-13 | AC-025-H1…X2 | Must |
| FR-026 | Stock status indicators | MVP | BP-10,21 | BO-07 | US-026 | Operations Manager | UR-04 | AC-026-H1…X2 | Must |
| FR-027 | Search/filter inventory | MVP | BP-10 | BO-01, BO-04, BO-16 | US-027 | Sales Representative | UR-12 | AC-027-H1…X2 | Must |
| FR-028 | Inbound/network availability | Ph2 | BP-10,23,26 | BO-14 | US-028 | Purchasing Manager | UR-15 | AC-028-H1…X2 | Should |

### Domain 4: Inventory Control & Accuracy

| FR | Requirement (Short) | Phase | BP | BO | US | Role (Story) | UR | AC IDs | MoSCoW |
|----|---------------------|-------|-----|-----|-----|--------------|-----|--------|--------|
| FR-029 | Movement history *(cross-cut)* | MVP | BP-10,+ | BO-03, BO-19 | US-029 | Inventory Controller | UR-05 | AC-029-H1…X2 | Must |
| FR-030 | Schedule cycle counts | MVP | BP-11 | BO-02 | US-030 | Inventory Controller | UR-05 | AC-030-H1…X2 | Must |
| FR-031 | Blind cycle counts | MVP | BP-11 | BO-02 | US-031 | Warehouse Staff | UR-09 | AC-031-H1…X2 | Must |
| FR-032 | Full physical count | MVP | BP-12 | BO-02 | US-032 | Inventory Controller | UR-05 | AC-032-H1…X2 | Must |
| FR-033 | Count variance identification | MVP | BP-13 | BO-02 | US-033 | Inventory Controller | UR-05 | AC-033-H1…X2 | Must |
| FR-034 | Approve count adjustments | MVP | BP-13 | BO-02, BO-19 | US-034 | Warehouse Manager | UR-06 | AC-034-H1…X2 | Must |
| FR-035 | Adjustments + reason codes | MVP | BP-14 | BO-11, BO-19 | US-035 | Warehouse Manager | UR-06 | AC-035-H1…X2 | Must |
| FR-036 | Write-offs with authorization | MVP | BP-14,15 | BO-11 | US-036 | Warehouse Manager | UR-06 | AC-036-H1…X2 | Must |
| FR-037 | Adjustment approval thresholds | MVP | BP-14,13 | BO-19 | US-037 | Operations Director | UR-04 | AC-037-H1…X2 | Must |
| FR-038 | Quarantine/hold stock | MVP | BP-14,28 | BO-05 | US-038 | Warehouse Manager | UR-06 | AC-038-H1…X2 | Must |
| FR-039 | Shrinkage/loss trends | Ph2 | BP-15 | BO-11 | US-039 | Inventory Controller | UR-05 | AC-039-H1…X2 | Should |
| FR-040 | Obsolete/slow-moving review | Ph2 | BP-01,14,29 | BO-09, BO-10 | US-040 | Purchasing Manager | UR-15 | AC-040-H1…X2 | Should |

### Domain 5: Order Fulfillment

| FR | Requirement (Short) | Phase | BP | BO | US | Role (Story) | UR | AC IDs | MoSCoW |
|----|---------------------|-------|-----|-----|-----|--------------|-----|--------|--------|
| FR-041 | Confirm availability | MVP | BP-16 | BO-05, BO-08, BO-15 | US-041 | Sales Representative | UR-12 | AC-041-H1…X2 | Must |
| FR-042 | Reserve inventory | MVP | BP-17 | BO-05, BO-08 | US-042 | Operations Manager | UR-04 | AC-042-H1…X2 | Must |
| FR-043 | Release reservations | MVP | BP-17,20 | BO-05 | US-043 | Customer Service Rep | UR-13 | AC-043-H1…X2 | Must |
| FR-044 | Pick, pack, ship | MVP | BP-18 | BO-05, BO-06, BO-15 | US-044 | Warehouse Picker | UR-08 | AC-044-H1…X2 | Must |
| FR-045 | Partial fulfillment | MVP | BP-19 | BO-05, BO-08 | US-045 | Customer Service Rep | UR-13 | AC-045-H1…X2 | Must |
| FR-046 | Backorder management | Ph2 | BP-19,17 | BO-08 | US-046 | Operations Manager | UR-04 | AC-046-H1…X2 | Should |
| FR-047 | Fulfillment exceptions | MVP | BP-20 | BO-05 | US-047 | Warehouse Manager | UR-06 | AC-047-H1…X2 | Must |
| FR-048 | Multi-location split fulfill | Ph2 | BP-16,18 | BO-05 | US-048 | Operations Manager | UR-04 | AC-048-H1…X2 | Should |
| FR-049 | Order fulfillment status | MVP | BP-18,19 | BO-06, BO-15, BO-17 | US-049 | Customer Service Rep | UR-13 | AC-049-H1…X2 | Must |
| FR-050 | Product substitution | Ph3 | BP-20 | BO-05 | US-050 | Warehouse Manager | UR-06 | AC-050-H1…X2 | Could |

### Domain 6: Replenishment & Inbound Supply

| FR | Requirement (Short) | Phase | BP | BO | US | Role (Story) | UR | AC IDs | MoSCoW |
|----|---------------------|-------|-----|-----|-----|--------------|-----|--------|--------|
| FR-051 | Low-stock/out-of-stock alerts | MVP | BP-21 | BO-07, BO-12, BO-13 | US-051 | Purchasing Manager | UR-15 | AC-051-H1…X2 | Must |
| FR-052 | Review/acknowledge alerts | MVP | BP-21 | BO-13 | US-052 | Purchasing Manager | UR-15 | AC-052-H1…X2 | Must |
| FR-053 | Replenishment suggestions | Ph2 | BP-22 | BO-09, BO-12 | US-053 | Buyer | UR-16 | AC-053-H1…X2 | Should |
| FR-054 | Purchase requisitions | Ph2 | BP-22,05 | BO-12, BO-13 | US-054 | Buyer | UR-16 | AC-054-H1…X2 | Should |
| FR-055 | Inbound supply tracking | Ph2 | BP-23 | BO-13 | US-055 | Customer Service Rep | UR-13 | AC-055-H1…X2 | Should |
| FR-056 | Safety stock protection | Ph2 | BP-03,17,24 | BO-07 | US-056 | Operations Director | UR-04 | AC-056-H1…X2 | Should |
| FR-057 | Promotional readiness review | Ph3/WNH | BP-31 | BO-24 | US-057 | Marketing Manager | UR-14 | AC-057-H1…X2 | **Won't** |

### Domain 7: Network Balance & Transfers

| FR | Requirement (Short) | Phase | BP | BO | US | Role (Story) | UR | AC IDs | MoSCoW |
|----|---------------------|-------|-----|-----|-----|--------------|-----|--------|--------|
| FR-058 | Request transfers | MVP | BP-24 | BO-14 | US-058 | Regional/Store Manager | UR-10 | AC-058-H1…X2 | Must |
| FR-059 | Approve/reject transfers | MVP | BP-24 | BO-14 | US-059 | Operations Director | UR-04 | AC-059-H1…X2 | Must |
| FR-060 | Execute transfers | MVP | BP-25 | BO-03, BO-14 | US-060 | Warehouse Manager | UR-06 | AC-060-H1…X2 | Must |
| FR-061 | Monitor in-transit inventory | Ph2 | BP-25 | BO-14 | US-061 | Operations Director | UR-04 | AC-061-H1…X2 | Should |
| FR-062 | Network rebalancing recommendations | Ph3/WNH | BP-26 | BO-14 | US-062 | Operations Director | UR-04 | AC-062-H1…X2 | **Won't** |
| FR-063 | Source minimum on transfers | Ph2 | BP-24,25 | BO-14 | US-063 | Operations Director | UR-04 | AC-063-H1…X2 | Should |

### Domain 8: Returns Management

| FR | Requirement (Short) | Phase | BP | BO | US | Role (Story) | UR | AC IDs | MoSCoW |
|----|---------------------|-------|-----|-----|-----|--------------|-----|--------|--------|
| FR-064 | Authorize/record returns | MVP | BP-27 | BO-03 | US-064 | Customer Service Rep | UR-13 | AC-064-H1…X2 | Must |
| FR-065 | Receive/inspect returns *(supersedes FR-019)* | Ph2 | BP-28 | BO-03, BO-11 | US-065 | Receiving Clerk | UR-07 | AC-065-H1…X2 | Should |
| FR-066 | Restock/write-off returns | Ph2 | BP-28 | BO-11 | US-066 | Warehouse Manager | UR-06 | AC-066-H1…X2 | Should |
| FR-067 | Return processing status | Ph2 | BP-27,28 | BO-17 | US-067 | Customer Service Rep | UR-13 | AC-067-H1…X2 | Should |

### Domain 9: Reporting & Dashboards

| FR | Requirement (Short) | Phase | BP | BO | US | Role (Story) | UR | AC IDs | MoSCoW |
|----|---------------------|-------|-----|-----|-----|--------------|-----|--------|--------|
| FR-068 | Inventory summary dashboard | MVP | BP-29 | BO-01, BO-04, BO-23 | US-068 | Operations Director | UR-04 | AC-068-H1…X2 | Must |
| FR-069 | Stock movement reports | MVP | BP-29 | BO-04, BO-19 | US-069 | Inventory Controller | UR-05 | AC-069-H1…X2 | Must |
| FR-070 | Stockout/overstock reports | MVP | BP-29,21,26 | BO-07, BO-09, BO-14 | US-070 | Purchasing Manager | UR-15 | AC-070-H1…X2 | Must |
| FR-071 | Accuracy/variance reports | MVP | BP-29,11,13 | BO-02, BO-20 | US-071 | Inventory Controller | UR-05 | AC-071-H1…X2 | Must |
| FR-072 | Location performance snapshots | Ph2 | BP-29 | BO-04 | US-072 | COO | UR-02 | AC-072-H1…X2 | Should |
| FR-073 | Inventory performance KPIs | Ph3 | BP-29 | BO-10, BO-23 | US-073 | CEO | UR-01 | AC-073-H1…X2 | Could |
| FR-074 | Basic replenishment reporting | Ph2 | BP-22,21 | BO-13 | US-074 | Buyer | UR-16 | AC-074-H1…X2 | Should |
| FR-075 | Valuation summary views | Ph2 | BP-30 | BO-10, BO-18, BO-20 | US-075 | Finance Manager | UR-17 | AC-075-H1…X2 | Should |

### Domain 10: Notifications & Alerts

| FR | Requirement (Short) | Phase | BP | BO | US | Role (Story) | UR | AC IDs | MoSCoW |
|----|---------------------|-------|-----|-----|-----|--------------|-----|--------|
| FR-076 | Low-stock notifications | MVP | BP-21 | BO-07, BO-13 | US-076 | Purchasing Manager | UR-15 | AC-076-H1…X2 | Must |
| FR-077 | Pending approval notifications | MVP | BP-13,14,24 | BO-19 | US-077 | Operations Director | UR-04 | AC-077-H1…X2 | Must |
| FR-078 | Transfer/fulfillment exceptions | Ph2 | BP-20,25 | BO-05, BO-14 | US-078 | Warehouse Manager | UR-06 | AC-078-H1…X2 | Should |
| FR-079 | Inbound delay notifications | Ph2 | BP-23 | BO-13 | US-079 | Buyer | UR-16 | AC-079-H1…X2 | Should |
| FR-080 | Campaign readiness alerts | Ph3/WNH | BP-31 | BO-24 | US-080 | Marketing Manager | UR-14 | AC-080-H1…X2 | **Won't** |

### Domain 11: User Access & Accountability

| FR | Requirement (Short) | Phase | BP | BO | US | Role (Story) | UR | AC IDs | MoSCoW |
|----|---------------------|-------|-----|-----|-----|--------------|-----|--------|--------|
| FR-081 | Role-based access control | MVP | BP-32 | BO-19, BO-21 | US-081 | System Administrator | *(Orphan)* | AC-081-H1…X2 | Must |
| FR-082 | Location-scoped access | MVP | BP-02,32 | BO-19 | US-082 | System Administrator | *(Orphan)* | AC-082-H1…X2 | Must |
| FR-083 | User activity logging | MVP | BP-32 | BO-19 | US-083 | Internal Auditor | UR-18 | AC-083-H1…X2 | Must |
| FR-084 | Segregation of duties | MVP | BP-13,14,32 | BO-19 | US-084 | System Administrator | *(Orphan)* | AC-084-H1…X2 | Must |
| FR-085 | User account management | MVP | BP-32 | BO-21 | US-085 | System Administrator | *(Orphan)* | AC-085-H1…X2 | Must |

### Domain 12: Governance, Audit & Compliance

| FR | Requirement (Short) | Phase | BP | BO | US | Role (Story) | UR | AC IDs | MoSCoW |
|----|---------------------|-------|-----|-----|-----|--------------|-----|--------|--------|
| FR-086 | Complete audit trail | MVP | BP-32 | BO-19 | US-086 | Internal Auditor | UR-18 | AC-086-H1…X2 | Must |
| FR-087 | Audit/control review queries | MVP | BP-32 | BO-19 | US-087 | Internal Auditor | UR-18 | AC-087-H1…X2 | Must |
| FR-088 | Control policy breach detection | Ph2 | BP-32 | BO-19 | US-088 | Internal Auditor | UR-18 | AC-088-H1…X2 | Should |
| FR-089 | Financial reconciliation support | Ph2 | BP-30 | BO-18, BO-20 | US-089 | Finance Manager | UR-17 | AC-089-H1…X2 | Should |
| FR-090 | Initial data import | MVP | BP-01,02 | BO-02 | US-090 | Inventory Controller | UR-05 | AC-090-H1…X2 | Must |

---

## 6. User Role Traceability Summary

### Story Role → UR Catalog Mapping

| Story Role (US) | UR ID | UR Name | Story Count | Notes |
|-----------------|-------|---------|-------------|-------|
| Inventory Controller | UR-05 | Inventory Controller | 18 | Primary master data and accuracy owner |
| Operations Director / Operations Manager | UR-04 | Operations Director | 22 | "Operations Manager" in stories maps to UR-04 |
| Warehouse Manager | UR-06 | Warehouse Manager | 12 | Location operations |
| Receiving Clerk | UR-07 | Receiving Clerk | 8 | Inbound operations |
| Warehouse Staff | UR-09 | Warehouse Staff | 2 | Put-away and counting |
| Warehouse Picker / Warehouse Operator | UR-08 | Warehouse Picker/Packer | 3 | Fulfillment floor |
| Buyer | UR-16 | Buyer/Procurement Officer | 6 | Purchasing execution |
| Purchasing Manager | UR-15 | Purchasing Manager | 8 | Procurement oversight |
| Sales Representative | UR-12 | Sales Representative | 4 | Commercial availability |
| Customer Service Representative | UR-13 | Customer Service Rep | 10 | Order status and returns |
| Regional / Store Manager | UR-10 | Regional/Store Manager | 1 | Transfer requests |
| Marketing Manager | UR-14 | Marketing Manager | 2 | Deferred (WNH) |
| Finance Manager | UR-17 | Finance Manager/Accountant | 2 | Valuation and reconciliation |
| Internal Auditor | UR-18 | Internal Auditor | 4 | Audit and compliance |
| COO | UR-02 | Chief Operating Officer | 1 | Location performance |
| CEO | UR-01 | Chief Executive Officer | 1 | Executive KPIs |
| **System Administrator** | **—** | **Not in UR catalog** | **4** | **OR-06: US-081, US-082, US-084, US-085** |

### UR → Primary FR Domains

| UR ID | Role | Primary FR Domains | BO Alignment |
|-------|------|-------------------|--------------|
| UR-01 | CEO | FR-073 | BO-23 |
| UR-02 | COO | FR-072, approvals | BO-05, BO-06 |
| UR-03 | CFO | FR-075 (read) | BO-10, BO-18 |
| UR-04 | Operations Director | FR-005–007, FR-037, FR-042, FR-048, FR-056, FR-059, FR-061–063, FR-068, FR-077 | BO-01–BO-06, BO-14 |
| UR-05 | Inventory Controller | FR-001–004, FR-008–011, FR-029–035, FR-039, FR-069, FR-071, FR-090 | BO-01, BO-02, BO-11, BO-19 |
| UR-06 | Warehouse Manager | FR-014–016, FR-034–038, FR-047, FR-050, FR-060, FR-066, FR-078 | BO-03, BO-05, BO-11 |
| UR-07 | Receiving Clerk | FR-003, FR-015–017, FR-019–020, FR-065 | BO-03 |
| UR-08 | Picker/Packer | FR-003, FR-044 | BO-05, BO-06 |
| UR-09 | Warehouse Staff | FR-018, FR-031 | BO-02, BO-03 |
| UR-10 | Regional/Store Manager | FR-058 | BO-14 |
| UR-11 | Sales Manager | FR-024, FR-027 (read) | BO-16 |
| UR-12 | Sales Representative | FR-024, FR-027, FR-041 | BO-16 |
| UR-13 | Customer Service Rep | FR-025, FR-043, FR-045, FR-049, FR-055, FR-064, FR-067 | BO-08, BO-15, BO-17 |
| UR-14 | Marketing Manager | FR-057, FR-080 *(deferred)* | BO-24 |
| UR-15 | Purchasing Manager | FR-013, FR-022, FR-051, FR-052, FR-053, FR-070, FR-076 | BO-07, BO-12, BO-13 |
| UR-16 | Buyer | FR-013, FR-021, FR-053, FR-054, FR-074, FR-079 | BO-12, BO-13 |
| UR-17 | Finance Manager | FR-075, FR-089 | BO-18, BO-20 |
| UR-18 | Internal Auditor | FR-083, FR-086–088 | BO-19 |
| UR-19 | External Auditor | *(Read-only via UR-18 parity)* | BO-19 |

---

## 7. Acceptance Criteria Coverage Summary

| Metric | Value |
|--------|-------|
| User stories with AC sections | **90 / 90 (100%)** |
| Estimated total acceptance criteria | **~360** (avg. 4 categories × ~4 criteria per story) |
| AC ID format | AC-{US}-H/V/E/X{n} |
| Stories with KPI/business threshold AC | **0** |
| Stories with integration AC | **0** |
| Stories with deferred (WNH) tag on AC | **0** (recommended for US-057, US-062, US-080) |
| Stories with E2E cross-reference | **0** |

### AC Category Distribution (All Stories)

| Category | Code | Purpose | Present For |
|----------|------|---------|-------------|
| Happy Path | H | Standard successful outcome | All 90 stories |
| Validation | V | Business rules and authorization | All 90 stories |
| Error | E | Failure handling | All 90 stories |
| Edge Cases | X | Boundaries and exceptions | All 90 stories |

---

## 8. Recommended Remediation Actions

| Priority | Action | Resolves |
|----------|--------|----------|
| **P1** | Publish Requirements Errata reconciling Phase vs MoSCoW for FR-057, FR-062, FR-080, FR-050 | OR-01–03, DUP conflicts |
| **P1** | Add explicit BO reference to every FR record | MT-01 |
| **P1** | Document FR-019→FR-065 and FR-057→FR-080 supersession rules | DUP-01, DUP-02 |
| **P1** | Add integration boundary FR for order intake minimum data contract | MT-06, OR-09 |
| **P2** | Create Acceptance Test Plan with BO/KPI thresholds (E2E scenarios) | MT-02, MT-08 |
| **P2** | Add UR-20 System Administrator to user roles catalog OR map to technical role | OR-06 |
| **P2** | Tag AC-057, AC-062, AC-080 as **Deferred — Won't Have** | OR-01–03 |
| **P2** | Define BO-22 success criteria outside IMS (change management plan) | OR-07, BO-22 |
| **P3** | Build NFR traceability matrix (204 NFRs → BO/FR) | MT-07 |
| **P3** | Add supplier master FR or document free-text supplier policy | OR-05 |
| **P3** | Add product substitute master FR before FR-050 delivery | OR-04 |

---

## 9. RTM Statistics

| Artifact | Total | Fully Traced | Gaps |
|----------|-------|--------------|------|
| Business Objectives | 24 | 22 (derived FR path) | 2 weak/uncovered (BO-22, BO-24) |
| Business Processes | 32 | 32 (via FR) | 3 partial at MVP (BP-05, BP-06, BP-31) |
| Functional Requirements | 90 | 90 (→US→AC) | 4 release orphans (WNH) |
| User Stories | 90 | 90 | 4 role orphans (Sys Admin) |
| Acceptance Criteria | ~360 | ~360 | 0 KPI; 0 integration; 0 E2E |
| User Roles | 19 | 17 linked to stories | Sys Admin, External Auditor (passive) |

---

## Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Senior Business Analyst | | | |
| Product Owner | | | |
| QA Lead | | | |

---

*End of Requirements Traceability Matrix*

*Document ID: RTM-IMS-001 | Version 1.0 | July 3, 2026*
