# Separation of Duties (SoD) Rules: Inventory Management System

**Document Owner:** Security Engineer  
**Purpose:** Define Separation of Duties rules that prevent conflicting responsibilities from being assigned to the same user, protecting inventory integrity and financial controls  
**Audience:** Security engineers, internal auditors, system administrators, and compliance officers  
**Scope:** Business SoD rules and control recommendations — no implementation design  
**Based On:** Functional Requirements (FR-084, FR-088), System Permissions (PERM-001–PERM-100), RBAC Matrix, Domain Knowledge (BR-19, BR-21), and Compliance Requirements (NFR-COM-009)

---

## Document Conventions

| Convention | Meaning |
|------------|---------|
| **SOD-xxx** | Separation of Duties rule identifier |
| **PERM-xxx** | Conflicting permission reference |
| **Initiate** | The user who creates, records, or submits the transaction |
| **Approve** | The user who independently authorizes the transaction before it takes effect |

SoD rules apply at the **user** level: the same individual must not hold both sides of a conflicting responsibility pair, whether through a single role or multiple role assignments. Authorized exceptions for small teams must be documented, time-limited, and flagged for audit review per FR-084.

---

## Rule Summary

| Rule ID | Domain | Conflict Type |
|---------|--------|---------------|
| SOD-001 | Procurement | Create and approve purchase order |
| SOD-002 | Procurement | Create and approve purchase requisition |
| SOD-003 | Inventory Control | Perform count and approve count adjustment |
| SOD-004 | Inventory Control | Request and approve stock adjustment |
| SOD-005 | Inventory Control | Request and approve inventory write-off |
| SOD-006 | Network Transfers | Request and approve stock transfer |
| SOD-007 | Inbound Receiving | Receive goods and approve receipt beyond tolerance |
| SOD-008 | Inbound Receiving | Receive goods and approve ad-hoc receipt |
| SOD-009 | Inbound Receiving | Document receipt discrepancy and resolve discrepancy |
| SOD-010 | System Setup | Import initial data and approve initial data import |
| SOD-011 | Returns | Inspect returned goods and approve restock disposition |
| SOD-012 | Returns | Inspect returned goods and approve write-off disposition |
| SOD-013 | Order Fulfillment | Reserve inventory and confirm shipment without verification |
| SOD-014 | Inventory Control | Investigate count variance and approve same variance |
| SOD-015 | Governance | Perform operational transactions and administer user access |
| SOD-016 | Audit | Perform operational transactions and query audit evidence |
| SOD-017 | Finance | Perform operational adjustments and perform financial reconciliation |
| SOD-018 | Procurement | Approve purchase order and receive goods for same PO |
| SOD-019 | Inventory Control | Override safety stock and approve own override |
| SOD-020 | Master Data | Maintain product master and approve count adjustment for same SKU |

---

## Procurement & Replenishment

---

### SOD-001: Create and Approve Purchase Order

| Attribute | Description |
|-----------|-------------|
| **Rule ID** | SOD-001 |
| **Conflicting Responsibilities** | **Initiate:** Create, amend, or cancel purchase order (PERM-024, PERM-025, PERM-026) · **Approve:** Approve purchase order (PERM-069) |
| **Reason** | Purchase orders create binding financial commitments with suppliers. The person who creates the order has a direct interest in its authorization and should not be the same person who approves it. Independent approval ensures orders align with business need, budget, and procurement policy before supplier commitment. |
| **Business Risk** | Unauthorized or fraudulent purchasing; duplicate or unnecessary orders; supplier collusion; budget overruns undetected until payment; weakened procurement audit trail. |
| **Recommendation** | The same user should not both create and approve a purchase order. Assign PERM-024–026 to Buyer role and PERM-069 to Purchasing Manager, COO, or CFO per authority matrix. System must block self-approval and log attempted violations (FR-084, FR-088). |

---

### SOD-002: Create and Approve Purchase Requisition

| Attribute | Description |
|-----------|-------------|
| **Rule ID** | SOD-002 |
| **Conflicting Responsibilities** | **Initiate:** Create purchase requisition (PERM-067) · **Approve:** Approve purchase requisition (PERM-068) |
| **Reason** | Requisitions formalize replenishment need before purchase order creation. Self-approval bypasses the managerial review that validates genuine demand, quantity reasonableness, and alignment with inventory policy. |
| **Business Risk** | Fictitious requisitions leading to unnecessary stock accumulation; circumvention of replenishment discipline; inflated working capital without independent challenge. |
| **Recommendation** | The same user should not both create and approve a purchase requisition. Buyers may create requisitions; Purchasing Manager approves. System must route requisitions to an independent approver before PO conversion. |

