# Implementation Plan — F-27: User Access & Role Management

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-27 |
| **Feature Name** | User Access & Role Management |
| **Document Type** | Technical Lead Implementation Plan |
| **Module** | M-12 Identity & Access + Platform auth |
| **Required previous features** | _None (foundation)_ |
| **Stack** | Java 21, Spring Boot 3.x / Modulith, JPA, Flyway, PostgreSQL 16, Angular 19 |

---

## 1. Feature Overview

Authenticate sessions, provision users, assign roles, and enforce location-scoped RBAC.


**Stack:** Java 21 · Spring Boot 3.x · Spring Modulith · Spring Data JPA · MapStruct · PostgreSQL 16 · Flyway · Angular 19 · Signals/Facades · RFC 7807 errors


---

## 2. Business Goal

Control who can view/transact/approve inventory operations (BO-19, BO-21).

---

## 3. User Stories

- US-081
- US-082
- US-085

Primary story references: **US-081, US-082, US-085** (see `project_businsse/user-stories-reviewed.md`).

---

## 4. Acceptance Criteria

Trace to reviewed AC document (`acceptance-criteria-reviewed.md`):

- AC-081 RBAC
- AC-082 location scope
- AC-085 user provisioning

**DoD extras (all features):** unit tests for domain invariants; API contract tests; UI happy-path + validation; RBAC checks; audit/movement side-effects verified where applicable.

---

## 5. Database Tasks

### Tables

| Object | Purpose |
|--------|---------|
| `identity.user_accounts` | Users |
| `identity.role_assignments` | Roles |
| `identity.role_assignment_locations` | Location scope |

### Relationships

- role_assignments → user; locations → assignment

### Constraints

- uk username/email; soft suspend/deactivate

### Migration Tasks (Flyway)

- V1_00__identity_schema.sql
- V1_01__user_accounts_roles.sql

**Also:** grant app role DML only; enable optimistic locking `version` on transactional headers; UTC timestamps.

---

## 6. Backend Tasks

### Entities
- UserAccount (AR)
- RoleAssignment

### Value Objects
- UserId
- RoleCode
- LocationScope

### Repositories
- UserAccountRepository
- RoleAssignmentRepository

### DTOs (application/API layer)
**Request:** `CreateUserRequest`, `AssignRoleRequest`, `SuspendUserRequest`, `DeactivateUserRequest`, `SyncUsersRequest`  
**Response:** `UserResponse`, `SessionResponse`, `RoleAssignmentResponse`, `CommandResultResponse`

### Validation
- unique username
- valid role codes UR-01–UR-19

Use Bean Validation + domain validators; map VR/BR codes into RFC 7807 `validationRuleId` / `businessRuleId`.

### Services
- UserAdminService
- SessionService
- AuthorizationService

### Controllers
- UserController
- AuthController
- AuthorizationController

### Exception Handling
- InvalidCredentialsException
- UserSuspendedException
- RoleAssignmentConflictException

Global `@ControllerAdvice` maps to Problem Details.

### Security
- ['OAuth2/OIDC JWT', 'ADMIN_USERS', 'public only login']

Evaluate permissions via API-148 and location scope via API-149 on every command/query.

---

## 7. Frontend Tasks

### Routes
- auth/sign-in
- admin/users
- admin/roles-access

Lazy-loaded under authenticated `AppShell`; add child routes (`:id`, `new`) as listed (gap: child routes currently missing).

### Pages
- SignInPage (UI-001)
- UserAccountManagementPage (UI-049)
- RoleAccessControlPage (UI-050)

### Components
- SignInForm
- UserTable
- RoleAssignmentMatrix
- LocationScopePicker
- SessionContextBadge

Prefer shared UI kit (`data-table`, banners, form controls) with CVA inputs.

### Models
- UserVm
- SessionVm
- PermissionVm

### Services
- AuthService
- UserApiService
- AuthorizationApiService
- SessionStore

Pattern: `*ApiService` (HttpClient) → `*Facade` (signals / ComponentStore) → Page.

### Forms
- SignInForm
- UserForm
- RoleAssignForm

### Validation
- credentials required
- role/location required on assign

Mirror server VR messages; show field errors from `ProblemDetailResponse.errors[]`.

### State Management
- ['core session signals, permission catalog, location scope']

Session/permissions remain in `core`; feature state stays local to facade.

---

## 8. API Contract

### Endpoints
- API-140–149
- API-173
- API-174

Full field specs: `SRS/API_Design/Request-DTOs.md`, `Response-DTOs.md`.

### Request DTOs
- CreateUserRequest
- AssignRoleRequest
- SuspendUserRequest
- DeactivateUserRequest
- SyncUsersRequest

### Response DTOs
- UserResponse
- SessionResponse
- RoleAssignmentResponse
- CommandResultResponse

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
- login/logout
- suspended blocked
- location scope filters data

### API Tests
- API-140–149, 173–174

### UI Tests
- UI-001/049/050
- authGuard/guestGuard

---

## 10. Dependencies

### Required features
_None (foundation)_

### Downstream (consumers)
See `implmention/IMS-Feature-Dependency-Map.md` for dependents of `F-27`.

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

*Generated for Technical Lead delivery planning — F-27*
