# System Context
## Inventory Management System

---

## Document Information

| Attribute | Detail |
|-----------|--------|
| **Document ID** | SRS-SA-002 |
| **Document Title** | System Context — Inventory Management System |
| **Version** | 1.0 |
| **Status** | Draft |
| **Document Owner** | Solution Architect |
| **Source Documents** | BRD-IMS-001, SRS-ES-004, SRS-DM-007, SRS-UC-001, Business Constraints (TEC-01 – TEC-06) |
| **Date** | July 6, 2026 |
| **Scope** | C4 Level 1 — system boundary, users, external systems, and third-party services; no internal module design |

### Purpose

This document defines the **System Context** for the Inventory Management System (IMS) — the single boundary within which inventory truth is established, governed, and consumed. It identifies who and what interacts with IMS, what data crosses each boundary, and why each interaction exists.

### System Purpose (Context Summary)

The IMS is the organization's **inventory system of record** — authoritative for stock quantities, movements, reservations, replenishment state, and inventory audit evidence. It is **not** the enterprise system of record for sales, finance, HR, or channel commerce (BRD §8.2; TEC-01).

---

## 1. Primary Users

IMS serves **19 business user roles** (BRD §11). External trading partners do **not** hold standing IMS accounts in MVP scope. Users access IMS via standard web browser on company-approved devices (TEC-03, TEC-06).

### 1.1 User Groups

| Group | User Roles | Primary Purpose |
|-------|------------|-----------------|
| **Operations & Warehouse** | Inventory Controller, Receiving Clerk, Warehouse Staff, Picker/Packer, Warehouse Manager, Regional/Store Manager, Operations Director | Record and control physical inventory — receive, store, count, transfer, pick, ship, quarantine |
| **Supply & Procurement** | Buyer, Purchasing Manager | Authorize inbound supply — requisitions, purchase orders, inbound planning, replenishment response |
| **Commercial & Customer-Facing** | Sales Representative, Customer Service Representative, Marketing Manager | Confirm availability, reserve and fulfill orders, manage returns, ring-fence promotional stock |
| **Finance & Governance** | Finance Manager, Internal Auditor, External Auditor *(temporary)* | Reconcile valuation, three-way match, audit trail review, control testing |
| **Executive Oversight** | CEO, CFO | Review inventory KPIs, valuation alignment, strategic performance |
| **Technology Administration** | System Administrator | Provision users, assign location-scoped roles, enforce SoD at access layer |

### 1.2 Primary User Detail

| ID | Role | Key Interactions With IMS |
|----|------|---------------------------|
| UR-01 | Inventory Controller | Product/location master, policies, counts, opening balances, governance |
| UR-02 | Receiving Clerk | Goods receipt verification, discrepancies, return receipt |
| UR-03 | Warehouse Staff | Put-away, cycle count, transfer dispatch/receipt |
| UR-04 | Picker/Packer | Pick verification, shipment dispatch |
| UR-05 | Warehouse Manager | Approvals, quarantine, adjustments, exceptions, returns disposition |
| UR-06 | Regional/Store Manager | Transfer requests, local stock monitoring |
| UR-07 | Operations Director | Transfer/adjustment approval, network rebalancing, executive operations view |
| UR-08 | Buyer | Purchase orders, inbound scheduling, replenishment execution |
| UR-09 | Purchasing Manager | Requisition approval, low-stock response |
| UR-10 | Sales Representative | ATP inquiry, order availability confirmation |
| UR-11 | Customer Service Representative | Order confirm/cancel, reservation, backorder, RMA, fulfillment status |
| UR-12 | Marketing Manager | Promotional stock allocation, campaign readiness |
| UR-13 | Finance Manager | Supplier invoice, three-way match, valuation snapshot, GL reconciliation |
| UR-14 | Internal Auditor | Read-only audit trail, movement history, SoD evidence |
| UR-15 | External Auditor | Temporary read-only access during statutory audit |
| UR-16 | CEO / CFO | Executive dashboards and KPI reports |
| UR-17 | System Administrator | User accounts, role assignments, location scope |

---

## 2. External Systems

