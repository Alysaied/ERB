# Inventory Management System Form Specifications and Validation

## Purpose

This document defines the UX form specification for every major form in the Inventory Management System. It aligns user-facing validation, inline behavior, success behavior, and error behavior with the approved API validation and error specifications in:

- `SRS/API_Design/Request-DTO-Validation-Spec.md`
- `SRS/API_Design/Error-Response-Specification.md`

## Scope Notes

- This document focuses on application forms, not read-only dashboards or query-only screens with no editable input.
- Where multiple screens use the same underlying form pattern, a single shared form specification is used.
- Validation messages are written for users but remain aligned to backend rules such as `VAL_*`, `BIZ_*`, `CONF_*`, and supporting `VR-xxx` / `BR-xxx` rules.
- Input types are expressed in UX terms such as text field, dropdown, date picker, numeric field, file upload, and checkbox.

---

## Shared Validation Behavior

These rules apply to all forms unless a form-specific rule overrides them.

### Inline Validation Behavior

- Validate required fields on blur and on submit.
- Validate format-sensitive fields on blur once the user leaves the field.
- Validate cross-field rules when any dependent field changes.
- Do not show an error before the user has interacted with a field, except after submit.
- Replace blocking field errors with success/neutral state immediately when corrected.
- For numeric quantity and amount fields, enforce allowed precision in the input where practical and confirm again on blur.
- For code fields such as SKU, Location Code, Supplier Code, and Reason Code, preserve uppercase formatting where the API expects uppercase patterns.

### Success Behavior

- After successful submit, show a visible success banner with a concise outcome statement.
- Keep the user on the record detail screen for create/update forms unless the workflow naturally returns to a queue.
- Refresh related summary panels, tables, and status badges immediately after success.
- For multi-step or queued work, mark the completed item as processed and move the user to the next logical task.

### Error Behavior

- For `400 VAL_*` errors, map field-level errors inline and show a form-level summary banner.
- For `409 CONF_*` errors, keep user-entered values intact and explain the conflicting record or state.
- For `422 BIZ_*` errors, show a form-level business-rule message and highlight any affected fields or sections.
- For `401 AUTH_*` errors, redirect to re-authentication or session recovery flow.
- For `403 AUTHZ_*` errors, disable retry-only behavior and explain that the user lacks access.
- For `500/503 SYS_*` errors, preserve draft state when possible and offer retry behavior.

### Standard Form-Level Error Summary Pattern

- Title: `There is a problem with this form.`
- Body: `Review the highlighted fields and try again.`
- If the API returns `traceId`, show it in support-facing error details but not as primary user content.

---

## Shared Field Patterns

### Shared Pattern A: Product SKU
- **Input type:** Single-line text field
- **Required fields:** Required when the form creates, updates, or references a specific product
- **Validation messages:**
  - `SKU is required.`
  - `SKU must use uppercase letters, numbers, hyphens, or underscores only.`
  - `SKU cannot be longer than 50 characters.`
  - `This product could not be found.` (`NF_PRODUCT_NOT_FOUND`)
- **Inline validation behavior:** Convert to uppercase on blur where appropriate; validate pattern `^[A-Z0-9][A-Z0-9_-]*$`.

### Shared Pattern B: Location Code
- **Input type:** Searchable dropdown or code text field depending on context
- **Required fields:** Required when location-scoped activity occurs
- **Validation messages:**
  - `Location is required.`
  - `Select a valid location.`
  - `You are not authorized for this location.` (`AUTHZ_LOCATION_SCOPE_DENIED`)
- **Inline validation behavior:** Validate existence and scope after selection when API lookup is available.

### Shared Pattern C: Quantity
- **Input type:** Numeric decimal field with unit label
- **Required fields:** Required when stock, order, receipt, or transfer quantity is submitted
- **Validation messages:**
  - `Quantity is required.`
  - `Quantity must be greater than 0.` for positive quantity contexts
  - `Quantity cannot be negative.`
  - `Quantity has too many decimal places.`
  - `Quantity exceeds the allowed available amount.` (`BIZ_INSUFFICIENT_ATP`, `BIZ_SOURCE_MINIMUM_PROTECTED`, or context equivalent)
- **Inline validation behavior:** Validate numeric format immediately; validate business ceilings after related context fields are complete.

### Shared Pattern D: Reason Code
- **Input type:** Dropdown
- **Required fields:** Required for adjustments, write-offs, discrepancies, holds, and many exception flows
- **Validation messages:**
  - `Reason code is required.`
  - `Select a valid active reason code.`
  - `This reason code cannot be used for this transaction type.`
- **Inline validation behavior:** Filter reason-code options by transaction type where possible.

### Shared Pattern E: Date Range
- **Input type:** Start date + end date date pickers
- **Required fields:** Required for reporting and audit forms where specified
- **Validation messages:**
  - `Start date is required.`
  - `End date is required.`
  - `Start date must be on or before end date.` (`VAL_INVALID_DATE_RANGE`)
  - `The selected date range is too large for this request.`
- **Inline validation behavior:** Revalidate both fields whenever either date changes.

---

## Form Specifications

## F-001 Sign In Form
- **Related screens:** `UI-001`
- **Aligned APIs:** Session/auth integration, `API-173`, `API-174`

### Fields
| Field | Input type | Required |
|---|---|---|
| Username / Email | Text field | Yes |
| Password | Password field | Yes |
| Remember Session | Checkbox | No |

### Validation messages
- `Username or email is required.`
- `Password is required.`
- `Your session could not be started. Check your credentials and try again.` (`AUTH_INVALID_TOKEN` equivalent UX messaging)
- `Your account is suspended.` (`AUTH_ACCOUNT_SUSPENDED`)
- `Your account is deactivated.` (`AUTH_ACCOUNT_DEACTIVATED`)

### Inline validation behavior
- Required validation on blur and submit.
- Password field does not show content-specific validation, only presence.

### Success behavior
- Redirect to `Operational Home Dashboard` or role-specific landing page.

### Error behavior
- Authentication failures show a form-level error banner.
- Preserve entered username/email after failure; clear password field.

---

## F-002 Product Form
- **Related screens:** `UI-005`
- **Aligned APIs:** `API-001`, `API-004`, `API-005`

### Fields
| Field | Input type | Required |
|---|---|---|
| SKU | Text field | Yes on create |
| Name | Text field | Yes |
| Description | Text area | No |
| Unit of Measure | Dropdown | Yes |
| Category Code | Searchable dropdown | No |
| Barcode | Text field | No |
| Is Traceable | Toggle | No |
| Rotation Policy | Dropdown | Conditional |
| Shelf Life Managed | Toggle | No |
| MRSL Threshold Days | Numeric field | Conditional |
| Lifecycle Status | Dropdown | Yes on edit/status action |
| Status Change Reason | Text area | No |
| Effective Date | Date picker | No |

### Validation messages
- `SKU is required.`
- `SKU must use uppercase letters, numbers, hyphens, or underscores only.`
- `SKU cannot be longer than 50 characters.`
- `A product with this SKU already exists.` (`CONF_DUPLICATE_SKU`)
- `Name is required.`
- `Name cannot be longer than 200 characters.`
- `Unit of measure is required.`
- `Barcode cannot be longer than 50 characters.`
- `A product with this barcode already exists.` (`CONF_DUPLICATE_BARCODE`)
- `Rotation policy is required when the product is traceable.`
- `MRSL threshold days is required when shelf life management is enabled.`
- `MRSL threshold days must be at least 1.`
- `Select a valid lifecycle status.`
- `This lifecycle change is not allowed for the current product state.`

