# Implementation Checklist — F-03: Stock Policy & Product Classification

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-03 |
| **Feature Name** | Stock Policy & Product Classification |
| **Document Type** | Technical Lead Implementation Checklist |
| **Feature dependencies** | F-01, F-02, F-27 |
| **Default status** | Not Started |
| **Task count** | 17 |

---

## Checklist

| Task ID | Feature | Task description | Layer | Priority | Status | Dependencies |
|---------|---------|------------------|-------|----------|--------|--------------|
| `CHK-03-DB-01` | F-03 | Create `governance` schema + `reason_codes` + `governance_policies` | Database | P0 | Not Started | F-27 |
| `CHK-03-DB-02` | F-03 | Create `inventory.stock_policies` + `stock_policy_history` | Database | P0 | Not Started | F-01, F-02 |
| `CHK-03-DB-03` | F-03 | Constraints: uk(location,sku), qty>=0, reason code unique/retire flag | Database | P0 | Not Started | CHK-03-DB-01, CHK-03-DB-02 |
| `CHK-03-DB-04` | F-03 | ABC column/attr on catalog.products if not present | Database | P2 | Not Started | F-01 |
| `CHK-03-BE-01` | F-03 | StockPolicy + GovernancePolicy + ReasonCode aggregates | Backend | P0 | Not Started | CHK-03-DB-03 |
| `CHK-03-BE-02` | F-03 | VOs: StockThresholdSet, ApprovalThreshold, QuantityTolerance, AbcClass | Backend | P0 | Not Started | CHK-03-BE-01 |
| `CHK-03-BE-03` | F-03 | Repositories + DTOs for policies/reason codes/ABC | Backend | P0 | Not Started | CHK-03-BE-01 |
| `CHK-03-BE-04` | F-03 | StockPolicyService + GovernanceService (effective dating) | Backend | P0 | Not Started | CHK-03-BE-03 |
| `CHK-03-BE-05` | F-03 | API-038–040, API-022–030, API-006 | Backend | P0 | Not Started | CHK-03-BE-04 |
| `CHK-03-BE-06` | F-03 | SafetyStockProtectionService hooks for later consumers | Backend | P2 | Not Started | CHK-03-BE-04 |
| `CHK-03-BE-07` | F-03 | Permissions POLICY_MANAGE / GOVERNANCE_MANAGE | Backend | P0 | Not Started | F-27, CHK-03-BE-05 |
| `CHK-03-FE-01` | F-03 | UI-008 stock policy forms wired to API | Frontend | P0 | Not Started | CHK-03-BE-05 |
| `CHK-03-FE-02` | F-03 | UI-010 reason codes + thresholds/tolerances | Frontend | P0 | Not Started | CHK-03-BE-05 |
| `CHK-03-FE-03` | F-03 | UI-009 ABC classification grid (Phase 2) | Frontend | P2 | Not Started | CHK-03-BE-05 |
| `CHK-03-TE-01` | F-03 | API tests thresholds + retire reason code blocks use | Testing | P0 | Not Started | CHK-03-BE-05 |
| `CHK-03-TE-02` | F-03 | FAC-03-H1/V1/V4/P1 automated | Testing | P0 | Not Started | CHK-03-FE-01 |
| `CHK-03-DO-01` | F-03 | Document effective-dating rules for ops | Documentation | P2 | Not Started | CHK-03-BE-04 |

## Layer summary

| Layer | Count |
|-------|-------|
| Database | 4 |
| Backend | 7 |
| Frontend | 3 |
| Testing | 2 |
| Documentation | 1 |

## Priority summary

| Priority | Meaning | Count |
|----------|---------|-------|
| P0 | MVP critical / blocking | 13 |
| P1 | MVP important | 0 |
| P2 | Phase 2 Should Have | 4 |
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

- Implementation plan: `implmention/plans/` (F-03)
- Acceptance criteria: `implmention/acceptance-criteria/F-03-Acceptance-Criteria.md`
- Sprint plan: `implmention/IMS-Sprint-Plan.md`

*Technical Lead checklist — F-03*
