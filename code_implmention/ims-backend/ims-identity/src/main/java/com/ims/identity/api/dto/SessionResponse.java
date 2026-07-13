package com.ims.identity.api.dto;

import java.time.Instant;
import java.util.List;

public record SessionResponse(
        String userId,
        String email,
        String displayName,
        List<String> roles,
        List<String> locationScope,
        List<String> permissions,
        Instant sessionExpiresAt
) {
}
