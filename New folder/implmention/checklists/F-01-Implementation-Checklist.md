# Implementation Checklist — F-01: Product Catalog Management

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | F-01 |
| **Feature Name** | Product Catalog Management |
| **Document Type** | Technical Lead Implementation Checklist |
| **Feature dependencies** | F-27 |
| **Default status** | Not Started |
| **Task count** | 26 |

---

## Checklist

| Task ID | Feature | Task description | Layer | Priority | Status | Dependencies |
|---------|---------|------------------|-------|----------|--------|--------------|
| `CHK-01-DB-01` | F-01 | Create Flyway schema `catalog` and baseline migration | Database | P0 | Not Started | F-27 platform DB |
| `CHK-01-DB-02` | F-01 | Create table `catalog.products` with SKU UK, lifecycle CHECK, version, audit columns | Database | P0 | Not Started | CHK-01-DB-01 |
| `CHK-01-DB-03` | F-01 | Create table `catalog.product_identifiers` with FK to products and unique identifier | Database | P0 | Not Started | CHK-01-DB-02 |
| `CHK-01-DB-04` | F-01 | Add indexes on products(sku), products(lifecycle_status), products(product_name) | Database | P1 | Not Started | CHK-01-DB-02 |
| `CHK-01-DB-05` | F-01 | Grant app role DML on catalog tables; revoke DDL from app role | Database | P1 | Not Started | CHK-01-DB-03 |
| `CHK-01-BE-01` | F-01 | Implement Product aggregate root + ProductIdentifier entity/VO | Backend | P0 | Not Started | CHK-01-DB-02 |
| `CHK-01-BE-02` | F-01 | Implement value objects: ProductSku, LifecycleStatus, UnitOfMeasure, Category | Backend | P0 | Not Started | CHK-01-BE-01 |
| `CHK-01-BE-03` | F-01 | Implement ProductRepository (Spring Data JPA) | Backend | P0 | Not Started | CHK-01-BE-01 |
| `CHK-01-BE-04` | F-01 | Implement Request/Response DTOs + MapStruct mappers for product APIs | Backend | P0 | Not Started | CHK-01-BE-02 |
| `CHK-01-BE-05` | F-01 | Implement Bean Validation + domain validators (VR-001/007, mandatory fields) | Backend | P0 | Not Started | CHK-01-BE-04 |
| `CHK-01-BE-06` | F-01 | Implement ProductCatalogService (create/update/search/lifecycle) | Backend | P0 | Not Started | CHK-01-BE-03, CHK-01-BE-05 |
| `CHK-01-BE-07` | F-01 | Implement DuplicateDetectionService + resolve API | Backend | P1 | Not Started | CHK-01-BE-06 |
| `CHK-01-BE-08` | F-01 | Implement ProductController API-001–005, 007–009 with Problem Details errors | Backend | P0 | Not Started | CHK-01-BE-06 |
| `CHK-01-BE-09` | F-01 | Enforce PRODUCT_MANAGE / PRODUCT_VIEW permissions on endpoints | Backend | P0 | Not Started | F-27, CHK-01-BE-08 |
| `CHK-01-FE-01` | F-01 | Add child routes: catalog/new, catalog/:sku, catalog/:sku/edit | Frontend | P0 | Not Started | F-27 auth |
| `CHK-01-FE-02` | F-01 | Implement ProductApiService (HttpClient) replacing mocks | Frontend | P0 | Not Started | CHK-01-BE-08 |
| `CHK-01-FE-03` | F-01 | Implement ProductFacade with signals for list/filters/selected/saveState | Frontend | P0 | Not Started | CHK-01-FE-02 |
| `CHK-01-FE-04` | F-01 | Build Product list/create/edit pages (UI-005) with reactive forms + validation | Frontend | P0 | Not Started | CHK-01-FE-03 |
| `CHK-01-FE-05` | F-01 | Build lifecycle change + duplicate resolution UI flows | Frontend | P1 | Not Started | CHK-01-FE-04 |
| `CHK-01-FE-06` | F-01 | Map RFC 7807 field errors to form controls | Frontend | P1 | Not Started | CHK-01-FE-04 |
| `CHK-01-TE-01` | F-01 | API contract tests for API-001–005, 009 (happy + 400/403/409) | Testing | P0 | Not Started | CHK-01-BE-08 |
| `CHK-01-TE-02` | F-01 | Unit tests for lifecycle transitions and duplicate SKU invariant | Testing | P0 | Not Started | CHK-01-BE-06 |
| `CHK-01-TE-03` | F-01 | UI/E2E: create product, edit, lifecycle change (FAC-01-H1/H2/H3) | Testing | P1 | Not Started | CHK-01-FE-04 |
| `CHK-01-TE-04` | F-01 | Permission test: non-manager denied create (FAC-01-P1) | Testing | P0 | Not Started | CHK-01-BE-09 |
| `CHK-01-DO-01` | F-01 | Update OpenAPI for product endpoints | Documentation | P1 | Not Started | CHK-01-BE-08 |
| `CHK-01-DO-02` | F-01 | Mark FAC-01 checklist items with evidence links in AC file | Documentation | P2 | Not Started | CHK-01-TE-03 |

## Layer summary

| Layer | Count |
|-------|-------|
| Database | 5 |
| Backend | 9 |
| Frontend | 6 |
| Testing | 4 |
| Documentation | 2 |

## Priority summary

| Priority | Meaning | Count |
|----------|---------|-------|
| P0 | MVP critical / blocking | 18 |
| P1 | MVP important | 7 |
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

- Implementation plan: `implmention/plans/` (F-01)
- Acceptance criteria: `implmention/acceptance-criteria/F-01-Acceptance-Criteria.md`
- Sprint plan: `implmention/IMS-Sprint-Plan.md`

*Technical Lead checklist — F-01*
