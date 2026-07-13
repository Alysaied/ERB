# Validation Coverage Report

**Project:** IMS Frontend vs. Approved Form Specifications  
**Specification Source:** `SRS/Inventory-Management-System-SRS.md` § Form Specifications (F-001–F-049)  
**UX Reference:** `SRS/UI Specification/UI Specification.md`, `IMS-Form-Specifications-and-Validation.md`  
**Implementation Source:** `ims-frontend/src/app/`  
**Report Date:** July 7, 2026

---

## Executive Summary

| Metric | Value |
|--------|-------|
| Forms in specification | **49** (F-001 – F-049) |
| Forms fully implemented | **0** |
| Forms partially implemented | **1** (F-001 Sign In) |
| Forms not implemented | **48** |
| Auxiliary search input (non-form) | **1** (Global Search Bar) |
| `ReactiveFormsModule` usage | **0** |
| `Validators` / custom validators | **0** |
| `ControlValueAccessor` on form controls | **0** |
| Shared `ValidationMessageBlock` wired | **0** |
| **Weighted validation coverage** | **~3%** |

### Implementation Reality

The Angular application contains **only one user-facing form**: the sign-in page (`UI-001`). All other screens display mock JSON and do not render editable forms. Twelve shared form components exist as scaffold files but are **not integrated** into any page and do not implement validation behavior.

---

## Shared Validation Specification (Applies to All Forms)

The approved spec defines global rules that **none** of the implemented code follows:

| Shared rule | Spec requirement | Frontend status |
|-------------|------------------|-----------------|
| Inline validation on blur | Required fields validate on blur and submit | Not implemented (HTML `required` only on sign-in) |
| Format validation on blur | SKU, email, codes validated after field exit | Not implemented |
| Cross-field validation | Revalidate when dependent fields change | Not implemented |
| No premature errors | Errors only after interaction or submit | Not enforced programmatically |
| Error correction | Clear errors when field corrected | Not implemented |
| Form-level error summary | `There is a problem with this form.` banner | Not implemented (sign-in uses custom message only) |
| API error mapping | `VAL_*`, `BIZ_*`, `CONF_*`, `AUTH_*` to inline/banner | Not implemented (no HTTP layer) |
| Preserve values on error | Keep user input on 409/422/500 | Partial on sign-in (email kept; password not cleared per spec) |
| Success banner | Concise outcome after submit | Not implemented on sign-in (redirect only) |
| `aria-describedby` / field errors | Programmatic label-error association | Not implemented |
| Loading state on submit | Disable inputs, show spinner | Not implemented on sign-in |

### Shared Field Patterns (Spec) — Implementation Status

| Pattern | Spec ID | Used in forms | Implemented |
|---------|---------|---------------|-------------|
| Product SKU | A | F-002, F-008, many line editors | No |
| Location Code | B | F-005, F-007, F-012+, filters | No |
| Quantity | C | F-012–F-041 line items | No |
| Reason Code | D | F-016, F-025, F-027, etc. | No |
| Date Range | E | F-021, F-042, F-045, F-046 | No |

---

## Master Validation Coverage Matrix

