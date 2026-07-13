# Routing Assessment Report

**Project:** IMS Frontend Routing vs. Approved Navigation Map  
**Specification Sources:**
- `SRS/Inventory-Management-System-SRS.md` § Navigation Structure (lines 49621–50156)
- `SRS/Frontend Architecture/Frontend-Architecture-Mapping.md` § Application routes (UI-001–UI-050)

**Implementation Source:** `ims-frontend/src/app/app.routes.ts`, guards, `navigation.model.ts`  
**Report Date:** July 7, 2026  
**Perspective:** Senior Angular Architect

---

## Executive Summary

| Metric | Spec | Implemented | Coverage |
|--------|------|-------------|----------|
| Top-level navigation modules | 12 | 12 | 100% |
| Base list/workspace routes (UI-001–UI-050) | 50 | 50 | 100% |
| Child/detail routes (`/new`, `/:id`, nested) | ~35 | 0 | 0% |
| Secondary nav items (Navigation Structure) | ~52 | ~44 linked | ~85% |
| Route guards (auth) | Required | 2 functional | Partial |
| Permission / scope guards | Required | 0 | 0% |
| Feature-area lazy loading (`loadChildren`) | Recommended | 0 | 0% |
| Component lazy loading (`loadComponent`) | Acceptable | 50 routes | 100% |
| Role-filtered navigation | Required | 0 | 0% |
| Dynamic breadcrumbs (record level) | Required | 0 | 0% |
| **Overall routing maturity** | — | — | **~38%** |

### Key Findings

1. **Base route coverage is complete** — all 50 UI screens have a registered path aligned with the Frontend Architecture Mapping.
2. **Workflow routing is absent** — no detail, create, or nested child routes; deep links to records (`:sku`, `:orderId`, etc.) are impossible.
3. **Guards are authentication-only** — no permission (`PERM-xxx`), location-scope, or role-based route protection.
4. **Lazy loading is shallow** — per-page `loadComponent` is used, but the architecture recommends domain-level `loadChildren` bundles.
5. **Navigation model diverges from the Navigation Map** — secondary menus, module placement, and cross-module links are inconsistent.

---

## Routing Architecture (As Implemented)

```text
app.routes.ts
├── '' → redirectTo 'home/operations'
├── auth/sign-in          [guestGuard]     loadComponent → SignInPage
├── '' (AppShell)         [authGuard]      component → AppShellComponent (eager)
│   └── 49 child routes   (no per-route guards)   loadComponent → *Page
└── '**' → redirectTo 'home/operations'
```

```1:14:ims-frontend/src/app/app.routes.ts
import { Routes } from '@angular/router';
import { authGuard, guestGuard } from './core/guards/auth.guard';
import { AppShellComponent } from './core/layout/app-shell/app-shell.component';

export const routes: Routes = [
  { path: '', redirectTo: 'home/operations', pathMatch: 'full' },
  {
    path: 'auth/sign-in',
    canActivate: [guestGuard],
    loadComponent: () =>
      import('./features/auth/sign-in-page/sign-in-page.page').then((m) => m.SignInPage),
  },
  {
    path: '',
    component: AppShellComponent,
    canActivate: [authGuard],
```

**Router configuration:** `provideRouter(routes)` only — no `withComponentInputBinding()`, `withViewTransitions()`, preloading strategy, or custom URL matchers.

---

## 1. Missing Routes

### 1.1 Child / Detail / Create Routes (Critical)

The Navigation Map sitemap and Frontend Architecture Mapping define **~35 parameterized and nested routes**. None are registered.

