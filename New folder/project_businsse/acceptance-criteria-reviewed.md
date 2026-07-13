# Acceptance Criteria — Product Owner Review

**Document Owner:** Product Owner  
**Purpose:** Reviewed, complete acceptance criteria for every user story using Given / When / Then format, organized by product epic  
**Audience:** QA, product owners, business analysts, and delivery teams  
**Scope:** Acceptance criteria only — no technical implementation design  
**Based On:** BRD-IMS-001, User Stories (US-001 – US-090), EPIC-IMS-001, Functional Requirements (FR-001 – FR-090)  
**Review Date:** July 5, 2026

### Review Summary

| Check | Result |
|-------|--------|
| Stories covered | 90 |
| Categories per story | Happy Path · Validation Scenarios · Error Scenarios · Edge Cases |
| Minimum criteria per category | 2 |
| Given/When/Then compliance | All criteria include explicit **When** clause (35 rewritten in this review) |
| Role alignment | Operations Director, Warehouse Staff, IMS Administrator per reviewed user stories |

**Changes applied:** Fixed incomplete Given/Then criteria; corrected double-When grammar (US-017, US-035); aligned roles for US-003, US-023, US-026, US-042, US-046, US-081–US-085.

---

## Epic-to-Story Index

| Epic | User Stories |
|------|--------------|
| EPIC-01 | US-001 – US-012, US-056*, US-090* |
| EPIC-02 | US-013 – US-022, US-055* |
| EPIC-03 | US-023 – US-028 |
| EPIC-04 | US-029 – US-040 |
| EPIC-05 | US-041 – US-050 |
| EPIC-06 | US-051 – US-054, US-057 |
| EPIC-07 | US-058 – US-063 |
| EPIC-08 | US-064 – US-067 |
| EPIC-09 | US-068 – US-075, US-089* |
| EPIC-10 | US-076 – US-080 |
| EPIC-11 | US-081 – US-085 |
| EPIC-12 | US-086 – US-088 |

\* Stories physically located under adjacent epic sections for narrative flow; primary epic ownership per EPIC-IMS-001.

---

## How to Read This Document

Each user story includes acceptance criteria grouped into four categories:

| Category | Purpose |
|----------|---------|
| **Happy Path** | Standard successful business outcome |
| **Validation Scenarios** | Required data, business rules, and authorization checks |
| **Error Scenarios** | Failures the business must handle clearly |
| **Edge Cases** | Boundary conditions, exceptions, and unusual but valid situations |

**Criterion ID format:** `AC-{StoryNumber}-{Category}{Sequence}` (e.g., AC-001-H1 = US-001 Happy Path 1)

---

## EPIC-01: Master Data & Network Foundation

### US-001 — Create and Maintain Product Master Records
**Role:** Inventory Controller | **FR:** FR-001

#### Happy Path
- **AC-001-H1:** Given I am an authorized Inventory Controller and all required product attributes are provided, When I create a new product record with a unique SKU, Then the product is saved as active and visible to all authorized users and locations.
- **AC-001-H2:** Given an existing active product, When I update its name, description, category, or unit of measure, Then the changes are saved and reflected in all operational views referencing that product.

#### Validation Scenarios
- **AC-001-V1:** Given I submit a product without a SKU, name, or unit of measure, When I attempt to save, Then the system prevents save and indicates which required fields are missing.
- **AC-001-V2:** Given I enter a SKU that already exists, When I attempt to save a new product, Then the system prevents duplicate SKU creation and informs me of the existing record.

#### Error Scenarios
- **AC-001-E1:** Given I am a user without product maintenance authority, When I attempt to create or edit a product, Then the action is denied and I receive a clear unauthorized message.
- **AC-001-E2:** Given a product update fails mid-review, When I cancel or abandon the change, Then no partial or unapproved product record is published to operational users.

#### Edge Cases
- **AC-001-X1:** Given a product has existing stock or open orders, When I update non-identity attributes (e.g., description), Then historical transactions and balances remain correctly linked to the same SKU.
- **AC-001-X2:** Given a new product is created, When no stock policy thresholds exist yet, Then the product is still receivable and visible but excluded from threshold-based alerts until thresholds are defined.

---

### US-002 — Manage Product Status Lifecycle
**Role:** Inventory Controller | **FR:** FR-002

#### Happy Path
- **AC-002-H1:** Given an approved new product, When I set status to active, Then the product may be received, replenished, reserved, and fulfilled per business policy.
- **AC-002-H2:** Given a product marked discontinued, When remaining stock exists, Then the system flags remaining quantity for clearance or write-off planning and blocks new replenishment.

#### Validation Scenarios
- **AC-002-V1:** Given a product is inactive, When a user attempts to reserve or fulfill it, Then the system blocks the action unless policy explicitly allows inactive product fulfillment.
- **AC-002-V2:** Given a status change is submitted, When I confirm the change, Then the status change is recorded with user, date, and prior status for audit purposes.

#### Error Scenarios
- **AC-002-E1:** Given I lack authority to discontinue products, When I attempt to set status to discontinued, Then the action is denied.
- **AC-002-E2:** Given a product has open purchase orders or unfulfilled reservations, When I attempt to discontinue it, Then the system warns me of dependent activity before allowing the change.

#### Edge Cases
- **AC-002-X1:** Given a discontinued product with zero on-hand and no open activity, When I view the product, Then it remains searchable for history but excluded from active operational lists by default.
- **AC-002-X2:** Given a product is reactivated from inactive, When status returns to active, Then threshold alerts and replenishment eligibility resume based on current stock levels.

---

### US-003 — Product Identifier Lookup
**Role:** Warehouse Staff | **FR:** FR-003

#### Happy Path
- **AC-003-H1:** Given a valid SKU or barcode for an active product, When I search or scan during receiving, counting, or picking, Then the matching product is returned with core attributes and current stock context for my location.
- **AC-003-H2:** Given multiple lookup methods are supported, When I enter any assigned identifier for a product, Then the same product record is returned consistently.

#### Validation Scenarios
- **AC-003-V1:** Given I search by partial product name, When matches exist, Then the system returns a list of candidate products for selection.
- **AC-003-V2:** Given I am restricted to a specific location, When I look up a product, Then stock context shown reflects only locations I am authorized to view.

#### Error Scenarios
- **AC-003-E1:** Given an unknown or invalid identifier, When I search or scan, Then the system reports no match found and does not create a new product implicitly.
- **AC-003-E2:** Given a discontinued or inactive product identifier, When I scan during fulfillment, Then the system identifies the product and indicates its status before proceeding.

#### Edge Cases
- **AC-003-X1:** Given two products share similar names but different SKUs, When I search by name, Then both are listed with distinguishing SKU and category for correct selection.
- **AC-003-X2:** Given a product exists at multiple locations, When I look it up without specifying location, Then on-hand and ATP for my authorized default location are shown first.

---

### US-004 — Detect and Resolve Duplicate Product Records
**Role:** Inventory Controller | **FR:** FR-004

#### Happy Path
- **AC-004-H1:** Given I create a product with a SKU or name similar to an existing record, When I submit, Then the system alerts me to the potential duplicate and offers to correct the existing record instead.
- **AC-004-H2:** Given a duplicate is confirmed and merged, When merge completes, Then all stock and transaction history remain associated with a single product identity.

#### Validation Scenarios
- **AC-004-V1:** Given a potential duplicate is flagged, When I review the comparison, Then the system shows matching identifiers, names, and categories side by side.
- **AC-004-V2:** Given I choose to proceed with a genuinely new product despite similarity, When I document the justification, Then a new SKU is created and the decision is auditable.

#### Error Scenarios
- **AC-004-E1:** Given two products both have stock on hand, When I attempt an unauthorized merge, Then the system blocks merge without Inventory Controller approval.
- **AC-004-E2:** Given duplicate detection is inconclusive, When I cancel the create action, Then no duplicate or partial record is saved.

#### Edge Cases
- **AC-004-X1:** Given the same barcode was erroneously assigned to two SKUs, When duplicate is detected, Then I can reassign barcode to the correct SKU without losing movement history.
- **AC-004-X2:** Given periodic data quality review runs, When duplicates are found in existing catalog, Then they are surfaced in a review list for correction.

---

### US-005 — Configure and Maintain Inventory Locations
**Role:** Operations Director | **FR:** FR-005

#### Happy Path
- **AC-005-H1:** Given I am authorized, When I create a new warehouse, store, or distribution point with name, type, and operational status, Then the location is available for stock assignment and reporting.
- **AC-005-H2:** Given an existing location, When I update its name, type, or accountable manager, Then changes are reflected in all location-scoped views and reports.

#### Validation Scenarios
- **AC-005-V1:** Given required location attributes are missing, When I attempt to save, Then the system prevents save and identifies missing fields.
- **AC-005-V2:** Given a location is deactivated, When deactivation is confirmed, Then new receipts, reservations, and fulfillments are blocked except authorized disposition activities.

#### Error Scenarios
- **AC-005-E1:** Given I lack location configuration authority, When I attempt to create or modify a location, Then the action is denied.
- **AC-005-E2:** Given a location has not completed opening balance setup, When I attempt to activate it for transactions, Then activation is blocked until opening balance is approved.

#### Edge Cases
- **AC-005-X1:** Given a location is renamed, When I view historical reports, Then past transactions remain linked to the same location identity.
- **AC-005-X2:** Given two locations share a similar name, When I search locations, Then both are distinguishable by type, code, or address in results.

---

### US-006 — Manage Location Hierarchy
**Role:** Operations Director | **FR:** FR-006

#### Happy Path
- **AC-006-H1:** Given authorized access, When I assign a location to a parent region or group, Then stock visibility and reports can be rolled up to that hierarchy level.
- **AC-006-H2:** Given a hierarchy exists, When I view network inventory for a region, Then quantities aggregate all child locations under that region.

#### Validation Scenarios
- **AC-006-V1:** Given I attempt to assign a location as its own parent, When I save, Then the system prevents circular hierarchy creation.
- **AC-006-V2:** Given a parent location is selected for reporting, When no stock exists at child locations, Then the rollup correctly shows zero rather than omitting the region.

#### Error Scenarios
- **AC-006-E1:** Given a location reassignment would create a circular reference, When I submit, Then the change is rejected with an explanatory message.
- **AC-006-E2:** Given I lack hierarchy maintenance authority, When I attempt to modify hierarchy, Then the action is denied.

#### Edge Cases
- **AC-006-X1:** Given a location is moved from one region to another, When the change is saved, Then historical reports by period still reflect the hierarchy in effect at that time.
- **AC-006-X2:** Given a parent region has no direct stock (only children hold inventory), When I run a regional summary, Then only child location stock appears in the rollup.

---

### US-007 — Plan Location Closure and Stock Disposition
**Role:** Operations Director | **FR:** FR-007

#### Happy Path
- **AC-007-H1:** Given a location closure is approved, When I view remaining stock, Then all on-hand products and quantities at that location are listed for disposition planning.
- **AC-007-H2:** Given disposition actions are executed (transfer out, sell-through, or write-off), When all stock is cleared, Then the location can be deactivated without orphaned inventory records.

#### Validation Scenarios
- **AC-007-V1:** Given disposition is in progress, When new inbound or fulfillment is attempted at the closing location, Then those transactions are blocked unless explicitly authorized as part of closure.
- **AC-007-V2:** Given stock is transferred out during closure, When transfer completes, Then source location balance decreases and destination balance increases correctly.

#### Error Scenarios
- **AC-007-E1:** Given remaining stock exists, When I attempt to deactivate the location without a disposition plan, Then the system prevents closure until stock is addressed or explicitly waived by authorized approver.
- **AC-007-E2:** Given an unauthorized user initiates closure disposition, When they submit transfer or write-off, Then the action is denied.

#### Edge Cases
- **AC-007-X1:** Given partial disposition is complete, When some SKUs remain, Then closure status shows progress and only remaining items require action.
- **AC-007-X2:** Given a closing location has in-transit stock, When closure is planned, Then in-transit items are visible and must be received or resolved before final deactivation.

---

### US-008 — Define Stock Policy and Replenishment Thresholds
**Role:** Inventory Controller | **FR:** FR-008

#### Happy Path
- **AC-008-H1:** Given an active product at a location, When I set reorder level, minimum threshold, and safety stock, Then those values are stored and used for alert evaluation and replenishment suggestions.
- **AC-008-H2:** Given thresholds are updated, When I save with an effective date, Then the new values apply from that date and prior values are retained in history.

#### Validation Scenarios
- **AC-008-V1:** Given reorder level is set below minimum threshold, When I attempt to save, Then the system warns or prevents illogical threshold combinations per policy.
- **AC-008-V2:** Given safety stock exceeds reorder level, When I save, Then the system validates the configuration against business policy rules.

#### Error Scenarios
- **AC-008-E1:** Given I enter negative or non-numeric threshold values, When I save, Then the system rejects the input with a clear validation message.
- **AC-008-E2:** Given I lack threshold maintenance authority, When I attempt to change stock policy, Then the action is denied.

#### Edge Cases
- **AC-008-X1:** Given a product is sold at multiple locations, When I set thresholds for one location only, Then alerts and suggestions apply only at that location until others are configured.
- **AC-008-X2:** Given thresholds are removed or zeroed, When ATP monitoring runs, Then the product is excluded from threshold alerts until new values are defined.

---

### US-009 — Classify Products by ABC Priority
**Role:** Inventory Controller | **FR:** FR-009

#### Happy Path
- **AC-009-H1:** Given ABC classification is performed, When I assign class A, B, or C to a SKU, Then the classification is saved and reflected in count schedules, alert priority, and reporting groupings.
- **AC-009-H2:** Given a bulk classification review, When I update multiple SKUs, Then all selected products receive the new class with change history recorded.

#### Validation Scenarios
- **AC-009-V1:** Given a product has no classification assigned, When count scheduling runs, Then it follows the default frequency for unclassified items per policy.
- **AC-009-V2:** Given class A is assigned, When low-stock alert is generated, Then the alert receives higher priority than class C alerts for the same condition.

#### Error Scenarios
- **AC-009-E1:** Given I attempt to assign an invalid classification value, When I save, Then the system rejects the entry.
- **AC-009-E2:** Given I lack classification authority, When I attempt bulk update, Then the action is denied.

