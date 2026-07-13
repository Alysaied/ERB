# Implementation Plan — F-14: Cycle Counting

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-14 |
| **Feature Name** | Cycle Counting |
| **Document Type** | Technical Lead Implementation Plan |
| **Module** | M-09 Inventory Accuracy |
| **Required previous features** | `F-01`, `F-02`, `F-04`, `F-27` |
| **Stack** | Java 21, Spring Boot 3.x / Modulith, JPA, Flyway, PostgreSQL 16, Angular 19 |

---

## 1. Feature Overview

Schedule, assign, and capture blind cycle counts; feed accuracy metrics.


**Stack:** Java 21 · Spring Boot 3.x · Spring Modulith · Spring Data JPA · MapStruct · PostgreSQL 16 · Flyway · Angular 19 · Signals/Facades · RFC 7807 errors


---

## 2. Business Goal

Sustain inventory accuracy without full-wall disruption (BO-02).

---

## 3. User Stories

- US-030
- US-031
- US-071

Primary story references: **US-030, US-031, US-071** (see `project_businsse/user-stories-reviewed.md`).

---

## 4. Acceptance Criteria

Trace to reviewed AC document (`acceptance-criteria-reviewed.md`):

- AC-030 schedule/assign
- AC-031 blind count
- AC-071 accuracy reporting

**DoD extras (all features):** unit tests for domain invariants; API contract tests; UI happy-path + validation; RBAC checks; audit/movement side-effects verified where applicable.

---

## 5. Database Tasks

### Tables

| Object | Purpose |
|--------|---------|
| `accuracy.cycle_counts` | Cycle count headers/results |

### Relationships

- count references location + sku; expected qty snapshotted

### Constraints

- blind: system qty hidden from counter UI
- counter != approver later

### Migration Tasks (Flyway)

- V1_70__cycle_counts.sql

**Also:** grant app role DML only; enable optimistic locking `version` on transactional headers; UTC timestamps.

---

## 6. Backend Tasks

### Entities
- CycleCount (AR)

### Value Objects
- CountQuantity
- BlindCountResult
- UserActionAttribution

### Repositories
- CycleCountRepository

### DTOs (application/API layer)
**Request:** `CreateCycleCountRequest`, `SubmitCycleCountResultRequest`, `CycleCountSearchQuery`  
**Response:** `CycleCountResponse`, `CountPerformanceResponse`

### Validation
- assigned user
- location not conflicting freeze optionally

Use Bean Validation + domain validators; map VR/BR codes into RFC 7807 `validationRuleId` / `businessRuleId`.

### Services
- CycleCountService

### Controllers
- CycleCountController

### Exception Handling
- CycleCountAlreadySubmittedException
- BlindCountViolationException

Global `@ControllerAdvice` maps to Problem Details.

### Security
- ['CYCLE_COUNT_MANAGE', 'CYCLE_COUNT_EXECUTE']

Evaluate permissions via API-148 and location scope via API-149 on every command/query.

---

## 7. Frontend Tasks

### Routes
- inventory/cycle-counts
- inventory/cycle-counts/:id

Lazy-loaded under authenticated `AppShell`; add child routes (`:id`, `new`) as listed (gap: child routes currently missing).

### Pages
- CycleCountWorkbenchPage (UI-023)

### Components
- CountAssignmentList
- BlindCountEntry
- CountSubmitConfirm

Prefer shared UI kit (`data-table`, banners, form controls) with CVA inputs.

### Models
- CycleCountVm

### Services
- CycleCountApiService
- CycleCountFacade

Pattern: `*ApiService` (HttpClient) → `*Facade` (signals / ComponentStore) → Page.

### Forms
- CountResultForm

### Validation
- qty >= 0
- no display of system qty

Mirror server VR messages; show field errors from `ProblemDetailResponse.errors[]`.

### State Management
- ['assigned counts, entry draft']

Session/permissions remain in `core`; feature state stays local to facade.

---

## 8. API Contract

### Endpoints
- API-108–111
- API-168

Full field specs: `SRS/API_Design/Request-DTOs.md`, `Response-DTOs.md`.

### Request DTOs
- CreateCycleCountRequest
- SubmitCycleCountResultRequest
- CycleCountSearchQuery

### Response DTOs
- CycleCountResponse
- CountPerformanceResponse

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
- blind enforced
- variance created when mismatch

### API Tests
- API-108–111

### UI Tests
- UI-023

---

## 10. Dependencies

### Required features
`F-01`, `F-02`, `F-04`, `F-27`

### Downstream (consumers)
See `implmention/IMS-Feature-Dependency-Map.md` for dependents of `F-14`.

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

*Generated for Technical Lead delivery planning — F-14*
