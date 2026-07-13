# Role Responsibilities: Inventory Management System

**Document Owner:** Business Analyst  
**Purpose:** Define discrete responsibilities for each IMS business user role with traceability to functional requirements and business processes  
**Audience:** Product owners, business analysts, solution designers, training leads, and QA  
**Scope:** Business responsibilities only — system permissions and access control are out of scope  
**Based On:** User Roles Document (UR-01–UR-19), Functional Requirements (FR-001–FR-090), Business Process Analysis (BP-01–BP-32)

---

## Document Conventions

| Convention | Meaning |
|------------|---------|
| **UR-xx** | User Role identifier |
| **FR-xxx** | Functional Requirement identifier |
| **BP-xx** | Business Process identifier |

Each responsibility is a distinct, accountable business activity performed by the role. Functional requirements describe system capabilities that support the responsibility; they do not define access rights.

---

## UR-01: Chief Executive Officer (CEO)

**Business Purpose:** Provide executive accountability for company strategy, growth, and overall business performance, including inventory as a strategic business capability.

---

### R-01-01: Review Executive Inventory Performance

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Review Executive Inventory Performance |
| **Description** | Periodically review consolidated inventory performance summaries including stock value, turnover trends, stockout frequency, fill rate, and network health indicators to assess whether inventory operations support strategic objectives. |
| **Business Importance** | Enables evidence-based strategic decisions on growth, investment, and risk management; prevents inventory performance gaps from remaining invisible until they affect revenue or working capital. |
| **Related Functional Requirements** | FR-068, FR-070, FR-073, FR-075 |
| **Related Business Processes** | BP-29 |

---

### R-01-02: Authorize Strategic Network and Location Decisions

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Authorize Strategic Network and Location Decisions |
| **Description** | Approve major decisions affecting the inventory location network such as new warehouse or store openings, network expansion, and significant rebalancing strategies that commit working capital or operational capacity. |
| **Business Importance** | Ensures network growth aligns with business strategy and financial capacity; prevents uncontrolled location proliferation that fragments inventory investment and operational focus. |
| **Related Functional Requirements** | FR-005, FR-006, FR-007, FR-062 |
| **Related Business Processes** | BP-02, BP-26 |

---

### R-01-03: Hold Leadership Accountable for Inventory KPIs

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Hold Leadership Accountable for Inventory KPIs |
| **Description** | Set expectations with executive and operational leadership on inventory KPI targets; review performance against those targets and direct corrective action when sustained underperformance threatens business objectives. |
| **Business Importance** | Drives organizational focus on inventory as a strategic capability; links operational metrics to executive accountability and board reporting. |
| **Related Functional Requirements** | FR-071, FR-073 |
| **Related Business Processes** | BP-29, BP-32 |

---

### R-01-04: Approve Major Inventory Policy Changes

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Approve Major Inventory Policy Changes |
| **Description** | Authorize significant changes to inventory management policy that affect working capital targets, write-off thresholds, network service levels, or enterprise-wide operational standards. |
| **Business Importance** | Protects the organization from policy drift that increases financial exposure or operational risk; ensures major governance changes receive appropriate executive scrutiny. |
| **Related Functional Requirements** | FR-012, FR-036, FR-037 |
| **Related Business Processes** | BP-03, BP-14, BP-32 |

---

## UR-02: Chief Operating Officer (COO)

**Business Purpose:** Lead end-to-end operational performance across warehousing, fulfillment, and supply coordination.

---

### R-02-01: Drive Operational Standardization Across Locations

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Drive Operational Standardization Across Locations |
| **Description** | Mandate consistent inventory processes, approval standards, and performance expectations across all warehouses and fulfillment locations; address location-level deviations that create uneven service and accuracy. |
| **Business Importance** | Reduces firefighting and escalations caused by inconsistent practices; enables scalable operations as the network grows without proportional management overhead. |
| **Related Functional Requirements** | FR-012, FR-072 |
| **Related Business Processes** | BP-10, BP-29, BP-32 |

---

### R-02-02: Approve High-Value Inventory Decisions

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Approve High-Value Inventory Decisions |
| **Description** | Review and approve inventory adjustments, write-offs, and inter-location transfers that exceed operational management authority thresholds due to financial or network impact. |
| **Business Importance** | Provides executive oversight proportional to financial risk; prevents large-scale inventory changes without appropriate governance. |
| **Related Functional Requirements** | FR-037, FR-059, FR-077 |
| **Related Business Processes** | BP-14, BP-24, BP-26 |

---

### R-02-03: Monitor Network Fulfillment and Accuracy Performance

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Monitor Network Fulfillment and Accuracy Performance |
| **Description** | Review network-wide fulfillment performance, inventory accuracy trends, stockout conditions, and exception volumes to identify systemic issues requiring operational intervention. |
| **Business Importance** | Enables proactive correction before customer-facing failures accumulate; supports continuous improvement across the fulfillment network. |
| **Related Functional Requirements** | FR-068, FR-070, FR-071, FR-072, FR-073 |
| **Related Business Processes** | BP-10, BP-15, BP-18, BP-19, BP-29 |

---

### R-02-04: Resolve Cross-Functional Operational Escalations

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Resolve Cross-Functional Operational Escalations |
| **Description** | Arbitrate escalated conflicts between sales, operations, purchasing, and warehouse teams when stock availability, fulfillment failures, or replenishment timing threaten customer commitments or network balance. |
| **Business Importance** | Prevents unresolved inter-department disputes from delaying replenishment, transfers, and customer resolution; maintains service continuity during supply constraints. |
| **Related Functional Requirements** | FR-028, FR-046, FR-047, FR-056, FR-062 |
| **Related Business Processes** | BP-16, BP-19, BP-21, BP-24, BP-26 |

---

### R-02-05: Sponsor Inventory Control and Audit Readiness

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Sponsor Inventory Control and Audit Readiness |
| **Description** | Champion enforcement of inventory controls, segregation of duties, and audit remediation actions identified through internal and external audit reviews. |
| **Business Importance** | Reduces fraud, error, and audit finding risk; demonstrates management commitment to control effectiveness required for financial statement reliability. |
| **Related Functional Requirements** | FR-086, FR-087, FR-088 |
| **Related Business Processes** | BP-32 |

---

### R-02-06: Review Executive Operational Dashboards

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Review Executive Operational Dashboards |
| **Description** | Consume executive-level inventory dashboards and KPI reports to assess operational health, identify trends, and direct improvement initiatives across the location network. |
| **Business Importance** | Provides the COO with a single operational view without manual report compilation; supports timely intervention on deteriorating metrics. |
| **Related Functional Requirements** | FR-068, FR-073 |
| **Related Business Processes** | BP-29 |

---

## UR-03: Chief Financial Officer (CFO)

**Business Purpose:** Ensure inventory is managed as a balance-sheet asset with accurate valuation and controlled working capital investment.

---

### R-03-01: Oversee Inventory Working Capital Performance

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Oversee Inventory Working Capital Performance |
| **Description** | Monitor inventory carrying cost, turnover, days of supply, and excess stock trends; challenge operations and purchasing when working capital is trapped in slow-moving or obsolete inventory. |
| **Business Importance** | Protects cash flow and balance sheet efficiency; aligns inventory investment with revenue and margin objectives. |
| **Related Functional Requirements** | FR-070, FR-073, FR-075 |
| **Related Business Processes** | BP-29, BP-30 |

---

### R-03-02: Approve Inventory-Related Financial Policies

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Approve Inventory-Related Financial Policies |
| **Description** | Authorize financial policies governing write-off thresholds, inventory valuation methods, and capital allocation for inventory initiatives and large purchase commitments. |
| **Business Importance** | Establishes financial guardrails for inventory decisions; prevents unauthorized write-offs and unbudgeted inventory investment. |
| **Related Functional Requirements** | FR-036, FR-037, FR-075 |
| **Related Business Processes** | BP-05, BP-14, BP-30 |

---

### R-03-03: Review Inventory Valuation and Financial Alignment

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Review Inventory Valuation and Financial Alignment |
| **Description** | Review inventory valuation summaries and reconciliation outcomes to confirm operational inventory records support accurate balance sheet reporting before month-end close and audit periods. |
| **Business Importance** | Reduces material misstatement risk; ensures executive confidence in published financial results. |
| **Related Functional Requirements** | FR-075, FR-089 |
| **Related Business Processes** | BP-30 |