### Inline validation behavior
- SKU: uppercase normalization, pattern validation on blur.
- Conditional fields appear and become required immediately when toggles are enabled.
- Duplicate SKU/barcode checks can run after blur if asynchronous validation is available.

### Success behavior
- Show success banner: `Product saved successfully.`
- Remain on `Product Detail`.

### Error behavior
- `400` field errors map inline.
- `409` duplicate conflicts show inline on SKU or barcode and in banner.
- `422` lifecycle/business-rule failures show form-level message and keep values intact.

---

## F-003 Product Duplicate Resolution Form
- **Related screens:** `UI-005`
- **Aligned APIs:** `API-009`

### Fields
| Field | Input type | Required |
|---|---|---|
| Resolution Action | Radio group | Yes |
| Source SKU | Read-only/select field | Yes |
| Target SKU | Searchable dropdown | Conditional |
| Merge Authorization Reference | Text field | Conditional |
| Notes | Text area | No |

### Validation messages
- `Resolution action is required.`
- `Target product is required when merging duplicates.`
- `Merge authorization reference is required when inventory exists on both products.`
- `Select a valid target product.`

### Inline validation behavior
- Conditional fields appear when `MERGE` is selected.
- Revalidate target and authorization reference immediately when resolution action changes.

### Success behavior
- Show success banner and refresh the related product records.

### Error behavior
- Keep all selections intact.
- Show conflict/business-rule guidance if merge is blocked.

---

## F-004 Bulk Product Import Form
- **Related screens:** `UI-006`
- **Aligned APIs:** `API-010`

### Fields
| Field | Input type | Required |
|---|---|---|
| Import Mode | Dropdown | Yes |
| Source Reference | Text field | No |
| Import File / Product Batch | File upload | Yes |

### Validation messages
- `Import mode is required.`
- `Import file is required.`
- `The selected file format is not supported.`
- `The batch cannot be empty.`
- `This import contains duplicate SKUs in the same batch.`
- `Some rows contain blocking validation errors.`

### Inline validation behavior
- Validate file presence immediately after selection.
- Validate file type and size before upload.
- Row-level validation is shown in the results table after validation/upload.

### Success behavior
- `VALIDATE_ONLY`: show validation summary.
- `UPSERT` / `CREATE_ONLY`: show import completion summary with created/updated counts.

### Error behavior
- Entire-request validation issues show form-level error.
- Per-row errors stay in the results grid with row-level messages.

---

## F-005 Location Form
- **Related screens:** `UI-007`
- **Aligned APIs:** `API-011`, `API-013`, `API-014`, `API-017`, `API-018`, `API-019`

### Fields
| Field | Input type | Required |
|---|---|---|
| Location Code | Text field | Yes on create |
| Name | Text field | Yes |
| Location Type | Dropdown | Yes |
| Operational Status | Dropdown | Yes |
| Parent Location Code | Searchable dropdown | No |
| Planned Go-Live Date | Date picker | No |
| Address Fields | Text fields | No |
| Activation Date | Date picker | No |
| Opening Balance Approval Reference | Text field | Conditional |
| Deactivation Reason | Text area | Conditional |
| Disposition Plan Reference | Text field | Conditional |
| Closure Waiver Reference | Text field | Conditional |

### Validation messages
- `Location code is required.`
- `Location code must use uppercase letters, numbers, hyphens, or underscores only.`
- `A location with this code already exists.` (`CONF_DUPLICATE_LOCATION`)
- `Name is required.`
- `Location type is required.`
- `Operational status is required.`
- `A location cannot be its own parent.`
- `Select a valid parent location.`
- `Opening balance approval reference is required before activation.`
- `A reason is required when deactivating a location.`
- `A disposition plan or closure waiver is required when stock remains at this location.`

### Inline validation behavior
- Validate hierarchy rules when parent changes.
- Activation-specific fields validate only when the user initiates activation.
- Closure fields validate only when the user initiates closure.

### Success behavior
- Save/update returns the user to `Location Detail` with updated status.

### Error behavior
- Hierarchy conflicts show inline on parent field and as banner.
- Business-rule closure and activation failures show form-level guidance.

---

## F-006 Storage Position Form
- **Related screens:** `UI-007`
- **Aligned APIs:** `API-015`

### Fields
| Field | Input type | Required |
|---|---|---|
| Location Code | Context field | Yes |
| Position Code | Text field | Yes |
| Zone | Text field | No |
| Aisle | Text field | No |
| Bin | Text field | No |
| Position Type | Dropdown | No |
| Active | Toggle | No |

### Validation messages
- `Position code is required.`
- `Position code must be unique within this location.`
- `Select a valid location.`

### Inline validation behavior
- Validate uniqueness after blur if supported.

### Success behavior
- Add/update row in storage positions table and clear or close form.

### Error behavior
- Preserve entered values; highlight duplicate or invalid position issues.

---

## F-007 Stock Policy Form
- **Related screens:** `UI-008`
- **Aligned APIs:** `API-038`, `API-040`

### Fields
| Field | Input type | Required |
|---|---|---|
| Location Code | Searchable dropdown | Yes |
| SKU | Searchable dropdown / text field | Yes |
| Reorder Level | Numeric field | Yes |
| Minimum Threshold | Numeric field | Yes |
| Safety Stock | Numeric field | Yes |
| Maximum Threshold | Numeric field | No |
| Effective From | Date picker | Yes |

### Validation messages
- `Location is required.`
- `Product is required.`
- `Reorder level is required.`
- `Minimum threshold is required.`
- `Safety stock is required.`
- `Values cannot be negative.`
- `Maximum threshold must be greater than or equal to reorder level.`
- `Minimum threshold must be less than or equal to reorder level.`
- `Effective from date is required.`

### Inline validation behavior
- Revalidate all threshold relationships whenever one threshold field changes.
- Numeric inputs enforce decimal/precision rules immediately.

### Success behavior
- Show success banner and refresh the policy summary view.

### Error behavior
- Field-level threshold errors shown inline.
- If location or product is inactive, show form-level business-rule message.

---

## F-008 ABC Classification Form
- **Related screens:** `UI-009`
- **Aligned APIs:** `API-006`

### Fields
| Field | Input type | Required |
|---|---|---|
| SKU | Context/select field | Yes |
| ABC Class | Dropdown / segmented control | Yes |
| Classification Basis | Dropdown | No |
| Effective Date | Date picker | No |

### Validation messages
- `Product is required.`
- `ABC class is required.`
- `Select A, B, or C.`

### Inline validation behavior
- Immediate validation when class is selected.

### Success behavior
- Update classification in list/table and show success banner.

### Error behavior
- Preserve selected class and surface any product-state conflict.

---

## F-009 Governance Policy Form
- **Related screens:** `UI-010`
- **Aligned APIs:** `API-026`, `API-027`, `API-028`

