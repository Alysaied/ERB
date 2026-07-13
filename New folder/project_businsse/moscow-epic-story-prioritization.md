# MoSCoW Prioritization: Epics & User Stories

**Document Owner:** Product Owner  
**Purpose:** Prioritize all product epics and user stories for the Inventory Management System using the MoSCoW method  
**Audience:** Steering committee, business stakeholders, product owners, delivery teams  
**Based On:** BRD-IMS-001, EPIC-IMS-001, US-001 – US-090, MoSCoW FR Prioritization, Project Scope (MVP / Phase 2 / Phase 3)  
**Review Date:** July 5, 2026

---

## MoSCoW Definitions

| Priority | Meaning | Target Release |
|----------|---------|----------------|
| **Must Have** | Non-negotiable for MVP go-live. Initiative or MVP success criteria fail without it. | Phase 1 — MVP (Months 0–6) |
| **Should Have** | Important for operational performance after MVP stabilization. Business can operate briefly without it. | Phase 2 (Months 6–12) |
| **Could Have** | Strategic maturity, analytics, financial alignment. Deferrable without blocking daily operations. | Phase 3 (Months 12–18) |
| **Won't Have** | Not committed for the current 18-month initiative. Documented for future planning. | Beyond current initiative |

**Note:** Epics spanning multiple phases are **Must Have** at epic level when their MVP subset is required for go-live. Individual stories within the epic carry their own MoSCoW priority.

---

## Prioritization Summary

### Epics

| Priority | Epics | Story Count |
|----------|-------|-------------|
| **Must Have** (MVP core) | EPIC-01, EPIC-02*, EPIC-03, EPIC-04, EPIC-05*, EPIC-06*, EPIC-07*, EPIC-09*, EPIC-10*, EPIC-11, EPIC-12* | 55 Must Have stories |
| **Should Have** (Phase 2 emphasis) | EPIC-02†, EPIC-05†, EPIC-06†, EPIC-07†, EPIC-08, EPIC-09†, EPIC-10†, EPIC-12† | 26 Should Have stories |
| **Could Have** (Phase 3) | EPIC-02‡, EPIC-04‡, EPIC-05‡, EPIC-09‡ | 6 Could Have stories |
| **Won't Have** | EPIC-06§, EPIC-07§, EPIC-10§ | 3 Won't Have stories |

\* Epic required for MVP; not all stories in epic are Must Have  
† Epic has significant Phase 2 delivery  
‡ Epic contains Phase 3 stories only  
§ Epic contains deferred stories only (rest of epic still required)

### User Stories

| Priority | Count | % |
|----------|-------|---|
| **Must Have** | 55 | 61% |
| **Should Have** | 26 | 29% |
| **Could Have** | 6 | 7% |
| **Won't Have** | 3 | 3% |
| **Total** | 90 | 100% |

---

## Suggested Implementation Roadmap

### Wave 0 — Enablers (Sprint 1–2)
| Order | Epic / Stories | Priority |
|-------|----------------|----------|
| 1 | **EPIC-11** — US-081 → US-085 | Must Have |
| 2 | **EPIC-01** — US-001 → US-006, US-011, US-090 | Must Have |

### Wave 1 — Foundation & Visibility (Sprint 3–5)
| Order | Epic / Stories | Priority |
|-------|----------------|----------|
| 3 | **EPIC-01** — US-008, US-010, US-002, US-003, US-004 | Must Have |
| 4 | **EPIC-03** — US-023 → US-027 | Must Have |
| 5 | **EPIC-04** — US-029 | Must Have |
| 6 | **EPIC-12** — US-086 | Must Have |

### Wave 2 — Inbound & Control (Sprint 6–9)
| Order | Epic / Stories | Priority |
|-------|----------------|----------|
| 7 | **EPIC-02** — US-015 → US-019, US-018 | Must Have |
| 8 | **EPIC-04** — US-030 → US-037 | Must Have |
| 9 | **EPIC-10** — US-077 | Must Have |

