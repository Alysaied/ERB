# Implementation Checklist — F-16: Count Variance Investigation & Approval

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-16 |
| **Feature Name** | Count Variance Investigation & Approval |
| **Document Type** | Technical Lead Implementation Checklist |
| **Feature dependencies** | F-14, F-15, F-03, F-28 |
| **Default status** | Not Started |
| **Task count** | 6 |

---

## Checklist

| Task ID | Feature | Task description | Layer | Priority | Status | Dependencies |
|---------|---------|------------------|-------|----------|--------|--------------|
| `CHK-16-DB-01` | F-16 | Create count_variances + adjustment case tables | Database | P0 | Not Started | F-14, F-15 |
| `CHK-16-BE-01` | F-16 | VarianceInvestigationService + approval routing/thresholds | Backend | P0 | Not Started | CHK-16-DB-01, F-03, F-28 |
| `CHK-16-BE-02` | F-16 | API-116–119, 123, 029, 031 | Backend | P0 | Not Started | CHK-16-BE-01 |
| `CHK-16-FE-01` | F-16 | UI-025 investigation + approve/reject | Frontend | P0 | Not Started | CHK-16-BE-02 |
| `CHK-16-TE-01` | F-16 | FAC-16-E1 SoD self-approve blocked; H2 approve posts adjust | Testing | P0 | Not Started | CHK-16-FE-01 |
| `CHK-16-DO-01` | F-16 | Variance approval matrix by threshold | Documentation | P1 | Not Started | CHK-16-BE-01 |

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

- Implementation plan: `implmention/plans/` (F-16)
- Acceptance criteria: `implmention/acceptance-criteria/F-16-Acceptance-Criteria.md`
- Sprint plan: `implmention/IMS-Sprint-Plan.md`

*Technical Lead checklist — F-16*
