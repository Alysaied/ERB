# Business Assumptions: Inventory Management System

**Document Owner:** Business Analyst  
**Based On:** Business Vision Document, Project Scope Document, Stakeholder Analysis, SMART Business Objectives  
**Purpose:** Document the business beliefs and conditions that underpin the IMS initiative; identify risks if assumptions prove false  
**Scope:** Business assumptions only — no technical or implementation assumptions

---

## Assumption Categories Overview

| Category | Count | Focus Area |
|----------|-------|------------|
| Organizational & People | 6 | Staffing, skills, leadership support |
| Process & Operations | 7 | Current and future workflows |
| Data & Product Information | 5 | Master data quality and ownership |
| Supply Chain & External Parties | 5 | Suppliers, carriers, customers |
| Financial & Commercial | 5 | Cost, revenue, and financial alignment |
| Strategic & Scope | 5 | Business direction and boundaries |
| Change Management & Adoption | 5 | User readiness and behavior change |
| Governance & Compliance | 4 | Policies, controls, and audit |
| Timeline & Resources | 4 | Budget, schedule, and capacity |

**Total: 46 business assumptions**

---

## Category 1: Organizational & People

---

### BA-01

| Attribute | Detail |
|-----------|--------|
| **Assumption** | Executive leadership will remain committed to the IMS initiative for the full 18-month business vision period, providing visible sponsorship and removing organizational blockers when needed |
| **Reason** | The business vision and SMART objectives depend on sustained leadership support to drive adoption, enforce process change, and protect project priority against competing initiatives |
| **Risk if False** | Scope reduction, delayed decisions, poor user adoption, failure to retire manual processes, and inability to achieve P1 and P2 objectives |
| **Validation Method** | Confirm executive sponsor assignment and steering committee charter at project kickoff; review leadership attendance and decision turnaround at monthly steering meetings |

---

### BA-02

| Attribute | Detail |
|-----------|--------|
| **Assumption** | Warehouse and operations staff at primary locations are available to participate in process definition, training, and go-live activities without critical disruption to daily fulfillment |
| **Reason** | Operational users are essential for defining realistic workflows and adopting the system; their unavailability would delay rollout and undermine accuracy objectives |
| **Risk if False** | Rushed or incomplete training; go-live during peak season causing failure; workflows designed without frontline input leading to low adoption |
| **Validation Method** | Agree rollout calendar with Operations Director avoiding peak seasons; confirm staff allocation plan with Warehouse Managers 60 days before each location go-live |

---

### BA-03

| Attribute | Detail |
|-----------|--------|
| **Assumption** | An Inventory Controller role (or equivalent accountability) exists or will be assigned to own product master data, count programs, and accuracy targets |
| **Reason** | BO-02 (inventory accuracy) and BO-03 (standardized recording) require a dedicated business owner; without one, data quality degrades and no one is accountable for variances |
| **Risk if False** | Chronic inventory inaccuracy; inconsistent product data; count programs not executed; SMART accuracy objectives not achieved |
| **Validation Method** | Confirm role assignment and job description update with HR and Operations Director before Phase 1 go-live; verify named individual in project RACI |

---

### BA-04

| Attribute | Detail |
|-----------|--------|
| **Assumption** | Current staffing levels at primary warehouses are sufficient to perform inventory transactions in the new system without requiring additional headcount in the first 12 months |
| **Reason** | The business case assumes efficiency gains from the system, not new hires; additional labor cost would reduce ROI and delay approval |
| **Risk if False** | Overloaded warehouse staff revert to shortcuts and manual workarounds; transaction recording compliance (BO-03) falls below target; fulfillment delays increase |
| **Validation Method** | Conduct workload assessment with Warehouse Managers at month 3 post go-live; compare transaction volumes and processing times against pre-implementation baseline |

---

### BA-05

| Attribute | Detail |
|-----------|--------|
| **Assumption** | Purchasing and sales teams will designate process owners to participate in replenishment alert and availability visibility design |
| **Reason** | BO-13 (replenishment timeliness) and BO-16 (sales self-service availability) require cross-functional agreement on who acts on alerts and how sales accesses stock data |
| **Risk if False** | Low-stock alerts ignored; sales continues calling warehouse; replenishment and sales enablement objectives not met |
| **Validation Method** | Confirm named process owners from Purchasing Manager and Sales Manager at requirements sign-off; validate role responsibilities in updated department procedures |