#### Edge Cases
- **AC-009-X1:** Given a product is reclassified from B to A mid-period, When cycle count schedule is evaluated, Then the higher frequency applies from the reclassification effective date.
- **AC-009-X2:** Given two products share the same revenue rank boundary, When classification is reviewed, Then business rules for tie-breaking are applied consistently.

---

### US-010 — Establish Opening Stock Balance at Location Go-Live
**Role:** Inventory Controller | **FR:** FR-010

#### Happy Path
- **AC-010-H1:** Given a new location is configured, When I enter opening balances from a verified physical count and receive authorized approval, Then the location is activated with trusted starting inventory.
- **AC-010-H2:** Given opening balance is approved, When operational transactions begin, Then all subsequent movements adjust from the approved baseline.

#### Validation Scenarios
- **AC-010-V1:** Given opening balance entry is incomplete for required SKUs, When I attempt to activate the location, Then activation is blocked until required items are counted and approved.
- **AC-010-V2:** Given opening balance requires approver sign-off, When submission occurs, Then the approver sees count details, location, and submitter before approval.

#### Error Scenarios
- **AC-010-E1:** Given opening balance is not approved, When a user attempts receipt or fulfillment at the location, Then transactions are blocked.
- **AC-010-E2:** Given count quantities are negative or non-numeric, When I submit, Then the system rejects invalid entries.

#### Edge Cases
- **AC-010-X1:** Given opening balance includes a SKU not yet in the product catalog, When I submit, Then the system flags the unknown product for resolution before activation.
- **AC-010-X2:** Given opening balance is revised before activation, When a correction is approved, Then only the latest approved baseline is used and prior draft is retained in audit history.

---

### US-011 — Maintain Standard Reason Codes
**Role:** Inventory Controller | **FR:** FR-011

#### Happy Path
- **AC-011-H1:** Given a corporate reason code list exists, When a user records an adjustment, write-off, or discrepancy, Then they must select from approved reason codes before submission.
- **AC-011-H2:** Given an authorized user adds a new reason code, When it is approved per policy, Then it becomes available for applicable transaction types.

#### Validation Scenarios
- **AC-011-V1:** Given reason code is mandatory for adjustments, When a user submits without selecting a code, Then submission is blocked.
- **AC-011-V2:** Given a reason code is retired, When users view selection lists, Then retired codes are hidden from new transactions but remain visible on historical records.

#### Error Scenarios
- **AC-011-E1:** Given I attempt to delete a reason code used on historical transactions, When I confirm deletion, Then the system prevents deletion or marks it inactive without breaking history.
- **AC-011-E2:** Given I lack reason code maintenance authority, When I attempt to add or retire codes, Then the action is denied.

#### Edge Cases
- **AC-011-X1:** Given location-extensible codes are permitted, When a location adds a local code, Then it is usable only at authorized locations unless promoted to corporate list.
- **AC-011-X2:** Given the same adjustment type supports multiple reason categories, When displayed, Then only applicable codes for that transaction type are shown.

---

### US-012 — Manage Inventory Governance Policies
**Role:** Operations Director | **FR:** FR-012

#### Happy Path
- **AC-012-H1:** Given governance policies are defined (approval thresholds, count tolerances, reservation timing), When authorized users view policy reference, Then current policy values and effective dates are displayed.
- **AC-012-H2:** Given a policy is updated, When the new version is published, Then operational workflows use the updated values from the effective date forward.

#### Validation Scenarios
- **AC-012-V1:** Given an adjustment exceeds the configured approval threshold, When submitted, Then it routes to the approver defined in policy automatically.
- **AC-012-V2:** Given count variance is within tolerance per policy, When count is submitted, Then it may auto-accept without investigation per configured rules.

#### Error Scenarios
- **AC-012-E1:** Given conflicting policy versions exist, When a transaction is evaluated, Then the system applies the single current effective policy without ambiguity.
- **AC-012-E2:** Given I lack policy maintenance authority, When I attempt to change governance parameters, Then the action is denied.

#### Edge Cases
- **AC-012-X1:** Given policy changes mid-day, When transactions submitted before the change are pending approval, Then they are evaluated against the policy in effect at submission time.
- **AC-012-X2:** Given a policy parameter is undefined, When a dependent workflow runs, Then the system flags the gap and prevents silent default behavior without authorized fallback.

---

## EPIC-02: Inbound Supply & Goods Receiving

### US-013 — Record Purchase Order Commitments
**Role:** Buyer | **FR:** FR-013

#### Happy Path
- **AC-013-H1:** Given replenishment need is approved, When I create a purchase order with product, quantity, supplier, expected delivery, and receiving location, Then the PO is saved as open and expected inbound quantity is visible to operations and sales.
- **AC-013-H2:** Given a PO is partially received, When I view the PO, Then received and outstanding quantities are shown separately and status reflects partial receipt.

#### Validation Scenarios
- **AC-013-V1:** Given required PO fields are missing, When I submit, Then save is blocked and missing fields are identified.
- **AC-013-V2:** Given the receiving location is deactivated, When I create a PO, Then the system prevents assignment to that location.

#### Error Scenarios
- **AC-013-E1:** Given I lack PO creation authority, When I submit a PO, Then the action is denied.
- **AC-013-E2:** Given the product is discontinued, When I add it to a PO, Then the system blocks or warns per policy before save.

#### Edge Cases
- **AC-013-X1:** Given multiple PO lines exist for the same product at one location, When inbound visibility is displayed, Then total expected inbound aggregates all open lines correctly.
- **AC-013-X2:** Given a PO expected date passes with no receipt, When inbound tracking is viewed, Then the PO appears as overdue for follow-up.

---

### US-014 — Plan and Communicate Expected Inbound Deliveries
**Role:** Warehouse Manager | **FR:** FR-014

#### Happy Path
- **AC-014-H1:** Given open POs with expected delivery dates exist, When I view the receiving schedule for my location, Then I see expected arrivals by date with products and quantities.
- **AC-014-H2:** Given a supplier confirms shipment, When expected delivery is updated, Then receiving teams see the revised date and contents.

#### Validation Scenarios
- **AC-014-V1:** Given I filter by date range, When I view inbound schedule, Then only deliveries within that range are shown.
- **AC-014-V2:** Given no inbound deliveries are scheduled, When I open the schedule, Then an empty state message is shown rather than stale data.

#### Error Scenarios
- **AC-014-E1:** Given I am restricted to Location A, When I attempt to view Location B inbound schedule, Then access is denied or data is hidden.
- **AC-014-E2:** Given delivery date is invalid, When a buyer updates expected delivery, Then the update is rejected.

#### Edge Cases
- **AC-014-X1:** Given multiple POs arrive on the same day, When schedule is viewed, Then all shipments are listed with combined dock workload visible.
- **AC-014-X2:** Given expected delivery is today but goods have not arrived, When schedule is viewed, Then the shipment appears as due/overdue for receiving attention.

---

### US-015 — Receive and Verify Inbound Goods
**Role:** Receiving Clerk | **FR:** FR-015

#### Happy Path
- **AC-015-H1:** Given a supplier shipment arrives with valid PO reference, When I verify quantity, product identity, and condition and record accepted quantity, Then on-hand increases only for verified accepted units and a receipt transaction is logged.
- **AC-015-H2:** Given accepted goods include damaged units, When I record accepted and rejected quantities separately, Then only accepted quantity enters receivable inventory.

#### Validation Scenarios
- **AC-015-V1:** Given received quantity exceeds PO open quantity, When I submit receipt, Then the system flags over-receipt per tolerance or approval rules.
- **AC-015-V2:** Given product identity does not match PO line, When I attempt receipt, Then the system prevents mismatched product acceptance without override.

#### Error Scenarios
- **AC-015-E1:** Given no PO or authorized ad-hoc approval exists, When I attempt standard supplier receipt, Then receipt is blocked.
- **AC-015-E2:** Given I enter zero or negative accepted quantity, When I submit, Then the receipt is rejected.

#### Edge Cases
- **AC-015-X1:** Given partial receipt against a PO line, When I receive remaining quantity later, Then cumulative received cannot exceed PO plus allowed tolerance without approval.
- **AC-015-X2:** Given receipt is recorded but put-away is not complete, When availability is queried, Then stock appears as received but not yet available for fulfillment.

---

### US-016 — Document and Resolve Receipt Discrepancies
**Role:** Receiving Clerk | **FR:** FR-016

#### Happy Path
- **AC-016-H1:** Given a quantity or condition mismatch at receipt, When I document discrepancy type, variance, and notes, Then disputed quantity is held from sellable availability until resolved.
- **AC-016-H2:** Given discrepancy is resolved with supplier credit or adjusted acceptance, When resolution is recorded, Then inventory and PO receipt status update to reflect the outcome.

#### Validation Scenarios
- **AC-016-V1:** Given a discrepancy is open, When I view the receipt, Then discrepancy status, type, and quantity are visible to receiving and purchasing roles.
- **AC-016-V2:** Given resolution requires purchasing approval, When I submit resolution, Then it routes to the authorized approver before inventory is finalized.

#### Error Scenarios
- **AC-016-E1:** Given I attempt to accept full PO quantity while discrepancy is unresolved, When I submit, Then the system prevents silent acceptance of disputed quantity.
- **AC-016-E2:** Given I lack authority to close a discrepancy, When I attempt resolution, Then the action is denied.

#### Edge Cases
- **AC-016-X1:** Given both short shipment and damage occur on the same line, When documented, Then each discrepancy type and quantity is captured separately.
- **AC-016-X2:** Given discrepancy remains unresolved beyond policy age, When purchasing reviews overdue list, Then the item appears for escalation.

---

### US-017 — Enforce Purchase Order Reference for Supplier Receipts
**Role:** Receiving Clerk | **FR:** FR-017

#### Happy Path
- **AC-017-H1:** Given a valid open PO exists for the shipment, When I receive goods against that PO, Then receipt proceeds and PO line eligibility is validated for product, location, and remaining quantity.
- **AC-017-H2:** Given emergency ad-hoc receipt is authorized, When I receive with approval reference and documented reason, Then receipt is accepted and exception is recorded for audit.

#### Validation Scenarios
- **AC-017-V1:** Given PO line is fully received, When I attempt additional receipt against that line, Then the system blocks unless over-receipt is approved per policy.
- **AC-017-V2:** Given ad-hoc receipt is attempted without approval, When I submit, Then receipt is blocked with instruction to obtain authorization.

#### Error Scenarios
- **AC-017-E1:** Given PO is cancelled, When I attempt receipt against it, Then receipt is rejected.
- **AC-017-E2:** Given PO belongs to a different receiving location, When I receive at my location, Then receipt is blocked unless PO allows cross-location receipt per policy.

#### Edge Cases
- **AC-017-X1:** Given a supplier delivers before the PO is visible to receiving, When the PO is confirmed and receipt is linked retroactively per policy, Then the audit trail shows timing and authorization.
- **AC-017-X2:** Given one delivery covers multiple PO lines, When I receive, Then I can allocate quantities across eligible PO lines in one session.

---

### US-018 — Manage Put-Away and Stock Availability Timing
**Role:** Warehouse Staff | **FR:** FR-018

#### Happy Path
- **AC-018-H1:** Given goods are verified at receipt, When put-away is confirmed, Then stock moves from receiving status to available and ATP increases accordingly.
- **AC-018-H2:** Given put-away is pending, When availability is queried, Then received quantity is visible as not yet available for sale or fulfillment.

#### Validation Scenarios
- **AC-018-V1:** Given partial put-away is completed, When I confirm put-away for a portion of received quantity, Then only that portion becomes available and remainder stays in receiving status.
- **AC-018-V2:** Given put-away requires supervisor assignment, When unauthorized staff attempt confirmation, Then action is denied per role policy.

#### Error Scenarios
- **AC-018-E1:** Given put-away quantity exceeds received quantity, When I submit, Then the system rejects the over-put-away attempt.
- **AC-018-E2:** Given receipt was rejected or cancelled, When put-away is attempted, Then put-away is blocked.

#### Edge Cases
- **AC-018-X1:** Given put-away is delayed overnight, When sales checks ATP, Then stock remains unavailable until put-away confirmation even though physically on site.
- **AC-018-X2:** Given multiple operators put away the same receipt, When concurrent confirmations occur, Then total put-away cannot exceed received quantity.

---

### US-019 — Receive Return and Non-PO Inbound Stock
**Role:** Receiving Clerk | **FR:** FR-019

#### Happy Path
- **AC-019-H1:** Given a valid return authorization exists, When I receive returned goods and record quantity and condition, Then return receipt is linked to the original order and routed to inspection or restock path.
- **AC-019-H2:** Given authorized non-PO inbound is approved, When I receive with reference and reason, Then inventory increase is recorded with full transaction history.

#### Validation Scenarios
- **AC-019-V1:** Given return receipt without valid authorization, When I submit, Then receipt is blocked or flagged for supervisor review per policy.
- **AC-019-V2:** Given inspection is required before restock, When receipt is recorded, Then quantity is not added to sellable ATP until inspection passes.

#### Error Scenarios
- **AC-019-E1:** Given returned product does not match authorization line, When I receive, Then mismatch is flagged and quantity is not silently accepted.
- **AC-019-E2:** Given I lack return receipt authority, When I attempt receipt, Then action is denied.

#### Edge Cases
- **AC-019-X1:** Given customer returns partial quantity against authorization, When received, Then remaining authorized quantity stays open for future receipt.
- **AC-019-X2:** Given multiple return authorizations arrive in one shipment, When processed, Then each authorization is matched and recorded separately.

---

### US-020 — Support Receipt Quantity Tolerance Evaluation
**Role:** Receiving Clerk | **FR:** FR-020

#### Happy Path
- **AC-020-H1:** Given received quantity is within defined tolerance of PO expected quantity, When I submit receipt, Then receipt auto-accepts without additional approval.
- **AC-020-H2:** Given tolerance rules differ by product class, When receipt is evaluated, Then the correct tolerance band is applied automatically.

#### Validation Scenarios
- **AC-020-V1:** Given over-receipt exceeds tolerance, When I submit, Then approval is required before acceptance is finalized.
- **AC-020-V2:** Given under-receipt is within tolerance, When I submit, Then PO line closes or remains open per policy with documented variance.

#### Error Scenarios
- **AC-020-E1:** Given tolerance policy is undefined for a product class, When receipt is submitted, Then the system applies default corporate tolerance or blocks pending policy definition per configuration.
- **AC-020-E2:** Given approver rejects over-receipt, When decision is recorded, Then only approved quantity enters inventory.

