# Inventory Management System UI Guidelines

## Purpose

This document defines UI guidelines for the Inventory Management System covering responsiveness, accessibility, keyboard interaction, and mobile behavior. The recommendations are aligned to WCAG principles of being:

- **Perceivable**
- **Operable**
- **Understandable**
- **Robust**

The guidance is intended for UX, UI, frontend engineering, QA, and accessibility review.

## Accessibility Target

The recommended baseline target for the IMS is:

- **WCAG 2.2 AA** for all core user journeys

This is especially important because the system is used for:

- Time-sensitive warehouse operations
- Data-entry-heavy workflows
- Multi-role enterprise access
- Reporting and audit use cases

---

## 1. Responsive Breakpoints

### Design Intent

The IMS is primarily a business web application used on desktop and laptop devices, but it should remain usable on tablets and selectively on mobile for read-heavy and lightweight task flows. Complex data-entry and table-heavy workflows should remain optimized for larger screens.

### Recommended Breakpoints

| Breakpoint | Width | Primary Usage |
|---|---:|---|
| `xs` | `0-479px` | Small mobile phones |
| `sm` | `480-767px` | Large phones / small mobile landscape |
| `md` | `768-1023px` | Tablets / small laptops |
| `lg` | `1024-1439px` | Standard laptops / desktop |
| `xl` | `1440px+` | Large desktop / wide operational monitors |

### Layout Guidance by Breakpoint

#### `xs` and `sm`
- Use a single-column layout.
- Collapse secondary navigation into drawers, accordions, or segmented tabs.
- Move filter bars into expandable panels.
- Stack form fields vertically.
- Replace dense multi-column tables with card-list or priority-column responsive tables.
- Limit simultaneous pane layouts; avoid side-by-side master-detail patterns unless converted to drill-in navigation.

#### `md`
- Allow two-panel layouts selectively.
- Keep primary navigation collapsible.
- Use horizontally scrollable tables only when card conversion would lose too much structure.
- Preserve important workbench workflows where possible, but simplify dense controls.

#### `lg` and `xl`
- Use full enterprise layout with:
  - persistent global header
  - primary navigation
  - secondary navigation
  - list-detail and workbench layouts
- Allow wider tables, multi-column forms, and parallel information panels.

### Responsive Rules

- Never rely on hover-only interaction at any breakpoint.
- Do not hide critical actions inside unstable overflow patterns without a clear alternative.
- Avoid fixed-height panels that trap content at smaller sizes.
- Preserve task order when stacking columns vertically.
- Ensure zoom to 200% does not break essential workflows.

### WCAG Alignment

- Supports **Perceivable** and **Operable** principles by maintaining content access across viewport sizes and zoom states.

---

## 2. Keyboard Navigation

### Design Intent

All essential tasks must be operable using a keyboard alone, especially because IMS users may:

- perform repetitive data entry
- use barcode/scanner-assisted input
- work quickly in operational contexts
- need non-pointer accessibility support

### Core Requirements

- All interactive controls must be reachable with `Tab`.
- Use `Shift + Tab` for backward movement in a predictable order.
- Ensure visible focus on every interactive element.
- All actions available by mouse must also be available by keyboard.
- Avoid keyboard traps.

### Expected Keyboard Behavior

#### Global
- `Tab` moves through interactive elements in reading/task order.
- `Enter` activates primary buttons and selected menu items.
- `Space` toggles checkboxes, switches, and some buttons where appropriate.
- `Esc` closes dialogs, menus, drawers, and temporary overlays.

#### Navigation
- Menus, tabs, accordions, and dropdowns must support arrow-key navigation where standard patterns apply.
- Breadcrumb links must be keyboard reachable.
- Skip link should be available to jump to main content.

#### Forms
- Entering data should not unexpectedly submit multi-field forms.
- Inline validation must not steal keyboard focus unless the user submits and an error summary intentionally redirects focus.

#### Tables and Grids
- Row actions must be reachable via keyboard.
- Sortable headers must be operable by keyboard.
- Expandable rows must support `Enter` or `Space`.
- If grid-like interactions are used, arrow-key behavior must be consistent and documented.

### Keyboard Priority Areas in IMS

Special attention is required for:

- `Goods Receipt Workbench`
- `Put-Away Workbench`
- `Cycle Count Workbench`
- `Pick, Pack, and Ship Workbench`
- `Stock Adjustment Management`
- `User Account Management`

### WCAG Alignment

- Supports **Operable** principle, especially keyboard accessibility and predictable interaction.

---

## 3. Focus Management

### Design Intent

Focus must move intentionally so users always know where they are, what changed, and what to do next.

### Global Focus Rules

- On page load, focus should move to the page heading or main content container, not remain ambiguously in the browser chrome.
- Do not move focus unexpectedly during normal typing or filtering.
- When opening a modal, drawer, or popup, move focus into it.
- When closing a modal, return focus to the triggering control.
- When a page update occurs after a submit, direct focus to the most relevant next element:
  - success banner
  - first validation error
  - updated record heading

