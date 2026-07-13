# Validation Rules Specification
## Inventory Management System

---

## Document Information

| Attribute | Detail |
|-----------|--------|
| **Document ID** | SRS-VR-001 |
| **Document Title** | Validation Rules — Inventory Management System |
| **Version** | 1.0 |
| **Status** | Draft |
| **Document Owner** | Senior Business Analyst |
| **Source Documents** | BRD-IMS-001, Functional Requirements (FR-001–FR-090), Business Rules (BR-001–BR-032), Acceptance Criteria |
| **Date** | July 5, 2026 |
| **Scope** | Data validation and business validation only — no implementation, API, or database design |

### Purpose

This document defines validation rules that must be satisfied when users interact with inventory management capabilities. Each rule is tied to a functional requirement and feature. Rules express *what* must be validated from a business perspective, not *how* the system enforces it technically.

### Validation Rule Fields

| Field | Description |
|-------|-------------|
| **Validation ID** | Unique identifier (VR-001, VR-002, …) |
| **Related Feature** | Primary feature from Feature Catalog (F-01–F-30) |
| **Related FR** | Functional requirement identifier |
| **Validation Rule** | The condition that must be satisfied |
| **Error Condition** | When validation fails |
| **User Message** | Plain-language message presented to the user |
| **Business Reason** | Why the rule exists |

---

## Domain 1: Master Data & Governance

### FR-001 — Create and Maintain Product Master Records (F-01)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-001 | F-01 | SKU, product name, and unit of measure are required on every product record. | Any required attribute is missing or blank. | Required product information is missing. Enter SKU, product name, and unit of measure before saving. | Incomplete product records cause ordering, receiving, and fulfillment errors across the network. |
| VR-002 | F-01 | SKU must be unique across the product catalog. | Submitted SKU already exists on another active or inactive product. | This SKU already exists. Use a unique SKU or update the existing product record. | Duplicate SKUs fragment stock visibility and undermine a single product identity (BR-001 context). |
| VR-003 | F-01 | Only authorized users may create or modify product master records. | User lacks product maintenance authority. | You are not authorized to create or change product records. | Product master data quality requires controlled ownership by the Inventory Controller function. |

### FR-002 — Manage Product Status Lifecycle (F-01)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-004 | F-01 | Discontinued products must not be eligible for new replenishment or purchase. | User attempts to reorder or replenish a discontinued product. | This product is discontinued and cannot be reordered. | Prevents obsolete inventory accumulation and conflicting assortment decisions (BR-027). |
| VR-005 | F-01 | Product status changes must record prior status, new status, user, and date. | Status change submitted without auditable attribution. | Product status could not be saved. A valid status and authorization are required. | Status history supports lifecycle accountability and audit review. |
| VR-006 | F-01 | Inactive or discontinued products must be blocked from new reservations unless policy explicitly permits. | Reservation or fulfillment attempted on non-active product without exception. | This product is not active and cannot be committed to new orders. | Prevents customer commitments against products the business has withdrawn from sale. |

### FR-003 — Support Product Identifier Lookup (F-01)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-007 | F-01 | Lookup by SKU, barcode, or assigned identifier must match an existing product record. | Identifier does not match any product. | No product found for this identifier. Verify the SKU or barcode and try again. | Prevents implicit creation of products during operational transactions. |
| VR-008 | F-01 | Stock context shown during lookup must respect the user's authorized location scope. | User requests stock detail for an unauthorized location. | You do not have access to inventory at this location. | Aligns visibility with operational accountability and location ownership. |

### FR-004 — Detect and Resolve Duplicate Product Records (F-01)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-009 | F-01 | New product submissions must be checked for matching or conflicting SKU, barcode, or highly similar name. | Potential duplicate detected and user proceeds without resolution. | A similar product already exists. Review the existing record before creating a new product. | Prevents parallel identities for the same physical product (PP-07). |
| VR-010 | F-01 | Merging duplicate products requires Inventory Controller authorization when both records have on-hand stock. | Unauthorized merge attempted on stocked products. | Product merge requires Inventory Controller approval when stock exists on both records. | Protects stock integrity during catalog consolidation. |

### FR-005 — Configure and Maintain Inventory Locations (F-02)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-011 | F-02 | Location name, type, and operational status are required. | Required location attributes missing. | Required location information is missing. Enter name, type, and status before saving. | Locations are the foundation for all stock assignment and reporting. |
| VR-012 | F-02 | Deactivated locations must not accept new receipts, reservations, or fulfillments except authorized disposition activity. | Transaction attempted at deactivated location. | This location is not active for new inventory activity. | Prevents stock and transactions at locations that are closed or not yet ready. |
| VR-013 | F-02 | Location activation for transactions requires approved opening balance when go-live policy applies. | Operational transaction at location without approved opening balance. | This location cannot process transactions until opening stock is verified and approved. | Go-live with unverified balances embeds errors that undermine trust (BA-16). |

### FR-006 — Manage Location Hierarchy (F-02)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-014 | F-02 | A location cannot be assigned as its own parent or ancestor. | Circular hierarchy proposed. | Invalid hierarchy: a location cannot be placed under itself or its own child. | Circular hierarchies break network roll-up and reporting. |
| VR-015 | F-02 | Each location may have only one parent in the hierarchy at a time. | Multiple conflicting parent assignments. | This location already belongs to another hierarchy branch. Resolve the assignment before saving. | Ensures unambiguous network structure for accountability and reporting. |

### FR-007 — Plan Location Closure and Stock Disposition (F-02)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-016 | F-02 | Location closure must be blocked while on-hand stock remains unless a disposition plan is documented or explicitly waived by an authorized approver. | Closure attempted with remaining stock and no plan. | This location still holds inventory. Complete stock disposition or obtain closure approval before deactivating. | Prevents stranded inventory and orphaned records when locations exit the network. |
| VR-017 | F-02 | New inbound and fulfillment activity must be blocked at a location in closure status except authorized disposition transactions. | Standard operational transaction at closing location. | This location is closing. Only authorized disposition activities are permitted. | Protects closure integrity while stock is being cleared. |

### FR-008 — Define Stock Policy and Replenishment Thresholds (F-03)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-018 | F-03 | Reorder level, minimum threshold, and safety stock must be zero or positive numeric values. | Negative or non-numeric threshold entered. | Threshold values must be zero or greater. Enter valid numbers for all thresholds. | Invalid thresholds produce false alerts or missed replenishment signals. |
| VR-019 | F-03 | Minimum threshold must not exceed reorder level unless business policy explicitly allows inverted configuration. | Illogical threshold combination submitted. | Minimum threshold cannot be higher than reorder level. Adjust values to match stock policy. | Illogical thresholds cause incorrect low-stock detection and replenishment timing (BR-009). |
| VR-020 | F-03 | Threshold changes must include an effective date and retain prior values in history. | Threshold saved without effective date or history loss. | Stock policy could not be saved. An effective date is required for threshold changes. | Historical thresholds explain past alert behavior and support audit review. |

### FR-009 — Classify Products by ABC Priority (F-03)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-021 | F-03 | ABC classification must be one of: A, B, or C. | Invalid classification value submitted. | Invalid product class. Select A, B, or C. | Standard classification enables consistent operational prioritization (BR-032). |
| VR-022 | F-03 | Classification may only be assigned to active or inactive products, not to invalid or unknown product references. | Classification applied to non-existent product. | Product not found. Classification can only be applied to valid product records. | Ensures classification drives count and alert rules for real catalog items. |

