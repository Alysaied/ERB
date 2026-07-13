# Figma AI Prompts for Inventory Management System

## UI-001 Sign In / Session Entry

Design a desktop-first enterprise sign-in screen for an Inventory Management System at 1440px width, with a tablet adaptation at 1024px and a mobile adaptation for small screens. Use a minimal unauthenticated layout with a light background `#F9FAFB`, a compact top header on white, and a centered sign-in card on a clean canvas. The screen should feel trustworthy, structured, calm, and operational rather than marketing-oriented.

Use Inter typography with a strong page heading in 28px bold, card title in 20px semibold, body text in 14px regular, helper text in 13px, and compact badge or metadata text in 12px semibold. Use a restrained enterprise palette: deep brand navy `#0F2A43` and action blue `#1D4E89` / `#2563A6` for primary actions and focus states, neutrals from `#111827` to `#F3F4F6` for text and surfaces, and semantic colors only for alerts. The main sign-in card should be white with a subtle border `#E5E7EB`, 12px corner radius, very soft shadow, and 24px padding.

Include these components: small unauthenticated header with product name, centered sign-in card, lock icon near the card title, labeled username or email field, labeled password field, remember me checkbox, primary `Sign In` button, secondary text link for `Forgot Password` or `Need Help`, top-of-form error banner, and lightweight footer with version, privacy, and security note. Inputs should be 40px tall with 8px radius, 12px horizontal padding, label above field, 6 to 8px label spacing, visible focus ring in brand blue, and strong error state in red `#B91C1C` with tinted error background `#FEE2E2`.

Spacing should follow a 4px system with 24px outer page padding, 24px card padding, 16px vertical spacing between form controls, 8px between labels and inputs, and 12px to 16px between inline elements. Use simple outline icons at 18px to 20px. Responsive behavior: on desktop keep the card centered with generous whitespace; on tablet keep the same centered pattern with slightly narrower width; on mobile use a single-column full-width card with large touch targets, no horizontal scroll, and the footer stacked vertically. Do not include any data tables. The dashboard style should not appear here; keep this screen intentionally minimal and authentication-focused.

## UI-002 Operational Home Dashboard

Design a desktop-first operational home dashboard for an Inventory Management System at 1440px width, with a tablet adaptation at 1024px and a mobile adaptation for small screens. Use a modern ERP-style shell with a dark left sidebar `#0F2A43`, white top header, and light content background `#F9FAFB`. The layout should feel dense but readable, highly scannable, role-aware, and action-oriented.

Create a page structure with persistent global header, left navigation, breadcrumb, page title bar, filter bar, top KPI row, alert and task widgets, and workflow shortcut tiles. Use a 12-column desktop grid with 32px outer margin at xl, 24px gutters, 24px page padding, 64px header height, 248px expanded sidebar, and card-based dashboard sections. Use white cards with `#E5E7EB` borders, 12px radius, 16px to 24px padding, and minimal shadows.

Include these components: global search, notifications, tasks or approvals shortcut, session or role badge, location and date filter bar, KPI summary cards, status summary strip, recent alerts table, pending tasks table, and quick action tiles linking to core workflows. Tables should use sticky headers, 44px table header height, 48px rows, 12 to 16px cell padding, sortable columns, row actions, status badges, pagination, and empty-state rows. Use compact forms in the filter bar with searchable selects and date inputs.

Apply the enterprise color system: brand blue `#1D4E89` for primary actions and selected states, white surfaces, neutral text `#111827` / `#1F2937`, border `#E5E7EB`, success `#15803D`, warning `#B45309`, danger `#B91C1C`, and info `#1D4ED8`. Typography should use Inter: page heading 28px bold, section titles 18 to 20px semibold, KPI values large and bold, table and form text 14px, metadata 13px, and badge labels 12px semibold.

Use outline icons at 18px to 20px: notification bell, checklist, inventory box, warning icon, and trend arrows. Responsive behavior: desktop shows full dashboard grid with multiple widgets; tablet stacks cards into fewer columns and simplifies low-priority widgets; mobile shows summary cards, alerts, and tasks as compact cards or lists, with filters in a drawer and tables converted to simplified list rows. Dashboard style should be strongly operational: bordered KPI cards, clear status badges, alert-driven panels, fast scanning, and no decorative hero elements.

## UI-003 Executive KPI Dashboard

Design a desktop-first executive KPI dashboard for an Inventory Management System at 1440px width with a tablet adaptation at 1024px. Use a refined analytics layout inside the same enterprise shell: dark left sidebar, white top header, light neutral app background, and a spacious but still structured dashboard for senior stakeholders.

Use a page structure with breadcrumb, page title, period filter bar, top KPI card row, trend summary blocks, target variance region, drill-down action group, and a KPI summary table beneath. Keep the layout wide, clean, and readable with 12 columns, 24px page padding, and generous separation between dashboard sections. Use white bordered cards with 12px radius and minimal elevation. Charts or data visuals should be simple and businesslike, with direct labeling and not overly stylized.

Include components such as date range picker, business unit and location group filters, KPI summary cards with values and targets, trend indicators, variance blocks, export controls, and a KPI summary table with value, target, variance, trend, and status columns. Tables should be compact yet readable, with sticky headers, clear numeric alignment, and visible status badges. Forms in the filter bar should be dense and efficient, with labels above inputs and helper text only where needed.

Use Inter typography with an optional 32px display title for the main dashboard heading, 24px and 20px section headings, 16px large body text where needed, 14px standard UI text, and 12 to 13px table headers and badges. Use brand navy and blue for emphasis, mostly neutral surfaces, and semantic states sparingly: green for good performance, amber for at risk, red for underperformance, and blue for informational trends. Use 20px outline icons for trend arrows, target, export, and underperformance warnings.

Responsive behavior: desktop presents full analytics cards and wide table; tablet keeps the KPI cards and a simplified or narrower comparison table; mobile is not a priority here, but if visualized at all it should be a read-only stacked KPI summary. Dashboard style should feel strategic, precise, quiet, and credible, similar to a modern ERP executive overview.

## UI-004 Notification Center

Design a desktop-first notification center for an Inventory Management System at 1440px width, with a tablet adaptation at 1024px and a mobile adaptation. Use the enterprise shell with dark sidebar, white header, and a light neutral content background. The layout should resemble an enterprise inbox: structured, high-signal, and easy to triage quickly.

Create a list-detail workspace with a filter area at the top, saved views, a notification list table on the left, and a selected notification detail panel on the right. The desktop split should feel like 35/65 or 40/60. Use white panels with clear borders, 12px radius, subtle shadows, and dense-but-readable spacing. Include breadcrumb and page title bar above the workspace.

Include these components: global header utilities, filter bar with type, priority, module, status, and date filters, saved-view chips, notification list table, detail panel, alert detail card, status badge, and action buttons for `Open Related Record`, `Mark as Handled`, `Acknowledge`, and `Refresh`. The notification table should include columns for type, priority, source module, age, and status, with compact rows, sticky header, inline unread indicator, row actions, selection state, and pagination. Detail panel should show context, message body, metadata, related record information, and actions.

Use Inter typography and the enterprise color system. Keep white cards on `#F9FAFB`, borders in `#E5E7EB`, primary text in `#111827`, secondary text in `#4B5563`, blue selected states, warning amber for high priority, red for blocking alerts, and purple for governance-related items. Use 18px to 20px outline icons: bell, check, warning triangle, delay clock, unread dot, and related record icons.

Use 24px page padding, 16px to 24px panel padding, 16px vertical spacing for forms, and 12px to 16px table cell padding. Responsive behavior: desktop uses split inbox layout; tablet stacks list over detail or uses tabs; mobile uses a filter drawer and a full-screen drill-in detail screen, with the notification list becoming cards instead of a dense table. Dashboard style should be operational inbox style rather than a broad KPI dashboard.

## UI-005 Product Catalog Management

Design a desktop-first product catalog management screen for an Inventory Management System at 1440px width with a tablet adaptation at 1024px. Use a list-detail enterprise workspace within a dark-sidebar, light-content ERP shell. The screen should feel structured, dense, reliable, and optimized for master data maintenance.

Use a page structure with breadcrumb, page title bar, top action bar, search and filter toolbar, product table, and a detail panel or detail region for the selected product. Keep a 35/65 or 40/60 split for table and detail on desktop. Use white panels with borders, 12px radius, and minimal shadow over a `#F9FAFB` app background.

Include components: filter bar, searchable product table, detail panel, structured form sections, status badges, metadata block, and validation banner. The product table should include SKU, product name, category, lifecycle status, ABC class, and row actions. The form should include SKU, name, description, unit of measure, category, barcode, traceability settings, shelf-life settings, and lifecycle status. Use compact form sections with clear headings and inline validation. Include actions for `Create Product`, `Edit`, `Save`, `Change Status`, and `Resolve Duplicate`.

Use enterprise table behavior: 44px header, 48px rows, sticky header, sortable columns, pinned key identifiers to the left, right-aligned numeric fields where relevant, status badges, pagination, skeleton rows, and empty states. Typography should use Inter with 28px page heading, 18px section headings, 14px form and table text, 13px helper text, and 12px badges. Color palette: action blue, neutral surfaces, success, warning, and danger used carefully. Icons should be simple outline style: box or product icon, edit icon, duplicate warning, and lifecycle chip icons.

Use spacing on a 4px system with 24px outer page padding, 24px card and detail panel padding, 16px between form fields, and 8px between label and input. Responsive behavior: desktop keeps table and detail visible together; tablet can switch detail to tabs or a larger slide-in panel; mobile should favor search and read-heavy detail only, not full master-data editing. Dashboard style should be absent here; focus on list-detail master data administration.

