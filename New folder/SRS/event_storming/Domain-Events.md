# Domain Events — Event Storming Catalog
## Inventory Management System

---

## Document Information

| Attribute | Detail |
|-----------|--------|
| **Document ID** | SRS-ES-001 |
| **Document Title** | Domain Events — Event Storming Catalog |
| **Version** | 1.0 |
| **Status** | Draft |
| **Document Owner** | Domain Expert |
| **Source Documents** | SRS-DM-001 (Domain Entities), SRS-DM-003 (Domain Aggregates), SRS-DM-006 (Domain Events), SRS-UC-001 (Use Case Catalog), SRS-UC-002 (Main Flows) |
| **Date** | July 6, 2026 |
| **Scope** | Business domain events only — no message brokers, integration technology, or UI interactions |

### Purpose

This document identifies **all domain events** for the Inventory Management System as derived from the domain model and use cases. Each event records a meaningful business fact expressed in **past tense**. Events are raised by aggregates after successful command execution and describe **what happened**, not what should happen next.

### Conventions

| Element | Convention |
|---------|------------|
| **Event ID** | `DE-xxx` — sequential identifier |
| **Event Name** | PascalCase past tense (e.g., `StockReserved`) |
| **Aggregate** | The consistency boundary that raises the event |
| **Triggering Command** | Imperative business command that caused the state change |
| **Resulting Business State** | Authoritative post-condition after the event is applied |

### Event Catalog Summary

| Domain Area | Event IDs | Count |
|-------------|-----------|-------|
| Catalog & Network | DE-001 – DE-010 | 10 |
| Inventory Balance | DE-011 – DE-022 | 12 |
| Procurement & Inbound | DE-023 – DE-035 | 13 |
| Order Fulfillment | DE-036 – DE-045 | 10 |
| Network Transfer | DE-046 – DE-051 | 6 |
| Inventory Control & Accuracy | DE-052 – DE-060 | 9 |
| Returns Management | DE-061 – DE-067 | 7 |
| Commercial & Monitoring | DE-068 – DE-073 | 6 |
| Financial & Governance | DE-074 – DE-081 | 8 |
| **Total** | | **81** |

---

## Domain 1: Catalog & Network

---

### DE-001 — ProductRegistered

| Field | Detail |
|-------|--------|
| **Event Name** | ProductRegistered |
| **Business Meaning** | The organization has introduced a new SKU into the trusted product catalog. The product is eligible for stock policy assignment and, when active, for procurement and fulfillment referencing. |
| **Aggregate Responsible** | Product Catalog |
| **Triggering Command** | `RegisterProduct` *(UC-001, UC-046)* |
| **Resulting Business State** | Product exists with unique SKU, mandatory attributes, and initial lifecycle status (typically active). Product is searchable across the network and eligible for downstream configuration. |

---

### DE-002 — ProductStatusChanged

| Field | Detail |
|-------|--------|
| **Event Name** | ProductStatusChanged |
| **Business Meaning** | The commercial availability of a SKU has changed. Discontinued status prohibits new procurement and reservations; inactive status restricts new customer commitments. |
| **Aggregate Responsible** | Product Catalog |
| **Triggering Command** | `ChangeProductStatus` *(UC-001)* |
| **Resulting Business State** | Product lifecycle status is updated with prior status, new status, and attribution recorded. Downstream eligibility rules (procurement, reservation, replenishment) reflect the new status. |

---

### DE-003 — ProductABCClassificationAssigned

| Field | Detail |
|-------|--------|
| **Event Name** | ProductABCClassificationAssigned |
| **Business Meaning** | Operational priority for the SKU has been set. Class A products receive highest count frequency, monitoring intensity, and alert priority. |
| **Aggregate Responsible** | Product Catalog |
| **Triggering Command** | `AssignABCClassification` *(UC-004)* |
| **Resulting Business State** | Product carries an ABC class (A, B, or C) with effective date. Cycle count scheduling and low-stock alert prioritization use the new classification. |

---

### DE-004 — InventoryLocationActivated

| Field | Detail |
|-------|--------|
| **Event Name** | InventoryLocationActivated |
| **Business Meaning** | A location is authorized to receive, hold, fulfill, and transact inventory. Stock positions may be established and operational workflows enabled. |
| **Aggregate Responsible** | Inventory Location |
| **Triggering Command** | `ActivateInventoryLocation` *(UC-002, UC-046)* |
| **Resulting Business State** | Location operational status is active. Opening balances (if required) are recorded. Location accepts receipts, reservations, fulfillments, and transfers. |

---

### DE-005 — InventoryLocationDeactivated

| Field | Detail |
|-------|--------|
| **Event Name** | InventoryLocationDeactivated |
| **Business Meaning** | A location is no longer authorized for new inventory activity. Existing stock must have been cleared or dispositioned before deactivation. |
| **Aggregate Responsible** | Inventory Location |
| **Triggering Command** | `DeactivateInventoryLocation` *(UC-002)* |
| **Resulting Business State** | Location operational status is deactivated or closing. New receipts, reservations, and fulfillments are blocked. Historical records remain intact. |

---

### DE-006 — StoragePositionConfigured

| Field | Detail |
|-------|--------|
| **Event Name** | StoragePositionConfigured |
| **Business Meaning** | A findable physical address within a location is available for put-away placement and pick path guidance. |
| **Aggregate Responsible** | Inventory Location |
| **Triggering Command** | `ConfigureStoragePosition` *(UC-002)* |
| **Resulting Business State** | Storage position (zone, aisle, bin) exists within the location hierarchy and is available for put-away and pick operations. |

---

### DE-007 — LocationFreezeImposed

| Field | Detail |
|-------|--------|
| **Event Name** | LocationFreezeImposed |
| **Business Meaning** | All receiving, shipping, transfers, and adjustments at the location are suspended until the wall-to-wall count is certified complete. Ensures a stable snapshot for accurate counting. |
| **Aggregate Responsible** | Physical Inventory Count |
| **Triggering Command** | `StartPhysicalInventoryCount` *(UC-015)* |
| **Resulting Business State** | Location is frozen. Receiving, shipping, transfers, and non-count adjustments are blocked. Count teams operate against a stable inventory snapshot. |

---

### DE-008 — LocationFreezeReleased

| Field | Detail |
|-------|--------|
| **Event Name** | LocationFreezeReleased |
| **Business Meaning** | Normal inventory operations may resume at the location. Count variances have been identified and routed for investigation. |
| **Aggregate Responsible** | Physical Inventory Count |
| **Triggering Command** | `CertifyPhysicalInventoryCount` *(UC-015)* |
| **Resulting Business State** | Location freeze is lifted. Normal receiving, shipping, transfers, and adjustments may resume. Count event is certified with variances routed to adjustment cases. |

---

### DE-009 — GovernancePolicyPublished

