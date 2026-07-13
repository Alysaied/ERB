# Stakeholder Analysis: Inventory Management System

**Document Owner:** Senior Business Analyst  
**Based On:** Business Vision Document, Project Scope Document  
**Purpose:** Identify all stakeholders, their needs, and their relationship to the Inventory Management System  
**Scope:** Business and product perspective — no implementation design

---

## Stakeholder Summary

| Category | Count | Stakeholder Groups |
|----------|-------|-------------------|
| **Internal — Executive & Governance** | 4 | CEO, COO, CFO, Internal Auditor |
| **Internal — Operations & Warehouse** | 6 | Operations Director, Warehouse Manager, Receiving Clerk, Warehouse Picker/Packer, Inventory Controller, Regional/Store Manager |
| **Internal — Commercial** | 4 | Sales Manager, Sales Representative, Customer Service Representative, Marketing Manager |
| **Internal — Supply & Finance** | 3 | Purchasing Manager, Buyer/Procurement Officer, Finance Manager/Accountant |
| **Internal — Technology & Project** | 4 | Project Sponsor, Product Owner, Business Analyst, System Administrator |
| **External — Supply Chain** | 3 | Supplier/Vendor, Logistics/Carrier Partner, Freight Forwarder |
| **External — Customers** | 2 | B2B Customer, B2C Customer |
| **External — Oversight & Partners** | 3 | External Auditor, Regulatory Authority, Sales Channel Partner |

**Total: 29 stakeholder profiles**

---

## Internal Stakeholders

---

### 1. Chief Executive Officer (CEO)

| Attribute | Detail |
|-----------|--------|
| **Name** | Chief Executive Officer (CEO) |
| **Responsibilities** | Sets company strategy; approves major investments; holds leadership accountable for growth, profitability, and operational risk; represents the company to board and investors |
| **Goals** | Protect revenue and margin; improve working capital efficiency; enable scalable growth; build market reputation for reliable fulfillment; reduce operational risk from inventory mismanagement |
| **Pain Points** | Cannot trust inventory data for strategic decisions; growth constrained by operational uncertainty; capital tied up in excess or obsolete stock; customer complaints affecting brand; limited confidence to expand locations or channels |
| **Permissions** | Executive dashboard view (read-only); access to high-level inventory KPIs and summary reports; no day-to-day transaction permissions |
| **System Interactions** | Reviews executive inventory dashboards; monitors stock value, turnover, and stockout trends; receives periodic performance summaries; uses data to support board reporting and growth decisions |

---

### 2. Chief Operating Officer (COO)

| Attribute | Detail |
|-----------|--------|
| **Name** | Chief Operating Officer (COO) |
| **Responsibilities** | Oversees end-to-end operations including warehousing, fulfillment, and supply coordination; drives operational efficiency; aligns operations with business strategy |
| **Goals** | Achieve high order fill rates; reduce fulfillment cycle time; standardize processes across locations; improve inventory accuracy; scale operations without proportional cost increase |
| **Pain Points** | Inconsistent processes across warehouses; no single view of network-wide stock; firefighting stockouts and overstock situations; difficulty measuring location performance; operational escalations consume leadership time |
| **Permissions** | Full read access across all locations; approve high-value adjustments and transfers; configure operational policies; access all operational and performance reports |
| **System Interactions** | Monitors network inventory health; reviews fulfillment performance and exceptions; approves major transfers and policy changes; uses reports to drive operational improvement initiatives |

---

### 3. Chief Financial Officer (CFO)

| Attribute | Detail |
|-----------|--------|
| **Name** | Chief Financial Officer (CFO) |
| **Responsibilities** | Manages financial health; oversees working capital; ensures accurate financial reporting; approves capital allocation; partners with operations on cost control |
| **Goals** | Reduce inventory carrying cost; improve inventory turnover; align stock investment with sales; minimize write-offs and shrinkage; support accurate balance sheet valuation |
| **Pain Points** | Inventory numbers on financial reports do not match operational reality; unexpected write-offs; cash trapped in slow-moving stock; difficulty forecasting working capital needs; weak audit trail for inventory changes |
| **Permissions** | Read access to inventory valuation reports, movement history, adjustment logs, and shrinkage reports; no transaction permissions |
| **System Interactions** | Reviews inventory valuation and aging reports; analyzes shrinkage and write-off trends; uses data for working capital planning; supports month-end and audit processes with inventory records |

