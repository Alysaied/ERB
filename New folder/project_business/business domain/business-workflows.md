# Business Workflow Descriptions: Inventory Management System

**Document Owner:** Senior Business Analyst  
**Purpose:** Describe the complete business workflow for each inventory management process  
**Scope:** Business activities only — no technical implementation, system design, or automation detail  
**Based On:** Business Process Analysis (32 processes), Business Actor Analysis, and Business Vision

---

## Executive Summary

This document provides end-to-end business workflow descriptions for all **32 inventory management processes**. Each workflow is expressed as a sequence of business activities performed by people and departments, including decision points, alternative paths, end conditions, and expected business outcomes.

Workflows are organized by the nine process domains defined in the business process analysis.

---

## Workflow Index

| ID | Workflow Name | Domain |
|----|---------------|--------|
| WF-01 | Product Master Data Management | Master Data & Governance |
| WF-02 | Location & Warehouse Setup | Master Data & Governance |
| WF-03 | Stock Policy & Threshold Definition | Master Data & Governance |
| WF-04 | ABC Product Classification | Master Data & Governance |
| WF-05 | Purchase Order Placement | Inbound & Receiving |
| WF-06 | Inbound Shipment Planning | Inbound & Receiving |
| WF-07 | Goods Receipt & Verification | Inbound & Receiving |
| WF-08 | Receipt Discrepancy Resolution | Inbound & Receiving |
| WF-09 | Stock Put-Away & Storage | Inbound & Receiving |
| WF-10 | Inventory Status Monitoring | Inventory Control |
| WF-11 | Cycle Counting | Inventory Control |
| WF-12 | Full Physical Inventory Count | Inventory Control |
| WF-13 | Count Variance Investigation & Approval | Inventory Control |
| WF-14 | Stock Adjustment & Write-Off | Inventory Control |
| WF-15 | Shrinkage & Loss Management | Inventory Control |
| WF-16 | Order Availability Confirmation | Order Fulfillment |
| WF-17 | Inventory Reservation | Order Fulfillment |
| WF-18 | Pick, Pack & Ship | Order Fulfillment |
| WF-19 | Partial Fulfillment & Backorder Management | Order Fulfillment |
| WF-20 | Outbound Exception Handling | Order Fulfillment |
| WF-21 | Low-Stock Alert Review | Replenishment |
| WF-22 | Replenishment Planning & Requisition | Replenishment |
| WF-23 | Inbound Supply Tracking | Replenishment |
| WF-24 | Inter-Location Transfer Request | Network Balance |
| WF-25 | Inter-Location Transfer Execution | Network Balance |
| WF-26 | Network Stock Rebalancing | Network Balance |
| WF-27 | Customer Return Intake | Returns |
| WF-28 | Return-to-Stock or Disposal Decision | Returns |
| WF-29 | Inventory Performance Reporting | Performance Management |
| WF-30 | Inventory Valuation & Financial Reconciliation | Financial Alignment |
| WF-31 | Promotional & Launch Stock Readiness | Commercial Alignment |
| WF-32 | Inventory Audit & Control Review | Governance & Compliance |

---

## Domain 1: Master Data & Governance

---

### WF-01: Product Master Data Management

| Attribute | Description |
|-----------|-------------|
| **Workflow Name** | Product Master Data Management |
| **Start Event** | A business need arises to introduce a new product, change an existing product attribute, discontinue a product, or correct a data quality issue |

**Sequential Business Steps**

1. Business stakeholder (purchasing, sales, marketing, or operations) submits a product data request with specifications
2. Inventory Controller reviews the request for completeness and checks for duplicate or conflicting product identifiers
3. Inventory Controller assigns or validates SKU, unit of measure, category, and required tracking attributes
4. Inventory Controller circulates the proposed product record to purchasing and operations for confirmation
5. For new launches, marketing and sales confirm product naming and commercial readiness
6. Finance provides costing reference data where applicable
7. Inventory Controller finalizes the product record and sets status (active, inactive, or discontinued)
8. Inventory Controller communicates the updated product information to affected locations and departments

**Decision Points**

| # | Decision | Options |
|---|----------|---------|
| D1 | Is the product request complete and valid? | Proceed / Return to requester for clarification |
| D2 | Does a duplicate or conflicting SKU already exist? | Merge or correct existing record / Create new record |
| D3 | Do purchasing and operations approve the product definition? | Approve / Revise and resubmit |
| D4 | What is the product status? | Active / Inactive / Discontinued |

**Alternative Paths**

- **Path A — New product introduction:** Full review cycle with all departments before activation
- **Path B — Attribute correction:** Expedited review by Inventory Controller with notification to affected departments
- **Path C — Product discontinuation:** Status changed to discontinued; remaining stock flagged for clearance or write-off planning
- **Path D — Duplicate detected:** Existing record corrected; no new SKU created

**End Condition**

Product record is finalized, approved, and communicated. All locations and departments reference a single consistent product definition.

**Business Outcome**

Accurate, standardized product master data supports reliable ordering, receiving, fulfillment, and reporting across the organization.

---

### WF-02: Location & Warehouse Setup

| Attribute | Description |
|-----------|-------------|
| **Workflow Name** | Location & Warehouse Setup |
| **Start Event** | Leadership approves opening, closing, consolidating, or reorganizing an inventory-holding location |

**Sequential Business Steps**

1. Operations leadership initiates a location change request with business justification
2. Operations team defines location details: name, address, type (warehouse, store, distribution point), and operational scope
3. COO reviews and approves the location within the network design
4. Operations Director assigns a responsible Warehouse Manager or Regional Manager
5. Finance is notified for asset and valuation tracking implications
6. Operations documents the location hierarchy and its position in the network
7. Warehouse Manager prepares the physical location for inventory operations
8. Operations communicates the new or changed location to all affected departments

**Decision Points**

| # | Decision | Options |
|---|----------|---------|
| D1 | Is the location change strategically approved? | Proceed / Defer or reject |
| D2 | Is this a new location, closure, or reorganization? | New / Close / Reorganize |
| D3 | For closures: is remaining stock disposition planned? | Transfer out / Write off / Sell through |

**Alternative Paths**

- **Path A — New location:** Full setup with manager assignment, hierarchy placement, and operational readiness
- **Path B — Location closure:** Stock disposition plan executed before deactivation; location marked inactive
- **Path C — Reorganization:** Hierarchy updated; accountability reassigned without physical closure

**End Condition**

Location is authorized, documented in the network hierarchy, and assigned an accountable manager. Affected departments are informed.

**Business Outcome**

The organization maintains a clear, current map of where inventory is held and who is accountable at each location.

---

### WF-03: Stock Policy & Threshold Definition

| Attribute | Description |
|-----------|-------------|
| **Workflow Name** | Stock Policy & Threshold Definition |
| **Start Event** | A new product is onboarded, demand patterns shift, supplier lead times change, or a performance review identifies chronic stockout or overstock conditions |

**Sequential Business Steps**

1. Inventory Controller identifies products or locations requiring policy review
2. Inventory Controller gathers consumption history, supplier lead times, and ABC classification
3. Sales provides demand forecast input for seasonal or promotional periods
4. Purchasing confirms supplier lead time and order quantity constraints
5. Finance advises on carrying cost implications for high-stock scenarios
6. Inventory Controller calculates proposed reorder levels, minimum thresholds, and safety stock parameters
7. Operations Director reviews and approves policy parameters
8. Inventory Controller publishes updated stock policies and communicates changes to purchasing and warehouse teams

**Decision Points**

| # | Decision | Options |
|---|----------|---------|
| D1 | Is this a new product or a policy revision? | New policy / Revise existing |
| D2 | Are proposed thresholds aligned with lead time and demand? | Approve / Adjust and recalculate |
| D3 | Should this SKU receive priority alert treatment? | Priority / Standard |

**Alternative Paths**

- **Path A — New product:** Initial thresholds set conservatively; flagged for review after 90 days of movement data
- **Path B — Chronic stockout:** Thresholds increased or lead time buffer added; purchasing notified
- **Path C — Chronic overstock:** Thresholds reduced; rebalancing or promotional clearance considered

