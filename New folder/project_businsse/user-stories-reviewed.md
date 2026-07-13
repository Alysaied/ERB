# User Stories — Senior Product Owner Review

**Document Owner:** Senior Product Owner  
**Purpose:** Review, refine, and organize all BRD user stories (US-001 – US-090) under product epics  
**Based On:** BRD-IMS-001, User Stories Document, Functional Requirements (FR-001 – FR-090), Product Epics (EPIC-IMS-001)  
**Review Date:** July 5, 2026

---

## Review Methodology

Each story was evaluated against four INVEST-aligned quality criteria:

| Criterion | What Was Checked |
|-----------|------------------|
| **Clarity** | Unambiguous role, goal, and outcome; consistent role naming (UR catalog); no grammatical defects |
| **Business Value** | Clear "so that" benefit tied to a business objective or pain point |
| **Independence** | Can be delivered and demonstrated without unfinished stories (prerequisites documented where unavoidable) |
| **Testability** | Observable outcomes suitable for acceptance criteria and UAT |

**Status legend:** ✅ Pass · ⚠️ Pass with notes · 🔄 Rewritten

---

## Review Summary

| Metric | Count |
|--------|-------|
| Total stories reviewed | 90 |
| Approved as-is | 74 |
| Rewritten for clarity / testability / role consistency | 10 |
| Pass with dependency or phase notes (no rewrite) | 6 |
| Stories with cross-epic prerequisites | 18 |

**Rewritten stories:** US-003, US-018, US-023, US-026, US-029, US-042, US-046, US-050, US-056, US-081

**Role standardization applied:** "Operations Manager" aligned to **Operations Director** (UR-04). "System Administrator" aligned to **IMS Administrator** (pending formal UR-20; interim governance role per BRD review ISS-011).

---

## EPIC-01: Master Data & Network Foundation

**Epic goal:** Establish trusted product, location, and policy master data and enable controlled go-live.

| Story | FR | Phase |
|-------|-----|-------|
| US-001 – US-012, US-056, US-090 | FR-001 – FR-012, FR-056, FR-090 | MVP / Phase 2 |

---

### US-001 · FR-001 · MVP

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ✅ | ✅ |

**Role:** Inventory Controller

**Story (approved):**  
As an **Inventory Controller**, I want to **create and maintain product master records including SKU, name, description, unit of measure, and category**, so that **all locations and departments reference a single, consistent product identity and ordering and fulfillment errors are eliminated**.

**Review notes:** Clear, testable, foundational. No dependencies beyond access control (EPIC-11).

---

### US-002 · FR-002 · MVP

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Inventory Controller

**Story (approved):**  
As an **Inventory Controller**, I want to **manage product status across active, inactive, and discontinued states with rules that control receiving, ordering, and fulfillment**, so that **obsolete or withdrawn products do not re-enter the supply chain and remaining stock can be planned for clearance or write-off**.

**Review notes:** Depends on US-001 (product must exist). Testable via status transition rules and blocked actions.

---

### US-003 · FR-003 · MVP

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| 🔄 | ✅ | ⚠️ | ✅ |

**Role:** Warehouse Staff *(was: Warehouse Operator — composite role)*

**Story (rewritten):**  
As **Warehouse Staff** (receiving, counting, or picking), I want to **look up a product by SKU, barcode, or other assigned identifier**, so that **I can confirm the correct product during operational tasks without manual cross-referencing or misidentification**.

**Review notes:** Original combined multiple roles into a non-catalog label. Rewritten for role clarity. Depends on US-001. Testable via scan/search scenarios in receiving, counting, and picking contexts.

---

### US-004 · FR-004 · MVP

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Inventory Controller

**Story (approved):**  
As an **Inventory Controller**, I want the system to **detect potential duplicate product records during creation or update and support correction without creating parallel identities**, so that **stock for the same physical product is not fragmented across multiple records causing inaccurate availability**.

**Review notes:** Depends on US-001. Testable with duplicate SKU/name submission scenarios.

---

### US-005 · FR-005 · MVP

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ✅ | ✅ |

**Role:** Operations Director

**Story (approved):**  
As an **Operations Director**, I want to **configure and maintain inventory locations including warehouses, stores, and distribution points with type and operational status**, so that **stock can be assigned, tracked, and reported at the correct locations across the network**.

**Review notes:** Foundational epic story. No functional prerequisites.

---

### US-006 · FR-006 · MVP

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Operations Director

**Story (approved):**  
As an **Operations Director**, I want to **define and maintain a location hierarchy reflecting how sites relate within the distribution network**, so that **I can roll up stock visibility, reporting, and accountability at regional and network levels**.

**Review notes:** Requires US-005 (locations exist). Testable via parent-child assignment and rollup views.

---

### US-007 · FR-007 · Phase 2

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Operations Director

**Story (approved):**  
As an **Operations Director**, I want to **plan and execute stock disposition when a location is closed or consolidated**, so that **no inventory is stranded or orphaned when a site exits the network and asset value is protected**.

**Review notes:** Depends on US-005, US-058/US-060 (transfers), US-035 (adjustments). Phase 2 delivery.

---

### US-008 · FR-008 · MVP

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Inventory Controller

**Story (approved):**  
As an **Inventory Controller**, I want to **define and maintain reorder levels, minimum thresholds, and safety stock parameters per product and location**, so that **low-stock conditions are identified proactively and purchasing aligns with operational needs**.

**Review notes:** Requires US-001 and US-005. Enables US-051 (alerts).

---

### US-009 · FR-009 · Phase 2

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Inventory Controller