---

### 4. Internal Auditor

| Attribute | Detail |
|-----------|--------|
| **Name** | Internal Auditor |
| **Responsibilities** | Evaluates internal controls; verifies compliance with company policies; investigates discrepancies; reports control weaknesses to audit committee |
| **Goals** | Ensure inventory controls are effective; verify transaction integrity; identify fraud or process failure risks; support clean internal and external audits |
| **Pain Points** | Incomplete or untraceable inventory records; manual overrides without documentation; inability to reconstruct who changed what and when; weak segregation of duties |
| **Permissions** | Read-only access to full audit trail, transaction history, user activity logs, adjustment records, and count variance reports; no create, edit, or delete permissions |
| **System Interactions** | Reviews audit logs and transaction histories; samples inventory movements for control testing; investigates variances and unauthorized adjustments; produces audit findings and recommendations |

---

### 5. Operations Director

| Attribute | Detail |
|-----------|--------|
| **Name** | Operations Director |
| **Responsibilities** | Manages day-to-day operational performance across warehouses and fulfillment; sets operational standards; resolves escalations; coordinates with purchasing and sales |
| **Goals** | Maintain inventory accuracy above target threshold; minimize stockouts on priority SKUs; optimize stock distribution across locations; reduce manual reconciliation effort |
| **Pain Points** | Fragmented data across locations; constant escalations from sales about unavailable stock; time spent reconciling spreadsheets; uneven performance between warehouse teams |
| **Permissions** | Full read/write access across assigned locations; approve adjustments, transfers, and count variances; manage user assignments for warehouse teams; configure location settings |
| **System Interactions** | Daily review of stock levels, alerts, and fulfillment queues; approves transfers and adjustments; monitors count schedules and accuracy metrics; coordinates with purchasing on replenishment needs |

---

### 6. Warehouse Manager

| Attribute | Detail |
|-----------|--------|
| **Name** | Warehouse Manager |
| **Responsibilities** | Runs daily warehouse operations at a specific location; supervises receiving, storage, picking, packing, and shipping; ensures safety and productivity; accountable for location inventory accuracy |
| **Goals** | Accurate stock records at their location; efficient pick and ship cycles; minimal count variances; well-organized stock placement; motivated and productive team |
| **Pain Points** | System stock does not match physical stock; pickers waste time locating items; receiving delays not reflected in system; pressure from sales for unavailable products; blame for errors caused upstream |
| **Permissions** | Full operational access within assigned warehouse; create receipts, transfers, adjustments, and fulfillments; approve cycle count results; manage warehouse staff user accounts; view location reports |
| **System Interactions** | Processes inbound receipts; assigns and monitors pick lists; approves stock count variances; initiates transfers to/from other locations; reviews daily movement and exception reports |

---

### 7. Receiving Clerk

| Attribute | Detail |
|-----------|--------|
| **Name** | Receiving Clerk |
| **Responsibilities** | Accepts inbound shipments; verifies quantity and condition against delivery documents; records received goods; flags discrepancies, damage, or wrong items |
| **Goals** | Fast and accurate receiving; clear visibility of expected inbound shipments; minimal rework from recording errors; immediate update of stock upon receipt |
| **Pain Points** | Expected deliveries not visible in system; manual paperwork parallel to system entry; disputes with suppliers over quantities; delays when supervisor approval is needed for discrepancies |
| **Permissions** | Create goods receipt transactions at assigned location; view expected inbound orders; record quantity variances and damage; cannot approve adjustments or delete records |
| **System Interactions** | Logs inbound receipts against purchase orders; records quantity received vs. expected; flags damaged or short shipments; searches products by SKU or barcode during receiving |

---

### 8. Warehouse Picker / Packer

| Attribute | Detail |
|-----------|--------|
| **Name** | Warehouse Picker / Packer |
| **Responsibilities** | Picks items for outbound orders; packs and prepares shipments; confirms picked quantities; reports stock not found or damaged during pick |
| **Goals** | Clear pick lists with accurate locations; fast picking with minimal errors; immediate confirmation of completed picks; easy way to report exceptions |
| **Pain Points** | Pick list shows stock that is not on shelf; unclear product location; system slow or confusing during high-volume periods; blamed for stockouts that are system errors |
| **Permissions** | View pick lists and order details for assigned tasks; confirm picks and packing completion; report pick exceptions (short pick, damaged item); no access to adjustments, transfers, or configuration |
| **System Interactions** | Views assigned pick lists; scans or selects products during pick; confirms quantities picked; marks orders as packed; reports unable-to-pick situations |

