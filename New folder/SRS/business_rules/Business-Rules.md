# Business Rules Specification
## Inventory Management System

---

## Document Information

| Attribute | Detail |
|-----------|--------|
| **Document ID** | SRS-BR-001 |
| **Document Title** | Business Rules — Inventory Management System |
| **Version** | 1.0 |
| **Status** | Draft |
| **Document Owner** | Senior Business Analyst |
| **Source Document** | BRD-IMS-001 (Business Requirements Document, Version 1.0) |
| **Date** | July 5, 2026 |
| **Scope** | Business policies only — no technical validation logic, system constraints, or implementation detail |

### Purpose

This document extracts and elaborates all **32 industry business rules** defined in the approved BRD (Section 13). Each rule is expressed as an enforceable business policy governing how the organization manages inventory, independent of how any system implements it.

### Rule Category Legend

| Category | Description |
|----------|-------------|
| **Inventory** | Stock availability, commitment, replenishment, and network balance |
| **Purchasing** | Procurement, inbound supply, and supplier accountability |
| **Warehousing** | Receiving, storage, movement, and fulfillment execution |
| **Products** | Product master data, lifecycle, classification, and commercial positioning |
| **Users** | Governance, accountability, segregation of duties, and authorization |
| **Reporting** | Performance measurement, audit, and management oversight |

---

## Business Rules Catalog

### Availability and Customer Commitment

---

#### BR-001 — ATP-Only Customer Commitment

| Attribute | Detail |
|-----------|--------|
| **Rule Name** | ATP-Only Customer Commitment |
| **Business Rule Statement** | The organization must sell and promise stock only against available-to-promise (ATP) quantity. On-hand quantity that is reserved, committed, quarantined, or otherwise unavailable must not be quoted or committed to customers. |
| **Business Reason** | On-hand quantity includes stock already reserved or committed to other orders. Quoting or selling against total on-hand causes overselling — confirming orders the business cannot fulfill. ATP is the only honest measure of what can still be promised to new customers. |
| **Related Business Process** | BP-10 (Inventory Status Monitoring), BP-16 (Order Availability Confirmation) |
| **Related Functional Requirements** | FR-024 (Display ATP quantity), FR-041 (Confirm order availability before commitment), FR-025 (Display reserved and committed stock) |
| **Rule Category** | Inventory |

---

#### BR-002 — Reservation at Order Confirmation

| Attribute | Detail |
|-----------|--------|
| **Rule Name** | Reservation at Order Confirmation |
| **Business Rule Statement** | Stock must be reserved at the point of order confirmation. Once a customer order is confirmed for fulfillment, the required quantity must be committed against on-hand stock and removed from ATP until fulfilled or released. |
| **Business Reason** | The gap between order confirmation and physical picking creates a window where the same stock can be sold to multiple customers. Reservation converts a commercial commitment into an operational hold, preventing double-allocation. |
| **Related Business Process** | BP-17 (Inventory Reservation) |
| **Related Functional Requirements** | FR-042 (Reserve inventory for confirmed orders), FR-025 (Display reserved and committed stock), FR-043 (Release inventory reservations) |
| **Rule Category** | Inventory |

---

#### BR-003 — Verified Pick Before Shipment

| Attribute | Detail |
|-----------|--------|
| **Rule Name** | Verified Pick Before Shipment |
| **Business Rule Statement** | The organization must not ship or deduct inventory until pick verification is complete. Orders may only be marked shipped after the correct items are physically retrieved, verified against the order, packed, and handed to the carrier. |
| **Business Reason** | Inventory should not be deducted and orders should not be marked shipped until the correct items are physically retrieved, verified, packed, and handed to the carrier. Premature shipment recording creates inaccurate stock and false delivery expectations. |
| **Related Business Process** | BP-18 (Pick, Pack & Ship) |
| **Related Functional Requirements** | FR-044 (Support pick, pack, and ship workflow), FR-029 (Record all inventory movements with full history) |
| **Rule Category** | Warehousing |

---

