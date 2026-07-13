# Technology Stack Recommendation
## Inventory Management System

---

## Document Information

| Attribute | Detail |
|-----------|--------|
| **Document ID** | SRS-SA-007 |
| **Document Title** | Technology Stack Recommendation — Inventory Management System |
| **Version** | 1.0 |
| **Status** | Draft |
| **Document Owner** | Senior Solution Architect |
| **Prepared For** | Steering committee, delivery leads, development squads, DevOps, and security |
| **Date** | July 6, 2026 |
| **Classification** | Internal — Architecture Confidential |
| **Scope** | Technology selection aligned to approved architecture — version pinning deferred to implementation standards |

### Related Documents

| Document | ID | Relationship |
|----------|-----|--------------|
| Architecture Vision | SRS-SA-001 | Modular monolith, event-driven, CQRS |
| Architecture Style Recommendation | SRS-SA-002 | Clean/Hexagonal per module |
| System Modules Design | SRS-SA-003 | 13 bounded-context modules |
| Layered Architecture Design | SRS-SA-004 | Layer placement |
| Integration Architecture Design | SRS-SA-005 | Sync/async, outbox pattern |
| Cross-Cutting Concerns | SRS-SA-006 | Security, caching, transactions |
| Non-Functional Requirements | 204 NFRs | Performance, security, availability constraints |

### Stakeholder Technology Mandates

The following technologies are **organizationally mandated** for this initiative:

| Mandate | Technology |
|---------|------------|
| Backend framework | **Java + Spring** |
| Frontend framework | **Angular** |
| Database | **PostgreSQL** |

All other selections complement these mandates and align with the approved modular monolith architecture.

### Document Purpose

This document recommends a complete technology stack for the Inventory Management System. For each technology it provides purpose, selection rationale, alternatives considered, and trade-offs — enabling informed approval before project bootstrap.

---

## 1. Stack Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  FRONTEND          Angular 19 │ Angular Material │ TypeScript │ RxJS         │
├─────────────────────────────────────────────────────────────────────────────┤
│  API               REST (JSON) │ OpenAPI 3 │ Spring MVC Controllers        │
├─────────────────────────────────────────────────────────────────────────────┤
│  BACKEND           Java 21 LTS │ Spring Boot 3.x │ Spring Modulith          │
│                    Spring Security │ Spring Data JPA │ MapStruct             │
├─────────────────────────────────────────────────────────────────────────────┤
│  MESSAGING (MVP)   Spring Application Events │ Transactional Outbox (PG)   │
│  MESSAGING (Ph.2+) RabbitMQ or Apache Kafka (deferred decision)            │
├─────────────────────────────────────────────────────────────────────────────┤
│  CACHE             Redis (ATP hot path, session optional)                   │
├─────────────────────────────────────────────────────────────────────────────┤
│  DATABASE          PostgreSQL 16 │ Flyway migrations │ schema-per-module    │
├─────────────────────────────────────────────────────────────────────────────┤
│  SECURITY          Spring Security 6 │ OAuth 2.0 / OIDC │ JWT Resource Srv │
├─────────────────────────────────────────────────────────────────────────────┤
│  OBSERVABILITY     Micrometer │ Prometheus │ Grafana │ Structured logging   │
├─────────────────────────────────────────────────────────────────────────────┤
│  BUILD             Maven (multi-module) │ GitHub Actions / Azure DevOps CI │
├─────────────────────────────────────────────────────────────────────────────┤
│  TESTING           JUnit 5 │ Mockito │ Testcontainers │ ArchUnit │ Cypress │
├─────────────────────────────────────────────────────────────────────────────┤
│  CONTAINERIZATION  Docker │ Docker Compose (dev) │ Kubernetes (prod Ph.2+)│
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Backend

### 2.1 Java 21 (LTS)

| Aspect | Detail |
|--------|--------|
| **Purpose** | Primary programming language for all server-side domain, application, and infrastructure code |
| **Why selected** | Mandated Java ecosystem; Java 21 is the current long-term support release with virtual threads (Project Loom) beneficial for I/O-bound warehouse API workloads; mature tooling and hiring pool for enterprise distribution/retail sector |
| **Alternatives considered** | Java 17 LTS (still supported but misses virtual threads maturity); Kotlin on JVM (concise but splits team skill set) |
| **Trade-offs** | (+) LTS stability, records/pattern matching, virtual threads for concurrency; (−) Slightly newer runtime than Java 17 — verify corporate JDK approval |

