# Business Rule Dependency Analysis
## Inventory Management System

---

## Document Information

| Attribute | Detail |
|-----------|--------|
| **Document ID** | SRS-BRDEP-001 |
| **Document Title** | Business Rule Dependencies — Inventory Management System |
| **Version** | 1.0 |
| **Status** | Draft |
| **Document Owner** | Senior Domain Expert |
| **Source Documents** | SRS-BR-001, BRD-IMS-001 (Section 13), Business Workflows (WF-01–WF-32), SRS-DT-001 |
| **Date** | July 5, 2026 |
| **Scope** | Business rule relationships only — not system implementation, validation rules, or technical constraints |

### Purpose

This document analyzes **dependencies among the 32 business rules** (BR-001–BR-032). For each dependency it identifies the **parent rule**, **dependent rule**, **dependency type**, and **business impact**. It also catalogs **conflicting** and **overlapping** rules that require explicit policy resolution.

### Dependency Type Definitions

| Type | Meaning |
|------|---------|
| **Prerequisite** | The parent rule must be satisfied or in force before the dependent rule can be applied meaningfully. |
| **Sequential** | The parent rule governs an earlier step in the same business process; the dependent rule applies only after the parent step completes. |
| **Compositional** | The dependent rule builds on or is calculated from conditions established by the parent rule. |
| **Constraint** | The parent rule limits, bounds, or restricts how the dependent rule may be executed. |
| **Exception** | The parent rule defines an authorized exception path to the dependent rule under defined conditions. |
| **Reinforcement** | Rules apply to the same control objective from different angles; both must hold simultaneously. |

### Conflict / Overlap Classification

| Classification | Meaning |
|----------------|---------|
| **Scope Overlap** | Two rules govern the same business object or decision point with partially duplicate intent. |
| **Operational Tension** | Both rules are valid but compete for the same resource, timing, or stock pool. |
| **Priority Ambiguity** | Precedence between rules is not explicit; actors may apply them in conflicting order. |
| **Mutual Exclusion** | Rules require mutually exclusive actions in the same context without a defined selector. |

---

## 1. Dependency Catalog

Dependencies are grouped by business domain. Rule pairs already noted in SRS-BR-001 as interdependent combinations are included and extended.

---

### 1.1 Availability, Commitment & Fulfillment

