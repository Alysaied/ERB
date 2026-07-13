# Use Case Alternate Flows
## Inventory Management System

---

## Document Information

| Attribute | Detail |
|-----------|--------|
| **Document ID** | SRS-UC-003 |
| **Document Title** | Use Case Alternate Flows — Inventory Management System |
| **Version** | 1.0 |
| **Status** | Draft |
| **Document Owner** | Business Analyst |
| **Source Documents** | SRS-UC-001 (Use Case Catalog), SRS-UC-002 (Use Case Main Flows) |
| **Date** | July 5, 2026 |
| **Scope** | Valid business alternatives only — no error or exception paths |

### Purpose

This document identifies alternate flows for each of the 48 use cases in the Inventory Management System. An alternate flow branches from the main flow at a defined step when a valid business condition applies, leading to a different but equally legitimate business outcome. Error conditions, system failures, and validation rejections are excluded.

### Alternate Flow Legend

| Field | Description |
|-------|-------------|
| **Alternate Flow ID** | Unique identifier in format UC-XXX-AF-NN |
| **Starting Step** | Main flow step number where the alternate path diverges |
| **Business Condition** | Valid business circumstance triggering the alternate path |
| **Alternative Actions** | Actor and system actions taken along the alternate path |
| **Business Outcome** | Resulting business state upon successful completion of the alternate path |

---

## Domain 1: Master Data & Governance

### UC-001 — Manage Product Master Data

#### UC-001-AF-01 — Update Existing Product Record

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-001-AF-01 |
| **Starting Step** | 2 |
| **Business Condition** | An existing product record requires attribute correction, identifier update, or description change rather than creation of a new SKU. |
| **Alternative Actions** | Inventory Controller searches and selects the existing product from the catalog. System loads the current product profile into the edit form. Inventory Controller updates the required attributes and submits the changes. System saves the revised record while preserving SKU identity and transaction history. |
| **Business Outcome** | Existing product master is updated with corrected attributes; all historical inventory transactions remain linked to the same SKU. |

#### UC-001-AF-02 — Change Product Lifecycle Status

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-001-AF-02 |
| **Starting Step** | 3 |
| **Business Condition** | Business decision requires changing product status to inactive or discontinued rather than modifying descriptive attributes. |
| **Alternative Actions** | Inventory Controller selects the product and chooses status change action. System presents status options (active, inactive, discontinued) with business impact summary. Inventory Controller sets new status and confirms. System applies status change, enforces discontinued reorder prohibition, and retains product record for historical reference. |
| **Business Outcome** | Product status reflects current commercial position; discontinued products are blocked from new replenishment while remaining visible in history and reporting. |

#### UC-001-AF-03 — Resolve Duplicate Product Record

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-001-AF-03 |
| **Starting Step** | 3 |
| **Business Condition** | System detects a potential duplicate SKU or identifier during create or update, and Inventory Controller confirms a merge or deduplication is required. |
| **Alternative Actions** | System presents duplicate match candidates. Inventory Controller designates the authoritative master record and selects the duplicate for resolution. Inventory Controller confirms merge or deactivation of the duplicate record. System consolidates references to the authoritative SKU and retires the duplicate. |
| **Business Outcome** | Single authoritative product identity is maintained; duplicate records are eliminated without loss of transaction traceability. |

---

### UC-002 — Configure Inventory Locations

#### UC-002-AF-01 — Update Existing Location Configuration

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-002-AF-01 |
| **Starting Step** | 2 |
| **Business Condition** | An existing location requires hierarchy adjustment, attribute update, or status change rather than creation of a new location. |
| **Alternative Actions** | Inventory Controller selects the existing location from the network view. System loads current location configuration. Inventory Controller updates hierarchy, attributes, or operational status and saves. System applies changes and confirms updated location definition. |
| **Business Outcome** | Location configuration reflects current operational structure; stock assignments and transactions remain associated with the updated location. |

#### UC-002-AF-02 — Plan Location Closure and Stock Disposition

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-002-AF-02 |
| **Starting Step** | 4 |
| **Business Condition** | A location is scheduled for closure and requires stock disposition planning before deactivation rather than go-live activation. |
| **Alternative Actions** | Inventory Controller initiates location closure planning. System displays on-hand stock by product at the location. Inventory Controller defines disposition plan (transfer to other locations, sell-down, or write-off). System records closure plan and schedules stock movement or depletion actions. Inventory Controller confirms closure readiness when stock is dispositioned. |
| **Business Outcome** | Location closure is planned with defined stock disposition; location is deactivated without stranded inventory. |

---

### UC-003 — Define Stock Policies and Thresholds

#### UC-003-AF-01 — Configure Policy at Product Group Level

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-003-AF-01 |
| **Starting Step** | 1 |
| **Business Condition** | Stock policy applies uniformly to a product category or group rather than individual SKUs. |
| **Alternative Actions** | Inventory Controller selects product group or category for policy configuration. System displays group members and current policy defaults. Inventory Controller sets reorder level, minimum threshold, and safety stock for the group. System applies policy to all group members and confirms group-level policy activation. |
| **Business Outcome** | Consistent stock policy is applied across the product group; monitoring and alerts operate at group-defined thresholds. |

#### UC-003-AF-02 — Apply Location-Specific Threshold Override

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-003-AF-02 |
| **Starting Step** | 2 |
| **Business Condition** | A specific location requires different thresholds than the network default due to local demand, lead time, or service-level requirements. |
| **Alternative Actions** | Inventory Controller selects product and overrides thresholds for a specific location. System displays network default and location-specific fields. Inventory Controller enters location-specific reorder level and minimum threshold. System saves location override while retaining network default for other locations. |
| **Business Outcome** | Location-specific thresholds reflect local operating conditions; replenishment alerts trigger based on location-appropriate levels. |

---

### UC-004 — Classify Products by ABC Priority

#### UC-004-AF-01 — Bulk Reclassification from Performance Analysis

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-004-AF-01 |
| **Starting Step** | 2 |
| **Business Condition** | Periodic review cycle produces system-recommended ABC assignments based on velocity, revenue, or criticality analysis. |
| **Alternative Actions** | Inventory Controller requests ABC analysis report. System generates recommended classifications based on defined criteria. Inventory Controller reviews recommendations and accepts bulk classification update. System applies new classifications and updates count frequency and monitoring rules. |
| **Business Outcome** | Product ABC classifications are refreshed based on current performance data; operational priorities align with updated segmentation. |

#### UC-004-AF-02 — Manual Override of Single Product Classification

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-004-AF-02 |
| **Starting Step** | 3 |
| **Business Condition** | Business judgment overrides system-recommended classification for a strategically critical or newly launched product. |
| **Alternative Actions** | Inventory Controller selects a product and assigns a different class than the system recommendation. System records override justification. Inventory Controller saves the manual classification. System applies override and adjusts monitoring intensity for the product. |
| **Business Outcome** | Strategically important product receives appropriate operational priority regardless of current velocity metrics. |

---

### UC-005 — Maintain Governance Policies and Reason Codes

#### UC-005-AF-01 — Retire or Deactivate Reason Code

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-005-AF-01 |
| **Starting Step** | 2 |
| **Business Condition** | An existing reason code is no longer used in operations and must be retired while preserving historical transaction references. |
| **Alternative Actions** | Inventory Controller selects existing reason code and initiates deactivation. System confirms no mandatory dependency on active policies. Inventory Controller deactivates the reason code. System marks code as inactive for new transactions while retaining it in historical records. |
| **Business Outcome** | Reason code catalog remains current; retired codes are unavailable for new transactions but visible in historical audit data. |

