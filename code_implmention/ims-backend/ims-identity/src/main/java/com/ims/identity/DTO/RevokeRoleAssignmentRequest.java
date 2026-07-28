package com.ims.identity.DTO;

import jakarta.validation.Valid;
import jakarta.validation.constraints.Max;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Size;

public record RevokeRoleAssignmentRequest(
        @NotBlank @Valid
        String userId,

        Long roleAssignmentId,
        @Size(max = 500)
        String revocationReason
) {
}
