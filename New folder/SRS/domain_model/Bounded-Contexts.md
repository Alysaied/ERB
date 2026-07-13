# Bounded Contexts
## Inventory Management System

---

## Document Information

| Attribute | Detail |
|-----------|--------|
| **Document ID** | SRS-DM-007 |
| **Document Title** | Bounded Contexts — Inventory Management System |
| **Version** | 1.0 |
| **Status** | Draft |
| **Document Owner** | DDD Solution Architect |
| **Source Documents** | BRD-IMS-001 (v1.0), SRS-DM-001 through SRS-DM-006, SRS-UC-001 (Use Case Catalog), SRS-BR-001 (Business Rules) |
| **Date** | July 5, 2026 |
| **Scope** | Strategic domain decomposition only — no microservice deployment, API design, or database partitioning |

### Purpose

This document defines the **Bounded Contexts** of the Inventory Management System — the explicit boundaries within which a domain model is unified, internally consistent, and expressed in a distinct ubiquitous language. Each context owns its aggregates and entities, exposes well-defined relationships to neighboring contexts, and can evolve independently without corrupting models in adjacent domains.

Bounded contexts are a **strategic design** decision. They reflect how the business organizes inventory capability — not necessarily how software is deployed in the first release.

### Context Map Legend

| Relationship | Meaning in IMS |
|--------------|----------------|
| **Upstream → Downstream** | Upstream context defines the model; downstream conforms or translates |
| **Shared Kernel** | Small shared model both contexts depend on (minimal, stable identifiers) |
| **Customer-Supplier** | Downstream (customer) negotiates needs with upstream (supplier) context |
| **Conformist** | Downstream accepts upstream model without translation |
| **Anti-Corruption Layer (ACL)** | Downstream translates foreign model to protect its own integrity |
| **Open Host Service (OHS)** | Context publishes a well-defined interface for others to consume |
| **Published Language** | Shared interchange format (e.g., SKU + Location Code identifiers) |

---

## Context Overview

| # | Bounded Context | Aggregates Owned | Primary Business Processes |
|---|-----------------|------------------|----------------------------|
| 1 | Product Catalog | Product Catalog | BP-01, BP-04 |
| 2 | Warehouse Network | Inventory Location | BP-02 |
| 3 | Inventory Governance | Inventory Governance | BP-01, BP-03, BP-32 |
| 4 | Inventory Balance | Stock Position, Stock Policy | BP-03, BP-10, BP-21 |
| 5 | Procurement & Supplier | Supplier, Purchase Requisition, Purchase Order | BP-05, BP-06, BP-22, BP-23 |
| 6 | Inbound Receiving | Goods Receipt, Supplier Invoice | BP-07, BP-08, BP-09, BP-30 |
| 7 | Order Fulfillment | Customer Order Fulfillment | BP-16 – BP-20 |
| 8 | Network Transfer | Stock Transfer | BP-24 – BP-26 |
| 9 | Inventory Accuracy | Cycle Count, Physical Inventory Count, Inventory Adjustment Case | BP-11 – BP-15 |
| 10 | Returns Management | Customer Return Case | BP-27, BP-28 |
| 11 | Commercial Campaign | Promotional Stock Allocation | BP-31 |
| 12 | Identity & Access | User Account | Cross-cutting |
| 13 | Inventory Intelligence | *(Read models — no write aggregates)* | BP-29, BP-30, BP-32 |

**Total Bounded Contexts:** 13

---

## Context 1: Product Catalog

### Business Responsibility

Maintain the authoritative product identity catalog — SKU definitions, lifecycle status, classification (ABC), rotation and traceability attributes — that all other inventory contexts reference when identifying *what* is being bought, held, counted, or sold.

### Owned Entities

| Entity / Aggregate | Role in Context |
|--------------------|-----------------|
| **Product** *(aggregate root)* | SKU master, lifecycle, ABC class, rotation policy, traceability rules |
| Product Identifier, Product Category, Product Lifecycle Status, ABC Classification, Rotation Policy, Shelf Life Profile *(value objects)* | Embedded catalog attributes |

### Related Use Cases

| Use Case | Name |
|----------|------|
| UC-001 | Manage Product Master Data |
| UC-004 | Classify Products by ABC Priority |
| UC-046 | Import Initial Product and Stock Master Data *(product portion)* |

### Relationships with Other Contexts

| Related Context | Relationship | Integration |
|-----------------|--------------|-------------|
| Inventory Balance | **Upstream → Downstream** (Product Catalog supplies) | Product SKU referenced by Stock Position and Stock Policy; Product Transaction Eligibility validates lifecycle before transactions |
| Procurement & Supplier | **Upstream → Downstream** | PO and requisition lines reference SKU; discontinued status blocks new orders |
| Order Fulfillment | **Upstream → Downstream** | Order lines reference SKU; inactive/discontinued products blocked from reservation |
| Inbound Receiving | **Upstream → Downstream** | Receipt verification validates product identity and MRSL policy |
| Inventory Accuracy | **Upstream → Downstream** | Cycle count scoped by product; ABC class drives count frequency |
| Inventory Intelligence | **Open Host Service** | Product catalog published for reporting and search |