#### UC-005-AF-02 — Update Governance Policy Without Reason Code Change

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-005-AF-02 |
| **Starting Step** | 3 |
| **Business Condition** | Governance policy parameters (approval thresholds, count rules, safety stock override rules) require update without changes to the reason code catalog. |
| **Alternative Actions** | Inventory Controller opens governance policy configuration. System displays current policy parameters by transaction type. Inventory Controller updates policy thresholds or rules and saves. System applies updated governance policy to future transactions. |
| **Business Outcome** | Inventory governance rules reflect current business policy; reason code catalog remains unchanged. |

---

## Domain 2: Inbound & Receiving

### UC-006 — Place and Manage Purchase Orders

#### UC-006-AF-01 — Amend Existing Open Purchase Order

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-006-AF-01 |
| **Starting Step** | 2 |
| **Business Condition** | An open or approved purchase order requires quantity, delivery date, or line adjustment rather than creation of a new order. |
| **Alternative Actions** | Buyer selects existing open purchase order. System displays current order lines and status. Buyer modifies quantities, dates, or lines and submits amendment. System routes amendment for approval if required and updates expected inbound supply. |
| **Business Outcome** | Purchase order reflects revised commercial commitment; inbound supply visibility is updated accordingly. |

#### UC-006-AF-02 — Cancel Purchase Order Before Receipt

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-006-AF-02 |
| **Starting Step** | 4 |
| **Business Condition** | Business need for the purchase order no longer exists or supplier confirms order cancellation before any goods are received. |
| **Alternative Actions** | Buyer selects purchase order and initiates cancellation. System verifies no goods have been received against the order. Purchasing Manager approves cancellation. System closes purchase order, removes expected inbound supply, and records cancellation reason. |
| **Business Outcome** | Purchase order is formally cancelled; no further receipt is expected and replenishment planning reflects removed inbound supply. |

---

### UC-007 — Plan Expected Inbound Deliveries

#### UC-007-AF-01 — Schedule Split Deliveries for Single Purchase Order

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-007-AF-01 |
| **Starting Step** | 2 |
| **Business Condition** | Supplier confirms that a single purchase order will arrive in multiple shipments on different dates. |
| **Alternative Actions** | Buyer selects purchase order and defines multiple expected delivery dates by line or shipment group. System records split delivery schedule with quantities per shipment. Buyer confirms split plan. System updates inbound visibility with multiple expected arrival events. |
| **Business Outcome** | Receiving and replenishment teams have accurate visibility into phased inbound supply for a single purchase order. |

#### UC-007-AF-02 — Reschedule Expected Delivery Date

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-007-AF-02 |
| **Starting Step** | 2 |
| **Business Condition** | Supplier communicates a revised delivery date that differs from the originally planned arrival. |
| **Alternative Actions** | Buyer updates expected shipment or arrival date based on supplier confirmation. System revises inbound delivery schedule. Buyer notifies receiving location of date change. System updates replenishment and alert calculations based on revised date. |
| **Business Outcome** | Inbound delivery plan reflects current supplier commitment; downstream planning uses updated arrival expectations. |

---

### UC-008 — Receive and Verify Supplier Goods

#### UC-008-AF-01 — Receive Partial Shipment Against Purchase Order

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-008-AF-01 |
| **Starting Step** | 3 |
| **Business Condition** | Supplier delivers only a portion of the ordered quantity with remaining quantity expected on a subsequent shipment. |
| **Alternative Actions** | Receiving Clerk verifies and records received quantities for delivered lines only. System records partial receipt against purchase order and retains outstanding quantity as open. Receiving Clerk confirms partial receipt completion. System stages received quantity for put-away and maintains open PO balance for future deliveries. |
| **Business Outcome** | Partial delivery is accurately recorded; purchase order remains open for remaining expected quantity. |

#### UC-008-AF-02 — Receive Against Authorized Ad-Hoc Receipt

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-008-AF-02 |
| **Starting Step** | 2 |
| **Business Condition** | Supplier goods arrive under an explicitly approved ad-hoc receipt authorization rather than a standard purchase order reference. |
| **Alternative Actions** | Receiving Clerk selects ad-hoc receipt option and enters approval reference. System validates authorization and presents expected receipt details. Receiving Clerk verifies and records goods per authorization. System records receipt linked to ad-hoc approval and stages for put-away. |
| **Business Outcome** | Non-standard inbound supply is received under documented authorization with full traceability. |

---

### UC-009 — Document and Resolve Receipt Discrepancies

#### UC-009-AF-01 — Resolve Discrepancy via Supplier Credit

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-009-AF-01 |
| **Starting Step** | 4 |
| **Business Condition** | Short shipment or pricing discrepancy is resolved through supplier credit or invoice adjustment rather than physical receipt of missing quantity. |
| **Alternative Actions** | Warehouse Manager selects supplier credit resolution path. System records credit resolution against discrepancy record. Buyer confirms supplier credit agreement reference. System closes discrepancy with financial resolution and retains accepted physical receipt quantities. |
| **Business Outcome** | Receipt discrepancy is resolved commercially; inventory records reflect only physically received and verified quantities. |

#### UC-009-AF-02 — Accept Over-Shipment with Supplier Agreement

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-009-AF-02 |
| **Starting Step** | 3 |
| **Business Condition** | Supplier delivers quantity exceeding purchase order and buyer confirms acceptance of the excess under agreed commercial terms. |
| **Alternative Actions** | Receiving Clerk documents over-shipment discrepancy. Buyer confirms acceptance of excess quantity. Warehouse Manager approves receipt of accepted excess. System records full accepted quantity including over-shipment and documents supplier agreement reference. |
| **Business Outcome** | Over-shipment is formally accepted and recorded; supplier accountability and three-way match data reflect agreed quantities. |

---

### UC-010 — Perform Stock Put-Away

#### UC-010-AF-01 — Put-Away to Alternate Storage Location

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-010-AF-01 |
| **Starting Step** | 3 |
| **Business Condition** | Suggested storage location is at capacity or operationally unsuitable; warehouse staff places stock in an approved alternate location. |
| **Alternative Actions** | Warehouse Staff selects alternate storage location within the same warehouse. System validates alternate location eligibility. Warehouse Staff confirms product, quantity, and alternate destination. System records put-away to alternate location and updates on-hand and ATP. |
| **Business Outcome** | Stock is available for fulfillment from the alternate storage location with correct rotation and location attribution. |

#### UC-010-AF-02 — Batch Put-Away for Multiple Receipt Lines

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-010-AF-02 |
| **Starting Step** | 1 |
| **Business Condition** | Multiple receipt lines from the same delivery are put away together in a single warehouse operation. |
| **Alternative Actions** | Warehouse Staff selects batch put-away for grouped receipt lines. System presents consolidated put-away task list. Warehouse Staff completes put-away confirmations for each line in sequence. System records all put-away completions and updates availability for all affected products. |
| **Business Outcome** | Efficient put-away of full delivery is completed; all received lines become available for sale and fulfillment. |

---

### UC-011 — Receive Return and Non-PO Inbound Stock

#### UC-011-AF-01 — Receive Authorized Customer Return

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-011-AF-01 |
| **Starting Step** | 2 |
| **Business Condition** | Inbound goods are a customer return covered by a valid return authorization rather than an ad-hoc receipt. |
| **Alternative Actions** | Receiving Clerk selects authorized return receipt type and enters return authorization reference. System retrieves linked order and authorized return lines. Receiving Clerk verifies returned products and quantities. System records return receipt and routes stock to inspection per return policy. |
| **Business Outcome** | Customer return is received against valid authorization and queued for inspection and disposition. |

