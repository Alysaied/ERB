# Domain Commands
## Inventory Management System

---

## Document Information

| Attribute | Detail |
|-----------|--------|
| **Document ID** | SRS-ES-002 |
| **Document Title** | Domain Commands — Event Storming Catalog |
| **Version** | 1.0 |
| **Status** | Draft |
| **Document Owner** | Domain Expert |
| **Source Documents** | SRS-ES-001 (Domain Events), SRS-DM-003 (Domain Aggregates), SRS-UC-001 (Use Case Catalog), SRS-UC-002 (Main Flows) |
| **Date** | July 6, 2026 |
| **Scope** | Business commands that mutate domain state and initiate domain events — no queries, UI actions, or infrastructure signals |

### Purpose

This document identifies **all domain commands** that initiate domain events in the Inventory Management System. A command expresses a **business intention** — what the organization wants to happen. Commands are imperative, issued by a business actor (human or policy-driven evaluator), and target exactly one aggregate per transaction.

Commands that fail validation emit **no domain event** — the aggregate state remains unchanged. When segregation-of-duties rules block an action, `SegregationOfDutiesViolationDetected` (DE-078) is raised instead of the intended event.

### Command Naming Convention

Commands use **PascalCase imperative verbs**: `RegisterProduct`, `ReserveStock`, `ApproveTransferRequest`.

### Command Categories

| Category | Description |
|----------|-------------|
| **Actor Command** | Issued directly by a business role through a use case |
| **Policy Command** | Issued by a domain service when business rules or thresholds are evaluated |
| **Reaction Command** | Issued by an aggregate handler consuming a domain event from another aggregate |

### Command Catalog Summary

| Domain Area | Command IDs | Count |
|-------------|-------------|-------|
| Catalog & Network | CMD-001 – CMD-010 | 10 |
| Inventory Balance | CMD-011 – CMD-020 | 10 |
| Procurement & Inbound | CMD-021 – CMD-033 | 13 |
| Order Fulfillment | CMD-034 – CMD-044 | 11 |
| Network Transfer | CMD-045 – CMD-050 | 6 |
| Inventory Control & Accuracy | CMD-051 – CMD-060 | 10 |
| Returns Management | CMD-061 – CMD-067 | 7 |
| Commercial & Monitoring | CMD-068 – CMD-072 | 5 |
| Financial & Governance | CMD-073 – CMD-078 | 6 |
| **Total** | | **78** |

---

## Domain 1: Catalog & Network

---

### CMD-001 — RegisterProduct

| Field | Detail |
|-------|--------|
| **Command Name** | RegisterProduct |
| **Actor** | Inventory Controller |
| **Target Aggregate** | Product Catalog |
| **Business Purpose** | Introduce a new SKU into the trusted product catalog so all inventory operations reference a single authoritative product identity. |
| **Expected Domain Event(s)** | ProductRegistered (DE-001), AuditTrailRecorded (DE-075) |
| **Use Case** | UC-001, UC-046 |

---

### CMD-002 — ChangeProductStatus

| Field | Detail |
|-------|--------|
| **Command Name** | ChangeProductStatus |
| **Actor** | Inventory Controller |
| **Target Aggregate** | Product Catalog |
| **Business Purpose** | Change commercial availability of a SKU (active, inactive, discontinued) to control eligibility for procurement, replenishment, and customer commitments. |
| **Expected Domain Event(s)** | ProductStatusChanged (DE-002), AuditTrailRecorded (DE-075) |
| **Use Case** | UC-001 |

---

### CMD-003 — AssignABCClassification

| Field | Detail |
|-------|--------|
| **Command Name** | AssignABCClassification |
| **Actor** | Inventory Controller |
| **Target Aggregate** | Product Catalog |
| **Business Purpose** | Set operational priority for a SKU so count frequency, monitoring intensity, and alert priority reflect business importance. |
| **Expected Domain Event(s)** | ProductABCClassificationAssigned (DE-003), AuditTrailRecorded (DE-075) |
| **Use Case** | UC-004 |

---

### CMD-004 — ActivateInventoryLocation

| Field | Detail |
|-------|--------|
| **Command Name** | ActivateInventoryLocation |
| **Actor** | Inventory Controller |
| **Target Aggregate** | Inventory Location |
| **Business Purpose** | Authorize a location for inventory operations after go-live readiness, enabling receipts, stock holding, fulfillment, and transfers. |
| **Expected Domain Event(s)** | InventoryLocationActivated (DE-004), AuditTrailRecorded (DE-075) |
| **Use Case** | UC-002, UC-046 |

---

### CMD-005 — DeactivateInventoryLocation

| Field | Detail |
|-------|--------|
| **Command Name** | DeactivateInventoryLocation |
| **Actor** | Inventory Controller |
| **Target Aggregate** | Inventory Location |
| **Business Purpose** | Close a location to new inventory activity after stock disposition is complete or authorized. |
| **Expected Domain Event(s)** | InventoryLocationDeactivated (DE-005), AuditTrailRecorded (DE-075) |
| **Use Case** | UC-002 |

---

### CMD-006 — ConfigureStoragePosition

| Field | Detail |
|-------|--------|
| **Command Name** | ConfigureStoragePosition |
| **Actor** | Inventory Controller |
| **Target Aggregate** | Inventory Location |
| **Business Purpose** | Define or update a findable physical address (zone, aisle, bin) within a location for put-away and pick operations. |
| **Expected Domain Event(s)** | StoragePositionConfigured (DE-006) |
| **Use Case** | UC-002 |

---

### CMD-007 — PublishGovernancePolicy

| Field | Detail |
|-------|--------|
| **Command Name** | PublishGovernancePolicy |
| **Actor** | Inventory Controller |
| **Target Aggregate** | Inventory Governance |
| **Business Purpose** | Make a new or updated governance policy version effective, setting approval thresholds, tolerances, and exception rules for all subsequent transactions. |
| **Expected Domain Event(s)** | GovernancePolicyPublished (DE-009), AuditTrailRecorded (DE-075) |
| **Use Case** | UC-005 |

