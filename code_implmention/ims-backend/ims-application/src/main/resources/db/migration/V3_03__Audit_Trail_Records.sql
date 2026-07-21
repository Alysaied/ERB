CREATE SCHEMA IF NOT EXISTS audit;
CREATE TABLE audit.audit_trail_records (
  id BIGINT ,
  audit_event_reference VARCHAR(64) NOT NULL ,
  affected_entity_type VARCHAR(64) NOT NULL ,
  affected_entity_id BIGINT NOT NULL ,
  action_performed VARCHAR(32) NOT NULL ,
  user_id BIGINT NOT NULL ,
  role_at_action VARCHAR(64) Null,
  before_state JSONB ,
    after_state JSONB,
    approval_chain_ref VARCHAR(128) null,
    movement_record_id BIGINT ,
    event_timestamp TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),

    CONSTRAINT pk_audit_trail_records PRIMARY KEY (id),
    CONSTRAINT uk_audit_trail_ref_ts UNIQUE (audit_event_reference,event_timestamp),
    CONSTRAINT fk_audit_trail_user FOREIGN KEY (user_id) REFERENCES identity.user_accounts (id),
    CONSTRAINT chk_audit_trail_action CHECK ( action_performed IN ('CREATE','UPDATE','APPROVED','CANCEL') )
);
CREATE INDEX ix_audit_trail_records_entity ON audit.audit_trail_records(affected_entity_type, affected_entity_id,event_timestamp DESC );

CREATE INDEX ix_audit_trail_user ON audit.audit_trail_records(user_id, event_timestamp DESC );

CREATE INDEX ix_audit_trail_timestamp ON audit.audit_trail_records(event_timestamp DESC );

CREATE INDEX ix_audit_trail_movement ON audit.audit_trail_records(movement_record_id)
WHERE movement_record_id IS NOT NULL;