**Story (approved):**  
As an **Inventory Controller**, I want to **classify products by ABC priority based on revenue, velocity, and criticality**, so that **counting effort, alert priority, and monitoring intensity focus on the items that matter most to the business**.

**Review notes:** Requires US-001. Phase 2. Testable via class assignment and reflected priority in counts/alerts.

---

### US-010 · FR-010 · MVP

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Inventory Controller

**Story (approved):**  
As an **Inventory Controller**, I want to **establish verified opening stock balances from a physical count before a new location becomes operational**, so that **the location starts with a trusted inventory baseline and avoids cascading fulfillment errors from embedded go-live errors**.

**Review notes:** Requires US-005 and count capability (US-032 or US-090 validated import per FR-010). Testable via blocked transactions until opening balance approved.

---

### US-011 · FR-011 · MVP

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ✅ | ✅ |

**Role:** Inventory Controller

**Story (approved):**  
As an **Inventory Controller**, I want to **maintain a controlled list of reason codes for adjustments, write-offs, and receipt discrepancies**, so that **every inventory change is categorized for shrinkage analysis, trend identification, and audit substantiation**.

**Review notes:** Independent configuration story. Consumed by US-035, US-036, US-016.

---

### US-012 · FR-012 · Phase 2

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ⚠️ |

**Role:** Operations Director

**Story (approved):**  
As an **Operations Director**, I want to **document and reference inventory governance policies such as approval thresholds, count tolerances, and reservation rules**, so that **operational decisions are consistent across locations and formally accountable**.

**Review notes:** Phase 2. Testability improved when threshold values are baselined (BRD ISS-017). Depends on US-037 patterns being defined.

---

### US-056 · FR-056 · Phase 2

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| 🔄 | ✅ | ⚠️ | ✅ |

**Role:** Operations Director

**Story (rewritten):**  
As an **Operations Director**, I want the system to **block or require authorized approval for reservations and transfers that would reduce stock below the defined safety stock minimum**, so that **the buffer protecting against demand and supply uncertainty is not eroded by routine operations**.

**Review notes:** Primary epic owner is EPIC-01 (policy definition via US-008); enforced in EPIC-05 and EPIC-07. Original did not name actionable transaction types. Depends on US-008. Testable via blocked reservation/transfer and approved exception paths.

---

### US-090 · FR-090 · MVP

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Inventory Controller

**Story (approved):**  
As an **Inventory Controller**, I want to **import initial product master data and opening stock balances with validation and authorized approval before activation**, so that **primary locations can go live efficiently without manual entry of the entire product catalog**.

**Review notes:** Depends on US-001, US-005, US-004 (duplicate check), US-010 (opening balance approval). Testable via import validation errors and post-approval activation.

---

## EPIC-02: Inbound Supply & Goods Receiving

**Epic goal:** Verify and record all inbound stock with procurement control and put-away discipline.

| Story | FR | Phase |
|-------|-----|-------|
| US-013 – US-022, US-055 | FR-013 – FR-022, FR-055 | MVP / Phase 2 / Phase 3 |

---

### US-013 · FR-013 · Phase 2

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Buyer

**Story (approved):**  
As a **Buyer**, I want to **record purchase orders with product, quantity, expected delivery, supplier, and receiving location**, so that **inbound supply is visible to receiving, operations, and sales before goods arrive**.

**Review notes:** Requires US-001, US-005. Phase 2. MVP workaround: manual PO reference outside system per BRD ISS-010.

---

### US-014 · FR-014 · Phase 2

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Warehouse Manager

**Story (approved):**  
As a **Warehouse Manager**, I want to **view expected inbound deliveries by date and receiving location**, so that **I can prepare dock capacity, staffing, and storage before shipments arrive**.

**Review notes:** Depends on US-013. Phase 2.

---

### US-015 · FR-015 · MVP

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Receiving Clerk

**Story (approved):**  
As a **Receiving Clerk**, I want to **receive and verify inbound goods against delivery documentation and purchase order reference before accepting stock into inventory**, so that **on-hand balances reflect what was actually received in acceptable condition**.

**Review notes:** Core MVP story. Depends on US-001, US-005, US-003. Testable via receipt with accepted/rejected quantity split.

---

### US-016 · FR-016 · MVP

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Receiving Clerk

**Story (approved):**  
As a **Receiving Clerk**, I want to **document receipt discrepancies such as short shipments, over-shipments, wrong items, and damage and track them through resolution**, so that **supplier accountability is preserved and inventory records are not corrupted by unverified variances**.

**Review notes:** Depends on US-015, US-011. Testable via discrepancy types and resolution status transitions.

---

### US-017 · FR-017 · MVP

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Receiving Clerk

**Story (approved):**  
As a **Receiving Clerk**, I want the system to **require a valid purchase order reference for standard supplier receipts with a controlled path for authorized emergency receipts**, so that **procurement controls are maintained and unauthorized receiving is prevented**.

**Review notes:** Depends on US-015. Ad-hoc exception matrix must be defined (BRD ISS-020) for full testability.

---

### US-018 · FR-018 · MVP

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| 🔄 | ✅ | ⚠️ | ✅ |

**Role:** Warehouse Staff

**Story (rewritten):**  
As **Warehouse Staff**, I want to **confirm put-away completion for received stock**, so that **sellable availability updates only after goods are stored in their designated location and pickers can fulfill orders without searching the receiving area**.

**Review notes:** Original had duplicate "so that" clauses (grammar defect). Depends on US-015. Testable via received vs. available quantity states and ATP timing.

---

### US-019 · FR-019 · MVP

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Receiving Clerk

