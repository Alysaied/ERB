# Domain Entity Relationships
## Inventory Management System

---

## Document Information

| Attribute | Detail |
|-----------|--------|
| **Document ID** | SRS-DM-004 |
| **Document Title** | Domain Entity Relationships — Inventory Management System |
| **Version** | 1.0 |
| **Status** | Draft |
| **Document Owner** | Domain Expert |
| **Source Documents** | SRS-DM-001 (Domain Entity Model, v1.0), SRS-DM-003 (Domain Aggregates, v1.0), SRS-BR-001 (Business Rules, v1.0) |
| **Date** | July 5, 2026 |
| **Scope** | Business relationships only — no database foreign keys, ORM mappings, or persistence design |

### Purpose

This document identifies **business relationships** between all 40 domain entities in the Inventory Management System. Each relationship expresses how entities collaborate in real operational workflows — ownership, dependency, modification, authorization, and derivation — independent of how any system stores or joins data.

### Relationship Type Legend

| Type | Meaning |
|------|---------|
| **Composition** | Target is a constituent part of source; target lifecycle is bound to source |
| **Association** | Ongoing business link; both entities exist independently |
| **Reference** | Source identifies or consults target by business identity without ownership |
| **Modification** | Source operation changes quantity, status, or availability of target |
| **Derivation** | Target is computed, triggered, or produced from source state or event |
| **Authorization** | Source permits, gates, or validates an action on target |
| **Verification** | Source is validated against target before proceeding |

### Multiplicity Notation

| Notation | Meaning |
|----------|---------|
| **1** | Exactly one |
| **0..1** | Zero or one (optional) |
| **1..*** | One or more (mandatory, many allowed) |
| **0..*** | Zero or more (optional, many allowed) |
| *** ** | Many (zero or more) |

---

## Relationship Index by Domain

| Domain | Relationship IDs | Count |
|--------|------------------|-------|
| Master Data & Reference | REL-001 – REL-018 | 18 |
| Inventory State & Balance | REL-019 – REL-032 | 14 |
| Procurement & Inbound | REL-033 – REL-058 | 26 |
| Order Fulfillment | REL-059 – REL-074 | 16 |
| Network Balance | REL-075 – REL-084 | 10 |
| Inventory Control & Accuracy | REL-085 – REL-104 | 20 |
| Returns Management | REL-105 – REL-114 | 10 |
| Accountability & Oversight | REL-115 – REL-128 | 14 |
| Financial Alignment | REL-129 – REL-134 | 6 |
| **Total** | **REL-001 – REL-134** | **134** |

---

## Domain 1: Master Data & Reference

---

### REL-001

| Field | Detail |
|-------|--------|
| **Source Entity** | Product |
| **Target Entity** | Stock Position |
| **Relationship Type** | Association |
| **Business Meaning** | Every stock balance tracks exactly one product; a product may be held at zero or many locations simultaneously. Product defines *what* is counted; Stock Position defines *how much* and *where*. |
| **Multiplicity** | Product **1** → Stock Position **0..*** |
| **Business Rules** | BR-027 — discontinued products must not receive new stock through procurement; existing Stock Positions may remain until depleted. BR-017 — traceable products require lot attribution on all Stock Position movements. |

---

### REL-002

| Field | Detail |
|-------|--------|
| **Source Entity** | Product |
| **Target Entity** | Stock Policy |
| **Relationship Type** | Association |
| **Business Meaning** | Replenishment thresholds are defined per product (and per location on the policy). Product classification (ABC, rotation, shelf-life) determines how policy is applied and monitored. |
| **Multiplicity** | Product **1** → Stock Policy **0..*** |
| **Business Rules** | BR-009 — reorder action triggers when Stock Position ATP reaches product-location reorder level defined in Stock Policy. BR-032 — Class A products require highest monitoring intensity. |

---

### REL-003

| Field | Detail |
|-------|--------|
| **Source Entity** | Product |
| **Target Entity** | Lot/Batch |
| **Relationship Type** | Composition |
| **Business Meaning** | For traceable products, lot/batch records are subordinate groupings of stock identity within a product scope. Lots cannot exist without a parent product definition. |
| **Multiplicity** | Product **1** → Lot/Batch **0..*** |
| **Business Rules** | BR-017 — lot identity must be captured at receipt and through all movements for traceable products. BR-014 — FEFO applies when product has shelf-life; BR-015 — FIFO for standard goods. |

---

### REL-004

| Field | Detail |
|-------|--------|
| **Source Entity** | Inventory Location |
| **Target Entity** | Storage Position |
| **Relationship Type** | Composition |
| **Business Meaning** | Storage positions are physical subdivisions within a location (zones, bins, shelves). They cannot exist outside their parent location and are decommissioned when the location closes. |
| **Multiplicity** | Inventory Location **1** → Storage Position **1..*** |
| **Business Rules** | BR-005 — put-away assigns received goods to a Storage Position before Stock Position ATP increases. BR-024 — location freeze suspends put-away activity during Physical Inventory Count. |

---

### REL-005

| Field | Detail |
|-------|--------|
| **Source Entity** | Inventory Location |
| **Target Entity** | Stock Position |
| **Relationship Type** | Association |
| **Business Meaning** | Stock balances are anchored to a location. A location holds zero or many product balances; each balance exists at exactly one location. |
| **Multiplicity** | Inventory Location **1** → Stock Position **0..*** |
| **Business Rules** | BR-012 — inter-location transfers must not deplete source location Stock Position below its Stock Policy minimum. BR-024 — location must be frozen during wall-to-wall count. |

---

### REL-006

| Field | Detail |
|-------|--------|
| **Source Entity** | Inventory Location |
| **Target Entity** | Inventory Location *(parent)* |
| **Relationship Type** | Association *(hierarchy)* |
| **Business Meaning** | Locations form a network hierarchy (region → site → zone) for reporting roll-up and organizational accountability. A location may optionally belong to one parent location. |
| **Multiplicity** | Inventory Location *(child)* **0..1** → Inventory Location *(parent)* **1** ; parent **1** → children **0..*** |
| **Business Rules** | A location cannot be its own parent or ancestor. Deactivated parent does not automatically deactivate children — each location has independent operational status. |

---

### REL-007

| Field | Detail |
|-------|--------|
| **Source Entity** | Inventory Location |
| **Target Entity** | Physical Inventory Count |
| **Relationship Type** | Association |
| **Business Meaning** | A wall-to-wall count event applies to exactly one location. The count event imposes operational freeze on that location for its duration. |
| **Multiplicity** | Inventory Location **1** → Physical Inventory Count **0..*** |
| **Business Rules** | BR-024 — receiving, shipping, transfers, and adjustments suspended at location while Physical Inventory Count is active and uncertified. |

---

### REL-008

| Field | Detail |
|-------|--------|
| **Source Entity** | Stock Policy |
| **Target Entity** | Product |
| **Relationship Type** | Reference |
| **Business Meaning** | Stock Policy is scoped to a specific product. The policy defines replenishment behavior for that SKU at a given location. |
| **Multiplicity** | Stock Policy **1** → Product **1** |
| **Business Rules** | BR-009 — reorder level on policy triggers replenishment when ATP breaches threshold. BR-010 — safety stock on policy must not be bypassed without authorized exception. |

---

### REL-009

| Field | Detail |
|-------|--------|
| **Source Entity** | Stock Policy |
| **Target Entity** | Inventory Location |
| **Relationship Type** | Reference |
| **Business Meaning** | Stock Policy is scoped to a specific location. The same product may have different thresholds at different locations reflecting local demand and lead time. |
| **Multiplicity** | Stock Policy **1** → Inventory Location **1** |
| **Business Rules** | BR-012 — minimum threshold on source location policy constrains maximum transfer quantity. Product + Location combination uniquely identifies a Stock Policy. |

---

### REL-010

| Field | Detail |
|-------|--------|
| **Source Entity** | Stock Policy |
| **Target Entity** | Operational Alert |
| **Relationship Type** | Derivation |
| **Business Meaning** | When Stock Position ATP crosses policy thresholds (reorder level, minimum, zero), the system derives low-stock or out-of-stock alerts for replenishment review. |
| **Multiplicity** | Stock Policy **1** → Operational Alert **0..*** |
| **Business Rules** | BR-009 — replenishment action must be initiated same business day when reorder level is reached. BR-032 — Class A products generate higher-priority alerts. |

---

### REL-011

| Field | Detail |
|-------|--------|
| **Source Entity** | Reason Code |
| **Target Entity** | Stock Adjustment |
| **Relationship Type** | Authorization |
| **Business Meaning** | Every stock adjustment must cite a reason code explaining why the correction occurred. Reason code categorizes the adjustment for shrinkage analysis and audit. |
| **Multiplicity** | Reason Code **1** → Stock Adjustment **0..*** ; Stock Adjustment **1** → Reason Code **1** |
| **Business Rules** | BR-020 — no adjustment may be applied without a categorized reason code. Retired reason codes must not be used on new adjustments. |

---

### REL-012

