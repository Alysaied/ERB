# Event Storming Hotspots
## Inventory Management System

---

## Document Information

| Attribute | Detail |
|-----------|--------|
| **Document ID** | SRS-ES-007 |
| **Document Title** | Event Storming Hotspots — Unresolved Business Issues |
| **Version** | 1.0 |
| **Status** | Draft |
| **Document Owner** | Domain Expert |
| **Source Documents** | SRS-ES-001 through SRS-ES-006, SRS-DM-009 (Domain Model Review), SRS-BR-001, SRS-UC-001 |
| **Date** | July 6, 2026 |
| **Scope** | Unresolved business uncertainties discovered during event storming — not technical design decisions |

### Purpose

In Event Storming, a **hotspot** marks an area where the business model is uncertain, contested, or incomplete. Hotspots block confident aggregate design, policy definition, or rule enforcement until domain experts resolve them. This document captures hotspots surfaced by cross-checking commands, events, policies, aggregates, and business rules.

### Hotspot Severity

| Severity | Meaning |
|----------|---------|
| **Critical** | Blocks architecture or MVP rule enforcement |
| **High** | Affects core workflows; workaround risky |
| **Medium** | Phase 2 scope or edge case; document assumption for MVP |
| **Low** | Clarification improves model; deferrable |

### Hotspot Summary

| ID | Hotspot | Severity | Status |
|----|---------|----------|--------|
| HS-001 | Ad-Hoc Receipt Without Purchase Order | Critical | Open |
| HS-002 | Opening Balance and Location Go-Live | Critical | Open |
| HS-003 | Location Freeze Authority During Physical Count | High | Open |
| HS-004 | Promotional Ring-Fence vs. General ATP | High | Open |
| HS-005 | Lot/Batch Quantity Model for Traceable Products | High | Open |
| HS-006 | Consignment Ownership Transfer Trigger | High | Open |
| HS-007 | Order Reservation and Stock Position Coordination | High | Open |
| HS-008 | Return Write-Off Governance Path | High | Open |
| HS-009 | Bonded Inventory vs. General Quarantine | Medium | Open |
| HS-010 | Transfer-Before-Buy vs. Purchase Decision | Medium | Open |
| HS-011 | Backorder Priority and Auto-Fulfillment | Medium | Open |
| HS-012 | Safety Stock Override Authorization | Medium | Open |
| HS-013 | Supplier Master Data Ownership and Lifecycle | Medium | Open |
| HS-014 | Finance System Boundary (Invoice and Valuation) | Medium | Open |
| HS-015 | Product Supersession and SKU Runout | Low | Open |
| HS-016 | Reservation Expiry and Stale Commitments | Low | Open |

**Total Hotspots:** 16 | **Open:** 16

---

## HS-001 — Ad-Hoc Receipt Without Purchase Order

| Field | Detail |
|-------|--------|
| **Area of Uncertainty** | How supplier goods may be received when no purchase order exists, and how financial controls apply afterward |
| **Why It Is Complex** | BR-007 requires a PO for supplier receipt *except explicitly approved ad-hoc exceptions*, but the exception matrix is undefined (BRD ISS-020). Event storming has `VerifyGoodsReceipt` and POL-011 for PO-backed flow only. No command, event, authorization artifact, or policy exists for the exception path. Business Rule Dependencies flag **CF-007**: ad-hoc receipt conflicts with BR-008 three-way match assumptions. Validation rules VR-040 and VR-042 reference ad-hoc approval but no workflow owns it. |
| **Related Business Processes** | BP-07 (Goods Receipt & Verification), BP-05 (Purchase Order Placement), BP-30 (Inventory Valuation & Financial Reconciliation) |
| **Questions Requiring Clarification** | 1. Who may authorize an ad-hoc receipt (role and approval level)? 2. Is retroactive PO creation required, and within what time limit? 3. What quantity/value caps apply per governance policy? 4. How does three-way match work when no PO existed at receipt — alternate match rules or retroactive PO? 5. Can ad-hoc receipt apply to consignment or bonded goods? 6. What reason codes and audit evidence are mandatory? |
| **Recommended Next Steps** | 1. Workshop with Purchasing, Receiving, and Finance to define ad-hoc exception matrix. 2. Add **Ad-Hoc Receipt Authorization** concept with `AdHocReceiptAuthorized` event. 3. Formalize **BR-033** (or extend BR-007) and resolve CF-007 with Finance. 4. Update Goods Receipt aggregate and POL-011 with exception branch. 5. Document in ubiquitous language. |