**Story (approved):**  
As a **Receiving Clerk**, I want to **receive customer returns and other non-purchase-order inbound stock with appropriate reference linkage and disposition routing**, so that **all inventory increases are captured in one system with complete movement history**.

**Review notes:** MVP interim returns path; superseded by US-064–US-066 in Phase 2 (BRD ISS-035). Depends on US-015 patterns.

---

### US-020 · FR-020 · Phase 2

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Receiving Clerk

**Story (approved):**  
As a **Receiving Clerk**, I want the system to **evaluate received quantities against purchase order expectations using defined tolerance rules and flag variances beyond acceptable limits**, so that **material over-receipts or under-receipts are not silently accepted**.

**Review notes:** Depends on US-013, US-015, US-016. Phase 2.

---

### US-021 · FR-021 · Phase 2

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Buyer

**Story (approved):**  
As a **Buyer**, I want to **cancel or amend open purchase orders before receipt is complete**, so that **inbound projections stay accurate and receiving is not performed against obsolete or changed orders**.

**Review notes:** Depends on US-013. Phase 2.

---

### US-022 · FR-022 · Phase 3

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Purchasing Manager

**Story (approved):**  
As a **Purchasing Manager**, I want to **review supplier delivery performance including on-time delivery, quantity accuracy, and discrepancy frequency**, so that **replenishment decisions and supplier relationships are informed by actual performance data**.

**Review notes:** Depends on US-013, US-015, US-016 history. Phase 3.

---

### US-055 · FR-055 · Phase 2

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Customer Service Representative

**Story (approved):**  
As a **Customer Service Representative**, I want to **view the status of open purchase orders and expected inbound deliveries including delays and partial receipts**, so that **I can communicate realistic restock dates to customers asking about out-of-stock items**.

**Review notes:** Placed in EPIC-02 (inbound supply ownership). Depends on US-013. Phase 2.

---

## EPIC-03: Real-Time Inventory Visibility

**Epic goal:** Provide a trusted, real-time view of stock across the network.

| Story | FR | Phase |
|-------|-----|-------|
| US-023 – US-028 | FR-023 – FR-028 | MVP / Phase 2 |

---

### US-023 · FR-023 · MVP

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| 🔄 | ✅ | ⚠️ | ✅ |

**Role:** Operations Director *(was: Operations Manager)*

**Story (rewritten):**  
As an **Operations Director**, I want to **view current on-hand inventory quantity for any product at any authorized location**, so that **I can answer what stock exists and where without relying on manual spreadsheets or warehouse calls**.

**Review notes:** Role aligned to UR-04. Depends on movement recording (US-029) and master data. "Real-time" = upon transaction completion per BRD glossary (ISS-015).

---

### US-024 · FR-024 · MVP

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ⚠️ |

**Role:** Sales Representative

**Story (approved):**  
As a **Sales Representative**, I want to **view available-to-promise quantity that excludes reserved and non-sellable stock**, so that **I promise customers only what can actually be fulfilled and avoid overselling**.

**Review notes:** Depends on US-023, US-025, US-018 (put-away). ATP definition must be baselined (BRD ISS-019) for complete testability.

---

### US-025 · FR-025 · MVP

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Customer Service Representative

**Story (approved):**  
As a **Customer Service Representative**, I want to **view inventory quantities reserved or committed to specific orders**, so that **I understand why available stock differs from on-hand and can explain fulfillment status accurately to customers**.

**Review notes:** Depends on US-042 (reservations). Testable once orders are reserved.

---

### US-026 · FR-026 · MVP

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| 🔄 | ✅ | ⚠️ | ✅ |

**Role:** Operations Director *(was: Operations Manager)*

**Story (rewritten):**  
As an **Operations Director**, I want to **see stock status indicators (in stock, low stock, out of stock) derived from defined thresholds at each location**, so that **I can identify problem items during daily reviews without manual threshold comparison**.

**Review notes:** Depends on US-008, US-024. Testable via threshold breach scenarios.

---

### US-027 · FR-027 · MVP

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Sales Representative

**Story (approved):**  
As a **Sales Representative**, I want to **search and filter inventory views by product, location, category, and status**, so that **I can find stock information quickly without interrupting warehouse operations for ad-hoc inquiries**.

**Review notes:** Depends on US-023. Respects location scope (US-082).

---

### US-028 · FR-028 · Phase 2

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Purchasing Manager

**Story (approved):**  
As a **Purchasing Manager**, I want to **view expected inbound stock and network-wide availability aggregated across all locations for a product**, so that **I can check network stock before placing a new purchase and sales can communicate realistic restock timelines**.

**Review notes:** Depends on US-013, US-023, US-024. Phase 2.

---

## EPIC-04: Inventory Control & Accuracy

**Epic goal:** Sustain inventory accuracy through counting, adjustments, and complete movement traceability.

| Story | FR | Phase |
|-------|-----|-------|
| US-029 – US-040 | FR-029 – FR-040 | MVP / Phase 2 / Phase 3 |

---

### US-029 · FR-029 · MVP

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| 🔄 | ✅ | ⚠️ | ✅ |

**Role:** Inventory Controller

**Story (rewritten):**  
As an **Inventory Controller**, I want to **view a complete history of every inventory movement with product, quantity, location, user, timestamp, and transaction type**, so that **I can trace any balance change for accountability, audit, and root-cause investigation**.

**Review notes:** Original passive phrasing obscured the inquiry capability. Cross-cutting enabler for all movement epics; demonstrated when any transaction story is delivered. Testable via movement history query by product, location, date, and type.