| Field | Detail |
|-------|--------|
| **Source Entity** | Reason Code |
| **Target Entity** | Inventory Write-Off |
| **Relationship Type** | Authorization |
| **Business Meaning** | Write-offs require a reason code documenting why inventory value is permanently removed (damage, obsolescence, loss). |
| **Multiplicity** | Reason Code **1** → Inventory Write-Off **0..*** ; Inventory Write-Off **1** → Reason Code **1** |
| **Business Rules** | BR-020, BR-023 — mandatory reason code plus documented evidence and authorization for write-offs. |

---

### REL-013

| Field | Detail |
|-------|--------|
| **Source Entity** | Reason Code |
| **Target Entity** | Receipt Discrepancy |
| **Relationship Type** | Association |
| **Business Meaning** | Receipt discrepancies are categorized by reason code type (short shipment, damage, wrong item) to drive resolution workflow and supplier accountability. |
| **Multiplicity** | Reason Code **1** → Receipt Discrepancy **0..*** |
| **Business Rules** | BR-006 — discrepancies must be documented with supporting evidence before acceptance. |

---

### REL-014

| Field | Detail |
|-------|--------|
| **Source Entity** | Governance Policy |
| **Target Entity** | Stock Adjustment |
| **Relationship Type** | Verification |
| **Business Meaning** | Governance policy defines approval thresholds that Stock Adjustment must satisfy before taking effect. Adjustments above threshold require independent approver per policy. |
| **Multiplicity** | Governance Policy **1** → Stock Adjustment **0..*** |
| **Business Rules** | BR-021 — adjustments above financial or quantity threshold require independent approval by authorized person who did not initiate underlying transaction. |

---

### REL-015

| Field | Detail |
|-------|--------|
| **Source Entity** | Governance Policy |
| **Target Entity** | Count Variance |
| **Relationship Type** | Verification |
| **Business Meaning** | Governance policy enforces segregation of duties — the counter who created the variance cannot be the approver defined by policy. |
| **Multiplicity** | Governance Policy **1** → Count Variance **0..*** |
| **Business Rules** | BR-019 — person who performed count must not approve adjustments arising from their own count. |

---

### REL-016

| Field | Detail |
|-------|--------|
| **Source Entity** | Governance Policy |
| **Target Entity** | Goods Receipt |
| **Relationship Type** | Verification |
| **Business Meaning** | Governance policy defines receipt quantity tolerance and ad-hoc receipt exception rules. Goods Receipt is evaluated against policy before acceptance. |
| **Multiplicity** | Governance Policy **1** → Goods Receipt **0..*** |
| **Business Rules** | BR-007 — PO required except where explicitly approved ad-hoc exception applies per governance policy. |

---

### REL-017

| Field | Detail |
|-------|--------|
| **Source Entity** | Storage Position |
| **Target Entity** | Put-Away |
| **Relationship Type** | Association |
| **Business Meaning** | Put-away confirms placement of received goods into a designated storage position, making stock physically findable for picking. |
| **Multiplicity** | Storage Position **1** → Put-Away **0..*** ; Put-Away **1** → Storage Position **1** |
| **Business Rules** | BR-005 — stock not available until put-away to storage position is confirmed. BR-014, BR-015 — rotation placement at put-away. |

---

### REL-018

| Field | Detail |
|-------|--------|
| **Source Entity** | Storage Position |
| **Target Entity** | Fulfillment Execution |
| **Relationship Type** | Reference |
| **Business Meaning** | Pick operations retrieve stock from a storage position. Fulfillment execution records which position supplied each pick line. |
| **Multiplicity** | Storage Position **1** → Fulfillment Execution **0..*** |
| **Business Rules** | BR-003 — pick must be verified before shipment. BR-014, BR-015 — FEFO/FIFO guides which storage position/lot is picked first. |

---

## Domain 2: Inventory State & Balance

---

### REL-019

| Field | Detail |
|-------|--------|
| **Source Entity** | Stock Position |
| **Target Entity** | Product |
| **Relationship Type** | Reference |
| **Business Meaning** | Stock Position identifies which product's quantity is being tracked. The product must exist in the catalog and be valid for the operation context. |
| **Multiplicity** | Stock Position **1** → Product **1** |
| **Business Rules** | BR-001 — ATP on Stock Position is the only quotable quantity for customer commitment. BR-027 — discontinued product positions deplete but are not replenished. |

---

### REL-020

| Field | Detail |
|-------|--------|
| **Source Entity** | Stock Position |
| **Target Entity** | Inventory Location |
| **Relationship Type** | Reference |
| **Business Meaning** | Stock Position is scoped to exactly one location — the place where the physical stock resides. |
| **Multiplicity** | Stock Position **1** → Inventory Location **1** |
| **Business Rules** | BR-012 — source location minimum applies when Stock Position at source is reduced by transfer. |

---

### REL-021

| Field | Detail |
|-------|--------|
| **Source Entity** | Stock Position |
| **Target Entity** | Stock Policy |
| **Relationship Type** | Reference |
| **Business Meaning** | Stock Position availability status (in stock, low stock, out of stock, overstock) is evaluated against the Stock Policy thresholds for the same product and location. |
| **Multiplicity** | Stock Position **1** → Stock Policy **0..1** |
| **Business Rules** | BR-009 — reorder triggered when ATP reaches policy reorder level. BR-010 — safety stock on policy protects against routine consumption. |

---

### REL-022

| Field | Detail |
|-------|--------|
| **Source Entity** | Stock Position |
| **Target Entity** | Quarantine Hold |
| **Relationship Type** | Composition |
| **Business Meaning** | Quarantine holds are applied to specific quantities within a Stock Position, removing held quantity from ATP while remaining physically on-hand. |
| **Multiplicity** | Stock Position **1** → Quarantine Hold **0..*** |
| **Business Rules** | BR-013 — quarantined quantity excluded from sellable ATP. BR-030 — bonded inventory held until customs clearance before release. |

---

### REL-023

| Field | Detail |
|-------|--------|
| **Source Entity** | Stock Position |
| **Target Entity** | Lot/Batch |
| **Relationship Type** | Composition |
| **Business Meaning** | For traceable products, Stock Position quantity is subdivided by lot/batch. Each lot carries expiration and quality attributes affecting pick priority. |
| **Multiplicity** | Stock Position **1** → Lot/Batch **0..*** |
| **Business Rules** | BR-017 — lot captured on all movements. BR-014 — FEFO pick order by lot expiration date. |

---

### REL-024

| Field | Detail |
|-------|--------|
| **Source Entity** | Inventory Reservation |
| **Target Entity** | Stock Position |
| **Relationship Type** | Modification |
| **Business Meaning** | Creating a reservation increases reserved quantity and decreases ATP on the target Stock Position. Releasing or fulfilling a reservation reverses or finalizes the hold. |
| **Multiplicity** | Inventory Reservation **0..*** → Stock Position **1** |
| **Business Rules** | BR-002 — reservation at order confirmation removes quantity from ATP. BR-010 — must not consume below safety stock without exception. BR-029 — promotional ring-fenced quantity not available for non-promotional reservations. |

---

### REL-025

| Field | Detail |
|-------|--------|
| **Source Entity** | Promotional Stock Allocation |
| **Target Entity** | Stock Position |
| **Relationship Type** | Modification |
| **Business Meaning** | Promotional allocation ring-fences a portion of Stock Position quantity for campaign use, reducing general ATP available to non-promotional orders. |
| **Multiplicity** | Promotional Stock Allocation **0..*** → Stock Position **1** |
| **Business Rules** | BR-029 — promotional stock must not be consumed by non-promotional orders without commercial leadership approval. |

---

### REL-026

| Field | Detail |
|-------|--------|
| **Source Entity** | Promotional Stock Allocation |
| **Target Entity** | Product |
| **Relationship Type** | Reference |
| **Business Meaning** | Allocation specifies which product's stock is ring-fenced for the campaign or launch. |
| **Multiplicity** | Promotional Stock Allocation **1** → Product **1** |
| **Business Rules** | BR-029 — allocation quantity must be confirmed before campaign commitment (BP-31). |

---

### REL-027

| Field | Detail |
|-------|--------|
| **Source Entity** | Promotional Stock Allocation |
| **Target Entity** | Inventory Location |
| **Relationship Type** | Reference |
| **Business Meaning** | Allocation may scope ring-fenced quantity to one or more locations supplying the promotional channel. |
| **Multiplicity** | Promotional Stock Allocation **1** → Inventory Location **1..*** |
| **Business Rules** | BR-029 — readiness review confirms sufficient allocated stock at fulfillment locations before campaign start. |

---

### REL-028

| Field | Detail |
|-------|--------|
| **Source Entity** | Quarantine Hold |
| **Target Entity** | Lot/Batch |
| **Relationship Type** | Reference |
| **Business Meaning** | Quality holds may target a specific lot within a Stock Position for targeted recall or investigation scope limitation. |
| **Multiplicity** | Quarantine Hold **0..1** → Lot/Batch **1** ; Lot/Batch **1** → Quarantine Hold **0..*** |
| **Business Rules** | BR-013 — held lot quantity excluded from ATP. BR-030 — bonded lots held pending customs clearance. |

---

### REL-029

