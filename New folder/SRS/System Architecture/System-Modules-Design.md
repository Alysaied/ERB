# System Modules Design
## Inventory Management System

---

## Document Information

| Attribute | Detail |
|-----------|--------|
| **Document ID** | SRS-SA-003 |
| **Document Title** | System Modules Design — Inventory Management System |
| **Version** | 1.0 |
| **Status** | Draft |
| **Document Owner** | Solution Architect |
| **Prepared For** | Delivery leads, technical architects, and development squads |
| **Date** | July 6, 2026 |
| **Classification** | Internal — Architecture Confidential |
| **Scope** | Logical module decomposition within the modular monolith — no class design, database schema, or API specification |

### Related Documents

| Document | ID | Relationship |
|----------|-----|--------------|
| Architecture Vision | SRS-SA-001 | Strategic direction |
| Architecture Style Recommendation | SRS-SA-002 | Modular monolith + Clean/Hexagonal |
| Bounded Contexts | SRS-DM-007 | 1:1 module alignment source |
| Domain Aggregates | SRS-DM-003 | Owned aggregate definitions |
| System Context | SRS-SA-002 (System Context) | External actors and systems |

### Document Purpose

This document defines the **logical system modules** of the Inventory Management System. Each module maps to a bounded context, owns specific aggregates, exposes a minimal public interface, and declares explicit dependencies. Modules are designed for **loose coupling** — integration occurs through commands, queries, domain events, and shared identifiers only.

### Module Design Principles

| Principle | Rule |
|-----------|------|
| **One module per bounded context** | Strategic domain boundary = compile-time module boundary |
| **Aggregate ownership is exclusive** | Each aggregate belongs to exactly one module |
| **No cross-module aggregate access** | Other modules reference aggregates by identity (SKU, Location Code, Order ID) only |
| **No shared mutable state** | Inventory Balance is the sole ATP mutator; Intelligence is read-only |
| **Events over direct calls** | Cross-module state propagation prefers domain events; synchronous queries for read-only consultation |
| **ACL at external boundaries** | Sales/CRM and Finance/ERP integrate through dedicated adapter ports — not module internals |

### Published Language (Cross-Module Identifiers)

All modules share these **value-only identifiers** — not domain object references:

| Identifier | Owner Module | Consumers |
|------------|--------------|-----------|
| `ProductSku` | Product Catalog | All operational modules |
| `LocationCode` | Warehouse Network | All operational modules |
| `UserId` | Identity & Access | All modules |
| `SupplierCode` | Procurement & Supplier | Inbound Receiving, Intelligence |
| `PurchaseOrderId` | Procurement & Supplier | Inbound Receiving, Intelligence |
| `GoodsReceiptId` | Inbound Receiving | Procurement, Intelligence, Finance ACL |
| `CustomerOrderId` | Order Fulfillment | Returns, Intelligence, Sales ACL |
| `TransferId` | Network Transfer | Inventory Balance, Intelligence |
| `AdjustmentCaseId` | Inventory Accuracy | Inventory Balance, Intelligence |
| `ReturnAuthorizationId` | Returns Management | Order Fulfillment, Inbound Receiving |
| `CampaignId` | Commercial Campaign | Order Fulfillment, Inventory Balance |
| `ReasonCode` | Inventory Governance | All modules performing adjustments or exceptions |

---

## Module Overview

| # | Module | Bounded Context | Aggregates | Phase |
|---|--------|-----------------|------------|-------|
| M-01 | Product Catalog | Product Catalog | 1 | MVP |
| M-02 | Warehouse Network | Warehouse Network | 1 | MVP |
| M-03 | Inventory Governance | Inventory Governance | 1 | MVP |
| M-04 | Inventory Balance | Inventory Balance | 2 | MVP |
| M-05 | Procurement & Supplier | Procurement & Supplier | 3 | Phase 2* |
| M-06 | Inbound Receiving | Inbound Receiving | 2 | MVP |
| M-07 | Order Fulfillment | Order Fulfillment | 1 | MVP |
| M-08 | Network Transfer | Network Transfer | 1 | Phase 2 |
| M-09 | Inventory Accuracy | Inventory Accuracy | 3 | MVP |
| M-10 | Returns Management | Returns Management | 1 | Phase 2 |
| M-11 | Commercial Campaign | Commercial Campaign | 1 | Phase 2 |
| M-12 | Identity & Access | Identity & Access | 1 | MVP |
| M-13 | Inventory Intelligence | Inventory Intelligence | 0 (read projections) | MVP |

*\*Procurement MVP subset: PO placement and receipt authorization without full requisition workflow may be enabled in Phase 1 per FR scope — module boundary exists from day one.*

---

## M-01 — Product Catalog

### 1. Module Name

**Product Catalog** (`ims.catalog`)

### 2. Business Responsibility

Maintain the authoritative product identity catalog — SKU definitions, lifecycle status, ABC classification, rotation policy, and traceability attributes — that all other modules reference when identifying *what* is being bought, held, counted, or sold.

| Process Coverage | BP-01, BP-04 |
|------------------|--------------|

### 3. Owned Aggregates

| Aggregate | Root Entity | Consistency Scope |
|-----------|-------------|-------------------|
| **Product Catalog** | Product | Single SKU master record and embedded classification attributes |

### 4. Public Interfaces

#### Commands (Write)

| Command | Description |
|---------|-------------|
| `CreateProduct` | Register new SKU with mandatory attributes |
| `UpdateProductAttributes` | Amend name, category, UoM, traceability settings |
| `ChangeProductLifecycleStatus` | Transition active → inactive → discontinued |
| `AssignAbcClassification` | Set or update ABC class for a SKU |
| `ResolveDuplicateProductConflict` | Merge or reject duplicate identity |

#### Queries (Read)

| Query | Description |
|-------|-------------|
| `GetProductBySku` | Retrieve product master by SKU |
| `SearchProducts` | Filter by name, category, status, ABC class |
| `ValidateProductTransactionEligibility` | Check lifecycle allows procurement/reservation |
| `ListProductsByCategory` | Catalog browse for operational screens |

#### Published Events

| Event | Consumers |
|-------|-----------|
| `ProductCreated` | Intelligence |
| `ProductUpdated` | Intelligence |
| `ProductLifecycleStatusChanged` | Procurement, Order Fulfillment, Intelligence |
| `AbcClassificationAssigned` | Inventory Accuracy, Intelligence |

