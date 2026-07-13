# Business Rule Catalog — Pre-Use Case Review
## Inventory Management System

---

## Document Information

| Attribute | Detail |
|-----------|--------|
| **Document ID** | SRS-REV-001 |
| **Document Title** | Business Rule Catalog Review — Pre-Use Case Readiness Assessment |
| **Version** | 1.0 |
| **Status** | Draft |
| **Document Owner** | Senior Domain Consultant |
| **Review Date** | July 5, 2026 |
| **Artifacts Reviewed** | SRS-BR-001, SRS-VR-001, SRS-BC-001, SRS-EX-001, SRS-DT-001, SRS-BRDEP-001 |
| **Reference Baseline** | BRD-IMS-001, FR-001–FR-090, BP-01–BP-32 |

### Purpose

This document provides a **senior domain review** of the complete rule catalog before the project proceeds to **Use Case** authoring. It assesses consistency, completeness, and traceability across business rules, validation rules, constraints, exception scenarios, and decision tables. Findings are classified as **missing**, **duplicate**, **conflicting**, **ambiguous**, or **unlinked** — with actionable recommendations.

### Review Verdict Summary

| Dimension | Status | Severity |
|-----------|--------|----------|
| **Catalog completeness** | Good foundation; 8–10 policy gaps | Medium |
| **Cross-artifact consistency** | Strong on core flows; weak on finance, rotation, trade | Medium |
| **Traceability to FRs** | 25 BRs well-linked; 7 BRs lack VR enforcement | High |
| **Conflict resolution** | 7 known tensions documented; 3 unresolved for use cases | High |
| **Ambiguity** | 12 rules need parameterization before use cases | High |
| **Readiness for Use Cases** | **Conditional go** — resolve Priority 1 items first | — |

---

## 1. Catalog Inventory Summary

| Artifact | Document ID | Count | Primary Role |
|----------|-------------|-------|--------------|
| Business Rules | SRS-BR-001 | 32 (BR-001–BR-032) | Organizational policy — *what the business must do* |
| Validation Rules | SRS-VR-001 | 200 (VR-001–VR-200) | Transaction gates — *what must be valid to proceed* |
| Business Constraints | SRS-BC-001 | 38 (BC, TC, LC, OC, ORC, TEC) | Initiative boundaries — *what the project/operation cannot change* |
| Exception Scenarios | SRS-EX-001 | 43 (EX-001–EX-043) | Exception behavior — *what to do when happy path fails* |
| Decision Tables | SRS-DT-001 | 32 (DT-01–DT-32) | Branching logic — *conditions → actions → outcomes* |
| Rule Dependencies | SRS-BRDEP-001 | 58 dependencies, 7 conflicts, 8 overlaps | Relationship analysis |

### Coverage Heat Map

| Domain | BR | VR | EX | DT | Assessment |
|--------|----|----|----|-----|------------|
| Availability & Fulfillment | Strong | Strong | Strong | Strong | Ready with ambiguity fixes |
| Inbound & Receiving | Strong | Strong | Strong | Strong | Ready |
| Replenishment & Network | Strong | Strong | Strong | Strong | Timing conflict to resolve |
| Inventory Control | Strong | Strong | Strong | Medium | SOD overlap to clarify |
| Returns | Adequate | Adequate | Adequate | Medium | Ready |
| Product Rotation & Traceability | Defined | **Weak** | Partial | Low | **Not ready** — VR gap |
| Financial / Trade (PO match, bonded, consignment) | Defined | **Absent** | Partial | Low | **Not ready** |
| Reporting & Notifications | None (by design) | Present | Partial | Low | OK for Phase 2/3 use cases |
| Governance & Audit | Partial | Strong | Adequate | Medium | BR gap on immutability |

---

## 2. Missing Rules

Rules implied by functional requirements, exception scenarios, or operational reality but **not expressed as business rules** in SRS-BR-001.

