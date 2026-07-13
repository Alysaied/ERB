# Inventory Management System Design System

## Purpose

This document defines the design system for the Inventory Management System (IMS). It is intended to support product design, UI design, frontend implementation, QA review, and AI-assisted design generation.

The system should reflect a modern enterprise dashboard style similar to ERP platforms: structured, dense but readable, highly scannable, role-aware, operationally efficient, and accessible.

## Design Principles

- Clarity first: prioritize operational readability over decoration.
- Enterprise density: support complex workflows without visual clutter.
- Consistency at scale: shared patterns across inventory, procurement, warehouse, fulfillment, audit, and admin.
- Action hierarchy: always make the next action obvious.
- Accessible by default: target `WCAG 2.2 AA`.
- Desktop-first, responsive second: optimize heavy workflows for `lg` and `xl`, simplify intelligently on smaller screens.

---

## Foundations

## Colors

### Color Strategy

Use a restrained enterprise palette built around cool neutrals, clear semantic states, and strong contrast. Most screens should feel calm and structured, with status colors used sparingly for alerts, approvals, risks, and workflow states.

### Core Brand and Interface Palette

| Token | Hex | Usage |
|---|---|---|
| `color-brand-900` | `#0F2A43` | strongest brand surfaces, sidebar dark areas |
| `color-brand-800` | `#163A5F` | primary navigation active areas |
| `color-brand-700` | `#1D4E89` | primary buttons, links, selected states |
| `color-brand-600` | `#2563A6` | hover states, active accents |
| `color-brand-500` | `#2F7CC1` | secondary brand emphasis |
| `color-brand-100` | `#DCEBFA` | selected row background, light info surfaces |
| `color-brand-050` | `#F4F8FD` | app background accents |

### Neutral Palette

| Token | Hex | Usage |
|---|---|---|
| `color-neutral-950` | `#0B1220` | highest emphasis text |
| `color-neutral-900` | `#111827` | headings, strong text |
| `color-neutral-800` | `#1F2937` | primary body text |
| `color-neutral-700` | `#374151` | secondary text |
| `color-neutral-600` | `#4B5563` | metadata, helper text |
| `color-neutral-500` | `#6B7280` | muted labels, icons |
| `color-neutral-400` | `#9CA3AF` | disabled text, placeholders |
| `color-neutral-300` | `#D1D5DB` | borders, dividers |
| `color-neutral-200` | `#E5E7EB` | light borders, table separators |
| `color-neutral-100` | `#F3F4F6` | card backgrounds, hover fills |
| `color-neutral-050` | `#F9FAFB` | app canvas |
| `color-white` | `#FFFFFF` | main surface |

### Semantic Palette

| Token | Hex | Usage |
|---|---|---|
| `color-success-700` | `#15803D` | success text, strong success states |
| `color-success-100` | `#DCFCE7` | success backgrounds |
| `color-warning-700` | `#B45309` | warnings, stock risk text |
| `color-warning-100` | `#FEF3C7` | warning backgrounds |
| `color-danger-700` | `#B91C1C` | destructive, errors, rejections |
| `color-danger-100` | `#FEE2E2` | error backgrounds |
| `color-info-700` | `#1D4ED8` | info messages, help states |
| `color-info-100` | `#DBEAFE` | info backgrounds |
| `color-purple-700` | `#6D28D9` | audit/governance special accents |
| `color-purple-100` | `#EDE9FE` | audit tinted backgrounds |

### Operational Status Colors

| State | Color | Notes |
|---|---|---|
| In Stock / Available | success | always pair with text label |
| Low Stock / At Risk | warning | use icon + badge text |
| Out of Stock / Blocked | danger | use icon + explicit label |
| In Transit / Pending | info | neutral-progress state |
| Quarantined / Hold | purple | use lock/quarantine icon |
| Draft / In Review | neutral | low emphasis but visible |
| Approved | success | for approvals and certifications |
| Rejected / Failed | danger | for rejected decisions and blocking failures |

### Surface Model

| Surface Token | Hex | Usage |
|---|---|---|
| `surface-app` | `#F9FAFB` | overall application background |
| `surface-primary` | `#FFFFFF` | cards, forms, tables |
| `surface-secondary` | `#F3F4F6` | filter bars, subpanels |
| `surface-tertiary` | `#E5E7EB` | disabled areas, subtle contrast sections |
| `surface-sidebar` | `#0F2A43` | primary sidebar background |
| `surface-header` | `#FFFFFF` | top header |
| `surface-overlay` | `rgba(17, 24, 39, 0.48)` | modal backdrop |