#### Edge Cases
- **AC-020-X1:** Given receipt is exactly at tolerance boundary, When evaluated, Then behavior matches policy definition for inclusive/exclusive boundary consistently.
- **AC-020-X2:** Given cumulative receipts across multiple deliveries, When tolerance is evaluated, Then total received against PO line is considered not just single delivery.

---

### US-021 — Cancel or Amend Open Purchase Orders
**Role:** Buyer | **FR:** FR-021

#### Happy Path
- **AC-021-H1:** Given a PO line is open with no receipt, When I cancel the line or entire PO, Then expected inbound quantity is removed and PO status reflects cancellation.
- **AC-021-H2:** Given demand changes, When I amend open quantity or expected delivery date, Then inbound projections update and change history is retained.

#### Validation Scenarios
- **AC-021-V1:** Given a PO line is partially received, When I amend quantity below received amount, Then amendment is blocked.
- **AC-021-V2:** Given cancellation requires approval, When I submit, Then it routes to approver before taking effect.

#### Error Scenarios
- **AC-021-E1:** Given PO is fully received, When I attempt cancellation, Then the action is rejected.
- **AC-021-E2:** Given I lack amend authority, When I attempt PO change, Then action is denied.

#### Edge Cases
- **AC-021-X1:** Given supplier confirms partial cancellation, When I amend multiple lines, Then each line history shows independent change records.
- **AC-021-X2:** Given cancelled PO had linked replenishment alert, When cancellation completes, Then alert re-evaluates and may reopen if stock still below threshold.

---

### US-022 — Record Supplier Delivery Performance
**Role:** Purchasing Manager | **FR:** FR-022

#### Happy Path
- **AC-022-H1:** Given receipts and PO records exist, When I view supplier performance, Then on-time delivery rate, quantity accuracy, and discrepancy frequency are displayed by supplier.
- **AC-022-H2:** Given a reporting period is selected, When performance is calculated, Then metrics reflect only transactions within that period.

#### Validation Scenarios
- **AC-022-V1:** Given a supplier has no receipts in period, When I view performance, Then metrics show no activity rather than zero-percent inaccurately.
- **AC-022-V2:** Given discrepancy was resolved, When accuracy is calculated, Then final accepted quantity determines accuracy metric per policy.

#### Error Scenarios
- **AC-022-E1:** Given I lack purchasing management reporting access, When I request supplier performance, Then access is denied.
- **AC-022-E2:** Given data is incomplete for a receipt date, When metrics run, Then those records are excluded or flagged rather than skewing results silently.

#### Edge Cases
- **AC-022-X1:** Given supplier had both early and late deliveries, When on-time metric is shown, Then calculation follows defined on-time business rule consistently.
- **AC-022-X2:** Given same supplier serves multiple locations, When I filter by location, Then performance metrics scope to selected locations only.

---

## EPIC-03: Real-Time Inventory Visibility

### US-023 — Display On-Hand Quantity by Product and Location
**Role:** Operations Director | **FR:** FR-023

#### Happy Path
- **AC-023-H1:** Given inventory movements have been recorded, When I query on-hand for a product at a location, Then the quantity reflects all receipts, transfers, adjustments, and fulfillments to date.
- **AC-023-H2:** Given a movement occurs, When I refresh or view on-hand immediately after, Then the balance reflects the latest transaction without manual recalculation.

#### Validation Scenarios
- **AC-023-V1:** Given I am authorized for multiple locations, When I view the same product, Then I see separate on-hand per location accurately.
- **AC-023-V2:** Given product has zero on-hand, When I query, Then zero is displayed clearly rather than omitting the product.

#### Error Scenarios
- **AC-023-E1:** Given I am not authorized for a location, When I query its on-hand, Then data is hidden or access is denied.
- **AC-023-E2:** Given product SKU does not exist, When I query on-hand, Then a not-found result is returned without error crash.

#### Edge Cases
- **AC-023-X1:** Given concurrent movements at same location, When balances update, Then final on-hand remains consistent with transaction sequence.
- **AC-023-X2:** Given product exists but never had activity at a location, When queried, Then on-hand shows zero with no misleading historical balance.

---

### US-024 — Display Available-to-Promise (ATP) Quantity
**Role:** Sales Representative | **FR:** FR-024

#### Happy Path
- **AC-024-H1:** Given on-hand stock exists with no reservations or holds, When I view ATP, Then ATP equals sellable on-hand at that location.
- **AC-024-H2:** Given reservations exist, When I view ATP, Then ATP equals on-hand minus reserved and non-sellable held quantity.

#### Validation Scenarios
- **AC-024-V1:** Given quarantined stock exists, When ATP is calculated, Then quarantined quantity is excluded from ATP.
- **AC-024-V2:** Given stock is in receiving pending put-away, When ATP is shown, Then receiving quantity is excluded from ATP.

#### Error Scenarios
- **AC-024-E1:** Given ATP would display negative due to data exception, When viewed, Then system shows zero or flags data issue per policy rather than negative sellable quantity.
- **AC-024-E2:** Given I query ATP for an unauthorized location, When the query runs, Then access is denied.

#### Edge Cases
- **AC-024-X1:** Given reservation is partially released, When ATP updates, Then released quantity immediately returns to ATP.
- **AC-024-X2:** Given safety stock policy reserves buffer, When ATP is displayed, Then safety stock treatment follows defined business rule consistently.

---

### US-025 — Display Reserved and Committed Stock
**Role:** Customer Service Representative | **FR:** FR-025

#### Happy Path
- **AC-025-H1:** Given orders have reserved stock, When I view reservations by order, Then product, quantity, location, and order reference are shown for each reservation.
- **AC-025-H2:** Given I view reservations by product, When reservations exist, Then total reserved quantity aggregates all orders at that location.

#### Validation Scenarios
- **AC-025-V1:** Given an order is partially shipped, When I view reservations, Then shipped quantity is deducted and remaining reservation is shown accurately.
- **AC-025-V2:** Given order is cancelled, When I view reservations, Then reservation no longer appears and ATP is restored.

#### Error Scenarios
- **AC-025-E1:** Given I search for a non-existent order, When I query reservations, Then no reservation data is returned with clear not-found indication.
- **AC-025-E2:** Given I lack access to the fulfillment location, When I query its reservations, Then data is restricted.

#### Edge Cases
- **AC-025-X1:** Given same product reserved across multiple orders, When total reserved exceeds on-hand, Then system flags oversold condition for operations review.
- **AC-025-X2:** Given split fulfillment across locations, When reservations are viewed at order level, Then all location reservations appear under one order summary.

---

### US-026 — Indicate Stock Status (In Stock, Low Stock, Out of Stock)
**Role:** Operations Director | **FR:** FR-026

#### Happy Path
- **AC-026-H1:** Given ATP is above reorder level, When status is displayed, Then product shows as in stock at that location.
- **AC-026-H2:** Given ATP falls below reorder level but above zero, When status updates, Then product shows as low stock.

#### Validation Scenarios
- **AC-026-V1:** Given ATP reaches zero, When status is evaluated, Then product shows as out of stock.
- **AC-026-V2:** Given thresholds are updated, When status is recalculated, Then status reflects new thresholds without manual refresh beyond normal update cycle.

#### Error Scenarios
- **AC-026-E1:** Given no threshold is defined, When status is derived, Then product shows neutral/unclassified status rather than incorrect low-stock flag.
- **AC-026-E2:** Given location is deactivated, When status lists are viewed, Then deactivated location stock is excluded from active operational status views by default.

#### Edge Cases
- **AC-026-X1:** Given ATP exactly equals reorder level, When status is assigned, Then boundary behavior matches policy definition consistently.
- **AC-026-X2:** Given product is discontinued with remaining stock, When status is shown, Then status reflects quantity and discontinued flag together.

---

### US-027 — Search and Filter Inventory Views
**Role:** Sales Representative | **FR:** FR-027

#### Happy Path
- **AC-027-H1:** Given I apply filters for location, category, and status, When search runs, Then results show matching products with on-hand, reserved, ATP, and status.
- **AC-027-H2:** Given I export or print filtered results, When export completes, Then output matches on-screen filtered data for my authorized scope.

#### Validation Scenarios
- **AC-027-V1:** Given no products match filters, When search runs, Then empty results message is shown.
- **AC-027-V2:** Given multiple filters are combined, When search runs, Then only products meeting all selected criteria are returned.

#### Error Scenarios
- **AC-027-E1:** Given I include unauthorized location in filter, When search runs, Then unauthorized location data is excluded from results.
- **AC-027-E2:** Given invalid filter values are entered, When search runs, Then validation message is shown and search does not return misleading results.

#### Edge Cases
- **AC-027-X1:** Given large result set, When search returns, Then results remain usable and accurately paginated or summarized per policy.
- **AC-027-X2:** Given ABC class filter is applied before ABC is configured, When search runs, Then unclassified products behave per defined default filter rule.

---

### US-028 — Display Expected Inbound and Network-Wide Availability
**Role:** Purchasing Manager | **FR:** FR-028

#### Happy Path
- **AC-028-H1:** Given open POs exist, When I view expected inbound for a product, Then expected quantity and date are shown by receiving location.
- **AC-028-H2:** Given I view network-wide availability, When aggregating ATP across locations, Then total network ATP and location breakdown are both visible.

#### Validation Scenarios
- **AC-028-V1:** Given one location is out of stock but another has excess, When network view is shown, Then transfer-before-purchase opportunity is identifiable.
- **AC-028-V2:** Given inbound PO is partially received, When expected inbound is shown, Then only outstanding PO quantity appears as expected.

#### Error Scenarios
- **AC-028-E1:** Given no open inbound supply exists, When expected inbound is queried, Then zero expected inbound is shown clearly.
- **AC-028-E2:** Given I lack network-wide access, When I request all-location aggregation, Then only authorized locations are included.

#### Edge Cases
- **AC-028-X1:** Given expected inbound date is past due, When displayed, Then item is flagged overdue for replenishment follow-up.
- **AC-028-X2:** Given same SKU is stocked at many locations, When network ATP is calculated, Then sum matches sum of individual location ATP values.

---

## EPIC-04: Inventory Control & Accuracy

### US-029 — Record All Inventory Movements with Full History
**Role:** Inventory Controller | **FR:** FR-029

#### Happy Path
- **AC-029-H1:** Given any receipt, transfer, adjustment, fulfillment, or return is completed, When the transaction is saved, Then a movement record is created with product, quantity, location, user, timestamp, and transaction type.
- **AC-029-H2:** Given I query movement history for a product, When results display, Then all movement types appear in chronological order with complete attribution.

#### Validation Scenarios
- **AC-029-V1:** Given I filter history by date range and transaction type, When query runs, Then only matching movements are returned.
- **AC-029-V2:** Given movement affects two locations (transfer), When recorded, Then both outbound and inbound legs appear in history with linked reference.

#### Error Scenarios
- **AC-029-E1:** Given unauthorized user attempts a movement, When blocked, Then no movement record or balance change occurs.
- **AC-029-E2:** Given movement submission fails validation, When rejected, Then no partial movement record corrupts balances.

#### Edge Cases
- **AC-029-X1:** Given high transaction volume day, When history is queried, Then results remain accurate and complete for the period.
- **AC-029-X2:** Given reversal or correction of prior movement, When recorded, Then history shows corrective entry linked to original without deleting original audit record.

---

### US-030 — Schedule and Assign Cycle Counts
**Role:** Inventory Controller | **FR:** FR-030

#### Happy Path
- **AC-030-H1:** Given count calendar defines assignments, When schedule date arrives, Then count tasks are generated with product, location, and assigned counter.
- **AC-030-H2:** Given high-variance SKU is flagged, When priority override is applied, Then expedited count task is created outside normal schedule.

#### Validation Scenarios
- **AC-030-V1:** Given ABC class drives frequency, When schedule generates, Then class A items appear more frequently than class C per policy.
- **AC-030-V2:** Given count task is completed, When status updates, Then task shows complete and is removed from open assignment list.

#### Error Scenarios
- **AC-030-E1:** Given location is deactivated, When schedule runs, Then no new count tasks are generated for that location.
- **AC-030-E2:** Given no counter is assigned, When task is released, Then task remains unassigned and visible for supervisor action.

#### Edge Cases
- **AC-030-X1:** Given count is rescheduled, When new date is set, Then original task history retains reschedule audit and new task date applies.
- **AC-030-X2:** Given same SKU scheduled at two locations same day, When tasks generate, Then separate location-specific tasks are created.

---

### US-031 — Perform Blind Cycle Counts
**Role:** Warehouse Staff | **FR:** FR-031

#### Happy Path
- **AC-031-H1:** Given I open an assigned count task, When count screen displays, Then I see product and location only without system expected quantity.
- **AC-031-H2:** Given I submit physical count quantity, When submission completes, Then variance is calculated and shown only after submission.

#### Validation Scenarios
- **AC-031-V1:** Given I attempt to view expected quantity before submit, When restricted, Then expected quantity remains hidden per blind count policy.
- **AC-031-V2:** Given count quantity is zero, When I submit, Then zero physical count is accepted as valid result.

#### Error Scenarios
- **AC-031-E1:** Given I am not assigned counter for task, When I attempt count entry, Then action is denied.
- **AC-031-E2:** Given non-numeric count entered, When I submit, Then submission is rejected.

#### Edge Cases
- **AC-031-X1:** Given I save draft count and resume later, When I return, Then expected quantity remains hidden until final submission.
- **AC-031-X2:** Given recount is ordered after variance, When new blind count task opens, Then prior submitted count remains in history and new count is independent.

---

### US-032 — Conduct Full Physical Inventory Count
**Role:** Inventory Controller | **FR:** FR-032

#### Happy Path
- **AC-032-H1:** Given full count is initiated for a location, When movement freeze is active, Then receipts, shipments, transfers, and adjustments are blocked per policy until count completes.
- **AC-032-H2:** Given all SKUs are counted and submitted, When count closes, Then comprehensive variance report is generated for approval.

#### Validation Scenarios
- **AC-032-V1:** Given movement freeze exception is authorized for emergency, When recorded, Then exception is logged and visible in count audit.
- **AC-032-V2:** Given partial location count progress exists, When count status is viewed, Then completion percentage and remaining SKUs are visible.

