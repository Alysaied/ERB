# Business Discovery Phase — Review Report

**Prepared By:** Senior Business Consultant  
**Review Date:** June 2026  
**Documents Reviewed:**

| # | Document | Owner |
|---|----------|-------|
| 1 | Business Vision | CEO |
| 2 | Project Scope | Product Owner |
| 3 | Stakeholder Analysis | Senior Business Analyst |
| 4 | SMART Business Objectives | Business Analyst |
| 5 | Business Assumptions | Business Analyst |
| 6 | Business Constraints | Product Owner |
| 7 | Success Metrics | CEO / Product Owner |

**Review Purpose:** Assess completeness, consistency, and readiness of the Business Discovery phase before proceeding to requirements definition or solution selection. This report does not redesign the project.

---

## Executive Summary

The Business Discovery phase delivers a **coherent and well-structured foundation** for an Inventory Management System initiative. The documents are logically sequenced, mutually referential, and consistently focused on business outcomes rather than technical design. The vision is compelling, scope discipline is strong, stakeholder coverage is broad, and the measurement framework is ambitious.

However, the discovery set is **not yet decision-ready**. Several gaps stem from the intentional use of a generic company profile, while others reflect **internal inconsistencies** between documents — particularly around timelines, MVP boundaries, and KPI targets. The most significant risks are not missing features; they are **unvalidated baselines**, **undefined primary locations**, **organizational prerequisites assumed but not secured**, and **objectives that outpace MVP capability and rollout schedule**.

### Overall Readiness Assessment

| Area | Rating | Comment |
|------|--------|---------|
| Vision | **Strong** | Clear strategic narrative; lacks quantified business context |
| Scope | **Strong** | Well-bounded; boundary conflicts with objectives and stakeholders |
| Stakeholders | **Good** | Comprehensive profiles; missing governance RACI and HR/Legal |
| Objectives | **Good** | Thorough SMART structure; priority and timeline inconsistencies |
| Assumptions | **Good** | Broad coverage; needs validation status tracking |
| Constraints | **Good** | Realistic; mostly qualitative without numeric limits |
| Success Metrics | **Good** | Executive-ready framework; target misalignments and estimated baselines |
| **Cross-document consistency** | **Needs Work** | Several contradictions require resolution |
| **Discovery completeness** | **Incomplete** | Key artifacts missing before next phase |

**Recommendation:** Resolve critical contradictions and secure organizational prerequisites before approving funding or vendor engagement. The discovery phase is approximately **75–80% complete** from a business readiness standpoint.

---

## 1. Vision — Review

### Strengths

- Clear articulation of why inventory is a strategic asset, not a warehouse function
- Well-differentiated long-term (3–5 year) and short-term (12–18 month) horizons
- Business problems are specific, recognizable, and tied to financial and customer outcomes
- Phase structure (stabilize → perform → decide) provides a logical narrative arc for executives

### Missing Information

| Gap | Impact |
|-----|--------|
| **No quantified company profile** — revenue scale, number of locations, SKU count, employee count, geographic footprint | Objectives and KPI baselines are industry estimates, not company-specific; board cannot assess materiality |
| **No B2B vs. B2C revenue split or channel priority** | Vision mentions both equally; scope postpones channel integration — unclear which channel suffers most from current problems |
| **No named competitive or market context** | "Market leader" aspiration is unanchored; no benchmark for operational excellence |
| **No explicit link to corporate strategic plan** | Growth initiatives referenced in objectives (BO-23) are not described in the vision |
| **No failure cost quantification** | Vision states problems affect revenue and margin but provides no estimated annual cost of inaction |

### Contradictions

| Issue | Documents Affected |
|-------|-------------------|
| Long-term vision promises **accurate customer availability information**, but scope and constraints defer **all channel integration** to 12+ months | Vision §4 vs. Project Scope §2, Business Constraints TEC-04 |
| Phase 2 vision (months 6–12) includes **lowering excess inventory**, but SMART objective BO-09 targets month **18**, and scope classifies financial optimization as **Phase 3** | Vision §5 vs. SMART BO-09 vs. Project Scope §4 |

### Business Risks

- Vision ambition may create stakeholder expectations (especially sales and marketing) that MVP cannot satisfy
- Without quantified pain, executive commitment may weaken when implementation disruption occurs

### Unanswered Questions

