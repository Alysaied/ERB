# Integration Architecture Design
## Inventory Management System

---

## Document Information

| Attribute | Detail |
|-----------|--------|
| **Document ID** | SRS-SA-005 |
| **Document Title** | Integration Architecture Design — Inventory Management System |
| **Version** | 1.0 |
| **Status** | Draft |
| **Document Owner** | Solution Architect |
| **Prepared For** | Delivery leads, integration architects, security, and development squads |
| **Date** | July 6, 2026 |
| **Classification** | Internal — Architecture Confidential |
| **Scope** | Integration patterns, boundaries, and communication styles — no message broker selection, API specification, or protocol implementation |

### Related Documents

| Document | ID | Relationship |
|----------|-----|--------------|
| Architecture Vision | SRS-SA-001 | Event-driven direction, ACL principles |
| System Modules Design | SRS-SA-003 | Module public interfaces and dependencies |
| Layered Architecture Design | SRS-SA-004 | Port/adapter placement |
| System Context | System Context doc | External systems and data flows |
| Bounded Contexts | SRS-DM-007 | Context map and integration patterns |
| Event Storming Board | SRS-ES-008 | End-to-end lifecycle chains |

### Document Purpose

This document defines **how the Inventory Management System integrates internally across its 13 modules and externally with enterprise systems and partners**. It establishes communication styles, synchronous versus asynchronous rules, and hard integration boundaries — so that quantity integrity, auditability, and phased delivery are preserved as integrations grow in complexity.

---

## 1. Integration Architecture Overview

### 1.1 Design Principles

| Principle | Statement |
|-----------|-----------|
| **IB-01 — Inventory Balance is the quantity authority** | No module other than Inventory Balance (M-04) mutates on-hand, reserved, or quarantined quantities |
| **IB-02 — Events for state propagation** | Cross-module state changes propagate through domain events, not shared mutable data |
| **IB-03 — Queries for read-only consultation** | Synchronous cross-module calls are permitted only for read-only lookups and pre-condition checks |
| **IB-04 — ACL at system boundary** | External models are translated at the boundary; foreign concepts never enter the domain layer |
| **IB-05 — Published language for identifiers** | Cross-boundary references use shared value identifiers (`ProductSku`, `LocationCode`) — not entity references |
| **IB-06 — Fail closed on integration uncertainty** | When ATP, freeze, or authorization cannot be confirmed, the operation is rejected — not guessed |
| **IB-07 — Idempotent integration handlers** | Duplicate event or command delivery must not double-apply stock mutations |
| **IB-08 — Observable integration flows** | Every cross-module and external exchange is traceable via correlation ID in audit and movement history |

### 1.2 Integration Topology

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                           EXTERNAL INTEGRATION ZONE                              │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ │
│  │ Sales /  │ │ Finance  │ │  Sales   │ │Marketing │ │    HR    │ │ Customs  │ │
│  │   CRM    │ │   ERP    │ │ Channel  │ │ Campaign │ │ Directory│ │ Regulatory│ │
│  └────┬─────┘ └────┬─────┘ └────┬─────┘ └────┬─────┘ └────┬─────┘ └────┬─────┘ │
│       │  ACL       │  ACL       │  ACL       │  ACL       │  ACL       │  ACL    │
└───────┼────────────┼────────────┼────────────┼────────────┼────────────┼────────┘
        │            │            │            │            │            │
┌───────▼────────────▼────────────▼────────────▼────────────▼────────────▼────────┐
│                        IMS MODULAR MONOLITH BOUNDARY                             │
│  ┌─────────────────────────────────────────────────────────────────────────────┐ │
│  │                     PRESENTATION / API GATEWAY LAYER                         │ │
│  └──────────────────────────────────┬──────────────────────────────────────────┘ │
│                                     │                                            │
│  ┌──────────────┐  ┌──────────────┐ │ ┌──────────────┐  ┌──────────────────┐  │
│  │  Fulfillment │  │  Inbound     │ │ │  Procurement │  │    Campaign      │  │
│  │    M-07      │  │    M-06      │ │ │     M-05     │  │      M-11        │  │
│  └──────┬───────┘  └──────┬───────┘ │ └──────┬───────┘  └────────┬─────────┘  │
│         │    sync query   │         │         │                   │             │
│         │    + saga       │ events  │         │                   │ events      │
│         ▼                 ▼         ▼         ▼                   ▼             │
│  ┌─────────────────────────────────────────────────────────────────────────┐  │
│  │              INVENTORY BALANCE (M-04) — Core Integration Hub             │  │
│  └─────────────────────────────────────────────────────────────────────────┘  │
│         ▲                 ▲                   ▲                   ▲             │
│  ┌──────┴───────┐  ┌──────┴───────┐  ┌──────┴───────┐  ┌──────┴─────────┐   │
│  │   Transfer   │  │   Accuracy   │  │   Returns    │  │    Network     │   │
│  │     M-08     │  │     M-09     │  │     M-10     │  │      M-02      │   │
│  └──────────────┘  └──────────────┘  └──────────────┘  └────────────────┘   │
│                                                                               │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │
│  │   Catalog   │  │ Governance  │  │  Identity   │  │   Intelligence      │  │
│  │    M-01     │  │    M-03     │  │    M-12     │  │      M-13           │  │
│  │  (upstream) │  │ (consulted) │  │ (consulted) │  │  (event subscriber) │  │
│  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────────────┘  │
│                                                                               │
│  ┌─────────────────────────────────────────────────────────────────────────┐  │
│  │              INTERNAL EVENT BUS (in-process MVP → outbox evolution)      │  │
│  └─────────────────────────────────────────────────────────────────────────┘  │
└───────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Internal Module Communication