---

### 2.2 Spring Boot 3.x

| Aspect | Detail |
|--------|--------|
| **Purpose** | Application framework — dependency injection, auto-configuration, REST API, transaction management, actuator health endpoints, integration with entire Spring ecosystem |
| **Why selected** | Mandated Spring stack; de facto enterprise standard; native support for security, data access, events, and testing; aligns with Clean Architecture via clear bean wiring of ports and adapters |
| **Alternatives considered** | Quarkus (faster startup, smaller footprint — less mature Modulith support); Micronaut (compile-time DI — smaller community for DDD patterns); Plain Spring Framework without Boot (more boilerplate, slower bootstrap) |
| **Trade-offs** | (+) Rapid development, extensive documentation, team familiarity; (−) Heavier runtime than Quarkus; requires discipline to avoid anemic Spring MVC + JPA anti-pattern — mitigated by Modulith and layered architecture |

---

### 2.3 Spring Modulith

| Aspect | Detail |
|--------|--------|
| **Purpose** | Enforces **modular monolith** boundaries — 13 bounded-context modules as separate Maven modules with compile-time dependency verification and module-scoped application events |
| **Why selected** | Directly implements SRS-SA-002 (modular monolith) and SRS-SA-003 (13 modules); provides `ApplicationModuleTest` to verify acyclic module dependencies; supports event publication APIs and JDBC event registry for outbox; avoids premature microservices while preserving decomposition path |
| **Alternatives considered** | Manual package-by-feature with ArchUnit only (works but no first-class event/outbox support); Microservices with Spring Cloud (rejected — ORC-04, BC-01); OSGi (obsolete complexity) |
| **Trade-offs** | (+) Architecture-as-code module boundaries; event infrastructure built-in; (−) Relatively newer Spring project — smaller reference base than core Spring Boot; team training required |

---

### 2.4 Spring Web (Spring MVC) + REST

| Aspect | Detail |
|--------|--------|
| **Purpose** | Presentation layer — expose REST JSON APIs for Angular SPA, mobile warehouse clients, and Phase 2 external integrations |
| **Why selected** | Standard Spring Boot stack; synchronous request-reply for ATP lookup (NFR-PERF-002, 2s target); well-understood by enterprise teams; integrates with Spring Security filter chain |
| **Alternatives considered** | Spring WebFlux (reactive — adds complexity without clear benefit for CRUD + domain-heavy workloads); gRPC (efficient but poor browser compatibility for Angular); GraphQL (flexible queries but overkill for defined use cases) |
| **Trade-offs** | (+) Simple mental model, excellent tooling, OpenAPI integration; (−) Thread-per-request model — mitigated by Java 21 virtual threads and connection pool tuning |

---

### 2.5 MapStruct

| Aspect | Detail |
|--------|--------|
| **Purpose** | Compile-time mapping between presentation DTOs, application commands/queries, and domain objects — keeps mapping out of controllers and handlers |
| **Why selected** | Type-safe, zero-reflection overhead; aligns with Clean Architecture boundary mapping (SRS-SA-004); reduces boilerplate across 48 use cases |
| **Alternatives considered** | ModelMapper (runtime reflection — harder to debug); Manual mapping (verbose, error-prone at scale); Dozer (legacy, maintenance declining) |
| **Trade-offs** | (+) Fast, compile-time errors, readable generated code; (−) Annotation processor setup; learning curve for complex mappings |

---

### 2.6 Springdoc OpenAPI

| Aspect | Detail |
|--------|--------|
| **Purpose** | Auto-generate OpenAPI 3 specification from Spring MVC controllers — API contract documentation and Angular client generation |
| **Why selected** | Standard for Spring Boot 3; supports contract-first collaboration between frontend and backend squads; enables Phase 2 CRM integration specification |
| **Alternatives considered** | Springfox (unmaintained, incompatible with Spring Boot 3); Manual OpenAPI YAML (high maintenance) |
| **Trade-offs** | (+) Always in sync with code; Swagger UI for QA; (−) Generated spec may need annotation tuning for clean contracts |

---

## 3. Frontend

### 3.1 Angular 19

