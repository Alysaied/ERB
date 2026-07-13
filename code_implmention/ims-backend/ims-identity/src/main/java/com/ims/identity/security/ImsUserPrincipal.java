package com.ims.identity.security;

import java.time.Instant;

public record ImsUserPrincipal(
        String userIdentifier,
        String email,
        String displayName,
        String jti,
        Instant expiresAt
) {
}