---

## HS-002 — Opening Balance and Location Go-Live

| Field | Detail |
|-------|--------|
| **Area of Uncertainty** | How opening stock balances are established, verified, and approved before a location becomes transactionally active |
| **Why It Is Complex** | `ActivateInventoryLocation` emits DE-004 and `EstablishOpeningBalances` creates Stock Position quantities, but no aggregate governs the verification workflow. UC-046 covers bulk import; VR-025 requires approver sign-off — yet no commands or events model certification. Exception EX-004 (opening balance dispute) exists without resolution workflow. Constraint **CF-009** tensions go-live continuity (operations cannot shut down) vs. FR-010 (no transactions until balance approved). Event storming gap: first Stock Position creation lacks governing business process. |
| **Related Business Processes** | BP-02 (Location & Warehouse Setup), BP-01 (Product Master Data Management), BP-12 (Full Physical Inventory Count) |
| **Questions Requiring Clarification** | 1. Is opening balance established by physical count, system import, or either? 2. Who approves opening balances (Inventory Controller, Finance, Operations Director)? 3. Can a location be *active* in read-only/staging mode before balance certification? 4. What happens when opening balance dispute arises at go-live (EX-004)? 5. Is a wall-to-wall count required for new locations or only data import with sample verification? 6. Relationship between FR-010 and FR-090 import — same workflow or alternatives? |
| **Recommended Next Steps** | 1. Business decision: count-validated vs. import-only go-live. 2. Model **Opening Balance Establishment** aggregate or subprocess with `SubmitOpeningBalance`, `CertifyOpeningBalance`, `OpeningBalanceCertified` event. 3. Add **BR-043** Opening Balance Certification (per Business Rule Catalog Review). 4. Define precondition chain: certify → activate location → establish balances on Stock Position. 5. Resolve CF-009 with staging-mode business rule if needed. |

---

## HS-003 — Location Freeze Authority During Physical Count

| Field | Detail |
|-------|--------|
| **Area of Uncertainty** | Which business concept owns location operational freeze during wall-to-wall physical inventory count |
| **Why It Is Complex** | BR-024 requires freeze during physical count. Events DE-007 (`LocationFreezeImposed`) and DE-008 (`LocationFreezeReleased`) originate from **Physical Inventory Count**, but **Inventory Location** aggregate also lists freeze enforcement. DS-014 (Freeze Guard) consults both. Two aggregates could mutate freeze state — risk of race conditions at count certification vs. location status changes. POL-034 and POL-056 block mutations but do not resolve ownership. |
| **Related Business Processes** | BP-12 (Full Physical Inventory Count), BP-02 (Location & Warehouse Setup), BP-07–BP-09 (Inbound), BP-18 (Pick, Pack & Ship), BP-25 (Transfer Execution) |
| **Questions Requiring Clarification** | 1. Does freeze apply to the entire location hierarchy or only the counted site? 2. Can emergency receipts or shipments override freeze with director authorization? 3. Who can release freeze early if count is aborted? 4. Are count-related adjustments the *only* mutations permitted during freeze? 5. What is the business consequence if freeze is violated — reject transaction or flag exception? |
| **Recommended Next Steps** | 1. Confirm pattern: Physical Count **initiates** freeze; Inventory Location **holds** authoritative frozen flag. 2. Document integration contract in bounded context map. 3. DS-014 reads Inventory Location state only. 4. Add **MR-09** formal rule: non-count adjustments blocked during freeze. 5. Workshop edge cases (emergency override, count abort). |

