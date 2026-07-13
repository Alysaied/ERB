# Actors and External Systems
## Inventory Management System — Event Storming

---

## Document Information

| Attribute | Detail |
|-----------|--------|
| **Document ID** | SRS-ES-004 |
| **Document Title** | Actors and External Systems — Event Storming Catalog |
| **Version** | 1.0 |
| **Status** | Draft |
| **Document Owner** | Domain Expert |
| **Source Documents** | SRS-ES-001 (Domain Events), SRS-ES-002 (Domain Commands), SRS-ES-003 (Domain Policies), SRS-UC-001 (Use Case Catalog) |
| **Date** | July 6, 2026 |
| **Scope** | Business participants only — humans and external systems outside the inventory domain core; excludes internal aggregate handlers |

### Purpose

This document identifies all **Actors** (human business roles) and **External Systems** (organizations and systems outside the Inventory Management System boundary) involved in event storming. For each participant it defines responsibilities, commands they initiate, and domain events they consume or react to in the course of business workflows.

### Participant Types

| Type | Definition |
|------|------------|
| **Human** | Business role with accountability for inventory decisions and operations |
| **External System** | Organization or system outside the IMS bounded context that exchanges business facts or triggers workflows |

### Participant Summary

| Category | IDs | Count |
|----------|-----|-------|
| Human Actors | ACT-001 – ACT-017 | 17 |
| External Systems | EXT-001 – EXT-006 | 6 |
| **Total** | | **23** |

### Legend — Events Consumed

"Events consumed" means the participant **acts upon**, **is notified of**, or **depends on** the business fact — via work queue, alert, dashboard, integration, or policy notification. Read-only inquiry events are included where the participant routinely monitors them for decisions.

---

## Human Actors

---

### ACT-001 — Inventory Controller

| Field | Detail |
|-------|--------|
| **Name** | Inventory Controller |
| **Type** | Human |
| **Responsibilities** | Maintain product catalog, location network, stock policies, governance policies, and ABC classification. Schedule cycle counts and lead physical inventory counts. Monitor network inventory health, movement history, and shrinkage analysis. Establish opening balances at go-live. |
| **Commands Initiated** | `RegisterProduct`, `ChangeProductStatus`, `AssignABCClassification`, `ActivateInventoryLocation`, `DeactivateInventoryLocation`, `ConfigureStoragePosition`, `PublishGovernancePolicy`, `RetireReasonCode`, `UpdateStockPolicyThresholds`, `ScheduleCycleCount`, `StartPhysicalInventoryCount`, `CertifyPhysicalInventoryCount`, `EstablishOpeningBalances` |
| **Events Consumed** | ProductRegistered, ProductStatusChanged, ProductABCClassificationAssigned, InventoryLocationActivated, InventoryLocationDeactivated, GovernancePolicyPublished, StockPolicyThresholdChanged, CycleCountScheduled, CycleCountCompleted, CountVarianceIdentified, PhysicalInventoryCountStarted, PhysicalInventoryCountCertified, LocationFreezeImposed, LocationFreezeReleased, LowStockThresholdBreached, OutOfStockDetected, OverstockDetected, InventoryMovementRecorded, StockAdjusted, StockWrittenOff |

---

### ACT-002 — Buyer

| Field | Detail |
|-------|--------|
| **Name** | Buyer |
| **Type** | Human |
| **Responsibilities** | Create and manage purchase orders, plan inbound deliveries, submit purchase requisitions, and track inbound supply status. Respond to supplier delays and replenishment recommendations. |
| **Commands Initiated** | `SubmitPurchaseRequisition`, `PlacePurchaseOrder`, `CancelPurchaseOrder`, `ScheduleInboundDelivery`, `RecordInboundDelay` |
| **Events Consumed** | PurchaseRequisitionApproved, PurchaseRequisitionRejected, PurchaseOrderPlaced, PurchaseOrderCancelled, InboundDeliveryScheduled, InboundDeliveryDelayed, ReplenishmentRecommended, LowStockThresholdBreached, ReceiptDiscrepancyRecorded, GoodsReceiptVerified |

---

### ACT-003 — Purchasing Manager