### 2.1 Recommended New Business Rules (Priority 1 — Before Use Cases)

| Proposed ID | Proposed Rule Name | Gap Source | Why Missing Matters |
|-------------|-------------------|------------|---------------------|
| **BR-033** | Authorized Product Substitution | FR-050, EX-023, BP-20 | Substitution is handled in exceptions and FRs but has no governing policy — who may substitute, customer consent, ATP impact, and lot compatibility are undefined. |
| **BR-034** | Scarce Stock Allocation Priority | EX-020, EX-042, EX-036 | When ATP < total demand, no rule defines allocation order (customer tier, order date, channel, SKU class). Leads to inconsistent fulfillment decisions. |
| **BR-035** | Receipt Quantity Tolerance Policy | FR-020, BR-008 (implicit) | BR-008 references "defined tolerance" for three-way match; no standalone rule defines over/short tolerance %, approver, or auto-accept limits. |
| **BR-036** | Purchase Commitment Approval Authority | BP-05, DT-05, VR-030 area | PO placement has workflow decisions but no business rule for financial approval thresholds by role — only VR for data completeness. |
| **BR-037** | Reservation Release and Expiry | FR-043, EX-021 | BR-002 requires reservation at confirmation; no rule defines when reservations must be released (cancel, timeout, payment failure). |
| **BR-038** | Backorder Hold Duration | BR-028 (partial), DT-19 R4 | Customer acknowledgment is required; maximum hold period and auto-cancel policy are not ruled. |
| **BR-039** | In-Transit Inventory Accountability | FR-061, BP-25 | Stock in transit between locations has no ownership/status rule — when source deducts, when destination may commit, loss accountability. |

### 2.2 Recommended New Business Rules (Priority 2 — During Use Case Elaboration)

| Proposed ID | Proposed Rule Name | Gap Source | Why Missing Matters |
|-------------|-------------------|------------|---------------------|
| **BR-040** | Multi-Location Split Fulfillment | FR-048, BP-16/17 | No policy for splitting one order across locations — shipping cost, customer communication, partial reservation rules. |
| **BR-041** | Channel Inventory Allocation | EX-036, BR-029 (related) | B2B vs B2C vs marketplace sharing of ATP is in exceptions but not ruled; BR-029 covers promo only. |
| **BR-042** | Audit Record Immutability | FR-086, VR-189, LC-02 | Strong VR and legal constraint; no business rule stating records cannot be altered post-creation. |
| **BR-043** | Opening Balance Certification | FR-010, EX-004, VR-025 | Scattered across VR/EX; no consolidated business rule that unverified opening balance blocks all transactions. |
| **BR-044** | Obsolete Stock Disposition Timeline | FR-040, EX-043 | Write-off rule exists (BR-023); no rule requiring disposition within defined period after discontinuation. |

### 2.3 Missing Validation Rules (BR Without VR Enforcement)

Seven business rules have **no validation rule reference** in SRS-VR-001. Use cases and acceptance criteria cannot verify these policies without new VRs.

| Business Rule | Policy Summary | Recommended VR Focus | Priority |
|---------------|----------------|---------------------|----------|
| **BR-008** | Three-way match before payment | Block payment authorization when PO, receipt, and invoice mismatch beyond tolerance | P1 |
| **BR-014** | FEFO for shelf-life products | Block pick/shipment of later-expiry lot when earlier lot has ATP | P1 |
| **BR-015** | FIFO for standard goods | Block pick of newer receipt when older receipt has ATP (or warn per policy) | P1 |
| **BR-016** | MRSL at receipt | Reject or quarantine receipt when remaining shelf life below product MRSL | P1 |
| **BR-017** | Lot/batch capture for traceable products | Block receive, transfer, ship without lot attribution on traceable SKUs | P1 |
| **BR-030** | Bonded inventory clearance | Block ATP increase and sellable put-away until customs clearance confirmed | P2 |
| **BR-031** | Consignment ownership at consumption | Block owned valuation and owned ATP treatment until consumption event | P2 |

