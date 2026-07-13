# Domain Policies
## Inventory Management System

---

## Document Information

| Attribute | Detail |
|-----------|--------|
| **Document ID** | SRS-ES-003 |
| **Document Title** | Domain Policies — Event Storming Catalog |
| **Version** | 1.0 |
| **Status** | Draft |
| **Document Owner** | Domain Expert |
| **Source Documents** | SRS-ES-001 (Domain Events), SRS-ES-002 (Domain Commands), SRS-DM-005 (Domain Services), SRS-BR-001 (Business Rules) |
| **Date** | July 6, 2026 |
| **Scope** | Business reaction policies only — no message handlers, sagas, or infrastructure orchestration |

### Purpose

This document identifies **Domain Policies** for the Inventory Management System. A policy is a business reaction rule expressed as:

> **Whenever** [Domain Event] **then** [Business Action]

Policies connect domain events to subsequent business intentions. They represent organizational workflow discipline — what must happen next when a meaningful business fact is recorded. Policies may issue a command, block an action, route work to a human actor, or raise an alert.

### Policy Naming Convention

Policies use descriptive **PascalCase** names ending in `Policy` where helpful: `ReserveStockOnOrderConfirmationPolicy`, or concise workflow names: `Activate Stock on Put-Away`.

### Policy Catalog Summary

| Workflow Area | Policy IDs | Count |
|---------------|------------|-------|
| Order Fulfillment | POL-001 – POL-010 | 10 |
| Inbound & Procurement | POL-011 – POL-020 | 10 |
| Inventory Balance & Replenishment | POL-021 – POL-028 | 8 |
| Network Transfer | POL-029 – POL-033 | 5 |
| Inventory Accuracy & Control | POL-034 – POL-042 | 9 |
| Returns Management | POL-043 – POL-048 | 6 |
| Commercial & Promotional | POL-049 – POL-052 | 4 |
| Governance & Access Control | POL-053 – POL-058 | 6 |
| Financial Alignment | POL-059 – POL-062 | 4 |
| Master Data & Reference | POL-063 – POL-066 | 4 |
| **Total** | | **64** |

---

## Workflow 1: Order Fulfillment

---

### POL-001 — Reserve Stock on Order Confirmation

| Field | Detail |
|-------|--------|
| **Policy Name** | Reserve Stock on Order Confirmation |
| **Triggering Domain Event** | CustomerOrderConfirmed (DE-037) |
| **Business Rule Applied** | BR-002 (Reservation at Order Confirmation), BR-010 (Safety Stock Protection), BR-029 (Promotional Stock Ring-Fencing) |
| **Action Taken** | Coordinate reservation across order lines and stock positions, validating ATP, safety stock, and promotional ring-fence rules before committing quantity. |
| **Resulting Command** | `ReserveStock` (CMD-012) |

---

### POL-002 — Release Reservation on Order Cancellation

| Field | Detail |
|-------|--------|
| **Policy Name** | Release Reservation on Order Cancellation |
| **Triggering Domain Event** | CustomerOrderCancelled (DE-038) |
| **Business Rule Applied** | BR-002 (Reservation at Order Confirmation) |
| **Action Taken** | Return all reserved quantity for cancelled order lines to the available-to-promise pool. |
| **Resulting Command** | `ReleaseReservation` (CMD-013) |

---

### POL-003 — Allocate Multi-Location Reservations

| Field | Detail |
|-------|--------|
| **Policy Name** | Allocate Multi-Location Reservations |
| **Triggering Domain Event** | MultiLocationFulfillmentPlanCreated (DE-045) |
| **Business Rule Applied** | BR-001 (ATP-Only Customer Commitment), BR-002 (Reservation at Order Confirmation) |
| **Action Taken** | Reserve stock at each assigned ship-from location according to the fulfillment plan decomposition. |
| **Resulting Command** | `ReserveStock` (CMD-012) *per allocated location* |

---

### POL-004 — Require Verified Pick Before Shipment

| Field | Detail |
|-------|--------|
| **Policy Name** | Require Verified Pick Before Shipment |
| **Triggering Domain Event** | PickVerified (DE-039) |
| **Business Rule Applied** | BR-003 (Verified Pick Before Shipment), BR-014 (FEFO), BR-015 (FIFO), BR-017 (Lot/Batch Capture) |
| **Action Taken** | Authorize shipment dispatch only after pick verification; apply rotation policy and capture lot/batch for traceable products. |
| **Resulting Command** | `DispatchShipment` (CMD-039) *when warehouse proceeds to ship* |

---

### POL-005 — Deduct Stock on Shipment Dispatch

| Field | Detail |
|-------|--------|
| **Policy Name** | Deduct Stock on Shipment Dispatch |
| **Triggering Domain Event** | ShipmentDispatched (DE-040) |
| **Business Rule Applied** | BR-003 (Verified Pick Before Shipment), BR-002 (Reservation consumed on shipment) |
| **Action Taken** | Deduct on-hand and reserved quantities from the source stock position and record outbound movement. |
| **Resulting Command** | `ShipStock` (CMD-015) |

---

### POL-006 — Record Partial Fulfillment and Backorder

| Field | Detail |
|-------|--------|
| **Policy Name** | Record Partial Fulfillment and Backorder |
| **Triggering Domain Event** | PartialFulfillmentCompleted (DE-041) |
| **Business Rule Applied** | BR-028 (Backorder Customer Acknowledgment), BR-001 (ATP-Only Customer Commitment) |
| **Action Taken** | Ship available quantity immediately; route unfulfilled remainder to backorder workflow pending customer acknowledgment. |
| **Resulting Command** | `DispatchShipment` (CMD-039) *fulfilled portion*; `RecordBackorder` (CMD-041) *remainder* |

