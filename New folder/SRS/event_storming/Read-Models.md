# Read Models
## Inventory Management System — Event Storming

---

## Document Information

| Attribute | Detail |
|-----------|--------|
| **Document ID** | SRS-ES-005 |
| **Document Title** | Read Models — Event Storming Catalog |
| **Version** | 1.0 |
| **Status** | Draft |
| **Document Owner** | Domain Expert |
| **Source Documents** | SRS-ES-001 (Domain Events), SRS-DM-003 (Domain Aggregates), SRS-DM-006 (Domain Events), SRS-UC-001 (Use Case Catalog), SRS-DM-004 (Bounded Contexts — Inventory Intelligence) |
| **Date** | July 6, 2026 |
| **Scope** | Business information projections only — no database schemas, SQL, or UI wireframes |

### Purpose

This document identifies **Read Models** required by the Inventory Management System. A read model is a purpose-built projection that answers a specific business question by consuming domain events. Read models support inquiry, monitoring, decision-making, and compliance — they never mutate transactional aggregate state.

Read models belong to the **Inventory Intelligence** bounded context. They are eventually consistent with operational writes and may be rebuilt from the event stream.

### Read Model Catalog Summary

| Domain Area | Read Model IDs | Count |
|-------------|----------------|-------|
| Inventory Visibility & Availability | RM-001 – RM-004 | 4 |
| Alerts & Notifications | RM-005 – RM-006 | 2 |
| Procurement & Inbound Supply | RM-007 – RM-012 | 6 |
| Order Fulfillment | RM-013 – RM-016 | 4 |
| Network Transfer & Balance | RM-017 – RM-019 | 3 |
| Inventory Accuracy & Control | RM-020 – RM-025 | 6 |
| Commercial & Promotional | RM-026 – RM-027 | 2 |
| Financial & Valuation | RM-028 – RM-031 | 4 |
| Governance & Compliance | RM-032 – RM-034 | 3 |
| Master Data & Reference | RM-035 – RM-039 | 5 |
| **Total** | | **39** |

---

## Domain 1: Inventory Visibility & Availability

---

### RM-001 — Network Stock Status Board

| Field | Detail |
|-------|--------|
| **Name** | Network Stock Status Board |
| **Purpose** | Answer *"What do we have, where is it, and what is its health?"* across the location network for daily operational monitoring. |
| **Information Displayed** | On-hand, reserved, quarantined, and ATP quantities by product and location; stock status indicator (in stock, low stock, out of stock, overstock); ABC classification; last movement date; ownership classification (owned vs. consignment) |
| **Primary Users** | Inventory Controller, Operations Director, Warehouse Manager, Purchasing Manager |
| **Source Events** | StockReceived, StockShipped, StockReserved, StockReservationReleased, StockAdjusted, StockWrittenOff, QuarantineHoldApplied, QuarantineHoldReleased, PromotionalStockAllocated, PromotionalAllocationReleased, ConsignmentOwnershipTransferred, StockPolicyThresholdChanged, ProductABCClassificationAssigned, LowStockThresholdBreached, OutOfStockDetected, OverstockDetected |
| **Use Cases** | UC-012, UC-037 |

---

### RM-002 — Availability Inquiry View

| Field | Detail |
|-------|--------|
| **Name** | Availability Inquiry View |
| **Purpose** | Answer *"Can we promise this quantity to a customer at this location or across the network?"* before commercial commitment. |
| **Information Displayed** | ATP by product and location; network-wide ATP rollup; reserved and quarantined exclusions; promotional ring-fence impact; product lifecycle eligibility; partial availability breakdown per order line |
| **Primary Users** | Sales Representative, Customer Service Representative, Sales Manager |
| **Source Events** | OrderAvailabilityConfirmed, StockReserved, StockReservationReleased, StockReceived, StockShipped, QuarantineHoldApplied, QuarantineHoldReleased, PromotionalStockAllocated, ProductStatusChanged, LowStockThresholdBreached, OutOfStockDetected |
| **Use Cases** | UC-013, UC-021, UC-048 |

---

### RM-003 — Quarantine and Hold Register

