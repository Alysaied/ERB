package com.ims.DTO;

import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Pattern;
import jakarta.validation.constraints.Size;

public record CreateProductRequest(
        @Size(max=50) @NotBlank
        @Pattern(regexp = "^[A-Z0-9][A-Z0-9_-]*$", message="Invalid SKU format")
        String sku,
        @Size(max=200) @NotBlank
        String name,
        @Size(max=2000)
        String description,
        @Size(max = 10)@NotBlank
        String unitOfMeasure,
        @Size(max = 30)
        String categoryCode,
        @Size(max = 50)
        String barcode,
        Boolean isTraceable,
        String rotationPolicy,
        Boolean shelfLifeManaged,
        Integer mrslThresholdDays
) {

}
