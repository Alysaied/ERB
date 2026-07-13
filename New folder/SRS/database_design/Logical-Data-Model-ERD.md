# Logical Data Model (ERD)
## Inventory Management System

---

## Document Information

| Attribute | Detail |
|-----------|--------|
| **Document ID** | SRS-DB-001 |
| **Document Title** | Logical Data Model — Entity Relationship Diagram |
| **Version** | 1.0 |
| **Status** | Draft |
| **Document Owner** | Senior Database Architect |
| **Source Documents** | SRS-DM-001 (Domain Entities), SRS-DM-003 (Domain Aggregates), SRS-DM-004 (Entity Relationships), SRS-BR-001 (Business Rules), SRS-ARCH (System Architecture) |
| **Date** | July 6, 2026 |
| **Scope** | Logical business data model only — no SQL, physical storage, indexes, or database-vendor specifics |

### Purpose

This document defines the **Logical Data Model** for the Inventory Management System. It translates the approved domain model, business rules, and aggregate boundaries into a conceptual entity-relationship structure suitable for data architecture review and physical design planning.

The model contains **40 transactional and reference entities** aligned to domain entities, plus **4 derived/observability entities** modeled as logical projections. Relationships express business collaboration — not implementation join strategies.

### Design Principles

| Principle | Application |
|-----------|-------------|
| **Domain fidelity** | Entity names and semantics follow SRS-DM-008 ubiquitous language |
| **Aggregate awareness** | Each entity maps to a DDD aggregate root or child entity |
| **Identity over navigation** | Cross-aggregate links are logical references by business identity (SKU, location code, order number) |
| **Invariant visibility** | Business constraints from BR-001 – BR-032 are captured per entity |
| **Logical only** | No data types, keys, partitions, or persistence technology |

### Cardinality Notation

| Notation | Meaning |
|----------|---------|
| `1` | Exactly one |
| `0..1` | Zero or one (optional) |
| `1..*` | One or more (mandatory, many allowed) |
| `0..*` | Zero or more |
| `*` | Many (zero or more) |

### Relationship Type Legend

| Type | Meaning |
|------|---------|
| **Composition** | Child lifecycle bound to parent |
| **Association** | Independent entities with ongoing business link |
| **Reference** | Identity lookup without ownership |
| **Modification** | Source operation changes target quantity or status |
| **Derivation** | Target produced from or computed from source |
| **Authorization** | Source gates or permits action on target |
| **Verification** | Source validated against target before proceeding |

---

## Aggregate-to-Entity Map

| Aggregate | Aggregate Root | Child / Member Entities |
|-----------|----------------|-------------------------|
| Product Catalog | Product | — |
| Inventory Location | Inventory Location | Storage Position |
| Supplier | Supplier | — |
| Inventory Governance | Governance Policy | Reason Code |
| Stock Position | Stock Position | Lot/Batch, Quarantine Hold |
| Stock Policy | Stock Policy | — |
| Purchase Requisition | Purchase Requisition | — |
| Purchase Order | Purchase Order | Expected Inbound Delivery |
| Goods Receipt | Goods Receipt | Receipt Discrepancy, Put-Away |
| Supplier Invoice | Supplier Invoice | — |
| Customer Order Fulfillment | Customer Order | Inventory Reservation, Fulfillment Execution, Backorder, Shipment |
| Stock Transfer | Stock Transfer | In-Transit Stock *(Transfer Request is initial lifecycle state)* |
| Cycle Count | Cycle Count | — |
| Physical Inventory Count | Physical Inventory Count | — |
| Inventory Adjustment Case | Count Variance / Stock Adjustment | Stock Adjustment, Inventory Write-Off |
| Customer Return Case | Return Authorization | Customer Return, Return Disposition |
| Promotional Stock Allocation | Promotional Stock Allocation | — |
| User Account | User Account | Role Assignment |
| *(Derived — no aggregate)* | — | Inventory Movement Record, Audit Trail Record, Operational Alert, Inventory Valuation Snapshot |

---

## Text-Based ERD — System Overview