**End Condition**

Reorder levels and minimum thresholds are defined, approved, and communicated for each reviewed product and location.

**Business Outcome**

Purchasing and operations can proactively identify low-stock conditions and align replenishment with actual business needs.

---

### WF-04: ABC Product Classification

| Attribute | Description |
|-----------|-------------|
| **Workflow Name** | ABC Product Classification |
| **Start Event** | Scheduled semi-annual review date arrives, a significant shift in sales mix occurs, or leadership requests a prioritization review |

**Sequential Business Steps**

1. Inventory Controller initiates the classification review cycle
2. Inventory Controller compiles sales volume, revenue, movement velocity, and margin data per SKU
3. Inventory Controller drafts preliminary A, B, and C classification assignments
4. Cross-functional workshop held with operations, purchasing, sales, and finance
5. Participants challenge and refine classifications based on business judgment
6. Operations Director approves the final classification
7. Inventory Controller publishes the priority product list
8. Inventory Controller updates count schedules and alert priorities to reflect new classifications

**Decision Points**

| # | Decision | Options |
|---|----------|---------|
| D1 | Does data support the proposed classification? | Confirm / Override with business justification |
| D2 | Which class does the SKU belong to? | A (high priority) / B (medium) / C (low) |
| D3 | Are count frequency and alert rules updated accordingly? | Yes / Deferred to next cycle |

**Alternative Paths**

- **Path A — Standard semi-annual review:** Full classification of all active SKUs
- **Path B — Ad-hoc review:** Targeted reclassification for new product lines or major assortment changes
- **Path C — Disputed classification:** Escalated to Operations Director for final decision

**End Condition**

Agreed ABC classification is published and operational priorities (count frequency, alert sensitivity) are aligned.

**Business Outcome**

Operational effort and replenishment focus are directed toward products with the highest business impact.

---

## Domain 2: Inbound & Receiving

---

### WF-05: Purchase Order Placement

| Attribute | Description |
|-----------|-------------|
| **Workflow Name** | Purchase Order Placement |
| **Start Event** | An approved replenishment requisition is received, a low-stock alert is validated, an emergency stockout occurs, or a promotional stock build is authorized |

**Sequential Business Steps**

1. Buyer receives an approved purchase requisition or validated replenishment need
2. Buyer verifies current stock levels and checks for existing open orders to avoid duplication
3. Buyer confirms supplier, product specifications, quantity, and expected delivery date
4. Buyer prepares the purchase order per supplier terms and commercial agreements
5. For orders exceeding financial authority, Purchasing Manager or Finance approves the commitment
6. Warehouse Manager confirms receiving capacity for the expected delivery date
7. Buyer issues the purchase order to the supplier
8. Buyer records the open order commitment and communicates expected inbound stock to receiving and operations

**Decision Points**

| # | Decision | Options |
|---|----------|---------|
| D1 | Is there already sufficient stock or an open order? | Cancel requisition / Reduce quantity / Proceed |
| D2 | Does order value exceed buyer's approval authority? | Buyer proceeds / Escalate to Purchasing Manager or Finance |
| D3 | Can receiving location accept delivery on proposed date? | Confirm date / Negotiate alternate date with supplier |
| D4 | Is this an emergency order? | Standard lead time / Expedited procurement |

**Alternative Paths**

- **Path A — Routine replenishment:** Standard PO issued per supplier lead time
- **Path B — Emergency stockout:** Expedited order with Operations Director awareness; premium freight may be authorized
- **Path C — Promotional pre-build:** Larger quantity ordered per campaign plan; delivery timed to marketing calendar
- **Path D — Duplicate detected:** Order cancelled; existing open PO referenced

**End Condition**

Purchase order is issued to supplier, recorded as inbound commitment, and receiving location is informed of expected delivery.

**Business Outcome**

Inventory is procured in the right quantity and timeframe to maintain availability while avoiding unnecessary duplicate orders.

---

### WF-06: Inbound Shipment Planning

| Attribute | Description |
|-----------|-------------|
| **Workflow Name** | Inbound Shipment Planning |
| **Start Event** | Supplier confirms a purchase order, sends an advance shipment notice, or a freight forwarder provides an expected arrival date |

**Sequential Business Steps**

1. Buyer or purchasing team receives supplier confirmation or shipment notice
2. Buyer updates expected delivery date and shipment contents against the open purchase order
3. Buyer communicates inbound shipment details to the receiving Warehouse Manager
4. Warehouse Manager assesses dock capacity, staffing, and storage space for the expected arrival
5. Warehouse Manager schedules receiving resources for the delivery window
6. Operations and sales are informed of inbound stock for availability planning
7. For consolidated or international shipments, freight forwarder ETA is coordinated with receiving schedule

**Decision Points**

| # | Decision | Options |
|---|----------|---------|
| D1 | Does receiving location have capacity on expected date? | Accept schedule / Request delivery reschedule |
| D2 | Is shipment content aligned with purchase order? | Aligned / Flag discrepancy for receiving |
| D3 | Should sales and operations be notified of inbound stock? | Notify (out-of-stock or priority SKU) / Standard processing |

**Alternative Paths**

- **Path A — Standard domestic delivery:** Routine scheduling with receiving team
- **Path B — Large or consolidated shipment:** Additional staffing and storage preparation
- **Path C — Delivery date conflict:** Buyer negotiates reschedule with supplier; operations informed of delay

**End Condition**

Receiving location is prepared for the inbound shipment and stakeholders have visibility of expected stock arrival.

**Business Outcome**

Inbound deliveries are processed promptly upon arrival without dock congestion, staffing gaps, or storage overflow.

---

### WF-07: Goods Receipt & Verification

| Attribute | Description |
|-----------|-------------|
| **Workflow Name** | Goods Receipt & Verification |
| **Start Event** | A supplier shipment physically arrives at the warehouse or store receiving dock |

**Sequential Business Steps**

1. Receiving Clerk accepts the delivery and obtains delivery documentation from the carrier or supplier
2. Receiving Clerk identifies the shipment against the corresponding purchase order
3. Receiving Clerk inspects packaging condition and notes visible damage
4. Receiving Clerk counts received quantities and verifies product identity against the packing list
5. Receiving Clerk compares received quantities to the purchase order expected quantities
6. Receiving Clerk formally records the goods receipt with product, quantity, and location
7. On-hand inventory is updated to reflect received stock
8. Receiving Clerk notifies Warehouse Manager of receipt completion or flags discrepancies

**Decision Points**

| # | Decision | Options |
|---|----------|---------|
| D1 | Does the shipment match the purchase order reference? | Match / No matching PO — hold for purchasing |
| D2 | Are received quantities equal to expected quantities? | Match / Variance — initiate discrepancy workflow |
| D3 | Is product condition acceptable? | Accept / Reject damaged goods — initiate discrepancy workflow |
| D4 | Are product identifiers correct? | Correct / Wrong item — initiate discrepancy workflow |

**Alternative Paths**

- **Path A — Clean receipt:** Full quantity received in good condition; proceeds to put-away
- **Path B — Quantity variance:** Triggers WF-08 Receipt Discrepancy Resolution
- **Path C — Damage or wrong item:** Triggers WF-08; acceptable portion may be received separately
- **Path D — No matching PO:** Shipment held; purchasing investigates before receipt is recorded

**End Condition**

Received goods are verified, recorded, and on-hand inventory reflects the accepted quantities. Discrepancies are flagged if present.

**Business Outcome**

Inventory records accurately reflect physical goods received, providing a trustworthy foundation for fulfillment and replenishment decisions.

---

### WF-08: Receipt Discrepancy Resolution

| Attribute | Description |
|-----------|-------------|
| **Workflow Name** | Receipt Discrepancy Resolution |
| **Start Event** | Receiving Clerk identifies a quantity mismatch, damaged goods, or incorrect items during goods receipt verification |

**Sequential Business Steps**