### Fields
| Field | Input type | Required |
|---|---|---|
| Policy Name | Text field | Yes |
| Description | Text area | No |
| Effective From | Date-time picker | Yes |
| Effective To | Date-time picker | No |
| Transaction Type | Dropdown | Conditional |
| Quantity Threshold | Numeric field | Conditional |
| Monetary Threshold | Numeric amount field | Conditional |
| Currency Code | Dropdown | Conditional |
| Quantity Tolerance Percent | Numeric field | Conditional |
| Absolute Tolerance | Numeric field | Conditional |
| Parameter Key/Value Pairs | Repeating fields | Conditional |

### Validation messages
- `Policy name is required.`
- `Effective from date is required.`
- `Effective to date must be after effective from date.`
- `At least one policy parameter is required.`
- `Transaction type is required for threshold updates.`
- `At least one threshold value is required.`
- `Thresholds cannot be negative.`
- `Tolerance percent must be between 0 and 100.`
- `A currency code is required when a monetary threshold is entered.`
- `This policy overlaps an existing effective policy version.`

### Inline validation behavior
- Cross-field validation runs when effective dates or threshold fields change.
- Monetary threshold and currency validate as a pair.

### Success behavior
- Show `Policy published successfully.` or equivalent outcome based on action.

### Error behavior
- Overlap and governance-rule issues surface as form-level errors with related fields highlighted.

---

## F-010 Reason Code Form
- **Related screens:** `UI-010`
- **Aligned APIs:** `API-022`, `API-024`

### Fields
| Field | Input type | Required |
|---|---|---|
| Code | Text field | Yes |
| Description | Text field | Yes |
| Transaction Types | Multi-select | Yes |
| Active | Toggle | No |
| Retirement Reason | Text area | Conditional |
| Effective Date | Date picker | No |

### Validation messages
- `Code is required.`
- `Code must use uppercase letters, numbers, and underscores only.`
- `Code cannot be longer than 20 characters.`
- `Description is required.`
- `Select at least one transaction type.`
- `Retirement reason is required when retiring a reason code.`

### Inline validation behavior
- Validate code format on blur.
- Retirement fields only validate when retire action is selected.

### Success behavior
- Refresh reason-code list and show success feedback.

### Error behavior
- Keep form open with code-specific errors preserved.

---

## F-011 Supplier Form
- **Related screens:** `UI-011`
- **Aligned APIs:** `API-049`, `API-052`, `API-053`

### Fields
| Field | Input type | Required |
|---|---|---|
| Supplier Code | Text field | Yes on create |
| Name | Text field | Yes |
| Email | Email field | No |
| Phone | Text field | No |
| Payment Terms Days | Numeric field | Yes |
| Lead Time | Numeric field | No |
| Currency Code | Dropdown | No |
| Is Consignment | Checkbox / toggle | No |
| Active Status | Toggle | No |
| Deactivation Reason | Text area | Conditional |

### Validation messages
- `Supplier code is required.`
- `A supplier with this code already exists.`
- `Name is required.`
- `Enter a valid email address.`
- `Payment terms days is required.`
- `Payment terms days cannot be negative.`
- `A reason is required when deactivating a supplier.`

### Inline validation behavior
- Validate code uniqueness and email format on blur when possible.

### Success behavior
- Stay on supplier detail and refresh supplier summary.

### Error behavior
- Duplicate/conflict errors stay attached to supplier code.

---

## F-012 Purchase Requisition Form
- **Related screens:** `UI-013`, `UI-037`
- **Aligned APIs:** `API-054`, `API-056`, `API-057`, `API-058`

### Fields
| Field | Input type | Required |
|---|---|---|
| Receiving Location Code | Searchable dropdown | Yes |
| Justification | Text area | Yes |
| Requisition Lines | Repeating line-item editor | Yes |
| Line SKU | Searchable dropdown / text field | Yes |
| Line Quantity | Numeric field | Yes |
| Required Date | Date picker | Yes per workflow if used |
| Supplier Code | Searchable dropdown | Conditional on conversion |
| Expected Delivery Date | Date picker | Conditional on conversion |
| Network Transfer Declined | Checkbox | No |
| Network Transfer Decline Reason | Text area | Conditional |
| Rejection Reason | Text area | Conditional |

### Validation messages
- `Receiving location is required.`
- `Justification is required.`
- `Add at least one requisition line.`
- `Each line must include a product and quantity.`
- `Quantity must be greater than 0.`
- `Discontinued products cannot be requisitioned.` (`BIZ_PRODUCT_DISCONTINUED`)
- `Provide a reason if network transfer was declined.`
- `Supplier is required to convert this requisition to a purchase order.`
- `Expected delivery date is required to convert this requisition.`
- `Rejection reason is required when rejecting a requisition.`

### Inline validation behavior
- Line-item validation runs per row and at whole-form level.
- Conditional conversion and approval fields appear only in those actions.

### Success behavior
- On create: show requisition detail.
- On approve/reject: update requisition status in place.
- On convert: navigate to resulting `Purchase Order Detail`.

### Error behavior
- Preserve all line items and entered notes.
- Surface network-transfer and discontinued-product rules as form-level business messages.

---

## F-013 Purchase Order Form
- **Related screens:** `UI-012`
- **Aligned APIs:** `API-059`, `API-062`, `API-063`, `API-064`

### Fields
| Field | Input type | Required |
|---|---|---|
| Supplier Code | Searchable dropdown | Yes |
| Receiving Location Code | Searchable dropdown | Yes |
| Expected Delivery Date | Date picker | Yes |
| PO Lines | Repeating line-item editor | Yes |
| Line SKU | Searchable dropdown / text field | Yes |
| Ordered Quantity | Numeric field | Yes |
| Amendment Reason | Text area | Conditional |
| Cancellation Reason | Text area | Conditional |
| Shipment / Delivery Update Quantity | Numeric field | Conditional |

### Validation messages
- `Supplier is required.`
- `Receiving location is required.`
- `Expected delivery date is required.`
- `Add at least one purchase order line.`
- `Each line must include a valid product and quantity.`
- `Quantity must be greater than 0.`
- `Discontinued products cannot be ordered.` (`BIZ_PRODUCT_DISCONTINUED`)
- `Supplier must be active.`
- `Amendment reason is required when changing a purchase order.`
- `Cancellation reason is required when canceling a purchase order.`
- `Amended quantity cannot be less than quantity already received.`

### Inline validation behavior
- Validate lines per row.
- Amendment/cancellation reason fields only validate during those actions.

### Success behavior
- Show PO detail with updated status and line summary.

### Error behavior
- State conflicts such as already-amended/canceled PO show form-level conflict banner.
- Preserve user changes for retry when possible.

---

## F-014 Inbound Delivery Planning Form
- **Related screens:** `UI-014`
- **Aligned APIs:** `API-064`

### Fields
| Field | Input type | Required |
|---|---|---|
| Purchase Order ID | Context field | Yes |
| Expected Arrival Date | Date picker | Yes |
| Carrier | Text field | No |
| Delivery Location | Context/select field | No |
| Expected Quantities by Line | Numeric fields | Conditional |

### Validation messages
- `Expected arrival date is required.`
- `Expected quantity cannot exceed the remaining open quantity.`

### Inline validation behavior
- Revalidate line quantities against outstanding PO quantity whenever edited.

### Success behavior
- Delivery schedule updates on the screen and in inbound calendar context.

### Error behavior
- Invalid line override quantities stay highlighted inline.

