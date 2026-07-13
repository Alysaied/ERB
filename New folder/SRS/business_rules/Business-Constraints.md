# Business Constraints Specification
## Inventory Management System

---

## Document Information

| Attribute | Detail |
|-----------|--------|
| **Document ID** | SRS-BC-001 |
| **Document Title** | Business Constraints — Inventory Management System |
| **Version** | 1.0 |
| **Status** | Draft |
| **Document Owner** | Senior Business Analyst |
| **Source Documents** | BRD-IMS-001 (Section 18), Business Constraints Discovery Artifact |
| **Date** | July 5, 2026 |
| **Scope** | Business and operational constraints only — not technical architecture, infrastructure, or implementation design |

### Purpose

This document identifies the **38 business constraints** that bound how the Inventory Management System initiative may be delivered and operated. Constraints are fixed business conditions — not optional preferences. Each constraint is expressed in operational terms: what the organization can and cannot do while running inventory management as a business capability.

### Constraint Categories

| Prefix | Category | Count |
|--------|----------|-------|
| BC | Budget | 6 |
| TC | Time | 6 |
| LC | Legal | 5 |
| OC | Operational | 8 |
| ORC | Organizational | 7 |
| TEC | Technology — Business Level | 6 |

### Severity Classification

| Severity | Constraints |
|----------|-------------|
| **Blocking** | BC-01, TC-02, OC-01, ORC-07 |
| **High** | BC-02, BC-05, TC-01, TC-03, TC-04, ORC-01, ORC-03, ORC-05, TEC-01, TEC-04 |
| **Medium** | BC-03, BC-04, BC-06, TC-05, TC-06, LC-01, LC-02, LC-03, OC-02, OC-04, OC-07, OC-08, ORC-02, ORC-04, ORC-06, TEC-02, TEC-05, TEC-06 |
| **Low** | LC-04, LC-05, OC-03, OC-05, OC-06 |

---

## 1. Budget Constraints

### BC-01: Fixed Total Initiative Budget

| Attribute | Detail |
|-----------|--------|
| **Constraint ID** | BC-01 |
| **Description** | The IMS initiative must be delivered within a fixed total budget approved by executive leadership, covering software, services, training, change management, and first-year operational support. No additional funding is guaranteed if overruns occur. |
| **Business Justification** | Inventory improvement must demonstrate return within approved capital and operating investment limits. Executive leadership has committed a defined envelope tied to business case ROI — not an open-ended transformation program. |
| **Affected Business Processes** | All processes (BP-01 – BP-32); particularly BP-29 (Performance Reporting), BP-31 (Promotional Readiness), and Phase 2/3 processes deferred by scope prioritization |
| **Consequences if Violated** | Scope reduction or project pause; P1 objectives (BO-01, BO-03, BO-19) at risk; Phase 2/3 capabilities (replenishment automation, financial alignment, network rebalancing) indefinitely deferred; stakeholder trust in program governance erodes |

---

### BC-02: No Additional Warehouse Headcount Budget

| Attribute | Detail |
|-----------|--------|
| **Constraint ID** | BC-02 |
| **Description** | The business case does not include budget for additional warehouse or inventory control headcount in the first 12 months. Efficiency must come from improved processes and system support, not new hires. |
| **Business Justification** | The initiative is funded as a productivity and control investment, not a staffing expansion. Leadership expects existing teams to operate more effectively with better visibility and standardized workflows. |
| **Affected Business Processes** | BP-07 (Goods Receipt), BP-09 (Put-Away), BP-11 (Cycle Counting), BP-18 (Pick, Pack & Ship), BP-21 (Low-Stock Alert Review), BP-30 (Financial Reconciliation) |
| **Consequences if Violated** | Unfunded headcount creates budget overrun (BC-01 conflict); existing staff overwhelmed during rollout; adoption fails (BO-21); manual parallel tools persist (BO-22); accuracy and movement recording objectives (BO-02, BO-03) not sustained |

---

### BC-03: Capital Expenditure vs. Operating Expenditure Limits

| Attribute | Detail |
|-----------|--------|
| **Constraint ID** | BC-03 |
| **Description** | Finance has defined separate caps for capital expenditure (licenses, implementation) and operating expenditure (subscriptions, support, training). Spending cannot be reclassified between categories without CFO approval. |
| **Business Justification** | Corporate financial policy requires predictable classification of investment versus recurring cost for balance-sheet and budget planning. IMS spending must fit established fiscal governance. |
| **Affected Business Processes** | BP-05 (Purchase Order Placement), BP-22 (Replenishment Planning), BP-30 (Financial Reconciliation) — indirect; primarily affects procurement timing of delivery activities |
| **Consequences if Violated** | Delivery delayed to next fiscal period; training or go-live support deferred; misaligned spend blocks vendor payment; project timeline slips against TC-02 and TC-05 milestones |