---

### US-030 · FR-030 · MVP

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Inventory Controller

**Story (approved):**  
As an **Inventory Controller**, I want to **schedule and assign cycle counts by location, category, or ABC class according to a count calendar**, so that **physical stock is verified on a rotating basis without waiting for disruptive full-wall counts**.

**Review notes:** Depends on US-001, US-005. Testable via assignment generation and completion tracking.

---

### US-031 · FR-031 · MVP

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Warehouse Staff

**Story (approved):**  
As **Warehouse Staff**, I want to **perform cycle counts without seeing the system's expected quantity until after I submit my count**, so that **count results are unbiased and accurately measure true inventory record accuracy**.

**Review notes:** Depends on US-030. Testable via hidden expected quantity until submission.

---

### US-032 · FR-032 · MVP

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Inventory Controller

**Story (approved):**  
As an **Inventory Controller**, I want to **conduct a full physical inventory count at a location with movement freeze and comprehensive variance reporting**, so that **a verified baseline is established for financial substantiation and accumulated discrepancies are corrected**.

**Review notes:** Depends on US-005. Supports US-010 opening balances.

---

### US-033 · FR-033 · MVP

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Inventory Controller

**Story (approved):**  
As an **Inventory Controller**, I want the system to **identify variances between physical count results and recorded quantities and flag those exceeding defined tolerance**, so that **investigation effort focuses on material discrepancies rather than immaterial noise**.

**Review notes:** Depends on US-030, US-031, or US-032. Testable via variance calculation and tolerance classification.

---

### US-034 · FR-034 · MVP

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Warehouse Manager

**Story (approved):**  
As a **Warehouse Manager**, I want to **investigate count variances, document root causes, and approve adjustments independently of the person who performed the count**, so that **inventory corrections are authorized, explained, and subject to proper oversight**.

**Review notes:** Depends on US-033. SoD enforced via US-084.

---

### US-035 · FR-035 · MVP

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Warehouse Manager

**Story (approved):**  
As a **Warehouse Manager**, I want to **process stock adjustments with mandatory reason codes, quantity, and user attribution**, so that **inventory records are corrected for damage, shrinkage, or errors with full accountability**.

**Review notes:** Depends on US-011. Routes to US-037 when above threshold.

---

### US-036 · FR-036 · MVP

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Warehouse Manager

**Story (approved):**  
As a **Warehouse Manager**, I want to **process inventory write-offs for obsolete, damaged, or stolen stock with documented evidence and authorized approval**, so that **removed stock is accurately reflected in operational records and protected against unauthorized disposal**.

**Review notes:** Depends on US-011, US-037. Testable via evidence attachment and approval workflow.

---

### US-037 · FR-037 · MVP

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ⚠️ |

**Role:** Operations Director

**Story (approved):**  
As an **Operations Director**, I want **adjustments and write-offs exceeding defined quantity or value thresholds routed to me for independent approval**, so that **high-impact inventory changes receive oversight proportional to their financial risk**.

**Review notes:** Threshold values pending policy sign-off (ISS-017). Depends on US-035, US-036, US-034. Triggers US-077 notifications.

---

### US-038 · FR-038 · Phase 2

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ⚠️ |

**Role:** Warehouse Manager

**Story (approved):**  
As a **Warehouse Manager**, I want to **place stock on quarantine or hold status pending quality investigation or inspection**, so that **defective, damaged, or uninspected goods are excluded from sellable availability and cannot be shipped to customers**.

**Review notes:** Phase 2. Affects US-024 ATP. Disposition workflow detail needed (ISS-030).

---

### US-039 · FR-039 · Phase 2

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Inventory Controller

**Story (approved):**  
As an **Inventory Controller**, I want to **analyze shrinkage and loss trends aggregated by reason code, location, and period**, so that **I can identify recurring loss patterns and target corrective action without manual spreadsheet analysis**.

**Review notes:** Depends on US-035, US-036, US-011 data. Phase 2.

---

### US-040 · FR-040 · Phase 3

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Purchasing Manager

**Story (approved):**  
As a **Purchasing Manager**, I want to **identify slow-moving and obsolete stock based on movement history and product status**, so that **working capital trapped in dead stock can be released through clearance, transfer, or write-off action**.

**Review notes:** Depends on US-029, US-002, US-070. Phase 3.

---

## EPIC-05: Order Fulfillment

**Epic goal:** Deliver reliable order fulfillment from availability check through shipment.

| Story | FR | Phase |
|-------|-----|-------|
| US-041 – US-050 | FR-041 – FR-050 | MVP / Phase 2 / Phase 3 |

---

### US-041 · FR-041 · MVP

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Sales Representative

**Story (approved):**  
As a **Sales Representative**, I want to **verify that requested products are available in sufficient quantity at the appropriate location before confirming delivery to a customer**, so that **I do not overpromise and create order failures, cancellations, or customer complaints**.

**Review notes:** Depends on US-024. Requires external order boundary definition (ISS-002).

---

### US-042 · FR-042 · MVP

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| 🔄 | ✅ | ⚠️ | ✅ |

**Role:** Operations Director *(was: Operations Manager)*

**Story (rewritten):**  
As an **Operations Director**, I want to **reserve specific inventory quantities against confirmed orders at the designated fulfillment location**, so that **stock is protected from allocation to other orders and available-to-promise reflects remaining sellable quantity**.

**Review notes:** Depends on US-024, US-041. Testable via ATP reduction on reservation.

---

### US-043 · FR-043 · MVP

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Customer Service Representative

