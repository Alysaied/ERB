# IMS Backend

Sprint 1 platform backbone: Spring Boot Modulith + PostgreSQL/Flyway + JWT session APIs.

## Modules

| Module | Purpose |
|--------|---------|
| `ims-shared-kernel` | Shared problem-detail contracts |
| `ims-identity` | M-12 identity, auth, session (API-173/174) |
| `ims-application` | Boot entrypoint, security, Flyway, health (API-175) |

## Prerequisites

- Java 21+ (project compiles with `--release 21`)
- Local PostgreSQL 16 (pgAdmin)
- Maven 3.9+ (or use `.tools/apache-maven-3.9.9` if present)

## Local database (pgAdmin) — no Docker

### 1. Create role + database

1. Open **pgAdmin** → connect to your local server (usually `localhost:5436` as `postgres`).
2. Open Query Tool on database **`postgres`** and run **SECTION A** from [`scripts/init-local-db.sql`](./scripts/init-local-db.sql).
3. Create database **`ims`** owned by role **`ims`**:
   - UI: Databases → Create → Database → Name `ims`, Owner `ims`
   - Or SQL: `CREATE DATABASE ims OWNER ims;`
4. Open Query Tool on database **`ims`** and run **SECTION B** from the same script.

Default credentials (match backend config):

| Setting | Value |
|---------|-------|
| Host | `localhost` |
| Port | `5436` |
| Database | `ims` |
| User | `ims` |
| Password | `ims` |

Override anytime with env vars: `IMS_DB_HOST`, `IMS_DB_PORT`, `IMS_DB_NAME`, `IMS_DB_USER`, `IMS_DB_PASSWORD`.

### 2. Build & run backend

```bash
cd ims-backend
mvn -DskipTests package
java -jar ims-application/target/ims-application-0.1.0-SNAPSHOT.jar --spring.profiles.active=local
```

Or:

```bash
mvn -f ims-application/pom.xml spring-boot:run -Dspring-boot.run.arguments=--spring.profiles.active=local
```

On first start, **Flyway** creates schema `identity` and seed users — no manual tables needed.

API base: `http://localhost:8080/api/v1`

### Seed users (local JWT)

| Email | Password | Role |
|-------|----------|------|
| `admin@ims.local` | `demo` | SYSTEM_ADMINISTRATOR |
| `warehouse@ims.local` | `demo` | WAREHOUSE_MANAGER |

### Endpoints (Sprint 1)

| ID | Method | Path | Auth |
|----|--------|------|------|
| *(local)* | `POST` | `/api/v1/auth/token` | Public — issues JWT (dev until OIDC) |
| API-173 | `GET` | `/api/v1/auth/session` | Bearer |
| API-174 | `POST` | `/api/v1/auth/logout` | Bearer |
| API-175 | `GET` | `/api/v1/health` | Public |

### Example

```bash
curl -s -X POST http://localhost:8080/api/v1/auth/token \
  -H "Content-Type: application/json" \
  -d "{\"email\":\"admin@ims.local\",\"password\":\"demo\"}"
```

## Notes

- If connection times out on `5432`, your local Postgres may listen on another port (this machine uses **5436**). Check with: `netstat -ano | findstr LISTEN | findstr 54`
- `POST /auth/token` is a **Sprint 1 local-auth bridge** (AUTH-01 / R-I03). Production auth is OIDC IdP.
- `password_hash` on `identity.user_accounts` is local-dev only.
- `role_assignment_locations.location_code` is a Sprint 1 stand-in until `network` schema (F-02) provides `location_id` FKs.
