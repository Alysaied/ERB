# IMS Technical Implementation Plans

| Attribute | Detail |
|-----------|--------|
| **Document ID** | IMPL-PLAN-INDEX |
| **Perspective** | Technical Lead |
| **Date** | July 11, 2026 |
| **Location** | `implmention/plans/` |

## What was delivered

Complete **per-feature implementation plans** for all **30 business features (F-01–F-30)**.

Each plan includes:

1. Feature overview  
2. Business goal  
3. User stories  
4. Acceptance criteria  
5. **Database tasks** — tables, relationships, constraints, Flyway migrations  
6. **Backend tasks** — entities, VOs, repositories, DTOs, validation, services, controllers, exceptions, security  
7. **Frontend tasks** — routes, pages, components, models, services, forms, validation, state  
8. **API contract** — endpoints, request/response DTOs, error responses  
9. **QA tasks** — functional, API, UI tests  
10. **Dependencies** — required previous features  

## Start here

| Doc | Purpose |
|-----|---------|
| [plans/README.md](plans/README.md) | Index of all 30 plans + squad ownership |
| [IMS-Implementation-Features.md](IMS-Implementation-Features.md) | Business feature catalog |
| [IMS-Feature-Dependency-Map.md](IMS-Feature-Dependency-Map.md) | Dependency map & optimal order |

## Implementation order (reminder)

Start with **F-27 → F-28 → F-01 → F-02 → F-03 → …** per the dependency map. Do not begin feature UI polish before auth/HTTP/facade foundations.

## Stack assumptions

Java 21 · Spring Boot 3.x / Modulith · JPA · Flyway · PostgreSQL 16 · Angular 19 · RFC 7807 errors · OAuth2/OIDC JWT
