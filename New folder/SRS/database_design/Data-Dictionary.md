# Data Dictionary
## Inventory Management System — PostgreSQL

---

## Document Information

| Attribute | Detail |
|-----------|--------|
| **Document ID** | SRS-DB-007 |
| **Document Title** | Data Dictionary — Inventory Management System |
| **Version** | 1.0 |
| **Status** | Draft |
| **Document Owner** | Database Architect |
| **Source Document** | SRS-DB-002 (Physical Data Model, v1.0) |
| **Target Platform** | PostgreSQL 15+ |
| **Date** | July 6, 2026 |

### Purpose

This document provides a **developer- and business-analyst-friendly reference** for every table and column in the Inventory Management System database. It translates the Physical Data Model (SRS-DB-002) into plain-language business definitions, relationship notes, and data-type conventions — without DDL or SQL.

### Conventions Used in This Document

| Convention | Meaning |
|------------|---------|
| **Nullable** | `YES` = column may be empty; `NO` = column is required |
| **Default** | Value assigned automatically when a row is inserted without an explicit value; `—` means no default |
| **Related Entity** | `→ schema.table (column)` for foreign keys; `— (primary key)` for surrogate PKs; business-key uniqueness noted where applicable |
| **Business Meaning** | One-sentence plain-language explanation suitable for business analysts |
| **Naming** | All identifiers use `snake_case` per PDM standards |

---

## Schema Index — All Tables (58)

| # | Schema.Table | One-Line Description |
|---|--------------|----------------------|
| 1 | `catalog.products` | Canonical SKU master — identity for all inventory operations across locations and channels. |
| 2 | `catalog.product_identifiers` | Alternate product identifiers (barcodes, vendor codes) for lookup at receipt and pick. |
| 3 | `network.inventory_locations` | Physical sites (warehouses, stores, DCs) anchoring all stock balances and operations. |
| 4 | `network.storage_positions` | Bin/zone/shelf addresses within a location for put-away and pick path. |
| 5 | `governance.governance_policies` | Organization-wide approval thresholds, tolerances, and exception rules. |
| 6 | `governance.reason_codes` | Standardized categorized explanations for adjustments, write-offs, and discrepancies. |
| 7 | `inventory.stock_positions` | Authoritative on-hand, reserved, and ATP quantities per product per location — central quantity hub. |
| 8 | `inventory.lot_batches` | Traceable lot/batch identity with shelf-life attributes for FEFO and recall. |
| 9 | `inventory.quarantine_holds` | Holds removing quantity from ATP for quality, regulatory, recall, or customs reasons. |
| 10 | `inventory.stock_policies` | Replenishment thresholds per product per location. |
| 11 | `inventory.stock_policy_history` | Immutable history of threshold changes for audit and replenishment analysis. |
| 12 | `procurement.suppliers` | External vendor master for procurement, receipt, and payment. |
| 13 | `procurement.purchase_requisitions` | Internal replenishment request with approval workflow before PO creation. |
| 14 | `procurement.purchase_requisition_lines` | Line-level product and quantity on a purchase requisition. |
| 15 | `procurement.purchase_orders` | Authorized commercial commitment to a supplier. |
| 16 | `procurement.purchase_order_lines` | Product, quantity, and price lines on a purchase order. |
| 17 | `procurement.expected_inbound_deliveries` | Planned supplier shipment schedule tied to a purchase order. |
| 18 | `procurement.expected_inbound_delivery_lines` | Expected quantity by product on an inbound delivery plan. |
| 19 | `inbound.goods_receipts` | Verified acceptance of inbound supplier goods at receiving dock. |
| 20 | `inbound.goods_receipt_lines` | Line-level received product, quantity, and condition. |
| 21 | `inbound.receipt_discrepancies` | Documented variance between expected and actual receipt. |
| 22 | `inbound.put_aways` | Confirmation of stock placement from dock to storage — triggers ATP availability. |
| 23 | `finance.supplier_invoices` | Supplier billing document for three-way match and payment authorization. |
| 24 | `finance.supplier_invoice_lines` | Billed product, quantity, and price for three-way match. |
| 25 | `finance.invoice_goods_receipt_match` | Associative link between supplier invoices and goods receipts for three-way match (BR-008). |
| 26 | `fulfillment.customer_orders` | Customer demand document driving reservation, pick, and ship. |
| 27 | `fulfillment.customer_order_lines` | Order line product, requested, fulfilled, and backordered quantities. |
| 28 | `fulfillment.inventory_reservations` | ATP hold for confirmed order lines until ship or release. |
| 29 | `fulfillment.fulfillment_executions` | Pick/pack/verify warehouse work unit for an order. |
| 30 | `fulfillment.fulfillment_pick_lines` | Individual pick line with lot attribution and verification. |
| 31 | `fulfillment.backorders` | Customer-agreed delay for unfulfilled order line quantity. |
| 32 | `fulfillment.shipments` | Confirmed dispatch deducting on-hand and consuming reservations. |
| 33 | `fulfillment.shipment_lines` | Shipped product, quantity, and lot per shipment. |
| 34 | `transfer.transfer_requests` | Formal request to move stock between locations; initial lifecycle state of Stock Transfer aggregate. |
| 35 | `transfer.transfer_request_lines` | Product and quantity requested on a transfer request. |
| 36 | `transfer.stock_transfers` | Executed inter-location stock movement from dispatch to receipt. |
| 37 | `transfer.stock_transfer_lines` | Product, quantity, and lot on a stock transfer. |
| 38 | `transfer.in_transit_stock` | Pipeline inventory between dispatch and destination receipt. |
| 39 | `accuracy.cycle_counts` | Scheduled partial physical count assignment with blind count protocol. |
| 40 | `accuracy.physical_inventory_counts` | Wall-to-wall count event imposing location freeze (BR-024). |
| 41 | `accuracy.count_variances` | System vs. physical quantity difference requiring investigation. |
| 42 | `accuracy.stock_adjustments` | Authorized correction to stock position with mandatory reason code. |
| 43 | `accuracy.inventory_write_offs` | Permanent authorized removal of inventory value. |
| 44 | `returns.return_authorizations` | RMA gating customer return before warehouse acceptance (BR-025). |
| 45 | `returns.return_authorization_lines` | Authorized return products and quantities on an RMA. |
| 46 | `returns.customer_returns` | Physical receipt of customer-returned goods. |
| 47 | `returns.customer_return_lines` | Returned product, quantity, and condition at receipt. |
| 48 | `returns.return_dispositions` | Inspection outcome — restock, quarantine, or write-off. |
| 49 | `commercial.promotional_stock_allocations` | Ring-fenced stock for promotional campaigns or product launches (BR-029). |
| 50 | `commercial.promotional_allocation_locations` | Locations supplying ring-fenced promotional stock. |
| 51 | `identity.user_accounts` | Authenticated user identity and accountability anchor for all operations. |
| 52 | `identity.role_assignments` | Role delegation with permission boundaries per user. |
| 53 | `identity.role_assignment_locations` | Location scope restricting role permissions to authorized sites. |
| 54 | `audit.inventory_movement_records` | Immutable append-only log of every stock quantity change. |
| 55 | `audit.audit_trail_records` | Governance-grade before/after snapshots for material entity changes. |
| 56 | `audit.operational_alerts` | Derived notifications for threshold breaches, pending approvals, and exceptions. |
| 57 | `audit.inventory_valuation_snapshots` | Point-in-time inventory value summary for finance reconciliation (BP-30). |
| 58 | `audit.inventory_valuation_lines` | Product-level quantity and value detail within a valuation snapshot. |

*All table definitions present in SRS-DB-002 are documented below (58 tables). PDM Appendix A inventory summary cites 59 tables across 14 schemas.*

---

## catalog.products

**Table description:** Canonical SKU master — identity for all inventory operations across locations and channels.

| Column | Data Type | Nullable | Default | Business Meaning | Related Entity |
|--------|-----------|----------|---------|------------------|----------------|
| `id` | `BIGINT` | NO | IDENTITY | System-generated unique identifier for this record. | — (primary key) |
| `sku` | `VARCHAR(64)` | NO | — | Unique business identifier for this record (stock keeping unit). | Unique business key |
| `product_name` | `VARCHAR(256)` | NO | — | The human-readable name shown to users in screens and reports. | — |
| `description` | `TEXT` | YES | — | Optional longer text describing additional details. | — |
| `unit_of_measure` | `VARCHAR(16)` | NO | — | Unit of measure for counting and transacting this product (e.g., each, case, kilogram). | — |
| `category_code` | `VARCHAR(64)` | YES | — | Code referencing the product's merchandise or category grouping. | — |
| `lifecycle_status` | `VARCHAR(32)` | NO | `'ACTIVE'` | Catalog lifecycle status indicating whether the product is sellable. | — |
| `abc_classification` | `VARCHAR(1)` | YES | — | ABC classification ranking inventory importance or turnover velocity. | — |
| `is_shelf_life` | `BOOLEAN` | NO | `FALSE` | Indicates whether this product requires expiration-date tracking. | — |
| `is_traceable` | `BOOLEAN` | NO | `FALSE` | Indicates whether this product must be tracked by lot or batch number. | — |
| `rotation_policy` | `VARCHAR(8)` | YES | — | Stock rotation policy: first-in-first-out or first-expired-first-out. | — |
| `mrsl_days` | `INTEGER` | YES | — | Minimum days of shelf life required before the product may be sold or shipped. | — |
| `superseded_by_sku` | `VARCHAR(64)` | YES | — | SKU of the successor product when this item is discontinued. | → `catalog.products` (`sku`) |
| `is_active` | `BOOLEAN` | NO | `TRUE` | Indicates whether this master-data record is active; deactivated records are retained for history. | — |
| `version` | `INTEGER` | NO | 1 | Version counter incremented on each update to prevent conflicting concurrent edits. | — |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp when this record was first created in the system. | — |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp of the most recent update to this record. | — |
| `created_by` | `BIGINT` | YES | — | The user who created this record. | → `identity.user_accounts` (`id`) |

---

## catalog.product_identifiers

**Table description:** Alternate product identifiers (barcodes, vendor codes) for lookup at receipt and pick.

| Column | Data Type | Nullable | Default | Business Meaning | Related Entity |
|--------|-----------|----------|---------|------------------|----------------|
| `id` | `BIGINT` | NO | IDENTITY | System-generated unique identifier for this record. | — (primary key) |
| `product_id` | `BIGINT` | NO | — | The product this record pertains to. | → `catalog.products` (`id`) |
| `identifier_type` | `VARCHAR(32)` | NO | — | Type of alternate identifier (barcode, vendor code, GTIN, etc.). | — |
| `identifier_value` | `VARCHAR(128)` | NO | — | The scanned or keyed identifier value. | — |
| `is_primary` | `BOOLEAN` | NO | `FALSE` | Indicates whether this is the default identifier used when scanning. | — |
| `is_active` | `BOOLEAN` | NO | `TRUE` | Indicates whether this master-data record is active; deactivated records are retained for history. | — |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp when this record was first created in the system. | — |

---

## network.inventory_locations

**Table description:** Physical sites (warehouses, stores, DCs) anchoring all stock balances and operations.

| Column | Data Type | Nullable | Default | Business Meaning | Related Entity |
|--------|-----------|----------|---------|------------------|----------------|
| `id` | `BIGINT` | NO | IDENTITY | System-generated unique identifier for this record. | — (primary key) |
| `location_code` | `VARCHAR(32)` | NO | — | Unique business identifier used in day-to-day operations. | Unique business key |
| `location_name` | `VARCHAR(256)` | NO | — | The human-readable name shown to users in screens and reports. | — |
| `location_type` | `VARCHAR(32)` | NO | — | Type of physical site (warehouse, store, or distribution point). | — |
| `parent_location_id` | `BIGINT` | YES | — | Optional reference to a parent location in the site hierarchy. | → `network.inventory_locations` (`id`) |
| `operational_status` | `VARCHAR(32)` | NO | `'ACTIVE'` | Operational status of the location. | — |
| `is_frozen` | `BOOLEAN` | NO | `FALSE` | Indicates the location is frozen and inventory movements are blocked during a physical count. | — |
| `address_line1` | `VARCHAR(256)` | YES | — | Primary street address line. | — |
| `address_line2` | `VARCHAR(256)` | YES | — | Secondary address line (suite, building, etc.). | — |
| `city` | `VARCHAR(128)` | YES | — | City name for the address. | — |
| `region_code` | `VARCHAR(32)` | YES | — | State, province, or regional code. | — |
| `postal_code` | `VARCHAR(16)` | YES | — | Postal or ZIP code for the address. | — |
| `country_code` | `CHAR(2)` | YES | — | Two-letter ISO country code. | — |
| `responsible_manager_id` | `BIGINT` | YES | — | The manager responsible for this location. | → `identity.user_accounts` (`id`) |
| `go_live_date` | `DATE` | YES | — | Date when the location became or will become operational. | — |
| `closure_plan` | `TEXT` | YES | — | Notes describing how inventory and operations will be handled when closing. | — |
| `is_active` | `BOOLEAN` | NO | `TRUE` | Indicates whether this master-data record is active; deactivated records are retained for history. | — |
| `version` | `INTEGER` | NO | 1 | Version counter incremented on each update to prevent conflicting concurrent edits. | — |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp when this record was first created in the system. | — |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp of the most recent update to this record. | — |

