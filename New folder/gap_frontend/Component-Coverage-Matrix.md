# Component Coverage Matrix

**Project:** IMS Frontend vs. Approved Component Inventory  
**Specification Source:** `SRS/Inventory-Management-System-SRS.md` (C-001–C-060)  
**Implementation Source:** `ims-frontend/src/app/shared/ui/`  
**Report Date:** July 7, 2026

---

## Executive Summary

| Metric | Value |
|--------|-------|
| Components in specification | 60 |
| Component files in codebase | 60 / 60 (100%) |
| Fully spec-compliant (**Yes** on responsibility) | 0 |
| Partially implemented (**Partial**) | 17 |
| Placeholder only (**No** on responsibility) | 43 |
| Components used in feature pages | 5 (+ 8 in app shell) |
| Components with `ControlValueAccessor` (form integration) | 0 |
| **Weighted average implementation** | **~28%** |

### Implementation Tiers

| Tier | Count | Description |
|------|-------|-------------|
| **T1 — Shell-integrated, functional** | 9 | App chrome and navigation; used in `AppShellComponent` / `GlobalHeaderComponent` |
| **T2 — Implemented UI, limited integration** | 8 | Render real markup; wired to 1–2 screens only |
| **T3 — API surface only** | 10 | `@Input()` declared; template is `ng-content` or ignores inputs |
| **T4 — Scaffold placeholder** | 33 | Empty wrapper with `ng-content`; no behavior |

### Cross-Cutting Architectural Gaps

- No shared component barrel (`shared/ui/index.ts`) for discoverability
- No `ControlValueAccessor` on form controls — cannot bind to `ReactiveFormsModule`
- No `@Output()` event contracts on workflow components (approve/reject, export, etc.)
- No CDK overlay/dialog service for `ConfirmationDialog`
- No accessibility patterns beyond basic `aria-label` on a few components
- No Storybook or component documentation
- 43 of 60 components are **never imported** outside their own file

---

## Assessment Methodology

### Field Definitions

| Field | Meaning |
|-------|---------|
| **Exists?** | Angular standalone component file present under `shared/ui/` |
| **Reusable?** | Architecturally reusable (standalone, domain-agnostic, in `shared/`) AND has a usable public API |
| **Correct responsibility?** | Implementation matches SRS purpose (not just filename) |
| **Completion %** | Weighted: structure (20%) + template behavior (40%) + inputs/outputs (20%) + variants (10%) + integration (10%) |

### Status Values

| Status | Criteria |
|--------|----------|
| **Yes** | ≥80% complete; correct responsibility; usable without parent filling all content |
| **Partial** | File exists; some behavior; major spec gaps |
| **No** | Placeholder only or responsibility mismatch |

---

## Master Matrix

