# Technical Debt Report

**Project:** `ims-frontend` (Angular 19)  
**Review Perspective:** Senior Solution Architect  
**Related Reports:** Code Quality, Feature Coverage, Routing Assessment, API Consumption, Validation Coverage  
**Report Date:** July 7, 2026

---

## Executive Summary

| Metric | Value |
|--------|-------|
| Total source files (`src/app`) | ~343 |
| Behavioral uniqueness | Very low (~5 distinct patterns) |
| Test files | 3 (0.9% of TS files) |
| API / HTTP layer | Absent |
| Shared components (functional) | ~7 of 60 (~12%) |
| Estimated remediation effort | **16–24 person-weeks** to reach MVP-ready architecture |
| **Overall technical debt severity** | **High** |

The codebase exhibits **structural completeness with behavioral emptiness**: the folder tree and component inventory suggest a mature IMS application, but implementation depth is concentrated in routing, shell layout, and static mocks. Debt is **architectural and compounding** — each new screen added in the current pattern increases merge conflict surface, mock service size, and integration cost without delivering business value.

### Debt Severity by Category

| Category | High | Medium | Low | Dominant risk |
|----------|------|--------|-----|---------------|
| Technical debt | 8 | 9 | 4 | Mock layer blocks API migration |
| Architectural issues | 7 | 6 | 3 | Missing facade/data-access layers |
| Duplicate components / code | 4 | 3 | 2 | 48 cloned page scaffolds |
| Tight coupling | 6 | 4 | 2 | Pages → `MockDataService` |
| Separation of concerns | 7 | 5 | 2 | Auth + routing + credentials in one service |
| Performance risks | 2 | 5 | 3 | No OnPush; root mock bundle |
| Refactoring opportunities | — | — | — | 12 prioritized refactors below |

---

## Debt Register (Prioritized)

| ID | Issue | Category | Priority | Effort | Risk if unaddressed |
|----|-------|----------|----------|--------|---------------------|
| TD-001 | No HTTP client, API services, or environment config | Architecture | **High** | M | Cannot integrate backend; all features remain mock |
| TD-002 | `MockDataService` god object (281 LOC, 50 screens) | Coupling / SoC | **High** | M | Every API migration touches one file; no domain isolation |
| TD-003 | 48 identical feature page scaffolds | Duplication | **High** | S | Linear maintenance cost per screen |
| TD-004 | 43 shared components are non-functional stubs | Technical debt | **High** | L | False sense of completeness; wasted bundle/metadata |
| TD-005 | No facade / repository abstraction layer | Architecture | **High** | L | Pages cannot swap data sources; violates DIP |
| TD-006 | Demo auth with hardcoded users in `AuthService` | Coupling / Security | **High** | M | Production auth requires rewrite; security exposure if shipped |
| TD-007 | No permission or SoD guards | Architecture | **High** | M | BRD compliance failure; unauthorized route access |
| TD-008 | Monolithic `app.routes.ts` (364 lines, 49 siblings) | Architecture | **High** | S | Merge conflicts; no feature ownership boundaries |
| TD-009 | Zero child/detail routes (~35 missing) | Architecture | **High** | L | Workflows cannot be built on current routing model |
| TD-010 | No automated tests on pages/components (3 specs total) | Technical debt | **High** | L | Regressions undetected during refactor |
| TD-011 | Feature pages use `unknown` for all view data | Technical debt | **Medium** | M | No type-safe refactoring; IDE assistance disabled |
| TD-012 | No `ChangeDetectionStrategy.OnPush` anywhere | Performance | **Medium** | S | CD overhead scales with 110+ components |
| TD-013 | Router subscription without `takeUntilDestroyed` | Technical debt | **Medium** | S | Memory leak pattern if shell lifecycle changes |
| TD-014 | Hardcoded notification/task counts in shell widgets | Coupling | **Medium** | S | UI lies to users; blocks real alert integration |
| TD-015 | Sign-in pre-fills demo credentials in component | Security / Debt | **Medium** | S | Credential leakage in production builds |
| TD-016 | Template-driven sign-in (`ngModel`) not reactive forms | Technical debt | **Medium** | S | Validation architecture inconsistent with 49 form specs |
| TD-017 | No path aliases (`@core`, `@shared`) | Technical debt | **Medium** | S | Fragile `../../../` imports across 48+ pages |
| TD-018 | `angular.json` prefix `app` vs. `ims-` selectors | Technical debt | **Low** | S | Generator inconsistency |
| TD-019 | Wildcard route silently redirects to dashboard | Architecture | **Medium** | S | Masks 404s and broken deep links |
| TD-020 | Secondary nav active-module heuristic is brittle | Technical debt | **Medium** | S | Wrong nav highlight for `/reports/*` under Home |
| TD-021 | No feature `loadChildren` bundles | Performance / Arch | **Medium** | M | Flat route tree; missed chunk grouping |
| TD-022 | `json` pipe for debug mock preview on 48 pages | Performance | **Low** | S | Unnecessary serialization on change detection |
| TD-023 | Empty `ngOnInit` on sign-in page | Technical debt | **Low** | S | Dead code smell |
| TD-024 | No barrel exports for shared UI | Technical debt | **Low** | S | Verbose import paths |
| TD-025 | `SessionContextBadge` not wired to `AuthService` | SoC | **Medium** | S | Session display disconnected from state |
| TD-026 | Global search input with no action handler | Technical debt | **Medium** | S | Dead UI control in production shell |
| TD-027 | Governance audit screens under `/reports` not `/governance` | Architecture | **Medium** | M | IA drift from Navigation Map |
| TD-028 | No error interceptor / API error mapping | Architecture | **Medium** | M | Cannot implement spec error envelopes |
| TD-029 | Duplicate Executive KPI in Home + Reports nav | Duplication | **Low** | S | Navigation confusion |
| TD-030 | 48 duplicate `.page.scss` mock-preview blocks | Duplication | **Medium** | S | Style drift across pages |