### Wave 3 — Fulfillment & Replenishment (Sprint 10–13)
| Order | Epic / Stories | Priority |
|-------|----------------|----------|
| 10 | **EPIC-05** — US-041 → US-045, US-049 | Must Have |
| 11 | **EPIC-06** — US-051 → US-053, US-074 | Must Have |
| 12 | **EPIC-10** — US-076 | Must Have |

### Wave 4 — Network & Reporting (Sprint 14–16)
| Order | Epic / Stories | Priority |
|-------|----------------|----------|
| 13 | **EPIC-07** — US-058 → US-060, US-063 | Must Have |
| 14 | **EPIC-09** — US-068 → US-071 | Must Have |

### Wave 5 — MVP Hardening & Go-Live (Sprint 17–18)
| Order | Epic / Stories | Priority |
|-------|----------------|----------|
| 15 | Regression, E2E golden paths, UAT | — |
| 16 | **EPIC-01** — US-090 data load at primary locations | Must Have |

### Wave 6 — Phase 2 Performance (Months 6–12)
| Order | Epic / Stories | Priority |
|-------|----------------|----------|
| 17 | **EPIC-02** — US-013, US-014, US-020, US-021, US-055 | Should Have |
| 18 | **EPIC-06** — US-054, US-056 | Should Have |
| 19 | **EPIC-05** — US-046, US-047, US-048 | Should Have |
| 20 | **EPIC-07** — US-061 | Should Have |
| 21 | **EPIC-08** — US-064 → US-067 | Should Have |
| 22 | **EPIC-01** — US-007, US-009, US-012 | Should Have |
| 23 | **EPIC-03** — US-028 | Should Have |
| 24 | **EPIC-04** — US-038, US-039 | Should Have |
| 25 | **EPIC-09** — US-072 | Should Have |
| 26 | **EPIC-10** — US-078, US-079 | Should Have |
| 27 | **EPIC-12** — US-087, US-088 | Should Have |

### Wave 7 — Phase 3 Strategic Maturity (Months 12–18)
| Order | Epic / Stories | Priority |
|-------|----------------|----------|
| 28 | **EPIC-09** — US-073, US-075, US-089 | Could Have |
| 29 | **EPIC-02** — US-022 | Could Have |
| 30 | **EPIC-04** — US-040 | Could Have |
| 31 | **EPIC-05** — US-050 | Could Have |

### Deferred — Won't Have (Current Release)
| Order | Stories | Priority |
|-------|---------|----------|
| — | US-057, US-062, US-080 | Won't Have |

---

# Epic Prioritization

---

## EPIC-11: Security, Access & Accountability

| Attribute | Detail |
|-----------|--------|
| **Epic priority** | **Must Have** |
| **Business justification** | Prerequisite for every operational story. Without RBAC, location scope, SoD, and user management, inventory data cannot be protected — blocking BO-19 (audit readiness) and BO-21 (controlled adoption). |
| **Dependencies** | None — deliver first or in parallel with EPIC-01 Wave 0 |
| **Suggested implementation order** | **1** (Wave 0) |

### User Stories

| Order | Story | Title | Priority | Business Justification | Dependencies |
|------:|-------|-------|----------|------------------------|--------------|
| 1 | US-081 | Enforce role-based access control | **Must Have** | Protects all inventory transactions by role — foundation of internal control | None |
| 2 | US-085 | Manage user accounts and role assignments | **Must Have** | Enables go-live provisioning and ongoing access governance | US-081 |
| 3 | US-082 | Restrict access by location | **Must Have** | Aligns visibility and transactions to location accountability (BO-01) | US-081, US-005 |
| 4 | US-083 | Log user activity for accountability | **Must Have** | Traceability for audit and loss prevention (BO-19) | US-081 |
| 5 | US-084 | Enforce segregation of duties | **Must Have** | Prevents self-approval fraud and error in counts/adjustments | US-081, US-034, US-037 |

---

## EPIC-01: Master Data & Network Foundation