---

### BC-04: Training and Change Management Budget Ceiling

| Attribute | Detail |
|-----------|--------|
| **Constraint ID** | BC-04 |
| **Description** | A fixed budget is allocated for training, communications, and change management. This budget cannot be reallocated from development or licensing budgets. |
| **Business Justification** | Change investment is necessary but bounded. Leadership requires demonstrable efficiency in rollout — scalable training models rather than unlimited per-location bespoke programs. |
| **Affected Business Processes** | All operational processes at rollout; especially BP-07, BP-11, BP-14, BP-18, BP-24 where floor adoption is critical |
| **Consequences if Violated** | Incomplete role training; location managers reject standardized processes (BO-03); user adoption below 90% (BO-21); parallel spreadsheets and paper logs continue (BO-22); rework and support costs increase without budget to absorb them |

---

### BC-05: No Budget for External System Replacement

| Attribute | Detail |
|-----------|--------|
| **Constraint ID** | BC-05 |
| **Description** | The IMS budget does not fund replacement of finance, sales, HR, or ERP systems. IMS must operate within the current enterprise application landscape. |
| **Business Justification** | IMS addresses inventory control as a targeted capability gap — not a full enterprise platform replacement. Finance, sales, and HR systems remain authoritative in their domains. |
| **Affected Business Processes** | BP-05 (Purchase Order Placement), BP-16 (Order Availability), BP-30 (Financial Reconciliation), BP-31 (Promotional Readiness) |
| **Consequences if Violated** | Scope creep into ERP/CRM territory; stakeholder resistance from system owners; delivery failure on inventory-specific objectives; duplicated master data across systems; BO-18 and BO-20 remain unachievable without agreed interim reconciliation |

---

### BC-06: Ongoing Operational Cost Limit

| Attribute | Detail |
|-----------|--------|
| **Constraint ID** | BC-06 |
| **Description** | Annual recurring cost for licenses, support, and maintenance after go-live must remain within a CFO-approved operating budget threshold, typically capped relative to current inventory carrying cost. |
| **Business Justification** | Sustainable inventory management must not impose recurring cost that exceeds the economic value of improved control. Ongoing spend must be defensible against working-capital and carrying-cost benefits. |
| **Affected Business Processes** | BP-02 (Location Setup) — future location onboarding; BP-29 (Performance Reporting) — executive visibility scope |
| **Consequences if Violated** | New locations cannot be onboarded without separate approval; feature tiers or user counts restricted; network-wide rollout (TC-03) stalls; long-term scalability of BO-01 and BO-14 constrained |

---

## 2. Time Constraints

### TC-01: 18-Month Business Vision Horizon

| Attribute | Detail |
|-----------|--------|
| **Constraint ID** | TC-01 |
| **Description** | All SMART business objectives and phased outcomes must be achievable within 18 months of project initiation, aligned with the short-term business vision. |
| **Business Justification** | Leadership committed to measurable inventory improvement within a defined planning horizon. Beyond 18 months, priorities may shift and funding is not assured. |
| **Affected Business Processes** | All processes; Phase 3 processes especially BP-26 (Network Rebalancing), BP-29 (KPI Reporting), BP-30 (Financial Reconciliation), BP-31 (Promotional Readiness) |
| **Consequences if Violated** | Objectives BO-09, BO-10, BO-18, BO-20, BO-23, BO-24 measured as failed despite incomplete delivery; steering committee loses confidence; initiative descoped or restarted |

---

### TC-02: MVP Delivery Within 6 Months

| Attribute | Detail |
|-----------|--------|
| **Constraint ID** | TC-02 |
| **Description** | Minimum Viable Product must be live at the first primary location within 6 months of project kickoff to meet Phase 1 vision and P1 SMART objectives. |
| **Business Justification** | Early credible control is the strategic intent of Phase 1. Delayed go-live prolongs stockouts, inaccurate records, and fulfillment failures that the initiative was created to resolve. |
| **Affected Business Processes** | BP-01 – BP-18, BP-24 – BP-25, BP-29 (core reports), BP-32 (audit trail) — MVP process set |
| **Consequences if Violated** | P1 objectives missed: trusted view (BO-01), movement recording (BO-03), audit trail (BO-19), sales self-service (BO-16), adoption (BO-21), manual tool retirement (BO-22); executive sponsorship weakens; business continues absorbing current-state losses |

---

### TC-03: Sequential Location Rollout Window

