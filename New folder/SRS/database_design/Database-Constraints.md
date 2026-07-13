# Database Constraints Specification
## Inventory Management System — PostgreSQL

---

## Document Information

| Attribute | Detail |
|-----------|--------|
| **Document ID** | SRS-DB-004 |
| **Document Title** | Database Constraints — Business Integrity Enforcement |
| **Version** | 1.0 |
| **Status** | Draft |
| **Document Owner** | Database Architect |
| **Source Documents** | SRS-DB-002 (Physical Data Model), SRS-DB-003 (Database Keys), SRS-BR-001 (Business Rules) |
| **Target Platform** | PostgreSQL 15+ |
| **Date** | July 6, 2026 |
| **Scope** | Constraint definitions and business justification — no DDL/SQL statements |

### Purpose

This document defines all **database constraints** for the Inventory Management System. Each constraint enforces a business rule or data integrity invariant at the persistence layer. Constraints are named using the pattern `{type}_{table}_{column_or_scope}`.

### Constraint Type Legend

| Type | Prefix | Description |
|------|--------|-------------|
| **NOT NULL** | `nn_` | Column must contain a value |
| **UNIQUE** | `uk_` | Column or combination must be unique |
| **CHECK** | `chk_` | Value must satisfy a business rule expression |
| **FOREIGN KEY** | `fk_` | Referential integrity to parent table |
| **DEFAULT** | `def_` | Default value when not supplied on INSERT |

### Standard Platform Constraints

Applied uniformly unless a table explicitly omits a column.

| Table Pattern | Column | Type | Constraint | Business Rule | Justification |
|---------------|--------|------|------------|---------------|---------------|
| All tables | `id` | NOT NULL | `nn_*_id` | — | Primary key identity must always exist |
| All tables | `id` | DEFAULT | `def_*_id` IDENTITY | — | System-generated stable surrogate key |
| Mutable tables | `created_at` | NOT NULL | `nn_*_created_at` | BO-19 | Every record has auditable creation timestamp |
| Mutable tables | `created_at` | DEFAULT | `def_*_created_at` = NOW() | BO-19 | Auto-stamp creation time in UTC |
| Mutable transactional headers | `version` | NOT NULL | `nn_*_version` | — | Optimistic locking counter required |
| Mutable transactional headers | `version` | DEFAULT | `def_*_version` = 1 | — | Initial version on insert |
| Master data tables | `is_active` | NOT NULL | `nn_*_is_active` | — | Soft-delete flag must be explicit |
| Master data tables | `is_active` | DEFAULT | `def_*_is_active` = TRUE | — | New master records active by default |

---

## Shared Domain CHECK Registry

Reusable enumerated value constraints referenced by multiple tables.

| Constraint Name | Allowed Values | Business Rule | Justification |
|-----------------|----------------|---------------|---------------|
| `chk_domain_lifecycle_status` | ACTIVE, INACTIVE, DISCONTINUED | BR-027 | Controls product eligibility for procurement and reservation |
| `chk_domain_abc_classification` | A, B, C | BR-032 | ABC class drives count frequency and alert priority |
| `chk_domain_rotation_policy` | FIFO, FEFO | BR-014, BR-015 | Rotation discipline for picking and put-away |
| `chk_domain_ownership_type` | OWNED, CONSIGNMENT, BONDED | BR-031, BR-030 | Ownership affects ATP, valuation, and customs hold |
| `chk_domain_quantity_non_negative` | value >= 0 | BR-001, LDM-01 | Inventory quantities cannot be negative |
| `chk_domain_quantity_positive` | value > 0 | — | Order/receipt line quantities must be meaningful |
| `chk_domain_order_status` | DRAFT, CONFIRMED, PARTIAL, FULFILLED, CANCELLED | BR-001, BR-002 | Order lifecycle states |
| `chk_domain_po_status` | OPEN, PARTIAL, CLOSED, CANCELLED | BR-007 | PO receipt authorization lifecycle |
| `chk_domain_approval_status` | PENDING, APPROVED, REJECTED (+ variants) | BR-019, BR-021 | Governance workflow states |
| `chk_domain_hold_type` | QUALITY, REGULATORY, RECALL, CUSTOMS, INVESTIGATION | BR-013, BR-030 | Quarantine hold classification |
| `chk_domain_disposition_decision` | RESTOCK, QUARANTINE, WRITE_OFF | BR-026 | Return outcome paths |
| `chk_domain_movement_type` | RECEIPT, SHIPMENT, TRANSFER, ADJUSTMENT, WRITE_OFF, RESERVATION, RETURN, PUT_AWAY | BR-017, BR-020 | Movement log taxonomy |

---

## Domain 1: Catalog

### `catalog.products`

| Column | Type | Constraint | Business Rule | Justification |
|--------|------|------------|---------------|---------------|
| `sku` | NOT NULL | `nn_products_sku` | — | SKU is mandatory product identity |
| `sku` | UNIQUE | `uk_products_sku` | BR-027 | Globally unique stock keeping unit |
| `product_name` | NOT NULL | `nn_products_product_name` | — | Product must be identifiable by name in operations |
| `unit_of_measure` | NOT NULL | `nn_products_uom` | — | All inventory quantities require a UOM |
| `lifecycle_status` | NOT NULL | `nn_products_lifecycle_status` | BR-027 | Status governs eligibility for new transactions |
| `lifecycle_status` | DEFAULT | `def_products_lifecycle_status` = 'ACTIVE' | — | New products enter as active |
| `lifecycle_status` | CHECK | `chk_products_lifecycle_status` | BR-027 | Only valid lifecycle states permitted |
| `abc_classification` | CHECK | `chk_products_abc_classification` | BR-032 | ABC must be A, B, or C when assigned |
| `is_shelf_life` | NOT NULL | `nn_products_is_shelf_life` | BR-014, BR-016 | Shelf-life flag required for MRSL enforcement |
| `is_shelf_life` | DEFAULT | `def_products_is_shelf_life` = FALSE | — | Most products are non-shelf-life |
| `is_traceable` | NOT NULL | `nn_products_is_traceable` | BR-017 | Traceability flag required |
| `is_traceable` | DEFAULT | `def_products_is_traceable` = FALSE | — | Traceability opt-in per product |
| `rotation_policy` | CHECK | `chk_products_rotation_policy` | BR-014, BR-015 | FIFO/FEFO only when specified |
| `(is_traceable, rotation_policy)` | CHECK | `chk_products_traceable_rotation` | BR-017 | Traceable products must declare rotation policy |
| `(is_shelf_life, mrsl_days)` | CHECK | `chk_products_shelf_life_mrsl` | BR-016 | Shelf-life products must have MRSL days > 0 |
| `is_active` | DEFAULT | `def_products_is_active` = TRUE | — | Soft-delete default |
| `version` | DEFAULT | `def_products_version` = 1 | — | Optimistic lock initial value |
| `created_by` | FOREIGN KEY | `fk_products_created_by` → `identity.user_accounts` | BO-19 | Product creation attribution |

### `catalog.product_identifiers`

| Column | Type | Constraint | Business Rule | Justification |
|--------|------|------------|---------------|---------------|
| `product_id` | NOT NULL | `nn_product_identifiers_product_id` | — | Identifier must belong to a product |
| `product_id` | FOREIGN KEY | `fk_product_identifiers_product` → `catalog.products` | BR-004 | Parent product must exist for scan lookup |
| `identifier_type` | NOT NULL | `nn_product_identifiers_type` | BR-004 | Type distinguishes barcode from vendor code |
| `identifier_value` | NOT NULL | `nn_product_identifiers_value` | BR-004 | Empty identifier unusable at scan |
| `(identifier_type, identifier_value)` | UNIQUE | `uk_product_identifiers_type_value` | BR-004 | One product per scan code globally |
| `(product_id, identifier_type, identifier_value)` | UNIQUE | `uk_product_identifiers_composite` | — | No duplicate identifiers on same product |
| `is_primary` | NOT NULL | `nn_product_identifiers_is_primary` | — | Primary flag must be explicit |
| `is_primary` | DEFAULT | `def_product_identifiers_is_primary` = FALSE | — | Non-primary by default |
| `is_active` | DEFAULT | `def_product_identifiers_is_active` = TRUE | — | Active identifier by default |

---

## Domain 2: Network

### `network.inventory_locations`

| Column | Type | Constraint | Business Rule | Justification |
|--------|------|------------|---------------|---------------|
| `location_code` | NOT NULL | `nn_inventory_locations_code` | — | Location code is mandatory network identity |
| `location_code` | UNIQUE | `uk_inventory_locations_code` | — | Unique site identifier across network |
| `location_name` | NOT NULL | `nn_inventory_locations_name` | — | Human-readable site name required |
| `location_type` | NOT NULL | `nn_inventory_locations_type` | — | Type drives operational capabilities |
| `location_type` | CHECK | `chk_inventory_locations_type` IN (WAREHOUSE, STORE, DISTRIBUTION_POINT) | — | Valid location types only |
| `parent_location_id` | FOREIGN KEY | `fk_inventory_locations_parent` → self | — | Hierarchy reference must be valid location |
| `parent_location_id` | CHECK | `chk_inventory_locations_not_self_parent` id ≠ parent_location_id | — | Location cannot be its own parent |
| `operational_status` | NOT NULL | `nn_inventory_locations_status` | BR-024 | Status controls transaction eligibility |
| `operational_status` | DEFAULT | `def_inventory_locations_status` = 'ACTIVE' | — | New locations active by default |
| `operational_status` | CHECK | `chk_inventory_locations_status` | — | ACTIVE, PLANNED, CLOSING, INACTIVE only |
| `is_frozen` | NOT NULL | `nn_inventory_locations_is_frozen` | BR-024 | Freeze flag must be explicit during wall count |
| `is_frozen` | DEFAULT | `def_inventory_locations_is_frozen` = FALSE | BR-024 | Locations not frozen by default |
| `responsible_manager_id` | FOREIGN KEY | `fk_inventory_locations_manager` → `identity.user_accounts` | — | Optional manager accountability |
| `country_code` | CHECK | `chk_inventory_locations_country` length = 2 | — | ISO 3166-1 alpha-2 when provided |

### `network.storage_positions`

| Column | Type | Constraint | Business Rule | Justification |
|--------|------|------------|---------------|---------------|
| `location_id` | NOT NULL | `nn_storage_positions_location_id` | BR-005 | Position must belong to a location |
| `location_id` | FOREIGN KEY | `fk_storage_positions_location` → `network.inventory_locations` | REL-004 | Composition within location aggregate |
| `position_code` | NOT NULL | `nn_storage_positions_code` | BR-005 | Bin address required for put-away |
| `(location_id, position_code)` | UNIQUE | `uk_storage_positions_location_code` | — | Code unique within location only |
| `storage_type` | NOT NULL | `nn_storage_positions_type` | BR-030 | Storage type drives bonded/quarantine routing |
| `storage_type` | DEFAULT | `def_storage_positions_type` = 'BULK' | — | Default bulk storage |
| `storage_type` | CHECK | `chk_storage_positions_type` IN (BULK, PICK_FACE, QUARANTINE, BONDED) | BR-030 | Valid storage classifications |
| `capacity_units` | CHECK | `chk_storage_positions_capacity` >= 0 OR NULL | — | Capacity cannot be negative |
| `dedicated_product_id` | FOREIGN KEY | `fk_storage_positions_product` → `catalog.products` | — | Dedicated bin references valid product |
| `(is_dedicated, dedicated_product_id)` | CHECK | `chk_storage_positions_dedicated` | — | Dedicated product required when is_dedicated = TRUE |

---

## Domain 3: Governance

### `governance.governance_policies`

| Column | Type | Constraint | Business Rule | Justification |
|--------|------|------------|---------------|---------------|
| `policy_code` | NOT NULL | `nn_governance_policies_code` | BR-021 | Policy must be identifiable |
| `policy_name` | NOT NULL | `nn_governance_policies_name` | — | Human-readable policy label |
| `policy_type` | NOT NULL | `nn_governance_policies_type` | BR-021 | Type determines enforcement context |
| `policy_type` | CHECK | `chk_governance_policies_type` | — | APPROVAL_THRESHOLD, TOLERANCE, ACCESS, EXCEPTION |
| `effective_from` | NOT NULL | `nn_governance_policies_effective_from` | BR-021 | Policy must have effective start |
| `(effective_from, effective_to)` | CHECK | `chk_governance_policies_dates` effective_to IS NULL OR effective_to > effective_from | — | No inverted effective periods |
| `(policy_code, effective_from)` | UNIQUE | `uk_governance_policies_code_from` | BR-021 | One version per code per effective date |
| `threshold_value` | CHECK | `chk_governance_policies_threshold` >= 0 OR NULL | BR-021 | Thresholds are non-negative |
| `is_active` | DEFAULT | `def_governance_policies_is_active` = TRUE | — | Active policy by default |

### `governance.reason_codes`

| Column | Type | Constraint | Business Rule | Justification |
|--------|------|------------|---------------|---------------|
| `reason_code` | NOT NULL | `nn_reason_codes_code` | BR-020 | Reason code mandatory on adjustments |
| `reason_code` | UNIQUE | `uk_reason_codes_code` | BR-020 | Unique taxonomy key |
| `description` | NOT NULL | `nn_reason_codes_description` | BR-020 | Operators must understand reason meaning |
| `category` | NOT NULL | `nn_reason_codes_category` | BR-020 | Category drives reporting and analysis |
| `category` | CHECK | `chk_reason_codes_category` | BR-020 | Valid adjustment/discrepancy categories |
| `approval_threshold_id` | FOREIGN KEY | `fk_reason_codes_policy` → `governance.governance_policies` | BR-021 | Links to approval threshold when applicable |
| `is_active` | NOT NULL | `nn_reason_codes_is_active` | BR-020 | Retired codes must be flagged, not deleted |
| `is_active` | DEFAULT | `def_reason_codes_is_active` = TRUE | BR-020 | New codes active by default |

---

## Domain 4: Inventory Balance

### `inventory.stock_positions`