---

## network.storage_positions

**Table description:** Bin/zone/shelf addresses within a location for put-away and pick path.

| Column | Data Type | Nullable | Default | Business Meaning | Related Entity |
|--------|-----------|----------|---------|------------------|----------------|
| `id` | `BIGINT` | NO | IDENTITY | System-generated unique identifier for this record. | — (primary key) |
| `location_id` | `BIGINT` | NO | — | The inventory location this record pertains to. | → `network.inventory_locations` (`id`) |
| `position_code` | `VARCHAR(64)` | NO | — | Storage position code that is unique within its parent location. | — |
| `zone` | `VARCHAR(32)` | YES | — | Warehouse zone code for routing and organization. | — |
| `aisle` | `VARCHAR(32)` | YES | — | Aisle identifier within the warehouse. | — |
| `bin` | `VARCHAR(32)` | YES | — | Bin or shelf identifier completing the storage address. | — |
| `storage_type` | `VARCHAR(32)` | NO | `'BULK'` | Storage position type (bulk, pick face, quarantine, or bonded). | — |
| `capacity_units` | `NUMERIC(18,4)` | YES | — | Maximum quantity or capacity this position can hold, if defined. | — |
| `is_dedicated` | `BOOLEAN` | NO | `FALSE` | Indicates whether this position is reserved for a single product. | — |
| `dedicated_product_id` | `BIGINT` | YES | — | The product exclusively assigned to this storage position. | → `catalog.products` (`id`) |
| `is_active` | `BOOLEAN` | NO | `TRUE` | Indicates whether this master-data record is active; deactivated records are retained for history. | — |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp when this record was first created in the system. | — |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp of the most recent update to this record. | — |

---

## governance.governance_policies

**Table description:** Organization-wide approval thresholds, tolerances, and exception rules.

| Column | Data Type | Nullable | Default | Business Meaning | Related Entity |
|--------|-----------|----------|---------|------------------|----------------|
| `id` | `BIGINT` | NO | IDENTITY | System-generated unique identifier for this record. | — (primary key) |
| `policy_code` | `VARCHAR(64)` | NO | — | Business identifier. | Unique business key |
| `policy_name` | `VARCHAR(256)` | NO | — | The human-readable name shown to users in screens and reports. | — |
| `policy_type` | `VARCHAR(32)` | NO | — | Category of governance policy. | — |
| `threshold_value` | `NUMERIC(18,4)` | YES | — | Numeric limit that triggers the policy rule. | — |
| `threshold_currency` | `CHAR(3)` | YES | — | ISO currency code when the threshold is a monetary amount. | — |
| `applicable_scope` | `VARCHAR(64)` | YES | — | Scope to which this policy applies. | — |
| `approval_authority_role` | `VARCHAR(64)` | YES | — | Role authorized to approve actions under this policy. | — |
| `effective_from` | `TIMESTAMPTZ` | NO | — | Date and time when this policy version becomes effective. | — |
| `effective_to` | `TIMESTAMPTZ` | YES | — | Date and time when this policy expires; null means no end date. | — |
| `is_active` | `BOOLEAN` | NO | `TRUE` | Indicates whether this master-data record is active; deactivated records are retained for history. | — |
| `version` | `INTEGER` | NO | 1 | Version counter incremented on each update to prevent conflicting concurrent edits. | — |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp when this record was first created in the system. | — |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp of the most recent update to this record. | — |

---

## governance.reason_codes

**Table description:** Standardized categorized explanations for adjustments, write-offs, and discrepancies.

| Column | Data Type | Nullable | Default | Business Meaning | Related Entity |
|--------|-----------|----------|---------|------------------|----------------|
| `id` | `BIGINT` | NO | IDENTITY | System-generated unique identifier for this record. | — (primary key) |
| `reason_code` | `VARCHAR(32)` | NO | — | Unique business identifier used in day-to-day operations. | Unique business key |
| `description` | `VARCHAR(512)` | NO | — | Plain-language label describing this code or reason. | — |
| `category` | `VARCHAR(32)` | NO | — | Business category classifying the reason for the transaction. | — |
| `reporting_group` | `VARCHAR(64)` | YES | — | Group used to roll up this reason in management reports. | — |
| `approval_threshold_id` | `BIGINT` | YES | — | The governance policy defining the approval threshold for this reason. | → `governance.governance_policies` (`id`) |
| `is_active` | `BOOLEAN` | NO | `TRUE` | Retired codes set FALSE. | — |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp when this record was first created in the system. | — |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp of the most recent update to this record. | — |

---

## inventory.stock_positions

**Table description:** Authoritative on-hand, reserved, and ATP quantities per product per location — central quantity hub.

| Column | Data Type | Nullable | Default | Business Meaning | Related Entity |
|--------|-----------|----------|---------|------------------|----------------|
| `id` | `BIGINT` | NO | IDENTITY | System-generated unique identifier for this record. | — (primary key) |
| `product_id` | `BIGINT` | NO | — | The product this record pertains to. | → `catalog.products` (`id`) |
| `location_id` | `BIGINT` | NO | — | The inventory location this record pertains to. | → `network.inventory_locations` (`id`) |
| `on_hand_qty` | `NUMERIC(18,4)` | NO | 0 | Total physical quantity currently in stock at this location. | — |
| `reserved_qty` | `NUMERIC(18,4)` | NO | 0 | Quantity reserved and committed to customer orders. | — |
| `quarantined_qty` | `NUMERIC(18,4)` | NO | 0 | Quantity held in quarantine and not available for sale. | — |
| `atp_qty` | `NUMERIC(18,4)` | NO | 0 | Quantity available to promise to customers after reservations and holds. | — |
| `inbound_expected_qty` | `NUMERIC(18,4)` | NO | 0 | Expected inbound quantity not yet received (informational only). | — |
| `stock_status` | `VARCHAR(32)` | NO | `'IN_STOCK'` | Derived stock health status for monitoring and alerts. | — |
| `ownership_type` | `VARCHAR(32)` | NO | `'OWNED'` | Ownership classification of the stock at this position. | — |
| `last_movement_at` | `TIMESTAMPTZ` | YES | — | Timestamp of the most recent quantity change at this position. | — |
| `version` | `INTEGER` | NO | 1 | Version counter critical for preventing lost updates during concurrent stock reservations. | — |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp when this record was first created in the system. | — |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp of the most recent update to this record. | — |

---

## inventory.lot_batches

**Table description:** Traceable lot/batch identity with shelf-life attributes for FEFO and recall.

| Column | Data Type | Nullable | Default | Business Meaning | Related Entity |
|--------|-----------|----------|---------|------------------|----------------|
| `id` | `BIGINT` | NO | IDENTITY | System-generated unique identifier for this record. | — (primary key) |
| `stock_position_id` | `BIGINT` | NO | — | The stock position (product at location) this record affects. | → `inventory.stock_positions` (`id`) |
| `product_id` | `BIGINT` | NO | — | The product this record pertains to. | → `catalog.products` (`id`) (denormalized) |
| `lot_number` | `VARCHAR(64)` | NO | — | Business lot or batch number for traceability. | — |
| `quantity` | `NUMERIC(18,4)` | NO | 0 | Quantity of this specific lot held at the stock position. | — |
| `expiration_date` | `DATE` | YES | — | Expiration date for shelf-life products in this lot. | — |
| `manufacture_date` | `DATE` | YES | — | Date the product in this lot was manufactured. | — |
| `receipt_date` | `DATE` | YES | — | Date this lot was first received into inventory. | — |
| `quality_status` | `VARCHAR(32)` | NO | `'ACCEPTED'` | Quality status of this lot (accepted, on hold, or rejected). | — |
| `supplier_id` | `BIGINT` | YES | — | The supplier associated with this record. | → `procurement.suppliers` (`id`) |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp when this record was first created in the system. | — |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp of the most recent update to this record. | — |

---

## inventory.quarantine_holds

**Table description:** Holds removing quantity from ATP for quality, regulatory, recall, or customs reasons.

| Column | Data Type | Nullable | Default | Business Meaning | Related Entity |
|--------|-----------|----------|---------|------------------|----------------|
| `id` | `BIGINT` | NO | IDENTITY | System-generated unique identifier for this record. | — (primary key) |
| `hold_reference` | `VARCHAR(64)` | NO | — | Human-readable reference number assigned to this transaction. | — |
| `stock_position_id` | `BIGINT` | NO | — | The stock position (product at location) this record affects. | → `inventory.stock_positions` (`id`) |
| `lot_batch_id` | `BIGINT` | YES | — | The lot or batch this record references, when applicable. | → `inventory.lot_batches` (`id`) |
| `held_qty` | `NUMERIC(18,4)` | NO | — | Quantity currently blocked from available-to-promise by this hold. | — |
| `hold_type` | `VARCHAR(32)` | NO | — | Category of quarantine hold. | — |
| `hold_reason` | `TEXT` | NO | — | Business justification explaining why stock is held. | — |
| `hold_status` | `VARCHAR(32)` | NO | `'ACTIVE'` | Current status of the quarantine hold. | — |
| `hold_start_at` | `TIMESTAMPTZ` | NO | `NOW()` | Date and time when the hold became effective. | — |
| `expected_resolution_at` | `TIMESTAMPTZ` | YES | — | Expected date when the hold will be resolved. | — |
| `released_at` | `TIMESTAMPTZ` | YES | — | Date and time when the hold was actually released. | — |
| `disposition_outcome` | `VARCHAR(32)` | YES | — | Final disposition outcome when the hold is resolved. | — |
| `authorized_by` | `BIGINT` | YES | — | The user who authorized this action. | → `identity.user_accounts` (`id`) |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp when this record was first created in the system. | — |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp of the most recent update to this record. | — |

---

## inventory.stock_policies

**Table description:** Replenishment thresholds per product per location.

| Column | Data Type | Nullable | Default | Business Meaning | Related Entity |
|--------|-----------|----------|---------|------------------|----------------|
| `id` | `BIGINT` | NO | IDENTITY | System-generated unique identifier for this record. | — (primary key) |
| `product_id` | `BIGINT` | NO | — | The product this record pertains to. | → `catalog.products` (`id`) |
| `location_id` | `BIGINT` | NO | — | The inventory location this record pertains to. | → `network.inventory_locations` (`id`) |
| `reorder_level` | `NUMERIC(18,4)` | NO | 0 | Available-to-promise level that triggers a replenishment request. | — |
| `minimum_threshold` | `NUMERIC(18,4)` | NO | 0 | Minimum acceptable stock level before urgent action is required. | — |
| `safety_stock_qty` | `NUMERIC(18,4)` | NO | 0 | Extra buffer quantity maintained above minimum to absorb demand variability. | — |
| `maximum_stock_level` | `NUMERIC(18,4)` | YES | — | Maximum stock level above which the position is considered overstocked. | — |
| `lead_time_days` | `INTEGER` | YES | — | Expected number of days from order to receipt for replenishment planning. | — |
| `review_frequency_days` | `INTEGER` | YES | — | How often replenishment parameters are reviewed, in days. | — |
| `effective_from` | `TIMESTAMPTZ` | NO | `NOW()` | Date from which the current threshold values are effective. | — |
| `exception_approval_ref` | `VARCHAR(64)` | YES | — | Reference documenting an approved exception to standard thresholds. | — |
| `version` | `INTEGER` | NO | 1 | Version counter incremented on each update to prevent conflicting concurrent edits. | — |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp when this record was first created in the system. | — |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp of the most recent update to this record. | — |

---

## inventory.stock_policy_history

**Table description:** Immutable history of threshold changes for audit and replenishment analysis.

