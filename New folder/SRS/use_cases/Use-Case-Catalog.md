# Use Case Catalog
## Inventory Management System

---

## Document Information

| Attribute | Detail |
|-----------|--------|
| **Document ID** | SRS-UC-001 |
| **Document Title** | Use Case Catalog — Inventory Management System |
| **Version** | 1.0 |
| **Status** | Draft |
| **Document Owner** | Senior Business Analyst |
| **Source Documents** | BRD-IMS-001 (v1.0), SRS-BR-001 (Business Rule Catalog, v1.0) |
| **Date** | July 5, 2026 |
| **Scope** | Business interactions only — workflow steps are documented separately |

### Purpose

This catalog identifies every business use case for the Inventory Management System derived from the approved Business Requirements Document and Business Rule Catalog. Each use case describes a meaningful interaction between business actors and the system to achieve a defined business goal. Detailed workflows are out of scope for this document.

### Traceability Legend

| Reference | Meaning |
|-----------|---------|
| BP-xx | Business Process (BRD Section 10) |
| FR-xxx | Functional Requirement (BRD Section 14) |
| BR-xxx | Business Rule (SRS-BR-001 / BRD Section 13) |

---

## Use Case Index

| ID | Use Case Name | Primary Actor | Business Process | Phase |
|----|---------------|---------------|------------------|-------|
| UC-001 | Manage Product Master Data | Inventory Controller | BP-01 | MVP |
| UC-002 | Configure Inventory Locations | Inventory Controller | BP-02 | MVP |
| UC-003 | Define Stock Policies and Thresholds | Inventory Controller | BP-03 | MVP |
| UC-004 | Classify Products by ABC Priority | Inventory Controller | BP-04 | Phase 2 |
| UC-005 | Maintain Governance Policies and Reason Codes | Inventory Controller | BP-01, BP-03 | MVP / Phase 2 |
| UC-006 | Place and Manage Purchase Orders | Buyer | BP-05 | Phase 2 |
| UC-007 | Plan Expected Inbound Deliveries | Buyer | BP-06 | Phase 2 |
| UC-008 | Receive and Verify Supplier Goods | Receiving Clerk | BP-07 | MVP |
| UC-009 | Document and Resolve Receipt Discrepancies | Receiving Clerk | BP-08 | MVP |
| UC-010 | Perform Stock Put-Away | Warehouse Staff | BP-09 | MVP |
| UC-011 | Receive Return and Non-PO Inbound Stock | Receiving Clerk | BP-07, BP-27 | MVP |
| UC-012 | Monitor Inventory Status | Inventory Controller | BP-10 | MVP |
| UC-013 | Inquire Inventory Availability | Sales Representative | BP-10, BP-16 | MVP |
| UC-014 | Perform Cycle Count | Warehouse Staff | BP-11 | MVP |
| UC-015 | Conduct Full Physical Inventory Count | Inventory Controller | BP-12 | MVP |
| UC-016 | Investigate and Approve Count Variances | Warehouse Manager | BP-13 | MVP |
| UC-017 | Process Stock Adjustments | Warehouse Manager | BP-14 | MVP |
| UC-018 | Authorize and Process Inventory Write-Offs | Operations Director | BP-14, BP-15 | MVP |
| UC-019 | Manage Quarantine and Hold Stock | Warehouse Manager | BP-14, BP-20 | MVP |
| UC-020 | Analyze Shrinkage, Loss, and Obsolete Stock | Inventory Controller | BP-15 | Phase 2 |
| UC-021 | Confirm Order Availability | Sales Representative | BP-16 | MVP |
| UC-022 | Reserve Inventory for Confirmed Orders | Customer Service Representative | BP-17 | MVP |
| UC-023 | Release Inventory Reservations | Customer Service Representative | BP-17 | MVP |
| UC-024 | Pick, Pack, and Ship Orders | Warehouse Picker / Packer | BP-18 | MVP |
| UC-025 | Handle Partial Fulfillment and Backorders | Customer Service Representative | BP-19 | MVP / Phase 2 |
| UC-026 | Handle Outbound Fulfillment Exceptions | Warehouse Manager | BP-20 | MVP |
| UC-027 | View Order Fulfillment Status | Customer Service Representative | BP-18, BP-19 | MVP |
| UC-028 | Review Low-Stock and Out-of-Stock Alerts | Purchasing Manager | BP-21 | MVP |
| UC-029 | Plan Replenishment and Create Purchase Requisitions | Buyer | BP-22 | Phase 2 |
| UC-030 | Track Inbound Supply Status | Buyer | BP-23 | Phase 2 |
| UC-031 | Request Inter-Location Stock Transfer | Regional / Store Manager | BP-24 | MVP |
| UC-032 | Approve or Reject Transfer Requests | Operations Director | BP-24, BP-25 | MVP |
| UC-033 | Execute and Record Inter-Location Transfer | Warehouse Staff | BP-25 | MVP |
| UC-034 | Analyze and Recommend Network Rebalancing | Operations Director | BP-26 | Phase 2 |
| UC-035 | Authorize and Record Customer Returns | Customer Service Representative | BP-27 | MVP |
| UC-036 | Receive, Inspect, and Disposition Returned Goods | Receiving Clerk | BP-28 | MVP / Phase 2 |
| UC-037 | Review Inventory Dashboards and Operational Reports | Operations Director | BP-29 | MVP / Phase 2 |
| UC-038 | Review Inventory Performance KPIs | Chief Executive Officer | BP-29 | Phase 3 |
| UC-039 | Reconcile Inventory Valuation with Finance | Finance Manager | BP-30 | Phase 2 |
| UC-040 | Confirm Promotional and Launch Stock Readiness | Marketing Manager | BP-31 | Phase 2 |
| UC-041 | Conduct Inventory Audit and Control Review | Internal Auditor | BP-32 | MVP / Phase 2 |
| UC-042 | View Inventory Movement and Transaction History | Inventory Controller | BP-10, BP-29 | MVP |
| UC-043 | Query and Review Audit Trail | Internal Auditor | BP-32 | MVP |
| UC-044 | Manage User Accounts and Role Assignments | System Administrator | — | MVP |
| UC-045 | Enforce Role-Based and Location-Scoped Access | System Administrator | — | MVP |
| UC-046 | Import Initial Product and Stock Master Data | Inventory Controller | BP-01, BP-02 | MVP |
| UC-047 | Receive and Respond to Operational Notifications | Warehouse Manager | BP-21, BP-24 | MVP / Phase 2 |
| UC-048 | Support Multi-Location Split Fulfillment | Warehouse Manager | BP-18, BP-19 | Phase 2 |