---

### POL-007 — Prioritize Backorder Replenishment

| Field | Detail |
|-------|--------|
| **Policy Name** | Prioritize Backorder Replenishment |
| **Triggering Domain Event** | BackorderRecorded (DE-042) |
| **Business Rule Applied** | BR-028 (Backorder Customer Acknowledgment), BR-009 (Reorder at Reorder Level) |
| **Action Taken** | Flag backordered products for priority replenishment review and notify purchasing and customer service teams. |
| **Resulting Command** | `RecommendReplenishmentAction` (CMD-071) |

---

### POL-008 — Fulfill Backorder When Stock Arrives

| Field | Detail |
|-------|--------|
| **Policy Name** | Fulfill Backorder When Stock Arrives |
| **Triggering Domain Event** | StockReceived (DE-011) |
| **Business Rule Applied** | BR-002 (Reservation at Order Confirmation), BR-028 (Backorder Customer Acknowledgment) |
| **Action Taken** | When inbound stock satisfies a pending backorder line, initiate reservation and fulfillment for the oldest acknowledged backorder first. |
| **Resulting Command** | `FulfillBackorder` (CMD-042) *when matching backorder exists* |

---

### POL-009 — Escalate Fulfillment Exception

| Field | Detail |
|-------|--------|
| **Policy Name** | Escalate Fulfillment Exception |
| **Triggering Domain Event** | FulfillmentExceptionRaised (DE-044) |
| **Business Rule Applied** | BR-003 (Verified Pick Before Shipment), BR-022 (Investigate Before Adjusting) |
| **Action Taken** | Halt shipment, notify warehouse manager, and route shelf mismatch to count variance investigation or quality hold as appropriate. |
| **Resulting Command** | `RaiseFulfillmentException` *(already raised)*; `IdentifyCountVariance` (CMD-057) or `ApplyQuarantineHold` (CMD-018) *as applicable* |

---

### POL-010 — Block Ineligible Product Reservation

| Field | Detail |
|-------|--------|
| **Policy Name** | Block Ineligible Product Reservation |
| **Triggering Domain Event** | ProductStatusChanged (DE-002) — *to inactive or discontinued* |
| **Business Rule Applied** | BR-027 (No Reorder of Discontinued Products) |
| **Action Taken** | Prevent new reservations and purchase order lines for products that are inactive or discontinued; existing reservations may fulfill but no new commitments permitted. |
| **Resulting Command** | None *(block `ConfirmCustomerOrder` and `PlacePurchaseOrder`)* |

---

## Workflow 2: Inbound & Procurement

---

### POL-011 — Stage Stock for Put-Away After Verification

| Field | Detail |
|-------|--------|
| **Policy Name** | Stage Stock for Put-Away After Verification |
| **Triggering Domain Event** | GoodsReceiptVerified (DE-030) |
| **Business Rule Applied** | BR-005 (Put-Away Before Availability), BR-004 (Verify Before Inventory Acceptance) |
| **Action Taken** | Keep received stock off sellable ATP; generate put-away work for warehouse staff to move goods to storage positions. |
| **Resulting Command** | `CompletePutAway` (CMD-031) *issued by warehouse when ready* |

---

### POL-012 — Activate Stock on Put-Away Completion

| Field | Detail |
|-------|--------|
| **Policy Name** | Activate Stock on Put-Away Completion |
| **Triggering Domain Event** | PutAwayCompleted (DE-033) |
| **Business Rule Applied** | BR-005 (Put-Away Before Availability), BR-030 (Bonded Inventory Customs Clearance) |
| **Action Taken** | Validate customs/bonded clearance status; if cleared, increase on-hand quantity and ATP at the destination stock position. |
| **Resulting Command** | `ReceiveStock` (CMD-014) |

---

### POL-013 — Hold Bonded Stock Until Customs Clearance

| Field | Detail |
|-------|--------|
| **Policy Name** | Hold Bonded Stock Until Customs Clearance |
| **Triggering Domain Event** | GoodsReceiptVerified (DE-030) — *bonded inventory* |
| **Business Rule Applied** | BR-030 (Bonded Inventory Customs Clearance), BR-013 (Quarantine Exclusion from Sellable Stock) |
| **Action Taken** | Place verified bonded goods under quarantine hold; exclude from put-away activation and sellable ATP until customs clearance is confirmed. |
| **Resulting Command** | `ApplyQuarantineHold` (CMD-018) |

---

### POL-014 — Document Discrepancy Before Acceptance

| Field | Detail |
|-------|--------|
| **Policy Name** | Document Discrepancy Before Acceptance |
| **Triggering Domain Event** | ReceiptDiscrepancyRecorded (DE-031) |
| **Business Rule Applied** | BR-006 (Document Receipt Discrepancies), BR-008 (Three-Way Match Before Payment) |
| **Action Taken** | Separate accepted quantities from unresolved variance; notify buyer and supplier for claim resolution before financial match proceeds. |
| **Resulting Command** | `ResolveReceiptDiscrepancy` (CMD-030) *when manager resolves* |

---

### POL-015 — Evaluate Three-Way Match on Invoice Receipt

| Field | Detail |
|-------|--------|
| **Policy Name** | Evaluate Three-Way Match on Invoice Receipt |
| **Triggering Domain Event** | SupplierInvoiceReceived (DE-034) |
| **Business Rule Applied** | BR-008 (Three-Way Match Before Payment) |
| **Action Taken** | Compare invoice lines against linked purchase order and goods receipt within governance tolerance limits. |
| **Resulting Command** | `EvaluateThreeWayMatch` (CMD-033) |

---

### POL-016 — Re-Evaluate Match After Receipt or Discrepancy Resolution

