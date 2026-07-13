# IMS Implementation Risk Register

| Attribute | Detail |
|-----------|--------|
| **Document ID** | IMPL-RISK-001 |
| **Perspective** | Technical Lead |
| **Date** | July 12, 2026 |
| **Based on** | Feature Implementation Plans, Dependency Map, Sprint Plan, Checklists, Gap Analysis, API Design Review |
| **Audience** | EM, PO, architects, delivery developer(s) |
| **Status** | Active — review at each sprint planning |

---

## 1. Purpose

Identify implementation risks that can undermine delivery of the Inventory Management System Feature Features **F-01–F-30**, and define mitigations tied to specific features.

### Scales

| Field | Scale |
|-------|--------|
| **Probability** | Low · Medium · High |
| **Impact** | Low · Medium · High · Critical |
| **Risk score** | Probability × Impact (qualitative: watch / manage / escalate) |

| Score band | Action |
|------------|--------|
| High × Critical / High × High | Escalate; mitigate before dependent sprints |
| Medium × High / High × Medium | Active mitigation in sprint plan |
| Low × * / Medium × Medium | Monitor; mitigate opportunistically |

---

## 2. Executive Risk Summary

| # | Top risks | Category | P | I | Primary features |
|---|-----------|----------|---|---|------------------|
| R-T01 | Concurrent reservation / stock race → oversell | Technical | High | Critical | F-10, F-11, F-04 |
| R-A01 | ATP consistency boundary violated across modules | Architecture | Medium | Critical | F-04, F-05, F-06, F-10 |
| R-I01 | API gaps C-01/C-03/C-04 block UI workflows | Integration | High | High | F-11, F-20, F-21 |
| R-L01 | Solo DDD/Modulith/Angular facade learning curve | Learning | High | High | All (esp. F-27→F-04) |
| R-S01 | Solo 20-sprint MVP schedule overrun | Schedule | High | High | MVP set F-01–F-30 slices |

**Overall posture:** Specs are strong; **execution risk is high** because readiness is ~18%, API contracts have known gaps, and the sprint plan assumes one FTE across all layers.

---

## 3. Technical Risks

### R-T01 — Stock concurrency / oversell

| Field | Detail |
|-------|--------|
| **1. Description** | Multiple reservations, picks, receipts, or transfers mutate the same `stock_positions` row without correct optimistic locking, idempotency, or transactional boundaries — producing negative ATP or double allocation. |
| **2. Probability** | **High** |
| **3. Impact** | **Critical** — breaks BO-06 fill rate and trust in F-04 visibility |
| **4. Mitigation strategy** | Require optimistic `version` on stock_positions; make `Idempotency-Key` mandatory on reservation/ship/transfer APIs (API review SEC-02); add concurrency tests in F-10/F-11 DoD; single writer = M-04 Stock Position for qty mutations. |
| **5. Related feature** | **F-10**, **F-11**, **F-04**, **F-08**, **F-05** |

---

### R-T02 — Received vs available timing bugs

| Field | Detail |
|-------|--------|
| **1. Description** | Stock becomes sellable ATP on verify instead of after put-away (or the inverse), so pickers cannot find goods or ATP understates inventory. |
| **2. Probability** | **Medium** |
| **3. Impact** | **High** |
| **4. Mitigation strategy** | Encode received/available states in domain; automate FAC-06-X1; document invariant in F-05/F-06 plans; reject early “ATP on dock” shortcuts. |
| **5. Related feature** | **F-05**, **F-06**, **F-04**, **F-10** |

---

### R-T03 — Freeze enforcement incomplete

| Field | Detail |
|-------|--------|
| **1. Description** | Physical count freeze (F-15) is not checked consistently on receive/ship/transfer/adjust endpoints, allowing mutations during wall-to-wall count. |
| **2. Probability** | **Medium** |
| **3. Impact** | **High** |
| **4. Mitigation strategy** | Central `LocationFreezeService` consulted by all mutators; integration test matrix (F-05/F-08/F-11/F-17 vs freeze); freeze banner on UI. |
| **5. Related feature** | **F-15**, **F-05**, **F-08**, **F-11**, **F-17** |