| ID | Component Name | Angular Selector | Exists | Reusable | Responsibility | Completion |
|----|----------------|----------------|--------|----------|----------------|------------|
| C-001 | Global Header | `ims-global-header` | Yes | Partial | Partial | 62% |
| C-002 | Main Navigation Bar | `ims-main-navigation-bar` | Yes | Partial | Partial | 58% |
| C-003 | Secondary Navigation Panel | `ims-secondary-navigation-panel` | Yes | Yes | Partial | 55% |
| C-004 | Breadcrumb Trail | `ims-breadcrumb-trail` | Yes | Yes | Yes | 72% |
| C-005 | Page Title Bar | `ims-page-title-bar` | Yes | Yes | Partial | 60% |
| C-006 | Footer Metadata Strip | `ims-footer-metadata-strip` | Yes | Partial | Partial | 45% |
| C-007 | Global Search Bar | `ims-global-search-bar` | Yes | Partial | Partial | 35% |
| C-008 | Notification Icon and Inbox Trigger | `ims-notification-icon-inbox-trigger` | Yes | Partial | Partial | 48% |
| C-009 | User Menu | `ims-user-menu` | Yes | Partial | Partial | 42% |
| C-010 | Quick Action Tile | `ims-quick-action-tile` | Yes | Yes | Partial | 55% |
| C-011 | Task / Approval Shortcut Widget | `ims-task-approval-shortcut-widget` | Yes | Partial | Partial | 50% |
| C-012 | Filter Bar | `ims-filter-bar` | Yes | No | No | 12% |
| C-013 | Date Range Picker | `ims-date-range-picker` | Yes | No | No | 10% |
| C-014 | Search Results List | `ims-search-results-list` | Yes | No | No | 10% |
| C-015 | Saved Filter / View Selector | `ims-saved-view-selector` | Yes | No | No | 10% |
| C-016 | KPI Summary Card | `ims-kpi-summary-card` | Yes | Yes | Partial | 58% |
| C-017 | Status Badge | `ims-status-badge` | Yes | No | No | 18% |
| C-018 | Summary Statistic Strip | `ims-summary-statistic-strip` | Yes | No | No | 10% |
| C-019 | Data Table | `ims-data-table` | Yes | Partial | Partial | 38% |
| C-020 | Table Row Action Menu | `ims-table-row-action-menu` | Yes | No | No | 10% |
| C-021 | Detail Panel | `ims-detail-panel` | Yes | No | No | 10% |
| C-022 | Comparison Panel | `ims-comparison-panel` | Yes | No | No | 10% |
| C-023 | Record Metadata Block | `ims-record-metadata-block` | Yes | No | No | 10% |
| C-024 | Standard Form Section | `ims-standard-form-section` | Yes | No | No | 10% |
| C-025 | Field Group Header | `ims-field-group-header` | Yes | Partial | Partial | 25% |
| C-026 | Text Input | `ims-text-input` | Yes | No | No | 15% |
| C-027 | Text Area / Notes Field | `ims-text-area-notes-field` | Yes | No | No | 12% |
| C-028 | Dropdown / Select Control | `ims-dropdown-select-control` | Yes | No | No | 15% |
| C-029 | Checkbox Group | `ims-checkbox-group` | Yes | No | No | 10% |
| C-030 | Radio Group / Segmented Choice | `ims-radio-group-segmented-choice` | Yes | No | No | 10% |
| C-031 | Number Input | `ims-number-input` | Yes | No | No | 12% |
| C-032 | Date / Date-Time Field | `ims-date-field` | Yes | No | No | 12% |
| C-033 | File Upload Control | `ims-file-upload-control` | Yes | No | No | 10% |
| C-034 | Validation Message Block | `ims-validation-message-block` | Yes | No | No | 18% |
| C-035 | Read-Only Review Form | `ims-read-only-review-form` | Yes | No | No | 10% |
| C-036 | Line Item Editor | `ims-line-item-editor` | Yes | No | No | 10% |
| C-037 | Queue List | `ims-queue-list` | Yes | No | No | 15% |
| C-038 | Step Progress Indicator | `ims-step-progress-indicator` | Yes | No | No | 18% |
| C-039 | Approval Decision Panel | `ims-approval-decision-panel` | Yes | No | No | 10% |
| C-040 | Status Timeline / History | `ims-status-timeline` | Yes | No | No | 10% |
| C-041 | Alert Detail Card | `ims-alert-detail-card` | Yes | No | No | 10% |
| C-042 | Recommendation Card | `ims-recommendation-card` | Yes | No | No | 10% |
| C-043 | Confirmation Dialog | `ims-confirmation-dialog` | Yes | No | No | 8% |
| C-044 | Success / Warning / Error Banner | `ims-success-warning-error-banner` | Yes | Yes | Partial | 65% |
| C-045 | Report Viewer | `ims-report-viewer` | Yes | No | No | 10% |
| C-046 | Export Action Group | `ims-export-action-group` | Yes | No | No | 10% |
| C-047 | Trend Indicator | `ims-trend-indicator` | Yes | No | No | 18% |
| C-048 | Variance Highlight Block | `ims-variance-highlight-block` | Yes | No | No | 10% |
| C-049 | Drill-Down Link Group | `ims-drill-down-link-group` | Yes | No | No | 10% |
| C-050 | Role Assignment Widget | `ims-role-assignment-widget` | Yes | No | No | 10% |
| C-051 | Permission Matrix | `ims-permission-matrix` | Yes | No | No | 10% |
| C-052 | Access Scope Selector | `ims-access-scope-selector` | Yes | No | No | 10% |
| C-053 | Audit Record Viewer | `ims-audit-record-viewer` | Yes | No | No | 10% |
| C-054 | Evidence Attachment Panel | `ims-evidence-attachment-panel` | Yes | No | No | 10% |
| C-055 | Session / Context Badge | `ims-session-context-badge` | Yes | Yes | Partial | 55% |
| C-056 | Empty State Panel | `ims-empty-state-panel` | Yes | No | No | 20% |
| C-057 | Loading State / Skeleton | `ims-loading-skeleton` | Yes | No | No | 10% |
| C-058 | Bulk Selection Toolbar | `ims-bulk-selection-toolbar` | Yes | No | No | 12% |
| C-059 | Toggle / Switch Control | `ims-toggle-switch-control` | Yes | No | No | 15% |
| C-060 | Tabs / Segmented Content Switcher | `ims-tabs-segmented-content-switcher` | Yes | No | No | 15% |

---

## Per-Component Detail

### Global Layout Components (C-001–C-006)

#### C-001 — Global Header
| Field | Assessment |
|-------|------------|
| **Exists?** | Yes — `shared/ui/layout/global-header/` |
| **Reusable?** | Partial — standalone and shell-level, but hard-wires child components and `AuthService` |
| **Correct responsibility?** | Partial — provides brand, search, notifications, user menu, session badge; missing environment indicator, help link, header variants (executive/admin/unauthenticated) |
| **Missing features** | Environment badge; help link; role-based header variant; unauthenticated simplified header for UI-001; tasks shortcut in header |
| **Refactoring recommendations** | Extract header composition into a configurable `HeaderConfig` input; inject `NotificationCountService` instead of hardcoded `notificationCount = 12`; add `@Input() variant: 'operational' \| 'executive' \| 'admin' \| 'guest'` |
| **Used in** | `AppShellComponent` (global) |

#### C-002 — Main Navigation Bar
| Field | Assessment |
|-------|------------|
| **Exists?** | Yes — `shared/ui/layout/main-navigation-bar/` |
| **Reusable?** | Partial — reads static `MAIN_NAVIGATION`; no role filtering |
| **Correct responsibility?** | Partial — renders 12 top-level modules with `routerLinkActive`; missing collapsed menu, role-filtered items, icon support |
| **Missing features** | Role-based visibility; collapsed/responsive menu; module icons from `NavItem.icon`; keyboard navigation |
| **Refactoring recommendations** | Inject `NavigationService` that filters `MAIN_NAVIGATION` by user permissions; add `@Input() collapsed`; map `icon` field to SVG/icon set |
| **Used in** | `AppShellComponent` |

#### C-003 — Secondary Navigation Panel
| Field | Assessment |
|-------|------------|
| **Exists?** | Yes — `shared/ui/layout/secondary-navigation-panel/` |
| **Reusable?** | Yes — route-aware module detection; no feature coupling |
| **Correct responsibility?** | Partial — shows child routes for active module; missing accordion/tabs variants; module matching logic is fragile |
| **Missing features** | Horizontal tabs variant; accordion sections; robust route-to-module resolver; hide when no children |
| **Refactoring recommendations** | Replace URL string-matching with `Router` route `data.module` or a `NavigationResolverService`; support `@Input() layout: 'sidebar' \| 'tabs'` |
| **Used in** | `AppShellComponent` |

