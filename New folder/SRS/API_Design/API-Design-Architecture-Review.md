# API Design Architecture Review
## Inventory Management System — Pre-UI Design Gate

---

## Document Information

| Attribute | Detail |
|-----------|--------|
| **Document ID** | SRS-API-010 |
| **Document Title** | Chief Backend Architect — API Design Review |
| **Version** | 1.0 |
| **Status** | Draft — Review Findings |
| **Reviewer Role** | Chief Backend Architect |
| **Date** | July 6, 2026 |
| **Scope** | Full API design package (SRS-API-001 through SRS-API-009) |
| **Gate** | **Must resolve Critical and High items before UI design begins** |

### Artifacts Reviewed

| ID | Document | Coverage |
|----|----------|----------|
| SRS-API-001 | `REST-API-Catalog.md` | 178 endpoints |
| SRS-API-002 | `Request-DTOs.md` | 178 request contracts |
| SRS-API-003 | `Response-DTOs.md` | 178 success responses |
| SRS-API-004 | `Request-DTO-Validation-Spec.md` | 178 APIs (15 grouped) |
| SRS-API-005 | `Error-Response-Specification.md` | RFC 7807 + IMS extensions |
| SRS-API-006 | `Collection-API-Strategy.md` | 44 collection endpoints |
| SRS-API-007 | `API-Authorization-Specification.md` | RBAC per endpoint |
| SRS-API-008 | `API-Versioning-Strategy.md` | URI path versioning |
| SRS-API-009 | `Complete-API-Specification.md` (Parts 1–3) | 178 endpoint specs |

### Review Method

Cross-artifact consistency analysis, REST maturity assessment, security/RBAC review, use-case traceability check (SRS-UC-001), and UI-readiness evaluation for screen-level data requirements.

---

## Executive Summary

The IMS API design package is **substantially complete and enterprise-grade** for a v1 inventory platform. Strengths include comprehensive use-case coverage (48/48 UCs mapped), consistent RBAC (`PERM-001`–`PERM-100`), a well-defined RFC 7807 error model, and a thoughtful collection strategy for list/search endpoints.

**Overall readiness for UI design: Conditional Go** — proceed only after resolving **6 Critical** and **12 High** findings below. The design is implementation-ready for backend scaffolding, but several contract inconsistencies will cause UI rework, integration failures, or security gaps if not corrected first.

| Dimension | Rating | Summary |
|-----------|--------|---------|
| API Catalog completeness | **B+** | 178 APIs; a few UI-critical list endpoints missing |
| DTO consistency | **B** | Strong shared primitives; naming drift across modules |
| Validation coverage | **B−** | All APIs referenced; 15 grouped profiles lack field detail |
| Response model | **B+** | Consistent wrappers; minor conflicts on API-089 |
| Error model | **A−** | RFC 7807, traceability, layer mapping — excellent |
| Pagination / filtering | **B+** | 44 collections documented; operational/intelligence split needs UI guidance |
| Versioning | **B** | Sound strategy; catalog vs. strategy path conflict on health |
| Authentication | **B−** | IdP-delegated model correct; login flow undocumented for UI |
| Authorization | **A−** | Per-endpoint RBAC with SoD and sensitivity classes |
| REST design | **B−** | Intentional command pattern; some path/purpose mismatches |

---

## 1. API Catalog Analysis

### 1.1 Strengths

- **Complete module coverage:** M-01 through M-13 plus Platform (178 APIs).
- **Traceability:** Every API links to use case(s) and domain aggregate.
- **Command/query separation:** Write commands via `POST` action sub-paths; reads via `GET` with filters.
- **Integration boundary:** ACL inbound/outbound isolated under `/integrations/` (API-176–178).

### 1.2 Missing Endpoints