---

### R-T04 — Blind count leakage

| Field | Detail |
|-------|--------|
| **1. Description** | Cycle count UI or API accidentally returns system on-hand to the counter, invalidating blind-count controls (BR accuracy). |
| **2. Probability** | **Medium** |
| **3. Impact** | **Medium** |
| **4. Mitigation strategy** | Separate counter DTO without expected qty; role-based response shaping; FAC-14-V3 automated UI assertion. |
| **5. Related feature** | **F-14**, **F-16** |

---

### R-T05 — Import / opening balance data corruption

| Field | Detail |
|-------|--------|
| **1. Description** | Bulk import upserts partial rows, creates orphan openings for unknown SKUs, or activates locations with unverified balances — poisoning go-live trust (BR-06). |
| **2. Probability** | **Medium** |
| **3. Impact** | **Critical** |
| **4. Mitigation strategy** | Staging batch + row-level validation; all-or-nothing or explicit partial report; SoD on approve; production F-30 only after Sprint 19 golden paths; dry-run mode. |
| **5. Related feature** | **F-30**, **F-01**, **F-02**, **F-04** |

---

### R-T06 — Idempotent retry double-posts

| Field | Detail |
|-------|--------|
| **1. Description** | Client retries on timeout create duplicate receipts, shipments, or transfers because idempotency is optional. |
| **2. Probability** | **Medium** |
| **3. Impact** | **High** |
| **4. Mitigation strategy** | Require Idempotency-Key on mutating POSTs; store key→result; E2E retry tests for F-05 verify and F-11 ship. |
| **5. Related feature** | **F-05**, **F-11**, **F-08**, **F-10** |

---

### R-T07 — Frontend scaffold debt slows real features

| Field | Detail |
|-------|--------|
| **1. Description** | 48 cloned page scaffolds, stub components, no HttpClient/facades — every feature pays rewrite tax (gap ~18% readiness). |
| **2. Probability** | **High** |
| **3. Impact** | **High** |
| **4. Mitigation strategy** | Sprint 1–2 platform: HTTP, interceptors, ScreenScaffold, feature facades; implement components just-in-time per vertical slice (per readiness report). |
| **5. Related feature** | **F-27** (enabler), then all UI features |

---

### R-T08 — Audit trail mutability or missing movements

| Field | Detail |
|-------|--------|
| **1. Description** | App role can UPDATE/DELETE audit rows, or mutators forget to append movements — defeating F-29 and auditor trust. |
| **2. Probability** | **Medium** |
| **3. Impact** | **High** |
| **4. Mitigation strategy** | DB REVOKE UPDATE/DELETE; domain event → MovementAppendService mandatory in mutator DoD; FAC-29-E1 test. |
| **5. Related feature** | **F-29**, **F-05**, **F-17**, **F-11**, **F-08** |

---

## 4. Architecture Risks

### R-A01 — Split-brain ATP (multiple qty writers)

| Field | Detail |
|-------|--------|
| **1. Description** | Fulfillment, inbound, or transfer modules update quantities directly instead of through Stock Position (M-04), causing divergent on-hand/reserved/ATP. |
| **2. Probability** | **Medium** |
| **3. Impact** | **Critical** |
| **4. Mitigation strategy** | Modulith ArchUnit rules: only M-04 mutates stock qty; other modules emit commands/events; code review checklist on F-05/F-10/F-11/F-08. |
| **5. Related feature** | **F-04**, **F-05**, **F-06**, **F-10**, **F-11**, **F-08**, **F-17** |

---

### R-A02 — Cross-module transaction coupling

