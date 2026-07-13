# Architecture Review Report
## Inventory Management System

---

## Document Information

| Attribute | Detail |
|-----------|--------|
| **Document ID** | SRS-SA-009 |
| **Document Title** | Chief Solution Architect — Complete Architecture Review |
| **Version** | 1.0 |
| **Status** | Final Review — Pre-Database Design Gate |
| **Document Owner** | Chief Solution Architect |
| **Review Date** | July 6, 2026 |
| **Classification** | Internal — Architecture Confidential |
| **Scope** | Holistic review of all SRS System Architecture artifacts (SRS-SA-001 through SRS-SA-008) against domain model, event storming, and NFR suite |

### Artifacts Reviewed

| Document | ID | Version |
|----------|-----|---------|
| Architecture Vision | SRS-SA-001 | 1.0 |
| Architecture Style Recommendation | SRS-SA-002 | 1.0 |
| System Modules Design | SRS-SA-003 | 1.0 |
| Layered Architecture Design | SRS-SA-004 | 1.0 |
| Integration Architecture Design | SRS-SA-005 | 1.0 |
| Cross-Cutting Concerns | SRS-SA-006 | 1.0 |
| Technology Stack Recommendation | SRS-SA-007 | 1.0 |
| Architecture Decision Records | SRS-SA-008 | 1.0 |
| Bounded Contexts | SRS-DM-007 | 1.0 |
| Domain Model Review | SRS-DM-009 | 1.0 |
| Event Storming Hotspots | SRS-ES-007 | 1.0 |
| NFR Review Report | NFR Review | 2026-07-03 |
| System Context | System Context | 1.0 |

### Review Purpose

This report provides a **Chief Solution Architect gate review** of the complete IMS architecture before proceeding to **Database Design**. It assesses coherence, risk, and readiness; identifies gaps and coupling; and delivers actionable recommendations.

---

## 1. Executive Summary

### 1.1 Overall Assessment

| Dimension | Rating | Summary |
|-----------|--------|---------|
| **Strategic alignment** | **Strong** | Architecture directly implements BRD objectives, 13 bounded contexts, and phased 18-month vision |
| **Internal coherence** | **Strong** | Style, modules, layers, integrations, technology, and ADRs are mutually consistent |
| **Domain alignment** | **Amber** | 8 P1 domain findings and 16 open hotspots — 2 Critical block database design |
| **NFR feasibility** | **Amber** | 6 critical NFR conflicts unresolved; capacity baseline not validated |
| **Implementation readiness** | **Amber** | Proceed to database design **conditionally** after gate actions in Section 8 |
| **Long-term evolvability** | **Strong** | Modular monolith, ADRs, ArchUnit, and CQRS provide credible decomposition path |

