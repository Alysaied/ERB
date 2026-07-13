# Domain Services
## Inventory Management System

---

## Document Information

| Attribute | Detail |
|-----------|--------|
| **Document ID** | SRS-DM-005 |
| **Document Title** | Domain Services — Inventory Management System |
| **Version** | 1.0 |
| **Status** | Draft |
| **Document Owner** | DDD Architect |
| **Source Documents** | SRS-DM-001 (Domain Entity Model), SRS-DM-003 (Domain Aggregates), SRS-DM-004 (Entity Relationships), SRS-BR-001 (Business Rules), SRS-UC-001 (Use Case Catalog) |
| **Date** | July 5, 2026 |
| **Scope** | Domain-layer business services only — no application services, infrastructure, APIs, or persistence |

### Purpose

This document identifies **Domain Services** for the Inventory Management System. A domain service encapsulates business logic that is essential to the domain but does not naturally belong to a single entity or aggregate root — typically because it **coordinates**, **evaluates**, or **computes** across multiple aggregates, entities, or value objects.

Domain services are **stateless** with respect to business identity: they operate on domain objects passed to them and enforce cross-cutting business rules that no single aggregate can own without creating improper coupling.

### Domain Service vs. Entity Responsibility

| Criterion | Belongs on Entity/Aggregate | Belongs in Domain Service |
|-----------|------------------------------|---------------------------|
| **Scope** | Single consistency boundary | Spans two or more aggregates |
| **State** | Owns lifecycle and identity | Stateless operation on passed objects |
| **Example** | Stock Position maintains its own ATP formula | Network availability sums ATP across many Stock Positions |

### Service Catalog Overview

| Domain Area | Services | IDs |
|-------------|----------|-----|
| Availability & Commitment | Availability Confirmation, Inventory Reservation Coordination, Multi-Location Fulfillment Allocation | DS-001 – DS-003 |
| Network & Replenishment | Network Availability Evaluation, Replenishment Recommendation, Transfer Capacity Evaluation, Network Rebalancing Analysis | DS-004 – DS-007 |
| Inbound & Procurement | Receipt Verification, Put-Away Activation, Three-Way Match Evaluation | DS-008 – DS-010 |
| Fulfillment Execution | Stock Rotation Selection, Shipment Completion Coordination, Partial Fulfillment & Backorder Orchestration | DS-011 – DS-013 |
| Inventory Control | Physical Inventory Freeze Guard, Adjustment Governance Evaluation, Count Variance Adjudication | DS-014 – DS-016 |
| Monitoring & Classification | Stock Status Classification, Low-Stock Alert Evaluation, Promotional Readiness Evaluation | DS-017 – DS-019 |
| Returns & Ownership | Return Eligibility & Disposition Routing, Consignment Ownership Evaluation | DS-020 – DS-021 |
| Financial & Governance | Inventory Valuation Reconciliation, Segregation of Duties Validation, Product Transaction Eligibility | DS-022 – DS-024 |

**Total Domain Services:** 24

---

## Domain 1: Availability & Commitment

---

### DS-001 — Availability Confirmation Service

| Aspect | Detail |
|--------|--------|
| **Business Responsibility** | Evaluate whether requested order quantities can be committed by consulting available-to-promise (ATP) across one or more Stock Positions, Promotional Stock Allocations, and Quarantine Holds. Returns a confirmation result indicating full availability, partial availability, or unavailability with per-line ATP breakdown. |
| **Why It Should Not Belong to an Entity** | Availability confirmation spans Customer Order, Stock Position (potentially multiple locations), Promotional Stock Allocation, and Product catalog validity. Customer Order does not own stock; Stock Position does not know about order context. Neither aggregate should embed the other's rules — confirmation is a cross-aggregate query and decision. |
| **Related Business Rules** | BR-001 (ATP-only customer commitment), BR-013 (quarantine exclusion from sellable stock), BR-029 (promotional ring-fencing), BR-027 (inactive/discontinued product blocking) |
| **Related Use Cases** | UC-013 (Inquire Inventory Availability), UC-021 (Confirm Order Availability), UC-048 (Support Multi-Location Split Fulfillment) |

---

### DS-002 — Inventory Reservation Coordination Service