#### UC-011-AF-02 — Receive Approved Ad-Hoc Inbound Stock

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-011-AF-02 |
| **Starting Step** | 2 |
| **Business Condition** | Inbound stock arrives under a pre-approved ad-hoc receipt (samples, emergency supply, or non-catalog inbound) without purchase order or return authorization. |
| **Alternative Actions** | Receiving Clerk selects ad-hoc receipt type and enters approval reference. System validates ad-hoc approval authority and scope. Receiving Clerk verifies and records inbound goods. System records ad-hoc receipt and stages stock per approval terms. |
| **Business Outcome** | Ad-hoc inbound stock is recorded under documented approval with defined next disposition steps. |

---

## Domain 3: Inventory Visibility & Status

### UC-012 — Monitor Inventory Status

#### UC-012-AF-01 — Monitor Single Location Inventory Health

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-012-AF-01 |
| **Starting Step** | 2 |
| **Business Condition** | Review is scoped to a single warehouse or store rather than network-wide status. |
| **Alternative Actions** | Inventory Controller filters monitoring view to a specific location. System displays stock status, alerts, and threshold breaches for the selected location only. Inventory Controller reviews location-specific low-stock and out-of-stock conditions. System retains location-scoped view for ongoing monitoring. |
| **Business Outcome** | Location-level inventory health is assessed; local replenishment and operational actions can be prioritized. |

#### UC-012-AF-02 — Export Status Snapshot for Management Review

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-012-AF-02 |
| **Starting Step** | 5 |
| **Business Condition** | Management briefing or steering review requires exported inventory status snapshot rather than live screen review only. |
| **Alternative Actions** | Inventory Controller requests export of current status view with applied filters. System generates exportable status report with timestamp. Inventory Controller distributes report to stakeholders. System archives export reference for audit. |
| **Business Outcome** | Point-in-time inventory status snapshot is available for management decision-making and meeting documentation. |

---

### UC-013 — Inquire Inventory Availability

#### UC-013-AF-01 — Network-Wide Availability Inquiry

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-013-AF-01 |
| **Starting Step** | 3 |
| **Business Condition** | Customer or sales inquiry requires total network availability rather than availability at a single fulfillment location. |
| **Alternative Actions** | Sales Representative requests network-wide availability view. System aggregates ATP across all fulfillment locations and displays network total with per-location breakdown. Sales Representative reviews network position and expected inbound supply. System presents consolidated availability for customer commitment discussion. |
| **Business Outcome** | Sales team has complete network visibility to support fulfillment options including multi-location or transfer scenarios. |

#### UC-013-AF-02 — Product Lookup by Barcode Scan

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-013-AF-02 |
| **Starting Step** | 2 |
| **Business Condition** | Product is identified by physical barcode scan rather than text search during customer-facing inquiry. |
| **Alternative Actions** | Sales Representative scans product barcode. System resolves barcode to SKU and retrieves product availability. Sales Representative reviews ATP and status for the scanned product. System displays availability result for immediate customer response. |
| **Business Outcome** | Rapid product identification and availability response during in-person or phone sales interaction. |

---

## Domain 4: Inventory Control & Accuracy

### UC-014 — Perform Cycle Count

#### UC-014-AF-01 — Count Matches System Quantity

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-014-AF-01 |
| **Starting Step** | 4 |
| **Business Condition** | Physical count result matches system quantity; no variance investigation is required. |
| **Alternative Actions** | Warehouse Staff submits count result. System compares count to system quantity and confirms match. System records count as verified accurate with no variance flag. Warehouse Staff reviews count confirmation showing no adjustment required. |
| **Business Outcome** | SKU-location accuracy is confirmed; count cycle completes without adjustment workflow. |

#### UC-014-AF-02 — Perform Unscheduled Ad-Hoc Cycle Count

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-014-AF-02 |
| **Starting Step** | 1 |
| **Business Condition** | Operations initiates an unscheduled count for a specific product or location outside the regular count schedule. |
| **Alternative Actions** | Warehouse Staff initiates ad-hoc cycle count for selected product and location. System presents blind count entry form. Warehouse Staff performs and submits count. System records ad-hoc count result and flags variance if present. |
| **Business Outcome** | Targeted accuracy verification is completed outside scheduled cycle; results feed variance workflow if needed. |

---

### UC-015 — Conduct Full Physical Inventory Count

#### UC-015-AF-01 — Phased Zone-Based Physical Count

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-015-AF-01 |
| **Starting Step** | 2 |
| **Business Condition** | Full count is executed in sequential zones rather than simultaneous wall-to-wall count across the entire location. |
| **Alternative Actions** | Inventory Controller defines zone sequence and assigns teams per zone. System generates zone-specific count sheets and applies freeze per zone as counted. Warehouse Staff complete each zone before proceeding to next. System tracks zone completion and compiles full-location count upon final zone close. |
| **Business Outcome** | Complete location count is achieved through controlled phased execution with reduced operational disruption. |

#### UC-015-AF-02 — Recount Selected Zones Before Count Close

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-015-AF-02 |
| **Starting Step** | 4 |
| **Business Condition** | Initial count results for specific zones require verification recount before final count session close. |
| **Alternative Actions** | Inventory Controller selects zones for recount. System generates recount assignments with blind count. Warehouse Staff perform recount and submit results. System compares recount to initial count and uses recount result for variance determination. |
| **Business Outcome** | Count accuracy is validated through targeted recount; final variance report reflects verified quantities. |

---

### UC-016 — Investigate and Approve Count Variances

#### UC-016-AF-01 — Variance Within Auto-Approval Tolerance

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-016-AF-01 |
| **Starting Step** | 4 |
| **Business Condition** | Count variance falls within defined auto-approval tolerance and does not require independent approver escalation. |
| **Alternative Actions** | Warehouse Manager documents brief investigation notes. System evaluates variance against auto-approval threshold. Warehouse Manager confirms variance approval within authority. System auto-approves adjustment and queues for processing without independent approver routing. |
| **Business Outcome** | Low-materiality variance is resolved efficiently; inventory record is corrected with appropriate documentation. |

#### UC-016-AF-02 — Investigation Concludes Count Is Accurate

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-016-AF-02 |
| **Starting Step** | 3 |
| **Business Condition** | Investigation determines the physical count was correct and the system record was in error due to an unrecorded prior movement since identified and explained. |
| **Alternative Actions** | Warehouse Manager documents investigation finding that supports count accuracy. System records investigation conclusion. Warehouse Manager approves adjustment to align system to counted quantity with documented root cause. System queues adjustment reflecting corrected system record. |
| **Business Outcome** | System inventory is aligned to verified physical quantity with documented investigation supporting the correction. |

---

### UC-017 — Process Stock Adjustments

#### UC-017-AF-01 — Process Inventory Increase Adjustment

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-017-AF-01 |
| **Starting Step** | 2 |
| **Business Condition** | Adjustment direction is an increase (found stock, receipt correction) rather than a decrease. |
| **Alternative Actions** | Warehouse Manager selects increase adjustment direction and enters quantity. System displays resulting on-hand increase preview. Warehouse Manager selects reason code and submits. System applies increase upon approval and updates ATP. |
| **Business Outcome** | On-hand and ATP are increased with documented reason; movement history records the positive adjustment. |

#### UC-017-AF-02 — Adjustment Below Approval Threshold

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-017-AF-02 |
| **Starting Step** | 4 |
| **Business Condition** | Adjustment quantity and value fall below the threshold requiring independent approver authorization. |
| **Alternative Actions** | Warehouse Manager submits adjustment within delegated authority. System confirms adjustment is below escalation threshold. Warehouse Manager confirms adjustment directly. System applies adjustment without independent approver routing. |
| **Business Outcome** | Routine low-materiality adjustment is completed within delegated authority with full audit trail. |