---

### BA-06

| Attribute | Detail |
|-----------|--------|
| **Assumption** | Finance will assign a dedicated contact to support monthly inventory valuation reconciliation with operational records |
| **Reason** | BO-18 (valuation reliability) and BO-20 (month-end close) require ongoing collaboration between operations and finance; without a finance counterpart, reconciliation remains manual and delayed |
| **Risk if False** | Persistent valuation variance; delayed month-end close; finance continues distrusting operational inventory data |
| **Validation Method** | Confirm finance liaison assignment at project kickoff; establish monthly reconciliation meeting cadence; track variance trend from month 3 post go-live |

---

## Category 2: Process & Operations

---

### BA-07

| Attribute | Detail |
|-----------|--------|
| **Assumption** | Current receiving, picking, transfer, and adjustment processes are documentable and can be standardized across primary locations with manageable variation |
| **Reason** | The project scope assumes standardized movement recording (BO-03); highly divergent location practices would require location-specific exceptions and delay network-wide visibility |
| **Risk if False** | Inconsistent data across locations; extended rollout timeline; user confusion; inability to compare location performance |
| **Validation Method** | Conduct as-is process mapping workshops at each primary location during discovery; document variation gaps and secure Operations Director agreement on standard to-be process |

---

### BA-08

| Attribute | Detail |
|-----------|--------|
| **Assumption** | Physical inventory counts can be performed at each primary location at least monthly without shutting down operations |
| **Reason** | BO-02 (95% accuracy) depends on regular cycle counts; full shutdown counts are disruptive and costly |
| **Risk if False** | Accuracy targets missed; variances accumulate undetected; financial and operational records diverge further |
| **Validation Method** | Pilot cycle count program at first go-live location; measure operational disruption and accuracy improvement; confirm count schedule feasibility with Warehouse Managers |

---

### BA-09

| Attribute | Detail |
|-----------|--------|
| **Assumption** | Order fulfillment at primary locations follows a predictable pick-pack-ship sequence that can be supported by inventory reservation and deduction workflows |
| **Reason** | MVP scope includes order reservation, partial fulfillment, and pick confirmation; unstructured fulfillment would not map to system workflows |
| **Risk if False** | Orders shipped without reservation; stock overselling; fill rate objectives (BO-05) not achievable |
| **Validation Method** | Map current order-to-shipment process with Operations Director; confirm reservation point (at order entry vs. at pick) through workshop with sales and warehouse teams |

---

### BA-10

| Attribute | Detail |
|-----------|--------|
| **Assumption** | Inter-location stock transfers are already occurring and will continue, driven by operational need rather than ad-hoc emergency requests only |
| **Reason** | BO-14 (reduce cross-location imbalance) assumes transfers are a normal business practice; if transfers are rare or politically blocked, imbalance cannot be corrected |
| **Risk if False** | Stock remains trapped at overstocked locations while other locations stockout; network optimization objectives fail |
| **Validation Method** | Review 12-month history of inter-location transfer volumes; confirm transfer approval policy with Regional Managers and Operations Director |

---

### BA-11

| Attribute | Detail |
|-----------|--------|
| **Assumption** | Reason codes for adjustments (damage, shrinkage, correction, write-off) can be defined and enforced as mandatory business policy across all locations |
| **Reason** | BO-11 (shrinkage reduction) and BO-19 (audit trail) require meaningful reason codes; optional or vague codes undermine accountability |
| **Risk if False** | Adjustments made without justification; shrinkage root causes untraceable; audit and loss prevention objectives fail |
| **Validation Method** | Draft reason code list with Inventory Controller and Internal Auditor; approve via operations policy update; audit compliance monthly from month 3 post go-live |

---

### BA-12

| Attribute | Detail |
|-----------|--------|
| **Assumption** | The business operates during defined business hours with predictable daily transaction volumes that allow same-day processing of receipts, picks, and adjustments |
| **Reason** | Replenishment response (BO-13) and fulfillment cycle time (BO-06) assume transactions are processed within the business day; overnight batch-only processing would delay objectives |
| **Risk if False** | Stale inventory data during business hours; sales quotes based on outdated stock; fulfillment delays |
| **Validation Method** | Document current transaction processing windows per location; confirm with Warehouse Managers that same-day recording is operationally feasible |

