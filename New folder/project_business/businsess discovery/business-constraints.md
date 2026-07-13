# Business Constraints: Inventory Management System

**Document Owner:** Product Owner  
**Based On:** Business Vision Document, Project Scope Document, Stakeholder Analysis, SMART Business Objectives, Business Assumptions  
**Purpose:** Identify all business constraints that limit or shape the IMS initiative and explain their impact on project delivery and outcomes  
**Scope:** Business constraints only — technology constraints expressed at business level, not implementation level

---

## Constraint Categories Overview

| Category | Count | Description |
|----------|-------|-------------|
| Budget Constraints | 6 | Financial limits on investment, spending, and ongoing cost |
| Time Constraints | 6 | Deadlines, phases, and calendar limitations |
| Legal Constraints | 5 | Regulatory, contractual, and compliance boundaries |
| Operational Constraints | 8 | Day-to-day business operations that limit change |
| Organizational Constraints | 7 | Structure, culture, and people limitations |
| Technology Constraints (Business Level) | 6 | System boundary and capability limits from a business perspective |

**Total: 38 business constraints**

---

## 1. Budget Constraints

---

### BC-01: Fixed Total Initiative Budget

| Attribute | Detail |
|-----------|--------|
| **Constraint** | The IMS initiative must be delivered within a fixed total budget approved by executive leadership, covering software, services, training, change management, and first-year operational support — with no guarantee of additional funding if overruns occur |
| **Impact on Project** | Product scope must be ruthlessly prioritized; MVP features are non-negotiable while Phase 2 and Phase 3 enhancements compete for remaining budget. Feature requests outside approved scope require formal change control and may be deferred. Vendor and service procurement must align with funding release schedule — delayed releases delay delivery. |

---

### BC-02: No Additional Warehouse Headcount Budget

| Attribute | Detail |
|-----------|--------|
| **Constraint** | The business case does not include budget for additional warehouse or inventory control headcount in the first 12 months; efficiency must come from the system and process improvement, not new hires |
| **Impact on Project** | System workflows must be simple enough for existing staff to absorb without dedicated system operators. Training investment becomes critical. Rollout cannot coincide with peak seasons when staff have no capacity for learning. Automation features that reduce manual effort (alerts, self-service availability) are prioritized over features that add recording burden. |

---

### BC-03: Capital Expenditure vs. Operating Expenditure Limits

| Attribute | Detail |
|-----------|--------|
| **Constraint** | Finance has defined separate caps for capital expenditure (licenses, implementation) and operating expenditure (subscriptions, support, training); spending category cannot be shifted without CFO approval |
| **Impact on Project** | Licensing and subscription model choices are constrained by how finance classifies costs. Multi-year subscription deals may conflict with annual opex budgets. Implementation services must be invoiced within the capital budget window or delivery is delayed to the next fiscal period. |

---

### BC-04: Training and Change Management Budget Ceiling

| Attribute | Detail |
|-----------|--------|
| **Constraint** | A fixed budget is allocated for training, communications, and change management activities — typically a defined percentage of total project cost — and cannot be reallocated from development or licensing budgets |
| **Impact on Project** | Training must be efficient and scalable: train-the-trainer models, e-learning, and standardized materials across locations rather than bespoke per-site programs. Locations beyond the primary rollout may receive lighter-touch onboarding. User adoption risk (BO-21) increases if training budget is insufficient for all roles. |

---

### BC-05: No Budget for External System Replacement

| Attribute | Detail |
|-----------|--------|
| **Constraint** | The IMS budget does not include funding to replace existing finance, sales, HR, or ERP systems; the IMS must operate within the current enterprise system landscape |
| **Impact on Project** | IMS is scoped as an inventory capability layer, not a platform replacement. Integration with existing systems may be manual or deferred in MVP. Finance and sales teams must continue using their current tools alongside the IMS. Scope boundary enforcement (BA-30) is a product management responsibility. |

---

### BC-06: Ongoing Operational Cost Limit