| ID | Gap | Impact | Recommendation |
|----|-----|--------|----------------|
| **GAP-API-01** | No `GET /api/v1/procurement/requisitions` list | Buyers cannot browse requisition queue in UI | Add **API-179** `GET /procurement/requisitions` with status/location filters (P-STD profile) |
| **GAP-API-02** | No warehouse pick queue at location scope | UC-024 pick workbench blocked | Add **API-180** `GET /api/v1/fulfillment/pick-lists/awaiting?locationCode=` OR fix API-089 (see Critical C-01) |
| **GAP-API-03** | No bulk import approval endpoint | API-010 references PERM-016 approval via "separate flow" but no API exists | Add **API-181** `POST /products/import/{jobId}/approve` or document job-status polling on import response |
| **GAP-API-04** | Version discovery not in catalog | SRS-API-008 defines `GET /api/versions`, `/api/v1/openapi`, `/api/v1/changelog` | Add Platform APIs **API-182–184** or explicitly mark as infrastructure-out-of-catalog |
| **GAP-API-05** | PERM-097 / PERM-100 unmapped | Security activity and breach record permissions have no APIs | Add read APIs for admin/security UI or defer with explicit "Phase 2" note in UI scope |
| **GAP-API-06** | No `GET` reservations list | Order detail UI cannot show active reservations without stock position drill-down | Add `GET .../reservations` or ensure order detail embeds reservations (document in API-083 response) |
| **GAP-API-07** | No product category master CRUD | UI category management only via product PATCH | Acceptable if categories are reference data managed offline; otherwise add governance APIs |
| **GAP-API-08** | No supplier delivery performance API | UC-006 / FR-022 gap (per Use Case Review) | Add intelligence projection or supplier scorecard endpoint for purchasing UI |
| **GAP-API-09** | No explicit safety-stock override request API | BR-010 enforced via `safetyStockExceptionReference` on existing commands only | Document UI flow: override is a reference captured on API-043/API-085, not a standalone workflow — or add governance case API |
| **GAP-API-10** | Authentication/login not in IMS API surface | Correct architecturally (SVC-01 IdP) but UI needs OIDC contract | Publish **UI Integration Addendum**: authorization code flow, token refresh, logout redirect — not new IMS endpoints |

### 1.3 Duplicate / Overlapping Endpoints

Not all overlaps are defects — many are **CQRS read/write splits**. Document intent for UI teams to avoid calling the wrong surface.

| Overlap | APIs | Assessment | UI Guidance |
|---------|------|------------|-------------|
| Order creation | API-081 (internal), API-176 (CRM integration) | **Intentional dual channel** | Sales UI → API-081; CRM → API-176; same domain command underneath |
| ATP inquiry | API-035, API-036, API-084 | **Different contexts** | Quick lookup → 035/036; order-scoped check → 084; audit log → 153 |
| Open PO board | API-060 (operational), API-161 (intelligence) | **Acceptable projection split** | Operational screens → 060; dashboard/KPI → 161; align filter params |
| Campaign readiness | API-136 (command evaluate), API-169 (read projection) | **CQRS pattern** | Launch workflow → 136; dashboard status → 169 |
| Ring-fence mutation | API-048 (event-driven internal), API-132 (user allocation) | **Potential confusion** | UI uses API-132/135/137/138; API-048 is system/integration only — **hide from UI route map** |
| Ring-fence check | API-139, embedded in API-035/036 flags | **Complementary** | Pre-order check → 139; ATP calc uses `excludePromotionalRingFence` on 036 |
| Return physical receipt | API-076 (`/inbound/return-receipts`), API-128 (`/returns/{returnId}/receive`) | **Overlapping responsibility** | **Clarify canonical path** — recommend API-128 for returns module UI; deprecate or alias API-076 |
| Transfer lists | API-099 (filtered), API-106, API-107 (specialized queues) | **Acceptable** | Approval queue UI → 106; in-transit pipeline → 107; general search → 099 |
| Stock status | API-037 (operational), API-151/152 (intelligence) | **Acceptable** | Location ops → 037; executive board → 152 |

