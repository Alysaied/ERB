# Project Architecture Report

**Project:** IMS Frontend (Inventory Management System)  
**Location:** `ims-frontend/`  
**Angular Version:** 19.2.x  
**Report Date:** July 7, 2026  
**Scope:** As-built architecture analysis (no SRS comparison)

---

## Executive Summary

The IMS frontend is a **modern, fully standalone Angular 19 application** organized around a **feature-folder architecture** with no `NgModule`-based feature modules. The app bootstraps via `bootstrapApplication`, uses **lazy-loaded route components**, and relies on a **mock-data layer** rather than HTTP APIs. Authentication is handled through a root-level `AuthService` with Angular Signals and `sessionStorage` persistence. The UI is built from **60 reusable shared components** grouped by concern (layout, forms, workflow, etc.) and **50 feature pages** mapped to screen IDs `UI-001` through `UI-050`.

---

## 1. Project Structure

### 1.1 Repository Layout

```
Inventory Management System/
├── ims-frontend/              # Angular application (analyzed project)
│   ├── angular.json
│   ├── package.json
│   ├── tsconfig.json
│   ├── public/                # Static assets (empty)
│   ├── scripts/
│   │   ├── scaffold-ims.mjs # Code generation scaffold
│   │   └── generated-routes.json
│   └── src/
│       ├── index.html
│       ├── main.ts
│       ├── styles.scss        # Global styles & design tokens
│       └── app/
│           ├── app.component.ts
│           ├── app.config.ts
│           ├── app.routes.ts
│           ├── core/
│           ├── shared/
│           └── features/
├── SRS/                       # Requirements documentation (out of scope)
└── gap_frontend/              # Gap analysis artifacts (this report)
```

### 1.2 Application Layering

| Layer | Path | Responsibility |
|-------|------|----------------|
| **Root** | `src/app/` | Bootstrap, routing table, root outlet |
| **Core** | `src/app/core/` | Cross-cutting concerns: auth, guards, shell layout, navigation model, mock data |
| **Shared** | `src/app/shared/ui/` | Reusable presentational & composite UI components |
| **Features** | `src/app/features/` | Domain-specific screen pages (one folder per screen) |

### 1.3 Architectural Style

- **Standalone-first:** No application `NgModule`s; all components declare `standalone: true`.
- **Route-driven features:** Features are folders, not Angular modules. Routing is centralized in `app.routes.ts`.
- **Lazy loading:** All feature pages use `loadComponent()` for code splitting.
- **Flat feature pages:** Each screen is a single page component (`.page.ts`) with co-located HTML/SCSS.
- **Scaffold-generated:** Project structure and routes are reproducible via `scripts/scaffold-ims.mjs`.

### 1.4 Naming Conventions

| Artifact | Pattern | Example |
|----------|---------|---------|
| Feature page | `{name}-page.page.ts` | `product-catalog-page.page.ts` |
| Shared component | `{name}.component.ts` | `data-table.component.ts` |
| Selector prefix | `ims-` | `ims-product-catalog-page` |
| Screen ID | `UI-###` | `UI-005` (Product Catalog) |
| Component ID (docs) | `C-###` | Referenced in README (C-001–C-060) |

---

## 2. Feature Modules (Feature Folders)

There are **no Angular `NgModule` feature modules**. Business domains are expressed as **feature folders** under `src/app/features/`, each containing one or more screen page components.

### 2.1 Feature Domains