| ID | Parent Rule | Dependent Rule | Dependency Type | Business Impact |
|----|-------------|----------------|-----------------|-----------------|
| DEP-001 | **BR-005** Put-Away Before Availability | **BR-001** ATP-Only Customer Commitment | Compositional | ATP cannot include received-but-not-put-away stock. Violating BR-005 inflates ATP and causes BR-001 overselling — customers confirmed against stock pickers cannot locate. |
| DEP-002 | **BR-013** Quarantine Exclusion | **BR-001** ATP-Only Customer Commitment | Compositional | Quarantined, hold, and recall stock must be excluded from ATP. If BR-013 is ignored, BR-001 permits commitment to non-sellable inventory — regulatory, quality, and customer risk. |
| DEP-003 | **BR-030** Bonded Inventory Clearance | **BR-001** ATP-Only Customer Commitment | Compositional | Bonded stock is non-sellable until customs release. Same ATP exclusion logic as BR-013; failure blocks legal domestic sale while appearing available. |
| DEP-004 | **BR-001** ATP-Only Customer Commitment | **BR-002** Reservation at Order Confirmation | Compositional | BR-001 defines what quantity is promiseable; BR-002 locks that quantity at confirmation. Without BR-001's ATP definition, reservations lack a consistent baseline and double-allocation risk returns. |
| DEP-005 | **BR-002** Reservation at Order Confirmation | **BR-001** ATP-Only Customer Commitment | Compositional | Each reservation reduces ATP. BR-002 is the mechanism that keeps BR-001 accurate as orders confirm — circular but mutually defining: ATP = on-hand minus reservations and non-sellable holds. |
| DEP-006 | **BR-001** ATP-Only Customer Commitment | **BR-028** Backorder Customer Acknowledgment | Sequential | When ATP is insufficient at confirmation, BR-028 governs the customer agreement path before backorder is recorded. BR-001 prevents silent over-commitment; BR-028 governs explicit under-commitment. |
| DEP-007 | **BR-002** Reservation at Order Confirmation | **BR-003** Verified Pick Before Shipment | Sequential | Stock must be reserved before pick execution. BR-003 deducts inventory only after verified pick; BR-002 ensures the picked quantity was already committed to the correct order. |
| DEP-008 | **BR-002** Reservation at Order Confirmation | **BR-028** Backorder Customer Acknowledgment | Sequential | Partial reservation (available portion) pairs with BR-028 for the unreserved remainder. Without sequencing, partial ship may occur without customer agreement on the backorder portion. |
| DEP-009 | **BR-010** Safety Stock Protection | **BR-002** Reservation at Order Confirmation | Constraint | Reservations must not consume safety stock without authorized exception and replenishment plan. Violation depletes buffer protecting against demand/supply uncertainty — next disruption causes stockout despite apparent policy compliance. |
| DEP-010 | **BR-029** Promotional Stock Ring-Fencing | **BR-001** ATP-Only Customer Commitment | Constraint | Promotional allocation reduces ATP available to non-promotional demand. BR-029 further restricts which orders may consume ring-fenced stock beyond ATP arithmetic alone. |
| DEP-011 | **BR-029** Promotional Stock Ring-Fencing | **BR-002** Reservation at Order Confirmation | Constraint | Non-promotional orders must not reserve ring-fenced promotional stock without commercial leadership approval. Prevents campaign stock erosion through standard reservation. |
| DEP-012 | **BR-014** FEFO Rotation | **BR-003** Verified Pick Before Shipment | Constraint | Pick verification must confirm correct lot/batch per FEFO priority. Wrong lot picked violates rotation even if quantity matches — expiry write-off and compliance risk. |
| DEP-013 | **BR-015** FIFO Rotation | **BR-003** Verified Pick Before Shipment | Constraint | Same as DEP-012 for non-perishable goods — oldest receipt date must be picked first. |
| DEP-014 | **BR-017** Lot/Batch Capture | **BR-003** Verified Pick Before Shipment | Prerequisite | Traceable products require lot attribution at pick. BR-003 verification is incomplete without lot capture — recall scope cannot be determined. |
| DEP-015 | **BR-017** Lot/Batch Capture | **BR-014** FEFO Rotation | Reinforcement | FEFO requires expiry-aware lot identity; BR-017 provides the data FEFO depends on for shelf-life products. |

---

### 1.2 Inbound, Receiving & Procurement

| ID | Parent Rule | Dependent Rule | Dependency Type | Business Impact |
|----|-------------|----------------|-----------------|-----------------|
| DEP-016 | **BR-007** PO Required for Supplier Receipt | **BR-004** Verify Before Inventory Acceptance | Prerequisite | Verification is performed against an authorized PO (or approved ad-hoc exception). Without BR-007, verification lacks a reference baseline — unauthorized receipts enter inventory. |
| DEP-017 | **BR-004** Verify Before Inventory Acceptance | **BR-005** Put-Away Before Availability | Sequential | Only verified quantities proceed to put-away. Put-away without verification propagates unconfirmed stock into the availability chain (DEP-001 risk). |
| DEP-018 | **BR-004** Verify Before Inventory Acceptance | **BR-006** Document Receipt Discrepancies | Sequential | Discrepancies are identified during verification and must be documented before acceptance. BR-006 preserves evidence BR-004 discovers — undocumented acceptance waives supplier claims. |
| DEP-019 | **BR-006** Document Receipt Discrepancies | **BR-008** Three-Way Match Before Payment | Prerequisite | Documented receipt quantities are the "received" leg of three-way match. Missing discrepancy documentation causes payment for goods not received or failure to withhold payment for shorts. |
| DEP-020 | **BR-007** PO Required for Supplier Receipt | **BR-008** Three-Way Match Before Payment | Prerequisite | PO is the "ordered" leg of three-way match. Receiving without PO (BR-007 violation) makes BR-008 impossible — payment control breakdown. |
| DEP-021 | **BR-004** Verify Before Inventory Acceptance | **BR-008** Three-Way Match Before Payment | Prerequisite | Verified receipt is the "received" leg. Unverified acceptance corrupts the match and financial records simultaneously. |
| DEP-022 | **BR-016** Minimum Remaining Shelf Life at Receipt | **BR-004** Verify Before Inventory Acceptance | Constraint | MRSL check is part of condition verification for shelf-life products. Failed MRSL triggers reject/disposition before acceptance — prevents BR-014 FEFO from managing already-expired inbound stock. |
| DEP-023 | **BR-016** Minimum Remaining Shelf Life at Receipt | **BR-014** FEFO Rotation | Reinforcement | MRSL at receipt ensures sufficient selling window; FEFO during fulfillment minimizes remaining expiry at customer delivery. Jointly protect shelf-life economics. |
| DEP-024 | **BR-017** Lot/Batch Capture | **BR-004** Verify Before Inventory Acceptance | Constraint | Traceable products require lot capture at receipt as part of verification completeness. |
| DEP-025 | **BR-017** Lot/Batch Capture | **BR-005** Put-Away Before Availability | Sequential | Lot identity must be assigned before or during put-away so subsequent movements maintain traceability. |
| DEP-026 | **BR-030** Bonded Inventory Clearance | **BR-005** Put-Away Before Availability | Constraint | Bonded goods may be physically stored but must not enter sellable availability (DEP-003) until customs clearance — put-away to sellable location prohibited until cleared. |
| DEP-027 | **BR-031** Consignment Ownership at Consumption | **BR-004** Verify Before Inventory Acceptance | Constraint | Consignment receipt is physical verification without ownership transfer. Misclassifying as owned at receipt overstates assets and breaks BR-031 valuation treatment. |
| DEP-028 | **BR-031** Consignment Ownership at Consumption | **BR-008** Three-Way Match Before Payment | Exception | Consignment may not trigger standard PO-to-payment flow until consumption event per supplier agreement — BR-008 applies at ownership transfer, not physical receipt. |