| Attribute | Detail |
|-----------|--------|
| **Constraint ID** | TC-03 |
| **Description** | Primary locations must be onboarded sequentially over approximately 6 months following first go-live, with a minimum 4-week gap between deployments — not simultaneous network-wide cutover. |
| **Business Justification** | Support capacity, change absorption, and lessons-learned application require controlled rollout. Simultaneous deployment would overwhelm operations and SMEs (ORC-01). |
| **Affected Business Processes** | BP-02 (Location Setup), BP-10 (Status Monitoring), BP-24 – BP-26 (Network Balance), BP-29 (Reporting) |
| **Consequences if Violated** | Inconsistent processes across locations persist (BO-03); network visibility incomplete until ~month 12 (BO-01); cross-location imbalance correction delayed (BO-14); hypercare support fails; accuracy and adoption vary by site |

---

### TC-04: Peak Season Blackout Periods

| Attribute | Detail |
|-----------|--------|
| **Constraint ID** | TC-04 |
| **Description** | Go-live, major upgrades, and intensive training cannot occur during defined peak business periods (e.g., holiday season, fiscal year-end, major promotional events) at each location. |
| **Business Justification** | Peak periods generate disproportionate revenue and customer commitments. Operational disruption during peak directly damages fill rate, on-time delivery, and brand reputation. |
| **Affected Business Processes** | BP-16 – BP-19 (Order Fulfillment), BP-18 (Pick, Pack & Ship), BP-31 (Promotional Readiness), BP-07 (Receiving) |
| **Consequences if Violated** | Fill rate and on-time delivery drop (BO-05, BO-15); stock-related cancellations increase (BO-08); customer complaints and revenue at risk; rollout calendar slips 3–6 months; staff cannot complete training before peak |

---

### TC-05: SMART Objective Measurement Deadlines

| Attribute | Detail |
|-----------|--------|
| **Constraint ID** | TC-05 |
| **Description** | Business objectives have fixed measurement milestones at months 3, 6, 9, 12, and 18 post-initiation. Enabling capabilities must be live before their measurement window opens. |
| **Business Justification** | Accountability to the business case requires time-bound outcomes. Objectives without aligned delivery dates cannot be governed or rewarded. |
| **Affected Business Processes** | Process-to-objective mapping: BP-10/16 (BO-01, BO-16); BP-11/13 (BO-02); BP-07/18/25 (BO-03); BP-18/19 (BO-05, BO-08); BP-21/22 (BO-07, BO-13); BP-30 (BO-18, BO-20) |
| **Consequences if Violated** | False "red" KPI status when capability not yet delivered; premature descoping of objectives; steering committee makes decisions on misleading data; team morale and sponsor confidence decline |

---

### TC-06: Baseline Measurement Lead Time

| Attribute | Detail |
|-----------|--------|
| **Constraint ID** | TC-06 |
| **Description** | Pre-implementation baseline data for SMART objectives must be collected 30–60 days before first go-live, consuming part of the overall project timeline. |
| **Business Justification** | Improvement claims require credible before-and-after comparison. Without baseline, ROI and objective achievement cannot be substantiated to leadership or auditors. |
| **Affected Business Processes** | BP-29 (Performance Reporting), BP-11/12/13 (Accuracy), BP-18/19 (Fulfillment), BP-15 (Shrinkage) |
| **Consequences if Violated** | BO-04, BO-06, BO-07, BO-09, BO-11 targets unprovable; steering committee cannot validate success; external audit challenges benefit claims; late baseline compresses build and test window (conflicts with TC-02) |

---

## 3. Legal Constraints

### LC-01: Data Protection and Privacy Regulations

| Attribute | Detail |
|-----------|--------|
| **Constraint ID** | LC-01 |
| **Description** | The business must comply with applicable data protection laws (e.g., GDPR, local privacy regulations) for personal data in user accounts, audit logs, and customer-linked order and return records. |
| **Business Justification** | Legal obligation to protect employee and customer personal data. Non-compliance exposes the organization to regulatory penalties, legal action, and reputational harm. |
| **Affected Business Processes** | BP-16 – BP-19 (customer-linked fulfillment), BP-27 – BP-28 (Returns), BP-32 (Audit & Control Review) |
| **Consequences if Violated** | Regulatory fines and enforcement actions; required data deletion or access restrictions disrupt audit trail (BO-19); customer data breaches damage trust; legal hold on system use pending remediation |

---

### LC-02: Financial Record Retention Requirements