| Domain Folder | Screens | Screen IDs | Description |
|---------------|---------|------------|-------------|
| `auth/` | 1 | UI-001 | Sign-in |
| `home/` | 1 | UI-002 | Operational dashboard |
| `notifications/` | 1 | UI-004 | Notification center |
| `products/` | 4 | UI-005–UI-006, UI-008–UI-009 | Catalog, import, stock policies, ABC classification |
| `locations/` | 1 | UI-007 | Location management |
| `governance/` | 1 | UI-010 | Governance policies |
| `procurement/` | 7 | UI-011–UI-014, UI-019, UI-036–UI-037 | Suppliers, POs, requisitions, inbound planning, supply tracking, alerts, replenishment |
| `inbound/` | 4 | UI-015–UI-018 | Goods receipt, discrepancies, put-away, non-PO receipts |
| `inventory/` | 10 | UI-020–UI-029 | Status monitor, availability, movement, counts, variances, adjustments, write-offs, quarantine, shrinkage |
| `fulfillment/` | 6 | UI-030–UI-035 | Reservations, pick/pack/ship, backorders, exceptions, order status, split planner |
| `transfers/` | 4 | UI-038–UI-041 | Requests, approvals, execution, network rebalancing |
| `returns/` | 2 | UI-042–UI-043 | Return authorizations, inspection & disposition |
| `reports/` | 6 | UI-003, UI-044–UI-048 | Executive KPIs, operational reports, valuation, promotional readiness, audit workspace, audit trail |
| `administration/` | 2 | UI-049–UI-050 | User accounts, roles & access control |

**Total:** 14 feature domains, **50 screen pages**.

### 2.2 Feature Page Pattern

Each feature page follows a consistent scaffold:

```typescript
@Component({
  selector: 'ims-{screen-name}-page',
  standalone: true,
  imports: [CommonModule, /* shared components */],
  templateUrl: './{screen-name}-page.page.html',
  styleUrl: './{screen-name}-page.page.scss'
})
export class {ScreenName}Page implements OnInit {
  private readonly mockData = inject(MockDataService);
  readonly screenId = 'UI-###';
  readonly title = '...';
  readonly description = '...';
  data: unknown = null;

  ngOnInit(): void {
    this.data = this.mockData.getScreenData('UI-###');
  }
}
```

Most pages are **thin presentation shells** that load mock data on init. The operational dashboard (`UI-002`) is a partial exception, composing additional shared widgets (KPI cards, quick actions, approval shortcuts).

---

## 3. Standalone Components

The application is **100% standalone**. Every component in `src/app/` declares `standalone: true`. There are no `NgModule` declarations in application source code.

### 3.1 Component Inventory

| Category | Count | Location |
|----------|-------|----------|
| Root component | 1 | `app.component.ts` |
| Core layout | 1 | `core/layout/app-shell/` |
| Feature pages | 50 | `features/**/**.page.ts` |
| Shared UI components | 60 | `shared/ui/**/**.component.ts` |
| **Total** | **112** | |

### 3.2 Bootstrap & Configuration

```typescript
// main.ts
bootstrapApplication(AppComponent, appConfig);

// app.config.ts
export const appConfig: ApplicationConfig = {
  providers: [
    provideZoneChangeDetection({ eventCoalescing: true }),
    provideRouter(routes),
  ],
};
```

### 3.3 Import Strategy

- Components import dependencies explicitly in their `imports` array.
- No shared `SharedModule` barrel; each consumer imports only what it needs.
- `CommonModule` and `RouterModule` are imported per component as needed.
- `FormsModule` is used only in sign-in and global search (template-driven forms).

---

## 4. Shared Components

Shared UI lives under `src/app/shared/ui/`, organized into **10 functional categories** with **60 components** total.

### 4.1 Category Breakdown

