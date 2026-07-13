# Inventory Management System Component Inventory

## Purpose

This document defines the reusable UI component inventory for the Inventory Management System. It focuses on shared design elements that can be used across multiple screens, modules, and user roles to support consistency, efficiency, and maintainability.

## Scope

The inventory is derived from the screen catalog, navigation structure, user journeys, user flows, and low-fidelity wireframe specifications. It emphasizes reusable components rather than one-off page content.

For each component, this document provides:

1. Component name
2. Purpose
3. Reusability
4. Variants
5. Related screens

---

## Global Layout Components

### C-001 Global Header
- **Purpose:** Provide persistent access to product identity, global search, notifications, tasks, and user account controls.
- **Reusability:** Global; used across nearly all authenticated screens.
- **Variants:** Standard operational header, executive header, admin-focused header, unauthenticated header.
- **Related screens:** `UI-002` to `UI-050`, plus simplified use on `UI-001`.

### C-002 Main Navigation Bar
- **Purpose:** Support movement between primary business modules.
- **Reusability:** Global; reused across all authenticated screens.
- **Variants:** Full menu, role-filtered menu, collapsed menu, highlighted-current-module state.
- **Related screens:** `UI-002` to `UI-050`.

### C-003 Secondary Navigation Panel
- **Purpose:** Organize module-level sections and workflows inside the selected business domain.
- **Reusability:** High; reused by all module-driven screens.
- **Variants:** Vertical sidebar, horizontal tabs, accordion section list.
- **Related screens:** `UI-005` to `UI-050`.

### C-004 Breadcrumb Trail
- **Purpose:** Show hierarchical location and allow quick return to parent levels.
- **Reusability:** Global on all non-home authenticated screens.
- **Variants:** Standard breadcrumb, breadcrumb with final record ID, breadcrumb with action state.
- **Related screens:** `UI-005` to `UI-050`.

### C-005 Page Title Bar
- **Purpose:** Provide a page title, context subtitle, primary action, and optional status indicator.
- **Reusability:** Very high; present on most application screens.
- **Variants:** Simple title bar, title with primary CTA, title with status badge, title with filter controls.
- **Related screens:** `UI-002` to `UI-050`.

### C-006 Footer Metadata Strip
- **Purpose:** Show system metadata such as timestamps, versioning, refresh state, or record audit information.
- **Reusability:** High; useful on dashboards, workbenches, and record detail screens.
- **Variants:** Page footer, report footer, record audit footer, lightweight timestamp-only footer.
- **Related screens:** `UI-001` to `UI-050`.

---

## Navigation and Utility Components

### C-007 Global Search Bar
- **Purpose:** Let users quickly search products, orders, transfers, users, or other indexed entities from anywhere.
- **Reusability:** High; shared utility in the header and some workbench screens.
- **Variants:** Header search, contextual scoped search, autocomplete search, advanced search modal.
- **Related screens:** `UI-002`, `UI-005`, `UI-020`, `UI-021`, `UI-030`, `UI-034`, `UI-049`.

### C-008 Notification Icon and Inbox Trigger
- **Purpose:** Surface pending alerts and open the notification center quickly.
- **Reusability:** Global utility for all operational roles.
- **Variants:** Header icon with count badge, inline notification shortcut, compact task-alert widget.
- **Related screens:** `UI-002`, `UI-004`, `UI-036`, `UI-039`, `UI-047`.

### C-009 User Menu
- **Purpose:** Provide session access, profile/context display, and sign-out actions.
- **Reusability:** Global.
- **Variants:** Minimal profile menu, profile with role/location context, admin profile menu.
- **Related screens:** `UI-002` to `UI-050`.

### C-010 Quick Action Tile
- **Purpose:** Offer shortcut navigation from dashboards to frequently used tasks.
- **Reusability:** Medium to high; mainly used on dashboards and home pages.
- **Variants:** Icon tile, KPI-linked tile, role-priority shortcut tile.
- **Related screens:** `UI-002`, `UI-003`.

### C-011 Task / Approval Shortcut Widget
- **Purpose:** Summarize work awaiting the current user and route them directly into task queues.
- **Reusability:** High for operational and managerial roles.
- **Variants:** Approvals summary, task summary, mixed workload widget.
- **Related screens:** `UI-002`, `UI-004`, `UI-025`, `UI-039`, `UI-047`.

---

## Filter, Search, and Query Components

