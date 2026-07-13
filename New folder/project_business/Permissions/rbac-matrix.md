# Role-Based Access Control (RBAC) Matrix: Inventory Management System

**Document Owner:** Security Engineer  
**Purpose:** Define the authoritative mapping of business roles to system permissions for the Inventory Management System  
**Audience:** Security engineers, system administrators, auditors, and solution architects  
**Scope:** RBAC assignment matrix with business justification for sensitive permissions — location scoping rules apply as a cross-cutting constraint (see Section 5)  
**Based On:** User Roles (UR-01–UR-19), System Permissions (PERM-001–PERM-100), Permission Groups, Role Responsibilities, and Business Role Hierarchy

---

## Document Conventions

| Symbol | Meaning |
|--------|---------|
| ✔ | Permission allowed for the role |
| ✖ | Permission not allowed for the role |
| **UR-xx** | User Role identifier |
| **PERM-xxx** | Permission identifier |

**Legend — Role Abbreviations**

| Abbr | Role | UR |
|------|------|-----|
| CEO | Chief Executive Officer | UR-01 |
| COO | Chief Operating Officer | UR-02 |
| CFO | Chief Financial Officer | UR-03 |
| OpsDir | Operations Director | UR-04 |
| InvCtrl | Inventory Controller | UR-05 |
| WHMgr | Warehouse Manager | UR-06 |
| RcvClk | Receiving Clerk | UR-07 |
| PikPak | Warehouse Picker / Packer | UR-08 |
| WHStf | Warehouse Staff | UR-09 |
| RegMgr | Regional / Store Manager | UR-10 |
| SalMgr | Sales Manager | UR-11 |
| SalRep | Sales Representative | UR-12 |
| CsRep | Customer Service Representative | UR-13 |
| MktMgr | Marketing Manager | UR-14 |
| PurMgr | Purchasing Manager | UR-15 |
| Buyer | Buyer / Procurement Officer | UR-16 |
| FinMgr | Finance Manager / Accountant | UR-17 |
| IntAud | Internal Auditor | UR-18 |
| ExtAud | External Auditor | UR-19 |

---

## 1. RBAC Design Principles

| Principle | Application in This Matrix |
|-----------|---------------------------|
| **Least privilege** | Roles receive only permissions required for documented responsibilities |
| **Segregation of duties (SoD)** | Initiate/approve pairs are never granted to the same role (e.g., Buyer cannot approve own PO) |
| **Location scoping** | Transactional permissions are constrained to assigned locations; network-wide visibility granted only where responsibilities require it |
| **Executive read-only** | CEO and CFO have broad visibility without transactional authority |
| **Audit independence** | Auditors have read/query access only — no operational transactions |
| **Count independence** | Counters (WHStf) cannot approve their own count results (InvCtrl or WHMgr approves) |

**Note:** PERM-095 (Manage User Accounts) and PERM-096 (Assign User Roles and Location Scope) are not assigned to any business role in this matrix. These permissions are reserved for a technical System Administrator role outside the business role catalog (see User Roles document).

---

## 2. Permission Group Summary Matrix

High-level role-to-group assignment for planning and review. ✔ indicates the role holds one or more permissions within the group.

