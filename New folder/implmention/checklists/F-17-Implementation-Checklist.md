# Implementation Checklist — F-17: Stock Adjustments & Write-Offs

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-17 |
| **Feature Name** | Stock Adjustments & Write-Offs |
| **Document Type** | Technical Lead Implementation Checklist |
| **Feature dependencies** | F-03, F-04, F-28, F-27 |
| **Default status** | Not Started |
| **Task count** | 7 |

---

## Checklist

| Task ID | Feature | Task description | Layer | Priority | Status | Dependencies |
|---------|---------|------------------|-------|----------|--------|--------------|
| `CHK-17-DB-01` | F-17 | Create accuracy.stock_adjustments + inventory_write_offs | Database | P0 | Not Started | F-03 |
| `CHK-17-BE-01` | F-17 | StockAdjustmentService + WriteOffService + reason validation | Backend | P0 | Not Started | CHK-17-DB-01, F-28 |
| `CHK-17-BE-02` | F-17 | API-120–122 (+ reason APIs); movement on post | Backend | P0 | Not Started | CHK-17-BE-01, F-29 |
| `CHK-17-BE-03` | F-17 | Permissions ADJUST_SUBMIT/APPROVE, WRITE_OFF_AUTHORIZE | Backend | P0 | Not Started | F-27, CHK-17-BE-02 |
| `CHK-17-FE-01` | F-17 | UI-026 adjustments, UI-027 write-offs | Frontend | P0 | Not Started | CHK-17-BE-02 |
| `CHK-17-TE-01` | F-17 | FAC-17-H2/V1/E1/P2 | Testing | P0 | Not Started | CHK-17-FE-01 |
| `CHK-17-DO-01` | F-17 | Reason code usage guide | Documentation | P1 | Not Started | F-03 |

## Layer summary

| Layer | Count |
|-------|-------|
| Database | 1 |
| Backend | 3 |
| Frontend | 1 |
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

- Implementation plan: `implmention/plans/` (F-17)
- Acceptance criteria: `implmention/acceptance-criteria/F-17-Acceptance-Criteria.md`
- Sprint plan: `implmention/IMS-Sprint-Plan.md`

*Technical Lead checklist — F-17*
