# Cross-Cutting Concerns
## Inventory Management System

---

## Document Information

| Attribute | Detail |
|-----------|--------|
| **Document ID** | SRS-SA-006 |
| **Document Title** | Cross-Cutting Concerns — Inventory Management System |
| **Version** | 1.0 |
| **Status** | Draft |
| **Document Owner** | Solution Architect |
| **Prepared For** | Development squads, security, DevOps, and QA leads |
| **Date** | July 6, 2026 |
| **Classification** | Internal — Architecture Confidential |
| **Scope** | Placement and responsibility of cross-cutting concerns across layers — no framework or library selection |

### Related Documents

| Document | ID | Relationship |
|----------|-----|--------------|
| Layered Architecture Design | SRS-SA-004 | Four-layer model and dependency rule |
| System Modules Design | SRS-SA-003 | Identity & Access module (M-12) |
| Integration Architecture Design | SRS-SA-005 | Security zones and correlation IDs |
| Security Requirements | NFR-SEC | Authentication and authorization NFRs |
| Logging Requirements | NFR-LOG | Operational and audit logging NFRs |
| Compliance Requirements | NFR-COM | Audit trail and retention NFRs |

### Document Purpose

Cross-cutting concerns affect every module and layer of the Inventory Management System. This document identifies **where each concern belongs** in the Clean Architecture stack, what it must **not** do, and how concerns interact — so that security, auditability, and operational quality are implemented consistently without polluting domain logic.

---

## 1. Cross-Cutting Concerns Overview

### 1.1 Layer Placement Summary

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  PRESENTATION     Auth middleware │ Input validators │ Exception filters    │
│                   Locale/format   │ Correlation ID attach                     │
├─────────────────────────────────────────────────────────────────────────────┤
│  APPLICATION      Authorization   │ Command/query  │ Transaction (UoW)     │
│                   behaviors       │ validation     │ Saga boundaries       │
│                   Exception map   │ Audit context  │ Cache policy (use)    │
├─────────────────────────────────────────────────────────────────────────────┤
│  DOMAIN           Business        │ Domain         │ Domain exceptions     │
│                   invariants      │ validation     │ (rule violations)     │
├─────────────────────────────────────────────────────────────────────────────┤
│  INFRASTRUCTURE   Auth adapter    │ Logger         │ Cache implementation  │
│                   (IdP/SSO)      │ Audit writer   │ Config provider       │
│                   AuthZ adapter  │ Exception log  │ Localization resources│
│                   (M-12 port)    │ UoW impl       │ Transaction manager   │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 1.2 Concern Placement Matrix

| Concern | Primary Layer | Supporting Layers | Owning Module |
|---------|---------------|-------------------|---------------|
| Authentication | Infrastructure | Presentation, Application | M-12 Identity & Access |
| Authorization | Application | Infrastructure (adapter), Domain (SoD rules) | M-12 + M-03 Governance |
| Logging | Infrastructure | Presentation (correlation), Application (context) | Platform (all modules) |
| Exception handling | Presentation + Application | Domain (throw), Infrastructure (log) | Per module |
| Validation | Domain + Presentation | Application (orchestration) | Per module |
| Auditing | Infrastructure + Application | Domain (events), Intelligence (projection) | M-13 Intelligence |
| Caching | Infrastructure | Application (policy) | M-04 Balance (ATP), M-13 Intelligence |
| Transactions | Application | Infrastructure (implementation) | Per module |
| Configuration | Infrastructure | Application (inject) | Platform |
| Localization | Presentation + Infrastructure | Application (formatting ports) | Platform |

---

## 2. Authentication

### 2.1 Definition in IMS

**Authentication** establishes *who* is performing an action — verifying that a user identity is genuine before any inventory command, query, or configuration change is accepted. Every transaction must be attributable to an individually authenticated user (NFR-SEC-001, NFR-SEC-002).

### 2.2 Architectural Placement

