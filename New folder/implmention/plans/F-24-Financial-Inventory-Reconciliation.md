# Implementation Plan — F-24: Financial Inventory Reconciliation

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-24 |
| **Feature Name** | Financial Inventory Reconciliation |
| **Document Type** | Technical Lead Implementation Plan |
| **Module** | M-06 finance slice + M-13 valuation |
| **Required previous features** | `F-05`, `F-07`, `F-17`, `F-29` |
| **Stack** | Java 21, Spring Boot 3.x / Modulith, JPA, Flyway, PostgreSQL 16, Angular 19 |

---

## 1. Feature Overview

Valuation snapshots, three-way match support, consignment ownership, and period-end reconciliation.


**Stack:** Java 21 · Spring Boot 3.x · Spring Modulith · Spring Data JPA · MapStruct · PostgreSQL 16 · Flyway · Angular 19 · Signals/Facades · RFC 7807 errors


---

## 2. Business Goal

Align operational inventory with finance needs (BO-07, BO-20).

---

## 3. User Stories

- US-075
- US-089

Primary story references: **US-075, US-089** (see `project_businsse/user-stories-reviewed.md`).

---

## 4. Acceptance Criteria

Trace to reviewed AC document (`acceptance-criteria-reviewed.md`):

- AC-075 valuation
- AC-089 reconciliation

**DoD extras (all features):** unit tests for domain invariants; API contract tests; UI happy-path + validation; RBAC checks; audit/movement side-effects verified where applicable.

---

## 5. Database Tasks

### Tables

| Object | Purpose |
|--------|---------|
| `finance.supplier_invoices (+ lines, match)` | 3-way match |
| `audit.inventory_valuation_snapshots / lines` | Valuation |

### Relationships

- invoice ↔ PO ↔ goods receipt match

### Constraints

- match status; payment auth after match

### Migration Tasks (Flyway)

- V3_20__finance_invoices.sql
- V3_21__valuation_snapshots.sql

**Also:** grant app role DML only; enable optimistic locking `version` on transactional headers; UTC timestamps.

---

## 6. Backend Tasks

### Entities
- SupplierInvoice (AR)
- ValuationSnapshot

### Value Objects
- MonetaryAmount
- MatchResult
- OwnershipClassification

### Repositories
- SupplierInvoiceRepository
- ValuationSnapshotRepository

### DTOs (application/API layer)
**Request:** `RegisterSupplierInvoiceRequest`, `ThreeWayMatchRequest`, `AuthorizePaymentRequest`, `ConsignmentOwnershipRequest`  
**Response:** `SupplierInvoiceResponse`, `ValuationSnapshotResponse`, `ReconciliationResponse`

### Validation
- PO+GR+invoice quantities
- currency

Use Bean Validation + domain validators; map VR/BR codes into RFC 7807 `validationRuleId` / `businessRuleId`.

### Services
- ThreeWayMatchService
- ValuationService
- ReconciliationService

### Controllers
- SupplierInvoiceController
- ValuationIntelligenceController

### Exception Handling
- ThreeWayMatchFailedException
- PaymentNotAuthorizedException

Global `@ControllerAdvice` maps to Problem Details.

### Security
- ['FINANCE_INVOICE', 'VALUATION_VIEW', 'RECONCILE']

Evaluate permissions via API-148 and location scope via API-149 on every command/query.

---

## 7. Frontend Tasks

### Routes
- reports/valuation-reconciliation

Lazy-loaded under authenticated `AppShell`; add child routes (`:id`, `new`) as listed (gap: child routes currently missing).

### Pages
- InventoryValuationReconciliationPage (UI-045)

### Components
- MatchPanel
- ValuationTable
- VarianceList

Prefer shared UI kit (`data-table`, banners, form controls) with CVA inputs.

### Models
- InvoiceVm
- ValuationVm
- ReconciliationVm

### Services
- FinanceApiService
- ValuationFacade

Pattern: `*ApiService` (HttpClient) → `*Facade` (signals / ComponentStore) → Page.

### Forms
- InvoiceForm
- ReconciliationSignoffForm

### Validation
- invoice totals

Mirror server VR messages; show field errors from `ProblemDetailResponse.errors[]`.

### State Management
- ['period, match results']

Session/permissions remain in `core`; feature state stays local to facade.

---

## 8. API Contract

### Endpoints
- API-077–080
- API-047
- API-171–172

Full field specs: `SRS/API_Design/Request-DTOs.md`, `Response-DTOs.md`.

### Request DTOs
- RegisterSupplierInvoiceRequest
- ThreeWayMatchRequest
- AuthorizePaymentRequest
- ConsignmentOwnershipRequest

### Response DTOs
- SupplierInvoiceResponse
- ValuationSnapshotResponse
- ReconciliationResponse

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
- match success/fail paths
- snapshot period close

### API Tests
- API-077–080, 171–172

### UI Tests
- UI-045

---

## 10. Dependencies

### Required features
`F-05`, `F-07`, `F-17`, `F-29`

### Downstream (consumers)
See `implmention/IMS-Feature-Dependency-Map.md` for dependents of `F-24`.

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

*Generated for Technical Lead delivery planning — F-24*
