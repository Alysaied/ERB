# Database Audit Strategy
## Inventory Management System — PostgreSQL

---

## Document Information

| Attribute | Detail |
|-----------|--------|
| **Document ID** | SRS-DB-006 |
| **Document Title** | Database Audit Strategy |
| **Version** | 1.0 |
| **Status** | Draft |
| **Document Owner** | Database Architect |
| **Source Documents** | SRS-DB-002 (Physical Data Model), SRS-DB-004 (Database Constraints), SRS-DM-006 (Domain Events), SRS-BR-001 (Business Rules), ADR-024 (Centralized Audit Trail Projection), Cross-Cutting Concerns §7 |
| **Target Platform** | PostgreSQL 15+ |
| **Date** | July 6, 2026 |
| **Scope** | Audit design, field standards, table classification, event catalog, retention — no DDL/SQL statements |

### Purpose

This document defines the **database audit strategy** for the Inventory Management System. Auditing supports **traceability** (who changed what, when, where, and why) and **compliance** (COSO internal control, financial record alignment, lot recall, segregation of duties). The strategy avoids audit sprawl: not every table receives the same treatment — audit depth matches business materiality.

---

## Part 1: Audit Architecture Overview

### 1.1 Three-Layer Audit Model

| Layer | Mechanism | Purpose | Immutability |
|-------|-----------|---------|--------------|
| **L1 — Row attribution** | Standard and entity-specific columns on transactional tables | Current-state accountability; lightweight trace on every mutable row | Mutable table rows can UPDATE; attribution columns capture last actor where applicable |
| **L2 — Movement log** | `audit.inventory_movement_records` | Append-only record of **every stock quantity change** with before/after quantities | **Append-only** — no UPDATE/DELETE |
| **L3 — Governance trail** | `audit.audit_trail_records` | Before/after snapshots for **material** entity and policy changes | **Append-only** — no UPDATE/DELETE |

**Supporting projections (not primary audit evidence):**

| Artifact | Table | Role |
|----------|-------|------|
| Threshold history | `inventory.stock_policy_history` | Dedicated history for replenishment policy changes |
| Operational alerts | `audit.operational_alerts` | Derived notifications — trace to source entity, not standalone evidence |
| Financial snapshots | `audit.inventory_valuation_snapshots` + `inventory_valuation_lines` | Point-in-time valuation evidence for reconciliation (BP-30) |

### 1.2 Architectural Rules (from ADR-024, AUD-01–AUD-05)

| Rule | Requirement |
|------|-------------|
| **AUD-01** | Audit store records are append-only — application role has INSERT only on L2/L3 tables |
| **AUD-02** | Governance trail retained ≥ 7 years (NFR-COM-019, NFR-COM-020) |
| **AUD-03** | Single authoritative audit projection — no per-module duplicate audit tables |
| **AUD-04** | Domain events are the primary audit source; database audit tables are the persistence projection |
| **AUD-05** | Auditor evidence export within 15 minutes (NFR-PERF-026, NFR-COM-012) |

### 1.3 What Auditing Is Not

| Not audit | Instead |
|-----------|---------|
| Application debug logs | Operational logging (NFR-LOG) — diagnostic, shorter retention |
| `updated_at` alone | Insufficient for compliance — no actor, no before state, no reason |
| Duplicating movement + trail for every SELECT | Read operations are authorized via security logs, not business audit trail |
| Indexing JSONB audit fields for ad-hoc search | Structured query dimensions (`affected_entity_type`, `user_id`, `event_timestamp`) |

---

## Part 2: Standard Audit Fields

### 2.1 Platform-Wide Columns (L1)

Applied per SRS-DB-002 conventions on **mutable** tables.

| Field | Data Type | Tables | Business Purpose |
|-------|-----------|--------|------------------|
| `created_at` | `TIMESTAMPTZ` NOT NULL DEFAULT NOW() | All mutable tables | When the record was first persisted (UTC) |
| `updated_at` | `TIMESTAMPTZ` NOT NULL DEFAULT NOW() | Mutable tables with UPDATE lifecycle | Last modification timestamp — maintained by application/trigger |
| `version` | `INTEGER` NOT NULL DEFAULT 1 | Transactional headers with concurrent updates | Optimistic locking — detects lost updates; audit-relevant as conflict signal |

### 2.2 Attribution Columns (L1 — actor tracking)