1. What is the company's actual revenue, location count, and active SKU count?
2. Which sales channel (B2B or B2C) is the primary driver of inventory pain?
3. What specific growth initiatives are planned in the next 18 months?
4. What is the estimated annual cost of current inventory inefficiency?

### Recommendations

1. Add a **one-page business context appendix** with quantified company facts, even if anonymized
2. Align Phase 2 vision language with BO-09/BO-10 timing, or explicitly note that excess inventory reduction is a Phase 3 outcome
3. Qualify long-term customer availability claims with "as channels are integrated" to manage expectations
4. Commission a **cost-of-inaction estimate** to strengthen the investment narrative

---

## 2. Scope — Review

### Strengths

- Excellent in-scope / out-of-scope discipline with clear postponement rationale
- MVP is appropriately minimal and tied to Phase 1 vision
- Scope decision principles ("accuracy before intelligence") are sound and reusable
- Future enhancements are organized by phase without committing delivery

### Missing Information

| Gap | Impact |
|-----|--------|
| **"Primary locations" never defined** — count, names, volume share, rollout sequence | Referenced in scope, assumptions (BA-31: 80% volume), constraints (TC-03), and objectives — but no definitive list exists |
| **Order management system boundary undefined** | Scope includes order reservation and fulfillment, but source of orders (existing sales/ERP system) is not documented |
| **Integration touchpoints not mapped at business level** | Finance, sales, and purchasing systems are referenced as out of scope but no business-level interface document exists |
| **Data migration scope unclear** | MVP mentions "manual or simple data import" but volume, quality, and ownership of migration are undefined |
| **No explicit change control process** | Scope boundaries exist but no governance for scope change requests is documented |

### Contradictions

| Issue | Detail |
|-------|--------|
| **Returns handling** | In-scope features include "goods receipt (inbound from suppliers **or returns**)" but returns management is listed under "Postpone Until Organizational Readiness" — unclear what return capability MVP delivers |
| **MVP roles vs. stakeholder needs** | MVP includes only warehouse operator, supervisor, and administrator; BO-16 requires **sales self-service at month 6**, but expanded sales/purchasing roles are Phase 2 scope |
| **Replenishment in MVP vs. Phase 2** | MVP includes low-stock alerts; Phase 2 adds purchase requisition workflows — but BO-13 (90% replenishment within 2 days by month 12) implies purchasing discipline that may need more than alerts |
| **Executive dashboards** | MVP success criteria include "management dashboard for inventory health" but custom/role-specific dashboards are Phase 3 future enhancements |
| **KPI reporting in scope** | Phase 3 scope lists "inventory performance KPIs" as future enhancement, but success metrics document defines 28 KPIs from go-live |

### Business Risks

- Order-to-fulfillment boundary gap may cause duplicate entry or data conflicts with existing sales systems
- Undefined primary locations make rollout planning, budget sizing, and licensing cost estimation impossible
- MVP role limitations may block sales and purchasing objectives unless explicitly addressed in MVP scope

### Unanswered Questions

1. Which specific locations are "primary" and in what rollout order?
2. Where do customer orders originate today, and what is the business process for passing them to the warehouse?
3. What is the minimum return handling capability needed at MVP?
4. Will sales and purchasing users have MVP access, or must BO-16 wait for Phase 2 roles?

### Recommendations

1. Publish a **Primary Locations Register** with volume share, go-live sequence, and manager names
2. Create a **business-level system context diagram** showing IMS boundaries with finance, sales, and purchasing (no technical design — process handoffs only)
3. Clarify returns: define MVP as "simple return receipt with reason code" and defer "returns management workflow" — resolve the in-scope/out-of-scope conflict
4. Confirm whether **sales read-only access** is MVP or Phase 2; update scope or BO-16 timeline accordingly
5. Add a **scope change control policy** referencing Product Owner and steering committee authority

---

## 3. Stakeholders — Review

### Strengths

- Comprehensive coverage of 29 stakeholders across internal and external groups
- Consistent attribute structure (responsibilities, goals, pain points, permissions, interactions)
- Influence/interest matrix and stakeholder-to-feature mapping add practical value
- Dependency table clearly shows cross-functional relationships

### Missing Information

