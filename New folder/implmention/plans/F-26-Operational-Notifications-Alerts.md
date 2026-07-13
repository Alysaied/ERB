# Implementation Plan — F-26: Operational Notifications & Alerts

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-26 |
| **Feature Name** | Operational Notifications & Alerts |
| **Document Type** | Technical Lead Implementation Plan |
| **Module** | M-13 + producers |
| **Required previous features** | `F-27` |
| **Stack** | Java 21, Spring Boot 3.x / Modulith, JPA, Flyway, PostgreSQL 16, Angular 19 |

---

## 1. Feature Overview

Central notification center for stock, approval, transfer/fulfillment exceptions, inbound delays, and campaign alerts.


**Stack:** Java 21 · Spring Boot 3.x · Spring Modulith · Spring Data JPA · MapStruct · PostgreSQL 16 · Flyway · Angular 19 · Signals/Facades · RFC 7807 errors


---

## 2. Business Goal

Reduce decision latency by delivering actionable alerts to the right roles (BO-05, BO-06).

---

## 3. User Stories

- US-076
- US-077
- US-078
- US-079
- US-080

Primary story references: **US-076, US-077, US-078, US-079, US-080** (see `project_businsse/user-stories-reviewed.md`).

---

## 4. Acceptance Criteria

Trace to reviewed AC document (`acceptance-criteria-reviewed.md`):

- AC-076/077 MVP
- AC-078/079 P2
- AC-080 deferred

**DoD extras (all features):** unit tests for domain invariants; API contract tests; UI happy-path + validation; RBAC checks; audit/movement side-effects verified where applicable.

---

## 5. Database Tasks

### Tables

| Object | Purpose |
|--------|---------|
| `audit.operational_alerts` | Unified alert store |

### Relationships

- alert references entity ids by type

### Constraints

- acknowledge user/timestamp; unread counts

### Migration Tasks (Flyway)

- V1_80__operational_alerts.sql (shared with F-20)

**Also:** grant app role DML only; enable optimistic locking `version` on transactional headers; UTC timestamps.

---

## 6. Backend Tasks

### Entities
- OperationalAlert

### Value Objects
- AlertSeverity
- AlertChannel
- Acknowledgement

### Repositories
- OperationalAlertRepository

### DTOs (application/API layer)
**Request:** `AcknowledgeAlertRequest`, `AlertSearchQuery`  
**Response:** `AlertResponse`, `AlertCountResponse`

### Validation
- ack only owner/role

Use Bean Validation + domain validators; map VR/BR codes into RFC 7807 `validationRuleId` / `businessRuleId`.

### Services
- NotificationService
- AlertDeliveryService

### Controllers
- AlertController

### Exception Handling
- AlertNotFoundException
- AlertAckForbiddenException

Global `@ControllerAdvice` maps to Problem Details.

### Security
- ['ALERT_VIEW', 'role-filtered feed']

Evaluate permissions via API-148 and location scope via API-149 on every command/query.

---

## 7. Frontend Tasks

### Routes
- notifications

Lazy-loaded under authenticated `AppShell`; add child routes (`:id`, `new`) as listed (gap: child routes currently missing).

### Pages
- NotificationCenterPage (UI-004)

### Components
- NotificationIconInboxTrigger
- AlertList
- AckButton
- DeepLinkAction

Prefer shared UI kit (`data-table`, banners, form controls) with CVA inputs.

### Models
- AlertVm
- AlertCountVm

### Services
- NotificationApiService
- NotificationFacade (core)

Pattern: `*ApiService` (HttpClient) → `*Facade` (signals / ComponentStore) → Page.

### Forms
- AckForm

### Validation
- optional rationale

Mirror server VR messages; show field errors from `ProblemDetailResponse.errors[]`.

### State Management
- ['core unread count signal; notification list']

Session/permissions remain in `core`; feature state stays local to facade.

---

## 8. API Contract

### Endpoints
- API-158/159
- queues API-106/123/163/169

Full field specs: `SRS/API_Design/Request-DTOs.md`, `Response-DTOs.md`.

### Request DTOs
- AcknowledgeAlertRequest
- AlertSearchQuery

### Response DTOs
- AlertResponse
- AlertCountResponse

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
- role sees only relevant alerts
- ack clears unread

### API Tests
- API-158/159

### UI Tests
- UI-004 + header badge

---

## 10. Dependencies

### Required features
`F-27`

### Downstream (consumers)
See `implmention/IMS-Feature-Dependency-Map.md` for dependents of `F-26`.

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

*Generated for Technical Lead delivery planning — F-26*