#### BR-028 — Backorder Customer Acknowledgment

| Attribute | Detail |
|-----------|--------|
| **Rule Name** | Backorder Customer Acknowledgment |
| **Business Rule Statement** | A backorder requires explicit customer acknowledgment before it is recorded. Customers must be informed of the delay, expected fulfillment timing, and their option to cancel or accept partial delivery. |
| **Business Reason** | A backorder is a mutual agreement to wait — not an internal note that an order cannot ship. Customers must be informed of the delay, the expected fulfillment date, and their right to cancel. Silent backorders destroy trust. |
| **Related Business Process** | BP-19 (Partial Fulfillment & Backorder Management) |
| **Related Functional Requirements** | FR-045 (Handle partial fulfillment), FR-046 (Manage backorders and replenishment priority) |
| **Rule Category** | Inventory |

---

### Inbound and Procurement

---

#### BR-004 — Verify Before Inventory Acceptance

| Attribute | Detail |
|-----------|--------|
| **Rule Name** | Verify Before Inventory Acceptance |
| **Business Rule Statement** | Inbound goods must be verified before acceptance into inventory. Quantity, product identity, and condition must be confirmed against the purchase order or authorized receipt documentation before stock is recorded as on-hand. |
| **Business Reason** | Arrival at the dock is not receipt. Until quantity, product identity, and condition are verified against the purchase order, the business does not know what it actually received. Recording unverified quantities corrupts inventory from the point of entry. |
| **Related Business Process** | BP-07 (Goods Receipt & Verification) |
| **Related Functional Requirements** | FR-015 (Receive and verify inbound goods), FR-003 (Support product identifier lookup) |
| **Rule Category** | Warehousing |

---

#### BR-005 — Put-Away Before Availability

| Attribute | Detail |
|-----------|--------|
| **Rule Name** | Put-Away Before Availability |
| **Business Rule Statement** | Received stock is not available for sale or fulfillment until put-away is complete. Stock verified at the receiving dock does not increase ATP until it is placed in its designated storage location and put-away is confirmed. |
| **Business Reason** | Stock sitting in the receiving area is physically in the building but not operationally available. Pickers cannot find it efficiently, it may be damaged in transit areas, and it is not in its designated storage location. Availability begins when put-away is confirmed. |
| **Related Business Process** | BP-09 (Stock Put-Away & Storage) |
| **Related Functional Requirements** | FR-018 (Manage put-away and stock availability timing), FR-024 (Display ATP quantity) |
| **Rule Category** | Warehousing |

---

#### BR-006 — Document Receipt Discrepancies

| Attribute | Detail |
|-----------|--------|
| **Rule Name** | Document Receipt Discrepancies |
| **Business Rule Statement** | Receipt discrepancies must be documented before acceptance. Short shipments, over-shipments, wrong items, and damage must be recorded at the point of receipt with supporting evidence before quantities are accepted into inventory. |
| **Business Reason** | Short shipments, over-shipments, wrong items, and damage must be recorded at the point of receipt — when evidence exists and the carrier or supplier is present. Undocumented acceptance waives the business's right to claim and hides supplier performance problems. |
| **Related Business Process** | BP-08 (Receipt Discrepancy Resolution) |
| **Related Functional Requirements** | FR-016 (Document and resolve receipt discrepancies), FR-011 (Maintain standard reason codes) |
| **Rule Category** | Purchasing |

---

#### BR-007 — Purchase Order Required for Supplier Receipt

| Attribute | Detail |
|-----------|--------|
| **Rule Name** | Purchase Order Required for Supplier Receipt |
| **Business Rule Statement** | A valid purchase order is required before receiving supplier goods. Supplier shipments must be matched to an authorized purchase order before acceptance, except where an explicitly approved ad-hoc receipt exception applies. |
| **Business Reason** | A purchase order is the authorized commercial commitment that defines what was ordered, at what price, and from whom. Receiving without a PO breaks financial controls, enables unauthorized purchases, and prevents three-way matching. |
| **Related Business Process** | BP-05 (Purchase Order Placement), BP-07 (Goods Receipt & Verification) |
| **Related Functional Requirements** | FR-017 (Enforce PO reference for supplier receipts), FR-013 (Record purchase order commitments) |
| **Rule Category** | Purchasing |

