# Implementation Checklist — F-05: Goods Receiving & Verification

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-05 |
| **Feature Name** | Goods Receiving & Verification |
| **Document Type** | Technical Lead Implementation Checklist |
| **Feature dependencies** | F-01, F-02, F-03, F-27 |
| **Default status** | Not Started |
| **Task count** | 18 |

---

## Checklist

| Task ID | Feature | Task description | Layer | Priority | Status | Dependencies |
|---------|---------|------------------|-------|----------|--------|--------------|
| `CHK-05-DB-01` | F-05 | Create `inbound` schema + goods_receipts / lines | Database | P0 | Not Started | F-02 |
| `CHK-05-DB-02` | F-05 | Create `inbound.receipt_discrepancies` | Database | P0 | Not Started | CHK-05-DB-01 |
| `CHK-05-DB-03` | F-05 | Ensure movement table available for receipt postings | Database | P0 | Not Started | F-29 |
| `CHK-05-DB-04` | F-05 | Minimal PO seed/table support for validate-for-receipt until F-07 | Database | P0 | Not Started | CHK-05-DB-01 |
| `CHK-05-BE-01` | F-05 | GoodsReceipt aggregate + discrepancy entity | Backend | P0 | Not Started | CHK-05-DB-02 |
| `CHK-05-BE-02` | F-05 | VOs: PositiveQuantity, LotIdentity, ShelfLifeProfile | Backend | P0 | Not Started | CHK-05-BE-01 |
| `CHK-05-BE-03` | F-05 | GoodsReceivingService + DiscrepancyService + movement recording | Backend | P0 | Not Started | CHK-05-BE-01, F-29 |
| `CHK-05-BE-04` | F-05 | API-065–072, 075–076 + reason/tolerance consult | Backend | P0 | Not Started | CHK-05-BE-03, F-03 |
| `CHK-05-BE-05` | F-05 | Freeze check + RECEIVE_GOODS / location scope security | Backend | P0 | Not Started | F-27, CHK-05-BE-04 |
| `CHK-05-FE-01` | F-05 | InboundApiService + GoodsReceiptFacade | Frontend | P0 | Not Started | CHK-05-BE-04 |
| `CHK-05-FE-02` | F-05 | UI-015 goods receipt workbench | Frontend | P0 | Not Started | CHK-05-FE-01 |
| `CHK-05-FE-03` | F-05 | UI-016 discrepancy resolution | Frontend | P0 | Not Started | CHK-05-FE-01 |
| `CHK-05-FE-04` | F-05 | UI-018 non-PO/return intake | Frontend | P1 | Not Started | CHK-05-FE-01 |
| `CHK-05-FE-05` | F-05 | UI-022 movement history consumer | Frontend | P1 | Not Started | F-29, CHK-05-BE-03 |
| `CHK-05-TE-01` | F-05 | API E2E receive+verify; discrepancy path FAC-05-H1/H2 | Testing | P0 | Not Started | CHK-05-FE-02 |
| `CHK-05-TE-02` | F-05 | Lot required for traceable product FAC-05-V2 | Testing | P0 | Not Started | CHK-05-BE-04 |
| `CHK-05-TE-03` | F-05 | Permission/location scope FAC-05-P1/P2 | Testing | P0 | Not Started | CHK-05-BE-05 |
| `CHK-05-DO-01` | F-05 | Document PO-stub vs F-07 cutover for receiving | Documentation | P1 | Not Started | CHK-05-BE-04 |

## Layer summary

| Layer | Count |
|-------|-------|
| Database | 4 |
| Backend | 5 |
| Frontend | 5 |
| Testing | 3 |
| Documentation | 1 |

## Priority summary

| Priority | Meaning | Count |
|----------|---------|-------|
| P0 | MVP critical / blocking | 15 |
| P1 | MVP important | 3 |
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

- Implementation plan: `implmention/plans/` (F-05)
- Acceptance criteria: `implmention/acceptance-criteria/F-05-Acceptance-Criteria.md`
- Sprint plan: `implmention/IMS-Sprint-Plan.md`

*Technical Lead checklist — F-05*