---

### BA-13

| Attribute | Detail |
|-----------|--------|
| **Assumption** | Returns from customers represent a manageable volume that can be handled through basic return-to-stock or write-off processes without a dedicated returns module in the first 12 months |
| **Reason** | Project scope postpones full returns management; assuming low return volume avoids scope creep while still supporting core inventory accuracy |
| **Risk if False** | Return volume overwhelms manual process; returned stock not recorded; accuracy and shrinkage metrics distorted |
| **Validation Method** | Analyze 12-month return volume and value with Customer Service and Finance; confirm return handling approach with Operations Director; revisit if returns exceed 5% of outbound volume |

---

## Category 3: Data & Product Information

---

### BA-14

| Attribute | Detail |
|-----------|--------|
| **Assumption** | A usable product catalog exists — or can be compiled — containing SKU, name, unit of measure, and category for all active products within 60 days of project start |
| **Reason** | MVP requires product master records; without a clean starting catalog, go-live cannot proceed and initial stock loading will be error-prone |
| **Risk if False** | Delayed go-live; duplicate or missing SKUs; incorrect units of measure causing fulfillment and purchasing errors |
| **Validation Method** | Conduct product data audit at project start; assign Inventory Controller to deliver cleansed catalog; sign-off by Purchasing and Operations before data load |

---

### BA-15

| Attribute | Detail |
|-----------|--------|
| **Assumption** | Products can be uniquely identified by SKU (or equivalent identifier) across all locations, sales channels, and supplier documents without widespread duplication |
| **Reason** | Single product identity is foundational to network-wide visibility; duplicate SKUs would fragment stock view and cause fulfillment errors |
| **Risk if False** | Same product tracked under multiple codes; inflated SKU count; unreliable availability and replenishment data |
| **Validation Method** | SKU deduplication review during product data audit; confirm identifier standards with Inventory Controller and Purchasing; validate against supplier catalogs |

---

### BA-16

| Attribute | Detail |
|-----------|--------|
| **Assumption** | Opening stock balances for each primary location can be established through a physical count or verified audit within 30 days before each location's go-live |
| **Reason** | BO-02 (accuracy) requires starting from a known baseline; loading unverified opening balances would embed existing errors into the new system |
| **Risk if False** | System starts with inaccurate data; users lose trust immediately; accuracy objectives unachievable from day one |
| **Validation Method** | Schedule pre-go-live physical count per location; require Operations Director sign-off on opening balances; document variances found during opening count |

---

### BA-17

| Attribute | Detail |
|-----------|--------|
| **Assumption** | Reorder levels and minimum stock thresholds can be defined for priority (A-class) products based on historical consumption and supplier lead times within the first 6 months |
| **Reason** | BO-07 (stockout reduction) and BO-13 (replenishment timeliness) depend on meaningful thresholds; without them, alerts are either absent or ignored as noise |
| **Risk if False** | Low-stock alerts either never trigger or fire constantly; purchasing ignores alerts; stockout objectives not met |
| **Validation Method** | Inventory Controller to define initial thresholds for A-class SKUs by month 3; review alert accuracy with Purchasing Manager monthly; refine thresholds quarterly |

---

### BA-18

| Attribute | Detail |
|-----------|--------|
| **Assumption** | Product categories and ABC classification (priority grouping) can be agreed upon by operations, purchasing, and sales to support reporting and alert prioritization |
| **Reason** | BO-07 targets priority products specifically; without agreed classification, stockout reduction efforts are unfocused |
| **Risk if False** | All products treated equally; high-value SKUs stockout while effort is wasted on slow movers; misaligned priorities between departments |
| **Validation Method** | Facilitate ABC classification workshop with Operations, Purchasing, and Sales; publish agreed classification; review and update semi-annually |

---

## Category 4: Supply Chain & External Parties

---

### BA-19

