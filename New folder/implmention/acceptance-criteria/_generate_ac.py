# -*- coding: utf-8 -*-
"""Generate feature-level GWT acceptance criteria for F-01..F-30."""
from pathlib import Path

OUT = Path(__file__).resolve().parent

def ac(id_, given, when, then):
    return {"id": id_, "g": given, "w": when, "t": then}

FEATURES = []

def add(fid, name, stories, roles, happy, validation, errors, permissions, edges):
    FEATURES.append({
        "id": fid, "name": name, "stories": stories, "roles": roles,
        "happy": happy, "validation": validation, "errors": errors,
        "permissions": permissions, "edges": edges,
    })

# ---- F-01 ----
add("F-01", "Product Catalog Management",
    ["US-001","US-002","US-003","US-004"],
    "Inventory Controller, Warehouse Staff (lookup)",
    [
      ac("FAC-01-H1","I am an authorized Inventory Controller and all required attributes (SKU, name, UoM, category) are provided","I create a new product with a unique SKU","the product is saved as ACTIVE and visible to authorized users across locations"),
      ac("FAC-01-H2","an existing ACTIVE product exists","I update name, description, category, or UoM","changes are saved and reflected in all operational views for that SKU"),
      ac("FAC-01-H3","an ACTIVE product exists","I change lifecycle status to INACTIVE or DISCONTINUED with confirmation","the new status is stored with prior status, user, and timestamp, and eligibility rules apply"),
      ac("FAC-01-H4","a product has SKU and barcode identifiers","I search or scan by any assigned identifier during receiving, counting, or picking","the same product record is returned with core attributes"),
      ac("FAC-01-H5","a potential duplicate is detected on create","I confirm merge into the existing product","stock and history remain on a single product identity"),
    ],
    [
      ac("FAC-01-V1","I omit SKU, name, or UoM","I attempt to save","save is blocked and missing required fields are indicated"),
      ac("FAC-01-V2","I enter a SKU that already exists","I attempt to create a new product","duplicate SKU creation is blocked and the existing record is referenced"),
      ac("FAC-01-V3","SKU format is invalid","I attempt to save","validation fails with field-level VAL_* errors"),
      ac("FAC-01-V4","I submit a name/barcode similar to an existing product","I attempt to save","the system flags a potential duplicate and requires review before proceeding"),
      ac("FAC-01-V5","I change status to DISCONTINUED","open POs or reservations exist","the system warns of dependent activity before allowing the change"),
    ],
    [
      ac("FAC-01-E1","the persistence layer fails mid-save","I attempt to create or update a product","no partial product is published and I receive a clear recoverable error"),
      ac("FAC-01-E2","I search with an unknown identifier","I scan or search","no match is returned and no product is auto-created"),
      ac("FAC-01-E3","two products both have on-hand stock","I attempt an unauthorized merge","merge is blocked until authorized Inventory Controller approval"),
      ac("FAC-01-E4","duplicate detection is inconclusive","I cancel the create action","no duplicate or partial record is saved"),
    ],
    [
      ac("FAC-01-P1","I am a user without PRODUCT_MANAGE","I attempt to create or edit a product","the action is denied with AUTH_* / 403 and no data changes"),
      ac("FAC-01-P2","I am Warehouse Staff with PRODUCT_VIEW only","I look up a product by barcode","I can view product identity but cannot edit master data"),
      ac("FAC-01-P3","I lack authority to discontinue products","I attempt to set DISCONTINUED","the action is denied"),
      ac("FAC-01-P4","my location scope is restricted","I look up a product","stock context shown reflects only authorized locations"),
    ],
    [
      ac("FAC-01-X1","a product has existing stock or open orders","I update non-identity attributes","historical transactions remain linked to the same SKU"),
      ac("FAC-01-X2","a new product has no stock policy yet","I create the product","it is receivable and visible but excluded from threshold alerts until thresholds exist"),
      ac("FAC-01-X3","a discontinued product has zero on-hand and no open activity","I search active catalogs","it is excluded by default but remains searchable for history"),
      ac("FAC-01-X4","the same barcode was assigned to two SKUs","duplicate detection runs","I can reassign the barcode without losing movement history"),
    ])

# ---- F-02 ----
add("F-02", "Location & Network Setup",
    ["US-005","US-006","US-007","US-010"],
    "Operations Director, Inventory Controller, Warehouse Manager",
    [
      ac("FAC-02-H1","I am authorized","I create a warehouse/store/DC with code, name, type, and status","the location is available for stock assignment and reporting"),
      ac("FAC-02-H2","multiple locations exist","I assign a parent in the hierarchy","roll-up visibility and accountability use the hierarchy path"),
      ac("FAC-02-H3","a location has storage positions configured","I list positions for put-away","zone/aisle/bin options are available for that location only"),
      ac("FAC-02-H4","opening balances are verified and approved","I activate a location","the location accepts transactional inventory activity"),
      ac("FAC-02-H5","a location is closing with a disposition plan (Phase 2)","I execute closure after stock disposition","the location is closed and no orphan stock remains"),
    ],
    [
      ac("FAC-02-V1","location code or name is missing","I attempt to save","save is blocked with required-field errors"),
      ac("FAC-02-V2","I set a location as its own parent","I save hierarchy","the system rejects the cyclic hierarchy"),
      ac("FAC-02-V3","opening balances are not approved","I attempt to activate the location","activation is blocked until openings are verified"),
      ac("FAC-02-V4","on-hand stock remains without disposition","I attempt to close the location","closure is blocked"),
    ],
    [
      ac("FAC-02-E1","location code already exists","I create a location","creation fails with conflict and existing code is cited"),
      ac("FAC-02-E2","a location is frozen for physical count","I attempt non-count transactions","operations are blocked with freeze reason"),
      ac("FAC-02-E3","storage position belongs to another location","I assign it on put-away for this site","the system rejects the position"),
    ],
    [
      ac("FAC-02-P1","I lack LOCATION_MANAGE","I attempt to create or edit locations","action is denied (403)"),
      ac("FAC-02-P2","I am a Regional Manager scoped to Region A","I list locations","only locations in my scope are returned"),
      ac("FAC-02-P3","I am not Operations Director","I attempt hierarchy redesign or closure","action is denied"),
    ],
    [
      ac("FAC-02-X1","a planned location exists before go-live","I view operational lists","it does not accept receipts/reservations until activated"),
      ac("FAC-02-X2","parent is deactivated","child locations still hold stock","children remain operable until individually changed; roll-up notes inactive parent"),
      ac("FAC-02-X3","I deactivate a location with open transfers in-transit","I confirm deactivation","system warns and restricts new activity while allowing receipt of in-transit"),
    ])