**Story (approved):**  
As a **Customer Service Representative**, I want to **release inventory reservations when orders are cancelled, modified, or fully fulfilled**, so that **stock is not indefinitely locked to unfulfilled orders and becomes available for other customers**.

**Review notes:** Depends on US-042. Testable via ATP restoration on release.

---

### US-044 · FR-044 · MVP

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Warehouse Picker

**Story (approved):**  
As a **Warehouse Picker**, I want to **receive pick lists, confirm picks, and record shipments with inventory deducted only after verified pick completion**, so that **fulfilled orders accurately reflect goods dispatched and inventory records stay aligned with physical stock**.

**Review notes:** Depends on US-042, US-003. Testable via pick confirmation and shipment deduction.

---

### US-045 · FR-045 · MVP

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Customer Service Representative

**Story (approved):**  
As a **Customer Service Representative**, I want to **process partial fulfillment by shipping available quantity and placing remaining lines on backorder with documented customer acknowledgment**, so that **customers receive partial delivery promptly rather than waiting for a complete order hold**.

**Review notes:** Depends on US-042, US-044. Testable via partial ship and backorder record creation.

---

### US-046 · FR-046 · Phase 2

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| 🔄 | ✅ | ⚠️ | ⚠️ |

**Role:** Operations Director *(was: Operations Manager)*

**Story (rewritten):**  
As an **Operations Director**, I want to **maintain a prioritized backorder queue that automatically reserves stock when it becomes available per defined allocation policy**, so that **delayed orders are fulfilled fairly without manual backorder tracking**.

**Review notes:** Depends on US-045. Priority policy must be defined (ISS-023) for full testability. Phase 2.

---

### US-047 · FR-047 · Phase 2

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Warehouse Manager

**Story (approved):**  
As a **Warehouse Manager**, I want to **resolve fulfillment exceptions such as pick failures, damaged items during pick, and order cancellations**, so that **customer impact is minimized and inventory records are corrected when physical reality differs from the system**.

**Review notes:** Depends on US-044. Triggers US-078. Phase 2.

---

### US-048 · FR-048 · Phase 2

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Operations Director

**Story (approved):**  
As an **Operations Director**, I want to **fulfill a single customer order from multiple locations when no single site holds sufficient stock**, so that **network fill rate is maximized and orders are not rejected when aggregate network availability is sufficient**.

**Review notes:** Depends on US-041, US-042, US-044, US-060. Phase 2.

---

### US-049 · FR-049 · MVP

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Customer Service Representative

**Story (approved):**  
As a **Customer Service Representative**, I want to **view order fulfillment status including reserved, picking, shipped, partially shipped, backordered, and cancelled states**, so that **I can give customers accurate and consistent information without calling the warehouse**.

**Review notes:** Depends on US-042, US-044, US-045. Testable via status transitions.

---

### US-050 · FR-050 · Phase 3

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| 🔄 | ✅ | ⚠️ | ⚠️ |

**Role:** Warehouse Manager

**Story (rewritten):**  
As a **Warehouse Manager**, I want to **substitute an ordered product with an approved alternate SKU when the primary product is unavailable, with documented approver authorization**, so that **orders can still be fulfilled while only pre-approved substitutes are shipped**.

**Review notes:** Depends on substitute master data (ISS-024). Phase 3. Testable via substitution approval and inventory update for actual SKU shipped.

---

## EPIC-06: Replenishment Planning & Stock Alerts

**Epic goal:** Detect stock breaches proactively and drive replenishment decisions.

| Story | FR | Phase |
|-------|-----|-------|
| US-051 – US-054, US-057 | FR-051 – FR-054, FR-057 | MVP / Phase 2 / Phase 3 |

---

### US-051 · FR-051 · MVP

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Purchasing Manager

**Story (approved):**  
As a **Purchasing Manager**, I want the system to **automatically generate alerts when stock falls below reorder thresholds or reaches zero at a location**, so that **I can act on replenishment needs before customers experience stockouts**.

**Review notes:** Depends on US-008, US-024, US-026. Enables US-076. Testable via threshold breach.

---

### US-052 · FR-052 · MVP

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Purchasing Manager

**Story (approved):**  
As a **Purchasing Manager**, I want to **review, acknowledge, and dismiss low-stock alerts with documented rationale**, so that **alerts drive genuine action rather than creating noise and alert fatigue**.

**Review notes:** Depends on US-051. Testable via acknowledge/dismiss with required reason.

---

### US-053 · FR-053 · MVP

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Buyer

**Story (approved):**  
As a **Buyer**, I want the system to **generate replenishment suggestions based on current stock, thresholds, open orders, and consumption patterns**, so that **my ordering decisions are driven by data rather than reactive gut-feel**.

**Review notes:** Depends on US-008, US-051, US-052. Testable via suggestion quantity and rationale display.

---

### US-054 · FR-054 · Phase 2

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Buyer

**Story (approved):**  
As a **Buyer**, I want to **create, submit, and track purchase requisitions derived from replenishment suggestions or manual requests**, so that **the handoff from replenishment planning to procurement is formalized with approval accountability**.

**Review notes:** Depends on US-053, US-013. Phase 2. Triggers US-077.

---

### US-057 · FR-057 · Phase 3 (Deferred)

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ⚠️ |

**Role:** Marketing Manager

**Story (approved):**  
As a **Marketing Manager**, I want to **review stock readiness against promotional or launch targets and ring-fence promotional inventory**, so that **campaigns and product launches are not undermined by stockouts at the worst possible moment**.

**Review notes:** MoSCoW Won't Have current release (ISS-008). Depends on US-008, US-013, US-028, US-053. Enables US-080.