| Role | PG-01 Products | PG-02 Locations | PG-03 Visibility | PG-04 Control | PG-05 Transfers | PG-06 Purchasing | PG-07 Receiving | PG-08 Fulfillment | PG-09 Returns | PG-10 Commercial | PG-11 Reports | PG-12 Finance | PG-13 Setup | PG-14 Admin | PG-15 Audit |
|------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| CEO | ✖ | ✖ | ✔ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✔ | ✔ | ✖ | ✖ | ✖ |
| COO | ✖ | ✔ | ✔ | ✔ | ✔ | ✔ | ✖ | ✔ | ✖ | ✔ | ✔ | ✔ | ✖ | ✖ | ✖ |
| CFO | ✖ | ✖ | ✔ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✔ | ✔ | ✖ | ✖ | ✖ |
| OpsDir | ✖ | ✔ | ✔ | ✔ | ✔ | ✔ | ✖ | ✔ | ✖ | ✖ | ✔ | ✖ | ✔ | ✖ | ✖ |
| InvCtrl | ✔ | ✖ | ✔ | ✔ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✔ | ✖ | ✔ | ✖ | ✖ |
| WHMgr | ✖ | ✖ | ✔ | ✔ | ✔ | ✖ | ✔ | ✔ | ✔ | ✖ | ✔ | ✖ | ✖ | ✖ | ✖ |
| RcvClk | ✖ | ✖ | ✔ | ✖ | ✖ | ✖ | ✔ | ✖ | ✔ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| PikPak | ✖ | ✖ | ✔ | ✖ | ✖ | ✖ | ✖ | ✔ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| WHStf | ✖ | ✖ | ✖ | ✔ | ✖ | ✖ | ✔ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| RegMgr | ✖ | ✖ | ✔ | ✖ | ✔ | ✖ | ✖ | ✖ | ✖ | ✖ | ✔ | ✖ | ✖ | ✖ | ✖ |
| SalMgr | ✖ | ✖ | ✔ | ✖ | ✖ | ✖ | ✖ | ✔ | ✖ | ✔ | ✔ | ✖ | ✖ | ✖ | ✖ |
| SalRep | ✖ | ✖ | ✔ | ✖ | ✖ | ✖ | ✖ | ✔ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| CsRep | ✖ | ✖ | ✔ | ✖ | ✖ | ✖ | ✖ | ✔ | ✔ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| MktMgr | ✖ | ✖ | ✔ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✔ | ✔ | ✖ | ✖ | ✖ | ✖ |
| PurMgr | ✖ | ✖ | ✔ | ✖ | ✖ | ✔ | ✖ | ✖ | ✖ | ✔ | ✔ | ✖ | ✖ | ✖ | ✖ |
| Buyer | ✖ | ✖ | ✔ | ✖ | ✖ | ✔ | ✖ | ✖ | ✖ | ✖ | ✔ | ✖ | ✖ | ✖ | ✖ |
| FinMgr | ✖ | ✖ | ✔ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✔ | ✔ | ✖ | ✖ | ✔ |
| IntAud | ✖ | ✖ | ✔ | ✔ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✔ | ✔ | ✖ | ✖ | ✔ |
| ExtAud | ✖ | ✖ | ✔ | ✔ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✔ | ✔ | ✖ | ✖ | ✔ |

---

## 3. Full RBAC Matrix by Permission Group

### 3.1 PG-01: Products (PERM-001 – PERM-005, PERM-012)

| Role | 001 Create | 002 Update | 003 Status | 004 Lookup | 005 Resolve Dup | 012 ABC |
|------|:---:|:---:|:---:|:---:|:---:|:---:|
| CEO | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| COO | ✖ | ✖ | ✖ | ✔ | ✖ | ✖ |
| CFO | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| OpsDir | ✖ | ✖ | ✖ | ✔ | ✖ | ✖ |
| InvCtrl | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| WHMgr | ✖ | ✖ | ✖ | ✔ | ✖ | ✖ |
| RcvClk | ✖ | ✖ | ✖ | ✔ | ✖ | ✖ |
| PikPak | ✖ | ✖ | ✖ | ✔ | ✖ | ✖ |
| WHStf | ✖ | ✖ | ✖ | ✔ | ✖ | ✖ |
| RegMgr | ✖ | ✖ | ✖ | ✔ | ✖ | ✖ |
| SalMgr | ✖ | ✖ | ✖ | ✔ | ✖ | ✖ |
| SalRep | ✖ | ✖ | ✖ | ✔ | ✖ | ✖ |
| CsRep | ✖ | ✖ | ✖ | ✔ | ✖ | ✖ |
| MktMgr | ✖ | ✖ | ✖ | ✔ | ✖ | ✖ |
| PurMgr | ✖ | ✖ | ✖ | ✔ | ✖ | ✖ |
| Buyer | ✖ | ✖ | ✖ | ✔ | ✖ | ✖ |
| FinMgr | ✖ | ✖ | ✖ | ✔ | ✖ | ✖ |
| IntAud | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| ExtAud | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |

---

### 3.2 PG-02: Locations & Network (PERM-006 – PERM-010)