| Field | Detail |
|-------|--------|
| **Name** | Purchasing Manager |
| **Type** | Human |
| **Responsibilities** | Approve or reject purchase requisitions. Review low-stock and out-of-stock alerts. Oversee replenishment response and supplier accountability. Coordinate with operations on inbound delays. |
| **Commands Initiated** | `ApprovePurchaseRequisition`, `RejectPurchaseRequisition` |
| **Events Consumed** | PurchaseRequisitionSubmitted, PurchaseRequisitionApproved, PurchaseRequisitionRejected, LowStockThresholdBreached, OutOfStockDetected, ReplenishmentRecommended, InboundDeliveryDelayed, ReceiptDiscrepancyRecorded, PromotionalReadinessGapIdentified, ThreeWayMatchExceptionRaised |

---

### ACT-004 — Receiving Clerk

| Field | Detail |
|-------|--------|
| **Name** | Receiving Clerk |
| **Type** | Human |
| **Responsibilities** | Verify inbound supplier shipments and non-PO receipts. Document receipt discrepancies. Receive and inspect customer returns at the dock. Capture lot/batch and shelf-life data at receipt. |
| **Commands Initiated** | `VerifyGoodsReceipt`, `RecordReceiptDiscrepancy`, `ReceiveCustomerReturn`, `InspectReturnedGoods` |
| **Events Consumed** | InboundDeliveryScheduled, InboundDeliveryDelayed, PurchaseOrderPlaced, ReturnAuthorizationIssued, ReturnAuthorizationExpired, GoodsReceiptVerified, ReceiptDiscrepancyRecorded, CustomerReturnReceived, TransferReceived |

---

### ACT-005 — Warehouse Staff

| Field | Detail |
|-------|--------|
| **Name** | Warehouse Staff |
| **Type** | Human |
| **Responsibilities** | Perform put-away of verified stock. Execute cycle counts. Dispatch and receive inter-location transfers. Move stock to designated storage positions applying rotation rules. |
| **Commands Initiated** | `CompletePutAway`, `SubmitCycleCountResult`, `DispatchTransfer`, `ConfirmTransferReceipt` |
| **Events Consumed** | GoodsReceiptVerified, PutAwayCompleted, CycleCountScheduled, TransferApproved, TransferDispatched, InTransitStockDelayed, LocationFreezeImposed, LocationFreezeReleased |

---

### ACT-006 — Warehouse Picker / Packer

| Field | Detail |
|-------|--------|
| **Name** | Warehouse Picker / Packer |
| **Type** | Human |
| **Responsibilities** | Physically pick, verify, pack, and dispatch customer orders. Apply FIFO/FEFO rotation during pick. Confirm lot/batch capture for traceable products. |
| **Commands Initiated** | `VerifyPick`, `DispatchShipment` |
| **Events Consumed** | CustomerOrderConfirmed, StockReserved, MultiLocationFulfillmentPlanCreated, PickVerified, FulfillmentExceptionRaised, LocationFreezeImposed |

---

### ACT-007 — Warehouse Manager

| Field | Detail |
|-------|--------|
| **Name** | Warehouse Manager |
| **Type** | Human |
| **Responsibilities** | Resolve receipt discrepancies. Manage quarantine and hold stock. Investigate and approve count variances. Submit stock adjustments. Handle fulfillment exceptions. Plan multi-location fulfillment. Disposition returned goods. Respond to operational alerts and transfer delays. |
| **Commands Initiated** | `ResolveReceiptDiscrepancy`, `ApplyQuarantineHold`, `ReleaseQuarantineHold`, `ApproveCountVariance`, `SubmitAdjustment`, `RaiseFulfillmentException`, `CreateMultiLocationFulfillmentPlan`, `QuarantineReturnedGoods`, `WriteOffReturnedGoods`, `RestockReturnedGoods`, `RecordTransferDelay` |
| **Events Consumed** | ReceiptDiscrepancyRecorded, ReceiptDiscrepancyResolved, CountVarianceIdentified, CountVarianceApproved, AdjustmentSubmitted, AdjustmentApproved, AdjustmentRejected, FulfillmentExceptionRaised, TransferRequested, TransferApproved, TransferRejected, InTransitStockDelayed, LowStockThresholdBreached, OutOfStockDetected, QuarantineHoldApplied, QuarantineHoldReleased, ReturnInspected, PromotionalReadinessGapIdentified |

