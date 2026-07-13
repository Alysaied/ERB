package com.ims.identity.security;

import org.springframework.stereotype.Component;

import java.time.Instant;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;

/**
 * In-memory JWT revoke list for Sprint 1 logout.
 * Replace with Redis when shared session store is introduced.
 */
@Component
public class TokenBlacklist {

    private final Map<String, Instant> revokedUntil = new ConcurrentHashMap<>();

    public void revoke(String jti, Instant expiresAt) {
        if (jti == null || expiresAt == null) {
            return;
        }
        revokedUntil.put(jti, expiresAt);
        purgeExpired();
    }

    public boolean isRevoked(String jti) {
        if (jti == null) {
            return false;
        }
        Instant until = revokedUntil.get(jti);
        if (until == null) {
            return false;
        }
        if (until.isBefore(Instant.now())) {
            revokedUntil.remove(jti);
            return false;
        }
        return true;
    }

    private void purgeExpired() {
        Instant now = Instant.now();
        revokedUntil.entrySet().removeIf(entry -> entry.getValue().isBefore(now));
    }
}