---

### 9. Inventory Controller

| Attribute | Detail |
|-----------|--------|
| **Name** | Inventory Controller |
| **Responsibilities** | Owns inventory accuracy program; schedules and oversees cycle counts; investigates variances; maintains product master data integrity; defines reorder levels and stock policies |
| **Goals** | Achieve and sustain high inventory record accuracy; timely resolution of variances; reliable product and location master data; effective count program across all locations |
| **Pain Points** | Chronic discrepancies without root cause; product data inconsistencies across locations; count schedules not adhered to; adjustments made without proper reason codes; no single owner of data quality |
| **Permissions** | Full read access across all locations; create and approve count schedules; approve count adjustments; maintain product master records and reorder parameters; generate accuracy and variance reports |
| **System Interactions** | Schedules and monitors cycle counts; reviews and approves count variances; maintains product catalog and stock thresholds; investigates discrepancy patterns; produces inventory accuracy reports |

---

### 10. Regional / Store Manager

| Attribute | Detail |
|-----------|--------|
| **Name** | Regional / Store Manager |
| **Responsibilities** | Manages retail store or regional group of locations; accountable for local sales, customer experience, and store-level stock; coordinates with warehouse for replenishment |
| **Goals** | Shelves stocked with right products; minimal customer-facing stockouts; balanced stock levels without excess; visibility into inbound transfers and replenishment |
| **Pain Points** | Store shows in-stock in system but shelf is empty; excess stock at one store while another stockouts; slow transfer requests; no visibility into when replenishment will arrive |
| **Permissions** | Read access for assigned store(s); request stock transfers; view inbound shipment status; initiate local cycle counts; limited adjustment permissions with approval |
| **System Interactions** | Checks local stock levels and availability; requests transfers from warehouse; monitors low-stock alerts; reviews inbound replenishment status; participates in store-level counts |

---

### 11. Sales Manager

| Attribute | Detail |
|-----------|--------|
| **Name** | Sales Manager |
| **Responsibilities** | Leads sales team performance; sets targets; ensures sales commitments align with supply capability; escalates fulfillment issues; coordinates with operations on product availability |
| **Goals** | Accurate stock availability for sales commitments; high order win rate without overpromising; visibility into backorder risk; data to support sales planning and promotions |
| **Pain Points** | Sales team promises delivery dates without knowing real stock; lost deals due to perceived unavailability; no visibility across locations for large orders; promotions fail due to insufficient stock |
| **Permissions** | Read access to available-to-promise (ATP) inventory across all locations; view order fulfillment status; access stockout and low-stock reports; no transaction permissions |
| **System Interactions** | Checks product availability before confirming large orders; monitors fulfillment status of key accounts; reviews stock levels for promotional planning; escalates stockout risks to operations |

---

### 12. Sales Representative

| Attribute | Detail |
|-----------|--------|
| **Name** | Sales Representative |
| **Responsibilities** | Engages B2B customers; creates quotes and orders; communicates delivery expectations; follows up on order status; identifies upsell opportunities |
| **Goals** | Quickly confirm product availability to customers; provide reliable delivery dates; avoid order cancellations; access real-time stock without calling warehouse |
| **Pain Points** | Must call warehouse to check stock; customer told product is available but order fails; embarrassed by delivery delays; no visibility into which location can fulfill fastest |
| **Permissions** | Read-only access to product availability (ATP) by location; view status of own customers' orders; no access to costs, adjustments, or internal movement details |
| **System Interactions** | Searches product availability before quoting; checks order fulfillment progress; identifies alternative locations with stock; communicates expected ship dates to customers |

---

### 13. Customer Service Representative

| Attribute | Detail |
|-----------|--------|
| **Name** | Customer Service Representative |
| **Responsibilities** | Handles customer inquiries, complaints, and order status requests; coordinates with warehouse on fulfillment issues; processes returns and replacements at intake level |
| **Goals** | Answer "where is my order?" instantly; proactively inform customers of delays; resolve stock-related complaints quickly; reduce call handling time |
| **Pain Points** | No real-time order or stock visibility; must email warehouse for status; customers receive conflicting information; cannot explain why item is backordered |
| **Permissions** | Read access to order fulfillment status and product availability; view shipment and reservation details; initiate return intake records; no adjustment or configuration access |
| **System Interactions** | Looks up order status and fulfillment progress; checks product availability for replacement orders; views reservation and backorder details; logs customer-facing issue notes |

