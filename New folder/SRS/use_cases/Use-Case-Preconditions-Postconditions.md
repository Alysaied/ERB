# Use Case Preconditions and Postconditions
## Inventory Management System

---

## Document Information

| Attribute | Detail |
|-----------|--------|
| **Document ID** | SRS-UC-005 |
| **Document Title** | Use Case Preconditions and Postconditions — Inventory Management System |
| **Version** | 1.0 |
| **Status** | Draft |
| **Document Owner** | Business Analyst |
| **Source Documents** | SRS-UC-001 (Use Case Catalog), SRS-UC-002 (Main Flows), SRS-BR-001 (Business Rule Catalog) |
| **Date** | July 5, 2026 |
| **Scope** | Successful completion scenario — conditions for main flow outcome |

### Purpose

This document defines preconditions and postconditions for each of the 48 use cases in the Inventory Management System. Preconditions describe what must be true before a use case can execute successfully. Postconditions describe what will be true after successful completion. Business rule references use the identifiers defined in SRS-BR-001 (BR-001 through BR-032).

### Condition Legend

| Symbol | Meaning |
|--------|---------|
| **[BR-xxx]** | Condition directly enforced by or derived from business rule BR-xxx |
| **(FR-xxx)** | Condition supported by functional requirement (referenced when no direct business rule applies) |

---

## Domain 1: Master Data & Governance

### UC-001 — Manage Product Master Data

**Primary Actor:** Inventory Controller

#### Preconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| P1 | Primary actor is authenticated with product master management permission (PG-01). | (FR-081) |
| P2 | Product category and unit of measure reference data are configured in the system. | — |
| P3 | For product updates, the target SKU exists as an active or inactive record in the product catalog. | — |
| P4 | For new products, the proposed SKU and identifier are not already assigned to another active product. | — |

#### Postconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| PO1 | Product master record exists with unique SKU, required attributes, and current lifecycle status. | — |
| PO2 | Product identifier (barcode) is registered and available for operational lookup. | (FR-003) |
| PO3 | If status is discontinued, the product is blocked from new purchase orders and replenishment requisitions. | [BR-027] |
| PO4 | Product creation or update is recorded in the audit trail with user, timestamp, and changed attributes. | (FR-086) |

---

### UC-002 — Configure Inventory Locations

**Primary Actor:** Inventory Controller

#### Preconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| P1 | Primary actor is authenticated with location management permission (PG-02). | (FR-081) |
| P2 | For new locations, parent location (if applicable) exists and is active in the location hierarchy. | — |
| P3 | For go-live activation, opening stock balances are verified where location cutover policy requires them. | — |
| P4 | For location closure, a stock disposition plan is defined if on-hand inventory remains. | (FR-007) |

#### Postconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| PO1 | Location record exists with valid hierarchy, type, and operational status (active or planned closure). | — |
| PO2 | For activated locations, stock can be assigned, received, and transacted against the location. | — |
| PO3 | For go-live locations, opening balances are recorded as initial on-hand quantities. | (FR-010) |
| PO4 | Location configuration change is recorded in the audit trail. | (FR-086) |

---

### UC-003 — Define Stock Policies and Thresholds

**Primary Actor:** Inventory Controller

#### Preconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| P1 | Primary actor is authenticated with stock policy configuration permission (PG-04, PG-13). | (FR-081) |
| P2 | Target product or product group exists and is in active status. | — |
| P3 | Target location scope (product-location or network default) is defined and active. | — |
| P4 | Proposed reorder level is not below minimum threshold or safety stock buffer without authorized exception. | [BR-010] |

#### Postconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| PO1 | Reorder level, minimum threshold, and safety stock policy are saved for the defined scope. | [BR-009] |
| PO2 | Low-stock and out-of-stock alert monitoring applies the new thresholds. | [BR-009] |
| PO3 | Safety stock buffer is protected from routine consumption without authorized override. | [BR-010] |
| PO4 | Policy effective date and scope are available for replenishment and monitoring functions. | — |

---

### UC-004 — Classify Products by ABC Priority

**Primary Actor:** Inventory Controller

#### Preconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| P1 | Primary actor is authenticated with ABC classification permission (PG-01). | (FR-009) |
| P2 | Target products exist in active status in the product catalog. | — |
| P3 | Product performance data (velocity, revenue, or criticality) is available for classification review. | — |

#### Postconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| PO1 | Each classified product has an assigned ABC class (A, B, or C) with effective date. | [BR-032] |
| PO2 | Class A products are scheduled for highest cycle count frequency and monitoring intensity. | [BR-032] |
| PO3 | Low-stock alert prioritization reflects ABC classification. | [BR-032] |
| PO4 | Classification change is recorded in the audit trail. | (FR-086) |

---

### UC-005 — Maintain Governance Policies and Reason Codes

**Primary Actor:** Inventory Controller

#### Preconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| P1 | Primary actor is authenticated with governance policy administration permission (PG-13). | (FR-012) |
| P2 | For reason code deactivation, no active governance policy or pending transaction mandates the code. | [BR-020] |
| P3 | Proposed approval thresholds do not create segregation of duties conflicts. | (FR-084) |

#### Postconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| PO1 | Active reason code catalog is available for adjustments, discrepancies, and exceptions. | [BR-020] |
| PO2 | Governance policies (approval thresholds, count rules, override rules) are active for applicable transaction types. | [BR-021] |
| PO3 | New or updated policies apply to subsequent inventory transactions. | (FR-012) |
| PO4 | Policy and reason code changes are recorded in the audit trail. | (FR-086) |

---

## Domain 2: Inbound & Receiving

### UC-006 — Place and Manage Purchase Orders

**Primary Actor:** Buyer

#### Preconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| P1 | Primary actor is authenticated with purchase order creation permission (PG-06). | (FR-081) |
| P2 | Supplier is registered and authorized for procurement. | — |
| P3 | All purchase order lines reference active, non-discontinued products. | [BR-027] |
| P4 | Delivery location is active and configured for receiving. | — |

#### Postconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| PO1 | Approved purchase order exists as authorized commercial commitment to supplier. | [BR-007] |
| PO2 | Expected inbound supply is visible for replenishment and receiving planning. | (FR-055) |
| PO3 | Purchase order is available for goods receipt matching and three-way match processing. | [BR-007], [BR-008] |
| PO4 | Purchase order creation, approval, amendment, or cancellation is recorded in the audit trail. | (FR-086) |

---

### UC-007 — Plan Expected Inbound Deliveries

**Primary Actor:** Buyer

#### Preconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| P1 | Primary actor is authenticated with inbound planning permission (PG-06). | (FR-014) |
| P2 | Target purchase order is approved and in open status. | [BR-007] |
| P3 | Supplier delivery schedule information is available from supplier communication. | — |

#### Postconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| PO1 | Expected delivery date and shipment details are recorded against the purchase order. | — |
| PO2 | Receiving location has visibility of planned inbound arrival. | (FR-055) |
| PO3 | Replenishment and alert functions reflect updated inbound supply timing. | [BR-009] |
| PO4 | Delivery schedule changes are recorded in transaction history. | (FR-029) |

---

### UC-008 — Receive and Verify Supplier Goods

**Primary Actor:** Receiving Clerk

#### Preconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| P1 | Primary actor is authenticated with goods receipt permission (PG-07) for the receiving location. | (FR-082) |
| P2 | Valid purchase order reference or approved ad-hoc receipt authorization exists for the shipment. | [BR-007] |
| P3 | Receiving location is active and not under physical inventory freeze. | [BR-024] |
| P4 | Supplier shipment is physically present at the receiving dock with documentation. | [BR-004] |

#### Postconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| PO1 | Verified receipt is recorded with quantity, product identity, and condition confirmed against authorization. | [BR-004] |
| PO2 | Lot or batch identity is captured for traceable products. | [BR-017] |
| PO3 | Shelf-life products meeting MRSL are accepted; non-compliant product is routed to discrepancy workflow. | [BR-016] |
| PO4 | Received stock is staged for put-away and is not yet included in available-to-promise. | [BR-005] |
| PO5 | Receipt transaction is recorded in movement history and audit trail. | (FR-029), (FR-086) |

---

### UC-009 — Document and Resolve Receipt Discrepancies

**Primary Actor:** Receiving Clerk

#### Preconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| P1 | Primary actor is authenticated with receipt and discrepancy permission (PG-07). | (FR-081) |
| P2 | Goods receipt verification is in progress or complete with identified variance. | [BR-006] |
| P3 | Mandatory reason codes for discrepancy types are active in the system. | [BR-020] |
| P4 | Warehouse Manager or authorized approver is available for beyond-tolerance resolution. | (SOD-007) |

#### Postconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| PO1 | Discrepancy is documented with type, variance quantity, reason code, and timestamp. | [BR-006] |
| PO2 | Accepted quantities are recorded; unresolved variance is held for supplier or finance resolution. | [BR-006] |
| PO3 | Discrepancy resolution supports three-way match and supplier accountability. | [BR-008] |
| PO4 | Discrepancy documentation is available in receipt record and audit trail. | (FR-086) |

---

### UC-010 — Perform Stock Put-Away

**Primary Actor:** Warehouse Staff

#### Preconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| P1 | Primary actor is authenticated with put-away permission (PG-07) for the receiving location. | (FR-082) |
| P2 | Goods receipt verification is complete for the stock to be put away. | [BR-004], [BR-005] |
| P3 | Destination storage location is authorized for the product category. | — |
| P4 | Bonded inventory, if applicable, has customs clearance before sellable put-away. | [BR-030] |

#### Postconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| PO1 | Stock is recorded at designated storage location with confirmed quantity. | [BR-005] |
| PO2 | On-hand quantity is updated at the storage location. | — |
| PO3 | Available-to-promise is increased by the put-away quantity (sellable stock). | [BR-005] |
| PO4 | Put-away is recorded in movement history with user, timestamp, and location. | (FR-029) |
| PO5 | FIFO/FEFO placement follows rotation policy for subsequent picking. | [BR-014], [BR-015] |

---

### UC-011 — Receive Return and Non-PO Inbound Stock

**Primary Actor:** Receiving Clerk

#### Preconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| P1 | Primary actor is authenticated with non-PO receipt permission (PG-07, PG-09). | (FR-019) |
| P2 | For customer returns, valid return authorization exists linked to original order. | [BR-025] |
| P3 | For ad-hoc receipts, pre-approved authorization reference exists. | [BR-007] |
| P4 | Receiving location is active and not under physical inventory freeze. | [BR-024] |

#### Postconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| PO1 | Non-PO inbound receipt is recorded against authorization reference. | [BR-025] |
| PO2 | Stock is staged for inspection, put-away, or disposition per receipt type — not immediately sellable unless policy allows. | [BR-026] |
| PO3 | Receipt is recorded in movement history and audit trail. | (FR-029), (FR-086) |
| PO4 | Return authorization status is updated to received pending inspection. | [BR-025] |

---

## Domain 3: Inventory Visibility & Status

### UC-012 — Monitor Inventory Status

**Primary Actor:** Inventory Controller

#### Preconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| P1 | Primary actor is authenticated with inventory visibility permission (PG-03) for authorized locations. | (FR-082) |
| P2 | Product master and location master data exist for monitored scope. | — |
| P3 | Stock policies and thresholds are defined for products under monitoring. | [BR-009] |

#### Postconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| PO1 | Current on-hand, reserved, ATP, and status indicators are displayed for monitored scope. | [BR-001] |
| PO2 | Low-stock and out-of-stock conditions are visible against defined thresholds. | [BR-009] |
| PO3 | Quarantined stock is displayed separately and excluded from sellable ATP view. | [BR-013] |
| PO4 | Monitoring session timestamp is recorded for accountability. | (FR-083) |

