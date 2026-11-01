package com.ims.identity.DTO;

import jakarta.validation.Valid;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.Size;

public record EvaluateAuthorizationRequest(
        @Size(max = 50)
        String userId,
        @NotBlank @Size(max = 100)
        String action,
        @Size(max = 50)
        String resourceType,
        @Size(max = 100)
        String resourceId,

        String locationCode
) {
    public EvaluateAuthorizationRequest(String userId, String action , String resourceType , String resourceId,String locationCode){
        this.userId=userId;
        this.action=action;
        this.resourceId=resourceId;
        this.resourceType=resourceType;
        this.locationCode=locationCode;

    }
}