| Aspect | Detail |
|--------|--------|
| **Purpose** | Single-page application framework for office users (purchasing, CS, management), warehouse web views, and system administration — all role-based IMS screens |
| **Why selected** | **Mandated** frontend framework; enterprise-grade structure (modules, dependency injection, routing); strong TypeScript integration; long-term Google backing; suits large multi-team IMS with 90 functional requirements and role-based UI |
| **Alternatives considered** | React (larger ecosystem but not mandated); Vue (lighter but less enterprise governance tooling); Blazor (requires .NET stack divergence) |
| **Trade-offs** | (+) Opinionated structure aids consistency across squads; built-in routing, forms, HTTP; (−) Steeper learning curve than React; larger bundle — mitigated by lazy-loaded feature modules per bounded context |

---

### 3.2 TypeScript 5.x

| Aspect | Detail |
|--------|--------|
| **Purpose** | Typed language for Angular — compile-time safety for API contracts, form models, and state |
| **Why selected** | Default and recommended language for Angular; reduces runtime errors in complex inventory forms (receipt lines, count entries, order lines) |
| **Alternatives considered** | JavaScript (no type safety — unacceptable for 90 FRs scale) |
| **Trade-offs** | (+) IDE support, refactoring safety; (−) Compilation step, type maintenance |

---

### 3.3 Angular Material

| Aspect | Detail |
|--------|--------|
| **Purpose** | UI component library — tables, forms, dialogs, navigation, data grids for inventory screens, dashboards, and approval workflows |
| **Why selected** | Official Angular component library; accessible (WCAG); consistent enterprise look; data table and paginator suit stock inquiry and movement history screens |
| **Alternatives considered** | PrimeNG (richer data components but third-party); NG-ZORRO (Ant Design — less common in Western enterprise); Custom CSS (slow, inconsistent) |
| **Trade-offs** | (+) Maintained by Angular team, theming support; (−) Material Design aesthetic may need customization for corporate branding |

---

### 3.4 RxJS + Angular Signals (Hybrid)

| Aspect | Detail |
|--------|--------|
| **Purpose** | Reactive state and async data flow — HTTP API calls, real-time dashboard refresh, form debounce on SKU search (NFR-PERF-002) |
| **Why selected** | RxJS is Angular's native async model; Angular 19 signals for local component state reduce boilerplate; hybrid approach suits ATP lookup streams and alert subscriptions |
| **Alternatives considered** | NgRx (full Redux — overkill for MVP, adds ceremony); Plain promises (poor composition for complex UI flows) |
| **Trade-offs** | (+) Powerful composition for search-as-you-type ATP; (−) RxJS learning curve — mitigate with shared service patterns and limited operator set |

---

### 3.5 Angular PWA (Progressive Web App) — Warehouse Mobile

| Aspect | Detail |
|--------|--------|
| **Purpose** | Installable web app for warehouse scanners and mobile devices — put-away, pick, cycle count without native app store deployment |
| **Why selected** | BRD constraint TEC-03 (online MVP, no offline); PWA provides home-screen install, responsive layout, and camera/barcode API access on modern devices; single Angular codebase serves office and warehouse |
| **Alternatives considered** | Native Android/iOS (higher cost, two codebases — BC-01); Ionic/Capacitor (adds layer — consider Phase 2 if scanner hardware integration deepens) |
| **Trade-offs** | (+) One codebase, faster MVP, no app store; (−) Limited offline (acceptable per TEC-03); scanner hardware integration may need Capacitor plugin in Phase 2 |

---

## 4. Database

### 4.1 PostgreSQL 16

| Aspect | Detail |
|--------|--------|
| **Purpose** | Primary relational database — transactional write store for all 13 modules, transactional outbox table, CQRS read projections, audit trail storage |
| **Why selected** | **Mandated** database; ACID compliance critical for Stock Position invariants; excellent JSONB support for event payloads and flexible audit metadata; row-level locking for reservation contention; mature replication for read scaling; open source aligns with BC-01 fixed budget |
| **Alternatives considered** | Microsoft SQL Server (licensing cost under BC-01); MySQL (weaker JSON and constraint tooling); Oracle (cost, overkill for mid-sized distribution); MongoDB (document model conflicts with aggregate transactional integrity) |
| **Trade-offs** | (+) ACID, JSONB, partial indexes, logical replication, strong ecosystem; (−) Horizontal write scaling limited — acceptable for modular monolith MVP scale; team must manage vacuum/autovacuum tuning |

---

### 4.2 Schema-per-Module (PostgreSQL Schemas)