---

### SOD-018: Approve Purchase Order and Receive Goods for Same PO

| Attribute | Description |
|-----------|-------------|
| **Rule ID** | SOD-018 |
| **Conflicting Responsibilities** | **Approve:** Approve purchase order (PERM-069) · **Execute:** Receive goods against the same purchase order (PERM-028) |
| **Reason** | The approver who authorized a purchase should not verify receipt of goods for that same order. Independent receiving confirms that physically delivered quantity and condition match what was ordered and approved — preventing acceptance of short, damaged, or fictitious deliveries on self-approved orders. |
| **Business Risk** | Payment for goods never received; acceptance of non-conforming shipments; phantom inventory created through collusive approve-and-receive cycles; supplier fraud undetected. |
| **Recommendation** | The same user should not approve a purchase order and receive goods against that same PO. Receiving Clerk or Warehouse Manager performs receipt; Purchasing Manager approves PO. System should flag when receiver and PO approver share the same user identity on a PO line. |

---

## Inventory Control & Accuracy

---

### SOD-003: Perform Count and Approve Count Adjustment

| Attribute | Description |
|-----------|-------------|
| **Rule ID** | SOD-003 |
| **Conflicting Responsibilities** | **Initiate:** Perform cycle count or full physical count (PERM-038) · **Approve:** Approve count adjustment resulting from that count (PERM-042) |
| **Reason** | Physical counting establishes the evidence base for inventory balance corrections. If the same person counts and approves the resulting adjustment, they can conceal theft, recording errors, or deliberate manipulation without independent detection. Blind count procedures (FR-031) are undermined if the counter also approves. |
| **Business Risk** | Undetected inventory shrinkage and fraud; inflated accuracy metrics that mask chronic discrepancies; unreliable count program undermining financial substantiation and audit confidence. |
| **Recommendation** | The same user should not both perform a physical count and approve the resulting count adjustment. Warehouse Staff and Regional/Store Manager perform counts; Inventory Controller, Warehouse Manager, or Operations Director approve per threshold policy. System must block self-approval of count adjustments (FR-084, BR-19). |

---

### SOD-004: Request and Approve Stock Adjustment

| Attribute | Description |
|-----------|-------------|
| **Rule ID** | SOD-004 |
| **Conflicting Responsibilities** | **Initiate:** Request stock adjustment (PERM-043) · **Approve:** Approve stock adjustment (PERM-044) |
| **Reason** | Stock adjustments directly change on-hand balances. Self-approval allows a user to correct inventory records without independent challenge — whether due to error, negligence, or intent to conceal loss. |
| **Business Risk** | Unauthorized inventory increases or decreases; concealment of theft or damage; manipulation of stock levels to hide fulfillment failures; financial misstatement when adjustments lack independent substantiation. |
| **Recommendation** | The same user should not both request and approve a stock adjustment. Warehouse Manager or Inventory Controller may request; Operations Director or COO approves per threshold. Inventory Controller must not approve adjustments they initiated. System enforces independent approver routing above zero threshold. |

---

### SOD-005: Request and Approve Inventory Write-Off

| Attribute | Description |
|-----------|-------------|
| **Rule ID** | SOD-005 |
| **Conflicting Responsibilities** | **Initiate:** Request inventory write-off (PERM-045) · **Approve:** Approve inventory write-off (PERM-046) |
| **Reason** | Write-offs permanently remove inventory from sellable stock and reduce balance-sheet asset value. Self-approval enables disposal of valuable goods without oversight and is a primary fraud vector in inventory management. |
| **Business Risk** | Theft disguised as write-off; premature disposal of saleable stock; material financial misstatement; audit findings on inadequate write-off controls; unrecoverable asset loss. |
| **Recommendation** | The same user should not both request and approve an inventory write-off. Warehouse Manager may request; Operations Director, COO, or CFO approves per value threshold. Require documented evidence and reason code on every write-off; system blocks self-approval unconditionally for write-offs. |

---

### SOD-014: Investigate Count Variance and Approve Same Variance

