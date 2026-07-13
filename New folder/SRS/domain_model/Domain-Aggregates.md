# Domain Aggregates
## Inventory Management System

---

## Document Information

| Attribute | Detail |
|-----------|--------|
| **Document ID** | SRS-DM-003 |
| **Document Title** | Domain Aggregates — Inventory Management System |
| **Version** | 1.0 |
| **Status** | Draft |
| **Document Owner** | DDD Solution Architect |
| **Source Documents** | BRD-IMS-001 (v1.0), SRS-DM-001 (Domain Entity Model, v1.0), SRS-DM-002 (Domain Value Objects, v1.0), SRS-BR-001 (Business Rules, v1.0) |
| **Date** | July 5, 2026 |
| **Scope** | Aggregate design only — no persistence, repositories, or infrastructure |

### Purpose

This document defines **Domain-Driven Design aggregates** for the Inventory Management System. Each aggregate is a consistency boundary: a cluster of entities and value objects mutated together in a single business transaction, accessed only through the aggregate root. External references use identity only — never direct navigation into aggregate internals.

### Aggregate Design Principles Applied

| Principle | Application in IMS |
|-----------|-------------------|
| **One transaction, one aggregate** | Stock deduction and reservation never share a transaction with PO creation |
| **Reference by identity** | Fulfillment references `StockPosition` by product + location; does not hold object references |
| **Small, business-meaningful boundaries** | Stock Position scoped to one product at one location — not entire warehouse |
| **Invariants enforced at root** | All quantity changes pass through aggregate root methods that validate business rules |
| **Eventual consistency across aggregates** | Goods Receipt completion raises domain event consumed by Stock Position aggregate |

### Bounded Context Overview

| Bounded Context | Aggregates |
|-----------------|------------|
| **Catalog & Network** | Product Catalog, Inventory Location, Supplier, Inventory Governance |
| **Inventory Balance** | Stock Position, Stock Policy |
| **Procurement & Inbound** | Purchase Requisition, Purchase Order, Goods Receipt, Supplier Invoice |
| **Order Fulfillment** | Customer Order Fulfillment |
| **Network Transfer** | Stock Transfer |
| **Inventory Accuracy** | Cycle Count, Physical Inventory Count, Inventory Adjustment Case |
| **Returns** | Customer Return Case |
| **Commercial** | Promotional Stock Allocation |
| **Identity & Access** | User Account |

**Total Aggregates:** 18

---

## Bounded Context 1: Catalog & Network

---

### Aggregate 1: Product Catalog

| Aspect | Detail |
|--------|--------|
| **Aggregate Root** | Product |
| **Included Entities** | None *(Product is a single-entity aggregate; classification and identifiers are value objects on the root)* |
| **Included Value Objects** | Product Identifier, Product Category, Product Lifecycle Status, ABC Classification, Rotation Policy, Shelf Life Profile (MRSL policy), Unit of Measure |
| **Invariants (Business Rules)** | SKU must be unique across the catalog. Product name and unit of measure are mandatory. Discontinued products must not be eligible for new replenishment or purchase orders (BR-027). Inactive or discontinued products must be blocked from new reservations unless an authorized exception exists. ABC classification must be A, B, or C when assigned (BR-032 context). Traceable products must declare lot/batch requirement and rotation policy (FIFO or FEFO). Product status transitions must record prior status, new status, and attribution. |
| **Responsibilities** | Maintain the single authoritative product identity (SKU) used across all locations and processes. Govern product lifecycle from introduction through discontinuation. Assign operational classification (ABC) and rotation/traceability attributes that downstream aggregates enforce. Detect and resolve duplicate product identity conflicts. |
| **Business Justification** | Product master data is referenced by every inventory transaction but changes infrequently and independently of stock quantities. A dedicated aggregate prevents catalog edits from coupling to high-frequency stock mutations. Discontinued status must be enforced before any procurement aggregate accepts an order line — the Product root is the gatekeeper of assortment validity. |

---

### Aggregate 2: Inventory Location

