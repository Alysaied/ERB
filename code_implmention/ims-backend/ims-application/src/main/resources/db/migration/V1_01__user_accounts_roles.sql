-- Sprint 1: role assignments + location scope codes (network FK deferred to F-02)
CREATE TABLE identity.role_assignments (
    id                 BIGSERIAL PRIMARY KEY,
    user_account_id    BIGINT       NOT NULL REFERENCES identity.user_accounts (id),
    role_name          VARCHAR(64)  NOT NULL,
    permission_set     VARCHAR(128),
    assignment_status  VARCHAR(32)  NOT NULL DEFAULT 'ACTIVE',
    effective_from     DATE         NOT NULL,
    effective_to       DATE,
    sod_compliant      BOOLEAN      NOT NULL DEFAULT TRUE,
    created_at         TIMESTAMPTZ  NOT NULL DEFAULT NOW(),
    CONSTRAINT ck_role_assignments_status CHECK (assignment_status IN ('ACTIVE', 'INACTIVE'))
);

CREATE INDEX ix_role_assignments_user ON identity.role_assignments (user_account_id);

CREATE TABLE identity.role_assignment_locations (
    id                  BIGSERIAL PRIMARY KEY,
    role_assignment_id  BIGINT       NOT NULL REFERENCES identity.role_assignments (id),
    location_code       VARCHAR(64)  NOT NULL,
    created_at          TIMESTAMPTZ  NOT NULL DEFAULT NOW(),
    CONSTRAINT uk_role_assignment_location UNIQUE (role_assignment_id, location_code)
);

CREATE INDEX ix_role_assignment_locations_assignment
    ON identity.role_assignment_locations (role_assignment_id);

COMMENT ON COLUMN identity.role_assignment_locations.location_code IS
    'Sprint 1 uses location codes; replace with location_id FK when network schema exists (F-02).';
