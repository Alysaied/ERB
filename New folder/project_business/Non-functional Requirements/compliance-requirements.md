# Compliance Requirements: Inventory Management System

**Document Owner:** Security Engineer  
**Purpose:** Define business-level compliance requirements for the Inventory Management System  
**Audience:** Business stakeholders, legal, finance, internal audit, product owners, operations leadership, and delivery teams  
**Scope:** Compliance requirements and required business controls only — no implementation design, certification procedures, or technology selection  
**Based On:** Business Constraints (LC-01 – LC-05, TEC-06), Security Requirements (NFR-SEC), Logging Requirements (NFR-LOG), Backup & DR Requirements (NFR-BDR), Functional Requirements (FR-081 – FR-090), Success Metrics, and Industry Standards (Domain Knowledge)

---

## How to Read This Document

| Field | Description |
|-------|-------------|
| **Requirement ID** | Unique identifier for traceability (NFR-COM-xxx) |
| **Regulation or Policy** | Applicable law, regulation, industry standard, or organizational policy driving the requirement |
| **Description** | What the business must ensure the IMS supports from a compliance perspective |
| **Business Impact** | Consequences of non-compliance — financial, legal, operational, and reputational |
| **Required Controls** | Business controls the IMS and operating procedures must enforce or enable |
| **Priority** | MoSCoW priority aligned with project phasing |

### Compliance Scope

The IMS processes and stores data that falls under multiple regulatory and governance domains: personal data of employees and customers, financial inventory records, audit evidence, and operational data used in customer commitments. Compliance is a shared responsibility between the system capability, defined business processes, and organizational policy enforcement.

### Priority Definitions

| Priority | Meaning | Release Alignment |
|----------|---------|-------------------|
| **Must Have** | Legal or audit non-negotiable for go-live; absence creates regulatory exposure or failed audit | Phase 1 — MVP (Months 0–6) |
| **Should Have** | Required for full governance maturity and external audit readiness after MVP | Phase 2 (Months 6–12) |
| **Could Have** | Required if specific industry vertical or jurisdiction mandates apply | Phase 3 or conditional |

---

## Requirements Summary

| Category | Requirement IDs | Count |
|----------|-----------------|-------|
| Data Privacy | NFR-COM-001 – NFR-COM-005 | 5 |
| Financial Records | NFR-COM-006 – NFR-COM-009 | 4 |
| Auditability | NFR-COM-010 – NFR-COM-014 | 5 |
| Industry Regulations | NFR-COM-015 – NFR-COM-018 | 4 |
| Record Retention | NFR-COM-019 – NFR-COM-022 | 4 |
| **Total** | | **22** |

---

## Category 1: Data Privacy

*Personal data processed by the IMS must comply with applicable data protection law and organizational privacy policy*

---

### NFR-COM-001: General Data Protection Regulation (GDPR) — Lawful Processing

| Attribute | Detail |
|-----------|--------|
| **Regulation or Policy** | EU General Data Protection Regulation (GDPR) and equivalent local data protection laws (LC-01) |
| **Description** | Personal data held in the IMS — including employee user accounts, user activity attributions, and customer-linked order and fulfillment records — must be processed only for documented, legitimate business purposes with a lawful basis recorded in the organization's Record of Processing Activities (ROPA) |
| **Business Impact** | Unlawful processing exposes the organization to regulatory fines (up to 4% of annual turnover under GDPR), data subject complaints, restrictions on processing, and reputational damage. Non-compliance may halt use of customer-linked fulfillment data in B2C operations |
| **Required Controls** | Published ROPA entry for IMS before go-live; data minimization — collect only personal data necessary for inventory operations; purpose limitation — personal data used only for stated purposes; Legal sign-off on processing activities; annual ROPA review |
| **Priority** | Must Have |

---

### NFR-COM-002: Data Subject Rights