| Aspect | Detail |
|--------|--------|
| **Aggregate Root** | Inventory Location |
| **Included Entities** | Storage Position |
| **Included Value Objects** | Physical Address, Location Type, Location Hierarchy Path (parent reference by identity), Effective Period (go-live / closure) |
| **Invariants (Business Rules)** | Location name, type, and operational status are mandatory. A location cannot be its own parent or ancestor in the hierarchy. Deactivated or closing locations must not accept new receipts, reservations, or fulfillments except authorized disposition activity. Location activation for transactions requires approved opening balances when go-live policy applies. Physical inventory freeze (BR-024) must block all receiving, shipping, transfers, and adjustments at the location while a Physical Inventory Count aggregate reports active freeze for this location. Closure is blocked while on-hand stock remains unless a disposition plan is documented or waived. |
| **Responsibilities** | Define the network of places where stock is held and operated. Manage storage position structure within a location. Control location operational status (active, planned, closing). Enforce freeze compliance during wall-to-wall counts. Support location go-live and closure lifecycle. |
| **Business Justification** | Location configuration and storage layout change independently of stock balances. Storage Positions belong to exactly one location and are meaningless outside it — they share the location's lifecycle. Freeze enforcement requires the location aggregate to expose a single authoritative "frozen" state that all other aggregates consult before permitting mutations at that site. |

---

### Aggregate 3: Supplier

| Aspect | Detail |
|--------|--------|
| **Aggregate Root** | Supplier |
| **Included Entities** | None |
| **Included Value Objects** | Contact Details, Payment Terms, Lead Time Duration (default) |
| **Invariants (Business Rules)** | Supplier code must be unique. Supplier must be active to appear on new purchase orders. Consignment agreement indicator governs ownership classification applied at receipt — consignment stock is not owned until consumption (BR-031). Payment terms must be defined before purchase orders are issued to the supplier. |
| **Responsibilities** | Maintain supplier commercial identity and default procurement terms. Indicate consignment relationship where ownership rules differ from standard purchase. Support supplier delivery performance tracking references. |
| **Business Justification** | Supplier is master data referenced by Purchase Order and Goods Receipt aggregates by identity. Commercial terms belong with the supplier definition and must remain consistent across all open POs — isolating suppliers prevents PO line edits from corrupting supplier master data. |

---

### Aggregate 4: Inventory Governance

| Aspect | Detail |
|--------|--------|
| **Aggregate Root** | Governance Policy |
| **Included Entities** | Reason Code |
| **Included Value Objects** | Approval Threshold, Quantity Tolerance, Effective Period |
| **Invariants (Business Rules)** | Reason codes must be unique; retired codes must not be selectable for new transactions (BR-020 context). Every adjustment, write-off, and receipt discrepancy requires an active reason code at submission time. Only one governance policy version may be effective for a given parameter at any point in time. Adjustments above defined financial or quantity thresholds require independent approval (BR-021). Receipt quantity tolerance limits govern auto-acceptance vs. discrepancy creation (BR-006, BR-008). Segregation-of-duties rules: counter must not approve adjustments from their own count (BR-019). |
| **Responsibilities** | Maintain the standardized reason code taxonomy for all inventory exceptions and corrections. Define approval thresholds, tolerance limits, and exception policies that other aggregates consult during validation. Govern policy versioning with non-overlapping effective periods. |
| **Business Justification** | Reason codes and governance thresholds are organization-wide reference data that many aggregates consult but none should own. Centralizing them in one aggregate ensures a single policy source — when a threshold changes, all aggregates evaluate against the same effective policy without embedding rules in each aggregate. |

---

## Bounded Context 2: Inventory Balance

---

### Aggregate 5: Stock Position

