package com.ims.application;

import com.ims.DTO.CreateProductRequest;
import com.ims.DTO.ProductDetailResponse;
import com.ims.domain.Product;
import com.ims.domain.ProductIdentifier;
import com.ims.infrastructure.ProductIdentifierRepository;
import com.ims.infrastructure.ProductRepository;
import com.ims.sharedkernel.problem.DomainException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.Optional;

@Service
public class ProductCatalogService {

    private final ProductRepository productRepository;
    private final ProductIdentifierRepository productIdentifierRepository;

    public ProductCatalogService(ProductRepository productRepository, ProductIdentifierRepository productIdentifierRepository) {
        this.productRepository = productRepository;
        this.productIdentifierRepository = productIdentifierRepository;

    }

    @Transactional
    public ProductDetailResponse newProduct(CreateProductRequest request) {
        String sku = request.sku().trim();
        if(productRepository.existsBySku(sku)){
            throw new DomainException(
                    "PRODUCT_SKU_EXISTS",
                    "Product SKU already exists : " + sku,
                    409
            );
        }
        boolean traceable= Boolean.TRUE.equals(request.isTraceable());
        boolean shelfLife= Boolean.TRUE.equals(request.shelfLifeManaged());
        String rotation = request.rotationPolicy()== null ? null : request.rotationPolicy().trim();
        String barcode = request.barcode() == null|| request.barcode().isBlank()? null : request.barcode().trim();

        if(traceable && (rotation == null || rotation.isBlank() )){
            throw new DomainException(
                    "ROTATION_POLICY_REQUIRED",
                    "rotationPolicy is required when isTraceable is true",
                    400
            );
        }
        if(shelfLife && (request.mrslThresholdDays()==null || request.mrslThresholdDays() < 1)){
            throw new DomainException(
                    "MRSL_REQUIRED",
                    "mrslThresholdDays is required when shelfLifeManaged is true",
                    400
            );
        }
        if(barcode!= null
        && productIdentifierRepository.existsByIdentifierTypeAndIdentifierValue("BARCODE",barcode)){
            throw new DomainException(
                    "PRODUCT_BARCODE_EXISTS",
                    "Barcode already exists : " + barcode,
                    409
            );
        }
        Product product = Product.create(
                sku,
                request.name().trim(),
                request.description(),
                request.unitOfMeasure().trim(),
                request.categoryCode(),
                traceable,
                rotation,
                shelfLife,
                request.mrslThresholdDays()
        );
        product = productRepository.save(product);
        if(barcode != null){
            productIdentifierRepository.save(
                    ProductIdentifier.barcode(product.getId(),barcode,true)
            );
        }
        return new ProductDetailResponse(
                product.getSku(),
                product.getProductName(),
                product.getLifeCycleStatus(),
                product.getAbcClassification(),
                product.getUnitOfMeasure(),
                product.getDescription(),
                product.getCategoryCode(),
                barcode,
                product.getIsTraceable(),
                product.getRotationPolicy(),
                product.getIsShelfLife(),
                product.getMrslDays(),
                product.getCreatedAt(),
                product.getUpdatedAt()

        );
    }
}