| Role | 006 Create | 007 Update | 008 Hierarchy | 009 Closure | 010 Opening Bal |
|------|:---:|:---:|:---:|:---:|:---:|
| CEO | ✖ | ✖ | ✖ | ✔ | ✖ |
| COO | ✔ | ✔ | ✔ | ✔ | ✖ |
| CFO | ✖ | ✖ | ✖ | ✖ | ✖ |
| OpsDir | ✔ | ✔ | ✔ | ✔ | ✔ |
| InvCtrl | ✖ | ✖ | ✖ | ✖ | ✔ |
| WHMgr | ✖ | ✖ | ✖ | ✖ | ✖ |
| RcvClk | ✖ | ✖ | ✖ | ✖ | ✖ |
| PikPak | ✖ | ✖ | ✖ | ✖ | ✖ |
| WHStf | ✖ | ✖ | ✖ | ✖ | ✖ |
| RegMgr | ✖ | ✖ | ✖ | ✖ | ✖ |
| SalMgr | ✖ | ✖ | ✖ | ✖ | ✖ |
| SalRep | ✖ | ✖ | ✖ | ✖ | ✖ |
| CsRep | ✖ | ✖ | ✖ | ✖ | ✖ |
| MktMgr | ✖ | ✖ | ✖ | ✖ | ✖ |
| PurMgr | ✖ | ✖ | ✖ | ✖ | ✖ |
| Buyer | ✖ | ✖ | ✖ | ✖ | ✖ |
| FinMgr | ✖ | ✖ | ✖ | ✖ | ✖ |
| IntAud | ✖ | ✖ | ✖ | ✖ | ✖ |
| ExtAud | ✖ | ✖ | ✖ | ✖ | ✖ |

---

### 3.3 PG-03: Inventory Visibility (PERM-017 – PERM-023)

| Role | 017 On-Hand | 018 ATP | 019 Reserved | 020 Status | 021 Search | 022 Network | 023 History |
|------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| CEO | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| COO | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| CFO | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| OpsDir | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| InvCtrl | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| WHMgr | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| RcvClk | ✔ | ✔ | ✖ | ✔ | ✔ | ✔ | ✖ |
| PikPak | ✔ | ✔ | ✖ | ✔ | ✔ | ✖ | ✖ |
| WHStf | ✔ | ✖ | ✖ | ✔ | ✔ | ✖ | ✖ |
| RegMgr | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✖ |
| SalMgr | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✖ |
| SalRep | ✔ | ✔ | ✖ | ✔ | ✔ | ✔ | ✖ |
| CsRep | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✖ |
| MktMgr | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✖ |
| PurMgr | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| Buyer | ✔ | ✔ | ✖ | ✔ | ✔ | ✔ | ✖ |
| FinMgr | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| IntAud | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| ExtAud | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |

---

### 3.4 PG-04: Inventory Control (PERM-011, PERM-013 – PERM-014, PERM-037 – PERM-050, PERM-070)

| Role | 011 Thresholds | 013 Policies | 014 Reasons | 037 Sched | 038 Count | 039 Full | 040 Var View | 041 Invest | 042 Appr Cnt | 043 Req Adj | 044 Appr Adj | 045 Req WO | 046 Appr WO | 047 Quar | 048 Release | 049 Shrink | 050 Obsolete | 070 Safety |
|------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| CEO | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✔ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✔ | ✔ | ✖ |
| COO | ✖ | ✔ | ✖ | ✖ | ✖ | ✖ | ✔ | ✖ | ✖ | ✖ | ✔ | ✖ | ✔ | ✖ | ✖ | ✔ | ✔ | ✔ |
| CFO | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✔ | ✖ | ✖ | ✖ | ✖ | ✖ | ✔ | ✖ | ✖ | ✔ | ✔ | ✖ |
| OpsDir | ✔ | ✔ | ✖ | ✔ | ✖ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| InvCtrl | ✔ | ✖ | ✔ | ✔ | ✖ | ✔ | ✔ | ✔ | ✔ | ✔ | ✖ | ✔ | ✖ | ✔ | ✔ | ✔ | ✔ | ✖ |
| WHMgr | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✔ | ✖ | ✔ | ✔ | ✖ | ✔ | ✖ | ✔ | ✔ | ✔ | ✖ | ✖ |
| RcvClk | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| PikPak | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| WHStf | ✖ | ✖ | ✖ | ✖ | ✔ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| RegMgr | ✖ | ✖ | ✖ | ✖ | ✔ | ✖ | ✔ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| SalMgr | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| SalRep | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| CsRep | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| MktMgr | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| PurMgr | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| Buyer | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| FinMgr | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✔ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✔ | ✔ | ✖ |
| IntAud | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✔ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✔ | ✔ | ✖ |
| ExtAud | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✔ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✔ | ✔ | ✖ |

---

### 3.5 PG-05: Stock Transfers (PERM-071 – PERM-076)