**Effort key:** S = hours–2 days, M = 3–10 days, L = 2+ weeks

---

## 1. Technical Debt

Technical debt is **debt incurred by expedient scaffolding** that must be repaid before MVP delivery.

### High Priority

| ID | Debt item | Evidence | Repayment action |
|----|-----------|----------|------------------|
| TD-004 | **Stub component inventory** | 46/46 shared templates use only `<ng-content>`; 0 `ControlValueAccessor`, 0 `output()` | Delete or implement incrementally; mark stubs `@deprecated` in README |
| TD-006 | **Demo authentication** | `AuthService` embeds `demoUsers` map; password check `length >= 4` | Extract `AuthApiService`; environment-gate demo provider |
| TD-010 | **Test debt** | 3 spec files; 0 page tests; 0 component tests; 0 guard tests | Add facade/guard tests first; smoke test top 10 routes |
| TD-002 | **Central mock datastore** | All UI-001–UI-050 keys in one `screenData` object | Split per feature; inject via `SCREEN_DATA` tokens |

### Medium Priority

| ID | Debt item | Evidence | Repayment action |
|----|-----------|----------|------------------|
| TD-011 | **Untyped view models** | `data: unknown = null` on every scaffold page | Introduce per-screen interfaces in `features/*/models/` |
| TD-016 | **Forms inconsistency** | Sign-in uses `FormsModule`; spec defines 49 reactive forms | Standardize on `ReactiveFormsModule` + shared field wrapper |
| TD-014 | **Hardcoded UI state** | `notificationCount = 12`, `pendingCount = 15`, static task routes | `NotificationFacade` with signals from API-158 |
| TD-015 | **Pre-filled credentials** | `email = 'admin@ims.local'`, `password = 'demo'` in `SignInPage` | Clear defaults; dev-only helper behind `isDevMode()` |
| TD-026 | **Non-functional global search** | `GlobalSearchBarComponent.query` bound but never submitted | Wire to route or remove until F-020 implemented |

