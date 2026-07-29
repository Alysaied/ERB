package com.ims.identity.application.port;

import java.time.Instant;

/**
 * External HR-directory identity (EXT-08). Mapped into local UserAccount by sync.
 */
public record DirectoryUser(
        String userId,
        String email,
        String displayName,
        boolean active,
        Instant modifiedAt
) {
}