| Role | 071 Request | 072 Approve | 073 Dispatch | 074 Receive | 075 In-Transit | 076 Rebalance |
|------|:---:|:---:|:---:|:---:|:---:|:---:|
| CEO | ✖ | ✖ | ✖ | ✖ | ✔ | ✔ |
| COO | ✖ | ✔ | ✖ | ✖ | ✔ | ✔ |
| CFO | ✖ | ✖ | ✖ | ✖ | ✔ | ✖ |
| OpsDir | ✔ | ✔ | ✖ | ✖ | ✔ | ✔ |
| InvCtrl | ✖ | ✖ | ✖ | ✖ | ✔ | ✔ |
| WHMgr | ✔ | ✖ | ✔ | ✔ | ✔ | ✖ |
| RcvClk | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| PikPak | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| WHStf | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| RegMgr | ✔ | ✖ | ✖ | ✖ | ✔ | ✖ |
| SalMgr | ✖ | ✖ | ✖ | ✖ | ✔ | ✖ |
| SalRep | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| CsRep | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| MktMgr | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| PurMgr | ✖ | ✖ | ✖ | ✖ | ✔ | ✖ |
| Buyer | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| FinMgr | ✖ | ✖ | ✖ | ✖ | ✔ | ✖ |
| IntAud | ✖ | ✖ | ✖ | ✖ | ✔ | ✖ |
| ExtAud | ✖ | ✖ | ✖ | ✖ | ✔ | ✖ |

---

### 3.6 PG-06: Purchasing & Replenishment (PERM-024 – PERM-027, PERM-035 – PERM-036, PERM-064 – PERM-069)

| Role | 024 PO | 025 Amend | 026 Cancel | 027 Inbound | 035 Supply | 036 Supplier | 064 Alerts | 065 Ack | 066 Suggest | 067 Req | 068 Appr Req | 069 Appr PO |
|------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| CEO | ✖ | ✖ | ✖ | ✔ | ✔ | ✔ | ✔ | ✖ | ✔ | ✖ | ✖ | ✖ |
| COO | ✖ | ✖ | ✖ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✖ | ✖ | ✔ |
| CFO | ✖ | ✖ | ✖ | ✔ | ✔ | ✔ | ✔ | ✖ | ✔ | ✖ | ✖ | ✔ |
| OpsDir | ✖ | ✖ | ✖ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✖ | ✖ | ✖ |
| InvCtrl | ✖ | ✖ | ✖ | ✔ | ✔ | ✖ | ✔ | ✖ | ✔ | ✖ | ✖ | ✖ |
| WHMgr | ✖ | ✖ | ✖ | ✔ | ✔ | ✖ | ✔ | ✖ | ✖ | ✖ | ✖ | ✖ |
| RcvClk | ✖ | ✖ | ✖ | ✔ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| PikPak | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| WHStf | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| RegMgr | ✖ | ✖ | ✖ | ✔ | ✔ | ✖ | ✔ | ✖ | ✖ | ✖ | ✖ | ✖ |
| SalMgr | ✖ | ✖ | ✖ | ✔ | ✔ | ✖ | ✔ | ✖ | ✔ | ✖ | ✖ | ✖ |
| SalRep | ✖ | ✖ | ✖ | ✔ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| CsRep | ✖ | ✖ | ✖ | ✔ | ✔ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| MktMgr | ✖ | ✖ | ✖ | ✔ | ✔ | ✖ | ✔ | ✖ | ✔ | ✖ | ✖ | ✖ |
| PurMgr | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| Buyer | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✖ | ✖ |
| FinMgr | ✖ | ✖ | ✖ | ✔ | ✔ | ✔ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| IntAud | ✖ | ✖ | ✖ | ✔ | ✔ | ✔ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| ExtAud | ✖ | ✖ | ✖ | ✔ | ✔ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |

---

### 3.7 PG-07: Receiving & Put-Away (PERM-028 – PERM-034)

| Role | 028 Receive | 029 Doc Disc | 030 Resolve | 031 Ad-Hoc | 032 Tolerance | 033 Put-Away | 034 Return In |
|------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| CEO | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| COO | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| CFO | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| OpsDir | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| InvCtrl | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| WHMgr | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| RcvClk | ✔ | ✔ | ✖ | ✖ | ✖ | ✖ | ✔ |
| PikPak | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| WHStf | ✖ | ✖ | ✖ | ✖ | ✖ | ✔ | ✖ |
| RegMgr | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| SalMgr | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| SalRep | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| CsRep | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| MktMgr | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| PurMgr | ✖ | ✖ | ✔ | ✖ | ✖ | ✖ | ✖ |
| Buyer | ✖ | ✖ | ✔ | ✖ | ✖ | ✖ | ✖ |
| FinMgr | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| IntAud | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| ExtAud | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |

---

### 3.8 PG-08: Order Fulfillment (PERM-051 – PERM-063)