| Layer | Responsibility | Components |
|-------|----------------|------------|
| **Presentation** | Extract credentials from incoming requests; attach authenticated principal to request context; reject unauthenticated requests before reaching handlers | Auth middleware, session/token extractor, `[Authorize]` guards on controllers |
| **Application** | Consume resolved `UserId` from context; never parse raw tokens; require identity for command attribution | `IUserContext` port (read-only), command enrichment with `UserId` |
| **Domain** | Accept `UserId` / `UserActionAttribution` as value objects on mutations; **no authentication logic** | `UserActionAttribution` value object on aggregates |
| **Infrastructure** | Integrate enterprise IdP (SSO); validate JWT/session; map claims to `UserId`; session store if required | `IdentityProviderAdapter`, `JwtTokenValidator`, `SessionStore` |

### 2.3 Module Ownership

| Module | Role |
|--------|------|
| **M-12 Identity & Access** | Owns user account lifecycle; defines authentication contract |
| **All other modules** | Consume `IUserContext` / `IIdentityService` port — never implement auth |

### 2.4 Key Rules

| Rule | Detail |
|------|--------|
| AUTH-01 | Zero shared accounts in production (NFR-SEC-001) |
| AUTH-02 | Authentication occurs before any handler or controller business logic |
| AUTH-03 | Re-authentication required for high-risk actions (NFR-SEC-004): bulk import, write-offs, role changes |
| AUTH-04 | Failed login handling: lockout after 5 attempts / 15 minutes (NFR-SEC-003) |
| AUTH-05 | Domain layer receives resolved identity only — never raw tokens or passwords |

### 2.5 Does Not Belong In

- **Domain** — authentication is an infrastructure concern; domain knows *who* acted, not *how* they proved identity
- **Other operational modules** — no module except M-12 implements token validation

---

## 3. Authorization

### 3.1 Definition in IMS

**Authorization** determines *what* an authenticated user may do — role-based and location-scoped permissions across 100 system permissions and 19 business roles, plus segregation-of-duties enforcement (FR-084, FR-085, NFR-SEC-005 – NFR-SEC-009).

### 3.2 Architectural Placement

| Layer | Responsibility | Components |
|-------|----------------|------------|
| **Presentation** | Optional coarse endpoint-level guards; delegate fine-grained checks to application layer | Route-level role attributes (supplementary only) |
| **Application** | **Primary authorization gate** — verify permission and location scope before every command handler; invoke SoD checks | `AuthorizationBehavior`, `RequirePermissionAttribute` handler, `LocationScopeBehavior` |
| **Domain** | Express SoD and eligibility as domain policies where business-meaningful; e.g., "counter cannot approve own count" | `SegregationOfDutiesPolicy`, governance consultation |
| **Infrastructure** | Implement `IIdentityService` / `IAuthorizationService` ports by delegating to M-12 Identity module adapter | `IdentityAuthorizationAdapter`, permission cache (short TTL) |

### 3.3 Policy Sources

| Policy Type | Defined In | Enforced In |
|-------------|------------|-------------|
| Role → permission matrix | M-12 Identity | Application layer `AuthorizeAction` |
| Location scope | M-12 Identity + M-02 Network codes | Application layer before location-scoped commands |
| Segregation of duties | M-03 Governance + M-12 Identity | Application layer at command; M-12 at role assignment |
| Business eligibility (e.g., discontinued SKU) | Domain of owning module | Domain layer invariants |

### 3.4 Key Rules

| Rule | Detail |
|------|--------|
| AUTHZ-01 | Fail closed — if authorization cannot be determined, reject the command |
| AUTHZ-02 | Authorization is checked in application layer, not in controllers alone |
| AUTHZ-03 | Location-scoped roles validated against `LocationCode` on every warehouse command |
| AUTHZ-04 | SoD violations blocked at role assignment (M-12) and at command execution (application) |
| AUTHZ-05 | Read queries scoped to user's authorized locations and permissions |

### 3.5 Does Not Belong In

