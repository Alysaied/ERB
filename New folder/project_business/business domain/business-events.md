# Business Events Catalog: Inventory Management System

**Document Owner:** Domain Expert  
**Purpose:** Identify every business event that occurs within inventory management operations and document its triggers, processes, actors, and outcomes  
**Scope:** Business events only — no software events, messaging systems, APIs, or technical triggers  
**Based On:** Business Process Analysis, Business Workflows, Business Actor Analysis, and Business Process Maps

---

## How to Read This Catalog

A **business event** is something that happens in the organization's inventory operations — a condition, decision, arrival, request, or scheduled milestone — that causes a business process to begin or continue. Events are what the business responds to, not how technology notifies systems.

**Timing classification:**

| Classification | Meaning |
|----------------|---------|
| **Scheduled** | Occurs on a calendar, cycle, or planned timetable |
| **Action-triggered** | Occurs because a person, department, customer, or external party takes an action or because a business condition is detected |

---

## Executive Summary

This catalog identifies **52 business events** across **10 event domains**. Each event is mapped to the business process it initiates (BP-01 through BP-32), the actors involved, expected business outcome, typical frequency, and timing classification.

| Domain | Events | Count |
|--------|--------|-------|
| Master Data & Governance | BE-01 to BE-07 | 7 |
| Inbound & Procurement | BE-08 to BE-16 | 9 |
| Inventory Control & Accuracy | BE-17 to BE-26 | 10 |
| Order Fulfillment | BE-27 to BE-35 | 9 |
| Replenishment | BE-36 to BE-40 | 5 |
| Network Balance & Transfers | BE-41 to BE-46 | 6 |
| Returns | BE-47 to BE-49 | 3 |
| Performance & Reporting | BE-50 to BE-52 | 3 |
| Financial & Commercial | BE-53 to BE-56 | 4 |
| Governance & Audit | BE-57 to BE-59 | 3 |
| **Total** | | **52** |

---

## Event Index

| ID | Event Name | Process | Timing |
|----|--------------|---------|--------|
| BE-01 | Product Data Change Requested | BP-01 | Action-triggered |
| BE-02 | New Product Introduction Requested | BP-01 | Action-triggered |
| BE-03 | Product Discontinuation Requested | BP-01 | Action-triggered |
| BE-04 | Inventory Location Change Approved | BP-02 | Action-triggered |
| BE-05 | Stock Policy Review Due | BP-03 | Scheduled |
| BE-06 | Demand or Supply Condition Changed | BP-03 | Action-triggered |
| BE-07 | ABC Classification Review Due | BP-04 | Scheduled |
| BE-08 | Replenishment Need Identified | BP-05, BP-22 | Action-triggered |
| BE-09 | Purchase Requisition Approved | BP-05 | Action-triggered |
| BE-10 | Emergency Stockout Declared | BP-05, BP-21 | Action-triggered |
| BE-11 | Promotional Stock Build Authorized | BP-05, BP-31 | Action-triggered |
| BE-12 | Supplier Shipment Confirmed | BP-06, BP-23 | Action-triggered |
| BE-13 | Inbound Delivery Date Approaching | BP-06 | Scheduled |
| BE-14 | Supplier Shipment Arrived | BP-07 | Action-triggered |
| BE-15 | Receipt Discrepancy Identified | BP-08 | Action-triggered |
| BE-16 | Goods Receipt Completed | BP-09 | Action-triggered |
| BE-17 | Business Day Inventory Review Due | BP-10 | Scheduled |
| BE-18 | Inventory Movement Recorded | BP-10 | Action-triggered |
| BE-19 | Stock Threshold Breached | BP-10, BP-21 | Action-triggered |
| BE-20 | Cycle Count Assignment Due | BP-11 | Scheduled |
| BE-21 | SKU Flagged for Verification Count | BP-11 | Action-triggered |
| BE-22 | Full Physical Count Scheduled | BP-12 | Scheduled |
| BE-23 | Audit Requires Inventory Substantiation | BP-12 | Action-triggered |
| BE-24 | Count Variance Identified | BP-13 | Action-triggered |
| BE-25 | Stock Correction Required | BP-14 | Action-triggered |
| BE-26 | Monthly Shrinkage Review Due | BP-15 | Scheduled |
| BE-27 | Significant Loss or Adjustment Event | BP-15 | Action-triggered |
| BE-28 | Customer Order or Quote Received | BP-16 | Action-triggered |
| BE-29 | Large or Strategic Order Submitted | BP-16 | Action-triggered |
| BE-30 | Order Confirmed for Fulfillment | BP-17 | Action-triggered |
| BE-31 | Backordered Stock Became Available | BP-17 | Action-triggered |
| BE-32 | Order Released to Fulfillment Queue | BP-18 | Action-triggered / Scheduled |
| BE-33 | Pick Exception Reported | BP-20 | Action-triggered |
| BE-34 | Insufficient Stock at Fulfillment | BP-19 | Action-triggered |
| BE-35 | Customer Order Cancelled | BP-20 | Action-triggered |
| BE-36 | Low-Stock Alert Issued | BP-21 | Action-triggered |
| BE-37 | Scheduled Replenishment Cycle Due | BP-22 | Scheduled |
| BE-38 | Purchase Requisition Prepared | BP-22 | Action-triggered |
| BE-39 | Supplier Delivery Delay Reported | BP-23 | Action-triggered |
| BE-40 | Inbound Stock Inquiry Received | BP-23 | Action-triggered |
| BE-41 | Inter-Location Transfer Requested | BP-24 | Action-triggered |
| BE-42 | Network Imbalance Identified | BP-24, BP-26 | Action-triggered |
| BE-43 | Transfer Request Approved | BP-25 | Action-triggered |
| BE-44 | Network Rebalancing Review Due | BP-26 | Scheduled |
| BE-45 | Transfer Shipment Dispatched | BP-25 | Action-triggered |
| BE-46 | Transfer Shipment Received | BP-25 | Action-triggered |
| BE-47 | Customer Return Requested | BP-27 | Action-triggered |
| BE-48 | Returned Goods Received at Warehouse | BP-28 | Action-triggered |
| BE-49 | Return Inspection Completed | BP-28 | Action-triggered |
| BE-50 | Inventory Reporting Cycle Due | BP-29 | Scheduled |
| BE-51 | KPI Threshold Breached | BP-29 | Action-triggered |
| BE-52 | Management Requests Inventory Report | BP-29 | Action-triggered |
| BE-53 | Month-End Financial Close Initiated | BP-30 | Scheduled |
| BE-54 | Significant Write-Off Recorded | BP-30 | Action-triggered |
| BE-55 | Marketing Campaign Scheduled | BP-31 | Scheduled |
| BE-56 | New Product Launch Date Set | BP-31 | Action-triggered |
| BE-57 | Internal Audit Cycle Due | BP-32 | Scheduled |
| BE-58 | External Audit Initiated | BP-32 | Action-triggered |
| BE-59 | Control Incident or Policy Breach Identified | BP-32 | Action-triggered |

