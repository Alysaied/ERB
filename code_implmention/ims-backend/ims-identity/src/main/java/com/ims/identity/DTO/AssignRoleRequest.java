package com.ims.identity.DTO;

import jakarta.validation.Valid;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;

public record AssignRoleRequest(

        @NotNull @Valid
        RoleAssignmentDto roleAssignment
) {
}