| Attribute | Detail |
|-----------|--------|
| **Epic priority** | **Must Have** (epic); mixed at story level |
| **Business justification** | Structural backbone — product catalog, locations, policies, and go-live import. Without this epic, no receiving, fulfillment, or reporting can function (BO-01, BO-02, BO-21). |
| **Dependencies** | EPIC-11 for authorized configuration access |
| **Suggested implementation order** | **2** (Wave 0–1) |

### User Stories

| Order | Story | Title | Priority | Business Justification | Dependencies |
|------:|-------|-------|----------|------------------------|--------------|
| 1 | US-001 | Create and maintain product master records | **Must Have** | Single product identity — eliminates PP-07 fragmented records | EPIC-11 |
| 2 | US-005 | Configure and maintain inventory locations | **Must Have** | Foundational structure for all stock tracking (BO-01) | EPIC-11 |
| 3 | US-006 | Manage location hierarchy | **Must Have** | Regional rollup and network reporting at MVP scale | US-005 |
| 4 | US-011 | Maintain standard reason codes | **Must Have** | Required for adjustments, write-offs, discrepancies (BR-20) | EPIC-11 |
| 5 | US-090 | Initial data import for go-live | **Must Have** | Practical adoption at primary locations without manual catalog entry | US-001, US-005, US-004, US-010 |
| 6 | US-002 | Manage product status lifecycle | **Must Have** | Blocks obsolete products from replenishment/fulfillment | US-001 |
| 7 | US-003 | Product identifier lookup | **Must Have** | Floor accuracy for receive, count, pick | US-001 |
| 8 | US-004 | Detect and resolve duplicate products | **Must Have** | Prevents split stock at go-live (BR-06) | US-001 |
| 9 | US-008 | Define stock policy and thresholds | **Must Have** | Enables proactive alerts and replenishment (BO-05) | US-001, US-005 |
| 10 | US-010 | Establish opening stock balance | **Must Have** | Trusted baseline at location go-live (BO-02) | US-005, US-032 |
| 11 | US-007 | Plan location closure and disposition | **Should Have** | Needed before first closure event, not initial go-live | US-005, US-058, US-060, US-035 |
| 12 | US-009 | Classify products by ABC priority | **Should Have** | Focuses count/alert effort on high-impact SKUs (BR-32) | US-001, US-030, US-051 |
| 13 | US-012 | Manage inventory governance policies | **Should Have** | Formalizes thresholds and approval rules (PP-09) | US-037, US-034, US-081 |
| 14 | US-056 | Enforce safety stock protection rules | **Should Have** | Preserves buffer stock from routine consumption (BR-10) | US-008, US-042, US-058, US-012 |

---

## EPIC-02: Inbound Supply & Goods Receiving

| Attribute | Detail |
|-----------|--------|
| **Epic priority** | **Must Have** (MVP receiving); **Should Have** (PO module) |
| **Business justification** | Ensures stock entering the organization is verified and recorded accurately from point of entry (BO-03, BO-05). |
| **Dependencies** | EPIC-01 (products, locations), EPIC-11 |
| **Suggested implementation order** | **3** (Wave 2 for MVP; Wave 6 for PO) |

### User Stories

| Order | Story | Title | Priority | Business Justification | Dependencies |
|------:|-------|-------|----------|------------------------|--------------|
| 1 | US-015 | Receive and verify inbound goods | **Must Have** | On-hand reflects physical reality at entry (BR-4) | US-001, US-005, US-003 |
| 2 | US-017 | Enforce PO reference for receipts | **Must Have** | Procurement control with ad-hoc exception path | US-015 |
| 3 | US-016 | Document and resolve receipt discrepancies | **Must Have** | Supplier accountability; prevents corrupt records | US-015, US-011 |
| 4 | US-018 | Confirm put-away completion | **Must Have** | ATP reflects locatable stock only (BR-5) | US-015 |
| 5 | US-019 | Receive return and non-PO inbound | **Must Have** | Captures all inventory increases (BO-03); MVP returns path | US-015 |
| 6 | US-013 | Record purchase order commitments | **Should Have** | Inbound visibility for ops and sales | US-001, US-005, US-015 |
| 7 | US-014 | Plan expected inbound deliveries | **Should Have** | Receiving preparedness; reduces dock congestion | US-013 |
| 8 | US-020 | Receipt quantity tolerance evaluation | **Should Have** | Balances flexibility with receipt control | US-015, US-016, US-013 |
| 9 | US-021 | Cancel or amend open purchase orders | **Should Have** | Accurate inbound projections | US-013 |
| 10 | US-055 | Track inbound supply status | **Should Have** | CS restock date communication (BP-23) | US-013, US-028 |
| 11 | US-022 | Supplier delivery performance | **Could Have** | Supplier analytics for replenishment decisions | US-013, US-016, US-015 |

