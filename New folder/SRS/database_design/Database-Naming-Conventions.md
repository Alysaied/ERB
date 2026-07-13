# Database Naming Conventions
## Inventory Management System — PostgreSQL

---

## Document Information

| Attribute | Detail |
|-----------|--------|
| **Document ID** | SRS-DB-008 |
| **Document Title** | Database Naming Conventions |
| **Version** | 1.0 |
| **Status** | Draft |
| **Document Owner** | Database Architect |
| **Source Documents** | SRS-DB-002 (PDM), SRS-DB-003 (Keys), SRS-DB-004 (Constraints), SRS-DB-005 (Indexing), SRS-DB-006 (Audit) |
| **Target Platform** | PostgreSQL 15+ |
| **Date** | July 6, 2026 |
| **Scope** | Naming standards for all database objects — no DDL/SQL statements |

### Purpose

This document defines **consistent, scalable naming conventions** for the Inventory Management System database. All new objects — tables, columns, keys, constraints, indexes, sequences, and views — must follow these standards. Conventions align with existing SRS-DB artifacts and PostgreSQL identifier limits (63 characters).

### Global Rules

| Rule | Standard |
|------|----------|
| **Case** | Lowercase only — `snake_case` for all identifiers |
| **Characters** | Letters, digits, underscores; start with a letter |
| **Length** | Target ≤ 40 characters; hard limit 63 (PostgreSQL) |
| **Reserved words** | Avoid PostgreSQL reserved words (`user`, `order`, `position`) — qualify with schema or use plural/descriptive names (`user_accounts`, `customer_orders`, `storage_positions`) |
| **Abbreviations** | Use only approved abbreviations (see Appendix A); prefer full words for clarity |
| **Pluralization** | **Tables:** plural nouns (`products`, `stock_positions`). **Columns:** singular attribute names (`product_id`, `order_date`) |
| **Language** | American English spelling in identifiers (`canceled` → use domain value `CANCELLED` in data, not in object names) |
| **Bounded context** | Schema name reflects domain module — not `dbo` or `public` for application tables |

---

## 1. Schemas

### 1.1 Naming Pattern

```
{bounded_context_noun}
```

| Rule | Detail |
|------|--------|
| Format | Single lowercase noun or compound noun — no prefix/suffix |
| Count | One schema per bounded context (14 schemas in IMS) |
| `public` | Reserved for extensions only — application tables do not use `public` |

### 1.2 Approved Schemas

| Schema | Purpose |
|--------|---------|
| `catalog` | Product master data |
| `network` | Locations and storage positions |
| `governance` | Policies and reason codes |
| `inventory` | Stock balances, lots, holds, policies |
| `procurement` | Suppliers, requisitions, purchase orders |
| `inbound` | Goods receipt, discrepancies, put-away |
| `finance` | Supplier invoices and three-way match |
| `fulfillment` | Customer orders, reservations, picks, shipments |
| `transfer` | Inter-location transfers |
| `accuracy` | Cycle counts, adjustments, write-offs |
| `returns` | RMA and customer returns |
| `commercial` | Promotional allocations |
| `identity` | Users and role assignments |
| `audit` | Movement log, audit trail, alerts, valuation |

### 1.3 Fully Qualified References

Always use **schema-qualified** names in documentation, migrations, and cross-schema FK definitions:

```
inventory.stock_positions
fulfillment.customer_orders
```

---

## 2. Tables

### 2.1 Naming Pattern

```
{entity_noun_plural}
```

or for associative / junction tables:

```
{parent_a}_{parent_b}          -- when relationship is the entity
{parent_entity}_{role_noun}      -- e.g. stock_policy_history, invoice_goods_receipt_match
```

