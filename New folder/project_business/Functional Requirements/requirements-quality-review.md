# Requirements Quality Review

**Document Owner:** Senior Product Owner  
**Purpose:** Review functional requirements artifacts for completeness, consistency, duplicates, ambiguities, and conflicts  
**Audience:** Product owners, business analysts, delivery teams, and QA  
**Scope:** Functional requirements, feature catalog, user stories, and acceptance criteria  
**Based On:** `functional-requirements.md`, `feature-catalog.md`, `user-stories.md`, `acceptance-criteria.md`, `moscow-prioritization.md`, `requirements-dependency-analysis.md`, project scope, domain analysis, and domain knowledge review

---

## Executive Summary

The requirements set is **structurally complete at the FR layer** (90/90 FRs → user stories → acceptance criteria) and **strong for MVP inventory control**. It is **not yet decision-ready for delivery** without resolving prioritization inconsistencies, several intentional-but-unclear overlaps, and gaps at integration and policy boundaries.

| Dimension | Score | Notes |
|-----------|-------|-------|
| FR completeness vs 32 BPs | **85%** | Core ops covered; integration, supplier, substitute gaps |
| Feature catalog coverage | **90%** | 90/90 FRs mapped; cross-cutting ownership unclear |
| User story coverage | **95%** | 1:1 complete; missing integration/epic stories |
| Acceptance criteria coverage | **90%** | All stories covered; missing KPI, integration, E2E |
| Internal consistency | **70%** | Phase/MoSCoW conflicts, duplicate paths, policy gaps |
| Delivery readiness | **Conditional Go** | Fix Priority 1 items before MVP sprint 1 on fulfillment/inbound |

---

## 1. Missing Features

These are business capabilities implied by scope, domain analysis, or dependent FRs but **not represented as features or FRs**:

| Gap | Why It Matters | Recommendation |
|-----|----------------|----------------|
| **Order intake / fulfillment integration boundary** | FR-041–049 assume orders exist; project scope excludes CRM but requires reservation and status visibility | Add **F-31: Order Fulfillment Integration** with FR for minimum order/line data contract, reservation trigger, and status sync — even if orders originate externally |
| **Supplier / vendor master** | FR-013, FR-022 reference supplier; no entity to maintain suppliers | Add **FR-091: Maintain Supplier Reference Data** (minimal: ID, name, status) or explicitly state supplier is free-text with no master |
| **Product alternate / substitute relationships** | FR-050 requires "approved alternate SKUs"; no FR to define them (Q-08) | Add **FR-092: Manage Approved Product Substitutes** linked to FR-001 |
| **Unit of measure conversion** | AC-050-X2 references conversion rules; domain knowledge flags this as top error source | Add **FR-093: Define UoM Conversion Rules** per product or category |
| **Backorder priority policy configuration** | FR-046 references undefined rules (WG-07, Q-07) | Add **FR-094: Configure Backorder Allocation Rules** or fold into FR-012 governance |
| **Notification preferences & routing** | F-26 covers delivery; not who receives what, escalation windows, or channel | Add lightweight **FR-095: Configure Alert Recipients and Escalation Rules** |
| **Transfer cancellation / reversal** | FR-058–060 cover request→execute; no explicit cancel-in-transit | Add **FR-096: Cancel or Reverse In-Flight Transfers** |
| **Quarantine release workflow (explicit)** | WG-05; FR-038 mentions release but no dedicated disposition step | Extend FR-038 or add **FR-097: Release or Dispose Quarantined Stock** with inspection outcomes |
| **Reason code administration (standalone feature)** | FR-011 is foundational but buried in F-17 (Adjustments) | Create **F-31a: Reference Data Administration** grouping FR-011, future supplier/substitute/UoM FRs |
| **ASN / advance shipment notice** | Domain Q-15; FR-014 is shipment planning only | Defer explicitly or add Phase 2 **FR for ASN-matched receiving** |