| Form ID | Form name | Screen(s) | Impl. status | Req. fields spec | Req. fields impl. | Validation impl. | Coverage |
|---------|-----------|-----------|--------------|------------------|-------------------|------------------|----------|
| F-001 | Sign In Form | UI-001 | **Partial** | 2 (+1 optional) | 2 / 3 | Minimal | **22%** |
| F-002 | Product Form | UI-005 | No | 4+ conditional | 0 | None | 0% |
| F-003 | Product Duplicate Resolution | UI-005 | No | 2+ conditional | 0 | None | 0% |
| F-004 | Bulk Product Import | UI-006 | No | 2 | 0 | None | 0% |
| F-005 | Location Form | UI-007 | No | 4+ conditional | 0 | None | 0% |
| F-006 | Storage Position Form | UI-007 | No | 2 | 0 | None | 0% |
| F-007 | Stock Policy Form | UI-008 | No | 6 | 0 | None | 0% |
| F-008 | ABC Classification Form | UI-009 | No | 2 | 0 | None | 0% |
| F-009 | Governance Policy Form | UI-010 | No | 2+ conditional | 0 | None | 0% |
| F-010 | Reason Code Form | UI-010 | No | 3+ conditional | 0 | None | 0% |
| F-011 | Supplier Form | UI-011 | No | 3+ conditional | 0 | None | 0% |
| F-012 | Purchase Requisition Form | UI-013, UI-037 | No | 3+ lines | 0 | None | 0% |
| F-013 | Purchase Order Form | UI-012 | No | 4+ lines | 0 | None | 0% |
| F-014 | Inbound Delivery Planning | UI-014 | No | 2+ conditional | 0 | None | 0% |
| F-015 | Goods Receipt / Verification | UI-015 | No | 3+ conditional lines | 0 | None | 0% |
| F-016 | Receipt Discrepancy | UI-016 | No | 5+ conditional | 0 | None | 0% |
| F-017 | Put-Away Form | UI-017 | No | 3 per line | 0 | None | 0% |
| F-018 | Ad-Hoc Inbound Receipt | UI-018 | No | 5+ lines | 0 | None | 0% |
| F-019 | Inventory Status Filter | UI-020 | No | 0–2 conditional | 0 | None | 0% |
| F-020 | Availability Inquiry | UI-021 | No | 1+ conditional | 0 | None | 0% |
| F-021 | Movement History Query | UI-022 | No | 2 | 0 | None | 0% |
| F-022 | Cycle Count Submission | UI-023 | No | 1 | 0 | None | 0% |
| F-023 | Physical Count Session | UI-024 | No | 3+ conditional | 0 | None | 0% |
| F-024 | Variance Investigation | UI-025 | No | 2+ conditional | 0 | None | 0% |
| F-025 | Stock Adjustment | UI-026 | No | 6+ conditional | 0 | None | 0% |
| F-026 | Write-Off Authorization | UI-027 | No | 1+ conditional | 0 | None | 0% |
| F-027 | Quarantine / Hold | UI-028 | No | 3+ conditional | 0 | None | 0% |
| F-028 | Order Creation / Import | UI-030 | No | 2+ lines | 0 | None | 0% |
| F-029 | Order Availability / Reservation | UI-030 | No | 1+ conditional | 0 | None | 0% |
| F-030 | Pick Verification | UI-031 | No | 2+ per line | 0 | None | 0% |
| F-031 | Pack Order | UI-031 | No | 2+ per package | 0 | None | 0% |
| F-032 | Shipment Confirmation | UI-031 | No | 2+ per line | 0 | None | 0% |
| F-033 | Partial Fulfillment / Backorder | UI-032 | No | 2+ conditional | 0 | None | 0% |
| F-034 | Fulfillment Exception | UI-033 | No | 2 | 0 | None | 0% |
| F-035 | Multi-Location Fulfillment Plan | UI-035 | No | 2 per allocation | 0 | None | 0% |
| F-036 | Alert Acknowledgment | UI-004, UI-036 | No | 1+ conditional | 0 | None | 0% |
| F-037 | Transfer Request | UI-038, UI-041 | No | 4+ lines | 0 | None | 0% |
| F-038 | Transfer Approval | UI-039 | No | 1+ conditional | 0 | None | 0% |
| F-039 | Transfer Dispatch / Receipt | UI-040 | No | 2+ conditional | 0 | None | 0% |
| F-040 | Return Authorization | UI-042 | No | 3+ lines | 0 | None | 0% |
| F-041 | Return Receipt / Inspection / Disposition | UI-043 | No | Multi-step conditional | 0 | None | 0% |
| F-042 | Report Filter | UI-044 | No | 1+ conditional | 0 | None | 0% |
| F-043 | Valuation Reconciliation | UI-045 | No | 1+ conditional | 0 | None | 0% |
| F-044 | Promotional Allocation / Readiness | UI-046 | No | 7+ conditional | 0 | None | 0% |
| F-045 | Audit Review Scope | UI-047 | No | 2+ conditional | 0 | None | 0% |
| F-046 | Audit Trail Query | UI-048 | No | 2 | 0 | None | 0% |
| F-047 | User Account | UI-049 | No | 4+ conditional | 0 | None | 0% |
| F-048 | Role and Access Control | UI-050 | No | 1+ conditional | 0 | None | 0% |
| F-049 | Session / Logout | Global menu | **Partial** | 0 required | 0 / 1 optional | None | **5%** |

---

## Detailed Analysis: Implemented Forms

### F-001 — Sign In Form