---

## EPIC-07: Network Balance & Stock Transfers

**Epic goal:** Balance stock across locations through controlled transfers.

| Story | FR | Phase |
|-------|-----|-------|
| US-058 – US-063 | FR-058 – FR-063 | MVP / Phase 2 / Phase 3 |

---

### US-058 · FR-058 · MVP

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Regional / Store Manager

**Story (approved):**  
As a **Regional / Store Manager**, I want to **request inter-location stock transfers specifying product, quantity, source, destination, and justification**, so that **local stockouts can be resolved using excess inventory elsewhere in the network without waiting for supplier delivery**.

**Review notes:** Depends on US-005, US-023, US-024. Testable via transfer request submission.

---

### US-059 · FR-059 · MVP

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Operations Director

**Story (approved):**  
As an **Operations Director**, I want to **approve, reject, or modify inter-location transfer requests with documented rationale**, so that **stock movements are authorized and do not create new imbalances or deplete source locations below service levels**.

**Review notes:** Depends on US-058, US-063. Triggers US-077.

---

### US-060 · FR-060 · MVP

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Warehouse Manager

**Story (approved):**  
As a **Warehouse Manager**, I want to **execute approved transfers by recording dispatch from source and receipt at destination with balanced inventory updates at both locations**, so that **stock is never lost between locations and both sites reflect accurate balances**.

**Review notes:** Depends on US-059, US-029. Testable via source deduction and destination addition.

---

### US-061 · FR-061 · Phase 2

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Operations Director

**Story (approved):**  
As an **Operations Director**, I want to **monitor inventory in transit between locations separately from on-hand at source or destination**, so that **network visibility is maintained during transfer lead time and accountability exists for goods between dispatch and receipt**.

**Review notes:** Depends on US-060. Triggers US-078. Phase 2.

---

### US-062 · FR-062 · Phase 3 (Deferred)

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ⚠️ |

**Role:** Operations Director

**Story (approved):**  
As an **Operations Director**, I want the system to **analyze stock distribution across the network and recommend rebalancing transfers identifying excess and shortage locations**, so that **inventory investment is optimized enterprise-wide rather than trapped at overstocked sites while others stockout**.

**Review notes:** MoSCoW Won't Have (ISS-008). Requires sustained accuracy ≥95% (BO-02). Depends on US-028, US-058, US-070, US-072.

---

### US-063 · FR-063 · MVP

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Operations Director

**Story (approved):**  
As an **Operations Director**, I want the system to **prevent transfer approval when the proposed quantity would deplete the source below its minimum threshold**, so that **fixing one location's shortage does not create a shortage at the sending location**.

**Review notes:** Depends on US-008. Enforced during US-058/US-059. Testable via blocked over-transfer.

---

## EPIC-08: Returns Management

**Epic goal:** Manage the customer return lifecycle with accurate inventory impact.

| Story | FR | Phase |
|-------|-----|-------|
| US-064 – US-067 (+ US-019 interim) | FR-064 – FR-067, FR-019 | MVP interim / Phase 2 |

---

### US-064 · FR-064 · Phase 2

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Customer Service Representative

**Story (approved):**  
As a **Customer Service Representative**, I want to **authorize and record customer returns linked to original orders with product, quantity, reason, and expected resolution**, so that **returns are connected to commercial transactions and the warehouse knows what to expect**.

**Review notes:** Depends on US-049 (order reference). Phase 2 full module.

---

### US-065 · FR-065 · Phase 2

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Receiving Clerk

**Story (approved):**  
As a **Receiving Clerk**, I want to **receive returned goods against return authorization and route them through an inspection workflow**, so that **only goods passing inspection can re-enter sellable inventory**.

**Review notes:** Depends on US-064. Supersedes basic path in US-019.

---

### US-066 · FR-066 · Phase 2

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Warehouse Manager

**Story (approved):**  
As a **Warehouse Manager**, I want to **restock resalable returned goods or write off non-resalable quantity based on inspection outcome**, so that **inventory records accurately reflect true sellable stock after returns processing**.

**Review notes:** Depends on US-065, US-035, US-036.

---

### US-067 · FR-067 · Phase 2

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Customer Service Representative

**Story (approved):**  
As a **Customer Service Representative**, I want to **track return processing status from authorization through receipt, inspection, and final disposition**, so that **I can inform customers accurately about refund, replacement, or credit timing**.

**Review notes:** Depends on US-064–US-066 chain. Testable via status lifecycle.

---

## EPIC-09: Reporting, Analytics & Financial Alignment

**Epic goal:** Enable operational oversight, KPI measurement, and finance alignment.

| Story | FR | Phase |
|-------|-----|-------|
| US-068 – US-075, US-089 | FR-068 – FR-075, FR-089 | MVP / Phase 2 / Phase 3 |

---

### US-068 · FR-068 · MVP

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Operations Director

**Story (approved):**  
As an **Operations Director**, I want to **view an inventory summary dashboard showing stock levels, low-stock counts, and out-of-stock counts across authorized locations**, so that **I have a single operational view of inventory health without compiling reports manually**.

**Review notes:** Depends on US-023, US-026, US-051 data.

---

### US-069 · FR-069 · MVP

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Inventory Controller

**Story (approved):**  
As an **Inventory Controller**, I want to **generate stock movement reports showing receipts, transfers, adjustments, fulfillments, and returns over a selectable period**, so that **operational review and audit substantiation do not require manual reconstruction of transaction history**.

**Review notes:** Depends on US-029 movement data.

---