| Attribute | Detail |
|-----------|--------|
| **Assumption** | Key suppliers will continue to deliver within current lead time ranges and will not materially change terms, minimum order quantities, or product availability during the first 18 months |
| **Reason** | Replenishment timing (BO-13) and stockout reduction (BO-07) assume stable supply; sudden lead time increases would invalidate reorder parameters |
| **Risk if False** | Stockouts despite correct system alerts; excess safety stock built as reaction; replenishment objectives missed through no fault of internal process |
| **Validation Method** | Review supplier lead time performance over prior 12 months with Purchasing Manager; monitor lead time variance monthly; flag suppliers with >20% lead time change for threshold review |

---

### BA-20

| Attribute | Detail |
|-----------|--------|
| **Assumption** | Suppliers will continue to provide delivery documentation (packing lists, delivery notes) that can be matched against purchase orders during receiving |
| **Reason** | Receiving workflow depends on matching inbound goods to expected orders; without supplier documentation, receipt verification and discrepancy recording cannot function |
| **Risk if False** | Receiving delays; unmatched receipts; inaccurate inbound recording; disputes with suppliers unresolved |
| **Validation Method** | Confirm documentation standards with top 10 suppliers by volume; document exceptions; include delivery document requirement in supplier terms review |

---

### BA-21

| Attribute | Detail |
|-----------|--------|
| **Assumption** | Carrier and logistics partners will continue to provide shipment tracking information that can be recorded against outbound orders, even if manually in the MVP phase |
| **Reason** | BO-15 (on-time delivery) and customer service objectives require shipment status; manual recording is acceptable in MVP per project scope |
| **Risk if False** | Customer service cannot answer delivery inquiries; on-time delivery cannot be measured; customer satisfaction objectives at risk |
| **Validation Method** | Confirm tracking information availability with current carriers; document manual recording process with Warehouse Manager; track percentage of shipments with tracking recorded |

---

### BA-22

| Attribute | Detail |
|-----------|--------|
| **Assumption** | B2B and B2C customers will accept partial shipments and revised delivery dates when communicated proactively, without significant churn increase |
| **Reason** | BO-08 (reduce cancellations) and partial fulfillment support assume customers tolerate partial delivery; if customers cancel on any partial, fill rate improvements may not translate to revenue retention |
| **Risk if False** | Partial fulfillment increases cancellations rather than reducing them; customer satisfaction declines despite operational improvements |
| **Validation Method** | Review historical partial shipment acceptance and cancellation rates with Customer Service; survey top 20 B2B accounts on partial delivery policy; monitor cancellation trend post go-live |

---

### BA-23

| Attribute | Detail |
|-----------|--------|
| **Assumption** | Sales channel partners and marketplaces are not expected to require real-time inventory feed integration within the first 12 months |
| **Reason** | Project scope postpones marketplace integration; assuming no immediate channel partner pressure avoids scope creep during MVP stabilization |
| **Risk if False** | Channel partners penalize or delist company for overselling; revenue from partner channels at risk; forced early integration diverts focus from core accuracy objectives |
| **Validation Method** | Confirm channel partner SLA requirements with Sales Manager and Marketing; document any partner with stock feed requirements; escalate to Product Owner if integration needed before month 12 |

---

## Category 5: Financial & Commercial

---

### BA-24

| Attribute | Detail |
|-----------|--------|
| **Assumption** | The business has approved budget for the IMS initiative covering the full 18-month business vision period, including change management, training, and ongoing operational support |
| **Reason** | All SMART objectives and phased rollout depend on sustained funding; mid-project budget cuts would force scope reduction and objective failure |
| **Risk if False** | Project paused or descoped; partial rollout leaves locations on mixed processes; ROI not realized |
| **Validation Method** | Confirm approved budget and funding release schedule with Project Sponsor and CFO at kickoff; review budget consumption at quarterly steering meetings |

---

### BA-25

| Attribute | Detail |
|-----------|--------|
| **Assumption** | Inventory carrying cost and shrinkage currently represent a material portion of operating expense, justifying investment in improved control |
| **Reason** | The business case depends on working capital and margin improvement (BO-09, BO-10, BO-11); if current losses are immaterial, executive motivation to enforce change may be low |
| **Risk if False** | Low executive urgency; tolerance for continued manual processes; adoption objectives (BO-21, BO-22) not enforced |
| **Validation Method** | Quantify current shrinkage value, write-offs, excess inventory, and emergency procurement spend with Finance; present business case figures to steering committee for validation |