---

#### BR-008 — Three-Way Match Before Payment

| Attribute | Detail |
|-----------|--------|
| **Rule Name** | Three-Way Match Before Payment |
| **Business Rule Statement** | Supplier payment must not be authorized until a three-way match is confirmed among the purchase order, goods receipt, and supplier invoice within defined tolerance. Payment for unordered, unreceived, or mispriced goods is prohibited. |
| **Business Reason** | Payment must be authorized only when the purchase order (what was ordered), goods receipt (what was received), and supplier invoice (what is billed) agree within defined tolerance. This prevents paying for unordered, unreceived, or mispriced goods. |
| **Related Business Process** | BP-05 (Purchase Order Placement), BP-08 (Receipt Discrepancy Resolution), BP-30 (Inventory Valuation & Financial Reconciliation) |
| **Related Functional Requirements** | FR-013 (Record purchase order commitments), FR-015 (Receive and verify inbound goods), FR-016 (Document and resolve receipt discrepancies), FR-089 (Support financial inventory reconciliation) |
| **Rule Category** | Purchasing |

---

### Replenishment and Stock Policy

---

#### BR-009 — Reorder at Reorder Level

| Attribute | Detail |
|-----------|--------|
| **Rule Name** | Reorder at Reorder Level |
| **Business Rule Statement** | Replenishment action must be triggered at or before the defined reorder level. When available stock reaches the reorder threshold, a replenishment review or purchase action must be initiated the same business day. |
| **Business Reason** | The reorder level is calculated to allow enough time for replenishment to arrive before stock reaches zero, accounting for lead time and demand during that period. Delaying action past the reorder level guarantees a stockout during lead time. |
| **Related Business Process** | BP-03 (Stock Policy & Threshold Definition), BP-21 (Low-Stock Alert Review), BP-22 (Replenishment Planning & Requisition) |
| **Related Functional Requirements** | FR-008 (Define stock policy and replenishment thresholds), FR-051 (Generate low-stock and out-of-stock alerts), FR-052 (Review and acknowledge stock alerts) |
| **Rule Category** | Inventory |

---

#### BR-010 — Safety Stock Protection

| Attribute | Detail |
|-----------|--------|
| **Rule Name** | Safety Stock Protection |
| **Business Rule Statement** | Safety stock must not be bypassed without an authorized exception. Safety stock buffers may not be consumed for routine fulfillment or reallocated without documented approval and a replenishment plan. |
| **Business Reason** | Safety stock is a deliberate buffer protecting against demand and supply uncertainty. Consuming safety stock to fulfill routine orders or reallocating it without replenishment plan removes the organization's protection against the next disruption. |
| **Related Business Process** | BP-03 (Stock Policy & Threshold Definition), BP-17 (Inventory Reservation), BP-24 (Inter-Location Transfer Request) |
| **Related Functional Requirements** | FR-056 (Enforce safety stock protection rules), FR-008 (Define stock policy and replenishment thresholds) |
| **Rule Category** | Inventory |

---

### Network Balance

---

#### BR-011 — Network Check Before Purchase

| Attribute | Detail |
|-----------|--------|
| **Rule Name** | Network Check Before Purchase |
| **Business Rule Statement** | Network availability must be checked before placing a new purchase order. When a location experiences shortage, excess stock at other locations must be evaluated for transfer before initiating new procurement. |
| **Business Reason** | A local stockout may be solvable with a transfer from another location that holds excess. Purchasing new stock when the network already owns sufficient quantity wastes capital, increases carrying cost, and worsens network imbalance. |
| **Related Business Process** | BP-21 (Low-Stock Alert Review), BP-24 (Inter-Location Transfer Request), BP-26 (Network Stock Rebalancing) |
| **Related Functional Requirements** | FR-028 (Display expected inbound and network-wide availability), FR-053 (Generate replenishment suggestions), FR-058 (Request inter-location stock transfers) |
| **Rule Category** | Inventory |