**Explicitly out of scope (correctly absent):** lot/batch traceability, bin/zone hierarchy, kitting/BOM, VMI/3PL portal, demand forecasting, marketplace integrations — per `project-scope.md`.

---

## 2. Missing User Stories

| Gap | Detail |
|-----|--------|
| **Integration / boundary stories** | No stories for "As an **Order System**, I want to **submit reservation requests**…" or finance sync — only human-role stories exist |
| **Feature-level / epic stories** | 30 features (F-01–F-30) have no epic narratives for release planning or stakeholder demos |
| **Administrator onboarding journey** | FR-011, FR-008, FR-081, FR-090 are scattered; no consolidated "system setup" story chain |
| **Supplier-facing stories** | Actor A-20 (Supplier) appears in F-05 but has no dedicated story |
| **Marketing / commercial actors for F-25** | FR-057/080 are Won't Have but still have US-057/080 — stories exist without committed delivery |

**Coverage check:** US-001–US-090 map 1:1 to FR-001–FR-090. **No missing FR-level stories.**

---

## 3. Missing Acceptance Criteria

| Status | Finding |
|--------|---------|
| **Quantity** | All 90 stories have AC sections (~360 criteria) — structurally complete |
| **Quality gaps** | See table below |

### AC Gaps to Address

| Gap | Example | Recommendation |
|-----|---------|----------------|
| **No business KPI thresholds** | BO-01 (≥95% inquiries via system), BO-02 (≥95% accuracy) absent from AC | Add non-functional AC tags or a separate **Acceptance Test Plan** with measurable targets |
| **Integration scenarios missing** | US-042 reservation has no AC for external order feed failure, duplicate reservation, stale ATP | Add **Integration** category for fulfillment and PO-related stories |
| **Policy-dependent criteria assume decisions** | AC-046-H2 assumes priority rules exist; AC-050-V1 assumes substitute list | Mark as **Conditional AC — pending Q-07, Q-08** or add setup prerequisites |
| **US-003 vs FR-003 mismatch** | AC-003-V1 tests partial **name** search; FR-003 specifies SKU/barcode/identifier | Align FR or AC; remove name search unless FR is expanded |
| **Returns dual-path not distinguished** | US-019 (MVP) and US-065 (Phase 2) AC are nearly identical | Add AC stating MVP path is superseded when F-21 is live; define cutover behavior |
| **Won't Have items still fully specified** | US-057, US-062, US-080 have full AC despite MoSCoW Won't Have | Tag AC as **Deferred — not in current release** to avoid wasted test effort |
| **Cross-story end-to-end flows** | No AC for receive → put-away → ATP → reserve → pick chain | Add **E2E scenario catalog** (5–8 golden paths) referencing multiple US IDs |

---

## 4. Duplicate Requirements

Not all overlap is wrong — some is **layering** (umbrella vs. specific). These need **consolidation or explicit scoping notes**:

| Pair | Relationship | Risk | Recommendation |
|------|--------------|------|----------------|
| **FR-019 ↔ FR-065** | Both cover return physical receipt | Phase 2 duplicate process; teams may build twice | Document FR-019 as **MVP interim**; FR-065 **supersedes** when F-21 ships; single receiving UI |
| **FR-057 ↔ FR-080** | Readiness review vs. readiness alerts | Same business logic evaluated twice | Merge into one FR with notification as behavior, or make FR-080 a thin wrapper referencing FR-057 |
| **FR-016 ↔ FR-020** | Discrepancy resolution vs. tolerance evaluation | Overlapping receipt variance handling | Clarify FR-020 = **automated pre-check**; FR-016 = **human resolution workflow** |
| **FR-029 ↔ FR-015/044/035/060** | Umbrella movement history vs. process-specific movements | FR-029 may be misread as separate feature to build | Reframe FR-029 as **non-functional cross-cutting requirement** enforced by all movement FRs |
| **FR-039 ↔ FR-040 ↔ FR-070** | Shrinkage, obsolescence, overstock analytics | Reporting overlap | Define data ownership: FR-039 = loss by reason; FR-040 = aging/no movement; FR-070 = threshold breach |
| **FR-074 in F-20 and F-22** | Same FR in two features | Planning duplication | Assign **single feature owner** (F-20); F-22 **consumes** report output |
| **FR-076/077/078/079/080 in F-26 plus domain features** | Cross-cutting notifications | Double-counting in sprint planning | Treat F-26 as **capability layer**, not separate delivery increment |