---

### 1.3 Replenishment & Network Balance

| ID | Parent Rule | Dependent Rule | Dependency Type | Business Impact |
|----|-------------|----------------|-----------------|-----------------|
| DEP-029 | **BR-009** Reorder at Reorder Level | **BR-021** Low-Stock Alert Review (via BP-21) | Sequential | Reorder level breach triggers replenishment review. BR-009 mandates same-business-day action; delay guarantees stockout during lead time. |
| DEP-030 | **BR-011** Network Check Before Purchase | **BR-009** Reorder at Reorder Level | Constraint | Before executing replenishment (BR-009), network transfer must be evaluated. Skipping BR-011 causes unnecessary PO spend and worsens network imbalance while BR-009 appears satisfied. |
| DEP-031 | **BR-011** Network Check Before Purchase | **BR-012** Protect Source Location Minimum | Reinforcement | Network check (BR-011) often resolves shortage via transfer; BR-012 ensures the transfer path does not create a new shortage at source. Both required for effective network balance. |
| DEP-032 | **BR-012** Protect Source Location Minimum | **BR-011** Network Check Before Purchase | Constraint | Transfer feasibility assessment must respect source minimum. BR-011 "network has stock" is insufficient if BR-012 blocks the transferable quantity. |
| DEP-033 | **BR-010** Safety Stock Protection | **BR-012** Protect Source Location Minimum | Reinforcement | Both protect minimum stock buffers — BR-010 at policy level, BR-012 at transfer execution. Source minimum typically includes safety stock component. |
| DEP-034 | **BR-027** No Reorder of Discontinued Products | **BR-009** Reorder at Reorder Level | Constraint | BR-009 replenishment action is prohibited for discontinued SKUs. Alert may still fire but response must be runout/clearance, not reorder. |
| DEP-035 | **BR-027** No Reorder of Discontinued Products | **BR-011** Network Check Before Purchase | Constraint | Network transfer may still move discontinued stock for clearance; new procurement is blocked. Prevents obsolete inventory creation. |
| DEP-036 | **BR-032** Class A Priority Monitoring | **BR-009** Reorder at Reorder Level | Constraint | Class A SKUs receive heightened monitoring and faster escalation when approaching reorder level. BR-032 intensifies BR-009 response without changing the threshold logic. |
| DEP-037 | **BR-032** Class A Priority Monitoring | **BR-011** Network Check Before Purchase | Reinforcement | Priority SKUs require expedited network evaluation before external purchase — reduces stockout duration on high-impact items. |

---

### 1.4 Inventory Control & Governance