| Field | Detail |
|-------|--------|
| **Policy Name** | Re-Evaluate Match After Receipt or Discrepancy Resolution |
| **Triggering Domain Event** | ReceiptDiscrepancyResolved (DE-032) OR GoodsReceiptVerified (DE-030) *when invoice already recorded* |
| **Business Rule Applied** | BR-008 (Three-Way Match Before Payment), BR-006 (Document Receipt Discrepancies) |
| **Action Taken** | Re-run three-way match evaluation when receipt data changes and a supplier invoice is awaiting match. |
| **Resulting Command** | `EvaluateThreeWayMatch` (CMD-033) |

---

### POL-017 — Authorize Payment on Successful Match

| Field | Detail |
|-------|--------|
| **Policy Name** | Authorize Payment on Successful Match |
| **Triggering Domain Event** | ThreeWayMatchCompleted (DE-035) |
| **Business Rule Applied** | BR-008 (Three-Way Match Before Payment) |
| **Action Taken** | Release payment authorization to finance for matched goods; update procurement accountability status. |
| **Resulting Command** | None *(finance payment workflow — outside inventory aggregate boundary)* |

---

### POL-018 — Block Payment on Match Exception

| Field | Detail |
|-------|--------|
| **Policy Name** | Block Payment on Match Exception |
| **Triggering Domain Event** | ThreeWayMatchExceptionRaised (DE-081) |
| **Business Rule Applied** | BR-008 (Three-Way Match Before Payment) |
| **Action Taken** | Block payment authorization; route quantity or price discrepancy to finance and purchasing for joint resolution. |
| **Resulting Command** | None *(human resolution workflow)* |

---

### POL-019 — Convert Approved Requisition to Purchase Order

| Field | Detail |
|-------|--------|
| **Policy Name** | Convert Approved Requisition to Purchase Order |
| **Triggering Domain Event** | PurchaseRequisitionApproved (DE-024) |
| **Business Rule Applied** | BR-027 (No Reorder of Discontinued Products), BR-011 (Network Check Before Purchase) |
| **Action Taken** | Notify buyer that internal authorization is granted; buyer creates commercial purchase order from approved requisition. |
| **Resulting Command** | `PlacePurchaseOrder` (CMD-024) *issued by buyer* |

---

### POL-020 — Plan Inbound Delivery on Purchase Order Placement

| Field | Detail |
|-------|--------|
| **Policy Name** | Plan Inbound Delivery on Purchase Order Placement |
| **Triggering Domain Event** | PurchaseOrderPlaced (DE-026) |
| **Business Rule Applied** | BR-007 (Purchase Order Required for Supplier Receipt) |
| **Action Taken** | Create expected inbound delivery schedule and communicate anticipated arrival to receiving location and replenishment planners. |
| **Resulting Command** | `ScheduleInboundDelivery` (CMD-026) |

---

## Workflow 3: Inventory Balance & Replenishment

---

### POL-021 — Reclassify Stock Status on Quantity Change

| Field | Detail |
|-------|--------|
| **Policy Name** | Reclassify Stock Status on Quantity Change |
| **Triggering Domain Event** | StockReceived (DE-011), StockShipped (DE-014), StockAdjusted (DE-015), StockWrittenOff (DE-016), StockReserved (DE-012), StockReservationReleased (DE-013) |
| **Business Rule Applied** | BR-009 (Reorder at Reorder Level) |
| **Action Taken** | Compare current ATP and on-hand against stock policy thresholds and reclassify status (in stock, low stock, out of stock, overstock). |
| **Resulting Command** | `EvaluateStockStatus` (CMD-070) |

---

### POL-022 — Trigger Replenishment on Low Stock

| Field | Detail |
|-------|--------|
| **Policy Name** | Trigger Replenishment on Low Stock |
| **Triggering Domain Event** | LowStockThresholdBreached (DE-068) |
| **Business Rule Applied** | BR-009 (Reorder at Reorder Level — same business day action), BR-011 (Network Check Before Purchase) |
| **Action Taken** | Evaluate network availability and recommend purchase requisition, transfer request, or no action; notify purchasing manager. |
| **Resulting Command** | `RecommendReplenishmentAction` (CMD-071) |

---

### POL-023 — Escalate Out-of-Stock Urgently

| Field | Detail |
|-------|--------|
| **Policy Name** | Escalate Out-of-Stock Urgently |
| **Triggering Domain Event** | OutOfStockDetected (DE-069) |
| **Business Rule Applied** | BR-009 (Reorder at Reorder Level), BR-032 (Class A Priority Monitoring) |
| **Action Taken** | Raise urgent operational alert with elevated priority for Class A products; escalate to purchasing and operations leadership. |
| **Resulting Command** | `RecommendReplenishmentAction` (CMD-071) |

---

### POL-024 — Flag Overstock for Network Rebalancing

| Field | Detail |
|-------|--------|
| **Policy Name** | Flag Overstock for Network Rebalancing |
| **Triggering Domain Event** | OverstockDetected (DE-070) |
| **Business Rule Applied** | BR-011 (Network Check Before Purchase), BR-012 (Protect Source Location Minimum) |
| **Action Taken** | Identify whether excess can be redistributed to locations with shortage before new procurement is considered. |
| **Resulting Command** | `AnalyzeNetworkBalance` (CMD-073) |

---

### POL-025 — Apply Adjustment on Governance Approval

| Field | Detail |
|-------|--------|
| **Policy Name** | Apply Adjustment on Governance Approval |
| **Triggering Domain Event** | AdjustmentApproved (DE-059) |
| **Business Rule Applied** | BR-021 (Independent Approval for Material Adjustments), BR-020 (Mandatory Adjustment Reason Codes) |
| **Action Taken** | Mutate stock position quantity per approved adjustment case — correction or permanent write-off. |
| **Resulting Command** | `ApplyApprovedAdjustment` (CMD-016) OR `ApplyApprovedWriteOff` (CMD-017) |

