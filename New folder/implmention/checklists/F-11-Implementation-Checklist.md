# Implementation Checklist — F-11: Pick, Pack & Ship Fulfillment

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-11 |
| **Feature Name** | Pick, Pack & Ship Fulfillment |
| **Document Type** | Technical Lead Implementation Checklist |
| **Feature dependencies** | F-10, F-27 |
| **Default status** | Not Started |
| **Task count** | 9 |

---

## Checklist

| Task ID | Feature | Task description | Layer | Priority | Status | Dependencies |
|---------|---------|------------------|-------|----------|--------|--------------|
| `CHK-11-DB-01` | F-11 | Create fulfillment_executions, pick_lines, shipments, shipment_lines | Database | P0 | Not Started | F-10 |
| `CHK-11-BE-01` | F-11 | PickPackShipService + lot selection helpers | Backend | P0 | Not Started | CHK-11-DB-01 |
| `CHK-11-BE-02` | F-11 | API-088–092, 082–083, 097 (+ C-01 location queue) | Backend | P0 | Not Started | CHK-11-BE-01 |
| `CHK-11-BE-03` | F-11 | Deduct on-hand only on ship; FULFILL_PICK/SHIP permissions | Backend | P0 | Not Started | CHK-11-BE-02, F-27 |
| `CHK-11-FE-01` | F-11 | PickPackShipFacade + UI-031 workbench | Frontend | P0 | Not Started | CHK-11-BE-02 |
| `CHK-11-FE-02` | F-11 | UI-034 order status | Frontend | P0 | Not Started | CHK-11-BE-02 |
| `CHK-11-TE-01` | F-11 | FAC-11-H1–H3; ship-before-pack blocked | Testing | P0 | Not Started | CHK-11-FE-01 |
| `CHK-11-TE-02` | F-11 | Golden path reserve→ship balances | Testing | P0 | Not Started | CHK-11-FE-01, F-10 |
| `CHK-11-DO-01` | F-11 | Document C-01 workaround until queue API exists | Documentation | P1 | Not Started | CHK-11-BE-02 |

## Layer summary

| Layer | Count |
|-------|-------|
| Database | 1 |
| Backend | 3 |
| Frontend | 2 |
| Testing | 2 |
| Documentation | 1 |

## Priority summary

| Priority | Meaning | Count |
|----------|---------|-------|
| P0 | MVP critical / blocking | 8 |
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

- Implementation plan: `implmention/plans/` (F-11)
- Acceptance criteria: `implmention/acceptance-criteria/F-11-Acceptance-Criteria.md`
- Sprint plan: `implmention/IMS-Sprint-Plan.md`

*Technical Lead checklist — F-11*
