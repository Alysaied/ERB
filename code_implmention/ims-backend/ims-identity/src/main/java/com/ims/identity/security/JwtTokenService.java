package com.ims.identity.security;

import com.ims.identity.domain.UserAccount;
import io.jsonwebtoken.Claims;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.security.Keys;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

import javax.crypto.SecretKey;
import java.nio.charset.StandardCharsets;
import java.time.Duration;
import java.time.Instant;
import java.util.Date;
import java.util.UUID;

@Service
public class JwtTokenService {

    private final SecretKey secretKey;
    private final Duration tokenTtl;

    public JwtTokenService(
            @Value("${ims.security.jwt.secret}") String secret,
            @Value("${ims.security.jwt.ttl-minutes:480}") long ttlMinutes
    ) {
        if (secret == null || secret.length() < 32) {
            throw new IllegalStateException("ims.security.jwt.secret must be at least 32 characters");
        }
        this.secretKey = Keys.hmacShaKeyFor(secret.getBytes(StandardCharsets.UTF_8));
        this.tokenTtl = Duration.ofMinutes(ttlMinutes);
    }

    public Instant defaultExpiry() {
        return Instant.now().plus(tokenTtl);
    }

    public String createAccessToken(UserAccount user, Instant expiresAt) {
        Instant now = Instant.now();
        return Jwts.builder()
                .id(UUID.randomUUID().toString())
                .subject(user.getUserIdentifier())
                .claim("email", user.getEmail())
                .claim("displayName", user.getDisplayName())
                .issuedAt(Date.from(now))
                .expiration(Date.from(expiresAt))
                .signWith(secretKey)
                .compact();
    }

    public Claims parseClaims(String token) {
        return Jwts.parser()
                .verifyWith(secretKey)
                .build()
                .parseSignedClaims(token)
                .getPayload();
    }

    public SecretKey getSecretKey() {
        return secretKey;
    }
}