| Aspect | Detail |
|--------|--------|
| **Business Responsibility** | Orchestrate reservation of stock for confirmed customer order lines by coordinating Customer Order Fulfillment aggregate with one or more Stock Position aggregates. Validates safety stock protection, promotional ring-fence rules, and product eligibility before instructing Stock Positions to increase reserved quantity and decrease ATP. Handles reservation release on cancellation. |
| **Why It Should Not Belong to an Entity** | Reservation requires atomic business intent across order and stock boundaries — Customer Order Fulfillment owns the commercial commitment while Stock Position owns quantity state. Placing reservation logic entirely in either aggregate creates coupling: the order aggregate would mutate foreign stock, or stock would need order context. Coordination is inherently a domain service operation. |
| **Related Business Rules** | BR-002 (reservation at order confirmation), BR-010 (safety stock protection), BR-029 (promotional stock ring-fencing), BR-001 (ATP-only commitment) |
| **Related Use Cases** | UC-022 (Reserve Inventory for Confirmed Orders), UC-023 (Release Inventory Reservations), UC-025 (Handle Partial Fulfillment and Backorders) |

---

### DS-003 — Multi-Location Fulfillment Allocation Service

| Aspect | Detail |
|--------|--------|
| **Business Responsibility** | When a single location cannot satisfy order quantity, determine optimal split allocation across network Stock Positions based on ATP, fulfillment cost proximity, and location operational status. Produces a fulfillment plan assigning order line quantities to one or more ship-from locations. |
| **Why It Should Not Belong to an Entity** | Split fulfillment requires simultaneous evaluation of ATP at multiple locations, transfer feasibility, and order line decomposition — no single Stock Position or Customer Order aggregate has network-wide visibility. Location selection is a policy-driven optimization across the network, not a property of any one entity. |
| **Related Business Rules** | BR-001 (commit only against ATP at each location), BR-002 (reservation per allocated location), BR-012 (source minimum if transfer needed as fallback) |
| **Related Use Cases** | UC-048 (Support Multi-Location Split Fulfillment), UC-021 (Confirm Order Availability), UC-024 (Pick, Pack, and Ship Orders) |

---

## Domain 2: Network & Replenishment

---

### DS-004 — Network Availability Evaluation Service

| Aspect | Detail |
|--------|--------|
| **Business Responsibility** | Before initiating procurement or approving a transfer request, evaluate network-wide stock availability — summing ATP and in-transit quantities across all locations for a product — to determine whether local shortage can be resolved by redistribution rather than new purchase. |
| **Why It Should Not Belong to an Entity** | Network evaluation aggregates data from Stock Positions at many locations, In-Transit Stock records, and Expected Inbound Deliveries. No single location-scoped Stock Position or Purchase Requisition aggregate should own network-wide logic — that would violate aggregate boundaries and create a god entity. |
| **Related Business Rules** | BR-011 (network check before purchase), BR-012 (protect source location minimum when evaluating transfer alternative) |
| **Related Use Cases** | UC-029 (Plan Replenishment and Create Purchase Requisitions), UC-031 (Request Inter-Location Stock Transfer), UC-034 (Analyze and Recommend Network Rebalancing), UC-028 (Review Low-Stock and Out-of-Stock Alerts) |

---

### DS-005 — Replenishment Recommendation Service

| Aspect | Detail |
|--------|--------|
| **Business Responsibility** | Generate replenishment recommendations when Stock Position ATP breaches Stock Policy thresholds. Considers reorder level, safety stock, inbound expected supply, network excess at other locations, product lifecycle status, and ABC classification priority. Recommends purchase requisition, transfer request, or no action. |
| **Why It Should Not Belong to an Entity** | Replenishment decisions synthesize Stock Policy (product-location), Stock Position (current ATP), Expected Inbound Delivery (pipeline), Product (discontinued status, ABC class), and network availability. Stock Policy defines thresholds but should not scan all positions; Stock Position holds quantity but not replenishment authority. The recommendation is a derived cross-domain judgment. |
| **Related Business Rules** | BR-009 (reorder at reorder level), BR-010 (safety stock protection), BR-011 (network check before purchase), BR-027 (no reorder of discontinued products), BR-032 (Class A priority monitoring) |
| **Related Use Cases** | UC-028 (Review Low-Stock and Out-of-Stock Alerts), UC-029 (Plan Replenishment and Create Purchase Requisitions), UC-047 (Receive and Respond to Operational Notifications) |

---

### DS-006 — Transfer Capacity Evaluation Service

