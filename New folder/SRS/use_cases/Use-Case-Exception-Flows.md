# Use Case Exception Flows
## Inventory Management System

---

## Document Information

| Attribute | Detail |
|-----------|--------|
| **Document ID** | SRS-UC-004 |
| **Document Title** | Use Case Exception Flows — Inventory Management System |
| **Version** | 1.0 |
| **Status** | Draft |
| **Document Owner** | Business Analyst |
| **Source Documents** | SRS-UC-001 (Use Case Catalog), SRS-UC-002 (Use Case Main Flows), SRS-BR-001 (Business Rule Catalog) |
| **Date** | July 5, 2026 |
| **Scope** | Business exceptions only — technical infrastructure failures are out of scope |

### Purpose

This document identifies exception flows for each of the 48 use cases in the Inventory Management System. A business exception occurs when a valid business rule, authorization constraint, or operational condition prevents the main flow from completing as intended. Each exception describes how the system must respond and what business outcome results.

### Exception Legend

| Field | Description |
|-------|-------------|
| **Exception ID** | Unique identifier in format UC-XXX-EX-NN |
| **Trigger** | Business event or condition that causes the exception |
| **Failed Step** | Main flow step where processing cannot complete successfully |
| **Expected System Behavior** | Required system response to the business exception |
| **User Notification** | Message or alert presented to the affected user or role |
| **Business Outcome** | Resulting business state; transaction is blocked, deferred, or routed for resolution |

---

## Domain 1: Master Data & Governance

### UC-001 — Manage Product Master Data

#### UC-001-EX-01 — Duplicate SKU or Identifier Detected

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-001-EX-01 |
| **Trigger** | Inventory Controller submits a new or updated product record with a SKU or barcode that already exists on another active product record. |
| **Failed Step** | 3 |
| **Expected System Behavior** | System blocks save, displays the conflicting existing product record, and prevents duplicate identity creation until resolved. |
| **User Notification** | "Duplicate SKU [or identifier] detected. Product [existing SKU/name] already uses this identifier. Resolve duplicate before saving." |
| **Business Outcome** | Product master integrity is preserved; no duplicate SKU enters the catalog. Inventory Controller must merge, correct, or choose a unique identifier. |

#### UC-001-EX-02 — Required Product Attributes Missing

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-001-EX-02 |
| **Trigger** | Inventory Controller submits product record without mandatory attributes (SKU, name, unit of measure, or category). |
| **Failed Step** | 4 |
| **Expected System Behavior** | System rejects submission, highlights missing required fields, and retains entered data for correction. |
| **User Notification** | "Required fields missing: [field list]. Complete all mandatory product attributes before saving." |
| **Business Outcome** | Incomplete product records are not saved; catalog quality standards are enforced. |

#### UC-001-EX-03 — Discontinued Product Reactivation Without Authorization

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-001-EX-03 |
| **Trigger** | Inventory Controller attempts to reactivate a discontinued product to active status without Operations Director authorization. |
| **Failed Step** | 4 |
| **Expected System Behavior** | System blocks status change and routes reactivation request for management approval per governance policy. |
| **User Notification** | "Discontinued product reactivation requires Operations Director approval. Request submitted for authorization." |
| **Business Outcome** | Discontinued product status is not changed without authorized review; obsolete inventory risk is controlled. |

---

### UC-002 — Configure Inventory Locations

#### UC-002-EX-01 — Invalid Location Hierarchy

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-002-EX-01 |
| **Trigger** | Inventory Controller defines a location hierarchy that creates circular parent-child reference or assigns invalid parent location type. |
| **Failed Step** | 3 |
| **Expected System Behavior** | System rejects hierarchy assignment and displays hierarchy validation failure detail. |
| **User Notification** | "Location hierarchy is invalid: [reason]. Correct parent assignment before saving." |
| **Business Outcome** | Location network structure remains valid; stock assignment and reporting hierarchy are not corrupted. |

#### UC-002-EX-02 — Location Activation with Unverified Opening Balances

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-002-EX-02 |
| **Trigger** | Inventory Controller attempts to activate a new location for operations without verified opening stock balances where go-live policy requires them. |
| **Failed Step** | 5 |
| **Expected System Behavior** | System blocks location activation and lists products missing opening balance entry or verification sign-off. |
| **User Notification** | "Location cannot be activated. Opening stock balances are unverified for [N] products. Complete verification before go-live." |
| **Business Outcome** | Location does not go live with embedded inventory errors; cutover integrity is protected. |

#### UC-002-EX-03 — Location Closure with Remaining On-Hand Stock

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-002-EX-03 |
| **Trigger** | Inventory Controller attempts to deactivate or close a location that still holds on-hand inventory without a completed disposition plan. |
| **Failed Step** | 5 |
| **Expected System Behavior** | System blocks deactivation and displays remaining on-hand stock by product requiring disposition. |
| **User Notification** | "Location closure blocked. [N] products with remaining on-hand stock require disposition (transfer, sell-down, or write-off) before deactivation." |
| **Business Outcome** | No location is closed with stranded inventory; stock must be dispositioned per closure policy. |

---

### UC-003 — Define Stock Policies and Thresholds

#### UC-003-EX-01 — Reorder Level Below Minimum Threshold

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-003-EX-01 |
| **Trigger** | Inventory Controller sets reorder level lower than minimum stock threshold or safety stock buffer, violating stock policy consistency rules. |
| **Failed Step** | 2 |
| **Expected System Behavior** | System rejects threshold configuration and displays policy consistency violation. |
| **User Notification** | "Reorder level cannot be below minimum threshold or safety stock. Adjust values to maintain policy consistency." |
| **Business Outcome** | Stock policy remains logically consistent; replenishment alerts will trigger before minimum breach. |

#### UC-003-EX-02 — Safety Stock Override Without Authorization

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-003-EX-02 |
| **Trigger** | Inventory Controller attempts to reduce or remove safety stock below governance minimum without authorized exception. |
| **Failed Step** | 3 |
| **Expected System Behavior** | System blocks safety stock reduction and routes override request to Operations Director per BR-010. |
| **User Notification** | "Safety stock reduction requires authorized exception. Override request submitted to Operations Director." |
| **Business Outcome** | Safety stock protection is maintained; unauthorized buffer removal is prevented. |

---

### UC-004 — Classify Products by ABC Priority

#### UC-004-EX-01 — Classification Save Without Required Review Period

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-004-EX-01 |
| **Trigger** | Inventory Controller attempts bulk reclassification outside the approved periodic review window without Operations Director override. |
| **Failed Step** | 4 |
| **Expected System Behavior** | System blocks bulk classification change and requires review period confirmation or management override. |
| **User Notification** | "Bulk ABC reclassification outside review cycle requires Operations Director approval. Submit override request to proceed." |
| **Business Outcome** | Classification changes follow governance cadence; ad-hoc bulk changes require explicit authorization. |

#### UC-004-EX-02 — Inactive Product Classification Attempt

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-004-EX-02 |
| **Trigger** | Inventory Controller assigns ABC classification to an inactive or discontinued product. |
| **Failed Step** | 3 |
| **Expected System Behavior** | System blocks classification assignment for non-active products. |
| **User Notification** | "ABC classification cannot be assigned to inactive or discontinued products. Activate product or exclude from classification." |
| **Business Outcome** | Operational monitoring effort is not applied to products outside active assortment. |