### C-012 Filter Bar
- **Purpose:** Narrow lists, reports, dashboards, and queues by key criteria.
- **Reusability:** Very high; used across list and analytics screens.
- **Variants:** Inline filter row, expandable advanced filters, sticky filter bar, compact dashboard filters.
- **Related screens:** `UI-002`, `UI-003`, `UI-004`, `UI-005`, `UI-019`, `UI-020`, `UI-022`, `UI-029`, `UI-036`, `UI-041`, `UI-044`, `UI-048`.

### C-013 Date Range Picker
- **Purpose:** Select periods for dashboards, reports, analytics, audit, and reconciliation workflows.
- **Reusability:** High.
- **Variants:** Preset range selector, custom date range, single-period selector.
- **Related screens:** `UI-003`, `UI-019`, `UI-029`, `UI-044`, `UI-045`, `UI-047`, `UI-048`.

### C-014 Search Results List
- **Purpose:** Present matching records after a search action in a structured, scannable way.
- **Reusability:** High.
- **Variants:** Product search results, order results, user results, audit query results.
- **Related screens:** `UI-005`, `UI-021`, `UI-034`, `UI-042`, `UI-049`, `UI-048`.

### C-015 Saved Filter / View Selector
- **Purpose:** Allow users to switch among common views such as open items, urgent items, my location, or all network.
- **Reusability:** Medium to high in operational systems.
- **Variants:** Dropdown saved views, segmented buttons, tabbed saved views.
- **Related screens:** `UI-004`, `UI-020`, `UI-036`, `UI-039`, `UI-044`.

---

## Data Display Components

### C-016 KPI Summary Card
- **Purpose:** Display a key metric with value, trend, status, and optional target comparison.
- **Reusability:** Very high across dashboards and reporting.
- **Variants:** Operational KPI card, executive KPI card, status count card, alert count card.
- **Related screens:** `UI-002`, `UI-003`, `UI-020`, `UI-024`, `UI-029`, `UI-045`, `UI-046`.

### C-017 Status Badge
- **Purpose:** Communicate record state clearly using short labels and color/state semantics.
- **Reusability:** Global.
- **Variants:** Stock status, workflow status, approval status, audit status, campaign readiness status.
- **Related screens:** Used widely across `UI-005` to `UI-050`.

### C-018 Summary Statistic Strip
- **Purpose:** Group several related top-line metrics in a compact horizontal summary region.
- **Reusability:** High for dashboards, workbenches, and record detail screens.
- **Variants:** Dashboard summary strip, record summary strip, queue summary strip.
- **Related screens:** `UI-002`, `UI-015`, `UI-020`, `UI-024`, `UI-030`, `UI-040`, `UI-046`.

### C-019 Data Table
- **Purpose:** Display structured records with sorting, filtering, selection, and row actions.
- **Reusability:** Core reusable component across almost all modules.
- **Variants:** Simple table, selectable table, expandable row table, sticky-header table, paginated table.
- **Related screens:** Nearly all list-based screens including `UI-005`, `UI-012`, `UI-015`, `UI-020`, `UI-034`, `UI-049`.

### C-020 Table Row Action Menu
- **Purpose:** Provide compact actions for a record without overcrowding the table.
- **Reusability:** Very high.
- **Variants:** Kebab menu, inline text actions, hover action set.
- **Related screens:** All screens using `C-019`, especially `UI-005`, `UI-012`, `UI-036`, `UI-039`, `UI-049`.

### C-021 Detail Panel
- **Purpose:** Show detailed information for a selected row or record without leaving the current context.
- **Reusability:** High in list-detail workflows.
- **Variants:** Right-side drawer, bottom panel, inline expandable detail.
- **Related screens:** `UI-005`, `UI-007`, `UI-015`, `UI-016`, `UI-025`, `UI-039`, `UI-049`.

### C-022 Comparison Panel
- **Purpose:** Help users compare two or more states, such as expected vs actual, source vs destination, or operational vs finance.
- **Reusability:** Medium but important for business-critical flows.
- **Variants:** Side-by-side columns, stacked comparison card, split-table comparison.
- **Related screens:** `UI-016`, `UI-025`, `UI-032`, `UI-039`, `UI-045`.

### C-023 Record Metadata Block
- **Purpose:** Display created by, updated by, timestamps, reference IDs, and versioning.
- **Reusability:** Very high on detail pages.
- **Variants:** Inline metadata row, side metadata card, footer metadata strip.
- **Related screens:** `UI-005`, `UI-012`, `UI-015`, `UI-026`, `UI-034`, `UI-042`, `UI-049`.

