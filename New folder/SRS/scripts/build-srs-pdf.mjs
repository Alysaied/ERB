import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { marked } from 'marked';
import puppeteer from 'puppeteer';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const SRS_ROOT = path.resolve(__dirname, '..');
const OUTPUT_MD = path.join(SRS_ROOT, 'Inventory-Management-System-SRS.md');
const OUTPUT_PDF = path.join(SRS_ROOT, 'Inventory-Management-System-SRS.pdf');

const SECTIONS = [
  {
    part: 'Part I — Introduction & System Context',
    files: [
      'System Architecture/Architecture-Vision.md',
      'System Architecture/System-Context.md',
      'System Architecture/Architecture-Style-Recommendation.md',
    ],
  },
  {
    part: 'Part II — Business Rules & Constraints',
    files: [
      'business_rules/Business-Rules.md',
      'business_rules/Validation-Rules.md',
      'business_rules/Business-Constraints.md',
      'business_rules/Business-Exception-Scenarios.md',
      'business_rules/Business-Process-Decision-Tables.md',
      'business_rules/Business-Rule-Dependencies.md',
    ],
  },
  {
    part: 'Part III — Use Cases',
    files: [
      'use_cases/Use-Case-Catalog.md',
      'use_cases/Use-Case-Main-Flows.md',
      'use_cases/Use-Case-Alternate-Flows.md',
      'use_cases/Use-Case-Exception-Flows.md',
      'use_cases/Use-Case-Preconditions-Postconditions.md',
    ],
  },
  {
    part: 'Part IV — Domain Model',
    files: [
      'domain_model/Ubiquitous-Language.md',
      'domain_model/Bounded-Contexts.md',
      'domain_model/Domain-Entities.md',
      'domain_model/Value-Objects.md',
      'domain_model/Domain-Aggregates.md',
      'domain_model/Domain-Entity-Relationships.md',
      'domain_model/Domain-Services.md',
      'domain_model/Domain-Events.md',
    ],
  },
  {
    part: 'Part V — Event Storming',
    files: [
      'event_storming/Actors-and-External-Systems.md',
      'event_storming/Domain-Commands.md',
      'event_storming/Domain-Events.md',
      'event_storming/Domain-Policies.md',
      'event_storming/Read-Models.md',
      'event_storming/Event-Storming-Board.md',
      'event_storming/Event-Storming-Hotspots.md',
    ],
  },
  {
    part: 'Part VI — System Architecture',
    files: [
      'System Architecture/System-Modules-Design.md',
      'System Architecture/Layered-Architecture-Design.md',
      'System Architecture/Integration-Architecture-Design.md',
      'System Architecture/Cross-Cutting-Concerns.md',
      'System Architecture/Technology-Stack-Recommendation.md',
      'System Architecture/Architecture-Decision-Records.md',
    ],
  },
  {
    part: 'Part VII — Database Design',
    files: [
      'database_design/Logical-Data-Model-ERD.md',
      'database_design/Physical-Data-Model.md',
      'database_design/Data-Dictionary.md',
      'database_design/Database-Keys.md',
      'database_design/Database-Constraints.md',
      'database_design/Database-Indexing-Strategy.md',
      'database_design/Database-Audit-Strategy.md',
      'database_design/Database-Naming-Conventions.md',
    ],
  },
  {
    part: 'Part VIII — API Design',
    files: [
      'API_Design/REST-API-Catalog.md',
      'API_Design/Complete-API-Specification.md',
      'API_Design/Complete-API-Specification-Part2.md',
      'API_Design/Complete-API-Specification-Part3.md',
      'API_Design/Request-DTOs.md',
      'API_Design/Response-DTOs.md',
      'API_Design/Request-DTO-Validation-Spec.md',
      'API_Design/Error-Response-Specification.md',
      'API_Design/API-Authorization-Specification.md',
      'API_Design/API-Versioning-Strategy.md',
      'API_Design/Collection-API-Strategy.md',
    ],
  },
  {
    part: 'Part IX — UI/UX Specification',
    files: [
      'UI_UX/IMS-Screen-Inventory.md',
      'UI_UX/IMS-Component-Inventory.md',
      'UI_UX/IMS-Navigation-Structure.md',
      'UI_UX/IMS-User-Journeys.md',
      'UI_UX/IMS-User-Flows.md',
      'UI_UX/IMS-Low-Fidelity-Wireframe-Specifications.md',
      'UI_UX/IMS-Form-Specifications-and-Validation.md',
      'UI_UX/IMS-Screen-State-Specifications.md',
      'UI_UX/IMS-UI-Guidelines-WCAG.md',
      'UI Specification/UI Specification.md',
      'UI Specification/Inventory-Management-System-Design-System.md',
    ],
  },
  {
    part: 'Part X — Frontend Architecture',
    files: ['Frontend Architecture/Frontend-Architecture-Mapping.md'],
  },
];