| Field | Detail |
|-------|--------|
| **Name** | Quarantine and Hold Register |
| **Purpose** | Answer *"What stock is physically present but not sellable, and why?"* for quality, regulatory, and customs oversight. |
| **Information Displayed** | Held quantity by product, location, and lot/batch; hold reason (quality, recall, customs, bonded); hold applied date and attribution; expected disposition; ATP exclusion impact |
| **Primary Users** | Warehouse Manager, Inventory Controller, Operations Director |
| **Source Events** | QuarantineHoldApplied, QuarantineHoldReleased, ReturnQuarantined, GoodsReceiptVerified *(bonded)* |
| **Use Cases** | UC-019, UC-037 |

---

### RM-004 — Availability Inquiry Log

| Field | Detail |
|-------|--------|
| **Name** | Availability Inquiry Log |
| **Purpose** | Answer *"What availability checks were performed and what was promised?"* for sales accountability and dispute resolution. |
| **Information Displayed** | Inquiry timestamp, product, requested quantity, location scope, ATP result, confirming user, linked order reference (if confirmed) |
| **Primary Users** | Sales Representative, Customer Service Representative, Inventory Controller |
| **Source Events** | OrderAvailabilityConfirmed |
| **Use Cases** | UC-013, UC-021 |

---

## Domain 2: Alerts & Notifications

---

### RM-005 — Operational Alert Board

| Field | Detail |
|-------|--------|
| **Name** | Operational Alert Board |
| **Purpose** | Answer *"What requires my attention right now?"* by surfacing threshold breaches, delays, exceptions, and pending approvals. |
| **Information Displayed** | Alert type (low stock, out of stock, inbound delay, transfer delay, fulfillment exception, promotional readiness gap, pending approval); severity and ABC priority; affected product and location; alert age; acknowledgment status; recommended action |
| **Primary Users** | Warehouse Manager, Purchasing Manager, Buyer, Operations Director, Marketing Manager, Customer Service Representative |
| **Source Events** | LowStockThresholdBreached, OutOfStockDetected, OverstockDetected, InboundDeliveryDelayed, InTransitStockDelayed, FulfillmentExceptionRaised, PromotionalReadinessGapIdentified, TransferRequested, AdjustmentSubmitted, ThreeWayMatchExceptionRaised, ReplenishmentRecommended, NetworkImbalanceDetected |
| **Use Cases** | UC-028, UC-047 |

---

### RM-006 — Replenishment Recommendation Log

| Field | Detail |
|-------|--------|
| **Name** | Replenishment Recommendation Log |
| **Purpose** | Answer *"What replenishment action did the business recommend and when?"* for purchasing and network balance decisions. |
| **Information Displayed** | Recommendation timestamp, product, location, triggering event, recommended action (purchase, transfer, hold), network availability context, ABC priority, acknowledgment status |
| **Primary Users** | Purchasing Manager, Buyer, Regional / Store Manager, Operations Director |
| **Source Events** | ReplenishmentRecommended, LowStockThresholdBreached, OutOfStockDetected, BackorderRecorded, NetworkImbalanceDetected |
| **Use Cases** | UC-028, UC-029, UC-034 |

---

## Domain 3: Procurement & Inbound Supply

---

### RM-007 — Open Purchase Order Board

| Field | Detail |
|-------|--------|
| **Name** | Open Purchase Order Board |
| **Purpose** | Answer *"What have we committed to buy and what is still outstanding?"* for procurement control and inbound planning. |
| **Information Displayed** | PO number, supplier, status (open, partial, closed, cancelled); line quantities ordered vs. received; receiving location; expected delivery date; linked requisition reference |
| **Primary Users** | Buyer, Purchasing Manager, Receiving Clerk, Finance Manager |
| **Source Events** | PurchaseOrderPlaced, PurchaseOrderCancelled, GoodsReceiptVerified, PutAwayCompleted, ReceiptDiscrepancyRecorded, ReceiptDiscrepancyResolved |
| **Use Cases** | UC-006, UC-030, UC-008 |

---

### RM-008 — Inbound Supply Calendar

| Field | Detail |
|-------|--------|
| **Name** | Inbound Supply Calendar |
| **Purpose** | Answer *"What inbound supply is expected and when?"* for dock preparation and replenishment timeline planning. |
| **Information Displayed** | Expected arrival date, supplier, PO reference, product lines and quantities, destination location, carrier information, delay status, receipt completion status |
| **Primary Users** | Buyer, Receiving Clerk, Warehouse Manager, Purchasing Manager |
| **Source Events** | InboundDeliveryScheduled, InboundDeliveryDelayed, PurchaseOrderPlaced, GoodsReceiptVerified, PutAwayCompleted |
| **Use Cases** | UC-007, UC-030 |