| ID | Parent Rule | Dependent Rule | Dependency Type | Business Impact |
|----|-------------|----------------|-----------------|-----------------|
| DEP-038 | **BR-018** Blind Cycle Counting | **BR-022** Investigate Before Adjusting | Sequential | Blind count produces unbiased variance detection that triggers investigation. Showing system quantity before count (BR-018 violation) undermines variance integrity and root cause analysis. |
| DEP-039 | **BR-022** Investigate Before Adjusting | **BR-020** Mandatory Adjustment Reason Codes | Sequential | Investigation findings must be captured as reason code at adjustment. BR-020 without BR-022 produces codes without verified root cause — analytically weak. |
| DEP-040 | **BR-022** Investigate Before Adjusting | **BR-021** Independent Approval for Material Adjustments | Sequential | Investigation completes before approval decision. Approving without investigation (BR-022 violation) repeats same variance on next count. |
| DEP-041 | **BR-018** Blind Cycle Counting | **BR-019** Independent Count Approval | Reinforcement | Blind count (BR-018) detects variance; independent approval (BR-019) prevents counter from self-approving biased or erroneous counts. Joint fraud/error control. |
| DEP-042 | **BR-019** Independent Count Approval | **BR-021** Independent Approval for Material Adjustments | Reinforcement | BR-019 applies to count variances; BR-021 applies to material adjustments generally. Same segregation principle — overlapping scope (see OV-003). |
| DEP-043 | **BR-020** Mandatory Adjustment Reason Codes | **BR-023** Documented Write-Off Authorization | Compositional | Write-off is a subset of adjustment requiring reason code (BR-020) plus additional evidence and authorization (BR-023). |
| DEP-044 | **BR-021** Independent Approval for Material Adjustments | **BR-023** Documented Write-Off Authorization | Reinforcement | Material write-offs require both threshold-based independent approval (BR-021) and documented evidence (BR-023). |
| DEP-045 | **BR-024** Physical Inventory Freeze | **BR-018** Blind Cycle Counting | Constraint | Full count freeze suspends movements that would change quantities during count. Cycle counts during operations (BR-018) continue under BP-11 without full freeze. |
| DEP-046 | **BR-024** Physical Inventory Freeze | **BR-003** Verified Pick Before Shipment | Operational Tension | Freeze suspends shipping until count complete. Conflicts with open order fulfillment — requires freeze scheduling and customer communication (see CF-001). |
| DEP-047 | **BR-024** Physical Inventory Freeze | **BR-005** Put-Away Before Availability | Operational Tension | Freeze suspends receiving/put-away at counted location. Inbound goods queue — delays BR-005 and downstream BR-001 ATP increase. |
| DEP-048 | **BR-013** Quarantine Exclusion | **BR-020** Mandatory Adjustment Reason Codes | Sequential | Quarantine disposition (damage, recall) typically results in adjustment with mandatory reason code — links quality hold to governance trail. |
| DEP-049 | **BR-032** Class A Priority Monitoring | **BR-018** Blind Cycle Counting | Constraint | Class A products receive highest count frequency per BR-032. More frequent BR-018 application on priority SKUs. |

---

### 1.5 Returns & Commercial

| ID | Parent Rule | Dependent Rule | Dependency Type | Business Impact |
|----|-------------|----------------|-----------------|-----------------|
| DEP-050 | **BR-025** Return Authorization Required | **BR-026** Inspect Returns Before Restocking | Sequential | Authorization precedes physical receipt; inspection precedes restocking. BR-026 cannot apply to unauthorized returns accepted at dock. |
| DEP-051 | **BR-026** Inspect Returns Before Restocking | **BR-013** Quarantine Exclusion | Sequential | Failed inspection routes to quarantine or write-off — must not enter ATP until disposition. BR-026 is the gate; BR-013 maintains exclusion during hold. |
| DEP-052 | **BR-026** Inspect Returns Before Restocking | **BR-001** ATP-Only Customer Commitment | Compositional | Only inspection-passed returns increase sellable ATP. Restocking without inspection (BR-026 violation) inflates ATP with potentially unsellable goods. |
| DEP-053 | **BR-025** Return Authorization Required | **BR-028** Backorder Customer Acknowledgment | Reinforcement | Both require explicit customer agreement before recording a commercial state (return acceptance / backorder). Shared consent principle across inbound return and outbound delay. |
| DEP-054 | **BR-026** Inspect Returns Before Restocking | **BR-023** Documented Write-Off Authorization | Sequential | Non-resalable returns proceed to write-off path requiring BR-023 authorization and evidence. |

