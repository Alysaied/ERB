# Database Design Review Report
## Inventory Management System — Chief Database Architect Assessment

---

## Document Information

| Attribute | Detail |
|-----------|--------|
| **Document ID** | SRS-DB-009 |
| **Document Title** | Database Design Review — Pre-API Design Gate |
| **Version** | 1.0 |
| **Status** | Draft — Review Findings |
| **Document Owner** | Chief Database Architect |
| **Artifacts Reviewed** | SRS-DB-001 through SRS-DB-008 |
| **Review Date** | July 6, 2026 |
| **Gate Purpose** | Approve or conditionally approve database design before API Design phase |

### Artifacts Under Review

| Doc ID | Title | Version | Verdict |
|--------|-------|---------|---------|
| SRS-DB-001 | Logical Data Model (ERD) | 1.0 | Sound foundation — minor cardinality gaps |
| SRS-DB-002 | Physical Data Model | 1.0 | Complete — table count discrepancy |
| SRS-DB-003 | Database Keys | 1.0 | Comprehensive — strong UK coverage |
| SRS-DB-004 | Database Constraints | 1.0 | Strong — critical gaps documented honestly |
| SRS-DB-005 | Database Indexing Strategy | 1.0 | Well-prioritized — ready for DDL |
| SRS-DB-006 | Database Audit Strategy | 1.0 | Mature three-layer model |
| SRS-DB-007 | Data Dictionary | 1.0 | Complete for 58 defined tables |
| SRS-DB-008 | Database Naming Conventions | 1.0 | Consistent and scalable |

---

## Executive Summary

The IMS database design is **architecturally sound and substantially complete** for a modular-monolith inventory platform. The design correctly centers on `inventory.stock_positions` as the quantity hub, separates bounded contexts into PostgreSQL schemas, and pairs transactional tables with append-only audit projections. Keys, constraints, and indexing strategy are aligned with business rules BR-001 through BR-032.

**Overall assessment: CONDITIONAL GO** for API Design — proceed after resolving **3 P1 blockers** and acknowledging **8 P2 items** in the first migration sprint.

| Dimension | Rating | Summary |
|-----------|--------|---------|
| Logical model fidelity | **Strong** | 40 entities + 4 derived map cleanly to aggregates |
| Physical model completeness | **Good** | 58 tables defined; 2 infrastructure tables missing |
| Referential integrity | **Good** | ~145 FKs; some cross-context coupling to review |
| Constraint coverage | **Good** | ATP formula, SoD checks, XOR origins enforced; cross-aggregate rules deferred to app |
| Index strategy | **Strong** | Tiered, partial indexes; avoids duplication |
| Audit & compliance | **Strong** | Movement + trail + retention; tiered storage pending |
| Scalability readiness | **Moderate** | Partitioning designed; hot-path contention and outbox growth need DDL |
| Documentation coherence | **Good** | Minor inconsistencies between artifacts |

---

## 1. Logical Data Model Review (SRS-DB-001)

### Strengths

- Aggregate boundaries are respected — no shared mutable structures across consistency boundaries.
- LDM integrity rules LDM-01 through LDM-10 are explicit and traceable to business rules.
- Derived entities (Movement Record, Audit Trail, Operational Alert, Valuation Snapshot) are correctly modeled as projections, not transactional aggregates.
- Cross-aggregate reference model (identity references + domain events) aligns with ADR-024 and DDD module design.

### Issues Identified

| ID | Severity | Finding |
|----|----------|---------|
| LDM-01 | **P2** | **Fulfillment Execution → Shipment cardinality** — LDM states `1 : 0..1`; physical model allows multiple `shipments` per `fulfillment_execution_id` (partial shipments). Physical model is more realistic — **update LDM** to `1 : 0..*`. |
| LDM-02 | **P2** | **Opening Balance workflow absent** — LDM references location activation and stock position creation but no Opening Balance Establishment entity (HS-002, ADR-027). Go-live path is incomplete at logical level. |
| LDM-03 | **P3** | **Promotional ring-fence** modeled as modification of Stock Position but no logical attribute for ring-fenced quantity on Stock Position — segregation is application-calculated only. |
| LDM-04 | **P3** | **Supplier in Catalog & Network BC** in bounded-context ownership table but physically in `procurement` schema — acceptable denormalization of ownership vs. storage. |