---

### RM-009 — Purchase Requisition Pipeline

| Field | Detail |
|-------|--------|
| **Name** | Purchase Requisition Pipeline |
| **Purpose** | Answer *"What internal procurement needs are pending, approved, or rejected?"* before commercial PO creation. |
| **Information Displayed** | Requisition status, requestor, product lines, target location, submission date, approval outcome, linked low-stock alert, conversion to PO status |
| **Primary Users** | Buyer, Purchasing Manager, Inventory Controller |
| **Source Events** | PurchaseRequisitionSubmitted, PurchaseRequisitionApproved, PurchaseRequisitionRejected, PurchaseOrderPlaced |
| **Use Cases** | UC-029 |

---

### RM-010 — Supplier Performance Scorecard

| Field | Detail |
|-------|--------|
| **Name** | Supplier Performance Scorecard |
| **Purpose** | Answer *"How reliably does each supplier deliver as ordered?"* for supplier accountability and sourcing decisions. |
| **Information Displayed** | Supplier, receipt discrepancy count and types, short-shipment frequency, on-time delivery rate, shelf-life rejection rate, unresolved claim status |
| **Primary Users** | Purchasing Manager, Buyer, Finance Manager, Operations Director |
| **Source Events** | ReceiptDiscrepancyRecorded, ReceiptDiscrepancyResolved, InboundDeliveryDelayed, GoodsReceiptVerified, ThreeWayMatchExceptionRaised |
| **Use Cases** | UC-009, UC-030, UC-037 |

---

### RM-011 — Receipt Discrepancy Register

| Field | Detail |
|-------|--------|
| **Name** | Receipt Discrepancy Register |
| **Purpose** | Answer *"What receipt variances are open, resolved, or pending supplier action?"* for inbound exception management. |
| **Information Displayed** | Discrepancy type, PO and receipt reference, product, variance quantity, reason code, evidence notes, resolution status, accepted vs. rejected quantities |
| **Primary Users** | Receiving Clerk, Warehouse Manager, Buyer, Finance Manager |
| **Source Events** | ReceiptDiscrepancyRecorded, ReceiptDiscrepancyResolved, GoodsReceiptVerified |
| **Use Cases** | UC-009 |

---

### RM-012 — Put-Away Work Queue

| Field | Detail |
|-------|--------|
| **Name** | Put-Away Work Queue |
| **Purpose** | Answer *"What verified stock is waiting to be stowed before it becomes sellable?"* for warehouse task prioritization. |
| **Information Displayed** | Receipt reference, product, quantity, receiving dock location, suggested storage position, rotation policy (FIFO/FEFO), bonded hold status, put-away completion status |
| **Primary Users** | Warehouse Staff, Warehouse Manager, Receiving Clerk |
| **Source Events** | GoodsReceiptVerified, PutAwayCompleted, QuarantineHoldApplied |
| **Use Cases** | UC-010 |

---

## Domain 4: Order Fulfillment

---

### RM-013 — Order Fulfillment Status Tracker

| Field | Detail |
|-------|--------|
| **Name** | Order Fulfillment Status Tracker |
| **Purpose** | Answer *"Where is each customer order in the fulfillment lifecycle?"* for customer service and operations visibility. |
| **Information Displayed** | Order reference, line status (confirmed, reserved, picking, shipped, backordered, cancelled); reservation quantity; pick verification status; shipment and carrier details; fulfillment location; exception flags |
| **Primary Users** | Customer Service Representative, Warehouse Manager, Sales Representative, Operations Director |
| **Source Events** | CustomerOrderConfirmed, CustomerOrderCancelled, StockReserved, StockReservationReleased, PickVerified, ShipmentDispatched, PartialFulfillmentCompleted, BackorderRecorded, BackorderFulfilled, FulfillmentExceptionRaised, MultiLocationFulfillmentPlanCreated |
| **Use Cases** | UC-027, UC-024, UC-025 |

---

### RM-014 — Backorder Pipeline

| Field | Detail |
|-------|--------|
| **Name** | Backorder Pipeline |
| **Purpose** | Answer *"What customer commitments are waiting for stock and how long?"* for priority replenishment and customer communication. |
| **Information Displayed** | Order reference, product, backordered quantity, customer acknowledgment date, age, priority, linked replenishment status, fulfillment progress |
| **Primary Users** | Customer Service Representative, Purchasing Manager, Buyer, Warehouse Manager |
| **Source Events** | BackorderRecorded, BackorderFulfilled, StockReceived, ReplenishmentRecommended |
| **Use Cases** | UC-025, UC-028 |

