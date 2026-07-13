package com.ims.identity.api.dto;

import java.time.Instant;
import java.util.List;

public record TokenResponse(
        String accessToken,
        String tokenType,
        Instant expiresAt,
        SessionResponse session
) {
    public static TokenResponse bearer(String accessToken, Instant expiresAt, SessionResponse session) {
        return new TokenResponse(accessToken, "Bearer", expiresAt, session);
    }
}