---

### 1.6 Cross-Domain & Financial

| ID | Parent Rule | Dependent Rule | Dependency Type | Business Impact |
|----|-------------|----------------|-----------------|-----------------|
| DEP-055 | **BR-004** Verify Before Inventory Acceptance | **BR-031** Consignment Ownership at Consumption | Compositional | Physical receipt verified under BR-004; ownership treatment governed separately by BR-031. |
| DEP-056 | **BR-008** Three-Way Match Before Payment | **BR-031** Consignment Ownership at Consumption | Sequential | Standard three-way match at invoice; consignment payment triggers at consumption per agreement — different timing, same control intent. |
| DEP-057 | **BR-020** Mandatory Adjustment Reason Codes | **BR-008** Three-Way Match Before Payment | Reinforcement | Inventory adjustments from receipt discrepancies (reason codes) must align with received quantities used in BR-008 — financial and operational records must reconcile. |
| DEP-058 | **BR-001** ATP-Only Customer Commitment | **BR-031** Consignment Ownership at Consumption | Constraint | Consignment stock may be physically present but not owned — must be excluded from owned ATP or separately identified to prevent BR-001 misapplication. |

---

## 2. Dependency Summary Matrix

**Reading guide:** Row = Parent; Column = Dependent. Cell shows dependency type abbreviation.

| Parent ↓ / Dependent → | BR-001 | BR-002 | BR-003 | BR-004 | BR-005 | BR-008 | BR-009 | BR-013 | BR-018 | BR-020 | BR-022 | BR-026 | BR-028 |
|------------------------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| BR-001 | — | Comp | — | — | — | — | — | — | — | — | — | — | Seq |
| BR-002 | Comp | — | Seq | — | — | — | — | — | — | — | — | — | Seq |
| BR-004 | — | — | — | — | Seq | Pre | — | — | — | — | — | — | — |
| BR-005 | Comp | — | — | — | — | — | — | — | — | — | — | — | — |
| BR-007 | — | — | — | Pre | — | Pre | — | — | — | — | — | — | — |
| BR-009 | — | — | — | — | — | — | — | — | — | — | — | — | — |
| BR-010 | — | Con | — | — | — | — | — | — | — | — | — | — | — |
| BR-011 | — | — | — | — | — | — | Con | — | — | — | — | — | — |
| BR-013 | Comp | — | — | — | — | — | — | — | — | Seq | — | Seq | — |
| BR-018 | — | — | — | — | — | — | — | — | — | — | Seq | — | — |
| BR-022 | — | — | — | — | — | — | — | — | — | Seq | — | — | — |
| BR-025 | — | — | — | — | — | — | — | — | — | — | — | Seq | Ref |
| BR-029 | Con | Con | — | — | — | — | — | — | — | — | — | — | — |

*Abbreviations: Comp = Compositional, Seq = Sequential, Pre = Prerequisite, Con = Constraint, Ref = Reinforcement*

---

## 3. Rule Dependency Chains

Critical end-to-end chains where breaking any link undermines the chain:

### Chain A — Sellable Availability (Inbound to Customer)

```text
BR-007 (PO) → BR-004 (Verify) → BR-006 (Document variance)
     → BR-005 (Put-away) → BR-013/BR-030 (Exclude non-sellable)
     → BR-001 (ATP) → BR-002 (Reserve) → BR-003 (Pick/Ship)
```

**Business impact of chain failure:** Any break causes phantom availability, overselling, or shipment of non-compliant stock.

### Chain B — Replenishment Without Waste

```text
BR-009 (Reorder trigger) → BR-011 (Network check) → BR-012 (Source minimum)
     → [Transfer] or [BR-007 PO path]
```

**Business impact:** Skipping network check wastes capital; ignoring source minimum relocates shortage.

### Chain C — Count Integrity

```text
BR-018 (Blind count) → BR-022 (Investigate) → BR-020 (Reason code)
     → BR-019/BR-021 (Independent approval)
```

**Business impact:** Skipping investigation or approval perpetuates errors and fraud exposure.

### Chain D — Financial Control

```text
BR-007 (PO) → BR-004 (Verify) → BR-006 (Document) → BR-008 (Three-way match)
```

