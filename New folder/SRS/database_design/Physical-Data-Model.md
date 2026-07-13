# Physical Data Model (PDM)
## Inventory Management System — PostgreSQL

---

## Document Information

| Attribute | Detail |
|-----------|--------|
| **Document ID** | SRS-DB-002 |
| **Document Title** | Physical Data Model — Inventory Management System |
| **Version** | 1.0 |
| **Status** | Draft |
| **Document Owner** | Database Architect |
| **Source Document** | SRS-DB-001 (Logical Data Model, v1.0) |
| **Target Platform** | PostgreSQL 15+ |
| **Date** | July 6, 2026 |
| **Scope** | Physical table design — no DDL/SQL statements |

### Purpose

This document converts the approved Logical Data Model (SRS-DB-001) into a **Physical Data Model** for PostgreSQL. It defines tables, columns, data types, nullability, defaults, and growth characteristics following PostgreSQL best practices.

### Physical Design Conventions

| Convention | Standard |
|------------|----------|
| **Naming** | `snake_case` for schemas, tables, and columns |
| **Primary keys** | `BIGINT` surrogate `id`, `GENERATED ALWAYS AS IDENTITY` |
| **Business keys** | Natural identifiers (`sku`, `location_code`, `order_number`) as `UNIQUE` alternate keys |
| **Quantities** | `NUMERIC(18,4)` — never `FLOAT`/`REAL` |
| **Monetary amounts** | `NUMERIC(18,2)` |
| **Timestamps** | `TIMESTAMPTZ` (UTC storage) |
| **Dates** | `DATE` for calendar dates without time |
| **Status / type codes** | `VARCHAR(32)` with application-enforced domain values |
| **Descriptions / notes** | `TEXT` |
| **Flexible snapshots** | `JSONB` for audit before/after state only |
| **Optimistic locking** | `version INTEGER NOT NULL DEFAULT 1` on mutable transactional headers |
| **Audit columns** | `created_at`, `updated_at` on all mutable tables; `created_by` where attribution required |
| **Soft delete** | `is_active BOOLEAN` on master data — no hard delete of reference rows |
| **Referential integrity** | Foreign keys within same bounded context; cross-context references by business key or loose FK with deferred validation |
| **High-volume tables** | Time-based range partitioning (monthly) on `movement_timestamp` / `event_timestamp` |
| **Indexing strategy** | B-tree on FKs and status filters; composite indexes on `(product_id, location_id)` hot paths |

### Schema Layout

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
| `accuracy` | Cycle counts, physical counts, adjustments, write-offs |
| `returns` | RMA, customer returns, dispositions |
| `commercial` | Promotional stock allocations |
| `identity` | Users and role assignments |
| `audit` | Movement log, audit trail, alerts, valuation snapshots |

### Growth Tier Legend

| Tier | Annual Row Estimate (mid-size deployment) | Strategy |
|------|-------------------------------------------|----------|
| **Low** | < 50K | Standard B-tree indexes |
| **Medium** | 50K – 5M | Composite indexes; archive closed documents > 3 years |
| **High** | 5M – 50M | Partitioning; read replicas for reporting |
| **Very High** | > 50M | Monthly partitions; cold storage archive; BRIN on timestamps |

---

## Domain 1: Catalog (`catalog` schema)

---

### Table: `catalog.products`

| Attribute | Detail |
|-----------|--------|
| **Business Purpose** | Canonical SKU master — identity for all inventory operations across locations and channels. |
| **Estimated Growth** | **Low** — ~10K–100K SKUs; stable with slow churn. |

| Column | Data Type | Nullable | Default | Description |
|--------|-----------|----------|---------|-------------|
| `id` | `BIGINT` | NO | IDENTITY | Surrogate primary key |
| `sku` | `VARCHAR(64)` | NO | — | Business key; stock keeping unit |
| `product_name` | `VARCHAR(256)` | NO | — | Display name |
| `description` | `TEXT` | YES | NULL | Extended description |
| `unit_of_measure` | `VARCHAR(16)` | NO | — | EA, CS, KG, etc. |
| `category_code` | `VARCHAR(64)` | YES | NULL | Product category reference |
| `lifecycle_status` | `VARCHAR(32)` | NO | `'ACTIVE'` | ACTIVE, INACTIVE, DISCONTINUED |
| `abc_classification` | `VARCHAR(1)` | YES | NULL | A, B, or C |
| `is_shelf_life` | `BOOLEAN` | NO | `FALSE` | Shelf-life product indicator |
| `is_traceable` | `BOOLEAN` | NO | `FALSE` | Lot/batch tracking required |
| `rotation_policy` | `VARCHAR(8)` | YES | NULL | FIFO or FEFO |
| `mrsl_days` | `INTEGER` | YES | NULL | Minimum remaining shelf life policy (days) |
| `superseded_by_sku` | `VARCHAR(64)` | YES | NULL | Replacement SKU if discontinued |
| `is_active` | `BOOLEAN` | NO | `TRUE` | Soft-delete flag |
| `version` | `INTEGER` | NO | `1` | Optimistic lock |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Record creation |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Last modification |
| `created_by` | `BIGINT` | YES | NULL | FK → `identity.user_accounts.id` |

---

### Table: `catalog.product_identifiers`

| Attribute | Detail |
|-----------|--------|
| **Business Purpose** | Alternate product identifiers (barcodes, vendor codes) for lookup at receipt and pick. |
| **Estimated Growth** | **Low** — ~1–3 identifiers per product. |

| Column | Data Type | Nullable | Default | Description |
|--------|-----------|----------|---------|-------------|
| `id` | `BIGINT` | NO | IDENTITY | Surrogate primary key |
| `product_id` | `BIGINT` | NO | — | FK → `catalog.products.id` |
| `identifier_type` | `VARCHAR(32)` | NO | — | BARCODE, VENDOR_CODE, GTIN, etc. |
| `identifier_value` | `VARCHAR(128)` | NO | — | Identifier string |
| `is_primary` | `BOOLEAN` | NO | `FALSE` | Primary scan identifier |
| `is_active` | `BOOLEAN` | NO | `TRUE` | Soft-delete flag |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Record creation |

---

## Domain 2: Network (`network` schema)

---

### Table: `network.inventory_locations`

| Attribute | Detail |
|-----------|--------|
| **Business Purpose** | Physical sites (warehouses, stores, DCs) anchoring all stock balances and operations. |
| **Estimated Growth** | **Low** — tens to low hundreds of locations. |

| Column | Data Type | Nullable | Default | Description |
|--------|-----------|----------|---------|-------------|
| `id` | `BIGINT` | NO | IDENTITY | Surrogate primary key |
| `location_code` | `VARCHAR(32)` | NO | — | Business key |
| `location_name` | `VARCHAR(256)` | NO | — | Display name |
| `location_type` | `VARCHAR(32)` | NO | — | WAREHOUSE, STORE, DISTRIBUTION_POINT |
| `parent_location_id` | `BIGINT` | YES | NULL | Self-FK for hierarchy |
| `operational_status` | `VARCHAR(32)` | NO | `'ACTIVE'` | ACTIVE, PLANNED, CLOSING, INACTIVE |
| `is_frozen` | `BOOLEAN` | NO | `FALSE` | Physical count freeze flag (BR-024) |
| `address_line1` | `VARCHAR(256)` | YES | NULL | Street address |
| `address_line2` | `VARCHAR(256)` | YES | NULL | Address continuation |
| `city` | `VARCHAR(128)` | YES | NULL | City |
| `region_code` | `VARCHAR(32)` | YES | NULL | State/province/region |
| `postal_code` | `VARCHAR(16)` | YES | NULL | Postal/ZIP code |
| `country_code` | `CHAR(2)` | YES | NULL | ISO 3166-1 alpha-2 |
| `responsible_manager_id` | `BIGINT` | YES | NULL | FK → `identity.user_accounts.id` |
| `go_live_date` | `DATE` | YES | NULL | Operational start date |
| `closure_plan` | `TEXT` | YES | NULL | Closure disposition plan |
| `is_active` | `BOOLEAN` | NO | `TRUE` | Soft-delete flag |
| `version` | `INTEGER` | NO | `1` | Optimistic lock |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Record creation |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Last modification |

---

### Table: `network.storage_positions`

| Attribute | Detail |
|-----------|--------|
| **Business Purpose** | Bin/zone/shelf addresses within a location for put-away and pick path. |
| **Estimated Growth** | **Low–Medium** — thousands per large warehouse. |

| Column | Data Type | Nullable | Default | Description |
|--------|-----------|----------|---------|-------------|
| `id` | `BIGINT` | NO | IDENTITY | Surrogate primary key |
| `location_id` | `BIGINT` | NO | — | FK → `network.inventory_locations.id` |
| `position_code` | `VARCHAR(64)` | NO | — | Unique within location |
| `zone` | `VARCHAR(32)` | YES | NULL | Zone designation |
| `aisle` | `VARCHAR(32)` | YES | NULL | Aisle designation |
| `bin` | `VARCHAR(32)` | YES | NULL | Bin designation |
| `storage_type` | `VARCHAR(32)` | NO | `'BULK'` | BULK, PICK_FACE, QUARANTINE, BONDED |
| `capacity_units` | `NUMERIC(18,4)` | YES | NULL | Optional capacity limit |
| `is_dedicated` | `BOOLEAN` | NO | `FALSE` | Product-dedicated position |
| `dedicated_product_id` | `BIGINT` | YES | NULL | FK → `catalog.products.id` |
| `is_active` | `BOOLEAN` | NO | `TRUE` | Soft-delete flag |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Record creation |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Last modification |

---

## Domain 3: Governance (`governance` schema)

---

### Table: `governance.governance_policies`

| Attribute | Detail |
|-----------|--------|
| **Business Purpose** | Organization-wide approval thresholds, tolerances, and exception rules. |
| **Estimated Growth** | **Low** — versioned policy set; < 1K active versions. |

| Column | Data Type | Nullable | Default | Description |
|--------|-----------|----------|---------|-------------|
| `id` | `BIGINT` | NO | IDENTITY | Surrogate primary key |
| `policy_code` | `VARCHAR(64)` | NO | — | Business identifier |
| `policy_name` | `VARCHAR(256)` | NO | — | Display name |
| `policy_type` | `VARCHAR(32)` | NO | — | APPROVAL_THRESHOLD, TOLERANCE, ACCESS, EXCEPTION |
| `threshold_value` | `NUMERIC(18,4)` | YES | NULL | Numeric threshold |
| `threshold_currency` | `CHAR(3)` | YES | NULL | ISO 4217 for financial thresholds |
| `applicable_scope` | `VARCHAR(64)` | YES | NULL | Location, role, or transaction scope |
| `approval_authority_role` | `VARCHAR(64)` | YES | NULL | Required approver role |
| `effective_from` | `TIMESTAMPTZ` | NO | — | Policy effective start |
| `effective_to` | `TIMESTAMPTZ` | YES | NULL | Policy effective end (NULL = open) |
| `is_active` | `BOOLEAN` | NO | `TRUE` | Soft-delete flag |
| `version` | `INTEGER` | NO | `1` | Optimistic lock |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Record creation |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Last modification |