---

### UC-018 — Authorize and Process Inventory Write-Offs

#### UC-018-AF-01 — Partial Quantity Write-Off

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-018-AF-01 |
| **Starting Step** | 2 |
| **Business Condition** | Only a portion of on-hand quantity is damaged or obsolete; remaining quantity remains sellable. |
| **Alternative Actions** | Operations Director reviews write-off request for partial quantity. System displays on-hand total and proposed write-off quantity. Operations Director approves partial write-off. System removes only the written-off quantity from on-hand and ATP; remaining quantity stays sellable. |
| **Business Outcome** | Damaged or obsolete portion is removed from inventory; sellable remainder continues in active stock. |

#### UC-018-AF-02 — Write-Off Initiated by Warehouse Manager

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-018-AF-02 |
| **Starting Step** | 1 |
| **Business Condition** | Warehouse Manager identifies write-off need at location level and submits request for Operations Director authorization. |
| **Alternative Actions** | Warehouse Manager creates write-off request with evidence and reason code. System routes request to Operations Director approval queue. Operations Director reviews and approves. Finance Manager acknowledges where required. System executes write-off upon final authorization. |
| **Business Outcome** | Location-initiated write-off is processed through proper authorization chain with full documentation. |

---

### UC-019 — Manage Quarantine and Hold Stock

#### UC-019-AF-01 — Release Stock from Quarantine to Sellable

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-019-AF-01 |
| **Starting Step** | 1 |
| **Business Condition** | Previously quarantined stock has passed quality review or customs clearance and is approved for return to sellable inventory. |
| **Alternative Actions** | Warehouse Manager selects quarantined stock for release review. System displays hold reason and quarantined quantity. Warehouse Manager confirms release authorization. System moves quantity from quarantined to sellable ATP and records release in movement history. |
| **Business Outcome** | Previously held stock is restored to sellable availability with documented release authorization. |

#### UC-019-AF-02 — Place Bonded Inventory on Customs Hold

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-019-AF-02 |
| **Starting Step** | 3 |
| **Business Condition** | Inbound bonded goods require customs clearance hold rather than quality quarantine. |
| **Alternative Actions** | Warehouse Manager assigns bonded customs hold status to received stock. System excludes quantity from sellable ATP under bonded hold classification. Warehouse Manager records customs reference. System maintains hold until clearance is confirmed. |
| **Business Outcome** | Bonded inventory remains under regulatory hold and excluded from fulfillment until customs release is documented. |

---

### UC-020 — Analyze Shrinkage, Loss, and Obsolete Stock

#### UC-020-AF-01 — Shrinkage Analysis by Location

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-020-AF-01 |
| **Starting Step** | 2 |
| **Business Condition** | Analysis is scoped to compare shrinkage performance across locations rather than enterprise-wide aggregation. |
| **Alternative Actions** | Inventory Controller selects location-comparative shrinkage report. System presents shrinkage by reason code and value per location. Inventory Controller identifies locations with elevated loss patterns. System supports drill-down to location-specific adjustment history. |
| **Business Outcome** | Location-level shrinkage accountability is established; targeted corrective actions can be assigned to underperforming sites. |

#### UC-020-AF-02 — Recommend Transfer to Clearance Channel

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-020-AF-02 |
| **Starting Step** | 4 |
| **Business Condition** | Slow-moving or obsolete stock is recommended for redistribution to outlet or clearance channel rather than write-off. |
| **Alternative Actions** | Inventory Controller documents transfer-to-clearance recommendation for identified SKUs. System records recommended disposition action. Inventory Controller initiates transfer request or commercial handoff to outlet channel. System links analysis recommendation to subsequent transfer or status change. |
| **Business Outcome** | Excess inventory is directed toward revenue recovery through alternate channel rather than immediate write-off. |

---

## Domain 5: Order Fulfillment

### UC-021 — Confirm Order Availability

#### UC-021-AF-01 — Fulfill from Alternate Location

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-021-AF-01 |
| **Starting Step** | 2 |
| **Business Condition** | Primary fulfillment location has insufficient ATP but another network location has adequate stock to fulfill the order. |
| **Alternative Actions** | Sales Representative requests availability check across all fulfillment locations. System identifies alternate location with sufficient ATP. Sales Representative confirms alternate fulfillment location with customer. System records availability confirmation with designated fulfillment location. |
| **Business Outcome** | Order availability is confirmed using alternate location stock; customer commitment reflects achievable fulfillment source. |

#### UC-021-AF-02 — Confirm Partial Availability for Customer Decision

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-021-AF-02 |
| **Starting Step** | 3 |
| **Business Condition** | Order line has partial ATP; customer must decide on partial fulfillment before proceeding to reservation. |
| **Alternative Actions** | Sales Representative presents partial availability to customer. System displays available quantity versus ordered quantity. Customer accepts partial quantity commitment. System records partial availability confirmation and routes to partial fulfillment or reservation workflow. |
| **Business Outcome** | Customer makes informed commitment based on partial availability; order proceeds with agreed fulfillable quantity. |

---

### UC-022 — Reserve Inventory for Confirmed Orders

#### UC-022-AF-01 — Reserve from Alternate Fulfillment Location

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-022-AF-01 |
| **Starting Step** | 3 |
| **Business Condition** | Reservation is made from a non-default fulfillment location selected during availability confirmation. |
| **Alternative Actions** | Customer Service Representative selects alternate fulfillment location for reservation. System validates ATP at selected location. Customer Service Representative confirms reservation at alternate location. System reserves stock at designated location and updates ATP. |
| **Business Outcome** | Order reservation is held at the location that will execute fulfillment; ATP is reduced at the correct source. |

#### UC-022-AF-02 — Reserve Partial Quantity with Backorder Remainder

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-022-AF-02 |
| **Starting Step** | 3 |
| **Business Condition** | Customer accepts partial reservation now with remaining quantity to be fulfilled when stock becomes available. |
| **Alternative Actions** | Customer Service Representative reserves available quantity for immediate fulfillment. System creates reservation for partial quantity and backorder record for remainder. Customer Service Representative confirms split reservation. System releases partial order to warehouse and holds backorder for replenishment priority. |
| **Business Outcome** | Available stock is reserved and queued for fulfillment; backordered remainder is tracked for future supply. |

---

### UC-023 — Release Inventory Reservations

#### UC-023-AF-01 — Release Single Order Line Reservation

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-023-AF-01 |
| **Starting Step** | 2 |
| **Business Condition** | Only specific order lines require reservation release while other lines remain reserved for fulfillment. |
| **Alternative Actions** | Customer Service Representative selects individual lines for release. System presents per-line release quantities and ATP restoration. Customer Service Representative confirms line-level release. System releases selected lines only and maintains reservation on remaining lines. |
| **Business Outcome** | Released line quantities return to ATP; remaining reserved lines continue toward fulfillment. |

#### UC-023-AF-02 — Release Reservation Due to Order Amendment

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-023-AF-02 |
| **Starting Step** | 4 |
| **Business Condition** | Customer amends order quantity downward; excess reserved quantity must be released while order remains active. |
| **Alternative Actions** | Customer Service Representative records order amendment and initiates partial reservation release. System calculates excess reserved quantity to release. Customer Service Representative confirms release of excess only. System restores excess quantity to ATP and updates reservation to amended quantity. |
| **Business Outcome** | Reservation aligns with amended order; released stock is available for other customer commitments. |

---

### UC-024 — Pick, Pack, and Ship Orders

