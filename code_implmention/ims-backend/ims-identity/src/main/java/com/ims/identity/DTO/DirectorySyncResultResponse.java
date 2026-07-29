package com.ims.identity.DTO;

import java.time.Instant;
import java.util.List;

public record DirectorySyncResultResponse(
        String syncMode,
        int usersCreated,
        int usersUpdated,
        int usersDeactivated,
        List<SyncErrorResponse> errors,
        Instant syncedAt
) {
}