| Aspect | Detail |
|--------|--------|
| **Purpose** | Logical data isolation — each bounded-context module owns tables in a dedicated PostgreSQL schema (`catalog`, `balance`, `fulfillment`, etc.) enforcing SRS-SA-003 module boundary rule MB-07 |
| **Why selected** | Single PostgreSQL instance (operational simplicity ORC-04) with module ownership boundaries; prevents cross-module JOIN temptation; supports per-module Flyway migration scripts |
| **Alternatives considered** | Single flat schema (no boundary enforcement); Database-per-module (microservices pattern — rejected); Separate databases per module (ops overhead) |
| **Trade-offs** | (+) Module ownership clear, single backup target, ACID within instance; (−) Discipline required — no cross-schema FKs except shared kernel reference tables |

---

### 4.3 Flyway

| Aspect | Detail |
|--------|--------|
| **Purpose** | Version-controlled database migration — schema evolution per module, repeatable across environments and location rollouts |
| **Why selected** | SQL-first migrations align with DBA review practices; Spring Boot native integration; per-module migration locations map to Spring Modulith structure |
| **Alternatives considered** | Liquibase (XML/YAML abstraction — more flexible but heavier); Hibernate `ddl-auto` (prohibited for production — no governance) |
| **Trade-offs** | (+) Simple, auditable SQL scripts, CI integration; (−) No automatic rollback — requires forward-fix migration discipline |

---

### 4.4 Redis 7 (Supplementary Cache Store)

| Aspect | Detail |
|--------|--------|
| **Purpose** | In-memory cache for ATP hot-path queries (NFR-PERF-002), optional session store, rate limiting counters — **not** system of record |
| **Why selected** | Sub-millisecond read for high-frequency SKU availability lookups; event-driven invalidation from Balance module domain events (SRS-SA-006 caching rules); offloads PostgreSQL read pressure during peak season (NFR-AVL-003) |
| **Alternatives considered** | Caffeine (in-process only — invalid in multi-instance deployment); PostgreSQL materialized views alone (insufficient for 2s SLA under concurrent load); Hazelcast (heavier operational footprint) |
| **Trade-offs** | (+) Proven, fast, TTL and pub/sub for invalidation; (−) Additional infrastructure component; cache staleness risk — mitigated by event invalidation and `asOf` timestamp |

---

## 5. ORM

### 5.1 Hibernate ORM 6 (via Spring Data JPA)

| Aspect | Detail |
|--------|--------|
| **Purpose** | Object-relational mapping — persist and hydrate domain aggregates via repository implementations in infrastructure layer; **not** exposed to domain layer |
| **Why selected** | Default JPA provider in Spring Boot 3; mature PostgreSQL dialect; supports optimistic locking (`@Version`) for Stock Position contention; Spring Data JPA reduces repository boilerplate; team familiarity in Java enterprise |
| **Alternatives considered** | **MyBatis** (SQL-centric — more control but mapping drifts from domain model); **jOOQ** (excellent for complex queries and CQRS read side — consider supplement for Intelligence module); **EclipseLink** (less Spring community momentum); **Raw JDBC** (too low-level for 18 aggregates) |
| **Trade-offs** | (+) Productivity, Spring integration, optimistic locking, auditing (`@CreatedBy`); (−) Risk of anemic domain model and lazy-loading leaks — **mitigated by**: aggregates mapped explicitly, repository interfaces in domain, no entity exposure past infrastructure, ArchUnit rules |

---

### 5.2 Spring Data JPA (Repository Abstraction)

| Aspect | Detail |
|--------|--------|
| **Purpose** | Implement `IStockPositionRepository` and other domain repository ports — query methods, custom `@Query` for complex reads, pagination for movement history |
| **Why selected** | Standard Spring stack; reduces CRUD boilerplate for master data modules (Catalog, Network, Governance); integrates with `@Transactional` unit of work |
| **Alternatives considered** | Plain Hibernate Session API (more verbose); Spring Data JDBC (no lazy loading — simpler but less aggregate mapping support) |
| **Trade-offs** | (+) Convention over configuration; (−) Derived query methods can hide expensive queries — require query review and EXPLAIN analysis for ATP paths |

---

### 5.3 jOOQ (Supplementary — Intelligence Read Side)

| Aspect | Detail |
|--------|--------|
| **Purpose** | Type-safe SQL for **CQRS read projections** in M-13 Intelligence — complex KPI queries, audit trail search, dashboard aggregations without loading JPA entities |
| **Why selected** | Reporting queries must not burden JPA entity model (AR-10); jOOQ generates type-safe SQL from PostgreSQL schema; complements JPA on write side |
| **Alternatives considered** | Native SQL in `@Query` (untyped, error-prone); PostgreSQL views only (limited composability in application) |
| **Trade-offs** | (+) Performance, type safety for read models; (−) Second data access pattern — limit to Intelligence module only |