| Gap | Impact |
|-----|--------|
| **No RACI matrix** for key processes (receiving, counting, replenishment, fulfillment, adjustments) | Accountability gaps will emerge at go-live; overlaps with ORC-07 (no formal inventory function) |
| **HR function absent** | Labor law constraints (LC-03) and assumption BA-38 reference HR/union — no HR stakeholder profile |
| **Legal/Compliance function absent** | Regulatory authority is external; no internal legal counsel profile for LC-01, LC-05 |
| **Board of Directors / Investors** | CEO reports to board; no stakeholder profile for governance oversight |
| **Named individuals not assigned** | All profiles are role-based; no actual names for Sponsor, Product Owner, Inventory Controller |
| **Customer segmentation** | B2B and B2C treated as single profiles; no distinction by account size or channel |

### Contradictions

| Issue | Detail |
|-------|--------|
| **Sales Rep permissions vs. MVP scope** | Stakeholder analysis grants sales ATP read access; MVP scope limits roles to warehouse and admin — sales needs unaddressed in MVP |
| **Project Sponsor vs. CEO** | Both champion the initiative; relationship and decision authority between them undefined |
| **Finance Manager vs. CFO** | Both need valuation reports; reporting line and reconciliation ownership between them unclear |

### Business Risks

- Without RACI, Inventory Controller role creation (BA-03) may overlap with Warehouse Manager and Purchasing Manager responsibilities
- Missing HR and Legal stakeholders may delay policy updates required before go-live (BC constraints LC-03, ORC-07)
- Decentralized location managers (ORC-05) have autonomy that conflicts with central standardization — stakeholder analysis identifies this but no escalation path is defined

### Unanswered Questions

1. Who is the named Project Sponsor and Product Owner?
2. Who will be appointed Inventory Controller, and when?
3. What is the RACI for inventory accuracy, replenishment, and adjustment approval?
4. Who owns the relationship with HR and Legal for process policy changes?

### Recommendations

1. Add **RACI matrix** for five core inventory processes
2. Add stakeholder profiles for **HR Business Partner** and **Legal/Compliance Counsel**
3. Assign **named individuals** to Sponsor, Product Owner, and Inventory Controller before kickoff
4. Define **escalation path** from Warehouse Manager → Operations Director → COO for process non-compliance
5. Document **Project Sponsor charter** clarifying authority relative to CEO and department heads

---

## 4. Objectives — Review

### Strengths

- 24 SMART objectives provide thorough, measurable coverage of business outcomes
- Clear priority tiers (P1/P2/P3) aligned to vision phases
- Each objective includes why it matters, measurement, success criteria, and time frame
- Objective-to-vision alignment table is well constructed

### Missing Information

| Gap | Impact |
|-----|--------|
| **No consolidated business case objective** | ROI is only in success metrics (KPI-28), not in SMART objectives — investment justification not formally objective-driven |
| **No objective owner assigned** | Measurement governance lists roles but individual objective ownership is undefined |
| **No interdependency mapping** | BO-02 (accuracy) is prerequisite for most others but dependencies are implicit only |
| **Baselines not captured in objectives** | All targets are forward-looking; current state values exist only in success metrics estimates |

### Contradictions

| Issue | Detail |
|-------|--------|
| **Priority count error** | Summary states P2 = 12 and P3 = 5; actual count is **P2 = 11** (BO-04 through BO-17 excluding BO-09/10/18/20/23/24) and **P3 = 6** (BO-09, 10, 18, 20, 23, 24) |
| **P1 vs. 6-month summary** | Document states "7 P1 objectives must be achieved in the first 6 months" but **BO-02** (accuracy ≥ 95%) has target **month 12** while marked P1 |
| **BO-11 priority vs. deadline** | Marked P2 (Phase 2) but deadline is **month 18** (Phase 3) |
| **BO-18 and BO-20** | Marked P3 but deadline **month 12** — priority tier and phase misaligned |
| **Objective burden vs. constraints** | 24 objectives with 11 P2 targets at month 12, while sequential rollout may not complete all locations until month 12 (TC-03) — network-wide objectives may be unmeasurable at deadline |

### Business Risks

- Too many simultaneous objectives at month 12 creates accountability diffusion — steering committee cannot focus
- P1 misclassification of BO-02 may cause premature success declaration at month 6 (90% interim) while true P1 target is 95% at month 12
- Objectives assuming network-wide performance before all locations are live will show false underperformance or force rushed rollouts

### Unanswered Questions

1. Which single objective is the **primary success criterion** if trade-offs are required?
2. Are month 12 objectives measured network-wide or per live location?
3. Who owns each of the 24 objectives?
4. What happens if P1 objectives are met but P3 objectives fail — is the initiative still a success?