#### External Adapter Ports (Inbound)

| Port | Source |
|------|--------|
| `BulkProductImportPort` | UC-046 go-live data import |

### 5. Dependencies

| Dependency | Module | Coupling Type | Purpose |
|------------|--------|---------------|---------|
| Identity & Access | M-12 | Sync query | User attribution on mutations |
| Inventory Intelligence | M-13 | Event publish | Catalog change projections |

**No dependencies on operational or quantity modules.** Product Catalog is an upstream supplier context.

---

## M-02 — Warehouse Network

### 1. Module Name

**Warehouse Network** (`ims.network`)

### 2. Business Responsibility

Define and manage the inventory location network — warehouses, stores, distribution points, storage positions, hierarchy, operational status, and location lifecycle (go-live, closure, freeze state) — that anchors all stock to physical places.

| Process Coverage | BP-02, BP-12 (freeze state) |
|------------------|----------------------------|

### 3. Owned Aggregates

| Aggregate | Root Entity | Consistency Scope |
|-----------|-------------|-------------------|
| **Inventory Location** | Inventory Location | Location master, hierarchy, status, **authoritative freeze flag**, storage positions |

### 4. Public Interfaces

#### Commands (Write)

| Command | Description |
|---------|-------------|
| `CreateInventoryLocation` | Register new warehouse, store, or DC |
| `UpdateLocationHierarchy` | Assign parent, zones, layout structure |
| `ConfigureStoragePosition` | Add or amend bin/aisle positions within location |
| `ActivateInventoryLocation` | Enable location after opening balance certification |
| `DeactivateInventoryLocation` | Begin closure workflow |
| `ApplyLocationFreeze` | Set frozen flag (driven by Physical Count event) |
| `ReleaseLocationFreeze` | Clear frozen flag (driven by Physical Count event) |
| `CloseInventoryLocation` | Finalize closure with disposition confirmation |

#### Queries (Read)

| Query | Description |
|-------|-------------|
| `GetLocationByCode` | Retrieve location master and status |
| `ListActiveLocations` | Network directory for dropdowns and filters |
| `GetStoragePositions` | Positions available for put-away assignment |
| `IsLocationFrozen` | Freeze guard check for operational modules |
| `IsLocationTransactionallyActive` | Go-live and status gate for mutations |

#### Published Events

| Event | Consumers |
|-------|-----------|
| `InventoryLocationCreated` | Intelligence |
| `InventoryLocationActivated` | Inventory Balance, Intelligence |
| `InventoryLocationDeactivated` | All operational modules, Intelligence |
| `LocationFreezeApplied` | Inventory Balance, Inbound, Fulfillment, Transfer, Intelligence |
| `LocationFreezeReleased` | All operational modules, Intelligence |
| `StoragePositionConfigured` | Inbound Receiving, Intelligence |

#### Subscribed Events

| Event | Source Module | Reaction |
|-------|---------------|----------|
| `LocationFreezeImposed` | Inventory Accuracy | `ApplyLocationFreeze` |
| `LocationFreezeReleased` | Inventory Accuracy | `ReleaseLocationFreeze` |

### 5. Dependencies

| Dependency | Module | Coupling Type | Purpose |
|------------|--------|---------------|---------|
| Identity & Access | M-12 | Sync query | User attribution; location-scoped role validation |
| Inventory Accuracy | M-09 | Event subscribe | Freeze initiation from physical count |
| Inventory Intelligence | M-13 | Event publish | Location network projections |

**Warehouse Network does not depend on Inventory Balance or any quantity module.**

---

## M-03 — Inventory Governance

### 1. Module Name

**Inventory Governance** (`ims.governance`)

### 2. Business Responsibility

Maintain organization-wide inventory control policies — reason codes, approval thresholds, tolerance limits, segregation-of-duties rules, and exception policies — that govern how operational modules authorize adjustments, receipts, and financial controls.

| Process Coverage | BP-01 (policy portion), BP-03 (policy portion), BP-32 |
|------------------|------------------------------------------------------|

### 3. Owned Aggregates

| Aggregate | Root Entity | Consistency Scope |
|-----------|-------------|-------------------|
| **Inventory Governance** | Governance Policy | Policy versions, reason codes, thresholds, tolerances |

### 4. Public Interfaces

#### Commands (Write)

| Command | Description |
|---------|-------------|
| `CreateReasonCode` | Add standardized exception/adjustment code |
| `RetireReasonCode` | Deactivate code for new transactions |
| `PublishGovernancePolicy` | Activate new policy version with effective date |
| `UpdateApprovalThreshold` | Amend financial/quantity approval limits |
| `UpdateReceiptTolerance` | Amend auto-accept vs. discrepancy thresholds |

#### Queries (Read)

| Command | Description |
|---------|-------------|
| `GetActiveReasonCodes` | List selectable codes for transaction forms |
| `ValidateReasonCode` | Confirm code active for transaction type |
| `GetEffectiveApprovalThreshold` | Threshold lookup for adjustment value |
| `GetReceiptTolerance` | Tolerance for receipt discrepancy auto-accept |
| `EvaluateSegregationOfDuties` | Check initiator vs. approver SoD compliance |

#### Published Events

| Event | Consumers |
|-------|-----------|
| `GovernancePolicyPublished` | All operational modules, Intelligence |
| `ReasonCodeCreated` | Intelligence |
| `ReasonCodeRetired` | All operational modules, Intelligence |
| `ApprovalThresholdUpdated` | Inventory Accuracy, Inbound, Intelligence |

### 5. Dependencies

| Dependency | Module | Coupling Type | Purpose |
|------------|--------|---------------|---------|
| Identity & Access | M-12 | Sync query | SoD evaluation uses role assignments |
| Inventory Intelligence | M-13 | Event publish | Policy compliance projections |

**Governance is consulted by operational modules; it does not call them.**

---

## M-04 — Inventory Balance

### 1. Module Name

**Inventory Balance** (`ims.balance`)

### 2. Business Responsibility

Own the authoritative inventory quantity state — on-hand, reserved, available-to-promise (ATP), quarantine holds, lot/batch breakdown, and replenishment thresholds — answering *what do we have, where is it, and what is available?*

This is the **core domain module** and the **sole mutator of stock quantities**.

| Process Coverage | BP-03, BP-10, BP-21 |
|------------------|----------------------|

### 3. Owned Aggregates