### 2.1 Communication Mechanisms

Internal integration uses **three mechanisms**, applied according to the nature of the interaction:

| Mechanism | Purpose | Consistency | Coupling |
|-----------|---------|-------------|----------|
| **Published Commands** | Request a state change in another module | Strong within target aggregate; eventual across modules | Low — via port interface |
| **Published Queries** | Read-only consultation | Read-your-writes within module; eventually consistent for projections | Low — via port interface |
| **Domain Events** | Notify that a business fact occurred | Eventual consistency | Lowest — subscriber unaware of publisher internals |

### 2.2 Module Integration Roles

| Role | Modules | Integration Behaviour |
|------|---------|----------------------|
| **Upstream reference data** | M-01 Catalog, M-02 Network, M-03 Governance, M-12 Identity | Consulted synchronously; emit change events for projections |
| **Core state authority** | M-04 Inventory Balance | Receives commands and events; sole ATP mutator; emits all balance change events |
| **Operational consumers** | M-05–M-11 | Consult upstream; command/event to Balance for quantity changes |
| **Read-only subscriber** | M-13 Intelligence | Subscribes to all material events; never initiates writes to transactional modules |

### 2.3 Internal Integration Catalogue

#### 2.3.1 Upstream Consultation (Synchronous Query)

| Consumer Module | Provider Module | Query Port | Business Purpose |
|-----------------|-----------------|------------|------------------|
| M-04 Balance | M-01 Catalog | `ValidateProductEligibility` | Block mutations on discontinued SKU |
| M-04 Balance | M-02 Network | `IsLocationTransactionallyActive`, `IsLocationFrozen` | Gate quantity changes |
| M-04 Balance | M-03 Governance | `EvaluateSafetyStockOverride` | BR-010 enforcement |
| M-05 Procurement | M-01, M-02, M-04 | Product/location validation, `GetNetworkAvailability` | BR-011 before requisition |
| M-06 Inbound | M-01, M-02, M-03, M-05 | Product, location, tolerance, PO validation | Receipt authorization |
| M-07 Fulfillment | M-01, M-02, M-04, M-11 | Eligibility, freeze, `GetAvailability`, ring-fence check | BR-001, BR-029 |
| M-08 Transfer | M-01, M-02, M-04 | Product, freeze, `EvaluateSourceTransferCapacity` | BR-012 |
| M-09 Accuracy | M-01, M-03, M-04, M-12 | ABC class, thresholds, system quantity, SoD | Blind count variance |
| M-10 Returns | M-01, M-02, M-07 | Product, location, original order validation | BR-025 |
| M-11 Campaign | M-01, M-02, M-04 | Product, location, available quantity | Ring-fence feasibility |
| All operational | M-12 Identity | `AuthorizeAction`, `GetUserAttribution` | RBAC and audit |
| All operational | M-03 Governance | `ValidateReasonCode`, `GetApprovalThreshold` | Governance consultation |

#### 2.3.2 Cross-Module Commands (Synchronous Write Request)

Used when one module must **request** a state change in another within a coordinated workflow (typically inside a saga):

| Caller Module | Target Module | Command | Saga Context |
|---------------|---------------|---------|--------------|
| M-07 Fulfillment | M-04 Balance | `ReserveStock` | Order confirmation saga |
| M-07 Fulfillment | M-04 Balance | `ReleaseReservation` | Order cancellation |
| M-07 Fulfillment | M-04 Balance | `DeductStockForShipment` | Post-pick shipment (or via event) |
| M-08 Transfer | M-04 Balance | `DeductStockForTransfer`, `ReceiveStockFromTransfer` | Transfer dispatch/receive |
| M-04 Balance | M-04 Balance | Internal only | Opening balance establishment |

*Preferred pattern: caller module publishes intent; Balance module executes atomically and publishes result event.*

#### 2.3.3 Domain Event Choreography (Asynchronous)

