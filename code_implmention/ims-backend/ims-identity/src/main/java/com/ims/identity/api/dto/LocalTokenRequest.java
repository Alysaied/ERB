package com.ims.identity.api.dto;

import jakarta.validation.constraints.NotBlank;

public record LocalTokenRequest(
        @NotBlank String email,
        @NotBlank String password
) {
}