---

### R-03-04: Support External Audit and Sign Off on Responses

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Support External Audit and Sign Off on Responses |
| **Description** | Engage with external auditors on inventory-related findings; review management responses and corrective action plans for material control deficiencies or valuation issues. |
| **Business Importance** | Protects audit opinion quality and investor confidence; ensures inventory control weaknesses receive executive attention and remediation. |
| **Related Functional Requirements** | FR-087, FR-089 |
| **Related Business Processes** | BP-30, BP-32 |

---

### R-03-05: Review Executive Financial Inventory Reports

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Review Executive Financial Inventory Reports |
| **Description** | Consume executive inventory performance and valuation reports including shrinkage trends, write-off volumes, and aging inventory to inform board and investor communications. |
| **Business Importance** | Connects operational inventory outcomes to financial narrative; enables early identification of trends affecting profitability. |
| **Related Functional Requirements** | FR-069, FR-039, FR-073, FR-075 |
| **Related Business Processes** | BP-29, BP-30 |

---

## UR-04: Operations Director

**Business Purpose:** Own day-to-day operational performance across warehouses and fulfillment, balancing network stock distribution, accuracy, and service levels.

---

### R-04-01: Configure and Maintain Location Network

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Configure and Maintain Location Network |
| **Description** | Define, update, and deactivate inventory locations including warehouses, stores, and distribution points; maintain location hierarchy and operational status reflecting the distribution network structure. |
| **Business Importance** | Establishes the foundation for accurate stock assignment, reporting, and accountability across all sites. |
| **Related Functional Requirements** | FR-005, FR-006, FR-007, FR-010 |
| **Related Business Processes** | BP-02 |

---

### R-04-02: Monitor Network Inventory Health

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Monitor Network Inventory Health |
| **Description** | Review daily network stock levels, status indicators, low-stock counts, and fulfillment queues across authorized locations to identify problems requiring intervention. |
| **Business Importance** | Enables proactive management before stockouts and fulfillment failures reach customers; replaces fragmented spreadsheet monitoring. |
| **Related Functional Requirements** | FR-023, FR-026, FR-027, FR-068, FR-070 |
| **Related Business Processes** | BP-10, BP-29 |

---

### R-04-03: Approve Stock Adjustments and Write-Offs

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Approve Stock Adjustments and Write-Offs |
| **Description** | Review and approve inventory adjustments and write-offs submitted by warehouse managers and inventory control that exceed local authority or fall within operations director approval thresholds. |
| **Business Importance** | Ensures material inventory changes receive appropriate oversight; maintains segregation between initiator and approver for high-impact transactions. |
| **Related Functional Requirements** | FR-035, FR-036, FR-037, FR-077 |
| **Related Business Processes** | BP-13, BP-14 |

---

### R-04-04: Approve Inter-Location Transfer Requests

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Approve Inter-Location Transfer Requests |
| **Description** | Review transfer requests for network balancing and store replenishment; approve, reject, or modify proposed transfers considering source and destination stock positions and minimum threshold protection. |
| **Business Importance** | Prevents unauthorized stock movements that create new imbalances; optimizes use of existing network inventory before new purchasing. |
| **Related Functional Requirements** | FR-058, FR-059, FR-063, FR-077 |
| **Related Business Processes** | BP-24, BP-26 |

---

### R-04-05: Oversee Count Programs and Variance Resolution

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Oversee Count Programs and Variance Resolution |
| **Description** | Monitor cycle count schedules, full count execution, and material variance investigations; ensure count programs run on schedule and variances are resolved with documented root cause. |
| **Business Importance** | Sustains inventory accuracy across the network; prevents chronic discrepancy accumulation that undermines trust in system data. |
| **Related Functional Requirements** | FR-030, FR-032, FR-033, FR-034, FR-071 |
| **Related Business Processes** | BP-11, BP-12, BP-13 |

---

### R-04-06: Manage Order Reservations and Fulfillment Oversight

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Manage Order Reservations and Fulfillment Oversight |
| **Description** | Oversee inventory reservation for confirmed orders, backorder queue management, and multi-location split fulfillment decisions when network ATP can satisfy demand no single location can fulfill alone. |
| **Business Importance** | Maximizes fill rate while protecting ATP integrity; reduces order rejections when aggregate network stock is sufficient. |
| **Related Functional Requirements** | FR-042, FR-043, FR-046, FR-048, FR-056 |
| **Related Business Processes** | BP-17, BP-19, BP-16 |

---

### R-04-07: Coordinate Replenishment and Supply Escalations

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Coordinate Replenishment and Supply Escalations |
| **Description** | Respond to low-stock escalations from sales and warehouse teams; coordinate with purchasing on replenishment urgency and safety stock exceptions when fulfillment demand threatens minimum buffers. |
| **Business Importance** | Bridges demand and supply during constraints; prevents safety stock erosion without documented replenishment plans. |
| **Related Functional Requirements** | FR-051, FR-052, FR-056, FR-076 |
| **Related Business Processes** | BP-21, BP-22, BP-03 |

---

### R-04-08: Monitor In-Transit and Network Rebalancing

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Monitor In-Transit and Network Rebalancing |
| **Description** | Track inventory in transit between locations; review network rebalancing recommendations and initiate corrective transfers when persistent imbalances are identified. |
| **Business Importance** | Maintains visibility during transfer lead time; optimizes enterprise-wide stock distribution and reduces trapped overstock. |
| **Related Functional Requirements** | FR-061, FR-062, FR-028 |
| **Related Business Processes** | BP-25, BP-26 |

---

### R-04-09: Document and Reference Governance Policies

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Document and Reference Governance Policies |
| **Description** | Maintain inventory governance policies including approval thresholds, count tolerances, and reservation rules; ensure operational decisions across locations follow consistent, documented standards. |
| **Business Importance** | Eliminates ad hoc decision-making; supports auditability and fair treatment across locations. |
| **Related Functional Requirements** | FR-012 |
| **Related Business Processes** | BP-03, BP-32 |

---

### R-04-10: Respond to Pending Approval Notifications

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Respond to Pending Approval Notifications |
| **Description** | Act on notifications for pending adjustments, count variances, transfers, and requisitions requiring operations director approval to prevent operational bottlenecks. |
| **Business Importance** | Reduces decision latency that delays replenishment, corrections, and stock movements. |
| **Related Functional Requirements** | FR-077 |
| **Related Business Processes** | BP-13, BP-14, BP-24, BP-22 |

---

## UR-05: Inventory Controller

**Business Purpose:** Serve as the business owner of inventory record accuracy, product master data integrity, stock policies, and physical count programs.

---

### R-05-01: Maintain Product Master Data

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Maintain Product Master Data |
| **Description** | Create and maintain product master records including SKU, name, description, unit of measure, category, and inventory tracking attributes; manage product status lifecycle across active, inactive, and discontinued states. |
| **Business Importance** | Ensures all locations reference a single product identity; eliminates ordering errors, fulfillment mismatches, and fragmented stock records. |
| **Related Functional Requirements** | FR-001, FR-002, FR-004, FR-090 |
| **Related Business Processes** | BP-01 |

---

### R-05-02: Define Stock Policies and Replenishment Thresholds

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Define Stock Policies and Replenishment Thresholds |
| **Description** | Establish and maintain reorder levels, minimum thresholds, and safety stock parameters per product and location; review and update thresholds when demand patterns or supply conditions change. |
| **Business Importance** | Enables proactive low-stock detection and threshold-driven replenishment; reduces reactive stockouts and emergency purchasing. |
| **Related Functional Requirements** | FR-008, FR-012 |
| **Related Business Processes** | BP-03 |

---

### R-05-03: Classify Products by ABC Priority

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Classify Products by ABC Priority |
| **Description** | Assign and maintain ABC classification based on revenue, velocity, and criticality; apply classification to count scheduling, alert priority, and monitoring intensity. |
| **Business Importance** | Focuses operational effort on high-impact items; improves fill rate on priority products while optimizing counting effort. |
| **Related Functional Requirements** | FR-009 |
| **Related Business Processes** | BP-04 |

---