| Aspect | Detail |
|--------|--------|
| **Aggregate Root** | Stock Position |
| **Included Entities** | Lot/Batch *(when product is traceable)*, Quarantine Hold |
| **Included Value Objects** | Stock Availability Breakdown, Stock Status Indicator, Ownership Classification, Quantity, Lot Identity, Hold Reason Classification, Reason Code Attribution, Audit Quantity Snapshot, User Action Attribution |
| **Invariants (Business Rules)** | On-hand quantity must never be negative. Available-to-promise (ATP) = on-hand minus reserved minus quarantined/hold quantities — ATP must never exceed on-hand (BR-001, BR-013). Quarantined and bonded stock must be excluded from ATP (BR-013, BR-030). Consignment stock must not be treated as owned for fulfillment until ownership transfer event (BR-031). Safety stock buffer must not be consumed below policy minimum without authorized exception (BR-010). Lot/batch identity must be captured for all movements on traceable products (BR-017). Stock status indicator must be recalculated when quantities cross policy thresholds. All quantity mutations must produce an Inventory Movement Record as a domain event — movement history is immutable. Location must not be frozen (consult Inventory Location aggregate) when accepting quantity changes except authorized count adjustments. |
| **Responsibilities** | Maintain authoritative on-hand, reserved, and ATP quantities for one product at one location. Manage lot/batch-level quantities for traceable products. Apply and release quarantine holds. Enforce ownership classification effects on availability and valuation treatment. Accept inbound quantity increases (from receipt, transfer-in, return restock) and outbound decreases (from shipment, transfer-out, adjustment, write-off) only through root operations. Emit domain events on every balance change for audit and reporting consumers. |
| **Business Justification** | Stock Position is the system's most contended consistency boundary — reservations, picks, receipts, and adjustments all compete for the same quantities. Scoping the aggregate to one product at one location minimizes lock contention while guaranteeing ATP is always mathematically consistent within the boundary. Lot/Batch and Quarantine Hold entities belong inside because hold application immediately reduces ATP — partial updates across separate aggregates would allow overselling. |

---

### Aggregate 6: Stock Policy

| Aspect | Detail |
|--------|--------|
| **Aggregate Root** | Stock Policy |
| **Included Entities** | None |
| **Included Value Objects** | Stock Threshold Set, Lead Time Duration, Effective Period |
| **Invariants (Business Rules)** | Reorder level, minimum threshold, and safety stock must be zero or positive. Minimum threshold must not exceed reorder level unless an explicitly authorized inverted configuration exists. Threshold changes must include an effective date and retain prior values as immutable history. Replenishment action must trigger when ATP reaches reorder level (BR-009). Safety stock must not be bypassed without documented approval and replenishment plan (BR-010). Source location minimum must be enforced when this policy governs a transfer source (BR-012). |
| **Responsibilities** | Define replenishment thresholds for a specific product at a specific location. Maintain threshold change history with effective dating. Provide the policy reference that Stock Position uses to compute stock status indicators and that replenishment processes use to trigger alerts. |
| **Business Justification** | Stock policy changes are infrequent, approval-governed events distinct from high-frequency quantity mutations. Separating policy from Stock Position allows threshold recalibration without locking stock during active fulfillment. The product + location identity key aligns with how planners think about replenishment — one policy per SKU per site. |

---

## Bounded Context 3: Procurement & Inbound

---

### Aggregate 7: Purchase Requisition

| Aspect | Detail |
|--------|--------|
| **Aggregate Root** | Purchase Requisition |
| **Included Entities** | None *(requisition lines are value objects)* |
| **Included Value Objects** | Requisition Line Detail (collection), User Action Attribution |
| **Invariants (Business Rules)** | Requisition lines must reference active products — discontinued products are prohibited (BR-027). Requested quantities must be greater than zero. Network availability must be evaluated before requisition approval — excess at other locations should trigger transfer consideration before procurement (BR-011). Safety stock must not be implicitly bypassed by requisition quantity decisions (BR-010). Requisition must reach approved status before conversion to a Purchase Order. |
| **Responsibilities** | Capture internal replenishment need with product, quantity, and target location. Route through approval workflow. Convert to Purchase Order upon approval. Link to triggering low-stock alert reference when applicable. |
| **Business Justification** | Requisition is an internal intent document with its own approval lifecycle, distinct from the commercial PO commitment. Keeping it as a separate aggregate allows rejection or amendment without affecting supplier-facing PO records. Conversion to PO is a cross-aggregate operation creating a new Purchase Order aggregate from approved requisition identity. |

---

### Aggregate 8: Purchase Order