---

### Table: `governance.reason_codes`

| Attribute | Detail |
|-----------|--------|
| **Business Purpose** | Standardized categorized explanations for adjustments, write-offs, and discrepancies. |
| **Estimated Growth** | **Low** — ~50–200 codes. |

| Column | Data Type | Nullable | Default | Description |
|--------|-----------|----------|---------|-------------|
| `id` | `BIGINT` | NO | IDENTITY | Surrogate primary key |
| `reason_code` | `VARCHAR(32)` | NO | — | Business key |
| `description` | `VARCHAR(512)` | NO | — | Human-readable label |
| `category` | `VARCHAR(32)` | NO | — | ADJUSTMENT, SHRINKAGE, DAMAGE, OBSOLESCENCE, RECEIPT_DISCREPANCY, RETURN, OTHER |
| `reporting_group` | `VARCHAR(64)` | YES | NULL | Reporting rollup group |
| `approval_threshold_id` | `BIGINT` | YES | NULL | FK → `governance.governance_policies.id` |
| `is_active` | `BOOLEAN` | NO | `TRUE` | Retired codes set FALSE |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Record creation |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Last modification |

---

## Domain 4: Inventory Balance (`inventory` schema)

---

### Table: `inventory.stock_positions`

| Attribute | Detail |
|-----------|--------|
| **Business Purpose** | Authoritative on-hand, reserved, and ATP quantities per product per location — central quantity hub. |
| **Estimated Growth** | **Medium** — product × location combinations; ~100K–2M rows. Hot contention table. |

| Column | Data Type | Nullable | Default | Description |
|--------|-----------|----------|---------|-------------|
| `id` | `BIGINT` | NO | IDENTITY | Surrogate primary key |
| `product_id` | `BIGINT` | NO | — | FK → `catalog.products.id` |
| `location_id` | `BIGINT` | NO | — | FK → `network.inventory_locations.id` |
| `on_hand_qty` | `NUMERIC(18,4)` | NO | `0` | Physical on-hand quantity |
| `reserved_qty` | `NUMERIC(18,4)` | NO | `0` | Committed to orders |
| `quarantined_qty` | `NUMERIC(18,4)` | NO | `0` | Held / non-sellable quantity |
| `atp_qty` | `NUMERIC(18,4)` | NO | `0` | Available-to-promise (derived: on_hand − reserved − quarantined) |
| `inbound_expected_qty` | `NUMERIC(18,4)` | NO | `0` | Informational pipeline quantity |
| `stock_status` | `VARCHAR(32)` | NO | `'IN_STOCK'` | IN_STOCK, LOW_STOCK, OUT_OF_STOCK, OVERSTOCK |
| `ownership_type` | `VARCHAR(32)` | NO | `'OWNED'` | OWNED, CONSIGNMENT, BONDED |
| `last_movement_at` | `TIMESTAMPTZ` | YES | NULL | Last quantity change timestamp |
| `version` | `INTEGER` | NO | `1` | Optimistic lock — critical for concurrent reservations |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Record creation |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Last modification |

---

### Table: `inventory.lot_batches`

| Attribute | Detail |
|-----------|--------|
| **Business Purpose** | Traceable lot/batch identity with shelf-life attributes for FEFO and recall. |
| **Estimated Growth** | **Medium–High** — new lot per receipt batch; 500K–10M rows over time. |

| Column | Data Type | Nullable | Default | Description |
|--------|-----------|----------|---------|-------------|
| `id` | `BIGINT` | NO | IDENTITY | Surrogate primary key |
| `stock_position_id` | `BIGINT` | NO | — | FK → `inventory.stock_positions.id` |
| `product_id` | `BIGINT` | NO | — | FK → `catalog.products.id` (denormalized for query) |
| `lot_number` | `VARCHAR(64)` | NO | — | Lot/batch business identifier |
| `quantity` | `NUMERIC(18,4)` | NO | `0` | Quantity in this lot at position |
| `expiration_date` | `DATE` | YES | NULL | Product expiration |
| `manufacture_date` | `DATE` | YES | NULL | Manufacture date |
| `receipt_date` | `DATE` | YES | NULL | First receipt date |
| `quality_status` | `VARCHAR(32)` | NO | `'ACCEPTED'` | ACCEPTED, HOLD, REJECTED |
| `supplier_id` | `BIGINT` | YES | NULL | FK → `procurement.suppliers.id` |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Record creation |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Last modification |

---

### Table: `inventory.quarantine_holds`

| Attribute | Detail |
|-----------|--------|
| **Business Purpose** | Holds removing quantity from ATP for quality, regulatory, recall, or customs reasons. |
| **Estimated Growth** | **Medium** — active holds low; historical ~100K–1M. |

| Column | Data Type | Nullable | Default | Description |
|--------|-----------|----------|---------|-------------|
| `id` | `BIGINT` | NO | IDENTITY | Surrogate primary key |
| `hold_reference` | `VARCHAR(64)` | NO | — | Business reference number |
| `stock_position_id` | `BIGINT` | NO | — | FK → `inventory.stock_positions.id` |
| `lot_batch_id` | `BIGINT` | YES | NULL | FK → `inventory.lot_batches.id` |
| `held_qty` | `NUMERIC(18,4)` | NO | — | Quantity under hold |
| `hold_type` | `VARCHAR(32)` | NO | — | QUALITY, REGULATORY, RECALL, CUSTOMS, INVESTIGATION |
| `hold_reason` | `TEXT` | NO | — | Hold justification |
| `hold_status` | `VARCHAR(32)` | NO | `'ACTIVE'` | ACTIVE, RELEASED, DISPOSED |
| `hold_start_at` | `TIMESTAMPTZ` | NO | `NOW()` | Hold effective start |
| `expected_resolution_at` | `TIMESTAMPTZ` | YES | NULL | Expected release date |
| `released_at` | `TIMESTAMPTZ` | YES | NULL | Actual release timestamp |
| `disposition_outcome` | `VARCHAR(32)` | YES | NULL | RESTOCK, WRITE_OFF, DESTROY |
| `authorized_by` | `BIGINT` | YES | NULL | FK → `identity.user_accounts.id` |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Record creation |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Last modification |

---

### Table: `inventory.stock_policies`

| Attribute | Detail |
|-----------|--------|
| **Business Purpose** | Replenishment thresholds per product per location. |
| **Estimated Growth** | **Medium** — mirrors stock position cardinality; ~100K–2M. |

| Column | Data Type | Nullable | Default | Description |
|--------|-----------|----------|---------|-------------|
| `id` | `BIGINT` | NO | IDENTITY | Surrogate primary key |
| `product_id` | `BIGINT` | NO | — | FK → `catalog.products.id` |
| `location_id` | `BIGINT` | NO | — | FK → `network.inventory_locations.id` |
| `reorder_level` | `NUMERIC(18,4)` | NO | `0` | ATP trigger for replenishment |
| `minimum_threshold` | `NUMERIC(18,4)` | NO | `0` | Minimum stock floor |
| `safety_stock_qty` | `NUMERIC(18,4)` | NO | `0` | Safety buffer |
| `maximum_stock_level` | `NUMERIC(18,4)` | YES | NULL | Overstock indicator |
| `lead_time_days` | `INTEGER` | YES | NULL | Assumed lead time |
| `review_frequency_days` | `INTEGER` | YES | NULL | Replenishment review cadence |
| `effective_from` | `TIMESTAMPTZ` | NO | `NOW()` | Current threshold effective date |
| `exception_approval_ref` | `VARCHAR(64)` | YES | NULL | Authorized exception reference |
| `version` | `INTEGER` | NO | `1` | Optimistic lock |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Record creation |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Last modification |

---

### Table: `inventory.stock_policy_history`

| Attribute | Detail |
|-----------|--------|
| **Business Purpose** | Immutable history of threshold changes for audit and replenishment analysis. |
| **Estimated Growth** | **Medium** — append-only; grows with policy changes. |

| Column | Data Type | Nullable | Default | Description |
|--------|-----------|----------|---------|-------------|
| `id` | `BIGINT` | NO | IDENTITY | Surrogate primary key |
| `stock_policy_id` | `BIGINT` | NO | — | FK → `inventory.stock_policies.id` |
| `reorder_level` | `NUMERIC(18,4)` | NO | — | Historical reorder level |
| `minimum_threshold` | `NUMERIC(18,4)` | NO | — | Historical minimum |
| `safety_stock_qty` | `NUMERIC(18,4)` | NO | — | Historical safety stock |
| `effective_from` | `TIMESTAMPTZ` | NO | — | Period start |
| `effective_to` | `TIMESTAMPTZ` | NO | — | Period end |
| `changed_by` | `BIGINT` | YES | NULL | FK → `identity.user_accounts.id` |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Record creation |

---

## Domain 5: Procurement (`procurement` schema)

---

### Table: `procurement.suppliers`

| Attribute | Detail |
|-----------|--------|
| **Business Purpose** | External vendor master for procurement, receipt, and payment. |
| **Estimated Growth** | **Low** — hundreds to low thousands. |

| Column | Data Type | Nullable | Default | Description |
|--------|-----------|----------|---------|-------------|
| `id` | `BIGINT` | NO | IDENTITY | Surrogate primary key |
| `supplier_code` | `VARCHAR(32)` | NO | — | Business key |
| `supplier_name` | `VARCHAR(256)` | NO | — | Legal/display name |
| `contact_name` | `VARCHAR(128)` | YES | NULL | Primary contact |
| `contact_email` | `VARCHAR(256)` | YES | NULL | Contact email |
| `contact_phone` | `VARCHAR(32)` | YES | NULL | Contact phone |
| `payment_terms_days` | `INTEGER` | NO | `30` | Net payment days |
| `default_lead_time_days` | `INTEGER` | YES | NULL | Default procurement lead time |
| `is_consignment` | `BOOLEAN` | NO | `FALSE` | Consignment agreement flag (BR-031) |
| `delivery_rating` | `NUMERIC(3,2)` | YES | NULL | Performance score 0.00–5.00 |
| `is_active` | `BOOLEAN` | NO | `TRUE` | Soft-delete flag |
| `version` | `INTEGER` | NO | `1` | Optimistic lock |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Record creation |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Last modification |

---

### Table: `procurement.purchase_requisitions`

| Attribute | Detail |
|-----------|--------|
| **Business Purpose** | Internal replenishment request with approval workflow before PO creation. |
| **Estimated Growth** | **Medium** — ~50K–500K/year. |