---

### ACT-008 — Operations Director

| Field | Detail |
|-------|--------|
| **Name** | Operations Director |
| **Type** | Human |
| **Responsibilities** | Approve or reject inter-location transfer requests. Authorize material inventory adjustments and write-offs. Oversee network rebalancing. Review operational dashboards and inventory performance. Resolve cross-functional escalations. |
| **Commands Initiated** | `ApproveTransferRequest`, `RejectTransferRequest`, `ApproveAdjustment`, `RejectAdjustment`, `AnalyzeNetworkBalance` |
| **Events Consumed** | TransferRequested, TransferApproved, TransferRejected, AdjustmentSubmitted, AdjustmentApproved, AdjustmentRejected, NetworkImbalanceDetected, ReplenishmentRecommended, ValuationVarianceIdentified, OutOfStockDetected, OverstockDetected, PhysicalInventoryCountCertified, SegregationOfDutiesViolationDetected, InventoryValuationSnapshotPrepared |

---

### ACT-009 — Regional / Store Manager

| Field | Detail |
|-------|--------|
| **Name** | Regional / Store Manager |
| **Type** | Human |
| **Responsibilities** | Request inter-location stock transfers to resolve local shortages. Monitor local stock position and service levels. Coordinate with network locations for redistribution before procurement. |
| **Commands Initiated** | `RequestStockTransfer` |
| **Events Consumed** | TransferApproved, TransferRejected, TransferReceived, OutOfStockDetected, LowStockThresholdBreached, ReplenishmentRecommended, NetworkImbalanceDetected, StockReceived |

---

### ACT-010 — Sales Representative

| Field | Detail |
|-------|--------|
| **Name** | Sales Representative |
| **Type** | Human |
| **Responsibilities** | Confirm order availability against ATP before customer commitment. Inquire network-wide stock visibility for sales conversations. Initiate availability checks on behalf of customers. |
| **Commands Initiated** | `ConfirmOrderAvailability` |
| **Events Consumed** | OrderAvailabilityConfirmed, OutOfStockDetected, LowStockThresholdBreached, PromotionalStockAllocated, QuarantineHoldApplied |

---

### ACT-011 — Customer Service Representative

| Field | Detail |
|-------|--------|
| **Name** | Customer Service Representative |
| **Type** | Human |
| **Responsibilities** | Confirm customer orders and reserve stock. Release reservations on cancellation. Handle partial fulfillment and backorders with customer acknowledgment. Issue return authorizations. Communicate order and shipment status to customers. |
| **Commands Initiated** | `ConfirmCustomerOrder`, `CancelCustomerOrder`, `ReleaseReservation`, `CompletePartialFulfillment`, `RecordBackorder`, `FulfillBackorder`, `IssueReturnAuthorization` |
| **Events Consumed** | OrderAvailabilityConfirmed, CustomerOrderConfirmed, CustomerOrderCancelled, StockReserved, StockReservationReleased, ShipmentDispatched, PartialFulfillmentCompleted, BackorderRecorded, BackorderFulfilled, FulfillmentExceptionRaised, ReturnAuthorizationIssued, ReturnAuthorizationExpired, CustomerReturnReceived, ReturnRestocked |

---

### ACT-012 — Finance Manager

| Field | Detail |
|-------|--------|
| **Name** | Finance Manager |
| **Type** | Human |
| **Responsibilities** | Record supplier invoices. Execute three-way match evaluation. Reconcile inventory valuation with general ledger. Authorize payment after match completion. Investigate valuation variances at month-end close. |
| **Commands Initiated** | `RecordSupplierInvoice`, `EvaluateThreeWayMatch`, `PrepareValuationSnapshot`, `ReconcileInventoryValuation` |
| **Events Consumed** | SupplierInvoiceReceived, ThreeWayMatchCompleted, ThreeWayMatchExceptionRaised, ReceiptDiscrepancyResolved, GoodsReceiptVerified, PurchaseOrderPlaced, InventoryValuationSnapshotPrepared, ValuationVarianceIdentified, StockWrittenOff, ConsignmentOwnershipTransferred, AdjustmentApproved |

