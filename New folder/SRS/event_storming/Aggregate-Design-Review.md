# Aggregate Design Review
## Inventory Management System — Event Storming Validation

---

## Document Information

| Attribute | Detail |
|-----------|--------|
| **Document ID** | SRS-ES-006 |
| **Document Title** | Aggregate Design Review — Event Storming Validation |
| **Version** | 1.0 |
| **Status** | Draft |
| **Document Owner** | DDD Architect / Domain Expert |
| **Source Documents** | SRS-DM-003 (Domain Aggregates), SRS-ES-001 (Domain Events), SRS-ES-002 (Domain Commands), SRS-ES-003 (Domain Policies), SRS-DM-009 (Domain Model Review) |
| **Date** | July 6, 2026 |
| **Scope** | Validation of 18 aggregates against event storming artifacts — split/merge recommendations only where evidence supports |

### Purpose

This document reviews the **18 domain aggregates** defined in SRS-DM-003 by cross-checking them against Event Storming results: commands issued, domain events produced, invariants enforced, and stated responsibilities. The goal is to confirm consistency boundaries are correct, complete, and aligned with business workflows before solution architecture.

### Review Method

For each aggregate:

| Check | Source |
|-------|--------|
| **Commands handled** | SRS-ES-002 (Domain Commands) — actor commands targeting the aggregate; reaction commands consumed via policies |
| **Events produced** | SRS-ES-001 (Domain Events) — event-to-aggregate origin matrix |
| **Invariants maintained** | SRS-DM-003 + SRS-BR-001 business rules |
| **Responsibilities** | SRS-DM-003 vs. actual command/event coverage from event storming |

### Verdict Legend

| Verdict | Meaning |
|---------|---------|
| **Sound** | Boundary is correct; minor documentation gaps only |
| **Sound with fixes** | Boundary is correct; clarify ownership, naming, or missing events |
| **Split candidate** | Aggregate is too large or mixes inconsistent lifecycles |
| **Merge candidate** | Aggregates should be combined |
| **Gap** | Missing commands, events, or aggregate for a modeled business concept |

---

## Executive Summary

### Overall Assessment

The **18-aggregate design is strategically sound** and validates well against Event Storming. Command-to-aggregate routing is consistent for all operational workflows. Event production aligns with aggregate responsibilities in **16 of 18** cases. Cross-aggregate coordination correctly uses domain events and policies rather than shared transactions.

### Findings Summary

| Category | Count | Details |
|----------|-------|---------|
| **Sound** | 12 | No boundary change required |
| **Sound with fixes** | 5 | Documentation, naming, or event ownership clarifications |
| **Gap** | 1 | Supplier aggregate has no commands or events |
| **Split candidate** | 1 | Customer Order Fulfillment — monitor post-MVP |
| **Merge candidate** | 0 | No merges recommended |
| **New aggregate candidate** | 1 | Opening Balance Establishment (go-live workflow) |

### Priority Actions

1. **Clarify location freeze authority** — Physical Inventory Count initiates; Inventory Location holds state (P1-03).
2. **Add Supplier lifecycle commands and events** — RegisterSupplier, SupplierActivated, etc.
3. **Rename Inventory Adjustment Case root** — single root `AdjustmentCase`, not polymorphic dual roots (P1-08).
4. **Document Opening Balance workflow** — new aggregate or certified subprocess before `EstablishOpeningBalances`.
5. **Clarify promotional ATP segregation** — Commercial aggregate owns intent; Stock Position reacts to events only (P1-02).

---

## Per-Aggregate Verification

---

### Aggregate 1: Product Catalog

| Aspect | Event Storming Validation |
|--------|---------------------------|
| **Commands Handled** | `RegisterProduct`, `ChangeProductStatus`, `AssignABCClassification` |
| **Events Produced** | ProductRegistered (DE-001), ProductStatusChanged (DE-002), ProductABCClassificationAssigned (DE-003) |
| **Invariants Maintained** | BR-027 (discontinued blocking), BR-032 (ABC class), SKU uniqueness, mandatory attributes, traceability declaration |
| **Responsibilities** | Single authoritative SKU identity; lifecycle gatekeeper for procurement and reservation eligibility |