| Column | Data Type | Nullable | Default | Description |
|--------|-----------|----------|---------|-------------|
| `id` | `BIGINT` | NO | IDENTITY | Surrogate primary key |
| `requisition_number` | `VARCHAR(64)` | NO | — | Business key |
| `requesting_location_id` | `BIGINT` | NO | — | FK → `network.inventory_locations.id` |
| `requested_delivery_date` | `DATE` | YES | NULL | Target delivery date |
| `triggering_alert_id` | `BIGINT` | YES | NULL | FK → `audit.operational_alerts.id` |
| `approval_status` | `VARCHAR(32)` | NO | `'DRAFT'` | DRAFT, SUBMITTED, APPROVED, REJECTED, CONVERTED |
| `approved_by` | `BIGINT` | YES | NULL | FK → `identity.user_accounts.id` |
| `approved_at` | `TIMESTAMPTZ` | YES | NULL | Approval timestamp |
| `purchase_order_id` | `BIGINT` | YES | NULL | FK → `procurement.purchase_orders.id` |
| `version` | `INTEGER` | NO | `1` | Optimistic lock |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Record creation |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Last modification |
| `created_by` | `BIGINT` | NO | — | FK → `identity.user_accounts.id` |

---

### Table: `procurement.purchase_requisition_lines`

| Attribute | Detail |
|-----------|--------|
| **Business Purpose** | Line-level product and quantity on a purchase requisition. |
| **Estimated Growth** | **Medium** — 1–20 lines per requisition. |

| Column | Data Type | Nullable | Default | Description |
|--------|-----------|----------|---------|-------------|
| `id` | `BIGINT` | NO | IDENTITY | Surrogate primary key |
| `requisition_id` | `BIGINT` | NO | — | FK → `procurement.purchase_requisitions.id` |
| `line_number` | `INTEGER` | NO | — | Sequence within requisition |
| `product_id` | `BIGINT` | NO | — | FK → `catalog.products.id` |
| `requested_qty` | `NUMERIC(18,4)` | NO | — | Requested quantity (> 0) |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Record creation |

---

### Table: `procurement.purchase_orders`

| Attribute | Detail |
|-----------|--------|
| **Business Purpose** | Authorized commercial commitment to a supplier. |
| **Estimated Growth** | **Medium** — ~20K–200K/year. |

| Column | Data Type | Nullable | Default | Description |
|--------|-----------|----------|---------|-------------|
| `id` | `BIGINT` | NO | IDENTITY | Surrogate primary key |
| `po_number` | `VARCHAR(64)` | NO | — | Business key |
| `supplier_id` | `BIGINT` | NO | — | FK → `procurement.suppliers.id` |
| `receiving_location_id` | `BIGINT` | NO | — | FK → `network.inventory_locations.id` |
| `order_date` | `DATE` | NO | — | PO creation date |
| `expected_delivery_date` | `DATE` | YES | NULL | Expected arrival |
| `po_status` | `VARCHAR(32)` | NO | `'OPEN'` | OPEN, PARTIAL, CLOSED, CANCELLED |
| `total_commitment_amount` | `NUMERIC(18,2)` | NO | `0` | Header total value |
| `currency_code` | `CHAR(3)` | NO | `'USD'` | ISO 4217 |
| `payment_terms_days` | `INTEGER` | NO | `30` | Copied from supplier at creation |
| `version` | `INTEGER` | NO | `1` | Optimistic lock |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Record creation |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Last modification |
| `created_by` | `BIGINT` | NO | — | FK → `identity.user_accounts.id` |

---

### Table: `procurement.purchase_order_lines`

| Attribute | Detail |
|-----------|--------|
| **Business Purpose** | Product, quantity, and price lines on a purchase order. |
| **Estimated Growth** | **Medium** — 1–50 lines per PO. |

| Column | Data Type | Nullable | Default | Description |
|--------|-----------|----------|---------|-------------|
| `id` | `BIGINT` | NO | IDENTITY | Surrogate primary key |
| `purchase_order_id` | `BIGINT` | NO | — | FK → `procurement.purchase_orders.id` |
| `line_number` | `INTEGER` | NO | — | Sequence within PO |
| `product_id` | `BIGINT` | NO | — | FK → `catalog.products.id` |
| `ordered_qty` | `NUMERIC(18,4)` | NO | — | Ordered quantity |
| `received_qty` | `NUMERIC(18,4)` | NO | `0` | Cumulative received |
| `unit_price` | `NUMERIC(18,4)` | NO | — | Price per UOM |
| `line_amount` | `NUMERIC(18,2)` | NO | — | Extended line value |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Record creation |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Last modification |

---

### Table: `procurement.expected_inbound_deliveries`

| Attribute | Detail |
|-----------|--------|
| **Business Purpose** | Planned supplier shipment schedule tied to a purchase order. |
| **Estimated Growth** | **Medium** — 0–N deliveries per PO. |

| Column | Data Type | Nullable | Default | Description |
|--------|-----------|----------|---------|-------------|
| `id` | `BIGINT` | NO | IDENTITY | Surrogate primary key |
| `delivery_reference` | `VARCHAR(64)` | NO | — | Business key |
| `purchase_order_id` | `BIGINT` | NO | — | FK → `procurement.purchase_orders.id` |
| `expected_arrival_date` | `DATE` | NO | — | Planned arrival |
| `carrier_reference` | `VARCHAR(128)` | YES | NULL | Carrier/shipment ID |
| `shipment_status` | `VARCHAR(32)` | NO | `'PLANNED'` | PLANNED, IN_TRANSIT, ARRIVED, DELAYED |
| `receiving_location_id` | `BIGINT` | NO | — | FK → `network.inventory_locations.id` |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Record creation |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Last modification |

---

### Table: `procurement.expected_inbound_delivery_lines`

| Attribute | Detail |
|-----------|--------|
| **Business Purpose** | Expected quantity by product on an inbound delivery plan. |
| **Estimated Growth** | **Medium** — lines per delivery. |

| Column | Data Type | Nullable | Default | Description |
|--------|-----------|----------|---------|-------------|
| `id` | `BIGINT` | NO | IDENTITY | Surrogate primary key |
| `delivery_id` | `BIGINT` | NO | — | FK → `procurement.expected_inbound_deliveries.id` |
| `purchase_order_line_id` | `BIGINT` | NO | — | FK → `procurement.purchase_order_lines.id` |
| `product_id` | `BIGINT` | NO | — | FK → `catalog.products.id` |
| `expected_qty` | `NUMERIC(18,4)` | NO | — | Expected quantity |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Record creation |

---

## Domain 6: Inbound (`inbound` schema)

---

### Table: `inbound.goods_receipts`

| Attribute | Detail |
|-----------|--------|
| **Business Purpose** | Verified acceptance of inbound supplier goods at receiving dock. |
| **Estimated Growth** | **Medium–High** — ~100K–2M/year depending on receipt volume. |

| Column | Data Type | Nullable | Default | Description |
|--------|-----------|----------|---------|-------------|
| `id` | `BIGINT` | NO | IDENTITY | Surrogate primary key |
| `gr_number` | `VARCHAR(64)` | NO | — | Business key |
| `purchase_order_id` | `BIGINT` | YES | NULL | FK → `procurement.purchase_orders.id` |
| `exception_authorization_ref` | `VARCHAR(64)` | YES | NULL | Ad-hoc receipt exception (BR-007) |
| `supplier_id` | `BIGINT` | NO | — | FK → `procurement.suppliers.id` |
| `receiving_location_id` | `BIGINT` | NO | — | FK → `network.inventory_locations.id` |
| `receipt_date` | `TIMESTAMPTZ` | NO | `NOW()` | Receipt timestamp |
| `verification_status` | `VARCHAR(32)` | NO | `'PENDING'` | PENDING, VERIFIED, REJECTED, PARTIAL |
| `receiving_clerk_id` | `BIGINT` | NO | — | FK → `identity.user_accounts.id` |
| `version` | `INTEGER` | NO | `1` | Optimistic lock |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Record creation |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Last modification |

---

### Table: `inbound.goods_receipt_lines`

| Attribute | Detail |
|-----------|--------|
| **Business Purpose** | Line-level received product, quantity, and condition. |
| **Estimated Growth** | **Medium–High** — multiple lines per receipt. |

| Column | Data Type | Nullable | Default | Description |
|--------|-----------|----------|---------|-------------|
| `id` | `BIGINT` | NO | IDENTITY | Surrogate primary key |
| `goods_receipt_id` | `BIGINT` | NO | — | FK → `inbound.goods_receipts.id` |
| `line_number` | `INTEGER` | NO | — | Sequence within receipt |
| `purchase_order_line_id` | `BIGINT` | YES | NULL | FK → `procurement.purchase_order_lines.id` |
| `product_id` | `BIGINT` | NO | — | FK → `catalog.products.id` |
| `received_qty` | `NUMERIC(18,4)` | NO | — | Received quantity |
| `accepted_qty` | `NUMERIC(18,4)` | NO | `0` | Accepted after verification |
| `condition_grade` | `VARCHAR(32)` | NO | `'GOOD'` | GOOD, DAMAGED, REJECTED |
| `lot_batch_id` | `BIGINT` | YES | NULL | FK → `inventory.lot_batches.id` |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Record creation |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Last modification |

---

### Table: `inbound.receipt_discrepancies`

| Attribute | Detail |
|-----------|--------|
| **Business Purpose** | Documented variance between expected and actual receipt. |
| **Estimated Growth** | **Medium** — ~5–15% of receipt lines. |

| Column | Data Type | Nullable | Default | Description |
|--------|-----------|----------|---------|-------------|
| `id` | `BIGINT` | NO | IDENTITY | Surrogate primary key |
| `discrepancy_reference` | `VARCHAR(64)` | NO | — | Business key |
| `goods_receipt_id` | `BIGINT` | NO | — | FK → `inbound.goods_receipts.id` |
| `goods_receipt_line_id` | `BIGINT` | YES | NULL | FK → `inbound.goods_receipt_lines.id` |
| `discrepancy_type` | `VARCHAR(32)` | NO | — | SHORT, OVER, WRONG_ITEM, DAMAGE, SHELF_LIFE |
| `expected_qty` | `NUMERIC(18,4)` | YES | NULL | Expected quantity |
| `actual_qty` | `NUMERIC(18,4)` | YES | NULL | Actual quantity |
| `product_id` | `BIGINT` | NO | — | FK → `catalog.products.id` |
| `reason_code_id` | `BIGINT` | YES | NULL | FK → `governance.reason_codes.id` |
| `evidence_notes` | `TEXT` | YES | NULL | Supporting evidence |
| `resolution_status` | `VARCHAR(32)` | NO | `'OPEN'` | OPEN, RESOLVED, CLAIMED |
| `resolution_outcome` | `VARCHAR(64)` | YES | NULL | Resolution description |
| `supplier_claim_ref` | `VARCHAR(64)` | YES | NULL | Supplier claim reference |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Record creation |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Last modification |

---

### Table: `inbound.put_aways`

| Attribute | Detail |
|-----------|--------|
| **Business Purpose** | Confirmation of stock placement from dock to storage — triggers ATP availability. |
| **Estimated Growth** | **Medium–High** — one or more per accepted receipt line. |