| Field | Data Type | When Required | Business Purpose |
|-------|-----------|---------------|------------------|
| `created_by` | `BIGINT` FK → `identity.user_accounts` | Document creation (requisitions, receipts, orders) | Who initiated the business document |
| `initiated_by` | `BIGINT` FK | Adjustments, write-offs, count workflows | Who started a correction requiring approval |
| `approved_by` | `BIGINT` FK | Any approval-gated action (BR-019, BR-021, BR-023) | Who authorized — **SoD verification** (must ≠ initiator/counter) |
| `authorized_by` | `BIGINT` FK | Quarantine release, write-off authorization | Formal authorization for irreversible or high-risk actions |
| `performed_by` | `BIGINT` FK | Put-away, movement source events | Who executed the physical operation |
| `prepared_by` | `BIGINT` FK | Valuation snapshots | Who certified the financial snapshot |

### 2.3 Workflow and Context Columns (L1 — traceability enrichment)

| Field | Data Type | Tables | Business Purpose |
|-------|-----------|--------|------------------|
| `reason_code_id` | `BIGINT` FK → `governance.reason_codes` | Adjustments, write-offs, some movements | **Why** the change occurred (BR-020) |
| `adjustment_reference` / `*_reference` | `VARCHAR(64)` | Headers across domains | Human-readable business key for external audit correspondence |
| `qty_before` / `qty_after` | `NUMERIC(18,4)` | Adjustments, movement records | Quantity state transition evidence |
| `approval_status` | `VARCHAR(32)` | Gated documents | Workflow state at time of audit |
| `approval_chain_ref` | `VARCHAR(128)` | Audit trail records | Link to workflow engine instance |
| `evidence_reference` | `VARCHAR(128)` | Write-offs, variances | External evidence (photo, inspector report) |

### 2.4 L2 Movement Record Fields

Every stock mutation produces one row in `audit.inventory_movement_records`:

| Field | Purpose |
|-------|---------|
| `movement_reference` | Correlates to source document line or transaction ID |
| `movement_type` | RECEIPT, SHIPMENT, TRANSFER, ADJUSTMENT, WRITE_OFF, RESERVATION, RETURN, PUT_AWAY |
| `stock_position_id`, `product_id`, `location_id` | **Where** and **what** changed (denormalized for query performance) |
| `quantity_change`, `qty_before`, `qty_after` | **What** changed numerically |
| `lot_batch_id` | Lot traceability (BR-017) |
| `reason_code_id` | **Why** for adjustments and write-offs |
| `source_document_type`, `source_document_id` | **Originating document** — receipt, shipment, adjustment, etc. |
| `performed_by` | **Who** executed |
| `movement_timestamp` | **When** (partition key) |

### 2.5 L3 Audit Trail Record Fields

Material non-movement or co-material changes produce rows in `audit.audit_trail_records`:

| Field | Purpose |
|-------|---------|
| `audit_event_reference` | Unique business event ID (correlates to domain event / outbox message) |
| `affected_entity_type` | Logical table or entity name (e.g. `stock_adjustments`, `products`) |
| `affected_entity_id` | PK of governed record |
| `action_performed` | CREATE, UPDATE, APPROVE, CANCEL |
| `user_id` | Actor |
| `role_at_action` | Role at time of action — supports SoD retrospective review |
| `before_state` / `after_state` | JSONB snapshots of changed attributes |
| `approval_chain_ref` | Workflow reference when approval involved |
| `movement_record_id` | Optional FK linking governance trail to L2 movement when both apply |
| `event_timestamp` | **When** (partition key) |

### 2.6 Recommended Application Audit Context (not stored on every row)

Passed from application layer to audit writer on each command — may be embedded in `before_state`/`after_state` or logged to security audit:

| Context Field | Purpose |
|---------------|---------|
| `correlation_id` | Traces one user action across multiple tables/events |
| `session_id` | Links to authentication session |
| `client_ip` / `user_agent` | Security investigation (security log primary; optional in trail) |
| `location_scope` | Location context of the acting user |
| `command_name` | Application command that triggered the change |

---

## Part 3: Tables Requiring Auditing

Tables are classified by **audit tier**. Higher tiers require more layers.

### 3.1 Tier Definitions