---

## HS-004 — Promotional Ring-Fence vs. General ATP

| Field | Detail |
|-------|--------|
| **Area of Uncertainty** | How promotional stock ring-fencing interacts with available-to-promise and who may consume ring-fenced quantity |
| **Why It Is Complex** | BR-029 requires ring-fencing during campaigns, but consumption rules for non-promotional orders are only partially stated (MR-10). Promotional Stock Allocation aggregate owns campaign intent; Stock Position owns ATP mechanics — dual context risks inconsistent state (P1-02). Event storming shows DE-020/DE-021 from Commercial aggregate and POL-026 affecting Stock Position, but invariant ownership is undocumented. Entity model still groups allocation under Inventory Balance domain. |
| **Related Business Processes** | BP-31 (Promotional & Launch Stock Readiness), BP-17 (Inventory Reservation), BP-16 (Order Availability Confirmation) |
| **Questions Requiring Clarification** | 1. Can non-promotional orders ever consume ring-fenced stock, and who approves override (commercial leadership)? 2. Is ring-fence at product-location or network level? 3. What happens to un consumed allocation at campaign end — auto-release or manual review? 4. How is promotional ATP presented in availability inquiry (RM-002)? 5. If campaign stock is insufficient (DE-072), may general ATP backfill the campaign commitment? 6. Priority between existing reservations and new promotional allocation on same SKU? |
| **Recommended Next Steps** | 1. Confirm: Commercial owns intent; Stock Position reacts to events only. 2. Formalize **MR-10** Promotional Consumption Approval. 3. Workshop Marketing, Sales, and Operations on override rules. 4. Update POL-026 with explicit ATP segregation mechanics. 5. Align SRS-DM-001 entity grouping with Commercial context. |

---

## HS-005 — Lot/Batch Quantity Model for Traceable Products

| Field | Detail |
|-------|--------|
| **Area of Uncertainty** | How traceable inventory quantities are scoped, reserved, picked, and counted when lot/batch identity is mandatory |
| **Why It Is Complex** | BR-017 requires lot/batch capture on receipt, transfer, and shipment. Stock Position identity is documented ambiguously as *product + location [+ lot]* vs. product-location with embedded Lot/Batch child entities (P1-05). This fork affects reservation (`ReserveStock`), cycle count variance scope, FEFO pick selection (DS-011), and transfer dispatch. Event storming commands do not specify lot-level vs. position-level reservation. |
| **Related Business Processes** | BP-07 (Goods Receipt), BP-09 (Put-Away), BP-11 (Cycle Counting), BP-18 (Pick, Pack & Ship), BP-25 (Transfer Execution), BP-28 (Return Disposition) |
| **Questions Requiring Clarification** | 1. One Stock Position per product-location with lot sub-quantities, or one position per lot? 2. Can ATP be promised without specifying lot, with lot assigned at pick? 3. How are partial lot quantities handled on count variance? 4. Mandatory FEFO — can picker override lot selection with manager approval? 5. Recall scenario: how is affected lot isolated across locations? 6. Mixed-lot storage position — allowed or prohibited? |
| **Recommended Next Steps** | 1. Business workshop with Quality and Warehouse on traceability operating model. 2. Adopt **single Stock Position per product-location** with Lot/Batch child entities (recommended in domain review). 3. Document invariant: lot quantities sum to on-hand; traceable products require lot on all movements. 4. Update reservation and pick commands with lot assignment rules. 5. Add recall workflow hotspot follow-up if in scope. |

---

## HS-006 — Consignment Ownership Transfer Trigger

