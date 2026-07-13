package com.ims.identity.api;

import com.ims.identity.api.dto.LocalTokenRequest;
import com.ims.identity.api.dto.LogoutRequest;
import com.ims.identity.api.dto.LogoutResponse;
import com.ims.identity.api.dto.SessionResponse;
import com.ims.identity.api.dto.TokenResponse;
import com.ims.identity.application.AuthApplicationService;
import com.ims.identity.security.ImsUserPrincipal;
import jakarta.validation.Valid;
import org.springframework.http.HttpStatus;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/v1/auth")
public class AuthController {

    private final AuthApplicationService authApplicationService;

    public AuthController(AuthApplicationService authApplicationService) {
        this.authApplicationService = authApplicationService;
    }

    /**
     * Sprint 1 local token endpoint (dev JWT). Production path is OIDC IdP (AUTH-01).
     */
    @PostMapping("/token")
    @ResponseStatus(HttpStatus.OK)
    public TokenResponse issueToken(@Valid @RequestBody LocalTokenRequest request) {
        return authApplicationService.issueLocalToken(request);
    }

    /** API-173 */
    @GetMapping("/session")
    public SessionResponse getSession(
            @AuthenticationPrincipal ImsUserPrincipal principal,
            @RequestParam(defaultValue = "false") boolean includePermissions,
            @RequestParam(defaultValue = "true") boolean includeLocationScope
    ) {
        return authApplicationService.getSession(
                principal.userIdentifier(),
                principal.expiresAt(),
                includePermissions,
                includeLocationScope
        );
    }

    /** API-174 */
    @PostMapping("/logout")
    public LogoutResponse logout(
            @AuthenticationPrincipal ImsUserPrincipal principal,
            @RequestBody(required = false) LogoutRequest request
    ) {
        boolean logoutAll = request != null && Boolean.TRUE.equals(request.logoutAllSessions());
        return authApplicationService.logout(principal.jti(), principal.expiresAt(), logoutAll);
    }
}