### Recommendations

1. **Correct priority counts** in summary (P2 = 11, P3 = 6)
2. Reclassify **BO-02**: either change to P2 with month 12 deadline, or keep P1 but split into interim (90% month 6) and final (95% month 12) with explicit labeling
3. Add **objective owner column** to summary matrix
4. Define **tiered success definition**: Minimum (all P1), Target (P1 + P2), Stretch (all) — for steering committee sign-off
5. Annotate network-wide objectives with **"measurable when ≥ 80% locations live"** per BA-31
6. Add explicit **objective dependency note** on BO-02 as gateway objective

---

## 5. Assumptions — Review

### Strengths

- 46 assumptions across 9 categories provide thorough risk foresight
- Each assumption includes reason, risk if false, and validation method
- Risk heat map (Critical/High/Medium/Low) enables prioritization
- Validation schedule by phase is practical
- Assumption-to-objective dependency table connects assumptions to outcomes

### Missing Information

| Gap | Impact |
|-----|--------|
| **No assumption status tracking** | All assumptions are undocumented as Validated / Unvalidated / Invalidated — no living log |
| **No assumption owner** | Validation methods name roles but not individual accountable owners |
| **No validation deadline dates** | Schedule says "pre-kickoff" and "discovery" but no calendar dates |
| **No consolidated risk register** | Assumption risks are dispersed; no single risk document with mitigation plans |
| **Existing systems landscape assumed** | BA-30 assumes systems remain in place but those systems are not inventoried |

### Contradictions

| Issue | Detail |
|-------|--------|
| **BA-04 vs. BC-02** | Assumption says staffing is sufficient; constraint says no headcount budget — both true but combined they leave **no buffer** if assumption fails |
| **BA-31 vs. undefined locations** | Assumes primary locations = 80% of volume but no document defines which locations qualify |
| **BA-23 vs. vision** | Assumes no channel integration pressure for 12 months; vision emphasizes multi-channel growth |
| **BA-13 vs. scope** | Assumes returns volume manageable manually; scope partially includes returns in receiving — validation threshold (5%) may be too late if discovered at month 3 |

### Business Risks

- **10 critical assumptions** include Inventory Controller existence (BA-03) and budget approval (BA-24) — neither has evidence of validation in discovery outputs
- If BA-03 fails (no Inventory Controller), 6+ objectives fail simultaneously — single point of failure
- Assumptions about supplier behavior (BA-19, BA-20) are external and largely uncontrollable

### Unanswered Questions

1. What is the current validation status of each of the 10 critical assumptions?
2. Who is the assumption owner and what is the validation due date?
3. What mitigation plans exist if BA-03 (Inventory Controller) or BA-34 (change resistance) fail?
4. What existing systems are in use for orders, finance, and purchasing?

### Recommendations

1. Create an **Assumption Log** with columns: ID, Status, Owner, Due Date, Evidence, Mitigation
2. **Validate all 10 critical assumptions** before project kickoff approval — block kickoff if BA-03 and BA-24 are unvalidated
3. Develop **mitigation plans** for top 5 critical assumptions (leadership commitment, Inventory Controller, budget, adoption, product catalog)
4. Add **existing systems inventory** as a business assumption validation output
5. Reconcile BA-23 with sales/marketing stakeholder expectations on channel timelines

---

## 6. Constraints — Review

### Strengths

- 38 constraints realistically reflect mid-market implementation challenges
- Constraint interaction table (compounding effects) is valuable and often overlooked
- Product Owner response strategy translates constraints into actionable guidance
- Alignment with assumptions table connects constraints to validation needs
- Severity classification (Blocking/High/Medium/Low) is clear

### Missing Information

| Gap | Impact |
|-----|--------|
| **No numeric budget figures** | BC-01 through BC-06 are qualitative — actual caps unknown |
| **Peak season dates undefined** | TC-04 references blackout periods but no calendar |
| **SME 20% allocation not confirmed** | ORC-01 states approximate allocation — not agreed with department heads |
| **No constraint exception process** | What happens if a blocking constraint must be relaxed? |
| **Geographic/jurisdictional scope** | Legal constraints reference GDPR and local law but operating jurisdictions not stated |

### Contradictions

