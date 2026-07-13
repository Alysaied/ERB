# Domain Events
## Inventory Management System

---

## Document Information

| Attribute | Detail |
|-----------|--------|
| **Document ID** | SRS-DM-006 |
| **Document Title** | Domain Events — Inventory Management System |
| **Version** | 1.0 |
| **Status** | Draft |
| **Document Owner** | Domain Expert |
| **Source Documents** | SRS-DM-001 (Domain Entity Model), SRS-DM-003 (Domain Aggregates), SRS-DM-005 (Domain Services), SRS-BR-001 (Business Rules), SRS-UC-001 (Use Case Catalog) |
| **Date** | July 5, 2026 |
| **Scope** | Business domain events only — no message brokers, event buses, or integration technology |

### Purpose

This document identifies **Domain Events** for the Inventory Management System. A domain event is an immutable record of something meaningful that happened in the business — expressed in past tense from the domain's ubiquitous language. Events announce state changes within aggregates and enable loose coupling between aggregates, read models, and downstream business reactions.

Domain events are **facts**, not commands. They describe what occurred; consumers decide how to respond.

### Event Naming Convention

Events are named in **PascalCase past tense**: `StockReserved`, `PutAwayCompleted`, `CountVarianceIdentified`. Each name should be understandable to business stakeholders without technical context.

### Consumer Types

| Consumer Type | Role |
|---------------|------|
| **Aggregate** | Another consistency boundary that reacts by updating its own state |
| **Domain Service** | Stateless evaluator triggered to apply cross-aggregate business rules |
| **Read Model / Projection** | Derived view rebuilt from events (movement history, alerts, dashboards) |
| **Business Process** | Human workflow or notification triggered for actor action |

---

## Event Catalog Overview

| Domain Area | Events | IDs |
|-------------|--------|-----|
| Catalog & Network | Product and location lifecycle | DE-001 – DE-010 |
| Inventory Balance | Stock quantity and hold state | DE-011 – DE-022 |
| Procurement & Inbound | Requisition through receipt | DE-023 – DE-035 |
| Order Fulfillment | Order commitment through shipment | DE-036 – DE-045 |
| Network Transfer | Inter-location movement | DE-046 – DE-051 |
| Inventory Control | Counting and correction | DE-052 – DE-060 |
| Returns | Reverse logistics | DE-061 – DE-067 |
| Commercial & Monitoring | Promotions and alerts | DE-068 – DE-073 |
| Financial & Governance | Finance alignment and audit | DE-074 – DE-081 |

**Total Domain Events:** 81

---

## Domain 1: Catalog & Network

---

### DE-001 — ProductRegistered

| Aspect | Detail |
|--------|--------|
| **Trigger** | Inventory Controller creates a new product record with unique SKU, name, and unit of measure in the Product Catalog aggregate. |
| **Related Aggregate** | Product Catalog |
| **Business Meaning** | The organization has introduced a new SKU into the trusted product catalog. The product is now eligible for stock policy assignment, procurement, and (when active) fulfillment referencing. |
| **Consumers** | Stock Policy aggregate *(policy may be assigned)*; Read Model — product catalog index; Business Process — master data notification to operational teams |

---

### DE-002 — ProductStatusChanged

| Aspect | Detail |
|--------|--------|
| **Trigger** | Product lifecycle status transitions among active, inactive, or discontinued within the Product Catalog aggregate. |
| **Related Aggregate** | Product Catalog |
| **Business Meaning** | The commercial availability of a SKU has changed. Discontinued status prohibits new procurement and reservations; inactive status restricts new customer commitments. |
| **Consumers** | Product Transaction Eligibility domain service *(DS-024)*; Purchase Order aggregate *(blocks new lines)*; Customer Order Fulfillment aggregate *(blocks new reservations)*; Replenishment Recommendation domain service *(DS-005)*; Read Model — product status history |

---

### DE-003 — ProductABCClassificationAssigned

| Aspect | Detail |
|--------|--------|
| **Trigger** | Inventory Controller assigns or updates ABC classification (A, B, or C) on a product during classification review. |
| **Related Aggregate** | Product Catalog |
| **Business Meaning** | Operational priority for the SKU has been set. Class A products receive highest count frequency, monitoring intensity, and alert priority per BR-032. |
| **Consumers** | Cycle Count aggregate *(scheduling priority)*; Low-Stock Alert Evaluation domain service *(DS-018)*; Read Model — ABC classification report |

---

### DE-004 — InventoryLocationActivated

| Aspect | Detail |
|--------|--------|
| **Trigger** | Inventory Location transitions to active operational status after opening balance approval at go-live. |
| **Related Aggregate** | Inventory Location |
| **Business Meaning** | A location is authorized to receive, hold, fulfill, and transact inventory. Stock positions may be established and operational workflows enabled. |
| **Consumers** | Stock Position aggregate *(opening balances created)*; Read Model — location network index; Business Process — go-live notification to warehouse team |

---

### DE-005 — InventoryLocationDeactivated

| Aspect | Detail |
|--------|--------|
| **Trigger** | Inventory Location is deactivated after stock disposition is complete or closure is authorized. |
| **Related Aggregate** | Inventory Location |
| **Business Meaning** | A location is no longer authorized for new inventory activity. Existing stock must have been cleared or dispositioned before deactivation. |
| **Consumers** | Physical Inventory Freeze Guard domain service *(DS-014)*; Purchase Order aggregate *(blocks new receiving)*; Customer Order Fulfillment aggregate *(blocks new fulfillment)*; Read Model — location status history |

---

### DE-006 — StoragePositionConfigured

| Aspect | Detail |
|--------|--------|
| **Trigger** | New storage position (zone, aisle, bin) is added or updated within an Inventory Location aggregate. |
| **Related Aggregate** | Inventory Location |
| **Business Meaning** | A findable physical address within a location is available for put-away placement and pick path guidance. |
| **Consumers** | Put-Away Activation domain service *(DS-009)*; Stock Rotation Selection domain service *(DS-011)*; Read Model — warehouse layout reference |

---

### DE-007 — LocationFreezeImposed

| Aspect | Detail |
|--------|--------|
| **Trigger** | Physical Inventory Count aggregate begins wall-to-wall count at a location, imposing operational freeze. |
| **Related Aggregate** | Physical Inventory Count |
| **Business Meaning** | All receiving, shipping, transfers, and adjustments at the location are suspended until the count is certified complete. Ensures stable snapshot for accurate counting per BR-024. |
| **Consumers** | Physical Inventory Freeze Guard domain service *(DS-014)*; Goods Receipt aggregate *(blocks receipt)*; Customer Order Fulfillment aggregate *(blocks shipment)*; Stock Transfer aggregate *(blocks dispatch/receipt)*; Inventory Adjustment Case aggregate *(blocks non-count adjustments)*; Business Process — freeze notification to warehouse staff |