---

## Domain 1: Master Data & Governance Events

---

### BE-01: Product Data Change Requested

| Attribute | Description |
|-----------|-------------|
| **Event Name** | Product Data Change Requested |
| **Trigger** | A business stakeholder identifies an error, omission, or required update in an existing product record (name, category, unit of measure, or attribute) |
| **Business Process Initiated** | BP-01: Product Master Data Management |
| **Actors Involved** | Inventory Controller, Purchasing Manager, Operations Director, Requesting stakeholder (Sales, Purchasing, or Operations) |
| **Business Outcome** | Product record corrected and communicated; all locations reference updated product definition |
| **Frequency** | Weekly — ongoing as corrections arise |
| **Scheduled or Action-Triggered** | Action-triggered |

---

### BE-02: New Product Introduction Requested

| Attribute | Description |
|-----------|-------------|
| **Event Name** | New Product Introduction Requested |
| **Trigger** | Purchasing, sales, or marketing identifies a new product to add to the sellable assortment |
| **Business Process Initiated** | BP-01: Product Master Data Management; may also initiate BP-03 (Stock Policy) and BP-31 (Launch Readiness) |
| **Actors Involved** | Inventory Controller, Purchasing Manager, Sales Manager, Marketing Manager, Finance Manager |
| **Business Outcome** | New SKU created, approved, and activated; product available for ordering, receiving, and fulfillment |
| **Frequency** | Weekly to monthly — varies with assortment expansion |
| **Scheduled or Action-Triggered** | Action-triggered |

---

### BE-03: Product Discontinuation Requested

| Attribute | Description |
|-----------|-------------|
| **Event Name** | Product Discontinuation Requested |
| **Trigger** | Purchasing or sales determines a product is no longer sold, supplied, or strategically relevant |
| **Business Process Initiated** | BP-01: Product Master Data Management |
| **Actors Involved** | Inventory Controller, Purchasing Manager, Sales Manager, Operations Director |
| **Business Outcome** | Product status set to discontinued; remaining stock flagged for clearance or write-off planning |
| **Frequency** | Monthly — as assortment is rationalized |
| **Scheduled or Action-Triggered** | Action-triggered |

---

### BE-04: Inventory Location Change Approved

| Attribute | Description |
|-----------|-------------|
| **Event Name** | Inventory Location Change Approved |
| **Trigger** | Leadership approves opening, closing, consolidating, or reorganizing a warehouse, store, or distribution point |
| **Business Process Initiated** | BP-02: Location & Warehouse Setup |
| **Actors Involved** | COO, Operations Director, Warehouse Manager, Regional Manager, Finance Manager |
| **Business Outcome** | Location authorized or decommissioned; accountability assigned; network hierarchy updated |
| **Frequency** | Quarterly or as needed — infrequent in stable networks |
| **Scheduled or Action-Triggered** | Action-triggered |

---

### BE-05: Stock Policy Review Due

| Attribute | Description |
|-----------|-------------|
| **Event Name** | Stock Policy Review Due |
| **Trigger** | Calendar date for monthly priority SKU review or quarterly comprehensive threshold review arrives |
| **Business Process Initiated** | BP-03: Stock Policy & Threshold Definition |
| **Actors Involved** | Inventory Controller, Purchasing Manager, Operations Director, Sales Manager, Finance Manager |
| **Business Outcome** | Reorder levels and minimum thresholds updated and published for reviewed products |
| **Frequency** | Monthly (priority products) / Quarterly (full review) |
| **Scheduled or Action-Triggered** | Scheduled |

---

### BE-06: Demand or Supply Condition Changed

| Attribute | Description |
|-----------|-------------|
| **Event Name** | Demand or Supply Condition Changed |
| **Trigger** | Significant shift in sales velocity, supplier lead time change, seasonal demand forecast update, or chronic stockout/overstock identified |
| **Business Process Initiated** | BP-03: Stock Policy & Threshold Definition |
| **Actors Involved** | Inventory Controller, Purchasing Manager, Sales Manager, Operations Director |
| **Business Outcome** | Stock policy parameters revised to reflect new demand or supply reality |
| **Frequency** | As needed — several times per month for volatile SKUs |
| **Scheduled or Action-Triggered** | Action-triggered |

---

### BE-07: ABC Classification Review Due

| Attribute | Description |
|-----------|-------------|
| **Event Name** | ABC Classification Review Due |
| **Trigger** | Semi-annual classification calendar date arrives or major assortment change prompts ad-hoc review |
| **Business Process Initiated** | BP-04: ABC Product Classification |
| **Actors Involved** | Inventory Controller, Operations Director, Purchasing Manager, Sales Manager, Finance Manager |
| **Business Outcome** | ABC classification updated; count schedules and alert priorities realigned |
| **Frequency** | Semi-annual — ad-hoc for major assortment changes |
| **Scheduled or Action-Triggered** | Scheduled |

---

## Domain 2: Inbound & Procurement Events

---

### BE-08: Replenishment Need Identified

| Attribute | Description |
|-----------|-------------|
| **Event Name** | Replenishment Need Identified |
| **Trigger** | Validated low-stock condition, consumption trend, or inventory review identifies need to procure additional stock |
| **Business Process Initiated** | BP-22: Replenishment Planning & Requisition → BP-05: Purchase Order Placement |
| **Actors Involved** | Buyer, Purchasing Manager, Inventory Controller |
| **Business Outcome** | Purchase requisition prepared and progressed toward supplier order |
| **Frequency** | Daily to weekly |
| **Scheduled or Action-Triggered** | Action-triggered |

---

### BE-09: Purchase Requisition Approved