---

### UC-013 — Inquire Inventory Availability

**Primary Actor:** Sales Representative

#### Preconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| P1 | Primary actor is authenticated with ATP inquiry permission (PG-03, PG-10). | (FR-081) |
| P2 | Target product exists in the product catalog. | — |
| P3 | Inventory records exist for at least one fulfillment location (ATP may be zero). | — |

#### Postconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| PO1 | On-hand, reserved, and ATP quantities are displayed per location and network-wide as authorized. | [BR-001] |
| PO2 | Stock status indicator (in stock, low stock, out of stock) is presented. | — |
| PO3 | Quarantined and ring-fenced promotional stock are excluded from quotable ATP. | [BR-013], [BR-029] |
| PO4 | Expected inbound supply is visible where applicable for customer commitment discussion. | (FR-028) |
| PO5 | No inventory reservation or commitment is created by inquiry alone. | [BR-001] |

---

## Domain 4: Inventory Control & Accuracy

### UC-014 — Perform Cycle Count

**Primary Actor:** Warehouse Staff

#### Preconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| P1 | Primary actor is authenticated with cycle count permission (PG-04) for the assigned location. | (FR-082) |
| P2 | Cycle count is scheduled and assigned to the counter for product-location combination. | [BR-018] |
| P3 | Counter is not shown system expected quantity (blind count enforced). | [BR-018] |
| P4 | Target location is not under full physical inventory freeze unless count is part of freeze program. | [BR-024] |

#### Postconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| PO1 | Physical count result is recorded with counter identity and timestamp. | [BR-018] |
| PO2 | System compares count to recorded quantity and flags variance if present. | — |
| PO3 | Count submission status is available (verified match or variance pending review). | [BR-022] |
| PO4 | Count transaction is recorded in audit trail. | (FR-086) |

---

### UC-015 — Conduct Full Physical Inventory Count

**Primary Actor:** Inventory Controller

#### Preconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| P1 | Primary actor is authenticated with physical count initiation permission (PG-04). | (FR-032) |
| P2 | Target location is active and count schedule is approved. | — |
| P3 | Count teams are assigned and available for wall-to-wall count execution. | — |
| P4 | Stakeholders are notified of impending inventory freeze at the location. | [BR-024] |

#### Postconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| PO1 | Physical inventory freeze was active during count execution at the location. | [BR-024] |
| PO2 | Complete count snapshot exists for all assigned zones and products. | — |
| PO3 | Inventory freeze is released upon count session close. | [BR-024] |
| PO4 | Variance report is generated for investigation and approval workflow. | [BR-022] |
| PO5 | Count session close is recorded in audit trail. | (FR-086) |

---

### UC-016 — Investigate and Approve Count Variances

**Primary Actor:** Warehouse Manager

#### Preconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| P1 | Primary actor is authenticated with variance investigation and approval permission (PG-04). | (FR-034) |
| P2 | Count variance record exists from cycle count or physical count. | [BR-022] |
| P3 | Approver is not the same person who performed the count. | [BR-019] |
| P4 | Investigation notes capability is available before approval. | [BR-022] |

#### Postconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| PO1 | Variance investigation findings are documented with investigator identity and timestamp. | [BR-022] |
| PO2 | Variance is approved or rejected by independent authorized approver. | [BR-019] |
| PO3 | Approved variance is queued for stock adjustment processing. | [BR-022] |
| PO4 | Approval decision is recorded in audit trail with approver identity. | [BR-021], (FR-086) |

---

### UC-017 — Process Stock Adjustments

**Primary Actor:** Warehouse Manager

#### Preconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| P1 | Primary actor is authenticated with stock adjustment permission (PG-04) for the location. | (FR-082) |
| P2 | Product exists at the target location with known current on-hand quantity. | — |
| P3 | Mandatory reason code is selected for the adjustment. | [BR-020] |
| P4 | For decrease adjustments, quantity does not exceed available on-hand (excluding already reserved). | — |
| P5 | Independent approver is available if adjustment exceeds threshold. | [BR-021] |

#### Postconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| PO1 | On-hand and ATP quantities reflect the approved adjustment. | — |
| PO2 | Adjustment is recorded with reason code, user, timestamp, and before/after quantities. | [BR-020] |
| PO3 | Material adjustments have independent approval recorded where threshold required. | [BR-021] |
| PO4 | Adjustment appears in movement history and audit trail. | (FR-029), (FR-086) |
| PO5 | Safety stock floor is not breached without documented authorized override. | [BR-010] |

---

### UC-018 — Authorize and Process Inventory Write-Offs

**Primary Actor:** Operations Director

#### Preconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| P1 | Primary actor is authenticated with write-off authorization permission (PG-04). | (FR-036) |
| P2 | Write-off request exists with product, quantity, location, and reason. | [BR-023] |
| P3 | Supporting documentation and evidence are attached to the write-off request. | [BR-023] |
| P4 | Write-off quantity does not exceed verified on-hand at location. | — |
| P5 | Finance acknowledgment is available where financial policy requires it. | [BR-023] |

#### Postconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| PO1 | Written-off quantity is removed from on-hand and ATP. | [BR-023] |
| PO2 | Write-off is recorded with reason code, authorizer, and supporting documentation reference. | [BR-020], [BR-023] |
| PO3 | Inventory valuation reflects reduced quantity for finance reconciliation. | (FR-075) |
| PO4 | Write-off transaction is recorded in movement history and audit trail. | (FR-029), (FR-086) |

---

### UC-019 — Manage Quarantine and Hold Stock

**Primary Actor:** Warehouse Manager

#### Preconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| P1 | Primary actor is authenticated with quarantine management permission (PG-04). | (FR-038) |
| P2 | Target stock exists as on-hand at the location. | — |
| P3 | Hold reason (quality, investigation, recall, bonded, customs) is defined. | [BR-013], [BR-030] |
| P4 | For release, quality review or customs clearance is documented where applicable. | [BR-030] |

#### Postconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| PO1 | Quarantined quantity is excluded from available-to-promise. | [BR-013] |
| PO2 | On-hand reflects total physical stock; sellable ATP excludes quarantined portion. | [BR-013] |
| PO3 | Hold reason, date, and responsible party are recorded. | — |
| PO4 | For release, stock is restored to sellable ATP with release authorization recorded. | [BR-013], [BR-030] |
| PO5 | Quarantine placement or release is recorded in movement history and audit trail. | (FR-029), (FR-086) |

---

### UC-020 — Analyze Shrinkage, Loss, and Obsolete Stock

**Primary Actor:** Inventory Controller

#### Preconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| P1 | Primary actor is authenticated with reporting and analysis permission (PG-11). | (FR-039) |
| P2 | Adjustment and write-off history with reason codes exists for the analysis period. | [BR-020] |
| P3 | Product movement and aging data is available for obsolescence analysis. | (FR-040) |

#### Postconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| PO1 | Shrinkage trends by reason code, location, and period are available for review. | [BR-020] |
| PO2 | Slow-moving and obsolete product candidates are identified with aging metrics. | (FR-040) |
| PO3 | Recommended disposition actions are documented where analysis conclusions are recorded. | — |
| PO4 | Analysis report is exportable for operations and finance stakeholders. | (FR-039) |

---

## Domain 5: Order Fulfillment

### UC-021 — Confirm Order Availability

**Primary Actor:** Sales Representative

#### Preconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| P1 | Primary actor is authenticated with availability confirmation permission (PG-10). | (FR-041) |
| P2 | Customer order exists with defined product lines and quantities. | — |
| P3 | Product master and inventory records exist for all order lines. | — |
| P4 | Fulfillment location(s) are identified or default fulfillment rules apply. | — |

#### Postconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| PO1 | Availability check result is recorded per order line against ATP (not total on-hand). | [BR-001] |
| PO2 | Ring-fenced promotional stock is excluded from quotable ATP for non-promotional orders. | [BR-029] |
| PO3 | Order availability status indicates lines cleared, partial, or unavailable for commitment. | [BR-001] |
| PO4 | No reservation is created until separate reservation use case is executed. | [BR-002] |
| PO5 | Availability check timestamp and result are recorded for audit. | (FR-083) |

---

### UC-022 — Reserve Inventory for Confirmed Orders

**Primary Actor:** Customer Service Representative

#### Preconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| P1 | Primary actor is authenticated with reservation permission (PG-08). | (FR-042) |
| P2 | Customer order is confirmed for fulfillment. | [BR-002] |
| P3 | Availability confirmation is complete or current ATP is sufficient at fulfillment location. | [BR-001] |
| P4 | ATP at fulfillment location covers reservation quantity (or partial per customer agreement). | [BR-002] |
| P5 | Promotional ring-fence rules are satisfied if consuming campaign stock. | [BR-029] |

#### Postconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| PO1 | Reserved quantity is committed against on-hand at fulfillment location. | [BR-002] |
| PO2 | ATP is reduced by reserved quantity. | [BR-001], [BR-002] |
| PO3 | Order is released to warehouse fulfillment queue with reservation reference per line. | — |
| PO4 | Reservation is recorded in movement history with user, timestamp, and order reference. | (FR-029) |
| PO5 | Safety stock is not consumed below buffer without authorized override. | [BR-010] |

---

### UC-023 — Release Inventory Reservations

**Primary Actor:** Customer Service Representative

#### Preconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| P1 | Primary actor is authenticated with reservation management permission (PG-08). | (FR-043) |
| P2 | Active reservation exists for the order or order line. | [BR-002] |
| P3 | Reserved lines are not already picked, packed, or shipped. | [BR-003] |
| P4 | Release reason is available where business policy requires it. | — |

#### Postconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| PO1 | Reservation hold is removed from specified order lines. | [BR-002] |
| PO2 | Released quantity is restored to available-to-promise. | [BR-001] |
| PO3 | Order status reflects released reservation. | — |
| PO4 | Release is recorded in transaction history with reason, user, and timestamp. | (FR-029), (FR-083) |

---

### UC-024 — Pick, Pack, and Ship Orders

**Primary Actor:** Warehouse Picker / Packer

#### Preconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| P1 | Primary actor is authenticated with pick, pack, and ship permission (PG-08) for the fulfillment location. | (FR-082) |
| P2 | Order has active reservation at the fulfillment location. | [BR-002] |
| P3 | Reserved stock is in sellable status (not quarantined). | [BR-013] |
| P4 | Pick list and storage locations are available for order lines. | — |

#### Postconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| PO1 | All shipped lines have pick verification recorded before shipment confirmation. | [BR-003] |
| PO2 | On-hand is deducted by shipped quantity; reservation is cleared. | [BR-003] |
| PO3 | Lot or batch attribution is recorded for traceable products on shipment. | [BR-017] |
| PO4 | FIFO/FEFO rotation is applied in pick execution. | [BR-014], [BR-015] |
| PO5 | Order status is updated to shipped with shipment date and carrier reference. | — |
| PO6 | Shipment is recorded in movement history and audit trail. | (FR-029), (FR-086) |

---

### UC-025 — Handle Partial Fulfillment and Backorders

**Primary Actor:** Customer Service Representative

#### Preconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| P1 | Primary actor is authenticated with partial fulfillment and backorder permission (PG-08, PG-10). | (FR-045) |
| P2 | Order line has insufficient ATP for full quantity. | [BR-001] |
| P3 | Partial ATP is available for immediate fulfillment or customer accepts full backorder. | — |
| P4 | For backorder, customer acknowledgment mechanism is available. | [BR-028] |

#### Postconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| PO1 | Available quantity is reserved for immediate fulfillment. | [BR-002] |
| PO2 | Backorder record exists with customer acknowledgment for remaining quantity. | [BR-028] |
| PO3 | Order reflects split status: pick-ready lines and backordered lines. | — |
| PO4 | Backorder is queued with replenishment priority where assigned. | (FR-046) |
| PO5 | Partial fulfillment and backorder decisions are recorded in audit trail. | (FR-086) |

---

### UC-026 — Handle Outbound Fulfillment Exceptions

**Primary Actor:** Warehouse Manager

#### Preconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| P1 | Primary actor is authenticated with fulfillment exception management permission (PG-08). | (FR-047) |
| P2 | Outbound exception exists (pick failure, quantity mismatch, damage). | — |
| P3 | Order has active reservation or is in pick/pack workflow. | [BR-002] |
| P4 | Authorized substitute products are defined if substitution is a resolution option. | (FR-050) |

#### Postconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| PO1 | Exception resolution is documented with manager authorization and reason. | — |
| PO2 | Order is returned to fulfillment flow, routed to substitution, partial ship, or quarantine per resolution. | [BR-003], [BR-013] |
| PO3 | Inventory and reservation states are adjusted to reflect resolution. | [BR-001] |
| PO4 | Exception and resolution are recorded in audit trail. | (FR-086) |

---

### UC-027 — View Order Fulfillment Status

**Primary Actor:** Customer Service Representative

#### Preconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| P1 | Primary actor is authenticated with order status visibility permission (PG-08, PG-10). | (FR-049) |
| P2 | Target order exists in the system. | — |

#### Postconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| PO1 | Current order fulfillment status is displayed (reserved, picking, packed, shipped, backordered). | — |
| PO2 | Line-level quantity, location, and status are visible. | — |
| PO3 | Shipment and carrier information is displayed for shipped lines. | — |
| PO4 | No inventory or order state is modified by status inquiry. | — |

---

## Domain 6: Replenishment & Inbound Supply

### UC-028 — Review Low-Stock and Out-of-Stock Alerts

**Primary Actor:** Purchasing Manager

#### Preconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| P1 | Primary actor is authenticated with alert review permission (PG-06, PG-11). | (FR-052) |
| P2 | Stock policies and thresholds are defined for alerted products. | [BR-009] |
| P3 | Active low-stock or out-of-stock alert exists for product-location combination. | [BR-009] |
| P4 | ABC classification is assigned for priority sorting where classification is in use. | [BR-032] |

#### Postconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| PO1 | Alert is acknowledged with user and timestamp. | (FR-052) |
| PO2 | Follow-up action is assigned (purchase, transfer, or deferral with reason). | [BR-009] |
| PO3 | Alert queue reflects updated acknowledgment status. | — |
| PO4 | Class A alert acknowledgment is recorded within monitoring SLA where defined. | [BR-032] |

---

### UC-029 — Plan Replenishment and Create Purchase Requisitions

**Primary Actor:** Buyer

#### Preconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| P1 | Primary actor is authenticated with requisition creation permission (PG-06). | (FR-054) |
| P2 | Replenishment need is identified from acknowledged alert or planning cycle. | [BR-009] |
| P3 | Network availability check is complete; transfer alternative evaluated. | [BR-011] |
| P4 | Target product is active and not discontinued. | [BR-027] |
| P5 | Safety stock rules are considered in requisition quantity. | [BR-010] |

#### Postconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| PO1 | Purchase requisition exists with product, quantity, required date, and delivery location. | — |
| PO2 | Requisition is approved and available for purchase order creation. | — |
| PO3 | Network check outcome is documented (purchase proceeded or transfer override recorded). | [BR-011] |
| PO4 | Requisition is recorded in audit trail. | (FR-086) |

---

### UC-030 — Track Inbound Supply Status

**Primary Actor:** Buyer

#### Preconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| P1 | Primary actor is authenticated with inbound supply tracking permission (PG-06). | (FR-055) |
| P2 | Open purchase order(s) exist with expected delivery information. | [BR-007] |

#### Postconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| PO1 | Inbound supply status reflects current ordered, received, and outstanding quantities. | (FR-055) |
| PO2 | Expected delivery dates are current based on latest supplier communication. | — |
| PO3 | Replenishment and alert functions have access to updated inbound supply position. | [BR-009] |
| PO4 | Status updates are recorded in transaction history. | (FR-029) |

---

## Domain 7: Network Balance & Transfers

### UC-031 — Request Inter-Location Stock Transfer

**Primary Actor:** Regional / Store Manager

#### Preconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| P1 | Primary actor is authenticated with transfer request permission (PG-05) for destination location. | (FR-058) |
| P2 | Source and destination locations are active. | — |
| P3 | Source location has sufficient ATP above minimum threshold for requested quantity. | [BR-012] |
| P4 | Product exists at source location with available (non-quarantined) stock. | [BR-013] |
| P5 | Network availability check supports transfer over new purchase where applicable. | [BR-011] |

#### Postconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| PO1 | Transfer request exists with pending approval status. | — |
| PO2 | Source and destination impact preview is recorded. | [BR-012] |
| PO3 | Approver is notified of pending transfer request. | (FR-077) |
| PO4 | Transfer request is recorded in audit trail. | (FR-086) |

---

### UC-032 — Approve or Reject Transfer Requests

**Primary Actor:** Operations Director

#### Preconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| P1 | Primary actor is authenticated with transfer approval permission (PG-05). | (FR-059) |
| P2 | Pending transfer request exists. | — |
| P3 | Approver is not the same person who submitted the transfer request. | (SOD-006) |
| P4 | Source location ATP and minimum threshold impact can be evaluated. | [BR-012] |

#### Postconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| PO1 | Transfer request status is approved or rejected with documented decision. | — |
| PO2 | For approval, source and destination locations are notified. | (FR-077) |
| PO3 | Approved transfer is available for execution at source location. | [BR-012] |
| PO4 | Approval decision is recorded with approver identity and timestamp. | (FR-086) |