### US-070 · FR-070 · MVP

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Purchasing Manager

**Story (approved):**  
As a **Purchasing Manager**, I want to **generate reports identifying products and locations in stockout or overstock condition**, so that **purchasing and transfer action is directed toward the areas causing lost sales or trapped capital**.

**Review notes:** Depends on US-026, US-008.

---

### US-071 · FR-071 · MVP

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Inventory Controller

**Story (approved):**  
As an **Inventory Controller**, I want to **generate inventory accuracy and count variance reports by location and period**, so that **I can measure progress toward accuracy targets and identify locations or SKUs requiring corrective attention**.

**Review notes:** Depends on US-030–US-034 count data. Supports BO-02 measurement.

---

### US-072 · FR-072 · Phase 2

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** COO

**Story (approved):**  
As a **COO**, I want to **view location performance snapshots comparing accuracy, stockout frequency, shrinkage, and fulfillment metrics across the network**, so that **I can hold locations accountable and identify best and worst performers fairly**.

**Review notes:** Depends on US-071, US-070, US-068. Phase 2.

---

### US-073 · FR-073 · Phase 3

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** CEO

**Story (approved):**  
As a **CEO**, I want to **view inventory performance KPIs including fill rate, turnover, days of supply, and record accuracy with trends against targets**, so that **I can measure operational maturity and progress toward strategic inventory objectives**.

**Review notes:** Depends on US-068, US-071, US-049, US-029. Phase 3. KPI targets from BO/KPI catalog.

---

### US-074 · FR-074 · MVP / Phase 2

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Buyer

**Story (approved):**  
As a **Buyer**, I want to **view a replenishment report showing items below threshold, active alerts, open requisitions, and expected inbound supply**, so that **all information needed for daily purchasing decisions is consolidated in one view**.

**Review notes:** Depends on US-051–US-054, US-055. Requisitions section Phase 2 only.

---

### US-075 · FR-075 · Phase 3

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ⚠️ |

**Role:** Finance Manager

**Story (approved):**  
As a **Finance Manager**, I want to **view inventory valuation summaries based on operational quantities and agreed unit costs**, so that **operations and finance inventory records can be reconciled without manual cross-department investigation**.

**Review notes:** Depends on costing method decision. Phase 3. Enables US-089.

---

### US-089 · FR-089 · Phase 3

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Finance Manager

**Story (approved):**  
As a **Finance Manager**, I want to **reconcile operational inventory records with finance reporting using quantity summaries, adjustment logs, and valuation views by period**, so that **month-end close is timely and operations-finance misalignment is reduced**.

**Review notes:** Placed in EPIC-09 (financial alignment). Depends on US-075, US-086, US-071, US-036. Phase 3; interim manual process per ISS-018.

---

## EPIC-10: Operational Notifications & Awareness

**Epic goal:** Deliver timely notifications when conditions require action.

| Story | FR | Phase |
|-------|-----|-------|
| US-076 – US-080 | FR-076 – FR-080 | MVP / Phase 2 / Phase 3 |

> **Epic note:** All notification stories are **dependent** on source-event stories. They are independently testable once prerequisites are delivered (notification delivery can be mocked or triggered in UAT).

---

### US-076 · FR-076 · MVP

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Purchasing Manager

**Story (approved):**  
As a **Purchasing Manager**, I want to **receive notifications when low-stock or out-of-stock conditions are detected for priority products**, so that **critical stock situations reach me promptly and I can act before customers are affected**.

**Review notes:** Depends on US-051. Recipient routing to be configured (ISS-028).

---

### US-077 · FR-077 · MVP

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Operations Director

**Story (approved):**  
As an **Operations Director**, I want to **receive notifications when adjustments, count variances, transfers, or requisitions require my approval**, so that **pending decisions do not create bottlenecks that delay replenishment, corrections, or stock movements**.

**Review notes:** Depends on US-037, US-034, US-059, US-054. Testable via pending approval trigger.

---

### US-078 · FR-078 · Phase 2

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Warehouse Manager

**Story (approved):**  
As a **Warehouse Manager**, I want to **receive alerts for transfer delays, in-transit exceptions, pick failures, and fulfillment disruptions**, so that **I can respond to operational problems before they escalate to customer complaints**.

**Review notes:** Depends on US-047, US-061. Phase 2.

---

### US-079 · FR-079 · Phase 2

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Purchasing Manager

**Story (approved):**  
As a **Purchasing Manager**, I want to **receive notifications when supplier deliveries are delayed beyond the expected date**, so that **I can proactively inform operations and customer service about restock delays before they become surprises**.

**Review notes:** Depends on US-055, US-013. Phase 2.

---

### US-080 · FR-080 · Phase 3 (Deferred)

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ⚠️ |

**Role:** Marketing Manager

**Story (approved):**  
As a **Marketing Manager**, I want to **receive alerts when promotional or launch stock readiness falls below target within the campaign preparation window**, so that **I have early warning to delay or adjust campaigns before public commitment**.

**Review notes:** MoSCoW Won't Have (ISS-008). Depends on US-057, US-076.

---

## EPIC-11: Security, Access & Accountability

**Epic goal:** Control access, enforce segregation of duties, and log user activity.

| Story | FR | Phase |
|-------|-----|-------|
| US-081 – US-085 | FR-081 – FR-085 | MVP |

---

### US-081 · FR-081 · MVP

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| 🔄 | ✅ | ✅ | ✅ |

**Role:** IMS Administrator *(was: System Administrator)*

**Story (rewritten):**  
As an **IMS Administrator**, I want to **assign roles so each user can only perform actions permitted for their business role**, so that **inventory integrity is protected through appropriate permission boundaries and segregation of duties**.