#### Error Scenarios
- **AC-032-E1:** Given movement attempted during freeze without authorization, When submitted, Then transaction is blocked.
- **AC-032-E2:** Given count closed without approval, When adjustment from count is attempted, Then adjustments remain pending until approved.

#### Edge Cases
- **AC-032-X1:** Given count spans multiple days per policy, When freeze extends, Then freeze status and authorized exceptions remain auditable across days.
- **AC-032-X2:** Given SKU with zero on-hand is included, When counted as zero, Then variance report includes zero lines for completeness.

---

### US-033 — Identify and Report Count Variances
**Role:** Inventory Controller | **FR:** FR-033

#### Happy Path
- **AC-033-H1:** Given physical count differs from system quantity, When count is submitted, Then variance quantity and direction (short/over) are calculated automatically.
- **AC-033-H2:** Given variance exceeds tolerance, When evaluated, Then item is routed for investigation rather than auto-adjusted.

#### Validation Scenarios
- **AC-033-V1:** Given variance is within tolerance, When policy allows auto-accept, Then item may proceed without investigation per rules.
- **AC-033-V2:** Given variance summary is requested, When report runs, Then variances group by location, product, and counter accurately.

#### Error Scenarios
- **AC-033-E1:** Given count submission missing quantity, When evaluated, Then variance is not calculated until valid quantity provided.
- **AC-033-E2:** Given tolerance policy undefined, When variance evaluated, Then item defaults to investigation route rather than silent adjust.

#### Edge Cases
- **AC-033-X1:** Given variance exactly equals tolerance limit, When evaluated, Then boundary behavior matches policy consistently.
- **AC-033-X2:** Given recurring variance on same SKU, When summary viewed, Then trend highlights repeat variances for root-cause review.

---

### US-034 — Investigate and Approve Count Adjustments
**Role:** Warehouse Manager | **FR:** FR-034

#### Happy Path
- **AC-034-H1:** Given material variance requires investigation, When I review with transaction history and document root cause, Then investigation notes are saved with variance record.
- **AC-034-H2:** Given investigation supports adjustment, When independent approver approves, Then inventory balance updates and variance is closed.

#### Validation Scenarios
- **AC-034-V1:** Given counter and approver are same person, When approval attempted, Then self-approval is blocked per segregation of duties.
- **AC-034-V2:** Given approver rejects adjustment, When rejection recorded with reason, Then balance remains unchanged and variance stays open or closed per policy.

#### Error Scenarios
- **AC-034-E1:** Given investigation notes are missing for material variance, When approval attempted, Then approval is blocked per policy.
- **AC-034-E2:** Given I am an unauthorized approver, When I attempt to approve a count adjustment, Then the action is denied.

#### Edge Cases
- **AC-034-X1:** Given recount changes variance before approval, When new count submitted, Then approval package updates to latest count result.
- **AC-034-X2:** Given multiple variances from same count event, When bulk approval attempted, Then each line retains individual investigation and approval record.

---

### US-035 — Process Stock Adjustments with Mandatory Reason Codes
**Role:** Warehouse Manager | **FR:** FR-035

#### Happy Path
- **AC-035-H1:** Given I submit adjustment with product, location, quantity, direction, and reason code, When approved per policy, Then on-hand and ATP update and movement history records the change.
- **AC-035-H2:** Given positive adjustment (increase), When approved, Then inventory increases with same accountability as decreases.

#### Validation Scenarios
- **AC-035-V1:** Given reason code is not selected, When I submit, Then adjustment is blocked.
- **AC-035-V2:** Given adjustment exceeds my approval limit, When submitted, Then it routes to higher approver automatically.

#### Error Scenarios
- **AC-035-E1:** Given adjustment would drive on-hand negative, When submitted, Then adjustment is rejected unless negative inventory explicitly allowed by policy.
- **AC-035-E2:** Given I am an unauthorized user, When I submit a stock adjustment, Then the action is denied.

#### Edge Cases
- **AC-035-X1:** Given an adjustment is pending approval, When on-hand changes due to other transactions before approval completes, Then the adjustment applies to the current balance upon approval with audit showing timing.
- **AC-035-X2:** Given duplicate adjustment requests for same event, When second is submitted, Then system warns of potential duplicate per policy.

---

### US-036 — Process Inventory Write-Offs with Authorization
**Role:** Warehouse Manager | **FR:** FR-036

#### Happy Path
- **AC-036-H1:** Given obsolete or damaged stock must be removed, When I submit write-off with evidence, reason code, and quantity, Then upon approval on-hand and ATP decrease permanently for that quantity.
- **AC-036-H2:** Given write-off is approved, When recorded, Then write-off appears in shrinkage reporting and movement history.

#### Validation Scenarios
- **AC-036-V1:** Given write-off exceeds threshold, When submitted, Then higher-level approval is required before inventory is reduced.
- **AC-036-V2:** Given evidence attachment is required by policy, When missing, Then submission is blocked.

#### Error Scenarios
- **AC-036-E1:** Given write-off quantity exceeds on-hand, When submitted, Then write-off is rejected.
- **AC-036-E2:** Given approver denies write-off, When decision saved, Then inventory remains unchanged.

#### Edge Cases
- **AC-036-X1:** Given partial write-off of damaged lot, When approved, Then remaining sellable quantity stays available if any.
- **AC-036-X2:** Given write-off submitted for product under investigation, When policy requires hold, Then write-off is blocked until investigation closes.

---

### US-037 — Enforce Adjustment Approval Thresholds
**Role:** Operations Director | **FR:** FR-037

#### Happy Path
- **AC-037-H1:** Given adjustment is within my delegated threshold, When I submit as authorized approver, Then it may auto-approve per role policy.
- **AC-037-H2:** Given adjustment exceeds threshold, When submitted, Then it routes to Operations Director or designated approver with full context.

#### Validation Scenarios
- **AC-037-V1:** Given threshold is defined by both quantity and value, When either limit exceeded, Then escalation triggers per policy.
- **AC-037-V2:** Given approver is unavailable, When delegation rule exists, Then alternate approver receives notification per policy.

#### Error Scenarios
- **AC-037-E1:** Given self-approval attempted above threshold, When submitted, Then blocked and rerouted to independent approver.
- **AC-037-E2:** Given threshold configuration missing, When adjustment submitted, Then system routes to default approver rather than auto-approving silently.

#### Edge Cases
- **AC-037-X1:** Given currency/value threshold uses product cost, When cost missing, Then escalation follows defined fallback policy.
- **AC-037-X2:** Given batch of small adjustments same day same SKU, When cumulative impact exceeds threshold, Then policy defines whether batch escalation applies.

---

### US-038 — Manage Quarantine and Hold Stock Status
**Role:** Warehouse Manager | **FR:** FR-038

#### Happy Path
- **AC-038-H1:** Given stock requires quality hold, When I place quantity on quarantine, Then that quantity is immediately excluded from ATP and cannot be fulfilled.
- **AC-038-H2:** Given inspection passes, When I release from quarantine, Then quantity returns to available ATP with release recorded in history.

#### Validation Scenarios
- **AC-038-V1:** Given partial quantity held, When ATP viewed, Then only held portion is excluded and remainder stays available.
- **AC-038-V2:** Given inspection fails, When disposition is write-off, Then quarantined quantity routes to write-off workflow without returning to ATP.

#### Error Scenarios
- **AC-038-E1:** Given fulfillment attempted from quarantined stock, When processed, Then fulfillment is blocked.
- **AC-038-E2:** Given hold quantity exceeds on-hand, When hold submitted, Then action is rejected.

#### Edge Cases
- **AC-038-X1:** Given hold expires per policy without decision, When expiry triggers, Then item escalates for supervisor review rather than auto-releasing silently.
- **AC-038-X2:** Given return stock and damaged inbound both require hold, When viewed, Then hold reason distinguishes sources in status views.

---

### US-039 — Analyze Shrinkage and Loss Trends
**Role:** Inventory Controller | **FR:** FR-039

#### Happy Path
- **AC-039-H1:** Given adjustments and write-offs exist for a period, When I run shrinkage analysis, Then totals group by reason code, location, and period accurately.
- **AC-039-H2:** Given recurring variance SKUs exist, When analysis runs, Then repeat offenders are highlighted for investigation.

#### Validation Scenarios
- **AC-039-V1:** Given date range filter applied, When report runs, Then only transactions in range are included.
- **AC-039-V2:** Given comparison to prior period requested, When displayed, Then trend direction (increase/decrease) is shown per category.

#### Error Scenarios
- **AC-039-E1:** Given no loss activity in period, When report runs, Then zero-activity report displays rather than error.
- **AC-039-E2:** Given I request unauthorized location data, When the shrinkage report runs, Then unauthorized locations are excluded from the report scope.

#### Edge Cases
- **AC-039-X1:** Given same event generated adjustment and write-off, When analyzed, Then reporting avoids double-counting per defined business rule.
- **AC-039-X2:** Given reason code was reclassified historically, When trend spans periods, Then report notes classification changes if they affect comparability.

---

### US-040 — Review and Action Obsolete and Slow-Moving Stock
**Role:** Purchasing Manager | **FR:** FR-040

#### Happy Path
- **AC-040-H1:** Given products exceed defined aging threshold without movement, When aging report runs, Then slow movers are listed by location with last movement date.
- **AC-040-H2:** Given discontinued products have remaining stock, When report runs, Then they are flagged for clearance, transfer, or write-off action.

#### Validation Scenarios
- **AC-040-V1:** Given aging threshold varies by category, When evaluated, Then correct threshold applies per product category.
- **AC-040-V2:** Given clearance action initiated from report, When recorded, Then product status or disposition workflow begins with audit trail.

#### Error Scenarios
- **AC-040-E1:** Given movement history incomplete, When aging calculated, Then items with missing data are flagged rather than excluded silently.
- **AC-040-E2:** Given I am an unauthorized user, When I attempt bulk clearance action, Then the action is denied.

#### Edge Cases
- **AC-040-X1:** Given seasonal SKU has no movement off-season, When aging evaluated, Then seasonal exclusion rule applies if configured.
- **AC-040-X2:** Given slow mover has inbound PO open, When listed, Then report shows inbound context to avoid duplicate ordering decisions.

---

## EPIC-05: Order Fulfillment

### US-041 — Confirm Order Availability Before Commitment
**Role:** Sales Representative | **FR:** FR-041

#### Happy Path
- **AC-041-H1:** Given customer order lines and preferred fulfillment location, When I check availability, Then system confirms sufficient ATP or reports shortfall by line.
- **AC-041-H2:** Given primary location insufficient but alternate location has stock, When checked, Then alternative fulfillment location is recommended.

#### Validation Scenarios
- **AC-041-V1:** Given product out of stock but inbound PO exists, When checked, Then expected inbound date is shown with availability indication.
- **AC-041-V2:** Given large order submitted, When checked, Then all lines evaluated and aggregate fulfillment feasibility is clear.

#### Error Scenarios
- **AC-041-E1:** Given product is discontinued, When availability checked for new order, Then system indicates product not available for new commitments.
- **AC-041-E2:** Given I query an unauthorized location, When I check availability, Then access is denied or the location is excluded from results.

#### Edge Cases
- **AC-041-X1:** Given ATP changes between check and confirmation, When order confirmed immediately after, Then reservation reflects latest ATP or fails clearly if insufficient.
- **AC-041-X2:** Given multi-line order with mixed availability, When checked, Then each line shows independent availability status.

---

### US-042 — Reserve Inventory for Confirmed Orders
**Role:** Operations Director | **FR:** FR-042

#### Happy Path
- **AC-042-H1:** Given sufficient ATP at fulfillment location, When order is confirmed, Then reservation is created tied to order line and ATP decreases immediately.
- **AC-042-H2:** Given reservation succeeds, When viewed, Then order appears in fulfillment queue with reserved quantity visible.

#### Validation Scenarios
- **AC-042-V1:** Given insufficient ATP, When reservation attempted, Then reservation fails unless authorized override per policy.
- **AC-042-V2:** Given partial ATP available, When partial reservation policy applies, Then partial reservation behaves per defined business rules.

#### Error Scenarios
- **AC-042-E1:** Given order already fully reserved, When duplicate reservation attempted, Then system prevents double reservation.
- **AC-042-E2:** Given product on hold/quarantine, When reservation attempted, Then held quantity is not available for reservation.

#### Edge Cases
- **AC-042-X1:** Given two orders compete for last units, When reservations processed in sequence, Then first confirmed reservation succeeds and second fails clearly.
- **AC-042-X2:** Given backordered stock arrives, When auto-reservation policy enabled, Then backorder queue receives priority reservation per rules.

---

### US-043 — Release Inventory Reservations
**Role:** Customer Service Representative | **FR:** FR-043

#### Happy Path
- **AC-043-H1:** Given customer cancels order, When cancellation processed, Then reservation is released and ATP restored for affected lines.
- **AC-043-H2:** Given order line quantity reduced, When update processed, Then excess reservation is partially released proportionally.

#### Validation Scenarios
- **AC-043-V1:** Given order fully shipped, When shipment confirmed, Then reservation for shipped quantity is consumed and not released back to ATP.
- **AC-043-V2:** Given reservation expiry policy applies, When expiry reached, Then reservation releases with notification per policy.

#### Error Scenarios
- **AC-043-E1:** Given cancel attempted on already shipped order, When processed, Then cancellation handles only unshipped reserved quantity.
- **AC-043-E2:** Given I am an unauthorized user, When I attempt to release a reservation, Then the action is denied.

#### Edge Cases
- **AC-043-X1:** Given partial ship then cancel remainder, When processed, Then shipped portion stays fulfilled and unshipped reservation releases.
- **AC-043-X2:** Given reservation released, When another order waits in queue, Then newly available ATP is visible immediately for new reservations.

---

### US-044 — Support Pick, Pack, and Ship Workflow
**Role:** Warehouse Picker | **FR:** FR-044

#### Happy Path
- **AC-044-H1:** Given order is released to fulfillment, When pick list generated, Then product, quantity, and location appear for each line.
- **AC-044-H2:** Given pick verified and shipment confirmed, When completed, Then inventory deducts, order status updates to shipped, and shipment is logged with user and timestamp.

#### Validation Scenarios
- **AC-044-V1:** Given partial pick completed, When confirmed, Then only picked quantity ships and remainder follows partial fulfillment policy.
- **AC-044-V2:** Given pick verification fails mismatch, When submitted, Then shipment is blocked until corrected.