---

### POL-026 — Segregate ATP on Promotional Allocation

| Field | Detail |
|-------|--------|
| **Policy Name** | Segregate ATP on Promotional Allocation |
| **Triggering Domain Event** | PromotionalStockAllocated (DE-020) |
| **Business Rule Applied** | BR-029 (Promotional Stock Ring-Fencing), BR-001 (ATP-Only Customer Commitment) |
| **Action Taken** | Reduce general ATP by ring-fenced quantity; protect allocated stock from non-promotional order reservations. |
| **Resulting Command** | None *(ATP segregation applied within Stock Position coordination)* |

---

### POL-027 — Restore General ATP on Campaign End

| Field | Detail |
|-------|--------|
| **Policy Name** | Restore General ATP on Campaign End |
| **Triggering Domain Event** | PromotionalAllocationReleased (DE-021) |
| **Business Rule Applied** | BR-029 (Promotional Stock Ring-Fencing) |
| **Action Taken** | Return unconsumed promotional quantity to general sellable pool for standard order fulfillment. |
| **Resulting Command** | `ReleasePromotionalAllocation` *(already executed)*; ATP restoration within Stock Position |

---

### POL-028 — Transfer Consignment Ownership on Consumption

| Field | Detail |
|-------|--------|
| **Policy Name** | Transfer Consignment Ownership on Consumption |
| **Triggering Domain Event** | StockShipped (DE-014) — *consignment stock* |
| **Business Rule Applied** | BR-031 (Consignment Ownership at Consumption) |
| **Action Taken** | Transfer ownership from supplier consignment to organization-owned inventory upon sale or consumption per supplier agreement. |
| **Resulting Command** | `TransferConsignmentOwnership` (CMD-020) |

---

## Workflow 4: Network Transfer

---

### POL-029 — Evaluate Network Before Procurement

| Field | Detail |
|-------|--------|
| **Policy Name** | Evaluate Network Before Procurement |
| **Triggering Domain Event** | PurchaseRequisitionSubmitted (DE-023) OR ReplenishmentRecommended (DE-071) |
| **Business Rule Applied** | BR-011 (Network Check Before Purchase) |
| **Action Taken** | Scan network-wide ATP and in-transit supply; recommend transfer instead of purchase when excess exists at another location. |
| **Resulting Command** | `RequestStockTransfer` (CMD-045) *recommended* OR `RejectPurchaseRequisition` (CMD-023) *if transfer preferred* |

---

### POL-030 — Validate Source Capacity on Transfer Request

| Field | Detail |
|-------|--------|
| **Policy Name** | Validate Source Capacity on Transfer Request |
| **Triggering Domain Event** | TransferRequested (DE-046) |
| **Business Rule Applied** | BR-012 (Protect Source Location Minimum), BR-010 (Safety Stock Protection) |
| **Action Taken** | Calculate maximum transferable quantity from source without breaching minimum threshold or safety stock buffer; route for operations director approval. |
| **Resulting Command** | `ApproveTransferRequest` (CMD-046) OR `RejectTransferRequest` (CMD-047) *by operations director* |

---

### POL-031 — Deduct Source Stock on Transfer Dispatch

| Field | Detail |
|-------|--------|
| **Policy Name** | Deduct Source Stock on Transfer Dispatch |
| **Triggering Domain Event** | TransferDispatched (DE-049) |
| **Business Rule Applied** | BR-012 (Protect Source Location Minimum), BR-017 (Lot/Batch Capture) |
| **Action Taken** | Reduce source location on-hand; create in-transit state excluded from both source and destination ATP. |
| **Resulting Command** | `DispatchTransferStock` (CMD-044) |

---

### POL-032 — Increase Destination Stock on Transfer Receipt

| Field | Detail |
|-------|--------|
| **Policy Name** | Increase Destination Stock on Transfer Receipt |
| **Triggering Domain Event** | TransferReceived (DE-050) |
| **Business Rule Applied** | BR-017 (Lot/Batch Capture for Traceable Products) |
| **Action Taken** | Close in-transit state and increase destination stock position on-hand and ATP. |
| **Resulting Command** | `ReceiveStock` (CMD-014) |

---

### POL-033 — Detect Network Imbalance Proactively

| Field | Detail |
|-------|--------|
| **Policy Name** | Detect Network Imbalance Proactively |
| **Triggering Domain Event** | NetworkImbalanceDetected (DE-073) |
| **Business Rule Applied** | BR-011 (Network Check Before Purchase), BR-012 (Protect Source Location Minimum) |
| **Action Taken** | Recommend redistribution transfers from excess locations to shortage locations before stockouts occur or procurement is initiated. |
| **Resulting Command** | `RequestStockTransfer` (CMD-045) *recommended to operations director* |

---

## Workflow 5: Inventory Accuracy & Control

---

### POL-034 — Impose Location Freeze on Wall-to-Wall Count

| Field | Detail |
|-------|--------|
| **Policy Name** | Impose Location Freeze on Wall-to-Wall Count |
| **Triggering Domain Event** | PhysicalInventoryCountStarted (DE-056) / LocationFreezeImposed (DE-007) |
| **Business Rule Applied** | BR-024 (Physical Inventory Freeze) |
| **Action Taken** | Block all receiving, shipping, transfers, and non-count adjustments at the location; notify warehouse staff of freeze. |
| **Resulting Command** | None *(block mutation commands at frozen location)* |

---

### POL-035 — Release Location Freeze on Count Certification

