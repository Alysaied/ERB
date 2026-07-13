# Acceptance Criteria — F-26: Operational Notifications & Alerts

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-26 |
| **Feature Name** | Operational Notifications & Alerts |
| **Document Type** | Feature Acceptance Criteria (PO + QA Lead) |
| **Related user stories** | US-076, US-077, US-078, US-079, US-080 |
| **Primary roles** | All operational roles (role-filtered) |
| **Format** | Given / When / Then |
| **Criteria count** | 13 (H4 / V1 / E2 / P3 / X3) |

---

## Purpose

Define testable acceptance criteria for **F-26** covering happy paths, validation, errors, permissions, and edge cases. Use for UAT, QA test design, and Definition of Done.

**ID legend:** `FAC-{nn}-{H|V|E|P|X}{n}` — Feature Acceptance Criteria; H=Happy, V=Validation, E=Error, P=Permission, X=Edge.

---

### 1. Happy Scenarios

#### FAC-26-H1
- **Given** low-stock event occurs
- **When** I open notification center / badge
- **Then** alert visible to purchasing roles

#### FAC-26-H2
- **Given** approval pending
- **When** approver is notified
- **Then** deep link opens approval queue

#### FAC-26-H3
- **Given** I acknowledge alert
- **When** unread count decreases
- **Then** ack user/time stored

#### FAC-26-H4
- **Given** transfer/fulfillment/inbound delay events (Phase 2)
- **When** respective roles notified
- **Then** alerts categorized correctly

### 2. Validation Scenarios

#### FAC-26-V1
- **Given** ack without required rationale on dismiss
- **When** I dismiss
- **Then** blocked

### 3. Error Scenarios

#### FAC-26-E1
- **Given** ack alert not in my feed
- **When** I ack by ID
- **Then** 403/404

#### FAC-26-E2
- **Given** producer fails to write alert
- **When** business txn still commits
- **Then** outbox retries alert without losing source txn

### 4. Permission Scenarios

#### FAC-26-P1
- **Given** warehouse user
- **When** I open feed
- **Then** does not see finance-only alerts

#### FAC-26-P2
- **Given** unauthenticated
- **When** I call alert API
- **Then** 401

#### FAC-26-P3
- **Given** I lack ALERT_VIEW
- **When** I open center
- **Then** denied

### 5. Edge Cases

#### FAC-26-X1
- **Given** burst of alerts
- **When** feed
- **Then** pagination/grouping prevents overload

#### FAC-26-X2
- **Given** already acked
- **When** I ack again
- **Then** idempotent success

#### FAC-26-X3
- **Given** campaign alerts deferred
- **When** feature flag off
- **Then** US-080 not delivered


## Traceability

| Link | Reference |
|------|-----------|
| User stories | US-076, US-077, US-078, US-079, US-080 |
| Story-level AC | `project_businsse/acceptance-criteria-reviewed.md` |
| Implementation plan | `implmention/plans/F-26-*.md` |
| Feature catalog | `implmention/IMS-Implementation-Features.md` |

## Feature DoD (QA gate)

- [ ] All Happy criteria passed in UAT or automated suite
- [ ] Validation + Error criteria covered by API and/or UI tests
- [ ] Permission criteria verified with at least two roles (allowed + denied)
- [ ] Edge cases reviewed; deferred edges explicitly waived with PO sign-off
- [ ] No open Sev-1/Sev-2 defects for this feature

---

*Product Owner & QA Lead — F-26*
