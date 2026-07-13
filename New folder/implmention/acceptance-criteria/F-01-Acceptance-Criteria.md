# Acceptance Criteria — F-01: Product Catalog Management

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-01 |
| **Feature Name** | Product Catalog Management |
| **Document Type** | Feature Acceptance Criteria (PO + QA Lead) |
| **Related user stories** | US-001, US-002, US-003, US-004 |
| **Primary roles** | Inventory Controller, Warehouse Staff (lookup) |
| **Format** | Given / When / Then |
| **Criteria count** | 22 (H5 / V5 / E4 / P4 / X4) |

---

## Purpose

Define testable acceptance criteria for **F-01** covering happy paths, validation, errors, permissions, and edge cases. Use for UAT, QA test design, and Definition of Done.

**ID legend:** `FAC-{nn}-{H|V|E|P|X}{n}` — Feature Acceptance Criteria; H=Happy, V=Validation, E=Error, P=Permission, X=Edge.

---

### 1. Happy Scenarios

#### FAC-01-H1
- **Given** I am an authorized Inventory Controller and all required attributes (SKU, name, UoM, category) are provided
- **When** I create a new product with a unique SKU
- **Then** the product is saved as ACTIVE and visible to authorized users across locations

#### FAC-01-H2
- **Given** an existing ACTIVE product exists
- **When** I update name, description, category, or UoM
- **Then** changes are saved and reflected in all operational views for that SKU

#### FAC-01-H3
- **Given** an ACTIVE product exists
- **When** I change lifecycle status to INACTIVE or DISCONTINUED with confirmation
- **Then** the new status is stored with prior status, user, and timestamp, and eligibility rules apply

#### FAC-01-H4
- **Given** a product has SKU and barcode identifiers
- **When** I search or scan by any assigned identifier during receiving, counting, or picking
- **Then** the same product record is returned with core attributes

#### FAC-01-H5
- **Given** a potential duplicate is detected on create
- **When** I confirm merge into the existing product
- **Then** stock and history remain on a single product identity

### 2. Validation Scenarios

#### FAC-01-V1
- **Given** I omit SKU, name, or UoM
- **When** I attempt to save
- **Then** save is blocked and missing required fields are indicated

#### FAC-01-V2
- **Given** I enter a SKU that already exists
- **When** I attempt to create a new product
- **Then** duplicate SKU creation is blocked and the existing record is referenced

#### FAC-01-V3
- **Given** SKU format is invalid
- **When** I attempt to save
- **Then** validation fails with field-level VAL_* errors

#### FAC-01-V4
- **Given** I submit a name/barcode similar to an existing product
- **When** I attempt to save
- **Then** the system flags a potential duplicate and requires review before proceeding

#### FAC-01-V5
- **Given** I change status to DISCONTINUED
- **When** open POs or reservations exist
- **Then** the system warns of dependent activity before allowing the change

### 3. Error Scenarios

#### FAC-01-E1
- **Given** the persistence layer fails mid-save
- **When** I attempt to create or update a product
- **Then** no partial product is published and I receive a clear recoverable error

#### FAC-01-E2
- **Given** I search with an unknown identifier
- **When** I scan or search
- **Then** no match is returned and no product is auto-created

#### FAC-01-E3
- **Given** two products both have on-hand stock
- **When** I attempt an unauthorized merge
- **Then** merge is blocked until authorized Inventory Controller approval

#### FAC-01-E4
- **Given** duplicate detection is inconclusive
- **When** I cancel the create action
- **Then** no duplicate or partial record is saved

### 4. Permission Scenarios

#### FAC-01-P1
- **Given** I am a user without PRODUCT_MANAGE
- **When** I attempt to create or edit a product
- **Then** the action is denied with AUTH_* / 403 and no data changes

#### FAC-01-P2
- **Given** I am Warehouse Staff with PRODUCT_VIEW only
- **When** I look up a product by barcode
- **Then** I can view product identity but cannot edit master data

#### FAC-01-P3
- **Given** I lack authority to discontinue products
- **When** I attempt to set DISCONTINUED
- **Then** the action is denied

#### FAC-01-P4
- **Given** my location scope is restricted
- **When** I look up a product
- **Then** stock context shown reflects only authorized locations

### 5. Edge Cases

#### FAC-01-X1
- **Given** a product has existing stock or open orders
- **When** I update non-identity attributes
- **Then** historical transactions remain linked to the same SKU

#### FAC-01-X2
- **Given** a new product has no stock policy yet
- **When** I create the product
- **Then** it is receivable and visible but excluded from threshold alerts until thresholds exist

#### FAC-01-X3
- **Given** a discontinued product has zero on-hand and no open activity
- **When** I search active catalogs
- **Then** it is excluded by default but remains searchable for history

#### FAC-01-X4
- **Given** the same barcode was assigned to two SKUs
- **When** duplicate detection runs
- **Then** I can reassign the barcode without losing movement history


## Traceability

| Link | Reference |
|------|-----------|
| User stories | US-001, US-002, US-003, US-004 |
| Story-level AC | `project_businsse/acceptance-criteria-reviewed.md` |
| Implementation plan | `implmention/plans/F-01-*.md` |
| Feature catalog | `implmention/IMS-Implementation-Features.md` |

## Feature DoD (QA gate)

- [ ] All Happy criteria passed in UAT or automated suite
- [ ] Validation + Error criteria covered by API and/or UI tests
- [ ] Permission criteria verified with at least two roles (allowed + denied)
- [ ] Edge cases reviewed; deferred edges explicitly waived with PO sign-off
- [ ] No open Sev-1/Sev-2 defects for this feature

---

*Product Owner & QA Lead — F-01*