#### Error Scenarios
- **AC-044-E1:** Given pick attempted without reservation, When processed, Then pick blocked or flagged per policy.
- **AC-044-E2:** Given ship confirmed without pick verification, When policy requires verification, Then shipment blocked.

#### Edge Cases
- **AC-044-X1:** Given expedited order flagged, When released, Then pick list priority reflects expedite status in queue ordering.
- **AC-044-X2:** Given multi-location split order, When each location picks, Then shipments link to same order with location-specific pick confirmation.

---

### US-045 — Handle Partial Fulfillment
**Role:** Customer Service Representative | **FR:** FR-045

#### Happy Path
- **AC-045-H1:** Given full quantity unavailable at pick, When partial fulfillment processed with customer acknowledgment, Then available quantity ships and remainder placed on backorder.
- **AC-045-H2:** Given partial shipment completes, When viewed, Then order shows partially shipped with backordered quantity visible.

#### Validation Scenarios
- **AC-045-V1:** Given customer acknowledgment required, When partial ship attempted without acknowledgment, Then shipment blocked per policy.
- **AC-045-V2:** Given backorder created, When stock arrives, Then backorder line eligible for fulfillment per priority rules.

#### Error Scenarios
- **AC-045-E1:** Given zero quantity available, When partial fulfillment attempted, Then full backorder or cancel path applies with no empty shipment.
- **AC-045-E2:** Given policy prohibits partial ship for customer/order type, When attempted, Then partial fulfillment blocked with clear message.

#### Edge Cases
- **AC-045-X1:** Given multiple partial shipments over time, When order viewed, Then cumulative shipped and remaining backorder totals reconcile to original order quantity.
- **AC-045-X2:** Given partial ship reduces reservation, When ATP recalculated, Then only unshipped reservation remains or backorder holds remainder per policy.

---

### US-046 — Manage Backorders and Replenishment Priority
**Role:** Operations Director | **FR:** FR-046

#### Happy Path
- **AC-046-H1:** Given backorders exist, When stock becomes available, Then system notifies operations and offers reservation per priority queue rules.
- **AC-046-H2:** Given priority rules by order date and customer tier, When multiple backorders compete, Then highest priority receives stock first per policy.

#### Validation Scenarios
- **AC-046-V1:** Given automatic reservation enabled, When stock received, Then top-priority backorder receives reservation without manual step if policy allows.
- **AC-046-V2:** Given backorder fulfilled, When shipment completes, Then backorder line closes and queue updates.

#### Error Scenarios
- **AC-046-E1:** Given insufficient stock for all backorders, When stock arrives, Then partial allocation follows priority rules and remainder stays backordered with clear allocation record.
- **AC-046-E2:** Given backorder cancelled by customer, When processed, Then line removed from queue and no reservation retained.

#### Edge Cases
- **AC-046-X1:** Given same customer has multiple backorder lines, When stock limited, Then policy defines whether line-level or order-level priority applies consistently.
- **AC-046-X2:** Given backorder aged beyond SLA, When reviewed, Then aged backorders highlighted for customer service escalation.

---

### US-047 — Handle Outbound Fulfillment Exceptions
**Role:** Warehouse Manager | **FR:** FR-047

#### Happy Path
- **AC-047-H1:** Given picker reports stock not found, When exception recorded, Then order pauses, investigation path opens, and inventory correction or re-pick initiated.
- **AC-047-H2:** Given damaged item found during pick, When exception recorded, Then damaged quantity routes to adjustment/write-off and order line re-evaluated.

#### Validation Scenarios
- **AC-047-V1:** Given re-pick succeeds, When confirmed, Then order proceeds without duplicate inventory deduction.
- **AC-047-V2:** Given customer cancellation during exception, When processed, Then reservation released and exception closed.

#### Error Scenarios
- **AC-047-E1:** Given exception unresolved, When ship attempted, Then shipment blocked until exception resolved or cancelled.
- **AC-047-E2:** Given I am an unauthorized user, When I attempt to close an exception with inventory impact, Then the action is denied.

#### Edge Cases
- **AC-047-X1:** Given recurring pick failures on same SKU/location, When frequency threshold exceeded, Then item flagged for cycle count or inventory investigation.
- **AC-047-X2:** Given carrier failed pickup recorded as exception, When resolved, Then order status reflects delay without incorrect inventory deduction.

---

### US-048 — Support Multi-Location Split Fulfillment
**Role:** Operations Manager | **FR:** FR-048

#### Happy Path
- **AC-048-H1:** Given no single location has full ATP but network total suffices, When split fulfillment planned, Then each line assigned to fulfillment location with reservations at each site.
- **AC-048-H2:** Given split shipments occur, When customer service views order, Then unified status shows shipments from all locations under one order.

#### Validation Scenarios
- **AC-048-V1:** Given shipping costs or policy restrict splits, When plan generated, Then system respects maximum locations or split rules per policy.
- **AC-048-V2:** Given one location fails to ship its portion, When exception occurs, Then other locations' shipments still track independently on same order.

#### Error Scenarios
- **AC-048-E1:** Given network total still insufficient, When split attempted, Then order remains partially backordered or rejected with clear shortfall.
- **AC-048-E2:** Given an unauthorized location is included in a split fulfillment, When allocation is submitted, Then the location is excluded or the action is denied.

#### Edge Cases
- **AC-048-X1:** Given customer accepts split with multiple delivery dates, When scheduled, Then each shipment promise tracked separately on order lines.
- **AC-048-X2:** Given same SKU split across two locations for one line, When both ship, Then total shipped quantity matches line quantity without double-counting reservation.

---

### US-049 — Display Order Fulfillment Status
**Role:** Customer Service Representative | **FR:** FR-049

#### Happy Path
- **AC-049-H1:** Given order exists in fulfillment process, When I query status, Then I see reserved, picking, shipped, partially shipped, backordered, or cancelled state per line.
- **AC-049-H2:** Given order shipped, When I query, Then shipment date and reference appear with shipped quantities by line.

#### Validation Scenarios
- **AC-049-V1:** Given split fulfillment order, When status viewed, Then all location shipments aggregate to coherent order-level status.
- **AC-049-V2:** Given real-time status change occurs, When I refresh, Then latest status displays without stale state beyond normal refresh timing.

#### Error Scenarios
- **AC-049-E1:** Given I query with an invalid order reference, When the query runs, Then a clear not-found result is returned.
- **AC-049-E2:** Given order belongs to restricted customer segment, When unauthorized user queries, Then access denied.

#### Edge Cases
- **AC-049-X1:** Given order partially shipped and partially backordered, When displayed, Then both states visible simultaneously on respective lines.
- **AC-049-X2:** Given cancelled line coexists with shipped lines on same order, When viewed, Then line-level status differs correctly within one order.

---

### US-050 — Support Authorized Product Substitution
**Role:** Warehouse Manager | **FR:** FR-050

#### Happy Path
- **AC-050-H1:** Given primary SKU unavailable and approved substitute exists, When substitution authorized, Then substitute is reserved, picked, and shipped with substitution recorded on order.
- **AC-050-H2:** Given substitution completed, When order history viewed, Then both original ordered SKU and fulfilled substitute SKU are visible.

#### Validation Scenarios
- **AC-050-V1:** Given substitute not on approved list, When substitution attempted, Then blocked unless elevated approval obtained.
- **AC-050-V2:** Given customer acceptance required, When substitution attempted without acceptance, Then blocked per policy.

#### Error Scenarios
- **AC-050-E1:** Given substitute also unavailable, When attempted, Then substitution fails and exception path opens.
- **AC-050-E2:** Given I am an unauthorized user, When I attempt to approve a product substitution, Then the action is denied.

#### Edge Cases
- **AC-050-X1:** Given substitute has different unit of measure, When substituted, Then quantity conversion follows product master rules consistently.
- **AC-050-X2:** Given partial line substitution (some units primary, some substitute), When recorded, Then line split documented clearly on order.

---

## EPIC-06: Replenishment Planning & Stock Alerts

### US-051 — Generate Low-Stock and Out-of-Stock Alerts
**Role:** Purchasing Manager | **FR:** FR-051

#### Happy Path
- **AC-051-H1:** Given ATP falls below reorder level, When threshold evaluation runs, Then low-stock alert is created with product, location, current ATP, and threshold.
- **AC-051-H2:** Given ATP reaches zero, When evaluated, Then out-of-stock alert is created with higher urgency than low-stock per policy.

#### Validation Scenarios
- **AC-051-V1:** Given alert already open for same condition, When evaluation runs again, Then duplicate alert noise is suppressed until resolved or acknowledged per policy.
- **AC-051-V2:** Given ABC class assigned, When alert created, Then class A alerts receive higher priority indicator.

#### Error Scenarios
- **AC-051-E1:** Given no threshold defined, When evaluation runs, Then no threshold alert generated for that product-location.
- **AC-051-E2:** Given a location is deactivated, When threshold evaluation runs, Then alerts are suppressed for that location.

#### Edge Cases
- **AC-051-X1:** Given ATP restored above threshold before alert acknowledged, When evaluated, Then alert auto-closes or marks resolved per policy.
- **AC-051-X2:** Given inbound PO will arrive before stockout, When alert generated, Then alert includes expected inbound context if available.

---

### US-052 — Review and Acknowledge Stock Alerts
**Role:** Purchasing Manager | **FR:** FR-052

#### Happy Path
- **AC-052-H1:** Given active alerts exist, When I open alert queue sorted by priority, Then I see all open low-stock and out-of-stock alerts for my scope.
- **AC-052-H2:** Given I acknowledge alert with action taken (requisition, transfer), When saved, Then alert status updates and action is recorded.

#### Validation Scenarios
- **AC-052-V1:** Given I dismiss alert as false positive, When I provide documented reason, Then alert closes without replenishment action.
- **AC-052-V2:** Given critical alert unacknowledged beyond escalation window, When time elapsed, Then escalation notification sent per policy.

#### Error Scenarios
- **AC-052-E1:** Given dismiss attempted without reason, When submitted, Then dismissal blocked per policy.
- **AC-052-E2:** Given I am an unauthorized user, When I access the alert queue, Then access is denied.

#### Edge Cases
- **AC-052-X1:** Given same SKU alerts at multiple locations, When acknowledged centrally, Then each location alert handled independently unless bulk action selected.
- **AC-052-X2:** Given an alert is acknowledged but stock drops further before action completes, When threshold is re-evaluated, Then alert severity may increase or a new alert is suppressed per duplicate-alert rules.

---

### US-053 — Generate Replenishment Suggestions
**Role:** Buyer | **FR:** FR-053

#### Happy Path
- **AC-053-H1:** Given validated low-stock condition, When suggestion generated, Then recommended order quantity and rationale based on thresholds and ATP are displayed.
- **AC-053-H2:** Given open PO inbound exists, When suggestion calculated, Then suggested quantity considers expected inbound to avoid over-ordering.

#### Validation Scenarios
- **AC-053-V1:** Given network location has excess stock, When suggestion evaluated, Then transfer recommendation appears before purchase recommendation per policy.
- **AC-053-V2:** Given I modify suggested quantity, When saved, Then modified value and reason can be recorded for audit.

#### Error Scenarios
- **AC-053-E1:** Given product discontinued, When suggestion attempted, Then system blocks replenishment suggestion.
- **AC-053-E2:** Given missing threshold parameters, When suggestion runs, Then item flagged for policy setup rather than generating misleading quantity.

#### Edge Cases
- **AC-053-X1:** Given emergency stockout override, When suggestion generated, Then expedited indicator shown with shorter lead-time assumption if configured.
- **AC-053-X2:** Given seasonal product with temporary threshold, When suggestion runs, Then seasonal threshold in effect is used.

---

### US-054 — Create and Track Purchase Requisitions
**Role:** Buyer | **FR:** FR-054

#### Happy Path
- **AC-054-H1:** Given approved replenishment suggestion, When I create requisition with product, quantity, location, and justification, Then requisition enters approval workflow with trackable status.
- **AC-054-H2:** Given requisition approved, When converted to PO, Then requisition status shows converted and links to resulting PO.

#### Validation Scenarios
- **AC-054-V1:** Given requisition requires approval, When submitted, Then approver notified and requisition remains pending until decision.
- **AC-054-V2:** Given manual requisition without suggestion, When created with justification, Then it follows same approval path.

#### Error Scenarios
- **AC-054-E1:** Given requisition rejected, When decision recorded, Then status shows rejected with reason and no PO created.
- **AC-054-E2:** Given I am an unauthorized user, When I create a purchase requisition, Then the action is denied.

#### Edge Cases
- **AC-054-X1:** Given partial approval of multi-line requisition, When processed, Then approved lines proceed and rejected lines documented separately if policy allows.
- **AC-054-X2:** Given requisition open while stock replenished via transfer, When transfer completes, Then requisition may auto-cancel or flag for review per policy.

---

### US-055 — Track Inbound Supply Status
**Role:** Customer Service Representative | **FR:** FR-055 | **Epic:** EPIC-02 (Inbound Supply)

#### Happy Path
- **AC-055-H1:** Given open POs exist, When I query inbound status for a product, Then I see expected date, outstanding quantity, and received-to-date totals.
- **AC-055-H2:** Given supplier delay recorded, When I view status, Then revised ETA displays with delay notation.

#### Validation Scenarios
- **AC-055-V1:** Given partial receipt occurred, When status viewed, Then outstanding PO quantity reflects only unreceived portion.
- **AC-055-V2:** Given multiple POs for same SKU, When queried, Then all open inbound lines listed with separate dates and quantities.

#### Error Scenarios
- **AC-055-E1:** Given PO cancelled, When status queried, Then cancelled PO excluded from active inbound expectations.
- **AC-055-E2:** Given I lack authorization for purchasing data, When I view inbound supply status, Then restricted fields are hidden or access is denied.

#### Edge Cases
- **AC-055-X1:** Given ETA passed with no receipt, When viewed, Then PO flagged overdue for customer communication context.
- **AC-055-X2:** Given inbound supports backorder promise, When CS queries, Then link between backorder lines and inbound PO visible if configured.

---

### US-056 — Enforce Safety Stock Protection Rules
**Role:** Operations Director | **FR:** FR-056 | **Epic:** EPIC-01 (Policy enforcement also affects EPIC-05, EPIC-07)