---

## EPIC-03: Real-Time Inventory Visibility

| Attribute | Detail |
|-----------|--------|
| **Epic priority** | **Must Have** |
| **Business justification** | Delivers single source of truth — "what do we have and where?" (BO-01, BO-16). Core value proposition of the initiative. |
| **Dependencies** | EPIC-01, EPIC-04 (US-029 movements), EPIC-02 (receipts) |
| **Suggested implementation order** | **4** (Wave 1) |

### User Stories

| Order | Story | Title | Priority | Business Justification | Dependencies |
|------:|-------|-------|----------|------------------------|--------------|
| 1 | US-023 | Display on-hand quantity | **Must Have** | Foundational visibility without spreadsheets (BO-01) | US-029, US-001, US-005 |
| 2 | US-024 | Display ATP quantity | **Must Have** | Prevents overselling (BR-1, BO-06) | US-023, US-025, US-018 |
| 3 | US-025 | Display reserved and committed stock | **Must Have** | Explains ATP vs on-hand gap | US-042 |
| 4 | US-026 | Indicate stock status indicators | **Must Have** | Rapid problem identification in daily review | US-008, US-024 |
| 5 | US-027 | Search and filter inventory views | **Must Have** | Self-service availability; reduces warehouse calls (BO-16) | US-023 |
| 6 | US-028 | Expected inbound and network-wide availability | **Should Have** | Transfer-before-purchase; network restock dates | US-013, US-023, US-024 |

---

## EPIC-04: Inventory Control & Accuracy

| Attribute | Detail |
|-----------|--------|
| **Epic priority** | **Must Have** |
| **Business justification** | Sustains ≥95% accuracy target (BO-02), complete traceability (BO-03, BO-19), and controlled adjustments. |
| **Dependencies** | EPIC-01, EPIC-11 |
| **Suggested implementation order** | **5** (Wave 1–2) |

### User Stories

| Order | Story | Title | Priority | Business Justification | Dependencies |
|------:|-------|-------|----------|------------------------|--------------|
| 1 | US-029 | Record all inventory movements | **Must Have** | Complete traceability for audit and investigation | US-001, US-005 |
| 2 | US-030 | Schedule and assign cycle counts | **Must Have** | Rotating verification sustains accuracy (BO-02) | US-001, US-005 |
| 3 | US-031 | Perform blind cycle counts | **Must Have** | Unbiased accuracy measurement (BR-18) | US-030 |
| 4 | US-032 | Conduct full physical inventory count | **Must Have** | Baseline for finance and opening balances | US-005 |
| 5 | US-033 | Identify and report count variances | **Must Have** | Focus investigation on material discrepancies | US-030, US-031, US-032 |
| 6 | US-034 | Investigate and approve count adjustments | **Must Have** | SoD and authorized corrections (BR-19) | US-033 |
| 7 | US-035 | Process stock adjustments with reason codes | **Must Have** | Accountable corrections (BR-20) | US-011, US-037 |
| 8 | US-036 | Process inventory write-offs | **Must Have** | Controlled removal of unsellable stock (BR-23) | US-011, US-037 |
| 9 | US-037 | Enforce adjustment approval thresholds | **Must Have** | Oversight proportional to financial impact | US-035, US-036, US-034 |
| 10 | US-038 | Manage quarantine and hold stock | **Should Have** | Prevents shipping defective goods (BR-13) | US-024, US-035, US-065 |
| 11 | US-039 | Analyze shrinkage and loss trends | **Should Have** | Actionable loss prevention insight | US-035, US-036, US-071 |
| 12 | US-040 | Review obsolete and slow-moving stock | **Could Have** | Releases working capital (PP-15) | US-029, US-002, US-070 |

