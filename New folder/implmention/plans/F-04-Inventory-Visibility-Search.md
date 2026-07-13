# Implementation Plan — F-04: Inventory Visibility & Search

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-04 |
| **Feature Name** | Inventory Visibility & Search |
| **Document Type** | Technical Lead Implementation Plan |
| **Module** | M-04 Inventory Balance + M-13 Intelligence (read) |
| **Required previous features** | `F-01`, `F-02`, `F-27` |
| **Stack** | Java 21, Spring Boot 3.x / Modulith, JPA, Flyway, PostgreSQL 16, Angular 19 |

---

## 1. Feature Overview

Real-time on-hand, reserved, ATP, stock status, and multi-criteria search across authorized locations.


**Stack:** Java 21 · Spring Boot 3.x · Spring Modulith · Spring Data JPA · MapStruct · PostgreSQL 16 · Flyway · Angular 19 · Signals/Facades · RFC 7807 errors


---

## 2. Business Goal

Provide a trusted single source of truth for stock questions without spreadsheets (BO-01, BO-16).

---

## 3. User Stories

- US-023
- US-024
- US-025
- US-026
- US-027
- US-028

Primary story references: **US-023, US-024, US-025, US-026, US-027, US-028** (see `project_businsse/user-stories-reviewed.md`).

---

## 4. Acceptance Criteria

Trace to reviewed AC document (`acceptance-criteria-reviewed.md`):

- AC-023–027 MVP visibility
- AC-028 network/inbound views Phase 2

**DoD extras (all features):** unit tests for domain invariants; API contract tests; UI happy-path + validation; RBAC checks; audit/movement side-effects verified where applicable.

---

## 5. Database Tasks

### Tables

| Object | Purpose |
|--------|---------|
| `inventory.stock_positions` | On-hand/reserved/ATP authoritative |
| `inventory.lot_batches` | Lot breakdown |
| `inventory.quarantine_holds` | Excluded from ATP |
| `inventory.stock_policies` | Status derivation |

### Relationships

- stock_positions unique (location_code, sku)
- lots/holds compose under stock_position

### Constraints

- chk on_hand/reserved/quarantine >= 0
- ATP invariant enforced in domain (on_hand - reserved - hold)

### Migration Tasks (Flyway)

- V1_30__inventory_stock_positions.sql
- V1_31__lot_batches_quarantine.sql
- Indexes on (location_code, sku), status

**Also:** grant app role DML only; enable optimistic locking `version` on transactional headers; UTC timestamps.

---

## 6. Backend Tasks

### Entities
- StockPosition (AR)
- LotBatch
- QuarantineHold

### Value Objects
- StockAvailabilityBreakdown
- StockStatusIndicator
- Quantity
- OwnershipClassification

### Repositories
- StockPositionRepository
- StockPositionQueryRepository

### DTOs (application/API layer)
**Request:** `StockPositionSearchQuery`, `AvailabilityQuery`  
**Response:** `StockPositionResponse`, `AvailabilityResponse`, `NetworkAvailabilityResponse`, `StockStatusResponse`, `StockStatusBoardResponse`

### Validation
- sku/location exist
- page size limits

Use Bean Validation + domain validators; map VR/BR codes into RFC 7807 `validationRuleId` / `businessRuleId`.

### Services
- InventoryVisibilityQueryService
- AtpCalculationService (read)

### Controllers
- StockPositionController
- AvailabilityController
- IntelligenceStockStatusController

### Exception Handling
- StockPositionNotFoundException
- UnauthorizedLocationAccessException

Global `@ControllerAdvice` maps to Problem Details.

### Security
- ['INVENTORY_VIEW', 'location-scope filter mandatory']

Evaluate permissions via API-148 and location scope via API-149 on every command/query.

---

## 7. Frontend Tasks

### Routes
- inventory/status-monitor
- inventory/availability
- home/operations (widgets)

Lazy-loaded under authenticated `AppShell`; add child routes (`:id`, `new`) as listed (gap: child routes currently missing).

### Pages
- InventoryStatusMonitorPage (UI-020)
- AvailabilityInquiryPage (UI-021)
- OperationalDashboardPage widgets

### Components
- StockStatusBoard
- AtpBadge
- LocationSkuFilter
- StockPositionTable

Prefer shared UI kit (`data-table`, banners, form controls) with CVA inputs.

### Models
- StockPositionVm
- AvailabilityVm
- StockStatus

### Services
- InventoryApiService
- InventoryVisibilityFacade

Pattern: `*ApiService` (HttpClient) → `*Facade` (signals / ComponentStore) → Page.

### Forms
- AvailabilitySearchForm
- StatusFilterForm

### Validation
- sku required for inquiry

Mirror server VR messages; show field errors from `ProblemDetailResponse.errors[]`.

### State Management
- ['filters, results, selected position signals']

Session/permissions remain in `core`; feature state stays local to facade.

---

## 8. API Contract

### Endpoints
- API-033/034 stock-positions
- API-035/036 availability
- API-037 stock-status
- API-012 locations
- API-151/152/153 intelligence

Full field specs: `SRS/API_Design/Request-DTOs.md`, `Response-DTOs.md`.

### Request DTOs
- StockPositionSearchQuery
- AvailabilityQuery

### Response DTOs
- StockPositionResponse
- AvailabilityResponse
- NetworkAvailabilityResponse
- StockStatusResponse
- StockStatusBoardResponse

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
- ATP matches on_hand-reserved-hold
- location scope hides other sites

### API Tests
- API-033–037, 151–153

### UI Tests
- UI-020/021 search/filter/drill

---

## 10. Dependencies

### Required features
`F-01`, `F-02`, `F-27`

### Downstream (consumers)
See `implmention/IMS-Feature-Dependency-Map.md` for dependents of `F-04`.

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

*Generated for Technical Lead delivery planning — F-04*
