# Business Process Maps: Inventory Management System

**Document Owner:** Business Process Consultant  
**Purpose:** Visualize the end-to-end flow of every major inventory management process using simple text-based diagrams  
**Scope:** Business activities and actors only — no software, database, or technical implementation detail  
**Based On:** Business Process Analysis, Business Workflows, and Business Actor Analysis

---

## How to Read These Diagrams

- **↓** indicates sequential flow to the next step  
- **├── Yes / No** indicates a decision branch  
- **[Actor]** identifies the responsible business actor for each activity  
- All **32 major business processes** are mapped below, grouped by domain

---

## Domain 1: Master Data & Governance

---

### BP-01: Product Master Data Management

| Attribute | Description |
|-----------|-------------|
| **Process Name** | Product Master Data Management |
| **Start Event** | New product introduction, attribute change, discontinuation, or data quality issue identified |
| **End Event** | Product record finalized, approved, and communicated to all affected departments |

```
Start
 ↓
Submit Product Data Request [Sales / Purchasing / Marketing / Operations]
 ↓
Review Request for Completeness [Inventory Controller]
 ↓
Request Complete?
 ├── No → Return to Requester for Clarification [Inventory Controller]
 │         ↓
 │        (Return to Review Request)
 └── Yes ↓
Check for Duplicate or Conflicting SKU [Inventory Controller]
 ↓
Duplicate Found?
 ├── Yes → Merge or Correct Existing Record [Inventory Controller]
 └── No → Assign or Validate SKU, Unit of Measure, Category [Inventory Controller]
 ↓
Circulate Product Definition for Approval [Inventory Controller]
 ↓
Purchasing and Operations Approve?
 ├── No → Revise and Resubmit [Inventory Controller]
 │         ↓
 │        (Return to Circulate Product Definition)
 └── Yes ↓
Finance Provides Costing Reference (if applicable) [Finance Manager]
 ↓
Marketing / Sales Confirm Launch Readiness (if new product) [Marketing Manager / Sales Manager]
 ↓
Set Product Status [Inventory Controller]
 ↓
Status?
 ├── Active → Publish Active Product Record
 ├── Inactive → Publish Inactive Product Record
 └── Discontinued → Flag Remaining Stock for Clearance [Inventory Controller]
 ↓
Communicate Updated Product Information to Locations [Inventory Controller]
 ↓
End
```

**Decision Points:** Request complete? | Duplicate found? | Purchasing and operations approve? | Product status?

---

### BP-02: Location & Warehouse Setup

| Attribute | Description |
|-----------|-------------|
| **Process Name** | Location & Warehouse Setup |
| **Start Event** | Leadership approves opening, closing, consolidating, or reorganizing an inventory location |
| **End Event** | Location authorized, documented in network hierarchy, and accountable manager assigned |

```
Start
 ↓
Submit Location Change Request [Operations Director]
 ↓
Define Location Details (Name, Address, Type, Scope) [Operations Director]
 ↓
Strategically Approved? [COO]
 ├── No → Defer or Reject Request [COO]
 │         ↓
 │        End (Rejected)
 └── Yes ↓
Change Type?
 ├── New Location → Assign Warehouse Manager or Regional Manager [Operations Director]
 │                  ↓
 │                 Document Location in Network Hierarchy [Operations Director]
 │                  ↓
 │                 Prepare Physical Location for Operations [Warehouse Manager]
 ├── Closure → Plan Remaining Stock Disposition [Operations Director]
 │              ↓
 │             Stock Disposition?
 │              ├── Transfer Out → Initiate Inter-Location Transfers [Warehouse Manager]
 │              ├── Write Off → Initiate Write-Off Process [Inventory Controller]
 │              └── Sell Through → Continue Sales Until Depleted [Regional Manager]
 │              ↓
 │             Mark Location Inactive [Operations Director]
 └── Reorganization → Update Hierarchy and Reassign Accountability [Operations Director]
 ↓
Notify Finance of Location Change [Operations Director]
 ↓
Communicate Location Change to All Departments [Operations Director]
 ↓
End
```

**Decision Points:** Strategically approved? | Change type (new / closure / reorganization)? | Stock disposition method?

---

### BP-03: Stock Policy & Threshold Definition

| Attribute | Description |
|-----------|-------------|
| **Process Name** | Stock Policy & Threshold Definition |
| **Start Event** | New product onboarding, demand shift, lead time change, or stockout/overstock review |
| **End Event** | Reorder levels and thresholds defined, approved, and published |

```
Start
 ↓
Identify Products Requiring Policy Review [Inventory Controller]
 ↓
Gather Consumption History and Lead Times [Inventory Controller]
 ↓
Collect Demand Forecast Input [Sales Manager]
 ↓
Confirm Supplier Lead Times [Purchasing Manager]
 ↓
Review Carrying Cost Implications [Finance Manager]
 ↓
Calculate Proposed Reorder Levels and Thresholds [Inventory Controller]
 ↓
Thresholds Aligned with Lead Time and Demand? [Operations Director]
 ├── No → Adjust and Recalculate [Inventory Controller]
 │         ↓
 │        (Return to Calculate Proposed Levels)
 └── Yes ↓
Priority Alert Treatment Required?
 ├── Yes → Flag as Priority SKU [Inventory Controller]
 └── No → Apply Standard Alert Rules [Inventory Controller]
 ↓
Approve Stock Policy Parameters [Operations Director]
 ↓
Publish Updated Policies to Purchasing and Warehouse Teams [Inventory Controller]
 ↓
End
```

**Decision Points:** Thresholds aligned? | Priority alert treatment?

---

### BP-04: ABC Product Classification

| Attribute | Description |
|-----------|-------------|
| **Process Name** | ABC Product Classification |
| **Start Event** | Semi-annual review date, sales mix shift, or leadership prioritization request |
| **End Event** | ABC classification published; count schedules and alert priorities updated |

```
Start
 ↓
Initiate Classification Review Cycle [Inventory Controller]
 ↓
Compile Sales Volume, Revenue, and Velocity Data [Inventory Controller]
 ↓
Draft Preliminary A, B, C Assignments [Inventory Controller]
 ↓
Hold Cross-Functional Review Workshop [Inventory Controller]
 ↓
Participants: Operations, Purchasing, Sales, Finance
 ↓
Classification Agreed? [Operations Director]
 ├── No → Override with Business Justification [Operations Director]
 │         ↓
 │        Revise Classification [Inventory Controller]
 └── Yes ↓
Approve Final Classification [Operations Director]
 ↓
Publish Priority Product List [Inventory Controller]
 ↓
Update Count Schedules and Alert Priorities [Inventory Controller]
 ↓
End
```