| Rule | Detail |
|------|--------|
| Plural | Tables hold collections — `products`, not `product` |
| Prefix | No `tbl_`, `t_`, or module prefix — schema provides context |
| Suffix | Avoid `_table`; use `_history`, `_lines`, `_match` only when semantically required |
| Line tables | Parent name + `_lines` — `purchase_order_lines`, `goods_receipt_lines` |
| Header documents | Domain noun — `purchase_orders`, `goods_receipts`, `customer_orders` |
| Log / audit tables | `_records` suffix for append-only logs — `inventory_movement_records`, `audit_trail_records` |
| Max length | ≤ 40 characters recommended |

### 2.2 Examples

| Good | Bad | Reason |
|------|-----|--------|
| `stock_positions` | `StockPosition` | Must be snake_case lowercase |
| `inventory_reservations` | `inv_res` | No unapproved abbreviations |
| `invoice_goods_receipt_match` | `inv_gr_match_tbl` | No `tbl_` prefix; spell out |
| `user_accounts` | `users` | Avoid reserved word `user` |
| `put_aways` | `putaway` | Compound operations use underscore |

### 2.3 Table Partition Naming (High-Volume Tables)

```
{parent_table}_{partition_bound}
```

| Partition Type | Pattern | Example |
|----------------|---------|---------|
| Monthly range | `{table}_y{YYYY}m{MM}` | `inventory_movement_records_y2026m07` |
| Yearly archive | `{table}_y{YYYY}` | `customer_orders_y2023` |

Partition child tables inherit parent naming root. Partition key column: `movement_timestamp`, `event_timestamp`.

---

## 3. Columns

### 3.1 General Rules

| Rule | Detail |
|------|--------|
| Format | `snake_case`, singular attribute name |
| Boolean | Prefix `is_` or `has_` — `is_active`, `has_sod_conflict`, `pack_confirmed` |
| Timestamps | Suffix `_at` for point-in-time — `created_at`, `reserved_at`, `released_at` |
| Dates | Suffix `_date` for calendar date — `order_date`, `expiration_date` |
| Quantities | Suffix `_qty` — `on_hand_qty`, `reserved_qty`, `adjustment_qty` |
| Amounts | Suffix `_amount` or `_value` — `total_amount`, `financial_value`, `line_amount` |
| Status | Suffix `_status` — `order_status`, `approval_status`, `match_status` |
| Type / category | Suffix `_type` — `movement_type`, `hold_type`, `ownership_type` |
| Codes | Suffix `_code` — `reason_code`, `category_code`, `currency_code` |
| References | Suffix `_reference` or `_ref` — `movement_reference`, `approval_chain_ref` |
| Counts | Suffix `_count` — `total_variances` (exception: use `_number` for business document numbers) |

### 3.2 Standard Platform Columns

Apply consistently per table type (see SRS-DB-002):

| Column | Type | Tables | Meaning |
|--------|------|--------|---------|
| `id` | `BIGINT` | All | Surrogate primary key |
| `version` | `INTEGER` | Mutable transactional headers | Optimistic lock counter |
| `is_active` | `BOOLEAN` | Master / reference data | Soft-delete flag |
| `created_at` | `TIMESTAMPTZ` | Mutable tables | Row creation timestamp (UTC) |
| `updated_at` | `TIMESTAMPTZ` | Mutable tables with UPDATE | Last modification timestamp |
| `created_by` | `BIGINT` | Document headers | Creating user FK |
| `line_number` | `INTEGER` | Document line tables | Sequence within parent document |

### 3.3 Foreign Key Column Naming

```
{referenced_table_singular}_id
```

| Referenced Table | FK Column | Notes |
|------------------|-----------|-------|
| `products` | `product_id` | Singular entity + `_id` |
| `inventory_locations` | `location_id` | Drop redundant prefix when unambiguous in context |
| `stock_positions` | `stock_position_id` | Full entity name when abbreviation is ambiguous |
| `user_accounts` | `user_id` or role-specific — see below | |

**Role-specific user FKs** (when multiple users on one row):