## UI-006 Product Import Workspace

Design a desktop-first multi-step product import workspace for an Inventory Management System at 1440px width with a tablet adaptation at 1024px. Use the same enterprise shell with a dark sidebar, white header, and light neutral background, but make the central content a guided workflow rather than a list-detail page.

Use a page structure with breadcrumb, page title, a horizontal step indicator, template instructions panel, upload zone, validation results table, and completion summary area. The visual style should feel controlled, procedural, and enterprise-ready for bulk data operations. Use white cards with 12px radius, light borders, and minimal shadow.

Include these components: step progress indicator, import mode selector, source reference field, file upload area that supports drag-and-drop and manual selection, `Download Template`, `Upload File`, `Validate`, `Confirm Import`, and `Cancel` actions, validation table, summary cards, and banner messages for status. The validation errors table should support row-level issues, severity or blocking status badges, and clear cell-level references. The completion summary table should show created, updated, skipped, and failed row counts.

Use Inter typography, 14px default interface text, 13px for table details, bold section headings, and monospaced treatment for file names or import references when useful. Use blue as the primary action color, neutrals for structure, amber for warnings, red for blocking errors, and green for successful completion. Use outline icons for upload, download, warning, success, and document states at 18px to 20px.

Spacing should follow the 4px scale with 24px page padding, 16px or 24px card padding, 16px between sections, and 12px to 16px table cell padding. Responsive behavior: desktop and tablet support the full workflow; mobile should not attempt full import execution, only template download and import status review. Tables should be dense and highly scannable, with sticky headers, pagination, and skeleton loading rows. Dashboard style should not dominate; this is a guided workflow workspace.

## UI-007 Location and Warehouse Management

Design a desktop-first location and warehouse management screen for an Inventory Management System at 1440px width with a tablet adaptation at 1024px. Use a three-zone enterprise workspace inside a dark-sidebar ERP shell with white header and neutral content area. The screen should feel operational, hierarchical, and highly structured.

Create a layout with breadcrumb, page title, location list table, hierarchy tree view, and a location detail area with a storage positions subsection. On desktop, the layout should clearly support three panes: left list, center hierarchy tree, right detail. Use white bordered panels with 12px corner radius and low-elevation shadows. Keep the overall experience dense but not cramped.

Include components: location table, keyboard-friendly hierarchy tree, detail panel, storage position editor, metadata strip, and confirmation dialog entry points. The location list table should include code, name, type, parent, status, and row actions. The storage positions table should include zone, aisle, bin, and status. The detail form should include code, name, type, parent, status, dates, and operating metadata. Actions include `Create Location`, `Edit`, `Save`, `Activate`, `Deactivate`, and `Close Location`.

Use Inter typography, 28px page heading, 18px panel titles, 14px table and form text, 13px metadata and helper text, and 12px badge labels. Use the enterprise palette with dark navy sidebar, neutral content surfaces, blue interactive accents, green for active, amber for caution, red for blocked or close-related warnings, and purple sparingly for controlled states. Icons should be outline style: warehouse or building, hierarchy tree, location pin, and activation or deactivation icons.

Use 24px page padding, 16px to 24px panel padding, 16px field spacing, and 12px to 16px cell padding. Tables should use sticky headers, row actions, status badges, and pagination. Responsive behavior: desktop uses the full three-zone view; tablet collapses hierarchy into tabs or an accordion; mobile should be mostly read-only with simplified lookup. Dashboard style is not primary here; the screen should emphasize list-detail plus hierarchy management.

## UI-008 Stock Policy and Threshold Management

Design a desktop-first stock policy and threshold management screen for an Inventory Management System at 1440px width with a tablet adaptation at 1024px. Use the enterprise shell with a dark left sidebar, white header, and light neutral background. The design should feel precise, numeric, and policy-driven.

Create a page with breadcrumb, title bar, filter and selector area, policy summary card, editable threshold panel, and supporting policy table. Use a structured layout where the selector and summary appear above or beside the editable form on desktop. Surfaces should be white with `#E5E7EB` borders, 12px radius, and subtle shadows.

Include components: filter bar, location selector, SKU selector, policy summary card, existing policy table, numeric form fields for reorder level, minimum threshold, safety stock, maximum threshold, and effective-from date, plus validation block and metadata footer. Include actions for `Search`, `Edit Policy`, `Save`, and `Reset`. The table should be compact and readable with sortable columns, sticky headers, right-aligned numeric values, badges, and pagination.

Use the IMS color palette: blue for interactive states and focus, neutral greys for structure, amber for threshold warnings, red for invalid cross-field combinations, and green for successful save states. Typography should use Inter, with strong section headings and 14px standard interface text. Include outline icons at 18px to 20px such as a threshold slider, alert indicator, and policy document icon.

Spacing should use a 4px system with 24px page padding, 16px or 24px card padding, 16px between form controls, and 8px label spacing. Responsive behavior: desktop and tablet support full editing; mobile should support only lookup or limited single-record edits. Dashboard style should be light and functional, centered on forms and tables rather than KPI storytelling.

## UI-009 ABC Classification Management

Design a desktop-first ABC classification management screen for an Inventory Management System at 1440px width with a tablet adaptation at 1024px. Use the standard ERP shell with dark left sidebar, white top header, and soft neutral content background. The screen should feel data-driven, scannable, and optimized for batch classification work.

Use a layout with breadcrumb, page title, top summary strip, classification filter bar, product classification table, and detail or edit panel. Keep the desktop workspace in a list-detail format with space for bulk actions. Use white bordered cards and panels with 12px radius and compact but readable spacing.

Include components: summary strip, filters for category, current class, and activity status, classification table, bulk action toolbar, class assignment control using segmented buttons or dropdown, reason and effective date inputs, metadata strip, and actions for `Assign Class`, `Save`, and `Bulk Update`. The main table should show product, category, current class, activity indicators, and row actions. Tables should support sticky headers, row selection, bulk selection checkboxes, pagination, and inline status badges.

Use the enterprise palette with blue for selected and active states, neutral borders and text, amber for unclassified attention states, and minimal use of semantic color elsewhere. ABC badges should be distinct and readable, paired with text labels, not color alone. Use Inter typography with 14px interface text, 13px dense table text if needed, 18px section titles, and 12px semibold badges. Use outline icons for product, A/B/C classification markers, and warnings.

Use 24px page padding, 16px to 24px card padding, 16px between controls, and 12px to 16px cell padding. Responsive behavior: desktop and tablet support full classification work; mobile uses simplified filters and drill-in editing only, not bulk updates. Dashboard style should be minimal; focus on a clean enterprise table and decision workflow.

## UI-010 Governance Policies and Reason Codes

Design a desktop-first governance policies and reason codes administration screen for an Inventory Management System at 1440px width with a tablet adaptation at 1024px. Use the standard enterprise shell with dark sidebar, white header, and neutral content background. The screen should feel controlled, auditable, and formal.

Create a tabbed interface with two major tabs: `Policies` and `Reason Codes`. Each tab should use a list-detail layout with tables, forms, status badges, publish or retire actions, and metadata. Use white cards and panels with crisp borders, 12px radius, and low visual noise. Keep a clear heading hierarchy and strong structural separation between tab content areas.

Include components: semantic tabs, policy table, reason code table, titled form sections, publish actions, status badges, metadata block, validation banners, and dialogs for sensitive actions. Policy forms should include name, version, thresholds, tolerances, dates, and status. Reason code forms should include code, description, transaction types, active state, and retirement information. Include `Create Policy`, `Publish`, `Create Reason Code`, `Retire`, and `Save` buttons.

Use Inter typography with 28px page heading, 18px section titles, 14px standard UI text, 13px helper text, and monospaced treatment for code fields if useful. Use the enterprise color system with blue action accents, neutral surfaces, green for published and active states, red for retire or failure states, and purple accents for governance-sensitive statuses. Use outline icons for policy document, shield, reason-code tag, and version history.

Use 24px outer padding, 16px to 24px panel padding, 16px form spacing, and 12px to 16px table cell padding. Tables should support sticky headers, row actions, status badges, and pagination. Responsive behavior: desktop-first due to dense governance forms, tablet acceptable with stacked sections, and mobile read-only at most. Dashboard style should be restrained and administrative, not KPI-focused.

## UI-011 Supplier Management

Design a desktop-first supplier management screen for an Inventory Management System at 1440px width with a tablet adaptation at 1024px. Use a list-detail ERP workspace within a dark left sidebar, white header, and light neutral background. The visual tone should be businesslike, clear, and optimized for vendor record maintenance.

Use a page structure with breadcrumb, title bar, supplier table on the left, and supplier detail or edit form on the right. Keep a 35/65 or 40/60 split for desktop. Surfaces should be white with light borders, 12px radius, and subtle shadows. Include a low-emphasis metadata strip for created and updated information.

Include components: supplier table with code, name, payment terms, lead time, active state, and row actions; detail panel; form sections; status badge; metadata strip; and actions for `Create Supplier`, `Edit`, `Save`, and `Deactivate`. The form should include supplier code, name, email, phone, payment terms, lead time, currency, consignment toggle, active toggle, and deactivation reason. Use inline validation and a compact but readable form layout.

Use Inter typography with 28px page heading, 18px panel titles, 14px body text, 13px helper text, and 12px badge labels. Use the enterprise color system with blue interactions, neutral structure, green for active, amber for cautionary states, and red for deactivation or errors. Icons should be simple outline style: supplier or building, contact, and warning or deactivate icons.

Use 24px page padding, 16px to 24px panel padding, 16px vertical form spacing, and 12px to 16px table cell padding. The table should have sticky headers, sortable columns, row actions, pagination, and empty or loading states. Responsive behavior: desktop and tablet support editing; mobile is suited for lookup only. Dashboard style should not dominate; this is a straightforward enterprise master-data screen.