| Field | Detail |
|-------|--------|
| **Area of Uncertainty** | When consignment stock becomes organization-owned for valuation, fulfillment, and payment purposes |
| **Why It Is Complex** | BR-031 states ownership transfers at *defined consumption or sale event per supplier agreement* — but the triggering events are not enumerated. DE-022 (`ConsignmentOwnershipTransferred`) is raised on `StockShipped` via POL-028, yet consignment agreements may trigger on issue, consumption, invoice, or other events. DEP-028 notes three-way match timing differs for consignment. VR/consignment ATP exclusion (CF-014) is unresolved — consignment may appear available for sale while not owned. Supplier aggregate has no lifecycle events to record agreement terms. |
| **Related Business Processes** | BP-07 (Goods Receipt), BP-18 (Pick, Pack & Ship), BP-30 (Valuation & Financial Reconciliation), BP-05 (Purchase Order Placement) |
| **Questions Requiring Clarification** | 1. What are the standard consumption triggers (shipment, internal issue, invoice, time-based)? 2. Is consignment stock included in ATP for customer commitment (BR-001 interaction)? 3. When does three-way match and payment occur for consignment — at ownership transfer? 4. How are consignment terms captured per supplier vs. per PO line? 5. Can consignment and owned stock coexist for same SKU at same location? 6. Financial valuation treatment before and after transfer? |
| **Recommended Next Steps** | 1. Catalog consignment agreement types with Finance and Procurement. 2. Formalize **MR-08** with explicit trigger event list per agreement type. 3. Add Supplier terms commands/events. 4. Clarify ATP formula for consignment in BR-001 context. 5. Map consignment path in three-way match (resolve DEP-028). |

---

## HS-007 — Order Reservation and Stock Position Coordination

| Field | Detail |
|-------|--------|
| **Area of Uncertainty** | How customer order commitment stays consistent with stock position quantity when operations span two aggregates without a single transaction |
| **Why It Is Complex** | Customer Order Fulfillment holds `InventoryReservation` entity; Stock Position holds `reserved` quantity — coordinated by DS-002 and POL-001/002. Partial failure scenario: order confirmed and reservation fails on Stock Position leaves inconsistent state. High-concurrency hot SKUs create contention. `CompletePartialFulfillment` decomposes lines across fulfilled and backordered — quantity reconciliation invariant must hold. Multi-location fulfillment (UC-048, DE-045) multiplies coordination points. Aggregate review flags Customer Order as split candidate post-MVP. |
| **Related Business Processes** | BP-16 (Order Availability Confirmation), BP-17 (Inventory Reservation), BP-18 (Pick, Pack & Ship), BP-19 (Partial Fulfillment & Backorder) |
| **Questions Requiring Clarification** | 1. What is the business response when order is confirmed but reservation fails (retry, cancel, partial)? 2. Is reservation synchronous with confirmation or eventual within SLA? 3. How long may reservation remain open before mandatory release (see HS-016)? 4. Who wins when two orders compete for last ATP unit? 5. Multi-location split — single customer communication or per-shipment? 6. Compensation policy if shipment deduct fails after pick verified? |
| **Recommended Next Steps** | 1. Define reservation SLA and failure compensation with Customer Service and Operations. 2. Document saga: ConfirmOrder → ReserveStock → on failure → CancelOrder or PartialConfirm. 3. Formalize order line invariant as published business rule. 4. Prototype contention scenario for Class A high-velocity SKUs. 5. Defer Shipment aggregate split decision until volume metrics available. |

---

## HS-008 — Return Write-Off Governance Path

| Field | Detail |
|-------|--------|
| **Area of Uncertainty** | Whether returned goods written off must follow the same adjustment governance workflow as operational write-offs |
| **Why It Is Complex** | BR-023 requires documented write-off authorization. Customer Return Case command `WriteOffReturnedGoods` currently triggers `ApplyApprovedWriteOff` on Stock Position directly (POL-047). Domain review REL-ISSUE-07 states return write-off should **create Adjustment Case** for governance. Two paths to write-off create SoD and audit inconsistency. Return inspection (BR-026) and write-off authorization (BR-023) may involve different approvers. |
| **Related Business Processes** | BP-27 (Customer Return Intake), BP-28 (Return-to-Stock or Disposal), BP-14 (Stock Adjustment & Write-Off), BP-15 (Shrinkage & Loss Management) |
| **Questions Requiring Clarification** | 1. Can warehouse manager authorize return write-off at inspection, or must Operations Director approve via Adjustment Case? 2. Is return write-off threshold governed by same approval limits as operational shrinkage? 3. Should return write-off reason codes differ from general adjustment codes? 4. Finance notification timing — at inspection or at governance approval? 5. Partial return line disposition — mixed restock and write-off on same RMA? |
| **Recommended Next Steps** | 1. Confirm with Finance and Operations: single governance path via Adjustment Case. 2. Update POL-047: `ReturnWrittenOff` → create Adjustment Case → `ApproveAdjustment` → `ApplyApprovedWriteOff`. 3. Define return-specific reason code subset. 4. Align event storming commands with BR-019/BR-021 SoD. |