| Attribute | Description |
|-----------|-------------|
| **Event Name** | Purchase Requisition Approved |
| **Trigger** | Purchasing Manager or Finance approves a prepared purchase requisition within authority limits |
| **Business Process Initiated** | BP-05: Purchase Order Placement |
| **Actors Involved** | Buyer, Purchasing Manager, Warehouse Manager, Supplier |
| **Business Outcome** | Purchase order issued to supplier; inbound stock commitment recorded |
| **Frequency** | Daily to weekly |
| **Scheduled or Action-Triggered** | Action-triggered |

---

### BE-10: Emergency Stockout Declared

| Attribute | Description |
|-----------|-------------|
| **Event Name** | Emergency Stockout Declared |
| **Trigger** | Priority SKU reaches zero available stock with active customer demand or open orders |
| **Business Process Initiated** | BP-21: Low-Stock Alert Review → BP-05: Purchase Order Placement (expedited) or BP-24: Transfer Request |
| **Actors Involved** | Purchasing Manager, Buyer, Operations Director, Sales Manager, Warehouse Manager |
| **Business Outcome** | Expedited replenishment or emergency transfer initiated to restore availability |
| **Frequency** | Weekly — more frequent during peak seasons |
| **Scheduled or Action-Triggered** | Action-triggered |

---

### BE-11: Promotional Stock Build Authorized

| Attribute | Description |
|-----------|-------------|
| **Event Name** | Promotional Stock Build Authorized |
| **Trigger** | Marketing campaign or product launch plan approved with identified stock gap requiring pre-build purchasing |
| **Business Process Initiated** | BP-31: Promotional & Launch Stock Readiness → BP-05: Purchase Order Placement |
| **Actors Involved** | Marketing Manager, Purchasing Manager, Buyer, Operations Director, Inventory Controller |
| **Business Outcome** | Pre-build purchase orders placed; stock positioned before campaign launch |
| **Frequency** | Per campaign — monthly to quarterly |
| **Scheduled or Action-Triggered** | Action-triggered |

---

### BE-12: Supplier Shipment Confirmed

| Attribute | Description |
|-----------|-------------|
| **Event Name** | Supplier Shipment Confirmed |
| **Trigger** | Supplier acknowledges purchase order and confirms shipment date, or sends advance shipment notice |
| **Business Process Initiated** | BP-06: Inbound Shipment Planning; BP-23: Inbound Supply Tracking |
| **Actors Involved** | Buyer, Supplier, Warehouse Manager, Freight Forwarder |
| **Business Outcome** | Expected delivery documented; receiving location prepared; stakeholders informed of inbound stock |
| **Frequency** | Daily |
| **Scheduled or Action-Triggered** | Action-triggered |

---

### BE-13: Inbound Delivery Date Approaching

| Attribute | Description |
|-----------|-------------|
| **Event Name** | Inbound Delivery Date Approaching |
| **Trigger** | Expected delivery date falls within the planning window (e.g., next 2–3 business days) per purchasing schedule |
| **Business Process Initiated** | BP-06: Inbound Shipment Planning |
| **Actors Involved** | Buyer, Warehouse Manager, Receiving Clerk |
| **Business Outcome** | Receiving resources and dock capacity scheduled for imminent arrival |
| **Frequency** | Daily |
| **Scheduled or Action-Triggered** | Scheduled |

---

### BE-14: Supplier Shipment Arrived

| Attribute | Description |
|-----------|-------------|
| **Event Name** | Supplier Shipment Arrived |
| **Trigger** | Physical delivery of supplier goods at warehouse or store receiving dock |
| **Business Process Initiated** | BP-07: Goods Receipt & Verification |
| **Actors Involved** | Receiving Clerk, Warehouse Manager, Supplier (via delivery documentation) |
| **Business Outcome** | Goods inspected, verified, and recorded; on-hand inventory increased for accepted quantities |
| **Frequency** | Daily at active receiving locations |
| **Scheduled or Action-Triggered** | Action-triggered |

---

### BE-15: Receipt Discrepancy Identified

| Attribute | Description |
|-----------|-------------|
| **Event Name** | Receipt Discrepancy Identified |
| **Trigger** | Receiving clerk finds quantity mismatch, damaged goods, or wrong items during shipment verification |
| **Business Process Initiated** | BP-08: Receipt Discrepancy Resolution |
| **Actors Involved** | Receiving Clerk, Warehouse Manager, Buyer, Supplier, Finance Manager |
| **Business Outcome** | Discrepancy resolved with supplier; inventory and payment records corrected |
| **Frequency** | Several times per week at active locations |
| **Scheduled or Action-Triggered** | Action-triggered |

---

### BE-16: Goods Receipt Completed

| Attribute | Description |
|-----------|-------------|
| **Event Name** | Goods Receipt Completed |
| **Trigger** | Receiving clerk completes verification and records accepted goods with no blocking discrepancy |
| **Business Process Initiated** | BP-09: Stock Put-Away & Storage |
| **Actors Involved** | Receiving Clerk, Warehouse Manager, Warehouse Staff |
| **Business Outcome** | Goods moved to storage location; stock locatable and available for fulfillment |
| **Frequency** | Daily |
| **Scheduled or Action-Triggered** | Action-triggered |

---

## Domain 3: Inventory Control & Accuracy Events

---

### BE-17: Business Day Inventory Review Due

| Attribute | Description |
|-----------|-------------|
| **Event Name** | Business Day Inventory Review Due |
| **Trigger** | Start of each business day per operations schedule |
| **Business Process Initiated** | BP-10: Inventory Status Monitoring |
| **Actors Involved** | Operations Director, Inventory Controller, Purchasing Manager, Sales Manager |
| **Business Outcome** | Current stock status reviewed; exceptions identified and routed |
| **Frequency** | Daily |
| **Scheduled or Action-Triggered** | Scheduled |

---

### BE-18: Inventory Movement Recorded

| Attribute | Description |
|-----------|-------------|
| **Event Name** | Inventory Movement Recorded |
| **Trigger** | Goods received, order shipped, transfer completed, or adjustment applied — any transaction that changes stock balance |
| **Business Process Initiated** | BP-10: Inventory Status Monitoring (re-evaluation of status and alerts) |
| **Actors Involved** | Warehouse Manager, Receiving Clerk, Warehouse Picker/Packer, Inventory Controller |
| **Business Outcome** | Stock status and available-to-promise recalculated; alerts triggered if thresholds breached |
| **Frequency** | Continuous — multiple times daily |
| **Scheduled or Action-Triggered** | Action-triggered |