| Column | Type | Constraint | Business Rule | Justification |
|--------|------|------------|---------------|---------------|
| `product_id` | NOT NULL | `nn_stock_positions_product_id` | — | Balance must reference a product |
| `product_id` | FOREIGN KEY | `fk_stock_positions_product` → `catalog.products` | BR-001 | Valid catalog product required |
| `location_id` | NOT NULL | `nn_stock_positions_location_id` | — | Balance must reference a location |
| `location_id` | FOREIGN KEY | `fk_stock_positions_location` → `network.inventory_locations` | BR-001 | Valid location required |
| `(product_id, location_id)` | UNIQUE | `uk_stock_positions_product_location` | BR-001, LDM-04 | One authoritative balance per SKU per site |
| `on_hand_qty` | NOT NULL | `nn_stock_positions_on_hand` | LDM-01 | On-hand is mandatory quantity |
| `on_hand_qty` | DEFAULT | `def_stock_positions_on_hand` = 0 | — | Zero balance at creation |
| `on_hand_qty` | CHECK | `chk_stock_positions_on_hand` >= 0 | LDM-01 | On-hand never negative |
| `reserved_qty` | NOT NULL | `nn_stock_positions_reserved` | BR-002 | Reserved quantity always tracked |
| `reserved_qty` | DEFAULT | `def_stock_positions_reserved` = 0 | BR-002 | No reservation at creation |
| `reserved_qty` | CHECK | `chk_stock_positions_reserved` >= 0 | BR-002 | Reserved cannot be negative |
| `reserved_qty` | CHECK | `chk_stock_positions_reserved_le_on_hand` reserved_qty <= on_hand_qty | BR-002 | Cannot reserve more than on-hand |
| `quarantined_qty` | NOT NULL | `nn_stock_positions_quarantined` | BR-013 | Quarantined quantity always tracked |
| `quarantined_qty` | DEFAULT | `def_stock_positions_quarantined` = 0 | BR-013 | No quarantine at creation |
| `quarantined_qty` | CHECK | `chk_stock_positions_quarantined` >= 0 | BR-013 | Quarantine qty non-negative |
| `quarantined_qty` | CHECK | `chk_stock_positions_quarantine_le_on_hand` quarantined_qty <= on_hand_qty | BR-013 | Hold cannot exceed on-hand |
| `atp_qty` | NOT NULL | `nn_stock_positions_atp` | BR-001 | ATP is mandatory availability measure |
| `atp_qty` | DEFAULT | `def_stock_positions_atp` = 0 | BR-001 | Zero ATP at creation |
| `atp_qty` | CHECK | `chk_stock_positions_atp` >= 0 | BR-001 | ATP never negative |
| `atp_qty` | CHECK | `chk_stock_positions_atp_le_on_hand` atp_qty <= on_hand_qty | BR-001 | ATP cannot exceed on-hand |
| `(on_hand_qty, reserved_qty, quarantined_qty, atp_qty)` | CHECK | `chk_stock_positions_atp_formula` atp_qty = on_hand_qty - reserved_qty - quarantined_qty | BR-001, LDM-01 | ATP formula integrity at persistence |
| `inbound_expected_qty` | NOT NULL | `nn_stock_positions_inbound_expected` | BR-005 | Pipeline qty tracked separately from ATP |
| `inbound_expected_qty` | DEFAULT | `def_stock_positions_inbound_expected` = 0 | BR-005 | Informational only — not ATP |
| `inbound_expected_qty` | CHECK | `chk_stock_positions_inbound_expected` >= 0 | BR-005 | Expected inbound non-negative |
| `stock_status` | NOT NULL | `nn_stock_positions_status` | BR-009 | Status indicator mandatory |
| `stock_status` | DEFAULT | `def_stock_positions_status` = 'IN_STOCK' | — | Default healthy status |
| `stock_status` | CHECK | `chk_stock_positions_status` IN (IN_STOCK, LOW_STOCK, OUT_OF_STOCK, OVERSTOCK) | BR-009 | Valid status values |
| `ownership_type` | NOT NULL | `nn_stock_positions_ownership` | BR-031 | Ownership classification required |
| `ownership_type` | DEFAULT | `def_stock_positions_ownership` = 'OWNED' | BR-031 | Owned stock by default |
| `ownership_type` | CHECK | `chk_stock_positions_ownership` | BR-031, BR-030 | OWNED, CONSIGNMENT, BONDED only |
| `version` | DEFAULT | `def_stock_positions_version` = 1 | — | Optimistic lock for concurrent reservations |

### `inventory.lot_batches`

| Column | Type | Constraint | Business Rule | Justification |
|--------|------|------------|---------------|---------------|
| `stock_position_id` | NOT NULL | `nn_lot_batches_position_id` | BR-017 | Lot belongs to a stock position |
| `stock_position_id` | FOREIGN KEY | `fk_lot_batches_position` → `inventory.stock_positions` | BR-017 | Parent balance must exist |
| `product_id` | NOT NULL | `nn_lot_batches_product_id` | BR-017 | Lot scoped to product |
| `product_id` | FOREIGN KEY | `fk_lot_batches_product` → `catalog.products` | BR-017 | Denormalized product for FEFO queries |
| `lot_number` | NOT NULL | `nn_lot_batches_lot_number` | BR-017 | Lot identity mandatory for traceable products |
| `(product_id, lot_number, stock_position_id)` | UNIQUE | `uk_lot_batches_composite` | BR-017 | One lot row per position |
| `quantity` | NOT NULL | `nn_lot_batches_quantity` | BR-017 | Lot quantity required |
| `quantity` | DEFAULT | `def_lot_batches_quantity` = 0 | — | Zero at lot creation |
| `quantity` | CHECK | `chk_lot_batches_quantity` >= 0 | LDM-01 | Lot quantity non-negative |
| `(expiration_date, manufacture_date)` | CHECK | `chk_lot_batches_dates` expiration IS NULL OR manufacture IS NULL OR expiration >= manufacture | BR-014 | Expiration after manufacture |
| `quality_status` | NOT NULL | `nn_lot_batches_quality` | BR-013 | Quality status required |
| `quality_status` | DEFAULT | `def_lot_batches_quality` = 'ACCEPTED' | — | Accepted at receipt default |
| `quality_status` | CHECK | `chk_lot_batches_quality` IN (ACCEPTED, HOLD, REJECTED) | BR-013 | Valid quality states |
| `supplier_id` | FOREIGN KEY | `fk_lot_batches_supplier` → `procurement.suppliers` | BR-017 | Supplier origin for recall traceability |

### `inventory.quarantine_holds`

| Column | Type | Constraint | Business Rule | Justification |
|--------|------|------------|---------------|---------------|
| `hold_reference` | NOT NULL | `nn_quarantine_holds_reference` | BR-013 | Hold document identity |
| `hold_reference` | UNIQUE | `uk_quarantine_holds_reference` | BR-013 | Unique hold reference |
| `stock_position_id` | NOT NULL | `nn_quarantine_holds_position_id` | BR-013 | Hold applied to specific balance |
| `stock_position_id` | FOREIGN KEY | `fk_quarantine_holds_position` → `inventory.stock_positions` | BR-013 | Valid balance required |
| `lot_batch_id` | FOREIGN KEY | `fk_quarantine_holds_lot` → `inventory.lot_batches` | BR-013 | Optional lot-scoped hold |
| `held_qty` | NOT NULL | `nn_quarantine_holds_held_qty` | BR-013 | Held quantity mandatory |
| `held_qty` | CHECK | `chk_quarantine_holds_held_qty` > 0 | BR-013 | Hold must affect positive quantity |
| `hold_type` | NOT NULL | `nn_quarantine_holds_type` | BR-013, BR-030 | Hold classification required |
| `hold_type` | CHECK | `chk_quarantine_holds_type` | BR-013, BR-030 | Valid hold types |
| `hold_reason` | NOT NULL | `nn_quarantine_holds_reason` | BR-013 | Hold must be justified |
| `hold_status` | NOT NULL | `nn_quarantine_holds_status` | BR-013 | Lifecycle state required |
| `hold_status` | DEFAULT | `def_quarantine_holds_status` = 'ACTIVE' | BR-013 | Active hold by default |
| `hold_status` | CHECK | `chk_quarantine_holds_status` IN (ACTIVE, RELEASED, DISPOSED) | BR-013 | Valid hold lifecycle |
| `hold_start_at` | NOT NULL | `nn_quarantine_holds_start` | BR-013 | Hold effective time required |
| `hold_start_at` | DEFAULT | `def_quarantine_holds_start` = NOW() | BR-013 | Auto-stamp hold start |
| `(hold_status, released_at)` | CHECK | `chk_quarantine_holds_release` | BR-013 | RELEASED status requires released_at |
| `authorized_by` | FOREIGN KEY | `fk_quarantine_holds_authorized_by` → `identity.user_accounts` | BR-013 | Hold authorization attribution |

### `inventory.stock_policies`

| Column | Type | Constraint | Business Rule | Justification |
|--------|------|------------|---------------|---------------|
| `product_id` | NOT NULL | `nn_stock_policies_product_id` | BR-009 | Policy scoped to product |
| `product_id` | FOREIGN KEY | `fk_stock_policies_product` → `catalog.products` | BR-009 | Valid product required |
| `location_id` | NOT NULL | `nn_stock_policies_location_id` | BR-009 | Policy scoped to location |
| `location_id` | FOREIGN KEY | `fk_stock_policies_location` → `network.inventory_locations` | BR-009 | Valid location required |
| `(product_id, location_id)` | UNIQUE | `uk_stock_policies_product_location` | BR-009, LDM-04 | One policy per SKU per site |
| `reorder_level` | NOT NULL | `nn_stock_policies_reorder` | BR-009 | Reorder trigger required |
| `reorder_level` | DEFAULT | `def_stock_policies_reorder` = 0 | — | Zero default |
| `reorder_level` | CHECK | `chk_stock_policies_reorder` >= 0 | BR-009 | Non-negative threshold |
| `minimum_threshold` | NOT NULL | `nn_stock_policies_minimum` | BR-010, BR-012 | Minimum floor required |
| `minimum_threshold` | DEFAULT | `def_stock_policies_minimum` = 0 | — | Zero default |
| `minimum_threshold` | CHECK | `chk_stock_policies_minimum` >= 0 | BR-010 | Non-negative minimum |
| `safety_stock_qty` | NOT NULL | `nn_stock_policies_safety` | BR-010 | Safety stock required |
| `safety_stock_qty` | DEFAULT | `def_stock_policies_safety` = 0 | BR-010 | Zero default |
| `safety_stock_qty` | CHECK | `chk_stock_policies_safety` >= 0 | BR-010 | Safety stock non-negative |
| `(minimum_threshold, reorder_level)` | CHECK | `chk_stock_policies_threshold_order` minimum_threshold <= reorder_level | BR-009, BR-010 | Minimum ≤ reorder unless authorized exception |
| `maximum_stock_level` | CHECK | `chk_stock_policies_maximum` > reorder_level OR NULL | — | Overstock level above reorder when set |
| `lead_time_days` | CHECK | `chk_stock_policies_lead_time` > 0 OR NULL | — | Lead time must be positive |
| `effective_from` | NOT NULL | `nn_stock_policies_effective_from` | BR-009 | Effective dating required |
| `effective_from` | DEFAULT | `def_stock_policies_effective_from` = NOW() | — | Current timestamp default |

### `inventory.stock_policy_history`

| Column | Type | Constraint | Business Rule | Justification |
|--------|------|------------|---------------|---------------|
| `stock_policy_id` | NOT NULL | `nn_stock_policy_history_policy_id` | BR-009 | History belongs to policy |
| `stock_policy_id` | FOREIGN KEY | `fk_stock_policy_history_policy` → `inventory.stock_policies` | BR-009 | Parent policy must exist |
| `reorder_level` | NOT NULL | `nn_stock_policy_history_reorder` | BR-009 | Historical value captured |
| `minimum_threshold` | NOT NULL | `nn_stock_policy_history_minimum` | BR-010 | Historical value captured |
| `safety_stock_qty` | NOT NULL | `nn_stock_policy_history_safety` | BR-010 | Historical value captured |
| `effective_from` | NOT NULL | `nn_stock_policy_history_from` | BR-009 | Period start required |
| `effective_to` | NOT NULL | `nn_stock_policy_history_to` | BR-009 | Period end required |
| `(effective_from, effective_to)` | CHECK | `chk_stock_policy_history_dates` effective_to > effective_from | BR-009 | Valid history window |
| `(stock_policy_id, effective_from)` | UNIQUE | `uk_stock_policy_history_policy_from` | BR-009 | Non-overlapping history periods |
| `changed_by` | FOREIGN KEY | `fk_stock_policy_history_changed_by` → `identity.user_accounts` | BO-19 | Change attribution |

---

## Domain 5: Procurement

### `procurement.suppliers`

| Column | Type | Constraint | Business Rule | Justification |
|--------|------|------------|---------------|---------------|
| `supplier_code` | NOT NULL | `nn_suppliers_code` | BR-007 | Vendor code mandatory |
| `supplier_code` | UNIQUE | `uk_suppliers_code` | BR-007 | Unique commercial counterparty |
| `supplier_name` | NOT NULL | `nn_suppliers_name` | BR-007 | Vendor must be identifiable |
| `payment_terms_days` | NOT NULL | `nn_suppliers_payment_terms` | BR-008 | Payment terms required before PO |
| `payment_terms_days` | DEFAULT | `def_suppliers_payment_terms` = 30 | — | Standard net-30 default |
| `payment_terms_days` | CHECK | `chk_suppliers_payment_terms` > 0 | BR-008 | Positive payment terms |
| `is_consignment` | NOT NULL | `nn_suppliers_is_consignment` | BR-031 | Consignment flag explicit |
| `is_consignment` | DEFAULT | `def_suppliers_is_consignment` = FALSE | BR-031 | Standard purchase by default |
| `delivery_rating` | CHECK | `chk_suppliers_rating` BETWEEN 0 AND 5 OR NULL | — | Valid rating scale |
| `default_lead_time_days` | CHECK | `chk_suppliers_lead_time` > 0 OR NULL | — | Positive lead time when set |

### `procurement.purchase_requisitions`

| Column | Type | Constraint | Business Rule | Justification |
|--------|------|------------|---------------|---------------|
| `requisition_number` | NOT NULL | `nn_purchase_requisitions_number` | BR-009 | Internal document identity |
| `requisition_number` | UNIQUE | `uk_purchase_requisitions_number` | — | Unique requisition reference |
| `requesting_location_id` | NOT NULL | `nn_purchase_requisitions_location` | BR-009 | Replenishment destination required |
| `requesting_location_id` | FOREIGN KEY | `fk_purchase_requisitions_location` → `network.inventory_locations` | BR-009 | Valid receiving site |
| `approval_status` | NOT NULL | `nn_purchase_requisitions_status` | BR-009 | Workflow state required |
| `approval_status` | DEFAULT | `def_purchase_requisitions_status` = 'DRAFT' | — | Starts as draft |
| `approval_status` | CHECK | `chk_purchase_requisitions_status` IN (DRAFT, SUBMITTED, APPROVED, REJECTED, CONVERTED) | BR-009 | Valid approval states |
| `(approval_status, approved_by)` | CHECK | `chk_purchase_requisitions_approval` | BR-021 | APPROVED requires approver |
| `triggering_alert_id` | FOREIGN KEY | `fk_purchase_requisitions_alert` → `audit.operational_alerts` | BR-009 | Alert-to-requisition traceability |
| `approved_by` | FOREIGN KEY | `fk_purchase_requisitions_approved_by` → `identity.user_accounts` | BR-021 | Approver attribution |
| `purchase_order_id` | FOREIGN KEY | `fk_purchase_requisitions_po` → `procurement.purchase_orders` | BR-009 | PO conversion link |
| `created_by` | NOT NULL | `nn_purchase_requisitions_created_by` | BO-19 | Initiator required |
| `created_by` | FOREIGN KEY | `fk_purchase_requisitions_created_by` → `identity.user_accounts` | BO-19 | Initiator attribution |

### `procurement.purchase_requisition_lines`

| Column | Type | Constraint | Business Rule | Justification |
|--------|------|------------|---------------|---------------|
| `requisition_id` | NOT NULL | `nn_purchase_requisition_lines_req_id` | — | Line belongs to requisition |
| `requisition_id` | FOREIGN KEY | `fk_purchase_requisition_lines_req` → `procurement.purchase_requisitions` | — | Parent document exists |
| `line_number` | NOT NULL | `nn_purchase_requisition_lines_line` | — | Line sequence required |
| `line_number` | CHECK | `chk_purchase_requisition_lines_line` > 0 | — | Positive line numbers |
| `(requisition_id, line_number)` | UNIQUE | `uk_purchase_requisition_lines_req_line` | — | Unique line per requisition |
| `product_id` | NOT NULL | `nn_purchase_requisition_lines_product` | BR-027 | Product required |
| `product_id` | FOREIGN KEY | `fk_purchase_requisition_lines_product` → `catalog.products` | BR-027 | Active product validation at application layer |
| `requested_qty` | NOT NULL | `nn_purchase_requisition_lines_qty` | BR-009 | Quantity required |
| `requested_qty` | CHECK | `chk_purchase_requisition_lines_qty` > 0 | BR-009 | Positive requested quantity |

### `procurement.purchase_orders`