**Verdict: Sound**

Event storming confirms Product Catalog is a low-frequency master-data boundary. `ProductStatusChanged` correctly triggers POL-010 (block ineligible reservations) without Product Catalog knowing about orders. No split or merge required.

**Minor gap:** `UpdateProductAttributes` (non-status edits on UC-001) has no distinct event — acceptable if covered by ProductRegistered semantics on create and audit trail on update; consider `ProductAttributesUpdated` if audit needs demand it.

---

### Aggregate 2: Inventory Location

| Aspect | Event Storming Validation |
|--------|---------------------------|
| **Commands Handled** | `ActivateInventoryLocation`, `DeactivateInventoryLocation`, `ConfigureStoragePosition` |
| **Events Produced** | InventoryLocationActivated (DE-004), InventoryLocationDeactivated (DE-005), StoragePositionConfigured (DE-006) |
| **Invariants Maintained** | Hierarchy validity, operational status, closure disposition, freeze compliance (BR-024) |
| **Responsibilities** | Location network definition, storage layout, operational status |

**Verdict: Sound with fixes**

Commands and events align for location lifecycle. **Freeze events (DE-007, DE-008) are produced by Physical Inventory Count, not Inventory Location** — event storming exposes an authority split:

| Role | Aggregate |
|------|-----------|
| **Freeze initiator** | Physical Inventory Count (`StartPhysicalInventoryCount`, `CertifyPhysicalInventoryCount`) |
| **Freeze state holder** | Inventory Location (applies freeze on `LocationFreezeImposed`, releases on `LocationFreezeReleased`) |

**Recommendation:** Inventory Location should **consume** DE-007/DE-008 and mutate its `frozen` flag. DS-014 (Freeze Guard) reads **Inventory Location state only**. Do not merge aggregates — clarify integration contract.

**Gap:** `EstablishOpeningBalances` (CMD-058) targets Stock Position, not Location. Location activation (DE-004) should require opening balance completion as a precondition — see New Aggregate Candidate below.

---

### Aggregate 3: Supplier

| Aspect | Event Storming Validation |
|--------|---------------------------|
| **Commands Handled** | **None documented** |
| **Events Produced** | **None documented** |
| **Invariants Maintained** | Supplier code uniqueness, active status for PO, consignment indicator (BR-031), payment terms |
| **Responsibilities** | Supplier commercial identity, consignment terms, procurement reference |

**Verdict: Gap**

Event storming reveals Supplier is referenced by `PlacePurchaseOrder` but has **no lifecycle commands or events**. Consignment ownership (DE-022) depends on supplier agreement data that cannot change without audit trail.

**Recommendation — do not merge.** Supplier is correctly separate from Purchase Order. **Add commands and events:**

| Command | Event |
|---------|-------|
| `RegisterSupplier` | SupplierRegistered |
| `UpdateSupplierTerms` | SupplierTermsUpdated |
| `ActivateSupplier` / `DeactivateSupplier` | SupplierStatusChanged |

Move bounded-context placement to **Procurement & Supplier** per SRS-DM-009 P1-01 (align SRS-DM-003 with SRS-DM-007).

---

### Aggregate 4: Inventory Governance

| Aspect | Event Storming Validation |
|--------|---------------------------|
| **Commands Handled** | `PublishGovernancePolicy`, `RetireReasonCode` |
| **Events Produced** | GovernancePolicyPublished (DE-009), ReasonCodeRetired (DE-010) |
| **Invariants Maintained** | BR-020, BR-021, BR-006, BR-008 (thresholds/tolerances), reason code uniqueness, single effective policy version |
| **Responsibilities** | Organization-wide governance parameters and reason code taxonomy |

**Verdict: Sound**

Governance is correctly a reference aggregate consulted by Adjustment Case, Goods Receipt, and Supplier Invoice — not mutated by them. POL-051 and POL-052 validate downstream policy consumption. Reason Code as child entity is acceptable; expose read-only OHS for other contexts.

**No merge** with Stock Policy — different concern (exception governance vs. replenishment thresholds).

---

### Aggregate 5: Stock Position