const COVER = `# Software Requirements Specification (SRS)
## Inventory Management System (IMS)

---

| Attribute | Detail |
|-----------|--------|
| **Document ID** | SRS-IMS-MASTER-001 |
| **Version** | 1.0 |
| **Status** | Draft — Consolidated Master Specification |
| **Date** | July 7, 2026 |
| **Classification** | Internal |
| **Prepared For** | Product owners, business analysts, architects, developers, QA, auditors |

---

## Document Purpose

This master Software Requirements Specification consolidates the complete IMS requirements package into a single authoritative document. It covers business rules, use cases, domain model, system architecture, database design, REST API specifications, UI/UX specifications, and frontend architecture mapping.

## Scope

The Inventory Management System is an enterprise web application providing authoritative inventory truth across a multi-location network — covering product master data, procurement, inbound receiving, inventory control, order fulfillment, transfers, returns, reporting, governance, and administration.

## Delivery Phasing

| Phase | Timeline | Focus |
|-------|----------|-------|
| **MVP (Phase 1)** | Months 0–6 | Core visibility, movement recording, fulfillment support, audit |
| **Phase 2** | Months 6–12 | Network maturity, procurement automation, commercial campaigns |
| **Phase 3** | Months 12–18 | Finance alignment, executive analytics, advanced integrations |

## Package Contents

| Part | Content |
|------|---------|
| I | Introduction & System Context |
| II | Business Rules & Constraints |
| III | Use Cases (48 use cases) |
| IV | Domain Model (13 bounded contexts) |
| V | Event Storming |
| VI | System Architecture |
| VII | Database Design |
| VIII | API Design (174 REST endpoints) |
| IX | UI/UX Specification (50 screens, 60 components) |
| X | Frontend Architecture |

## Traceability Summary

| Artifact | Count |
|----------|-------|
| Business Rules | 32 |
| Use Cases | 48 |
| Bounded Contexts | 13 |
| Domain Events | 81 |
| REST APIs | 174 |
| UI Screens | UI-001 to UI-050 |
| UI Components | C-001 to C-060 |
| User Roles | 19 |

---

<div class="page-break"></div>

`;

function readSectionFile(relativePath) {
  const fullPath = path.join(SRS_ROOT, relativePath);
  if (!fs.existsSync(fullPath)) {
    console.warn(`Warning: missing file ${relativePath}`);
    return `> **Missing source file:** \`${relativePath}\`\n\n`;
  }
  return fs.readFileSync(fullPath, 'utf8').trim() + '\n\n';
}

function buildMarkdown() {
  const parts = [COVER];

  for (const section of SECTIONS) {
    parts.push(`# ${section.part}\n\n`);
    parts.push('<div class="page-break"></div>\n\n');
    for (const file of section.files) {
      parts.push(readSectionFile(file));
      parts.push('<div class="section-break"></div>\n\n');
    }
  }

  return parts.join('');
}