```
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                         MASTER DATA & NETWORK (Catalog & Network BC)                    │
├─────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                           │
│   ┌──────────┐         ┌───────────────────┐         ┌─────────────┐                   │
│   │ Product  │────────►│   Stock Policy    │◄────────│  Supplier   │                   │
│   │  (SKU)   │  1..*   │ (Product+Location)│         │             │                   │
│   └────┬─────┘         └─────────┬─────────┘         └──────┬──────┘                   │
│        │ 1                       │ 1                          │ 1                         │
│        │                         │                            │                           │
│        │ 0..*                    │ 1                          │ 0..*                      │
│        ▼                         ▼                            ▼                           │
│   ┌──────────────┐    ┌───────────────────┐         ┌─────────────────┐               │
│   │ Stock        │◄───│ Inventory Location │         │ Purchase Order  │               │
│   │ Position     │ 1  │  (hierarchy)       │         │                 │               │
│   │ (Product+    │    └─────────┬─────────┘         └────────┬────────┘               │
│   │  Location)   │              │ 1                            │ 1                        │
│   └──────┬───────┘              │ 1..*                         │ 0..*                   │
│          │                      ▼                              ▼                        │
│          │              ┌───────────────────┐         ┌─────────────────────┐            │
│          │              │ Storage Position  │         │ Expected Inbound    │            │
│          │              └───────────────────┘         │ Delivery            │            │
│          │                                            └─────────────────────┘            │
│   ┌──────┴───────┐    ┌───────────────────┐                                              │
│   │ Lot/Batch    │    │ Governance Policy │─── Reason Code                               │
│   │ Quarantine   │    └───────────────────┘                                              │
│   │ Hold         │                                                                        │
│   └──────────────┘                                                                        │
└─────────────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                      INBOUND SUPPLY (Procurement & Inbound BC)                            │
├─────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                           │
│   Purchase Requisition ──0..1──► Purchase Order ──0..*──► Goods Receipt               │
│         │ 1                              │ 1                      │ 1                    │
│         │                                │                        ├── Receipt Discrepancy │
│         ▼                                ▼                        └── Put-Away ──► Stock  │
│   Operational Alert              Supplier Invoice ◄── three-way match ──► Position       │
│   (trigger)                      (PO + GR + Invoice)                                      │
└─────────────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                      ORDER FULFILLMENT (Order Fulfillment BC)                             │
├─────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                           │
│   Customer Order ──┬── Inventory Reservation ──modifies──► Stock Position                 │
│                    ├── Fulfillment Execution ──0..1──► Shipment ──modifies──► Stock     │
│                    ├── Backorder                                                          │
│                    └── Return Authorization (returns path)                                │
│                                                                                           │
│   Promotional Stock Allocation ──modifies──► Stock Position (ring-fence)                │
└─────────────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                      NETWORK TRANSFER (Network Transfer BC)                               │
├─────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                           │
│   Transfer Request ──0..1──► Stock Transfer ──1..*──► In-Transit Stock                  │
│         │                           │                                                     │
│         └── verifies Stock Policy   └── modifies Stock Position (source + destination)    │
└─────────────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                   INVENTORY ACCURACY (Inventory Accuracy BC)                              │
├─────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                           │
│   Cycle Count ──0..1──► Count Variance ──0..1──► Stock Adjustment ──► Stock Position   │
│   Physical Inv. Count ──0..*──► Count Variance ──0..1──► Inventory Write-Off             │
│         │                                                                                 │
│         └── freezes Inventory Location (BR-024)                                           │
└─────────────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                      RETURNS (Returns BC)                                                   │
├─────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                           │
│   Return Authorization ──0..1──► Customer Return ──1..*──► Return Disposition             │
│         │                              │                         │                        │
│         └── verifies Customer Order    └── at Location           ├──► Stock Position      │
│                                                                  ├──► Quarantine Hold     │
│                                                                  └──► Inventory Write-Off │
└─────────────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────────────┐
│              ACCOUNTABILITY, OVERSIGHT & FINANCE (Cross-cutting)                        │
├─────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                           │
│   User Account ──1..*──► Role Assignment ──0..*──► Inventory Location (scope)           │
│                                                                                           │
│   Stock Position mutations ──derive──► Inventory Movement Record ──► Audit Trail Record │
│   Threshold breaches ──derive──► Operational Alert                                        │
│   Stock Position + costs ──derive──► Inventory Valuation Snapshot                         │
└─────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## Text-Based ERD — Core Inventory Hub

Stock Position is the central quantity authority. This diagram emphasizes modification paths.

```
                              ┌─────────────┐
                              │   Product   │
                              └──────┬──────┘
                                     │ 1
                    ┌────────────────┼────────────────┐
                    │ 1              │ 1              │ 0..*
                    ▼                ▼                ▼
             ┌────────────┐  ┌─────────────┐  ┌─────────────┐
             │Stock Policy│  │Stock Position│  │  Lot/Batch  │
             └─────┬──────┘  └──────┬──────┘  └──────┬──────┘
                   │                │                 │
                   │ derives        │ 0..*            │ 0..*
                   ▼                ▼                 ▼
             ┌────────────┐  ┌─────────────┐  ┌──────────────┐
             │Operational │  │ Quarantine  │  │ Promotional  │
             │   Alert    │  │    Hold     │  │ Stock Alloc. │
             └────────────┘  └─────────────┘  └──────────────┘
                                   ▲
                                   │
     ┌─────────────────────────────┼─────────────────────────────┐
     │ INCREASES on-hand (+)       │ DECREASES on-hand (-)         │
     ├─────────────────────────────┼─────────────────────────────┤
     │ Put-Away (after GR)         │ Shipment                      │
     │ Stock Transfer (receipt)    │ Stock Transfer (dispatch)     │
     │ Return Disposition (restock)│ Stock Adjustment (-)        │
     │ Stock Adjustment (+)        │ Inventory Write-Off           │
     └─────────────────────────────┴─────────────────────────────┘

     MODIFIES ATP (reserved ring-fence, not on-hand):
     Inventory Reservation (+reserved / -ATP)
     Promotional Stock Allocation (-general ATP)
     Quarantine Hold (-ATP)