### 1.2 Gate Decision

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  DATABASE DESIGN GATE:  CONDITIONAL PROCEED                                   │
│                                                                             │
│  Complete Section 8 mandatory actions BEFORE physical data model draft.     │
│  Do NOT finalize Stock Position, freeze, or opening balance schemas         │
│  until ADR-009 and ADR-010 are Accepted.                                    │
└─────────────────────────────────────────────────────────────────────────────┘
```

The architecture is **sound and appropriately ambitious** for a mid-sized distribution organization under budget and IT capacity constraints. The compound style (DDD + modular monolith + events + CQRS + sagas) is the correct long-term choice. The primary risks are **unresolved domain forks** that directly determine database keys and **operational NFR conflicts** that determine data tiering — not structural flaws in the architecture itself.

---

## 2. Architecture Style Review

### 2.1 Decision Under Review

**DDD + Modular Monolith + Clean/Hexagonal internals + Event-Driven integration + CQRS (Intelligence) + Sagas** (ADR-001 through ADR-008, SRS-SA-002).

### 2.2 Strengths

| Strength | Evidence |
|----------|----------|
| **Appropriate complexity level** | 13 contexts, 81 events, 32 rules — DDD is justified, not ceremonial |
| **Budget and ops alignment** | Modular monolith honors BC-01 and ORC-04; microservices correctly deferred |
| **Core domain protection** | Inventory Balance as quantity authority (ADR-004) is consistently reflected across all documents |
| **Decomposition readiness** | Intelligence and integration gateway identified as Phase 2+ extraction candidates |
| **Rejected alternatives documented** | Layered-only and microservices-day-one rejections are well-reasoned |

### 2.3 Concerns

| Concern | Severity | Detail |
|---------|----------|--------|
| **Style compound complexity** | Medium | Teams must simultaneously apply DDD, Clean Architecture, CQRS, sagas, and Modulith — high skill bar; Sprint 0 reference implementation essential |
| **Eventual consistency acceptance** | Medium | Business stakeholders must understand ATP on dashboards may lag seconds behind dock operations — not documented in BRD user-facing terms |
| **Saga compensation gaps** | High | ADR-008 accepted but HS-007 reservation failure policy undefined — architecture assumes compensation without business rules |
| **CQRS scope creep risk** | Medium | jOOQ read side only in Intelligence (ADR-019) — teams may expand CQRS to other modules without ADR |

### 2.4 Style Review Verdict

**Approved.** The architecture style is fit for purpose. No style change recommended. Mitigate complexity through reference module template and architecture guild.

---

## 3. Modules Review

### 3.1 Module Decomposition (M-01 – M-13)

| Assessment | Detail |
|------------|--------|
| **Alignment** | 1:1 mapping to SRS-DM-007 bounded contexts — correct |
| **Ownership** | Aggregate ownership table in SRS-SA-003 is exclusive and traceable |
| **Phasing** | MVP module set (M-01–M-04, M-06–M-07, M-09, M-12–M-13) is deliverable and BRD-aligned |
| **Hub pattern** | M-04 Balance as integration hub is correct but creates availability dependency |

### 3.2 Module-Specific Issues

| Module | Issue | Risk | Recommendation |
|--------|-------|------|----------------|
| **M-04 Balance** | ADR-009 Proposed — identity model undecided | **Critical** for DB design | Accept ADR-009 before Stock Position schema |
| **M-02 Network** | ADR-010 Proposed — freeze authority split | **High** | Accept ADR-010; freeze flag on `inventory_location` table |
| **M-05 Procurement** | Phase 2 module but PO receipt needed MVP | Medium | MVP subset documented but procurement squad may be under-resourced in Phase 1 |
| **M-06 Inbound** | Missing Ad-Hoc Receipt Authorization entity (P1-06) | **High** | Add entity before goods_receipt schema |
| **M-09 Accuracy** | Opening Balance workflow missing (P1-07, HS-002) | **Critical** for go-live | Model Opening Balance aggregate or subprocess before location schema |
| **M-09 Accuracy** | Polymorphic Adjustment Case root (P1-08) | Medium | Single `adjustment_case` table with `case_origin` discriminator |
| **M-12 Identity** | 100 permissions × 19 roles — no permission catalog artifact | Medium | Publish permission enum/registry before authorization schema |
| **M-13 Intelligence** | Read-only module but shares PostgreSQL instance | Low | Acceptable MVP; monitor connection pool contention |

### 3.3 Missing Module Consideration

| Missing Component | Assessment |
|-------------------|------------|
| **Dedicated Integration Gateway module** | Not required for MVP — ACL adapters in Fulfillment and Intelligence suffice. **Recommend** extracting to M-14 in Phase 2 when EXT-01 and EXT-03 APIs activate |
| **Notification module** | Correctly excluded — SVC-02 handled as infrastructure adapter from Intelligence events |
| **Bulk Import module** | UC-046 spans Catalog, Network, Balance — correctly handled as cross-module use case with dedicated import adapter, not separate module |

### 3.4 Modules Review Verdict

**Approved with conditions.** Module boundaries are correct. Two Proposed ADRs and three P1 domain entities must be resolved before physical schema for affected modules.

---

## 4. Layers Review

### 4.1 Layer Model (SRS-SA-004)

| Layer | Assessment |
|-------|------------|
| **Presentation** | Correctly thin — DTOs, syntactic validation, auth middleware only |
| **Application** | Correctly owns transactions, sagas, authorization behaviors |
| **Domain** | Correctly center — no framework dependencies specified |
| **Infrastructure** | Correctly implements ports — JPA, ACL, cache, outbox |

### 4.2 Layer Concerns

| Concern | Severity | Detail |
|---------|----------|--------|
| **JPA anemic domain risk** | **High** | Hibernate in infrastructure must not drive model design — ArchUnit rules (ADR-025) critical; domain review flagged weak behavioral specification |
| **Per-module presentation packages** | Low | 13 modules × REST controllers — ensure consistent API versioning and error contract via shared presentation kernel |
| **Application pipeline ordering** | Medium | Authorization → validation → audit → handler order must be standardized — not documented as fixed pipeline sequence |
| **Shared kernel scope creep** | Medium | `ims-shared-kernel` must stay identifiers + event envelope only — resist shared DTOs or base entities |

### 4.3 CQRS Layer Split

| Path | Assessment |
|------|------------|
| **Command path** | JPA aggregates in transactional modules — correct |
| **Query path** | jOOQ in Intelligence + Redis ATP cache — correct |
| **Risk** | Teams may query JPA write entities from Intelligence for "quick reports" — **prohibit via ArchUnit and code review** |

### 4.4 Layers Review Verdict

**Approved.** Layer placement is sound. Add **shared application pipeline specification** and **behavioral contract templates** for aggregates before implementation.

---

## 5. Integrations Review

### 5.1 Internal Integration (SRS-SA-005)

| Pattern | Assessment |
|---------|------------|
| **Events for state propagation** | Correct — PutAwayCompleted, AdjustmentApproved, etc. |
| **Sync queries for consultation** | Correct — ATP, freeze, eligibility |
| **Sagas for cross-module writes** | Correct — but compensation policies incomplete |
| **Outbox** | Correct — ADR-006 aligns with NFR-REL-007 |
| **Hot-path sync limit (≤2 hops)** | Correct — supports NFR-PERF-002 |

### 5.2 Tight Coupling Identified (Internal)

| Coupling Point | Modules | Severity | Mitigation |
|----------------|---------|----------|------------|
| **M-07 → M-04 reservation saga** | Fulfillment, Balance | **High** (necessary) | Saga + port interface; monitor Balance availability as single point of failure |
| **All modules → M-12 Identity** | All, Identity | Medium (necessary) | Cache permissions with short TTL; Identity module HA |
| **All modules → M-03 Governance** | All, Governance | Medium | Governance read cache; governance outage blocks adjustments — acceptable |
| **M-06 → M-05 PO validation** | Inbound, Procurement | Medium | Event + query port; PO module delay blocks receiving — acceptable MVP |
| **Sync query proliferation** | Multiple | Medium | ArchUnit rule: max 3 injected query ports per handler; prefer events for non-blocking |

### 5.3 External Integration (SRS-SA-005, System Context)

| Integration | MVP Depth | Risk |
|-------------|-----------|------|
| **EXT-01 Sales/CRM** | Manual order entry | Channel overselling until Phase 2 API (BRD risk) |
| **EXT-02 Finance ERP** | File export | Manual reconciliation gap (COM-R-02, TEC-05) |
| **EXT-03 Sales Channel** | None MVP | TEC-04 — no real-time ATP feed |
| **SVC-01 IdP** | Should Have | MVP at risk if SSO not ready — form login fallback needed |
| **HS-014 Finance boundary** | Open | Three-way match schema depends on ERP decision |

### 5.4 Integrations Review Verdict

**Approved for MVP scope.** External integration depth is honestly phased. **Mandatory:** document interim manual sync procedures for CRM and finance before go-live.

---

## 6. Technology Decisions Review

### 6.1 Stack Summary (SRS-SA-007)

| Technology | Mandated | Assessment |
|------------|----------|------------|
| Java 21 + Spring Boot 3 | Yes | Appropriate |
| Spring Modulith | No | Strong fit for ADR-001 |
| Angular 19 + Material | Yes | Appropriate |
| PostgreSQL 16 | Yes | Appropriate |
| Hibernate JPA + jOOQ | No | Appropriate split |
| Redis | No | Required for NFR-PERF-002 |
| Maven multi-module | No | Appropriate |
| Docker | No | Appropriate |

### 6.2 Technology Risks

| Risk | Severity | Detail |
|------|----------|--------|
| **Spring Modulith maturity** | Medium | Smaller reference base — mitigated by ArchUnit backup |
| **JPA aggregate mapping complexity** | **High** | Stock Position with embedded lots, quarantine holds, optimistic locking — most complex mapping in system |
| **Angular + Spring team split** | Medium | OpenAPI contract and shared API review essential |
| **Redis as additional infra** | Low | ORC-04 — managed Redis service recommended over self-hosted |
| **RabbitMQ deferred** | Low | ADR-022 correct; outbox schema must include `published_at` for broker relay |
| **Kubernetes vs PaaS undecided** | Medium | Recommend managed PaaS for MVP to honor ORC-04 |

### 6.3 NFR vs Technology Alignment

| NFR | Technology Support | Gap |
|-----|-------------------|-----|
| NFR-PERF-002 (2s ATP) | Redis + CQRS read | Capacity not validated |
| NFR-BDR-001 (15-min RPO) | PostgreSQL WAL + backup service | Cost vs BC-01 unresolved (C-03) |
| NFR-COM-020 (7-year retention) | PostgreSQL + tiered archive | Tiered architecture not designed — **blocks DB design** |
| NFR-AVL-001 (99.5%) | Single monolith + PaaS | Availability math conflict (C-01) |

### 6.4 Technology Review Verdict

**Approved.** Stack is coherent and mandate-compliant. **Mandatory before DB design:** tiered data architecture decision (hot/warm/cold) per NFR-COM-019 and C-04.

---

## 7. ADR Review

### 7.1 ADR Coverage Assessment

| Area | ADRs | Coverage |
|------|------|----------|
| Deployment & structure | 001–003, 015, 018, 025 | Complete |
| Domain & integration | 004–008, 011, 023 | Complete |
| Pending domain forks | 009, 010 | **Block DB design** |
| External boundaries | 012, 013 | Complete — HS-014 detail deferred |
| Technology | 014, 016–017, 019–022 | Complete |
| Quality | 021, 024 | Complete |

### 7.2 ADR Gaps — Recommended New ADRs

| Proposed ADR | Topic | Priority |
|--------------|-------|----------|
| **ADR-026** | Tiered data retention (hot/warm/cold) | **P1 — before DB design** |
| **ADR-027** | Opening balance and go-live workflow | **P1 — before DB design** |
| **ADR-028** | Ad-hoc receipt authorization model | **P1 — before inbound schema** |
| **ADR-029** | Idempotency key strategy for commands | P2 |
| **ADR-030** | API versioning and compatibility policy | P2 |
| **ADR-031** | Multi-instance deployment and session model | P2 |

### 7.3 ADR Consistency Check

| Check | Result |
|-------|--------|
| ADR-001 (monolith) vs ADR-015 (Modulith) | Consistent |
| ADR-005 (events) vs ADR-022 (in-process MVP) | Consistent |
| ADR-007 (CQRS) vs ADR-019 (jOOQ) | Consistent |
| ADR-009 (Proposed) vs SRS-SA-003 Balance module | **Inconsistent until Accepted** |
| ADR-010 (Proposed) vs SRS-SA-003 Network module | **Inconsistent until Accepted** |
| ADR-011 (campaign events) vs ADR-004 (balance authority) | Consistent |

### 7.4 ADR Review Verdict

**25 ADRs provide strong decision traceability.** Three new ADRs required before database design. Accept ADR-009 and ADR-010 via workshop.

---

## 8. Cross-Cutting Concerns Review

### 8.1 Placement Assessment (SRS-SA-006)

| Concern | Placement | Assessment |
|---------|-----------|------------|
| Authentication | Infrastructure + Presentation | Correct |
| Authorization | Application | Correct |
| Logging | Infrastructure | Correct |
| Exception handling | Presentation + Application | Correct |
| Validation | Three-tier (Presentation/Application/Domain) | Correct |
| Auditing | Intelligence projection | Correct |
| Caching | Infrastructure (Redis) | Correct |
| Transactions | Application (UoW) | Correct |
| Configuration | Infrastructure | Correct — governance thresholds in M-03 not config |
| Localization | Presentation | Correct |

### 8.2 Cross-Cutting Gaps

| Gap | Severity | Recommendation |
|-----|----------|----------------|
| **No idempotency standard** | **High** | Define `Idempotency-Key` header for receipt, reservation, adjustment commands — critical for warehouse retry and mobile flaky network |
| **No API error contract standard** | Medium | Publish RFC 7807 Problem Details schema shared across modules |
| **Pipeline behavior order not fixed** | Medium | Document: Auth → Idempotency → Validation → Audit → Handler |
| **GDPR vs 7-year audit conflict** | **High** | Legal matrix (C-05) not published — affects PII columns in user and audit tables |
| **No rate limiting specification** | Medium | ATP inquiry endpoint needs per-user rate limit — NFR missing |
| **Correlation ID end-to-end** | Low | Specified but Angular client propagation not documented |

### 8.3 Cross-Cutting Review Verdict

**Approved with gaps.** Add idempotency and error contract standards before API and database design.

---

## 9. Risk Register (Consolidated)

### 9.1 Critical Risks (Block or Condition Database Design)

| Risk ID | Risk | Source | Impact |
|---------|------|--------|--------|
| **AR-C01** | Stock Position identity undecided (ADR-009 Proposed) | HS-005, P1-05 | Wrong primary key design — expensive rework |
| **AR-C02** | Opening balance workflow undefined (HS-002) | P1-07 | Location go-live schema incomplete |
| **AR-C03** | Tiered data architecture not designed | NFR C-04, COM-019 | Audit/movement tables grow unbounded in hot DB |
| **AR-C04** | Reservation saga compensation undefined | HS-007 | order_line vs reservation state inconsistency |
| **AR-C05** | Ad-hoc receipt entity missing | HS-001, P1-06 | goods_receipt schema incomplete for BR-007 |

### 9.2 High Risks

| Risk ID | Risk | Source | Impact |
|---------|------|--------|--------|
| **AR-H01** | M-04 Balance single point of failure and contention | ADR-004 | Availability and performance under peak |
| **AR-H02** | JPA anemic domain + weak behavioral spec | SRS-DM-009 | Business rules not enforced in aggregates |
| **AR-H03** | NFR availability math conflict (C-01) | NFR Review | False acceptance testing |
| **AR-H04** | 15-min RPO vs fixed budget (C-03) | NFR Review | Backup architecture under-funded |
| **AR-H05** | Finance ERP boundary open (HS-014) | SRS-ES-007 | supplier_invoice and match tables scope unclear |
| **AR-H06** | Modular monolith boundary erosion | AR-09 | Gradual coupling over 18 months |
| **AR-H07** | Channel overselling until Phase 2 integration | TEC-04 | Revenue and trust risk |
| **AR-H08** | Redis cache invalidation failure | ADR-021 | Overselling on stale ATP |

### 9.3 Medium Risks

| Risk ID | Risk | Source |
|---------|------|--------|
| **AR-M01** | Spring Modulith learning curve | ADR-015 |
| **AR-M02** | CQRS projection lag on dashboards | ADR-007 |
| **AR-M03** | Supplier entity domain doc misalignment | P1-01 |
| **AR-M04** | Missing integration NFRs | NFR Review §4.3 |
| **AR-M05** | Capacity baseline not validated | NFR Review §4.4 |
| **AR-M06** | PWA scanner hardware limitations | ADR-016 |
| **AR-M07** | Outbox table growth without archival | ADR-006 |
| **AR-M08** | Permission model complexity (100 permissions) | FR-081–090 |

---

## 10. Scalability Concerns

| Concern | Horizon | Analysis | Mitigation |
|---------|---------|----------|------------|
| **Stock Position write contention** | MVP–Phase 2 | Product-location aggregate with optimistic locking — correct granularity; Class A SKU peak may exhaust retries | Retry with backoff; partition by location in application routing; Redis read offload |
| **PostgreSQL vertical limit** | Phase 2–3 | Single instance scales to mid-size distribution; 30% growth (NFR-SCAL-001) achievable with tuning | Read replica for Intelligence; connection pool per module |
| **Monolith horizontal scaling** | Phase 2 | Multiple app instances require sticky-less design — JWT supports this; Redis cache shared; in-process events **do not scale across instances** without broker | ADR-022 Phase 2 broker migration trigger: >1 app instance OR external integration |
| **Audit/movement table growth** | 7 years | Millions of rows per NFR-COM-020 — hot PostgreSQL unsustainable | **Tiered architecture mandatory** — partition by month; archive to warm/cold store |
| **Intelligence query load** | Phase 3 | Month-end KPI queries may contend with OLTP on shared PostgreSQL | Extract Intelligence read DB or replica; jOOQ on separate connection pool |
| **Multi-location rollout** | MVP | Sequential rollout (OC-01) reduces blast radius — architecture supports per-location feature flags | Location-scoped configuration in M-02 master data |

---

## 11. Security Concerns

| Concern | Severity | Detail | Recommendation |
|---------|----------|--------|----------------|
| **JWT token revocation** | High | Deprovisioned user retains access until TTL expires | Short access token (15 min) + refresh; maintain blocklist in Redis for immediate revoke |
| **Location-scoped RBAC complexity** | High | 100 permissions × location matrix — misconfiguration risk | Permission registry artifact; automated SoD tests; role assignment approval workflow |
| **SoD enforcement at two layers** | Medium | M-12 at assignment, M-03 at command — must be consistent | Integration tests for all 20 SoD rules |
| **ACL input validation** | High | CRM order import could inject malformed SKU or negative quantities | Strict ACL validation before `ImportCustomerOrder` command |
| **Audit trail immutability** | High | Append-only projection must resist UPDATE/DELETE | DB permissions: Intelligence read tables INSERT-only for app role |
| **Secrets in configuration** | Medium | SVC-07 required | Vault integration from day one — no secrets in Git |
| **GDPR PII in audit logs** | High | User names in audit trail vs erasure rights (C-05) | Legal matrix before user table design |
| **Warehouse shared devices** | Medium | Physical device session sharing risk | Short session timeout; re-auth for high-risk actions (NFR-SEC-004) |
| **API rate limiting** | Medium | ATP endpoint abuse or scraping | Rate limit per user/IP on read APIs |
| **Test data in non-prod** | Medium | No environment governance NFR | Masked production subset; no real customer PII in dev |

---

## 12. Maintainability Issues

| Issue | Impact | Recommendation |
|-------|--------|----------------|
| **13 modules × 4 layers = 52 packages** | Navigation complexity | Reference module template; architecture guild; CODEOWNERS per module |
| **81 domain events versioning** | Breaking changes break projections | Event schema registry; upcasters for Intelligence projections |
| **Dual data access (JPA + jOOQ)** | Two patterns to maintain | Confine jOOQ to `ims-intelligence-infrastructure` only |
| **Saga state persistence** | Debugging and recovery | `saga_instance` table with correlation ID — include in database design |
| **Flyway per-module migrations** | Coordination on shared kernel changes | Migration dependency order documented; shared kernel migrations in parent |
| **OpenAPI contract drift** | Angular/Spring desync | CI contract test; generate TypeScript client from OpenAPI |
| **Behavioral specification gap** | Anemic aggregates | Aggregate behavior specification document before coding Balance module |
| **16 open hotspots** | Latent design debt | Hotspot resolution tracker linked to ADRs |

---

## 13. Missing Components

### 13.1 Architecture Artifacts Missing

| Component | Priority | Required Before |
|-----------|----------|-----------------|
| **Tiered data architecture specification** | P1 | Database design |
| **Capacity model / baseline workbook** | P1 | Index strategy, partitioning |
| **Permission and role registry** | P1 | Identity schema |
| **Event schema catalog (versioned)** | P1 | Outbox and projection tables |
| **Saga compensation specification (SAG-01)** | P1 | Order and reservation tables |
| **Opening balance workflow model** | P1 | Location and balance schema |
| **Ad-hoc receipt authorization model** | P1 | Goods receipt schema |
| **API error contract standard** | P2 | REST design |
| **Idempotency key standard** | P2 | Command tables |
| **NFR traceability matrix (204 requirements)** | P2 | Test planning |
| **Integration NFR supplement** | P2 | Phase 2 integration design |
| **Primary Locations Register** | P1 | Location schema seed data |
| **Data classification register** | P1 | Column-level security design |
| **Privacy vs audit retention matrix** | P1 | User and audit tables |
| **Reference architecture spike output** | P1 | Squad onboarding |

### 13.2 Runtime Components Missing (Phase 2+)

| Component | When Needed |
|-----------|-------------|
| Message broker (RabbitMQ) | Phase 2 external integration |
| Integration gateway module (M-14) | Phase 2 CRM/channel APIs |
| Read replica or Intelligence extract DB | Phase 3 reporting scale |
| API gateway (rate limiting, WAF) | Multi-instance production |
| Data archive / cold storage service | Year 2+ audit retention |

---

## 14. Recommendations — Pre-Database Design Gate

### 14.1 Mandatory Actions (Gate Blockers)

Complete these **before** drafting physical data model:

| # | Action | Owner | Deliverable | Blocks |
|---|--------|-------|-------------|--------|
| G-01 | **Accept ADR-009** — Stock Position per product-location with lot child entities | Solution Architect + Warehouse/Quality | Updated ADR-009 status = Accepted | `stock_position`, `lot_batch` tables |
| G-02 | **Accept ADR-010** — Freeze initiator vs holder split | DDD Architect | Updated ADR-010 + integration contract | `inventory_location.freeze_flag` |
| G-03 | **Define Opening Balance workflow** — aggregate or subprocess (HS-002) | Inventory Controller + BA | ADR-027 + domain update | Location go-live, balance initialization |
| G-04 | **Define Ad-Hoc Receipt Authorization** (HS-001) | Senior BA + Finance | ADR-028 + entity in domain model | `goods_receipt` schema |
| G-05 | **Design tiered data architecture** (hot/warm/cold) | Solution Architect + DBA | ADR-026 + retention mapping | Movement, audit, outbox tables |
| G-06 | **Publish saga compensation spec for SAG-01** (HS-007) | Operations Director + Architect | Saga state diagram + compensation table | `customer_order`, reservation coordination |
| G-07 | **Resolve NFR conflict C-01** (availability math) | Solution Architect + QA | Harmonized SLA register | Non-functional — informs HA design |
| G-08 | **Publish permission registry** (100 permissions) | Product Owner + Security | `permissions.yaml` or equivalent | `role_assignment` schema |
| G-09 | **Legal sign-off on C-05** (GDPR vs audit retention) | Legal + Internal Audit | Privacy/audit matrix | `user_account`, audit projection columns |
| G-10 | **Sprint 0 reference module spike** (Catalog or Governance) | Tech Lead | Working Modulith module with all 4 layers | Validates stack before Balance complexity |

### 14.2 Strongly Recommended (Parallel with Database Design)

| # | Action | Owner |
|---|--------|-------|
| R-01 | Create versioned **event schema catalog** linking DE-001–DE-081 to outbox payload types | DDD Architect |
| R-02 | Add **`saga_instance`** and **`idempotency_key`** tables to database design scope | Solution Architect |
| R-03 | Define **PostgreSQL partitioning strategy** for `inventory_movement` and `audit_trail` (monthly range) | DBA |
| R-04 | Plan **Optimistic lock (`version` column)** on all aggregate root tables | DBA + Tech Lead |
| R-05 | Document **schema-per-module naming convention** and shared kernel exception list | DBA |
| R-06 | Resolve **HS-014** finance boundary workshop — even if MVP stays manual export | CFO + Architect |
| R-07 | Publish **aggregate behavior specification** for Stock Position and Goods Receipt | Domain Expert |
| R-08 | Align **SRS-DM-003** with SRS-DM-007 (Supplier placement, Adjustment Case root) | DDD Architect |
| R-09 | Add **integration NFR supplement** for TEC-04/TEC-05 manual process SLAs | Solution Architect |
| R-10 | Define **RFC 7807 error contract** for all REST APIs | Tech Lead |

### 14.3 Database Design Scope Guidance

When gate actions are complete, database design should proceed in this order:

```
Phase A — Shared kernel & platform
  └── published identifiers, event envelope, outbox, saga, idempotency

