package com.ims.identity.DTO;

import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Size;

import java.time.LocalDate;
import java.util.List;

public record RoleAssignmentDto(
        @NotBlank(message="role code is required")
        @Size(max=50)
        String roleCode,

        List <@Size(max = 30)String> locationCodes,

        LocalDate effectiveFrom,
        LocalDate effectiveTo){
}