| Column | Type | Constraint | Business Rule | Justification |
|--------|------|------------|---------------|---------------|
| `po_number` | NOT NULL | `nn_purchase_orders_number` | BR-007 | PO document identity |
| `po_number` | UNIQUE | `uk_purchase_orders_number` | BR-007 | Unique authorization document |
| `supplier_id` | NOT NULL | `nn_purchase_orders_supplier` | BR-007 | PO requires supplier |
| `supplier_id` | FOREIGN KEY | `fk_purchase_orders_supplier` → `procurement.suppliers` | BR-007 | Valid active supplier |
| `receiving_location_id` | NOT NULL | `nn_purchase_orders_location` | BR-007 | Receiving site required |
| `receiving_location_id` | FOREIGN KEY | `fk_purchase_orders_location` → `network.inventory_locations` | BR-007 | Valid receiving location |
| `order_date` | NOT NULL | `nn_purchase_orders_order_date` | BR-007 | PO date mandatory |
| `po_status` | NOT NULL | `nn_purchase_orders_status` | BR-007 | PO lifecycle state |
| `po_status` | DEFAULT | `def_purchase_orders_status` = 'OPEN' | BR-007 | New POs open |
| `po_status` | CHECK | `chk_purchase_orders_status` | BR-007 | OPEN, PARTIAL, CLOSED, CANCELLED |
| `total_commitment_amount` | NOT NULL | `nn_purchase_orders_total` | BR-008 | Financial commitment tracked |
| `total_commitment_amount` | DEFAULT | `def_purchase_orders_total` = 0 | — | Zero until lines added |
| `total_commitment_amount` | CHECK | `chk_purchase_orders_total` >= 0 | BR-008 | Non-negative commitment |
| `currency_code` | NOT NULL | `nn_purchase_orders_currency` | BR-008 | Currency required |
| `currency_code` | DEFAULT | `def_purchase_orders_currency` = 'USD' | — | Default currency |
| `currency_code` | CHECK | `chk_purchase_orders_currency` length = 3 | — | ISO 4217 format |
| `payment_terms_days` | NOT NULL | `nn_purchase_orders_terms` | BR-008 | Terms on PO |
| `payment_terms_days` | DEFAULT | `def_purchase_orders_terms` = 30 | — | Default net-30 |
| `created_by` | NOT NULL | `nn_purchase_orders_created_by` | BO-19 | Buyer attribution |
| `created_by` | FOREIGN KEY | `fk_purchase_orders_created_by` → `identity.user_accounts` | BO-19 | Buyer identity |

### `procurement.purchase_order_lines`

| Column | Type | Constraint | Business Rule | Justification |
|--------|------|------------|---------------|---------------|
| `purchase_order_id` | NOT NULL | `nn_purchase_order_lines_po_id` | BR-007 | Line belongs to PO |
| `purchase_order_id` | FOREIGN KEY | `fk_purchase_order_lines_po` → `procurement.purchase_orders` | BR-007 | Parent PO exists |
| `line_number` | NOT NULL | `nn_purchase_order_lines_line` | — | Line sequence required |
| `line_number` | CHECK | `chk_purchase_order_lines_line` > 0 | — | Positive line number |
| `(purchase_order_id, line_number)` | UNIQUE | `uk_purchase_order_lines_po_line` | — | Unique line per PO |
| `product_id` | NOT NULL | `nn_purchase_order_lines_product` | BR-027 | Product required |
| `product_id` | FOREIGN KEY | `fk_purchase_order_lines_product` → `catalog.products` | BR-027 | Discontinued blocked at app layer |
| `ordered_qty` | NOT NULL | `nn_purchase_order_lines_ordered` | BR-007 | Ordered quantity required |
| `ordered_qty` | CHECK | `chk_purchase_order_lines_ordered` > 0 | BR-007 | Positive order quantity |
| `received_qty` | NOT NULL | `nn_purchase_order_lines_received` | BR-007 | Received cumulative tracked |
| `received_qty` | DEFAULT | `def_purchase_order_lines_received` = 0 | — | Zero at line creation |
| `received_qty` | CHECK | `chk_purchase_order_lines_received` >= 0 | BR-007 | Non-negative received |
| `received_qty` | CHECK | `chk_purchase_order_lines_received_le_ordered` received_qty <= ordered_qty + tolerance | BR-006, BR-007 | Over-receipt requires discrepancy workflow |
| `unit_price` | NOT NULL | `nn_purchase_order_lines_price` | BR-008 | Price required for match |
| `unit_price` | CHECK | `chk_purchase_order_lines_price` >= 0 | BR-008 | Non-negative price |
| `line_amount` | NOT NULL | `nn_purchase_order_lines_amount` | BR-008 | Extended amount required |
| `line_amount` | CHECK | `chk_purchase_order_lines_amount` >= 0 | BR-008 | Non-negative line value |

### `procurement.expected_inbound_deliveries`

| Column | Type | Constraint | Business Rule | Justification |
|--------|------|------------|---------------|---------------|
| `delivery_reference` | NOT NULL | `nn_expected_inbound_deliveries_ref` | — | Shipment plan identity |
| `delivery_reference` | UNIQUE | `uk_expected_inbound_deliveries_ref` | — | Unique delivery reference |
| `purchase_order_id` | NOT NULL | `nn_expected_inbound_deliveries_po` | BR-007 | Delivery tied to PO |
| `purchase_order_id` | FOREIGN KEY | `fk_expected_inbound_deliveries_po` → `procurement.purchase_orders` | BR-007 | Valid open PO |
| `expected_arrival_date` | NOT NULL | `nn_expected_inbound_deliveries_date` | — | Arrival date required |
| `shipment_status` | NOT NULL | `nn_expected_inbound_deliveries_status` | — | Shipment state required |
| `shipment_status` | DEFAULT | `def_expected_inbound_deliveries_status` = 'PLANNED' | — | Planned by default |
| `shipment_status` | CHECK | `chk_expected_inbound_deliveries_status` IN (PLANNED, IN_TRANSIT, ARRIVED, DELAYED) | — | Valid shipment states |
| `receiving_location_id` | NOT NULL | `nn_expected_inbound_deliveries_location` | — | Destination required |
| `receiving_location_id` | FOREIGN KEY | `fk_expected_inbound_deliveries_location` → `network.inventory_locations` | — | Valid location |

### `procurement.expected_inbound_delivery_lines`

| Column | Type | Constraint | Business Rule | Justification |
|--------|------|------------|---------------|---------------|
| `delivery_id` | NOT NULL | `nn_expected_inbound_delivery_lines_delivery` | — | Line belongs to delivery |
| `delivery_id` | FOREIGN KEY | `fk_expected_inbound_delivery_lines_delivery` → `procurement.expected_inbound_deliveries` | — | Parent delivery exists |
| `purchase_order_line_id` | NOT NULL | `nn_expected_inbound_delivery_lines_pol` | BR-007 | Links to PO line |
| `purchase_order_line_id` | FOREIGN KEY | `fk_expected_inbound_delivery_lines_pol` → `procurement.purchase_order_lines` | BR-007 | Valid PO line |
| `product_id` | NOT NULL | `nn_expected_inbound_delivery_lines_product` | — | Product required |
| `product_id` | FOREIGN KEY | `fk_expected_inbound_delivery_lines_product` → `catalog.products` | — | Valid product |
| `expected_qty` | NOT NULL | `nn_expected_inbound_delivery_lines_qty` | — | Expected quantity required |
| `expected_qty` | CHECK | `chk_expected_inbound_delivery_lines_qty` > 0 | — | Positive expected qty |
| `(delivery_id, purchase_order_line_id)` | UNIQUE | `uk_expected_inbound_delivery_lines` | — | One entry per PO line per delivery |

---

## Domain 6: Inbound

### `inbound.goods_receipts`

| Column | Type | Constraint | Business Rule | Justification |
|--------|------|------------|---------------|---------------|
| `gr_number` | NOT NULL | `nn_goods_receipts_number` | BR-004 | Receipt document identity |
| `gr_number` | UNIQUE | `uk_goods_receipts_number` | BR-004 | Unique receipt reference |
| `purchase_order_id` | FOREIGN KEY | `fk_goods_receipts_po` → `procurement.purchase_orders` | BR-007 | PO authorization when not ad-hoc |
| `(purchase_order_id, exception_authorization_ref)` | CHECK | `chk_goods_receipts_po_or_exception` | BR-007 | PO or documented exception required |
| `supplier_id` | NOT NULL | `nn_goods_receipts_supplier` | BR-004 | Supplier accountability |
| `supplier_id` | FOREIGN KEY | `fk_goods_receipts_supplier` → `procurement.suppliers` | BR-004 | Valid supplier |
| `receiving_location_id` | NOT NULL | `nn_goods_receipts_location` | BR-004, BR-024 | Receipt site required |
| `receiving_location_id` | FOREIGN KEY | `fk_goods_receipts_location` → `network.inventory_locations` | BR-024 | Location not frozen (app layer) |
| `receipt_date` | NOT NULL | `nn_goods_receipts_date` | BR-004 | Receipt timestamp required |
| `receipt_date` | DEFAULT | `def_goods_receipts_date` = NOW() | BR-004 | Auto-stamp receipt |
| `verification_status` | NOT NULL | `nn_goods_receipts_verification` | BR-004 | Verification state required |
| `verification_status` | DEFAULT | `def_goods_receipts_verification` = 'PENDING' | BR-004 | Pending until verified |
| `verification_status` | CHECK | `chk_goods_receipts_verification` IN (PENDING, VERIFIED, REJECTED, PARTIAL) | BR-004 | Valid verification states |
| `receiving_clerk_id` | NOT NULL | `nn_goods_receipts_clerk` | BO-19 | Receiving clerk required |
| `receiving_clerk_id` | FOREIGN KEY | `fk_goods_receipts_clerk` → `identity.user_accounts` | BO-19 | Clerk attribution |

### `inbound.goods_receipt_lines`

| Column | Type | Constraint | Business Rule | Justification |
|--------|------|------------|---------------|---------------|
| `goods_receipt_id` | NOT NULL | `nn_goods_receipt_lines_gr_id` | BR-004 | Line belongs to receipt |
| `goods_receipt_id` | FOREIGN KEY | `fk_goods_receipt_lines_gr` → `inbound.goods_receipts` | BR-004 | Parent receipt exists |
| `line_number` | NOT NULL | `nn_goods_receipt_lines_line` | — | Line sequence required |
| `(goods_receipt_id, line_number)` | UNIQUE | `uk_goods_receipt_lines_gr_line` | — | Unique line per receipt |
| `product_id` | NOT NULL | `nn_goods_receipt_lines_product` | BR-004 | Product identity required |
| `product_id` | FOREIGN KEY | `fk_goods_receipt_lines_product` → `catalog.products` | BR-004 | Valid product |
| `purchase_order_line_id` | FOREIGN KEY | `fk_goods_receipt_lines_pol` → `procurement.purchase_order_lines` | BR-007 | PO line match when applicable |
| `received_qty` | NOT NULL | `nn_goods_receipt_lines_received` | BR-004 | Received qty required |
| `received_qty` | CHECK | `chk_goods_receipt_lines_received` >= 0 | BR-004 | Non-negative received |
| `accepted_qty` | NOT NULL | `nn_goods_receipt_lines_accepted` | BR-004 | Accepted qty tracked |
| `accepted_qty` | DEFAULT | `def_goods_receipt_lines_accepted` = 0 | BR-004 | Zero until verified |
| `accepted_qty` | CHECK | `chk_goods_receipt_lines_accepted` >= 0 | BR-004 | Non-negative accepted |
| `accepted_qty` | CHECK | `chk_goods_receipt_lines_accepted_le_received` accepted_qty <= received_qty | BR-004 | Cannot accept more than received |
| `condition_grade` | NOT NULL | `nn_goods_receipt_lines_condition` | BR-004 | Condition assessment required |
| `condition_grade` | DEFAULT | `def_goods_receipt_lines_condition` = 'GOOD' | — | Good condition default |
| `condition_grade` | CHECK | `chk_goods_receipt_lines_condition` IN (GOOD, DAMAGED, REJECTED) | BR-004 | Valid condition grades |
| `lot_batch_id` | FOREIGN KEY | `fk_goods_receipt_lines_lot` → `inventory.lot_batches` | BR-017 | Lot when traceable |

### `inbound.receipt_discrepancies`

| Column | Type | Constraint | Business Rule | Justification |
|--------|------|------------|---------------|---------------|
| `discrepancy_reference` | NOT NULL | `nn_receipt_discrepancies_ref` | BR-006 | Discrepancy document identity |
| `discrepancy_reference` | UNIQUE | `uk_receipt_discrepancies_ref` | BR-006 | Unique discrepancy reference |
| `goods_receipt_id` | NOT NULL | `nn_receipt_discrepancies_gr` | BR-006 | Discrepancy at receipt point |
| `goods_receipt_id` | FOREIGN KEY | `fk_receipt_discrepancies_gr` → `inbound.goods_receipts` | BR-006 | Parent receipt exists |
| `goods_receipt_line_id` | FOREIGN KEY | `fk_receipt_discrepancies_gr_line` → `inbound.goods_receipt_lines` | BR-006 | Optional line-level discrepancy |
| `discrepancy_type` | NOT NULL | `nn_receipt_discrepancies_type` | BR-006 | Discrepancy classification |
| `discrepancy_type` | CHECK | `chk_receipt_discrepancies_type` IN (SHORT, OVER, WRONG_ITEM, DAMAGE, SHELF_LIFE) | BR-006, BR-016 | Valid discrepancy types |
| `product_id` | NOT NULL | `nn_receipt_discrepancies_product` | BR-006 | Affected product required |
| `product_id` | FOREIGN KEY | `fk_receipt_discrepancies_product` → `catalog.products` | BR-006 | Valid product |
| `reason_code_id` | FOREIGN KEY | `fk_receipt_discrepancies_reason` → `governance.reason_codes` | BR-006 | Categorized reason |
| `resolution_status` | NOT NULL | `nn_receipt_discrepancies_resolution` | BR-006 | Resolution tracking |
| `resolution_status` | DEFAULT | `def_receipt_discrepancies_resolution` = 'OPEN' | BR-006 | Open until resolved |
| `resolution_status` | CHECK | `chk_receipt_discrepancies_resolution` IN (OPEN, RESOLVED, CLAIMED) | BR-006 | Valid resolution states |

### `inbound.put_aways`

| Column | Type | Constraint | Business Rule | Justification |
|--------|------|------------|---------------|---------------|
| `put_away_reference` | NOT NULL | `nn_put_aways_reference` | BR-005 | Put-away document identity |
| `put_away_reference` | UNIQUE | `uk_put_aways_reference` | BR-005 | Unique put-away reference |
| `goods_receipt_id` | NOT NULL | `nn_put_aways_gr` | BR-005 | Put-away completes receipt |
| `goods_receipt_id` | FOREIGN KEY | `fk_put_aways_gr` → `inbound.goods_receipts` | BR-005 | Parent receipt exists |
| `goods_receipt_line_id` | NOT NULL | `nn_put_aways_gr_line` | BR-005 | Line-level put-away |
| `goods_receipt_line_id` | FOREIGN KEY | `fk_put_aways_gr_line` → `inbound.goods_receipt_lines` | BR-005 | Valid receipt line |
| `product_id` | NOT NULL | `nn_put_aways_product` | BR-005 | Product placed |
| `product_id` | FOREIGN KEY | `fk_put_aways_product` → `catalog.products` | BR-005 | Valid product |
| `quantity` | NOT NULL | `nn_put_aways_quantity` | BR-005 | Put-away quantity required |
| `quantity` | CHECK | `chk_put_aways_quantity` > 0 | BR-005 | Positive placement quantity |
| `storage_position_id` | NOT NULL | `nn_put_aways_position` | BR-005 | Destination bin required |
| `storage_position_id` | FOREIGN KEY | `fk_put_aways_position` → `network.storage_positions` | BR-005, BR-014 | Valid storage for rotation |
| `lot_batch_id` | FOREIGN KEY | `fk_put_aways_lot` → `inventory.lot_batches` | BR-017 | Lot placement when traceable |
| `put_away_at` | NOT NULL | `nn_put_aways_at` | BR-005 | Completion time required |
| `put_away_at` | DEFAULT | `def_put_aways_at` = NOW() | BR-005 | Auto-stamp completion |
| `availability_effective_at` | NOT NULL | `nn_put_aways_availability` | BR-005 | ATP effective time required |
| `availability_effective_at` | DEFAULT | `def_put_aways_availability` = NOW() | BR-005 | ATP starts at put-away |
| `performed_by` | NOT NULL | `nn_put_aways_performed_by` | BO-19 | Staff attribution required |
| `performed_by` | FOREIGN KEY | `fk_put_aways_performed_by` → `identity.user_accounts` | BO-19 | Performer identity |