| Aspect | Detail |
|--------|--------|
| **Business Responsibility** | Calculate the maximum transferable quantity from a source location for a given product without breaching Stock Policy minimum threshold or safety stock buffer. Used during transfer request creation and approval to enforce source location protection. |
| **Why It Should Not Belong to an Entity** | Transfer capacity requires reading source Stock Position ATP/on-hand, source Stock Policy thresholds, and existing reservations — then computing spare quantity. Stock Transfer aggregate should not own source policy rules; Stock Policy aggregate should not know about transfer requests. The calculation is a stateless evaluation spanning source stock and policy. |
| **Related Business Rules** | BR-012 (protect source location minimum), BR-010 (safety stock protection) |
| **Related Use Cases** | UC-031 (Request Inter-Location Stock Transfer), UC-032 (Approve or Reject Transfer Requests), UC-033 (Execute and Record Inter-Location Transfer) |

---

### DS-007 — Network Rebalancing Analysis Service

| Aspect | Detail |
|--------|--------|
| **Business Responsibility** | Analyze network-wide stock distribution for a product or category to identify imbalance patterns — locations with stockout risk alongside locations with excess — and recommend redistribution transfers. Supports proactive rebalancing before stockouts occur. |
| **Why It Should Not Belong to an Entity** | Rebalancing analysis compares Stock Positions and Stock Policies across the entire location network, identifying pairwise transfer opportunities. This network optimization view belongs to no single location, product, or transfer entity — it is an analytical domain operation over multiple aggregates. |
| **Related Business Rules** | BR-011 (network check before purchase), BR-012 (protect source location minimum), BR-009 (reorder level context for imbalance severity) |
| **Related Use Cases** | UC-034 (Analyze and Recommend Network Rebalancing), UC-031 (Request Inter-Location Stock Transfer), UC-012 (Monitor Inventory Status) |

---

## Domain 3: Inbound & Procurement

---

### DS-008 — Receipt Verification Service

| Aspect | Detail |
|--------|--------|
| **Business Responsibility** | Verify inbound goods against Purchase Order lines, Product catalog (identity, traceability requirements), and Governance Policy (tolerance limits). Validates minimum remaining shelf life (MRSL) for shelf-life products, captures lot/batch requirements, and determines whether receipt discrepancies must be raised before acceptance. |
| **Why It Should Not Belong to an Entity** | Verification compares Goods Receipt data against Purchase Order (separate aggregate), Product (catalog aggregate), and Governance Policy (reference aggregate). Goods Receipt should record outcome but not own PO matching rules, MRSL policy from Product, or tolerance from Governance — those are cross-aggregate validations. |
| **Related Business Rules** | BR-004 (verify before inventory acceptance), BR-006 (document receipt discrepancies), BR-007 (PO required for supplier receipt), BR-016 (minimum remaining shelf life at receipt), BR-017 (lot/batch capture for traceable products) |
| **Related Use Cases** | UC-008 (Receive and Verify Supplier Goods), UC-009 (Document and Resolve Receipt Discrepancies), UC-011 (Receive Return and Non-PO Inbound Stock) |

---

### DS-009 — Put-Away Activation Service

| Aspect | Detail |
|--------|--------|
| **Business Responsibility** | Upon put-away confirmation, coordinate availability activation by validating bonded/customs clearance status (Quarantine Hold), assigning rotation-compliant storage position, and instructing the target Stock Position aggregate to increase on-hand quantity. Ensures stock does not become sellable until all preconditions are satisfied. |
| **Why It Should Not Belong to an Entity** | Put-away completion touches Goods Receipt (put-away entity), Storage Position (location aggregate), Quarantine Hold (stock aggregate), and Stock Position (quantity increase). Goods Receipt owns receipt workflow but should not directly mutate Stock Position; Stock Position should not embed put-away or customs rules. Activation is the cross-aggregate handoff point. |
| **Related Business Rules** | BR-005 (put-away before availability), BR-030 (bonded inventory customs clearance), BR-014 (FEFO rotation placement), BR-015 (FIFO rotation placement) |
| **Related Use Cases** | UC-010 (Perform Stock Put-Away), UC-008 (Receive and Verify Supplier Goods), UC-019 (Manage Quarantine and Hold Stock) |

---

### DS-010 — Three-Way Match Evaluation Service

| Aspect | Detail |
|--------|--------|
| **Business Responsibility** | Compare Purchase Order, Goods Receipt, and Supplier Invoice lines within Governance Policy tolerance limits. Determine match status (matched, quantity exception, price exception, unmatched) and whether payment authorization may proceed. |
| **Why It Should Not Belong to an Entity** | Three-way match is a financial control operation spanning three independent aggregates (Purchase Order, Goods Receipt, Supplier Invoice) plus Governance Policy tolerances. None of the three document aggregates should own the comparison logic — each would create improper dependency on the other two. Match evaluation is a classic domain service. |
| **Related Business Rules** | BR-008 (three-way match before payment), BR-006 (receipt discrepancies affect match outcome) |
| **Related Use Cases** | UC-039 (Reconcile Inventory Valuation with Finance), UC-006 (Place and Manage Purchase Orders), UC-008 (Receive and Verify Supplier Goods) |

