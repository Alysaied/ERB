package com.ims.identity.DTO;

import java.time.LocalDate;
import java.util.List;

public record RoleAssignmentResponse(
        String roleAssignmentId,
        String roleCode,
        List<String> locationCodes,
        LocalDate effectiveFrom,
        LocalDate effectiveTo
) {
}