**Business impact:** Payment for unordered, unreceived, or mispriced goods; audit failure.

---

## 4. Conflicting Rules

Rules that create genuine tension requiring explicit policy, timing, or precedence resolution.

---

### CF-001 — BR-024 Physical Inventory Freeze vs. BR-002 / BR-003 Fulfillment

| Attribute | Detail |
|-----------|--------|
| **Rules in Conflict** | BR-024 (suspend shipping during full count) vs. BR-002 (honor reservations) vs. BR-003 (ship verified picks) |
| **Conflict Type** | Operational Tension |
| **Nature** | Full count freeze stops outbound movements; confirmed orders with reservations expect fulfillment. |
| **Business Impact** | Customer delivery delays; reservation hold times extend; potential BR-028 backorder triggers if freeze is prolonged. |
| **Recommended Resolution** | Schedule freeze during low-activity window; pre-communicate delays; complete freeze before peak; regional freeze rotation so network can fulfill from alternate locations (BR-011). |

---

### CF-002 — BR-024 Physical Inventory Freeze vs. BR-005 / BR-004 Inbound

| Attribute | Detail |
|-----------|--------|
| **Rules in Conflict** | BR-024 vs. BR-004 / BR-005 |
| **Conflict Type** | Operational Tension |
| **Nature** | Freeze suspends receiving and put-away; supplier deliveries may arrive on schedule regardless. |
| **Business Impact** | Dock congestion; delayed ATP increase; supplier detention charges; inbound backlog after freeze lifts. |
| **Recommended Resolution** | Coordinate inbound schedule with count calendar; stage received goods without put-away to quarantine/staging if policy allows; or reschedule supplier deliveries. |

---

### CF-003 — BR-009 Same-Day Replenishment vs. BR-011 Network Evaluation Time

| Attribute | Detail |
|-----------|--------|
| **Rules in Conflict** | BR-009 (act same business day at reorder level) vs. BR-011 (evaluate network before purchase) |
| **Conflict Type** | Priority Ambiguity |
| **Nature** | Thorough network transfer evaluation may delay PO placement beyond same day; rushing BR-011 risks missing transferable stock. |
| **Business Impact** | Either stockout (BR-009 delayed) or unnecessary PO (BR-011 skipped). |
| **Recommended Resolution** | Define SLA: network check within same business day for Class A (BR-032); standard SKUs may place PO same day while transfer evaluation runs in parallel for next cycle. |

---

### CF-004 — BR-006 Document Before Acceptance vs. Partial Receipt Urgency

| Attribute | Detail |
|-----------|--------|
| **Rules in Conflict** | BR-006 (document all discrepancies before acceptance) vs. operational need to accept good units immediately |
| **Conflict Type** | Priority Ambiguity |
| **Nature** | Damaged/wrong items mixed with good stock — strict interpretation blocks all acceptance until full documentation; operations want good portion in inventory. |
| **Business Impact** | Dock hold delays BR-005/BR-001; or premature full acceptance waives claims (BR-006 violation). |
| **Recommended Resolution** | Accept verified good quantity with documented discrepancy on remainder — partial acceptance path in BP-08/DT-08; never accept undocumented variance. |

---

### CF-005 — BR-029 Promotional Ring-Fence vs. BR-001 / BR-002 General Fulfillment

| Attribute | Detail |
|-----------|--------|
| **Rules in Conflict** | BR-029 (promo stock reserved for campaign) vs. BR-001/BR-002 (ATP and reservation for any confirmed order) |
| **Conflict Type** | Operational Tension |
| **Nature** | ATP may show stock available that BR-029 reserves for promotional channel only. |
| **Business Impact** | Campaign stock consumed by routine orders; promoted channel stockout; or routine orders rejected despite apparent ATP. |
| **Recommended Resolution** | Treat ring-fenced quantity as separate ATP pool or hard reservation at campaign setup; BR-029 overrides general BR-001 for ring-fenced portion. |

---

### CF-006 — BR-010 Safety Stock Exception vs. BR-002 Reservation for Urgent Orders