---

## Domain 4: Fulfillment Execution

---

### DS-011 — Stock Rotation Selection Service

| Aspect | Detail |
|--------|--------|
| **Business Responsibility** | For pick and put-away operations, select the correct lot/batch or oldest stock based on Product rotation policy (FIFO for standard goods, FEFO for shelf-life products). Returns recommended pick source (storage position and lot) from available Stock Position and Lot/Batch data at a location. |
| **Why It Should Not Belong to an Entity** | Rotation selection compares multiple Lot/Batch records under a Stock Position against Product rotation policy — a decision spanning Product (policy), Lot/Batch (expiration dates), Storage Position (physical location), and Fulfillment Execution (pick context). No single entity owns the selection algorithm without duplicating policy from Product into warehouse entities. |
| **Related Business Rules** | BR-014 (FEFO rotation for shelf-life products), BR-015 (FIFO rotation for standard goods), BR-017 (lot/batch capture on selected stock) |
| **Related Use Cases** | UC-024 (Pick, Pack, and Ship Orders), UC-010 (Perform Stock Put-Away), UC-026 (Handle Outbound Fulfillment Exceptions) |

---

### DS-012 — Shipment Completion Coordination Service

| Aspect | Detail |
|--------|--------|
| **Business Responsibility** | Upon verified pick confirmation, coordinate shipment recording by instructing Stock Position to deduct on-hand quantity, Customer Order Fulfillment to consume Inventory Reservation, and movement history to be recorded. Validates that pick verification preceded dispatch. |
| **Why It Should Not Belong to an Entity** | Shipment completion is the cross-aggregate moment where Fulfillment Execution, Shipment, Stock Position, and Inventory Reservation must align. Shipment entity records dispatch but should not own stock deduction; Stock Position deducts but should not know order fulfillment state. Coordination ensures BR-003 is enforced across boundaries. |
| **Related Business Rules** | BR-003 (verified pick before shipment), BR-002 (reservation consumed on shipment), BR-017 (lot captured on outbound movement) |
| **Related Use Cases** | UC-024 (Pick, Pack, and Ship Orders), UC-027 (View Order Fulfillment Status), UC-026 (Handle Outbound Fulfillment Exceptions) |

---

### DS-013 — Partial Fulfillment and Backorder Orchestration Service

| Aspect | Detail |
|--------|--------|
| **Business Responsibility** | When full order quantity cannot be fulfilled, decompose order lines into fulfillable and backordered quantities, validate customer acknowledgment for backorder remainder, and coordinate partial reservation, partial shipment, and backorder recording within Customer Order Fulfillment aggregate while updating Stock Positions for fulfilled portion only. |
| **Why It Should Not Belong to an Entity** | Partial fulfillment spans availability confirmation (ATP check), reservation (partial quantity), backorder (customer acknowledgment), and shipment (partial dispatch) — each touching different aggregates with distinct lifecycle rules. Backorder acknowledgment (BR-028) is a commercial rule that neither Stock Position nor Shipment alone should own. |
| **Related Business Rules** | BR-028 (backorder customer acknowledgment), BR-001 (ATP-only for fulfillable portion), BR-002 (partial reservation) |
| **Related Use Cases** | UC-025 (Handle Partial Fulfillment and Backorders), UC-021 (Confirm Order Availability), UC-022 (Reserve Inventory for Confirmed Orders) |

---

## Domain 5: Inventory Control

---

### DS-014 — Physical Inventory Freeze Guard Service

| Aspect | Detail |
|--------|--------|
| **Business Responsibility** | Before any stock mutation operation (receipt, shipment, transfer, adjustment), verify that the target Inventory Location is not under an active Physical Inventory Count freeze. Blocks unauthorized mutations and permits only authorized count-related adjustments during freeze period. |
| **Why It Should Not Belong to an Entity** | Freeze state belongs to Physical Inventory Count and Inventory Location aggregates, but enforcement must intercept operations initiated by Goods Receipt, Stock Transfer, Customer Order Fulfillment, and Inventory Adjustment Case — four separate aggregates. No mutating aggregate should own freeze enforcement without coupling to count lifecycle. |
| **Related Business Rules** | BR-024 (physical inventory freeze during wall-to-wall count) |
| **Related Use Cases** | UC-015 (Conduct Full Physical Inventory Count), UC-008 (Receive and Verify Supplier Goods), UC-024 (Pick, Pack, and Ship Orders), UC-033 (Execute and Record Inter-Location Transfer), UC-017 (Process Stock Adjustments) |