**Decision Points:** Classification agreed?

---

## Domain 2: Inbound & Receiving

---

### BP-05: Purchase Order Placement

| Attribute | Description |
|-----------|-------------|
| **Process Name** | Purchase Order Placement |
| **Start Event** | Approved replenishment requisition, validated low-stock alert, emergency stockout, or promotional stock build |
| **End Event** | Purchase order issued to supplier and inbound commitment recorded |

```
Start
 ↓
Receive Approved Requisition or Replenishment Need [Buyer]
 ↓
Verify Current Stock and Open Orders [Buyer]
 ↓
Sufficient Stock or Open Order Exists?
 ├── Yes → Cancel or Reduce Requisition [Buyer]
 │         ↓
 │        End (No PO Required)
 └── No ↓
Confirm Supplier, Quantity, and Delivery Date [Buyer]
 ↓
Order Value Within Buyer Authority? [Buyer]
 ├── No → Escalate for Approval [Purchasing Manager / Finance Manager]
 │         ↓
 │        Approved?
 │         ├── No → End (Rejected)
 │         └── Yes ↓
 └── Yes ↓
Confirm Receiving Capacity with Warehouse [Warehouse Manager]
 ↓
Receiving Date Acceptable?
 ├── No → Negotiate Alternate Date with Supplier [Buyer]
 └── Yes ↓
Issue Purchase Order to Supplier [Buyer]
 ↓
Record Open Order and Communicate Inbound Expectation [Buyer]
 ↓
End
```

**Decision Points:** Sufficient stock or open order? | Within buyer authority? | Receiving date acceptable?

---

### BP-06: Inbound Shipment Planning

| Attribute | Description |
|-----------|-------------|
| **Process Name** | Inbound Shipment Planning |
| **Start Event** | Supplier confirms order, advance shipment notice received, or delivery date approaching |
| **End Event** | Receiving location prepared; stakeholders informed of expected inbound stock |

```
Start
 ↓
Receive Supplier Confirmation or Shipment Notice [Buyer]
 ↓
Update Expected Delivery Date and Contents [Buyer]
 ↓
Communicate Inbound Details to Warehouse Manager [Buyer]
 ↓
Assess Dock Capacity, Staffing, and Storage [Warehouse Manager]
 ↓
Receiving Location Has Capacity?
 ├── No → Request Delivery Reschedule [Buyer]
 │         ↓
 │        Supplier Agrees to New Date?
 │         ├── No → Escalate to Purchasing Manager [Buyer]
 │         └── Yes ↓
 └── Yes ↓
Schedule Receiving Resources [Warehouse Manager]
 ↓
Shipment Content Aligned with PO?
 ├── No → Flag Discrepancy for Receiving [Buyer]
 └── Yes ↓
Notify Operations and Sales (if priority SKU) [Buyer]
 ↓
Coordinate Freight Forwarder ETA (if applicable) [Buyer / Freight Forwarder]
 ↓
End
```

**Decision Points:** Receiving capacity available? | Shipment aligned with PO?

---

### BP-07: Goods Receipt & Verification

| Attribute | Description |
|-----------|-------------|
| **Process Name** | Goods Receipt & Verification |
| **Start Event** | Supplier shipment physically arrives at receiving dock |
| **End Event** | Received goods verified, recorded, and on-hand inventory updated |

```
Start
 ↓
Accept Delivery and Obtain Documentation [Receiving Clerk]
 ↓
Identify Shipment Against Purchase Order [Receiving Clerk]
 ↓
Matching PO Found?
 ├── No → Hold Shipment for Purchasing Investigation [Receiving Clerk]
 │         ↓
 │        End (Held — Pending PO Match)
 └── Yes ↓
Inspect Packaging Condition [Receiving Clerk]
 ↓
Count Received Quantities [Receiving Clerk]
 ↓
Verify Product Identity Against Packing List [Receiving Clerk]
 ↓
Quantities Match PO and Condition Acceptable? [Receiving Clerk]
 ├── Yes → Record Goods Receipt [Receiving Clerk]
 │         ↓
 │        Update On-Hand Inventory [Receiving Clerk]
 │         ↓
 │        Notify Warehouse Manager of Completion [Receiving Clerk]
 │         ↓
 │        End (Clean Receipt)
 └── No ↓
Discrepancy Type?
 ├── Short Shipment → Initiate Receipt Discrepancy Resolution [Warehouse Manager]
 ├── Damage → Initiate Receipt Discrepancy Resolution [Warehouse Manager]
 ├── Wrong Item → Initiate Receipt Discrepancy Resolution [Warehouse Manager]
 └── Over-Shipment → Initiate Receipt Discrepancy Resolution [Warehouse Manager]
 ↓
Receive Acceptable Portion (if applicable) [Receiving Clerk]
 ↓
End (With Discrepancy Flagged)
```

**Decision Points:** Matching PO found? | Quantities and condition acceptable? | Discrepancy type?

---

### BP-08: Receipt Discrepancy Resolution

| Attribute | Description |
|-----------|-------------|
| **Process Name** | Receipt Discrepancy Resolution |
| **Start Event** | Receiving clerk identifies quantity mismatch, damage, or wrong items during verification |
| **End Event** | Discrepancy resolved, inventory corrected, and supplier accountability documented |

```
Start
 ↓
Document Discrepancy with Evidence [Receiving Clerk]
 ↓
Review Discrepancy Report [Warehouse Manager]
 ↓
Determine Discrepancy Type [Warehouse Manager]
 ↓
Type?
 ├── Short Shipment
 ├── Over-Shipment
 ├── Damage
 └── Wrong Item
 ↓
Accept Partial Receipt Now?
 ├── Yes → Record Accepted Quantities [Receiving Clerk]
 └── No → Hold Entire Shipment [Warehouse Manager]
 ↓
Report Discrepancy to Supplier [Buyer]
 ↓
Supplier Accepts Claim? [Supplier / Buyer]
 ├── Yes → Resolution?
 │         ├── Credit → Process Supplier Credit [Finance Manager]
 │         ├── Replacement → Arrange Replacement Shipment [Buyer]
 │         └── Accept with Adjustment → Correct Receipt Record [Receiving Clerk]
 └── No → Escalate Dispute [Purchasing Manager]
           ↓
          Negotiate Resolution [Purchasing Manager]
 ↓
Record Corrected Receipt Quantities [Receiving Clerk]
 ↓
Close Discrepancy Case with Documentation [Warehouse Manager]
 ↓
End
```

**Decision Points:** Discrepancy type? | Accept partial receipt? | Supplier accepts claim? | Resolution type?

---

### BP-09: Stock Put-Away & Storage

