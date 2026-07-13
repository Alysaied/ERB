package com.ims.sharedkernel.problem;

import com.fasterxml.jackson.annotation.JsonInclude;

import java.time.Instant;
import java.util.List;

@JsonInclude(JsonInclude.Include.NON_NULL)
public record ProblemDetailResponse(
        String type,
        String title,
        int status,
        String detail,
        String instance,
        String errorCode,
        String businessRuleId,
        String validationRuleId,
        Instant timestamp,
        List<FieldError> errors
) {
    public record FieldError(String field, String message, String code) {}
}