---

## 5. Ambiguous Requirements

| FR / Area | Ambiguity | Clarification Needed |
|-----------|-----------|---------------------|
| **FR-017 vs FR-019** | PO mandatory for supplier receipts vs. non-PO inbound allowed | Define **exception matrix**: who authorizes, which reason codes, audit treatment |
| **FR-018 (Put-away)** | Received stock excluded from ATP until put-away | Does **cross-docking** bypass put-away? Domain knowledge flags tension with cross-dock standard |
| **FR-024 (ATP formula)** | Rules scattered across FR-025, FR-038, FR-018, FR-056, FR-057 ring-fence | Add **ATP calculation definition** appendix listing all exclusions |
| **FR-046** | Backorder priority "per policy" undefined | Resolve Q-07; specify default if policy absent |
| **FR-050** | Substitute approval and acceptable alternates undefined | Resolve Q-08; link to substitute master FR |
| **FR-048** | Split fulfillment coordination steps incomplete (WG-06) | Define minimum coordination: allocation plan, ship sequence, CS visibility |
| **FR-012 vs FR-008/037** | Governance policies vs. operational threshold config | Clarify **single source of truth** — are thresholds in FR-008 or FR-012? |
| **FR-010 vs FR-090** | Opening balance manual vs. import | Define whether FR-090 replaces FR-010 workflow or extends it |
| **FR-084** | Segregation when teams are too small (WG-08) | AC-084-V1 covers exception; **FR-084 body does not** — align FR text with AC |
| **FR-049** | Order status without order creation FR | Define minimum order record the IMS owns vs. receives from external system |
| **FR-022** | Supplier performance without supplier master | Define how supplier identity is keyed and maintained |

**18 domain clarification questions** (domain analysis review) remain largely **unresolved in FR text** — requirements inherit ambiguity from discovery.

---

## 6. Conflicting Requirements

| Conflict | Documents Involved | Impact |
|----------|-------------------|--------|
| **Phase tag vs MoSCoW** | FR-057, FR-062, FR-080 tagged **Phase 3** in FR doc; MoSCoW = **Won't Have** | Delivery teams may plan Phase 3 work that PO has deferred |
| **FR-050 phase** | FR doc = Phase 3; MoSCoW = **Could Have**; F-13 = Phase 2 | Feature and FR prioritization disagree |
| **F-25 priority vs content** | F-25 = Medium P3; contains Won't Have FR-057/080 | Feature catalog misleads roadmap |
| **Put-away vs cross-dock availability** | FR-018 vs industry cross-dock practice | Operations conflict at receiving |
| **Safety stock vs reservation** | FR-056 blocks reservation; FR-042 reserves freely above threshold | Unclear whether safety stock is hard block or soft warning |
| **Strict PO (FR-017) vs ad-hoc receipt (FR-019, MVP scope)** | MVP allows ad-hoc receipts | Receiving clerks may bypass PO controls inconsistently |
| **Reservation display (FR-025) depends on FR-042** | MoSCoW lists FR-025 Must Have, FR-042 Must Have — circular dependency noted | Sequencing risk if reservation UI built before reservation process |
| **Marketing in scope via FR-057/080 vs CRM out of scope** | Project scope excludes marketing campaigns engine | Campaign readiness is inventory-adjacent but needs explicit **in/out boundary** |

---