**Count:** 7 BR gaps → approximately **15–20 new validation rules** recommended.

### 2.4 Missing Exception Scenarios

| Gap | Related BR/FR | Recommended Exception |
|-----|---------------|----------------------|
| Bonded goods released without clearance | BR-030 | EX-044: Customs hold violation or clearance delay |
| Consignment consumption not recorded | BR-031, FR-075 | EX-045: Consignment stock used without ownership transfer |
| FEFO violation discovered at pick | BR-014 | EX-046: Wrong expiry lot selected during pick |
| MRSL failure at receiving | BR-016 | EX-047: Shelf-life below minimum at receipt |
| Three-way match failure at invoice | BR-008 | EX-048: Invoice mismatch blocks payment |
| Substitution rejected by customer | BR-033 (proposed) | EX-049: Customer declines substitute — cancel or wait |

### 2.5 Missing Decision Table Coverage

| Process | Gap | Recommendation |
|---------|-----|----------------|
| BP-05 PO Placement | BR-036 (proposed) approval authority not in DT-05 | Extend DT-05 with approval matrix rows |
| BP-18 Pick/Pack/Ship | BR-014/BR-015 rotation not in DT-18 | Add rotation verification decision rows |
| BP-30 Financial Reconciliation | BR-008 three-way match not tabulated | Add DT-33 for payment authorization |
| BP-23 Inbound Tracking | No BR for expedite vs wait beyond EX-011 | Link EX-011 to DT-23 explicitly |

### 2.6 Missing Constraint-to-Rule Links

Constraints reference business impact but rarely cite governing rules. Critical links to add:

| Constraint | Should Reference | Gap |
|------------|------------------|-----|
| LC-05 Consumer Protection | BR-001, BR-028 | Not cross-linked in SRS-BC-001 |
| OC-07 Cycle Count Without Disruption | BR-024 | Tension not documented in constraints doc |
| LC-04 Supplier Contracts | BR-006, BR-007 | Partial reference only |
| TEC-05 Manual integration | BR-001 ATP freshness | ATP staleness not ruled |

---

## 3. Duplicate Rules

Duplication across artifacts is not always erroneous — BR states policy, VR enforces it. Duplicates flagged below are **redundant, overlapping, or merge candidates**.

### 3.1 Cross-Artifact Duplicates (Intentional — Keep, But Cross-Link)

| Policy Intent | Business Rule | Validation Rule(s) | Recommendation |
|---------------|---------------|-------------------|----------------|
| ATP-only commitment | BR-001 | VR-055, VR-090 | Keep both; add explicit BR→VR traceability table in SRS-BR-001 |
| Discontinued no reorder | BR-027 | VR-004, VR-120 | Keep both; reference single policy ID in use cases |
| Safety stock protection | BR-010 | VR-094, VR-124 | Keep both; clarify reservation vs transfer scope in BR-010 |
| SOD on adjustments | BR-019, BR-021 | VR-075, VR-082, VR-083 | See §3.2 — scope overlap |

### 3.2 True Overlaps Requiring Consolidation or Clarification