---

### UC-005 — Maintain Governance Policies and Reason Codes

#### UC-005-EX-01 — Deactivate Reason Code in Active Use

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-005-EX-01 |
| **Trigger** | Inventory Controller attempts to deactivate a reason code that is mandated by an active governance policy or referenced in pending transactions. |
| **Failed Step** | 4 |
| **Expected System Behavior** | System blocks deactivation and displays dependent policies or pending transaction references. |
| **User Notification** | "Reason code cannot be deactivated. Active policy [policy name] or [N] pending transactions reference this code. Reassign dependencies first." |
| **Business Outcome** | Reason code catalog integrity is maintained; in-flight transactions retain valid reason code references. |

#### UC-005-EX-02 — Approval Threshold Policy Conflict

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-005-EX-02 |
| **Trigger** | Inventory Controller defines governance policy with approval thresholds that conflict with segregation of duties rules (e.g., same role as initiator and approver). |
| **Failed Step** | 3 |
| **Expected System Behavior** | System rejects policy configuration and identifies SoD conflict per FR-084. |
| **User Notification** | "Governance policy conflicts with segregation of duties rule [SOD-XXX]. Initiator and approver roles cannot be the same." |
| **Business Outcome** | Governance policies comply with control framework; conflicting approval rules are not activated. |

---

## Domain 2: Inbound & Receiving

### UC-006 — Place and Manage Purchase Orders

#### UC-006-EX-01 — Purchase Order for Discontinued Product

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-006-EX-01 |
| **Trigger** | Buyer adds a discontinued product line to a purchase order. |
| **Failed Step** | 3 |
| **Expected System Behavior** | System blocks line entry and prevents purchase order submission for discontinued SKU per BR-027. |
| **User Notification** | "Product [SKU/name] is discontinued. New purchase orders for this SKU are not permitted." |
| **Business Outcome** | No new procurement is created for discontinued products; obsolete inventory risk is avoided. |

#### UC-006-EX-02 — Purchase Order Submitted Without Required Approval

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-006-EX-02 |
| **Trigger** | Buyer attempts to mark purchase order as confirmed or send to supplier before Purchasing Manager approval is recorded. |
| **Failed Step** | 5 |
| **Expected System Behavior** | System maintains purchase order in pending approval status and blocks supplier commitment until approved. |
| **User Notification** | "Purchase order requires Purchasing Manager approval before confirmation. Status remains Pending Approval." |
| **Business Outcome** | Unauthorized commercial commitments are prevented; procurement controls are enforced. |

#### UC-006-EX-03 — Cancel Purchase Order with Received Goods

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-006-EX-03 |
| **Trigger** | Buyer attempts to cancel a purchase order that has partial or full goods receipt recorded. |
| **Failed Step** | 4 |
| **Expected System Behavior** | System blocks full cancellation and displays received quantities requiring receipt reversal or closure processing. |
| **User Notification** | "Purchase order cannot be cancelled. [Quantity] already received. Process receipt reversal or close remaining open lines separately." |
| **Business Outcome** | Received inventory and financial records remain consistent; cancellation does not orphan receipt data. |

---

### UC-007 — Plan Expected Inbound Deliveries

#### UC-007-EX-01 — Delivery Plan for Unapproved Purchase Order

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-007-EX-01 |
| **Trigger** | Buyer attempts to schedule inbound delivery for a purchase order not yet approved. |
| **Failed Step** | 2 |
| **Expected System Behavior** | System blocks delivery planning and indicates purchase order approval is prerequisite. |
| **User Notification** | "Inbound delivery cannot be planned. Purchase order [PO number] is not approved. Complete approval before scheduling." |
| **Business Outcome** | Receiving locations are not notified of unconfirmed supply; inbound visibility reflects authorized orders only. |

#### UC-007-EX-02 — Delivery Date Precedes Current Date

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-007-EX-02 |
| **Trigger** | Buyer enters expected delivery date in the past without documented receipt or correction context. |
| **Failed Step** | 2 |
| **Expected System Behavior** | System rejects past-date entry for future delivery planning and prompts correction or receipt action instead. |
| **User Notification** | "Expected delivery date cannot be in the past for open orders. Update to future date or process goods receipt if already delivered." |
| **Business Outcome** | Inbound schedule data remains accurate for replenishment and receiving planning. |

---

### UC-008 — Receive and Verify Supplier Goods

#### UC-008-EX-01 — Receipt Without Valid Purchase Order Reference

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-008-EX-01 |
| **Trigger** | Receiving Clerk attempts to receive supplier goods without matching purchase order reference and without approved ad-hoc receipt authorization per BR-007. |
| **Failed Step** | 2 |
| **Expected System Behavior** | System blocks receipt processing and requires valid PO reference or ad-hoc authorization before proceeding. |
| **User Notification** | "Supplier receipt requires valid purchase order reference or approved ad-hoc receipt authorization. Cannot accept goods without authorization." |
| **Business Outcome** | Unauthorized inbound supply is rejected; financial and procurement controls are preserved. |

#### UC-008-EX-02 — Minimum Remaining Shelf Life Not Met

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-008-EX-02 |
| **Trigger** | Receiving Clerk verifies shelf-life product with remaining shelf life below minimum policy threshold at receipt per BR-016. |
| **Failed Step** | 4 |
| **Expected System Behavior** | System blocks acceptance into sellable inventory and routes to discrepancy disposition workflow. |
| **User Notification** | "Product [SKU] does not meet minimum remaining shelf life requirement. Receipt blocked. Document discrepancy for supplier resolution." |
| **Business Outcome** | Short-dated product is not accepted into sellable stock; supplier accountability is preserved. |

#### UC-008-EX-03 — Lot or Batch Not Captured for Traceable Product

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-008-EX-03 |
| **Trigger** | Receiving Clerk attempts to confirm receipt for a traceable product without entering required lot or batch identity per BR-017. |
| **Failed Step** | 4 |
| **Expected System Behavior** | System blocks receipt confirmation until lot or batch is recorded. |
| **User Notification** | "Lot/batch number is required for traceable product [SKU]. Enter lot identity before completing receipt." |
| **Business Outcome** | Traceability data is captured at point of entry; recall and quality investigation capability is maintained. |

---

### UC-009 — Document and Resolve Receipt Discrepancies

#### UC-009-EX-01 — Discrepancy Accepted Without Documentation

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-009-EX-01 |
| **Trigger** | Receiving Clerk attempts to complete receipt with quantity variance but without mandatory discrepancy documentation per BR-006. |
| **Failed Step** | 2 |
| **Expected System Behavior** | System blocks receipt completion and requires discrepancy type, variance quantity, and reason code. |
| **User Notification** | "Receipt discrepancy must be documented before acceptance. Enter discrepancy type, variance, and reason code." |
| **Business Outcome** | Supplier accountability evidence is captured at receipt; undocumented variances are prevented. |

