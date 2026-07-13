# Implementation Checklist — F-15: Full Physical Inventory Count

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-15 |
| **Feature Name** | Full Physical Inventory Count |
| **Document Type** | Technical Lead Implementation Checklist |
| **Feature dependencies** | F-02, F-04, F-27 |
| **Default status** | Not Started |
| **Task count** | 6 |

---

## Checklist

| Task ID | Feature | Task description | Layer | Priority | Status | Dependencies |
|---------|---------|------------------|-------|----------|--------|--------------|
| `CHK-15-DB-01` | F-15 | Create `accuracy.physical_inventory_counts`; freeze flag on locations | Database | P0 | Not Started | F-02 |
| `CHK-15-BE-01` | F-15 | PhysicalInventoryCountService + LocationFreezeService | Backend | P0 | Not Started | CHK-15-DB-01 |
| `CHK-15-BE-02` | F-15 | API-020, 112–115; block mutators when frozen | Backend | P0 | Not Started | CHK-15-BE-01 |
| `CHK-15-FE-01` | F-15 | UI-024 initiate/progress/certify + freeze banner | Frontend | P0 | Not Started | CHK-15-BE-02 |
| `CHK-15-TE-01` | F-15 | FAC-15-H1/E1 receive blocked while frozen | Testing | P0 | Not Started | CHK-15-FE-01, F-05 |
| `CHK-15-DO-01` | F-15 | Physical count freeze checklist | Documentation | P1 | Not Started | CHK-15-BE-02 |

## Layer summary

| Layer | Count |
|-------|-------|
| Database | 1 |
| Backend | 2 |
| Frontend | 1 |
| Testing | 1 |
| Documentation | 1 |

## Priority summary

| Priority | Meaning | Count |
|----------|---------|-------|
| P0 | MVP critical / blocking | 5 |
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

- Implementation plan: `implmention/plans/` (F-15)
- Acceptance criteria: `implmention/acceptance-criteria/F-15-Acceptance-Criteria.md`
- Sprint plan: `implmention/IMS-Sprint-Plan.md`

*Technical Lead checklist — F-15*