| Attribute | Description |
|-----------|-------------|
| **Rule ID** | SOD-014 |
| **Conflicting Responsibilities** | **Initiate:** Investigate count variance (PERM-041) · **Approve:** Approve count adjustment for the same variance (PERM-042) — when the investigator was also the counter (PERM-038) |
| **Reason** | Variance investigation is an objective review of why physical count differs from system records. When the investigator also counted the stock and approves the correction, the investigation provides no independent assurance. |
| **Business Risk** | Biased investigation conclusions; root cause never identified; recurring variances at same location or SKU undetected; false sense of control from completed but ineffective investigations. |
| **Recommendation** | The same user should not investigate and approve a count variance they personally counted. Inventory Controller investigates; a different authorized approver (Operations Director or independent Warehouse Manager) approves material variances. System should link count, investigation, and approval records to detect same-user chains. |

---

### SOD-019: Override Safety Stock and Approve Own Override

| Attribute | Description |
|-----------|-------------|
| **Rule ID** | SOD-019 |
| **Conflicting Responsibilities** | **Initiate:** Reserve inventory or request transfer that would breach safety stock (PERM-052, PERM-071) · **Approve:** Override safety stock protection (PERM-070) |
| **Reason** | Safety stock buffers protect against demand and supply uncertainty. Allowing the same user to create the demand that breaches safety stock and authorize the breach removes the control purpose of the buffer. |
| **Business Risk** | Systematic erosion of safety stock leading to preventable stockouts; priority orders consuming buffer without replenishment plan; network vulnerability to demand spikes. |
| **Recommendation** | The same user should not both trigger a safety stock breach and approve the override. Operations Director or COO approves overrides; frontline fulfillment and purchasing roles cannot self-authorize. System requires documented replenishment plan and independent approver on every override (FR-056). |

---

### SOD-020: Maintain Product Master and Approve Count Adjustment for Same SKU

| Attribute | Description |
|-----------|-------------|
| **Rule ID** | SOD-020 |
| **Conflicting Responsibilities** | **Initiate:** Create or update product master records (PERM-001, PERM-002) · **Approve:** Approve count adjustment for the same product (PERM-042) within a defined review period |
| **Reason** | Product master changes (unit of measure, tracking attributes) can explain or mask count variances. A user who recently altered product data should not approve adjustments for that product without independent review. |
| **Business Risk** | Product data manipulation to justify fraudulent adjustments; UOM changes used to explain away quantity variances; master data integrity compromised by same person who benefits from adjustment approval. |
| **Recommendation** | The same user should not approve a count adjustment for a SKU they modified in product master within the same count cycle. System should flag same-user product master change and count approval within configurable window; route to Operations Director for independent approval. |

---

## Network Transfers

---

### SOD-006: Request and Approve Stock Transfer

| Attribute | Description |
|-----------|-------------|
| **Rule ID** | SOD-006 |
| **Conflicting Responsibilities** | **Initiate:** Request stock transfer (PERM-071) · **Approve:** Approve stock transfer (PERM-072) |
| **Reason** | Inter-location transfers redistribute network inventory and affect service levels at both source and destination. Self-approval allows unauthorized stock movement that can create stockouts, hide shrinkage in transit, or divert stock for improper purposes. |
| **Business Risk** | Unauthorized stock diversion; source location stockouts caused by unreviewed transfers; in-transit loss undetected; network imbalance worsened by uncontrolled movements. |
| **Recommendation** | The same user should not both request and approve a stock transfer. Regional/Store Manager and Warehouse Manager may request; Operations Director or COO approves. System blocks self-approval and enforces source minimum threshold checks (FR-063) before approval routing. |

---

## Inbound Receiving

---

### SOD-007: Receive Goods and Approve Receipt Beyond Tolerance

| Attribute | Description |
|-----------|-------------|
| **Rule ID** | SOD-007 |
| **Conflicting Responsibilities** | **Initiate:** Receive goods and record quantities (PERM-028) · **Approve:** Approve receipt beyond defined tolerance (PERM-032) |
| **Reason** | Receiving is the point where physical goods enter inventory records. Accepting quantities outside PO tolerance without independent review can mask supplier short-shipment, over-billing, or deliberate recording of inflated quantities. |
| **Business Risk** | Payment for undelivered goods; inflated inventory balances (phantom stock); supplier quantity disputes without objective receiving evidence; fulfillment failures when system shows stock that was never received. |
| **Recommendation** | The same user should not both receive goods and approve receipt beyond tolerance. Receiving Clerk records receipt; Warehouse Manager approves tolerance exceptions after physical verification. System auto-accepts within tolerance; routes exceptions to independent approver. |