#### C-004 — Breadcrumb Trail
| Field | Assessment |
|-------|------------|
| **Exists?** | Yes — `shared/ui/layout/breadcrumb-trail/` |
| **Reusable?** | Yes — pure presentational; `@Input() items` array |
| **Correct responsibility?** | Yes — hierarchical trail with links and current-item styling; matches spec variants for standard breadcrumb |
| **Missing features** | Record ID crumb variant; action-state crumb; auto-generation from router (currently manual per page) |
| **Refactoring recommendations** | Add optional `BreadcrumbService` to derive crumbs from route `data.breadcrumb`; support `{{ recordId }}` template in final crumb |
| **Used in** | All 49 authenticated feature pages (manual configuration) |

#### C-005 — Page Title Bar
| Field | Assessment |
|-------|------------|
| **Exists?** | Yes — `shared/ui/layout/page-title-bar/` |
| **Reusable?** | Yes — `title`, `subtitle`, `[actions]` content projection |
| **Correct responsibility?** | Partial — title/subtitle present; missing status badge slot, filter controls variant, primary CTA pattern |
| **Missing features** | `@Input() status` with `StatusBadge` integration; built-in primary action button; filter controls in title bar |
| **Refactoring recommendations** | Add `@Input() statusBadge`; document `[actions]` slot convention; create `PageTitleBarActionsDirective` for consistent CTA placement |
| **Used in** | All 49 authenticated feature pages |

#### C-006 — Footer Metadata Strip
| Field | Assessment |
|-------|------------|
| **Exists?** | Yes — `shared/ui/layout/footer-metadata-strip/` |
| **Reusable?** | Partial — hardcoded version and refresh timestamp |
| **Correct responsibility?** | Partial — shows version and refresh time; not connected to actual data refresh events |
| **Missing features** | `@Input()` for record audit metadata; dynamic last-refresh from parent; report footer variant; security notice (UI-001) |
| **Refactoring recommendations** | Accept `@Input() lastRefresh: Date` and `@Input() metadata: RecordMetadata`; emit refresh events from page facades |
| **Used in** | `AppShellComponent` |

---

### Navigation and Utility Components (C-007–C-011)

#### C-007 — Global Search Bar
| Field | Assessment |
|-------|------------|
| **Exists?** | Yes — `shared/ui/navigation/global-search-bar/` |
| **Reusable?** | Partial — local `query` only; no search service |
| **Correct responsibility?** | Partial — renders search input; does not search, autocomplete, or navigate |
| **Missing features** | Entity-type scoping; autocomplete results; advanced search modal; `@Output() search` event; keyboard shortcuts |
| **Refactoring recommendations** | Create `GlobalSearchFacade` with debounced query; emit `searchRequested`; integrate `SearchResultsList` as dropdown overlay |
| **Used in** | `GlobalHeaderComponent` |

#### C-008 — Notification Icon and Inbox Trigger
| Field | Assessment |
|-------|------------|
| **Exists?** | Yes — `shared/ui/navigation/notification-icon-inbox-trigger/` |
| **Reusable?** | Partial — `@Input() count` but parent passes hardcoded `12` |
| **Correct responsibility?** | Partial — badge + link to `/notifications`; missing inline shortcut variant |
| **Missing features** | Live unread count from service; compact task-alert widget variant; real-time updates |
| **Refactoring recommendations** | Inject `NotificationFacade` with `unreadCount` signal; replace emoji icon with accessible SVG |
| **Used in** | `GlobalHeaderComponent` |

#### C-009 — User Menu
| Field | Assessment |
|-------|------------|
| **Exists?** | Yes — `shared/ui/navigation/user-menu/` |
| **Reusable?** | Partial — coupled to `AuthService` |
| **Correct responsibility?** | Partial — avatar, name, sign-out; missing profile view, role/location display in menu, admin variant |
| **Missing features** | Profile link; role and location in dropdown; session details; keyboard/a11y for dropdown |
| **Refactoring recommendations** | Add menu items via `@Input() items: MenuItem[]`; show `SessionContextBadge` inside dropdown; use CDK Menu for accessibility |
| **Used in** | `GlobalHeaderComponent` |

#### C-010 — Quick Action Tile
| Field | Assessment |
|-------|------------|
| **Exists?** | Yes — `shared/ui/navigation/quick-action-tile/` |
| **Reusable?** | Yes — `@Input() label`, `@Input() route` |
| **Correct responsibility?** | Partial — navigation tile works; missing icon, KPI-linked, role-priority variants |
| **Missing features** | `@Input() icon`; `@Input() count` for KPI-linked tiles; role-based visibility |
| **Refactoring recommendations** | Add optional icon input; support `routerLink` + `queryParams` for contextual shortcuts |
| **Used in** | `OperationalDashboardPage` (UI-002) |

#### C-011 — Task / Approval Shortcut Widget
| Field | Assessment |
|-------|------------|
| **Exists?** | Yes — `shared/ui/navigation/task-approval-shortcut-widget/` |
| **Reusable?** | Partial — hardcoded task list and counts |
| **Correct responsibility?** | Partial — shows pending items with links; not driven by approval APIs |
| **Missing features** | Dynamic task feed from `TaskInboxService`; approvals vs. tasks variant; mixed workload mode |
| **Refactoring recommendations** | Accept `@Input() tasks: TaskSummary[]` or inject `PendingApprovalsFacade`; align counts with `API-106`, `API-123` |
| **Used in** | `OperationalDashboardPage` (UI-002) |

---

### Filter, Search, and Query Components (C-012–C-015)

#### C-012 — Filter Bar
| Field | Assessment |
|-------|------------|
| **Exists?** | Yes — `shared/ui/filters/filter-bar/` |
| **Reusable?** | No — empty `ng-content` wrapper |
| **Correct responsibility?** | No |
| **Missing features** | Filter field composition; apply/reset actions; expandable advanced filters; sticky behavior; `@Output() filterChange` |
| **Refactoring recommendations** | Implement as composable container with `@Input() filters: FilterDefinition[]` or content-projected filter slots; pair with form controls implementing `ControlValueAccessor` |
| **Used in** | Not used |

