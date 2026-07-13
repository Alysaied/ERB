# Event Storming Board
## Inventory Management System — Complete Business Lifecycle

---

## Document Information

| Attribute | Detail |
|-----------|--------|
| **Document ID** | SRS-ES-008 |
| **Document Title** | Event Storming Board — Inventory Management System |
| **Version** | 1.0 |
| **Status** | Draft |
| **Document Owner** | Domain Expert |
| **Source Documents** | SRS-ES-001 (Events), SRS-ES-002 (Commands), SRS-ES-003 (Policies), SRS-ES-004 (Actors), SRS-DM-003 (Aggregates) |
| **Date** | July 6, 2026 |

### Board Legend

```
┌─────────────┐
│   ACTOR     │  Human role or external system initiating action
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  COMMAND    │  Business intention (imperative verb)
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  AGGREGATE  │  Consistency boundary / transaction scope
└──────┬──────┘
       │
       ▼
┌─────────────┐
│DOMAIN EVENT │  Past-tense business fact (DE-xxx)
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   POLICY    │  Whenever [Event] then [Action] (POL-xxx)
└──────┬──────┘
       │
       ▼
   (next command in chain…)
```

| Symbol | Meaning |
|--------|---------|
| `[Actor]` | Business participant |
| `→ CMD` | Command issued |
| `⇒ AGG` | Target aggregate |
| `⇒ EVT` | Domain event raised |
| `⇒ POL` | Policy reaction |
| `┄┄┄` | Optional / conditional branch |
| `════` | Cross-aggregate reaction (eventual consistency) |

### Lifecycle Index

| Board | Lifecycle | Primary Actors |
|-------|-----------|----------------|
| 1 | Foundation & Go-Live | Inventory Controller |
| 2 | Replenishment Detection | System / Purchasing Manager |
| 3 | Procurement & Inbound Supply | Buyer → Receiving Clerk → Warehouse Staff → Finance Manager |
| 4 | Order Fulfillment | Sales Rep → CS Rep → Picker |
| 5 | Partial Fulfillment & Backorder | Customer Service Representative |
| 6 | Network Transfer | Regional Manager → Operations Director → Warehouse Staff |
| 7 | Cycle Count & Adjustment | Warehouse Staff → Warehouse Manager → Operations Director |
| 8 | Physical Inventory Count | Inventory Controller |
| 9 | Customer Returns | CS Rep → Receiving Clerk → Warehouse Manager |
| 10 | Promotional Campaign | Marketing Manager |
| 11 | Quarantine & Hold | Warehouse Manager |
| 12 | Finance & Valuation Close | Finance Manager |

---

## Master Board — End-to-End Business Lifecycle