| Issue | Detail |
|-------|--------|
| **TC-02 + TC-03 + TC-04** | MVP at month 6, sequential rollout over 6 months, plus peak blackouts — realistically pushes **full network live to month 12–15**, conflicting with month 6 and month 12 objective deadlines |
| **BC-02 + ORC-01 + BC-04** | No new headcount, part-time SMEs, capped training budget — **change capacity is critically thin**; constraints understate cumulative impact |
| **TEC-04 + vision customer experience** | Business constraint defers channel sync 12 months; vision promises customer availability improvements in Phase 2 |
| **ORC-07 (no inventory function) listed as Blocking** but no resolution path documented in any discovery artifact | Constraint identifies problem; assumptions say role will be assigned — gap between identification and commitment |

### Business Risks

- **Four blocking constraints** (BC-01, TC-02, OC-01, ORC-07) — ORC-07 has no assigned resolution action in discovery outputs
- Combined time constraints may make month 12 P2 objectives **mathematically unachievable** for network-wide metrics
- Fixed budget with 24 objectives and 28 KPIs creates **measurement and delivery overload** relative to resources

### Unanswered Questions

1. What is the approved budget amount (total, capex, opex)?
2. What are the specific peak season blackout dates per location?
3. Has the 20% SME allocation been agreed by Operations, Purchasing, and Sales directors?
4. What is the formal process to request a constraint exception?

### Recommendations

1. Document **approved budget ranges** at least at order-of-magnitude level for planning
2. Publish **rollout calendar** incorporating TC-02, TC-03, and TC-04 with realistic location live dates
3. Secure **written SME time commitment** from department heads — attach to ORC-01
4. Assign **immediate action** to resolve ORC-07: create Inventory Controller role before kickoff
5. Add **constraint exception process** (requestor, approver, impact assessment template)
6. Reconcile timeline constraints with objective deadlines — adjust targets or rollout plan

---

## 7. Success Metrics — Review

### Strengths

- 28 KPIs provide executive, operational, and tactical measurement layers
- KPI-to-SMART objective alignment table ensures traceability
- RAG status definitions and reporting cadence by audience are governance-ready
- Baseline collection protocol acknowledges estimates must be replaced
- Phased target summary aligns with vision phases

### Missing Information

| Gap | Impact |
|-----|--------|
| **All current states are estimates** | Every KPI uses industry benchmarks — no company-validated baseline exists |
| **Data source systems undefined** | Fill rate, cancellations, on-time delivery, NPS require order and customer data potentially **outside IMS** |
| **No KPI calculation ownership** | Reporting cadence lists audiences but not who calculates each KPI |
| **No target failure escalation process** | RAG definitions exist but remediation governance is undefined |
| **KPI burden vs. reporting capacity** | 28 KPIs with weekly, monthly, and quarterly frequencies — may overwhelm part-time SMEs |

### Contradictions

| KPI | Issue |
|-----|-------|
| **KPI-06 (Turnover)** | Summary dashboard shows **+15% at month 12**; detailed section says **+8% month 12, +15% month 18** |
| **KPI-07 (Excess Inventory)** | Dashboard shows **−20% at month 12**; detail says **−10% month 12, −20% month 18** |
| **KPI-26 (Growth Confidence)** | Dashboard month 12 column implies target at 12; detail and BO-23 say **≥ 4.0 at month 18** (3.5 at month 12) |
| **KPI-27 (NPS)** | Listed with month 12 dashboard column; detail target is **+10 points at month 18** |
| **KPI-09 naming** | Summary calls it "Gross Margin Impact from Shrinkage"; detail calls it "Shrinkage & Write-Off Value" — inconsistent naming |
| **KPI tier assignment** | KPI-19 (Sales Self-Service) is Tier 2 but BO-16 is P1 Critical — priority misaligned |

### Business Risks

- Measuring 28 KPIs with estimated baselines risks **false success or false failure** at first review
- KPIs depending on external systems (orders, CRM, ticketing) may be **unmeasurable** if integration is manual and deferred
- Executive dashboard with 11 Tier 1 KPIs may be **too dense** for monthly board reporting — lacks focus
- ROII (KPI-28) depends on benefit quantification methodology not defined in discovery

### Unanswered Questions

1. What system is the source of truth for order fill rate, cancellations, and on-time delivery?
2. Who calculates each KPI and with what data extract process?
3. Which 5 KPIs does the CEO consider **non-negotiable** success measures?
4. What is the ROII benefit calculation methodology and who approves it?