| Tier | L1 Columns | L2 Movement | L3 Trail | Rationale |
|------|------------|-------------|----------|-----------|
| **T0 — Audit store** | N/A (is audit) | — | Self | Append-only audit tables |
| **T1 — Stock mutation** | Full attribution | **Required** on every qty change | **Required** on approval/status transitions | Financial and operational materiality |
| **T2 — Governance & master** | `created_at`/`updated_at` + actor on change | If qty affected | **Required** on CREATE/UPDATE/DEACTIVATE | Master data and policy integrity |
| **T3 — Transactional document** | Full attribution on header | Via lines/execution | On status transitions (submit, approve, cancel, ship) | Document lifecycle traceability |
| **T4 — Line / child** | `created_at` only | Via parent workflow | Only if line is approval point | Inherits header audit chain via FK |
| **T5 — Reference / junction** | `created_at` only | No | No — parent audited | Low independent materiality |
| **T6 — Derived / snapshot** | `created_at` + `prepared_by` where applicable | No | No — immutable snapshot IS the record | Point-in-time evidence |

### 3.2 Complete Table Classification (59 tables)

#### T0 — Audit Store (5 tables)

| Table | Audit Treatment |
|-------|-----------------|
| `audit.inventory_movement_records` | Append-only; DB role INSERT-only; monthly partition |
| `audit.audit_trail_records` | Append-only; DB role INSERT-only; monthly partition |
| `audit.operational_alerts` | Mutable status (ACKNOWLEDGED/RESOLVED); derived — not primary evidence |
| `audit.inventory_valuation_snapshots` | Immutable after publish; financial evidence |
| `audit.inventory_valuation_lines` | Immutable child of snapshot |

#### T1 — Stock Mutation (11 tables)

| Table | L1 Fields | L2 | L3 Events |
|-------|-----------|----|-----------|
| `inventory.stock_positions` | `created_at`, `updated_at`, `version`, `last_movement_at` | **Every** qty change | Status/ownership changes |
| `inventory.lot_batches` | `created_at`, `updated_at` | Qty changes per lot | Quality status, expiration corrections |
| `inventory.quarantine_holds` | `authorized_by`, hold/release timestamps | Hold apply/release qty | CREATE, RELEASE, DISPOSE |
| `fulfillment.inventory_reservations` | `created_at`, `updated_at` | Reserve/release/fulfill | Status transitions |
| `inbound.put_aways` | `performed_by` | ATP increase on completion | Completion event |
| `fulfillment.shipments` | `created_at`, `updated_at` | Ship qty deduction | Ship confirm, cancel |
| `transfer.stock_transfers` | `created_at`, `updated_at` | Transfer in/out | Status transitions |
| `transfer.in_transit_stock` | `created_at`, `updated_at` | In-transit qty tracking | Receive, loss, exception |
| `accuracy.stock_adjustments` | `initiated_by`, `approved_by`, `qty_before/after`, `reason_code_id` | On APPROVED | PENDING→APPROVED/REJECTED |
| `accuracy.inventory_write_offs` | `initiated_by`, `authorized_by`, `reason_code_id` | On authorization | CREATE, AUTHORIZE |
| `returns.return_dispositions` | `created_at`, `updated_at` | Restock/scrap qty | Disposition decision |

#### T2 — Governance & Master Data (11 tables)

| Table | L1 Fields | L3 Events |
|-------|-----------|-----------|
| `catalog.products` | `created_at`, `updated_at`, `created_by` | ProductRegistered, ProductStatusChanged, ABC classification |
| `catalog.product_identifiers` | `created_at`, `updated_at` | Identifier add/change (barcode integrity) |
| `network.inventory_locations` | `created_at`, `updated_at` | LocationActivated, LocationDeactivated |
| `network.storage_positions` | `created_at`, `updated_at` | StoragePositionConfigured |
| `governance.governance_policies` | `created_at`, `updated_at` | Policy threshold changes |
| `governance.reason_codes` | `created_at`, `updated_at` | Reason code add/deactivate |
| `procurement.suppliers` | `created_at`, `updated_at`, `is_active` | Supplier activation/deactivation |
| `inventory.stock_policies` | `created_at`, `updated_at` | Threshold create/update — also writes `stock_policy_history` |
| `inventory.stock_policy_history` | Dedicated history table | **Is** the audit artifact for policy changes |
| `identity.user_accounts` | `created_at`, `updated_at`, `account_status` | Account create, suspend, deactivate |
| `identity.role_assignments` | `created_at`, `updated_at`, `effective_from/to` | Role grant/revoke — **security-critical** |

