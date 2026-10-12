package com.ims.DTO;

import com.ims.identity.DTO.AuditInfoResponse;

public record ProductDetailResponse(
        String sku,
        String name,
        String lifecycleStatus,
        String abcClass,
        String unitOfMeasure,
        String description,
        String categoryCode,
        String barcode,
        Boolean isTraceable,
        String rotationPolicy,
        Boolean shelfLifeManaged,
        Integer mrslThresholdDays,
        AuditInfoResponse audit

) {
}
