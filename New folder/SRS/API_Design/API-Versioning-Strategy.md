# API Versioning Strategy
## Inventory Management System

---

## Document Information

| Attribute | Detail |
|-----------|--------|
| **Document ID** | SRS-API-008 |
| **Document Title** | API Versioning Strategy — Inventory Management System |
| **Version** | 1.0 |
| **Status** | Draft |
| **Document Owner** | Senior Backend Architect |
| **Source Documents** | SRS-API-001, SRS-SA-005 (Integration Architecture), SRS-SA-004 (Layered Architecture), ADR backlog item ADR-030 |
| **Date** | July 6, 2026 |
| **Scope** | Public REST APIs under `/api`; internal domain events are governed separately |

### Purpose

Defines how the Inventory Management System **versions, evolves, deprecates, and retires** its REST API surface. Ensures warehouse operations, finance integrations, and external ACL partners (Sales/CRM, Marketing) can adopt changes predictably without disrupting stock integrity or audit trails.

---

## Executive Recommendation

### Recommended Strategy: **URI Path Versioning (`/api/v{major}`)**

| Decision | Choice |
|----------|--------|
| **Primary mechanism** | Major version in URL path — `/api/v1/...`, `/api/v2/...` |
| **Secondary signals** | `Deprecation` and `Sunset` HTTP headers on deprecated endpoints |
| **Contract artifact** | OpenAPI 3 document per major version (`openapi-v1.yaml`, `openapi-v2.yaml`) |
| **Release alignment** | API major version increments only on **breaking** changes |

**Why this fits IMS:**

1. **Already adopted** — All 178 APIs in SRS-API-001 use `/api/v1`; zero migration cost at launch.
2. **Integration-heavy** — EXT-01 (Sales) and EXT-07 (Marketing) partners configure fixed base URLs; path versioning is the most discoverable and gateway-friendly model for B2B ACL.
3. **Operational visibility** — Warehouse mobile clients, API gateways, and WAF rules route and log version explicitly.
4. **Enterprise lifecycle** — Finance and audit consumers need long deprecation windows; a visible major version supports parallel operation of v1 and v2 during migration.
5. **Team scale** — 13 modules share a presentation kernel; path versioning keeps module routing uniform (`/api/v1/inventory/...`, `/api/v1/fulfillment/...`).

**Not recommended for IMS:**

| Strategy | Reason excluded |
|----------|-----------------|
| **Header-only** (`Accept-Version`, custom headers) | Harder for operations to debug; integration partners often miss header requirements |
| **Media type (HATEOAS)** (`application/vnd.ims.v2+json`) | High complexity for 178 endpoints; limited client ecosystem benefit |
| **Query parameter** (`?version=2`) | Cache-unfriendly; easy to omit accidentally on stock-mutation commands |

Header-based negotiation may supplement path versioning for **minor** contract metadata but must not replace the major version in the URL.

---

## 1. Version Format

### 1.1 URL Structure

```
https://{host}/api/v{major}/{resource-path}
```

| Component | Format | Example | Rules |
|-----------|--------|---------|-------|
| **Base path** | `/api` | `/api` | Fixed prefix for all REST APIs |
| **Major version** | `v` + positive integer | `v1`, `v2` | No minor/patch in URL |
| **Resource path** | kebab-case plural nouns | `/inventory/stock-positions` | Unversioned within major |
| **Action sub-paths** | verb noun commands | `/orders/{id}/confirm` | Stable within major version |

**Current baseline:** `v1` — covers APIs API-001 through API-178.

### 1.2 API Release Identifier (Documentation)

Each major version has a **contract release tag** for changelog and OpenAPI publishing:

```
IMS-API-{major}.{minor}.{patch}
```

| Segment | Meaning | Example |
|---------|---------|---------|
| **major** | Breaking change → new `/api/v{n}` | `2` → `/api/v2` |
| **minor** | Backward-compatible addition within same major | `1.3.0` — new optional fields, new endpoints |
| **patch** | Documentation or non-contract fix | `1.3.1` — typo in OpenAPI description |

**Example:** `IMS-API-1.4.0` = fourth minor release of v1 contract (all under `/api/v1`).

### 1.3 Version Discovery Endpoints