| Parent route | Missing child routes | Screen | Nav sitemap reference |
|--------------|---------------------|--------|----------------------|
| `/products/catalog` | `/new`, `/:sku` | UI-005 | Product Detail, Create, Edit |
| `/products/stock-policies` | `/:locationCode/:sku` | UI-008 | Product-Location Policy Detail |
| `/locations` | `/new`, `/:locationCode` | UI-007 | Location Detail |
| `/governance/policies` | — (tabs only) | UI-010 | — |
| `/governance/reason-codes` | **entire route missing** | UI-010 | Reason Codes (secondary nav) |
| `/procurement/suppliers` | `/new`, `/:supplierCode` | UI-011 | Supplier Detail |
| `/procurement/purchase-orders` | `/new`, `/:purchaseOrderId` | UI-012 | PO Detail |
| `/procurement/requisitions` | `/:requisitionId` | UI-013 | Requisition Detail |
| `/inbound/goods-receipts` | `/:goodsReceiptId` | UI-015 | Goods Receipt Detail |
| `/inbound/discrepancies` | `/goods-receipts/:goodsReceiptId/discrepancies` | UI-016 | Discrepancy Detail (nested) |
| `/inbound/put-away` | `/:goodsReceiptId` | UI-017 | Put-Away Task Detail |
| `/inventory/cycle-counts` | `/:cycleCountId` | UI-023 | Count Submission |
| `/inventory/physical-counts` | `/:physicalCountId` | UI-024 | Count Session Detail |
| `/inventory/variances` | `/:caseId` | UI-025 | Variance Investigation Detail |
| `/inventory/adjustments` | `/:caseId` | UI-026 | Adjustment Case Detail |
| `/inventory/write-offs` | `/:caseId` | UI-027 | Write-Off Authorization Detail |
| `/fulfillment/reservations` | `/:orderId` | UI-030 | Order Reservation Detail |
| `/fulfillment/pick-pack-ship` | `/:orderId` | UI-031 | Pick/Pack/Ship workflow |
| `/fulfillment/partial-backorders` | `/:orderId` | UI-032 | Backorder Detail |
| `/fulfillment/exceptions` | `/:orderId` | UI-033 | Exception Detail |
| `/fulfillment/order-status` | `/:orderId` | UI-034 | Order Detail |
| `/fulfillment/split-planner` | `/:orderId` | UI-035 | Split Fulfillment Plan |
| `/transfers/requests` | `/new`, `/:transferId` | UI-038 | Transfer Request Detail |
| `/transfers/approvals` | `/:transferId` | UI-039 | Approval Detail |
| `/transfers/execution` | `/:transferId` | UI-040 | Dispatch / Receipt Detail |
| `/returns/authorizations` | `/new`, `/:returnAuthorizationId` | UI-042 | Return Authorization Detail |
| `/returns/inspection-disposition` | `/:returnId` | UI-043 | Receipt / Inspection / Disposition |
| `/admin/users` | `/new`, `/:userId` | UI-049 | User Account Detail |

**Impact:** Bookmarking, email/deep links, browser back/forward through workflows, and breadcrumb record crumbs cannot work. Contextual navigation defined in the Navigation Map (e.g. “View Product”, “Open PO”) has no target routes.

### 1.2 Routes Referenced in Navigation Structure but Absent

| Item | Navigation Map location | Expected behavior | Status |
|------|----------------------|-------------------|--------|
| `/governance/reason-codes` | Governance secondary nav; UI-010 | Standalone or tabbed reason-code admin | **Missing route** |
| Inventory Dashboard | Reports secondary nav; sitemap | Distinct from Operational Dashboard / Status Monitor | **No route** |
| My Tasks / Approvals | Home secondary; persistent utility | Aggregated approval inbox | **No route** (widget links to individual queues only) |
| Approvals Inbox | Governance secondary | Cross-domain approval hub | **No route** |
| In-Transit Tracking | Transfers secondary; sitemap | May be tab on execution page | **No dedicated route** (acceptable if tab-only) |
| Location Hierarchy | Locations secondary | Tab or sub-route on UI-007 | **No route/tab wiring** |
| Storage Positions | Locations secondary | Tab on location detail | **No route/tab wiring** |
| Location Activation / Closure | Locations secondary | Action flow on location detail | **No route/action wiring** |
| Global Search results | Persistent utility | `/search?q=` or modal route | **No route** |

### 1.3 Post-Login and Session Routes