const HTML_TEMPLATE = (body, toc) => `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Inventory Management System — SRS</title>
  <style>
    @page {
      size: A4;
      margin: 18mm 16mm 22mm 16mm;
    }
    * { box-sizing: border-box; }
    body {
      font-family: "Segoe UI", Inter, Arial, sans-serif;
      font-size: 10.5pt;
      line-height: 1.45;
      color: #111827;
      margin: 0;
      padding: 0;
    }
    h1 {
      font-size: 20pt;
      color: #0F2A43;
      border-bottom: 2px solid #1D4E89;
      padding-bottom: 0.3em;
      margin-top: 1.2em;
      page-break-after: avoid;
    }
    h2 {
      font-size: 14pt;
      color: #1D4E89;
      margin-top: 1.1em;
      page-break-after: avoid;
    }
    h3 {
      font-size: 12pt;
      color: #2563A6;
      margin-top: 0.9em;
      page-break-after: avoid;
    }
    h4, h5, h6 {
      font-size: 11pt;
      color: #374151;
      page-break-after: avoid;
    }
    p, li { orphans: 3; widows: 3; }
    table {
      width: 100%;
      border-collapse: collapse;
      margin: 0.8em 0;
      font-size: 9pt;
      page-break-inside: auto;
    }
    th, td {
      border: 1px solid #D1D5DB;
      padding: 5px 7px;
      text-align: left;
      vertical-align: top;
    }
    th {
      background: #F3F4F6;
      font-weight: 600;
    }
    tr { page-break-inside: avoid; }
    code, pre {
      font-family: Consolas, "Courier New", monospace;
      font-size: 8.5pt;
      background: #F9FAFB;
    }
    pre {
      border: 1px solid #E5E7EB;
      border-radius: 4px;
      padding: 8px 10px;
      overflow-wrap: anywhere;
      white-space: pre-wrap;
      page-break-inside: avoid;
    }
    hr {
      border: none;
      border-top: 1px solid #E5E7EB;
      margin: 1.2em 0;
    }
    blockquote {
      border-left: 3px solid #93C5FD;
      margin: 0.8em 0;
      padding: 0.2em 0 0.2em 0.9em;
      color: #4B5563;
    }
    ul, ol { padding-left: 1.4em; }
    .cover-title {
      text-align: center;
      padding: 48px 0 24px;
    }
    .cover-title h1 {
      border: none;
      font-size: 28pt;
      margin-bottom: 0.2em;
    }
    .cover-title h2 {
      font-size: 16pt;
      font-weight: 500;
      color: #4B5563;
      border: none;
    }
    .toc {
      page-break-after: always;
    }
    .toc h2 { margin-top: 0; }
    .toc ul {
      list-style: none;
      padding-left: 0;
    }
    .toc li {
      margin: 0.25em 0;
      font-size: 10pt;
    }
    .toc .level-2 { padding-left: 1.2em; }
    .page-break { page-break-before: always; }
    .section-break { height: 0; }
  </style>
</head>
<body>
  <div class="cover-title">
    <h1>Software Requirements Specification</h1>
    <h2>Inventory Management System (IMS)</h2>
    <p><strong>Version 1.0</strong> &nbsp;|&nbsp; July 7, 2026 &nbsp;|&nbsp; SRS-IMS-MASTER-001</p>
  </div>
  <div class="toc">
    <h2>Table of Contents</h2>
    ${toc}
  </div>
  ${body}
</body>
</html>`;

function buildToc(markdown) {
  const lines = markdown.split('\n');
  const items = [];
  for (const line of lines) {
    const h1 = line.match(/^# (.+)/);
    const h2 = line.match(/^## (.+)/);
    if (h1 && !h1[1].startsWith('Software Requirements Specification')) {
      items.push(`<li><strong>${escapeHtml(h1[1])}</strong></li>`);
    } else if (h2 && !h2[1].startsWith('Document ')) {
      items.push(`<li class="level-2">${escapeHtml(h2[1])}</li>`);
    }
  }
  return `<ul>${items.slice(0, 120).join('')}</ul>`;
}

function escapeHtml(text) {
  return text
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;');
}

async function generatePdf() {
  console.log('Building consolidated SRS markdown...');
  const markdown = buildMarkdown();
  fs.writeFileSync(OUTPUT_MD, markdown, 'utf8');
  console.log(`Written: ${OUTPUT_MD}`);
  console.log(`Markdown size: ${(markdown.length / 1024 / 1024).toFixed(2)} MB`);

  marked.setOptions({ gfm: true, breaks: false });
  const htmlBody = marked.parse(markdown.replace(/<div class="page-break"><\/div>/g, '\n\n---\n\n'));
  const toc = buildToc(markdown);
  const html = HTML_TEMPLATE(htmlBody, toc);
  const htmlPath = path.join(SRS_ROOT, 'Inventory-Management-System-SRS.html');
  fs.writeFileSync(htmlPath, html, 'utf8');
  console.log(`Written: ${htmlPath}`);

  console.log('Launching headless browser for PDF generation...');
  const browser = await puppeteer.launch({
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage'],
  });

  try {
    const page = await browser.newPage();
    page.setDefaultNavigationTimeout(600000);
    page.setDefaultTimeout(600000);

    const fileUrl = `file:///${htmlPath.replace(/\\/g, '/')}`;
    await page.goto(fileUrl, { waitUntil: 'domcontentloaded', timeout: 600000 });
    await page.evaluate(() => document.fonts?.ready);
    await page.pdf({
      path: OUTPUT_PDF,
      format: 'A4',
      printBackground: true,
      margin: { top: '18mm', right: '16mm', bottom: '22mm', left: '16mm' },
      displayHeaderFooter: true,
      headerTemplate: '<div></div>',
      footerTemplate: `
        <div style="width:100%;font-size:8px;color:#6B7280;padding:0 16mm;display:flex;justify-content:space-between;">
          <span>Inventory Management System — SRS v1.0</span>
          <span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span>
        </div>`,
      timeout: 600000,
    });
    console.log(`PDF generated: ${OUTPUT_PDF}`);
    const stats = fs.statSync(OUTPUT_PDF);
    console.log(`PDF size: ${(stats.size / 1024 / 1024).toFixed(2)} MB`);
  } finally {
    await browser.close();
  }
}

generatePdf().catch((err) => {
  console.error('PDF generation failed:', err);
  process.exit(1);
});