---

### ACT-013 — Marketing Manager

| Field | Detail |
|-------|--------|
| **Name** | Marketing Manager |
| **Type** | Human |
| **Responsibilities** | Allocate and release promotional stock ring-fences for campaigns and product launches. Confirm promotional readiness before commercial commitment. Coordinate with purchasing on campaign stock gaps. |
| **Commands Initiated** | `AllocatePromotionalStock`, `ReleasePromotionalAllocation`, `EvaluatePromotionalReadiness` |
| **Events Consumed** | PromotionalStockAllocated, PromotionalAllocationReleased, PromotionalReadinessGapIdentified, StockReceived, LowStockThresholdBreached |

---

### ACT-014 — Internal Auditor

| Field | Detail |
|-------|--------|
| **Name** | Internal Auditor |
| **Type** | Human |
| **Responsibilities** | Review audit trails and inventory movement history. Test segregation-of-duties controls. Verify compliance with governance policies. Investigate control breaches and adjustment authorization chains. |
| **Commands Initiated** | None *(read and review workflows — no mutating inventory commands)* |
| **Events Consumed** | AuditTrailRecorded, InventoryMovementRecorded, SegregationOfDutiesViolationDetected, AdjustmentApproved, AdjustmentRejected, CountVarianceApproved, StockWrittenOff, RoleAssignmentChanged, GovernancePolicyPublished, PhysicalInventoryCountCertified |

---

### ACT-015 — System Administrator

| Field | Detail |
|-------|--------|
| **Name** | System Administrator |
| **Type** | Human |
| **Responsibilities** | Provision user accounts and manage role assignments with location scope. Enforce role-based access and segregation-of-duties constraints at assignment time. Support go-live data import orchestration. |
| **Commands Initiated** | `ProvisionUserAccount`, `ChangeRoleAssignment` |
| **Events Consumed** | UserAccountProvisioned, RoleAssignmentChanged, SegregationOfDutiesViolationDetected |

---

### ACT-016 — Chief Executive Officer

| Field | Detail |
|-------|--------|
| **Name** | Chief Executive Officer |
| **Type** | Human |
| **Responsibilities** | Review executive-level inventory KPIs including turnover, fill rate, accuracy, and working capital impact. Monitor strategic inventory performance for steering decisions. |
| **Commands Initiated** | None *(executive review — no operational commands)* |
| **Events Consumed** | InventoryValuationSnapshotPrepared, OutOfStockDetected, OverstockDetected, NetworkImbalanceDetected, ValuationVarianceIdentified *(via KPI dashboards and executive reports)* |

---

### ACT-017 — Chief Financial Officer

| Field | Detail |
|-------|--------|
| **Name** | Chief Financial Officer |
| **Type** | Human |
| **Responsibilities** | Oversee month-end inventory valuation alignment with financial statements. Review material valuation variances and three-way match control effectiveness. |
| **Commands Initiated** | None *(governance oversight — delegates to Finance Manager)* |
| **Events Consumed** | InventoryValuationSnapshotPrepared, ValuationVarianceIdentified, ThreeWayMatchCompleted, ThreeWayMatchExceptionRaised, StockWrittenOff *(via finance reporting)* |

---

## External Systems

---

### EXT-001 — Supplier / Vendor

| Field | Detail |
|-------|--------|
| **Name** | Supplier / Vendor |
| **Type** | External System |
| **Responsibilities** | Fulfill purchase orders by delivering goods to the receiving location. Communicate shipment schedules and delays. Submit invoices for received goods. Participate in discrepancy resolution and claims. Operate under consignment agreements where applicable. |
| **Commands Initiated** | None *(within IMS boundary — supplier actions occur outside the system)* |
| **Events Consumed** | PurchaseOrderPlaced, PurchaseOrderCancelled, InboundDeliveryScheduled, ReceiptDiscrepancyRecorded *(supplier notified of claims via buyer workflow)* |
| **Business Triggers Into IMS** | Physical shipment arrival → `VerifyGoodsReceipt`; Invoice submission → `RecordSupplierInvoice`; Schedule communication → `ScheduleInboundDelivery` / `RecordInboundDelay` |