| Field | Detail |
|-------|--------|
| **Event Name** | GovernancePolicyPublished |
| **Business Meaning** | Organization-wide inventory control parameters have changed. All subsequent transactions must evaluate against the new effective policy. |
| **Aggregate Responsible** | Inventory Governance |
| **Triggering Command** | `PublishGovernancePolicy` *(UC-005)* |
| **Resulting Business State** | New governance policy version is effective with approval thresholds, tolerances, and exception rules. Subsequent adjustments, receipts, and matches evaluate against this policy. |

---

### DE-010 — ReasonCodeRetired

| Field | Detail |
|-------|--------|
| **Event Name** | ReasonCodeRetired |
| **Business Meaning** | A categorized exception reason is no longer valid for new transactions. Historical records retain prior reason code attributions unchanged. |
| **Aggregate Responsible** | Inventory Governance |
| **Triggering Command** | `RetireReasonCode` *(UC-005)* |
| **Resulting Business State** | Reason code status is retired and removed from active selection lists. Historical transactions retain original reason code references. |

---

## Domain 2: Inventory Balance

---

### DE-011 — StockReceived

| Field | Detail |
|-------|--------|
| **Event Name** | StockReceived |
| **Business Meaning** | Verified inbound stock is now physically placed and recorded as on-hand inventory. ATP increases correspondingly unless quarantine or ownership rules apply. |
| **Aggregate Responsible** | Stock Position |
| **Triggering Command** | `IncreaseOnHandQuantity` *(reacts to `CompletePutAway`, `ConfirmTransferReceipt`, `RestockReturnedGoods`)* |
| **Resulting Business State** | On-hand quantity increased at product-location. ATP recalculated. Stock status indicator updated. Movement history appended. |

---

### DE-012 — StockReserved

| Field | Detail |
|-------|--------|
| **Event Name** | StockReserved |
| **Business Meaning** | Quantity is operationally committed to a customer order and is no longer available for new sales promises. Prevents double-allocation. |
| **Aggregate Responsible** | Stock Position |
| **Triggering Command** | `ReserveStock` *(UC-022)* |
| **Resulting Business State** | Reserved quantity increased; ATP decreased by reserved amount. Reservation linked to customer order line. On-hand unchanged. |

---

### DE-013 — StockReservationReleased

| Field | Detail |
|-------|--------|
| **Event Name** | StockReservationReleased |
| **Business Meaning** | Previously committed stock is returned to the available-to-promise pool and may be promised to other customers or orders. |
| **Aggregate Responsible** | Stock Position |
| **Triggering Command** | `ReleaseReservation` *(UC-023)* |
| **Resulting Business State** | Reserved quantity decreased; ATP restored. Order reservation cleared or reduced. On-hand unchanged. |

---

### DE-014 — StockShipped

| Field | Detail |
|-------|--------|
| **Event Name** | StockShipped |
| **Business Meaning** | Physical stock has left the location for customer delivery. Inventory record reflects deduction only after verified pick. |
| **Aggregate Responsible** | Stock Position |
| **Triggering Command** | `DeductShippedQuantity` *(reacts to `DispatchShipment` — UC-024)* |
| **Resulting Business State** | On-hand and reserved quantities decreased. ATP unchanged (already reserved). Lot/batch attribution recorded for traceable products. |

---

### DE-015 — StockAdjusted

| Field | Detail |
|-------|--------|
| **Event Name** | StockAdjusted |
| **Business Meaning** | Recorded inventory has been aligned with physical reality following investigation and authorization. Distinct from write-off — adjustment is a correction, not permanent value removal. |
| **Aggregate Responsible** | Stock Position |
| **Triggering Command** | `ApplyApprovedAdjustment` *(reacts to `ApproveAdjustment` — UC-017)* |
| **Resulting Business State** | On-hand quantity corrected with mandatory reason code. ATP recalculated. Adjustment case finalized. Movement and audit records created. |

---

### DE-016 — StockWrittenOff

| Field | Detail |
|-------|--------|
| **Event Name** | StockWrittenOff |
| **Business Meaning** | Inventory value has been formally removed for damaged, obsolete, expired, or lost goods. Terminal event — quantity cannot be restored without new receipt. |
| **Aggregate Responsible** | Stock Position |
| **Triggering Command** | `ApplyApprovedWriteOff` *(reacts to `AuthorizeWriteOff` — UC-018)* |
| **Resulting Business State** | On-hand quantity permanently reduced. ATP decreased. Write-off case closed. Valuation impact recorded for finance reconciliation. |

---

### DE-017 — QuarantineHoldApplied

| Field | Detail |
|-------|--------|
| **Event Name** | QuarantineHoldApplied |
| **Business Meaning** | Stock is physically present but not sellable due to quality investigation, regulatory restriction, recall, or customs hold. ATP reduced accordingly. |
| **Aggregate Responsible** | Stock Position |
| **Triggering Command** | `ApplyQuarantineHold` *(UC-019)* |
| **Resulting Business State** | Quarantine hold active on specified quantity. Held quantity excluded from ATP. Hold reason and attribution recorded. |

---

### DE-018 — QuarantineHoldReleased

| Field | Detail |
|-------|--------|
| **Event Name** | QuarantineHoldReleased |
| **Business Meaning** | Previously held stock is cleared for sale or fulfillment. Bonded inventory cleared for domestic commerce. |
| **Aggregate Responsible** | Stock Position |
| **Triggering Command** | `ReleaseQuarantineHold` *(UC-019)* |
| **Resulting Business State** | Quarantine hold cleared. Quantity restored to sellable ATP (or routed to disposition). Hold closure reason recorded. |

---

### DE-019 — StockPolicyThresholdChanged

| Field | Detail |
|-------|--------|
| **Event Name** | StockPolicyThresholdChanged |
| **Business Meaning** | Replenishment and alert rules for a product at a location have been recalibrated. Future low-stock detection uses new thresholds. |
| **Aggregate Responsible** | Stock Policy |
| **Triggering Command** | `UpdateStockPolicyThresholds` *(UC-003)* |
| **Resulting Business State** | Reorder level, minimum, safety stock, and/or maximum thresholds saved with effective date. Prior values retained as immutable history. Monitoring rules updated. |

---

### DE-020 — PromotionalStockAllocated

| Field | Detail |
|-------|--------|
| **Event Name** | PromotionalStockAllocated |
| **Business Meaning** | Defined inventory quantity is reserved for promotional or launch use and excluded from general ATP for non-approved orders. |
| **Aggregate Responsible** | Promotional Stock Allocation |
| **Triggering Command** | `AllocatePromotionalStock` *(UC-040)* |
| **Resulting Business State** | Campaign allocation active with ring-fenced quantity. General ATP reduced by allocated amount. Campaign period and channel designation recorded. |

---

### DE-021 — PromotionalAllocationReleased

