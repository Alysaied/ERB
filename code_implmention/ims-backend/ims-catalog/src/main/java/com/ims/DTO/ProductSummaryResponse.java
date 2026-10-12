package com.ims.DTO;

public record ProductSummaryResponse(
        String sku,
        String name,
        String lifeCycleStatus,
        String abcClass,
        String unitOfMeasure
) {
}