| Aspect | Detail |
|--------|--------|
| **Aggregate Root** | Purchase Order |
| **Included Entities** | Expected Inbound Delivery |
| **Included Value Objects** | Purchase Order Line (collection), Payment Terms, Lead Time Duration, Monetary Amount |
| **Invariants (Business Rules)** | PO must include supplier reference, receiving location, product lines, and expected delivery date. PO lines must reference active products and active receiving locations — discontinued products prohibited (BR-027). Ordered quantity must be greater than zero. A valid PO is required before supplier goods receipt except explicitly approved ad-hoc exceptions (BR-007). Received quantity per line must not exceed ordered quantity plus defined tolerance without discrepancy workflow. PO status transitions: open → partial → closed/cancelled; cancelled POs must not accept receipts. Expected inbound delivery dates must be valid and associated with an open PO line. |
| **Responsibilities** | Record authorized commercial commitment to a supplier. Track ordered vs. received quantities per line. Manage expected inbound delivery schedules. Support PO amendment and cancellation with receipt implications. Provide the reference document for goods receipt verification and three-way match. |
| **Business Justification** | Purchase Order is the commercial control document governing inbound supply. Expected Inbound Delivery entities belong inside because delivery schedule changes are part of the same procurement commitment — splitting them risks inconsistent inbound visibility. PO enforces BR-007 as the gate for the Goods Receipt aggregate. |

---

### Aggregate 9: Goods Receipt

| Aspect | Detail |
|--------|--------|
| **Aggregate Root** | Goods Receipt |
| **Included Entities** | Receipt Discrepancy, Put-Away |
| **Included Value Objects** | Receipt Line Detail (collection), Condition Grade, Discrepancy Classification, Quantity Variance, Shelf Life Profile, Lot Identity, User Action Attribution |
| **Invariants (Business Rules)** | Inbound goods must be verified before acceptance — quantity, product identity, and condition confirmed (BR-004). Valid PO reference required except approved ad-hoc exception (BR-007). Receipt discrepancies must be documented before acceptance of affected quantities (BR-006). Minimum remaining shelf life (MRSL) must be met for shelf-life products — non-compliant deliveries rejected or dispositioned (BR-016). Lot/batch identity must be captured for traceable products at receipt (BR-017). Bonded inventory must remain on hold until customs clearance — not released to sellable via put-away (BR-030). Received stock is not available for sale until put-away is confirmed (BR-005). Put-away must assign storage position and apply rotation placement (BR-014, BR-015). Received quantity must not be accepted into stock position until put-away completion triggers cross-aggregate notification. |
| **Responsibilities** | Orchestrate the inbound verification workflow from dock arrival through put-away confirmation. Document and resolve receipt discrepancies with evidence. Capture lot/batch and shelf-life data at receipt. Manage put-away as the final step before stock becomes available. Emit domain event on put-away completion for Stock Position aggregate to increase on-hand quantity. |
| **Business Justification** | Receipt, discrepancy resolution, and put-away are one operational unit of work at the receiving dock — a receiver verifies, documents exceptions, and stows goods in a continuous flow. Combining them ensures stock is never marked available (BR-005) without verified receipt and confirmed put-away within the same consistency boundary. Put-Away as an entity inside (not separate aggregate) prevents orphan "received but not stowed" states. |

---

### Aggregate 10: Supplier Invoice

| Aspect | Detail |
|--------|--------|
| **Aggregate Root** | Supplier Invoice |
| **Included Entities** | None *(invoice lines are value objects)* |
| **Included Value Objects** | Invoice Line Detail (collection), Three-Way Match Result, Quantity Tolerance, Monetary Amount |
| **Invariants (Business Rules)** | Three-way match must be confirmed among PO, goods receipt, and invoice within defined tolerance before payment authorization (BR-008). Payment for unordered, unreceived, or mispriced goods is prohibited. Invoice lines must reference products and quantities that exist on the linked PO and receipt. Match exceptions must be documented and resolved or waived by authorized approver before payment status transitions to authorized. |
| **Responsibilities** | Record supplier billing document. Execute three-way match evaluation against Purchase Order and Goods Receipt aggregates (referenced by identity). Track match status and payment authorization gate. Document match exceptions for finance resolution. |
| **Business Justification** | Invoice matching is a financial control boundary that compares three independent documents. The Supplier Invoice aggregate owns the match outcome — it consults PO and GR by identity but does not mutate them. This isolates financial approval workflow from operational receipt processing while enforcing BR-008 as a single coherent decision. |

---

## Bounded Context 4: Order Fulfillment

---

### Aggregate 11: Customer Order Fulfillment