```
═══════════════════════════════════════════════════════════════════════════════
 PHASE 1: FOUNDATION
═══════════════════════════════════════════════════════════════════════════════
 Inventory Controller
   → RegisterProduct              ⇒ Product Catalog        ⇒ ProductRegistered
   → ActivateInventoryLocation    ⇒ Inventory Location     ⇒ InventoryLocationActivated
     ⇒ POL-064: Establish Opening Balances
   → EstablishOpeningBalances     ⇒ Stock Position         ⇒ StockReceived
   → UpdateStockPolicyThresholds  ⇒ Stock Policy           ⇒ StockPolicyThresholdChanged
   → PublishGovernancePolicy      ⇒ Inventory Governance   ⇒ GovernancePolicyPublished

═══════════════════════════════════════════════════════════════════════════════
 PHASE 2: REPLENISHMENT & INBOUND SUPPLY
═══════════════════════════════════════════════════════════════════════════════
 [Low stock detected]
   ⇒ Stock Position               ⇒ LowStockThresholdBreached
     ⇒ POL-022: Trigger Replenishment
   → RecommendReplenishmentAction ⇒ (Domain Service)       ⇒ ReplenishmentRecommended

 Purchasing Manager / Buyer
   → SubmitPurchaseRequisition    ⇒ Purchase Requisition   ⇒ PurchaseRequisitionSubmitted
     ⇒ POL-029: Evaluate Network Before Procurement
   → ApprovePurchaseRequisition   ⇒ Purchase Requisition   ⇒ PurchaseRequisitionApproved
     ⇒ POL-019: Convert to PO
   → PlacePurchaseOrder           ⇒ Purchase Order         ⇒ PurchaseOrderPlaced
     ⇒ POL-020: Schedule Inbound
   → ScheduleInboundDelivery      ⇒ Purchase Order         ⇒ InboundDeliveryScheduled

 Supplier (external) delivers goods
 Receiving Clerk
   → VerifyGoodsReceipt           ⇒ Goods Receipt          ⇒ GoodsReceiptVerified
     ⇒ POL-011: Stage for Put-Away
 Warehouse Staff
   → CompletePutAway              ⇒ Goods Receipt          ⇒ PutAwayCompleted
     ⇒ POL-012: Activate Stock
   → ReceiveStock                 ⇒ Stock Position         ⇒ StockReceived
     ⇒ POL-021: Reclassify Stock Status

 Finance Manager
   → RecordSupplierInvoice        ⇒ Supplier Invoice       ⇒ SupplierInvoiceReceived
     ⇒ POL-015: Evaluate Match
   → EvaluateThreeWayMatch        ⇒ Supplier Invoice       ⇒ ThreeWayMatchCompleted
     ⇒ POL-017: Authorize Payment

═══════════════════════════════════════════════════════════════════════════════
 PHASE 3: ORDER FULFILLMENT
═══════════════════════════════════════════════════════════════════════════════
 Sales Representative
   → ConfirmOrderAvailability     ⇒ Customer Order         ⇒ OrderAvailabilityConfirmed
 Customer Service Representative
   → ConfirmCustomerOrder           ⇒ Customer Order         ⇒ CustomerOrderConfirmed
     ⇒ POL-001: Reserve Stock
   → ReserveStock                   ⇒ Stock Position         ⇒ StockReserved
 Warehouse Picker
   → VerifyPick                     ⇒ Customer Order         ⇒ PickVerified
     ⇒ POL-004: Authorize Shipment
   → DispatchShipment               ⇒ Customer Order         ⇒ ShipmentDispatched
     ⇒ POL-005: Deduct Stock
   → ShipStock                      ⇒ Stock Position         ⇒ StockShipped
 Logistics / Carrier (external) picks up

═══════════════════════════════════════════════════════════════════════════════
 PHASE 4: INVENTORY CONTROL & RETURNS (parallel ongoing operations)
═══════════════════════════════════════════════════════════════════════════════
 Cycle Count path ──► CountVarianceIdentified ──► AdjustmentApproved ──► StockAdjusted
 Transfer path    ──► TransferRequested ──► TransferApproved ──► TransferReceived ──► StockReceived
 Returns path     ──► ReturnAuthorizationIssued ──► ReturnInspected ──► ReturnRestocked ──► StockReceived

═══════════════════════════════════════════════════════════════════════════════
 PHASE 5: FINANCIAL CLOSE
═══════════════════════════════════════════════════════════════════════════════
 Finance Manager
   → PrepareValuationSnapshot     ⇒ Valuation Snapshot     ⇒ InventoryValuationSnapshotPrepared
   → ReconcileInventoryValuation  ⇒ Valuation Snapshot     ⇒ ValuationVarianceIdentified (if mismatch)
```

---

## Board 1 — Foundation & Go-Live

**Business Process:** BP-01, BP-02, BP-03 | **Use Cases:** UC-001, UC-002, UC-003, UC-005, UC-046

```
[Inventory Controller]
        │
        ▼
→ RegisterProduct ──────────────────────⇒ [Product Catalog]
        │                                        │
        │                                        ▼
        │                                 ProductRegistered (DE-001)
        │                                        │
        │                                        ▼
        │                                 POL-063: Enable Stock Policy Assignment
        │                                        │
        │                                        ▼
        │                          [Inventory Controller]
        │                                        │
        │                                        ▼
        │                          → UpdateStockPolicyThresholds
        │                                        │
        │                                        ▼
        │                                 [Stock Policy]
        │                                        │
        │                                        ▼
        │                          StockPolicyThresholdChanged (DE-019)
        │
        ▼
→ AssignABCClassification ──────────────⇒ [Product Catalog]
        │                                        │
        │                                        ▼
        │                    ProductABCClassificationAssigned (DE-003)
        │                                        │
        │                                        ▼
        │                                 POL-040: Prioritize Class A Count Scheduling
        │
        ▼
→ ConfigureStoragePosition ───────────⇒ [Inventory Location]
        │                                        │
        │                                        ▼
        │                          StoragePositionConfigured (DE-006)
        │
        ▼
→ EstablishOpeningBalances ───────────⇒ [Stock Position]  *(per product line)*
        │                                        │
        │                                        ▼
        │                                 StockReceived (DE-011)
        │
        ▼
→ ActivateInventoryLocation ──────────⇒ [Inventory Location]
                                                 │
                                                 ▼
                                  InventoryLocationActivated (DE-004)

[Inventory Controller]
        │
        ▼
→ PublishGovernancePolicy ──────────────⇒ [Inventory Governance]
        │                                        │
        │                                        ▼
        │                          GovernancePolicyPublished (DE-009)
        │                                        │
        │                                        ▼
        │                                 POL-051: Apply Updated Governance Thresholds
```

---

## Board 2 — Replenishment Detection & Planning

**Business Process:** BP-21, BP-22 | **Use Cases:** UC-012, UC-028, UC-029