1. Receiving Clerk documents the discrepancy with quantities, product details, and condition evidence
2. Warehouse Manager reviews the discrepancy report and validates physical evidence
3. Warehouse Manager determines discrepancy type: short shipment, over-shipment, damage, or wrong item
4. Buyer contacts the supplier to report the discrepancy and request resolution
5. Supplier responds with credit, replacement shipment, or dispute of the claim
6. For accepted resolutions, Receiving Clerk records the corrected receipt quantities
7. Finance processes supplier credit or adjusts payment as applicable
8. Warehouse Manager closes the discrepancy case with documented resolution

**Decision Points**

| # | Decision | Options |
|---|----------|---------|
| D1 | What type of discrepancy occurred? | Short / Over / Damage / Wrong item |
| D2 | Should physically acceptable portion be received now? | Receive partial / Hold entire shipment |
| D3 | Does supplier accept the discrepancy claim? | Accepted / Disputed |
| D4 | For disputes: is escalation required? | Resolve commercially / Escalate to Purchasing Manager |

**Alternative Paths**

- **Path A — Short shipment accepted:** Partial receipt recorded; supplier credit or balance shipment arranged
- **Path B — Damage rejected:** Goods not added to inventory; supplier replacement or credit pursued
- **Path C — Over-shipment:** Purchasing decides to accept excess (new PO or return excess to supplier)
- **Path D — Supplier dispute:** Purchasing Manager negotiates; may involve Finance and legal review

**End Condition**

Discrepancy is resolved with corrected inventory records, supplier accountability documented, and financial adjustment processed if applicable.

**Business Outcome**

Inventory accuracy is protected, supplier performance is tracked, and receipt disputes are resolved with clear accountability.

---

### WF-09: Stock Put-Away & Storage

| Attribute | Description |
|-----------|-------------|
| **Workflow Name** | Stock Put-Away & Storage |
| **Start Event** | Goods receipt verification is completed and verified stock awaits placement in storage |

**Sequential Business Steps**

1. Warehouse Manager assigns put-away tasks based on product type, volume, and storage availability
2. Warehouse staff retrieves accepted goods from the receiving area
3. Warehouse staff moves goods to the designated storage location within the warehouse
4. Warehouse staff confirms placement and organizes stock for accessibility
5. Warehouse Manager verifies put-away completion
6. Stock is confirmed as available and locatable for picking or transfer

**Decision Points**

| # | Decision | Options |
|---|----------|---------|
| D1 | Is designated storage location available? | Use assigned location / Assign alternate location |
| D2 | Does product require special handling? | Standard storage / Special handling area |
| D3 | Is put-away completed same business day? | Completed / Queued for next shift |

**Alternative Paths**

- **Path A — Standard put-away:** Goods moved to regular storage location same day
- **Path B — Storage capacity constraint:** Warehouse Manager assigns overflow location; rebalancing planned
- **Path C — Special handling required:** Goods placed in designated area (fragile, temperature-sensitive, high-value)

**End Condition**

Received goods are physically stored in assigned locations and confirmed as available for operational use.

**Business Outcome**

Stock is organized, locatable, and ready for efficient picking and fulfillment.

---

## Domain 3: Inventory Control

---

### WF-10: Inventory Status Monitoring

| Attribute | Description |
|-----------|-------------|
| **Workflow Name** | Inventory Status Monitoring |
| **Start Event** | Business day begins, an inventory movement occurs, management requests a status review, or a threshold breach is detected |

**Sequential Business Steps**

1. Operations or Inventory Controller reviews current stock balances across all locations
2. Reserved and committed quantities are identified separately from total on-hand stock
3. Available-to-promise quantities are calculated for each product and location
4. Stock status is classified as in stock, low stock, or out of stock against defined thresholds
5. Exception alerts are generated for low-stock, out-of-stock, and overstock conditions
6. Alerts are routed to purchasing, operations, and sales as appropriate
7. Management reviews network-wide inventory health summary
8. Identified exceptions trigger downstream processes (replenishment, transfer, or escalation)

**Decision Points**

| # | Decision | Options |
|---|----------|---------|
| D1 | Is stock level below reorder threshold? | Trigger low-stock review / No action |
| D2 | Is product out of stock? | Escalate urgently / Monitor if inbound stock expected |
| D3 | Is location experiencing overstock? | Flag for rebalancing / No action |
| D4 | Does sales or management need proactive notification? | Notify / Standard monitoring |

**Alternative Paths**

- **Path A — Normal status:** Routine monitoring; no exceptions
- **Path B — Low-stock detected:** Triggers WF-21 Low-Stock Alert Review
- **Path C — Out-of-stock on priority SKU:** Urgent escalation to purchasing and operations
- **Path D — Overstock identified:** Flagged for WF-26 Network Stock Rebalancing

**End Condition**

Current inventory status is visible across the organization; exceptions are identified and routed to appropriate processes.

**Business Outcome**

Decision-makers have timely, accurate visibility of what stock exists, where it is, and what is available for sale or fulfillment.

---

### WF-11: Cycle Counting

| Attribute | Description |
|-----------|-------------|
| **Workflow Name** | Cycle Counting |
| **Start Event** | A scheduled count assignment arises per the count calendar, or a specific SKU is flagged for verification |

**Sequential Business Steps**

1. Inventory Controller issues count assignments per the cycle count schedule (by location, category, or ABC class)
2. Warehouse Manager assigns counters and provides count instructions
3. Counters physically count assigned products at the designated location
4. Counters record physical quantities found
5. Counters submit count results to Warehouse Manager
6. Warehouse Manager compares physical counts to recorded on-hand balances
7. Variances within tolerance are noted; variances exceeding tolerance are flagged
8. Count completion is confirmed and results forwarded for variance investigation if needed

**Decision Points**

| # | Decision | Options |
|---|----------|---------|
| D1 | Does physical count match recorded balance within tolerance? | Match — close count / Variance — investigate |
| D2 | Is a recount required? | Accept count / Recount before submission |
| D3 | Should counting continue without disrupting fulfillment? | Count during operations / Count during low-activity window |

**Alternative Paths**

- **Path A — Count matches:** Count closed; no further action
- **Path B — Variance within tolerance:** Noted and recorded; may be batch-adjusted per policy
- **Path C — Variance exceeds tolerance:** Triggers WF-13 Count Variance Investigation
- **Path D — Recount requested:** Counter repeats count before submission

**End Condition**

Assigned products are physically counted, results are recorded, and variances are identified for follow-up.

**Business Outcome**

Inventory accuracy is maintained through regular verification without requiring disruptive full-location shutdowns.

---

### WF-12: Full Physical Inventory Count

| Attribute | Description |
|-----------|-------------|
| **Workflow Name** | Full Physical Inventory Count |
| **Start Event** | Annual or semi-annual count calendar date arrives, audit requires substantiation, or leadership mandates a baseline count |

**Sequential Business Steps**

1. Inventory Controller plans the full count: date, team assignments, methodology, and operational impact minimization
2. Operations Director approves the count plan and communicates to the location
3. Warehouse Manager prepares the location: organizes stock, clears receiving area, briefs count teams
4. Finance and Internal Auditor are notified of count schedule
5. Count teams systematically count all products across all storage areas
6. Team leads verify count sheets for completeness and accuracy
7. Inventory Controller compiles total count results and compares to recorded inventory
8. Variance report is produced for the entire location
9. Operations Director and Finance review results; significant variances trigger investigation

**Decision Points**

| # | Decision | Options |
|---|----------|---------|
| D1 | Is the location prepared for full count? | Proceed / Reschedule |
| D2 | Are all areas and SKUs counted? | Complete / Identify gaps and recount |
| D3 | Is total location variance within acceptable range? | Accept baseline / Full investigation required |
| D4 | Does result require financial adjustment? | Yes — reconciliation / No — confirm and close |

**Alternative Paths**