| Attribute | Detail |
|-----------|--------|
| **Regulation or Policy** | GDPR Articles 15–22 (and equivalent local rights); organizational privacy policy (LC-01) |
| **Description** | The business must be able to respond to data subject rights requests — access, rectification, erasure, restriction, and portability — for personal data held in IMS user accounts, activity logs, and customer-linked fulfillment records within applicable legal timeframes |
| **Business Impact** | Failure to respond within statutory deadlines (typically 30 days under GDPR) triggers regulatory complaint and fine risk. Inability to correct inaccurate employee or customer data undermines data accuracy obligations and customer trust |
| **Required Controls** | Documented data subject request procedure owned by Legal; IMS supports identification and export of personal data by subject; erasure/anonymization applied where legally required; conflict resolution procedure when erasure conflicts with audit retention (NFR-COM-019); requests logged and tracked to completion |
| **Priority** | Must Have |

---

### NFR-COM-003: Privacy by Design and Data Minimization

| Attribute | Detail |
|-----------|--------|
| **Regulation or Policy** | GDPR Article 25 (Privacy by Design); organizational data classification policy (NFR-SEC-017) |
| **Description** | IMS user interfaces, reports, and exports must display and distribute only the personal data necessary for each role — customer contact details, employee identifiers, and order-linked personal information restricted to roles with legitimate need |
| **Business Impact** | Over-exposure of personal data to warehouse and sales roles violates the minimum-necessary principle, increases insider breach risk, and expands regulatory scope. Privacy complaints and audit findings damage employee and customer trust |
| **Required Controls** | Role-based field restriction per data classification register; customer contact data visible only to sales and customer service roles; privacy impact assessment (PIA) completed and approved by Legal before go-live; annual review of role-data access matrix |
| **Priority** | Should Have |

---

### NFR-COM-004: Personal Data Retention and Disposal

| Attribute | Detail |
|-----------|--------|
| **Regulation or Policy** | GDPR Article 5(1)(e) (Storage Limitation); organizational retention schedule (LC-01, NFR-SEC-031) |
| **Description** | Personal data in the IMS must be retained only for the period necessary for its business purpose and deleted or anonymized when no longer required — balanced against overriding legal retention for financial and audit records |
| **Business Impact** | Indefinite retention increases regulatory exposure and subject rights request volume. Premature deletion of personal data needed for audit attribution creates compliance conflict and investigation gaps |
| **Required Controls** | Published retention schedule for IMS personal data categories approved by Legal; deactivated employee personal data anonymized within **90 days** except where audit attribution requires retention; annual retention compliance review; disposal actions logged |
| **Priority** | Should Have |

---

### NFR-COM-005: Cross-Border Data Transfer Compliance

| Attribute | Detail |
|-----------|--------|
| **Regulation or Policy** | GDPR Chapter V (International Transfers); applicable local data residency laws |
| **Description** | If IMS data — including personal data and inventory records — is stored or processed outside the data subject's jurisdiction, the organization must ensure an approved transfer mechanism is in place and documented |
| **Business Impact** | Unlawful cross-border transfer invalidates processing activity and may require suspension of IMS operations in affected regions. Geographic expansion plans (NFR-SCAL-018) depend on lawful data handling |
| **Required Controls** | Data residency and transfer assessment completed by Legal before go-live; transfer mechanism documented (e.g., adequacy decision, standard contractual clauses); assessment updated when hosting geography changes; geographic expansion gated on Legal approval |
| **Priority** | Could Have |

---

## Category 2: Financial Records

*Inventory records that substantiate financial reporting must meet accounting, tax, and corporate governance obligations*

---

### NFR-COM-006: Financial Record Retention — Tax and Corporate Law