---

## Form Components

### C-024 Standard Form Section
- **Purpose:** Group related input fields into a clear, reusable form structure.
- **Reusability:** Very high.
- **Variants:** Single-column form, two-column form, stepped form, grouped accordion form.
- **Related screens:** Most create/edit screens including `UI-005`, `UI-007`, `UI-010`, `UI-012`, `UI-026`, `UI-049`.

### C-025 Field Group Header
- **Purpose:** Label and separate major form sections such as header details, line items, approvals, or notes.
- **Reusability:** High.
- **Variants:** Plain section heading, collapsible section heading, heading with helper text.
- **Related screens:** `UI-005`, `UI-012`, `UI-015`, `UI-017`, `UI-026`, `UI-043`, `UI-049`.

### C-026 Text Input
- **Purpose:** Capture short free-text data such as names, codes, and references.
- **Reusability:** Universal.
- **Variants:** Single-line, masked input, searchable text input, read-only text field.
- **Related screens:** Used across almost all form-based screens.

### C-027 Text Area / Notes Field
- **Purpose:** Capture longer comments, rationale, investigation notes, or exception details.
- **Reusability:** High.
- **Variants:** Plain notes field, expandable text area, rich note field with character count.
- **Related screens:** `UI-010`, `UI-016`, `UI-025`, `UI-026`, `UI-027`, `UI-033`, `UI-045`, `UI-047`.

### C-028 Dropdown / Select Control
- **Purpose:** Let users choose from predefined options such as status, role, location, reason code, or supplier.
- **Reusability:** Universal.
- **Variants:** Single-select, multi-select, searchable dropdown, grouped dropdown.
- **Related screens:** Broad use across all forms.

### C-029 Checkbox Group
- **Purpose:** Support multiple non-exclusive selections or confirmations.
- **Reusability:** Medium.
- **Variants:** Inline checkbox list, stacked checkbox list, checkbox with help text.
- **Related screens:** `UI-001`, `UI-010`, `UI-024`, `UI-046`, `UI-050`.

### C-030 Radio Group / Segmented Choice
- **Purpose:** Support mutually exclusive selections where quick comparison matters.
- **Reusability:** High.
- **Variants:** Traditional radio group, segmented control, card-select radio set.
- **Related screens:** `UI-018`, `UI-026`, `UI-028`, `UI-035`, `UI-043`.

### C-031 Number Input
- **Purpose:** Capture quantities, thresholds, counts, values, and numeric adjustments.
- **Reusability:** Very high in inventory workflows.
- **Variants:** Integer field, decimal field, quantity-with-unit, plus/minus stepper.
- **Related screens:** `UI-008`, `UI-012`, `UI-015`, `UI-023`, `UI-026`, `UI-032`, `UI-038`, `UI-043`.

### C-032 Date / Date-Time Field
- **Purpose:** Capture effective dates, expected delivery dates, reporting periods, and session times.
- **Reusability:** High.
- **Variants:** Date picker, date-time picker, read-only timestamp field.
- **Related screens:** `UI-008`, `UI-012`, `UI-014`, `UI-024`, `UI-037`, `UI-045`, `UI-046`.

### C-033 File Upload Control
- **Purpose:** Support import files, evidence attachments, and supporting documents.
- **Reusability:** Medium to high.
- **Variants:** Drag-and-drop upload, button upload, evidence attachment upload with file list.
- **Related screens:** `UI-006`, `UI-016`, `UI-025`, `UI-027`, `UI-047`.

### C-034 Validation Message Block
- **Purpose:** Show field-level or form-level validation feedback before submission.
- **Reusability:** Universal.
- **Variants:** Inline field error, form summary banner, warning advisory block.
- **Related screens:** All form-based screens.

### C-035 Read-Only Review Form
- **Purpose:** Present captured data in review mode before confirmation, approval, or publication.
- **Reusability:** High.
- **Variants:** Review summary card, approval review panel, final confirmation screen section.
- **Related screens:** `UI-006`, `UI-013`, `UI-015`, `UI-027`, `UI-038`, `UI-042`.

---

## Workflow and Transaction Components

### C-036 Line Item Editor
- **Purpose:** Allow users to add, edit, and review multiple structured items within one transaction.
- **Reusability:** Very high for orders, POs, receipts, and returns.
- **Variants:** Inline editable table, add-row editor, master-detail line editor.
- **Related screens:** `UI-012`, `UI-015`, `UI-030`, `UI-034`, `UI-042`, `UI-043`.