---

### 14. Marketing Manager

| Attribute | Detail |
|-----------|--------|
| **Name** | Marketing Manager |
| **Responsibilities** | Plans promotions, campaigns, and product launches; coordinates timing with operations and purchasing; ensures marketed products are available |
| **Goals** | Confidence that promoted products are adequately stocked; visibility into launch inventory readiness; avoid customer disappointment from campaigns |
| **Pain Points** | Promotions launched without stock confirmation; no early warning of insufficient inventory for campaigns; disconnect between marketing calendar and replenishment |
| **Permissions** | Read-only access to stock levels for promoted SKUs; view inbound replenishment for campaign products; access stockout risk reports; no transaction permissions |
| **System Interactions** | Reviews stock readiness before campaign launch; monitors inventory levels during promotions; coordinates with purchasing on pre-promotion stock build-up |

---

### 15. Purchasing Manager

| Attribute | Detail |
|-----------|--------|
| **Name** | Purchasing Manager |
| **Responsibilities** | Oversees procurement strategy; manages supplier relationships; approves purchase orders; aligns purchasing with demand and inventory policy |
| **Goals** | Right products ordered at right time and quantity; reduced emergency purchases; reliable inbound visibility; optimized order frequency and order sizes |
| **Pain Points** | Reactive ordering based on gut feel; no trust in reorder suggestions; unaware of inbound stock already on order; over-purchasing slow movers while understocking fast movers |
| **Permissions** | Full read access to inventory levels, movement history, and replenishment reports across all locations; create purchase requisitions; view and track inbound orders; configure reorder parameters (with approval) |
| **System Interactions** | Reviews low-stock alerts and replenishment suggestions; creates purchase requisitions; monitors inbound shipment status; analyzes consumption trends for purchasing decisions |

---

### 16. Buyer / Procurement Officer

| Attribute | Detail |
|-----------|--------|
| **Name** | Buyer / Procurement Officer |
| **Responsibilities** | Executes day-to-day purchasing; places orders with suppliers; tracks deliveries; resolves supplier discrepancies; maintains supplier item catalogs |
| **Goals** | Timely order placement; accurate tracking of open purchase orders; quick resolution of receipt discrepancies; avoid duplicate ordering |
| **Pain Points** | Unclear what is already on order; duplicate POs for same product; supplier delivery delays not visible to operations; manual follow-up on every open order |
| **Permissions** | Create and manage purchase orders; view inventory levels and replenishment alerts; view receipt status and discrepancies; read movement history for assigned product categories |
| **System Interactions** | Creates purchase orders from replenishment suggestions; tracks expected inbound deliveries; reviews receiving discrepancies; checks stock before placing emergency orders |

---

### 17. Finance Manager / Accountant

| Attribute | Detail |
|-----------|--------|
| **Name** | Finance Manager / Accountant |
| **Responsibilities** | Records inventory value in financial systems; performs month-end close; reconciles inventory accounts; analyzes cost of goods and shrinkage |
| **Goals** | Accurate inventory valuation; timely month-end reconciliation; clear documentation for adjustments and write-offs; alignment between operational and financial records |
| **Pain Points** | Operational inventory data does not match GL; manual reconciliation every month-end; adjustments without financial justification; surprise shrinkage entries |
| **Permissions** | Read access to inventory valuation reports, adjustment logs, write-off records, and movement summaries; export data for financial reconciliation; no operational transaction permissions |
| **System Interactions** | Extracts inventory valuation data for financial posting; reviews adjustment and write-off reports; reconciles system inventory value with general ledger; supports audit with inventory records |

---

### 18. Project Sponsor

| Attribute | Detail |
|-----------|--------|
| **Name** | Project Sponsor |
| **Responsibilities** | Champions the IMS initiative; secures budget and resources; removes organizational blockers; accountable for project success and business adoption |
| **Goals** | On-time, on-budget delivery of business value; strong user adoption; measurable improvement in inventory KPIs; organizational alignment around the new system |
| **Pain Points** | Competing priorities across departments; resistance to process change; difficulty demonstrating ROI early; scope creep threatening delivery |
| **Permissions** | Executive-level read access to project status and system dashboards; no operational transaction permissions; authority to approve scope and policy decisions |
| **System Interactions** | Reviews project milestones and adoption metrics; monitors early KPI improvements; participates in go/no-go decisions; communicates progress to executive team |