---

### SOD-008: Receive Goods and Approve Ad-Hoc Receipt

| Attribute | Description |
|-----------|-------------|
| **Rule ID** | SOD-008 |
| **Conflicting Responsibilities** | **Initiate:** Receive goods without purchase order reference (PERM-028) · **Approve:** Approve ad-hoc receipt exception (PERM-031) |
| **Reason** | Ad-hoc receipts bypass standard procurement controls. The person physically receiving goods should not also authorize the control exception that permits receipt without a PO — this would eliminate procurement oversight entirely for that transaction. |
| **Business Risk** | Unauthorized inbound inventory; goods received outside procurement policy; payment disputes with no PO reference; uncontrolled inventory increases that bypass replenishment discipline. |
| **Recommendation** | The same user should not both receive goods and approve ad-hoc receipt. Receiving Clerk records receipt attempt; Warehouse Manager or Purchasing Manager approves ad-hoc exception with documented reason before stock is accepted. System holds receipt in pending state until exception approved (FR-017). |

---

### SOD-009: Document Receipt Discrepancy and Resolve Discrepancy

| Attribute | Description |
|-----------|-------------|
| **Rule ID** | SOD-009 |
| **Conflicting Responsibilities** | **Initiate:** Document receipt discrepancy (PERM-029) · **Approve:** Resolve receipt discrepancy (PERM-030) |
| **Reason** | Discrepancy documentation records the receiver's claim about quantity or condition variance. Resolution adjudicates supplier accountability and determines final accepted quantity. Same-user resolution allows the receiver to unilaterally close disputes in their own favor. |
| **Business Risk** | Supplier short-shipments accepted without challenge; fictitious over-receipts resolved to inflate inventory; supplier credits not pursued; chronic receiving errors never corrected. |
| **Recommendation** | The same user should not both document and resolve a receipt discrepancy. Receiving Clerk documents; Purchasing Manager or Warehouse Manager resolves with supplier. System routes open discrepancies to purchasing for independent resolution. |

---

## Returns Management

---

### SOD-011: Inspect Returned Goods and Approve Restock Disposition

| Attribute | Description |
|-----------|-------------|
| **Rule ID** | SOD-011 |
| **Conflicting Responsibilities** | **Initiate:** Inspect returned goods (PERM-079) · **Approve:** Restock returned inventory (PERM-080) |
| **Reason** | Return inspection determines whether goods are resalable. Self-approval of restock allows damaged, used, or non-conforming returns to re-enter sellable inventory without independent quality confirmation. |
| **Business Risk** | Defective products shipped to customers as new; customer complaints and returns escalation; brand damage; inflated sellable inventory from non-resalable goods. |
| **Recommendation** | The same user should not both inspect returned goods and approve restock for the same return. Inspector records outcome; Warehouse Manager or Inventory Controller authorizes restock based on inspection result. System requires inspection record before restock transaction is enabled. |

---

### SOD-012: Inspect Returned Goods and Approve Write-Off Disposition

| Attribute | Description |
|-----------|-------------|
| **Rule ID** | SOD-012 |
| **Conflicting Responsibilities** | **Initiate:** Inspect returned goods (PERM-079) · **Approve:** Write off returned inventory (PERM-081) |
| **Reason** | Write-off disposition permanently removes return quantity from inventory. Inspector self-approving write-off can dispose of valuable returnable goods without oversight or divert goods while recording a write-off. |
| **Business Risk** | Theft of returnable goods disguised as write-off; customer refunds issued while goods are resold informally; inaccurate return processing metrics. |
| **Recommendation** | The same user should not both inspect returned goods and approve write-off for the same return. Inspector records condition; Warehouse Manager approves write-off with reason code. Align with SOD-005 write-off approval thresholds for high-value returns. |

---

## Order Fulfillment

---

### SOD-013: Reserve Inventory and Confirm Shipment Without Verification