#### UC-009-EX-02 — Discrepancy Resolution Exceeds Approval Authority

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-009-EX-02 |
| **Trigger** | Warehouse Manager attempts to approve receipt discrepancy resolution exceeding defined tolerance or value threshold without independent approver per SOD-007. |
| **Failed Step** | 4 |
| **Expected System Behavior** | System routes discrepancy resolution to authorized approver and blocks completion pending escalation. |
| **User Notification** | "Discrepancy resolution exceeds your approval authority. Escalated to [approver role] for independent approval." |
| **Business Outcome** | Material receipt variances receive proportional oversight; receiving clerk cannot self-approve beyond-tolerance discrepancies. |

---

### UC-010 — Perform Stock Put-Away

#### UC-010-EX-01 — Put-Away Before Receipt Verification Complete

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-010-EX-01 |
| **Trigger** | Warehouse Staff attempts put-away for stock that has not completed goods receipt verification per BR-004. |
| **Failed Step** | 1 |
| **Expected System Behavior** | System excludes unverified receipts from put-away queue and displays verification prerequisite status. |
| **User Notification** | "Put-away not available. Goods receipt [reference] requires verification completion before put-away." |
| **Business Outcome** | Unverified stock does not enter storage or availability; inventory accuracy is protected at point of entry. |

#### UC-010-EX-02 — Put-Away to Unauthorized Storage Location

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-010-EX-02 |
| **Trigger** | Warehouse Staff confirms put-away to a storage location not authorized for the product category or location type. |
| **Failed Step** | 3 |
| **Expected System Behavior** | System rejects location assignment and presents list of authorized storage locations. |
| **User Notification** | "Storage location [location] is not authorized for product category [category]. Select an authorized location." |
| **Business Outcome** | Stock is stored only in appropriate locations; retrieval efficiency and product handling rules are maintained. |

---

### UC-011 — Receive Return and Non-PO Inbound Stock

#### UC-011-EX-01 — Return Received Without Authorization

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-011-EX-01 |
| **Trigger** | Receiving Clerk attempts to receive customer return without valid return authorization reference per BR-025. |
| **Failed Step** | 2 |
| **Expected System Behavior** | System blocks return receipt and requires valid return authorization before acceptance. |
| **User Notification** | "Return receipt blocked. Valid return authorization is required. Contact Customer Service to issue authorization." |
| **Business Outcome** | Unauthorized returns are not accepted; warehouse has no unlinked inbound goods. |

#### UC-011-EX-02 — Ad-Hoc Receipt Without Pre-Approval

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-011-EX-02 |
| **Trigger** | Receiving Clerk attempts ad-hoc non-PO receipt without valid pre-approved authorization reference. |
| **Failed Step** | 2 |
| **Expected System Behavior** | System blocks ad-hoc receipt and requires authorization reference from authorized approver. |
| **User Notification** | "Ad-hoc receipt requires pre-approved authorization reference. Obtain approval before receiving goods." |
| **Business Outcome** | Non-standard inbound is controlled; unauthorized ad-hoc supply entry is prevented. |

---

## Domain 3: Inventory Visibility & Status

### UC-012 — Monitor Inventory Status

#### UC-012-EX-01 — Insufficient Access to Location Data

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-012-EX-01 |
| **Trigger** | Inventory Controller attempts to view inventory status for a location outside assigned access scope per FR-082. |
| **Failed Step** | 2 |
| **Expected System Behavior** | System restricts view to authorized locations only and does not display restricted location data. |
| **User Notification** | "Access denied for location [location name]. You do not have visibility permission for this site." |
| **Business Outcome** | Location-scoped access is enforced; unauthorized network visibility is prevented. |

---

### UC-013 — Inquire Inventory Availability

#### UC-013-EX-01 — Product Not Found

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-013-EX-01 |
| **Trigger** | Sales Representative searches for a product SKU, name, or barcode that does not exist in the product master. |
| **Failed Step** | 2 |
| **Expected System Behavior** | System returns no-match result and suggests similar products if available. |
| **User Notification** | "No product found matching '[search term]'. Verify SKU, name, or barcode. Similar products: [list if any]." |
| **Business Outcome** | Sales representative is informed that product is not in catalog; customer cannot be promised unavailable SKU. |

#### UC-013-EX-02 — Inactive Product Availability Inquiry

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-013-EX-02 |
| **Trigger** | Sales Representative requests availability for an inactive or discontinued product. |
| **Failed Step** | 3 |
| **Expected System Behavior** | System displays product status as inactive or discontinued and shows remaining ATP if any with sell restriction indicator. |
| **User Notification** | "Product [SKU] is [inactive/discontinued]. Not available for new sales commitment. Remaining ATP: [quantity] (sell-through only)." |
| **Business Outcome** | Sales team cannot commit new orders against discontinued assortment without explicit visibility of status. |

---

## Domain 4: Inventory Control & Accuracy

### UC-014 — Perform Cycle Count

#### UC-014-EX-01 — Count Entry for Unassigned Product-Location

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-014-EX-01 |
| **Trigger** | Warehouse Staff attempts to enter cycle count for a product-location not on the assigned count schedule. |
| **Failed Step** | 2 |
| **Expected System Behavior** | System blocks unscheduled count entry unless ad-hoc count authorization is granted by Warehouse Manager. |
| **User Notification** | "Product-location not on your assigned count schedule. Request ad-hoc count authorization from Warehouse Manager." |
| **Business Outcome** | Count program integrity is maintained; uncontrolled counts do not disrupt scheduled accuracy program. |

#### UC-014-EX-02 — Count Submitted with Zero Quantity for Active SKU

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-014-EX-02 |
| **Trigger** | Warehouse Staff submits zero count for a product-location with recent movement history or open reservations. |
| **Failed Step** | 4 |
| **Expected System Behavior** | System flags zero-count confirmation prompt and requires explicit confirmation before accepting. |
| **User Notification** | "Zero count submitted for active SKU with recent activity. Confirm zero count is correct or re-count before submitting." |
| **Business Outcome** | Potentially erroneous zero counts receive additional verification before variance processing. |

---

### UC-015 — Conduct Full Physical Inventory Count

#### UC-015-EX-01 — Movement Attempted During Inventory Freeze

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-015-EX-01 |
| **Trigger** | Any user attempts receiving, shipping, transfer, or adjustment at a location under physical inventory freeze per BR-024. |
| **Failed Step** | 3 |
| **Expected System Behavior** | System blocks inventory movement transactions for frozen location and displays freeze status. |
| **User Notification** | "Location [location] is under physical inventory freeze. [Transaction type] is suspended until count is completed." |
| **Business Outcome** | Count snapshot integrity is preserved; movements do not invalidate wall-to-wall count. |

#### UC-015-EX-02 — Count Close with Uncounted Zones

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-015-EX-02 |
| **Trigger** | Inventory Controller attempts to close full physical count session with uncounted zones or products remaining. |
| **Failed Step** | 5 |
| **Expected System Behavior** | System blocks count close and displays list of uncounted assignments. |
| **User Notification** | "Physical count cannot be closed. [N] zones/products remain uncounted. Complete all assignments or document approved exclusions." |
| **Business Outcome** | Incomplete count is not finalized; accuracy baseline is not established with gaps. |

---

### UC-016 — Investigate and Approve Count Variances