## UI-012 Purchase Order Management

Design a desktop-first purchase order management screen for an Inventory Management System at 1440px width with a tablet adaptation at 1024px. Use the dark-sidebar, white-header ERP shell with a light neutral content area. The screen should feel robust, transaction-heavy, and optimized for reviewing and editing line-item-based documents.

Create a page with breadcrumb, title bar, search and filter area above a purchase order list table, and a selected purchase order detail region below or beside it. The detail area should include header fields, line items, a status timeline, metadata block, and action area. Use white panels with 12px radius, light borders, and minimal elevation.

Include components: filter bar, purchase order table, line-item table editor, structured header form, status timeline, metadata block, and confirmation dialog for sensitive actions. The purchase order table should show supplier, destination, expected date, status, and row actions. The line-item table should support SKU, quantity, UOM, price, notes, inline validation, add-row actions, and right-aligned numeric columns. Include `Create PO`, `Save Draft`, `Submit`, `Amend`, and `Cancel PO` buttons.

Use compact enterprise tables with sticky headers, 44px header height, 48px default rows, pagination, empty-state rows, and skeleton states. Use Inter typography: 28px page heading, 18px and 20px section headings, 14px table and form text, 13px helper text, 12px badge labels, and monospaced treatment for PO numbers if helpful. Use blue primary actions, neutral structure, amber for warnings, red for cancellation or blocking errors, and green for success messages.

Use 24px page padding, 16px to 24px card padding, 16px spacing between fields and sections, and 12px to 16px cell padding. Icons should be outline style: PO document, supplier, add-row, cancel warning. Responsive behavior: desktop-first, tablet supports stacked header and horizontally scrollable line table, mobile should be read-only or very limited. Dashboard style should be minimal; emphasize document editing and line-item clarity.

## UI-013 Purchase Requisition Management

Design a desktop-first purchase requisition management screen for an Inventory Management System at 1440px width with a tablet adaptation at 1024px. Use the shared ERP shell with dark sidebar, white header, and soft neutral background. The screen should feel like a queue-driven review and conversion workspace.

Use a queue-plus-detail layout with a requisition list on the left and a selected requisition detail on the center or right, with status history below or in a side section. Keep the detail view large enough to support line-item review and approval actions. Use white bordered panels, 12px radius, compact spacing, and strong information hierarchy.

Include components: queue list, requisition detail panel, line-item editor, approval decision panel, status timeline, and action buttons for `Create Requisition`, `Approve`, `Reject`, `Convert to PO`, and `Save`. The requisition table should include status, age, destination, and justification summary. The detail form should include receiving location, justification, line items, required date, supplier for conversion, expected delivery date, and rejection reason. Use inline validation and persistent draft states.

Use Inter typography, 14px standard UI text, 13px helper and metadata text, 18px panel titles, and 12px semibold status badges. Use the enterprise palette with blue for action emphasis, neutral backgrounds, green for approved, red for rejected, and amber for pending or caution states. Use outline icons for requisition document, approval, conversion arrow, and warnings.

Use 24px page padding, 16px to 24px panel padding, 16px form spacing, and compact table cell spacing. Tables should be sticky-header, sortable where useful, paginated, and equipped with skeleton states. Responsive behavior: desktop and tablet support full review and conversion; mobile may support approval review only. Dashboard style should not dominate; this is a queue workbench for decision-making.

## UI-014 Inbound Delivery Planning

Design a desktop-first inbound delivery planning screen for an Inventory Management System at 1440px width with a tablet adaptation at 1024px. Use the standard dark-sidebar ERP shell with a white header and `#F9FAFB` content background. The experience should feel logistics-focused, schedule-aware, and easy to scan.

Create a hybrid calendar-or-list planning workspace with breadcrumb, page title, date filters, inbound deliveries table, and a selected delivery detail panel. The page should prioritize structured planning over decorative visuals. Use white cards and panels, clear borders, 12px radius, and minimal shadow.

Include components: date filters, inbound deliveries table, detail panel, update form, and status badges. The table should show PO reference, supplier, ETA, carrier, destination, and delay state, with row selection, sticky header, pagination, and row actions. The detail form should include PO reference, shipment date, ETA, carrier, destination, and expected quantities by line. Include buttons for `Update Delivery`, `Save`, and `Notify Receiving`.

Use Inter typography with 28px page title, 18px section titles, 14px standard text, and 12px to 13px table headers. Use the IMS color system: blue for primary interactions, neutral text and surfaces, amber for delay, red for major issue states, and green for successful updates. Icons should be outline style: calendar, truck, delay clock, notification bell.

Use 24px page padding, 16px to 24px panel padding, and 16px control spacing. Responsive behavior: desktop and tablet support the full planning view; mobile should switch to a simpler list-based tracking view rather than a dense planner. Tables remain important, but the overall style is more schedule management than dashboard.

## UI-015 Goods Receipt Workbench

Design a desktop-first goods receipt workbench for an Inventory Management System at 1440px width with a tablet adaptation at 1024px. Use the enterprise shell with dark sidebar, white header, and neutral content background. This should be a high-priority warehouse workbench: fast, clear, keyboard-efficient, and scanner-friendly.

Use a queue workbench pattern with breadcrumb, page title, location context badge, pending receipt queue on the left, receipt detail in the main panel, line verification grid, status strip, and next-step actions. The layout should support continuous operational flow, with strong emphasis on the current task. Use white panels with borders, 12px radius, and subtle shadows.

Include components: pending receipts table, receipt line items table, scanner-ready inputs, step indicator, status strip, metadata block, and buttons for `Open Receipt`, `Verify`, `Log Discrepancy`, `Confirm Receipt`, and `Send to Put-Away`. The line grid should support accepted quantity, rejected quantity, condition, lot number, expiration date, and manufacture date, with clear row-level validation and right-aligned numeric values. Use loading skeletons that preserve the full workbench structure.

Use Inter typography with 28px page title, 18px section headers, 14px body and table text, 13px helper text, and monospaced styling for references like receipt IDs and POs. Use blue for primary controls, neutral structure, amber for discrepancy or traceability warnings, red for blocking validation, green for verified success, and purple for quarantine-like exceptions. Use 18px to 20px outline icons such as receiving dock, scanner, warning, success check, and put-away arrow.

Use 24px outer padding, 16px to 24px panel padding, 16px between major zones, and 12px to 16px cell padding. Responsive behavior: desktop and tablet must fully support the workflow; mobile should be limited to light verification or lookup only unless a special scanner flow is designed. Tables and forms are central; dashboard styling should be minimal and utility-driven.

## UI-016 Receipt Discrepancy Resolution

Design a desktop-first receipt discrepancy resolution screen for an Inventory Management System at 1440px width with a tablet adaptation at 1024px. Use the shared ERP shell with dark sidebar, white header, and soft neutral background. The screen should feel investigative, operational, and evidence-driven.

Use a queue-detail workspace with discrepancy list, discrepancy detail panel, comparison area for expected versus received values, and an evidence or notes section. The layout should make the discrepancy case the center of attention while still supporting fast queue movement. Use white cards and panels with 12px radius, crisp borders, and minimal shadow.

Include components: discrepancy queue table, variance comparison panel, evidence attachment area, form sections, status timeline, and actions for `Save Discrepancy`, `Resolve`, `Escalate`, and `Close`. The discrepancy table should show type, receipt reference, quantity variance, age, and status. The form should include discrepancy type, variance quantity, reason code, notes, evidence, resolution outcome, and resolution notes. Use inline validation and visible case status badges.

Use Inter typography with strong panel headings, 14px standard text, 13px helper and metadata text, 12px badges, and optional monospaced references for receipt IDs. Use the enterprise palette with blue interactions, neutral structure, amber for caution, red for blocking issues, and purple where governance or hold statuses are relevant. Use 18px to 20px outline icons like warning triangle, damaged item, attachment, and escalation.

Use 24px page padding, 16px to 24px panel padding, 16px control spacing, and 12px to 16px table cell padding. Responsive behavior: desktop and tablet support full discrepancy handling; mobile should support view and simple escalation only. Dashboard style should not dominate; this is a queue workbench and investigation screen.

## UI-017 Put-Away Workbench

Design a desktop-first put-away workbench for an Inventory Management System at 1440px width with a tablet adaptation at 1024px. Use the standard dark-sidebar ERP shell with a white header and soft neutral app background. The screen should feel warehouse-optimized, direct, and fast for repeated task completion.

Use a queue workbench layout with breadcrumb, page title, task queue on the left, task detail and destination confirmation on the right, plus a status strip and metadata footer. The interface should prioritize the active task with large enough controls for location confirmation and quantity visibility. Use bordered white panels with 12px radius and subtle depth.

Include components: pending put-away tasks table, task detail panel, storage position selector, status strip, metadata footer, and action buttons for `Open Task`, `Confirm Location`, `Complete Put-Away`, and `Reassign Location`. The task area should show receipt reference, product, quantity, suggested location, and actual location. The queue table should be compact, with sticky headers, row actions, and pagination when needed.

Use Inter typography with clear hierarchy, 14px standard text, 13px helper text, and monospaced references for task IDs or receipt codes if helpful. Use the enterprise palette with blue actions, neutral structure, green for completed states, amber for reassignment warnings, and red for blocking errors. Icons should be 18px to 20px outline style: shelf or bin, location marker, move arrow, and success check.

Use 24px page padding, 16px to 24px panel padding, 16px spacing between controls, and compact table cell spacing. Responsive behavior: desktop and tablet fully support the workbench; mobile should support only simplified confirm workflows. Dashboard style should be minimal and operational, with emphasis on queue progression and location action clarity.