### FR-010 — Establish Opening Stock Balance at Location Go-Live (F-02)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-023 | F-02 | Opening balance quantities must be non-negative numbers for each counted SKU. | Negative or non-numeric opening quantity entered. | Opening quantity must be zero or greater. Correct invalid count entries before submitting. | Negative opening balances corrupt inventory from go-live. |
| VR-024 | F-02 | Every opening balance SKU must exist in the product catalog before location activation. | Opening balance references unknown SKU. | Unknown product in opening balance. Resolve catalog gaps before activating this location. | Opening balances must tie to a single trusted product identity. |
| VR-025 | F-02 | Location activation requires authorized approval of the complete opening balance package. | Activation attempted before approver sign-off. | Opening balance must be approved before this location can go live. | Verified baselines are required for credible inventory control at cutover. |

### FR-011 — Maintain Standard Reason Codes (F-17)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-026 | F-17 | Adjustments, write-offs, and receipt discrepancies require selection of an active reason code before submission. | Transaction submitted without reason code. | A reason code is required. Select the reason for this inventory change. | Uncategorized adjustments prevent shrinkage analysis and audit substantiation (BR-020). |
| VR-027 | F-17 | Retired reason codes must not be selectable for new transactions. | Retired code used on new transaction. | This reason code is no longer active. Select a current reason code. | Retired codes remain on history only; active list reflects current policy. |

### FR-012 — Manage Inventory Governance Policies (F-03)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-028 | F-03 | Only one governance policy version may be effective for a given parameter at any point in time. | Overlapping effective policy versions detected. | Conflicting policy versions exist. Publish a single effective policy before proceeding. | Ambiguous policy causes inconsistent approvals and control failures. |
| VR-029 | F-03 | Policy parameters referenced by workflows must be defined before dependent transactions are processed. | Transaction evaluated against undefined policy value. | Required business policy is not configured. Contact operations leadership to define policy values. | Prevents silent defaults on financially material decisions. |

---

## Domain 2: Inbound & Receiving

### FR-013 — Record Purchase Order Commitments (F-07)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-030 | F-07 | Purchase order must include product, ordered quantity, supplier reference, receiving location, and expected delivery date. | Required PO field missing. | Required purchase order information is missing. Complete all mandatory fields before saving. | Incomplete POs cannot support receiving verification or inbound visibility. |
| VR-031 | F-07 | PO lines must reference active products and active receiving locations. | Discontinued product or deactivated location on PO line. | This product or location is not valid for ordering. Select an active product and receiving location. | Prevents procurement against invalid catalog or network entities. |
| VR-032 | F-07 | Ordered quantity must be greater than zero. | Zero or negative PO quantity. | Order quantity must be greater than zero. | Zero-quantity orders add no inbound supply value and corrupt replenishment planning. |

### FR-014 — Plan and Communicate Expected Inbound Deliveries (F-07)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-033 | F-07 | Expected delivery date must be a valid calendar date not in the distant past for new schedules. | Invalid or unreasonably past delivery date entered. | Enter a valid expected delivery date. | Invalid dates undermine receiving preparation and availability projections. |
| VR-034 | F-07 | Inbound schedule views must be limited to locations the user is authorized to access. | User views unauthorized location schedule. | You do not have access to inbound schedules for this location. | Protects location-scoped operational data. |

### FR-015 — Receive and Verify Inbound Goods (F-05)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-035 | F-05 | Accepted receipt quantity must be greater than zero and must not exceed physically verified quantity. | Zero, negative, or unsubstantiated accepted quantity. | Enter a valid accepted quantity greater than zero. | Recording unverified quantities creates phantom inventory (BR-004). |
| VR-036 | F-05 | Received product must match the PO line product identity. | Product on receipt does not match PO line. | Product received does not match the purchase order. Correct the product or document a discrepancy. | Wrong-item receipt corrupts inventory and supplier accountability. |
| VR-037 | F-05 | Only verified accepted quantity may increase on-hand balance; rejected or damaged quantity must be recorded separately. | Full PO quantity accepted when portion is damaged or rejected. | Record accepted and rejected quantities separately. Only accepted stock may enter inventory. | Separates sellable stock from disputed or unsellable goods (BR-006). |

### FR-016 — Document and Resolve Receipt Discrepancies (F-05)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-038 | F-05 | Open discrepancies must be documented with type, variance quantity, and notes before disputed quantity is finalized. | Discrepancy closed without required documentation. | Document the discrepancy type and quantity before resolving this receipt. | Undocumented discrepancies waive supplier accountability (BR-006). |
| VR-039 | F-05 | Disputed quantity must remain excluded from sellable availability until resolution is approved. | Disputed stock made available before resolution. | Disputed quantity cannot be made available until the discrepancy is resolved. | Prevents fulfillment from stock that is not confirmed received. |

### FR-017 — Enforce Purchase Order Reference for Supplier Receipts (F-05)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-040 | F-05 | Standard supplier receipts require a valid open purchase order reference. | Receipt attempted without PO or valid ad-hoc exception. | A valid purchase order is required to receive this shipment. Obtain PO confirmation or authorized ad-hoc approval. | Maintains procurement control and supports financial matching (BR-007). |
| VR-041 | F-05 | Receipt against a PO line must not exceed remaining open quantity plus approved tolerance. | Receipt quantity exceeds allowable open PO quantity. | Received quantity exceeds the remaining purchase order quantity. Adjust quantity or obtain over-receipt approval. | Prevents silent over-receipt that affects payment and inventory accuracy. |
| VR-042 | F-05 | Ad-hoc receipts require documented approver and business reason. | Ad-hoc receipt without authorization. | Emergency receipt requires authorized approval and a documented reason. | Authorized exceptions only; unaudited receipts break financial controls. |

### FR-018 — Manage Put-Away and Stock Availability Timing (F-06)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-043 | F-06 | Put-away quantity must not exceed received quantity still in receiving status. | Put-away total exceeds received quantity. | Put-away quantity cannot exceed the quantity received. Verify counts before confirming put-away. | Prevents availability inflation beyond physically received stock (BR-005). |
| VR-044 | F-06 | ATP must not increase until put-away is confirmed for the corresponding quantity. | Availability updated before put-away confirmation. | Stock is not yet available. Complete put-away before this quantity can be promised or picked. | Stock in the receiving area is not operationally locatable (BR-005). |

### FR-019 — Receive Return and Non-PO Inbound Stock (F-05)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-045 | F-05 | Customer return receipts require a valid return authorization reference. | Return received without valid authorization. | A valid return authorization is required to accept this return. | Links physical returns to commercial transactions (BR-025). |
| VR-046 | F-05 | Return receipt quantity must not exceed authorized return quantity. | Received return quantity exceeds authorization. | Received quantity exceeds the authorized return amount. Verify the return authorization. | Prevents acceptance of unauthorized or excess returns. |
| VR-047 | F-05 | Sellable ATP must not increase from return receipt until inspection passes when inspection is required. | Restock to available before inspection completion. | Returned goods must pass inspection before being added to sellable stock. | Protects customers from receiving used or damaged goods as new (BR-026). |