**Total Use Cases:** 48

---

## Domain 1: Master Data & Governance

### UC-001 — Manage Product Master Data

| Attribute | Detail |
|-----------|--------|
| **Use Case ID** | UC-001 |
| **Use Case Name** | Manage Product Master Data |
| **Goal** | Establish and maintain accurate, unique product identity records so all inventory operations reference a single trusted SKU definition across the network. |
| **Primary Actor** | Inventory Controller |
| **Supporting Actors** | Operations Director, Warehouse Manager, Purchasing Manager, Sales Manager |
| **Trigger** | A new product is introduced, an existing product attribute requires correction, or duplicate product records are detected. |
| **Business Process** | BP-01 — Product Master Data Management |
| **Related Functional Requirements** | FR-001, FR-002, FR-003, FR-004 |
| **Related Business Rules** | BR-027 (No Reorder of Discontinued Products) |

---

### UC-002 — Configure Inventory Locations

| Attribute | Detail |
|-----------|--------|
| **Use Case ID** | UC-002 |
| **Use Case Name** | Configure Inventory Locations |
| **Goal** | Define and maintain the inventory location network so stock can be assigned, tracked, and reported by warehouse, store, or distribution point. |
| **Primary Actor** | Inventory Controller |
| **Supporting Actors** | Operations Director, Warehouse Manager, Regional / Store Manager, Finance Manager |
| **Trigger** | A new location is opened, location hierarchy changes, a location requires closure planning, or opening stock balances must be established at go-live. |
| **Business Process** | BP-02 — Location & Warehouse Setup |
| **Related Functional Requirements** | FR-005, FR-006, FR-007, FR-010 |
| **Related Business Rules** | — |

---

### UC-003 — Define Stock Policies and Thresholds

| Attribute | Detail |
|-----------|--------|
| **Use Case ID** | UC-003 |
| **Use Case Name** | Define Stock Policies and Thresholds |
| **Goal** | Set reorder levels, minimum thresholds, and safety stock policies so replenishment and availability monitoring reflect business service-level targets. |
| **Primary Actor** | Inventory Controller |
| **Supporting Actors** | Purchasing Manager, Operations Director, Warehouse Manager |
| **Trigger** | A new product is onboarded, demand or lead-time assumptions change, or replenishment performance indicates threshold recalibration is needed. |
| **Business Process** | BP-03 — Stock Policy & Threshold Definition |
| **Related Functional Requirements** | FR-008 |
| **Related Business Rules** | BR-009 (Reorder at Reorder Level), BR-010 (Safety Stock Protection) |

---

### UC-004 — Classify Products by ABC Priority

| Attribute | Detail |
|-----------|--------|
| **Use Case ID** | UC-004 |
| **Use Case Name** | Classify Products by ABC Priority |
| **Goal** | Segment products by business importance so operational effort, count frequency, and monitoring intensity focus on high-impact SKUs. |
| **Primary Actor** | Inventory Controller |
| **Supporting Actors** | Operations Director, Purchasing Manager, Sales Manager, Finance Manager |
| **Trigger** | Periodic classification review cycle, significant shift in product velocity or revenue contribution, or new product portfolio expansion. |
| **Business Process** | BP-04 — ABC Product Classification |
| **Related Functional Requirements** | FR-009 |
| **Related Business Rules** | BR-032 (Class A Priority Monitoring) |

---

### UC-005 — Maintain Governance Policies and Reason Codes

| Attribute | Detail |
|-----------|--------|
| **Use Case ID** | UC-005 |
| **Use Case Name** | Maintain Governance Policies and Reason Codes |
| **Goal** | Define standardized reason codes and inventory governance policies that govern adjustments, exceptions, and accountability across all locations. |
| **Primary Actor** | Inventory Controller |
| **Supporting Actors** | Operations Director, Internal Auditor, Finance Manager |
| **Trigger** | New exception categories emerge, audit findings require policy updates, or reason code taxonomy needs expansion or consolidation. |
| **Business Process** | BP-01 — Product Master Data Management; BP-03 — Stock Policy & Threshold Definition |
| **Related Functional Requirements** | FR-011, FR-012 |
| **Related Business Rules** | BR-020 (Mandatory Adjustment Reason Codes) |

---

## Domain 2: Inbound & Receiving

### UC-006 — Place and Manage Purchase Orders

| Attribute | Detail |
|-----------|--------|
| **Use Case ID** | UC-006 |
| **Use Case Name** | Place and Manage Purchase Orders |
| **Goal** | Create authorized commercial commitments to suppliers that define what will be ordered, enabling controlled inbound supply and financial accountability. |
| **Primary Actor** | Buyer |
| **Supporting Actors** | Purchasing Manager, Supplier / Vendor, Finance Manager, Receiving Clerk |
| **Trigger** | Replenishment planning identifies a purchase need, safety stock is breached, or an existing purchase order requires amendment or cancellation. |
| **Business Process** | BP-05 — Purchase Order Placement |
| **Related Functional Requirements** | FR-013, FR-021, FR-022 |
| **Related Business Rules** | BR-007 (Purchase Order Required for Supplier Receipt), BR-008 (Three-Way Match Before Payment), BR-027 (No Reorder of Discontinued Products) |

---

### UC-007 — Plan Expected Inbound Deliveries

| Attribute | Detail |
|-----------|--------|
| **Use Case ID** | UC-007 |
| **Use Case Name** | Plan Expected Inbound Deliveries |
| **Goal** | Communicate and track expected supplier deliveries so receiving operations and replenishment planners can anticipate inbound supply. |
| **Primary Actor** | Buyer |
| **Supporting Actors** | Warehouse Manager, Receiving Clerk, Supplier / Vendor, Logistics / Carrier Partner |
| **Trigger** | A purchase order is confirmed, supplier communicates shipment schedule, or inbound delivery timing changes. |
| **Business Process** | BP-06 — Inbound Shipment Planning |
| **Related Functional Requirements** | FR-014, FR-055 |
| **Related Business Rules** | — |