#### T3 — Transactional Documents (16 tables)

| Table | L1 Fields | L3 Events |
|-------|-----------|-----------|
| `procurement.purchase_requisitions` | `created_by`, `approved_by`, `version` | Submit, approve, reject, convert |
| `procurement.purchase_orders` | `created_at`, `updated_at`, `version` | Place, amend, cancel, close |
| `inbound.goods_receipts` | `created_at`, `updated_at`, `version` | Receive, close, discrepancy |
| `inbound.receipt_discrepancies` | `created_at`, `updated_at` | Discrepancy resolution |
| `finance.supplier_invoices` | `created_at`, `updated_at` | Register, match, authorize payment |
| `finance.invoice_goods_receipt_match` | `created_at` | Three-way match outcome (BR-008) |
| `fulfillment.customer_orders` | `created_at`, `updated_at`, `version` | Confirm, cancel, complete |
| `fulfillment.fulfillment_executions` | `created_at`, `updated_at` | Pick start, complete, exception |
| `fulfillment.backorders` | `created_at`, `updated_at` | Backorder create, fulfill, cancel |
| `transfer.transfer_requests` | `created_at`, `updated_at`, `approved_by` | Request, approve, reject |
| `accuracy.cycle_counts` | `created_at`, `updated_at` | Schedule, start, complete |
| `accuracy.physical_inventory_counts` | `created_at`, `updated_at` | Count certification (BR-024 freeze) |
| `accuracy.count_variances` | `initiated_by`, `approved_by` | Variance identification, approval (BR-019) |
| `returns.return_authorizations` | `created_at`, `updated_at`, `version` | RMA issue, cancel, expire |
| `returns.customer_returns` | `created_at`, `updated_at` | Return receipt |
| `commercial.promotional_stock_allocations` | `created_at`, `updated_at` | Campaign allocation create/amend (BR-029) |

#### T4 — Line / Child Tables (15 tables)

Inherit audit chain from parent header via FK. L3 trail written at header level unless line is the approval point.

| Table | Parent | Line-Level L3 When |
|-------|--------|-------------------|
| `catalog.product_identifiers` | `products` | Barcode change (also T2) |
| `procurement.purchase_requisition_lines` | `purchase_requisitions` | — |
| `procurement.purchase_order_lines` | `purchase_orders` | — |
| `procurement.expected_inbound_deliveries` | — | Status changes |
| `procurement.expected_inbound_delivery_lines` | `expected_inbound_deliveries` | — |
| `inbound.goods_receipt_lines` | `goods_receipts` | Lot capture (BR-017) |
| `finance.supplier_invoice_lines` | `supplier_invoices` | — |
| `fulfillment.customer_order_lines` | `customer_orders` | — |
| `fulfillment.fulfillment_pick_lines` | `fulfillment_executions` | Pick confirmation |
| `fulfillment.shipment_lines` | `shipments` | — |
| `transfer.transfer_request_lines` | `transfer_requests` | — |
| `transfer.stock_transfer_lines` | `stock_transfers` | — |
| `returns.return_authorization_lines` | `return_authorizations` | — |
| `returns.customer_return_lines` | `customer_returns` | — |
| `commercial.promotional_allocation_locations` | `promotional_stock_allocations` | — |

#### T5 — Junction / Scope (1 table)

| Table | Treatment |
|-------|-----------|
| `identity.role_assignment_locations` | `created_at` only; scope changes audited via parent `role_assignments` L3 entry |

#### T6 — Derived Snapshots (2 tables — also in T0)

| Table | Treatment |
|-------|-----------|
| `audit.inventory_valuation_snapshots` | Immutable financial point-in-time; `prepared_by` required |
| `audit.inventory_valuation_lines` | Immutable detail; no UPDATE after snapshot publish |

### 3.3 Tables Explicitly NOT Requiring L3 Trail

| Table | Reason |
|-------|--------|
| `identity.role_assignment_locations` | Junction — parent role assignment carries audit |
| All T4 line tables (unless noted) | Parent document audit + movement log captures qty impact |
| `audit.operational_alerts` | Derived notification — auditors trace via `source_entity_type/id` to source |

---

## Part 4: Audit Tables

### 4.1 Primary Audit Tables

#### `audit.inventory_movement_records` — Operational Quantity Audit