---

## 6. Security

### 6.1 Spring Security 6

| Aspect | Detail |
|--------|--------|
| **Purpose** | Application security framework — authentication filter chain, authorization rules, CSRF protection, method-level security, session management |
| **Why selected** | Industry standard for Spring Boot; implements SRS-SA-006 authentication and authorization placement; integrates with OAuth2/OIDC resource server; supports location-scoped permission expressions |
| **Alternatives considered** | Apache Shiro (less Spring-native); Custom JWT filter (reinventing maintained library); Keycloak adapters deprecated in favor of OAuth2 resource server pattern |
| **Trade-offs** | (+) Comprehensive, well-documented, NFR-SEC alignment; (−) Configuration complexity — mitigate with shared security module and tested config |

---

### 6.2 OAuth 2.0 / OpenID Connect (OIDC)

| Aspect | Detail |
|--------|--------|
| **Purpose** | Enterprise SSO integration with identity provider (SVC-01) — Entra ID, Okta, or LDAP-federated OIDC; JWT bearer tokens for Angular SPA and API |
| **Why selected** | NFR-SEC-001 (unique user authentication); no shared accounts; standard protocol supported by all enterprise IdPs; Angular `angular-oauth2-oidc` library mature |
| **Alternatives considered** | SAML 2.0 (legacy, XML-heavy — still supported but OIDC preferred for SPA); Session-only form login (no SSO, poor for enterprise); API keys (insufficient for user attribution) |
| **Trade-offs** | (+) Enterprise SSO, token-based stateless API, refresh token flow; (−) Token management complexity in Angular; requires IdP provisioning process for 19 roles |

---

### 6.3 JWT Resource Server

| Aspect | Detail |
|--------|--------|
| **Purpose** | Validate JWT access tokens on every API request; extract claims for `UserId`, roles, and location scope; stateless API authentication |
| **Why selected** | Aligns with Angular SPA architecture; scales horizontally without server-side session affinity; supports NFR-SEC-021 session management policies |
| **Alternatives considered** | Server-side sessions with Redis (stateful — works but adds session management overhead); Basic auth (prohibited — NFR-SEC-001) |
| **Trade-offs** | (+) Stateless, cloud-friendly; (−) Token revocation requires short TTL + refresh or token blocklist for immediate deprovision |

---

### 6.4 BCrypt / DelegatingPasswordEncoder

| Aspect | Detail |
|--------|--------|
| **Purpose** | Password hashing for locally provisioned accounts (fallback when SSO unavailable) and service account secrets |
| **Why selected** | Spring Security default; NFR-SEC-010 password policy compliance; adaptive cost factor |
| **Alternatives considered** | Argon2 (stronger — supported via DelegatingPasswordEncoder if policy requires); Plain hash (prohibited) |
| **Trade-offs** | (+) Built-in, proven; (−) BCrypt 72-byte limit — irrelevant for generated passwords |

---

## 7. Messaging

### 7.1 Spring Application Events + Spring Modulith Event API (MVP)

| Aspect | Detail |
|--------|--------|
| **Purpose** | **In-process domain event bus** for MVP — cross-module choreography within modular monolith (SRS-SA-005); `PutAwayCompleted` → Balance, all events → Intelligence |
| **Why selected** | No external broker ops for MVP (ORC-04); Spring Modulith provides module-scoped event publication and subscription; transactional integrity with JDBC event registry; meets internal event latency < 5 seconds |
| **Alternatives considered** | RabbitMQ/Kafka from day one (ops overhead, BC-01); Direct method calls (tight coupling — violates module boundaries); Database polling only (higher latency) |
| **Trade-offs** | (+) Zero additional infrastructure, ACID with outbox, simple debugging; (−) Not suitable for external system integration — Phase 2 broker required for CRM webhooks and channel feeds |

---

### 7.2 Transactional Outbox (PostgreSQL + Spring Modulith JDBC Registry)