---

### DS-015 — Adjustment Governance Evaluation Service

| Aspect | Detail |
|--------|--------|
| **Business Responsibility** | Evaluate whether a proposed Stock Adjustment or Inventory Write-Off satisfies governance requirements: mandatory reason code validity, financial/quantity approval threshold from Governance Policy, and segregation of duties (initiator distinct from required approver). Returns approval requirement and authorization outcome. |
| **Why It Should Not Belong to an Entity** | Governance evaluation consults Inventory Governance (thresholds, reason codes), Inventory Adjustment Case (proposed change), and User Account (initiator/approver identities). Adjustment aggregate should not embed policy thresholds that change independently; Governance Policy should not know about specific adjustment instances. |
| **Related Business Rules** | BR-020 (mandatory adjustment reason codes), BR-021 (independent approval for material adjustments), BR-022 (investigate before adjusting), BR-023 (documented write-off authorization) |
| **Related Use Cases** | UC-017 (Process Stock Adjustments), UC-018 (Authorize and Process Inventory Write-Offs), UC-016 (Investigate and Approve Count Variances) |

---

### DS-016 — Count Variance Adjudication Service

| Aspect | Detail |
|--------|--------|
| **Business Responsibility** | Adjudicate count variances by comparing Cycle Count or Physical Inventory Count results against Stock Position system quantity, enforcing blind count protocol (variance calculated at submission only), validating investigation completion, and confirming approver independence from counter before authorizing adjustment creation. |
| **Why It Should Not Belong to an Entity** | Adjudication connects Cycle Count (count result), Stock Position (system quantity), Count Variance (discrepancy), User Account (counter vs. approver), and Inventory Adjustment Case (correction). Cycle Count should not mutate Stock Position directly; Stock Position should not know count protocol. Adjudication is the governed bridge between count and correction domains. |
| **Related Business Rules** | BR-018 (blind cycle counting), BR-019 (independent count approval), BR-022 (investigate before adjusting) |
| **Related Use Cases** | UC-014 (Perform Cycle Count), UC-015 (Conduct Full Physical Inventory Count), UC-016 (Investigate and Approve Count Variances) |

---

## Domain 6: Monitoring & Classification

---

### DS-017 — Stock Status Classification Service

| Aspect | Detail |
|--------|--------|
| **Business Responsibility** | Classify a Stock Position as in stock, low stock, out of stock, or overstock by comparing current ATP and on-hand quantities against Stock Policy thresholds (reorder level, minimum, maximum). Applies ABC classification weighting for alert priority where configured. |
| **Why It Should Not Belong to an Entity** | Classification derives status from two aggregates — Stock Position (quantities) and Stock Policy (thresholds) — plus Product (ABC class). Stock Position could compute a local indicator but should not own policy thresholds; Stock Policy defines limits but not current quantities. Classification is a derived cross-aggregate evaluation refreshed on quantity or policy changes. |
| **Related Business Rules** | BR-009 (reorder at reorder level), BR-032 (Class A priority monitoring) |
| **Related Use Cases** | UC-012 (Monitor Inventory Status), UC-013 (Inquire Inventory Availability), UC-028 (Review Low-Stock and Out-of-Stock Alerts) |

---

### DS-018 — Low-Stock Alert Evaluation Service

| Aspect | Detail |
|--------|--------|
| **Business Responsibility** | Scan Stock Positions against Stock Policies across the network to detect threshold breaches and generate or update Operational Alerts. Applies Class A priority escalation rules and suppresses duplicate alerts for acknowledged conditions. |
| **Why It Should Not Belong to an Entity** | Alert generation is a network-wide batch evaluation over many Stock Position and Stock Policy pairs — not a responsibility of any single position or policy. Operational Alert is a derived notification entity; the evaluation logic that creates it spans the monitoring domain without belonging to the alert itself. |
| **Related Business Rules** | BR-009 (reorder at reorder level — same business day action), BR-032 (Class A priority monitoring) |
| **Related Use Cases** | UC-028 (Review Low-Stock and Out-of-Stock Alerts), UC-047 (Receive and Respond to Operational Notifications), UC-012 (Monitor Inventory Status) |