| Attribute | Detail |
|-----------|--------|
| **Constraint ID** | LC-02 |
| **Description** | Inventory transaction records, adjustment logs, valuation substantiation, and audit evidence must be retained for the minimum period required by tax and corporate law — typically 5–7 years. |
| **Business Justification** | Statutory and audit requirements mandate preservation of financial and inventory substantiation records. Early destruction invalidates audit defense and tax compliance. |
| **Affected Business Processes** | BP-14 (Adjustments & Write-Offs), BP-30 (Financial Reconciliation), BP-32 (Audit & Control Review), BP-07 (Goods Receipt), BP-25 (Transfer Execution) |
| **Consequences if Violated** | Audit findings and qualified opinions; inability to defend inventory valuations in tax review; regulatory penalties; BO-19 (audit trail) and BO-18 (valuation alignment) fail at external audit |

---

### LC-03: Employment and Labor Law

| Attribute | Detail |
|-----------|--------|
| **Constraint ID** | LC-03 |
| **Description** | Changes to work procedures, performance measurement, and mandatory transaction recording introduced by IMS must comply with employment contracts, collective bargaining agreements, and labor regulations. |
| **Business Justification** | Workforce practices are legally governed. Unilateral imposition of new performance or recording requirements without proper consultation creates labor relations and legal risk. |
| **Affected Business Processes** | BP-07, BP-09, BP-11, BP-18 (floor work procedures); BP-32 (accountability policies) |
| **Consequences if Violated** | Union grievances or work stoppages at affected locations; rollback of mandatory recording policies (BO-03, BO-22 fail); go-live delay at unionized sites; HR and legal remediation costs |

---

### LC-04: Supplier and Commercial Contract Terms

| Attribute | Detail |
|-----------|--------|
| **Constraint ID** | LC-04 |
| **Description** | Purchase order formats, delivery documentation, and receipt dispute processes must remain compatible with existing supplier contracts. Suppliers cannot be required to adopt new processes without contract amendment. |
| **Business Justification** | Supplier relationships are contractually bound. Receiving and procurement workflows must work with current commercial terms — the IMS initiative does not renegotiate the supplier base. |
| **Affected Business Processes** | BP-05 (Purchase Order Placement), BP-07 (Goods Receipt), BP-08 (Receipt Discrepancy Resolution) |
| **Consequences if Violated** | Supplier refusal to deliver or document shipments; receipt disputes unresolvable; inbound supply disruption; emergency procurement increases (BO-12); BR-006 and BR-007 controls weakened |

---

### LC-05: Consumer Protection and Trade Regulations

| Attribute | Detail |
|-----------|--------|
| **Constraint ID** | LC-05 |
| **Description** | Customer-facing availability and delivery commitments based on IMS data must comply with consumer protection laws on accurate product representation, cancellation rights, and delivery obligations. |
| **Business Justification** | B2B and B2C customers have legal protections against misleading availability and unfair commercial practices. ATP-based commitments must be defensible. |
| **Affected Business Processes** | BP-16 (Order Availability Confirmation), BP-19 (Partial Fulfillment & Backorder), BP-18 (Pick, Pack & Ship) |
| **Consequences if Violated** | Customer complaints to regulators; chargebacks and compensation claims; contractual penalties with B2B customers; reputational damage; BO-08 (cancellations) and BO-15 (on-time delivery) worsen |

---

## 4. Operational Constraints

### OC-01: No Operational Shutdown for Go-Live

| Attribute | Detail |
|-----------|--------|
| **Constraint ID** | OC-01 |
| **Description** | Warehouses and stores must continue receiving, fulfilling, and shipping orders during and after go-live. No full operational shutdown is permitted for system transition. |
| **Business Justification** | Customer commitments and revenue depend on continuous fulfillment. A shutdown-based cutover is commercially unacceptable for a distribution and retail operator. |
| **Affected Business Processes** | BP-07 (Receiving), BP-17 – BP-18 (Reservation & Fulfillment), BP-24 – BP-25 (Transfers), BP-10 (Status Monitoring) |
| **Consequences if Violated** | Lost sales and customer cancellations; carrier and supplier penalties; emergency manual fulfillment at higher cost; opening balance errors from rushed cutover (BO-02); rollback required with extended dual-system operation |

---

### OC-02: Daily Fulfillment Service Levels Must Be Maintained

| Attribute | Detail |
|-----------|--------|
| **Constraint ID** | OC-02 |
| **Description** | Agreed customer fulfillment service levels (fill rate, dispatch timeliness) must not materially degrade during implementation and rollout. |
| **Business Justification** | Customer contracts and brand promise depend on reliable fulfillment. The IMS program must improve control without becoming a cause of service failure. |
| **Affected Business Processes** | BP-16 – BP-20 (Order Fulfillment), BP-17 (Reservation), BP-18 (Pick, Pack & Ship) |
| **Consequences if Violated** | BO-05 (fill rate), BO-06 (cycle time), BO-15 (on-time delivery) regress; NPS on fulfillment drops (KPI-27); B2B penalties; steering committee halts rollout; revert to manual processes |