### R-05-04: Schedule and Oversee Cycle Counts

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Schedule and Oversee Cycle Counts |
| **Description** | Plan cycle count calendars by location, category, or ABC class; assign count tasks; monitor completion and follow up on overdue or high-variance counts. |
| **Business Importance** | Sustains rotating physical verification without disruptive full-wall counts; detects discrepancies early. |
| **Related Functional Requirements** | FR-030, FR-031 |
| **Related Business Processes** | BP-11 |

---

### R-05-05: Conduct Full Physical Inventory Counts

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Conduct Full Physical Inventory Counts |
| **Description** | Plan and oversee full physical inventory counts at locations including movement freeze coordination, count execution supervision, and comprehensive variance reporting upon completion. |
| **Business Importance** | Establishes verified baselines for financial substantiation; corrects accumulated discrepancies cycle counts may not fully address. |
| **Related Functional Requirements** | FR-032, FR-010 |
| **Related Business Processes** | BP-12, BP-02 |

---

### R-05-06: Investigate Count Variances

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Investigate Count Variances |
| **Description** | Review variances exceeding defined tolerance; conduct root-cause investigation; document findings and route material variances for independent approval before balance adjustment. |
| **Business Importance** | Focuses correction effort on material discrepancies; prevents unexplained adjustments that mask systemic problems. |
| **Related Functional Requirements** | FR-033, FR-034 |
| **Related Business Processes** | BP-13 |

---

### R-05-07: Maintain Reason Codes and Adjustment Standards

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Maintain Reason Codes and Adjustment Standards |
| **Description** | Maintain the controlled list of reason codes for adjustments, write-offs, and receipt discrepancies; ensure all inventory changes are categorized for analysis and audit substantiation. |
| **Business Importance** | Enables meaningful shrinkage analysis and trend identification; uncategorized adjustments are analytically useless for loss prevention. |
| **Related Functional Requirements** | FR-011 |
| **Related Business Processes** | BP-14, BP-08, BP-13 |

---

### R-05-08: Analyze Shrinkage and Loss Trends

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Analyze Shrinkage and Loss Trends |
| **Description** | Review shrinkage and loss data aggregated by reason code, location, and period; identify recurring loss patterns and recommend corrective actions to operations leadership. |
| **Business Importance** | Converts transaction data into actionable management insight; targets loss prevention where patterns indicate systemic issues. |
| **Related Functional Requirements** | FR-039 |
| **Related Business Processes** | BP-15 |

---

### R-05-09: Produce Inventory Accuracy and Movement Reports

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Produce Inventory Accuracy and Movement Reports |
| **Description** | Generate inventory accuracy, count variance, and stock movement reports for operational review, audit substantiation, and progress tracking toward accuracy targets. |
| **Business Importance** | Measures program effectiveness; supports audit evidence without manual reconstruction of transaction history. |
| **Related Functional Requirements** | FR-029, FR-069, FR-071 |
| **Related Business Processes** | BP-29, BP-11, BP-13 |

---

### R-05-10: Support Return Disposition Decisions

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Support Return Disposition Decisions |
| **Description** | Participate in return-to-stock or disposal decisions for returned goods; ensure disposition outcomes are recorded with appropriate reason codes and inventory impact. |
| **Business Importance** | Maintains accurate sellable stock after returns processing; prevents damaged goods from re-entering fulfillment streams. |
| **Related Functional Requirements** | FR-066, FR-038 |
| **Related Business Processes** | BP-28 |

---

### R-05-11: Support Initial Data Import for Go-Live

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Support Initial Data Import for Go-Live |
| **Description** | Coordinate controlled import of initial product master data and opening stock balances with validation review before location activation. |
| **Business Importance** | Accelerates deployment without manual catalog entry; prevents go-live with embedded inventory errors. |
| **Related Functional Requirements** | FR-090 |
| **Related Business Processes** | BP-01, BP-02 |

---

## UR-06: Warehouse Manager

**Business Purpose:** Accountable for daily warehouse operations and location-level inventory accuracy at an assigned site.

---

### R-06-01: Supervise Daily Warehouse Operations

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Supervise Daily Warehouse Operations |
| **Description** | Oversee receiving, put-away, storage, picking, packing, and shipping activities at the assigned location; ensure transactions are recorded timely and warehouse team follows operational standards. |
| **Business Importance** | Maintains location service levels and inventory accuracy; translates network policies into consistent floor execution. |
| **Related Functional Requirements** | FR-029, FR-044, FR-049 |
| **Related Business Processes** | BP-06, BP-07, BP-09, BP-18 |

---

### R-06-02: Authorize Goods Receipt and Inbound Processing

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Authorize Goods Receipt and Inbound Processing |
| **Description** | Supervise and authorize goods receipt activities; review receipt discrepancies escalated by receiving clerks; ensure inbound stock progresses through put-away to available status. |
| **Business Importance** | Ensures on-hand balances reflect physical reality from point of entry; prevents phantom inventory and delayed availability updates. |
| **Related Functional Requirements** | FR-015, FR-016, FR-018 |
| **Related Business Processes** | BP-07, BP-08, BP-09 |

---

### R-06-03: Release Orders to Fulfillment Queue

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Release Orders to Fulfillment Queue |
| **Description** | Release confirmed orders to the pick queue; monitor pick list assignment and fulfillment progress; address outbound exceptions reported by pickers. |
| **Business Importance** | Controls fulfillment pacing and prioritization; ensures pick operations align with operational capacity and service commitments. |
| **Related Functional Requirements** | FR-044, FR-047, FR-078 |
| **Related Business Processes** | BP-18, BP-20 |

---

### R-06-04: Initiate Stock Adjustments and Write-Off Requests

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Initiate Stock Adjustments and Write-Off Requests |
| **Description** | Submit stock adjustment and write-off requests for discovered damage, shrinkage, spoilage, or data corrections at the location, with mandatory reason codes and supporting documentation. |
| **Business Importance** | Keeps location records aligned with physical reality; provides documented basis for financial and operational reconciliation. |
| **Related Functional Requirements** | FR-035, FR-036, FR-011 |
| **Related Business Processes** | BP-14, BP-15 |

---

### R-06-05: Approve Local Cycle Count Results

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Approve Local Cycle Count Results |
| **Description** | Review cycle count results at the location; approve immaterial variances within policy; escalate material variances to inventory control and operations director per threshold rules. |
| **Business Importance** | Provides first-line variance governance at the location; maintains segregation between counter and approver where policy requires. |
| **Related Functional Requirements** | FR-033, FR-034, FR-037 |
| **Related Business Processes** | BP-11, BP-13 |

---

### R-06-06: Execute Inter-Location Transfers

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Execute Inter-Location Transfers |
| **Description** | Dispatch approved outbound transfers from the location; confirm receipt of inbound transfers; handle partial receipts and transfer variances at the location level. |
| **Business Importance** | Ensures both sending and receiving location balances remain accurate; prevents stock appearing lost between sites. |
| **Related Functional Requirements** | FR-060, FR-061 |
| **Related Business Processes** | BP-25 |

---

### R-06-07: Manage Partial Fulfillment and Backorders

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Manage Partial Fulfillment and Backorders |
| **Description** | Process partial shipments when full order quantity is unavailable; create backorder records for remaining lines and coordinate with customer service on customer acknowledgment. |
| **Business Importance** | Balances customer service with inventory reality; avoids holding entire orders when partial delivery is acceptable. |
| **Related Functional Requirements** | FR-045, FR-046 |
| **Related Business Processes** | BP-19 |

---

### R-06-08: Process Return Receipts and Disposition

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Process Return Receipts and Disposition |
| **Description** | Oversee physical receipt of returned goods; route items through inspection; apply restock or write-off disposition based on inspection outcome. |
| **Business Importance** | Ensures only resalable goods re-enter sellable inventory; captures complete return impact on location stock. |
| **Related Functional Requirements** | FR-065, FR-066, FR-019 |
| **Related Business Processes** | BP-27, BP-28 |

---

### R-06-09: Review Location Daily Reports

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Review Location Daily Reports |
| **Description** | Review daily movement, exception, and stock status reports for the assigned location to identify issues requiring same-day action. |
| **Business Importance** | Enables proactive local management; reduces end-of-period surprise variances and fulfillment failures. |
| **Related Functional Requirements** | FR-068, FR-069, FR-072 |
| **Related Business Processes** | BP-10, BP-29 |