---

## Domain 7: Finance

### `finance.supplier_invoices`

| Column | Type | Constraint | Business Rule | Justification |
|--------|------|------------|---------------|---------------|
| `invoice_number` | NOT NULL | `nn_supplier_invoices_number` | BR-008 | Invoice identity required |
| `(supplier_id, invoice_number)` | UNIQUE | `uk_supplier_invoices_supplier_number` | BR-008 | Unique within supplier |
| `supplier_id` | NOT NULL | `nn_supplier_invoices_supplier` | BR-008 | Billing party required |
| `supplier_id` | FOREIGN KEY | `fk_supplier_invoices_supplier` → `procurement.suppliers` | BR-008 | Valid supplier |
| `purchase_order_id` | NOT NULL | `nn_supplier_invoices_po` | BR-008 | PO leg of three-way match |
| `purchase_order_id` | FOREIGN KEY | `fk_supplier_invoices_po` → `procurement.purchase_orders` | BR-008 | Valid PO reference |
| `invoice_date` | NOT NULL | `nn_supplier_invoices_date` | BR-008 | Invoice date required |
| `total_amount` | NOT NULL | `nn_supplier_invoices_total` | BR-008 | Invoice total required |
| `total_amount` | CHECK | `chk_supplier_invoices_total` >= 0 | BR-008 | Non-negative invoice |
| `currency_code` | NOT NULL | `nn_supplier_invoices_currency` | BR-008 | Currency required |
| `currency_code` | DEFAULT | `def_supplier_invoices_currency` = 'USD' | — | Default currency |
| `match_status` | NOT NULL | `nn_supplier_invoices_match` | BR-008 | Match state required |
| `match_status` | DEFAULT | `def_supplier_invoices_match` = 'PENDING' | BR-008 | Pending until matched |
| `match_status` | CHECK | `chk_supplier_invoices_match` IN (PENDING, MATCHED, EXCEPTION) | BR-008 | Valid match states |
| `payment_status` | NOT NULL | `nn_supplier_invoices_payment` | BR-008 | Payment gate required |
| `payment_status` | DEFAULT | `def_supplier_invoices_payment` = 'UNAUTHORIZED' | BR-008 | Unauthorized until matched |
| `payment_status` | CHECK | `chk_supplier_invoices_payment` IN (UNAUTHORIZED, AUTHORIZED, PAID) | BR-008 | Valid payment states |
| `(match_status, payment_status)` | CHECK | `chk_supplier_invoices_payment_gate` | BR-008 | AUTHORIZED/PAID only when MATCHED |

### `finance.supplier_invoice_lines`

| Column | Type | Constraint | Business Rule | Justification |
|--------|------|------------|---------------|---------------|
| `supplier_invoice_id` | NOT NULL | `nn_supplier_invoice_lines_invoice` | BR-008 | Line belongs to invoice |
| `supplier_invoice_id` | FOREIGN KEY | `fk_supplier_invoice_lines_invoice` → `finance.supplier_invoices` | BR-008 | Parent invoice exists |
| `line_number` | NOT NULL | `nn_supplier_invoice_lines_line` | — | Line sequence required |
| `(supplier_invoice_id, line_number)` | UNIQUE | `uk_supplier_invoice_lines_inv_line` | — | Unique line per invoice |
| `product_id` | NOT NULL | `nn_supplier_invoice_lines_product` | BR-008 | Billed product required |
| `product_id` | FOREIGN KEY | `fk_supplier_invoice_lines_product` → `catalog.products` | BR-008 | Valid product |
| `purchase_order_line_id` | FOREIGN KEY | `fk_supplier_invoice_lines_pol` → `procurement.purchase_order_lines` | BR-008 | PO line match |
| `billed_qty` | NOT NULL | `nn_supplier_invoice_lines_qty` | BR-008 | Billed quantity required |
| `billed_qty` | CHECK | `chk_supplier_invoice_lines_qty` > 0 | BR-008 | Positive billed qty |
| `unit_price` | NOT NULL | `nn_supplier_invoice_lines_price` | BR-008 | Unit price required |
| `unit_price` | CHECK | `chk_supplier_invoice_lines_price` >= 0 | BR-008 | Non-negative price |
| `line_amount` | NOT NULL | `nn_supplier_invoice_lines_amount` | BR-008 | Extended amount required |

### `finance.invoice_goods_receipt_match`

| Column | Type | Constraint | Business Rule | Justification |
|--------|------|------------|---------------|---------------|
| `supplier_invoice_id` | NOT NULL | `nn_inv_gr_match_invoice` | BR-008 | Invoice in match set |
| `supplier_invoice_id` | FOREIGN KEY | `fk_inv_gr_match_invoice` → `finance.supplier_invoices` | BR-008 | Valid invoice |
| `goods_receipt_id` | NOT NULL | `nn_inv_gr_match_gr` | BR-008 | Receipt in match set |
| `goods_receipt_id` | FOREIGN KEY | `fk_inv_gr_match_gr` → `inbound.goods_receipts` | BR-008 | Valid receipt |
| `(supplier_invoice_id, goods_receipt_id)` | UNIQUE | `uk_inv_gr_match_pair` | BR-008 | One match record per pair |
| `match_status` | NOT NULL | `nn_inv_gr_match_status` | BR-008 | Match outcome tracked |
| `match_status` | DEFAULT | `def_inv_gr_match_status` = 'PENDING' | BR-008 | Pending by default |
| `match_status` | CHECK | `chk_inv_gr_match_status` IN (PENDING, MATCHED, EXCEPTION) | BR-008 | Valid match states |

---

## Domain 8: Fulfillment

### `fulfillment.customer_orders`

| Column | Type | Constraint | Business Rule | Justification |
|--------|------|------------|---------------|---------------|
| `order_number` | NOT NULL | `nn_customer_orders_number` | BR-001 | Order document identity |
| `order_number` | UNIQUE | `uk_customer_orders_number` | — | Unique order reference |
| `order_date` | NOT NULL | `nn_customer_orders_date` | — | Order date required |
| `order_date` | DEFAULT | `def_customer_orders_date` = NOW() | — | Auto-stamp order date |
| `order_status` | NOT NULL | `nn_customer_orders_status` | BR-001, BR-002 | Lifecycle state required |
| `order_status` | DEFAULT | `def_customer_orders_status` = 'DRAFT' | — | Draft until confirmed |
| `order_status` | CHECK | `chk_customer_orders_status` | BR-001 | DRAFT, CONFIRMED, PARTIAL, FULFILLED, CANCELLED |

### `fulfillment.customer_order_lines`

| Column | Type | Constraint | Business Rule | Justification |
|--------|------|------------|---------------|---------------|
| `customer_order_id` | NOT NULL | `nn_customer_order_lines_order` | — | Line belongs to order |
| `customer_order_id` | FOREIGN KEY | `fk_customer_order_lines_order` → `fulfillment.customer_orders` | — | Parent order exists |
| `line_number` | NOT NULL | `nn_customer_order_lines_line` | — | Line sequence required |
| `(customer_order_id, line_number)` | UNIQUE | `uk_customer_order_lines_order_line` | — | Unique line per order |
| `product_id` | NOT NULL | `nn_customer_order_lines_product` | BR-027 | Product required |
| `product_id` | FOREIGN KEY | `fk_customer_order_lines_product` → `catalog.products` | BR-027 | Valid product |
| `requested_qty` | NOT NULL | `nn_customer_order_lines_requested` | BR-001 | Requested qty required |
| `requested_qty` | CHECK | `chk_customer_order_lines_requested` > 0 | BR-001 | Positive order quantity |
| `fulfilled_qty` | NOT NULL | `nn_customer_order_lines_fulfilled` | BR-003 | Fulfilled tracked |
| `fulfilled_qty` | DEFAULT | `def_customer_order_lines_fulfilled` = 0 | — | Zero at creation |
| `fulfilled_qty` | CHECK | `chk_customer_order_lines_fulfilled` >= 0 | BR-003 | Non-negative fulfilled |
| `backordered_qty` | NOT NULL | `nn_customer_order_lines_backordered` | BR-028 | Backorder tracked |
| `backordered_qty` | DEFAULT | `def_customer_order_lines_backordered` = 0 | BR-028 | Zero at creation |
| `backordered_qty` | CHECK | `chk_customer_order_lines_backordered` >= 0 | BR-028 | Non-negative backorder |
| `(requested_qty, fulfilled_qty, backordered_qty)` | CHECK | `chk_customer_order_lines_qty_balance` fulfilled + backordered <= requested | BR-001, BR-028 | Line quantity reconciliation |
| `fulfillment_location_id` | FOREIGN KEY | `fk_customer_order_lines_location` → `network.inventory_locations` | BR-001 | Ship-from site |

### `fulfillment.inventory_reservations`

| Column | Type | Constraint | Business Rule | Justification |
|--------|------|------------|---------------|---------------|
| `reservation_reference` | NOT NULL | `nn_inventory_reservations_ref` | BR-002 | Reservation document identity |
| `reservation_reference` | UNIQUE | `uk_inventory_reservations_ref` | BR-002 | Unique reservation reference |
| `customer_order_id` | NOT NULL | `nn_inventory_reservations_order` | BR-002 | Reservation serves order |
| `customer_order_id` | FOREIGN KEY | `fk_inventory_reservations_order` → `fulfillment.customer_orders` | BR-002 | Valid order |
| `order_line_id` | NOT NULL | `nn_inventory_reservations_line` | BR-002 | Line-level reservation |
| `order_line_id` | FOREIGN KEY | `fk_inventory_reservations_line` → `fulfillment.customer_order_lines` | BR-002 | Valid order line |
| `product_id` | NOT NULL | `nn_inventory_reservations_product` | BR-002 | Reserved SKU |
| `product_id` | FOREIGN KEY | `fk_inventory_reservations_product` → `catalog.products` | BR-027 | Valid product |
| `location_id` | NOT NULL | `nn_inventory_reservations_location` | BR-002 | Reservation location |
| `location_id` | FOREIGN KEY | `fk_inventory_reservations_location` → `network.inventory_locations` | BR-002 | Valid location |
| `stock_position_id` | NOT NULL | `nn_inventory_reservations_position` | BR-002 | Target balance |
| `stock_position_id` | FOREIGN KEY | `fk_inventory_reservations_position` → `inventory.stock_positions` | BR-002 | Valid stock position |
| `reserved_qty` | NOT NULL | `nn_inventory_reservations_qty` | BR-002 | Reserved quantity required |
| `reserved_qty` | CHECK | `chk_inventory_reservations_qty` > 0 | BR-002 | Positive reservation |
| `reservation_status` | NOT NULL | `nn_inventory_reservations_status` | BR-002 | Lifecycle state |
| `reservation_status` | DEFAULT | `def_inventory_reservations_status` = 'ACTIVE' | BR-002 | Active on creation |
| `reservation_status` | CHECK | `chk_inventory_reservations_status` IN (ACTIVE, RELEASED, FULFILLED) | BR-002 | Valid states |
| `reserved_at` | NOT NULL | `nn_inventory_reservations_at` | BR-002 | Reservation timestamp |
| `reserved_at` | DEFAULT | `def_inventory_reservations_at` = NOW() | BR-002 | Auto-stamp at confirmation |

### `fulfillment.fulfillment_executions`

| Column | Type | Constraint | Business Rule | Justification |
|--------|------|------------|---------------|---------------|
| `fulfillment_reference` | NOT NULL | `nn_fulfillment_executions_ref` | BR-003 | Pick work document |
| `fulfillment_reference` | UNIQUE | `uk_fulfillment_executions_ref` | BR-003 | Unique fulfillment reference |
| `customer_order_id` | NOT NULL | `nn_fulfillment_executions_order` | BR-003 | Execution serves order |
| `customer_order_id` | FOREIGN KEY | `fk_fulfillment_executions_order` → `fulfillment.customer_orders` | BR-003 | Valid order |
| `fulfillment_location_id` | NOT NULL | `nn_fulfillment_executions_location` | BR-003, BR-024 | Pick site required |
| `fulfillment_location_id` | FOREIGN KEY | `fk_fulfillment_executions_location` → `network.inventory_locations` | BR-024 | Valid non-frozen location |
| `pick_verification_status` | NOT NULL | `nn_fulfillment_executions_pick_status` | BR-003 | Pick verification state |
| `pick_verification_status` | DEFAULT | `def_fulfillment_executions_pick_status` = 'PENDING' | BR-003 | Pending until verified |
| `pick_verification_status` | CHECK | `chk_fulfillment_executions_pick_status` IN (PENDING, VERIFIED, EXCEPTION) | BR-003 | Valid pick states |
| `pack_confirmed` | NOT NULL | `nn_fulfillment_executions_pack` | BR-003 | Pack flag explicit |
| `pack_confirmed` | DEFAULT | `def_fulfillment_executions_pack` = FALSE | BR-003 | Not packed by default |
| `has_exception` | NOT NULL | `nn_fulfillment_executions_exception` | BR-003 | Exception flag explicit |
| `has_exception` | DEFAULT | `def_fulfillment_executions_exception` = FALSE | — | No exception by default |
| `assigned_picker_id` | FOREIGN KEY | `fk_fulfillment_executions_picker` → `identity.user_accounts` | BO-19 | Picker attribution |

### `fulfillment.fulfillment_pick_lines`

| Column | Type | Constraint | Business Rule | Justification |
|--------|------|------------|---------------|---------------|
| `fulfillment_execution_id` | NOT NULL | `nn_fulfillment_pick_lines_fe` | BR-003 | Pick belongs to execution |
| `fulfillment_execution_id` | FOREIGN KEY | `fk_fulfillment_pick_lines_fe` → `fulfillment.fulfillment_executions` | BR-003 | Parent execution exists |
| `order_line_id` | NOT NULL | `nn_fulfillment_pick_lines_ol` | BR-003 | Fulfills order line |
| `order_line_id` | FOREIGN KEY | `fk_fulfillment_pick_lines_ol` → `fulfillment.customer_order_lines` | BR-003 | Valid order line |
| `product_id` | NOT NULL | `nn_fulfillment_pick_lines_product` | BR-003 | Picked product |
| `product_id` | FOREIGN KEY | `fk_fulfillment_pick_lines_product` → `catalog.products` | BR-003 | Valid product |
| `(fulfillment_execution_id, order_line_id)` | UNIQUE | `uk_fulfillment_pick_lines_fe_ol` | BR-003 | One pick per line per execution |
| `requested_qty` | NOT NULL | `nn_fulfillment_pick_lines_requested` | BR-003 | Pick quantity required |
| `requested_qty` | CHECK | `chk_fulfillment_pick_lines_requested` > 0 | BR-003 | Positive pick qty |
| `picked_qty` | NOT NULL | `nn_fulfillment_pick_lines_picked` | BR-003 | Actual picked tracked |
| `picked_qty` | DEFAULT | `def_fulfillment_pick_lines_picked` = 0 | BR-003 | Zero until picked |
| `picked_qty` | CHECK | `chk_fulfillment_pick_lines_picked` >= 0 | BR-003 | Non-negative picked |
| `picked_qty` | CHECK | `chk_fulfillment_pick_lines_picked_le_requested` picked_qty <= requested_qty | BR-003 | Cannot over-pick without exception |
| `storage_position_id` | FOREIGN KEY | `fk_fulfillment_pick_lines_position` → `network.storage_positions` | BR-014 | Source bin |
| `lot_batch_id` | FOREIGN KEY | `fk_fulfillment_pick_lines_lot` → `inventory.lot_batches` | BR-017 | Lot on pick when traceable |