| Aspect | Detail |
|--------|--------|
| **Aggregate Root** | Customer Order |
| **Included Entities** | Inventory Reservation, Fulfillment Execution, Backorder, Shipment |
| **Included Value Objects** | Order Line Quantity (collection), Fulfillment Quantity Breakdown, Customer Acknowledgment, Pick Line Detail, Shipment Line Detail, Channel Designation, User Action Attribution |
| **Invariants (Business Rules)** | Availability confirmation must use ATP only — not total on-hand (BR-001). Stock must be reserved at order confirmation; reserved quantity removed from ATP until fulfilled or released (BR-002). Reservation must reference active products at authorized locations. Safety stock and promotional ring-fence rules must be respected when reserving (BR-010, BR-029). Verified pick must complete before shipment recording — no ship without pick confirmation (BR-003). FEFO/FIFO rotation must be applied during pick line assignment (BR-014, BR-015). Lot/batch must be captured on pick for traceable products (BR-017). Backorder requires explicit customer acknowledgment before recording (BR-028). Partial fulfillment must decompose order line into fulfilled and backordered quantities consistently. Shipment deducts stock only after verified pick — emits domain event to Stock Position aggregate. Reservation release on cancellation must restore ATP via cross-aggregate command. |
| **Responsibilities** | Manage the complete customer order lifecycle from availability confirmation through reservation, pick/pack/ship, and partial/backorder handling. Coordinate ATP commitment and release with Stock Position aggregate. Enforce pick verification before shipment. Capture customer acknowledgment for backorders. Emit shipment events that trigger stock deduction. Provide order fulfillment status visibility. |
| **Business Justification** | Order confirmation, reservation, picking, and shipping are one coherent business transaction chain with tightly coupled state — a reservation without pick tracking or a shipment without reservation release creates overselling or phantom stock. Keeping these entities in one aggregate guarantees order line quantities reconcile: requested = reserved = picked + backordered + cancelled at every stage. Cross-aggregate calls to Stock Position handle ATP mechanics while the order aggregate owns fulfillment intent. |

---

## Bounded Context 5: Network Transfer

---

### Aggregate 12: Stock Transfer

| Aspect | Detail |
|--------|--------|
| **Aggregate Root** | Stock Transfer *(Transfer Request is the initial state; approved request promotes to transfer execution within same aggregate)* |
| **Included Entities** | In-Transit Stock |
| **Included Value Objects** | Transfer Line Detail (collection), Quantity, Lot Identity, User Action Attribution, Approval Threshold (evaluated) |
| **Invariants (Business Rules)** | Transfer must not deplete source below its minimum threshold — quantity limited to spare stock above source policy minimum (BR-012). Network availability must have been evaluated before transfer was initiated as alternative to purchase (BR-011). Safety stock at source must not be breached without authorized exception (BR-010). Transfer requires approval before dispatch when policy mandates. Lot/batch must be captured on transfer lines for traceable products (BR-017). Dispatch deducts source Stock Position; receipt at destination increases destination Stock Position — in-transit quantity tracked between. In-transit stock excluded from both source and destination ATP until receipt confirmed. Source and destination locations must not be frozen during dispatch/receipt. |
| **Responsibilities** | Manage inter-location transfer lifecycle: request, approval, dispatch, in-transit tracking, and receipt confirmation. Enforce source location minimum protection. Track in-transit inventory state. Coordinate stock deductions and additions across two Stock Position aggregates via domain events. |
| **Business Justification** | A transfer is a single business operation spanning two locations with three states (requested → in-transit → received). In-Transit Stock belongs inside because it is meaningless without the transfer that created it — splitting would orphan pipeline inventory. Source minimum enforcement (BR-012) requires evaluating source Stock Policy within the transfer decision, making the transfer aggregate the natural enforcement point before dispatch events fire. |

---

## Bounded Context 6: Inventory Accuracy

---

### Aggregate 13: Cycle Count

| Aspect | Detail |
|--------|--------|
| **Aggregate Root** | Cycle Count |
| **Included Entities** | None *(count result and variance reference are value objects; variance investigation spawns separate aggregate)* |
| **Included Value Objects** | Quantity (physical count result), Quantity Variance, User Action Attribution |
| **Invariants (Business Rules)** | Count must be performed blind — counter must not see system expected quantity before recording result (BR-018). Class A products must receive highest count frequency (BR-032). Physical count quantity must be non-negative. Count assignment must reference valid product and location. Count completion with variance must spawn an Inventory Adjustment Case aggregate — Cycle Count does not directly mutate Stock Position. Counter identity recorded and must differ from eventual approver (BR-019). |
| **Responsibilities** | Schedule and assign cycle count work. Enforce blind counting protocol. Record physical count result. Calculate variance against system quantity (evaluated at submission, not shown to counter). Initiate variance investigation workflow when variance exists. |
| **Business Justification** | Cycle count is a bounded operational task — assign, count, record. It deliberately does not adjust stock directly because BR-022 requires investigation before adjustment and BR-019 requires independent approval. Separating count from adjustment into different aggregates enforces segregation of duties by design. |

