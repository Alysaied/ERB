-- =============================================================================
-- IMS local database setup (pgAdmin)
-- =============================================================================
-- Step A — as superuser on database "postgres":
--   1. Open Query Tool on database postgres
--   2. Run SECTION A below
--   3. Then: Databases → Create → Database → Name: ims, Owner: ims
--      OR run: CREATE DATABASE ims OWNER ims;
--
-- Step B — reconnect Query Tool to database "ims", then run SECTION B
-- =============================================================================

-- ========== SECTION A (database: postgres) ==========
DO $$
BEGIN
  IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname = 'ims') THEN
    CREATE ROLE ims LOGIN PASSWORD 'ims';
  END IF;
END
$$;

-- CREATE DATABASE ims OWNER ims;   -- run alone if Create Database UI not used

-- ========== SECTION B (database: ims) ==========
GRANT USAGE, CREATE ON SCHEMA public TO ims;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO ims;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON SEQUENCES TO ims;

-- Flyway creates schema "identity" + tables on first backend start.
-- You do not need to create tables manually.