| Attribute | Description |
|-----------|-------------|
| **Process Name** | Stock Put-Away & Storage |
| **Start Event** | Goods receipt verification completed; verified stock awaits storage placement |
| **End Event** | Goods stored in assigned location and confirmed available for operations |

```
Start
 ↓
Assign Put-Away Tasks [Warehouse Manager]
 ↓
Retrieve Goods from Receiving Area [Warehouse Staff]
 ↓
Designated Storage Location Available? [Warehouse Staff]
 ├── No → Assign Alternate Location [Warehouse Manager]
 └── Yes ↓
Product Requires Special Handling?
 ├── Yes → Move to Designated Special Area [Warehouse Staff]
 └── No → Move to Standard Storage Location [Warehouse Staff]
 ↓
Confirm Placement and Organize Stock [Warehouse Staff]
 ↓
Verify Put-Away Completion [Warehouse Manager]
 ↓
Put-Away Completed Same Business Day?
 ├── Yes → Confirm Stock Available for Picking [Warehouse Manager]
 └── No → Queue for Next Shift [Warehouse Manager]
 ↓
End
```

**Decision Points:** Storage location available? | Special handling required? | Same-day completion?

---

## Domain 3: Inventory Control

---

### BP-10: Inventory Status Monitoring

| Attribute | Description |
|-----------|-------------|
| **Process Name** | Inventory Status Monitoring |
| **Start Event** | Business day begins, inventory movement occurs, or threshold breach detected |
| **End Event** | Current inventory status visible; exceptions identified and routed |

```
Start
 ↓
Review Stock Balances Across All Locations [Operations Director / Inventory Controller]
 ↓
Identify Reserved and Committed Quantities [Inventory Controller]
 ↓
Calculate Available-to-Promise per Product and Location [Inventory Controller]
 ↓
Classify Stock Status [Inventory Controller]
 ↓
Status?
 ├── In Stock → Continue Monitoring
 ├── Low Stock → Generate Low-Stock Alert [Inventory Controller]
 │               ↓
 │              Route Alert to Purchasing [Inventory Controller]
 │               ↓
 │              Initiate Low-Stock Alert Review
 ├── Out of Stock → Escalate Urgently [Inventory Controller]
 │                  ↓
 │                 Notify Purchasing and Operations [Inventory Controller]
 └── Overstock → Flag for Network Rebalancing [Inventory Controller]
 ↓
Distribute Status Summary to Stakeholders [Operations Director]
 ↓
Management Review Required?
 ├── Yes → Present Network Health Summary [Operations Director]
 └── No ↓
End
```

**Decision Points:** Stock status classification? | Management review required?

---

### BP-11: Cycle Counting

| Attribute | Description |
|-----------|-------------|
| **Process Name** | Cycle Counting |
| **Start Event** | Scheduled count assignment per count calendar or SKU flagged for verification |
| **End Event** | Assigned products counted, results recorded, variances flagged |

```
Start
 ↓
Issue Count Assignments per Schedule [Inventory Controller]
 ↓
Assign Counters and Provide Instructions [Warehouse Manager]
 ↓
Counters Physically Count Assigned Products [Warehouse Staff]
 ↓
Record Physical Quantities Found [Warehouse Staff]
 ↓
Submit Count Results [Warehouse Staff]
 ↓
Recount Required? [Warehouse Manager]
 ├── Yes → Repeat Physical Count [Warehouse Staff]
 └── No ↓
Compare Physical Count to Recorded Balance [Warehouse Manager]
 ↓
Variance Within Tolerance?
 ├── Yes → Close Count — Note Variance [Warehouse Manager]
 └── No → Flag for Variance Investigation [Warehouse Manager]
           ↓
          Initiate Count Variance Investigation
 ↓
Confirm Count Completion [Inventory Controller]
 ↓
End
```

**Decision Points:** Recount required? | Variance within tolerance?

---

### BP-12: Full Physical Inventory Count

| Attribute | Description |
|-----------|-------------|
| **Process Name** | Full Physical Inventory Count |
| **Start Event** | Annual or semi-annual count calendar, audit requirement, or baseline establishment |
| **End Event** | All location inventory counted, variances documented, baseline established |

```
Start
 ↓
Plan Count: Date, Teams, Methodology [Inventory Controller]
 ↓
Approve Count Plan [Operations Director]
 ↓
Notify Finance and Internal Auditor [Inventory Controller]
 ↓
Prepare Location: Organize Stock, Brief Teams [Warehouse Manager]
 ↓
Location Ready for Count?
 ├── No → Reschedule Count [Operations Director]
 └── Yes ↓
Count All Products Across All Storage Areas [Warehouse Staff]
 ↓
Verify Count Sheets for Completeness [Warehouse Manager]
 ↓
All Areas and SKUs Counted?
 ├── No → Identify Gaps and Recount [Warehouse Manager]
 └── Yes ↓
Compile Total Count Results [Inventory Controller]
 ↓
Compare to Recorded Inventory [Inventory Controller]
 ↓
Total Location Variance Within Acceptable Range? [Operations Director]
 ├── Yes → Confirm Baseline [Operations Director]
 └── No → Initiate Variance Investigation for Significant Items [Inventory Controller]
 ↓
Finance Reviews Results [Finance Manager]
 ↓
End
```

**Decision Points:** Location ready? | All areas counted? | Variance within acceptable range?

---

### BP-13: Count Variance Investigation & Approval

| Attribute | Description |
|-----------|-------------|
| **Process Name** | Count Variance Investigation & Approval |
| **Start Event** | Cycle or full count identifies variance exceeding defined tolerance |
| **End Event** | Variance investigated, root cause documented, adjustment approved or rejected |

```
Start
 ↓
Receive Variance Report [Warehouse Manager / Inventory Controller]
 ↓
Review Transaction History for Affected SKU [Inventory Controller]
 ↓
Interview Warehouse Staff on Recent Activity [Inventory Controller]
 ↓
Uncertainty Remains?
 ├── Yes → Order Physical Recount [Warehouse Manager]
 │         ↓
 │        Recount Consistent with Original?
 │         ├── No → Dispute Original — Recount Again [Warehouse Manager]
 │         └── Yes ↓
 └── No ↓
Determine Probable Root Cause [Inventory Controller]
 ↓
Root Cause Identifiable?
 ├── Yes → Document Root Cause [Inventory Controller]
 └── No → Escalate for Loss Prevention Review [Inventory Controller]
 ↓
Prepare Adjustment Recommendation with Reason Code [Inventory Controller]
 ↓
Adjustment Within Approver Authority? [Warehouse Manager]
 ├── Yes → Approve or Reject Adjustment [Warehouse Manager]
 └── No → Escalate to Operations Director [Operations Director]
           ↓
          Approve or Reject Adjustment [Operations Director]
 ↓
Approved?
 ├── Yes → Execute Stock Adjustment
 └── No → Continue Investigation [Inventory Controller]
 ↓
End
```

