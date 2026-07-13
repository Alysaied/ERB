package com.ims.sharedkernel.problem;

public class DomainException extends RuntimeException {
    private final String errorCode;
    private final String businessRuleId;
    private final String validationRuleId;
    private final int status;

    public DomainException(String errorCode, String message, int status) {
        this(errorCode, message, status, null, null);
    }

    public DomainException(
            String errorCode,
            String message,
            int status,
            String businessRuleId,
            String validationRuleId
    ) {
        super(message);
        this.errorCode = errorCode;
        this.status = status;
        this.businessRuleId = businessRuleId;
        this.validationRuleId = validationRuleId;
    }

    public String getErrorCode() {
        return errorCode;
    }

    public String getBusinessRuleId() {
        return businessRuleId;
    }

    public String getValidationRuleId() {
        return validationRuleId;
    }

    public int getStatus() {
        return status;
    }
}