| Aspect | Event Storming Validation |
|--------|---------------------------|
| **Commands Handled** | `ReserveStock`, `ReleaseReservation`, `ReceiveStock`, `ShipStock`, `ApplyApprovedAdjustment`, `ApplyApprovedWriteOff`, `ApplyQuarantineHold`, `ReleaseQuarantineHold`, `TransferConsignmentOwnership`, `EstablishOpeningBalances`, `DispatchTransferStock` *(reaction)* |
| **Events Produced** | StockReceived (DE-011), StockReserved (DE-012), StockReservationReleased (DE-013), StockShipped (DE-014), StockAdjusted (DE-015), StockWrittenOff (DE-016), QuarantineHoldApplied (DE-017), QuarantineHoldReleased (DE-018), ConsignmentOwnershipTransferred (DE-022), LowStockThresholdBreached (DE-068), OutOfStockDetected (DE-069), OverstockDetected (DE-070), InventoryMovementRecorded (DE-074) |
| **Invariants Maintained** | BR-001, BR-002, BR-003, BR-010, BR-013, BR-017, BR-030, BR-031; non-negative on-hand; ATP formula |
| **Responsibilities** | Authoritative quantity state per product-location; lot/batch and quarantine as child entities |

**Verdict: Sound with fixes**

This is the **most validated aggregate** in event storming — 13 reaction entry points from policies, 13 events produced. Correctly scoped to product + location.

**Fixes required:**

1. **Lot/batch identity (P1-05):** Document explicitly — one Stock Position per product-location; Lot/Batch entities hold sub-quantities that must sum to on-hand.
2. **Promotional ring-fence (P1-02):** Stock Position reacts to DE-020/DE-021; never self-initiates ring-fence. POL-026 is a projection-side effect, not a command on Stock Position root from marketing.
3. **Remove pipeline quantity** from aggregate state — inbound expected is a read model (RM-008), not Stock Position field (AG-02).
4. **EvaluateStockStatus** (DE-068–070) is emitted after quantity mutations via domain service — confirm these are raised by Stock Position root after `recalculateStatus()`, not a separate aggregate.

**No split.** Lot/Batch and Quarantine Hold belong inside — ATP changes immediately on hold application.

---

### Aggregate 6: Stock Policy

| Aspect | Event Storming Validation |
|--------|---------------------------|
| **Commands Handled** | `UpdateStockPolicyThresholds` |
| **Events Produced** | StockPolicyThresholdChanged (DE-019) |
| **Invariants Maintained** | BR-009, BR-010, BR-012; non-negative thresholds; effective dating; immutable history |
| **Responsibilities** | Replenishment thresholds per product-location |

**Verdict: Sound**

Correct separation from Stock Position confirmed by event storming: policy changes are infrequent (CMD-011) and trigger POL-021 (`EvaluateStockStatus`) without locking stock during fulfillment.

**No merge** with Stock Position — would couple high-frequency mutations with low-frequency policy edits.

---

### Aggregate 7: Purchase Requisition

| Aspect | Event Storming Validation |
|--------|---------------------------|
| **Commands Handled** | `SubmitPurchaseRequisition`, `ApprovePurchaseRequisition`, `RejectPurchaseRequisition` |
| **Events Produced** | PurchaseRequisitionSubmitted (DE-023), PurchaseRequisitionApproved (DE-024), PurchaseRequisitionRejected (DE-025) |
| **Invariants Maintained** | BR-027, BR-010, BR-011; active products only; approval before PO conversion |
| **Responsibilities** | Internal procurement intent with approval workflow |

**Verdict: Sound**

POL-019 correctly routes approved requisitions to `PlacePurchaseOrder` on a **new** Purchase Order aggregate — not conversion in-place. POL-029 validates BR-011 network check at submission.

**No merge** with Purchase Order — distinct lifecycles (internal intent vs. supplier commitment) confirmed by separate event chains.

---

### Aggregate 8: Purchase Order

| Aspect | Event Storming Validation |
|--------|---------------------------|
| **Commands Handled** | `PlacePurchaseOrder`, `CancelPurchaseOrder`, `ScheduleInboundDelivery`, `RecordInboundDelay` |
| **Events Produced** | PurchaseOrderPlaced (DE-026), PurchaseOrderCancelled (DE-027), InboundDeliveryScheduled (DE-028), InboundDeliveryDelayed (DE-029) |
| **Invariants Maintained** | BR-007, BR-027; supplier/location references; ordered vs. received tracking; status transitions |
| **Responsibilities** | Commercial supplier commitment; inbound delivery schedule |