---

### DE-008 — LocationFreezeReleased

| Aspect | Detail |
|--------|--------|
| **Trigger** | Physical Inventory Count aggregate certifies count completion and releases location freeze. |
| **Related Aggregate** | Physical Inventory Count |
| **Business Meaning** | Normal inventory operations may resume at the location. Count variances have been identified and routed for investigation. |
| **Consumers** | Physical Inventory Freeze Guard domain service *(DS-014)*; Business Process — operations resume notification to warehouse staff |

---

### DE-009 — GovernancePolicyPublished

| Aspect | Detail |
|--------|--------|
| **Trigger** | New or updated governance policy version becomes effective in the Inventory Governance aggregate (approval thresholds, tolerances, exception rules). |
| **Related Aggregate** | Inventory Governance |
| **Business Meaning** | Organization-wide inventory control parameters have changed. All subsequent transactions must evaluate against the new effective policy. |
| **Consumers** | Adjustment Governance Evaluation domain service *(DS-015)*; Receipt Verification domain service *(DS-008)*; Three-Way Match Evaluation domain service *(DS-010)*; Read Model — policy version history |

---

### DE-010 — ReasonCodeRetired

| Aspect | Detail |
|--------|--------|
| **Trigger** | A reason code is marked retired in the Inventory Governance aggregate and removed from active selection lists. |
| **Related Aggregate** | Inventory Governance |
| **Business Meaning** | A categorized exception reason is no longer valid for new transactions. Historical records retain prior reason code attributions unchanged. |
| **Consumers** | Adjustment Governance Evaluation domain service *(DS-015)*; Read Model — reason code catalog |

---

## Domain 2: Inventory Balance

---

### DE-011 — StockReceived

| Aspect | Detail |
|--------|--------|
| **Trigger** | Put-away is confirmed and Stock Position aggregate increases on-hand quantity for a product at a location. |
| **Related Aggregate** | Stock Position |
| **Business Meaning** | Verified inbound stock is now physically placed and recorded as on-hand inventory. ATP increases correspondingly unless quarantine or ownership rules apply. |
| **Consumers** | Stock Status Classification domain service *(DS-017)*; Inventory Movement Record read model; Audit Trail Record read model; Network Availability Evaluation domain service *(DS-004)* |

---

### DE-012 — StockReserved

| Aspect | Detail |
|--------|--------|
| **Trigger** | Stock Position aggregate increases reserved quantity and decreases ATP following reservation coordination for a confirmed customer order. |
| **Related Aggregate** | Stock Position |
| **Business Meaning** | Quantity is operationally committed to a customer order and is no longer available for new sales promises. Prevents double-allocation per BR-002. |
| **Consumers** | Customer Order Fulfillment aggregate *(reservation confirmed)*; Inventory Movement Record read model; Stock Status Classification domain service *(DS-017)* |

---

### DE-013 — StockReservationReleased

| Aspect | Detail |
|--------|--------|
| **Trigger** | Stock Position aggregate decreases reserved quantity and restores ATP when a reservation is cancelled or order line removed. |
| **Related Aggregate** | Stock Position |
| **Business Meaning** | Previously committed stock is returned to available-to-promise pool and may be promised to other customers or orders. |
| **Consumers** | Customer Order Fulfillment aggregate *(reservation cleared)*; Inventory Movement Record read model; Low-Stock Alert Evaluation domain service *(DS-018)* |

---

### DE-014 — StockShipped

| Aspect | Detail |
|--------|--------|
| **Trigger** | Stock Position aggregate decreases on-hand and reserved quantity upon verified shipment dispatch. |
| **Related Aggregate** | Stock Position |
| **Business Meaning** | Physical stock has left the location for customer delivery. Inventory record reflects deduction only after verified pick per BR-003. |
| **Consumers** | Customer Order Fulfillment aggregate *(shipment confirmed)*; Consignment Ownership Evaluation domain service *(DS-021)*; Inventory Movement Record read model; Stock Status Classification domain service *(DS-017)*; Read Model — fill rate metrics |

---

### DE-015 — StockAdjusted

| Aspect | Detail |
|--------|--------|
| **Trigger** | Approved Stock Adjustment is applied and Stock Position on-hand quantity is corrected with mandatory reason code. |
| **Related Aggregate** | Stock Position |
| **Business Meaning** | Recorded inventory has been aligned with physical reality following investigation and authorization. Distinct from write-off — adjustment is a correction, not permanent value removal. |
| **Consumers** | Inventory Adjustment Case aggregate *(adjustment finalized)*; Inventory Movement Record read model; Audit Trail Record read model; Stock Status Classification domain service *(DS-017)*; Read Model — shrinkage analysis |

---

### DE-016 — StockWrittenOff

| Aspect | Detail |
|--------|--------|
| **Trigger** | Authorized Inventory Write-Off permanently removes quantity and value from Stock Position. |
| **Related Aggregate** | Stock Position |
| **Business Meaning** | Inventory value has been formally removed for damaged, obsolete, expired, or lost goods. Terminal event — quantity cannot be restored without new receipt per BR-023. |
| **Consumers** | Inventory Adjustment Case aggregate *(write-off finalized)*; Inventory Valuation Reconciliation domain service *(DS-022)*; Inventory Movement Record read model; Audit Trail Record read model; Read Model — shrinkage and loss reporting |

---

### DE-017 — QuarantineHoldApplied

| Aspect | Detail |
|--------|--------|
| **Trigger** | Quarantine Hold is placed on quantity within Stock Position, excluding it from ATP. |
| **Related Aggregate** | Stock Position |
| **Business Meaning** | Stock is physically present but not sellable due to quality investigation, regulatory restriction, recall, or customs hold. ATP reduced accordingly per BR-013. |
| **Consumers** | Availability Confirmation domain service *(DS-001)*; Inventory Movement Record read model; Business Process — quality/regulatory investigation workflow |

---

### DE-018 — QuarantineHoldReleased