| Route | Spec | Status |
|-------|------|--------|
| `/auth/sign-in` | UI-001 | Implemented |
| Return URL after login | Preserve `returnUrl` query param | **Not implemented** |
| Session expired redirect | Redirect to sign-in with message | **Not implemented** |
| `/auth/session-expired` | Optional dedicated screen | Not defined |

---

## 2. Incorrect Routes

No base list-route paths conflict with the Frontend Architecture Mapping — all 49 shell child paths match the approved `Application routes` entries for list/workspace screens.

### 2.1 Behavioral / Semantic Issues

| Issue | Current behavior | Spec expectation | Severity |
|-------|------------------|------------------|----------|
| Wildcard fallback | `{ path: '**', redirectTo: 'home/operations' }` | Unknown URLs should show not-found or access-denied | Medium |
| Auth failure masking | Invalid deep links silently land on dashboard | User should see 404 or permission denied | Medium |
| Sign-in success target | Always `home/operations` | Role-specific home (Executive → KPI dashboard) | Low |
| `non-po-receipts` path | `/inbound/non-po-receipts` | UI-018 name “Non-PO Receipt Intake” — path acceptable but inconsistent naming vs. `ad-hoc-receipts` in architecture folder | Low |

### 2.2 Structural Mismatches (Module Placement)

These are not wrong URLs but **incorrect information architecture** relative to the Navigation Map:

| Screen | Implemented under | Navigation Map secondary nav |
|--------|-------------------|------------------------------|
| Executive KPI Dashboard | Home **and** Reports (`/reports/executive-kpis`) | Home + Reports (duplicate is spec-intended) |
| Audit Workspace | Reports (`/reports/audit-workspace`) | **Governance & Audit** |
| Audit Trail Query | Reports (`/reports/audit-trail`) | **Governance & Audit** |
| Reason Codes | Not routed (only policies page) | **Governance & Audit** |

The Frontend Architecture Mapping places audit routes under `reports` feature module — a valid technical choice — but **`MAIN_NAVIGATION` places Governance & Audit separately** with only policies linked, creating user-facing inconsistency.

---

## 3. Route Guards

### 3.1 Implemented Guards

| Guard | File | Applied to | Behavior |
|-------|------|------------|----------|
| `authGuard` | `core/guards/auth.guard.ts` | App shell parent | Redirects unauthenticated users to `/auth/sign-in` |
| `guestGuard` | `core/guards/auth.guard.ts` | `/auth/sign-in` | Redirects authenticated users to `/home/operations` |

```5:25:ims-frontend/src/app/core/guards/auth.guard.ts
export const authGuard: CanActivateFn = () => {
  const auth = inject(AuthService);
  const router = inject(Router);

  if (auth.isAuthenticated()) {
    return true;
  }

  return router.createUrlTree(['/auth/sign-in']);
};

export const guestGuard: CanActivateFn = () => {
  const auth = inject(AuthService);
  const router = inject(Router);

  if (!auth.isAuthenticated()) {
    return true;
  }

  return router.createUrlTree(['/home/operations']);
};
```

**Assessment:** Functional for demo auth (`sessionStorage` + hardcoded users). No `returnUrl` preservation. No integration with `GET /api/v1/auth/session`.

### 3.2 Missing Guards (Per Spec)

| Guard | Purpose | Routes affected | Spec reference |
|-------|---------|-----------------|----------------|
| `permissionGuard` | Enforce `PERM-xxx` on route `data.permissions` | All 49 shell routes | Frontend Architecture § “permission-based access” |
| `roleGuard` | Hide/restrict modules by role menu | Module parent routes | Navigation Structure § Role-Specific Menus |
| `locationScopeGuard` | Validate `locationCode` route param against user scope | Routes with `:locationCode` | API location-scope validation |
| `unsavedChangesGuard` | `canDeactivate` on draft forms | Create/edit routes | Form spec success/error behavior |
| `sessionValidityGuard` | Revalidate session server-side on navigation | App shell | API-173 session bootstrap |