---

### RM-015 — Fill Rate Performance Report

| Field | Detail |
|-------|--------|
| **Name** | Fill Rate Performance Report |
| **Purpose** | Answer *"How completely and on time are we fulfilling customer demand?"* for service-level management. |
| **Information Displayed** | Fill rate by product, location, and period; partial fulfillment frequency; backorder rate; on-time shipment rate; order line completion time |
| **Primary Users** | Operations Director, Sales Manager, Chief Executive Officer, Warehouse Manager |
| **Source Events** | ShipmentDispatched, PartialFulfillmentCompleted, BackorderRecorded, BackorderFulfilled, FulfillmentExceptionRaised, CustomerOrderConfirmed |
| **Use Cases** | UC-037, UC-038 |

---

### RM-016 — Fulfillment Work Queue

| Field | Detail |
|-------|--------|
| **Name** | Fulfillment Work Queue |
| **Purpose** | Answer *"What orders are ready to pick, pack, and ship?"* for warehouse execution prioritization. |
| **Information Displayed** | Order priority, ship-from location, product lines and quantities, reservation status, pick path hints, rotation policy, lot/batch requirements, freeze status at location |
| **Primary Users** | Warehouse Picker / Packer, Warehouse Manager |
| **Source Events** | CustomerOrderConfirmed, StockReserved, MultiLocationFulfillmentPlanCreated, PickVerified, LocationFreezeImposed, LocationFreezeReleased |
| **Use Cases** | UC-024 |

---

## Domain 5: Network Transfer & Balance

---

### RM-017 — Transfer Pipeline and In-Transit Tracker

| Field | Detail |
|-------|--------|
| **Name** | Transfer Pipeline and In-Transit Tracker |
| **Purpose** | Answer *"What stock is moving between locations and where is it in the transfer lifecycle?"* for network visibility. |
| **Information Displayed** | Transfer reference, source and destination locations, product and quantity, status (requested, approved, in-transit, received, rejected); in-transit quantity; expected receipt date; delay flags; lot/batch attribution |
| **Primary Users** | Regional / Store Manager, Warehouse Staff, Warehouse Manager, Operations Director |
| **Source Events** | TransferRequested, TransferApproved, TransferRejected, TransferDispatched, TransferReceived, InTransitStockDelayed |
| **Use Cases** | UC-031, UC-033, UC-030 |

---

### RM-018 — Network Rebalancing Opportunity View

| Field | Detail |
|-------|--------|
| **Name** | Network Rebalancing Opportunity View |
| **Purpose** | Answer *"Where is stock maldistributed and what transfers would resolve imbalance?"* for proactive network optimization. |
| **Information Displayed** | Product, shortage location, excess location, imbalance severity, recommended transfer quantity, source spare capacity, transfer-before-buy opportunity flag |
| **Primary Users** | Operations Director, Inventory Controller, Purchasing Manager, Regional / Store Manager |
| **Source Events** | NetworkImbalanceDetected, OutOfStockDetected, OverstockDetected, LowStockThresholdBreached, ReplenishmentRecommended |
| **Use Cases** | UC-034, UC-031 |

---

### RM-019 — Network Availability Summary

| Field | Detail |
|-------|--------|
| **Name** | Network Availability Summary |
| **Purpose** | Answer *"Does the network as a whole have enough stock before we purchase?"* for replenishment and transfer decisions. |
| **Information Displayed** | Network-wide ATP by product; in-transit pipeline quantity; expected inbound quantity; location-level ATP breakdown; excess location identification |
| **Primary Users** | Buyer, Purchasing Manager, Operations Director, Regional / Store Manager |
| **Source Events** | StockReceived, StockShipped, TransferDispatched, TransferReceived, InboundDeliveryScheduled, PurchaseOrderPlaced, LowStockThresholdBreached |
| **Use Cases** | UC-029, UC-031, UC-034 |

---

## Domain 6: Inventory Accuracy & Control

---

### RM-020 — Inventory Movement History