| Column | Data Type | Nullable | Default | Business Meaning | Related Entity |
|--------|-----------|----------|---------|------------------|----------------|
| `id` | `BIGINT` | NO | IDENTITY | System-generated unique identifier for this record. | — (primary key) |
| `stock_policy_id` | `BIGINT` | NO | — | The stock policy whose historical values are captured here. | → `inventory.stock_policies` (`id`) |
| `reorder_level` | `NUMERIC(18,4)` | NO | — | Reorder level that was in effect during this historical period. | — |
| `minimum_threshold` | `NUMERIC(18,4)` | NO | — | Minimum threshold in effect during this historical period. | — |
| `safety_stock_qty` | `NUMERIC(18,4)` | NO | — | Safety stock quantity in effect during this historical period. | — |
| `effective_from` | `TIMESTAMPTZ` | NO | — | Start of the period when these threshold values were effective. | — |
| `effective_to` | `TIMESTAMPTZ` | NO | — | End of the period when these threshold values were effective. | — |
| `changed_by` | `BIGINT` | YES | — | The user who made this policy change. | → `identity.user_accounts` (`id`) |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp when this record was first created in the system. | — |

---

## procurement.suppliers

**Table description:** External vendor master for procurement, receipt, and payment.

| Column | Data Type | Nullable | Default | Business Meaning | Related Entity |
|--------|-----------|----------|---------|------------------|----------------|
| `id` | `BIGINT` | NO | IDENTITY | System-generated unique identifier for this record. | — (primary key) |
| `supplier_code` | `VARCHAR(32)` | NO | — | Unique business identifier used in day-to-day operations. | Unique business key |
| `supplier_name` | `VARCHAR(256)` | NO | — | Legal or commonly used display name of the supplier. | — |
| `contact_name` | `VARCHAR(128)` | YES | — | Name of the primary contact person. | — |
| `contact_email` | `VARCHAR(256)` | YES | — | Email address for contacting this person or organization. | — |
| `contact_phone` | `VARCHAR(32)` | YES | — | Telephone number for contacting this person or organization. | — |
| `payment_terms_days` | `INTEGER` | NO | 30 | Number of days until payment is due (net terms). | — |
| `default_lead_time_days` | `INTEGER` | YES | — | Supplier's typical lead time in days for purchase orders. | — |
| `is_consignment` | `BOOLEAN` | NO | `FALSE` | Indicates whether stock from this supplier is held on consignment. | — |
| `delivery_rating` | `NUMERIC(3,2)` | YES | — | Supplier delivery performance rating on a zero-to-five scale. | — |
| `is_active` | `BOOLEAN` | NO | `TRUE` | Indicates whether this master-data record is active; deactivated records are retained for history. | — |
| `version` | `INTEGER` | NO | 1 | Version counter incremented on each update to prevent conflicting concurrent edits. | — |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp when this record was first created in the system. | — |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp of the most recent update to this record. | — |

---

## procurement.purchase_requisitions

**Table description:** Internal replenishment request with approval workflow before PO creation.

| Column | Data Type | Nullable | Default | Business Meaning | Related Entity |
|--------|-----------|----------|---------|------------------|----------------|
| `id` | `BIGINT` | NO | IDENTITY | System-generated unique identifier for this record. | — (primary key) |
| `requisition_number` | `VARCHAR(64)` | NO | — | Unique business identifier used in day-to-day operations. | Unique business key |
| `requesting_location_id` | `BIGINT` | NO | — | The location requesting replenishment on this requisition. | → `network.inventory_locations` (`id`) |
| `requested_delivery_date` | `DATE` | YES | — | Date by which delivery is requested. | — |
| `triggering_alert_id` | `BIGINT` | YES | — | The operational alert that triggered this requisition, if applicable. | → `audit.operational_alerts` (`id`) |
| `approval_status` | `VARCHAR(32)` | NO | `'DRAFT'` | Approval workflow status of the requisition. | — |
| `approved_by` | `BIGINT` | YES | — | The user who approved this record or transaction. | → `identity.user_accounts` (`id`) |
| `approved_at` | `TIMESTAMPTZ` | YES | — | Date and time when approval was granted. | — |
| `purchase_order_id` | `BIGINT` | YES | — | The purchase order linked to this invoice or receipt. | → `procurement.purchase_orders` (`id`) |
| `version` | `INTEGER` | NO | 1 | Version counter incremented on each update to prevent conflicting concurrent edits. | — |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp when this record was first created in the system. | — |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp of the most recent update to this record. | — |
| `created_by` | `BIGINT` | NO | — | The user who created this record. | → `identity.user_accounts` (`id`) |

---

## procurement.purchase_requisition_lines

**Table description:** Line-level product and quantity on a purchase requisition.

| Column | Data Type | Nullable | Default | Business Meaning | Related Entity |
|--------|-----------|----------|---------|------------------|----------------|
| `id` | `BIGINT` | NO | IDENTITY | System-generated unique identifier for this record. | — (primary key) |
| `requisition_id` | `BIGINT` | NO | — | The purchase requisition this line belongs to. | → `procurement.purchase_requisitions` (`id`) |
| `line_number` | `INTEGER` | NO | — | Line sequence number within the parent purchase requisition. | — |
| `product_id` | `BIGINT` | NO | — | The product this record pertains to. | → `catalog.products` (`id`) |
| `requested_qty` | `NUMERIC(18,4)` | NO | — | Quantity requested on this requisition line; must be greater than zero. | — |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp when this record was first created in the system. | — |

---

## procurement.purchase_orders

**Table description:** Authorized commercial commitment to a supplier.

| Column | Data Type | Nullable | Default | Business Meaning | Related Entity |
|--------|-----------|----------|---------|------------------|----------------|
| `id` | `BIGINT` | NO | IDENTITY | System-generated unique identifier for this record. | — (primary key) |
| `po_number` | `VARCHAR(64)` | NO | — | Unique business identifier used in day-to-day operations. | Unique business key |
| `supplier_id` | `BIGINT` | NO | — | The supplier associated with this record. | → `procurement.suppliers` (`id`) |
| `receiving_location_id` | `BIGINT` | NO | — | The location where goods will be or were received. | → `network.inventory_locations` (`id`) |
| `order_date` | `DATE` | NO | — | Calendar date the purchase order was created. | — |
| `expected_delivery_date` | `DATE` | YES | — | Expected date when in-transit stock will arrive. | — |
| `po_status` | `VARCHAR(32)` | NO | `'OPEN'` | Fulfillment status of the purchase order. | — |
| `total_commitment_amount` | `NUMERIC(18,2)` | NO | 0 | Total committed monetary value of the purchase order. | — |
| `currency_code` | `CHAR(3)` | NO | `'USD'` | ISO 4217 three-letter currency code. | — |
| `payment_terms_days` | `INTEGER` | NO | 30 | Payment terms copied from the supplier master at PO creation. | — |
| `version` | `INTEGER` | NO | 1 | Version counter incremented on each update to prevent conflicting concurrent edits. | — |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp when this record was first created in the system. | — |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp of the most recent update to this record. | — |
| `created_by` | `BIGINT` | NO | — | The user who created this record. | → `identity.user_accounts` (`id`) |

---

## procurement.purchase_order_lines

**Table description:** Product, quantity, and price lines on a purchase order.

| Column | Data Type | Nullable | Default | Business Meaning | Related Entity |
|--------|-----------|----------|---------|------------------|----------------|
| `id` | `BIGINT` | NO | IDENTITY | System-generated unique identifier for this record. | — (primary key) |
| `purchase_order_id` | `BIGINT` | NO | — | The purchase order linked to this invoice or receipt. | → `procurement.purchase_orders` (`id`) |
| `line_number` | `INTEGER` | NO | — | Line sequence number within the parent purchase order. | — |
| `product_id` | `BIGINT` | NO | — | The product this record pertains to. | → `catalog.products` (`id`) |
| `ordered_qty` | `NUMERIC(18,4)` | NO | — | Quantity the customer ordered on this line. | — |
| `received_qty` | `NUMERIC(18,4)` | NO | 0 | Total quantity received to date against this PO line. | — |
| `unit_price` | `NUMERIC(18,4)` | NO | — | Unit price per unit of measure on this line. | — |
| `line_amount` | `NUMERIC(18,2)` | NO | — | Line total calculated as quantity times unit price. | — |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp when this record was first created in the system. | — |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp of the most recent update to this record. | — |

---

## procurement.expected_inbound_deliveries

**Table description:** Planned supplier shipment schedule tied to a purchase order.

| Column | Data Type | Nullable | Default | Business Meaning | Related Entity |
|--------|-----------|----------|---------|------------------|----------------|
| `id` | `BIGINT` | NO | IDENTITY | System-generated unique identifier for this record. | — (primary key) |
| `delivery_reference` | `VARCHAR(64)` | NO | — | Unique business identifier used in day-to-day operations. | Unique business key |
| `purchase_order_id` | `BIGINT` | NO | — | The purchase order linked to this invoice or receipt. | → `procurement.purchase_orders` (`id`) |
| `expected_arrival_date` | `DATE` | NO | — | Planned arrival date for this inbound delivery. | — |
| `carrier_reference` | `VARCHAR(128)` | YES | — | Carrier tracking or shipment reference number. | — |
| `shipment_status` | `VARCHAR(32)` | NO | `'PLANNED'` | Status of the planned inbound shipment. | — |
| `receiving_location_id` | `BIGINT` | NO | — | The location where goods will be or were received. | → `network.inventory_locations` (`id`) |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp when this record was first created in the system. | — |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp of the most recent update to this record. | — |

---

## procurement.expected_inbound_delivery_lines

**Table description:** Expected quantity by product on an inbound delivery plan.

| Column | Data Type | Nullable | Default | Business Meaning | Related Entity |
|--------|-----------|----------|---------|------------------|----------------|
| `id` | `BIGINT` | NO | IDENTITY | System-generated unique identifier for this record. | — (primary key) |
| `delivery_id` | `BIGINT` | NO | — | The expected inbound delivery this line belongs to. | → `procurement.expected_inbound_deliveries` (`id`) |
| `purchase_order_line_id` | `BIGINT` | NO | — | The purchase order line this record is linked to. | → `procurement.purchase_order_lines` (`id`) |
| `product_id` | `BIGINT` | NO | — | The product this record pertains to. | → `catalog.products` (`id`) |
| `expected_qty` | `NUMERIC(18,4)` | NO | — | Quantity that was expected to be received. | — |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp when this record was first created in the system. | — |

---

## inbound.goods_receipts

**Table description:** Verified acceptance of inbound supplier goods at receiving dock.

| Column | Data Type | Nullable | Default | Business Meaning | Related Entity |
|--------|-----------|----------|---------|------------------|----------------|
| `id` | `BIGINT` | NO | IDENTITY | System-generated unique identifier for this record. | — (primary key) |
| `gr_number` | `VARCHAR(64)` | NO | — | Unique business identifier used in day-to-day operations. | Unique business key |
| `purchase_order_id` | `BIGINT` | YES | — | The purchase order linked to this invoice or receipt. | → `procurement.purchase_orders` (`id`) |
| `exception_authorization_ref` | `VARCHAR(64)` | YES | — | Authorization reference for receiving without a matching purchase order. | — |
| `supplier_id` | `BIGINT` | NO | — | The supplier associated with this record. | → `procurement.suppliers` (`id`) |
| `receiving_location_id` | `BIGINT` | NO | — | The location where goods will be or were received. | → `network.inventory_locations` (`id`) |
| `receipt_date` | `TIMESTAMPTZ` | NO | `NOW()` | Date and time when goods were received at the dock. | — |
| `verification_status` | `VARCHAR(32)` | NO | `'PENDING'` | Verification status of the goods receipt. | — |
| `receiving_clerk_id` | `BIGINT` | NO | — | The receiving clerk who processed this receipt. | → `identity.user_accounts` (`id`) |
| `version` | `INTEGER` | NO | 1 | Version counter incremented on each update to prevent conflicting concurrent edits. | — |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp when this record was first created in the system. | — |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp of the most recent update to this record. | — |

---

## inbound.goods_receipt_lines

**Table description:** Line-level received product, quantity, and condition.