---

## F-015 Goods Receipt Creation / Verification Form
- **Related screens:** `UI-015`
- **Aligned APIs:** `API-066`, `API-069`

### Fields
| Field | Input type | Required |
|---|---|---|
| Receiving Location Code | Searchable dropdown | Yes |
| Purchase Order ID | Search/select field | Conditional |
| Supplier Code | Search/select field | Conditional |
| Receipt Lines | Repeating line-item editor | Yes on verify |
| Line ID | Hidden/context | Yes |
| SKU | Read-only/context | Yes |
| Accepted Quantity | Numeric field | Yes |
| Rejected Quantity | Numeric field | No |
| Condition | Dropdown | No |
| Lot Number | Text field | Conditional |
| Expiration Date | Date picker | Conditional |
| Manufacture Date | Date picker | No |

### Validation messages
- `Receiving location is required.`
- `A valid purchase order is required for supplier receipts.` (`BIZ_PO_REQUIRED_FOR_RECEIPT`)
- `Add at least one verified line.`
- `Accepted quantity is required.`
- `Accepted quantity cannot be negative.`
- `Accepted and rejected quantities cannot exceed the physically verified quantity.`
- `Lot number is required for traceable products.` (`BIZ_LOT_REQUIRED`)
- `Expiration date is required for shelf-life products.`
- `Remaining shelf life does not meet the minimum threshold.` (`BIZ_MRSL_NON_COMPLIANT`)

### Inline validation behavior
- Line-level quantities validate immediately on blur.
- Traceability and shelf-life fields become required based on selected/loaded product attributes.

### Success behavior
- Receipt is marked verified and becomes available for put-away workflow.

### Error behavior
- Business-rule errors appear at line level when specific, otherwise as form-level banner.

---

## F-016 Receipt Discrepancy Form
- **Related screens:** `UI-016`
- **Aligned APIs:** `API-070`, `API-072`

### Fields
| Field | Input type | Required |
|---|---|---|
| Receipt Line ID | Context field | Yes |
| Discrepancy Type | Dropdown | Yes |
| Variance Quantity | Numeric field | Yes |
| Reason Code | Dropdown | Yes |
| Notes | Text area | Yes |
| Evidence Reference / Attachment | File upload or text field | No |
| Resolution Outcome | Dropdown | Conditional |
| Resolution Notes | Text area | Conditional |

### Validation messages
- `Discrepancy type is required.`
- `Variance quantity is required.`
- `Reason code is required.`
- `Notes are required.`
- `Resolution outcome is required to close this discrepancy.`
- `Resolution notes are required to close this discrepancy.`

### Inline validation behavior
- Close-resolution fields validate only when the user chooses a resolve action.

### Success behavior
- Discrepancy updates to resolved/open status and related receipt reflects accepted outcome.

### Error behavior
- Keep all evidence and notes attached to the draft state.

---

## F-017 Put-Away Form
- **Related screens:** `UI-017`
- **Aligned APIs:** `API-073`

### Fields
| Field | Input type | Required |
|---|---|---|
| Put-Away Lines | Repeating line-item editor | Yes |
| Receipt Line ID | Hidden/context | Yes |
| Quantity | Numeric field | Yes |
| Storage Position Code | Searchable dropdown | Yes |

### Validation messages
- `Add at least one put-away line.`
- `Quantity is required.`
- `Storage position is required.`
- `Put-away quantity cannot exceed the remaining unplaced quantity.`
- `Select a valid storage position.`

### Inline validation behavior
- Quantity and storage position validate per row.
- Remaining unplaced quantity should be visible as helper text.

### Success behavior
- Task is marked complete and quantity is moved to active stock position.

### Error behavior
- Keep the task open and preserve entered row values.

---

## F-018 Ad-Hoc Inbound Receipt Form
- **Related screens:** `UI-018`
- **Aligned APIs:** `API-075`

### Fields
| Field | Input type | Required |
|---|---|---|
| Receiving Location Code | Searchable dropdown | Yes |
| Ad-Hoc Authorization Reference | Text field | Yes |
| Reason Code | Dropdown | Yes |
| Source Description | Text area / text field | Yes |
| Lines | Repeating line-item editor | Yes |
| SKU | Searchable dropdown / text field | Yes |
| Quantity | Numeric field | Yes |

### Validation messages
- `Receiving location is required.`
- `Authorization reference is required.`
- `Reason code is required.`
- `Source description is required.`
- `Add at least one line.`
- `Quantity must be greater than 0.`

### Inline validation behavior
- Validate reference and reason code on blur/selection.

### Success behavior
- Create ad-hoc receipt and route to verification/put-away states.

### Error behavior
- Show governance-rule error if authorization is not valid.

---

## F-019 Inventory Status Filter Form
- **Related screens:** `UI-020`
- **Aligned APIs:** `API-033` to `API-037`

### Fields
| Field | Input type | Required |
|---|---|---|
| Location | Searchable dropdown | Conditional |
| SKU | Search field | Conditional |
| Category | Dropdown | No |
| Status | Dropdown | No |
| ABC Class | Dropdown | No |

### Validation messages
- `Enter at least one search filter.` when the query requires SKU or location context
- `You are not authorized for this location.`

### Inline validation behavior
- Validate scope-sensitive locations after selection.

### Success behavior
- Refresh the board/table results in place.

### Error behavior
- Keep selected filters and show a banner if the query is invalid or unauthorized.

---

## F-020 Availability Inquiry Form
- **Related screens:** `UI-021`
- **Aligned APIs:** `API-002`, `API-035`, `API-036`

### Fields
| Field | Input type | Required |
|---|---|---|
| SKU | Search field | Conditional |
| Product Name | Search field | Conditional |
| Barcode | Search field | Conditional |
| Category | Dropdown | No |
| Location | Searchable dropdown | Conditional |

### Validation messages
- `Enter a product search value.`
- `Select a valid product.`
- `You are not authorized for this location.`

### Inline validation behavior
- Search inputs can validate on submit rather than blur to avoid interrupting discovery.

### Success behavior
- Show matching products and availability detail.

### Error behavior
- No-match state uses empty-state messaging, not error styling.

---

## F-021 Movement History Query Form
- **Related screens:** `UI-022`
- **Aligned APIs:** `API-155`

### Fields
| Field | Input type | Required |
|---|---|---|
| Start Date | Date picker | Yes |
| End Date | Date picker | Yes |
| SKU | Search field | No |
| Location | Searchable dropdown | No |
| Transaction Type | Dropdown | No |
| User | Search field | No |

### Validation messages
- `Start date is required.`
- `End date is required.`
- `Start date must be on or before end date.`
- `Add at least one additional filter to narrow the result set.` when applicable to UX guidance

### Inline validation behavior
- Date range validation runs whenever either date changes.

### Success behavior
- Populate movement result list and detail panel.

### Error behavior
- Date-range issues shown inline on both date fields.

---

## F-022 Cycle Count Submission Form
- **Related screens:** `UI-023`
- **Aligned APIs:** `API-111`

### Fields
| Field | Input type | Required |
|---|---|---|
| Physical Quantity | Numeric field | Yes |
| Notes | Text area | No |

### Validation messages
- `Counted quantity is required.`
- `Counted quantity cannot be negative.`