#### UC-016-EX-01 — Counter Attempts to Approve Own Count Variance

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-016-EX-01 |
| **Trigger** | Warehouse Staff who performed the count attempts to approve the resulting variance adjustment per BR-019 and SOD-003. |
| **Failed Step** | 4 |
| **Expected System Behavior** | System blocks self-approval and routes variance to independent approver (Inventory Controller or Warehouse Manager if not counter). |
| **User Notification** | "You cannot approve adjustments from your own count. Variance routed to [approver role] for independent review." |
| **Business Outcome** | Segregation of duties is enforced; count accuracy oversight remains independent. |

#### UC-016-EX-02 — Variance Approved Without Investigation Notes

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-016-EX-02 |
| **Trigger** | Warehouse Manager attempts to approve count variance without documented investigation per BR-022. |
| **Failed Step** | 3 |
| **Expected System Behavior** | System blocks approval until mandatory investigation notes are entered. |
| **User Notification** | "Investigation notes are required before variance approval. Document root cause analysis or investigation effort." |
| **Business Outcome** | Adjustments are not applied without investigation; recurring variance root causes can be identified. |

---

### UC-017 — Process Stock Adjustments

#### UC-017-EX-01 — Adjustment Without Mandatory Reason Code

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-017-EX-01 |
| **Trigger** | Warehouse Manager submits stock adjustment without selecting a reason code per BR-020. |
| **Failed Step** | 3 |
| **Expected System Behavior** | System blocks adjustment submission until reason code is selected. |
| **User Notification** | "Reason code is mandatory for all adjustments. Select a reason code before submitting." |
| **Business Outcome** | All adjustments are analytically categorized; shrinkage and loss analysis integrity is maintained. |

#### UC-017-EX-02 — Adjustment Exceeds Approval Threshold

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-017-EX-02 |
| **Trigger** | Warehouse Manager submits adjustment exceeding defined quantity or value threshold without independent approver per BR-021. |
| **Failed Step** | 4 |
| **Expected System Behavior** | System routes adjustment to Operations Director or Inventory Controller and blocks application pending approval. |
| **User Notification** | "Adjustment exceeds approval threshold. Submitted to [approver role] for independent authorization." |
| **Business Outcome** | Material adjustments receive proportional oversight; high-impact changes are not self-approved. |

#### UC-017-EX-03 — Adjustment Would Breach Safety Stock Floor

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-017-EX-03 |
| **Trigger** | Decrease adjustment would reduce on-hand below safety stock buffer without authorized exception per BR-010. |
| **Failed Step** | 2 |
| **Expected System Behavior** | System warns of safety stock breach and requires authorized override or reduced adjustment quantity. |
| **User Notification** | "Adjustment would reduce stock below safety stock level. Reduce adjustment quantity or obtain authorized safety stock override." |
| **Business Outcome** | Safety stock protection is maintained; unauthorized buffer consumption is prevented. |

---

### UC-018 — Authorize and Process Inventory Write-Offs

#### UC-018-EX-01 — Write-Off Without Supporting Documentation

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-018-EX-01 |
| **Trigger** | Operations Director attempts to authorize write-off without attached evidence or documentation per BR-023. |
| **Failed Step** | 3 |
| **Expected System Behavior** | System blocks write-off authorization until supporting documentation is attached. |
| **User Notification** | "Write-off authorization requires supporting documentation. Attach evidence before approving." |
| **Business Outcome** | Write-offs are auditable; undocumented value removal is prevented. |

#### UC-018-EX-02 — Write-Off Exceeds Authorized Quantity

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-018-EX-02 |
| **Trigger** | Write-off request quantity exceeds verified on-hand or quarantined quantity at location. |
| **Failed Step** | 5 |
| **Expected System Behavior** | System blocks write-off execution and displays available quantity for write-off. |
| **User Notification** | "Write-off quantity [requested] exceeds available on-hand [available] at location [location]. Adjust write-off quantity." |
| **Business Outcome** | Inventory cannot be written off below zero; record accuracy is maintained. |

---

### UC-019 — Manage Quarantine and Hold Stock

#### UC-019-EX-01 — Quarantined Stock Included in Reservation Attempt

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-019-EX-01 |
| **Trigger** | System or user workflow attempts to reserve quarantined stock for customer order per BR-013. |
| **Failed Step** | 4 |
| **Expected System Behavior** | System excludes quarantined quantity from reservation eligibility and displays quarantine hold reason. |
| **User Notification** | "Quantity [N] is quarantined and not available for reservation. ATP excludes quarantined stock." |
| **Business Outcome** | Defective or held stock is not committed to customers; sellable availability remains accurate. |

#### UC-019-EX-02 — Bonded Stock Released Without Customs Clearance

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-019-EX-02 |
| **Trigger** | Warehouse Manager attempts to release bonded inventory to sellable status without documented customs clearance per BR-030. |
| **Failed Step** | 1 |
| **Expected System Behavior** | System blocks release and maintains bonded hold status until clearance reference is recorded. |
| **User Notification** | "Bonded inventory cannot be released without customs clearance. Record clearance reference before release." |
| **Business Outcome** | Regulatory compliance is maintained; bonded goods are not released into domestic commerce prematurely. |

---

### UC-020 — Analyze Shrinkage, Loss, and Obsolete Stock

#### UC-020-EX-01 — Analysis Period Exceeds Data Retention for Reason Codes

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-020-EX-01 |
| **Trigger** | Inventory Controller requests shrinkage analysis for a period where historical reason codes were not consistently recorded (pre-go-live or legacy data gap). |
| **Failed Step** | 2 |
| **Expected System Behavior** | System displays analysis with data completeness warning and excludes periods below minimum reason code compliance threshold. |
| **User Notification** | "Shrinkage analysis for [period] has incomplete reason code data ([X]% compliance). Results may not be reliable. Adjust period or scope." |
| **Business Outcome** | User is informed of data quality limitations; decisions are not made on unreliable historical analysis. |

---

## Domain 5: Order Fulfillment

### UC-021 — Confirm Order Availability

#### UC-021-EX-01 — Insufficient ATP for Order Line

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-021-EX-01 |
| **Trigger** | Available-to-promise quantity is less than ordered quantity at all fulfillment locations per BR-001. |
| **Failed Step** | 2 |
| **Expected System Behavior** | System displays ATP shortfall by line and blocks full availability confirmation. |
| **User Notification** | "Insufficient ATP for line [SKU]: ordered [N], available [M]. Confirm partial availability or revise order quantity." |
| **Business Outcome** | Customer cannot be promised unavailable quantity; overselling is prevented at confirmation stage. |

#### UC-021-EX-02 — Promotional Stock Ring-Fence Blocks General Order

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-021-EX-02 |
| **Trigger** | Order line draws from promotional ring-fenced stock reserved for campaign without commercial leadership approval per BR-029. |
| **Failed Step** | 2 |
| **Expected System Behavior** | System excludes ring-fenced promotional quantity from ATP available for non-promotional orders. |
| **User Notification** | "Available ATP excludes [N] units ring-fenced for campaign [campaign name]. Marketing Manager approval required to consume promotional stock." |
| **Business Outcome** | Campaign inventory is protected; promotional commitments are not consumed by general orders. |

---

### UC-022 — Reserve Inventory for Confirmed Orders