| Column | Data Type | Nullable | Default | Business Meaning | Related Entity |
|--------|-----------|----------|---------|------------------|----------------|
| `id` | `BIGINT` | NO | IDENTITY | System-generated unique identifier for this record. | — (primary key) |
| `goods_receipt_id` | `BIGINT` | NO | — | The goods receipt this record belongs to. | → `inbound.goods_receipts` (`id`) |
| `line_number` | `INTEGER` | NO | — | Line sequence number within the parent goods receipt. | — |
| `purchase_order_line_id` | `BIGINT` | YES | — | The purchase order line this record is linked to. | → `procurement.purchase_order_lines` (`id`) |
| `product_id` | `BIGINT` | NO | — | The product this record pertains to. | → `catalog.products` (`id`) |
| `received_qty` | `NUMERIC(18,4)` | NO | — | Quantity physically received on this line. | — |
| `accepted_qty` | `NUMERIC(18,4)` | NO | 0 | Quantity accepted into inventory after quality verification. | — |
| `condition_grade` | `VARCHAR(32)` | NO | `'GOOD'` | Physical condition grade of received goods. | — |
| `lot_batch_id` | `BIGINT` | YES | — | The lot or batch this record references, when applicable. | → `inventory.lot_batches` (`id`) |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp when this record was first created in the system. | — |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp of the most recent update to this record. | — |

---

## inbound.receipt_discrepancies

**Table description:** Documented variance between expected and actual receipt.

| Column | Data Type | Nullable | Default | Business Meaning | Related Entity |
|--------|-----------|----------|---------|------------------|----------------|
| `id` | `BIGINT` | NO | IDENTITY | System-generated unique identifier for this record. | — (primary key) |
| `discrepancy_reference` | `VARCHAR(64)` | NO | — | Unique business identifier used in day-to-day operations. | Unique business key |
| `goods_receipt_id` | `BIGINT` | NO | — | The goods receipt this record belongs to. | → `inbound.goods_receipts` (`id`) |
| `goods_receipt_line_id` | `BIGINT` | YES | — | The goods receipt line this record belongs to. | → `inbound.goods_receipt_lines` (`id`) |
| `discrepancy_type` | `VARCHAR(32)` | NO | — | Type of discrepancy between expected and actual receipt. | — |
| `expected_qty` | `NUMERIC(18,4)` | YES | — | Quantity that was expected to be received. | — |
| `actual_qty` | `NUMERIC(18,4)` | YES | — | Quantity that was actually received. | — |
| `product_id` | `BIGINT` | NO | — | The product this record pertains to. | → `catalog.products` (`id`) |
| `reason_code_id` | `BIGINT` | YES | — | The standardized reason code explaining this transaction. | → `governance.reason_codes` (`id`) |
| `evidence_notes` | `TEXT` | YES | — | Notes or references supporting the discrepancy investigation. | — |
| `resolution_status` | `VARCHAR(32)` | NO | `'OPEN'` | Resolution status of the receipt discrepancy. | — |
| `resolution_outcome` | `VARCHAR(64)` | YES | — | Description of how the discrepancy was resolved. | — |
| `supplier_claim_ref` | `VARCHAR(64)` | YES | — | Reference number for a claim filed with the supplier. | — |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp when this record was first created in the system. | — |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp of the most recent update to this record. | — |

---

## inbound.put_aways

**Table description:** Confirmation of stock placement from dock to storage — triggers ATP availability.

| Column | Data Type | Nullable | Default | Business Meaning | Related Entity |
|--------|-----------|----------|---------|------------------|----------------|
| `id` | `BIGINT` | NO | IDENTITY | System-generated unique identifier for this record. | — (primary key) |
| `put_away_reference` | `VARCHAR(64)` | NO | — | Unique business identifier used in day-to-day operations. | Unique business key |
| `goods_receipt_id` | `BIGINT` | NO | — | The goods receipt this record belongs to. | → `inbound.goods_receipts` (`id`) |
| `goods_receipt_line_id` | `BIGINT` | NO | — | The goods receipt line this record belongs to. | → `inbound.goods_receipt_lines` (`id`) |
| `product_id` | `BIGINT` | NO | — | The product this record pertains to. | → `catalog.products` (`id`) |
| `quantity` | `NUMERIC(18,4)` | NO | — | Quantity moved from receiving dock to storage. | — |
| `from_area` | `VARCHAR(64)` | NO | `'RECEIVING_DOCK'` | Area from which stock was moved (typically receiving dock). | — |
| `storage_position_id` | `BIGINT` | NO | — | The storage position (bin/shelf) where stock is or was located. | → `network.storage_positions` (`id`) |
| `lot_batch_id` | `BIGINT` | YES | — | The lot or batch this record references, when applicable. | → `inventory.lot_batches` (`id`) |
| `put_away_at` | `TIMESTAMPTZ` | NO | `NOW()` | Date and time when put-away was completed. | — |
| `availability_effective_at` | `TIMESTAMPTZ` | NO | `NOW()` | Date and time from which stock becomes available to promise after put-away. | — |
| `performed_by` | `BIGINT` | NO | — | The user who performed this inventory movement. | → `identity.user_accounts` (`id`) |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp when this record was first created in the system. | — |

---

## finance.supplier_invoices

**Table description:** Supplier billing document for three-way match and payment authorization.

| Column | Data Type | Nullable | Default | Business Meaning | Related Entity |
|--------|-----------|----------|---------|------------------|----------------|
| `id` | `BIGINT` | NO | IDENTITY | System-generated unique identifier for this record. | — (primary key) |
| `invoice_number` | `VARCHAR(64)` | NO | — | Invoice number as printed on the supplier's billing document. | — |
| `supplier_id` | `BIGINT` | NO | — | The supplier associated with this record. | → `procurement.suppliers` (`id`) |
| `purchase_order_id` | `BIGINT` | NO | — | The purchase order linked to this invoice or receipt. | → `procurement.purchase_orders` (`id`) |
| `invoice_date` | `DATE` | NO | — | Date printed on the supplier invoice. | — |
| `total_amount` | `NUMERIC(18,2)` | NO | — | Total amount billed on the supplier invoice. | — |
| `currency_code` | `CHAR(3)` | NO | `'USD'` | ISO 4217 three-letter currency code. | — |
| `match_status` | `VARCHAR(32)` | NO | `'PENDING'` | Three-way match status for the invoice. | — |
| `tolerance_variance` | `NUMERIC(18,2)` | YES | — | Monetary variance within approved tolerance during invoice matching. | — |
| `payment_status` | `VARCHAR(32)` | NO | `'UNAUTHORIZED'` | Payment authorization and settlement status. | — |
| `version` | `INTEGER` | NO | 1 | Version counter incremented on each update to prevent conflicting concurrent edits. | — |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp when this record was first created in the system. | — |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp of the most recent update to this record. | — |

---

## finance.supplier_invoice_lines

**Table description:** Billed product, quantity, and price for three-way match.

| Column | Data Type | Nullable | Default | Business Meaning | Related Entity |
|--------|-----------|----------|---------|------------------|----------------|
| `id` | `BIGINT` | NO | IDENTITY | System-generated unique identifier for this record. | — (primary key) |
| `supplier_invoice_id` | `BIGINT` | NO | — | The supplier invoice this record belongs to. | → `finance.supplier_invoices` (`id`) |
| `line_number` | `INTEGER` | NO | — | Line sequence number within the parent supplier invoice. | — |
| `purchase_order_line_id` | `BIGINT` | YES | — | The purchase order line this record is linked to. | → `procurement.purchase_order_lines` (`id`) |
| `product_id` | `BIGINT` | NO | — | The product this record pertains to. | → `catalog.products` (`id`) |
| `billed_qty` | `NUMERIC(18,4)` | NO | — | Quantity billed by the supplier on this invoice line. | — |
| `unit_price` | `NUMERIC(18,4)` | NO | — | Unit price billed by the supplier on this line. | — |
| `line_amount` | `NUMERIC(18,2)` | NO | — | Extended monetary amount for this invoice line. | — |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp when this record was first created in the system. | — |

---

## finance.invoice_goods_receipt_match

**Table description:** Associative link between supplier invoices and goods receipts for three-way match (BR-008).

| Column | Data Type | Nullable | Default | Business Meaning | Related Entity |
|--------|-----------|----------|---------|------------------|----------------|
| `id` | `BIGINT` | NO | IDENTITY | System-generated unique identifier for this record. | — (primary key) |
| `supplier_invoice_id` | `BIGINT` | NO | — | The supplier invoice this record belongs to. | → `finance.supplier_invoices` (`id`) |
| `goods_receipt_id` | `BIGINT` | NO | — | The goods receipt this record belongs to. | → `inbound.goods_receipts` (`id`) |
| `match_status` | `VARCHAR(32)` | NO | `'PENDING'` | Three-way match status for the invoice. | — |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp when this record was first created in the system. | — |

---

## fulfillment.customer_orders

**Table description:** Customer demand document driving reservation, pick, and ship.

| Column | Data Type | Nullable | Default | Business Meaning | Related Entity |
|--------|-----------|----------|---------|------------------|----------------|
| `id` | `BIGINT` | NO | IDENTITY | System-generated unique identifier for this record. | — (primary key) |
| `order_number` | `VARCHAR(64)` | NO | — | Unique business identifier used in day-to-day operations. | Unique business key |
| `customer_reference` | `VARCHAR(128)` | YES | — | Customer identifier from an external sales or CRM system. | — |
| `order_date` | `TIMESTAMPTZ` | NO | `NOW()` | Date and time when the customer placed the order. | — |
| `requested_delivery_date` | `DATE` | YES | — | Delivery date requested by the customer. | — |
| `order_status` | `VARCHAR(32)` | NO | `'DRAFT'` | Overall fulfillment status of the customer order. | — |
| `channel` | `VARCHAR(32)` | YES | — | Sales channel through which the order was placed. | — |
| `version` | `INTEGER` | NO | 1 | Version counter incremented on each update to prevent conflicting concurrent edits. | — |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp when this record was first created in the system. | — |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp of the most recent update to this record. | — |

---

## fulfillment.customer_order_lines

**Table description:** Order line product, requested, fulfilled, and backordered quantities.

| Column | Data Type | Nullable | Default | Business Meaning | Related Entity |
|--------|-----------|----------|---------|------------------|----------------|
| `id` | `BIGINT` | NO | IDENTITY | System-generated unique identifier for this record. | — (primary key) |
| `customer_order_id` | `BIGINT` | NO | — | The customer order this record belongs to. | → `fulfillment.customer_orders` (`id`) |
| `line_number` | `INTEGER` | NO | — | Line sequence number within the parent customer order. | — |
| `product_id` | `BIGINT` | NO | — | The product this record pertains to. | → `catalog.products` (`id`) |
| `requested_qty` | `NUMERIC(18,4)` | NO | — | Quantity the customer ordered on this line. | — |
| `fulfilled_qty` | `NUMERIC(18,4)` | NO | 0 | Quantity shipped to the customer on this line to date. | — |
| `backordered_qty` | `NUMERIC(18,4)` | NO | 0 | Quantity not yet fulfilled and held as a backorder. | — |
| `fulfillment_location_id` | `BIGINT` | YES | — | The warehouse location fulfilling this order line or execution. | → `network.inventory_locations` (`id`) |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp when this record was first created in the system. | — |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp of the most recent update to this record. | — |

---

## fulfillment.inventory_reservations

**Table description:** ATP hold for confirmed order lines until ship or release.

| Column | Data Type | Nullable | Default | Business Meaning | Related Entity |
|--------|-----------|----------|---------|------------------|----------------|
| `id` | `BIGINT` | NO | IDENTITY | System-generated unique identifier for this record. | — (primary key) |
| `reservation_reference` | `VARCHAR(64)` | NO | — | Unique business identifier used in day-to-day operations. | Unique business key |
| `customer_order_id` | `BIGINT` | NO | — | The customer order this record belongs to. | → `fulfillment.customer_orders` (`id`) |
| `order_line_id` | `BIGINT` | NO | — | The customer order line this record belongs to. | → `fulfillment.customer_order_lines` (`id`) |
| `product_id` | `BIGINT` | NO | — | The product this record pertains to. | → `catalog.products` (`id`) |
| `location_id` | `BIGINT` | NO | — | The inventory location this record pertains to. | → `network.inventory_locations` (`id`) |
| `stock_position_id` | `BIGINT` | NO | — | The stock position (product at location) this record affects. | → `inventory.stock_positions` (`id`) |
| `reserved_qty` | `NUMERIC(18,4)` | NO | — | Quantity currently reserved against available stock. | — |
| `reservation_status` | `VARCHAR(32)` | NO | `'ACTIVE'` | Status of the inventory reservation. | — |
| `reserved_at` | `TIMESTAMPTZ` | NO | `NOW()` | Date and time when stock was reserved. | — |
| `expires_at` | `TIMESTAMPTZ` | YES | — | Optional date and time when the reservation expires if not fulfilled. | — |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp when this record was first created in the system. | — |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp of the most recent update to this record. | — |

