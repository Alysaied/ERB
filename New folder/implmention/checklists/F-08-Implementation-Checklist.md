# Implementation Checklist — F-08: Inter-Location Stock Transfers

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-08 |
| **Feature Name** | Inter-Location Stock Transfers |
| **Document Type** | Technical Lead Implementation Checklist |
| **Feature dependencies** | F-02, F-03, F-04, F-27, F-28 |
| **Default status** | Not Started |
| **Task count** | 12 |

---

## Checklist

| Task ID | Feature | Task description | Layer | Priority | Status | Dependencies |
|---------|---------|------------------|-------|----------|--------|--------------|
| `CHK-08-DB-01` | F-08 | Create `transfer` schema: requests, transfers, lines, in_transit_stock | Database | P0 | Not Started | F-02 |
| `CHK-08-DB-02` | F-08 | Constraints source!=dest; status CHECKs; optimistic locking | Database | P0 | Not Started | CHK-08-DB-01 |
| `CHK-08-BE-01` | F-08 | StockTransfer aggregate + capacity evaluation vs stock policy | Backend | P0 | Not Started | CHK-08-DB-02, F-03, F-04 |
| `CHK-08-BE-02` | F-08 | TransferService request/approve/reject/dispatch/receive | Backend | P0 | Not Started | CHK-08-BE-01, F-28 |
| `CHK-08-BE-03` | F-08 | API-098–107, API-042 | Backend | P0 | Not Started | CHK-08-BE-02 |
| `CHK-08-BE-04` | F-08 | SoD on approve; TRANSFER_* permissions | Backend | P0 | Not Started | F-28, CHK-08-BE-03 |
| `CHK-08-FE-01` | F-08 | TransferApiService + TransferFacade | Frontend | P0 | Not Started | CHK-08-BE-03 |
| `CHK-08-FE-02` | F-08 | UI-038 request, UI-039 approval, UI-040 execution | Frontend | P0 | Not Started | CHK-08-FE-01 |
| `CHK-08-FE-03` | F-08 | In-transit monitor polish (US-061 Phase 2) | Frontend | P2 | Not Started | CHK-08-FE-02 |
| `CHK-08-TE-01` | F-08 | FAC-08-H1–H3/V2/E2 golden path + SoD | Testing | P0 | Not Started | CHK-08-FE-02 |
| `CHK-08-TE-02` | F-08 | Source minimum blocks over-transfer | Testing | P0 | Not Started | CHK-08-BE-03 |
| `CHK-08-DO-01` | F-08 | Transfer state machine for UAT | Documentation | P1 | Not Started | CHK-08-BE-02 |

## Layer summary

| Layer | Count |
|-------|-------|
| Database | 2 |
| Backend | 4 |
| Frontend | 3 |
| Testing | 2 |
| Documentation | 1 |

## Priority summary

| Priority | Meaning | Count |
|----------|---------|-------|
| P0 | MVP critical / blocking | 10 |
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

- Implementation plan: `implmention/plans/` (F-08)
- Acceptance criteria: `implmention/acceptance-criteria/F-08-Acceptance-Criteria.md`
- Sprint plan: `implmention/IMS-Sprint-Plan.md`

*Technical Lead checklist — F-08*
