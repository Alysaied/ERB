# Implementation Checklist — F-28: Operational Accountability & Controls

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-28 |
| **Feature Name** | Operational Accountability & Controls |
| **Document Type** | Technical Lead Implementation Checklist |
| **Feature dependencies** | F-27 |
| **Default status** | Not Started |
| **Task count** | 7 |

---

## Checklist

| Task ID | Feature | Task description | Layer | Priority | Status | Dependencies |
|---------|---------|------------------|-------|----------|--------|--------------|
| `CHK-28-DB-01` | F-28 | Ensure audit_trail_records; SoD rule seed in governance | Database | P0 | Not Started | F-27 |
| `CHK-28-BE-01` | F-28 | SegregationOfDutiesService + ActivityLogging aspect/interceptor | Backend | P0 | Not Started | CHK-28-DB-01 |
| `CHK-28-BE-02` | F-28 | API-031, 148, 149 wired into approval commands | Backend | P0 | Not Started | CHK-28-BE-01 |
| `CHK-28-FE-01` | F-28 | Disable approve actions when SoD evaluate fails; show dialog | Frontend | P0 | Not Started | CHK-28-BE-02 |
| `CHK-28-FE-02` | F-28 | UI-050 SoD/policy configuration surfaces | Frontend | P1 | Not Started | CHK-28-BE-02 |
| `CHK-28-TE-01` | F-28 | FAC-28-H2/E1 self-approve blocked on adjustment/variance/transfer | Testing | P0 | Not Started | CHK-28-FE-01, F-17 |
| `CHK-28-DO-01` | F-28 | SoD matrix (initiator vs approver) for auditors | Documentation | P1 | Not Started | CHK-28-BE-01 |

## Layer summary

| Layer | Count |
|-------|-------|
| Database | 1 |
| Backend | 2 |
| Frontend | 2 |
| Testing | 1 |
| Documentation | 1 |

## Priority summary

| Priority | Meaning | Count |
|----------|---------|-------|
| P0 | MVP critical / blocking | 5 |
| P1 | MVP important | 2 |
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

- Implementation plan: `implmention/plans/` (F-28)
- Acceptance criteria: `implmention/acceptance-criteria/F-28-Acceptance-Criteria.md`
- Sprint plan: `implmention/IMS-Sprint-Plan.md`

*Technical Lead checklist — F-28*