#### Happy Path
- **AC-056-H1:** Given reservation or transfer would consume quantity below safety stock, When submitted without exception, Then action blocked or reduced to allowable quantity per policy.
- **AC-056-H2:** Given authorized exception with replenishment plan approved, When recorded, Then action proceeds with exception logged for audit.

#### Validation Scenarios
- **AC-056-V1:** Given available quantity above safety stock but below total demand, When evaluated, Then system shows maximum fulfillable/transferable without breaching safety stock.
- **AC-056-V2:** Given safety stock replenished after exception, When stock rises, Then normal rules resume without manual reset.

#### Error Scenarios
- **AC-056-E1:** Given an exception is attempted without an approver, When submitted, Then the action is blocked.
- **AC-056-E2:** Given safety stock undefined, When rule evaluated, Then policy defines fallback (block, warn, or ignore) consistently.

#### Edge Cases
- **AC-056-X1:** Given emergency customer order conflicts with safety stock, When override requested, Then approver sees impact on buffer and replenishment plan requirement.
- **AC-056-X2:** Given network transfer would breach safety stock at source but fix stockout at destination, When evaluated, Then policy balances transfer limits with network rules.

---

### US-057 — Support Promotional Stock Readiness Review
**Role:** Marketing Manager | **FR:** FR-057

#### Happy Path
- **AC-057-H1:** Given campaign targets defined by SKU and location, When readiness review runs, Then current plus inbound stock compared to target with gap identified.
- **AC-057-H2:** Given promotional stock ring-fenced, When campaign active, Then ring-fenced quantity excluded from general ATP for non-promotional channels per policy.

#### Validation Scenarios
- **AC-057-V1:** Given gap exists with insufficient lead time, When review runs, Then go/no-go indication shows at-risk status.
- **AC-057-V2:** Given inbound PO will close gap before launch, When review runs, Then projected readiness date reflects inbound timing.

#### Error Scenarios
- **AC-057-E1:** Given campaign target undefined, When review attempted, Then setup required before readiness calculated.
- **AC-057-E2:** Given I am an unauthorized user, When I attempt to ring-fence promotional stock, Then the action is denied.

#### Edge Cases
- **AC-057-X1:** Given campaign delayed, When dates updated, Then readiness review recalculates against new launch date.
- **AC-057-X2:** Given partial network readiness (some locations ready, others not), When displayed, Then location-level readiness breakdown shown.

---

## EPIC-07: Network Balance & Stock Transfers

### US-058 — Request Inter-Location Stock Transfers
**Role:** Regional / Store Manager | **FR:** FR-058

#### Happy Path
- **AC-058-H1:** Given destination location needs stock, When I submit transfer request with source, product, quantity, and justification, Then request enters approval workflow with trackable status.
- **AC-058-H2:** Given source has sufficient ATP above minimum, When request validated, Then request proceeds to approval; otherwise quantity limited or blocked per rules.

#### Validation Scenarios
- **AC-058-V1:** Given network view shows alternate source with more excess, When I select source, Then system may suggest better source per policy.
- **AC-058-V2:** Given mandatory justification field empty, When submitted, Then request blocked.

#### Error Scenarios
- **AC-058-E1:** Given source ATP insufficient, When request submitted, Then rejected or quantity auto-reduced with explanation.
- **AC-058-E2:** Given I am an unauthorized user, When I request an inter-location transfer, Then the action is denied.

#### Edge Cases
- **AC-058-X1:** Given urgent transfer flagged, When submitted, Then expedited approval routing applies if configured.
- **AC-058-X2:** Given same SKU requested from same source repeatedly same day, When submitted, Then duplicate request warning may appear per policy.

---

### US-059 — Approve or Reject Transfer Requests
**Role:** Operations Director | **FR:** FR-059

#### Happy Path
- **AC-059-H1:** Given pending transfer request, When I review with source and destination stock context, Then I can approve, reject, or modify quantity with rationale.
- **AC-059-H2:** Given approval granted, When saved, Then requester notified and transfer released for execution.

#### Validation Scenarios
- **AC-059-V1:** Given modified quantity approved, When saved, Then approved quantity may differ from requested with documented reason.
- **AC-059-V2:** Given rejection requires reason, When rejected without reason, Then submission blocked.

#### Error Scenarios
- **AC-059-E1:** Given source stock changed since request making approval invalid, When approver opens request, Then updated stock context shown and revalidation required.
- **AC-059-E2:** Given I am an unauthorized approver, When I attempt a transfer approval decision, Then the action is denied.

#### Edge Cases
- **AC-059-X1:** Given approver delegates during absence, When delegate approves, Then audit shows delegator and delegate per policy.
- **AC-059-X2:** Given partial approval across multi-line transfer request, When processed, Then each line status independent if policy allows line-level approval.

---

### US-060 — Execute and Record Inter-Location Transfers
**Role:** Warehouse Manager | **FR:** FR-060

#### Happy Path
- **AC-060-H1:** Given approved transfer, When source confirms dispatch, Then source on-hand decreases and in-transit quantity recorded if policy tracks in transit.
- **AC-060-H2:** Given destination confirms receipt, When received quantity matches dispatch, Then destination on-hand increases and transfer closes.

#### Validation Scenarios
- **AC-060-V1:** Given partial receipt at destination, When recorded, Then remaining quantity stays in transit or exception workflow opens per policy.
- **AC-060-V2:** Given receipt variance at destination, When documented, Then variance investigation follows count/adjustment rules.

#### Error Scenarios
- **AC-060-E1:** Given dispatch is attempted without approval, When submitted, Then the dispatch is blocked.
- **AC-060-E2:** Given receipt quantity exceeds dispatched quantity, When submitted, Then rejected or flagged for investigation.

#### Edge Cases
- **AC-060-X1:** Given transfer cancelled after dispatch but before receipt, When processed, Then inventory restored at source or exception recorded per policy.
- **AC-060-X2:** Given same transfer reference used for multiple products, When executed, Then each product line tracked independently under one transfer authorization.

---

### US-061 — Monitor In-Transit Inventory
**Role:** Operations Director | **FR:** FR-061

#### Happy Path
- **AC-061-H1:** Given transfer dispatched, When I view in-transit report, Then product, quantity, source, destination, and dispatch date appear.
- **AC-061-H2:** Given transfer received, When completed, Then in-transit quantity clears and no longer appears in in-transit views.

#### Validation Scenarios
- **AC-061-V1:** Given in-transit exceeds expected lead time, When report viewed, Then overdue transfers flagged.
- **AC-061-V2:** Given in-transit inquiry by product, When searched, Then all in-flight transfers for that SKU listed.

#### Error Scenarios
- **AC-061-E1:** Given in-transit loss recorded, When exception saved, Then quantities adjusted at source or destination per investigation outcome.
- **AC-061-E2:** Given I lack network-wide authorization, When I view in-transit inventory, Then in-transit data is restricted to my authorized locations.

#### Edge Cases
- **AC-061-X1:** Given multiple transfers same lane same day, When monitored, Then each transfer distinguishable by reference and timestamp.
- **AC-061-X2:** Given destination receives before source dispatch recorded (data error), When detected, Then reconciliation exception flagged.

---

### US-062 — Analyze and Recommend Network Rebalancing
**Role:** Operations Director | **FR:** FR-062

#### Happy Path
- **AC-062-H1:** Given network stock data exists, When rebalancing analysis runs, Then products with surplus at one location and shortage at another are identified with recommended transfer quantities.
- **AC-062-H2:** Given I accept recommendation, When converted to transfer request, Then pre-filled transfer request created respecting source minimums.

#### Validation Scenarios
- **AC-062-V1:** Given recommended transfer would breach source minimum, When displayed, Then recommendation quantity reduced to allowable maximum.
- **AC-062-V2:** Given no rebalancing opportunity exists, When analysis runs, Then report indicates balanced network for criteria selected.

#### Error Scenarios
- **AC-062-E1:** Given incomplete stock data at a location, When analysis runs, Then location flagged as excluded or data quality warning shown.
- **AC-062-E2:** Given I am an unauthorized user, When I run network rebalancing analysis, Then access is denied.

#### Edge Cases
- **AC-062-X1:** Given demand spike temporary at one location, When analysis runs, Then recommendations may be filtered by demand confidence per policy.
- **AC-062-X2:** Given multiple excess locations can supply one shortage, When recommendations generated, Then prioritization rule selects preferred source consistently.

---

### US-063 — Enforce Source Location Minimum on Transfers
**Role:** Operations Director | **FR:** FR-063

#### Happy Path
- **AC-063-H1:** Given transfer request submitted, When evaluated against source minimum threshold, Then maximum transferable quantity calculated and displayed to requester and approver.
- **AC-063-H2:** Given requested quantity exceeds allowable maximum, When submitted, Then quantity auto-reduced or request blocked with explanation.

#### Validation Scenarios
- **AC-063-V1:** Given alternate source locations available, When primary source insufficient, Then system suggests alternate source if configured.
- **AC-063-V2:** Given source minimum updated after request submitted, When revalidated at approval, Then latest minimum applied.

#### Error Scenarios
- **AC-063-E1:** Given source minimum undefined, When evaluated, Then policy fallback applies consistently (warn, block, or use zero minimum).
- **AC-063-E2:** Given override is attempted without authorization, When submitted, Then the override is blocked.

#### Edge Cases
- **AC-063-X1:** Given source ATP exactly equals minimum, When transfer requested, Then zero transferable quantity unless emergency override approved.
- **AC-063-X2:** Given concurrent transfers from same source, When second transfer evaluated, Then remaining transferable quantity reflects first approved transfer impact.

---

## EPIC-08: Returns Management

### US-064 — Authorize and Record Customer Returns
**Role:** Customer Service Representative | **FR:** FR-064

#### Happy Path
- **AC-064-H1:** Given customer return request against original order, When I issue return authorization with product, quantity, and reason, Then RA reference is generated and linked to order for warehouse use.
- **AC-064-H2:** Given RA issued, When customer ships return, Then return status shows authorized awaiting receipt.

#### Validation Scenarios
- **AC-064-V1:** Given return quantity exceeds original order line quantity, When RA attempted, Then blocked or requires override per policy.
- **AC-064-V2:** Given return window expired per policy, When RA attempted, Then blocked or requires supervisor approval.

#### Error Scenarios
- **AC-064-E1:** Given order not found, When RA attempted, Then RA blocked with clear message.
- **AC-064-E2:** Given I am an unauthorized user, When I issue a return authorization, Then the action is denied.

#### Edge Cases
- **AC-064-X1:** Given partial return on multi-quantity line, When RA issued, Then remaining returnable quantity on line tracked for future RAs.
- **AC-064-X2:** Given replacement and return paired resolution, When RA created, Then resolution type recorded for downstream processing.

---

### US-065 — Receive and Inspect Returned Goods
**Role:** Receiving Clerk | **FR:** FR-065

#### Happy Path
- **AC-065-H1:** Given return arrives with valid RA, When I receive and record quantity and condition, Then return linked to authorization and routed to inspection queue.
- **AC-065-H2:** Given inspection completed, When outcome recorded as restock, rework, or write-off, Then disposition path determined before sellable ATP changes.

#### Validation Scenarios
- **AC-065-V1:** Given received quantity differs from RA quantity, When recorded, Then variance flagged for customer service review.
- **AC-065-V2:** Given inspection fails resellable standard, When outcome saved, Then restock to ATP blocked.

#### Error Scenarios
- **AC-065-E1:** Given RA invalid or expired, When receipt attempted, Then blocked or supervisor review required per policy.
- **AC-065-E2:** Given product on RA does not match physical return, When received, Then mismatch flagged and restock blocked pending resolution.

#### Edge Cases
- **AC-065-X1:** Given return package contains items from multiple RAs, When processed, Then each RA matched separately in same receiving session.
- **AC-065-X2:** Given inspection delayed, When return in inspection queue, Then quantity remains non-sellable until inspection completes.

---

### US-066 — Restock or Write Off Returned Inventory
**Role:** Warehouse Manager | **FR:** FR-066

#### Happy Path
- **AC-066-H1:** Given inspection approves restock, When disposition confirmed, Then approved quantity added to on-hand and ATP at designated location.
- **AC-066-H2:** Given inspection rejects restock, When write-off processed, Then quantity removed with reason code linked to return record.

#### Validation Scenarios
- **AC-066-V1:** Given partial restock partial write-off, When disposition saved, Then quantities sum to inspected received quantity.
- **AC-066-V2:** Given restock requires secondary cleaning/repack workflow, When recorded, Then status reflects rework before ATP increase if policy requires.

#### Error Scenarios
- **AC-066-E1:** Given restock is attempted without completed inspection, When submitted, Then restock is blocked.
- **AC-066-E2:** Given write-off quantity exceeds received return quantity, When submitted, Then the write-off is rejected.

#### Edge Cases
- **AC-066-X1:** Given restock to different location than origin, When processed, Then inventory increases at chosen location with audit linkage to return.
- **AC-066-X2:** Given customer refund already issued before restock, When restock completes, Then return status shows complete with financial resolution noted externally per process.

---

### US-067 — Track Return Processing Status
**Role:** Customer Service Representative | **FR:** FR-067

#### Happy Path
- **AC-067-H1:** Given RA exists, When I query return status, Then I see authorized, in transit, received, inspecting, restocked, written off, or complete states.
- **AC-067-H2:** Given return completes, When queried, Then disposition outcome and inventory impact summary visible.

#### Validation Scenarios
- **AC-067-V1:** Given search by order number, When returns exist, Then all RAs for that order listed with current status.
- **AC-067-V2:** Given status changes at warehouse, When CS refreshes, Then latest status reflects warehouse progress.

#### Error Scenarios
- **AC-067-E1:** Given I search with an invalid return authorization reference, When the query runs, Then a clear not-found result is returned.
- **AC-067-E2:** Given customer data is restricted, When an unauthorized user queries return status, Then access is denied.

#### Edge Cases
- **AC-067-X1:** Given return stalled in inspection beyond SLA, When viewed, Then aged inspection flag visible for escalation.
- **AC-067-X2:** Given multiple return lines on one RA, When tracked, Then line-level status may differ within same RA.

---

## EPIC-09: Reporting, Analytics & Financial Alignment

### US-068 — Display Inventory Summary Dashboard
**Role:** Operations Director | **FR:** FR-068