#### C-013 — Date Range Picker
| Field | Assessment |
|-------|------------|
| **Exists?** | Yes — `shared/ui/filters/date-range-picker/` |
| **Reusable?** | No — placeholder |
| **Correct responsibility?** | No |
| **Missing features** | Preset ranges (7d, 30d, QTD); custom from/to dates; `ControlValueAccessor`; single-period mode |
| **Refactoring recommendations** | Build on native `input[type=date]` pair or integrate lightweight date library; expose `DateRange` model with presets |
| **Used in** | Not used |

#### C-014 — Search Results List
| Field | Assessment |
|-------|------------|
| **Exists?** | Yes — `shared/ui/filters/search-results-list/` |
| **Reusable?** | No — placeholder |
| **Correct responsibility?** | No |
| **Missing features** | Result row template; selection; empty state; entity-type icons; `@Input() results` |
| **Refactoring recommendations** | Define `SearchResultItem` interface; use `@for` with configurable `itemTemplate`; integrate with C-007 |
| **Used in** | Not used |

#### C-015 — Saved Filter / View Selector
| Field | Assessment |
|-------|------------|
| **Exists?** | Yes — `shared/ui/filters/saved-view-selector/` |
| **Reusable?** | No — placeholder |
| **Correct responsibility?** | No |
| **Missing features** | Saved view dropdown; segmented button variant; persist views to `localStorage` or API |
| **Refactoring recommendations** | Implement as `select` or segmented control with `@Input() views: SavedView[]` and `@Output() viewSelected` |
| **Used in** | Not used |

---

### Data Display Components (C-016–C-023)

#### C-016 — KPI Summary Card
| Field | Assessment |
|-------|------------|
| **Exists?** | Yes — `shared/ui/display/kpi-summary-card/` |
| **Reusable?** | Yes — `@Input() label`, `value`, `trend` |
| **Correct responsibility?** | Partial — displays metric and trend color; missing target comparison, status semantics, executive variant |
| **Missing features** | `@Input() target`; `@Input() status: 'healthy' \| 'warning' \| 'critical'`; integrate C-047 `TrendIndicator`; alert count variant |
| **Refactoring recommendations** | Compose with `TrendIndicator` child; add RAG styling tokens; support `drillDownRoute` for C-049 integration |
| **Used in** | `OperationalDashboardPage` (UI-002) |

#### C-017 — Status Badge
| Field | Assessment |
|-------|------------|
| **Exists?** | Yes — `shared/ui/display/status-badge/` |
| **Reusable?** | No — `@Input() status` and `variant` declared but template ignores them (`ng-content` only) |
| **Correct responsibility?** | No — inputs not bound to template |
| **Missing features** | Render `{{ status }}` with variant CSS classes; stock/workflow/approval/audit status color maps |
| **Refactoring recommendations** | Fix template to use inputs; create `StatusBadgeVariant` enum aligned with domain statuses; remove `ng-content` or use for icon slot only |
| **Used in** | Not used |

#### C-018 — Summary Statistic Strip
| Field | Assessment |
|-------|------------|
| **Exists?** | Yes — `shared/ui/display/summary-statistic-strip/` |
| **Reusable?** | No — placeholder |
| **Correct responsibility?** | No |
| **Missing features** | Horizontal metric group; `@Input() stats: { label, value }[]` |
| **Refactoring recommendations** | Implement compact flex row of stat chips; reuse in workbenches (UI-015, UI-040) |
| **Used in** | Not used |

#### C-019 — Data Table
| Field | Assessment |
|-------|------------|
| **Exists?** | Yes — `shared/ui/tables/data-table/` |
| **Reusable?** | Partial — basic read-only table |
| **Correct responsibility?** | Partial — renders columns/rows; missing sort, filter, selection, pagination, row actions, sticky header |
| **Missing features** | Column sorting; row selection; pagination; `TableRowActionMenu` integration; expandable rows; empty/loading states |
| **Refactoring recommendations** | Define `TableColumn<T>` interface with `key`, `label`, `sortable`; add `@Output() rowSelected`; consider CDK Table for accessibility; compose C-020 and C-056 |
| **Used in** | Not used in feature pages |

#### C-020 — Table Row Action Menu
| Field | Assessment |
|-------|------------|
| **Exists?** | Yes — `shared/ui/tables/table-row-action-menu/` |
| **Reusable?** | No — placeholder |
| **Correct responsibility?** | No |
| **Missing features** | Kebab menu; `@Input() actions: RowAction[]`; permission-gated actions |
| **Refactoring recommendations** | Use CDK Menu; emit `@Output() actionSelected`; integrate as column in C-019 |
| **Used in** | Not used |

#### C-021 — Detail Panel
| Field | Assessment |
|-------|------------|
| **Exists?** | Yes — `shared/ui/display/detail-panel/` |
| **Reusable?** | No — placeholder |
| **Correct responsibility?** | No |
| **Missing features** | Right drawer / bottom panel layouts; open/close state; `@Input() record` |
| **Refactoring recommendations** | Implement slide-over panel with CDK Overlay; support list-detail pattern on catalog screens |
| **Used in** | Not used |

#### C-022 — Comparison Panel
| Field | Assessment |
|-------|------------|
| **Exists?** | Yes — `shared/ui/display/comparison-panel/` |
| **Reusable?** | No — placeholder |
| **Correct responsibility?** | No |
| **Missing features** | Side-by-side columns; expected vs. actual labels; variance highlighting (compose C-048) |
| **Refactoring recommendations** | Define `ComparisonSide { label, values }` model; use CSS grid two-column layout |
| **Used in** | Not used |

#### C-023 — Record Metadata Block
| Field | Assessment |
|-------|------------|
| **Exists?** | Yes — `shared/ui/display/record-metadata-block/` |
| **Reusable?** | No — placeholder |
| **Correct responsibility?** | No |
| **Missing features** | Created/updated by; timestamps; reference IDs; version display |
| **Refactoring recommendations** | Accept `@Input() metadata: RecordMetadata` DTO; use on detail panels and form footers |
| **Used in** | Not used |