---

## HS-009 — Bonded Inventory vs. General Quarantine

| Field | Detail |
|-------|--------|
| **Area of Uncertainty** | Whether customs-bonded inventory follows the same hold workflow as quality quarantine |
| **Why It Is Complex** | BR-030 requires bonded goods remain on hold until customs clearance — modeled today as `QuarantineHoldApplied` (POL-013). Business may require distinct **Customs Clearance Record** (ME-05) with different release authority (Regulatory Authority vs. Warehouse Manager). Bonded release triggers put-away activation; quality quarantine may route to write-off. External participant EXT-005 (Customs) triggers `ReleaseQuarantineHold` but clearance documentation differs from quality release. |
| **Related Business Processes** | BP-07 (Goods Receipt), BP-09 (Put-Away), BP-14 (Stock Adjustment & Write-Off) |
| **Questions Requiring Clarification** | 1. Is bonded hold a quarantine subtype or separate business concept? 2. Who records customs clearance — receiving clerk or finance/compliance role? 3. Can bonded goods move within bonded zone without clearance? 4. Partial clearance — some quantity cleared, remainder held? 5. Audit evidence required for clearance (document reference)? |
| **Recommended Next Steps** | 1. Clarify with Compliance whether bonded = quarantine subtype for MVP. 2. If distinct, add Customs Clearance Record and `CustomsClearanceGranted` event. 3. Update POL-013 and POL-012 bonded branch. 4. Defer to Phase 2 if bonded inventory not in MVP scope. |

---

## HS-010 — Transfer-Before-Buy vs. Purchase Decision

| Field | Detail |
|-------|--------|
| **Area of Uncertainty** | Who decides between network transfer and new procurement when local shortage is detected, and how mandatory the network check is |
| **Why It Is Complex** | BR-011 requires network availability evaluation before purchase. POL-029 may recommend `RequestStockTransfer` or `RejectPurchaseRequisition`, but replenishment recommendation (DE-071) is advisory — not a binding business decision. Regional manager, buyer, and operations director may disagree. Source location minimum (BR-012) may block transfer that purchasing prefers. No persistent **Replenishment Suggestion** entity for audit of overridden recommendations (ME-06). |
| **Related Business Processes** | BP-21 (Low-Stock Alert Review), BP-22 (Replenishment Planning), BP-24 (Transfer Request), BP-26 (Network Rebalancing) |
| **Questions Requiring Clarification** | 1. Is network check mandatory gate before PO approval, or advisory? 2. Who has final authority when transfer is recommended but buyer prefers purchase? 3. Must rejection of transfer recommendation be documented? 4. Cost comparison (transfer cost vs. purchase) — in scope for decision? 5. Auto-generated transfer request from rebalancing (UC-034) — approval required? |
| **Recommended Next Steps** | 1. Define decision authority matrix: Purchasing vs. Operations vs. Regional Manager. 2. Clarify BR-011 enforcement level (hard block vs. warning). 3. Add acknowledgment workflow when recommendation overridden. 4. Workshop BP-21/BP-22/BP-24 integrated replenishment policy. |

---

## HS-011 — Backorder Priority and Auto-Fulfillment