| Aspect | Detail |
|--------|--------|
| **Trigger** | Quarantine Hold is cleared after quality approval, customs clearance, or disposition decision, restoring quantity to ATP. |
| **Related Aggregate** | Stock Position |
| **Business Meaning** | Previously held stock is cleared for sale or fulfillment. Bonded inventory cleared for domestic commerce per BR-030. |
| **Consumers** | Put-Away Activation domain service *(DS-009)*; Availability Confirmation domain service *(DS-001)*; Inventory Movement Record read model |

---

### DE-019 — StockPolicyThresholdChanged

| Aspect | Detail |
|--------|--------|
| **Trigger** | Stock Policy aggregate records new reorder level, minimum, safety stock, or maximum thresholds with effective date. |
| **Related Aggregate** | Stock Policy |
| **Business Meaning** | Replenishment and alert rules for a product at a location have been recalibrated. Future low-stock detection uses new thresholds per BR-009. |
| **Consumers** | Stock Status Classification domain service *(DS-017)*; Low-Stock Alert Evaluation domain service *(DS-018)*; Replenishment Recommendation domain service *(DS-005)*; Read Model — policy change history |

---

### DE-020 — PromotionalStockAllocated

| Aspect | Detail |
|--------|--------|
| **Trigger** | Promotional Stock Allocation aggregate ring-fences quantity for a campaign or launch period. |
| **Related Aggregate** | Promotional Stock Allocation |
| **Business Meaning** | Defined inventory quantity is reserved for promotional or launch use and excluded from general ATP for non-approved orders per BR-029. |
| **Consumers** | Stock Position aggregate *(ATP segregation)*; Availability Confirmation domain service *(DS-001)*; Promotional Readiness Evaluation domain service *(DS-019)*; Business Process — marketing readiness notification |

---

### DE-021 — PromotionalAllocationReleased

| Aspect | Detail |
|--------|--------|
| **Trigger** | Campaign period ends or allocation is manually released; ring-fenced quantity returns to general availability. |
| **Related Aggregate** | Promotional Stock Allocation |
| **Business Meaning** | Un consumed promotional stock is returned to general sellable pool. Campaign commitment period has concluded. |
| **Consumers** | Stock Position aggregate *(ATP restored)*; Availability Confirmation domain service *(DS-001)*; Read Model — campaign performance report |

---

### DE-022 — ConsignmentOwnershipTransferred

| Aspect | Detail |
|--------|--------|
| **Trigger** | Consignment stock ownership transfers from supplier to organization upon defined consumption or sale event per supplier agreement. |
| **Related Aggregate** | Stock Position |
| **Business Meaning** | Stock previously held under consignment classification becomes owned inventory for valuation and financial recording per BR-031. |
| **Consumers** | Consignment Ownership Evaluation domain service *(DS-021)*; Inventory Valuation Reconciliation domain service *(DS-022)*; Inventory Movement Record read model |

---

## Domain 3: Procurement & Inbound

---

### DE-023 — PurchaseRequisitionSubmitted

| Aspect | Detail |
|--------|--------|
| **Trigger** | Internal replenishment need is recorded and submitted for approval in the Purchase Requisition aggregate. |
| **Related Aggregate** | Purchase Requisition |
| **Business Meaning** | The organization has identified a procurement need for specific products at a target location, pending internal approval before commercial PO creation. |
| **Consumers** | Network Availability Evaluation domain service *(DS-004)*; Business Process — purchasing manager approval workflow; Read Model — requisition pipeline |

---

### DE-024 — PurchaseRequisitionApproved

| Aspect | Detail |
|--------|--------|
| **Trigger** | Purchase Requisition reaches approved status after network check and policy validation. |
| **Related Aggregate** | Purchase Requisition |
| **Business Meaning** | Internal authorization to proceed with supplier procurement is granted. Requisition is eligible for conversion to Purchase Order. |
| **Consumers** | Purchase Order aggregate *(PO creation initiated)*; Business Process — buyer notification to create PO |

---

### DE-025 — PurchaseRequisitionRejected

| Aspect | Detail |
|--------|--------|
| **Trigger** | Purchase Requisition is rejected — e.g., network transfer alternative identified or policy violation. |
| **Related Aggregate** | Purchase Requisition |
| **Business Meaning** | Procurement request denied. Network redistribution or other alternative should be pursued instead of new purchase per BR-011. |
| **Consumers** | Business Process — requestor notification; Read Model — requisition status history |

---

### DE-026 — PurchaseOrderPlaced

| Aspect | Detail |
|--------|--------|
| **Trigger** | Authorized commercial commitment is recorded with supplier, products, quantities, and delivery terms in the Purchase Order aggregate. |
| **Related Aggregate** | Purchase Order |
| **Business Meaning** | The organization has committed to purchase specified goods from a supplier. Inbound receipt is authorized upon delivery per BR-007. |
| **Consumers** | Expected Inbound Delivery aggregate *(delivery planning)*; Business Process — supplier notification; Read Model — open PO dashboard; Inbound supply tracking |

---

### DE-027 — PurchaseOrderCancelled

| Aspect | Detail |
|--------|--------|
| **Trigger** | Open Purchase Order is cancelled before full receipt. |
| **Related Aggregate** | Purchase Order |
| **Business Meaning** | Commercial commitment to supplier is withdrawn. No further receipts authorized against cancelled PO lines. |
| **Consumers** | Expected Inbound Delivery aggregate *(schedule cancelled)*; Business Process — supplier and buyer notification; Read Model — PO status history |

---

### DE-028 — InboundDeliveryScheduled

| Aspect | Detail |
|--------|--------|
| **Trigger** | Expected Inbound Delivery is planned with arrival date and quantity tied to a Purchase Order. |
| **Related Aggregate** | Purchase Order |
| **Business Meaning** | Receiving operations and replenishment planners are informed when and what quantity to expect, supporting dock preparation and inbound visibility. |
| **Consumers** | Read Model — inbound supply calendar; Network Availability Evaluation domain service *(DS-004)*; Business Process — receiving clerk preparation notification |

---

### DE-029 — InboundDeliveryDelayed

| Aspect | Detail |
|--------|--------|
| **Trigger** | Expected arrival date passes without Goods Receipt, or supplier communicates schedule change. |
| **Related Aggregate** | Purchase Order |
| **Business Meaning** | Anticipated inbound supply will arrive later than planned. Replenishment timelines and fulfillment promises may be affected. |
| **Consumers** | Operational Alert read model *(inbound delay alert)*; Replenishment Recommendation domain service *(DS-005)*; Business Process — buyer and purchasing manager notification *(UC-047)* |

---