- **Infrastructure (business rules)** — permission matrix is not hard-coded in adapters
- **Domain (role checks)** — domain enforces business SoD invariants, not RBAC matrix lookups

---

## 4. Logging

### 4.1 Definition in IMS

**Logging** captures operational diagnostic and security information — request traces, errors, performance markers, and security events — to support troubleshooting, monitoring (NFR-MON), and security investigation (NFR-LOG, NFR-SEC-025 – NFR-SEC-028).

Logging is distinct from **auditing** (Section 6) — logs are for operators; audit records are for compliance and governance.

### 4.2 Architectural Placement

| Layer | Responsibility | Components |
|-------|----------------|------------|
| **Presentation** | Attach `CorrelationId`, `RequestId`, HTTP metadata to logging scope; log request start/end at info level | Request logging middleware, correlation ID middleware |
| **Application** | Enrich log scope with command name, aggregate ID, `UserId`; log handler entry/exit and saga steps | Structured log context in behaviors, saga step logging |
| **Domain** | **No logging** — domain remains pure; exceptions carry message codes only | — |
| **Infrastructure** | Logger implementation, log sinks, log format standard, retention, immutability for security logs | `StructuredLogger`, log appenders, NFR-LOG-001 standard fields |

### 4.3 Standard Log Attributes (NFR-LOG-001)

Every log entry includes: timestamp (UTC), severity, `CorrelationId`, `UserId`, module name, operation name, outcome, and duration where applicable.

| Log Category | Examples | Retention |
|--------------|----------|-----------|
| **Operational** | Handler execution, query performance, cache hit/miss | Per NFR-LOG retention schedule |
| **Security** | Login success/failure, permission denied, SoD violation | ≥ 7 years (NFR-COM-020) |
| **Error** | Unhandled exceptions, saga compensation, integration failure | Per operational schedule |
| **Integration** | Cross-module port calls, ACL adapter requests, event publish | Correlation-linked |

### 4.4 Key Rules

| Rule | Detail |
|------|--------|
| LOG-01 | Domain layer does not write logs — keeps business logic testable and pure |
| LOG-02 | Never log passwords, tokens, or full PII — mask sensitive fields (NFR-SEC-017) |
| LOG-03 | Correlation ID propagates from presentation through application to infrastructure and cross-module calls |
| LOG-04 | Security events logged at warn or higher; never suppressed |
| LOG-05 | Log structure is consistent across all 13 modules |

### 4.5 Does Not Belong In

- **Domain** — no `ILogger` in aggregates
- **Audit trail** — operational logs are not the compliance audit record (see Auditing)

---

## 5. Exception Handling

### 5.1 Definition in IMS

**Exception handling** manages the translation of failures — business rule violations, validation errors, authorization denials, and infrastructure faults — into controlled responses without exposing internal state or corrupting inventory data.

### 5.2 Architectural Placement

| Layer | Responsibility | Components |
|-------|----------------|------------|
| **Presentation** | Catch application/domain exceptions; map to HTTP status and user-safe response DTOs; never expose stack traces to clients | `ExceptionFilter`, `ProblemDetails` mapper, global exception handler |
| **Application** | Catch infrastructure exceptions; wrap in application exceptions; trigger saga compensation; decide retry vs. fail | Saga compensation handlers, `CommandExceptionBehavior` |
| **Domain** | Throw **domain exceptions** for business rule violations — typed, meaningful, no HTTP concepts | `InsufficientAtpException`, `LocationFrozenException`, `SegregationOfDutiesViolationException` |
| **Infrastructure** | Log unhandled technical exceptions; translate persistence/network errors to infrastructure exceptions | ORM exception wrapper, retry policies for transient DB errors |

### 5.3 Exception Taxonomy