#### UC-024-AF-01 — Customer Pickup Instead of Carrier Shipment

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-024-AF-01 |
| **Starting Step** | 4 |
| **Business Condition** | Customer collects order from warehouse or store rather than carrier delivery. |
| **Alternative Actions** | Warehouse Picker / Packer selects customer pickup dispatch method. System updates order to pickup-ready status. Warehouse Picker / Packer confirms customer collection upon handover. System deducts inventory and records pickup completion without carrier tracking. |
| **Business Outcome** | Order is fulfilled via customer pickup; inventory is deducted and order marked complete. |

#### UC-024-AF-02 — Batch Pick Multiple Orders

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-024-AF-02 |
| **Starting Step** | 2 |
| **Business Condition** | Warehouse efficiency practice combines picking for multiple orders in a single pass through storage areas. |
| **Alternative Actions** | Warehouse Picker / Packer selects batch pick for grouped orders. System generates consolidated pick list organized by storage location. Warehouse Picker / Packer picks and verifies items per order within the batch. System records pick verification per order line across the batch. |
| **Business Outcome** | Multiple orders are picked efficiently; each order proceeds independently to pack and ship steps. |

---

### UC-025 — Handle Partial Fulfillment and Backorders

#### UC-025-AF-01 — Partial Shipment Only, No Backorder

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-025-AF-01 |
| **Starting Step** | 3 |
| **Business Condition** | Customer accepts immediate partial shipment and declines backorder for the remaining quantity. |
| **Alternative Actions** | Customer Service Representative records customer acceptance of partial quantity only. System cancels unfulfilled remainder from order commitment. Customer Service Representative confirms partial fulfillment plan. System reserves and releases available quantity for fulfillment; remaining quantity is removed from order. |
| **Business Outcome** | Order is fulfilled for agreed partial quantity; no backorder obligation remains for declined remainder. |

#### UC-025-AF-02 — Backorder with Replenishment Priority

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-025-AF-02 |
| **Starting Step** | 4 |
| **Business Condition** | Customer accepts backorder and business assigns replenishment priority based on customer tier or product class. |
| **Alternative Actions** | Customer Service Representative confirms backorder with customer acknowledgment. System creates backorder with assigned priority level. Customer Service Representative links backorder to replenishment alert. System queues backorder for fulfillment upon next available supply at priority rank. |
| **Business Outcome** | Backorder is recorded with customer agreement and priority-based fulfillment sequencing. |

---

### UC-026 — Handle Outbound Fulfillment Exceptions

#### UC-026-AF-01 — Authorized Product Substitution

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-026-AF-01 |
| **Starting Step** | 3 |
| **Business Condition** | Original ordered product is unavailable but an authorized substitute SKU is available and approved for the customer order. |
| **Alternative Actions** | Warehouse Manager selects authorized substitution resolution. System presents approved substitute products with ATP. Warehouse Manager confirms substitute SKU and quantity. System updates order line to substitute product, adjusts reservation, and returns order to pick workflow. |
| **Business Outcome** | Order is fulfilled with approved substitute; customer receives equivalent product without order cancellation. |

#### UC-026-AF-02 — Re-Pick from Alternate Storage Location

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-026-AF-02 |
| **Starting Step** | 3 |
| **Business Condition** | Pick failure is resolved by retrieving stock from alternate storage location within the same warehouse. |
| **Alternative Actions** | Warehouse Manager authorizes re-pick from alternate location. System presents alternate location with available quantity. Warehouse Picker / Packer completes re-pick and verification. System records successful pick from alternate location and clears exception. |
| **Business Outcome** | Order fulfillment continues without substitution or cancellation; pick is completed from verified alternate location. |

---

### UC-027 — View Order Fulfillment Status

#### UC-027-AF-01 — Search by Customer Reference

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-027-AF-01 |
| **Starting Step** | 2 |
| **Business Condition** | Customer or service inquiry provides customer reference or purchase order number rather than internal order number. |
| **Alternative Actions** | Customer Service Representative searches by customer reference. System locates matching order(s) and presents search results. Customer Service Representative selects correct order. System displays fulfillment status for the matched order. |
| **Business Outcome** | Order is located and status communicated using customer-provided reference. |

#### UC-027-AF-02 — View Backorder and Expected Supply for Pending Lines

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-027-AF-02 |
| **Starting Step** | 3 |
| **Business Condition** | Order has backordered lines and customer inquiry requires expected availability information. |
| **Alternative Actions** | Customer Service Representative selects backordered lines for detail. System displays backorder quantity, priority, and expected supply date from inbound or replenishment data. Customer Service Representative communicates expected timing to customer. System retains inquiry view with backorder supply visibility. |
| **Business Outcome** | Customer receives informed expectation for backordered line fulfillment. |

---

## Domain 6: Replenishment & Inbound Supply

### UC-028 — Review Low-Stock and Out-of-Stock Alerts

#### UC-028-AF-01 — Delegate Alert Follow-Up to Buyer

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-028-AF-01 |
| **Starting Step** | 4 |
| **Business Condition** | Alert follow-up action is purchase replenishment and Purchasing Manager delegates execution to Buyer. |
| **Alternative Actions** | Purchasing Manager acknowledges alert and assigns follow-up to Buyer. System records assignment and routes alert to Buyer work queue. Buyer accepts assignment. System tracks alert as in-progress under Buyer ownership. |
| **Business Outcome** | Alert follow-up is assigned with clear ownership; replenishment action proceeds under Buyer responsibility. |

#### UC-028-AF-02 — Initiate Transfer Instead of Purchase Response

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-028-AF-02 |
| **Starting Step** | 3 |
| **Business Condition** | Network availability check reveals excess stock at another location sufficient to resolve the alert without new procurement. |
| **Alternative Actions** | Purchasing Manager reviews network availability on alert detail. System shows transfer alternative with source location excess. Purchasing Manager initiates transfer request from alert context. System creates transfer request and links to originating alert. |
| **Business Outcome** | Low-stock condition is addressed through network transfer; procurement is avoided where network stock exists. |

---

### UC-029 — Plan Replenishment and Create Purchase Requisitions

#### UC-029-AF-01 — Create Requisition from System Suggestion

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-029-AF-01 |
| **Starting Step** | 3 |
| **Business Condition** | Buyer accepts system-generated replenishment suggestion without manual quantity modification. |
| **Alternative Actions** | Buyer selects replenishment suggestion and accepts recommended quantity and supplier. System pre-populates requisition from suggestion. Buyer submits requisition for approval. System routes for Purchasing Manager approval. |
| **Business Outcome** | Replenishment requisition is created efficiently from system recommendation with full audit trail. |

#### UC-029-AF-02 — Initiate Transfer Request Instead of Purchase Requisition

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-029-AF-02 |
| **Starting Step** | 2 |
| **Business Condition** | Network check confirms excess stock at another location; transfer is preferred over new purchase. |
| **Alternative Actions** | Buyer selects transfer alternative from replenishment planning view. System presents transfer request form pre-populated from alert context. Buyer submits transfer request. System routes transfer for approval per network balance policy. |
| **Business Outcome** | Replenishment need is addressed through inter-location transfer rather than new procurement. |

---

### UC-030 — Track Inbound Supply Status

#### UC-030-AF-01 — Advance Delivery Date for Early Shipment

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-030-AF-01 |
| **Starting Step** | 3 |
| **Business Condition** | Supplier confirms shipment will arrive earlier than originally scheduled. |
| **Alternative Actions** | Buyer updates expected delivery to earlier date based on supplier confirmation. System revises inbound supply schedule. Buyer notifies receiving location of accelerated arrival. System updates replenishment and alert projections with earlier supply date. |
| **Business Outcome** | Inbound supply visibility reflects early delivery; receiving and replenishment planning adjust accordingly. |