---

### R-06-10: Respond to Operational Notifications

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Respond to Operational Notifications |
| **Description** | Act on notifications for low-stock conditions, fulfillment exceptions, transfer delays, and pending local approvals requiring warehouse manager attention. |
| **Business Importance** | Reduces time-to-action on conditions that affect pick success and customer delivery. |
| **Related Functional Requirements** | FR-076, FR-077, FR-078 |
| **Related Business Processes** | BP-20, BP-21, BP-25 |

---

## UR-07: Receiving Clerk

**Business Purpose:** Execute frontline inbound operations by accepting deliveries, verifying goods, and recording receipts.

---

### R-07-01: Accept and Verify Inbound Deliveries

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Accept and Verify Inbound Deliveries |
| **Description** | Accept inbound shipments at the dock; verify product identity, quantity, and condition against purchase orders and delivery documentation before recording receipt. |
| **Business Importance** | Ensures inventory increases reflect verified physical goods; prevents payment for undelivered items and phantom stock. |
| **Related Functional Requirements** | FR-015, FR-017, FR-003 |
| **Related Business Processes** | BP-07 |

---

### R-07-02: Record Goods Receipt Transactions

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Record Goods Receipt Transactions |
| **Description** | Enter accepted quantities into the system upon verification; link receipts to purchase order references; record user attribution and receipt timestamp for each transaction. |
| **Business Importance** | Provides immediate inventory visibility upon arrival; creates auditable receipt history for supplier accountability. |
| **Related Functional Requirements** | FR-015, FR-029 |
| **Related Business Processes** | BP-07 |

---

### R-07-03: Document Receipt Discrepancies

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Document Receipt Discrepancies |
| **Description** | Flag and document short shipments, over-shipments, wrong items, and damaged goods with discrepancy type, quantity variance, and supporting notes; hold disputed quantity from sellable availability. |
| **Business Importance** | Protects supplier accountability and inventory accuracy; initiates resolution before incorrect stock enters fulfillment. |
| **Related Functional Requirements** | FR-016, FR-020, FR-011 |
| **Related Business Processes** | BP-08 |

---

### R-07-04: Review Expected Inbound Deliveries

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Review Expected Inbound Deliveries |
| **Description** | Review scheduled inbound deliveries by date and location to prepare the receiving dock and prioritize receipt processing for expected shipments. |
| **Business Importance** | Reduces dock congestion and receipt delays; improves timeliness of stock availability updates. |
| **Related Functional Requirements** | FR-014 |
| **Related Business Processes** | BP-06 |

---

### R-07-05: Process Return and Non-PO Receipts

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Process Return and Non-PO Receipts |
| **Description** | Receive customer returns and other authorized non-purchase-order inbound movements with appropriate return authorization or reference linkage. |
| **Business Importance** | Captures all inventory increases in one system; maintains complete movement history for returns traceability. |
| **Related Functional Requirements** | FR-019, FR-065 |
| **Related Business Processes** | BP-07, BP-28 |

---

### R-07-06: Hand Off Verified Goods for Put-Away

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Hand Off Verified Goods for Put-Away |
| **Description** | Transfer verified received goods to warehouse staff for put-away assignment; ensure receipt is recorded before physical movement to storage. |
| **Business Importance** | Maintains clear handoff between receiving and storage; supports received-vs-available stock distinction. |
| **Related Functional Requirements** | FR-018 |
| **Related Business Processes** | BP-09 |

---

## UR-08: Warehouse Picker / Packer

**Business Purpose:** Execute order fulfillment on the warehouse floor through picking, packing, and shipment preparation.

---

### R-08-01: Execute Pick Operations

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Execute Pick Operations |
| **Description** | Pick items per assigned pick list; verify product identity and quantity at the pick location; use product identifier lookup to confirm correct SKU selection. |
| **Business Importance** | Directly affects order accuracy and customer satisfaction; mis-picks generate returns, rework, and customer complaints. |
| **Related Functional Requirements** | FR-044, FR-003 |
| **Related Business Processes** | BP-18 |

---

### R-08-02: Confirm Pick and Pack Completion

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Confirm Pick and Pack Completion |
| **Description** | Confirm picked quantities and mark orders as packed per shipping standards; ensure pick verification is completed before shipment recording. |
| **Business Importance** | Triggers accurate inventory deduction and order status update; prevents shipping unverified or incomplete orders. |
| **Related Functional Requirements** | FR-044, FR-049 |
| **Related Business Processes** | BP-18 |

---

### R-08-03: Report Pick Exceptions

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Report Pick Exceptions |
| **Description** | Report unable-to-pick, short-pick, stock-not-found, and damaged-item situations encountered during picking with product, location, and order context. |
| **Business Importance** | Enables rapid exception resolution before customer impact; triggers inventory correction when physical stock differs from system. |
| **Related Functional Requirements** | FR-047, FR-078 |
| **Related Business Processes** | BP-20 |

---

### R-08-04: Prepare Shipments for Carrier Handoff

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Prepare Shipments for Carrier Handoff |
| **Description** | Pack orders per shipping standards and prepare shipments for carrier pickup with accurate manifests aligned to picked quantities. |
| **Business Importance** | Completes the physical fulfillment cycle; reduces carrier disputes and delivery failures from packaging or quantity errors. |
| **Related Functional Requirements** | FR-044 |
| **Related Business Processes** | BP-18 |

---

## UR-09: Warehouse Staff

**Business Purpose:** Support warehouse material handling including put-away, counting, and general stock movement.

---

### R-09-01: Execute Put-Away Activities

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Execute Put-Away Activities |
| **Description** | Move received goods from the dock to assigned storage locations and confirm put-away completion so stock transitions from received to available status. |
| **Business Importance** | Ensures pickers can locate goods and ATP reflects operationally available stock; prevents promising stock that cannot be found. |
| **Related Functional Requirements** | FR-018 |
| **Related Business Processes** | BP-09 |

---

### R-09-02: Perform Assigned Cycle Counts

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Perform Assigned Cycle Counts |
| **Description** | Complete assigned cycle count tasks using blind count procedures; record physical quantities for designated products and locations without viewing expected system quantities during count. |
| **Business Importance** | Produces unbiased accuracy measurement; rotating verification detects discrepancies before they compound. |
| **Related Functional Requirements** | FR-031, FR-003 |
| **Related Business Processes** | BP-11 |

---

### R-09-03: Participate in Full Physical Counts

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Participate in Full Physical Counts |
| **Description** | Count all SKUs at the location during full physical inventory events per supervisor direction; follow movement freeze procedures during active count periods. |
| **Business Importance** | Establishes verified location baseline for financial substantiation; corrects accumulated discrepancies. |
| **Related Functional Requirements** | FR-032 |
| **Related Business Processes** | BP-12 |

---

### R-09-04: Report Observed Stock Issues

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Report Observed Stock Issues |
| **Description** | Report observed damage, misplaced stock, or storage organization issues encountered during put-away, counting, or material handling to the warehouse manager. |
| **Business Importance** | Enables early correction of physical conditions that cause pick failures and inventory variance. |
| **Related Functional Requirements** | FR-035 |
| **Related Business Processes** | BP-09, BP-14, BP-15 |

---

## UR-10: Regional / Store Manager

**Business Purpose:** Manage retail store or regional location performance, ensuring local stock supports customer experience.

---

### R-10-01: Monitor Local Stock Levels

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Monitor Local Stock Levels |
| **Description** | Review on-hand, ATP, and stock status indicators for assigned store(s); identify low-stock and out-of-stock conditions affecting shelf availability and customer experience. |
| **Business Importance** | Prevents customer-facing stockouts; enables timely replenishment action before lost sales occur. |
| **Related Functional Requirements** | FR-023, FR-024, FR-026, FR-027 |
| **Related Business Processes** | BP-10 |

---

### R-10-02: Request Inter-Location Replenishment Transfers

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Request Inter-Location Replenishment Transfers |
| **Description** | Initiate transfer requests from warehouse or other locations to replenish store stock, specifying product, quantity, source preference, and business justification. |
| **Business Importance** | Corrects local stockouts using existing network inventory; faster than waiting for supplier replenishment in many cases. |
| **Related Functional Requirements** | FR-058 |
| **Related Business Processes** | BP-24 |