| Aspect | Detail |
|--------|--------|
| **Purpose** | Immutable log of every stock quantity change |
| **Populated by** | Domain event handlers after successful stock mutation commit |
| **Cardinality** | 1+ per stock mutation; links to source document |
| **Growth** | Very high (10M–100M+/year) |
| **Partitioning** | Monthly range on `movement_timestamp` |
| **Permissions** | Application role: INSERT only |
| **Linked from** | `audit.audit_trail_records.movement_record_id` when co-material |

#### `audit.audit_trail_records` — Governance Compliance Audit

| Aspect | Detail |
|--------|--------|
| **Purpose** | Before/after snapshots for material entity and policy changes |
| **Populated by** | M-13 Intelligence projection from domain events + command audit context |
| **Cardinality** | 0–1 per material command; may pair with movement record |
| **Growth** | Very high (proportional to governed mutations) |
| **Partitioning** | Monthly range on `event_timestamp` |
| **Permissions** | Application role: INSERT only |
| **JSONB scope** | Changed attributes only — not full row dump unless material |

#### `inventory.stock_policy_history` — Dedicated Policy History

| Aspect | Detail |
|--------|--------|
| **Purpose** | Threshold change history without polluting operational stock tables |
| **Populated by** | Trigger or application on `stock_policies` UPDATE |
| **Retention** | Align with governance trail (7 years) |

### 4.2 Supporting Audit Artifacts

| Table | Audit Role | Retention |
|-------|------------|-----------|
| `audit.operational_alerts` | Exception and threshold **notification** trail | Purge resolved > 90 days |
| `audit.inventory_valuation_snapshots` | Financial reconciliation evidence (BP-30) | 7 years |
| `audit.inventory_valuation_lines` | Snapshot detail | 7 years (with parent) |

### 4.3 Audit Write Flow

```text
User Command
    │
    ├─► [Application] Enrich AuditContext (user, role, correlation, reason)
    │
    ├─► [Domain] Mutate aggregate + raise domain event
    │
    ├─► [DB Transaction] UPDATE transactional table (L1 columns)
    │                      INSERT movement record (L2) if qty changed
    │
    └─► [Post-commit Handler] INSERT audit_trail_record (L3) from event payload
```

**Rule:** L2 and L3 writes occur in the **same database transaction** as the stock mutation when possible. L3 from async projection is acceptable only for non-qty master data changes with eventual consistency ≤ 5 seconds.

### 4.4 Before/After Snapshot Guidelines (JSONB)

| Entity Type | Include in `before_state` / `after_state` |
|-------------|---------------------------------------------|
| `stock_positions` | `on_hand_qty`, `reserved_qty`, `quarantined_qty`, `atp_qty`, `stock_status`, `ownership_type` |
| `stock_adjustments` | `adjustment_qty`, `approval_status`, `reason_code_id`, `initiated_by`, `approved_by` |
| `products` | `sku`, `product_status`, `abc_classification`, `is_traceable`, `unit_of_measure` |
| `inventory_locations` | `location_code`, `operational_status`, `location_type` |
| `role_assignments` | `role_name`, `assignment_status`, `effective_from`, `effective_to`, `sod_compliant` |
| `supplier_invoices` | `invoice_status`, `match_status`, `total_amount`, `authorization_status` |
| `governance_policies` | Policy type, threshold values, effective dates |

**Exclude:** Large TEXT blobs, redundant denormalized fields already on movement record, PII beyond `user_id` reference.

---

## Part 5: Business Events to Audit

Events map to domain events (SRS-DM-006). Each **material** event produces at minimum L1 update; stock events also produce L2; governance events produce L3.

### 5.1 Stock & Balance Events (L2 + L3)