```
[Stock Position quantity changes from any lifecycle]
        │
        ▼
→ EvaluateStockStatus ──────────────────⇒ [Stock Position]  *(domain service)*
        │
        ├──────────────────────────────────────────────────────────┐
        ▼                                                          ▼
 LowStockThresholdBreached (DE-068)              OutOfStockDetected (DE-069)
        │                                                          │
        ▼                                                          ▼
 POL-022: Trigger Replenishment on Low Stock      POL-023: Escalate Out-of-Stock Urgently
        │                                                          │
        ▼                                                          ▼
→ RecommendReplenishmentAction ─────────⇒ (Domain Service)
        │
        ▼
 ReplenishmentRecommended (DE-071)
        │
        ├────────────────────────────┬─────────────────────────────┐
        ▼                            ▼                             ▼
 [Purchasing Manager]        [Regional / Store Manager]     [Buyer]
 reviews alert              may request transfer            creates requisition
        │                            │                             │
        │                            │                             ▼
        │                            │              → SubmitPurchaseRequisition
        │                            │                             │
        │                            │                             ▼
        │                            │              [Purchase Requisition]
        │                            │                             │
        │                            │                             ▼
        │                            │         PurchaseRequisitionSubmitted (DE-023)
        │                            │                             │
        │                            │                             ▼
        │                            │         POL-029: Evaluate Network Before Procurement
        │                            │                             │
        │                            └─────────────┬───────────────┘
        │                                          ▼
        │                            ┌── Recommend transfer (POL-033)
        │                            └── Or proceed to procurement (Board 3)
        ▼
 [Network imbalance detected separately]
        │
        ▼
 NetworkImbalanceDetected (DE-073)
        │
        ▼
 POL-033: Detect Network Imbalance → recommend RequestStockTransfer (Board 6)
```

---

## Board 3 — Procurement & Inbound Supply (Complete)

**Business Process:** BP-05 → BP-09, BP-30 | **Use Cases:** UC-006 – UC-010, UC-039

```
[Purchasing Manager]
        │
        ▼
→ ApprovePurchaseRequisition ───────────⇒ [Purchase Requisition]
        │                                        │
        │                                        ▼
        │                    PurchaseRequisitionApproved (DE-024)
        │                                        │
        │                                        ▼
        │                                 POL-019: Convert Approved Requisition to PO
        │                                        │
        ▼                                        ▼
[Buyer]                              → PlacePurchaseOrder
        │                                        │
        ▼                                        ▼
                                 [Purchase Order]
        │                                        │
        │                                        ▼
        │                          PurchaseOrderPlaced (DE-026)
        │                                        │
        │                                        ▼
        │                                 POL-020: Plan Inbound Delivery
        │                                        │
        │                                        ▼
        │                          → ScheduleInboundDelivery
        │                                        │
        │                                        ▼
        │                          InboundDeliveryScheduled (DE-028)
        │                                        │
        │                          ┌─────────────┴─────────────┐
        │                          ▼                           ▼
        │               [Receiving Clerk notified]    [Buyer tracks supply]
        │                          │                           │
        │               ┌──────────┴──────────┐                ▼
        │               ▼                     ▼     InboundDeliveryDelayed (DE-029)
        │        On-time delivery      Delay reported          │
        │               │                     │                ▼
        ▼               ▼                     ▼         POL-057: Notify Responsible Actor
→ RecordInboundDelay    │                     │
 (if delayed)           │                     │
                        ▼                     ▼
[Receiving Clerk]
        │
        ▼
→ VerifyGoodsReceipt ───────────────────⇒ [Goods Receipt]
        │                                        │
        ├────────────────────────────────────────┤
        ▼                                        ▼
  (discrepancy found)                  GoodsReceiptVerified (DE-030)
        │                                        │
        ▼                                        ├────────────────────────────┐
→ RecordReceiptDiscrepancy                        ▼                            ▼
        │                                 POL-011: Stage for Put-Away    POL-013: Hold Bonded Stock
        ▼                                        │                     (if bonded)
 ReceiptDiscrepancyRecorded (DE-031)             │                            │
        │                                        │                            ▼
        ▼                                        │              → ApplyQuarantineHold
[Warehouse Manager]                              │                            │
        │                                        │                            ▼
        ▼                                        │              QuarantineHoldApplied (DE-017)
→ ResolveReceiptDiscrepancy                      │
        │                                        ▼
        ▼                               [Warehouse Staff]
 ReceiptDiscrepancyResolved (DE-032)            │
                                                 ▼
                                    → CompletePutAway
                                                 │
                                                 ▼
                                      [Goods Receipt]
                                                 │
                                                 ▼
                                    PutAwayCompleted (DE-033)
                                                 │
                                                 ▼
                                      POL-012: Activate Stock on Put-Away
                                                 │
                                                 ▼
                                    → ReceiveStock ══════════════⇒ [Stock Position]
                                                 │                        │
                                                 ▼                        ▼
                                        (handoff complete)      StockReceived (DE-011)
                                                                        │
                                                                        ▼
                                                                 POL-021: Reclassify Stock Status
                                                                        │
                                                                        ▼
                                                                 → EvaluateStockStatus
                                                                        │
                                                                        ▼
                                                                 LowStockThresholdBreached / etc.
                                                                        │
                                                                        ▼
                                                                 POL-008: Fulfill Backorder When Stock Arrives
                                                                        │
                                                                        ▼
                                                                 → FulfillBackorder (if backorders pending)

══════════════════════ FINANCE LEG ══════════════════════

[Finance Manager]
        │
        ▼
→ RecordSupplierInvoice ────────────────⇒ [Supplier Invoice]
        │                                        │
        │                                        ▼
        │                    SupplierInvoiceReceived (DE-034)
        │                                        │
        │                                        ▼
        │                                 POL-015: Evaluate Three-Way Match
        │                                        │
        │                                        ▼
        │                          → EvaluateThreeWayMatch
        │                                        │
        │                          ┌─────────────┴─────────────┐
        │                          ▼                           ▼
        │            ThreeWayMatchCompleted (DE-035)   ThreeWayMatchExceptionRaised (DE-081)
        │                          │                           │
        │                          ▼                           ▼
        │                   POL-017: Authorize Payment   POL-018: Block Payment
        │                          │                           │
        │                          ▼                           ▼
        │                   POL-059: Prepare Valuation    [Finance + Purchasing resolve]
        │                          │
        │                          ▼
        │               → PrepareValuationSnapshot
        │                          │
        │                          ▼
        │        InventoryValuationSnapshotPrepared (DE-076)
```