### 3.3 Guard Coverage Matrix (Sample)

| Route | Auth | Permission (spec) | Implemented permission check |
|-------|------|-------------------|------------------------------|
| `/home/operations` | Yes | PERM-083, 085, 064 | No |
| `/products/catalog` | Yes | PERM-001–005 | No |
| `/inventory/adjustments` | Yes | PERM-043–045 | No |
| `/admin/users` | Yes | PERM-095, 096 | No |
| `/admin/roles-access` | Yes | PERM-013, 062 | No |
| `/reports/executive-kpis` | Yes | PERM-088 | No |

**Risk:** Any authenticated demo user can navigate to all routes regardless of role (`admin@ims.local` vs `warehouse@ims.local` see identical menus and routes).

---

## 4. Lazy Loading Opportunities

### 4.1 Current State

| Technique | Usage | Assessment |
|-----------|-------|------------|
| `loadComponent` | All 50 page routes | Good — code-split per page |
| `loadChildren` | None | Gap vs. architecture recommendation |
| `AppShellComponent` | Eager import in `app.routes.ts` | Shell always in main bundle |
| Preloading | None | No `PreloadAllModules` or custom strategy |
| Route-level providers | None | Facades/services not scoped to features |

Every route is a **sibling** under a flat `children` array (49 entries). This scales poorly for maintainability even though each page lazy-loads individually.

### 4.2 Recommended Feature-Area Lazy Loading

Align with Frontend Architecture § Routing Recommendation:

```typescript
// Target structure (illustrative)
{
  path: 'inventory',
  canActivate: [authGuard, permissionGuard],
  loadChildren: () => import('./features/inventory/inventory.routes'),
}
```

| Feature area | Routes | Est. chunk | Priority |
|--------------|--------|------------|----------|
| `auth` | sign-in | Small | P0 |
| `home` | operations | Small | P0 |
| `inventory` | 10 routes | Large | P0 |
| `procurement` | 7 routes | Large | P1 |
| `inbound` | 4 routes | Medium | P1 |
| `fulfillment` | 6 routes | Large | P1 |
| `products` | 4 routes | Medium | P1 |
| `transfers` | 4 routes | Medium | P2 |
| `returns` | 2 routes | Small | P2 |
| `reports` | 6 routes | Large | P2 |
| `procurement` + alerts | shared chunk | — | P2 |
| `governance` | 2 routes | Small | P2 |
| `admin` | 2 routes | Small | P3 |
| `locations` | 1+ routes | Small | P3 |
| `notifications` | 1 route | Small | P3 |

### 4.3 Additional Optimizations

| Opportunity | Benefit |
|-------------|---------|
| `withComponentInputBinding()` | Bind `:sku`, `:orderId` directly to `@Input()` on routed components |
| Custom preloader for Home + Inventory | Faster perceived load for warehouse roles |
| Shared workflow chunk | Pick/pack/ship, approvals, queues share components |
| Defer shell sub-nav | Lazy-load `SecondaryNavigationPanel` metadata per module |
| Route `data: { preload: true }` | Mark high-traffic operational routes |

---

## 5. Navigation Inconsistencies

### 5.1 `MAIN_NAVIGATION` vs. Navigation Structure

| Area | Navigation Map (spec) | `navigation.model.ts` | Gap |
|------|----------------------|----------------------|-----|
| **Home** | Operational Dashboard, Executive KPI, My Notifications, **My Approvals** | Dashboard, Executive KPI, Notifications | **My Approvals** missing |
| **Locations** | Directory, **Hierarchy**, **Storage Positions**, **Activation/Closure** | Directory only | 3 secondary items missing |
| **Transfers** | Requests, Approvals, Execution, **In-Transit Tracking**, Rebalancing | 4 items (no In-Transit label) | Label mismatch |
| **Reports** | Operational, **Inventory Dashboard**, KPI, Valuation, Promotional | Operational, Executive KPI, Valuation, Promotional, **Audit Workspace**, **Audit Trail** | Inventory Dashboard missing; audit items under Reports not Governance |
| **Governance** | Policies, **Reason Codes**, **Audit Workspace**, **Audit Trail**, **Approvals Inbox** | Policies only | 4 items missing or misplaced |