---

### BA-26

| Attribute | Detail |
|-----------|--------|
| **Assumption** | Product unit costs or valuation rates are available or can be assigned for inventory value reporting without requiring full cost accounting integration in the first 12 months |
| **Reason** | BO-18 (valuation reliability) and executive dashboards require inventory value; full costing integration is out of scope per project scope document |
| **Risk if False** | Valuation reports unusable; finance cannot reconcile; CFO loses confidence in system; financial objectives deferred indefinitely |
| **Validation Method** | Confirm available cost data sources with Finance Manager; agree interim valuation method (e.g., standard cost or last purchase price); validate against GL sample at month 3 |

---

### BA-27

| Attribute | Detail |
|-----------|--------|
| **Assumption** | Revenue growth will continue at a moderate pace and will not require immediate onboarding of new warehouses, product lines, or sales channels during the first 6 months post go-live |
| **Reason** | MVP focuses on primary locations only; simultaneous growth and stabilization would split operational focus and risk adoption at existing sites |
| **Risk if False** | Resources diverted to new locations before existing ones stabilize; accuracy and adoption objectives fail at primary sites; growth proceeds without inventory control |
| **Validation Method** | Review growth plan with CEO and COO; align rollout calendar to avoid conflict with planned expansions; confirm no new location opens within 6 months of primary go-live without executive exception |

---

### BA-28

| Attribute | Detail |
|-----------|--------|
| **Assumption** | Sales pricing, discounts, and promotions are managed outside the IMS and will not require inventory system involvement beyond stock readiness checks in the first 12 months |
| **Reason** | Project scope excludes pricing and promotions engine; BO-24 (promotional readiness) only requires stock visibility, not pricing integration |
| **Risk if False** | Sales and marketing expect IMS to manage promotional pricing; scope conflict; delayed delivery of core inventory features |
| **Validation Method** | Confirm scope boundary with Sales Manager and Marketing Manager at kickoff; document promotional readiness process using stock reports only |

---

## Category 6: Strategic & Scope

---

### BA-29

| Attribute | Detail |
|-----------|--------|
| **Assumption** | The company's core business model will remain distribution and retail operations; the business will not pivot to in-house manufacturing within the 18-month vision period |
| **Reason** | Project scope explicitly excludes manufacturing and MRP; a business model change would invalidate scope, stakeholder map, and objectives |
| **Risk if False** | Fundamental requirements change; BOM, work orders, and production scheduling needed; project requires restart or parallel initiative |
| **Validation Method** | Confirm strategic plan with CEO and COO at project kickoff; review at annual strategic planning session; escalate any manufacturing exploration to steering committee |

---

### BA-30

| Attribute | Detail |
|-----------|--------|
| **Assumption** | Existing finance, sales, and HR systems will remain in place and the IMS will not be expected to replace ERP, CRM, or accounting functions within 18 months |
| **Reason** | Project scope defines IMS as inventory capability, not enterprise platform replacement; scope creep into ERP territory would fail |
| **Risk if False** | Stakeholders withhold adoption waiting for "full ERP"; conflicting system boundaries; finance and sales resist using IMS |
| **Validation Method** | Publish system boundary document to all department heads; obtain signed acknowledgment from CFO, Sales Manager, and COO; reinforce at steering meetings |

---

### BA-31

| Attribute | Detail |
|-----------|--------|
| **Assumption** | Primary locations (warehouses and stores targeted for MVP) represent at least 80% of total inventory volume and order fulfillment activity |
| **Reason** | MVP is limited to primary locations; if excluded locations handle significant volume, network-wide objectives (BO-01, BO-14) cannot be achieved |
| **Risk if False** | Majority of stock and orders remain outside system; business continues operating with partial visibility; executive dashboards misleading |
| **Validation Method** | Analyze inventory value and order volume by location with Operations Director; confirm primary location list covers ≥ 80% of volume; document excluded locations and timeline for inclusion |

---

### BA-32

