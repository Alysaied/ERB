CREATE TABLE catalog.product_identifiers(
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY ,
    product_id BIGINT NOT NULL REFERENCES catalog.products (id),
    identifier_type VARCHAR(32) NOT NULL ,
    identifier_value VARCHAR(128) NOT NULL ,
    is_primary BOOLEAN NOT NULL DEFAULT FALSE,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    CONSTRAINT uk_product_identifiers_type_value UNIQUE (identifier_type, identifier_value)
);