### 1.4 REST Anti-Patterns

| ID | Pattern | Examples | Severity | Recommendation |
|----|---------|----------|----------|----------------|
| **REST-01** | **RPC-style POST commands** | `/approve`, `/dispatch`, `/verify`, `/certify` | Low (accepted) | Document as **Command API** pattern in UI dev guide; not pure REST — aligns with domain commands (CMD-xxx) |
| **REST-02** | **Path/purpose mismatch** | API-089 — see Critical C-01 | **Critical** | Fix path or purpose |
| **REST-03** | **Deep resource nesting** | `/inventory/stock-positions/{loc}/{sku}/reservations/{id}/release` | Medium | Accept for v1; consider `/reservations/{id}/release` in v2 |
| **REST-04** | **Inconsistent update verbs** | API-006 `PUT` for ABC; most updates use `PATCH` | Low | Standardize on `PATCH` in v2; document exception |
| **REST-05** | **DELETE rarely used** | Only API-144 uses `DELETE`; others use `POST .../cancel` | Low | Consistent with audit/traceability requirement — document convention |
| **REST-06** | **Static segments after path params risk** | `/transfers/pending-approvals` correctly ordered before `{transferId}` | None | Good — maintain this rule in new endpoints |
| **REST-07** | **GET used for export** | API-157 audit export may return large payloads | Medium | Confirm `202` async pattern for large exports; UI must poll export job |
| **REST-08** | **POST for reads** | API-084 availability check, API-148/149 auth evaluate | Low | Acceptable for complex request bodies; document why GET not used |

### 1.5 Naming Inconsistencies

| Area | Issue | Examples | Recommendation |
|------|-------|----------|----------------|
| **Resource ID names** | Mixed suffix conventions | `transferId`, `returnId`, `returnAuthorizationId`, `goodsReceiptId`, `purchaseOrderId` | Publish **Path Parameter Glossary** for UI code generators |
| **Return domain split** | RMA vs. return case | API-124–127 use `returnAuthorizationId`; API-128–130 use `returnId` | Document lifecycle: `returnAuthorizationId` → spawns `returnId` (return case) on first receipt; add to UI domain model |
| **Search parameter** | `q` vs. `search` | Most collections use `q`; API-141 users uses `search` | Normalize to `q` in v1.1 or document both in OpenAPI |
| **Module path prefixes** | Inconsistent top-level grouping | `/products`, `/inventory`, `/fulfillment`, `/inbound`, `/transfers`, `/accuracy` | Acceptable bounded context split — provide **UI API client module map** |
| **Intelligence prefix** | Read projections under `/intelligence/` | Ops reads at `/inventory/...`; dashboards at `/intelligence/...` | UI style guide: operational screens vs. analytics screens |
| **Health endpoint path** | **Conflict** — see Critical C-02 | Catalog: `/api/v1/health`; Versioning: `/api/health` | Pick one canonical path |
| **DTO naming** | API-089 DTO `ListOrdersAwaitingPickQuery` but path requires `orderId` | Misleading name | Rename to `ListAwaitingPickListsQuery` or fix endpoint |

---

## 2. DTO Analysis

### 2.1 Strengths

- Shared primitives (`ProductSku`, `LocationCode`, `QuantityDto`) with validation references.
- `PaginationQuery`, `DateRangeQuery`, `CommandResultResponse`, `PagedResponse<T>` reused consistently.
- Request and response DTOs cross-reference the same API IDs.

### 2.2 Issues