| Role | 051 Avail | 052 Reserve | 053 Release | 054 Release Ord | 055 Pick | 056 Ship | 057 Partial | 058 Backorder | 059 Rpt Exc | 060 Resolve | 061 Multi-Loc | 062 Status | 063 Subst |
|------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| CEO | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✔ | ✖ |
| COO | ✔ | ✔ | ✔ | ✔ | ✖ | ✖ | ✔ | ✔ | ✖ | ✔ | ✔ | ✔ | ✔ |
| CFO | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✔ | ✖ |
| OpsDir | ✔ | ✔ | ✔ | ✔ | ✖ | ✖ | ✔ | ✔ | ✖ | ✔ | ✔ | ✔ | ✔ |
| InvCtrl | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✔ | ✖ |
| WHMgr | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✖ | ✔ | ✔ |
| RcvClk | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| PikPak | ✖ | ✖ | ✖ | ✖ | ✔ | ✔ | ✖ | ✖ | ✔ | ✖ | ✖ | ✔ | ✖ |
| WHStf | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| RegMgr | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✔ | ✖ |
| SalMgr | ✔ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✔ | ✖ | ✖ | ✖ | ✔ | ✖ |
| SalRep | ✔ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✔ | ✖ |
| CsRep | ✔ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✔ | ✖ | ✖ | ✖ | ✔ | ✖ |
| MktMgr | ✔ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✔ | ✖ |
| PurMgr | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✔ | ✖ | ✖ | ✖ | ✔ | ✖ |
| Buyer | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| FinMgr | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✔ | ✖ |
| IntAud | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✔ | ✖ |
| ExtAud | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✔ | ✖ |

---

### 3.9 PG-09: Returns (PERM-077 – PERM-082)

| Role | 077 Authorize | 078 Receive | 079 Inspect | 080 Restock | 081 Write Off | 082 Status |
|------|:---:|:---:|:---:|:---:|:---:|:---:|
| CEO | ✖ | ✖ | ✖ | ✖ | ✖ | ✔ |
| COO | ✖ | ✖ | ✖ | ✖ | ✖ | ✔ |
| CFO | ✖ | ✖ | ✖ | ✖ | ✖ | ✔ |
| OpsDir | ✖ | ✖ | ✖ | ✖ | ✖ | ✔ |
| InvCtrl | ✖ | ✖ | ✖ | ✔ | ✔ | ✔ |
| WHMgr | ✖ | ✔ | ✔ | ✔ | ✔ | ✔ |
| RcvClk | ✖ | ✔ | ✖ | ✖ | ✖ | ✖ |
| PikPak | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| WHStf | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| RegMgr | ✖ | ✖ | ✖ | ✖ | ✖ | ✔ |
| SalMgr | ✖ | ✖ | ✖ | ✖ | ✖ | ✔ |
| SalRep | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| CsRep | ✔ | ✖ | ✖ | ✖ | ✖ | ✔ |
| MktMgr | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| PurMgr | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| Buyer | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| FinMgr | ✖ | ✖ | ✖ | ✖ | ✖ | ✔ |
| IntAud | ✖ | ✖ | ✖ | ✖ | ✖ | ✔ |
| ExtAud | ✖ | ✖ | ✖ | ✖ | ✖ | ✔ |

---

### 3.10 PG-10: Commercial & Promotions (PERM-092 – PERM-093)

| Role | 092 Readiness | 093 Ring-Fence |
|------|:---:|:---:|
| CEO | ✔ | ✖ |
| COO | ✔ | ✔ |
| CFO | ✖ | ✖ |
| OpsDir | ✔ | ✔ |
| InvCtrl | ✖ | ✖ |
| WHMgr | ✖ | ✖ |
| RcvClk | ✖ | ✖ |
| PikPak | ✖ | ✖ |
| WHStf | ✖ | ✖ |
| RegMgr | ✖ | ✖ |
| SalMgr | ✔ | ✖ |
| SalRep | ✖ | ✖ |
| CsRep | ✖ | ✖ |
| MktMgr | ✔ | ✔ |
| PurMgr | ✔ | ✖ |
| Buyer | ✖ | ✖ |
| FinMgr | ✖ | ✖ |
| IntAud | ✖ | ✖ |
| ExtAud | ✖ | ✖ |

---

### 3.11 PG-11 & PG-12: Reports, Finance (PERM-083 – PERM-091, PERM-094)