- **Path A — Clean count:** Baseline confirmed; location accuracy certified
- **Path B — Material variances:** Triggers WF-13 for significant items; may trigger WF-14 adjustments
- **Path C — Count incomplete:** Gaps identified; partial recount before finalization
- **Path D — Audit-driven count:** External Auditor observes; evidence package prepared

**End Condition**

All inventory at the location is counted, results are compiled, variances are documented, and baseline position is established or corrected.

**Business Outcome**

A verified inventory position supports financial reporting, audit requirements, and correction of accumulated discrepancies.

---

### WF-13: Count Variance Investigation & Approval

| Attribute | Description |
|-----------|-------------|
| **Workflow Name** | Count Variance Investigation & Approval |
| **Start Event** | A cycle count or full count identifies a quantity variance exceeding the defined tolerance |

**Sequential Business Steps**

1. Warehouse Manager or Inventory Controller receives the variance report
2. Investigator reviews recent transaction history for the affected SKU and location
3. Investigator interviews warehouse staff about recent activity, misplacement, or known issues
4. If uncertainty remains, a physical recount is ordered
5. Investigator determines probable root cause (process error, theft, damage, misplacement, recording error)
6. Investigator prepares an adjustment recommendation with reason code and supporting evidence
7. Warehouse Manager or Inventory Controller approves variances within their authority
8. Significant variances are escalated to Operations Director for approval
9. Approved adjustment is executed; rejected variances require further investigation

**Decision Points**

| # | Decision | Options |
|---|----------|---------|
| D1 | Is recount consistent with original count? | Confirm variance / Dispute — recount again |
| D2 | Is root cause identifiable? | Identified / Unexplained — escalate |
| D3 | Is adjustment within approver's authority? | Approve locally / Escalate to Operations Director |
| D4 | Should adjustment be approved? | Approve / Reject — continue investigation |

**Alternative Paths**

- **Path A — Explained variance:** Adjustment approved with documented root cause
- **Path B — Unexplained variance:** Escalated for loss prevention review; may trigger WF-15
- **Path C — Recount eliminates variance:** No adjustment; original count error documented
- **Path D — High-value variance:** Operations Director and Finance review before approval

**End Condition**

Variance is investigated, root cause is documented, and adjustment is approved or rejected with full accountability.

**Business Outcome**

Inventory corrections are justified, authorized, and traceable — protecting accuracy and internal control.

---

### WF-14: Stock Adjustment & Write-Off

| Attribute | Description |
|-----------|-------------|
| **Workflow Name** | Stock Adjustment & Write-Off |
| **Start Event** | An approved count variance, discovered damage, obsolescence, theft, loss, or data correction requires an inventory balance change |

**Sequential Business Steps**

1. Initiator (Warehouse Manager or Inventory Controller) prepares an adjustment request
2. Initiator specifies product, location, quantity, direction (increase or decrease), and mandatory reason code
3. Initiator attaches supporting evidence (photos, incident report, count sheet, approval reference)
4. Approver reviews the request against policy thresholds and segregation of duties rules
5. Approver approves or rejects the adjustment
6. For write-offs, Finance is notified for financial recording
7. Approved adjustment is applied to inventory balance
8. Adjustment is documented with initiator, approver, reason, and timestamp

**Decision Points**

| # | Decision | Options |
|---|----------|---------|
| D1 | Is reason code valid and evidence sufficient? | Proceed / Return for more documentation |
| D2 | Is adjustment value within approver's authority? | Approve / Escalate to Operations Director or COO |
| D3 | Is this a write-off requiring financial treatment? | Write-off / Correction only |
| D4 | Does segregation of duties allow this approver to act? | Approve / Reassign to independent approver |

**Alternative Paths**

- **Path A — Routine correction:** Approved by Warehouse Manager or Inventory Controller
- **Path B — High-value write-off:** Escalated to Operations Director and Finance
- **Path C — Rejected adjustment:** Returned to initiator; further investigation required
- **Path D — Obsolescence write-off:** Finance records financial impact; product may be marked discontinued

**End Condition**

Inventory balance reflects the approved adjustment with full documentation and appropriate financial treatment.

**Business Outcome**

Inventory records are corrected with accountability, supporting accurate operations and financial reporting.

---

### WF-15: Shrinkage & Loss Management

| Attribute | Description |
|-----------|-------------|
| **Workflow Name** | Shrinkage & Loss Management |
| **Start Event** | Monthly review cycle begins, recurring variance patterns emerge, an audit finding is issued, or a significant adjustment event occurs |

**Sequential Business Steps**

1. Inventory Controller compiles adjustment, write-off, and variance data for the review period
2. Inventory Controller analyzes trends by location, product category, and reason code
3. Inventory Controller identifies locations or SKUs with abnormal shrinkage rates
4. Inventory Controller presents findings to Operations Director and Finance
5. Team investigates root causes: process failures, training gaps, theft risk, or supplier quality
6. Corrective action plan is developed (process change, additional counts, training, security measures)
7. Operations Director assigns accountability and timelines for corrective actions
8. Internal Auditor is informed of significant control concerns
9. Progress against corrective actions is reviewed in the following cycle

**Decision Points**

| # | Decision | Options |
|---|----------|---------|
| D1 | Is shrinkage rate within acceptable threshold? | Monitor / Investigate |
| D2 | Is root cause operational, criminal, or supplier-related? | Operational fix / Security escalation / Supplier action |
| D3 | Are corrective actions sufficient? | Close review / Continue monitoring |
| D4 | Should audit or leadership be escalated? | Escalate / Manage within operations |

**Alternative Paths**

- **Path A — Normal shrinkage:** Documented and monitored; no action required
- **Path B — Location-specific spike:** Targeted investigation and corrective plan for that location
- **Path C — Suspected theft or fraud:** Escalated to leadership and Internal Auditor
- **Path D — Process failure identified:** Training and procedure update implemented

**End Condition**

Shrinkage is analyzed, root causes are addressed, and corrective actions are assigned with follow-up scheduled.

**Business Outcome**

Inventory loss is reduced over time through systematic analysis and targeted improvement actions.

---

## Domain 4: Order Fulfillment

---

### WF-16: Order Availability Confirmation

| Attribute | Description |
|-----------|-------------|
| **Workflow Name** | Order Availability Confirmation |
| **Start Event** | A customer places an order, a sales quote is requested, or a large or strategic order requires feasibility review |

**Sequential Business Steps**

1. Sales Representative or Customer Service receives the customer order or quote request
2. Agent identifies required products, quantities, and requested delivery date
3. Agent checks available-to-promise stock across potential fulfillment locations
4. Agent considers inbound expected stock if current availability is insufficient
5. For large orders, Sales Manager or Operations is consulted on fulfillment capacity
6. Agent determines whether the full order can be fulfilled from a single location or requires split fulfillment
7. Agent confirms availability and realistic delivery date to the customer, or identifies shortfall
8. If shortfall exists, agent communicates alternative options (partial delivery, backorder, substitute, revised date)

**Decision Points**

| # | Decision | Options |
|---|----------|---------|
| D1 | Is sufficient stock available at any single location? | Confirm / Check alternate locations |
| D2 | Will inbound stock arrive in time for requested delivery? | Include in commitment / Cannot meet date |
| D3 | Is this a large or strategic order requiring management review? | Standard confirmation / Escalate to Sales Manager or Operations |
| D4 | Can customer accept partial or delayed fulfillment? | Full commitment / Partial or backorder — triggers WF-19 |

**Alternative Paths**

- **Path A — Full availability:** Order confirmed with delivery commitment; proceeds to WF-17
- **Path B — Partial availability:** Customer offered partial shipment; WF-19 if accepted
- **Path C — No availability:** Backorder or cancellation discussed; purchasing alerted for replenishment
- **Path D — Multi-location fulfillment:** Split shipment planned across locations

**End Condition**

Customer receives a confirmed availability response or clear explanation of shortfall and alternatives.

**Business Outcome**

Sales commitments align with actual stock capability, reducing order failures and customer disappointment.

---

### WF-17: Inventory Reservation