| Field | Detail |
|-------|--------|
| **Area of Uncertainty** | How backordered customer commitments are prioritized and fulfilled when stock becomes available |
| **Why It Is Complex** | BR-028 requires customer acknowledgment for backorders. POL-008 triggers `FulfillBackorder` on `StockReceived`, but priority rules are undefined — FIFO by acknowledgment date, order value, customer tier, or product class? MR-06 states backorder must convert to reservation before fulfillment — sequence not fully modeled. Competition between backorder fulfillment and new order reservation on inbound stock. `BackorderFulfilled` (DE-043) chain spans multiple commands without documented priority policy. |
| **Related Business Processes** | BP-19 (Partial Fulfillment & Backorder), BP-17 (Inventory Reservation), BP-09 (Put-Away), BP-22 (Replenishment Planning) |
| **Questions Requiring Clarification** | 1. Backorder fulfillment priority rule when multiple backorders and new orders await same SKU? 2. Auto-fulfill on stock arrival or manual customer service trigger? 3. Customer notification required before backorder shipment? 4. Partial backorder fulfillment over multiple receipts — allowed? 5. Backorder expiry or cancellation policy? |
| **Recommended Next Steps** | 1. Define backorder priority policy with Customer Service. 2. Formalize MR-05 and MR-06 as business rules. 3. Update POL-008 with explicit priority algorithm. 4. Document in RM-014 (Backorder Pipeline) sort order. |

---

## HS-012 — Safety Stock Override Authorization

| Field | Detail |
|-------|--------|
| **Area of Uncertainty** | When and how safety stock buffer may be consumed below policy minimum for reservations, transfers, or fulfillment |
| **Why It Is Complex** | BR-010 prohibits bypassing safety stock without documented approval and replenishment plan — but override authority, documentation, and enforcement point are unclear. DS-002 checks safety stock on reservation; DS-006 on transfer — inconsistent override path. Emergency fulfillment during stockout may pressure safety stock consumption. MR-04 proposed but not formalized. Exception scenario EX-ad-hoc policy override exists generically. |
| **Related Business Processes** | BP-17 (Inventory Reservation), BP-24 (Transfer Request), BP-21 (Low-Stock Alert Review), BP-20 (Outbound Exception Handling) |
| **Questions Requiring Clarification** | 1. Who may authorize safety stock override (Warehouse Manager, Operations Director)? 2. Is override per transaction or blanket for period? 3. Must replenishment plan be created before or after override? 4. Does override apply to source location on transfer (BR-012 interaction)? 5. Audit evidence and expiry of override authorization? |
| **Recommended Next Steps** | 1. Formalize MR-04 as BR-033+ with approver and evidence requirements. 2. Add `SafetyStockOverrideAuthorized` event or governance consultation pattern. 3. Align DS-002 and DS-006 override handling. 4. Include in governance policy parameters. |

---

## HS-013 — Supplier Master Data Ownership and Lifecycle

| Field | Detail |
|-------|--------|
| **Area of Uncertainty** | Organizational ownership of supplier master data and how supplier lifecycle is managed in the domain model |
| **Why It Is Complex** | Supplier aggregate exists but event storming reveals **no commands or events** — gap HS from aggregate review. Bounded context placement differs: Catalog & Network (SRS-DM-003) vs. Procurement & Supplier (SRS-DM-007). Consignment terms (BR-031) live on Supplier but affect Stock Position and Finance. Supplier performance scorecard (RM-010) consumes events Supplier never produces. |
| **Related Business Processes** | BP-05 (Purchase Order Placement), BP-07 (Goods Receipt), BP-30 (Valuation & Financial Reconciliation) |
| **Questions Requiring Clarification** | 1. Who owns supplier master data — Procurement or Finance? 2. Supplier onboarding and deactivation workflow? 3. How are consignment agreement terms versioned and effective-dated? 4. Can inactive supplier appear on in-flight PO? 5. Supplier performance feedback — formal review cycle or event-driven only? |
| **Recommended Next Steps** | 1. Align bounded context to Procurement & Supplier. 2. Add supplier lifecycle commands and events. 3. Link consignment terms to BR-031 trigger catalog (HS-006). 4. Assign product owner for supplier master data. |

