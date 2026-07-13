package com.ims.identity.application;

import com.ims.identity.api.dto.LocalTokenRequest;
import com.ims.identity.api.dto.LogoutResponse;
import com.ims.identity.api.dto.SessionResponse;
import com.ims.identity.api.dto.TokenResponse;
import com.ims.identity.domain.UserAccount;
import com.ims.identity.infrastructure.UserAccountRepository;
import com.ims.identity.security.JwtTokenService;
import com.ims.identity.security.TokenBlacklist;
import com.ims.sharedkernel.problem.DomainException;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.Instant;

@Service
public class AuthApplicationService {

    private final UserAccountRepository userAccountRepository;
    private final PasswordEncoder passwordEncoder;
    private final JwtTokenService jwtTokenService;
    private final SessionService sessionService;
    private final TokenBlacklist tokenBlacklist;

    public AuthApplicationService(
            UserAccountRepository userAccountRepository,
            PasswordEncoder passwordEncoder,
            JwtTokenService jwtTokenService,
            SessionService sessionService,
            TokenBlacklist tokenBlacklist
    ) {
        this.userAccountRepository = userAccountRepository;
        this.passwordEncoder = passwordEncoder;
        this.jwtTokenService = jwtTokenService;
        this.sessionService = sessionService;
        this.tokenBlacklist = tokenBlacklist;
    }

    /**
     * Local JWT issuance for Sprint 1 (replaces IdP until OIDC is wired — AUTH-01 / R-I03).
     */
    @Transactional
    public TokenResponse issueLocalToken(LocalTokenRequest request) {
        UserAccount user = userAccountRepository.findByEmailIgnoreCase(request.email().trim())
                .orElseThrow(() -> new DomainException("AUTH_INVALID_CREDENTIALS", "Invalid email or password", 401));

        sessionService.assertAccountUsable(user);

        if (user.getPasswordHash() == null || !passwordEncoder.matches(request.password(), user.getPasswordHash())) {
            throw new DomainException("AUTH_INVALID_CREDENTIALS", "Invalid email or password", 401);
        }

        user.markActivity();
        Instant expiresAt = jwtTokenService.defaultExpiry();
        String token = jwtTokenService.createAccessToken(user, expiresAt);
        SessionResponse session = sessionService.buildSession(user.getUserIdentifier(), expiresAt, true, true);
        return TokenResponse.bearer(token, expiresAt, session);
    }

    @Transactional(readOnly = true)
    public SessionResponse getSession(
            String userIdentifier,
            Instant expiresAt,
            boolean includePermissions,
            boolean includeLocationScope
    ) {
        return sessionService.buildSession(userIdentifier, expiresAt, includePermissions, includeLocationScope);
    }

    public LogoutResponse logout(String jti, Instant expiresAt, boolean logoutAllSessions) {
        if (jti != null && expiresAt != null) {
            tokenBlacklist.revoke(jti, expiresAt);
        }
        // logoutAllSessions reserved for Redis-backed session store in later sprints
        return new LogoutResponse(true, Instant.now());
    }
}