---

## Board 4 — Order Fulfillment (Complete)

**Business Process:** BP-16 → BP-18 | **Use Cases:** UC-013, UC-021 – UC-024

```
[Sales Representative]
        │
        ▼
→ ConfirmOrderAvailability ─────────────⇒ [Customer Order Fulfillment]
        │                                        │
        │                                        ▼
        │                    OrderAvailabilityConfirmed (DE-036)
        │
        ▼
[Customer Service Representative]
        │
        ▼
→ ConfirmCustomerOrder ───────────────────⇒ [Customer Order Fulfillment]
        │                                        │
        │                                        ▼
        │                    CustomerOrderConfirmed (DE-037)
        │                                        │
        │                                        ▼
        │                                 POL-001: Reserve Stock on Order Confirmation
        │                                        │
        │                                        ▼
        │                          → ReserveStock ══════════════⇒ [Stock Position]
        │                                        │                        │
        │                                        │                        ▼
        │                                        │              StockReserved (DE-012)
        │                                        │                        │
        │                                        │                        ▼
        │                                        │                 POL-021: Reclassify Stock Status
        │                                        ▼
        │                          [Warehouse Picker — fulfillment queue]
        │                                        │
        │                                        ▼
        │                          → VerifyPick
        │                                        │
        │                                        ▼
        │                                 [Customer Order Fulfillment]
        │                                        │
        │                                        ▼
        │                              PickVerified (DE-039)
        │                                        │
        │                                        ▼
        │                                 POL-004: Require Verified Pick Before Shipment
        │                                        │
        │                                        ▼
        │                          → DispatchShipment
        │                                        │
        │                                        ▼
        │                    ShipmentDispatched (DE-040)
        │                                        │
        │                                        ▼
        │                                 POL-005: Deduct Stock on Shipment
        │                                        │
        │                                        ▼
        │                          → ShipStock ══════════════════⇒ [Stock Position]
        │                                        │                        │
        │                                        │                        ▼
        │                                        │              StockShipped (DE-014)
        │                                        │                        │
        │                                        │                        ├─────────────────────┐
        │                                        │                        ▼                     ▼
        │                                        │                 POL-042: Record Movement  POL-028: Transfer Consignment Ownership
        │                                        │                        │                (if consignment)
        │                                        │                        ▼
        │                                        │           InventoryMovementRecorded (DE-074)
        │                                        ▼
        │                          [Customer / CS Rep notified of shipment]
        │
        ┄┄┄ CANCELLATION BRANCH ┄┄┄
[Customer Service Representative]
        │
        ▼
→ CancelCustomerOrder ────────────────────⇒ [Customer Order Fulfillment]
        │                                        │
        │                                        ▼
        │                    CustomerOrderCancelled (DE-038)
        │                                        │
        │                                        ▼
        │                                 POL-002: Release Reservation on Cancellation
        │                                        │
        │                                        ▼
        │                          → ReleaseReservation ════════⇒ [Stock Position]
        │                                        │                        │
        │                                        │                        ▼
        │                                        │         StockReservationReleased (DE-013)
```

---

## Board 5 — Partial Fulfillment, Backorder & Multi-Location

**Business Process:** BP-19 | **Use Cases:** UC-025, UC-048