---

### R-10-03: Track Replenishment and Transfer Status

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Track Replenishment and Transfer Status |
| **Description** | Monitor status of pending transfer requests and expected inbound replenishment to plan shelf stocking and customer communication. |
| **Business Importance** | Reduces uncertainty about when stock will arrive; supports store staffing and merchandising decisions. |
| **Related Functional Requirements** | FR-060, FR-055, FR-028 |
| **Related Business Processes** | BP-24, BP-25, BP-23 |

---

### R-10-04: Participate in Local Count Activities

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Participate in Local Count Activities |
| **Description** | Initiate or participate in store-level cycle count requests; support count execution and escalate material variances to inventory control. |
| **Business Importance** | Maintains store-level inventory accuracy; prevents shelf-versus-system discrepancies that damage customer trust. |
| **Related Functional Requirements** | FR-030, FR-031 |
| **Related Business Processes** | BP-11 |

---

### R-10-05: Escalate Customer-Impacting Stockouts

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Escalate Customer-Impacting Stockouts |
| **Description** | Escalate persistent or high-impact stockout situations to operations director when local replenishment actions cannot resolve availability gaps in time. |
| **Business Importance** | Ensures critical availability gaps receive network-level attention; protects customer experience and sales at priority locations. |
| **Related Functional Requirements** | FR-070, FR-076 |
| **Related Business Processes** | BP-10, BP-26 |

---

### R-10-06: Review Local Performance Reports

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Review Local Performance Reports |
| **Description** | Review location-level inventory and performance snapshots for assigned stores to assess local stock health and replenishment effectiveness. |
| **Business Importance** | Supports accountability for store-level stock outcomes; identifies recurring local issues requiring process change. |
| **Related Functional Requirements** | FR-072, FR-068 |
| **Related Business Processes** | BP-29 |

---

## UR-11: Sales Manager

**Business Purpose:** Lead commercial performance by ensuring sales commitments align with supply capability.

---

### R-11-01: Confirm Large Order Feasibility

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Confirm Large Order Feasibility |
| **Description** | Validate product availability across the network before approving large or strategic sales commitments; coordinate with operations on fulfillment location and timing. |
| **Business Importance** | Prevents overpromising on high-value orders; protects win rate and customer relationships on strategic accounts. |
| **Related Functional Requirements** | FR-041, FR-024, FR-028 |
| **Related Business Processes** | BP-16 |

---

### R-11-02: Monitor Order Fulfillment for Key Accounts

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Monitor Order Fulfillment for Key Accounts |
| **Description** | Track fulfillment status, partial shipments, and backorder conditions for priority customers and large orders; intervene when fulfillment risk threatens account relationships. |
| **Business Importance** | Protects revenue from key accounts; enables proactive customer communication before delivery failures. |
| **Related Functional Requirements** | FR-049, FR-045, FR-046 |
| **Related Business Processes** | BP-18, BP-19 |

---

### R-11-03: Escalate Stockout and Fulfillment Risks

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Escalate Stockout and Fulfillment Risks |
| **Description** | Escalate stockout conditions and fulfillment failures to operations and purchasing when commercial commitments are at risk; provide demand context for replenishment prioritization. |
| **Business Importance** | Bridges commercial urgency with supply response; reduces lost deals from perceived unavailability. |
| **Related Functional Requirements** | FR-026, FR-070, FR-051 |
| **Related Business Processes** | BP-10, BP-21, BP-23 |

---

### R-11-04: Coordinate Promotional Demand with Operations

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Coordinate Promotional Demand with Operations |
| **Description** | Communicate expected promotional and campaign demand to marketing, purchasing, and operations; participate in stock readiness reviews before campaign launch. |
| **Business Importance** | Aligns sales expectations with supply preparation; prevents campaign failures due to insufficient inventory. |
| **Related Functional Requirements** | FR-057, FR-080 |
| **Related Business Processes** | BP-31 |

---

### R-11-05: Review Availability for Sales Planning

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Review Availability for Sales Planning |
| **Description** | Review network availability, stockout reports, and inbound supply projections to inform sales planning, quota setting, and promotional timing decisions. |
| **Business Importance** | Grounds sales strategy in supply reality; reduces planning based on unreliable availability assumptions. |
| **Related Functional Requirements** | FR-024, FR-028, FR-070 |
| **Related Business Processes** | BP-10, BP-29, BP-04 |

---

### R-11-06: Direct Sales Team on Availability Practices

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Direct Sales Team on Availability Practices |
| **Description** | Ensure sales representatives confirm ATP before quoting and escalate unfulfillable orders; monitor team adherence to availability confirmation practices. |
| **Business Importance** | Reduces order cancellations and customer embarrassment from stock errors at the point of sale. |
| **Related Functional Requirements** | FR-041, FR-024 |
| **Related Business Processes** | BP-16 |

---

## UR-12: Sales Representative

**Business Purpose:** Serve as the customer-facing sales professional who confirms availability and creates orders.

---

### R-12-01: Confirm Product Availability Before Quoting

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Confirm Product Availability Before Quoting |
| **Description** | Check available-to-promise quantity by location before providing quotes or accepting customer orders; identify alternative fulfillment locations when primary location is insufficient. |
| **Business Importance** | Prevents order failures and customer disappointment; eliminates dependency on manual warehouse stock checks. |
| **Related Functional Requirements** | FR-024, FR-041, FR-027 |
| **Related Business Processes** | BP-16 |

---

### R-12-02: Create Customer Orders

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Create Customer Orders |
| **Description** | Place customer orders with accurate product, quantity, and delivery expectations based on confirmed availability; communicate expected ship dates grounded in fulfillment status. |
| **Business Importance** | Converts confirmed availability into revenue; sets realistic delivery expectations that operations can meet. |
| **Related Functional Requirements** | FR-041, FR-042 |
| **Related Business Processes** | BP-16, BP-17 |

---

### R-12-03: Communicate Delivery Expectations

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Communicate Delivery Expectations |
| **Description** | Provide customers with reliable delivery dates based on confirmed availability and fulfillment location; revise expectations when availability or inbound supply changes. |
| **Business Importance** | Builds customer trust; reduces cancellations and complaints from unrealistic delivery promises. |
| **Related Functional Requirements** | FR-028, FR-055 |
| **Related Business Processes** | BP-16, BP-23 |

---

### R-12-04: Follow Up on Order Status

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Follow Up on Order Status |
| **Description** | Check order fulfillment progress for own customers; identify delays, partial shipments, or backorder conditions requiring customer communication. |
| **Business Importance** | Enables proactive customer management; reduces surprise delivery failures on active deals. |
| **Related Functional Requirements** | FR-049, FR-025 |
| **Related Business Processes** | BP-18, BP-19 |

---

### R-12-05: Escalate Unfulfillable Orders

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Escalate Unfulfillable Orders |
| **Description** | Escalate orders that cannot be fulfilled from available stock to sales manager and operations for resolution, alternative sourcing, or customer negotiation. |
| **Business Importance** | Prevents silent order failures; ensures commercial leadership aware of at-risk revenue. |
| **Related Functional Requirements** | FR-041, FR-046 |
| **Related Business Processes** | BP-16, BP-19 |

---

### R-12-06: Identify Upsell Opportunities Within Stock Constraints

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Identify Upsell Opportunities Within Stock Constraints |
| **Description** | Recommend alternative products or quantities that can be fulfilled from current ATP when primary request cannot be fully satisfied. |
| **Business Importance** | Recovers revenue from orders that might otherwise be lost; maximizes use of available inventory. |
| **Related Functional Requirements** | FR-024, FR-027, FR-050 |
| **Related Business Processes** | BP-16, BP-20 |

---

## UR-13: Customer Service Representative

**Business Purpose:** Provide frontline customer support for order inquiries, complaints, delivery updates, and return intake.

---

### R-13-01: Answer Order Status Inquiries

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Answer Order Status Inquiries |
| **Description** | Look up order fulfillment status including reserved, picking, shipped, partially shipped, and backordered states; provide accurate answers to customer "where is my order?" inquiries. |
| **Business Importance** | Reduces inquiry handling time and conflicting information; improves customer satisfaction through accurate, immediate responses. |
| **Related Functional Requirements** | FR-049, FR-025 |
| **Related Business Processes** | BP-18, BP-19 |