---

### Form Components (C-024–C-035)

#### C-024 — Standard Form Section
| Field | Assessment |
|-------|------------|
| **Exists?** | Yes — `shared/ui/forms/standard-form-section/` |
| **Reusable?** | No — placeholder |
| **Correct responsibility?** | No |
| **Missing features** | Section wrapper with legend; single/two-column layouts; accordion variant |
| **Refactoring recommendations** | Combine with C-025 `FieldGroupHeader`; provide grid layout classes |
| **Used in** | Not used |

#### C-025 — Field Group Header
| Field | Assessment |
|-------|------------|
| **Exists?** | Yes — `shared/ui/forms/field-group-header/` |
| **Reusable?** | Partial — `@Input() title` declared; template is `ng-content` only (title not rendered) |
| **Correct responsibility?** | No — input unused in template |
| **Missing features** | Render title; collapsible variant; helper text |
| **Refactoring recommendations** | Fix template: `<h3>{{ title }}</h3>`; add `@Input() collapsible` |
| **Used in** | Not used |

#### C-026 — Text Input
| Field | Assessment |
|-------|------------|
| **Exists?** | Yes — `shared/ui/forms/text-input/` |
| **Reusable?** | No — placeholder; no `ControlValueAccessor` |
| **Correct responsibility?** | No |
| **Missing features** | Label rendering; `formControlName` binding; read-only/masked variants; validation display |
| **Refactoring recommendations** | Implement `ControlValueAccessor`; compose C-034 for errors; replace raw `<input>` usage in SignInPage |
| **Used in** | Not used (SignInPage uses native `<input>`) |

#### C-027 — Text Area / Notes Field
| Field | Assessment |
|-------|------------|
| **Exists?** | Yes — `shared/ui/forms/text-area-notes-field/` |
| **Reusable?** | No — placeholder |
| **Correct responsibility?** | No |
| **Missing features** | Textarea with label; character count; `ControlValueAccessor` |
| **Refactoring recommendations** | Implement as CVA; use in investigation/approval screens (UI-025, UI-033) |
| **Used in** | Not used |

#### C-028 — Dropdown / Select Control
| Field | Assessment |
|-------|------------|
| **Exists?** | Yes — `shared/ui/forms/dropdown-select-control/` |
| **Reusable?** | No — `@Input() label`, `options` unused in template |
| **Correct responsibility?** | No |
| **Missing features** | Render `<select>` or custom dropdown; searchable/multi-select variants; CVA |
| **Refactoring recommendations** | Wire inputs to template; support `{ value, label }[]` options model |
| **Used in** | Not used |

#### C-029 — Checkbox Group
| Field | Assessment |
|-------|------------|
| **Exists?** | Yes — `shared/ui/forms/checkbox-group/` |
| **Reusable?** | No — placeholder |
| **Correct responsibility?** | No |
| **Missing features** | Multi-select checkboxes; inline/stacked layouts; CVA |
| **Refactoring recommendations** | Implement for certification checklists (UI-024) and permission toggles (UI-050) |
| **Used in** | Not used |

#### C-030 — Radio Group / Segmented Choice
| Field | Assessment |
|-------|------------|
| **Exists?** | Yes — `shared/ui/forms/radio-group-segmented-choice/` |
| **Reusable?** | No — placeholder |
| **Correct responsibility?** | No |
| **Missing features** | Segmented control UI; mutually exclusive options; disposition choices (UI-043) |
| **Refactoring recommendations** | Implement segmented button group with `role="radiogroup"` for accessibility |
| **Used in** | Not used |

#### C-031 — Number Input
| Field | Assessment |
|-------|------------|
| **Exists?** | Yes — `shared/ui/forms/number-input/` |
| **Reusable?** | No — `@Input() label` unused |
| **Correct responsibility?** | No |
| **Missing features** | Quantity field with min/max/step; plus/minus stepper; unit suffix |
| **Refactoring recommendations** | Implement CVA with `type="number"`; critical for cycle counts (UI-023) and thresholds (UI-008) |
| **Used in** | Not used |

#### C-032 — Date / Date-Time Field
| Field | Assessment |
|-------|------------|
| **Exists?** | Yes — `shared/ui/forms/date-field/` |
| **Reusable?** | No — `@Input() label` unused |
| **Correct responsibility?** | No |
| **Missing features** | Date picker input; date-time variant; read-only timestamp display |
| **Refactoring recommendations** | Implement single-date CVA; pair with C-013 for ranges |
| **Used in** | Not used |

#### C-033 — File Upload Control
| Field | Assessment |
|-------|------------|
| **Exists?** | Yes — `shared/ui/forms/file-upload-control/` |
| **Reusable?** | No — placeholder |
| **Correct responsibility?** | No |
| **Missing features** | Drag-and-drop zone; file list; upload progress; accept MIME types |
| **Refactoring recommendations** | Implement for product import (UI-006) and evidence panel (C-054) |
| **Used in** | Not used |

#### C-034 — Validation Message Block
| Field | Assessment |
|-------|------------|
| **Exists?** | Yes — `shared/ui/forms/validation-message-block/` |
| **Reusable?** | No — `@Input() message` unused in template |
| **Correct responsibility?** | No |
| **Missing features** | Inline field error display; form summary; warning advisory |
| **Refactoring recommendations** | Fix template; differentiate from C-044 banner (field-level vs. page-level) |
| **Used in** | Not used |

#### C-035 — Read-Only Review Form
| Field | Assessment |
|-------|------------|
| **Exists?** | Yes — `shared/ui/forms/read-only-review-form/` |
| **Reusable?** | No — placeholder |
| **Correct responsibility?** | No |
| **Missing features** | Label-value pairs in review layout; approval confirmation section |
| **Refactoring recommendations** | Accept `@Input() fields: { label, value }[]`; use before submit/approve actions |
| **Used in** | Not used |