---

### DS-019 — Promotional Readiness Evaluation Service

| Aspect | Detail |
|--------|--------|
| **Business Responsibility** | Evaluate whether Promotional Stock Allocation ring-fenced quantity is sufficient for upcoming campaign requirements by comparing allocated ATP against campaign demand forecast and effective campaign period. Identifies readiness gaps and triggers readiness alerts. |
| **Why It Should Not Belong to an Entity** | Readiness evaluation crosses Promotional Stock Allocation (ring-fenced quantity), Stock Position (actual availability), Product (campaign SKU), and campaign period parameters. Marketing readiness is a commercial judgment spanning inventory and campaign entities — neither aggregate owns the full readiness question. |
| **Related Business Rules** | BR-029 (promotional stock ring-fencing), BR-001 (general ATP separate from promotional pool) |
| **Related Use Cases** | UC-040 (Confirm Promotional and Launch Stock Readiness), UC-047 (Receive and Respond to Operational Notifications), UC-022 (Reserve Inventory for Confirmed Orders) |

---

## Domain 7: Returns & Ownership

---

### DS-020 — Return Eligibility and Disposition Routing Service

| Aspect | Detail |
|--------|--------|
| **Business Responsibility** | Validate return eligibility by matching Return Authorization against original Customer Order lines and return policy. Upon inspection, route returned goods to the correct outcome — restock (Stock Position increase), quarantine (Quarantine Hold), or write-off (Inventory Write-Off) — based on condition assessment. |
| **Why It Should Not Belong to an Entity** | Return processing spans Return Authorization, Customer Order, Customer Return, Return Disposition, Stock Position, Quarantine Hold, and Inventory Write-Off. Customer Return records receipt but should not own disposition routing rules; Stock Position should not embed return policy. Routing is a cross-aggregate orchestration of reverse logistics. |
| **Related Business Rules** | BR-025 (return authorization required), BR-026 (inspect returns before restocking), BR-004 (verify before acceptance), BR-013 (quarantine exclusion), BR-023 (write-off authorization) |
| **Related Use Cases** | UC-035 (Authorize and Record Customer Returns), UC-036 (Receive, Inspect, and Disposition Returned Goods), UC-011 (Receive Return and Non-PO Inbound Stock) |

---

### DS-021 — Consignment Ownership Evaluation Service

| Aspect | Detail |
|--------|--------|
| **Business Responsibility** | Determine ownership classification (owned vs. consignment) for stock at receipt and at consumption/sale events based on Supplier consignment agreement. Governs whether Stock Position quantity counts toward owned valuation and when ownership transfer triggers financial recording. |
| **Why It Should Not Belong to an Entity** | Ownership determination consults Supplier (consignment agreement), Goods Receipt (inbound context), Stock Position (current classification), and Shipment (consumption event). Supplier owns commercial terms; Stock Position holds physical quantity — neither should fully own the ownership transfer decision that affects finance (Inventory Valuation Snapshot). |
| **Related Business Rules** | BR-031 (consignment ownership at consumption) |
| **Related Use Cases** | UC-039 (Reconcile Inventory Valuation with Finance), UC-008 (Receive and Verify Supplier Goods), UC-024 (Pick, Pack, and Ship Orders) |

---

## Domain 8: Financial & Governance

---

### DS-022 — Inventory Valuation Reconciliation Service

| Aspect | Detail |
|--------|--------|
| **Business Responsibility** | Produce Inventory Valuation Snapshot by aggregating owned Stock Position quantities (excluding consignment, quarantined, and in-transit per policy), applying unit costs from matched Supplier Invoices, and comparing result against general ledger expectations to identify reconciliation variances. |
| **Why It Should Not Belong to an Entity** | Valuation reconciliation synthesizes Stock Positions (quantities, ownership), Supplier Invoices (costs), Inventory Write-Offs (period reductions), and Quarantine/In-Transit exclusions into a point-in-time financial view. No operational entity should own finance reconciliation — it is a derived cross-domain computation. |
| **Related Business Rules** | BR-008 (three-way match — cost authority), BR-031 (consignment exclusion from owned valuation) |
| **Related Use Cases** | UC-039 (Reconcile Inventory Valuation with Finance), UC-037 (Review Inventory Dashboards and Operational Reports), UC-038 (Review Inventory Performance KPIs) |

---

### DS-023 — Segregation of Duties Validation Service