### Color Usage Rules

- Never use color as the only indicator of state.
- Text on primary surfaces should meet a minimum `4.5:1` contrast ratio.
- Use semantic backgrounds in banners, chips, badges, and alert cards, not full-page saturation.
- Dark sidebar + light content is the default enterprise shell.

---

## Typography

### Typeface Recommendation

Use a neutral, modern UI sans-serif such as:

- `Inter`
- fallback: `Segoe UI`, `Roboto`, `Arial`, `sans-serif`

### Typography Scale

| Token | Size | Weight | Line Height | Usage |
|---|---:|---:|---:|---|
| `type-display-lg` | 32px | 700 | 40px | executive dashboard title, rare |
| `type-heading-1` | 28px | 700 | 36px | top-level page headings |
| `type-heading-2` | 24px | 700 | 32px | major workspace headings |
| `type-heading-3` | 20px | 600 | 28px | section headings |
| `type-heading-4` | 18px | 600 | 26px | card titles, panel titles |
| `type-body-lg` | 16px | 400 | 24px | primary body text |
| `type-body-md` | 14px | 400 | 20px | forms, tables, standard UI text |
| `type-body-sm` | 13px | 400 | 18px | helper text, metadata |
| `type-label-md` | 14px | 500 | 20px | form labels, nav labels |
| `type-label-sm` | 12px | 600 | 16px | badge labels, overlines |
| `type-mono-sm` | 13px | 500 | 18px | IDs, SKU codes, transaction refs |

### Typography Rules

- Use `14px` as the default interface text size.
- Use `13px` for dense tables only when readability remains strong.
- Use monospaced styling selectively for record IDs, SKUs, PO numbers, transfer IDs, and audit references.
- Avoid all-caps for large content blocks; reserve uppercase styling for small labels and metadata only.

---

## Spacing

### Base Spacing Unit

Use a `4px` base unit.

### Spacing Scale

| Token | Value | Typical Usage |
|---|---:|---|
| `space-1` | 4px | icon gap, small offsets |
| `space-2` | 8px | inline gaps, chip spacing |
| `space-3` | 12px | compact form spacing |
| `space-4` | 16px | default control spacing |
| `space-5` | 20px | section gutters |
| `space-6` | 24px | card padding, block spacing |
| `space-8` | 32px | page sections |
| `space-10` | 40px | large dashboard separation |
| `space-12` | 48px | major layout spacing |

### Spacing Rules

- Page outer padding on desktop: `24px`.
- Card padding: `16px` or `24px` depending on density.
- Form field vertical spacing: `16px`.
- Label-to-input spacing: `6px` to `8px`.
- Table cell horizontal padding: `12px` to `16px`.

---

## Grid

### Breakpoints

| Breakpoint | Width |
|---|---|
| `xs` | `0-479px` |
| `sm` | `480-767px` |
| `md` | `768-1023px` |
| `lg` | `1024-1439px` |
| `xl` | `1440px+` |

### Layout Grid

| Breakpoint | Columns | Margin | Gutter |
|---|---:|---:|---:|
| `xs` | 4 | 16px | 16px |
| `sm` | 4 | 16px | 16px |
| `md` | 8 | 20px | 20px |
| `lg` | 12 | 24px | 24px |
| `xl` | 12 | 32px | 24px |

### Enterprise Shell Layout

- Sidebar width expanded: `248px`
- Sidebar width collapsed: `72px`
- Header height: `64px`
- Subheader or page title bar height: `56px`
- Content max width: fluid
- Default content column behavior:
  - dashboards: multi-column responsive grid
  - list-detail: 35/65 or 40/60 split
  - forms: two columns on desktop, one on small screens

---

## Components

## Buttons

### Button Variants

1. `Primary`
2. `Secondary`
3. `Tertiary`
4. `Destructive`
5. `Ghost`
6. `Icon Only`

### Primary Button

- Background: `color-brand-700`
- Text: white
- Border: none
- Radius: `8px`
- Height: `40px`
- Horizontal padding: `16px`
- Hover: `color-brand-600`
- Active: `color-brand-800`

### Secondary Button