Phase B — Master data modules (low coupling)
  └── M-01 Catalog, M-02 Network, M-03 Governance, M-12 Identity

Phase C — Core domain (after G-01, G-05, G-06)
  └── M-04 Balance (stock_position, stock_policy, lot_batch, quarantine_hold)

Phase D — Operational modules
  └── M-06 Inbound (after G-04), M-07 Fulfillment, M-09 Accuracy (after G-02, G-03)

Phase E — Read side
  └── M-13 Intelligence projections (partitioned movement, audit, KPI)

Phase F — Phase 2 modules
  └── M-05 Procurement, M-08 Transfer, M-10 Returns, M-11 Campaign
```

### 14.4 What Database Design Must Encode

| Architectural Decision | Database Expression |
|------------------------|---------------------|
| ADR-004 sole ATP mutator | Only `balance` schema has `on_hand`, `reserved`, `quarantined` columns |
| ADR-006 outbox | `platform.outbox_event` table with `published_at`, `event_id` unique |
| ADR-018 schema-per-module | PostgreSQL schemas: `catalog`, `network`, `balance`, etc. |
| ADR-009 product-location identity | `stock_position` PK = `(product_sku, location_code)` |
| ADR-021 Redis cache | No ATP duplicated as source of truth in DB — cache is derivative |
| ADR-024 centralized audit | `intelligence.audit_trail` append-only; no per-module audit tables |
| MB-07 no cross-module FKs | Reference by identifier only; no FK from `fulfillment` to `balance` tables |
| Optimistic locking | `version` column on all aggregate roots |
| 7-year retention | Partitioning + archive policy on movement and audit tables |

---

## 15. Architecture Strengths Summary

The IMS architecture demonstrates **mature strategic design** uncommon in mid-market initiatives:

1. **Honest phasing** — MVP scope, manual integrations, and broker deferral match BC-01 and ORC-04
2. **Consistent quantity authority** — ADR-004 threaded through every document
3. **Decision traceability** — 25 ADRs provide durable rationale
4. **Enforceable boundaries** — Spring Modulith + ArchUnit + schema-per-module
5. **Performance-aware** — CQRS, Redis, and jOOQ split protect the write path
6. **Compliance-ready structure** — centralized audit projection and append-only design
7. **Domain-first** — 13 modules mirror approved bounded contexts, not technical convenience

---

## 16. Final Gate Verdict

| Question | Answer |
|----------|--------|
| Is the architecture style correct? | **Yes** |
| Are modules correctly decomposed? | **Yes** — with 2 Proposed ADRs pending |
| Are layers correctly placed? | **Yes** |
| Are integrations appropriately designed? | **Yes** for MVP scope |
| Is the technology stack coherent? | **Yes** — mandate-compliant |
| Are ADRs sufficient? | **Mostly** — 3 new ADRs needed |
| Are cross-cutting concerns addressed? | **Mostly** — idempotency and tiered data gaps |
| Ready for database design? | **Conditional proceed** after G-01 through G-10 |

### Sign-Off Required

| Role | Gate Action | Status |
|------|-------------|--------|
| Chief Solution Architect | Architecture review complete | ☐ |
| DDD Architect | Accept ADR-009, ADR-010 path | ☐ |
| Product Owner | Prioritize G-01–G-10 in sprint plan | ☐ |
| Inventory Controller | Opening balance workshop (G-03) | ☐ |
| Finance / Legal | Retention matrix (G-09) | ☐ |
| DBA | Await G-05 tiered architecture before modeling | ☐ |

---

## Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Chief Solution Architect | | | |
| DDD Solution Architect | | | |
| Product Owner | | | |
| Steering Committee Sponsor | | | |
| Lead DBA | | | |
| Security Engineer | | | |

---

*End of Architecture Review Report*

*Document ID: SRS-SA-009 | Version 1.0 | July 6, 2026*