| Field | Detail |
|-------|--------|
| **Policy Name** | Release Location Freeze on Count Certification |
| **Triggering Domain Event** | PhysicalInventoryCountCertified (DE-057) / LocationFreezeReleased (DE-008) |
| **Business Rule Applied** | BR-024 (Physical Inventory Freeze) |
| **Action Taken** | Lift operational freeze and notify warehouse that normal receiving, shipping, and transfers may resume. |
| **Resulting Command** | None *(mutation commands permitted again)* |

---

### POL-036 — Open Variance Case on Count Discrepancy

| Field | Detail |
|-------|--------|
| **Policy Name** | Open Variance Case on Count Discrepancy |
| **Triggering Domain Event** | CycleCountCompleted (DE-053) OR PhysicalInventoryCountCertified (DE-057) *with variance* |
| **Business Rule Applied** | BR-018 (Blind Cycle Counting), BR-022 (Investigate Before Adjusting) |
| **Action Taken** | Calculate variance at submission without counter having seen expected quantity; open investigation case without directly mutating stock. |
| **Resulting Command** | `IdentifyCountVariance` (CMD-057) |

---

### POL-037 — Require Independent Approval for Count Variance

| Field | Detail |
|-------|--------|
| **Policy Name** | Require Independent Approval for Count Variance |
| **Triggering Domain Event** | CountVarianceIdentified (DE-054) |
| **Business Rule Applied** | BR-019 (Independent Count Approval), BR-022 (Investigate Before Adjusting) |
| **Action Taken** | Route variance to warehouse manager for root cause investigation; block stock adjustment until independent approver authorizes. |
| **Resulting Command** | `ApproveCountVariance` (CMD-053) *after investigation* |

---

### POL-038 — Submit Adjustment After Variance Approval

| Field | Detail |
|-------|--------|
| **Policy Name** | Submit Adjustment After Variance Approval |
| **Triggering Domain Event** | CountVarianceApproved (DE-055) |
| **Business Rule Applied** | BR-020 (Mandatory Adjustment Reason Codes), BR-021 (Independent Approval for Material Adjustments) |
| **Action Taken** | Create stock adjustment proposal with mandatory reason code and route through governance evaluation for final approval. |
| **Resulting Command** | `SubmitAdjustment` (CMD-054) |

---

### POL-039 — Evaluate Adjustment Governance on Submission

| Field | Detail |
|-------|--------|
| **Policy Name** | Evaluate Adjustment Governance on Submission |
| **Triggering Domain Event** | AdjustmentSubmitted (DE-058) |
| **Business Rule Applied** | BR-020 (Mandatory Adjustment Reason Codes), BR-021 (Independent Approval for Material Adjustments), BR-023 (Documented Write-Off Authorization) |
| **Action Taken** | Validate reason code, check approval threshold, and verify initiator is distinct from required approver before routing for authorization. |
| **Resulting Command** | `ApproveAdjustment` (CMD-055) OR `RejectAdjustment` (CMD-056) *by authorized approver* |

---

### POL-040 — Prioritize Class A Cycle Count Scheduling

| Field | Detail |
|-------|--------|
| **Policy Name** | Prioritize Class A Cycle Count Scheduling |
| **Triggering Domain Event** | ProductABCClassificationAssigned (DE-003) |
| **Business Rule Applied** | BR-032 (Class A Priority Monitoring) |
| **Action Taken** | Increase cycle count frequency and monitoring intensity for Class A products in the count schedule. |
| **Resulting Command** | `ScheduleCycleCount` (CMD-051) *at elevated frequency* |

---

### POL-041 — Block Mutations at Deactivated Location

| Field | Detail |
|-------|--------|
| **Policy Name** | Block Mutations at Deactivated Location |
| **Triggering Domain Event** | InventoryLocationDeactivated (DE-005) |
| **Business Rule Applied** | BR-024 (Physical Inventory Freeze) — *closure equivalent* |
| **Action Taken** | Prevent new receipts, reservations, fulfillments, and transfers at deactivated location; allow only authorized disposition activity. |
| **Resulting Command** | None *(block mutation commands)* |

---

### POL-042 — Record Movement History on Stock Mutation

| Field | Detail |
|-------|--------|
| **Policy Name** | Record Movement History on Stock Mutation |
| **Triggering Domain Event** | StockReceived (DE-011), StockShipped (DE-014), StockAdjusted (DE-015), StockWrittenOff (DE-016), StockReserved (DE-012), StockReservationReleased (DE-013) |
| **Business Rule Applied** | BR-017 (Lot/Batch Capture for Traceable Products) |
| **Action Taken** | Append immutable movement record documenting what changed, where, how much, by whom, and why for operational traceability. |
| **Resulting Command** | None *(InventoryMovementRecorded DE-074 raised automatically)* |

---

## Workflow 6: Returns Management

---

### POL-043 — Validate Return Authorization on Receipt

| Field | Detail |
|-------|--------|
| **Policy Name** | Validate Return Authorization on Receipt |
| **Triggering Domain Event** | CustomerReturnReceived (DE-063) |
| **Business Rule Applied** | BR-025 (Return Authorization Required), BR-004 (Verify Before Inventory Acceptance) |
| **Action Taken** | Match received goods to active RMA and original order; reject receipt if authorization is missing or expired. |
| **Resulting Command** | `InspectReturnedGoods` (CMD-064) *if validation passes* |

---

### POL-044 — Block Receipt on Expired Authorization

| Field | Detail |
|-------|--------|
| **Policy Name** | Block Receipt on Expired Authorization |
| **Triggering Domain Event** | ReturnAuthorizationExpired (DE-062) |
| **Business Rule Applied** | BR-025 (Return Authorization Required) |
| **Action Taken** | Prevent warehouse acceptance of goods against expired RMA; notify customer that return window has closed. |
| **Resulting Command** | None *(block `ReceiveCustomerReturn`)* |