| Column | Data Type | Nullable | Default | Description |
|--------|-----------|----------|---------|-------------|
| `id` | `BIGINT` | NO | IDENTITY | Surrogate primary key |
| `put_away_reference` | `VARCHAR(64)` | NO | — | Business key |
| `goods_receipt_id` | `BIGINT` | NO | — | FK → `inbound.goods_receipts.id` |
| `goods_receipt_line_id` | `BIGINT` | NO | — | FK → `inbound.goods_receipt_lines.id` |
| `product_id` | `BIGINT` | NO | — | FK → `catalog.products.id` |
| `quantity` | `NUMERIC(18,4)` | NO | — | Put-away quantity |
| `from_area` | `VARCHAR(64)` | NO | `'RECEIVING_DOCK'` | Source area |
| `storage_position_id` | `BIGINT` | NO | — | FK → `network.storage_positions.id` |
| `lot_batch_id` | `BIGINT` | YES | NULL | FK → `inventory.lot_batches.id` |
| `put_away_at` | `TIMESTAMPTZ` | NO | `NOW()` | Put-away completion time |
| `availability_effective_at` | `TIMESTAMPTZ` | NO | `NOW()` | ATP effective timestamp (BR-005) |
| `performed_by` | `BIGINT` | NO | — | FK → `identity.user_accounts.id` |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Record creation |

---

## Domain 7: Finance (`finance` schema)

---

### Table: `finance.supplier_invoices`

| Attribute | Detail |
|-----------|--------|
| **Business Purpose** | Supplier billing document for three-way match and payment authorization. |
| **Estimated Growth** | **Medium** — ~20K–200K/year aligned with PO volume. |

| Column | Data Type | Nullable | Default | Description |
|--------|-----------|----------|---------|-------------|
| `id` | `BIGINT` | NO | IDENTITY | Surrogate primary key |
| `invoice_number` | `VARCHAR(64)` | NO | — | Supplier invoice number |
| `supplier_id` | `BIGINT` | NO | — | FK → `procurement.suppliers.id` |
| `purchase_order_id` | `BIGINT` | NO | — | FK → `procurement.purchase_orders.id` |
| `invoice_date` | `DATE` | NO | — | Invoice date |
| `total_amount` | `NUMERIC(18,2)` | NO | — | Invoice total |
| `currency_code` | `CHAR(3)` | NO | `'USD'` | ISO 4217 |
| `match_status` | `VARCHAR(32)` | NO | `'PENDING'` | PENDING, MATCHED, EXCEPTION |
| `tolerance_variance` | `NUMERIC(18,2)` | YES | NULL | Match tolerance variance |
| `payment_status` | `VARCHAR(32)` | NO | `'UNAUTHORIZED'` | UNAUTHORIZED, AUTHORIZED, PAID |
| `version` | `INTEGER` | NO | `1` | Optimistic lock |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Record creation |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Last modification |

---

### Table: `finance.supplier_invoice_lines`

| Attribute | Detail |
|-----------|--------|
| **Business Purpose** | Billed product, quantity, and price for three-way match. |
| **Estimated Growth** | **Medium** — lines per invoice. |

| Column | Data Type | Nullable | Default | Description |
|--------|-----------|----------|---------|-------------|
| `id` | `BIGINT` | NO | IDENTITY | Surrogate primary key |
| `supplier_invoice_id` | `BIGINT` | NO | — | FK → `finance.supplier_invoices.id` |
| `line_number` | `INTEGER` | NO | — | Sequence within invoice |
| `purchase_order_line_id` | `BIGINT` | YES | NULL | FK → `procurement.purchase_order_lines.id` |
| `product_id` | `BIGINT` | NO | — | FK → `catalog.products.id` |
| `billed_qty` | `NUMERIC(18,4)` | NO | — | Billed quantity |
| `unit_price` | `NUMERIC(18,4)` | NO | — | Billed unit price |
| `line_amount` | `NUMERIC(18,2)` | NO | — | Extended amount |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Record creation |

---

### Table: `finance.invoice_goods_receipt_match`

| Attribute | Detail |
|-----------|--------|
| **Business Purpose** | Associative link between supplier invoices and goods receipts for three-way match (BR-008). |
| **Estimated Growth** | **Medium** — M:N between invoices and receipts. |

| Column | Data Type | Nullable | Default | Description |
|--------|-----------|----------|---------|-------------|
| `id` | `BIGINT` | NO | IDENTITY | Surrogate primary key |
| `supplier_invoice_id` | `BIGINT` | NO | — | FK → `finance.supplier_invoices.id` |
| `goods_receipt_id` | `BIGINT` | NO | — | FK → `inbound.goods_receipts.id` |
| `match_status` | `VARCHAR(32)` | NO | `'PENDING'` | PENDING, MATCHED, EXCEPTION |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Record creation |

---

## Domain 8: Fulfillment (`fulfillment` schema)

---

### Table: `fulfillment.customer_orders`

| Attribute | Detail |
|-----------|--------|
| **Business Purpose** | Customer demand document driving reservation, pick, and ship. |
| **Estimated Growth** | **High** — ~500K–10M/year for active retailers. |

| Column | Data Type | Nullable | Default | Description |
|--------|-----------|----------|---------|-------------|
| `id` | `BIGINT` | NO | IDENTITY | Surrogate primary key |
| `order_number` | `VARCHAR(64)` | NO | — | Business key |
| `customer_reference` | `VARCHAR(128)` | YES | NULL | External customer ID |
| `order_date` | `TIMESTAMPTZ` | NO | `NOW()` | Order placement date |
| `requested_delivery_date` | `DATE` | YES | NULL | Customer requested delivery |
| `order_status` | `VARCHAR(32)` | NO | `'DRAFT'` | DRAFT, CONFIRMED, PARTIAL, FULFILLED, CANCELLED |
| `channel` | `VARCHAR(32)` | YES | NULL | WEB, STORE, B2B, EDI |
| `version` | `INTEGER` | NO | `1` | Optimistic lock |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Record creation |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Last modification |

---

### Table: `fulfillment.customer_order_lines`

| Attribute | Detail |
|-----------|--------|
| **Business Purpose** | Order line product, requested, fulfilled, and backordered quantities. |
| **Estimated Growth** | **High** — 1–20 lines per order. |

| Column | Data Type | Nullable | Default | Description |
|--------|-----------|----------|---------|-------------|
| `id` | `BIGINT` | NO | IDENTITY | Surrogate primary key |
| `customer_order_id` | `BIGINT` | NO | — | FK → `fulfillment.customer_orders.id` |
| `line_number` | `INTEGER` | NO | — | Sequence within order |
| `product_id` | `BIGINT` | NO | — | FK → `catalog.products.id` |
| `requested_qty` | `NUMERIC(18,4)` | NO | — | Ordered quantity |
| `fulfilled_qty` | `NUMERIC(18,4)` | NO | `0` | Shipped quantity |
| `backordered_qty` | `NUMERIC(18,4)` | NO | `0` | Backordered quantity |
| `fulfillment_location_id` | `BIGINT` | YES | NULL | FK → `network.inventory_locations.id` |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Record creation |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Last modification |

---

### Table: `fulfillment.inventory_reservations`

| Attribute | Detail |
|-----------|--------|
| **Business Purpose** | ATP hold for confirmed order lines until ship or release. |
| **Estimated Growth** | **High** — active reservations proportional to open orders. |

| Column | Data Type | Nullable | Default | Description |
|--------|-----------|----------|---------|-------------|
| `id` | `BIGINT` | NO | IDENTITY | Surrogate primary key |
| `reservation_reference` | `VARCHAR(64)` | NO | — | Business key |
| `customer_order_id` | `BIGINT` | NO | — | FK → `fulfillment.customer_orders.id` |
| `order_line_id` | `BIGINT` | NO | — | FK → `fulfillment.customer_order_lines.id` |
| `product_id` | `BIGINT` | NO | — | FK → `catalog.products.id` |
| `location_id` | `BIGINT` | NO | — | FK → `network.inventory_locations.id` |
| `stock_position_id` | `BIGINT` | NO | — | FK → `inventory.stock_positions.id` |
| `reserved_qty` | `NUMERIC(18,4)` | NO | — | Reserved quantity |
| `reservation_status` | `VARCHAR(32)` | NO | `'ACTIVE'` | ACTIVE, RELEASED, FULFILLED |
| `reserved_at` | `TIMESTAMPTZ` | NO | `NOW()` | Reservation timestamp |
| `expires_at` | `TIMESTAMPTZ` | YES | NULL | Optional expiry |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Record creation |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Last modification |

---

### Table: `fulfillment.fulfillment_executions`

| Attribute | Detail |
|-----------|--------|
| **Business Purpose** | Pick/pack/verify warehouse work unit for an order. |
| **Estimated Growth** | **High** — 1+ per order; ~500K–10M/year. |

| Column | Data Type | Nullable | Default | Description |
|--------|-----------|----------|---------|-------------|
| `id` | `BIGINT` | NO | IDENTITY | Surrogate primary key |
| `fulfillment_reference` | `VARCHAR(64)` | NO | — | Business key |
| `customer_order_id` | `BIGINT` | NO | — | FK → `fulfillment.customer_orders.id` |
| `fulfillment_location_id` | `BIGINT` | NO | — | FK → `network.inventory_locations.id` |
| `pick_verification_status` | `VARCHAR(32)` | NO | `'PENDING'` | PENDING, VERIFIED, EXCEPTION |
| `pack_confirmed` | `BOOLEAN` | NO | `FALSE` | Pack confirmation flag |
| `assigned_picker_id` | `BIGINT` | YES | NULL | FK → `identity.user_accounts.id` |
| `has_exception` | `BOOLEAN` | NO | `FALSE` | Exception flag |
| `pick_completed_at` | `TIMESTAMPTZ` | YES | NULL | Pick completion timestamp |
| `version` | `INTEGER` | NO | `1` | Optimistic lock |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Record creation |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Last modification |

---

### Table: `fulfillment.fulfillment_pick_lines`

| Attribute | Detail |
|-----------|--------|
| **Business Purpose** | Individual pick line with lot attribution and verification. |
| **Estimated Growth** | **High** — multiple per fulfillment execution. |

| Column | Data Type | Nullable | Default | Description |
|--------|-----------|----------|---------|-------------|
| `id` | `BIGINT` | NO | IDENTITY | Surrogate primary key |
| `fulfillment_execution_id` | `BIGINT` | NO | — | FK → `fulfillment.fulfillment_executions.id` |
| `order_line_id` | `BIGINT` | NO | — | FK → `fulfillment.customer_order_lines.id` |
| `product_id` | `BIGINT` | NO | — | FK → `catalog.products.id` |
| `requested_qty` | `NUMERIC(18,4)` | NO | — | Quantity to pick |
| `picked_qty` | `NUMERIC(18,4)` | NO | `0` | Actual picked quantity |
| `storage_position_id` | `BIGINT` | YES | NULL | FK → `network.storage_positions.id` |
| `lot_batch_id` | `BIGINT` | YES | NULL | FK → `inventory.lot_batches.id` |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Record creation |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Last modification |