| Publisher Module | Event | Subscriber Module(s) | Subscriber Reaction |
|------------------|-------|----------------------|---------------------|
| M-06 Inbound | `PutAwayCompleted` | M-04 Balance | `ReceiveStock` |
| M-07 Fulfillment | `ShipmentDispatched` | M-04 Balance | `DeductStockForShipment` |
| M-08 Transfer | `TransferDispatched` | M-04 Balance | `DeductStockForTransfer` |
| M-08 Transfer | `TransferReceived` | M-04 Balance | `ReceiveStockFromTransfer` |
| M-09 Accuracy | `AdjustmentApproved` | M-04 Balance | `ApplyApprovedAdjustment` |
| M-09 Accuracy | `WriteOffApproved` | M-04 Balance | `ApplyApprovedWriteOff` |
| M-09 Accuracy | `LocationFreezeImposed` | M-02 Network | `ApplyLocationFreeze` |
| M-09 Accuracy | `LocationFreezeReleased` | M-02 Network | `ReleaseLocationFreeze` |
| M-10 Returns | `ReturnRestocked` | M-04 Balance | `ReceiveStock` |
| M-10 Returns | `ReturnQuarantined` | M-04 Balance | `ApplyQuarantineHold` |
| M-10 Returns | `ReturnWrittenOff` | M-09 Accuracy | Open adjustment case |
| M-11 Campaign | `PromotionalStockAllocated` | M-04 Balance | `SegregatePromotionalStock` |
| M-11 Campaign | `PromotionalAllocationReleased` | M-04 Balance | `ReleasePromotionalAllocation` |
| M-05 Procurement | `PurchaseOrderPlaced` | M-06 Inbound | Enable receipt against PO |
| M-04 Balance | `StockReceived` | M-07 Fulfillment | Backorder fulfillment policy |
| M-04 Balance | `LowStockThresholdBreached` | M-05 Procurement | Replenishment alert |
| **All transactional** | *material events* | M-13 Intelligence | Update read projections |
| M-13 Intelligence | `OperationalAlertRaised` | Notification gateway | Deliver alert |

### 2.4 Saga-Orchestrated Workflows (Internal)

Cross-module workflows that require **compensation** on partial failure are orchestrated by sagas in the **calling module's application layer**:

| Saga ID | Orchestrator | Participants | Compensation on Failure |
|---------|--------------|--------------|-------------------------|
| SAG-01 | M-07 Fulfillment | M-04 Balance | Cancel order confirmation; release partial reservation |
| SAG-02 | M-06 Inbound | M-04 Balance | Reverse put-away intent; flag receipt incomplete |
| SAG-03 | M-08 Transfer | M-04 Balance (×2) | Restore source if dispatch fails; cancel in-transit |
| SAG-04 | M-09 Accuracy | M-02 Network, M-04 Balance | Release freeze if certification fails |
| SAG-05 | M-02 Network | M-04 Balance | Block activation if opening balance fails |
| SAG-06 | M-11 Campaign | M-04 Balance | Release partial allocation on campaign abort |
| SAG-07 | M-10 Returns | M-04 or M-09 | Roll back disposition if downstream rejects |

```
SAG-01: Order Confirmation Saga (M-07 → M-04)

  ConfirmCustomerOrder          ReserveStock              StockReserved
  ───────────────────►  ───────────────────►  ───────────────────►
        │                        │                         │
        │                        │ fail                    │ success
        │                        ▼                         ▼
        │               CompensateOrder            CompleteConfirmation
        │               (release / cancel)
        ▼
   OrderConfirmationFailed
```

### 2.5 Internal Event Bus Architecture

| Aspect | MVP (Phase 1) | Evolution (Phase 2–3) |
|--------|---------------|----------------------|
| **Transport** | In-process event dispatcher within modular monolith | Transactional outbox with optional external broker for Intelligence extraction |
| **Delivery** | At-least-once within process; handler idempotency required | At-least-once across processes; deduplication by event ID |
| **Ordering** | Per-aggregate ordering guaranteed | Per-aggregate partition key preserved |
| **Failure handling** | Retry with backoff; dead-letter queue for poison events | Same + ops alerting |
| **Transactional integrity** | Domain events collected in same DB transaction as aggregate save (outbox pattern) | Outbox processor publishes after commit |

### 2.6 Internal Integration Anti-Patterns (Prohibited)

| Anti-Pattern | Why Prohibited |
|--------------|----------------|
| Shared database tables across modules | Bypasses aggregate invariants; creates hidden coupling |
| Direct import of another module's domain entities | Violates bounded context boundary |
| Synchronous cross-module call chain > 2 hops on hot path | Threatens NFR-PERF-002 (2s ATP lookup) |
| Balance module calling Fulfillment | Inverts dependency; Balance must not know consumers |
| Intelligence writing back to transactional modules | Corrupts write model; violates CQRS |
| Polling another module's database | Breaks encapsulation and module ownership |