#### UC-030-AF-02 — Review Aggregate Inbound Supply Position

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-030-AF-02 |
| **Starting Step** | 2 |
| **Business Condition** | Buyer reviews total expected inbound supply across all open purchase orders for a product or category rather than a single PO. |
| **Alternative Actions** | Buyer selects product or category aggregate inbound view. System displays total ordered, received, and outstanding across all open POs. Buyer reviews consolidated supply timeline. System presents aggregate inbound position for replenishment planning. |
| **Business Outcome** | Buyer has consolidated view of total inbound supply for informed replenishment and allocation decisions. |

---

## Domain 7: Network Balance & Transfers

### UC-031 — Request Inter-Location Stock Transfer

#### UC-031-AF-01 — Request Reduced Quantity Within Source Limits

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-031-AF-01 |
| **Starting Step** | 2 |
| **Business Condition** | Requested transfer quantity would breach source minimum threshold; requester reduces quantity to compliant level. |
| **Alternative Actions** | Regional / Store Manager reviews source minimum threshold warning. System displays maximum transferable quantity. Regional / Store Manager revises request to compliant quantity. System accepts revised transfer request and proceeds to submission. |
| **Business Outcome** | Transfer request complies with source protection rules; source location service level is preserved. |

#### UC-031-AF-02 — Warehouse Manager Initiates Transfer on Behalf of Store

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-031-AF-02 |
| **Starting Step** | 1 |
| **Business Condition** | Warehouse Manager identifies rebalancing need and initiates transfer request on behalf of a requesting store or regional manager. |
| **Alternative Actions** | Warehouse Manager creates transfer request specifying requesting destination. System records Warehouse Manager as initiator with destination beneficiary. Warehouse Manager completes request with justification. System submits for approval with initiator and beneficiary attribution. |
| **Business Outcome** | Transfer request is initiated by operations staff on behalf of destination; approval workflow proceeds normally. |

---

### UC-032 — Approve or Reject Transfer Requests

#### UC-032-AF-01 — Reject Transfer Request

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-032-AF-01 |
| **Starting Step** | 3 |
| **Business Condition** | Transfer would negatively impact source service level, cost exceeds benefit, or destination need does not justify movement. |
| **Alternative Actions** | Operations Director reviews transfer impact and selects rejection. System prompts for rejection reason. Operations Director documents rejection justification and confirms. System notifies requester, records rejection, and closes transfer request. |
| **Business Outcome** | Transfer request is formally rejected with documented reason; requester can pursue alternate replenishment options. |

#### UC-032-AF-02 — Approve Transfer with Modified Quantity

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-032-AF-02 |
| **Starting Step** | 3 |
| **Business Condition** | Transfer is justified but approved quantity differs from requested quantity to protect source minimum threshold. |
| **Alternative Actions** | Operations Director modifies approved transfer quantity to compliant level. System recalculates source and destination impact. Operations Director approves modified transfer. System notifies locations of approved quantity and updates transfer record. |
| **Business Outcome** | Transfer proceeds at approved quantity that balances destination need with source protection. |

---

### UC-033 — Execute and Record Inter-Location Transfer

#### UC-033-AF-01 — Direct Store-to-Store Transfer

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-033-AF-01 |
| **Starting Step** | 1 |
| **Business Condition** | Transfer moves directly between retail stores without routing through a central distribution warehouse. |
| **Alternative Actions** | Warehouse Staff at source store dispatches transfer to destination store. System records direct store-to-store dispatch and in-transit status. Destination store staff receive and confirm. System completes transfer between store locations without hub involvement. |
| **Business Outcome** | Stock is rebalanced directly between stores with full movement traceability. |

#### UC-033-AF-02 — Receive Partial Transfer with Remainder In-Transit

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-033-AF-02 |
| **Starting Step** | 4 |
| **Business Condition** | Destination receives partial transfer quantity in first delivery with balance to follow in subsequent shipment. |
| **Alternative Actions** | Warehouse Staff at destination confirms partial receipt quantity. System records partial receipt and maintains in-transit balance. Source or carrier delivers remainder. Destination staff confirm final receipt. System closes transfer upon full quantity receipt. |
| **Business Outcome** | Partial transfer receipt is accurately tracked; in-transit quantity remains visible until transfer is complete. |

---

### UC-034 — Analyze and Recommend Network Rebalancing

#### UC-034-AF-01 — Phased Rebalancing Across Multiple Periods

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-034-AF-01 |
| **Starting Step** | 4 |
| **Business Condition** | Operations Director approves subset of rebalancing recommendations for immediate execution and defers remainder to subsequent planning cycle. |
| **Alternative Actions** | Operations Director selects priority recommendations for immediate transfer initiation. System generates transfer requests for selected items. Operations Director defers remaining recommendations with scheduled review date. System tracks deferred recommendations for future rebalancing cycle. |
| **Business Outcome** | Network rebalancing proceeds in manageable phases; deferred items remain in planning queue. |

#### UC-034-AF-02 — Manual Rebalancing Override

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-034-AF-02 |
| **Starting Step** | 2 |
| **Business Condition** | Operations judgment identifies rebalancing need not captured by system recommendations. |
| **Alternative Actions** | Operations Director creates manual rebalancing transfer proposal. System accepts manual source, destination, product, and quantity. Operations Director submits manual proposal for execution. System generates transfer request from manual override with documented justification. |
| **Business Outcome** | Business-directed rebalancing action is initiated outside automated recommendations with full audit trail. |

---

## Domain 8: Returns Management

### UC-035 — Authorize and Record Customer Returns

#### UC-035-AF-01 — Partial Return Authorization

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-035-AF-01 |
| **Starting Step** | 2 |
| **Business Condition** | Customer returns only a subset of order lines or partial quantity within eligible return policy. |
| **Alternative Actions** | Customer Service Representative selects specific lines and quantities for return. System calculates authorized return quantity per line. Customer Service Representative validates eligibility and issues partial return authorization. System generates authorization for selected lines only. |
| **Business Outcome** | Return authorization covers only the returned portion; remaining order lines are unaffected. |

#### UC-035-AF-02 — Exchange Authorization Instead of Refund Return

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-035-AF-02 |
| **Starting Step** | 3 |
| **Business Condition** | Customer requests product exchange rather than refund return per return policy. |
| **Alternative Actions** | Customer Service Representative selects exchange authorization type. System links return authorization to replacement order or product. Customer Service Representative issues exchange authorization with return and replacement details. System generates authorization referencing both return inbound and replacement fulfillment. |
| **Business Outcome** | Exchange is authorized with linked return receipt and replacement order workflow. |

---

### UC-036 — Receive, Inspect, and Disposition Returned Goods

#### UC-036-AF-01 — Restock to Sellable Inventory

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-036-AF-01 |
| **Starting Step** | 4 |
| **Business Condition** | Inspection confirms returned product is in resalable condition meeting quality standards. |
| **Alternative Actions** | Receiving Clerk records inspection outcome as resalable. System accepts restock disposition with reason code. Receiving Clerk confirms restock to sellable inventory. System increases on-hand and ATP at designated location. |
| **Business Outcome** | Returned product re-enters sellable inventory and is available for future fulfillment. |

#### UC-036-AF-02 — Quarantine Return for Further Inspection

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-036-AF-02 |
| **Starting Step** | 4 |
| **Business Condition** | Initial inspection is inconclusive; returned product requires extended quality review before disposition. |
| **Alternative Actions** | Receiving Clerk records inspection outcome as requires further review. System routes disposition to quarantine status. Receiving Clerk confirms quarantine placement. System moves quantity to quarantined hold excluded from ATP. |
| **Business Outcome** | Returned product is held pending definitive disposition; sellable inventory is not affected until review completes. |