```
[Customer Service Representative]
        │
        ▼
→ ConfirmCustomerOrder ───────────────────⇒ [Customer Order Fulfillment]
        │   *(insufficient ATP for full quantity)*
        │                                        │
        │                                        ▼
        │                    CustomerOrderConfirmed (DE-037)
        │                                        │
        ▼                                        ▼
→ CompletePartialFulfillment              POL-001: Reserve Stock (partial qty)
        │                                        │
        ▼                                        ▼
 [Customer Order Fulfillment]          → ReserveStock (partial) ⇒ StockReserved
        │
        ▼
 PartialFulfillmentCompleted (DE-041)
        │
        ├────────────────────────────────────────┐
        ▼                                        ▼
 POL-006: Record Partial Fulfillment      Ship available portion
        │                                        │
        ▼                                        ▼
→ RecordBackorder                          → DispatchShipment
        │                                        │
        ▼                                        ▼
 BackorderRecorded (DE-042)              ShipmentDispatched (DE-040) → … → StockShipped
        │
        ▼
 POL-007: Prioritize Backorder Replenishment
        │
        ▼
→ RecommendReplenishmentAction ⇒ ReplenishmentRecommended (DE-071)

┄┄┄ WHEN STOCK ARRIVES (links to Board 3 / POL-008) ┄┄┄
 StockReceived (DE-011)
        │
        ▼
 POL-008: Fulfill Backorder When Stock Arrives
        │
        ▼
→ FulfillBackorder
        │
        ▼
 BackorderFulfilled (DE-043)
        │
        ▼
 POL-001 → ReserveStock → … → DispatchShipment → StockShipped

══════════════════════ MULTI-LOCATION BRANCH ══════════════════════

[Warehouse Manager]
        │
        ▼
→ CreateMultiLocationFulfillmentPlan ───⇒ [Customer Order Fulfillment]
        │                                        │
        │                                        ▼
        │         MultiLocationFulfillmentPlanCreated (DE-045)
        │                                        │
        │                                        ▼
        │                                 POL-003: Allocate Multi-Location Reservations
        │                                        │
        │                                        ▼
        │                          → ReserveStock (per location) ⇒ StockReserved × N
        │                                        │
        └────────────────────────────────────────┘
                          (continues pick/ship per location on Board 4)
```

---

## Board 6 — Network Transfer (Complete)

**Business Process:** BP-24, BP-25 | **Use Cases:** UC-031 – UC-033

```
[Regional / Store Manager]
        │
        ▼
→ RequestStockTransfer ─────────────────⇒ [Stock Transfer]
        │                                        │
        │                                        ▼
        │                    TransferRequested (DE-046)
        │                                        │
        │                                        ▼
        │                                 POL-030: Validate Source Capacity
        │                                        │
        ▼                                        ▼
[Operations Director]
        │
        ├─────────────────────┬─────────────────────┐
        ▼                     ▼                     ▼
→ ApproveTransferRequest  → RejectTransferRequest   │
        │                     │                     │
        ▼                     ▼                     │
 [Stock Transfer]      [Stock Transfer]              │
        │                     │                     │
        ▼                     ▼                     │
 TransferApproved (DE-047)  TransferRejected (DE-048)│
        │                                            │
        ▼                                            ▼
 [Warehouse Staff — source]              [Regional Manager notified]
        │
        ▼
→ DispatchTransfer ─────────────────────⇒ [Stock Transfer]
        │                                        │
        │                                        ▼
        │                    TransferDispatched (DE-049)
        │                                        │
        │                                        ▼
        │                                 POL-031: Deduct Source Stock
        │                                        │
        │                                        ▼
        │                          → DispatchTransferStock ══⇒ [Stock Position — source]
        │                                        │
        │                          ┌─────────────┴─────────────┐
        │                          ▼                           ▼
        │               InventoryMovementRecorded    InTransitStockDelayed (DE-051)
        │               (DE-074)                              │
        │                                                     ▼
        │                                              POL-057: Notify Actor
        ▼
 [Warehouse Staff — destination]
        │
        ▼
→ ConfirmTransferReceipt ───────────────⇒ [Stock Transfer]
        │                                        │
        │                                        ▼
        │                    TransferReceived (DE-050)
        │                                        │
        │                                        ▼
        │                                 POL-032: Increase Destination Stock
        │                                        │
        │                                        ▼
        │                          → ReceiveStock ══════════════⇒ [Stock Position — destination]
        │                                        │                        │
        │                                        │                        ▼
        │                                        │              StockReceived (DE-011)
        │                                        │                        │
        │                                        │                        ▼
        │                                        │                 POL-021: Reclassify Stock Status
```

---

## Board 7 — Cycle Count & Adjustment (Complete)

**Business Process:** BP-11, BP-13, BP-14 | **Use Cases:** UC-014, UC-016, UC-017, UC-018

