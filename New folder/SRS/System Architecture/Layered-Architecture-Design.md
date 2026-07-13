# Layered Architecture Design
## Inventory Management System

---

## Document Information

| Attribute | Detail |
|-----------|--------|
| **Document ID** | SRS-SA-004 |
| **Document Title** | Layered Architecture Design — Inventory Management System |
| **Version** | 1.0 |
| **Status** | Draft |
| **Document Owner** | Solution Architect |
| **Prepared For** | Development squads, technical architects, and QA leads |
| **Date** | July 6, 2026 |
| **Classification** | Internal — Architecture Confidential |
| **Scope** | Layer structure and dependency rules within each bounded-context module — no framework selection, class diagrams, or code |

### Related Documents

| Document | ID | Relationship |
|----------|-----|--------------|
| Architecture Vision | SRS-SA-001 | Strategic direction |
| Architecture Style Recommendation | SRS-SA-002 | Clean/Hexagonal + modular monolith |
| System Modules Design | SRS-SA-003 | 13 module boundaries |
| Domain Aggregates | SRS-DM-003 | Domain layer content |
| Domain Services | SRS-DM-005 | Domain and application coordination |

### Document Purpose

This document defines the **four-layer internal architecture** applied within each bounded-context module of the Inventory Management System modular monolith. It follows **Clean Architecture** (dependency rule: source code dependencies point inward) combined with **Hexagonal ports and adapters** at module boundaries.

---

## 1. Clean Architecture Overview

### 1.1 Layer Model

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        PRESENTATION LAYER                                    │
│   HTTP Controllers │ Web UI │ Mobile API │ Integration Webhooks │ DTOs      │
└──────────────────────────────────┬──────────────────────────────────────────┘
                                   │ calls
                                   ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                        APPLICATION LAYER                                     │
│   Command Handlers │ Query Handlers │ Sagas │ Event Handlers │ AuthZ Gates  │
└──────────────────────────────────┬──────────────────────────────────────────┘
                                   │ orchestrates
                                   ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                          DOMAIN LAYER                                        │
│   Aggregates │ Entities │ Value Objects │ Domain Services │ Domain Events   │
│   Repository Interfaces (ports) │ Domain Policies │ Invariants              │
└──────────────────────────────────┬──────────────────────────────────────────┘
                                   │ implemented by
                                   ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                       INFRASTRUCTURE LAYER                                   │
│   Persistence │ Event Bus │ ACL Adapters │ Auth │ Logging │ Notifications   │
└─────────────────────────────────────────────────────────────────────────────┘

        ◄────────────── DEPENDENCY DIRECTION (inward only) ──────────────