---

### R-13-02: Communicate Delays and Partial Shipments

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Communicate Delays and Partial Shipments |
| **Description** | Proactively inform customers of fulfillment delays, partial shipments, and backorder status with revised delivery expectations based on current fulfillment and inbound supply data. |
| **Business Importance** | Prevents surprise customer complaints; maintains trust through transparent communication. |
| **Related Functional Requirements** | FR-045, FR-046, FR-055 |
| **Related Business Processes** | BP-19, BP-23 |

---

### R-13-03: Check Product Availability for Replacements

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Check Product Availability for Replacements |
| **Description** | Verify product availability when processing replacement orders or resolving stock-related complaints; confirm ATP before committing replacement delivery dates. |
| **Business Importance** | Avoids repeating fulfillment failures on replacement orders; speeds complaint resolution. |
| **Related Functional Requirements** | FR-024, FR-041 |
| **Related Business Processes** | BP-16, BP-20 |

---

### R-13-04: Initiate Customer Return Requests

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Initiate Customer Return Requests |
| **Description** | Create return authorization records linked to original orders with product, quantity, reason, and expected resolution; communicate authorization reference to the customer. |
| **Business Importance** | Connects physical returns to commercial transactions; prevents unauthorized returns and enables accurate inventory and refund processing. |
| **Related Functional Requirements** | FR-064, FR-067 |
| **Related Business Processes** | BP-27 |

---

### R-13-05: Coordinate with Warehouse on Fulfillment Issues

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Coordinate with Warehouse on Fulfillment Issues |
| **Description** | Escalate fulfillment failures, pick exceptions, and shipment delays to warehouse management; log customer-facing issue notes for operational follow-up. |
| **Business Importance** | Bridges customer impact to operational resolution; reduces duplicate inquiries and unresolved complaints. |
| **Related Functional Requirements** | FR-047, FR-078 |
| **Related Business Processes** | BP-20 |

---

### R-13-06: Track Return Processing Status

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Track Return Processing Status |
| **Description** | Monitor return status from authorization through receipt, inspection, and final disposition; communicate outcomes and timing to customers. |
| **Business Importance** | Enables accurate customer communication on refund, replacement, or credit timing; reduces return-related escalations. |
| **Related Functional Requirements** | FR-067 |
| **Related Business Processes** | BP-27, BP-28 |

---

### R-13-07: Review Inbound Supply for Backorder Customers

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Review Inbound Supply for Backorder Customers |
| **Description** | Check inbound supply status and expected availability dates when communicating backorder recovery timelines to customers. |
| **Business Importance** | Provides realistic restock dates; reduces repeated customer contacts and frustration during supply delays. |
| **Related Functional Requirements** | FR-055, FR-028 |
| **Related Business Processes** | BP-23, BP-19 |

---

## UR-14: Marketing Manager

**Business Purpose:** Plan promotions and launches with confidence that marketed products will be adequately stocked.

---

### R-14-01: Plan Promotional Calendar with Supply Coordination

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Plan Promotional Calendar with Supply Coordination |
| **Description** | Develop promotional and launch calendar in coordination with purchasing and operations; communicate campaign timing and expected demand uplift for supply planning. |
| **Business Importance** | Aligns marketing activity with replenishment execution; prevents campaigns launched without supply preparation. |
| **Related Functional Requirements** | FR-057 |
| **Related Business Processes** | BP-31 |

---

### R-14-02: Request Stock Readiness Assessments

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Request Stock Readiness Assessments |
| **Description** | Request and review stock readiness assessments for campaign SKUs comparing current and inbound stock against promotional targets before public campaign commitment. |
| **Business Importance** | Provides go/no-go input for campaigns; avoids customer disappointment and brand damage from promotional stockouts. |
| **Related Functional Requirements** | FR-057, FR-080 |
| **Related Business Processes** | BP-31 |

---

### R-14-03: Monitor Campaign Inventory Levels

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Monitor Campaign Inventory Levels |
| **Description** | Monitor stock levels for promoted SKUs during active campaigns; respond to readiness alerts when inventory falls below campaign targets. |
| **Business Importance** | Enables mid-campaign intervention; protects promotional ROI and customer experience during high-visibility periods. |
| **Related Functional Requirements** | FR-026, FR-057, FR-080 |
| **Related Business Processes** | BP-10, BP-31 |

---

### R-14-04: Participate in Campaign Go/No-Go Decisions

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Participate in Campaign Go/No-Go Decisions |
| **Description** | Use stock readiness indications and inbound supply projections to decide whether to proceed, delay, or modify campaigns when inventory gaps are identified within the preparation window. |
| **Business Importance** | Prevents public commitment to promotions the supply chain cannot support; protects brand reputation. |
| **Related Functional Requirements** | FR-057, FR-080 |
| **Related Business Processes** | BP-31 |

---

### R-14-05: Review Inbound Replenishment for Campaign Products

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Review Inbound Replenishment for Campaign Products |
| **Description** | Review inbound replenishment status and expected delivery dates for campaign SKUs during pre-launch preparation periods. |
| **Business Importance** | Provides early visibility into whether pre-promotion stock build will complete on schedule. |
| **Related Functional Requirements** | FR-055, FR-028 |
| **Related Business Processes** | BP-31, BP-23 |

---

## UR-15: Purchasing Manager

**Business Purpose:** Lead procurement strategy and replenishment execution aligned with inventory policy and demand signals.

---

### R-15-01: Approve Purchase Requisitions and Orders

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Approve Purchase Requisitions and Orders |
| **Description** | Review and approve purchase requisitions and purchase orders within authority limits; ensure orders align with replenishment policy, budget, and inventory thresholds. |
| **Business Importance** | Maintains procurement control and spend discipline; prevents unauthorized or duplicate purchasing. |
| **Related Functional Requirements** | FR-013, FR-054, FR-021 |
| **Related Business Processes** | BP-05, BP-22 |

---

### R-15-02: Review Low-Stock Alerts and Replenishment Suggestions

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Review Low-Stock Alerts and Replenishment Suggestions |
| **Description** | Review daily low-stock and out-of-stock alerts; validate replenishment suggestions; acknowledge or dismiss alerts with documented rationale for deferred action. |
| **Business Importance** | Converts passive monitoring into purchasing action; reduces alert fatigue by distinguishing genuine needs from false positives. |
| **Related Functional Requirements** | FR-051, FR-052, FR-053, FR-074 |
| **Related Business Processes** | BP-21, BP-22 |

---

### R-15-03: Align Purchasing with Inventory Policy

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Align Purchasing with Inventory Policy |
| **Description** | Partner with inventory control on reorder parameters; ensure purchasing decisions reflect defined thresholds, ABC priorities, and safety stock rules. |
| **Business Importance** | Creates consistent replenishment discipline; reduces both stockouts and over-purchasing of slow movers. |
| **Related Functional Requirements** | FR-008, FR-009, FR-056 |
| **Related Business Processes** | BP-03, BP-04 |

---

### R-15-04: Monitor Inbound Supply Pipeline

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Monitor Inbound Supply Pipeline |
| **Description** | Track open purchase orders, expected deliveries, and inbound delays; coordinate with buyers and warehouse on receipt timing and supply risk. |
| **Business Importance** | Enables proactive response to supply disruptions; gives operations and sales realistic restock visibility. |
| **Related Functional Requirements** | FR-055, FR-014, FR-079 |
| **Related Business Processes** | BP-23, BP-06 |

---

### R-15-05: Resolve Supplier Disputes

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Resolve Supplier Disputes |
| **Description** | Lead resolution of receipt discrepancies, quantity disputes, and delivery failures with suppliers; coordinate credit and replacement outcomes with finance and receiving. |
| **Business Importance** | Protects supplier accountability and financial accuracy; prevents recurring discrepancy patterns from eroding inventory trust. |
| **Related Functional Requirements** | FR-016, FR-022 |
| **Related Business Processes** | BP-08 |

---

### R-15-06: Coordinate Emergency Procurement

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Coordinate Emergency Procurement |
| **Description** | Authorize and prioritize emergency purchase activity when stockouts threaten customer commitments; ensure emergency orders are documented and communicated to operations. |
| **Business Importance** | Recovers from supply failures quickly; balances urgency with procurement control and cost awareness. |
| **Related Functional Requirements** | FR-053, FR-017, FR-076 |
| **Related Business Processes** | BP-05, BP-21 |