| Attribute | Description |
|-----------|-------------|
| **Workflow Name** | Inventory Reservation |
| **Start Event** | A customer order is confirmed for fulfillment, or stock arrives to fulfill a previously backordered line |

**Sequential Business Steps**

1. Operations or Warehouse Manager receives the confirmed order for fulfillment
2. Fulfillment team identifies the optimal location based on stock availability and proximity to customer
3. Team reserves the required quantity against on-hand stock at the selected location
4. Reserved stock is tied to the specific order and removed from available-to-promise balance
5. Order is placed in the fulfillment queue with reservation confirmation
6. Sales and Customer Service are notified that the order is reserved and queued for picking
7. For backorder fulfillment, newly arrived stock is reserved against waiting backorder lines in priority sequence

**Decision Points**

| # | Decision | Options |
|---|----------|---------|
| D1 | Which location should fulfill the order? | Primary location / Alternate location |
| D2 | Is full quantity available for reservation? | Reserve full / Reserve partial — triggers WF-19 |
| D3 | Is this a priority or expedited order? | Standard queue / Priority queue |
| D4 | For backorders: which waiting orders receive new stock first? | Priority rules (date, customer tier, SKU class) |

**Alternative Paths**

- **Path A — Full reservation:** Entire order reserved; proceeds to WF-18
- **Path B — Partial reservation:** Available quantity reserved; remainder on backorder per WF-19
- **Path C — Reservation failure:** Stock no longer available (race condition); reverts to WF-16
- **Path D — Backorder release:** Inbound stock received; backorder lines reserved in sequence

**End Condition**

Stock is committed to the order, protected from other allocations, and the order is queued for fulfillment.

**Business Outcome**

Orders are fulfilled against genuinely available stock; overselling and double-allocation are prevented.

---

### WF-18: Pick, Pack & Ship

| Attribute | Description |
|-----------|-------------|
| **Workflow Name** | Pick, Pack & Ship |
| **Start Event** | A reserved order is released to the warehouse fulfillment queue or a daily pick wave is initiated |

**Sequential Business Steps**

1. Warehouse Manager releases reserved orders to the pick queue (or schedules a pick wave)
2. Picker receives pick list with product, quantity, and storage location
3. Picker travels to storage location and retrieves the specified products
4. Picker verifies product identity and quantity at the pick point
5. Picker reports any unable-to-pick situations to Warehouse Manager
6. Packer consolidates picked items, packs per shipping standards, and prepares shipment documentation
7. Packer confirms packed order is complete and applies shipping labels
8. Shipment is handed off to the carrier with tracking information recorded
9. Inventory is deducted upon shipment confirmation
10. Customer Service is notified of shipment for customer communication

**Decision Points**

| # | Decision | Options |
|---|----------|---------|
| D1 | Can picker locate and retrieve full quantity? | Complete pick / Exception — triggers WF-20 |
| D2 | Is product condition acceptable at pick? | Accept / Damaged — triggers WF-20 |
| D3 | Is order packed and ready for carrier? | Ship / Hold for additional items (partial fulfillment) |
| D4 | Is this a priority or expedited shipment? | Standard carrier / Expedited shipping |

**Alternative Paths**

- **Path A — Clean pick and ship:** Full order shipped; inventory deducted; customer notified
- **Path B — Pick exception:** WF-20 Outbound Exception Handling triggered
- **Path C — Partial pick:** Available items shipped; remainder handled per WF-19
- **Path D — Carrier failed pickup:** WF-20 triggered; shipment held for rebooking

**End Condition**

Order is physically packed, handed to carrier, inventory is deducted, and shipment confirmation is communicated.

**Business Outcome**

Customer orders are physically fulfilled and inventory records reflect the outbound movement accurately.

---

### WF-19: Partial Fulfillment & Backorder Management

| Attribute | Description |
|-----------|-------------|
| **Workflow Name** | Partial Fulfillment & Backorder Management |
| **Start Event** | Full order quantity cannot be fulfilled at reservation or pick time, and customer policy allows partial delivery |

**Sequential Business Steps**

1. Warehouse Manager or Operations identifies the unfulfillable portion of the order
2. Available quantity is confirmed for immediate shipment
3. Customer Service contacts the customer to explain partial shipment and revised delivery for remaining items
4. Customer accepts or rejects the partial delivery proposal
5. If accepted, available items are shipped per WF-18
6. Remaining quantity is placed on backorder with expected availability date
7. Purchasing is alerted to expedite replenishment for backordered SKUs
8. When inbound stock arrives, backordered lines are fulfilled per WF-17 priority rules
9. Customer Service notifies customer when backordered items ship

**Decision Points**

| # | Decision | Options |
|---|----------|---------|
| D1 | Does customer accept partial shipment? | Accept / Reject — cancel or wait for full order |
| D2 | Is expected replenishment date known? | Communicate ETA / Uncertain — provide range or cancel option |
| D3 | Should transfer from another location be considered? | Initiate WF-24 / Wait for supplier replenishment |
| D4 | How long will backorder be held before cancellation? | Per policy timeline / Customer agreement |

**Alternative Paths**

- **Path A — Partial accepted:** Partial shipment sent; backorder tracked to completion
- **Path B — Customer rejects partial:** Entire order held or cancelled per customer preference
- **Path C — Transfer resolves backorder:** WF-24 initiated to source stock from another location
- **Path D — Backorder cancelled:** Customer cancels waiting portion; reservation released

**End Condition**

Customer is informed, partial shipment is delivered if accepted, and backordered lines are tracked to resolution or cancellation.

**Business Outcome**

Revenue is partially preserved during stock constraints, customer expectations are managed, and backorders are resolved systematically.

---

### WF-20: Outbound Exception Handling

| Attribute | Description |
|-----------|-------------|
| **Workflow Name** | Outbound Exception Handling |
| **Start Event** | A picker reports unable-to-pick, damaged item at pick, customer cancellation, or carrier failed pickup or delivery |

**Sequential Business Steps**

1. Exception is reported by picker, carrier, or customer service to Warehouse Manager
2. Warehouse Manager assesses the exception type and impact on the order
3. For stock-not-found: physical search of location conducted; inventory record investigated
4. For damaged item: product quarantined; stock adjustment initiated if needed
5. For customer cancellation: reservation released; picked items returned to stock if applicable
6. Warehouse Manager determines resolution: re-pick, substitute product, partial ship, cancel, or adjust inventory
7. Customer Service communicates resolution to the customer
8. If inventory record error is found, WF-14 adjustment is initiated
9. Recurring exceptions at same location or SKU are reported to Inventory Controller

**Decision Points**

| # | Decision | Options |
|---|----------|---------|
| D1 | What type of exception occurred? | Stock not found / Damage / Cancellation / Carrier failure |
| D2 | Can the order still be fulfilled? | Re-pick or substitute / Partial / Cancel |
| D3 | Is inventory record inaccurate? | Adjust inventory / No adjustment — one-time event |
| D4 | Is substitute product acceptable to customer? | Substitute / Cancel line / Wait for correct product |

**Alternative Paths**

- **Path A — Stock found on re-search:** Pick completed normally
- **Path B — Inventory record error:** Adjustment made; order re-queued or cancelled
- **Path C — Customer cancellation:** Reservation released; order closed
- **Path D — Substitute accepted:** Alternative product shipped with customer approval

**End Condition**

Exception is resolved, order status is updated, inventory is corrected if needed, and customer is informed.

**Business Outcome**

Fulfillment disruptions are resolved with minimal customer impact and inventory accuracy is maintained.

---

## Domain 5: Replenishment

---

### WF-21: Low-Stock Alert Review

| Attribute | Description |
|-----------|-------------|
| **Workflow Name** | Low-Stock Alert Review |
| **Start Event** | Stock level falls below the defined reorder threshold, a product goes out of stock, or a priority SKU alert is generated |

**Sequential Business Steps**