---

### CMD-008 — RetireReasonCode

| Field | Detail |
|-------|--------|
| **Command Name** | RetireReasonCode |
| **Actor** | Inventory Controller |
| **Target Aggregate** | Inventory Governance |
| **Business Purpose** | Remove an exception reason from active use while preserving historical attributions on past transactions. |
| **Expected Domain Event(s)** | ReasonCodeRetired (DE-010), AuditTrailRecorded (DE-075) |
| **Use Case** | UC-005 |

---

### CMD-009 — StartPhysicalInventoryCount

| Field | Detail |
|-------|--------|
| **Command Name** | StartPhysicalInventoryCount |
| **Actor** | Inventory Controller |
| **Target Aggregate** | Physical Inventory Count |
| **Business Purpose** | Initiate a wall-to-wall count at a location and impose operational freeze to ensure an accurate, stable inventory snapshot. |
| **Expected Domain Event(s)** | PhysicalInventoryCountStarted (DE-056), LocationFreezeImposed (DE-007) |
| **Use Case** | UC-015 |

---

### CMD-010 — CertifyPhysicalInventoryCount

| Field | Detail |
|-------|--------|
| **Command Name** | CertifyPhysicalInventoryCount |
| **Actor** | Inventory Controller |
| **Target Aggregate** | Physical Inventory Count |
| **Business Purpose** | Declare the wall-to-wall count complete and authoritative, route variances for investigation, and release the location freeze. |
| **Expected Domain Event(s)** | PhysicalInventoryCountCertified (DE-057), LocationFreezeReleased (DE-008), CountVarianceIdentified (DE-054) *per variance line* |
| **Use Case** | UC-015 |

---

## Domain 2: Inventory Balance

---

### CMD-011 — UpdateStockPolicyThresholds

| Field | Detail |
|-------|--------|
| **Command Name** | UpdateStockPolicyThresholds |
| **Actor** | Inventory Controller |
| **Target Aggregate** | Stock Policy |
| **Business Purpose** | Recalibrate reorder level, minimum, safety stock, and maximum thresholds to align replenishment and alerting with current service-level targets. |
| **Expected Domain Event(s)** | StockPolicyThresholdChanged (DE-019), AuditTrailRecorded (DE-075) |
| **Use Case** | UC-003 |

---

### CMD-012 — ReserveStock

| Field | Detail |
|-------|--------|
| **Command Name** | ReserveStock |
| **Actor** | Customer Service Representative *(or system on order confirmation)* |
| **Target Aggregate** | Stock Position |
| **Business Purpose** | Commit on-hand stock to a confirmed customer order and remove reserved quantity from ATP to prevent double-allocation. |
| **Expected Domain Event(s)** | StockReserved (DE-012), InventoryMovementRecorded (DE-074) |
| **Use Case** | UC-022 |

---

### CMD-013 — ReleaseReservation

| Field | Detail |
|-------|--------|
| **Command Name** | ReleaseReservation |
| **Actor** | Customer Service Representative |
| **Target Aggregate** | Stock Position |
| **Business Purpose** | Return previously committed stock to the ATP pool when an order or line is cancelled or amended. |
| **Expected Domain Event(s)** | StockReservationReleased (DE-013), InventoryMovementRecorded (DE-074), LowStockThresholdBreached (DE-068) *if ATP crosses reorder level* |
| **Use Case** | UC-023 |

---

### CMD-014 — ReceiveStock

| Field | Detail |
|-------|--------|
| **Command Name** | ReceiveStock |
| **Actor** | Stock Position *(reaction handler — triggered by inbound completion)* |
| **Target Aggregate** | Stock Position |
| **Business Purpose** | Record verified inbound quantity as on-hand inventory after put-away, transfer receipt, return restock, or opening balance establishment. |
| **Expected Domain Event(s)** | StockReceived (DE-011), InventoryMovementRecorded (DE-074), EvaluateStockStatus → LowStockThresholdBreached / OutOfStockDetected / OverstockDetected (DE-068 – DE-070) *as applicable* |
| **Triggered By** | CompletePutAway, ConfirmTransferReceipt, RestockReturnedGoods, EstablishOpeningBalances |
| **Use Case** | UC-010, UC-033, UC-036, UC-046 |

---

### CMD-015 — ShipStock

| Field | Detail |
|-------|--------|
| **Command Name** | ShipStock |
| **Actor** | Stock Position *(reaction handler — triggered by shipment dispatch)* |
| **Target Aggregate** | Stock Position |
| **Business Purpose** | Deduct on-hand and reserved quantities when verified goods leave the location for customer delivery. |
| **Expected Domain Event(s)** | StockShipped (DE-014), InventoryMovementRecorded (DE-074), ConsignmentOwnershipTransferred (DE-022) *if consignment*, EvaluateStockStatus → threshold events (DE-068 – DE-070) *as applicable* |
| **Triggered By** | DispatchShipment |
| **Use Case** | UC-024 |

---

### CMD-016 — ApplyApprovedAdjustment

| Field | Detail |
|-------|--------|
| **Command Name** | ApplyApprovedAdjustment |
| **Actor** | Stock Position *(reaction handler — triggered by adjustment approval)* |
| **Target Aggregate** | Stock Position |
| **Business Purpose** | Correct on-hand quantity to align recorded inventory with physical reality after investigation and authorization. |
| **Expected Domain Event(s)** | StockAdjusted (DE-015), InventoryMovementRecorded (DE-074), AuditTrailRecorded (DE-075) |
| **Triggered By** | ApproveAdjustment |
| **Use Case** | UC-017 |

---

### CMD-017 — ApplyApprovedWriteOff