---

#### BR-012 — Protect Source Location Minimum

| Attribute | Detail |
|-----------|--------|
| **Rule Name** | Protect Source Location Minimum |
| **Business Rule Statement** | An inter-location transfer must not deplete the source location below its minimum threshold. Transfer quantity must be limited to stock the source can spare while maintaining its own service level. |
| **Business Reason** | Sending stock to fix one location's shortage must not create a shortage at the source. Transfers require verification that the sending location can spare the quantity while maintaining its own service level. |
| **Related Business Process** | BP-24 (Inter-Location Transfer Request), BP-25 (Inter-Location Transfer Execution) |
| **Related Functional Requirements** | FR-063 (Enforce source location minimum on transfers), FR-058 (Request inter-location stock transfers), FR-060 (Execute and record inter-location transfers) |
| **Rule Category** | Warehousing |

---

### Quality and Rotation

---

#### BR-013 — Quarantine Exclusion from Sellable Stock

| Attribute | Detail |
|-----------|--------|
| **Rule Name** | Quarantine Exclusion from Sellable Stock |
| **Business Rule Statement** | Quarantined stock must be excluded from sellable availability. Inventory under quality hold, investigation, or recall must not be included in ATP or committed to customer orders. |
| **Business Reason** | Quarantined inventory is held pending quality investigation, regulatory clearance, or recall response. Including quarantined stock in sellable availability risks shipping defective, contaminated, or non-compliant products to customers. |
| **Related Business Process** | BP-14 (Stock Adjustment & Write-Off), BP-20 (Outbound Exception Handling) |
| **Related Functional Requirements** | FR-038 (Manage quarantine and hold stock status), FR-024 (Display ATP quantity) |
| **Rule Category** | Inventory |

---

#### BR-014 — FEFO Rotation for Shelf-Life Products

| Attribute | Detail |
|-----------|--------|
| **Rule Name** | FEFO Rotation for Shelf-Life Products |
| **Business Rule Statement** | First-expired, first-out (FEFO) rotation is required for products with defined shelf life. Fulfillment must prioritize stock with the earliest expiration date. |
| **Business Reason** | Products with expiration dates must ship in order of earliest expiry first. Shipping newer stock while older stock expires in the warehouse causes write-offs, customer safety issues, and regulatory violations. |
| **Related Business Process** | BP-09 (Stock Put-Away & Storage), BP-18 (Pick, Pack & Ship) |
| **Related Functional Requirements** | FR-044 (Support pick, pack, and ship workflow), FR-029 (Record all inventory movements with full history) |
| **Rule Category** | Products |

---

#### BR-015 — FIFO Rotation for Standard Goods

| Attribute | Detail |
|-----------|--------|
| **Rule Name** | FIFO Rotation for Standard Goods |
| **Business Rule Statement** | First-in, first-out (FIFO) rotation is required for non-perishable standard goods. Oldest received stock must be picked and shipped before newer stock for the same SKU. |
| **Business Reason** | Oldest stock should move first to minimize obsolescence, packaging degradation, and model-year expiration. Consistent FIFO prevents aged inventory from sitting indefinitely while new stock cycles normally. |
| **Related Business Process** | BP-09 (Stock Put-Away & Storage), BP-18 (Pick, Pack & Ship) |
| **Related Functional Requirements** | FR-044 (Support pick, pack, and ship workflow), FR-029 (Record all inventory movements with full history) |
| **Rule Category** | Products |

---

#### BR-016 — Minimum Remaining Shelf Life at Receipt