**Decision Points:** Recount needed? | Root cause identifiable? | Within approver authority? | Approved?

---

### BP-14: Stock Adjustment & Write-Off

| Attribute | Description |
|-----------|-------------|
| **Process Name** | Stock Adjustment & Write-Off |
| **Start Event** | Approved count variance, damage, obsolescence, theft, loss, or data correction |
| **End Event** | Inventory balance updated with full documentation and financial treatment |

```
Start
 ↓
Prepare Adjustment Request with Reason Code [Warehouse Manager / Inventory Controller]
 ↓
Attach Supporting Evidence [Initiator]
 ↓
Reason Code Valid and Evidence Sufficient? [Approver]
 ├── No → Return for More Documentation [Approver]
 │         ↓
 │        (Return to Prepare Request)
 └── Yes ↓
Adjustment Value Within Approver Authority? [Approver]
 ├── No → Escalate to Operations Director or COO [Operations Director / COO]
 └── Yes ↓
Segregation of Duties Satisfied? [Approver]
 ├── No → Reassign to Independent Approver [Operations Director]
 └── Yes ↓
Approve or Reject Adjustment [Approver]
 ↓
Approved?
 ├── No → Return to Initiator for Further Investigation
 └── Yes ↓
Write-Off Requiring Financial Treatment?
 ├── Yes → Notify Finance [Finance Manager]
 │         ↓
 │        Record Financial Impact [Finance Manager]
 └── No ↓
Apply Adjustment to Inventory Balance [Inventory Controller]
 ↓
Document Initiator, Approver, Reason, and Date [Inventory Controller]
 ↓
End
```

**Decision Points:** Evidence sufficient? | Within authority? | Segregation satisfied? | Approved? | Write-off?

---

### BP-15: Shrinkage & Loss Management

| Attribute | Description |
|-----------|-------------|
| **Process Name** | Shrinkage & Loss Management |
| **Start Event** | Monthly review cycle, recurring variance patterns, audit finding, or significant adjustment |
| **End Event** | Shrinkage analyzed, corrective actions assigned, follow-up scheduled |

```
Start
 ↓
Compile Adjustment, Write-Off, and Variance Data [Inventory Controller]
 ↓
Analyze Trends by Location, Category, and Reason Code [Inventory Controller]
 ↓
Identify Abnormal Shrinkage Rates [Inventory Controller]
 ↓
Shrinkage Within Acceptable Threshold? [Inventory Controller]
 ├── Yes → Document and Monitor [Inventory Controller]
 │         ↓
 │        End (No Action Required)
 └── No ↓
Investigate Root Causes [Inventory Controller / Operations Director]
 ↓
Root Cause Type?
 ├── Process Failure → Develop Process Improvement Plan [Operations Director]
 ├── Training Gap → Schedule Training [Warehouse Manager]
 ├── Theft Risk → Escalate to Leadership and Internal Auditor [Operations Director]
 └── Supplier Quality → Address with Purchasing [Purchasing Manager]
 ↓
Assign Corrective Actions and Timelines [Operations Director]
 ↓
Inform Internal Auditor of Significant Concerns [Internal Auditor]
 ↓
Review Progress in Next Cycle [Inventory Controller]
 ↓
End
```

**Decision Points:** Shrinkage within threshold? | Root cause type?

---

## Domain 4: Order Fulfillment

---

### BP-16: Order Availability Confirmation

| Attribute | Description |
|-----------|-------------|
| **Process Name** | Order Availability Confirmation |
| **Start Event** | Customer order, quote request, or large/strategic order review |
| **End Event** | Customer receives confirmed availability or clear shortfall explanation |

```
Start
 ↓
Receive Customer Order or Quote Request [Sales Representative / Customer Service]
 ↓
Identify Required Products, Quantities, and Delivery Date [Sales Representative]
 ↓
Check Available-to-Promise Across Locations [Sales Representative]
 ↓
Sufficient Stock at Single Location?
 ├── Yes → Confirm Fulfillment Location [Sales Representative]
 └── No → Check Alternate Locations [Sales Representative]
           ↓
          Stock Available at Any Location?
           ├── Yes → Plan Single or Split Fulfillment [Operations Director]
           └── No → Check Inbound Expected Stock [Sales Representative]
                     ↓
                    Inbound Arrives in Time?
                     ├── Yes → Commit with Future Date [Sales Representative]
                     └── No → Identify Shortfall [Sales Representative]
 ↓
Large or Strategic Order?
 ├── Yes → Consult Sales Manager or Operations [Sales Manager / Operations Director]
 └── No ↓
Communicate Availability and Delivery Date to Customer [Sales Representative]
 ↓
Full Availability Confirmed?
 ├── Yes → Proceed to Order Reservation
 └── No → Offer Alternatives [Sales Representative]
           ↓
          Alternatives?
           ├── Partial Delivery → Initiate Partial Fulfillment Process
           ├── Backorder → Initiate Backorder Process
           ├── Substitute → Confirm Substitute with Customer [Sales Representative]
           └── Cancel → Close Order Line [Customer Service]
 ↓
End
```

**Decision Points:** Sufficient stock? | Inbound in time? | Large order? | Full availability? | Alternative accepted?

---

### BP-17: Inventory Reservation

| Attribute | Description |
|-----------|-------------|
| **Process Name** | Inventory Reservation |
| **Start Event** | Customer order confirmed for fulfillment, or stock arrives for backordered line |
| **End Event** | Stock committed to order, ATP reduced, order queued for picking |

```
Start
 ↓
Receive Confirmed Order for Fulfillment [Operations Director / Warehouse Manager]
 ↓
Select Optimal Fulfillment Location [Warehouse Manager]
 ↓
Full Quantity Available for Reservation? [Warehouse Manager]
 ├── Yes → Reserve Full Quantity [Warehouse Manager]
 └── No → Reserve Partial Quantity [Warehouse Manager]
           ↓
          Initiate Partial Fulfillment / Backorder Process
 ↓
Tie Reserved Stock to Specific Order [Warehouse Manager]
 ↓
Reduce Available-to-Promise Balance [Warehouse Manager]
 ↓
Place Order in Fulfillment Queue [Warehouse Manager]
 ↓
Priority or Expedited Order?
 ├── Yes → Assign to Priority Queue [Warehouse Manager]
 └── No → Assign to Standard Queue [Warehouse Manager]
 ↓
Notify Sales and Customer Service of Reservation [Warehouse Manager]
 ↓
End
```