### Recommendations

1. Amend SRS-DB-001 cardinality for Shipment and document partial-shipment pattern.
2. Add logical entity or subprocess for **Opening Balance Certification** before API exposes location activation.
3. Document promotional ATP segregation as a **derived calculation** in LDM narrative.

---

## 2. Physical Data Model Review (SRS-DB-002)

### Strengths

- 14 schemas mirror bounded contexts — supports modular monolith and clear ownership.
- Sensible header/line normalization for all document aggregates.
- Growth tiers and partitioning strategy documented for movement and audit tables.
- Consistent use of `BIGINT` identity PKs, `NUMERIC` quantities, `TIMESTAMPTZ` timestamps.

### Issues Identified

| ID | Severity | Finding |
|----|----------|---------|
| PDM-01 | **P1** | **Table count mismatch** — Appendix A cites **59 tables** (`procurement` = 8) but only **7 procurement tables** and **58 total** are defined in the PDM body. Data Dictionary correctly notes 58. **Reconcile appendix or add missing table.** |
| PDM-02 | **P1** | **Transactional outbox table missing** — ADR-006, architecture review (G-01), and technology stack require `platform.outbox_event` (or equivalent) in same PostgreSQL database. Not in any SRS-DB artifact. **Required before event-driven API contracts.** |
| PDM-03 | **P1** | **Opening balance / go-live tables missing** — No `opening_balance_submissions`, `opening_balance_lines`, or certified subprocess tables. Blocks FR-010, HS-002, and `ActivateInventoryLocation` API design. |
| PDM-04 | **P2** | **PostgreSQL version inconsistency** — SRS-DB documents say PostgreSQL **15+**; ADR PostgreSQL decision cites **16**. Align to single version before DDL. |
| PDM-05 | **P2** | **No `platform` schema** for cross-cutting infrastructure (outbox, idempotency, saga state). Recommended before API idempotency keys are defined. |
| PDM-06 | **P2** | **`product_identifiers` missing `updated_at`** — inconsistent with mutable-table convention; add if identifiers can be deactivated/changed. |
| PDM-07 | **P3** | **No persistent unit cost table** — `unit_cost` appears only on valuation snapshot lines. Three-way match (BR-008) implies cost authority at receipt — consider `inventory.product_cost_layers` or document as application-derived at snapshot time. |
| PDM-08 | **P3** | **Customs clearance (BR-030)** — partially modeled via `quarantine_holds` + `ownership_type = BONDED` but no dedicated customs clearance document. May suffice if hold workflow is complete. |

### Missing Tables (Recommended)

| Table | Schema | Purpose | Priority |
|-------|--------|---------|----------|
| `outbox_events` | `platform` | Transactional outbox (ADR-006) | **P1** |
| `idempotency_keys` | `platform` | API/command deduplication (NFR-REL) | **P2** |
| `opening_balance_certifications` | `accuracy` or `network` | Go-live workflow header (HS-002) | **P1** |
| `opening_balance_lines` | `accuracy` or `network` | Product × location opening qty lines | **P1** |
| `saga_instances` | `platform` | Optional — long-running saga state (SAG-01, SAG-04, SAG-05) | **P3** |

### Redundant Tables Assessment