---

### EXT-002 — Logistics / Carrier Partner

| Field | Detail |
|-------|--------|
| **Name** | Logistics / Carrier Partner |
| **Type** | External System |
| **Responsibilities** | Transport inbound supplier shipments, outbound customer orders, and inter-location transfers. Provide shipment tracking and delay notifications. Confirm pickup and delivery handoffs. |
| **Commands Initiated** | None |
| **Events Consumed** | ShipmentDispatched, TransferDispatched, InboundDeliveryScheduled |
| **Business Triggers Into IMS** | Delivery confirmation → supports `DispatchShipment` / `ConfirmTransferReceipt` completion; Delay notification → `RecordInboundDelay` / `RecordTransferDelay` |

---

### EXT-003 — Customer (B2B / B2C)

| Field | Detail |
|-------|--------|
| **Name** | Customer (B2B / B2C) |
| **Type** | External System |
| **Responsibilities** | Place orders and request delivery commitments. Acknowledge backorders when partial fulfillment is offered. Initiate return requests per return policy. Receive shipment and return authorization communications. |
| **Commands Initiated** | None *(customer order capture may occur in sales channel — IMS receives availability and fulfillment commands from internal actors)* |
| **Events Consumed** | OrderAvailabilityConfirmed, ShipmentDispatched, PartialFulfillmentCompleted, BackorderRecorded, ReturnAuthorizationIssued, ReturnAuthorizationExpired |
| **Business Triggers Into IMS** | Order request → `ConfirmOrderAvailability` / `ConfirmCustomerOrder`; Cancellation → `CancelCustomerOrder`; Backorder acknowledgment → `RecordBackorder`; Return request → `IssueReturnAuthorization`; Return shipment → `ReceiveCustomerReturn` |

---

### EXT-004 — General Ledger / Finance ERP

| Field | Detail |
|-------|--------|
| **Name** | General Ledger / Finance ERP |
| **Type** | External System |
| **Responsibilities** | Maintain authoritative financial inventory valuation in the general ledger. Receive inventory valuation snapshots for reconciliation. Record payment transactions after three-way match authorization. |
| **Commands Initiated** | None *(Finance Manager initiates reconciliation commands on behalf of finance alignment)* |
| **Events Consumed** | InventoryValuationSnapshotPrepared, ThreeWayMatchCompleted, StockWrittenOff, ConsignmentOwnershipTransferred, AdjustmentApproved |
| **Business Triggers Into IMS** | Ledger balance inquiry → `ReconcileInventoryValuation`; Period-end close cycle → `PrepareValuationSnapshot` |

---

### EXT-005 — Customs / Regulatory Authority

| Field | Detail |
|-------|--------|
| **Name** | Customs / Regulatory Authority |
| **Type** | External System |
| **Responsibilities** | Clear bonded and imported inventory for domestic commerce. Enforce regulatory holds on recalled or restricted goods. Authorize release of quarantined stock under regulatory investigation. |
| **Commands Initiated** | None |
| **Events Consumed** | QuarantineHoldApplied, GoodsReceiptVerified *(bonded receipt)* |
| **Business Triggers Into IMS** | Customs clearance granted → `ReleaseQuarantineHold`; Regulatory hold imposed → `ApplyQuarantineHold` |

---

### EXT-006 — External Auditor

| Field | Detail |
|-------|--------|
| **Name** | External Auditor |
| **Type** | External System |
| **Responsibilities** | Independently review inventory controls, audit trails, and physical count certification during statutory or regulatory audit engagements. Verify three-way match and write-off authorization evidence. |
| **Commands Initiated** | None |
| **Events Consumed** | AuditTrailRecorded, PhysicalInventoryCountCertified, ThreeWayMatchCompleted, AdjustmentApproved, StockWrittenOff, SegregationOfDutiesViolationDetected, InventoryValuationSnapshotPrepared |
| **Business Triggers Into IMS** | None *(read-only access via auditor review workflows)* |

---

## Participant Interaction Map

