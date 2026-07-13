-- Seed accounts without password hashes (hashes applied at app startup via PasswordEncoder)
INSERT INTO identity.user_accounts (
    user_identifier, display_name, email, account_status, effective_from
) VALUES
    ('USR-001', 'System Admin', 'admin@ims.local', 'ACTIVE', CURRENT_DATE),
    ('USR-002', 'Warehouse Manager', 'warehouse@ims.local', 'ACTIVE', CURRENT_DATE);

INSERT INTO identity.role_assignments (
    user_account_id, role_name, permission_set, assignment_status, effective_from, sod_compliant
)
SELECT id, 'SYSTEM_ADMINISTRATOR', 'ADMIN_FULL', 'ACTIVE', CURRENT_DATE, TRUE
FROM identity.user_accounts WHERE user_identifier = 'USR-001';

INSERT INTO identity.role_assignments (
    user_account_id, role_name, permission_set, assignment_status, effective_from, sod_compliant
)
SELECT id, 'WAREHOUSE_MANAGER', 'WH_OPS', 'ACTIVE', CURRENT_DATE, TRUE
FROM identity.user_accounts WHERE user_identifier = 'USR-002';

INSERT INTO identity.role_assignment_locations (role_assignment_id, location_code)
SELECT ra.id, 'NETWORK'
FROM identity.role_assignments ra
JOIN identity.user_accounts ua ON ua.id = ra.user_account_id
WHERE ua.user_identifier = 'USR-001';

INSERT INTO identity.role_assignment_locations (role_assignment_id, location_code)
SELECT ra.id, 'WH-EAST'
FROM identity.role_assignments ra
JOIN identity.user_accounts ua ON ua.id = ra.user_account_id
WHERE ua.user_identifier = 'USR-002';