---

### UC-008 — Receive and Verify Supplier Goods

| Attribute | Detail |
|-----------|--------|
| **Use Case ID** | UC-008 |
| **Use Case Name** | Receive and Verify Supplier Goods |
| **Goal** | Confirm quantity, product identity, and condition of inbound supplier shipments before stock is accepted into inventory records. |
| **Primary Actor** | Receiving Clerk |
| **Supporting Actors** | Supplier / Vendor, Warehouse Manager, Buyer, Logistics / Carrier Partner |
| **Trigger** | A supplier shipment arrives at the receiving dock with purchase order or authorized receipt documentation. |
| **Business Process** | BP-07 — Goods Receipt & Verification |
| **Related Functional Requirements** | FR-015, FR-017, FR-003 |
| **Related Business Rules** | BR-004 (Verify Before Inventory Acceptance), BR-007 (Purchase Order Required for Supplier Receipt), BR-016 (Minimum Remaining Shelf Life at Receipt), BR-017 (Lot or Batch Capture for Traceable Products), BR-030 (Bonded Inventory Customs Clearance) |

---

### UC-009 — Document and Resolve Receipt Discrepancies

| Attribute | Detail |
|-----------|--------|
| **Use Case ID** | UC-009 |
| **Use Case Name** | Document and Resolve Receipt Discrepancies |
| **Goal** | Record and resolve differences between expected and received goods while preserving supplier accountability and evidence for claims. |
| **Primary Actor** | Receiving Clerk |
| **Supporting Actors** | Warehouse Manager, Buyer, Supplier / Vendor, Finance Manager |
| **Trigger** | Verification identifies short shipment, over-shipment, wrong item, damage, or shelf-life non-compliance at receipt. |
| **Business Process** | BP-08 — Receipt Discrepancy Resolution |
| **Related Functional Requirements** | FR-016, FR-020 |
| **Related Business Rules** | BR-006 (Document Receipt Discrepancies), BR-008 (Three-Way Match Before Payment), BR-016 (Minimum Remaining Shelf Life at Receipt) |

---

### UC-010 — Perform Stock Put-Away

| Attribute | Detail |
|-----------|--------|
| **Use Case ID** | UC-010 |
| **Use Case Name** | Perform Stock Put-Away |
| **Goal** | Move verified received goods to designated storage locations and confirm availability for sale and fulfillment. |
| **Primary Actor** | Warehouse Staff |
| **Supporting Actors** | Receiving Clerk, Warehouse Manager, Warehouse Picker / Packer |
| **Trigger** | Goods receipt verification is complete and stock awaits placement in storage. |
| **Business Process** | BP-09 — Stock Put-Away & Storage |
| **Related Functional Requirements** | FR-018 |
| **Related Business Rules** | BR-005 (Put-Away Before Availability), BR-014 (FEFO Rotation for Shelf-Life Products), BR-015 (FIFO Rotation for Standard Goods), BR-030 (Bonded Inventory Customs Clearance) |

---

### UC-011 — Receive Return and Non-PO Inbound Stock

| Attribute | Detail |
|-----------|--------|
| **Use Case ID** | UC-011 |
| **Use Case Name** | Receive Return and Non-PO Inbound Stock |
| **Goal** | Accept and record inbound stock that arrives without a standard purchase order, including customer returns and approved ad-hoc receipts. |
| **Primary Actor** | Receiving Clerk |
| **Supporting Actors** | Customer Service Representative, Warehouse Manager, Inventory Controller |
| **Trigger** | Customer return shipment arrives, approved ad-hoc receipt is authorized, or non-PO inbound stock requires recording. |
| **Business Process** | BP-07 — Goods Receipt & Verification; BP-27 — Customer Return Intake |
| **Related Functional Requirements** | FR-019 |
| **Related Business Rules** | BR-004 (Verify Before Inventory Acceptance), BR-025 (Return Authorization Required) |

---

## Domain 3: Inventory Visibility & Status

### UC-012 — Monitor Inventory Status

| Attribute | Detail |
|-----------|--------|
| **Use Case ID** | UC-012 |
| **Use Case Name** | Monitor Inventory Status |
| **Goal** | Continuously observe stock levels and status indicators across locations to detect low stock, out-of-stock, and overstock conditions proactively. |
| **Primary Actor** | Inventory Controller |
| **Supporting Actors** | Operations Director, Warehouse Manager, Purchasing Manager |
| **Trigger** | Scheduled monitoring cycle, threshold breach, or management request for inventory health review. |
| **Business Process** | BP-10 — Inventory Status Monitoring |
| **Related Functional Requirements** | FR-026, FR-023 |
| **Related Business Rules** | BR-009 (Reorder at Reorder Level), BR-013 (Quarantine Exclusion from Sellable Stock) |

---

### UC-013 — Inquire Inventory Availability

| Attribute | Detail |
|-----------|--------|
| **Use Case ID** | UC-013 |
| **Use Case Name** | Inquire Inventory Availability |
| **Goal** | Provide accurate on-hand, reserved, and available-to-promise visibility to support sales conversations, customer service, and fulfillment planning without warehouse escalation. |
| **Primary Actor** | Sales Representative |
| **Supporting Actors** | Customer Service Representative, Sales Manager, B2B Customer, B2C Customer |
| **Trigger** | Customer or internal stakeholder requests stock availability, product lookup, or network-wide availability check. |
| **Business Process** | BP-10 — Inventory Status Monitoring; BP-16 — Order Availability Confirmation |
| **Related Functional Requirements** | FR-023, FR-024, FR-025, FR-027, FR-028 |
| **Related Business Rules** | BR-001 (ATP-Only Customer Commitment) |

---

## Domain 4: Inventory Control & Accuracy

### UC-014 — Perform Cycle Count

| Attribute | Detail |
|-----------|--------|
| **Use Case ID** | UC-014 |
| **Use Case Name** | Perform Cycle Count |
| **Goal** | Verify physical stock against system records through scheduled partial counts without disrupting full warehouse operations. |
| **Primary Actor** | Warehouse Staff |
| **Supporting Actors** | Inventory Controller, Warehouse Manager |
| **Trigger** | Cycle count schedule assigns products or locations for counting, or Class A SKU requires elevated count frequency. |
| **Business Process** | BP-11 — Cycle Counting |
| **Related Functional Requirements** | FR-030, FR-031 |
| **Related Business Rules** | BR-018 (Blind Cycle Counting), BR-032 (Class A Priority Monitoring) |