### Recommendations

1. **Reconcile all dashboard vs. detail target discrepancies** (KPI-06, 07, 26, 27 minimum)
2. Complete **baseline validation** before go-live — replace all estimates; block executive reporting until baselines are validated
3. Define **data source map** for each KPI (IMS, order system, finance GL, CS platform, survey)
4. Reduce executive dashboard to **5–7 primary KPIs** (recommend: KPI-01, 03, 04, 05, 09, 10, 28)
5. Assign **KPI calculation owner** per metric
6. Document **ROII methodology** with CFO approval before month 6 review
7. Align KPI-19 to Tier 1 or reclassify BO-16 — resolve priority inconsistency

---

## Cross-Document Analysis

### Consistency Matrix

| Topic | Vision | Scope | Stakeholders | Objectives | Assumptions | Constraints | Metrics | Status |
|-------|--------|-------|--------------|------------|-------------|-------------|---------|--------|
| 18-month horizon | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | **Aligned** |
| Primary locations | Implied | Referenced | — | Implied | 80% rule | Sequential rollout | — | **Undefined** |
| Sales user access | ✓ | MVP limited | ✓ permissions | BO-16 month 6 | — | — | KPI-19 | **Conflict** |
| Channel integration | ✓ long-term | Out of scope | Channel partner | — | Deferred 12mo | TEC-04 | — | **Conflict** |
| Excess inventory timing | Phase 2 | Phase 3 | — | BO-09 month 18 | — | — | KPI-07 mixed | **Conflict** |
| Returns handling | — | In + postponed | CS stakeholder | — | BA-13 | OC-06 | — | **Conflict** |
| Finance integration | Phase 3 | Deferred | CFO profile | BO-18 month 12 | — | TEC-05 manual | KPI-20 | **Tension** |
| Inventory Controller | Implied | — | Profile exists | BO-02, 03 | BA-03 critical | ORC-07 blocking | — | **Unsecured** |
| Network-wide metrics | Phase 1 | MVP primary only | — | Month 6–12 | BA-31 80% | TC-03 sequential | Month 12 targets | **Timeline risk** |
| Real-time visibility | ✓ | ✓ in scope | — | BO-01 | — | Manual bridges | — | **Tension** |

### Top 10 Business Risks (Consolidated)

| Rank | Risk | Source | Likelihood | Impact | Mitigation Priority |
|------|------|--------|------------|--------|---------------------|
| 1 | **No Inventory Controller appointed** — accuracy and governance objectives fail | BA-03, ORC-07 | High | Critical | Immediate |
| 2 | **Rollout timeline exceeds objective deadlines** — month 12 network KPIs measured before all locations live | TC-03, BO-05–15 | High | High | Immediate |
| 3 | **All KPI baselines are estimates** — success/failure unprovable | Success Metrics | Certain | High | Before go-live |
| 4 | **MVP role scope blocks sales objectives** — BO-16 at month 6 without sales access | Scope vs. BO-16 | High | High | Before MVP lock |
| 5 | **Change resistance and parallel tools persist** — adoption KPIs fail | BA-34, ORC-03, BO-22 | Medium | Critical | Change management |
| 6 | **Order system boundary undefined** — fulfillment KPIs unmeasurable or duplicated | Scope gap | High | High | Discovery gap |
| 7 | **Fixed budget with expansive objectives** — Phase 2/3 features unfunded | BC-01, 24 objectives | Medium | High | Prioritization |
| 8 | **Manual finance reconciliation** — BO-18/KPI-20 fail at month 12 | TEC-05, BO-18 | Medium | Medium | Process design |
| 9 | **Channel overselling continues** — customer impact despite internal improvements | TEC-04, BA-23 | Medium | High | Expectation management |
| 10 | **SME capacity insufficient** — requirements, UAT, and KPI reporting degraded | ORC-01, BC-04 | Medium | High | Resource commitment |

### Discovery Artifacts Still Missing