| Role | 083 Dash | 084 Move | 085 Stockout | 086 Accuracy | 087 Location | 088 KPI | 089 Replen | 090 Valuation | 091 Export | 094 Reconcile |
|------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| CEO | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✖ |
| COO | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✖ |
| CFO | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| OpsDir | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✖ | ✔ | ✖ |
| InvCtrl | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✖ | ✔ | ✖ |
| WHMgr | ✔ | ✔ | ✔ | ✔ | ✔ | ✖ | ✖ | ✖ | ✔ | ✖ |
| RcvClk | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| PikPak | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| WHStf | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| RegMgr | ✔ | ✖ | ✔ | ✖ | ✔ | ✖ | ✖ | ✖ | ✖ | ✖ |
| SalMgr | ✔ | ✖ | ✔ | ✖ | ✖ | ✔ | ✔ | ✖ | ✔ | ✖ |
| SalRep | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| CsRep | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| MktMgr | ✔ | ✖ | ✔ | ✖ | ✖ | ✖ | ✔ | ✖ | ✖ | ✖ |
| PurMgr | ✔ | ✔ | ✔ | ✖ | ✖ | ✖ | ✔ | ✖ | ✔ | ✖ |
| Buyer | ✔ | ✖ | ✖ | ✖ | ✖ | ✖ | ✔ | ✖ | ✔ | ✖ |
| FinMgr | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| IntAud | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✖ |
| ExtAud | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✖ | ✔ | ✔ | ✖ |

---

### 3.12 PG-13, PG-14, PG-15: Setup, Administration, Audit (PERM-015 – PERM-016, PERM-095 – PERM-100)

| Role | 015 Import | 016 Appr Import | 095 Users | 096 Roles | 097 Activity | 098 Audit Trail | 099 Query | 100 Breaches |
|------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| CEO | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| COO | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| CFO | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| OpsDir | ✔ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| InvCtrl | ✔ | ✔ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| WHMgr | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| RcvClk | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| PikPak | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| WHStf | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| RegMgr | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| SalMgr | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| SalRep | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| CsRep | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| MktMgr | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| PurMgr | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| Buyer | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ | ✖ |
| FinMgr | ✖ | ✖ | ✖ | ✖ | ✖ | ✔ | ✔ | ✔ |
| IntAud | ✖ | ✖ | ✖ | ✖ | ✔ | ✔ | ✔ | ✔ |
| ExtAud | ✖ | ✖ | ✖ | ✖ | ✖ | ✔ | ✔ | ✖ |

---

## 4. Role Permission Count Summary

| Role | Allowed | Not Allowed | Coverage |
|------|---------|-------------|----------|
| CEO | 28 | 72 | Executive visibility and reporting |
| COO | 52 | 48 | Operational oversight and high-value approvals |
| CFO | 30 | 70 | Financial visibility, valuation, write-off approval |
| OpsDir | 62 | 38 | Network operations management |
| InvCtrl | 38 | 62 | Master data, count programs, variance control |
| WHMgr | 42 | 58 | Location warehouse operations |
| RcvClk | 11 | 89 | Inbound receipt execution |
| PikPak | 9 | 91 | Pick, pack, ship execution |
| WHStf | 5 | 95 | Put-away and counting execution |
| RegMgr | 14 | 86 | Store visibility and transfer requests |
| SalMgr | 22 | 78 | Commercial visibility and availability |
| SalRep | 8 | 92 | Customer-facing availability inquiry |
| CsRep | 14 | 86 | Order status and return intake |
| MktMgr | 14 | 86 | Campaign readiness monitoring |
| PurMgr | 32 | 68 | Full procurement and replenishment |
| Buyer | 20 | 80 | Purchase execution without approval |
| FinMgr | 28 | 72 | Financial reporting and reconciliation |
| IntAud | 24 | 76 | Read-only audit and compliance |
| ExtAud | 20 | 80 | Temporary audit read access |

---

## 5. Location Scoping Rules

Permissions marked ✔ are subject to location scope based on role assignment:

| Scope | Roles | Effect |
|-------|-------|--------|
| **Network-wide** | CEO, COO, CFO, OpsDir, InvCtrl, PurMgr, FinMgr, IntAud, ExtAud, SalMgr, MktMgr | Visibility and reports across all authorized locations |
| **Assigned location(s)** | WHMgr, RcvClk, PikPak, WHStf, RegMgr | Transactional permissions limited to assigned warehouse or store |
| **No location constraint** | SalRep, CsRep, Buyer | Visibility scoped to business need (customer orders, PO lines) not physical location |

---

## 6. Segregation of Duties Validation