---

### UC-015 — Conduct Full Physical Inventory Count

| Attribute | Detail |
|-----------|--------|
| **Use Case ID** | UC-015 |
| **Use Case Name** | Conduct Full Physical Inventory Count |
| **Goal** | Execute a comprehensive wall-to-wall physical count at a location to establish authoritative inventory accuracy baseline. |
| **Primary Actor** | Inventory Controller |
| **Supporting Actors** | Warehouse Manager, Warehouse Staff, Operations Director, Finance Manager |
| **Trigger** | Annual or periodic full count cycle, location go-live cutover, or audit-mandated physical verification. |
| **Business Process** | BP-12 — Full Physical Inventory Count |
| **Related Functional Requirements** | FR-032 |
| **Related Business Rules** | BR-024 (Physical Inventory Freeze) |

---

### UC-016 — Investigate and Approve Count Variances

| Attribute | Detail |
|-----------|--------|
| **Use Case ID** | UC-016 |
| **Use Case Name** | Investigate and Approve Count Variances |
| **Goal** | Investigate root causes of count discrepancies and obtain independent approval before adjusting system records. |
| **Primary Actor** | Warehouse Manager |
| **Supporting Actors** | Inventory Controller, Operations Director, Warehouse Staff |
| **Trigger** | Cycle count or physical count identifies variance between system quantity and physical quantity. |
| **Business Process** | BP-13 — Count Variance Investigation & Approval |
| **Related Functional Requirements** | FR-033, FR-034 |
| **Related Business Rules** | BR-019 (Independent Count Approval), BR-021 (Independent Approval for Material Adjustments), BR-022 (Investigate Before Adjusting) |

---

### UC-017 — Process Stock Adjustments

| Attribute | Detail |
|-----------|--------|
| **Use Case ID** | UC-017 |
| **Use Case Name** | Process Stock Adjustments |
| **Goal** | Correct recorded inventory quantities with mandatory reason codes and appropriate authorization when physical reality differs from system records. |
| **Primary Actor** | Warehouse Manager |
| **Supporting Actors** | Inventory Controller, Operations Director, Warehouse Staff |
| **Trigger** | Approved count variance, identified damage, misplacement, or other correction requiring quantity change. |
| **Business Process** | BP-14 — Stock Adjustment & Write-Off |
| **Related Functional Requirements** | FR-035, FR-037 |
| **Related Business Rules** | BR-020 (Mandatory Adjustment Reason Codes), BR-021 (Independent Approval for Material Adjustments), BR-022 (Investigate Before Adjusting) |

---

### UC-018 — Authorize and Process Inventory Write-Offs

| Attribute | Detail |
|-----------|--------|
| **Use Case ID** | UC-018 |
| **Use Case Name** | Authorize and Process Inventory Write-Offs |
| **Goal** | Formally remove inventory value for damaged, obsolete, or lost goods with documented evidence and authorized approval. |
| **Primary Actor** | Operations Director |
| **Supporting Actors** | Finance Manager, Inventory Controller, Warehouse Manager |
| **Trigger** | Goods are confirmed damaged beyond resale, obsolete, expired, or lost and require permanent removal from inventory. |
| **Business Process** | BP-14 — Stock Adjustment & Write-Off; BP-15 — Shrinkage & Loss Management |
| **Related Functional Requirements** | FR-036 |
| **Related Business Rules** | BR-023 (Documented Write-Off Authorization), BR-020 (Mandatory Adjustment Reason Codes) |

---

### UC-019 — Manage Quarantine and Hold Stock

| Attribute | Detail |
|-----------|--------|
| **Use Case ID** | UC-019 |
| **Use Case Name** | Manage Quarantine and Hold Stock |
| **Goal** | Place inventory under quality hold or regulatory restriction and exclude it from sellable availability until cleared or dispositioned. |
| **Primary Actor** | Warehouse Manager |
| **Supporting Actors** | Inventory Controller, Operations Director, Regulatory Authority |
| **Trigger** | Quality concern, recall, customs hold, investigation requirement, or bonded inventory pending clearance. |
| **Business Process** | BP-14 — Stock Adjustment & Write-Off; BP-20 — Outbound Exception Handling |
| **Related Functional Requirements** | FR-038 |
| **Related Business Rules** | BR-013 (Quarantine Exclusion from Sellable Stock), BR-030 (Bonded Inventory Customs Clearance) |

---

### UC-020 — Analyze Shrinkage, Loss, and Obsolete Stock

| Attribute | Detail |
|-----------|--------|
| **Use Case ID** | UC-020 |
| **Use Case Name** | Analyze Shrinkage, Loss, and Obsolete Stock |
| **Goal** | Identify shrinkage patterns, loss trends, and slow-moving or obsolete inventory to drive corrective action and working capital optimization. |
| **Primary Actor** | Inventory Controller |
| **Supporting Actors** | Finance Manager, Operations Director, Purchasing Manager, Warehouse Manager |
| **Trigger** | Periodic shrinkage review, rising adjustment volumes, or aging inventory exceeds policy thresholds. |
| **Business Process** | BP-15 — Shrinkage & Loss Management |
| **Related Functional Requirements** | FR-039, FR-040 |
| **Related Business Rules** | BR-020 (Mandatory Adjustment Reason Codes), BR-027 (No Reorder of Discontinued Products) |

---

## Domain 5: Order Fulfillment

### UC-021 — Confirm Order Availability

| Attribute | Detail |
|-----------|--------|
| **Use Case ID** | UC-021 |
| **Use Case Name** | Confirm Order Availability |
| **Goal** | Validate that available-to-promise stock can support a customer order before the business commits to fulfillment. |
| **Primary Actor** | Sales Representative |
| **Supporting Actors** | Customer Service Representative, Sales Manager, B2B Customer, B2C Customer |
| **Trigger** | Customer places order or requests delivery commitment; sales or customer service initiates availability check. |
| **Business Process** | BP-16 — Order Availability Confirmation |
| **Related Functional Requirements** | FR-041 |
| **Related Business Rules** | BR-001 (ATP-Only Customer Commitment) |

---

### UC-022 — Reserve Inventory for Confirmed Orders

