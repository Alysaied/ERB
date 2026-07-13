# Implementation Plan — F-02: Location & Network Setup

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-02 |
| **Feature Name** | Location & Network Setup |
| **Document Type** | Technical Lead Implementation Plan |
| **Module** | M-02 Warehouse Network (`ims.network`) |
| **Required previous features** | `F-27` |
| **Stack** | Java 21, Spring Boot 3.x / Modulith, JPA, Flyway, PostgreSQL 16, Angular 19 |

---

## 1. Feature Overview

Configure inventory locations, hierarchy, storage positions, and location operational lifecycle (activate/deactivate/close).


**Stack:** Java 21 · Spring Boot 3.x · Spring Modulith · Spring Data JPA · MapStruct · PostgreSQL 16 · Flyway · Angular 19 · Signals/Facades · RFC 7807 errors


---

## 2. Business Goal

Enable stock assignment, tracking, and reporting at the correct warehouses, stores, and DCs (BO-01).

---

## 3. User Stories

- US-005
- US-006
- US-007
- US-010

Primary story references: **US-005, US-006, US-007, US-010** (see `project_businsse/user-stories-reviewed.md`).

---

## 4. Acceptance Criteria

Trace to reviewed AC document (`acceptance-criteria-reviewed.md`):

- AC-005-* location CRUD
- AC-006-* hierarchy
- AC-007-* closure disposition (P2)
- AC-010-* opening balance gate before operational

**DoD extras (all features):** unit tests for domain invariants; API contract tests; UI happy-path + validation; RBAC checks; audit/movement side-effects verified where applicable.

---

## 5. Database Tasks

### Tables

| Object | Purpose |
|--------|---------|
| `network.inventory_locations` | Location master + hierarchy + freeze/operational status |
| `network.storage_positions` | Zone/aisle/bin under location |

### Relationships

- storage_positions.location_id → inventory_locations.id
- inventory_locations.parent_location_id → inventory_locations.id (self-FK)

### Constraints

- uk_inventory_locations_location_code; no self-parent cycle (app + CHECK)
- nn location name/type/status; chk operational status enums

### Migration Tasks (Flyway)

- V1_10__network_schema.sql
- V1_11__inventory_locations.sql
- V1_12__storage_positions.sql

**Also:** grant app role DML only; enable optimistic locking `version` on transactional headers; UTC timestamps.

---

## 6. Backend Tasks

### Entities
- InventoryLocation (AR)
- StoragePosition

### Value Objects
- LocationCode
- LocationType
- LocationHierarchyPath
- PhysicalAddress
- EffectivePeriod

### Repositories
- InventoryLocationRepository
- StoragePositionRepository

### DTOs (application/API layer)
**Request:** `CreateLocationRequest`, `UpdateHierarchyRequest`, `CreateStoragePositionRequest`, `ActivateLocationRequest`, `CloseLocationRequest`  
**Response:** `LocationResponse`, `LocationSummaryResponse`, `StoragePositionResponse`, `FreezeStatusResponse`, `OperationalStatusResponse`

### Validation
- VR-011 LocationCode
- hierarchy acyclic
- close blocked if stock remains unless disposition

Use Bean Validation + domain validators; map VR/BR codes into RFC 7807 `validationRuleId` / `businessRuleId`.

### Services
- WarehouseNetworkService
- LocationLifecycleService

### Controllers
- LocationController — /api/v1/locations

### Exception Handling
- LocationNotFoundException
- InvalidHierarchyException
- LocationCloseBlockedException
- LocationFrozenException

Global `@ControllerAdvice` maps to Problem Details.

### Security
- ['LOCATION_MANAGE / LOCATION_VIEW', 'Ops Director for hierarchy/closure']

Evaluate permissions via API-148 and location scope via API-149 on every command/query.

---

## 7. Frontend Tasks

### Routes
- locations
- locations/new
- locations/:locationCode
- locations/:locationCode/storage

Lazy-loaded under authenticated `AppShell`; add child routes (`:id`, `new`) as listed (gap: child routes currently missing).

### Pages
- LocationWarehouseManagementPage (UI-007)
- LocationDetailPage
- StoragePositionEditor

### Components
- LocationForm
- HierarchyTree
- StoragePositionGrid
- OperationalStatusChip

Prefer shared UI kit (`data-table`, banners, form controls) with CVA inputs.

### Models
- LocationVm
- StoragePositionVm

### Services
- LocationApiService
- LocationFacade

Pattern: `*ApiService` (HttpClient) → `*Facade` (signals / ComponentStore) → Page.

### Forms
- LocationForm
- StoragePositionForm
- ActivateLocationForm

### Validation
- required code/name/type
- parent != self

Mirror server VR messages; show field errors from `ProblemDetailResponse.errors[]`.

### State Management
- ['LocationFacade: tree, selected location, positions']

Session/permissions remain in `core`; feature state stays local to facade.

---

## 8. API Contract

### Endpoints
- API-011 POST /api/v1/locations
- API-012 GET /api/v1/locations
- API-013 GET /api/v1/locations/{locationCode}
- API-014 PATCH .../hierarchy
- API-015/016 storage-positions
- API-017/018/019 activate/deactivate/close
- API-020 freeze-status
- API-021 operational-status

Full field specs: `SRS/API_Design/Request-DTOs.md`, `Response-DTOs.md`.

### Request DTOs
- CreateLocationRequest
- UpdateHierarchyRequest
- CreateStoragePositionRequest
- ActivateLocationRequest
- CloseLocationRequest

### Response DTOs
- LocationResponse
- LocationSummaryResponse
- StoragePositionResponse
- FreezeStatusResponse
- OperationalStatusResponse

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
- Create location + storage bins
- hierarchy rollup
- activation requires opening balance policy

### API Tests
- API-011–021 contract + freeze status

### UI Tests
- UI-007 create/edit/list
- storage position add

---

## 10. Dependencies

### Required features
`F-27`

### Downstream (consumers)
See `implmention/IMS-Feature-Dependency-Map.md` for dependents of `F-02`.

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

*Generated for Technical Lead delivery planning — F-02*
