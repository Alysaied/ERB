# Domain Knowledge Phase — Review Report

**Reviewer Role:** Senior Inventory Consultant  
**Date:** July 3, 2026  
**Scope Reviewed:** Seven Domain Knowledge deliverables plus alignment with Business Discovery and Business Domain artifacts  
**Review Type:** Completeness, consistency, and readiness for requirements analysis

---

## Executive Summary

The Domain Knowledge phase is **substantially complete and well-structured** for a general-purpose, multi-industry inventory management initiative. The seven documents form a coherent knowledge stack — concepts establish the foundation, standards and best practices define *how* work should be done, the advanced glossary extends vocabulary, scenarios make situations concrete, challenges explain persistent failures, and rules codify non-negotiable policy.

**Overall readiness for requirements analysis: Conditional Go (≈75–80%)**

The knowledge base is strong enough to begin functional requirements, but several **scope-alignment gaps**, **missing operational areas**, and **unresolved policy questions** should be addressed early in requirements workshops. Without that, requirements risk reflecting generic industry knowledge rather than this organization's operating model.

| Document | Items | Quality | Primary Gap |
|----------|-------|---------|-------------|
| Core Concepts | 13 | Strong | Manufacturing, omnichannel, ownership models underrepresented |
| Industry Standards | 18 | Strong | Regulated-industry and retail-shrinkage standards thin |
| Best Practices | 18 | Strong | Limited exception/authority guidance |
| Advanced Glossary | 60 | Strong | Overlaps standards; some terms exceed project scope |
| Business Scenarios | 25 | Strong | Missing procurement, VMI, kitting, customs scenarios |
| Common Challenges | 20 | Strong | Organizational and integration challenges light |
| Industry Rules | 32 | Strong | Missing tolerance, channel, and exception rules |

---

## 1. Domain Concepts — Assessment

### Strengths

- Covers the full operational lifecycle: visibility → supply → demand → control → finance → governance.
- The concept connection diagram clearly shows reinforcing relationships.
- Availability states (on-hand, reserved, committed, inbound, ATP) are well articulated.
- Network thinking is treated as a first-class concept, not an afterthought.

### Missing Concepts

| Missing Concept | Why It Matters |
|-----------------|----------------|
| **Inventory ownership models** (owned, consignment, VMI, drop-ship) | Governs when stock enters the balance sheet and who replenishes |
| **Storage hierarchy** (location → zone → aisle → bin) | Warehouse operations and pick accuracy depend on it |
| **Unit of measure conversion** | Case/each/pallet mismatches are a top source of quantity errors |
| **Product substitution / alternates** | Critical when primary SKU is unavailable |
| **Kitting and bill-of-materials explosion** | Even distributors assemble kits; manufacturing-adjacent orgs need it |
| **Channel allocation** | Distinct from reservation — governs how network stock is split across channels |
| **Inbound ownership timing** (Incoterms / goods-in-transit) | Finance and operations must agree when stock is "ours" |
| **Demand planning vs. replenishment execution** | S&OP and forecasting are referenced in the glossary but not as core concepts |
| **Capacity and throughput constraints** | Receiving docks, pick capacity, and storage limits affect what "available" means |
| **Cold chain / hazmat segregation** | Regulated and perishable operations need explicit concept coverage |

### Observation

Core concepts are optimized for **distribution and retail**. Manufacturing (WIP, raw materials, production consumption) and **heavy compliance** (serialization, regulatory holds) appear only in the advanced glossary, not in the foundational concept set.

---

## 2. Industry Standards — Assessment

### Strengths

- Good blend of formal standards (GS1, Incoterms, COSO/SOX-aligned segregation) and operational conventions (ABC, EOQ, FIFO/FEFO, cycle counting).
- The "standards working together" section provides a practical operating model.
- Performance benchmarks (fill rate, accuracy) give measurable targets.

### Missing Standards