| Field | Detail |
|-------|--------|
| **Command Name** | ApplyApprovedWriteOff |
| **Actor** | Stock Position *(reaction handler — triggered by write-off authorization)* |
| **Target Aggregate** | Stock Position |
| **Business Purpose** | Permanently remove damaged, obsolete, expired, or lost inventory from on-hand and valuation records. |
| **Expected Domain Event(s)** | StockWrittenOff (DE-016), InventoryMovementRecorded (DE-074), AuditTrailRecorded (DE-075) |
| **Triggered By** | ApproveAdjustment, WriteOffReturnedGoods |
| **Use Case** | UC-018, UC-036 |

---

### CMD-018 — ApplyQuarantineHold

| Field | Detail |
|-------|--------|
| **Command Name** | ApplyQuarantineHold |
| **Actor** | Warehouse Manager |
| **Target Aggregate** | Stock Position |
| **Business Purpose** | Exclude quantity from sellable ATP due to quality investigation, regulatory restriction, recall, or customs hold. |
| **Expected Domain Event(s)** | QuarantineHoldApplied (DE-017), InventoryMovementRecorded (DE-074) |
| **Use Case** | UC-019 |

---

### CMD-019 — ReleaseQuarantineHold

| Field | Detail |
|-------|--------|
| **Command Name** | ReleaseQuarantineHold |
| **Actor** | Warehouse Manager |
| **Target Aggregate** | Stock Position |
| **Business Purpose** | Clear a hold and restore quantity to sellable ATP after quality approval, customs clearance, or disposition decision. |
| **Expected Domain Event(s)** | QuarantineHoldReleased (DE-018), InventoryMovementRecorded (DE-074) |
| **Use Case** | UC-019 |

---

### CMD-020 — TransferConsignmentOwnership

| Field | Detail |
|-------|--------|
| **Command Name** | TransferConsignmentOwnership |
| **Actor** | Domain Service — Consignment Ownership Evaluation *(on consumption or sale)* |
| **Target Aggregate** | Stock Position |
| **Business Purpose** | Transfer ownership from supplier consignment to organization-owned inventory upon defined consumption or sale per supplier agreement. |
| **Expected Domain Event(s)** | ConsignmentOwnershipTransferred (DE-022), InventoryMovementRecorded (DE-074) |
| **Use Case** | UC-039 |

---

## Domain 3: Procurement & Inbound

---

### CMD-021 — SubmitPurchaseRequisition

| Field | Detail |
|-------|--------|
| **Command Name** | SubmitPurchaseRequisition |
| **Actor** | Buyer |
| **Target Aggregate** | Purchase Requisition |
| **Business Purpose** | Record an internal procurement need for specific products at a target location and route for approval before commercial commitment. |
| **Expected Domain Event(s)** | PurchaseRequisitionSubmitted (DE-023) |
| **Use Case** | UC-029 |

---

### CMD-022 — ApprovePurchaseRequisition

| Field | Detail |
|-------|--------|
| **Command Name** | ApprovePurchaseRequisition |
| **Actor** | Purchasing Manager |
| **Target Aggregate** | Purchase Requisition |
| **Business Purpose** | Grant internal authorization to proceed with supplier procurement after network availability and policy validation. |
| **Expected Domain Event(s)** | PurchaseRequisitionApproved (DE-024) |
| **Use Case** | UC-029 |

---

### CMD-023 — RejectPurchaseRequisition

| Field | Detail |
|-------|--------|
| **Command Name** | RejectPurchaseRequisition |
| **Actor** | Purchasing Manager |
| **Target Aggregate** | Purchase Requisition |
| **Business Purpose** | Deny a procurement request when network transfer is preferable or policy violations exist, directing requestor to alternatives. |
| **Expected Domain Event(s)** | PurchaseRequisitionRejected (DE-025) |
| **Use Case** | UC-029 |

---

### CMD-024 — PlacePurchaseOrder

| Field | Detail |
|-------|--------|
| **Command Name** | PlacePurchaseOrder |
| **Actor** | Buyer |
| **Target Aggregate** | Purchase Order |
| **Business Purpose** | Record an authorized commercial commitment to a supplier defining products, quantities, delivery terms, and receiving location. |
| **Expected Domain Event(s)** | PurchaseOrderPlaced (DE-026), AuditTrailRecorded (DE-075) |
| **Use Case** | UC-006 |

---

### CMD-025 — CancelPurchaseOrder

| Field | Detail |
|-------|--------|
| **Command Name** | CancelPurchaseOrder |
| **Actor** | Buyer |
| **Target Aggregate** | Purchase Order |
| **Business Purpose** | Withdraw a commercial commitment before full receipt when supply is no longer needed or terms cannot be met. |
| **Expected Domain Event(s)** | PurchaseOrderCancelled (DE-027), AuditTrailRecorded (DE-075) |
| **Use Case** | UC-006 |

---

### CMD-026 — ScheduleInboundDelivery

| Field | Detail |
|-------|--------|
| **Command Name** | ScheduleInboundDelivery |
| **Actor** | Buyer |
| **Target Aggregate** | Purchase Order |
| **Business Purpose** | Plan expected supplier arrival date and quantity so receiving operations and replenishment planners can prepare. |
| **Expected Domain Event(s)** | InboundDeliveryScheduled (DE-028) |
| **Use Case** | UC-007 |

---

### CMD-027 — RecordInboundDelay

| Field | Detail |
|-------|--------|
| **Command Name** | RecordInboundDelay |
| **Actor** | Buyer |
| **Target Aggregate** | Purchase Order |
| **Business Purpose** | Document that anticipated inbound supply will arrive later than planned, enabling replenishment and fulfillment risk response. |
| **Expected Domain Event(s)** | InboundDeliveryDelayed (DE-029) |
| **Use Case** | UC-030, UC-047 |

---

### CMD-028 — VerifyGoodsReceipt