---

### POL-045 — Restock Return on Passing Inspection

| Field | Detail |
|-------|--------|
| **Policy Name** | Restock Return on Passing Inspection |
| **Triggering Domain Event** | ReturnInspected (DE-064) — *resale quality confirmed* |
| **Business Rule Applied** | BR-026 (Inspect Returns Before Restocking) |
| **Action Taken** | Return qualifying goods to sellable inventory at receiving location. |
| **Resulting Command** | `RestockReturnedGoods` (CMD-065) → `ReceiveStock` (CMD-014) |

---

### POL-046 — Quarantine Return Pending Further Evaluation

| Field | Detail |
|-------|--------|
| **Policy Name** | Quarantine Return Pending Further Evaluation |
| **Triggering Domain Event** | ReturnInspected (DE-064) — *condition uncertain* |
| **Business Rule Applied** | BR-026 (Inspect Returns Before Restocking), BR-013 (Quarantine Exclusion from Sellable Stock) |
| **Action Taken** | Place returned goods under quarantine hold; exclude from sellable ATP pending quality team investigation. |
| **Resulting Command** | `QuarantineReturnedGoods` (CMD-066) |

---

### POL-047 — Write Off Non-Resalable Returns

| Field | Detail |
|-------|--------|
| **Policy Name** | Write Off Non-Resalable Returns |
| **Triggering Domain Event** | ReturnInspected (DE-064) — *damaged or defective* |
| **Business Rule Applied** | BR-026 (Inspect Returns Before Restocking), BR-023 (Documented Write-Off Authorization) |
| **Action Taken** | Permanently remove non-resalable returned goods from inventory value after inspection confirms disposition. |
| **Resulting Command** | `WriteOffReturnedGoods` (CMD-067) → `ApplyApprovedWriteOff` (CMD-017) |

---

### POL-048 — Notify Warehouse on Return Authorization

| Field | Detail |
|-------|--------|
| **Policy Name** | Notify Warehouse on Return Authorization |
| **Triggering Domain Event** | ReturnAuthorizationIssued (DE-061) |
| **Business Rule Applied** | BR-025 (Return Authorization Required) |
| **Action Taken** | Send return instructions to customer and advance notice to receiving clerk to expect inbound return shipment. |
| **Resulting Command** | None *(notification workflow — receiving awaits `ReceiveCustomerReturn`)* |

---

## Workflow 7: Commercial & Promotional

---

### POL-049 — Evaluate Promotional Readiness Before Campaign

| Field | Detail |
|-------|--------|
| **Policy Name** | Evaluate Promotional Readiness Before Campaign |
| **Triggering Domain Event** | PromotionalStockAllocated (DE-020) OR campaign deadline approaching |
| **Business Rule Applied** | BR-029 (Promotional Stock Ring-Fencing) |
| **Action Taken** | Compare ring-fenced quantity against campaign demand forecast; alert marketing and purchasing if readiness gap exists. |
| **Resulting Command** | `EvaluatePromotionalReadiness` (CMD-072) |

---

### POL-050 — Alert on Promotional Readiness Gap

| Field | Detail |
|-------|--------|
| **Policy Name** | Alert on Promotional Readiness Gap |
| **Triggering Domain Event** | PromotionalReadinessGapIdentified (DE-072) |
| **Business Rule Applied** | BR-029 (Promotional Stock Ring-Fencing) |
| **Action Taken** | Notify marketing manager and purchasing manager that campaign commitment is at risk due to insufficient ring-fenced stock. |
| **Resulting Command** | `AllocatePromotionalStock` (CMD-068) *increase allocation* OR `RecommendReplenishmentAction` (CMD-071) |

---

### POL-051 — Apply Updated Governance Thresholds

| Field | Detail |
|-------|--------|
| **Policy Name** | Apply Updated Governance Thresholds |
| **Triggering Domain Event** | GovernancePolicyPublished (DE-009) |
| **Business Rule Applied** | BR-021 (Independent Approval for Material Adjustments), BR-008 (Three-Way Match Before Payment), BR-006 (Document Receipt Discrepancies) |
| **Action Taken** | All subsequent adjustments, receipt verifications, and three-way match evaluations use the newly effective policy version. |
| **Resulting Command** | None *(policy consultation on next governed command)* |

---

### POL-052 — Retire Obsolete Reason Codes from Selection

| Field | Detail |
|-------|--------|
| **Policy Name** | Retire Obsolete Reason Codes from Selection |
| **Triggering Domain Event** | ReasonCodeRetired (DE-010) |
| **Business Rule Applied** | BR-020 (Mandatory Adjustment Reason Codes) |
| **Action Taken** | Remove retired reason code from active selection lists; block new adjustments or discrepancies from using retired codes. |
| **Resulting Command** | None *(validation on next `SubmitAdjustment` or `RecordReceiptDiscrepancy`)* |

---

## Workflow 8: Governance & Access Control

---

### POL-053 — Enforce Segregation of Duties on Approval

| Field | Detail |
|-------|--------|
| **Policy Name** | Enforce Segregation of Duties on Approval |
| **Triggering Domain Event** | *(Intercepts)* `ApproveCountVariance`, `ApproveAdjustment`, `ChangeRoleAssignment` |
| **Business Rule Applied** | BR-019 (Independent Count Approval), BR-021 (Independent Approval for Material Adjustments) |
| **Action Taken** | Block action when approver is the same person as counter or initiator; log accountability violation for audit review. |
| **Resulting Command** | `ValidateSegregationOfDuties` (CMD-078) → SegregationOfDutiesViolationDetected (DE-078) *on violation* |

