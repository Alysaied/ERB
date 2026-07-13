# Implementation Checklist — F-27: User Access & Role Management

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-27 |
| **Feature Name** | User Access & Role Management |
| **Document Type** | Technical Lead Implementation Checklist |
| **Feature dependencies** | None |
| **Default status** | Not Started |
| **Task count** | 13 |

---

## Checklist

| Task ID | Feature | Task description | Layer | Priority | Status | Dependencies |
|---------|---------|------------------|-------|----------|--------|--------------|
| `CHK-27-DB-01` | F-27 | Create `identity` schema: user_accounts, role_assignments, role_assignment_locations | Database | P0 | Not Started | — |
| `CHK-27-DB-02` | F-27 | Seed admin user + baseline roles (UR subset) | Database | P0 | Not Started | CHK-27-DB-01 |
| `CHK-27-BE-01` | F-27 | Spring Security OAuth2/JWT resource server + session endpoints | Backend | P0 | Not Started | CHK-27-DB-02 |
| `CHK-27-BE-02` | F-27 | UserAccount aggregate + UserAdminService | Backend | P0 | Not Started | CHK-27-DB-01 |
| `CHK-27-BE-03` | F-27 | API-140–149, 173, 174 | Backend | P0 | Not Started | CHK-27-BE-01, CHK-27-BE-02 |
| `CHK-27-BE-04` | F-27 | Authorization evaluate + location-scope validate services | Backend | P0 | Not Started | CHK-27-BE-03 |
| `CHK-27-FE-01` | F-27 | HttpClient, interceptors, environments, auth/guest guards | Frontend | P0 | Not Started | CHK-27-BE-01 |
| `CHK-27-FE-02` | F-27 | UI-001 real sign-in; AuthService/SessionStore signals | Frontend | P0 | Not Started | CHK-27-FE-01 |
| `CHK-27-FE-03` | F-27 | UI-049 user admin, UI-050 roles/access | Frontend | P0 | Not Started | CHK-27-BE-03 |
| `CHK-27-FE-04` | F-27 | Permission-aware navigation filtering | Frontend | P1 | Not Started | CHK-27-FE-03 |
| `CHK-27-TE-01` | F-27 | FAC-27-H1/H3/E1/E2/P1 API+UI | Testing | P0 | Not Started | CHK-27-FE-02 |
| `CHK-27-TE-02` | F-27 | Protected route returns 401 without token | Testing | P0 | Not Started | CHK-27-FE-01 |
| `CHK-27-DO-01` | F-27 | Auth setup, seed users, role matrix quick ref | Documentation | P0 | Not Started | CHK-27-BE-03 |

## Layer summary

| Layer | Count |
|-------|-------|
| Database | 2 |
| Backend | 4 |
| Frontend | 4 |
| Testing | 2 |
| Documentation | 1 |

## Priority summary

| Priority | Meaning | Count |
|----------|---------|-------|
| P0 | MVP critical / blocking | 12 |
| P1 | MVP important | 1 |
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

- Implementation plan: `implmention/plans/` (F-27)
- Acceptance criteria: `implmention/acceptance-criteria/F-27-Acceptance-Criteria.md`
- Sprint plan: `implmention/IMS-Sprint-Plan.md`

*Technical Lead checklist — F-27*