| Exception Type | Origin Layer | HTTP Mapping (Presentation) | User Message |
|----------------|--------------|----------------------------|--------------|
| `ValidationException` | Presentation / Application | 400 Bad Request | Field-level errors |
| `UnauthorizedException` | Application | 401 Unauthorized | Generic auth failure |
| `ForbiddenException` | Application | 403 Forbidden | Insufficient permission |
| `NotFoundException` | Application | 404 Not Found | Resource not found |
| `BusinessRuleViolationException` | Domain | 422 Unprocessable Entity | Business-safe rule message |
| `ConflictException` | Application / Domain | 409 Conflict | Concurrent modification, duplicate |
| `InfrastructureException` | Infrastructure | 503 Service Unavailable | Generic system error |

### 5.4 Saga and Exception Interaction

| Scenario | Handling |
|----------|----------|
| Reservation fails after order confirmed | Saga compensates — `CompensateOrderConfirmation` |
| Put-away fails after receipt verified | Receipt remains verified; put-away retried; no stock increase |
| Authorization denied mid-saga | Saga aborts; no partial commits |
| Transient DB error | Infrastructure retry; application remains unaware of retry count |

### 5.5 Key Rules

| Rule | Detail |
|------|--------|
| EXC-01 | Domain throws domain exceptions — never returns error codes as return values |
| EXC-02 | Presentation is the only layer that maps exceptions to HTTP |
| EXC-03 | Business rule messages use ubiquitous language terms — not technical codes in user text |
| EXC-04 | Unhandled exceptions logged at error with full correlation context |
| EXC-05 | Exception handling never swallows stock mutation failures silently |

### 5.6 Does Not Belong In

- **Domain** — no HTTP status codes, no logging in catch blocks
- **Infrastructure** — no business rule interpretation; wrap and rethrow

---

## 6. Validation

### 6.1 Definition in IMS

**Validation** ensures inputs and state transitions are well-formed and business-legal before execution. IMS distinguishes **three validation levels** — each belongs in a different layer.

### 6.2 Three Levels of Validation

| Level | Layer | Scope | Examples |
|-------|-------|-------|----------|
| **Syntactic** | Presentation | Request shape, types, required fields, format | SKU not empty, quantity is positive integer, date parseable |
| **Application** | Application | Command preconditions, cross-field rules, saga guards | "Approve adjustment" requires pending case ID; import batch size limit |
| **Domain / Business** | Domain | Invariants, business rules (BR-001 – BR-032) | ATP ≥ 0, cannot reserve on frozen location, BR-019 SoD |

### 6.3 Architectural Placement

| Layer | Responsibility | Components |
|-------|----------------|------------|
| **Presentation** | Syntactic validation on request DTOs; return 400 before dispatching command | Fluent validators, data annotations, request DTO rules |
| **Application** | Application-level validation behaviors in command pipeline; consult governance/catalog/network ports for preconditions | `ValidationBehavior`, command validators |
| **Domain** | **Authoritative business validation** — invariants enforced in aggregate methods; cannot be bypassed | Aggregate root methods, domain policies, specifications |
| **Infrastructure** | Database constraints as last-resort safety net only — not primary validation | Unique indexes, FK constraints, check constraints |

### 6.4 Validation Pipeline (Command Path)

```
Request DTO
    │
    ▼
[Presentation]  Syntactic validation ──fail──► 400 Bad Request
    │
    ▼
[Application]     Authorization check
    │
    ▼
[Application]     Application precondition validation ──fail──► ValidationException
    │
    ▼
[Domain]          Aggregate method enforces invariants ──fail──► BusinessRuleViolationException
    │
    ▼
[Infrastructure]  Persist (DB constraints as safety net)
```

### 6.5 Key Rules

| Rule | Detail |
|------|--------|
| VAL-01 | Business rules live in domain — never only in UI or API validators |
| VAL-02 | Presentation validation is for user experience — domain validation is for correctness |
| VAL-03 | Validation rules from SRS-BR-001 and VR-xxx trace to domain invariants or application preconditions |
| VAL-04 | Blind cycle count: application must not pass system quantity to presentation for counter view (BR-018) |
| VAL-05 | Duplicate syntactic validation in domain is acceptable for defense in depth on critical invariants |

