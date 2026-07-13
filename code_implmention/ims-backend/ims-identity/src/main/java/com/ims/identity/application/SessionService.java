package com.ims.identity.application;

import com.ims.identity.domain.AccountStatus;
import com.ims.identity.domain.RoleAssignment;
import com.ims.identity.domain.RoleAssignmentLocation;
import com.ims.identity.domain.UserAccount;
import com.ims.identity.infrastructure.RoleAssignmentLocationRepository;
import com.ims.identity.infrastructure.RoleAssignmentRepository;
import com.ims.identity.infrastructure.UserAccountRepository;
import com.ims.identity.api.dto.SessionResponse;
import com.ims.sharedkernel.problem.DomainException;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.Instant;
import java.util.ArrayList;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Set;

@Service
public class SessionService {

    private final UserAccountRepository userAccountRepository;
    private final RoleAssignmentRepository roleAssignmentRepository;
    private final RoleAssignmentLocationRepository roleAssignmentLocationRepository;
    private final PermissionCatalog permissionCatalog;

    public SessionService(
            UserAccountRepository userAccountRepository,
            RoleAssignmentRepository roleAssignmentRepository,
            RoleAssignmentLocationRepository roleAssignmentLocationRepository,
            PermissionCatalog permissionCatalog
    ) {
        this.userAccountRepository = userAccountRepository;
        this.roleAssignmentRepository = roleAssignmentRepository;
        this.roleAssignmentLocationRepository = roleAssignmentLocationRepository;
        this.permissionCatalog = permissionCatalog;
    }

    @Transactional(readOnly = true)
    public SessionResponse buildSession(
            String userIdentifier,
            Instant expiresAt,
            boolean includePermissions,
            boolean includeLocationScope
    ) {
        UserAccount user = userAccountRepository.findByUserIdentifier(userIdentifier)
                .orElseThrow(() -> new DomainException("AUTH_TOKEN_INVALID", "User not found for token", 401));

        assertAccountUsable(user);

        List<RoleAssignment> activeRoles = roleAssignmentRepository.findByUserAccountId(user.getId()).stream()
                .filter(RoleAssignment::isCurrentlyActive)
                .toList();

        List<String> roles = activeRoles.stream().map(RoleAssignment::getRoleName).distinct().toList();

        List<String> locationScope = List.of();
        if (includeLocationScope) {
            List<Long> assignmentIds = activeRoles.stream().map(RoleAssignment::getId).toList();
            Set<String> locations = new LinkedHashSet<>();
            if (!assignmentIds.isEmpty()) {
                for (RoleAssignmentLocation location : roleAssignmentLocationRepository.findByRoleAssignmentIdIn(assignmentIds)) {
                    locations.add(location.getLocationCode());
                }
            }
            if (locations.isEmpty() && roles.contains("SYSTEM_ADMINISTRATOR")) {
                locations.add("NETWORK");
            }
            locationScope = new ArrayList<>(locations);
        }

        List<String> permissions = includePermissions
                ? permissionCatalog.resolve(roles)
                : List.of();

        return new SessionResponse(
                user.getUserIdentifier(),
                user.getEmail(),
                user.getDisplayName(),
                roles,
                locationScope,
                permissions,
                expiresAt
        );
    }

    public void assertAccountUsable(UserAccount user) {
        if (user.getAccountStatus() == AccountStatus.SUSPENDED) {
            throw new DomainException("AUTH_ACCOUNT_SUSPENDED", "Account is suspended", 401);
        }
        if (user.getAccountStatus() == AccountStatus.DEACTIVATED) {
            throw new DomainException("AUTH_ACCOUNT_DEACTIVATED", "Account is deactivated", 401);
        }
        if (!user.isLoginAllowed()) {
            throw new DomainException("AUTH_ACCOUNT_INACTIVE", "Account cannot sign in", 401);
        }
    }
}