| Attribute | Detail |
|-----------|--------|
| **Assumption** | No new regulatory requirements (e.g., product traceability, serialization, hazardous materials reporting) will be imposed on the business within the first 18 months |
| **Reason** | Project scope excludes industry-specific compliance modules; unexpected regulation would require scope change and additional investment |
| **Risk if False** | Compliance gap; potential fines or market access loss; project must absorb unplanned compliance features |
| **Validation Method** | Review regulatory landscape with legal/compliance contact at kickoff; monitor industry regulatory announcements quarterly; reassess if business enters new product categories |

---

### BA-33

| Attribute | Detail |
|-----------|--------|
| **Assumption** | The business will not undergo merger, acquisition, or divestiture of inventory-holding entities during the first 12 months of implementation |
| **Reason** | Organizational change during implementation disrupts process standardization, data migration, and user adoption |
| **Risk if False** | Duplicate systems; conflicting processes; data migration complexity; rollout paused or restarted |
| **Validation Method** | Confirm M&A pipeline status with CEO and CFO at kickoff; include M&A clause in steering committee terms of reference for immediate escalation |

---

## Category 7: Change Management & Adoption

---

### BA-34

| Attribute | Detail |
|-----------|--------|
| **Assumption** | Warehouse and operations staff are willing to change from current manual and informal practices to system-mandated recording discipline |
| **Reason** | BO-03 (100% movement recording) and BO-22 (retire parallel tools) require behavioral change; resistance would preserve old workarounds |
| **Risk if False** | Dual systems persist; data remains unreliable; adoption objectives fail; investment wasted |
| **Validation Method** | Conduct change readiness assessment survey before go-live; monitor parallel tool audit (BO-22); track user adoption rate (BO-21) weekly in first 3 months |

---

### BA-35

| Attribute | Detail |
|-----------|--------|
| **Assumption** | Management will enforce compliance with new inventory processes and will not tolerate continued use of spreadsheets or offline tracking after the 6-month transition period |
| **Reason** | BO-22 depends on management enforcement; without consequences for non-compliance, staff revert to familiar tools |
| **Risk if False** | Parallel tracking persists indefinitely; system data incomplete; accuracy and visibility objectives unachievable |
| **Validation Method** | Operations Director to issue compliance policy before go-live; conduct parallel tool audit at months 3 and 6; report non-compliance at steering committee |

---

### BA-36

| Attribute | Detail |
|-----------|--------|
| **Assumption** | Training can be delivered to all target user roles in each location within 2 weeks before go-live without exceeding practical classroom and floor-training capacity |
| **Reason** | BO-21 (90% adoption) requires users to be competent at go-live; insufficient training causes errors and rejection |
| **Risk if False** | High error rates at go-live; user frustration; inventory accuracy drops before it improves; negative first impression |
| **Validation Method** | Develop training plan with headcount and schedule per location; pilot training at first location; collect training effectiveness feedback; adjust before subsequent rollouts |

---

### BA-37

| Attribute | Detail |
|-----------|--------|
| **Assumption** | Sales and customer service teams will shift from calling warehouses for stock checks to using system availability views within 30 days of being granted access |
| **Reason** | BO-16 (sales self-service) and BO-17 (CS resolution time) depend on changed behavior; continued phone-based checks undermine efficiency objectives |
| **Risk if False** | Warehouse distraction continues; sales availability objective not met; no measurable efficiency gain for either team |
| **Validation Method** | Track system availability lookups by sales and CS users; compare against warehouse inquiry log; review at month 1 and month 3 post access grant |

---

### BA-38

| Attribute | Detail |
|-----------|--------|
| **Assumption** | Union or labor agreements, if applicable, do not restrict changes to work procedures, performance measurement, or transaction recording requirements introduced by the IMS |
| **Reason** | Process standardization and accountability (BO-11, BO-19) may change how performance is measured; labor restrictions could block enforcement |
| **Risk if False** | Cannot enforce mandatory recording or reason codes; accountability objectives fail; legal dispute risk |
| **Validation Method** | Review with HR and legal before process policy changes; confirm no contractual barriers at project kickoff; engage union representatives early if applicable |

---

## Category 8: Governance & Compliance

---

### BA-39