**Location:** `features/auth/sign-in-page/sign-in-page.page.{ts,html}`  
**Aligned APIs:** API-173, API-174

#### Required fields

| Field | Spec required | Implemented | Notes |
|-------|---------------|-------------|-------|
| Username / Email | Yes | Yes | `type="email"`, `[(ngModel)]="email"` |
| Password | Yes | Yes | `type="password"`, `[(ngModel)]="password"` |
| Remember Session | No (optional) | **No** | Checkbox absent |

**Required field score:** 2 / 2 mandatory fields present; 0 / 1 optional field.

#### Validation implemented

| Validation | Spec | Implemented | How |
|------------|------|-------------|-----|
| Email/username required | Yes | Partial | HTML `required` attribute only |
| Password required | Yes | Partial | HTML `required` attribute only |
| Blur validation | Yes | **No** | No `(blur)` handlers or touched state |
| Email format | Implied | **No** | `type="email"` gives browser hint only |
| Auth failure message | Yes | Partial | Custom banner, not spec wording |
| Suspended account | Yes | **No** | Not distinguishable in demo auth |
| Deactivated account | Yes | **No** | Not distinguishable in demo auth |
| Clear password on failure | Yes | **No** | Password value retained |
| Preserve username on failure | Yes | Yes | Email not cleared |
| Loading / disable on submit | Yes | **No** | No spinner or disabled state |
| Form-level error summary pattern | Yes | **No** | No standard title/body pattern |
| Success banner before redirect | Optional | **No** | Immediate navigation only |

#### Missing validation

- `Username or email is required.` — inline message on blur/submit
- `Password is required.` — inline message on blur/submit
- `Your session could not be started. Check your credentials and try again.`
- `Your account is suspended.` (`AUTH_ACCOUNT_SUSPENDED`)
- `Your account is deactivated.` (`AUTH_ACCOUNT_DEACTIVATED`)
- Standard form-level summary: `There is a problem with this form.`
- Programmatic validation via `ReactiveFormsModule` + `Validators.required`, `Validators.email`
- Server-side error mapping from API-173 response codes
- Password field clear after failed attempt

#### UX issues

| Issue | Severity | Detail |
|-------|----------|--------|
| Demo credentials pre-filled | High | `email` and `password` defaulted in component TS — inappropriate for production |
| Demo hint panel | High | Visible list of credentials undermines security UX |
| No Forgot Password / Need Help | Medium | Spec requires secondary actions |
| No Remember Session checkbox | Low | Optional field omitted |
| No footer version / privacy notice | Low | Spec UI-001 wireframe element missing |
| No loading state | Medium | Spec: disable inputs, show `Signing you in...` spinner |
| No focus management | Medium | Spec: focus on heading or username on load; WCAG 2.2 AA |
| Native `required` only | Medium | Browser tooltips instead of spec-aligned inline messages |
| Error banner not using `ValidationMessageBlock` | Low | Uses `SuccessWarningErrorBanner` instead of field-level pattern |
| Sign-in uses raw `<input>` not `TextInputComponent` | Medium | Design system bypass |
| No `aria-describedby` for errors | Medium | Accessibility gap per UI spec |
| Auth is client-side demo | Critical | `AuthService.signIn()` checks hardcoded map, not API-173 |

#### Improvement recommendations

1. Replace template-driven form with `FormGroup`: `email: [null, [Validators.required, Validators.email]]`, `password: [null, Validators.required]`
2. Add `Remember Session` checkbox bound to `rememberMe` for session persistence policy
3. On failed login: clear password, preserve email, show spec-aligned banner message
4. Add `submitting` signal: disable inputs and show button spinner during API call
5. Integrate `GET /api/v1/auth/session` on app init; map `AUTH_ACCOUNT_SUSPENDED` / `AUTH_ACCOUNT_DEACTIVATED` to distinct messages
6. Wire `ValidationMessageBlock` per field with `aria-describedby`
7. Remove demo defaults and demo hint from production builds (environment-gated dev helper only)
8. Add `Forgot Password` / `Need Help` links per wireframe
9. Add footer strip with version and security notice

**Coverage score: 22%**

---

### Auxiliary: Global Search Bar (not F-###, relates to F-020)

**Location:** `shared/ui/navigation/global-search-bar/`  
**Used in:** `GlobalHeaderComponent`