```

### 1.2 The Dependency Rule

| Rule | Statement |
|------|-----------|
| **DR-01** | Source code dependencies must point **inward** only — from outer layers toward the domain |
| **DR-02** | Inner layers **never** reference outer layers — no domain import of controllers, ORM, or HTTP clients |
| **DR-03** | Cross-layer collaboration uses **interfaces (ports)** defined in the domain or application layer, implemented in infrastructure |
| **DR-04** | Data crosses boundaries as **plain data structures** — DTOs, commands, queries, events — never as framework types |
| **DR-05** | Frameworks and drivers are **details** relegated to the infrastructure layer |

### 1.3 Layer-to-Module Relationship

Each of the **13 bounded-context modules** (SRS-SA-003) contains its own complete four-layer stack. Layers are **replicated per module**, not shared as a single horizontal slice across the entire application.

```
ims/
├── catalog/          (M-01)  → presentation / application / domain / infrastructure
├── network/          (M-02)
├── governance/       (M-03)
├── balance/          (M-04)  → core domain — richest layer
├── procurement/      (M-05)
├── inbound/          (M-06)
├── fulfillment/      (M-07)
├── transfer/         (M-08)
├── accuracy/         (M-09)
├── returns/          (M-10)
├── campaign/         (M-11)
├── identity/         (M-12)
├── intelligence/     (M-13)  → query-heavy; thin domain, rich application + infra read models
└── shared-kernel/    → published identifiers only (ProductSku, LocationCode) — no layers
```

### 1.4 CQRS Layer Split

Command and query paths share the domain layer but diverge in application and infrastructure:

| Path | Application Layer | Infrastructure Layer |
|------|-------------------|----------------------|
| **Commands** (writes) | Command handlers, sagas, domain event dispatch | Write repositories, transactional outbox, unit of work |
| **Queries** (reads) | Query handlers | Read repositories, projections, materialized views |

Inventory Intelligence (M-13) is predominantly **query path** — minimal domain, no write command handlers.

---

## 2. Presentation Layer

### 2.1 Responsibilities

The Presentation Layer is the **outermost adapter** that translates external actor input into application-layer commands and queries, and translates application results into responses consumable by users and external systems.

| Responsibility | Description |
|----------------|-------------|
| **Request reception** | Accept HTTP requests, UI actions, mobile scanner input, and integration webhook payloads |
| **Input validation (syntactic)** | Validate request shape, required fields, data types, and format — not business rules |
| **Authentication presentation** | Extract identity tokens or session credentials and pass to application layer |
| **DTO mapping** | Map HTTP/JSON/UI models to application commands and queries; map results to response DTOs |
| **Authorization presentation** | Invoke application-layer authorization gates before dispatching commands |
| **Error translation** | Map application/domain exceptions to HTTP status codes and user-safe error messages |
| **API versioning and routing** | Route requests to correct module endpoints |
| **Content negotiation** | JSON for APIs; HTML/view models for web UI; optimized payloads for mobile warehouse clients |
| **Correlation ID attachment** | Attach trace/correlation identifiers to requests for observability |

**The Presentation Layer does not:**
- Enforce business rules (BR-001 – BR-032)
- Access databases or repositories directly
- Mutate domain entities
- Publish domain events
- Contain transaction boundaries

### 2.2 Allowed Dependencies

| May Depend On | Must Not Depend On |
|---------------|-------------------|
| Application Layer (command/query dispatch) | Domain Layer (direct aggregate access) |
| Shared presentation utilities (validation attributes, base controller) | Infrastructure Layer (repositories, ORM, message bus) |
| Cross-cutting presentation middleware (auth middleware invokes application) | Other modules' domain internals |
| Published DTO / request/response contracts | Framework-specific types leaking into application |

```
Presentation ──► Application     ✅
Presentation ──► Domain          ❌
Presentation ──► Infrastructure  ❌
```

### 2.3 Typical Components

| Component | Purpose | IMS Examples |
|-----------|---------|--------------|
| **REST API Controllers** | HTTP endpoint per use case group | `StockController`, `ReceiptController`, `OrderController` |
| **Web UI Controllers / Views** | Server-rendered or SPA shell pages | Dashboard views, master data forms |
| **Mobile Warehouse API Controllers** | Optimized endpoints for scanner workflows | `PickController`, `PutAwayController`, `CycleCountController` |
| **Integration Webhook Controllers** | Inbound endpoints for external systems | `SalesOrderWebhookController` (CRM ACL entry) |
| **Request DTOs** | Inbound data contracts | `ReserveStockRequest`, `VerifyReceiptRequest` |
| **Response DTOs** | Outbound data contracts | `AvailabilityResponse`, `OrderStatusResponse` |
| **Input Validators** | Syntactic validation | Required SKU, positive quantity, valid date format |
| **Exception Filters / Handlers** | Uniform error responses | `BusinessRuleViolationException` → 422; `NotFoundException` → 404 |
| **Authentication Middleware** | Token/session extraction | JWT bearer, SSO redirect |
| **API Documentation** | OpenAPI/Swagger metadata | Endpoint catalog per module |
| **Model Binders / Mappers** | DTO ↔ Command/Query translation | `ReserveStockRequest` → `ReserveStockCommand` |

### 2.4 Presentation Layer by Actor

| Actor | Presentation Entry Points |
|-------|--------------------------|
| Warehouse Staff | Mobile API — put-away, cycle count, transfer |
| Receiving Clerk | Mobile/Web API — goods receipt, discrepancy |
| Picker/Packer | Mobile API — pick verification, shipment |
| Customer Service | Web API — availability inquiry, order confirm, RMA |
| Purchasing | Web API — PO, requisition, inbound pipeline |
| Management | Web UI — dashboards (delegates to Intelligence queries) |
| Finance | Web API — invoice match, valuation export |
| System Administrator | Web UI — user and role management |
| Sales/CRM (external) | Integration webhook — order import |

---

## 3. Application Layer

### 3.1 Responsibilities

The Application Layer **orchestrates use cases** — it coordinates domain objects, enforces application-level workflow, manages transactions, and dispatches cross-module integration. It contains **no business invariants**; those belong in the domain layer.

| Responsibility | Description |
|----------------|-------------|
| **Use case execution** | Receive commands/queries from presentation and execute the corresponding workflow |
| **Transaction management** | Define unit-of-work boundaries — one aggregate mutation per transaction (DR-DDD) |
| **Domain orchestration** | Load aggregates via repository ports, invoke domain methods, persist changes |
| **Authorization gates** | Verify user permission and location scope before command execution (delegates to Identity module) |
| **Saga coordination** | Manage multi-step cross-module workflows with compensation (order confirm → reserve) |
| **Domain event dispatch** | Collect domain events from aggregates and publish via event bus port |
| **Cross-module consultation** | Invoke other modules' query ports synchronously (e.g., ATP lookup, freeze check) |
| **Application services** | Coordinate operations spanning domain services or multiple ports within one use case |
| **Idempotency** | Ensure duplicate command submission does not double-apply (receipt, reservation) |
| **Audit context enrichment** | Attach user identity and correlation ID to commands before domain execution |
| **Query orchestration** | Route read requests to appropriate read repositories or cross-module query ports |
| **DTO assembly (reads)** | Compose query results from read models into response shapes |

**The Application Layer does not:**
- Implement business invariants (ATP formula, SoD, freeze rules)
- Contain SQL or ORM code
- Reference HTTP, JSON, or UI frameworks
- Own long-lived state beyond saga/process manager instances

### 3.2 Allowed Dependencies

| May Depend On | Must Not Depend On |
|---------------|-------------------|
| Domain Layer (aggregates, domain services, repository interfaces) | Infrastructure Layer (concrete implementations) |
| Application contracts (commands, queries, handler interfaces) | Presentation Layer |
| Cross-module **query ports** (interfaces only) | Other modules' aggregate internals |
| Shared kernel identifiers (`ProductSku`, `LocationCode`) | ORM entities, HTTP clients, framework types |

```
Application ──► Domain              ✅
Application ──► Infrastructure      ❌  (depends on ports defined in domain/application)
Application ──► Presentation        ❌
```

**Dependency inversion:** Application layer defines or uses **interfaces (ports)** that infrastructure implements:

| Port Type | Defined In | Implemented In |
|-----------|------------|----------------|
| `IStockPositionRepository` | Domain | Infrastructure |
| `IEventBus` | Application | Infrastructure |
| `IUnitOfWork` | Application | Infrastructure |
| `IAvailabilityQueryPort` | Application (fulfillment module) | Infrastructure or Balance module adapter |
| `IIdentityService` | Application | Infrastructure (Identity module adapter) |

### 3.3 Typical Components

| Component | Purpose | IMS Examples |
|-----------|---------|--------------|
| **Commands** | Immutable write intent records | `ReserveStockCommand`, `ConfirmPutAwayCommand`, `ApproveAdjustmentCommand` |
| **Queries** | Immutable read intent records | `GetAvailabilityQuery`, `GetStockPositionQuery`, `SearchAuditTrailQuery` |
| **Command Handlers** | One handler per command — executes use case | `ReserveStockCommandHandler`, `VerifyGoodsReceiptCommandHandler` |
| **Query Handlers** | One handler per query — returns read data | `GetAvailabilityQueryHandler`, `GetDashboardQueryHandler` |
| **Saga / Process Managers** | Multi-step cross-module workflows | `OrderConfirmationSaga`, `OpeningBalanceGoLiveSaga` |
| **Saga Steps** | Individual saga activities with compensation | `ReserveStockStep`, `CompensateOrderConfirmationStep` |
| **Domain Event Handlers** | React to events from other modules | `OnPutAwayCompletedHandler` (Balance module) |
| **Application Services** | Coordinate when logic is not natural on one aggregate | `AvailabilityConfirmationService`, `TransferCapacityEvaluationService` |
| **Authorization Behaviors** | Pre-handler permission checks | `RequirePermissionBehavior`, `LocationScopeBehavior` |
| **Validation Behaviors** | Application-level validation (not domain) | Command field presence, saga preconditions |
| **Unit of Work** | Transaction boundary abstraction | `IUnitOfWork.Begin()`, `Commit()`, `Rollback()` |
| **Command Bus / Dispatcher** | Route commands to handlers | Mediator-style dispatch |
| **Query Bus / Dispatcher** | Route queries to handlers | CQRS query dispatch |
| **Integration Command Adapters** | Translate external commands to internal | `ImportSalesOrderCommandHandler` |
| **Read Model Assemblers** | Compose complex query responses | `DashboardAssembler`, `KpiReportAssembler` |

### 3.4 Application Layer Patterns by Module

| Module | Notable Application Components |
|--------|-------------------------------|
| M-04 Inventory Balance | `ReserveStockCommandHandler`, `ReceiveStockCommandHandler`; contention-sensitive handlers |
| M-07 Order Fulfillment | `OrderConfirmationSaga`, `FulfillBackorderCommandHandler` |
| M-06 Inbound Receiving | `ConfirmPutAwayCommandHandler` → publishes `PutAwayCompleted` |
| M-09 Inventory Accuracy | `ApproveAdjustmentCommandHandler` → publishes `AdjustmentApproved` |
| M-13 Intelligence | Query handlers only — `GetDashboardQueryHandler`, `ExportAuditEvidenceQueryHandler` |

### 3.5 Command Handler Flow (Reference)

```
Controller
    │
    ▼