**Verdict: Sound**

Expected Inbound Delivery correctly embedded — `ScheduleInboundDelivery` and `RecordInboundDelay` mutate the same aggregate. Event storming shows clean handoff to Goods Receipt via `VerifyGoodsReceipt` referencing PO by identity.

**No split** of Expected Inbound Delivery — would orphan delivery schedule from commercial commitment.

---

### Aggregate 9: Goods Receipt

| Aspect | Event Storming Validation |
|--------|---------------------------|
| **Commands Handled** | `VerifyGoodsReceipt`, `RecordReceiptDiscrepancy`, `ResolveReceiptDiscrepancy`, `CompletePutAway` |
| **Events Produced** | GoodsReceiptVerified (DE-030), ReceiptDiscrepancyRecorded (DE-031), ReceiptDiscrepancyResolved (DE-032), PutAwayCompleted (DE-033) |
| **Invariants Maintained** | BR-004, BR-005, BR-006, BR-007, BR-016, BR-017, BR-030; verify before accept; put-away before ATP |
| **Responsibilities** | Dock-to-storage inbound workflow including discrepancy and put-away |

**Verdict: Sound with fixes**

Receipt → discrepancy → put-away as one aggregate is **validated by POL-011, POL-012, POL-014** — prevents stock entering ATP without verified, stowed goods.

**Fixes:**

1. **Ad-hoc receipt (BR-007 exception):** Event storming has no `AdHocReceiptAuthorized` event — add authorization artifact and command (P1-06).
2. **Customer return boundary:** `ReceiveCustomerReturn` targets Customer Return Case, not Goods Receipt. UC-011 overlap is resolved by **separate aggregates** sharing Receipt Verification domain service (DS-008) — do not merge (REL-ISSUE-05).
3. **Bonded goods:** POL-013 routes to `ApplyQuarantineHold` on Stock Position after DE-030 — Goods Receipt must flag bonded status; clearance is not put-away completion.

**No split** of Put-Away or Receipt Discrepancy — would violate BR-005 and create orphan "verified but not stowed" states.

---

### Aggregate 10: Supplier Invoice

| Aspect | Event Storming Validation |
|--------|---------------------------|
| **Commands Handled** | `RecordSupplierInvoice`, `EvaluateThreeWayMatch` |
| **Events Produced** | SupplierInvoiceReceived (DE-034), ThreeWayMatchCompleted (DE-035), ThreeWayMatchExceptionRaised (DE-081) |
| **Invariants Maintained** | BR-008; match before payment; tolerance from Governance |
| **Responsibilities** | Invoice recording and three-way match outcome |

**Verdict: Sound**

Correctly consults PO and Goods Receipt by identity without mutating them. POL-015 through POL-018 validate the procure-to-pay read side.

**No merge** with Purchase Order — financial control boundary is independent. **Context note:** evaluate finance ERP ACL at architecture phase (AG-03) — acceptable for MVP.

---

### Aggregate 11: Customer Order Fulfillment

| Aspect | Event Storming Validation |
|--------|---------------------------|
| **Commands Handled** | `ConfirmOrderAvailability`, `ConfirmCustomerOrder`, `CancelCustomerOrder`, `CreateMultiLocationFulfillmentPlan`, `VerifyPick`, `DispatchShipment`, `CompletePartialFulfillment`, `RecordBackorder`, `FulfillBackorder`, `RaiseFulfillmentException` |
| **Events Produced** | OrderAvailabilityConfirmed (DE-036), CustomerOrderConfirmed (DE-037), CustomerOrderCancelled (DE-038), PickVerified (DE-039), ShipmentDispatched (DE-040), PartialFulfillmentCompleted (DE-041), BackorderRecorded (DE-042), BackorderFulfilled (DE-043), FulfillmentExceptionRaised (DE-044), MultiLocationFulfillmentPlanCreated (DE-045) |
| **Invariants Maintained** | BR-001, BR-002, BR-003, BR-028, BR-010, BR-029; order line quantity reconciliation; pick before ship |
| **Responsibilities** | Full order lifecycle from availability through shipment and backorder |