| Table Pair | Verdict |
|------------|---------|
| `stock_policies` + `stock_policy_history` | **Not redundant** — history is append-only audit-optimized; keep both |
| `transfer_requests` + `stock_transfers` | **Not redundant** — request vs. execution lifecycle per aggregate design |
| `expected_inbound_deliveries` + `purchase_order_lines` | **Not redundant** — delivery schedule vs. commercial commitment |
| `audit_trail_records` + `inventory_movement_records` | **Not redundant** — governance snapshots vs. quantity operational log |
| `backorders` + `customer_order_lines.backordered_qty` | **Borderline** — header line qty is summary; `backorders` table adds acknowledgment workflow (BR-028). **Keep both** but API must define sync rules |
| `operational_alerts` + dashboard queries on source tables | **Acceptable** — alerts are derived notifications, not duplicate business state |

**No tables recommended for removal.**

---

## 3. Keys Review (SRS-DB-003)

### Strengths

- Universal surrogate PK (`id`) with business keys as UK — correct for scale and integration.
- Composite UK on `(product_id, location_id)` for stock positions and policies — enforces LDM-04.
- Document line UK `(parent_id, line_number)` on all line tables — prevents duplicate lines.
- Business document numbers (`po_number`, `order_number`, `gr_number`, etc.) consistently UK'd.

### Issues Identified

| ID | Severity | Finding |
|----|----------|---------|
| KEY-01 | **P2** | **`purchase_requisition_lines`** — no UK on `(requisition_id, product_id)` by design (amendments may duplicate SKU). API must prevent duplicate active lines or add partial UK. |
| KEY-02 | **P2** | **`fulfillment_executions`** — no UK on `(customer_order_id, fulfillment_location_id)` — multiple executions per order per location may be valid (split pick waves) but should be explicit in API. |
| KEY-03 | **P2** | **`inventory_reservations`** — no UK preventing duplicate ACTIVE reservations for same `order_line_id` + `stock_position_id`. Risk of double-reservation under retry. **Add partial UK or app idempotency.** |
| KEY-04 | **P3** | **`invoice_goods_receipt_match`** — no UK on `(supplier_invoice_id, goods_receipt_id)` pair — duplicate match rows possible. |
| KEY-05 | **P3** | **Role assignment** — no UK on `(user_account_id, role_name, effective_from)` — duplicate role rows possible. |

### Recommendations

1. Add **partial unique index** on `inventory_reservations (order_line_id, stock_position_id) WHERE reservation_status = 'ACTIVE'`.
2. Add UK on `invoice_goods_receipt_match (supplier_invoice_id, goods_receipt_id)`.
3. Document split fulfillment execution rules in API Design before enforcing UK.

---

## 4. Constraints Review (SRS-DB-004)

### Strengths

- ATP formula CHECK on `stock_positions` — `atp_qty = on_hand_qty - reserved_qty - quarantined_qty` (LDM-01, BR-001).
- SoD CHECK on `stock_adjustments` and `inventory_write_offs` — initiator ≠ approver when both set.
- Count variance XOR origin — `chk_count_variances_single_origin` (cycle OR physical, not both).
- Order line quantity balance — `fulfilled_qty + backordered_qty <= requested_qty`.
- Domain CHECK catalogs for status enums — consistent across modules.
- Appendix C honestly documents application-layer-only rules.

### Missing Constraints

| ID | Severity | Rule / Invariant | Recommendation |
|----|----------|------------------|----------------|
| CON-01 | **P1** | **BR-019 SoD: counter ≠ variance approver** — cross-table (`cycle_counts.counter_id` vs `count_variances.approver_id`) | Deferred constraint trigger or mandatory application check with DB test; document in API |
| CON-02 | **P1** | **BR-027 discontinued product** on PO/requisition/reservation line insert | `BEFORE INSERT` trigger joining `products.lifecycle_status` or API-only with integration test |
| CON-03 | **P1** | **BR-024 location freeze** — block mutations when `inventory_locations.is_frozen = TRUE` | Trigger on movement-affecting tables or single application guard — must be consistent |
| CON-04 | **P2** | **Lot quantity sum** — `SUM(lot_batches.quantity) = stock_positions.on_hand_qty` per position | Not DB-enforceable without materialized trigger; document as aggregate invariant |
| CON-05 | **P2** | **Reservation sum** — `SUM(active reservations) = reserved_qty` | Same — aggregate responsibility |
| CON-06 | **P2** | **Quarantine sum** — `SUM(active holds.held_qty) = quarantined_qty` | Same — aggregate responsibility |
| CON-07 | **P2** | **BR-029 promotional ring-fence** — reservation must not consume ring-fenced qty | Application/domain only — no DB constraint possible without promo columns on stock_positions |
| CON-08 | **P2** | **`put_aways.quantity` ≤ `goods_receipt_lines.accepted_qty`** | Add CHECK via trigger or defer to application |
| CON-09 | **P3** | **`stock_transfer_lines.received_qty` ≤ `dispatched_qty`** | Add CHECK |
| CON-10 | **P3** | **Valuation snapshot immutability** — no UPDATE after `reconciliation_status = 'RECONCILED'` | Trigger block per audit strategy |