### 5.2 Cross-Module Link Inconsistencies

| Source | Link target | Issue |
|--------|-------------|-------|
| Home → Executive KPI | `/reports/executive-kpis` | Cross-module route under Home secondary nav (spec allows this) |
| Task Approval Widget | `/transfers/approvals`, `/inventory/variances`, `/procurement/requisitions` | Hardcoded mock counts; no unified `/tasks` route |
| Operational Dashboard quick actions | 4 routes | Valid; missing replenishment, cycle count per role menus |
| Global header brand | `/home/operations` | Correct |
| Notification icon | `/notifications` | Correct |
| Breadcrumbs (all pages) | Static 2-level | No module segment, no record crumb (spec requires 3–4 levels) |

Example static breadcrumb (no module, no dynamic record):

```2:2:ims-frontend/src/app/features/products/product-catalog-page/product-catalog-page.page.html
  <ims-breadcrumb-trail [items]="[{ label: 'Home', route: '/home/operations' }, { label: 'Product Catalog Management' }]"></ims-breadcrumb-trail>
```

Spec format: `Home > Products > Product Catalog > SKU-100245`

### 5.3 Secondary Navigation Active-State Logic

```25:36:ims-frontend/src/app/shared/ui/layout/secondary-navigation-panel/secondary-navigation-panel.component.ts
  private updateActiveModule(url: string): void {
    this.activeModule =
      MAIN_NAVIGATION.find(
        (m) => url.startsWith(m.route.split('/').slice(0, 2).join('/')) || url.startsWith('/' + m.label.toLowerCase())
      ) ??
      MAIN_NAVIGATION.find((m) => m.children?.some((c) => url.startsWith(c.route))) ??
      null;

    if (!this.activeModule) {
      const segment = '/' + url.split('/').filter(Boolean).slice(0, 2).join('/');
      this.activeModule = MAIN_NAVIGATION.find((m) => m.children?.some((c) => c.route.startsWith(segment))) ?? null;
    }
  }
```

| Problem | Example |
|---------|---------|
| Label-based match fails | `"Reports & Analytics".toLowerCase()` → `/reports & analytics` — never matches `/reports/...` |
| Executive KPI under Home | Visiting `/reports/executive-kpis` highlights **Reports**, not Home — dual-placement confusion |
| Notifications | Under Home children but top-level utility — module highlight ambiguous |
| Governance audit screens | Routed under `/reports/*` — Governance module never highlights for audit pages |

### 5.4 Role-Based Navigation (Not Implemented)

Navigation Structure defines **7 role profiles** with distinct priority menus. Current implementation:

- Static `MAIN_NAVIGATION` for all users
- No `*ngIf` / route filter by `AuthService.user().roles`
- Warehouse user sees Administration, Governance, Reports same as admin

### 5.5 Persistent Utilities

| Utility | Spec | Implementation |
|---------|------|----------------|
| Global Search | Persistent; drives availability/product discovery | Input in header; **no route, no navigation action** |
| My Tasks / Approvals | Persistent shortcut | Widget on dashboard only |
| User Menu / Session | Sign out, profile | Sign out works; **no profile route**, no F-049 logout-all-sessions |

---

## Route-to-Screen Traceability Matrix