```
[Inventory Controller]
        │
        ▼
→ ScheduleCycleCount ───────────────────⇒ [Cycle Count]
        │                                        │
        │                                        ▼
        │                    CycleCountScheduled (DE-052)
        │
        ▼
[Warehouse Staff]
        │
        ▼
→ SubmitCycleCountResult ───────────────⇒ [Cycle Count]
        │                                        │
        │                                        ▼
        │                    CycleCountCompleted (DE-053)
        │                                        │
        │                          ┌─────────────┴─────────────┐
        │                          ▼                           ▼
        │                   (no variance)              (variance exists)
        │                   count closed                      │
        │                                                     ▼
        │                                          POL-036: Open Variance Case
        │                                                     │
        │                                                     ▼
        │                                          → IdentifyCountVariance
        │                                                     │
        │                                                     ▼
        │                                          [Inventory Adjustment Case]
        │                                                     │
        │                                                     ▼
        │                                    CountVarianceIdentified (DE-054)
        │                                                     │
        │                                                     ▼
        │                                          POL-037: Require Independent Approval
        │                                                     │
        ▼                                                     ▼
[Warehouse Manager]                              → ApproveCountVariance
        │                                                     │
        │                                                     ▼
        │                                    CountVarianceApproved (DE-055)
        │                                                     │
        │                                                     ▼
        │                                          POL-038: Submit Adjustment After Approval
        │                                                     │
        │                                                     ▼
        │                                          → SubmitAdjustment
        │                                                     │
        │                                                     ▼
        │                                    AdjustmentSubmitted (DE-058)
        │                                                     │
        │                                                     ▼
        │                                          POL-039: Evaluate Adjustment Governance
        │                                                     │
        │                                                     ▼
        │                                          POL-053: Enforce Segregation of Duties
        │                                                     │
        ▼                                                     ▼
[Operations Director]
        │
        ├─────────────────────┬─────────────────────┐
        ▼                     ▼                     │
→ ApproveAdjustment    → RejectAdjustment           │
        │                     │                     │
        ▼                     ▼                     │
 [Adjustment Case]     [Adjustment Case]             │
        │                     │                     │
        ▼                     ▼                     │
 AdjustmentApproved     AdjustmentRejected          │
 (DE-059)               (DE-060)                    │
        │                                            │
        ▼                                            │
 POL-025: Apply Adjustment on Approval              │
        │                                            │
        ├────────────────────┬───────────────────────┘
        ▼                    ▼
→ ApplyApprovedAdjustment  → ApplyApprovedWriteOff
        │                    │
        ▼                    ▼
 [Stock Position]      [Stock Position]
        │                    │
        ▼                    ▼
 StockAdjusted          StockWrittenOff
 (DE-015)               (DE-016)
        │                    │
        └────────┬───────────┘
                 ▼
          POL-042: Record Movement History
                 │
                 ▼
   InventoryMovementRecorded (DE-074)
                 │
                 ▼
          POL-054: Record Audit Trail
                 │
                 ▼
        AuditTrailRecorded (DE-075)
```

---

## Board 8 — Physical Inventory Count & Location Freeze

**Business Process:** BP-12 | **Use Cases:** UC-015

```
[Inventory Controller]
        │
        ▼
→ StartPhysicalInventoryCount ──────────⇒ [Physical Inventory Count]
        │                                        │
        │                                        ├────────────────────────────┐
        │                                        ▼                            ▼
        │               PhysicalInventoryCountStarted (DE-056)   LocationFreezeImposed (DE-007)
        │                                        │                            │
        │                                        │                            ▼
        │                                        │                     POL-034: Impose Location Freeze
        │                                        │                            │
        │                                        │                            ▼
        │                                        │              → Apply freeze on [Inventory Location]
        │                                        │                            │
        │                                        │                            ▼
        │                                        │                     POL-056: Block Mutations During Freeze
        │                                        │                     (blocks receipt, ship, transfer, adjust)
        │                                        ▼
        │                          [Count teams perform wall-to-wall count]
        │                                        │
        ▼                                        ▼
→ CertifyPhysicalInventoryCount
        │
        ├────────────────────────────────────────┐
        ▼                                        ▼
 [Physical Inventory Count]          LocationFreezeReleased (DE-008)
        │                                        │
        ▼                                        ▼
 PhysicalInventoryCountCertified      POL-035: Release Location Freeze
 (DE-057)                                      │
        │                                        ▼
        ▼                               [Normal operations resume]
 POL-036: Open Variance Case (per line)
        │
        ▼
 CountVarianceIdentified (DE-054) ──► continues on Board 7
```

---

## Board 9 — Customer Returns (Complete)

**Business Process:** BP-27, BP-28 | **Use Cases:** UC-035, UC-036