**Decision Points:** Full quantity available? | Priority order?

---

### BP-18: Pick, Pack & Ship

| Attribute | Description |
|-----------|-------------|
| **Process Name** | Pick, Pack & Ship |
| **Start Event** | Reserved order released to fulfillment queue or daily pick wave initiated |
| **End Event** | Order packed, handed to carrier, inventory deducted, customer notified |

```
Start
 ↓
Release Reserved Orders to Pick Queue [Warehouse Manager]
 ↓
Picker Receives Pick List [Warehouse Picker / Packer]
 ↓
Travel to Storage Location and Retrieve Items [Warehouse Picker / Packer]
 ↓
Verify Product Identity and Quantity [Warehouse Packer / Packer]
 ↓
Full Quantity Picked?
 ├── Yes → Proceed to Pack [Warehouse Picker / Packer]
 └── No → Report Exception [Warehouse Picker / Packer]
           ↓
          Initiate Outbound Exception Handling
 ↓
Product Condition Acceptable?
 ├── No → Report Damage [Warehouse Picker / Packer]
 │         ↓
 │        Initiate Outbound Exception Handling
 └── Yes ↓
Pack Items per Shipping Standards [Warehouse Picker / Packer]
 ↓
Apply Shipping Labels and Documentation [Warehouse Picker / Packer]
 ↓
Hand Shipment to Carrier [Warehouse Picker / Packer]
 ↓
Record Tracking Information [Warehouse Manager]
 ↓
Deduct Inventory upon Shipment Confirmation [Warehouse Manager]
 ↓
Notify Customer Service of Shipment [Warehouse Manager]
 ↓
End
```

**Decision Points:** Full quantity picked? | Product condition acceptable?

---

### BP-19: Partial Fulfillment & Backorder Management

| Attribute | Description |
|-----------|-------------|
| **Process Name** | Partial Fulfillment & Backorder Management |
| **Start Event** | Full order quantity cannot be fulfilled at reservation or pick time |
| **End Event** | Customer informed; partial shipment delivered or backorder tracked to resolution |

```
Start
 ↓
Identify Unfulfillable Portion of Order [Warehouse Manager / Operations Director]
 ↓
Confirm Available Quantity for Immediate Shipment [Warehouse Manager]
 ↓
Contact Customer with Partial Delivery Proposal [Customer Service]
 ↓
Customer Accepts Partial Shipment?
 ├── No → Customer Preference?
 │         ├── Wait for Full Order → Place Entire Order on Backorder [Customer Service]
 │         └── Cancel → Release Reservation and Cancel [Customer Service]
 └── Yes ↓
Ship Available Items [Warehouse Manager]
 ↓
Place Remaining Quantity on Backorder [Customer Service]
 ↓
Communicate Expected Availability Date [Customer Service]
 ↓
Expected Date Known?
 ├── Yes → Inform Customer of ETA [Customer Service]
 └── No → Provide Range or Cancel Option [Customer Service]
 ↓
Transfer from Another Location Faster?
 ├── Yes → Initiate Inter-Location Transfer Request [Operations Director]
 └── No → Alert Purchasing for Expedited Replenishment [Purchasing Manager]
 ↓
Inbound Stock Arrives → Reserve Against Backorder Lines [Warehouse Manager]
 ↓
Ship Backordered Items [Warehouse Manager]
 ↓
Notify Customer of Backorder Shipment [Customer Service]
 ↓
End
```

**Decision Points:** Customer accepts partial? | Expected date known? | Transfer faster than purchase?

---

### BP-20: Outbound Exception Handling

| Attribute | Description |
|-----------|-------------|
| **Process Name** | Outbound Exception Handling |
| **Start Event** | Unable-to-pick, damaged item, customer cancellation, or carrier failure |
| **End Event** | Exception resolved, order status updated, inventory corrected if needed |

```
Start
 ↓
Receive Exception Report [Warehouse Picker / Packer / Carrier / Customer Service]
 ↓
Assess Exception Type [Warehouse Manager]
 ↓
Type?
 ├── Stock Not Found → Search Physical Location [Warehouse Staff]
 ├── Damaged Item → Quarantine Product [Warehouse Staff]
 ├── Customer Cancellation → Release Reservation [Customer Service]
 └── Carrier Failure → Hold Shipment for Rebooking [Warehouse Manager]
 ↓
Stock Not Found — Located on Re-Search?
 ├── Yes → Complete Pick [Warehouse Picker / Packer]
 └── No → Inventory Record Error? [Warehouse Manager]
           ├── Yes → Initiate Stock Adjustment [Inventory Controller]
           └── No → Determine Resolution [Warehouse Manager]
 ↓
Resolution?
 ├── Re-Pick → Return to Pick Process [Warehouse Picker / Packer]
 ├── Substitute → Confirm with Customer [Customer Service]
 ├── Partial Ship → Initiate Partial Fulfillment [Warehouse Manager]
 └── Cancel → Release Reservation and Close [Customer Service]
 ↓
Notify Customer of Resolution [Customer Service]
 ↓
Recurring Exception at Same Location or SKU?
 ├── Yes → Report to Inventory Controller [Inventory Controller]
 └── No ↓
End
```

**Decision Points:** Exception type? | Stock found on re-search? | Inventory record error? | Resolution type? | Recurring?

---

## Domain 5: Replenishment

---

### BP-21: Low-Stock Alert Review

| Attribute | Description |
|-----------|-------------|
| **Process Name** | Low-Stock Alert Review |
| **Start Event** | Stock falls below reorder threshold, out-of-stock condition, or priority SKU alert |
| **End Event** | Alert validated or dismissed; replenishment or transfer action initiated |

```
Start
 ↓
Receive Low-Stock or Out-of-Stock Alert [Buyer / Purchasing Manager]
 ↓
Review On-Hand, Reserved, and Available Quantities [Buyer]
 ↓
Check for Existing Open Purchase Orders [Buyer]
 ↓
Stock Already on Order?
 ├── Yes → Dismiss Alert — Monitor Inbound Supply [Buyer]
 │         ↓
 │        End (Monitoring)
 └── No ↓
Validate Alert Against Consumption Trend [Buyer]
 ↓
Alert Valid (Not False Positive)?
 ├── No → Dismiss with Documented Reason [Buyer]
 │         ↓
 │        End (False Alert)
 └── Yes ↓
Priority (A-Class) SKU?
 ├── Yes → Escalate Urgency to Purchasing Manager [Buyer]
 └── No ↓
Transfer Resolve Faster Than Purchase?
 ├── Yes → Initiate Inter-Location Transfer Request [Operations Director]
 └── No → Forward to Replenishment Planning [Buyer]
 ↓
Notify Operations and Sales of Timeline (if out-of-stock) [Buyer]
 ↓
End
```