---

### BE-19: Stock Threshold Breached

| Attribute | Description |
|-----------|-------------|
| **Event Name** | Stock Threshold Breached |
| **Trigger** | Available stock falls below reorder level, minimum threshold, or reaches zero |
| **Business Process Initiated** | BP-10: Inventory Status Monitoring → BP-21: Low-Stock Alert Review |
| **Actors Involved** | Inventory Controller, Buyer, Purchasing Manager, Operations Director |
| **Business Outcome** | Low-stock or out-of-stock condition flagged; replenishment or transfer action initiated |
| **Frequency** | Daily — varies by SKU velocity |
| **Scheduled or Action-Triggered** | Action-triggered |

---

### BE-20: Cycle Count Assignment Due

| Attribute | Description |
|-----------|-------------|
| **Event Name** | Cycle Count Assignment Due |
| **Trigger** | Cycle count calendar assigns specific products, categories, or locations for counting on the current date |
| **Business Process Initiated** | BP-11: Cycle Counting |
| **Actors Involved** | Inventory Controller, Warehouse Manager, Warehouse Staff |
| **Business Outcome** | Assigned products physically counted; variances identified for follow-up |
| **Frequency** | Daily to weekly — distributed across calendar |
| **Scheduled or Action-Triggered** | Scheduled |

---

### BE-21: SKU Flagged for Verification Count

| Attribute | Description |
|-----------|-------------|
| **Event Name** | SKU Flagged for Verification Count |
| **Trigger** | Recurring pick failures, chronic variance history, or post-incident accuracy concern identifies a specific SKU for unscheduled count |
| **Business Process Initiated** | BP-11: Cycle Counting |
| **Actors Involved** | Inventory Controller, Warehouse Manager, Warehouse Staff |
| **Business Outcome** | Targeted SKU verified; accuracy confirmed or variance escalated |
| **Frequency** | As needed — several times per week at active locations |
| **Scheduled or Action-Triggered** | Action-triggered |

---

### BE-22: Full Physical Count Scheduled

| Attribute | Description |
|-----------|-------------|
| **Event Name** | Full Physical Count Scheduled |
| **Trigger** | Annual or semi-annual count calendar date arrives for a location |
| **Business Process Initiated** | BP-12: Full Physical Inventory Count |
| **Actors Involved** | Inventory Controller, Warehouse Manager, Warehouse Staff, Finance Manager, Internal Auditor |
| **Business Outcome** | Complete location inventory verified; baseline established or corrected |
| **Frequency** | Annual or semi-annual per location |
| **Scheduled or Action-Triggered** | Scheduled |

---

### BE-23: Audit Requires Inventory Substantiation

| Attribute | Description |
|-----------|-------------|
| **Event Name** | Audit Requires Inventory Substantiation |
| **Trigger** | Internal or external auditor requests physical inventory verification to support financial statements |
| **Business Process Initiated** | BP-12: Full Physical Inventory Count |
| **Actors Involved** | Inventory Controller, Warehouse Manager, Finance Manager, External Auditor, Internal Auditor |
| **Business Outcome** | Audit-ready inventory substantiation completed with documented count evidence |
| **Frequency** | Annual (external) / Quarterly (internal sampling) |
| **Scheduled or Action-Triggered** | Action-triggered |

---

### BE-24: Count Variance Identified

| Attribute | Description |
|-----------|-------------|
| **Event Name** | Count Variance Identified |
| **Trigger** | Cycle count or full count finds physical quantity differs from recorded balance beyond defined tolerance |
| **Business Process Initiated** | BP-13: Count Variance Investigation & Approval |
| **Actors Involved** | Inventory Controller, Warehouse Manager, Operations Director |
| **Business Outcome** | Variance investigated, root cause documented, adjustment approved or rejected |
| **Frequency** | Daily to weekly — follows each count cycle |
| **Scheduled or Action-Triggered** | Action-triggered |

---

### BE-25: Stock Correction Required

| Attribute | Description |
|-----------|-------------|
| **Event Name** | Stock Correction Required |
| **Trigger** | Approved count variance, discovered damage, obsolescence, theft, loss, or confirmed data error requires inventory balance change |
| **Business Process Initiated** | BP-14: Stock Adjustment & Write-Off |
| **Actors Involved** | Warehouse Manager, Inventory Controller, Operations Director, Finance Manager |
| **Business Outcome** | Inventory balance corrected with documented reason, approval, and financial treatment |
| **Frequency** | Daily at active locations |
| **Scheduled or Action-Triggered** | Action-triggered |

---

### BE-26: Monthly Shrinkage Review Due

| Attribute | Description |
|-----------|-------------|
| **Event Name** | Monthly Shrinkage Review Due |
| **Trigger** | First business week of each month per inventory control calendar |
| **Business Process Initiated** | BP-15: Shrinkage & Loss Management |
| **Actors Involved** | Inventory Controller, Operations Director, Finance Manager, Internal Auditor, Warehouse Managers |
| **Business Outcome** | Shrinkage trends analyzed; corrective actions assigned; control weaknesses escalated |
| **Frequency** | Monthly |
| **Scheduled or Action-Triggered** | Scheduled |

---

### BE-27: Significant Loss or Adjustment Event

| Attribute | Description |
|-----------|-------------|
| **Event Name** | Significant Loss or Adjustment Event |
| **Trigger** | Single adjustment or loss event exceeds defined materiality threshold, or recurring variance pattern detected mid-cycle |
| **Business Process Initiated** | BP-15: Shrinkage & Loss Management (ad-hoc) |
| **Actors Involved** | Inventory Controller, Operations Director, Internal Auditor, Warehouse Manager |
| **Business Outcome** | Immediate investigation launched; interim corrective action before next scheduled review |
| **Frequency** | As needed — several times per month |
| **Scheduled or Action-Triggered** | Action-triggered |

---

## Domain 4: Order Fulfillment Events

---

### BE-28: Customer Order or Quote Received