---

### OC-03: Physical Warehouse Layout and Storage Are Fixed

| Attribute | Detail |
|-----------|--------|
| **Constraint ID** | OC-03 |
| **Description** | Warehouse layouts, racking, and storage zones will not be restructured as part of the IMS initiative. Physical infrastructure remains as-is. |
| **Business Justification** | Facility investment is outside IMS funding and timeline. Accuracy and efficiency gains must come from process discipline and visibility, not capital warehouse redesign. |
| **Affected Business Processes** | BP-09 (Put-Away), BP-18 (Pick, Pack & Ship), BP-11 (Cycle Counting) |
| **Consequences if Violated** | Unfunded facility projects distract from IMS; bin-level optimization deferred; pick path inefficiency persists; accuracy improvements slower than planned (BO-02) if layout is root cause |

---

### OC-04: Existing Product Portfolio and SKU Count

| Attribute | Detail |
|-----------|--------|
| **Constraint ID** | OC-04 |
| **Description** | IMS must accommodate the current active product catalog and projected SKU growth over 18 months without requiring product range reduction. |
| **Business Justification** | Commercial strategy continues to expand assortment and channels. Inventory control must scale with the business — not force assortment rationalization as a prerequisite. |
| **Affected Business Processes** | BP-01 (Product Master), BP-03 (Stock Policy), BP-04 (ABC Classification), BP-10 (Status Monitoring) |
| **Consequences if Violated** | Forced SKU reduction damages sales; catalog cutover errors; threshold and alert programs unmanageable; BO-07 (priority stockouts) on excluded products; data migration failure at go-live |

---

### OC-05: Current Supplier and Carrier Relationships

| Attribute | Detail |
|-----------|--------|
| **Constraint ID** | OC-05 |
| **Description** | Inbound and outbound logistics continue through existing approved suppliers and carriers. The IMS project does not include supplier renegotiation or carrier replacement. |
| **Business Justification** | Supply chain partnerships are long-term commercial relationships. Receiving and shipping workflows must align with current partner capabilities and lead times. |
| **Affected Business Processes** | BP-05 – BP-09 (Inbound), BP-18 (Shipment Handoff), BP-23 (Inbound Supply Tracking) |
| **Consequences if Violated** | Unplanned partner changes disrupt supply; receiving documentation mismatch; inbound delays invalidate replenishment thresholds (BO-13); carrier tracking gaps persist |

---

### OC-06: Returns Volume Within Manual Handling Capacity

| Attribute | Detail |
|-----------|--------|
| **Constraint ID** | OC-06 |
| **Description** | Customer returns volume is expected to remain processable through basic return workflows without a dedicated returns operation for the first 12 months. If volume exceeds ~5% of outbound, scope review is required. |
| **Business Justification** | Returns handling capacity is sized for current business volume. Full reverse-logistics maturity is Phase 2 — not day-one operational capacity. |
| **Affected Business Processes** | BP-27 (Customer Return Intake), BP-28 (Return-to-Stock or Disposal) |
| **Consequences if Violated** | Returns backlog; incorrect restock or write-off; customer refund delays; warehouse floor congestion; BO-11 (shrinkage) worsens from mishandled returns; scope exception and unfunded work required |

---

### OC-07: Cycle Counting Without Operational Disruption

| Attribute | Detail |
|-----------|--------|
| **Constraint ID** | OC-07 |
| **Description** | Physical inventory verification required for accuracy objectives must be performed without shutting down receiving, picking, or shipping at any location. |
| **Business Justification** | Continuous operations are non-negotiable (OC-01, OC-02). Accuracy programs must use rolling cycle counts — not full shutdowns — except scheduled full counts planned outside peak. |
| **Affected Business Processes** | BP-11 (Cycle Counting), BP-12 (Full Physical Count), BP-13 (Variance Investigation) |
| **Consequences if Violated** | Forced shutdown conflicts with OC-01; accuracy targets delayed (BO-02); count variances increase from concurrent movements; local managers refuse count program (ORC-05); audit substantiation weak |

---

### OC-08: Multi-Location Network with Existing Transfer Practices