---

### Aggregate 14: Physical Inventory Count

| Aspect | Detail |
|--------|--------|
| **Aggregate Root** | Physical Inventory Count |
| **Included Entities** | None *(count teams and location scope managed on root)* |
| **Included Value Objects** | Effective Period (freeze window), Quantity Variance (per line, collected), User Action Attribution |
| **Invariants (Business Rules)** | Physical inventory freeze must apply during wall-to-wall count — no receiving, shipping, transfers, or adjustments at the location until count completed and verified (BR-024). Freeze state must be communicated to Inventory Location aggregate. Count must cover full location scope. Count certification requires all variances identified and routed to Inventory Adjustment Case aggregates. Location must return to active operational status only after count event is certified complete and freeze released. |
| **Responsibilities** | Orchestrate full wall-to-wall count at a location. Impose and release location freeze. Collect all line-level count results and variances. Certify count completion. Coordinate with Inventory Location aggregate for freeze enforcement. |
| **Business Justification** | Physical count is a location-wide event affecting every concurrent operation — BR-024 freeze is the defining invariant. This aggregate owns the count event and freeze lifecycle because only the count process knows when the location snapshot is stable. Individual variances still flow to adjustment cases rather than mutating stock during the count. |

---

### Aggregate 15: Inventory Adjustment Case

| Aspect | Detail |
|--------|--------|
| **Aggregate Root** | Count Variance *(when originating from count)* or Stock Adjustment *(when direct adjustment)* — unified as **Adjustment Case** with polymorphic origin |
| **Included Entities** | Stock Adjustment, Inventory Write-Off |
| **Included Value Objects** | Quantity Variance, Reason Code Attribution, Condition Grade, Disposition Decision, Approval Threshold, Audit Quantity Snapshot, User Action Attribution, Valuation Line Amount |
| **Invariants (Business Rules)** | Variances must be investigated before adjustment is applied — root cause analysis or documented effort required (BR-022). Counter must not approve adjustments from their own count (BR-019). Every adjustment requires a mandatory reason code (BR-020). Adjustments above threshold require independent approval by someone who did not initiate the underlying transaction (BR-021). Write-off requires documented evidence and authorized approval (BR-023). Adjustment and write-off must emit domain events to Stock Position aggregate for quantity mutation. Write-off is terminal — quantity permanently removed. Adjustment quantity must not drive stock negative. |
| **Responsibilities** | Investigate count variances and document findings. Process stock adjustments with reason code and approval chain. Process inventory write-offs with evidence and authorization. Enforce segregation of duties between initiator and approver. Trigger Stock Position mutations only upon approved, finalized adjustment or write-off. |
| **Business Justification** | Investigation, approval, and execution of inventory corrections form a governance workflow that must not be bypassed. Combining Count Variance, Stock Adjustment, and Write-Off in one case aggregate ensures BR-022 (investigate before adjusting) and BR-019/BR-021 (independent approval) are enforced as a single state machine: variance → investigation → approval → stock mutation. Stock Position remains the quantity owner — this aggregate owns the decision to change it. |

---

## Bounded Context 7: Returns

---

### Aggregate 16: Customer Return Case