| Field | Detail |
|-------|--------|
| **Event Name** | PromotionalAllocationReleased |
| **Business Meaning** | Unconsumed promotional stock is returned to the general sellable pool. Campaign commitment period has concluded. |
| **Aggregate Responsible** | Promotional Stock Allocation |
| **Triggering Command** | `ReleasePromotionalAllocation` *(UC-040)* |
| **Resulting Business State** | Allocation inactive or closed. Ring-fenced quantity returned to general ATP. Campaign performance data available for review. |

---

### DE-022 — ConsignmentOwnershipTransferred

| Field | Detail |
|-------|--------|
| **Event Name** | ConsignmentOwnershipTransferred |
| **Business Meaning** | Stock previously held under consignment classification becomes owned inventory for valuation and financial recording upon defined consumption or sale event. |
| **Aggregate Responsible** | Stock Position |
| **Triggering Command** | `TransferConsignmentOwnership` *(reacts to consignment consumption/sale — UC-039)* |
| **Resulting Business State** | Ownership classification changed from consignment to owned. Valuation treatment updated. Financial reconciliation triggered. |

---

## Domain 3: Procurement & Inbound

---

### DE-023 — PurchaseRequisitionSubmitted

| Field | Detail |
|-------|--------|
| **Event Name** | PurchaseRequisitionSubmitted |
| **Business Meaning** | The organization has identified a procurement need for specific products at a target location, pending internal approval before commercial PO creation. |
| **Aggregate Responsible** | Purchase Requisition |
| **Triggering Command** | `SubmitPurchaseRequisition` *(UC-029)* |
| **Resulting Business State** | Requisition status is submitted and pending approval. Lines reference active products, quantities, and target location. Linked to triggering low-stock alert when applicable. |

---

### DE-024 — PurchaseRequisitionApproved

| Field | Detail |
|-------|--------|
| **Event Name** | PurchaseRequisitionApproved |
| **Business Meaning** | Internal authorization to proceed with supplier procurement is granted. Requisition is eligible for conversion to Purchase Order. |
| **Aggregate Responsible** | Purchase Requisition |
| **Triggering Command** | `ApprovePurchaseRequisition` *(UC-029)* |
| **Resulting Business State** | Requisition status is approved. Network availability and policy validation completed. Eligible for PO conversion by buyer. |

---

### DE-025 — PurchaseRequisitionRejected

| Field | Detail |
|-------|--------|
| **Event Name** | PurchaseRequisitionRejected |
| **Business Meaning** | Procurement request denied. Network redistribution or other alternative should be pursued instead of new purchase. |
| **Aggregate Responsible** | Purchase Requisition |
| **Triggering Command** | `RejectPurchaseRequisition` *(UC-029)* |
| **Resulting Business State** | Requisition status is rejected with documented reason. No PO may be created from this requisition. Requestor notified to pursue alternatives. |

---

### DE-026 — PurchaseOrderPlaced

| Field | Detail |
|-------|--------|
| **Event Name** | PurchaseOrderPlaced |
| **Business Meaning** | The organization has committed to purchase specified goods from a supplier. Inbound receipt is authorized upon delivery. |
| **Aggregate Responsible** | Purchase Order |
| **Triggering Command** | `PlacePurchaseOrder` *(UC-006)* |
| **Resulting Business State** | PO status is open/authorized with supplier, product lines, quantities, delivery terms, and receiving location. Inbound receipt permitted against PO lines. |

---

### DE-027 — PurchaseOrderCancelled

| Field | Detail |
|-------|--------|
| **Event Name** | PurchaseOrderCancelled |
| **Business Meaning** | Commercial commitment to supplier is withdrawn. No further receipts authorized against cancelled PO lines. |
| **Aggregate Responsible** | Purchase Order |
| **Triggering Command** | `CancelPurchaseOrder` *(UC-006)* |
| **Resulting Business State** | PO status is cancelled. Expected inbound deliveries cancelled. Open receipt lines blocked. Supplier and buyer notified. |

---

### DE-028 — InboundDeliveryScheduled

| Field | Detail |
|-------|--------|
| **Event Name** | InboundDeliveryScheduled |
| **Business Meaning** | Receiving operations and replenishment planners are informed when and what quantity to expect, supporting dock preparation and inbound visibility. |
| **Aggregate Responsible** | Purchase Order |
| **Triggering Command** | `ScheduleInboundDelivery` *(UC-007)* |
| **Resulting Business State** | Expected Inbound Delivery recorded with arrival date, quantity, and PO line association. Visible on inbound supply calendar. |

---

### DE-029 — InboundDeliveryDelayed

| Field | Detail |
|-------|--------|
| **Event Name** | InboundDeliveryDelayed |
| **Business Meaning** | Anticipated inbound supply will arrive later than planned. Replenishment timelines and fulfillment promises may be affected. |
| **Aggregate Responsible** | Purchase Order |
| **Triggering Command** | `RecordInboundDelay` *(UC-030, UC-047)* |
| **Resulting Business State** | Expected arrival date updated or delay flag set. Inbound supply status reflects late delivery. Operational alert raised for responsible actors. |

---

### DE-030 — GoodsReceiptVerified

| Field | Detail |
|-------|--------|
| **Event Name** | GoodsReceiptVerified |
| **Business Meaning** | The business has confirmed what actually arrived at the dock matches authorized expectation. Stock is not yet available — put-away must follow. |
| **Aggregate Responsible** | Goods Receipt |
| **Triggering Command** | `VerifyGoodsReceipt` *(UC-008, UC-011)* |
| **Resulting Business State** | Receipt status is verified with accepted quantities, product identity, and condition confirmed. Lot/batch and shelf-life captured where required. Stock staged for put-away — not yet in ATP. |

---

### DE-031 — ReceiptDiscrepancyRecorded

| Field | Detail |
|-------|--------|
| **Event Name** | ReceiptDiscrepancyRecorded |
| **Business Meaning** | Short shipment, over-shipment, wrong item, damage, or shelf-life non-compliance captured at point of receipt when evidence exists. |
| **Aggregate Responsible** | Goods Receipt |
| **Triggering Command** | `RecordReceiptDiscrepancy` *(UC-009)* |
| **Resulting Business State** | Discrepancy documented with type, variance quantity, reason code, and evidence. Accepted quantities separated from unresolved variance. Supplier claim workflow initiated. |

---

### DE-032 — ReceiptDiscrepancyResolved

| Field | Detail |
|-------|--------|
| **Event Name** | ReceiptDiscrepancyResolved |
| **Business Meaning** | Receipt exception has been closed with documented outcome. Accepted quantities may proceed to put-away; rejected quantities will not enter inventory. |
| **Aggregate Responsible** | Goods Receipt |
| **Triggering Command** | `ResolveReceiptDiscrepancy` *(UC-009)* |
| **Resulting Business State** | Discrepancy status is resolved (partial acceptance, rejection, or supplier claim completed). Receipt record finalized. Three-way match evaluation updated. |