### FR-020 — Support Receipt Quantity Tolerance Evaluation (F-05)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-048 | F-05 | Receipt variances within defined tolerance may be auto-accepted; variances beyond tolerance require approver action. | Over- or under-receipt beyond tolerance accepted without approval. | Receipt variance exceeds allowed tolerance. Supervisor approval is required. | Balances operational flexibility with control over material variances. |
| VR-049 | F-05 | Tolerance decision must be recorded on the receipt record. | Tolerance applied without audit record. | Receipt could not be finalized. Tolerance evaluation must be documented. | Supports supplier performance tracking and payment dispute evidence. |

### FR-021 — Cancel or Amend Open Purchase Orders (F-07)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-050 | F-07 | Fully received PO lines must not be cancelled or reduced below received quantity. | Amendment would reduce quantity below already received amount. | Cannot amend below quantity already received. Adjust the change to reflect actual receipts. | Protects integrity between PO commitment and receipt history. |
| VR-051 | F-07 | PO cancellation or material amendment requires authorized purchasing approval. | Unauthorized user amends or cancels PO. | You are not authorized to change this purchase order. | Prevents unauthorized changes to supplier commitments. |

### FR-022 — Record Supplier Delivery Performance (F-07)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-052 | F-07 | Performance metrics must be derived only from completed receipts and resolved discrepancies tied to valid PO records. | Performance calculated from incomplete or unlinked transactions. | Supplier performance cannot be calculated for this period. Complete receipts and resolve discrepancies first. | Ensures supplier scorecards reflect actual delivery outcomes. |

---

## Domain 3: Inventory Visibility & Status

### FR-023 — Display On-Hand Quantity (F-04)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-053 | F-04 | On-hand display must reflect only locations within the user's authorized scope. | Unauthorized location data requested. | You do not have access to on-hand data for this location. | Location-scoped access aligns with operational accountability. |
| VR-054 | F-04 | Inquiry must reference a valid product or valid filter criteria. | Empty or invalid product/location selection. | Select a valid product or location to view on-hand quantity. | Prevents ambiguous queries that could mislead decisions. |

### FR-024 — Display Available-to-Promise Quantity (F-04)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-055 | F-04 | ATP must equal on-hand minus reservations and non-sellable holds including quarantined stock. | ATP displayed inconsistent with underlying availability components. | Availability cannot be displayed. Stock status data is incomplete. | ATP is the only honest quotable quantity (BR-001). |
| VR-056 | F-04 | Quarantined and held stock must be excluded from ATP in all availability views. | Quarantined quantity included in ATP. | Quarantined stock is not available for sale. | Prevents promising stock under quality or regulatory hold (BR-013). |

### FR-025 — Display Reserved and Committed Stock (F-04)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-057 | F-04 | Reserved quantity must not exceed on-hand quantity at the same product and location. | Reserved balance greater than on-hand. | Reserved quantity cannot exceed on-hand stock. Escalate to operations for investigation. | Excess reservation indicates data integrity failure or overselling risk. |
| VR-058 | F-04 | Reservation display must include linked order reference for each reserved quantity. | Reservation shown without order linkage. | Reservation detail is incomplete. Order reference is required for committed stock display. | Supports fulfillment planning and dispute resolution between sales and warehouse. |

### FR-026 — Indicate Stock Status (F-04)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-059 | F-04 | Stock status must be derived from ATP relative to defined reorder and minimum thresholds. | Status shown without configured thresholds for product-location. | Stock status is unavailable. Define thresholds for this product at this location. | Status indicators require policy thresholds to be meaningful. |
| VR-060 | F-04 | Out-of-stock status applies when ATP is zero or below minimum sellable unit. | Positive ATP shown as out of stock, or zero ATP shown as in stock. | Stock status does not match current availability. Refresh or escalate data review. | Incorrect status drives wrong replenishment and sales decisions. |

### FR-027 — Search and Filter Inventory Views (F-04)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-061 | F-04 | Search results must respect user location access permissions. | Results include unauthorized locations. | Some results are hidden based on your location access. | Prevents cross-location data exposure to unauthorized users. |
| VR-062 | F-04 | Date-bounded filters must have a valid start date on or before end date. | Invalid date range entered. | Enter a valid date range. Start date must be on or before end date. | Invalid ranges produce empty or misleading inventory views. |

### FR-028 — Display Expected Inbound and Network-Wide Availability (F-04)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-063 | F-04 | Expected inbound quantities must include only open PO lines not yet fully received. | Closed or fully received PO lines counted as inbound. | Inbound projection unavailable. Verify purchase order status. | Accurate inbound projection supports transfer-before-purchase decisions (BR-011). |
| VR-064 | F-04 | Network ATP aggregation must sum only authorized locations. | Unauthorized locations included in network total. | Network availability is limited to locations you are authorized to view. | Network views still require appropriate access scope. |

---

## Domain 4: Inventory Control & Accuracy

### FR-029 — Record All Inventory Movements (F-05)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-065 | F-05 | Every balance-changing transaction must record product, quantity, location, transaction type, user, and timestamp. | Movement recorded without required audit attributes. | Transaction could not be completed. Required movement details are missing. | Complete movement history is required for accountability (BO-003, BO-019). |
| VR-066 | F-05 | Movement quantity must be non-zero. | Zero-quantity movement submitted. | Quantity must be greater than zero for inventory movements. | Zero movements add noise without business meaning. |

### FR-030 — Schedule and Assign Cycle Counts (F-14)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-067 | F-14 | Count assignments must reference valid active products at valid active locations. | Assignment to invalid product or location. | Count assignment is invalid. Select an active product and location. | Counts on invalid entities waste effort and produce no control value. |
| VR-068 | F-14 | Class A products must be scheduled at higher frequency than Class C per ABC policy when classification exists. | Class A scheduled less frequently than Class C without authorized exception. | Class A products require more frequent counting per policy. Adjust the count schedule. | Focuses accuracy effort where business impact is highest (BR-032). |

### FR-031 — Perform Blind Cycle Counts (F-14)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-069 | F-14 | Counter must not see system expected quantity during an active blind count. | Expected quantity visible before count submission. | Blind count in progress. System quantity is hidden until you submit your count. | Blind counting prevents biased confirmation of bad data (BR-018). |
| VR-070 | F-14 | Physical count quantity must be a non-negative number. | Negative or non-numeric count entered. | Enter a valid physical count quantity of zero or greater. | Invalid entries cannot support variance analysis. |

### FR-032 — Conduct Full Physical Inventory Count (F-15)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-071 | F-15 | Movement freeze must be in effect at the location during an active full wall-to-wall count. | Receipt, shipment, transfer, or adjustment attempted during freeze. | Inventory count in progress. Movements are frozen until the count is completed. | Movements during count invalidate the snapshot (BR-024). |
| VR-072 | F-15 | Full count must cover all SKUs with on-hand or receiving status at the location before variances are finalized. | Count finalized with uncounted SKUs remaining. | Full count is incomplete. All products must be counted before closing the count. | Partial counts cannot establish a reliable location baseline. |