### Incorrect / Inconsistent Relationships

| ID | Severity | Finding |
|----|----------|---------|
| REL-01 | **P2** | **`purchase_requisitions.triggering_alert_id` → `audit.operational_alerts`** — procurement schema FK to audit derived table creates **upstream dependency** from transactional to projection. Prefer `source_entity` reference on requisition or event correlation ID without FK. |
| REL-02 | **P2** | **`purchase_requisitions.purchase_order_id`** — FK set when converted but no CHECK that `approval_status = 'CONVERTED'` when PO linked. |
| REL-03 | **P3** | **`return_dispositions`** links to write-off, quarantine, and restock targets — mutually exclusive outcomes need CHECK (one of restock_location_id, quarantine_hold_id, write_off_id based on `disposition_decision`). |
| REL-04 | **P3** | **Audit strategy references `count_variances.initiated_by`** but PDM has `approver_id` only — SoD uses `cycle_counts.counter_id`. **Fix SRS-DB-006** documentation. |

---

## 5. Indexing Strategy Review (SRS-DB-005)

### Strengths

- Tiered prioritization (Critical / Operational / Reporting) matches business impact.
- Partial indexes for ACTIVE reservations, PENDING approvals, OPEN alerts — correct pattern.
- BRIN on movement/audit timestamps for time-range scans — appropriate at scale.
- Explicit "do NOT index" list prevents over-indexing.
- Duplicate reservation index resolved (single partial index).

### Performance Concerns

| ID | Severity | Concern | Recommendation |
|----|----------|---------|----------------|
| IDX-01 | **P1** | **`stock_positions` row-level lock contention** — hottest table; every reservation/ship updates same row | Short transactions; `SELECT … FOR UPDATE` discipline; consider advisory lock ordering by `id`; monitor `pg_locks` |
| IDX-02 | **P1** | **Partial UK on reservations not yet in indexing doc as DDL name** | Add `idx_reservations_order_line_position_partial_active` UK per KEY-03 |
| IDX-03 | **P2** | **`customer_orders` at 5M–10M rows/year** — only status+date index; API list by `customer_reference` unindexed | Add index when CRM integration confirmed (already noted as optional) |
| IDX-04 | **P2** | **Partition index propagation** — monthly partitions need automated index creation on new partitions | Document in migration runbook |
| IDX-05 | **P2** | **`audit_trail_records.before_state` JSONB** — no GIN; correct for now; add only if auditor search requires JSON containment |
| IDX-06 | **P3** | **Covering indexes** — ATP hot path may benefit from `INCLUDE (atp_qty, stock_status)` on `(product_id, location_id)` | Evaluate after load test |

### Missing Indexes (Add to SRS-DB-005)

| Table | Columns | Rationale |
|-------|---------|-----------|
| `inventory_reservations` | `(order_line_id, stock_position_id)` partial ACTIVE | Idempotent reservation (KEY-03) |
| `finance.invoice_goods_receipt_match` | `(supplier_invoice_id, goods_receipt_id)` UNIQUE | Prevent duplicate match rows |
| `platform.outbox_events` | `(published_at)` partial unpublished | Outbox dispatcher poll |