| Attribute | Detail |
|-----------|--------|
| **Regulation or Policy** | Applicable tax law and corporate record-keeping statutes (LC-02); typically **5–7 years** depending on jurisdiction |
| **Description** | Inventory transaction records, adjustment logs, write-off documentation, valuation summaries, and month-end reconciliation outputs must be retained for the full statutory period and remain retrievable for tax examination, financial audit, and legal proceedings |
| **Business Impact** | Inability to produce historical inventory records during tax audit risks reassessment, penalties, and interest. Failed financial audit opinions affect investor confidence, debt covenants, and executive accountability. CFO cannot substantiate balance sheet inventory values (KPI-20) |
| **Required Controls** | Retention period confirmed by Legal and CFO (minimum **7 years** unless longer jurisdiction applies); IMS supports retrieval of transaction and valuation records for full retention period; premature disposal prohibited and logged; external auditor read access to historical records (NFR-COM-012) |
| **Priority** | Must Have |

---

### NFR-COM-007: Inventory Valuation and Financial Reconciliation

| Attribute | Detail |
|-----------|--------|
| **Regulation or Policy** | Applicable accounting standards (e.g., IFRS IAS 2 / US GAAP ASC 330 — Inventories); organizational finance policy |
| **Description** | IMS must support operational-to-financial inventory reconciliation — providing quantity summaries, adjustment logs, write-off records, and period-end snapshots that finance can use to substantiate inventory valuation on the balance sheet |
| **Business Impact** | Unreconciled inventory records cause material misstatement of financial statements, delayed month-end close (KPI-21), and valuation variance between operations and finance (KPI-20). Material misstatement triggers restatement, regulatory filing correction, and audit qualification |
| **Required Controls** | Period-end inventory quantity summary exportable by location and category (FR-089); adjustment and write-off log with reason codes exportable for finance; reconciliation procedure documented between Operations and Finance; monthly reconciliation meeting per business assumption BA-06; variance ≤ 2% target (KPI-20) |
| **Priority** | Must Have |

---

### NFR-COM-008: Shrinkage, Write-Off, and Adjustment Substantiation

| Attribute | Detail |
|-----------|--------|
| **Regulation or Policy** | Accounting standards for inventory write-downs; organizational finance and loss prevention policy; LC-02 |
| **Description** | Every inventory adjustment and write-off recorded in the IMS must include a mandatory reason code, user attribution, timestamp, and — for material values — independent approval — providing substantiation for financial impact of shrinkage and obsolescence |
| **Business Impact** | Unsubstantiated adjustments are treated as potential fraud or misstatement by auditors. Undocumented shrinkage inflates gross margin inaccurately (KPI-09), hides loss prevention failures, and prevents targeted corrective action |
| **Required Controls** | Mandatory reason codes for all adjustments (FR functional requirements); approval workflow for adjustments above defined value threshold (NFR-SEC-008); reason code included in audit trail and financial export; monthly shrinkage review per business process BP-15 |
| **Priority** | Must Have |

---

### NFR-COM-009: Segregation of Financially Material Transactions

| Attribute | Detail |
|-----------|--------|
| **Regulation or Policy** | COSO Internal Control Framework; SOX Section 404 (if applicable to organization); organizational control policy |
| **Description** | Financially material inventory transactions — high-value adjustments, write-offs, and opening balance establishment — must require independent approval by a person who did not initiate the transaction, with the control enforced by the IMS |
| **Business Impact** | Absence of segregation of duties is a material weakness in internal controls over financial reporting. External auditors issue adverse opinions; public companies face SEC scrutiny. Fraud and undetected error risk increases materially |
| **Required Controls** | Segregation of duties enforced by IMS (FR-084, NFR-SEC-007); approval authority matrix documented and signed by Internal Auditor; self-approval blocked for defined transaction types; authorized small-team exceptions documented with expiry; control tested in internal audit cycle |
| **Priority** | Must Have |

---

## Category 3: Auditability

*The IMS must enable internal and external auditors to verify control effectiveness and transaction integrity*

---

### NFR-COM-010: Complete and Immutable Audit Trail