| Field | Detail |
|-------|--------|
| **Source Entity** | Goods Receipt |
| **Target Entity** | Stock Position |
| **Relationship Type** | Modification |
| **Business Meaning** | Completed put-away following goods receipt increases on-hand quantity on the Stock Position at the receiving location. Until put-away completes, Stock Position is not modified. |
| **Multiplicity** | Goods Receipt **0..*** → Stock Position **1** |
| **Business Rules** | BR-004 — verify before acceptance. BR-005 — put-away before availability increase. BR-016 — MRSL check before acceptance. |

---

### REL-030

| Field | Detail |
|-------|--------|
| **Source Entity** | Shipment |
| **Target Entity** | Stock Position |
| **Relationship Type** | Modification |
| **Business Meaning** | Shipment dispatch decreases on-hand and releases reserved quantity on the ship-from Stock Position. |
| **Multiplicity** | Shipment **0..*** → Stock Position **1** |
| **Business Rules** | BR-003 — shipment only after verified pick. BR-002 — reservation released or consumed on shipment. |

---

### REL-031

| Field | Detail |
|-------|--------|
| **Source Entity** | Stock Adjustment |
| **Target Entity** | Stock Position |
| **Relationship Type** | Modification |
| **Business Meaning** | Approved stock adjustment increases or decreases on-hand quantity on Stock Position to align record with physical reality. |
| **Multiplicity** | Stock Adjustment **0..*** → Stock Position **1** |
| **Business Rules** | BR-020 — reason code mandatory. BR-021 — independent approval above threshold. BR-022 — investigate before adjusting when originating from count variance. |

---

### REL-032

| Field | Detail |
|-------|--------|
| **Source Entity** | Inventory Write-Off |
| **Target Entity** | Stock Position |
| **Relationship Type** | Modification |
| **Business Meaning** | Write-off permanently decreases on-hand quantity and removes inventory value from Stock Position. Distinct from adjustment — write-off is terminal. |
| **Multiplicity** | Inventory Write-Off **0..*** → Stock Position **1** |
| **Business Rules** | BR-023 — documented evidence and authorization required. BR-020 — reason code mandatory. |

---

## Domain 3: Procurement & Inbound Supply

---

### REL-033

| Field | Detail |
|-------|--------|
| **Source Entity** | Supplier |
| **Target Entity** | Purchase Order |
| **Relationship Type** | Association |
| **Business Meaning** | Purchase orders are commercial commitments to a specific supplier. A supplier may have many open and historical purchase orders. |
| **Multiplicity** | Supplier **1** → Purchase Order **0..*** |
| **Business Rules** | BR-007 — PO authorizes supplier receipt. BR-031 — consignment supplier relationship affects Stock Position ownership classification at receipt. |

---

### REL-034

| Field | Detail |
|-------|--------|
| **Source Entity** | Supplier |
| **Target Entity** | Supplier Invoice |
| **Relationship Type** | Association |
| **Business Meaning** | Supplier invoices are billing documents from a supplier, matched against POs and receipts for payment authorization. |
| **Multiplicity** | Supplier **1** → Supplier Invoice **0..*** |
| **Business Rules** | BR-008 — three-way match before payment authorization. |

---

### REL-035

| Field | Detail |
|-------|--------|
| **Source Entity** | Purchase Requisition |
| **Target Entity** | Product |
| **Relationship Type** | Reference |
| **Business Meaning** | Requisition lines specify which products the organization intends to procure and in what quantity. |
| **Multiplicity** | Purchase Requisition **1** → Product **1..*** |
| **Business Rules** | BR-027 — discontinued products prohibited on requisitions. BR-011 — network check before requisition approval. |

---

### REL-036

| Field | Detail |
|-------|--------|
| **Source Entity** | Purchase Requisition |
| **Target Entity** | Inventory Location |
| **Relationship Type** | Reference |
| **Business Meaning** | Requisition specifies the target receiving location where inbound stock is needed. |
| **Multiplicity** | Purchase Requisition **1** → Inventory Location **1** |
| **Business Rules** | BR-009 — requisition typically triggered by Stock Policy threshold breach at requesting location. BR-010 — safety stock protection evaluated before approval. |

---

### REL-037

| Field | Detail |
|-------|--------|
| **Source Entity** | Purchase Requisition |
| **Target Entity** | Purchase Order |
| **Relationship Type** | Derivation |
| **Business Meaning** | An approved requisition is converted into a purchase order — the commercial document sent to the supplier. One requisition may produce zero or one PO. |
| **Multiplicity** | Purchase Requisition **1** → Purchase Order **0..1** |
| **Business Rules** | BR-027 — PO must not include discontinued products from requisition. BR-011 — network transfer alternative should be evaluated before PO creation. |

---

### REL-038

| Field | Detail |
|-------|--------|
| **Source Entity** | Purchase Requisition |
| **Target Entity** | Operational Alert |
| **Relationship Type** | Reference |
| **Business Meaning** | Requisitions may be triggered by low-stock or out-of-stock alerts, maintaining traceability from alert to procurement action. |
| **Multiplicity** | Operational Alert **0..1** → Purchase Requisition **0..1** |
| **Business Rules** | BR-009 — replenishment action same business day as alert for reorder-level breach. |

---

### REL-039

| Field | Detail |
|-------|--------|
| **Source Entity** | Purchase Order |
| **Target Entity** | Supplier |
| **Relationship Type** | Reference |
| **Business Meaning** | Every PO identifies the supplier who will fulfill the order. PO cannot exist without a valid active supplier. |
| **Multiplicity** | Purchase Order **1** → Supplier **1** |
| **Business Rules** | BR-007 — PO is the authorization document for supplier receipt. BR-008 — PO is the first leg of three-way match. |

---

### REL-040

| Field | Detail |
|-------|--------|
| **Source Entity** | Purchase Order |
| **Target Entity** | Inventory Location |
| **Relationship Type** | Reference |
| **Business Meaning** | PO specifies the receiving location where goods are expected to be delivered and put away. |
| **Multiplicity** | Purchase Order **1** → Inventory Location **1** |
| **Business Rules** | Receiving location must be active. Goods Receipt must occur at PO-designated location unless authorized redirect. |

---

### REL-041

| Field | Detail |
|-------|--------|
| **Source Entity** | Purchase Order |
| **Target Entity** | Product |
| **Relationship Type** | Reference |
| **Business Meaning** | PO line items reference products being ordered with quantity and price. |
| **Multiplicity** | Purchase Order **1** → Product **1..*** |
| **Business Rules** | BR-027 — discontinued products prohibited on new PO lines. |

---

### REL-042

| Field | Detail |
|-------|--------|
| **Source Entity** | Purchase Order |
| **Target Entity** | Expected Inbound Delivery |
| **Relationship Type** | Composition |
| **Business Meaning** | Expected inbound deliveries are shipment plans subordinate to a PO, communicating anticipated arrival dates and quantities to receiving operations. |
| **Multiplicity** | Purchase Order **1** → Expected Inbound Delivery **0..*** |
| **Business Rules** | Expected delivery dates must align with PO expected delivery. Delays trigger inbound supply notifications (BP-23). |

---

### REL-043

| Field | Detail |
|-------|--------|
| **Source Entity** | Purchase Order |
| **Target Entity** | Goods Receipt |
| **Relationship Type** | Authorization |
| **Business Meaning** | PO authorizes what may be received from the supplier. Goods receipt must match to a valid PO except approved ad-hoc exceptions. |
| **Multiplicity** | Purchase Order **1** → Goods Receipt **0..*** |
| **Business Rules** | BR-007 — valid PO required before supplier goods acceptance. BR-004 — verify received against PO quantity and product. |

---

### REL-044

| Field | Detail |
|-------|--------|
| **Source Entity** | Purchase Order |
| **Target Entity** | Supplier Invoice |
| **Relationship Type** | Verification |
| **Business Meaning** | Supplier invoice is matched against the PO as the first leg of three-way match — confirming billed items were authorized for purchase. |
| **Multiplicity** | Purchase Order **1** → Supplier Invoice **0..*** |
| **Business Rules** | BR-008 — PO, receipt, and invoice must agree within tolerance before payment. |

---

### REL-045

| Field | Detail |
|-------|--------|
| **Source Entity** | Expected Inbound Delivery |
| **Target Entity** | Purchase Order |
| **Relationship Type** | Reference |
| **Business Meaning** | Inbound delivery plan belongs to and derives quantities from its parent purchase order. |
| **Multiplicity** | Expected Inbound Delivery **1** → Purchase Order **1** |
| **Business Rules** | Expected quantities must not exceed remaining open PO line quantities. |

---

### REL-046

| Field | Detail |
|-------|--------|
| **Source Entity** | Expected Inbound Delivery |
| **Target Entity** | Stock Position |
| **Relationship Type** | Derivation |
| **Business Meaning** | Expected inbound quantity contributes to network availability views — stock "in pipeline" before physical receipt — informing replenishment and fulfillment planning. |
| **Multiplicity** | Expected Inbound Delivery **0..*** → Stock Position **1** |
| **Business Rules** | Inbound expected is informational only — does not increase ATP until put-away completes (BR-005). |

---

### REL-047