| Field | Detail |
|-------|--------|
| **Command Name** | VerifyGoodsReceipt |
| **Actor** | Receiving Clerk |
| **Target Aggregate** | Goods Receipt |
| **Business Purpose** | Confirm quantity, product identity, and condition of inbound goods against purchase order or authorized receipt before acceptance. |
| **Expected Domain Event(s)** | GoodsReceiptVerified (DE-030) |
| **Use Case** | UC-008, UC-011 |

---

### CMD-029 — RecordReceiptDiscrepancy

| Field | Detail |
|-------|--------|
| **Command Name** | RecordReceiptDiscrepancy |
| **Actor** | Receiving Clerk |
| **Target Aggregate** | Goods Receipt |
| **Business Purpose** | Document variance between expected and received goods with evidence to preserve supplier accountability. |
| **Expected Domain Event(s)** | ReceiptDiscrepancyRecorded (DE-031) |
| **Use Case** | UC-009 |

---

### CMD-030 — ResolveReceiptDiscrepancy

| Field | Detail |
|-------|--------|
| **Command Name** | ResolveReceiptDiscrepancy |
| **Actor** | Warehouse Manager |
| **Target Aggregate** | Goods Receipt |
| **Business Purpose** | Close a receipt exception with documented outcome so accepted quantities proceed and rejected quantities are excluded from inventory. |
| **Expected Domain Event(s)** | ReceiptDiscrepancyResolved (DE-032), AuditTrailRecorded (DE-075) |
| **Use Case** | UC-009 |

---

### CMD-031 — CompletePutAway

| Field | Detail |
|-------|--------|
| **Command Name** | CompletePutAway |
| **Actor** | Warehouse Staff |
| **Target Aggregate** | Goods Receipt |
| **Business Purpose** | Confirm received goods are placed in designated storage position, completing the inbound workflow and enabling stock availability. |
| **Expected Domain Event(s)** | PutAwayCompleted (DE-033) → ReceiveStock → StockReceived (DE-011) |
| **Use Case** | UC-010 |

---

### CMD-032 — RecordSupplierInvoice

| Field | Detail |
|-------|--------|
| **Command Name** | RecordSupplierInvoice |
| **Actor** | Finance Manager |
| **Target Aggregate** | Supplier Invoice |
| **Business Purpose** | Register supplier billing document and initiate financial control evaluation against purchase order and goods receipt. |
| **Expected Domain Event(s)** | SupplierInvoiceReceived (DE-034) |
| **Use Case** | UC-039 |

---

### CMD-033 — EvaluateThreeWayMatch

| Field | Detail |
|-------|--------|
| **Command Name** | EvaluateThreeWayMatch |
| **Actor** | Finance Manager *(or domain service on invoice receipt)* |
| **Target Aggregate** | Supplier Invoice |
| **Business Purpose** | Compare PO, goods receipt, and invoice lines within tolerance to authorize or block payment. |
| **Expected Domain Event(s)** | ThreeWayMatchCompleted (DE-035) *on success* OR ThreeWayMatchExceptionRaised (DE-081) *on failure* |
| **Use Case** | UC-039 |

---

## Domain 4: Order Fulfillment

---

### CMD-034 — ConfirmOrderAvailability

| Field | Detail |
|-------|--------|
| **Command Name** | ConfirmOrderAvailability |
| **Actor** | Sales Representative |
| **Target Aggregate** | Customer Order Fulfillment |
| **Business Purpose** | Validate that ATP can support the order (fully or partially) before the business makes a commercial commitment to the customer. |
| **Expected Domain Event(s)** | OrderAvailabilityConfirmed (DE-036) |
| **Use Case** | UC-013, UC-021 |

---

### CMD-035 — ConfirmCustomerOrder

| Field | Detail |
|-------|--------|
| **Command Name** | ConfirmCustomerOrder |
| **Actor** | Customer Service Representative |
| **Target Aggregate** | Customer Order Fulfillment |
| **Business Purpose** | Establish commercial commitment to fulfill the order and initiate immediate stock reservation. |
| **Expected Domain Event(s)** | CustomerOrderConfirmed (DE-037) → ReserveStock → StockReserved (DE-012) |
| **Use Case** | UC-022 |

---

### CMD-036 — CancelCustomerOrder

| Field | Detail |
|-------|--------|
| **Command Name** | CancelCustomerOrder |
| **Actor** | Customer Service Representative |
| **Target Aggregate** | Customer Order Fulfillment |
| **Business Purpose** | Withdraw commercial commitment and release reserved stock back to ATP when order or line is no longer required. |
| **Expected Domain Event(s)** | CustomerOrderCancelled (DE-038) → ReleaseReservation → StockReservationReleased (DE-013) |
| **Use Case** | UC-023 |

---

### CMD-037 — CreateMultiLocationFulfillmentPlan

| Field | Detail |
|-------|--------|
| **Command Name** | CreateMultiLocationFulfillmentPlan |
| **Actor** | Warehouse Manager |
| **Target Aggregate** | Customer Order Fulfillment |
| **Business Purpose** | Assign order lines to multiple ship-from locations when no single location holds sufficient ATP for the full order. |
| **Expected Domain Event(s)** | MultiLocationFulfillmentPlanCreated (DE-045) → ReserveStock *per location* → StockReserved (DE-012) |
| **Use Case** | UC-048 |

---

### CMD-038 — VerifyPick

| Field | Detail |
|-------|--------|
| **Command Name** | VerifyPick |
| **Actor** | Warehouse Picker / Packer |
| **Target Aggregate** | Customer Order Fulfillment |
| **Business Purpose** | Confirm physical pick matches order requirements and authorize shipment, capturing lot/batch for traceable products. |
| **Expected Domain Event(s)** | PickVerified (DE-039), InventoryMovementRecorded (DE-074) |
| **Use Case** | UC-024 |

---

### CMD-039 — DispatchShipment