# ---- F-03 ----
add("F-03", "Stock Policy & Product Classification",
    ["US-008","US-009","US-012","US-056"],
    "Inventory Controller, Purchasing Manager, Operations Director",
    [
      ac("FAC-03-H1","product and location exist","I set reorder, minimum, and safety stock for that pair","policy is saved with effective date and prior values retained in history"),
      ac("FAC-03-H2","ATP crosses reorder level","stock status and alert engines evaluate policy","LOW_STOCK / OOS indicators and alerts can fire"),
      ac("FAC-03-H3","I am authorized (Phase 2)","I assign ABC class A/B/C to a product","class is stored and available to counting/alert priority"),
      ac("FAC-03-H4","I publish governance policy with reason codes and thresholds","effective date arrives","new transactions use the new policy version"),
      ac("FAC-03-H5","safety stock protection is enabled","a fulfillment attempt would breach safety stock without exception","the system blocks or requires authorized exception + replenishment plan"),
    ],
    [
      ac("FAC-03-V1","threshold values are negative","I save policy","save is rejected"),
      ac("FAC-03-V2","minimum exceeds reorder without authorized invert","I save","validation fails"),
      ac("FAC-03-V3","ABC value is not A/B/C","I assign classification","validation fails"),
      ac("FAC-03-V4","I try to use a retired reason code","I submit an adjustment","selection is blocked"),
    ],
    [
      ac("FAC-03-E1","policy for location+sku does not exist","downstream status calculation runs","status falls back to defined default (e.g., no threshold alerts) without crashing"),
      ac("FAC-03-E2","two policy versions would overlap effective periods","I publish","system rejects overlapping effectivity"),
      ac("FAC-03-E3","receipt tolerance config is invalid","I save tolerances","save fails with field errors"),
    ],
    [
      ac("FAC-03-P1","I lack POLICY_MANAGE","I attempt to edit thresholds","denied"),
      ac("FAC-03-P2","I lack GOVERNANCE_MANAGE","I attempt to create reason codes or approval thresholds","denied"),
      ac("FAC-03-P3","I am Purchasing Manager with policy view","I view thresholds for my locations","read succeeds; write denied"),
    ],
    [
      ac("FAC-03-X1","threshold change is future-dated","current date is before effective date","old thresholds remain in force until effective date"),
      ac("FAC-03-X2","safety stock bypass is requested with documented approval","authorized user confirms","bypass is allowed and auditable"),
      ac("FAC-03-X3","ABC not yet assigned","cycle count scheduling runs","product is treated as default priority class"),
    ])

# ---- F-04 ----
add("F-04", "Inventory Visibility & Search",
    ["US-023","US-024","US-025","US-026","US-027","US-028"],
    "Inventory Controller, Operations Director, Sales, CSR, Warehouse Manager",
    [
      ac("FAC-04-H1","stock exists at my authorized location","I open inventory status for a SKU","on-hand, reserved, and ATP are displayed"),
      ac("FAC-04-H2","reservations and holds exist","I view ATP","ATP equals on-hand minus reserved minus quarantined"),
      ac("FAC-04-H3","thresholds exist","quantities cross bands","status shows In Stock / Low / Out / Overstock correctly"),
      ac("FAC-04-H4","I enter multi-criteria filters","I search inventory","matching rows for my scope are returned"),
      ac("FAC-04-H5","Phase 2 network view is enabled","I request network ATP for a SKU","rollup across authorized locations is shown including expected inbound when available"),
    ],
    [
      ac("FAC-04-V1","SKU is blank on availability inquiry","I submit","validation requires SKU"),
      ac("FAC-04-V2","page size exceeds max","I request a list","request is rejected or capped per API rules"),
      ac("FAC-04-V3","location filter is outside my scope","I submit","filter is ignored or rejected; only scoped data returns"),
    ],
    [
      ac("FAC-04-E1","SKU does not exist","I inquire availability","404/not found with clear message"),
      ac("FAC-04-E2","downstream stock service is unavailable","I open the monitor","graceful error is shown; no fabricated balances"),
      ac("FAC-04-E3","stock position missing for location+sku","I query detail","empty/zero position semantics are clear (not a crash)"),
    ],
    [
      ac("FAC-04-P1","I am not authenticated","I call stock APIs","401"),
      ac("FAC-04-P2","I lack INVENTORY_VIEW","I open status monitor","403 / route blocked"),
      ac("FAC-04-P3","I am scoped to Location A only","I query Location B","no Location B data is returned"),
    ],
    [
      ac("FAC-04-X1","on-hand is zero but inbound is expected (Phase 2)","I view availability","inbound projection is separate from ATP sellable"),
      ac("FAC-04-X2","lot-tracked product","I drill into position","lot breakdown is available without changing ATP math"),
      ac("FAC-04-X3","concurrent reservation updates ATP","I refresh the view","updated ATP is shown after refresh"),
    ])

# ---- F-05 ----
add("F-05", "Goods Receiving & Verification",
    ["US-015","US-016","US-017","US-019","US-020","US-029"],
    "Receiving Clerk, Warehouse Manager, Buyer",
    [
      ac("FAC-05-H1","a valid open PO exists for my location","I create and verify a goods receipt matching PO lines","receipt is recorded and pending put-away is created"),
      ac("FAC-05-H2","received qty/identity/condition differs","I document a discrepancy with reason and evidence","discrepancy is open and PO/receipt status reflects it"),
      ac("FAC-05-H3","discrepancy is investigated","I resolve it with outcome","resolution is auditable and receipt can proceed per rules"),
      ac("FAC-05-H4","authorized non-PO or return inbound arrives","I record ad-hoc/return receipt with authorization","inbound is captured without inventing a PO"),
      ac("FAC-05-H5","any receipt completes quantity change","I query movement history","an immutable movement record exists with user, time, type, qty"),
    ],
    [
      ac("FAC-05-V1","PO is not valid for receipt","I attempt to receive against it","receipt is blocked (BR-007)"),
      ac("FAC-05-V2","traceable product requires lot","I verify without lot","verification fails"),
      ac("FAC-05-V3","discrepancy lacks reason code","I submit","validation fails"),
      ac("FAC-05-V4","qty is zero or negative","I add a line","validation fails"),
      ac("FAC-05-V5","tolerance exceeded (Phase 2)","qty is outside tolerance","system forces discrepancy path"),
    ],
    [
      ac("FAC-05-E1","PO closed/cancelled","I validate for receipt","validation fails with clear status"),
      ac("FAC-05-E2","location is under physical freeze","I attempt receipt","receipt is blocked"),
      ac("FAC-05-E3","concurrent update conflicts on receipt","I verify","409 conflict; no double-post"),
    ],
    [
      ac("FAC-05-P1","I lack RECEIVE_GOODS","I open goods receipt workbench commands","denied"),
      ac("FAC-05-P2","I am scoped to WH-01","I try to receive into WH-02","denied by location scope"),
      ac("FAC-05-P3","I lack discrepancy resolve permission","I attempt resolve","denied; Receiving Clerk may create but not always resolve"),
    ],
    [
      ac("FAC-05-X1","partial PO receipt","I receive subset of lines","PO remains PARTIAL; remaining qty still receivable"),
      ac("FAC-05-X2","over-receipt within tolerance","auto-accept path applies","no discrepancy required"),
      ac("FAC-05-X3","shelf-life below MRSL","I verify","receipt is blocked or quarantined per policy"),
    ])

