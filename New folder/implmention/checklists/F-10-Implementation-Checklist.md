# Implementation Checklist — F-10: Order Availability & Reservation

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-10 |
| **Feature Name** | Order Availability & Reservation |
| **Document Type** | Technical Lead Implementation Checklist |
| **Feature dependencies** | F-04, F-01, F-27 |
| **Default status** | Not Started |
| **Task count** | 11 |

---

## Checklist

| Task ID | Feature | Task description | Layer | Priority | Status | Dependencies |
|---------|---------|------------------|-------|----------|--------|--------------|
| `CHK-10-DB-01` | F-10 | Create fulfillment.customer_orders, order_lines, inventory_reservations | Database | P0 | Not Started | F-04 |
| `CHK-10-DB-02` | F-10 | Optimistic locking on stock_positions for reservation races | Database | P0 | Not Started | CHK-10-DB-01 |
| `CHK-10-BE-01` | F-10 | CustomerOrderFulfillment aggregate + reservation saga | Backend | P0 | Not Started | CHK-10-DB-02 |
| `CHK-10-BE-02` | F-10 | API-081, 084–086, 043–044 (087 multi-location P2) | Backend | P0 | Not Started | CHK-10-BE-01 |
| `CHK-10-BE-03` | F-10 | ORDER_RESERVE permission + location scope | Backend | P0 | Not Started | F-27, CHK-10-BE-02 |
| `CHK-10-FE-01` | F-10 | FulfillmentApiService + ReservationFacade | Frontend | P0 | Not Started | CHK-10-BE-02 |
| `CHK-10-FE-02` | F-10 | UI-030 reservation workbench | Frontend | P0 | Not Started | CHK-10-FE-01 |
| `CHK-10-FE-03` | F-10 | UI-035 multi-location planner (Phase 2) | Frontend | P2 | Not Started | CHK-10-BE-02 |
| `CHK-10-TE-01` | F-10 | FAC-10-H1–H3, E1 concurrency, V3 insufficient ATP | Testing | P0 | Not Started | CHK-10-FE-02 |
| `CHK-10-TE-02` | F-10 | Cancel releases reservation restores ATP | Testing | P0 | Not Started | CHK-10-BE-02 |
| `CHK-10-DO-01` | F-10 | Reservation saga notes + idempotency keys | Documentation | P1 | Not Started | CHK-10-BE-01 |

## Layer summary

| Layer | Count |
|-------|-------|
| Database | 2 |
| Backend | 3 |
| Frontend | 3 |
| Testing | 2 |
| Documentation | 1 |

## Priority summary

| Priority | Meaning | Count |
|----------|---------|-------|
| P0 | MVP critical / blocking | 9 |
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

- Implementation plan: `implmention/plans/` (F-10)
- Acceptance criteria: `implmention/acceptance-criteria/F-10-Acceptance-Criteria.md`
- Sprint plan: `implmention/IMS-Sprint-Plan.md`

*Technical Lead checklist — F-10*
