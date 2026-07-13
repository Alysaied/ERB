# Implementation Checklist — F-21: Returns Management

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-21 |
| **Feature Name** | Returns Management |
| **Document Type** | Technical Lead Implementation Checklist |
| **Feature dependencies** | F-10, F-11, F-05, F-27 |
| **Default status** | Not Started |
| **Task count** | 6 |

---

## Checklist

| Task ID | Feature | Task description | Layer | Priority | Status | Dependencies |
|---------|---------|------------------|-------|----------|--------|--------------|
| `CHK-21-DB-01` | F-21 | Create returns schema: RAs, customer_returns, dispositions | Database | P2 | Not Started | F-10 |
| `CHK-21-BE-01` | F-21 | CustomerReturnCase aggregate + services | Backend | P2 | Not Started | CHK-21-DB-01 |
| `CHK-21-BE-02` | F-21 | API-124–131 (prefer 128 over 076 — C-04) | Backend | P2 | Not Started | CHK-21-BE-01 |
| `CHK-21-FE-01` | F-21 | UI-042 RA management, UI-043 inspection/disposition | Frontend | P2 | Not Started | CHK-21-BE-02 |
| `CHK-21-TE-01` | F-21 | FAC-21-H1–H5/V2/P1 | Testing | P2 | Not Started | CHK-21-FE-01 |
| `CHK-21-DO-01` | F-21 | Returns disposition decision tree | Documentation | P2 | Not Started | CHK-21-BE-02 |

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
| P0 | MVP critical / blocking | 0 |
| P1 | MVP important | 0 |
| P2 | Phase 2 Should Have | 6 |
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

- Implementation plan: `implmention/plans/` (F-21)
- Acceptance criteria: `implmention/acceptance-criteria/F-21-Acceptance-Criteria.md`
- Sprint plan: `implmention/IMS-Sprint-Plan.md`

*Technical Lead checklist — F-21*