| Attribute | Description |
|-----------|-------------|
| **Event Name** | Customer Order or Quote Received |
| **Trigger** | B2B or B2C customer submits order or requests quote through sales, customer service, or retail channel |
| **Business Process Initiated** | BP-16: Order Availability Confirmation |
| **Actors Involved** | Sales Representative, Customer Service Representative, Operations Director, Warehouse Manager |
| **Business Outcome** | Availability confirmed or shortfall identified; realistic delivery commitment made to customer |
| **Frequency** | Multiple times daily |
| **Scheduled or Action-Triggered** | Action-triggered |

---

### BE-29: Large or Strategic Order Submitted

| Attribute | Description |
|-----------|-------------|
| **Event Name** | Large or Strategic Order Submitted |
| **Trigger** | Order volume or value exceeds defined threshold requiring management review of fulfillment feasibility |
| **Business Process Initiated** | BP-16: Order Availability Confirmation (escalated) |
| **Actors Involved** | Sales Manager, Operations Director, Warehouse Manager, Purchasing Manager |
| **Business Outcome** | Management-confirmed fulfillment plan; network capacity and stock allocation agreed |
| **Frequency** | Weekly |
| **Scheduled or Action-Triggered** | Action-triggered |

---

### BE-30: Order Confirmed for Fulfillment

| Attribute | Description |
|-----------|-------------|
| **Event Name** | Order Confirmed for Fulfillment |
| **Trigger** | Customer accepts quote; sales releases order; or availability check completed with customer commitment |
| **Business Process Initiated** | BP-17: Inventory Reservation |
| **Actors Involved** | Warehouse Manager, Operations Director, Sales Representative, Customer Service Representative |
| **Business Outcome** | Stock reserved against order; available-to-promise reduced; order queued for picking |
| **Frequency** | Multiple times daily |
| **Scheduled or Action-Triggered** | Action-triggered |

---

### BE-31: Backordered Stock Became Available

| Attribute | Description |
|-----------|-------------|
| **Event Name** | Backordered Stock Became Available |
| **Trigger** | Inbound receipt, transfer arrival, or replenishment completes for a SKU with open backorder lines |
| **Business Process Initiated** | BP-17: Inventory Reservation (backorder release) → BP-18: Pick, Pack & Ship |
| **Actors Involved** | Warehouse Manager, Customer Service Representative, Buyer |
| **Business Outcome** | Backorder lines reserved and fulfilled; customers notified of shipment |
| **Frequency** | Daily |
| **Scheduled or Action-Triggered** | Action-triggered |

---

### BE-32: Order Released to Fulfillment Queue

| Attribute | Description |
|-----------|-------------|
| **Event Name** | Order Released to Fulfillment Queue |
| **Trigger** | Warehouse manager releases reserved orders, or daily pick wave schedule initiates batch picking |
| **Business Process Initiated** | BP-18: Pick, Pack & Ship |
| **Actors Involved** | Warehouse Manager, Warehouse Picker/Packer, Carrier Partner, Customer Service Representative |
| **Business Outcome** | Order picked, packed, shipped; inventory deducted; customer notified |
| **Frequency** | Daily — continuous or scheduled pick waves |
| **Scheduled or Action-Triggered** | Scheduled (pick waves) / Action-triggered (individual release) |

---

### BE-33: Pick Exception Reported

| Attribute | Description |
|-----------|-------------|
| **Event Name** | Pick Exception Reported |
| **Trigger** | Picker cannot locate stock, finds damaged item, or identifies quantity shortfall during pick |
| **Business Process Initiated** | BP-20: Outbound Exception Handling |
| **Actors Involved** | Warehouse Picker/Packer, Warehouse Manager, Customer Service Representative, Inventory Controller |
| **Business Outcome** | Exception resolved; order re-picked, substituted, partially shipped, or cancelled; inventory corrected if needed |
| **Frequency** | Daily at high-volume locations |
| **Scheduled or Action-Triggered** | Action-triggered |

---

### BE-34: Insufficient Stock at Fulfillment

| Attribute | Description |
|-----------|-------------|
| **Event Name** | Insufficient Stock at Fulfillment |
| **Trigger** | Reserved quantity cannot be fully picked; reservation shortfall discovered at pick time |
| **Business Process Initiated** | BP-19: Partial Fulfillment & Backorder Management |
| **Actors Involved** | Warehouse Manager, Customer Service Representative, Sales Representative, Purchasing Manager |
| **Business Outcome** | Partial shipment executed or backorder created with customer agreement; replenishment prioritized |
| **Frequency** | Daily to weekly — varies with accuracy and demand |
| **Scheduled or Action-Triggered** | Action-triggered |

---

### BE-35: Customer Order Cancelled

| Attribute | Description |
|-----------|-------------|
| **Event Name** | Customer Order Cancelled |
| **Trigger** | Customer requests cancellation; sales cancels unfulfilled order; or prolonged backorder results in cancellation |
| **Business Process Initiated** | BP-20: Outbound Exception Handling |
| **Actors Involved** | Customer Service Representative, Sales Representative, Warehouse Manager |
| **Business Outcome** | Reservation released; picked goods returned to stock if applicable; customer notified |
| **Frequency** | Daily |
| **Scheduled or Action-Triggered** | Action-triggered |

---

## Domain 5: Replenishment Events

---

### BE-36: Low-Stock Alert Issued

| Attribute | Description |
|-----------|-------------|
| **Event Name** | Low-Stock Alert Issued |
| **Trigger** | Stock monitoring detects quantity below reorder level or out-of-stock on priority SKU |
| **Business Process Initiated** | BP-21: Low-Stock Alert Review |
| **Actors Involved** | Buyer, Purchasing Manager, Inventory Controller, Operations Director |
| **Business Outcome** | Alert validated or dismissed; replenishment, transfer, or escalation action initiated |
| **Frequency** | Daily |
| **Scheduled or Action-Triggered** | Action-triggered |

---

### BE-37: Scheduled Replenishment Cycle Due

| Attribute | Description |
|-----------|-------------|
| **Event Name** | Scheduled Replenishment Cycle Due |
| **Trigger** | Weekly or daily replenishment planning calendar triggers routine order review for non-urgent SKUs |
| **Business Process Initiated** | BP-22: Replenishment Planning & Requisition |
| **Actors Involved** | Buyer, Purchasing Manager, Inventory Controller, Finance Manager |
| **Business Outcome** | Batch purchase requisitions prepared for routine replenishment |
| **Frequency** | Daily (urgent) / Weekly (routine) |
| **Scheduled or Action-Triggered** | Scheduled |