# ---- F-06 ----
add("F-06", "Put-Away Management",
    ["US-018"],
    "Warehouse Staff, Warehouse Manager",
    [
      ac("FAC-06-H1","verified receipts await put-away","I open the put-away queue","pending tasks for my location are listed"),
      ac("FAC-06-H2","I select a valid storage position","I confirm put-away","put-away is recorded and sellable ATP increases accordingly"),
      ac("FAC-06-H3","put-away completes","pickers search stock","quantity is locatable at the confirmed position"),
    ],
    [
      ac("FAC-06-V1","storage position is missing","I confirm put-away","validation fails"),
      ac("FAC-06-V2","position is not at receipt location","I confirm","rejected"),
      ac("FAC-06-V3","qty exceeds pending put-away","I confirm","rejected"),
    ],
    [
      ac("FAC-06-E1","receipt not yet verified","I attempt put-away","blocked"),
      ac("FAC-06-E2","already put away","I confirm again","idempotent rejection / already complete"),
      ac("FAC-06-E3","location frozen","I attempt put-away","blocked"),
    ],
    [
      ac("FAC-06-P1","I lack PUT_AWAY_EXECUTE","I confirm put-away","denied"),
      ac("FAC-06-P2","task is for another location outside my scope","I view queue","task not visible"),
    ],
    [
      ac("FAC-06-X1","stock received but not put away","Sales checks ATP","quantity is not fully sellable/available per policy"),
      ac("FAC-06-X2","split put-away across bins","I complete multiple confirmations","pending reaches zero and positions sum to received qty"),
    ])

# ---- F-07 ----
add("F-07", "Purchase Order & Inbound Supply Management",
    ["US-013","US-014","US-021","US-022","US-055","US-079"],
    "Buyer, Purchasing Manager, Warehouse Manager",
    [
      ac("FAC-07-H1","supplier and products are active","I create a PO with lines","PO is OPEN and visible in inbound pipeline"),
      ac("FAC-07-H2","PO is open","I schedule expected delivery dates","inbound calendar reflects the plan"),
      ac("FAC-07-H3","PO needs change","I amend lines/dates or cancel per rules","status and receipt authorization update correctly"),
      ac("FAC-07-H4","open POs and delays exist","I open inbound tracking","open qty, ETA, and delays are visible"),
      ac("FAC-07-H5","inbound delay is detected","notification recipients are configured","delay alert is raised (via F-26)"),
    ],
    [
      ac("FAC-07-V1","supplier is inactive","I create PO","blocked"),
      ac("FAC-07-V2","line product is discontinued","I add line","blocked (BR-027)"),
      ac("FAC-07-V3","line qty <= 0","I save","validation fails"),
      ac("FAC-07-V4","cancel when fully received","I cancel","blocked"),
    ],
    [
      ac("FAC-07-E1","amend after partial receipt beyond allowed","I amend received lines downward below received qty","rejected"),
      ac("FAC-07-E2","supplier code unknown","I reference supplier","404/validation error"),
      ac("FAC-07-E3","concurrent amend","two buyers save","optimistic lock conflict on one"),
    ],
    [
      ac("FAC-07-P1","I lack PO_MANAGE","I create/amend PO","denied"),
      ac("FAC-07-P2","I have PO_VIEW only","I list open POs","read OK, write denied"),
      ac("FAC-07-P3","PO is for another location outside scope","I view","hidden or denied"),
    ],
    [
      ac("FAC-07-X1","requisition converts to PO","I convert approved requisition","PO created with traceable link"),
      ac("FAC-07-X2","supplier performance metrics (Phase 3)","deliveries complete late","performance record updates"),
      ac("FAC-07-X3","expected delivery in the past without receipt","tracking view","shows delayed status"),
    ])

# ---- F-08 ----
add("F-08", "Inter-Location Stock Transfers",
    ["US-058","US-059","US-060","US-061","US-063"],
    "Regional/Store Manager, Operations Director, Warehouse Manager",
    [
      ac("FAC-08-H1","source has transferable capacity above minimum","I submit a transfer request with justification","request is PENDING approval"),
      ac("FAC-08-H2","I am an independent approver","I approve the request","transfer becomes approved for execution"),
      ac("FAC-08-H3","transfer is approved","I dispatch then receive at destination","source decreases, destination increases, in-transit clears"),
      ac("FAC-08-H4","transfer is in transit (Phase 2)","I open in-transit monitor","qty, source, destination, and status are visible"),
      ac("FAC-08-H5","I reject a request with reason","request is rejected","no stock moves; rationale is stored"),
    ],
    [
      ac("FAC-08-V1","source equals destination","I submit","validation fails"),
      ac("FAC-08-V2","requested qty exceeds transfer capacity","I submit","blocked by source minimum (BR-012)"),
      ac("FAC-08-V3","justification missing","I submit","validation fails"),
      ac("FAC-08-V4","qty <= 0","I submit","validation fails"),
    ],
    [
      ac("FAC-08-E1","source location frozen","I dispatch","blocked"),
      ac("FAC-08-E2","approve own request (SoD)","I approve","blocked"),
      ac("FAC-08-E3","receive qty mismatches dispatch","I receive","discrepancy/exception path required"),
    ],
    [
      ac("FAC-08-P1","I lack TRANSFER_REQUEST","I create request","denied"),
      ac("FAC-08-P2","I lack TRANSFER_APPROVE","I approve","denied"),
      ac("FAC-08-P3","I can request for my store but not approve network transfers","I open approval queue","queue empty / unauthorized"),
    ],
    [
      ac("FAC-08-X1","capacity changes after request before approve","approver reviews","system re-validates capacity at approval"),
      ac("FAC-08-X2","cancel after dispatch not allowed","I cancel","only pre-dispatch cancel permitted"),
      ac("FAC-08-X3","partial receive","remaining stays in-transit until complete","balances stay consistent"),
    ])

# ---- F-09 ----
add("F-09", "Network Stock Rebalancing",
    ["US-062"],
    "Operations Director, Inventory Controller",
    [
      ac("FAC-09-H1","network has overstock and stockout sites for a SKU","I run rebalance analysis","imbalance scores and recommendations appear"),
      ac("FAC-09-H2","a recommendation is acceptable","I convert it to a transfer request","F-08 request is created pre-filled"),
    ],
    [
      ac("FAC-09-V1","no SKU/network filter when required","I run analysis","validation requires scope"),
      ac("FAC-09-V2","recommendation would breach source minimum","I convert","blocked or adjusted qty proposed"),
    ],
    [
      ac("FAC-09-E1","insufficient data history","I run analysis","clear unavailable message"),
      ac("FAC-09-E2","intelligence service down","I open UI","error state, no fake recommendations"),
    ],
    [
      ac("FAC-09-P1","I lack NETWORK_REBALANCE_VIEW","I open analysis","denied"),
      ac("FAC-09-P2","I can view but lack TRANSFER_REQUEST","I convert recommendation","convert denied"),
    ],
    [
      ac("FAC-09-X1","multiple recommendations for same source","I convert several","capacity is re-checked sequentially"),
      ac("FAC-09-X2","all locations balanced","I run analysis","empty recommendation set with success status"),
    ])