### `fulfillment.backorders`

| Column | Type | Constraint | Business Rule | Justification |
|--------|------|------------|---------------|---------------|
| `backorder_reference` | NOT NULL | `nn_backorders_ref` | BR-028 | Backorder document identity |
| `backorder_reference` | UNIQUE | `uk_backorders_ref` | BR-028 | Unique backorder reference |
| `customer_order_id` | NOT NULL | `nn_backorders_order` | BR-028 | Backorder on order |
| `customer_order_id` | FOREIGN KEY | `fk_backorders_order` → `fulfillment.customer_orders` | BR-028 | Valid order |
| `order_line_id` | NOT NULL | `nn_backorders_line` | BR-028 | Line-level backorder |
| `order_line_id` | FOREIGN KEY | `fk_backorders_line` → `fulfillment.customer_order_lines` | BR-028 | Valid order line |
| `product_id` | NOT NULL | `nn_backorders_product` | BR-028 | Awaiting SKU |
| `product_id` | FOREIGN KEY | `fk_backorders_product` → `catalog.products` | BR-028 | Valid product |
| `backordered_qty` | NOT NULL | `nn_backorders_qty` | BR-028 | Backordered quantity |
| `backordered_qty` | CHECK | `chk_backorders_qty` > 0 | BR-028 | Positive backorder qty |
| `customer_acknowledged` | NOT NULL | `nn_backorders_acknowledged` | BR-028 | Acknowledgment flag required |
| `customer_acknowledged` | DEFAULT | `def_backorders_acknowledged` = FALSE | BR-028 | Not acknowledged by default |
| `(customer_acknowledged, acknowledged_at)` | CHECK | `chk_backorders_ack_timestamp` | BR-028 | Acknowledged requires timestamp |
| `resolution_status` | NOT NULL | `nn_backorders_resolution` | BR-028 | Resolution tracking |
| `resolution_status` | DEFAULT | `def_backorders_resolution` = 'OPEN' | BR-028 | Open until resolved |
| `resolution_status` | CHECK | `chk_backorders_resolution` IN (OPEN, FULFILLED, CANCELLED) | BR-028 | Valid resolution states |

### `fulfillment.shipments`

| Column | Type | Constraint | Business Rule | Justification |
|--------|------|------------|---------------|---------------|
| `shipment_number` | NOT NULL | `nn_shipments_number` | BR-003 | Shipment document identity |
| `shipment_number` | UNIQUE | `uk_shipments_number` | BR-003 | Unique shipment reference |
| `customer_order_id` | NOT NULL | `nn_shipments_order` | BR-003 | Shipment fulfills order |
| `customer_order_id` | FOREIGN KEY | `fk_shipments_order` → `fulfillment.customer_orders` | BR-003 | Valid order |
| `fulfillment_execution_id` | NOT NULL | `nn_shipments_fe` | BR-003 | Verified pick required |
| `fulfillment_execution_id` | FOREIGN KEY | `fk_shipments_fe` → `fulfillment.fulfillment_executions` | BR-003 | Valid verified execution |
| `ship_from_location_id` | NOT NULL | `nn_shipments_location` | BR-003 | Ship-from site |
| `ship_from_location_id` | FOREIGN KEY | `fk_shipments_location` → `network.inventory_locations` | BR-003 | Valid location |
| `ship_date` | NOT NULL | `nn_shipments_date` | BR-003 | Dispatch timestamp |
| `ship_date` | DEFAULT | `def_shipments_date` = NOW() | BR-003 | Auto-stamp dispatch |
| `shipment_status` | NOT NULL | `nn_shipments_status` | BR-003 | Shipment lifecycle |
| `shipment_status` | DEFAULT | `def_shipments_status` = 'DISPATCHED' | BR-003 | Dispatched on creation |
| `shipment_status` | CHECK | `chk_shipments_status` IN (DISPATCHED, IN_TRANSIT, DELIVERED) | BR-003 | Valid shipment states |

### `fulfillment.shipment_lines`

| Column | Type | Constraint | Business Rule | Justification |
|--------|------|------------|---------------|---------------|
| `shipment_id` | NOT NULL | `nn_shipment_lines_shipment` | BR-003 | Line belongs to shipment |
| `shipment_id` | FOREIGN KEY | `fk_shipment_lines_shipment` → `fulfillment.shipments` | BR-003 | Parent shipment exists |
| `order_line_id` | NOT NULL | `nn_shipment_lines_ol` | BR-003 | Shipped order line |
| `order_line_id` | FOREIGN KEY | `fk_shipment_lines_ol` → `fulfillment.customer_order_lines` | BR-003 | Valid order line |
| `(shipment_id, order_line_id)` | UNIQUE | `uk_shipment_lines_shipment_ol` | BR-003 | One line per shipment |
| `product_id` | NOT NULL | `nn_shipment_lines_product` | BR-003 | Shipped product |
| `product_id` | FOREIGN KEY | `fk_shipment_lines_product` → `catalog.products` | BR-003 | Valid product |
| `shipped_qty` | NOT NULL | `nn_shipment_lines_qty` | BR-003 | Shipped quantity |
| `shipped_qty` | CHECK | `chk_shipment_lines_qty` > 0 | BR-003 | Positive shipped qty |
| `lot_batch_id` | FOREIGN KEY | `fk_shipment_lines_lot` → `inventory.lot_batches` | BR-017 | Lot traceability on dispatch |
| `reservation_id` | FOREIGN KEY | `fk_shipment_lines_reservation` → `fulfillment.inventory_reservations` | BR-002 | Consumes reservation |

---

## Domain 9: Network Transfer

### `transfer.transfer_requests`

| Column | Type | Constraint | Business Rule | Justification |
|--------|------|------------|---------------|---------------|
| `request_number` | NOT NULL | `nn_transfer_requests_number` | BR-011 | Transfer request identity |
| `request_number` | UNIQUE | `uk_transfer_requests_number` | — | Unique request reference |
| `source_location_id` | NOT NULL | `nn_transfer_requests_source` | BR-012 | Source site required |
| `source_location_id` | FOREIGN KEY | `fk_transfer_requests_source` → `network.inventory_locations` | BR-012 | Valid source |
| `destination_location_id` | NOT NULL | `nn_transfer_requests_dest` | BR-011 | Destination required |
| `destination_location_id` | FOREIGN KEY | `fk_transfer_requests_dest` → `network.inventory_locations` | BR-011 | Valid destination |
| `(source_location_id, destination_location_id)` | CHECK | `chk_transfer_requests_distinct_locations` source ≠ destination | BR-011 | Source and destination must differ |
| `request_status` | NOT NULL | `nn_transfer_requests_status` | BR-012 | Approval workflow state |
| `request_status` | DEFAULT | `def_transfer_requests_status` = 'SUBMITTED' | — | Submitted on creation |
| `request_status` | CHECK | `chk_transfer_requests_status` IN (SUBMITTED, APPROVED, REJECTED, CONVERTED) | BR-012 | Valid states |
| `requested_by` | NOT NULL | `nn_transfer_requests_requester` | BO-19 | Requestor required |
| `requested_by` | FOREIGN KEY | `fk_transfer_requests_requester` → `identity.user_accounts` | BO-19 | Requestor attribution |
| `approved_by` | FOREIGN KEY | `fk_transfer_requests_approver` → `identity.user_accounts` | BR-012 | Approver attribution |
| `stock_transfer_id` | FOREIGN KEY | `fk_transfer_requests_transfer` → `transfer.stock_transfers` | BR-012 | Execution link |

### `transfer.transfer_request_lines`

| Column | Type | Constraint | Business Rule | Justification |
|--------|------|------------|---------------|---------------|
| `transfer_request_id` | NOT NULL | `nn_transfer_request_lines_req` | BR-012 | Line belongs to request |
| `transfer_request_id` | FOREIGN KEY | `fk_transfer_request_lines_req` → `transfer.transfer_requests` | BR-012 | Parent request exists |
| `(transfer_request_id, line_number)` | UNIQUE | `uk_transfer_request_lines_req_line` | — | Unique line per request |
| `product_id` | NOT NULL | `nn_transfer_request_lines_product` | BR-017 | Product to transfer |
| `product_id` | FOREIGN KEY | `fk_transfer_request_lines_product` → `catalog.products` | BR-017 | Valid product |
| `requested_qty` | NOT NULL | `nn_transfer_request_lines_qty` | BR-012 | Requested quantity |
| `requested_qty` | CHECK | `chk_transfer_request_lines_qty` > 0 | BR-012 | Positive transfer qty |

### `transfer.stock_transfers`

| Column | Type | Constraint | Business Rule | Justification |
|--------|------|------------|---------------|---------------|
| `transfer_number` | NOT NULL | `nn_stock_transfers_number` | BR-012 | Transfer document identity |
| `transfer_number` | UNIQUE | `uk_stock_transfers_number` | — | Unique transfer reference |
| `transfer_request_id` | FOREIGN KEY | `fk_stock_transfers_request` → `transfer.transfer_requests` | BR-012 | Optional request origin |
| `source_location_id` | NOT NULL | `nn_stock_transfers_source` | BR-012 | Source site |
| `source_location_id` | FOREIGN KEY | `fk_stock_transfers_source` → `network.inventory_locations` | BR-012 | Valid source |
| `destination_location_id` | NOT NULL | `nn_stock_transfers_dest` | BR-012 | Destination site |
| `destination_location_id` | FOREIGN KEY | `fk_stock_transfers_dest` → `network.inventory_locations` | BR-012 | Valid destination |
| `(source_location_id, destination_location_id)` | CHECK | `chk_stock_transfers_distinct_locations` | BR-011 | Distinct endpoints |
| `transfer_status` | NOT NULL | `nn_stock_transfers_status` | BR-012 | Transfer lifecycle |
| `transfer_status` | DEFAULT | `def_stock_transfers_status` = 'APPROVED' | — | Approved when created |
| `transfer_status` | CHECK | `chk_stock_transfers_status` IN (REQUESTED, APPROVED, IN_TRANSIT, RECEIVED, CANCELLED) | BR-012 | Valid states |
| `(transfer_status, dispatch_date)` | CHECK | `chk_stock_transfers_dispatch` | BR-012 | IN_TRANSIT/RECEIVED requires dispatch_date |
| `(transfer_status, receipt_date)` | CHECK | `chk_stock_transfers_receipt` | BR-012 | RECEIVED requires receipt_date |

### `transfer.stock_transfer_lines`

| Column | Type | Constraint | Business Rule | Justification |
|--------|------|------------|---------------|---------------|
| `stock_transfer_id` | NOT NULL | `nn_stock_transfer_lines_transfer` | BR-012 | Line belongs to transfer |
| `stock_transfer_id` | FOREIGN KEY | `fk_stock_transfer_lines_transfer` → `transfer.stock_transfers` | BR-012 | Parent transfer exists |
| `(stock_transfer_id, line_number)` | UNIQUE | `uk_stock_transfer_lines_transfer_line` | — | Unique line per transfer |
| `product_id` | NOT NULL | `nn_stock_transfer_lines_product` | BR-017 | Transferred product |
| `product_id` | FOREIGN KEY | `fk_stock_transfer_lines_product` → `catalog.products` | BR-017 | Valid product |
| `quantity` | NOT NULL | `nn_stock_transfer_lines_qty` | BR-012 | Transfer quantity |
| `quantity` | CHECK | `chk_stock_transfer_lines_qty` > 0 | BR-012 | Positive transfer qty |
| `dispatched_qty` | NOT NULL | `nn_stock_transfer_lines_dispatched` | BR-012 | Dispatched tracked |
| `dispatched_qty` | DEFAULT | `def_stock_transfer_lines_dispatched` = 0 | — | Zero until dispatch |
| `dispatched_qty` | CHECK | `chk_stock_transfer_lines_dispatched` >= 0 | BR-012 | Non-negative |
| `received_qty` | NOT NULL | `nn_stock_transfer_lines_received` | BR-012 | Received tracked |
| `received_qty` | DEFAULT | `def_stock_transfer_lines_received` = 0 | — | Zero until receipt |
| `received_qty` | CHECK | `chk_stock_transfer_lines_received` >= 0 | BR-012 | Non-negative |
| `received_qty` | CHECK | `chk_stock_transfer_lines_received_le_dispatched` received_qty <= dispatched_qty | BR-012 | Cannot receive more than dispatched |
| `lot_batch_id` | FOREIGN KEY | `fk_stock_transfer_lines_lot` → `inventory.lot_batches` | BR-017 | Lot on transfer |

### `transfer.in_transit_stock`

| Column | Type | Constraint | Business Rule | Justification |
|--------|------|------------|---------------|---------------|
| `in_transit_reference` | NOT NULL | `nn_in_transit_stock_ref` | BR-012 | Pipeline stock identity |
| `in_transit_reference` | UNIQUE | `uk_in_transit_stock_ref` | — | Unique in-transit reference |
| `stock_transfer_id` | NOT NULL | `nn_in_transit_stock_transfer` | BR-012 | Belongs to transfer |
| `stock_transfer_id` | FOREIGN KEY | `fk_in_transit_stock_transfer` → `transfer.stock_transfers` | BR-012 | Parent transfer exists |
| `stock_transfer_line_id` | NOT NULL | `nn_in_transit_stock_line` | BR-012 | Line-level tracking |
| `stock_transfer_line_id` | FOREIGN KEY | `fk_in_transit_stock_line` → `transfer.stock_transfer_lines` | BR-012 | Valid transfer line |
| `product_id` | NOT NULL | `nn_in_transit_stock_product` | — | Product in pipeline |
| `product_id` | FOREIGN KEY | `fk_in_transit_stock_product` → `catalog.products` | — | Valid product |
| `quantity` | NOT NULL | `nn_in_transit_stock_qty` | BR-012 | In-transit quantity |
| `quantity` | CHECK | `chk_in_transit_stock_qty` > 0 | BR-012 | Positive pipeline qty |
| `source_location_id` | NOT NULL | `nn_in_transit_stock_source` | BR-012 | Origin site |
| `source_location_id` | FOREIGN KEY | `fk_in_transit_stock_source` → `network.inventory_locations` | BR-012 | Valid source |
| `destination_location_id` | NOT NULL | `nn_in_transit_stock_dest` | BR-012 | Destination site |
| `destination_location_id` | FOREIGN KEY | `fk_in_transit_stock_dest` → `network.inventory_locations` | BR-012 | Valid destination |
| `dispatch_date` | NOT NULL | `nn_in_transit_stock_dispatch` | BR-012 | Dispatch time required |
| `in_transit_status` | NOT NULL | `nn_in_transit_stock_status` | BR-012 | Pipeline state |
| `in_transit_status` | DEFAULT | `def_in_transit_stock_status` = 'IN_TRANSIT' | BR-012 | In-transit by default |
| `in_transit_status` | CHECK | `chk_in_transit_stock_status` IN (IN_TRANSIT, RECEIVED, LOST, DELAYED) | BR-012 | Valid pipeline states |

---

## Domain 10: Inventory Accuracy

### `accuracy.cycle_counts`

