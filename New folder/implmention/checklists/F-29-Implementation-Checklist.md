# Implementation Checklist — F-29: Audit Trail & Compliance

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-29 |
| **Feature Name** | Audit Trail & Compliance |
| **Document Type** | Technical Lead Implementation Checklist |
| **Feature dependencies** | F-28 |
| **Default status** | Not Started |
| **Task count** | 9 |

---

## Checklist

| Task ID | Feature | Task description | Layer | Priority | Status | Dependencies |
|---------|---------|------------------|-------|----------|--------|--------------|
| `CHK-29-DB-01` | F-29 | inventory_movement_records + audit_trail_records; REVOKE UPDATE/DELETE | Database | P0 | Not Started | F-28 |
| `CHK-29-DB-02` | F-29 | Indexes on entity/date/user for query performance | Database | P1 | Not Started | CHK-29-DB-01 |
| `CHK-29-BE-01` | F-29 | MovementAppendService used by all stock mutators | Backend | P0 | Not Started | CHK-29-DB-01 |
| `CHK-29-BE-02` | F-29 | AuditTrailQueryService + API-155–157 | Backend | P0 | Not Started | CHK-29-BE-01 |
| `CHK-29-BE-03` | F-29 | Control breach detection (Phase 2) | Backend | P2 | Not Started | CHK-29-BE-02 |
| `CHK-29-FE-01` | F-29 | UI-022 movement history; UI-048 audit query | Frontend | P0 | Not Started | CHK-29-BE-02 |
| `CHK-29-FE-02` | F-29 | UI-047 audit workspace (Phase 2) | Frontend | P2 | Not Started | CHK-29-BE-03 |
| `CHK-29-TE-01` | F-29 | FAC-29-H1/E1 mutate audit forbidden; P1 AUDIT_VIEW | Testing | P0 | Not Started | CHK-29-FE-01 |
| `CHK-29-DO-01` | F-29 | Audit retention & export policy | Documentation | P1 | Not Started | CHK-29-BE-02 |

## Layer summary

| Layer | Count |
|-------|-------|
| Database | 2 |
| Backend | 3 |
| Frontend | 2 |
| Testing | 1 |
| Documentation | 1 |

## Priority summary

| Priority | Meaning | Count |
|----------|---------|-------|
| P0 | MVP critical / blocking | 5 |
| P1 | MVP important | 2 |
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

- Implementation plan: `implmention/plans/` (F-29)
- Acceptance criteria: `implmention/acceptance-criteria/F-29-Acceptance-Criteria.md`
- Sprint plan: `implmention/IMS-Sprint-Plan.md`

*Technical Lead checklist — F-29*