# ---- F-10 ----
add("F-10", "Order Availability & Reservation",
    ["US-041","US-042","US-043","US-048"],
    "Sales Representative, CSR, Sales Manager",
    [
      ac("FAC-10-H1","ATP is sufficient at a location","I confirm availability for an order","confirmation succeeds with ATP snapshot"),
      ac("FAC-10-H2","availability confirmed","I confirm the order","reservations are created and ATP decreases"),
      ac("FAC-10-H3","order is cancelled before ship","I cancel","reservations release and ATP restores"),
      ac("FAC-10-H4","single location ATP insufficient (Phase 2)","I create multi-location plan","plan allocates across locations without overselling"),
    ],
    [
      ac("FAC-10-V1","order lines empty or qty <= 0","I confirm availability","validation fails"),
      ac("FAC-10-V2","product inactive/discontinued","I reserve","blocked unless authorized exception"),
      ac("FAC-10-V3","requested qty > ATP","I confirm","fails with insufficient ATP"),
    ],
    [
      ac("FAC-10-E1","concurrent reservations exhaust ATP","second confirm runs","one succeeds; other fails with conflict/insufficient ATP"),
      ac("FAC-10-E2","order already cancelled","I reserve again","state error"),
      ac("FAC-10-E3","promotional ring-fence reduces general ATP","I reserve general stock","cannot consume ring-fenced qty"),
    ],
    [
      ac("FAC-10-P1","I lack ORDER_RESERVE","I confirm order","denied"),
      ac("FAC-10-P2","order location outside my scope","I view/reserve","denied or filtered"),
      ac("FAC-10-P3","unauthenticated","I call availability API","401"),
    ],
    [
      ac("FAC-10-X1","partial line availability","I confirm","system reports which lines fail"),
      ac("FAC-10-X2","release after partial fulfill","I cancel remaining","only open reservations release"),
      ac("FAC-10-X3","idempotent confirm retry with same key","I retry","no double reservation"),
    ])

# ---- F-11 ----
add("F-11", "Pick, Pack & Ship Fulfillment",
    ["US-044","US-049"],
    "Warehouse Picker/Packer, Warehouse Manager, CSR",
    [
      ac("FAC-11-H1","confirmed reserved orders await pick","I generate/open pick list","queue shows my location work"),
      ac("FAC-11-H2","I pick and verify lines","I pack and ship","shipment is confirmed and on-hand decreases; reservation clears"),
      ac("FAC-11-H3","order progresses","CSR opens status","reservation/pick/pack/ship states are visible"),
    ],
    [
      ac("FAC-11-V1","verify qty does not match pick","I submit verify","fails"),
      ac("FAC-11-V2","lot required but missing","I verify pick","fails"),
      ac("FAC-11-V3","ship before pack","I ship","blocked"),
    ],
    [
      ac("FAC-11-E1","location frozen","I pick","blocked"),
      ac("FAC-11-E2","stock physically missing at pick","I record pick failure","exception path (F-13) engaged; no silent short ship"),
      ac("FAC-11-E3","shipment API fails after pack","I retry ship","no double deduction"),
    ],
    [
      ac("FAC-11-P1","I lack FULFILL_PICK","I verify pick","denied"),
      ac("FAC-11-P2","I lack FULFILL_SHIP","I confirm shipment","denied"),
      ac("FAC-11-P3","pick queue for other site","I list awaiting picks","not visible outside scope"),
    ],
    [
      ac("FAC-11-X1","FEFO lot selection","I pick perishable","system guides/enforces rotation policy"),
      ac("FAC-11-X2","status inquiry during pick","CSR views","shows in-progress state"),
      ac("FAC-11-X3","gap C-01 location queue missing","workaround list-by-order works until endpoint added","documented limitation not treated as pass"),
    ])

# ---- F-12 ----
add("F-12", "Partial Fulfillment & Backorder Management",
    ["US-045","US-046"],
    "CSR, Warehouse Manager, Purchasing",
    [
      ac("FAC-12-H1","full qty unavailable","I ship available qty with customer acknowledgment","partial shipment posts; backorder created for remainder"),
      ac("FAC-12-H2","stock arrives for backorder (Phase 2)","priority queue auto-reserves","backorder can be fulfilled in sequence"),
      ac("FAC-12-H3","I view backorder board","open backorders show","customer, SKU, qty, priority, status"),
    ],
    [
      ac("FAC-12-V1","partial ship without customer ack","I submit","blocked"),
      ac("FAC-12-V2","ship qty > available","I submit","blocked"),
      ac("FAC-12-V3","backorder qty <= 0","I create","validation fails"),
    ],
    [
      ac("FAC-12-E1","order already fully shipped","I create backorder","rejected"),
      ac("FAC-12-E2","backorder fulfill when ATP still insufficient","I fulfill","fails with clear ATP error"),
    ],
    [
      ac("FAC-12-P1","I lack BACKORDER_MANAGE","I create/prioritize backorders","denied"),
      ac("FAC-12-P2","CSR can ack partial but not change purchasing priority","I edit priority","denied if not authorized"),
    ],
    [
      ac("FAC-12-X1","multiple backorders same SKU","stock arrives for 1 unit","highest priority consumes first"),
      ac("FAC-12-X2","customer cancels backorder","I cancel","reservation/backorder cleared"),
    ])

# ---- F-13 ----
add("F-13", "Fulfillment Exception Handling",
    ["US-047","US-050","US-078"],
    "Warehouse Manager, CSR, Inventory Controller",
    [
      ac("FAC-13-H1","pick failure or damage occurs","I create an exception with reason","order is routed out of happy path; alert raised"),
      ac("FAC-13-H2","damage exception","I apply quarantine","ATP excludes damaged qty"),
      ac("FAC-13-H3","exception resolved","I return order to correct flow or cancel","status and inventory corrected"),
      ac("FAC-13-H4","authorized substitution (Phase 3)","approver accepts substitute SKU","fulfillment continues with audit of substitution"),
    ],
    [
      ac("FAC-13-V1","exception without reason","I submit","validation fails"),
      ac("FAC-13-V2","substitution without approval","I submit substitute","blocked"),
    ],
    [
      ac("FAC-13-E1","resolve already-resolved exception","I resolve again","rejected"),
      ac("FAC-13-E2","exception on cancelled order","I create","rejected"),
    ],
    [
      ac("FAC-13-P1","I lack FULFILL_EXCEPTION_MANAGE","I create/resolve","denied"),
      ac("FAC-13-P2","picker can report but not approve substitution","I approve substitute","denied"),
    ],
    [
      ac("FAC-13-X1","exception mid-pack","I resolve to re-pick","pack state resets appropriately"),
      ac("FAC-13-X2","alert delivery fails","exception still saved","retry notification without losing exception"),
    ])

# ---- F-14 ----
add("F-14", "Cycle Counting",
    ["US-030","US-031","US-071"],
    "Inventory Controller, Warehouse Staff",
    [
      ac("FAC-14-H1","I schedule and assign cycle counts","assignees open workbench","assigned blind counts appear"),
      ac("FAC-14-H2","I am a counter","I enter physical qty without seeing system qty","result submits and variances generate when mismatch"),
      ac("FAC-14-H3","counts complete over a period","accuracy report runs","count performance metrics are available"),
    ],
    [
      ac("FAC-14-V1","assignment missing user/location/sku","I create count","validation fails"),
      ac("FAC-14-V2","negative count qty","I submit","validation fails"),
      ac("FAC-14-V3","UI attempts to display system qty to counter","blind mode","system qty is not shown"),
    ],
    [
      ac("FAC-14-E1","submit twice","I resubmit","rejected as already submitted"),
      ac("FAC-14-E2","count for unknown SKU","I submit","rejected"),
    ],
    [
      ac("FAC-14-P1","I lack CYCLE_COUNT_EXECUTE","I submit count","denied"),
      ac("FAC-14-P2","I lack CYCLE_COUNT_MANAGE","I schedule counts","denied"),
      ac("FAC-14-P3","assigned to another user","I open my queue","I do not see others' assignments"),
    ],
    [
      ac("FAC-14-X1","ABC-A counted more frequently","schedule generated","A items appear more often than C"),
      ac("FAC-14-X2","zero physical found","I enter 0","variance equals full system qty"),
    ])