#### UC-022-EX-01 — ATP Changed Since Availability Confirmation

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-022-EX-01 |
| **Trigger** | ATP at fulfillment location has decreased since availability confirmation due to concurrent reservation or adjustment. |
| **Failed Step** | 2 |
| **Expected System Behavior** | System blocks full reservation and displays current ATP versus previously confirmed quantity. |
| **User Notification** | "ATP has changed since availability check. Confirmed: [N], current ATP: [M]. Re-confirm availability or reserve partial quantity." |
| **Business Outcome** | Reservation reflects current stock position; double-allocation from stale availability data is prevented. |

#### UC-022-EX-02 — Reservation Exceeds Location ATP

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-022-EX-02 |
| **Trigger** | Customer Service Representative attempts to reserve quantity exceeding ATP at selected fulfillment location. |
| **Failed Step** | 3 |
| **Expected System Behavior** | System blocks over-reservation and displays maximum reservable quantity. |
| **User Notification** | "Reservation quantity [N] exceeds available ATP [M] at [location]. Reduce reservation or select alternate location." |
| **Business Outcome** | Reserved quantity never exceeds available stock; ATP integrity is maintained. |

---

### UC-023 — Release Inventory Reservations

#### UC-023-EX-01 — Release Attempt on Shipped or Picked Order

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-023-EX-01 |
| **Trigger** | Customer Service Representative attempts to release reservation for order lines already picked, packed, or shipped. |
| **Failed Step** | 2 |
| **Expected System Behavior** | System blocks reservation release for fulfilled lines and displays current fulfillment status. |
| **User Notification** | "Reservation cannot be released. Order line [SKU] is [picked/shipped]. Process return or cancellation workflow instead." |
| **Business Outcome** | Physical fulfillment state and reservation state remain consistent; improper ATP restoration is prevented. |

---

### UC-024 — Pick, Pack, and Ship Orders

#### UC-024-EX-01 — Shipment Confirmed Without Pick Verification

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-024-EX-01 |
| **Trigger** | Warehouse Picker / Packer attempts to confirm shipment before all order lines are pick-verified per BR-003. |
| **Failed Step** | 5 |
| **Expected System Behavior** | System blocks shipment confirmation and lists unverified pick lines. |
| **User Notification** | "Shipment cannot be confirmed. [N] lines require pick verification. Complete verification before shipping." |
| **Business Outcome** | Inventory is not deducted and orders are not marked shipped until picks are verified. |

#### UC-024-EX-02 — Pick Quantity Exceeds Reserved Quantity

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-024-EX-02 |
| **Trigger** | Warehouse Picker / Packer attempts to pick quantity greater than reserved quantity for order line. |
| **Failed Step** | 3 |
| **Expected System Behavior** | System blocks over-pick and displays reserved quantity limit. |
| **User Notification** | "Pick quantity [N] exceeds reserved quantity [M] for order line [SKU]. Adjust pick to reserved amount." |
| **Business Outcome** | Fulfillment does not exceed committed reservation; unreserved stock is not shipped. |

#### UC-024-EX-03 — FEFO/FIFO Rotation Violation

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-024-EX-03 |
| **Trigger** | Warehouse Picker / Packer scans lot or batch that violates FEFO or FIFO rotation rules per BR-014 and BR-015. |
| **Failed Step** | 3 |
| **Expected System Behavior** | System warns of rotation violation and directs picker to correct lot or batch with earlier expiry or receipt date. |
| **User Notification** | "Rotation violation: earlier [expiry/receipt date] stock exists at [location]. Pick lot [correct lot] first." |
| **Business Outcome** | Product rotation policy is enforced; expired or aged stock write-off risk is reduced. |

---

### UC-025 — Handle Partial Fulfillment and Backorders

#### UC-025-EX-01 — Backorder Recorded Without Customer Acknowledgment

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-025-EX-01 |
| **Trigger** | Customer Service Representative attempts to create backorder without recorded customer acknowledgment per BR-028. |
| **Failed Step** | 3 |
| **Expected System Behavior** | System blocks backorder creation until customer acknowledgment is captured. |
| **User Notification** | "Backorder requires customer acknowledgment. Record customer acceptance of delay terms before proceeding." |
| **Business Outcome** | Backorders are mutual agreements; silent backorders that damage customer trust are prevented. |

#### UC-025-EX-02 — Zero ATP for Immediate Partial Fulfillment

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-025-EX-02 |
| **Trigger** | Customer accepts partial fulfillment but zero ATP is available for any immediate shipment quantity. |
| **Failed Step** | 4 |
| **Expected System Behavior** | System blocks partial fulfillment reservation and offers full backorder or order hold options only. |
| **User Notification** | "No ATP available for immediate partial fulfillment. Create full backorder or hold order until supply arrives." |
| **Business Outcome** | Customer is not promised immediate shipment when no stock exists; commitment aligns with availability. |

---

### UC-026 — Handle Outbound Fulfillment Exceptions

#### UC-026-EX-01 — Unauthorized Product Substitution Attempted

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-026-EX-01 |
| **Trigger** | Warehouse Manager attempts substitution with a product not on the authorized substitute list per FR-050. |
| **Failed Step** | 3 |
| **Expected System Behavior** | System blocks unauthorized substitution and displays approved substitute products if any. |
| **User Notification** | "Product [SKU] is not an authorized substitute for [original SKU]. Select approved substitute or escalate to Customer Service." |
| **Business Outcome** | Customers receive only approved equivalent products; unauthorized substitutions are prevented. |

---

### UC-027 — View Order Fulfillment Status

#### UC-027-EX-01 — Order Not Found

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-027-EX-01 |
| **Trigger** | Customer Service Representative searches for order number or customer reference that does not exist in the system. |
| **Failed Step** | 2 |
| **Expected System Behavior** | System returns no-match result with search criteria confirmation. |
| **User Notification** | "No order found for '[search term]'. Verify order number or customer reference." |
| **Business Outcome** | User is informed no matching order exists; incorrect status information is not presented. |

---

## Domain 6: Replenishment & Inbound Supply

### UC-028 — Review Low-Stock and Out-of-Stock Alerts

#### UC-028-EX-01 — Alert for Product with Open Purchase Order

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-028-EX-01 |
| **Trigger** | Purchasing Manager reviews low-stock alert for product with sufficient inbound supply on open approved purchase order arriving within lead time. |
| **Failed Step** | 3 |
| **Expected System Behavior** | System displays alert with inbound supply context and suggests alert acknowledgment with inbound coverage note. |
| **User Notification** | "Low-stock alert: [SKU]. Open PO [number] with [quantity] expected [date] may resolve condition. Review before initiating new procurement." |
| **Business Outcome** | Duplicate procurement is avoided; alert response considers existing inbound supply. |

---

### UC-029 — Plan Replenishment and Create Purchase Requisitions

#### UC-029-EX-01 — Requisition for Discontinued Product

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-029-EX-01 |
| **Trigger** | Buyer attempts to create purchase requisition for discontinued product per BR-027. |
| **Failed Step** | 3 |
| **Expected System Behavior** | System blocks requisition creation for discontinued SKU. |
| **User Notification** | "Purchase requisition blocked. Product [SKU] is discontinued and cannot be reordered." |
| **Business Outcome** | Replenishment does not recreate obsolete inventory. |