| Aspect | Detail |
|--------|--------|
| **Purpose** | Reliable domain event delivery — events written to outbox table in same transaction as aggregate save; async dispatcher publishes after commit (SRS-SA-005, NFR-REL-007) |
| **Why selected** | Prevents lost events on crash between DB commit and publish; idempotent event handlers; supports at-least-once delivery with deduplication by `EventId` |
| **Alternatives considered** | Dual-write (publish then save — inconsistent); XA two-phase commit (complex, performance penalty); Change Data Capture / Debezium (ops heavy for MVP) |
| **Trade-offs** | (+) Proven pattern, uses existing Postgre PostgreSQL; (−) Outbox table growth — requires archival job; slight publish latency (acceptable) |

---

### 7.3 RabbitMQ (Phase 2 — Recommended External Broker)

| Aspect | Detail |
|--------|--------|
| **Purpose** | External async integration — CRM order webhooks, channel ATP feed, finance export triggers, notification dispatch; decouple IMS from external consumer pace |
| **Why selected** | Mature, operable by limited IT team; sufficient throughput for IMS scale; Spring AMQP integration; easier ops than Kafka for mid-sized message volumes |
| **Alternatives considered** | **Apache Kafka** (higher throughput, event replay — overkill for MVP scale, steeper ops ORC-04); **AWS SQS** (cloud lock-in); **Redis Streams** (less durable guarantee) |
| **Trade-offs** | (+) Proven, Spring integration, manageable ops; (−) Not ideal for event sourcing replay at scale — acceptable as IMS uses PostgreSQL as source of truth, not broker log |

*Final broker selection deferred to Phase 2 integration workshop (HS-014, EXT-01).*

---

## 8. Build Tools

### 8.1 Apache Maven (Multi-Module)

| Aspect | Detail |
|--------|--------|
| **Purpose** | Build orchestration — multi-module project structure mapping to 13 bounded contexts + shared kernel + application shell; dependency management, packaging, CI integration |
| **Why selected** | Enterprise standard for Java/Spring; explicit XML configuration aids governance review; Spring Modulith documentation uses Maven; predictable CI pipeline; wide IDE support |
| **Alternatives considered** | **Gradle** (faster builds, Kotlin DSL — preferred by some teams but less universal in enterprise procurement environments); **Bazel** (overkill); Single-module build (no boundary enforcement) |
| **Trade-offs** | (+) Universal, stable, audit-friendly `pom.xml`; (−) Slower than Gradle; verbose XML — mitigate with parent POM and BOM |

---

### 8.2 Spring Boot Maven BOM

| Aspect | Detail |
|--------|--------|
| **Purpose** | Centralized dependency version management — aligned Spring Boot, Spring Security, Hibernate, Jackson versions across all modules |
| **Why selected** | Prevents version conflicts across 13 modules; Spring-tested compatibility matrix |
| **Alternatives considered** | Manual version pinning per module (drift risk) |
| **Trade-offs** | (+) Consistency, security patch alignment; (−) Tied to Spring Boot release cadence |

---

### 8.3 GitHub Actions / Azure DevOps Pipelines (CI/CD)

| Aspect | Detail |
|--------|--------|
| **Purpose** | Continuous integration — build, test, ArchUnit boundary checks, Flyway validation, Docker image publish on merge |
| **Why selected** | Automated quality gate for 13-module codebase; supports parallel module test execution; organization likely has existing pipeline platform |
| **Alternatives considered** | Jenkins (self-hosted ops overhead); GitLab CI (depends on repo hosting) |
| **Trade-offs** | (+) Automated NFR regression via test suite; (−) Pipeline maintenance — shared templates reduce per-module duplication |

---

## 9. Testing

### 9.1 JUnit 5

| Aspect | Detail |
|--------|--------|
| **Purpose** | Unit and integration test framework — domain invariant tests, command handler tests, repository tests |
| **Why selected** | Java standard; Spring Boot Test native support; parameterized tests for business rule matrices (BR-001 – BR-032) |
| **Alternatives considered** | TestNG (less Spring ecosystem momentum); Spock/Groovy (different language) |
| **Trade-offs** | (+) Universal, IDE support; (−) Verbose compared to Spock — acceptable |

---

### 9.2 Mockito

| Aspect | Detail |
|--------|--------|
| **Purpose** | Mock domain repository ports and cross-module query ports in application layer unit tests — isolate handlers from infrastructure |
| **Why selected** | Standard Java mocking; aligns with Clean Architecture testing (SRS-SA-004 LS-10) |
| **Alternatives considered** | WireMock (for HTTP — use for ACL adapter tests); Manual stubs (verbose) |
| **Trade-offs** | (+) Fast unit tests; (−) Over-mocking risk — balance with integration tests |