## UI-018 Non-PO and Return Receipt Intake

Design a desktop-first non-PO and return receipt intake screen for an Inventory Management System at 1440px width with a tablet adaptation at 1024px. Use the shared ERP shell with dark sidebar, white header, and light neutral background. The screen should feel like a guided intake workflow for exception-based inbound processes.

Use a single-screen workflow layout with a receipt type selector at the top, intake form sections, line-entry area, and verification or confirmation section below. Keep the interface clear, structured, and easy to scan, with white bordered cards, 12px radius, and low shadow. Use strong section headers and visible action hierarchy.

Include components: segmented receipt-type selector, form sections, optional received line items table for multi-line entries, banner messages, and actions for `Start Intake`, `Verify`, `Confirm Receipt`, and `Cancel`. The form should include receipt type, authorization reference or return authorization, product, quantity, condition, notes, reason code, and source description. Inputs should be 40px high with 8px radius and visible focus states.

Use Inter typography with 28px title, 18px section headings, 14px body and form text, 13px helper text, and 12px label or badge text. Use the enterprise palette with blue for primary interactions, neutral structure, amber for caution, red for invalid references or blocking problems, and green for successful confirmation. Use outline icons such as return arrow, intake inbox, approval reference, and warning.

Use 24px page padding, 16px to 24px card padding, 16px form spacing, and 12px to 16px table cell padding. Responsive behavior: tablet supports the full intake flow; mobile should support only simple single-line intake; desktop is preferred for multi-line processing. Dashboard style should not appear; this is a transactional intake screen.

## UI-019 Inbound Supply Tracking

Design a desktop-first inbound supply tracking screen for an Inventory Management System at 1440px width with a tablet adaptation at 1024px. Use the enterprise shell with a dark sidebar, white header, and light app background. The screen should feel like a monitoring and drill-down surface for open inbound supply.

Use a page structure with breadcrumb, title bar, filter bar, open supply table, status badges, and a PO drill-in detail panel. The overall layout should be a list-detail monitoring screen with compact density and clear exception visibility. Use white panels, `#E5E7EB` borders, 12px radius, and low shadow.

Include components: supplier, location, status, and expected date filters; open supply table; detail panel; refresh controls; and actions for `View PO`, `Update Delivery Status`, and `Refresh`. The table should show open PO and inbound supply data, support sorting, sticky headers, row actions, pagination, and inline delay badges. The detail panel should show contextual supply information and related PO details.

Use Inter typography with 28px page title, 18px section titles, 14px standard UI text, and 12px to 13px dense table labels. Use the enterprise palette with blue interactions, neutral backgrounds, amber for delay, red for critical issues, and green for healthy status signals. Icons should be outline style: truck, delay clock, and PO document.

Use 24px page padding, 16px to 24px panel padding, 16px control spacing, and 12px to 16px cell padding. Responsive behavior: desktop and tablet support full tracking; mobile should provide summarized read-only tracking. Dashboard style should be light and data-focused, not heavy on KPI cards.

## UI-020 Inventory Status Monitor

Design a desktop-first inventory status monitor for an Inventory Management System at 1440px width with a tablet adaptation at 1024px. Use a modern ERP shell with dark left sidebar, white top header, and a neutral background. The screen should blend analytics and operational workbench behavior, optimized for stock visibility and action routing.

Use a page structure with breadcrumb, title bar, filter bar, top summary or KPI cards, a central stock board or inventory status table, and a drill-down detail panel. The table should be the dominant element, supported by lightweight KPI cards rather than an oversized dashboard. Use bordered white cards and panels with 12px radius and minimal shadow.

Include components: filter bar, KPI or status cards, inventory status table, detail panel, drill-down links, and action menu buttons for `View Detail`, `Request Transfer`, `Open Replenishment`, `Create Adjustment`, and `Refresh`. The table should show SKU, location, on-hand, reserved, ATP, and stock status with sticky header, sortable columns, inline badges, row actions, pagination, empty states, and skeleton rows.

Use Inter typography with 28px title, 18px section titles, 14px table and form text, 13px metadata text, and monospaced treatment for SKUs where appropriate. Use blue for interaction, green for available stock, amber for low stock, red for out of stock or blocked states, purple for quarantine or hold, and neutral surfaces elsewhere. Icons should be outline style: box, low-stock warning, out-of-stock indicator, quarantine lock, and transfer arrows.

Use 24px page padding, 16px to 24px panel padding, and 12px to 16px table cell padding. Responsive behavior: desktop-first; tablet shows fewer columns and keeps a drill-in panel; mobile uses summary cards and drill-in stock cards rather than a wide table. Dashboard style should feel operational and data-first.

## UI-021 Inventory Availability Inquiry

Design a desktop-first inventory availability inquiry screen for an Inventory Management System at 1440px width, with a tablet adaptation at 1024px and a mobile adaptation. Use the shared ERP shell with dark sidebar, white header, and soft neutral background. The screen should support quick answer workflows for sales and service users.

Create a layout with a search panel at the top, product search results below, and a selected product availability detail view with an optional network availability table. Keep the UI simple, quick, and highly scannable. Use white bordered panels and cards with 12px radius and low-elevation shadows.

Include components: search bar, search form with SKU, name, barcode, category, and optional location scope, results table, availability summary card, location availability table, and action shortcuts for `Search`, `View Network Availability`, and `Reserve from Order`. Tables should support sticky headers, compact rows, pagination, inline badges, and empty states. The availability summary should clearly differentiate on-hand, reserved, and ATP values.

Use Inter typography with 28px page title, 18px section titles, 14px interface text, 13px helper text, and monospaced style for SKU references if helpful. Use blue as the primary action color, neutral structure, green for available, amber for low, red for unavailable, and blue or neutral for informational states. Use outline icons at 18px to 20px such as search, ATP info, network, and reserve lock.

Use 24px page padding, 16px to 24px panel padding, 16px vertical form spacing, and 12px to 16px table cell padding. Responsive behavior: desktop and tablet support the full inquiry experience; mobile should work well using stacked product cards and a compact location list. Dashboard style should be very light; this is a utility inquiry screen.

## UI-022 Inventory Movement History

Design a desktop-first inventory movement history screen for an Inventory Management System at 1440px width with a tablet adaptation at 1024px. Use the standard ERP shell with dark sidebar, white header, and a neutral background. The screen should feel investigative, audit-friendly, and centered on a large results table.

Use a layout with breadcrumb, page title, query or filter form at the top, movement history table beneath, and an adjacent or lower transaction detail panel. Make the table the dominant element. Use bordered white panels with 12px radius, minimal shadow, and dense but readable spacing.

Include components: filter bar, date range picker, movement history table, detail panel, and export actions. The table should include transaction date, type, product, location, quantity, actor, and reference, with sticky header, sorting, pagination, empty state row, and skeleton loading rows. The filter form should include SKU, location, transaction type, user, and date range. Include `Search`, `Open Transaction`, and `Export` buttons.

Use Inter typography with strong page heading, 14px body and table text, 13px helper text, and monospaced text for transaction IDs, SKUs, or references. Use the enterprise palette with blue interactions, neutral text and surfaces, and restrained semantic colors for statuses or export confirmations. Use simple outline icons like history clock, movement arrows, export, and audit detail.

Use 24px page padding, 16px to 24px panel padding, and 12px to 16px table cell padding. Responsive behavior: desktop and tablet supported; mobile should be limited to simplified search and detail lookup. Dashboard style should not be prominent; this is a report-viewer and history query screen.

## UI-023 Cycle Count Workbench

Design a desktop-first cycle count workbench for an Inventory Management System at 1440px width with a tablet adaptation at 1024px. Use the standard dark-sidebar ERP shell with white header and light neutral background. The screen should feel task-oriented, focused, and warehouse-efficient.

Use a queue workbench pattern with breadcrumb, title bar, assigned counts queue, count-entry panel, confirmation area, status strip, and metadata footer. The layout should support fast sequential completion of blind counts without showing system quantities. Use white bordered panels with 12px radius and minimal shadows.

Include components: assigned counts table, count-entry form, status strip, metadata footer, and actions for `Open Count`, `Submit Count`, and `Save Draft`. The form should include counted quantity and optional notes, with strong visual separation between task context and entry controls. Use loading skeletons that preserve the workbench structure and clear empty-state messaging.

Use Inter typography with 28px page title, 18px panel headings, 14px form and table text, 13px helper text, and monospaced treatment for assignment references if useful. Use the enterprise palette with blue actions, neutral surfaces, green for submitted success, amber for caution, and red for blocking validation. Use 18px to 20px outline icons such as count checklist, location pin, and completion check.

Use 24px page padding, 16px to 24px panel padding, 16px between major controls, and compact table cell spacing. Responsive behavior: tablet support is important and should remain fully usable; mobile may support single-task submission if optimized. Dashboard style should be absent; this is a queue-driven warehouse task screen.

## UI-024 Physical Inventory Count Management

Design a desktop-first physical inventory count management screen for an Inventory Management System at 1440px width with a tablet adaptation at 1024px. Use the enterprise shell with dark sidebar, white header, and a neutral content background. The screen should feel controlled, operational, and suitable for overseeing a wall-to-wall count.

Use a page structure with breadcrumb, page title, count session summary cards, progress widgets, zone or team assignment table, certification panel, and status timeline. The layout should look like a management dashboard with operational depth, not a marketing dashboard. Use white bordered cards and panels with 12px radius and low shadow.

Include components: session summary cards, count progress table, zone or team assignment table, certification form, status timeline, and buttons for `Start Count`, `Assign Teams`, `Monitor Progress`, `Certify Count`, and `Release Freeze`. Tables should use sticky headers, compact rows, badges, and pagination. Forms should be structured with labels above inputs and visible validation states.