External systems are organization or partner systems **outside the IMS boundary** that exchange business facts or receive inventory-derived information. Integration depth varies by phase (TEC-04, TEC-05).

| ID | External System | MVP Integration | Phase |
|----|-----------------|-----------------|-------|
| EXT-01 | **Sales / Order Management (CRM)** | Manual or batch order intake; CS/Sales enter fulfillment commands | MVP: indirect; Phase 2+: API/ACL |
| EXT-02 | **Finance ERP / General Ledger** | Scheduled export; manual reconciliation (TEC-05) | MVP: manual; Phase 3: automated ACL |
| EXT-03 | **Sales Channel / E-Commerce / Marketplace** | No real-time feed (TEC-04); manual stock updates | Phase 2+ |
| EXT-04 | **Supplier / Vendor** | PO communicated outside IMS; physical delivery triggers receipt | MVP: human-mediated |
| EXT-05 | **Logistics / Carrier Partner** | Tracking and delay info via operational workflow | MVP: human-mediated |
| EXT-06 | **Customer (B2B / B2C)** | No direct IMS access; interacts via sales channels and CS | External participant |
| EXT-07 | **Marketing / Campaign Planning** | Campaign plans may originate externally; IMS holds ring-fence | Phase 2 |
| EXT-08 | **HR / Enterprise Directory** | User identity source for provisioning | MVP: manual or sync |
| EXT-09 | **Customs / Regulatory Authority** | Clearance decisions affect quarantine release | Phase 2 if bonded in scope |

*Trading partners (EXT-04, EXT-05, EXT-06) do not execute commands inside IMS — internal actors record outcomes.*

---

## 3. Third-Party Services

Third-party services are **managed capabilities** consumed by IMS infrastructure. They are not business participants but enable security, notification, resilience, and operations.

| ID | Third-Party Service | Purpose | MVP |
|----|---------------------|---------|-----|
| SVC-01 | **Enterprise Identity Provider (SSO / Directory)** | Authenticate users; optional federated identity (LDAP/Entra ID/Okta) | Should Have |
| SVC-02 | **Email / Notification Gateway** | Deliver low-stock alerts, approval requests, exception escalations (NFR-PERF-014) | Must Have |
| SVC-03 | **SMS Gateway** *(optional)* | Urgent operational alerts for warehouse supervisors | Could Have |
| SVC-04 | **Cloud Hosting Platform** | Run IMS application and data services | Must Have |
| SVC-05 | **Backup & Disaster Recovery Service** | Protect stock balances, transactions, audit logs; ≤15-min RPO (NFR-BDR-001) | Must Have |
| SVC-06 | **Monitoring & Alerting Platform** | Availability, performance, error, and KPI monitoring (NFR-MON) | Must Have |
| SVC-07 | **Certificate / Secrets Management** | TLS, API keys, credential rotation | Must Have |
| SVC-08 | **Time Synchronization (NTP)** | Consistent timestamps for audit trail and movement ordering | Must Have |

*Excluded from business context (infrastructure only): report rendering engine, internal job scheduler — treated as IMS internal components.*

---

## 4. Data Exchanged & Communication Purpose

### 4.1 User ↔ IMS

| User Group | Data Sent to IMS | Data Received From IMS | Communication Purpose |
|------------|------------------|------------------------|----------------------|
| Operations & Warehouse | Receipt lines, put-away confirmations, count results, transfer dispatch/receipt, pick/ship confirmations, quarantine actions, adjustments | Stock positions, ATP, location status, freeze alerts, pick lists, transfer authorizations, operational alerts | Execute and control physical inventory with governed accuracy |
| Supply & Procurement | Requisitions, POs, inbound schedules, delay notices | Low-stock alerts, network ATP, inbound pipeline status, replenishment recommendations | Commit and track inbound supply |
| Commercial | Availability checks, order confirm/cancel, reservations, backorders, RMAs, promotional allocations | ATP by SKU/location, reservation status, shipment status, backorder pipeline, campaign readiness | Sell and fulfill without overselling |
| Finance & Governance | Supplier invoices, match decisions, valuation reconciliation inputs | Movement history, receipt facts, match results, valuation snapshots, write-off records, audit exports | Financial control and statutory audit |
| Executive | Report filters, dashboard scope | KPIs — fill rate, accuracy, turnover, stockout, valuation variance | Strategic oversight |
| System Administrator | User profiles, role assignments, location scope | SoD violation alerts, access audit log | Secure, scoped access |