---

## fulfillment.fulfillment_executions

**Table description:** Pick/pack/verify warehouse work unit for an order.

| Column | Data Type | Nullable | Default | Business Meaning | Related Entity |
|--------|-----------|----------|---------|------------------|----------------|
| `id` | `BIGINT` | NO | IDENTITY | System-generated unique identifier for this record. | — (primary key) |
| `fulfillment_reference` | `VARCHAR(64)` | NO | — | Unique business identifier used in day-to-day operations. | Unique business key |
| `customer_order_id` | `BIGINT` | NO | — | The customer order this record belongs to. | → `fulfillment.customer_orders` (`id`) |
| `fulfillment_location_id` | `BIGINT` | NO | — | The warehouse location fulfilling this order line or execution. | → `network.inventory_locations` (`id`) |
| `pick_verification_status` | `VARCHAR(32)` | NO | `'PENDING'` | Pick verification status for this fulfillment execution. | — |
| `pack_confirmed` | `BOOLEAN` | NO | `FALSE` | Indicates whether packing has been confirmed. | — |
| `assigned_picker_id` | `BIGINT` | YES | — | The warehouse picker assigned to this fulfillment task. | → `identity.user_accounts` (`id`) |
| `has_exception` | `BOOLEAN` | NO | `FALSE` | Indicates whether an exception occurred during fulfillment. | — |
| `pick_completed_at` | `TIMESTAMPTZ` | YES | — | Date and time when picking was completed. | — |
| `version` | `INTEGER` | NO | 1 | Version counter incremented on each update to prevent conflicting concurrent edits. | — |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp when this record was first created in the system. | — |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp of the most recent update to this record. | — |

---

## fulfillment.fulfillment_pick_lines

**Table description:** Individual pick line with lot attribution and verification.

| Column | Data Type | Nullable | Default | Business Meaning | Related Entity |
|--------|-----------|----------|---------|------------------|----------------|
| `id` | `BIGINT` | NO | IDENTITY | System-generated unique identifier for this record. | — (primary key) |
| `fulfillment_execution_id` | `BIGINT` | NO | — | The fulfillment execution (pick/pack unit) this record belongs to. | → `fulfillment.fulfillment_executions` (`id`) |
| `order_line_id` | `BIGINT` | NO | — | The customer order line this record belongs to. | → `fulfillment.customer_order_lines` (`id`) |
| `product_id` | `BIGINT` | NO | — | The product this record pertains to. | → `catalog.products` (`id`) |
| `requested_qty` | `NUMERIC(18,4)` | NO | — | Quantity the picker is instructed to retrieve. | — |
| `picked_qty` | `NUMERIC(18,4)` | NO | 0 | Quantity actually picked by the warehouse operator. | — |
| `storage_position_id` | `BIGINT` | YES | — | The storage position (bin/shelf) where stock is or was located. | → `network.storage_positions` (`id`) |
| `lot_batch_id` | `BIGINT` | YES | — | The lot or batch this record references, when applicable. | → `inventory.lot_batches` (`id`) |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp when this record was first created in the system. | — |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp of the most recent update to this record. | — |

---

## fulfillment.backorders

**Table description:** Customer-agreed delay for unfulfilled order line quantity.

| Column | Data Type | Nullable | Default | Business Meaning | Related Entity |
|--------|-----------|----------|---------|------------------|----------------|
| `id` | `BIGINT` | NO | IDENTITY | System-generated unique identifier for this record. | — (primary key) |
| `backorder_reference` | `VARCHAR(64)` | NO | — | Unique business identifier used in day-to-day operations. | Unique business key |
| `customer_order_id` | `BIGINT` | NO | — | The customer order this record belongs to. | → `fulfillment.customer_orders` (`id`) |
| `order_line_id` | `BIGINT` | NO | — | The customer order line this record belongs to. | → `fulfillment.customer_order_lines` (`id`) |
| `product_id` | `BIGINT` | NO | — | The product this record pertains to. | → `catalog.products` (`id`) |
| `backordered_qty` | `NUMERIC(18,4)` | NO | — | Quantity not yet fulfilled and held as a backorder. | — |
| `customer_acknowledged` | `BOOLEAN` | NO | `FALSE` | Indicates the customer has acknowledged the backorder delay. | — |
| `acknowledged_at` | `TIMESTAMPTZ` | YES | — | Date and time when the customer acknowledged the backorder. | — |
| `expected_fulfillment_date` | `DATE` | YES | — | Expected date when the backordered quantity will ship. | — |
| `backorder_reason` | `VARCHAR(64)` | YES | — | Short code explaining why the line is backordered. | — |
| `resolution_status` | `VARCHAR(32)` | NO | `'OPEN'` | Resolution status of the backorder. | — |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp when this record was first created in the system. | — |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp of the most recent update to this record. | — |

---

## fulfillment.shipments

**Table description:** Confirmed dispatch deducting on-hand and consuming reservations.

| Column | Data Type | Nullable | Default | Business Meaning | Related Entity |
|--------|-----------|----------|---------|------------------|----------------|
| `id` | `BIGINT` | NO | IDENTITY | System-generated unique identifier for this record. | — (primary key) |
| `shipment_number` | `VARCHAR(64)` | NO | — | Unique business identifier used in day-to-day operations. | Unique business key |
| `customer_order_id` | `BIGINT` | NO | — | The customer order this record belongs to. | → `fulfillment.customer_orders` (`id`) |
| `fulfillment_execution_id` | `BIGINT` | NO | — | The fulfillment execution (pick/pack unit) this record belongs to. | → `fulfillment.fulfillment_executions` (`id`) |
| `ship_from_location_id` | `BIGINT` | NO | — | The location from which this shipment was dispatched. | → `network.inventory_locations` (`id`) |
| `ship_date` | `TIMESTAMPTZ` | NO | `NOW()` | Date and time when goods were dispatched for transfer. | — |
| `carrier_reference` | `VARCHAR(128)` | YES | — | Name or code of the shipping carrier. | — |
| `tracking_identifier` | `VARCHAR(128)` | YES | — | Carrier tracking number for shipment visibility. | — |
| `shipment_status` | `VARCHAR(32)` | NO | `'DISPATCHED'` | Shipment delivery status. | — |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp when this record was first created in the system. | — |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp of the most recent update to this record. | — |

---

## fulfillment.shipment_lines

**Table description:** Shipped product, quantity, and lot per shipment.

| Column | Data Type | Nullable | Default | Business Meaning | Related Entity |
|--------|-----------|----------|---------|------------------|----------------|
| `id` | `BIGINT` | NO | IDENTITY | System-generated unique identifier for this record. | — (primary key) |
| `shipment_id` | `BIGINT` | NO | — | The shipment this line belongs to. | → `fulfillment.shipments` (`id`) |
| `order_line_id` | `BIGINT` | NO | — | The customer order line this record belongs to. | → `fulfillment.customer_order_lines` (`id`) |
| `product_id` | `BIGINT` | NO | — | The product this record pertains to. | → `catalog.products` (`id`) |
| `shipped_qty` | `NUMERIC(18,4)` | NO | — | Quantity shipped to the customer on this line to date. | — |
| `lot_batch_id` | `BIGINT` | YES | — | The lot or batch this record references, when applicable. | → `inventory.lot_batches` (`id`) |
| `reservation_id` | `BIGINT` | YES | — | The inventory reservation consumed by this shipment line, if applicable. | → `fulfillment.inventory_reservations` (`id`) |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp when this record was first created in the system. | — |

---

## transfer.transfer_requests

**Table description:** Formal request to move stock between locations; initial lifecycle state of Stock Transfer aggregate.

| Column | Data Type | Nullable | Default | Business Meaning | Related Entity |
|--------|-----------|----------|---------|------------------|----------------|
| `id` | `BIGINT` | NO | IDENTITY | System-generated unique identifier for this record. | — (primary key) |
| `request_number` | `VARCHAR(64)` | NO | — | Unique business identifier used in day-to-day operations. | Unique business key |
| `source_location_id` | `BIGINT` | NO | — | The location stock is being transferred from. | → `network.inventory_locations` (`id`) |
| `destination_location_id` | `BIGINT` | NO | — | The location stock is being transferred to. | → `network.inventory_locations` (`id`) |
| `request_reason` | `VARCHAR(128)` | YES | — | Business reason for requesting the inter-location transfer. | — |
| `request_status` | `VARCHAR(32)` | NO | `'SUBMITTED'` | Approval status of the transfer request. | — |
| `requested_by` | `BIGINT` | NO | — | The user who submitted this request. | → `identity.user_accounts` (`id`) |
| `approved_by` | `BIGINT` | YES | — | The user who approved this record or transaction. | → `identity.user_accounts` (`id`) |
| `approved_at` | `TIMESTAMPTZ` | YES | — | Date and time when approval was granted. | — |
| `rejection_reason` | `TEXT` | YES | — | Explanation provided when the transfer request was rejected. | — |
| `stock_transfer_id` | `BIGINT` | YES | — | The stock transfer this record belongs to. | → `transfer.stock_transfers` (`id`) |
| `version` | `INTEGER` | NO | 1 | Version counter incremented on each update to prevent conflicting concurrent edits. | — |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp when this record was first created in the system. | — |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp of the most recent update to this record. | — |

---

## transfer.transfer_request_lines

**Table description:** Product and quantity requested on a transfer request.

| Column | Data Type | Nullable | Default | Business Meaning | Related Entity |
|--------|-----------|----------|---------|------------------|----------------|
| `id` | `BIGINT` | NO | IDENTITY | System-generated unique identifier for this record. | — (primary key) |
| `transfer_request_id` | `BIGINT` | NO | — | The transfer request this record belongs to. | → `transfer.transfer_requests` (`id`) |
| `line_number` | `INTEGER` | NO | — | Line sequence number within the parent transfer request. | — |
| `product_id` | `BIGINT` | NO | — | The product this record pertains to. | → `catalog.products` (`id`) |
| `requested_qty` | `NUMERIC(18,4)` | NO | — | Requested quantity. | — |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp when this record was first created in the system. | — |

---

## transfer.stock_transfers

**Table description:** Executed inter-location stock movement from dispatch to receipt.

| Column | Data Type | Nullable | Default | Business Meaning | Related Entity |
|--------|-----------|----------|---------|------------------|----------------|
| `id` | `BIGINT` | NO | IDENTITY | System-generated unique identifier for this record. | — (primary key) |
| `transfer_number` | `VARCHAR(64)` | NO | — | Unique business identifier used in day-to-day operations. | Unique business key |
| `transfer_request_id` | `BIGINT` | YES | — | The transfer request this record belongs to. | → `transfer.transfer_requests` (`id`) |
| `source_location_id` | `BIGINT` | NO | — | The location stock is being transferred from. | → `network.inventory_locations` (`id`) |
| `destination_location_id` | `BIGINT` | NO | — | The location stock is being transferred to. | → `network.inventory_locations` (`id`) |
| `transfer_status` | `VARCHAR(32)` | NO | `'APPROVED'` | Lifecycle status of the stock transfer execution. | — |
| `dispatch_date` | `TIMESTAMPTZ` | YES | — | Date and time when stock was dispatched from the source location. | — |
| `receipt_date` | `TIMESTAMPTZ` | YES | — | Date and time when stock was received at the destination. | — |
| `version` | `INTEGER` | NO | 1 | Version counter incremented on each update to prevent conflicting concurrent edits. | — |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp when this record was first created in the system. | — |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp of the most recent update to this record. | — |

---

## transfer.stock_transfer_lines

**Table description:** Product, quantity, and lot on a stock transfer.

| Column | Data Type | Nullable | Default | Business Meaning | Related Entity |
|--------|-----------|----------|---------|------------------|----------------|
| `id` | `BIGINT` | NO | IDENTITY | System-generated unique identifier for this record. | — (primary key) |
| `stock_transfer_id` | `BIGINT` | NO | — | The stock transfer this record belongs to. | → `transfer.stock_transfers` (`id`) |
| `line_number` | `INTEGER` | NO | — | Line sequence number within the parent stock transfer. | — |
| `product_id` | `BIGINT` | NO | — | The product this record pertains to. | → `catalog.products` (`id`) |
| `quantity` | `NUMERIC(18,4)` | NO | — | Quantity being transferred on this line. | — |
| `lot_batch_id` | `BIGINT` | YES | — | The lot or batch this record references, when applicable. | → `inventory.lot_batches` (`id`) |
| `dispatched_qty` | `NUMERIC(18,4)` | NO | 0 | Quantity actually dispatched from the source. | — |
| `received_qty` | `NUMERIC(18,4)` | NO | 0 | Quantity actually received at the destination. | — |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp when this record was first created in the system. | — |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp of the most recent update to this record. | — |