| Field | Detail |
|-------|--------|
| **Source Entity** | Goods Receipt |
| **Target Entity** | Purchase Order |
| **Relationship Type** | Verification |
| **Business Meaning** | Receipt verifies inbound goods against PO — confirming product identity, quantity, and condition match the authorized order. |
| **Multiplicity** | Goods Receipt **0..*** → Purchase Order **0..1** |
| **Business Rules** | BR-007 — PO reference required except ad-hoc exception. BR-004 — verify before acceptance. BR-006 — document discrepancies before acceptance. |

---

### REL-048

| Field | Detail |
|-------|--------|
| **Source Entity** | Goods Receipt |
| **Target Entity** | Supplier |
| **Relationship Type** | Reference |
| **Business Meaning** | Receipt records which supplier delivered the goods, supporting supplier performance tracking and discrepancy claims. |
| **Multiplicity** | Goods Receipt **1** → Supplier **1** |
| **Business Rules** | BR-006 — discrepancy documentation preserves supplier accountability at receipt when carrier or supplier is present. |

---

### REL-049

| Field | Detail |
|-------|--------|
| **Source Entity** | Goods Receipt |
| **Target Entity** | Inventory Location |
| **Relationship Type** | Reference |
| **Business Meaning** | Receipt occurs at a receiving location — the dock where goods arrive before put-away to storage positions. |
| **Multiplicity** | Goods Receipt **1** → Inventory Location **1** |
| **Business Rules** | BR-024 — receipt blocked at location under physical inventory freeze. |

---

### REL-050

| Field | Detail |
|-------|--------|
| **Source Entity** | Goods Receipt |
| **Target Entity** | Receipt Discrepancy |
| **Relationship Type** | Composition |
| **Business Meaning** | Discrepancies are exception records subordinate to a goods receipt, documenting variance between expected and actual at the point of receipt. |
| **Multiplicity** | Goods Receipt **1** → Receipt Discrepancy **0..*** |
| **Business Rules** | BR-006 — discrepancies documented before acceptance. BR-016 — shelf-life non-compliance recorded as discrepancy. |

---

### REL-051

| Field | Detail |
|-------|--------|
| **Source Entity** | Goods Receipt |
| **Target Entity** | Put-Away |
| **Relationship Type** | Composition |
| **Business Meaning** | Put-away is the final step of the receipt workflow — moving verified goods from dock to storage. Every accepted receipt line requires put-away before availability. |
| **Multiplicity** | Goods Receipt **1** → Put-Away **1..*** |
| **Business Rules** | BR-005 — ATP not increased until put-away confirmed. BR-030 — bonded goods put-away to hold storage until customs clearance. |

---

### REL-052

| Field | Detail |
|-------|--------|
| **Source Entity** | Goods Receipt |
| **Target Entity** | Lot/Batch |
| **Relationship Type** | Derivation |
| **Business Meaning** | Receipt of traceable products creates or assigns lot/batch records with expiration and supplier origin captured at the point of entry. |
| **Multiplicity** | Goods Receipt **0..*** → Lot/Batch **0..*** |
| **Business Rules** | BR-017 — lot/batch captured at receipt. BR-016 — MRSL validated at receipt for shelf-life products. |

---

### REL-053

| Field | Detail |
|-------|--------|
| **Source Entity** | Receipt Discrepancy |
| **Target Entity** | Goods Receipt |
| **Relationship Type** | Reference |
| **Business Meaning** | Discrepancy belongs to the receipt event where the variance was discovered — evidence tied to point of arrival. |
| **Multiplicity** | Receipt Discrepancy **1** → Goods Receipt **1** |
| **Business Rules** | BR-006 — must be recorded when carrier or supplier present. BR-008 — unresolved discrepancies affect three-way match outcome. |

---

### REL-054

| Field | Detail |
|-------|--------|
| **Source Entity** | Put-Away |
| **Target Entity** | Goods Receipt |
| **Relationship Type** | Reference |
| **Business Meaning** | Put-away completes a goods receipt line — without put-away the receipt is incomplete from an availability perspective. |
| **Multiplicity** | Put-Away **1** → Goods Receipt **1** |
| **Business Rules** | BR-005 — availability begins at put-away confirmation, not at dock receipt. |

---

### REL-055

| Field | Detail |
|-------|--------|
| **Source Entity** | Supplier Invoice |
| **Target Entity** | Purchase Order |
| **Relationship Type** | Verification |
| **Business Meaning** | Invoice lines are matched to PO lines to confirm supplier is billing for authorized products at agreed prices. |
| **Multiplicity** | Supplier Invoice **1** → Purchase Order **1** |
| **Business Rules** | BR-008 — three-way match required before payment. |

---

### REL-056

| Field | Detail |
|-------|--------|
| **Source Entity** | Supplier Invoice |
| **Target Entity** | Goods Receipt |
| **Relationship Type** | Verification |
| **Business Meaning** | Invoice lines are matched to receipt lines to confirm supplier is billing only for goods actually received and accepted. |
| **Multiplicity** | Supplier Invoice **1** → Goods Receipt **0..*** |
| **Business Rules** | BR-008 — payment prohibited for unreceived or mispriced goods. Receipt discrepancies may block match. |

---

### REL-057

| Field | Detail |
|-------|--------|
| **Source Entity** | Supplier Invoice |
| **Target Entity** | Supplier |
| **Relationship Type** | Reference |
| **Business Meaning** | Invoice identifies the billing supplier. Payment authorization is directed to this commercial counterparty. |
| **Multiplicity** | Supplier Invoice **1** → Supplier **1** |
| **Business Rules** | BR-008 — match must be confirmed before payment to supplier. |

---

### REL-058

| Field | Detail |
|-------|--------|
| **Source Entity** | Supplier Invoice |
| **Target Entity** | Inventory Valuation Snapshot |
| **Relationship Type** | Derivation |
| **Business Meaning** | Invoice unit costs inform inventory valuation for received goods included in period-end financial reconciliation. |
| **Multiplicity** | Supplier Invoice **0..*** → Inventory Valuation Snapshot **1** |
| **Business Rules** | BR-008 — financial alignment depends on accurate PO-receipt-invoice matching. BR-031 — consignment goods excluded from owned valuation. |

---

## Domain 4: Order Fulfillment

---

### REL-059

| Field | Detail |
|-------|--------|
| **Source Entity** | Customer Order |
| **Target Entity** | Stock Position |
| **Relationship Type** | Reference |
| **Business Meaning** | Order availability confirmation consults Stock Position ATP to determine whether the order can be committed. Order does not own stock — it references availability. |
| **Multiplicity** | Customer Order **1** → Stock Position **1..*** |
| **Business Rules** | BR-001 — commit only against ATP, not total on-hand. Multi-location orders may reference multiple Stock Positions. |

---

### REL-060

| Field | Detail |
|-------|--------|
| **Source Entity** | Customer Order |
| **Target Entity** | Inventory Reservation |
| **Relationship Type** | Composition |
| **Business Meaning** | Reservations are operational holds created when the order is confirmed, one or more per order line, locking stock until fulfillment or cancellation. |
| **Multiplicity** | Customer Order **1** → Inventory Reservation **0..*** |
| **Business Rules** | BR-002 — reservation mandatory at order confirmation. BR-029 — must respect promotional ring-fence. |

---

### REL-061

| Field | Detail |
|-------|--------|
| **Source Entity** | Customer Order |
| **Target Entity** | Fulfillment Execution |
| **Relationship Type** | Composition |
| **Business Meaning** | Fulfillment execution is warehouse work (pick, pack) triggered by a confirmed order. One order may have one or more fulfillment executions (e.g., split fulfillment). |
| **Multiplicity** | Customer Order **1** → Fulfillment Execution **0..*** |
| **Business Rules** | BR-003 — pick verification required. BR-014, BR-015 — rotation applied during pick. |

---

### REL-062

| Field | Detail |
|-------|--------|
| **Source Entity** | Customer Order |
| **Target Entity** | Backorder |
| **Relationship Type** | Composition |
| **Business Meaning** | Backorders record customer-agreed delays for unfulfilled order line quantity when full ATP is unavailable. |
| **Multiplicity** | Customer Order **1** → Backorder **0..*** |
| **Business Rules** | BR-028 — explicit customer acknowledgment required before backorder is recorded. |

---

### REL-063

| Field | Detail |
|-------|--------|
| **Source Entity** | Customer Order |
| **Target Entity** | Shipment |
| **Relationship Type** | Composition |
| **Business Meaning** | Shipments are dispatch events fulfilling order lines. An order may ship in one or multiple shipments (partial fulfillment). |
| **Multiplicity** | Customer Order **1** → Shipment **0..*** |
| **Business Rules** | BR-003 — shipment only after verified pick. Each shipment deducts stock and consumes reservation. |

---

### REL-064

| Field | Detail |
|-------|--------|
| **Source Entity** | Customer Order |
| **Target Entity** | Return Authorization |
| **Relationship Type** | Association |
| **Business Meaning** | Return authorizations reference the original customer order to validate return eligibility, products, and quantities against what was shipped. |
| **Multiplicity** | Customer Order **1** → Return Authorization **0..*** |
| **Business Rules** | BR-025 — return must link to original order and return policy. |

---

### REL-065