### Error Focus Rules

- On failed submit, move focus to the error summary if present.
- The error summary should include links or relationships to invalid fields.
- Focus should then allow the user to move naturally into each field error.

### Success Focus Rules

- For save/update actions that remain on the same page, focus should move to:
  - success banner, then
  - updated record title or first relevant next action

- For create flows that navigate to a detail page, focus should land on the new page heading.

### Dynamic Content Rules

- When filters refresh results asynchronously, do not steal focus from the current control unless the user explicitly triggers navigation into results.
- If an item disappears from a queue after success, move focus to:
  - the next logical row, or
  - the list heading if the queue becomes empty

### Dialog and Overlay Rules

- Focus must be trapped within active modals.
- Background content must not be keyboard reachable while modal is open.
- Closing the overlay restores prior focus context.

### WCAG Alignment

- Supports **Operable** and **Understandable** principles through predictable navigation and state transitions.

---

## 4. Color Contrast

### Design Intent

Color must support meaning, not carry meaning alone. IMS screens use many statuses, alerts, thresholds, and workflow states, so contrast and redundant cues are critical.

### Minimum Contrast Recommendations

- Normal text: **4.5:1** minimum
- Large text: **3:1** minimum
- Essential UI components and icons: **3:1** minimum against adjacent colors
- Focus indicators: clearly visible with **3:1** minimum contrast against surrounding colors

### Status and Semantic Guidance

Status indicators such as:

- low stock
- out of stock
- quarantined
- approved
- rejected
- delayed
- at risk

must not rely on color alone.

Use at least one of:

- text labels
- icons
- patterns
- badges
- helper text

Example:
- Not just red dot
- Use: `Out of Stock` badge with icon and accessible text

### Background and Surface Guidance

- Avoid placing light text on low-contrast tinted cards.
- Avoid thin gray text in metadata areas if it drops below accessibility thresholds.
- Ensure disabled state still remains readable enough to understand context, while clearly differentiated from enabled state.

### Charts and Data Visualization

- Use more than color to distinguish series:
  - labels
  - patterns
  - markers
  - direct annotations
- Ensure chart legends are keyboard and screen-reader understandable where interactive.

### WCAG Alignment

- Supports **Perceivable** principle through sufficient visual contrast and non-color-dependent communication.

---

## 5. Form Accessibility

### Design Intent

Forms are central to the IMS, especially for inventory transactions, approvals, receiving, fulfillment, and administration. They must be accessible, efficient, and forgiving.

### Labeling Rules

- Every input must have a persistent visible label.
- Placeholder text must not replace labels.
- Required fields must be clearly identified visually and programmatically.
- Optional fields may be marked explicitly if that reduces ambiguity.

### Instruction and Help Rules

- Put concise helper text near the field when needed.
- Use examples only if they clarify format.
- Keep field guidance short and specific.

### Validation Rules

- Field errors must be programmatically associated with the field.
- Error text must explain:
  - what is wrong
  - how to fix it
- Validation must not depend only on color.
- Use clear language like:
  - `Quantity must be greater than 0`
  - not: `Invalid value`

### Grouping Rules

- Related controls should be grouped with clear section headings.
- Radio groups and checkbox groups should be wrapped in accessible group semantics.
- Repeating line-item forms must expose row and field context clearly.

### Input Behavior Rules

- Use appropriate input types:
  - email for email
  - numeric fields for quantities
  - date pickers for dates
- Support manual entry in addition to picker-only interactions where practical.
- Avoid requiring drag-only or pointer-only actions.

### Required Accessibility Features

- Labels linked to controls
- Error text linked to controls
- Required state announced to assistive technology
- Disabled/read-only states distinguishable programmatically
- Autosave or draft patterns must not interrupt screen reader flow unexpectedly

### Form-Specific IMS Priorities

Special care is needed for:

- line-item editors
- barcode/scanner-assisted fields
- conditional fields
- approval decision sections
- multi-step receiving and return workflows

### WCAG Alignment

- Supports **Perceivable**, **Operable**, **Understandable**, and **Robust** principles.

---

## 6. Table Accessibility

### Design Intent

Tables are one of the most heavily used patterns in the IMS. They must support scanning, sorting, selection, and row actions without becoming inaccessible.

### Structural Rules

- Use true table semantics for tabular data.
- Header cells must be properly associated with their columns.
- Complex tables with grouped headers should preserve readable relationships.

### Interaction Rules

- Sortable columns must indicate current sort state.
- Row selection checkboxes must have clear labels.
- Row action menus must be keyboard and screen-reader accessible.
- Expandable rows must announce expanded/collapsed state.

### Content Rules

- Keep column names concise and descriptive.
- Do not truncate essential meaning without a way to access full content.
- Numeric values should be aligned consistently for readability, but semantic structure must remain intact.

### Responsive Table Rules

On smaller screens:

- prioritize critical columns
- allow horizontal scrolling only when necessary
- consider card transformation for highly dense operational lists
- preserve access to row actions and identifiers