---

### R-15-07: Support Promotional Stock Build

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Support Promotional Stock Build |
| **Description** | Coordinate pre-promotion purchasing and inbound timing with marketing and operations to achieve campaign stock targets before launch dates. |
| **Business Importance** | Prevents campaign stockouts that waste marketing investment and damage customer experience. |
| **Related Functional Requirements** | FR-057, FR-013 |
| **Related Business Processes** | BP-31, BP-05 |

---

### R-15-08: Review Replenishment and Supplier Performance Reports

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Review Replenishment and Supplier Performance Reports |
| **Description** | Review replenishment reports, stockout/overstock reports, and supplier delivery performance data to inform purchasing strategy and supplier relationship decisions. |
| **Business Importance** | Drives continuous improvement in procurement effectiveness; identifies chronic supply gaps requiring strategic intervention. |
| **Related Functional Requirements** | FR-074, FR-070, FR-022 |
| **Related Business Processes** | BP-29, BP-23 |

---

### R-15-09: Respond to Replenishment Notifications

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Respond to Replenishment Notifications |
| **Description** | Act on low-stock, out-of-stock, and inbound delay notifications directed to purchasing; ensure critical alerts receive timely purchasing response. |
| **Business Importance** | Reduces time from alert to purchase action; prevents preventable stockouts on priority SKUs. |
| **Related Functional Requirements** | FR-076, FR-079 |
| **Related Business Processes** | BP-21, BP-23 |

---

## UR-16: Buyer / Procurement Officer

**Business Purpose:** Execute day-to-day purchasing and supplier follow-up.

---

### R-16-01: Place Purchase Orders

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Place Purchase Orders |
| **Description** | Create purchase orders from approved requisitions or replenishment suggestions; specify product, quantity, supplier, expected delivery, and receiving location. |
| **Business Importance** | Translates replenishment decisions into supplier commitments; initiates inbound supply visibility for operations. |
| **Related Functional Requirements** | FR-013, FR-053, FR-054 |
| **Related Business Processes** | BP-05, BP-22 |

---

### R-16-02: Track Open Purchase Orders

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Track Open Purchase Orders |
| **Description** | Monitor status of open purchase orders including received versus outstanding quantities; follow up with suppliers on delayed or partial deliveries. |
| **Business Importance** | Maintains accurate inbound projections; prevents duplicate orders and unnoticed supply gaps. |
| **Related Functional Requirements** | FR-055, FR-021 |
| **Related Business Processes** | BP-23 |

---

### R-16-03: Resolve Receipt Discrepancies with Suppliers

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Resolve Receipt Discrepancies with Suppliers |
| **Description** | Work with suppliers to resolve short shipments, over-shipments, wrong items, and damage claims documented by receiving; initiate credit or replacement requests. |
| **Business Importance** | Recovers value from supplier errors; closes discrepancy records so inventory reflects agreed resolution. |
| **Related Functional Requirements** | FR-016, FR-020 |
| **Related Business Processes** | BP-08 |

---

### R-16-04: Verify Stock Before Emergency Orders

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Verify Stock Before Emergency Orders |
| **Description** | Check current stock levels, open PO inbound quantities, and network availability before placing emergency purchase orders to avoid unnecessary duplicate procurement. |
| **Business Importance** | Prevents over-purchasing during crisis response; considers network and inbound stock before new supplier orders. |
| **Related Functional Requirements** | FR-028, FR-053, FR-055 |
| **Related Business Processes** | BP-05, BP-21, BP-26 |

---

### R-16-05: Communicate Inbound ETA to Stakeholders

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Communicate Inbound ETA to Stakeholders |
| **Description** | Update and communicate expected arrival dates for inbound shipments to operations, customer service, and sales when supplier delivery schedules change. |
| **Business Importance** | Enables realistic customer and operational planning; reduces surprise stockouts despite open purchase orders. |
| **Related Functional Requirements** | FR-055, FR-079, FR-014 |
| **Related Business Processes** | BP-23, BP-06 |

---

### R-16-06: Review Expected Inbound for Receiving Coordination

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Review Expected Inbound for Receiving Coordination |
| **Description** | Review scheduled inbound deliveries and coordinate with warehouse receiving on timing, volume, and PO references for upcoming shipments. |
| **Business Importance** | Prepares receiving dock for efficient processing; reduces receipt delays and dock congestion. |
| **Related Functional Requirements** | FR-014 |
| **Related Business Processes** | BP-06 |

---

### R-16-07: Use Replenishment Reports for Daily Purchasing

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Use Replenishment Reports for Daily Purchasing |
| **Description** | Use replenishment-focused reports showing items below threshold, active alerts, and open requisitions to prioritize daily purchasing activity. |
| **Business Importance** | Consolidates decision information in one view; reduces time gathering data from multiple sources. |
| **Related Functional Requirements** | FR-074, FR-052 |
| **Related Business Processes** | BP-22, BP-21 |

---

## UR-17: Finance Manager / Accountant

**Business Purpose:** Align operational inventory records with financial books through valuation and reconciliation.

---

### R-17-01: Perform Month-End Inventory Reconciliation

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Perform Month-End Inventory Reconciliation |
| **Description** | Reconcile operational inventory quantities and values with general ledger accounts at period end; investigate and resolve variances between operational and financial records. |
| **Business Importance** | Ensures accurate balance sheet valuation; supports timely month-end close and audit readiness. |
| **Related Functional Requirements** | FR-089, FR-075 |
| **Related Business Processes** | BP-30 |

---

### R-17-02: Review Adjustment and Write-Off Documentation

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Review Adjustment and Write-Off Documentation |
| **Description** | Review adjustment and write-off records for financial substantiation including reason codes, quantities, values, and approval evidence before financial posting. |
| **Business Importance** | Prevents unsupported inventory reductions in financial records; satisfies audit evidence requirements for inventory changes. |
| **Related Functional Requirements** | FR-035, FR-036, FR-069 |
| **Related Business Processes** | BP-14, BP-15 |

---

### R-17-03: Extract Inventory Valuation Data

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Extract Inventory Valuation Data |
| **Description** | Extract inventory valuation summaries by product and location using operational quantities and agreed unit costs for financial reporting and substantiation. |
| **Business Importance** | Bridges operations and finance inventory records; reduces manual valuation compilation effort. |
| **Related Functional Requirements** | FR-075 |
| **Related Business Processes** | BP-30 |

---

### R-17-04: Analyze Shrinkage Financial Impact

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Analyze Shrinkage Financial Impact |
| **Description** | Analyze financial impact of shrinkage, write-offs, and count variances by period and location; challenge unexplained operational variances with inventory control and operations. |
| **Business Importance** | Quantifies inventory loss in financial terms; drives accountability for recurring shrinkage patterns. |
| **Related Functional Requirements** | FR-039, FR-069 |
| **Related Business Processes** | BP-15, BP-30 |

---

### R-17-05: Support Internal and External Audit

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Support Internal and External Audit |
| **Description** | Provide inventory valuation reports, adjustment logs, movement summaries, and reconciliation evidence to internal and external auditors during audit periods. |
| **Business Importance** | Enables efficient audit completion; demonstrates financial record support for inventory balances. |
| **Related Functional Requirements** | FR-087, FR-089, FR-069 |
| **Related Business Processes** | BP-30, BP-32 |

---

### R-17-06: Coordinate Supplier Credits for Receipt Discrepancies

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Coordinate Supplier Credits for Receipt Discrepancies |
| **Description** | Coordinate financial treatment of supplier credits and payment adjustments linked to resolved receipt discrepancies with purchasing and receiving teams. |
| **Business Importance** | Ensures financial records reflect supplier dispute outcomes; prevents payment for undelivered or rejected goods. |
| **Related Functional Requirements** | FR-016 |
| **Related Business Processes** | BP-08 |

---

### R-17-07: Review Obsolete and Slow-Moving Stock

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Review Obsolete and Slow-Moving Stock |
| **Description** | Participate in reviews of slow-moving and obsolete inventory identified by aging analysis; support clearance, transfer, or write-off financial planning. |
| **Business Importance** | Releases working capital trapped in dead stock; reduces carrying cost and obsolescence risk on the balance sheet. |
| **Related Functional Requirements** | FR-040, FR-070 |
| **Related Business Processes** | BP-14, BP-29 |