---

### POL-054 — Record Audit Trail on Governed Change

| Field | Detail |
|-------|--------|
| **Policy Name** | Record Audit Trail on Governed Change |
| **Triggering Domain Event** | AdjustmentApproved (DE-059), ProductStatusChanged (DE-002), RoleAssignmentChanged (DE-080), GovernancePolicyPublished (DE-009), and other material mutations |
| **Business Rule Applied** | BR-019, BR-020, BR-021, BR-023 |
| **Action Taken** | Capture immutable before/after state, user identity, approval chain, and timestamp for compliance and control testing. |
| **Resulting Command** | None *(AuditTrailRecorded DE-075 raised automatically)* |

---

### POL-055 — Re-Evaluate SoD on Role Change

| Field | Detail |
|-------|--------|
| **Policy Name** | Re-Evaluate SoD on Role Change |
| **Triggering Domain Event** | RoleAssignmentChanged (DE-080) |
| **Business Rule Applied** | BR-019 (Independent Count Approval), BR-021 (Independent Approval for Material Adjustments) |
| **Action Taken** | Re-evaluate user's role combination for segregation-of-duties conflicts; block conflicting role assignments. |
| **Resulting Command** | `ValidateSegregationOfDuties` (CMD-078) |

---

### POL-056 — Block Mutations During Location Freeze

| Field | Detail |
|-------|--------|
| **Policy Name** | Block Mutations During Location Freeze |
| **Triggering Domain Event** | LocationFreezeImposed (DE-007) |
| **Business Rule Applied** | BR-024 (Physical Inventory Freeze) |
| **Action Taken** | Intercept receipt, shipment, transfer, and adjustment commands at frozen location; permit only authorized count-related activity. |
| **Resulting Command** | None *(block `VerifyGoodsReceipt`, `DispatchShipment`, `DispatchTransfer`, `SubmitAdjustment` at location)* |

---

### POL-057 — Notify Responsible Actor on Operational Alert

| Field | Detail |
|-------|--------|
| **Policy Name** | Notify Responsible Actor on Operational Alert |
| **Triggering Domain Event** | LowStockThresholdBreached (DE-068), InboundDeliveryDelayed (DE-029), InTransitStockDelayed (DE-051), FulfillmentExceptionRaised (DE-044), PromotionalReadinessGapIdentified (DE-072) |
| **Business Rule Applied** | BR-009 (Reorder at Reorder Level — same business day action) |
| **Action Taken** | Deliver timely notification to the responsible business actor (purchasing manager, buyer, warehouse manager, marketing manager) for action. |
| **Resulting Command** | None *(human responds with appropriate command)* |

---

### POL-058 — Investigate SoD Violation for Audit

| Field | Detail |
|-------|--------|
| **Policy Name** | Investigate SoD Violation for Audit |
| **Triggering Domain Event** | SegregationOfDutiesViolationDetected (DE-078) |
| **Business Rule Applied** | BR-019, BR-021 |
| **Action Taken** | Alert system administrator and internal auditor; record violation in audit trail for control testing and investigation. |
| **Resulting Command** | None *(audit review workflow)* |

---

## Workflow 9: Financial Alignment

---

### POL-059 — Prepare Valuation Snapshot at Period End

| Field | Detail |
|-------|--------|
| **Policy Name** | Prepare Valuation Snapshot at Period End |
| **Triggering Domain Event** | ThreeWayMatchCompleted (DE-035) OR month-end close cycle |
| **Business Rule Applied** | BR-008 (Three-Way Match Before Payment), BR-031 (Consignment Ownership at Consumption) |
| **Action Taken** | Aggregate owned stock quantities (excluding consignment, quarantined, and in-transit) with matched unit costs for finance reconciliation. |
| **Resulting Command** | `PrepareValuationSnapshot` (CMD-074) |

---

### POL-060 — Investigate Valuation Variance with Finance

| Field | Detail |
|-------|--------|
| **Policy Name** | Investigate Valuation Variance with Finance |
| **Triggering Domain Event** | ValuationVarianceIdentified (DE-077) |
| **Business Rule Applied** | BR-008 (Three-Way Match Before Payment), BR-031 (Consignment Ownership at Consumption) |
| **Action Taken** | Route operational-to-ledger misalignment to finance manager and inventory controller for joint investigation before month-end close. |
| **Resulting Command** | `ReconcileInventoryValuation` (CMD-075) |

---

### POL-061 — Update Valuation on Write-Off

| Field | Detail |
|-------|--------|
| **Policy Name** | Update Valuation on Write-Off |
| **Triggering Domain Event** | StockWrittenOff (DE-016) |
| **Business Rule Applied** | BR-023 (Documented Write-Off Authorization) |
| **Action Taken** | Reduce owned inventory value in valuation projections; include write-off in shrinkage and loss reporting for finance. |
| **Resulting Command** | None *(valuation read model projection updated)* |

---

### POL-062 — Exclude Quarantined Stock from Valuation

| Field | Detail |
|-------|--------|
| **Policy Name** | Exclude Quarantined Stock from Valuation |
| **Triggering Domain Event** | QuarantineHoldApplied (DE-017) |
| **Business Rule Applied** | BR-013 (Quarantine Exclusion from Sellable Stock), BR-031 (Consignment Ownership at Consumption) |
| **Action Taken** | Exclude quarantined quantity from sellable ATP and owned valuation snapshot until hold is released or dispositioned. |
| **Resulting Command** | None *(valuation projection rule applied)* |

---

## Workflow 10: Master Data & Reference

---

### POL-063 — Enable Stock Policy Assignment on Product Registration