| Column | Meaning |
|--------|---------|
| `created_by` | Record creator |
| `initiated_by` | Workflow initiator |
| `approved_by` | Approver |
| `authorized_by` | Formal authorizer |
| `performed_by` | Physical executor |
| `prepared_by` | Snapshot preparer |
| `counter_id` | Cycle count performer |
| `inspector_id` | Return inspector |
| `receiving_clerk_id` | Receipt operator |
| `assigned_picker_id` | Pick assignee |
| `approver_id` | Variance approver (when `approved_by` not used) |

Do **not** use `user_id` when a role-specific name is clearer.

### 3.4 Business Key Columns

Natural identifiers use domain terms — not `business_key` or `code` alone:

| Entity | Column |
|--------|--------|
| Product | `sku` |
| Location | `location_code` |
| Purchase order | `po_number` |
| Customer order | `order_number` |
| Goods receipt | `gr_number` |
| Shipment | `shipment_number` |
| RMA | `rma_number` |

### 3.5 Denormalized Columns

When FK target is duplicated for query performance, use same name as canonical FK:

```
product_id    -- denormalized on lot_batches, movement_records
location_id   -- denormalized on movement_records
```

Comment in data dictionary: "(denormalized)" — do not use `product_id_dup` or `product_id_fk2`.

### 3.6 Anti-Patterns

| Avoid | Use Instead |
|-------|-------------|
| `desc` | `description` |
| `amt` | `amount` |
| `qty1`, `qty2` | `qty_before`, `qty_after` |
| `status1` | `approval_status`, `order_status` |
| `data`, `info`, `misc` | Domain-specific name |
| Hungarian notation (`strName`, `iCount`) | `product_name`, `line_count` |

---

## 4. Primary Keys

### 4.1 Column Standard

| Attribute | Standard |
|-----------|----------|
| Column name | `id` — always, on every table |
| Data type | `BIGINT` |
| Generation | `GENERATED ALWAYS AS IDENTITY` (preferred over sequences) |
| Nullability | `NOT NULL` |
| Uniqueness | Single-column primary key only — no composite PKs |

### 4.2 Constraint Naming

```
pk_{table_name}
```

`{table_name}` is the table name **without schema prefix**.

| Table | PK Constraint Name |
|-------|-------------------|
| `catalog.products` | `pk_products` |
| `inventory.stock_positions` | `pk_stock_positions` |
| `audit.inventory_movement_records` | `pk_inventory_movement_records` |

### 4.3 Rationale

- Surrogate `id` is stable across business key changes (`sku` format evolution).
- Narrow `BIGINT` PK optimizes FK indexes and joins.
- Single-column PK simplifies ORM mapping and partition key design.
- Business uniqueness enforced via **unique constraints**, not composite PKs.

---

## 5. Foreign Keys

### 5.1 Column Standard

See §3.3. Every FK column references parent `id` unless documented otherwise.

### 5.2 Constraint Naming

```
fk_{child_table}_{parent_entity_or_role}
```

| Rule | Detail |
|------|--------|
| Prefix | `fk_` |
| Child | Child table name (without schema) |
| Parent | Parent table singular noun or role qualifier |
| Length | Truncate parent qualifier if > 63 chars — keep child table name intact |

### 5.3 Examples

| Child Table | Column | FK Constraint Name |
|-------------|--------|-------------------|
| `product_identifiers` | `product_id` | `fk_product_identifiers_product` |
| `stock_positions` | `product_id` | `fk_stock_positions_product` |
| `stock_positions` | `location_id` | `fk_stock_positions_location` |
| `products` | `created_by` | `fk_products_created_by` |
| `purchase_requisitions` | `triggering_alert_id` | `fk_purchase_requisitions_alert` |
| `audit_trail_records` | `movement_record_id` | `fk_audit_trail_movement` |

### 5.4 Self-Referencing FKs

```
fk_{table}_{relationship_role}
```

