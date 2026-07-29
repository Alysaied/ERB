package com.ims.identity.DTO;

import jakarta.validation.constraints.Max;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Size;

import java.time.LocalDate;

public record SuspendUserAccountRequest(

        @NotBlank @Size(max=1000)
        String suspensionReason,
        LocalDate suspendedUntil
) {
}