| Aggregate | Root Entity | Consistency Scope |
|-----------|-------------|-------------------|
| **Stock Position** | Stock Position | On-hand, reserved, ATP, lots, quarantine holds — per product per location |
| **Stock Policy** | Stock Policy | Reorder level, minimum, safety stock, maximum — per product per location |

### 4. Public Interfaces

#### Commands (Write)

| Command | Description |
|---------|-------------|
| `EstablishOpeningBalance` | Create initial Stock Position at location go-live |
| `ReceiveStock` | Increase on-hand after put-away (event-driven) |
| `ReserveStock` | Commit ATP for order line |
| `ReleaseReservation` | Restore ATP on cancellation |
| `DeductStockForShipment` | Reduce on-hand and reserved after verified pick |
| `DeductStockForTransfer` | Reduce source on dispatch |
| `ReceiveStockFromTransfer` | Increase destination on transfer receipt |
| `ApplyApprovedAdjustment` | Apply governed quantity correction |
| `ApplyApprovedWriteOff` | Permanently remove quantity |
| `ApplyQuarantineHold` | Reduce ATP for held quantity |
| `ReleaseQuarantineHold` | Restore ATP after clearance |
| `SegregatePromotionalStock` | Ring-fence ATP per campaign event |
| `ReleasePromotionalAllocation` | Restore general ATP after campaign |
| `TransferConsignmentOwnership` | Reclassify ownership on consumption trigger |
| `DefineStockPolicy` | Set replenishment thresholds |
| `UpdateStockPolicy` | Amend thresholds with effective dating |

#### Queries (Read)

| Query | Description |
|-------|-------------|
| `GetStockPosition` | On-hand, reserved, ATP for product at location |
| `GetAvailabilityBySku` | ATP for single SKU (hot path — NFR-PERF-002) |
| `GetNetworkAvailability` | ATP across locations for a SKU |
| `GetStockStatusIndicator` | In-stock / low-stock / out-of-stock derived state |
| `GetStockPolicy` | Thresholds for product at location |
| `GetLotBreakdown` | Lot-level quantities for traceable products |
| `EvaluateSourceTransferCapacity` | Spare quantity above minimum for transfer |

#### Published Events

| Event | Consumers |
|-------|-----------|
| `OpeningBalanceEstablished` | Intelligence |
| `StockReceived` | Order Fulfillment (backorder), Intelligence |
| `StockReserved` | Order Fulfillment, Intelligence |
| `ReservationReleased` | Intelligence |
| `StockShipped` | Intelligence, Finance ACL |
| `StockAdjusted` | Intelligence, Finance ACL |
| `StockWrittenOff` | Intelligence, Finance ACL |
| `QuarantineHoldApplied` | Intelligence |
| `QuarantineHoldReleased` | Intelligence |
| `LowStockThresholdBreached` | Procurement, Intelligence |
| `OutOfStockDetected` | Procurement, Intelligence |
| `PromotionalStockSegregated` | Commercial Campaign, Intelligence |
| `PromotionalAllocationReleased` | Commercial Campaign, Intelligence |
| `ConsignmentOwnershipTransferred` | Intelligence, Finance ACL |

#### Subscribed Events

| Event | Source Module | Reaction |
|-------|---------------|----------|
| `PutAwayCompleted` | Inbound Receiving | `ReceiveStock` |
| `TransferDispatched` | Network Transfer | `DeductStockForTransfer` |
| `TransferReceived` | Network Transfer | `ReceiveStockFromTransfer` |
| `AdjustmentApproved` | Inventory Accuracy | `ApplyApprovedAdjustment` / `ApplyApprovedWriteOff` |
| `ReturnRestocked` | Returns Management | `ReceiveStock` |
| `ReturnQuarantined` | Returns Management | `ApplyQuarantineHold` |
| `PromotionalStockAllocated` | Commercial Campaign | `SegregatePromotionalStock` |
| `PromotionalAllocationReleased` | Commercial Campaign | `ReleasePromotionalAllocation` |
| `ShipmentDispatched` | Order Fulfillment | `DeductStockForShipment` |

### 5. Dependencies

| Dependency | Module | Coupling Type | Purpose |
|------------|--------|---------------|---------|
| Product Catalog | M-01 | Sync query | SKU validation and lifecycle eligibility |
| Warehouse Network | M-02 | Sync query | Location status and freeze guard |
| Inventory Governance | M-03 | Sync query | Safety stock override, tolerance consultation |
| Identity & Access | M-12 | Sync query | User attribution |
| Inbound Receiving | M-06 | Event subscribe | Stock increase on put-away |
| Order Fulfillment | M-07 | Command/Event | Reservation and deduction coordination |
| Network Transfer | M-08 | Event subscribe | Transfer quantity mutations |
| Inventory Accuracy | M-09 | Event subscribe | Approved adjustments and write-offs |
| Returns Management | M-10 | Event subscribe | Restock and quarantine |
| Commercial Campaign | M-11 | Event subscribe | Promotional ATP segregation |
| Inventory Intelligence | M-13 | Event publish | All balance change projections |

**Inventory Balance never imports domain objects from consumer modules — only identities and events.**

---

## M-05 — Procurement & Supplier

### 1. Module Name

**Procurement & Supplier** (`ims.procurement`)

### 2. Business Responsibility

Manage the inbound supply commitment lifecycle — supplier relationships, internal requisition approval, purchase order placement, and expected inbound delivery planning — authorizing *what the organization has committed to buy* before goods arrive.

| Process Coverage | BP-05, BP-06, BP-22, BP-23 |
|------------------|----------------------------|

### 3. Owned Aggregates

| Aggregate | Root Entity | Consistency Scope |
|-----------|-------------|-------------------|
| **Supplier** | Supplier | Supplier master, payment terms, consignment agreement |
| **Purchase Requisition** | Purchase Requisition | Internal replenishment request and approval |
| **Purchase Order** | Purchase Order | Commercial supplier commitment and expected deliveries |

### 4. Public Interfaces

#### Commands (Write)

| Command | Description |
|---------|-------------|
| `RegisterSupplier` | Create supplier master record |
| `UpdateSupplierTerms` | Amend payment terms, lead time, consignment flag |
| `DeactivateSupplier` | Block new PO creation |
| `CreatePurchaseRequisition` | Internal replenishment request |
| `ApprovePurchaseRequisition` | Authorize requisition for PO conversion |
| `RejectPurchaseRequisition` | Decline with reason |
| `ConvertRequisitionToPurchaseOrder` | Create PO from approved requisition |
| `PlacePurchaseOrder` | Issue commercial commitment to supplier |
| `AmendPurchaseOrder` | Modify lines or delivery schedule |
| `CancelPurchaseOrder` | Cancel with receipt implications |
| `RecordExpectedInboundDelivery` | Update shipment schedule |

