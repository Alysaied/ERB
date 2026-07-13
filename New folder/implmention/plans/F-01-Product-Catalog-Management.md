# Implementation Plan — F-01: Product Catalog Management

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-01 |
| **Feature Name** | Product Catalog Management |
| **Document Type** | Technical Lead Implementation Plan |
| **Module** | M-01 Product Catalog (`ims.catalog`) |
| **Required previous features** | `F-27` |
| **Stack** | Java 21, Spring Boot 3.x / Modulith, JPA, Flyway, PostgreSQL 16, Angular 19 |

---

## 1. Feature Overview

Create, update, search, and govern product master records (SKU identity, attributes, lifecycle, duplicate resolution) as the single product source of truth.


**Stack:** Java 21 · Spring Boot 3.x · Spring Modulith · Spring Data JPA · MapStruct · PostgreSQL 16 · Flyway · Angular 19 · Signals/Facades · RFC 7807 errors


---

## 2. Business Goal

Eliminate duplicate product identities and ensure every location references the same SKU, attributes, and lifecycle rules (BO-01, BO-21).

---

## 3. User Stories

- US-001
- US-002
- US-003
- US-004

Primary story references: **US-001, US-002, US-003, US-004** (see `project_businsse/user-stories-reviewed.md`).

---

## 4. Acceptance Criteria

Trace to reviewed AC document (`acceptance-criteria-reviewed.md`):

- AC-001-H1/H2, V1/V2, E1/E2, X1/X2 — create/update product master
- AC-002-* — lifecycle ACTIVE/INACTIVE/DISCONTINUED with audit of prior status
- AC-003-* — lookup by SKU/barcode with location-scoped stock context
- AC-004-* — duplicate detection, merge/reject with justification

**DoD extras (all features):** unit tests for domain invariants; API contract tests; UI happy-path + validation; RBAC checks; audit/movement side-effects verified where applicable.

---

## 5. Database Tasks

### Tables

| Object | Purpose |
|--------|---------|
| `catalog.products` | Product master; SKU unique; lifecycle; ABC; UoM; rotation |
| `catalog.product_identifiers` | Alternate IDs/barcodes → product |

### Relationships

- product_identifiers.product_id → products.id (FK, CASCADE delete restricted if history)
- Referenced by identity only from inventory, procurement, fulfillment (SKU)

### Constraints

- uk_products_sku; nn_products_sku/name/uom; chk_domain_lifecycle_status
- chk_domain_abc_classification (nullable until assigned); chk_domain_rotation_policy
- uk_product_identifiers (identifier_type, identifier_value)

### Migration Tasks (Flyway)

- V1_01__catalog_schema.sql — create schema catalog
- V1_02__catalog_products.sql — products + identifiers + indexes on sku, name, status
- V1_03__catalog_seed_categories_if_needed.sql (optional reference data)

**Also:** grant app role DML only; enable optimistic locking `version` on transactional headers; UTC timestamps.

---

## 6. Backend Tasks

### Entities
- Product (AR)
- ProductIdentifier (VO or child entity)

### Value Objects
- ProductSku
- ProductCategory
- ProductLifecycleStatus
- UnitOfMeasure
- AbcClassification
- RotationPolicy
- ShelfLifeProfile

### Repositories
- ProductRepository
- ProductIdentifierRepository (or embedded)

### DTOs (application/API layer)
**Request:** `CreateProductRequest`, `UpdateProductRequest`, `ChangeLifecycleStatusRequest`, `ResolveDuplicateRequest`, `ProductSearchQuery`  
**Response:** `ProductResponse`, `ProductSummaryResponse`, `PagedResponse<ProductSummaryResponse>`, `DuplicateResolutionResultResponse`, `EligibilityResponse`

### Validation
- VR-001/007 SKU pattern
- mandatory name/UoM
- duplicate SKU
- lifecycle transition rules BR-027

Use Bean Validation + domain validators; map VR/BR codes into RFC 7807 `validationRuleId` / `businessRuleId`.

### Services
- ProductCatalogService / ProductApplicationService
- DuplicateDetectionService

### Controllers
- ProductController — /api/v1/products

### Exception Handling
- DuplicateSkuException → 409
- ProductNotFoundException → 404
- InvalidLifecycleTransitionException → 422
- UnauthorizedProductMaintenanceException → 403

Global `@ControllerAdvice` maps to Problem Details.