| Attribute | Detail |
|-----------|--------|
| **Rule Name** | Minimum Remaining Shelf Life at Receipt |
| **Business Rule Statement** | Products with shelf-life requirements must meet minimum remaining shelf life (MRSL) at receipt. Inbound deliveries that do not meet MRSL policy must be rejected or dispositioned before acceptance into sellable inventory. |
| **Business Reason** | Receiving product too close to expiration guarantees write-off before sale. Minimum remaining shelf life requirements protect the business from accepting stock with insufficient selling window. |
| **Related Business Process** | BP-07 (Goods Receipt & Verification), BP-08 (Receipt Discrepancy Resolution) |
| **Related Functional Requirements** | FR-015 (Receive and verify inbound goods), FR-016 (Document and resolve receipt discrepancies) |
| **Rule Category** | Products |

---

#### BR-017 — Lot or Batch Capture for Traceable Products

| Attribute | Detail |
|-----------|--------|
| **Rule Name** | Lot or Batch Capture for Traceable Products |
| **Business Rule Statement** | Lot or batch identity must be captured for traceable products at receipt and through all subsequent inventory movements. Traceable products must not be received, transferred, or shipped without lot or batch attribution. |
| **Business Reason** | Lot capture at every transaction point enables targeted recall, quality investigation, and regulatory compliance. Without lot data, the only option in a defect scenario is a full product-line recall. |
| **Related Business Process** | BP-07 (Goods Receipt & Verification), BP-18 (Pick, Pack & Ship), BP-25 (Inter-Location Transfer Execution) |
| **Related Functional Requirements** | FR-029 (Record all inventory movements with full history), FR-015 (Receive and verify inbound goods) |
| **Rule Category** | Products |

---

### Inventory Control and Governance

---

#### BR-018 — Blind Cycle Counting

| Attribute | Detail |
|-----------|--------|
| **Rule Name** | Blind Cycle Counting |
| **Business Rule Statement** | Cycle counts must be performed blind. Counters must not be shown the system's expected quantity before recording the physical count result. |
| **Business Reason** | Counters who see the system's expected quantity before counting may consciously or unconsciously match it, defeating the purpose of verification. Blind counting produces unbiased accuracy measurement. |
| **Related Business Process** | BP-11 (Cycle Counting) |
| **Related Functional Requirements** | FR-031 (Perform blind cycle counts), FR-030 (Schedule and assign cycle counts) |
| **Rule Category** | Inventory |

---

#### BR-019 — Independent Count Approval

| Attribute | Detail |
|-----------|--------|
| **Rule Name** | Independent Count Approval |
| **Business Rule Statement** | The person who performed a count must not approve adjustments arising from their own count. Count variances require review and approval by an independent authorized person. |
| **Business Reason** | Segregation of duties prevents fraud and undetected error. When the same person counts, investigates, and approves, there is no independent verification of the variance or its cause. |
| **Related Business Process** | BP-13 (Count Variance Investigation & Approval) |
| **Related Functional Requirements** | FR-034 (Investigate and approve count adjustments), FR-084 (Enforce segregation of duties) |
| **Rule Category** | Users |

---

#### BR-020 — Mandatory Adjustment Reason Codes

| Attribute | Detail |
|-----------|--------|
| **Rule Name** | Mandatory Adjustment Reason Codes |
| **Business Rule Statement** | Every inventory adjustment requires a reason code. No stock correction, increase, or decrease may be applied without a categorized business reason. |
| **Business Reason** | Adjustments without categorized reasons are analytically useless. The business knows quantity changed but not why — preventing shrinkage analysis, trend identification, and targeted corrective action. |
| **Related Business Process** | BP-14 (Stock Adjustment & Write-Off), BP-15 (Shrinkage & Loss Management) |
| **Related Functional Requirements** | FR-035 (Process stock adjustments with mandatory reason codes), FR-011 (Maintain standard reason codes) |
| **Rule Category** | Inventory |

---

#### BR-021 — Independent Approval for Material Adjustments

