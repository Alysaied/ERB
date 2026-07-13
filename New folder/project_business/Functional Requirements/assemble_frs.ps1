$base = "D:\precatice\Inventory Management System\Functional Requirements"
$out = Join-Path $base "functional-requirements-specification.md"

function Get-BodyAfterHeader {
    param([string]$Path)
    $lines = Get-Content -Path $Path -Encoding UTF8
    $start = 0
    for ($i = 0; $i -lt $lines.Count; $i++) {
        if ($lines[$i] -eq '---' -and $i -gt 0) {
            $start = $i + 1
            break
        }
    }
    if ($start -eq 0) {
        for ($i = 0; $i -lt $lines.Count; $i++) {
            if ($lines[$i] -like '## *') {
                $start = $i
                break
            }
        }
    }
    return $lines[$start..($lines.Count - 1)]
}

$header = @'
# Functional Requirements Specification (FRS)
## Inventory Management System

| Attribute | Detail |
|-----------|--------|
| **Document ID** | FRS-IMS-001 |
| **Version** | 1.0 |
| **Status** | For Stakeholder Review |
| **Document Owner** | Senior Business Analyst |
| **Prepared For** | Business stakeholders, product owners, delivery planners, QA |
| **Date** | July 3, 2026 |
| **Scope** | Functional and business behavior only - no technical design, architecture, or implementation |

---

## Document Purpose

This Functional Requirements Specification consolidates all Requirements Definition phase deliverables into a single authoritative document for stakeholder review and delivery planning. It defines **what** the Inventory Management System must do from a business perspective.

**Source phases:** Business Discovery, Domain Analysis, Domain Knowledge, Requirements Definition.

---

## Table of Contents

1. [Introduction](#part-0-introduction)
2. [Feature Catalog](#part-1-feature-catalog)
3. [Functional Requirements](#part-2-functional-requirements)
4. [User Stories](#part-3-user-stories)
5. [Acceptance Criteria](#part-4-acceptance-criteria)
6. [Requirement Priorities](#part-5-requirement-priorities)
7. [Requirement Dependencies](#part-6-requirement-dependencies)
8. [Appendices](#appendices)

---

## Specification Summary

| Artifact | Count | Identifier Range |
|----------|-------|------------------|
| Features | 30 | F-01 to F-30 |
| Functional Requirements | 90 | FR-001 to FR-090 |
| User Stories | 90 | US-001 to US-090 |
| Acceptance Criteria | 360+ | AC-{Story}-{Category}{Seq} |
| Dependency Relationships | 185 | DEP-001 to DEP-185 |
| Business Processes (traceability) | 32 | BP-01 to BP-32 |

### MoSCoW Distribution

| Priority | Count | Percentage |
|----------|-------|------------|
| Must Have | 55 | 61% |
| Should Have | 26 | 29% |
| Could Have | 6 | 7% |
| Won't Have (Current Release) | 3 | 3% |

### Foundational Requirements

- **FR-001** - Product master
- **FR-005** - Location master
- **FR-011** - Reason codes
- **FR-081** - Access control

---

# Part 0: Introduction

## Scope

This specification covers inventory management capabilities for a multi-location distribution and retail organization, including master data, inbound logistics, visibility, control, fulfillment, replenishment, transfers, returns, reporting, notifications, access control, and governance.

## Out of Scope

Per project scope, this specification excludes: ERP/finance modules, CRM, manufacturing/MRP, transportation management, 3PL/VMI portals, AI forecasting, marketplace integrations, and dedicated regulatory compliance modules.

## Conventions

| Convention | Meaning |
|------------|---------|
| **F-xx** | Feature identifier |
| **FR-xxx** | Functional requirement identifier |
| **US-xxx** | User story identifier |
| **AC-xxx** | Acceptance criterion identifier |
| **BP-xx** | Business process |
| **DEP-xxx** | Dependency relationship identifier |

## Traceability Model

Business Process (BP) -> Feature (F) -> Functional Requirement (FR) -> User Story (US) -> Acceptance Criteria (AC), with MoSCoW Priority and Dependency (DEP).

---

'@

$parts = @(
    @{ Title = 'Part 1: Feature Catalog'; File = 'feature-catalog.md' },
    @{ Title = 'Part 2: Functional Requirements'; File = 'functional-requirements.md' },
    @{ Title = 'Part 3: User Stories'; File = 'user-stories.md' },
    @{ Title = 'Part 4: Acceptance Criteria'; File = 'acceptance-criteria.md' },
    @{ Title = 'Part 5: Requirement Priorities'; File = 'moscow-prioritization.md' },
    @{ Title = 'Part 6: Requirement Dependencies'; File = 'requirements-dependency-analysis.md' }
)

$appendix = Get-Content (Join-Path $base 'frs-appendix.md') -Raw -Encoding UTF8

$sb = New-Object System.Text.StringBuilder
[void]$sb.Append($header)

foreach ($part in $parts) {
    [void]$sb.Append("`n---`n`n# $($part.Title)`n`n")
    $body = Get-BodyAfterHeader (Join-Path $base $part.File)
    [void]$sb.Append(($body -join "`n"))
    [void]$sb.Append("`n")
}

[void]$sb.Append($appendix)

[System.IO.File]::WriteAllText($out, $sb.ToString(), [System.Text.UTF8Encoding]::new($true))

$info = Get-Item $out
$lineCount = (Get-Content $out | Measure-Object -Line).Lines
Write-Output "Created: $($info.FullName)"
Write-Output "Lines: $lineCount"
Write-Output "Size: $($info.Length) bytes"