| ID | Duplicate / Overlap | Artifacts | Issue | Recommendation |
|----|---------------------|-----------|-------|----------------|
| **DUP-001** | Independent approval for count vs material adjustment | BR-019 vs BR-021 | Same SOD principle; different scope boundaries unclear | Add scope matrix: BR-019 = count-originated always; BR-021 = value/quantity threshold for all adjustments |
| **DUP-002** | Counter cannot approve own work | VR-075 vs VR-083 | VR-075: count adjustment; VR-083: general SOD — nearly identical user messages | Consolidate to one VR with transaction-type parameter; reference both BR-019 and BR-021 |
| **DUP-003** | Safety stock block | VR-094 vs VR-124 | VR-094: reservation; VR-124: reservation and transfer — duplicate logic | Single VR with transaction-type list; one use case with variants |
| **DUP-004** | Non-sellable exclusion from ATP | BR-013 vs BR-030 | Both exclude stock from ATP for different hold reasons | Keep separate BRs; single ATP exclusion concept in use cases with hold-reason subtypes |
| **DUP-005** | Return authorization | BR-025 | VR-045, VR-142, VR-144 | Three VRs for same policy — acceptable if lifecycle staged; use cases should reference BR-025 once |
| **DUP-006** | Investigate before adjust | BR-022 | VR-074, VR-076 | VR-074 = routing; VR-076 = documentation — complementary not duplicate; clarify in catalog |
| **DUP-007** | EX-017 vs EX-020 | Exception catalog | Both cover insufficient ATP / concurrent demand | Merge narrative in use cases; keep both EX IDs for different triggers |

### 3.3 Decision Table / Exception Redundancy

| Decision Table | Overlapping Exceptions | Recommendation |
|----------------|------------------------|----------------|
| DT-07 (Goods Receipt) | EX-005 – EX-009 | Use DT for happy-path branching; EX for actor/escalation detail — cross-reference in use cases |
| DT-19 (Backorder) | EX-022 | Single use case with DT-19 as main flow, EX-022 as exception extension |
| DT-21 (Low Stock) | EX-024, EX-025 | Consolidate into one replenishment use case family |

---

## 4. Conflicting Rules

Conflicts documented in SRS-BRDEP-001 plus additional cross-artifact conflicts.

### 4.1 Business Rule Conflicts (From SRS-BRDEP-001)

| Conflict ID | Rules | Type | Business Impact | Resolution Status |
|-------------|-------|------|-----------------|-------------------|
| CF-001 | BR-024 vs BR-002, BR-003 | Operational tension | Freeze stops shipping; reservations expect fulfillment | **Unresolved** — needs freeze scheduling policy |
| CF-002 | BR-024 vs BR-004, BR-005 | Operational tension | Inbound blocked during count; dock backlog | **Unresolved** — needs inbound coordination policy |
| CF-003 | BR-009 vs BR-011 | Priority ambiguity | Same-day reorder vs network check duration | **Unresolved** — needs SLA by ABC class |
| CF-004 | BR-006 vs partial receipt | Priority ambiguity | Document-all vs accept good units now | Partially resolved in DT-08; **needs BR clarification** |
| CF-005 | BR-029 vs BR-001, BR-002 | Operational tension | Promo ring-fence vs general ATP | **Unresolved** — needs separate ATP pool rule |
| CF-006 | BR-010 vs BR-002 | Priority ambiguity | Safety stock vs urgent reservation | **Unresolved** — needs exception workflow |
| CF-007 | BR-007 vs BR-008 | Exception gap | Ad-hoc receipt vs three-way match | **Unresolved** — needs ad-hoc payment match rules |

### 4.2 Constraint vs Business Rule Conflicts (New Findings)

| Conflict ID | Constraint / Rule | Type | Business Impact | Recommendation |
|-------------|---------------------|------|-----------------|----------------|
| **CF-008** | **OC-07** (no shutdown for cycle count) vs **BR-024** (freeze during full count) | Operational tension | OC-07 permits rolling counts without disruption; BR-024 freezes all movements at location | Define BR-024 as applying to **full wall-to-wall count only**; amend BR-024 statement to distinguish from cycle count |
| **CF-009** | **OC-01** (no shutdown at go-live) vs **FR-010/VR-025** (opening balance approval before activation) | Timing tension | Location cannot transact until opening balance approved; operations must continue | Use read-only or staging mode at go-live; document in use case |
| **CF-010** | **OC-02** (maintain service levels) vs **BR-018** (blind count slows counting) | Performance tension | Blind count may reduce count speed during peak | Schedule Class A counts in low windows per BR-032 |
| **CF-011** | **BC-02** (no new headcount) vs **BR-032** (higher count frequency for Class A) | Capacity tension | More counts without more staff | Prioritize Class A SKUs; accept lower Class C frequency — document trade-off |
| **CF-012** | **LC-04** (supplier contract compatibility) vs **BR-006** (document before acceptance) | Process tension | Suppliers may refuse new documentation fields | Map BR-006 minimum fields to existing delivery note format |

