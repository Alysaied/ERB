package com.ims.identity.DTO;

import jakarta.validation.constraints.NotBlank;

import java.time.Instant;

public record SyncUsersFromDirectoryRequest(
        @NotBlank
        String syncMode,
        Instant sinceTimestamp,
        Boolean dryRun
) {
}