| Column | Type | Constraint | Business Rule | Justification |
|--------|------|------------|---------------|---------------|
| `count_assignment_number` | NOT NULL | `nn_cycle_counts_number` | BR-018 | Count assignment identity |
| `count_assignment_number` | UNIQUE | `uk_cycle_counts_number` | BR-018 | Unique count reference |
| `schedule_date` | NOT NULL | `nn_cycle_counts_schedule` | BR-018, BR-032 | Scheduled date required |
| `location_id` | NOT NULL | `nn_cycle_counts_location` | BR-018 | Count site required |
| `location_id` | FOREIGN KEY | `fk_cycle_counts_location` → `network.inventory_locations` | BR-018 | Valid location |
| `product_id` | NOT NULL | `nn_cycle_counts_product` | BR-018 | Counted SKU required |
| `product_id` | FOREIGN KEY | `fk_cycle_counts_product` → `catalog.products` | BR-032 | Valid product |
| `storage_position_id` | FOREIGN KEY | `fk_cycle_counts_position` → `network.storage_positions` | — | Optional bin scope |
| `counter_id` | NOT NULL | `nn_cycle_counts_counter` | BR-018, BR-019 | Counter required |
| `counter_id` | FOREIGN KEY | `fk_cycle_counts_counter` → `identity.user_accounts` | BR-019 | Counter attribution |
| `count_status` | NOT NULL | `nn_cycle_counts_status` | BR-018 | Count workflow state |
| `count_status` | DEFAULT | `def_cycle_counts_status` = 'SCHEDULED' | BR-018 | Scheduled by default |
| `count_status` | CHECK | `chk_cycle_counts_status` IN (SCHEDULED, IN_PROGRESS, COMPLETED) | BR-018 | Valid count states |
| `physical_count_qty` | CHECK | `chk_cycle_counts_physical` >= 0 OR NULL | BR-018 | Physical qty non-negative when recorded |
| `(count_status, physical_count_qty)` | CHECK | `chk_cycle_counts_completed` | BR-018 | COMPLETED requires physical_count_qty |

### `accuracy.physical_inventory_counts`

| Column | Type | Constraint | Business Rule | Justification |
|--------|------|------------|---------------|---------------|
| `count_event_number` | NOT NULL | `nn_physical_inventory_counts_number` | BR-024 | Count event identity |
| `count_event_number` | UNIQUE | `uk_physical_inventory_counts_number` | BR-024 | Unique event reference |
| `location_id` | NOT NULL | `nn_physical_inventory_counts_location` | BR-024 | Wall-to-wall site |
| `location_id` | FOREIGN KEY | `fk_physical_inventory_counts_location` → `network.inventory_locations` | BR-024 | Valid location |
| `count_start_date` | NOT NULL | `nn_physical_inventory_counts_start` | BR-024 | Count start required |
| `freeze_status` | NOT NULL | `nn_physical_inventory_counts_freeze` | BR-024 | Freeze state tracked |
| `freeze_status` | DEFAULT | `def_physical_inventory_counts_freeze` = 'ACTIVE' | BR-024 | Active freeze on start |
| `freeze_status` | CHECK | `chk_physical_inventory_counts_freeze` IN (ACTIVE, RELEASED) | BR-024 | Valid freeze states |
| `total_variances` | NOT NULL | `nn_physical_inventory_counts_variances` | BR-024 | Variance count tracked |
| `total_variances` | DEFAULT | `def_physical_inventory_counts_variances` = 0 | — | Zero at start |
| `total_variances` | CHECK | `chk_physical_inventory_counts_variances` >= 0 | — | Non-negative count |
| `certification_status` | NOT NULL | `nn_physical_inventory_counts_cert` | BR-024 | Certification tracking |
| `certification_status` | DEFAULT | `def_physical_inventory_counts_cert` = 'IN_PROGRESS' | BR-024 | In progress on start |
| `certification_status` | CHECK | `chk_physical_inventory_counts_cert` IN (IN_PROGRESS, CERTIFIED) | BR-024 | Valid certification states |
| `(freeze_status, certification_status)` | CHECK | `chk_physical_inventory_counts_freeze_release` | BR-024 | CERTIFIED requires freeze RELEASED |

### `accuracy.count_variances`

| Column | Type | Constraint | Business Rule | Justification |
|--------|------|------------|---------------|---------------|
| `variance_reference` | NOT NULL | `nn_count_variances_ref` | BR-022 | Variance document identity |
| `variance_reference` | UNIQUE | `uk_count_variances_ref` | BR-022 | Unique variance reference |
| `cycle_count_id` | FOREIGN KEY | `fk_count_variances_cycle` → `accuracy.cycle_counts` | BR-022 | Cycle count origin |
| `physical_count_id` | FOREIGN KEY | `fk_count_variances_physical` → `accuracy.physical_inventory_counts` | BR-022 | Physical count origin |
| `(cycle_count_id, physical_count_id)` | CHECK | `chk_count_variances_single_origin` | BR-022 | Exactly one count origin — XOR not both null, not both set |
| `stock_position_id` | NOT NULL | `nn_count_variances_position` | BR-022 | Affected balance |
| `stock_position_id` | FOREIGN KEY | `fk_count_variances_position` → `inventory.stock_positions` | BR-022 | Valid stock position |
| `product_id` | NOT NULL | `nn_count_variances_product` | — | Denormalized product |
| `product_id` | FOREIGN KEY | `fk_count_variances_product` → `catalog.products` | — | Valid product |
| `location_id` | NOT NULL | `nn_count_variances_location` | — | Denormalized location |
| `location_id` | FOREIGN KEY | `fk_count_variances_location` → `network.inventory_locations` | — | Valid location |
| `system_qty` | NOT NULL | `nn_count_variances_system` | BR-018 | System quantity at count |
| `system_qty` | CHECK | `chk_count_variances_system` >= 0 | LDM-01 | Non-negative system qty |
| `physical_qty` | NOT NULL | `nn_count_variances_physical` | BR-018 | Physical quantity recorded |
| `physical_qty` | CHECK | `chk_count_variances_physical` >= 0 | BR-018 | Non-negative physical qty |
| `variance_qty` | NOT NULL | `nn_count_variances_variance` | BR-022 | Variance quantity |
| `investigation_status` | NOT NULL | `nn_count_variances_investigation` | BR-022 | Investigation required |
| `investigation_status` | DEFAULT | `def_count_variances_investigation` = 'OPEN' | BR-022 | Open until investigated |
| `investigation_status` | CHECK | `chk_count_variances_investigation` IN (OPEN, INVESTIGATED) | BR-022 | Valid investigation states |
| `approval_status` | NOT NULL | `nn_count_variances_approval` | BR-019, BR-021 | Approval workflow |
| `approval_status` | DEFAULT | `def_count_variances_approval` = 'PENDING' | BR-019 | Pending approval |
| `approval_status` | CHECK | `chk_count_variances_approval` IN (PENDING, APPROVED, REJECTED) | BR-019 | Valid approval states |
| `approver_id` | FOREIGN KEY | `fk_count_variances_approver` → `identity.user_accounts` | BR-019 | Independent approver |
| `(approval_status, approver_id)` | CHECK | `chk_count_variances_approver_required` | BR-019 | APPROVED requires approver |

### `accuracy.stock_adjustments`

| Column | Type | Constraint | Business Rule | Justification |
|--------|------|------------|---------------|---------------|
| `adjustment_reference` | NOT NULL | `nn_stock_adjustments_ref` | BR-020 | Adjustment document identity |
| `adjustment_reference` | UNIQUE | `uk_stock_adjustments_ref` | BR-020 | Unique adjustment reference |
| `stock_position_id` | NOT NULL | `nn_stock_adjustments_position` | BR-020 | Target balance |
| `stock_position_id` | FOREIGN KEY | `fk_stock_adjustments_position` → `inventory.stock_positions` | BR-020 | Valid stock position |
| `product_id` | NOT NULL | `nn_stock_adjustments_product` | BR-020 | Denormalized product |
| `product_id` | FOREIGN KEY | `fk_stock_adjustments_product` → `catalog.products` | BR-020 | Valid product |
| `location_id` | NOT NULL | `nn_stock_adjustments_location` | BR-020 | Denormalized location |
| `location_id` | FOREIGN KEY | `fk_stock_adjustments_location` → `network.inventory_locations` | BR-020 | Valid location |
| `adjustment_qty` | NOT NULL | `nn_stock_adjustments_qty` | BR-020 | Signed adjustment required |
| `adjustment_qty` | CHECK | `chk_stock_adjustments_qty` <> 0 | BR-020 | Zero adjustment meaningless |
| `qty_before` | NOT NULL | `nn_stock_adjustments_before` | BR-020 | Before snapshot required |
| `qty_before` | CHECK | `chk_stock_adjustments_before` >= 0 | LDM-01 | Non-negative before |
| `qty_after` | NOT NULL | `nn_stock_adjustments_after` | BR-020 | After snapshot required |
| `qty_after` | CHECK | `chk_stock_adjustments_after` >= 0 | LDM-01 | Adjustment must not drive negative (LDM-10) |
| `(qty_before, qty_after, adjustment_qty)` | CHECK | `chk_stock_adjustments_balance` qty_after = qty_before + adjustment_qty | BR-020 | Quantity arithmetic integrity |
| `reason_code_id` | NOT NULL | `nn_stock_adjustments_reason` | BR-020 | Reason mandatory |
| `reason_code_id` | FOREIGN KEY | `fk_stock_adjustments_reason` → `governance.reason_codes` | BR-020 | Valid active reason code |
| `count_variance_id` | FOREIGN KEY | `fk_stock_adjustments_variance` → `accuracy.count_variances` | BR-022 | Count-to-correction link |
| `approval_status` | NOT NULL | `nn_stock_adjustments_approval` | BR-021 | Approval workflow |
| `approval_status` | DEFAULT | `def_stock_adjustments_approval` = 'PENDING' | BR-021 | Pending by default |
| `approval_status` | CHECK | `chk_stock_adjustments_approval` IN (PENDING, APPROVED, REJECTED) | BR-021 | Valid states |
| `initiated_by` | NOT NULL | `nn_stock_adjustments_initiator` | BR-021 | Initiator required |
| `initiated_by` | FOREIGN KEY | `fk_stock_adjustments_initiator` → `identity.user_accounts` | BR-021 | Initiator attribution |
| `approved_by` | FOREIGN KEY | `fk_stock_adjustments_approver` → `identity.user_accounts` | BR-021 | Approver attribution |
| `(initiated_by, approved_by)` | CHECK | `chk_stock_adjustments_sod` | BR-021 | Approver ≠ initiator when both set |
| `adjustment_date` | NOT NULL | `nn_stock_adjustments_date` | BR-020 | Effective date required |
| `adjustment_date` | DEFAULT | `def_stock_adjustments_date` = NOW() | BR-020 | Auto-stamp effective date |

### `accuracy.inventory_write_offs`

| Column | Type | Constraint | Business Rule | Justification |
|--------|------|------------|---------------|---------------|
| `write_off_reference` | NOT NULL | `nn_inventory_write_offs_ref` | BR-023 | Write-off document identity |
| `write_off_reference` | UNIQUE | `uk_inventory_write_offs_ref` | BR-023 | Unique write-off reference |
| `stock_position_id` | NOT NULL | `nn_inventory_write_offs_position` | BR-023 | Target balance |
| `stock_position_id` | FOREIGN KEY | `fk_inventory_write_offs_position` → `inventory.stock_positions` | BR-023 | Valid stock position |
| `product_id` | NOT NULL | `nn_inventory_write_offs_product` | BR-023 | Denormalized product |
| `product_id` | FOREIGN KEY | `fk_inventory_write_offs_product` → `catalog.products` | BR-023 | Valid product |
| `location_id` | NOT NULL | `nn_inventory_write_offs_location` | BR-023 | Denormalized location |
| `location_id` | FOREIGN KEY | `fk_inventory_write_offs_location` → `network.inventory_locations` | BR-023 | Valid location |
| `write_off_qty` | NOT NULL | `nn_inventory_write_offs_qty` | BR-023 | Write-off quantity |
| `write_off_qty` | CHECK | `chk_inventory_write_offs_qty` > 0 | BR-023 | Positive removal quantity |
| `reason_code_id` | NOT NULL | `nn_inventory_write_offs_reason` | BR-020, BR-023 | Reason mandatory |
| `reason_code_id` | FOREIGN KEY | `fk_inventory_write_offs_reason` → `governance.reason_codes` | BR-020 | Valid reason code |
| `return_disposition_id` | FOREIGN KEY | `fk_inventory_write_offs_disposition` → `returns.return_dispositions` | BR-026 | Return-originated write-off |
| `initiated_by` | NOT NULL | `nn_inventory_write_offs_initiator` | BR-023 | Initiator required |
| `initiated_by` | FOREIGN KEY | `fk_inventory_write_offs_initiator` → `identity.user_accounts` | BR-023 | Initiator attribution |
| `authorized_by` | NOT NULL | `nn_inventory_write_offs_authorizer` | BR-023 | Authorization required |
| `authorized_by` | FOREIGN KEY | `fk_inventory_write_offs_authorizer` → `identity.user_accounts` | BR-023 | Authorizer attribution |
| `(initiated_by, authorized_by)` | CHECK | `chk_inventory_write_offs_sod` | BR-023 | Authorizer ≠ initiator |
| `write_off_date` | NOT NULL | `nn_inventory_write_offs_date` | BR-023 | Effective date |
| `write_off_date` | DEFAULT | `def_inventory_write_offs_date` = NOW() | BR-023 | Auto-stamp effective date |
| `disposition_method` | CHECK | `chk_inventory_write_offs_disposition` IN (DESTROY, DONATE, SCRAP) OR NULL | BR-023 | Valid disposition methods |

---

## Domain 11: Returns

### `returns.return_authorizations`

| Column | Type | Constraint | Business Rule | Justification |
|--------|------|------------|---------------|---------------|
| `rma_number` | NOT NULL | `nn_return_authorizations_rma` | BR-025 | RMA document identity |
| `rma_number` | UNIQUE | `uk_return_authorizations_rma` | BR-025 | Unique RMA reference |
| `customer_order_id` | NOT NULL | `nn_return_authorizations_order` | BR-025 | Original order required |
| `customer_order_id` | FOREIGN KEY | `fk_return_authorizations_order` → `fulfillment.customer_orders` | BR-025 | Valid original order |
| `authorization_date` | NOT NULL | `nn_return_authorizations_date` | BR-025 | Issue date required |
| `authorization_date` | DEFAULT | `def_return_authorizations_date` = NOW() | BR-025 | Auto-stamp issue |
| `(authorization_date, expiration_date)` | CHECK | `chk_return_authorizations_expiry` expiration IS NULL OR expiration >= authorization_date::date | BR-025 | Valid expiry window |
| `authorization_status` | NOT NULL | `nn_return_authorizations_status` | BR-025 | RMA lifecycle |
| `authorization_status` | DEFAULT | `def_return_authorizations_status` = 'ACTIVE' | BR-025 | Active on issue |
| `authorization_status` | CHECK | `chk_return_authorizations_status` IN (ACTIVE, EXPIRED, USED, CANCELLED) | BR-025 | Valid RMA states |

### `returns.return_authorization_lines`

| Column | Type | Constraint | Business Rule | Justification |
|--------|------|------------|---------------|---------------|
| `return_authorization_id` | NOT NULL | `nn_return_authorization_lines_rma` | BR-025 | Line belongs to RMA |
| `return_authorization_id` | FOREIGN KEY | `fk_return_authorization_lines_rma` → `returns.return_authorizations` | BR-025 | Parent RMA exists |
| `(return_authorization_id, line_number)` | UNIQUE | `uk_return_authorization_lines_rma_line` | BR-025 | Unique line per RMA |
| `product_id` | NOT NULL | `nn_return_authorization_lines_product` | BR-025 | Authorized product |
| `product_id` | FOREIGN KEY | `fk_return_authorization_lines_product` → `catalog.products` | BR-025 | Valid product |
| `authorized_qty` | NOT NULL | `nn_return_authorization_lines_qty` | BR-025 | Authorized quantity |
| `authorized_qty` | CHECK | `chk_return_authorization_lines_qty` > 0 | BR-025 | Positive authorized qty |