### C-037 Queue List
- **Purpose:** Present task-based operational records waiting for user action.
- **Reusability:** Very high in warehouse and approval workflows.
- **Variants:** Pick queue, receipt queue, approvals queue, alerts queue, returns queue.
- **Related screens:** `UI-015`, `UI-017`, `UI-023`, `UI-025`, `UI-031`, `UI-033`, `UI-039`, `UI-043`.

### C-038 Step Progress Indicator
- **Purpose:** Show where the user is in a multi-step workflow such as import, receiving, packing, or return processing.
- **Reusability:** Medium to high.
- **Variants:** Horizontal steps, vertical progress steps, checklist progress.
- **Related screens:** `UI-006`, `UI-015`, `UI-031`, `UI-043`, `UI-047`.

### C-039 Approval Decision Panel
- **Purpose:** Standardize approve/reject workflows with decision note capture.
- **Reusability:** High for governance-heavy processes.
- **Variants:** Binary approve/reject, approve/reject/escalate, approve with threshold warning.
- **Related screens:** `UI-013`, `UI-025`, `UI-027`, `UI-039`.

### C-040 Status Timeline / History
- **Purpose:** Display the chronological progression of a transaction or workflow.
- **Reusability:** High across operational records.
- **Variants:** Vertical timeline, status history table, compact event log.
- **Related screens:** `UI-013`, `UI-015`, `UI-030`, `UI-034`, `UI-038`, `UI-042`, `UI-043`.

### C-041 Alert Detail Card
- **Purpose:** Present key alert context, severity, and recommended next action.
- **Reusability:** High in notification and replenishment workflows.
- **Variants:** Low-stock alert card, exception alert card, delay alert card, readiness alert card.
- **Related screens:** `UI-004`, `UI-036`, `UI-037`, `UI-046`.

### C-042 Recommendation Card
- **Purpose:** Present system-identified next-best actions such as replenishment, transfer, or rebalancing.
- **Reusability:** Medium to high.
- **Variants:** Replenishment recommendation, transfer recommendation, network rebalance recommendation.
- **Related screens:** `UI-037`, `UI-041`.

### C-043 Confirmation Dialog
- **Purpose:** Prevent accidental execution of sensitive or irreversible actions.
- **Reusability:** Universal for critical actions.
- **Variants:** Delete/deactivate confirmation, approve/reject confirmation, ship/dispatch confirmation, write-off confirmation.
- **Related screens:** `UI-007`, `UI-012`, `UI-026`, `UI-027`, `UI-031`, `UI-039`, `UI-049`.

### C-044 Success / Warning / Error Banner
- **Purpose:** Provide immediate feedback after a user action or system event.
- **Reusability:** Universal.
- **Variants:** Success banner, warning banner, blocking error banner, informational banner.
- **Related screens:** Broad use across all transactional screens.

---

## Reporting and Analytics Components

### C-045 Report Viewer
- **Purpose:** Display tabular or summarized report output with filtering and export capability.
- **Reusability:** High in analytics and management review.
- **Variants:** Operational report viewer, audit evidence viewer, valuation report viewer.
- **Related screens:** `UI-044`, `UI-045`, `UI-047`, `UI-048`.

### C-046 Export Action Group
- **Purpose:** Standardize export options for reports, audit results, dashboards, and movement histories.
- **Reusability:** High.
- **Variants:** Export CSV, export PDF, export evidence package, print-friendly export.
- **Related screens:** `UI-003`, `UI-022`, `UI-029`, `UI-044`, `UI-045`, `UI-047`, `UI-048`.

### C-047 Trend Indicator
- **Purpose:** Show whether a metric is improving, declining, or stable relative to target or previous period.
- **Reusability:** High in dashboards and reports.
- **Variants:** Up/down arrow, percentage delta, RAG trend chip.
- **Related screens:** `UI-002`, `UI-003`, `UI-029`, `UI-044`, `UI-045`, `UI-046`.

### C-048 Variance Highlight Block
- **Purpose:** Emphasize differences between actual and expected values in operational or finance contexts.
- **Reusability:** Medium to high.
- **Variants:** Count variance block, receipt discrepancy block, valuation variance block.
- **Related screens:** `UI-016`, `UI-025`, `UI-045`.