| Missing Standard | Relevance |
|------------------|-----------|
| **XYZ / ABC-XYZ classification** | Demand variability classification — referenced in glossary, absent from standards |
| **OTIF (On Time In Full)** | Major retail-supplier standard; in glossary but not standards doc |
| **Receiving tolerance standards** (acceptable over/under-ship %) | Every receiving operation needs defined tolerance |
| **Dock-to-stock time SLA** | In glossary; should be elevated as operational standard |
| **NRF / industry shrinkage benchmarks** | Retail loss prevention benchmark missing |
| **HACCP / GMP / FSMA traceability expectations** | Food and pharma compliance standards not covered |
| **VED analysis** (Vital, Essential, Desirable) | Common in healthcare/MRO classification |
| **Inventory costing methods** (FIFO, LIFO, WAC, standard cost) | Financial standard partially covered only via WAC in glossary |
| **CPFR / collaborative planning norms** | Relevant for key supplier relationships |
| **Periodic vs. perpetual inventory** | Perpetual covered; periodic as alternative approach not documented |

### Observation

Standards documentation is **operationally strong for general distribution** but **not sufficient for regulated or healthcare verticals** without supplemental domain work.

---

## 3. Best Practices — Assessment

### Strengths

- Highly actionable and aligned with rules and standards.
- Maturity model (Stabilizing → Refining) is useful for phased adoption.
- "Practices that reinforce each other" table adds practical value beyond a flat list.

### Gaps

| Gap | Detail |
|-----|--------|
| **Exception management** | Practices describe ideal state; little guidance on authorized exceptions |
| **3PL / outsourced warehouse** | No practices for third-party operated facilities |
| **Opening balances / go-live** | No practice for establishing initial inventory trust at launch |
| **Substitution management** | No practice for offering alternates when primary SKU is out |
| **Supplier collaboration** | ASN and OTIF in glossary; no best practice for supplier scorecarding |
| **Data migration hygiene** | Not covered — critical for IMS implementations |

### Potential Internal Tension (see Conflicting Practices)

Best Practice #8 (put-away before availability) may conflict with cross-docking operations documented in Industry Standards #15.

---

## 4. Advanced Terminology — Assessment

### Strengths

- Excellent extension beyond the 50-term Business Glossary.
- Strong coverage of planning (MRP, DRP, DDMRP, S&OP), omnichannel, and financial metrics (GMROI, DIO).
- "Commonly confused term pairs" table reduces ambiguity.

### Gaps

| Missing Terms | Notes |
|---------------|-------|
| BOPIS / BORIS | Core omnichannel terms absent |
| Goods Receipt Note (GRN) | Common inbound document |
| Substitution / alternate SKU | Fulfillment term |
| Allocation run / push distribution | Retail initial distribution |
| Kitting / assembly | Product structure |
| Hazmat / dangerous goods classification | Compliance |
| Pre-pack / pack optimization | Retail distribution |
| Reservation expiry | Fulfillment control |
| Tolerance threshold | Count and receiving |
| Opening balance / seed stock | Implementation term |

### Overlap Concern

Approximately **12–15 terms duplicate** content already in Industry Standards (EOQ, cross-docking, three-way match, slotting, wave picking, etc.). This is acceptable if the glossary is a reference index, but requirements authors may cite conflicting levels of detail.

### Scope Misalignment

Advanced glossary includes **MRP, BOM, WIP, VMI, serialization, bonded warehouse** — several explicitly **out of scope** in the Project Scope document. This creates risk that stakeholders expect capabilities the product will not deliver in initial releases.

---

## 5. Business Scenarios — Assessment

### Strengths

- 25 scenarios cover the highest-frequency operational situations.
- Each scenario includes actors, expected outcome, and business considerations — directly usable in use case workshops.
- Scenario response patterns table connects situations to disciplines.

### Missing Scenarios