#### UC-029-EX-02 — Network Stock Available, Purchase Not Required

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-029-EX-02 |
| **Trigger** | Buyer attempts to create purchase requisition when network check confirms excess stock at another location per BR-011. |
| **Failed Step** | 2 |
| **Expected System Behavior** | System warns of network excess and recommends transfer before purchase; requires documented override to proceed with purchase. |
| **User Notification** | "Network check: [N] units excess at [source location]. Transfer recommended before new purchase. Override required to proceed with requisition." |
| **Business Outcome** | Transfer-before-buy discipline is enforced; unnecessary procurement and network imbalance are prevented. |

---

### UC-030 — Track Inbound Supply Status

#### UC-030-EX-01 — Purchase Order Fully Received, Status Update Attempted

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-030-EX-01 |
| **Trigger** | Buyer attempts to update delivery status on a purchase order already fully received and closed. |
| **Failed Step** | 3 |
| **Expected System Behavior** | System displays closed status and prevents delivery schedule modification. |
| **User Notification** | "Purchase order [number] is fully received and closed. Delivery status cannot be modified." |
| **Business Outcome** | Historical inbound records are not altered after completion; data integrity is maintained. |

---

## Domain 7: Network Balance & Transfers

### UC-031 — Request Inter-Location Stock Transfer

#### UC-031-EX-01 — Transfer Would Breach Source Minimum Threshold

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-031-EX-01 |
| **Trigger** | Requested transfer quantity would reduce source location below its minimum threshold per BR-012. |
| **Failed Step** | 2 |
| **Expected System Behavior** | System blocks transfer request submission and displays maximum transferable quantity. |
| **User Notification** | "Transfer blocked. Requested quantity would breach source minimum threshold at [location]. Maximum transferable: [N] units." |
| **Business Outcome** | Source location service level is protected; transfer does not create shortage at sending site. |

#### UC-031-EX-02 — Insufficient ATP at Source Location

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-031-EX-02 |
| **Trigger** | Requested transfer quantity exceeds available ATP at source location (stock reserved or quarantined). |
| **Failed Step** | 2 |
| **Expected System Behavior** | System blocks transfer request and displays ATP breakdown (on-hand, reserved, quarantined, available). |
| **User Notification** | "Insufficient ATP at source [location]. Requested: [N], available: [M]. Reduce quantity or select alternate source." |
| **Business Outcome** | Transfer request reflects actually available stock; committed or held stock is not double-allocated. |

---

### UC-032 — Approve or Reject Transfer Requests

#### UC-032-EX-01 — Approver Is Transfer Requester

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-032-EX-01 |
| **Trigger** | Operations Director who submitted the transfer request attempts to approve the same request per SOD-006. |
| **Failed Step** | 3 |
| **Expected System Behavior** | System blocks self-approval and routes to alternate authorized approver (COO or designated delegate). |
| **User Notification** | "You cannot approve your own transfer request. Routed to [alternate approver] per segregation of duties." |
| **Business Outcome** | Transfer authorization remains independent; self-approved transfers are prevented. |

---

### UC-033 — Execute and Record Inter-Location Transfer

#### UC-033-EX-01 — Dispatch Exceeds Approved Transfer Quantity

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-033-EX-01 |
| **Trigger** | Warehouse Staff attempts to dispatch quantity greater than approved transfer quantity. |
| **Failed Step** | 3 |
| **Expected System Behavior** | System blocks over-dispatch and displays approved transfer quantity. |
| **User Notification** | "Dispatch quantity [N] exceeds approved transfer [M]. Adjust dispatch to approved amount." |
| **Business Outcome** | Physical movement matches authorized transfer; unauthorized stock movement is prevented. |

#### UC-033-EX-02 — Receipt Quantity Exceeds Dispatched Quantity

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-033-EX-02 |
| **Trigger** | Destination Warehouse Staff attempts to receive quantity greater than dispatched in-transit quantity. |
| **Failed Step** | 4 |
| **Expected System Behavior** | System blocks over-receipt and displays expected in-transit quantity. |
| **User Notification** | "Receipt quantity [N] exceeds in-transit quantity [M]. Confirm dispatch record or document variance." |
| **Business Outcome** | Transfer receipt matches dispatch; inventory inflation at destination is prevented. |

---

### UC-034 — Analyze and Recommend Network Rebalancing

#### UC-034-EX-01 — No Actionable Imbalance Identified

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-034-EX-01 |
| **Trigger** | Operations Director runs network rebalancing analysis but no location pairs meet minimum imbalance threshold for recommendation. |
| **Failed Step** | 2 |
| **Expected System Behavior** | System displays analysis complete with no recommendations and current network balance summary. |
| **User Notification** | "Network rebalancing analysis complete. No transfer recommendations — all locations within balance tolerance." |
| **Business Outcome** | Operations confirms no rebalancing action is needed; unnecessary transfers are avoided. |

---

## Domain 8: Returns Management

### UC-035 — Authorize and Record Customer Returns

#### UC-035-EX-01 — Return Outside Policy Window

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-035-EX-01 |
| **Trigger** | Customer Service Representative attempts return authorization for order line outside defined return policy time window. |
| **Failed Step** | 3 |
| **Expected System Behavior** | System blocks standard return authorization and routes to management override workflow if applicable. |
| **User Notification** | "Return outside policy window ([N] days). Standard authorization blocked. Submit management override request if applicable." |
| **Business Outcome** | Return policy is enforced; unauthorized returns outside policy require explicit management exception. |

#### UC-035-EX-02 — Return Quantity Exceeds Original Order Quantity

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-035-EX-02 |
| **Trigger** | Customer Service Representative requests return quantity greater than originally ordered or previously returned quantity. |
| **Failed Step** | 2 |
| **Expected System Behavior** | System blocks excess return authorization and displays maximum returnable quantity. |
| **User Notification** | "Return quantity [N] exceeds returnable amount [M] for order line [SKU]. Adjust to eligible quantity." |
| **Business Outcome** | Return authorization does not exceed commercial transaction scope; fraudulent or erroneous returns are limited. |

---

### UC-036 — Receive, Inspect, and Disposition Returned Goods

#### UC-036-EX-01 — Return Quantity Exceeds Authorization

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-036-EX-01 |
| **Trigger** | Receiving Clerk attempts to receive return quantity exceeding return authorization per line. |
| **Failed Step** | 2 |
| **Expected System Behavior** | System blocks excess receipt and displays authorized return quantity. |
| **User Notification** | "Received quantity [N] exceeds authorized return [M]. Accept only authorized quantity or obtain authorization amendment." |
| **Business Outcome** | Physical return receipt matches authorization; unauthorized excess goods are not accepted. |

#### UC-036-EX-02 — Restock Attempt on Failed Inspection

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-036-EX-02 |
| **Trigger** | Receiving Clerk attempts to disposition returned goods as restock when inspection outcome is damaged or defective per BR-026. |
| **Failed Step** | 4 |
| **Expected System Behavior** | System blocks restock disposition and requires quarantine or write-off disposition for failed inspection. |
| **User Notification** | "Restock not permitted. Inspection outcome: [damaged/defective]. Select quarantine or write-off disposition." |
| **Business Outcome** | Non-resalable returns do not re-enter sellable inventory; customer quality standards are protected. |