| Aspect | Status |
|--------|--------|
| Form element | No `<form>` wrapper |
| Fields | Single `query` text input (F-020 expects SKU / name / barcode / category / location) |
| Submit / search action | **None** — no `(ngSubmit)`, no search handler |
| Validation | None |
| Empty query handling | None |

**UX issues:** Search input with no action confuses users; placeholder promises search but Enter does nothing.

**Recommendation:** Either implement as F-020 Availability Inquiry quick-search with submit and validation, or reduce placeholder scope to "Search (coming soon)" until wired.

---

### F-049 — Session / Logout (partial)

**Location:** `shared/ui/navigation/user-menu/user-menu.component.html`  
**Trigger:** Sign Out button calls `AuthService.signOut()`

| Field | Spec | Implemented |
|-------|------|-------------|
| Logout All Sessions checkbox | Optional | **No** |

| Behavior | Spec | Implemented |
|----------|------|-------------|
| End session | Yes | Partial — clears `sessionStorage` only |
| `POST /api/v1/auth/logout` | Yes | **No** |
| Logout failure banner + retry | Yes | **No** |
| Redirect to sign-in | Yes | Yes |

**Coverage score: 5%**

---

## Forms Not Implemented (F-002 – F-048)

The following 47 forms have **zero UI implementation**. Screens show `PageTitleBar` + JSON mock preview only. Shared form components (`TextInput`, `DropdownSelect`, `LineItemEditor`, etc.) exist as empty shells and are not used.

### Summary by domain

| Domain | Forms | Total spec required field groups | Validation rules in spec (approx.) |
|--------|-------|----------------------------------|-------------------------------------|
| Master data | F-002–F-011 | ~45 fields | ~80 messages |
| Procurement / inbound | F-012–F-018 | ~50 fields | ~70 messages |
| Inventory visibility | F-019–F-021 | ~12 fields | ~15 messages |
| Inventory accuracy | F-022–F-027 | ~25 fields | ~45 messages |
| Fulfillment | F-028–F-035 | ~40 fields | ~55 messages |
| Transfers / alerts | F-036–F-039 | ~20 fields | ~30 messages |
| Returns | F-040–F-041 | ~25 fields | ~35 messages |
| Reports / finance | F-042–F-044 | ~15 fields | ~25 messages |
| Audit / admin | F-045–F-048 | ~20 fields | ~30 messages |

### Critical missing forms by business priority

| Priority | Form | Why critical | Key validations missing |
|----------|------|--------------|-------------------------|
| P0 | F-002 Product | Master data foundation | SKU pattern, duplicate SKU, lifecycle conditionals |
| P0 | F-015 Goods Receipt | Core inbound workflow | Lot/MRSL traceability, quantity vs PO |
| P0 | F-025 Stock Adjustment | Governance-controlled | Reason code required, SoD, on-hand ceiling |
| P0 | F-029 Order Reservation | Fulfillment core | ATP ceiling, safety stock breach |
| P1 | F-012 / F-013 Requisition / PO | Procurement | Line-item validation, discontinued product |
| P1 | F-037 Transfer Request | Network balance | Source≠destination, minimum threshold |
| P1 | F-038 Transfer Approval | SoD approvals | Rejection reason conditional |
| P1 | F-047 User Account | Security | Email format, role SoD, suspension reason |
| P2 | F-021 Movement History | Auditability | Date range cross-validation |
| P2 | F-046 Audit Trail Query | Compliance | Date range, export size limit |

### Per-form quick reference (not implemented)

For each form below: **Required fields implemented = 0**, **Validation implemented = None**, **Coverage = 0%**. Missing validation = all spec messages for that form. UX issue = form UI absent; user cannot perform workflow.