### 6.6 Does Not Belong In

- **Infrastructure as primary validator** — DB constraints supplement, not replace, domain rules
- **Presentation for business rules** — UI cannot be the only enforcement of BR-001 (ATP)

---

## 7. Auditing

### 7.1 Definition in IMS

**Auditing** produces an **immutable, governance-grade record** of material inventory actions — who did what, when, where, why, and what changed — supporting BO-19 (100% audit trail), internal control (COSO), and external audit (NFR-COM-010, NFR-REL-009).

Auditing is **not** the same as operational logging. Audit records are structured business evidence; logs are diagnostic.

### 7.2 Architectural Placement

| Layer | Responsibility | Components |
|-------|----------------|------------|
| **Presentation** | No audit logic — passes through authenticated context | — |
| **Application** | Enrich commands with audit context (`UserId`, reason code, correlation ID); collect domain events after successful commit | `AuditContextEnricher`, post-handler event collection |
| **Domain** | Raise **domain events** that constitute auditable business facts; embed `UserActionAttribution` on mutations | `StockReserved`, `AdjustmentApproved`, attribution value objects |
| **Infrastructure** | Persist audit records; implement append-only audit store; export evidence packages | `AuditTrailWriter`, immutable log store |
| **M-13 Intelligence** | **Audit trail read projection** — query, search, export for auditors (NFR-COM-012, NFR-PERF-026) | `AuditTrailProjection`, `ExportAuditEvidenceQueryHandler` |

### 7.3 Audit Record Sources

| Source | Mechanism | Content |
|--------|-----------|---------|
| Domain events | Event → Intelligence projection | Business fact, before/after quantities, reason code |
| Command metadata | Application layer audit context | Initiator, approver, timestamp, location scope |
| Security events | Infrastructure security log → audit projection | Login, permission denied, role change |
| Governance decisions | M-03 events | Policy change, threshold amendment |

### 7.4 Material Actions Requiring Audit (Non-Exhaustive)

| Category | Actions |
|----------|---------|
| Stock mutations | Receipt, reservation, shipment, transfer, adjustment, write-off, quarantine |
| Governance | Adjustment approval, write-off approval, policy change, reason code change |
| Master data | Product lifecycle change, location activation/closure, supplier deactivation |
| Access | Role assignment, SoD violation attempt, account deactivation |
| Count | Cycle count result, physical count certification, variance approval |
| Financial | Three-way match outcome, invoice authorization |

### 7.5 Key Rules

| Rule | Detail |
|------|--------|
| AUD-01 | Audit records are append-only — no update or delete (NFR-LOG-026, NFR-COM-010) |
| AUD-02 | Retained ≥ 7 years aligned with financial records (NFR-COM-019, NFR-COM-020) |
| AUD-03 | Single authoritative audit projection in M-13 Intelligence — not duplicated per module |
| AUD-04 | Domain events are the primary audit source — audit is a consequence of correct domain design |
| AUD-05 | Auditor export within 15 minutes (NFR-PERF-026, NFR-COM-012) |

### 7.6 Does Not Belong In

- **Presentation** — no audit persistence in controllers
- **Operational logs as audit substitute** — logs lack business structure and immutability guarantees
- **Per-module audit tables** — centralized projection in Intelligence

---

## 8. Caching

### 8.1 Definition in IMS

**Caching** stores frequently accessed read data to meet performance NFRs — especially ATP lookup (NFR-PERF-002, 2 seconds) and dashboard load (NFR-PERF-004) — without serving stale data that could cause overselling.

### 8.2 Architectural Placement

| Layer | Responsibility | Components |
|-------|----------------|------------|
| **Presentation** | HTTP cache headers for safe static resources only — **not** for ATP or stock data | Static asset cache headers |
| **Application** | Define cache use policy — when to read from cache vs. authoritative source; never cache write paths | `ICachePolicy` consultation in query handlers |
| **Domain** | **No caching** — domain always works with authoritative state | — |
| **Infrastructure** | Cache implementation, storage, TTL, invalidation on domain events | `AtpCacheService`, `DashboardCacheService`, event-driven invalidation handlers |

