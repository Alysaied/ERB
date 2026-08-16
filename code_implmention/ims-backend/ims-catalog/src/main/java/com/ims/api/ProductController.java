package com.ims.api;

import com.ims.DTO.CreateProductRequest;
import com.ims.DTO.ProductDetailResponse;
import com.ims.application.ProductCatalogService;
import jakarta.validation.Valid;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/v1")
public class ProductController {
    private final ProductCatalogService productCatalogService;

    public ProductController(ProductCatalogService productCatalogService){
        this.productCatalogService=productCatalogService;
    }

    @PostMapping("/products")
    ResponseEntity<ProductDetailResponse> create(@Valid @RequestBody CreateProductRequest request){
        ProductDetailResponse body = productCatalogService.newProduct(request);
        return ResponseEntity.status(HttpStatus.CREATED).body(body);
    }
}
