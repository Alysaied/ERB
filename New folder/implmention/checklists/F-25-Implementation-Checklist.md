# Implementation Checklist — F-25: Promotional & Launch Stock Readiness

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-25 |
| **Feature Name** | Promotional & Launch Stock Readiness |
| **Document Type** | Technical Lead Implementation Checklist |
| **Feature dependencies** | F-04, F-10, F-27 |
| **Default status** | Not Started |
| **Task count** | 5 |

---

## Checklist

| Task ID | Feature | Task description | Layer | Priority | Status | Dependencies |
|---------|---------|------------------|-------|----------|--------|--------------|
| `CHK-25-DB-01` | F-25 | commercial.promotional_stock_allocations* | Database | P3 | Not Started | F-04 |
| `CHK-25-BE-01` | F-25 | CampaignAllocationService + API-132–139, 048, 169 | Backend | P3 | Not Started | CHK-25-DB-01 |
| `CHK-25-FE-01` | F-25 | UI-046 promotional readiness | Frontend | P3 | Not Started | CHK-25-BE-01 |
| `CHK-25-TE-01` | F-25 | FAC-25-H1/H2/E2 ring-fence isolation | Testing | P3 | Not Started | CHK-25-FE-01 |
| `CHK-25-DO-01` | F-25 | Campaign readiness checklist | Documentation | P3 | Not Started | CHK-25-FE-01 |

## Layer summary

| Layer | Count |
|-------|-------|
| Database | 1 |
| Backend | 1 |
| Frontend | 1 |
| Testing | 1 |
| Documentation | 1 |

## Priority summary

| Priority | Meaning | Count |
|----------|---------|-------|
| P0 | MVP critical / blocking | 0 |
| P1 | MVP important | 0 |
| P2 | Phase 2 Should Have | 0 |
| P3 | Phase 3 / deferred | 5 |

## Status legend

| Status | Meaning |
|--------|---------|
| Not Started | Not begun |
| In Progress | Actively being worked |
| Blocked | Waiting on dependency |
| Done | Complete and verified |
| Won't Do | Explicitly waived by PO |

## Related artifacts

- Implementation plan: `implmention/plans/` (F-25)
- Acceptance criteria: `implmention/acceptance-criteria/F-25-Acceptance-Criteria.md`
- Sprint plan: `implmention/IMS-Sprint-Plan.md`

*Technical Lead checklist — F-25*
