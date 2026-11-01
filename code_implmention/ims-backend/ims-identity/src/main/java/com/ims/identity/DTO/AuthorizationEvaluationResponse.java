package com.ims.identity.DTO;

public record AuthorizationEvaluationResponse(
        boolean authorized,
        String userId,
        String action,
        String denialReason
) {
    public boolean isAuthorized() {
        return this.authorized;
    }

}
