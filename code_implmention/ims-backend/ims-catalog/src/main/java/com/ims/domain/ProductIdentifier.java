package com.ims.domain;

import jakarta.persistence.*;

import java.time.Instant;

@Entity
@Table(name = "product_identifiers", schema = "catalog")
public class ProductIdentifier {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name="product_id",nullable = false)
    private Long productId;

    @Column(name="identifier_type",nullable = false,length = 32)
    private String identifierType;

    @Column(name="identifier_value", nullable = false,length = 128)
    private String identifierValue;

    @Column(name="is_primary",nullable = false)
    private Boolean isPrimary = false;

    @Column(name="is_active",nullable = false)
    private Boolean isActive=true;

    @Column(name="created_at",nullable = false)
    Instant createdAt = Instant.now();

    protected  ProductIdentifier(){}
    public static ProductIdentifier barcode(Long productId,String value,boolean primary){
        ProductIdentifier i = new ProductIdentifier();
        i.productId=productId;
        i.identifierType="BARCODE";
        i.identifierValue=value;
        i.isPrimary=primary;
        i.isActive=true;
        i.createdAt=Instant.now();
        return i;
    }
    public String getIdentifierValue(){return identifierValue;}
}