| Attribute | Detail |
|-----------|--------|
| **Constraint ID** | OC-08 |
| **Description** | Inter-location transfers follow existing approval practices and freight arrangements. The project does not introduce new logistics infrastructure or transfer service level agreements. |
| **Business Justification** | Network redistribution depends on current freight capacity and approval culture. IMS standardizes recording — not physical logistics network redesign. |
| **Affected Business Processes** | BP-24 (Transfer Request), BP-25 (Transfer Execution), BP-26 (Network Rebalancing) |
| **Consequences if Violated** | Unfunded logistics investment expected; transfer SLAs assumed but not met; BO-14 (imbalance reduction) delayed; emergency transfers continue outside system; source locations stockout from uncontrolled transfers (BR-012 risk) |

---

## 5. Organizational Constraints

### ORC-01: No Dedicated Full-Time Project Team

| Attribute | Detail |
|-----------|--------|
| **Constraint ID** | ORC-01 |
| **Description** | The project relies on part-time contribution from business SMEs (~20% allocation). No dedicated full-time business operations lead is assigned exclusively to the initiative. |
| **Business Justification** | Operational leaders must continue running daily business. The organization cannot spare full-time inventory SMEs without compromising fulfillment and replenishment. |
| **Affected Business Processes** | All processes requiring SME definition: BP-01, BP-03, BP-07, BP-11, BP-14, BP-21, BP-32 |
| **Consequences if Violated** | Slow decisions delay TC-02; UAT incomplete; policies undefined at go-live; floor users adopt workarounds; requirements errors discovered post-go-live; accuracy and adoption objectives fail |

---

### ORC-02: Single Product Owner Authority

| Attribute | Detail |
|-----------|--------|
| **Constraint ID** | ORC-02 |
| **Description** | Product prioritization is centralized under one Product Owner with steering committee oversight. Department heads cannot unilaterally add scope for their function. |
| **Business Justification** | Twenty-nine stakeholder groups create conflicting demands. Central prioritization protects MVP delivery and budget (BC-01) against local optimization. |
| **Affected Business Processes** | Scope affects all processes; escalations common for BP-05, BP-31, BP-26, BP-30 when deferred |
| **Consequences if Violated** | Scope creep breaches BC-01; MVP date missed (TC-02); fragmented product with inconsistent workflows (BO-03); steering committee loses governance confidence |

---

### ORC-03: Change Resistance in Warehouse Culture

| Attribute | Detail |
|-----------|--------|
| **Constraint ID** | ORC-03 |
| **Description** | Warehouse teams rely on informal practices — spreadsheets, paper logs, tribal knowledge — and history shows resistance to mandated system use without management enforcement. |
| **Business Justification** | Cultural inertia is a known organizational reality, not a failure of intent. Adoption requires enforcement policy, not only training and tooling. |
| **Affected Business Processes** | BP-07, BP-09, BP-11, BP-14, BP-18, BP-25 — all floor-recording processes |
| **Consequences if Violated** | Dual systems persist (BO-22 fails); movement recording below 98% (BO-03); accuracy stays at ~78% (BO-02); audit trail incomplete (BO-19); pilot failure poisons network rollout (TC-03) |

---

### ORC-04: Limited Internal IT Business Support Capacity

| Attribute | Detail |
|-----------|--------|
| **Constraint ID** | ORC-04 |
| **Description** | Internal technology support has limited capacity for business process design support, bulk user provisioning, and post-go-live business hypercare. Primary IT focus remains existing enterprise systems. |
| **Business Justification** | IT resources are committed to maintaining current finance, sales, and infrastructure systems. IMS operational support must be business-led at go-live. |
| **Affected Business Processes** | BP-32 (user access and audit); rollout of all transactional processes |
| **Consequences if Violated** | User provisioning delays location go-live; access errors block floor operations; post-go-live issues unresolved; business hypercare unfunded; adoption stalls (BO-21) |

---

### ORC-05: Decentralized Location Management Structure

| Attribute | Detail |
|-----------|--------|
| **Constraint ID** | ORC-05 |
| **Description** | Each warehouse and store is managed locally with operational autonomy. Central mandates require regional or executive endorsement for enforcement. |
| **Business Justification** | The operating model delegates day-to-day accountability to site managers. Network standardization is a cultural and governance challenge — not automatic with system deployment. |
| **Affected Business Processes** | BP-02 (Location Setup), BP-03 (Stock Policy), BP-11 (Cycle Counting), BP-24 (Transfers), BP-29 (Location Performance) |
| **Consequences if Violated** | Location-to-location process variation continues (BO-03); network KPIs not comparable; some sites never adopt; BO-14 (imbalance) uncorrected; executive dashboard misleading (BO-01) |

---

### ORC-06: Finance and Operations Reporting Alignment Gap