- Background: white
- Text: `color-brand-700`
- Border: `1px solid color-neutral-300`
- Hover background: `color-brand-050`

### Tertiary Button

- Background: transparent
- Text: `color-neutral-800`
- Border: transparent
- Hover background: `color-neutral-100`

### Destructive Button

- Background: `color-danger-700`
- Text: white
- Hover: slightly darker destructive tone

### Sizes

| Size | Height | Text |
|---|---:|---|
| `sm` | 32px | 13px |
| `md` | 40px | 14px |
| `lg` | 48px | 16px |

### Button Rules

- One primary button per action cluster.
- In dense tables, use tertiary or icon actions first.
- Use destructive only for irreversible actions.
- Loading buttons show spinner and retain width.

---

## Inputs

### Input Types

- text input
- searchable select
- dropdown
- textarea
- number input
- date/date-time input
- checkbox
- radio group
- switch
- file upload

### Text Input Specification

- Height: `40px`
- Padding: `0 12px`
- Border: `1px solid color-neutral-300`
- Radius: `8px`
- Background: white
- Text: `color-neutral-900`
- Placeholder: `color-neutral-400`

### States

- Default
- Hover
- Focus
- Filled
- Disabled
- Read-only
- Error
- Success

### Focus Style

- Border color: `color-brand-700`
- Outer ring: `2px` or `3px` translucent brand ring
- Must remain visible on white and tinted surfaces

### Error Style

- Border color: `color-danger-700`
- Helper text: `color-danger-700`
- Optional error icon inside field for complex forms

### Textarea

- Min height: `88px`
- Resize vertically only
- Use for notes, rationale, and comments

### Selects and Searchable Inputs

- Same height and radius as text input
- Searchable select is the default for product, location, supplier, and user lookup
- Use grouped options where domain structure matters

### Form Layout Rules

- Label above input
- Helper text below input
- Error message replaces or sits below helper text
- Group related fields into titled sections

---

## Tables

### Table Design Intent

Tables are the backbone of the IMS and should feel highly scannable, compact, and action-oriented without becoming visually noisy.

### Table Specification

- Header height: `44px`
- Row height:
  - compact: `40px`
  - default: `48px`
  - expanded: `56px`
- Cell padding: `12px 16px`
- Header text: `12px` to `13px`, semibold
- Body text: `13px` to `14px`
- Border color: `color-neutral-200`
- Zebra striping: optional and subtle only

### Table Features

- sortable columns
- sticky header for long tables
- row selection checkboxes
- row action menu
- inline status badges
- pagination
- empty state row/panel
- skeleton loading rows

### Row States

- default
- hover
- selected
- focused
- warning-highlighted
- disabled

### Table Rules

- Keep key identifiers pinned left where practical.
- Use badges for status columns.
- Numeric values should align consistently, usually right-aligned.
- Avoid more than 8 to 10 visible columns before introducing prioritization or horizontal scroll.

---

## Cards

### Card Types

1. KPI card
2. summary card
3. detail card
4. recommendation card
5. alert card
6. empty state card

### Card Specification

- Background: white
- Border: `1px solid color-neutral-200`
- Radius: `12px`
- Padding: `16px` or `24px`
- Shadow: minimal, soft, enterprise-light

### KPI Card Structure

- label
- primary value
- trend indicator
- optional subtitle
- optional target delta

### Recommendation Card Structure

- title
- short context sentence
- impact summary
- recommended action
- CTA

---

## Dialogs

### Dialog Types

1. confirmation dialog
2. destructive confirmation dialog
3. form dialog
4. review dialog
5. system alert dialog

### Dialog Specification

- Width:
  - small: `400px`
  - medium: `560px`
  - large: `720px`
- Radius: `16px`
- Padding: `24px`
- Overlay: dark translucent scrim

### Dialog Structure

- title
- explanatory body
- optional highlighted warning section
- primary and secondary actions
- close icon top-right when appropriate

### Dialog Rules

- Use dialogs for confirmations and small supporting forms.
- Use full-screen pages for high-risk, multi-step, or line-item-heavy flows.
- Destructive dialogs must name the object and consequence clearly.

---

## Icons

### Icon Style

- Outline-first enterprise icon set
- Consistent stroke width
- Simple, geometric, legible at small sizes

### Recommended Sizes

| Size | Use |
|---|---|
| `16px` | inline metadata, compact actions |
| `18px` | standard control icons |
| `20px` | header, buttons, cards |
| `24px` | section or feature icons |