| Missing Scenario | Why Include |
|------------------|-------------|
| **Supplier over-shipment** | Complement to short-shipment; different approval and payment rules |
| **Partial receipt across multiple deliveries** | One PO, multiple shipments — common in B2B |
| **Product substitution requested by customer** | Availability recovery without stockout |
| **Kit/assembly component shortage** | Blocks parent SKU fulfillment |
| **Consignment stock reconciliation with supplier** | Ownership timing disputes |
| **VMI supplier replenishment visit** | Out of product scope but may exist operationally |
| **Inbound customs / bonded release** | International operations |
| **Opening inventory establishment (go-live)** | Every IMS project needs this scenario |
| **Store associate-initiated transfer** | Retail floor practice |
| **Bulk damage event** (fire, flood, container loss) | Catastrophic adjustment scenario |
| **Inbound ASN mismatch** | ASN says 1,000; physical is 900 |
| **Auto-replenishment generates wrong quantity** | Policy misconfiguration scenario |

### Observation

Scenarios align well with Business Workflows (32 processes) but do not explicitly **map scenario → process → rule**, which would accelerate traceability in requirements.

---

## 6. Common Challenges — Assessment

### Strengths

- Root-cause orientation is strong — causes, impacts, and mitigations are practical.
- Interdependency chain diagram shows how challenges cascade.
- Mitigation priority framework aligns with project phasing (stabilize first).

### Gaps

| Missing Challenge | Relevance |
|-------------------|-----------|
| **Skills and training deficit** | BC-02 (no new headcount) makes this critical |
| **Integration dependency with orders/purchasing** | Business-level, not technical — who owns the handoff? |
| **Seasonal operational capacity overload** | Receiving and count discipline fails during peak |
| **Vendor / supplier master data quality** | Bad lead times corrupt replenishment |
| **Parallel system operation during transition** | Dual-running old and new records |
| **Executive metric distrust** | Cultural challenge beyond data accuracy |
| **Contractual customer SLA pressure** | B2B penalty exposure not addressed |

### Overlap with Business Pain Points

The Challenges document and `business-pain-points.md` (28 pain points) cover **~70% overlapping territory**. Pain points are organization-specific and severity-rated; challenges are industry-generic. Both are valuable, but requirements workshops should use **pain points for prioritization** and **challenges for completeness checking** — this distinction is not documented.

---

## 7. Industry Rules — Assessment

### Strengths

- 32 rules cover availability, inbound, replenishment, network, quality, governance, returns, and trade.
- Control objective mapping and rule combination table are excellent for policy design.
- Correctly framed as operational policy, not system validation.

### Missing Rules

| Missing Rule | Domain |
|--------------|--------|
| **Negative sellable inventory prohibited** | Record integrity |
| **Over-receipt beyond tolerance requires approval** | Inbound |
| **Reservation expires if order not fulfilled within N days** | Fulfillment |
| **Channel priority during scarcity** (defined hierarchy) | Omnichannel |
| **Substitution only to pre-approved alternate SKUs** | Fulfillment |
| **UOM conversion must use official product conversion factors** | Master data |
| **Inbound stock ownership per agreed Incoterm / contract** | Trade |
| **Count variance within tolerance auto-accepts; above tolerance investigates** | Control |
| **Inter-company transfers require dual-location confirmation** | Network |
| **Kit cannot ship until all components available** | Fulfillment |
| **Opening balance requires dual sign-off at go-live** | Implementation |

### Rules Without Defined Parameters

Many rules reference thresholds that are **not parameterized** anywhere in Domain Knowledge:

- Adjustment approval threshold ("above 10 units or $500" appears only as an example in challenges, not as a rule parameter)
- Receiving tolerance percentage
- Count variance tolerance
- Reservation hold duration
- MRSL days by product category

Requirements analysis cannot specify behavior without these business decisions.

---

## Cross-Cutting Strengths