---

## 3. External Integrations

### 3.1 External Integration Zones

| Zone | Systems | IMS Role | Integration Maturity |
|------|---------|----------|---------------------|
| **Commercial demand** | EXT-01 Sales/CRM, EXT-03 Sales Channel | Fulfillment consumer; ATP publisher | MVP: manual/indirect → Phase 2+: API |
| **Financial control** | EXT-02 Finance ERP/GL | Operational facts publisher; match participant | MVP: export → Phase 3: ACL |
| **Supply chain partners** | EXT-04 Supplier, EXT-05 Carrier | Human-mediated operational recording | MVP: no direct system link |
| **Commercial planning** | EXT-07 Marketing | Campaign intent consumer | Phase 2 |
| **Identity** | EXT-08 HR Directory, SVC-01 IdP | Identity consumer | MVP: manual/sync |
| **Regulatory** | EXT-09 Customs | Clearance fact consumer | Phase 2 (if in scope) |
| **Notifications** | SVC-02 Email/SMS | Alert publisher | MVP |
| **Audit** | External Auditor | Read-only evidence consumer | MVP |

### 3.2 External System Integration Catalogue

#### EXT-01 — Sales / Order Management (CRM)

| Attribute | Detail |
|-----------|--------|
| **IMS modules** | M-07 Order Fulfillment (primary), M-13 Intelligence (status feed) |
| **Direction** | Inbound: orders; Outbound: ATP, reservation, fulfillment status |
| **ACL owner** | Fulfillment module — `SalesOrderInboundPort`, `FulfillmentStatusOutboundPort` |
| **Published language** | `CustomerOrderId`, `ProductSku`, `LocationCode`, `ReservationId`, `ShipmentId` |
| **Phase** | MVP: CS enters orders manually; Phase 2+: automated order import API |
| **Risk** | Channel overselling until integration live (BRD risk register) — manual sync interim |

| Interaction | Style | Data Exchanged |
|-------------|-------|----------------|
| Order intake | Sync (Phase 2+) / Manual (MVP) | Order lines, ship-from preference, customer reference |
| Availability check | Sync | SKU, location → ATP quantity |
| Reservation confirmation | Async event → outbound notification | Reservation ID, expiry |
| Shipment notice | Async event → outbound notification | Shipment ID, carrier ref, line quantities |

#### EXT-02 — Finance ERP / General Ledger

| Attribute | Detail |
|-----------|--------|
| **IMS modules** | M-06 Inbound (three-way match), M-13 Intelligence (valuation), M-04 Balance (movement facts) |
| **Direction** | Inbound: GL balance, cost parameters; Outbound: valuation snapshot, adjustments, match results |
| **ACL owner** | Intelligence module — `FinanceValuationExportPort`; Inbound — `FinanceMatchStatusPort` |
| **Phase** | MVP: scheduled file export (TEC-05); Phase 3: automated reconciliation ACL |
| **Open decision** | HS-014 — IMS owns match vs. ERP owns match; architecture assumes IMS operational SoR, Finance payment authority |

| Interaction | Style | Data Exchanged |
|-------------|-------|----------------|
| Valuation snapshot export | Async (scheduled) | Period-end inventory value by SKU/location |
| Adjustment/write-off facts | Async (event-driven export) | Reason code, quantity, value, approver |
| Three-way match result | Async | PO, receipt, invoice match status |
| Consignment ownership transfer | Async | Ownership change event for GL posting |
| GL balance import | Async (scheduled) | Reconciliation comparison input |

#### EXT-03 — Sales Channel / E-Commerce / Marketplace

| Attribute | Detail |
|-----------|--------|
| **IMS modules** | M-13 Intelligence (ATP feed), M-04 Balance (source of truth) |
| **Direction** | Outbound: available quantity feed |
| **ACL owner** | Intelligence or dedicated integration adapter |
| **Phase** | Phase 2+ (TEC-04 — no real-time MVP) |
| **Constraint** | Feed must reflect ATP, not on-hand — prevent oversell (BR-001) |

| Interaction | Style | Data Exchanged |
|-------------|-------|----------------|
| ATP / availability feed | Async (scheduled or event-triggered) | SKU, channel, available quantity |
| Stockout notification | Async | SKU, channel, alert |

#### EXT-04 — Supplier / Vendor

| Attribute | Detail |
|-----------|--------|
| **IMS modules** | M-05 Procurement, M-06 Inbound |
| **Direction** | Human-mediated — buyer sends PO externally; clerk records receipt in IMS |
| **Phase** | MVP: no EDI/API; future: ASN inbound adapter |
| **Boundary** | Supplier never executes commands in IMS |