| Field | Detail |
|-------|--------|
| **Source Entity** | Inventory Reservation |
| **Target Entity** | Customer Order |
| **Relationship Type** | Reference |
| **Business Meaning** | Reservation exists to fulfill a specific order line on a specific order. |
| **Multiplicity** | Inventory Reservation **1** → Customer Order **1** |
| **Business Rules** | BR-002 — reservation created at confirmation; released on cancellation or consumed on shipment. |

---

### REL-066

| Field | Detail |
|-------|--------|
| **Source Entity** | Inventory Reservation |
| **Target Entity** | Product |
| **Relationship Type** | Reference |
| **Business Meaning** | Reservation locks quantity of a specific product. |
| **Multiplicity** | Inventory Reservation **1** → Product **1** |
| **Business Rules** | BR-027 — inactive/discontinued products blocked from new reservations. |

---

### REL-067

| Field | Detail |
|-------|--------|
| **Source Entity** | Fulfillment Execution |
| **Target Entity** | Customer Order |
| **Relationship Type** | Reference |
| **Business Meaning** | Fulfillment execution fulfills lines on a specific customer order. |
| **Multiplicity** | Fulfillment Execution **1** → Customer Order **1** |
| **Business Rules** | BR-003 — fulfillment must complete pick verification before shipment entity is created. |

---

### REL-068

| Field | Detail |
|-------|--------|
| **Source Entity** | Fulfillment Execution |
| **Target Entity** | Inventory Location |
| **Relationship Type** | Reference |
| **Business Meaning** | Fulfillment executes at a ship-from location where pick and pack occur. |
| **Multiplicity** | Fulfillment Execution **1** → Inventory Location **1** |
| **Business Rules** | BR-024 — fulfillment blocked at frozen location. Split fulfillment may involve multiple locations. |

---

### REL-069

| Field | Detail |
|-------|--------|
| **Source Entity** | Fulfillment Execution |
| **Target Entity** | Lot/Batch |
| **Relationship Type** | Reference |
| **Business Meaning** | Pick lines on fulfillment execution record which lot was picked for traceable products. |
| **Multiplicity** | Fulfillment Execution **0..*** → Lot/Batch **0..1** *(per pick line)* |
| **Business Rules** | BR-017 — lot captured on pick. BR-014 — earliest-expiring lot picked first (FEFO). |

---

### REL-070

| Field | Detail |
|-------|--------|
| **Source Entity** | Fulfillment Execution |
| **Target Entity** | Shipment |
| **Relationship Type** | Derivation |
| **Business Meaning** | Verified fulfillment execution produces a shipment — dispatch is the outcome of successful pick and pack. |
| **Multiplicity** | Fulfillment Execution **1** → Shipment **0..1** |
| **Business Rules** | BR-003 — no shipment without verified pick completion. |

---

### REL-071

| Field | Detail |
|-------|--------|
| **Source Entity** | Backorder |
| **Target Entity** | Customer Order |
| **Relationship Type** | Reference |
| **Business Meaning** | Backorder records remaining unfulfilled quantity for a specific order line on a customer order. |
| **Multiplicity** | Backorder **1** → Customer Order **1** |
| **Business Rules** | BR-028 — customer acknowledgment required. Backorder may convert to reservation when stock arrives. |

---

### REL-072

| Field | Detail |
|-------|--------|
| **Source Entity** | Backorder |
| **Target Entity** | Product |
| **Relationship Type** | Reference |
| **Business Meaning** | Backorder identifies which product awaits replenishment and fulfillment. |
| **Multiplicity** | Backorder **1** → Product **1** |
| **Business Rules** | Backordered products may receive replenishment priority in BP-22 planning. |

---

### REL-073

| Field | Detail |
|-------|--------|
| **Source Entity** | Shipment |
| **Target Entity** | Fulfillment Execution |
| **Relationship Type** | Reference |
| **Business Meaning** | Shipment records which fulfillment execution authorized the dispatch, maintaining pick-to-ship traceability. |
| **Multiplicity** | Shipment **1** → Fulfillment Execution **1** |
| **Business Rules** | BR-003 — shipment linked to verified fulfillment only. |

---

### REL-074

| Field | Detail |
|-------|--------|
| **Source Entity** | Shipment |
| **Target Entity** | Inventory Reservation |
| **Relationship Type** | Modification |
| **Business Meaning** | Shipment consumes or releases the reservation for shipped quantity — reservation status transitions to fulfilled for shipped lines. |
| **Multiplicity** | Shipment **0..*** → Inventory Reservation **1** |
| **Business Rules** | BR-002 — reservation removed from ATP at confirmation; consumed at shipment. |

---

## Domain 5: Network Balance

---

### REL-075

| Field | Detail |
|-------|--------|
| **Source Entity** | Transfer Request |
| **Target Entity** | Inventory Location *(source)* |
| **Relationship Type** | Reference |
| **Business Meaning** | Transfer request specifies the location sending stock. Source location policy minimum must be evaluated before approval. |
| **Multiplicity** | Transfer Request **1** → Inventory Location *(source)* **1** |
| **Business Rules** | BR-012 — transfer must not deplete source below minimum threshold. BR-010 — safety stock protection at source. |

---

### REL-076

| Field | Detail |
|-------|--------|
| **Source Entity** | Transfer Request |
| **Target Entity** | Inventory Location *(destination)* |
| **Relationship Type** | Reference |
| **Business Meaning** | Transfer request specifies the location receiving stock to resolve local shortage or rebalance network. |
| **Multiplicity** | Transfer Request **1** → Inventory Location *(destination)* **1** |
| **Business Rules** | BR-011 — transfer evaluated before new purchase when network has excess elsewhere. Source and destination must be distinct active locations. |

---

### REL-077

| Field | Detail |
|-------|--------|
| **Source Entity** | Transfer Request |
| **Target Entity** | Product |
| **Relationship Type** | Reference |
| **Business Meaning** | Transfer request specifies product and quantity to move between locations. |
| **Multiplicity** | Transfer Request **1** → Product **1..*** |
| **Business Rules** | BR-017 — lot attribution required on transfer lines for traceable products. |

---

### REL-078

| Field | Detail |
|-------|--------|
| **Source Entity** | Transfer Request |
| **Target Entity** | Stock Transfer |
| **Relationship Type** | Derivation |
| **Business Meaning** | Approved transfer request initiates stock transfer execution. Request may result in zero transfers if rejected. |
| **Multiplicity** | Transfer Request **1** → Stock Transfer **0..1** |
| **Business Rules** | BR-012 — approval validates source can spare quantity above minimum. |

---

### REL-079

| Field | Detail |
|-------|--------|
| **Source Entity** | Transfer Request |
| **Target Entity** | Stock Policy |
| **Relationship Type** | Verification |
| **Business Meaning** | Transfer approval consults source location Stock Policy to ensure transfer quantity does not breach minimum or safety stock thresholds. |
| **Multiplicity** | Transfer Request **0..*** → Stock Policy **1** *(source product-location)* |
| **Business Rules** | BR-012, BR-010 — source minimum and safety stock protection. |

---

### REL-080

| Field | Detail |
|-------|--------|
| **Source Entity** | Stock Transfer |
| **Target Entity** | Transfer Request |
| **Relationship Type** | Reference |
| **Business Meaning** | Executed transfer may originate from an approved transfer request, maintaining request-to-execution traceability. |
| **Multiplicity** | Stock Transfer **0..1** → Transfer Request **1** |
| **Business Rules** | Ad-hoc transfers without request require equivalent authorization per governance policy. |

---

### REL-081

| Field | Detail |
|-------|--------|
| **Source Entity** | Stock Transfer |
| **Target Entity** | In-Transit Stock |
| **Relationship Type** | Composition |
| **Business Meaning** | In-transit stock records are pipeline state subordinate to a stock transfer — tracking quantity between dispatch and destination receipt. |
| **Multiplicity** | Stock Transfer **1** → In-Transit Stock **1..*** |
| **Business Rules** | In-transit quantity excluded from both source and destination ATP until receipt confirmed. |

---

### REL-082

| Field | Detail |
|-------|--------|
| **Source Entity** | Stock Transfer |
| **Target Entity** | Stock Position *(source and destination)* |
| **Relationship Type** | Modification |
| **Business Meaning** | Dispatch decreases source Stock Position; receipt increases destination Stock Position. |
| **Multiplicity** | Stock Transfer **1** → Stock Position **2** *(one source, one destination per product line)* |
| **Business Rules** | BR-012 — source not depleted below minimum. BR-017 — lot captured on transfer. BR-024 — blocked during location freeze. |

---

### REL-083

| Field | Detail |
|-------|--------|
| **Source Entity** | Stock Transfer |
| **Target Entity** | Lot/Batch |
| **Relationship Type** | Reference |
| **Business Meaning** | Transfer lines for traceable products carry lot identity through the network move. |
| **Multiplicity** | Stock Transfer **0..*** → Lot/Batch **0..1** *(per line)* |
| **Business Rules** | BR-017 — lot attribution on all transfer movements. |

---

### REL-084

| Field | Detail |
|-------|--------|
| **Source Entity** | In-Transit Stock |
| **Target Entity** | Stock Transfer |
| **Relationship Type** | Reference |
| **Business Meaning** | In-transit state belongs to a specific stock transfer and has no meaning outside that transfer context. |
| **Multiplicity** | In-Transit Stock **1** → Stock Transfer **1** |
| **Business Rules** | Delayed or lost in-transit stock triggers transfer exception alerts. |