1. Purchasing team receives low-stock or out-of-stock alert
2. Buyer reviews current on-hand, reserved, and available quantities
3. Buyer checks for existing open purchase orders covering the same product
4. Buyer reviews recent consumption trend to validate alert is not a false positive
5. For priority (A-class) SKUs, buyer escalates urgency to Purchasing Manager
6. Buyer determines whether replenishment, transfer, or demand adjustment is the appropriate response
7. Validated replenishment need is forwarded to WF-22, or false alert is dismissed with documented reason
8. For out-of-stock priority items, operations and sales are notified of expected resolution timeline

**Decision Points**

| # | Decision | Options |
|---|----------|---------|
| D1 | Is the alert valid (not a false positive from data timing)? | Valid / Dismiss with reason |
| D2 | Is stock already on order? | Monitor open PO / Initiate new replenishment |
| D3 | Can a transfer resolve the condition faster than purchasing? | Initiate WF-24 / Proceed to replenishment |
| D4 | Is this a priority SKU requiring emergency action? | Emergency escalation / Standard replenishment |

**Alternative Paths**

- **Path A — Valid alert, no open order:** Proceeds to WF-22 Replenishment Planning
- **Path B — Stock already on order:** Alert dismissed; WF-23 tracks inbound supply
- **Path C — Transfer faster than purchase:** WF-24 initiated instead of new PO
- **Path D — False alert:** Dismissed; threshold may be reviewed in WF-03

**End Condition**

Alert is validated or dismissed, and appropriate replenishment or transfer action is initiated.

**Business Outcome**

Stockouts are prevented through timely, validated response to low-stock conditions.

---

### WF-22: Replenishment Planning & Requisition

| Attribute | Description |
|-----------|-------------|
| **Workflow Name** | Replenishment Planning & Requisition |
| **Start Event** | A validated low-stock alert is received, a scheduled replenishment cycle runs, or a promotional stock build is authorized |

**Sequential Business Steps**

1. Buyer or Purchasing Manager receives the validated replenishment need
2. Planner reviews movement history, lead time, and current stock position
3. Planner calculates recommended order quantity considering economic order size and budget
4. Planner checks budget availability for the proposed purchase
5. Planner prepares a purchase requisition with product, quantity, supplier, and rationale
6. Purchasing Manager reviews and approves the requisition within authority limits
7. For requisitions exceeding authority, Finance or COO approval is obtained
8. Approved requisition is handed to WF-05 Purchase Order Placement

**Decision Points**

| # | Decision | Options |
|---|----------|---------|
| D1 | What order quantity is appropriate? | Standard replenishment qty / Adjusted for promotion or seasonality |
| D2 | Is budget available? | Approve / Defer or reduce quantity |
| D3 | Does requisition require escalation? | Purchasing Manager approves / Escalate to Finance or COO |
| D4 | Should multiple SKUs be combined into one supplier order? | Combined order / Separate orders |

**Alternative Paths**

- **Path A — Standard replenishment:** Routine requisition approved and PO placed
- **Path B — Budget-constrained:** Quantity reduced or order deferred; sales and operations informed
- **Path C — Promotional pre-build:** Larger quantity approved per campaign plan WF-31
- **Path D — Multi-SKU consolidation:** Single PO covering multiple replenishment needs from same supplier

**End Condition**

Approved purchase requisition is prepared and handed off for purchase order placement.

**Business Outcome**

Replenishment decisions are deliberate, budget-aware, and converted into actionable procurement.

---

### WF-23: Inbound Supply Tracking

| Attribute | Description |
|-----------|-------------|
| **Workflow Name** | Inbound Supply Tracking |
| **Start Event** | A purchase order is placed, supplier confirms shipment, a delivery delay is reported, or a stakeholder inquires about expected stock |

**Sequential Business Steps**

1. Buyer monitors all open purchase orders daily
2. Buyer follows up with suppliers on orders approaching or past expected delivery date
3. Buyer updates expected arrival dates based on supplier and freight forwarder communications
4. Buyer communicates revised ETAs to operations, warehouse, and sales for priority items
5. For delayed shipments, Buyer escalates to Purchasing Manager and explores alternatives
6. Customer Service and Sales are updated on inbound stock for backorder and availability inquiries
7. Upon receipt, Buyer confirms order closure and updates inbound supply status

**Decision Points**

| # | Decision | Options |
|---|----------|---------|
| D1 | Is delivery on schedule? | Monitor / Follow up with supplier |
| D2 | Is delay material to stockout risk? | Notify operations and sales / Standard tracking |
| D3 | Should alternative supply be sought? | Expedite / Alternate supplier / Wait |
| D4 | Has shipment been received and closed? | Close PO / Continue tracking |

**Alternative Paths**

- **Path A — On schedule:** Routine monitoring until receipt
- **Path B — Minor delay:** ETA updated; stakeholders informed if priority SKU
- **Path C — Critical delay:** Escalation; emergency procurement or transfer considered
- **Path D — Received:** PO closed; backorder fulfillment triggered per WF-17

**End Condition**

Open purchase orders are tracked to receipt or resolution; stakeholders have current inbound supply visibility.

**Business Outcome**

Operations, sales, and customer service can communicate realistic stock arrival expectations to customers and internal teams.

---

## Domain 6: Network Balance

---

### WF-24: Inter-Location Transfer Request

| Attribute | Description |
|-----------|-------------|
| **Workflow Name** | Inter-Location Transfer Request |
| **Start Event** | A location experiences stockout or low stock, another location has excess, a sales request requires specific location fulfillment, or a network rebalancing review identifies need |

**Sequential Business Steps**

1. Requester (Regional Manager, Sales, or Operations) identifies the transfer need with product, quantity, source, and destination
2. Requester verifies source location has available (unreserved) stock
3. Requester submits transfer request with business justification
4. Operations Director or Warehouse Manager at source location reviews availability impact
5. Approver assesses transfer cost, urgency, and impact on source location service levels
6. Transfer is approved, modified, or rejected with documented reason
7. Approved transfer authorization is communicated to source and destination Warehouse Managers

**Decision Points**

| # | Decision | Options |
|---|----------|---------|
| D1 | Does source location have unreserved excess stock? | Proceed / Reject — insufficient stock |
| D2 | Is transfer justified vs. waiting for replenishment? | Approve transfer / Reject — purchase instead |
| D3 | Does transfer require Operations Director approval? | Warehouse Manager approves / Escalate |
| D4 | Is transfer urgent (stockout at destination)? | Expedite / Standard transfer queue |

**Alternative Paths**

- **Path A — Approved:** Proceeds to WF-25 Transfer Execution
- **Path B — Rejected:** Requester notified; replenishment or backorder path followed
- **Path C — Modified quantity:** Partial transfer approved based on source availability
- **Path D — Emergency transfer:** Expedited approval and execution for priority stockout

**End Condition**

Transfer request is approved or rejected with documented rationale; approved transfers are authorized for execution.

**Business Outcome**

Stock is repositioned across the network to address local shortages without waiting for supplier lead times.

---

### WF-25: Inter-Location Transfer Execution

| Attribute | Description |
|-----------|-------------|
| **Workflow Name** | Inter-Location Transfer Execution |
| **Start Event** | A transfer request is approved and ready for physical movement |

**Sequential Business Steps**

1. Source Warehouse Manager assigns pick and pack of transfer items
2. Warehouse staff picks the approved quantity from source location storage
3. Items are packed for inter-location transport with transfer documentation
4. Shipment is arranged with internal logistics or carrier partner
5. Source location inventory is reduced upon dispatch
6. Destination Warehouse Manager is notified of incoming transfer with ETA
7. Destination Receiving Clerk accepts and verifies the transfer shipment upon arrival
8. Destination location inventory is increased upon verified receipt
9. Transfer is closed with both locations' balances updated

**Decision Points**

| # | Decision | Options |
|---|----------|---------|
| D1 | Can source location fulfill the full approved quantity? | Ship full / Ship partial — notify destination |
| D2 | Is transport arranged? | Internal transfer / External carrier |
| D3 | Does destination receipt match dispatched quantity? | Match / Variance — investigate |
| D4 | Are items in acceptable condition at receipt? | Accept / Reject damaged — initiate adjustment |