1. **Consistent vocabulary** across documents — ATP, ABC, FIFO/FEFO, three-way match, SLOB used uniformly.
2. **Business-only framing** maintained throughout — no implementation leakage.
3. **Complementary layering** — concepts explain *why*, standards describe *norms*, practices recommend *how*, rules define *must*, scenarios show *when*.
4. **Strong alignment** with Business Glossary (50 terms), Business Processes (32), and Business Events (52).
5. **Traceability potential** — rules ↔ practices ↔ standards ↔ scenarios form a requirements traceability backbone once explicitly linked.

---

## Conflicting or Ambiguous Practices

| # | Conflict | Documents Involved | Resolution Needed |
|---|----------|------------------|-------------------|
| 1 | **Put-away before availability** vs. **cross-docking** | Best Practices #8, Standards #15 | Cross-docked goods bypass storage — define when put-away rule applies vs. cross-dock exception |
| 2 | **PO required before receiving** vs. **ad-hoc receipts in MVP** | Rules #7, Project Scope MVP | Clarify whether emergency/ad-hoc receiving is permitted and under what approval |
| 3 | **Advanced manufacturing terms** vs. **manufacturing out of scope** | Advanced Glossary, Project Scope | Glossary educates domain; scope limits product — document explicitly as "domain knowledge vs. product boundary" |
| 4 | **Lot traceability as standard** vs. **compliance modules out of scope** | Standards #17, Project Scope | Define minimum lot capture (record only) vs. full regulatory reporting |
| 5 | **VMI and consignment in glossary** vs. **VMI out of scope** | Advanced Glossary, Project Scope | Clarify whether consignment/VMI is tracked manually or excluded entirely in Phase 1 |
| 6 | **Fill rate definition variants** | Business Glossary, Standards #17, Scenarios | Business Glossary notes fill rate measurement nuances — pick one organizational definition |
| 7 | **Safety stock bypass with exception** (Rule 10) vs. **never consume safety stock casually** (Challenges mitigation) | Rules, Challenges | Define who can authorize exception and required replenishment plan |
| 8 | **Class A weekly count** (Rule 32) vs. **ABC-based frequencies** (Standards #2) | Rules, Standards | Harmonize — Rule 32 says "highest frequency" but doesn't specify weekly vs. monthly |

---

## Knowledge Gaps (Cross-Document)

### A. Organizational Context Not Anchored

Domain Knowledge is **industry-generic**. It does not reflect the specific organization described in Business Discovery:

- Mid-sized multi-location **distribution and retail** (from pain points)
- Fixed budget, no new headcount (BC-02)
- Phased MVP → near-term → future approach

The knowledge base does not indicate **which concepts, standards, and rules apply in Phase 1 (MVP) vs. later phases**.

### B. Role and Authority Matrix Missing

Rules and scenarios name actors but no document defines:

- Who can approve adjustments, write-offs, transfers, exceptions
- Dollar/quantity approval thresholds by role
- Segregation of duties by role (only by principle)

### C. Integration Boundaries (Business Level)

No Domain Knowledge artifact defines business handoffs with:

- Order management / sales orders
- Purchasing / procurement
- Finance / GL
- POS (retail)
- External suppliers (ASN, VMI)

Requirements will need integration stories even if technical integration is deferred.

### D. Metric Definitions and Targets Not Consolidated

Targets appear scattered:

- Fill rate: 95–98% retail, 98–99.5% healthcare (Standards)
- Accuracy: 99%+ Class A, 97%+ overall (Standards, Challenges)
- Shrinkage: 1.5–2% mentioned in Challenges only
- OTIF: 88% example in glossary — no organizational target

A **single metrics dictionary** with organizational targets is missing.

### E. Regulated Industry Depth

Food, pharma, and medical device rules (MRSL, serialization, GMP, mock recall) appear fragmentarily. If the organization handles regulated goods, a **vertical supplement** is required.

### F. Implementation and Transition Scenarios

No coverage of:

- Opening balance / cutover
- Parallel run period
- Data cleansing and SKU deduplication
- Legacy spreadsheet retirement

These are operational realities for any IMS initiative.

### G. Traceability Matrix Not Built

No document links:

`Scenario → Process (BP-xx) → Rule → Practice → Concept → Pain Point`

This matrix would be the primary requirements analysis input.

---

## Questions to Answer Before Requirements Analysis

### Strategic and Scope

1. What is the **primary industry vertical** for Phase 1 — general distribution, retail, healthcare, manufacturing, or mixed?
2. Which **location types** are in MVP — warehouses only, or warehouses + stores?
3. Is **omnichannel** (ship-from-store, endless aisle, BOPIS) in MVP, near-term, or out of scope?
4. Does the organization handle **regulated products** (food expiry, pharma lots, hazmat)?
5. What is explicitly **out of scope for operations** even if industry knowledge covers it (VMI, MRP, serialization)?

### Availability and Fulfillment

6. What is the **authoritative ATP formula** — does it subtract reserved only, or also soft allocations and quarantine?
7. When does **reservation occur** — order creation, payment confirmation, or credit approval?
8. Do **reservations expire**? If so, after how long and with what notification?
9. What is the **channel priority hierarchy** when stock is scarce (wholesale vs. retail vs. e-commerce)?
10. Are **product substitutions** permitted? If so, who approves and is a substitute list maintained?
11. Is **partial shipment** default behavior or opt-in per customer/order?
12. Does the business use **cross-docking**? If yes, how is "available" defined for cross-docked stock?

### Inbound and Procurement

13. Is a **purchase order mandatory** for all receipts, or are ad-hoc/emergency receipts permitted?
14. What are **receiving tolerances** — acceptable over/under-ship percentages by product class?
15. Is **ASN** used today? Is it required for receiving efficiency in target state?
16. What is the target **dock-to-stock SLA**?
17. When does **inventory ownership transfer** — at receipt, at shipment from supplier, or per Incoterm?

### Replenishment and Policy

18. What **replenishment method** is primary — reorder point, min-max, or manual review?
19. Who **owns reorder parameter maintenance** — central planning, buyers, or location managers?
20. How often are **reorder points and safety stock recalculated**?
21. What **service level targets** by ABC class (e.g., A = 98%, B = 95%, C = 90%)?
22. Is **network check before purchase** a mandatory rule or recommended practice?

### Inventory Control

23. What are **count frequencies** by ABC class at this organization?
24. What is the **variance tolerance** — auto-accept below N units/percent, investigate above?
25. What are **adjustment approval thresholds** by role and dollar value?
26. What is the **standard reason code list** — fixed corporate list or location-extensible?
27. Is **blind counting** mandatory for all counts or only cycle counts?

### Network and Transfers

28. Who can **initiate transfers** — central planning only, or location managers?
29. What **transfer approval** is required, and what are source minimum protections?
30. What is the expected **transfer lead time** by lane (DC-to-store, store-to-store)?

### Financial Alignment

31. What **costing method** applies — WAC, FIFO, standard cost?
32. How often do **operations and finance reconcile**, and what tolerance is acceptable?
33. Who approves **write-offs and E&O provisions**?
34. Is **landed cost** tracked in inventory valuation or handled in finance only?

### Governance and Compliance

35. What is the **segregation of duties matrix** by role for count, adjust, approve, receive?
36. Is the organization subject to **SOX or external audit** inventory controls?
37. What **lot/batch capture** is required at MVP — none, optional, or mandatory by product class?
38. What **audit trail retention period** is required?

### Organizational and Transition

39. How many **locations and SKUs** in MVP vs. full rollout?
40. What is the **opening balance / cutover approach** — big bang, phased by location?
41. Will **parallel operation** with spreadsheets occur during transition? For how long?
42. What **training capacity** exists given no new headcount (BC-02)?
43. Which **pain points (PP-01 to PP-28)** are MVP must-solve vs. Phase 2?

---

## Readiness Assessment

| Criterion | Status | Comment |
|-----------|--------|---------|
| Foundational concepts defined | ✅ Ready | 13 concepts cover core operating model |
| Industry norms documented | ✅ Ready | 18 standards sufficient for general distribution/retail |
| Operational guidance available | ✅ Ready | 18 practices + 32 rules provide policy foundation |
| Situation catalog for use cases | ✅ Ready | 25 scenarios cover majority of daily operations |
| Problem domain understood | ✅ Ready | 20 challenges + 28 pain points (business domain) |
| Advanced vocabulary available | ✅ Ready | 60 terms; watch scope alignment |
| Organizational policy decisions made | ⚠️ Not ready | Thresholds, tolerances, approvals undefined |
| Phase prioritization mapped | ⚠️ Not ready | Domain knowledge not tagged MVP vs. Phase 2 |
| Vertical/regulatory clarity | ⚠️ Not ready | Generic — regulated ops need supplement |
| Traceability to requirements inputs | ⚠️ Not ready | No scenario-to-rule-to-process matrix |
| Conflict resolution | ⚠️ Not ready | 8 identified conflicts need decisions |
| Integration boundaries | ⚠️ Not ready | Business handoffs not documented |

---

## Recommendations

### Before Requirements Workshops (Must Do)

1. **Answer the 43 questions above** — at minimum, questions 1–5 (scope), 6–12 (fulfillment), 23–26 (control), and 39–43 (transition).
2. **Resolve the 8 identified conflicts** — especially PO-required vs. ad-hoc receipt and put-away vs. cross-dock.
3. **Tag Domain Knowledge by phase** — mark each rule, practice, and scenario as MVP, Phase 2, or reference-only.
4. **Build a traceability matrix** linking scenarios to business processes (BP-01–32), rules, and pain points.

### During Requirements Analysis (Should Do)

5. Produce an **organizational metrics dictionary** with adopted targets for fill rate, accuracy, OTIF, shrinkage, and dock-to-stock.
6. Produce a **role and approval authority matrix** derived from governance rules.
7. Add **5–8 missing scenarios** (opening balance, over-shipment, substitution, partial multi-receipt, ASN mismatch).
8. Clarify **product boundary document** — what advanced glossary terms are educational only vs. in-scope capability.

### Optional Enrichment (Could Do)

9. Vertical supplement if regulated products apply (food/pharma).
10. Consolidate challenges and pain points into a single **prioritized problem backlog**.
11. Add missing standards (OTIF, receiving tolerance, shrinkage benchmark, ABC-XYZ).

---

## Conclusion

The Domain Knowledge phase delivers a **high-quality, internally consistent body of operational inventory knowledge** suitable as the intellectual foundation for requirements analysis. It is notably strong in availability management, inbound discipline, inventory control, network balancing, and governance.

The phase is **not yet sufficient on its own** to write unambiguous requirements because it lacks **organization-specific policy parameters**, **phase prioritization**, **role authority definitions**, and **explicit resolution of scope tensions** between domain breadth and project scope.

**Recommendation:** Proceed to requirements analysis after a focused **Domain Knowledge Validation Workshop** (1–2 sessions) to answer the critical questions, resolve conflicts, and produce the traceability matrix and phased applicability map.

---

## Related Documents

| Document | Path |
|----------|------|
| Core Inventory Management Concepts | `Domain Knowledge/core-inventory-management-concepts.md` |
| Inventory Management Industry Standards | `Domain Knowledge/inventory-management-industry-standards.md` |
| Inventory Management Best Practices | `Domain Knowledge/inventory-management-best-practices.md` |
| Advanced Inventory Management Glossary | `Domain Knowledge/advanced-inventory-management-glossary.md` |
| Common Business Scenarios | `Domain Knowledge/common-inventory-management-scenarios.md` |
| Common Challenges | `Domain Knowledge/common-inventory-management-challenges.md` |
| Industry Business Rules | `Domain Knowledge/inventory-management-business-rules.md` |
| Business Pain Points | `business domain/business-pain-points.md` |
| Project Scope | `businsess discovery/project-scope.md` |

---

*End of Domain Knowledge Phase Review Report*
