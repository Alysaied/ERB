# Architecture Decision Records (ADR)
## Inventory Management System

---

## Document Information

| Attribute | Detail |
|-----------|--------|
| **Document ID** | SRS-SA-008 |
| **Document Title** | Architecture Decision Records — Inventory Management System |
| **Version** | 1.0 |
| **Status** | Active |
| **Document Owner** | Senior Solution Architect |
| **Date** | July 6, 2026 |
| **Classification** | Internal — Architecture Confidential |

### Purpose

This document records **significant architectural decisions** for the Inventory Management System. Each ADR captures the context, decision, alternatives, consequences, and status to provide a durable rationale for future teams, auditors, and steering governance.

### Status Definitions

| Status | Meaning |
|--------|---------|
| **Accepted** | Decision approved and in force |
| **Proposed** | Decision direction agreed; pending workshop or gate confirmation |
| **Deprecated** | No longer recommended — see superseding ADR |
| **Superseded** | Replaced by another ADR |

### ADR Index

| ID | Title | Status |
|----|-------|--------|
| [ADR-001](#adr-001-modular-monolith-as-deployment-topology) | Modular Monolith as Deployment Topology | Accepted |
| [ADR-002](#adr-002-domain-driven-design-with-bounded-context-modules) | Domain-Driven Design with Bounded Context Modules | Accepted |
| [ADR-003](#adr-003-cleanhexagonal-internal-layer-structure) | Clean/Hexagonal Internal Layer Structure | Accepted |
| [ADR-004](#adr-004-inventory-balance-as-sole-quantity-authority) | Inventory Balance as Sole Quantity Authority | Accepted |
| [ADR-005](#adr-005-event-driven-cross-module-integration) | Event-Driven Cross-Module Integration | Accepted |
| [ADR-006](#adr-006-transactional-outbox-for-reliable-event-delivery) | Transactional Outbox for Reliable Event Delivery | Accepted |
| [ADR-007](#adr-007-cqrs-for-inventory-intelligence) | CQRS for Inventory Intelligence | Accepted |
| [ADR-008](#adr-008-saga-pattern-for-cross-module-workflows) | Saga Pattern for Cross-Module Workflows | Accepted |
| [ADR-009](#adr-009-stock-position-identity-per-product-location) | Stock Position Identity per Product-Location | Proposed |
| [ADR-010](#adr-010-location-freeze-authority-split) | Location Freeze Authority Split | Proposed |
| [ADR-011](#adr-011-promotional-ring-fence-via-domain-events) | Promotional Ring-Fence via Domain Events | Accepted |
| [ADR-012](#adr-012-anti-corruption-layers-for-external-systems) | Anti-Corruption Layers for External Systems | Accepted |
| [ADR-013](#adr-013-ims-as-operational-system-of-record) | IMS as Operational System of Record | Accepted |
| [ADR-014](#adr-014-java-spring-boot-backend-stack) | Java Spring Boot Backend Stack | Accepted |
| [ADR-015](#adr-015-spring-modulith-for-module-boundary-enforcement) | Spring Modulith for Module Boundary Enforcement | Accepted |
| [ADR-016](#adr-016-angular-spa-and-pwa-frontend) | Angular SPA and PWA Frontend | Accepted |
| [ADR-017](#adr-017-postgresql-as-primary-database) | PostgreSQL as Primary Database | Accepted |
| [ADR-018](#adr-018-schema-per-module-database-organization) | Schema-per-Module Database Organization | Accepted |
| [ADR-019](#adr-019-jpa-for-writes-jooq-for-intelligence-reads) | JPA for Writes, jOOQ for Intelligence Reads | Accepted |
| [ADR-020](#adr-020-oauth-20--oidc-with-jwt-resource-server) | OAuth 2.0 / OIDC with JWT Resource Server | Accepted |
| [ADR-021](#adr-021-redis-cache-for-atp-hot-path) | Redis Cache for ATP Hot Path | Accepted |
| [ADR-022](#adr-022-in-process-messaging-for-mvp) | In-Process Messaging for MVP | Accepted |
| [ADR-023](#adr-023-published-language-for-cross-boundary-references) | Published Language for Cross-Boundary References | Accepted |
| [ADR-024](#adr-024-centralized-audit-trail-projection) | Centralized Audit Trail Projection | Accepted |
| [ADR-025](#adr-025-architecture-fitness-functions-with-archunit) | Architecture Fitness Functions with ArchUnit | Accepted |

### Source Documents

SRS-SA-001 through SRS-SA-007, SRS-DM-007, SRS-DM-009, SRS-ES-007, BRD-IMS-001, NFR suite.

---

## ADR-001: Modular Monolith as Deployment Topology

| Field | Detail |
|-------|--------|
| **Decision ID** | ADR-001 |
| **Title** | Modular Monolith as Deployment Topology |
| **Status** | Accepted |

### Context

The IMS must support 13 bounded contexts, 18 aggregates, and 81 domain events while operating under a **fixed initiative budget (BC-01)** and **limited internal IT capacity (ORC-04)**. The organization requires phased delivery (MVP Months 0–6) without operational shutdown at go-live (OC-01). Strategic domain design (SRS-DM-007) defines clear context boundaries, but bounded contexts are explicitly **not** microservice boundaries.

The team must choose a deployment topology that balances domain alignment, operational simplicity, Stock Position consistency, and a credible path to future scale.

### Decision

Deploy the Inventory Management System as a **single modular monolith** — one deployable application composed of 13 loosely coupled modules aligned to bounded contexts, with compile-time boundary enforcement and a decomposition-ready interface surface.

Microservices are **deferred** until volume metrics and operational maturity justify selective extraction (Inventory Intelligence, integration gateway).

### Alternatives Considered

| Alternative | Reason Not Selected |
|-------------|---------------------|
| **Microservices (13 services)** | Distributed consistency risk on Stock Position; ops overhead exceeds ORC-04; premature with 16 open domain hotspots |
| **Traditional layered monolith** | No bounded-context boundaries; high coupling; rules scatter across layers |
| **Service-oriented (few coarse services)** | Arbitrary split; still distributed ops without clear domain mapping |

### Consequences

**Positive**
- Single deployment pipeline and runtime — lower ops cost
- ACID transactions within aggregate and in-process saga steps
- Faster MVP delivery and cross-module refactoring
- Module interfaces preserved for future extraction

**Negative**
- Shared runtime blast radius — defect in one module can affect availability
- Cannot independently scale Stock Position writes vs. reporting without read-side separation (mitigated by ADR-007)
- Requires discipline to prevent module boundary erosion

**Neutral**
- Team structure should align to core modules but shares one codebase

---

## ADR-002: Domain-Driven Design with Bounded Context Modules

| Field | Detail |
|-------|--------|
| **Decision ID** | ADR-002 |
| **Title** | Domain-Driven Design with Bounded Context Modules |
| **Status** | Accepted |

### Context

Domain analysis produced 13 bounded contexts, 18 aggregates, 24 domain services, 81 domain events, and 72 ubiquitous language terms. Business rules (BR-001 – BR-032) and segregation-of-duties requirements span multiple stakeholder functions (warehouse, purchasing, finance, marketing). A purely technical decomposition (UI / service / data layers only) cannot preserve domain integrity.

### Decision

Adopt **Domain-Driven Design (DDD)** as the strategic and tactical design approach. Each **bounded context maps 1:1 to a system module** (M-01 through M-13). Aggregates define consistency boundaries. Cross-context integration uses published language identifiers, domain events, and application-layer ports — never shared mutable domain objects.

### Alternatives Considered

| Alternative | Reason Not Selected |
|-------------|---------------------|
| **CRUD-centric data model** | Cannot express 32 business rules, SoD, and event choreography |
| **Transaction script pattern** | Business logic scatters; untestable rule enforcement |
| **Anemic domain model with service layer only** | Invariants not protected at aggregate boundaries |

### Consequences

**Positive**
- Direct traceability from BRD → domain model → modules → code
- Independent change velocity per context (catalog vs. balance vs. governance)
- Ubiquitous language (SRS-DM-008) drives API and code naming

**Negative**
- Higher initial design investment; DDD skill required across squads
- Cross-context workflows require explicit integration design (events, sagas)

**Neutral**
- Generic subdomains (Identity) may use simpler patterns within DDD module structure

---

## ADR-003: Clean/Hexagonal Internal Layer Structure

| Field | Detail |
|-------|--------|
| **Decision ID** | ADR-003 |
| **Title** | Clean/Hexagonal Internal Layer Structure |
| **Status** | Accepted |

### Context

Each of the 13 modules requires internal organization that protects domain rules from infrastructure concerns (ORM, HTTP, SSO, messaging) while supporting testability and ACL adapters for external systems. Multiple layering models (Layered, Clean, Hexagonal, Onion) were evaluated (SRS-SA-002).

### Decision

Apply **Clean Architecture with Hexagonal ports and adapters** inside every module:

- **Domain** (center): aggregates, value objects, domain events, repository interfaces
- **Application**: command/query handlers, sagas, authorization behaviors
- **Presentation** (per module API package): REST controllers, DTOs
- **Infrastructure**: JPA repositories, ACL adapters, event bus, cache

**Dependency rule:** source dependencies point inward only. Frameworks are details in infrastructure.

### Alternatives Considered

| Alternative | Reason Not Selected |
|-------------|---------------------|
| **Layered only (UI → Service → DAO)** | Domain logic leaks; insufficient port/adapter isolation |
| **Clean without hexagonal ports** | Weaker external integration boundary protection |
| **No internal layers (flat packages)** | Unmaintainable at 13 modules × 48 use cases |

### Consequences

**Positive**
- Domain testable without database or HTTP
- ACL adapters cleanly isolated for CRM and Finance
- Consistent structure across all squads

**Negative**
- Mapping boilerplate (DTO ↔ command ↔ domain) — mitigated by MapStruct
- Learning curve for teams accustomed to annotation-driven MVC only

---

## ADR-004: Inventory Balance as Sole Quantity Authority

| Field | Detail |
|-------|--------|
| **Decision ID** | ADR-004 |
| **Title** | Inventory Balance as Sole Quantity Authority |
| **Status** | Accepted |

### Context

The system's core value is answering *what do we have, where, and what is available?* Multiple modules mutate stock-related state (receiving, fulfillment, transfers, adjustments, returns, campaigns). Without a single authority, ATP can diverge — causing overselling (BR-001), audit failures (BO-19), and customer trust loss.

Domain model review (SRS-DM-009) confirms Stock Position as the core domain center of gravity.

### Decision

**Module M-04 (Inventory Balance) is the sole mutator** of on-hand, reserved, quarantined, and ATP quantities. All other modules request quantity changes via **commands, domain events, or sagas** — they never write to balance tables or hold mutable quantity state.

### Alternatives Considered

| Alternative | Reason Not Selected |
|-------------|---------------------|
| **Distributed quantity ownership** (fulfillment owns reservation table, balance owns on-hand) | Split-brain ATP; HS-007 reservation coordination risk |
| **Shared stock tables** accessed by all modules | No aggregate protection; invariant violations |
| **Event sourcing as sole write model** | Higher complexity; team maturity and BC-01 constraints |

### Consequences

**Positive**
- Single mathematical invariant: ATP = on-hand − reserved − quarantined
- Clear audit chain for all quantity changes
- Contention localized to Stock Position aggregate (product-location scope)

**Negative**
- M-04 becomes highest-contention module — requires optimistic locking and caching
- All quantity workflows have dependency on Balance module availability

---

## ADR-005: Event-Driven Cross-Module Integration

| Field | Detail |
|-------|--------|
| **Decision ID** | ADR-005 |
| **Title** | Event-Driven Cross-Module Integration |
| **Status** | Accepted |

### Context

Event storming identified 81 domain events and 12 end-to-end lifecycles with policy chains (e.g., put-away → stock available → backorder fulfill). Synchronous coupling of all 13 modules would create fragile call chains, threaten NFR-PERF-002 (2s ATP), and embed reporting inside transactional paths.

### Decision

Use **domain event choreography** as the primary cross-module state propagation mechanism. Modules publish domain events after successful aggregate commits. Subscribing modules react via application-layer event handlers. Synchronous cross-module calls are limited to **read-only queries** and **saga command steps** requiring immediate confirmation.

### Alternatives Considered

| Alternative | Reason Not Selected |
|-------------|---------------------|
| **Pure synchronous orchestration** | Tight coupling; hot-path latency; cascading failures |
| **Shared database triggers** | Hidden logic; untestable; violates module ownership |
| **Central orchestration engine (ESB)** | Over-engineering; BC-01; ORC-04 |

### Consequences

**Positive**
- Loose coupling; new subscribers (Intelligence, alerts) without publisher changes
- Natural audit trail from event stream
- Aligns with ADR-007 CQRS projections

**Negative**
- Eventual consistency between modules — requires saga compensation (ADR-008)
- Event schema versioning discipline required
- Debugging distributed flows harder than single call stack — mitigated by correlation IDs

---

## ADR-006: Transactional Outbox for Reliable Event Delivery

| Field | Detail |
|-------|--------|
| **Decision ID** | ADR-006 |
| **Title** | Transactional Outbox for Reliable Event Delivery |
| **Status** | Accepted |

### Context

NFR-REL-007 requires ≤15-minute recoverable data loss. NFR-BDR-001 requires continuous transaction protection. Publishing domain events **after** database commit creates a dual-write risk — crash between commit and publish loses events, causing Stock Position and Intelligence projections to diverge from operational truth.

### Decision

Implement the **transactional outbox pattern** — domain events are persisted to an outbox table in the **same database transaction** as the aggregate save. A separate dispatcher publishes events after commit. Handlers must be **idempotent** (deduplicate by `EventId`).

### Alternatives Considered

| Alternative | Reason Not Selected |
|-------------|---------------------|
| **Publish-then-save** | Inconsistent on failure |
| **XA two-phase commit** | Performance penalty; operational complexity |
| **Change Data Capture (Debezium)** | Additional ops infrastructure for MVP |

### Consequences

**Positive**
- At-least-once delivery with atomic write + event record
- Outbox table in PostgreSQL — no additional broker required for MVP
- Ready for external broker relay in Phase 2

**Negative**
- Outbox table growth — requires archival job
- Slight latency between commit and handler execution (acceptable per SRS-SA-005)

---

## ADR-007: CQRS for Inventory Intelligence

| Field | Detail |
|-------|--------|
| **Decision ID** | ADR-007 |
| **Title** | CQRS for Inventory Intelligence |
| **Status** | Accepted |

### Context

M-13 Inventory Intelligence owns dashboards, KPIs, movement history, audit trail, and valuation snapshots — with **no write aggregates**. Running reporting queries against transactional Stock Position tables risks dock performance degradation (AR-10) and violates NFR-PERF-002/PERF-004. Intelligence has fundamentally different read-heavy, eventually consistent NFR profile.

### Decision

Apply **Command Query Responsibility Segregation (CQRS)** for the Intelligence concern:

- **Commands** mutate aggregates in transactional modules (M-01 – M-12)
- **Queries** for dashboards, audit, KPIs, and ATP display read from **dedicated read projections** maintained by event handlers in M-13
- Read models are rebuildable from domain event history

### Alternatives Considered

| Alternative | Reason Not Selected |
|-------------|---------------------|
| **Single model (JPA entities for everything)** | Reporting load on write tables |
| **Database views only** | Limited application-level composition; coupling to write schema |
| **Separate reporting database via ETL batch** | Stale data; complex pipeline for MVP |

### Consequences

**Positive**
- Write path protected for fulfillment and receiving performance
- Intelligence module extractable to separate service in Phase 3
- Audit trail append-only and query-optimized

**Negative**
- Eventual consistency on dashboards (seconds lag — acceptable)
- Projection rebuild complexity on schema evolution
- Second data access pattern (jOOQ) in Intelligence module

---

## ADR-008: Saga Pattern for Cross-Module Workflows

| Field | Detail |
|-------|--------|
| **Decision ID** | ADR-008 |
| **Title** | Saga Pattern for Cross-Module Workflows |
| **Status** | Accepted |

### Context

Business workflows span multiple aggregates and modules: order confirm → reserve stock, put-away → stock increase, transfer dispatch → source deduct + destination increase, physical count → freeze → adjust. DDD rule "one transaction, one aggregate" prohibits single ACID transaction across modules. Hotspot HS-007 highlights partial failure risk when order confirms but reservation fails.

### Decision

Implement **orchestrated sagas** in the calling module's application layer for cross-module workflows. Each saga step is its own transaction. Define **explicit compensation actions** for each step failure. Critical sagas: SAG-01 (order confirm-reserve), SAG-04 (physical count-freeze), SAG-05 (opening balance go-live).

### Alternatives Considered

| Alternative | Reason Not Selected |
|-------------|---------------------|
| **Distributed two-phase commit** | Impractical across modules; performance and availability impact |
| **Choreography only (no orchestrator)** | Hard to trace and compensate multi-step failures |
| **Manual reconciliation** | Unacceptable for ATP integrity and customer orders |

### Consequences

**Positive**
- Clear failure handling and compensation paths
- Each step remains single-aggregate ACID
- Testable with integration tests per saga

**Negative**
- Saga state management adds application complexity
- Compensation logic must be carefully designed to avoid orphaned state
- Requires HS-007 workshop for reservation failure policy

---

## ADR-009: Stock Position Identity per Product-Location

| Field | Detail |
|-------|--------|
| **Decision ID** | ADR-009 |
| **Title** | Stock Position Identity per Product-Location |
| **Status** | Proposed |

### Context

Domain model review (P1-05) and hotspot HS-005 identify a fundamental fork: Stock Position identity as *product + location* with embedded Lot/Batch child entities, versus *product + location + lot* as separate positions. This decision affects reservation, pick, cycle count, transfer, and persistence design across all operational modules.

### Decision

Adopt **one Stock Position aggregate per product-location**. Lot/Batch entities are **child entities** within the aggregate holding sub-quantities. ATP at root = sum of sellable lot quantities minus holds. Traceable products require lot capture on all movements (BR-017).

*Pending confirmation at architecture gate workshop with Quality and Warehouse stakeholders.*

### Alternatives Considered

| Alternative | Reason Not Selected |
|-------------|---------------------|
| **One Stock Position per product-location-lot** | Explosion of aggregates; complex network ATP aggregation |
| **Lot-less Stock Position for all products** | Violates BR-017 for traceable products |

### Consequences

**Positive**
- Single ATP query point per SKU per location
- Lot quantities enforced to sum to on-hand invariant
- Aligns with FEFO pick selection within aggregate

**Negative**
- Larger aggregate for high-lot-count products — lock contention risk
- Pending business confirmation — **blocks detailed Balance module design until Accepted**

---

## ADR-010: Location Freeze Authority Split

| Field | Detail |
|-------|--------|
| **Decision ID** | ADR-010 |
| **Title** | Location Freeze Authority Split |
| **Status** | Proposed |

### Context

BR-024 requires location freeze during wall-to-wall physical inventory count. Hotspot HS-003 and finding P1-03 identify dual ownership risk: Physical Inventory Count aggregate initiates freeze while Inventory Location aggregate also lists freeze enforcement. Two writers could cause race conditions at count certification.

### Decision

**Physical Inventory Count (M-09) initiates freeze** via `LocationFreezeImposed` event. **Inventory Location (M-02) holds the authoritative frozen flag** and applies/releases state. All operational modules consult M-02 `IsLocationFrozen` query only — never M-09 directly.

### Alternatives Considered

| Alternative | Reason Not Selected |
|-------------|---------------------|
| **Freeze owned only by Physical Count module** | Network module cannot enforce freeze for non-count scenarios |
| **Freeze duplicated in both aggregates** | Race conditions; inconsistent state |

### Consequences

**Positive**
- Single authoritative freeze read point (Freeze Guard DS-014)
- Clear event-driven handoff between accuracy and network modules

**Negative**
- Eventual consistency window between impose event and flag apply — must be sub-second
- Emergency override policy still requires business workshop

---

## ADR-011: Promotional Ring-Fence via Domain Events

| Field | Detail |
|-------|--------|
| **Decision ID** | ADR-011 |
| **Title** | Promotional Ring-Fence via Domain Events |
| **Status** | Accepted |

### Context

Finding P1-02 and hotspot HS-004 identify dual ownership risk for promotional ATP segregation. Commercial Campaign and Inventory Balance both reference ring-fenced quantity. BR-029 requires ring-fencing during campaigns without corrupting general ATP.

### Decision

**M-11 Commercial Campaign owns allocation intent and lifecycle.** M-04 Inventory Balance owns ATP mechanics. Campaign publishes `PromotionalStockAllocated` / `PromotionalAllocationReleased` events. Balance reacts by segregating/restoring ATP — **never self-initiates ring-fence**.

### Alternatives Considered

| Alternative | Reason Not Selected |
|-------------|---------------------|
| **Ring-fence logic only in Stock Position** | Marketing lifecycle coupled to core domain |
| **Shared mutable segregation table** | Dual writers; inconsistent ATP |

### Consequences

**Positive**
- Clear ownership aligned to stakeholder functions (Marketing vs. Operations)
- Phase 2 campaign module independently evolvable

**Negative**
- Brief eventual consistency between allocation command and ATP segregation
- Override rules (MR-10) require business policy workshop

---

## ADR-012: Anti-Corruption Layers for External Systems

| Field | Detail |
|-------|--------|
| **Decision ID** | ADR-012 |
| **Title** | Anti-Corruption Layers for External Systems |
| **Status** | Accepted |

### Context

IMS integrates with Sales/CRM (EXT-01), Finance ERP (EXT-02), Sales Channel (EXT-03), Marketing (EXT-07), and HR Directory (EXT-08). External systems have foreign domain models, lifecycles, and authority boundaries. BRD scope excludes full CRM and GL ownership from IMS. Absorbing foreign models corrupts fulfillment and balance domains.

### Decision

Implement **Anti-Corruption Layers (ACL)** as infrastructure adapters at module boundaries:

| External System | ACL Location | Translates To |
|-----------------|--------------|--------------|
| Sales/CRM | M-07 Fulfillment | `ImportCustomerOrder` command |
| Finance ERP | M-13 Intelligence | Valuation snapshot export format |
| Finance ERP | M-06 Inbound | Match status (HS-014) |
| Marketing | M-11 Campaign | `CreatePromotionalAllocation` |
| HR Directory | M-12 Identity | `ProvisionUserAccount` |

Foreign models **never enter the domain layer**.

### Alternatives Considered

| Alternative | Reason Not Selected |
|-------------|---------------------|
| **Shared canonical enterprise data model** | Multi-year integration program; out of BC-01 scope |
| **Direct CRM entity mapping to JPA** | Couples fulfillment to CRM schema changes |
| **Point-to-point API calls without ACL** | Foreign concepts leak into application layer |

### Consequences

**Positive**
- IMS domain remains stable when CRM or ERP changes
- Phased integration depth (manual MVP → API Phase 2) without domain rewrite

**Negative**
- ACL maintenance overhead per external system
- Mapping logic requires tests and versioning

---

## ADR-013: IMS as Operational System of Record

| Field | Detail |
|-------|--------|
| **Decision ID** | ADR-013 |
| **Title** | IMS as Operational System of Record |
| **Status** | Accepted |

### Context

Hotspot HS-014 questions whether IMS or Finance ERP owns supplier invoicing, three-way match, and valuation. BRD positions IMS as inventory system of record (TEC-01). Finance owns GL and payment authority. ~8% current valuation variance must reduce to ≤2% (BO-18).

### Decision

IMS is the **operational system of record** for stock quantities, movements, reservations, receipt facts, and operational match outcomes. Finance ERP remains **financial system of record** for GL postings and payment authorization. IMS publishes valuation snapshots and movement facts via ACL; Finance publishes GL balance for reconciliation.

### Alternatives Considered

| Alternative | Reason Not Selected |
|-------------|---------------------|
| **ERP owns all financial inventory** | IMS cannot enforce BR-004 – BR-008 at dock speed |
| **IMS owns payment authorization** | Outside BRD scope; duplicates ERP |

### Consequences

**Positive**
- Clear data ownership boundaries
- Warehouse operations not blocked by ERP availability

**Negative**
- Reconciliation workflow required (Phase 3 automation)
- Temporary manual finance export in MVP (TEC-05)

---

## ADR-014: Java Spring Boot Backend Stack

| Field | Detail |
|-------|--------|
| **Decision ID** | ADR-014 |
| **Title** | Java Spring Boot Backend Stack |
| **Status** | Accepted |

### Context

Organization mandates **Java and Spring**. IMS requires enterprise-grade security, transaction management, REST APIs, and integration with PostgreSQL. Team hiring and supportability favor mainstream stack. Virtual threads in Java 21 benefit I/O-bound warehouse workloads.

### Decision

Adopt **Java 21 LTS** with **Spring Boot 3.x** as the backend runtime — including Spring Web, Spring Security, Spring Data JPA, and Spring Modulith (ADR-015).

### Alternatives Considered

| Alternative | Reason Not Selected |
|-------------|---------------------|
| **Quarkus** | Less Modulith maturity; not mandated |
| **.NET** | Diverges from Java mandate |
| **Java EE/Jakarta EE standalone** | More ceremony than Spring Boot |

### Consequences

**Positive**
- Mandate compliance; large hiring pool; mature ecosystem
- Spring Boot Test, Actuator, and security integration

**Negative**
- Heavier runtime than Quarkus — acceptable for enterprise deployment
- Requires discipline to avoid Spring MVC + JPA anemic pattern

---

## ADR-015: Spring Modulith for Module Boundary Enforcement

| Field | Detail |
|-------|--------|
| **Decision ID** | ADR-015 |
| **Title** | Spring Modulith for Module Boundary Enforcement |
| **Status** | Accepted |

### Context

ADR-001 modular monolith requires enforceable boundaries between 13 bounded contexts. Package naming alone is insufficient — ArchUnit helps but Spring Modulith provides first-class module APIs, event publication, JDBC event registry, and `ApplicationModuleTest` verification.

### Decision

Use **Spring Modulith** to structure the modular monolith — module definitions, allowed dependencies, module-scoped events, and integration with transactional outbox.

### Alternatives Considered

| Alternative | Reason Not Selected |
|-------------|---------------------|
| **ArchUnit only** | No built-in event/outbox support |
| **OSGi** | Obsolete complexity |
| **Manual package conventions** | Not compile-time verifiable |

### Consequences

**Positive**
- Architecture enforced in CI via module tests
- Event infrastructure aligned to DDD modules

**Negative**
- Newer Spring project — smaller community reference base
- Team training in Sprint 0 required

---

## ADR-016: Angular SPA and PWA Frontend

| Field | Detail |
|-------|--------|
| **Decision ID** | ADR-016 |
| **Title** | Angular SPA and PWA Frontend |
| **Status** | Accepted |

### Context

Organization mandates **Angular**. IMS serves 19 user roles across office and warehouse with 90 functional requirements. TEC-03 excludes offline MVP. Warehouse staff need mobile-friendly interfaces without maintaining separate native apps under BC-01.

### Decision

Build a **single Angular 19 SPA** with Angular Material, lazy-loaded feature modules per bounded context, and **PWA capabilities** for warehouse mobile (installable, responsive, barcode-ready).

### Alternatives Considered

| Alternative | Reason Not Selected |
|-------------|---------------------|
| **React** | Not mandated |
| **Separate native mobile apps** | Cost and dual codebase |
| **Server-rendered only (Thymeleaf)** | Poor mobile UX for warehouse |

### Consequences

**Positive**
- One frontend codebase; mandate compliance; enterprise structure
- OpenAPI-generated TypeScript clients possible

**Negative**
- Large bundle — mitigated by lazy loading
- PWA limitations on specialized scanner hardware — Capacitor in Phase 2 if needed

---

## ADR-017: PostgreSQL as Primary Database

| Field | Detail |
|-------|--------|
| **Decision ID** | ADR-017 |
| **Title** | PostgreSQL as Primary Database |
| **Status** | Accepted |

### Context

Organization mandates **PostgreSQL**. IMS requires ACID transactions for Stock Position, JSONB for event payloads, row-level locking for reservation contention, 7-year retention (NFR-COM-019), and ≤15-minute RPO (NFR-BDR-001). Fixed budget favors open-source database.

### Decision

Use **PostgreSQL 16** as the sole primary relational database for transactional writes, outbox, read projections, and audit storage.

### Alternatives Considered

| Alternative | Reason Not Selected |
|-------------|---------------------|
| **SQL Server / Oracle** | Licensing cost (BC-01) |
| **MySQL** | Weaker JSON and constraint ecosystem |
| **MongoDB** | Poor fit for ATP transactional integrity |

### Consequences

**Positive**
- Mandate compliance; ACID; JSONB; logical replication for read scaling
- Testcontainers parity in CI

**Negative**
- Write scaling vertical — acceptable for MVP–Phase 2 scale
- DBA tuning (vacuum, indexes) required for ATP hot paths

---

## ADR-018: Schema-per-Module Database Organization

| Field | Detail |
|-------|--------|
| **Decision ID** | ADR-018 |
| **Title** | Schema-per-Module Database Organization |
| **Status** | Accepted |

### Context

ADR-002 defines 13 modules with exclusive aggregate ownership. Module boundary rule MB-07 prohibits shared tables. Single PostgreSQL instance required for operational simplicity (ORC-04) and ACID within monolith.

### Decision

Each module owns tables in a **dedicated PostgreSQL schema** (`catalog`, `balance`, `fulfillment`, etc.). Flyway migrations are per-module. **No cross-schema foreign keys** except shared kernel reference tables (`product_sku`, `location_code`).

### Alternatives Considered

| Alternative | Reason Not Selected |
|-------------|---------------------|
| **Single flat schema** | No ownership enforcement |
| **Database per module** | Microservices ops overhead |

### Consequences

**Positive**
- Clear data ownership; extraction-ready
- Single backup and instance management

**Negative**
- Cross-schema queries discouraged — use module ports
- Migration coordination on shared kernel changes

---

## ADR-019: JPA for Writes, jOOQ for Intelligence Reads

| Field | Detail |
|-------|--------|
| **Decision ID** | ADR-019 |
| **Title** | JPA for Writes, jOOQ for Intelligence Reads |
| **Status** | Accepted |

### Context

ADR-007 CQRS separates write and read paths. Write side requires aggregate mapping with optimistic locking. Intelligence module requires complex KPI aggregations, audit search, and dashboard queries that should not load JPA entity graphs (AR-10).

### Decision

Use **Hibernate 6 / Spring Data JPA** for transactional module write repositories only. Use **jOOQ** exclusively in **M-13 Intelligence** for read projections and reports.

### Alternatives Considered

| Alternative | Reason Not Selected |
|-------------|---------------------|
| **JPA for all queries** | Performance and coupling risk on reporting |
| **jOOQ for all modules** | Verbose aggregate persistence; loses optimistic locking conventions |
| **MyBatis** | Less Spring Boot native integration |

### Consequences

**Positive**
- Right tool per path; type-safe SQL for reports
- Domain layer remains ORM-free

**Negative**
- Two data access patterns — confined to clear module boundary
- jOOQ schema codegen pipeline required

---

## ADR-020: OAuth 2.0 / OIDC with JWT Resource Server

| Field | Detail |
|-------|--------|
| **Decision ID** | ADR-020 |
| **Title** | OAuth 2.0 / OIDC with JWT Resource Server |
| **Status** | Accepted |

### Context

NFR-SEC-001 requires unique user authentication. NFR-SEC-005 – SEC-009 require RBAC and location-scoped permissions. Enterprise IdP (SVC-01) expected. Angular SPA requires token-based API auth. 19 roles and 20 SoD rules must be enforced.

### Decision

Integrate **OAuth 2.0 / OpenID Connect** with enterprise IdP. Spring Security **JWT resource server** validates bearer tokens on every API request. Angular uses `angular-oauth2-oidc`. Authorization enforced in application layer via M-12 Identity ports.

### Alternatives Considered

| Alternative | Reason Not Selected |
|-------------|---------------------|
| **Session-only form login** | No SSO; poor SPA scaling |
| **SAML only** | Heavier SPA integration than OIDC |
| **API keys** | No user attribution |

### Consequences

**Positive**
- Enterprise SSO; stateless API; horizontal scaling
- Mandate-aligned security posture

**Negative**
- Token revocation requires short TTL or blocklist on deprovision
- IdP role mapping to 100 IMS permissions requires governance

---

## ADR-021: Redis Cache for ATP Hot Path

| Field | Detail |
|-------|--------|
| **Decision ID** | ADR-021 |
| **Title** | Redis Cache for ATP Hot Path |
| **Status** | Accepted |

### Context

NFR-PERF-002 requires ≥98% of ATP lookups within 2 seconds. Stock Position is high-read, high-write contention aggregate. CS and sales conduct live availability inquiries during customer calls (BO-16). PostgreSQL alone may insufficient under peak concurrent reads.

### Decision

Deploy **Redis** as distributed cache for ATP by SKU/location. Cache invalidated on **every Balance domain event** affecting quantities. Cached responses include `asOf` timestamp. Cache miss falls through to authoritative read repository — never default to zero.

### Alternatives Considered

| Alternative | Reason Not Selected |
|-------------|---------------------|
| **In-process Caffeine only** | Invalid with multiple app instances |
| **PostgreSQL materialized views only** | Refresh lag; write coupling |
| **No cache** | Risk of NFR-PERF-002 breach at scale |

### Consequences

**Positive**
- Sub-millisecond reads for hot SKUs
- Event invalidation preserves BR-001 integrity

**Negative**
- Additional infrastructure component
- Staleness risk if invalidation fails — monitor and alert

---

## ADR-022: In-Process Messaging for MVP

| Field | Detail |
|-------|--------|
| **Decision ID** | ADR-022 |
| **Title** | In-Process Messaging for MVP |
| **Status** | Accepted |

### Context

ADR-005 event-driven integration requires message transport. ORC-04 limits ops capacity. MVP modular monolith does not require cross-process messaging. External CRM and channel integration deferred to Phase 2 (TEC-04).

### Decision

Use **Spring Application Events / Spring Modulith event API** with **transactional outbox** for MVP internal messaging. **Defer external message broker** (RabbitMQ recommended) to Phase 2 when CRM API and channel feeds require cross-process async integration.

### Alternatives Considered

| Alternative | Reason Not Selected |
|-------------|---------------------|
| **Kafka from day one** | Ops overhead; overkill for monolith MVP |
| **RabbitMQ from day one** | Additional infra without external consumers |
| **Synchronous only** | Violates ADR-005; couples modules |

### Consequences

**Positive**
- Zero broker ops for MVP; simpler debugging
- Outbox schema ready for broker relay

**Negative**
- Cannot horizontally scale event consumers independently in MVP
- Phase 2 migration requires broker introduction and handler compatibility testing

---

## ADR-023: Published Language for Cross-Boundary References

| Field | Detail |
|-------|--------|
| **Decision ID** | ADR-023 |
| **Title** | Published Language for Cross-Boundary References |
| **Status** | Accepted |

### Context

13 modules and external systems must reference products, locations, users, and orders without sharing domain entity types. DDD strategic design requires identity-only references between aggregates and contexts.

### Decision

Define a **shared kernel** of immutable identifier value types: `ProductSku`, `LocationCode`, `UserId`, `SupplierCode`, and standard event envelope (`EventId`, `CorrelationId`, `OccurredAt`). All cross-module and ACL integrations use published language only — **no foreign aggregate imports**.

### Alternatives Considered

| Alternative | Reason Not Selected |
|-------------|---------------------|
| **Shared entity library** | Couples module lifecycles; lazy-loading leaks |
| **Primitive strings only** | No type safety; conflation of identifiers |

### Consequences

**Positive**
- Compile-time type safety for identifiers
- Modules evolve independently

**Negative**
- Shared kernel must remain minimal — resist feature creep
- Identifier format changes are organization-wide breaking changes

---

## ADR-024: Centralized Audit Trail Projection

| Field | Detail |
|-------|--------|
| **Decision ID** | ADR-024 |
| **Title** | Centralized Audit Trail Projection |
| **Status** | Accepted |

### Context

BO-19 requires 100% audit trail coverage. NFR-COM-010 requires immutable audit records. NFR review identified duplicate audit requirements across NFR-LOG, NFR-SEC, and NFR-COM. Per-module audit tables would fragment evidence and complicate 7-year retention.

### Decision

Maintain a **single authoritative audit trail projection** in **M-13 Intelligence**, built from domain events and command audit context. Operational logs (NFR-LOG) remain separate diagnostic records. Auditor export via `ExportAuditEvidencePackage` query (NFR-PERF-026, NFR-COM-012).

### Alternatives Considered

| Alternative | Reason Not Selected |
|-------------|---------------------|
| **Per-module audit tables** | Fragmented; inconsistent schema |
| **Operational logs as audit** | Insufficient structure and immutability |
| **External SIEM only** | Business fact context missing |

### Consequences

**Positive**
- Single query point for auditors
- Event-sourced rebuild capability

**Negative**
- Seconds-level lag on audit visibility — acceptable for compliance
- Intelligence module becomes critical for audit access

---

## ADR-025: Architecture Fitness Functions with ArchUnit

| Field | Detail |
|-------|--------|
| **Decision ID** | ADR-025 |
| **Title** | Architecture Fitness Functions with ArchUnit |
| **Status** | Accepted |

### Context

Modular monolith erosion is the primary long-term risk (AR-09). ADR-003 layer rules and ADR-002 module boundaries must survive team turnover and delivery pressure across 18 months. Manual architecture review alone is insufficient.

### Decision

Implement **ArchUnit** fitness functions in CI enforcing:

- Domain packages do not depend on infrastructure, application, or presentation
- Modules do not import other modules' domain packages
- JPA annotations absent from domain layer
- Controllers do not access repositories directly

Complement with **Spring Modulith `ApplicationModuleTest`**.

### Alternatives Considered

| Alternative | Reason Not Selected |
|-------------|---------------------|
| **Code review only** | Inconsistent enforcement |
| **jQAssistant** | Heavier setup than needed |

### Consequences

**Positive**
- Automated regression on architecture rules
- Fast feedback on PRs

**Negative**
- Rules require maintenance as packages evolve
- False positives possible — tune carefully

---

## ADR Governance

### Process

| Step | Action | Owner |
|------|--------|-------|
| 1 | Propose ADR via PR with context and alternatives | Any architect or tech lead |
| 2 | Review with DDD architect and affected squad leads | Solution Architect |
| 3 | Accept, reject, or mark Proposed pending workshop | Steering committee / ARB |
| 4 | Update status when superseded | Solution Architect |
| 5 | Link ADR in module README and relevant SRS docs | Author |

### Review Schedule

| ADR | Next Review Trigger |
|-----|---------------------|
| ADR-009 | HS-005 workshop completion |
| ADR-010 | HS-003 workshop completion |
| ADR-022 | Phase 2 external integration kickoff |
| ADR-001 | 30% transaction growth or multi-region deployment |

---

## Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Senior Solution Architect | | | |
| DDD Solution Architect | | | |
| Product Owner | | | |
| Steering Committee Sponsor | | | |

---

*End of Architecture Decision Records*

*Document ID: SRS-SA-008 | Version 1.0 | July 6, 2026*
