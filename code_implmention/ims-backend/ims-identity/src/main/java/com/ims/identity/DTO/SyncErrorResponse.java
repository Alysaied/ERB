package com.ims.identity.DTO;

public record SyncErrorResponse(
        String userId,
        String code,
        String message
) {
}
