package com.ims.DTO;

import java.time.Instant;

public record ProductDetailResponse(
        String sku,
        String name,
        String lifeCycleStatus,
        String abcClass,
        String unitOfMeasure,
        String description,
        String categoryCode,
        String barcode,
        Boolean isTraceable,
        String rotationPolicy,
        Boolean shelfLifeManaged,
        Integer mrslThresholdDays,
        Instant createdAt,
        Instant updatedAt

) {
}