### Why This Context Should Be Independent

Product master data changes **infrequently** and is owned by the **Inventory Controller** function, while stock quantities change **continuously** in warehouse operations. Merging catalog and balance into one model causes high-frequency transactional code to couple with low-frequency master data governance. Product lifecycle rules (discontinued, ABC) are assortment decisions — not warehouse execution decisions. Independent evolution allows catalog enrichment (attributes, classification) without redeploying fulfillment or receiving logic.

---

## Context 2: Warehouse Network

### Business Responsibility

Define and manage the inventory location network — warehouses, stores, distribution points, storage positions, hierarchy, operational status, and location lifecycle (go-live, closure) — that anchors all stock to physical places.

### Owned Entities

| Entity / Aggregate | Role in Context |
|--------------------|-----------------|
| **Inventory Location** *(aggregate root)* | Location master, hierarchy, status, freeze state |
| **Storage Position** *(entity)* | Zone, aisle, bin within location |
| Physical Address, Location Type, Storage Position Address *(value objects)* | Location descriptors |

### Related Use Cases

| Use Case | Name |
|----------|------|
| UC-002 | Configure Inventory Locations |
| UC-046 | Import Initial Product and Stock Master Data *(location portion)* |
| UC-015 | Conduct Full Physical Inventory Count *(freeze enforcement)* |

### Relationships with Other Contexts

| Related Context | Relationship | Integration |
|-----------------|--------------|-------------|
| Inventory Balance | **Upstream → Downstream** | Stock Position anchored to Location Code; location must be active for transactions |
| Inbound Receiving | **Upstream → Downstream** | Receiving location and put-away storage positions |
| Order Fulfillment | **Upstream → Downstream** | Ship-from location; location freeze blocks shipment |
| Network Transfer | **Upstream → Downstream** | Source and destination locations |
| Inventory Accuracy | **Customer-Supplier** | Physical count imposes freeze on location; location context owns freeze state |
| Identity & Access | **Upstream → Downstream** | Role assignments scoped to location codes |

### Why This Context Should Be Independent

Location network structure is **organizational master data** — new warehouses, closures, and layout changes follow a different lifecycle and approval path than daily stock movements. Storage position configuration is a **facilities concern** distinct from quantity accounting. Location freeze during physical count (BR-024) is a network-wide operational control that must be authoritative without embedding freeze logic inside every transactional context. Separating network setup allows geographic expansion without modifying procurement or fulfillment domain models.

---

## Context 3: Inventory Governance

### Business Responsibility

Maintain organization-wide inventory control policies — reason codes, approval thresholds, tolerance limits, segregation-of-duties rules, and exception policies — that govern how operational contexts authorize adjustments, receipts, and financial controls.

### Owned Entities

| Entity / Aggregate | Role in Context |
|--------------------|-----------------|
| **Governance Policy** *(aggregate root)* | Approval thresholds, tolerances, effective periods |
| **Reason Code** *(entity)* | Standardized exception and adjustment taxonomy |
| Approval Threshold, Quantity Tolerance, Effective Period *(value objects)* | Policy parameters |

### Related Use Cases

| Use Case | Name |
|----------|------|
| UC-005 | Maintain Governance Policies and Reason Codes |
| UC-041 | Conduct Inventory Audit and Control Review *(policy compliance)* |
| UC-045 | Enforce Role-Based and Location-Scoped Access *(SoD rules)* |

### Relationships with Other Contexts

| Related Context | Relationship | Integration |
|-----------------|--------------|-------------|
| Inventory Accuracy | **Upstream → Downstream** | Adjustment and count approval consult governance thresholds and SoD rules |
| Inbound Receiving | **Upstream → Downstream** | Receipt tolerance and ad-hoc exception policies |
| Procurement & Supplier | **Upstream → Downstream** | Three-way match tolerance limits |
| Identity & Access | **Shared Kernel** *(SoD rules)* | Governance defines SoD constraints; Identity & Access enforces at role assignment |
| All operational contexts | **Open Host Service** | Published reason code catalog and policy lookup |

### Why This Context Should Be Independent

Governance policies are **enterprise control standards** set by operations leadership and audit — not warehouse floor concerns. They change on **audit cycles and policy reviews**, independent of daily receipts or shipments. Centralizing reason codes and thresholds prevents each operational context from embedding its own (potentially inconsistent) approval rules. When audit findings require threshold changes, only this context updates — all consumers re-evaluate against the new policy without model changes in fulfillment or receiving.