| Endpoint | Auth | Response |
|----------|------|----------|
| `GET /api/versions` | Public | Supported major versions, current, deprecated, sunset dates |
| `GET /api/v1/openapi` | Authenticated | OpenAPI 3 spec for v1 |
| `GET /api/v1/changelog` | Authenticated | Human-readable contract changelog |

`GET /api/health` (API-175) remains unversioned for load balancers.

### 1.4 Response Headers (All Versioned APIs)

| Header | When | Example |
|--------|------|---------|
| `X-API-Version` | Always | `1.4.0` (contract release) |
| `X-API-Major-Version` | Always | `1` |
| `Deprecation` | Deprecated endpoint | `true` |
| `Sunset` | Deprecated endpoint | `Sat, 01 Jan 2028 00:00:00 GMT` |
| `Link` | Deprecated endpoint | `<https://api.ims.example/api/v2/products>; rel="successor-version"` |

---

## 2. Backward Compatibility Approach

### 2.1 Compatibility Guarantee

Within a **major version**, IMS guarantees **backward compatibility** for existing clients:

> A client written against contract release `IMS-API-1.0.0` must continue to work against `IMS-API-1.x.x` without code changes.

### 2.2 Non-Breaking (Allowed in Same Major Version)

| Change Type | Rule | Example |
|-------------|------|---------|
| **Add optional request field** | Client may omit | New `correlationId` on command body |
| **Add response field** | Clients must ignore unknown fields | New `lastCountedAt` on stock position |
| **Add new endpoint** | No impact on existing | `GET /api/v1/intelligence/new-report` |
| **Add optional query parameter** | Default preserves prior behavior | New filter `abcClass` on product search |
| **Add enum value** | Only if clients tolerate unknown values | New `holdReason=BONDED` |
| **Relax validation** | Wider acceptance | Increase `pageSize` max from 100 to 200 |
| **Add HTTP header** | Optional on request/response | `X-Trace-Id` |
| **Bug fix** | Correct behavior to match documented contract | Fix ATP calculation matching BR-001 |

### 2.3 Breaking (Requires New Major Version)

See Section 4. Same major version must **never** include breaking changes.

### 2.4 Client Responsibilities (Tolerant Reader Pattern)

| Rule | Rationale |
|------|-----------|
| Ignore unknown JSON properties in responses | Forward compatibility |
| Do not depend on response field ordering | JSON is unordered |
| Treat new enum values as opaque or map to `UNKNOWN` | Enum extension |
| Use `errorCode` not HTTP status alone | Stable error handling (SRS-API-005) |
| Pin integration tests to contract release tag | Detect unintended drift |

### 2.5 DTO and OpenAPI Versioning

| Artifact | Versioning |
|----------|------------|
| Request DTOs (SRS-API-002) | Annotated with `since: IMS-API-1.x.0` per field |
| Response DTOs (SRS-API-003) | New fields marked `optional` in OpenAPI |
| Validation rules (SRS-API-004) | Stricter validation is **breaking** unless behind new optional field |
| Error codes (SRS-API-005) | New codes are non-breaking; removing/renaming codes is breaking |

### 2.6 Database vs API Versioning

API major version is **independent** of database schema version. The application layer maps v1 and v2 DTOs to the current domain model via anti-corruption adapters in the presentation layer — domain aggregates do not fork per API version.

---

## 3. Deprecation Policy

### 3.1 Deprecation Triggers

An endpoint or field is **deprecated** when:

1. A successor exists in the same or next major version
2. A module is refactored and the endpoint is superseded
3. A business process is retired (with BRD approval)
4. Security or compliance requires replacement

Deprecation does **not** remove functionality — it signals intent to remove.

### 3.2 Deprecation Timeline

| Consumer Type | Minimum Notice | Parallel Support |
|-------------|----------------|------------------|
| **Internal UI (Angular)** | 1 minor release (≈ 6 weeks) | Same major version |
| **Internal modules / BFF** | 1 minor release | Same major version |
| **External integration (EXT-01, EXT-07)** | **12 months** from deprecation announcement | v1 + v2 parallel |
| **Partner/custom API consumers** | **12 months** | v1 + v2 parallel |
| **Deprecated major version (v1 entire)** | **18 months** after v2 GA | Full v1 stack operational |

### 3.3 Deprecation Process