---

## Domain 9: Reporting, Performance & Financial Alignment

### UC-037 — Review Inventory Dashboards and Operational Reports

#### UC-037-EX-01 — Report Generation Exceeds Authorized Data Scope

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-037-EX-01 |
| **Trigger** | Operations Director attempts to generate location performance report including locations outside authorized visibility scope. |
| **Failed Step** | 3 |
| **Expected System Behavior** | System generates report for authorized locations only and notes excluded locations. |
| **User Notification** | "Report generated for authorized locations only. [N] locations excluded due to access restrictions." |
| **Business Outcome** | Reporting respects location-scoped access; unauthorized data is not disclosed in reports. |

---

### UC-038 — Review Inventory Performance KPIs

#### UC-038-EX-01 — KPI Data Incomplete for Selected Period

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-038-EX-01 |
| **Trigger** | Chief Executive Officer selects KPI period where baseline data or location rollout was incomplete (e.g., pre-go-live or partial network adoption). |
| **Failed Step** | 2 |
| **Expected System Behavior** | System displays KPI values with data completeness indicator and flags metrics with insufficient coverage. |
| **User Notification** | "KPI data for [period] is incomplete ([X]% network coverage). Metrics marked with data quality warning should be interpreted with caution." |
| **Business Outcome** | Executive is not misled by KPIs based on incomplete data; governance decisions account for data maturity. |

---

### UC-039 — Reconcile Inventory Valuation with Finance

#### UC-039-EX-01 — Valuation Variance Exceeds Tolerance

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-039-EX-01 |
| **Trigger** | Operational inventory valuation differs from general ledger balance by more than defined reconciliation tolerance (target ≤2% per BO-18). |
| **Failed Step** | 3 |
| **Expected System Behavior** | System flags reconciliation as out of tolerance and requires documented variance investigation before close. |
| **User Notification** | "Reconciliation variance [X]% exceeds tolerance [Y]%. Investigation required before period close. Drill down to contributing transactions." |
| **Business Outcome** | Material valuation variances are investigated; month-end close does not proceed without resolution or documented exception. |

#### UC-039-EX-02 — Consignment Stock Included in Owned Valuation

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-039-EX-02 |
| **Trigger** | Finance Manager reconciliation includes consignment inventory in owned valuation calculation per BR-031. |
| **Failed Step** | 3 |
| **Expected System Behavior** | System separates consignment stock from owned valuation and displays consignment quantity excluded from GL comparison. |
| **User Notification** | "Consignment stock [N] units ([value]) excluded from owned valuation per ownership policy. Adjust reconciliation scope." |
| **Business Outcome** | Financial reconciliation reflects correct ownership; consignment stock does not inflate owned asset valuation. |

---

## Domain 10: Commercial Alignment & Governance

### UC-040 — Confirm Promotional and Launch Stock Readiness

#### UC-040-EX-01 — Insufficient Ring-Fenced Stock for Campaign

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-040-EX-01 |
| **Trigger** | Ring-fenced promotional stock plus expected inbound supply is insufficient to meet campaign requirement by start date. |
| **Failed Step** | 3 |
| **Expected System Behavior** | System displays readiness status as Not Ready and quantifies shortfall by product. |
| **User Notification** | "Campaign readiness: NOT READY. Shortfall of [N] units for [SKU] before [campaign date]. Escalate to Purchasing and Operations." |
| **Business Outcome** | Marketing cannot confirm launch readiness; campaign commitment is blocked until supply gap is resolved. |

#### UC-040-EX-02 — Campaign Readiness Confirmation Without Inbound Coverage

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-040-EX-02 |
| **Trigger** | Marketing Manager attempts unconditional readiness confirmation when current ring-fenced stock is insufficient and inbound supply is not confirmed before campaign date. |
| **Failed Step** | 4 |
| **Expected System Behavior** | System blocks unconditional confirmation and requires conditional confirmation with documented inbound dependency or management risk acceptance. |
| **User Notification** | "Unconditional readiness blocked. Current stock insufficient. Confirm conditionally with inbound dependency or obtain executive risk acceptance." |
| **Business Outcome** | Promotional launch is not confirmed without adequate stock coverage; campaign failure risk is explicitly acknowledged if proceeding conditionally. |

---

### UC-041 — Conduct Inventory Audit and Control Review

#### UC-041-EX-01 — Segregation of Duties Violation Detected

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-041-EX-01 |
| **Trigger** | Internal Auditor identifies transaction where initiator and approver are the same user, violating SoD rules. |
| **Failed Step** | 3 |
| **Expected System Behavior** | System flags transaction as SoD violation in audit review and records control breach per FR-088. |
| **User Notification** | "Control breach detected: [transaction type] [reference]. Initiator and approver are the same user [user]. Document finding for remediation." |
| **Business Outcome** | Control weakness is identified and documented; remediation action can be assigned before external audit. |

#### UC-041-EX-02 — Adjustment Without Reason Code in Audit Sample

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-041-EX-02 |
| **Trigger** | Internal Auditor samples adjustment transaction missing mandatory reason code per BR-020 (legacy or policy breach). |
| **Failed Step** | 4 |
| **Expected System Behavior** | System flags transaction as policy non-compliance and includes in audit findings report. |
| **User Notification** | "Policy non-compliance: Adjustment [reference] missing reason code. Include in audit findings and assign corrective action." |
| **Business Outcome** | Governance gap is documented; reason code compliance enforcement is reinforced. |

---

## Domain 11: Cross-Cutting System Interactions

### UC-042 — View Inventory Movement and Transaction History

#### UC-042-EX-01 — No Transactions Found for Search Criteria

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-042-EX-01 |
| **Trigger** | Inventory Controller searches movement history with criteria that match no transactions in the selected period. |
| **Failed Step** | 2 |
| **Expected System Behavior** | System returns empty result set with search criteria summary and suggests broadening filters. |
| **User Notification** | "No movement transactions found for selected criteria. Broaden date range, location, or product filters." |
| **Business Outcome** | User is informed no matching history exists; investigation scope can be adjusted. |

---

### UC-043 — Query and Review Audit Trail

#### UC-043-EX-01 — Audit Query Exceeds Authorized Scope

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-043-EX-01 |
| **Trigger** | Internal Auditor attempts audit trail query for entity types or locations outside authorized audit scope. |
| **Failed Step** | 2 |
| **Expected System Behavior** | System restricts query results to authorized audit scope and logs access attempt. |
| **User Notification** | "Audit query scope restricted. Results limited to authorized entities. Contact System Administrator for expanded audit access." |
| **Business Outcome** | Audit access is controlled; sensitive data beyond audit mandate is not exposed. |

---

### UC-044 — Manage User Accounts and Role Assignments

#### UC-044-EX-01 — Segregation of Duties Conflict in Role Assignment

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-044-EX-01 |
| **Trigger** | System Administrator assigns role combination that creates segregation of duties conflict (e.g., Buyer and Purchasing Manager on same user). |
| **Failed Step** | 3 |
| **Expected System Behavior** | System blocks role assignment and displays conflicting SoD rule. |
| **User Notification** | "Role assignment blocked. Conflicts with segregation of duties rule [SOD-XXX]: [conflict description]. Assign non-conflicting roles." |
| **Business Outcome** | User accounts do not combine conflicting duties; control framework integrity is maintained. |

