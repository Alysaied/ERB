# Implementation Checklist — F-07: Purchase Order & Inbound Supply Management

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-07 |
| **Feature Name** | Purchase Order & Inbound Supply Management |
| **Document Type** | Technical Lead Implementation Checklist |
| **Feature dependencies** | F-01, F-02, F-27 |
| **Default status** | Not Started |
| **Task count** | 12 |

---

## Checklist

| Task ID | Feature | Task description | Layer | Priority | Status | Dependencies |
|---------|---------|------------------|-------|----------|--------|--------------|
| `CHK-07-DB-01` | F-07 | Create `procurement` schema: suppliers, POs, lines, expected deliveries | Database | P2 | Not Started | F-01, F-02 |
| `CHK-07-DB-02` | F-07 | PO status CHECKs; supplier_code UK; FKs for lines/deliveries | Database | P2 | Not Started | CHK-07-DB-01 |
| `CHK-07-BE-01` | F-07 | Supplier + PurchaseOrder aggregates | Backend | P2 | Not Started | CHK-07-DB-02 |
| `CHK-07-BE-02` | F-07 | PurchaseOrderService (create/amend/cancel/schedule delivery) | Backend | P2 | Not Started | CHK-07-BE-01 |
| `CHK-07-BE-03` | F-07 | API-049–053, 059–065, 161–163 | Backend | P2 | Not Started | CHK-07-BE-02 |
| `CHK-07-BE-04` | F-07 | Permissions SUPPLIER_MANAGE / PO_MANAGE / PO_VIEW | Backend | P2 | Not Started | F-27, CHK-07-BE-03 |
| `CHK-07-FE-01` | F-07 | ProcurementApiService + PurchaseOrderFacade | Frontend | P2 | Not Started | CHK-07-BE-03 |
| `CHK-07-FE-02` | F-07 | UI-011 suppliers, UI-012 POs | Frontend | P2 | Not Started | CHK-07-FE-01 |
| `CHK-07-FE-03` | F-07 | UI-014 delivery planning, UI-019 inbound tracking | Frontend | P2 | Not Started | CHK-07-FE-01 |
| `CHK-07-TE-01` | F-07 | FAC-07-H1/H3/V1/V2 API+UI | Testing | P2 | Not Started | CHK-07-FE-02 |
| `CHK-07-TE-02` | F-07 | Receiving integration uses live validate-for-receipt | Testing | P2 | Not Started | CHK-07-BE-03, F-05 |
| `CHK-07-DO-01` | F-07 | Replace PO-stub runbook with F-07 cutover notes | Documentation | P2 | Not Started | CHK-07-BE-03 |

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
| P0 | MVP critical / blocking | 0 |
| P1 | MVP important | 0 |
| P2 | Phase 2 Should Have | 12 |
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

- Implementation plan: `implmention/plans/` (F-07)
- Acceptance criteria: `implmention/acceptance-criteria/F-07-Acceptance-Criteria.md`
- Sprint plan: `implmention/IMS-Sprint-Plan.md`

*Technical Lead checklist — F-07*