| Attribute | Detail |
|-----------|--------|
| **Constraint** | Annual recurring cost for licenses, support, and maintenance after go-live must remain within a defined operating budget threshold approved by CFO — typically expressed as a maximum percentage of current inventory carrying cost |
| **Impact on Project** | Per-user or per-location licensing models directly affect scalability economics. Features that require premium license tiers may be postponed. Future location onboarding incurs incremental cost that must be pre-approved. Long-term TCO is a product selection criterion alongside functional fit. |

---

## 2. Time Constraints

---

### TC-01: 18-Month Business Vision Horizon

| Attribute | Detail |
|-----------|--------|
| **Constraint** | All SMART business objectives and phased outcomes must be achievable within an 18-month window from project initiation, aligned with the business vision short-term plan |
| **Impact on Project** | Product roadmap is bounded by three phases: stabilize (0–6 months), improve performance (6–12 months), enable decisions (12–18 months). Features beyond 18 months are classified as future enhancements, not committed deliverables. Objective measurement deadlines (BO-01 through BO-24) drive release prioritization. |

---

### TC-02: MVP Delivery Within 6 Months

| Attribute | Detail |
|-----------|--------|
| **Constraint** | The Minimum Viable Product must be live at the first primary location within 6 months of project kickoff to meet Phase 1 business vision and P1 SMART objectives |
| **Impact on Project** | Only MVP must-have features are in scope for the first release. Discovery and requirements must be completed quickly — extended analysis phases delay go-live. UAT and training windows are compressed. Postponed features (per project scope) are explicitly excluded from the 6-month commitment. |

---

### TC-03: Sequential Location Rollout Window

| Attribute | Detail |
|-----------|--------|
| **Constraint** | Primary locations must be onboarded sequentially over a 6-month window following first go-live, with a minimum 4-week gap between location deployments — not all locations simultaneously |
| **Impact on Project** | Full network-wide objectives (BO-01, BO-14) are not achievable until all primary locations are live — approximately month 12. Product configuration must be portable across locations. Lessons learned from each rollout inform the next. Support team capacity limits parallel deployments. |

---

### TC-04: Peak Season Blackout Periods

| Attribute | Detail |
|-----------|--------|
| **Constraint** | System go-live, major upgrades, and intensive training cannot occur during defined peak business periods (e.g., holiday retail season, fiscal year-end, promotional events) at each location |
| **Impact on Project** | Rollout calendar is dictated by business calendar, not project preference. Locations with peak in Q4 may not go live until Q1. Training must be completed before peak blackout begins. Feature releases that risk operational disruption are scheduled outside blackout windows. |

---

### TC-05: SMART Objective Measurement Deadlines

| Attribute | Detail |
|-----------|--------|
| **Constraint** | Business objectives have fixed measurement milestones at months 3, 6, 9, 12, and 18 post go-live; features required to achieve objectives must be delivered before their measurement window opens |
| **Impact on Project** | P1 objectives (months 3–6) dictate MVP content. P2 objectives (months 6–12) dictate Phase 2 release content. P3 objectives (months 12–18) dictate Phase 3 content. Late feature delivery means objectives are measured before the enabling capability exists — creating false failure signals. |

---

### TC-06: Baseline Measurement Lead Time

| Attribute | Detail |
|-----------|--------|
| **Constraint** | Pre-implementation baseline data for SMART objectives must be collected 30–60 days before first go-live, consuming part of the overall project timeline |
| **Impact on Project** | Discovery and baseline collection run in parallel with early design activities. If baseline collection starts late, improvement metrics are unprovable. Project plan must allocate 4–8 weeks for baseline before go-live, reducing available time for build and test. |

---

## 3. Legal Constraints

---

### LC-01: Data Protection and Privacy Regulations

| Attribute | Detail |
|-----------|--------|
| **Constraint** | The business must comply with applicable data protection laws (e.g., GDPR, local data privacy regulations) regarding personal data stored in system user accounts, audit logs, and customer-linked order records |
| **Impact on Project** | User data retention policies must be defined. Audit logs containing user identity are subject to privacy requirements. Customer data visible in order fulfillment must comply with access and retention rules. Data export and deletion capabilities may be required for compliance requests. |