### 4.3 Validation vs Business Rule Conflicts

| Conflict ID | Rules | Issue | Recommendation |
|-------------|-------|-------|----------------|
| **CF-013** | VR-019 vs BR-009 | VR allows inverted threshold "unless policy explicitly allows" — no BR defines when inversion is permitted | Add BR or governance policy for inverted thresholds; default remains VR-019 block |
| **CF-014** | VR-055 (ATP formula) vs BR-031 | Consignment physically present — ATP formula may treat as available if not excluded | Add VR for consignment exclusion from owned ATP; link BR-031 |
| **CF-015** | VR-071 (freeze enforcement) vs OC-07 | VR enforces BR-024 freeze; OC-07 says cycle counting without disruption — scope confusion | VR-071 should reference full count only, not cycle count |

---

## 5. Ambiguous Rules

Rules that are **policy-complete in intent** but **insufficiently parameterized** for use case and acceptance criteria authoring.

### 5.1 High Ambiguity (Must Resolve Before Use Cases)

| Rule / VR | Ambiguity | Questions to Answer | Impact if Unresolved |
|-----------|-----------|-------------------|----------------------|
| **BR-007** | "Explicitly approved ad-hoc receipt exception" | Who approves? Retroactive PO required? Time limit? | Receiving clerk cannot act on emergency inbound (EX-008) |
| **BR-009** | "Same business day" | Which timezone? What if alert fires at 5 PM? Weekend/holiday? | Replenishment SLA disputes |
| **BR-010** | "Authorized exception" | Approver role? Required replenishment plan fields? Duration? | Safety stock silently eroded |
| **BR-016** | MRSL values | Per product? Per category? Supplier-specific? | Receivers cannot reject near-expiry goods |
| **BR-021** | "Defined financial or quantity threshold" | Numeric values by role? By location? Currency? | Approvers cannot route consistently |
| **BR-023** | "Documented evidence" | Photo? Supplier letter? Minimum fields? | Write-off audit failures |
| **BR-028** | "Explicit customer acknowledgment" | Verbal OK? Email? System click? Record retention? | Backorder disputes |
| **BR-029** | "Commercial leadership approval" | Role name? Delegation? Campaign end date? | Promo stock consumed incorrectly |
| **BR-031** | "Consumption or sale event" | Which events transfer ownership? Consignment vs sale timing? | Finance misvaluation |
| **BR-014 / BR-015** | Product classification | Who assigns FEFO vs FIFO? Mixed SKU handling? | Wrong rotation rule applied |
| **VR-019** | Inverted threshold exception | What policy allows min > reorder? | Threshold validation inconsistent |
| **EX-042** | "Apply allocation rules" | No BR-034 exists | Flash demand handled ad hoc |

### 5.2 Medium Ambiguity (Resolve During Use Case Workshops)

| Rule / VR | Ambiguity | Recommendation |
|-----------|-----------|----------------|
| BR-008 | Tolerance % for three-way match | Finance workshop — propose BR-035 |
| BR-032 | "Higher frequency" for Class A | Quantify: A = monthly, B = quarterly, C = semi-annual |
| VR-068 | Class A frequency vs Class C | Align with BR-032 quantification |
| EX-041 | Exception normalization risk | Define quarterly exception review in BP-32 use case |
| DT-05 R3 | "Exceeds buyer authority" | Link to proposed BR-036 with numeric limits |
| FR-050 | Substitution without BR | Create BR-033 before use case |