---

### DE-033 — PutAwayCompleted

| Field | Detail |
|-------|--------|
| **Event Name** | PutAwayCompleted |
| **Business Meaning** | Inbound stock has transitioned from receiving dock to operational storage. Triggers availability activation — stock may now enter sellable ATP. |
| **Aggregate Responsible** | Goods Receipt |
| **Triggering Command** | `CompletePutAway` *(UC-010)* |
| **Resulting Business State** | Put-away confirmed with storage position assignment. Receipt workflow complete. Cross-aggregate notification to increase Stock Position on-hand and ATP. |

---

### DE-034 — SupplierInvoiceReceived

| Field | Detail |
|-------|--------|
| **Event Name** | SupplierInvoiceReceived |
| **Business Meaning** | Supplier has invoiced for goods supplied. Three-way match evaluation against PO and receipt must proceed before payment authorization. |
| **Aggregate Responsible** | Supplier Invoice |
| **Triggering Command** | `RecordSupplierInvoice` *(UC-039)* |
| **Resulting Business State** | Invoice recorded with line details linked to PO and receipt references. Match status pending. Payment blocked until match completes. |

---

### DE-035 — ThreeWayMatchCompleted

| Field | Detail |
|-------|--------|
| **Event Name** | ThreeWayMatchCompleted |
| **Business Meaning** | Financial control confirmed — payment for received, authorized goods may proceed. Closes the procurement-to-payment accountability loop. |
| **Aggregate Responsible** | Supplier Invoice |
| **Triggering Command** | `CompleteThreeWayMatch` *(UC-039)* |
| **Resulting Business State** | PO, receipt, and invoice lines agree within tolerance. Match status is complete. Payment authorization enabled for finance. |

---

## Domain 4: Order Fulfillment

---

### DE-036 — OrderAvailabilityConfirmed

| Field | Detail |
|-------|--------|
| **Event Name** | OrderAvailabilityConfirmed |
| **Business Meaning** | The business has verified that available-to-promise stock can support the order (fully or partially) before commercial commitment. |
| **Aggregate Responsible** | Customer Order Fulfillment |
| **Triggering Command** | `ConfirmOrderAvailability` *(UC-013, UC-021)* |
| **Resulting Business State** | Order availability check recorded with ATP validation result per line. Order eligible for confirmation if availability sufficient. No reservation yet applied. |

---

### DE-037 — CustomerOrderConfirmed

| Field | Detail |
|-------|--------|
| **Event Name** | CustomerOrderConfirmed |
| **Business Meaning** | Commercial commitment to fulfill the order is established. Reservation of stock must follow immediately. |
| **Aggregate Responsible** | Customer Order Fulfillment |
| **Triggering Command** | `ConfirmCustomerOrder` *(UC-022)* |
| **Resulting Business State** | Order status is confirmed. Reservation workflow initiated. Order released to fulfillment queue. |

---

### DE-038 — CustomerOrderCancelled

| Field | Detail |
|-------|--------|
| **Event Name** | CustomerOrderCancelled |
| **Business Meaning** | Commercial commitment withdrawn. Reserved stock must be released back to ATP. |
| **Aggregate Responsible** | Customer Order Fulfillment |
| **Triggering Command** | `CancelCustomerOrder` *(UC-023)* |
| **Resulting Business State** | Order or order line status is cancelled. Reservation release triggered. Fulfillment workflow terminated for cancelled lines. |

---

### DE-039 — PickVerified

| Field | Detail |
|-------|--------|
| **Event Name** | PickVerified |
| **Business Meaning** | Physical pick matches order requirements. Shipment is authorized to proceed. Lot/batch captured for traceable products. |
| **Aggregate Responsible** | Customer Order Fulfillment |
| **Triggering Command** | `VerifyPick` *(UC-024)* |
| **Resulting Business State** | Pick lines verified against order. Fulfillment execution status updated. Shipment authorized. Rotation policy (FIFO/FEFO) applied. |

---

### DE-040 — ShipmentDispatched

| Field | Detail |
|-------|--------|
| **Event Name** | ShipmentDispatched |
| **Business Meaning** | Order goods have left the warehouse. Inventory deduction and reservation consumption triggered. Delivery promise activated for customer. |
| **Aggregate Responsible** | Customer Order Fulfillment |
| **Triggering Command** | `DispatchShipment` *(UC-024)* |
| **Resulting Business State** | Shipment recorded with carrier handoff. Stock deduction triggered on Stock Position. Order fulfillment status updated. Customer notification eligible. |

---

### DE-041 — PartialFulfillmentCompleted

| Field | Detail |
|-------|--------|
| **Event Name** | PartialFulfillmentCompleted |
| **Business Meaning** | Customer receives available quantity now; unfulfilled portion handled separately via backorder with customer acknowledgment. |
| **Aggregate Responsible** | Customer Order Fulfillment |
| **Triggering Command** | `CompletePartialFulfillment` *(UC-025)* |
| **Resulting Business State** | Order line decomposed into fulfilled and backordered quantities. Shipment dispatched for available portion. Remainder routed to backorder workflow. |

---

### DE-042 — BackorderRecorded

| Field | Detail |
|-------|--------|
| **Event Name** | BackorderRecorded |
| **Business Meaning** | Customer has agreed to wait for remaining quantity. Mutual commercial commitment — not an internal note. |
| **Aggregate Responsible** | Customer Order Fulfillment |
| **Triggering Command** | `RecordBackorder` *(UC-025)* |
| **Resulting Business State** | Backorder active with customer acknowledgment. Unfulfilled quantity tracked. Priority replenishment eligible. Customer confirmation recorded. |

---

### DE-043 — BackorderFulfilled

| Field | Detail |
|-------|--------|
| **Event Name** | BackorderFulfilled |
| **Business Meaning** | Delayed customer commitment is now being executed. Backorder closed for fulfilled quantity. |
| **Aggregate Responsible** | Customer Order Fulfillment |
| **Triggering Command** | `FulfillBackorder` *(UC-025)* |
| **Resulting Business State** | Backorder quantity reserved and fulfilled. Backorder reduced or closed. Customer notification of backorder shipment eligible. |

---

### DE-044 — FulfillmentExceptionRaised

| Field | Detail |
|-------|--------|
| **Event Name** | FulfillmentExceptionRaised |
| **Business Meaning** | Warehouse cannot fulfill as planned without resolution. Inventory accuracy or product quality issue requires manager intervention. |
| **Aggregate Responsible** | Customer Order Fulfillment |
| **Triggering Command** | `RaiseFulfillmentException` *(UC-026)* |
| **Resulting Business State** | Fulfillment execution blocked with exception reason. Operational alert raised. Manager investigation workflow initiated. Shipment prevented until resolved. |

---