| UI ID | Screen | Spec route(s) | Impl. list route | Child routes | Match |
|-------|--------|---------------|------------------|--------------|-------|
| UI-001 | Sign In | `/auth/sign-in` | Yes | — | Yes |
| UI-002 | Operational Dashboard | `/home/operations` | Yes | — | Yes |
| UI-003 | Executive KPI | `/reports/executive-kpis` | Yes | — | Yes |
| UI-004 | Notification Center | `/notifications` | Yes | — | Yes |
| UI-005 | Product Catalog | `/products/catalog` + children | Yes | **No** | Partial |
| UI-006 | Product Import | `/products/import` | Yes | — | Yes |
| UI-007 | Location Management | `/locations` + children | Yes | **No** | Partial |
| UI-008 | Stock Policies | `/products/stock-policies` + children | Yes | **No** | Partial |
| UI-009 | ABC Classification | `/products/abc-classification` | Yes | — | Yes |
| UI-010 | Governance & Reason Codes | `/governance/policies`, `/governance/reason-codes` | Policies only | **reason-codes missing** | Partial |
| UI-011 | Supplier Management | `/procurement/suppliers` + children | Yes | **No** | Partial |
| UI-012 | Purchase Orders | `/procurement/purchase-orders` + children | Yes | **No** | Partial |
| UI-013 | Requisitions | `/procurement/requisitions` + children | Yes | **No** | Partial |
| UI-014 | Inbound Delivery Planning | `/procurement/inbound-delivery-planning` | Yes | — | Yes |
| UI-015 | Goods Receipt | `/inbound/goods-receipts` + children | Yes | **No** | Partial |
| UI-016 | Receipt Discrepancy | `/inbound/discrepancies` + nested | Yes | **No** | Partial |
| UI-017 | Put-Away | `/inbound/put-away` + children | Yes | **No** | Partial |
| UI-018 | Non-PO Receipt | `/inbound/non-po-receipts` | Yes | — | Yes |
| UI-019 | Inbound Supply Tracking | `/procurement/inbound-supply-tracking` | Yes | — | Yes |
| UI-020 | Status Monitor | `/inventory/status-monitor` | Yes | — | Yes |
| UI-021 | Availability Inquiry | `/inventory/availability` | Yes | — | Yes |
| UI-022 | Movement History | `/inventory/movement-history` | Yes | — | Yes |
| UI-023 | Cycle Counts | `/inventory/cycle-counts` + children | Yes | **No** | Partial |
| UI-024 | Physical Counts | `/inventory/physical-counts` + children | Yes | **No** | Partial |
| UI-025 | Variance Approvals | `/inventory/variances` + children | Yes | **No** | Partial |
| UI-026 | Stock Adjustments | `/inventory/adjustments` + children | Yes | **No** | Partial |
| UI-027 | Write-Offs | `/inventory/write-offs` + children | Yes | **No** | Partial |
| UI-028 | Quarantine & Holds | `/inventory/quarantine` | Yes | — | Yes |
| UI-029 | Shrinkage Analysis | `/inventory/shrinkage-obsolescence` | Yes | — | Yes |
| UI-030 | Order Reservation | `/fulfillment/reservations` + children | Yes | **No** | Partial |
| UI-031 | Pick / Pack / Ship | `/fulfillment/pick-pack-ship` + children | Yes | **No** | Partial |
| UI-032 | Partial / Backorder | `/fulfillment/partial-backorders` + children | Yes | **No** | Partial |
| UI-033 | Fulfillment Exceptions | `/fulfillment/exceptions` + children | Yes | **No** | Partial |
| UI-034 | Order Status | `/fulfillment/order-status` + children | Yes | **No** | Partial |
| UI-035 | Split Fulfillment | `/fulfillment/split-planner` + children | Yes | **No** | Partial |
| UI-036 | Low-Stock Alerts | `/procurement/low-stock-alerts` | Yes | — | Yes |
| UI-037 | Replenishment Planning | `/procurement/replenishment-planning` | Yes | — | Yes |
| UI-038 | Transfer Request | `/transfers/requests` + children | Yes | **No** | Partial |
| UI-039 | Transfer Approvals | `/transfers/approvals` + children | Yes | **No** | Partial |
| UI-040 | Transfer Execution | `/transfers/execution` + children | Yes | **No** | Partial |
| UI-041 | Network Rebalancing | `/transfers/network-rebalancing` | Yes | — | Yes |
| UI-042 | Return Authorization | `/returns/authorizations` + children | Yes | **No** | Partial |
| UI-043 | Return Inspection | `/returns/inspection-disposition` + children | Yes | **No** | Partial |
| UI-044 | Operational Reports | `/reports/operational` | Yes | — | Yes |
| UI-045 | Valuation Reconciliation | `/reports/valuation-reconciliation` | Yes | — | Yes |
| UI-046 | Promotional Readiness | `/reports/promotional-readiness` | Yes | — | Yes |
| UI-047 | Audit Workspace | `/reports/audit-workspace` | Yes | — | Yes |
| UI-048 | Audit Trail Query | `/reports/audit-trail` | Yes | — | Yes |
| UI-049 | User Accounts | `/admin/users` + children | Yes | **No** | Partial |
| UI-050 | Roles & Access | `/admin/roles-access` | Yes | — | Yes |