| Field | Detail |
|-------|--------|
| **Command Name** | DispatchShipment |
| **Actor** | Warehouse Picker / Packer |
| **Target Aggregate** | Customer Order Fulfillment |
| **Business Purpose** | Record handoff to carrier and trigger inventory deduction for verified picked goods. |
| **Expected Domain Event(s)** | ShipmentDispatched (DE-040) → ShipStock → StockShipped (DE-014), InventoryMovementRecorded (DE-074) |
| **Use Case** | UC-024 |

---

### CMD-040 — CompletePartialFulfillment

| Field | Detail |
|-------|--------|
| **Command Name** | CompletePartialFulfillment |
| **Actor** | Customer Service Representative |
| **Target Aggregate** | Customer Order Fulfillment |
| **Business Purpose** | Ship available quantity now and route unfulfilled remainder to backorder workflow with customer acknowledgment. |
| **Expected Domain Event(s)** | PartialFulfillmentCompleted (DE-041) → ShipmentDispatched (DE-040) *for fulfilled portion* |
| **Use Case** | UC-025 |

---

### CMD-041 — RecordBackorder

| Field | Detail |
|-------|--------|
| **Command Name** | RecordBackorder |
| **Actor** | Customer Service Representative |
| **Target Aggregate** | Customer Order Fulfillment |
| **Business Purpose** | Record mutual commercial commitment for unfulfilled quantity after explicit customer acknowledgment to wait. |
| **Expected Domain Event(s)** | BackorderRecorded (DE-042) |
| **Use Case** | UC-025 |

---

### CMD-042 — FulfillBackorder

| Field | Detail |
|-------|--------|
| **Command Name** | FulfillBackorder |
| **Actor** | Customer Service Representative |
| **Target Aggregate** | Customer Order Fulfillment |
| **Business Purpose** | Execute a previously backordered quantity when stock becomes available, reserving and fulfilling the delayed commitment. |
| **Expected Domain Event(s)** | BackorderFulfilled (DE-043) → ReserveStock → StockReserved (DE-012) → DispatchShipment (DE-040) |
| **Use Case** | UC-025 |

---

### CMD-043 — RaiseFulfillmentException

| Field | Detail |
|-------|--------|
| **Command Name** | RaiseFulfillmentException |
| **Actor** | Warehouse Manager |
| **Target Aggregate** | Customer Order Fulfillment |
| **Business Purpose** | Halt fulfillment when pick verification fails or shelf quantity mismatches system record, requiring manager resolution. |
| **Expected Domain Event(s)** | FulfillmentExceptionRaised (DE-044) |
| **Use Case** | UC-026 |

---

### CMD-044 — DispatchTransferStock

| Field | Detail |
|-------|--------|
| **Command Name** | DispatchTransferStock |
| **Actor** | Stock Position *(reaction handler — triggered by transfer dispatch)* |
| **Target Aggregate** | Stock Position |
| **Business Purpose** | Reduce source location on-hand when stock physically leaves for inter-location transfer. |
| **Expected Domain Event(s)** | InventoryMovementRecorded (DE-074), EvaluateStockStatus → threshold events (DE-068 – DE-070) *as applicable* |
| **Triggered By** | DispatchTransfer |
| **Use Case** | UC-033 |

---

## Domain 5: Network Transfer

---

### CMD-045 — RequestStockTransfer

| Field | Detail |
|-------|--------|
| **Command Name** | RequestStockTransfer |
| **Actor** | Regional / Store Manager |
| **Target Aggregate** | Stock Transfer |
| **Business Purpose** | Request stock movement from another location to resolve local shortage or rebalance network before new procurement. |
| **Expected Domain Event(s)** | TransferRequested (DE-046) |
| **Use Case** | UC-031 |

---

### CMD-046 — ApproveTransferRequest

| Field | Detail |
|-------|--------|
| **Command Name** | ApproveTransferRequest |
| **Actor** | Operations Director |
| **Target Aggregate** | Stock Transfer |
| **Business Purpose** | Authorize network redistribution after confirming source location can spare quantity while maintaining its service level. |
| **Expected Domain Event(s)** | TransferApproved (DE-047), AuditTrailRecorded (DE-075) |
| **Use Case** | UC-032 |

---

### CMD-047 — RejectTransferRequest

| Field | Detail |
|-------|--------|
| **Command Name** | RejectTransferRequest |
| **Actor** | Operations Director |
| **Target Aggregate** | Stock Transfer |
| **Business Purpose** | Deny redistribution when source cannot spare quantity or business justification is insufficient. |
| **Expected Domain Event(s)** | TransferRejected (DE-048) |
| **Use Case** | UC-032 |

---

### CMD-048 — DispatchTransfer

| Field | Detail |
|-------|--------|
| **Command Name** | DispatchTransfer |
| **Actor** | Warehouse Staff |
| **Target Aggregate** | Stock Transfer |
| **Business Purpose** | Record physical dispatch of stock from source location and create in-transit state excluded from both locations' ATP. |
| **Expected Domain Event(s)** | TransferDispatched (DE-049) → DispatchTransferStock → InventoryMovementRecorded (DE-074) |
| **Use Case** | UC-033 |

---

### CMD-049 — ConfirmTransferReceipt

| Field | Detail |
|-------|--------|
| **Command Name** | ConfirmTransferReceipt |
| **Actor** | Warehouse Staff |
| **Target Aggregate** | Stock Transfer |
| **Business Purpose** | Confirm destination receipt of transferred stock, closing in-transit state and increasing destination on-hand. |
| **Expected Domain Event(s)** | TransferReceived (DE-050) → ReceiveStock → StockReceived (DE-011) |
| **Use Case** | UC-033 |

---

### CMD-050 — RecordTransferDelay