# ---- F-15 ----
add("F-15", "Full Physical Inventory Count",
    ["US-032"],
    "Inventory Controller, Warehouse Manager, Ops Director",
    [
      ac("FAC-15-H1","I initiate physical count for a location","freeze activates","receiving/shipping/transfers/adjustments blocked"),
      ac("FAC-15-H2","teams enter results","I monitor progress","completion % is visible"),
      ac("FAC-15-H3","all zones complete","I certify the count","variances are produced and freeze can be released per process"),
    ],
    [
      ac("FAC-15-V1","certify while incomplete","I certify","blocked"),
      ac("FAC-15-V2","missing location","I create count","validation fails"),
    ],
    [
      ac("FAC-15-E1","transaction attempted during freeze","I receive/ship","blocked with freeze status"),
      ac("FAC-15-E2","certify without authority","I certify","denied"),
    ],
    [
      ac("FAC-15-P1","I lack PHYSICAL_COUNT_MANAGE","I initiate","denied"),
      ac("FAC-15-P2","I lack PHYSICAL_COUNT_CERTIFY","I certify","denied"),
      ac("FAC-15-P3","staff can enter counts but not lift freeze","I attempt unfreeze","denied"),
    ],
    [
      ac("FAC-15-X1","in-transit transfer exists at freeze start","I initiate","system warns and handles per policy"),
      ac("FAC-15-X2","recount required for large variance","I flag recount","certify waits on recount"),
    ])

# ---- F-16 ----
add("F-16", "Count Variance Investigation & Approval",
    ["US-033","US-034","US-037"],
    "Inventory Controller, Warehouse Manager, Ops Director",
    [
      ac("FAC-16-H1","count results differ from system","variances appear in case","classified vs tolerance"),
      ac("FAC-16-H2","I investigate with findings","independent approver approves","adjustment posts to stock"),
      ac("FAC-16-H3","variance above threshold","routing sends to elevated approver","approval by correct role required"),
    ],
    [
      ac("FAC-16-V1","approve without investigation findings when required","I approve","blocked"),
      ac("FAC-16-V2","reject without reason","I reject","validation fails"),
    ],
    [
      ac("FAC-16-E1","counter approves own count","I approve","SoD violation blocked"),
      ac("FAC-16-E2","approve already approved case","I approve again","rejected"),
    ],
    [
      ac("FAC-16-P1","I lack VARIANCE_INVESTIGATE","I add findings","denied"),
      ac("FAC-16-P2","I lack VARIANCE_APPROVE","I approve","denied"),
      ac("FAC-16-P3","threshold requires Finance","Ops Director approves high-value write-down","blocked until Finance"),
    ],
    [
      ac("FAC-16-X1","within tolerance auto-classify","case created","may auto-route to simplified path per policy"),
      ac("FAC-16-X2","pending approval notification","approver subscribed","F-26 alert created"),
    ])

# ---- F-17 ----
add("F-17", "Stock Adjustments & Write-Offs",
    ["US-011","US-035","US-036","US-077"],
    "Warehouse Manager, Inventory Controller, Ops Director, Finance",
    [
      ac("FAC-17-H1","I maintain reason codes","codes are active","selectable on adjustments/discrepancies"),
      ac("FAC-17-H2","I submit adjustment with reason and qty","routing applies","pending approval then posts to stock + movement"),
      ac("FAC-17-H3","I submit write-off with evidence","authorized approvers approve","qty permanently removed with audit"),
      ac("FAC-17-H4","adjustment pending","approver notified","F-26 approval notification delivered"),
    ],
    [
      ac("FAC-17-V1","adjustment without reason code","I submit","blocked"),
      ac("FAC-17-V2","retired reason code","I select","blocked"),
      ac("FAC-17-V3","write-off without evidence when required","I submit","blocked"),
      ac("FAC-17-V4","qty zero","I submit","blocked"),
    ],
    [
      ac("FAC-17-E1","approve own adjustment (SoD)","I approve","blocked"),
      ac("FAC-17-E2","insufficient on-hand for negative adjustment","I approve","blocked"),
      ac("FAC-17-E3","location frozen","I submit ad-hoc adjust","blocked except count-driven path"),
    ],
    [
      ac("FAC-17-P1","I lack ADJUST_SUBMIT","I submit","denied"),
      ac("FAC-17-P2","I lack ADJUST_APPROVE / WRITE_OFF_AUTHORIZE","I approve","denied"),
      ac("FAC-17-P3","Finance-only write-off tier","Ops tries to final-approve","denied"),
    ],
    [
      ac("FAC-17-X1","threshold exactly at boundary","I submit","routes to correct approver tier"),
      ac("FAC-17-X2","reject adjustment","stock unchanged","reason stored; submitter notified"),
    ])

# ---- F-18 ----
add("F-18", "Quarantine & Hold Stock Management",
    ["US-038"],
    "Warehouse Manager, Inventory Controller",
    [
      ac("FAC-18-H1","sellable stock exists","I apply quarantine hold with type/reason/qty","ATP decreases; register shows hold"),
      ac("FAC-18-H2","inspection complete","I release hold to available","ATP restores"),
      ac("FAC-18-H3","hold should be written off","I route to write-off","F-17 path can consume held qty"),
    ],
    [
      ac("FAC-18-V1","hold qty > available for hold","I apply","blocked"),
      ac("FAC-18-V2","missing hold type/reason","I apply","validation fails"),
    ],
    [
      ac("FAC-18-E1","release unknown hold","I release","404"),
      ac("FAC-18-E2","double release","I release again","rejected"),
    ],
    [
      ac("FAC-18-P1","I lack QUARANTINE_MANAGE","I apply/release","denied"),
      ac("FAC-18-P2","location outside scope","I view register","not visible"),
    ],
    [
      ac("FAC-18-X1","reserved qty exists","I apply hold","cannot hold reserved qty beyond rules; reservation preserved"),
      ac("FAC-18-X2","bonded/customs hold type","ATP excluded","fulfillment blocked for that qty"),
    ])

# ---- F-19 ----
add("F-19", "Shrinkage & Obsolescence Analysis",
    ["US-039","US-040"],
    "Inventory Controller, Finance, Ops, Purchasing",
    [
      ac("FAC-19-H1","reason-coded losses exist","I run shrinkage analysis for a period","trends by reason/location/sku display"),
      ac("FAC-19-H2","slow-moving stock exists (Phase 3)","I open obsolescence view","candidates and disposition actions are listed"),
    ],
    [
      ac("FAC-19-V1","end date before start date","I run report","validation fails"),
      ac("FAC-19-V2","period exceeds max window","I run","validation fails or requires export job"),
    ],
    [
      ac("FAC-19-E1","no adjustment history","I run","empty result with success, not error"),
      ac("FAC-19-E2","intelligence API down","I open page","error banner"),
    ],
    [
      ac("FAC-19-P1","I lack SHRINKAGE_VIEW","I open analysis","denied"),
      ac("FAC-19-P2","scoped user","I run","only scoped locations included"),
    ],
    [
      ac("FAC-19-X1","retired reason codes in history","I analyze","historical codes still appear in trends"),
      ac("FAC-19-X2","action from obsolete list creates write-off","I launch disposition","F-17 draft prefilled"),
    ])