| Aspect | Detail |
|--------|--------|
| **Business Responsibility** | Validate that a proposed action does not violate segregation-of-duties rules by checking User Account role assignments — e.g., counter cannot approve own count variance, initiator cannot approve own material adjustment, conflicting roles not held simultaneously. |
| **Why It Should Not Belong to an Entity** | SoD validation compares the acting user and proposed approver against User Account role assignments and Governance Policy rules across unrelated transactions (count, adjustment, write-off). Individual transaction entities should not embed user role logic — identity governance is a cross-cutting domain concern. |
| **Related Business Rules** | BR-019 (independent count approval), BR-021 (independent approval for material adjustments), BR-023 (write-off authorization by authorized person) |
| **Related Use Cases** | UC-016 (Investigate and Approve Count Variances), UC-017 (Process Stock Adjustments), UC-018 (Authorize and Process Inventory Write-Offs), UC-045 (Enforce Role-Based and Location-Scoped Access), UC-041 (Conduct Inventory Audit and Control Review) |

---

### DS-024 — Product Transaction Eligibility Service

| Aspect | Detail |
|--------|--------|
| **Business Responsibility** | Validate that a product is eligible for a proposed transaction type — purchase, reservation, fulfillment, or replenishment — based on Product lifecycle status (active, inactive, discontinued) and any authorized exceptions recorded in Governance Policy. |
| **Why It Should Not Belong to an Entity** | Eligibility checks Product catalog status against transaction context from Purchase Order, Customer Order, or Purchase Requisition. Product owns its status but should not know all transaction types that consume it; transaction aggregates should not duplicate lifecycle rules. Centralized eligibility prevents inconsistent enforcement of BR-027 across procurement and fulfillment. |
| **Related Business Rules** | BR-027 (no reorder of discontinued products) |
| **Related Use Cases** | UC-006 (Place and Manage Purchase Orders), UC-022 (Reserve Inventory for Confirmed Orders), UC-029 (Plan Replenishment and Create Purchase Requisitions), UC-001 (Manage Product Master Data) |

---

## Domain Service Interaction Map

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         ORDER FULFILLMENT FLOW                              │
├─────────────────────────────────────────────────────────────────────────────┤
│  DS-024 Product Eligibility                                                 │
│       ↓                                                                     │
│  DS-001 Availability Confirmation ←── DS-003 Multi-Location Allocation      │
│       ↓                                                                     │
│  DS-002 Reservation Coordination                                            │
│       ↓                                                                     │
│  DS-011 Rotation Selection → DS-012 Shipment Coordination                   │
│       ↑                          ↑                                          │
│  DS-014 Freeze Guard ────────────┘                                          │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│                         REPLENISHMENT FLOW                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│  DS-017 Stock Status → DS-018 Low-Stock Alerts → DS-005 Replenishment Rec.  │
│       ↓                                                                     │
│  DS-004 Network Availability ──→ Transfer (DS-006) or Purchase (DS-024)   │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│                         INBOUND FLOW                                        │
├─────────────────────────────────────────────────────────────────────────────┤
│  DS-014 Freeze Guard → DS-008 Receipt Verification → DS-009 Put-Away Activ. │
│       ↓                                                                     │
│  DS-010 Three-Way Match (with Supplier Invoice)                             │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│                    GOVERNANCE (cross-cutting)                               │
├─────────────────────────────────────────────────────────────────────────────┤
│  DS-023 Segregation of Duties — applied by DS-015, DS-016                   │
│  DS-014 Freeze Guard — applied by all mutation services                     │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Domain Service-to-Aggregate Matrix