### FR-033 — Identify and Report Count Variances (F-16)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-073 | F-16 | Variance must be calculated as physical count minus system quantity after count submission. | Variance calculated before count submission or with visible expected quantity in blind count. | Variance cannot be calculated until the physical count is submitted. | Ensures unbiased variance measurement (BR-018). |
| VR-074 | F-16 | Variances exceeding defined tolerance must be routed for investigation before adjustment. | Within-tolerance auto-adjustment applied to material variance, or material variance ignored. | Count variance exceeds tolerance and requires investigation. | Focuses correction effort on material discrepancies (BR-022). |

### FR-034 — Investigate and Approve Count Adjustments (F-16)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-075 | F-16 | Counter must not approve adjustments arising from their own count. | Same user submits count and approves adjustment. | You cannot approve an adjustment for a count you performed. An independent approver is required. | Segregation of duties prevents fraud and undetected error (BR-019). |
| VR-076 | F-16 | Material variances require investigation notes before approval. | Adjustment approved without investigation documentation. | Document investigation findings before approving this count adjustment. | Adjustments fix records; investigation fixes processes (BR-022). |

### FR-035 — Process Stock Adjustments (F-17)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-077 | F-17 | Adjustments require product, location, quantity, direction, and active reason code. | Missing mandatory adjustment attribute. | Required adjustment information is missing. Complete product, location, quantity, and reason code. | Incomplete adjustments are unauditable and analytically useless (BR-020). |
| VR-078 | F-17 | Decrease adjustments must not exceed available on-hand at the product and location. | Adjustment would drive negative on-hand. | Adjustment quantity exceeds available on-hand stock. | Negative on-hand indicates invalid correction or requires write-off workflow. |
| VR-079 | F-17 | User must be authorized for adjustment at the specified location. | Unauthorized location adjustment attempted. | You are not authorized to adjust inventory at this location. | Location-scoped accountability for stock corrections. |

### FR-036 — Process Inventory Write-Offs (F-17)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-080 | F-17 | Write-offs require documented evidence and approver per policy threshold. | Write-off submitted without evidence or required approval. | Write-off requires supporting evidence and authorized approval. | Unauthorized write-offs enable fraud and financial misstatement (BR-023). |
| VR-081 | F-17 | Write-off quantity must not exceed on-hand quantity at the location. | Write-off exceeds available stock. | Write-off quantity exceeds on-hand stock at this location. | Cannot write off stock that does not exist on record. |

### FR-037 — Enforce Adjustment Approval Thresholds (F-16)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-082 | F-16 | Adjustments above quantity or value threshold require independent approver who did not initiate the transaction. | Self-approved above-threshold adjustment. | This adjustment requires approval from an authorized independent approver. | Oversight proportional to financial impact (BR-021). |
| VR-083 | F-16 | Submitter must not be the final approver when segregation of duties policy applies. | Initiator and approver are the same person on restricted transaction. | You cannot approve your own adjustment. Route to an independent approver. | Core internal control requirement (BR-019). |

### FR-038 — Manage Quarantine and Hold Stock (F-18)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-084 | F-18 | Quarantined quantity must be immediately excluded from ATP. | Quarantined stock still available for reservation or fulfillment. | Quarantined stock cannot be sold or reserved. | Prevents shipping uninspected or defective goods (BR-013). |
| VR-085 | F-18 | Release from quarantine to sellable stock requires inspection outcome and authorized disposition decision. | Quarantine released without inspection decision. | Quarantined stock cannot be released without an approved inspection outcome. | Ensures only quality-approved stock returns to sellable inventory. |

### FR-039 — Analyze Shrinkage and Loss Trends (F-19)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-086 | F-19 | Shrinkage analysis periods must use valid start and end dates with start on or before end. | Invalid analysis period. | Select a valid reporting period for shrinkage analysis. | Invalid periods produce meaningless loss trends. |
| VR-087 | F-19 | Analysis must include only transactions with valid reason codes. | Uncategorized adjustments included in shrinkage totals without flag. | Shrinkage analysis excludes uncategorized adjustments. Review reason code compliance. | Reason codes enable root-cause analysis (BR-020). |

### FR-040 — Review Obsolete and Slow-Moving Stock (F-19)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-088 | F-19 | Aging threshold must be a positive number of days when configuring slow-moving criteria. | Invalid aging threshold. | Enter a valid number of days for slow-moving stock criteria. | Invalid thresholds misidentify obsolete inventory. |
| VR-089 | F-19 | Discontinued products with remaining on-hand must appear in obsolete review lists. | Discontinued stocked SKU omitted from review. | Discontinued products with remaining stock require disposition review. | Prevents trapped capital in products the business has exited (BR-027). |

---

## Domain 5: Order Fulfillment

### FR-041 — Confirm Order Availability (F-10)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-090 | F-10 | Availability confirmation must compare requested quantity to ATP at the fulfillment location, not on-hand alone. | Commitment made using on-hand ignoring reservations. | Insufficient available stock. Only unreserved quantity can be promised to customers. | Prevents overselling against committed stock (BR-001). |
| VR-091 | F-10 | Confirmed delivery commitment must not exceed ATP plus approved inbound only when inbound policy allows inclusion. | Commitment exceeds realistic fulfillable quantity. | Requested quantity cannot be confirmed with current availability. | Aligns customer promises with fulfillable stock. |

### FR-042 — Reserve Inventory for Confirmed Orders (F-10)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-092 | F-10 | Reservation quantity must not exceed ATP at the reservation location. | Reservation exceeds available stock. | Cannot reserve more than available stock. Reduce quantity or select another location. | Prevents double-allocation and pick failures (BR-002). |
| VR-093 | F-10 | Reservation must tie to a confirmed order line with product, quantity, and location. | Reservation without valid order reference. | Reservation requires a confirmed order line with product and quantity. | Links operational holds to commercial commitments. |
| VR-094 | F-10 | Safety stock must not be consumed by reservation without authorized exception when safety stock policy applies. | Reservation breaches safety stock without approval. | This reservation would use safety stock. Authorized exception and replenishment plan required. | Preserves buffer against next disruption (BR-010). |

### FR-043 — Release Inventory Reservations (F-10)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-095 | F-10 | Released quantity must not exceed reserved quantity for the order line. | Release exceeds active reservation. | Release quantity exceeds reserved amount for this order line. | Prevents artificial inflation of ATP. |
| VR-096 | F-10 | Reservation release must record reason such as cancellation, quantity change, fulfillment, or policy expiry. | Release without documented reason. | Select a reason for releasing this reservation. | Supports audit trail and availability restoration analysis. |

### FR-044 — Pick, Pack, and Ship (F-11)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-097 | F-11 | Shipment must not be recorded until pick verification confirms correct product and quantity. | Shipment recorded without pick confirmation. | Confirm picked product and quantity before marking this order shipped. | Inventory must not be deducted before verified pick (BR-003). |
| VR-098 | F-11 | Shipped quantity must not exceed reserved quantity for the order line. | Ship quantity greater than reservation. | Shipped quantity cannot exceed reserved quantity. Adjust shipment or reservation. | Maintains alignment between commitment, reservation, and fulfillment. |
| VR-099 | F-11 | Picked product must match order line product unless authorized substitution is approved. | Wrong product picked and shipped without approval. | Picked product does not match the order line. Obtain authorized substitution or re-pick. | Prevents wrong-item shipments and customer disputes. |