**Decision Points:** Stock on order? | Alert valid? | Priority SKU? | Transfer faster?

---

### BP-22: Replenishment Planning & Requisition

| Attribute | Description |
|-----------|-------------|
| **Process Name** | Replenishment Planning & Requisition |
| **Start Event** | Validated low-stock alert, scheduled replenishment cycle, or promotional stock build |
| **End Event** | Approved purchase requisition handed off for purchase order placement |

```
Start
 ↓
Receive Validated Replenishment Need [Buyer / Purchasing Manager]
 ↓
Review Movement History and Lead Time [Buyer]
 ↓
Calculate Recommended Order Quantity [Buyer]
 ↓
Check Budget Availability [Buyer]
 ↓
Budget Available?
 ├── No → Defer or Reduce Quantity [Purchasing Manager]
 │         ↓
 │        Inform Operations and Sales [Purchasing Manager]
 └── Yes ↓
Prepare Purchase Requisition [Buyer]
 ↓
Requisition Within Purchasing Manager Authority? [Purchasing Manager]
 ├── Yes → Approve Requisition [Purchasing Manager]
 └── No → Escalate to Finance or COO [Finance Manager / COO]
           ↓
          Approved?
           ├── No → End (Rejected)
           └── Yes ↓
Combine Multiple SKUs from Same Supplier?
 ├── Yes → Consolidate into Single Requisition [Buyer]
 └── No ↓
Hand Off to Purchase Order Placement [Buyer]
 ↓
End
```

**Decision Points:** Budget available? | Within authority? | Consolidate SKUs?

---

### BP-23: Inbound Supply Tracking

| Attribute | Description |
|-----------|-------------|
| **Process Name** | Inbound Supply Tracking |
| **Start Event** | Purchase order placed, supplier confirms shipment, delay reported, or stakeholder inquiry |
| **End Event** | Open orders tracked to receipt or resolution; stakeholders have current ETA visibility |

```
Start
 ↓
Review All Open Purchase Orders [Buyer]
 ↓
Identify Orders Approaching or Past Expected Date [Buyer]
 ↓
Follow Up with Supplier on Status [Buyer]
 ↓
Delivery On Schedule?
 ├── Yes → Continue Monitoring [Buyer]
 └── No → Update Revised ETA [Buyer]
           ↓
          Delay Material to Stockout Risk?
           ├── Yes → Notify Operations, Sales, and Customer Service [Buyer]
           └── No → Update Records Only [Buyer]
 ↓
Explore Alternatives for Critical Delays [Purchasing Manager]
 ↓
Alternatives?
 ├── Expedite with Supplier [Buyer]
 ├── Alternate Supplier [Purchasing Manager]
 └── Wait [Buyer]
 ↓
Shipment Received at Warehouse?
 ├── Yes → Confirm Order Closure [Buyer]
 └── No → Continue Tracking [Buyer]
 ↓
Backorder Fulfillment Triggered? [Warehouse Manager]
 ↓
End
```

**Decision Points:** On schedule? | Material delay? | Alternatives needed? | Received?

---

## Domain 6: Network Balance

---

### BP-24: Inter-Location Transfer Request

| Attribute | Description |
|-----------|-------------|
| **Process Name** | Inter-Location Transfer Request |
| **Start Event** | Stockout or low stock at destination, excess at source, sales request, or rebalancing review |
| **End Event** | Transfer approved or rejected with documented rationale |

```
Start
 ↓
Identify Transfer Need (Product, Quantity, Source, Destination) [Regional Manager / Sales Manager / Operations Director]
 ↓
Verify Source Location Has Unreserved Stock [Requester]
 ↓
Source Has Sufficient Excess?
 ├── No → Reject — Insufficient Stock [Operations Director]
 │         ↓
 │        End (Rejected)
 └── Yes ↓
Submit Transfer Request with Justification [Requester]
 ↓
Review Impact on Source Location Service Levels [Warehouse Manager — Source]
 ↓
Transfer Justified vs. Waiting for Replenishment? [Operations Director]
 ├── No → Reject — Purchase Instead [Operations Director]
 │         ↓
 │        End (Rejected)
 └── Yes ↓
Within Warehouse Manager Authority?
 ├── Yes → Approve Transfer [Warehouse Manager]
 └── No → Escalate to Operations Director [Operations Director]
           ↓
          Approve, Modify, or Reject [Operations Director]
 ↓
Approved?
 ├── Yes → Communicate Authorization to Source and Destination [Operations Director]
 └── No → Notify Requester with Reason [Operations Director]
 ↓
End
```

**Decision Points:** Source has excess? | Transfer justified? | Within authority? | Approved?

---

### BP-25: Inter-Location Transfer Execution

| Attribute | Description |
|-----------|-------------|
| **Process Name** | Inter-Location Transfer Execution |
| **Start Event** | Transfer request approved and ready for physical movement |
| **End Event** | Stock moved, both location balances updated, transfer documentation complete |

```
Start
 ↓
Assign Pick and Pack of Transfer Items [Warehouse Manager — Source]
 ↓
Pick Approved Quantity [Warehouse Staff]
 ↓
Full Approved Quantity Available?
 ├── Yes → Pack Full Quantity [Warehouse Staff]
 └── No → Pack Available Quantity [Warehouse Staff]
           ↓
          Notify Destination of Partial Dispatch [Warehouse Manager — Source]
 ↓
Prepare Transfer Documentation [Warehouse Manager — Source]
 ↓
Arrange Transport [Warehouse Manager — Source / Carrier Partner]
 ↓
Dispatch Shipment — Reduce Source Inventory [Warehouse Manager — Source]
 ↓
Notify Destination of Incoming Transfer with ETA [Warehouse Manager — Source]
 ↓
Accept and Verify Transfer at Destination [Receiving Clerk — Destination]
 ↓
Received Quantity Matches Dispatch?
 ├── Yes → Increase Destination Inventory [Receiving Clerk — Destination]
 └── No → Investigate Variance [Warehouse Manager — Destination]
           ↓
          Initiate Stock Adjustment if Required [Inventory Controller]
 ↓
Items in Acceptable Condition?
 ├── Yes → Confirm Transfer Complete [Warehouse Manager — Destination]
 └── No → Reject Damaged — Initiate Write-Off [Warehouse Manager — Destination]
 ↓
End
```

**Decision Points:** Full quantity available? | Quantity matches? | Condition acceptable?

---

### BP-26: Network Stock Rebalancing