### Inline validation behavior
- Quantity validates on blur and before submit.
- Do not expose expected system quantity during this workflow.

### Success behavior
- Show `Count submitted successfully.` and return to queue or next assignment.

### Error behavior
- Keep entered quantity intact unless the API rejects the case status.

---

## F-023 Physical Count Session Form
- **Related screens:** `UI-024`
- **Aligned APIs:** `API-112`, `API-114`, `API-115`

### Fields
| Field | Input type | Required |
|---|---|---|
| Location Code | Searchable dropdown | Yes |
| Planned Start Date | Date-time picker | Yes |
| Planned End Date | Date-time picker | Yes |
| Count Lines | Repeating line-item editor | Conditional during result entry |
| Physical Quantity | Numeric field | Yes per line during result entry |
| Certification Notes | Text area | No |

### Validation messages
- `Location is required.`
- `Planned start date is required.`
- `Planned end date is required.`
- `Planned end date must be on or after the start date.`
- `All required count lines must be entered before certification.`

### Inline validation behavior
- Start/end date validation runs immediately when either changes.
- Certification checks all required work is complete before submit.

### Success behavior
- Start action creates count session.
- Certification closes session and updates status badges.

### Error behavior
- Block certification until incomplete sections are resolved.

---

## F-024 Variance Investigation Form
- **Related screens:** `UI-025`
- **Aligned APIs:** `API-118`, `API-119`

### Fields
| Field | Input type | Required |
|---|---|---|
| Root Cause Category | Dropdown | Yes |
| Investigation Findings | Text area | Yes |
| Approved Adjustment Quantity | Numeric field | Conditional on approval |
| Approver Note | Text area | No |

### Validation messages
- `Root cause category is required.`
- `Investigation findings are required.`
- `Approved adjustment quantity is required to approve the variance.`
- `The approver cannot be the same person who performed the count.` (`BIZ_SEGREGATION_OF_DUTIES`)

### Inline validation behavior
- Approval quantity validates only when approval action is selected.

### Success behavior
- Case advances to approved/rejected state and updates pending approvals queue.

### Error behavior
- SoD and approval-rule failures show a form-level governance error.

---

## F-025 Stock Adjustment Form
- **Related screens:** `UI-026`
- **Aligned APIs:** `API-116`, `API-120`, `API-121`, `API-122`

### Fields
| Field | Input type | Required |
|---|---|---|
| Origin Type | Dropdown | Yes |
| Location Code | Searchable dropdown | Yes |
| SKU | Searchable dropdown / text field | Yes |
| Adjustment Type | Dropdown | Yes |
| Quantity | Numeric field | Yes |
| Reason Code | Dropdown | Yes |
| Notes | Text area | No |
| Evidence Reference | File upload / text field | Conditional for write-off |
| Rejection Reason | Text area | Conditional |

### Validation messages
- `Origin type is required.`
- `Location is required.`
- `Product is required.`
- `Adjustment type is required.`
- `Quantity is required.`
- `Reason code is required.`
- `Quantity must be greater than 0.`
- `Decrease quantity cannot exceed on-hand quantity.`
- `Evidence is required for write-offs.`
- `Rejection reason is required when rejecting an adjustment.`
- `This adjustment requires independent approval.` (`AUTHZ_APPROVAL_THRESHOLD` / `BIZ_SEGREGATION_OF_DUTIES`)

### Inline validation behavior
- Quantity direction and on-hand constraints validate when type and quantity are both known.
- Write-off evidence becomes required when adjustment type indicates write-off.

### Success behavior
- Case moves to pending approval or applied state depending on thresholds.

### Error behavior
- Preserve full draft including attachments and notes.
- Business-rule and approval-threshold failures remain at form level.

---

## F-026 Write-Off Authorization Form
- **Related screens:** `UI-027`
- **Aligned APIs:** `API-120`, `API-121`, `API-122`

### Fields
| Field | Input type | Required |
|---|---|---|
| Case ID | Context field | Yes |
| Approval Decision | Radio group | Yes |
| Finance Acknowledgment | Checkbox / status input | Conditional |
| Approver Note | Text area | No |
| Rejection Reason | Text area | Conditional |

### Validation messages
- `Approval decision is required.`
- `Finance acknowledgment is required before this write-off can be finalized.` when policy applies
- `Rejection reason is required when rejecting a write-off.`

### Inline validation behavior
- Decision-sensitive fields appear immediately after decision selection.

### Success behavior
- Show updated authorization status and refresh pending requests list.

### Error behavior
- If blocked by threshold or SoD rules, show governance message and keep user input.

---

## F-027 Quarantine / Hold Form
- **Related screens:** `UI-028`
- **Aligned APIs:** `API-045`, `API-046`

### Fields
| Field | Input type | Required |
|---|---|---|
| Quantity | Numeric field | Yes |
| Hold Reason | Dropdown | Yes |
| Reason Code | Dropdown | Yes |
| Lot Identity | Text field | Conditional |
| Disposition | Dropdown | Conditional on release |
| Inspection Outcome Reference | Text field | Conditional on restore to sellable |

### Validation messages
- `Quantity is required.`
- `Hold reason is required.`
- `Reason code is required.`
- `Lot number is required for traceable products.`
- `Hold quantity cannot exceed on-hand quantity.`
- `Disposition is required when releasing a hold.`
- `Inspection outcome reference is required before restoring stock to sellable status.`

### Inline validation behavior
- Release-specific fields validate only in release mode.
- Traceability rules activate based on product context.

### Success behavior
- Register updates instantly and affected availability metrics refresh.

### Error behavior
- Business-rule conflicts such as bonded/customs restrictions show as form-level errors.

---

## F-028 Order Creation / Import Form
- **Related screens:** `UI-030` supporting context
- **Aligned APIs:** `API-081`, `API-176`

### Fields
| Field | Input type | Required |
|---|---|---|
| Channel | Dropdown | Yes |
| External Order ID | Text field | Conditional for integration/import contexts |
| External System Code | Text field | Conditional for integration/import contexts |
| Order Lines | Repeating line-item editor | Yes |
| Line Number | Text field / auto-generated | Yes |
| SKU | Searchable dropdown / text field | Yes |
| Requested Quantity | Numeric field | Yes |

### Validation messages
- `Channel is required.`
- `Add at least one order line.`
- `Each order line must include a product and quantity.`
- `Quantity must be greater than 0.`
- `Product must be active.`
- `External order ID is required for imported orders.`
- `External system code is required for imported orders.`

### Inline validation behavior
- Validate each row independently and show row-level errors.

### Success behavior
- Order is created and available for availability/reservation flow.

### Error behavior
- Idempotent integration conflicts show clear conflict banner while preserving payload if user-entered.

---

## F-029 Order Availability / Reservation Form
- **Related screens:** `UI-030`
- **Aligned APIs:** `API-084`, `API-085`, `API-043`, `API-044`, `API-086`

### Fields
| Field | Input type | Required |
|---|---|---|
| Order ID | Context field | Yes |
| Selected Fulfillment Location | Searchable dropdown | Conditional |
| Reservation Quantity by Line | Numeric field | Conditional |
| Safety Stock Exception Reference | Text field | Conditional |
| Release Reason | Dropdown / text area | Conditional |
| Cancellation Reason | Text area | Conditional |