| Attribute | Detail |
|-----------|--------|
| **Rule Name** | Independent Approval for Material Adjustments |
| **Business Rule Statement** | Adjustments above the defined financial or quantity threshold require independent approval by an authorized person who did not initiate the underlying transaction. |
| **Business Reason** | High-value or high-quantity adjustments carry greater financial and fraud risk. Independent approval by an authorized person who did not perform the underlying transaction provides oversight proportional to the impact. |
| **Related Business Process** | BP-14 (Stock Adjustment & Write-Off), BP-13 (Count Variance Investigation & Approval) |
| **Related Functional Requirements** | FR-037 (Enforce adjustment approval thresholds), FR-084 (Enforce segregation of duties) |
| **Rule Category** | Users |

---

#### BR-022 — Investigate Before Adjusting

| Attribute | Detail |
|-----------|--------|
| **Rule Name** | Investigate Before Adjusting |
| **Business Rule Statement** | Count and inventory variances must be investigated before an adjustment is applied. Adjustments may only be approved after root cause analysis or documented investigation effort. |
| **Business Reason** | Adjustments fix the record; investigation fixes the process. Applying adjustments without understanding why the variance occurred guarantees the same discrepancy will reappear on the next count. |
| **Related Business Process** | BP-13 (Count Variance Investigation & Approval) |
| **Related Functional Requirements** | FR-033 (Identify and report count variances), FR-034 (Investigate and approve count adjustments) |
| **Rule Category** | Inventory |

---

#### BR-023 — Documented Write-Off Authorization

| Attribute | Detail |
|-----------|--------|
| **Rule Name** | Documented Write-Off Authorization |
| **Business Rule Statement** | Inventory write-off requires documented evidence and authorization. Write-offs must include supporting documentation and approval by an authorized person before inventory value is removed. |
| **Business Reason** | Write-offs permanently remove inventory value from the business. Unauthorized or undocumented write-offs enable fraud, inflate remaining inventory inaccurately, and create audit exposure. |
| **Related Business Process** | BP-14 (Stock Adjustment & Write-Off), BP-15 (Shrinkage & Loss Management) |
| **Related Functional Requirements** | FR-036 (Process inventory write-offs with authorization), FR-011 (Maintain standard reason codes) |
| **Rule Category** | Users |

---

#### BR-024 — Physical Inventory Freeze

| Attribute | Detail |
|-----------|--------|
| **Rule Name** | Physical Inventory Freeze |
| **Business Rule Statement** | A physical inventory freeze applies during a full wall-to-wall count. Receiving, shipping, transfers, and adjustments must be suspended for the counted location until the count is completed and verified. |
| **Business Reason** | Movements during a full count change the quantity being counted, making the snapshot unreliable. A freeze ensures the counted quantity is stable and auditable. |
| **Related Business Process** | BP-12 (Full Physical Inventory Count) |
| **Related Functional Requirements** | FR-032 (Conduct full physical inventory count), FR-033 (Identify and report count variances) |
| **Rule Category** | Warehousing |

---

#### BR-032 — Class A Priority Monitoring

| Attribute | Detail |
|-----------|--------|
| **Rule Name** | Class A Priority Monitoring |
| **Business Rule Statement** | Class A products require the highest count frequency and monitoring intensity. Priority SKUs must receive more frequent cycle counts, availability monitoring, and replenishment attention than lower-classification products. |
| **Business Reason** | Not all products warrant equal operational effort. Class A items drive the majority of revenue and customer impact. Higher count frequency and monitoring intensity on A items prevents stockouts and accuracy failures where they matter most. |
| **Related Business Process** | BP-04 (ABC Product Classification), BP-11 (Cycle Counting), BP-21 (Low-Stock Alert Review) |
| **Related Functional Requirements** | FR-009 (Classify products by ABC priority), FR-030 (Schedule and assign cycle counts), FR-051 (Generate low-stock and out-of-stock alerts) |
| **Rule Category** | Products |

---

### Returns and Commercial

---

#### BR-025 — Return Authorization Required