| Attribute | Detail |
|-----------|--------|
| **Rules in Conflict** | BR-010 (no safety stock consumption without exception) vs. BR-002 (reserve at confirmation for urgent/priority orders) |
| **Conflict Type** | Priority Ambiguity |
| **Nature** | Urgent order confirmation may require stock below safety threshold; BR-010 blocks unless exception documented. |
| **Business Impact** | Order confirmation fails despite physical stock; or safety buffer eroded without replenishment plan. |
| **Recommended Resolution** | Explicit safety-stock exception workflow with approver, replenishment plan, and time limit; priority orders do not auto-bypass BR-010. |

---

### CF-007 — BR-007 PO Required vs. Emergency Ad-Hoc Receipt

| Attribute | Detail |
|-----------|--------|
| **Rules in Conflict** | BR-007 (PO required) vs. emergency receiving without pre-issued PO |
| **Conflict Type** | Exception Gap |
| **Nature** | BR-007 allows "explicitly approved ad-hoc receipt exception" but BR-008 three-way match assumes standard PO flow. |
| **Business Impact** | Emergency stock received but payment blocked; or unauthorized receipt bypasses financial controls. |
| **Recommended Resolution** | Define ad-hoc exception approver, retroactive PO process, and BR-008 alternate match rules for emergency receipts. |

---

## 5. Overlapping Rules

Rules with partially duplicate scope that are complementary when coordinated, or redundant/confusing when not.

---

### OV-001 — BR-013 Quarantine Exclusion vs. BR-030 Bonded Inventory Clearance

| Attribute | Detail |
|-----------|--------|
| **Overlap Type** | Scope Overlap |
| **Shared Scope** | Stock excluded from sellable ATP |
| **Distinction** | BR-013: quality hold, investigation, recall. BR-030: customs/regulatory hold. |
| **Business Impact** | If treated as one status, customs-cleared bonded stock may remain blocked; or quality-hold stock may be released incorrectly. |
| **Recommendation** | Maintain separate hold reasons; both exclude from ATP (DEP-002, DEP-003); disposition paths differ. |

---

### OV-002 — BR-014 FEFO vs. BR-015 FIFO

| Attribute | Detail |
|-----------|--------|
| **Overlap Type** | Mutual Exclusion (by product attribute) |
| **Shared Scope** | Pick and ship rotation priority |
| **Distinction** | BR-014 applies to shelf-life products; BR-015 to non-perishable standard goods. |
| **Business Impact** | Applying wrong rule ships suboptimal lot — expiry write-off (BR-014) or aged stock accumulation (BR-015). |
| **Recommendation** | Product master must classify rotation rule per SKU; never apply both simultaneously to same product. |

---

### OV-003 — BR-019 Independent Count Approval vs. BR-021 Independent Approval for Material Adjustments

| Attribute | Detail |
|-----------|--------|
| **Overlap Type** | Scope Overlap |
| **Shared Scope** | Segregation of duties for inventory adjustments |
| **Distinction** | BR-019: count-specific (counter ≠ approver). BR-021: value/quantity threshold for any adjustment. |
| **Business Impact** | Low-value count variance may satisfy BR-019 but not BR-021 threshold — approver rules differ. Material non-count adjustment triggers BR-021 only. |
| **Recommendation** | Apply both where applicable; BR-021 is superset for materiality; BR-019 always applies to count-originated adjustments regardless of value. |

---

### OV-004 — BR-020 Mandatory Reason Codes vs. BR-022 Investigate Before Adjusting

| Attribute | Detail |
|-----------|--------|
| **Overlap Type** | Scope Overlap |
| **Shared Scope** | Adjustment governance |
| **Distinction** | BR-022: process requirement (investigate first). BR-020: data requirement (reason code). |
| **Business Impact** | Reason code without investigation produces categorized but unexplained adjustments; investigation without code loses analytical value. |
| **Recommendation** | Enforce sequence: investigate (BR-022) → reason code reflects finding (BR-020) → approve (BR-019/BR-021). |

---

### OV-005 — BR-009 Reorder at Reorder Level vs. BR-032 Class A Priority Monitoring

| Attribute | Detail |
|-----------|--------|
| **Overlap Type** | Scope Overlap |
| **Shared Scope** | Low-stock response intensity |
| **Distinction** | BR-009: universal threshold trigger. BR-032: heightened frequency and escalation for Class A. |
| **Business Impact** | Class A stockout if treated with same response speed as Class C; or over-procurement if Class A rules applied to all SKUs. |
| **Recommendation** | BR-009 sets the trigger; BR-032 modulates response priority and monitoring cadence by classification. |