| Field | Detail |
|-------|--------|
| **1. Description** | Long DB transactions spanning PO + receipt + stock + alert violate “one transaction, one aggregate” and create deadlocks/timeouts. |
| **2. Probability** | **Medium** |
| **3. Impact** | **High** |
| **4. Mitigation strategy** | Saga/outbox for cross-aggregate flows (reservation, transfer, receipt→position→alert); keep local transactions short; Spring Modulith events. |
| **5. Related feature** | **F-10**, **F-05**, **F-08**, **F-20**, **F-26** |

---

### R-A03 — SoD enforced only in UI

| Field | Detail |
|-------|--------|
| **1. Description** | Approval screens hide buttons but APIs accept self-approval — control failure under API/scripts. |
| **2. Probability** | **Medium** |
| **3. Impact** | **Critical** (audit/compliance) |
| **4. Mitigation strategy** | Server-side API-031 on every approve; UI is secondary; FAC-16/17/08 SoD API tests mandatory. |
| **5. Related feature** | **F-28**, **F-16**, **F-17**, **F-08** |

---

### R-A04 — Location scope bypass

| Field | Detail |
|-------|--------|
| **1. Description** | Queries filter in UI only; backend returns all locations — data leak across sites. |
| **2. Probability** | **Medium** |
| **3. Impact** | **High** |
| **4. Mitigation strategy** | Mandatory location-scope filter in query services (API-149); never trust client location list; FAC-04-P3 tests. |
| **5. Related feature** | **F-27**, **F-04**, **F-05**, **F-22**, **F-26** |

---

### R-A05 — Feature build order violated

| Field | Detail |
|-------|--------|
| **1. Description** | Delivery pressure causes F-11 before F-10/F-04, F-20 before F-03, or production F-30 before golden paths — known anti-patterns. |
| **2. Probability** | **Medium** |
| **3. Impact** | **High** |
| **4. Mitigation strategy** | EM/TL gate: sprint goals must match IMPL-DEP-001 sequence; PO cannot pull Phase 2 into MVP without waiver. |
| **5. Related feature** | All; especially **F-04**, **F-10**, **F-11**, **F-03**, **F-20**, **F-30** |

---

### R-A06 — Modular monolith module bleed

| Field | Detail |
|-------|--------|
| **1. Description** | Shared JPA entities / package cycles erode M-01–M-13 boundaries, making later extraction and testing harder. |
| **2. Probability** | **Medium** |
| **3. Impact** | **Medium** |
| **4. Mitigation strategy** | Spring Modulith + ArchUnit in CI from Sprint 2; publish language IDs only across modules. |
| **5. Related feature** | Platform + **F-01–F-11** early modules |

---

### R-A07 — Intelligence read models stale/wrong

| Field | Detail |
|-------|--------|
| **1. Description** | Dashboard/alert projections (M-13) diverge from transactional stock because events are missing or async lag is undocumented. |
| **2. Probability** | **Medium** |
| **3. Impact** | **Medium** |
| **4. Mitigation strategy** | Define freshness SLA; prefer sync query for ATP hot path; event-driven for alerts/dashboard with “as of” timestamp on UI. |
| **5. Related feature** | **F-22**, **F-26**, **F-20**, **F-04** |

---

## 5. Integration Risks

### R-I01 — Known API contract gaps (C-01, C-03, C-04)

| Field | Detail |
|-------|--------|
| **1. Description** | Missing/incorrect pick queue (C-01), requisition list (C-03), and dual return receipt paths (C-04) block or confuse F-11/F-20/F-21 UI. |
| **2. Probability** | **High** (already identified) |
| **3. Impact** | **High** |
| **4. Mitigation strategy** | Close C-01 before F-11 polish; C-03 before F-20 requisitions; designate API-128 canonical before F-21; track as explicit checklist tasks. |
| **5. Related feature** | **F-11**, **F-20**, **F-21** |

---

### R-I02 — Zero HttpClient / no backend yet

