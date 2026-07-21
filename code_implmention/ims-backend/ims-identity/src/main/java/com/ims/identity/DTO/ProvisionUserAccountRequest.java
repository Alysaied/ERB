package com.ims.identity.DTO;

import jakarta.validation.Valid;
import jakarta.validation.constraints.*;

import java.util.List;

public record ProvisionUserAccountRequest(
        @NotBlank(message = "userId is required")
        @Size(max=50,message="userId must not exceed 50 characters")
        @Pattern(
                regexp ="^[A-Za-z0-9_]+$",
                message="userId must contain only alphanumeric characters and underscores"
        )
         String userId,
        @NotBlank(message="email is required")
        @Email(message="email must be a valid email address")
        @Size( max=254, message="email must not exceed 254 characters")
        String email,

        @NotBlank(message="displayName is required ")
        @Size(max = 200,message="displayName must not exceed 200 characters")
        String displayName,

        @NotEmpty(message="initialRoles must contain at least one role ")
        @Valid
        List<RoleAssignmentDto> initialRoles,

        @Size(max=100, message = "externalDirectoryId must not exceed 100 characters")
        String externalDirectoryId


) {
}