| Table | Column | Constraint Name |
|-------|--------|-----------------|
| `inventory_locations` | `parent_location_id` | `fk_inventory_locations_parent` |

### 5.5 Cross-Schema FKs

Permitted and named identically. Schema qualification appears in DDL target, not constraint name:

```
fk_goods_receipts_purchase_order   → procurement.purchase_orders(id)
fk_stock_adjustments_reason_code   → governance.reason_codes(id)
```

### 5.6 Index Requirement

PostgreSQL does **not** auto-index FK columns. Create supporting index per SRS-DB-005 when column appears in JOIN/WHERE. Index name follows §7 — not the FK constraint name.

---

## 6. Constraints

### 6.1 Naming Pattern

```
{type_prefix}_{table_name}_{column_or_scope}
```

### 6.2 Type Prefixes

| Constraint Type | Prefix | Example |
|-----------------|--------|---------|
| Primary key | `pk_` | `pk_products` |
| Foreign key | `fk_` | `fk_products_created_by` |
| Unique | `uk_` | `uk_products_sku` |
| Check | `chk_` | `chk_products_lifecycle_status` |
| Not null | `nn_` | `nn_products_sku` |
| Default | `def_` | `def_products_created_at` |

*Note: PostgreSQL merges NOT NULL and DEFAULT into column definitions — `nn_` and `def_` names are logical/documentation identifiers used in SRS-DB-004; use in migration comments or extended property metadata.*

### 6.3 Unique Constraint Naming

```
uk_{table}_{column}
uk_{table}_{col1}_{col2}        -- composite; omit redundant table prefix on columns
```

| Table | Column(s) | Constraint Name |
|-------|-----------|-----------------|
| `products` | `sku` | `uk_products_sku` |
| `stock_positions` | `(product_id, location_id)` | `uk_stock_positions_product_location` |
| `product_identifiers` | `(identifier_type, identifier_value)` | `uk_product_identifiers_type_value` |
| `supplier_invoices` | `(supplier_id, invoice_number)` | `uk_supplier_invoices_supplier_number` |
| `audit_trail_records` | `(audit_event_reference, event_timestamp)` | `uk_audit_trail_ref_ts` |

### 6.4 Check Constraint Naming

```
chk_{table}_{column_or_rule}
```

| Scope | Pattern | Example |
|-------|---------|---------|
| Single column domain | `chk_{table}_{column}` | `chk_products_lifecycle_status` |
| Cross-column rule | `chk_{table}_{rule_short_name}` | `chk_stock_positions_atp_formula` |
| Shared domain (reusable) | `chk_domain_{domain_name}` | `chk_domain_approval_status` |

**Shared domain checks** — when identical value sets apply across tables, use `chk_domain_*` prefix and document in SRS-DB-004 Appendix. Table-level checks may alias the same rule.

### 6.5 Composite Constraint Scope Abbreviations

When column list exceeds name length, use semantic scope:

| Scope Token | Meaning |
|-------------|---------|
| `product_location` | `(product_id, location_id)` |
| `type_value` | `(identifier_type, identifier_value)` |
| `ref_ts` | `(reference, timestamp)` partition uniqueness |
| `atp_formula` | `atp_qty = on_hand_qty - reserved_qty - quarantined_qty` |

---

## 7. Indexes

### 7.1 Naming Pattern

```
idx_{table}_{column_or_scope}[_{suffix}]
```

| Rule | Detail |
|------|--------|
| Prefix | `idx_` — distinguishes from unique constraints (`uk_`) |
| Table | Child table name without schema |
| Columns | Leading column names joined by underscore; omit `_id` suffix on single FK when clear |
| Suffix | Optional qualifier for special index types |

### 7.2 Index Type Suffixes