---

### LC-02: Financial Record Retention Requirements

| Attribute | Detail |
|-----------|--------|
| **Constraint** | Inventory transaction records, adjustment logs, and valuation reports must be retained for a minimum period defined by tax and corporate law — typically 5–7 years depending on jurisdiction |
| **Impact on Project** | System must support retrieval of historical inventory records for the full retention period. Archiving and export capabilities are a business requirement, not optional. Disposal of records before retention period expires is prohibited. External audit access to historical data must be supported. |

---

### LC-03: Employment and Labor Law

| Attribute | Detail |
|-----------|--------|
| **Constraint** | Changes to work procedures, performance measurement, and transaction recording requirements introduced by the IMS must comply with employment contracts, collective bargaining agreements, and labor regulations |
| **Impact on Project** | Mandatory recording policies and performance metrics tied to system compliance must be reviewed by HR and legal before enforcement. Union consultation may be required before go-live at unionized locations. Process changes cannot be implemented unilaterally if restricted by labor agreements (see BA-38). |

---

### LC-04: Supplier and Commercial Contract Terms

| Attribute | Detail |
|-----------|--------|
| **Constraint** | Purchase order formats, delivery documentation requirements, and dispute resolution processes must remain compatible with existing supplier contracts; suppliers cannot be forced to adopt new processes without contract amendment |
| **Impact on Project** | Receiving workflows must accommodate current supplier documentation standards. Supplier portal or EDI integration (future enhancement) requires contractual negotiation — cannot be mandated in MVP. Top suppliers by volume drive receiving design; long-tail suppliers may continue manual processes. |

---

### LC-05: Consumer Protection and Trade Regulations

| Attribute | Detail |
|-----------|--------|
| **Constraint** | Customer-facing availability and delivery commitments made using IMS data must comply with consumer protection laws regarding accurate product representation, cancellation rights, and delivery obligations |
| **Impact on Project** | Available-to-promise data shown to customers must be defensible — overstating availability creates legal exposure. Delivery date commitments must be based on reliable fulfillment data. Partial shipment and cancellation policies must comply with consumer rights. B2C channel integration requires legal review of availability display rules. |

---

## 4. Operational Constraints

---

### OC-01: No Operational Shutdown for Go-Live

| Attribute | Detail |
|-----------|--------|
| **Constraint** | Warehouses and stores must continue fulfilling orders during and after go-live; there can be no full operational shutdown for system transition |
| **Impact on Project** | Go-live must use a phased or parallel-run approach with cutover during low-activity periods. Opening stock balances must be established without halting receipts or shipments. Rollback plan is required if go-live disrupts fulfillment. Training must prepare users before they encounter live transactions. |

---

### OC-02: Daily Fulfillment Service Levels Must Be Maintained

| Attribute | Detail |
|-----------|--------|
| **Constraint** | Order fulfillment service levels agreed with customers (fill rate, dispatch time) must not materially degrade during implementation and rollout phases |
| **Impact on Project** | Go-live timing avoids peak volume periods. Additional support staff may be needed on go-live day without budget for permanent hires. System issues during rollout directly affect customer commitments — robust hypercare support is required. BO-05 and BO-06 cannot be sacrificed during transition. |

---

### OC-03: Physical Warehouse Layout and Storage Are Fixed

| Attribute | Detail |
|-----------|--------|
| **Constraint** | The business will not restructure warehouse layouts, install new racking, or redesign storage zones as part of the IMS project; physical infrastructure remains as-is |
| **Impact on Project** | Bin-level and shelf-level location management (future enhancement) is limited by existing physical organization. Pick paths cannot be optimized through layout changes. Location hierarchy in the system reflects current physical structure. Accuracy improvements must come from process and system, not facility investment. |

---

### OC-04: Existing Product Portfolio and SKU Count