---

### 19. Product Owner

| Attribute | Detail |
|-----------|--------|
| **Name** | Product Owner |
| **Responsibilities** | Defines and prioritizes product backlog; represents stakeholder needs; accepts delivered features; balances scope, value, and timeline |
| **Goals** | Deliver highest-value features first; ensure product solves real business problems; maintain alignment between vision and delivered capabilities; drive user adoption through relevant functionality |
| **Pain Points** | Conflicting stakeholder priorities; pressure to add out-of-scope features; gap between business expectations and delivery capacity; insufficient user feedback during development |
| **Permissions** | Full read access to all system areas for validation; configure test environments; manage feature acceptance; no production data modification outside of UAT |
| **System Interactions** | Validates features against acceptance criteria; reviews user feedback and defect reports; prioritizes enhancements; demos capabilities to stakeholders |

---

### 20. Business Analyst

| Attribute | Detail |
|-----------|--------|
| **Name** | Business Analyst |
| **Responsibilities** | Elicits and documents requirements; facilitates stakeholder workshops; maps business processes; validates that delivered solution meets business needs |
| **Goals** | Complete and unambiguous requirements; stakeholder alignment; traceability from business problems to features; smooth UAT and change management |
| **Pain Points** | Hidden requirements from disengaged stakeholders; undocumented tribal processes; late discovery of integration needs; conflicting process definitions across locations |
| **Permissions** | Read access across all modules for analysis and documentation; access to UAT environment; no production transaction permissions |
| **System Interactions** | Documents as-is and to-be processes; creates user stories and acceptance criteria; facilitates UAT sessions; produces training materials and process guides |

---

### 21. System Administrator

| Attribute | Detail |
|-----------|--------|
| **Name** | System Administrator |
| **Responsibilities** | Manages user accounts and role assignments; configures system settings; monitors system health; supports access requests and security policies |
| **Goals** | Secure, well-governed system access; minimal downtime; proper role-based access control; efficient onboarding and offboarding of users |
| **Pain Points** | Ad-hoc access requests without clear role definitions; users sharing credentials; orphaned accounts after staff turnover; unclear permission model across locations |
| **Permissions** | Full administrative access: user management, role configuration, system settings, audit log access, backup and maintenance functions; no routine inventory transactions |
| **System Interactions** | Creates and deactivates user accounts; assigns roles and location permissions; configures notification rules and system parameters; monitors audit logs for security events |

---

## External Stakeholders

---

### 22. Supplier / Vendor

| Attribute | Detail |
|-----------|--------|
| **Name** | Supplier / Vendor |
| **Responsibilities** | Provides products per agreed terms; fulfills purchase orders; delivers on schedule; resolves quantity and quality disputes; maintains product catalog information |
| **Goals** | Clear, timely purchase orders; predictable receiving process; quick resolution of delivery discrepancies; long-term supply partnership |
| **Pain Points** | Unclear or changing orders; receiving rejects without timely communication; payment delays linked to receipt disputes; no visibility into customer's stock levels (for VMI scenarios) |
| **Permissions** | No direct system access in MVP; future optional supplier portal for PO acknowledgment and shipment notices (read-only on their orders) |
| **System Interactions** | Receives purchase orders from buyers (outside system or via email/EDI); delivers goods to warehouse; referenced in receiving transactions; delivery performance tracked in system records |

---

### 23. Logistics / Carrier Partner

| Attribute | Detail |
|-----------|--------|
| **Name** | Logistics / Carrier Partner |
| **Responsibilities** | Transports goods between supplier, warehouse, and customer; provides tracking information; meets delivery service levels |
| **Goals** | Accurate shipment manifests; efficient pickup and delivery scheduling; clear delivery instructions; minimal failed deliveries |
| **Pain Points** | Incorrect shipment quantities on manifests; delivery attempted when customer/order not ready; lack of shipment status integration |
| **Permissions** | No direct system access in MVP; future integration for shipment tracking updates |
| **System Interactions** | Picks up packed orders from warehouse; provides tracking numbers recorded in fulfillment; delivery status may be updated manually or via future integration |

---

### 24. Freight Forwarder