**Alternative Paths**

- **Path A — Clean transfer:** Full quantity shipped, received, and recorded at both locations
- **Path B — Partial dispatch:** Source ships available quantity; remainder cancelled or re-requested
- **Path C — Receipt variance:** Investigation at destination; adjustment per WF-14 if needed
- **Path D — Damage in transit:** Damaged items written off; acceptable items received

**End Condition**

Stock is physically moved, both location balances are updated, and transfer documentation is complete.

**Business Outcome**

Network inventory is redistributed accurately with full traceability of the movement.

---

### WF-26: Network Stock Rebalancing

| Attribute | Description |
|-----------|-------------|
| **Workflow Name** | Network Stock Rebalancing |
| **Start Event** | Weekly or monthly network review identifies persistent imbalance, seasonal redistribution is needed, or a new location requires initial stocking |

**Sequential Business Steps**

1. Operations Director initiates network-wide stock distribution review
2. Inventory Controller compiles stock levels, demand patterns, and overstock/stockout reports by location
3. Analyst identifies SKUs with excess at one location and shortage at another
4. Operations team develops rebalancing recommendations with transfer quantities and priorities
5. Regional Managers and Warehouse Managers validate recommendations against local knowledge
6. Purchasing confirms no inbound PO will resolve imbalance before transfer cost is incurred
7. COO approves the rebalancing plan for significant network moves
8. Approved transfers are initiated per WF-24 and executed per WF-25
9. Results are measured in subsequent review cycle

**Decision Points**

| # | Decision | Options |
|---|----------|---------|
| D1 | Is imbalance significant enough to warrant transfer cost? | Rebalance / Monitor — inbound PO will resolve |
| D2 | Which locations are source and destination? | Per recommendation / Adjust based on local input |
| D3 | Does plan require executive approval? | Operations Director approves / COO approves |
| D4 | Should purchasing be adjusted to prevent future imbalance? | Update replenishment by location / Transfer only |

**Alternative Paths**

- **Path A — Transfer-based rebalancing:** Multiple WF-24/WF-25 transfers executed
- **Path B — Inbound PO resolves imbalance:** Purchasing adjusts destination allocation; no transfer
- **Path C — New location stocking:** Initial stock deployment from central warehouse
- **Path D — Seasonal pre-positioning:** Proactive transfers ahead of demand shift

**End Condition**

Rebalancing plan is executed or deferred with documented rationale; network distribution is improved.

**Business Outcome**

Inventory investment is optimized across the network, reducing simultaneous stockouts and overstock at different locations.

---

## Domain 7: Returns

---

### WF-27: Customer Return Intake

| Attribute | Description |
|-----------|-------------|
| **Workflow Name** | Customer Return Intake |
| **Start Event** | A customer initiates a return request due to defect, wrong item, change of mind, or warranty claim |

**Sequential Business Steps**

1. Customer contacts Customer Service or Sales with a return request
2. Agent verifies the original order reference and purchase details
3. Agent confirms the return reason and assesses eligibility per return policy
4. Agent documents the return: product, quantity, reason, and customer resolution expectation (refund, replacement, credit)
5. Agent issues return authorization and return shipping instructions to the customer
6. Agent notifies Warehouse Manager of expected return shipment
7. For refund resolutions, Finance is notified to prepare refund processing upon receipt
8. For replacement orders, WF-16 availability confirmation is initiated

**Decision Points**

| # | Decision | Options |
|---|----------|---------|
| D1 | Is the return eligible per policy? | Authorize / Deny with explanation |
| D2 | What resolution does the customer expect? | Refund / Replacement / Store credit |
| D3 | Should customer ship return or drop off at store? | Ship to warehouse / Store return |
| D4 | Is replacement product available? | Initiate replacement order / Backorder replacement |

**Alternative Paths**

- **Path A — Eligible return, refund:** Authorization issued; Finance notified
- **Path B — Eligible return, replacement:** Return authorized; replacement order placed
- **Path C — Ineligible return:** Customer informed of policy; return denied
- **Path D — Store drop-off:** Regional Manager or store receives return; forwards to warehouse

**End Condition**

Return is authorized, documented, and routed for physical receipt and resolution processing.

**Business Outcome**

Customer returns are tracked from initiation with clear resolution path and inventory impact captured.

---

### WF-28: Return-to-Stock or Disposal Decision

| Attribute | Description |
|-----------|-------------|
| **Workflow Name** | Return-to-Stock or Disposal Decision |
| **Start Event** | Returned goods are physically received at the warehouse and matched to a return authorization |

**Sequential Business Steps**

1. Receiving Clerk accepts the return shipment and matches it to the return authorization
2. Receiving Clerk inspects returned product condition and verifies quantity
3. Warehouse Manager assesses whether returned product meets resale quality standards
4. Warehouse Manager determines disposition: restock, rework, or write-off/disposal
5. For resalable items, stock is added back to inventory at the appropriate location
6. For non-resalable items, write-off is initiated per WF-14 with return reason documented
7. Finance processes refund or credit per the resolution agreed in WF-27
8. Customer Service confirms return completion to the customer

**Decision Points**

| # | Decision | Options |
|---|----------|---------|
| D1 | Does returned product match the authorization? | Match / Mismatch — contact customer |
| D2 | Is product condition acceptable for resale? | Restock / Rework / Write off |
| D3 | Does product require quarantine or quality hold? | Hold for inspection / Immediate disposition |
| D4 | Is refund or credit ready to process? | Process refund / Pending inspection |

**Alternative Paths**

- **Path A — Resalable return:** Restocked; refund or credit processed
- **Path B — Damaged or unsellable:** Written off; refund still processed per policy
- **Path C — Wrong item returned:** Customer contacted; item held or returned to customer
- **Path D — Partial return:** Proportional resolution applied

**End Condition**

Returned goods are dispositioned, inventory is updated, financial resolution is processed, and customer is notified.

**Business Outcome**

Return inventory is accurately reflected; resalable stock is recovered and unsellable goods are properly removed.

---

## Domain 8: Performance Management & Commercial Alignment

---

### WF-29: Inventory Performance Reporting

| Attribute | Description |
|-----------|-------------|
| **Workflow Name** | Inventory Performance Reporting |
| **Start Event** | A scheduled reporting cycle begins (daily, weekly, or monthly), management requests a report, or a KPI threshold is breached |

**Sequential Business Steps**

1. Inventory Controller or Operations compiles inventory data for the reporting period
2. Analyst calculates key metrics: stock levels, stockouts, overstock, accuracy, fill rate, movement volumes
3. Analyst prepares reports tailored to audience: operational (daily), management (weekly), executive (monthly)
4. Reports are reviewed for accuracy and completeness by Inventory Controller
5. Reports are distributed to stakeholders: operations, purchasing, sales, finance, and leadership
6. Management reviews reports in scheduled meetings (daily standup, weekly ops review, monthly steering)
7. Identified issues are assigned corrective actions or escalated to relevant processes
8. Trend comparisons to prior periods and targets are documented

**Decision Points**

| # | Decision | Options |
|---|----------|---------|
| D1 | Does any KPI breach defined threshold? | Escalate / Monitor |
| D2 | Which report format for the audience? | Operational detail / Management summary / Executive dashboard |
| D3 | Are data anomalies investigated before distribution? | Investigate / Distribute with caveat |
| D4 | Should corrective action be initiated? | Assign action / Continue monitoring |

**Alternative Paths**

- **Path A — Routine reporting:** Standard reports distributed; no escalation
- **Path B — KPI breach:** Escalation to process owner; corrective action assigned
- **Path C — Ad-hoc management request:** Custom report prepared for specific inquiry
- **Path D — Data quality issue:** Report delayed until data corrected

**End Condition**

Reports are distributed, reviewed, and exceptions are assigned for action.

**Business Outcome**

Management has visibility into inventory health and can drive improvement with data-informed decisions.

---

### WF-30: Inventory Valuation & Financial Reconciliation