| Attribute | Detail |
|-----------|--------|
| **Constraint** | The IMS must accommodate the current active product catalog size and projected SKU growth over 18 months without requiring product range reduction or simplification |
| **Impact on Project** | Product data migration scope is defined by current catalog size. Performance and usability expectations must hold at current SKU volume. New product introductions during rollout add ongoing data maintenance workload for Inventory Controller. ABC classification (BA-18) must be manageable at current catalog scale. |

---

### OC-05: Current Supplier and Carrier Relationships

| Attribute | Detail |
|-----------|--------|
| **Constraint** | Inbound and outbound logistics continue through existing approved suppliers and carriers; the IMS project does not include supplier renegotiation or carrier replacement |
| **Impact on Project** | Receiving and shipping workflows must match current partner capabilities. Supplier lead times and documentation standards are inputs, not outputs of the project. Carrier tracking integration (manual in MVP) is constrained by what current partners provide. Emergency supplier changes during rollout are out of scope. |

---

### OC-06: Returns Volume Within Manual Handling Capacity

| Attribute | Detail |
|-----------|--------|
| **Constraint** | Customer returns volume is expected to remain within levels that can be processed through basic return-to-stock or write-off workflows without a dedicated returns module for the first 12 months |
| **Impact on Project** | Full returns management is postponed per project scope. If return volume exceeds 5% of outbound (per BA-13 validation), a scope exception may be needed. Return handling process must be documented and staffed within existing customer service and warehouse capacity. |

---

### OC-07: Cycle Counting Without Operational Disruption

| Attribute | Detail |
|-----------|--------|
| **Constraint** | Physical inventory counts required for accuracy objectives (BO-02) must be performed without shutting down receiving, picking, or shipping at any location |
| **Impact on Project** | Cycle count program design must use rolling counts by zone or category, not full-wall-to-wall counts that halt operations. Count frequency and scope are constrained by floor staff availability. Accuracy targets may take longer to achieve if count coverage is limited by operational continuity requirement. |

---

### OC-08: Multi-Location Network with Existing Transfer Practices

| Attribute | Detail |
|-----------|--------|
| **Constraint** | Inter-location stock transfers follow existing business approval practices and freight arrangements; the IMS project does not include new logistics infrastructure or transfer service level agreements |
| **Impact on Project** | Transfer workflows in the system mirror current approval chains. Transfer lead time between locations is a business constant — imbalance correction (BO-14) is limited by physical transfer speed. Emergency transfers during rollout may still occur outside the system if process is not yet adopted. |

---

## 5. Organizational Constraints

---

### ORC-01: No Dedicated Full-Time Project Team

| Attribute | Detail |
|-----------|--------|
| **Constraint** | The project relies on part-time contribution from business subject matter experts (Inventory Controller, Warehouse Managers, Purchasing Manager, Sales Manager) at approximately 20% allocation — there is no dedicated full-time business analyst or operations lead assigned exclusively to the project |
| **Impact on Project** | Requirements workshops, UAT, and rollout support compete with daily operational duties. Decision turnaround depends on SME availability. Product Owner must batch decisions and minimize round-trips. Extended discovery phases are not feasible. SME absence during peak operations delays project milestones. |

---

### ORC-02: Single Product Owner Authority

| Attribute | Detail |
|-----------|--------|
| **Constraint** | Product prioritization decisions are made by one Product Owner with steering committee oversight; individual department heads cannot unilaterally add scope for their function |
| **Impact on Project** | Conflicting stakeholder requests are resolved through prioritization, not accommodation. Department-specific features wait unless they serve cross-functional objectives. Escalation to steering committee is required for scope changes. Product Owner must maintain scope discipline against 29 stakeholder groups. |

---

### ORC-03: Change Resistance in Warehouse Culture