CommandBus.Dispatch(ReserveStockCommand)
    │
    ▼
AuthorizationBehavior          ──► IIdentityService.AuthorizeAction()
    │
    ▼
ReserveStockCommandHandler
    │
    ├──► IStockPositionRepository.GetBySkuAndLocation()
    ├──► StockPosition.Reserve(quantity)     [Domain Layer]
    ├──► IStockPositionRepository.Save()
    ├──► IUnitOfWork.Commit()
    └──► IEventBus.Publish(StockReserved)    [Infrastructure port]
```

---

## 4. Domain Layer

### 4.1 Responsibilities

The Domain Layer is the **center of the architecture** — it contains the business logic, rules, and models that represent the inventory management problem space. It is **framework-agnostic** and **persistence-ignorant**.

| Responsibility | Description |
|----------------|-------------|
| **Aggregate roots** | Enforce consistency boundaries and transactional invariants |
| **Entities** | Objects with identity and lifecycle within aggregates |
| **Value objects** | Immutable, identity-less concepts (Quantity, Money, ReasonCode) |
| **Domain invariants** | Enforce business rules at aggregate boundaries (BR-001 – BR-032) |
| **Domain events** | Record meaningful business facts in past tense (`StockReserved`, `PutAwayCompleted`) |
| **Domain services** | Stateless operations spanning concepts not natural on one entity |
| **Domain policies** | Encapsulate decision rules (FEFO lot selection, freeze guard evaluation) |
| **Repository interfaces** | Define persistence contracts — no implementation |
| **Factory methods** | Controlled aggregate creation with invariant validation |
| **Ubiquitous language** | Naming aligned to SRS-DM-008 terms |

**The Domain Layer does not:**
- Know about databases, HTTP, UI, or message brokers
- Depend on application or infrastructure layers
- Perform I/O of any kind
- Reference other modules' aggregates directly — only shared identifiers

### 4.2 Allowed Dependencies

| May Depend On | Must Not Depend On |
|---------------|-------------------|
| Other domain types within the **same module** | Application Layer |
| Shared kernel value types (`ProductSku`, `LocationCode`, `UserId`) | Infrastructure Layer |
| Domain interfaces (repository ports) defined in same module | Presentation Layer |
| Standard language primitives and approved domain libraries (none required) | ORM attributes, HTTP attributes, logging frameworks |
| | Other modules' domain aggregates or entities |

```
Domain ──► Shared Kernel identifiers    ✅
Domain ──► Application                  ❌
Domain ──► Infrastructure               ❌
Domain ──► Presentation                 ❌
Domain ──► Other module domain          ❌
```

**Cross-module domain interaction** uses only:
- **Identity references** (`ProductSku`, not `Product` entity)
- **Domain events** consumed by application-layer handlers in other modules
- **Query ports** (interfaces) for read-only consultation — interface may be defined in calling module's domain or a shared contracts package; implementation in infrastructure

### 4.3 Typical Components

| Component | Purpose | IMS Examples |
|-----------|---------|--------------|
| **Aggregate Roots** | Consistency and mutation entry points | `StockPosition`, `GoodsReceipt`, `CustomerOrder`, `GovernancePolicy` |
| **Entities** | Identified objects within aggregates | `LotBatch`, `QuarantineHold`, `InventoryReservation`, `PutAway` |
| **Value Objects** | Immutable domain concepts | `Quantity`, `ProductSku`, `LocationCode`, `AtpBreakdown`, `ReasonCode`, `ApprovalThreshold` |
| **Domain Events** | Past-tense business facts | `StockReserved`, `PutAwayCompleted`, `AdjustmentApproved`, `LocationFreezeApplied` |
| **Domain Services** | Cross-aggregate logic within module | `FefoLotSelectionService`, `AtpCalculationService` |
| **Domain Policies** | Reusable rule evaluators | `SafetyStockPolicy`, `ProductEligibilityPolicy`, `SegregationOfDutiesPolicy` |
| **Repository Interfaces** | Persistence ports | `IStockPositionRepository`, `IGoodsReceiptRepository`, `IProductRepository` |
| **Specification Objects** | Composable query predicates (domain language) | `ActiveProductSpecification`, `FrozenLocationSpecification` |
| **Domain Exceptions** | Business rule violations | `InsufficientAtpException`, `LocationFrozenException`, `SegregationOfDutiesViolationException` |
| **Enumerations / Status Types** | Lifecycle states as domain concepts | `ProductLifecycleStatus`, `TransferStatus`, `AdjustmentCaseStatus` |
| **Aggregate Factories** | Controlled creation | `StockPosition.CreateOpeningBalance()`, `GoodsReceipt.CreateFromPurchaseOrder()` |

### 4.4 Domain Layer Richness by Module

| Module | Domain Complexity | Key Aggregates / Concepts |
|--------|-------------------|---------------------------|
| M-04 Inventory Balance | **Highest (core domain)** | `StockPosition` invariants: ATP = on-hand − reserved − quarantined |
| M-07 Order Fulfillment | High | `CustomerOrder` lifecycle: confirm → reserve → pick → ship |
| M-06 Inbound Receiving | High | `GoodsReceipt` — verify → discrepancy → put-away chain |
| M-09 Inventory Accuracy | High | `AdjustmentCase` state machine: variance → investigate → approve |
| M-03 Inventory Governance | Medium | `GovernancePolicy` versioning, reason code lifecycle |
| M-01 Product Catalog | Medium | `Product` lifecycle and eligibility |
| M-13 Intelligence | **Minimal** | No write aggregates; optional read value types only |

### 4.5 Aggregate Design Rules in Domain Layer

| Rule | Description |
|------|-------------|
| DL-01 | All state changes go through aggregate root public methods |
| DL-02 | One transaction modifies one aggregate |
| DL-03 | External references hold identity only — `ProductSku`, not `Product` |
| DL-04 | Domain events raised inside aggregate before persistence |
| DL-05 | Repository interfaces return aggregate roots — not ORM entities |
| DL-06 | Value objects are immutable — replacement, not mutation |
| DL-07 | Domain layer never queries other modules — consultation via ports at application layer |

---

## 5. Infrastructure Layer

### 5.1 Responsibilities

The Infrastructure Layer provides **technical capabilities** — the concrete implementations of ports defined by inner layers. It is the **outermost implementation detail**, swappable without changing business logic.

| Responsibility | Description |
|----------------|-------------|
| **Persistence** | Implement repository interfaces — ORM mappings, SQL, aggregate hydration and persistence |
| **Event bus** | Publish and subscribe to domain events — in-process bus (MVP) or message broker (future) |
| **Transactional outbox** | Ensure reliable event delivery with database commits |
| **Unit of work** | Manage database transactions and connection lifecycle |
| **ACL adapters** | Translate external system models to/from application commands (Sales/CRM, Finance ERP) |
| **Authentication adapter** | Integrate enterprise IdP (SSO), validate tokens, resolve `UserId` |
| **Authorization adapter** | Implement Identity module query ports for other modules |
| **Cross-module adapters** | Implement query/command ports between modules within the monolith |
| **Read model projections** | Maintain CQRS read stores for Intelligence module |
| **Caching** | ATP hot-path cache with invalidation on balance events |
| **Logging and audit** | Structured logging, audit record persistence |
| **Monitoring** | Metrics, health checks, distributed tracing hooks |
| **Notification delivery** | Email/SMS gateway for operational alerts |
| **Background jobs** | Scheduled tasks — reservation expiry, KPI rollups, backup verification |
| **File import/export** | Bulk product/stock import (FR-090), audit evidence export |
| **Clock / ID generation** | Injectable time source and unique ID generation for testability |

**The Infrastructure Layer does not:**
- Contain business rules or invariants
- Be referenced directly by presentation layer
- Leak ORM entities into domain or application layers

### 5.2 Allowed Dependencies

| May Depend On | Must Not Depend On |
|---------------|-------------------|
| Domain Layer (implement repository interfaces) | Presentation Layer |
| Application Layer (implement ports, event handlers wiring) | — |
| Infrastructure frameworks (ORM, HTTP clients, message brokers) | Domain aggregate internals (only through repository interfaces) |
| Other modules' **public query ports** (adapter implementations) | Other modules' private infrastructure |
| Shared kernel types | — |

```
Infrastructure ──► Domain         ✅  (implements interfaces)
Infrastructure ──► Application     ✅  (implements ports, wires handlers)
Infrastructure ──► Presentation    ❌
```

### 5.3 Typical Components

| Component | Purpose | IMS Examples |
|-----------|---------|--------------|
| **Repository Implementations** | Aggregate persistence | `StockPositionRepository`, `GoodsReceiptRepository`, `ProductRepository` |
| **ORM Entity Mappings** | Database row ↔ aggregate mapping | `StockPositionConfiguration`, `GoodsReceiptConfiguration` |
| **Unit of Work Implementation** | Transaction scope | `EfUnitOfWork`, `DbContext` wrapper |
| **In-Process Event Bus** | MVP domain event dispatch | `InProcessEventBus`, `DomainEventDispatcher` |
| **Transactional Outbox** | Reliable event publish | `OutboxMessage`, `OutboxProcessor` |
| **Event Handlers (wiring)** | Register handlers with bus | `EventHandlerRegistry`, module startup configuration |
| **Cross-Module Adapters** | Inter-module port implementations | `BalanceAvailabilityQueryAdapter` (fulfillment → balance) |
| **ACL Adapters (external)** | External system translation | `SalesCrmOrderAdapter`, `FinanceErpValuationAdapter` |
| **Identity Provider Adapter** | SSO integration | `EntraIdAuthenticationAdapter`, `JwtTokenValidator` |
| **Read Model Repositories** | CQRS query stores | `MovementHistoryReadRepository`, `DashboardReadRepository` |
| **Projection Handlers** | Update read models on events | `OnStockReservedProjectionHandler` |
| **Cache Providers** | Performance optimization | `AtpCacheService` with event-driven invalidation |
| **Logging Adapter** | Structured audit logging | `SerilogAuditLogger`, `AuditTrailWriter` |
| **Notification Adapter** | Alert delivery | `EmailNotificationGateway` (SVC-02) |
| **Import/Export Adapters** | Bulk data operations | `ProductStockBulkImporter`, `AuditEvidenceExporter` |
| **Background Job Scheduler** | Async processing | `ReservationExpiryJob`, `KpiRollupJob` |
| **Health Check Implementations** | Ops monitoring | `DatabaseHealthCheck`, `EventBusHealthCheck` |
| **Migration Scripts** | Schema versioning | Per-module database migrations |

### 5.4 Infrastructure by Concern

| Concern | Components | NFR Alignment |
|---------|------------|---------------|
| **Write persistence** | Repositories, UoW, outbox | NFR-REL-006 (integrity), NFR-BDR-001 (RPO) |
| **Read persistence** | Read repositories, projections | NFR-PERF-002 (ATP), NFR-PERF-004 (dashboards) |
| **Security** | Auth adapter, encryption | NFR-SEC-001 – NFR-SEC-032 |
| **Observability** | Logging, metrics, tracing | NFR-LOG, NFR-MON |
| **Integration** | ACL adapters | TEC-04, TEC-05, HS-014 |
| **Resilience** | Outbox, retry, idempotency store | NFR-REL-011 – NFR-REL-014 |

### 5.5 Cross-Module Infrastructure Pattern

Cross-module integration within the monolith uses **infrastructure adapters** implementing application-layer ports:

```
┌─────────────────────┐         ┌──────────────────────────────┐
│ Fulfillment Module  │         │ Balance Module               │
│  Application Layer  │         │  Application Layer           │
│  IAtpQueryPort ◄────┼─────────┼── BalanceAtpQueryAdapter     │
│                     │         │       (Infrastructure)       │
└─────────────────────┘         └──────────────────────────────┘
```

The port interface (`IAtpQueryPort`) is defined in the **calling module's application layer**. The adapter is implemented in **infrastructure** and may live in either module's infrastructure package, registered at application composition root.

---

## 6. Cross-Cutting Concerns Placement

| Concern | Primary Layer | Notes |
|---------|---------------|-------|
| Business rules (BR-xxx) | **Domain** | Never in presentation or infrastructure |
| Use case orchestration | **Application** | Handlers and sagas |
| Syntactic input validation | **Presentation** | Format, required fields |
| Permission checks | **Application** | Via `IIdentityService` port before handler |
| Authentication | **Infrastructure** (adapter) + **Presentation** (middleware) | Token validation in infra; extraction in presentation |
| Transaction boundaries | **Application** | `IUnitOfWork` port |
| Audit trail recording | **Infrastructure** (persistence) | Triggered by domain events → Intelligence projections |
| API rate limiting | **Presentation** or **Infrastructure** | Edge concern |
| Correlation / tracing | **Presentation** (attach) + **Infrastructure** (propagate) | |
| Idempotency | **Application** (logic) + **Infrastructure** (store) | |
| Caching | **Infrastructure** | ATP cache with domain-event invalidation |
| Exception mapping | **Presentation** | HTTP status from domain exception types |

---

## 7. Dependency Matrix (Complete)

| Layer | Presentation | Application | Domain | Infrastructure |
|-------|:---:|:---:|:---:|:---:|
| **Presentation** | — | ✅ | ❌ | ❌ |
| **Application** | ❌ | internal | ✅ | ❌ (ports only) |
| **Domain** | ❌ | ❌ | internal | ❌ (interfaces only) |
| **Infrastructure** | ❌ | ✅ | ✅ | internal |

---

## 8. Request Lifecycle (End-to-End)

### 8.1 Write Path — Confirm Customer Order

```
1. [Presentation]  OrderController.ConfirmOrder(ConfirmOrderRequest dto)
                      → maps to ConfirmCustomerOrderCommand