---

## Domain 6: Inventory Control & Accuracy

---

### REL-085

| Field | Detail |
|-------|--------|
| **Source Entity** | Cycle Count |
| **Target Entity** | Product |
| **Relationship Type** | Reference |
| **Business Meaning** | Cycle count assignment targets a specific product (or product set) for physical verification. |
| **Multiplicity** | Cycle Count **1** → Product **1** |
| **Business Rules** | BR-032 — Class A products scheduled at highest frequency. BR-018 — blind count enforced. |

---

### REL-086

| Field | Detail |
|-------|--------|
| **Source Entity** | Cycle Count |
| **Target Entity** | Inventory Location |
| **Relationship Type** | Reference |
| **Business Meaning** | Cycle count occurs at a specific location where the product stock is held. |
| **Multiplicity** | Cycle Count **1** → Inventory Location **1** |
| **Business Rules** | BR-018 — counter must not see system quantity before recording physical count. |

---

### REL-087

| Field | Detail |
|-------|--------|
| **Source Entity** | Cycle Count |
| **Target Entity** | Storage Position |
| **Relationship Type** | Reference |
| **Business Meaning** | Cycle count may optionally scope to a specific storage position for bin-level accuracy programs. |
| **Multiplicity** | Cycle Count **0..1** → Storage Position **1** |
| **Business Rules** | Optional bin-level scope in Phase 2 operations. |

---

### REL-088

| Field | Detail |
|-------|--------|
| **Source Entity** | Cycle Count |
| **Target Entity** | Count Variance |
| **Relationship Type** | Derivation |
| **Business Meaning** | When physical count differs from system quantity, cycle count produces a count variance for investigation. |
| **Multiplicity** | Cycle Count **1** → Count Variance **0..1** |
| **Business Rules** | BR-018 — variance calculated at submission, not shown to counter during count. BR-022 — investigation required before adjustment. |

---

### REL-089

| Field | Detail |
|-------|--------|
| **Source Entity** | Cycle Count |
| **Target Entity** | User Account *(counter)* |
| **Relationship Type** | Reference |
| **Business Meaning** | Cycle count records who performed the physical count for accountability and segregation-of-duties enforcement. |
| **Multiplicity** | Cycle Count **1** → User Account **1** |
| **Business Rules** | BR-019 — counter must not approve resulting adjustments. |

---

### REL-090

| Field | Detail |
|-------|--------|
| **Source Entity** | Physical Inventory Count |
| **Target Entity** | Inventory Location |
| **Relationship Type** | Association |
| **Business Meaning** | Physical count applies to an entire location, imposing freeze and full scope count across all products at the site. |
| **Multiplicity** | Physical Inventory Count **1** → Inventory Location **1** |
| **Business Rules** | BR-024 — freeze all movements at location during count. |

---

### REL-091

| Field | Detail |
|-------|--------|
| **Source Entity** | Physical Inventory Count |
| **Target Entity** | Count Variance |
| **Relationship Type** | Derivation |
| **Business Meaning** | Wall-to-wall count may produce multiple count variances — one per product/location combination where physical differs from system. |
| **Multiplicity** | Physical Inventory Count **1** → Count Variance **0..*** |
| **Business Rules** | BR-022 — each variance investigated before adjustment. BR-024 — no movements during count that would invalidate snapshot. |

---

### REL-092

| Field | Detail |
|-------|--------|
| **Source Entity** | Count Variance |
| **Target Entity** | Cycle Count *(or Physical Inventory Count)* |
| **Relationship Type** | Reference |
| **Business Meaning** | Variance originates from either a cycle count or physical inventory count event — linking discrepancy to the count that discovered it. |
| **Multiplicity** | Count Variance **1** → Cycle Count **0..1** ; Count Variance **1** → Physical Inventory Count **0..1** |
| **Business Rules** | Exactly one count origin per variance. BR-019 — counter identity on originating count must differ from approver. |

---

### REL-093

| Field | Detail |
|-------|--------|
| **Source Entity** | Count Variance |
| **Target Entity** | Stock Position |
| **Relationship Type** | Reference |
| **Business Meaning** | Variance compares physical quantity to system quantity on a specific Stock Position. |
| **Multiplicity** | Count Variance **1** → Stock Position **1** |
| **Business Rules** | BR-022 — investigate root cause before adjustment applied to Stock Position. |

---

### REL-094

| Field | Detail |
|-------|--------|
| **Source Entity** | Count Variance |
| **Target Entity** | Stock Adjustment |
| **Relationship Type** | Derivation |
| **Business Meaning** | Approved count variance may produce a stock adjustment to correct the Stock Position — after investigation and independent approval. |
| **Multiplicity** | Count Variance **1** → Stock Adjustment **0..1** |
| **Business Rules** | BR-019, BR-021, BR-022 — investigation, independent approval, then adjustment. |

---

### REL-095

| Field | Detail |
|-------|--------|
| **Source Entity** | Count Variance |
| **Target Entity** | User Account *(approver)* |
| **Relationship Type** | Reference |
| **Business Meaning** | Variance approval records the independent approver who must differ from the original counter. |
| **Multiplicity** | Count Variance **0..1** → User Account *(approver)* **1** |
| **Business Rules** | BR-019 — approver must not be the counter who performed the originating count. |

---

### REL-096

| Field | Detail |
|-------|--------|
| **Source Entity** | Stock Adjustment |
| **Target Entity** | Count Variance |
| **Relationship Type** | Reference |
| **Business Meaning** | Adjustments originating from count activities reference the variance that triggered the correction — maintaining count-to-correction traceability. |
| **Multiplicity** | Stock Adjustment **0..1** → Count Variance **1** |
| **Business Rules** | BR-022 — adjustment from count requires prior investigation on linked variance. |

---

### REL-097

| Field | Detail |
|-------|--------|
| **Source Entity** | Stock Adjustment |
| **Target Entity** | Reason Code |
| **Relationship Type** | Reference |
| **Business Meaning** | Adjustment cites reason code explaining the correction category. |
| **Multiplicity** | Stock Adjustment **1** → Reason Code **1** |
| **Business Rules** | BR-020 — mandatory reason code on every adjustment. |

---

### REL-098

| Field | Detail |
|-------|--------|
| **Source Entity** | Stock Adjustment |
| **Target Entity** | User Account *(initiator and approver)* |
| **Relationship Type** | Reference |
| **Business Meaning** | Adjustment records initiating user and independent approver (when threshold requires) for accountability. |
| **Multiplicity** | Stock Adjustment **1** → User Account *(initiator)* **1** ; Stock Adjustment **0..1** → User Account *(approver)* **1** |
| **Business Rules** | BR-021 — approver must differ from initiator for material adjustments. |

---

### REL-099

| Field | Detail |
|-------|--------|
| **Source Entity** | Inventory Write-Off |
| **Target Entity** | Return Disposition |
| **Relationship Type** | Reference |
| **Business Meaning** | Write-off may originate from return disposition when returned goods are deemed non-resalable. |
| **Multiplicity** | Return Disposition **0..1** → Inventory Write-Off **1** |
| **Business Rules** | BR-026 — inspect before restock; damaged returns routed to write-off. BR-023 — authorization required. |

---

### REL-100

| Field | Detail |
|-------|--------|
| **Source Entity** | Inventory Write-Off |
| **Target Entity** | Reason Code |
| **Relationship Type** | Reference |
| **Business Meaning** | Write-off cites reason code (obsolescence, damage, loss) for shrinkage reporting. |
| **Multiplicity** | Inventory Write-Off **1** → Reason Code **1** |
| **Business Rules** | BR-020, BR-023 — reason code and documented evidence mandatory. |

---

### REL-101

| Field | Detail |
|-------|--------|
| **Source Entity** | Inventory Write-Off |
| **Target Entity** | User Account *(authorizer)* |
| **Relationship Type** | Authorization |
| **Business Meaning** | Write-off requires authorized approver distinct from initiator for high-value disposals. |
| **Multiplicity** | Inventory Write-Off **1** → User Account *(authorizer)* **1** |
| **Business Rules** | BR-023 — documented authorization by authorized person before value removal. |

---

### REL-102

| Field | Detail |
|-------|--------|
| **Source Entity** | Quarantine Hold |
| **Target Entity** | Return Disposition |
| **Relationship Type** | Derivation |
| **Business Meaning** | Return disposition may place returned goods into quarantine hold pending further quality investigation rather than immediate restock or write-off. |
| **Multiplicity** | Return Disposition **0..1** → Quarantine Hold **0..1** |
| **Business Rules** | BR-026 — inspect before restock. BR-013 — quarantined quantity excluded from ATP. |

---

### REL-103

| Field | Detail |
|-------|--------|
| **Source Entity** | Quarantine Hold |
| **Target Entity** | Stock Adjustment |
| **Relationship Type** | Derivation |
| **Business Meaning** | Release from quarantine or disposition to write-off may trigger stock adjustment or write-off on the held Stock Position quantity. |
| **Multiplicity** | Quarantine Hold **0..1** → Stock Adjustment **0..1** ; Quarantine Hold **0..1** → Inventory Write-Off **0..1** |
| **Business Rules** | BR-013 — hold release restores ATP only when quality/regulatory clearance confirmed. BR-030 — customs clearance required for bonded release. |