## 7. Recommendations

### Priority 1 — Before Sprint Planning (Blocking)

1. **Publish a Requirements Errata** reconciling Phase tags, MoSCoW, and feature priorities — one authoritative column per FR.
2. **Resolve the 5 blocking clarification questions** from domain analysis (Q-07 backorder priority, Q-08 substitution, Q-13 PO mandatory rules, Q-25 approval thresholds, Q-37 lot/batch at MVP).
3. **Add integration boundary FR(s)** for order intake and minimum order data — even as a thin "assumption" FR documenting what the external order system must provide.
4. **Document supersession rules** for FR-019→FR-065 and FR-057→FR-080 to eliminate duplicate build risk.
5. **Add ATP Calculation Definition** appendix — single business rule document referenced by FR-024, FR-018, FR-025, FR-038, FR-056.

### Priority 2 — Strengthen Backlog Quality

6. **Split F-17** — extract **Reference Data & Reason Codes** (FR-011) from Adjustments; add supplier/substitute/UoM when approved.
7. **Create E2E acceptance scenario catalog** (8 golden paths): go-live, receive-to-ATP, order fulfillment, count-to-adjust, transfer in-transit, return disposition, replenishment alert-to-PO, audit review.
8. **Tag deferred AC** on FR-057, FR-062, FR-080 as out of current release.
9. **Add integration AC category** to US-041, US-042, US-044, US-049.
10. **Align US-003 AC** with FR-003 scope (identifier lookup only, or expand FR).

### Priority 3 — Maturity and Traceability

11. **Build RTM**: FR → Feature → US → AC → BP → MoSCoW → Dependency Wave → Test Case.
12. **Add policy configuration FRs** (or expand FR-012) for backorder priority, substitution rules, receiving tolerances, SOD exceptions.
13. **Reclassify FR-029** as cross-cutting quality attribute rather than standalone deliverable.
14. **Rename or re-scope F-25** to "Deferred — Commercial Alignment" matching Won't Have status.
15. **Schedule requirements workshop** for the remaining 13 non-blocking clarification questions before Phase 2 FRs enter development.

---

## 8. Proposed Requirements Errata (Draft)

| FR | Current Phase (FR Doc) | MoSCoW | Feature Priority | Recommended Authoritative Status |
|----|------------------------|--------|------------------|----------------------------------|
| FR-050 | Phase 3 | Could Have | F-13 High P2 | **Could Have — Phase 3** (align feature catalog to Phase 3) |
| FR-057 | Phase 3 | Won't Have | F-25 Medium P3 | **Won't Have — defer to future program** |
| FR-062 | Phase 3 | Won't Have | F-09 Medium P3 | **Won't Have — defer to future program** |
| FR-080 | Phase 3 | Won't Have | F-25/F-26 | **Won't Have — defer with FR-057** |
| FR-019 | MVP | Must Have | F-05 Critical P1 | **MVP interim — superseded by FR-065 in Phase 2** |
| FR-084 | MVP | Must Have | F-28 Critical P1 | **Update FR body to include small-team SOD exception (match AC-084-V1)** |

---

## 9. Related Artifacts

| Artifact | Location |
|----------|----------|
| Functional Requirements | `Functional Requirements/functional-requirements.md` |
| Feature Catalog | `Functional Requirements/feature-catalog.md` |
| User Stories | `Functional Requirements/user-stories.md` |
| Acceptance Criteria | `Functional Requirements/acceptance-criteria.md` |
| MoSCoW Prioritization | `Functional Requirements/moscow-prioritization.md` |
| Dependency Analysis | `Functional Requirements/requirements-dependency-analysis.md` |
| Project Scope | `businsess discovery/project-scope.md` |
| Domain Analysis Review | `business domain/domain-analysis-review-report.md` |
| Domain Knowledge Review | `Domain Knowledge/domain-knowledge-review-report.md` |

---

*End of Requirements Quality Review Document*
