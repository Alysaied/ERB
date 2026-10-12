package com.ims.identity.DTO;

import java.time.Instant;
import java.time.LocalDate;

public record AuditInfoResponse(
        Instant createdAt,
        String  createdBy,
        Instant updatedAt,
        String  updatedBy
) {


    public AuditInfoResponse(Instant createdAt, Long createdBy, Instant updatedAt, Long updatedBy) {

        this(createdAt, createdBy != null ?
                createdBy.toString() : null,
                updatedAt, updatedBy != null ?
                        updatedBy.toString() : null);
    }
}