---

### Table: `fulfillment.backorders`

| Attribute | Detail |
|-----------|--------|
| **Business Purpose** | Customer-agreed delay for unfulfilled order line quantity. |
| **Estimated Growth** | **Medium** — subset of order lines during stockouts. |

| Column | Data Type | Nullable | Default | Description |
|--------|-----------|----------|---------|-------------|
| `id` | `BIGINT` | NO | IDENTITY | Surrogate primary key |
| `backorder_reference` | `VARCHAR(64)` | NO | — | Business key |
| `customer_order_id` | `BIGINT` | NO | — | FK → `fulfillment.customer_orders.id` |
| `order_line_id` | `BIGINT` | NO | — | FK → `fulfillment.customer_order_lines.id` |
| `product_id` | `BIGINT` | NO | — | FK → `catalog.products.id` |
| `backordered_qty` | `NUMERIC(18,4)` | NO | — | Backordered quantity |
| `customer_acknowledged` | `BOOLEAN` | NO | `FALSE` | BR-028 acknowledgment flag |
| `acknowledged_at` | `TIMESTAMPTZ` | YES | NULL | Acknowledgment timestamp |
| `expected_fulfillment_date` | `DATE` | YES | NULL | Expected ship date |
| `backorder_reason` | `VARCHAR(64)` | YES | NULL | Reason code |
| `resolution_status` | `VARCHAR(32)` | NO | `'OPEN'` | OPEN, FULFILLED, CANCELLED |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Record creation |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Last modification |

---

### Table: `fulfillment.shipments`

| Attribute | Detail |
|-----------|--------|
| **Business Purpose** | Confirmed dispatch deducting on-hand and consuming reservations. |
| **Estimated Growth** | **High** — ~500K–10M/year. |

| Column | Data Type | Nullable | Default | Description |
|--------|-----------|----------|---------|-------------|
| `id` | `BIGINT` | NO | IDENTITY | Surrogate primary key |
| `shipment_number` | `VARCHAR(64)` | NO | — | Business key |
| `customer_order_id` | `BIGINT` | NO | — | FK → `fulfillment.customer_orders.id` |
| `fulfillment_execution_id` | `BIGINT` | NO | — | FK → `fulfillment.fulfillment_executions.id` |
| `ship_from_location_id` | `BIGINT` | NO | — | FK → `network.inventory_locations.id` |
| `ship_date` | `TIMESTAMPTZ` | NO | `NOW()` | Dispatch timestamp |
| `carrier_reference` | `VARCHAR(128)` | YES | NULL | Carrier name/code |
| `tracking_identifier` | `VARCHAR(128)` | YES | NULL | Tracking number |
| `shipment_status` | `VARCHAR(32)` | NO | `'DISPATCHED'` | DISPATCHED, IN_TRANSIT, DELIVERED |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Record creation |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Last modification |

---

### Table: `fulfillment.shipment_lines`

| Attribute | Detail |
|-----------|--------|
| **Business Purpose** | Shipped product, quantity, and lot per shipment. |
| **Estimated Growth** | **High** — multiple lines per shipment. |

| Column | Data Type | Nullable | Default | Description |
|--------|-----------|----------|---------|-------------|
| `id` | `BIGINT` | NO | IDENTITY | Surrogate primary key |
| `shipment_id` | `BIGINT` | NO | — | FK → `fulfillment.shipments.id` |
| `order_line_id` | `BIGINT` | NO | — | FK → `fulfillment.customer_order_lines.id` |
| `product_id` | `BIGINT` | NO | — | FK → `catalog.products.id` |
| `shipped_qty` | `NUMERIC(18,4)` | NO | — | Shipped quantity |
| `lot_batch_id` | `BIGINT` | YES | NULL | FK → `inventory.lot_batches.id` |
| `reservation_id` | `BIGINT` | YES | NULL | FK → `fulfillment.inventory_reservations.id` |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Record creation |

---

## Domain 9: Network Transfer (`transfer` schema)

---

### Table: `transfer.transfer_requests`

| Attribute | Detail |
|-----------|--------|
| **Business Purpose** | Formal request to move stock between locations; initial lifecycle state of Stock Transfer aggregate. |
| **Estimated Growth** | **Medium** — ~10K–100K/year. |

| Column | Data Type | Nullable | Default | Description |
|--------|-----------|----------|---------|-------------|
| `id` | `BIGINT` | NO | IDENTITY | Surrogate primary key |
| `request_number` | `VARCHAR(64)` | NO | — | Business key |
| `source_location_id` | `BIGINT` | NO | — | FK → `network.inventory_locations.id` |
| `destination_location_id` | `BIGINT` | NO | — | FK → `network.inventory_locations.id` |
| `request_reason` | `VARCHAR(128)` | YES | NULL | Rebalance, shortage, operational |
| `request_status` | `VARCHAR(32)` | NO | `'SUBMITTED'` | SUBMITTED, APPROVED, REJECTED, CONVERTED |
| `requested_by` | `BIGINT` | NO | — | FK → `identity.user_accounts.id` |
| `approved_by` | `BIGINT` | YES | NULL | FK → `identity.user_accounts.id` |
| `approved_at` | `TIMESTAMPTZ` | YES | NULL | Approval timestamp |
| `rejection_reason` | `TEXT` | YES | NULL | Rejection justification |
| `stock_transfer_id` | `BIGINT` | YES | NULL | FK → `transfer.stock_transfers.id` |
| `version` | `INTEGER` | NO | `1` | Optimistic lock |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Record creation |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Last modification |

---

### Table: `transfer.transfer_request_lines`

| Attribute | Detail |
|-----------|--------|
| **Business Purpose** | Product and quantity requested on a transfer request. |
| **Estimated Growth** | **Medium** — lines per request. |

| Column | Data Type | Nullable | Default | Description |
|--------|-----------|----------|---------|-------------|
| `id` | `BIGINT` | NO | IDENTITY | Surrogate primary key |
| `transfer_request_id` | `BIGINT` | NO | — | FK → `transfer.transfer_requests.id` |
| `line_number` | `INTEGER` | NO | — | Sequence within request |
| `product_id` | `BIGINT` | NO | — | FK → `catalog.products.id` |
| `requested_qty` | `NUMERIC(18,4)` | NO | — | Requested quantity |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Record creation |

---

### Table: `transfer.stock_transfers`

| Attribute | Detail |
|-----------|--------|
| **Business Purpose** | Executed inter-location stock movement from dispatch to receipt. |
| **Estimated Growth** | **Medium** — ~10K–100K/year. |

| Column | Data Type | Nullable | Default | Description |
|--------|-----------|----------|---------|-------------|
| `id` | `BIGINT` | NO | IDENTITY | Surrogate primary key |
| `transfer_number` | `VARCHAR(64)` | NO | — | Business key |
| `transfer_request_id` | `BIGINT` | YES | NULL | FK → `transfer.transfer_requests.id` |
| `source_location_id` | `BIGINT` | NO | — | FK → `network.inventory_locations.id` |
| `destination_location_id` | `BIGINT` | NO | — | FK → `network.inventory_locations.id` |
| `transfer_status` | `VARCHAR(32)` | NO | `'APPROVED'` | REQUESTED, APPROVED, IN_TRANSIT, RECEIVED, CANCELLED |
| `dispatch_date` | `TIMESTAMPTZ` | YES | NULL | Source dispatch timestamp |
| `receipt_date` | `TIMESTAMPTZ` | YES | NULL | Destination receipt timestamp |
| `version` | `INTEGER` | NO | `1` | Optimistic lock |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Record creation |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Last modification |

---

### Table: `transfer.stock_transfer_lines`

| Attribute | Detail |
|-----------|--------|
| **Business Purpose** | Product, quantity, and lot on a stock transfer. |
| **Estimated Growth** | **Medium** — lines per transfer. |

| Column | Data Type | Nullable | Default | Description |
|--------|-----------|----------|---------|-------------|
| `id` | `BIGINT` | NO | IDENTITY | Surrogate primary key |
| `stock_transfer_id` | `BIGINT` | NO | — | FK → `transfer.stock_transfers.id` |
| `line_number` | `INTEGER` | NO | — | Sequence within transfer |
| `product_id` | `BIGINT` | NO | — | FK → `catalog.products.id` |
| `quantity` | `NUMERIC(18,4)` | NO | — | Transfer quantity |
| `lot_batch_id` | `BIGINT` | YES | NULL | FK → `inventory.lot_batches.id` |
| `dispatched_qty` | `NUMERIC(18,4)` | NO | `0` | Quantity dispatched |
| `received_qty` | `NUMERIC(18,4)` | NO | `0` | Quantity received |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Record creation |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Last modification |

---

### Table: `transfer.in_transit_stock`

| Attribute | Detail |
|-----------|--------|
| **Business Purpose** | Pipeline inventory between dispatch and destination receipt. |
| **Estimated Growth** | **Medium** — active in-transit rows; short lifecycle. |

| Column | Data Type | Nullable | Default | Description |
|--------|-----------|----------|---------|-------------|
| `id` | `BIGINT` | NO | IDENTITY | Surrogate primary key |
| `in_transit_reference` | `VARCHAR(64)` | NO | — | Business key |
| `stock_transfer_id` | `BIGINT` | NO | — | FK → `transfer.stock_transfers.id` |
| `stock_transfer_line_id` | `BIGINT` | NO | — | FK → `transfer.stock_transfer_lines.id` |
| `product_id` | `BIGINT` | NO | — | FK → `catalog.products.id` |
| `quantity` | `NUMERIC(18,4)` | NO | — | In-transit quantity |
| `source_location_id` | `BIGINT` | NO | — | FK → `network.inventory_locations.id` |
| `destination_location_id` | `BIGINT` | NO | — | FK → `network.inventory_locations.id` |
| `dispatch_date` | `TIMESTAMPTZ` | NO | — | Dispatch timestamp |
| `expected_receipt_date` | `DATE` | YES | NULL | Expected arrival |
| `in_transit_status` | `VARCHAR(32)` | NO | `'IN_TRANSIT'` | IN_TRANSIT, RECEIVED, LOST, DELAYED |
| `carrier_reference` | `VARCHAR(128)` | YES | NULL | Carrier reference |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Record creation |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Last modification |

---

## Domain 10: Inventory Accuracy (`accuracy` schema)

---

### Table: `accuracy.cycle_counts`

| Attribute | Detail |
|-----------|--------|
| **Business Purpose** | Scheduled partial physical count assignment with blind count protocol. |
| **Estimated Growth** | **Medium–High** — continuous rotating counts; ~50K–500K/year. |