---

## Context 4: Inventory Balance

### Business Responsibility

Own the authoritative inventory quantity state — on-hand, reserved, available-to-promise (ATP), quarantine holds, lot/batch breakdown, and replenishment thresholds — answering *what do we have, where is it, and what is available?*

### Owned Entities

| Entity / Aggregate | Role in Context |
|--------------------|-----------------|
| **Stock Position** *(aggregate root)* | On-hand, reserved, ATP, ownership classification |
| **Stock Policy** *(aggregate root)* | Reorder level, minimum, safety stock, maximum thresholds |
| **Lot/Batch** *(entity)* | Traceable stock grouping within Stock Position |
| **Quarantine Hold** *(entity)* | Non-sellable hold within Stock Position |
| Stock Availability Breakdown, Stock Status Indicator, Ownership Classification *(value objects)* | Derived quantity states |

### Related Use Cases

| Use Case | Name |
|----------|------|
| UC-003 | Define Stock Policies and Thresholds |
| UC-012 | Monitor Inventory Status |
| UC-013 | Inquire Inventory Availability |
| UC-019 | Manage Quarantine and Hold Stock |
| UC-028 | Review Low-Stock and Out-of-Stock Alerts *(threshold source)* |

### Relationships with Other Contexts

| Related Context | Relationship | Integration |
|-----------------|--------------|-------------|
| Product Catalog | **Downstream (conformist)** | References Product SKU; conforms to lifecycle rules |
| Warehouse Network | **Downstream (conformist)** | References Location Code; respects freeze state |
| Order Fulfillment | **Customer-Supplier** | Fulfillment requests reservation/deduction; Balance context owns quantity |
| Inbound Receiving | **Customer-Supplier** | Receiving requests quantity increase after put-away |
| Network Transfer | **Customer-Supplier** | Transfer requests source deduction and destination increase |
| Inventory Accuracy | **Customer-Supplier** | Adjustments request quantity correction |
| Returns Management | **Customer-Supplier** | Restock requests quantity increase |
| Commercial Campaign | **Customer-Supplier** | Promotional allocation segregates ATP |
| Inventory Intelligence | **Upstream → Downstream** | Publishes quantity and status events for dashboards |

### Why This Context Should Be Independent

Inventory balance is the **system's core transactional state** — the highest-contention, highest-frequency domain. It has a distinct ubiquitous language: ATP, on-hand, reserved, quarantined — terms that mean nothing in procurement or catalog contexts. Separating balance from fulfillment prevents order lifecycle logic from corrupting quantity invariants (BR-001, BR-002, BR-013). Stock Policy belongs here because thresholds are evaluated against live quantities, even though policy *definition* is a planning act. Independent context enables the balance model to scale (per product-location aggregates) without dragging in PO or order models.

---

## Context 5: Procurement & Supplier

### Business Responsibility

Manage the inbound supply commitment lifecycle — supplier relationships, internal requisition approval, purchase order placement, and expected inbound delivery planning — authorizing *what the organization has committed to buy* before goods arrive.

### Owned Entities

| Entity / Aggregate | Role in Context |
|--------------------|-----------------|
| **Supplier** *(aggregate root)* | Supplier master, payment terms, consignment agreement |
| **Purchase Requisition** *(aggregate root)* | Internal replenishment request and approval |
| **Purchase Order** *(aggregate root)* | Commercial supplier commitment |
| **Expected Inbound Delivery** *(entity)* | Planned shipment schedule tied to PO |
| Purchase Order Line, Payment Terms, Lead Time Duration *(value objects)* | Procurement line details |

### Related Use Cases

| Use Case | Name |
|----------|------|
| UC-006 | Place and Manage Purchase Orders |
| UC-007 | Plan Expected Inbound Deliveries |
| UC-029 | Plan Replenishment and Create Purchase Requisitions |
| UC-030 | Track Inbound Supply Status |

### Relationships with Other Contexts

| Related Context | Relationship | Integration |
|-----------------|--------------|-------------|
| Product Catalog | **Downstream (conformist)** | PO lines reference SKU; respects discontinued status |
| Warehouse Network | **Downstream (conformist)** | PO specifies receiving location |
| Inventory Balance | **Downstream (ACL via domain service)** | Network Availability Evaluation before requisition; reads ATP network-wide |
| Inventory Governance | **Downstream (conformist)** | Ad-hoc receipt exception policies |
| Inbound Receiving | **Upstream → Downstream** | PO authorizes goods receipt |
| Inventory Intelligence | **Upstream → Downstream** | Open PO and inbound pipeline reporting |

### Why This Context Should Be Independent