| Attribute | Detail |
|-----------|--------|
| **Regulation or Policy** | COSO — Monitoring Activities; organizational audit charter; KPI-24 (Audit Trail Completeness Rate — 100%) |
| **Description** | Every inventory quantity change must be recorded in an immutable audit trail capturing before and after balances, transaction type, reason code, user identity, location, and timestamp — with no ability to alter or delete records through normal business use |
| **Business Impact** | Incomplete or tamperable audit trails are material control deficiencies. Internal audit cannot verify transaction integrity; external audit scope expands; shrinkage and fraud investigations lack evidence. KPI-24 at less than 100% is an initiative failure criterion |
| **Required Controls** | Audit trail for all balance-affecting transactions (FR-086, NFR-LOG-010); audit records immutable through standard user and administrator functions; audit trail queryable by product, location, user, date range, and transaction type; completeness monitored (KPI-24) |
| **Priority** | Must Have |

---

### NFR-COM-011: User Activity and Accountability Logging

| Attribute | Detail |
|-----------|--------|
| **Regulation or Policy** | COSO — Control Activities; organizational loss prevention policy; FR-083 |
| **Description** | All material user actions — inventory transactions, approvals, configuration changes, data exports, and authentication events — must be logged with user identity, action type, timestamp, and affected entity to support accountability and investigation |
| **Business Impact** | Without activity logs, the business cannot attribute shrinkage, investigate discrepancies, or demonstrate who performed each action during audit. Loss prevention cases fail; employment disciplinary actions lack evidence; audit findings cite inadequate monitoring |
| **Required Controls** | User activity logging for all material actions (NFR-LOG-007); unique user authentication — no shared accounts (NFR-SEC-001); activity logs retained per retention schedule (NFR-COM-020); logs queryable by administrators and auditors |
| **Priority** | Must Have |

---

### NFR-COM-012: Independent Auditor Access

| Attribute | Detail |
|-----------|--------|
| **Regulation or Policy** | External audit standards (ISA / PCAOB); organizational audit committee requirements; FR-087 |
| **Description** | Internal and external auditors must be granted read-only access to audit trails, transaction histories, user activity logs, count records, and control evidence — without ability to modify inventory data, user accounts, or audit records |
| **Business Impact** | Denying or delaying auditor access extends audit timelines, increases audit fees, and risks qualified opinions. Auditors who cannot independently verify controls expand testing scope — disrupting operations and increasing cost |
| **Required Controls** | Dedicated auditor read-only role (NFR-SEC-016); auditors can query and export evidence packages by period and location; zero auditor accounts with write permissions; audit evidence exportable within **15 minutes** (NFR-PERF-026); annual access provision for external audit |
| **Priority** | Must Have |

---

### NFR-COM-013: Control Policy Breach Detection and Recording

| Attribute | Detail |
|-----------|--------|
| **Regulation or Policy** | COSO — Monitoring Activities; organizational control policy; FR-088 |
| **Description** | The IMS must detect and record instances where operational actions breach defined control policies — including receipt without purchase order, self-approval attempts, safety stock overrides, and unauthorized adjustments — for governance review |
| **Business Impact** | Control breaches discovered only at year-end audit indicate monitoring failure. Undetected breaches allow fraud and error to accumulate. Governance cannot demonstrate proactive control environment to board and regulators |
| **Required Controls** | Policy breach and authorized exception logging (FR-088, NFR-LOG-016); governance review report including breach trends by location and type; quarterly review by Internal Auditor and Operations Director; breach rate trended and reported to audit committee |
| **Priority** | Should Have |

---

### NFR-COM-014: Physical Inventory Substantiation

| Attribute | Detail |
|-----------|--------|
| **Regulation or Policy** | COSO — Physical Controls; industry inventory accuracy benchmarks; organizational count program policy |
| **Description** | The IMS must support cycle count and full physical count programs that produce auditable evidence of inventory substantiation — including count records, variance investigation, independent approval, and adjustment posting |
| **Business Impact** | External auditors require physical inventory substantiation for balance sheet inventory. Without auditable count evidence, auditors expand sample sizes, impose qualifications, or require additional procedures — increasing cost and management burden |
| **Required Controls** | Cycle count and full count workflows with variance recording (FR functional requirements); count variance requires independent approval (segregation of duties); count records retained for audit period; inventory accuracy rate ≥ 95% (KPI-01) measured and reported |
| **Priority** | Must Have |