---

## transfer.in_transit_stock

**Table description:** Pipeline inventory between dispatch and destination receipt.

| Column | Data Type | Nullable | Default | Business Meaning | Related Entity |
|--------|-----------|----------|---------|------------------|----------------|
| `id` | `BIGINT` | NO | IDENTITY | System-generated unique identifier for this record. | — (primary key) |
| `in_transit_reference` | `VARCHAR(64)` | NO | — | Unique business identifier used in day-to-day operations. | Unique business key |
| `stock_transfer_id` | `BIGINT` | NO | — | The stock transfer this record belongs to. | → `transfer.stock_transfers` (`id`) |
| `stock_transfer_line_id` | `BIGINT` | NO | — | The stock transfer line this in-transit record belongs to. | → `transfer.stock_transfer_lines` (`id`) |
| `product_id` | `BIGINT` | NO | — | The product this record pertains to. | → `catalog.products` (`id`) |
| `quantity` | `NUMERIC(18,4)` | NO | — | Quantity currently in transit between locations. | — |
| `source_location_id` | `BIGINT` | NO | — | The location stock is being transferred from. | → `network.inventory_locations` (`id`) |
| `destination_location_id` | `BIGINT` | NO | — | The location stock is being transferred to. | → `network.inventory_locations` (`id`) |
| `dispatch_date` | `TIMESTAMPTZ` | NO | — | Date and time when goods were dispatched for transfer. | — |
| `expected_receipt_date` | `DATE` | YES | — | Expected date when in-transit stock will arrive. | — |
| `in_transit_status` | `VARCHAR(32)` | NO | `'IN_TRANSIT'` | Status of stock while in transit. | — |
| `carrier_reference` | `VARCHAR(128)` | YES | — | Carrier reference. | — |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp when this record was first created in the system. | — |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp of the most recent update to this record. | — |

---

## accuracy.cycle_counts

**Table description:** Scheduled partial physical count assignment with blind count protocol.

| Column | Data Type | Nullable | Default | Business Meaning | Related Entity |
|--------|-----------|----------|---------|------------------|----------------|
| `id` | `BIGINT` | NO | IDENTITY | System-generated unique identifier for this record. | — (primary key) |
| `count_assignment_number` | `VARCHAR(64)` | NO | — | Unique business identifier used in day-to-day operations. | Unique business key |
| `schedule_date` | `DATE` | NO | — | Calendar date when the cycle count is scheduled. | — |
| `location_id` | `BIGINT` | NO | — | The inventory location this record pertains to. | → `network.inventory_locations` (`id`) |
| `product_id` | `BIGINT` | NO | — | The product this record pertains to. | → `catalog.products` (`id`) |
| `storage_position_id` | `BIGINT` | YES | — | The storage position (bin/shelf) where stock is or was located. | → `network.storage_positions` (`id`) |
| `counter_id` | `BIGINT` | NO | — | The user assigned to perform this count. | → `identity.user_accounts` (`id`) |
| `count_status` | `VARCHAR(32)` | NO | `'SCHEDULED'` | Status of the cycle count assignment. | — |
| `physical_count_qty` | `NUMERIC(18,4)` | YES | — | Quantity physically counted by the operator. | — |
| `system_count_qty` | `NUMERIC(18,4)` | YES | — | System on-hand quantity revealed only after count submission (blind count). | — |
| `completed_at` | `TIMESTAMPTZ` | YES | — | Date and time when the count was completed. | — |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp when this record was first created in the system. | — |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp of the most recent update to this record. | — |

---

## accuracy.physical_inventory_counts

**Table description:** Wall-to-wall count event imposing location freeze (BR-024).

| Column | Data Type | Nullable | Default | Business Meaning | Related Entity |
|--------|-----------|----------|---------|------------------|----------------|
| `id` | `BIGINT` | NO | IDENTITY | System-generated unique identifier for this record. | — (primary key) |
| `count_event_number` | `VARCHAR(64)` | NO | — | Unique business identifier used in day-to-day operations. | Unique business key |
| `location_id` | `BIGINT` | NO | — | The inventory location this record pertains to. | → `network.inventory_locations` (`id`) |
| `count_start_date` | `TIMESTAMPTZ` | NO | — | Date and time when the wall-to-wall physical count began. | — |
| `count_completion_date` | `TIMESTAMPTZ` | YES | — | Date and time when the wall-to-wall physical count ended. | — |
| `freeze_status` | `VARCHAR(32)` | NO | `'ACTIVE'` | Freeze status during the physical inventory count. | — |
| `total_variances` | `INTEGER` | NO | 0 | Number of variances discovered during the count event. | — |
| `certification_status` | `VARCHAR(32)` | NO | `'IN_PROGRESS'` | Certification status of the physical count event. | — |
| `version` | `INTEGER` | NO | 1 | Version counter incremented on each update to prevent conflicting concurrent edits. | — |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp when this record was first created in the system. | — |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp of the most recent update to this record. | — |

---

## accuracy.count_variances

**Table description:** System vs. physical quantity difference requiring investigation.

| Column | Data Type | Nullable | Default | Business Meaning | Related Entity |
|--------|-----------|----------|---------|------------------|----------------|
| `id` | `BIGINT` | NO | IDENTITY | System-generated unique identifier for this record. | — (primary key) |
| `variance_reference` | `VARCHAR(64)` | NO | — | Unique business identifier used in day-to-day operations. | Unique business key |
| `cycle_count_id` | `BIGINT` | YES | — | The cycle count assignment that produced this variance, if applicable. | → `accuracy.cycle_counts` (`id`) |
| `physical_count_id` | `BIGINT` | YES | — | The physical inventory count event that produced this variance, if applicable. | → `accuracy.physical_inventory_counts` (`id`) |
| `stock_position_id` | `BIGINT` | NO | — | The stock position (product at location) this record affects. | → `inventory.stock_positions` (`id`) |
| `product_id` | `BIGINT` | NO | — | The product this record pertains to. | → `catalog.products` (`id`) |
| `location_id` | `BIGINT` | NO | — | The inventory location this record pertains to. | → `network.inventory_locations` (`id`) |
| `system_qty` | `NUMERIC(18,4)` | NO | — | System on-hand quantity at the time of the count. | — |
| `physical_qty` | `NUMERIC(18,4)` | NO | — | Quantity physically counted during the inventory event. | — |
| `variance_qty` | `NUMERIC(18,4)` | NO | — | Variance quantity calculated as physical minus system quantity. | — |
| `variance_value` | `NUMERIC(18,2)` | YES | — | Estimated monetary value of the quantity variance. | — |
| `investigation_status` | `VARCHAR(32)` | NO | `'OPEN'` | Investigation status of the count variance. | — |
| `investigation_findings` | `TEXT` | YES | — | Notes documenting the root cause found during investigation. | — |
| `approval_status` | `VARCHAR(32)` | NO | `'PENDING'` | Approval status for the variance or adjustment. | — |
| `approver_id` | `BIGINT` | YES | — | The user who approved or rejected this variance. | → `identity.user_accounts` (`id`) |
| `approved_at` | `TIMESTAMPTZ` | YES | — | Date and time when approval was granted. | — |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp when this record was first created in the system. | — |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp of the most recent update to this record. | — |

---

## accuracy.stock_adjustments

**Table description:** Authorized correction to stock position with mandatory reason code.

| Column | Data Type | Nullable | Default | Business Meaning | Related Entity |
|--------|-----------|----------|---------|------------------|----------------|
| `id` | `BIGINT` | NO | IDENTITY | System-generated unique identifier for this record. | — (primary key) |
| `adjustment_reference` | `VARCHAR(64)` | NO | — | Unique business identifier used in day-to-day operations. | Unique business key |
| `stock_position_id` | `BIGINT` | NO | — | The stock position (product at location) this record affects. | → `inventory.stock_positions` (`id`) |
| `product_id` | `BIGINT` | NO | — | The product this record pertains to. | → `catalog.products` (`id`) |
| `location_id` | `BIGINT` | NO | — | The inventory location this record pertains to. | → `network.inventory_locations` (`id`) |
| `adjustment_qty` | `NUMERIC(18,4)` | NO | — | Signed adjustment quantity (positive increases, negative decreases stock). | — |
| `qty_before` | `NUMERIC(18,4)` | NO | — | On-hand quantity before the adjustment was applied. | — |
| `qty_after` | `NUMERIC(18,4)` | NO | — | On-hand quantity after the adjustment was applied. | — |
| `reason_code_id` | `BIGINT` | NO | — | The standardized reason code explaining this transaction. | → `governance.reason_codes` (`id`) |
| `count_variance_id` | `BIGINT` | YES | — | The count variance that triggered this stock adjustment, if applicable. | → `accuracy.count_variances` (`id`) |
| `approval_status` | `VARCHAR(32)` | NO | `'PENDING'` | Approval status for the variance or adjustment. | — |
| `initiated_by` | `BIGINT` | NO | — | The user who initiated this transaction. | → `identity.user_accounts` (`id`) |
| `approved_by` | `BIGINT` | YES | — | The user who approved this record or transaction. | → `identity.user_accounts` (`id`) |
| `adjustment_date` | `TIMESTAMPTZ` | NO | `NOW()` | Date and time when the adjustment or write-off takes effect. | — |
| `version` | `INTEGER` | NO | 1 | Version counter incremented on each update to prevent conflicting concurrent edits. | — |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp when this record was first created in the system. | — |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp of the most recent update to this record. | — |

---

## accuracy.inventory_write_offs

**Table description:** Permanent authorized removal of inventory value.

| Column | Data Type | Nullable | Default | Business Meaning | Related Entity |
|--------|-----------|----------|---------|------------------|----------------|
| `id` | `BIGINT` | NO | IDENTITY | System-generated unique identifier for this record. | — (primary key) |
| `write_off_reference` | `VARCHAR(64)` | NO | — | Unique business identifier used in day-to-day operations. | Unique business key |
| `stock_position_id` | `BIGINT` | NO | — | The stock position (product at location) this record affects. | → `inventory.stock_positions` (`id`) |
| `product_id` | `BIGINT` | NO | — | The product this record pertains to. | → `catalog.products` (`id`) |
| `location_id` | `BIGINT` | NO | — | The inventory location this record pertains to. | → `network.inventory_locations` (`id`) |
| `write_off_qty` | `NUMERIC(18,4)` | NO | — | Quantity permanently removed from inventory. | — |
| `financial_value` | `NUMERIC(18,2)` | YES | — | Monetary value impact of the write-off. | — |
| `reason_code_id` | `BIGINT` | NO | — | The standardized reason code explaining this transaction. | → `governance.reason_codes` (`id`) |
| `evidence_reference` | `VARCHAR(128)` | YES | — | Reference to supporting documentation for the write-off. | — |
| `disposition_method` | `VARCHAR(32)` | YES | — | Physical disposition method for written-off goods. | — |
| `return_disposition_id` | `BIGINT` | YES | — | The return disposition linked to this write-off, if applicable. | → `returns.return_dispositions` (`id`) |
| `initiated_by` | `BIGINT` | NO | — | The user who initiated this transaction. | → `identity.user_accounts` (`id`) |
| `authorized_by` | `BIGINT` | NO | — | The user who authorized this action. | → `identity.user_accounts` (`id`) |
| `write_off_date` | `TIMESTAMPTZ` | NO | `NOW()` | Date and time when the adjustment or write-off takes effect. | — |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp when this record was first created in the system. | — |

---

## returns.return_authorizations

**Table description:** RMA gating customer return before warehouse acceptance (BR-025).

| Column | Data Type | Nullable | Default | Business Meaning | Related Entity |
|--------|-----------|----------|---------|------------------|----------------|
| `id` | `BIGINT` | NO | IDENTITY | System-generated unique identifier for this record. | — (primary key) |
| `rma_number` | `VARCHAR(64)` | NO | — | Unique business identifier used in day-to-day operations. | Unique business key |
| `customer_order_id` | `BIGINT` | NO | — | The customer order this record belongs to. | → `fulfillment.customer_orders` (`id`) |
| `customer_reference` | `VARCHAR(128)` | YES | — | Customer identifier. | — |
| `return_reason` | `VARCHAR(128)` | YES | — | Customer-stated reason for returning the goods. | — |
| `authorization_date` | `TIMESTAMPTZ` | NO | `NOW()` | Date and time when the return authorization was issued. | — |
| `expiration_date` | `DATE` | YES | — | Date after which the return authorization is no longer valid. | — |
| `disposition_expectation` | `VARCHAR(64)` | YES | — | Expected outcome for returned goods (restock, scrap, etc.). | — |
| `authorization_status` | `VARCHAR(32)` | NO | `'ACTIVE'` | Status of the return authorization. | — |
| `version` | `INTEGER` | NO | 1 | Version counter incremented on each update to prevent conflicting concurrent edits. | — |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp when this record was first created in the system. | — |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp of the most recent update to this record. | — |