Procurement speaks the language of **commercial commitment** — requisitions, POs, suppliers, lead times — distinct from warehouse language of receipt and put-away. Purchasing is owned by **Buyers and Purchasing Managers**; receiving is owned by **Receiving Clerks**. Commitment (PO placed) happens days or weeks before execution (goods arrive) — different timelines and consistency boundaries. BR-007 (PO required for receipt) establishes a clear handoff between contexts via domain events, not shared tables. Separating procurement allows PO workflow evolution (approval chains, supplier portals) without touching stock quantity logic.

---

## Context 6: Inbound Receiving

### Business Responsibility

Execute the inbound supply verification workflow — goods receipt, discrepancy documentation, put-away confirmation, and supplier invoice matching — governing *what was actually received and when it becomes available*.

### Owned Entities

| Entity / Aggregate | Role in Context |
|--------------------|-----------------|
| **Goods Receipt** *(aggregate root)* | Verification, receipt lines, put-away |
| **Receipt Discrepancy** *(entity)* | Documented receipt variance |
| **Put-Away** *(entity)* | Storage placement confirmation |
| **Supplier Invoice** *(aggregate root)* | Billing document and three-way match |
| Receipt Line Detail, Discrepancy Classification, Three-Way Match Result *(value objects)* | Receipt and match artifacts |

### Related Use Cases

| Use Case | Name |
|----------|------|
| UC-008 | Receive and Verify Supplier Goods |
| UC-009 | Document and Resolve Receipt Discrepancies |
| UC-010 | Perform Stock Put-Away |
| UC-011 | Receive Return and Non-PO Inbound Stock *(supplier/ad-hoc portion)* |
| UC-039 | Reconcile Inventory Valuation with Finance *(three-way match portion)* |

### Relationships with Other Contexts

| Related Context | Relationship | Integration |
|-----------------|--------------|-------------|
| Procurement & Supplier | **Downstream (conformist)** | Receipt must match PO; conforms to authorized quantities |
| Product Catalog | **Downstream (conformist)** | Product identity and MRSL validation at receipt |
| Warehouse Network | **Downstream (conformist)** | Receiving location and storage position assignment |
| Inventory Governance | **Downstream (conformist)** | Tolerance limits and reason codes for discrepancies |
| Inventory Balance | **Upstream → Downstream** | PutAwayCompleted event triggers StockReceived in Balance context |
| Inventory Intelligence | **Upstream → Downstream** | Receipt and match status for supplier performance reporting |

### Why This Context Should Be Independent

Receiving is **operational execution at the dock** — a distinct physical workflow from commercial PO creation. Its ubiquitous language centers on verification, discrepancy, put-away, and match — not on ATP or order reservation. BR-004, BR-005, and BR-006 form a cohesive receiving rule set that should not leak into procurement or balance models. Three-way match (Supplier Invoice) bridges to finance but originates from receipt facts — keeping it here maintains the PO→Receipt→Invoice accountability chain. Separation allows receiving workflows (mobile scanning, carrier integration) to evolve independently of PO management.

---

## Context 7: Order Fulfillment

### Business Responsibility

Manage the customer order fulfillment lifecycle — availability confirmation, reservation, pick/pack/ship, partial fulfillment, backorders, and fulfillment exceptions — governing *how customer demand consumes inventory*.

### Owned Entities

| Entity / Aggregate | Role in Context |
|--------------------|-----------------|
| **Customer Order** *(aggregate root)* | Order lines, fulfillment state |
| **Inventory Reservation** *(entity)* | Operational hold for order line |
| **Fulfillment Execution** *(entity)* | Pick, pack, verify workflow |
| **Backorder** *(entity)* | Customer-agreed delay for unfulfilled quantity |
| **Shipment** *(entity)* | Dispatch confirmation |
| Order Line Quantity, Fulfillment Quantity Breakdown, Customer Acknowledgment *(value objects)* | Fulfillment line states |

### Related Use Cases

| Use Case | Name |
|----------|------|
| UC-021 | Confirm Order Availability |
| UC-022 | Reserve Inventory for Confirmed Orders |
| UC-023 | Release Inventory Reservations |
| UC-024 | Pick, Pack, and Ship Orders |
| UC-025 | Handle Partial Fulfillment and Backorders |
| UC-026 | Handle Outbound Fulfillment Exceptions |
| UC-027 | View Order Fulfillment Status |
| UC-048 | Support Multi-Location Split Fulfillment |

### Relationships with Other Contexts

| Related Context | Relationship | Integration |
|-----------------|--------------|-------------|
| Inventory Balance | **Downstream (ACL via domain services)** | Reads ATP; commands reservation/deduction via events; does not own quantity |
| Product Catalog | **Downstream (conformist)** | Order lines reference SKU; respects product lifecycle |
| Warehouse Network | **Downstream (conformist)** | Ship-from location; respects location freeze |
| Commercial Campaign | **Downstream (conformist)** | Respects promotional ring-fence rules |
| Inventory Governance | **Downstream (conformist)** | Pick verification and exception policies |
| External Sales/CRM | **Upstream → Downstream (ACL)** | Customer order may originate externally; IMS holds fulfillment-relevant subset |
| Inventory Intelligence | **Upstream → Downstream** | Fulfillment status and fill rate metrics |
| Returns Management | **Upstream → Downstream** | Original order referenced for return authorization |