| Attribute | Description |
|-----------|-------------|
| **Process Name** | Network Stock Rebalancing |
| **Start Event** | Weekly or monthly network review, persistent imbalance, seasonal need, or new location stocking |
| **End Event** | Rebalancing plan executed or deferred with documented rationale |

```
Start
 ↓
Initiate Network-Wide Stock Distribution Review [Operations Director]
 ↓
Compile Stock Levels and Demand by Location [Inventory Controller]
 ↓
Identify Overstock and Stockout Imbalances [Inventory Controller]
 ↓
Imbalance Significant Enough to Warrant Transfer Cost? [Operations Director]
 ├── No → Monitor — Inbound PO May Resolve [Operations Director]
 │         ↓
 │        End (Deferred)
 └── Yes ↓
Develop Rebalancing Recommendations [Operations Director]
 ↓
Validate with Regional Managers and Warehouse Managers [Regional Manager / Warehouse Manager]
 ↓
Purchasing Confirms No Inbound PO Will Resolve Soon [Purchasing Manager]
 ↓
Plan Requires Executive Approval?
 ├── Yes → Submit to COO [COO]
 └── No → Operations Director Approves [Operations Director]
 ↓
Approved?
 ├── No → End (Rejected)
 └── Yes ↓
Initiate Transfer Requests per Approved Plan [Operations Director]
 ↓
Execute Transfers [Warehouse Manager]
 ↓
Measure Results in Next Review Cycle [Inventory Controller]
 ↓
End
```

**Decision Points:** Imbalance significant? | Executive approval needed? | Approved?

---

## Domain 7: Returns

---

### BP-27: Customer Return Intake

| Attribute | Description |
|-----------|-------------|
| **Process Name** | Customer Return Intake |
| **Start Event** | Customer initiates return for defect, wrong item, change of mind, or warranty claim |
| **End Event** | Return authorized, documented, and routed for physical receipt and resolution |

```
Start
 ↓
Receive Customer Return Request [Customer Service Representative]
 ↓
Verify Original Order Reference [Customer Service Representative]
 ↓
Return Eligible per Policy? [Customer Service Representative]
 ├── No → Inform Customer — Return Denied [Customer Service Representative]
 │         ↓
 │        End (Denied)
 └── Yes ↓
Document Return: Product, Quantity, Reason [Customer Service Representative]
 ↓
Customer Resolution Expectation?
 ├── Refund → Notify Finance [Finance Manager]
 ├── Replacement → Check Product Availability [Customer Service Representative]
 └── Store Credit → Notify Finance [Finance Manager]
 ↓
Issue Return Authorization and Shipping Instructions [Customer Service Representative]
 ↓
Return Method?
 ├── Ship to Warehouse → Notify Warehouse Manager [Customer Service Representative]
 └── Store Drop-Off → Notify Regional Manager [Regional Manager]
 ↓
Replacement Available?
 ├── Yes → Initiate Replacement Order [Sales Representative]
 └── No → Place Replacement on Backorder [Customer Service Representative]
 ↓
End
```

**Decision Points:** Eligible per policy? | Resolution type? | Return method? | Replacement available?

---

### BP-28: Return-to-Stock or Disposal Decision

| Attribute | Description |
|-----------|-------------|
| **Process Name** | Return-to-Stock or Disposal Decision |
| **Start Event** | Returned goods physically received at warehouse and matched to return authorization |
| **End Event** | Goods dispositioned, inventory updated, financial resolution processed, customer notified |

```
Start
 ↓
Accept Return Shipment [Receiving Clerk]
 ↓
Match to Return Authorization [Receiving Clerk]
 ↓
Authorization Match?
 ├── No → Contact Customer Service [Receiving Clerk]
 │         ↓
 │        Resolve Mismatch [Customer Service Representative]
 └── Yes ↓
Inspect Product Condition and Verify Quantity [Receiving Clerk]
 ↓
Product Meets Resale Quality Standards? [Warehouse Manager]
 ├── Yes → Restock — Add to Inventory [Warehouse Manager]
 └── No → Disposition?
           ├── Rework → Send to Rework Area [Warehouse Manager]
           └── Write Off → Initiate Write-Off [Warehouse Manager]
 ↓
Process Refund or Credit per Agreed Resolution [Finance Manager]
 ↓
Confirm Return Completion to Customer [Customer Service Representative]
 ↓
End
```

**Decision Points:** Authorization match? | Meets resale standards? | Disposition type?

---

## Domain 8: Performance Management & Commercial Alignment

---

### BP-29: Inventory Performance Reporting

| Attribute | Description |
|-----------|-------------|
| **Process Name** | Inventory Performance Reporting |
| **Start Event** | Scheduled reporting cycle, management request, or KPI threshold breach |
| **End Event** | Reports distributed, reviewed, and exceptions assigned for action |

```
Start
 ↓
Compile Inventory Data for Reporting Period [Inventory Controller]
 ↓
Calculate Metrics: Stock Levels, Stockouts, Accuracy, Fill Rate, Movements [Inventory Controller]
 ↓
Data Anomalies Detected?
 ├── Yes → Investigate Before Distribution [Inventory Controller]
 └── No ↓
Prepare Reports for Audience [Inventory Controller]
 ↓
Report Type?
 ├── Daily Operational → Distribute to Warehouse Managers [Inventory Controller]
 ├── Weekly Management → Present at Ops Review [Operations Director]
 └── Monthly Executive → Present to COO, CEO, CFO [Operations Director]
 ↓
KPI Threshold Breached?
 ├── Yes → Assign Corrective Action [Operations Director]
 └── No ↓
Document Trend vs. Prior Period and Targets [Inventory Controller]
 ↓
End
```

**Decision Points:** Data anomalies? | Report type? | KPI breach?

---

### BP-30: Inventory Valuation & Financial Reconciliation

| Attribute | Description |
|-----------|-------------|
| **Process Name** | Inventory Valuation & Financial Reconciliation |
| **Start Event** | Month-end close cycle, quarterly reporting, or audit request |
| **End Event** | Operational and financial records reconciled; variances explained; posting supported |

```
Start
 ↓
Initiate Month-End Inventory Reconciliation [Finance Manager]
 ↓
Extract Operational Inventory Quantities [Finance Manager]
 ↓
Apply Unit Costs or Valuation Rates [Finance Manager]
 ↓
Calculate Total Inventory Value [Finance Manager]
 ↓
Compare to General Ledger Balance [Finance Manager]
 ↓
Variance Within Acceptable Tolerance? [Finance Manager]
 ├── Yes → Prepare Reconciliation Report [Finance Manager]
 └── No → Investigate Variance [Finance Manager]
           ↓
          Variance Cause?
           ├── Timing (In-Transit) → Document and Explain [Finance Manager]
           ├── Unrecorded Receipt → Coordinate with Warehouse [Warehouse Manager]
           └── Operational Error → Initiate Stock Adjustment [Inventory Controller]
 ↓
CFO Reviews Reconciliation [CFO]
 ↓
Reconciliation Approved for Financial Posting?
 ├── Yes → Support Financial Posting [Finance Manager]
 └── No → Hold for Further Review [Finance Manager]
 ↓
Archive Evidence for Audit [Finance Manager]
 ↓
End
```