| Attribute | Detail |
|-----------|--------|
| **Constraint** | Warehouse teams have established informal practices — paper logs, spreadsheets, tribal knowledge — and organizational history shows resistance to mandated system use without management enforcement |
| **Impact on Project** | Adoption objectives (BO-21, BO-22) require active change management, not just system delivery. Parallel manual tools must be explicitly retired with management backing. Training alone is insufficient — compliance policy and audit are needed. First impressions at pilot location determine network-wide adoption trajectory. |

---

### ORC-04: Limited Internal IT Business Support Capacity

| Attribute | Detail |
|-----------|--------|
| **Constraint** | Internal IT or technology support team has limited capacity to support business process design, user provisioning at scale, and post-go-live business support — primary IT focus remains on existing enterprise systems |
| **Impact on Project** | User account management and role assignment may depend on a small admin team — bulk provisioning must be planned. Business-side hypercare support is needed at go-live, not just technical support. System administrator role (stakeholder) must be clearly defined and staffed. IT cannot absorb unlimited post-go-live enhancement requests. |

---

### ORC-05: Decentralized Location Management Structure

| Attribute | Detail |
|-----------|--------|
| **Constraint** | Each warehouse and store is managed by a local manager with operational autonomy; central mandates require regional or executive endorsement to be enforced |
| **Impact on Project** | Standardized processes (BO-03) require buy-in from each location manager, not just central operations. Rollout at each location needs local champion and manager commitment. Configuration may need location-specific exceptions if central standard is rejected. Network-wide objectives depend on consistent local compliance. |

---

### ORC-06: Finance and Operations Reporting Alignment Gap

| Attribute | Detail |
|-----------|--------|
| **Constraint** | Finance and operations currently use different data sources and reconciliation practices for inventory; no established single reconciliation process exists between operational and financial records |
| **Impact on Project** | BO-18 (valuation variance ≤ 2%) requires new cross-department process design, not just system delivery. Finance liaison (BA-06) must be assigned. Month-end close improvement (BO-20) depends on process agreement, not system alone. Interim valuation method must be agreed before financial reporting from IMS is trusted. |

---

### ORC-07: No Formal Inventory Management Function Today

| Attribute | Detail |
|-----------|--------|
| **Constraint** | The business does not currently have a mature, centralized inventory management function with defined policies, KPIs, and accountability — inventory control is distributed across warehouse, purchasing, and finance with overlapping responsibilities |
| **Impact on Project** | Inventory Controller role (BA-03) must be created or formally assigned as part of the initiative. Policies for adjustments, counts, and replenishment must be written, not just configured. SMART objectives require an accountable owner that does not fully exist today. Project delivers capability; organization must deliver governance. |

---

## 6. Technology Constraints (Business Level Only)

---

### TEC-01: Must Coexist With Existing Enterprise Systems

| Attribute | Detail |
|-----------|--------|
| **Constraint** | The IMS must operate alongside existing finance, sales, and HR systems without replacing them; users will continue to work across multiple systems daily |
| **Impact on Project** | IMS is the inventory system of record, not the enterprise system of record. Data handoff to finance and sales may be manual export in MVP. Users experience multiple logins and interfaces. Integration features are future enhancements, not MVP commitments. Scope boundary with ERP must be communicated clearly to all stakeholders. |

---

### TEC-02: No Budget for Dedicated Hardware or Devices

| Attribute | Detail |
|-----------|--------|
| **Constraint** | The business will not purchase dedicated warehouse hardware (handheld scanners, rugged devices, label printers) as part of the IMS project; users will access the system via existing company-provided computers and devices |
| **Impact on Project** | Warehouse floor workflows must be usable on existing desktops, laptops, or personal devices available at each location. Barcode scanning (in scope per project scope) depends on device camera or existing peripherals. Mobile-optimized warehouse experience is postponed. Pick and receive speed may be limited by input method until hardware investment is approved separately. |

---

### TEC-03: Standard Web Browser Access Required

| Attribute | Detail |
|-----------|--------|
| **Constraint** | All users must be able to access the system through a standard web browser on company-approved devices without installing specialized desktop applications |
| **Impact on Project** | Solution must be browser-accessible from a business requirement perspective. Offline operation is not a business requirement in MVP — locations without reliable internet face operational risk. User experience must be functional on minimum company device standards. |