| Field | Detail |
|-------|--------|
| **Name** | Inventory Movement History |
| **Purpose** | Answer *"What changed, where, when, and why?"* for operational investigation, traceability, and accountability. |
| **Information Displayed** | Movement type (receipt, shipment, adjustment, transfer, reservation, hold); product, location, quantity delta; lot/batch; reason code; user attribution; timestamp; linked transaction reference |
| **Primary Users** | Inventory Controller, Warehouse Manager, Finance Manager, Internal Auditor, Operations Director |
| **Source Events** | InventoryMovementRecorded *(and all quantity mutation events: StockReceived, StockShipped, StockAdjusted, StockWrittenOff, StockReserved, StockReservationReleased, QuarantineHoldApplied, QuarantineHoldReleased, ConsignmentOwnershipTransferred)* |
| **Use Cases** | UC-042, UC-037 |

---

### RM-021 — Cycle Count Schedule and Completion Log

| Field | Detail |
|-------|--------|
| **Name** | Cycle Count Schedule and Completion Log |
| **Purpose** | Answer *"What counts are scheduled, completed, or overdue?"* for inventory accuracy program management. |
| **Information Displayed** | Scheduled count date, product, location, assigned counter, ABC class, completion status, physical count result, variance flag, count frequency compliance |
| **Primary Users** | Inventory Controller, Warehouse Staff, Warehouse Manager |
| **Source Events** | CycleCountScheduled, CycleCountCompleted, CountVarianceIdentified, ProductABCClassificationAssigned |
| **Use Cases** | UC-014 |

---

### RM-022 — Physical Inventory Count Status Board

| Field | Detail |
|-------|--------|
| **Name** | Physical Inventory Count Status Board |
| **Purpose** | Answer *"What is the status of the wall-to-wall count and location freeze?"* during full physical inventory events. |
| **Information Displayed** | Location, count event status, freeze window, team assignments, lines counted vs. total, variance count, certification status, freeze active indicator |
| **Primary Users** | Inventory Controller, Warehouse Manager, Finance Manager, Operations Director |
| **Source Events** | PhysicalInventoryCountStarted, PhysicalInventoryCountCertified, LocationFreezeImposed, LocationFreezeReleased, CountVarianceIdentified |
| **Use Cases** | UC-015 |

---

### RM-023 — Inventory Accuracy Metrics Report

| Field | Detail |
|-------|--------|
| **Name** | Inventory Accuracy Metrics Report |
| **Purpose** | Answer *"How accurate is our inventory by location, product class, and period?"* for continuous improvement and audit evidence. |
| **Information Displayed** | Accuracy percentage by location and ABC class; variance count and value; count completion rate; adjustment frequency; accuracy trend over time; post-physical-count baseline |
| **Primary Users** | Inventory Controller, Operations Director, Internal Auditor, Chief Executive Officer, Finance Manager |
| **Source Events** | CycleCountCompleted, CountVarianceIdentified, CountVarianceApproved, PhysicalInventoryCountCertified, StockAdjusted, AdjustmentApproved |
| **Use Cases** | UC-016, UC-037, UC-038, UC-041 |

---

### RM-024 — Count Variance Investigation Board

| Field | Detail |
|-------|--------|
| **Name** | Count Variance Investigation Board |
| **Purpose** | Answer *"What count discrepancies are under investigation and awaiting approval?"* for variance workflow management. |
| **Information Displayed** | Variance reference, product, location, system vs. physical quantity, variance amount, counter identity, investigation status, approver, approval outcome, linked adjustment case |
| **Primary Users** | Warehouse Manager, Inventory Controller, Operations Director |
| **Source Events** | CountVarianceIdentified, CountVarianceApproved, AdjustmentSubmitted, AdjustmentApproved, AdjustmentRejected |
| **Use Cases** | UC-016 |

---

### RM-025 — Shrinkage and Loss Analysis Report

| Field | Detail |
|-------|--------|
| **Name** | Shrinkage and Loss Analysis Report |
| **Purpose** | Answer *"Where is inventory loss occurring and what are the patterns?"* for corrective action and working capital optimization. |
| **Information Displayed** | Adjustment and write-off volume by reason code, location, and product; shrinkage rate trend; obsolete and slow-moving stock; loss value by category; repeat variance hotspots |
| **Primary Users** | Inventory Controller, Finance Manager, Operations Director, Purchasing Manager |
| **Source Events** | StockAdjusted, StockWrittenOff, AdjustmentApproved, CountVarianceIdentified, ReturnWrittenOff, ProductStatusChanged |
| **Use Cases** | UC-020, UC-037 |