---

## HS-014 — Finance System Boundary (Invoice and Valuation)

| Field | Detail |
|-------|--------|
| **Area of Uncertainty** | Whether IMS owns supplier invoicing and valuation reconciliation or synchronizes with external Finance ERP |
| **Why It Is Complex** | Supplier Invoice aggregate performs three-way match (BR-008) — typically ERP-owned in mature organizations. `InventoryValuationSnapshotPrepared` (DE-076) must align with general ledger — EXT-004. Architecture review AG-03 flags finance coupling as Phase 3 evaluation. Event storming models full match workflow; business may intend IMS as operational record with ERP as financial system of record. Valuation variance (DE-077) investigation spans both systems. |
| **Related Business Processes** | BP-30 (Inventory Valuation & Financial Reconciliation), BP-05 (Purchase Order), BP-07 (Goods Receipt) |
| **Questions Requiring Clarification** | 1. Does IMS record invoices or receive match status from ERP? 2. Which system authorizes payment? 3. Valuation method (FIFO, weighted average) — owned by Finance or IMS? 4. Month-end close — IMS pushes snapshot or ERP pulls? 5. Consignment and write-off impact — which system is authoritative? |
| **Recommended Next Steps** | 1. Integration workshop with CFO and Finance systems team. 2. Define anti-corruption layer for ERP boundary. 3. MVP decision: IMS owns match for accountability chain vs. ERP read-only. 4. Document in bounded context map as explicit ACL. 5. Defer if finance integration is Phase 2. |

---

## HS-015 — Product Supersession and SKU Runout

| Field | Detail |
|-------|--------|
| **Area of Uncertainty** | How product supersession affects procurement, fulfillment, and inventory runout of replaced SKUs |
| **Why It Is Complex** | BR-027 blocks discontinued product reorder; BRD references supersession (FR-019→FR-065) but no **Product Supersession Link** entity (ME-03). Discontinuing SKU while stock remains creates fulfillment and transfer policy questions. Event storming POL-010 blocks new reservations on discontinued status but not migration to successor SKU. |
| **Related Business Processes** | BP-01 (Product Master Data), BP-04 (ABC Classification), BP-15 (Shrinkage & Obsolete Stock) |
| **Questions Requiring Clarification** | 1. Is supersession a product catalog relationship (old SKU → new SKU)? 2. May discontinued SKU still fulfill existing backorders and reservations? 3. Auto-suggest successor on availability inquiry? 4. Runout policy — markdown, transfer, or write-off remaining stock? 5. Timeline between supersession announcement and discontinue status? |
| **Recommended Next Steps** | 1. Confirm supersession in MVP scope (Phase 2 per UC-004 context). 2. If in scope, add supersession link to Product Catalog. 3. Define POL for discontinued + superseded SKU handling. 4. Link to shrinkage analysis (RM-025). |

---

## HS-016 — Reservation Expiry and Stale Commitments

| Field | Detail |
|-------|--------|
| **Area of Uncertainty** | Whether inventory reservations expire and how stale commitments are released |
| **Why It Is Complex** | Reservations reduce ATP indefinitely until fulfillment or cancellation (BR-002). MR-05 proposes expiry/escalation policy — not formalized. Long-lived reservations on slow-moving orders block ATP for other customers. No command `ExpireReservation` or policy for auto-release. Customer Service may not cancel abandoned orders promptly. |
| **Related Business Processes** | BP-17 (Inventory Reservation), BP-16 (Order Availability Confirmation), BP-10 (Inventory Status Monitoring) |
| **Questions Requiring Clarification** | 1. Reservation time limit — days, weeks, configurable by product class? 2. Auto-release vs. escalation notification before release? 3. Customer notification before reservation release? 4. Does expiry apply to backorders differently than confirmed reservations? 5. Re-reservation priority if customer reorders after expiry? |
| **Recommended Next Steps** | 1. Define reservation TTL policy with Customer Service and Sales. 2. Formalize MR-05 as business rule if approved. 3. Add `ReservationExpired` event and POL if auto-release adopted. 4. MVP: manual release only with dashboard alert for aged reservations. |