### Why This Context Should Be Independent

Fulfillment speaks the language of **customer commitment** — orders, reservations, picks, shipments, backorders — fundamentally different from procurement's supplier language or balance's quantity language. Fulfillment is owned by **Customer Service and Warehouse** teams with distinct peak load patterns from receiving. BR-001, BR-002, BR-003, and BR-028 form a cohesive fulfillment rule set. The BRD explicitly scopes full CRM/sales outside IMS — fulfillment context holds only what inventory needs via ACL from external order systems. Separating fulfillment prevents customer order lifecycle complexity from polluting the high-performance stock balance model.

---

## Context 8: Network Transfer

### Business Responsibility

Manage inter-location stock redistribution — transfer requests, approval, dispatch, in-transit tracking, and destination receipt — resolving network imbalance without new procurement.

### Owned Entities

| Entity / Aggregate | Role in Context |
|--------------------|-----------------|
| **Stock Transfer** *(aggregate root)* | Transfer lifecycle including request, approval, dispatch, receipt |
| **In-Transit Stock** *(entity)* | Pipeline quantity between locations |
| Transfer Line Detail, Quantity *(value objects)* | Transfer line artifacts |

*Note: Transfer Request is the initial state of the Stock Transfer aggregate — not a separate bounded context.*

### Related Use Cases

| Use Case | Name |
|----------|------|
| UC-031 | Request Inter-Location Stock Transfer |
| UC-032 | Approve or Reject Transfer Requests |
| UC-033 | Execute and Record Inter-Location Transfer |
| UC-034 | Analyze and Recommend Network Rebalancing *(initiates transfers)* |

### Relationships with Other Contexts

| Related Context | Relationship | Integration |
|-----------------|--------------|-------------|
| Inventory Balance | **Downstream (ACL via domain services)** | Transfer Capacity Evaluation reads source policy and ATP; TransferDispatched/Received events mutate Stock Positions |
| Warehouse Network | **Downstream (conformist)** | Source and destination location validation; freeze check |
| Product Catalog | **Downstream (conformist)** | Product and lot traceability on transfer lines |
| Procurement & Supplier | **Customer-Supplier** | Transfer alternative evaluated before new purchase (BR-011) |
| Inventory Intelligence | **Upstream → Downstream** | In-transit and network balance reporting |

### Why This Context Should Be Independent

Network transfer is a **distinct operational workflow** from both procurement (external supply) and fulfillment (customer demand). Its language — request, approve, dispatch, in-transit, receive — describes **internal redistribution**, not customer or supplier relationships. BR-011 and BR-012 are network-specific rules with no meaning in single-location fulfillment. In-transit stock is a pipeline state invisible to customer-facing ATP queries. Separating transfers allows network balancing algorithms and approval workflows to evolve without modifying PO or order models.

---

## Context 9: Inventory Accuracy

### Business Responsibility

Maintain inventory record accuracy through cycle counting, physical inventory counts, variance investigation, governed adjustments, and write-offs — ensuring *recorded stock reflects physical reality*.

### Owned Entities

| Entity / Aggregate | Role in Context |
|--------------------|-----------------|
| **Cycle Count** *(aggregate root)* | Scheduled partial counts |
| **Physical Inventory Count** *(aggregate root)* | Wall-to-wall count events |
| **Inventory Adjustment Case** *(aggregate root)* | Count variance, stock adjustment, write-off |
| Count Variance, Quantity Variance, Reason Code Attribution *(value objects)* | Variance and correction artifacts |

### Related Use Cases

| Use Case | Name |
|----------|------|
| UC-014 | Perform Cycle Count |
| UC-015 | Conduct Full Physical Inventory Count |
| UC-016 | Investigate and Approve Count Variances |
| UC-017 | Process Stock Adjustments |
| UC-018 | Authorize and Process Inventory Write-Offs |
| UC-020 | Analyze Shrinkage, Loss, and Obsolete Stock |

### Relationships with Other Contexts

| Related Context | Relationship | Integration |
|-----------------|--------------|-------------|
| Inventory Balance | **Customer-Supplier** | Approved adjustments command StockAdjusted/StockWrittenOff events; reads system quantity for variance |
| Warehouse Network | **Customer-Supplier** | Physical count imposes/releases location freeze |
| Inventory Governance | **Downstream (conformist)** | Reason codes, approval thresholds, SoD rules |
| Product Catalog | **Downstream (conformist)** | ABC classification drives count frequency |
| Identity & Access | **Downstream (conformist)** | Counter vs. approver SoD validation |
| Inventory Intelligence | **Upstream → Downstream** | Accuracy metrics, shrinkage trends |