| Attribute | Detail |
|-----------|--------|
| **Name** | Freight Forwarder |
| **Responsibilities** | Coordinates international or bulk inbound shipments; manages customs documentation; consolidates shipments from multiple suppliers |
| **Goals** | Accurate shipment documentation; clear expected arrival dates; efficient customs clearance; coordinated delivery to warehouse |
| **Pain Points** | Warehouse not prepared for large inbound deliveries; documentation mismatches causing receiving delays; no visibility into expected arrival for planning |
| **Permissions** | No direct system access; shipment details communicated to purchasing and receiving teams |
| **System Interactions** | Provides shipment and ETA information to buyers; inbound shipments recorded as expected receipts; receiving clerk processes arrival in system |

---

### 25. B2B Customer

| Attribute | Detail |
|-----------|--------|
| **Name** | B2B Customer (Business Buyer) |
| **Responsibilities** | Places bulk or recurring orders; negotiates terms; expects reliable delivery; manages their own inventory planning based on supplier performance |
| **Goals** | Accurate availability information; reliable delivery commitments; order status transparency; consistent product supply for their operations |
| **Pain Points** | Told product is available but order is backordered; unpredictable lead times; no self-service order tracking; partial shipments without notice |
| **Permissions** | No direct IMS access; interacts through sales and customer service channels; future B2B portal may provide order and availability visibility |
| **System Interactions** | Places orders via sales team; receives fulfillment and delivery updates; indirectly affected by inventory accuracy, reservation, and pick/ship processes |

---

### 26. B2C Customer

| Attribute | Detail |
|-----------|--------|
| **Name** | B2C Customer (Retail Consumer) |
| **Responsibilities** | Purchases products for personal use; expects accurate online or in-store availability; expects timely delivery or pickup |
| **Goals** | Product available when ordered; accurate delivery estimates; minimal cancellations; easy returns if needed |
| **Pain Points** | Website shows in-stock but order is cancelled; delayed shipping without explanation; store visit wasted when shelf is empty despite online availability |
| **Permissions** | No direct IMS access; experiences inventory accuracy through e-commerce, store, and customer service |
| **System Interactions** | Views product availability on sales channels (fed by IMS data); places orders processed against inventory reservations; receives shipment notifications |

---

### 27. External Auditor

| Attribute | Detail |
|-----------|--------|
| **Name** | External Auditor |
| **Responsibilities** | Independently verifies financial statements; tests internal controls over inventory; issues audit opinion; identifies material misstatements |
| **Goals** | Sufficient evidence of inventory existence and valuation; effective controls over inventory movements; complete and tamper-evident audit trail |
| **Pain Points** | Cannot rely on inventory records; insufficient documentation for sample testing; control weaknesses in count and adjustment processes |
| **Permissions** | Temporary read-only access to inventory reports, count records, adjustment logs, and audit trail during audit period; no transaction permissions |
| **System Interactions** | Reviews inventory valuation reports; tests cycle count results against records; samples transaction history; evaluates control design and operating effectiveness |

---

### 28. Regulatory Authority

| Attribute | Detail |
|-----------|--------|
| **Name** | Regulatory Authority |
| **Responsibilities** | Enforces industry regulations related to product traceability, safety, or reporting (if applicable); conducts inspections; issues compliance requirements |
| **Goals** | Demonstrable product traceability; compliant record-keeping; timely reporting when required; evidence of recall capability |
| **Pain Points** | Not applicable in current scope unless company enters regulated product categories; would require lot/batch traceability and regulatory reporting |
| **Permissions** | No standing system access; may request data exports or reports during inspections |
| **System Interactions** | Minimal in current scope; future interaction if regulated products require lot tracking, expiry management, or mandatory reporting from IMS records |

---

### 29. Sales Channel Partner

| Attribute | Detail |
|-----------|--------|
| **Name** | Sales Channel Partner (Marketplace / Reseller) |
| **Responsibilities** | Sells company products through external platforms; expects accurate stock feeds; processes orders routed to company fulfillment |
| **Goals** | Real-time or near-real-time stock synchronization; minimal order cancellations due to stock errors; reliable fulfillment SLAs |
| **Pain Points** | Overselling due to stale inventory feeds; order cancellations damage partner ratings; no visibility into fulfillment status |
| **Permissions** | No direct IMS access in MVP; future API or integration access for stock levels and order routing (read stock, submit orders) |
| **System Interactions** | Receives inventory availability feeds (future integration); sends orders for fulfillment; expects reservation and shipment confirmation |