---

### TEC-04: No Real-Time External Channel Integration in MVP

| Attribute | Detail |
|-----------|--------|
| **Constraint** | From a business perspective, sales channels (e-commerce, B2B portal, marketplaces) will not receive automated real-time inventory feeds from the IMS in the first 12 months; stock availability to customers is updated through existing channel processes |
| **Impact on Project** | Overselling risk on external channels persists until integration is delivered. BO-16 (sales self-service) applies to internal sales team, not automated channel sync. Marketplace and partner SLAs (BA-23) must be managed manually. Channel integration is a future enhancement requiring separate business case. |

---

### TEC-05: Manual Data Exchange With Finance System

| Attribute | Detail |
|-----------|--------|
| **Constraint** | Inventory valuation and movement data will be transferred to the finance system through scheduled export or manual reconciliation in the first 12 months — not automated real-time GL posting |
| **Impact on Project** | BO-18 and BO-20 depend on a defined manual reconciliation process until integration is built. Finance team workload includes export/import steps. Valuation timeliness is limited by reconciliation frequency (e.g., monthly at close). Automated finance integration is a Phase 3 or future enhancement. |

---

### TEC-06: User Access Limited to Company Network and Approved Devices

| Attribute | Detail |
|-----------|--------|
| **Constraint** | Business policy requires that access to inventory data — including stock levels, valuation, and movement history — is restricted to company-managed devices and approved network access; remote access follows company VPN and security policies |
| **Impact on Project** | Remote warehouse managers and regional staff must use approved access methods. Sales representatives checking availability remotely depend on VPN or company device policy. External parties (suppliers, auditors) receive data through export or temporary access, not standing system accounts in MVP. |

---

## Constraint Impact Summary Matrix

| Constraint ID | Category | Primary Impact Area | Affected Objectives |
|---------------|----------|--------------------|--------------------|
| BC-01 | Budget | Scope prioritization | All objectives — funding limits feature delivery |
| BC-02 | Budget | Workflow simplicity | BO-04, BO-21 |
| BC-05 | Budget | System boundary | BO-18, BO-20 |
| TC-01 | Time | Roadmap boundaries | All objectives — 18-month cap |
| TC-02 | Time | MVP scope | BO-01, BO-03, BO-16, BO-19, BO-21, BO-22 |
| TC-03 | Time | Network-wide delivery | BO-01, BO-14 |
| TC-04 | Time | Rollout calendar | BO-21, BO-22 |
| LC-01 | Legal | Data handling | BO-19 |
| LC-02 | Legal | Record retention | BO-18, BO-19, BO-20 |
| OC-01 | Operational | Go-live approach | BO-02, BO-05, BO-06 |
| OC-02 | Operational | Service continuity | BO-05, BO-06, BO-15 |
| OC-07 | Operational | Count program design | BO-02 |
| ORC-01 | Organizational | Decision speed | All — SME availability |
| ORC-03 | Organizational | Adoption | BO-03, BO-21, BO-22 |
| ORC-07 | Organizational | Governance | BO-02, BO-11, BO-13 |
| TEC-01 | Technology (business) | Multi-system landscape | BO-16, BO-18 |
| TEC-04 | Technology (business) | Channel accuracy | BO-08, BO-15 |
| TEC-05 | Technology (business) | Finance alignment | BO-18, BO-20 |

---

## Constraint Severity Classification

| Severity | Definition | Constraints |
|----------|------------|-------------|
| **Blocking** | Cannot proceed without explicit resolution or exception | BC-01, TC-02, OC-01, ORC-07 |
| **High** | Significantly shapes scope, timeline, or adoption | BC-02, BC-05, TC-01, TC-03, TC-04, ORC-01, ORC-03, ORC-05, TEC-01, TEC-04 |
| **Medium** | Requires mitigation planning but manageable | BC-03, BC-04, BC-06, TC-05, TC-06, LC-01, LC-02, LC-03, OC-02, OC-04, OC-07, OC-08, ORC-02, ORC-04, ORC-06, TEC-02, TEC-05, TEC-06 |
| **Low** | Monitor and accommodate in design | LC-04, LC-05, OC-03, OC-05, OC-06 |