---

### Workflow and Transaction Components (C-036–C-044)

#### C-036 — Line Item Editor
| Field | Assessment |
|-------|------------|
| **Exists?** | Yes — `shared/ui/workflow/line-item-editor/` |
| **Reusable?** | No — placeholder |
| **Correct responsibility?** | No |
| **Missing features** | Add/remove rows; inline editable table; SKU/qty/UOM columns; validation |
| **Refactoring recommendations** | High-priority for PO (UI-012), receipts (UI-015), returns (UI-042); use `FormArray` internally |
| **Used in** | Not used |

#### C-037 — Queue List
| Field | Assessment |
|-------|------------|
| **Exists?** | Yes — `shared/ui/workflow/queue-list/` |
| **Reusable?** | No — `@Input() items` declared but template ignores it |
| **Correct responsibility?** | No |
| **Missing features** | Render queue items with status, priority, age; selection; empty state |
| **Refactoring recommendations** | Define `QueueItem` interface; fix template to iterate `items`; compose C-056 for empty |
| **Used in** | Not used |

#### C-038 — Step Progress Indicator
| Field | Assessment |
|-------|------------|
| **Exists?** | Yes — `shared/ui/workflow/step-progress-indicator/` |
| **Reusable?** | No — `@Input() steps`, `currentStep` unused in template |
| **Correct responsibility?** | No |
| **Missing features** | Horizontal step visualization; completed/active/pending states |
| **Refactoring recommendations** | Fix template to render step bar from inputs; use in import (UI-006) and returns (UI-043) |
| **Used in** | Not used |

#### C-039 — Approval Decision Panel
| Field | Assessment |
|-------|------------|
| **Exists?** | Yes — `shared/ui/workflow/approval-decision-panel/` |
| **Reusable?** | No — placeholder |
| **Correct responsibility?** | No |
| **Missing features** | Approve/reject/escalate buttons; decision notes field; threshold warning |
| **Refactoring recommendations** | Emit `@Output() decision: ApprovalDecision`; compose C-027 for notes; gate by permissions |
| **Used in** | Not used |

#### C-040 — Status Timeline / History
| Field | Assessment |
|-------|------------|
| **Exists?** | Yes — `shared/ui/workflow/status-timeline/` |
| **Reusable?** | No — placeholder |
| **Correct responsibility?** | No |
| **Missing features** | Chronological events; actor/timestamp; compact log variant |
| **Refactoring recommendations** | Accept `@Input() events: TimelineEvent[]`; vertical layout with connectors |
| **Used in** | Not used |

#### C-041 — Alert Detail Card
| Field | Assessment |
|-------|------------|
| **Exists?** | Yes — `shared/ui/workflow/alert-detail-card/` |
| **Reusable?** | No — placeholder |
| **Correct responsibility?** | No |
| **Missing features** | Severity badge; alert context; recommended action CTA |
| **Refactoring recommendations** | Define `AlertDetail` model from `API-158` response; use in UI-004, UI-036 |
| **Used in** | Not used |

#### C-042 — Recommendation Card
| Field | Assessment |
|-------|------------|
| **Exists?** | Yes — `shared/ui/workflow/recommendation-card/` |
| **Reusable?** | No — placeholder |
| **Correct responsibility?** | No |
| **Missing features** | Replenishment/transfer/rebalance recommendation display; accept/reject actions |
| **Refactoring recommendations** | Pair with `API-160` response shape; use in UI-037, UI-041 |
| **Used in** | Not used |

#### C-043 — Confirmation Dialog
| Field | Assessment |
|-------|------------|
| **Exists?** | Yes — `shared/ui/feedback/confirmation-dialog/` |
| **Reusable?** | No — placeholder; not a true modal/dialog |
| **Correct responsibility?** | No |
| **Missing features** | Modal overlay; title/message; confirm/cancel; destructive action styling; service-based API |
| **Refactoring recommendations** | Implement `ConfirmationDialogService.open()` using CDK Dialog; support async confirm for ship/deactivate/write-off |
| **Used in** | Not used |

#### C-044 — Success / Warning / Error Banner
| Field | Assessment |
|-------|------------|
| **Exists?** | Yes — `shared/ui/feedback/success-warning-error-banner/` |
| **Reusable?** | Yes — `@Input() type`, `@Input() message`; renders styled banner |
| **Correct responsibility?** | Partial — four types supported; missing dismiss action, auto-hide, form-summary variant |
| **Missing features** | `@Output() dismissed`; auto-dismiss timer; `role="alert"` live region; stacking multiple banners |
| **Refactoring recommendations** | Add dismiss button; create `BannerService` for app-wide toast/banner queue; use `role="alert"` |
| **Used in** | `SignInPage` (UI-001) |

---

### Reporting and Analytics Components (C-045–C-049)

#### C-045 — Report Viewer
| Field | Assessment |
|-------|------------|
| **Exists?** | Yes — `shared/ui/analytics/report-viewer/` |
| **Reusable?** | No — placeholder |
| **Correct responsibility?** | No |
| **Missing features** | Tabular/summary report display; filter integration; loading state |
| **Refactoring recommendations** | Compose C-019 + C-012 + C-057; accept report definition config |
| **Used in** | Not used |

#### C-046 — Export Action Group
| Field | Assessment |
|-------|------------|
| **Exists?** | Yes — `shared/ui/analytics/export-action-group/` |
| **Reusable?** | No — placeholder |
| **Correct responsibility?** | No |
| **Missing features** | CSV/PDF/export evidence buttons; `@Output() export` with format |
| **Refactoring recommendations** | Standardize export menu; connect to `API-157` audit export |
| **Used in** | Not used |