---

## Stakeholder Influence & Interest Matrix

```
                    HIGH INFLUENCE
                         │
    Manage Closely       │       Keep Satisfied
    ─────────────────────┼──────────────────────
    • CEO                │    • CFO
    • COO                │    • External Auditor
    • Project Sponsor    │    • Regulatory Authority
    • Operations Director│
    • Product Owner      │
    • Warehouse Manager  │
    • Purchasing Manager │
    ─────────────────────┼──────────────────────
    Keep Informed        │       Monitor
                         │
    • Sales Manager      │    • B2C Customer
    • Sales Rep          │    • Freight Forwarder
    • Customer Service   │    • Sales Channel Partner
    • Marketing Manager  │
    • Regional Manager   │
    • Finance Accountant │
    • Inventory Control  │
    • Business Analyst   │
    • System Admin       │
    • Receiving Clerk    │
    • Picker/Packer      │
    • Buyer              │
    • B2B Customer       │
    • Supplier           │
    • Carrier Partner    │
                         │
                    LOW INFLUENCE

         LOW INTEREST ────────────── HIGH INTEREST
```

---

## Stakeholder-to-Feature Mapping

| Stakeholder | Primary System Features Used |
|-------------|------------------------------|
| CEO / CFO | Executive dashboards, inventory valuation, KPI reports |
| COO / Operations Director | Network stock view, fulfillment monitoring, transfer approval |
| Warehouse Manager | Receiving, picking, counts, adjustments, location reports |
| Receiving Clerk | Goods receipt, inbound PO matching, discrepancy logging |
| Picker / Packer | Pick lists, pick confirmation, exception reporting |
| Inventory Controller | Cycle counts, product master, reorder levels, accuracy reports |
| Regional / Store Manager | Local stock view, transfer requests, replenishment status |
| Sales Manager / Rep | ATP availability, order status, stockout reports |
| Customer Service | Order fulfillment status, availability lookup, return intake |
| Marketing Manager | Campaign SKU stock levels, inbound replenishment view |
| Purchasing Manager / Buyer | Low-stock alerts, replenishment suggestions, PO tracking |
| Finance / Accountant | Valuation reports, adjustment logs, export for reconciliation |
| Internal / External Auditor | Audit trail, transaction history, count records |
| System Administrator | User management, roles, system configuration |
| Supplier | PO receipt (indirect), delivery performance (tracked) |
| B2B / B2C Customer | Availability and fulfillment (indirect via sales channels) |
| Carrier / Channel Partner | Shipment and stock sync (indirect / future integration) |

---

## Key Stakeholder Dependencies

| Dependency | From | To | Nature |
|------------|------|----|--------|
| Stock availability for sales | Operations / Warehouse | Sales / Customer Service | Sales depends on accurate IMS data |
| Replenishment timing | Inventory Controller | Purchasing | Reorder levels drive purchase decisions |
| Inbound processing | Supplier | Receiving Clerk | Deliveries must be recorded to update stock |
| Financial reconciliation | IMS records | Finance | Inventory movements must align with GL |
| Fulfillment execution | Picker / Packer | Customer Service / Customer | Pick confirmation drives order status |
| Product data quality | Inventory Controller | All operational users | Bad master data affects all transactions |
| User access provisioning | HR / Operations | System Administrator | Staff changes drive account management |
| Campaign readiness | Purchasing / Warehouse | Marketing | Stock must be in place before promotions |

---

## Document Summary

This analysis identifies **29 stakeholders** across internal operations, commercial, finance, governance, technology, and external supply chain and customer groups. Each stakeholder has distinct responsibilities, goals, pain points, permission needs, and system interaction patterns.

Primary system users with daily transactional interaction: **Receiving Clerk, Picker/Packer, Warehouse Manager, Inventory Controller, Buyer, and Customer Service Representative**.

Primary decision-makers relying on reports and dashboards: **CEO, COO, CFO, Operations Director, Purchasing Manager, and Sales Manager**.

Governance and oversight stakeholders requiring audit access: **Internal Auditor, External Auditor, and Finance Manager**.

External parties impacted indirectly or through future integration: **Suppliers, Carriers, B2B/B2C Customers, and Sales Channel Partners**.

This stakeholder map should guide requirements prioritization, role-based access design, training plans, and change management activities in subsequent project phases.

---

*End of Stakeholder Analysis Document*