| Column | Data Type | Nullable | Default | Description |
|--------|-----------|----------|---------|-------------|
| `id` | `BIGINT` | NO | IDENTITY | Surrogate primary key |
| `count_assignment_number` | `VARCHAR(64)` | NO | — | Business key |
| `schedule_date` | `DATE` | NO | — | Scheduled count date |
| `location_id` | `BIGINT` | NO | — | FK → `network.inventory_locations.id` |
| `product_id` | `BIGINT` | NO | — | FK → `catalog.products.id` |
| `storage_position_id` | `BIGINT` | YES | NULL | FK → `network.storage_positions.id` |
| `counter_id` | `BIGINT` | NO | — | FK → `identity.user_accounts.id` |
| `count_status` | `VARCHAR(32)` | NO | `'SCHEDULED'` | SCHEDULED, IN_PROGRESS, COMPLETED |
| `physical_count_qty` | `NUMERIC(18,4)` | YES | NULL | Recorded physical quantity |
| `system_count_qty` | `NUMERIC(18,4)` | YES | NULL | System qty (hidden until submission) |
| `completed_at` | `TIMESTAMPTZ` | YES | NULL | Completion timestamp |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Record creation |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Last modification |

---

### Table: `accuracy.physical_inventory_counts`

| Attribute | Detail |
|-----------|--------|
| **Business Purpose** | Wall-to-wall count event imposing location freeze (BR-024). |
| **Estimated Growth** | **Low** — 1–4 per location per year. |

| Column | Data Type | Nullable | Default | Description |
|--------|-----------|----------|---------|-------------|
| `id` | `BIGINT` | NO | IDENTITY | Surrogate primary key |
| `count_event_number` | `VARCHAR(64)` | NO | — | Business key |
| `location_id` | `BIGINT` | NO | — | FK → `network.inventory_locations.id` |
| `count_start_date` | `TIMESTAMPTZ` | NO | — | Count start |
| `count_completion_date` | `TIMESTAMPTZ` | YES | NULL | Count end |
| `freeze_status` | `VARCHAR(32)` | NO | `'ACTIVE'` | ACTIVE, RELEASED |
| `total_variances` | `INTEGER` | NO | `0` | Variance count |
| `certification_status` | `VARCHAR(32)` | NO | `'IN_PROGRESS'` | IN_PROGRESS, CERTIFIED |
| `version` | `INTEGER` | NO | `1` | Optimistic lock |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Record creation |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Last modification |

---

### Table: `accuracy.count_variances`

| Attribute | Detail |
|-----------|--------|
| **Business Purpose** | System vs. physical quantity difference requiring investigation. |
| **Estimated Growth** | **Medium** — subset of count events. |

| Column | Data Type | Nullable | Default | Description |
|--------|-----------|----------|---------|-------------|
| `id` | `BIGINT` | NO | IDENTITY | Surrogate primary key |
| `variance_reference` | `VARCHAR(64)` | NO | — | Business key |
| `cycle_count_id` | `BIGINT` | YES | NULL | FK → `accuracy.cycle_counts.id` |
| `physical_count_id` | `BIGINT` | YES | NULL | FK → `accuracy.physical_inventory_counts.id` |
| `stock_position_id` | `BIGINT` | NO | — | FK → `inventory.stock_positions.id` |
| `product_id` | `BIGINT` | NO | — | FK → `catalog.products.id` |
| `location_id` | `BIGINT` | NO | — | FK → `network.inventory_locations.id` |
| `system_qty` | `NUMERIC(18,4)` | NO | — | System quantity at count |
| `physical_qty` | `NUMERIC(18,4)` | NO | — | Physical quantity counted |
| `variance_qty` | `NUMERIC(18,4)` | NO | — | physical − system |
| `variance_value` | `NUMERIC(18,2)` | YES | NULL | Financial impact |
| `investigation_status` | `VARCHAR(32)` | NO | `'OPEN'` | OPEN, INVESTIGATED |
| `investigation_findings` | `TEXT` | YES | NULL | Root cause notes |
| `approval_status` | `VARCHAR(32)` | NO | `'PENDING'` | PENDING, APPROVED, REJECTED |
| `approver_id` | `BIGINT` | YES | NULL | FK → `identity.user_accounts.id` |
| `approved_at` | `TIMESTAMPTZ` | YES | NULL | Approval timestamp |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Record creation |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Last modification |

---

### Table: `accuracy.stock_adjustments`

| Attribute | Detail |
|-----------|--------|
| **Business Purpose** | Authorized correction to stock position with mandatory reason code. |
| **Estimated Growth** | **Medium** — adjustments from counts and ad-hoc corrections. |

| Column | Data Type | Nullable | Default | Description |
|--------|-----------|----------|---------|-------------|
| `id` | `BIGINT` | NO | IDENTITY | Surrogate primary key |
| `adjustment_reference` | `VARCHAR(64)` | NO | — | Business key |
| `stock_position_id` | `BIGINT` | NO | — | FK → `inventory.stock_positions.id` |
| `product_id` | `BIGINT` | NO | — | FK → `catalog.products.id` |
| `location_id` | `BIGINT` | NO | — | FK → `network.inventory_locations.id` |
| `adjustment_qty` | `NUMERIC(18,4)` | NO | — | Signed quantity (+/−) |
| `qty_before` | `NUMERIC(18,4)` | NO | — | On-hand before adjustment |
| `qty_after` | `NUMERIC(18,4)` | NO | — | On-hand after adjustment |
| `reason_code_id` | `BIGINT` | NO | — | FK → `governance.reason_codes.id` |
| `count_variance_id` | `BIGINT` | YES | NULL | FK → `accuracy.count_variances.id` |
| `approval_status` | `VARCHAR(32)` | NO | `'PENDING'` | PENDING, APPROVED, REJECTED |
| `initiated_by` | `BIGINT` | NO | — | FK → `identity.user_accounts.id` |
| `approved_by` | `BIGINT` | YES | NULL | FK → `identity.user_accounts.id` |
| `adjustment_date` | `TIMESTAMPTZ` | NO | `NOW()` | Effective date |
| `version` | `INTEGER` | NO | `1` | Optimistic lock |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Record creation |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Last modification |

---

### Table: `accuracy.inventory_write_offs`

| Attribute | Detail |
|-----------|--------|
| **Business Purpose** | Permanent authorized removal of inventory value. |
| **Estimated Growth** | **Low–Medium** — smaller volume than adjustments. |

| Column | Data Type | Nullable | Default | Description |
|--------|-----------|----------|---------|-------------|
| `id` | `BIGINT` | NO | IDENTITY | Surrogate primary key |
| `write_off_reference` | `VARCHAR(64)` | NO | — | Business key |
| `stock_position_id` | `BIGINT` | NO | — | FK → `inventory.stock_positions.id` |
| `product_id` | `BIGINT` | NO | — | FK → `catalog.products.id` |
| `location_id` | `BIGINT` | NO | — | FK → `network.inventory_locations.id` |
| `write_off_qty` | `NUMERIC(18,4)` | NO | — | Quantity written off |
| `financial_value` | `NUMERIC(18,2)` | YES | NULL | Value impact |
| `reason_code_id` | `BIGINT` | NO | — | FK → `governance.reason_codes.id` |
| `evidence_reference` | `VARCHAR(128)` | YES | NULL | Supporting evidence ref |
| `disposition_method` | `VARCHAR(32)` | YES | NULL | DESTROY, DONATE, SCRAP |
| `return_disposition_id` | `BIGINT` | YES | NULL | FK → `returns.return_dispositions.id` |
| `initiated_by` | `BIGINT` | NO | — | FK → `identity.user_accounts.id` |
| `authorized_by` | `BIGINT` | NO | — | FK → `identity.user_accounts.id` |
| `write_off_date` | `TIMESTAMPTZ` | NO | `NOW()` | Effective date |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Record creation |

---

## Domain 11: Returns (`returns` schema)

---

### Table: `returns.return_authorizations`

| Attribute | Detail |
|-----------|--------|
| **Business Purpose** | RMA gating customer return before warehouse acceptance (BR-025). |
| **Estimated Growth** | **Medium** — ~5–15% of order volume. |

| Column | Data Type | Nullable | Default | Description |
|--------|-----------|----------|---------|-------------|
| `id` | `BIGINT` | NO | IDENTITY | Surrogate primary key |
| `rma_number` | `VARCHAR(64)` | NO | — | Business key |
| `customer_order_id` | `BIGINT` | NO | — | FK → `fulfillment.customer_orders.id` |
| `customer_reference` | `VARCHAR(128)` | YES | NULL | Customer identifier |
| `return_reason` | `VARCHAR(128)` | YES | NULL | Return reason |
| `authorization_date` | `TIMESTAMPTZ` | NO | `NOW()` | RMA issue date |
| `expiration_date` | `DATE` | YES | NULL | RMA expiry |
| `disposition_expectation` | `VARCHAR(64)` | YES | NULL | Expected disposition |
| `authorization_status` | `VARCHAR(32)` | NO | `'ACTIVE'` | ACTIVE, EXPIRED, USED, CANCELLED |
| `version` | `INTEGER` | NO | `1` | Optimistic lock |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Record creation |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Last modification |

---

### Table: `returns.return_authorization_lines`

| Attribute | Detail |
|-----------|--------|
| **Business Purpose** | Authorized return products and quantities on an RMA. |
| **Estimated Growth** | **Medium** — lines per RMA. |

| Column | Data Type | Nullable | Default | Description |
|--------|-----------|----------|---------|-------------|
| `id` | `BIGINT` | NO | IDENTITY | Surrogate primary key |
| `return_authorization_id` | `BIGINT` | NO | — | FK → `returns.return_authorizations.id` |
| `line_number` | `INTEGER` | NO | — | Sequence within RMA |
| `product_id` | `BIGINT` | NO | — | FK → `catalog.products.id` |
| `authorized_qty` | `NUMERIC(18,4)` | NO | — | Authorized return quantity |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Record creation |

---

### Table: `returns.customer_returns`

| Attribute | Detail |
|-----------|--------|
| **Business Purpose** | Physical receipt of customer-returned goods. |
| **Estimated Growth** | **Medium** — aligned with RMA volume. |

| Column | Data Type | Nullable | Default | Description |
|--------|-----------|----------|---------|-------------|
| `id` | `BIGINT` | NO | IDENTITY | Surrogate primary key |
| `return_number` | `VARCHAR(64)` | NO | — | Business key |
| `return_authorization_id` | `BIGINT` | NO | — | FK → `returns.return_authorizations.id` |
| `customer_order_id` | `BIGINT` | NO | — | FK → `fulfillment.customer_orders.id` |
| `receiving_location_id` | `BIGINT` | NO | — | FK → `network.inventory_locations.id` |
| `receipt_date` | `TIMESTAMPTZ` | NO | `NOW()` | Receipt timestamp |
| `inspection_status` | `VARCHAR(32)` | NO | `'PENDING'` | PENDING, INSPECTED |
| `receiving_clerk_id` | `BIGINT` | NO | — | FK → `identity.user_accounts.id` |
| `version` | `INTEGER` | NO | `1` | Optimistic lock |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Record creation |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Last modification |

---

### Table: `returns.customer_return_lines`

| Attribute | Detail |
|-----------|--------|
| **Business Purpose** | Returned product, quantity, and condition at receipt. |
| **Estimated Growth** | **Medium** — lines per return. |

