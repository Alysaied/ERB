package com.ims.identity.application;

import org.springframework.stereotype.Component;

import java.util.LinkedHashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

/**
 * Minimal role→permission map for Sprint 1 session context.
 * Full catalog lands with F-27 admin APIs in Sprint 2.
 */
@Component
public class PermissionCatalog {

    private static final Map<String, List<String>> ROLE_PERMISSIONS = Map.of(
            "SYSTEM_ADMINISTRATOR", List.of(
                    "PERM-ADMIN-USERS",
                    "PERM-ADMIN-ROLES",
                    "PERM-STOCK-VIEW",
                    "PERM-STOCK-ADJUST",
                    "PERM-AUDIT-READ"
            ),
            "WAREHOUSE_MANAGER", List.of(
                    "PERM-STOCK-VIEW",
                    "PERM-STOCK-ADJUST",
                    "PERM-RECEIVE",
                    "PERM-FULFILL"
            )
    );
    public boolean isKnownRole(String roleCode) {
        return ROLE_PERMISSIONS.containsKey(roleCode);
    }

    public String permissionSetFor(String roleCode) {
        return String.join(",", ROLE_PERMISSIONS.getOrDefault(roleCode, List.of()));
    }

    public List<String> resolve(List<String> roles) {
        Set<String> permissions = new LinkedHashSet<>();
        for (String role : roles) {
            permissions.addAll(ROLE_PERMISSIONS.getOrDefault(role, List.of()));
        }
        return List.copyOf(permissions);
    }
}