### DE-030 — GoodsReceiptVerified

| Aspect | Detail |
|--------|--------|
| **Trigger** | Inbound goods pass verification against Purchase Order — quantity, product identity, and condition confirmed in Goods Receipt aggregate. |
| **Related Aggregate** | Goods Receipt |
| **Business Meaning** | The business has confirmed what actually arrived at the dock matches authorized expectation. Stock is not yet available — put-away must follow per BR-004, BR-005. |
| **Consumers** | Receipt Verification domain service *(DS-008)*; Three-Way Match Evaluation domain service *(DS-010)*; Business Process — put-away task generation |

---

### DE-031 — ReceiptDiscrepancyRecorded

| Aspect | Detail |
|--------|--------|
| **Trigger** | Variance between expected and received goods is documented with evidence at receipt in Goods Receipt aggregate. |
| **Related Aggregate** | Goods Receipt |
| **Business Meaning** | Short shipment, over-shipment, wrong item, damage, or shelf-life non-compliance captured at point of receipt when evidence exists per BR-006. |
| **Consumers** | Three-Way Match Evaluation domain service *(DS-010)*; Business Process — supplier claim and buyer notification; Read Model — supplier performance tracking |

---

### DE-032 — ReceiptDiscrepancyResolved

| Aspect | Detail |
|--------|--------|
| **Trigger** | Receipt discrepancy reaches resolved status — partial acceptance, rejection, or supplier claim completed. |
| **Related Aggregate** | Goods Receipt |
| **Business Meaning** | Receipt exception has been closed with documented outcome. Accepted quantities may proceed to put-away; rejected quantities will not enter inventory. |
| **Consumers** | Three-Way Match Evaluation domain service *(DS-010)*; Read Model — discrepancy resolution history |

---

### DE-033 — PutAwayCompleted

| Aspect | Detail |
|--------|--------|
| **Trigger** | Received goods are confirmed placed in designated storage position within Goods Receipt aggregate. |
| **Related Aggregate** | Goods Receipt |
| **Business Meaning** | Inbound stock has transitioned from receiving dock to operational storage. Triggers availability activation — stock may now enter sellable ATP per BR-005. |
| **Consumers** | Put-Away Activation domain service *(DS-009)*; Stock Position aggregate *(StockReceived)*; Purchase Order aggregate *(received quantity updated)*; Inventory Movement Record read model |

---

### DE-034 — SupplierInvoiceReceived

| Aspect | Detail |
|--------|--------|
| **Trigger** | Supplier billing document is recorded in the Supplier Invoice aggregate. |
| **Related Aggregate** | Supplier Invoice |
| **Business Meaning** | Supplier has invoiced for goods supplied. Three-way match evaluation against PO and receipt must proceed before payment authorization per BR-008. |
| **Consumers** | Three-Way Match Evaluation domain service *(DS-010)*; Business Process — finance accounts payable workflow |

---

### DE-035 — ThreeWayMatchCompleted

| Aspect | Detail |
|--------|--------|
| **Trigger** | PO, goods receipt, and supplier invoice lines agree within tolerance in Supplier Invoice aggregate. |
| **Related Aggregate** | Supplier Invoice |
| **Business Meaning** | Financial control confirmed — payment for received, authorized goods may proceed. Closes the procurement-to-payment accountability loop per BR-008. |
| **Consumers** | Inventory Valuation Reconciliation domain service *(DS-022)*; Business Process — payment authorization to finance; Read Model — match status dashboard |

---

## Domain 4: Order Fulfillment

---

### DE-036 — OrderAvailabilityConfirmed

| Aspect | Detail |
|--------|--------|
| **Trigger** | Availability Confirmation domain service validates order lines against ATP and records confirmation result on Customer Order Fulfillment aggregate. |
| **Related Aggregate** | Customer Order Fulfillment |
| **Business Meaning** | The business has verified that available-to-promise stock can support the order (fully or partially) before commercial commitment per BR-001. |
| **Consumers** | Business Process — sales/customer service confirmation to customer; Read Model — availability inquiry log |

---

### DE-037 — CustomerOrderConfirmed

| Aspect | Detail |
|--------|--------|
| **Trigger** | Customer order transitions to confirmed status ready for reservation and fulfillment execution. |
| **Related Aggregate** | Customer Order Fulfillment |
| **Business Meaning** | Commercial commitment to fulfill the order is established. Reservation of stock must follow immediately per BR-002. |
| **Consumers** | Inventory Reservation Coordination domain service *(DS-002)*; Business Process — warehouse fulfillment queue |

---

### DE-038 — CustomerOrderCancelled

| Aspect | Detail |
|--------|--------|
| **Trigger** | Confirmed customer order or order line is cancelled before full shipment. |
| **Related Aggregate** | Customer Order Fulfillment |
| **Business Meaning** | Commercial commitment withdrawn. Reserved stock must be released back to ATP. |
| **Consumers** | Inventory Reservation Coordination domain service *(DS-002)* → StockReservationReleased; Business Process — customer cancellation confirmation |

---

### DE-039 — PickVerified

| Aspect | Detail |
|--------|--------|
| **Trigger** | Warehouse picker confirms correct items retrieved and verified against order in Fulfillment Execution within Customer Order Fulfillment aggregate. |
| **Related Aggregate** | Customer Order Fulfillment |
| **Business Meaning** | Physical pick matches order requirements. Shipment is authorized to proceed per BR-003. Lot/batch captured for traceable products per BR-017. |
| **Consumers** | Shipment Completion Coordination domain service *(DS-012)*; Inventory Movement Record read model |

---

### DE-040 — ShipmentDispatched

| Aspect | Detail |
|--------|--------|
| **Trigger** | Verified goods handed to carrier and shipment recorded in Customer Order Fulfillment aggregate. |
| **Related Aggregate** | Customer Order Fulfillment |
| **Business Meaning** | Order goods have left the warehouse. Inventory deduction and reservation consumption triggered. Delivery promise activated for customer. |
| **Consumers** | Shipment Completion Coordination domain service *(DS-012)* → StockShipped; Inventory Movement Record read model; Business Process — customer shipment notification *(UC-027)*; Read Model — on-time delivery metrics |

---

### DE-041 — PartialFulfillmentCompleted

| Aspect | Detail |
|--------|--------|
| **Trigger** | Available portion of order line shipped while remainder is backordered or awaiting stock. |
| **Related Aggregate** | Customer Order Fulfillment |
| **Business Meaning** | Customer receives available quantity now; unfulfilled portion handled separately via backorder with customer acknowledgment per BR-028. |
| **Consumers** | Partial Fulfillment and Backorder Orchestration domain service *(DS-013)*; Business Process — customer partial shipment notification |