### FR-045 — Handle Partial Fulfillment (F-12)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-100 | F-12 | Partial shipment quantity must be greater than zero and less than full order line quantity. | Partial ship of zero or full quantity without backorder handling. | Partial shipment must be between zero and the full order quantity. | Defines true partial fulfillment versus full ship or cancel. |
| VR-101 | F-12 | Backorder for remaining quantity requires documented customer acknowledgment before processing. | Backorder created without customer acknowledgment. | Customer acknowledgment is required before placing the remaining quantity on backorder. | Backorder is a mutual agreement, not an internal note (BR-028). |

### FR-046 — Manage Backorders (F-12)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-102 | F-12 | Backorder fulfillment must follow defined priority rules when stock becomes available. | Stock reserved for backorder out of priority sequence without override. | Backorder fulfillment must follow priority policy. Escalate for manual override if needed. | Ensures fair and policy-driven delayed order fulfillment. |
| VR-103 | F-12 | Backorder quantity must equal unfulfilled order line quantity after partial shipments. | Backorder quantity inconsistent with order remainder. | Backorder quantity does not match the remaining order quantity. Reconcile order lines. | Keeps customer expectation aligned with system records. |

### FR-047 — Handle Outbound Fulfillment Exceptions (F-13)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-104 | F-13 | Pick failure or damage exception must be documented with type and quantity before order status is updated. | Exception closed without documentation. | Document the fulfillment exception type and affected quantity. | Enables root-cause analysis and customer communication. |
| VR-105 | F-13 | Inventory adjustment from pick failure requires reason code and may require approval per policy. | Record adjusted without reason or approval. | Inventory correction from this exception requires a reason code and may require approval. | Maintains accuracy after fulfillment disruptions. |

### FR-048 — Multi-Location Split Fulfillment (F-10)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-106 | F-10 | Total reserved quantity across locations must equal order line quantity. | Sum of location reservations does not match order line. | Split fulfillment reservations must total the full order line quantity. | Prevents under- or over-allocation on multi-location orders. |
| VR-107 | F-10 | Each location reservation must not exceed ATP at that location. | Location reservation exceeds local ATP. | Insufficient stock at {location}. Reduce reservation or choose another location. | Each fulfillment point must have real available stock. |

### FR-049 — Display Order Fulfillment Status (F-11)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-108 | F-11 | Order status inquiry requires valid order reference. | Invalid or unknown order reference. | Order not found. Verify the order reference and try again. | Prevents misleading status responses. |
| VR-109 | F-11 | Displayed shipped, reserved, and backordered quantities must reconcile to order line quantity. | Status quantities inconsistent. | Order status is temporarily unavailable. Quantities do not reconcile — escalate to operations. | Customer service requires trustworthy order status. |

### FR-050 — Authorized Product Substitution (F-13)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-110 | F-13 | Substitution must use only pre-approved alternate SKUs for the ordered product. | Non-approved substitute selected. | This product is not an approved substitute. Select an authorized alternate or cancel the line. | Controls acceptable replacements and margin impact. |
| VR-111 | F-13 | Substitution requires authorized approval and customer acceptance when policy requires. | Substitution without required approvals. | Product substitution requires authorized approval and customer acceptance. | Protects customer expectation and commercial policy. |

---

## Domain 6: Replenishment & Inbound Supply

### FR-051 — Generate Low-Stock and Out-of-Stock Alerts (F-20)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-112 | F-20 | Alerts must fire when ATP is at or below reorder level or when ATP is zero. | Alert missing despite threshold breach. | Low-stock condition detected. Review replenishment for this product at this location. | Timely alerts prevent preventable stockouts (BR-009). |
| VR-113 | F-20 | Duplicate active alerts for the same product-location-condition must be suppressed until resolved or acknowledged. | Multiple identical open alerts created. | An active alert already exists for this product at this location. | Reduces alert fatigue and duplicate procurement action. |

### FR-052 — Review and Acknowledge Stock Alerts (F-20)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-114 | F-20 | Dismissed or deferred alerts require documented rationale. | Alert dismissed without reason. | Provide a reason for dismissing or deferring this stock alert. | Ensures alerts drive deliberate action or accountable deferral. |
| VR-115 | F-20 | Acknowledged alerts must record action taken: requisition, transfer, or dismiss. | Acknowledgment without action category. | Select the action taken for this alert before acknowledging. | Links alert response to downstream replenishment or transfer processes. |

### FR-053 — Generate Replenishment Suggestions (F-20)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-116 | F-20 | Replenishment suggestion must consider open PO inbound quantity before recommending new purchase. | Purchase suggested when sufficient inbound supply exists. | Open purchase orders already cover this need. Review inbound supply before ordering. | Avoids duplicate procurement investment (BR-011). |
| VR-117 | F-20 | Suggested order quantity must be greater than zero and based on defined threshold parameters. | Zero or negative suggestion generated. | Replenishment suggestion cannot be calculated. Verify stock policy thresholds. | Invalid suggestions would misdirect buyers. |
| VR-118 | F-20 | Network excess must be evaluated before purchase suggestion is finalized. | Purchase suggested while transferable network stock exists without documented transfer decline. | Stock is available at other locations. Consider a transfer before purchasing. | Transfer-before-buy discipline optimizes network inventory (BR-011). |

### FR-054 — Create and Track Purchase Requisitions (F-20)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-119 | F-20 | Requisition must include product, quantity, receiving location, and business justification. | Missing mandatory requisition field. | Required requisition information is missing. Complete product, quantity, location, and justification. | Formalizes replenishment handoff with accountability. |
| VR-120 | F-20 | Requisitions for discontinued products must be blocked. | Requisition created for discontinued SKU. | Cannot requisition a discontinued product. | Enforces product lifecycle policy (BR-027). |
| VR-121 | F-20 | Requisition approval must follow purchasing authority limits. | Requisition approved by unauthorized role. | This requisition requires approval from an authorized purchasing approver. | Maintains procurement financial controls. |

### FR-055 — Track Inbound Supply Status (F-07)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-122 | F-07 | Received quantity on PO lines must not exceed ordered quantity plus approved tolerance. | Cumulative receipt exceeds allowable PO quantity. | Received quantity exceeds the purchase order limit. Resolve over-receipt before closing the PO line. | Keeps inbound tracking aligned with supplier commitment. |
| VR-123 | F-07 | Overdue PO lines must be identifiable when expected date has passed without receipt. | Overdue PO not flagged. | Purchase order is past expected delivery. Update status or follow up with supplier. | Enables proactive response to replenishment delays. |

### FR-056 — Enforce Safety Stock Protection (F-03)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-124 | F-03 | Reservations and transfers that would reduce stock below safety level must be blocked or require authorized exception. | Safety stock breached without approval. | This action would use safety stock. Authorized exception and replenishment plan required. | Safety stock protects against demand and supply variability (BR-010). |
| VR-125 | F-03 | Safety stock exception must document approver, reason, and replenishment plan. | Exception granted without required documentation. | Safety stock exception requires approver, reason, and replenishment plan. | Exceptions without recovery plan guarantee the next stockout. |

### FR-057 — Promotional Stock Readiness Review (F-25)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-126 | F-25 | Campaign readiness review requires defined target quantity by SKU, location, and campaign start date. | Readiness review without campaign targets. | Campaign stock targets are not defined. Set promotional quantities before running readiness review. | Cannot assess readiness without defined requirements. |
| VR-127 | F-25 | Promotional ring-fenced quantity must not be consumed by non-promotional orders during campaign period. | General order consumes ring-fenced stock. | This quantity is reserved for the promotion and cannot be used for standard orders. | Protects campaign supply (BR-029). |