#### C-047 — Trend Indicator
| Field | Assessment |
|-------|------------|
| **Exists?** | Yes — `shared/ui/analytics/trend-indicator/` |
| **Reusable?** | No — `@Input() direction`, `value` unused in template |
| **Correct responsibility?** | No |
| **Missing features** | Up/down/flat arrows; percentage delta; RAG chip |
| **Refactoring recommendations** | Fix template; extract from inline trend logic in C-016; support `target` comparison |
| **Used in** | Not used |

#### C-048 — Variance Highlight Block
| Field | Assessment |
|-------|------------|
| **Exists?** | Yes — `shared/ui/analytics/variance-highlight-block/` |
| **Reusable?** | No — placeholder |
| **Correct responsibility?** | No |
| **Missing features** | Expected vs. actual variance emphasis; tolerance breach styling |
| **Refactoring recommendations** | Use inside C-022 Comparison Panel; highlight material variances per BR-022 |
| **Used in** | Not used |

#### C-049 — Drill-Down Link Group
| Field | Assessment |
|-------|------------|
| **Exists?** | Yes — `shared/ui/analytics/drill-down-link-group/` |
| **Reusable?** | No — placeholder |
| **Correct responsibility?** | No |
| **Missing features** | KPI-to-record navigation links; `@Input() links: DrillDownLink[]` |
| **Refactoring recommendations** | Wire from dashboard KPIs to underlying list screens |
| **Used in** | Not used |

---

### Identity, Access, and Audit Components (C-050–C-055)

#### C-050 — Role Assignment Widget
| Field | Assessment |
|-------|------------|
| **Exists?** | Yes — `shared/ui/audit/role-assignment-widget/` |
| **Reusable?** | No — placeholder |
| **Correct responsibility?** | No |
| **Missing features** | Role picker; location scope per role; effective-role summary |
| **Refactoring recommendations** | Compose C-052; bind to `API-143`, `API-144`; use in UI-049 |
| **Used in** | Not used |

#### C-051 — Permission Matrix
| Field | Assessment |
|-------|------------|
| **Exists?** | Yes — `shared/ui/audit/permission-matrix/` |
| **Reusable?** | No — placeholder |
| **Correct responsibility?** | No |
| **Missing features** | Role × permission grid; read-only and editable modes; compare-two-roles |
| **Refactoring recommendations** | High priority for UI-050; use accessible HTML table with sticky headers |
| **Used in** | Not used |

#### C-052 — Access Scope Selector
| Field | Assessment |
|-------|------------|
| **Exists?** | Yes — `shared/ui/audit/access-scope-selector/` |
| **Reusable?** | No — placeholder |
| **Correct responsibility?** | No |
| **Missing features** | Single/multi-location selector; network-wide scope; validation via `API-149` |
| **Refactoring recommendations** | Populate from location API; use in user admin and role admin |
| **Used in** | Not used |

#### C-053 — Audit Record Viewer
| Field | Assessment |
|-------|------------|
| **Exists?** | Yes — `shared/ui/audit/audit-record-viewer/` |
| **Reusable?** | No — placeholder |
| **Correct responsibility?** | No |
| **Missing features** | Before/after values; actor; timestamp; reason reference; split view |
| **Refactoring recommendations** | Map to audit trail API response; use in UI-048 drawer and UI-047 workspace |
| **Used in** | Not used |

#### C-054 — Evidence Attachment Panel
| Field | Assessment |
|-------|------------|
| **Exists?** | Yes — `shared/ui/audit/evidence-attachment-panel/` |
| **Reusable?** | No — placeholder |
| **Correct responsibility?** | No |
| **Missing features** | File list; upload; metadata; link to cases |
| **Refactoring recommendations** | Compose C-033; use in discrepancy (UI-016), variance (UI-025), audit (UI-047) |
| **Used in** | Not used |

#### C-055 — Session / Context Badge
| Field | Assessment |
|-------|------------|
| **Exists?** | Yes — `shared/ui/layout/session-context-badge/` |
| **Reusable?** | Yes — `@Input() role`, `@Input() location` |
| **Correct responsibility?** | Partial — displays role and location; missing combined badge variants |
| **Missing features** | Role-only / location-only variants; tooltip with full scope; clickable scope switcher |
| **Refactoring recommendations** | Accept `SessionUser` object; add `title` tooltip for full `locationScope` code |
| **Used in** | `GlobalHeaderComponent` |

---

### Selection and State Components (C-056–C-060)

#### C-056 — Empty State Panel
| Field | Assessment |
|-------|------------|
| **Exists?** | Yes — `shared/ui/feedback/empty-state-panel/` |
| **Reusable?** | No — `@Input() title`, `message` unused in template |
| **Correct responsibility?** | No |
| **Missing features** | Illustration/icon; primary action CTA; contextual messages per scenario |
| **Refactoring recommendations** | Fix template to render title/message; add `@Input() actionLabel` + `@Output() action` |
| **Used in** | Not used |

#### C-057 — Loading State / Skeleton
| Field | Assessment |
|-------|------------|
| **Exists?** | Yes — `shared/ui/feedback/loading-skeleton/` |
| **Reusable?** | No — placeholder |
| **Correct responsibility?** | No |
| **Missing features** | Table/card/detail/dashboard skeleton variants; shimmer animation |
| **Refactoring recommendations** | Create variant inputs: `@Input() variant: 'table' \| 'card' \| 'detail'`; use during API loading |
| **Used in** | Not used |

#### C-058 — Bulk Selection Toolbar
| Field | Assessment |
|-------|------------|
| **Exists?** | Yes — `shared/ui/feedback/bulk-selection-toolbar/` |
| **Reusable?** | No — `ng-content` only |
| **Correct responsibility?** | No |
| **Missing features** | Selected count; bulk action buttons; appears when rows selected |
| **Refactoring recommendations** | Pair with C-019 selectable table; emit bulk action events |
| **Used in** | Not used |