| ID | Issue | Location | Recommendation |
|----|-------|----------|----------------|
| **DTO-01** | API-089 response type conflict | Response-DTOs: `PagedResponse`; Collection-Strategy: `BoundedListResponse` | Align on one wrapper |
| **DTO-02** | Grouped request specs (15 groups) | API-013–014, 034–037, 050–053, 125–127, 141–142, 151–152 | Expand to per-API field tables before UI codegen |
| **DTO-03** | `CursorPagedResponse` vs. `PagedResponse` | API-177 integration feed | Document cursor response shape in Response-DTOs with example `links.next` |
| **DTO-04** | Bulk import payload undefined | API-010 | Specify file upload (`multipart/form-data`) vs. JSON array; max row count |
| **DTO-05** | `If-Match` / ETag only explicit on API-004 | Complete spec Part 1 | Extend optimistic locking documentation to API-040, API-062, API-135 PATCH endpoints |
| **DTO-06** | `ExportJobResponse` referenced but not in shared types | API-157 | Add to Response-DTOs shared section |

---

## 3. Validation Analysis

### 3.1 Strengths

- Every API has a validation profile in SRS-API-004.
- BR-xxx and VR-xxx traceability indexes are comprehensive.
- Cross-field rules documented for transfers, adjustments, returns, campaigns.
- SoD rules linked to API-031 and approval endpoints.

### 3.2 Missing / Weak Validations

| ID | Gap | APIs Affected | Recommendation |
|----|-----|---------------|----------------|
| **VAL-01** | Grouped profiles lack field-level rules | ~25 APIs in groups | Expand before UI form validation mirroring |
| **VAL-02** | Collection query enum values not in validation spec | All 44 collection GETs | Import `sortBy` whitelist and filter enums from SRS-API-006 into SRS-API-004 |
| **VAL-03** | `Idempotency-Key` format/reuse rules | S8 mutations, API-176–178 | Add VR for UUID format, 24h TTL, payload hash match (`CONF_IDEMPOTENCY_KEY_REUSED`) |
| **VAL-04** | `If-Match` header validation | Mutable PATCH endpoints | Add VR: ETag required on concurrent-sensitive updates |
| **VAL-05** | API-076 vs. API-128 mutual exclusivity | Return receipt paths | Add business rule: goods accepted via one path only |
| **VAL-06** | Integration `externalSystemCode` registry | API-176, 177, 178 | Validate against registered integration principals |
| **VAL-07** | `pageSize` max per profile | Collection APIs | Already in SRS-API-006 — ensure mirrored in validation spec |
| **VAL-08** | File import row-level validation | API-010 | Define per-row error reporting in import job response |

---

## 4. Response Model Analysis

### 4.1 Strengths

- Clear HTTP status conventions (`201` create, `200` command/read).
- `CommandResultResponse` standardizes action endpoints.
- `AuditInfoResponse` on master data supports UI audit panels.
- Error responses separated to SRS-API-005 (correct layering).

### 4.2 Issues

| ID | Issue | Recommendation |
|----|-------|----------------|
| **RES-01** | API-089 response wrapper inconsistency | Align Paged vs. Bounded — likely `BoundedListResponse` for single-order pick lists |
| **RES-02** | Order detail (API-083) may need embedded reservations, pick lists, shipments for UI | Evaluate `CustomerOrderDetailResponse` composition; add nested objects or document required follow-up calls |
| **RES-03** | `204 No Content` avoided by design | Document for UI: always parse JSON body on success |
| **RES-04** | Intelligence `R-AGG` responses unpaginated | UI must handle full payload or implement client-side virtualization with documented max rows |
| **RES-05** | `Location` response on `201 Created` | Verify all `201` responses include `Location` header per Complete API Spec global conventions |

---

## 5. Error Model Analysis

### 5.1 Strengths (Exemplary)

- RFC 7807 `ProblemDetailResponse` with IMS extensions (`errorCode`, `traceId`, `businessRuleId`).
- Category catalog: `VAL_*`, `AUTH_*`, `AUTHZ_*`, `NF_*`, `CONF_*`, `BIZ_*`, `SYS_*`.
- Field-level `errors[]` array for 400 responses.
- No stack trace leakage policy documented.
- Examples per error category.

### 5.2 Gaps

