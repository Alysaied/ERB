package com.ims.identity.api.dto;

import java.time.Instant;
import java.util.Map;

public record HealthCheckResponse(
        String status,
        Instant timestamp,
        String version,
        Map<String, String> components
) {
}