### Low Priority

| ID | Debt item | Evidence | Repayment action |
|----|-----------|----------|------------------|
| TD-022 | **Debug `json` pipe in production templates** | 48 pages render `<pre>{{ data \| json }}</pre>` | Replace with real UI; gate debug panel behind dev flag |
| TD-023 | **Empty lifecycle hooks** | `SignInPage.ngOnInit(): void {}` | Remove or use for session redirect |
| TD-018 | **CLI prefix mismatch** | `"prefix": "app"` in `angular.json`; 111 `ims-` selectors | Set prefix to `ims` |

---

## 2. Architectural Issues

Compared to `SRS/Frontend Architecture/Frontend-Architecture-Mapping.md`.

### High Priority

| ID | Issue | Current state | Target state |
|----|-------|---------------|--------------|
| TD-001 | **No data-access layer** | 0 `HttpClient`, 0 `*ApiService`, 0 environments | `provideHttpClient`, interceptors, per-domain API services |
| TD-005 | **No application/facade layer** | Pages call `MockDataService` directly | `*Facade` orchestrates loading, commands, error state |
| TD-007 | **Security architecture incomplete** | `authGuard` only; no `permissionGuard`, no action-level auth | Route `data.permissions`; `AuthorizationService` |
| TD-008 | **Flat routing architecture** | Single `app.routes.ts` with 49 children | Feature `*.routes.ts` + `loadChildren` per domain |
| TD-009 | **No workflow routing model** | List routes only | Parent/child routes with `:id`, `/new`, nested paths |

### Medium Priority

| ID | Issue | Detail |
|----|-------|--------|
| TD-019 | **Fault masking** | `**` → `home/operations` hides broken URLs |
| TD-027 | **Module boundary drift** | Audit under `reports/` feature folder vs. Governance in nav |
| TD-028 | **No cross-cutting HTTP concerns** | Missing auth interceptor, error mapper, loading interceptor |
| TD-021 | **Shallow lazy loading** | `loadComponent` per page but no feature chunk grouping |
| — | **No state management strategy** | Spec recommends signals + feature stores; only auth uses signals |
| — | **No DTO/mapper layer** | API shapes cannot be adapted to view models |

### Low Priority

| ID | Issue | Detail |
|----|-------|--------|
| TD-024 | **No public API surface per feature** | Features export pages only; no barrel boundaries |
| — | **No `withComponentInputBinding()`** | Route params not bound to `@Input()` |
| — | **No preloading strategy** | All chunks load on demand only |

### Architecture Gap Diagram

```text
SPEC (Clean Architecture)          CURRENT IMPLEMENTATION

features/                          features/
  ui/ (pages)          ✓             ui/ (*-page only)
  application/ (facades) ✗         — MISSING
  data-access/           ✗         — MISSING
    services/            ✗         — MISSING
    dto/                 ✗         — MISSING
    mappers/             ✗         — MISSING

core/                              core/
  guards/              ✓ partial    guards/ (auth only)
  http/                ✗           — MISSING
  services/            ▓           auth + mock only
```

---

## 3. Duplicate Components

### High Priority

| Duplication | Count | Lines (est.) | Priority | Remediation |
|-------------|-------|--------------|----------|-------------|
| **Feature page TypeScript** | 48 clones | ~960 | **High** | `MockScreenPageBase` or `ScreenScaffoldComponent` |
| **Feature page HTML** | 48 clones | ~480 | **High** | Single scaffold template with content projection |
| **Feature page SCSS** | 48 clones | ~576 | **High** | Shared `.mock-preview` in global or scaffold |

### Medium Priority

| Duplication | Detail | Priority |
|-------------|--------|----------|
| **Shared stub components** | 43 components with identical structure: wrapper div + `ng-content` | **Medium** | Consolidate to `ContentSlotComponent` or generate from manifest |
| **Breadcrumb definitions** | Inline `[{ label: 'Home', route: '...' }, ...]` per page | **Medium** | `BreadcrumbService` from route `data` |
| **Import blocks** | Same 4-line import pattern × 48 pages | **Medium** | Path aliases + scaffold component |