#### Happy Path
- **AC-068-H1:** Given authorized access, When I open inventory dashboard, Then aggregate on-hand, reserved, ATP, low-stock count, and out-of-stock count display for my scope.
- **AC-068-H2:** Given I filter dashboard by location or category, When applied, Then metrics recalculate for selected filters only.

#### Validation Scenarios
- **AC-068-V1:** Given no stock data for filter, When displayed, Then zero or empty state shown accurately not omitted misleadingly.
- **AC-068-V2:** Given dashboard refreshed after movement, When updated, Then figures reflect current balances.

#### Error Scenarios
- **AC-068-E1:** Given I include an unauthorized location in dashboard scope, When the dashboard loads, Then unauthorized locations are excluded from metrics.
- **AC-068-E2:** Given partial data load failure, When dashboard renders, Then affected widgets show error state rather than incorrect numbers silently.

#### Edge Cases
- **AC-068-X1:** Given user has single-location scope, When dashboard opens, Then defaults to that location without exposing unauthorized network totals.
- **AC-068-X2:** Given large SKU count network, When dashboard aggregates, Then performance remains acceptable and totals mathematically correct.

---

### US-069 — Generate Stock Movement Reports
**Role:** Inventory Controller | **FR:** FR-069

#### Happy Path
- **AC-069-H1:** Given date range and optional filters selected, When movement report runs, Then receipts, transfers, adjustments, fulfillments, and returns listed with quantity, user, timestamp, and reference.
- **AC-069-H2:** Given export requested, When generated, Then export matches report filters and authorized scope.

#### Validation Scenarios
- **AC-069-V1:** Given filter by transaction type only, When run, Then only selected types appear.
- **AC-069-V2:** Given filter by product and location together, When run, Then intersection of criteria applied correctly.

#### Error Scenarios
- **AC-069-E1:** Given date range invalid (end before start), When run, Then validation error shown.
- **AC-069-E2:** Given the report date range includes unauthorized locations, When the movement report runs, Then unauthorized location data is excluded.

#### Edge Cases
- **AC-069-X1:** Given high-volume day, When report runs, Then all transactions included without truncation unless pagination explicitly indicated.
- **AC-069-X2:** Given transfer reported, When viewed, Then both source decrease and destination increase traceable via reference linkage.

---

### US-070 — Generate Stockout and Overstock Reports
**Role:** Purchasing Manager | **FR:** FR-070

#### Happy Path
- **AC-070-H1:** Given reporting period selected, When stockout report runs, Then products/locations at zero ATP listed with stockout duration where available.
- **AC-070-H2:** Given overstock criteria defined, When overstock report runs, Then products exceeding threshold relative to movement listed for action.

#### Validation Scenarios
- **AC-070-V1:** Given sort by severity or ABC class, When displayed, Then sort order correct and stable.
- **AC-070-V2:** Given recommended action indicators configured, When shown, Then suggest transfer vs purchase contextually where rules support.

#### Error Scenarios
- **AC-070-E1:** Given no stockouts in period, When report runs, Then empty result with clear message.
- **AC-070-E2:** Given overstock threshold is undefined for a category, When the overstock report runs, Then items are flagged using the default threshold or excluded per policy consistently.

#### Edge Cases
- **AC-070-X1:** Given intermittent stockout (in and out same day), When duration calculated, Then policy defines minimum duration threshold for inclusion.
- **AC-070-X2:** Given overstock at one location and stockout at another for same SKU, When network report viewed, Then rebalancing opportunity highlighted if configured.

---

### US-071 — Generate Inventory Accuracy and Variance Reports
**Role:** Inventory Controller | **FR:** FR-071

#### Happy Path
- **AC-071-H1:** Given count results exist for period, When accuracy report runs, Then accuracy rate calculated as SKUs with zero variance divided by SKUs counted.
- **AC-071-H2:** Given variance summary requested, When run, Then variances grouped by location, category, and counter with amounts and directions.

#### Validation Scenarios
- **AC-071-V1:** Given trend over multiple periods, When displayed, Then accuracy trend line or table shows period-over-period change.
- **AC-071-V2:** Given recurring variance SKUs configured, When run, Then repeat SKUs highlighted.

#### Error Scenarios
- **AC-071-E1:** Given no counts in period, When report runs, Then no-data state not zero-percent accuracy misleadingly.
- **AC-071-E2:** Given unauthorized location counts exist in the period, When the accuracy report runs, Then those locations are excluded from the accuracy rollup.

#### Edge Cases
- **AC-071-X1:** Given full count and cycle counts mixed in period, When accuracy calculated, Then policy defines weighting or separate sections for each count type.
- **AC-071-X2:** Given immaterial variances excluded per tolerance, When accuracy calculated, Then calculation documents exclusion rule applied.

---

### US-072 — Provide Location Performance Snapshots
**Role:** COO | **FR:** FR-072

#### Happy Path
- **AC-072-H1:** Given network locations active, When performance snapshot viewed, Then each location shows accuracy, stockout frequency, shrinkage, and fulfillment metrics side by side.
- **AC-072-H2:** Given location below network average, When displayed, Then visual indicator highlights underperformance for review.

#### Validation Scenarios
- **AC-072-V1:** Given filter by region, When applied, Then only locations in region compared.
- **AC-072-V2:** Given drill-down to location detail, When selected, Then underlying metric components accessible from snapshot.

#### Error Scenarios
- **AC-072-E1:** Given location missing metric data, When displayed, Then gap flagged rather than showing misleading zero benchmark.
- **AC-072-E2:** Given I view an executive snapshot with restricted locations in scope, When the snapshot renders, Then unauthorized locations are excluded.

#### Edge Cases
- **AC-072-X1:** Given new location with short history, When included, Then metrics note insufficient history or use partial period per policy.
- **AC-072-X2:** Given metric definitions change mid-period, When snapshot spans period, Then footnote indicates comparability limitation if applicable.

---

### US-073 — Report Inventory Performance KPIs
**Role:** CEO | **FR:** FR-073

#### Happy Path
- **AC-073-H1:** Given KPI period selected, When executive KPI view opened, Then fill rate, turnover, days of supply, and record accuracy display with values and trends.
- **AC-073-H2:** Given targets configured, When KPIs rendered, Then actual vs target comparison shown for each metric.

#### Validation Scenarios
- **AC-073-V1:** Given role-specific executive view, When opened, Then only authorized KPI set visible per role configuration.
- **AC-073-V2:** Given KPI threshold breached, When viewed, Then breach indicator highlights metric requiring attention.

#### Error Scenarios
- **AC-073-E1:** Given insufficient data for KPI calculation, When rendered, Then KPI marked unavailable with reason not fabricated value.
- **AC-073-E2:** Given I am an unauthorized user, When I access executive KPIs, Then access is denied.

#### Edge Cases
- **AC-073-X1:** Given partial month-to-date view, When KPIs calculated, Then annualized projections distinguished from full-period metrics if both shown.
- **AC-073-X2:** Given fill rate definition has organizational variant, When displayed, Then definition reference available to avoid misinterpretation.

---

### US-074 — Support Basic Replenishment Reporting
**Role:** Buyer | **FR:** FR-074

#### Happy Path
- **AC-074-H1:** Given replenishment report run, When displayed, Then items below threshold, active alerts, open requisitions, and expected inbound listed by product and location.
- **AC-074-H2:** Given export for buyer workflow, When exported, Then data supports daily purchasing review without supplementary spreadsheets.

#### Validation Scenarios
- **AC-074-V1:** Given filter to urgent items only, When applied, Then only out-of-stock and critical low-stock appear per policy.
- **AC-074-V2:** Given alert age shown, When reviewed, Then oldest unactioned alerts sort to top if configured.

#### Error Scenarios
- **AC-074-E1:** Given no items below threshold, When report runs, Then clear empty state message.
- **AC-074-E2:** Given I lack authorization for purchasing data, When I view the replenishment report, Then restricted data is hidden or access is denied.

#### Edge Cases
- **AC-074-X1:** Given same SKU on report from alerts and open requisition, When displayed, Then duplication handled clearly (linked or deduplicated per policy).
- **AC-074-X2:** Given inbound PO covers threshold breach imminently, When report shows, Then inbound context displayed on same line.

---

### US-075 — Support Inventory Valuation Summary Views
**Role:** Finance Manager | **FR:** FR-075

#### Happy Path
- **AC-075-H1:** Given unit costs configured, When valuation summary run, Then extended value by product and location and total inventory value calculated using agreed costing method.
- **AC-075-H2:** Given finance reconciliation view opened, When displayed, Then operational quantity summary available alongside valuation for comparison workflow.

#### Validation Scenarios
- **AC-075-V1:** Given product missing unit cost, When valuation calculated, Then item flagged in exception list rather than valued at zero silently without flag.
- **AC-075-V2:** Given period-end snapshot requested, When generated, Then snapshot timestamp and scope recorded for audit.

#### Error Scenarios
- **AC-075-E1:** Given costing method not defined organizationally, When valuation attempted, Then blocked pending configuration.
- **AC-075-E2:** Given I am an unauthorized user, When I access inventory valuation views, Then access is denied.

#### Edge Cases
- **AC-075-X1:** Given large write-off same day as snapshot, When both occur, Then snapshot timing rules define inclusion consistently.
- **AC-075-X2:** Given multi-location rollup to enterprise total, When calculated, Then sum of location values equals enterprise total without rounding discrepancy beyond defined tolerance.

---

## EPIC-10: Operational Notifications & Awareness

### US-076 — Deliver Low-Stock and Out-of-Stock Notifications
**Role:** Purchasing Manager | **FR:** FR-076

#### Happy Path
- **AC-076-H1:** Given low-stock or out-of-stock alert created, When notification rules apply, Then designated recipients receive notification with product, location, ATP, and threshold.
- **AC-076-H2:** Given I acknowledge alert from notification, When processed, Then acknowledgment recorded and escalation timer reset if applicable.

#### Validation Scenarios
- **AC-076-V1:** Given priority product (class A), When notified, Then notification indicates higher priority than standard alerts.
- **AC-076-V2:** Given notification preferences by role, When alert fires, Then only configured channels/recipients used.

#### Error Scenarios
- **AC-076-E1:** Given recipient unavailable in notification list, When alert fires, Then fallback recipient or escalation path applies per policy.
- **AC-076-E2:** Given an alert condition resolves before notification is sent, When the notification job runs, Then duplicate or stale notifications are suppressed if still in queue.

#### Edge Cases
- **AC-076-X1:** Given burst of alerts same SKU multiple locations, When delivered, Then notifications grouped or summarized per policy to reduce noise.
- **AC-076-X2:** Given critical alert unacknowledged, When escalation triggers, Then secondary recipients notified per escalation ladder.

---

### US-077 — Deliver Pending Approval Notifications
**Role:** Operations Director | **FR:** FR-077

#### Happy Path
- **AC-077-H1:** Given adjustment, variance, transfer, or requisition submitted for my approval, When submission completes, Then I receive notification with summary and link to review.
- **AC-077-H2:** Given I approve or reject, When decision saved, Then requester receives notification of outcome.

#### Validation Scenarios
- **AC-077-V1:** Given approval pending beyond escalation threshold, When time elapsed, Then reminder notification sent.
- **AC-077-V2:** Given multiple pending items, When notification digest enabled, Then items may batch per user preference policy.

#### Error Scenarios
- **AC-077-E1:** Given approver role misassigned, When notification sent, Then also flagged to administrator for role correction if undeliverable.
- **AC-077-E2:** Given item already approved by delegate, When original approver opens notification, Then status shows completed to prevent duplicate action.

#### Edge Cases
- **AC-077-X1:** Given high-value item requires COO approval, When threshold exceeded, Then notification routes to correct hierarchy level automatically.
- **AC-077-X2:** Given request withdrawn before approval, When approver opens notification, Then item shows cancelled status.

---

### US-078 — Deliver Transfer and Fulfillment Exception Alerts
**Role:** Warehouse Manager | **FR:** FR-078

#### Happy Path
- **AC-078-H1:** Given pick exception or transfer delay occurs, When exception recorded, Then warehouse manager and relevant operations roles receive targeted alert with type and affected reference.
- **AC-078-H2:** Given exception resolved, When closed, Then alert status updated and resolution visible in alert history.

#### Validation Scenarios
- **AC-078-V1:** Given customer-impacting fulfillment exception, When created, Then customer service also notified if policy requires.
- **AC-078-V2:** Given in-transit overdue, When threshold passed, Then transfer exception alert generated.

#### Error Scenarios
- **AC-078-E1:** Given an alert cannot be routed to any configured owner, When the exception is recorded, Then the fallback operations queue receives the alert per policy.
- **AC-078-E2:** Given duplicate exception records for same event, When detected, Then user warned to prevent duplicate processing.

#### Edge Cases
- **AC-078-X1:** Given after-hours exception, When created, Then on-call routing rules apply if configured.
- **AC-078-X2:** Given exception reopens after prior closure, When recorded, Then alert history shows reopen with reason.

---

### US-079 — Deliver Inbound Supply Delay Notifications
**Role:** Purchasing Manager | **FR:** FR-079

#### Happy Path
- **AC-079-H1:** Given open PO expected date passed without receipt, When delay detected, Then purchasing manager and affected location manager notified with product and revised ETA if known.
- **AC-079-H2:** Given supplier reports revised ETA, When updated, Then delay notification updated or follow-up sent if material change.

#### Validation Scenarios
- **AC-079-V1:** Given delay affects active backorders, When notification sent, Then backorder linkage included for CS visibility if configured.
- **AC-079-V2:** Given partial receipt occurred (not full delay), When evaluated, Then notification distinguishes partial vs full delay per policy.

#### Error Scenarios
- **AC-079-E1:** Given PO cancelled after delay notification, When status changes, Then follow-up cancellation notice sent or alert auto-closed.
- **AC-079-E2:** Given false delay (receipt logged late), When reconciled, Then alert cleared with correction note.

#### Edge Cases
- **AC-079-X1:** Given supplier delay affects multiple PO lines, When notified, Then grouped notification lists all affected lines.
- **AC-079-X2:** Given chronic delay same supplier, When pattern detected, Then supplier highlighted on performance context in notification if configured.

---

### US-080 — Deliver Campaign and Launch Readiness Alerts
**Role:** Marketing Manager | **FR:** FR-080