### Validation messages
- `Select a fulfillment location.`
- `Reservation quantity cannot exceed available-to-promise.`
- `A safety stock exception reference is required to continue.` (`BIZ_SAFETY_STOCK_BREACH`)
- `Release reason is required when releasing a reservation.`
- `Cancellation reason is required when canceling the order.`
- `This order is already confirmed.` (`CONF_ORDER_ALREADY_CONFIRMED`)

### Inline validation behavior
- Quantity validates against ATP after location is selected.
- Safety-stock reference becomes required only when a breach condition is detected.

### Success behavior
- Order status updates to reserved/released/canceled and warehouse queue state refreshes.

### Error behavior
- ATP and safety-stock failures show form-level business messages and line-level highlights where applicable.

---

## F-030 Pick Verification Form
- **Related screens:** `UI-031`
- **Aligned APIs:** `API-090`

### Fields
| Field | Input type | Required |
|---|---|---|
| Pick Lines | Repeating line-item editor | Yes |
| Picked Quantity | Numeric field | Yes |
| Picked SKU | Context / scanned input | Yes |
| Lot Number | Text field | Conditional |
| Substitution Reference | Text field | Conditional |

### Validation messages
- `Add at least one pick line.`
- `Picked quantity is required.`
- `Picked quantity cannot exceed reserved quantity.`
- `Lot number is required for traceable products.`
- `A substitution reference is required when the picked product differs from the order line.`

### Inline validation behavior
- Validate line by line as scans/entries occur.
- Substitution reference appears only when SKU mismatch is detected or selected.

### Success behavior
- Pick lines move to packed-ready state.

### Error behavior
- Quantity or SKU mismatches keep the pick in exception-ready state without losing scanned values.

---

## F-031 Pack Order Form
- **Related screens:** `UI-031`
- **Aligned APIs:** `API-091`

### Fields
| Field | Input type | Required |
|---|---|---|
| Packages | Repeating package editor | Yes |
| Package Reference | Text field | No |
| Package Line Items | Repeating line-item editor | Yes |
| Quantity per Line | Numeric field | Yes |

### Validation messages
- `Add at least one package.`
- `Each package must contain at least one line item.`
- `Packed quantity cannot exceed picked quantity.`

### Inline validation behavior
- Validate package totals against picked quantities whenever package lines change.

### Success behavior
- Order moves to packed state and enables shipment confirmation.

### Error behavior
- Preserve package structure and highlight the package row with the issue.

---

## F-032 Shipment Confirmation Form
- **Related screens:** `UI-031`
- **Aligned APIs:** `API-092`

### Fields
| Field | Input type | Required |
|---|---|---|
| Shipment Lines | Repeating line-item editor | Yes |
| Shipped Quantity | Numeric field | Yes |
| Carrier | Text field / dropdown | No |
| Tracking Reference | Text field | No |
| Lot Number | Text field | Conditional |

### Validation messages
- `Add at least one shipment line.`
- `Shipped quantity cannot exceed picked quantity.`
- `Lot number is required for traceable products.`
- `Pick verification must be completed before shipment.` (`BIZ_VERIFY_BEFORE_ACCEPTANCE`-style fulfillment rule / `BR-003`)

### Inline validation behavior
- Shipment line validation runs per row; traceability rules appear by product context.

### Success behavior
- Order status changes to shipped and reservation is cleared.

### Error behavior
- Keep shipment draft values if dispatch fails or network issue occurs.

---

## F-033 Partial Fulfillment / Backorder Form
- **Related screens:** `UI-032`
- **Aligned APIs:** `API-093`, `API-094`, `API-095`

### Fields
| Field | Input type | Required |
|---|---|---|
| Fulfillment Lines | Repeating line-item editor | Yes |
| Fulfill Quantity | Numeric field | Yes |
| Create Backorder for Remainder | Checkbox | Yes |
| Customer Acknowledgment Reference | Text field | Conditional |
| Priority Override Reference | Text field | Conditional for backorder fulfillment |

### Validation messages
- `Add at least one fulfillment line.`
- `Fulfill quantity must be greater than 0.`
- `Fulfill quantity must be less than the full ordered line for a partial fulfillment flow.`
- `Customer acknowledgment reference is required before creating a backorder.` (`BIZ_BACKORDER_ACK_REQUIRED`)
- `Backorder quantity must match the unfulfilled remainder.`
- `Priority override reference is required when fulfilling out of sequence.`

### Inline validation behavior
- Backorder-required fields validate as soon as the user indicates the remainder will be backordered.
- Recalculate remainder live as fulfill quantity changes.

### Success behavior
- Immediate quantity progresses to fulfillment; remainder moves into backorder state.

### Error behavior
- Keep line breakdown visible and preserve customer acknowledgment entry.

---

## F-034 Fulfillment Exception Form
- **Related screens:** `UI-033`
- **Aligned APIs:** `API-096`

### Fields
| Field | Input type | Required |
|---|---|---|
| Exception Type | Dropdown | Yes |
| Description | Text area | Yes |
| Resolution Path | Dropdown | No at creation; yes in resolution step |
| Notes | Text area | No |

### Validation messages
- `Exception type is required.`
- `Description is required.`
- `Description cannot be longer than 2000 characters.`

### Inline validation behavior
- Basic validation only on create; richer resolution validation occurs in downstream resolution interactions.

### Success behavior
- Exception case is logged and visible in exception queue.

### Error behavior
- Keep entered description and route context if submission fails.

---

## F-035 Multi-Location Fulfillment Plan Form
- **Related screens:** `UI-035`
- **Aligned APIs:** `API-087`

### Fields
| Field | Input type | Required |
|---|---|---|
| Allocations | Repeating line-item allocation editor | Yes |
| Location Code | Searchable dropdown | Yes |
| Quantity | Numeric field | Yes |

### Validation messages
- `Add at least one allocation.`
- `Each allocation must include a location and quantity.`
- `Allocated quantity cannot exceed ATP at the selected location.`
- `The total allocated quantity must equal the order line quantity.`

### Inline validation behavior
- Validate totals continuously as allocations change.
- Show remaining/unallocated quantity helper text.

### Success behavior
- Reservations are split by location and downstream pick queues are prepared.

### Error behavior
- Keep allocations intact when any one row fails.

---

## F-036 Alert Acknowledgment Form
- **Related screens:** `UI-004`, `UI-036`
- **Aligned APIs:** `API-159`

### Fields
| Field | Input type | Required |
|---|---|---|
| Action Taken | Dropdown / radio group | Yes |
| Acknowledgment Notes | Text area | Conditional |

### Validation messages
- `Action taken is required.`
- `Notes are required when dismissing or deferring an alert.`

### Inline validation behavior
- Notes validate immediately when `Dismiss` or `Defer` is selected.

### Success behavior
- Alert state updates and is removed from active queue when appropriate.

### Error behavior
- Preserve selected action and notes.

---

## F-037 Transfer Request Form
- **Related screens:** `UI-038`, `UI-041`
- **Aligned APIs:** `API-098`

### Fields
| Field | Input type | Required |
|---|---|---|
| Source Location Code | Searchable dropdown | Yes |
| Destination Location Code | Searchable dropdown | Yes |
| Justification | Text area | Yes |
| Lines | Repeating line-item editor | Yes |
| SKU | Searchable dropdown / text field | Yes |
| Quantity | Numeric field | Yes |