| Attribute | Detail |
|-----------|--------|
| **Use Case ID** | UC-022 |
| **Use Case Name** | Reserve Inventory for Confirmed Orders |
| **Goal** | Commit on-hand stock to confirmed customer orders and remove reserved quantity from available-to-promise to prevent double-allocation. |
| **Primary Actor** | Customer Service Representative |
| **Supporting Actors** | Sales Representative, Warehouse Manager, Warehouse Picker / Packer |
| **Trigger** | Customer order is confirmed for fulfillment after availability validation. |
| **Business Process** | BP-17 — Inventory Reservation |
| **Related Functional Requirements** | FR-042, FR-025 |
| **Related Business Rules** | BR-002 (Reservation at Order Confirmation), BR-010 (Safety Stock Protection), BR-029 (Promotional Stock Ring-Fencing) |

---

### UC-023 — Release Inventory Reservations

| Attribute | Detail |
|-----------|--------|
| **Use Case ID** | UC-023 |
| **Use Case Name** | Release Inventory Reservations |
| **Goal** | Return previously reserved stock to available-to-promise when orders are cancelled, amended, or no longer require committed inventory. |
| **Primary Actor** | Customer Service Representative |
| **Supporting Actors** | Sales Representative, Warehouse Manager |
| **Trigger** | Customer cancels order, order line is removed, or reservation is no longer required for fulfillment. |
| **Business Process** | BP-17 — Inventory Reservation |
| **Related Functional Requirements** | FR-043 |
| **Related Business Rules** | BR-002 (Reservation at Order Confirmation) |

---

### UC-024 — Pick, Pack, and Ship Orders

| Attribute | Detail |
|-----------|--------|
| **Use Case ID** | UC-024 |
| **Use Case Name** | Pick, Pack, and Ship Orders |
| **Goal** | Physically retrieve, verify, pack, and dispatch ordered goods and record inventory deduction only after verified pick completion. |
| **Primary Actor** | Warehouse Picker / Packer |
| **Supporting Actors** | Warehouse Manager, Logistics / Carrier Partner, Customer Service Representative |
| **Trigger** | Reserved order is released to warehouse for fulfillment execution. |
| **Business Process** | BP-18 — Pick, Pack & Ship |
| **Related Functional Requirements** | FR-044, FR-029 |
| **Related Business Rules** | BR-003 (Verified Pick Before Shipment), BR-014 (FEFO Rotation for Shelf-Life Products), BR-015 (FIFO Rotation for Standard Goods), BR-017 (Lot or Batch Capture for Traceable Products) |

---

### UC-025 — Handle Partial Fulfillment and Backorders

| Attribute | Detail |
|-----------|--------|
| **Use Case ID** | UC-025 |
| **Use Case Name** | Handle Partial Fulfillment and Backorders |
| **Goal** | Fulfill available order quantity when full quantity is unavailable and obtain customer acknowledgment for backordered remainder. |
| **Primary Actor** | Customer Service Representative |
| **Supporting Actors** | Sales Representative, Warehouse Picker / Packer, B2B Customer, B2C Customer, Purchasing Manager |
| **Trigger** | Insufficient stock to fulfill entire order quantity at confirmation or pick stage. |
| **Business Process** | BP-19 — Partial Fulfillment & Backorder Management |
| **Related Functional Requirements** | FR-045, FR-046, FR-050 |
| **Related Business Rules** | BR-028 (Backorder Customer Acknowledgment), BR-001 (ATP-Only Customer Commitment) |

---

### UC-026 — Handle Outbound Fulfillment Exceptions

| Attribute | Detail |
|-----------|--------|
| **Use Case ID** | UC-026 |
| **Use Case Name** | Handle Outbound Fulfillment Exceptions |
| **Goal** | Resolve fulfillment failures such as pick discrepancies, damaged goods, or shelf-record mismatches without compromising inventory accuracy. |
| **Primary Actor** | Warehouse Manager |
| **Supporting Actors** | Warehouse Picker / Packer, Inventory Controller, Customer Service Representative |
| **Trigger** | Pick verification fails, shelf quantity differs from system record, or outbound quality issue is identified. |
| **Business Process** | BP-20 — Outbound Exception Handling |
| **Related Functional Requirements** | FR-047 |
| **Related Business Rules** | BR-003 (Verified Pick Before Shipment), BR-013 (Quarantine Exclusion from Sellable Stock) |

---

### UC-027 — View Order Fulfillment Status

| Attribute | Detail |
|-----------|--------|
| **Use Case ID** | UC-027 |
| **Use Case Name** | View Order Fulfillment Status |
| **Goal** | Provide operations and customer-facing teams visibility into order reservation, picking, shipping, and exception status. |
| **Primary Actor** | Customer Service Representative |
| **Supporting Actors** | Sales Representative, Sales Manager, B2B Customer, B2C Customer, Warehouse Manager |
| **Trigger** | Customer or internal stakeholder inquires about order progress, shipment status, or fulfillment exception. |
| **Business Process** | BP-18 — Pick, Pack & Ship; BP-19 — Partial Fulfillment & Backorder Management |
| **Related Functional Requirements** | FR-049 |
| **Related Business Rules** | — |

---

## Domain 6: Replenishment & Inbound Supply

### UC-028 — Review Low-Stock and Out-of-Stock Alerts

| Attribute | Detail |
|-----------|--------|
| **Use Case ID** | UC-028 |
| **Use Case Name** | Review Low-Stock and Out-of-Stock Alerts |
| **Goal** | Review and acknowledge replenishment alerts so purchasing and operations respond before stockouts affect fulfillment. |
| **Primary Actor** | Purchasing Manager |
| **Supporting Actors** | Buyer, Inventory Controller, Operations Director, Warehouse Manager |
| **Trigger** | Available stock reaches reorder level, falls below minimum threshold, or reaches zero ATP. |
| **Business Process** | BP-21 — Low-Stock Alert Review |
| **Related Functional Requirements** | FR-051, FR-052, FR-076 |
| **Related Business Rules** | BR-009 (Reorder at Reorder Level), BR-032 (Class A Priority Monitoring) |

---

### UC-029 — Plan Replenishment and Create Purchase Requisitions