---

## 6. Audit Strategy Review (SRS-DB-006)

### Strengths

- Three-layer model (L1 row / L2 movement / L3 trail) is industry-appropriate.
- 7-year retention aligned with NFR-COM-020.
- SoD audit evidence requirements mapped to columns.
- Immutability enforcement via DB role — correct approach.
- Tiered hot/warm/cold architecture acknowledged.

### Issues

| ID | Severity | Finding |
|----|----------|---------|
| AUD-01 | **P2** | **L3 eventual consistency ≤ 5 seconds** for master data — API read-after-write on product update may return stale audit | API must document audit trail lag for master data mutations |
| AUD-02 | **P2** | **Tiered archive DDL not designed** — retention policy without `ATTACH/DETACH PARTITION` scripts | Add to migration phase 2 before production volume |
| AUD-03 | **P3** | **Doc inconsistency** — `count_variances.initiated_by` cited but column does not exist | Correct audit strategy to `cycle_counts.counter_id` vs `count_variances.approver_id` |

---

## 7. Data Dictionary Review (SRS-DB-007)

### Strengths

- All 58 PDM tables documented with 670 columns.
- Business meanings are BA-accessible.
- Related Entity column aids navigation.
- ER overview appendix supports onboarding.

### Issues

| ID | Severity | Finding |
|----|----------|---------|
| DD-01 | **P2** | **Table count header says 59** in index title history — corrected to 58; keep synchronized with PDM appendix |
| DD-02 | **P2** | **Missing platform/outbox/opening balance tables** — will need dictionary update when P1 tables added |
| DD-03 | **P3** | **Domain value enums** (status codes) in dictionary are in column text but not centralized | Consider Appendix D: Domain Value Catalog for API enum generation |

---

## 8. Naming Conventions Review (SRS-DB-008)

### Strengths

- Consistent `snake_case`, plural tables, singular columns.
- Constraint prefixes align with SRS-DB-003 and SRS-DB-004.
- Index naming with partial/BRIN suffixes — scalable.
- Identity over sequences for PKs — PostgreSQL best practice.
- View naming (`vw_`, `mvw_`) and schema placement rules clear.

### Issues

| ID | Severity | Finding |
|----|----------|---------|
| NAM-01 | **P3** | **`put_aways` pluralization** — grammatically awkward but consistent; document as approved exception |
| NAM-02 | **P3** | **Logical index IDs (IDX-NNN) vs physical `idx_` names** — mapping table in conventions is brief; add full mapping appendix when DDL generated |

**No naming convention changes required before API Design.**

---

## 9. Normalization Analysis

| Pattern | Assessment | Action |
|---------|------------|--------|
| Header / line document split (3NF) | **Correct** — all document aggregates normalized | None |
| `stock_positions` derived `atp_qty`, `stock_status` | **Controlled denormalization** — CHECK enforces ATP; status is cache | Keep; document refresh rules in API |
| `lot_batches.product_id` denormalized | **Acceptable** — FEFO query performance | Keep |
| `movement_records` denormalized `product_id`, `location_id` | **Acceptable** — partition pruning and history queries | Keep |
| `promotional_stock_allocations` without stock_position FK on header | **Partial normalization** — location detail in junction table only | Acceptable for campaign model |
| `backorders` separate from order lines | **2NF acceptable** — workflow attributes (acknowledgment) don't belong on line | Keep |
| Reference data in VARCHAR status codes vs. lookup tables | **Pragmatic** — enums via CHECK; no `status_types` table | Acceptable at current scale; API enums mirror CHECK values |

**No harmful normalization violations identified.** Denormalization is intentional and documented.

---

## 10. Scalability Analysis

### Current Capacity Design