| ID | Name | Spec required fields (summary) | Top missing validations |
|----|------|-------------------------------|-------------------------|
| F-002 | Product Form | SKU, Name, UoM, Lifecycle Status | SKU pattern, duplicate SKU/barcode, traceability conditionals |
| F-003 | Duplicate Resolution | Resolution Action, Source SKU | MERGE conditionals, merge authorization |
| F-004 | Bulk Import | Import Mode, File | File type, batch duplicate SKUs, row errors |
| F-005 | Location Form | Code, Name, Type, Status | Hierarchy rules, activation/closure conditionals |
| F-006 | Storage Position | Location, Position Code | Uniqueness within location |
| F-007 | Stock Policy | Location, SKU, 3 thresholds, Effective From | Threshold ordering (min ≤ reorder ≤ max) |
| F-008 | ABC Classification | SKU, ABC Class | A/B/C enum validation |
| F-009 | Governance Policy | Name, Effective From, parameters | Date range, threshold/tolerance pairs |
| F-010 | Reason Code | Code, Description, Transaction Types | Code format uppercase, retirement reason |
| F-011 | Supplier | Code, Name, Payment Terms Days | Email format, duplicate code, deactivation reason |
| F-012 | Purchase Requisition | Location, Justification, Lines | Discontinued product, network transfer decline |
| F-013 | Purchase Order | Supplier, Location, Delivery Date, Lines | Amendment/cancel reasons, received qty floor |
| F-014 | Inbound Delivery Planning | PO context, Arrival Date | Qty vs open PO remaining |
| F-015 | Goods Receipt | Location, Lines, Accepted Qty | Lot required, MRSL compliance, PO validation |
| F-016 | Receipt Discrepancy | Type, Variance, Reason, Notes | Resolution outcome conditionals |
| F-017 | Put-Away | Lines, Qty, Storage Position | Qty vs unplaced remainder |
| F-018 | Ad-Hoc Receipt | Location, Auth Ref, Reason, Lines | Governance authorization |
| F-019 | Status Filter | Conditional location/SKU | At least one filter, location scope |
| F-020 | Availability Inquiry | Product search value | Product selection, location scope |
| F-021 | Movement History | Start Date, End Date | Date range, optional filter guidance |
| F-022 | Cycle Count | Physical Quantity | Non-negative, blind count (no system qty) |
| F-023 | Physical Count | Location, Start/End dates | Certification completeness |
| F-024 | Variance Investigation | Root Cause, Findings | SoD — approver ≠ counter |
| F-025 | Stock Adjustment | Location, SKU, Type, Qty, Reason | On-hand ceiling, write-off evidence |
| F-026 | Write-Off Authorization | Decision | Finance acknowledgment conditional |
| F-027 | Quarantine / Hold | Qty, Hold Reason, Reason Code | Release disposition conditionals |
| F-028 | Order Creation | Channel, Lines | Active product, external ID for import |
| F-029 | Order Reservation | Location, Qty (conditional) | ATP limit, safety stock breach |
| F-030 | Pick Verification | Picked Qty, SKU | Lot, substitution reference |
| F-031 | Pack Order | Packages, line items | Packed ≤ picked |
| F-032 | Shipment Confirmation | Shipment lines, Shipped Qty | Pick verified gate, lot |
| F-033 | Partial / Backorder | Fulfill Qty, Backorder checkbox | Customer ack reference, remainder math |
| F-034 | Fulfillment Exception | Type, Description | 2000 char limit |
| F-035 | Split Fulfillment Plan | Allocations (location + qty) | Total = order qty, per-location ATP |
| F-036 | Alert Acknowledgment | Action Taken | Notes when dismiss/defer |
| F-037 | Transfer Request | Source, Dest, Justification, Lines | Source ≠ dest, minimum threshold |
| F-038 | Transfer Approval | Decision | Rejection reason conditional |
| F-039 | Transfer Dispatch/Receipt | Qty per line | Variance notes on mismatch |
| F-040 | Return Authorization | Order, Reason, Lines | Qty ≤ shipped, eligibility |
| F-041 | Return Inspection/Disposition | Multi-step lines | Inspection before disposition (BR-026) |
| F-042 | Report Filter | Report Type | Conditional dates, range size limit |
| F-043 | Valuation Reconciliation | Period End Date | Threshold 0–100% |
| F-044 | Promotional Allocation | Campaign, Location, SKU, Qty, Dates | Date range, ATP, override auth |
| F-045 | Audit Review Scope | Start/End dates | Finding fields conditional, export size |
| F-046 | Audit Trail Query | Start/End dates | Date range, export size |
| F-047 | User Account | User ID, Email, Name, Roles | SoD on roles, suspend/deactivate reasons |
| F-048 | Role & Access Control | Permission matrix | SoD evaluation fields, initiator ≠ approver |

---

## Form Component Library vs. Validation Spec

Shared form components exist but **do not implement** the validation behaviors they were designed for:

| Component | Spec role | `ControlValueAccessor` | Validation wired | Used in pages |
|-----------|-----------|------------------------|------------------|---------------|
| `TextInputComponent` | C-026 | No | No | No |
| `TextAreaNotesFieldComponent` | C-027 | No | No | No |
| `DropdownSelectControlComponent` | C-028 | No | No | No |
| `CheckboxGroupComponent` | C-029 | No | No | No |
| `RadioGroupSegmentedChoiceComponent` | C-030 | No | No | No |
| `NumberInputComponent` | C-031 | No | No | No |
| `DateFieldComponent` | C-032 | No | No | No |
| `FileUploadControlComponent` | C-033 | No | No | No |
| `ValidationMessageBlockComponent` | C-034 | N/A | **Input unused in template** | No |
| `ReadOnlyReviewFormComponent` | C-035 | N/A | No | No |
| `LineItemEditorComponent` | C-036 | No | No | No |
| `ToggleSwitchControlComponent` | C-059 | No | No | No |

**Impact:** Even when forms are built, validation must be added from scratch unless components are upgraded to support `ControlValueAccessor` and error display.

---

## Recommended Validation Architecture

### 1. Form builder foundation

```typescript
// shared/forms/ims-validators.ts
export const skuValidator = Validators.pattern(/^[A-Z0-9][A-Z0-9_-]*$/);
export const dateRangeValidator: ValidatorFn = (group) => { /* ... */ };
export const quantityPositiveValidator = Validators.min(0.0001);
```

### 2. Reusable field wrapper

```html
<ims-form-field [label]="'SKU'" [control]="form.controls.sku">
  <input imsInput formControlName="sku" />
</ims-form-field>
```

`ims-form-field` shows `ValidationMessageBlock` when `control.touched && control.invalid`.

### 3. Error mapping service

```typescript
mapApiErrors(error: ApiErrorResponse, form: FormGroup): void {
  // VAL_* → control.setErrors
  // BIZ_* / CONF_* → formLevelBanner
}
```

### 4. Implementation order aligned to forms

| Wave | Forms | Validation focus |
|------|-------|------------------|
| 1 | F-001, F-049 | Auth session, logout |
| 2 | F-002, F-005, F-007, F-011 | Master data patterns A, B, C |
| 3 | F-012, F-013, F-015–F-018 | Line-item editors + reason codes |
| 4 | F-025–F-027, F-038, F-026 | Approval + SoD + reason code D |
| 5 | F-021, F-042, F-045, F-046 | Date range pattern E |
| 6 | F-029–F-035 | ATP / quantity ceiling validations |
| 7 | F-047, F-048 | Role SoD, permission matrix |

### 5. Testing strategy

- Unit tests per `ValidatorFn` (SKU pattern, date range, threshold ordering)
- Component tests: blur shows error, submit shows all errors, correct error clears on fix
- E2E: sign-in failure preserves email / clears password; adjustment blocked without reason code

---

## Coverage Statistics

| Category | Forms | Avg coverage |
|----------|-------|--------------|
| Authentication (F-001, F-049) | 2 | 13% |
| Master data (F-002–F-011) | 10 | 0% |
| Procurement / inbound (F-012–F-018) | 7 | 0% |
| Inventory query (F-019–F-021) | 3 | 0% |
| Inventory accuracy (F-022–F-027) | 6 | 0% |
| Fulfillment (F-028–F-035) | 8 | 0% |
| Transfers / alerts (F-036–F-039) | 4 | 0% |
| Returns (F-040–F-041) | 2 | 0% |
| Reports / campaigns (F-042–F-044) | 3 | 0% |
| Audit / admin (F-045–F-048) | 4 | 0% |
| **Overall** | **49** | **~3%** |

---

## Document References

| Document | Path |
|----------|------|
| Form Specifications F-001–F-049 | `SRS/Inventory-Management-System-SRS.md` |
| Shared validation behavior | Same document § Shared Validation Behavior |
| UI Specification (validation section) | `SRS/UI Specification/UI Specification.md` |
| Request DTO Validation | `SRS/API_Design/Request-DTO-Validation-Spec.md` |
| Sign-in implementation | `ims-frontend/src/app/features/auth/sign-in-page/` |
| Component Coverage Matrix | `gap_frontend/Component-Coverage-Matrix.md` |
| Screen Coverage Matrix | `gap_frontend/Screen-Coverage-Matrix.md` |

---

*End of report.*
