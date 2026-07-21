package com.ims.audit.domain;

import com.fasterxml.jackson.databind.JsonNode;
import com.ims.audit.enums.AuditAction;
import jakarta.persistence.*;
import lombok.*;
import org.hibernate.annotations.JdbcTypeCode;
import org.hibernate.type.SqlTypes;

import java.time.OffsetDateTime;

    @Entity
    @Table(name = "audit_trail_records", schema = "audit")
    @Getter
    @AllArgsConstructor
    @NoArgsConstructor(access= AccessLevel.PROTECTED)
    @Builder
    public class AuditTrailRecords {
        @Id
        @GeneratedValue(strategy = GenerationType.IDENTITY )
        private Long id;

        @Column(name = "audit_event_reference",length = 64, nullable = false)
        private String auditEventReference;

        @Column(name="affected_entity_type",length = 64,nullable=false)
        private String affectedEntityType;

        @Column(name="affected_entity_id",nullable = false)
        private Long affectedEntityId;

        @Enumerated(EnumType.STRING)
        @Column(name="action_performed",length =32,nullable=false)
        private AuditAction actionPerformed;

        @Column(name="user_id",nullable = false)
        private Long userId;

        @Column(name="role_at_action",length =64,nullable = true)
        private String roleAtAction;

        @JdbcTypeCode(SqlTypes.JSON)
        @Column(name="before_state",columnDefinition = "jsonb")
        private JsonNode beforeState;

        @JdbcTypeCode(SqlTypes.JSON)
        @Column(name="after_state",columnDefinition = "jsonb")
        private JsonNode afterState;

        @Column(name="approval_chain_ref",length =128,nullable = true )
        private String approvalChainRef;

        @Column(name="movement_record_id",nullable = true)
        private Long movementRecordId;

        @Column(name="event_timestamp",nullable = false)
        private OffsetDateTime eventTimestamp;

        @Column(name="created_at",nullable = false)
        private OffsetDateTime createdAt;

    }
    