| Category | Path | Components | Purpose |
|----------|------|------------|---------|
| **Layout** | `shared/ui/layout/` | 7 | App chrome: header, nav bars, breadcrumbs, page title, footer, session badge |
| **Navigation** | `shared/ui/navigation/` | 6 | Search bar, user menu, notifications, quick actions, approval shortcuts |
| **Forms** | `shared/ui/forms/` | 12 | Text input, dropdown, date, number, checkbox, radio, file upload, validation, form sections |
| **Display** | `shared/ui/display/` | 8 | KPI cards, status badges, detail panels, tabs, summary strips, metadata blocks |
| **Tables** | `shared/ui/tables/` | 2 | Data table, row action menu |
| **Filters** | `shared/ui/filters/` | 4 | Filter bar, date range picker, saved views, search results list |
| **Feedback** | `shared/ui/feedback/` | 6 | Banners, dialogs, empty states, loading skeletons, bulk selection toolbar |
| **Workflow** | `shared/ui/workflow/` | 7 | Queues, timelines, approval panels, line-item editor, step progress, alerts |
| **Analytics** | `shared/ui/analytics/` | 5 | Report viewer, export actions, trend indicators, drill-down links, variance blocks |
| **Audit** | `shared/ui/audit/` | 5 | Permission matrix, role assignment, audit record viewer, evidence panel, scope selector |

### 4.2 Key Shared Components (Shell Integration)

The authenticated app shell composes these shared layout/navigation components:

- `GlobalHeaderComponent` — search, notifications, user menu, session context
- `MainNavigationBarComponent` — primary domain navigation (driven by `MAIN_NAVIGATION`)
- `SecondaryNavigationPanelComponent` — child route navigation per domain
- `FooterMetadataStripComponent` — footer metadata display
- `PageTitleBarComponent` / `BreadcrumbTrailComponent` — used on most feature pages

### 4.3 Shared Component Design

- All standalone with co-located `.html`, `.scss`, `.ts` files.
- Presentational by default; minimal service injection (e.g., `AuthService` in header/user menu).
- No shared component index/barrel exports observed; direct path imports used.
- Component library appears scaffolded to align with SRS component inventory (C-001–C-060).

---

## 5. Core Services

Only **two root-scoped services** exist in `src/app/core/services/`.

### 5.1 AuthService

| Attribute | Detail |
|-----------|--------|
| **Path** | `core/services/auth.service.ts` |
| **Scope** | `providedIn: 'root'` |
| **State** | Angular `signal<SessionUser \| null>` with `computed` `isAuthenticated` |
| **Persistence** | `sessionStorage` key `ims-session` |
| **Methods** | `signIn(email, password)`, `signOut()` |
| **Demo users** | `admin@ims.local` (System Administrator), `warehouse@ims.local` (Warehouse Manager) |

```typescript
export interface SessionUser {
  id: string;
  email: string;
  name: string;
  roles: string[];
  locationScope: string;
}
```

Authentication is **client-side demo logic** (hardcoded users, password length ≥ 4). No JWT, OAuth, or backend integration.

### 5.2 MockDataService

| Attribute | Detail |
|-----------|--------|
| **Path** | `core/services/mock-data.service.ts` |
| **Scope** | `providedIn: 'root'` |
| **Data store** | In-memory `Record<string, unknown>` keyed by screen ID (`UI-001`–`UI-050`) |
| **Primary API** | `getScreenData(screenId: string): unknown` |
| **Convenience methods** | `getProducts()`, `getLocations()`, `getDashboardKpis()`, `getAlerts()` |

This service is the **sole data layer** for all feature pages. No `HttpClient`, API services, or interceptors exist.

### 5.3 Core Models

| File | Purpose |
|------|---------|
| `core/models/navigation.model.ts` | `NavItem` interface and `MAIN_NAVIGATION` constant (12 top-level nav groups with child routes) |

### 5.4 Missing Core Infrastructure

The following are **not present** in the current codebase:

- HTTP client / API services
- Error handling service
- Logging service
- Environment configuration (`environment.ts`)
- HTTP interceptors (auth token, error handling)
- Role-based authorization service (beyond demo user roles in session)

---

## 6. Routing Structure

Routing is **fully centralized** in `src/app/app.routes.ts` (~365 lines). No child route files or feature-level route modules.

### 6.1 Route Topology