---

### BE-38: Purchase Requisition Prepared

| Attribute | Description |
|-----------|-------------|
| **Event Name** | Purchase Requisition Prepared |
| **Trigger** | Buyer completes requisition with product, quantity, supplier, and rationale following validated replenishment need |
| **Business Process Initiated** | BP-22: Replenishment Planning & Requisition (approval stage) → BP-05 upon approval |
| **Actors Involved** | Buyer, Purchasing Manager, Finance Manager |
| **Business Outcome** | Requisition submitted for approval; progressed to purchase order upon authorization |
| **Frequency** | Daily to weekly |
| **Scheduled or Action-Triggered** | Action-triggered |

---

### BE-39: Supplier Delivery Delay Reported

| Attribute | Description |
|-----------|-------------|
| **Event Name** | Supplier Delivery Delay Reported |
| **Trigger** | Supplier communicates revised delivery date past original expectation, or buyer identifies overdue open order |
| **Business Process Initiated** | BP-23: Inbound Supply Tracking |
| **Actors Involved** | Buyer, Purchasing Manager, Operations Director, Sales Manager, Customer Service Representative |
| **Business Outcome** | Revised ETA communicated; escalation or alternative supply explored for critical delays |
| **Frequency** | Several times per week |
| **Scheduled or Action-Triggered** | Action-triggered |

---

### BE-40: Inbound Stock Inquiry Received

| Attribute | Description |
|-----------|-------------|
| **Event Name** | Inbound Stock Inquiry Received |
| **Trigger** | Sales, customer service, or operations asks when expected inbound stock will arrive for a specific SKU |
| **Business Process Initiated** | BP-23: Inbound Supply Tracking |
| **Actors Involved** | Buyer, Purchasing Manager, Customer Service Representative, Sales Representative |
| **Business Outcome** | Current inbound status retrieved; customer or internal stakeholder informed of expected arrival |
| **Frequency** | Daily |
| **Scheduled or Action-Triggered** | Action-triggered |

---

## Domain 6: Network Balance & Transfer Events

---

### BE-41: Inter-Location Transfer Requested

| Attribute | Description |
|-----------|-------------|
| **Event Name** | Inter-Location Transfer Requested |
| **Trigger** | Store or regional manager, sales, or operations identifies need to move stock between locations |
| **Business Process Initiated** | BP-24: Inter-Location Transfer Request |
| **Actors Involved** | Regional Manager, Sales Manager, Operations Director, Warehouse Manager, Inventory Controller |
| **Business Outcome** | Transfer approved or rejected with documented rationale |
| **Frequency** | Several times per week in multi-location networks |
| **Scheduled or Action-Triggered** | Action-triggered |

---

### BE-42: Network Imbalance Identified

| Attribute | Description |
|-----------|-------------|
| **Event Name** | Network Imbalance Identified |
| **Trigger** | Stock monitoring or location review finds simultaneous overstock at one site and stockout at another for the same SKU |
| **Business Process Initiated** | BP-24: Inter-Location Transfer Request or BP-26: Network Stock Rebalancing |
| **Actors Involved** | Operations Director, Inventory Controller, Regional Manager, Purchasing Manager |
| **Business Outcome** | Transfer initiated or rebalancing plan developed to correct imbalance |
| **Frequency** | Weekly |
| **Scheduled or Action-Triggered** | Action-triggered |

---

### BE-43: Transfer Request Approved

| Attribute | Description |
|-----------|-------------|
| **Event Name** | Transfer Request Approved |
| **Trigger** | Operations Director or Warehouse Manager authorizes inter-location transfer |
| **Business Process Initiated** | BP-25: Inter-Location Transfer Execution |
| **Actors Involved** | Warehouse Manager (source and destination), Warehouse Staff, Carrier Partner, Inventory Controller |
| **Business Outcome** | Stock physically moved; both location balances updated |
| **Frequency** | Several times per week |
| **Scheduled or Action-Triggered** | Action-triggered |

---

### BE-44: Network Rebalancing Review Due

| Attribute | Description |
|-----------|-------------|
| **Event Name** | Network Rebalancing Review Due |
| **Trigger** | Weekly or monthly network review calendar date arrives |
| **Business Process Initiated** | BP-26: Network Stock Rebalancing |
| **Actors Involved** | Operations Director, Inventory Controller, Regional Managers, Purchasing Manager, COO |
| **Business Outcome** | Rebalancing recommendations developed and executed; network distribution optimized |
| **Frequency** | Weekly / Monthly |
| **Scheduled or Action-Triggered** | Scheduled |

---

### BE-45: Transfer Shipment Dispatched

| Attribute | Description |
|-----------|-------------|
| **Event Name** | Transfer Shipment Dispatched |
| **Trigger** | Source location picks, packs, and ships approved transfer quantity |
| **Business Process Initiated** | BP-25: Inter-Location Transfer Execution (in transit phase) |
| **Actors Involved** | Warehouse Manager (source), Warehouse Staff, Carrier Partner |
| **Business Outcome** | Source location inventory reduced; destination notified of incoming shipment |
| **Frequency** | Daily to weekly |
| **Scheduled or Action-Triggered** | Action-triggered |

---

### BE-46: Transfer Shipment Received

| Attribute | Description |
|-----------|-------------|
| **Event Name** | Transfer Shipment Received |
| **Trigger** | Destination location accepts and verifies incoming transfer shipment |
| **Business Process Initiated** | BP-25: Inter-Location Transfer Execution (completion phase) |
| **Actors Involved** | Receiving Clerk (destination), Warehouse Manager (destination), Inventory Controller |
| **Business Outcome** | Destination inventory increased; transfer closed; variance investigated if quantity mismatch |
| **Frequency** | Daily to weekly |
| **Scheduled or Action-Triggered** | Action-triggered |

---

## Domain 7: Returns Events

---

### BE-47: Customer Return Requested

| Attribute | Description |
|-----------|-------------|
| **Event Name** | Customer Return Requested |
| **Trigger** | Customer contacts sales or customer service to return product (defect, wrong item, change of mind, warranty) |
| **Business Process Initiated** | BP-27: Customer Return Intake |
| **Actors Involved** | Customer Service Representative, Sales Representative, Finance Manager, Warehouse Manager |
| **Business Outcome** | Return authorized, documented, and routed for physical receipt and resolution |
| **Frequency** | Daily |
| **Scheduled or Action-Triggered** | Action-triggered |