### 4.2 External System ↔ IMS

| External System | Direction | Data Exchanged | Communication Purpose |
|-----------------|-----------|----------------|----------------------|
| **Sales / Order Management** | → IMS | Order header, line items (SKU, qty), ship-from preference, customer ref | Initiate availability check and reservation |
| | ← IMS | ATP confirmation, reservation ID, fulfillment status, shipment notice | Prevent oversell; synchronize order execution state |
| **Finance ERP / GL** | → IMS | GL inventory balance, cost method parameters, period status | Month-end reconciliation |
| | ← IMS | Valuation snapshot, adjustment/write-off facts, three-way match outcome, consignment transfer events | Align operational and financial inventory records |
| **Sales Channel / E-Commerce** | ← IMS *(Phase 2+)* | ATP or available qty feed by SKU/channel | Reduce channel oversell (TEC-04 risk mitigation) |
| **Supplier / Vendor** | → IMS *(via clerk)* | ASN/delivery notice, invoice, discrepancy response | Trigger receipt verification and invoice match |
| | ← IMS *(via buyer)* | PO, PO change/cancel, discrepancy claim | Commercial commitment and claims |
| **Logistics / Carrier** | → IMS *(via staff)* | Pickup confirmation, delivery proof, delay reason | Complete shipment/transfer; record in-transit delays |
| | ← IMS *(via staff)* | Shipment/transfer dispatch notice | Coordinate pickup |
| **Customer** | → IMS *(via CS/channel)* | Order, cancellation, backorder ack, return request | Demand and reverse logistics intake |
| | ← IMS *(via CS/channel)* | Availability answer, shipment tracking, RMA, backorder notice | Customer commitment and service |
| **Marketing / Campaign** | → IMS | Campaign SKU list, qty, channel, period | Ring-fence stock for promotional readiness |
| | ← IMS | Allocation status, readiness gap alerts | Campaign launch confidence |
| **HR / Directory** | → IMS | Employee ID, name, department, status | Provision/deprovision user accounts |
| **Customs / Regulatory** | → IMS *(via compliance)* | Clearance grant, hold notice, recall directive | Release or hold bonded/quarantined stock |
| **External Auditor** | ← IMS | Audit trail export, movement history, count certification, SoD evidence | Independent control testing |

### 4.3 Third-Party Service ↔ IMS

| Service | Data Exchanged | Communication Purpose |
|---------|----------------|----------------------|
| Identity Provider | Auth tokens, user claims, group membership | Single sign-on; unique user attribution (NFR-SEC-001) |
| Email / SMS Gateway | Alert payloads, recipient, delivery status | Timely operational notification (NFR-PERF-014) |
| Cloud Platform | Compute, storage, network | Host application and data |
| Backup / DR | Database snapshots, transaction logs, config | Business continuity; ≤15-min RPO (NFR-BDR-001) |
| Monitoring | Metrics, logs, traces, alert events | Detect outage within 5 min (NFR-MON-001) |

---

## 5. Text-Based Context Diagram

### 5.1 C4 System Context (Primary View)

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                           EXTERNAL PARTICIPANTS & SYSTEMS                                    │
└─────────────────────────────────────────────────────────────────────────────────────────────┘

  ┌──────────────┐     order lines,        ┌──────────────┐     PO, invoice,     ┌──────────────┐
  │   Customer   │────availability,────────│  Sales /     │────ATP, reservation,│   Finance    │
  │  (B2B/B2C)   │    shipment, RMA       │    Order     │    fulfillment,     │  ERP / GL    │
  └──────┬───────┘                        │  Management  │    valuation snap   └──────┬───────┘
         │                                └──────┬───────┘                            │
         │ via CS / channel                        │                                    │
         │                                         │                                    │
         │         ┌──────────────┐                │         ┌──────────────┐          │
         │         │   Supplier   │──goods, invoice─│         │  Marketing   │          │
         │         │   / Vendor   │                │         │  / Campaign  │          │
         │         └──────┬───────┘                │         └──────┬───────┘          │
         │                │                        │                │                    │
         │         ┌──────┴───────┐                │         ┌──────┴───────┐          │
         │         │  Logistics / │──tracking──────┤         │   Customs /  │          │
         │         │   Carrier    │                │         │  Regulatory  │          │
         │         └──────────────┘                │         └──────────────┘          │
         │                                         │                                    │
         │         ┌──────────────┐                │                                    │
         └────────►│ Sales Channel│◄──ATP feed────┤                                    │
                   │ / E-Commerce │  (Phase 2+)   │                                    │
                   └──────────────┘                │                                    │
                                                   │                                    │