| Index Type | Suffix | Example |
|------------|--------|---------|
| B-tree (default) | *(none)* | `idx_reservations_stock_position` |
| Partial index | `_partial_{predicate_short}` | `idx_reservations_stock_position_partial_active` |
| BRIN | `_brin` | `idx_movement_records_brin` |
| GIN (JSONB) | `_gin` | `idx_audit_trail_before_state_gin` |
| DESC sort | `_desc` on column | `idx_movement_records_position_timestamp_desc` |

### 7.3 Examples

| Table | Index Columns | Index Name |
|-------|---------------|------------|
| `stock_positions` | `(location_id, stock_status)` partial LOW/OUT | `idx_stock_positions_location_status_partial_low` |
| `inventory_reservations` | `(stock_position_id)` WHERE ACTIVE | `idx_reservations_stock_position_partial_active` |
| `inventory_movement_records` | `(stock_position_id, movement_timestamp DESC)` | `idx_movement_records_position_timestamp_desc` |
| `inventory_movement_records` | `movement_timestamp` BRIN | `idx_movement_records_brin` |
| `goods_receipts` | `purchase_order_id` | `idx_goods_receipts_purchase_order` |
| `customer_orders` | `(order_status, order_date DESC)` | `idx_customer_orders_status_date_desc` |

### 7.4 Rules

| Rule | Detail |
|------|--------|
| UK/PK indexes | **Do not** create duplicate `idx_` when `uk_` or `pk_` already provides the index |
| FK indexes | Name after FK column, not FK constraint name |
| Max length | Abbreviate column scope tokens (§6.5) before truncating table name |
| Partitioned tables | Index on parent propagates to partitions — name on parent only |
| One partial per predicate | Do not create both full and partial index on same columns |

### 7.5 Strategy Document Cross-Reference

Logical index IDs in SRS-DB-005 (`IDX-001` – `IDX-052`) map to physical names during DDL generation:

```
IDX-004 → idx_reservations_stock_position_partial_active
IDX-005 → idx_lot_batches_position_expiration
```

---

## 8. Sequences

### 8.1 Preferred Approach — Identity Columns

IMS **does not use standalone sequences** for primary keys. All tables use:

```
id BIGINT GENERATED ALWAYS AS IDENTITY
```

Implicit sequence names are PostgreSQL-generated (`{table}_id_seq`) — **do not rename** unless required for replication tooling.

### 8.2 When Standalone Sequences Are Permitted

Use only for **business reference number generation** outside PK identity:

| Use Case | Example |
|----------|---------|
| Document number pools | PO number series per location |
| External-facing reference ranges | Movement reference batch |

### 8.3 Sequence Naming Pattern

```
seq_{purpose}_{scope}
```

| Rule | Detail |
|------|--------|
| Prefix | `seq_` |
| Purpose | Document or reference type |
| Scope | Optional location or year qualifier |

### 8.4 Examples

| Sequence Name | Purpose |
|---------------|---------|
| `seq_movement_reference` | Global movement reference counter |
| `seq_po_number_wh01` | PO numbers scoped to location WH-01 |
| `seq_audit_event_y2026` | Annual audit event reference partition |

### 8.5 Business Reference Column Naming

Generated business references use `_reference` or domain-specific `_number` — not the sequence name:

| Sequence | Populates Column |
|----------|------------------|
| `seq_movement_reference` | `movement_reference` |
| `seq_po_number_wh01` | `po_number` |

---

## 9. Views

### 9.1 Naming Pattern

```
vw_{purpose}_{entity_or_scope}
```

| Rule | Detail |
|------|--------|
| Prefix | `vw_` — distinguishes from tables |
| Purpose | `rpt_` segment optional for reporting — `vw_rpt_open_orders` |
| Materialized | Prefix `mvw_` — `mvw_dashboard_atp_summary` |
| No `v_` | Use `vw_` consistently (two-letter prefix improves readability) |

### 9.2 Schema Placement