### 8.3 Cache Domains

| Cache Target | Owner | Invalidation Trigger | Staleness Tolerance |
|--------------|-------|----------------------|---------------------|
| **ATP by SKU/location** | M-04 Balance infrastructure | `StockReserved`, `StockReceived`, `StockShipped`, `StockAdjusted`, quarantine events | Near-zero — invalidate immediately on balance event |
| **Product master** | M-01 Catalog infrastructure | `ProductUpdated`, `ProductLifecycleStatusChanged` | Minutes — catalog changes infrequently |
| **Location status / freeze** | M-02 Network infrastructure | `LocationFreezeApplied`, `LocationFreezeReleased`, activation events | Near-zero for freeze; minutes for status |
| **Dashboard KPIs** | M-13 Intelligence infrastructure | Scheduled refresh + event-triggered for critical alerts | Minutes (NFR-PERF-004) |
| **Permission lookup** | M-12 Identity infrastructure | `RoleAssigned`, `RoleRevoked` | Short TTL (seconds) as safety net |

### 8.4 Key Rules

| Rule | Detail |
|------|--------|
| CACHE-01 | **Never cache write command paths** — cache is read-only optimization |
| CACHE-02 | ATP cache must invalidate on any balance change event — oversell risk |
| CACHE-03 | Cache miss falls through to authoritative read repository — no fail-to-zero ATP |
| CACHE-04 | Cached responses include `asOf` timestamp for channel feeds (EXT-03) |
| CACHE-05 | Domain layer is cache-unaware — testability and correctness |

### 8.5 Does Not Belong In

- **Domain** — aggregates never read from cache
- **Application (implementation)** — application defines policy; infrastructure implements store
- **Presentation** — no in-memory ATP caching in controllers

---

## 9. Transactions

### 9.1 Definition in IMS

**Transactions** define atomicity boundaries — ensuring that one aggregate mutation completes fully or not at all, and that domain events are reliably published with the commit (outbox pattern).

### 9.2 Architectural Placement

| Layer | Responsibility | Components |
|-------|----------------|------------|
| **Presentation** | No transaction management | — |
| **Application** | **Own transaction boundaries** — `IUnitOfWork` per command handler; one aggregate per transaction; saga spans multiple transactions | `IUnitOfWork`, command handlers, saga orchestrators |
| **Domain** | Define consistency within aggregate; no transaction awareness | Aggregate atomic mutations |
| **Infrastructure** | Implement `IUnitOfWork`, database connection, transaction manager, transactional outbox | `DbUnitOfWork`, `OutboxMessage` persistence |

### 9.3 Transaction Rules (DDD)

| Rule | Scope | Detail |
|------|-------|--------|
| TX-01 | Single command handler | One `UnitOfWork.Commit()` per command — one aggregate mutation |
| TX-02 | Cross-aggregate workflow | Saga — each step is its own transaction; eventual consistency between steps |
| TX-03 | Cross-module workflow | Same as saga — no distributed transaction across modules |
| TX-04 | Event publish | Domain events written to outbox in same DB transaction as aggregate save |
| TX-05 | Read queries | No transaction required for CQRS read path; read-uncommitted not used for ATP |
| TX-06 | Intelligence projections | Separate transaction per projection handler — idempotent upsert |

### 9.4 Transaction Flow

```
CommandHandler:
    UnitOfWork.Begin()
        aggregate = Repository.Get()
        aggregate.ExecuteCommand()     // domain invariants
        Repository.Save(aggregate)
        Outbox.Add(domainEvents)
    UnitOfWork.Commit()                // atomic: aggregate + outbox
    EventBus.Dispatch(outboxEvents)    // after commit
```

### 9.5 Key Rules

