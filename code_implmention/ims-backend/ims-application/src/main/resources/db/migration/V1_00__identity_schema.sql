-- Sprint 1 baseline: identity schema (F-27 platform)
CREATE SCHEMA IF NOT EXISTS identity;

CREATE TABLE identity.user_accounts (
    id                BIGSERIAL PRIMARY KEY,
    user_identifier   VARCHAR(64)  NOT NULL,
    display_name      VARCHAR(256) NOT NULL,
    email             VARCHAR(256),
    password_hash     VARCHAR(255),
    account_status    VARCHAR(32)  NOT NULL DEFAULT 'ACTIVE',
    effective_from    DATE         NOT NULL,
    last_activity_at  TIMESTAMPTZ,
    has_sod_conflict  BOOLEAN      NOT NULL DEFAULT FALSE,
    version           INTEGER      NOT NULL DEFAULT 1,
    created_at        TIMESTAMPTZ  NOT NULL DEFAULT NOW(),
    updated_at        TIMESTAMPTZ  NOT NULL DEFAULT NOW(),
    CONSTRAINT uk_user_accounts_user_identifier UNIQUE (user_identifier),
    CONSTRAINT uk_user_accounts_email UNIQUE (email),
    CONSTRAINT ck_user_accounts_status CHECK (account_status IN ('ACTIVE', 'SUSPENDED', 'DEACTIVATED'))
);

COMMENT ON COLUMN identity.user_accounts.password_hash IS
    'Local-dev credential only until OIDC IdP owns passwords (AUTH-01).';