---

## returns.return_authorization_lines

**Table description:** Authorized return products and quantities on an RMA.

| Column | Data Type | Nullable | Default | Business Meaning | Related Entity |
|--------|-----------|----------|---------|------------------|----------------|
| `id` | `BIGINT` | NO | IDENTITY | System-generated unique identifier for this record. | — (primary key) |
| `return_authorization_id` | `BIGINT` | NO | — | The return authorization (RMA) governing this return. | → `returns.return_authorizations` (`id`) |
| `line_number` | `INTEGER` | NO | — | Line sequence number within the parent return authorization. | — |
| `product_id` | `BIGINT` | NO | — | The product this record pertains to. | → `catalog.products` (`id`) |
| `authorized_qty` | `NUMERIC(18,4)` | NO | — | Quantity the customer is authorized to return. | — |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp when this record was first created in the system. | — |

---

## returns.customer_returns

**Table description:** Physical receipt of customer-returned goods.

| Column | Data Type | Nullable | Default | Business Meaning | Related Entity |
|--------|-----------|----------|---------|------------------|----------------|
| `id` | `BIGINT` | NO | IDENTITY | System-generated unique identifier for this record. | — (primary key) |
| `return_number` | `VARCHAR(64)` | NO | — | Unique business identifier used in day-to-day operations. | Unique business key |
| `return_authorization_id` | `BIGINT` | NO | — | The return authorization (RMA) governing this return. | → `returns.return_authorizations` (`id`) |
| `customer_order_id` | `BIGINT` | NO | — | The customer order this record belongs to. | → `fulfillment.customer_orders` (`id`) |
| `receiving_location_id` | `BIGINT` | NO | — | The location where goods will be or were received. | → `network.inventory_locations` (`id`) |
| `receipt_date` | `TIMESTAMPTZ` | NO | `NOW()` | Date and time when goods were received at the dock. | — |
| `inspection_status` | `VARCHAR(32)` | NO | `'PENDING'` | Inspection status of the customer return receipt. | — |
| `receiving_clerk_id` | `BIGINT` | NO | — | The receiving clerk who processed this receipt. | → `identity.user_accounts` (`id`) |
| `version` | `INTEGER` | NO | 1 | Version counter incremented on each update to prevent conflicting concurrent edits. | — |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp when this record was first created in the system. | — |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp of the most recent update to this record. | — |

---

## returns.customer_return_lines

**Table description:** Returned product, quantity, and condition at receipt.

| Column | Data Type | Nullable | Default | Business Meaning | Related Entity |
|--------|-----------|----------|---------|------------------|----------------|
| `id` | `BIGINT` | NO | IDENTITY | System-generated unique identifier for this record. | — (primary key) |
| `customer_return_id` | `BIGINT` | NO | — | The customer return receipt this record belongs to. | → `returns.customer_returns` (`id`) |
| `line_number` | `INTEGER` | NO | — | Line sequence number within the parent customer return. | — |
| `product_id` | `BIGINT` | NO | — | The product this record pertains to. | → `catalog.products` (`id`) |
| `returned_qty` | `NUMERIC(18,4)` | NO | — | Returned quantity. | — |
| `condition_at_receipt` | `VARCHAR(32)` | NO | — | Condition of returned goods at receipt. | — |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp when this record was first created in the system. | — |

---

## returns.return_dispositions

**Table description:** Inspection outcome — restock, quarantine, or write-off.

| Column | Data Type | Nullable | Default | Business Meaning | Related Entity |
|--------|-----------|----------|---------|------------------|----------------|
| `id` | `BIGINT` | NO | IDENTITY | System-generated unique identifier for this record. | — (primary key) |
| `disposition_reference` | `VARCHAR(64)` | NO | — | Unique business identifier used in day-to-day operations. | Unique business key |
| `customer_return_id` | `BIGINT` | NO | — | The customer return receipt this record belongs to. | → `returns.customer_returns` (`id`) |
| `return_line_id` | `BIGINT` | NO | — | The customer return line this disposition applies to. | → `returns.customer_return_lines` (`id`) |
| `product_id` | `BIGINT` | NO | — | The product this record pertains to. | → `catalog.products` (`id`) |
| `quantity` | `NUMERIC(18,4)` | NO | — | Disposition quantity. | — |
| `condition_grade` | `VARCHAR(32)` | NO | — | Quality grade assigned during return inspection. | — |
| `disposition_decision` | `VARCHAR(32)` | NO | — | Disposition decision for returned goods. | — |
| `restock_location_id` | `BIGINT` | YES | — | The location where returned goods will be restocked, if applicable. | → `network.inventory_locations` (`id`) |
| `quarantine_hold_id` | `BIGINT` | YES | — | The quarantine hold created when goods are quarantined on return. | → `inventory.quarantine_holds` (`id`) |
| `write_off_id` | `BIGINT` | YES | — | The inventory write-off created when returned goods are written off. | → `accuracy.inventory_write_offs` (`id`) |
| `inspector_id` | `BIGINT` | NO | — | The user who inspected and determined the disposition. | → `identity.user_accounts` (`id`) |
| `inspection_date` | `TIMESTAMPTZ` | NO | `NOW()` | Date and time when the return inspection was completed. | — |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp when this record was first created in the system. | — |

---

## commercial.promotional_stock_allocations

**Table description:** Ring-fenced stock for promotional campaigns or product launches (BR-029).

| Column | Data Type | Nullable | Default | Business Meaning | Related Entity |
|--------|-----------|----------|---------|------------------|----------------|
| `id` | `BIGINT` | NO | IDENTITY | System-generated unique identifier for this record. | — (primary key) |
| `allocation_reference` | `VARCHAR(64)` | NO | — | Unique business identifier used in day-to-day operations. | Unique business key |
| `product_id` | `BIGINT` | NO | — | The product this record pertains to. | → `catalog.products` (`id`) |
| `allocated_qty` | `NUMERIC(18,4)` | NO | — | Quantity reserved exclusively for the promotional campaign. | — |
| `campaign_name` | `VARCHAR(256)` | NO | — | Name of the promotional campaign or product launch. | — |
| `channel` | `VARCHAR(32)` | YES | — | Sales channel to which the promotional allocation applies. | — |
| `effective_start_date` | `DATE` | NO | — | First date the promotional allocation is effective. | — |
| `effective_end_date` | `DATE` | NO | — | Last date the promotional allocation is effective. | — |
| `readiness_status` | `VARCHAR(32)` | NO | `'PLANNED'` | Readiness lifecycle status of the promotional allocation. | — |
| `commercial_approval_ref` | `VARCHAR(64)` | YES | — | Reference documenting commercial team approval. | — |
| `version` | `INTEGER` | NO | 1 | Version counter incremented on each update to prevent conflicting concurrent edits. | — |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp when this record was first created in the system. | — |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp of the most recent update to this record. | — |

---

## commercial.promotional_allocation_locations

**Table description:** Locations supplying ring-fenced promotional stock.

| Column | Data Type | Nullable | Default | Business Meaning | Related Entity |
|--------|-----------|----------|---------|------------------|----------------|
| `id` | `BIGINT` | NO | IDENTITY | System-generated unique identifier for this record. | — (primary key) |
| `allocation_id` | `BIGINT` | NO | — | The promotional stock allocation this location assignment belongs to. | → `commercial.promotional_stock_allocations` (`id`) |
| `location_id` | `BIGINT` | NO | — | The inventory location this record pertains to. | → `network.inventory_locations` (`id`) |
| `stock_position_id` | `BIGINT` | YES | — | The stock position (product at location) this record affects. | → `inventory.stock_positions` (`id`) |
| `allocated_qty_at_location` | `NUMERIC(18,4)` | NO | — | Portion of the promotional allocation ring-fenced at this location. | — |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp when this record was first created in the system. | — |

---

## identity.user_accounts

**Table description:** Authenticated user identity and accountability anchor for all operations.

| Column | Data Type | Nullable | Default | Business Meaning | Related Entity |
|--------|-----------|----------|---------|------------------|----------------|
| `id` | `BIGINT` | NO | IDENTITY | System-generated unique identifier for this record. | — (primary key) |
| `user_identifier` | `VARCHAR(64)` | NO | — | Unique login or employee identifier used for authentication. | Unique business key |
| `display_name` | `VARCHAR(256)` | NO | — | The user's full name as displayed in the application. | — |
| `email` | `VARCHAR(256)` | YES | — | Email address for contacting this person or organization. | — |
| `account_status` | `VARCHAR(32)` | NO | `'ACTIVE'` | Account status controlling user access. | — |
| `effective_from` | `DATE` | NO | — | Date from which the user account is effective. | — |
| `last_activity_at` | `TIMESTAMPTZ` | YES | — | Timestamp of the user's most recent system activity. | — |
| `has_sod_conflict` | `BOOLEAN` | NO | `FALSE` | Indicates a segregation-of-duties conflict exists for this user. | — |
| `version` | `INTEGER` | NO | 1 | Version counter incremented on each update to prevent conflicting concurrent edits. | — |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp when this record was first created in the system. | — |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp of the most recent update to this record. | — |

---

## identity.role_assignments

**Table description:** Role delegation with permission boundaries per user.