┌──────────────────────────────────────────────────┼────────────────────────────────────┼───────┐
│  PRIMARY USERS (19 roles)                        │                                    │       │
│                                                  ▼                                    ▼       │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────────────────────────────────┐ │
│  │  Operations &   │  │ Supply &        │  │                                             │ │
│  │  Warehouse (7)  │  │ Procurement (2) │  │     INVENTORY MANAGEMENT SYSTEM (IMS)       │ │
│  └────────┬────────┘  └────────┬────────┘  │                                             │ │
│           │                    │            │  • Single source of inventory truth         │ │
│  ┌────────┴────────┐  ┌────────┴────────┐  │  • Stock positions, ATP, reservations       │ │
│  │  Commercial &   │  │ Finance &       │  │  • Movements, counts, adjustments           │ │
│  │  Customer (3)   │  │ Governance (4)  │  │  • Fulfillment, replenishment, transfers    │ │
│  └────────┬────────┘  └────────┬────────┘  │  • Audit trail & operational intelligence   │ │
│           │                    │            │                                             │ │
│  ┌────────┴────────┐  ┌────────┴────────┐  └──────────────────────┬──────────────────────┘ │
│  │  Executive (2)  │  │ Sys Admin (1)   │                         │                        │
│  └─────────────────┘  └─────────────────┘                         │                        │
│         transactions, queries, approvals, exports                  │                        │
└────────────────────────────────────────────────────────────────────┼────────────────────────┘
                                                                     │
                    ┌────────────────────────────────────────────────┼────────────────────┐
                    │              THIRD-PARTY SERVICES              │                    │
                    │                                                ▼                    │
                    │   ┌─────────────┐  ┌─────────────┐  ┌─────────────────┐           │
                    │   │  Identity   │  │   Email /   │  │    Cloud Host   │           │
                    │   │  Provider   │  │ Notification│  │    Platform     │           │
                    │   │   (SSO)     │  │   Gateway   │  └────────┬────────┘           │
                    │   └─────────────┘  └─────────────┘           │                    │
                    │   ┌─────────────┐  ┌─────────────┐  ┌─────────┴────────┐           │
                    │   │  Backup &   │  │ Monitoring  │  │    HR / Directory │           │
                    │   │     DR      │  │  Platform   │  │   (identity feed) │           │
                    │   └─────────────┘  └─────────────┘  └──────────────────┘           │
                    └─────────────────────────────────────────────────────────────────────┘

                    ┌──────────────┐
                    │  External    │──── read-only audit exports ────► IMS
                    │   Auditor    │
                    └──────────────┘