---

### R-17-08: Participate in Full Count Financial Substantiation

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Participate in Full Count Financial Substantiation |
| **Description** | Support full physical inventory count activities from a financial substantiation perspective; review count variance reports for material financial impact before adjustment posting. |
| **Business Importance** | Provides financial oversight of count results; ensures count adjustments are reflected accurately in financial close. |
| **Related Functional Requirements** | FR-032, FR-033, FR-071 |
| **Related Business Processes** | BP-12, BP-30 |

---

## UR-18: Internal Auditor

**Business Purpose:** Provide independent assurance that inventory controls are designed effectively and operating as intended.

---

### R-18-01: Test Inventory Control Effectiveness

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Test Inventory Control Effectiveness |
| **Description** | Design and execute control tests over inventory processes including receiving, counting, adjustments, transfers, and fulfillment; evaluate whether controls operate as designed. |
| **Business Importance** | Identifies control weaknesses before they result in fraud, error, or audit findings; supports clean internal and external audit outcomes. |
| **Related Functional Requirements** | FR-087, FR-088 |
| **Related Business Processes** | BP-32 |

---

### R-18-02: Sample Inventory Transactions

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Sample Inventory Transactions |
| **Description** | Select and review samples of inventory movements, adjustments, count variances, and approvals for compliance with policy and completeness of documentation. |
| **Business Importance** | Validates transaction integrity across the inventory lifecycle; detects unauthorized or undocumented changes. |
| **Related Functional Requirements** | FR-086, FR-029, FR-069 |
| **Related Business Processes** | BP-32, BP-14, BP-13 |

---

### R-18-03: Review User Activity and Audit Trail

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Review User Activity and Audit Trail |
| **Description** | Review user activity logs and immutable audit trails for inventory quantity changes including before/after balances, reason codes, users, and timestamps. |
| **Business Importance** | Enables traceability during investigations; demonstrates accountability for all material inventory actions. |
| **Related Functional Requirements** | FR-083, FR-086 |
| **Related Business Processes** | BP-32 |

---

### R-18-04: Investigate Control Weaknesses and Policy Breaches

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Investigate Control Weaknesses and Policy Breaches |
| **Description** | Investigate identified control incidents, policy breaches, and segregation-of-duties concerns; document findings and recommend corrective actions to management and the audit committee. |
| **Business Importance** | Drives remediation of systemic control failures; reduces repeat findings and fraud exposure. |
| **Related Functional Requirements** | FR-088, FR-084 |
| **Related Business Processes** | BP-32 |

---

### R-18-05: Review Count and Variance Records

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Review Count and Variance Records |
| **Description** | Review cycle count and full count results, variance investigations, and approval packages for compliance with count policy and segregation of duties between counter and approver. |
| **Business Importance** | Validates that accuracy programs produce trustworthy results; detects count process manipulation or self-approval. |
| **Related Functional Requirements** | FR-031, FR-033, FR-034, FR-071 |
| **Related Business Processes** | BP-11, BP-12, BP-13 |

---

### R-18-06: Export Audit Evidence Packages

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Export Audit Evidence Packages |
| **Description** | Run structured queries and export evidence packages covering transactions, adjustments, count records, and control compliance for audit committee and external auditor support. |
| **Business Importance** | Reduces audit preparation effort; demonstrates control effectiveness efficiently. |
| **Related Functional Requirements** | FR-087 |
| **Related Business Processes** | BP-32 |

---

### R-18-07: Support External Audit Preparation

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Support External Audit Preparation |
| **Description** | Coordinate internal evidence gathering and control documentation to support external auditor requirements during annual financial statement audit. |
| **Business Importance** | Accelerates external audit completion; reduces disruption to operations during audit fieldwork. |
| **Related Functional Requirements** | FR-087, FR-086 |
| **Related Business Processes** | BP-32, BP-30 |

---

## UR-19: External Auditor

**Business Purpose:** Independently verify inventory existence, valuation, and control effectiveness during the annual financial statement audit.

---

### R-19-01: Test Inventory Existence

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Test Inventory Existence |
| **Description** | Perform existence testing procedures including observation of physical counts, trace-from count to records, and trace-from records to supporting documentation for selected inventory samples. |
| **Business Importance** | Provides independent verification that recorded inventory quantities represent physically present goods; core audit assertion for balance sheet accuracy. |
| **Related Functional Requirements** | FR-032, FR-031, FR-071 |
| **Related Business Processes** | BP-12, BP-30 |

---

### R-19-02: Evaluate Inventory Valuation

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Evaluate Inventory Valuation |
| **Description** | Review inventory valuation methodology, unit costs, and extended values; test valuation calculations and assess obsolescence and write-down adequacy. |
| **Business Importance** | Validates that inventory is stated at appropriate value on financial statements; detects overstatement from obsolete or impaired stock. |
| **Related Functional Requirements** | FR-075, FR-089, FR-040 |
| **Related Business Processes** | BP-30 |

---

### R-19-03: Test Controls Over Inventory Movements

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Test Controls Over Inventory Movements |
| **Description** | Evaluate design and operating effectiveness of controls over receipts, transfers, adjustments, write-offs, and fulfillments through transaction sampling and walkthrough procedures. |
| **Business Importance** | Determines reliance on internal controls for substantive testing scope; identifies material control deficiencies requiring reporting. |
| **Related Functional Requirements** | FR-086, FR-087, FR-088 |
| **Related Business Processes** | BP-32 |

---

### R-19-04: Request and Review Audit Evidence

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Request and Review Audit Evidence |
| **Description** | Request inventory reports, count records, adjustment logs, movement histories, and reconciliation documentation from finance, inventory control, and operations personnel during the audit period. |
| **Business Importance** | Forms the evidentiary basis for audit opinion; incomplete evidence increases audit risk and qualification potential. |
| **Related Functional Requirements** | FR-087, FR-069, FR-071 |
| **Related Business Processes** | BP-32, BP-30 |

---

### R-19-05: Issue Audit Findings and Opinion

| Attribute | Description |
|-----------|-------------|
| **Responsibility Name** | Issue Audit Findings and Opinion |
| **Description** | Document identified material misstatements, control deficiencies, and inventory-related findings; incorporate conclusions into the overall financial statement audit opinion. |
| **Business Importance** | Provides independent assurance to investors, lenders, and regulators on financial statement reliability including inventory balances. |
| **Related Functional Requirements** | FR-087, FR-088 |
| **Related Business Processes** | BP-32, BP-30 |

---

## Responsibility Index Summary

| Role ID | Role Name | Responsibility Count |
|---------|-----------|---------------------|
| UR-01 | Chief Executive Officer (CEO) | 4 |
| UR-02 | Chief Operating Officer (COO) | 6 |
| UR-03 | Chief Financial Officer (CFO) | 5 |
| UR-04 | Operations Director | 10 |
| UR-05 | Inventory Controller | 11 |
| UR-06 | Warehouse Manager | 10 |
| UR-07 | Receiving Clerk | 6 |
| UR-08 | Warehouse Picker / Packer | 4 |
| UR-09 | Warehouse Staff | 4 |
| UR-10 | Regional / Store Manager | 6 |
| UR-11 | Sales Manager | 6 |
| UR-12 | Sales Representative | 6 |
| UR-13 | Customer Service Representative | 7 |
| UR-14 | Marketing Manager | 5 |
| UR-15 | Purchasing Manager | 9 |
| UR-16 | Buyer / Procurement Officer | 7 |
| UR-17 | Finance Manager / Accountant | 8 |
| UR-18 | Internal Auditor | 7 |
| UR-19 | External Auditor | 5 |
| **Total** | **19 roles** | **116 responsibilities** |

---

## Document Summary

This document defines **116 discrete business responsibilities** across **19 user roles** for the Inventory Management System. Each responsibility is traced to supporting functional requirements and related business processes, providing a foundation for user story validation, training design, acceptance testing, and organizational RACI development.

System permissions and access control mappings are intentionally excluded. Responsibilities describe *what* each role is accountable for in business terms; how the system enforces role boundaries is addressed in a separate access control design phase.

---

*End of Role Responsibilities Document*