### Low Priority

| Duplication | Detail | Priority |
|-------------|--------|----------|
| TD-029 | Executive KPI linked from Home and Reports nav children | **Low** | Single canonical nav entry |
| — | `PageTitleBar` + `BreadcrumbTrail` imported together on every page | **Low** | Bundled in `ScreenScaffoldComponent` |

### Not Duplicate (Clarification)

The 60 shared component **files** are not duplicates of each other — they are **unique names with duplicate implementation pattern** (empty shells). The debt is **homogeneous stub proliferation**, not copy-paste of the same component.

---

## 4. Tight Coupling

### High Priority

| Coupling | From | To | Impact |
|----------|------|-----|--------|
| TD-002 | 48 feature pages | `MockDataService` (concrete) | Cannot introduce APIs without editing every page |
| TD-006 | `AuthService` | `Router` + `sessionStorage` + credential map | Auth redesign ripples through service |
| TD-006 | `SignInPage` | `AuthService` + `Router` + form state | No `AuthFacade`; untestable orchestration |
| — | All authenticated routes | `AppShellComponent` (eager) | Shell always loaded; hard to test pages in isolation |
| — | Navigation model | Static `MAIN_NAVIGATION` array | Cannot filter by role without editing central config |

### Medium Priority

| Coupling | Detail |
|----------|--------|
| TD-014 | `GlobalHeaderComponent` hardcodes `notificationCount`; not driven by `AuthService` or alert service |
| TD-020 | `SecondaryNavigationPanel` embeds route-matching logic tied to `MAIN_NAVIGATION` shape |
| — | `UserMenuComponent` calls `auth.signOut()` which navigates internally — menu coupled to auth navigation |
| — | Dashboard `quickActions` and task widget routes hardcoded in component TS |

### Low Priority

| Coupling | Detail |
|----------|--------|
| — | `MockDataService` helper methods (`getProducts`, `getLocations`) reach into specific UI keys — cross-screen coupling within mock layer |
| — | Feature pages import layout components via deep relative paths — compile-time coupling to folder depth |

### Dependency Inversion Violations

```text
CURRENT ( tightly coupled ):
  ProductCatalogPage → MockDataService → inline JSON

TARGET ( loosely coupled ):
  ProductCatalogPage → ProductCatalogFacade → ProductRepository (interface)
                                              ├── MockProductRepository (dev)
                                              └── HttpProductRepository (prod)
```

---

## 5. Poor Separation of Concerns

### High Priority

| Violation | Location | Concern mixed |
|-----------|----------|---------------|
| TD-002 | `MockDataService` | Data + all domain knowledge + screen registry |
| TD-006 | `AuthService` | Authentication + session persistence + navigation side-effect |
| TD-005 | Feature pages | Presentation + data loading + screen metadata |
| — | `app.routes.ts` | Routing + no route metadata (title, permissions, breadcrumbs) |
| — | No domain services | Business rules (BR-001–032) have no home in frontend |

### Medium Priority

| Violation | Location | Concern mixed |
|-----------|----------|---------------|
| TD-020 | `SecondaryNavigationPanel` | Presentation + route parsing logic |
| — | `SignInPage` | View + validation + auth command + routing |
| TD-025 | `SessionContextBadge` | Presentational component with `@Input` but parent doesn't bind auth state |
| — | `OperationalDashboardPage` | Layout + mock data shaping + hardcoded quick actions |

### Low Priority

| Violation | Detail |
|----------|--------|
| — | `AppComponent` holds unused `title` property |
| TD-023 | Empty `ngOnInit` implies unfinished separation |

### Concern Mapping (Target)