---

## Hotspot Dependency Map

```
HS-001 Ad-Hoc Receipt ──────────────► HS-014 Finance Boundary
         │
HS-002 Opening Balance ─────────────► HS-003 Location Freeze (if count-based go-live)
         │
HS-005 Lot/Batch Model ─────────────► HS-007 Reservation Coordination
         │                                    │
HS-006 Consignment Trigger ──────────► HS-014 Finance Boundary
         │
HS-004 Promotional Ring-Fence ─────► HS-007 Reservation Coordination
         │
HS-008 Return Write-Off ────────────► HS-012 Safety Stock (if shared approvers)
         │
HS-010 Transfer vs. Buy ────────────► HS-012 Safety Stock (source minimum)
         │
HS-011 Backorder Priority ──────────► HS-007 Reservation Coordination
```

---

## Workshop Prioritization

### Session 1 — Critical Path (MVP Blockers)

| Hotspot | Participants |
|---------|--------------|
| HS-001 Ad-Hoc Receipt | Purchasing, Receiving, Finance |
| HS-002 Opening Balance | Inventory Controller, Operations, Finance |
| HS-003 Location Freeze | Inventory Controller, Warehouse Manager |
| HS-005 Lot/Batch Model | Warehouse, Quality, Inventory Controller |

### Session 2 — Core Operations

| Hotspot | Participants |
|---------|--------------|
| HS-004 Promotional Ring-Fence | Marketing, Sales, Operations |
| HS-007 Reservation Coordination | Customer Service, Warehouse, Operations |
| HS-008 Return Write-Off | Customer Service, Finance, Warehouse |
| HS-010 Transfer vs. Buy | Purchasing, Operations, Regional Managers |

### Session 3 — Financial & Advanced

| Hotspot | Participants |
|---------|--------------|
| HS-006 Consignment | Procurement, Finance |
| HS-014 Finance ERP Boundary | CFO, Finance systems, IMS product owner |
| HS-009 Bonded Inventory | Compliance, Receiving |
| HS-011–HS-016 | As needed per phase plan |

---

## Resolution Tracking

| Hotspot | Target Resolution | Owner | Resolution Document |
|---------|-------------------|-------|---------------------|
| HS-001 | Before architecture | Senior BA | BR-033, Ad-Hoc Receipt Authorization |
| HS-002 | Before architecture | Inventory Controller | Opening Balance workflow |
| HS-003 | Before architecture | DDD Architect | Context integration contract |
| HS-004 | Before MVP cut | Marketing / Operations | MR-10, POL-026 update |
| HS-005 | Before architecture | Solution Architect | Stock Position identity spec |
| HS-006 | Phase 2 or MVP if consignment in scope | Finance | MR-08, Supplier terms |
| HS-007 | Before MVP test | Operations Director | Saga compensation spec |
| HS-008 | Before MVP | Finance / Operations | POL-047 realignment |
| HS-009 | Phase 2 unless bonded in MVP | Compliance | ME-05 decision |
| HS-010 | MVP policy document | Purchasing Manager | BR-011 enforcement level |
| HS-011 | MVP or Phase 2 | Customer Service | Backorder priority policy |
| HS-012 | MVP governance update | Operations Director | MR-04 formalization |
| HS-013 | Before architecture | Procurement | Supplier lifecycle events |
| HS-014 | Architecture phase | CFO / IT | ERP integration decision |
| HS-015 | Phase 2 | Product / Inventory | Supersession entity |
| HS-016 | Phase 2 | Customer Service | MR-05 decision |

---

## Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Domain Expert | | | |
| DDD Architect | | | |
| Product Owner | | | |
| Operations Director | | | |

---

*End of Event Storming Hotspots*

*Document ID: SRS-ES-007 | Version 1.0 | July 6, 2026*
