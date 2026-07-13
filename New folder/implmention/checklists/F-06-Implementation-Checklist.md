# Implementation Checklist — F-06: Put-Away Management

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-06 |
| **Feature Name** | Put-Away Management |
| **Document Type** | Technical Lead Implementation Checklist |
| **Feature dependencies** | F-05, F-02, F-27 |
| **Default status** | Not Started |
| **Task count** | 10 |

---

## Checklist

| Task ID | Feature | Task description | Layer | Priority | Status | Dependencies |
|---------|---------|------------------|-------|----------|--------|--------------|
| `CHK-06-DB-01` | F-06 | Create `inbound.put_aways` with FK to goods_receipt and storage_position | Database | P0 | Not Started | F-05, F-02 |
| `CHK-06-DB-02` | F-06 | Constraints: position belongs to receipt location | Database | P0 | Not Started | CHK-06-DB-01 |
| `CHK-06-BE-01` | F-06 | PutAwayService confirming storage and updating availability | Backend | P0 | Not Started | CHK-06-DB-02, F-04 |
| `CHK-06-BE-02` | F-06 | API-073, API-074 (+ storage position APIs) | Backend | P0 | Not Started | CHK-06-BE-01 |
| `CHK-06-BE-03` | F-06 | Permission PUT_AWAY_EXECUTE + location scope | Backend | P0 | Not Started | F-27, CHK-06-BE-02 |
| `CHK-06-FE-01` | F-06 | PutAwayApiService + facade | Frontend | P0 | Not Started | CHK-06-BE-02 |
| `CHK-06-FE-02` | F-06 | UI-017 pending queue + position picker + confirm | Frontend | P0 | Not Started | CHK-06-FE-01 |
| `CHK-06-TE-01` | F-06 | FAC-06-H2/X1 ATP only after put-away | Testing | P0 | Not Started | CHK-06-FE-02 |
| `CHK-06-TE-02` | F-06 | Invalid position / already put away errors | Testing | P1 | Not Started | CHK-06-BE-02 |
| `CHK-06-DO-01` | F-06 | Received vs available state diagram for UAT | Documentation | P2 | Not Started | CHK-06-BE-01 |

## Layer summary

| Layer | Count |
|-------|-------|
| Database | 2 |
| Backend | 3 |
| Frontend | 2 |
| Testing | 2 |
| Documentation | 1 |

## Priority summary

| Priority | Meaning | Count |
|----------|---------|-------|
| P0 | MVP critical / blocking | 8 |
| P1 | MVP important | 1 |
| P2 | Phase 2 Should Have | 1 |
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

- Implementation plan: `implmention/plans/` (F-06)
- Acceptance criteria: `implmention/acceptance-criteria/F-06-Acceptance-Criteria.md`
- Sprint plan: `implmention/IMS-Sprint-Plan.md`

*Technical Lead checklist — F-06*