```

### 5.2 Simplified Context Diagram (Relationships Only)

```
                                    ┌─────────────────┐
                                    │  Sales Channel  │
                                    │  / E-Commerce   │◄──── ATP / availability (Phase 2+)
                                    └────────┬────────┘
                                             │
    ┌─────────────┐    orders / lines       │         valuation / match
    │   Sales /   │◄───────────────────────┼──────────────────────►┌─────────────┐
    │    Order    │    fulfillment status  │                        │   Finance   │
    │  Management │────────────────────────┼───────────────────────►│  ERP / GL   │
    └──────┬──────┘                        │                        └─────────────┘
           │                               │
           │         ┌─────────────────────┴─────────────────────┐
           │         │                                           │
           ▼         ▼                                           ▼
    ┌──────────┐  ┌──────────────────────────────────────┐  ┌──────────┐
    │ Customer │  │   INVENTORY MANAGEMENT SYSTEM        │  │ Marketing│
    │ B2B/B2C  │  │   (Inventory System of Record)       │  │ Campaign │
    └──────────┘  └──────────────────┬───────────────────┘  └──────────┘
           ▲                         │
           │                         │ movements, receipts,
    ┌──────┴──────┐                  │ reservations, audit
    │  Commercial │                  │
    │  CS / Sales │──────────────────┤
    │  Marketing  │                  │
    └─────────────┘                  │
    ┌─────────────┐                  │                    ┌─────────────┐
    │  Operations │──────────────────┤                    │  External   │
    │  Warehouse  │                  │                    │   Auditor   │
    └─────────────┘                  │                    └──────┬──────┘
    ┌─────────────┐                  │                           │
    │ Procurement │──────────────────┤                           │ read-only
    └─────────────┘                  │                           │
    ┌─────────────┐                  │                           │
    │   Finance   │──────────────────┘                           │
    │  Governance │◄─────────────────────────────────────────────┘
    └─────────────┘
    ┌─────────────┐
    │  Executive  │──────────────────► dashboards / KPIs
    └─────────────┘
    ┌─────────────┐
    │ Sys Admin   │──────────────────► users / roles / access
    └─────────────┘

           ▲                    ▲                    ▲
           │                    │                    │
    ┌──────┴──────┐      ┌──────┴──────┐      ┌──────┴──────┐
    │  Supplier   │      │  Logistics  │      │  Customs /  │
    │  / Vendor   │      │  / Carrier  │      │ Regulatory  │
    └─────────────┘      └─────────────┘      └─────────────┘
      goods, invoices      shipments, delays     clearance, holds
      (via receiving)      (via warehouse)       (via compliance)

    ═══════════════════════════════════════════════════════════════
    THIRD-PARTY (infrastructure): SSO · Email · Cloud · Backup · Monitoring
    ═══════════════════════════════════════════════════════════════
```

### 5.3 Interaction Legend

| Symbol | Meaning |
|--------|---------|
| `───►` | Primary data or command flow |
| `◄───` | Response, query result, or outbound notification |
| `(Phase 2+)` | Not in MVP integration scope per TEC-04 / TEC-05 |
| `via clerk/staff` | Human-mediated — no direct system integration in MVP |

---

## 6. System Boundary Rules

| Rule | Statement |
|------|-----------|
| **SB-01** | IMS owns inventory quantity state, movement history, and inventory audit evidence |
| **SB-02** | IMS does **not** own general ledger, customer master, pricing, or sales pipeline |
| **SB-03** | Customer orders may **originate** in Sales/Order Management; IMS owns **fulfillment-relevant subset** via ACL |
| **SB-04** | Finance ERP remains **financial system of record**; IMS publishes operational valuation facts |
| **SB-05** | External trading partners interact through **business workflows**, not standing IMS accounts (MVP) |
| **SB-06** | Notifications are **delivered** via third-party gateways; alert **content and routing** are IMS responsibility |
| **SB-07** | Channel ATP sync is **out of MVP scope** (TEC-04); oversell risk managed by manual process until Phase 2 |

---

## 7. Phase Integration Summary

| Integration | MVP (Months 0–6) | Phase 2 (6–12) | Phase 3 (12–18) |
|-------------|------------------|----------------|-----------------|
| Sales / Order Management | Manual entry / batch import | API with ACL | Bi-directional status sync |
| Finance ERP | Export + manual reconcile (TEC-05) | Scheduled file / API | Automated valuation alignment |
| Sales Channel | Manual stock updates | ATP feed | Real-time availability |
| Supplier | Human workflow | Optional ASN import | Supplier portal (long-term) |
| Marketing Campaign | In-app only | External campaign feed ACL | — |
| HR Directory | Manual provisioning | Directory sync | Federated SSO |

---

## Document Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Solution Architect | | | |
| Product Owner | | | |
| Domain Expert | | | |
| Security Engineer | | | |

---

*End of System Context*

*Document ID: SRS-SA-002 | Version 1.0 | July 6, 2026*