| ID | Gap | Recommendation |
|----|-----|----------------|
| **ERR-01** | UI error mapping guide missing | Add table: `errorCode` → user message → recoverable action |
| **ERR-02** | `403` vs. `404` for unauthorized resource access | Document security policy: use `404` for cross-tenant/location scope hide vs. `403` — must be consistent |
| **ERR-03** | Validation error `field` path convention for nested arrays | Document JSON Pointer format for UI field highlighting |
| **ERR-04** | Problem `type` URI environment placeholder | Confirm `{environment}` resolution per deployment |

---

## 6. Pagination, Filtering & Search Analysis

### 6.1 Strengths

- Five collection profiles: `P-STD`, `P-OPS`, `P-LOG`, `P-INT`, `R-AGG`, `C-FED`, `B-NST`.
- Global defaults: `page=1`, `pageSize=20`, max 100.
- Cursor pagination for integration feed (API-177).
- Location scope enforced by default on transactional collections.
- Collection endpoint index covers 44 endpoints with profile assignment.

### 6.2 Gaps

| ID | Gap | Recommendation |
|----|-----|----------------|
| **COL-01** | 78 `GET` endpoints but only 44 in collection index | Document which GETs are **single-resource** vs. **collection** in a master matrix for UI |
| **COL-02** | `X-Total-Count` header optional | UI infinite scroll components should use `totalElements` in body as primary |
| **COL-03** | Intelligence `R-AGG` endpoints lack pagination — risk for KPI/shrinkage dashboards | Set hard max rows; return `413` or truncate with warning field |
| **COL-04** | API-089 incorrectly listed as collection with `locationCode` filter under order scope | Fix with C-01 |
| **COL-05** | Pending approval queues fragmented | API-106 (transfers), API-123 (adjustments) — UI needs unified "My Approvals" aggregator endpoint or client-side merge |
| **COL-06** | `sortDirection` without `sortBy` silently ignored | UI should always send both or neither; add lint rule |

---

## 7. Versioning Analysis

### 7.1 Strengths

- URI path versioning (`/api/v1`) — correct for B2B integrations.
- Breaking vs. non-breaking change policy defined.
- Deprecation via `Deprecation` and `Sunset` headers.
- Contract release tag `IMS-API-{major}.{minor}.{patch}`.
- OpenAPI per major version planned.

### 7.2 Issues

| ID | Issue | Recommendation |
|----|-------|----------------|
| **VER-01** | **Health path conflict** | Catalog/DTOs: `/api/v1/health`; SRS-API-008: `/api/health` unversioned — **resolve before gateway config** |
| **VER-02** | Version discovery endpoints not in API catalog | Add to catalog or infrastructure appendix |
| **VER-03** | OpenAPI artifact referenced but not produced | Generate `openapi-v1.yaml` before UI codegen |
| **VER-04** | `X-API-Major-Version` optional header | Document interaction with URL version for UI SDK |

---

## 8. Authentication Analysis

### 8.1 Strengths

- OAuth 2.0 Bearer JWT for users (SVC-01 IdP).
- Client Credentials for integration principals (`INT_SALES`, `INT_MKT`).
- API-173 session validation, API-174 logout defined.
- API-175 health check public (monitoring).

### 8.2 Gaps

| ID | Gap | Recommendation |
|----|-----|----------------|
| **AUTH-01** | No token issuance endpoint in IMS | **Expected** — publish **Frontend Auth Integration Guide** referencing IdP (authorize, token, refresh, silent renew) |
| **AUTH-02** | Logout scope unclear (local vs. IdP session) | Document `logoutAllSessions` behavior and front-channel logout URL |
| **AUTH-03** | Integration token rotation / expiry handling | Document for EXT-01/EXT-07 partners |
| **AUTH-04** | MFA / step-up auth not addressed | Map to IdP capabilities; identify S1/S4 operations requiring step-up |
| **AUTH-05** | No rate limiting specification | Add NFR: per-principal rate limits (especially API-176, API-155, API-157) |

---

## 9. Authorization Analysis