---

### DE-042 — BackorderRecorded

| Aspect | Detail |
|--------|--------|
| **Trigger** | Unfulfilled order quantity recorded as backorder after customer acknowledgment in Customer Order Fulfillment aggregate. |
| **Related Aggregate** | Customer Order Fulfillment |
| **Business Meaning** | Customer has agreed to wait for remaining quantity. Mutual commercial commitment — not an internal note per BR-028. |
| **Consumers** | Replenishment Recommendation domain service *(DS-005)* *(priority replenishment)*; Business Process — customer backorder confirmation; Read Model — backorder pipeline |

---

### DE-043 — BackorderFulfilled

| Aspect | Detail |
|--------|--------|
| **Trigger** | Previously backordered quantity is reserved and fulfilled when stock becomes available. |
| **Related Aggregate** | Customer Order Fulfillment |
| **Business Meaning** | Delayed customer commitment is now being executed. Backorder closed for fulfilled quantity. |
| **Consumers** | Inventory Reservation Coordination domain service *(DS-002)*; Business Process — customer notification of backorder shipment |

---

### DE-044 — FulfillmentExceptionRaised

| Aspect | Detail |
|--------|--------|
| **Trigger** | Pick verification fails, shelf quantity mismatch, or outbound quality issue identified during fulfillment. |
| **Related Aggregate** | Customer Order Fulfillment |
| **Business Meaning** | Warehouse cannot fulfill as planned without resolution. Inventory accuracy or product quality issue requires manager intervention per BP-20. |
| **Consumers** | Business Process — warehouse manager exception workflow *(UC-026)*; Operational Alert read model; Count Variance Adjudication domain service *(DS-016)* *(if shelf mismatch)* |

---

### DE-045 — MultiLocationFulfillmentPlanCreated

| Aspect | Detail |
|--------|--------|
| **Trigger** | Multi-Location Fulfillment Allocation domain service assigns order lines to multiple ship-from locations. |
| **Related Aggregate** | Customer Order Fulfillment |
| **Business Meaning** | Single customer order will be fulfilled from more than one warehouse to satisfy total quantity when no single location has sufficient ATP. |
| **Consumers** | Inventory Reservation Coordination domain service *(DS-002)* *(reservations at each location)*; Business Process — multi-shipment customer communication *(UC-048)* |

---

## Domain 5: Network Transfer

---

### DE-046 — TransferRequested

| Aspect | Detail |
|--------|--------|
| **Trigger** | Inter-location stock transfer request submitted specifying source, destination, product, and quantity in Stock Transfer aggregate. |
| **Related Aggregate** | Stock Transfer |
| **Business Meaning** | A location requests stock from another location to resolve local shortage or rebalance network before new procurement per BR-011. |
| **Consumers** | Transfer Capacity Evaluation domain service *(DS-006)*; Business Process — operations director approval workflow *(UC-032)*; Operational Alert read model *(pending approval)* |

---

### DE-047 — TransferApproved

| Aspect | Detail |
|--------|--------|
| **Trigger** | Transfer request passes approval after source minimum and safety stock validation. |
| **Related Aggregate** | Stock Transfer |
| **Business Meaning** | Network redistribution authorized. Source location can spare quantity while maintaining its own service level per BR-012. |
| **Consumers** | Business Process — source warehouse dispatch notification; Read Model — transfer pipeline |

---

### DE-048 — TransferRejected

| Aspect | Detail |
|--------|--------|
| **Trigger** | Transfer request denied — source cannot spare quantity or business justification insufficient. |
| **Related Aggregate** | Stock Transfer |
| **Business Meaning** | Proposed redistribution will not proceed. Requestor must pursue alternative (procurement, different source) to resolve shortage. |
| **Consumers** | Business Process — requestor notification; Read Model — transfer request history |

---

### DE-049 — TransferDispatched

| Aspect | Detail |
|--------|--------|
| **Trigger** | Stock physically leaves source location; Stock Transfer aggregate records dispatch and creates in-transit state. |
| **Related Aggregate** | Stock Transfer |
| **Business Meaning** | Source Stock Position reduced. Quantity is in transit — excluded from both source and destination ATP until receipt confirmed. |
| **Consumers** | Stock Position aggregate *(source deduction)*; In-Transit Stock tracking; Inventory Movement Record read model; Network Availability Evaluation domain service *(DS-004)* |

---

### DE-050 — TransferReceived

| Aspect | Detail |
|--------|--------|
| **Trigger** | Destination location confirms receipt of transferred stock in Stock Transfer aggregate. |
| **Related Aggregate** | Stock Transfer |
| **Business Meaning** | Network redistribution complete. Destination Stock Position increased; in-transit state closed. Lot/batch preserved for traceable products per BR-017. |
| **Consumers** | Stock Position aggregate *(destination StockReceived)*; Inventory Movement Record read model; Stock Status Classification domain service *(DS-017)* |

---

### DE-051 — InTransitStockDelayed

| Aspect | Detail |
|--------|--------|
| **Trigger** | Expected transfer receipt date passes without confirmation, or carrier reports delay. |
| **Related Aggregate** | Stock Transfer |
| **Business Meaning** | Pipeline stock is delayed en route. Destination location fulfillment and replenishment plans may be impacted. |
| **Consumers** | Operational Alert read model *(transfer exception)*; Business Process — destination warehouse and requestor notification *(UC-047)* |

---

## Domain 6: Inventory Control & Accuracy

---

### DE-052 — CycleCountScheduled

| Aspect | Detail |
|--------|--------|
| **Trigger** | Cycle Count assignment created with product, location, and counter for scheduled count date. |
| **Related Aggregate** | Cycle Count |
| **Business Meaning** | Partial physical verification scheduled. Class A products scheduled at highest frequency per BR-032. |
| **Consumers** | Business Process — counter assignment notification; Read Model — count schedule calendar |

---

### DE-053 — CycleCountCompleted

| Aspect | Detail |
|--------|--------|
| **Trigger** | Counter submits physical count result under blind count protocol in Cycle Count aggregate. |
| **Related Aggregate** | Cycle Count |
| **Business Meaning** | Physical quantity recorded without counter having seen system expected quantity per BR-018. Variance calculated at submission. |
| **Consumers** | Count Variance Adjudication domain service *(DS-016)*; Read Model — count completion log |