2. [Application]     AuthorizationBehavior checks permission
3. [Application]     ConfirmCustomerOrderCommandHandler
                      → starts OrderConfirmationSaga
4. [Application]     Saga step: CustomerOrder.Confirm()          [Domain]
5. [Infrastructure]  CustomerOrderRepository.Save()
6. [Application]     Saga step: ReserveStockCommand → Balance module port
7. [Application]     ReserveStockCommandHandler (Balance module)
                      → StockPosition.Reserve()                   [Domain]
8. [Infrastructure]  StockPositionRepository.Save()
                      → UnitOfWork.Commit()
                      → Outbox.Publish(StockReserved)
9. [Infrastructure]  EventBus dispatches StockReserved
10.[Application]     Fulfillment saga resumes on StockReserved event
11.[Presentation]    OrderController returns ConfirmOrderResponse
```

### 8.2 Read Path — ATP Lookup

```
1. [Presentation]  StockController.GetAvailability(sku, location)
                      → maps to GetAvailabilityQuery
2. [Application]     GetAvailabilityQueryHandler
3. [Infrastructure]  AtpReadRepository (or cache) returns projection
4. [Presentation]    Maps to AvailabilityResponse DTO
```

*Read path bypasses domain aggregate load for performance (CQRS) — NFR-PERF-002.*

---

## 9. Layer Implementation Standards

| Standard ID | Rule |
|-------------|------|
| LS-01 | Every module packages layers as `ModuleName.Presentation`, `.Application`, `.Domain`, `.Infrastructure` |
| LS-02 | Domain project has **zero** references to outer layer projects |
| LS-03 | Application project references Domain only — infrastructure wired at composition root |
| LS-04 | Repository interfaces live in Domain; implementations live in Infrastructure |
| LS-05 | Commands and queries are immutable records in Application layer |
| LS-06 | One command handler per command; handlers are stateless |
| LS-07 | Domain events are raised inside aggregates, collected by application layer after save |
| LS-08 | Cross-module calls use ports — never `using OtherModule.Domain` |
| LS-09 | Intelligence module has no command handlers for transactional writes |
| LS-10 | Integration tests target Application + Infrastructure with in-memory or test database adapters |

---

## 10. Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Solution Architect | | | |
| DDD Solution Architect | | | |
| Delivery Lead | | | |
| Tech Lead | | | |

---

*End of Layered Architecture Design*

*Document ID: SRS-SA-004 | Version 1.0 | July 6, 2026*