**Review notes:** Role aligned pending formal UR-20 (ISS-011). Foundational — no functional prerequisites. Testable via denied unauthorized actions.

---

### US-082 · FR-082 · MVP

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** IMS Administrator

**Story (approved):**  
As an **IMS Administrator**, I want to **restrict user visibility and transaction authority by assigned location scope**, so that **users can only view and transact at locations they are accountable for unless explicitly granted network-wide access**.

**Review notes:** Depends on US-005 (locations), US-081. Testable via cross-location access denial.

---

### US-083 · FR-083 · MVP

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Internal Auditor

**Story (approved):**  
As an **Internal Auditor**, I want **user activity logged for inventory transactions, approvals, configuration changes, and login events**, so that **I can trace who performed each action during investigations and control testing**.

**Review notes:** Depends on US-081. Cross-cutting — validated when any transactional story is exercised.

---

### US-084 · FR-084 · MVP

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ⚠️ |

**Role:** IMS Administrator

**Story (approved):**  
As an **IMS Administrator**, I want the system to **prevent the same user from performing conflicting actions such as counting and approving their own adjustment**, so that **segregation of duties is enforced and fraud or undetected error risk is reduced**.

**Review notes:** Small-team exception policy required (ISS-025). Depends on US-081. Testable via blocked self-approval.

---

### US-085 · FR-085 · MVP

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** IMS Administrator

**Story (approved):**  
As an **IMS Administrator**, I want to **create, deactivate, and manage user accounts and role assignments including location scope**, so that **system access always reflects the current organization and departed employees cannot retain access**.

**Review notes:** Depends on US-081. Testable via account lifecycle and deactivated user login denial.

---

## EPIC-12: Governance, Audit & Compliance

**Epic goal:** Maintain audit-ready evidence and detect control breaches.

| Story | FR | Phase |
|-------|-----|-------|
| US-086 – US-088 | FR-086 – FR-088 | MVP / Phase 2 |

---

### US-086 · FR-086 · MVP

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Internal Auditor

**Story (approved):**  
As an **Internal Auditor**, I want a **complete, immutable audit trail of all inventory quantity changes with before and after balances, reason codes, user, and timestamp**, so that **I have reliable evidence for audit, dispute resolution, and root-cause investigation**.

**Review notes:** Depends on US-029 movement recording. Core MVP compliance story (BO-19).

---

### US-087 · FR-087 · Phase 2

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ✅ |

**Role:** Internal Auditor

**Story (approved):**  
As an **Internal Auditor**, I want to **run structured queries and export evidence packages for review of inventory controls, transactions, and count records**, so that **audit preparation effort is reduced and control effectiveness can be demonstrated efficiently**.

**Review notes:** Depends on US-086, US-083, US-084. Phase 2.

---

### US-088 · FR-088 · Phase 2

| Clarity | Business Value | Independence | Testability |
|---------|----------------|--------------|-------------|
| ✅ | ✅ | ⚠️ | ⚠️ |

**Role:** Internal Auditor

**Story (approved):**  
As an **Internal Auditor**, I want the system to **detect and record instances where operational actions breach defined control policies**, so that **control weaknesses are visible for corrective action rather than discovered only at audit time**.

**Review notes:** Depends on US-012 governance policies. Phase 2.

---

## Epic-to-Story Index

| Epic | Stories |
|------|---------|
| EPIC-01 | US-001, US-002, US-003, US-004, US-005, US-006, US-007, US-008, US-009, US-010, US-011, US-012, US-056, US-090 |
| EPIC-02 | US-013, US-014, US-015, US-016, US-017, US-018, US-019, US-020, US-021, US-022, US-055 |
| EPIC-03 | US-023, US-024, US-025, US-026, US-027, US-028 |
| EPIC-04 | US-029, US-030, US-031, US-032, US-033, US-034, US-035, US-036, US-037, US-038, US-039, US-040 |
| EPIC-05 | US-041, US-042, US-043, US-044, US-045, US-046, US-047, US-048, US-049, US-050 |
| EPIC-06 | US-051, US-052, US-053, US-054, US-057 |
| EPIC-07 | US-058, US-059, US-060, US-061, US-062, US-063 |
| EPIC-08 | US-064, US-065, US-066, US-067 |
| EPIC-09 | US-068, US-069, US-070, US-071, US-072, US-073, US-074, US-075, US-089 |
| EPIC-10 | US-076, US-077, US-078, US-079, US-080 |
| EPIC-11 | US-081, US-082, US-083, US-084, US-085 |
| EPIC-12 | US-086, US-087, US-088 |

---

## Recommended Next Actions

1. **Update source user-stories.md** with the 10 rewritten stories and role standardizations.
2. **Resolve blocking clarifications** (ISS-017, ISS-019, ISS-020, ISS-023) before UAT planning for affected stories.
3. **Formalize UR-20 IMS Administrator** role in the BRD role catalog.
4. **Sequence sprint planning** using epic dependencies — EPIC-11 and EPIC-01 must lead MVP waves.
5. **Align acceptance criteria** in `acceptance-criteria.md` with rewritten role names (US-003, US-023, US-026, US-042, US-046, US-081).

---

## Document Control

| Attribute | Detail |
|-----------|--------|
| **Document ID** | US-REV-IMS-001 |
| **Version** | 1.0 |
| **Related Artifacts** | BRD-IMS-001, EPIC-IMS-001, US-001–US-090, AC-001–AC-090 |

---

*End of User Stories Review Document*