---

## Category 4: Industry Regulations

*IMS data and commitments must comply with industry-specific and trade regulations applicable to the organization's operations*

---

### NFR-COM-015: Consumer Protection — Accurate Availability and Delivery Commitments

| Attribute | Detail |
|-----------|--------|
| **Regulation or Policy** | Applicable consumer protection and trade practice laws (LC-05); e-commerce and distance selling regulations where B2C applies |
| **Description** | Available-to-promise data and delivery commitments derived from IMS stock positions must be accurate and defensible — the organization must not display or communicate stock availability to customers that the IMS cannot substantiate |
| **Business Impact** | Overstating availability to B2C customers creates legal exposure under consumer protection law — including claims for misleading representation, cancellation rights, and compensation. Regulatory enforcement and customer complaints damage brand and B2C channel viability |
| **Required Controls** | ATP calculated from on-hand minus reservations and non-sellable holds (FR functional requirements); sales and customer service trained on ATP meaning and limitations; B2C availability display rules reviewed by Legal before channel use; stock-related order cancellation rate monitored (KPI-13 ≤ 2%) |
| **Priority** | Must Have |

---

### NFR-COM-016: Product Identification Standards

| Attribute | Detail |
|-----------|--------|
| **Regulation or Policy** | GS1 Global Standards (GTIN, barcode identification); organizational product data governance policy |
| **Description** | Product master data in the IMS must support standardized product identification — including SKU, barcode or GTIN, and unit of measure — consistent with industry identification standards used in receiving, picking, and customer fulfillment |
| **Business Impact** | Non-standard product identification causes receiving errors, mis-picks, and inability to exchange data with suppliers and retail partners. GS1 non-compliance blocks trade with major retailers and distributors requiring standardized identification |
| **Required Controls** | Product master records include standardized identifier fields (FR-001); barcode scanning supported for operational lookup; duplicate and conflicting identifiers blocked at product creation; Inventory Controller owns identifier quality (BA-03) |
| **Priority** | Must Have |

---

### NFR-COM-017: Employment and Labor Law — Performance Monitoring

| Attribute | Detail |
|-----------|--------|
| **Regulation or Policy** | Applicable employment contracts, collective bargaining agreements, and labor regulations (LC-03, BA-38) |
| **Description** | IMS-derived performance metrics — including movement recording compliance rates, transaction volumes per user, and system activity logs used for performance management — must comply with employment law, union agreements, and organizational HR policy before enforcement |
| **Business Impact** | Using system compliance metrics for disciplinary action without legal review exposes the organization to unfair dismissal claims, union grievances, and work stoppages. Mandatory recording policies enforced without labor consultation are unenforceable at unionized locations |
| **Required Controls** | Movement recording compliance metrics (KPI-23) reviewed by HR and Legal before use in performance management; union consultation completed at unionized locations before go-live; activity logs used for investigation — not automated performance scoring — without HR policy framework |
| **Priority** | Must Have |

---

### NFR-COM-018: Lot and Batch Traceability — Baseline Capture

| Attribute | Detail |
|-----------|--------|
| **Regulation or Policy** | Industry traceability expectations (GS1, food safety, product safety regulations); organizational quality policy; conditional on regulated product handling |
| **Description** | Where the organization handles products requiring lot or batch traceability — including expiry-dated goods, recall-sensitive products, or regulated categories — the IMS must capture and retain lot or batch identifiers at receipt, movement, and fulfillment to support targeted recall and quality investigation |
| **Business Impact** | Inability to identify affected lots during a product defect or recall forces full product-line recall — vastly more expensive and damaging than targeted lot recall. Regulatory penalties apply in food, pharmaceutical, and consumer safety jurisdictions. Consumer harm creates legal liability |
| **Required Controls** | Lot/batch identifier captured at receipt and fulfillment where product category requires it; lot-level movement history queryable; quarantine workflow excludes non-compliant stock from sellable availability; recall scenario drill documented annually if regulated products in scope; **Note:** dedicated regulatory compliance modules are out of project scope — minimum capture and query capability required |
| **Priority** | Could Have |