| SoD Rule | Role A (Initiate) | Role B (Approve) | Enforced |
|----------|-------------------|------------------|----------|
| Count and approve count | WHStf, RegMgr (PERM-038) | InvCtrl, WHMgr (PERM-042) | ✔ Different roles |
| Request and approve adjustment | WHMgr, InvCtrl, OpsDir (PERM-043) | OpsDir, COO (PERM-044) | ✔ InvCtrl cannot approve (PERM-044 ✖) |
| Request and approve write-off | WHMgr, OpsDir (PERM-045) | OpsDir, COO, CFO (PERM-046) | ✔ WHMgr cannot approve (PERM-046 ✖) |
| Create and approve requisition | Buyer (PERM-067) | PurMgr (PERM-068) | ✔ Different roles |
| Create and approve PO | Buyer (PERM-024) | PurMgr, COO, CFO (PERM-069) | ✔ Buyer cannot approve (PERM-069 ✖) |
| Request and approve transfer | WHMgr, RegMgr, OpsDir (PERM-071) | OpsDir, COO (PERM-072) | ✔ Requesters cannot approve own transfer |
| Receive and approve tolerance | RcvClk (PERM-028) | WHMgr (PERM-032) | ✔ Different roles |
| Import and approve import | OpsDir (PERM-015) | InvCtrl (PERM-016) | ✔ Different roles |

---

## 7. Sensitive Permission Justifications

The following table documents business justification for every permission classified as **sensitive** — those that approve financial impact, override controls, manage governance, or administer system access.

### 7.1 Approval Permissions

| Permission | Role(s) Allowed | Business Justification |
|------------|-----------------|------------------------|
| **PERM-042** Approve Count Adjustment | OpsDir, InvCtrl, WHMgr | Count adjustments directly change inventory balances. InvCtrl approves as independent control owner; WHMgr approves immaterial local variances within policy; OpsDir approves material network variances. WHStf and RcvClk are denied to enforce counter/approver segregation. |
| **PERM-044** Approve Stock Adjustment | OpsDir, COO | Stock adjustments can materially affect financial records. Operations Director approves within threshold; COO approves high-value adjustments. InvCtrl may request (PERM-043) but cannot approve own requests. WHMgr denied to prevent location managers from unilaterally correcting records. |
| **PERM-046** Approve Inventory Write-Off | OpsDir, COO, CFO | Write-offs permanently remove asset value from the balance sheet. Three-role approval chain ensures operational justification (OpsDir), executive oversight (COO), and financial governance (CFO). No frontline or control roles may approve to prevent fraudulent disposal. |
| **PERM-068** Approve Purchase Requisition | PurMgr | Requisitions commit the organization to future spend. Only Purchasing Manager may approve, segregated from Buyer who creates requisitions (PERM-067). |
| **PERM-069** Approve Purchase Order | PurMgr, COO, CFO | Purchase orders create binding supplier commitments. PurMgr approves within authority; COO approves operationally significant orders; CFO approves financially material commitments. Buyer denied to prevent self-approval of own orders. |
| **PERM-072** Approve Stock Transfer | OpsDir, COO | Transfers redistribute network assets and can create new stockouts at source locations. OpsDir approves routine transfers; COO approves transfers with significant network impact. Requesters (WHMgr, RegMgr) cannot approve. |
| **PERM-016** Approve Initial Data Import | InvCtrl | Go-live data imports embed baseline inventory values affecting all future transactions. Inventory Controller approves as data quality owner; segregated from OpsDir who submits (PERM-015). |

### 7.2 Control Override Permissions

| Permission | Role(s) Allowed | Business Justification |
|------------|-----------------|------------------------|
| **PERM-031** Approve Ad-Hoc Receipt | WHMgr | Receipts without PO reference bypass procurement controls. Only Warehouse Manager may authorize at location level where physical verification occurs; receiving clerks cannot self-authorize. |
| **PERM-032** Approve Receipt Beyond Tolerance | WHMgr | Accepting quantities outside PO tolerance affects payment and inventory accuracy. Warehouse Manager verifies physical goods before approving; segregated from Receiving Clerk who records receipt. |
| **PERM-070** Override Safety Stock Protection | OpsDir, COO | Consuming safety stock exposes the network to stockout risk. Restricted to operations leadership who can document replenishment plans; frontline and purchasing roles denied to prevent routine buffer erosion. |
| **PERM-063** Approve Product Substitution | WHMgr, OpsDir, COO | Substitutions ship different products than ordered, creating commercial and compliance risk. Warehouse Manager approves routine substitutes; OpsDir/COO for high-value or regulated products. |

### 7.3 Governance and Policy Permissions