---

### OV-006 — BR-001 ATP-Only Commitment vs. BR-029 Promotional Ring-Fencing

| Attribute | Detail |
|-----------|--------|
| **Overlap Type** | Scope Overlap |
| **Shared Scope** | What quantity may be promised to customers |
| **Distinction** | BR-001: general ATP arithmetic. BR-029: commercial allocation restriction on subset of ATP. |
| **Business Impact** | See CF-005 — double-counting available stock across channels. |
| **Recommendation** | Campaign setup creates explicit ring-fence reservation reducing general ATP. |

---

### OV-007 — BR-023 Write-Off Authorization vs. BR-021 Material Adjustment Approval

| Attribute | Detail |
|-----------|--------|
| **Overlap Type** | Scope Overlap |
| **Shared Scope** | Authorization for inventory value removal |
| **Distinction** | BR-023: evidence and authorization specific to write-offs. BR-021: independent approver for material adjustments generally. |
| **Business Impact** | Write-off may satisfy BR-023 documentation but still need BR-021 approver if above threshold; or low-value write-off may need BR-023 evidence but not BR-021 escalation. |
| **Recommendation** | All write-offs require BR-023; material write-offs also require BR-021 independent approver. |

---

### OV-008 — BR-025 Return Authorization vs. BR-028 Backorder Acknowledgment

| Attribute | Detail |
|-----------|--------|
| **Overlap Type** | Scope Overlap (Principle) |
| **Shared Scope** | Explicit customer consent before recording commercial inventory state |
| **Distinction** | BR-025: inbound return acceptance. BR-028: outbound delay acceptance. |
| **Business Impact** | Inconsistent consent standards between returns and backorders erode customer trust policy coherence. |
| **Recommendation** | Unified "customer acknowledgment required" policy in training; separate process paths. |

---

## 6. High-Risk Dependency Failures

| Risk ID | Broken Dependency | Likely Symptom | Affected Objectives |
|---------|-------------------|----------------|---------------------|
| RK-001 | DEP-001 (BR-005 → BR-001) | Overselling received-but-not-located stock | BO-03 accuracy, BO-08 cancellation reduction |
| RK-002 | DEP-004/005 (BR-001 ↔ BR-002) | Double allocation of same units | BO-08, customer satisfaction |
| RK-003 | DEP-016–021 (Inbound → Financial) | Payment without receipt; receipt without PO | Audit, BO-18 valuation |
| RK-004 | DEP-030–032 (BR-009/011/012) | PO placed while transferable stock sits idle | Carrying cost, BO-17 network balance |
| RK-005 | DEP-038–040 (Count governance chain) | Adjustments without investigation or independent approval | BO-02 accuracy, fraud exposure |
| RK-006 | CF-005 / OV-006 (Promo vs ATP) | Campaign stockout despite warehouse availability | BO-14 promotional readiness |
| RK-007 | DEP-051–052 (Returns → ATP) | Damaged returns in sellable stock | Returns rate, customer complaints |

---

## 7. Dependency Statistics

| Metric | Count |
|--------|-------|
| Total dependencies cataloged | 58 |
| Prerequisite | 6 |
| Sequential | 22 |
| Compositional | 10 |
| Constraint | 14 |
| Reinforcement | 12 |
| Exception | 1 |
| Conflicts identified | 7 |
| Overlaps identified | 8 |
| Rules with no upstream dependency (foundational) | BR-007, BR-009, BR-014, BR-015, BR-018, BR-024, BR-025, BR-027, BR-029, BR-032 |
| Rules with highest fan-out (most dependents) | BR-001 (9), BR-004 (8), BR-022 (4), BR-013 (4) |

---

## 8. Traceability Reference

| Source | Identifier |
|--------|------------|
| Business Rules | SRS-BR-001 (BR-001 – BR-032) |
| Decision Tables | SRS-DT-001 (DT-01 – DT-32) |
| Business Exception Scenarios | SRS-EX-001 |
| Separation of Duties | SOD-003, SOD-004, SOD-006, SOD-007 |

---

## Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Senior Domain Expert | | | |
| Product Owner | | | |
| Operations Director | | | |
| Inventory Controller | | | |

---

*End of Business Rule Dependency Analysis*

*Document ID: SRS-BRDEP-001 | Version 1.0 | July 5, 2026*