### DE-045 — MultiLocationFulfillmentPlanCreated

| Field | Detail |
|-------|--------|
| **Event Name** | MultiLocationFulfillmentPlanCreated |
| **Business Meaning** | Single customer order will be fulfilled from more than one warehouse to satisfy total quantity when no single location has sufficient ATP. |
| **Aggregate Responsible** | Customer Order Fulfillment |
| **Triggering Command** | `CreateMultiLocationFulfillmentPlan` *(UC-048)* |
| **Resulting Business State** | Order lines assigned to multiple ship-from locations. Reservation workflow initiated at each location. Multi-shipment customer communication eligible. |

---

## Domain 5: Network Transfer

---

### DE-046 — TransferRequested

| Field | Detail |
|-------|--------|
| **Event Name** | TransferRequested |
| **Business Meaning** | A location requests stock from another location to resolve local shortage or rebalance network before new procurement. |
| **Aggregate Responsible** | Stock Transfer |
| **Triggering Command** | `RequestStockTransfer` *(UC-031)* |
| **Resulting Business State** | Transfer request status is pending approval. Source, destination, product, and quantity documented. Network availability evaluation completed. |

---

### DE-047 — TransferApproved

| Field | Detail |
|-------|--------|
| **Event Name** | TransferApproved |
| **Business Meaning** | Network redistribution authorized. Source location can spare quantity while maintaining its own service level. |
| **Aggregate Responsible** | Stock Transfer |
| **Triggering Command** | `ApproveTransferRequest` *(UC-032)* |
| **Resulting Business State** | Transfer status is approved. Source minimum and safety stock validation passed. Source warehouse dispatch notification eligible. |

---

### DE-048 — TransferRejected

| Field | Detail |
|-------|--------|
| **Event Name** | TransferRejected |
| **Business Meaning** | Proposed redistribution will not proceed. Requestor must pursue alternative (procurement, different source) to resolve shortage. |
| **Aggregate Responsible** | Stock Transfer |
| **Triggering Command** | `RejectTransferRequest` *(UC-032)* |
| **Resulting Business State** | Transfer status is rejected with documented reason. No stock movement authorized. Requestor notified. |

---

### DE-049 — TransferDispatched

| Field | Detail |
|-------|--------|
| **Event Name** | TransferDispatched |
| **Business Meaning** | Source Stock Position reduced. Quantity is in transit — excluded from both source and destination ATP until receipt confirmed. |
| **Aggregate Responsible** | Stock Transfer |
| **Triggering Command** | `DispatchTransfer` *(UC-033)* |
| **Resulting Business State** | Transfer status is in-transit. Source on-hand reduced. In-Transit Stock entity active. Lot/batch preserved for traceable products. |

---

### DE-050 — TransferReceived

| Field | Detail |
|-------|--------|
| **Event Name** | TransferReceived |
| **Business Meaning** | Network redistribution complete. Destination Stock Position increased; in-transit state closed. Lot/batch preserved for traceable products. |
| **Aggregate Responsible** | Stock Transfer |
| **Triggering Command** | `ConfirmTransferReceipt` *(UC-033)* |
| **Resulting Business State** | Transfer status is received/complete. In-transit state closed. Destination Stock Position increase triggered. Transfer history complete. |

---

### DE-051 — InTransitStockDelayed

| Field | Detail |
|-------|--------|
| **Event Name** | InTransitStockDelayed |
| **Business Meaning** | Pipeline stock is delayed en route. Destination location fulfillment and replenishment plans may be impacted. |
| **Aggregate Responsible** | Stock Transfer |
| **Triggering Command** | `RecordTransferDelay` *(UC-030, UC-047)* |
| **Resulting Business State** | In-transit delay flag set. Expected receipt date updated. Operational alert raised. Destination and requestor notification eligible. |

---

## Domain 6: Inventory Control & Accuracy

---

### DE-052 — CycleCountScheduled

| Field | Detail |
|-------|--------|
| **Event Name** | CycleCountScheduled |
| **Business Meaning** | Partial physical verification scheduled. Class A products scheduled at highest frequency. |
| **Aggregate Responsible** | Cycle Count |
| **Triggering Command** | `ScheduleCycleCount` *(UC-014)* |
| **Resulting Business State** | Cycle count assignment created with product, location, counter, and scheduled date. Counter notification eligible. |

---

### DE-053 — CycleCountCompleted

| Field | Detail |
|-------|--------|
| **Event Name** | CycleCountCompleted |
| **Business Meaning** | Physical quantity recorded without counter having seen system expected quantity. Variance calculated at submission. |
| **Aggregate Responsible** | Cycle Count |
| **Triggering Command** | `SubmitCycleCountResult` *(UC-014)* |
| **Resulting Business State** | Count result recorded under blind count protocol. Variance calculated against system quantity. Count status complete. Variance investigation initiated if discrepancy exists. |

---

### DE-054 — CountVarianceIdentified

| Field | Detail |
|-------|--------|
| **Event Name** | CountVarianceIdentified |
| **Business Meaning** | Inventory accuracy discrepancy discovered. Investigation required before any Stock Position adjustment. |
| **Aggregate Responsible** | Inventory Adjustment Case |
| **Triggering Command** | `IdentifyCountVariance` *(reacts to `SubmitCycleCountResult` or physical count — UC-016)* |
| **Resulting Business State** | Variance case opened with quantity difference documented. Investigation workflow pending. Stock Position unchanged pending approval. |

---

### DE-055 — CountVarianceApproved

| Field | Detail |
|-------|--------|
| **Event Name** | CountVarianceApproved |
| **Business Meaning** | Variance investigation complete and adjustment authorized. Segregation of duties confirmed. |
| **Aggregate Responsible** | Inventory Adjustment Case |
| **Triggering Command** | `ApproveCountVariance` *(UC-016)* |
| **Resulting Business State** | Variance approved by independent approver (distinct from counter). Adjustment submission authorized. Segregation of duties validated. |

---

### DE-056 — PhysicalInventoryCountStarted

| Field | Detail |
|-------|--------|
| **Event Name** | PhysicalInventoryCountStarted |
| **Business Meaning** | Full location snapshot count initiated. All movements suspended. Authoritative accuracy baseline in progress. |
| **Aggregate Responsible** | Physical Inventory Count |
| **Triggering Command** | `StartPhysicalInventoryCount` *(UC-015)* |
| **Resulting Business State** | Wall-to-wall count in progress. Location freeze imposed. Count teams mobilized. All concurrent movements suspended. |

---

### DE-057 — PhysicalInventoryCountCertified

| Field | Detail |
|-------|--------|
| **Event Name** | PhysicalInventoryCountCertified |
| **Business Meaning** | Wall-to-wall count authoritative and complete. Location freeze may be released. Variances routed for investigation. |
| **Aggregate Responsible** | Physical Inventory Count |
| **Triggering Command** | `CertifyPhysicalInventoryCount` *(UC-015)* |
| **Resulting Business State** | Count event certified complete. All variances identified and routed. Location freeze release eligible. Finance reconciliation notification eligible. |