| Interaction | Style | Data Exchanged |
|-------------|-------|----------------|
| PO issuance | Outbound (human/process) | PO document |
| ASN / delivery notice | Inbound (human entry MVP) | Expected delivery, carrier |
| Supplier invoice | Inbound (human or Phase 2 scan) | Invoice lines for three-way match |

#### EXT-05 — Logistics / Carrier Partner

| Attribute | Detail |
|-----------|--------|
| **IMS modules** | M-07 Fulfillment, M-08 Transfer |
| **Direction** | Human-mediated tracking entry |
| **Phase** | MVP: operational workflow; future: carrier tracking API |

| Interaction | Style | Data Exchanged |
|-------------|-------|----------------|
| Dispatch notice | Outbound (human) | Shipment/transfer details |
| Delivery confirmation | Inbound (human) | Proof of delivery, delay reason |

#### EXT-07 — Marketing / Campaign Planning

| Attribute | Detail |
|-----------|--------|
| **IMS modules** | M-11 Commercial Campaign |
| **Direction** | Inbound: campaign plan; Outbound: readiness status |
| **ACL owner** | Campaign module — `CampaignPlanInboundPort` |
| **Phase** | Phase 2 |

| Interaction | Style | Data Exchanged |
|-------------|-------|----------------|
| Campaign plan import | Sync or batch | SKU list, quantity, channel, period |
| Readiness status | Async outbound | Allocated vs. required, gap alert |

#### EXT-08 — HR / Enterprise Directory

| Attribute | Detail |
|-----------|--------|
| **IMS modules** | M-12 Identity & Access |
| **Direction** | Inbound: employee identity feed |
| **ACL owner** | Identity module — `DirectorySyncPort` |
| **Phase** | MVP: manual provisioning or periodic sync |

| Interaction | Style | Data Exchanged |
|-------------|-------|----------------|
| User provisioning | Async (scheduled sync) | Employee ID, name, department, status |
| Deprovisioning | Async | Termination status → account deactivation |

#### EXT-09 — Customs / Regulatory Authority

| Attribute | Detail |
|-----------|--------|
| **IMS modules** | M-04 Balance (quarantine), M-06 Inbound |
| **Direction** | Inbound: clearance decisions via compliance role |
| **Phase** | Phase 2 if bonded inventory in scope (HS-009) |

| Interaction | Style | Data Exchanged |
|-------------|-------|----------------|
| Clearance granted | Sync (human entry) | Document reference, cleared quantity |
| Hold / recall notice | Sync (human entry) | Affected lots, locations |

#### SVC-01 — Enterprise Identity Provider (SSO)

| Attribute | Detail |
|-----------|--------|
| **IMS modules** | M-12 Identity |
| **Direction** | Inbound: authentication tokens and claims |
| **Style** | Synchronous per request (auth handshake) |

#### SVC-02 — Email / Notification Gateway

| Attribute | Detail |
|-----------|--------|
| **IMS modules** | M-13 Intelligence |
| **Direction** | Outbound: alert payloads |
| **Style** | Asynchronous — fire-and-forget with delivery status callback |
| **SLA** | NFR-PERF-014 — alerts within 5 minutes of trigger |

### 3.3 External Integration Phasing

| Phase | External Integrations Activated |
|-------|--------------------------------|
| **Phase 1 — MVP** | SVC-01 SSO, SVC-02 notifications, EXT-08 manual/sync, EXT-02 file export, EXT-01 manual order entry |
| **Phase 2** | EXT-01 API order feed, EXT-03 ATP channel feed, EXT-07 campaign import, EXT-04 ASN (optional) |
| **Phase 3** | EXT-02 automated Finance ACL, EXT-03 real-time feeds, EXT-05 carrier API |

---

## 4. Communication Style

### 4.1 Communication Style Catalogue

| Style | Description | When Used |
|-------|-------------|-----------|
| **Request-Reply (Sync)** | Caller waits for response before proceeding | Read-only queries, pre-condition checks, user-facing ATP lookup |
| **Command Dispatch (Sync)** | Caller sends command; target commits atomically; returns success/failure | Saga steps requiring immediate confirmation (reserve stock) |
| **Event Notification (Async)** | Publisher emits fact; subscribers react independently | Post-commit state propagation, projections, alerts |
| **Saga Choreography (Mixed)** | Sync steps coordinated with async event continuations | Multi-module workflows with compensation |
| **Batch Export / Import** | Scheduled file or bulk data transfer | Finance export, go-live import (FR-090), directory sync |
| **Fire-and-Forget** | Outbound notification with no response required | Email alerts, channel feed push |
| **Human-Mediated** | External party communicates outside system; internal user records outcome | Supplier PO, carrier tracking, MVP order entry |

### 4.2 Communication Style by Integration Type

