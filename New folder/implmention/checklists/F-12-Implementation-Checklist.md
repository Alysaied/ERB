# Implementation Checklist — F-12: Partial Fulfillment & Backorder Management

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-12 |
| **Feature Name** | Partial Fulfillment & Backorder Management |
| **Document Type** | Technical Lead Implementation Checklist |
| **Feature dependencies** | F-10, F-11 |
| **Default status** | Not Started |
| **Task count** | 8 |

---

## Checklist

| Task ID | Feature | Task description | Layer | Priority | Status | Dependencies |
|---------|---------|------------------|-------|----------|--------|--------------|
| `CHK-12-DB-01` | F-12 | Create `fulfillment.backorders` with priority/status | Database | P0 | Not Started | F-11 |
| `CHK-12-BE-01` | F-12 | PartialFulfillmentService + BackorderService | Backend | P0 | Not Started | CHK-12-DB-01 |
| `CHK-12-BE-02` | F-12 | API-093–095, 164 (priority Phase 2) | Backend | P0 | Not Started | CHK-12-BE-01 |
| `CHK-12-BE-03` | F-12 | Require customer ack for partial ship | Backend | P0 | Not Started | CHK-12-BE-02 |
| `CHK-12-FE-01` | F-12 | UI-032 partial ship wizard + backorder board | Frontend | P0 | Not Started | CHK-12-BE-02 |
| `CHK-12-FE-02` | F-12 | Backorder priority UI (Phase 2) | Frontend | P2 | Not Started | CHK-12-FE-01 |
| `CHK-12-TE-01` | F-12 | FAC-12-H1/V1; priority sequencing Phase 2 | Testing | P0 | Not Started | CHK-12-FE-01 |
| `CHK-12-DO-01` | F-12 | Partial/backorder customer comms notes | Documentation | P2 | Not Started | CHK-12-BE-02 |

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
| P0 | MVP critical / blocking | 6 |
| P1 | MVP important | 0 |
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

- Implementation plan: `implmention/plans/` (F-12)
- Acceptance criteria: `implmention/acceptance-criteria/F-12-Acceptance-Criteria.md`
- Sprint plan: `implmention/IMS-Sprint-Plan.md`

*Technical Lead checklist — F-12*