| Artifact | Why Needed | Suggested Owner |
|----------|------------|-----------------|
| **Business Case / ROI Model** | Investment approval, KPI-28 methodology | CFO + Project Sponsor |
| **Primary Locations Register** | Rollout planning, licensing, objective scoping | Operations Director |
| **Current State Process Maps (As-Is)** | Validate BA-07, workflow design | Business Analyst |
| **Existing Systems Landscape (business level)** | Integration boundaries, KPI data sources | Business Analyst |
| **RACI Matrix** | Process accountability | Operations Director |
| **Assumption Validation Log** | Track critical assumption status | Business Analyst |
| **Consolidated Risk Register** | Single view of initiative risks | Project Sponsor |
| **Change Management Plan** | Address ORC-03, BO-21, BO-22 | Product Owner |
| **Baseline Measurement Report** | Replace all KPI estimates | Business Analyst + Finance |
| **Steering Committee Charter** | Governance, escalation, scope authority | Project Sponsor |
| **Traceability Matrix** | Vision → Scope → Objectives → KPIs (single document) | Business Analyst |

---

## Areas Needing Clarification — Priority List

### Must Clarify Before Kickoff

1. Who is the named **Project Sponsor, Product Owner, and Inventory Controller**?
2. What are the **primary locations** and rollout sequence?
3. What is the **approved budget** (total, capex, opex)?
4. Where do **orders originate** and how do they reach fulfillment today?
5. Will **sales users** have IMS access at MVP or Phase 2?
6. What is the validation status of **10 critical assumptions**?

### Must Clarify Before MVP Scope Lock

7. What is the **minimum return handling** capability at MVP?
8. What **executive dashboard** content is MVP vs. Phase 3?
9. What **purchase order / replenishment** capability is needed for BO-13 by month 12?
10. Which **5–7 KPIs** are the non-negotiable executive success measures?

### Must Clarify Before First Go-Live

11. What are **validated baselines** for all KPIs and objectives?
12. What is the **approved compliance policy** for mandatory recording and reason codes?
13. What is the **hypercare support model** for the first 4 weeks post go-live?
14. What is the **parallel tool retirement plan** per location (BO-22)?

---

## Recommendations Summary

### Immediate Actions (Before Kickoff Approval)

| # | Action | Owner |
|---|--------|-------|
| 1 | Appoint and document Inventory Controller, Sponsor, and Product Owner | CEO |
| 2 | Publish Primary Locations Register with rollout calendar | Operations Director |
| 3 | Validate 10 critical assumptions; create Assumption Log | Business Analyst |
| 4 | Resolve MVP sales access scope conflict (update scope or BO-16 timeline) | Product Owner |
| 5 | Correct SMART objectives priority counts and P1/6-month inconsistencies | Business Analyst |
| 6 | Reconcile success metrics dashboard targets with detailed sections | Product Owner |
| 7 | Confirm approved budget ranges with CFO | Project Sponsor |

### Short-Term Actions (During Discovery Completion)

| # | Action | Owner |
|---|--------|-------|
| 8 | Create business-level systems landscape and order-to-fulfillment process map | Business Analyst |
| 9 | Develop RACI for core inventory processes | Operations Director |
| 10 | Build business case with cost-of-inaction and ROII methodology | CFO |
| 11 | Reduce executive KPI dashboard to 5–7 primary measures | CEO + Product Owner |
| 12 | Define tiered success criteria (Minimum / Target / Stretch) | Project Sponsor |
| 13 | Publish steering committee charter with scope change authority | Project Sponsor |
| 14 | Clarify returns scope boundary in project scope document | Product Owner |

### Ongoing Governance

| # | Action | Owner |
|---|--------|-------|
| 15 | Monthly assumption and constraint review at steering committee | Project Sponsor |
| 16 | Baseline validation report before go-live (block reporting without it) | Business Analyst |
| 17 | Quarterly cross-document consistency review as scope evolves | Product Owner |
| 18 | RAG escalation process for KPI failures | COO |

---

## Conclusion

The Business Discovery phase demonstrates **strong strategic thinking and unusual discipline in scope control** for an inventory initiative of this nature. The document set is suitable as a foundation for requirements definition **after identified gaps are closed**.

The discovery phase should **not be considered complete** until:

- Organizational prerequisites are secured (Inventory Controller, Sponsor, SME commitments)
- Primary locations and rollout calendar are defined
- Critical contradictions between scope, objectives, and metrics are resolved
- Baselines are validated rather than estimated
- Missing governance artifacts (RACI, assumption log, business case, systems landscape) are produced

With these actions, the organization can proceed to the next phase with **confidence that the business problem is understood, the scope is achievable, and success is measurable**. Without them, the initiative risks delivering a system that is technically deployed but fails to achieve the business outcomes the vision promises.

---

*End of Business Discovery Review Report*