| Attribute | Description |
|-----------|-------------|
| **Workflow Name** | Inventory Valuation & Financial Reconciliation |
| **Start Event** | Month-end close cycle begins, quarterly financial reporting is due, or audit requests inventory substantiation |

**Sequential Business Steps**

1. Finance Manager initiates month-end inventory reconciliation
2. Finance extracts operational inventory quantities by product and location
3. Finance applies unit costs or valuation rates to calculate total inventory value
4. Finance compares operational inventory value to general ledger inventory balance
5. Finance identifies and investigates variances between operational and financial records
6. Finance works with Inventory Controller and Operations to explain variances
7. Unexplained variances trigger adjustment review or WF-14 write-off investigation
8. Finance prepares reconciliation report with variance explanations
9. CFO reviews reconciliation; approved figures support financial posting and reporting
10. Reconciliation evidence is archived for audit

**Decision Points**

| # | Decision | Options |
|---|----------|---------|
| D1 | Is variance within acceptable tolerance? | Accept / Investigate |
| D2 | Is variance due to timing (in-transit, unrecorded receipt)? | Explain and reconcile / Adjust |
| D3 | Does variance require operational correction? | Initiate WF-14 / Financial adjustment only |
| D4 | Is reconciliation approved for financial posting? | Approve / Hold for further review |

**Alternative Paths**

- **Path A — Clean reconciliation:** Variance within tolerance; financial posting proceeds
- **Path B — Timing variance:** Explained by in-transit or cutoff differences; no operational change
- **Path C — Operational variance:** WF-14 adjustments required before reconciliation closes
- **Path D — Audit-driven reconciliation:** External Auditor reviews evidence package

**End Condition**

Operational and financial inventory records are reconciled, variances are explained, and financial posting is supported.

**Business Outcome**

Balance sheet inventory value is accurate and auditable; finance and operations share a reconciled view of inventory.

---

### WF-31: Promotional & Launch Stock Readiness

| Attribute | Description |
|-----------|-------------|
| **Workflow Name** | Promotional & Launch Stock Readiness |
| **Start Event** | Marketing schedules a campaign or promotion, a new product launch date is set, or seasonal peak planning begins |

**Sequential Business Steps**

1. Marketing communicates campaign calendar, promoted SKUs, and expected demand uplift to operations and purchasing
2. Sales provides historical and forecast demand for promoted products
3. Inventory Controller assesses current stock and inbound supply against campaign requirements
4. Purchasing calculates stock gap and prepares pre-build purchase orders if needed
5. Operations confirms warehouse capacity to receive and store pre-built inventory
6. Warehouse Manager plans staffing and space for expected fulfillment surge
7. Cross-functional readiness review held with marketing, sales, purchasing, and operations
8. Team issues go/no-go recommendation based on stock readiness vs. campaign start date
9. If gap remains, marketing adjusts campaign scope or purchasing expedites supply

**Decision Points**

| # | Decision | Options |
|---|----------|---------|
| D1 | Is current plus inbound stock sufficient for campaign? | Ready / Gap identified |
| D2 | Can purchasing close the gap before campaign start? | Pre-build PO / Campaign delay |
| D3 | Does operations have fulfillment capacity for expected surge? | Ready / Add capacity or limit promotion |
| D4 | Go or no-go for campaign launch? | Go / Delay / Reduce campaign scope |

**Alternative Paths**

- **Path A — Fully ready:** Campaign proceeds on schedule
- **Path B — Stock gap, recoverable:** Expedited purchasing per WF-05; campaign proceeds with risk note
- **Path C — Stock gap, not recoverable:** Campaign delayed or scope reduced
- **Path D — New product launch:** Coordinated with WF-01 product setup and initial stocking

**End Condition**

Stock readiness is confirmed or gap is documented with agreed mitigation before campaign launch.

**Business Outcome**

Promotions and launches proceed with adequate stock, protecting brand reputation and campaign ROI.

---

## Domain 9: Governance & Compliance

---

### WF-32: Inventory Audit & Control Review

| Attribute | Description |
|-----------|-------------|
| **Workflow Name** | Inventory Audit & Control Review |
| **Start Event** | Quarterly internal audit schedule, annual external audit, significant control incident, or regulatory inspection |

**Sequential Business Steps**

1. Internal Auditor defines audit scope, period, and sample selection criteria
2. Auditor reviews company inventory policies and segregation of duties design
3. Auditor samples inventory transactions: receipts, adjustments, transfers, write-offs, and count approvals
4. Auditor verifies that approvals match policy authority thresholds
5. Auditor tests count records against physical verification evidence
6. Auditor interviews process owners (Inventory Controller, Warehouse Managers, Finance)
7. Auditor documents findings: control strengths, weaknesses, and exceptions
8. Auditor prepares audit report with recommendations and risk ratings
9. Operations Director and COO review findings and assign corrective actions
10. For external audit, evidence package is prepared and provided to External Auditor
11. Corrective action completion is verified in follow-up review

**Decision Points**

| # | Decision | Options |
|---|----------|---------|
| D1 | Are controls operating effectively? | Effective / Deficiency identified |
| D2 | Is finding material or immaterial? | Material — escalate / Immaterial — monitor |
| D3 | Is corrective action required? | Immediate action / Process improvement / Policy update |
| D4 | Is external audit opinion at risk? | Escalate to CFO and COO / Standard remediation |

**Alternative Paths**

- **Path A — Clean audit:** Controls effective; no material findings
- **Path B — Minor findings:** Corrective actions assigned; follow-up in next cycle
- **Path C — Material control weakness:** Escalation to COO and CFO; accelerated remediation
- **Path D — External audit:** Internal evidence provided; External Auditor issues independent opinion

**End Condition**

Audit is completed, findings are documented, corrective actions are assigned, and follow-up is scheduled.

**Business Outcome**

Inventory controls are verified, weaknesses are remediated, and the organization is prepared for regulatory and financial audit scrutiny.

---

## Workflow Dependency Summary

| Upstream Workflow | Downstream Workflow | Relationship |
|-------------------|---------------------|--------------|
| WF-01, WF-04 | WF-03 | Product data and classification inform stock policies |
| WF-03 | WF-21 | Thresholds trigger low-stock alerts |
| WF-21 | WF-22 | Validated alerts drive replenishment planning |
| WF-22 | WF-05 | Approved requisitions become purchase orders |
| WF-05 | WF-06, WF-23 | POs trigger shipment planning and supply tracking |
| WF-06 | WF-07 | Planned shipments are received and verified |
| WF-07 | WF-08, WF-09 | Clean receipt goes to put-away; variances to discrepancy resolution |
| WF-07 | WF-10 | Receipts update inventory status |
| WF-10 | WF-16, WF-21 | Status monitoring drives availability checks and alerts |
| WF-16 | WF-17 | Confirmed availability leads to reservation |
| WF-17 | WF-18, WF-19 | Reservations fulfilled or partially fulfilled |
| WF-18 | WF-20 | Pick/ship exceptions handled separately |
| WF-11, WF-12 | WF-13 | Count variances investigated |
| WF-13 | WF-14 | Approved variances become adjustments |
| WF-14 | WF-15, WF-30 | Adjustments feed shrinkage analysis and financial reconciliation |
| WF-24 | WF-25 | Approved requests are executed |
| WF-26 | WF-24, WF-25 | Rebalancing generates transfer requests and executions |
| WF-27 | WF-28 | Return intake leads to disposition decision |
| WF-10, WF-14, WF-18 | WF-29 | Operational data feeds performance reporting |
| WF-31 | WF-05, WF-22 | Campaign readiness drives pre-build purchasing |

---

## Document Summary

This document describes the complete business workflow for all **32 inventory management processes**. Each workflow is expressed as a sequence of human and departmental activities with explicit decision points, alternative paths, end conditions, and business outcomes.

These workflows support process mapping workshops, training material development, exception handling design, and business requirements traceability — without reference to technical implementation.

---

*End of Business Workflow Descriptions Document*