| Column | Data Type | Nullable | Default | Business Meaning | Related Entity |
|--------|-----------|----------|---------|------------------|----------------|
| `id` | `BIGINT` | NO | IDENTITY | System-generated unique identifier for this record. | — (primary key) |
| `user_account_id` | `BIGINT` | NO | — | The user account this role assignment belongs to. | → `identity.user_accounts` (`id`) |
| `role_name` | `VARCHAR(64)` | NO | — | Business role assigned to the user. | — |
| `permission_set` | `VARCHAR(128)` | YES | — | Reference to the permission set granted by this role. | — |
| `assignment_status` | `VARCHAR(32)` | NO | `'ACTIVE'` | Whether this role assignment is currently active. | — |
| `effective_from` | `DATE` | NO | — | Date from which this role assignment is effective. | — |
| `effective_to` | `DATE` | YES | — | Date when this role assignment expires; null means open-ended. | — |
| `sod_compliant` | `BOOLEAN` | NO | `TRUE` | Indicates whether this assignment complies with segregation-of-duties rules. | — |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp when this record was first created in the system. | — |
| `updated_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp of the most recent update to this record. | — |

---

## identity.role_assignment_locations

**Table description:** Location scope restricting role permissions to authorized sites.

| Column | Data Type | Nullable | Default | Business Meaning | Related Entity |
|--------|-----------|----------|---------|------------------|----------------|
| `id` | `BIGINT` | NO | IDENTITY | System-generated unique identifier for this record. | — (primary key) |
| `role_assignment_id` | `BIGINT` | NO | — | The role assignment this location scope restriction belongs to. | → `identity.role_assignments` (`id`) |
| `location_id` | `BIGINT` | NO | — | The inventory location this record pertains to. | → `network.inventory_locations` (`id`) |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp when this record was first created in the system. | — |

---

## audit.inventory_movement_records

**Table description:** Immutable append-only log of every stock quantity change.

| Column | Data Type | Nullable | Default | Business Meaning | Related Entity |
|--------|-----------|----------|---------|------------------|----------------|
| `id` | `BIGINT` | NO | IDENTITY | System-generated unique identifier for this record within its monthly partition. | — (primary key) |
| `movement_reference` | `VARCHAR(64)` | NO | — | Reference number linking this movement to its originating business transaction. | — |
| `movement_type` | `VARCHAR(32)` | NO | — | Category of inventory movement recorded. | — |
| `stock_position_id` | `BIGINT` | NO | — | The stock position (product at location) this record affects. | → `inventory.stock_positions` (`id`) |
| `product_id` | `BIGINT` | NO | — | The product this record pertains to. | → `catalog.products` (`id`) (denormalized) |
| `location_id` | `BIGINT` | NO | — | The inventory location this record pertains to. | → `network.inventory_locations` (`id`) (denormalized) |
| `quantity_change` | `NUMERIC(18,4)` | NO | — | Signed change in quantity (positive for increases, negative for decreases). | — |
| `qty_before` | `NUMERIC(18,4)` | NO | — | On-hand quantity immediately before this movement. | — |
| `qty_after` | `NUMERIC(18,4)` | NO | — | On-hand quantity immediately after this movement. | — |
| `lot_batch_id` | `BIGINT` | YES | — | The lot or batch this record references, when applicable. | → `inventory.lot_batches` (`id`) |
| `reason_code_id` | `BIGINT` | YES | — | The standardized reason code explaining this transaction. | → `governance.reason_codes` (`id`) |
| `source_document_type` | `VARCHAR(32)` | NO | — | Type of business document that caused this movement. | Polymorphic document reference |
| `source_document_id` | `BIGINT` | NO | — | Primary key of the business document that caused this movement. | Polymorphic document reference |
| `performed_by` | `BIGINT` | NO | — | The user who performed this inventory movement. | → `identity.user_accounts` (`id`) |
| `movement_timestamp` | `TIMESTAMPTZ` | NO | `NOW()` | Business event timestamp used as the monthly partition key. | — |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp when this row was physically inserted into the database. | — |

---

## audit.audit_trail_records

**Table description:** Governance-grade before/after snapshots for material entity changes.

| Column | Data Type | Nullable | Default | Business Meaning | Related Entity |
|--------|-----------|----------|---------|------------------|----------------|
| `id` | `BIGINT` | NO | IDENTITY | System-generated unique identifier for this record within its monthly partition. | — (primary key) |
| `audit_event_reference` | `VARCHAR(64)` | NO | — | Human-readable reference number for this business transaction. | — |
| `affected_entity_type` | `VARCHAR(64)` | NO | — | Name of the entity type that was changed. | — |
| `affected_entity_id` | `BIGINT` | NO | — | Primary key of the record that was changed. | — |
| `action_performed` | `VARCHAR(32)` | NO | — | Type of action performed on the affected entity. | — |
| `user_id` | `BIGINT` | NO | — | The user who performed the audited action. | → `identity.user_accounts` (`id`) |
| `role_at_action` | `VARCHAR(64)` | YES | — | User's role at the moment the action was performed. | — |
| `before_state` | `JSONB` | YES | — | JSON snapshot of the entity state before the change. | — |
| `after_state` | `JSONB` | YES | — | JSON snapshot of the entity state after the change. | — |
| `approval_chain_ref` | `VARCHAR(128)` | YES | — | Reference to the approval workflow chain for this action. | — |
| `movement_record_id` | `BIGINT` | YES | — | The inventory movement record associated with this audit event, if applicable. | → `audit.inventory_movement_records` (`id`) |
| `event_timestamp` | `TIMESTAMPTZ` | NO | `NOW()` | Business event timestamp used as the monthly partition key. | — |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp when this row was physically inserted into the database. | — |

---

## audit.operational_alerts

**Table description:** Derived notifications for threshold breaches, pending approvals, and exceptions.

| Column | Data Type | Nullable | Default | Business Meaning | Related Entity |
|--------|-----------|----------|---------|------------------|----------------|
| `id` | `BIGINT` | NO | IDENTITY | System-generated unique identifier for this record. | — (primary key) |
| `alert_reference` | `VARCHAR(64)` | NO | — | Unique business identifier used in day-to-day operations. | Unique business key |
| `alert_type` | `VARCHAR(32)` | NO | — | Category of operational alert. | — |
| `severity` | `VARCHAR(16)` | NO | `'MEDIUM'` | Severity level of the alert. | — |
| `product_id` | `BIGINT` | YES | — | The product this record pertains to. | → `catalog.products` (`id`) |
| `location_id` | `BIGINT` | YES | — | The inventory location this record pertains to. | → `network.inventory_locations` (`id`) |
| `stock_position_id` | `BIGINT` | YES | — | The stock position (product at location) this record affects. | → `inventory.stock_positions` (`id`) |
| `source_entity_type` | `VARCHAR(64)` | YES | — | Type of business entity that triggered the alert. | Polymorphic source reference |
| `source_entity_id` | `BIGINT` | YES | — | Primary key of the entity that triggered the alert. | Polymorphic source reference |
| `triggering_condition` | `TEXT` | YES | — | Plain-language description of the condition that triggered the alert. | — |
| `assigned_role` | `VARCHAR(64)` | YES | — | Role responsible for acknowledging and resolving the alert. | — |
| `acknowledgment_status` | `VARCHAR(32)` | NO | `'OPEN'` | Whether the alert has been acknowledged. | — |
| `resolution_status` | `VARCHAR(32)` | NO | `'PENDING'` | Whether the underlying issue has been resolved. | — |
| `alert_date` | `TIMESTAMPTZ` | NO | `NOW()` | Date and time when the alert was generated. | — |
| `resolved_at` | `TIMESTAMPTZ` | YES | — | Date and time when the alert was resolved. | — |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp when this record was first created in the system. | — |

---

## audit.inventory_valuation_snapshots

**Table description:** Point-in-time inventory value summary for finance reconciliation (BP-30).

| Column | Data Type | Nullable | Default | Business Meaning | Related Entity |
|--------|-----------|----------|---------|------------------|----------------|
| `id` | `BIGINT` | NO | IDENTITY | System-generated unique identifier for this record. | — (primary key) |
| `snapshot_reference` | `VARCHAR(64)` | NO | — | Unique business identifier used in day-to-day operations. | Unique business key |
| `valuation_date` | `DATE` | NO | — | Calendar date representing the point in time for this valuation. | — |
| `location_scope` | `VARCHAR(32)` | NO | — | Scope of locations included in the valuation snapshot. | — |
| `total_inventory_value` | `NUMERIC(18,2)` | NO | — | Total monetary value of owned inventory in the snapshot. | — |
| `owned_value` | `NUMERIC(18,2)` | NO | — | Monetary value of inventory owned by the organization. | — |
| `consignment_value` | `NUMERIC(18,2)` | NO | 0 | Monetary value of consignment stock excluded from owned totals. | — |
| `gl_variance` | `NUMERIC(18,2)` | YES | — | Difference between inventory valuation and the general ledger balance. | — |
| `reconciliation_status` | `VARCHAR(32)` | NO | `'DRAFT'` | Reconciliation status against the general ledger. | — |
| `prepared_by` | `BIGINT` | NO | — | The user who prepared this valuation snapshot. | → `identity.user_accounts` (`id`) |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp when this record was first created in the system. | — |

---

## audit.inventory_valuation_lines

**Table description:** Product-level quantity and value detail within a valuation snapshot.

| Column | Data Type | Nullable | Default | Business Meaning | Related Entity |
|--------|-----------|----------|---------|------------------|----------------|
| `id` | `BIGINT` | NO | IDENTITY | System-generated unique identifier for this record. | — (primary key) |
| `snapshot_id` | `BIGINT` | NO | — | The valuation snapshot this detail line belongs to. | → `audit.inventory_valuation_snapshots` (`id`) |
| `product_id` | `BIGINT` | NO | — | The product this record pertains to. | → `catalog.products` (`id`) |
| `location_id` | `BIGINT` | NO | — | The inventory location this record pertains to. | → `network.inventory_locations` (`id`) |
| `quantity` | `NUMERIC(18,4)` | NO | — | On-hand quantity captured in the valuation snapshot. | — |
| `unit_cost` | `NUMERIC(18,4)` | NO | — | Cost per unit used to value inventory in the snapshot. | — |
| `extended_value` | `NUMERIC(18,2)` | NO | — | Extended value calculated as quantity multiplied by unit cost. | — |
| `ownership_type` | `VARCHAR(32)` | NO | `'OWNED'` | OWNED, CONSIGNMENT. | — |
| `created_at` | `TIMESTAMPTZ` | NO | `NOW()` | Timestamp when this record was first created in the system. | — |

---

## Appendix A: Data Type Legend

| Data Type | Business Meaning |
|-----------|------------------|
| `BIGINT` | Large whole number; used for primary keys and foreign key references |
| `INTEGER` | Whole number for counts, days, and version counters |
| `NUMERIC(18,4)` | Precise decimal for quantities — never floating-point |
| `NUMERIC(18,2)` | Precise decimal for monetary amounts |
| `NUMERIC(3,2)` | Decimal with limited precision (e.g., ratings 0.00–5.00) |
| `VARCHAR(n)` | Variable-length text up to n characters; used for codes, names, and status values |
| `CHAR(n)` | Fixed-length text; used for ISO codes (country, currency) |
| `TEXT` | Unlimited-length text for descriptions, notes, and evidence |
| `BOOLEAN` | True/false flag |
| `DATE` | Calendar date without time component |
| `TIMESTAMPTZ` | Date and time stored in UTC with timezone awareness |
| `JSONB` | Structured JSON snapshot for audit before/after state |

---

## Appendix B: Standard Audit Columns

Many tables share common audit and control columns. Their business purpose is consistent across the model:

| Column | Typical Presence | Business Meaning |
|--------|------------------|------------------|
| `id` | All tables | Surrogate primary key generated automatically by the database |
| `version` | Mutable transactional headers | Optimistic lock counter preventing lost updates during concurrent edits |
| `is_active` | Master/reference data | Soft-delete flag; inactive rows are retained but excluded from operational use |
| `created_at` | Most mutable tables | When the record was first created |
| `updated_at` | Most mutable tables | When the record was last modified |
| `created_by` | Documents requiring attribution | User who created the record |
| `line_number` | Document line tables | Sequence position of the line within its parent document |

---

## Appendix C: Entity Relationship Overview

High-level data flow and relationships across bounded contexts:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           FOUNDATION LAYER                                   │
│  catalog.products ◄──── catalog.product_identifiers                          │
│  network.inventory_locations ◄── network.storage_positions (self-hierarchy)  │
│  governance.governance_policies ◄── governance.reason_codes                  │
│  identity.user_accounts ◄── identity.role_assignments ◄── role_assignment_locations │
└─────────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                         INVENTORY CORE (quantity hub)                        │
│  inventory.stock_positions (product × location)                              │
│       ├── inventory.lot_batches                                              │
│       ├── inventory.quarantine_holds                                         │
│       └── inventory.stock_policies ──► inventory.stock_policy_history        │
└─────────────────────────────────────────────────────────────────────────────┘
          ▲                    ▲                    ▲                    ▲
          │                    │                    │                    │
   PROCUREMENT            INBOUND              FULFILLMENT           TRANSFER
          │                    │                    │                    │
 procurement.suppliers   inbound.goods_receipts   fulfillment.customer_orders   transfer.transfer_requests
 procurement.purchase_*  inbound.goods_receipt_*  fulfillment.* (reservations,   transfer.stock_transfers
 expected_inbound_*        receipt_discrepancies      picks, shipments, backorders)  in_transit_stock
          │                    │                    │                    │
          └──────── finance.supplier_invoices ◄─────┴────────────────────┘
                    (three-way match via invoice_goods_receipt_match)
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                    ACCURACY · RETURNS · COMMERCIAL                           │
│  accuracy.cycle_counts / physical_inventory_counts ──► count_variances       │
│       └── stock_adjustments · inventory_write_offs                           │
│  returns.return_authorizations ──► customer_returns ──► return_dispositions  │
│  commercial.promotional_stock_allocations ──► promotional_allocation_locations│
└─────────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                              AUDIT LAYER                                     │
│  audit.inventory_movement_records (append-only quantity changes)             │
│  audit.audit_trail_records (entity change snapshots)                         │
│  audit.operational_alerts (threshold & exception notifications)              │
│  audit.inventory_valuation_snapshots ──► inventory_valuation_lines           │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Key relationship patterns:**

- **Product × Location hub:** `inventory.stock_positions` is the central quantity record; most operational tables reference it directly or via `product_id` + `location_id`.
- **Document header / line pattern:** Requisitions, POs, orders, receipts, transfers, and returns follow a header table with child line tables linked by parent FK.
- **Procure-to-receive:** `procurement.purchase_orders` → `inbound.goods_receipts` → `inbound.put_aways` → stock position update.
- **Order-to-ship:** `fulfillment.customer_orders` → `inventory_reservations` → `fulfillment_executions` → `shipments`.
- **Three-way match:** `finance.supplier_invoices` linked to `inbound.goods_receipts` via `invoice_goods_receipt_match`, matched against `purchase_order_lines`.
- **Audit trail:** Every material quantity change posts to `audit.inventory_movement_records`; governed entity changes post to `audit.audit_trail_records`.

---

*End of Data Dictionary*

*Document ID: SRS-DB-007 | Version 1.0 | July 6, 2026*