| Aspect | Detail |
|--------|--------|
| **Aggregate Root** | Return Authorization |
| **Included Entities** | Customer Return, Return Disposition |
| **Included Value Objects** | Condition Grade, Disposition Decision, Receipt Line Detail, Reason Code Attribution, User Action Attribution |
| **Invariants (Business Rules)** | Return authorization required before warehouse acceptance — no receipt without valid RMA linked to original order (BR-025). Returned goods must be verified on receipt — quantity and product matched to authorization (BR-004). Returned goods must be inspected before restocking — condition assessment mandatory (BR-026). Restock to sellable inventory permitted only when condition grade confirms resale quality. Damaged or defective returns must be dispositioned to quarantine or write-off — never directly to ATP. Disposition emits domain event to Stock Position (restock increase) or Inventory Adjustment Case (write-off). Original order referenced by identity for policy validation. |
| **Responsibilities** | Issue return authorization linked to original customer order. Receive and verify returned goods against authorization. Inspect condition and decide disposition (restock, quarantine, write-off). Coordinate stock position increase or write-off initiation based on disposition. Track return processing status end-to-end. |
| **Business Justification** | Return authorization, physical receipt, inspection, and disposition are one reverse-logistics workflow with strict sequencing (BR-025 → BR-004 → BR-026). Combining them prevents unauthorized returns entering stock and prevents uninspected goods reaching sellable inventory. The RMA is the natural root because it gates all subsequent steps — without authorization, receipt and disposition cannot proceed. |

---

## Bounded Context 8: Commercial

---

### Aggregate 17: Promotional Stock Allocation

| Aspect | Detail |
|--------|--------|
| **Aggregate Root** | Promotional Stock Allocation |
| **Included Entities** | None |
| **Included Value Objects** | Campaign Period, Channel Designation, Quantity, Stock Availability Breakdown (ring-fenced portion) |
| **Invariants (Business Rules)** | Promotional stock must be ring-fenced during campaign — allocated quantity must not be consumed by non-promotional orders without commercial leadership approval (BR-029). Allocation quantity must not exceed available stock at allocation time. Ring-fenced quantity reduces general ATP on Stock Position while allocation is active. Allocation must define effective campaign period — inactive outside period. Readiness status must be confirmable before campaign commitment. Release of un consumed allocation after campaign end restores quantity to general ATP. |
| **Responsibilities** | Ring-fence defined quantity for a promotional campaign or launch. Protect allocated stock from non-promotional reservation. Support readiness review before campaign start. Release un consumed allocation on campaign end. Coordinate with Stock Position aggregate to segregate ATP. |
| **Business Justification** | Promotional ring-fencing is a commercial policy overlay on stock availability with its own lifecycle (campaign start/end) independent of order fulfillment mechanics. A dedicated aggregate allows marketing and commercial teams to manage allocations without coupling to individual Customer Order Fulfillment aggregates. BR-029 enforcement requires a single authority on what quantity is promotional vs. general — this aggregate is that authority. |

---

## Bounded Context 9: Identity & Access

---

### Aggregate 18: User Account

| Aspect | Detail |
|--------|--------|
| **Aggregate Root** | User Account |
| **Included Entities** | Role Assignment |
| **Included Value Objects** | User Action Attribution (template), Effective Period (assignment dates) |
| **Invariants (Business Rules)** | User identifier must be unique. Account must have at least one role assignment to perform system actions. Segregation-of-duties conflicts must be blocked — e.g., user cannot hold both cycle count operator and count approval roles simultaneously (BR-019, BR-021). Location scope on role assignment must reference valid active locations. Deactivated accounts must not authenticate or perform actions. Role changes must be effective-dated; prior assignments retained as history. |
| **Responsibilities** | Provision and manage user identity for inventory operations. Assign roles with location scope and permission boundaries. Enforce segregation-of-duties constraints at assignment time. Support account lifecycle (active, suspended, deactivated). Provide user identity context consumed by all aggregates for attribution. |
| **Business Justification** | User identity and role assignments change independently of inventory transactions but govern who may initiate and approve them. Centralizing access control in one aggregate ensures SoD rules (BR-019, BR-021) are evaluated consistently at role assignment — not re-implemented in each operational aggregate. Role Assignments belong inside because they have no meaning without the user account they belong to. |

---

## Cross-Aggregate Interaction Model

Aggregates coordinate through **domain events** and **identity references** — never through shared mutable state.

