# Implementation Checklist — F-30: System Go-Live & Initial Data Setup

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-30 |
| **Feature Name** | System Go-Live & Initial Data Setup |
| **Document Type** | Technical Lead Implementation Checklist |
| **Feature dependencies** | F-01, F-02, F-27 |
| **Default status** | Not Started |
| **Task count** | 8 |

---

## Checklist

| Task ID | Feature | Task description | Layer | Priority | Status | Dependencies |
|---------|---------|------------------|-------|----------|--------|--------------|
| `CHK-30-DB-01` | F-30 | Optional import_batches / import_errors staging tables | Database | P0 | Not Started | F-01 |
| `CHK-30-BE-01` | F-30 | ProductImportService validate/upsert + OpeningBalanceService | Backend | P0 | Not Started | CHK-30-DB-01, F-01, F-04 |
| `CHK-30-BE-02` | F-30 | API-010, 032, 017 activation gate | Backend | P0 | Not Started | CHK-30-BE-01, F-02 |
| `CHK-30-BE-03` | F-30 | SoD: importer ≠ opening approver when required | Backend | P0 | Not Started | F-28, CHK-30-BE-02 |
| `CHK-30-FE-01` | F-30 | UI-006 import wizard: upload/validate/review/approve/activate | Frontend | P0 | Not Started | CHK-30-BE-02 |
| `CHK-30-TE-01` | F-30 | FAC-30-H1–H3/V1/V4/P3 | Testing | P0 | Not Started | CHK-30-FE-01 |
| `CHK-30-TE-02` | F-30 | Production cutover dry-run checklist execution | Testing | P0 | Not Started | CHK-30-FE-01 |
| `CHK-30-DO-01` | F-30 | Go-live runbook + rollback plan | Documentation | P0 | Not Started | CHK-30-BE-02 |

## Layer summary

| Layer | Count |
|-------|-------|
| Database | 1 |
| Backend | 3 |
| Frontend | 1 |
| Testing | 2 |
| Documentation | 1 |

## Priority summary

| Priority | Meaning | Count |
|----------|---------|-------|
| P0 | MVP critical / blocking | 8 |
| P1 | MVP important | 0 |
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

- Implementation plan: `implmention/plans/` (F-30)
- Acceptance criteria: `implmention/acceptance-criteria/F-30-Acceptance-Criteria.md`
- Sprint plan: `implmention/IMS-Sprint-Plan.md`

*Technical Lead checklist — F-30*