### 9.1 Strengths (Best-in-class for this program)

- Every API mapped to `PERM-xxx` with authorized roles.
- Sensitive operation classification S1–S8.
- Location scope model: `NET`, `LOC`, `NONE`, `SELF`.
- SoD on approval APIs with API-031 pre-check.
- Self-service rules for API-142, API-148, API-149.
- Finance/audit isolation (S4, S5) on valuation and audit endpoints.

### 9.2 Security Concerns

| ID | Concern | Severity | Recommendation |
|----|---------|----------|----------------|
| **SEC-01** | API-089 path/purpose mismatch may expose wrong data scope | **Critical** | Fix endpoint design |
| **SEC-02** | Idempotency optional on stock mutations (S8) | **High** | Make `Idempotency-Key` **required** on API-043, 044, 092, 103, 104, 111, 176 |
| **SEC-03** | Audit export API-157 — bulk sensitive data egress | **High** | Require S5 permission + async job + download token; log all exports |
| **SEC-04** | API-156 audit trail query — no field-level redaction spec | Medium | Document which fields are visible per role |
| **SEC-05** | API-110 blind count — response must never include system quantity | **High** | Add contract test + API gateway response schema validation |
| **SEC-06** | API-031 SoD evaluate — could enumerate user relationships | Medium | Restrict to PERM-013 roles only; rate limit |
| **SEC-07** | API-142 self-read — must enforce `userId === principal.sub` | **High** | Document as mandatory server-side check |
| **SEC-08** | Integration APIs lack mTLS recommendation | Medium | Add to integration architecture: Client Credentials + mTLS for EXT-01/EXT-07 |
| **SEC-09** | PERM-097/100 security monitoring permissions unused | Low | Phase 2 or remove from RBAC matrix until APIs exist |
| **SEC-10** | Health endpoint information disclosure | Low | Ensure `/health` returns minimal info publicly; details behind auth |
| **SEC-11** | `403` on location scope reveals resource existence | Medium | Adopt consistent `{404}` policy for out-of-scope resources |

---

## 10. Critical Findings (Block UI Design)

| ID | Finding | Action Required |
|----|---------|-----------------|
| **C-01** | **API-089 design defect:** Catalog states *"List orders awaiting pick at a fulfillment location"* but path is `/fulfillment/orders/{orderId}/pick-lists/awaiting` (single-order scope). DTO named `ListOrdersAwaitingPickQuery` but requires `orderId` path param. | **Add** `GET /api/v1/fulfillment/pick-lists/awaiting?locationCode=` **or** correct catalog purpose to "list awaiting pick lists for an order" and add separate location queue API |
| **C-02** | **Health endpoint path conflict:** SRS-API-001/002/003/009 use `/api/v1/health`; SRS-API-008 states `/api/health` unversioned | Architecture decision record; update all artifacts to single canonical path |
| **C-03** | **Missing requisition list API** blocks procurement UI (UC-029) | Add `GET /procurement/requisitions` |
| **C-04** | **Return receipt dual path** (API-076 vs. API-128) without canonical guidance | Designate API-128 as canonical; deprecate or restrict API-076 |
| **C-05** | **OpenAPI spec not generated** — UI codegen blocked | Produce `openapi-v1.yaml` from SRS-API-002/003/004/005 |
| **C-06** | **Bulk import approval flow incomplete** (PERM-016 referenced, no API) | Add approval endpoint or job-status workflow |

---

## 11. High-Priority Recommendations