**Decision Points:** Variance within tolerance? | Variance cause? | Approved for posting?

---

### BP-31: Promotional & Launch Stock Readiness

| Attribute | Description |
|-----------|-------------|
| **Process Name** | Promotional & Launch Stock Readiness |
| **Start Event** | Marketing campaign scheduled, product launch date set, or seasonal peak planning |
| **End Event** | Stock readiness confirmed or gap documented with agreed mitigation before launch |

```
Start
 ↓
Marketing Communicates Campaign Calendar and Promoted SKUs [Marketing Manager]
 ↓
Sales Provides Demand Forecast [Sales Manager]
 ↓
Assess Current and Inbound Stock vs. Campaign Requirements [Inventory Controller]
 ↓
Current Plus Inbound Stock Sufficient?
 ├── Yes → Confirm Readiness [Inventory Controller]
 └── No → Calculate Stock Gap [Inventory Controller]
           ↓
          Purchasing Prepares Pre-Build Orders [Purchasing Manager]
           ↓
          Can Gap Close Before Campaign Start? [Purchasing Manager]
           ├── Yes → Place Expedited Purchase Orders [Buyer]
           └── No → Escalate to Leadership [Marketing Manager / COO]
 ↓
Operations Confirms Warehouse Capacity [Warehouse Manager]
 ↓
Fulfillment Capacity Sufficient for Expected Surge? [Operations Director]
 ├── No → Add Capacity or Limit Promotion Scope [Operations Director]
 └── Yes ↓
Hold Cross-Functional Readiness Review [Marketing Manager]
 ↓
Participants: Marketing, Sales, Purchasing, Operations, Inventory Control
 ↓
Go / No-Go Decision [COO / Marketing Manager]
 ↓
Decision?
 ├── Go → Campaign Proceeds on Schedule
 ├── Delay → Revise Campaign Date [Marketing Manager]
 └── Reduce Scope → Limit Promoted SKUs [Marketing Manager]
 ↓
End
```

**Decision Points:** Stock sufficient? | Gap closable? | Capacity sufficient? | Go / no-go?

---

## Domain 9: Governance & Compliance

---

### BP-32: Inventory Audit & Control Review

| Attribute | Description |
|-----------|-------------|
| **Process Name** | Inventory Audit & Control Review |
| **Start Event** | Quarterly internal audit schedule, annual external audit, or control incident |
| **End Event** | Audit completed, findings documented, corrective actions assigned |

```
Start
 ↓
Define Audit Scope, Period, and Sample Criteria [Internal Auditor]
 ↓
Review Inventory Policies and Segregation of Duties Design [Internal Auditor]
 ↓
Sample Transactions: Receipts, Adjustments, Transfers, Write-Offs [Internal Auditor]
 ↓
Verify Approvals Match Policy Thresholds [Internal Auditor]
 ↓
Test Count Records Against Physical Evidence [Internal Auditor]
 ↓
Interview Process Owners [Internal Auditor]
 ↓
Controls Operating Effectively?
 ├── Yes → Document Strengths [Internal Auditor]
 └── No → Document Deficiencies [Internal Auditor]
 ↓
Finding Material?
 ├── No → Note for Monitoring [Internal Auditor]
 └── Yes → Escalate to COO and CFO [Internal Auditor]
 ↓
Prepare Audit Report with Recommendations [Internal Auditor]
 ↓
Operations Director and COO Review Findings [Operations Director / COO]
 ↓
Assign Corrective Actions and Timelines [COO]
 ↓
External Audit Required?
 ├── Yes → Prepare Evidence Package [Finance Manager / Inventory Controller]
 │         ↓
 │        Provide to External Auditor [External Auditor]
 └── No ↓
Schedule Follow-Up Review for Corrective Actions [Internal Auditor]
 ↓
End
```

**Decision Points:** Controls effective? | Finding material? | External audit required?

---

## Process Map Summary

| Domain | Processes Mapped | Count |
|--------|------------------|-------|
| Master Data & Governance | BP-01 to BP-04 | 4 |
| Inbound & Receiving | BP-05 to BP-09 | 5 |
| Inventory Control | BP-10 to BP-15 | 6 |
| Order Fulfillment | BP-16 to BP-20 | 5 |
| Replenishment | BP-21 to BP-23 | 3 |
| Network Balance | BP-24 to BP-26 | 3 |
| Returns | BP-27 to BP-28 | 2 |
| Performance & Commercial | BP-29 to BP-31 | 3 |
| Governance & Compliance | BP-32 | 1 |
| **Total** | | **32** |

---

## Cross-Process Handoffs

| From Process | To Process | Trigger |
|--------------|------------|---------|
| BP-07 Goods Receipt | BP-08 Discrepancy Resolution | Variance at receiving |
| BP-07 Goods Receipt | BP-09 Put-Away | Clean receipt |
| BP-10 Status Monitoring | BP-21 Low-Stock Review | Threshold breach |
| BP-11 Cycle Count | BP-13 Variance Investigation | Variance exceeds tolerance |
| BP-13 Variance Investigation | BP-14 Stock Adjustment | Approved variance |
| BP-16 Availability Confirmation | BP-17 Reservation | Order confirmed |
| BP-17 Reservation | BP-18 Pick Pack Ship | Order queued |
| BP-18 Pick Pack Ship | BP-19 Partial Fulfillment | Insufficient pick quantity |
| BP-18 Pick Pack Ship | BP-20 Outbound Exception | Pick or carrier failure |
| BP-21 Low-Stock Review | BP-22 Replenishment Planning | Valid alert |
| BP-22 Replenishment Planning | BP-05 Purchase Order | Approved requisition |
| BP-24 Transfer Request | BP-25 Transfer Execution | Approved transfer |
| BP-27 Return Intake | BP-28 Return Disposition | Goods received at warehouse |
| BP-31 Campaign Readiness | BP-05 Purchase Order | Pre-build required |

---

## Document Summary

This document provides text-based process maps for all **32 major inventory management business processes**. Each map includes the process name, start event, sequential activities with responsible actors, decision points with branches, and end event — expressed entirely as business activities without software or database detail.

These maps support process workshops, training, standard operating procedure development, and exception handling design.

---

*End of Business Process Maps Document*