**Verdict: Sound — split candidate post-MVP**

Event storming validates the unified boundary: POL-001 through POL-008 form a coherent chain. Order line invariant `requested = reserved + picked + backordered + cancelled` requires single aggregate.

**Tension identified:**

| Concern | Evidence |
|---------|----------|
| **Reservation dual-tracking** | Customer Order holds `InventoryReservation` entity; Stock Position holds `reserved` quantity — coordinated by DS-002 and POL-001. Correct pattern but requires careful saga on partial failure. |
| **Concurrency** | High-volume SKUs: many `ReserveStock` + `DispatchShipment` commands on same Stock Position from different orders. |
| **Aggregate size** | 5 child entity types with long-lived state. |

**Split candidate (post-MVP, not now):** Extract **Shipment** as separate aggregate if ship-confirm contention is observed. Would require compensation saga: `PickVerified` → Shipment aggregate → `ShipmentDispatched` → `ShipStock`. **Do not split for MVP.**

**Fix:** Add `FulfillmentException` as entity inside aggregate (ME-04) — event DE-044 exists but no persistent case entity documented.

---

### Aggregate 12: Stock Transfer

| Aspect | Event Storming Validation |
|--------|---------------------------|
| **Commands Handled** | `RequestStockTransfer`, `ApproveTransferRequest`, `RejectTransferRequest`, `DispatchTransfer`, `ConfirmTransferReceipt`, `RecordTransferDelay` |
| **Events Produced** | TransferRequested (DE-046), TransferApproved (DE-047), TransferRejected (DE-048), TransferDispatched (DE-049), TransferReceived (DE-050), InTransitStockDelayed (DE-051) |
| **Invariants Maintained** | BR-011, BR-012, BR-010, BR-017; source minimum protection; in-transit excluded from ATP |
| **Responsibilities** | Request → approval → dispatch → in-transit → receipt lifecycle |

**Verdict: Sound**

Event storming **confirms merge of Transfer Request into Stock Transfer** (P1-04 resolved). Transfer Request is a lifecycle phase, not a separate aggregate. POL-030 through POL-032 validate cross-Stock-Position coordination via events.

**No split** of In-Transit Stock — meaningless without parent transfer.

---

### Aggregate 13: Cycle Count

| Aspect | Event Storming Validation |
|--------|---------------------------|
| **Commands Handled** | `ScheduleCycleCount`, `SubmitCycleCountResult` |
| **Events Produced** | CycleCountScheduled (DE-052), CycleCountCompleted (DE-053) |
| **Invariants Maintained** | BR-018, BR-032, BR-019; blind count; no direct stock mutation |
| **Responsibilities** | Partial count scheduling and result recording |

**Verdict: Sound**

POL-036 correctly spawns `IdentifyCountVariance` on Adjustment Case — Cycle Count does not mutate Stock Position. Segregation of duties enforced by aggregate boundary.

**No merge** with Physical Inventory Count — different protocols (partial blind count vs. wall-to-wall freeze). Different actors, events, and invariants.

---

### Aggregate 14: Physical Inventory Count

| Aspect | Event Storming Validation |
|--------|---------------------------|
| **Commands Handled** | `StartPhysicalInventoryCount`, `CertifyPhysicalInventoryCount` |
| **Events Produced** | PhysicalInventoryCountStarted (DE-056), PhysicalInventoryCountCertified (DE-057), LocationFreezeImposed (DE-007), LocationFreezeReleased (DE-008) |
| **Invariants Maintained** | BR-024; full location scope; freeze during count; variances routed not applied |
| **Responsibilities** | Wall-to-wall count event; freeze initiation; certification |

**Verdict: Sound with fixes**

See Aggregate 2 for freeze authority pattern. POL-034 and POL-035 validate freeze blocking across Goods Receipt, Order Fulfillment, and Stock Transfer.

**No merge** with Cycle Count or Inventory Location.

**Consider:** Opening Balance at go-live may reuse Physical Inventory Count pattern or become separate aggregate (below).

---