| Attribute | Description |
|-----------|-------------|
| **Rule ID** | SOD-013 |
| **Conflicting Responsibilities** | **Initiate:** Reserve inventory for order (PERM-052) · **Execute:** Confirm shipment and deduct inventory (PERM-056) — without pick verification (PERM-055) by a second person or supervisor |
| **Reason** | Reservation commits stock to an order; shipment confirmation permanently deducts inventory. When the same user reserves and ships without independent pick verification, they can ship incorrect quantities or ship against non-existent stock while system records show fulfillment. |
| **Business Risk** | Inventory deducted without physical shipment; customer orders marked shipped but not delivered; ATP corrupted by false shipment confirmations; revenue recognized without goods movement. |
| **Recommendation** | The same user should not reserve inventory, execute pick/pack, and confirm shipment as a single unchecked action. Picker/Packer executes pick (PERM-055); Warehouse Manager or system workflow verifies before shipment confirmation (PERM-056). For small teams, require supervisor confirmation on shipment rather than same-user end-to-end processing. |

---

## System Setup & Master Data

---

### SOD-010: Import Initial Data and Approve Initial Data Import

| Attribute | Description |
|-----------|-------------|
| **Rule ID** | SOD-010 |
| **Conflicting Responsibilities** | **Initiate:** Import initial master data and opening stock balances (PERM-015) · **Approve:** Approve initial data import activation (PERM-016) |
| **Reason** | Go-live data imports establish the inventory baseline for all future transactions. Self-approval allows embedded errors, inflated opening balances, or fraudulent baseline data to enter production records without validation. |
| **Business Risk** | Go-live with systematically wrong inventory positions; cascading fulfillment errors from day one; financial misstatement from incorrect opening balances; costly remediation after operational dependence on bad baseline. |
| **Recommendation** | The same user should not both import and approve initial data activation. Operations Director prepares import; Inventory Controller validates and approves activation. System holds imported data in staging until independent approval (FR-090). |

---

## Governance, Administration & Audit

---

### SOD-015: Perform Operational Transactions and Administer User Access

| Attribute | Description |
|-----------|-------------|
| **Rule ID** | SOD-015 |
| **Conflicting Responsibilities** | **Operational:** Any inventory transaction permission (PERM-028–PERM-081) · **Administrative:** Manage user accounts or assign roles and location scope (PERM-095, PERM-096) |
| **Reason** | User administration determines who can perform inventory transactions. A user with both operational and administrative access can grant themselves additional permissions, cover audit trails by reassigning roles, or create orphaned accounts to obscure activity. |
| **Business Risk** | Privilege escalation; fraud concealed through self-granted permissions; audit trail attribution compromised; inability to demonstrate access control effectiveness to auditors. |
| **Recommendation** | The same user should not perform routine inventory transactions and administer user accounts or role assignments. Reserve PERM-095 and PERM-096 exclusively for System Administrator role with no operational inventory permissions. System alerts when role assignment creates operational + administrative conflict. |

---

### SOD-016: Perform Operational Transactions and Query Audit Evidence

| Attribute | Description |
|-----------|-------------|
| **Rule ID** | SOD-016 |
| **Conflicting Responsibilities** | **Operational:** Create or approve inventory transactions (PERM-028–PERM-046, PERM-024–PERM-069) · **Audit:** Query audit evidence or view control breach records (PERM-099, PERM-100) — for same user in operational roles |
| **Reason** | Audit query access reveals investigation patterns, sampling methodologies, and detected control weaknesses. Operational users with audit access can tailor behavior to avoid detection or identify which transactions are under review. |
| **Business Risk** | Fraudsters evade detection by monitoring audit queries; control testing compromised; investigation integrity undermined; regulatory and external audit findings on inadequate access separation. |
| **Recommendation** | Operational users should not hold audit evidence query permissions. Restrict PERM-099 and PERM-100 to Internal Auditor and Finance Manager oversight roles. External Auditor receives time-limited read access during audit period only. Operational roles may view movement history (PERM-023) but not audit investigation tools. |

---

### SOD-017: Perform Operational Adjustments and Perform Financial Reconciliation

