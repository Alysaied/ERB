# Implementation Checklist — F-22: Inventory Reporting & Dashboards

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-22 |
| **Feature Name** | Inventory Reporting & Dashboards |
| **Document Type** | Technical Lead Implementation Checklist |
| **Feature dependencies** | F-04 |
| **Default status** | Not Started |
| **Task count** | 7 |

---

## Checklist

| Task ID | Feature | Task description | Layer | Priority | Status | Dependencies |
|---------|---------|------------------|-------|----------|--------|--------------|
| `CHK-22-DB-01` | F-22 | Reporting views/indexes for dashboard & movements | Database | P0 | Not Started | F-04, F-05 |
| `CHK-22-BE-01` | F-22 | DashboardService + OperationalReportService | Backend | P0 | Not Started | CHK-22-DB-01 |
| `CHK-22-BE-02` | F-22 | API-150–152, 155 (+ 167/168 as available) | Backend | P0 | Not Started | CHK-22-BE-01 |
| `CHK-22-FE-01` | F-22 | Replace UI-002 mocks with live widgets | Frontend | P0 | Not Started | CHK-22-BE-02 |
| `CHK-22-FE-02` | F-22 | UI-044 operational reports + filters/export | Frontend | P0 | Not Started | CHK-22-BE-02 |
| `CHK-22-TE-01` | F-22 | FAC-22-H1–H4/P2 | Testing | P0 | Not Started | CHK-22-FE-01 |
| `CHK-22-DO-01` | F-22 | Dashboard widget catalog for roles | Documentation | P1 | Not Started | CHK-22-FE-01 |

## Layer summary

| Layer | Count |
|-------|-------|
| Database | 1 |
| Backend | 2 |
| Frontend | 2 |
| Testing | 1 |
| Documentation | 1 |

## Priority summary

| Priority | Meaning | Count |
|----------|---------|-------|
| P0 | MVP critical / blocking | 6 |
| P1 | MVP important | 1 |
| P2 | Phase 2 Should Have | 0 |
| P3 | Phase 3 / deferred | 0 |

## Status legend

| Status | Meaning |
|--------|---------|
| Not Started | Not begun |
| In Progress | Actively being worked |
| Blocked | Waiting on dependency |
| Done | Complete and verified |
| Won't Do | Explicitly waived by PO |

## Related artifacts

- Implementation plan: `implmention/plans/` (F-22)
- Acceptance criteria: `implmention/acceptance-criteria/F-22-Acceptance-Criteria.md`
- Sprint plan: `implmention/IMS-Sprint-Plan.md`

*Technical Lead checklist — F-22*