---

### UC-033 — Execute and Record Inter-Location Transfer

**Primary Actor:** Warehouse Staff

#### Preconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| P1 | Primary actor is authenticated with transfer execution permission (PG-05) at source and destination. | (FR-060) |
| P2 | Transfer request is approved. | — |
| P3 | Source location has approved quantity available for dispatch. | [BR-012] |
| P4 | Source location is not under physical inventory freeze. | [BR-024] |
| P5 | Lot or batch capture is required for traceable products. | [BR-017] |

#### Postconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| PO1 | Source on-hand is reduced by dispatched quantity. | — |
| PO2 | In-transit status exists from dispatch until destination receipt confirmation. | (FR-061) |
| PO3 | Destination on-hand is increased upon receipt confirmation. | — |
| PO4 | Transfer is complete with full movement history at source, in-transit, and destination. | (FR-029) |
| PO5 | Lot or batch attribution is maintained through transfer for traceable products. | [BR-017] |
| PO6 | Source location remains above minimum threshold after transfer. | [BR-012] |

---

### UC-034 — Analyze and Recommend Network Rebalancing

**Primary Actor:** Operations Director

#### Preconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| P1 | Primary actor is authenticated with network rebalancing analysis permission (PG-05, PG-11). | (FR-062) |
| P2 | Inventory records exist across multiple active locations. | — |
| P3 | Network-wide visibility is available for imbalance identification. | (FR-028) |

#### Postconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| PO1 | Location-level imbalances (stockout vs. excess) are identified and documented. | [BR-011] |
| PO2 | Transfer recommendations exist with source, destination, product, and quantity. | [BR-012] |
| PO3 | Approved recommendations generate transfer requests for execution. | — |
| PO4 | Network balance improvement summary is available for management review. | — |

---

## Domain 8: Returns Management

### UC-035 — Authorize and Record Customer Returns

**Primary Actor:** Customer Service Representative

#### Preconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| P1 | Primary actor is authenticated with return authorization permission (PG-09). | (FR-064) |
| P2 | Original customer order exists and is locatable in the system. | — |
| P3 | Return request is within return policy eligibility (quantity, timeframe, product condition policy). | [BR-025] |
| P4 | Return destination location is active and configured for return receipt. | — |

#### Postconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| PO1 | Return authorization exists with reference, authorized products, quantities, and destination. | [BR-025] |
| PO2 | Return authorization is linked to original order and return policy. | [BR-025] |
| PO3 | Return status is pending receipt at warehouse. | — |
| PO4 | Authorization is recorded in audit trail. | (FR-086) |

---

### UC-036 — Receive, Inspect, and Disposition Returned Goods

**Primary Actor:** Receiving Clerk

#### Preconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| P1 | Primary actor is authenticated with return receipt and inspection permission (PG-09). | (FR-065) |
| P2 | Valid return authorization exists for the inbound return shipment. | [BR-025] |
| P3 | Returned goods are physically present at receiving location. | — |
| P4 | Inspection criteria and disposition options (restock, quarantine, write-off) are defined. | [BR-026] |

#### Postconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| PO1 | Return receipt quantity is recorded against authorization. | [BR-025] |
| PO2 | Inspection outcome is documented with condition assessment. | [BR-026] |
| PO3 | For restock disposition, sellable on-hand and ATP are increased at designated location. | [BR-026] |
| PO4 | For quarantine or write-off disposition, stock is routed per disposition workflow. | [BR-026], [BR-013] |
| PO5 | Return authorization is closed or updated with final disposition status. | (FR-067) |
| PO6 | Return processing is recorded in movement history and audit trail. | (FR-029), (FR-086) |

---

## Domain 9: Reporting, Performance & Financial Alignment

### UC-037 — Review Inventory Dashboards and Operational Reports

**Primary Actor:** Operations Director

#### Preconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| P1 | Primary actor is authenticated with dashboard and reporting permission (PG-11). | (FR-068) |
| P2 | Inventory transaction and balance data exists for the reporting scope. | — |
| P3 | Reporting period and location scope are within actor's authorized visibility. | (FR-082) |

#### Postconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| PO1 | Dashboard or report reflects current inventory data for selected scope and period. | — |
| PO2 | Report generation timestamp is recorded. | — |
| PO3 | Exportable report output is available where export is requested. | — |
| PO4 | No inventory data is modified by reporting activity. | — |

---

### UC-038 — Review Inventory Performance KPIs

**Primary Actor:** Chief Executive Officer

#### Preconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| P1 | Primary actor is authenticated with executive KPI visibility permission (PG-11). | (FR-073) |
| P2 | KPI baseline and target values are defined for the reporting period. | — |
| P3 | Sufficient operational data exists for KPI calculation (data completeness indicator available). | — |

#### Postconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| PO1 | Tier 1 inventory KPIs are displayed with target comparison and trend. | — |
| PO2 | RAG status is indicated per KPI where thresholds are defined. | — |
| PO3 | Drill-down to contributing factors is available for underperforming KPIs. | — |
| PO4 | No operational data is modified by KPI review. | — |

---

### UC-039 — Reconcile Inventory Valuation with Finance

**Primary Actor:** Finance Manager

#### Preconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| P1 | Primary actor is authenticated with valuation and reconciliation permission (PG-12). | (FR-089) |
| P2 | Operational inventory valuation data exists for the reconciliation period. | — |
| P3 | General ledger inventory balance is available for comparison. | [BR-008] |
| P4 | Consignment stock is identifiable and separable from owned inventory. | [BR-031] |

#### Postconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| PO1 | Side-by-side comparison of operational valuation and GL balance is documented. | [BR-008] |
| PO2 | Variance amount and percentage are calculated; tolerance status is indicated. | — |
| PO3 | Reconciliation is marked complete with finance notes and status. | — |
| PO4 | Consignment stock is excluded from owned valuation comparison. | [BR-031] |
| PO5 | Reconciliation record is archived for audit. | (FR-086) |