# ---- F-20 ----
add("F-20", "Low-Stock Alerting & Replenishment",
    ["US-051","US-052","US-053","US-054","US-074"],
    "Purchasing Manager, Buyer, Inventory Controller",
    [
      ac("FAC-20-H1","ATP reaches reorder level","alert is generated","appears in alert review with SKU/location/severity"),
      ac("FAC-20-H2","I acknowledge an alert","ack stored","alert leaves unread / requires rationale if dismissed"),
      ac("FAC-20-H3","network has surplus elsewhere","I view recommendation","transfer-before-buy suggested"),
      ac("FAC-20-H4","I create requisition from recommendation (Phase 2)","approval then convert to PO","traceable replenishment path"),
      ac("FAC-20-H5","I open replenishment reporting","period metrics show","alerts acted vs ignored"),
    ],
    [
      ac("FAC-20-V1","dismiss without rationale when required","I dismiss","blocked"),
      ac("FAC-20-V2","requisition line qty <= 0","I submit","validation fails"),
      ac("FAC-20-V3","approve requisition without network check","system evaluates","must consider transfer options (BR-011)"),
    ],
    [
      ac("FAC-20-E1","acknowledge unknown alert","I ack","404"),
      ac("FAC-20-E2","convert unapproved requisition to PO","I convert","blocked"),
      ac("FAC-20-E3","duplicate alert storm for same breach","generation runs","deduped/coalesced per policy"),
    ],
    [
      ac("FAC-20-P1","I lack ALERT_REVIEW","I ack","denied"),
      ac("FAC-20-P2","I lack REQUISITION_APPROVE","I approve","denied"),
      ac("FAC-20-P3","buyer can create requisition but not convert","I convert","denied"),
    ],
    [
      ac("FAC-20-X1","threshold changed after alert","I review","alert shows snapshot vs current policy"),
      ac("FAC-20-X2","OOS vs low-stock","both fire","distinct severities"),
      ac("FAC-20-X3","C-03 list API missing","queue UX limited","not accepted as complete until list endpoint exists"),
    ])

# ---- F-21 ----
add("F-21", "Returns Management",
    ["US-064","US-065","US-066","US-067"],
    "CSR, Receiving Clerk, Warehouse Manager, Inventory Controller",
    [
      ac("FAC-21-H1","original order exists and is eligible","I create RA","RA issued and visible to warehouse"),
      ac("FAC-21-H2","goods arrive","I receive against RA and inspect","inspection result recorded"),
      ac("FAC-21-H3","disposition RESTOCK","I complete disposition","ATP increases for sellable qty"),
      ac("FAC-21-H4","disposition WRITE_OFF or QUARANTINE","I complete","stock does not re-enter sellable incorrectly"),
      ac("FAC-21-H5","CSR views status","end-to-end RA→receive→disposition status visible","customer communication supported"),
    ],
    [
      ac("FAC-21-V1","RA qty > shipped qty","I create","blocked"),
      ac("FAC-21-V2","disposition before inspection","I disposition","blocked"),
      ac("FAC-21-V3","invalid disposition decision","I submit","validation fails"),
    ],
    [
      ac("FAC-21-E1","receive without RA when RA required","I receive","blocked"),
      ac("FAC-21-E2","cancel RA after receipt started","I cancel","blocked"),
      ac("FAC-21-E3","wrong item vs RA","I inspect","discrepancy/exception required"),
    ],
    [
      ac("FAC-21-P1","I lack RETURN_AUTHORIZE","I create RA","denied"),
      ac("FAC-21-P2","I lack RETURN_DISPOSITION","I disposition","denied"),
      ac("FAC-21-P3","CSR cannot write-off high value without Finance","I write-off","routed/denied per threshold"),
    ],
    [
      ac("FAC-21-X1","partial return lines","I RA subset","remaining order lines unaffected"),
      ac("FAC-21-X2","restock damaged accidentally selected","policy prevents","only RESTOCK if inspection OK"),
    ])

# ---- F-22 ----
add("F-22", "Inventory Reporting & Dashboards",
    ["US-068","US-069","US-070","US-072","US-074"],
    "Ops Director, COO, Inventory Controller, Warehouse Manager, Purchasing",
    [
      ac("FAC-22-H1","operational data exists","I open operational dashboard","KPIs/stock health/alerts/tasks load for my scope"),
      ac("FAC-22-H2","I run movement report for a period","filters applied","movements by type/product/location returned"),
      ac("FAC-22-H3","stockouts/overstocks exist","I run stock health report","items listed with status"),
      ac("FAC-22-H4","counts/variances exist","I run accuracy report","accuracy metrics display"),
      ac("FAC-22-H5","Phase 2 location performance","I open location snapshot","per-location metrics shown"),
    ],
    [
      ac("FAC-22-V1","invalid date range","I run report","validation fails"),
      ac("FAC-22-V2","export without required filters","I export","validation fails"),
    ],
    [
      ac("FAC-22-E1","report API timeout","I load dashboard","error state per widget, not blank fake zeros without indicator"),
      ac("FAC-22-E2","no data in period","I run","empty successful result"),
    ],
    [
      ac("FAC-22-P1","I lack DASHBOARD_VIEW / REPORT_VIEW","I open","denied"),
      ac("FAC-22-P2","scoped user","I view dashboard","only scoped locations"),
      ac("FAC-22-P3","executive-only widgets","warehouse user","does not see exec-only tiles"),
    ],
    [
      ac("FAC-22-X1","drill-down from KPI","I click stockout card","navigates to filtered status monitor"),
      ac("FAC-22-X2","refresh","I refresh","data reloads with timestamp"),
    ])

# ---- F-23 ----
add("F-23", "Inventory Performance KPIs",
    ["US-073"],
    "CEO, COO, CFO, Ops Director",
    [
      ac("FAC-23-H1","fulfillment and inventory history exist","I open executive KPI dashboard","fill rate, turnover, DOS, accuracy vs targets display"),
      ac("FAC-23-H2","I select a period","trends update","comparison to targets visible"),
    ],
    [
      ac("FAC-23-V1","period missing","I query KPIs","validation fails"),
    ],
    [
      ac("FAC-23-E1","insufficient history for turnover","I view","KPI shows unavailable/N/A with explanation"),
      ac("FAC-23-E2","service error","I open","error banner"),
    ],
    [
      ac("FAC-23-P1","I lack KPI_VIEW_EXEC","I open UI-003","denied"),
      ac("FAC-23-P2","non-executive role","I navigate via URL","blocked by permission guard"),
    ],
    [
      ac("FAC-23-X1","target not configured","I view","KPI shows value without target comparison"),
      ac("FAC-23-X2","drill to operational report","I click fill rate","opens supporting F-22 report"),
    ])

# ---- F-24 ----
add("F-24", "Financial Inventory Reconciliation",
    ["US-075","US-089"],
    "Finance Manager, CFO, Inventory Controller, Auditor",
    [
      ac("FAC-24-H1","PO, GR, and invoice exist","I run three-way match","match result success/fail recorded"),
      ac("FAC-24-H2","match succeeds","I authorize payment","authorization stored"),
      ac("FAC-24-H3","period close","I generate valuation snapshot","quantities/values available for recon"),
      ac("FAC-24-H4","operational vs finance variance","I reconcile and sign off","status finalized with audit"),
    ],
    [
      ac("FAC-24-V1","invoice lines don't reference PO","I register","validation fails"),
      ac("FAC-24-V2","authorize payment before match","I authorize","blocked"),
    ],
    [
      ac("FAC-24-E1","qty mismatch PO/GR/invoice","I match","fail with detailed differences"),
      ac("FAC-24-E2","consignment not owned","valuation treats correctly","not counted as owned until ownership transfer"),
    ],
    [
      ac("FAC-24-P1","I lack FINANCE_INVOICE / RECONCILE","I match or sign off","denied"),
      ac("FAC-24-P2","I am an Ops user without finance roles","I open valuation","read-only or denied per role"),
    ],
    [
      ac("FAC-24-X1","partial GR vs invoice","match","partial match states supported"),
      ac("FAC-24-X2","re-open closed period requires elevated auth","I attempt","denied or special override audited"),
    ])