| Concern | Should live in | Currently lives in |
|---------|----------------|-------------------|
| Screen metadata (title, UI-ID) | Route `data` or resolver | Each page class |
| Data fetching | Facade | Page `ngOnInit` |
| Auth state | `SessionService` (signals) | `AuthService` + `sessionStorage` |
| Navigation config | `NavigationService` (role-filtered) | Static `navigation.model.ts` |
| Business rules | `PolicyService` / validators | Nowhere |

---

## 6. Performance Risks

### High Priority

| Risk | Detail | When it hurts |
|------|--------|---------------|
| — | **No API caching strategy planned** | When facades added without query deduplication — duplicate calls across widgets |

### Medium Priority

| ID | Risk | Evidence | Mitigation |
|----|------|----------|------------|
| TD-012 | **Default change detection everywhere** | 0 `OnPush` usages | Add `OnPush` to all presentational components |
| TD-002 | **Root-provided mock bundle grows** | `MockDataService` `providedIn: 'root'` loads all screen JSON upfront | Feature-scoped providers or lazy mock loaders |
| TD-021 | **49 route definitions in main chunk metadata** | Large `app.routes.ts` parsed at bootstrap | Feature route modules |
| — | **`DataTable` without virtualization** | Simple `*ngFor` over rows | Virtual scroll when real data (12k+ SKUs) arrives |
| TD-022 | **`json` pipe in templates** | Serializes on every CD cycle | Remove before production |

### Low Priority

| Risk | Detail |
|------|--------|
| TD-013 | Router events subscription without teardown — low risk while shell is permanent |
| — | No image/asset optimization concerns — minimal assets today |
| — | No service worker / caching — acceptable for admin SPA initially |
| — | Zone.js default — acceptable; consider zoneless later |

### Performance Posture Summary

| Area | Current | Risk level |
|------|---------|------------|
| Bundle splitting (route level) | Good | Low |
| Bundle splitting (feature level) | Missing | Medium |
| Change detection | Default everywhere | Medium |
| List rendering | No virtualization | Medium (future) |
| Network | N/A (no HTTP) | High when APIs added without plan |

---

## 7. Refactoring Opportunities

Prioritized refactors with highest ROI first.

### Tier 1 — Foundation (do before feature work)

| # | Refactor | Priority | Effort | Addresses |
|---|----------|----------|--------|-----------|
| R-01 | Add `provideHttpClient`, environments, auth/error interceptors | **High** | M | TD-001, TD-028 |
| R-02 | Introduce `ScreenScaffoldComponent` + migrate 48 pages | **High** | M | TD-003, TD-030 |
| R-03 | Split `app.routes.ts` into feature `*.routes.ts` with `loadChildren` | **High** | M | TD-008, TD-021 |
| R-04 | Define `*Facade` + repository interface per first MVP feature (e.g. inbound) | **High** | L | TD-005, TD-002 |
| R-05 | Replace `AuthService` with session + auth API adapter | **High** | M | TD-006 |

### Tier 2 — Security and routing depth

| # | Refactor | Priority | Effort | Addresses |
|---|----------|----------|--------|-----------|
| R-06 | Add `permissionGuard` + route `data.permissions` | **High** | M | TD-007 |
| R-07 | Register child routes for top 5 workflows | **High** | L | TD-009 |
| R-08 | `BreadcrumbService` driven by router state | **Medium** | S | Duplication, TD-020 |
| R-09 | Fix wildcard → `NotFoundPage` | **Medium** | S | TD-019 |
| R-10 | `takeUntilDestroyed` on router subscription | **Medium** | S | TD-013 |

### Tier 3 — Component honesty and quality

| # | Refactor | Priority | Effort | Addresses |
|---|----------|----------|--------|-----------|
| R-11 | Audit shared components: implement or remove 43 stubs | **High** | L | TD-004 |
| R-12 | Add `OnPush` to all shared/presentational components | **Medium** | S | TD-012 |
| R-13 | `tsconfig` path aliases (`@core`, `@shared`, `@features`) | **Medium** | S | TD-017 |
| R-14 | Typed view models per feature | **Medium** | M | TD-011 |
| R-15 | Reactive forms + `ims-form-field` wrapper | **Medium** | M | TD-016 |