| Field | Detail |
|-------|--------|
| **Policy Name** | Enable Stock Policy Assignment on Product Registration |
| **Triggering Domain Event** | ProductRegistered (DE-001) |
| **Business Rule Applied** | — |
| **Action Taken** | Make new SKU eligible for stock policy configuration, replenishment planning, and (when active) procurement and fulfillment. |
| **Resulting Command** | `UpdateStockPolicyThresholds` (CMD-011) *by inventory controller* |

---

### POL-064 — Establish Opening Balances on Location Activation

| Field | Detail |
|-------|--------|
| **Policy Name** | Establish Opening Balances on Location Activation |
| **Triggering Domain Event** | InventoryLocationActivated (DE-004) |
| **Business Rule Applied** | — |
| **Action Taken** | Load verified opening on-hand quantities for go-live location to establish authoritative inventory baseline. |
| **Resulting Command** | `EstablishOpeningBalances` (CMD-058) |

---

### POL-065 — Enable Put-Away on Storage Position Configuration

| Field | Detail |
|-------|--------|
| **Policy Name** | Enable Put-Away on Storage Position Configuration |
| **Triggering Domain Event** | StoragePositionConfigured (DE-006) |
| **Business Rule Applied** | BR-014 (FEFO), BR-015 (FIFO) |
| **Action Taken** | Make new storage address available for put-away placement and rotation-compliant pick path guidance. |
| **Resulting Command** | None *(next `CompletePutAway` may assign to position)* |

---

### POL-066 — Reject Procurement for Discontinued Products

| Field | Detail |
|-------|--------|
| **Policy Name** | Reject Procurement for Discontinued Products |
| **Triggering Domain Event** | PurchaseRequisitionSubmitted (DE-023) OR `PlacePurchaseOrder` attempted |
| **Business Rule Applied** | BR-027 (No Reorder of Discontinued Products) |
| **Action Taken** | Validate product eligibility before procurement proceeds; reject requisition or PO lines referencing discontinued SKUs. |
| **Resulting Command** | `RejectPurchaseRequisition` (CMD-023) OR block `PlacePurchaseOrder` |

---

## Policy Flow — Core Business Lifecycles

### Order-to-Cash Reaction Chain

```
CustomerOrderConfirmed
  → [POL-001] ReserveStock
    → StockReserved
      → [POL-021] EvaluateStockStatus

PickVerified
  → [POL-004] authorize DispatchShipment
    → ShipmentDispatched
      → [POL-005] ShipStock
        → StockShipped
          → [POL-028] TransferConsignmentOwnership (if consignment)
          → [POL-042] InventoryMovementRecorded
```

### Procure-to-Pay Reaction Chain

```
PurchaseOrderPlaced
  → [POL-020] ScheduleInboundDelivery

GoodsReceiptVerified
  → [POL-011] stage for CompletePutAway
  → [POL-013] ApplyQuarantineHold (if bonded)

PutAwayCompleted
  → [POL-012] ReceiveStock
    → [POL-021] EvaluateStockStatus
      → [POL-022] RecommendReplenishmentAction (if low)

SupplierInvoiceReceived
  → [POL-015] EvaluateThreeWayMatch
    → ThreeWayMatchCompleted
      → [POL-017] authorize payment
      → [POL-059] PrepareValuationSnapshot
```

### Count-to-Adjust Reaction Chain

```
CycleCountCompleted
  → [POL-036] IdentifyCountVariance
    → CountVarianceIdentified
      → [POL-037] route for ApproveCountVariance
        → CountVarianceApproved
          → [POL-038] SubmitAdjustment
            → [POL-039] governance evaluation
              → AdjustmentApproved
                → [POL-025] ApplyApprovedAdjustment
```

---

## Policy-to-Event-to-Command Matrix

| Policy | Trigger Event | Resulting Command(s) |
|--------|---------------|----------------------|
| POL-001 | DE-037 CustomerOrderConfirmed | ReserveStock |
| POL-002 | DE-038 CustomerOrderCancelled | ReleaseReservation |
| POL-005 | DE-040 ShipmentDispatched | ShipStock |
| POL-012 | DE-033 PutAwayCompleted | ReceiveStock |
| POL-022 | DE-068 LowStockThresholdBreached | RecommendReplenishmentAction |
| POL-025 | DE-059 AdjustmentApproved | ApplyApprovedAdjustment / ApplyApprovedWriteOff |
| POL-029 | DE-023 PurchaseRequisitionSubmitted | RequestStockTransfer / RejectPurchaseRequisition |
| POL-031 | DE-049 TransferDispatched | DispatchTransferStock |
| POL-032 | DE-050 TransferReceived | ReceiveStock |
| POL-036 | DE-053 CycleCountCompleted | IdentifyCountVariance |
| POL-045 | DE-064 ReturnInspected | RestockReturnedGoods |
| POL-053 | *(approval intercept)* | ValidateSegregationOfDuties |

---

## Excluded from Domain Policies

| Occurrence | Treatment | Rationale |
|------------|-----------|-----------|
| User views dashboard or report | Read model query | No reactive business workflow |
| User acknowledges alert without action | UI state only | Acknowledgment does not change inventory domain state |
| Command validation failure | Rejection response | No event raised — nothing to react to |
| Email/SMS delivery | Infrastructure | Delivery mechanism is not a business policy |
| Scheduled timer firing | Infrastructure signal | Policy reacts to the resulting domain event, not the timer |

---

## Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Domain Expert | | | |
| DDD Architect | | | |
| Senior Business Analyst | | | |
| Solution Architect | | | |

---

*End of Domain Policies*

*Document ID: SRS-ES-003 | Version 1.0 | July 6, 2026*
