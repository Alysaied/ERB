package com.ims.infrastructure;

import com.ims.domain.ProductIdentifier;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface ProductIdentifierRepository extends JpaRepository<ProductIdentifier, Long> {

    boolean existsByIdentifierTypeAndIdentifierValue(String identifierType, String identifierValue);
}