```
/  → redirect → /home/operations

/auth/sign-in          [guestGuard]     → SignInPage (lazy)

/                      [authGuard]      → AppShellComponent
  ├── /home/operations                  → OperationalDashboardPage (lazy)
  ├── /notifications                    → NotificationCenterPage (lazy)
  ├── /products/*                       → 4 product screens (lazy)
  ├── /locations                        → LocationManagementPage (lazy)
  ├── /governance/policies              → GovernancePoliciesPage (lazy)
  ├── /procurement/*                    → 7 procurement screens (lazy)
  ├── /inbound/*                        → 4 inbound screens (lazy)
  ├── /inventory/*                      → 10 inventory screens (lazy)
  ├── /fulfillment/*                    → 6 fulfillment screens (lazy)
  ├── /transfers/*                      → 4 transfer screens (lazy)
  ├── /returns/*                        → 2 return screens (lazy)
  ├── /reports/*                        → 6 report screens (lazy)
  └── /admin/*                          → 2 admin screens (lazy)

/**  → redirect → /home/operations
```

### 6.2 Route Configuration Characteristics

| Aspect | Implementation |
|--------|----------------|
| **Lazy loading** | All 50 feature pages via `loadComponent()` dynamic import |
| **Shell layout** | `AppShellComponent` wraps all authenticated routes as parent |
| **Auth boundary** | Single parent route with `canActivate: [authGuard]` |
| **Guest route** | Sign-in isolated with `canActivate: [guestGuard]` |
| **Wildcard** | Redirects unauthenticated unknown paths to dashboard (after auth guard) |
| **Route params** | No parameterized routes (`:id`) observed |
| **Nested routing** | Flat child routes under shell; no secondary `RouterOutlet` nesting |
| **Preloading** | No `PreloadAllModules` or custom preloading strategy |
| **Route data/resolvers** | Not used |

### 6.3 Navigation ↔ Route Alignment

`MAIN_NAVIGATION` in `navigation.model.ts` mirrors the route table with 12 primary domains and ~50 child links. Navigation is **configuration-driven**, not derived from the router config at runtime.

---

## 7. Guards

Two **functional route guards** (`CanActivateFn`) are defined in `core/guards/auth.guard.ts`.

### 7.1 authGuard

| Property | Value |
|----------|-------|
| **Applied to** | Parent shell route (`path: ''` with `AppShellComponent`) |
| **Logic** | Allows access if `AuthService.isAuthenticated()` is true |
| **Failure action** | Redirect to `/auth/sign-in` via `router.createUrlTree()` |

### 7.2 guestGuard

| Property | Value |
|----------|-------|
| **Applied to** | `/auth/sign-in` |
| **Logic** | Allows access only if user is **not** authenticated |
| **Failure action** | Redirect to `/home/operations` |

### 7.3 Guards Not Present

- Role-based guards (`CanActivate` by permission/role)
- `CanMatch` guards for lazy route protection
- `CanDeactivate` guards (unsaved changes)
- `CanActivateChild` guards
- Resolver guards for data prefetching

---

## 8. State Management Approach

### 8.1 Current Strategy: Local + Service State (No Global Store)

The application does **not** use NgRx, NGXS, Akita, Elf, or any dedicated state management library.

| State Type | Mechanism | Location |
|------------|-----------|----------|
| **Session/auth** | Angular `signal` + `computed` + `sessionStorage` | `AuthService` |
| **Screen data** | Component property set in `ngOnInit` from `MockDataService` | Each feature page |
| **Form state** | Template-driven (`ngModel`) | Sign-in, search bar |
| **UI feedback** | Component `signal` | Sign-in error message |
| **Navigation** | Static constant | `MAIN_NAVIGATION` |

### 8.2 Data Flow Pattern

```
MockDataService.getScreenData('UI-###')
        ↓
Feature Page (ngOnInit → local property)
        ↓
Template binding (one-way / minimal interactivity)
```

### 8.3 Observations

