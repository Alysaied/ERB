# IMS Implementation Checklists

| Attribute | Detail |
|-----------|--------|
| **Document ID** | IMPL-CHK-INDEX |
| **Perspective** | Technical Lead |
| **Date** | July 11, 2026 |
| **Location** | `implmention/checklists/` |

## Deliverable

Every feature **F-01–F-30** converted into an implementation checklist.

Each checklist item includes:

1. **Task ID** — `CHK-{nn}-{DB|BE|FE|TE|DO}-{seq}`
2. **Feature** — F-xx
3. **Task description**
4. **Layer** — Database | Backend | Frontend | Testing | Documentation
5. **Priority** — P0–P3
6. **Status** — baseline **Not Started**
7. **Dependencies** — feature and/or task IDs

**Total tasks:** 288

## Start here

| File | Purpose |
|------|---------|
| [checklists/README.md](checklists/README.md) | Per-feature index |
| [checklists/IMS-Consolidated-Implementation-Checklist.md](checklists/IMS-Consolidated-Implementation-Checklist.md) | All 288 tasks in one table |
| Example: [checklists/F-01-Implementation-Checklist.md](checklists/F-01-Implementation-Checklist.md) | Product catalog checklist |

## Priority legend

| Code | Meaning |
|------|---------|
| P0 | MVP critical / blocking |
| P1 | MVP important |
| P2 | Phase 2 Should Have |
| P3 | Phase 3 / deferred |

Work order within a feature: **Database → Backend → Frontend → Testing → Documentation**.