| Rule | Detail |
|------|--------|
| TX-07 | Application layer opens and commits transactions — not controllers, not domain |
| TX-08 | Stock Position reservation and order confirmation are separate transactions linked by saga |
| TX-09 | Retry of transient failures at infrastructure layer must not double-apply — idempotent handlers |
| TX-10 | Long-running transactions prohibited — no transaction spans user think time or external API wait |

### 9.6 Does Not Belong In

- **Domain** — no `BeginTransaction()` in aggregates
- **Presentation** — no request-scoped transactions across multiple commands
- **Distributed two-phase commit** — prohibited across modules

---

## 10. Configuration

### 10.1 Definition in IMS

**Configuration** supplies environment-specific and tunable parameters — connection strings, feature flags, integration endpoints, threshold defaults, retention periods — without hard-coding them in domain or application logic.

### 10.2 Architectural Placement

| Layer | Responsibility | Components |
|-------|----------------|------------|
| **Presentation** | UI display configuration only (e.g., page size defaults) — not system config | View settings |
| **Application** | Consume configuration via injected options interfaces — no direct file/env access | `IOptions<InventorySettings>`, `IFeatureManager` |
| **Domain** | **No configuration** — business thresholds that are governance policy live in M-03 Governance aggregate, not config files | — |
| **Infrastructure** | Load configuration from environment, secrets manager, config files; bind to options classes | `ConfigurationProvider`, secrets adapter (SVC-07) |

### 10.3 Configuration Categories

| Category | Examples | Layer | Mutable At Runtime |
|----------|----------|-------|-------------------|
| **Infrastructure** | DB connection, IdP endpoint, email gateway | Infrastructure | Deploy time |
| **Secrets** | API keys, certificates | Infrastructure (secrets manager) | Rotation via SVC-07 |
| **Feature flags** | Enable campaign module, bonded inventory | Application (via infra provider) | Yes — phased rollout |
| **Operational tuning** | Cache TTL, saga timeout, retry count | Application options | Yes — ops tuning |
| **Business policy** | Approval thresholds, reason codes | **M-03 Governance aggregate** | Via governance commands — not config file |
| **Location-specific** | Business hours per location (NFR-AVL-005) | M-02 Network master data | Via location commands |

### 10.4 Key Rules

| Rule | Detail |
|------|--------|
| CFG-01 | Business rules (BR-xxx) are domain/governance — not `appsettings.json` |
| CFG-02 | Secrets never in source control or domain layer |
| CFG-03 | Configuration injected via interfaces — application depends on `IOptions<T>`, not raw config |
| CFG-04 | Feature flags control module activation per phased delivery — not compile-time branching |
| CFG-05 | Location business hours are master data (M-02), not environment config |

### 10.5 Does Not Belong In

- **Domain** — no `IConfiguration` in aggregates
- **Governance thresholds in config files** — use M-03 Governance Policy aggregate for auditability

---

## 11. Localization

### 11.1 Definition in IMS

**Localization** adapts user-facing text, number/date formats, and currency display for multi-region operations — without altering domain logic, business rules, or stored data formats.

### 11.2 Architectural Placement

| Layer | Responsibility | Components |
|-------|----------------|------------|
| **Presentation** | **Primary localization** — UI labels, messages, error text, report headers; culture selection from user preference or browser | Resource files (`.resx` / i18n bundles), `IStringLocalizer`, culture middleware |
| **Application** | Format dates and currency for query responses via abstraction — stored values remain UTC and canonical | `ILocalizationService`, `IDateTimeFormatter` ports |
| **Domain** | **Culture-neutral** — quantities, dates stored in canonical form (UTC, invariant decimal); reason codes stored as codes with localized display in presentation | Canonical value objects only |
| **Infrastructure** | Load resource bundles; provide localization service implementation | `LocalizationService`, resource providers |

### 11.3 Localization Scope