---

### DE-054 — CountVarianceIdentified

| Aspect | Detail |
|--------|--------|
| **Trigger** | Physical count differs from system quantity — variance recorded in Inventory Adjustment Case aggregate. |
| **Related Aggregate** | Inventory Adjustment Case |
| **Business Meaning** | Inventory accuracy discrepancy discovered. Investigation required before any Stock Position adjustment per BR-022. |
| **Consumers** | Count Variance Adjudication domain service *(DS-016)*; Business Process — warehouse manager investigation workflow *(UC-016)*; Read Model — accuracy metrics |

---

### DE-055 — CountVarianceApproved

| Aspect | Detail |
|--------|--------|
| **Trigger** | Independent approver (distinct from counter) authorizes count variance after investigation in Inventory Adjustment Case aggregate. |
| **Related Aggregate** | Inventory Adjustment Case |
| **Business Meaning** | Variance investigation complete and adjustment authorized. Segregation of duties confirmed per BR-019. |
| **Consumers** | Adjustment Governance Evaluation domain service *(DS-015)*; Stock Adjustment creation; Business Process — adjustment processing notification |

---

### DE-056 — PhysicalInventoryCountStarted

| Aspect | Detail |
|--------|--------|
| **Trigger** | Wall-to-wall count begins at a location with freeze imposed in Physical Inventory Count aggregate. |
| **Related Aggregate** | Physical Inventory Count |
| **Business Meaning** | Full location snapshot count initiated. All movements suspended per BR-024. Authoritative accuracy baseline in progress. |
| **Consumers** | LocationFreezeImposed *(DE-007)*; Business Process — count team mobilization; Read Model — count event status |

---

### DE-057 — PhysicalInventoryCountCertified

| Aspect | Detail |
|--------|--------|
| **Trigger** | Full count completed, all variances identified, and count event certified in Physical Inventory Count aggregate. |
| **Related Aggregate** | Physical Inventory Count |
| **Business Meaning** | Wall-to-wall count authoritative and complete. Location freeze may be released. Variances routed for investigation. |
| **Consumers** | LocationFreezeReleased *(DE-008)*; Read Model — inventory accuracy baseline; Business Process — finance notification for reconciliation |

---

### DE-058 — AdjustmentSubmitted

| Aspect | Detail |
|--------|--------|
| **Trigger** | Stock adjustment or write-off proposal submitted with reason code in Inventory Adjustment Case aggregate. |
| **Related Aggregate** | Inventory Adjustment Case |
| **Business Meaning** | Correction or removal request recorded pending governance evaluation. Reason code captured per BR-020. |
| **Consumers** | Adjustment Governance Evaluation domain service *(DS-015)*; Segregation of Duties Validation domain service *(DS-023)*; Operational Alert read model *(pending approval)* |

---

### DE-059 — AdjustmentApproved

| Aspect | Detail |
|--------|--------|
| **Trigger** | Independent approver authorizes adjustment or write-off after threshold and SoD validation. |
| **Related Aggregate** | Inventory Adjustment Case |
| **Business Meaning** | Governance requirements satisfied. Stock Position mutation authorized per BR-021, BR-023. |
| **Consumers** | Stock Position aggregate *(StockAdjusted or StockWrittenOff)*; Audit Trail Record read model |

---

### DE-060 — AdjustmentRejected

| Aspect | Detail |
|--------|--------|
| **Trigger** | Adjustment or write-off denied due to insufficient evidence, SoD violation, or policy threshold breach. |
| **Related Aggregate** | Inventory Adjustment Case |
| **Business Meaning** | Proposed inventory change will not take effect. Initiator must revise or provide additional justification. |
| **Consumers** | Business Process — initiator notification; Read Model — adjustment case history |

---

## Domain 7: Returns Management

---

### DE-061 — ReturnAuthorizationIssued

| Aspect | Detail |
|--------|--------|
| **Trigger** | Return Authorization (RMA) created and linked to original customer order in Customer Return Case aggregate. |
| **Related Aggregate** | Customer Return Case |
| **Business Meaning** | Customer is authorized to return specified products. Warehouse notified to expect inbound return per BR-025. |
| **Consumers** | Business Process — customer return instructions; Business Process — receiving clerk advance notice |

---

### DE-062 — ReturnAuthorizationExpired

| Aspect | Detail |
|--------|--------|
| **Trigger** | RMA passes expiration date without Customer Return receipt. |
| **Related Aggregate** | Customer Return Case |
| **Business Meaning** | Return window closed. Warehouse must not accept goods against expired authorization. |
| **Consumers** | Business Process — customer expiration notification; Return Eligibility domain service *(DS-020)* |

---

### DE-063 — CustomerReturnReceived

| Aspect | Detail |
|--------|--------|
| **Trigger** | Returned goods arrive and pass verification against RMA in Customer Return Case aggregate. |
| **Related Aggregate** | Customer Return Case |
| **Business Meaning** | Authorized return physically received. Inspection and disposition workflow initiated per BR-004, BR-025. |
| **Consumers** | Return Eligibility and Disposition Routing domain service *(DS-020)*; Business Process — inspection task assignment |

---

### DE-064 — ReturnInspected

| Aspect | Detail |
|--------|--------|
| **Trigger** | Condition assessment completed on returned goods in Customer Return Case aggregate. |
| **Related Aggregate** | Customer Return Case |
| **Business Meaning** | Resale quality of returned goods evaluated. Disposition decision (restock, quarantine, write-off) authorized to proceed per BR-026. |
| **Consumers** | Return Eligibility and Disposition Routing domain service *(DS-020)* |

---

### DE-065 — ReturnRestocked

| Aspect | Detail |
|--------|--------|
| **Trigger** | Disposition decision confirms returned goods meet resale standards; restock applied to Stock Position. |
| **Related Aggregate** | Customer Return Case |
| **Business Meaning** | Qualifying returned goods re-enter sellable inventory. ATP increased at receiving location per BR-026. |
| **Consumers** | Stock Position aggregate *(StockReceived)*; Inventory Movement Record read model |

---

### DE-066 — ReturnQuarantined

| Aspect | Detail |
|--------|--------|
| **Trigger** | Returned goods placed under quarantine hold pending further quality investigation. |
| **Related Aggregate** | Customer Return Case |
| **Business Meaning** | Returns requiring further evaluation excluded from sellable ATP per BR-013, BR-026. |
| **Consumers** | Stock Position aggregate *(QuarantineHoldApplied)*; Business Process — quality team investigation |