| Attribute | Detail |
|-----------|--------|
| **Rule Name** | Return Authorization Required |
| **Business Rule Statement** | Customer returns require authorization before acceptance. Returned goods must not be received at the warehouse without a valid return authorization linked to the original order and return policy. |
| **Business Reason** | Unauthorized returns cannot be linked to original orders, may violate return policy, and give the warehouse no advance notice. Authorization connects the physical return to the commercial transaction and expected resolution. |
| **Related Business Process** | BP-27 (Customer Return Intake) |
| **Related Functional Requirements** | FR-064 (Authorize and record customer returns), FR-067 (Track return processing status) |
| **Rule Category** | Inventory |

---

#### BR-026 — Inspect Returns Before Restocking

| Attribute | Detail |
|-----------|--------|
| **Rule Name** | Inspect Returns Before Restocking |
| **Business Rule Statement** | Returned goods must be inspected before restocking. Products may only be returned to sellable inventory after condition assessment confirms they meet resale quality standards. |
| **Business Reason** | Not all returns are resalable. Used, damaged, or defective products placed back in sellable inventory will be shipped to the next customer as new — generating repeat returns, complaints, and brand damage. |
| **Related Business Process** | BP-28 (Return-to-Stock or Disposal Decision) |
| **Related Functional Requirements** | FR-065 (Receive and inspect returned goods), FR-066 (Restock or write off returned inventory) |
| **Rule Category** | Warehousing |

---

#### BR-027 — No Reorder of Discontinued Products

| Attribute | Detail |
|-----------|--------|
| **Rule Name** | No Reorder of Discontinued Products |
| **Business Rule Statement** | Discontinued products must not be reordered. Once a product is marked discontinued, new purchase orders and replenishment requisitions for that SKU are prohibited. |
| **Business Reason** | Discontinued status means the business has decided to exit the product. Reordering discontinued SKUs creates obsolete inventory that must eventually be written off, and conflicts with supersession plans. |
| **Related Business Process** | BP-01 (Product Master Data Management), BP-22 (Replenishment Planning & Requisition) |
| **Related Functional Requirements** | FR-002 (Manage product status lifecycle), FR-054 (Create and track purchase requisitions) |
| **Rule Category** | Products |

---

#### BR-029 — Promotional Stock Ring-Fencing

| Attribute | Detail |
|-----------|--------|
| **Rule Name** | Promotional Stock Ring-Fencing |
| **Business Rule Statement** | Promotional stock must be ring-fenced during a campaign. Inventory allocated to a promotion or launch must not be consumed by non-promotional orders without commercial leadership approval. |
| **Business Reason** | Promotional inventory is positioned for a specific campaign period and channel. Allowing non-promotional orders to consume promotional stock defeats the campaign plan and leaves promoted channels without supply. |
| **Related Business Process** | BP-31 (Promotional & Launch Stock Readiness) |
| **Related Functional Requirements** | FR-057 (Support promotional stock readiness review), FR-080 (Deliver campaign and launch readiness alerts) |
| **Rule Category** | Products |

---

### Ownership and Trade

---

#### BR-030 — Bonded Inventory Customs Clearance

| Attribute | Detail |
|-----------|--------|
| **Rule Name** | Bonded Inventory Customs Clearance |
| **Business Rule Statement** | Bonded inventory must not be released into domestic sellable stock without customs clearance. Duties and regulatory release must be confirmed before bonded goods are made available for sale or fulfillment. |
| **Business Reason** | Bonded warehouse stock is under customs control. Duties and taxes have not been paid. Releasing bonded goods into domestic commerce without customs authorization is illegal and creates financial and regulatory liability. |
| **Related Business Process** | BP-07 (Goods Receipt & Verification), BP-09 (Stock Put-Away & Storage) |
| **Related Functional Requirements** | FR-038 (Manage quarantine and hold stock status), FR-018 (Manage put-away and stock availability timing) |
| **Rule Category** | Purchasing |

---

#### BR-031 — Consignment Ownership at Consumption