#### Queries (Read)

| Query | Description |
|-------|-------------|
| `GetSupplierByCode` | Supplier master and terms |
| `GetPurchaseOrder` | PO header, lines, received quantities |
| `ListOpenPurchaseOrders` | Inbound pipeline for receiving and planning |
| `ValidatePoForReceipt` | Confirm PO authorizes receipt (BR-007) |
| `GetInboundPipelineStatus` | Expected deliveries by location |

#### Published Events

| Event | Consumers |
|-------|-----------|
| `SupplierRegistered` | Intelligence |
| `PurchaseRequisitionCreated` | Intelligence |
| `PurchaseRequisitionApproved` | Intelligence |
| `PurchaseOrderPlaced` | Inbound Receiving, Intelligence |
| `PurchaseOrderAmended` | Inbound Receiving, Intelligence |
| `PurchaseOrderCancelled` | Inbound Receiving, Intelligence |
| `ExpectedInboundDeliveryUpdated` | Intelligence |

#### Domain Service Ports (Outbound Consultation)

| Port | Target Module | Purpose |
|------|---------------|---------|
| `NetworkAvailabilityPort` | M-04 Inventory Balance | Evaluate network ATP before requisition (BR-011) |

### 5. Dependencies

| Dependency | Module | Coupling Type | Purpose |
|------------|--------|---------------|---------|
| Product Catalog | M-01 | Sync query | SKU lifecycle validation on lines |
| Warehouse Network | M-02 | Sync query | Receiving location validation |
| Inventory Balance | M-04 | Sync query | Network availability evaluation |
| Inventory Governance | M-03 | Sync query | Ad-hoc receipt policy, tolerances |
| Identity & Access | M-12 | Sync query | User attribution and approval authority |
| Inbound Receiving | M-06 | Event publish | PO authorizes goods receipt |
| Inventory Intelligence | M-13 | Event publish | Procurement pipeline projections |

**Procurement does not mutate stock quantities.**

---

## M-06 — Inbound Receiving

### 1. Module Name

**Inbound Receiving** (`ims.inbound`)

### 2. Business Responsibility

Execute the inbound supply verification workflow — goods receipt, discrepancy documentation, put-away confirmation, and supplier invoice matching — governing *what was actually received and when it becomes available*.

| Process Coverage | BP-07, BP-08, BP-09, BP-30 (match portion) |
|------------------|---------------------------------------------|

### 3. Owned Aggregates

| Aggregate | Root Entity | Consistency Scope |
|-----------|-------------|-------------------|
| **Goods Receipt** | Goods Receipt | Verification, receipt lines, discrepancies, put-away |
| **Supplier Invoice** | Supplier Invoice | Billing document and three-way match outcome |

### 4. Public Interfaces

#### Commands (Write)

| Command | Description |
|---------|-------------|
| `CreateGoodsReceipt` | Initiate receipt against PO or ad-hoc authorization |
| `VerifyGoodsReceipt` | Confirm quantity, product, condition at dock |
| `DocumentReceiptDiscrepancy` | Record variance with classification |
| `ResolveReceiptDiscrepancy` | Close discrepancy with resolution |
| `ConfirmPutAway` | Assign storage position and complete put-away |
| `ReceiveAdHocInbound` | Non-PO receipt with governance authorization |
| `ReceiveReturnInbound` | Accept physical return (shared workflow with Returns) |
| `RegisterSupplierInvoice` | Record supplier billing document |
| `PerformThreeWayMatch` | Evaluate PO, receipt, invoice alignment |
| `AuthorizeInvoicePayment` | Approve match for payment gate |

#### Queries (Read)

| Query | Description |
|-------|-------------|
| `GetGoodsReceipt` | Receipt status, lines, put-away state |
| `ListPendingPutAway` | Receipts awaiting storage placement |
| `GetReceiptDiscrepancies` | Open discrepancies by location |
| `GetSupplierInvoice` | Invoice and match status |
| `GetThreeWayMatchResult` | Match outcome for finance review |

#### Published Events

| Event | Consumers |
|-------|-----------|
| `GoodsReceiptVerified` | Intelligence |
| `ReceiptDiscrepancyDocumented` | Intelligence |
| `PutAwayCompleted` | **Inventory Balance**, Intelligence |
| `SupplierInvoiceRegistered` | Intelligence |
| `ThreeWayMatchCompleted` | Intelligence, Finance ACL |
| `InvoicePaymentAuthorized` | Finance ACL |

#### Subscribed Events

| Event | Source Module | Reaction |
|-------|---------------|----------|
| `PurchaseOrderPlaced` | Procurement | Enable receipt against PO |
| `PurchaseOrderCancelled` | Procurement | Block new receipts against PO |

### 5. Dependencies

| Dependency | Module | Coupling Type | Purpose |
|------------|--------|---------------|---------|
| Product Catalog | M-01 | Sync query | Product identity and MRSL validation |
| Warehouse Network | M-02 | Sync query | Receiving location, positions, freeze check |
| Inventory Governance | M-03 | Sync query | Tolerances, reason codes, ad-hoc policy |
| Procurement & Supplier | M-05 | Sync query + event | PO authorization for receipt |
| Identity & Access | M-12 | Sync query | User attribution |
| Inventory Balance | M-06 | Event publish | Put-away triggers stock increase |
| Returns Management | M-10 | Sync query | RMA validation for return receipt |
| Inventory Intelligence | M-13 | Event publish | Receipt and match projections |

---

## M-07 — Order Fulfillment

### 1. Module Name

**Order Fulfillment** (`ims.fulfillment`)

### 2. Business Responsibility

Manage the customer order fulfillment lifecycle — availability confirmation, reservation, pick/pack/ship, partial fulfillment, backorders, and fulfillment exceptions — governing *how customer demand consumes inventory*.

| Process Coverage | BP-16, BP-17, BP-18, BP-19, BP-20 |
|------------------|-----------------------------------|

### 3. Owned Aggregates