### Why This Context Should Be Independent

Inventory accuracy is a **governance and quality discipline** — not daily execution. Its language — blind count, variance, investigation, adjustment, write-off, shrinkage — is foreign to fulfillment or procurement. Accuracy workflows enforce **segregation of duties** (BR-018, BR-019) that deliberately slow down corrections — opposite to the speed requirement of order fulfillment. Count-to-adjustment is a multi-step governed pipeline that must not be embedded in Stock Position (which should apply corrections quickly once authorized). Independent context allows audit and accuracy program maturity without disrupting transactional throughput.

---

## Context 10: Returns Management

### Business Responsibility

Manage reverse logistics — return authorization, physical return receipt, condition inspection, and disposition routing (restock, quarantine, write-off) — governing *how returned goods re-enter or exit inventory*.

### Owned Entities

| Entity / Aggregate | Role in Context |
|--------------------|-----------------|
| **Return Authorization** *(aggregate root)* | RMA and return eligibility |
| **Customer Return** *(entity)* | Physical return receipt |
| **Return Disposition** *(entity)* | Restock, quarantine, or write-off decision |
| Condition Grade, Disposition Decision *(value objects)* | Inspection outcomes |

### Related Use Cases

| Use Case | Name |
|----------|------|
| UC-035 | Authorize and Record Customer Returns |
| UC-036 | Receive, Inspect, and Disposition Returned Goods |
| UC-011 | Receive Return and Non-PO Inbound Stock *(return portion)* |

### Relationships with Other Contexts

| Related Context | Relationship | Integration |
|-----------------|--------------|-------------|
| Order Fulfillment | **Downstream (conformist)** | RMA validates against original customer order |
| Inbound Receiving | **Shared Kernel** *(receipt verification pattern)* | Similar verify-before-accept discipline; may share receipt workflow concepts |
| Inventory Balance | **Customer-Supplier** | Restock triggers StockReceived; quarantine triggers QuarantineHoldApplied |
| Inventory Accuracy | **Customer-Supplier** | Write-off disposition triggers Inventory Adjustment Case |
| Product Catalog | **Downstream (conformist)** | Returned product identity validation |
| Warehouse Network | **Downstream (conformist)** | Return receiving location |

### Why This Context Should Be Independent

Returns are **reverse logistics** with a distinct rule chain (BR-025 → BR-026 → disposition) and customer-facing authorization requirements unlike forward fulfillment or supplier receiving. Returns involve **Customer Service** (RMA) and **Quality** (inspection) stakeholders not central to outbound pick/pack. Conflating returns with inbound supplier receiving would blur fundamentally different accountability — supplier discrepancies vs. customer policy eligibility. Independent context allows return policy, inspection grading, and disposition rules to evolve with customer experience programs without affecting PO or order models.

---

## Context 11: Commercial Campaign

### Business Responsibility

Ring-fence inventory for promotional campaigns and product launches, protect allocated stock from non-promotional consumption, and support campaign readiness confirmation.

### Owned Entities

| Entity / Aggregate | Role in Context |
|--------------------|-----------------|
| **Promotional Stock Allocation** *(aggregate root)* | Campaign ring-fence, channel scope, readiness |
| Campaign Period, Channel Designation, Quantity *(value objects)* | Campaign parameters |

### Related Use Cases

| Use Case | Name |
|----------|------|
| UC-040 | Confirm Promotional and Launch Stock Readiness |
| UC-047 | Receive and Respond to Operational Notifications *(campaign readiness alerts)* |
| UC-022 | Reserve Inventory for Confirmed Orders *(must respect ring-fence per BR-029)* |

### Relationships with Other Contexts

| Related Context | Relationship | Integration |
|-----------------|--------------|-------------|
| Inventory Balance | **Customer-Supplier** | Allocation segregates ATP on Stock Position; released on campaign end |
| Product Catalog | **Downstream (conformist)** | Campaign SKUs reference product identity |
| Warehouse Network | **Downstream (conformist)** | Allocation scoped to fulfillment locations |
| Order Fulfillment | **Upstream → Downstream** | Fulfillment must check ring-fence before general reservation |
| Inventory Intelligence | **Upstream → Downstream** | Campaign readiness dashboards |
| External Marketing | **Upstream → Downstream (ACL)** | Campaign plans may originate in marketing systems |

### Why This Context Should Be Independent

Commercial campaign management speaks the language of **marketing commitments** — campaigns, launches, channels, readiness — not warehouse or procurement language. It is owned by **Marketing and Commercial** leadership with seasonal/event-driven cycles unrelated to daily replenishment. BR-029 (promotional ring-fencing) is a commercial policy overlay on stock availability that general fulfillment should not own. Phase 2 scope in the BRD confirms this is a distinct maturity capability. Independent context allows campaign tooling integration without modifying core balance or fulfillment aggregates.