```
┌─────────────────────┐     PutAwayCompleted      ┌─────────────────────┐
│   Goods Receipt     │ ─────────────────────────►│   Stock Position    │
│   (Aggregate 9)     │     (product, location,   │   (Aggregate 5)     │
└─────────────────────┘      qty, lot)            └─────────────────────┘
                                                           ▲
┌─────────────────────┐     ReservationCommitted          │
│ Customer Order      │ ──────────────────────────────────┤
│ Fulfillment (11)    │     ShipmentDispatched (deduct)   │
└─────────────────────┘ ──────────────────────────────────┘

┌─────────────────────┐     TransferDispatched            │
│   Stock Transfer    │ ──────────────────────────────────┤
│   (Aggregate 12)    │     TransferReceived              │
└─────────────────────┘ ──────────────────────────────────┘

┌─────────────────────┐     AdjustmentApproved            │
│ Inventory Adjustment│ ──────────────────────────────────┘
│ Case (15)           │
└─────────────────────┘

┌─────────────────────┐     RestockApproved               │
│ Customer Return     │ ──────────────────────────────────► Stock Position
│ Case (16)           │
└─────────────────────┘
```

### Interaction Rules

| Rule | Description |
|------|-------------|
| **No cross-aggregate transaction** | Goods Receipt put-away and Stock Position update are eventual consistency via domain event |
| **Reference by identity** | Customer Order Fulfillment holds `productSku + locationCode`, not Stock Position object reference |
| **Consult, don't couple** | Stock Transfer consults Stock Policy and Stock Position by identity for source minimum check before dispatch |
| **Governance consultation** | All adjustment aggregates consult Inventory Governance for reason code validity and approval thresholds |
| **Catalog validation** | Procurement and fulfillment aggregates consult Product Catalog by SKU for lifecycle status before accepting lines |

---

## Aggregate Summary

| # | Aggregate | Root | Bounded Context | Primary Business Processes |
|---|-----------|------|-----------------|------------------------------|
| 1 | Product Catalog | Product | Catalog & Network | BP-01, BP-04 |
| 2 | Inventory Location | Inventory Location | Catalog & Network | BP-02, BP-12 |
| 3 | Supplier | Supplier | Catalog & Network | BP-05, BP-07 |
| 4 | Inventory Governance | Governance Policy | Catalog & Network | BP-01, BP-13, BP-14 |
| 5 | Stock Position | Stock Position | Inventory Balance | BP-10, BP-16, BP-17 |
| 6 | Stock Policy | Stock Policy | Inventory Balance | BP-03, BP-21 |
| 7 | Purchase Requisition | Purchase Requisition | Procurement & Inbound | BP-22 |
| 8 | Purchase Order | Purchase Order | Procurement & Inbound | BP-05, BP-06, BP-23 |
| 9 | Goods Receipt | Goods Receipt | Procurement & Inbound | BP-07, BP-08, BP-09 |
| 10 | Supplier Invoice | Supplier Invoice | Procurement & Inbound | BP-30 |
| 11 | Customer Order Fulfillment | Customer Order | Order Fulfillment | BP-16, BP-17, BP-18, BP-19 |
| 12 | Stock Transfer | Stock Transfer | Network Transfer | BP-24, BP-25 |
| 13 | Cycle Count | Cycle Count | Inventory Accuracy | BP-11 |
| 14 | Physical Inventory Count | Physical Inventory Count | Inventory Accuracy | BP-12 |
| 15 | Inventory Adjustment Case | Count Variance / Stock Adjustment | Inventory Accuracy | BP-13, BP-14, BP-15 |
| 16 | Customer Return Case | Return Authorization | Returns | BP-27, BP-28 |
| 17 | Promotional Stock Allocation | Promotional Stock Allocation | Commercial | BP-31 |
| 18 | User Account | User Account | Identity & Access | Cross-cutting |

---

## Excluded from Aggregate Design

The following domain concepts are intentionally **not** modeled as aggregates:

| Concept | Treatment | Rationale |
|---------|-----------|-----------|
| **Inventory Movement Record** | Domain event / append-only log | Immutable history produced by aggregates; not a consistency boundary |
| **Audit Trail Record** | Domain event / compliance log | Cross-cutting observation of aggregate mutations |
| **Operational Alert** | Read model / notification projection | Derived from threshold breaches; no transactional invariant |
| **Inventory Valuation Snapshot** | Reporting read model | Point-in-time projection for finance; rebuilt from Stock Position events |

---

## Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| DDD Solution Architect | | | |
| Domain Expert | | | |
| Senior Business Analyst | | | |
| Product Owner | | | |

---

*End of Domain Aggregates*

*Document ID: SRS-DM-003 | Version 1.0 | July 5, 2026*