#### UC-036-AF-03 — Write-Off Non-Resalable Return

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-036-AF-03 |
| **Starting Step** | 4 |
| **Business Condition** | Inspection confirms returned product is damaged or defective and cannot be restocked. |
| **Alternative Actions** | Receiving Clerk records inspection outcome as non-resalable. System routes disposition to write-off with mandatory reason code. Warehouse Manager or Operations Director authorizes write-off per policy. System removes quantity from inventory and closes return line. |
| **Business Outcome** | Non-resalable return is removed from inventory with documented inspection and authorization. |

---

## Domain 9: Reporting, Performance & Financial Alignment

### UC-037 — Review Inventory Dashboards and Operational Reports

#### UC-037-AF-01 — Dashboard Review Without Detailed Report

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-037-AF-01 |
| **Starting Step** | 2 |
| **Business Condition** | Management needs summary dashboard visibility only without generating a detailed operational report. |
| **Alternative Actions** | Operations Director reviews inventory summary dashboard metrics. System displays real-time KPIs, alert counts, and status distribution. Operations Director identifies areas of concern from dashboard indicators. System supports drill-down from dashboard widgets if further detail is needed. |
| **Business Outcome** | Rapid operational health assessment completed from dashboard without formal report generation. |

#### UC-037-AF-02 — Compare Location Performance Across Periods

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-037-AF-02 |
| **Starting Step** | 3 |
| **Business Condition** | Analysis requires comparison of location performance between two time periods rather than single-period snapshot. |
| **Alternative Actions** | Operations Director selects location performance report with comparative period filter. System generates side-by-side or variance comparison between periods. Operations Director reviews period-over-period changes. System highlights significant shifts in accuracy, stockouts, or movement volume. |
| **Business Outcome** | Location performance trend is understood; improvement or deterioration is identified for management action. |

---

### UC-038 — Review Inventory Performance KPIs

#### UC-038-AF-01 — Executive Summary Review Without Drill-Down

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-038-AF-01 |
| **Starting Step** | 3 |
| **Business Condition** | Executive review session requires Tier 1 KPI summary and RAG status only without detailed contributing factor analysis. |
| **Alternative Actions** | Chief Executive Officer reviews KPI dashboard summary view. System presents Tier 1 metrics with target comparison and RAG indicators. Chief Executive Officer assesses overall inventory program health. System retains summary view for steering committee reference. |
| **Business Outcome** | Executive has concise program health assessment suitable for governance reporting. |

#### UC-038-AF-02 — Year-over-Year KPI Comparison

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-038-AF-02 |
| **Starting Step** | 2 |
| **Business Condition** | Strategic review requires comparison of current period KPIs to same period prior year. |
| **Alternative Actions** | Chief Executive Officer selects year-over-year comparison period. System displays current and prior-year KPI values with variance. Chief Executive Officer reviews long-term trend direction. System presents trend charts for key executive metrics. |
| **Business Outcome** | Strategic progress against inventory objectives is assessed on annual comparison basis. |

---

### UC-039 — Reconcile Inventory Valuation with Finance

#### UC-039-AF-01 — Confirm Alignment Within Tolerance

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-039-AF-01 |
| **Starting Step** | 4 |
| **Business Condition** | Operational valuation and general ledger balance are within defined reconciliation tolerance requiring no adjustment. |
| **Alternative Actions** | Finance Manager compares operational and GL balances. System displays variance within tolerance threshold. Finance Manager documents confirmation of alignment. System records reconciliation as complete with no adjustment required. |
| **Business Outcome** | Period reconciliation is closed confirming operational and financial inventory alignment. |

#### UC-039-AF-02 — Document Reconciling Adjustment

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-039-AF-02 |
| **Starting Step** | 4 |
| **Business Condition** | Variance between operational and GL valuation requires documented reconciling adjustment for finance posting. |
| **Alternative Actions** | Finance Manager identifies reconciling items causing variance. System supports drill-down to contributing transactions. Finance Manager documents reconciling adjustment with finance notes. System records reconciliation with adjustment reference for GL posting. |
| **Business Outcome** | Valuation variance is explained and reconciled; finance has documented basis for period-end adjustment. |

---

## Domain 10: Commercial Alignment & Governance

### UC-040 — Confirm Promotional and Launch Stock Readiness

#### UC-040-AF-01 — Conditional Readiness Pending Inbound Supply

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-040-AF-01 |
| **Starting Step** | 4 |
| **Business Condition** | Campaign readiness is confirmed contingent on expected inbound supply arriving before campaign start date. |
| **Alternative Actions** | Marketing Manager reviews readiness with inbound supply dependency. System displays current ring-fenced stock plus expected inbound before campaign date. Marketing Manager records conditional readiness confirmation with inbound dependency noted. System tracks conditional status and monitors inbound supply against campaign deadline. |
| **Business Outcome** | Campaign readiness is documented with explicit inbound supply dependency; monitoring continues until unconditional confirmation. |

#### UC-040-AF-02 — Request Additional Ring-Fenced Stock Allocation

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-040-AF-02 |
| **Starting Step** | 2 |
| **Business Condition** | Current ring-fenced promotional allocation is insufficient; additional stock must be reserved for the campaign. |
| **Alternative Actions** | Marketing Manager requests increase to ring-fenced promotional allocation. System presents available network stock and current allocations. Operations Director or Purchasing Manager approves additional ring-fence. System increases promotional reservation and updates readiness calculation. |
| **Business Outcome** | Promotional stock ring-fence is increased; campaign readiness reflects expanded committed inventory. |

---

### UC-041 — Conduct Inventory Audit and Control Review

#### UC-041-AF-01 — Statistical Sample Audit

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-041-AF-01 |
| **Starting Step** | 3 |
| **Business Condition** | Audit scope is large; Internal Auditor applies statistical sampling methodology rather than full population review. |
| **Alternative Actions** | Internal Auditor defines sample size and selection criteria. System generates random or stratified sample from scoped population. Internal Auditor reviews sample transactions for control compliance. System supports extrapolation of sample results to population conclusion. |
| **Business Outcome** | Control effectiveness is assessed through valid statistical sample with documented methodology. |

#### UC-041-AF-02 — Location-Scoped Audit Review

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-041-AF-02 |
| **Starting Step** | 2 |
| **Business Condition** | Audit engagement is scoped to specific location rather than enterprise-wide transaction population. |
| **Alternative Actions** | Internal Auditor defines audit scope limited to selected location(s). System retrieves location-scoped transaction population. Internal Auditor performs control testing on location transactions. System generates location-specific audit findings summary. |
| **Business Outcome** | Location-level control compliance is assessed; findings support location-specific corrective action. |

---

## Domain 11: Cross-Cutting System Interactions

### UC-042 — View Inventory Movement and Transaction History

#### UC-042-AF-01 — Search by Product Across All Locations

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-042-AF-01 |
| **Starting Step** | 2 |
| **Business Condition** | Investigation requires all movement history for a product across the entire network without location filter. |
| **Alternative Actions** | Inventory Controller enters product identifier without location constraint. System retrieves all movements for the product across all locations. Inventory Controller reviews network-wide movement chronology. System displays consolidated history with location attribution per transaction. |
| **Business Outcome** | Complete product movement history across network is available for investigation or analysis. |