| Field | Detail |
|-------|--------|
| **1. Description** | Frontend consumes 0/178 APIs; backend may not exist in-repo — first sprints are greenfield integration, not feature polish. |
| **2. Probability** | **High** |
| **3. Impact** | **High** |
| **4. Mitigation strategy** | Sprint 1 platform spike: Boot app + Flyway + one protected GET; contract-first OpenAPI; don’t schedule feature UI until auth+HTTP works. |
| **5. Related feature** | **F-27**, then all features |

---

### R-I03 — IdP / OIDC contract ambiguity

| Field | Detail |
|-------|--------|
| **1. Description** | Session is IdP-owned (API-173) but login UX/token refresh/logout-all not fully specified — auth integration stalls F-27. |
| **2. Probability** | **Medium** |
| **3. Impact** | **High** |
| **4. Mitigation strategy** | Publish Frontend Auth Guide (API review GAP-API-10); decide demo IdP vs production OIDC early in Sprint 1; feature-flag local JWT for dev. |
| **5. Related feature** | **F-27**, **F-28** |

---

### R-I04 — Sales/CRM & Finance external integrations

| Field | Detail |
|-------|--------|
| **1. Description** | Order import (API-081) and finance match (F-24) assume external systems; adapters undefined → blocked UAT with real orders/invoices. |
| **2. Probability** | **Medium** |
| **3. Impact** | **Medium** (MVP can stub; Phase 3 Critical for F-24) |
| **4. Mitigation strategy** | MVP: manual/order create API in IMS; Phase 2/3: ACL adapters; don’t block ship path on CRM. |
| **5. Related feature** | **F-10**, **F-11**, **F-24**, **F-07** |

---

### R-I05 — DTO / OpenAPI drift

| Field | Detail |
|-------|--------|
| **1. Description** | Request/Response DTO docs diverge from implemented controllers → Angular forms break; rework spikes. |
| **2. Probability** | **High** |
| **3. Impact** | **Medium** |
| **4. Mitigation strategy** | Springdoc OpenAPI as CI artifact; generate or validate FE models; checklist DO tasks per feature. |
| **5. Related feature** | All API-bearing features |

---

### R-I06 — Alert/notification outbox failure

| Field | Detail |
|-------|--------|
| **1. Description** | Business transaction commits but alert insert fails (or vice versa) → missed approvals/low-stock signals. |
| **2. Probability** | **Medium** |
| **3. Impact** | **Medium** |
| **4. Mitigation strategy** | Transactional outbox; FAC-26-E2; alerts never block stock commit. |
| **5. Related feature** | **F-26**, **F-20**, **F-17**, **F-16**, **F-08** |

---

### R-I07 — Health/versioning path conflicts

| Field | Detail |
|-------|--------|
| **1. Description** | Conflicting `/api/v1/health` vs `/api/health` (C-02) breaks ops probes and gateway routing. |
| **2. Probability** | **Low** |
| **3. Impact** | **Medium** |
| **4. Mitigation strategy** | ADR in Sprint 1; single canonical health path in all specs. |
| **5. Related feature** | Platform (supports all features) |

---

## 6. Learning Risks

### R-L01 — DDD aggregates + Spring Modulith ramp-up

| Field | Detail |
|-------|--------|
| **1. Description** | Solo developer must learn aggregate boundaries, domain events, and Modulith while delivering — early modules may be anemic CRUD. |
| **2. Probability** | **High** |
| **3. Impact** | **High** |
| **4. Mitigation strategy** | Spike week: Product + StockPosition sample; pair with architecture docs; TL review first 3 features (F-01, F-02, F-04) heavily; postpone “perfect DDD” on F-22 reads. |
| **5. Related feature** | **F-01**, **F-04**, **F-10** (hardest invariants) |

---

### R-L02 — Angular 19 signals + facade architecture