| Attribute | Detail |
|-----------|--------|
| **Constraint ID** | ORC-06 |
| **Description** | Finance and operations use different data sources and reconciliation practices for inventory. No established single reconciliation process exists between operational and financial records. |
| **Business Justification** | Historical organizational silos separated operational stock records from general ledger inventory. IMS alone cannot create alignment — cross-department process must be designed. |
| **Affected Business Processes** | BP-14 (Adjustments & Write-Offs), BP-30 (Financial Reconciliation), BP-29 (Reporting) |
| **Consequences if Violated** | BO-18 (valuation variance ≤2%) unachievable; month-end close remains 7+ days (BO-20); finance distrusts operational data; manual reconciliation continues (BO-04 fails); audit findings on inventory substantiation |

---

### ORC-07: No Formal Inventory Management Function Today

| Attribute | Detail |
|-----------|--------|
| **Constraint ID** | ORC-07 |
| **Description** | The business lacks a mature, centralized inventory management function with defined policies, KPIs, and single-point accountability. Control is distributed across warehouse, purchasing, and finance. |
| **Business Justification** | Growth outpaced governance design. The initiative assumes creation of Inventory Controller accountability — a structural gap that must be closed for sustained control. |
| **Affected Business Processes** | BP-01, BP-03, BP-04, BP-11, BP-13, BP-15, BP-21, BP-32 — all governance-heavy processes |
| **Consequences if Violated** | Policies unwritten and unenforced; no owner for accuracy program (BO-02); replenishment remains reactive (BO-13); shrinkage unanalyzed (BO-11); project delivers software without organizational capability; chronic inaccuracy persists |

---

## 6. Technology Constraints — Business Level

*Expressed as business operating boundaries, not technical implementation limits.*

### TEC-01: Must Coexist With Existing Enterprise Systems

| Attribute | Detail |
|-----------|--------|
| **Constraint ID** | TEC-01 |
| **Description** | IMS operates alongside existing finance, sales, and HR systems without replacing them. Users continue working across multiple systems daily. |
| **Business Justification** | Enterprise systems remain authoritative in their domains per BC-05. IMS is the inventory system of record — not the enterprise platform of record. |
| **Affected Business Processes** | BP-05 (PO with finance), BP-16 (orders from sales systems), BP-30 (valuation to finance), BP-27 (returns with CS systems) |
| **Consequences if Violated** | Stakeholder conflict and duplicate data entry; users revert to legacy tools; BO-16 limited to IMS-native workflows; finance alignment delayed (BO-18); initiative perceived as failed ERP attempt |

---

### TEC-02: No Budget for Dedicated Warehouse Hardware

| Attribute | Detail |
|-----------|--------|
| **Constraint ID** | TEC-02 |
| **Description** | The business will not purchase dedicated warehouse hardware (rugged scanners, handhelds, label printers) as part of IMS. Users access the system via existing company computers and devices. |
| **Business Justification** | Hardware investment is a separate capital decision. IMS rollout must be achievable with assets already deployed at sites. |
| **Affected Business Processes** | BP-07 (Receiving), BP-11 (Cycle Counting), BP-18 (Pick, Pack & Ship) |
| **Consequences if Violated** | Unbudgeted capex request (BC-03 conflict); floor process slower than planned (BO-06); barcode benefits limited; users skip scanning steps; receipt and pick errors persist (BO-02, BO-05) |

---

### TEC-03: Standard Web Browser Access Required

| Attribute | Detail |
|-----------|--------|
| **Constraint ID** | TEC-03 |
| **Description** | All users must access IMS through a standard web browser on company-approved devices without installing specialized desktop applications. |
| **Business Justification** | Corporate IT standardizes on browser-based applications for supportability and security. Proprietary client software is not approved for this initiative. |
| **Affected Business Processes** | All user-facing processes; floor operations at BP-07, BP-11, BP-18 most affected |
| **Consequences if Violated** | IT blocks deployment; locations without reliable connectivity cannot operate (floor downtime); adoption limited to office roles; warehouse recording compliance drops (BO-03) |

---

### TEC-04: No Real-Time External Channel Integration in MVP

| Attribute | Detail |
|-----------|--------|
| **Constraint ID** | TEC-04 |
| **Description** | Sales channels (e-commerce, B2B portal, marketplaces) will not receive automated real-time inventory feeds from IMS in the first 12 months. Channel availability updates follow existing manual processes. |
| **Business Justification** | Channel integration requires separate business case and partner agreements. MVP focuses on internal operational truth before external synchronization. |
| **Affected Business Processes** | BP-10 (Status Monitoring), BP-16 (Availability Confirmation) — external channel context |
| **Consequences if Violated** | Unplanned integration work breaches BC-01 and TC-02; channel overselling continues (BO-08); marketplace penalties; BO-16 applies only to internal sales — external channels remain inaccurate |

