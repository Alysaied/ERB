package com.ims.identity.DTO;

import java.util.List;

public record UserAccountResponse(
        String userId,
        String email,
        String displayName,
        String status,
        List<RoleAssignmentResponse>roles,
        AuditInfoResponse audit
) {
}