| Aggregate | Root Entity | Consistency Scope |
|-----------|-------------|-------------------|
| **Customer Order Fulfillment** | Customer Order | Order lines, reservations, pick/pack, backorders, shipments |

### 4. Public Interfaces

#### Commands (Write)

| Command | Description |
|---------|-------------|
| `ImportCustomerOrder` | Accept order from Sales/CRM ACL |
| `ConfirmOrderAvailability` | Validate ATP for all lines |
| `ConfirmCustomerOrder` | Commit order and initiate reservation saga |
| `ReserveInventoryForOrder` | Request stock reservation (saga step) |
| `ReleaseOrderReservations` | Cancel reservations on order cancel |
| `AssignPickList` | Allocate pick work to warehouse |
| `VerifyPick` | Confirm picked quantity and lot |
| `PackOrder` | Complete packing step |
| `DispatchShipment` | Record shipment and trigger stock deduction |
| `RecordPartialFulfillment` | Split line into fulfilled and backordered |
| `CreateBackorder` | Record customer-agreed delay |
| `FulfillBackorder` | Convert backorder to reservation on stock arrival |
| `HandleFulfillmentException` | Document and resolve outbound exception |

#### Queries (Read)

| Query | Description |
|-------|-------------|
| `GetCustomerOrder` | Order status and line breakdown |
| `GetOrderFulfillmentStatus` | Reservation, pick, ship state |
| `ListOrdersAwaitingPick` | Warehouse work queue |
| `GetBackorderPipeline` | Open backorders by SKU |

#### Published Events

| Event | Consumers |
|-------|-----------|
| `CustomerOrderImported` | Intelligence |
| `OrderAvailabilityConfirmed` | Intelligence |
| `CustomerOrderConfirmed` | Intelligence |
| `OrderReservationRequested` | Inventory Balance (via saga) |
| `OrderReservationFailed` | Intelligence (saga compensation) |
| `PickVerified` | Intelligence |
| `ShipmentDispatched` | **Inventory Balance**, Intelligence |
| `BackorderCreated` | Intelligence |
| `BackorderFulfilled` | Intelligence |
| `OrderCancelled` | Inventory Balance, Intelligence |

#### Subscribed Events

| Event | Source Module | Reaction |
|-------|---------------|----------|
| `StockReserved` | Inventory Balance | Advance reservation saga |
| `ReservationReleased` | Inventory Balance | Confirm cancellation |
| `StockReceived` | Inventory Balance | Trigger backorder fulfillment policy |
| `LocationFreezeApplied` | Warehouse Network | Block shipment at frozen location |

#### External Adapter Ports

| Port | External System | Purpose |
|------|-----------------|---------|
| `SalesOrderInboundPort` | EXT-01 Sales/CRM | Translate external order to fulfillment model (ACL) |
| `FulfillmentStatusOutboundPort` | EXT-01 Sales/CRM | Publish ship status back to sales system |

### 5. Dependencies

| Dependency | Module | Coupling Type | Purpose |
|------------|--------|---------------|---------|
| Product Catalog | M-01 | Sync query | SKU lifecycle on order lines |
| Warehouse Network | M-02 | Sync query | Ship-from location, freeze check |
| Inventory Balance | M-04 | Sync query + command + event | ATP read, reservation, deduction |
| Inventory Governance | M-03 | Sync query | Pick verification policy |
| Commercial Campaign | M-11 | Sync query | Ring-fence check before reservation |
| Identity & Access | M-12 | Sync query | User attribution |
| Returns Management | M-10 | Sync query | Original order reference for RMA |
| Inventory Intelligence | M-13 | Event publish | Fulfillment status projections |

---

## M-08 — Network Transfer

### 1. Module Name

**Network Transfer** (`ims.transfer`)

### 2. Business Responsibility

Manage inter-location stock redistribution — transfer requests, approval, dispatch, in-transit tracking, and destination receipt — resolving network imbalance without new procurement.

| Process Coverage | BP-24, BP-25, BP-26 |
|------------------|---------------------|

### 3. Owned Aggregates

| Aggregate | Root Entity | Consistency Scope |
|-----------|-------------|-------------------|
| **Stock Transfer** | Stock Transfer | Request, approval, dispatch, in-transit, receipt — full transfer lifecycle |

### 4. Public Interfaces

#### Commands (Write)

| Command | Description |
|---------|-------------|
| `RequestStockTransfer` | Initiate transfer from source to destination |
| `ApproveTransferRequest` | Authorize transfer for dispatch |
| `RejectTransferRequest` | Decline with reason |
| `DispatchTransfer` | Ship from source; create in-transit state |
| `ReceiveTransfer` | Confirm receipt at destination |
| `CancelInTransitTransfer` | Abort in-transit with reversal workflow |

#### Queries (Read)

| Query | Description |
|-------|-------------|
| `GetStockTransfer` | Transfer status and line detail |
| `ListPendingTransferApprovals` | Approval queue for managers |
| `ListInTransitStock` | Pipeline inventory by location |
| `GetTransferHistory` | Completed transfers for location |

#### Published Events

| Event | Consumers |
|-------|-----------|
| `TransferRequested` | Intelligence |
| `TransferApproved` | Intelligence |
| `TransferDispatched` | **Inventory Balance**, Intelligence |
| `TransferInTransit` | Intelligence |
| `TransferReceived` | **Inventory Balance**, Intelligence |
| `TransferCancelled` | Intelligence |

### 5. Dependencies

| Dependency | Module | Coupling Type | Purpose |
|------------|--------|---------------|---------|
| Product Catalog | M-01 | Sync query | Product and lot traceability on lines |
| Warehouse Network | M-02 | Sync query | Source/destination validation, freeze check |
| Inventory Balance | M-04 | Sync query + event | Source capacity check; quantity mutations |
| Inventory Governance | M-03 | Sync query | Approval thresholds |
| Identity & Access | M-12 | Sync query | User attribution |
| Procurement & Supplier | M-05 | Event/consult | Transfer recommended before purchase (BR-011) |
| Inventory Intelligence | M-13 | Event publish | In-transit and network balance projections |

---

## M-09 — Inventory Accuracy

### 1. Module Name

**Inventory Accuracy** (`ims.accuracy`)

### 2. Business Responsibility

Maintain inventory record accuracy through cycle counting, physical inventory counts, variance investigation, governed adjustments, and write-offs — ensuring *recorded stock reflects physical reality*.

| Process Coverage | BP-11, BP-12, BP-13, BP-14, BP-15 |
|------------------|------------------------------------|