---

## Domain 7: Commercial & Promotional

---

### RM-026 — Promotional Allocation and Readiness View

| Field | Detail |
|-------|--------|
| **Name** | Promotional Allocation and Readiness View |
| **Purpose** | Answer *"Is ring-fenced campaign stock sufficient and protected?"* before commercial launch commitment. |
| **Information Displayed** | Campaign name and period, product, allocated quantity, consumed quantity, remaining ring-fence, general ATP impact, readiness status, gap severity, channel designation |
| **Primary Users** | Marketing Manager, Purchasing Manager, Warehouse Manager, Sales Manager |
| **Source Events** | PromotionalStockAllocated, PromotionalAllocationReleased, PromotionalReadinessGapIdentified, StockReserved, StockShipped, StockReceived |
| **Use Cases** | UC-040 |

---

### RM-027 — Campaign Performance Report

| Field | Detail |
|-------|--------|
| **Name** | Campaign Performance Report |
| **Purpose** | Answer *"How did promotional inventory perform against campaign commitment?"* after or during campaign execution. |
| **Information Displayed** | Campaign period, allocated vs. consumed quantity, sell-through rate, unallocated remainder returned to general pool, stockout during campaign, fulfillment from promotional pool vs. general ATP |
| **Primary Users** | Marketing Manager, Operations Director, Sales Manager |
| **Source Events** | PromotionalStockAllocated, PromotionalAllocationReleased, StockShipped, StockReserved, PromotionalReadinessGapIdentified |
| **Use Cases** | UC-040, UC-037 |

---

## Domain 8: Financial & Valuation

---

### RM-028 — Inventory Valuation Snapshot

| Field | Detail |
|-------|--------|
| **Name** | Inventory Valuation Snapshot |
| **Purpose** | Answer *"What is the owned inventory value at a point in time?"* for finance reconciliation and executive reporting. |
| **Information Displayed** | Period-end date, owned quantity by product and location, unit cost, extended value, consignment exclusion, quarantine exclusion, in-transit exclusion, total valuation |
| **Primary Users** | Finance Manager, Chief Financial Officer, Inventory Controller, Chief Executive Officer |
| **Source Events** | InventoryValuationSnapshotPrepared, StockReceived, StockShipped, StockWrittenOff, ConsignmentOwnershipTransferred, AdjustmentApproved, ThreeWayMatchCompleted |
| **Use Cases** | UC-039, UC-038 |

---

### RM-029 — Valuation Reconciliation Status Board

| Field | Detail |
|-------|--------|
| **Name** | Valuation Reconciliation Status Board |
| **Purpose** | Answer *"Are operational inventory records aligned with the general ledger?"* for month-end close management. |
| **Information Displayed** | Snapshot reference, operational valuation total, general ledger balance, variance amount, tolerance threshold, reconciliation status, investigation notes, close readiness indicator |
| **Primary Users** | Finance Manager, Chief Financial Officer, Inventory Controller, Internal Auditor |
| **Source Events** | InventoryValuationSnapshotPrepared, ValuationVarianceIdentified, StockAdjusted, StockWrittenOff, ConsignmentOwnershipTransferred |
| **Use Cases** | UC-039 |

---

### RM-030 — Three-Way Match Status Board

| Field | Detail |
|-------|--------|
| **Name** | Three-Way Match Status Board |
| **Purpose** | Answer *"Which supplier invoices are matched, blocked, or awaiting resolution?"* for payment control. |
| **Information Displayed** | Invoice reference, supplier, PO and receipt linkage, match status (matched, exception, pending), quantity and price variance, payment authorization status |
| **Primary Users** | Finance Manager, Buyer, Purchasing Manager, Chief Financial Officer |
| **Source Events** | SupplierInvoiceReceived, ThreeWayMatchCompleted, ThreeWayMatchExceptionRaised, ReceiptDiscrepancyResolved, GoodsReceiptVerified |
| **Use Cases** | UC-039, UC-006 |

---

### RM-031 — Executive KPI Dashboard