```
[Customer Service Representative]
        │
        ▼
→ IssueReturnAuthorization ─────────────⇒ [Customer Return Case]
        │                                        │
        │                                        ▼
        │                    ReturnAuthorizationIssued (DE-061)
        │                                        │
        │                                        ▼
        │                                 POL-048: Notify Warehouse on Return Authorization
        │                                        │
        ├────────────────────────────────────────┤
        │                          ┌─────────────┴─────────────┐
        │                          ▼                           ▼
        │               [Customer ships return]     (window expires)
        │                          │                           │
        ▼                          │                           ▼
[Receiving Clerk]                  │              ReturnAuthorizationExpired (DE-062)
        │                          │                           │
        ▼                          │                           ▼
→ ReceiveCustomerReturn            │                    POL-044: Block Receipt on Expired RMA
        │                          │
        ▼                          │
 [Customer Return Case]            │
        │                          │
        ▼                          │
 CustomerReturnReceived (DE-063)    │
        │                          │
        ▼                          │
 POL-043: Validate Return Authorization
        │                          │
        ▼                          │
→ InspectReturnedGoods             │
        │                          │
        ▼                          │
 ReturnInspected (DE-064)           │
        │                          │
        ├──────────────┬───────────┴───────────┐
        ▼              ▼                       ▼
  (resale quality)  (uncertain)          (damaged/defective)
        │              │                       │
        ▼              ▼                       ▼
 POL-045: Restock  POL-046: Quarantine   POL-047: Write Off
        │              │                       │
        ▼              ▼                       ▼
→ RestockReturned  → QuarantineReturned  → WriteOffReturned
        │              │                       │
        ▼              ▼                       ▼
 ReturnRestocked   ReturnQuarantined    ReturnWrittenOff
 (DE-065)          (DE-066)             (DE-067)
        │              │                       │
        ▼              ▼                       ▼
→ ReceiveStock     → ApplyQuarantineHold  → ApplyApprovedWriteOff
        │              │                       │
        ▼              ▼                       ▼
 StockReceived      QuarantineHoldApplied  StockWrittenOff
 (DE-011)           (DE-017)               (DE-016)
```

---

## Board 10 — Promotional Campaign

**Business Process:** BP-31 | **Use Cases:** UC-040

```
[Marketing Manager]
        │
        ▼
→ AllocatePromotionalStock ─────────────⇒ [Promotional Stock Allocation]
        │                                        │
        │                                        ▼
        │                    PromotionalStockAllocated (DE-020)
        │                                        │
        │                          ┌─────────────┴─────────────┐
        │                          ▼                           ▼
        │                   POL-026: Segregate ATP      POL-049: Evaluate Promotional Readiness
        │                   on Stock Position                    │
        │                          │                           ▼
        │                          ▼               → EvaluatePromotionalReadiness
        │               (ATP reduced for               │
        │                ring-fenced qty)              ▼
        │                                   PromotionalReadinessGapIdentified (DE-072)
        │                                              │
        │                                              ▼
        │                                   POL-050: Alert on Readiness Gap
        │                                              │
        ▼                                              ▼
 [Campaign runs — orders consume promotional pool]   [Marketing + Purchasing act]
        │
        ▼
 [Marketing Manager — campaign end]
        │
        ▼
→ ReleasePromotionalAllocation ─────────⇒ [Promotional Stock Allocation]
        │                                        │
        │                                        ▼
        │                    PromotionalAllocationReleased (DE-021)
        │                                        │
        │                                        ▼
        │                                 POL-027: Restore General ATP
        │                                        │
        │                                        ▼
        │                          (unconsumed qty returns to general ATP)
```

---

## Board 11 — Quarantine & Hold Management

**Business Process:** BP-14, BP-20 | **Use Cases:** UC-019

```
[Warehouse Manager]
        │
        ├────────────────────────────┬────────────────────────────┐
        ▼                            ▼                            ▼
→ ApplyQuarantineHold          → ReleaseQuarantineHold      (from return path)
 (quality/recall/customs)       (after clearance/approval)
        │                            │
        ▼                            ▼
 [Stock Position]              [Stock Position]
        │                            │
        ▼                            ▼
 QuarantineHoldApplied        QuarantineHoldReleased
 (DE-017)                     (DE-018)
        │                            │
        ▼                            ▼
 POL-062: Exclude from        (ATP restored;
 Valuation Snapshot            put-away may proceed
        │                     for bonded — POL-013)
        ▼
 (quantity excluded from
  sellable ATP and
  owned valuation)
```

---

## Board 12 — Fulfillment Exception Path

**Business Process:** BP-20 | **Use Cases:** UC-026

```
[Warehouse Manager]
        │
        ▼
→ RaiseFulfillmentException ────────────⇒ [Customer Order Fulfillment]
        │                                        │
        │                                        ▼
        │                    FulfillmentExceptionRaised (DE-044)
        │                                        │
        │                                        ▼
        │                                 POL-009: Escalate Fulfillment Exception
        │                                        │
        │                          ┌─────────────┴─────────────┐
        │                          ▼                           ▼
        │               (shelf mismatch)              (quality issue)
        │                          │                           │
        │                          ▼                           ▼
        │               → IdentifyCountVariance        → ApplyQuarantineHold
        │               (Board 7)                      (Board 11)
        │                          │                           │
        └──────────────────────────┴───────────────────────────┘
                                   ▼
                          POL-057: Notify Responsible Actor
```