#### Happy Path
- **AC-080-H1:** Given campaign milestone date approaches and stock below target, When readiness check runs, Then marketing, sales, and operations receive readiness gap alert.
- **AC-080-H2:** Given readiness restored before launch, When reassessed, Then all-clear or updated status notification sent if previously at risk.

#### Validation Scenarios
- **AC-080-V1:** Given multiple campaigns concurrent, When alerts fire, Then each campaign identified distinctly in notification.
- **AC-080-V2:** Given go/no-go decision point reached, When readiness still at risk, Then escalation severity increases per milestone policy.

#### Error Scenarios
- **AC-080-E1:** Given campaign targets incomplete, When milestone check runs, Then setup alert sent instead of misleading readiness score.
- **AC-080-E2:** Given notification recipients are misconfigured, When a readiness alert is triggered, Then the IMS Administrator is alerted to the configuration gap.

#### Edge Cases
- **AC-080-X1:** Given inbound PO closes gap after alert sent, When reassessed, Then follow-up notification indicates risk reduced with new projected readiness date.
- **AC-080-X2:** Given launch delayed, When campaign dates shift, Then alert schedule realigns to new milestone dates.

---

## EPIC-11: Security, Access & Accountability

### US-081 — Enforce Role-Based Access Control
**Role:** IMS Administrator | **FR:** FR-081

#### Happy Path
- **AC-081-H1:** Given user authenticated with warehouse operator role, When attempting permitted transaction (e.g., receipt), Then action succeeds; when attempting configuration, Then denied.
- **AC-081-H2:** Given role permissions updated, When user next accesses system, Then new permissions apply to subsequent actions.

#### Validation Scenarios
- **AC-081-V1:** Given user has multiple roles, When permissions overlap, Then effective permission follows defined precedence rule consistently.
- **AC-081-V2:** Given read-only finance viewer role, When attempting transaction, Then all write actions denied.

#### Error Scenarios
- **AC-081-E1:** Given a deactivated user account, When login is attempted, Then access is denied.
- **AC-081-E2:** Given session expires, When action attempted, Then re-authentication required before continuing.

#### Edge Cases
- **AC-081-X1:** Given temporary elevated permission granted for cover period, When expiry reached, Then elevation auto-revokes.
- **AC-081-X2:** Given role renamed but permissions unchanged, When users assigned, Then behavior identical with updated role label only.

---

### US-082 — Restrict Access by Location
**Role:** IMS Administrator | **FR:** FR-082

#### Happy Path
- **AC-082-H1:** Given user assigned to Location A only, When viewing inventory or transacting, Then only Location A data accessible and Location B hidden or denied.
- **AC-082-H2:** Given network-wide role assigned, When user accesses system, Then all authorized network locations visible per role scope.

#### Validation Scenarios
- **AC-082-V1:** Given user assigned multiple locations, When acting, Then can switch or aggregate only within assigned set.
- **AC-082-V2:** Given location assignment changed, When user logs in after change, Then new scope applies immediately.

#### Error Scenarios
- **AC-082-E1:** Given I attempt a transaction at an unauthorized location, When the transaction is submitted, Then it is blocked and the attempt is logged per policy.
- **AC-082-E2:** Given user with no location assignment, When accessing operational functions, Then blocked pending administrator assignment.

#### Edge Cases
- **AC-082-X1:** Given regional manager oversees child locations, When hierarchy role used, Then access includes all child locations automatically per hierarchy assignment.
- **AC-082-X2:** Given report spans authorized and unauthorized locations, When run, Then report silently excludes unauthorized or prompts scope correction per policy.

---

### US-083 — Log User Activity for Accountability
**Role:** Internal Auditor | **FR:** FR-083

#### Happy Path
- **AC-083-H1:** Given user performs inventory transaction, When saved, Then activity log records user, action type, timestamp, and affected entity.
- **AC-083-H2:** Given administrator queries activity log by user and date range, When run, Then complete activity list returned for authorized audit scope.

#### Validation Scenarios
- **AC-083-V1:** Given login and logout events, When occur, Then authentication events logged separately from business transactions.
- **AC-083-V2:** Given configuration change made, When saved, Then before/after or change description captured in activity log per policy.

#### Error Scenarios
- **AC-083-E1:** Given I am an unauthorized auditor, When I query restricted user activity logs, Then access is denied.
- **AC-083-E2:** Given logging subsystem unavailable, When transaction attempted, Then transaction blocked or queued per fail-safe policy — never silent unlogged write if policy requires logging.

#### Edge Cases
- **AC-083-X1:** Given delegated approval performed, When logged, Then both delegator context and acting user captured.
- **AC-083-X2:** Given bulk import performed, When completed, Then bulk action logged as single event with summary count and initiator.

---

### US-084 — Enforce Segregation of Duties
**Role:** IMS Administrator | **FR:** FR-084

#### Happy Path
- **AC-084-H1:** Given user performed cycle count, When same user attempts to approve resulting adjustment, Then self-approval blocked and routed to independent approver.
- **AC-084-H2:** Given role assignment creates segregation conflict, When administrator saves roles, Then conflict warning displayed before save completes.

#### Validation Scenarios
- **AC-084-V1:** Given small team authorized exception documented, When self-approval attempted with valid exception code, Then allowed with enhanced audit flag per policy.
- **AC-084-V2:** Given a receiver attempts to approve their own discrepancy resolution beyond the limit, When approval is submitted, Then the action is blocked per the segregation matrix.

#### Error Scenarios
- **AC-084-E1:** Given segregation rule undefined for action pair, When attempted, Then conservative block or administrator alert per default policy.
- **AC-084-E2:** Given circumvention attempted via alternate account, When detected by same person credentials policy, Then blocked if identity linkage rules exist organizationally.

#### Edge Cases
- **AC-084-X1:** Given approver on leave with formal delegate, When delegate approves, Then segregation satisfied via delegate identity not original counter.
- **AC-084-X2:** Given emergency break-glass override, When used, Then enhanced logging and post-event review notification triggered.

---

### US-085 — Manage User Accounts and Role Assignments
**Role:** IMS Administrator | **FR:** FR-085

#### Happy Path
- **AC-085-H1:** Given new employee onboarded, When I create account with role and location scope, Then user can authenticate and access permitted functions only.
- **AC-085-H2:** Given employee departs, When I deactivate account, Then user cannot authenticate and active sessions terminated per policy.

#### Validation Scenarios
- **AC-085-V1:** Given role change submitted, When saved, Then account change history records prior and new roles with administrator attribution.
- **AC-085-V2:** Given periodic access review export requested, When generated, Then all active users with roles and locations listed.

#### Error Scenarios
- **AC-085-E1:** Given duplicate username attempted, When saved, Then creation blocked.
- **AC-085-E2:** Given an administrator attempts to remove their own last admin access without a replacement, When the change is submitted, Then it is blocked to prevent system lockout.

#### Edge Cases
- **AC-085-X1:** Given user rehired, When account reactivated, Then new effective dates applied and prior history retained.
- **AC-085-X2:** Given bulk role update for location reorganization, When applied, Then all affected users updated consistently with batch audit record.

---

## EPIC-12: Governance, Audit & Compliance

### US-086 — Maintain Complete Audit Trail of Inventory Changes
**Role:** Internal Auditor | **FR:** FR-086

#### Happy Path
- **AC-086-H1:** Given any inventory balance change occurs, When transaction completes, Then audit entry records before quantity, after quantity, transaction type, reason code, user, and timestamp.
- **AC-086-H2:** Given auditor queries audit trail by product and date range, When run, Then complete immutable history returned in chronological order.

#### Validation Scenarios
- **AC-086-V1:** Given audit entry created, When any user attempts modification or deletion, Then operation blocked preserving immutability.
- **AC-086-V2:** Given export for external audit requested, When generated, Then export matches query criteria and includes required fields per audit policy.

#### Error Scenarios
- **AC-086-E1:** Given I am an unauthorized user, When I query the full audit trail, Then access is restricted to authorized audit roles.
- **AC-086-E2:** Given audit logging fails during a transaction, When the transaction is processed, Then handling follows the fail-safe policy (block or queue) without silent unaudited change if required by policy.

#### Edge Cases
- **AC-086-X1:** Given high-volume period, When audit trail queried, Then completeness verified — no gaps in sequence per location/product if sequence tracking used.
- **AC-086-X2:** Given corrective entry references original, When audit viewed, Then linkage between original and correction visible.

---

### US-087 — Support Audit and Control Review Queries
**Role:** Internal Auditor | **FR:** FR-087

#### Happy Path
- **AC-087-H1:** Given internal audit cycle, When I run control review queries for adjustment approvals, count variances, and segregation compliance, Then structured results returned for sample period and locations.
- **AC-087-H2:** Given evidence package export requested, When generated, Then package includes transactions, approvals, and supporting audit trail for selected scope.

#### Validation Scenarios
- **AC-087-V1:** Given external auditor read-only role, When accessing audit views, Then write actions unavailable but query and export permitted.
- **AC-087-V2:** Given sample size parameter defined, When query runs, Then random or stratified sample follows audit methodology settings.

#### Error Scenarios
- **AC-087-E1:** Given a query scope exceeds my authorized locations, When the audit query runs, Then results are truncated to authorized scope with notice.
- **AC-087-E2:** Given incomplete approval records in sample, When queried, Then exceptions flagged as control deficiency findings.

#### Edge Cases
- **AC-087-X1:** Given audit spans fiscal year boundary, When queried, Then period filter handles year-end cutover consistently.
- **AC-087-X2:** Given remediation verified after prior finding, When follow-up query runs, Then closed finding status trackable if remediation module referenced externally.

---

### US-088 — Detect and Record Control Policy Breaches
**Role:** Internal Auditor | **FR:** FR-088

#### Happy Path
- **AC-088-H1:** Given user performs action breaching policy (e.g., ad-hoc receipt without PO without approval), When action occurs, Then breach or authorized exception logged with user, action, policy reference, and approver if excepted.
- **AC-088-H2:** Given governance review report run, When generated, Then breach frequency by location and type displayed for management review.

#### Validation Scenarios
- **AC-088-V1:** Given authorized exception properly approved, When logged, Then recorded as exception not breach with approver attribution.
- **AC-088-V2:** Given repeat breach same location, When trend analyzed, Then pattern highlighted in governance report.

#### Error Scenarios
- **AC-088-E1:** Given breach detection rule misconfigured, When administrator reviews config, Then validation prevents contradictory rules if possible.
- **AC-088-E2:** Given I am an unauthorized user, When I attempt to delete a control breach record, Then the action is blocked to preserve record integrity.

#### Edge Cases
- **AC-088-X1:** Given policy changes redefine breach, When historical breaches viewed, Then historical records retain evaluation against policy in effect at time of event.
- **AC-088-X2:** Given near-threshold action not quite breach, When evaluated, Then no false breach logged — only true violations recorded.

---

### US-089 — Support Financial Inventory Reconciliation
**Role:** Finance Manager | **FR:** FR-089 | **Epic:** EPIC-09 (Financial Alignment)

#### Happy Path
- **AC-089-H1:** Given month-end close initiated, When reconciliation view opened, Then period-end quantity summary by location and category available for finance comparison.
- **AC-089-H2:** Given adjustment and write-off log exported for period, When generated, Then finance receives complete list supporting GL substantiation workflow externally.

#### Validation Scenarios
- **AC-089-V1:** Given operational vs finance comparison view used, When variance entered on finance side externally, Then operational side provides quantity and movement substantiation references.
- **AC-089-V2:** Given reconciliation snapshot saved, When retrieved later, Then point-in-time quantities match snapshot values not current balances.

#### Error Scenarios
- **AC-089-E1:** Given the period is not closed, When I attempt an early reconciliation snapshot, Then the snapshot is labeled preliminary if policy distinguishes preliminary vs final snapshots.
- **AC-089-E2:** Given I am an unauthorized finance user, When I access reconciliation views, Then access is denied.

#### Edge Cases
- **AC-089-X1:** Given significant write-off same day as close, When reconciliation run, Then write-off included in period if timestamp within close window per policy.
- **AC-089-X2:** Given location deactivated mid-period, When reconciled, Then disposition transactions through deactivation visible in period log.

---

### US-090 — Support Initial Data Import for Product and Stock Setup
**Role:** Inventory Controller | **FR:** FR-090 | **Epic:** EPIC-01 (Go-Live)

#### Happy Path
- **AC-090-H1:** Given structured import file with product master data, When validated and approved, Then products created or updated per file with error report for any rejected rows.
- **AC-090-H2:** Given opening balance import for location, When validated and approved, Then opening balances established and location eligible for activation upon approval completion.

#### Validation Scenarios
- **AC-090-V1:** Given import contains invalid SKU references for balances, When validated, Then those rows rejected with line-level error detail before any partial load if policy requires all-or-nothing.
- **AC-090-V2:** Given import requires approver sign-off, When submitted, Then data not active until approver confirms.

#### Error Scenarios
- **AC-090-E1:** Given malformed file or missing required columns, When upload attempted, Then import rejected with format error message.
- **AC-090-E2:** Given I am an unauthorized user, When I attempt a data import, Then the action is denied.

#### Edge Cases
- **AC-090-X1:** Given duplicate SKUs within same import file, When validated, Then duplicates flagged before processing.
- **AC-090-X2:** Given import partially succeeds with row errors, When complete, Then successful rows active and failed rows listed for correction and re-import without duplicating successful rows.

---

## Document Summary

This document defines reviewed acceptance criteria for all **90 user stories** (US-001 – US-090), totaling **360 individual Given/When/Then criteria** (2 per category × 4 categories × 90 stories).

| Review Item | Status |
|-------------|--------|
| Happy Path per story | ✅ Complete (2 each) |
| Validation Scenarios per story | ✅ Complete (2 each) |
| Error Scenarios per story | ✅ Complete (2 each) |
| Edge Cases per story | ✅ Complete (2 each) |
| Given/When/Then format | ✅ Normalized in PO review |
| Epic organization | ✅ EPIC-01 through EPIC-12 |

Each criterion is testable from a business perspective and maps 1:1 to its user story and underlying functional requirement.

---

## Traceability Summary

| User Story | Functional Requirement | Criteria IDs |
|------------|------------------------|--------------|
| US-001 – US-090 | FR-001 – FR-090 | AC-{001-090}-{H,V,E,X}n |

---

*End of Acceptance Criteria Document*