| Column | Data Type | Nullable | Default | Description |
|--------|-----------|----------|---------|-------------|
| `id` | `BIGINT` | NO | IDENTITY | Surrogate primary key |
| `customer_return_id` | `BIGINT` | NO | — | FK → `returns.customer_returns.id` |
| `line_number` | `INTEGER` | NO | — | Sequence within return |
| `product_id` | `BIGINT` | NO | — | FK → `catalog.products.id` |
| `returned_qty` | `NUMERIC(18,4)` | NO | — | Returned quantity |
| `condition_at_receipt` | `VARCHAR(32)` | NO | — | GOOD, DAMAGED, DEFECTIVE, OPENED |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Record creation |

---

### Table: `returns.return_dispositions`

| Attribute | Detail |
|-----------|--------|
| **Business Purpose** | Inspection outcome — restock, quarantine, or write-off. |
| **Estimated Growth** | **Medium** — one per return line. |

| Column | Data Type | Nullable | Default | Description |
|--------|-----------|----------|---------|-------------|
| `id` | `BIGINT` | NO | IDENTITY | Surrogate primary key |
| `disposition_reference` | `VARCHAR(64)` | NO | — | Business key |
| `customer_return_id` | `BIGINT` | NO | — | FK → `returns.customer_returns.id` |
| `return_line_id` | `BIGINT` | NO | — | FK → `returns.customer_return_lines.id` |
| `product_id` | `BIGINT` | NO | — | FK → `catalog.products.id` |
| `quantity` | `NUMERIC(18,4)` | NO | — | Disposition quantity |
| `condition_grade` | `VARCHAR(32)` | NO | — | Resale quality grade |
| `disposition_decision` | `VARCHAR(32)` | NO | — | RESTOCK, QUARANTINE, WRITE_OFF |
| `restock_location_id` | `BIGINT` | YES | NULL | FK → `network.inventory_locations.id` |
| `quarantine_hold_id` | `BIGINT` | YES | NULL | FK → `inventory.quarantine_holds.id` |
| `write_off_id` | `BIGINT` | YES | NULL | FK → `accuracy.inventory_write_offs.id` |
| `inspector_id` | `BIGINT` | NO | — | FK → `identity.user_accounts.id` |
| `inspection_date` | `TIMESTAMPTZ` | NO | `NOW()` | Inspection timestamp |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Record creation |

---

## Domain 12: Commercial (`commercial` schema)

---

### Table: `commercial.promotional_stock_allocations`

| Attribute | Detail |
|-----------|--------|
| **Business Purpose** | Ring-fenced stock for promotional campaigns or product launches (BR-029). |
| **Estimated Growth** | **Low** — hundreds to low thousands active campaigns. |

| Column | Data Type | Nullable | Default | Description |
|--------|-----------|----------|---------|-------------|
| `id` | `BIGINT` | NO | IDENTITY | Surrogate primary key |
| `allocation_reference` | `VARCHAR(64)` | NO | — | Business key |
| `product_id` | `BIGINT` | NO | — | FK → `catalog.products.id` |
| `allocated_qty` | `NUMERIC(18,4)` | NO | — | Ring-fenced quantity |
| `campaign_name` | `VARCHAR(256)` | NO | — | Campaign or launch name |
| `channel` | `VARCHAR(32)` | YES | NULL | Channel scope |
| `effective_start_date` | `DATE` | NO | — | Campaign start |
| `effective_end_date` | `DATE` | NO | — | Campaign end |
| `readiness_status` | `VARCHAR(32)` | NO | `'PLANNED'` | PLANNED, READY, ACTIVE, CLOSED |
| `commercial_approval_ref` | `VARCHAR(64)` | YES | NULL | Commercial approval reference |
| `version` | `INTEGER` | NO | `1` | Optimistic lock |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Record creation |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Last modification |

---

### Table: `commercial.promotional_allocation_locations`

| Attribute | Detail |
|-----------|--------|
| **Business Purpose** | Locations supplying ring-fenced promotional stock. |
| **Estimated Growth** | **Low** — 1–N locations per allocation. |

| Column | Data Type | Nullable | Default | Description |
|--------|-----------|----------|---------|-------------|
| `id` | `BIGINT` | NO | IDENTITY | Surrogate primary key |
| `allocation_id` | `BIGINT` | NO | — | FK → `commercial.promotional_stock_allocations.id` |
| `location_id` | `BIGINT` | NO | — | FK → `network.inventory_locations.id` |
| `stock_position_id` | `BIGINT` | YES | NULL | FK → `inventory.stock_positions.id` |
| `allocated_qty_at_location` | `NUMERIC(18,4)` | NO | — | Quantity at this location |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Record creation |

---

## Domain 13: Identity & Access (`identity` schema)

---

### Table: `identity.user_accounts`

| Attribute | Detail |
|-----------|--------|
| **Business Purpose** | Authenticated user identity and accountability anchor for all operations. |
| **Estimated Growth** | **Low** — hundreds to low thousands of users. |

| Column | Data Type | Nullable | Default | Description |
|--------|-----------|----------|---------|-------------|
| `id` | `BIGINT` | NO | IDENTITY | Surrogate primary key |
| `user_identifier` | `VARCHAR(64)` | NO | — | Login / employee ID |
| `display_name` | `VARCHAR(256)` | NO | — | Full display name |
| `email` | `VARCHAR(256)` | YES | NULL | Contact email |
| `account_status` | `VARCHAR(32)` | NO | `'ACTIVE'` | ACTIVE, SUSPENDED, DEACTIVATED |
| `effective_from` | `DATE` | NO | — | Account effective start |
| `last_activity_at` | `TIMESTAMPTZ` | YES | NULL | Last system activity |
| `has_sod_conflict` | `BOOLEAN` | NO | `FALSE` | Segregation-of-duties conflict flag |
| `version` | `INTEGER` | NO | `1` | Optimistic lock |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Record creation |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Last modification |

---

### Table: `identity.role_assignments`

| Attribute | Detail |
|-----------|--------|
| **Business Purpose** | Role delegation with permission boundaries per user. |
| **Estimated Growth** | **Low** — 1–5 roles per user. |

| Column | Data Type | Nullable | Default | Description |
|--------|-----------|----------|---------|-------------|
| `id` | `BIGINT` | NO | IDENTITY | Surrogate primary key |
| `user_account_id` | `BIGINT` | NO | — | FK → `identity.user_accounts.id` |
| `role_name` | `VARCHAR(64)` | NO | — | WAREHOUSE_MANAGER, RECEIVING_CLERK, BUYER, etc. |
| `permission_set` | `VARCHAR(128)` | YES | NULL | Permission bundle reference |
| `assignment_status` | `VARCHAR(32)` | NO | `'ACTIVE'` | ACTIVE, INACTIVE |
| `effective_from` | `DATE` | NO | — | Assignment start |
| `effective_to` | `DATE` | YES | NULL | Assignment end |
| `sod_compliant` | `BOOLEAN` | NO | `TRUE` | SoD compliance at assignment |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Record creation |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Last modification |

---

### Table: `identity.role_assignment_locations`

| Attribute | Detail |
|-----------|--------|
| **Business Purpose** | Location scope restricting role permissions to authorized sites. |
| **Estimated Growth** | **Low** — 0–N locations per assignment. |

| Column | Data Type | Nullable | Default | Description |
|--------|-----------|----------|---------|-------------|
| `id` | `BIGINT` | NO | IDENTITY | Surrogate primary key |
| `role_assignment_id` | `BIGINT` | NO | — | FK → `identity.role_assignments.id` |
| `location_id` | `BIGINT` | NO | — | FK → `network.inventory_locations.id` |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Record creation |

---

## Domain 14: Audit & Reporting (`audit` schema)

---

### Table: `audit.inventory_movement_records`

| Attribute | Detail |
|-----------|--------|
| **Business Purpose** | Immutable append-only log of every stock quantity change. |
| **Estimated Growth** | **Very High** — 10M–100M+/year. **Partition monthly** on `movement_timestamp`. |

| Column | Data Type | Nullable | Default | Description |
|--------|-----------|----------|---------|-------------|
| `id` | `BIGINT` | NO | IDENTITY | Surrogate primary key (per partition) |
| `movement_reference` | `VARCHAR(64)` | NO | — | Business transaction reference |
| `movement_type` | `VARCHAR(32)` | NO | — | RECEIPT, SHIPMENT, TRANSFER, ADJUSTMENT, WRITE_OFF, RESERVATION, RETURN, PUT_AWAY |
| `stock_position_id` | `BIGINT` | NO | — | FK → `inventory.stock_positions.id` |
| `product_id` | `BIGINT` | NO | — | FK → `catalog.products.id` (denormalized) |
| `location_id` | `BIGINT` | NO | — | FK → `network.inventory_locations.id` (denormalized) |
| `quantity_change` | `NUMERIC(18,4)` | NO | — | Signed quantity delta |
| `qty_before` | `NUMERIC(18,4)` | NO | — | On-hand before |
| `qty_after` | `NUMERIC(18,4)` | NO | — | On-hand after |
| `lot_batch_id` | `BIGINT` | YES | NULL | FK → `inventory.lot_batches.id` |
| `reason_code_id` | `BIGINT` | YES | NULL | FK → `governance.reason_codes.id` |
| `source_document_type` | `VARCHAR(32)` | NO | — | Originating document type |
| `source_document_id` | `BIGINT` | NO | — | Originating document PK |
| `performed_by` | `BIGINT` | NO | — | FK → `identity.user_accounts.id` |
| `movement_timestamp` | `TIMESTAMPTZ` | NO | `NOW()` | Event timestamp (partition key) |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Insert timestamp |

**Partitioning:** Range partition by `movement_timestamp` (monthly). Retain 24 months online; archive older partitions to cold storage.

---

### Table: `audit.audit_trail_records`

| Attribute | Detail |
|-----------|--------|
| **Business Purpose** | Governance-grade before/after snapshots for material entity changes. |
| **Estimated Growth** | **Very High** — proportional to governed mutations. **Partition monthly** on `event_timestamp`. |

| Column | Data Type | Nullable | Default | Description |
|--------|-----------|----------|---------|-------------|
| `id` | `BIGINT` | NO | IDENTITY | Surrogate primary key (per partition) |
| `audit_event_reference` | `VARCHAR(64)` | NO | — | Business reference |
| `affected_entity_type` | `VARCHAR(64)` | NO | — | Entity/table name |
| `affected_entity_id` | `BIGINT` | NO | — | Affected record PK |
| `action_performed` | `VARCHAR(32)` | NO | — | CREATE, UPDATE, APPROVE, CANCEL |
| `user_id` | `BIGINT` | NO | — | FK → `identity.user_accounts.id` |
| `role_at_action` | `VARCHAR(64)` | YES | NULL | Role at time of action |
| `before_state` | `JSONB` | YES | NULL | Snapshot before change |
| `after_state` | `JSONB` | YES | NULL | Snapshot after change |
| `approval_chain_ref` | `VARCHAR(128)` | YES | NULL | Approval workflow reference |
| `movement_record_id` | `BIGINT` | YES | NULL | FK → `audit.inventory_movement_records.id` |
| `event_timestamp` | `TIMESTAMPTZ` | NO | `NOW()` | Event timestamp (partition key) |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Insert timestamp |