---

### TEC-05: Manual Data Exchange With Finance System

| Attribute | Detail |
|-----------|--------|
| **Constraint ID** | TEC-05 |
| **Description** | Inventory valuation and movement data transfer to finance through scheduled export or manual reconciliation in the first 12 months — not automated general ledger posting. |
| **Business Justification** | Finance system integration is out of IMS scope (BC-05). Interim operating model must close books using agreed manual reconciliation until Phase 3 automation. |
| **Affected Business Processes** | BP-14 (Adjustments & Write-Offs), BP-30 (Financial Reconciliation) |
| **Consequences if Violated** | Finance team unprepared for new data volume; month-end delays continue (BO-20); valuation variance stays at ~8% (BO-18); duplicate or lost adjustments; audit trail gaps if exports not archived (LC-02) |

---

### TEC-06: User Access Limited to Company Network and Approved Devices

| Attribute | Detail |
|-----------|--------|
| **Constraint ID** | TEC-06 |
| **Description** | Access to inventory data — stock levels, valuation, movement history — is restricted to company-managed devices and approved network access per corporate security policy. |
| **Business Justification** | Inventory data is commercially and financially sensitive. Corporate security policy prohibits unmanaged device access to operational and valuation information. |
| **Affected Business Processes** | BP-10 (Visibility), BP-16 (Sales Availability), BP-29/30 (Management & Finance Reporting) |
| **Consequences if Violated** | Security policy breach; data leakage of stock positions or valuation; remote sales and regional managers cannot access ATP without VPN; workaround spreadsheets reappear (BO-22); regulatory exposure (LC-01) |

---

## Constraint Interaction Summary

Constraints frequently compound. The following interactions have amplified operational impact:

| Interaction | Constraints | Operational Consequence if Ignored |
|-------------|-------------|-----------------------------------|
| Budget + Time | BC-01 + TC-02 | MVP scope inflation causes missed go-live and unfunded overrun |
| Budget + Organization | BC-02 + ORC-01 | Same staff run daily ops and project — burnout and adoption failure |
| Operational + Time | OC-01 + TC-04 | Narrow rollout windows; missed blackout = delayed network benefits 6+ months |
| Organization + Technology | ORC-03 + TEC-01 | Resistant users juggle IMS plus legacy systems without integration |
| Legal + Operations | LC-02 + TEC-05 | Manual finance exports must still meet 5–7 year retention |
| Operational + Organization | OC-07 + ORC-05 | Rolling counts need local manager cooperation at every decentralized site |
| Governance gap + Time | ORC-07 + TC-02 | Go-live without Inventory Controller — policies undefined, accuracy fails |

---

## Constraints by Business Process Domain

| Process Domain | Primary Constraints |
|----------------|---------------------|
| Master Data & Governance (BP-01 – BP-04) | ORC-07, ORC-01, OC-04, TC-02 |
| Inbound & Receiving (BP-05 – BP-09) | LC-04, OC-05, OC-01, ORC-03, TEC-02 |
| Inventory Control (BP-10 – BP-15) | OC-07, ORC-07, ORC-05, LC-02 |
| Order Fulfillment (BP-16 – BP-20) | OC-02, OC-01, LC-05, TEC-04, TC-04 |
| Replenishment (BP-21 – BP-23) | ORC-07, BC-02, OC-05, LC-04 |
| Network Balance (BP-24 – BP-26) | OC-08, TC-03, ORC-05 |
| Returns (BP-27 – BP-28) | OC-06, LC-01, LC-05 |
| Performance & Financial (BP-29 – BP-30) | ORC-06, TEC-05, LC-02, TC-05 |
| Commercial & Governance (BP-31 – BP-32) | ORC-07, LC-01, LC-03, BC-01 |

---

## Traceability Reference

| Source | Identifier |
|--------|------------|
| Business Requirements Document | BRD-IMS-001, Section 18 |
| Business Constraints Discovery | BC-01 – BC-06, TC-01 – TC-06, LC-01 – LC-05, OC-01 – OC-08, ORC-01 – ORC-07, TEC-01 – TEC-06 |
| Business Processes | BP-01 – BP-32 |
| SMART Business Objectives | BO-01 – BO-24 |
| Business Assumptions | BA-03, BA-13, BA-24, BA-30, BA-38, BA-43 |

---

## Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Senior Business Analyst | | | |
| Product Owner | | | |
| Project Sponsor | | | |

---

*End of Business Constraints Specification*

*Document ID: SRS-BC-001 | Version 1.0 | July 5, 2026*