| Component | Design | Risk at Scale |
|-----------|--------|---------------|
| Stock positions | ~100K–2M rows, row-level locking | **High contention** at peak order events |
| Movement records | 10M–100M+/year, monthly partitions | **Storage & query** without tiered archive |
| Audit trail | Proportional to mutations, 7-year retention | **~140 GB+** — hot PG unsustainable alone |
| Customer orders | 500K–10M/year | Manageable with archive |
| Outbox (missing) | Unbounded growth per ADR-006 | **Blocker** if not partitioned/archived |

### Scalability Risks

| ID | Severity | Risk | Mitigation |
|----|----------|------|------------|
| SCL-01 | **P1** | Single `stock_positions` row per product×location becomes **write hotspot** | Short TX; batch non-ATP reads to replicas; future: partition by location_id for read replicas |
| SCL-02 | **P1** | **7-year movement data on primary** | Implement ADR-026 tiered architecture before year-2 production volume |
| SCL-03 | **P2** | **No read replica strategy in DB docs** | M-13 Intelligence queries → read replica; writes → primary |
| SCL-04 | **P2** | **CQRS projection tables** beyond audit not defined | API dashboards may query transactional tables — violate AR-10; define read projections or views in `audit` schema |
| SCL-05 | **P2** | **Connection pool sizing** not addressed | Add to deployment guide — estimate from peak reservation TPS |
| SCL-06 | **P3** | **Multi-tenant** not in scope | If future SaaS, schema-per-tenant or `tenant_id` column needed — out of scope for v1 |

---

## 11. Cross-Artifact Consistency Matrix

| Topic | DB-001 | DB-002 | DB-003 | DB-004 | DB-005 | DB-006 | DB-007 | DB-008 | Status |
|-------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| Table count | 40 entities | 59 claimed / 58 defined | 59 refs | 59 refs | — | 59 refs | 58 | — | **Fix** |
| Shipment cardinality | 0..1 | 0..* implied | — | — | — | — | — | — | **Fix LDM** |
| Opening balance | Implied | Missing | Missing | Missing | — | — | Missing | — | **Add tables** |
| Outbox | — | Missing | Missing | Missing | — | Referenced | Missing | — | **Add table** |
| PostgreSQL version | — | 15+ | 15+ | 15+ | 15+ | 15+ | 15+ | 15+ | Align to 16 |
| SoD count variance | counter≠approver | counter_id / approver_id | FK documented | XOR origin | — | initiated_by **wrong** | Correct | — | **Fix DB-006** |
| BR-029 ring-fence | Modifies position | No column | — | App layer | Partial index | — | — | — | **API rule** |

---

## 12. Findings Summary

### By Severity

| Severity | Count | Must Resolve Before API |
|----------|-------|-------------------------|
| **P1 — Blocker** | 9 | Yes |
| **P2 — High** | 22 | First API sprint |
| **P3 — Medium** | 14 | DDL / Phase 2 |

### P1 Blockers (Must resolve)

| ID | Finding | Owner |
|----|---------|-------|
| PDM-02 | Add `platform.outbox_events` table | DBA + Backend |
| PDM-03 | Add opening balance certification tables | DBA + Domain |
| PDM-01 | Reconcile 58 vs 59 table count | DBA |
| CON-01 | Implement BR-019 cross-table SoD enforcement strategy | Backend + DBA |
| CON-02 | Implement BR-027 discontinued product gate | Backend + DBA |
| CON-03 | Implement BR-024 location freeze guard | Backend + DBA |
| IDX-01 | Document stock_positions locking strategy for API | DBA + Backend |
| KEY-03 | Partial UK on active reservations | DBA |
| SCL-02 | Tiered archive design for movement/audit (ADR-026) | DBA + DevOps |

---

## 13. Recommendations Before API Design

### 13.1 Immediate Actions (Pre-API Gate)