| Permission | Role(s) Allowed | Business Justification |
|------------|-----------------|------------------------|
| **PERM-013** Manage Inventory Governance Policies | OpsDir, COO | Policy parameters (approval thresholds, count tolerances) govern all inventory decisions. Restricted to operations leadership to prevent policy drift by operational or frontline roles. |
| **PERM-011** Define Stock Thresholds | InvCtrl, OpsDir | Thresholds drive replenishment and alerts across the network. Inventory Controller owns data-driven threshold definition; OpsDir may adjust for network strategy. Purchasing and sales roles denied to prevent threshold manipulation for convenience. |
| **PERM-014** Manage Reason Codes | InvCtrl | Reason codes substantiate every adjustment and write-off for audit. Centralized control by Inventory Controller ensures consistent categorization for shrinkage analysis. |
| **PERM-009** Plan Location Closure and Disposition | CEO, COO, OpsDir | Location closure affects network capacity and asset disposition. CEO approves strategic closures; COO and OpsDir execute disposition planning. |
| **PERM-093** Ring-Fence Promotional Stock | COO, OpsDir, MktMgr | Ring-fencing removes stock from general ATP, affecting all sales channels. Marketing Manager requests; COO/OpsDir authorize to balance campaign needs against general availability. |

### 7.4 Financial Permissions

| Permission | Role(s) Allowed | Business Justification |
|------------|-----------------|------------------------|
| **PERM-090** View Inventory Valuation Reports | CEO, COO, CFO, FinMgr, IntAud, ExtAud | Valuation data reveals unit costs and margin structure. Restricted to finance and executive roles plus auditors; operational and commercial roles denied to protect sensitive cost information. |
| **PERM-094** Perform Financial Inventory Reconciliation | CFO, FinMgr | Reconciliation directly affects balance sheet reporting. Restricted to finance function under CFO accountability; operations roles denied to preserve finance independence. |

### 7.5 Administration and Audit Permissions

| Permission | Role(s) Allowed | Business Justification |
|------------|-----------------|------------------------|
| **PERM-095** Manage User Accounts | None (business roles) | Account lifecycle management is a technical administration function outside business role scope. Reserved for System Administrator role. |
| **PERM-096** Assign User Roles and Location Scope | None (business roles) | Role assignment determines access boundaries for all users. Reserved for System Administrator to prevent privilege escalation by business roles. |
| **PERM-097** View User Activity Log | IntAud, FinMgr | Activity logs reveal user behavior patterns for fraud investigation. Internal Auditor for control testing; Finance Manager for reconciliation support. Operational roles denied. |
| **PERM-098** View Inventory Audit Trail | FinMgr, IntAud, ExtAud | Immutable audit trail is primary fraud and error investigation evidence. Finance and audit roles only; no operational role may access to prevent tampering awareness exploitation. |
| **PERM-099** Query Audit Evidence | FinMgr, IntAud, ExtAud | Structured audit queries support formal assurance activities. Restricted to audit and finance oversight functions during defined review periods. |
| **PERM-100** View Control Policy Breach Records | FinMgr, IntAud | Breach records reveal control weaknesses. Finance and internal audit review for remediation; denied to operational roles to encourage reporting without fear of retaliation manipulation. |

### 7.6 Master Data Permissions

| Permission | Role(s) Allowed | Business Justification |
|------------|-----------------|------------------------|
| **PERM-001–003, 005** Create/Update/Status/Resolve Product | InvCtrl | Product master data integrity affects every inventory transaction. Centralized ownership by Inventory Controller prevents duplicate identities and unauthorized product changes by operational roles. |
| **PERM-006–008** Create/Update/Hierarchy Location | COO, OpsDir | Location network structure determines accountability and reporting. Restricted to operations leadership; warehouse managers cannot create parallel location records. |
| **PERM-015** Import Initial Master Data | OpsDir, InvCtrl | Bulk import can load thousands of records instantly. OpsDir prepares cutover; InvCtrl validates. Segregated from PERM-016 approval. |

---

## 8. Document Summary

This RBAC matrix maps **19 business roles** to **100 system permissions** with explicit ✔/✖ assignments organized across **15 permission groups**. Assignments reflect role responsibilities, organizational hierarchy, least-privilege principles, and segregation-of-duties requirements.

Sensitive permissions — approvals, control overrides, governance, financial data, and audit access — are documented with business justification in Section 7. Location scoping (Section 5) applies as a cross-cutting constraint on all transactional permissions.

System Administrator permissions (PERM-095, PERM-096) are intentionally unassigned to business roles and require a separate technical administration profile.

---

*End of RBAC Matrix Document*