### Usage Rules

- Pair status icons with text labels.
- Use icon-only buttons only when the label is obvious and accessible.
- In ERP-like dashboards, icons should support scanning, not dominate the interface.

### Core Icon Categories

- navigation
- inventory and warehouse
- procurement and supplier
- transfers and logistics
- returns
- reports and analytics
- governance and audit
- administration
- alerts and statuses

---

## Alerts

### Alert Types

- success
- info
- warning
- error

### Alert Specification

- Radius: `10px`
- Padding: `12px 16px`
- Border left or full border for emphasis
- Optional icon leading
- Optional action link/button trailing

### Example Styles

- Success: green tint background, dark green text
- Info: blue tint background, dark blue text
- Warning: amber tint background, dark amber text
- Error: red tint background, dark red text

### Usage Rules

- Use page-level alerts for save, submit, conflict, permission, and system errors.
- Use inline alerts inside cards or panels for contextual warnings.
- Keep message copy concise and action-oriented.

---

## Badges

### Badge Purpose

Badges communicate short, high-signal status labels.

### Badge Specification

- Height: `22px` to `24px`
- Padding: `0 8px`
- Radius: pill or `999px`
- Text: `12px`, semibold

### Badge Types

- stock status
- workflow status
- approval state
- inventory condition
- audit severity

### Example Badge Mapping

- `Available` -> success
- `Low Stock` -> warning
- `Out of Stock` -> danger
- `Draft` -> neutral
- `Pending Approval` -> info
- `Quarantine` -> purple

---

## Chips

### Chip Purpose

Chips represent filters, tags, lightweight states, and selectable attributes.

### Chip Variants

- static chip
- selectable chip
- removable chip
- filter chip

### Chip Specification

- Height: `28px` to `32px`
- Radius: `999px`
- Horizontal padding: `10px` to `12px`
- Background:
  - neutral by default
  - tinted for active/filter state

### Usage Rules

- Use chips for active filters and quick categorization.
- Do not replace badges with chips where the purpose is status display only.

---

## Navigation

### Primary Navigation

The main navigation should be module-based and persist across authenticated screens.

Modules:

1. `Home`
2. `Inventory`
3. `Products`
4. `Locations`
5. `Procurement`
6. `Inbound`
7. `Fulfillment`
8. `Transfers`
9. `Returns`
10. `Reports & Analytics`
11. `Governance & Audit`
12. `Administration`

### Navigation Style

- Vertical left sidebar by default
- Dark background, light text
- Current module highlighted with stronger surface and left accent bar
- Nested items shown in the secondary navigation region or local sidebar

### Navigation Behavior

- Expanded by default on desktop
- Collapsible to icon-only mode
- Drawer on tablet/mobile
- Role-based visibility: show only relevant modules

---

## Sidebar

### Sidebar Specification

- Width expanded: `248px`
- Width collapsed: `72px`
- Background: `surface-sidebar`
- Text color: white or near-white with muted variants for secondary items

### Sidebar Sections

- product / system brand area
- main nav links
- optional pinned shortcuts
- bottom area for collapse toggle

### Sidebar Item States

- default
- hover
- active
- keyboard focus
- collapsed tooltip state

### Sidebar Rules

- Keep icons aligned and consistent.
- Show item labels clearly in expanded state.
- Use concise enterprise labels.

---

## Header

### Header Specification

- Height: `64px`
- Background: white
- Border bottom: `1px solid color-neutral-200`
- Horizontal padding: `16px` to `24px`

### Header Content

- page or module context
- global search
- notifications
- tasks / approvals shortcut
- session context badge
- user menu

### Header Variants

- unauthenticated header
- standard operational header
- executive header
- admin header

### Header Rules

- Search should remain visible on desktop.
- Utility controls should remain grouped on the right.
- Use concise indicators for unread counts and role/location context.

---

## Footer

### Footer Role

The footer is lightweight and informational, not promotional.

### Footer Types

- global app footer
- page metadata strip
- record metadata strip
- report footer

### Footer Content

- last updated timestamp
- data as-of timestamp
- record created/updated metadata
- version or environment when needed

### Footer Style

- Small text
- light divider
- low visual weight

---

## Pagination

### Pagination Purpose

Pagination supports large enterprise tables and reports without overwhelming users.

### Pagination Specification