### Empty and Error Rules

- Empty tables should clearly explain that there are no records, not simply show blank space.
- Loading tables should use skeleton rows.
- Error states should appear above the table and allow retry.

### High-Priority IMS Table Types

Special care is needed for:

- inventory status tables
- purchase order line tables
- receipt line tables
- order line status tables
- transfer and approval queues
- audit logs
- permission matrices

### WCAG Alignment

- Supports **Perceivable**, **Operable**, and **Understandable** principles for structured data access.

---

## 7. Mobile Considerations

### Design Intent

The IMS should support mobile selectively. Not every desktop workflow should be forced into a full mobile experience. The mobile strategy should prioritize:

- lookup tasks
- lightweight approvals
- notifications
- simple updates
- selected warehouse actions where practical

### Suitable Mobile-First or Mobile-Friendly Tasks

- notifications
- approvals
- stock lookup
- order status inquiry
- low-stock alert review
- basic return receipt steps
- simple transfer confirmation

### Desktop-Preferred Tasks

These should remain optimized for tablet/desktop due to complexity:

- purchase order editing with many lines
- large discrepancy resolution
- detailed physical counts
- complex inventory adjustment cases
- valuation reconciliation
- permission matrix editing
- audit review with large datasets

### Mobile Interaction Rules

- Use larger tap targets.
- Avoid hover-only actions.
- Keep one primary action visible at a time.
- Use sticky bottom action areas sparingly and only when they do not cover content.
- Favor drill-down flows over multi-pane layouts.
- Use clear back navigation and preserve entered data when moving between screens.

### Mobile Form Rules

- Keep forms short and segmented.
- Reduce side-by-side fields.
- Use mobile-friendly input controls where appropriate.
- Ensure scanners or hardware keyboards do not break focus order.

### Mobile Table Rules

- Convert dense tables into stacked cards where needed.
- Keep record ID, status, and primary action visible.
- Hide secondary metadata behind expand/collapse patterns if necessary.

### Orientation and Zoom

- Support portrait-first for phones.
- Avoid requiring landscape for essential tasks unless the task is explicitly desktop/tablet-only.
- Ensure users can zoom without clipping essential controls.

### WCAG Alignment

- Supports **Operable** and **Perceivable** principles by preserving access under touch, zoom, and small-screen constraints.

---

## 8. Additional WCAG-Aligned Recommendations

### Language and Clarity

- Use plain, task-oriented labels.
- Keep system messages specific and actionable.
- Avoid unexplained abbreviations unless they are common in the user domain and defined consistently.

### Time and Session

- Warn users before session timeout where data entry may be lost.
- Provide recovery options for long-running forms.

### Motion and Animation

- Avoid unnecessary motion in operational workflows.
- Any animation should be subtle, short, and never required to understand state changes.

### Error Prevention

- Confirm destructive actions such as:
  - write-offs
  - deactivation
  - cancel order
  - cancel PO
  - release promotional allocation
- Allow review before finalizing important inventory transactions.

### Assistive Technology Robustness

- Use semantic HTML or equivalent accessible roles.
- Ensure labels, status messages, dialogs, tables, and menus are announced correctly by assistive technologies.
- Test with keyboard-only navigation and screen readers on core flows.

---

## 9. Recommended Testing Checklist

The following should be tested on all critical flows:

- Can the entire task be completed using keyboard only?
- Is focus always visible and predictable?
- Are all field errors announced and understandable?
- Are status colors understandable without color perception?
- Do tables remain usable at 200% zoom?
- Do mobile layouts preserve primary tasks clearly?
- Are dialogs and overlays focus-trapped correctly?
- Are success and error messages exposed to assistive technology?
- Are no-permission states understandable without exposing restricted data?

---

## 10. Priority Screens for Accessibility Review

The following screens should receive first-pass accessibility testing because they combine complexity, frequency, and business criticality:

1. `UI-015 Goods Receipt Workbench`
2. `UI-017 Put-Away Workbench`
3. `UI-023 Cycle Count Workbench`
4. `UI-026 Stock Adjustment Management`
5. `UI-030 Order Reservation Workbench`
6. `UI-031 Pick, Pack, and Ship Workbench`
7. `UI-034 Order Fulfillment Status`
8. `UI-040 Transfer Execution and In-Transit Tracking`
9. `UI-043 Return Inspection and Disposition`
10. `UI-049 User Account Management`
11. `UI-050 Role and Access Control Administration`

---

## Summary

These guidelines establish the accessibility and responsive foundation for the IMS UI. The system should prioritize:

- desktop excellence for complex operations
- controlled mobile support for lightweight tasks
- complete keyboard operability
- predictable focus behavior
- strong color contrast and non-color status communication
- accessible forms and tables

This guidance should be used alongside:

- `IMS-Component-Inventory.md`
- `IMS-Form-Specifications-and-Validation.md`
- `IMS-Screen-State-Specifications.md`
- `IMS-Low-Fidelity-Wireframe-Specifications.md`