#### UC-044-EX-02 — Deactivate User with Pending Approvals

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-044-EX-02 |
| **Trigger** | System Administrator attempts to deactivate user account with pending approval items in user's queue. |
| **Failed Step** | 4 |
| **Expected System Behavior** | System blocks deactivation and displays pending approval count requiring reassignment. |
| **User Notification** | "User cannot be deactivated. [N] pending approvals in queue. Reassign approvals before deactivation." |
| **Business Outcome** | Approval workflow is not orphaned; pending business decisions are reassigned before access removal. |

---

### UC-045 — Enforce Role-Based and Location-Scoped Access

#### UC-045-EX-01 — Unauthorized Function Access Attempt

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-045-EX-01 |
| **Trigger** | User attempts to access function or transaction type not granted by assigned role per FR-081. |
| **Failed Step** | 4 |
| **Expected System Behavior** | System denies access, does not display restricted function, and logs access denial per FR-083. |
| **User Notification** | "Access denied. Your role [role] does not have permission for [function]. Contact System Administrator if access is required." |
| **Business Outcome** | Least-privilege access is enforced; unauthorized business actions are prevented. |

#### UC-045-EX-02 — Cross-Location Transaction Without Authorization

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-045-EX-02 |
| **Trigger** | Transactional user attempts inventory transaction at location outside assigned location scope per FR-082 and NFR-SEC-006. |
| **Failed Step** | 4 |
| **Expected System Behavior** | System blocks transaction and displays user's authorized location scope. |
| **User Notification** | "Transaction blocked. Location [location] is outside your authorized scope. Authorized locations: [list]." |
| **Business Outcome** | Location-scoped access is enforced; cross-location transactions by unauthorized users are prevented. |

#### UC-045-EX-03 — SoD Violation on Transaction Attempt

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-045-EX-03 |
| **Trigger** | User attempts action that combines initiator and approver roles prohibited by segregation of duties (e.g., count and approve same variance). |
| **Failed Step** | 4 |
| **Expected System Behavior** | System blocks action and identifies conflicting SoD rule; routes to independent actor if applicable. |
| **User Notification** | "Action blocked per segregation of duties [SOD-XXX]. This action requires a different authorized role." |
| **Business Outcome** | Conflicting duties cannot be performed by same user; fraud and error risk controls are enforced. |

---

### UC-046 — Import Initial Product and Stock Master Data

#### UC-046-EX-01 — Import File Contains Duplicate SKUs

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-046-EX-01 |
| **Trigger** | Import validation detects duplicate SKU entries within the import file or against existing catalog. |
| **Failed Step** | 3 |
| **Expected System Behavior** | System rejects duplicate records, displays duplicate list, and processes only unique valid records if partial import is selected. |
| **User Notification** | "Import validation failed: [N] duplicate SKUs detected. [list]. Correct file and re-import or proceed with non-duplicate records only." |
| **Business Outcome** | Catalog integrity is protected at go-live; duplicate identities are not bulk-loaded. |

#### UC-046-EX-02 — Import References Unknown Location

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-046-EX-02 |
| **Trigger** | Stock balance import references location code not defined in location master. |
| **Failed Step** | 3 |
| **Expected System Behavior** | System rejects affected stock balance records and lists unknown location references. |
| **User Notification** | "Import blocked for [N] records. Unknown location codes: [list]. Configure locations before importing stock balances." |
| **Business Outcome** | Opening balances are not assigned to undefined locations; location master precedes stock data load. |

---

### UC-047 — Receive and Respond to Operational Notifications

#### UC-047-EX-01 — Notification Action Deadline Passed

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-047-EX-01 |
| **Trigger** | Warehouse Manager opens notification after business-defined response deadline (e.g., Class A low-stock alert exceeding replenishment SLA). |
| **Failed Step** | 1 |
| **Expected System Behavior** | System displays notification as overdue, escalates to Operations Director or Purchasing Manager, and retains overdue status. |
| **User Notification** | "OVERDUE: [notification type] for [SKU/location]. Response deadline [date/time] passed. Escalated to [escalation role]." |
| **Business Outcome** | Overdue operational conditions receive management escalation; SLA breaches are visible and tracked. |

---

### UC-048 — Support Multi-Location Split Fulfillment

#### UC-048-EX-01 — Network ATP Insufficient for Full Order Despite Multi-Location Option

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-048-EX-01 |
| **Trigger** | Combined ATP across all locations is still less than total order quantity after multi-location split evaluation. |
| **Failed Step** | 2 |
| **Expected System Behavior** | System displays network ATP shortfall and blocks full split fulfillment plan; routes to partial fulfillment or backorder workflow. |
| **User Notification** | "Network ATP insufficient for full order. Total available: [N], ordered: [M]. Proceed with partial fulfillment or backorder for shortfall." |
| **Business Outcome** | Full order commitment is not made when network cannot supply; customer commitment aligns with total available stock. |

#### UC-048-EX-02 — Split Fulfillment Blocked by Source Minimum on Contributing Location

| Field | Detail |
|-------|--------|
| **Exception ID** | UC-048-EX-02 |
| **Trigger** | Proposed split allocation from a contributing location would breach that location's minimum threshold per BR-012. |
| **Failed Step** | 3 |
| **Expected System Behavior** | System reduces or removes allocation from affected location and recalculates split plan with source protection applied. |
| **User Notification** | "Split allocation adjusted. Location [location] contribution reduced to [N] to protect minimum threshold. Revised plan displayed." |
| **Business Outcome** | Multi-location fulfillment does not deplete contributing locations below service levels; split plan respects network balance rules. |

---

## Summary

| Metric | Count |
|--------|-------|
| Use Cases | 48 |
| Business Exceptions | 97 |
| Average Exceptions per Use Case | 2.0 |
| Related Business Rules Referenced | BR-001 through BR-031, SOD-003, SOD-006, SOD-007 |

### Exceptions by Category

| Category | Representative Exceptions |
|----------|--------------------------|
| Authorization & SoD | Self-approval blocked, role conflict, threshold escalation |
| Stock availability | Insufficient ATP, safety stock breach, quarantine exclusion |
| Procurement controls | Discontinued product, PO approval, network check before buy |
| Receiving & quality | MRSL failure, missing lot/batch, undocumented discrepancy |
| Fulfillment commitment | Oversell prevention, backorder acknowledgment, pick verification |
| Governance & audit | Missing reason code, SoD violation, incomplete data warnings |

---

## Traceability

| Source Document | Reference |
|-----------------|-----------|
| Use Case Catalog | SRS-UC-001 |
| Use Case Main Flows | SRS-UC-002 |
| Use Case Alternate Flows | SRS-UC-003 |
| Business Rule Catalog | SRS-BR-001 |
| Business Requirements Document | BRD-IMS-001 |

---

## Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Business Analyst | | | |
| Product Owner | | | |
| Operations Director | | | |

---

*End of Use Case Exception Flows*

*Document ID: SRS-UC-004 | Version 1.0 | July 5, 2026*