| Attribute | Detail |
|-----------|--------|
| **Use Case ID** | UC-029 |
| **Use Case Name** | Plan Replenishment and Create Purchase Requisitions |
| **Goal** | Translate replenishment needs into purchase requisitions and procurement actions after evaluating network availability and safety stock rules. |
| **Primary Actor** | Buyer |
| **Supporting Actors** | Purchasing Manager, Inventory Controller, Operations Director, Supplier / Vendor |
| **Trigger** | Acknowledged low-stock alert, replenishment suggestion, or planned restocking cycle. |
| **Business Process** | BP-22 — Replenishment Planning & Requisition |
| **Related Functional Requirements** | FR-053, FR-054, FR-056, FR-074 |
| **Related Business Rules** | BR-009 (Reorder at Reorder Level), BR-010 (Safety Stock Protection), BR-011 (Network Check Before Purchase), BR-027 (No Reorder of Discontinued Products) |

---

### UC-030 — Track Inbound Supply Status

| Attribute | Detail |
|-----------|--------|
| **Use Case ID** | UC-030 |
| **Use Case Name** | Track Inbound Supply Status |
| **Goal** | Monitor open purchase orders and expected inbound deliveries to inform replenishment decisions and delay response. |
| **Primary Actor** | Buyer |
| **Supporting Actors** | Purchasing Manager, Warehouse Manager, Receiving Clerk, Supplier / Vendor |
| **Trigger** | Replenishment review requires inbound visibility, supplier delivery is delayed, or receiving planning needs expected stock confirmation. |
| **Business Process** | BP-23 — Inbound Supply Tracking |
| **Related Functional Requirements** | FR-055, FR-079 |
| **Related Business Rules** | — |

---

## Domain 7: Network Balance & Transfers

### UC-031 — Request Inter-Location Stock Transfer

| Attribute | Detail |
|-----------|--------|
| **Use Case ID** | UC-031 |
| **Use Case Name** | Request Inter-Location Stock Transfer |
| **Goal** | Initiate movement of stock between locations to resolve local shortages using network inventory before new procurement. |
| **Primary Actor** | Regional / Store Manager |
| **Supporting Actors** | Warehouse Manager, Operations Director, Inventory Controller, Purchasing Manager |
| **Trigger** | Local stockout or low-stock condition while excess exists at another location, or network rebalancing need identified. |
| **Business Process** | BP-24 — Inter-Location Transfer Request |
| **Related Functional Requirements** | FR-058 |
| **Related Business Rules** | BR-011 (Network Check Before Purchase), BR-012 (Protect Source Location Minimum), BR-010 (Safety Stock Protection) |

---

### UC-032 — Approve or Reject Transfer Requests

| Attribute | Detail |
|-----------|--------|
| **Use Case ID** | UC-032 |
| **Use Case Name** | Approve or Reject Transfer Requests |
| **Goal** | Authorize or deny inter-location transfer requests based on network balance, source location capacity, and service-level impact. |
| **Primary Actor** | Operations Director |
| **Supporting Actors** | Warehouse Manager, Regional / Store Manager, Inventory Controller |
| **Trigger** | Transfer request is submitted and requires management approval per authorization policy. |
| **Business Process** | BP-24 — Inter-Location Transfer Request; BP-25 — Inter-Location Transfer Execution |
| **Related Functional Requirements** | FR-059, FR-077 |
| **Related Business Rules** | BR-012 (Protect Source Location Minimum) |

---

### UC-033 — Execute and Record Inter-Location Transfer

| Attribute | Detail |
|-----------|--------|
| **Use Case ID** | UC-033 |
| **Use Case Name** | Execute and Record Inter-Location Transfer |
| **Goal** | Physically dispatch and receive stock between locations with complete transaction history and in-transit visibility. |
| **Primary Actor** | Warehouse Staff |
| **Supporting Actors** | Warehouse Manager, Regional / Store Manager, Logistics / Carrier Partner |
| **Trigger** | Transfer request is approved and stock is ready for dispatch from source location. |
| **Business Process** | BP-25 — Inter-Location Transfer Execution |
| **Related Functional Requirements** | FR-060, FR-061, FR-063 |
| **Related Business Rules** | BR-012 (Protect Source Location Minimum), BR-017 (Lot or Batch Capture for Traceable Products) |

---

### UC-034 — Analyze and Recommend Network Rebalancing

| Attribute | Detail |
|-----------|--------|
| **Use Case ID** | UC-034 |
| **Use Case Name** | Analyze and Recommend Network Rebalancing |
| **Goal** | Proactively identify and recommend stock redistribution across the network to reduce imbalance, stockouts, and excess capital. |
| **Primary Actor** | Operations Director |
| **Supporting Actors** | Inventory Controller, Purchasing Manager, Warehouse Manager, Regional / Store Manager |
| **Trigger** | Periodic network review, rising cross-location imbalance events, or executive KPI indicates network inefficiency. |
| **Business Process** | BP-26 — Network Stock Rebalancing |
| **Related Functional Requirements** | FR-062, FR-028 |
| **Related Business Rules** | BR-011 (Network Check Before Purchase), BR-012 (Protect Source Location Minimum) |

---

## Domain 8: Returns Management

### UC-035 — Authorize and Record Customer Returns

| Attribute | Detail |
|-----------|--------|
| **Use Case ID** | UC-035 |
| **Use Case Name** | Authorize and Record Customer Returns |
| **Goal** | Issue return authorization linked to original order and return policy before goods are accepted at the warehouse. |
| **Primary Actor** | Customer Service Representative |
| **Supporting Actors** | B2B Customer, B2C Customer, Sales Representative, Receiving Clerk |
| **Trigger** | Customer requests return of purchased goods per return policy. |
| **Business Process** | BP-27 — Customer Return Intake |
| **Related Functional Requirements** | FR-064, FR-067 |
| **Related Business Rules** | BR-025 (Return Authorization Required) |

---

### UC-036 — Receive, Inspect, and Disposition Returned Goods

| Attribute | Detail |
|-----------|--------|
| **Use Case ID** | UC-036 |
| **Use Case Name** | Receive, Inspect, and Disposition Returned Goods |
| **Goal** | Receive authorized returns, assess condition, and determine restock, quarantine, or write-off disposition. |
| **Primary Actor** | Receiving Clerk |
| **Supporting Actors** | Warehouse Manager, Inventory Controller, Customer Service Representative, Finance Manager |
| **Trigger** | Authorized return shipment arrives at receiving location. |
| **Business Process** | BP-28 — Return-to-Stock or Disposal Decision |
| **Related Functional Requirements** | FR-065, FR-066, FR-067 |
| **Related Business Rules** | BR-026 (Inspect Returns Before Restocking), BR-025 (Return Authorization Required) |