```
                    ┌──────────────────────────────────────────────────────────┐
                    │              INVENTORY MANAGEMENT SYSTEM                  │
                    │         (Commands → Aggregates → Domain Events)           │
                    └──────────────────────────────────────────────────────────┘
        Commands ▲                              │ Domain Events ▼
                 │                              │
    ┌────────────┼──────────────┐    ┌──────────┼──────────────────────────┐
    │  OPERATIONS & WAREHOUSE   │    │  ALERTS & WORKFLOW ROUTING            │
    │  ACT-001 Inventory Ctrl   │    │  → ACT-003 Purchasing Manager         │
    │  ACT-004 Receiving Clerk  │    │  → ACT-007 Warehouse Manager          │
    │  ACT-005 Warehouse Staff  │    │  → ACT-008 Operations Director        │
    │  ACT-006 Picker / Packer  │    │  → ACT-011 Customer Service Rep       │
    │  ACT-007 Warehouse Mgr    │    └──────────────────────────────────────┘
    └───────────────────────────┘
    ┌───────────────────────────┐    ┌──────────────────────────────────────┐
    │  COMMERCIAL & DEMAND        │    │  FINANCE & GOVERNANCE                │
    │  ACT-010 Sales Rep          │    │  ACT-012 Finance Manager             │
    │  ACT-011 Customer Svc Rep   │    │  ACT-014 Internal Auditor            │
    │  ACT-013 Marketing Manager  │    │  ACT-015 System Administrator        │
    └───────────────────────────┘    │  EXT-004 General Ledger / Finance ERP │
    ┌───────────────────────────┐    └──────────────────────────────────────┘
    │  SUPPLY & NETWORK           │
    │  ACT-002 Buyer              │    ┌──────────────────────────────────────┐
    │  ACT-003 Purchasing Mgr     │    │  EXTERNAL TRADING PARTNERS           │
    │  ACT-008 Operations Dir     │    │  EXT-001 Supplier / Vendor           │
    │  ACT-009 Regional Manager   │    │  EXT-002 Logistics / Carrier         │
    └───────────────────────────┘    │  EXT-003 Customer (B2B / B2C)        │
                                       │  EXT-005 Customs / Regulatory        │
                                       │  EXT-006 External Auditor            │
                                       └──────────────────────────────────────┘
```

---

## Actor-to-Command Matrix

| Actor | Commands Initiated | Count |
|-------|-------------------|-------|
| Inventory Controller | RegisterProduct, ChangeProductStatus, AssignABCClassification, ActivateInventoryLocation, DeactivateInventoryLocation, ConfigureStoragePosition, PublishGovernancePolicy, RetireReasonCode, UpdateStockPolicyThresholds, ScheduleCycleCount, StartPhysicalInventoryCount, CertifyPhysicalInventoryCount, EstablishOpeningBalances | 13 |
| Buyer | SubmitPurchaseRequisition, PlacePurchaseOrder, CancelPurchaseOrder, ScheduleInboundDelivery, RecordInboundDelay | 5 |
| Purchasing Manager | ApprovePurchaseRequisition, RejectPurchaseRequisition | 2 |
| Receiving Clerk | VerifyGoodsReceipt, RecordReceiptDiscrepancy, ReceiveCustomerReturn, InspectReturnedGoods | 4 |
| Warehouse Staff | CompletePutAway, SubmitCycleCountResult, DispatchTransfer, ConfirmTransferReceipt | 4 |
| Warehouse Picker / Packer | VerifyPick, DispatchShipment | 2 |
| Warehouse Manager | ResolveReceiptDiscrepancy, ApplyQuarantineHold, ReleaseQuarantineHold, ApproveCountVariance, SubmitAdjustment, RaiseFulfillmentException, CreateMultiLocationFulfillmentPlan, QuarantineReturnedGoods, WriteOffReturnedGoods, RestockReturnedGoods, RecordTransferDelay | 11 |
| Operations Director | ApproveTransferRequest, RejectTransferRequest, ApproveAdjustment, RejectAdjustment, AnalyzeNetworkBalance | 5 |
| Regional / Store Manager | RequestStockTransfer | 1 |
| Sales Representative | ConfirmOrderAvailability | 1 |
| Customer Service Representative | ConfirmCustomerOrder, CancelCustomerOrder, ReleaseReservation, CompletePartialFulfillment, RecordBackorder, FulfillBackorder, IssueReturnAuthorization | 7 |
| Finance Manager | RecordSupplierInvoice, EvaluateThreeWayMatch, PrepareValuationSnapshot, ReconcileInventoryValuation | 4 |
| Marketing Manager | AllocatePromotionalStock, ReleasePromotionalAllocation, EvaluatePromotionalReadiness | 3 |
| System Administrator | ProvisionUserAccount, ChangeRoleAssignment | 2 |
| Internal Auditor, CEO, CFO | None | 0 |