| Field | Detail |
|-------|--------|
| **Command Name** | RecordTransferDelay |
| **Actor** | Warehouse Manager |
| **Target Aggregate** | Stock Transfer |
| **Business Purpose** | Document delayed in-transit stock so destination fulfillment and replenishment plans can be adjusted. |
| **Expected Domain Event(s)** | InTransitStockDelayed (DE-051) |
| **Use Case** | UC-030, UC-047 |

---

## Domain 6: Inventory Control & Accuracy

---

### CMD-051 — ScheduleCycleCount

| Field | Detail |
|-------|--------|
| **Command Name** | ScheduleCycleCount |
| **Actor** | Inventory Controller |
| **Target Aggregate** | Cycle Count |
| **Business Purpose** | Assign partial physical verification work for a product at a location, prioritizing Class A SKUs at highest frequency. |
| **Expected Domain Event(s)** | CycleCountScheduled (DE-052) |
| **Use Case** | UC-014 |

---

### CMD-052 — SubmitCycleCountResult

| Field | Detail |
|-------|--------|
| **Command Name** | SubmitCycleCountResult |
| **Actor** | Warehouse Staff |
| **Target Aggregate** | Cycle Count |
| **Business Purpose** | Record physical count under blind count protocol and calculate variance against system quantity at submission. |
| **Expected Domain Event(s)** | CycleCountCompleted (DE-053) → IdentifyCountVariance → CountVarianceIdentified (DE-054) *if variance exists* |
| **Use Case** | UC-014 |

---

### CMD-053 — ApproveCountVariance

| Field | Detail |
|-------|--------|
| **Command Name** | ApproveCountVariance |
| **Actor** | Warehouse Manager |
| **Target Aggregate** | Inventory Adjustment Case |
| **Business Purpose** | Authorize count variance adjustment after independent investigation, enforcing segregation of duties from counter. |
| **Expected Domain Event(s)** | CountVarianceApproved (DE-055), SegregationOfDutiesViolationDetected (DE-078) *if approver is counter* |
| **Use Case** | UC-016 |

---

### CMD-054 — SubmitAdjustment

| Field | Detail |
|-------|--------|
| **Command Name** | SubmitAdjustment |
| **Actor** | Warehouse Manager |
| **Target Aggregate** | Inventory Adjustment Case |
| **Business Purpose** | Propose inventory quantity correction with mandatory reason code, pending governance evaluation and approval. |
| **Expected Domain Event(s)** | AdjustmentSubmitted (DE-058) |
| **Use Case** | UC-017, UC-018 |

---

### CMD-055 — ApproveAdjustment

| Field | Detail |
|-------|--------|
| **Command Name** | ApproveAdjustment |
| **Actor** | Operations Director |
| **Target Aggregate** | Inventory Adjustment Case |
| **Business Purpose** | Authorize inventory correction or write-off after threshold validation and independent approval chain satisfaction. |
| **Expected Domain Event(s)** | AdjustmentApproved (DE-059) → ApplyApprovedAdjustment → StockAdjusted (DE-015) OR ApplyApprovedWriteOff → StockWrittenOff (DE-016); SegregationOfDutiesViolationDetected (DE-078) *if SoD violated*; AuditTrailRecorded (DE-075) |
| **Use Case** | UC-017, UC-018 |

---

### CMD-056 — RejectAdjustment

| Field | Detail |
|-------|--------|
| **Command Name** | RejectAdjustment |
| **Actor** | Operations Director |
| **Target Aggregate** | Inventory Adjustment Case |
| **Business Purpose** | Deny proposed inventory change due to insufficient evidence, policy threshold breach, or segregation-of-duties violation. |
| **Expected Domain Event(s)** | AdjustmentRejected (DE-060) |
| **Use Case** | UC-017, UC-018 |

---

### CMD-057 — IdentifyCountVariance

| Field | Detail |
|-------|--------|
| **Command Name** | IdentifyCountVariance |
| **Actor** | Inventory Adjustment Case *(reaction handler — triggered by count submission)* |
| **Target Aggregate** | Inventory Adjustment Case |
| **Business Purpose** | Open an investigation case when physical count differs from system quantity, blocking direct stock mutation. |
| **Expected Domain Event(s)** | CountVarianceIdentified (DE-054) |
| **Triggered By** | SubmitCycleCountResult, CertifyPhysicalInventoryCount |
| **Use Case** | UC-016 |

---

### CMD-058 — EstablishOpeningBalances

| Field | Detail |
|-------|--------|
| **Command Name** | EstablishOpeningBalances |
| **Actor** | Inventory Controller |
| **Target Aggregate** | Stock Position |
| **Business Purpose** | Load verified opening on-hand quantities at location go-live to establish the authoritative inventory baseline. |
| **Expected Domain Event(s)** | StockReceived (DE-011) *per product line*, InventoryMovementRecorded (DE-074), AuditTrailRecorded (DE-075) |
| **Use Case** | UC-046 |

---

### CMD-059 — ApplyQuarantineFromReturn

| Field | Detail |
|-------|--------|
| **Command Name** | ApplyQuarantineFromReturn |
| **Actor** | Stock Position *(reaction handler — triggered by return quarantine disposition)* |
| **Target Aggregate** | Stock Position |
| **Business Purpose** | Place returned goods under quarantine hold pending further quality evaluation. |
| **Expected Domain Event(s)** | QuarantineHoldApplied (DE-017), InventoryMovementRecorded (DE-074) |
| **Triggered By** | QuarantineReturnedGoods |
| **Use Case** | UC-036 |

---

### CMD-060 — RecordCountVarianceFromPhysicalCount

| Field | Detail |
|-------|--------|
| **Command Name** | RecordCountVarianceFromPhysicalCount |
| **Actor** | Physical Inventory Count *(during certification)* |
| **Target Aggregate** | Inventory Adjustment Case |
| **Business Purpose** | Route each wall-to-wall count line variance to investigation without mutating stock during the count event. |
| **Expected Domain Event(s)** | CountVarianceIdentified (DE-054) *per variance line* |
| **Triggered By** | CertifyPhysicalInventoryCount |
| **Use Case** | UC-015, UC-016 |

