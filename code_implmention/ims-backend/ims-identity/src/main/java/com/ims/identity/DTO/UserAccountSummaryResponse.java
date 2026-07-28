package com.ims.identity.DTO;

import java.time.Instant;
import java.util.List;

public record UserAccountSummaryResponse(
        String userId,
        String email,
        String displayName,
        String status,
        List<String> roles,
        boolean hasSodConflict,
        Instant lastActivityAt
) {
}