---

## Domain 7: Network Balance & Transfers

### FR-058 — Request Inter-Location Transfers (F-08)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-128 | F-08 | Transfer request must include product, quantity, source location, destination location, and justification. | Missing mandatory transfer field. | Required transfer information is missing. Complete product, quantity, source, destination, and reason. | Incomplete requests cannot be evaluated for network impact. |
| VR-129 | F-08 | Source and destination locations must be different active locations. | Same location or inactive location selected. | Source and destination must be different active locations. | Transfers require distinct valid endpoints. |
| VR-130 | F-08 | Requested quantity must not exceed source ATP. | Transfer quantity exceeds source available stock. | Transfer quantity exceeds available stock at the source location. | Cannot transfer stock that is not available or is reserved. |

### FR-059 — Approve or Reject Transfer Requests (F-08)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-131 | F-08 | Rejection must include documented reason communicated to requester. | Transfer rejected without reason. | Provide a reason for rejecting this transfer request. | Requesters need rationale to pursue alternate replenishment paths. |
| VR-132 | F-08 | Approver must revalidate source ATP at approval time when stock may have changed since request. | Approval granted when source no longer has stock. | Source stock has changed. Revalidate availability before approving this transfer. | Prevents approval of transfers that can no longer be fulfilled. |

### FR-060 — Execute and Record Transfers (F-08)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-133 | F-08 | Dispatch quantity must not exceed approved transfer quantity. | Dispatch exceeds approval. | Dispatch quantity cannot exceed the approved transfer amount. | Execution must match authorized transfer. |
| VR-134 | F-08 | Source on-hand must decrease on dispatch and destination on-hand must increase only on verified receipt. | Destination increased before receipt or source not reduced on dispatch. | Transfer receipt must be confirmed at the destination before stock is added. | Prevents stock appearing in two places or lost in transit. |
| VR-135 | F-08 | Receipt variance at destination must trigger investigation before transfer is closed. | Transfer closed with unreconciled receipt variance. | Received quantity does not match dispatched quantity. Investigate before closing this transfer. | Maintains network accuracy and loss accountability. |

### FR-061 — Monitor In-Transit Inventory (F-08)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-136 | F-08 | In-transit quantity must be excluded from source ATP and destination on-hand until receipt confirmed. | In-transit counted as available at source or destination. | Stock in transit is not available at either location until receipt is confirmed. | Accurate availability during transfer lead time. |
| VR-137 | F-08 | Transfers exceeding defined in-transit age must be flagged as overdue. | Overdue in-transit transfer not escalated. | Transfer shipment is overdue. Investigate in-transit status. | Prevents silent loss of goods between locations. |

### FR-062 — Network Rebalancing Recommendations (F-09)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-138 | F-09 | Recommended transfer quantity must respect source minimum threshold and safety stock rules. | Recommendation would breach source minimum. | Recommended transfer would leave the source below its minimum threshold. Reduce quantity or choose another source. | Network optimization must not create new shortages (BR-012). |
| VR-139 | F-09 | Recommendations must not be generated for inactive products or locations. | Recommendation includes invalid entities. | Rebalancing recommendation includes invalid products or locations. Refresh network data. | Recommendations must reflect current operational network. |

### FR-063 — Enforce Source Location Minimum on Transfers (F-08)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-140 | F-08 | Maximum transferable quantity equals source ATP minus source minimum threshold and safety stock per policy. | Transfer approved above maximum transferable quantity. | Transfer would leave the source below its minimum stock level. Maximum transferable quantity is {maxQty}. | Protects source service level (BR-012). |
| VR-141 | F-08 | Modified transfer quantity at approval must be revalidated against source minimum. | Approved quantity exceeds allowable maximum after modification. | Approved quantity exceeds what the source can spare. Reduce transfer quantity. | Approval must respect real-time source constraints. |

---

## Domain 8: Returns Management

### FR-064 — Authorize and Record Customer Returns (F-21)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-142 | F-21 | Return authorization must link to a valid original order and return-eligible products per return policy. | Return authorized without valid order or ineligible item. | This return is not eligible. Verify the original order and return policy. | Prevents unauthorized returns and policy violations (BR-025). |
| VR-143 | F-21 | Authorized return quantity must be greater than zero and not exceed original shipped quantity for the line. | Return quantity exceeds original order line quantity. | Return quantity cannot exceed the quantity originally shipped on this order. | Protects against fraudulent or excessive return claims. |

### FR-065 — Receive and Inspect Returned Goods (F-21)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-144 | F-21 | Return receipt must match a valid, open return authorization. | Receipt against invalid or expired authorization. | Return authorization is invalid or expired. Obtain a valid authorization before receiving. | Warehouse must not accept unauthorized returns (BR-025). |
| VR-145 | F-21 | Received product must match authorized return product unless documented exception approved. | Wrong product received against authorization. | Returned product does not match the authorization. Contact customer service. | Prevents incorrect inventory and refund processing. |
| VR-146 | F-21 | Inspection outcome is required before restock or write-off disposition. | Disposition applied without inspection result. | Inspection outcome is required before restocking or writing off returned goods. | Only resalable goods re-enter sellable stock (BR-026). |

### FR-066 — Restock or Write Off Returned Inventory (F-21)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-147 | F-21 | Restock quantity plus write-off quantity must equal inspected received quantity. | Disposition quantities do not reconcile to received amount. | Restock and write-off quantities must equal the inspected return quantity. | Ensures full accountability for returned goods. |
| VR-148 | F-21 | Write-off portion requires reason code and approval per write-off policy. | Return write-off without reason or approval. | Write-off of returned goods requires a reason code and authorized approval. | Returned damaged goods follow same control as other write-offs (BR-023). |

### FR-067 — Track Return Processing Status (F-21)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-149 | F-21 | Return status inquiry requires valid return authorization or order reference. | Invalid return reference. | Return not found. Verify the return authorization or order reference. | Enables accurate customer communication. |
| VR-150 | F-21 | Displayed status must reflect current stage: authorized, in transit, received, inspecting, restocked, written off, or complete. | Status inconsistent with actual processing stage. | Return status is being updated. Refresh or contact the returns team. | Customers and CS need reliable return progress visibility. |

---

## Domain 9: Reporting & Dashboards

### FR-068 — Inventory Summary Dashboard (F-22)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-151 | F-22 | Dashboard aggregates must include only authorized locations. | Unauthorized location data in dashboard totals. | Dashboard shows data for your authorized locations only. | Executive and operational views respect access scope. |
| VR-152 | F-22 | Dashboard metrics must use current inventory balances, not stale cached totals beyond defined freshness policy. | Metrics exceed acceptable data freshness. | Dashboard data may be stale. Refresh for current inventory position. | Decisions require timely stock picture (BO-001). |

### FR-069 — Stock Movement Reports (F-22)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-153 | F-22 | Report period must have valid start and end dates with start on or before end. | Invalid report date range. | Select a valid report period. Start date must be on or before end date. | Invalid periods produce unusable movement analysis. |
| VR-154 | F-22 | Movement report must include only transaction types and locations within user authority. | Unauthorized data in exported report. | Report export excludes locations outside your access scope. | Protects sensitive operational data in exports. |