---

### DE-058 — AdjustmentSubmitted

| Field | Detail |
|-------|--------|
| **Event Name** | AdjustmentSubmitted |
| **Business Meaning** | Correction or removal request recorded pending governance evaluation. Reason code captured. |
| **Aggregate Responsible** | Inventory Adjustment Case |
| **Triggering Command** | `SubmitAdjustment` *(UC-017, UC-018)* |
| **Resulting Business State** | Adjustment case status is pending approval. Reason code and quantity documented. Governance evaluation and SoD validation initiated. Stock Position unchanged. |

---

### DE-059 — AdjustmentApproved

| Field | Detail |
|-------|--------|
| **Event Name** | AdjustmentApproved |
| **Business Meaning** | Governance requirements satisfied. Stock Position mutation authorized. |
| **Aggregate Responsible** | Inventory Adjustment Case |
| **Triggering Command** | `ApproveAdjustment` *(UC-017, UC-018)* |
| **Resulting Business State** | Adjustment or write-off approved. Stock Position mutation triggered (`StockAdjusted` or `StockWrittenOff`). Audit trail recorded. Case finalized. |

---

### DE-060 — AdjustmentRejected

| Field | Detail |
|-------|--------|
| **Event Name** | AdjustmentRejected |
| **Business Meaning** | Proposed inventory change will not take effect. Initiator must revise or provide additional justification. |
| **Aggregate Responsible** | Inventory Adjustment Case |
| **Triggering Command** | `RejectAdjustment` *(UC-017, UC-018)* |
| **Resulting Business State** | Adjustment case status is rejected. Stock Position unchanged. Initiator notified with rejection reason. |

---

## Domain 7: Returns Management

---

### DE-061 — ReturnAuthorizationIssued

| Field | Detail |
|-------|--------|
| **Event Name** | ReturnAuthorizationIssued |
| **Business Meaning** | Customer is authorized to return specified products. Warehouse notified to expect inbound return. |
| **Aggregate Responsible** | Customer Return Case |
| **Triggering Command** | `IssueReturnAuthorization` *(UC-035)* |
| **Resulting Business State** | RMA active and linked to original customer order. Return window and product lines documented. Warehouse advance notice eligible. |

---

### DE-062 — ReturnAuthorizationExpired

| Field | Detail |
|-------|--------|
| **Event Name** | ReturnAuthorizationExpired |
| **Business Meaning** | Return window closed. Warehouse must not accept goods against expired authorization. |
| **Aggregate Responsible** | Customer Return Case |
| **Triggering Command** | `ExpireReturnAuthorization` *(system policy — UC-035)* |
| **Resulting Business State** | RMA status is expired. Warehouse receipt blocked against this authorization. Customer expiration notification eligible. |

---

### DE-063 — CustomerReturnReceived

| Field | Detail |
|-------|--------|
| **Event Name** | CustomerReturnReceived |
| **Business Meaning** | Authorized return physically received. Inspection and disposition workflow initiated. |
| **Aggregate Responsible** | Customer Return Case |
| **Triggering Command** | `ReceiveCustomerReturn` *(UC-011, UC-036)* |
| **Resulting Business State** | Return receipt verified against RMA. Inspection task assigned. Stock not yet in sellable ATP. |

---

### DE-064 — ReturnInspected

| Field | Detail |
|-------|--------|
| **Event Name** | ReturnInspected |
| **Business Meaning** | Resale quality of returned goods evaluated. Disposition decision (restock, quarantine, write-off) authorized to proceed. |
| **Aggregate Responsible** | Customer Return Case |
| **Triggering Command** | `InspectReturnedGoods` *(UC-036)* |
| **Resulting Business State** | Condition grade recorded. Disposition decision pending or ready for execution. Inspection attribution documented. |

---

### DE-065 — ReturnRestocked

| Field | Detail |
|-------|--------|
| **Event Name** | ReturnRestocked |
| **Business Meaning** | Qualifying returned goods re-enter sellable inventory. ATP increased at receiving location. |
| **Aggregate Responsible** | Customer Return Case |
| **Triggering Command** | `RestockReturnedGoods` *(UC-036)* |
| **Resulting Business State** | Disposition is restock. Stock Position increase triggered. Return case progressing toward closure. ATP increased at receiving location. |

---

### DE-066 — ReturnQuarantined

| Field | Detail |
|-------|--------|
| **Event Name** | ReturnQuarantined |
| **Business Meaning** | Returns requiring further evaluation excluded from sellable ATP. |
| **Aggregate Responsible** | Customer Return Case |
| **Triggering Command** | `QuarantineReturnedGoods` *(UC-036)* |
| **Resulting Business State** | Disposition is quarantine. Quarantine hold applied on Stock Position. Quality investigation workflow initiated. |

---

### DE-067 — ReturnWrittenOff

| Field | Detail |
|-------|--------|
| **Event Name** | ReturnWrittenOff |
| **Business Meaning** | Damaged or defective returns permanently removed from inventory value. |
| **Aggregate Responsible** | Customer Return Case |
| **Triggering Command** | `WriteOffReturnedGoods` *(UC-036)* |
| **Resulting Business State** | Disposition is write-off. Stock Position write-off triggered. Return case closed. Valuation impact recorded. |

---

## Domain 8: Commercial & Monitoring

---

### DE-068 — LowStockThresholdBreached

| Field | Detail |
|-------|--------|
| **Event Name** | LowStockThresholdBreached |
| **Business Meaning** | Replenishment action required same business day. Product at location needs purchasing or network transfer review. |
| **Aggregate Responsible** | Stock Position *(state change)* / Stock Policy *(threshold reference)* |
| **Triggering Command** | `EvaluateStockStatus` *(reacts to quantity change — UC-012, UC-028)* |
| **Resulting Business State** | ATP at or below reorder level. Stock status indicator is low-stock. Replenishment recommendation and alert workflows triggered. |

---

### DE-069 — OutOfStockDetected

| Field | Detail |
|-------|--------|
| **Event Name** | OutOfStockDetected |
| **Business Meaning** | No quantity available to promise to new customers at this location. Existing reservations may still be fulfilled from on-hand. Stockout condition active. |
| **Aggregate Responsible** | Stock Position |
| **Triggering Command** | `EvaluateStockStatus` *(reacts to ATP reaching zero — UC-012, UC-028)* |
| **Resulting Business State** | ATP is zero. Stock status indicator is out-of-stock. Urgent replenishment escalation and operational alert triggered. |

---

### DE-070 — OverstockDetected