---

### BE-48: Returned Goods Received at Warehouse

| Attribute | Description |
|-----------|-------------|
| **Event Name** | Returned Goods Received at Warehouse |
| **Trigger** | Customer return shipment arrives at warehouse or store forwards returned goods |
| **Business Process Initiated** | BP-28: Return-to-Stock or Disposal Decision |
| **Actors Involved** | Receiving Clerk, Warehouse Manager, Inventory Controller, Customer Service Representative |
| **Business Outcome** | Return matched to authorization; inspection and disposition decision made |
| **Frequency** | Daily |
| **Scheduled or Action-Triggered** | Action-triggered |

---

### BE-49: Return Inspection Completed

| Attribute | Description |
|-----------|-------------|
| **Event Name** | Return Inspection Completed |
| **Trigger** | Warehouse manager or receiving clerk completes quality inspection of returned product |
| **Business Process Initiated** | BP-28: Return-to-Stock or Disposal Decision (disposition phase) |
| **Actors Involved** | Warehouse Manager, Inventory Controller, Finance Manager, Customer Service Representative |
| **Business Outcome** | Product restocked, reworked, or written off; refund processed; customer notified of completion |
| **Frequency** | Daily — follows return receipt |
| **Scheduled or Action-Triggered** | Action-triggered |

---

## Domain 8: Performance & Reporting Events

---

### BE-50: Inventory Reporting Cycle Due

| Attribute | Description |
|-----------|-------------|
| **Event Name** | Inventory Reporting Cycle Due |
| **Trigger** | Daily operational, weekly management, or monthly executive reporting calendar date arrives |
| **Business Process Initiated** | BP-29: Inventory Performance Reporting |
| **Actors Involved** | Inventory Controller, Operations Director, COO, CEO, CFO, Warehouse Managers |
| **Business Outcome** | Inventory health reports distributed; trends documented; exceptions assigned |
| **Frequency** | Daily / Weekly / Monthly |
| **Scheduled or Action-Triggered** | Scheduled |

---

### BE-51: KPI Threshold Breached

| Attribute | Description |
|-----------|-------------|
| **Event Name** | KPI Threshold Breached |
| **Trigger** | Inventory accuracy, fill rate, stockout frequency, or shrinkage rate exceeds defined tolerance during monitoring |
| **Business Process Initiated** | BP-29: Inventory Performance Reporting (escalation) |
| **Actors Involved** | Operations Director, Inventory Controller, COO, Warehouse Manager |
| **Business Outcome** | Corrective action assigned; escalation to leadership; targeted improvement initiative launched |
| **Frequency** | As needed — weekly during improvement periods |
| **Scheduled or Action-Triggered** | Action-triggered |

---

### BE-52: Management Requests Inventory Report

| Attribute | Description |
|-----------|-------------|
| **Event Name** | Management Requests Inventory Report |
| **Trigger** | Executive, steering committee, or department head requests ad-hoc inventory analysis or status report |
| **Business Process Initiated** | BP-29: Inventory Performance Reporting (ad-hoc) |
| **Actors Involved** | Inventory Controller, Operations Director, Requesting executive or manager |
| **Business Outcome** | Custom report prepared and delivered; management question answered with current data |
| **Frequency** | As needed — several times per month |
| **Scheduled or Action-Triggered** | Action-triggered |

---

## Domain 9: Financial & Commercial Events

---

### BE-53: Month-End Financial Close Initiated

| Attribute | Description |
|-----------|-------------|
| **Event Name** | Month-End Financial Close Initiated |
| **Trigger** | Finance calendar marks beginning of month-end close period |
| **Business Process Initiated** | BP-30: Inventory Valuation & Financial Reconciliation |
| **Actors Involved** | Finance Manager, Inventory Controller, Operations Director, CFO |
| **Business Outcome** | Operational and financial inventory records reconciled; variances explained; posting supported |
| **Frequency** | Monthly |
| **Scheduled or Action-Triggered** | Scheduled |

---

### BE-54: Significant Write-Off Recorded

| Attribute | Description |
|-----------|-------------|
| **Event Name** | Significant Write-Off Recorded |
| **Trigger** | Write-off exceeding defined financial materiality threshold is approved and recorded |
| **Business Process Initiated** | BP-30: Inventory Valuation & Financial Reconciliation (triggered review) |
| **Actors Involved** | Finance Manager, Inventory Controller, Operations Director, CFO |
| **Business Outcome** | Financial impact assessed; reconciliation updated; leadership informed if material |
| **Frequency** | As needed — several times per month |
| **Scheduled or Action-Triggered** | Action-triggered |

---

### BE-55: Marketing Campaign Scheduled

| Attribute | Description |
|-----------|-------------|
| **Event Name** | Marketing Campaign Scheduled |
| **Trigger** | Marketing publishes campaign calendar with promoted SKUs and launch date |
| **Business Process Initiated** | BP-31: Promotional & Launch Stock Readiness |
| **Actors Involved** | Marketing Manager, Sales Manager, Purchasing Manager, Operations Director, Inventory Controller |
| **Business Outcome** | Stock readiness assessed; pre-build ordered if needed; go/no-go decision before launch |
| **Frequency** | Per campaign — monthly to quarterly |
| **Scheduled or Action-Triggered** | Scheduled |

---

### BE-56: New Product Launch Date Set

| Attribute | Description |
|-----------|-------------|
| **Event Name** | New Product Launch Date Set |
| **Trigger** | Business sets official date for new product availability to customers |
| **Business Process Initiated** | BP-31: Promotional & Launch Stock Readiness; BP-01 (Product Master) |
| **Actors Involved** | Marketing Manager, Inventory Controller, Purchasing Manager, Warehouse Manager, Sales Manager |
| **Business Outcome** | Launch stock positioned; product master active; sales enabled on launch date |
| **Frequency** | Per launch — monthly to quarterly |
| **Scheduled or Action-Triggered** | Action-triggered |

---

## Domain 10: Governance & Audit Events

---

### BE-57: Internal Audit Cycle Due