---

## Domain 9: Reporting, Performance & Financial Alignment

### UC-037 — Review Inventory Dashboards and Operational Reports

| Attribute | Detail |
|-----------|--------|
| **Use Case ID** | UC-037 |
| **Use Case Name** | Review Inventory Dashboards and Operational Reports |
| **Goal** | Access inventory summary, movement, stockout, overstock, accuracy, and location performance views to manage daily operations. |
| **Primary Actor** | Operations Director |
| **Supporting Actors** | Chief Operating Officer, Inventory Controller, Warehouse Manager, Purchasing Manager, Sales Manager |
| **Trigger** | Scheduled management review, operational issue investigation, or stakeholder request for inventory snapshot. |
| **Business Process** | BP-29 — Inventory Performance Reporting |
| **Related Functional Requirements** | FR-068, FR-069, FR-070, FR-071, FR-072, FR-074 |
| **Related Business Rules** | — |

---

### UC-038 — Review Inventory Performance KPIs

| Attribute | Detail |
|-----------|--------|
| **Use Case ID** | UC-038 |
| **Use Case Name** | Review Inventory Performance KPIs |
| **Goal** | Monitor executive-level inventory KPIs including turnover, fill rate, accuracy, and working capital metrics for strategic decision-making. |
| **Primary Actor** | Chief Executive Officer |
| **Supporting Actors** | Chief Operating Officer, Chief Financial Officer, Operations Director, Finance Manager |
| **Trigger** | Executive review cycle, steering committee meeting, or KPI threshold breach. |
| **Business Process** | BP-29 — Inventory Performance Reporting |
| **Related Functional Requirements** | FR-073 |
| **Related Business Rules** | — |

---

### UC-039 — Reconcile Inventory Valuation with Finance

| Attribute | Detail |
|-----------|--------|
| **Use Case ID** | UC-039 |
| **Use Case Name** | Reconcile Inventory Valuation with Finance |
| **Goal** | Align operational inventory records with financial valuation and general ledger to support accurate month-end close and supplier payment controls. |
| **Primary Actor** | Finance Manager |
| **Supporting Actors** | Chief Financial Officer, Inventory Controller, Operations Director, Internal Auditor, External Auditor |
| **Trigger** | Month-end close cycle, valuation variance identified, or audit reconciliation requirement. |
| **Business Process** | BP-30 — Inventory Valuation & Financial Reconciliation |
| **Related Functional Requirements** | FR-075, FR-089 |
| **Related Business Rules** | BR-008 (Three-Way Match Before Payment), BR-031 (Consignment Ownership at Consumption) |

---

## Domain 10: Commercial Alignment & Governance

### UC-040 — Confirm Promotional and Launch Stock Readiness

| Attribute | Detail |
|-----------|--------|
| **Use Case ID** | UC-040 |
| **Use Case Name** | Confirm Promotional and Launch Stock Readiness |
| **Goal** | Verify that ring-fenced promotional inventory is available and sufficient before campaign or product launch commitment. |
| **Primary Actor** | Marketing Manager |
| **Supporting Actors** | Purchasing Manager, Warehouse Manager, Sales Manager, Operations Director |
| **Trigger** | Upcoming promotional campaign, product launch, or channel-specific stock commitment deadline. |
| **Business Process** | BP-31 — Promotional & Launch Stock Readiness |
| **Related Functional Requirements** | FR-057, FR-080 |
| **Related Business Rules** | BR-029 (Promotional Stock Ring-Fencing) |

---

### UC-041 — Conduct Inventory Audit and Control Review

| Attribute | Detail |
|-----------|--------|
| **Use Case ID** | UC-041 |
| **Use Case Name** | Conduct Inventory Audit and Control Review |
| **Goal** | Test inventory controls, review audit trails, and verify compliance with governance policies and segregation of duties. |
| **Primary Actor** | Internal Auditor |
| **Supporting Actors** | External Auditor, Finance Manager, Operations Director, Inventory Controller |
| **Trigger** | Scheduled internal audit cycle, control breach detection, or external audit engagement. |
| **Business Process** | BP-32 — Inventory Audit & Control Review |
| **Related Functional Requirements** | FR-087, FR-088 |
| **Related Business Rules** | BR-019 (Independent Count Approval), BR-021 (Independent Approval for Material Adjustments), BR-023 (Documented Write-Off Authorization) |

---

## Domain 11: Cross-Cutting System Interactions

### UC-042 — View Inventory Movement and Transaction History

| Attribute | Detail |
|-----------|--------|
| **Use Case ID** | UC-042 |
| **Use Case Name** | View Inventory Movement and Transaction History |
| **Goal** | Trace complete history of inventory movements by product, location, user, and date range for operational investigation and accountability. |
| **Primary Actor** | Inventory Controller |
| **Supporting Actors** | Warehouse Manager, Finance Manager, Internal Auditor, Operations Director |
| **Trigger** | Discrepancy investigation, customer inquiry, or management request for movement traceability. |
| **Business Process** | BP-10 — Inventory Status Monitoring; BP-29 — Inventory Performance Reporting |
| **Related Functional Requirements** | FR-029 |
| **Related Business Rules** | BR-017 (Lot or Batch Capture for Traceable Products) |

---

### UC-043 — Query and Review Audit Trail

| Attribute | Detail |
|-----------|--------|
| **Use Case ID** | UC-043 |
| **Use Case Name** | Query and Review Audit Trail |
| **Goal** | Access immutable record of all material inventory changes with user identity, timestamp, and before/after state for governance and compliance. |
| **Primary Actor** | Internal Auditor |
| **Supporting Actors** | External Auditor, Finance Manager, Operations Director |
| **Trigger** | Audit engagement, control testing, fraud investigation, or regulatory inquiry. |
| **Business Process** | BP-32 — Inventory Audit & Control Review |
| **Related Functional Requirements** | FR-086, FR-083 |
| **Related Business Rules** | BR-019 (Independent Count Approval), BR-020 (Mandatory Adjustment Reason Codes), BR-021 (Independent Approval for Material Adjustments) |