```

---

## Entity Catalog

Entities are grouped by business domain. Each entry includes business purpose, relationships, cardinality, owning aggregate, and governing constraints.

---

### Domain 1: Master Data & Reference

---

#### 1. Product

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Canonical stock-keeping unit (SKU) identity for all inventory operations — what the organization buys, holds, and sells across locations and channels. |
| **Related Aggregate** | Product Catalog *(root)* |
| **Relationships** | → Stock Position (Association); → Stock Policy (Association); → Lot/Batch (Composition); referenced by procurement, fulfillment, transfer, count, and return line items |
| **Cardinality** | Product `1` → Stock Position `0..*`; Product `1` → Stock Policy `0..*`; Product `1` → Lot/Batch `0..*` |
| **Important Business Constraints** | SKU must be unique. Name and unit of measure are mandatory. Discontinued products must not appear on new POs or requisitions (BR-027). Traceable products must declare lot requirement and rotation policy (FIFO/FEFO). ABC classification must be A, B, or C when assigned (BR-032). |

---

#### 2. Inventory Location

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Physical site in the distribution network where stock is received, stored, counted, and fulfilled. |
| **Related Aggregate** | Inventory Location *(root)* |
| **Relationships** | → Storage Position (Composition); → Stock Position (Association); → Inventory Location parent (Hierarchy Association); → Physical Inventory Count (Association); referenced as receiving, fulfillment, and transfer endpoint |
| **Cardinality** | Location `1` → Storage Position `1..*`; Location `1` → Stock Position `0..*`; Child Location `0..1` → Parent Location `1` |
| **Important Business Constraints** | Location cannot be its own ancestor. Deactivated/closing locations must not accept new receipts, reservations, or fulfillments. Physical inventory freeze (BR-024) blocks movements while wall-to-wall count is active. Closure blocked while on-hand stock remains without disposition plan. |

---

#### 3. Storage Position

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Designated storage area (zone, aisle, bin) within a location for put-away placement and pick path guidance. |
| **Related Aggregate** | Inventory Location *(child of Inventory Location aggregate)* |
| **Relationships** | ← Inventory Location (Composition); → Put-Away (Association); → Fulfillment Execution (Reference); → Cycle Count (optional Reference) |
| **Cardinality** | Storage Position `1` → Inventory Location `1`; Storage Position `1` → Put-Away `0..*`; Put-Away `1` → Storage Position `1` |
| **Important Business Constraints** | Cannot exist outside parent location. Put-away must assign storage position before stock becomes available (BR-005). Rotation placement (FIFO/FEFO) applied at put-away (BR-014, BR-015). Put-away suspended during location freeze (BR-024). |

---

#### 4. Stock Policy

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Replenishment thresholds (reorder level, minimum, safety stock) for a product at a specific location. |
| **Related Aggregate** | Stock Policy *(root)* |
| **Relationships** | → Product (Reference); → Inventory Location (Reference); → Operational Alert (Derivation); verified by Transfer Request |
| **Cardinality** | Stock Policy `1` → Product `1`; Stock Policy `1` → Inventory Location `1`; Product + Location uniquely identifies policy; Stock Policy `1` → Operational Alert `0..*` |
| **Important Business Constraints** | Reorder, minimum, and safety stock must be non-negative. Minimum must not exceed reorder level unless explicitly authorized. Replenishment triggers when ATP reaches reorder level (BR-009). Safety stock must not be bypassed without approval (BR-010). Source minimum constrains transfer quantity (BR-012). |

---

#### 5. Reason Code

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Standardized categorized explanation for adjustments, write-offs, and receipt exceptions. |
| **Related Aggregate** | Inventory Governance *(child of Governance Policy aggregate)* |
| **Relationships** | → Stock Adjustment (Authorization); → Inventory Write-Off (Authorization); → Receipt Discrepancy (Association) |
| **Cardinality** | Reason Code `1` → Stock Adjustment `0..*`; Stock Adjustment `1` → Reason Code `1`; Write-Off `1` → Reason Code `1` |
| **Important Business Constraints** | Reason codes must be unique. Retired codes not selectable for new transactions. Mandatory on every adjustment and write-off (BR-020, BR-023). |

---

#### 6. Governance Policy

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Organization-wide control policies — approval thresholds, tolerance limits, segregation-of-duties rules, and exception handling. |
| **Related Aggregate** | Inventory Governance *(root)* |
| **Relationships** | → Stock Adjustment (Verification); → Count Variance (Verification); → Goods Receipt (Verification); contains Reason Code |
| **Cardinality** | Governance Policy `1` → Stock Adjustment `0..*`; Governance Policy `1` → Count Variance `0..*`; Governance Policy `1` → Goods Receipt `0..*` |
| **Important Business Constraints** | Only one effective policy version per parameter at any time. Adjustments above threshold require independent approval (BR-021). Counter must not approve own count variances (BR-019). PO required for supplier receipt except approved ad-hoc exception (BR-007). |

---

### Domain 2: Inventory State & Balance

---

#### 7. Stock Position

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Authoritative inventory balance for a product at a location — on-hand, reserved, and available-to-promise (ATP). |
| **Related Aggregate** | Stock Position *(root)* |
| **Relationships** | → Product, Inventory Location, Stock Policy (Reference); → Lot/Batch, Quarantine Hold (Composition); modified by Reservation, Shipment, GR/Put-Away, Transfer, Adjustment, Write-Off, Return Disposition, Promotional Allocation |
| **Cardinality** | Stock Position `1` → Product `1`; Stock Position `1` → Inventory Location `1`; Stock Position `1` → Stock Policy `0..1`; Stock Position `1` → Lot/Batch `0..*`; Stock Position `1` → Quarantine Hold `0..*` |
| **Important Business Constraints** | On-hand never negative. ATP = on-hand − reserved − quarantined (BR-001, BR-013). ATP never exceeds on-hand. Consignment stock not owned until consumption (BR-031). All mutations produce Inventory Movement Record. Location freeze blocks changes except authorized count adjustments (BR-024). |

---

#### 8. Lot / Batch

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Traceable production or receipt grouping enabling recall, FEFO rotation, and regulatory compliance. |
| **Related Aggregate** | Stock Position *(child when product is traceable)* |
| **Relationships** | ← Product (Composition); ← Stock Position (Composition); → Supplier (Reference); referenced on GR, Put-Away, Fulfillment, Transfer, Quarantine Hold |
| **Cardinality** | Product `1` → Lot/Batch `0..*`; Stock Position `1` → Lot/Batch `0..*`; Lot/Batch `0..1` → Supplier `1` |
| **Important Business Constraints** | Lot identity captured at receipt and all movements for traceable products (BR-017). FEFO pick by expiration (BR-014). MRSL validated at receipt (BR-016). |

---

#### 9. Quarantine Hold

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Inventory physically on-hand but excluded from sellable ATP due to quality, regulatory, recall, or customs hold. |
| **Related Aggregate** | Stock Position *(child)* |
| **Relationships** | ← Stock Position (Composition); → Lot/Batch (Reference); derived from Return Disposition; may derive Adjustment or Write-Off on release |
| **Cardinality** | Stock Position `1` → Quarantine Hold `0..*`; Quarantine Hold `0..1` → Lot/Batch `1` |
| **Important Business Constraints** | Held quantity excluded from ATP (BR-013). Bonded inventory held until customs clearance (BR-030). Release restores ATP only after clearance confirmed. |

---

#### 10. Promotional Stock Allocation

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Ring-fenced inventory for promotional campaigns or product launches, protected from general demand. |
| **Related Aggregate** | Promotional Stock Allocation *(root)* |
| **Relationships** | → Product (Reference); → Inventory Location `1..*` (Reference); → Stock Position (Modification); → Operational Alert (Derivation) |
| **Cardinality** | Allocation `1` → Product `1`; Allocation `1` → Location `1..*`; Allocation `0..*` → Stock Position `1` |
| **Important Business Constraints** | Ring-fenced quantity must not serve non-promotional orders without commercial approval (BR-029). Allocation cannot exceed available stock at allocation time. Inactive outside campaign period. Unconsumed allocation released after campaign end. |

---

### Domain 3: Procurement & Inbound Supply

---

#### 11. Supplier

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | External vendor — commercial counterparty for procurement, receipt, and payment. |
| **Related Aggregate** | Supplier *(root)* |
| **Relationships** | → Purchase Order (Association); → Supplier Invoice (Association); referenced by Goods Receipt and Lot/Batch |
| **Cardinality** | Supplier `1` → Purchase Order `0..*`; Supplier `1` → Supplier Invoice `0..*` |
| **Important Business Constraints** | Supplier code unique. Must be active for new POs. Consignment indicator governs ownership at receipt (BR-031). Payment terms required before PO issuance. |

---

#### 12. Purchase Requisition

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Internal request to procure stock, preceding formal PO creation with approval workflow. |
| **Related Aggregate** | Purchase Requisition *(root)* |
| **Relationships** | → Product `1..*` (Reference); → Inventory Location (Reference); → Purchase Order (Derivation); → Operational Alert (Reference) |
| **Cardinality** | Requisition `1` → Product `1..*`; Requisition `1` → Location `1`; Requisition `1` → Purchase Order `0..1`; Alert `0..1` → Requisition `0..1` |
| **Important Business Constraints** | Lines must reference active products — discontinued prohibited (BR-027). Network availability evaluated before approval (BR-011). Safety stock not implicitly bypassed (BR-010). Must be approved before PO conversion. |

---

#### 13. Purchase Order

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Authorized commercial commitment to a supplier specifying products, quantities, prices, and delivery terms. |
| **Related Aggregate** | Purchase Order *(root)* |
| **Relationships** | → Supplier, Inventory Location, Product (Reference); → Expected Inbound Delivery (Composition); → Goods Receipt (Authorization); → Supplier Invoice (Verification) |
| **Cardinality** | PO `1` → Supplier `1`; PO `1` → Location `1`; PO `1` → Product `1..*`; PO `1` → Expected Delivery `0..*`; PO `1` → Goods Receipt `0..*` |
| **Important Business Constraints** | Valid PO required before supplier receipt except approved exception (BR-007). Discontinued products prohibited (BR-027). Received qty per line within tolerance or discrepancy workflow. Status: open → partial → closed/cancelled. |

---

#### 14. Expected Inbound Delivery

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Planned or confirmed supplier shipment communicating anticipated arrival for receiving preparation. |
| **Related Aggregate** | Purchase Order *(child)* |
| **Relationships** | → Purchase Order (Reference); → Stock Position (Derivation — informational inbound expected); → Operational Alert (Derivation) |
| **Cardinality** | Expected Delivery `1` → Purchase Order `1`; Expected Delivery `0..*` → Stock Position `1` |
| **Important Business Constraints** | Expected quantities must not exceed remaining open PO line quantities. Inbound expected is informational only — does not increase ATP until put-away (BR-005). Delays trigger replenishment notifications. |

---

#### 15. Goods Receipt

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Business event of accepting verified inbound goods into inventory control after dock verification. |
| **Related Aggregate** | Goods Receipt *(root)* |
| **Relationships** | → Purchase Order (Verification); → Supplier, Inventory Location (Reference); → Receipt Discrepancy, Put-Away (Composition); → Stock Position (Modification on put-away completion); → Lot/Batch (Derivation) |
| **Cardinality** | Goods Receipt `0..*` → Purchase Order `0..1`; GR `1` → Supplier `1`; GR `1` → Location `1`; GR `1` → Discrepancy `0..*`; GR `1` → Put-Away `1..*` |
| **Important Business Constraints** | Verify quantity, product, condition before acceptance (BR-004). PO required except exception (BR-007). Discrepancies documented before acceptance (BR-006). MRSL met for shelf-life products (BR-016). Lot captured for traceable products (BR-017). Receipt blocked during location freeze (BR-024). |

---

#### 16. Receipt Discrepancy

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Documented difference between expected and actual receipt (short, over, wrong item, damage, shelf-life failure). |
| **Related Aggregate** | Goods Receipt *(child)* |
| **Relationships** | → Goods Receipt (Composition); → Reason Code (Association) |
| **Cardinality** | Discrepancy `1` → Goods Receipt `1`; Goods Receipt `1` → Discrepancy `0..*` |
| **Important Business Constraints** | Must be recorded before acceptance of affected quantities (BR-006). Unresolved discrepancies affect three-way match (BR-008). Shelf-life non-compliance recorded as discrepancy (BR-016). |

---

#### 17. Put-Away

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Confirmation that received goods are moved from receiving area to storage position and are operationally available. |
| **Related Aggregate** | Goods Receipt *(child)* |
| **Relationships** | → Goods Receipt (Reference); → Storage Position (Association); → Stock Position (Modification — triggers on-hand/ATP increase) |
| **Cardinality** | Put-Away `1` → Goods Receipt `1`; Put-Away `1` → Storage Position `1` |
| **Important Business Constraints** | ATP not increased until put-away confirmed (BR-005). Rotation placement applied (BR-014, BR-015). Bonded goods to hold storage until customs clearance (BR-030). |

---

#### 18. Supplier Invoice

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Supplier billing document — financial leg of three-way match against PO and goods receipt. |
| **Related Aggregate** | Supplier Invoice *(root)* |
| **Relationships** | → Supplier, Purchase Order (Reference); → Goods Receipt (Verification); → Inventory Valuation Snapshot (Derivation) |
| **Cardinality** | Invoice `1` → Supplier `1`; Invoice `1` → Purchase Order `1`; Invoice `1` → Goods Receipt `0..*` |
| **Important Business Constraints** | Three-way match within tolerance before payment (BR-008). Payment prohibited for unordered, unreceived, or mispriced goods. Match exceptions require resolution or waiver. |

---

### Domain 4: Order Fulfillment

---

#### 19. Customer Order

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Customer demand triggering availability confirmation, reservation, picking, and shipment. |
| **Related Aggregate** | Customer Order Fulfillment *(root)* |
| **Relationships** | → Stock Position (Reference for ATP); → Inventory Reservation, Fulfillment Execution, Backorder, Shipment (Composition); → Return Authorization (Association) |
| **Cardinality** | Order `1` → Reservation `0..*`; Order `1` → Fulfillment `0..*`; Order `1` → Backorder `0..*`; Order `1` → Shipment `0..*`; Order `1` → Stock Position `1..*` |
| **Important Business Constraints** | Commit only against ATP, not total on-hand (BR-001). Reserve at confirmation (BR-002). Respect promotional ring-fence (BR-029). Order line reconciliation: requested = reserved + fulfilled + backordered + cancelled. |

---

#### 20. Inventory Reservation

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Operational hold on stock for a confirmed order line, reducing ATP until fulfillment or release. |
| **Related Aggregate** | Customer Order Fulfillment *(child)* |
| **Relationships** | → Customer Order (Reference); → Product, Inventory Location (Reference); → Stock Position (Modification); consumed by Shipment |
| **Cardinality** | Reservation `1` → Customer Order `1`; Reservation `1` → Product `1`; Reservation `0..*` → Stock Position `1` |
| **Important Business Constraints** | Created at order confirmation (BR-002). Must not consume below safety stock without exception (BR-010). Promotional ring-fence respected (BR-029). Released on cancellation; consumed on shipment. |

---

#### 21. Fulfillment Execution

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Warehouse pick, verify, and pack work bridging reservation to shipment. |
| **Related Aggregate** | Customer Order Fulfillment *(child)* |
| **Relationships** | → Customer Order (Reference); → Inventory Location, Storage Position, Lot/Batch (Reference); → Shipment (Derivation) |
| **Cardinality** | Fulfillment `1` → Customer Order `1`; Fulfillment `1` → Location `1`; Fulfillment `1` → Shipment `0..1` |
| **Important Business Constraints** | Verified pick required before shipment (BR-003). FEFO/FIFO applied during pick (BR-014, BR-015). Lot captured on pick for traceable products (BR-017). Blocked at frozen location (BR-024). |

---

#### 22. Backorder

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Customer-agreed delay for unfulfilled order line quantity when full ATP unavailable. |
| **Related Aggregate** | Customer Order Fulfillment *(child)* |
| **Relationships** | → Customer Order (Reference); → Product (Reference) |
| **Cardinality** | Backorder `1` → Customer Order `1`; Backorder `1` → Product `1` |
| **Important Business Constraints** | Explicit customer acknowledgment required before recording (BR-028). May convert to reservation when stock arrives. Replenishment priority may apply. |

---

#### 23. Shipment

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Confirmed dispatch of fulfilled goods — inventory deduction and delivery promise activation. |
| **Related Aggregate** | Customer Order Fulfillment *(child)* |
| **Relationships** | → Customer Order, Fulfillment Execution (Reference); → Inventory Reservation (Modification); → Stock Position (Modification) |
| **Cardinality** | Shipment `1` → Fulfillment Execution `1`; Shipment `0..*` → Reservation `1`; Shipment `0..*` → Stock Position `1` |
| **Important Business Constraints** | Only after verified pick (BR-003). Deducts on-hand and consumes reservation (BR-002). Creates outbound movement record. |

---

### Domain 5: Network Balance

---

#### 24. Transfer Request

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Formal request to move stock between locations to resolve shortage or rebalance network before new procurement. |
| **Related Aggregate** | Stock Transfer *(initial lifecycle state within Stock Transfer aggregate)* |
| **Relationships** | → Inventory Location source and destination (Reference); → Product `1..*` (Reference); → Stock Policy source (Verification); → Stock Transfer (Derivation) |
| **Cardinality** | Request `1` → Source Location `1`; Request `1` → Destination Location `1`; Request `1` → Product `1..*`; Request `1` → Stock Transfer `0..1` |
| **Important Business Constraints** | Must not deplete source below minimum (BR-012). Network check before purchase alternative (BR-011). Safety stock at source protected (BR-010). Source and destination must be distinct active locations. |

---

#### 25. Stock Transfer

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Executed inter-location stock movement from dispatch through destination receipt. |
| **Related Aggregate** | Stock Transfer *(root)* |
| **Relationships** | → Transfer Request (Reference); → In-Transit Stock (Composition); → Stock Position source and destination (Modification); → Lot/Batch (Reference) |
| **Cardinality** | Transfer `0..1` → Transfer Request `1`; Transfer `1` → In-Transit Stock `1..*`; Transfer `1` → Stock Position `2` per product line |
| **Important Business Constraints** | Source not depleted below minimum (BR-012). Lot captured for traceable products (BR-017). Blocked during location freeze (BR-024). In-transit excluded from both endpoints' ATP until receipt. |

---

#### 26. In-Transit Stock

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Pipeline inventory that left source but is not yet received at destination. |
| **Related Aggregate** | Stock Transfer *(child)* |
| **Relationships** | → Stock Transfer (Composition); references Product, source and destination locations |
| **Cardinality** | In-Transit `1` → Stock Transfer `1`; Transfer `1` → In-Transit `1..*` |
| **Important Business Constraints** | Excluded from source and destination ATP until receipt confirmed. Delayed/lost in-transit triggers exception alerts. |

---

### Domain 6: Inventory Control & Accuracy

---

#### 27. Cycle Count

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Scheduled partial physical count on rotating basis without full warehouse shutdown. |
| **Related Aggregate** | Cycle Count *(root)* |
| **Relationships** | → Product, Inventory Location (Reference); → Storage Position (optional Reference); → Count Variance (Derivation); → User Account counter (Reference) |
| **Cardinality** | Cycle Count `1` → Product `1`; Cycle Count `1` → Location `1`; Cycle Count `0..1` → Storage Position `1`; Cycle Count `1` → Count Variance `0..1` |
| **Important Business Constraints** | Blind count — counter must not see system quantity (BR-018). Class A highest frequency (BR-032). Does not directly mutate Stock Position — spawns Adjustment Case on variance. Counter ≠ approver (BR-019). |

---

#### 28. Physical Inventory Count

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Comprehensive wall-to-wall count at a location for audit-mandated accuracy baseline. |
| **Related Aggregate** | Physical Inventory Count *(root)* |
| **Relationships** | → Inventory Location (Association); → Count Variance `0..*` (Derivation) |
| **Cardinality** | Physical Count `1` → Location `1`; Location `1` → Physical Count `0..*`; Physical Count `1` → Count Variance `0..*` |
| **Important Business Constraints** | Location freeze during count — no receiving, shipping, transfers, or adjustments (BR-024). Full location scope required. Certification requires variances routed to adjustment cases. |

---

#### 29. Count Variance

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Identified difference between system and physical quantity requiring investigation before correction. |
| **Related Aggregate** | Inventory Adjustment Case *(root when originating from count)* |
| **Relationships** | → Cycle Count or Physical Inventory Count (Reference); → Stock Position (Reference); → Stock Adjustment (Derivation); → User Account approver (Reference); verified by Governance Policy |
| **Cardinality** | Variance `1` → exactly one count origin; Variance `1` → Stock Position `1`; Variance `1` → Stock Adjustment `0..1` |
| **Important Business Constraints** | Investigate before adjusting (BR-022). Counter must not approve own variance (BR-019). Independent approval above threshold (BR-021). |

---

#### 30. Stock Adjustment

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Corrective change to recorded inventory quantity with mandatory reason and authorization. |
| **Related Aggregate** | Inventory Adjustment Case *(child)* |
| **Relationships** | → Stock Position (Modification); → Count Variance (optional Reference); → Reason Code (Reference); → User Account initiator and approver (Reference); verified by Governance Policy |
| **Cardinality** | Adjustment `0..1` → Count Variance `1`; Adjustment `1` → Reason Code `1`; Adjustment `0..*` → Stock Position `1` |
| **Important Business Constraints** | Mandatory reason code (BR-020). Independent approval above threshold (BR-021). Investigate when from count (BR-022). Must not drive stock negative. |

---

#### 31. Inventory Write-Off

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Formal authorized permanent removal of inventory value for damaged, obsolete, expired, or lost goods. |
| **Related Aggregate** | Inventory Adjustment Case *(child)* |
| **Relationships** | → Stock Position (Modification); → Reason Code (Reference); → Return Disposition (Reference); → User Account authorizer (Authorization) |
| **Cardinality** | Write-Off `0..*` → Stock Position `1`; Write-Off `1` → Reason Code `1`; Disposition `0..1` → Write-Off `1` |
| **Important Business Constraints** | Documented evidence and authorization required (BR-023). Mandatory reason code (BR-020). Terminal — quantity permanently removed. |

---

### Domain 7: Returns Management

---

#### 32. Return Authorization

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Approved permission (RMA) for customer return linked to original order before warehouse acceptance. |
| **Related Aggregate** | Customer Return Case *(root)* |
| **Relationships** | → Customer Order (Verification); → Product `1..*` (Reference); → Customer Return (Authorization) |
| **Cardinality** | RMA `1` → Customer Order `1`; RMA `1` → Product `1..*`; RMA `1` → Customer Return `0..1` |
| **Important Business Constraints** | Required before warehouse acceptance (BR-025). Must link to original order. RMA expiration enforced. Returned products must match authorized lines. |

---

#### 33. Customer Return

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Physical receipt of customer-returned goods at warehouse, initiating inspection workflow. |
| **Related Aggregate** | Customer Return Case *(child)* |
| **Relationships** | → Return Authorization (Verification); → Inventory Location (Reference); → Return Disposition (Composition) |
| **Cardinality** | Return `1` → RMA `1`; Return `1` → Location `1`; Return `1` → Disposition `1..*` |
| **Important Business Constraints** | No receipt without valid RMA (BR-025). Verify quantity and product on receipt (BR-004). Inspection mandatory before disposition (BR-026). |

---

#### 34. Return Disposition

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Business decision on returned goods — restock, quarantine, or write-off based on condition. |
| **Related Aggregate** | Customer Return Case *(child)* |
| **Relationships** | → Customer Return (Reference); → Stock Position (Modification on restock); → Quarantine Hold, Inventory Write-Off (Derivation) |
| **Cardinality** | Disposition `1` → Customer Return `1`; Disposition `0..1` → Stock Position `1`; Disposition `0..1` → Quarantine Hold `0..1`; Disposition `0..1` → Write-Off `1` |
| **Important Business Constraints** | Inspect before restock (BR-026). Restock only when condition confirms resale quality. Damaged goods to quarantine or write-off — never direct to ATP. |

---

### Domain 8: Accountability & Oversight

---

#### 35. Inventory Movement Record

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Immutable documented change in inventory position — operational history of every stock activity. |
| **Related Aggregate** | *(Derived — append-only event log; not an aggregate consistency boundary)* |
| **Relationships** | → Stock Position (Association); → originating business document (Reference); → User Account (Reference); → Lot/Batch, Reason Code (optional Reference) |
| **Cardinality** | Movement `0..*` → Stock Position `1`; Movement `1` → originating document `1`; Movement `1` → User Account `1` |
| **Important Business Constraints** | Every stock mutation must produce a movement record. Lot on movement for traceable products (BR-017). Reason code on adjustment movements (BR-020). Immutable after creation. |

---

#### 36. Audit Trail Record

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Governance-grade record of material changes with user identity, timestamp, and before/after state. |
| **Related Aggregate** | *(Derived — compliance log; not an aggregate consistency boundary)* |
| **Relationships** | → governed entity (Association); → Inventory Movement Record (Association); → User Account (Reference) |
| **Cardinality** | Audit `0..*` → governed entity `1`; Audit `0..1` → Movement Record `1`; Audit `1` → User Account `1` |
| **Important Business Constraints** | Supports segregation-of-duties verification (BR-019, BR-021). Immutable after write. Material changes require both movement and audit records. |

---

#### 37. Operational Alert

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Proactive notification of conditions requiring human review — low stock, pending approval, exceptions. |
| **Related Aggregate** | *(Derived — read model / notification projection)* |
| **Relationships** | derived from Stock Position + Stock Policy; Transfer Request; Promotional Allocation; Expected Inbound Delivery |
| **Cardinality** | Alert `0..*` → Stock Position `1`; Alert `0..*` → Transfer Request `0..1`; Alert `0..*` → Promotional Allocation `0..1` |
| **Important Business Constraints** | Reorder-level breach triggers same-day replenishment review (BR-009). Class A products generate higher-priority alerts (BR-032). Campaign readiness alerts before launch commitment (BR-029). |

---

#### 38. User Account

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Identified individual authorized to perform inventory operations within role and location scope. |
| **Related Aggregate** | User Account *(root)* |
| **Relationships** | → Role Assignment (Composition); associated with Cycle Count, Goods Receipt, Adjustments, Movement and Audit records |
| **Cardinality** | User Account `1` → Role Assignment `1..*` |
| **Important Business Constraints** | User identifier unique. At least one role required to transact. Conflicting duty combinations blocked — counter + approver (BR-019, BR-021). Deactivated accounts cannot perform actions. |

---

#### 39. Role Assignment

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Delegation of business permissions to a user with location scope and segregation-of-duties enforcement. |
| **Related Aggregate** | User Account *(child)* |
| **Relationships** | → User Account (Composition); → Inventory Location `0..*` (Reference for scope) |
| **Cardinality** | Role Assignment `1` → User Account `1`; Role Assignment `1` → Location `0..*` |
| **Important Business Constraints** | SoD conflicts blocked at assignment. Location scope enforced on transactions. Effective-dated with history retained. Empty scope may mean network-wide for executive roles. |

---

### Domain 9: Financial Alignment

---

#### 40. Inventory Valuation Snapshot

| Aspect | Detail |
|--------|--------|
| **Business Purpose** | Point-in-time inventory value summary by product and location for finance reconciliation and month-end close. |
| **Related Aggregate** | *(Derived — reporting read model; rebuilt from Stock Position events and matched costs)* |
| **Relationships** | derived from Stock Position, Product, Inventory Location; references Supplier Invoice costs, Inventory Write-Off |
| **Cardinality** | Snapshot `1` → Stock Position `0..*`; Snapshot `1` → Product `0..*`; Snapshot `1` → Location `0..*` |
| **Important Business Constraints** | Consignment stock excluded from owned valuation (BR-031). Quarantined and in-transit stock excluded per policy. Three-way matched invoice costs authoritative for received inventory (BR-008). |

---

## Relationship Summary Matrix

| From Entity | To Entity | Type | Cardinality | Governing Rules |
|-------------|-----------|------|-------------|-----------------|
| Product | Stock Position | Association | 1 : 0..* | BR-001, BR-027, BR-017 |
| Product | Stock Policy | Association | 1 : 0..* | BR-009, BR-032 |
| Inventory Location | Storage Position | Composition | 1 : 1..* | BR-005, BR-024 |
| Inventory Location | Stock Position | Association | 1 : 0..* | BR-012, BR-024 |
| Stock Position | Quarantine Hold | Composition | 1 : 0..* | BR-013, BR-030 |
| Stock Position | Lot/Batch | Composition | 1 : 0..* | BR-017, BR-014 |
| Inventory Reservation | Stock Position | Modification | 0..* : 1 | BR-002, BR-010, BR-029 |
| Goods Receipt | Put-Away | Composition | 1 : 1..* | BR-005 |
| Put-Away | Stock Position | Modification | 0..* : 1 | BR-005 |
| Purchase Order | Goods Receipt | Authorization | 1 : 0..* | BR-007, BR-004 |
| Customer Order | Inventory Reservation | Composition | 1 : 0..* | BR-002 |
| Fulfillment Execution | Shipment | Derivation | 1 : 0..1 | BR-003 |
| Shipment | Stock Position | Modification | 0..* : 1 | BR-003 |
| Transfer Request | Stock Transfer | Derivation | 1 : 0..1 | BR-012 |
| Stock Transfer | In-Transit Stock | Composition | 1 : 1..* | — |
| Cycle Count | Count Variance | Derivation | 1 : 0..1 | BR-018, BR-022 |
| Count Variance | Stock Adjustment | Derivation | 1 : 0..1 | BR-019, BR-021, BR-022 |
| Return Authorization | Customer Return | Authorization | 1 : 0..1 | BR-025 |
| Return Disposition | Stock Position | Modification | 0..1 : 1 | BR-026 |
| Supplier Invoice | Purchase Order + Goods Receipt | Verification | 1 : 1 + 0..* | BR-008 |
| User Account | Role Assignment | Composition | 1 : 1..* | BR-019, BR-021 |

*Full relationship catalog: SRS-DM-004 (REL-001 – REL-134).*

---

## Cross-Aggregate Reference Model

Aggregates coordinate through **identity references** and **domain events** — not shared mutable structures.

```
┌──────────────────┐   PutAwayCompleted    ┌──────────────────┐
│  Goods Receipt   │ ─────────────────────►│  Stock Position  │
│  (Aggregate 9)   │                       │  (Aggregate 5)   │
└──────────────────┘                       └────────▲─────────┘
                                                  │