---

## Constraint Interactions

Several constraints compound each other and create amplified impact:

| Interaction | Constraints | Combined Impact |
|-------------|-------------|-----------------|
| **Budget + Time** | BC-01 + TC-02 | MVP must deliver maximum business value within fixed budget and 6-month deadline — no scope expansion and no timeline extension |
| **Budget + Organizational** | BC-02 + ORC-01 | No new hires and no full-time project team — existing staff must absorb project and daily operations simultaneously |
| **Operational + Time** | OC-01 + TC-04 | Go-live must be non-disruptive AND avoid peak seasons — rollout windows are narrow |
| **Organizational + Technology** | ORC-03 + TEC-01 | Users resistant to one new system must now work across multiple systems without integration |
| **Legal + Technology** | LC-02 + TEC-05 | Retention requirements apply to records that are manually exchanged with finance — archival of exports is a business process requirement |
| **Operational + Organizational** | OC-07 + ORC-05 | Cycle counts without shutdown require local manager cooperation at each decentralized location |

---

## Product Owner Response Strategy

| Strategy | Applicable Constraints | Action |
|----------|----------------------|--------|
| **Scope discipline** | BC-01, BC-05, TC-01, TC-02 | Enforce MVP boundary; defer enhancements per project scope |
| **Phased delivery** | TC-01, TC-03, TC-05 | Align releases to SMART objective milestones |
| **Change management investment** | BC-04, ORC-03, ORC-05 | Protect training budget; secure management enforcement policy |
| **Governance establishment** | ORC-07, ORC-06 | Assign Inventory Controller and finance liaison before go-live |
| **Calendar planning** | TC-04, OC-01, OC-02 | Publish rollout calendar with blackout periods 6 months ahead |
| **Manual process bridges** | TEC-04, TEC-05, TEC-01 | Document interim manual processes for finance and channel sync |
| **Legal review** | LC-01, LC-03, LC-05 | Engage legal and HR before policy changes and customer-facing availability |

---

## Alignment with Business Assumptions

| Constraint | Related Assumption | Relationship |
|------------|-------------------|--------------|
| BC-01 | BA-24 (approved budget) | Assumption must be true for constraint to be manageable |
| BC-02 | BA-04 (sufficient staffing) | Constraint makes assumption harder to validate |
| TC-03 | BA-43 (sequential rollout) | Constraint enforces assumption |
| OC-06 | BA-13 (returns volume manageable) | Assumption must be validated or constraint forces scope change |
| ORC-07 | BA-03 (Inventory Controller exists) | Constraint requires assumption to be proactively resolved |
| TEC-04 | BA-23 (no channel integration in 12 months) | Constraint and assumption are aligned |
| LC-03 | BA-38 (no labor restrictions) | Assumption validation required to confirm constraint severity |

---

## Document Summary

This document identifies **38 business constraints** across six categories that bound the Inventory Management System initiative. These constraints are not optional obstacles — they are fixed conditions within which the product must be delivered and adopted.

**Four blocking constraints** (fixed budget, 6-month MVP deadline, no operational shutdown, no existing inventory governance function) require explicit resolution before or during project initiation.

**Ten high-severity constraints** significantly shape product scope, rollout calendar, adoption strategy, and system boundary decisions.

The Product Owner must manage delivery within these constraints by enforcing scope discipline, aligning releases to SMART objective milestones, investing in change management, establishing governance roles, and documenting manual process bridges where automation is constrained.

Constraints should be reviewed at each steering committee meeting; any constraint that changes status (e.g., budget increase, peak season shift, new legal requirement) triggers a scope and timeline impact assessment.

---

*End of Business Constraints Document*