### Validation messages
- `Source location is required.`
- `Destination location is required.`
- `Source and destination cannot be the same.`
- `Justification is required.`
- `Add at least one transfer line.`
- `Quantity must be greater than 0.`
- `Requested quantity exceeds available transferable stock.`
- `This transfer would breach the source minimum threshold.` (`BIZ_SOURCE_MINIMUM_PROTECTED`)

### Inline validation behavior
- Source vs destination validation runs immediately when either location changes.
- Quantity validates against transferable capacity when source and SKU are known.

### Success behavior
- Transfer request is created and appears in approval queue.

### Error behavior
- Preserve all lines and justification.

---

## F-038 Transfer Approval Form
- **Related screens:** `UI-039`
- **Aligned APIs:** `API-101`, `API-102`

### Fields
| Field | Input type | Required |
|---|---|---|
| Decision | Radio group | Yes |
| Rejection Reason | Text area | Conditional |

### Validation messages
- `Approval decision is required.`
- `Rejection reason is required when rejecting a transfer.`
- `This transfer can no longer be approved in its current state.`

### Inline validation behavior
- Rejection reason validates immediately when reject is selected.

### Success behavior
- Request status updates to approved/rejected and dependent queues refresh.

### Error behavior
- Revalidation failures due to changed ATP show business-rule banner.

---

## F-039 Transfer Dispatch / Receipt Form
- **Related screens:** `UI-040`
- **Aligned APIs:** `API-103`, `API-104`, `API-105`

### Fields
| Field | Input type | Required |
|---|---|---|
| Dispatch Lines | Repeating line-item editor | Conditional on dispatch |
| Receipt Lines | Repeating line-item editor | Conditional on receipt |
| Quantity | Numeric field | Yes |
| Lot Number | Text field | Conditional |
| Variance Notes | Text area | Conditional |
| Cancellation Reason | Text area | Conditional |

### Validation messages
- `Add at least one transfer line.`
- `Dispatched quantity cannot exceed approved quantity.`
- `Received quantity is required.`
- `Variance notes are required when received quantity differs from dispatched quantity.`
- `A cancellation reason is required to cancel an in-transit transfer.`

### Inline validation behavior
- Dispatch and receipt validation depend on current workflow state.
- Variance notes appear only when mismatch is detected.

### Success behavior
- Dispatch moves transfer to in-transit state.
- Receipt completes transfer and updates both locations.

### Error behavior
- Preserve row edits and mismatch notes.

---

## F-040 Return Authorization Form
- **Related screens:** `UI-042`
- **Aligned APIs:** `API-124`, `API-127`

### Fields
| Field | Input type | Required |
|---|---|---|
| Original Order ID | Search/select field | Yes |
| Return Reason | Text area / text field | Yes |
| Return Lines | Repeating line-item editor | Yes |
| SKU / Order Line | Context/select field | Yes |
| Authorized Quantity | Numeric field | Yes |
| Cancellation Reason | Text area | Conditional |

### Validation messages
- `Original order is required.`
- `Return reason is required.`
- `Add at least one return line.`
- `Authorized quantity must be greater than 0.`
- `Authorized quantity cannot exceed shipped quantity.`
- `A cancellation reason is required when canceling a return authorization.`
- `This order line is not eligible for return.` (`BIZ_RETURN_AUTH_REQUIRED`-adjacent eligibility rule)

### Inline validation behavior
- Quantity validates against available shipped quantity after order line selection.

### Success behavior
- Return authorization is issued and visible in pending returns.

### Error behavior
- Preserve selected lines and quantities.

---

## F-041 Return Receipt / Inspection / Disposition Form
- **Related screens:** `UI-043`
- **Aligned APIs:** `API-128`, `API-129`, `API-130`

### Fields
| Field | Input type | Required |
|---|---|---|
| Return ID / Authorization Reference | Context field | Yes |
| Receiving Location Code | Searchable dropdown | Yes on receipt |
| Received Lines | Repeating line-item editor | Yes |
| Received Quantity | Numeric field | Yes |
| Inspection Lines | Repeating line-item editor | Yes on inspection |
| Condition | Dropdown | Yes |
| Disposition Action | Dropdown | Yes |
| Disposition Lines | Repeating line-item editor | Yes |
| Restock Location Code | Searchable dropdown | Conditional |
| Write-Off Reference / Evidence | Text field / upload | Conditional |

### Validation messages
- `Receiving location is required.`
- `Add at least one received line.`
- `Received quantity cannot exceed authorized quantity.`
- `Inspection must be completed before disposition.` (`BR-026`)
- `Disposition action is required.`
- `Disposition quantities must equal the inspected quantity.`
- `Restock location is required when returning inventory to stock.`
- `Write-off reference or evidence is required when disposition is write-off.`

### Inline validation behavior
- Workflow-step validation changes as the record moves from receipt to inspection to disposition.
- Quantity balancing runs continuously in disposition step.

### Success behavior
- Return progresses to the next state or completes with final inventory outcome.

### Error behavior
- Preserve line breakdowns and condition assessments across retries.

---

## F-042 Report Filter Form
- **Related screens:** `UI-044`
- **Aligned APIs:** `API-150` to `API-172` depending on selected report

### Fields
| Field | Input type | Required |
|---|---|---|
| Report Type | Dropdown | Yes |
| Start Date | Date picker | Conditional |
| End Date | Date picker | Conditional |
| Location | Searchable dropdown / multi-select | No |
| Category | Dropdown | No |
| Status | Dropdown | No |
| KPI Codes | Multi-select | Conditional |
| Period End Date | Date picker | Conditional for valuation reconciliation |

### Validation messages
- `Report type is required.`
- `Start date is required for this report.`
- `End date is required for this report.`
- `Start date must be on or before end date.`
- `The selected date range is too large for this report.`
- `Select valid KPI codes.`

### Inline validation behavior
- Required fields change based on selected report type.
- Date-range validation runs immediately after either date changes.

### Success behavior
- Report output refreshes in place.

### Error behavior
- Keep filters intact and focus the user on invalid filter fields.

---

## F-043 Valuation Reconciliation Form
- **Related screens:** `UI-045`
- **Aligned APIs:** `API-171`, `API-172`, `API-077` to `API-080` supporting context

### Fields
| Field | Input type | Required |
|---|---|---|
| Period End Date | Date picker | Yes |
| Variance Threshold Percent | Numeric field | No |
| Reconciliation Notes | Text area | No |
| Finalization Status | Dropdown / action choice | Conditional |

### Validation messages
- `Period end date is required.`
- `Variance threshold percent must be between 0 and 100.`

### Inline validation behavior
- Threshold field validates numeric range on blur.

### Success behavior
- The reconciliation view refreshes with final status and saved notes.

### Error behavior
- Preserve notes and selected period on failure.

---

## F-044 Promotional Allocation / Readiness Form
- **Related screens:** `UI-046`
- **Aligned APIs:** `API-132`, `API-135`, `API-136`, `API-137`, `API-138`