---

### DE-067 — ReturnWrittenOff

| Aspect | Detail |
|--------|--------|
| **Trigger** | Returned goods deemed non-resalable; write-off authorized from Customer Return Case. |
| **Related Aggregate** | Customer Return Case |
| **Business Meaning** | Damaged or defective returns permanently removed from inventory value per BR-023, BR-026. |
| **Consumers** | Stock Position aggregate *(StockWrittenOff)*; Inventory Valuation Reconciliation domain service *(DS-022)* |

---

## Domain 8: Commercial & Monitoring

---

### DE-068 — LowStockThresholdBreached

| Aspect | Detail |
|--------|--------|
| **Trigger** | Stock Position ATP falls to or below Stock Policy reorder level; detected by Stock Status Classification domain service. |
| **Related Aggregate** | Stock Position *(state change)* / Stock Policy *(threshold reference)* |
| **Business Meaning** | Replenishment action required same business day per BR-009. Product at location needs purchasing or network transfer review. |
| **Consumers** | Low-Stock Alert Evaluation domain service *(DS-018)*; Replenishment Recommendation domain service *(DS-005)*; Operational Alert read model; Business Process — purchasing manager notification *(UC-028, UC-047)* |

---

### DE-069 — OutOfStockDetected

| Aspect | Detail |
|--------|--------|
| **Trigger** | Stock Position ATP reaches zero for a product at a location. |
| **Related Aggregate** | Stock Position |
| **Business Meaning** | No quantity available to promise to new customers at this location. Existing reservations may still be fulfilled from on-hand. Stockout condition active. |
| **Consumers** | Low-Stock Alert Evaluation domain service *(DS-018)*; Operational Alert read model; Read Model — stockout report *(UC-037)*; Business Process — urgent replenishment escalation |

---

### DE-070 — OverstockDetected

| Aspect | Detail |
|--------|--------|
| **Trigger** | Stock Position on-hand exceeds Stock Policy maximum level. |
| **Related Aggregate** | Stock Position / Stock Policy |
| **Business Meaning** | Excess capital tied in inventory above policy maximum. Network rebalancing or purchasing freeze may be warranted. |
| **Consumers** | Network Rebalancing Analysis domain service *(DS-007)*; Read Model — overstock report; Business Process — inventory controller review |

---

### DE-071 — ReplenishmentRecommended

| Aspect | Detail |
|--------|--------|
| **Trigger** | Replenishment Recommendation domain service produces action recommendation after threshold breach and network evaluation. |
| **Related Aggregate** | *(Cross-cutting — no single aggregate)* |
| **Business Meaning** | System recommends purchase requisition, transfer request, or no action based on policy, network availability, and product status. |
| **Consumers** | Business Process — buyer or regional manager action *(UC-029, UC-031)*; Read Model — replenishment suggestion log |

---

### DE-072 — PromotionalReadinessGapIdentified

| Aspect | Detail |
|--------|--------|
| **Trigger** | Promotional Readiness Evaluation domain service detects insufficient ring-fenced stock before campaign deadline. |
| **Related Aggregate** | Promotional Stock Allocation |
| **Business Meaning** | Campaign or launch commitment at risk — allocated quantity insufficient for planned demand per BR-029. |
| **Consumers** | Operational Alert read model; Business Process — marketing and purchasing notification *(UC-040, UC-047)* |

---

### DE-073 — NetworkImbalanceDetected

| Aspect | Detail |
|--------|--------|
| **Trigger** | Network Rebalancing Analysis domain service identifies simultaneous stockout risk at one location and excess at another for the same product. |
| **Related Aggregate** | *(Cross-cutting)* |
| **Business Meaning** | Network holds sufficient total stock but maldistributed. Transfer-before-buy opportunity exists per BR-011. |
| **Consumers** | Business Process — operations director rebalancing review *(UC-034)*; Replenishment Recommendation domain service *(DS-005)* |

---

## Domain 9: Financial & Governance

---

### DE-074 — InventoryMovementRecorded

| Aspect | Detail |
|--------|--------|
| **Trigger** | Any Stock Position quantity or status mutation completes (receipt, shipment, adjustment, transfer, reservation, hold). |
| **Related Aggregate** | Stock Position |
| **Business Meaning** | Immutable operational fact recorded — what changed, where, how much, by whom, and why. Complete movement history per BO-19 audit trail objective. |
| **Consumers** | Inventory Movement Record read model *(UC-042)*; Audit Trail Record read model; Read Model — movement reports *(UC-037)* |

---

### DE-075 — AuditTrailRecorded

| Aspect | Detail |
|--------|--------|
| **Trigger** | Material governed change completes with before/after state, user identity, and approval chain captured. |
| **Related Aggregate** | *(Cross-cutting — emitted by governed aggregates)* |
| **Business Meaning** | Governance-grade evidence of who changed what and when. Supports compliance, fraud investigation, and control testing per BP-32. |
| **Consumers** | Audit Trail Record read model *(UC-043)*; Business Process — internal auditor review *(UC-041)* |

---

### DE-076 — InventoryValuationSnapshotPrepared

| Aspect | Detail |
|--------|--------|
| **Trigger** | Inventory Valuation Reconciliation domain service completes period-end valuation summary. |
| **Related Aggregate** | *(Read model — Inventory Valuation Snapshot)* |
| **Business Meaning** | Point-in-time owned inventory value prepared for finance reconciliation against general ledger per BO-18. |
| **Consumers** | Business Process — finance manager month-end close *(UC-039)*; Read Model — executive KPI dashboard *(UC-038)* |

---

### DE-077 — ValuationVarianceIdentified

| Aspect | Detail |
|--------|--------|
| **Trigger** | Inventory Valuation Snapshot variance against general ledger exceeds tolerance threshold. |
| **Related Aggregate** | *(Read model)* |
| **Business Meaning** | Operational inventory records and financial ledger are misaligned. Investigation and reconciliation required before month-end close. |
| **Consumers** | Business Process — finance and inventory controller joint investigation *(UC-039)*; Read Model — reconciliation status dashboard |

---

### DE-078 — SegregationOfDutiesViolationDetected

| Aspect | Detail |
|--------|--------|
| **Trigger** | Segregation of Duties Validation domain service blocks action due to conflicting user roles (e.g., counter attempting to approve own count). |
| **Related Aggregate** | User Account |
| **Business Meaning** | Proposed action violates accountability controls. Prevents fraud and undetected error per BR-019, BR-021. |
| **Consumers** | Business Process — security/administrator notification; Audit Trail Record read model; Business Process — internal auditor alert *(UC-041)* |