### 3. Owned Aggregates

| Aggregate | Root Entity | Consistency Scope |
|-----------|-------------|-------------------|
| **Cycle Count** | Cycle Count | Scheduled partial counts, blind count protocol |
| **Physical Inventory Count** | Physical Inventory Count | Wall-to-wall count, freeze initiation |
| **Inventory Adjustment Case** | Adjustment Case | Variance investigation, adjustment, write-off |

### 4. Public Interfaces

#### Commands (Write)

| Command | Description |
|---------|-------------|
| `ScheduleCycleCount` | Assign count work by product/location |
| `RecordCycleCountResult` | Submit blind count result |
| `InitiatePhysicalInventoryCount` | Start wall-to-wall count at location |
| `RecordPhysicalCountResult` | Submit line-level count during freeze |
| `CertifyPhysicalInventoryCount` | Complete count and release freeze |
| `OpenAdjustmentCase` | Create case from variance or direct adjustment |
| `InvestigateVariance` | Document root cause analysis |
| `SubmitAdjustmentForApproval` | Route adjustment through governance |
| `ApproveAdjustment` | Independent approver authorization |
| `RejectAdjustment` | Decline adjustment with reason |
| `FinalizeWriteOff` | Approve permanent quantity removal |

#### Queries (Read)

| Query | Description |
|-------|-------------|
| `GetCycleCountAssignment` | Count task without revealing system quantity (blind) |
| `GetPhysicalCountStatus` | Count progress and freeze window |
| `GetAdjustmentCase` | Investigation and approval state |
| `ListPendingApprovals` | Adjustment queue for managers |

#### Published Events

| Event | Consumers |
|-------|-----------|
| `CycleCountCompleted` | Intelligence |
| `CycleCountVarianceDetected` | Intelligence |
| `LocationFreezeImposed` | **Warehouse Network**, Intelligence |
| `LocationFreezeReleased` | **Warehouse Network**, Intelligence |
| `PhysicalInventoryCountCertified` | Intelligence |
| `AdjustmentCaseOpened` | Intelligence |
| `AdjustmentApproved` | **Inventory Balance**, Intelligence |
| `WriteOffApproved` | **Inventory Balance**, Intelligence |

#### Domain Service Ports (Outbound Consultation)

| Port | Target Module | Purpose |
|------|---------------|---------|
| `SystemQuantityPort` | M-04 Inventory Balance | Read system quantity at variance calculation (not shown to counter) |

### 5. Dependencies

| Dependency | Module | Coupling Type | Purpose |
|------------|--------|---------------|---------|
| Product Catalog | M-01 | Sync query | ABC-driven count frequency |
| Warehouse Network | M-02 | Sync query + event | Freeze apply/release |
| Inventory Balance | M-04 | Sync query + event | System quantity read; approved mutations |
| Inventory Governance | M-03 | Sync query | Reason codes, thresholds, SoD |
| Identity & Access | M-12 | Sync query | Counter vs. approver SoD |
| Returns Management | M-10 | Command | Return write-off may open Adjustment Case |
| Inventory Intelligence | M-13 | Event publish | Accuracy and shrinkage projections |

**Inventory Accuracy never directly mutates Stock Position — only via approved events.**

---

## M-10 — Returns Management

### 1. Module Name

**Returns Management** (`ims.returns`)

### 2. Business Responsibility

Manage reverse logistics — return authorization, physical return receipt, condition inspection, and disposition routing (restock, quarantine, write-off) — governing *how returned goods re-enter or exit inventory*.

| Process Coverage | BP-27, BP-28 |
|------------------|--------------|

### 3. Owned Aggregates

| Aggregate | Root Entity | Consistency Scope |
|-----------|-------------|-------------------|
| **Customer Return Case** | Return Authorization | RMA, return receipt, inspection, disposition |

### 4. Public Interfaces

#### Commands (Write)

| Command | Description |
|---------|-------------|
| `AuthorizeCustomerReturn` | Issue RMA linked to original order |
| `ReceiveReturnedGoods` | Record physical return at warehouse |
| `InspectReturnedGoods` | Assess condition grade |
| `DispositionReturn` | Route to restock, quarantine, or write-off |
| `CancelReturnAuthorization` | Void unused RMA |

#### Queries (Read)

| Query | Description |
|-------|-------------|
| `GetReturnAuthorization` | RMA status and eligibility |
| `ListPendingReturnReceipts` | Returns awaiting warehouse processing |
| `GetReturnDisposition` | Inspection outcome and routing |

#### Published Events

| Event | Consumers |
|-------|-----------|
| `ReturnAuthorized` | Intelligence |
| `ReturnReceived` | Intelligence |
| `ReturnInspected` | Intelligence |
| `ReturnRestocked` | **Inventory Balance**, Intelligence |
| `ReturnQuarantined` | **Inventory Balance**, Intelligence |
| `ReturnWrittenOff` | **Inventory Accuracy** (Adjustment Case), Intelligence |

### 5. Dependencies

| Dependency | Module | Coupling Type | Purpose |
|------------|--------|---------------|---------|
| Product Catalog | M-01 | Sync query | Returned product validation |
| Warehouse Network | M-02 | Sync query | Return receiving location |
| Order Fulfillment | M-07 | Sync query | Original order reference (BR-025) |
| Inbound Receiving | M-06 | Shared workflow | Physical receipt verification pattern |
| Inventory Balance | M-04 | Event publish | Restock and quarantine |
| Inventory Accuracy | M-09 | Event publish | Write-off via Adjustment Case |
| Inventory Governance | M-03 | Sync query | Disposition reason codes |
| Identity & Access | M-12 | Sync query | User attribution |
| Inventory Intelligence | M-13 | Event publish | Returns pipeline projections |

---

## M-11 — Commercial Campaign

### 1. Module Name

**Commercial Campaign** (`ims.campaign`)

### 2. Business Responsibility

Ring-fence inventory for promotional campaigns and product launches, protect allocated stock from non-promotional consumption, and support campaign readiness confirmation.

| Process Coverage | BP-31 |
|------------------|-------|

### 3. Owned Aggregates

| Aggregate | Root Entity | Consistency Scope |
|-----------|-------------|-------------------|
| **Promotional Stock Allocation** | Promotional Stock Allocation | Campaign ring-fence, channel scope, readiness |

### 4. Public Interfaces

#### Commands (Write)