| # | Recommendation | Owner | Before UI |
|---|----------------|-------|-----------|
| 1 | Resolve API-089 and add location-level pick queue | Backend Architect | **Yes** |
| 2 | Normalize health check path across all SRS documents | Backend Architect | **Yes** |
| 3 | Generate OpenAPI 3.0 spec (`openapi-v1.yaml`) | Backend Lead | **Yes** |
| 4 | Publish **Frontend Auth Integration Guide** (IdP OIDC, not IMS login API) | Security Architect | **Yes** |
| 5 | Publish **UI API Client Module Map** (operational vs. intelligence paths) | Backend Architect | **Yes** |
| 6 | Add `GET /procurement/requisitions` collection endpoint | Product Owner + Architect | **Yes** |
| 7 | Expand grouped validation profiles to field-level (15 groups) | Backend Lead | **Yes** |
| 8 | Make `Idempotency-Key` required on all S8 stock mutation APIs | Backend Architect | **Yes** |
| 9 | Add `errorCode` → UI message mapping table to SRS-API-005 | UX + Backend | **Yes** |
| 10 | Document `returnAuthorizationId` → `returnId` lifecycle for returns UI | Domain Architect | **Yes** |
| 11 | Normalize API-089 response wrapper (Paged vs. Bounded) | Backend Lead | **Yes** |
| 12 | Define unified "Approvals Inbox" API or client aggregation pattern for API-106, 123 | Product Owner | Recommended |

---

## 12. Medium-Priority Recommendations (During UI Design)

| # | Recommendation |
|---|----------------|
| 1 | Add version discovery endpoints to catalog (API-182–184) or infrastructure appendix |
| 2 | Enrich `CustomerOrderDetailResponse` with nested reservations/picks/shipments for order detail screen |
| 3 | Standardize search param to `q` across all collections (including API-141 users) |
| 4 | Document `403` vs `404` policy for location-scoped resources |
| 5 | Add rate limiting NFR section to API design package |
| 6 | Complete API Specification Part 2 normalization (API-049–097 compact format → full 18-field) |
| 7 | Add supplier delivery performance read API for purchasing dashboard |
| 8 | Specify API-010 bulk import as `multipart/form-data` with async job pattern |
| 9 | Extend ETag/`If-Match` to all concurrent-sensitive PATCH endpoints |
| 10 | Add PERM-097/100 security monitoring APIs or mark Phase 2 in UI scope |

---

## 13. Low-Priority / v1.1 Backlog

- Flatten deep nesting (`/reservations/{id}/release`) in v2.
- Standardize all updates to `PATCH` (retire `PUT` on API-006).
- Unified approvals aggregator endpoint across modules.
- Webhook/callback alternative to polling for API-177 fulfillment feed.
- Consignment lifecycle APIs beyond API-047 consumption event.
- `GET /reservations` collection endpoint.

---

## 14. UI Design Prerequisites Checklist

Complete these before UI wireframes enter development sprints:

- [ ] **C-01** Pick queue endpoint resolved
- [ ] **C-02** Health path normalized
- [ ] **C-03** Requisition list API added or UI scope adjusted
- [ ] **C-04** Return receipt canonical path documented
- [ ] **C-05** OpenAPI v1 published
- [ ] **C-06** Bulk import approval workflow defined
- [ ] Frontend Auth Integration Guide published
- [ ] UI API Client Module Map published
- [ ] `errorCode` → user message mapping available
- [ ] Returns lifecycle (`returnAuthorizationId` / `returnId`) documented
- [ ] Operational vs. intelligence API routing guide for dashboard screens
- [ ] Collection endpoint master matrix (44 collections + single-resource GETs)

---

## 15. Conclusion

The IMS API design is a **strong foundation** with exceptional authorization modeling and error handling. The primary risks before UI design are **contract inconsistencies** (API-089, health path, return receipt duality), **missing list endpoints** for procurement and warehouse queues, and **absence of machine-readable OpenAPI** for client generation.

**Recommendation:** Hold UI implementation until Critical items C-01 through C-06 are resolved. Parallel track: generate OpenAPI and Frontend Auth Guide while API gaps are remediated.

---

## Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Chief Backend Architect | | | |
| Solution Architect | | | |
| Product Owner | | | |
| Security Architect | | | |
| UI/UX Lead | | | |

*SRS-API-010 | July 6, 2026*