---

### DE-079 — UserAccountProvisioned

| Aspect | Detail |
|--------|--------|
| **Trigger** | New User Account created with initial role assignments in User Account aggregate. |
| **Related Aggregate** | User Account |
| **Business Meaning** | Individual authorized to perform inventory operations within assigned role and location scope. |
| **Consumers** | Segregation of Duties Validation domain service *(DS-023)*; Business Process — onboarding notification *(UC-044)* |

---

### DE-080 — RoleAssignmentChanged

| Aspect | Detail |
|--------|--------|
| **Trigger** | User role or location scope added, modified, or removed in User Account aggregate. |
| **Related Aggregate** | User Account |
| **Business Meaning** | User's operational authority has changed. SoD compliance re-evaluated for new role combination. |
| **Consumers** | Segregation of Duties Validation domain service *(DS-023)*; Audit Trail Record read model; Business Process — access change notification *(UC-045)* |

---

### DE-081 — ThreeWayMatchExceptionRaised

| Aspect | Detail |
|--------|--------|
| **Trigger** | PO, receipt, and invoice lines fail to match within tolerance during Three-Way Match Evaluation. |
| **Related Aggregate** | Supplier Invoice |
| **Business Meaning** | Payment blocked pending resolution of quantity or price discrepancy. Financial control intervention required per BR-008. |
| **Consumers** | Business Process — finance and purchasing exception workflow; Read Model — match exception dashboard |

---

## Event Flow — Core Business Lifecycles

### Inbound Supply Lifecycle

```
PurchaseOrderPlaced → InboundDeliveryScheduled → GoodsReceiptVerified
    → [ReceiptDiscrepancyRecorded → ReceiptDiscrepancyResolved]
    → PutAwayCompleted → StockReceived → InventoryMovementRecorded
    → SupplierInvoiceReceived → ThreeWayMatchCompleted
```

### Order Fulfillment Lifecycle

```
OrderAvailabilityConfirmed → CustomerOrderConfirmed → StockReserved
    → PickVerified → ShipmentDispatched → StockShipped → InventoryMovementRecorded
    → [PartialFulfillmentCompleted → BackorderRecorded → BackorderFulfilled]
```

### Inventory Accuracy Lifecycle

```
CycleCountScheduled → CycleCountCompleted → CountVarianceIdentified
    → CountVarianceApproved → AdjustmentSubmitted → AdjustmentApproved
    → StockAdjusted → InventoryMovementRecorded → AuditTrailRecorded
```

### Network Transfer Lifecycle

```
TransferRequested → TransferApproved → TransferDispatched → TransferReceived
    → StockReceived (destination) → InventoryMovementRecorded
```

---

## Event-to-Aggregate Origin Matrix

| Aggregate | Events Raised |
|-----------|---------------|
| Product Catalog | DE-001, DE-002, DE-003 |
| Inventory Location | DE-004, DE-005, DE-006 |
| Physical Inventory Count | DE-007, DE-008, DE-056, DE-057 |
| Inventory Governance | DE-009, DE-010 |
| Stock Position | DE-011 – DE-018, DE-022, DE-068 – DE-070, DE-074 |
| Stock Policy | DE-019 |
| Promotional Stock Allocation | DE-020, DE-021, DE-072 |
| Purchase Requisition | DE-023 – DE-025 |
| Purchase Order | DE-026 – DE-029 |
| Goods Receipt | DE-030 – DE-033 |
| Supplier Invoice | DE-034, DE-035, DE-081 |
| Customer Order Fulfillment | DE-036 – DE-045, DE-042, DE-043 |
| Stock Transfer | DE-046 – DE-051 |
| Cycle Count | DE-052, DE-053 |
| Inventory Adjustment Case | DE-054, DE-055, DE-058 – DE-060 |
| Customer Return Case | DE-061 – DE-067 |
| User Account | DE-078 – DE-080 |
| Cross-cutting / Domain Services | DE-071, DE-073, DE-075 – DE-077 |

---

## Event-to-Use Case Traceability

| Use Case | Key Domain Events |
|----------|-------------------|
| UC-008 Receive and Verify Supplier Goods | DE-030, DE-031, DE-033 |
| UC-010 Perform Stock Put-Away | DE-033, DE-011 |
| UC-014 Perform Cycle Count | DE-052, DE-053, DE-054 |
| UC-015 Conduct Full Physical Inventory Count | DE-056, DE-057, DE-007, DE-008 |
| UC-016 Investigate and Approve Count Variances | DE-054, DE-055, DE-058, DE-059 |
| UC-021 Confirm Order Availability | DE-036 |
| UC-022 Reserve Inventory for Confirmed Orders | DE-037, DE-012 |
| UC-024 Pick, Pack, and Ship Orders | DE-039, DE-040, DE-014 |
| UC-025 Handle Partial Fulfillment and Backorders | DE-041, DE-042, DE-043 |
| UC-028 Review Low-Stock Alerts | DE-068, DE-069, DE-071 |
| UC-031 Request Inter-Location Transfer | DE-046, DE-047, DE-048 |
| UC-033 Execute Inter-Location Transfer | DE-049, DE-050 |
| UC-035 Authorize Customer Returns | DE-061 |
| UC-036 Receive and Disposition Returns | DE-063 – DE-067 |
| UC-039 Reconcile Inventory Valuation | DE-076, DE-077, DE-035 |
| UC-040 Confirm Promotional Readiness | DE-072, DE-020 |
| UC-042 View Movement History | DE-074 |
| UC-043 Query Audit Trail | DE-075 |

---

## Excluded from Domain Events

| Occurrence | Treatment | Rationale |
|------------|-----------|-----------|
| User clicks "Search" on inventory screen | UI interaction | No business state change |
| Report query executed | Read operation | Queries do not change domain state |
| Validation failure (business rule rejected) | Rejection response | Nothing happened — state unchanged |
| Scheduled job timer fired | Infrastructure | Timer is not a business event; the resulting state change emits the event |
| Email delivery confirmed | Infrastructure | Notification delivery is not inventory domain concern |

---

## Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Domain Expert | | | |
| DDD Architect | | | |
| Senior Business Analyst | | | |
| Solution Architect | | | |

---

*End of Domain Events*

*Document ID: SRS-DM-006 | Version 1.0 | July 5, 2026*