| View Type | Schema | Example |
|-----------|--------|---------|
| Operational read models | Same schema as source or `audit` | `audit.vw_rpt_open_alerts` |
| Cross-domain reporting | `audit` (M-13 Intelligence) | `audit.vw_rpt_atp_by_location` |
| Auditor export (AUD-05) | `audit` | `audit.vw_export_audit_evidence` |
| Application convenience | Avoid — prefer explicit queries or ORM projections |

### 9.3 Examples

| View Name | Purpose |
|-----------|---------|
| `vw_rpt_stock_position_atp` | ATP summary with product and location names |
| `vw_rpt_open_purchase_orders` | Open PO dashboard |
| `vw_rpt_pending_approvals` | Cross-table approval queue |
| `vw_rpt_movement_history` | Movement log with denormalized product SKU |
| `mvw_rpt_low_stock_alerts` | Materialized low-stock dashboard (refreshed on schedule) |
| `vw_export_audit_trail` | Auditor evidence package source |

### 9.4 Column Naming in Views

| Rule | Detail |
|------|--------|
| Inherit | Use source column names unchanged when exposing base columns |
| Computed | `snake_case` descriptive — `days_until_expiry`, `is_below_reorder` |
| Alias prefix | Do not prefix with `vw_` — `vw_atp_qty` is wrong; use `atp_qty` |
| Consistency | Same business term as base table — `sku`, not `product_sku_code` |

### 9.5 View Object Comments

Every view must have a `COMMENT ON VIEW` describing purpose, refresh policy (if materialized), and source tables.

---

## 10. Additional Database Objects

### 10.1 Triggers

```
trg_{table}_{timing}_{event}_{purpose}
```

| Example | Event |
|---------|-------|
| `trg_stock_policies_after_update_history` | Append `stock_policy_history` on policy change |
| `trg_audit_trail_records_before_update_block` | Prevent UPDATE on audit tables |
| `trg_stock_positions_before_update_timestamp` | Maintain `updated_at` |

Timing: `before` / `after`. Event: `insert` / `update` / `delete`.

### 10.2 Functions and Procedures

```
fn_{verb}_{entity}          -- returns scalar or set
sp_{verb}_{entity}          -- procedure (side effects)
```

| Example | Purpose |
|---------|---------|
| `fn_calculate_atp` | ATP derivation |
| `sp_archive_movement_partition` | Partition detach and archive |

### 10.3 Database Roles

```
ims_{module}_{access_level}
```

| Example | Purpose |
|---------|---------|
| `ims_app_readwrite` | Application DML role |
| `ims_audit_writer` | INSERT-only on audit tables |
| `ims_reporting_read` | SELECT-only for BI |
| `ims_migration_admin` | DDL migration role |

### 10.4 Enum Types (If Used)

Prefer `VARCHAR(32)` + CHECK constraints in IMS. If native PostgreSQL enums are introduced:

```
{schema}.{domain}_enum
```

Example: `inventory.ownership_type_enum` — use only when value set is truly immutable.

---

## 11. Scalability Guidelines

### 11.1 Adding New Tables

1. Assign to correct **schema** (bounded context).
2. Use plural **table name** ≤ 40 characters.
3. Include `id BIGINT GENERATED ALWAYS AS IDENTITY` as PK.
4. Apply standard audit columns per table tier (SRS-DB-006).
5. Name constraints and indexes before first deployment — renaming in production is costly.

### 11.2 Adding New Columns

1. Follow suffix conventions (§3.1).
2. FK columns: `{entity}_id` referencing parent `id`.
3. Add `nn_`, `chk_`, `fk_` constraints with names per §6.
4. Add index per §7 if column is filtered or joined frequently.
5. Update SRS-DB-007 Data Dictionary.

### 11.3 Name Collision Resolution

| Situation | Resolution |
|-----------|------------|
| Same entity name in two schemas | Schema qualifies — `catalog.products` vs external `erp.products` (avoid — use `erp_product_id` FK column instead) |
| Long composite UK name | Abbreviate scope tokens (§6.5), not table name |
| Index name > 63 chars | Drop `_id` suffixes from column tokens first, then abbreviate scope |

