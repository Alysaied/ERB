# Implementation Checklist — F-20: Low-Stock Alerting & Replenishment

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-20 |
| **Feature Name** | Low-Stock Alerting & Replenishment |
| **Document Type** | Technical Lead Implementation Checklist |
| **Feature dependencies** | F-03, F-04, F-27 |
| **Default status** | Not Started |
| **Task count** | 8 |

---

## Checklist

| Task ID | Feature | Task description | Layer | Priority | Status | Dependencies |
|---------|---------|------------------|-------|----------|--------|--------------|
| `CHK-20-DB-01` | F-20 | Create audit.operational_alerts; purchase_requisitions (Phase 2) | Database | P0 | Not Started | F-03 |
| `CHK-20-BE-01` | F-20 | StockAlertService threshold breach detection + dedupe | Backend | P0 | Not Started | CHK-20-DB-01, F-04 |
| `CHK-20-BE-02` | F-20 | API-158–160 alerts/recommendations (MVP) | Backend | P0 | Not Started | CHK-20-BE-01 |
| `CHK-20-BE-03` | F-20 | Requisition APIs 054–058 + list gap C-03 (Phase 2) | Backend | P2 | Not Started | CHK-20-DB-01, F-07 |
| `CHK-20-FE-01` | F-20 | UI-036 alert review + ack | Frontend | P0 | Not Started | CHK-20-BE-02 |
| `CHK-20-FE-02` | F-20 | UI-037 / UI-013 requisition flows (Phase 2) | Frontend | P2 | Not Started | CHK-20-BE-03 |
| `CHK-20-TE-01` | F-20 | FAC-20-H1/H2/H3; requisition FAC-20-H4 Phase 2 | Testing | P0 | Not Started | CHK-20-FE-01 |
| `CHK-20-DO-01` | F-20 | Alert severity & ack policy | Documentation | P1 | Not Started | CHK-20-BE-01 |

## Layer summary

| Layer | Count |
|-------|-------|
| Database | 1 |
| Backend | 3 |
| Frontend | 2 |
| Testing | 1 |
| Documentation | 1 |

## Priority summary

| Priority | Meaning | Count |
|----------|---------|-------|
| P0 | MVP critical / blocking | 5 |
| P1 | MVP important | 1 |
| P2 | Phase 2 Should Have | 2 |
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

- Implementation plan: `implmention/plans/` (F-20)
- Acceptance criteria: `implmention/acceptance-criteria/F-20-Acceptance-Criteria.md`
- Sprint plan: `implmention/IMS-Sprint-Plan.md`

*Technical Lead checklist — F-20*
