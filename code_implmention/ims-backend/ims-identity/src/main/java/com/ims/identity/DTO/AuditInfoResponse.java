package com.ims.identity.DTO;

import java.time.Instant;
import java.time.LocalDate;

public record AuditInfoResponse(
        Instant createdAt,
        String  createdBy,
        Instant updatedAt,
        String  updatedBy
) {


}