---

### REL-104

| Field | Detail |
|-------|--------|
| **Source Entity** | Return Disposition |
| **Target Entity** | Stock Position |
| **Relationship Type** | Modification |
| **Business Meaning** | Restock disposition increases on-hand and ATP on Stock Position at the receiving location for resalable returned goods. |
| **Multiplicity** | Return Disposition **0..1** → Stock Position **1** |
| **Business Rules** | BR-026 — restock only after condition assessment confirms resale quality. BR-013 — quarantine path excludes from ATP until cleared. |

---

## Domain 7: Returns Management

---

### REL-105

| Field | Detail |
|-------|--------|
| **Source Entity** | Return Authorization |
| **Target Entity** | Customer Order |
| **Relationship Type** | Verification |
| **Business Meaning** | RMA validates return request against original order — confirming products, quantities, and eligibility under return policy. |
| **Multiplicity** | Return Authorization **1** → Customer Order **1** |
| **Business Rules** | BR-025 — authorization required before warehouse acceptance; must link to original order. |

---

### REL-106

| Field | Detail |
|-------|--------|
| **Source Entity** | Return Authorization |
| **Target Entity** | Customer Return |
| **Relationship Type** | Authorization |
| **Business Meaning** | RMA gates physical return receipt — warehouse must not accept goods without valid authorization. |
| **Multiplicity** | Return Authorization **1** → Customer Return **0..1** |
| **Business Rules** | BR-025 — no receipt without valid RMA. RMA expiration date enforced. |

---

### REL-107

| Field | Detail |
|-------|--------|
| **Source Entity** | Return Authorization |
| **Target Entity** | Product |
| **Relationship Type** | Reference |
| **Business Meaning** | RMA specifies which products and quantities the customer is authorized to return. |
| **Multiplicity** | Return Authorization **1** → Product **1..*** |
| **Business Rules** | Returned products must match RMA authorized lines. |

---

### REL-108

| Field | Detail |
|-------|--------|
| **Source Entity** | Customer Return |
| **Target Entity** | Return Authorization |
| **Relationship Type** | Verification |
| **Business Meaning** | Physical return must match a valid RMA — verifying authorization before acceptance. |
| **Multiplicity** | Customer Return **1** → Return Authorization **1** |
| **Business Rules** | BR-025 — authorization required. BR-004 — verify quantity and product on receipt. |

---

### REL-109

| Field | Detail |
|-------|--------|
| **Source Entity** | Customer Return |
| **Target Entity** | Inventory Location |
| **Relationship Type** | Reference |
| **Business Meaning** | Returns are received at a designated warehouse location — same receiving infrastructure as inbound supplier goods. |
| **Multiplicity** | Customer Return **1** → Inventory Location **1** |
| **Business Rules** | BR-004 — verify before acceptance into inventory control. |

---

### REL-110

| Field | Detail |
|-------|--------|
| **Source Entity** | Customer Return |
| **Target Entity** | Return Disposition |
| **Relationship Type** | Composition |
| **Business Meaning** | Disposition decisions (restock, quarantine, write-off) are subordinate outcomes of the return receipt and inspection workflow. |
| **Multiplicity** | Customer Return **1** → Return Disposition **1..*** |
| **Business Rules** | BR-026 — inspection mandatory before disposition. One disposition per returned line. |

---

### REL-111

| Field | Detail |
|-------|--------|
| **Source Entity** | Customer Return |
| **Target Entity** | Goods Receipt |
| **Relationship Type** | Association |
| **Business Meaning** | Customer return receipt follows the same verification discipline as supplier goods receipt — parallel inbound workflow pattern. |
| **Multiplicity** | Customer Return **0..*** → Goods Receipt **0..*** *(conceptual parallel — return may use receipt workflow)* |
| **Business Rules** | BR-004 — verify before acceptance applies to return inbound same as supplier inbound. |

---

### REL-112

| Field | Detail |
|-------|--------|
| **Source Entity** | Return Disposition |
| **Target Entity** | Customer Return |
| **Relationship Type** | Reference |
| **Business Meaning** | Disposition applies to goods received on a specific customer return. |
| **Multiplicity** | Return Disposition **1** → Customer Return **1** |
| **Business Rules** | BR-026 — condition assessment drives disposition outcome. |

---

### REL-113

| Field | Detail |
|-------|--------|
| **Source Entity** | Return Disposition |
| **Target Entity** | Inventory Write-Off |
| **Relationship Type** | Derivation |
| **Business Meaning** | Disposition decision of "write-off" produces an inventory write-off for non-resalable returned goods. |
| **Multiplicity** | Return Disposition **0..1** → Inventory Write-Off **1** |
| **Business Rules** | BR-023 — write-off authorization required. BR-026 — damaged/defective returns not restocked. |

---

### REL-114

| Field | Detail |
|-------|--------|
| **Source Entity** | Return Disposition |
| **Target Entity** | Quarantine Hold |
| **Relationship Type** | Derivation |
| **Business Meaning** | Disposition decision of "quarantine" applies hold on returned quantity pending further investigation. |
| **Multiplicity** | Return Disposition **0..1** → Quarantine Hold **1** |
| **Business Rules** | BR-013 — quarantined returns excluded from sellable ATP. |

---

## Domain 8: Accountability & Oversight

---

### REL-115

| Field | Detail |
|-------|--------|
| **Source Entity** | Inventory Movement Record |
| **Target Entity** | Stock Position |
| **Relationship Type** | Association |
| **Business Meaning** | Every movement record documents a change to a specific Stock Position — forming the immutable history of quantity and status changes. |
| **Multiplicity** | Inventory Movement Record **0..*** → Stock Position **1** |
| **Business Rules** | BR-017 — lot on movement for traceable products. BR-020 — reason code on adjustment movements. All mutations must produce movement record. |

---

### REL-116

| Field | Detail |
|-------|--------|
| **Source Entity** | Inventory Movement Record |
| **Target Entity** | Goods Receipt *(and other source documents)* |
| **Relationship Type** | Reference |
| **Business Meaning** | Movement record references the originating business document (receipt, shipment, transfer, adjustment) that caused the stock change. |
| **Multiplicity** | Inventory Movement Record **1** → originating document **1** |
| **Business Rules** | Full traceability from movement back to business event. Originating document types: Goods Receipt, Shipment, Stock Transfer, Stock Adjustment, Inventory Write-Off, Put-Away, Customer Return. |

---

### REL-117

| Field | Detail |
|-------|--------|
| **Source Entity** | Inventory Movement Record |
| **Target Entity** | User Account |
| **Relationship Type** | Reference |
| **Business Meaning** | Movement records who performed the action for operational accountability. |
| **Multiplicity** | Inventory Movement Record **1** → User Account **1** |
| **Business Rules** | BO-19 — 100% audit trail coverage with user identity required. |

---

### REL-118

| Field | Detail |
|-------|--------|
| **Source Entity** | Audit Trail Record |
| **Target Entity** | Stock Adjustment *(and other governed entities)* |
| **Relationship Type** | Association |
| **Business Meaning** | Audit trail captures governance-grade before/after state for material changes to inventory entities — complementing movement records with approval context. |
| **Multiplicity** | Audit Trail Record **0..*** → governed entity **1** |
| **Business Rules** | BR-019, BR-021 — audit trail supports segregation-of-duties verification. Immutable after write. |

---

### REL-119

| Field | Detail |
|-------|--------|
| **Source Entity** | Audit Trail Record |
| **Target Entity** | User Account |
| **Relationship Type** | Reference |
| **Business Meaning** | Audit record captures user identity and role at time of action for compliance and fraud investigation. |
| **Multiplicity** | Audit Trail Record **1** → User Account **1** |
| **Business Rules** | BR-019, BR-020, BR-021 — user attribution mandatory on governed changes. |

---

### REL-120

| Field | Detail |
|-------|--------|
| **Source Entity** | Operational Alert |
| **Target Entity** | Stock Position |
| **Relationship Type** | Derivation |
| **Business Meaning** | Low-stock and out-of-stock alerts are derived when Stock Position ATP crosses Stock Policy thresholds. |
| **Multiplicity** | Operational Alert **0..*** → Stock Position **1** |
| **Business Rules** | BR-009 — alert at reorder level triggers same-day replenishment review. BR-032 — Class A alerts prioritized. |

---

### REL-121

| Field | Detail |
|-------|--------|
| **Source Entity** | Operational Alert |
| **Target Entity** | Transfer Request |
| **Relationship Type** | Derivation |
| **Business Meaning** | Transfer exception alerts signal pending approvals, dispatch delays, or receipt failures on inter-location transfers. |
| **Multiplicity** | Operational Alert **0..*** → Transfer Request **0..1** |
| **Business Rules** | Pending approval notifications route to Operations Director per BP-24. |

---

### REL-122