| Attribute | Detail |
|-----------|--------|
| **Assumption** | Existing company policies on inventory adjustments, write-offs, and transfer approvals can be updated to align with system-enforced approval workflows |
| **Reason** | BO-19 (audit trail) and BO-11 (shrinkage) require policy-backed approval chains; system-only controls without policy support are bypassed |
| **Risk if False** | Users circumvent approval workflows; unauthorized adjustments continue; audit findings and shrinkage objectives fail |
| **Validation Method** | Review current inventory policies with Internal Auditor; draft updated policies before go-live; obtain COO sign-off; audit compliance quarterly |

---

### BA-40

| Attribute | Detail |
|-----------|--------|
| **Assumption** | Segregation of duties can be defined and applied — e.g., counters cannot approve their own variances, receivers cannot approve their own discrepancies |
| **Reason** | Internal and external audit expectations require separation of recording and approval roles; without it, control objectives (BO-19) fail audit testing |
| **Risk if False** | Audit findings; fraud and error risk unmitigated; external auditor qualifies opinion on inventory controls |
| **Validation Method** | Define segregation matrix with Internal Auditor; configure role permissions accordingly; test control design before go-live; include in quarterly internal audit sample |

---

### BA-41

| Attribute | Detail |
|-----------|--------|
| **Assumption** | The business does not currently operate under formal regulatory inventory reporting obligations that would require specialized compliance features at launch |
| **Reason** | Scope excludes regulatory modules; if obligations exist, launch could be non-compliant |
| **Risk if False** | Regulatory non-compliance; fines; forced scope expansion; delayed go-live |
| **Validation Method** | Confirm with legal/compliance and External Auditor at kickoff; document any applicable obligations; escalate if compliance features are required |

---

### BA-42

| Attribute | Detail |
|-----------|--------|
| **Assumption** | Data retention and record-keeping requirements for inventory transactions can be met through system audit logs and reports without separate manual archiving in the first 18 months |
| **Reason** | Audit trail (BO-19) and external audit support assume retrievable history; if retention rules exceed system capability, manual archiving reintroduces inefficiency |
| **Risk if False** | Audit evidence gaps; inability to support tax or legal inquiries; manual archive workload |
| **Validation Method** | Confirm retention period requirements with Internal Auditor and legal; validate report and log export capability meets minimum retention at UAT |

---

## Category 9: Timeline & Resources

---

### BA-43

| Attribute | Detail |
|-----------|--------|
| **Assumption** | Primary locations can be onboarded sequentially — not all simultaneously — over a 6-month rollout window following first location go-live |
| **Reason** | Sequential rollout allows lessons learned to improve subsequent deployments; simultaneous rollout would overwhelm support and training capacity |
| **Risk if False** | Support team overwhelmed; quality of each deployment degrades; adoption and accuracy objectives fail at multiple sites simultaneously |
| **Validation Method** | Confirm rollout sequence and 4–6 week gap between location go-lives with Operations Director; review lessons learned after first location before scheduling next |

---

### BA-44

| Attribute | Detail |
|-----------|--------|
| **Assumption** | Business subject matter experts (Inventory Controller, Warehouse Managers, Purchasing Manager, Sales Manager) can allocate approximately 20% of their time to the project during discovery, UAT, and rollout phases |
| **Reason** | Requirements quality, UAT, and rollout support depend on SME participation; zero availability would produce unusable requirements and untested workflows |
| **Risk if False** | Poor requirements; UAT skipped or superficial; go-live issues discovered in production; rework and delay |
| **Validation Method** | Secure SME time commitment in writing from department heads at kickoff; track attendance at workshops and UAT sessions; escalate absences to Project Sponsor |

---

### BA-45

| Attribute | Detail |
|-----------|--------|
| **Assumption** | Baseline measurements for SMART objectives (accuracy, fill rate, cycle time, shrinkage, etc.) can be established from existing records or a 30–60 day pre-go-live measurement period |
| **Reason** | All SMART objectives are measured as improvement from baseline; without baseline, success cannot be demonstrated and ROI is unprovable |
| **Risk if False** | Cannot prove business value; steering committee loses confidence; continued investment unjustified |
| **Validation Method** | Initiate baseline data collection project at month -2 before go-live; document data sources and gaps; agree proxy measures with Business Analyst where historical data is incomplete |