### FR-070 — Stockout and Overstock Reports (F-22)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-155 | F-22 | Stockout list must include only products where ATP is zero or below minimum sellable unit at the location. | Incorrect stockout classification. | Stockout report requires current thresholds and availability. Refresh report parameters. | Directs action to genuine availability failures. |
| VR-156 | F-22 | Overstock list must compare on-hand or ATP to defined maximum or policy threshold where configured. | Overstock shown without threshold basis. | Overstock criteria are not defined for some products. Configure thresholds or review policy. | Overstock identification requires policy reference. |

### FR-071 — Inventory Accuracy and Variance Reports (F-14)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-157 | F-14 | Accuracy rate must be calculated only from completed counts in the selected period. | Incomplete counts included in accuracy rate. | Accuracy report includes only completed counts for the selected period. | Incomplete counts distort accuracy metrics (BO-002). |
| VR-158 | F-14 | Report must exclude count lines still under investigation when calculating finalized accuracy. | Open variances counted as accurate. | Pending variances are excluded until investigation is complete. | Accuracy metrics must reflect resolved position. |

### FR-072 — Location Performance Snapshots (F-22)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-159 | F-22 | Comparison view must use consistent metric definitions and period across all locations shown. | Inconsistent metric basis between locations. | Location comparison uses inconsistent periods or definitions. Select a uniform reporting period. | Fair network comparison requires consistent measurement. |
| VR-160 | F-22 | User must have network or regional authority to view multi-location comparison. | Location-scoped user accesses network comparison. | You do not have access to network-wide location comparisons. | Restricts sensitive comparative performance data. |

### FR-073 — Inventory Performance KPIs (F-23)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-161 | F-23 | KPI calculations must use defined formulas and agreed targets from business objectives. | KPI displayed without defined target or formula. | KPI target is not configured for this metric. | KPIs without targets cannot govern performance (BO-005, BO-010). |
| VR-162 | F-23 | KPI period selection must be valid and align to available transaction history. | KPI requested for period with insufficient data. | Insufficient data to calculate this KPI for the selected period. | Prevents misleading KPIs from incomplete history. |

### FR-074 — Basic Replenishment Reporting (F-20, F-22)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-163 | F-20 | Replenishment report must show only items at or below reorder level with configured thresholds. | Items without thresholds appear as below reorder without basis. | Some products lack thresholds and are excluded from replenishment reporting. | Report must reflect policy-based replenishment signals. |
| VR-164 | F-22 | Open alert and requisition status must reconcile to current workflow state, not historical duplicates. | Report shows stale alert status. | Replenishment report refreshed to show current alert and requisition status. | Buyers need current decision information. |

### FR-075 — Inventory Valuation Summary Views (F-24)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-165 | F-24 | Valuation view access restricted to authorized finance and executive roles. | Unauthorized user accesses valuation summary. | You are not authorized to view inventory valuation. | Valuation data is financially sensitive (NFR-SEC-017). |
| VR-166 | F-24 | Valuation requires valid unit cost for each product included in the summary. | Product missing cost in valuation calculation. | Valuation incomplete. Unit cost is missing for one or more products. | Incomplete costing produces unreliable financial substantiation (BO-018). |

---

## Domain 10: Notifications & Alerts

### FR-076 — Low-Stock and Out-of-Stock Notifications (F-20, F-26)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-167 | F-26 | Notifications must be sent only when a new alert condition occurs or escalation timer expires, not on every minor stock movement. | Duplicate notifications for unchanged condition. | Alert already sent for this condition. Acknowledge or resolve the existing alert. | Prevents notification fatigue and ignored critical alerts. |
| VR-168 | F-26 | Critical out-of-stock notifications for Class A products must escalate if unacknowledged within policy timeframe. | Class A out-of-stock alert unacknowledged beyond escalation threshold. | Critical stockout alert unacknowledged. Immediate replenishment review required. | Priority SKUs require fastest response (BR-032). |

### FR-077 — Pending Approval Notifications (F-17, F-26)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-169 | F-26 | Approval notifications must identify transaction type, requester, quantity, and age. | Notification missing required context. | Approval request details are incomplete. Open the approval task for full information. | Approvers need sufficient context for timely decisions. |
| VR-170 | F-26 | Reminder notifications must fire when approval pending exceeds defined escalation age. | Stale approval without reminder. | Approval pending beyond policy timeframe. Review required items awaiting your approval. | Approval bottlenecks delay replenishment and corrections. |

### FR-078 — Transfer and Fulfillment Exception Alerts (F-13, F-26)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-171 | F-26 | Exception alerts must be generated only for documented exception types with business impact. | Alert fired without logged exception record. | Exception alert requires a recorded fulfillment or transfer exception. | Alerts must trace to actionable operational events. |
| VR-172 | F-26 | Alert recipients must be roles authorized for the affected location and process. | Alert sent to unauthorized recipient. | Alert could not be delivered. Recipient is not authorized for this location or process. | Targeted alerts reduce noise and protect data scope. |

### FR-079 — Inbound Supply Delay Notifications (F-07, F-26)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-173 | F-26 | Delay notification requires PO line past expected delivery date with outstanding quantity. | Delay alert for on-time or closed PO. | No overdue inbound supply for this notification. | Alerts must reflect genuine supply delays affecting replenishment. |
| VR-174 | F-26 | Delay notification must include product, original ETA, and outstanding quantity. | Incomplete delay notification content. | Inbound delay details are incomplete. Review purchase order status directly. | Purchasing and operations need actionable delay information. |

### FR-080 — Campaign and Launch Readiness Alerts (F-25, F-26)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-175 | F-26 | Readiness alert fires when campaign stock gap exceeds tolerance within defined pre-launch window. | Alert without configured campaign target or timeline. | Campaign readiness alert requires defined targets and launch date. | Early warning requires measurable readiness criteria (BO-024). |
| VR-176 | F-26 | Alert must identify affected SKUs, locations, gap quantity, and days until campaign start. | Incomplete readiness alert. | Campaign readiness gap detected. Review promotional stock targets before launch. | Marketing and operations need specific gap visibility. |

---

## Domain 11: User Access & Accountability

### FR-081 — Enforce Role-Based Access Control (F-27)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-177 | F-27 | Users must be authenticated before any inventory view or transaction. | Unauthenticated access attempt. | Sign in to continue. Your session has expired or you are not authenticated. | Every transaction must be attributable to an individual (NFR-SEC-001). |
| VR-178 | F-27 | Users may perform only actions permitted by their assigned role. | Action outside role permission. | You are not authorized to perform this action. | Role boundaries protect inventory integrity and segregation of duties. |

### FR-082 — Restrict Access by Location (F-27)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-179 | F-27 | Transactional users may view and transact only at assigned locations unless granted network scope. | Cross-location transaction by location-scoped user. | You are not authorized for inventory activity at this location. | Aligns access with warehouse accountability. |
| VR-180 | F-27 | Attempts to access unauthorized locations must be logged for security review. | Unauthorized access attempt not recorded. | Access denied. This attempt has been recorded. | Supports investigation of improper access attempts. |