**Summary:** 28 screens fully matched at list level; 22 screens missing child/detail routes; 1 screen missing an entire sub-route (`/governance/reason-codes`).

---

## Recommendations

### Priority 0 — Foundation

1. **Add `permissionGuard`** with route `data: { permissions: ['PERM-xxx'] }` on every shell child route.
2. **Introduce feature `*.routes.ts` files** with `loadChildren` per domain (inventory, procurement, fulfillment, etc.).
3. **Replace wildcard redirect** with a dedicated `NotFoundPage` or `ForbiddenPage` component.
4. **Preserve `returnUrl`** on `authGuard` redirect and honor it after sign-in.

### Priority 1 — Workflow Routing

5. **Add child routes** for the highest-traffic workflows first:
   - `/products/catalog/:sku`, `/inbound/goods-receipts/:goodsReceiptId`
   - `/fulfillment/reservations/:orderId`, `/transfers/requests/:transferId`
   - `/inventory/adjustments/:caseId`, `/procurement/purchase-orders/:purchaseOrderId`
6. **Register `/governance/reason-codes`** (or tab route on policies page with URL `?tab=reason-codes`).
7. **Enable `withComponentInputBinding()`** for route params.

### Priority 2 — Navigation Alignment

8. **Reconcile Governance vs. Reports** — either move audit routes under `/governance/*` or expand Governance secondary nav to link to `/reports/audit-*` explicitly.
9. **Align `MAIN_NAVIGATION`** with Navigation Structure secondary items (Locations sub-sections, My Approvals, Inventory Dashboard).
10. **Fix `updateActiveModule`** — remove label-based URL hack; use route prefix map.
11. **Implement role-filtered navigation** from `AuthService.user().roles`.

### Priority 3 — UX Polish

12. **Dynamic breadcrumb service** — derive crumbs from `ActivatedRoute` snapshot + record titles.
13. **Add `/tasks` or `/approvals`** inbox route per Navigation Map persistent utilities.
14. **Global search route** — `/search` with query params syncing to F-020 availability inquiry.
15. **`canDeactivate` guards** on forms with dirty state.

### Suggested Route Config Pattern

```typescript
{
  path: 'products',
  loadChildren: () => import('./features/products/products.routes'),
  canActivate: [authGuard],
  data: { module: 'products' },
},
// products.routes.ts
{
  path: 'catalog',
  children: [
    { path: '', loadComponent: () => import('./catalog.page') },
    { path: 'new', loadComponent: () => import('./catalog-create.page') },
    { path: ':sku', loadComponent: () => import('./catalog-detail.page') },
  ],
}
```

---

## Related Reports

| Report | Path |
|--------|------|
| Screen Coverage Matrix | `gap_frontend/Screen-Coverage-Matrix.md` |
| Project Architecture Report | `gap_frontend/Project-Architecture-Report.md` |
| Validation Coverage Report | `gap_frontend/Validation-Coverage-Report.md` |
| Frontend Architecture Mapping | `SRS/Frontend Architecture/Frontend-Architecture-Mapping.md` |
| Navigation Structure | `SRS/Inventory-Management-System-SRS.md` § Navigation Structure |

---

*End of report.*