### C-049 Drill-Down Link Group
- **Purpose:** Help users move from summary insights into the underlying records driving them.
- **Reusability:** High for analytical screens.
- **Variants:** KPI drill-down links, report-to-record links, alert-to-action links.
- **Related screens:** `UI-002`, `UI-003`, `UI-020`, `UI-029`, `UI-044`, `UI-046`.

---

## Identity, Access, and Audit Components

### C-050 Role Assignment Widget
- **Purpose:** Assign one or more business roles and scope them to locations or permissions.
- **Reusability:** High in admin workflows.
- **Variants:** Simple role picker, role plus location-scope matrix, effective-role summary.
- **Related screens:** `UI-049`, `UI-050`.

### C-051 Permission Matrix
- **Purpose:** Show or edit the mapping between roles, permission groups, and scope.
- **Reusability:** High for access control management.
- **Variants:** Read-only matrix, editable matrix, compare-two-roles matrix.
- **Related screens:** `UI-050`.

### C-052 Access Scope Selector
- **Purpose:** Specify the organizational or location boundaries for a role or action.
- **Reusability:** Medium to high.
- **Variants:** Single-location selector, multi-location selector, network-wide scope selector.
- **Related screens:** `UI-049`, `UI-050`, optionally `UI-001` and `UI-002` for context display.

### C-053 Audit Record Viewer
- **Purpose:** Display before/after values, actor identity, timestamp, and reason reference for an auditable event.
- **Reusability:** High in audit, governance, and exception review.
- **Variants:** Inline audit record, modal audit record viewer, split before/after viewer.
- **Related screens:** `UI-047`, `UI-048`, and supporting detail usage in `UI-025`, `UI-026`, `UI-049`.

### C-054 Evidence Attachment Panel
- **Purpose:** Collect and display uploaded evidence linked to discrepancies, write-offs, investigations, and audits.
- **Reusability:** Medium to high.
- **Variants:** File list with thumbnails, document list with uploader metadata, attachment upload panel.
- **Related screens:** `UI-016`, `UI-025`, `UI-027`, `UI-047`.

### C-055 Session / Context Badge
- **Purpose:** Display the current role, location scope, or operating context to reduce user mistakes.
- **Reusability:** High for multi-role and location-scoped systems.
- **Variants:** Role badge, location badge, combined role-location badge.
- **Related screens:** `UI-002`, `UI-015`, `UI-017`, `UI-023`, `UI-031`, `UI-040`, `UI-049`.

---

## Selection and State Components

### C-056 Empty State Panel
- **Purpose:** Guide users when no records, tasks, alerts, or results are available.
- **Reusability:** Universal.
- **Variants:** No search results, no tasks, no alerts, no data for selected period.
- **Related screens:** All list, queue, and report screens.

### C-057 Loading State / Skeleton
- **Purpose:** Show that data is being retrieved while preserving page structure.
- **Reusability:** Universal.
- **Variants:** Table skeleton, card skeleton, detail panel skeleton, dashboard skeleton.
- **Related screens:** All data-driven screens.

### C-058 Bulk Selection Toolbar
- **Purpose:** Support actions on multiple selected rows at once.
- **Reusability:** Medium; useful for admin and operational batch tasks.
- **Variants:** Bulk acknowledge, bulk export, bulk classification update, bulk approve/reject.
- **Related screens:** `UI-004`, `UI-009`, `UI-036`, `UI-049`.

### C-059 Toggle / Switch Control
- **Purpose:** Support fast binary settings such as active/inactive, include/exclude, or network/local view.
- **Reusability:** High.
- **Variants:** Status switch, view toggle, scope toggle.
- **Related screens:** `UI-005`, `UI-007`, `UI-010`, `UI-020`, `UI-049`, `UI-050`.

### C-060 Tabs / Segmented Content Switcher
- **Purpose:** Let users switch between related content views without leaving the page.
- **Reusability:** High.
- **Variants:** Detail tabs, record subview tabs, mode switcher.
- **Related screens:** `UI-010`, `UI-034`, `UI-045`, `UI-047`.

---

## Summary

- **Total reusable components identified:** 60
- **Primary focus:** Shared structural, workflow, form, data display, and governance components
- **Design intent:** Promote consistency across inventory, procurement, warehouse, fulfillment, reporting, and administration experiences

## Recommended Next Use

This component inventory should be used as the baseline for:

- A design system starter library
- Component-level wireframes
- State definitions for validation, loading, empty, and error behavior
- UX acceptance criteria for reusable UI patterns