| Field | Detail |
|-------|--------|
| **Event Name** | OverstockDetected |
| **Business Meaning** | Excess capital tied in inventory above policy maximum. Network rebalancing or purchasing freeze may be warranted. |
| **Aggregate Responsible** | Stock Position / Stock Policy |
| **Triggering Command** | `EvaluateStockStatus` *(reacts to on-hand exceeding maximum — UC-012, UC-020)* |
| **Resulting Business State** | On-hand exceeds policy maximum. Stock status indicator is overstock. Network rebalancing analysis and inventory controller review eligible. |

---

### DE-071 — ReplenishmentRecommended

| Field | Detail |
|-------|--------|
| **Event Name** | ReplenishmentRecommended |
| **Business Meaning** | System recommends purchase requisition, transfer request, or no action based on policy, network availability, and product status. |
| **Aggregate Responsible** | *(Cross-cutting — domain service outcome)* |
| **Triggering Command** | `RecommendReplenishmentAction` *(UC-028, UC-029, UC-034)* |
| **Resulting Business State** | Replenishment recommendation recorded with suggested action (purchase, transfer, or hold). Buyer or regional manager action eligible. |

---

### DE-072 — PromotionalReadinessGapIdentified

| Field | Detail |
|-------|--------|
| **Event Name** | PromotionalReadinessGapIdentified |
| **Business Meaning** | Campaign or launch commitment at risk — allocated quantity insufficient for planned demand. |
| **Aggregate Responsible** | Promotional Stock Allocation |
| **Triggering Command** | `EvaluatePromotionalReadiness` *(UC-040, UC-047)* |
| **Resulting Business State** | Readiness gap documented. Ring-fenced quantity below campaign requirement. Marketing and purchasing notification eligible. |

---

### DE-073 — NetworkImbalanceDetected

| Field | Detail |
|-------|--------|
| **Event Name** | NetworkImbalanceDetected |
| **Business Meaning** | Network holds sufficient total stock but maldistributed. Transfer-before-buy opportunity exists. |
| **Aggregate Responsible** | *(Cross-cutting — domain service outcome)* |
| **Triggering Command** | `AnalyzeNetworkBalance` *(UC-034)* |
| **Resulting Business State** | Imbalance documented with source excess and destination shortage for same product. Transfer recommendation eligible. Operations director review triggered. |

---

## Domain 9: Financial & Governance

---

### DE-074 — InventoryMovementRecorded

| Field | Detail |
|-------|--------|
| **Event Name** | InventoryMovementRecorded |
| **Business Meaning** | Immutable operational fact recorded — what changed, where, how much, by whom, and why. Complete movement history maintained. |
| **Aggregate Responsible** | Stock Position |
| **Triggering Command** | *(Automatic — raised after any quantity mutation command)* |
| **Resulting Business State** | Movement record appended with product, location, quantity delta, reason, user, and timestamp. Movement history queryable for investigation. |

---

### DE-075 — AuditTrailRecorded

| Field | Detail |
|-------|--------|
| **Event Name** | AuditTrailRecorded |
| **Business Meaning** | Governance-grade evidence of who changed what and when. Supports compliance, fraud investigation, and control testing. |
| **Aggregate Responsible** | *(Cross-cutting — emitted by governed aggregates)* |
| **Triggering Command** | *(Automatic — raised after governed state change)* |
| **Resulting Business State** | Audit record with before/after state, user identity, approval chain, and timestamp. Available for auditor query. |

---

### DE-076 — InventoryValuationSnapshotPrepared

| Field | Detail |
|-------|--------|
| **Event Name** | InventoryValuationSnapshotPrepared |
| **Business Meaning** | Point-in-time owned inventory value prepared for finance reconciliation against general ledger. |
| **Aggregate Responsible** | *(Read model — Inventory Valuation Snapshot)* |
| **Triggering Command** | `PrepareValuationSnapshot` *(UC-039)* |
| **Resulting Business State** | Period-end valuation summary available. Owned inventory value calculated. Finance month-end close workflow eligible. |

---

### DE-077 — ValuationVarianceIdentified

| Field | Detail |
|-------|--------|
| **Event Name** | ValuationVarianceIdentified |
| **Business Meaning** | Operational inventory records and financial ledger are misaligned. Investigation and reconciliation required before month-end close. |
| **Aggregate Responsible** | *(Read model)* |
| **Triggering Command** | `ReconcileInventoryValuation` *(UC-039)* |
| **Resulting Business State** | Variance against general ledger documented and exceeds tolerance. Joint finance and inventory investigation triggered. Reconciliation status dashboard updated. |

---

### DE-078 — SegregationOfDutiesViolationDetected

| Field | Detail |
|-------|--------|
| **Event Name** | SegregationOfDutiesViolationDetected |
| **Business Meaning** | Proposed action violates accountability controls. Prevents fraud and undetected error. |
| **Aggregate Responsible** | User Account |
| **Triggering Command** | *(Blocked command — e.g., `ApproveCountVariance`, `ApproveAdjustment`, `AssignRole` — UC-045)* |
| **Resulting Business State** | Command rejected. No domain state change on target aggregate. Security violation logged. Administrator and auditor alert eligible. |

---

### DE-079 — UserAccountProvisioned

| Field | Detail |
|-------|--------|
| **Event Name** | UserAccountProvisioned |
| **Business Meaning** | Individual authorized to perform inventory operations within assigned role and location scope. |
| **Aggregate Responsible** | User Account |
| **Triggering Command** | `ProvisionUserAccount` *(UC-044)* |
| **Resulting Business State** | User account active with initial role assignments and location scope. SoD rules evaluated at assignment. Onboarding notification eligible. |

---

### DE-080 — RoleAssignmentChanged

| Field | Detail |
|-------|--------|
| **Event Name** | RoleAssignmentChanged |
| **Business Meaning** | User's operational authority has changed. SoD compliance re-evaluated for new role combination. |
| **Aggregate Responsible** | User Account |
| **Triggering Command** | `ChangeRoleAssignment` *(UC-044, UC-045)* |
| **Resulting Business State** | Role or location scope updated with effective dating. Prior assignments retained as history. SoD re-evaluation complete. Access change notification eligible. |

---

### DE-081 — ThreeWayMatchExceptionRaised

| Field | Detail |
|-------|--------|
| **Event Name** | ThreeWayMatchExceptionRaised |
| **Business Meaning** | Payment blocked pending resolution of quantity or price discrepancy. Financial control intervention required. |
| **Aggregate Responsible** | Supplier Invoice |
| **Triggering Command** | `EvaluateThreeWayMatch` *(UC-039)* |
| **Resulting Business State** | Match status is exception. Payment authorization blocked. Discrepancy documented for finance and purchasing resolution. |

---

## Event Flow — Core Business Lifecycles

### Inbound Supply