---

## EPIC-05: Order Fulfillment

| Attribute | Detail |
|-----------|--------|
| **Epic priority** | **Must Have** (core fulfillment); **Should Have** (exceptions/split) |
| **Business justification** | Reliable fill rate and customer commitment integrity (BO-06, BO-16). Prevents overselling and fulfillment failures. |
| **Dependencies** | EPIC-03 (ATP), EPIC-11; external order boundary |
| **Suggested implementation order** | **6** (Wave 3) |

### User Stories

| Order | Story | Title | Priority | Business Justification | Dependencies |
|------:|-------|-------|----------|------------------------|--------------|
| 1 | US-041 | Confirm order availability | **Must Have** | Prevents overpromising (PP-04) | US-024 |
| 2 | US-042 | Reserve inventory for orders | **Must Have** | Prevents double-allocation (BR-2) | US-024, US-041 |
| 3 | US-043 | Release inventory reservations | **Must Have** | Restores ATP on cancel/fulfill | US-042 |
| 4 | US-044 | Pick, pack, and ship workflow | **Must Have** | Accurate deduction at shipment (BR-3) | US-042, US-003 |
| 5 | US-045 | Handle partial fulfillment | **Must Have** | Balances service with inventory reality | US-042, US-044 |
| 6 | US-049 | Display order fulfillment status | **Must Have** | CS accuracy; reduces warehouse calls | US-042, US-044, US-045 |
| 7 | US-046 | Manage backorders and priority | **Should Have** | Fair delayed-order fulfillment | US-045, US-042, US-053 |
| 8 | US-047 | Handle fulfillment exceptions | **Should Have** | Minimizes customer impact from pick failures | US-044, US-035, US-049 |
| 9 | US-048 | Multi-location split fulfillment | **Should Have** | Maximizes network fill rate | US-041, US-042, US-044, US-060 |
| 10 | US-050 | Authorized product substitution | **Could Have** | Recovers revenue on unavailable SKUs | US-047, US-001, US-044 |

---

## EPIC-06: Replenishment Planning & Stock Alerts

| Attribute | Detail |
|-----------|--------|
| **Epic priority** | **Must Have** (alerts/suggestions); **Should Have** (requisitions) |
| **Business justification** | Proactive stockout prevention and threshold-driven purchasing (BO-05). |
| **Dependencies** | EPIC-01 (US-008 thresholds), EPIC-03 |
| **Suggested implementation order** | **7** (Wave 3) |

### User Stories

| Order | Story | Title | Priority | Business Justification | Dependencies |
|------:|-------|-------|----------|------------------------|--------------|
| 1 | US-051 | Generate low-stock and out-of-stock alerts | **Must Have** | Actionable signals before customer stockouts (BR-9) | US-008, US-024, US-026 |
| 2 | US-052 | Review and acknowledge stock alerts | **Must Have** | Closes alert loop; prevents fatigue | US-051 |
| 3 | US-053 | Generate replenishment suggestions | **Must Have** | Data-driven ordering vs gut-feel | US-008, US-051, US-052 |
| 4 | US-074 | Basic replenishment reporting | **Must Have** | Consolidated purchasing daily view | US-051, US-053 |
| 5 | US-054 | Create and track purchase requisitions | **Should Have** | Formal procurement handoff | US-053, US-013, US-077 |
| 6 | US-057 | Promotional stock readiness review | **Won't Have** | Campaign ROI protection — deferred (BO-24) | US-008, US-013, US-028, US-053 |

---

## EPIC-07: Network Balance & Stock Transfers