# ---- F-25 ----
add("F-25", "Promotional & Launch Stock Readiness",
    ["US-057","US-080"],
    "Marketing Manager, Purchasing, Warehouse, Sales, Ops",
    [
      ac("FAC-25-H1","campaign targets defined","I create allocation and ring-fence qty","general ATP reduced; campaign ATP tracked"),
      ac("FAC-25-H2","I run readiness check","coverage vs target shown","go/no-go indicated"),
      ac("FAC-25-H3","campaign ends","I release allocation","qty returns to general ATP"),
      ac("FAC-25-H4","readiness below threshold","campaign alert raised","F-26 notifies stakeholders"),
    ],
    [
      ac("FAC-25-V1","ring-fence qty > ATP","I allocate","blocked"),
      ac("FAC-25-V2","override without reason","I override","blocked"),
    ],
    [
      ac("FAC-25-E1","release unknown allocation","I release","404"),
      ac("FAC-25-E2","fulfillment tries to consume ring-fence for normal order","reserve","blocked from ring-fence pool"),
    ],
    [
      ac("FAC-25-P1","I lack CAMPAIGN_MANAGE","I create allocation","denied"),
      ac("FAC-25-P2","I lack CAMPAIGN_OVERRIDE","I override no-go","denied"),
    ],
    [
      ac("FAC-25-X1","multi-location allocation","readiness","aggregates per location and total"),
      ac("FAC-25-X2","partial release","I release subset","remaining stays ring-fenced"),
    ])

# ---- F-26 ----
add("F-26", "Operational Notifications & Alerts",
    ["US-076","US-077","US-078","US-079","US-080"],
    "All operational roles (role-filtered)",
    [
      ac("FAC-26-H1","low-stock event occurs","I open notification center / badge","alert visible to purchasing roles"),
      ac("FAC-26-H2","approval pending","approver is notified","deep link opens approval queue"),
      ac("FAC-26-H3","I acknowledge alert","unread count decreases","ack user/time stored"),
      ac("FAC-26-H4","transfer/fulfillment/inbound delay events (Phase 2)","respective roles notified","alerts categorized correctly"),
    ],
    [
      ac("FAC-26-V1","ack without required rationale on dismiss","I dismiss","blocked"),
    ],
    [
      ac("FAC-26-E1","ack alert not in my feed","I ack by ID","403/404"),
      ac("FAC-26-E2","producer fails to write alert","business txn still commits","outbox retries alert without losing source txn"),
    ],
    [
      ac("FAC-26-P1","warehouse user","I open feed","does not see finance-only alerts"),
      ac("FAC-26-P2","unauthenticated","I call alert API","401"),
      ac("FAC-26-P3","I lack ALERT_VIEW","I open center","denied"),
    ],
    [
      ac("FAC-26-X1","burst of alerts","feed","pagination/grouping prevents overload"),
      ac("FAC-26-X2","already acked","I ack again","idempotent success"),
      ac("FAC-26-X3","campaign alerts deferred","feature flag off","US-080 not delivered"),
    ])

# ---- F-27 ----
add("F-27", "User Access & Role Management",
    ["US-081","US-082","US-085"],
    "IMS Administrator, Ops Director",
    [
      ac("FAC-27-H1","valid credentials for active user","I sign in","session established with roles and location scope"),
      ac("FAC-27-H2","I create a user and assign roles/locations","user activates","user can access permitted functions only"),
      ac("FAC-27-H3","I suspend or deactivate a user","user attempts login","access blocked"),
      ac("FAC-27-H4","I sign out","session ends","protected routes require login again"),
    ],
    [
      ac("FAC-27-V1","missing username/password","I sign in","validation fails"),
      ac("FAC-27-V2","assign unknown role code","I assign","validation fails"),
      ac("FAC-27-V3","user without location scope where required","I save","validation fails or warns per policy"),
    ],
    [
      ac("FAC-27-E1","invalid credentials","I sign in","401 with generic message (no user enumeration)"),
      ac("FAC-27-E2","suspended user","I sign in","denied with suspended reason"),
      ac("FAC-27-E3","expired/invalid token","I call API","401"),
    ],
    [
      ac("FAC-27-P1","non-admin","I open user admin","denied"),
      ac("FAC-27-P2","admin cannot assign roles above policy without elevated right","I assign","denied"),
      ac("FAC-27-P3","user cannot escalate own permissions","I self-assign ADMIN","denied"),
    ],
    [
      ac("FAC-27-X1","IdP sync updates roles","sync runs","local assignments reconcile per sync rules"),
      ac("FAC-27-X2","remember-session optional","I check remember","session duration follows policy"),
      ac("FAC-27-X3","concurrent sessions","logout-all if supported","other sessions invalidated per design"),
    ])

# ---- F-28 ----
add("F-28", "Operational Accountability & Controls",
    ["US-083","US-084"],
    "All users (enforced); Admin/Auditor configure",
    [
      ac("FAC-28-H1","I perform a material action (adjust/approve/receive)","action completes","activity/audit record captures user, action, entity, timestamp"),
      ac("FAC-28-H2","initiator and approver are different authorized users","approval proceeds","SoD evaluation passes"),
      ac("FAC-28-H3","conflicting roles on one user","user attempts conflicting action pair","blocked by SoD policy"),
    ],
    [
      ac("FAC-28-V1","SoD evaluate missing actor/action","I call evaluate","validation fails"),
    ],
    [
      ac("FAC-28-E1","same user initiates and approves","I approve","SoD violation 422/403"),
      ac("FAC-28-E2","location scope mismatch on action","I act on out-of-scope location","blocked"),
    ],
    [
      ac("FAC-28-P1","user with only submit rights","I approve","denied"),
      ac("FAC-28-P2","auditor can view activity but not approve inventory","I approve adjustment","denied"),
    ],
    [
      ac("FAC-28-X1","break-glass emergency override exists","override used","requires elevated role and is heavily audited"),
      ac("FAC-28-X2","read-only views","I view stock","may log access if policy requires; no SoD on reads"),
    ])

# ---- F-29 ----
add("F-29", "Audit Trail & Compliance",
    ["US-086","US-087","US-088"],
    "Internal/External Auditor, Finance, Ops Director",
    [
      ac("FAC-29-H1","inventory qty changed via any mutator","I query movements/audit","immutable record exists with before/after where applicable"),
      ac("FAC-29-H2","I filter audit by entity/user/date (Phase 2)","results return","export available within limits"),
      ac("FAC-29-H3","control breach detected (Phase 2)","breach recorded","visible in audit workspace"),
    ],
    [
      ac("FAC-29-V1","query without mandatory filters on large dataset","I search","validation requires narrowed scope"),
      ac("FAC-29-V2","export exceeds size limit","I export","rejected or async job required"),
    ],
    [
      ac("FAC-29-E1","attempt to update/delete audit row via API","I call update","not allowed / 405/404"),
      ac("FAC-29-E2","unauthorized export","I export","denied"),
    ],
    [
      ac("FAC-29-P1","I lack AUDIT_VIEW","I open audit trail","denied"),
      ac("FAC-29-P2","I lack AUDIT_EXPORT","I export","denied"),
      ac("FAC-29-P3","warehouse operator","I open auditor workspace","denied"),
    ],
    [
      ac("FAC-29-X1","high-volume day","I query","pagination performs within NFR"),
      ac("FAC-29-X2","movement and audit both exist for same event","I correlate via trace/entity ids","consistent story"),
    ])