---

## Domain 7: Returns Management

---

### CMD-061 — IssueReturnAuthorization

| Field | Detail |
|-------|--------|
| **Command Name** | IssueReturnAuthorization |
| **Actor** | Customer Service Representative |
| **Target Aggregate** | Customer Return Case |
| **Business Purpose** | Authorize customer return linked to original order so warehouse can expect and accept inbound return goods. |
| **Expected Domain Event(s)** | ReturnAuthorizationIssued (DE-061) |
| **Use Case** | UC-035 |

---

### CMD-062 — ExpireReturnAuthorization

| Field | Detail |
|-------|--------|
| **Command Name** | ExpireReturnAuthorization |
| **Actor** | Domain Policy *(return window elapsed)* |
| **Target Aggregate** | Customer Return Case |
| **Business Purpose** | Close return window when authorized period passes without receipt, preventing unauthorized warehouse acceptance. |
| **Expected Domain Event(s)** | ReturnAuthorizationExpired (DE-062) |
| **Use Case** | UC-035 |

---

### CMD-063 — ReceiveCustomerReturn

| Field | Detail |
|-------|--------|
| **Command Name** | ReceiveCustomerReturn |
| **Actor** | Receiving Clerk |
| **Target Aggregate** | Customer Return Case |
| **Business Purpose** | Verify and accept authorized return goods at the warehouse, initiating inspection and disposition workflow. |
| **Expected Domain Event(s)** | CustomerReturnReceived (DE-063) |
| **Use Case** | UC-011, UC-036 |

---

### CMD-064 — InspectReturnedGoods

| Field | Detail |
|-------|--------|
| **Command Name** | InspectReturnedGoods |
| **Actor** | Receiving Clerk |
| **Target Aggregate** | Customer Return Case |
| **Business Purpose** | Assess condition of returned goods to determine whether restock, quarantine, or write-off disposition is appropriate. |
| **Expected Domain Event(s)** | ReturnInspected (DE-064) |
| **Use Case** | UC-036 |

---

### CMD-065 — RestockReturnedGoods

| Field | Detail |
|-------|--------|
| **Command Name** | RestockReturnedGoods |
| **Actor** | Receiving Clerk |
| **Target Aggregate** | Customer Return Case |
| **Business Purpose** | Return qualifying goods to sellable inventory when condition grade confirms resale quality. |
| **Expected Domain Event(s)** | ReturnRestocked (DE-065) → ReceiveStock → StockReceived (DE-011) |
| **Use Case** | UC-036 |

---

### CMD-066 — QuarantineReturnedGoods

| Field | Detail |
|-------|--------|
| **Command Name** | QuarantineReturnedGoods |
| **Actor** | Warehouse Manager |
| **Target Aggregate** | Customer Return Case |
| **Business Purpose** | Place returned goods requiring further evaluation under quarantine, excluding them from sellable ATP. |
| **Expected Domain Event(s)** | ReturnQuarantined (DE-066) → ApplyQuarantineFromReturn → QuarantineHoldApplied (DE-017) |
| **Use Case** | UC-036 |

---

### CMD-067 — WriteOffReturnedGoods

| Field | Detail |
|-------|--------|
| **Command Name** | WriteOffReturnedGoods |
| **Actor** | Warehouse Manager |
| **Target Aggregate** | Customer Return Case |
| **Business Purpose** | Permanently remove non-resalable returned goods from inventory value after inspection confirms damage or defect. |
| **Expected Domain Event(s)** | ReturnWrittenOff (DE-067) → ApplyApprovedWriteOff → StockWrittenOff (DE-016) |
| **Use Case** | UC-036 |

---

## Domain 8: Commercial & Monitoring

---

### CMD-068 — AllocatePromotionalStock

| Field | Detail |
|-------|--------|
| **Command Name** | AllocatePromotionalStock |
| **Actor** | Marketing Manager |
| **Target Aggregate** | Promotional Stock Allocation |
| **Business Purpose** | Ring-fence defined quantity for a promotional campaign or launch, excluding it from general ATP for non-approved orders. |
| **Expected Domain Event(s)** | PromotionalStockAllocated (DE-020) |
| **Use Case** | UC-040 |

---

### CMD-069 — ReleasePromotionalAllocation

| Field | Detail |
|-------|--------|
| **Command Name** | ReleasePromotionalAllocation |
| **Actor** | Marketing Manager |
| **Target Aggregate** | Promotional Stock Allocation |
| **Business Purpose** | Return unconsumed promotional stock to general sellable pool when campaign period ends or allocation is manually released. |
| **Expected Domain Event(s)** | PromotionalAllocationReleased (DE-021) |
| **Use Case** | UC-040 |

---

### CMD-070 — EvaluateStockStatus

| Field | Detail |
|-------|--------|
| **Command Name** | EvaluateStockStatus |
| **Actor** | Domain Service — Stock Status Classification |
| **Target Aggregate** | Stock Position |
| **Business Purpose** | Reclassify stock status when quantities cross policy thresholds to trigger replenishment alerts and operational response. |
| **Expected Domain Event(s)** | LowStockThresholdBreached (DE-068) OR OutOfStockDetected (DE-069) OR OverstockDetected (DE-070) *as applicable* |
| **Use Case** | UC-012, UC-028 |

---

### CMD-071 — RecommendReplenishmentAction

| Field | Detail |
|-------|--------|
| **Command Name** | RecommendReplenishmentAction |
| **Actor** | Domain Service — Replenishment Recommendation |
| **Target Aggregate** | *(Cross-cutting — no single aggregate mutation)* |
| **Business Purpose** | Produce replenishment guidance (purchase, transfer, or no action) after threshold breach and network availability evaluation. |
| **Expected Domain Event(s)** | ReplenishmentRecommended (DE-071) |
| **Use Case** | UC-028, UC-029, UC-034 |