- Position: bottom-right of tables by default
- Include:
  - previous/next
  - page numbers
  - page size selector
  - total items summary

### Recommended Page Sizes

- `10`
- `25`
- `50`
- `100`

### Pagination Rules

- Default to `25` for standard list screens.
- Default to `50` for operational queues where scanning speed matters.
- Keep pagination aligned with table width and visible after filtering.

---

## Layout Patterns

## Dashboard Pattern

Use for executive and operational summaries.

Structure:

- page title and filter bar
- KPI cards row
- summary widgets
- task or alert table
- quick action area

## List-Detail Pattern

Use for products, suppliers, users, locations, and many admin screens.

Structure:

- search/filter bar
- results table or list
- detail panel or detail page region
- metadata footer

## Queue Workbench Pattern

Use for receiving, put-away, counting, fulfillment, approvals, and returns.

Structure:

- task queue
- current task detail
- action panel
- status summary

## Report Viewer Pattern

Use for analytics, movement history, valuation, and audit.

Structure:

- filter bar
- result area
- detail/drill-down
- export actions

---

## Motion and Interaction

### Motion Principles

- Minimal and purposeful
- Fast response for operational workflows
- No decorative animation in task-heavy screens

### Recommended Motion

- 120ms to 180ms hover/focus transitions
- 180ms to 220ms panel open/close
- subtle fade/slide for banners and dialogs

### Avoid

- long easing animations
- bouncing or playful effects
- transitions that slow repeated data entry

---

## Elevation, Borders, and Radius

### Elevation

| Token | Use |
|---|---|
| `elevation-0` | flat app background |
| `elevation-1` | cards, panels |
| `elevation-2` | dropdowns, menus |
| `elevation-3` | dialogs |

Use shadow sparingly. Borders should carry most structural separation.

### Border Radius

| Token | Value | Use |
|---|---:|---|
| `radius-sm` | 6px | tags, compact controls |
| `radius-md` | 8px | inputs, buttons |
| `radius-lg` | 12px | cards |
| `radius-xl` | 16px | dialogs, large panels |
| `radius-pill` | 999px | badges, chips |

---

## Accessibility Standards

### Core Standards

- Target `WCAG 2.2 AA`
- All critical flows keyboard operable
- Visible focus on all controls
- Clear heading hierarchy
- Error messages programmatically associated with fields
- Tables use true table semantics
- Dialogs trap focus correctly
- Statuses never depend on color alone

### High-Priority Accessible Components

- queue workbenches
- data tables
- editable line-item grids
- approval panels
- permission matrix
- global navigation

---

## Enterprise Dashboard Style Notes

To keep the IMS visually aligned with modern ERP systems:

- Use generous structure, not excessive decoration.
- Keep surfaces mostly neutral with brand color used as an accent.
- Favor bordered cards and clean panel separation over strong shadows.
- Use clear iconography and visible labels for operational scanning.
- Maintain a compact but readable density model.
- Prioritize data clarity, state clarity, and action clarity over visual novelty.

---

## Recommended Design Tokens Summary

### Core Tokens

- colors: brand, neutral, semantic, surface
- typography: headings, body, label, mono
- spacing: 4px-based scale
- radius: 6 / 8 / 12 / 16 / pill
- layout: 12-column desktop grid
- shell: 248px sidebar, 64px header

### Default Component Sizes

- button height: `40px`
- input height: `40px`
- badge height: `24px`
- chip height: `28px` to `32px`
- table row height: `48px`
- card padding: `16px` or `24px`

---

## Usage Guidance for AI Design Tools

When using this design system in Figma AI or similar tools:

- Generate a desktop-first ERP dashboard design.
- Use a dark left sidebar and light content area.
- Use white cards on a soft neutral app background.
- Use blue as the main action color.
- Use green, amber, red, and purple for semantic enterprise states.
- Use Inter or a similar neutral enterprise sans-serif.
- Favor bordered cards, compact tables, structured forms, and high-scannability layouts.
- Avoid consumer-app aesthetics such as oversized hero sections, playful gradients, oversized rounded blobs, or excessive illustration.

## Final Design Intent

The IMS design system should feel like a modern, dependable enterprise operating environment:

- precise
- calm
- efficient
- informative
- role-aware
- scalable
- accessible

It should support fast daily execution for warehouse and operations users while still feeling robust enough for finance, audit, and administrative control workflows.