Use Inter typography with 28px title, 18px section headings, 14px UI text, 13px metadata, and 12px badges. Use the enterprise palette with blue actions, neutral surfaces, green for complete or certified states, amber for in-progress or pending areas, red for blockers, and purple or dark accents for freeze-related states. Icons should be outline style: inventory audit, freeze lock, certification checkmark, and team icon.

Use 24px page padding, 16px to 24px card padding, and 12px to 16px table cell padding. Responsive behavior: desktop-first; tablet supports review; mobile should be read-only for oversight. Dashboard style should be moderate: KPI summary cards plus data tables and control panels.

## UI-025 Variance Investigation and Approval

Design a desktop-first variance investigation and approval screen for an Inventory Management System at 1440px width with a tablet adaptation at 1024px. Use the standard ERP shell with dark sidebar, white header, and soft neutral background. The interface should feel investigative, controlled, and approval-focused.

Use a queue-plus-detail layout with a variance cases table, a side-by-side expected versus counted comparison panel, investigation notes area, evidence panel, approval controls, and status history. Keep the current case visually prominent. Use white panels with 12px radius, clear borders, and minimal shadow.

Include components: variance queue list, comparison panel, evidence panel, approval decision panel, status history, and actions for `Investigate`, `Approve`, `Reject`, and `Escalate`. The variance cases table should show age, product, location, variance amount, and status. The form should include root cause category, investigation findings, approved adjustment quantity, and approver note. Use inline validation and preserve draft notes in the design.

Use Inter typography with clear headings, 14px body text, 13px helper and metadata text, and 12px badges. Use blue for primary actions, neutral structure, amber for attention states, red for rejects or severe variances, and green for approvals. Use outline icons such as delta or variance, attachment, approve, and reject.

Use 24px page padding, 16px to 24px panel padding, 16px field spacing, and 12px to 16px cell padding. Responsive behavior: desktop and tablet support full investigation; mobile should support review only. Dashboard style should be minimal; this is an approval workbench with comparison-heavy detail.

## UI-026 Stock Adjustment Management

Design a desktop-first stock adjustment management screen for an Inventory Management System at 1440px width with a tablet adaptation at 1024px. Use the shared ERP shell with dark sidebar, white header, and light content background. The screen should feel procedural, auditable, and optimized for controlled stock corrections.

Use a page structure with breadcrumb, page title, adjustment cases table, detail form, reason code selector, evidence panel, approval or status summary, and banner areas. Keep the layout centered on form-and-table interaction. Use white bordered panels with 12px radius and low shadow.

Include components: adjustment table, form sections, reason-code selector, evidence area, approval badges, page-level alert banners, and buttons for `Create Adjustment`, `Submit`, `Approve`, `Reject`, and `Apply`. The form should include origin type, location, SKU, adjustment type, quantity, reason code, notes, evidence, and rejection reason. Tables should support sorting, sticky headers, badges, row actions, pagination, and skeleton states.

Use Inter typography with 28px page title, 18px section titles, 14px UI text, 13px helper text, and monospaced styling for adjustment references and SKUs if useful. Use blue for primary workflow actions, neutral structure, amber for caution, red for write-off or failure states, and green for success. Icons should be outline style: plus or minus adjustment, warning, approval, and attachment.

Use 24px page padding, 16px to 24px card padding, 16px field spacing, and 12px to 16px cell padding. Responsive behavior: desktop and tablet support full adjustment management; mobile should be limited to light approval or status review. Dashboard style should be absent; prioritize data entry, review, and audit clarity.

## UI-027 Write-Off Authorization

Design a desktop-first write-off authorization screen for an Inventory Management System at 1440px width with a tablet adaptation at 1024px. Use the enterprise shell with dark sidebar, white header, and neutral content background. The tone should feel high-control, risk-aware, and finance-conscious.

Use a queue-detail layout with a pending write-offs list on the left, selected request detail in the center, and evidence plus finance acknowledgment section on the right or below. Use white panels with clear borders, 12px radius, and minimal shadow. Keep the approval decision area visually distinct because it handles irreversible actions.

Include components: queue list, read-only review panel, approval decision panel, evidence attachment panel, finance acknowledgment area, and confirmation dialog pattern. Include actions for `Review`, `Approve`, `Reject`, and `Request More Info`. The table should be compact with sticky headers, badges, row selection, pagination, and aging indicators. The approval form should include decision, finance acknowledgment, approver note, and rejection reason.

Use Inter typography with strong heading hierarchy, 14px body and form text, 13px metadata, and 12px badges. Use the enterprise palette with blue for informational actions, green for approval, red for destructive or rejection decisions, amber for caution, and neutral surfaces elsewhere. Use outline icons at 18px to 20px such as write-off, finance ledger, attachment, and warning.

Use 24px page padding, 16px to 24px panel padding, 16px field spacing, and 12px to 16px cell padding. Responsive behavior: desktop and tablet support review; mobile can support simplified approval review. Dashboard style should be minimal; this is a review and authorization workbench.

## UI-028 Quarantine and Hold Register

Design a desktop-first quarantine and hold register for an Inventory Management System at 1440px width with a tablet adaptation at 1024px. Use the standard ERP shell with dark sidebar, white header, and a soft neutral content background. The screen should feel controlled, inventory-sensitive, and clearly status-driven.

Use a register layout with a main hold table, selected hold detail card, and an apply or release action panel. On desktop, the table should dominate with a side detail region. Use white bordered surfaces, 12px radius, low-elevation shadow, and a clean structured information hierarchy.

Include components: hold register table, detail card, status badges, apply or release form, metadata strip, and actions for `Apply Hold`, `Release Hold`, and `View Product`. The table should show product, location, quantity, hold type, reason, duration, and status with sticky header, sorting, row actions, inline badges, and pagination. The form should include quantity, hold reason, reason code, lot identity, disposition, and inspection reference.

Use Inter typography with 28px title, 18px section titles, 14px UI text, 13px helper text, and 12px pill badges. Use the enterprise palette with blue interaction accents, neutral structure, purple for quarantine or hold states, amber for caution, red for blocked severity, and green for successful release. Use outline icons such as quarantine, lock, unlock, and warning badge.

Use 24px page padding, 16px to 24px card padding, 16px form spacing, and 12px to 16px table cell padding. Responsive behavior: desktop and tablet support full register use; mobile may support lookup and simple release only. Dashboard style should be low; prioritize clear status communication and action safety.

## UI-029 Shrinkage, Loss, and Obsolescence Analysis

Design a desktop-first shrinkage, loss, and obsolescence analysis screen for an Inventory Management System at 1440px width with a tablet adaptation at 1024px. Use the enterprise shell with dark sidebar, white header, and neutral app background. The screen should feel analytical, finance-aware, and operationally credible.

Use an analytics layout with breadcrumb, page title, filter bar, KPI summary cards, chart zones, recommendations section, and supporting tables. Keep the design structured and restrained, with cards and charts that support decisions without looking flashy. Use white bordered cards with 12px radius, low shadow, and generous but efficient spacing.

Include components: filter bar, KPI cards, trend indicators, recommendation links, chart areas, shrinkage summary table, obsolete or aging items table, and actions for `Apply Filters`, `Export`, and `Open Adjustment Cases`. Tables should support sticky headers, numeric alignment, badges, pagination, and loading skeletons. Charts should be simple enterprise visuals with labels, legends, and direct annotations.

Use Inter typography with 28px page title, 18px section titles, 14px UI text, 13px metadata, and 12px chart labels or badge labels where needed. Use blue for interaction, neutral surfaces, amber for aging risk, red for shrinkage or loss severity, green for positive recovery or healthy states, and purple only if needed for governed exceptions. Use outline icons such as trend, loss warning, aging hourglass, and export.

Use 24px page padding, 16px to 24px card padding, and 12px to 16px table cell padding. Responsive behavior: desktop-first, tablet summary view is acceptable, mobile should be read-only KPI cards only. Dashboard style should be moderate and analytical, with strong table support and business charts.

## UI-030 Order Reservation Workbench

Design a desktop-first order reservation workbench for an Inventory Management System at 1440px width with a tablet adaptation at 1024px. Use the standard dark-sidebar ERP shell with white header and light neutral content background. The screen should feel operational, fulfillment-aware, and optimized for quick allocation decisions.

Use a queue-plus-detail workbench with an order queue or search panel, order line availability panel, and reservation summary area. Structure the desktop layout so the selected order becomes the dominant working context. Use white bordered panels with 12px radius, subtle shadows, and strong section separation.

Include components: orders table, order lines table, availability summary, reservation form, status timeline, and buttons for `Check Availability`, `Reserve Stock`, `Release Reservation`, and `Open Split Fulfillment`. Tables should support sticky headers, compact rows, row actions, badges, pagination, and empty-state messaging. The form should include selected fulfillment location, reservation quantity by line, release reason, and cancellation reason.

Use Inter typography with 28px page title, 18px section titles, 14px body and table text, 13px helper text, and monospaced formatting for order references if helpful. Use blue for primary actions, green for successful reservations, amber for low ATP or safety stock warnings, red for blocking unavailability, and neutral structure throughout. Use outline icons like order, reserve lock, ATP info, and split fulfillment network.

Use 24px page padding, 16px to 24px panel padding, and 12px to 16px table cell padding. Responsive behavior: desktop and tablet support the full workbench; mobile should support order lookup and release only, not full allocation management. Dashboard style should be absent; this is an action-heavy queue workbench.

## UI-031 Pick, Pack, and Ship Workbench