---

### CMD-072 — EvaluatePromotionalReadiness

| Field | Detail |
|-------|--------|
| **Command Name** | EvaluatePromotionalReadiness |
| **Actor** | Domain Service — Promotional Readiness Evaluation |
| **Target Aggregate** | Promotional Stock Allocation |
| **Business Purpose** | Assess whether ring-fenced promotional stock is sufficient before campaign or launch commitment deadline. |
| **Expected Domain Event(s)** | PromotionalReadinessGapIdentified (DE-072) *when insufficient* |
| **Use Case** | UC-040, UC-047 |

---

### CMD-073 — AnalyzeNetworkBalance

| Field | Detail |
|-------|--------|
| **Command Name** | AnalyzeNetworkBalance |
| **Actor** | Domain Service — Network Rebalancing Analysis |
| **Target Aggregate** | *(Cross-cutting — no single aggregate mutation)* |
| **Business Purpose** | Detect simultaneous stockout risk at one location and excess at another for the same product to recommend transfer-before-buy. |
| **Expected Domain Event(s)** | NetworkImbalanceDetected (DE-073) |
| **Use Case** | UC-034 |

---

## Domain 9: Financial & Governance

---

### CMD-074 — PrepareValuationSnapshot

| Field | Detail |
|-------|--------|
| **Command Name** | PrepareValuationSnapshot |
| **Actor** | Finance Manager |
| **Target Aggregate** | Inventory Valuation Snapshot *(read model)* |
| **Business Purpose** | Compile point-in-time owned inventory value for finance reconciliation against general ledger at period end. |
| **Expected Domain Event(s)** | InventoryValuationSnapshotPrepared (DE-076) |
| **Use Case** | UC-039 |

---

### CMD-075 — ReconcileInventoryValuation

| Field | Detail |
|-------|--------|
| **Command Name** | ReconcileInventoryValuation |
| **Actor** | Finance Manager |
| **Target Aggregate** | Inventory Valuation Snapshot *(read model)* |
| **Business Purpose** | Compare operational inventory valuation against general ledger and identify misalignment requiring investigation. |
| **Expected Domain Event(s)** | ValuationVarianceIdentified (DE-077) *when variance exceeds tolerance* |
| **Use Case** | UC-039 |

---

### CMD-076 — ProvisionUserAccount

| Field | Detail |
|-------|--------|
| **Command Name** | ProvisionUserAccount |
| **Actor** | System Administrator |
| **Target Aggregate** | User Account |
| **Business Purpose** | Create user identity with initial role assignments and location scope for authorized inventory operations. |
| **Expected Domain Event(s)** | UserAccountProvisioned (DE-079), AuditTrailRecorded (DE-075) |
| **Use Case** | UC-044 |

---

### CMD-077 — ChangeRoleAssignment

| Field | Detail |
|-------|--------|
| **Command Name** | ChangeRoleAssignment |
| **Actor** | System Administrator |
| **Target Aggregate** | User Account |
| **Business Purpose** | Add, modify, or remove user role and location scope, re-evaluating segregation-of-duties compliance. |
| **Expected Domain Event(s)** | RoleAssignmentChanged (DE-080), SegregationOfDutiesViolationDetected (DE-078) *if conflicting roles assigned*; AuditTrailRecorded (DE-075) |
| **Use Case** | UC-044, UC-045 |

---

### CMD-078 — ValidateSegregationOfDuties

| Field | Detail |
|-------|--------|
| **Command Name** | ValidateSegregationOfDuties |
| **Actor** | Domain Service — Segregation of Duties Validation |
| **Target Aggregate** | User Account |
| **Business Purpose** | Block actions that violate accountability controls when the same user attempts conflicting initiate and approve roles. |
| **Expected Domain Event(s)** | SegregationOfDutiesViolationDetected (DE-078) |
| **Triggered By** | ApproveCountVariance, ApproveAdjustment, ChangeRoleAssignment, and other governed approval commands |
| **Use Case** | UC-045 |

---

## Command-to-Event Quick Reference

| Command | Primary Event(s) | Downstream Event Chain |
|---------|------------------|------------------------|
| RegisterProduct | DE-001 | DE-075 |
| ChangeProductStatus | DE-002 | DE-075 |
| ConfirmCustomerOrder | DE-037 | DE-012, DE-074 |
| CompletePutAway | DE-033 | DE-011, DE-074, DE-068–070 |
| DispatchShipment | DE-040 | DE-014, DE-074, DE-022 |
| ApproveAdjustment | DE-059 | DE-015 or DE-016, DE-074, DE-075 |
| DispatchTransfer | DE-049 | DE-074, DE-050→DE-011 |
| SubmitCycleCountResult | DE-053 | DE-054 |
| RestockReturnedGoods | DE-065 | DE-011, DE-074 |
| EvaluateThreeWayMatch | DE-035 or DE-081 | — |
| EvaluateStockStatus | DE-068, DE-069, or DE-070 | DE-071 |

---

## Excluded from Domain Commands

| Action | Treatment | Rationale |
|--------|-----------|-----------|
| SearchProduct, ViewInventory, QueryAuditTrail | Query | Read-only — no state mutation |
| AcknowledgeAlert, ViewDashboard | Notification/Read | Acknowledgment does not change inventory domain state |
| Failed validation (rule rejected) | Rejection response | Aggregate unchanged — no event |
| Login, Logout | Identity infrastructure | Outside inventory domain boundary |
| SendEmail, DeliverNotification | Infrastructure | Delivery channel is not a business command |

---

## Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Domain Expert | | | |
| DDD Architect | | | |
| Senior Business Analyst | | | |
| Solution Architect | | | |

---

*End of Domain Commands*

*Document ID: SRS-ES-002 | Version 1.0 | July 6, 2026*
