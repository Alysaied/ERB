# Implementation Checklist — F-04: Inventory Visibility & Search

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-04 |
| **Feature Name** | Inventory Visibility & Search |
| **Document Type** | Technical Lead Implementation Checklist |
| **Feature dependencies** | F-01, F-02, F-27 |
| **Default status** | Not Started |
| **Task count** | 16 |

---

## Checklist

| Task ID | Feature | Task description | Layer | Priority | Status | Dependencies |
|---------|---------|------------------|-------|----------|--------|--------------|
| `CHK-04-DB-01` | F-04 | Ensure `inventory.stock_positions` with on_hand/reserved/quarantine qty CHECKs | Database | P0 | Not Started | F-01, F-02 |
| `CHK-04-DB-02` | F-04 | Create `inventory.lot_batches` and `quarantine_holds` tables | Database | P1 | Not Started | CHK-04-DB-01 |
| `CHK-04-DB-03` | F-04 | Indexes for (location_code, sku) and status queries | Database | P0 | Not Started | CHK-04-DB-01 |
| `CHK-04-BE-01` | F-04 | StockPosition aggregate + ATP calculation domain service | Backend | P0 | Not Started | CHK-04-DB-01 |
| `CHK-04-BE-02` | F-04 | StockPositionRepository + query repository | Backend | P0 | Not Started | CHK-04-BE-01 |
| `CHK-04-BE-03` | F-04 | DTOs for stock position, availability, status board | Backend | P0 | Not Started | CHK-04-BE-02 |
| `CHK-04-BE-04` | F-04 | API-033–037 + intelligence 151–153 (MVP subset) | Backend | P0 | Not Started | CHK-04-BE-03 |
| `CHK-04-BE-05` | F-04 | Enforce INVENTORY_VIEW + mandatory location-scope filter | Backend | P0 | Not Started | F-27, CHK-04-BE-04 |
| `CHK-04-FE-01` | F-04 | InventoryApiService + InventoryVisibilityFacade | Frontend | P0 | Not Started | CHK-04-BE-04 |
| `CHK-04-FE-02` | F-04 | UI-020 status monitor with real data + filters | Frontend | P0 | Not Started | CHK-04-FE-01 |
| `CHK-04-FE-03` | F-04 | UI-021 availability inquiry form + results | Frontend | P0 | Not Started | CHK-04-FE-01 |
| `CHK-04-FE-04` | F-04 | Network/inbound views (US-028 Phase 2) | Frontend | P2 | Not Started | CHK-04-FE-02, F-07 |
| `CHK-04-TE-01` | F-04 | Unit tests ATP = on_hand - reserved - hold | Testing | P0 | Not Started | CHK-04-BE-01 |
| `CHK-04-TE-02` | F-04 | API + scope tests FAC-04-H1/P3 | Testing | P0 | Not Started | CHK-04-BE-05 |
| `CHK-04-TE-03` | F-04 | UI smoke FAC-04-H4 search/filter | Testing | P1 | Not Started | CHK-04-FE-02 |
| `CHK-04-DO-01` | F-04 | ATP definition note for UAT script | Documentation | P1 | Not Started | CHK-04-BE-01 |

## Layer summary

| Layer | Count |
|-------|-------|
| Database | 3 |
| Backend | 5 |
| Frontend | 4 |
| Testing | 3 |
| Documentation | 1 |

## Priority summary

| Priority | Meaning | Count |
|----------|---------|-------|
| P0 | MVP critical / blocking | 12 |
| P1 | MVP important | 3 |
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

- Implementation plan: `implmention/plans/` (F-04)
- Acceptance criteria: `implmention/acceptance-criteria/F-04-Acceptance-Criteria.md`
- Sprint plan: `implmention/IMS-Sprint-Plan.md`

*Technical Lead checklist — F-04*
