# Implementation Checklist — F-26: Operational Notifications & Alerts

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-26 |
| **Feature Name** | Operational Notifications & Alerts |
| **Document Type** | Technical Lead Implementation Checklist |
| **Feature dependencies** | F-27 |
| **Default status** | Not Started |
| **Task count** | 7 |

---

## Checklist

| Task ID | Feature | Task description | Layer | Priority | Status | Dependencies |
|---------|---------|------------------|-------|----------|--------|--------------|
| `CHK-26-DB-01` | F-26 | Ensure `audit.operational_alerts` with ack columns/indexes | Database | P0 | Not Started | F-27 |
| `CHK-26-BE-01` | F-26 | NotificationService + role-filtered feed + API-158/159 | Backend | P0 | Not Started | CHK-26-DB-01 |
| `CHK-26-BE-02` | F-26 | Wire producers: stock, approval, transfer, fulfillment, inbound, campaign | Backend | P1 | Not Started | CHK-26-BE-01, F-20, F-17 |
| `CHK-26-FE-01` | F-26 | Core NotificationFacade + header badge | Frontend | P0 | Not Started | CHK-26-BE-01 |
| `CHK-26-FE-02` | F-26 | UI-004 notification center list/ack/deep links | Frontend | P0 | Not Started | CHK-26-FE-01 |
| `CHK-26-TE-01` | F-26 | FAC-26-H1–H3/P1 role filtering | Testing | P0 | Not Started | CHK-26-FE-02 |
| `CHK-26-DO-01` | F-26 | Alert taxonomy & recipient matrix | Documentation | P1 | Not Started | CHK-26-BE-02 |

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

- Implementation plan: `implmention/plans/` (F-26)
- Acceptance criteria: `implmention/acceptance-criteria/F-26-Acceptance-Criteria.md`
- Sprint plan: `implmention/IMS-Sprint-Plan.md`

*Technical Lead checklist — F-26*