| Localizable | Not Localizable |
|-------------|-----------------|
| UI labels and menus | `ProductSku`, `LocationCode` identifiers |
| Validation error messages (presentation/application) | Domain event names |
| Report column headers | Audit trail stored values |
| User notification email templates | Database-stored reason code keys (display localized separately) |
| Currency **display** format | Monetary amounts stored in canonical decimal |
| Date **display** in user's timezone | Timestamps stored UTC (NFR-LOG-001) |

### 11.4 Key Rules

| Rule | Detail |
|------|--------|
| L10N-01 | Domain and persistence use invariant culture for all stored values |
| L10N-02 | Business rule exception messages may carry message keys — presentation localizes for user display |
| L10N-03 | Ubiquitous language terms (SRS-DM-008) are the source for translation keys — ATP, not "available stock" inconsistently |
| L10N-04 | Audit and finance exports use locale-neutral formats for machine consumption; human reports may be localized |
| L10N-05 | MVP may ship with single locale (English); architecture supports multi-locale without domain changes |

### 11.5 Does Not Belong In

- **Domain** — no culture-specific logic or translated strings in aggregates
- **Database** — no per-locale duplicate master data rows for products

---

## 12. Cross-Cutting Pipeline (Command Request)

The following shows how all concerns interact on a single write request:

```
HTTP Request
    │
    ├─ [Presentation]  Correlation ID middleware
    ├─ [Presentation]  Authentication middleware ──────────► Infrastructure (IdP)
    ├─ [Presentation]  Localization (culture)
    ├─ [Presentation]  Syntactic validation
    │
    ▼
Command Bus
    │
    ├─ [Application]  Authorization behavior ───────────────► Infrastructure (M-12 port)
    ├─ [Application]  Application validation behavior
    ├─ [Application]  Audit context enrichment
    ├─ [Application]  Logging scope (command name, user)
    │
    ▼
Command Handler
    │
    ├─ [Application]  UnitOfWork.Begin()
    ├─ [Domain]       Aggregate enforces invariants
    ├─ [Infrastructure] Repository.Save + Outbox
    ├─ [Application]  UnitOfWork.Commit()
    ├─ [Infrastructure] Event bus dispatch
    ├─ [Infrastructure] Cache invalidation (if balance change)
    ├─ [Infrastructure] Audit projection update (M-13 handler)
    ├─ [Application]  Logging (success)
    │
    ▼
[Presentation]  Map result / Map exception ─────────────────► Client response
```

---

## 13. Concern Interaction Summary

| Concern | Depends On | Feeds Into |
|---------|------------|------------|
| Authentication | IdP (Infrastructure) | Authorization, Auditing, Logging |
| Authorization | Authentication, M-12, M-03 | Command execution gate |
| Validation | — | Domain execution or early rejection |
| Transactions | — | Event publish, Audit record |
| Auditing | Authentication, Domain events | Intelligence projection, Finance export |
| Logging | Correlation ID | Monitoring (NFR-MON) |
| Exception handling | All layers | Logging, Client response |
| Caching | Domain events (invalidation) | Query performance |
| Configuration | Infrastructure | Application behavior, Feature flags |
| Localization | User culture (Presentation) | UI display only |

---

## 14. Implementation Standards

| ID | Standard |
|----|----------|
| CC-01 | Cross-cutting behaviors implemented as ordered pipeline behaviors in application layer — not copy-pasted per handler |
| CC-02 | All modules use shared cross-cutting libraries for logging format, exception types, correlation, and auth ports |
| CC-03 | Domain layer projects have zero package references to logging, config, cache, or auth libraries |
| CC-04 | Cross-cutting concerns tested independently — auth denial, validation failure, audit record creation |
| CC-05 | NFR traceability maintained — each concern maps to specific NFR-SEC, NFR-LOG, NFR-COM requirements |

---

## 15. Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Solution Architect | | | |
| Security Engineer | | | |
| Tech Lead | | | |
| QA Lead | | | |

---

*End of Cross-Cutting Concerns*

*Document ID: SRS-SA-006 | Version 1.0 | July 6, 2026*