### Aggregate 15: Inventory Adjustment Case

| Aspect | Event Storming Validation |
|--------|---------------------------|
| **Commands Handled** | `IdentifyCountVariance` *(reaction)*, `ApproveCountVariance`, `SubmitAdjustment`, `ApproveAdjustment`, `RejectAdjustment` |
| **Events Produced** | CountVarianceIdentified (DE-054), CountVarianceApproved (DE-055), AdjustmentSubmitted (DE-058), AdjustmentApproved (DE-059), AdjustmentRejected (DE-060) |
| **Invariants Maintained** | BR-019, BR-020, BR-021, BR-022, BR-023; investigation before adjust; SoD; mandatory reason code |
| **Responsibilities** | Variance investigation, adjustment/write-off governance, stock mutation authorization |

**Verdict: Sound with fixes**

Event storming validates the governance chain: POL-036 → POL-037 → POL-038 → POL-039 → POL-025 (`ApplyApprovedAdjustment` on Stock Position).

**Fix (P1-08):** Rename root to **`AdjustmentCase`** with `CaseOrigin` value object (`CountOriginated` | `DirectRequest`). Count Variance and Stock Adjustment are **phases/entities**, not alternate roots.

**Return write-off path (REL-ISSUE-07):** `WriteOffReturnedGoods` on Customer Return Case should **create Adjustment Case** for write-off governance rather than directly calling `ApplyApprovedWriteOff`. Event storming currently shows direct path — **align policy POL-047** to route through Adjustment Case for BR-023 compliance.

**No split** of write-off from adjustment — shared governance state machine.

---

### Aggregate 16: Customer Return Case

| Aspect | Event Storming Validation |
|--------|---------------------------|
| **Commands Handled** | `IssueReturnAuthorization`, `ExpireReturnAuthorization`, `ReceiveCustomerReturn`, `InspectReturnedGoods`, `RestockReturnedGoods`, `QuarantineReturnedGoods`, `WriteOffReturnedGoods` |
| **Events Produced** | ReturnAuthorizationIssued (DE-061), ReturnAuthorizationExpired (DE-062), CustomerReturnReceived (DE-063), ReturnInspected (DE-064), ReturnRestocked (DE-065), ReturnQuarantined (DE-066), ReturnWrittenOff (DE-067) |
| **Invariants Maintained** | BR-025, BR-026, BR-004, BR-013, BR-023; RMA before receipt; inspect before restock |
| **Responsibilities** | Reverse logistics: authorize → receive → inspect → disposition |

**Verdict: Sound**

POL-043 through POL-048 validate strict sequencing. Return Authorization as root correctly gates all subsequent steps.

**No merge** with Goods Receipt — different entry (RMA vs. PO) and disposition rules (BR-026). Shared verification logic belongs in DS-008, not shared aggregate.

**Fix:** Write-off disposition should spawn Adjustment Case (see Aggregate 15).

---

### Aggregate 17: Promotional Stock Allocation

| Aspect | Event Storming Validation |
|--------|---------------------------|
| **Commands Handled** | `AllocatePromotionalStock`, `ReleasePromotionalAllocation`, `EvaluatePromotionalReadiness` |
| **Events Produced** | PromotionalStockAllocated (DE-020), PromotionalAllocationReleased (DE-021), PromotionalReadinessGapIdentified (DE-072) |
| **Invariants Maintained** | BR-029; ring-fence during campaign; allocation ≤ available; effective period |
| **Responsibilities** | Campaign stock ring-fence intent and lifecycle |

**Verdict: Sound with fixes**

Commercial intent correctly separated from Stock Position mechanics. POL-026, POL-027, POL-049 validate event-driven ATP segregation.

**Fix (P1-02):** Remove Promotional Stock Allocation from Inventory Balance entity grouping in SRS-DM-001. Stock Position **only reacts** to DE-020/DE-021 — never owns campaign definition.

**No merge** with Customer Order Fulfillment — marketing lifecycle ≠ order lifecycle.

---

### Aggregate 18: User Account