| Attribute | Description |
|-----------|-------------|
| **Rule ID** | SOD-017 |
| **Conflicting Responsibilities** | **Operational:** Request or approve stock adjustments and write-offs (PERM-043–PERM-046) · **Financial:** Perform financial inventory reconciliation (PERM-094) |
| **Reason** | Financial reconciliation independently verifies that operational inventory records align with general ledger balances. The person creating or approving operational adjustments should not also reconcile those same adjustments — this compromises the independence of the reconciliation control. |
| **Business Risk** | Adjustments approved and reconciled by same person never challenged; material misstatement undetected at month-end; weak finance oversight over operational inventory changes; audit findings on lack of reconciliation independence. |
| **Recommendation** | The same user should not both approve inventory adjustments and perform financial reconciliation for the same period. Finance Manager reconciles; Operations Director approves adjustments. Finance may view adjustment logs (PERM-084) but must not hold PERM-044 or PERM-046 on the same account. |

---

## SoD Rule Matrix (Quick Reference)

| Rule | Initiate Responsibility | Approve / Conflicting Responsibility |
|------|------------------------|--------------------------------------|
| SOD-001 | Create purchase order | Approve purchase order |
| SOD-002 | Create purchase requisition | Approve purchase requisition |
| SOD-003 | Perform physical count | Approve count adjustment |
| SOD-004 | Request stock adjustment | Approve stock adjustment |
| SOD-005 | Request inventory write-off | Approve inventory write-off |
| SOD-006 | Request stock transfer | Approve stock transfer |
| SOD-007 | Receive goods | Approve receipt beyond tolerance |
| SOD-008 | Receive goods (ad-hoc) | Approve ad-hoc receipt |
| SOD-009 | Document receipt discrepancy | Resolve receipt discrepancy |
| SOD-010 | Import initial data | Approve initial data import |
| SOD-011 | Inspect returned goods | Restock returned inventory |
| SOD-012 | Inspect returned goods | Write off returned inventory |
| SOD-013 | Reserve inventory | Confirm shipment (without pick verification) |
| SOD-014 | Count and investigate variance | Approve same variance |
| SOD-015 | Operational transactions | Administer user access |
| SOD-016 | Operational transactions | Query audit evidence |
| SOD-017 | Approve adjustments | Perform financial reconciliation |
| SOD-018 | Approve purchase order | Receive goods for same PO |
| SOD-019 | Breach safety stock | Approve safety stock override |
| SOD-020 | Modify product master | Approve count adjustment for same SKU |

---

## Exception Handling

| Scenario | Policy | Controls |
|----------|--------|----------|
| **Small warehouse team** | Documented authorized exception with named approver delegate | Time-limited exception code; enhanced audit flag on every transaction; Internal Auditor review quarterly |
| **Approver on leave** | Formal delegate assignment by management | Delegate acts under own identity; original approver cannot perform both sides; delegation logged and expires automatically |
| **Emergency receiving** | Ad-hoc receipt with post-facto review | PERM-031 approved by manager within 24 hours; FR-088 logs policy breach if approval delayed |
| **Undefined action pair** | Conservative default | System blocks conflicting combination and alerts System Administrator per FR-084 acceptance criteria |

---

## Monitoring and Compliance

| Control | Frequency | Owner |
|---------|-----------|-------|
| SoD rule compliance in role assignments | On every role change | System Administrator |
| Self-approval attempt log review | Weekly | Internal Auditor |
| SoD violation trend analysis | Monthly | Internal Auditor + COO |
| Full SoD control effectiveness test | Quarterly | Internal Auditor |
| Role-permission recertification | Semi-annual | Operations Director + HR |

System must log all blocked self-approval attempts and SoD violations per FR-088 and NFR-LOG-008 for audit evidence.

---

## Related Requirements

| Requirement | Relevance |
|-------------|-----------|
| FR-084 | Enforce segregation of duties — primary functional requirement |
| FR-088 | Detect and record control policy breaches including self-approval |
| FR-037 | Route adjustments above threshold to independent approver |
| BR-19 | Industry rule — segregation of duties for count and adjustment |
| BR-21 | Approval thresholds proportional to financial impact |
| NFR-COM-009 | Segregation of financially material transactions |
| NFR-SEC-007 | Automated SoD enforcement in production |

---

## Document Summary

This document defines **20 Separation of Duties rules** covering procurement, inventory control, transfers, receiving, returns, fulfillment, system setup, and governance domains. Each rule identifies conflicting responsibilities, the control reason, business risk if violated, and a specific recommendation aligned with the RBAC matrix and organizational role hierarchy.

These rules must be enforced by the system (FR-084), reflected in role assignment design, and tested during internal audit cycles. Role-to-permission assignments that violate SoD rules require documented exception approval — not silent override.

---

*End of Separation of Duties Rules Document*
