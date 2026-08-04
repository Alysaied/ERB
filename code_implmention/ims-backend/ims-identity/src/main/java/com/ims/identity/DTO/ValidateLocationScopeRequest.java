package com.ims.identity.DTO;

import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.Size;

public record ValidateLocationScopeRequest(

        String userId,
        @NotBlank @Size(max = 100)
        String locationCode,
        @Size(max = 100)
        String requiredPermission
) {
}