### Tier 4 — Polish

| # | Refactor | Priority | Effort | Addresses |
|---|----------|----------|--------|-----------|
| R-16 | `NotificationFacade` replacing hardcoded counts | **Medium** | S | TD-014 |
| R-17 | Wire `SessionContextBadge` to auth signals | **Medium** | S | TD-025 |
| R-18 | Role-filtered `NavigationService` | **Medium** | M | Coupling |
| R-19 | Shared UI barrel exports | **Low** | S | TD-024 |
| R-20 | Set CLI prefix to `ims` | **Low** | S | TD-018 |

---

## Repayment Roadmap

### Sprint 1–2 (Stabilize architecture)

```text
R-01 → R-03 → R-02 → R-05 → R-10
```

**Exit criteria:** HTTP layer exists; pages use scaffold; routes split by feature; auth uses API adapter; no new page clones.

### Sprint 3–5 (First MVP vertical slice)

```text
R-04 (inbound) → R-06 → R-07 (goods receipt routes) → R-11 (queue, line-item, step components only)
```

**Exit criteria:** Goods receipt workflow end-to-end with real API; permission guard on inbound routes.

### Sprint 6–8 (Scale pattern)

```text
R-04 (fulfillment, inventory) → R-14 → R-15 → R-12 → R-16
```

**Exit criteria:** 3+ domains on facade pattern; shared forms functional; OnPush default for new components.

---

## Debt Metrics (Track Over Time)

| Metric | Baseline (now) | Target (MVP) |
|--------|----------------|--------------|
| Pages injecting `MockDataService` directly | 48 | 0 |
| Shared stub components (ng-content only) | 43 | ≤10 |
| Spec files | 3 | ≥50 |
| `app.routes.ts` lines | 364 | <80 (delegates to features) |
| `MockDataService` lines | 281 | 0 (replaced by fixtures/MSW) |
| Routes with `permissionGuard` | 0 | 49 |
| Child/detail routes | 0 | ≥20 |
| Components with `OnPush` | 0 | 100% presentational |

---

## Risk Assessment: If Debt Is Not Repaid

| Scenario | Consequence | Likelihood |
|----------|-------------|------------|
| Continue adding screens in current pattern | +5 files per screen, +50 LOC mock data; integration cost grows exponentially | **Certain** |
| Connect APIs without facades | 48 page rewrites in one release | **High** |
| Ship demo auth to production | Security incident; failed compliance | **High** if undetected |
| Implement features on stub components | Rework when real component API differs | **High** |
| Skip tests during refactor | Regressions in routing/auth during MVP crunch | **Medium** |
| Ignore OnPush until late | Performance firefighting with real data volumes | **Medium** |

---

## Related Reports

| Report | Path |
|--------|------|
| Code Quality Report | `gap_frontend/Code-Quality-Report.md` |
| Feature Coverage Matrix | `gap_frontend/Feature-Coverage-Matrix.md` |
| Routing Assessment Report | `gap_frontend/Routing-Assessment-Report.md` |
| API Consumption Matrix | `gap_frontend/API-Consumption-Matrix.md` |
| Frontend Architecture Mapping | `SRS/Frontend Architecture/Frontend-Architecture-Mapping.md` |

---

## Conclusion

Technical debt in `ims-frontend` is **front-loaded and architectural**, not cosmetic. The highest-priority repayments are:

1. **Stop scaffold duplication** (`ScreenScaffoldComponent`)
2. **Introduce HTTP + facade boundaries** (eliminate `MockDataService` coupling)
3. **Split routing and add guards** (feature ownership + security)
4. **Resolve stub component honesty** (implement or remove)
5. **Add tests before vertical-slice work** (protect refactors)

Deferring these while building more screens will **increase repayment cost superlinearly**. The recommended approach is a **2-sprint architecture stabilization** before continuing MVP feature delivery.

---

*End of report.*