### Security
- ['Permission: PRODUCT_MANAGE / PRODUCT_VIEW', 'location scope N/A for catalog; audit createdBy']

Evaluate permissions via API-148 and location scope via API-149 on every command/query.

---

## 7. Frontend Tasks

### Routes
- products/catalog (list)
- products/catalog/new
- products/catalog/:sku
- products/catalog/:sku/edit
- products/catalog/duplicates (optional)

Lazy-loaded under authenticated `AppShell`; add child routes (`:id`, `new`) as listed (gap: child routes currently missing).

### Pages
- ProductCatalogPage (UI-005)
- ProductDetailPage
- ProductFormPage
- DuplicateResolutionDialog

### Components
- ProductSearchBar
- ProductForm
- LifecycleStatusBadge
- IdentifierEditor
- DuplicateComparePanel

Prefer shared UI kit (`data-table`, banners, form controls) with CVA inputs.

### Models
- ProductVm
- ProductIdentifierVm
- LifecycleStatus

### Services
- ProductApiService
- ProductFacade

Pattern: `*ApiService` (HttpClient) → `*Facade` (signals / ComponentStore) → Page.

### Forms
- ProductCreateForm
- ProductEditForm
- LifecycleChangeForm

### Validation
- required sku/name/uom
- sku pattern
- async duplicate check

Mirror server VR messages; show field errors from `ProblemDetailResponse.errors[]`.

### State Management
- ['ProductFacade signals: list, filters, selectedSku, saveState']

Session/permissions remain in `core`; feature state stays local to facade.

---

## 8. API Contract

### Endpoints
- API-001 POST /api/v1/products
- API-002 GET /api/v1/products
- API-003 GET /api/v1/products/{sku}
- API-004 PATCH /api/v1/products/{sku}
- API-005 POST /api/v1/products/{sku}/lifecycle-status
- API-007 GET /api/v1/products/{sku}/eligibility
- API-008 GET /api/v1/products/categories/{categoryCode}/products
- API-009 POST /api/v1/products/duplicate-resolutions

Full field specs: `SRS/API_Design/Request-DTOs.md`, `Response-DTOs.md`.

### Request DTOs
- CreateProductRequest
- UpdateProductRequest
- ChangeLifecycleStatusRequest
- ResolveDuplicateRequest
- ProductSearchQuery

### Response DTOs
- ProductResponse
- ProductSummaryResponse
- PagedResponse<ProductSummaryResponse>
- DuplicateResolutionResultResponse
- EligibilityResponse

### Error Responses

| HTTP | Category | Typical `errorCode` prefix |
|------|----------|---------------------------|
| 400 | validation-error | `VAL_*` |
| 401 | authentication-error | `AUTH_*` |
| 403 | authorization-error | `AUTHZ_*` |
| 404 | not-found | `NOT_FOUND_*` |
| 409 | conflict | `CONFLICT_*` |
| 422 | business-rule-violation | `BIZ_*` / `BR-*` |
| 500 | internal-server-error | `SYS_*` |

Envelope: RFC 7807 `ProblemDetailResponse` (`type`, `title`, `status`, `detail`, `instance`, `errorCode`, `traceId`, `timestamp`, optional `errors[]`).


---

## 9. QA Tasks

### Functional Tests
- Create/update/search product UAT per AC-001–004
- Lifecycle blocks reservation when discontinued

### API Tests
- Contract tests for API-001–009
- 400/403/409/422 cases

### UI Tests
- UI-005 CRUD happy path
- duplicate banner
- permission denied

---

## 10. Dependencies

### Required features
`F-27`

### Downstream (consumers)
See `implmention/IMS-Feature-Dependency-Map.md` for dependents of `F-01`.

### Implementation sequence hint
Follow IMPL-DEP-001 optimal order; do not start UI polish before HTTP facade + auth for this module.

---

## 11. Definition of Done (Feature)

- [ ] Flyway migrations applied in CI
- [ ] Domain invariants covered by unit tests
- [ ] All listed APIs implemented + OpenAPI updated
- [ ] Angular routes/pages/facades wired (no mock-only)
- [ ] RBAC + location scope verified
- [ ] AC happy/validation/error/edge sampled in UAT pack
- [ ] Audit/movement side-effects verified (if mutating)
- [ ] Feature flagged or released per wave plan

---

*Generated for Technical Lead delivery planning — F-01*
