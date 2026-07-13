# Feature Acceptance Criteria (PO + QA Lead)

| Attribute | Detail |
|-----------|--------|
| **Document ID** | IMPL-AC-INDEX |
| **Perspective** | Product Owner & QA Lead |
| **Date** | July 11, 2026 |
| **Location** | `implmention/acceptance-criteria/` |

## Deliverable

**Given / When / Then** acceptance criteria for all **30 implementation features (F-01–F-30)**.

Each feature file includes:

| Category | Purpose |
|----------|---------|
| Happy scenarios | Successful business outcomes |
| Validation scenarios | Required fields, formats, rule checks |
| Error scenarios | Failures, conflicts, unavailable services |
| Permission scenarios | AuthN/AuthZ, RBAC, location scope, SoD |
| Edge cases | Boundaries, concurrency, phase splits |

**Total criteria:** 429 across 30 features.

## Start here

- Index: [`acceptance-criteria/README.md`](acceptance-criteria/README.md)
- Example: [`acceptance-criteria/F-01-Acceptance-Criteria.md`](acceptance-criteria/F-01-Acceptance-Criteria.md)
- Story-level AC (detail): `project_businsse/acceptance-criteria-reviewed.md`

## ID format

`FAC-{feature#}-{H|V|E|P|X}{n}`

Example: `FAC-01-H1`, `FAC-08-P2`, `FAC-27-E1`