| Event ID | Domain Event | Source Table(s) | Movement Type | L3 Action |
|----------|--------------|-----------------|---------------|-----------|
| AE-001 | StockIncreased (receipt) | `goods_receipts`, `put_aways`, `stock_positions` | RECEIPT / PUT_AWAY | APPROVE on put-away complete |
| AE-002 | StockReserved | `inventory_reservations`, `stock_positions` | RESERVATION | UPDATE |
| AE-003 | ReservationReleased | `inventory_reservations` | RESERVATION (negative) | UPDATE |
| AE-004 | StockShipped | `shipments`, `shipment_lines` | SHIPMENT | APPROVE |
| AE-005 | StockTransferred | `stock_transfers`, `in_transit_stock` | TRANSFER | UPDATE |
| AE-006 | TransferReceived | `stock_transfers`, `in_transit_stock` | TRANSFER | APPROVE |
| AE-007 | StockAdjusted | `stock_adjustments` | ADJUSTMENT | APPROVE |
| AE-008 | StockWrittenOff | `inventory_write_offs` | WRITE_OFF | APPROVE |
| AE-009 | StockQuarantined | `quarantine_holds` | ADJUSTMENT (quarantine bucket) | CREATE |
| AE-010 | QuarantineReleased | `quarantine_holds` | ADJUSTMENT | UPDATE |
| AE-011 | ReturnRestocked | `return_dispositions`, `customer_returns` | RETURN | APPROVE |
| AE-012 | LotQuantityChanged | `lot_batches` | Per parent movement | UPDATE if lot attrs change |

### 5.2 Inbound & Procurement Events (L3; L2 on receipt)

| Event ID | Domain Event | Source Table(s) | L3 Action |
|----------|--------------|-----------------|-----------|
| AE-020 | PurchaseRequisitionSubmitted | `purchase_requisitions` | UPDATE |
| AE-021 | PurchaseRequisitionApproved | `purchase_requisitions` | APPROVE |
| AE-022 | PurchaseOrderPlaced | `purchase_orders` | CREATE |
| AE-023 | PurchaseOrderCancelled | `purchase_orders` | CANCEL |
| AE-024 | GoodsReceived | `goods_receipts` | CREATE |
| AE-025 | ReceiptDiscrepancyIdentified | `receipt_discrepancies` | CREATE |
| AE-026 | PutAwayCompleted | `put_aways` | APPROVE |

### 5.3 Fulfillment Events (L2 + L3)

| Event ID | Domain Event | Source Table(s) | L3 Action |
|----------|--------------|-----------------|-----------|
| AE-030 | CustomerOrderConfirmed | `customer_orders` | UPDATE |
| AE-031 | CustomerOrderCancelled | `customer_orders` | CANCEL |
| AE-032 | FulfillmentStarted | `fulfillment_executions` | UPDATE |
| AE-033 | PickConfirmed | `fulfillment_pick_lines` | UPDATE |
| AE-034 | ShipmentDispatched | `shipments` | APPROVE |
| AE-035 | BackorderCreated | `backorders` | CREATE |

### 5.4 Inventory Control Events (L2 + L3 — SoD critical)

| Event ID | Domain Event | Source Table(s) | L3 Action | Compliance Note |
|----------|--------------|-----------------|-----------|-----------------|
| AE-040 | CycleCountStarted | `cycle_counts` | UPDATE | — |
| AE-041 | PhysicalInventoryCountCertified | `physical_inventory_counts` | APPROVE | BR-024 freeze evidence |
| AE-042 | CountVarianceIdentified | `count_variances` | CREATE | Counter recorded |
| AE-043 | CountVarianceApproved | `count_variances` | APPROVE | **Approver ≠ counter** (BR-019) |
| AE-044 | AdjustmentApproved | `stock_adjustments` | APPROVE | **Approver ≠ initiator** (BR-021) |
| AE-045 | WriteOffAuthorized | `inventory_write_offs` | APPROVE | Dual authorization (BR-023) |

### 5.5 Financial & Governance Events (L3)

| Event ID | Domain Event | Source Table(s) | L3 Action | Compliance Note |
|----------|--------------|-----------------|-----------|-----------------|
| AE-050 | ThreeWayMatchCompleted | `invoice_goods_receipt_match` | APPROVE | BR-008 payment gate |
| AE-051 | InvoicePaymentAuthorized | `supplier_invoices` | APPROVE | Financial control |
| AE-052 | GovernancePolicyChanged | `governance_policies` | UPDATE | Threshold audit |
| AE-053 | ReasonCodeDeactivated | `reason_codes` | UPDATE | Prevents orphan reasons |
| AE-054 | ValuationSnapshotPublished | `inventory_valuation_snapshots` | CREATE | BP-30 reconciliation |

### 5.6 Master Data & Security Events (L3)

