package com.ims.identity.DTO;

import java.time.Instant;

public record RoleRevocationResponse(
        String roleAssignmentId,
        String userId,
        Instant revokedAt
) {
}