| Command | Description |
|---------|-------------|
| `CreatePromotionalAllocation` | Ring-fence quantity for campaign |
| `AmendPromotionalAllocation` | Adjust allocated quantity or period |
| `ConfirmCampaignReadiness` | Certify stock sufficient for launch |
| `ReleasePromotionalAllocation` | End campaign and release unspent stock |
| `AuthorizePromotionalOverride` | Allow non-promotional consumption of ring-fenced stock |

#### Queries (Read)

| Query | Description |
|-------|-------------|
| `GetPromotionalAllocation` | Allocation status and quantity |
| `CheckRingFenceForSku` | Whether SKU has active ring-fence at location |
| `GetCampaignReadinessStatus` | Launch readiness assessment |
| `ListActiveCampaigns` | Active allocations by period |

#### Published Events

| Event | Consumers |
|-------|-----------|
| `PromotionalStockAllocated` | **Inventory Balance**, Intelligence |
| `CampaignReadinessConfirmed` | Intelligence |
| `CampaignReadinessFailed` | Intelligence |
| `PromotionalAllocationReleased` | **Inventory Balance**, Intelligence |
| `PromotionalOverrideAuthorized` | Order Fulfillment, Intelligence |

#### External Adapter Ports

| Port | External System | Purpose |
|------|-----------------|---------|
| `CampaignPlanInboundPort` | EXT-07 Marketing | Import campaign plan (ACL) |

### 5. Dependencies

| Dependency | Module | Coupling Type | Purpose |
|------------|--------|---------------|---------|
| Product Catalog | M-01 | Sync query | Campaign SKU validation |
| Warehouse Network | M-02 | Sync query | Allocation location scope |
| Inventory Balance | M-04 | Sync query + event | Available quantity check; ATP segregation |
| Order Fulfillment | M-07 | Event publish | Override authorization |
| Identity & Access | M-12 | Sync query | User attribution |
| Inventory Intelligence | M-13 | Event publish | Campaign readiness projections |

**Commercial Campaign owns allocation intent; Inventory Balance owns ATP mechanics.**

---

## M-12 — Identity & Access

### 1. Module Name

**Identity & Access** (`ims.identity`)

### 2. Business Responsibility

Manage user identity, role assignments, location-scoped permissions, and segregation-of-duties enforcement for all inventory operations — governing *who may perform and approve* inventory actions.

| Process Coverage | Cross-cutting (UC-044, UC-045) |
|------------------|-------------------------------|

### 3. Owned Aggregates

| Aggregate | Root Entity | Consistency Scope |
|-----------|-------------|-------------------|
| **User Account** | User Account | User identity, role assignments, location scope |

### 4. Public Interfaces

#### Commands (Write)

| Command | Description |
|---------|-------------|
| `ProvisionUserAccount` | Create user identity |
| `AssignRole` | Delegate role with location scope |
| `RevokeRole` | Remove role assignment |
| `SuspendUserAccount` | Temporarily block access |
| `DeactivateUserAccount` | Permanent account closure |
| `SyncUserFromDirectory` | Import identity from HR/IdP |

#### Queries (Read)

| Query | Description |
|-------|-------------|
| `GetUserAccount` | User profile and role assignments |
| `AuthorizeAction` | Permission check for command execution |
| `ValidateLocationScope` | Confirm user authorized for location |
| `DetectSegregationOfDutiesConflict` | Block conflicting role combinations |
| `GetUserAttribution` | Identity template for audit records |

#### Published Events

| Event | Consumers |
|-------|-----------|
| `UserAccountProvisioned` | Intelligence |
| `RoleAssigned` | Intelligence |
| `RoleRevoked` | Intelligence |
| `UserAccountDeactivated` | All modules (session invalidation), Intelligence |
| `SegregationOfDutiesViolationDetected` | Intelligence |

#### External Adapter Ports

| Port | External System | Purpose |
|------|-----------------|---------|
| `IdentityProviderPort` | SVC-01 Enterprise IdP | SSO authentication |
| `DirectorySyncPort` | EXT-08 HR Directory | User provisioning sync |

### 5. Dependencies

| Dependency | Module | Coupling Type | Purpose |
|------------|--------|---------------|---------|
| Warehouse Network | M-02 | Sync query | Location codes for scope validation |
| Inventory Governance | M-03 | Shared policy | SoD rules defined in governance, enforced here |
| Inventory Intelligence | M-13 | Event publish | Access audit projections |

**Identity & Access is consumed by all modules; it does not depend on operational modules except Network (for location scope).**

---

## M-13 — Inventory Intelligence

### 1. Module Name

**Inventory Intelligence** (`ims.intelligence`)

### 2. Business Responsibility

Provide read-optimized views of inventory state — dashboards, KPIs, movement history, audit trails, alerts, and valuation snapshots — supporting management oversight **without owning transactional write models**.

| Process Coverage | BP-29, BP-30 (reporting), BP-32 |
|------------------|--------------------------------|

### 3. Owned Aggregates

**None.** This module owns **read projections** only:

| Projection | Source Events | Purpose |
|------------|---------------|---------|
| Inventory Movement Record | All balance change events | Append-only movement history |
| Audit Trail Record | All material command events | Governance-grade change log |
| Operational Alert | Threshold and exception events | Low-stock, approval pending, freeze alerts |
| Inventory Valuation Snapshot | Period-end aggregation | Finance reconciliation |
| KPI Dashboard Views | Multiple event streams | Fill rate, accuracy, turnover metrics |
| Backorder Pipeline View | Fulfillment events | CS and operations visibility |
| Inbound Pipeline View | Procurement and receipt events | Supply chain visibility |

### 4. Public Interfaces

#### Queries (Read Only — No Commands)

| Query | Description |
|-------|-------------|
| `GetInventoryDashboard` | Location or network summary dashboard |
| `GetStockStatusSummary` | On-hand, ATP, low-stock counts |
| `SearchMovementHistory` | Filter movements by SKU, location, period |
| `QueryAuditTrail` | Compliance audit search and export |
| `GetOperationalAlerts` | Active alerts for user/location scope |
| `GetKpiReport` | Performance KPIs (fill rate, accuracy, shrinkage) |
| `GetValuationSnapshot` | Period-end inventory valuation |
| `GetBackorderPipeline` | Open backorders sorted by policy |
| `GetInboundPipelineReport` | Open POs and expected deliveries |
| `ExportAuditEvidencePackage` | Auditor export (NFR-PERF-026, NFR-COM-012) |