| # | Action | Rationale |
|---|--------|-----------|
| 1 | **Add `platform` schema** with `outbox_events` table design to SRS-DB-002 | API event publishing and transactional integrity depend on outbox |
| 2 | **Add opening balance tables** or formally defer go-live API with documented workaround | Location activation API cannot be specified without balance certification model |
| 3 | **Fix table count** across all SRS-DB documents (58 defined + platform tables) | Prevents migration and dictionary drift |
| 4 | **Add partial UK** on active reservations | API idempotency for `ConfirmOrder` / `ReserveStock` |
| 5 | **Publish Application Invariant Contract** — list CON-04 through CON-07 as aggregate rules API must enforce | DB cannot enforce all cross-row invariants |
| 6 | **Correct SRS-DB-006** count variance SoD column references | Audit API export accuracy |

### 13.2 API Design Guidance (Derived from DB Review)

| API Domain | DB Implication |
|------------|----------------|
| **ATP queries** | Read `stock_positions.atp_qty` — do not calculate in API; handle staleness via cache policy |
| **Order confirmation** | Idempotent on `order_number`; reservation uses partial UK |
| **Location activation** | Block until opening balance certified; check `is_frozen` |
| **Adjustments / write-offs** | Return 409 if initiator = approver; reason_code_id required |
| **Audit trail reads** | Query `audit` schema; allow ≤5s lag for L3 on master data |
| **Pagination** | Movement/audit history — cursor on `(movement_timestamp, id)` using partition key |
| **Enum values** | Mirror CHECK constraint value sets — generate from SRS-DB-004 domain catalog |
| **Cross-schema operations** | Single DB transaction per aggregate; saga for cross-module (outbox events) |

### 13.3 DDL Generation Sequence (Post-API Conceptual Lock)

```
Phase 1: Schemas + reference/master data tables
Phase 2: Transactional core (stock_positions, orders, receipts)
Phase 3: platform.outbox_events + constraints + indexes Tier 1
Phase 4: Audit tables + partitions
Phase 5: Indexes Tier 2–3 + views
Phase 6: Triggers (policy history, audit immutability, freeze guard)
```

### 13.4 Documents to Update

| Document | Update Required |
|----------|-----------------|
| SRS-DB-002 | Add platform + opening balance tables; fix appendix count |
| SRS-DB-003 | Keys for new tables; reservation partial UK |
| SRS-DB-004 | Constraints for new tables; return_disposition XOR |
| SRS-DB-005 | New indexes (reservation UK, outbox poll, match UK) |
| SRS-DB-006 | Fix count variance SoD column reference |
| SRS-DB-007 | New table entries |
| SRS-DB-001 | Shipment cardinality; opening balance entity |

---

## 14. Gate Decision

| Criterion | Met? |
|-----------|------|
| Logical model supports all MVP business rules | **Yes** — with opening balance gap |
| Physical model implementable in PostgreSQL | **Yes** |
| Keys and constraints enforce critical invariants | **Yes** — with documented app-layer rules |
| Index strategy supports ATP and operational SLAs | **Yes** |
| Audit meets compliance requirements | **Yes** — tiered storage execution pending |
| Naming conventions ready for DDL generation | **Yes** |
| Infrastructure tables (outbox) defined | **No** — P1 blocker |
| Go-live data path complete | **No** — P1 blocker |

### Decision: **CONDITIONAL GO**

API Design may proceed **in parallel** with P1 database amendments for:

- Domains not blocked: **Catalog, Network, Governance, Procurement (except go-live), Fulfillment (with reservation UK addendum), Transfer, Returns, Finance**
- Domains **blocked** until P1 resolved: **Location activation / opening balance APIs**, **Event publishing contract** (needs outbox schema)

---

## 15. Approval

| Role | Name | Signature | Date | Decision |
|------|------|-----------|------|----------|
| Chief Database Architect | | | | Conditional Go |
| Solution Architect | | | | |
| DDD Solution Architect | | | | |
| Development Lead | | | | |
| Product Owner | | | | |

---

*End of Database Design Review Report*

*Document ID: SRS-DB-009 | Version 1.0 | July 6, 2026*