### 5.3 Ambiguity Resolution Template (For Workshops)

For each high-ambiguity rule, capture in a **Policy Parameter Sheet** before use cases:

```
Rule ID:
Parameter:
Allowed Values:
Default:
Approver (if exception):
Linked FR/VR/EX:
```

---

## 6. Rules Not Linked to Requirements

### 6.1 Business Rules Without Functional Requirement Links

SRS-BR-001 lists related FRs per rule. The following **business rules have thin or no FR mapping** in the catalog (implementation may exist but traceability is weak):

| Business Rule | FRs Listed in SRS-BR-001 | Gap | Recommended FR Link |
|---------------|--------------------------|-----|---------------------|
| BR-008 | FR-013, FR-015, FR-016, FR-089 | No FR dedicated to payment match | **FR-089** primary; consider new FR-091 Payment Match in Phase 3 |
| BR-014 | FR-044, FR-029 | No rotation-specific FR | **FR-044** (extend) or new FR for rotation |
| BR-015 | FR-044, FR-029 | Same as BR-014 | Same |
| BR-016 | FR-015, FR-016 | MRSL not explicit in FR text | **FR-015** acceptance criteria |
| BR-017 | FR-029, FR-015 | Lot capture scattered | **FR-029** movement history |
| BR-030 | FR-038, FR-018 | Bonded status not in FR-038 text | **FR-038** hold types |
| BR-031 | FR-075, FR-089 | Consignment not explicit | **FR-075**, **FR-089** |

### 6.2 Functional Requirements Without Business Rule Links

**52 of 90 FRs** are not referenced in any SRS-BR-001 "Related Functional Requirements" field. The following **operational FRs** should have business rules but do not:

| FR | Description | Severity | Action |
|----|-------------|----------|--------|
| FR-020 | Receipt quantity tolerance evaluation | High | Add BR-035; VR for BR-008 |
| FR-048 | Multi-location split fulfillment | High | Add BR-040 |
| FR-050 | Authorized product substitution | High | Add BR-033 |
| FR-061 | Monitor in-transit inventory | High | Add BR-039 |
| FR-059 | Approve/reject transfer requests | Medium | Extend BR-012 with approval authority |
| FR-021 | Cancel/amend open POs | Medium | Add procurement cancellation rule |
| FR-062 | Network rebalancing recommendations | Medium | Link to BR-011 (informational) |

**Reporting, notification, and admin FRs** (FR-068–074, FR-076–079, FR-081–083, FR-085–088) appropriately have no business rule — they are system capabilities supporting ruled processes. **Do not create BRs for every FR.**

### 6.3 Validation Rules Without Business Rule Parent

Approximately **153 of 200 VRs** do not cite a BR-xxx in the Business Reason field. This is acceptable for data-quality VRs (VR-001, VR-011, etc.). Priority gaps are the **7 BRs with zero VR coverage** (§2.3).

### 6.4 Exception Scenarios Without Decision Table Path

| Exception | Missing DT Link | Process |
|-----------|-----------------|---------|
| EX-008 | Receipt without PO | BP-07 — in DT-07 R2; **link explicitly** |
| EX-026 | Safety stock override | BP-17/21 — **add DT row** |
| EX-036 | Channel conflict | No DT | **Add DT-34 or extend DT-31** |
| EX-037 | Finance mismatch | DT-30 exists | Cross-link EX-037 ↔ DT-30 |
| EX-040 | Product recall | No DT | **Add DT-35 quarantine disposition** |
| EX-041 | Authorized exception | No DT | **Add DT-36 exception governance** |

### 6.5 Traceability Matrix Gaps