```
┌────────────────────┬──────────────────────────────────────────────────────────┐
│ Integration Type   │ Primary Communication Style                              │
├────────────────────┼──────────────────────────────────────────────────────────┤
│ Master data lookup │ Request-Reply (Sync)                                     │
│ Authorization      │ Request-Reply (Sync)                                     │
│ User-facing ATP    │ Request-Reply (Sync) — CQRS read path                    │
│ Stock mutation     │ Command Dispatch (Sync) OR Event Notification (Async)  │
│ Cross-module flow  │ Saga Choreography (Mixed)                                │
│ Read projections   │ Event Notification (Async)                               │
│ External inbound   │ ACL Translate → Command Dispatch                         │
│ External outbound  │ Event Notification → ACL Translate → Batch/API           │
│ Alerts             │ Fire-and-Forget                                          │
│ Partner (MVP)      │ Human-Mediated                                           │
└────────────────────┴──────────────────────────────────────────────────────────┘
```

### 4.3 Published Language (Integration Contract)

All integrations — internal and external — exchange data through the **published language** of immutable identifiers and value objects:

| Concept | Format | Example |
|---------|--------|---------|
| Product identity | `ProductSku` | `SKU-12345` |
| Location identity | `LocationCode` | `WH-EAST-01` |
| Quantity | `Quantity` + `UnitOfMeasure` | `100 EA` |
| User identity | `UserId` | `usr-abc-001` |
| Temporal | `Instant` (UTC) + location business calendar | ISO-8601 |
| Money | `Amount` + `Currency` | `1500.00 USD` |
| Event envelope | `EventId`, `CorrelationId`, `CausationId`, `OccurredAt` | Traceable audit chain |

**Foreign concepts are translated at the ACL** — e.g., CRM `orderLineId` maps to IMS `CustomerOrderId` + line reference; never stored as CRM's native structure in domain layer.

### 4.4 API Exposure Style (IMS as Provider)

When IMS exposes interfaces to external consumers:

| Exposure | Consumers | Content |
|----------|-----------|---------|
| **Operational API** | CRM, mobile warehouse, web UI | Commands and queries for active workflows |
| **Read API** | CRM, channels, executive BI | ATP, status, dashboards (read-only) |
| **Integration API** | Finance, marketing | Scheduled exports, webhook callbacks |
| **Audit API** | Internal/external auditor | Read-only evidence packages |

*Detailed API specification is out of scope for this document — style and boundary only.*

---

## 5. Synchronous vs Asynchronous Interactions

### 5.1 Decision Framework

```
                    ┌─────────────────────────────────────┐
                    │ Does the caller need the result     │
                    │ to proceed or respond to the user?  │
                    └─────────────────┬───────────────────┘
                                      │
                         ┌────────────┴────────────┐
                         │ YES                     │ NO
                         ▼                         ▼
              ┌─────────────────────┐    ┌─────────────────────┐
              │ Is it a read-only   │    │ ASYNC               │
              │ lookup or auth check? │    │ Domain event or     │
              └─────────┬───────────┘    │ outbound notification│
                        │                └─────────────────────┘
              ┌─────────┴─────────┐
              │ YES               │ NO (write)
              ▼                   ▼
       ┌─────────────┐    ┌─────────────────────┐
       │ SYNC QUERY  │    │ Is it within a saga │
       │             │    │ requiring immediate │
       └─────────────┘    │ commit confirmation?│
                            └─────────┬───────────┘
                                      │
                            ┌─────────┴─────────┐
                            │ YES               │ NO
                            ▼                   ▼
                     ┌─────────────┐    ┌─────────────┐
                     │ SYNC COMMAND│    │ ASYNC EVENT │
                     │ (saga step) │    │ preferred   │
                     └─────────────┘    └─────────────┘
```

### 5.2 Synchronous Interactions

**Use when:** immediate answer required; user or saga is waiting; read-only consultation; pre-condition gate.

| Interaction | Modules / External | Rationale |
|-------------|-------------------|-----------|
| ATP availability lookup | M-04 → caller / EXT-01 | NFR-PERF-002 — 2s response; user on phone |
| Product lifecycle check | M-01 → consumer | Block invalid transaction before attempt |
| Location freeze check | M-02 → consumer | BR-024 — reject before mutation |
| Permission authorization | M-12 → all | NFR-SEC — fail closed before command |
| Governance threshold lookup | M-03 → consumer | Approval routing decision |
| Reserve stock (saga step) | M-07 → M-04 | Order confirmation cannot complete without reservation result |
| SSO authentication | SVC-01 → M-12 | Per-request identity validation |
| Campaign readiness check | M-11 → M-04 | Sync quantity check before allocation command |

**Constraints on synchronous calls:**

| Constraint | Limit |
|------------|-------|
| Hot-path chain depth | ≤ 2 cross-module sync calls (e.g., Fulfillment → Balance) |
| Timeout | Fail and compensate — do not block indefinitely |
| Retry | Idempotent queries only; commands via saga retry with deduplication |
| Circuit breaking | Degraded mode: reject writes; serve cached ATP with staleness indicator for reads |