| Attribute | Detail |
|-----------|--------|
| **Rule Name** | Consignment Ownership at Consumption |
| **Business Rule Statement** | Consignment stock is not owned by the organization until a defined consumption or sale event occurs per supplier agreement. Consignment inventory must not be treated as owned stock for valuation or fulfillment until ownership transfers. |
| **Business Reason** | Consignment inventory is physically at the buyer's location but owned by the supplier until the buyer consumes, sells, or issues it per agreement. Treating consignment as owned inventory overstates assets and triggers incorrect financial recording. |
| **Related Business Process** | BP-30 (Inventory Valuation & Financial Reconciliation), BP-07 (Goods Receipt & Verification) |
| **Related Functional Requirements** | FR-075 (Support inventory valuation summary views), FR-089 (Support financial inventory reconciliation) |
| **Rule Category** | Purchasing |

---

## Rules Summary by Category

| Category | Rule IDs | Count |
|----------|----------|-------|
| **Inventory** | BR-001, BR-002, BR-009, BR-010, BR-011, BR-013, BR-018, BR-020, BR-022, BR-025, BR-028 | 11 |
| **Purchasing** | BR-006, BR-007, BR-008, BR-030, BR-031 | 5 |
| **Warehousing** | BR-003, BR-004, BR-005, BR-012, BR-024, BR-026 | 6 |
| **Products** | BR-014, BR-015, BR-016, BR-017, BR-027, BR-029, BR-032 | 7 |
| **Users** | BR-019, BR-021, BR-023 | 3 |
| **Reporting** | — | 0 |
| **Total** | BR-001 through BR-032 | **32** |

*Note: Reporting as a category applies to business oversight processes (BP-29, BP-32) that consume rule compliance data rather than standalone inventory policy rules.*

---

## Rules by Business Process Domain

| Process Domain | Related Rules |
|----------------|---------------|
| Master Data & Governance (BP-01 – BP-04) | BR-027, BR-032 |
| Inbound & Receiving (BP-05 – BP-09) | BR-004, BR-005, BR-006, BR-007, BR-008, BR-016, BR-017, BR-030 |
| Inventory Control (BP-10 – BP-15) | BR-013, BR-018, BR-019, BR-020, BR-021, BR-022, BR-023, BR-024 |
| Order Fulfillment (BP-16 – BP-20) | BR-001, BR-002, BR-003, BR-028 |
| Replenishment (BP-21 – BP-23) | BR-009, BR-010, BR-011 |
| Network Balance (BP-24 – BP-26) | BR-011, BR-012 |
| Returns (BP-27 – BP-28) | BR-025, BR-026 |
| Performance & Financial (BP-29 – BP-30) | BR-008, BR-031 |
| Commercial & Governance (BP-31 – BP-32) | BR-029, BR-019, BR-021, BR-023 |

---

## Interdependent Rule Combinations

The BRD identifies the following rule combinations that must operate together to be effective:

| Combination | Business Purpose |
|-------------|------------------|
| BR-001 + BR-002 | ATP defines what is available; reservation locks it against confirmed commitments |
| BR-004 + BR-006 | Verification confirms what arrived; documentation preserves supplier accountability |
| BR-018 + BR-019 | Blind counting detects variance; independent approval prevents fraud |
| BR-020 + BR-022 | Investigation finds root cause; reason code captures it for analysis |
| BR-014 + BR-016 | FEFO manages rotation; MRSL prevents accepting stock too close to expiry |
| BR-011 + BR-012 | Network check enables transfer; source protection prevents new shortages |

---

## Traceability Reference

| Source | Identifier |
|--------|------------|
| Business Requirements Document | BRD-IMS-001, Section 13 |
| Industry Business Rules (Domain Knowledge) | 32 operational rules |
| Functional Requirements | FR-001 – FR-090 |
| Business Processes | BP-01 – BP-32 |
| Separation of Duties | SOD-003, SOD-004, SOD-006, SOD-007 (support BR-019, BR-021) |

---

## Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Senior Business Analyst | | | |
| Product Owner | | | |
| Operations Director | | | |
| Inventory Controller | | | |

---

*End of Business Rules Specification*

*Document ID: SRS-BR-001 | Version 1.0 | July 5, 2026*