| Field | Detail |
|-------|--------|
| **Name** | Executive KPI Dashboard |
| **Purpose** | Answer *"How is inventory performing as a strategic business asset?"* for leadership decision-making. |
| **Information Displayed** | Inventory turnover, fill rate, accuracy rate, stockout frequency, days of supply, working capital tied in inventory, shrinkage rate, network imbalance index, valuation trend |
| **Primary Users** | Chief Executive Officer, Chief Financial Officer, Chief Operating Officer, Operations Director |
| **Source Events** | InventoryValuationSnapshotPrepared, OutOfStockDetected, OverstockDetected, ShipmentDispatched, PartialFulfillmentCompleted, CycleCountCompleted, CountVarianceIdentified, StockWrittenOff, NetworkImbalanceDetected, LowStockThresholdBreached |
| **Use Cases** | UC-038, UC-037 |

---

## Domain 9: Governance & Compliance

---

### RM-032 — Audit Trail Register

| Field | Detail |
|-------|--------|
| **Name** | Audit Trail Register |
| **Purpose** | Answer *"Who changed what, when, and with whose approval?"* for governance, compliance, and fraud investigation. |
| **Information Displayed** | Transaction type, entity affected, before/after state, user identity, timestamp, approval chain, reason code, location scope |
| **Primary Users** | Internal Auditor, External Auditor, Finance Manager, Operations Director, System Administrator |
| **Source Events** | AuditTrailRecorded *(and governed events: AdjustmentApproved, ProductStatusChanged, RoleAssignmentChanged, GovernancePolicyPublished, CountVarianceApproved, StockWrittenOff, SegregationOfDutiesViolationDetected)* |
| **Use Cases** | UC-043, UC-041 |

---

### RM-033 — Adjustment Case History

| Field | Detail |
|-------|--------|
| **Name** | Adjustment Case History |
| **Purpose** | Answer *"What inventory corrections and write-offs were proposed, approved, or rejected?"* for governance review. |
| **Information Displayed** | Case reference, type (variance, adjustment, write-off), product, location, quantity, reason code, initiator, approver, status, investigation notes, threshold breach flag |
| **Primary Users** | Warehouse Manager, Operations Director, Inventory Controller, Internal Auditor, Finance Manager |
| **Source Events** | AdjustmentSubmitted, AdjustmentApproved, AdjustmentRejected, CountVarianceIdentified, CountVarianceApproved, StockAdjusted, StockWrittenOff |
| **Use Cases** | UC-017, UC-018, UC-016, UC-041 |

---

### RM-034 — Segregation of Duties Violation Log

| Field | Detail |
|-------|--------|
| **Name** | Segregation of Duties Violation Log |
| **Purpose** | Answer *"Were accountability controls breached?"* for control testing and security review. |
| **Information Displayed** | Violation timestamp, attempted action, user identity, conflicting roles, blocked command, affected transaction reference |
| **Primary Users** | Internal Auditor, System Administrator, Operations Director |
| **Source Events** | SegregationOfDutiesViolationDetected |
| **Use Cases** | UC-041, UC-045 |

---

## Domain 10: Master Data & Reference

---

### RM-035 — Product Catalog Directory

| Field | Detail |
|-------|--------|
| **Name** | Product Catalog Directory |
| **Purpose** | Answer *"What is the authoritative product identity and definition?"* for all operational lookups and references. |
| **Information Displayed** | SKU, name, description, unit of measure, category, barcode, lifecycle status, ABC class, rotation policy, traceability requirements, shelf-life profile |
| **Primary Users** | Inventory Controller, Sales Representative, Buyer, Receiving Clerk, Warehouse Staff |
| **Source Events** | ProductRegistered, ProductStatusChanged, ProductABCClassificationAssigned |
| **Use Cases** | UC-001, UC-013, UC-046 |

---

### RM-036 — Location Network Directory

| Field | Detail |
|-------|--------|
| **Name** | Location Network Directory |
| **Purpose** | Answer *"What locations exist, how are they organized, and are they operational?"* for network-scoped operations. |
| **Information Displayed** | Location code, name, type, hierarchy path, operational status, freeze status, go-live date, parent location, storage position count |
| **Primary Users** | Inventory Controller, Warehouse Manager, Regional / Store Manager, System Administrator |
| **Source Events** | InventoryLocationActivated, InventoryLocationDeactivated, StoragePositionConfigured, LocationFreezeImposed, LocationFreezeReleased |
| **Use Cases** | UC-002, UC-046 |

---

### RM-037 — Warehouse Layout Reference