### Fields
| Field | Input type | Required |
|---|---|---|
| Campaign ID | Text field | Yes |
| Campaign Name | Text field | Yes |
| Location Code | Searchable dropdown | Yes |
| SKU | Searchable dropdown / text field | Yes |
| Allocated Quantity | Numeric field | Yes |
| Campaign Start Date | Date picker | Yes |
| Campaign End Date | Date picker | Yes |
| Amendment Reason | Text area | Conditional |
| Target Quantity | Numeric field | Conditional |
| Release Reason | Dropdown | Conditional |
| Override Quantity | Numeric field | Conditional |
| Authorization Reference | Text field | Conditional |
| Justification | Text area | Conditional |

### Validation messages
- `Campaign ID is required.`
- `Campaign name is required.`
- `Location is required.`
- `Product is required.`
- `Allocated quantity is required.`
- `Allocated quantity must be greater than 0.`
- `Campaign start date is required.`
- `Campaign end date is required.`
- `Campaign end date must be on or after campaign start date.`
- `Allocated quantity cannot exceed available stock.`
- `Authorization reference is required for promotional override.`
- `Justification is required for promotional override.`

### Inline validation behavior
- Date range validation and quantity-vs-ATP validation run immediately when inputs change.
- Action-specific fields validate only during amend/release/override actions.

### Success behavior
- Allocation/readiness status refreshes and campaign grid updates.

### Error behavior
- Ring-fence and ATP errors remain as form-level business messages.

---

## F-045 Audit Review Scope Form
- **Related screens:** `UI-047`
- **Aligned APIs:** `API-156`, `API-157`, `API-167`, `API-168`

### Fields
| Field | Input type | Required |
|---|---|---|
| Start Date | Date picker | Yes |
| End Date | Date picker | Yes |
| Location | Searchable dropdown / multi-select | No |
| Transaction Type | Dropdown | No |
| Reviewer | Text field / context field | No |
| Finding Type | Dropdown | Conditional when recording finding |
| Severity | Dropdown | Conditional when recording finding |
| Finding Note | Text area | Conditional when recording finding |
| Evidence Reference | File upload / text field | No |

### Validation messages
- `Start date is required.`
- `End date is required.`
- `Start date must be on or before end date.`
- `The selected date range is too large for audit export.`
- `Finding type is required when recording a finding.`
- `Severity is required when recording a finding.`
- `Finding note is required when recording a finding.`

### Inline validation behavior
- Date-range validation runs immediately.
- Finding fields only validate after the user chooses to record a finding.

### Success behavior
- Review scope loads results; findings save without leaving the review.

### Error behavior
- Export failures preserve the audit scope and show retry guidance.

---

## F-046 Audit Trail Query Form
- **Related screens:** `UI-048`
- **Aligned APIs:** `API-156`, `API-157`

### Fields
| Field | Input type | Required |
|---|---|---|
| Entity Type | Dropdown | No |
| Entity ID | Text field | No |
| User | Text field | No |
| Start Date | Date picker | Yes |
| End Date | Date picker | Yes |
| Action Type | Dropdown | No |

### Validation messages
- `Start date is required.`
- `End date is required.`
- `Start date must be on or before end date.`
- `The selected date range is too large for export.`

### Inline validation behavior
- Date fields revalidate together.

### Success behavior
- Results populate in query table; detail panel opens on row selection.

### Error behavior
- Keep query filters intact and show export/range messages inline and in banner if needed.

---

## F-047 User Account Form
- **Related screens:** `UI-049`
- **Aligned APIs:** `API-140`, `API-143`, `API-145`, `API-146`

### Fields
| Field | Input type | Required |
|---|---|---|
| User ID | Text field | Yes on create |
| Email | Email field | Yes |
| Display Name | Text field | Yes |
| Initial Roles / Role Assignments | Role assignment widget | Yes |
| Role Code | Dropdown | Yes |
| Location Codes | Multi-select | No |
| Effective From | Date picker | No |
| Effective To | Date picker | No |
| Suspension Reason | Text area | Conditional |
| Deactivation Reason | Text area | Conditional |

### Validation messages
- `User ID is required.`
- `User ID can contain letters, numbers, and underscores only.`
- `Email is required.`
- `Enter a valid email address.`
- `Display name is required.`
- `Assign at least one role.`
- `Effective to date must be on or after effective from date.`
- `This role assignment creates a segregation-of-duties conflict.` (`BIZ_SEGREGATION_OF_DUTIES`)
- `Suspension reason is required when suspending a user.`
- `Deactivation reason is required when deactivating a user.`

### Inline validation behavior
- Role and location assignments validate as a group.
- SoD checks can run after role selection if asynchronous evaluation is available.

### Success behavior
- User detail refreshes with active roles and status.

### Error behavior
- Preserve all role assignments and notes on error.

---

## F-048 Role and Access Control Form
- **Related screens:** `UI-050`
- **Aligned APIs:** `API-031`, `API-148`, `API-149`

### Fields
| Field | Input type | Required |
|---|---|---|
| Role Name | Text field / context field | Yes |
| Permission Group Assignments | Permission matrix | Yes |
| Location Scope Rules | Multi-select / scope selector | No |
| Initiator User ID | Text field | Conditional for SoD evaluation |
| Approver User ID | Text field | Conditional for SoD evaluation |
| Transaction Type | Dropdown | Conditional for SoD evaluation |

### Validation messages
- `Select at least one permission for this role.`
- `Approver cannot be the same as the initiator.` (`BIZ_SEGREGATION_OF_DUTIES`)
- `Select a valid transaction type for segregation-of-duties evaluation.`
- `You are not authorized to assign this role.` (`AUTHZ_ROLE_ASSIGNMENT_DENIED`)

### Inline validation behavior
- SoD evaluation can run when both users and transaction type are present.
- Permission matrix should show conflict/warning state before save where possible.

### Success behavior
- Permission matrix saves and confirmation banner appears.

### Error behavior
- Keep all edited permission changes in memory until user chooses to discard or retry.

---

## F-049 Session / Logout Form
- **Related screens:** Global user menu
- **Aligned APIs:** `API-174`

### Fields
| Field | Input type | Required |
|---|---|---|
| Logout All Sessions | Checkbox | No |

### Validation messages
- None beyond system-level failure messaging

### Inline validation behavior
- No inline validation required

### Success behavior
- End session and redirect to sign-in screen

### Error behavior
- If logout fails, show lightweight banner and allow retry

---

## Traceability Summary

- Product, catalog, and lifecycle forms align primarily to `VR-001` to `VR-010`.
- Location and storage forms align primarily to `VR-011` to `VR-017`.
- Stock policy, governance, and threshold forms align primarily to `VR-018` to `VR-028`.
- Procurement and supplier forms align primarily to `VR-030` to `VR-051`.
- Receiving and discrepancy forms align primarily to `VR-035` to `VR-048`.
- Fulfillment forms align primarily to `VR-090` to `VR-111`.
- Replenishment and transfer forms align primarily to `VR-117` to `VR-141`.
- Returns forms align primarily to `VR-142` to `VR-149`.
- Reporting and audit date-range forms align primarily to `VR-062`, `VR-153`, and related intelligence query rules.
- User and access forms align primarily to `VR-083` and location-scope validations such as `VR-008` and `VR-053`.

## Notes

- This specification is written for UX and frontend implementation and should be read together with the backend validation and error contracts.
- Final field-level implementation should preserve API naming, value constraints, and business-rule enforcement even if labels are simplified for users.
- Empty, loading, disabled, and async-check states should be specified in the next UI interaction-state pass.