| Event ID | Domain Event | Source Table(s) | L3 Action | Compliance Note |
|----------|--------------|-----------------|-----------|-----------------|
| AE-060 | ProductStatusChanged | `products` | UPDATE | BR-027 discontinued |
| AE-061 | InventoryLocationDeactivated | `inventory_locations` | UPDATE | Closure authorization |
| AE-062 | SupplierDeactivated | `suppliers` | UPDATE | Procurement block |
| AE-063 | RoleAssigned | `role_assignments` | CREATE | Access control |
| AE-064 | RoleRevoked | `role_assignments` | UPDATE | Access control |
| AE-065 | UserAccountDeactivated | `user_accounts` | UPDATE | Security |
| AE-066 | SoDViolationAttemptBlocked | — (security log + L3) | CREATE | BR-019, BR-021 |

### 5.7 Traceability-Specific Events (Lot Recall)

| Event ID | Domain Event | Tables | Audit Requirement |
|----------|--------------|--------|-------------------|
| AE-070 | LotCapturedAtReceipt | `goods_receipt_lines`, `lot_batches` | L2 with `lot_batch_id`; L3 on lot create |
| AE-071 | LotMovedWithTransfer | `stock_transfer_lines`, `lot_batches` | L2 must carry `lot_batch_id` |
| AE-072 | LotShippedToCustomer | `shipment_lines`, `lot_batches` | L2 for recall forward trace |
| AE-073 | LotRecalled | `quarantine_holds`, `lot_batches` | L3 + L2; `hold_type = RECALL` |

**Recall query pattern:** Forward trace from `lot_batches` → `inventory_movement_records` by `lot_batch_id`; backward from shipment to receipt via movement chain.

### 5.8 Events NOT Written to L3 Trail

| Event / Operation | Reason |
|-------------------|--------|
| Read-only queries (ATP lookup, dashboards) | Not a state change — security log only if required |
| Alert generation | Derived — source condition already audited |
| Cache invalidation | Infrastructure — not business audit |
| Failed validation (pre-commit) | No state change — operational log |
| Optimistic lock retry (success) | Only final successful commit audited |

---

## Part 6: Retention Policy Considerations

### 6.1 Retention Tiers

| Tier | Storage | Access Pattern | Technology |
|------|---------|----------------|------------|
| **Hot** | 0–24 months | Sub-second operational queries | PostgreSQL primary — partitioned |
| **Warm** | 25 months–7 years | Auditor search, compliance export | PostgreSQL archive schema or read replica |
| **Cold** | 7+ years (if mandated beyond) | Legal hold, rare retrieval | Object storage (Parquet/CSV), compressed |
| **Purge** | After retention expiry | None | Secure deletion per legal approval |

### 6.2 Table-Specific Retention

| Table / Data Class | Hot (online) | Total Retention | Purge Rule | Regulatory Driver |
|--------------------|--------------|-----------------|------------|-------------------|
| `audit.inventory_movement_records` | 24 months | **7 years** total | Archive partition to warm/cold; drop after 7 years | Financial records alignment (NFR-COM-020); lot traceability (BR-017) |
| `audit.audit_trail_records` | 24 months | **7 years** minimum | Tiered archive; legal hold overrides purge | COSO, external audit (BO-19, NFR-COM-010) |
| `inventory.stock_policy_history` | Full period | **7 years** | Archive with governance trail | Replenishment decision audit |
| `audit.inventory_valuation_snapshots` + lines | 36 months | **7 years** | Archive with finance records | Month-end close, BP-30 |
| Security audit events (login, SoD) | 24 months | **7 years** | Separate security log store | NFR-COM-020 |
| `audit.operational_alerts` | 90 days resolved | 90 days after RESOLVED | Scheduled purge job | Operational — not compliance primary |
| Transactional documents (closed PO, orders) | 36 months | 7 years | Archive closed documents | Commercial dispute resolution |
| `identity.user_accounts` (deactivated) | Active + 36 months | 7 years after deactivation | Pseudonymize PII per legal matrix | GDPR vs audit (C-05) — legal sign-off required |
| Operational application logs | 90 days | 1 year | Standard log rotation | NFR-LOG — not compliance audit |

### 6.3 Partitioning and Archival Mechanics

| Table | Partition Key | Archival Action |
|-------|---------------|-----------------|
| `inventory_movement_records` | `movement_timestamp` (monthly) | `DETACH PARTITION` → export to cold → `DROP` from hot after 24 months |
| `audit_trail_records` | `event_timestamp` (monthly) | Same; retain detached partitions in warm store until year 7 |
| Others | Not partitioned | Row-level archive job by `created_at` / status |

### 6.4 Legal Hold and Compliance Overrides