### `returns.customer_returns`

| Column | Type | Constraint | Business Rule | Justification |
|--------|------|------------|---------------|---------------|
| `return_number` | NOT NULL | `nn_customer_returns_number` | BR-025 | Return receipt identity |
| `return_number` | UNIQUE | `uk_customer_returns_number` | BR-025 | Unique return reference |
| `return_authorization_id` | NOT NULL | `nn_customer_returns_rma` | BR-025 | Valid RMA required |
| `return_authorization_id` | FOREIGN KEY | `fk_customer_returns_rma` → `returns.return_authorizations` | BR-025 | RMA must exist and be active |
| `customer_order_id` | NOT NULL | `nn_customer_returns_order` | BR-025 | Original order link |
| `customer_order_id` | FOREIGN KEY | `fk_customer_returns_order` → `fulfillment.customer_orders` | BR-025 | Valid order |
| `receiving_location_id` | NOT NULL | `nn_customer_returns_location` | BR-004 | Receipt site |
| `receiving_location_id` | FOREIGN KEY | `fk_customer_returns_location` → `network.inventory_locations` | BR-004 | Valid location |
| `receipt_date` | NOT NULL | `nn_customer_returns_date` | BR-004 | Receipt timestamp |
| `receipt_date` | DEFAULT | `def_customer_returns_date` = NOW() | BR-004 | Auto-stamp receipt |
| `inspection_status` | NOT NULL | `nn_customer_returns_inspection` | BR-026 | Inspection workflow |
| `inspection_status` | DEFAULT | `def_customer_returns_inspection` = 'PENDING' | BR-026 | Pending inspection |
| `inspection_status` | CHECK | `chk_customer_returns_inspection` IN (PENDING, INSPECTED) | BR-026 | Valid inspection states |
| `receiving_clerk_id` | NOT NULL | `nn_customer_returns_clerk` | BO-19 | Clerk attribution |
| `receiving_clerk_id` | FOREIGN KEY | `fk_customer_returns_clerk` → `identity.user_accounts` | BO-19 | Clerk identity |

### `returns.customer_return_lines`

| Column | Type | Constraint | Business Rule | Justification |
|--------|------|------------|---------------|---------------|
| `customer_return_id` | NOT NULL | `nn_customer_return_lines_return` | BR-004 | Line belongs to return |
| `customer_return_id` | FOREIGN KEY | `fk_customer_return_lines_return` → `returns.customer_returns` | BR-004 | Parent return exists |
| `(customer_return_id, line_number)` | UNIQUE | `uk_customer_return_lines_return_line` | — | Unique line per return |
| `product_id` | NOT NULL | `nn_customer_return_lines_product` | BR-004 | Returned product |
| `product_id` | FOREIGN KEY | `fk_customer_return_lines_product` → `catalog.products` | BR-004 | Valid product |
| `returned_qty` | NOT NULL | `nn_customer_return_lines_qty` | BR-004 | Returned quantity |
| `returned_qty` | CHECK | `chk_customer_return_lines_qty` > 0 | BR-004 | Positive returned qty |
| `condition_at_receipt` | NOT NULL | `nn_customer_return_lines_condition` | BR-004 | Condition at receipt |
| `condition_at_receipt` | CHECK | `chk_customer_return_lines_condition` IN (GOOD, DAMAGED, DEFECTIVE, OPENED) | BR-004 | Valid condition codes |

### `returns.return_dispositions`

| Column | Type | Constraint | Business Rule | Justification |
|--------|------|------------|---------------|---------------|
| `disposition_reference` | NOT NULL | `nn_return_dispositions_ref` | BR-026 | Disposition document |
| `disposition_reference` | UNIQUE | `uk_return_dispositions_ref` | BR-026 | Unique disposition reference |
| `customer_return_id` | NOT NULL | `nn_return_dispositions_return` | BR-026 | Parent return |
| `customer_return_id` | FOREIGN KEY | `fk_return_dispositions_return` → `returns.customer_returns` | BR-026 | Valid return |
| `return_line_id` | NOT NULL | `nn_return_dispositions_line` | BR-026 | Return line |
| `return_line_id` | FOREIGN KEY | `fk_return_dispositions_line` → `returns.customer_return_lines` | BR-026 | Valid return line |
| `product_id` | NOT NULL | `nn_return_dispositions_product` | BR-026 | Dispositioned product |
| `product_id` | FOREIGN KEY | `fk_return_dispositions_product` → `catalog.products` | BR-026 | Valid product |
| `quantity` | NOT NULL | `nn_return_dispositions_qty` | BR-026 | Disposition quantity |
| `quantity` | CHECK | `chk_return_dispositions_qty` > 0 | BR-026 | Positive quantity |
| `condition_grade` | NOT NULL | `nn_return_dispositions_grade` | BR-026 | Quality grade required |
| `disposition_decision` | NOT NULL | `nn_return_dispositions_decision` | BR-026 | Outcome required |
| `disposition_decision` | CHECK | `chk_return_dispositions_decision` | BR-026 | RESTOCK, QUARANTINE, WRITE_OFF |
| `restock_location_id` | FOREIGN KEY | `fk_return_dispositions_location` → `network.inventory_locations` | BR-026 | Restock target when RESTOCK |
| `quarantine_hold_id` | FOREIGN KEY | `fk_return_dispositions_hold` → `inventory.quarantine_holds` | BR-013 | Quarantine path |
| `write_off_id` | FOREIGN KEY | `fk_return_dispositions_writeoff` → `accuracy.inventory_write_offs` | BR-023 | Write-off path |
| `inspector_id` | NOT NULL | `nn_return_dispositions_inspector` | BR-026 | Inspector required |
| `inspector_id` | FOREIGN KEY | `fk_return_dispositions_inspector` → `identity.user_accounts` | BR-026 | Inspector attribution |
| `inspection_date` | NOT NULL | `nn_return_dispositions_date` | BR-026 | Inspection timestamp |
| `inspection_date` | DEFAULT | `def_return_dispositions_date` = NOW() | BR-026 | Auto-stamp inspection |
| `(disposition_decision, restock_location_id)` | CHECK | `chk_return_dispositions_restock` | BR-026 | RESTOCK requires restock_location_id |
| `(disposition_decision, quarantine_hold_id)` | CHECK | `chk_return_dispositions_quarantine` | BR-013 | QUARANTINE requires hold reference |
| `(disposition_decision, write_off_id)` | CHECK | `chk_return_dispositions_writeoff` | BR-023 | WRITE_OFF requires write_off_id |

---

## Domain 12: Commercial

### `commercial.promotional_stock_allocations`

| Column | Type | Constraint | Business Rule | Justification |
|--------|------|------------|---------------|---------------|
| `allocation_reference` | NOT NULL | `nn_promotional_allocations_ref` | BR-029 | Allocation document identity |
| `allocation_reference` | UNIQUE | `uk_promotional_allocations_ref` | BR-029 | Unique allocation reference |
| `product_id` | NOT NULL | `nn_promotional_allocations_product` | BR-029 | Ring-fenced SKU |
| `product_id` | FOREIGN KEY | `fk_promotional_allocations_product` → `catalog.products` | BR-029 | Valid product |
| `allocated_qty` | NOT NULL | `nn_promotional_allocations_qty` | BR-029 | Ring-fenced quantity |
| `allocated_qty` | CHECK | `chk_promotional_allocations_qty` > 0 | BR-029 | Positive allocation |
| `campaign_name` | NOT NULL | `nn_promotional_allocations_campaign` | BR-029 | Campaign identity required |
| `effective_start_date` | NOT NULL | `nn_promotional_allocations_start` | BR-029 | Campaign start |
| `effective_end_date` | NOT NULL | `nn_promotional_allocations_end` | BR-029 | Campaign end |
| `(effective_start_date, effective_end_date)` | CHECK | `chk_promotional_allocations_dates` end_date >= start_date | BR-029 | Valid campaign window |
| `readiness_status` | NOT NULL | `nn_promotional_allocations_readiness` | BR-029 | Readiness tracking |
| `readiness_status` | DEFAULT | `def_promotional_allocations_readiness` = 'PLANNED' | BR-029 | Planned until confirmed |
| `readiness_status` | CHECK | `chk_promotional_allocations_readiness` IN (PLANNED, READY, ACTIVE, CLOSED) | BR-029 | Valid readiness states |

### `commercial.promotional_allocation_locations`

| Column | Type | Constraint | Business Rule | Justification |
|--------|------|------------|---------------|---------------|
| `allocation_id` | NOT NULL | `nn_promo_alloc_locations_allocation` | BR-029 | Belongs to allocation |
| `allocation_id` | FOREIGN KEY | `fk_promo_alloc_locations_allocation` → `commercial.promotional_stock_allocations` | BR-029 | Parent allocation exists |
| `location_id` | NOT NULL | `nn_promo_alloc_locations_location` | BR-029 | Supplying location |
| `location_id` | FOREIGN KEY | `fk_promo_alloc_locations_location` → `network.inventory_locations` | BR-029 | Valid location |
| `stock_position_id` | FOREIGN KEY | `fk_promo_alloc_locations_position` → `inventory.stock_positions` | BR-029 | Specific balance ring-fenced |
| `(allocation_id, location_id)` | UNIQUE | `uk_promo_alloc_locations_alloc_loc` | BR-029 | One entry per location per campaign |
| `allocated_qty_at_location` | NOT NULL | `nn_promo_alloc_locations_qty` | BR-029 | Location-level quantity |
| `allocated_qty_at_location` | CHECK | `chk_promo_alloc_locations_qty` > 0 | BR-029 | Positive location allocation |

---

## Domain 13: Identity & Access

### `identity.user_accounts`

| Column | Type | Constraint | Business Rule | Justification |
|--------|------|------------|---------------|---------------|
| `user_identifier` | NOT NULL | `nn_user_accounts_identifier` | BO-19 | Login identity required |
| `user_identifier` | UNIQUE | `uk_user_accounts_identifier` | BO-19 | Unique user identity |
| `display_name` | NOT NULL | `nn_user_accounts_name` | BO-19 | Display name for attribution |
| `email` | UNIQUE | `uk_user_accounts_email` | — | Unique email when provided |
| `account_status` | NOT NULL | `nn_user_accounts_status` | BR-019 | Account state required |
| `account_status` | DEFAULT | `def_user_accounts_status` = 'ACTIVE' | — | Active by default |
| `account_status` | CHECK | `chk_user_accounts_status` IN (ACTIVE, SUSPENDED, DEACTIVATED) | BR-019 | Valid account states |
| `effective_from` | NOT NULL | `nn_user_accounts_effective_from` | — | Account effective date |
| `has_sod_conflict` | NOT NULL | `nn_user_accounts_sod` | BR-019, BR-021 | SoD flag explicit |
| `has_sod_conflict` | DEFAULT | `def_user_accounts_sod` = FALSE | BR-019 | No conflict by default |

### `identity.role_assignments`

| Column | Type | Constraint | Business Rule | Justification |
|--------|------|------------|---------------|---------------|
| `user_account_id` | NOT NULL | `nn_role_assignments_user` | BR-019 | Assignment belongs to user |
| `user_account_id` | FOREIGN KEY | `fk_role_assignments_user` → `identity.user_accounts` | BR-019 | Valid user account |
| `role_name` | NOT NULL | `nn_role_assignments_role` | BR-019 | Role name required |
| `(user_account_id, role_name, effective_from)` | UNIQUE | `uk_role_assignments_user_role_from` | BR-019 | No duplicate role at same effective date |
| `assignment_status` | NOT NULL | `nn_role_assignments_status` | BR-019 | Assignment state |
| `assignment_status` | DEFAULT | `def_role_assignments_status` = 'ACTIVE' | — | Active by default |
| `assignment_status` | CHECK | `chk_role_assignments_status` IN (ACTIVE, INACTIVE) | BR-019 | Valid assignment states |
| `effective_from` | NOT NULL | `nn_role_assignments_from` | BR-019 | Effective start required |
| `(effective_from, effective_to)` | CHECK | `chk_role_assignments_dates` effective_to IS NULL OR effective_to >= effective_from | — | Valid assignment period |
| `sod_compliant` | NOT NULL | `nn_role_assignments_sod` | BR-019, BR-021 | SoD compliance flag |
| `sod_compliant` | DEFAULT | `def_role_assignments_sod` = TRUE | BR-019 | Compliant by default |

### `identity.role_assignment_locations`

| Column | Type | Constraint | Business Rule | Justification |
|--------|------|------------|---------------|---------------|
| `role_assignment_id` | NOT NULL | `nn_role_assignment_locations_assignment` | BR-019 | Scope belongs to assignment |
| `role_assignment_id` | FOREIGN KEY | `fk_role_assignment_locations_assignment` → `identity.role_assignments` | BR-019 | Valid assignment |
| `location_id` | NOT NULL | `nn_role_assignment_locations_location` | BR-019 | Scoped location |
| `location_id` | FOREIGN KEY | `fk_role_assignment_locations_location` → `network.inventory_locations` | BR-019 | Valid location |
| `(role_assignment_id, location_id)` | UNIQUE | `uk_role_assignment_locations` | BR-019 | One scope entry per location |

---

## Domain 14: Audit & Reporting

### `audit.inventory_movement_records`

| Column | Type | Constraint | Business Rule | Justification |
|--------|------|------------|---------------|---------------|
| `movement_reference` | NOT NULL | `nn_movement_records_ref` | BO-19, BR-017 | Movement document identity |
| `(movement_reference, movement_timestamp)` | UNIQUE | `uk_movement_records_ref_ts` | BO-19 | Idempotent event ingestion per partition |
| `movement_type` | NOT NULL | `nn_movement_records_type` | BR-017, BR-020 | Movement classification |
| `movement_type` | CHECK | `chk_movement_records_type` | — | Valid movement taxonomy |
| `stock_position_id` | NOT NULL | `nn_movement_records_position` | BO-19 | Affected balance |
| `stock_position_id` | FOREIGN KEY | `fk_movement_records_position` → `inventory.stock_positions` | BO-19 | Valid stock position |
| `product_id` | NOT NULL | `nn_movement_records_product` | BR-017 | Denormalized product |
| `product_id` | FOREIGN KEY | `fk_movement_records_product` → `catalog.products` | BR-017 | Valid product |
| `location_id` | NOT NULL | `nn_movement_records_location` | BO-19 | Denormalized location |
| `location_id` | FOREIGN KEY | `fk_movement_records_location` → `network.inventory_locations` | BO-19 | Valid location |
| `quantity_change` | NOT NULL | `nn_movement_records_change` | BO-19 | Signed delta required |
| `quantity_change` | CHECK | `chk_movement_records_change` <> 0 | BO-19 | Zero change not logged |
| `qty_before` | NOT NULL | `nn_movement_records_before` | BO-19 | Before snapshot |
| `qty_before` | CHECK | `chk_movement_records_before` >= 0 | LDM-01 | Non-negative before |
| `qty_after` | NOT NULL | `nn_movement_records_after` | BO-19 | After snapshot |
| `qty_after` | CHECK | `chk_movement_records_after` >= 0 | LDM-01 | Non-negative after |
| `(qty_before, qty_after, quantity_change)` | CHECK | `chk_movement_records_balance` qty_after = qty_before + quantity_change | BO-19 | Movement arithmetic integrity |
| `lot_batch_id` | FOREIGN KEY | `fk_movement_records_lot` → `inventory.lot_batches` | BR-017 | Lot on traceable movements |
| `reason_code_id` | FOREIGN KEY | `fk_movement_records_reason` → `governance.reason_codes` | BR-020 | Reason on adjustment movements |
| `source_document_type` | NOT NULL | `nn_movement_records_source_type` | BO-19 | Origin document type |
| `source_document_id` | NOT NULL | `nn_movement_records_source_id` | BO-19 | Origin document PK |
| `performed_by` | NOT NULL | `nn_movement_records_user` | BO-19 | User attribution |
| `performed_by` | FOREIGN KEY | `fk_movement_records_user` → `identity.user_accounts` | BO-19 | Valid user |
| `movement_timestamp` | NOT NULL | `nn_movement_records_timestamp` | BO-19 | Event time — partition key |
| `movement_timestamp` | DEFAULT | `def_movement_records_timestamp` = NOW() | BO-19 | Auto-stamp event time |