| Attribute | Detail |
|-----------|--------|
| **Epic priority** | **Must Have** (manual transfers); **Won't Have** (auto rebalancing) |
| **Business justification** | Resolve local stockouts using network inventory without waiting for suppliers (PP-02, BO-05). |
| **Dependencies** | EPIC-01, EPIC-03 |
| **Suggested implementation order** | **8** (Wave 4) |

### User Stories

| Order | Story | Title | Priority | Business Justification | Dependencies |
|------:|-------|-------|----------|------------------------|--------------|
| 1 | US-058 | Request inter-location transfers | **Must Have** | Network balancing without supplier wait | US-005, US-023, US-024 |
| 2 | US-059 | Approve or reject transfer requests | **Must Have** | Authorized stock movements | US-058, US-063 |
| 3 | US-060 | Execute and record transfers | **Must Have** | Accurate balances at both locations | US-059, US-029 |
| 4 | US-063 | Enforce source location minimum | **Must Have** | Prevents cascading stockouts (BR-12) | US-008, US-058 |
| 5 | US-061 | Monitor in-transit inventory | **Should Have** | Visibility during transfer lead time | US-060 |
| 6 | US-062 | Network rebalancing recommendations | **Won't Have** | Premature without sustained accuracy (BO-02) | US-028, US-058, US-070, US-072 |

---

## EPIC-08: Returns Management

| Attribute | Detail |
|-----------|--------|
| **Epic priority** | **Should Have** (full module); MVP covered by US-019 |
| **Business justification** | Complete return lifecycle with inspection and disposition (BO-03, BO-06). |
| **Dependencies** | EPIC-05 (US-049), EPIC-02 (US-019 interim) |
| **Suggested implementation order** | **9** (Wave 6) |

### User Stories

| Order | Story | Title | Priority | Business Justification | Dependencies |
|------:|-------|-------|----------|------------------------|--------------|
| 1 | US-064 | Authorize and record customer returns | **Should Have** | Links returns to orders (BR-25) | US-049, US-019 |
| 2 | US-065 | Receive and inspect returned goods | **Should Have** | Only resalable stock re-enters ATP (BR-26) | US-064, US-038 |
| 3 | US-066 | Restock or write off returned inventory | **Should Have** | Accurate post-return balances | US-065, US-035, US-036 |
| 4 | US-067 | Track return processing status | **Should Have** | CS communication on refund timing | US-064, US-065, US-066 |

---

## EPIC-09: Reporting, Analytics & Financial Alignment

| Attribute | Detail |
|-----------|--------|
| **Epic priority** | **Must Have** (operational reports); **Could Have** (KPIs, finance) |
| **Business justification** | Management oversight, accuracy measurement, and reconciliation reduction (BO-01, BO-04, BO-07). |
| **Dependencies** | EPIC-03, EPIC-04 transaction data |
| **Suggested implementation order** | **10** (Wave 4 MVP; Wave 7 Phase 3) |

### User Stories

| Order | Story | Title | Priority | Business Justification | Dependencies |
|------:|-------|-------|----------|------------------------|--------------|
| 1 | US-068 | Inventory summary dashboard | **Must Have** | Single operational health view (BO-01) | US-023, US-026, US-051 |
| 2 | US-069 | Stock movement reports | **Must Have** | Replaces manual reconstruction (BO-04) | US-029 |
| 3 | US-070 | Stockout and overstock reports | **Must Have** | Directs purchasing and transfer action | US-026, US-008 |
| 4 | US-071 | Inventory accuracy and variance reports | **Must Have** | Measures BO-02 progress | US-030, US-033, US-034 |
| 5 | US-072 | Location performance snapshots | **Should Have** | Cross-location accountability | US-071, US-070, US-068 |
| 6 | US-073 | Inventory performance KPIs | **Could Have** | Executive maturity metrics | US-068, US-071, US-049, US-029 |
| 7 | US-075 | Inventory valuation summary views | **Could Have** | Ops-finance bridge (BO-07) | US-023, US-035, US-036 |
| 8 | US-089 | Financial inventory reconciliation | **Could Have** | Timely month-end close (BO-20) | US-075, US-086, US-071, US-036 |

