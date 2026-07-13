# Feature Acceptance Criteria — Index

| Attribute | Detail |
|-----------|--------|
| **Document ID** | IMPL-AC-000 |
| **Perspective** | Product Owner & QA Lead |
| **Date** | July 11, 2026 |
| **Format** | Given / When / Then |
| **Features covered** | 30 (F-01–F-30) |
| **Total criteria** | 429 |

## Categories (every feature)

| Category | Prefix | Purpose |
|----------|--------|---------|
| Happy | H | Successful business outcomes |
| Validation | V | Required fields, formats, business-rule checks before commit |
| Error | E | Failures, conflicts, unavailable dependencies |
| Permission | P | AuthN/AuthZ, RBAC, location scope, SoD |
| Edge | X | Boundaries, concurrency, phase splits, unusual valid cases |

## Criteria by feature

| ID | Feature | Stories | # AC | Document |
|----|---------|---------|------|----------|
| F-01 | Product Catalog Management | US-001, US-002, US-003, US-004 | 22 | [F-01-Acceptance-Criteria.md](./F-01-Acceptance-Criteria.md) |
| F-02 | Location & Network Setup | US-005, US-006, US-007, US-010 | 18 | [F-02-Acceptance-Criteria.md](./F-02-Acceptance-Criteria.md) |
| F-03 | Stock Policy & Product Classification | US-008, US-009, US-012, US-056 | 18 | [F-03-Acceptance-Criteria.md](./F-03-Acceptance-Criteria.md) |
| F-04 | Inventory Visibility & Search | US-023, US-024, US-025, US-026, US-027, US-028 | 17 | [F-04-Acceptance-Criteria.md](./F-04-Acceptance-Criteria.md) |
| F-05 | Goods Receiving & Verification | US-015, US-016, US-017, US-019, US-020, US-029 | 19 | [F-05-Acceptance-Criteria.md](./F-05-Acceptance-Criteria.md) |
| F-06 | Put-Away Management | US-018 | 13 | [F-06-Acceptance-Criteria.md](./F-06-Acceptance-Criteria.md) |
| F-07 | Purchase Order & Inbound Supply Management | US-013, US-014, US-021, US-022, US-055, US-079 | 18 | [F-07-Acceptance-Criteria.md](./F-07-Acceptance-Criteria.md) |
| F-08 | Inter-Location Stock Transfers | US-058, US-059, US-060, US-061, US-063 | 18 | [F-08-Acceptance-Criteria.md](./F-08-Acceptance-Criteria.md) |
| F-09 | Network Stock Rebalancing | US-062 | 10 | [F-09-Acceptance-Criteria.md](./F-09-Acceptance-Criteria.md) |
| F-10 | Order Availability & Reservation | US-041, US-042, US-043, US-048 | 16 | [F-10-Acceptance-Criteria.md](./F-10-Acceptance-Criteria.md) |
| F-11 | Pick, Pack & Ship Fulfillment | US-044, US-049 | 15 | [F-11-Acceptance-Criteria.md](./F-11-Acceptance-Criteria.md) |
| F-12 | Partial Fulfillment & Backorder Management | US-045, US-046 | 12 | [F-12-Acceptance-Criteria.md](./F-12-Acceptance-Criteria.md) |
| F-13 | Fulfillment Exception Handling | US-047, US-050, US-078 | 12 | [F-13-Acceptance-Criteria.md](./F-13-Acceptance-Criteria.md) |
| F-14 | Cycle Counting | US-030, US-031, US-071 | 13 | [F-14-Acceptance-Criteria.md](./F-14-Acceptance-Criteria.md) |
| F-15 | Full Physical Inventory Count | US-032 | 12 | [F-15-Acceptance-Criteria.md](./F-15-Acceptance-Criteria.md) |
| F-16 | Count Variance Investigation & Approval | US-033, US-034, US-037 | 12 | [F-16-Acceptance-Criteria.md](./F-16-Acceptance-Criteria.md) |
| F-17 | Stock Adjustments & Write-Offs | US-011, US-035, US-036, US-077 | 16 | [F-17-Acceptance-Criteria.md](./F-17-Acceptance-Criteria.md) |
| F-18 | Quarantine & Hold Stock Management | US-038 | 11 | [F-18-Acceptance-Criteria.md](./F-18-Acceptance-Criteria.md) |
| F-19 | Shrinkage & Obsolescence Analysis | US-039, US-040 | 10 | [F-19-Acceptance-Criteria.md](./F-19-Acceptance-Criteria.md) |
| F-20 | Low-Stock Alerting & Replenishment | US-051, US-052, US-053, US-054, US-074 | 17 | [F-20-Acceptance-Criteria.md](./F-20-Acceptance-Criteria.md) |
| F-21 | Returns Management | US-064, US-065, US-066, US-067 | 16 | [F-21-Acceptance-Criteria.md](./F-21-Acceptance-Criteria.md) |
| F-22 | Inventory Reporting & Dashboards | US-068, US-069, US-070, US-072, US-074 | 14 | [F-22-Acceptance-Criteria.md](./F-22-Acceptance-Criteria.md) |
| F-23 | Inventory Performance KPIs | US-073 | 9 | [F-23-Acceptance-Criteria.md](./F-23-Acceptance-Criteria.md) |
| F-24 | Financial Inventory Reconciliation | US-075, US-089 | 12 | [F-24-Acceptance-Criteria.md](./F-24-Acceptance-Criteria.md) |
| F-25 | Promotional & Launch Stock Readiness | US-057, US-080 | 12 | [F-25-Acceptance-Criteria.md](./F-25-Acceptance-Criteria.md) |
| F-26 | Operational Notifications & Alerts | US-076, US-077, US-078, US-079, US-080 | 13 | [F-26-Acceptance-Criteria.md](./F-26-Acceptance-Criteria.md) |
| F-27 | User Access & Role Management | US-081, US-082, US-085 | 16 | [F-27-Acceptance-Criteria.md](./F-27-Acceptance-Criteria.md) |
| F-28 | Operational Accountability & Controls | US-083, US-084 | 10 | [F-28-Acceptance-Criteria.md](./F-28-Acceptance-Criteria.md) |
| F-29 | Audit Trail & Compliance | US-086, US-087, US-088 | 12 | [F-29-Acceptance-Criteria.md](./F-29-Acceptance-Criteria.md) |
| F-30 | System Go-Live & Initial Data Setup | US-090 | 16 | [F-30-Acceptance-Criteria.md](./F-30-Acceptance-Criteria.md) |

## How QA should use these

1. Map each `FAC-*` to test cases (API + UI + UAT scripts).
2. Prefer automating **V**, **E**, and **P** at API layer; **H** and key **P/X** in UI/E2E.
3. Story-level detail remains in `project_businsse/acceptance-criteria-reviewed.md` — feature AC is the **release gate** view.
4. Sign off feature DoD checklist at bottom of each file before marking F-xx Done.

## Related documents

- [IMS-Implementation-Features.md](../IMS-Implementation-Features.md)
- [IMS-Feature-Dependency-Map.md](../IMS-Feature-Dependency-Map.md)
- [plans/README.md](../plans/README.md)