### FR-083 — Log User Activity (F-28)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-181 | F-28 | Material inventory actions must log user, action type, timestamp, and affected entity. | Material action without activity log entry. | Action could not be completed. Activity logging is required for this operation. | Accountability and audit depend on complete activity records (BO-019). |
| VR-182 | F-28 | Activity log entries must not be altered or deleted by operational users. | User attempts to modify historical activity log. | Activity history cannot be changed. Contact an administrator or auditor for log inquiries. | Log integrity is required for audit and investigation. |

### FR-084 — Enforce Segregation of Duties (F-28)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-183 | F-28 | User may not approve a transaction they initiated where policy prohibits self-approval. | Self-approval attempted on restricted workflow. | You cannot approve a transaction you submitted. An independent approver is required. | Prevents fraud and undetected error (BR-019, SOD-003). |
| VR-184 | F-28 | Conflicting role assignments that violate segregation rules must be blocked or flagged at assignment time. | User assigned conflicting roles without exception. | This role combination violates segregation of duties policy. Adjust role assignments. | Control design must prevent inherent conflicts (SOD rules). |

### FR-085 — Manage User Accounts and Role Assignments (F-27)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-185 | F-27 | Deactivated users must not access the system or perform transactions. | Deactivated account used for login or action. | This account is deactivated. Contact your administrator for access. | Prevents orphaned access after role changes or departure. |
| VR-186 | F-27 | Each user account must map to a unique identifiable individual; shared accounts must not be used. | Shared or generic account used for transactions. | Shared accounts are not permitted. Use your individual user account. | Attribution requires unique user identity (NFR-SEC-001). |
| VR-187 | F-27 | User must have at least one role and valid location scope when assigned to transactional functions. | Transactional user without role or location. | User account is incomplete. Assign a role and location scope before granting operational access. | Incomplete provisioning causes authorization failures or excessive access. |

---

## Domain 12: Governance, Audit & Compliance

### FR-086 — Maintain Complete Audit Trail (F-29)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-188 | F-29 | Every balance-changing event must create an audit entry with before quantity, after quantity, reason, user, and timestamp. | Balance changes without audit entry. | Transaction blocked. Inventory changes must be fully auditable. | Complete audit trail is a P1 business objective (BO-019). |
| VR-189 | F-29 | Audit records must not be modified or deleted after creation. | Audit record alteration attempted. | Audit records cannot be changed or deleted. | Immutability is required for audit and dispute resolution. |

### FR-087 — Support Audit and Control Review Queries (F-29)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-190 | F-29 | Audit queries must require valid period, location scope, and auditor authorization. | Unauthorized or unbounded audit export attempted. | Audit query requires authorized access and a defined scope. | Protects sensitive audit data while supporting review efficiency. |
| VR-191 | F-29 | Exported audit evidence must match query criteria and include required fields per audit policy. | Export missing mandatory audit attributes. | Audit export is incomplete. Required audit fields are missing from the export. | Audit packages must substantiate control testing. |

### FR-088 — Detect and Record Control Policy Breaches (F-29)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-192 | F-29 | Policy breaches such as receipt without PO, self-approval, or safety stock override must be logged even when authorized exception applies. | Exception or breach not recorded. | Control exception must be documented for governance review. | Makes control weaknesses visible before audit discovery. |
| VR-193 | F-29 | Authorized exceptions must include approver, policy reference, and business justification. | Exception without required documentation. | Policy exception requires approver, policy reference, and documented reason. | Exceptions without documentation cannot be audited. |

### FR-089 — Support Financial Inventory Reconciliation (F-24)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-194 | F-24 | Period-end reconciliation export must include all adjustments and write-offs in the reporting period. | Reconciliation export omits period adjustments. | Reconciliation data is incomplete for this period. Include all adjustments before closing. | Finance reconciliation requires complete operational substantiation (BO-018). |
| VR-195 | F-24 | Reconciliation snapshot must be tied to a defined period close date and cannot span overlapping open periods. | Overlapping or open period reconciliation snapshot. | Select a closed reporting period for reconciliation snapshot. | Period boundaries must align with finance close discipline. |

### FR-090 — Support Initial Data Import (F-30)

| Validation ID | Related Feature | Validation Rule | Error Condition | User Message | Business Reason |
|---------------|-----------------|-----------------|---------------|--------------|-----------------|
| VR-196 | F-30 | Import file must include required product attributes and non-negative opening quantities for each row. | Import row missing required fields or invalid quantity. | Import row is invalid. Correct missing product fields or negative quantities before importing. | Bad cutover data embeds errors from day one (BA-16). |
| VR-197 | F-30 | Import must reject duplicate SKUs within the file and against existing catalog unless merge rules apply. | Duplicate SKU in import batch. | Duplicate SKU found in import file or catalog. Resolve duplicates before activation. | Prevents catalog fragmentation at go-live. |
| VR-198 | F-30 | Import activation requires authorized approval after validation preview. | Import activated without approver sign-off. | Initial data import requires authorized approval after validation review. | Controlled cutover protects production inventory integrity. |
| VR-199 | F-30 | Opening balance import must reference valid active locations in the network. | Import references unknown or inactive location. | Import contains invalid location references. Use active configured locations only. | Stock must be assigned to real accountable locations. |
| VR-200 | F-30 | Import must not activate operational transactions until validation errors are resolved to zero blocking errors. | Activation with unresolved blocking validation errors. | Import cannot be activated until all blocking errors are resolved. | Go-live with validation errors undermines accuracy objectives (BO-002). |

---

## Validation Rules Summary

| Domain | FR Range | Validation Rules | Rule IDs |
|--------|----------|------------------|----------|
| Master Data & Governance | FR-001 – FR-012 | 29 | VR-001 – VR-029 |
| Inbound & Receiving | FR-013 – FR-022 | 23 | VR-030 – VR-052 |
| Inventory Visibility & Status | FR-023 – FR-028 | 12 | VR-053 – VR-064 |
| Inventory Control & Accuracy | FR-029 – FR-040 | 25 | VR-065 – VR-089 |
| Order Fulfillment | FR-041 – FR-050 | 22 | VR-090 – VR-111 |
| Replenishment & Inbound Supply | FR-051 – FR-057 | 16 | VR-112 – VR-127 |
| Network Balance & Transfers | FR-058 – FR-063 | 14 | VR-128 – VR-141 |
| Returns Management | FR-064 – FR-067 | 9 | VR-142 – VR-150 |
| Reporting & Dashboards | FR-068 – FR-075 | 16 | VR-151 – VR-166 |
| Notifications & Alerts | FR-076 – FR-080 | 10 | VR-167 – VR-176 |
| User Access & Accountability | FR-081 – FR-085 | 11 | VR-177 – VR-187 |
| Governance, Audit & Compliance | FR-086 – FR-090 | 13 | VR-188 – VR-200 |
| **Total** | **90 FRs** | **200** | **VR-001 – VR-200** |

---

## Traceability Reference

| Source | Identifier |
|--------|------------|
| Functional Requirements | FR-001 – FR-090 |
| Feature Catalog | F-01 – F-30 |
| Business Rules | BR-001 – BR-032 |
| Acceptance Criteria | AC-001 – AC-090 (Validation scenarios) |
| Separation of Duties | SOD-001 – SOD-020 |

---

## Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Senior Business Analyst | | | |
| Product Owner | | | |
| QA Lead | | | |

---

*End of Validation Rules Specification*

*Document ID: SRS-VR-001 | Version 1.0 | July 5, 2026*