| Field | Detail |
|-------|--------|
| **1. Description** | Gap codebase uses mocks/signals inconsistently; facades/CVA forms unfamiliar → inconsistent FE patterns and rework. |
| **2. Probability** | **High** |
| **3. Impact** | **Medium** |
| **4. Mitigation strategy** | One reference vertical (F-01) as template; copy facade/ApiService pattern; defer NgRx global store. |
| **5. Related feature** | **F-01** (template), then **F-05**, **F-10** |

---

### R-L03 — Inventory domain / BR catalog depth

| Field | Detail |
|-------|--------|
| **1. Description** | 32 business rules (ATP, SoD, freeze, tolerances, FEFO) misapplied by developers without ops domain experience. |
| **2. Probability** | **Medium** |
| **3. Impact** | **High** |
| **4. Mitigation strategy** | BR cheat-sheet per feature in checklist DO tasks; PO walkthrough of golden paths; encode BRs in domain tests, not only docs. |
| **5. Related feature** | **F-04**, **F-05**, **F-10**, **F-15**, **F-28** |

---

### R-L04 — Security (OIDC, RBAC, SoD) breadth

| Field | Detail |
|-------|--------|
| **1. Description** | Permission model (UR roles, location scope, SoD) is complex; incorrect grants cause over/under-privilege. |
| **2. Probability** | **Medium** |
| **3. Impact** | **High** |
| **4. Mitigation strategy** | Start with minimal role set for MVP; expand in F-27/F-28; security test matrix each sprint; deny-by-default. |
| **5. Related feature** | **F-27**, **F-28**, all transactional features |

---

### R-L05 — QA ownership by same developer

| Field | Detail |
|-------|--------|
| **1. Description** | Builder tests own code; FAC coverage thin; escaped defects in concurrency/SoD. |
| **2. Probability** | **High** |
| **3. Impact** | **Medium** |
| **4. Mitigation strategy** | Automate API tests first; PO UAT at Sprint 19/20; require FAC-P and concurrency cases in DoD; optional external review for F-10/F-28. |
| **5. Related feature** | All; critical on **F-10**, **F-28**, **F-30** |

---

## 7. Schedule Risks

### R-S01 — Solo FTE MVP (~20 sprints) slips

| Field | Detail |
|-------|--------|
| **1. Description** | One person owns DB+BE+FE+QA; large features (F-05, F-08, F-11) overrun; 10-month MVP becomes 14–18 months. |
| **2. Probability** | **High** |
| **3. Impact** | **High** |
| **4. Mitigation strategy** | Hard WIP=1; cut scope to Must-Have slices only; use Sprint 19 buffer; escalate for second developer if S1–7 slip >2 sprints. |
| **5. Related feature** | Entire MVP set (**F-01–F-08**, **F-10–F-12**, **F-14–F-17**, **F-20**, **F-22**, **F-26–F-30**) |

---

### R-S02 — Platform stabilization underestimated

| Field | Detail |
|-------|--------|
| **1. Description** | Gap analysis recommended 2–3 sprints architecture stabilization; Sprint 1–2 may be insufficient for auth+HTTP+Flyway+Modulith. |
| **2. Probability** | **Medium** |
| **3. Impact** | **High** |
| **4. Mitigation strategy** | Allow Sprint 0/2.5 if needed; do not start F-01 UI until auth E2E works; track as milestone gate. |
| **5. Related feature** | **F-27**, **F-28** |

---

### R-S03 — Scope creep from Phase 2 into MVP

| Field | Detail |
|-------|--------|
| **1. Description** | Stakeholders pull F-07 PO, F-21 returns, or F-23 KPIs into MVP — delays go-live. |
| **2. Probability** | **High** |
| **3. Impact** | **High** |
| **4. Mitigation strategy** | MoSCoW freeze; PO change control; Phase 2 nav hidden; seeded PO stub for receiving until F-07. |
| **5. Related feature** | **F-07**, **F-21**, **F-23**, **F-24**, **F-09**, **F-25** |

---

