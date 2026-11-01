package com.ims.application;

import com.ims.DTO.CreateProductRequest;
import com.ims.DTO.ProductDetailResponse;
import com.ims.domain.Product;
import com.ims.domain.ProductIdentifier;
import com.ims.identity.DTO.AuditInfoResponse;
import com.ims.identity.DTO.EvaluateAuthorizationRequest;
import com.ims.identity.application.AuthorizationService;
import com.ims.identity.domain.UserAccount;
import com.ims.identity.infrastructure.UserAccountRepository;
import com.ims.identity.security.ImsUserPrincipal;
import com.ims.infrastructure.ProductIdentifierRepository;
import com.ims.infrastructure.ProductRepository;
import com.ims.sharedkernel.problem.DomainException;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
public class ProductCatalogService {

    private final ProductRepository productRepository;
    private final ProductIdentifierRepository productIdentifierRepository;
    private final UserAccountRepository userAccountRepository;
    private final AuthorizationService authorizationService;

    public ProductCatalogService(ProductRepository productRepository, ProductIdentifierRepository productIdentifierRepository,UserAccountRepository userAccountRepository,
                                 AuthorizationService authorizationService
    ) {
        this.productRepository = productRepository;
        this.productIdentifierRepository = productIdentifierRepository;
        this.userAccountRepository=userAccountRepository;
        this.authorizationService=authorizationService;
    }

    @Transactional
    public ProductDetailResponse newProduct(CreateProductRequest request , ImsUserPrincipal principal) {
        if(principal == null ||principal.userIdentifier() == null || principal.userIdentifier().isBlank()){
            throw new DomainException(
                    "AUTH_UNAUTHORIZED",
                    "Authentication required",
                    401
            );
        }
        UserAccount user = userAccountRepository.findByUserIdentifier(principal.userIdentifier())
                .orElseThrow(()-> new DomainException(
                        "AUTH_TOKEN_INVALID",
                        "User not found for userIdentifier: " + principal.userIdentifier(),
                        401,
                        null,
                        "VR-001"
                ));
        EvaluateAuthorizationRequest req = new EvaluateAuthorizationRequest(
                null,
                "PERM-001",
                null,
                null,null
        );
       if(!authorizationService.evaluate(req, user.getUserIdentifier()).isAuthorized()){
           throw new DomainException(
                   "AUTH_FORBIDDEN",
                   "User does not have permission to create product",
                   403,
                   null,
                   "VR-001"
           );
       }

        String sku = request.sku().trim();
        if(productRepository.existsBySku(sku)){
            throw new DomainException(
                    "CONF_DUPLICATE_SKU",
                    "Product SKU already exists : " + sku,
                    409,
                    null,
                    "VR-002"
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
                    400,
                    null,
                    "VR-003"

            );
        }
        if(traceable && (!rotation.equals("FIFO") && !rotation.equals("FEFO")) ){
            throw new DomainException(
                    "INVALID_ROTATION_POLICY",
                    "Invalid rotation policy. Only 'FIFO' and 'FEFO' are allowed when isTraceable is true",
                    400,
                    null,
                    "VR-003"
            );
        }
        if(shelfLife && (request.mrslThresholdDays()==null || request.mrslThresholdDays() < 1)){
            throw new DomainException(
                    "MRSL_REQUIRED",
                    "mrslThresholdDays is required when shelfLifeManaged is true",
                    400,
                    null,
                    "VR-003"
            );
        }
        if(barcode!= null
        && productIdentifierRepository.existsByIdentifierTypeAndIdentifierValue("BARCODE",barcode)){
            throw new DomainException(
                    "PRODUCT_BARCODE_EXISTS",
                    "Barcode already exists : " + barcode,
                    409,
                    null,
                    "VR-009"
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
                request.mrslThresholdDays(),
                user.getId()
        );
        product = productRepository.save(product);
        if(barcode != null){
            productIdentifierRepository.save(
                    ProductIdentifier.barcode(product.getId(),barcode,true)
            );
        }
        AuditInfoResponse audit= new AuditInfoResponse(
                product.getCreatedAt(),
                product.getCreatedBy(),
                product.getUpdatedAt(),
                product.getUpdatedBy()
        );
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
                audit

        );
    }
}
