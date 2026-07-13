# Implementation Checklist — F-02: Location & Network Setup

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-02 |
| **Feature Name** | Location & Network Setup |
| **Document Type** | Technical Lead Implementation Checklist |
| **Feature dependencies** | F-27 |
| **Default status** | Not Started |
| **Task count** | 20 |

---

## Checklist

| Task ID | Feature | Task description | Layer | Priority | Status | Dependencies |
|---------|---------|------------------|-------|----------|--------|--------------|
| `CHK-02-DB-01` | F-02 | Create Flyway schema `network` | Database | P0 | Not Started | F-27 |
| `CHK-02-DB-02` | F-02 | Create `network.inventory_locations` with location_code UK, hierarchy self-FK, status | Database | P0 | Not Started | CHK-02-DB-01 |
| `CHK-02-DB-03` | F-02 | Create `network.storage_positions` FK to location | Database | P0 | Not Started | CHK-02-DB-02 |
| `CHK-02-DB-04` | F-02 | Add freeze/operational status columns and CHECKs | Database | P0 | Not Started | CHK-02-DB-02 |
| `CHK-02-DB-05` | F-02 | Indexes on location_code, parent_location_id, operational_status | Database | P1 | Not Started | CHK-02-DB-02 |
| `CHK-02-BE-01` | F-02 | Implement InventoryLocation aggregate + StoragePosition entity | Backend | P0 | Not Started | CHK-02-DB-03 |
| `CHK-02-BE-02` | F-02 | VOs: LocationCode, LocationType, HierarchyPath, PhysicalAddress | Backend | P0 | Not Started | CHK-02-BE-01 |
| `CHK-02-BE-03` | F-02 | Repositories for location and storage positions | Backend | P0 | Not Started | CHK-02-BE-01 |
| `CHK-02-BE-04` | F-02 | DTOs/mappers for location APIs | Backend | P0 | Not Started | CHK-02-BE-02 |
| `CHK-02-BE-05` | F-02 | LocationLifecycleService (create, hierarchy, activate/deactivate/close, freeze status) | Backend | P0 | Not Started | CHK-02-BE-03 |
| `CHK-02-BE-06` | F-02 | LocationController API-011–021 + cycle hierarchy validation | Backend | P0 | Not Started | CHK-02-BE-05 |
| `CHK-02-BE-07` | F-02 | Enforce LOCATION_MANAGE/VIEW + location-scope filters | Backend | P0 | Not Started | F-27, CHK-02-BE-06 |
| `CHK-02-FE-01` | F-02 | Child routes for location detail and storage positions | Frontend | P0 | Not Started | F-27 |
| `CHK-02-FE-02` | F-02 | LocationApiService + LocationFacade | Frontend | P0 | Not Started | CHK-02-BE-06 |
| `CHK-02-FE-03` | F-02 | UI-007 list/create/edit + hierarchy tree + storage grid | Frontend | P0 | Not Started | CHK-02-FE-02 |
| `CHK-02-FE-04` | F-02 | Activation UX with opening-balance gate messaging | Frontend | P1 | Not Started | CHK-02-FE-03, F-30 |
| `CHK-02-TE-01` | F-02 | API tests API-011–017; reject cyclic hierarchy | Testing | P0 | Not Started | CHK-02-BE-06 |
| `CHK-02-TE-02` | F-02 | UI test create WH + add bin (FAC-02-H1/H3) | Testing | P1 | Not Started | CHK-02-FE-03 |
| `CHK-02-TE-03` | F-02 | Permission deny without LOCATION_MANAGE (FAC-02-P1) | Testing | P0 | Not Started | CHK-02-BE-07 |
| `CHK-02-DO-01` | F-02 | OpenAPI location module + go-live activation notes | Documentation | P1 | Not Started | CHK-02-BE-06 |

## Layer summary

| Layer | Count |
|-------|-------|
| Database | 5 |
| Backend | 7 |
| Frontend | 4 |
| Testing | 3 |
| Documentation | 1 |

## Priority summary

| Priority | Meaning | Count |
|----------|---------|-------|
| P0 | MVP critical / blocking | 16 |
| P1 | MVP important | 4 |
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

- Implementation plan: `implmention/plans/` (F-02)
- Acceptance criteria: `implmention/acceptance-criteria/F-02-Acceptance-Criteria.md`
- Sprint plan: `implmention/IMS-Sprint-Plan.md`

*Technical Lead checklist — F-02*