---

### UC-044 — Manage User Accounts and Role Assignments

| Attribute | Detail |
|-----------|--------|
| **Use Case ID** | UC-044 |
| **Use Case Name** | Manage User Accounts and Role Assignments |
| **Goal** | Provision, modify, and deactivate user accounts with appropriate role assignments to ensure authorized system access. |
| **Primary Actor** | System Administrator |
| **Supporting Actors** | Operations Director, Internal Auditor |
| **Trigger** | New employee onboarding, role change, location reassignment, or employee departure. |
| **Business Process** | User Access & Accountability (BRD Section 8.1, 16) |
| **Related Functional Requirements** | FR-085 |
| **Related Business Rules** | — |

---

### UC-045 — Enforce Role-Based and Location-Scoped Access

| Attribute | Detail |
|-----------|--------|
| **Use Case ID** | UC-045 |
| **Use Case Name** | Enforce Role-Based and Location-Scoped Access |
| **Goal** | Ensure users can only perform permitted functions within assigned locations and that conflicting duties are segregated. |
| **Primary Actor** | System Administrator |
| **Supporting Actors** | Internal Auditor, Operations Director, Warehouse Manager |
| **Trigger** | User attempts system action; role or permission policy is defined or updated; segregation of duties rule applies. |
| **Business Process** | User Access & Accountability (BRD Section 16) |
| **Related Functional Requirements** | FR-081, FR-082, FR-084 |
| **Related Business Rules** | BR-019 (Independent Count Approval), BR-021 (Independent Approval for Material Adjustments) |

---

### UC-046 — Import Initial Product and Stock Master Data

| Attribute | Detail |
|-----------|--------|
| **Use Case ID** | UC-046 |
| **Use Case Name** | Import Initial Product and Stock Master Data |
| **Goal** | Load verified product catalog and opening stock balances to establish authoritative system baseline at location go-live. |
| **Primary Actor** | Inventory Controller |
| **Supporting Actors** | System Administrator, Operations Director, Finance Manager, Warehouse Manager |
| **Trigger** | New location or system go-live requires bulk load of product master and verified opening balances. |
| **Business Process** | BP-01 — Product Master Data Management; BP-02 — Location & Warehouse Setup |
| **Related Functional Requirements** | FR-090 |
| **Related Business Rules** | — |

---

### UC-047 — Receive and Respond to Operational Notifications

| Attribute | Detail |
|-----------|--------|
| **Use Case ID** | UC-047 |
| **Use Case Name** | Receive and Respond to Operational Notifications |
| **Goal** | Deliver timely alerts for low stock, pending approvals, transfer exceptions, inbound delays, and campaign readiness so responsible actors can act. |
| **Primary Actor** | Warehouse Manager |
| **Supporting Actors** | Purchasing Manager, Operations Director, Buyer, Marketing Manager, Customer Service Representative |
| **Trigger** | System detects threshold breach, pending approval, exception condition, or readiness deadline approaching. |
| **Business Process** | BP-21 — Low-Stock Alert Review; BP-24 — Inter-Location Transfer Request; BP-31 — Promotional & Launch Stock Readiness |
| **Related Functional Requirements** | FR-076, FR-077, FR-078, FR-079, FR-080 |
| **Related Business Rules** | BR-009 (Reorder at Reorder Level) |

---

### UC-048 — Support Multi-Location Split Fulfillment

| Attribute | Detail |
|-----------|--------|
| **Use Case ID** | UC-048 |
| **Use Case Name** | Support Multi-Location Split Fulfillment |
| **Goal** | Fulfill a single customer order from multiple inventory locations when no single location holds sufficient available stock. |
| **Primary Actor** | Warehouse Manager |
| **Supporting Actors** | Customer Service Representative, Warehouse Picker / Packer, Operations Director, Logistics / Carrier Partner |
| **Trigger** | Confirmed order quantity exceeds single-location ATP but network-wide stock can satisfy the order. |
| **Business Process** | BP-18 — Pick, Pack & Ship; BP-19 — Partial Fulfillment & Backorder Management |
| **Related Functional Requirements** | FR-048 |
| **Related Business Rules** | BR-001 (ATP-Only Customer Commitment), BR-002 (Reservation at Order Confirmation) |

---

## Traceability Summary

### Use Cases by Business Process

| Business Process | Use Case(s) |
|------------------|-------------|
| BP-01 | UC-001, UC-005, UC-046 |
| BP-02 | UC-002, UC-046 |
| BP-03 | UC-003, UC-005 |
| BP-04 | UC-004 |
| BP-05 | UC-006 |
| BP-06 | UC-007 |
| BP-07 | UC-008, UC-011 |
| BP-08 | UC-009 |
| BP-09 | UC-010 |
| BP-10 | UC-012, UC-013, UC-042 |
| BP-11 | UC-014 |
| BP-12 | UC-015 |
| BP-13 | UC-016 |
| BP-14 | UC-017, UC-018, UC-019 |
| BP-15 | UC-018, UC-020 |
| BP-16 | UC-013, UC-021 |
| BP-17 | UC-022, UC-023 |
| BP-18 | UC-024, UC-027, UC-048 |
| BP-19 | UC-025, UC-027, UC-048 |
| BP-20 | UC-019, UC-026 |
| BP-21 | UC-028, UC-047 |
| BP-22 | UC-029 |
| BP-23 | UC-030 |
| BP-24 | UC-031, UC-032, UC-047 |
| BP-25 | UC-032, UC-033 |
| BP-26 | UC-034 |
| BP-27 | UC-011, UC-035 |
| BP-28 | UC-036 |
| BP-29 | UC-037, UC-038, UC-042 |
| BP-30 | UC-039 |
| BP-31 | UC-040, UC-047 |
| BP-32 | UC-041, UC-043 |

### Functional Requirement Coverage

All 90 functional requirements (FR-001 through FR-090) are covered by at least one use case in this catalog.

### Business Rule Coverage

All 32 business rules (BR-001 through BR-032) are referenced by at least one use case in this catalog.

---

## Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Senior Business Analyst | | | |
| Product Owner | | | |
| Operations Director | | | |

---

*End of Use Case Catalog*

*Document ID: SRS-UC-001 | Version 1.0 | July 5, 2026*