---

## Category 5: Record Retention

*Records must be retained, protected, and disposed of in accordance with legal and governance obligations*

---

### NFR-COM-019: Unified Record Retention Schedule

| Attribute | Detail |
|-----------|--------|
| **Regulation or Policy** | LC-02 (Financial Record Retention); GDPR Article 5(1)(e); organizational records management policy |
| **Description** | The business must maintain a unified retention schedule for all IMS record categories — inventory transactions, audit trails, security logs, personal data, valuation reports, and configuration change history — with retention periods approved by Legal, CFO, and Inventory Controller |
| **Business Impact** | Inconsistent retention — destroying financial records too early or keeping personal data too long — creates simultaneous audit failure and privacy violation risk. Without a unified schedule, departments apply conflicting rules |
| **Required Controls** | Retention schedule published before go-live; categories mapped to retention period (minimum **7 years** for financial and audit records); schedule reviewed annually; disposal actions require Legal approval and dual authorization; disposal logged |
| **Priority** | Must Have |

---

### NFR-COM-020: Audit and Security Log Retention

| Attribute | Detail |
|-----------|--------|
| **Regulation or Policy** | LC-02; COSO — Monitoring; NFR-LOG-027; NFR-SEC-015 |
| **Description** | Audit trails, user activity logs, and security event logs must be retained for the full financial record retention period — minimum **7 years** — and remain queryable and exportable for audit, investigation, and legal proceedings |
| **Business Impact** | Log destruction before the audit window closes invalidates control testing for historical periods. Security investigations of fraud discovered years after the event require historical logs. Legal discovery demands producible records |
| **Required Controls** | Logs retained ≥ **7 years**; protected backup copies include audit and security logs (NFR-BDR-006); log immutability enforced (NFR-LOG-026); audit evidence export within **15 minutes**; annual retrieval test from archived logs |
| **Priority** | Must Have |

---

### NFR-COM-021: Legal Hold and Litigation Preservation

| Attribute | Detail |
|-----------|--------|
| **Regulation or Policy** | Applicable civil procedure and evidence preservation law; organizational legal hold policy |
| **Description** | When the organization is subject to legal hold or litigation involving inventory, supplier, customer, or employment matters, IMS records within the hold scope must be preserved and exempt from routine disposal until Legal releases the hold |
| **Business Impact** | Spoliation of evidence during litigation results in adverse inference rulings, sanctions, and case loss. Destroying IMS records subject to legal hold — even inadvertently through routine retention — creates severe legal exposure |
| **Required Controls** | Legal hold notification procedure includes IMS record scope; hold flag prevents automated disposal of affected records; System Administrator receives hold instructions from Legal; hold releases documented; annual legal hold procedure test |
| **Priority** | Should Have |

---

### NFR-COM-022: Supplier and Commercial Record Compatibility

| Attribute | Detail |
|-----------|--------|
| **Regulation or Policy** | Existing supplier and commercial contracts (LC-04); organizational procurement policy |
| **Description** | IMS receiving records, purchase order references, and dispute documentation must remain compatible with documentation standards and retention requirements defined in existing supplier contracts — without requiring suppliers to adopt new formats without contract amendment |
| **Business Impact** | Receiving records that do not match contractually agreed documentation weaken the organization's position in supplier quantity and quality disputes. Inability to produce PO-linked receipt evidence during arbitration loses commercial claims |
| **Required Controls** | Receiving workflow captures PO reference and supplier documentation fields per contract standards; receipt dispute records retained for contract limitation period; ad-hoc receipt requires authorized exception and documented reason; procurement policy aligned with IMS receiving design |
| **Priority** | Must Have |

