# Implementation Plan — F-03: Stock Policy & Product Classification

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-03 |
| **Feature Name** | Stock Policy & Product Classification |
| **Document Type** | Technical Lead Implementation Plan |
| **Module** | M-03 Inventory Governance + M-04 Stock Policy |
| **Required previous features** | `F-01`, `F-02`, `F-27` |
| **Stack** | Java 21, Spring Boot 3.x / Modulith, JPA, Flyway, PostgreSQL 16, Angular 19 |

---

## 1. Feature Overview

Define per product-location stock thresholds, ABC class, governance policies, reason codes, approval thresholds, and receipt tolerances.


**Stack:** Java 21 · Spring Boot 3.x · Spring Modulith · Spring Data JPA · MapStruct · PostgreSQL 16 · Flyway · Angular 19 · Signals/Facades · RFC 7807 errors


---

## 2. Business Goal

Drive proactive replenishment, differentiated counting, and consistent exception governance (BO-05).

---

## 3. User Stories

- US-008
- US-009
- US-012
- US-056

Primary story references: **US-008, US-009, US-012, US-056** (see `project_businsse/user-stories-reviewed.md`).

---

## 4. Acceptance Criteria

Trace to reviewed AC document (`acceptance-criteria-reviewed.md`):

- AC-008-* thresholds
- AC-009-* ABC (P2)
- AC-012-* governance policies (P2)
- AC-056-* safety stock protection

**DoD extras (all features):** unit tests for domain invariants; API contract tests; UI happy-path + validation; RBAC checks; audit/movement side-effects verified where applicable.

---

## 5. Database Tasks

### Tables

| Object | Purpose |
|--------|---------|
| `inventory.stock_policies` | Reorder/min/safety per location+sku |
| `inventory.stock_policy_history` | Immutable threshold history |
| `governance.governance_policies` | Policy versions |
| `governance.reason_codes` | Standardized reason taxonomy |

### Relationships

- stock_policies references ProductSku + LocationCode (logical FKs)
- reason_codes owned by governance_policies / independent with retire

### Constraints

- uk_stock_policies (location_code, sku)
- chk quantities >= 0; min <= reorder unless authorized invert
- uk_reason_codes_code; retired codes not selectable

### Migration Tasks (Flyway)

- V1_20__governance_schema.sql
- V1_21__reason_codes_policies.sql
- V1_22__stock_policies.sql

**Also:** grant app role DML only; enable optimistic locking `version` on transactional headers; UTC timestamps.

---

## 6. Backend Tasks

### Entities
- StockPolicy (AR)
- GovernancePolicy (AR)
- ReasonCode

### Value Objects
- StockThresholdSet
- ApprovalThreshold
- QuantityTolerance
- EffectivePeriod
- AbcClass

### Repositories
- StockPolicyRepository
- GovernancePolicyRepository
- ReasonCodeRepository

### DTOs (application/API layer)
**Request:** `CreateStockPolicyRequest`, `UpdateStockPolicyRequest`, `AssignAbcRequest`, `CreateReasonCodeRequest`, `UpdateApprovalThresholdsRequest`, `UpdateReceiptTolerancesRequest`  
**Response:** `StockPolicyResponse`, `ReasonCodeResponse`, `GovernancePolicyResponse`, `ApprovalThresholdResponse`, `ReceiptToleranceResponse`

### Validation
- VR thresholds
- VR-021 ABC
- VR-026/027 reason codes
- effective dating non-overlap

Use Bean Validation + domain validators; map VR/BR codes into RFC 7807 `validationRuleId` / `businessRuleId`.

### Services
- StockPolicyService
- GovernanceService
- SafetyStockProtectionService

### Controllers
- StockPolicyController
- GovernanceController
- ProductAbc endpoint on ProductController

### Exception Handling
- PolicyNotFoundException
- ReasonCodeRetiredException
- InvalidThresholdException
- SafetyStockBypassRejectedException

Global `@ControllerAdvice` maps to Problem Details.

### Security
- ['POLICY_MANAGE', 'GOVERNANCE_MANAGE', 'ABC_ASSIGN']

Evaluate permissions via API-148 and location scope via API-149 on every command/query.

---

## 7. Frontend Tasks

### Routes
- products/stock-policies
- products/abc-classification
- governance/policies

Lazy-loaded under authenticated `AppShell`; add child routes (`:id`, `new`) as listed (gap: child routes currently missing).

### Pages
- StockPolicyPage (UI-008)
- AbcClassificationPage (UI-009)
- GovernancePoliciesPage (UI-010)

### Components
- ThresholdForm
- ReasonCodeTable
- ToleranceEditor
- AbcAssignGrid

Prefer shared UI kit (`data-table`, banners, form controls) with CVA inputs.

### Models
- StockPolicyVm
- ReasonCodeVm
- GovernancePolicyVm

### Services
- StockPolicyApiService
- GovernanceApiService
- PolicyFacade

Pattern: `*ApiService` (HttpClient) → `*Facade` (signals / ComponentStore) → Page.

### Forms
- StockPolicyForm
- ReasonCodeForm
- ThresholdForm

### Validation
- min/reorder/safety numeric rules
- effective date required

Mirror server VR messages; show field errors from `ProblemDetailResponse.errors[]`.

### State Management
- ['PolicyFacade: selected location/sku, policy draft']

Session/permissions remain in `core`; feature state stays local to facade.

---

## 8. API Contract

### Endpoints
- API-038/039/040 stock-policies
- API-006 ABC classification
- API-022–030 governance reason codes, policies, thresholds, tolerances

Full field specs: `SRS/API_Design/Request-DTOs.md`, `Response-DTOs.md`.

### Request DTOs
- CreateStockPolicyRequest
- UpdateStockPolicyRequest
- AssignAbcRequest
- CreateReasonCodeRequest
- UpdateApprovalThresholdsRequest
- UpdateReceiptTolerancesRequest

### Response DTOs
- StockPolicyResponse
- ReasonCodeResponse
- GovernancePolicyResponse
- ApprovalThresholdResponse
- ReceiptToleranceResponse

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
- Set thresholds → status/alerts consume
- retire reason code blocks new use

### API Tests
- API-006, 022–030, 038–040

### UI Tests
- UI-008/009/010 forms + list

---

## 10. Dependencies

### Required features
`F-01`, `F-02`, `F-27`

### Downstream (consumers)
See `implmention/IMS-Feature-Dependency-Map.md` for dependents of `F-03`.

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

*Generated for Technical Lead delivery planning — F-03*
