# IMS Implementation Checklists — Master Index

| Attribute | Detail |
|-----------|--------|
| **Document ID** | IMPL-CHK-000 |
| **Perspective** | Technical Lead |
| **Date** | July 11, 2026 |
| **Features** | 30 |
| **Total tasks** | 288 |
| **Default status** | Not Started |

## Layers

| Layer | Description |
|-------|-------------|
| Database | Schemas, tables, constraints, Flyway migrations |
| Backend | Domain, repos, DTOs, services, controllers, security |
| Frontend | Routes, pages, components, services, forms, state |
| Testing | Unit, API, UI/E2E, permission tests |
| Documentation | OpenAPI, runbooks, UAT notes |

## Priority

| Code | Meaning |
|------|---------|
| P0 | MVP critical / blocking |
| P1 | MVP important |
| P2 | Phase 2 Should Have |
| P3 | Phase 3 / deferred |

## Checklists by feature

| Feature | Name | Tasks | File |
|---------|------|-------|------|
| F-01 | Product Catalog Management | 26 | [F-01-Implementation-Checklist.md](./F-01-Implementation-Checklist.md) |
| F-02 | Location & Network Setup | 20 | [F-02-Implementation-Checklist.md](./F-02-Implementation-Checklist.md) |
| F-03 | Stock Policy & Product Classification | 17 | [F-03-Implementation-Checklist.md](./F-03-Implementation-Checklist.md) |
| F-04 | Inventory Visibility & Search | 16 | [F-04-Implementation-Checklist.md](./F-04-Implementation-Checklist.md) |
| F-05 | Goods Receiving & Verification | 18 | [F-05-Implementation-Checklist.md](./F-05-Implementation-Checklist.md) |
| F-06 | Put-Away Management | 10 | [F-06-Implementation-Checklist.md](./F-06-Implementation-Checklist.md) |
| F-07 | Purchase Order & Inbound Supply Management | 12 | [F-07-Implementation-Checklist.md](./F-07-Implementation-Checklist.md) |
| F-08 | Inter-Location Stock Transfers | 12 | [F-08-Implementation-Checklist.md](./F-08-Implementation-Checklist.md) |
| F-09 | Network Stock Rebalancing | 6 | [F-09-Implementation-Checklist.md](./F-09-Implementation-Checklist.md) |
| F-10 | Order Availability & Reservation | 11 | [F-10-Implementation-Checklist.md](./F-10-Implementation-Checklist.md) |
| F-11 | Pick, Pack & Ship Fulfillment | 9 | [F-11-Implementation-Checklist.md](./F-11-Implementation-Checklist.md) |
| F-12 | Partial Fulfillment & Backorder Management | 8 | [F-12-Implementation-Checklist.md](./F-12-Implementation-Checklist.md) |
| F-13 | Fulfillment Exception Handling | 6 | [F-13-Implementation-Checklist.md](./F-13-Implementation-Checklist.md) |
| F-14 | Cycle Counting | 7 | [F-14-Implementation-Checklist.md](./F-14-Implementation-Checklist.md) |
| F-15 | Full Physical Inventory Count | 6 | [F-15-Implementation-Checklist.md](./F-15-Implementation-Checklist.md) |
| F-16 | Count Variance Investigation & Approval | 6 | [F-16-Implementation-Checklist.md](./F-16-Implementation-Checklist.md) |
| F-17 | Stock Adjustments & Write-Offs | 7 | [F-17-Implementation-Checklist.md](./F-17-Implementation-Checklist.md) |
| F-18 | Quarantine & Hold Stock Management | 6 | [F-18-Implementation-Checklist.md](./F-18-Implementation-Checklist.md) |
| F-19 | Shrinkage & Obsolescence Analysis | 5 | [F-19-Implementation-Checklist.md](./F-19-Implementation-Checklist.md) |
| F-20 | Low-Stock Alerting & Replenishment | 8 | [F-20-Implementation-Checklist.md](./F-20-Implementation-Checklist.md) |
| F-21 | Returns Management | 6 | [F-21-Implementation-Checklist.md](./F-21-Implementation-Checklist.md) |
| F-22 | Inventory Reporting & Dashboards | 7 | [F-22-Implementation-Checklist.md](./F-22-Implementation-Checklist.md) |
| F-23 | Inventory Performance KPIs | 5 | [F-23-Implementation-Checklist.md](./F-23-Implementation-Checklist.md) |
| F-24 | Financial Inventory Reconciliation | 5 | [F-24-Implementation-Checklist.md](./F-24-Implementation-Checklist.md) |
| F-25 | Promotional & Launch Stock Readiness | 5 | [F-25-Implementation-Checklist.md](./F-25-Implementation-Checklist.md) |
| F-26 | Operational Notifications & Alerts | 7 | [F-26-Implementation-Checklist.md](./F-26-Implementation-Checklist.md) |
| F-27 | User Access & Role Management | 13 | [F-27-Implementation-Checklist.md](./F-27-Implementation-Checklist.md) |
| F-28 | Operational Accountability & Controls | 7 | [F-28-Implementation-Checklist.md](./F-28-Implementation-Checklist.md) |
| F-29 | Audit Trail & Compliance | 9 | [F-29-Implementation-Checklist.md](./F-29-Implementation-Checklist.md) |
| F-30 | System Go-Live & Initial Data Setup | 8 | [F-30-Implementation-Checklist.md](./F-30-Implementation-Checklist.md) |

## How to use

1. Open the feature checklist for the current sprint feature.
2. Work **Database → Backend → Frontend → Testing → Documentation** unless blocked.
3. Update **Status** in the feature file as work progresses.
4. Do not mark Done until related FAC-* acceptance criteria pass.

## Related

- [IMS-Sprint-Plan.md](../IMS-Sprint-Plan.md)
- [IMS-Feature-Dependency-Map.md](../IMS-Feature-Dependency-Map.md)
- [plans/README.md](../plans/README.md)