Design a desktop-first pick, pack, and ship workbench for an Inventory Management System at 1440px width with a tablet adaptation at 1024px. Use the enterprise shell with dark sidebar, white header, and neutral content background. The interface should feel highly operational, warehouse-ready, and optimized for sequential fulfillment tasks.

Use a workbench layout with task queue, pick verification panel, packing section, and shipment confirmation section inside a single workspace. Include visible shift or location context and ensure the current task stands out. Use white bordered panels with 12px radius and minimal elevation. Prioritize line-item clarity and fast repeated use.

Include components: pick queue table, pick line items table, scanner inputs, packing editor, shipment confirmation block, exception route actions, status strip, and step-specific actions for `Open Pick`, `Verify Pick`, `Pack`, `Raise Exception`, and `Confirm Shipment`. The line-item grid should support lot or batch data, picked quantity, package references, carrier, notes, and tracking reference. Use sticky headers, row validation, badges, and skeleton states.

Use Inter typography with strong panel headings, 14px standard text, 13px helper text, and monospaced styling for pick IDs or tracking references. Use blue for main actions, neutral surfaces, green for completion, amber for exceptions, red for blocking validation, and purple where hold or quarantine routing is relevant. Use 18px to 20px outline icons like pick cart, barcode scanner, package, shipment truck, and warning.

Use 24px page padding, 16px to 24px panel padding, 16px spacing between workflow sections, and 12px to 16px cell padding. Responsive behavior: desktop and tablet must support the workflow; mobile should only support carefully optimized warehouse tasks if included. Dashboard style should be minimal and utility-first.

## UI-032 Partial Fulfillment and Backorder Management

Design a desktop-first partial fulfillment and backorder management screen for an Inventory Management System at 1440px width with a tablet adaptation at 1024px. Use the standard ERP shell with dark sidebar, white header, and soft neutral background. The screen should feel exception-oriented and quantity-comparison heavy.

Use a list-detail workspace with affected orders list, quantity comparison panel, and backorder planning section. The selected case should present clear visual comparisons between full quantity, fulfill-now quantity, and backorder quantity. Use white panels with 12px radius, light borders, and subtle shadows.

Include components: cases table, comparison panel, line-item editor, acknowledgment section, status history, and buttons for `Confirm Partial Fulfillment`, `Create Backorder`, and `Cancel Remainder`. The table should be compact, sticky-header, paginated, and badge-enabled. The form should include fulfill-now quantity, backorder quantity, customer acknowledgment reference, expected date, and priority override reference.

Use Inter typography with 28px page title, 18px section titles, 14px standard text, and 13px helper text. Use blue for primary actions, neutral structure, amber for at-risk or pending states, red for canceled or blocked states, and green for confirmed outcomes. Use outline icons such as split shipment, backorder clock, and customer acknowledgment.

Use 24px page padding, 16px to 24px panel padding, 16px field spacing, and 12px to 16px cell padding. Responsive behavior: desktop and tablet support full management; mobile may support simplified customer-service review. Dashboard style should be minimal; focus on comparison, form decisions, and queue progression.

## UI-033 Fulfillment Exception Management

Design a desktop-first fulfillment exception management screen for an Inventory Management System at 1440px width with a tablet adaptation at 1024px. Use the standard enterprise shell with dark left sidebar, white top header, and light neutral content background. The screen should feel like an exception triage console.

Use a queue-detail layout with an exception queue, exception detail or context panel, and resolution options panel. Keep contextual routing links visible so users can move to repick, backorder, quarantine, or customer service actions. Use white bordered cards and panels with 12px radius and minimal shadow.

Include components: queue list, detail panel, resolution form, status timeline, contextual navigation links, and actions for `Resolve`, `Re-Pick`, `Partial Ship`, `Quarantine`, and `Route to Customer Service`. The fulfillment exceptions table should support type, age, order reference, location, status, row selection, pagination, and badges. The resolution form should include resolution type, notes, reassignment, and customer follow-up flag.

Use Inter typography with clear headings, 14px standard text, 13px metadata, and 12px badges. Use the enterprise palette with blue interactions, neutral structure, amber for open exceptions, red for severe failures, purple for quarantine routes, and green for completed resolutions. Use outline icons like warning triangle, retry or repick, partial ship, quarantine lock, and customer service.

Use 24px page padding, 16px to 24px panel padding, 16px control spacing, and 12px to 16px table cell padding. Responsive behavior: desktop and tablet support full exception management; mobile review is possible with simplified actions. Dashboard style should be absent; this is a queue-based resolution workbench.

## UI-034 Order Fulfillment Status

Design a desktop-first order fulfillment status screen for an Inventory Management System at 1440px width, with a tablet adaptation at 1024px and a mobile adaptation. Use the enterprise shell with dark sidebar, white header, and a neutral content background. The screen should be read-heavy, easy to scan, and ideal for service or operations inquiries.

Use a layout with order search bar, order status summary header, line-level progress table, and tabbed details for shipments, backorders, and exceptions. Keep the summary area strong but compact. Use white bordered cards and panels with 12px radius and low shadow.

Include components: search bar, search form, order summary card, status badges, line-status table, semantic tabs or segmented switcher, metadata strip, and buttons for `Search`, `View Shipment`, `View Exception`, and `View Backorder`. The line-status table should be compact, sticky-header, sortable where useful, paginated if necessary, and badge-rich. The search form should support order ID, customer reference, date, and status.

Use Inter typography with 28px page title, 18px section titles, 14px standard text, 13px metadata, and 12px status badges. Use blue for active interactions, green for complete stages, amber for backorder or pending risk, red for failed or exception states, and neutral surfaces elsewhere. Use outline icons like order, truck, warning, and backorder clock.

Use 24px page padding, 16px to 24px panel padding, and 12px to 16px table cell padding. Responsive behavior: desktop supports full detail, tablet simplifies table width, and mobile should use stacked order cards with collapsible line details and tab content. Dashboard style should be very light; this is a status inquiry screen.

## UI-035 Multi-Location Split Fulfillment Planner

Design a desktop-first multi-location split fulfillment planner for an Inventory Management System at 1440px width with a tablet adaptation at 1024px. Use the ERP shell with dark sidebar, white header, and soft neutral background. The interface should feel like a planning tool with network allocation intelligence.

Use a layout with order shortage summary, split allocation table, network availability summary, recommendation card, and location-specific reservation section. The allocation table should be the central element and should clearly show totals and remaining quantities. Use white bordered panels with 12px radius and subtle depth.

Include components: allocation table, network availability summary, recommendation card, confirmation banner, and actions for `Generate Plan`, `Adjust Allocation`, `Confirm Split`, and `Release to Queues`. The split allocation table should include location, quantity, ATP, shipping grouping, and allocation state, with inline validation, right-aligned quantities, sticky headers, and pagination if needed.

Use Inter typography with 28px title, 18px section titles, 14px UI text, 13px helper text, and monospaced style for order or location references if useful. Use blue for primary planning actions, neutral structure, green for valid allocations, amber for constrained locations, and red for invalid totals or over-allocation. Use outline icons such as network split, location markers, allocation arrows, and queue release.

Use 24px page padding, 16px to 24px panel padding, 16px spacing between planning areas, and 12px to 16px table cell padding. Responsive behavior: desktop and tablet support planning; mobile should be read-only or omitted. Dashboard style should be minimal; focus on planning table, summaries, and decision support.

## UI-036 Low-Stock Alert Review

Design a desktop-first low-stock alert review screen for an Inventory Management System at 1440px width, with a tablet adaptation at 1024px and a mobile adaptation. Use the standard ERP shell with dark sidebar, white header, and a light neutral app background. The screen should feel like an alert-driven operational review surface.

Use a layout with alert summary strip, filter bar, low-stock alerts table or list, selected alert detail card, and a recommended action panel. On desktop, use a list-detail layout; on mobile, shift to card-based alerts. Use white bordered surfaces with 12px radius and minimal shadow.

Include components: alert summary cards, low-stock alerts table, detail card, filter bar, acknowledgment form, and actions for `Acknowledge`, `Open Replenishment`, `Create Transfer Request`, and `Refresh`. The table should support severity and priority badges, location and category filters, row actions, sticky header, pagination, and empty states. The detail card should include product, location, threshold context, and recommended next steps.

Use Inter typography with 28px page title, 18px section headings, 14px table and form text, 13px helper text, and 12px badges. Use blue for primary actions, green for resolved alerts, amber for low-stock severity, red for urgent risk, and neutral surfaces elsewhere. Use outline icons like low-stock indicator, severity badge, transfer, and requisition or planning.

Use 24px page padding, 16px to 24px card padding, 16px filter spacing, and 12px to 16px table cell padding. Responsive behavior: desktop keeps list-detail, tablet simplifies panel layout, mobile uses stacked alert cards and a filter drawer. Dashboard style should be moderate: summary cards plus alert list, but still practical and dense.

## UI-037 Replenishment Planning

Design a desktop-first replenishment planning screen for an Inventory Management System at 1440px width with a tablet adaptation at 1024px. Use the enterprise shell with dark sidebar, white header, and soft neutral background. The screen should feel like a recommendation-to-action planner.

Use a layout with recommendation cards, recommendations table, network availability comparison, and requisition creation panel. The main interaction should center on converting recommendations into requisitions or transfer actions. Use white bordered cards and panels with 12px radius, subtle shadow, and clean structure.

Include components: recommendation cards, recommendations table, comparison panel, requisition form, status badges, and actions for `Create Requisition`, `Adjust Quantity`, `View Open PO`, and `Open Transfer Option`. The recommendations table should support sticky headers, sorting, badges, row actions, pagination, and loading states. The form should include product, suggested quantity, final quantity, required date, supplier, destination, and justification.