#### Published Events

| Event | Consumers |
|-------|-----------|
| `OperationalAlertRaised` | Notification gateway (SVC-02) |
| `KpiThresholdBreached` | Notification gateway |
| `ValuationSnapshotPrepared` | Finance ACL (EXT-02) |

#### Subscribed Events

| Event | Source |
|-------|--------|
| *All domain events from M-01 through M-12* | Event bus — projection handlers update read models |

#### External Adapter Ports (Outbound)

| Port | External System | Purpose |
|------|-----------------|---------|
| `FinanceValuationExportPort` | EXT-02 Finance ERP | Valuation snapshot ACL |
| `ExecutiveBiExportPort` | External BI | KPI data feed |

### 5. Dependencies

| Dependency | Module | Coupling Type | Purpose |
|------------|--------|---------------|---------|
| All transactional modules | M-01 – M-12 | Event subscribe | Build and maintain read projections |
| Identity & Access | M-12 | Sync query | Scope queries to user permissions |

**Inventory Intelligence has no write dependencies and never calls back into transactional modules.**

---

## Cross-Module Integration Map

### Dependency Direction (Upstream → Downstream)

```
                    ┌─────────────────┐
                    │ Identity &      │
                    │ Access (M-12)   │
                    └────────┬────────┘
                             │ consulted by all
    ┌────────────────────────┼────────────────────────┐
    │                        │                        │
┌───▼────┐  ┌───────────▼───┐  ┌──────▼──────┐
│Product │  │  Warehouse    │  │ Inventory   │
│Catalog │  │  Network      │  │ Governance  │
│(M-01)  │  │  (M-02)       │  │ (M-03)      │
└───┬────┘  └───────┬───────┘  └──────┬──────┘
    │ upstream      │ upstream        │ consulted
    └───────────────┼─────────────────┘
                    ▼
         ┌──────────────────────┐
         │  INVENTORY BALANCE   │  ◄── core domain, sole ATP mutator
         │       (M-04)         │
         └──────────┬───────────┘
                    │ events
    ┌───────┬───────┼───────┬───────┬───────┐
    ▼       ▼       ▼       ▼       ▼       ▼
┌──────┐┌──────┐┌──────┐┌──────┐┌──────┐┌──────┐
│Inbnd ││Fulfl ││Trans ││Accrcy││Retrn ││Campn │
│ M-06 ││ M-07 ││ M-08 ││ M-09 ││ M-10 ││ M-11 │
└──┬───┘└──────┘└──────┘└──────┘└──────┘└──────┘
   │
┌──▼──────────┐
│ Procurement │
│    (M-05)   │
└─────────────┘

         ┌──────────────────────┐
         │ Inventory Intelligence│  ◄── read-only, all events in
         │       (M-13)          │
         └──────────────────────┘
```

### Coupling Mechanism Summary

| From Module | To Module | Mechanism | Mutable State? |
|-------------|-----------|-----------|----------------|
| Any operational | Product Catalog | Sync query | No |
| Any operational | Warehouse Network | Sync query | No |
| Any operational | Inventory Governance | Sync query | No |
| Any operational | Identity & Access | Sync query | No |
| Fulfillment, Transfer, Accuracy, Returns, Campaign | Inventory Balance | Command + event | Yes (Balance only) |
| Inbound Receiving | Inventory Balance | Event (`PutAwayCompleted`) | Yes (Balance only) |
| Inventory Accuracy | Warehouse Network | Event (freeze) | Yes (Network only) |
| Commercial Campaign | Inventory Balance | Event (ring-fence) | Yes (Balance only) |
| All transactional | Intelligence | Event publish | No (projections only) |
| Fulfillment | Sales/CRM | ACL adapter | External |
| Intelligence | Finance ERP | ACL adapter | External |

### Saga Ownership (Cross-Module Workflows)

| Saga | Orchestrator Module | Participating Modules |
|------|---------------------|----------------------|
| Order Confirm → Reserve | Order Fulfillment (M-07) | Inventory Balance (M-04) |
| Put-Away → Stock Available | Inbound Receiving (M-06) | Inventory Balance (M-04) |
| Transfer Dispatch → Receive | Network Transfer (M-08) | Inventory Balance (M-04) |
| Count Variance → Adjust | Inventory Accuracy (M-09) | Inventory Balance (M-04), Warehouse Network (M-02) |
| Return Disposition → Restock/Write-off | Returns Management (M-10) | Inventory Balance (M-04) or Accuracy (M-09) |
| Opening Balance → Location Activate | Warehouse Network (M-02) | Inventory Balance (M-04) |
| Campaign Allocate → ATP Segregate | Commercial Campaign (M-11) | Inventory Balance (M-04) |

---

## Module Boundary Enforcement Rules

| Rule ID | Rule |
|---------|------|
| MB-01 | No module imports another module's domain entities or aggregate internals |
| MB-02 | Cross-module communication uses only published commands, queries, events, and shared identifiers |
| MB-03 | Only M-04 (Inventory Balance) mutates on-hand, reserved, or quarantined quantities |
| MB-04 | Only M-02 (Warehouse Network) mutates the location freeze flag — initiated by M-09 events |
| MB-05 | M-13 (Intelligence) subscribes to events only — no write-back to source modules |
| MB-06 | External systems integrate through ACL adapter ports — never directly into domain cores |
| MB-07 | Each module owns its persistence — no shared tables across module boundaries |
| MB-08 | Governance and Identity are consulted synchronously; state changes propagate asynchronously via events |

---

## Phased Module Activation

| Phase | Active Modules | Notes |
|-------|----------------|-------|
| **Phase 1 — MVP (0–6 mo)** | M-01, M-02, M-03, M-04, M-06, M-07, M-09, M-12, M-13 | Core receive, fulfill, count, adjust; basic procurement receipt against PO |
| **Phase 2 (6–12 mo)** | + M-05 (full), M-08, M-10, M-11 | Full procurement, transfers, returns, campaigns |
| **Phase 3 (12–18 mo)** | All modules at full maturity | Finance ACL, advanced Intelligence, valuation snapshots |

---

## Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Solution Architect | | | |
| DDD Solution Architect | | | |
| Delivery Lead | | | |
| Product Owner | | | |

---

*End of System Modules Design*

*Document ID: SRS-SA-003 | Version 1.0 | July 6, 2026*