### R-S04 — Critical-path length (receive→promise→ship)

| Field | Detail |
|-------|--------|
| **1. Description** | Value stream needs F-27→…→F-05→F-06→F-04→F-10→F-11 (~8+ stages); any slip delays first end-to-end demo. |
| **2. Probability** | **Medium** |
| **3. Impact** | **High** |
| **4. Mitigation strategy** | Protect critical path in sprint goals; demo partial slices early (visibility then receive); parallelize only after F-04. |
| **5. Related feature** | **F-27**, **F-01**, **F-02**, **F-03**, **F-04**, **F-05**, **F-06**, **F-10**, **F-11** |

---

### R-S05 — Go-live cutover (F-30) scheduled too early

| Field | Detail |
|-------|--------|
| **1. Description** | Pressure to load production openings before hardening (Sprint 19) embeds bad data and destroys adoption. |
| **2. Probability** | **Medium** |
| **3. Impact** | **Critical** |
| **4. Mitigation strategy** | Hard gate: no production F-30 until golden paths pass; dual-control approve; rollback plan tested. |
| **5. Related feature** | **F-30**, **F-04**, **F-22** |

---

### R-S06 — Checklist volume (288 tasks) vs capacity

| Field | Detail |
|-------|--------|
| **1. Description** | 288 checklist items across 30 features overwhelm planning; status tracking abandoned; “unknown unknown” work. |
| **2. Probability** | **Medium** |
| **3. Impact** | **Medium** |
| **4. Mitigation strategy** | Pull only P0 tasks for current feature into sprint backlog; update checklist status weekly; don’t track all 288 in daily standups. |
| **5. Related feature** | All (process risk) |

---

### R-S07 — Key-person / burnout

| Field | Detail |
|-------|--------|
| **1. Description** | Single developer illness or burnout stops all delivery; no backup for domain knowledge. |
| **2. Probability** | **Medium** |
| **3. Impact** | **Critical** |
| **4. Mitigation strategy** | Sustainable pace; documentation DO tasks mandatory; cross-train when second hire available; vacation buffer in plan. |
| **5. Related feature** | All |

---

## 8. Risk Matrix (summary)

| ID | Category | Risk | P | I | Priority |
|----|----------|------|---|---|----------|
| R-T01 | Technical | Stock concurrency / oversell | H | C | **Escalate** |
| R-T02 | Technical | Received vs available timing | M | H | Manage |
| R-T03 | Technical | Freeze enforcement gaps | M | H | Manage |
| R-T04 | Technical | Blind count leakage | M | M | Watch |
| R-T05 | Technical | Import/opening corruption | M | C | **Escalate** |
| R-T06 | Technical | Double-post on retry | M | H | Manage |
| R-T07 | Technical | Frontend scaffold debt | H | H | **Escalate** |
| R-T08 | Technical | Audit missing/mutable | M | H | Manage |
| R-A01 | Architecture | Split-brain ATP | M | C | **Escalate** |
| R-A02 | Architecture | Cross-module TX coupling | M | H | Manage |
| R-A03 | Architecture | SoD UI-only | M | C | **Escalate** |
| R-A04 | Architecture | Location scope bypass | M | H | Manage |
| R-A05 | Architecture | Build order violated | M | H | Manage |
| R-A06 | Architecture | Module bleed | M | M | Watch |
| R-A07 | Architecture | Stale intelligence | M | M | Watch |
| R-I01 | Integration | API gaps C-01/03/04 | H | H | **Escalate** |
| R-I02 | Integration | No HTTP/backend yet | H | H | **Escalate** |
| R-I03 | Integration | OIDC ambiguity | M | H | Manage |
| R-I04 | Integration | External CRM/Finance | M | M | Watch |
| R-I05 | Integration | OpenAPI drift | H | M | Manage |
| R-I06 | Integration | Alert outbox failure | M | M | Watch |
| R-I07 | Integration | Health path conflict | L | M | Watch |
| R-L01 | Learning | DDD/Modulith ramp | H | H | **Escalate** |
| R-L02 | Learning | Angular facade patterns | H | M | Manage |
| R-L03 | Learning | Domain BR depth | M | H | Manage |
| R-L04 | Learning | Security model complexity | M | H | Manage |
| R-L05 | Learning | Same-dev QA bias | H | M | Manage |
| R-S01 | Schedule | Solo MVP slip | H | H | **Escalate** |
| R-S02 | Schedule | Platform underestimation | M | H | Manage |
| R-S03 | Schedule | Scope creep | H | H | **Escalate** |
| R-S04 | Schedule | Critical-path length | M | H | Manage |
| R-S05 | Schedule | Early cutover | M | C | **Escalate** |
| R-S06 | Schedule | Checklist overload | M | M | Watch |
| R-S07 | Schedule | Key-person burnout | M | C | **Escalate** |