---

## Compliance Control Matrix (Summary)

| Domain | Primary Regulations | Key Required Controls | Priority |
|--------|--------------------|-----------------------|----------|
| **Data Privacy** | GDPR, local privacy law | ROPA, subject rights, minimization, retention | Must / Should |
| **Financial Records** | Tax law, IFRS/GAAP, COSO/SOX | Retention, reconciliation, substantiation, segregation | Must Have |
| **Auditability** | COSO, ISA/PCAOB, KPI-24 | Immutable audit trail, activity logs, auditor access | Must Have |
| **Industry Regulations** | Consumer protection, GS1, labor law, traceability | ATP accuracy, product ID, HR review, lot capture | Must / Conditional |
| **Record Retention** | LC-02, GDPR, legal hold | Unified schedule, 7-year logs, legal hold, supplier records | Must / Should |

---

## Priority Summary

| Priority | Count | Requirement IDs |
|----------|-------|-----------------|
| **Must Have** | 16 | NFR-COM-001 – 002, 006 – 012, 014 – 017, 019 – 020, 022 |
| **Should Have** | 4 | NFR-COM-003 – 004, 013, 021 |
| **Could Have** | 2 | NFR-COM-005, 018 |
| **Total** | 22 | |

---

## Traceability

| Compliance Requirement | Related Business Constraints | Related Functional / NFR Requirements |
|--------------------------|------------------------------|--------------------------------------|
| NFR-COM-001 – 005 | LC-01 | NFR-SEC-029 – 032 |
| NFR-COM-006 – 009 | LC-02 | FR-089, NFR-BDR-005, KPI-20, KPI-21 |
| NFR-COM-010 – 014 | KPI-24 | FR-086 – 088, NFR-LOG-010 – 016 |
| NFR-COM-015 | LC-05 | FR-023 – 028, KPI-13, KPI-19 |
| NFR-COM-016 | GS1 standards | FR-001 – 004 |
| NFR-COM-017 | LC-03, BA-38 | KPI-23, FR-083 |
| NFR-COM-018 | Domain Knowledge #17 | Project scope boundary note |
| NFR-COM-019 – 022 | LC-02, LC-04 | NFR-BDR-005 – 008, NFR-LOG-027 |

---

## Conditional Applicability

| Requirement | Condition for Applicability |
|-------------|----------------------------|
| NFR-COM-005 | Applies when IMS data is stored or processed outside the data subject's jurisdiction |
| NFR-COM-009 (SOX) | Applies if organization is subject to Sarbanes-Oxley or equivalent public company reporting obligations |
| NFR-COM-018 | Applies when organization handles lot-controlled, expiry-dated, or recall-sensitive product categories |
| NFR-COM-015 (B2C) | Heightened scrutiny when ATP data is displayed directly to B2C consumers |

Legal must confirm applicable regulations for all operating jurisdictions before go-live.

---

## Assumptions and Validation Notes

| ID | Assumption | Validation Action |
|----|------------|-------------------|
| CA-01 | Organization operates in jurisdictions subject to GDPR or equivalent privacy law | Legal confirms applicable privacy regulations |
| CA-02 | 7-year retention satisfies all operating jurisdictions; longer period applied where required | Legal and CFO sign retention schedule |
| CA-03 | Organization is not a regulated food/pharma operator unless NFR-COM-018 triggered | Product category review with Inventory Controller |
| CA-04 | SOX applicability determined before control design finalization | CFO and Internal Auditor confirm |
| CA-05 | Compliance requirements reviewed annually and at each new location or jurisdiction rollout | Steering committee annual compliance review |

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-07-03 | Security Engineer | Initial compliance requirements definition |

---

*This document defines business-level compliance requirements only. Certification procedures, regulatory filing obligations, and compliance technology implementation are out of scope and will be addressed in separate governance and legal artifacts.*