---

### 9.3 Spring Boot Test + Testcontainers

| Aspect | Detail |
|--------|--------|
| **Purpose** | Integration tests with real PostgreSQL and Redis in Docker containers — verify repository mappings, Flyway migrations, saga flows, and outbox delivery |
| **Why selected** | Eliminates H2/embedded DB divergence from PostgreSQL production behaviour; Testcontainers is industry standard for Spring integration tests |
| **Alternatives considered** | H2 in-memory (PostgreSQL incompatibility — JSONB, locking); Dedicated test database (CI hygiene issues) |
| **Trade-offs** | (+) Production-parity testing; (−) Slower CI — mitigate with test slicing and parallel execution |

---

### 9.4 ArchUnit

| Aspect | Detail |
|--------|--------|
| **Purpose** | Architecture fitness functions — enforce module boundary rules (SRS-SA-003 MB-01 – MB-08), layer dependency rule (SRS-SA-004), domain purity (no JPA in domain package) |
| **Why selected** | Prevents modular monolith erosion; automated gate in CI; complements Spring Modulith module tests |
| **Alternatives considered** | Manual code review only (insufficient at scale); jQAssistant (heavier graph analysis) |
| **Trade-offs** | (+) Automated architecture governance; (−) Rules require maintenance as packages evolve |

---

### 9.5 Cypress (E2E — Angular)

| Aspect | Detail |
|--------|--------|
| **Purpose** | End-to-end browser tests for critical user journeys — ATP lookup, goods receipt, order reservation, cycle count blind entry |
| **Why selected** | Strong Angular integration; readable tests for QA collaboration; supports warehouse responsive viewport testing |
| **Alternatives considered** | Playwright (excellent, growing — either acceptable); Selenium (verbose, flaky); Protractor (deprecated) |
| **Trade-offs** | (+) Developer-friendly, good debugging; (−) Slower than unit tests — limit to MVP critical path suite (~20 journeys) |

---

### 9.6 k6 / Gatling (Performance — Phase 2)

| Aspect | Detail |
|--------|--------|
| **Purpose** | Load testing for NFR-PERF validation — concurrent ATP lookups, reservation contention on Class A SKUs, peak season simulation |
| **Why selected** | Validates NFR-PERF-001 – NFR-PERF-003 before go-live; k6 scriptable in CI |
| **Alternatives considered** | JMeter (GUI-heavy, less CI-friendly) |
| **Trade-offs** | (+) Evidence for capacity model; (−) Deferred to pre-go-live phase per NFR performance baseline program |

---

## 10. Containerization

### 10.1 Docker

| Aspect | Detail |
|--------|--------|
| **Purpose** | Package IMS application, Angular static assets (via nginx sidecar or embedded), and local development dependencies (PostgreSQL, Redis) as portable containers |
| **Why selected** | Industry standard; consistent dev/prod parity; required for Testcontainers; supports ORC-04 limited ops via immutable deployments |
| **Alternatives considered** | Bare JAR deployment (environment drift); VM images (heavier, slower iteration) |
| **Trade-offs** | (+) Reproducible, portable, CI-friendly; (−) Team Docker literacy required; image security scanning needed |

---

### 10.2 Docker Compose (Development & Integration Test)

| Aspect | Detail |
|--------|--------|
| **Purpose** | Local developer environment — Spring Boot app + PostgreSQL + Redis + mail catcher (notifications) with single `docker compose up` |
| **Why selected** | Fast onboarding for mixed-skill delivery team; mirrors integration test environment |
| **Alternatives considered** | Local native PostgreSQL install (inconsistent versions); Devcontainers (optional supplement) |
| **Trade-offs** | (+) One-command environment; (−) Not for production — production uses orchestrator |

---

### 10.3 Kubernetes (Production — Phase 2+)

| Aspect | Detail |
|--------|--------|
| **Purpose** | Production orchestration — horizontal pod autoscaling for API tier, rolling deployments for zero-downtime location rollouts (OC-01), health checks (NFR-AVL-001) |
| **Why selected** | Cloud platform standard (SVC-04); supports 99.5% uptime with replica sets; secrets via SVC-07 integration |
| **Alternatives considered** | **Managed PaaS** (Azure App Service, AWS Elastic Beanstalk — simpler ops, recommended for MVP if ORC-04 is critical); **Docker Swarm** (declining adoption) |
| **Trade-offs** | (+) Scalable, self-healing, industry standard; (−) Operational complexity — **recommend managed Kubernetes (AKS/EKS) or PaaS for MVP**, defer full K8s ops to Phase 2 |