```
PlacePurchaseOrder → PurchaseOrderPlaced
ScheduleInboundDelivery → InboundDeliveryScheduled
VerifyGoodsReceipt → GoodsReceiptVerified
[RecordReceiptDiscrepancy → ReceiptDiscrepancyRecorded → ResolveReceiptDiscrepancy → ReceiptDiscrepancyResolved]
CompletePutAway → PutAwayCompleted → StockReceived → InventoryMovementRecorded
RecordSupplierInvoice → SupplierInvoiceReceived → CompleteThreeWayMatch → ThreeWayMatchCompleted
```

### Order Fulfillment

```
ConfirmOrderAvailability → OrderAvailabilityConfirmed
ConfirmCustomerOrder → CustomerOrderConfirmed → ReserveStock → StockReserved
VerifyPick → PickVerified
DispatchShipment → ShipmentDispatched → StockShipped → InventoryMovementRecorded
[CompletePartialFulfillment → PartialFulfillmentCompleted → RecordBackorder → BackorderRecorded → FulfillBackorder → BackorderFulfilled]
```

### Inventory Accuracy

```
ScheduleCycleCount → CycleCountScheduled
SubmitCycleCountResult → CycleCountCompleted → IdentifyCountVariance → CountVarianceIdentified
ApproveCountVariance → CountVarianceApproved
SubmitAdjustment → AdjustmentSubmitted → ApproveAdjustment → AdjustmentApproved
→ StockAdjusted → InventoryMovementRecorded → AuditTrailRecorded
```

### Network Transfer

```
RequestStockTransfer → TransferRequested
ApproveTransferRequest → TransferApproved
DispatchTransfer → TransferDispatched
ConfirmTransferReceipt → TransferReceived → StockReceived → InventoryMovementRecorded
```

### Returns

```
IssueReturnAuthorization → ReturnAuthorizationIssued
ReceiveCustomerReturn → CustomerReturnReceived
InspectReturnedGoods → ReturnInspected
[RestockReturnedGoods → ReturnRestocked | QuarantineReturnedGoods → ReturnQuarantined | WriteOffReturnedGoods → ReturnWrittenOff]
```

---

## Command-to-Event Traceability Matrix

| Command | Domain Event(s) Raised | Use Case |
|---------|------------------------|----------|
| `RegisterProduct` | ProductRegistered | UC-001 |
| `ChangeProductStatus` | ProductStatusChanged | UC-001 |
| `AssignABCClassification` | ProductABCClassificationAssigned | UC-004 |
| `ActivateInventoryLocation` | InventoryLocationActivated | UC-002 |
| `DeactivateInventoryLocation` | InventoryLocationDeactivated | UC-002 |
| `ConfigureStoragePosition` | StoragePositionConfigured | UC-002 |
| `StartPhysicalInventoryCount` | PhysicalInventoryCountStarted, LocationFreezeImposed | UC-015 |
| `CertifyPhysicalInventoryCount` | PhysicalInventoryCountCertified, LocationFreezeReleased | UC-015 |
| `PublishGovernancePolicy` | GovernancePolicyPublished | UC-005 |
| `RetireReasonCode` | ReasonCodeRetired | UC-005 |
| `UpdateStockPolicyThresholds` | StockPolicyThresholdChanged | UC-003 |
| `ReserveStock` | StockReserved | UC-022 |
| `ReleaseReservation` | StockReservationReleased | UC-023 |
| `ApplyQuarantineHold` | QuarantineHoldApplied | UC-019 |
| `ReleaseQuarantineHold` | QuarantineHoldReleased | UC-019 |
| `AllocatePromotionalStock` | PromotionalStockAllocated | UC-040 |
| `ReleasePromotionalAllocation` | PromotionalAllocationReleased | UC-040 |
| `SubmitPurchaseRequisition` | PurchaseRequisitionSubmitted | UC-029 |
| `ApprovePurchaseRequisition` | PurchaseRequisitionApproved | UC-029 |
| `RejectPurchaseRequisition` | PurchaseRequisitionRejected | UC-029 |
| `PlacePurchaseOrder` | PurchaseOrderPlaced | UC-006 |
| `CancelPurchaseOrder` | PurchaseOrderCancelled | UC-006 |
| `ScheduleInboundDelivery` | InboundDeliveryScheduled | UC-007 |
| `VerifyGoodsReceipt` | GoodsReceiptVerified | UC-008 |
| `RecordReceiptDiscrepancy` | ReceiptDiscrepancyRecorded | UC-009 |
| `ResolveReceiptDiscrepancy` | ReceiptDiscrepancyResolved | UC-009 |
| `CompletePutAway` | PutAwayCompleted → StockReceived | UC-010 |
| `ConfirmOrderAvailability` | OrderAvailabilityConfirmed | UC-021 |
| `ConfirmCustomerOrder` | CustomerOrderConfirmed | UC-022 |
| `CancelCustomerOrder` | CustomerOrderCancelled | UC-023 |
| `VerifyPick` | PickVerified | UC-024 |
| `DispatchShipment` | ShipmentDispatched → StockShipped | UC-024 |
| `RecordBackorder` | BackorderRecorded | UC-025 |
| `RequestStockTransfer` | TransferRequested | UC-031 |
| `ApproveTransferRequest` | TransferApproved | UC-032 |
| `DispatchTransfer` | TransferDispatched | UC-033 |
| `ConfirmTransferReceipt` | TransferReceived → StockReceived | UC-033 |
| `SubmitCycleCountResult` | CycleCountCompleted → CountVarianceIdentified | UC-014 |
| `ApproveCountVariance` | CountVarianceApproved | UC-016 |
| `ApproveAdjustment` | AdjustmentApproved → StockAdjusted / StockWrittenOff | UC-017, UC-018 |
| `IssueReturnAuthorization` | ReturnAuthorizationIssued | UC-035 |
| `ReceiveCustomerReturn` | CustomerReturnReceived | UC-036 |
| `InspectReturnedGoods` | ReturnInspected | UC-036 |
| `RestockReturnedGoods` | ReturnRestocked → StockReceived | UC-036 |
| `ProvisionUserAccount` | UserAccountProvisioned | UC-044 |
| `ChangeRoleAssignment` | RoleAssignmentChanged | UC-044 |

---

## Excluded from Domain Events

| Occurrence | Treatment | Rationale |
|------------|-----------|-----------|
| User searches or views inventory | Read operation | No business state change |
| Report query executed | Read model projection | Queries do not mutate domain state |
| Validation failure / business rule rejection | Rejection response | Nothing happened — state unchanged |
| Scheduled timer fired | Infrastructure signal | Timer is not a business event; resulting evaluation emits the business event |
| Email or notification delivered | Infrastructure | Delivery channel is not an inventory domain concern |

---

## Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Domain Expert | | | |
| DDD Architect | | | |
| Senior Business Analyst | | | |
| Solution Architect | | | |

---

*End of Domain Events — Event Storming Catalog*

*Document ID: SRS-ES-001 | Version 1.0 | July 6, 2026*