| Aspect | Event Storming Validation |
|--------|---------------------------|
| **Commands Handled** | `ProvisionUserAccount`, `ChangeRoleAssignment`; `ValidateSegregationOfDuties` *(intercepts approvals)* |
| **Events Produced** | UserAccountProvisioned (DE-079), RoleAssignmentChanged (DE-080), SegregationOfDutiesViolationDetected (DE-078) |
| **Invariants Maintained** | BR-019, BR-021; unique user ID; SoD at assignment; location scope validity |
| **Responsibilities** | Identity, role assignment, SoD enforcement |

**Verdict: Sound**

POL-053 and POL-055 validate cross-cutting SoD interception. User Account correctly does not belong inside operational aggregates.

**No merge** with Inventory Governance — identity vs. transaction governance are distinct concerns.

---

## Split and Merge Recommendations

### Recommended Splits

| Aggregate | Split Proposal | Rationale | When |
|-----------|----------------|-----------|------|
| **Customer Order Fulfillment** | Extract **Shipment** as separate aggregate | Reduce contention; long pick-to-ship window decoupled from order state | Post-MVP if metrics show contention |
| *(none others)* | — | All other boundaries validated by invariant cohesion | — |

### Recommended Merges

| Aggregates Proposed | Verdict | Rationale |
|---------------------|---------|-----------|
| Purchase Requisition + Purchase Order | **Reject** | Different approval vs. commercial commitment; event storming shows clean cross-aggregate handoff (POL-019) |
| Cycle Count + Physical Inventory Count | **Reject** | BR-018 blind partial count vs. BR-024 wall-to-wall freeze — incompatible invariants |
| Goods Receipt + Put-Away (separate) | **Reject** | BR-005 requires verified + stowed in one boundary; POL-012 depends on it |
| Transfer Request + Stock Transfer (separate) | **Reject** | Already correctly merged; event storming confirms single lifecycle |
| Customer Return Case + Goods Receipt | **Reject** | Different authorization (RMA vs. PO); shared DS-008 only |
| Stock Position + Stock Policy | **Reject** | Frequency and lock contention differ; POL-021 depends on separation |
| Supplier + Purchase Order | **Reject** | Master data vs. transactional document |
| Inventory Location + Physical Inventory Count | **Reject** | Different concerns; integrate via freeze events, not merge |
| Reason Code + Governance Policy (separate) | **Reject** | Reason codes version with policy; child entity acceptable |

### New Aggregate Candidate

| Proposed Aggregate | Rationale | Commands | Events |
|--------------------|-----------|----------|--------|
| **Opening Balance Establishment** | UC-046 / DE-004 require verified baseline before location go-live; `EstablishOpeningBalances` currently has no governing workflow aggregate (P1-07) | `SubmitOpeningBalance`, `CertifyOpeningBalance` | OpeningBalanceCertified → triggers `EstablishOpeningBalances` per product line on Stock Position |

**Alternative:** Treat as a specialized **Physical Inventory Count** at go-live (simpler, reuses BR-024 freeze pattern). Business must confirm with stakeholders.

---

## Cross-Aggregate Consistency Matrix

| Event Storming Flow | Aggregates Involved | Consistent? | Note |
|-------------------|---------------------|-------------|------|
| Inbound: PO → Receipt → Put-away → Stock | Purchase Order → Goods Receipt → Stock Position | Yes | POL-011, POL-012 |
| Order: Confirm → Reserve → Pick → Ship → Deduct | Customer Order → Stock Position | Yes | POL-001, POL-004, POL-005 |
| Count: Count → Variance → Approve → Adjust | Cycle Count → Adjustment Case → Stock Position | Yes | POL-036–039, POL-025 |
| Transfer: Request → Approve → Dispatch → Receive | Stock Transfer → Stock Position (×2) | Yes | POL-030–032 |
| Return: RMA → Receive → Inspect → Restock | Customer Return → Stock Position | Yes | POL-043–045 |
| Freeze: Start count → Block mutations → Release | Physical Count → Inventory Location → all mutators | **Fix needed** | P1-03 state holder pattern |
| Promotional: Allocate → Segregate ATP | Promotional Allocation → Stock Position | **Fix needed** | P1-02 react-only on Stock Position |
| Finance: Invoice → Match → Pay | Supplier Invoice → (read PO, GR) | Yes | POL-015–018 |
| Write-off from return | Customer Return → Adjustment Case → Stock Position | **Fix needed** | Route through governance |