| From | To | Status |
|------|-----|--------|
| BR → VR | 25/32 BRs have ≥1 VR | **7 gaps** (§2.3) |
| BR → EX | 28/32 BRs referenced in EX | BR-014, BR-015, BR-030, BR-031 weak |
| BR → DT | 6/32 BRs explicitly cited in DT | Low explicit citation — acceptable if DT outcomes imply BR |
| BR → FR | 38 FR citations across 32 BRs | 52 FRs unreferenced by BR |
| Constraint → BR | 2 explicit BR cites in BC-001 | **Weak** — add constraint impact matrix |

---

## 7. Artifact Consistency Assessment

### 7.1 Strengths

1. **Core fulfillment chain** (BR-001 → BR-002 → BR-003) is well aligned across BR, VR, EX, and DT.
2. **Inbound verification chain** (BR-004 → BR-006 → BR-007) is consistent and exception-rich.
3. **Count governance** (BR-018 → BR-022 → BR-019/BR-021) is reinforced across three artifact types.
4. **200 validation rules** provide strong use-case acceptance criteria source material.
5. **43 exception scenarios** cover realistic operational failures with accountable actors.
6. **SRS-BRDEP-001** proactively documents rule interactions and conflicts.

### 7.2 Weaknesses

1. **Finance and trade rules** (BR-008, BR-030, BR-031) lack validation enforcement.
2. **Rotation and traceability** (BR-014–BR-017) are policy without operational VR gates.
3. **Constraint vs rule tensions** (OC-07 vs BR-024) not harmonized in one document.
4. **Allocation and substitution** appear in FR/EX but not in business rules.
5. **Explicit BR ↔ VR traceability** missing from SRS-BR-001 (only FR links today).
6. **Reporting category** in SRS-BR-001 is empty — correct for inventory policy, but audit oversight rules (BR-042 proposed) would fit BP-32.

---

## 8. Recommendations Before Use Cases

### 8.1 Priority 1 — Blocking (Complete Before Use Case Authoring Starts)

| # | Action | Owner | Deliverable |
|---|--------|-------|-------------|
| 1 | **Resolve CF-001, CF-005, CF-006** — publish precedence policy for freeze vs fulfillment, promo ring-fence vs ATP, safety stock exceptions | Operations Director + Product Owner | Policy addendum to SRS-BR-001 |
| 2 | **Parameterize high-ambiguity rules** (§5.1) — at minimum BR-007, BR-009, BR-010, BR-021, BR-028 | Inventory Controller + Finance | Policy Parameter Sheet |
| 3 | **Add BR-033, BR-034, BR-035, BR-037, BR-039** | Business Analyst | SRS-BR-001 v1.1 |
| 4 | **Add VRs for BR-008, BR-014, BR-015, BR-016, BR-017** | Business Analyst | SRS-VR-001 v1.1 (~15–20 rules) |
| 5 | **Clarify BR-024 scope** — full count only; amend CF-008 and VR-071 | Domain Consultant | BR-024 revision + OC-07 cross-link |
| 6 | **Add BR→VR traceability matrix** to SRS-BR-001 | Business Analyst | Appendix table |

### 8.2 Priority 2 — During Use Case Authoring (First Sprint)

| # | Action | Owner | Deliverable |
|---|--------|-------|-------------|
| 7 | Consolidate DUP-002, DUP-003 VR overlaps | BA + QA | SRS-VR-001 cleanup |
| 8 | Cross-link EX ↔ DT for top 10 exception paths | BA | SRS-EX-001 / SRS-DT-001 update |
| 9 | Add BR-040, BR-041, BR-042 and matching VRs | BA | Catalog v1.1 |
| 10 | Add EX-044 – EX-049 for finance/trade/rotation gaps | Domain Consultant | SRS-EX-001 v1.1 |
| 11 | Add constraint-to-rule impact matrix in SRS-BC-001 | BA | BC appendix |
| 12 | Harmonize BR-032 and VR-068 with quantified count frequencies | Operations | Single frequency table |

### 8.3 Priority 3 — Before UAT / Acceptance Criteria

