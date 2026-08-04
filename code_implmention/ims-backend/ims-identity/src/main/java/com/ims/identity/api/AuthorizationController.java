package com.ims.identity.api;

import com.ims.identity.DTO.AuthorizationEvaluationResponse;
import com.ims.identity.DTO.EvaluateAuthorizationRequest;
import com.ims.identity.DTO.LocationScopeValidationResponse;
import com.ims.identity.DTO.ValidateLocationScopeRequest;
import com.ims.identity.application.AuthorizationService;
import com.ims.identity.security.ImsUserPrincipal;
import jakarta.validation.Valid;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/v1")
public class AuthorizationController {
    private final AuthorizationService authorizationService;
    public AuthorizationController(AuthorizationService authorizationService) {
        this.authorizationService = authorizationService;
    }
    @PostMapping("/authorization/actions/evaluate")
    AuthorizationEvaluationResponse evaluate(
            @AuthenticationPrincipal ImsUserPrincipal principal,
            @Valid @RequestBody EvaluateAuthorizationRequest request
    ) {
        String callerUserId = principal == null ? null : principal.userIdentifier();
        return authorizationService.evaluate(request, callerUserId);
    }

    @PostMapping("/authorization/location-scope/validate")
    LocationScopeValidationResponse validateLocationScope(
            @AuthenticationPrincipal ImsUserPrincipal principal,
            @Valid @RequestBody ValidateLocationScopeRequest request
    ) {
        String callerUserId = principal == null ? null : principal.userIdentifier();
        return authorizationService.validateLocationScope(request, callerUserId);
    }

}