### 5.3 Asynchronous Interactions

**Use when:** state propagation after commit; projections; notifications; external system feeds; no caller waiting.

| Interaction | Modules / External | Rationale |
|-------------|-------------------|-----------|
| Put-away → stock available | M-06 → M-04 | Decouple receiving from balance; eventual consistency acceptable (seconds) |
| Shipment → stock deduction | M-07 → M-04 | Post-commit propagation |
| Adjustment approved → apply | M-09 → M-04 | Governance pipeline complete before mutation |
| All events → Intelligence | M-01–M-12 → M-13 | CQRS projection update |
| Low-stock alert → Procurement | M-04 → M-05 | Replenishment is reaction, not blocking |
| Backorder fulfill on receipt | M-04 → M-07 | Policy reaction to `StockReceived` |
| Valuation export → Finance | M-13 → EXT-02 | Scheduled batch; no real-time GL need |
| ATP feed → Sales Channel | M-13 → EXT-03 | Channel tolerance for minutes-level lag |
| Operational alert → Email | M-13 → SVC-02 | NFR-PERF-014 — 5 min SLA |
| Directory sync → Identity | EXT-08 → M-12 | HR changes not real-time critical |

**Asynchronous delivery guarantees:**

| Guarantee | Requirement |
|-----------|-------------|
| Durability | Events persisted in outbox before commit acknowledgment |
| At-least-once delivery | Handlers must be idempotent |
| Ordering | Per-aggregate event sequence preserved |
| Latency target | Internal event propagation < 5 seconds under normal load |
| Visibility | Correlation ID links saga steps across async boundaries |

### 5.4 Synchronous vs Asynchronous Summary Matrix

| Flow | Sync | Async | Notes |
|------|:----:|:-----:|-------|
| ATP inquiry (user) | ✅ | | CQRS read path |
| Product/location validation | ✅ | | Pre-condition |
| Order confirm → reserve | ✅ | | Saga step 1–2 |
| Reserve → stock event | | ✅ | Post-commit notification to Intelligence |
| Put-away → stock increase | | ✅ | Preferred over sync command |
| Pick → ship → deduct | ✅ confirm | ✅ propagate | Pick sync; deduct via event |
| Count → freeze → adjust | Mixed | ✅ | Freeze sync apply; adjust async |
| Dashboard refresh | ✅ | | Query projection |
| Finance month-end export | | ✅ | Scheduled batch |
| CRM order import (Phase 2) | ✅ | | Translate + command at boundary |
| Email alert | | ✅ | Fire-and-forget |

---

## 6. Integration Boundaries

### 6.1 Boundary Model

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ BOUNDARY 4: External Partner Zone (no system access)                          │
│   Supplier, Carrier, Customer — human-mediated facts enter via IMS users      │
├─────────────────────────────────────────────────────────────────────────────┤
│ BOUNDARY 3: External System Zone (ACL required)                              │
│   CRM, ERP, Channel, Marketing, HR, Customs — translated at adapter ports   │
├─────────────────────────────────────────────────────────────────────────────┤
│ BOUNDARY 2: IMS Modular Monolith Shell                                      │
│   API Gateway, auth middleware, correlation, rate limiting                    │
├─────────────────────────────────────────────────────────────────────────────┤
│ BOUNDARY 1: Module-to-Module (published commands, queries, events)           │
│   13 bounded context modules — no domain object leakage                     │
├─────────────────────────────────────────────────────────────────────────────┤
│ BOUNDARY 0: Aggregate (within module)                                       │
│   Single transaction, single consistency boundary                           │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 6.2 Boundary Rules

| Boundary | Rule | Enforcement |
|----------|------|-------------|
| **B0 — Aggregate** | One transaction modifies one aggregate | Application layer unit of work |
| **B1 — Module** | Modules communicate only via published interfaces | Compile-time module references; code review |
| **B2 — Monolith shell** | All external traffic enters through presentation/API layer | No infrastructure bypass |
| **B3 — External system** | ACL translates foreign models; domain never sees external schema | Adapter in infrastructure layer |
| **B4 — Partner** | Partners never hold IMS credentials or execute commands | Process design; no API exposure |

### 6.3 Anti-Corruption Layer (ACL) Boundaries

| ACL | Location | Translates | Protects |
|-----|----------|------------|----------|
| **Sales Order ACL** | M-07 Fulfillment infrastructure | CRM order model → `ImportCustomerOrder` command | Fulfillment domain from CRM lifecycle complexity |
| **Finance Export ACL** | M-13 Intelligence infrastructure | Valuation snapshot → GL posting format | Finance chart of accounts from IMS movement model |
| **Finance Match ACL** | M-06 Inbound infrastructure | ERP payment status → match workflow state | Three-way match from ERP payment authority (HS-014) |
| **Channel Feed ACL** | M-13 Intelligence infrastructure | ATP projection → channel-specific availability format | Channel semantics (safety buffer) from raw ATP |
| **Campaign Plan ACL** | M-11 Campaign infrastructure | Marketing plan → `CreatePromotionalAllocation` | Campaign domain from marketing tooling model |
| **Directory Sync ACL** | M-12 Identity infrastructure | HR employee record → `ProvisionUserAccount` | Identity model from HR org structure |

