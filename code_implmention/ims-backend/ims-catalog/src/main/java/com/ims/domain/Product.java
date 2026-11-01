package com.ims.domain;

import com.ims.enums.LifecycleStatus;
import jakarta.persistence.*;

import java.time.Instant;

@Entity
@Table(name="products",schema = "catalog")
public class Product {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
     private Long id;

    @Column(name="sku",length = 64,nullable = false,unique = true)
    private  String sku;

    @Column(name="product_name",length = 256,nullable = false)
    private String productName;

    @Column(name="description")
    private String description;

    @Column(name="unit_of_measure",nullable = false,length = 16)
    private String unitOfMeasure;

    @Column(name="category_code",length=64)
    private String  categoryCode;

    @Column(name="lifecycle_status",length=32,nullable = false)
    private String lifeCycleStatus = LifecycleStatus.ACTIVE.name();

    @Column(name="abc_classification",length = 1)
    private String abcClassification;

    @Column(name="is_shelf_life",nullable = false)
    private Boolean isShelfLife = false;

    @Column(name="is_traceable",nullable = false)
    private Boolean isTraceable = false;

    @Column(name="rotation_policy",length = 8)
    private String rotationPolicy;

    @Column(name="mrsl_days")
    private Integer mrslDays;

    @Column(name="superseded_by_sku",length=64)
    private String supersededBySku;

    @Column(name = "is_active",nullable = false)
    private Boolean isActive=true;

    @Column(name="version",nullable = false)
    private Integer version = 1 ;

    @Column(name="created_at",nullable = false)
    private Instant createdAt = Instant.now();

    @Column(name="updated_at",nullable = false)
    private Instant updatedAt = Instant.now();

    @Column(name="created_by")
    private Long createdBy;

    @Column(name="updated_by")
    private Long updatedBy;


    protected Product() {
    }

    public Product(
            String sku, String productName, String description, String unitOfMeasure,String categoryCode,
            String lifeCycleStatus,String abcClassification,Boolean isShelfLife,Boolean isTraceable,String rotationPolicy,Integer mrslDays,
            String supersededBySku,Boolean isActive,Integer version,Long updatedBy
    ){
        Instant now = Instant.now();
        this.sku=sku;
        this.productName=productName;
        this.description=description;
        this.unitOfMeasure=unitOfMeasure;
        this.categoryCode=categoryCode;
        this.lifeCycleStatus=lifeCycleStatus;
        this.abcClassification=abcClassification;
        this.isShelfLife=isShelfLife;
        this.isTraceable=isTraceable;
        this.supersededBySku=supersededBySku;
        this.isActive=isActive;
        this.version=version;
        this.createdAt=now;
        this.updatedAt=now;
        this.createdBy=updatedBy;
        this.updatedBy=updatedBy;
        this.rotationPolicy=rotationPolicy;

    }
    public static Product create(
            String sku,
            String productName,
            String description,
            String unitOfMeasure,
            String categoryCode,
            boolean isTraceable,
            String rotationPolicy,
            boolean isShelfLife,
            Integer mrslDays,
            Long createdBy
    ){
        Product p = new Product();
        p.sku= sku;
        p.productName=productName;
        p.description= description;
        p.unitOfMeasure= unitOfMeasure;
        p.categoryCode = categoryCode;
        p.lifeCycleStatus= LifecycleStatus.ACTIVE.name();
        p.isTraceable = isTraceable;
        p.rotationPolicy= rotationPolicy;
        p.isShelfLife=isShelfLife;
        p.mrslDays=mrslDays;
        p.isActive = true;
        p.createdAt = Instant.now();
        p.updatedAt = Instant.now();
        p.createdBy=createdBy;
        p.updatedBy=createdBy;
        return p ;
    }
    public void setId(Long id){
        this.id=id;
    }
    public Long getId(){
        return id;
    }
    public void setProductName(String name){
        this.productName=name;
    }
    public String getProductName(){
        return productName;
    }
    public void setSku(String sku){
        this.sku=sku;
    }
    public String getSku(){
        return sku;
    }
    public void setUnitOfMeasure(String uom){
        this.unitOfMeasure=uom;
    }
    public String getUnitOfMeasure(){
        return unitOfMeasure;
    }
    public void setCategoryCode(String cateCOde){
        this.categoryCode=cateCOde;
    }
    public String getCategoryCode(){
        return categoryCode;
    }
    public void setLifeCycleStatus(String status){
        this.lifeCycleStatus=status;
    }
    public String getLifeCycleStatus(){
        return this.lifeCycleStatus;
    }
    public void setAbcClassification(String abc){
        this.abcClassification=abc;
    }
    public String getAbcClassification(){
        return abcClassification;
    }
    public void setIsShelfLife(Boolean shelfLife){
        this.isShelfLife=shelfLife;
    }
    public Boolean getIsShelfLife(){
        return isShelfLife;
    }
    public void setIsTraceable(Boolean traceable){
        this.isTraceable=traceable;
    }
    public Boolean getIsTraceable(){
        return isTraceable;
    }

    public void setDescription(String des){
        this.description=des;
    }
    public String getDescription(){
        return description;
    }
    public void setRotationPolicy(String rotationPolicy){
        this.rotationPolicy=rotationPolicy;
    }
    public String getRotationPolicy(){
        return rotationPolicy;
    }
    public void setMrslDays(Integer mrslDays){
        this.mrslDays=mrslDays;
    }
    public Integer getMrslDays(){
        return mrslDays;
    }
    public void setIsActive( Boolean isActive){
        this.isActive=isActive;
    }
    public Boolean getIsActive(){
        return isActive;
    }
    public void setSupersededBySku(String supersededBySku){
        this.supersededBySku=supersededBySku;
    }
    public String getSupersededBySku(){
        return supersededBySku;
    }


    public Instant getCreatedAt() {
        return createdAt;
    }

    public Instant getUpdatedAt() {
        return updatedAt;
    }

    public Long getUpdatedBy(){
        return updatedBy;
    }

    public Long getCreatedBy(){
        return createdBy;
    }
}