```
1. Mark deprecated in OpenAPI (deprecated: true)
2. Add Deprecation + Sunset headers on responses
3. Log Warning on each deprecated call (metric: api.deprecated.calls)
4. Publish changelog entry and notify integration owners
5. Update SRS-API-001 with DEPRECATED badge
6. Remove only after sunset date + zero critical consumers
```

### 3.4 Deprecation Documentation Requirements

Each deprecation entry must include:

| Field | Content |
|-------|---------|
| **Deprecated artifact** | Endpoint, field, or enum value |
| **Since release** | `IMS-API-1.x.0` |
| **Sunset date** | ISO date |
| **Successor** | Replacement endpoint or migration path |
| **Migration guide** | Request/response mapping |
| **Business owner sign-off** | Product Owner or Integration Architect |

### 3.5 Field-Level Deprecation

Prefer **field-level** deprecation before endpoint removal:

```json
{
  "sku": "WIDGET-01",
  "legacyBarcode": "12345",
  "_deprecatedFields": ["legacyBarcode"]
}
```

OpenAPI `deprecated: true` on the field. Field removed only in next **major** version.

---

## 4. Breaking Change Policy

### 4.1 Definition

A change is **breaking** if an existing conforming client would fail or behave differently without modification.

### 4.2 Breaking Change Catalog

| # | Breaking Change | Example |
|---|-----------------|---------|
| B1 | Remove endpoint | Delete `GET /api/v1/legacy-report` |
| B2 | Remove request/response field | Remove `mrslThresholdDays` |
| B3 | Rename field or endpoint | `orderedQuantity` → `quantity` |
| B4 | Change field type | `quantity` string → number |
| B5 | Change field semantics | `atp` includes quarantined stock |
| B6 | Add required request field | New required `reasonCode` on POST |
| B7 | Tighten validation | SKU max length 50 → 30 |
| B8 | Change URL path or HTTP method | `PATCH` → `PUT` for product update |
| B9 | Change authentication model | Bearer scope requirements |
| B10 | Change error code for same condition | `BIZ_INSUFFICIENT_ATP` renamed |
| B11 | Change pagination defaults materially | Default `pageSize` 20 → 5 with no opt-out |
| B12 | Remove enum value | Remove `DISCONTINUED` status |
| B13 | Change idempotency behavior | Idempotency key scope change |
| B14 | Change HTTP status for same outcome | `201` → `200` for create |

### 4.3 Breaking Change Approval

| Step | Owner | Gate |
|------|-------|------|
| 1. Propose RFC | Backend Architect | Impact analysis on 178 APIs + integrations |
| 2. Classify breaking/non-breaking | API governance board | Check against §2.2 / §4.2 |
| 3. Business impact review | Product Owner | Operational/finance impact |
| 4. Integration impact review | Integration Architect | EXT-01, EXT-07 partner notice |
| 5. Security review | Security Engineer | Auth/RBAC changes |
| 6. Approve major version bump | Tech Lead + PO | RFC signed |
| 7. Implement v{n+1} parallel to v{n} | Development squads | No removal of v{n} until sunset |

### 4.4 Emergency Breaking Changes

Security vulnerabilities (e.g., data exposure, auth bypass) may require **accelerated** breaking changes:

- Minimum notice: **30 days** for integrations (unless active exploit)
- Requires CFO/COO notification for finance-facing APIs
- Documented as `SECURITY` in changelog

---

## 5. Version Lifecycle

### 5.1 States

```
PLANNED → BETA → CURRENT → DEPRECATED → SUNSET → RETIRED
```

| State | `/api/v1` active | Headers | New clients |
|-------|------------------|---------|-------------|
| **PLANNED** | No | — | Not accepted |
| **BETA** | Preview path optional | `X-API-Version: 2.0.0-beta` | Opt-in partners only |
| **CURRENT** | Yes | Standard | Default for new integrations |
| **DEPRECATED** | Yes | `Deprecation: true` | Discouraged; migrate to CURRENT |
| **SUNSET** | Yes (limited) | `Sunset` date passed warning | Existing only; no new keys |
| **RETIRED** | **No** | `410 Gone` | Not accepted |

### 5.2 Multi-Version Operation

During migration from v1 to v2:

```
                    ┌─────────────────┐
  Client v1 ───────►│  API Gateway    │──────► /api/v1/* → v1 Controllers
                    │  (route by path)│
  Client v2 ───────►│                 │──────► /api/v2/* → v2 Controllers
                    └────────┬────────┘
                             │
                    Shared Application + Domain Layer
                    (DTO adapters per major version)
```

- **v1 and v2 share** domain services and aggregates — only presentation DTOs and controllers differ.
- Stock mutations from v1 and v2 use the **same** domain commands — no duplicate business logic.
- Integration tests run against **both** versions during overlap period.

### 5.3 Version Support Matrix (Illustrative)

| Major Version | Status | GA Date | Deprecation | Sunset | Notes |
|---------------|--------|---------|-------------|--------|-------|
| **v1** | CURRENT | Jul 2026 | TBD | TBD | Initial 178-API catalog |
| **v2** | PLANNED | — | — | — | First major when breaking need arises |

---

## 6. Implementation Standards

### 6.1 Code Organization

```
presentation/
  api/
    v1/
      product/ProductControllerV1.java
      inventory/StockPositionControllerV1.java
    v2/
      product/ProductControllerV2.java
    common/
      VersionFilter.java          # X-API-Version headers
      DeprecationInterceptor.java # Deprecation/Sunset headers
```

### 6.2 Spring Boot Routing

```java
@RestController
@RequestMapping("/api/v1/products")
public class ProductControllerV1 { ... }
```

Gateway rule: `/api/v1/**` and `/api/v2/**` route to same service; unknown version → `404` with available versions in body.

### 6.3 Contract Testing

| Test Type | Scope |
|-----------|-------|
| **OpenAPI diff** | CI fails on breaking change in same major (oasdiff) |
| **Consumer-driven contracts** | EXT-01, EXT-07 pact tests pinned to `IMS-API-1.x.0` |
| **Regression suite** | Golden JSON fixtures per release tag |

### 6.4 Changelog Discipline

Every API change requires an entry in `CHANGELOG-API.md`:

```markdown
## [IMS-API-1.5.0] - 2026-09-01
### Added
- API-179 `GET /api/v1/intelligence/reservation-utilization` (non-breaking)

### Deprecated
- `GET /api/v1/intelligence/alerts` — use API-158 filters instead; sunset 2027-09-01
```

---

## 7. Versioning by API Category

| Category | Version Sensitivity | Guidance |
|----------|-------------------|----------|
| **Stock mutations** (reserve, ship, transfer) | High | Breaking changes require v2; never alter semantics in minor |
| **Approvals** (adjustment, PO, transfer) | High | Error codes and status transitions are contract |
| **Master data** (product, location) | Medium | Additive fields OK; identifier format changes are breaking |
| **Read/query** (intelligence, lists) | Medium | New filters OK; removing filters is breaking |
| **Integration ACL** (API-176–178) | **Highest** | 12-month deprecation; partner sign-off on any change |
| **Platform** (health, session) | Low | Health unversioned; session follows auth provider |

---

## 8. Relationship to Other Versioning Concerns

| Concern | Versioning mechanism | Document |
|---------|---------------------|----------|
| **REST API** | URI `/api/v{major}` | This document |
| **Domain events** | Event type version + upcasters | ADR / event schema catalog |
| **Database schema** | Flyway migrations | SRS-DB |
| **RBAC permissions** | Additive PERM-xxx only in minor | rbac-matrix.md |
| **Error codes** | Additive in minor; remove in major | SRS-API-005 |

---

## 9. Decision Summary

| Question | Decision |
|----------|----------|
| **Which versioning strategy?** | **URI path major versioning** (`/api/v1`, `/api/v2`) |
| **Version format?** | `v{major}` in URL; `IMS-API-{major}.{minor}.{patch}` for contract releases |
| **Backward compatibility?** | Guaranteed within major; tolerant reader; additive-only minors |
| **Deprecation?** | `Deprecation`/`Sunset` headers; 12-month external notice; documented successors |
| **Breaking changes?** | New major version only; RFC + governance approval; parallel operation period |
| **When to create v2?** | First catalogued B1–B14 breaking change that cannot be avoided |

---

## Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Senior Backend Architect | | | |
| Solution Architect | | | |
| Tech Lead | | | |
| Product Owner | | | |
| Integration Architect | | | |

---

*End of API Versioning Strategy*

*Document ID: SRS-API-008 | Version 1.0 | July 6, 2026*