# ---- F-30 ----
add("F-30", "System Go-Live & Initial Data Setup",
    ["US-090"],
    "Inventory Controller, Ops Director, IMS Administrator",
    [
      ac("FAC-30-H1","I upload a valid product import file","validation passes","products created/updated in reviewable batch"),
      ac("FAC-30-H2","I load verified opening balances","approver approves","stock positions established"),
      ac("FAC-30-H3","openings approved","I activate location","location becomes operational"),
    ],
    [
      ac("FAC-30-V1","file missing required columns","I upload","validation errors per row/column"),
      ac("FAC-30-V2","duplicate SKUs inside file","I upload","rows flagged; batch not activated blindly"),
      ac("FAC-30-V3","opening qty negative","I load","rejected"),
      ac("FAC-30-V4","activate without approved openings when required","I activate","blocked"),
    ],
    [
      ac("FAC-30-E1","partial failure mid-import","I upload","failed rows reported; no silent partial publish without report"),
      ac("FAC-30-E2","SKU in openings missing from catalog","I load openings","row errors; no orphan stock"),
      ac("FAC-30-E3","approve already-activated batch incorrectly","I re-run","idempotent/guarded behavior"),
    ],
    [
      ac("FAC-30-P1","I lack DATA_IMPORT","I upload","denied"),
      ac("FAC-30-P2","I lack OPENING_BALANCE_APPROVE","I approve openings","denied"),
      ac("FAC-30-P3","importer cannot self-approve openings if SoD required","same user approves","blocked"),
    ],
    [
      ac("FAC-30-X1","re-import updates existing SKUs","I import","updates applied per upsert rules with audit"),
      ac("FAC-30-X2","dry-run/validate-only","I validate without commit","errors shown; DB unchanged"),
      ac("FAC-30-X3","production cutover after UAT","I load production openings","uses same controls as test with dual control"),
    ])


def render_section(title, items):
    lines = [f"### {title}", ""]
    for a in items:
        lines.append(f"#### {a['id']}")
        lines.append(f"- **Given** {a['g']}")
        lines.append(f"- **When** {a['w']}")
        lines.append(f"- **Then** {a['t']}")
        lines.append("")
    return "\n".join(lines)


def render_feature(f):
    stories = ", ".join(f["stories"])
    counts = (
        len(f["happy"]), len(f["validation"]), len(f["errors"]),
        len(f["permissions"]), len(f["edges"])
    )
    total = sum(counts)
    return f"""# Acceptance Criteria — {f['id']}: {f['name']}

| Attribute | Detail |
|-----------|--------|
| **Feature ID** | {f['id']} |
| **Feature Name** | {f['name']} |
| **Document Type** | Feature Acceptance Criteria (PO + QA Lead) |
| **Related user stories** | {stories} |
| **Primary roles** | {f['roles']} |
| **Format** | Given / When / Then |
| **Criteria count** | {total} (H{counts[0]} / V{counts[1]} / E{counts[2]} / P{counts[3]} / X{counts[4]}) |

---

## Purpose

Define testable acceptance criteria for **{f['id']}** covering happy paths, validation, errors, permissions, and edge cases. Use for UAT, QA test design, and Definition of Done.

**ID legend:** `FAC-{{nn}}-{{H|V|E|P|X}}{{n}}` — Feature Acceptance Criteria; H=Happy, V=Validation, E=Error, P=Permission, X=Edge.

---

{render_section("1. Happy Scenarios", f["happy"])}
{render_section("2. Validation Scenarios", f["validation"])}
{render_section("3. Error Scenarios", f["errors"])}
{render_section("4. Permission Scenarios", f["permissions"])}
{render_section("5. Edge Cases", f["edges"])}

## Traceability

| Link | Reference |
|------|-----------|
| User stories | {stories} |
| Story-level AC | `project_businsse/acceptance-criteria-reviewed.md` |
| Implementation plan | `implmention/plans/{f['id']}-*.md` |
| Feature catalog | `implmention/IMS-Implementation-Features.md` |

## Feature DoD (QA gate)

- [ ] All Happy criteria passed in UAT or automated suite
- [ ] Validation + Error criteria covered by API and/or UI tests
- [ ] Permission criteria verified with at least two roles (allowed + denied)
- [ ] Edge cases reviewed; deferred edges explicitly waived with PO sign-off
- [ ] No open Sev-1/Sev-2 defects for this feature

---

*Product Owner & QA Lead — {f['id']}*
"""


def main():
    rows = []
    total_ac = 0
    for f in FEATURES:
        fname = f"{f['id']}-Acceptance-Criteria.md"
        text = render_feature(f)
        (OUT / fname).write_text(text, encoding="utf-8")
        n = sum(len(f[k]) for k in ("happy","validation","errors","permissions","edges"))
        total_ac += n
        rows.append(f"| {f['id']} | {f['name']} | {', '.join(f['stories'])} | {n} | [{fname}](./{fname}) |")
        print("wrote", fname, n)

    index = f"""# Feature Acceptance Criteria — Index

| Attribute | Detail |
|-----------|--------|
| **Document ID** | IMPL-AC-000 |
| **Perspective** | Product Owner & QA Lead |
| **Date** | July 11, 2026 |
| **Format** | Given / When / Then |
| **Features covered** | {len(FEATURES)} (F-01–F-30) |
| **Total criteria** | {total_ac} |

## Categories (every feature)

| Category | Prefix | Purpose |
|----------|--------|---------|
| Happy | H | Successful business outcomes |
| Validation | V | Required fields, formats, business-rule checks before commit |
| Error | E | Failures, conflicts, unavailable dependencies |
| Permission | P | AuthN/AuthZ, RBAC, location scope, SoD |
| Edge | X | Boundaries, concurrency, phase splits, unusual valid cases |

## Criteria by feature

| ID | Feature | Stories | # AC | Document |
|----|---------|---------|------|----------|
{chr(10).join(rows)}

## How QA should use these

1. Map each `FAC-*` to test cases (API + UI + UAT scripts).
2. Prefer automating **V**, **E**, and **P** at API layer; **H** and key **P/X** in UI/E2E.
3. Story-level detail remains in `project_businsse/acceptance-criteria-reviewed.md` — feature AC is the **release gate** view.
4. Sign off feature DoD checklist at bottom of each file before marking F-xx Done.

## Related documents

- [IMS-Implementation-Features.md](../IMS-Implementation-Features.md)
- [IMS-Feature-Dependency-Map.md](../IMS-Feature-Dependency-Map.md)
- [plans/README.md](../plans/README.md)
"""
    (OUT / "README.md").write_text(index, encoding="utf-8")
    print("TOTAL", len(FEATURES), "features", total_ac, "criteria")


if __name__ == "__main__":
    main()
