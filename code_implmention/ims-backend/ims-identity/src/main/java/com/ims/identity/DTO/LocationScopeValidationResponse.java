package com.ims.identity.DTO;

import java.util.List;

public record LocationScopeValidationResponse(
        boolean authorized,
        String userId,
        String locationCode,
        List<String> scopedLocations
) {
}