| Domain Service | Aggregates Coordinated |
|----------------|------------------------|
| DS-001 Availability Confirmation | Customer Order Fulfillment, Stock Position, Promotional Stock Allocation, Product Catalog |
| DS-002 Reservation Coordination | Customer Order Fulfillment, Stock Position, Stock Policy, Promotional Stock Allocation |
| DS-003 Multi-Location Fulfillment Allocation | Customer Order Fulfillment, Stock Position (multiple), Inventory Location |
| DS-004 Network Availability Evaluation | Stock Position (network), In-Transit Stock, Expected Inbound Delivery |
| DS-005 Replenishment Recommendation | Stock Position, Stock Policy, Product Catalog, Expected Inbound Delivery |
| DS-006 Transfer Capacity Evaluation | Stock Position, Stock Policy |
| DS-007 Network Rebalancing Analysis | Stock Position, Stock Policy, Inventory Location (network) |
| DS-008 Receipt Verification | Goods Receipt, Purchase Order, Product Catalog, Inventory Governance |
| DS-009 Put-Away Activation | Goods Receipt, Stock Position, Inventory Location, Quarantine Hold |
| DS-010 Three-Way Match Evaluation | Supplier Invoice, Purchase Order, Goods Receipt, Inventory Governance |
| DS-011 Stock Rotation Selection | Product Catalog, Stock Position, Lot/Batch, Storage Position |
| DS-012 Shipment Completion Coordination | Customer Order Fulfillment, Stock Position |
| DS-013 Partial Fulfillment & Backorder | Customer Order Fulfillment, Stock Position |
| DS-014 Physical Inventory Freeze Guard | Physical Inventory Count, Inventory Location, all mutation aggregates |
| DS-015 Adjustment Governance Evaluation | Inventory Adjustment Case, Inventory Governance, User Account |
| DS-016 Count Variance Adjudication | Cycle Count, Physical Inventory Count, Stock Position, Inventory Adjustment Case, User Account |
| DS-017 Stock Status Classification | Stock Position, Stock Policy, Product Catalog |
| DS-018 Low-Stock Alert Evaluation | Stock Position, Stock Policy, Operational Alert |
| DS-019 Promotional Readiness Evaluation | Promotional Stock Allocation, Stock Position, Product Catalog |
| DS-020 Return Eligibility & Disposition | Customer Return Case, Customer Order Fulfillment, Stock Position, Inventory Adjustment Case |
| DS-021 Consignment Ownership Evaluation | Supplier, Stock Position, Goods Receipt, Customer Order Fulfillment |
| DS-022 Inventory Valuation Reconciliation | Stock Position, Supplier Invoice, Inventory Valuation Snapshot, Inventory Write-Off |
| DS-023 Segregation of Duties Validation | User Account, Inventory Governance |
| DS-024 Product Transaction Eligibility | Product Catalog, Inventory Governance |

---

## Domain Service-to-Use Case Coverage

| Use Case | Domain Services Invoked |
|----------|------------------------|
| UC-008 Receive and Verify Supplier Goods | DS-014, DS-008, DS-024 |
| UC-010 Perform Stock Put-Away | DS-009, DS-011, DS-014 |
| UC-013 Inquire Inventory Availability | DS-001, DS-017 |
| UC-014 Perform Cycle Count | DS-016, DS-014 |
| UC-015 Conduct Full Physical Inventory Count | DS-014, DS-016 |
| UC-016 Investigate and Approve Count Variances | DS-016, DS-015, DS-023 |
| UC-017 Process Stock Adjustments | DS-015, DS-023, DS-014 |
| UC-021 Confirm Order Availability | DS-001, DS-024, DS-003 |
| UC-022 Reserve Inventory for Confirmed Orders | DS-002, DS-001, DS-024 |
| UC-024 Pick, Pack, and Ship Orders | DS-011, DS-012, DS-014 |
| UC-025 Handle Partial Fulfillment and Backorders | DS-013, DS-002, DS-001 |
| UC-028 Review Low-Stock Alerts | DS-018, DS-017, DS-005 |
| UC-029 Plan Replenishment | DS-005, DS-004, DS-024 |
| UC-031 Request Inter-Location Transfer | DS-006, DS-004, DS-014 |
| UC-036 Receive, Inspect, Disposition Returns | DS-020, DS-008, DS-015 |
| UC-039 Reconcile Inventory Valuation | DS-022, DS-010, DS-021 |
| UC-040 Confirm Promotional Readiness | DS-019, DS-001 |
| UC-048 Multi-Location Split Fulfillment | DS-003, DS-002, DS-001 |

---

## Excluded from Domain Services

The following are **not** domain services — they belong to other layers or patterns:

| Capability | Classification | Rationale |
|------------|----------------|-----------|
| Send email/SMS notification | Application / Infrastructure Service | Delivery mechanism, not business logic |
| Generate PDF report | Application Service | Presentation concern |
| Persist Stock Position | Repository (Infrastructure) | Persistence, not domain behavior |
| Authenticate user session | Application / Infrastructure | Technical security, not inventory domain |
| Calculate inventory turnover KPI | Read Model / Analytics | Derived metric for reporting, not transactional domain logic |
| Import CSV product file | Application Service | File parsing and orchestration wrapping domain operations |

---

## Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| DDD Architect | | | |
| Domain Expert | | | |
| Solution Architect | | | |
| Senior Business Analyst | | | |

---

*End of Domain Services*

*Document ID: SRS-DM-005 | Version 1.0 | July 5, 2026*