#### UC-042-AF-02 — Navigate to Audit Trail from Movement Detail

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-042-AF-02 |
| **Starting Step** | 4 |
| **Business Condition** | Movement investigation requires detailed audit trail including before-and-after state beyond standard movement summary. |
| **Alternative Actions** | Inventory Controller selects movement transaction and requests linked audit trail. System presents immutable audit record with before-and-after values. Inventory Controller reviews complete change history for the transaction. System displays audit detail suitable for governance review. |
| **Business Outcome** | Full audit evidence is accessed from movement inquiry for accountability verification. |

---

### UC-043 — Query and Review Audit Trail

#### UC-043-AF-01 — Query Audit Trail by User Activity

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-043-AF-01 |
| **Starting Step** | 2 |
| **Business Condition** | Audit review is focused on all actions performed by a specific user during a defined period. |
| **Alternative Actions** | Internal Auditor defines query by user identity and date range. System retrieves all audit entries for the user in the period. Internal Auditor reviews user activity chronology. System displays complete user action log with entity references. |
| **Business Outcome** | User accountability is assessed through complete activity audit for the review period. |

#### UC-043-AF-02 — Provide Audit Evidence to External Auditor

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-043-AF-02 |
| **Starting Step** | 5 |
| **Business Condition** | External audit engagement requires export of audit trail evidence for independent review. |
| **Alternative Actions** | Internal Auditor prepares scoped audit trail export for external auditor. System generates export package with query parameters documented. External Auditor receives read-only access or exported evidence. System logs external auditor access for compliance record. |
| **Business Outcome** | External auditor receives complete audit evidence package with documented scope and access record. |

---

### UC-044 — Manage User Accounts and Role Assignments

#### UC-044-AF-01 — Modify Existing User Role Assignment

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-044-AF-01 |
| **Starting Step** | 2 |
| **Business Condition** | Existing user requires role change, location scope update, or profile correction rather than new account creation. |
| **Alternative Actions** | System Administrator selects existing user account. System displays current roles and location scope. System Administrator updates role assignment or location scope. System applies changes and confirms updated permissions. |
| **Business Outcome** | User access reflects current job responsibilities without creating duplicate accounts. |

#### UC-044-AF-02 — Deactivate User Account

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-044-AF-02 |
| **Starting Step** | 4 |
| **Business Condition** | User departs organization or changes role no longer requiring system access. |
| **Alternative Actions** | System Administrator selects user account for deactivation. System confirms no pending approvals or sole-authority dependencies. System Administrator deactivates account. System revokes access while preserving user attribution in historical audit records. |
| **Business Outcome** | Departed user can no longer access system; historical transactions retain correct user attribution. |

---

### UC-045 — Enforce Role-Based and Location-Scoped Access

#### UC-045-AF-01 — Update Location Scope for Existing Role

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-045-AF-01 |
| **Starting Step** | 2 |
| **Business Condition** | User role permissions remain unchanged but location scope must be expanded or restricted. |
| **Alternative Actions** | System Administrator selects role and modifies location scope assignment. System validates location definitions and updates scope mapping. System Administrator saves location scope changes. System applies updated scope to all users with the affected role. |
| **Business Outcome** | Users retain role permissions with corrected location access boundaries. |

#### UC-045-AF-02 — Grant Network-Wide Read Access to Executive Role

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-045-AF-02 |
| **Starting Step** | 4 |
| **Business Condition** | Executive or oversight role requires read-only visibility across all locations without transactional authority. |
| **Alternative Actions** | System Administrator configures executive role with network-wide read scope. System applies read-only permission set without transactional grants. Executive user accesses inventory visibility across all locations. System grants read access without location restriction for visibility functions only. |
| **Business Outcome** | Executive stakeholders have network-wide inventory visibility without transactional or approval authority. |

---

### UC-046 — Import Initial Product and Stock Master Data

#### UC-046-AF-01 — Import Product Master Only

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-046-AF-01 |
| **Starting Step** | 2 |
| **Business Condition** | Product catalog is imported first; opening stock balances will be entered separately after physical verification. |
| **Alternative Actions** | Inventory Controller uploads product master import file without stock balances. System validates and imports product records. Inventory Controller reviews product import completion. System confirms product catalog availability; stock balances remain at zero pending separate entry. |
| **Business Outcome** | Product master is loaded; opening balances are deferred for verified physical count entry. |

#### UC-046-AF-02 — Import Updates to Existing Catalog

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-046-AF-02 |
| **Starting Step** | 4 |
| **Business Condition** | Import file updates existing product attributes or stock balances rather than initial go-live load. |
| **Alternative Actions** | Inventory Controller confirms import mode as update to existing records. System matches import records to existing SKUs and applies updates. Inventory Controller reviews update summary showing changed versus unchanged records. System confirms updated catalog and balances. |
| **Business Outcome** | Existing product and stock data is bulk-updated with import audit trail of changes applied. |

---

### UC-047 — Receive and Respond to Operational Notifications

#### UC-047-AF-01 — Delegate Notification to Another Role

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-047-AF-01 |
| **Starting Step** | 3 |
| **Business Condition** | Notification action is outside Warehouse Manager responsibility and must be delegated to Purchasing Manager or Buyer. |
| **Alternative Actions** | Warehouse Manager reassigns notification to appropriate role owner. System routes notification to delegated recipient work queue. Delegated actor accepts and acts on notification. System records delegation chain and action completion. |
| **Business Outcome** | Notification is handled by correct role owner with documented delegation. |

#### UC-047-AF-02 — Defer Notification for Scheduled Follow-Up

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-047-AF-02 |
| **Starting Step** | 5 |
| **Business Condition** | Notification requires action at a future time; immediate handling is not operationally appropriate. |
| **Alternative Actions** | Warehouse Manager schedules notification follow-up for future date or time. System retains notification in deferred queue with reminder. System re-surfaces notification at scheduled time. Warehouse Manager completes action when deferral period ends. |
| **Business Outcome** | Notification is handled at operationally appropriate time without loss of tracking accountability. |

---

### UC-048 — Support Multi-Location Split Fulfillment

#### UC-048-AF-01 — Manual Adjustment of Split Allocation

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-048-AF-01 |
| **Starting Step** | 3 |
| **Business Condition** | Operations judgment requires different location split than system-proposed allocation. |
| **Alternative Actions** | Warehouse Manager modifies proposed quantities per source location. System recalculates ATP impact for revised split. Warehouse Manager confirms adjusted split allocation. System creates reservations per revised location allocation. |
| **Business Outcome** | Multi-location fulfillment reflects operations-approved allocation across source locations. |

#### UC-048-AF-02 — Consolidated Customer Delivery After Multi-Location Ship

| Field | Detail |
|-------|--------|
| **Alternate Flow ID** | UC-048-AF-02 |
| **Starting Step** | 5 |
| **Business Condition** | Multiple location shipments are consolidated at hub before single customer delivery rather than direct multi-shipment to customer. |
| **Alternative Actions** | Warehouse Manager designates consolidation hub location. System tracks in-transit shipments from source locations to hub. Hub receives and consolidates split shipment components. System records consolidated shipment to customer from hub with linked parent order reference. |
| **Business Outcome** | Customer receives single consolidated delivery while inventory deductions reflect multi-location sourcing. |

---

## Summary

| Metric | Count |
|--------|-------|
| Use Cases | 48 |
| Alternate Flows | 96 |
| Average Alternate Flows per Use Case | 2.0 |

---

## Traceability

| Source Document | Reference |
|-----------------|-----------|
| Use Case Catalog | SRS-UC-001 |
| Use Case Main Flows | SRS-UC-002 |
| Business Requirements Document | BRD-IMS-001 |

---

## Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Business Analyst | | | |
| Product Owner | | | |
| Operations Director | | | |

---

*End of Use Case Alternate Flows*

*Document ID: SRS-UC-003 | Version 1.0 | July 5, 2026*