---

## EPIC-10: Operational Notifications & Awareness

| Attribute | Detail |
|-----------|--------|
| **Epic priority** | **Must Have** (stock/approval alerts); **Should Have** (exception/inbound) |
| **Business justification** | Reduces decision latency for stock, approvals, and exceptions (BO-05, BO-06). |
| **Dependencies** | Source stories in EPIC-04, EPIC-05, EPIC-06, EPIC-07 |
| **Suggested implementation order** | **11** (Wave 2–3 MVP; Wave 6 extensions) |

### User Stories

| Order | Story | Title | Priority | Business Justification | Dependencies |
|------:|-------|-------|----------|------------------------|--------------|
| 1 | US-077 | Pending approval notifications | **Must Have** | Prevents approval bottlenecks | US-037, US-034, US-059 |
| 2 | US-076 | Low-stock and out-of-stock notifications | **Must Have** | Prompt action on preventable stockouts | US-051 |
| 3 | US-078 | Transfer and fulfillment exception alerts | **Should Have** | Rapid exception response | US-047, US-061, US-076 |
| 4 | US-079 | Inbound supply delay notifications | **Should Have** | Proactive restock delay communication | US-055, US-076 |
| 5 | US-080 | Campaign readiness alerts | **Won't Have** | Depends on deferred US-057 | US-057, US-076, US-051 |

---

## EPIC-12: Governance, Audit & Compliance

| Attribute | Detail |
|-----------|--------|
| **Epic priority** | **Must Have** (audit trail); **Should Have** (audit queries, breach detection) |
| **Business justification** | Demonstrates control effectiveness and supports audit readiness (BO-19, BO-07). |
| **Dependencies** | EPIC-04 (US-029), EPIC-11 |
| **Suggested implementation order** | **12** (Wave 1 MVP trail; Wave 6 maturity) |

### User Stories

| Order | Story | Title | Priority | Business Justification | Dependencies |
|------:|-------|-------|----------|------------------------|--------------|
| 1 | US-086 | Complete audit trail of inventory changes | **Must Have** | 100% traceability for audit (BO-19) | US-029, US-083 |
| 2 | US-087 | Audit and control review queries | **Should Have** | Reduces audit preparation effort | US-086, US-083, US-084 |
| 3 | US-088 | Detect and record control policy breaches | **Should Have** | Proactive control weakness visibility | US-012, US-086, US-083 |

---

## Master Story List — Implementation Order