---

## Event Coverage Gaps

| Gap | Affected Aggregate | Recommendation |
|-----|-------------------|----------------|
| No Supplier lifecycle events | Supplier | Add DE-SUP-001 through DE-SUP-003 |
| No ad-hoc receipt authorization | Goods Receipt | Add aggregate child or sibling authorization; `AdHocReceiptAuthorized` |
| No opening balance certification | Inventory Location / new aggregate | Add Opening Balance workflow before DE-004 |
| `UpdateProductAttributes` without event | Product Catalog | Add `ProductAttributesUpdated` or confirm audit trail suffices |
| Return write-off bypasses Adjustment Case | Customer Return Case | Align POL-047 with Adjustment Case routing |
| `ReplenishmentRecommended` / `NetworkImbalanceDetected` | No aggregate (correct) | Remain cross-cutting domain service outcomes → read models |

---

## Invariant Stress Test Results

| Business Rule | Enforcing Aggregate(s) | Event Storming Validates? |
|---------------|------------------------|---------------------------|
| BR-001 ATP-only commitment | Stock Position + Customer Order (DS-001) | Yes — POL-001, RM-002 |
| BR-002 Reservation at confirmation | Stock Position + Customer Order | Yes — POL-001 |
| BR-003 Verified pick before ship | Customer Order | Yes — POL-004, POL-005 |
| BR-005 Put-away before availability | Goods Receipt → Stock Position | Yes — POL-011, POL-012 |
| BR-007 PO required for receipt | Purchase Order + Goods Receipt | Partial — ad-hoc path missing |
| BR-008 Three-way match | Supplier Invoice | Yes — POL-015–018 |
| BR-009 Reorder at reorder level | Stock Policy → Stock Position | Yes — POL-021, POL-022 |
| BR-011 Network before purchase | Purchase Requisition (DS-004) | Yes — POL-029 |
| BR-012 Source minimum on transfer | Stock Transfer (DS-006) | Yes — POL-030 |
| BR-018 Blind cycle count | Cycle Count | Yes — POL-036 |
| BR-019 Independent count approval | Adjustment Case + User Account | Yes — POL-037, POL-053 |
| BR-022 Investigate before adjust | Adjustment Case | Yes — POL-036, POL-039 |
| BR-024 Physical inventory freeze | Physical Count + Inventory Location | Partial — authority split needs fix |
| BR-025 Return authorization | Customer Return Case | Yes — POL-043, POL-044 |
| BR-026 Inspect before restock | Customer Return Case | Yes — POL-045–047 |
| BR-029 Promotional ring-fence | Promotional Allocation + Stock Position | Partial — ATP ownership clarify |
| BR-031 Consignment ownership | Stock Position (DS-021) | Yes — POL-028 |

---

## Final Verdict

### Aggregate Design Quality: **Good — proceed with documented fixes**

The 18-aggregate model is **validated by Event Storming** as a coherent set of consistency boundaries. Command routing, event production, and policy reactions are aligned for all core lifecycles (inbound, fulfillment, transfer, count-to-adjust, returns, procurement).

### Required Before Architecture

1. Fix **location freeze** command/event ownership (Physical Count initiates, Location holds).
2. Add **Supplier** lifecycle commands and events.
3. Rename **Adjustment Case** root; fix **return write-off** routing through governance.
4. Clarify **promotional ATP** as event-driven reaction on Stock Position.
5. Define **opening balance** workflow aggregate or reuse physical count pattern.

### Deferred (Post-MVP)

1. Monitor **Customer Order Fulfillment** for Shipment extraction.
2. Evaluate **Supplier Invoice** finance ERP boundary.
3. Add **Fulfillment Exception** entity inside order aggregate.

### No Merges Recommended

Event storming provides **no evidence** that any current pair of aggregates should be merged. Proposed merges would weaken invariant enforcement or couple independent lifecycles.

---

## Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| DDD Architect | | | |
| Domain Expert | | | |
| Solution Architect | | | |
| Senior Business Analyst | | | |

---

*End of Aggregate Design Review*

*Document ID: SRS-ES-006 | Version 1.0 | July 6, 2026*