---

## Context 12: Identity & Access

### Business Responsibility

Manage user identity, role assignments, location-scoped permissions, and segregation-of-duties enforcement for all inventory operations — governing *who may perform and approve* inventory actions.

### Owned Entities

| Entity / Aggregate | Role in Context |
|--------------------|-----------------|
| **User Account** *(aggregate root)* | User identity and lifecycle |
| **Role Assignment** *(entity)* | Role and location scope delegation |
| User Action Attribution *(value object)* | Accountability template |

### Related Use Cases

| Use Case | Name |
|----------|------|
| UC-044 | Manage User Accounts and Role Assignments |
| UC-045 | Enforce Role-Based and Location-Scoped Access |
| UC-041 | Conduct Inventory Audit and Control Review *(access compliance)* |

### Relationships with Other Contexts

| Related Context | Relationship | Integration |
|-----------------|--------------|-------------|
| All operational contexts | **Open Host Service** | Provides user identity and authorization checks |
| Inventory Governance | **Shared Kernel** *(SoD rules)* | Governance defines SoD policy; Identity enforces at assignment |
| Inventory Accuracy | **Upstream → Downstream** | Counter/approver identity validation |
| Warehouse Network | **Downstream (conformist)** | Location scope references location codes |

### Why This Context Should Be Independent

Identity and access is **cross-cutting infrastructure capability** with its own ubiquitous language — roles, permissions, scopes, segregation of duties — unrelated to inventory quantities or orders. It changes on **HR lifecycle events** (hire, transfer, termination) independent of inventory transactions. Every operational context needs identity but none should own it — embedding user models in Stock Position or Goods Receipt would couple security to business logic. Independent context enables enterprise SSO integration, role model expansion, and audit of access changes without touching inventory domain models.

---

## Context 13: Inventory Intelligence

### Business Responsibility

Provide read-optimized views of inventory state — dashboards, KPIs, movement history, audit trails, alerts, and valuation snapshots — supporting management oversight without owning transactional write models.

### Owned Entities

| Concept | Role in Context |
|---------|-----------------|
| **Inventory Movement Record** *(read projection)* | Append-only movement history |
| **Audit Trail Record** *(read projection)* | Governance-grade change log |
| **Operational Alert** *(read projection)* | Threshold and exception notifications |
| **Inventory Valuation Snapshot** *(read projection)* | Period-end financial summary |

*This context owns no write aggregates — it consumes domain events from all transactional contexts.*

### Related Use Cases

| Use Case | Name |
|----------|------|
| UC-012 | Monitor Inventory Status |
| UC-037 | Review Inventory Dashboards and Operational Reports |
| UC-038 | Review Inventory Performance KPIs |
| UC-042 | View Inventory Movement and Transaction History |
| UC-043 | Query and Review Audit Trail |
| UC-047 | Receive and Respond to Operational Notifications |
| UC-039 | Reconcile Inventory Valuation with Finance *(snapshot portion)* |
| UC-020 | Analyze Shrinkage, Loss, and Obsolete Stock |

### Relationships with Other Contexts

| Related Context | Relationship | Integration |
|-----------------|--------------|-------------|
| All transactional contexts | **Downstream (conformist)** | Consumes domain events; never writes back to source aggregates |
| Inventory Balance | **Downstream (conformist)** | Quantity and status projections |
| External Finance/GL | **Anti-Corruption Layer** | Valuation snapshot translated for finance reconciliation |
| External Executive BI | **Open Host Service** | KPI and dashboard data published |

### Why This Context Should Be Independent

Reporting and analytics have fundamentally different non-functional requirements — read-heavy, eventually consistent, aggregation-optimized — versus transactional contexts that require strong consistency and low-latency writes. Mixing dashboard queries into Stock Position or Order Fulfillment corrupts the write model with reporting concerns (the "reporting database inside the transaction" anti-pattern). Inventory Intelligence can rebuild projections from domain events without affecting operational correctness. Independent context allows query model optimization (materialized views, KPI caches) and finance integration without redeploying warehouse execution logic.

---

## Context Map Diagram