---

### 10.4 Nginx (Static Asset Serving)

| Aspect | Detail |
|--------|--------|
| **Purpose** | Serve Angular production build; reverse proxy to Spring Boot API; TLS termination at edge |
| **Why selected** | Lightweight, proven; separates static frontend from API scaling |
| **Alternatives considered** | Spring Boot serving static files (couples frontend deploy to backend); CDN only (premature for internal IMS) |
| **Trade-offs** | (+) Clean separation, cache headers for static assets; (−) Additional container in deployment |

---

## 11. Observability Stack (Supplementary)

| Technology | Purpose | Why Selected |
|------------|---------|--------------|
| **Micrometer** | Application metrics facade | Spring Boot Actuator native; NFR-MON KPI metrics |
| **Prometheus** | Metrics collection and storage | Industry standard; scrape Spring Actuator `/actuator/prometheus` |
| **Grafana** | Dashboards and alerting | Ops visibility; NFR-MON-001 5-minute outage detection |
| **Logback + JSON encoder** | Structured logging | NFR-LOG-001 standard fields; ELK/Loki ingestion ready |
| **OpenTelemetry** | Distributed tracing | Correlation ID propagation across modules (SRS-SA-006) |

---

## 12. Recommended Module Structure (Maven)

```
ims-parent/                          (BOM, dependency management)
├── ims-shared-kernel/               (ProductSku, LocationCode, shared events envelope)
├── ims-catalog/                     (M-01)
│   ├── catalog-domain/
│   ├── catalog-application/
│   ├── catalog-infrastructure/
│   └── catalog-api/                 (REST controllers — presentation)
├── ims-balance/                     (M-04 — core domain)
├── ims-fulfillment/                 (M-07)
├── ...                              (remaining modules)
├── ims-intelligence/                (M-13 — jOOQ read side)
├── ims-identity/                    (M-12)
└── ims-application/                 (Spring Boot main, Modulith assembly, security config)
```

---

## 13. Stack Decision Summary

| Category | Selected | MVP / Phase |
|----------|----------|-------------|
| Language | Java 21 LTS | MVP |
| Backend framework | Spring Boot 3.x + Spring Modulith | MVP |
| API | REST + OpenAPI | MVP |
| Frontend | Angular 19 + Material + TypeScript | MVP |
| Database | PostgreSQL 16 | MVP |
| Cache | Redis 7 | MVP |
| ORM (write) | Hibernate 6 / Spring Data JPA | MVP |
| ORM (read) | jOOQ (Intelligence module) | MVP |
| Migrations | Flyway | MVP |
| Security | Spring Security 6 + OIDC + JWT | MVP |
| Messaging (internal) | Spring Events + Outbox | MVP |
| Messaging (external) | RabbitMQ | Phase 2 |
| Build | Maven multi-module | MVP |
| CI/CD | GitHub Actions / Azure DevOps | MVP |
| Unit/Integration test | JUnit 5 + Mockito + Testcontainers | MVP |
| Architecture test | ArchUnit + Spring Modulith tests | MVP |
| E2E test | Cypress | MVP |
| Containers | Docker + Compose | MVP |
| Orchestration | Managed PaaS or Kubernetes | PaaS MVP → K8s Phase 2 |

---

## 14. Risk and Mitigation

| Risk | Mitigation |
|------|------------|
| JPA anemic domain model | Repository ports in domain; ArchUnit rules; aggregate-focused mapping |
| Angular + Spring team silos | OpenAPI contract; shared API review; full-stack pairing on critical flows |
| PostgreSQL write contention on Stock Position | Optimistic locking; product-location aggregate scope; Redis ATP cache |
| Spring Modulith learning curve | Reference architecture spike in Sprint 0; module template |
| Redis cache staleness | Event-driven invalidation; `asOf` on ATP responses |
| MVP without external broker | In-process events sufficient; outbox ready for broker migration |

---

## 15. Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Senior Solution Architect | | | |
| Tech Lead | | | |
| Security Engineer | | | |
| DevOps Engineer | | | |
| Product Owner | | | |

---

*End of Technology Stack Recommendation*

*Document ID: SRS-SA-007 | Version 1.0 | July 6, 2026*
