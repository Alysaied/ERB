package com.ims.identity.DTO;

import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Size;

import java.time.LocalDate;

public record DeactivateUserAccountRequest(
        @Size(max = 1000) @NotBlank
        String deactivationReason,
        LocalDate effectiveDate
) {
}