```
                    ┌─────────────────────────────────────────────────────────┐
                    │              EXTERNAL SYSTEMS                           │
                    │   [Sales/CRM]              [Finance/GL]               │
                    └───────┬──────────────────────────┬──────────────────────┘
                            │ ACL                      │ ACL
                            ▼                          ▼
┌──────────────┐    ┌───────────────┐         ┌──────────────────┐
│   Product    │    │    Order      │         │   Inventory      │
│   Catalog    │───►│  Fulfillment  │         │  Intelligence    │
└──────┬───────┘    └───────┬───────┘         └────────▲─────────┘
       │ upstream           │                          │ events
       ▼                    ▼                          │
┌──────────────┐    ┌───────────────┐         ┌────────┴─────────┐
│  Warehouse   │    │  Commercial   │         │  (all contexts   │
│   Network    │───►│   Campaign    │         │   publish to     │
└──────┬───────┘    └───────┬───────┘         │   intelligence)  │
       │                    │                 └──────────────────┘
       ▼                    ▼
┌──────────────────────────────────────────────────────────────────┐
│                     INVENTORY BALANCE                            │
│              (central quantity authority)                        │
└───▲──────▲──────▲──────▲──────▲──────▲──────────────────────────┘
    │      │      │      │      │      │
    │      │      │      │      │      └── Returns Management
    │      │      │      │      └───────── Inventory Accuracy
    │      │      │      └──────────────── Network Transfer
    │      │      └─────────────────────── Order Fulfillment
    │      └────────────────────────────── Inbound Receiving
    └───────────────────────────────────── (via events)

┌──────────────────┐         ┌──────────────────┐
│   Procurement    │────────►│     Inbound      │
│    & Supplier    │ upstream│    Receiving     │
└──────────────────┘         └──────────────────┘

┌──────────────────┐         ┌──────────────────┐
│   Inventory      │◄───────►│    Identity &    │
│   Governance     │ shared  │     Access       │
└──────────────────┘  kernel └──────────────────┘
         ▲
         │ conformist (all operational contexts consult governance)
```

---

## Context Integration Summary

| Integration Pattern | Contexts | Mechanism |
|--------------------|----------|-----------|
| **Domain Events** | All transactional → Inventory Balance | PutAwayCompleted, StockReserved, StockShipped, StockAdjusted, TransferReceived, ReturnRestocked |
| **Domain Events** | All transactional → Inventory Intelligence | InventoryMovementRecorded, AuditTrailRecorded, threshold alerts |
| **Domain Services** | Order Fulfillment ↔ Inventory Balance | Availability Confirmation, Reservation Coordination |
| **Domain Services** | Procurement ↔ Inventory Balance | Network Availability Evaluation before requisition |
| **Published Language** | All contexts | Product SKU, Location Code, User Identifier as shared identifiers |
| **ACL** | External Sales/CRM → Order Fulfillment | Fulfillment-relevant order subset translated |
| **ACL** | Inventory Intelligence → External Finance | Valuation snapshot mapped to GL format |

---

## Context-to-Use Case Coverage Matrix

| Context | Use Cases |
|---------|-----------|
| Product Catalog | UC-001, UC-004, UC-046 |
| Warehouse Network | UC-002, UC-046, UC-015 |
| Inventory Governance | UC-005, UC-041, UC-045 |
| Inventory Balance | UC-003, UC-012, UC-013, UC-019, UC-028 |
| Procurement & Supplier | UC-006, UC-007, UC-029, UC-030 |
| Inbound Receiving | UC-008, UC-009, UC-010, UC-011, UC-039 |
| Order Fulfillment | UC-021 – UC-027, UC-048 |
| Network Transfer | UC-031 – UC-034 |
| Inventory Accuracy | UC-014 – UC-018, UC-020 |
| Returns Management | UC-035, UC-036, UC-011 |
| Commercial Campaign | UC-040, UC-047 |
| Identity & Access | UC-044, UC-045, UC-041 |
| Inventory Intelligence | UC-012, UC-037, UC-038, UC-042, UC-043, UC-047, UC-039, UC-020 |

*All 48 use cases are covered across contexts. Some use cases span multiple contexts as indicated.*

---

## Independence Principles Applied

| Principle | How Contexts Apply It |
|-----------|----------------------|
| **Distinct ubiquitous language** | Each context names concepts in its stakeholders' vocabulary — ATP (Balance) vs. PO (Procurement) vs. RMA (Returns) |
| **Separate ownership** | Different business functions own different contexts — Purchasing vs. Warehouse vs. Marketing vs. Finance |
| **Independent change velocity** | Catalog changes quarterly; balance changes every second; governance changes on audit cycles |
| **Autonomous consistency** | Each context enforces its own invariants internally; cross-context rules via events and domain services |
| **Team alignment** | Context boundaries align to BRD actor groups — Buyer, Receiving Clerk, Customer Service, Marketing Manager |
| **Phased delivery** | MVP contexts (Balance, Receiving, Fulfillment) deliverable without Phase 2 contexts (Campaign, full Procurement) |

---

## Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| DDD Solution Architect | | | |
| Domain Expert | | | |
| Solution Architect | | | |
| Product Owner | | | |

---

*End of Bounded Contexts*

*Document ID: SRS-DM-007 | Version 1.0 | July 5, 2026*