Global sequence for committed stories (Won't Have stories excluded).

| Impl. # | Story | Epic | Priority | Phase |
|--------:|-------|------|----------|-------|
| 1 | US-081 | EPIC-11 | Must Have | MVP |
| 2 | US-085 | EPIC-11 | Must Have | MVP |
| 3 | US-082 | EPIC-11 | Must Have | MVP |
| 4 | US-083 | EPIC-11 | Must Have | MVP |
| 5 | US-084 | EPIC-11 | Must Have | MVP |
| 6 | US-001 | EPIC-01 | Must Have | MVP |
| 7 | US-005 | EPIC-01 | Must Have | MVP |
| 8 | US-006 | EPIC-01 | Must Have | MVP |
| 9 | US-011 | EPIC-01 | Must Have | MVP |
| 10 | US-002 | EPIC-01 | Must Have | MVP |
| 11 | US-003 | EPIC-01 | Must Have | MVP |
| 12 | US-004 | EPIC-01 | Must Have | MVP |
| 13 | US-008 | EPIC-01 | Must Have | MVP |
| 14 | US-029 | EPIC-04 | Must Have | MVP |
| 15 | US-086 | EPIC-12 | Must Have | MVP |
| 16 | US-023 | EPIC-03 | Must Have | MVP |
| 17 | US-024 | EPIC-03 | Must Have | MVP |
| 18 | US-025 | EPIC-03 | Must Have | MVP |
| 19 | US-026 | EPIC-03 | Must Have | MVP |
| 20 | US-027 | EPIC-03 | Must Have | MVP |
| 21 | US-077 | EPIC-10 | Must Have | MVP |
| 22 | US-015 | EPIC-02 | Must Have | MVP |
| 23 | US-017 | EPIC-02 | Must Have | MVP |
| 24 | US-016 | EPIC-02 | Must Have | MVP |
| 25 | US-018 | EPIC-02 | Must Have | MVP |
| 26 | US-019 | EPIC-02 | Must Have | MVP |
| 27 | US-010 | EPIC-01 | Must Have | MVP |
| 28 | US-030 | EPIC-04 | Must Have | MVP |
| 29 | US-031 | EPIC-04 | Must Have | MVP |
| 30 | US-032 | EPIC-04 | Must Have | MVP |
| 31 | US-033 | EPIC-04 | Must Have | MVP |
| 32 | US-034 | EPIC-04 | Must Have | MVP |
| 33 | US-035 | EPIC-04 | Must Have | MVP |
| 34 | US-036 | EPIC-04 | Must Have | MVP |
| 35 | US-037 | EPIC-04 | Must Have | MVP |
| 36 | US-041 | EPIC-05 | Must Have | MVP |
| 37 | US-042 | EPIC-05 | Must Have | MVP |
| 38 | US-043 | EPIC-05 | Must Have | MVP |
| 39 | US-044 | EPIC-05 | Must Have | MVP |
| 40 | US-045 | EPIC-05 | Must Have | MVP |
| 41 | US-049 | EPIC-05 | Must Have | MVP |
| 42 | US-051 | EPIC-06 | Must Have | MVP |
| 43 | US-052 | EPIC-06 | Must Have | MVP |
| 44 | US-053 | EPIC-06 | Must Have | MVP |
| 45 | US-074 | EPIC-06/09 | Must Have | MVP |
| 46 | US-076 | EPIC-10 | Must Have | MVP |
| 47 | US-058 | EPIC-07 | Must Have | MVP |
| 48 | US-059 | EPIC-07 | Must Have | MVP |
| 49 | US-060 | EPIC-07 | Must Have | MVP |
| 50 | US-063 | EPIC-07 | Must Have | MVP |
| 51 | US-068 | EPIC-09 | Must Have | MVP |
| 52 | US-069 | EPIC-09 | Must Have | MVP |
| 53 | US-070 | EPIC-09 | Must Have | MVP |
| 54 | US-071 | EPIC-09 | Must Have | MVP |
| 55 | US-090 | EPIC-01 | Must Have | MVP |
| 56–81 | US-007, US-009, US-012, US-013–US-014, US-020–US-021, US-028, US-038–US-039, US-046–US-048, US-054–US-055, US-056, US-061, US-064–US-067, US-072, US-078–US-079, US-087–US-088 | Various | Should Have | Phase 2 |
| 82–87 | US-022, US-040, US-050, US-073, US-075, US-089 | Various | Could Have | Phase 3 |
| — | US-057, US-062, US-080 | Various | Won't Have | Deferred |

---

## Dependency Rules for Sprint Planning

1. **Never schedule** a story before its dependencies are Done (per DOR-IMS-001 §4).
2. **EPIC-11** stories must be Done before operational UAT begins.
3. **US-090** runs late in MVP but **US-004** duplicate check must be Done before import.
4. **Notification stories** (EPIC-10) deploy after their source event stories.
5. **Won't Have** stories (US-057, US-062, US-080) are excluded from release commitment until steering committee re-baselines scope.

---

## Document Control

| Attribute | Detail |
|-----------|--------|
| **Document ID** | MOSCOW-EPIC-IMS-001 |
| **Version** | 1.0 |
| **Related Artifacts** | MoSCoW FR Prioritization, EPIC-IMS-001, DOR-IMS-001, BRD-IMS-001 |
| **Review Cadence** | Re-baseline at phase gates and after steering committee scope decisions |

---

*End of MoSCoW Epic & User Story Prioritization*