### 6.4 Data Ownership Boundaries

| Data Domain | System of Record | Readers | Writers |
|-------------|------------------|---------|---------|
| Stock quantities (on-hand, reserved, ATP) | IMS M-04 | All modules, CRM (ATP), Channel | **M-04 only** |
| Product master | IMS M-01 | All modules | M-01 only |
| Location network | IMS M-02 | All modules | M-02 only |
| Customer order (fulfillment view) | IMS M-07 | Returns, Intelligence | M-07 only; intake from CRM ACL |
| Customer order (commercial view) | EXT-01 CRM | IMS (subset via ACL) | CRM |
| Purchase order | IMS M-05 | Inbound, Intelligence | M-05 only |
| Goods receipt facts | IMS M-06 | Balance, Finance | M-06 only |
| Supplier invoice / match | IMS M-06 (operational) | Finance | M-06; payment authority EXT-02 |
| GL valuation | EXT-02 Finance | IMS (reconciliation) | Finance |
| User identity | IMS M-12 (operational) | All modules | M-12; source EXT-08 |
| Audit trail | IMS M-13 (projection) | Auditors | Event-driven append only |
| Campaign allocation | IMS M-11 | Fulfillment, Balance | M-11 only |

### 6.5 Trust Boundaries and Security

| Zone | Trust Level | Controls |
|------|-------------|----------|
| Internal module calls | High — same process | Identity context propagation; no anonymous calls |
| External API (CRM, channel) | Medium | Mutual TLS, API keys, scoped permissions, rate limits |
| Finance export/import | Medium | Encrypted transfer, checksum, approval workflow |
| Auditor access | Read-only, time-bound | Dedicated role (NFR-SEC-016); no write endpoints |
| Partner (supplier/carrier) | Untrusted | No direct access; human verification |
| Notification gateway | Trusted service | Authenticated outbound; no inventory mutation |

### 6.6 Integration Failure Boundaries

| Failure Scenario | Boundary Behaviour |
|------------------|-------------------|
| CRM unavailable (Phase 2) | CS manual order entry fallback; no auto-confirm without ATP check |
| Finance export fails | Retry with alert; operational IMS continues; reconciliation deferred |
| Event handler fails | Retry; dead-letter; no partial stock state — outbox ensures consistency |
| Balance reservation fails | Saga compensates order; CRM notified of failure (Phase 2) |
| IdP unavailable | Existing sessions continue; new auth blocked — fail closed |
| Channel feed stale | Feed includes `asOf` timestamp; channel applies safety buffer |

---

## 7. Integration Patterns Reference

| Pattern | Internal / External | Application in IMS |
|---------|--------------------|--------------------|
| **Anti-Corruption Layer** | External | CRM, Finance, Marketing, HR adapters |
| **Published Language** | Both | `ProductSku`, `LocationCode` shared identifiers |
| **Domain Events** | Internal | Cross-module state propagation |
| **CQRS** | Internal | Intelligence read side; ATP query path |
| **Saga / Process Manager** | Internal | Order confirm-reserve, go-live, transfer |
| **Transactional Outbox** | Internal | Reliable event publish with DB commit |
| **Open Host Service** | Internal | Catalog, Governance, Identity query ports |
| **Conformist** | Internal | Consumers accept Catalog/Network reference models |
| **Customer-Supplier** | Internal | Fulfillment ↔ Balance; Accuracy ↔ Balance |
| **Batch Export** | External | Finance valuation, audit evidence |
| **Human-Mediated** | External | Supplier, carrier, MVP CRM |

---

## 8. Integration Governance

| Activity | Owner | Frequency |
|----------|-------|-----------|
| Integration contract review (ports, events) | Solution Architect | Per module release |
| ACL mapping review | Integration architect + domain expert | Per external system onboarding |
| Saga compensation testing | QA + Operations | Per sprint with cross-module stories |
| Event schema versioning | Tech lead | Breaking change requires versioned event types |
| External API consumer onboarding | Security + Product Owner | Per new integration |
| Integration failure runbook | DevOps | Per external system |

---

## 9. Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Solution Architect | | | |
| Integration Architect | | | |
| DDD Solution Architect | | | |
| Security Engineer | | | |
| Product Owner | | | |

---

*End of Integration Architecture Design*

*Document ID: SRS-SA-005 | Version 1.0 | July 6, 2026*