*Automated domain service commands (`EvaluateStockStatus`, `RecommendReplenishmentAction`, `ReceiveStock`, `ShipStock`, etc.) are executed by IMS policies — not initiated by human actors or external systems directly.*

---

## Actor-to-Event Consumption Matrix

| Actor | Primary Events Consumed (Business Reaction) |
|-------|---------------------------------------------|
| Inventory Controller | Stock policy and catalog lifecycle events; count and variance events; movement and adjustment events for investigation |
| Buyer | Requisition approval, PO lifecycle, inbound schedule/delay, replenishment recommendations |
| Purchasing Manager | Low-stock, out-of-stock, requisition submission, inbound delays, promotional readiness gaps |
| Receiving Clerk | Inbound delivery schedule, return authorization, transfer receipt |
| Warehouse Staff | Verified receipt staging, cycle count assignment, transfer approval/dispatch |
| Warehouse Picker / Packer | Order confirmation, reservation, pick authorization, freeze status |
| Warehouse Manager | Discrepancies, variances, exceptions, transfers, quarantine, operational alerts |
| Operations Director | Transfer requests, adjustment submissions, network imbalance, valuation variance |
| Regional / Store Manager | Transfer decision, local stockout, replenishment recommendations |
| Sales Representative | Availability confirmation result, stockout/low-stock for sales conversations |
| Customer Service Representative | Order lifecycle, shipment, backorder, return authorization and receipt |
| Finance Manager | Invoice, match outcome, valuation snapshot, write-off, consignment transfer |
| Marketing Manager | Promotional allocation, readiness gaps |
| Internal Auditor | Audit trail, movement history, SoD violations, governance changes |
| System Administrator | Account provisioning, role changes, SoD violations |
| CEO / CFO | Valuation, stockout, imbalance, variance *(executive reporting)* |

---

## External System Boundary Interactions

| External System | Direction | Business Interaction |
|-----------------|-----------|----------------------|
| Supplier / Vendor | Inbound to IMS | Delivers goods → triggers goods receipt verification |
| Supplier / Vendor | Outbound from IMS | Notified of PO placement, cancellation, discrepancy claims |
| Logistics / Carrier | Bidirectional | Picks up shipments/transfers; reports delays |
| Customer | Inbound to IMS | Orders, cancellations, return requests, backorder acknowledgments |
| Customer | Outbound from IMS | Availability answers, shipment notices, RMA instructions |
| General Ledger / ERP | Inbound to IMS | Ledger balance for reconciliation |
| General Ledger / ERP | Outbound from IMS | Valuation snapshots, match completion, write-off facts |
| Customs / Regulatory | Inbound to IMS | Clearance decisions → quarantine release or hold |
| External Auditor | Inbound to IMS | Read-only review of audit trail and control evidence |

---

## Excluded Participants

| Participant | Treatment | Rationale |
|-------------|-----------|-----------|
| Aggregate reaction handlers | Internal IMS mechanism | Stock Position handlers executing `ReceiveStock` are not business participants |
| Domain services (policy engine) | Internal IMS mechanism | Automated policies are system behavior, not external actors |
| Email / SMS gateway | Infrastructure | Notification delivery channel, not a business participant |
| Report rendering engine | Infrastructure | Presentation layer, not a business actor |
| Sales order capture system | Out of scope | May feed order intent; IMS receives commands from Sales/CS reps |

---

## Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Domain Expert | | | |
| DDD Architect | | | |
| Senior Business Analyst | | | |
| Solution Architect | | | |

---

*End of Actors and External Systems*

*Document ID: SRS-ES-004 | Version 1.0 | July 6, 2026*