Use Inter typography with 28px page title, 18px section titles, 14px UI text, 13px helper text, and 12px badges. Use blue for primary actions, neutral surfaces, green for accepted recommendations, amber for caution or imbalance, red for shortages or validation issues, and informational blue for open supply references. Use outline icons such as recommendation, replenishment arrow, transfer, and supplier or PO.

Use 24px page padding, 16px to 24px panel padding, and 12px to 16px table cell padding. Responsive behavior: desktop and tablet support planning; mobile should be limited to recommendation lookup. Dashboard style should be light; this is primarily a planning table and action form screen.

## UI-038 Transfer Request

Design a desktop-first transfer request screen for an Inventory Management System at 1440px width with a tablet adaptation at 1024px. Use the dark-sidebar ERP shell with a white header and neutral content background. The screen should feel form-led, logistics-aware, and safe for operational request creation.

Use a page structure with primary request form, side or lower source-impact summary, and a recent requests table. Keep the form dominant on desktop with a supporting capacity preview or impact panel. Use white bordered cards with 12px radius, minimal shadow, and clear visual grouping.

Include components: form sections, capacity preview, recent transfer requests table, status badges, confirmation dialog pattern, and buttons for `Check Capacity`, `Submit Request`, and `Save Draft`. The form should include source location, destination location, justification, SKU, quantity, and optional multi-line request rows. The recent requests table should support sticky header, row actions, badges, pagination, and empty states.

Use Inter typography with 28px page title, 18px section headings, 14px form and table text, 13px helper text, and monospaced styling for request IDs if useful. Use blue primary actions, neutral surfaces, green for successful submission, amber for capacity warnings, red for threshold breach or same-location errors, and info blue for capacity preview states. Use outline icons like transfer arrows, source and destination location, and capacity info.

Use 24px page padding, 16px to 24px card padding, 16px field spacing, and 12px to 16px table cell padding. Responsive behavior: tablet supports the form flow; mobile may support simple single-line requests with simplified capacity preview. Dashboard style should not dominate; this is a transaction form plus recent activity.

## UI-039 Transfer Approval Queue

Design a desktop-first transfer approval queue for an Inventory Management System at 1440px width with a tablet adaptation at 1024px. Use the shared ERP shell with dark sidebar, white header, and a light neutral content background. The screen should feel managerial, queue-driven, and impact-aware.

Use an approval workspace layout with a queue list, selected request detail, source-versus-destination comparison panel, decision form, and status history. Keep the impact comparison visually strong so approvers can judge transfer risk quickly. Use white panels with 12px radius, clean borders, and subtle shadows.

Include components: approval queue table, comparison panel, decision form, status history, badges, and actions for `Approve`, `Reject`, and `View Source Capacity`. The approval table should include aging, request reference, source, destination, quantity, and status with sticky headers, pagination, and row actions. The decision form should include approval or reject choice, approver note, and rejection reason.

Use Inter typography with 28px page heading, 18px panel headings, 14px standard text, 13px helper text, and 12px badges. Use blue for actions, green for approval, red for reject, amber for aging risk, and neutral surfaces elsewhere. Use outline icons such as approval check, reject, capacity info, and aging clock.

Use 24px page padding, 16px to 24px panel padding, and 12px to 16px table cell padding. Responsive behavior: tablet and simplified mobile review are possible, but desktop should deliver the richest source-versus-destination comparison. Dashboard style should be minimal; this is an approval workbench.

## UI-040 Transfer Execution and In-Transit Tracking

Design a desktop-first transfer execution and in-transit tracking screen for an Inventory Management System at 1440px width with a tablet adaptation at 1024px. Use the standard enterprise shell with dark sidebar, white header, and neutral content background. The screen should feel like a logistics operations console.

Use a three-zone layout with dispatch queue, in-transit tracking section, and destination receipt confirmation section. Keep state transitions visible and easy to follow. Use white bordered panels with 12px radius, low shadow, and compact operational density.

Include components: transfer queue table, in-transit transfers table, receipt confirmation form, status timeline, location context badge, and buttons for `Dispatch`, `Confirm Receipt`, and `Cancel Transfer`. The queue and transit tables should support sticky headers, badges, row actions, pagination, and inline status chips. The forms should include dispatch quantity, lot or batch details, received quantity, variance note, and cancellation reason when needed.

Use Inter typography with strong page heading, 14px standard UI text, 13px helper text, and monospaced style for transfer references if useful. Use blue for primary actions, neutral surfaces, green for successful dispatch or receipt, amber for in-transit or variance warnings, and red for cancellation or major errors. Use outline icons like dispatch arrow, truck in transit, receive inbox, and variance warning.

Use 24px page padding, 16px to 24px panel padding, 16px between zones, and 12px to 16px table cell padding. Responsive behavior: desktop and tablet must support operations; mobile may support simplified receipt confirmation only. Dashboard style should be low; focus on workbench flow and state tracking.

## UI-041 Network Rebalancing Analysis

Design a desktop-first network rebalancing analysis screen for an Inventory Management System at 1440px width with a tablet adaptation at 1024px. Use the ERP shell with dark sidebar, white header, and light neutral background. The screen should feel analytical, logistics-smart, and recommendation-driven.

Use an analytics and planning layout with filter bar, imbalance summary cards, recommendation cards, recommendations table, impact preview panel, and export actions. Keep the layout clean and controlled, with data and action clarity over visual complexity. Use white bordered cards with 12px radius and minimal shadows.

Include components: summary cards, recommendation cards, recommendations table, impact comparison panel, export action group, and buttons for `Generate Recommendation`, `Create Transfer`, and `Export`. The table should support location pair, product, quantity, urgency, and action state columns with sticky headers, badges, sorting, and pagination. The impact panel should clearly describe the tradeoff between source and destination stock.

Use Inter typography with 28px page title, 18px section titles, 14px standard text, and 13px metadata. Use blue for interactions, neutral surfaces, green for favorable rebalance outcomes, amber for imbalance warnings, red for critical shortages, and informational blue for recommendations. Use outline icons like network, rebalance arrows, compare or impact, and export.

Use 24px page padding, 16px to 24px panel padding, and 12px to 16px table cell padding. Responsive behavior: desktop-first planning surface, tablet summary view acceptable, mobile read-only only. Dashboard style should be moderate and analytical with strong emphasis on recommendation tables.

## UI-042 Return Authorization Management

Design a desktop-first return authorization management screen for an Inventory Management System at 1440px width, with a tablet adaptation at 1024px and a mobile adaptation. Use the standard enterprise shell with dark sidebar, white header, and a neutral content background. The screen should feel customer-service-friendly, controlled, and eligibility-focused.

Use a layout with order search at the top, eligible return lines in the central area, and an authorization detail panel beside or below. Keep the page easy to scan and not overly dense. Use white bordered surfaces with 12px radius and minimal shadow.

Include components: search bar, eligible return lines table, authorization detail section, status timeline, and buttons for `Validate Eligibility`, `Issue Authorization`, and `Cancel Authorization`. The search form should support order or customer reference fields. The eligible lines table should show item, shipped quantity, return-eligible quantity, and selection state, with sticky header, badges, pagination, and empty states. The detail form should include selected item quantity, reason, authorization notes, and cancellation reason.

Use Inter typography with 28px title, 18px section titles, 14px UI text, 13px helper text, and 12px status labels. Use blue for primary actions, neutral structure, green for eligible and authorized, amber for partial or cautionary states, and red for invalid policy or cancellation states. Use outline icons such as return arrow, order lookup, and eligibility check.

Use 24px page padding, 16px to 24px panel padding, and 12px to 16px table cell padding. Responsive behavior: tablet and mobile-friendly support should use simpler line selection and stacked sections. Dashboard style should be absent; this is a search-and-authorize workflow.

## UI-043 Return Inspection and Disposition

Design a desktop-first return inspection and disposition screen for an Inventory Management System at 1440px width with a tablet adaptation at 1024px. Use the shared ERP shell with dark sidebar, white header, and a light neutral background. The screen should feel like a warehouse return processing workbench with clear steps.

Use a queue-plus-step-workflow layout with pending returns queue, step progress indicator, line-item editor, condition selectors, disposition controls, and status timeline. Keep the current step obvious and support fast movement from receipt to inspection to disposition. Use white bordered cards and panels with 12px radius and minimal shadow.

Include components: pending returns table, step progress indicator, line-item editor, condition controls, disposition panel, status timeline, and actions for `Receive Return`, `Record Inspection`, and `Confirm Disposition`. The form should include receiving location, received quantities, condition, disposition action, restock location, and write-off reference or evidence. Tables should support sticky headers, compact rows, badges, and loading states.

Use Inter typography with 28px title, 18px section titles, 14px standard text, 13px helper text, and monospaced references for return authorization IDs if useful. Use blue for workflow actions, neutral surfaces, green for successful step completion, amber for inspection attention, red for write-off or blocking issues, and purple for quarantine routes. Use outline icons like return, inspection check, quarantine, write-off, and restock arrow.

Use 24px page padding, 16px to 24px panel padding, 16px between step regions, and 12px to 16px table cell padding. Responsive behavior: tablet support is valuable; mobile should support simplified receipt and inspection only. Dashboard style should be minimal and process-focused.

## UI-044 Operational Reports and Analytics

Design a desktop-first operational reports and analytics screen for an Inventory Management System at 1440px width with a tablet adaptation at 1024px. Use the dark-sidebar enterprise shell with white header and light app background. The screen should feel like a report viewer for operations, not a marketing dashboard.

Use a layout with report selector and filters at the top, report output region in the center, and drill-down or export area to the side or bottom. Support both table and simple chart outputs while keeping the interface practical and dense. Use white bordered cards and panels with 12px radius and minimal shadow.