#### C-059 — Toggle / Switch Control
| Field | Assessment |
|-------|------------|
| **Exists?** | Yes — `shared/ui/forms/toggle-switch-control/` |
| **Reusable?** | No — `@Input() label`, `checked` unused in template |
| **Correct responsibility?** | No |
| **Missing features** | Switch UI; `ControlValueAccessor`; active/inactive labels |
| **Refactoring recommendations** | Implement accessible switch with `role="switch"`; use for location status (UI-007) |
| **Used in** | Not used |

#### C-060 — Tabs / Segmented Content Switcher
| Field | Assessment |
|-------|------------|
| **Exists?** | Yes — `shared/ui/display/tabs-segmented-content-switcher/` |
| **Reusable?** | No — `@Input() tabs` unused in template |
| **Correct responsibility?** | No |
| **Missing features** | Tab headers; active tab content; `@Output() tabChange` |
| **Refactoring recommendations** | Fix template to render tab bar from `tabs` input; use content projection per tab; needed for UI-010, UI-034, UI-045 |
| **Used in** | Not used |

---

## Component-to-Screen Integration Map

| Component | Spec screens | Actually used in |
|-----------|--------------|------------------|
| C-001 Global Header | UI-001–050 | App shell |
| C-002 Main Navigation Bar | UI-002–050 | App shell |
| C-003 Secondary Navigation Panel | UI-005–050 | App shell |
| C-004 Breadcrumb Trail | UI-005–050 | All feature pages |
| C-005 Page Title Bar | UI-002–050 | All feature pages |
| C-006 Footer Metadata Strip | UI-001–050 | App shell |
| C-007 Global Search Bar | UI-002,005,020,021,030,034,049 | App shell header only |
| C-008 Notification Trigger | UI-002,004,036,039,047 | App shell header only |
| C-009 User Menu | UI-002–050 | App shell header only |
| C-010 Quick Action Tile | UI-002,003 | UI-002 only |
| C-011 Task Widget | UI-002,004,025,039,047 | UI-002 only |
| C-016 KPI Summary Card | UI-002,003,020,024,029,045,046 | UI-002 only |
| C-044 Success/Warning/Error Banner | All transactional | UI-001 only |
| C-055 Session Context Badge | UI-002,015,017,023,031,040,049 | App shell header only |
| C-012–C-043, C-045–C-054, C-056–C-060 | Per spec | **Not used** |

---

## Systemic Refactoring Recommendations

### 1. Establish a Form Control Foundation (Priority: Critical)

All C-026–C-035 and C-059 form components should implement `ControlValueAccessor` and optionally `Validator`. Today SignInPage bypasses the design system with raw `<input>` elements.

```text
shared/ui/forms/
  base/           # Abstract field wrapper (label, hint, error slot)
  *.component.ts  # Each implements CVA + composes ValidationMessageBlock
```

### 2. Fix Input/Template Mismatches (Priority: High)

These components declare `@Input()` but templates ignore them — a scaffold anti-pattern:

- C-017 Status Badge
- C-025 Field Group Header
- C-028 Dropdown Select
- C-034 Validation Message Block
- C-037 Queue List
- C-038 Step Progress Indicator
- C-047 Trend Indicator
- C-056 Empty State Panel
- C-059 Toggle Switch
- C-060 Tabs Switcher

**Action:** Either wire inputs to templates or remove dead inputs until implemented.

### 3. Introduce Overlay/Dialog Infrastructure (Priority: High)

C-043 Confirmation Dialog and C-021 Detail Panel require Angular CDK (`@angular/cdk/dialog`, `@angular/cdk/overlay`). Add CDK dependency and a `DialogService` wrapper.

### 4. Create Shared UI Barrel and Contracts (Priority: Medium)

```text
shared/ui/
  index.ts              # Public API exports
  models/               # QueueItem, TableColumn, AlertDetail, etc.
  tokens/               # DI tokens for optional services
```

### 5. Tiered Implementation Roadmap (Priority: Medium)

| Wave | Components | Enables screens |
|------|------------|-----------------|
| Wave 1 | C-019, C-020, C-012, C-056, C-057 | All list screens |
| Wave 2 | C-026–C-035 (forms + CVA) | All create/edit screens |
| Wave 3 | C-037, C-039, C-040, C-043 | Approval/workflow screens |
| Wave 4 | C-045–C-049 | Report/analytics screens |
| Wave 5 | C-050–C-054 | Admin/audit screens |

### 6. Replace Scaffold `ng-content` Pattern (Priority: Medium)

33 components use only `<ng-content></ng-content>`. This creates false coverage — files exist but deliver no spec behavior. Prefer deleting unused stubs or implementing minimally viable templates before adding new screen pages.

### 7. Data Table as Platform Component (Priority: High)

C-019 is the highest-impact component (used on ~30 screens). Invest in a proper `DataTableComponent<T>` with:

- Generic column definitions
- Sorting and pagination
- Row selection + C-058 bulk toolbar
- C-020 row actions
- C-056 empty state
- C-057 loading skeleton

---

## Summary Statistics

| Category | Components | Avg Completion |
|----------|------------|----------------|
| Global Layout (C-001–006) | 6 | 55% |
| Navigation & Utility (C-007–011) | 5 | 46% |
| Filter & Query (C-012–015) | 4 | 11% |
| Data Display (C-016–023) | 8 | 22% |
| Form (C-024–035) | 12 | 12% |
| Workflow (C-036–044) | 9 | 18% |
| Analytics (C-045–049) | 5 | 11% |
| Identity & Audit (C-050–055) | 6 | 19% |
| State & Selection (C-056–060) | 5 | 14% |
| **Overall** | **60** | **~28%** |

---

## Document References

| Document | Path |
|----------|------|
| Component Inventory (SRS) | `SRS/Inventory-Management-System-SRS.md` § C-001–C-060 |
| Shared UI implementation | `ims-frontend/src/app/shared/ui/` |
| Screen Coverage Matrix | `gap_frontend/Screen-Coverage-Matrix.md` |
| Project Architecture Report | `gap_frontend/Project-Architecture-Report.md` |

---

*End of matrix.*