---

## Domain 10: Commercial Alignment & Governance

### UC-040 — Confirm Promotional and Launch Stock Readiness

**Primary Actor:** Marketing Manager

#### Preconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| P1 | Primary actor is authenticated with campaign readiness permission (PG-10). | (FR-057) |
| P2 | Campaign or launch definition exists with required products and quantities. | [BR-029] |
| P3 | Campaign start date is defined. | — |
| P4 | Ring-fenced promotional stock allocation is configured or allocatable. | [BR-029] |

#### Postconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| PO1 | Readiness status per product is recorded (confirmed, conditional, or not ready). | — |
| PO2 | Ring-fenced promotional stock is protected from non-promotional consumption. | [BR-029] |
| PO3 | Readiness confirmation or gap summary is documented with manager identity and date. | — |
| PO4 | Campaign readiness alerts are updated for remaining gaps. | (FR-080) |

---

### UC-041 — Conduct Inventory Audit and Control Review

**Primary Actor:** Internal Auditor

#### Preconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| P1 | Primary actor is authenticated with audit query permission (PG-15). | (FR-087) |
| P2 | Inventory transaction and audit trail data exists for the audit scope period. | (FR-086) |
| P3 | Segregation of duties rules and governance policies are defined for compliance testing. | [BR-019], [BR-021] |
| P4 | Audit scope (period, location, transaction type) is defined. | — |

#### Postconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| PO1 | Audit sample or population is reviewed for control compliance. | — |
| PO2 | SoD violations and policy non-compliance are flagged where detected. | [BR-019], [BR-020], [BR-021] |
| PO3 | Audit findings and review session are documented. | — |
| PO4 | Audit workpaper summary is exportable for governance records. | (FR-087) |
| PO5 | No operational inventory data is modified by audit review (read-only). | — |

---

## Domain 11: Cross-Cutting System Interactions

### UC-042 — View Inventory Movement and Transaction History

**Primary Actor:** Inventory Controller

#### Preconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| P1 | Primary actor is authenticated with movement history inquiry permission (PG-03, PG-11). | (FR-029) |
| P2 | Inventory movements have been recorded for the search scope. | (FR-029) |
| P3 | Search criteria (product, location, date range, type) are within authorized visibility. | (FR-082) |

#### Postconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| PO1 | Matching movement transactions are displayed chronologically. | (FR-029) |
| PO2 | Transaction detail includes quantity, type, user, timestamp, and reason code where applicable. | [BR-020] |
| PO3 | Lot or batch attribution is visible for traceable product movements. | [BR-017] |
| PO4 | Exportable movement history is available for the search scope. | — |
| PO5 | No inventory data is modified by history inquiry. | — |

---

### UC-043 — Query and Review Audit Trail

**Primary Actor:** Internal Auditor

#### Preconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| P1 | Primary actor is authenticated with audit trail query permission (PG-15). | (FR-086) |
| P2 | Audit log entries exist for the query scope. | (FR-086) |
| P3 | Query parameters are within authorized audit scope. | — |

#### Postconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| PO1 | Immutable audit log entries matching criteria are displayed. | (FR-086) |
| PO2 | Before-and-after state is available for material changes. | (FR-086) |
| PO3 | Exportable audit report is available for evidence purposes. | — |
| PO4 | Audit query activity is logged for accountability. | (FR-083) |
| PO5 | No operational data is modified by audit trail query. | — |

---

### UC-044 — Manage User Accounts and Role Assignments

**Primary Actor:** System Administrator

#### Preconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| P1 | Primary actor is authenticated with user administration permission (PG-14). | (FR-085) |
| P2 | Business roles and location definitions exist in the system. | (FR-081) |
| P3 | Proposed role assignment does not create segregation of duties conflict. | (FR-084) |
| P4 | For deactivation, pending approvals in user's queue are reassigned or resolved. | — |

#### Postconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| PO1 | User account exists with correct status (active or deactivated). | (FR-085) |
| PO2 | Assigned roles and location scope reflect current job responsibilities. | (FR-081), (FR-082) |
| PO3 | User permissions align with RBAC matrix without SoD conflicts. | (FR-084) |
| PO4 | Account creation, modification, or deactivation is recorded in audit trail. | (FR-086) |

---

### UC-045 — Enforce Role-Based and Location-Scoped Access

**Primary Actor:** System Administrator

#### Preconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| P1 | Primary actor is authenticated with access control configuration permission (PG-14). | (FR-081) |
| P2 | Role-permission matrix and location scope definitions exist. | (FR-082) |
| P3 | Segregation of duties rules are defined for validation. | (FR-084) |
| P4 | For access enforcement events, user account is active with assigned roles. | — |

#### Postconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| PO1 | Updated permissions apply to all users assigned the affected role. | (FR-081) |
| PO2 | Access attempts are granted only for permitted functions within location scope. | (FR-082) |
| PO3 | Unauthorized access attempts are denied and logged. | (FR-083) |
| PO4 | SoD conflicts are prevented in role permission configuration. | [BR-019], [BR-021], (FR-084) |
| PO5 | Access control changes are recorded in audit trail. | (FR-086) |

---

### UC-046 — Import Initial Product and Stock Master Data

**Primary Actor:** Inventory Controller

#### Preconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| P1 | Primary actor is authenticated with data import permission and product/location management access. | (FR-090) |
| P2 | Import file conforms to system template format. | (FR-090) |
| P3 | Location master exists for all location codes referenced in stock balance import. | — |
| P4 | Import file SKUs are unique within file and do not conflict with existing catalog (for initial load). | — |

#### Postconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| PO1 | Product master records are created or updated per validated import rows. | — |
| PO2 | Opening stock balances are recorded at specified locations. | (FR-010) |
| PO3 | Import completion report documents created, updated, and skipped records. | — |
| PO4 | Imported data is available for operational transactions. | — |
| PO5 | Import execution is recorded in audit trail with user and timestamp. | (FR-086) |

---

### UC-047 — Receive and Respond to Operational Notifications

**Primary Actor:** Warehouse Manager

#### Preconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| P1 | Primary actor is authenticated with notification access for relevant notification types. | (FR-076) |
| P2 | Pending notification exists (alert, approval, exception, inbound delay, campaign). | — |
| P3 | Linked business context (product, order, transfer, campaign) is accessible to actor. | — |

#### Postconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| PO1 | Notification action is completed or delegated with recorded outcome. | — |
| PO2 | Linked business record reflects action taken (acknowledgment, approval, resolution). | [BR-009] |
| PO3 | Notification is archived or removed from active pending queue. | — |
| PO4 | Notification handling is recorded with user and timestamp. | (FR-083) |

---

### UC-048 — Support Multi-Location Split Fulfillment

**Primary Actor:** Warehouse Manager

#### Preconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| P1 | Primary actor is authenticated with multi-location fulfillment permission (PG-08). | (FR-048) |
| P2 | Customer order is confirmed with lines requiring fulfillment. | [BR-002] |
| P3 | Single fulfillment location has insufficient ATP; network-wide ATP can satisfy order (fully or partially). | [BR-001] |
| P4 | Contributing source locations have available stock above minimum thresholds. | [BR-012] |
| P5 | Availability confirmation is complete or current network ATP is validated. | [BR-001] |

#### Postconditions

| # | Condition | Business Rule |
|---|-----------|---------------|
| PO1 | Location-specific reservations exist for each contributing fulfillment location. | [BR-002] |
| PO2 | ATP is reduced at each contributing location by allocated quantity. | [BR-001] |
| PO3 | Pick tasks are routed to each source location with linked parent order reference. | — |
| PO4 | Consolidated order status reflects multi-location fulfillment progress. | — |
| PO5 | Source locations remain above minimum threshold after allocation. | [BR-012] |
| PO6 | Split fulfillment plan is recorded in audit trail. | (FR-086) |

---

## Business Rule Coverage Matrix

| Business Rule | Use Cases with Preconditions | Use Cases with Postconditions |
|---------------|------------------------------|-------------------------------|
| BR-001 | UC-013, UC-021, UC-022, UC-048 | UC-012, UC-013, UC-021, UC-022, UC-023, UC-026, UC-048 |
| BR-002 | UC-021, UC-022, UC-023, UC-024, UC-048 | UC-021, UC-022, UC-023, UC-024, UC-025, UC-048 |
| BR-003 | UC-023, UC-024 | UC-024, UC-026 |
| BR-004 | UC-008, UC-010, UC-011 | UC-008 |
| BR-005 | UC-010 | UC-010 |
| BR-006 | UC-009 | UC-009 |
| BR-007 | UC-006, UC-007, UC-008, UC-011 | UC-006, UC-030 |
| BR-008 | UC-039 | UC-009, UC-039 |
| BR-009 | UC-003, UC-012, UC-028, UC-029, UC-030 | UC-003, UC-028, UC-029, UC-030, UC-047 |
| BR-010 | UC-003, UC-017, UC-022, UC-029 | UC-003, UC-017, UC-022 |
| BR-011 | UC-029, UC-031, UC-034 | UC-028, UC-029, UC-034 |
| BR-012 | UC-031, UC-032, UC-033, UC-048 | UC-031, UC-032, UC-033, UC-048 |
| BR-013 | UC-019, UC-024, UC-031 | UC-012, UC-019, UC-024, UC-026, UC-031, UC-036 |
| BR-014 | UC-024 | UC-010, UC-024 |
| BR-015 | UC-024 | UC-010, UC-024 |
| BR-016 | UC-008 | UC-008 |
| BR-017 | UC-008, UC-033, UC-042, UC-048 | UC-008, UC-024, UC-033, UC-042 |
| BR-018 | UC-014 | UC-014 |
| BR-019 | UC-016, UC-041, UC-045 | UC-016, UC-041, UC-045 |
| BR-020 | UC-005, UC-009, UC-017, UC-020, UC-041 | UC-005, UC-017, UC-018, UC-020, UC-041, UC-042 |
| BR-021 | UC-005, UC-016, UC-017, UC-041, UC-045 | UC-005, UC-016, UC-017, UC-041, UC-045 |
| BR-022 | UC-015, UC-016 | UC-015, UC-016 |
| BR-023 | UC-018 | UC-018 |
| BR-024 | UC-008, UC-010, UC-011, UC-014, UC-033 | UC-015 |
| BR-025 | UC-011, UC-035, UC-036 | UC-011, UC-035, UC-036 |
| BR-026 | UC-036 | UC-036 |
| BR-027 | UC-006, UC-029 | UC-001, UC-006, UC-029 |
| BR-028 | UC-025 | UC-025 |
| BR-029 | UC-021, UC-022, UC-040 | UC-013, UC-021, UC-022, UC-040 |
| BR-030 | UC-010, UC-019 | UC-010, UC-019 |
| BR-031 | UC-039 | UC-039 |
| BR-032 | UC-004, UC-028 | UC-004, UC-028 |

---

## Traceability

| Source Document | Reference |
|-----------------|-----------|
| Use Case Catalog | SRS-UC-001 |
| Use Case Main Flows | SRS-UC-002 |
| Use Case Alternate Flows | SRS-UC-003 |
| Use Case Exception Flows | SRS-UC-004 |
| Business Rule Catalog | SRS-BR-001 |

---

## Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Business Analyst | | | |
| Product Owner | | | |
| Operations Director | | | |

---

*End of Use Case Preconditions and Postconditions*

*Document ID: SRS-UC-005 | Version 1.0 | July 5, 2026*