┌──────────────────┐   ReservationCommitted       │
│ Customer Order   │ ───────────────────────────┤
│ Fulfillment (11)│   ShipmentDispatched        │
└──────────────────┘ ───────────────────────────┘

┌──────────────────┐   TransferDispatched/Received
│  Stock Transfer  │ ───────────────────────────► Stock Position
│  (Aggregate 12)  │
└──────────────────┘

┌──────────────────┐   AdjustmentApproved
│ Adjustment Case  │ ───────────────────────────► Stock Position
│  (Aggregate 15)  │
└──────────────────┘

┌──────────────────┐   RestockApproved
│ Customer Return  │ ───────────────────────────► Stock Position
│  Case (16)       │
└──────────────────┘
```

| Interaction Rule | Description |
|------------------|-------------|
| One transaction, one aggregate | Stock deduction and PO creation never share a consistency boundary |
| Reference by identity | Cross-aggregate links use SKU, location code, order number — not object graphs |
| Consult, don't couple | Transfer consults Stock Policy and Stock Position by identity for source minimum |
| Governance consultation | Adjustment aggregates consult Inventory Governance for thresholds and reason codes |
| Catalog validation | Procurement and fulfillment consult Product Catalog for lifecycle status |

---

## Entity Integrity Rules (Logical Level)

| Rule ID | Rule | Entities Affected |
|---------|------|-------------------|
| LDM-01 | ATP = on-hand − reserved − quarantined; ATP ≤ on-hand | Stock Position, Quarantine Hold, Inventory Reservation |
| LDM-02 | Stock availability increases only after Put-Away completion | Goods Receipt, Put-Away, Stock Position |
| LDM-03 | Shipment decreases on-hand only after verified Fulfillment Execution | Fulfillment Execution, Shipment, Stock Position |
| LDM-04 | Product + Location uniquely identifies Stock Position and Stock Policy | Stock Position, Stock Policy |
| LDM-05 | Discontinued Product prohibited on new PO, Requisition, and Reservation lines | Product, Purchase Order, Purchase Requisition, Inventory Reservation |
| LDM-06 | Counter User Account ≠ Approver User Account on same Count Variance | Cycle Count, Count Variance, User Account |
| LDM-07 | Customer Return requires valid Return Authorization | Return Authorization, Customer Return |
| LDM-08 | In-transit quantity excluded from both endpoint Stock Positions' ATP | In-Transit Stock, Stock Transfer, Stock Position |
| LDM-09 | Physical Inventory Count imposes freeze on all Inventory Location movements | Physical Inventory Count, Inventory Location |
| LDM-10 | Every Stock Position mutation produces Inventory Movement Record | Stock Position, Inventory Movement Record |

---

## Bounded Context Data Ownership

| Bounded Context | Owning Entities | Consuming Contexts (read by identity) |
|-----------------|-----------------|--------------------------------------|
| Catalog & Network | Product, Inventory Location, Storage Position, Supplier, Governance Policy, Reason Code | All operational contexts |
| Inventory Balance | Stock Position, Lot/Batch, Quarantine Hold, Stock Policy | Fulfillment, Inbound, Transfer, Accuracy, Returns, Commercial |
| Procurement & Inbound | Purchase Requisition, Purchase Order, Expected Inbound Delivery, Goods Receipt, Receipt Discrepancy, Put-Away, Supplier Invoice | Inventory Balance, Financial |
| Order Fulfillment | Customer Order, Inventory Reservation, Fulfillment Execution, Backorder, Shipment | Inventory Balance, Returns |
| Network Transfer | Transfer Request, Stock Transfer, In-Transit Stock | Inventory Balance |
| Inventory Accuracy | Cycle Count, Physical Inventory Count, Count Variance, Stock Adjustment, Inventory Write-Off | Inventory Balance, Catalog & Network |
| Returns | Return Authorization, Customer Return, Return Disposition | Order Fulfillment, Inventory Balance, Inventory Accuracy |
| Commercial | Promotional Stock Allocation | Inventory Balance, Order Fulfillment |
| Identity & Access | User Account, Role Assignment | All contexts |
| Intelligence & Reporting | Inventory Movement Record, Audit Trail Record, Operational Alert, Inventory Valuation Snapshot | All contexts (derived) |

---

## Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Senior Database Architect | | | |
| DDD Solution Architect | | | |
| Solution Architect | | | |
| Inventory Controller | | | |
| Product Owner | | | |

---

*End of Logical Data Model*

*Document ID: SRS-DB-001 | Version 1.0 | July 6, 2026*