| Field | Detail |
|-------|--------|
| **Source Entity** | Operational Alert |
| **Target Entity** | Promotional Stock Allocation |
| **Relationship Type** | Derivation |
| **Business Meaning** | Campaign readiness alerts signal insufficient ring-fenced stock approaching launch deadline. |
| **Multiplicity** | Operational Alert **0..*** → Promotional Stock Allocation **0..1** |
| **Business Rules** | BR-029 — readiness confirmed before campaign commitment. BO-24 — 95% promotional launch readiness target. |

---

### REL-123

| Field | Detail |
|-------|--------|
| **Source Entity** | User Account |
| **Target Entity** | Role Assignment |
| **Relationship Type** | Composition |
| **Business Meaning** | Role assignments delegate permissions to a user. Assignments are subordinate to the user account and meaningless without it. |
| **Multiplicity** | User Account **1** → Role Assignment **1..*** |
| **Business Rules** | BR-019, BR-021 — conflicting roles blocked (counter + approver). Account must have at least one role to transact. |

---

### REL-124

| Field | Detail |
|-------|--------|
| **Source Entity** | Role Assignment |
| **Target Entity** | Inventory Location |
| **Relationship Type** | Reference |
| **Business Meaning** | Role assignment scopes user permissions to authorized locations — user may only operate within assigned location boundaries. |
| **Multiplicity** | Role Assignment **1** → Inventory Location **0..*** |
| **Business Rules** | Location-scoped access enforced on all operational transactions. Empty scope may mean network-wide for executive roles. |

---

### REL-125

| Field | Detail |
|-------|--------|
| **Source Entity** | User Account |
| **Target Entity** | Cycle Count |
| **Relationship Type** | Association |
| **Business Meaning** | User accounts are linked to cycle counts as counters or approvers — enforcing segregation of duties across the count-to-adjustment workflow. |
| **Multiplicity** | User Account **1** → Cycle Count **0..*** *(as counter)* ; User Account **1** → Count Variance **0..*** *(as approver)* |
| **Business Rules** | BR-019 — same user cannot count and approve same variance. |

---

### REL-126

| Field | Detail |
|-------|--------|
| **Source Entity** | User Account |
| **Target Entity** | Goods Receipt |
| **Relationship Type** | Association |
| **Business Meaning** | Receiving clerk user account attributed on goods receipt for inbound accountability. |
| **Multiplicity** | User Account **1** → Goods Receipt **0..*** |
| **Business Rules** | All inbound transactions require user attribution per BO-19 audit trail objective. |

---

### REL-127

| Field | Detail |
|-------|--------|
| **Source Entity** | Audit Trail Record |
| **Target Entity** | Inventory Movement Record |
| **Relationship Type** | Association |
| **Business Meaning** | Audit trail complements movement record with before/after state snapshots and approval chain — movement is operational history, audit is governance evidence. |
| **Multiplicity** | Audit Trail Record **0..1** → Inventory Movement Record **1** |
| **Business Rules** | Material changes require both movement record and audit trail per BO-19. |

---

### REL-128

| Field | Detail |
|-------|--------|
| **Source Entity** | Operational Alert |
| **Target Entity** | Expected Inbound Delivery |
| **Relationship Type** | Derivation |
| **Business Meaning** | Inbound delay alerts notify when expected delivery date passes without corresponding goods receipt. |
| **Multiplicity** | Operational Alert **0..*** → Expected Inbound Delivery **0..1** |
| **Business Rules** | Delay response informs replenishment planning (BP-23). |

---

## Domain 9: Financial Alignment

---

### REL-129

| Field | Detail |
|-------|--------|
| **Source Entity** | Inventory Valuation Snapshot |
| **Target Entity** | Stock Position |
| **Relationship Type** | Derivation |
| **Business Meaning** | Valuation snapshot summarizes Stock Position quantities and values at a point in time for finance reconciliation. |
| **Multiplicity** | Inventory Valuation Snapshot **1** → Stock Position **0..*** |
| **Business Rules** | BR-031 — consignment stock excluded from owned valuation. Quarantined and in-transit stock excluded per policy. |

---

### REL-130

| Field | Detail |
|-------|--------|
| **Source Entity** | Inventory Valuation Snapshot |
| **Target Entity** | Product |
| **Relationship Type** | Reference |
| **Business Meaning** | Valuation lines reference products with unit cost and extended value for financial reporting by SKU. |
| **Multiplicity** | Inventory Valuation Snapshot **1** → Product **0..*** |
| **Business Rules** | BO-18 — valuation variance ≤2% vs. general ledger target. |

---

### REL-131

| Field | Detail |
|-------|--------|
| **Source Entity** | Inventory Valuation Snapshot |
| **Target Entity** | Inventory Location |
| **Relationship Type** | Reference |
| **Business Meaning** | Snapshot may scope to specific locations or network-wide for regional and consolidated financial reporting. |
| **Multiplicity** | Inventory Valuation Snapshot **1** → Inventory Location **0..*** |
| **Business Rules** | Month-end close alignment per BP-30. |

---

### REL-132

| Field | Detail |
|-------|--------|
| **Source Entity** | Inventory Valuation Snapshot |
| **Target Entity** | Supplier Invoice |
| **Relationship Type** | Reference |
| **Business Meaning** | Valuation uses invoice-matched costs from supplier invoices for recently received owned inventory. |
| **Multiplicity** | Inventory Valuation Snapshot **0..*** → Supplier Invoice **0..*** |
| **Business Rules** | BR-008 — three-way matched costs are authoritative for received inventory valuation. |

---

### REL-133

| Field | Detail |
|-------|--------|
| **Source Entity** | Inventory Valuation Snapshot |
| **Target Entity** | Inventory Write-Off |
| **Relationship Type** | Reference |
| **Business Meaning** | Period valuation reflects write-offs that permanently removed value during the snapshot period. |
| **Multiplicity** | Inventory Valuation Snapshot **0..*** → Inventory Write-Off **0..*** |
| **Business Rules** | BR-023 — authorized write-offs reduce period-end inventory value. |

---

### REL-134

| Field | Detail |
|-------|--------|
| **Source Entity** | Lot/Batch |
| **Target Entity** | Supplier |
| **Relationship Type** | Reference |
| **Business Meaning** | Lot/batch may record supplier origin for traceability back to source in quality investigation or recall. |
| **Multiplicity** | Lot/Batch **0..1** → Supplier **1** |
| **Business Rules** | BR-017 — lot captured at receipt with supplier context for traceable products. |

---

## Entity Relationship Matrix

Rows = Source Entity, Columns = Target Entity. Cell shows Relationship ID(s) if related.

| Source ↓ / Target → | Product | Location | Stock Pos. | PO | GR | Cust. Order | Stock Adj. |
|---------------------|---------|----------|------------|----|----|-------------|------------|
| **Product** | — | — | REL-001 | REL-041 | — | — | — |
| **Stock Position** | REL-019 | REL-020 | — | — | REL-029 | REL-059 | REL-031 |
| **Purchase Order** | REL-041 | REL-040 | — | — | REL-043 | — | — |
| **Goods Receipt** | — | REL-049 | REL-029 | REL-047 | — | — | — |
| **Customer Order** | — | — | REL-059 | — | — | — | — |
| **Count Variance** | — | — | REL-093 | — | — | — | REL-094 |
| **Supplier Invoice** | — | — | — | REL-055 | REL-056 | — | — |

*Full relationship detail in REL-001 through REL-134 above.*

---

## Relationship Diagram — Core Inventory Flow

```
                    ┌─────────────┐
                    │   Product   │
                    └──────┬──────┘
                           │ REL-001, REL-002, REL-003
              ┌────────────┼────────────┐
              ▼            ▼            ▼
       ┌────────────┐ ┌─────────┐ ┌─────────────┐
       │Stock Policy│ │Stock    │ │ Lot/Batch   │
       └─────┬──────┘ │Position │ └──────┬──────┘
             │        └────┬────┘        │
    REL-010  │    ┌────────┼────────┐   │
             ▼    │        │        │   │
       ┌──────────┐│        │        │   │
       │Operational│       │        │   │
       │Alert     ││        │        │   │
       └──────────┘│        │        │   │
                   │        │        │   │
    ┌──────────────┘        │        └───────────────┐
    │ REL-004               │                        │
    ▼                       │ REL-024                │ REL-029
┌───────────────┐           │                        │
│Inventory      │           ▼                        ▼
│Location       │◄── REL-020 ── Stock Position ◄── Goods Receipt
└───┬───────────┘           ▲                        │
    │                       │ REL-030                │ REL-051
    │ REL-007               │                        ▼
    ▼                       │                   Put-Away
┌───────────────┐           │
│Physical       │     ┌─────┴──────┐
│Inventory Count│     │ Shipment   │◄── Fulfillment Execution
└───────────────┘     └────────────┘         ▲
                          ▲                  │ REL-070
                          │ REL-063          │
                    ┌─────┴──────────────────┴─────┐
                    │       Customer Order          │
                    │  ┌──────────┐  ┌───────────┐  │
                    │  │Reservation│  │ Backorder │  │
                    │  └──────────┘  └───────────┘  │
                    └──────────────────────────────┘
```

---

## Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Domain Expert | | | |
| DDD Solution Architect | | | |
| Senior Business Analyst | | | |
| Inventory Controller | | | |

---

*End of Domain Entity Relationships*

*Document ID: SRS-DM-004 | Version 1.0 | July 5, 2026*
