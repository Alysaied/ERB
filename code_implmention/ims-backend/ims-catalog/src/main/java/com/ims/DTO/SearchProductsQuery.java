package com.ims.DTO;

import com.ims.enums.LifecycleStatus;
import jakarta.validation.constraints.Size;

public record SearchProductsQuery(
        @Size(max=200)
         String name,

        String sku,
        @Size(max = 30)
        String  categoryCode,
        LifecycleStatus lifecycleStatus,
        String abcClass,
        @Size(max = 50)
        String barcode,
        @Size(min = 1)
        Integer page,
        @Size(max=100 , min = 1)
        Integer pageSize,
        String sortBy,
        String sortDirection
) {
}