- **No shared reactive data layer** across screens.
- **No caching** of mock data beyond service singleton.
- **No optimistic updates** or write operations wired.
- **RxJS** is a dependency but minimally used in application code (primarily framework-internal).
- **Angular Signals** adoption is early-stage (auth + one form error).

### 8.4 Implied Evolution Path

When backend integration is added, the likely pattern would be:
1. Feature-specific API services replacing `MockDataService` calls
2. Optional feature-level state with signals or RxJS `BehaviorSubject`
3. Global auth/session state already partially in place via `AuthService`

---

## 9. Styling Approach

### 9.1 Technology Stack

| Aspect | Choice |
|--------|--------|
| **Preprocessor** | SCSS (configured in `angular.json` schematics) |
| **Global styles** | Single `src/styles.scss` entry |
| **Component styles** | Co-located `.scss` per component/page |
| **CSS framework** | None (no Bootstrap, Tailwind, Angular Material, PrimeNG) |
| **Design system** | Custom CSS custom properties (design tokens) |

### 9.2 Design Tokens (`styles.scss`)

```scss
:root {
  --ims-primary: #2563eb;
  --ims-primary-dark: #1d4ed8;
  --ims-primary-light: #eff6ff;
  --ims-bg: #f8fafc;
  --ims-surface: #ffffff;
  --ims-surface-muted: #f1f5f9;
  --ims-text: #0f172a;
  --ims-text-muted: #64748b;
  --ims-border: #e2e8f0;
  --ims-success: #16a34a;
  --ims-warning: #d97706;
  --ims-danger: #dc2626;
  --ims-info: #0284c7;
}
```

### 9.3 Styling Conventions

- **BEM-like** class naming within components (observed in component SCSS files).
- **System font stack:** `'Segoe UI', system-ui, -apple-system, sans-serif`.
- **No global component style library** — each shared component owns its styles.
- **No `ViewEncapsulation` overrides** observed; default emulated encapsulation.
- **No dark mode** theming.
- **No SCSS partials/mixins** shared across components (tokens only at global level).
- **Style budgets** configured: 4 kB warning / 8 kB error per component style (production).

### 9.4 Layout Architecture

- `AppShellComponent` provides the authenticated layout frame (header + dual nav + content + footer).
- Sign-in page renders outside the shell (full-page layout).
- Responsive behavior is component-local; no global breakpoint variables defined.

---

## 10. Third-Party Libraries

### 10.1 Production Dependencies

| Package | Version | Usage |
|---------|---------|-------|
| `@angular/common` | ^19.2.0 | Common directives, pipes |
| `@angular/compiler` | ^19.2.0 | JIT/AOT compilation |
| `@angular/core` | ^19.2.0 | Framework core, signals, DI |
| `@angular/forms` | ^19.2.0 | `FormsModule` (template-driven forms) |
| `@angular/platform-browser` | ^19.2.0 | DOM rendering |
| `@angular/platform-browser-dynamic` | ^19.2.0 | Bootstrap (dev) |
| `@angular/router` | ^19.2.0 | Routing, lazy loading, guards |
| `rxjs` | ~7.8.0 | Reactive primitives (framework-level) |
| `tslib` | ^2.3.0 | TypeScript helpers |
| `zone.js` | ~0.15.0 | Change detection |

### 10.2 Development Dependencies

| Package | Version | Usage |
|---------|---------|-------|
| `@angular/cli` | ^19.2.27 | CLI tooling |
| `@angular-devkit/build-angular` | ^19.2.27 | Build pipeline (esbuild/Vite-based) |
| `@angular/compiler-cli` | ^19.2.0 | AOT compiler |
| `typescript` | ~5.7.2 | Language |
| `jasmine-core` | ~5.6.0 | Test framework |
| `karma` + plugins | ~6.4.0 | Test runner |

### 10.3 Notable Absences

The following common Angular ecosystem libraries are **not installed**:

| Category | Missing Libraries |
|----------|-------------------|
| UI frameworks | Angular Material, PrimeNG, NG-ZORRO, Spartan UI |
| CSS utilities | Tailwind CSS, Bootstrap |
| State management | NgRx, NGXS, Elf |
| HTTP utilities | No explicit `@angular/common/http` usage despite being part of `@angular/common` |
| Charts | Chart.js, ng2-charts, D3 |
| Tables | AG Grid, TanStack Table |
| Date/time | date-fns, dayjs, Luxon |
| i18n | `@angular/localize` (not configured) |
| Auth | OAuth/OIDC clients (Auth0, MSAL) |

### 10.4 Build Tooling

- **Builder:** `@angular-devkit/build-angular:application` (modern application builder)
- **Dev server:** Vite-based (Angular 19 default)
- **Output:** `dist/ims-frontend`
- **Strict TypeScript:** enabled (`strict: true`, strict templates)

---

## Appendix A: Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                         main.ts                                  │
│              bootstrapApplication(AppComponent)                  │
└────────────────────────────┬────────────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────────┐
│                      app.config.ts                               │
│   provideZoneChangeDetection │ provideRouter(routes)             │
└────────────────────────────┬────────────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────────┐
│                     app.routes.ts                                  │
│  ┌──────────────┐  ┌──────────────────────────────────────────┐ │
│  │ guestGuard   │  │ authGuard → AppShellComponent            │ │
│  │ /auth/sign-in│  │   └─ 49 lazy-loaded feature pages        │ │
│  └──────────────┘  └──────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
         │                              │
         ▼                              ▼
┌─────────────────┐          ┌─────────────────────────────────────┐
│  SignInPage     │          │  AppShellComponent (core/layout)  │
│  (features/auth)│          │  ├─ GlobalHeader                    │
└────────┬────────┘          │  ├─ MainNavigationBar             │
         │                   │  ├─ SecondaryNavigationPanel       │
         ▼                   │  ├─ <router-outlet> (features)     │
┌─────────────────┐          │  └─ FooterMetadataStrip            │
│  AuthService    │◄─────────┤                                     │
│  (signals)      │          └─────────────────────────────────────┘
└─────────────────┘                        │
                                           ▼
                              ┌─────────────────────────────────────┐
                              │  Feature Pages (50)                 │
                              │  └─ inject(MockDataService)         │
                              │     └─ shared/ui components         │
                              └─────────────────────────────────────┘