| Field | Detail |
|-------|--------|
| **Name** | Warehouse Layout Reference |
| **Purpose** | Answer *"Where should stock be placed or picked from?"* for put-away and pick path operations. |
| **Information Displayed** | Storage position hierarchy (zone, aisle, bin), location assignment, capacity indicators, rotation zone designation, active/inactive status |
| **Primary Users** | Warehouse Staff, Warehouse Manager, Inventory Controller |
| **Source Events** | StoragePositionConfigured, InventoryLocationActivated |
| **Use Cases** | UC-002, UC-010 |

---

### RM-038 — Governance Policy and Reason Code Catalog

| Field | Detail |
|-------|--------|
| **Name** | Governance Policy and Reason Code Catalog |
| **Purpose** | Answer *"What rules and reason codes govern inventory exceptions and corrections?"* for consistent accountability. |
| **Information Displayed** | Active governance policy version, effective period, approval thresholds, tolerance limits, reason code list with category and status (active/retired), applicable transaction types |
| **Primary Users** | Inventory Controller, Warehouse Manager, Internal Auditor, Finance Manager |
| **Source Events** | GovernancePolicyPublished, ReasonCodeRetired |
| **Use Cases** | UC-005, UC-017, UC-041 |

---

### RM-039 — Stock Policy Registry

| Field | Detail |
|-------|--------|
| **Name** | Stock Policy Registry |
| **Purpose** | Answer *"What replenishment thresholds apply to each product at each location?"* for monitoring and planning. |
| **Information Displayed** | Product, location, reorder level, minimum threshold, safety stock, maximum level, effective date, prior threshold history, policy change attribution |
| **Primary Users** | Inventory Controller, Purchasing Manager, Operations Director |
| **Source Events** | StockPolicyThresholdChanged, ProductRegistered, InventoryLocationActivated |
| **Use Cases** | UC-003, UC-012 |

---

## Read Model-to-Event Source Matrix

| Read Model | Primary Source Events | Event Count |
|------------|----------------------|-------------|
| RM-001 Network Stock Status Board | Stock mutation + status events | 16 |
| RM-005 Operational Alert Board | Threshold, delay, exception events | 12 |
| RM-007 Open Purchase Order Board | PO and receipt lifecycle | 6 |
| RM-013 Order Fulfillment Status Tracker | Order fulfillment lifecycle | 11 |
| RM-020 Inventory Movement History | InventoryMovementRecorded + mutations | 10+ |
| RM-028 Inventory Valuation Snapshot | Valuation and quantity events | 7 |
| RM-032 Audit Trail Register | AuditTrailRecorded + governed events | 8+ |
| RM-035 Product Catalog Directory | Product lifecycle events | 3 |

---

## Read Model-to-Use Case Coverage

| Use Case | Read Models Served |
|----------|-------------------|
| UC-012 Monitor Inventory Status | RM-001, RM-039 |
| UC-013 Inquire Availability | RM-002, RM-004, RM-035 |
| UC-020 Analyze Shrinkage | RM-025, RM-033 |
| UC-027 View Order Fulfillment Status | RM-013, RM-014 |
| UC-028 Review Low-Stock Alerts | RM-005, RM-006 |
| UC-030 Track Inbound Supply | RM-007, RM-008 |
| UC-037 Operational Dashboards | RM-001, RM-015, RM-023, RM-025, RM-031 |
| UC-038 Executive KPIs | RM-031, RM-028, RM-023 |
| UC-039 Reconcile Valuation | RM-028, RM-029, RM-030 |
| UC-040 Promotional Readiness | RM-026, RM-027 |
| UC-041 Audit Review | RM-032, RM-033, RM-034, RM-023 |
| UC-042 Movement History | RM-020 |
| UC-043 Audit Trail | RM-032 |
| UC-047 Operational Notifications | RM-005 |

---

## Excluded from Read Models

| Capability | Treatment | Rationale |
|------------|-----------|-----------|
| Aggregate current state query | Write model | ATP and on-hand authority lives in Stock Position aggregate — availability views project from events but operational commands read aggregate state for consistency |
| Ad-hoc SQL analytics | External BI | Exploratory analysis outside IMS bounded context |
| Real-time command validation | Domain service | Eligibility and freeze checks are synchronous evaluations, not read models |
| User session and permission cache | Infrastructure | Identity layer concern, not inventory intelligence |

---

## Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Domain Expert | | | |
| DDD Architect | | | |
| Senior Business Analyst | | | |
| Solution Architect | | | |

---

*End of Read Models*

*Document ID: SRS-ES-005 | Version 1.0 | July 6, 2026*