| # | Action | Owner |
|---|--------|-------|
| 13 | Full RTM refresh: BR ↔ FR ↔ VR ↔ EX ↔ DT ↔ BP | BA |
| 14 | Resolve CF-007 ad-hoc receipt payment path with Finance | CFO liaison |
| 15 | Add DT-33 (payment match), DT-35 (recall), DT-36 (governed exception) | Domain Consultant |
| 16 | Use case catalog aligned to BP (32 primary + exception variants) | BA |

### 8.4 Use Case Authoring Guidance

When writing use cases, apply this **rule invocation order**:

```text
1. Business Constraint (BC/OC/LC) — can the process run at all?
2. Business Rule (BR) — what policy applies?
3. Decision Table (DT) — which branch?
4. Validation Rule (VR) — what must pass at each step?
5. Exception Scenario (EX) — what if validation or decision fails?
```

**Use case naming convention (recommended):**

| Pattern | Example |
|---------|---------|
| `UC-BP-xx` | UC-BP-07 Confirm Goods Receipt |
| `UC-EX-xx` | UC-EX-005 Resolve Supplier Short-Shipment |
| Primary flow cites | BR-xxx, VR-xxx, DT-xx |
| Alternate flow cites | EX-xxx, CF-xxx resolution |

**Do not** create use cases for:

- Pure reporting FRs without ruled behavior (FR-068–074) — defer to Phase 2/3
- Duplicate VR enforcement paths — one use case per business capability

---

## 9. Pre-Use Case Readiness Checklist

| # | Criterion | Status |
|---|-----------|--------|
| 1 | All 32 BRs have clear, parameterized statements for MVP scope | ☐ Partial — 12 ambiguous |
| 2 | Every MVP BR has ≥1 validation rule | ☐ Fail — 7 BRs missing |
| 3 | Top 20 exceptions have decision table or use case path | ☐ Partial |
| 4 | Known conflicts have documented resolution | ☐ Partial — 7 open |
| 5 | Constraint vs rule tensions documented | ☐ Done in this review |
| 6 | FR-048, FR-050, FR-020 have governing business rules | ☐ Fail — propose BR-033–035, 040 |
| 7 | BR→VR traceability matrix published | ☐ Not started |
| 8 | Policy Parameter Sheet for P1 ambiguities | ☐ Not started |
| 9 | Stakeholder sign-off on conflict resolutions CF-001, CF-005, CF-006 | ☐ Not started |
| 10 | Use case authoring standards agreed | ☐ Recommended in §8.4 |

**Overall readiness:** ☐ **Not ready for bulk use case authoring** — complete Priority 1 items (estimated 1–2 workshops + catalog update).

**Conditional start:** Use cases for **BP-07, BP-16, BP-17, BP-18, BP-21** may begin now — these domains are catalog-mature.

**Defer use cases for:** BP-30 (financial match), bonded/consignment receiving, FEFO/FIFO pick — until §2.3 and §8.1 items complete.

---

## 10. Issue Register Summary

| Category | Count | IDs |
|----------|-------|-----|
| Missing business rules (proposed) | 12 | BR-033 – BR-044 |
| Missing validation rules (est.) | 15–20 | For BR-008, BR-014–017, BR-030–031 |
| Missing exceptions (proposed) | 6 | EX-044 – EX-049 |
| Duplicates / overlaps | 7 | DUP-001 – DUP-007 |
| Conflicts | 15 | CF-001 – CF-015 |
| Ambiguous rules | 12 high + 6 medium | §5.1, §5.2 |
| Unlinked FRs (operational) | 7 high priority | §6.2 |
| BRs without VR | 7 | §2.3 |

---

## Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Senior Domain Consultant | | | |
| Product Owner | | | |
| Senior Business Analyst | | | |
| Operations Director | | | |
| Inventory Controller | | | |

---

*End of Business Rule Catalog Review*

*Document ID: SRS-REV-001 | Version 1.0 | July 5, 2026*