### 11.4 Prohibited Practices

| Practice | Reason |
|----------|--------|
| Hungarian notation | Reduces readability for BAs and developers |
| Single-letter column names | Not self-documenting |
| Duplicate indexes (UK + idx) | Wastes write performance and storage |
| Renaming `id` to `{table}_id` on PK | Breaks ORM and convention consistency |
| Mixed case identifiers | PostgreSQL folds unquoted identifiers to lowercase — use snake_case explicitly |
| Quotes in identifiers | Requires quoted SQL everywhere — avoid |

---

## Appendix A: Approved Abbreviations

Use only when necessary for length or established domain usage:

| Abbreviation | Full Term | Context |
|--------------|-----------|---------|
| `qty` | quantity | Column suffix |
| `po` | purchase order | `po_number`, `po_status` |
| `gr` | goods receipt | `gr_number` |
| `rma` | return merchandise authorization | `rma_number` |
| `atp` | available to promise | `atp_qty` |
| `mrsl` | minimum remaining shelf life | `mrsl_days` |
| `fefo` | first expired first out | Domain values, not object names |
| `fifo` | first in first out | Domain values |
| `sod` | segregation of duties | `sod_compliant`, `has_sod_conflict` |
| `ref` | reference | Suffix only — `approval_chain_ref` |
| `desc` | **Never** — use `description` | — |

---

## Appendix B: Quick Reference Card

| Object | Pattern | Example |
|--------|---------|---------|
| Schema | `{context}` | `inventory` |
| Table | `{entities_plural}` | `stock_positions` |
| Column | `{attribute}` / `{entity}_id` | `on_hand_qty`, `product_id` |
| Primary key | `id` / `pk_{table}` | `pk_stock_positions` |
| Foreign key | `fk_{child}_{parent}` | `fk_stock_positions_product` |
| Unique | `uk_{table}_{cols}` | `uk_products_sku` |
| Check | `chk_{table}_{col}` | `chk_products_lifecycle_status` |
| Index | `idx_{table}_{cols}` | `idx_goods_receipts_purchase_order` |
| Partial index | `idx_{table}_{cols}_partial_{pred}` | `idx_reservations_stock_position_partial_active` |
| Sequence | `seq_{purpose}` | `seq_movement_reference` |
| View | `vw_{purpose}_{entity}` | `vw_rpt_open_orders` |
| Materialized view | `mvw_{purpose}_{entity}` | `mvw_rpt_low_stock_alerts` |
| Partition | `{table}_y{YYYY}m{MM}` | `inventory_movement_records_y2026m07` |
| Trigger | `trg_{table}_{timing}_{event}_{purpose}` | `trg_audit_trail_records_before_update_block` |
| Role | `ims_{scope}_{access}` | `ims_audit_writer` |

---

## Appendix C: Cross-Document Alignment

| SRS Document | Naming Content |
|--------------|----------------|
| SRS-DB-002 (PDM) | Table and column names — canonical examples |
| SRS-DB-003 (Keys) | `pk_`, `uk_`, `fk_` logical constraint names |
| SRS-DB-004 (Constraints) | `nn_`, `uk_`, `chk_`, `fk_`, `def_` prefixes |
| SRS-DB-005 (Indexing) | `idx_` patterns; IDX-NNN logical IDs |
| SRS-DB-006 (Audit) | Audit table and column standards |
| SRS-DB-007 (Data Dictionary) | Business meanings — updated when names change |
| SRS-DB-008 (this document) | Authoritative naming standard |

---

## Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Database Architect | | | |
| Database Performance Specialist | | | |
| Solution Architect | | | |
| Development Lead | | | |

---

*End of Database Naming Conventions*

*Document ID: SRS-DB-008 | Version 1.0 | July 6, 2026*
