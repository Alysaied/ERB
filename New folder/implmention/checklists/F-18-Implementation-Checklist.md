# Implementation Checklist — F-18: Quarantine & Hold Stock Management

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-18 |
| **Feature Name** | Quarantine & Hold Stock Management |
| **Document Type** | Technical Lead Implementation Checklist |
| **Feature dependencies** | F-04, F-27 |
| **Default status** | Not Started |
| **Task count** | 6 |

---

## Checklist

| Task ID | Feature | Task description | Layer | Priority | Status | Dependencies |
|---------|---------|------------------|-------|----------|--------|--------------|
| `CHK-18-DB-01` | F-18 | Ensure quarantine_holds table + hold type CHECK | Database | P2 | Not Started | F-04 |
| `CHK-18-BE-01` | F-18 | QuarantineHoldService apply/release updating ATP | Backend | P2 | Not Started | CHK-18-DB-01 |
| `CHK-18-BE-02` | F-18 | API-045, 046, 154 | Backend | P2 | Not Started | CHK-18-BE-01 |
| `CHK-18-FE-01` | F-18 | UI-028 quarantine register | Frontend | P2 | Not Started | CHK-18-BE-02 |
| `CHK-18-TE-01` | F-18 | FAC-18-H1/H2 ATP exclusion | Testing | P2 | Not Started | CHK-18-FE-01 |
| `CHK-18-DO-01` | F-18 | Hold type definitions for WH | Documentation | P2 | Not Started | CHK-18-BE-02 |

## Layer summary

| Layer | Count |
|-------|-------|
| Database | 1 |
| Backend | 2 |
| Frontend | 1 |
| Testing | 1 |
| Documentation | 1 |

## Priority summary

| Priority | Meaning | Count |
|----------|---------|-------|
| P0 | MVP critical / blocking | 0 |
| P1 | MVP important | 0 |
| P2 | Phase 2 Should Have | 6 |
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

- Implementation plan: `implmention/plans/` (F-18)
- Acceptance criteria: `implmention/acceptance-criteria/F-18-Acceptance-Criteria.md`
- Sprint plan: `implmention/IMS-Sprint-Plan.md`

*Technical Lead checklist — F-18*