**Escalate count:** 12 · **Manage:** 15 · **Watch:** 7 · **Total risks:** 34

---

## 9. Feature Heat Map (risk concentration)

| Feature | Elevated risks | Why |
|---------|----------------|-----|
| **F-04** | R-T01, R-A01, R-A04 | ATP source of truth |
| **F-05 / F-06** | R-T02, R-T06, R-A01 | First qty mutators |
| **F-10 / F-11** | R-T01, R-T06, R-I01, R-S04 | Oversell + pick gap C-01 |
| **F-15** | R-T03 | Freeze |
| **F-16 / F-17 / F-08** | R-A03, R-L04 | SoD approvals |
| **F-20 / F-21** | R-I01 | C-03 / C-04 |
| **F-27 / F-28** | R-I02, R-I03, R-L01, R-S02 | Platform critical path |
| **F-29** | R-T08 | Compliance evidence |
| **F-30** | R-T05, R-S05 | Go-live trust |
| **F-22 / F-26** | R-A07, R-I06 | Projections/alerts |

---

## 10. Mitigation Backlog (near-term actions)

| When | Action | Addresses |
|------|--------|-----------|
| Sprint 1 | HTTP + auth + Flyway + health ADR | R-I02, R-I07, R-T07, R-S02 |
| Sprint 1–2 | OIDC/dev JWT decision + Auth guide | R-I03 |
| Sprint 2 | ArchUnit module rules + SoD API-031 | R-A01, R-A03, R-A06 |
| Before F-10 | Idempotency + optimistic locking standard | R-T01, R-T06 |
| Before F-11 polish | Resolve API C-01 | R-I01 |
| Before F-20 requisitions | Resolve API C-03 | R-I01 |
| Before F-21 | Canonicalize API-128 (C-04) | R-I01 |
| Every sprint | P0 checklist only; FAC-P sample | R-S06, R-L05 |
| Sprint 19 gate | Golden paths before F-30 prod | R-S05, R-T05 |
| Ongoing | MoSCoW change control | R-S03, R-A05 |

---

## 11. Review Cadence

| Forum | Frequency | Focus |
|-------|-----------|--------|
| Sprint planning | Every 2 weeks | Risks touching sprint features |
| Mid-sprint check | Day 6 | New blockers (integration/schedule) |
| Release gate (S20/S30) | Per release | Escalate list must be mitigated or waived by PO |

---

## 12. Related Documents

| Document | Path |
|----------|------|
| Feature catalog | `implmention/IMS-Implementation-Features.md` |
| Dependency map | `implmention/IMS-Feature-Dependency-Map.md` |
| Sprint plan | `implmention/IMS-Sprint-Plan.md` |
| Checklists | `implmention/checklists/` |
| Gap / readiness | `gap_frontend/Implementation-Readiness-Report.md` |
| API risks | `SRS/API_Design/API-Design-Architecture-Review.md` |

---

*Technical Lead — Implementation Risk Register IMPL-RISK-001*