| Scenario | Action |
|----------|--------|
| Active litigation / regulatory investigation | Suspend purge for affected `lot_batch_id`, `product_id`, date range, or `user_id` |
| Recall event (AE-073) | Extend movement retention for affected lots — **no purge** until recall closed |
| GDPR erasure request (C-05) | Pseudonymize `user_accounts.display_name/email`; retain `user_id` in audit trail for compliance |
| External auditor export (AUD-05) | Hot+warm data exportable within 15 minutes — pre-built evidence package views |

### 6.5 Immutability Enforcement

| Control | Implementation |
|---------|----------------|
| Database permissions | `audit_writer` role: INSERT on L2/L3 only; no UPDATE/DELETE |
| Application | No ORM update paths to audit tables |
| Trigger guard (optional) | `BEFORE UPDATE OR DELETE` → RAISE EXCEPTION on audit tables |
| Monitoring | Alert on any DDL against `audit` schema |
| Hash chain (future) | Optional `record_hash` + `previous_hash` on L3 for tamper evidence — not in v1.0 |

### 6.6 Storage Growth Estimates (Planning)

| Table | Annual Rows (est.) | Row Size (est.) | 7-Year Storage (est.) |
|-------|-------------------|-----------------|----------------------|
| `inventory_movement_records` | 50M | ~500 bytes | ~175 GB + indexes |
| `audit_trail_records` | 10M | ~2 KB (JSONB) | ~140 GB + indexes |
| `operational_alerts` | 2M (rolling) | ~300 bytes | < 1 GB (purged) |

**Implication:** Hot PostgreSQL cannot hold 7 years of movement data at scale — **tiered architecture is mandatory** (ADR-026, Architecture Review G-05).

---

## Part 7: Segregation of Duties (SoD) Audit Requirements

| Business Rule | Audit Evidence Required | Tables |
|---------------|------------------------|--------|
| BR-019 | Counter ≠ variance approver | `count_variances.initiated_by` vs `approved_by` + L3 trail |
| BR-021 | Initiator ≠ adjustment approver | `stock_adjustments.initiated_by` vs `approved_by` + L3 trail |
| BR-023 | Write-off requires authorization | `inventory_write_offs.initiated_by` vs `authorized_by` |
| BR-008 | Three-way match before payment | `invoice_goods_receipt_match` + L3 APPROVE |
| Identity SoD | Role conflict blocked | `role_assignments.sod_compliant`, AE-066 on violation attempt |

**Auditor query pattern:** Join L3 `audit_trail_records` where `action_performed = 'APPROVE'` and compare `user_id` to `before_state.initiated_by`.

---

## Part 8: Implementation Checklist

| # | Task | Owner |
|---|------|-------|
| 1 | Apply L1 audit columns per table tier in migrations | DBA |
| 2 | Create `audit_writer` DB role with INSERT-only on L2/L3 | DBA |
| 3 | Implement movement record writer in stock mutation transaction | Backend |
| 4 | Implement audit trail projection handler (M-13) | Backend |
| 5 | Map domain events AE-001–AE-073 to audit writers | Backend |
| 6 | Configure monthly partitions on movement and trail tables | DBA |
| 7 | Build partition detach/archive job (hot → warm) | DevOps |
| 8 | Define legal hold flag and purge suspension | Legal + DBA |
| 9 | Privacy matrix for GDPR vs 7-year retention (G-09) | Legal |
| 10 | Auditor export views / evidence package (AUD-05) | Intelligence module |

---

## Part 9: Summary Matrix

| Audit Layer | Tables | Write Trigger | Retention |
|-------------|--------|---------------|-----------|
| L1 Row attribution | 54 mutable tables | Every INSERT/UPDATE | Life of row |
| L2 Movement log | Stock mutations (11 source tables) | Every qty change | 7 years (tiered) |
| L3 Governance trail | 35 material tables/events | Material commands | 7 years (tiered) |
| Policy history | `stock_policy_history` | Policy UPDATE | 7 years |
| Financial snapshot | Valuation tables | Period close | 7 years |
| Alerts (supporting) | `operational_alerts` | Threshold/exception | 90 days resolved |

---

## Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Database Architect | | | |
| Database Performance Specialist | | | |
| Internal Audit / Compliance | | | |
| Solution Architect | | | |

---

*End of Database Audit Strategy*

*Document ID: SRS-DB-006 | Version 1.0 | July 6, 2026*