---

### BA-46

| Attribute | Detail |
|-----------|--------|
| **Assumption** | The first primary location selected for go-live is representative of others and is not an outlier in size, complexity, or process maturity |
| **Reason** | Pilot location lessons drive rollout design; an outlier pilot would produce non-transferable configuration and training materials |
| **Risk if False** | Subsequent locations require significant rework; rollout timeline extends; configuration not scalable to network |
| **Validation Method** | Score each primary location on volume, SKU count, staff experience, and process maturity; select median-complexity site; validate representativeness with Operations Director |

---

## Assumption Risk Heat Map

| Risk Level | Assumption IDs | Count |
|------------|----------------|-------|
| **Critical** — Project success depends on these; validate before kickoff | BA-01, BA-03, BA-14, BA-16, BA-24, BA-29, BA-30, BA-31, BA-34, BA-35 | 10 |
| **High** — Significant objective impact if false; validate during discovery | BA-07, BA-09, BA-17, BA-19, BA-25, BA-26, BA-36, BA-39, BA-40, BA-43, BA-45, BA-46 | 12 |
| **Medium** — Manageable with mitigation; monitor during rollout | BA-02, BA-04, BA-05, BA-08, BA-10, BA-11, BA-12, BA-15, BA-18, BA-20, BA-21, BA-27, BA-32, BA-33, BA-37, BA-38, BA-44 | 17 |
| **Low** — Limited impact or easily adapted; validate as needed | BA-06, BA-13, BA-22, BA-23, BA-28, BA-41, BA-42 | 7 |

---

## Validation Schedule

| Phase | When | Assumptions to Validate |
|-------|------|------------------------|
| **Pre-Kickoff** | Before project approval | BA-24, BA-25, BA-27, BA-29, BA-30, BA-31, BA-32, BA-33 |
| **Discovery** | Weeks 1–8 | BA-01, BA-03, BA-05, BA-06, BA-07, BA-14, BA-15, BA-18, BA-19, BA-20, BA-26, BA-28, BA-38, BA-39, BA-40, BA-41, BA-44, BA-45, BA-46 |
| **Pre-Go-Live (per location)** | 30–60 days before | BA-02, BA-08, BA-09, BA-12, BA-16, BA-17, BA-36, BA-43 |
| **Post-Go-Live** | Months 1–6 | BA-04, BA-10, BA-11, BA-13, BA-21, BA-22, BA-34, BA-35, BA-37 |
| **Ongoing** | Monthly / quarterly | BA-19, BA-23, BA-42; reassess BA-27, BA-32, BA-33 at steering reviews |

---

## Assumption-to-Objective Dependency

| If This Assumption Fails | These Objectives Are at Risk |
|------------------------|------------------------------|
| BA-03, BA-14, BA-16 (data ownership & quality) | BO-01, BO-02, BO-03, BO-19 |
| BA-34, BA-35, BA-36 (adoption & change) | BO-03, BO-04, BO-21, BO-22 |
| BA-09, BA-12 (fulfillment process) | BO-05, BO-06, BO-08 |
| BA-17, BA-19 (replenishment & supply) | BO-07, BO-12, BO-13 |
| BA-10, BA-18 (network balance) | BO-14 |
| BA-26, BA-06 (finance alignment) | BO-18, BO-20 |
| BA-37 (sales behavior change) | BO-16, BO-17 |
| BA-01, BA-27 (leadership & growth) | BO-23, BO-24 |

---

## Document Summary

This document captures **46 business assumptions** across nine categories that underpin the Inventory Management System initiative. These assumptions represent beliefs about organizational readiness, process maturity, data quality, external party behavior, financial conditions, strategic direction, change capacity, governance, and resource availability.

**10 assumptions are rated Critical** and must be validated before or at project kickoff to avoid fundamental project failure. **12 are High risk** and should be validated during the discovery phase. Ongoing monitoring is required for supply chain, adoption, and strategic assumptions throughout the 18-month business vision.

If any critical assumption proves false, the Business Analyst should raise an immediate issue to the Project Sponsor with impact assessment against SMART objectives and recommended mitigation or scope adjustment.

---

*End of Business Assumptions Document*