**Partitioning:** Range partition by `event_timestamp` (monthly). Immutable — no UPDATE/DELETE.

---

### Table: `audit.operational_alerts`

| Attribute | Detail |
|-----------|--------|
| **Business Purpose** | Derived notifications for threshold breaches, pending approvals, and exceptions. |
| **Estimated Growth** | **High** — alerts generated and resolved continuously; purge resolved > 90 days. |

| Column | Data Type | Nullable | Default | Description |
|--------|-----------|----------|---------|-------------|
| `id` | `BIGINT` | NO | IDENTITY | Surrogate primary key |
| `alert_reference` | `VARCHAR(64)` | NO | — | Business key |
| `alert_type` | `VARCHAR(32)` | NO | — | LOW_STOCK, OUT_OF_STOCK, PENDING_APPROVAL, TRANSFER_EXCEPTION, INBOUND_DELAY, CAMPAIGN_READINESS |
| `severity` | `VARCHAR(16)` | NO | `'MEDIUM'` | LOW, MEDIUM, HIGH, CRITICAL |
| `product_id` | `BIGINT` | YES | NULL | FK → `catalog.products.id` |
| `location_id` | `BIGINT` | YES | NULL | FK → `network.inventory_locations.id` |
| `stock_position_id` | `BIGINT` | YES | NULL | FK → `inventory.stock_positions.id` |
| `source_entity_type` | `VARCHAR(64)` | YES | NULL | Triggering entity type |
| `source_entity_id` | `BIGINT` | YES | NULL | Triggering entity PK |
| `triggering_condition` | `TEXT` | YES | NULL | Condition description |
| `assigned_role` | `VARCHAR(64)` | YES | NULL | Recipient role |
| `acknowledgment_status` | `VARCHAR(32)` | NO | `'OPEN'` | OPEN, ACKNOWLEDGED, RESOLVED |
| `resolution_status` | `VARCHAR(32)` | NO | `'PENDING'` | PENDING, RESOLVED, DISMISSED |
| `alert_date` | `TIMESTAMPTZ` | NO | `NOW()` | Alert creation |
| `resolved_at` | `TIMESTAMPTZ` | YES | NULL | Resolution timestamp |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Record creation |

---

### Table: `audit.inventory_valuation_snapshots`

| Attribute | Detail |
|-----------|--------|
| **Business Purpose** | Point-in-time inventory value summary for finance reconciliation (BP-30). |
| **Estimated Growth** | **Low** — monthly/periodic snapshots; ~12–52 per year plus ad-hoc. |

| Column | Data Type | Nullable | Default | Description |
|--------|-----------|----------|---------|-------------|
| `id` | `BIGINT` | NO | IDENTITY | Surrogate primary key |
| `snapshot_reference` | `VARCHAR(64)` | NO | — | Business key |
| `valuation_date` | `DATE` | NO | — | Snapshot as-of date |
| `location_scope` | `VARCHAR(32)` | NO | — | SINGLE, REGION, NETWORK |
| `total_inventory_value` | `NUMERIC(18,2)` | NO | — | Total owned value |
| `owned_value` | `NUMERIC(18,2)` | NO | — | Owned stock value |
| `consignment_value` | `NUMERIC(18,2)` | NO | `0` | Consignment (excluded from owned) |
| `gl_variance` | `NUMERIC(18,2)` | YES | NULL | Variance vs. general ledger |
| `reconciliation_status` | `VARCHAR(32)` | NO | `'DRAFT'` | DRAFT, RECONCILED, EXCEPTION |
| `prepared_by` | `BIGINT` | NO | — | FK → `identity.user_accounts.id` |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Record creation |

---

### Table: `audit.inventory_valuation_lines`

| Attribute | Detail |
|-----------|--------|
| **Business Purpose** | Product-level quantity and value detail within a valuation snapshot. |
| **Estimated Growth** | **Medium per snapshot** — product × location lines; snapshot-bound. |

| Column | Data Type | Nullable | Default | Description |
|--------|-----------|----------|---------|-------------|
| `id` | `BIGINT` | NO | IDENTITY | Surrogate primary key |
| `snapshot_id` | `BIGINT` | NO | — | FK → `audit.inventory_valuation_snapshots.id` |
| `product_id` | `BIGINT` | NO | — | FK → `catalog.products.id` |
| `location_id` | `BIGINT` | NO | — | FK → `network.inventory_locations.id` |
| `quantity` | `NUMERIC(18,4)` | NO | — | Snapshot quantity |
| `unit_cost` | `NUMERIC(18,4)` | NO | — | Unit valuation cost |
| `extended_value` | `NUMERIC(18,2)` | NO | — | quantity × unit_cost |
| `ownership_type` | `VARCHAR(32)` | NO | `'OWNED'` | OWNED, CONSIGNMENT |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Record creation |

---

## Physical Design Appendices

### Appendix A: Table Inventory Summary

| Schema | Tables | Growth Tier |
|--------|--------|-------------|
| `catalog` | 2 | Low |
| `network` | 2 | Low |
| `governance` | 2 | Low |
| `inventory` | 5 | Medium |
| `procurement` | 8 | Medium |
| `inbound` | 4 | Medium–High |
| `finance` | 3 | Medium |
| `fulfillment` | 8 | High |
| `transfer` | 5 | Medium |
| `accuracy` | 5 | Medium |
| `returns` | 5 | Medium |
| `commercial` | 2 | Low |
| `identity` | 3 | Low |
| `audit` | 5 | Low–Very High |
| **Total** | **59 tables** | |

### Appendix B: Critical Unique Constraints (Logical)

| Table | Unique Key Columns |
|-------|-------------------|
| `catalog.products` | `sku` |
| `network.inventory_locations` | `location_code` |
| `network.storage_positions` | `(location_id, position_code)` |
| `inventory.stock_positions` | `(product_id, location_id)` |
| `inventory.stock_policies` | `(product_id, location_id)` |
| `procurement.suppliers` | `supplier_code` |
| `procurement.purchase_orders` | `po_number` |
| `fulfillment.customer_orders` | `order_number` |
| `identity.user_accounts` | `user_identifier` |
| `governance.reason_codes` | `reason_code` |

### Appendix C: Partitioning & Archival Strategy

| Table | Strategy | Retention |
|-------|----------|-----------|
| `audit.inventory_movement_records` | Monthly range on `movement_timestamp` | 24 months online; archive thereafter |
| `audit.audit_trail_records` | Monthly range on `event_timestamp` | 7 years (compliance); tiered storage |
| `audit.operational_alerts` | No partition; index on `acknowledgment_status` | Purge resolved > 90 days |
| `fulfillment.customer_orders` | Optional yearly archive of closed orders | 3 years online |
| `inbound.goods_receipts` | Archive closed receipts > 3 years | Cold storage |

### Appendix D: High-Priority Index Candidates

| Table | Index Columns | Rationale |
|-------|---------------|-----------|
| `inventory.stock_positions` | `(product_id, location_id)` | Unique lookup; hottest path |
| `inventory.stock_positions` | `(location_id, stock_status)` | Low-stock monitoring |
| `fulfillment.inventory_reservations` | `(stock_position_id, reservation_status)` | Active reservation queries |
| `fulfillment.customer_orders` | `(order_status, order_date)` | Open order dashboards |
| `audit.inventory_movement_records` | `(stock_position_id, movement_timestamp DESC)` | Position history |
| `inbound.goods_receipts` | `(purchase_order_id)` | PO receipt lookup |
| `procurement.purchase_order_lines` | `(purchase_order_id, product_id)` | Open PO line queries |
| `inventory.lot_batches` | `(product_id, expiration_date)` | FEFO pick ordering |

### Appendix E: Logical-to-Physical Entity Mapping

| Logical Entity (SRS-DB-001) | Physical Table(s) |
|-----------------------------|-------------------|
| Product | `catalog.products`, `catalog.product_identifiers` |
| Inventory Location | `network.inventory_locations` |
| Storage Position | `network.storage_positions` |
| Governance Policy | `governance.governance_policies` |
| Reason Code | `governance.reason_codes` |
| Stock Position | `inventory.stock_positions` |
| Lot/Batch | `inventory.lot_batches` |
| Quarantine Hold | `inventory.quarantine_holds` |
| Stock Policy | `inventory.stock_policies`, `inventory.stock_policy_history` |
| Supplier | `procurement.suppliers` |
| Purchase Requisition | `procurement.purchase_requisitions`, `_lines` |
| Purchase Order | `procurement.purchase_orders`, `_lines` |
| Expected Inbound Delivery | `procurement.expected_inbound_deliveries`, `_lines` |
| Goods Receipt | `inbound.goods_receipts`, `_lines` |
| Receipt Discrepancy | `inbound.receipt_discrepancies` |
| Put-Away | `inbound.put_aways` |
| Supplier Invoice | `finance.supplier_invoices`, `_lines`, `invoice_goods_receipt_match` |
| Customer Order | `fulfillment.customer_orders`, `_lines` |
| Inventory Reservation | `fulfillment.inventory_reservations` |
| Fulfillment Execution | `fulfillment.fulfillment_executions`, `fulfillment_pick_lines` |
| Backorder | `fulfillment.backorders` |
| Shipment | `fulfillment.shipments`, `shipment_lines` |
| Transfer Request | `transfer.transfer_requests`, `_lines` |
| Stock Transfer | `transfer.stock_transfers`, `_lines` |
| In-Transit Stock | `transfer.in_transit_stock` |
| Cycle Count | `accuracy.cycle_counts` |
| Physical Inventory Count | `accuracy.physical_inventory_counts` |
| Count Variance | `accuracy.count_variances` |
| Stock Adjustment | `accuracy.stock_adjustments` |
| Inventory Write-Off | `accuracy.inventory_write_offs` |
| Return Authorization | `returns.return_authorizations`, `_lines` |
| Customer Return | `returns.customer_returns`, `_lines` |
| Return Disposition | `returns.return_dispositions` |
| Promotional Stock Allocation | `commercial.promotional_stock_allocations`, `promotional_allocation_locations` |
| User Account | `identity.user_accounts` |
| Role Assignment | `identity.role_assignments`, `role_assignment_locations` |
| Inventory Movement Record | `audit.inventory_movement_records` |
| Audit Trail Record | `audit.audit_trail_records` |
| Operational Alert | `audit.operational_alerts` |
| Inventory Valuation Snapshot | `audit.inventory_valuation_snapshots`, `inventory_valuation_lines` |

---

## Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Database Architect | | | |
| DDD Solution Architect | | | |
| Solution Architect | | | |
| Inventory Controller | | | |

---

*End of Physical Data Model*

*Document ID: SRS-DB-002 | Version 1.0 | July 6, 2026*