### `audit.audit_trail_records`

| Column | Type | Constraint | Business Rule | Justification |
|--------|------|------------|---------------|---------------|
| `audit_event_reference` | NOT NULL | `nn_audit_trail_ref` | BO-19 | Audit event identity |
| `(audit_event_reference, event_timestamp)` | UNIQUE | `uk_audit_trail_ref_ts` | BO-19 | Unique event per partition |
| `affected_entity_type` | NOT NULL | `nn_audit_trail_entity_type` | BO-19 | Entity type required |
| `affected_entity_id` | NOT NULL | `nn_audit_trail_entity_id` | BO-19 | Entity PK required |
| `action_performed` | NOT NULL | `nn_audit_trail_action` | BO-19 | Action classification |
| `action_performed` | CHECK | `chk_audit_trail_action` IN (CREATE, UPDATE, APPROVE, CANCEL) | BO-19 | Valid audit actions |
| `user_id` | NOT NULL | `nn_audit_trail_user` | BO-19 | Actor required |
| `user_id` | FOREIGN KEY | `fk_audit_trail_user` → `identity.user_accounts` | BO-19 | Valid user |
| `movement_record_id` | FOREIGN KEY | `fk_audit_trail_movement` → `audit.inventory_movement_records` | BO-19 | Links to operational movement |
| `event_timestamp` | NOT NULL | `nn_audit_trail_timestamp` | BO-19 | Event time — partition key |
| `event_timestamp` | DEFAULT | `def_audit_trail_timestamp` = NOW() | BO-19 | Auto-stamp event time |

### `audit.operational_alerts`

| Column | Type | Constraint | Business Rule | Justification |
|--------|------|------------|---------------|---------------|
| `alert_reference` | NOT NULL | `nn_operational_alerts_ref` | BR-009, BR-032 | Alert document identity |
| `alert_reference` | UNIQUE | `uk_operational_alerts_ref` | — | Unique alert reference |
| `alert_type` | NOT NULL | `nn_operational_alerts_type` | BR-009 | Alert classification |
| `alert_type` | CHECK | `chk_operational_alerts_type` IN (LOW_STOCK, OUT_OF_STOCK, PENDING_APPROVAL, TRANSFER_EXCEPTION, INBOUND_DELAY, CAMPAIGN_READINESS) | BR-009, BR-032 | Valid alert types |
| `severity` | NOT NULL | `nn_operational_alerts_severity` | BR-032 | Priority required |
| `severity` | DEFAULT | `def_operational_alerts_severity` = 'MEDIUM' | BR-032 | Medium default |
| `severity` | CHECK | `chk_operational_alerts_severity` IN (LOW, MEDIUM, HIGH, CRITICAL) | BR-032 | Valid severity levels |
| `product_id` | FOREIGN KEY | `fk_operational_alerts_product` → `catalog.products` | BR-009 | Alert context SKU |
| `location_id` | FOREIGN KEY | `fk_operational_alerts_location` → `network.inventory_locations` | BR-009 | Alert context site |
| `stock_position_id` | FOREIGN KEY | `fk_operational_alerts_position` → `inventory.stock_positions` | BR-009 | Threshold breach source |
| `acknowledgment_status` | NOT NULL | `nn_operational_alerts_ack` | BR-009 | Acknowledgment tracking |
| `acknowledgment_status` | DEFAULT | `def_operational_alerts_ack` = 'OPEN' | BR-009 | Open until acknowledged |
| `acknowledgment_status` | CHECK | `chk_operational_alerts_ack` IN (OPEN, ACKNOWLEDGED, RESOLVED) | BR-009 | Valid ack states |
| `resolution_status` | NOT NULL | `nn_operational_alerts_resolution` | BR-009 | Resolution tracking |
| `resolution_status` | DEFAULT | `def_operational_alerts_resolution` = 'PENDING' | BR-009 | Pending by default |
| `resolution_status` | CHECK | `chk_operational_alerts_resolution` IN (PENDING, RESOLVED, DISMISSED) | BR-009 | Valid resolution states |
| `alert_date` | NOT NULL | `nn_operational_alerts_date` | BR-009 | Alert creation time |
| `alert_date` | DEFAULT | `def_operational_alerts_date` = NOW() | BR-009 | Auto-stamp alert |
| `(resolution_status, resolved_at)` | CHECK | `chk_operational_alerts_resolved` | BR-009 | RESOLVED requires resolved_at |

### `audit.inventory_valuation_snapshots`

| Column | Type | Constraint | Business Rule | Justification |
|--------|------|------------|---------------|---------------|
| `snapshot_reference` | NOT NULL | `nn_valuation_snapshots_ref` | BR-008, BR-031 | Snapshot document identity |
| `snapshot_reference` | UNIQUE | `uk_valuation_snapshots_ref` | — | Unique snapshot reference |
| `valuation_date` | NOT NULL | `nn_valuation_snapshots_date` | BR-031 | As-of date required |
| `location_scope` | NOT NULL | `nn_valuation_snapshots_scope` | BR-031 | Scope classification |
| `location_scope` | CHECK | `chk_valuation_snapshots_scope` IN (SINGLE, REGION, NETWORK) | BR-031 | Valid scope values |
| `(valuation_date, location_scope)` | UNIQUE | `uk_valuation_snapshots_date_scope` | BR-031 | One snapshot per period per scope |
| `total_inventory_value` | NOT NULL | `nn_valuation_snapshots_total` | BR-031 | Total value required |
| `total_inventory_value` | CHECK | `chk_valuation_snapshots_total` >= 0 | BR-031 | Non-negative total |
| `owned_value` | NOT NULL | `nn_valuation_snapshots_owned` | BR-031 | Owned value required |
| `owned_value` | CHECK | `chk_valuation_snapshots_owned` >= 0 | BR-031 | Consignment excluded from owned |
| `consignment_value` | NOT NULL | `nn_valuation_snapshots_consignment` | BR-031 | Consignment tracked separately |
| `consignment_value` | DEFAULT | `def_valuation_snapshots_consignment` = 0 | BR-031 | Zero consignment default |
| `consignment_value` | CHECK | `chk_valuation_snapshots_consignment` >= 0 | BR-031 | Non-negative consignment |
| `(owned_value, consignment_value, total_inventory_value)` | CHECK | `chk_valuation_snapshots_sum` total >= owned | BR-031 | Total includes owned component |
| `reconciliation_status` | NOT NULL | `nn_valuation_snapshots_recon` | BR-008 | Reconciliation state |
| `reconciliation_status` | DEFAULT | `def_valuation_snapshots_recon` = 'DRAFT' | — | Draft until reconciled |
| `reconciliation_status` | CHECK | `chk_valuation_snapshots_recon` IN (DRAFT, RECONCILED, EXCEPTION) | BR-008 | Valid recon states |
| `prepared_by` | NOT NULL | `nn_valuation_snapshots_prepared_by` | BO-19 | Preparer attribution |
| `prepared_by` | FOREIGN KEY | `fk_valuation_snapshots_prepared_by` → `identity.user_accounts` | BO-19 | Valid user |

### `audit.inventory_valuation_lines`

| Column | Type | Constraint | Business Rule | Justification |
|--------|------|------------|---------------|---------------|
| `snapshot_id` | NOT NULL | `nn_valuation_lines_snapshot` | BR-031 | Line belongs to snapshot |
| `snapshot_id` | FOREIGN KEY | `fk_valuation_lines_snapshot` → `audit.inventory_valuation_snapshots` | BR-031 | Parent snapshot exists |
| `product_id` | NOT NULL | `nn_valuation_lines_product` | BR-031 | Valued SKU |
| `product_id` | FOREIGN KEY | `fk_valuation_lines_product` → `catalog.products` | BR-031 | Valid product |
| `location_id` | NOT NULL | `nn_valuation_lines_location` | BR-031 | Valued site |
| `location_id` | FOREIGN KEY | `fk_valuation_lines_location` → `network.inventory_locations` | BR-031 | Valid location |
| `(snapshot_id, product_id, location_id)` | UNIQUE | `uk_valuation_lines_snapshot_prod_loc` | BR-031 | One line per SKU per site per snapshot |
| `quantity` | NOT NULL | `nn_valuation_lines_qty` | BR-031 | Snapshot quantity |
| `quantity` | CHECK | `chk_valuation_lines_qty` >= 0 | BR-031 | Non-negative snapshot qty |
| `unit_cost` | NOT NULL | `nn_valuation_lines_cost` | BR-008 | Unit cost from matched invoices |
| `unit_cost` | CHECK | `chk_valuation_lines_cost` >= 0 | BR-008 | Non-negative unit cost |
| `extended_value` | NOT NULL | `nn_valuation_lines_extended` | BR-031 | Extended value required |
| `(quantity, unit_cost, extended_value)` | CHECK | `chk_valuation_lines_calc` extended_value = quantity * unit_cost | BR-031 | Valuation arithmetic integrity |
| `ownership_type` | NOT NULL | `nn_valuation_lines_ownership` | BR-031 | Ownership classification |
| `ownership_type` | DEFAULT | `def_valuation_lines_ownership` = 'OWNED' | BR-031 | Owned by default |
| `ownership_type` | CHECK | `chk_valuation_lines_ownership` IN (OWNED, CONSIGNMENT) | BR-031 | Consignment excluded from owned total |

---

## Appendix A: Business Rule to Constraint Index

| Business Rule | Key Constraints Enforcing Rule |
|---------------|------------------------------|
| **BR-001** ATP-only commitment | `chk_stock_positions_atp_formula`, `chk_stock_positions_atp_le_on_hand`, `chk_customer_order_lines_qty_balance` |
| **BR-002** Reservation at confirmation | `nn_inventory_reservations_*`, `fk_inventory_reservations_position`, `chk_stock_positions_reserved_le_on_hand` |
| **BR-003** Verified pick before shipment | `nn_shipments_fe`, `fk_shipments_fe`, `chk_fulfillment_executions_pick_status` |
| **BR-004** Verify before acceptance | `nn_goods_receipts_verification`, `chk_goods_receipt_lines_accepted_le_received` |
| **BR-005** Put-away before availability | `nn_put_aways_*`, `fk_put_aways_position`, `def_put_aways_availability` |
| **BR-006** Document discrepancies | `nn_receipt_discrepancies_*`, `uk_receipt_discrepancies_ref` |
| **BR-007** PO required for receipt | `chk_goods_receipts_po_or_exception`, `fk_goods_receipts_po` |
| **BR-008** Three-way match | `chk_supplier_invoices_payment_gate`, `uk_inv_gr_match_pair`, `chk_valuation_lines_cost` |
| **BR-009** Reorder at reorder level | `nn_stock_policies_*`, `uk_stock_policies_product_location`, `chk_operational_alerts_type` |
| **BR-010** Safety stock protection | `chk_stock_policies_safety`, `chk_stock_policies_threshold_order` |
| **BR-012** Protect source minimum | `chk_transfer_requests_distinct_locations`, `chk_stock_transfer_lines_qty` |
| **BR-013** Quarantine exclusion | `chk_stock_positions_atp_formula`, `chk_quarantine_holds_held_qty` |
| **BR-014** FEFO rotation | `chk_products_rotation_policy`, `chk_lot_batches_dates` |
| **BR-016** MRSL at receipt | `chk_products_shelf_life_mrsl`, `chk_receipt_discrepancies_type` |
| **BR-017** Lot capture | `chk_products_traceable_rotation`, `fk_*_lot` across receipt/pick/transfer |
| **BR-019** Independent count approval | `chk_count_variances_single_origin`, `chk_stock_adjustments_sod` |
| **BR-020** Mandatory reason codes | `nn_stock_adjustments_reason`, `fk_stock_adjustments_reason` |
| **BR-021** Independent approval | `chk_stock_adjustments_sod`, `chk_count_variances_approver_required` |
| **BR-022** Investigate before adjusting | `chk_count_variances_investigation`, `fk_stock_adjustments_variance` |
| **BR-023** Write-off authorization | `nn_inventory_write_offs_authorizer`, `chk_inventory_write_offs_sod` |
| **BR-024** Physical inventory freeze | `nn_physical_inventory_counts_freeze`, `chk_physical_inventory_counts_freeze_release` |
| **BR-025** RMA required | `nn_customer_returns_rma`, `fk_customer_returns_rma` |
| **BR-026** Inspect returns | `chk_return_dispositions_decision`, `chk_return_dispositions_restock` |
| **BR-027** No discontinued reorder | FK to `products` + application lifecycle check on insert |
| **BR-028** Backorder acknowledgment | `nn_backorders_acknowledged`, `chk_backorders_ack_timestamp` |
| **BR-029** Promotional ring-fence | `chk_promotional_allocations_qty`, `uk_promo_alloc_locations_alloc_loc` |
| **BR-030** Bonded customs | `chk_stock_positions_ownership`, `chk_quarantine_holds_type`, `chk_storage_positions_type` |
| **BR-031** Consignment ownership | `chk_stock_positions_ownership`, `chk_valuation_lines_ownership` |
| **BR-032** Class A monitoring | `chk_products_abc_classification`, `chk_operational_alerts_severity` |

---

## Appendix B: Constraint Count Summary

| Constraint Type | Approximate Count | Primary Purpose |
|-----------------|-------------------|-----------------|
| NOT NULL | ~420 | Mandatory business fields and audit columns |
| UNIQUE | ~75 | Business keys, document lines, dimensional identity |
| CHECK | ~130 | Quantity invariants, status enums, SoD, date logic, ATP formula |
| FOREIGN KEY | ~145 | Referential integrity across 14 schemas |
| DEFAULT | ~95 | Sensible initial states and auto-timestamps |

---

## Appendix C: Application-Layer Constraints (Not Database-Enforced)

These business rules require runtime validation beyond static CHECK constraints:

| Business Rule | Reason Not DB-Enforced | Application Enforcement |
|---------------|------------------------|-------------------------|
| BR-027 Discontinued product block | Requires join to `products.lifecycle_status` on child insert | Trigger or application service before PO/requisition/reservation insert |
| BR-019 Counter ≠ approver | Requires cross-row comparison on `cycle_counts` and `count_variances` | Application SoD check or deferred constraint trigger |
| BR-024 Location freeze | Requires checking `inventory_locations.is_frozen` on transaction insert | Application guard before receipt/shipment/transfer |
| BR-010 Safety stock bypass | Requires policy evaluation against live ATP | Domain service on reservation insert |
| BR-012 Source minimum on transfer | Requires `stock_policies` and `stock_positions` evaluation | Transfer approval service |
| BR-029 Promotional ring-fence | Requires live ATP segregation calculation | Stock Position aggregate coordination |

---

## Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Database Architect | | | |
| DDD Solution Architect | | | |
| Solution Architect | | | |
| Inventory Controller | | | |

---

*End of Database Constraints Specification*

*Document ID: SRS-DB-004 | Version 1.0 | July 6, 2026*