```

---

## Appendix B: Screen-to-Route Mapping (Complete)

| Screen ID | Route | Feature Page |
|-----------|-------|--------------|
| UI-001 | `/auth/sign-in` | SignInPage |
| UI-002 | `/home/operations` | OperationalDashboardPage |
| UI-003 | `/reports/executive-kpis` | ExecutiveKpiDashboardPage |
| UI-004 | `/notifications` | NotificationCenterPage |
| UI-005 | `/products/catalog` | ProductCatalogPage |
| UI-006 | `/products/import` | ProductImportWorkspacePage |
| UI-007 | `/locations` | LocationManagementPage |
| UI-008 | `/products/stock-policies` | StockPolicyManagementPage |
| UI-009 | `/products/abc-classification` | AbcClassificationPage |
| UI-010 | `/governance/policies` | GovernancePoliciesPage |
| UI-011 | `/procurement/suppliers` | SupplierManagementPage |
| UI-012 | `/procurement/purchase-orders` | PurchaseOrderManagementPage |
| UI-013 | `/procurement/requisitions` | PurchaseRequisitionManagementPage |
| UI-014 | `/procurement/inbound-delivery-planning` | InboundDeliveryPlanningPage |
| UI-015 | `/inbound/goods-receipts` | GoodsReceiptWorkbenchPage |
| UI-016 | `/inbound/discrepancies` | ReceiptDiscrepancyResolutionPage |
| UI-017 | `/inbound/put-away` | PutAwayWorkbenchPage |
| UI-018 | `/inbound/non-po-receipts` | NonPoReturnReceiptIntakePage |
| UI-019 | `/procurement/inbound-supply-tracking` | InboundSupplyTrackingPage |
| UI-020 | `/inventory/status-monitor` | InventoryStatusMonitorPage |
| UI-021 | `/inventory/availability` | InventoryAvailabilityInquiryPage |
| UI-022 | `/inventory/movement-history` | InventoryMovementHistoryPage |
| UI-023 | `/inventory/cycle-counts` | CycleCountWorkbenchPage |
| UI-024 | `/inventory/physical-counts` | PhysicalInventoryCountManagementPage |
| UI-025 | `/inventory/variances` | VarianceInvestigationApprovalPage |
| UI-026 | `/inventory/adjustments` | StockAdjustmentManagementPage |
| UI-027 | `/inventory/write-offs` | WriteOffAuthorizationPage |
| UI-028 | `/inventory/quarantine` | QuarantineHoldRegisterPage |
| UI-029 | `/inventory/shrinkage-obsolescence` | ShrinkageAnalysisPage |
| UI-030 | `/fulfillment/reservations` | OrderReservationWorkbenchPage |
| UI-031 | `/fulfillment/pick-pack-ship` | PickPackShipWorkbenchPage |
| UI-032 | `/fulfillment/partial-backorders` | PartialFulfillmentBackorderPage |
| UI-033 | `/fulfillment/exceptions` | FulfillmentExceptionManagementPage |
| UI-034 | `/fulfillment/order-status` | OrderFulfillmentStatusPage |
| UI-035 | `/fulfillment/split-planner` | MultiLocationSplitFulfillmentPlannerPage |
| UI-036 | `/procurement/low-stock-alerts` | LowStockAlertReviewPage |
| UI-037 | `/procurement/replenishment-planning` | ReplenishmentPlanningPage |
| UI-038 | `/transfers/requests` | TransferRequestPage |
| UI-039 | `/transfers/approvals` | TransferApprovalQueuePage |
| UI-040 | `/transfers/execution` | TransferExecutionTrackingPage |
| UI-041 | `/transfers/network-rebalancing` | NetworkRebalancingAnalysisPage |
| UI-042 | `/returns/authorizations` | ReturnAuthorizationManagementPage |
| UI-043 | `/returns/inspection-disposition` | ReturnInspectionDispositionPage |
| UI-044 | `/reports/operational` | OperationalReportsAnalyticsPage |
| UI-045 | `/reports/valuation-reconciliation` | InventoryValuationReconciliationPage |
| UI-046 | `/reports/promotional-readiness` | PromotionalStockReadinessPage |
| UI-047 | `/reports/audit-workspace` | AuditControlReviewWorkspacePage |
| UI-048 | `/reports/audit-trail` | AuditTrailQueryPage |
| UI-049 | `/admin/users` | UserAccountManagementPage |
| UI-050 | `/admin/roles-access` | RoleAccessControlAdministrationPage |

---

## Appendix C: Key Files Reference

| File | Role |
|------|------|
| `src/main.ts` | Application bootstrap |
| `src/app/app.config.ts` | Root providers |
| `src/app/app.routes.ts` | Complete routing table |
| `src/app/app.component.ts` | Root router outlet |
| `src/app/core/guards/auth.guard.ts` | Auth & guest guards |
| `src/app/core/services/auth.service.ts` | Session management |
| `src/app/core/services/mock-data.service.ts` | Mock data layer |
| `src/app/core/models/navigation.model.ts` | Navigation configuration |
| `src/app/core/layout/app-shell/app-shell.component.ts` | Authenticated layout shell |
| `src/styles.scss` | Global design tokens & resets |
| `scripts/scaffold-ims.mjs` | Project scaffolding generator |

---

*End of report.*