| Attribute | Description |
|-----------|-------------|
| **Event Name** | Internal Audit Cycle Due |
| **Trigger** | Quarterly internal audit schedule for inventory controls arrives |
| **Business Process Initiated** | BP-32: Inventory Audit & Control Review |
| **Actors Involved** | Internal Auditor, Inventory Controller, Operations Director, Finance Manager, Warehouse Managers |
| **Business Outcome** | Controls tested; findings documented; corrective actions assigned |
| **Frequency** | Quarterly |
| **Scheduled or Action-Triggered** | Scheduled |

---

### BE-58: External Audit Initiated

| Attribute | Description |
|-----------|-------------|
| **Event Name** | External Audit Initiated |
| **Trigger** | External auditor begins annual financial statement audit requiring inventory evidence |
| **Business Process Initiated** | BP-32: Inventory Audit & Control Review |
| **Actors Involved** | External Auditor, Internal Auditor, Finance Manager, Inventory Controller, CFO |
| **Business Outcome** | Audit evidence package provided; control effectiveness evaluated; opinion supported |
| **Frequency** | Annual |
| **Scheduled or Action-Triggered** | Action-triggered |

---

### BE-59: Control Incident or Policy Breach Identified

| Attribute | Description |
|-----------|-------------|
| **Event Name** | Control Incident or Policy Breach Identified |
| **Trigger** | Unauthorized adjustment discovered, segregation of duties violation reported, or significant undocumented inventory change identified |
| **Business Process Initiated** | BP-32: Inventory Audit & Control Review (ad-hoc); may also trigger BP-15 (Shrinkage) |
| **Actors Involved** | Internal Auditor, Operations Director, COO, Inventory Controller, Finance Manager |
| **Business Outcome** | Incident investigated; control weakness remediated; disciplinary or process action taken |
| **Frequency** | As needed — hopefully rare |
| **Scheduled or Action-Triggered** | Action-triggered |

---

## Event-to-Process Mapping Summary

| Business Process | Events That Initiate It |
|------------------|-------------------------|
| **BP-01** Product Master Data Management | BE-01, BE-02, BE-03, BE-56 |
| **BP-02** Location & Warehouse Setup | BE-04 |
| **BP-03** Stock Policy & Threshold Definition | BE-05, BE-06 |
| **BP-04** ABC Product Classification | BE-07 |
| **BP-05** Purchase Order Placement | BE-08, BE-09, BE-10, BE-11 |
| **BP-06** Inbound Shipment Planning | BE-12, BE-13 |
| **BP-07** Goods Receipt & Verification | BE-14 |
| **BP-08** Receipt Discrepancy Resolution | BE-15 |
| **BP-09** Stock Put-Away & Storage | BE-16 |
| **BP-10** Inventory Status Monitoring | BE-17, BE-18, BE-19 |
| **BP-11** Cycle Counting | BE-20, BE-21 |
| **BP-12** Full Physical Inventory Count | BE-22, BE-23 |
| **BP-13** Count Variance Investigation | BE-24 |
| **BP-14** Stock Adjustment & Write-Off | BE-25 |
| **BP-15** Shrinkage & Loss Management | BE-26, BE-27 |
| **BP-16** Order Availability Confirmation | BE-28, BE-29 |
| **BP-17** Inventory Reservation | BE-30, BE-31 |
| **BP-18** Pick, Pack & Ship | BE-32, BE-31 |
| **BP-19** Partial Fulfillment & Backorder | BE-34 |
| **BP-20** Outbound Exception Handling | BE-33, BE-35 |
| **BP-21** Low-Stock Alert Review | BE-19, BE-36, BE-10 |
| **BP-22** Replenishment Planning | BE-08, BE-37, BE-38 |
| **BP-23** Inbound Supply Tracking | BE-12, BE-39, BE-40 |
| **BP-24** Transfer Request | BE-41, BE-42 |
| **BP-25** Transfer Execution | BE-43, BE-45, BE-46 |
| **BP-26** Network Stock Rebalancing | BE-44, BE-42 |
| **BP-27** Customer Return Intake | BE-47 |
| **BP-28** Return Disposition | BE-48, BE-49 |
| **BP-29** Performance Reporting | BE-50, BE-51, BE-52 |
| **BP-30** Financial Reconciliation | BE-53, BE-54 |
| **BP-31** Campaign Stock Readiness | BE-11, BE-55, BE-56 |
| **BP-32** Audit & Control Review | BE-57, BE-58, BE-59 |

---

## Event Timing Summary

| Classification | Count | Examples |
|----------------|-------|----------|
| **Scheduled** | 14 | BE-05, BE-07, BE-13, BE-17, BE-20, BE-22, BE-26, BE-37, BE-44, BE-50, BE-53, BE-55, BE-57 |
| **Action-triggered** | 36 | BE-14, BE-19, BE-28, BE-30, BE-33, BE-41, BE-47, etc. |
| **Both** | 2 | BE-32 (scheduled pick waves or manual release), BE-31 (receipt-triggered) |

---

## Event Chain Examples

Events frequently cascade — one business event completes and triggers the next:

### Inbound supply chain
```
BE-08 Replenishment Need → BE-38 Requisition Prepared → BE-09 Requisition Approved
 → BE-12 Supplier Confirmed → BE-13 Delivery Approaching → BE-14 Shipment Arrived
 → BE-16 Receipt Completed (or BE-15 Discrepancy)
```

### Order fulfillment chain
```
BE-28 Order Received → BE-30 Order Confirmed → BE-32 Released to Queue
 → BE-33 Pick Exception (if problem) OR shipment complete
```

### Accuracy control chain
```
BE-20 Cycle Count Due → BE-24 Variance Identified → BE-25 Correction Required
 → BE-18 Movement Recorded → BE-17 Next Day Review
```

### Stockout response chain
```
BE-19 Threshold Breached → BE-36 Low-Stock Alert → BE-08 Replenishment Need
 → BE-41 Transfer Requested (if faster than purchase)
```

---

## Document Summary

This catalog documents **52 business events** that occur across inventory management operations. Each event is a business occurrence — not a technical signal — that initiates one or more of the **32 defined business processes**. Events are classified as **scheduled** (14), **action-triggered** (36), or **both** (2).

This catalog supports process design workshops, standard operating procedure development, event-driven requirements traceability, and operational playbook creation — entirely from a business perspective.

---

*End of Business Events Catalog Document*