---

## Board 13 — Governance & Access Control

**Business Process:** Cross-cutting | **Use Cases:** UC-044, UC-045

```
[System Administrator]
        │
        ▼
→ ProvisionUserAccount ─────────────────⇒ [User Account]
        │                                        │
        │                                        ▼
        │                    UserAccountProvisioned (DE-079)
        │
        ▼
→ ChangeRoleAssignment ─────────────────⇒ [User Account]
        │                                        │
        │                                        ▼
        │                    RoleAssignmentChanged (DE-080)
        │                                        │
        │                                        ▼
        │                                 POL-055: Re-Evaluate SoD on Role Change
        │
        ┄┄┄ INTERCEPTS ALL APPROVAL COMMANDS ┄┄┄
        │
        ▼
→ ValidateSegregationOfDuties ────────⇒ [User Account]
   *(on ApproveCountVariance,            │
     ApproveAdjustment,                  ├──── (violation)
     ChangeRoleAssignment)*               │         │
        │                                 │         ▼
        │ (passes)                        │  SegregationOfDutiesViolationDetected
        │                                 │         (DE-078)
        ▼                                 │         │
 approval proceeds                        │         ▼
 on target aggregate                      │  POL-058: Investigate SoD Violation
```

---

## Complete Lifecycle Swimlane — Chronological Summary

```
TIME ──────────────────────────────────────────────────────────────────────────►

FOUNDATION     REPLENISH        INBOUND           FULFILLMENT        CONTROL
    │              │               │                  │                 │
    │         LowStock           PO placed          Order            Cycle Count
    │         detected           Receipt            confirmed        Variance
    │              │               │                  │                 │
    ▼              ▼               ▼                  ▼                 ▼
 Product      Requisition      PutAway           ReserveStock      Adjustment
 Location     → PO             completed         → Pick            approved
 activated    → Receipt        → StockReceived   → Ship            → StockAdjusted
 → Opening    → Match          → ATP updated     → StockShipped
   balances

     │                                                    │
     └────────────────── STOCK POSITION (central) ──────────┘
              on-hand │ reserved │ ATP │ quarantine │ status

RETURNS (parallel)          TRANSFER (parallel)         FINANCE (periodic)
    │                           │                          │
 RMA issued                Transfer approved            Valuation snapshot
 → Received               → Dispatched                 → GL reconcile
 → Inspected               → Received                   → Payment authorized
 → Restocked/Written-off  → StockReceived
```

---

## Aggregate Participation Matrix

| Aggregate | Boards | Commands Handled | Events Produced |
|-----------|--------|------------------|-----------------|
| Product Catalog | 1 | 3 | DE-001–003 |
| Inventory Location | 1, 8 | 3 | DE-004–006 |
| Inventory Governance | 1, 7 | 2 | DE-009–010 |
| Stock Policy | 1, 2 | 1 | DE-019 |
| Stock Position | 1–12 | 11+ | DE-011–018, 022, 068–070, 074 |
| Purchase Requisition | 2, 3 | 3 | DE-023–025 |
| Purchase Order | 3 | 4 | DE-026–029 |
| Goods Receipt | 3 | 4 | DE-030–033 |
| Supplier Invoice | 3 | 2 | DE-034–035, 081 |
| Customer Order Fulfillment | 4, 5, 12 | 10 | DE-036–045 |
| Stock Transfer | 6 | 6 | DE-046–051 |
| Cycle Count | 7 | 2 | DE-052–053 |
| Physical Inventory Count | 8 | 2 | DE-056–057, 007–008 |
| Inventory Adjustment Case | 7 | 5 | DE-054–055, 058–060 |
| Customer Return Case | 9 | 7 | DE-061–067 |
| Promotional Stock Allocation | 10 | 3 | DE-020–021, 072 |
| User Account | 13 | 3 | DE-078–080 |

---

## External System Touchpoints on Board

| External System | Board | Trigger | Event / Command |
|-----------------|-------|---------|-----------------|
| Supplier / Vendor | 3 | Delivers shipment | → VerifyGoodsReceipt |
| Supplier / Vendor | 3 | Sends invoice | → RecordSupplierInvoice |
| Logistics / Carrier | 4, 6 | Picks up goods | After ShipmentDispatched / TransferDispatched |
| Customer (B2B/B2C) | 4, 5, 9 | Places order / accepts backorder / returns | → ConfirmCustomerOrder / RecordBackorder / IssueReturnAuthorization |
| General Ledger / ERP | 3, 12 | Month-end close | InventoryValuationSnapshotPrepared |
| Customs / Regulatory | 3, 11 | Clearance granted | → ReleaseQuarantineHold |

---

## Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Domain Expert | | | |
| DDD Architect | | | |
| Product Owner | | | |

---

*End of Event Storming Board*

*Document ID: SRS-ES-008 | Version 1.0 | July 6, 2026*