Include components: report selector, filter bar, report viewer, export action group, drill-down links, report output table, and optional chart zones. Tables should support sticky headers, sorting, pagination, empty states, skeleton rows, and row actions. Forms should support report type, location, category, date range, status, KPI code, and context-sensitive filters. Include `Run Report`, `Export`, and `Open Detail` buttons.

Use Inter typography with 28px page title, 18px section titles, 14px UI text, 13px metadata, and 12px table headers or badges. Use blue for actions, neutral structure, green for successful run or export, amber for partial warning states, and restrained semantic colors in charts and badges. Use outline icons like report document, filter, chart, and export.

Use 24px page padding, 16px to 24px card padding, and 12px to 16px table cell padding. Responsive behavior: desktop-first, tablet supports summary and simplified tables, mobile should be summary-only and read-only. Dashboard style should be limited and report-centric.

## UI-045 Inventory Valuation Reconciliation

Design a desktop-first inventory valuation reconciliation screen for an Inventory Management System at 1440px width with a tablet adaptation at 1024px. Use the enterprise shell with dark sidebar, white header, and neutral content background. The screen should feel finance-oriented, serious, and comparison-heavy.

Use a layout with period selector and summary cards at the top, side-by-side valuation comparison blocks, notes panel, and supporting variance tables. Make the financial comparison central and visually structured. Use white bordered cards and panels with 12px radius, subtle shadow, and compact but readable density.

Include components: summary cards, comparison panel, notes form, report viewer, export actions, status badges, valuation comparison table, and adjustment or variance detail table. Include actions for `Load Period`, `Add Note`, `Finalize Reconciliation`, and `Export`. Tables should support sticky headers, numeric alignment, badges, pagination, and skeleton loading states. The notes area should look formal and easy to review.

Use Inter typography with 28px page title, 18px section titles, 14px standard UI text, 13px metadata, and monospaced treatment for valuation references or ledger IDs where helpful. Use blue for interactions, neutral structure, green for reconciled or finalized states, amber for material variance warnings, red for blocking discrepancies, and muted purple only if needed for governance emphasis. Use outline icons such as finance ledger, compare, variance warning, and finalize check.

Use 24px page padding, 16px to 24px card padding, and 12px to 16px table cell padding. Responsive behavior: desktop-first finance review, tablet summary only, mobile read-only or unsupported. Dashboard style should be restrained and financial, with comparison panels and data tables dominating.

## UI-046 Promotional Stock Readiness

Design a desktop-first promotional stock readiness screen for an Inventory Management System at 1440px width with a tablet adaptation at 1024px. Use the standard ERP shell with dark sidebar, white header, and a light neutral app background. The screen should feel campaign-focused, analytical, and inventory-aware.

Use a layout with campaign selector, readiness summary cards, campaign product readiness grid, and gap or escalation section. The readiness table should be central and easy to scan for risk. Use white bordered cards and panels with 12px radius, clean structure, and low shadow.

Include components: campaign selector, summary cards, readiness table, gap panel, escalation actions, status badges, and buttons for `Check Readiness`, `Confirm Readiness`, `Escalate Gap`, and `Release Allocation`. The table should show allocated quantity, target quantity, ATP, inbound support, and readiness state with sticky headers, badges, sorting, and pagination. The escalation panel should be visible but compact.

Use Inter typography with 28px page title, 18px section headings, 14px standard text, 13px helper and metadata text, and 12px badges. Use blue for actions, neutral surfaces, green for ready, amber for at-risk, red for launch risk, and informational blue for support or inbound indicators. Use outline icons like campaign megaphone, readiness check, at-risk warning, and release icon.

Use 24px page padding, 16px to 24px panel padding, and 12px to 16px table cell padding. Responsive behavior: desktop and tablet support the screen; mobile should be summary-only. Dashboard style should be moderate: summary cards plus readiness grid, with strong operational clarity.

## UI-047 Audit and Control Review Workspace

Design a desktop-first audit and control review workspace for an Inventory Management System at 1440px width with a tablet adaptation at 1024px. Use the enterprise shell with dark sidebar, white header, and a neutral content background. The screen should feel investigative, rigorous, and evidence-centric.

Use a layout with scope setup area, sample or review workspace, reviewed-transactions table, findings panel, evidence panel, and export actions. The interface should balance setup, investigation, and documentation in one coherent audit workspace. Use white bordered panels with 12px radius, subtle shadow, and compact data density.

Include components: scope form, reviewed-transactions table, findings table, evidence panel, export action group, status strip, and actions for `Start Review`, `Record Finding`, `Export Evidence`, and `Complete Review`. Tables should support sticky headers, sorting, row actions, pagination, and skeleton loading states. The forms should include scope dates, location, transaction type, reviewer, finding type, severity, note, and evidence reference.

Use Inter typography with 28px page title, 18px section titles, 14px standard text, 13px metadata, and 12px severity badges. Use blue for actions, neutral structure, purple for governance or audit emphasis, amber for cautionary findings, red for severe findings, and green for completed review states. Use outline icons such as audit search, evidence attachment, finding warning, and export.

Use 24px page padding, 16px to 24px panel padding, and 12px to 16px table cell padding. Responsive behavior: desktop-first because of data density, tablet summary review acceptable, mobile unsupported or read-only. Dashboard style should be minimal; this is a report-review and evidence-capture workspace.

## UI-048 Audit Trail Query

Design a desktop-first audit trail query screen for an Inventory Management System at 1440px width with a tablet adaptation at 1024px. Use the standard dark-sidebar ERP shell with white header and a light neutral content background. The screen should feel like a forensic search and record inspection tool.

Use a layout with query filter panel at the top or left, results table in the main region, and selected record before-and-after detail panel. Keep the table dominant and the detail pane structured for comparison. Use white panels with 12px radius, light borders, and subtle shadows.

Include components: query form, results table, audit record viewer, export actions, metadata footer, and buttons for `Run Query`, `Open Record`, and `Export Results`. The query form should include entity type, entity ID, user, date range, and action type. The results table should support sticky headers, sorting, pagination, badges, and skeleton loading rows. The detail panel should clearly separate before and after values with explicit headings.

Use Inter typography with 28px page title, 18px panel headings, 14px standard text, 13px helper or metadata text, and monospaced styling for record IDs, entity IDs, and audit references. Use blue for interactions, neutral structure, purple for audit emphasis, amber for cautionary changes if needed, and restrained semantic color use overall. Use outline icons like audit log, compare, export, and filter.

Use 24px page padding, 16px to 24px panel padding, and 12px to 16px table cell padding. Responsive behavior: desktop-first investigative interface, tablet summary review acceptable, mobile read-only or unsupported. Dashboard style should be absent; this is a search-and-inspect audit tool.

## UI-049 User Account Management

Design a desktop-first user account management screen for an Inventory Management System at 1440px width, with a tablet adaptation at 1024px and a simplified mobile adaptation. Use the standard ERP shell with dark sidebar, white header, and soft neutral background. The screen should feel administrative, secure, and role-aware.

Use a layout with user directory list, account detail panel, role assignment section, status badges, and audit metadata. Keep the desktop arrangement in a list-detail format with enough room for a role assignment table. Use white bordered panels with 12px radius and minimal shadow.

Include components: users table, detail panel, role assignment widget, status badges, confirmation dialogs, metadata strip, and actions for `Create User`, `Save`, `Suspend`, `Deactivate`, and `Sync Users`. The users table should include user ID, display name, email, active state, and row actions with sticky header, pagination, and badges. The forms should include user ID, email, display name, initial roles, role code, location codes, effective dates, suspension reason, and deactivation reason.

Use Inter typography with 28px page title, 18px section headings, 14px standard text, 13px metadata, and 12px badges. Use blue for actions, neutral structure, green for active, amber for suspended or caution states, red for deactivated or blocking issues, and purple sparingly for governance-sensitive access indicators. Use outline icons like user, role shield, pause or suspend, warning, and sync.

Use 24px page padding, 16px to 24px panel padding, and 12px to 16px table cell padding. Responsive behavior: desktop and tablet support full management; mobile should support lookup and simple status review only. Dashboard style should be minimal; this is an admin list-detail screen with forms and tables.

## UI-050 Role and Access Control Administration

Design a desktop-first role and access control administration screen for an Inventory Management System at 1440px width with a tablet adaptation at 1024px. Use the enterprise shell with dark sidebar, white header, and neutral content background. The screen should feel formal, matrix-driven, and suitable for secure administration.

Use a layout with role list on the left, permission matrix in the main region, location scope rules section, conflict warning area, and save or reset action bar. The permission matrix should be the primary visual element and must feel organized, dense, and readable. Use white bordered panels with 12px radius, crisp borders, and minimal shadow.

Include components: roles table, permissions matrix table, scope selector, conflict warning panel, validation banner, and buttons for `Edit Role`, `Save Permissions`, `Validate SoD`, and `Reset Changes`. The roles table should support selection, sticky header, badges, and pagination. The permissions matrix should include explicit row and column headers, checkbox or toggle cells, grouped permission sections, and highlighted conflict states.

Use Inter typography with 28px page title, 18px section titles, 14px standard text, 13px helper or metadata text, and 12px badge labels. Use blue for selected states and actions, neutral structure and surfaces, purple for governance or access-control accents, amber for warnings, and red for conflicts or blocked combinations. Use outline icons such as shield, matrix grid, conflict warning, and validation check.

Use 24px page padding, 16px to 24px panel padding, and 12px to 16px table cell padding. Responsive behavior: desktop-only or desktop-first because of matrix density, tablet read-only at most, mobile not recommended. Dashboard style should be absent; the emphasis should be on a clear permission matrix, structured forms, and accessible administrative control.
