import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";
import { marked } from "marked";
import puppeteer from "puppeteer-core";

const __dirname = path.dirname(fileURLToPath(import.meta.url));

const FILES = [
  "Business-Requirements-Document.md",
  "Requirements-Traceability-Matrix.md",
  "BRD-Review-Report.md",
  "BRD-Approval-Checklist.md",
];

const CHROME_PATHS = [
  "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
  "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe",
  "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe",
];

function findBrowser() {
  for (const p of CHROME_PATHS) {
    if (fs.existsSync(p)) return p;
  }
  throw new Error("Chrome or Edge not found");
}

function mergeMarkdown() {
  const parts = FILES.map((file, i) => {
    const content = fs.readFileSync(path.join(__dirname, file), "utf8");
    const separator =
      i === 0
        ? ""
        : "\n\n<div style=\"page-break-before: always;\"></div>\n\n";
    return separator + content;
  });
  return parts.join("\n");
}

const CSS = `
  @page { margin: 20mm 15mm; size: A4; }
  body {
    font-family: "Segoe UI", Calibri, Arial, sans-serif;
    font-size: 10pt;
    line-height: 1.45;
    color: #1a1a1a;
    max-width: 100%;
  }
  h1 { font-size: 20pt; color: #1e3a5f; border-bottom: 2px solid #1e3a5f; padding-bottom: 6px; margin-top: 24px; page-break-after: avoid; }
  h2 { font-size: 14pt; color: #2c5282; margin-top: 20px; page-break-after: avoid; }
  h3 { font-size: 12pt; color: #2d3748; margin-top: 16px; page-break-after: avoid; }
  h4 { font-size: 11pt; page-break-after: avoid; }
  table { border-collapse: collapse; width: 100%; margin: 12px 0; font-size: 9pt; page-break-inside: auto; }
  th, td { border: 1px solid #cbd5e0; padding: 5px 8px; text-align: left; vertical-align: top; }
  th { background: #edf2f7; font-weight: 600; }
  tr { page-break-inside: avoid; page-break-after: auto; }
  hr { border: none; border-top: 1px solid #e2e8f0; margin: 20px 0; }
  code { background: #f7fafc; padding: 1px 4px; border-radius: 3px; font-size: 9pt; }
  pre { background: #f7fafc; padding: 10px; border-radius: 4px; overflow-x: auto; font-size: 9pt; }
  blockquote { border-left: 3px solid #4299e1; margin: 12px 0; padding: 4px 12px; color: #4a5568; }
  ul, ol { margin: 8px 0; padding-left: 24px; }
  li { margin: 3px 0; }
  strong { color: #1a202c; }
`;

async function main() {
  const md = mergeMarkdown();
  const htmlBody = marked.parse(md, { gfm: true, breaks: false });
  const html = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>BRD Package — Inventory Management System</title>
  <style>${CSS}</style>
</head>
<body>${htmlBody}</body>
</html>`;

  const htmlPath = path.join(__dirname, "_merged-brd.html");
  fs.writeFileSync(htmlPath, html, "utf8");

  const browser = await puppeteer.launch({
    executablePath: findBrowser(),
    headless: true,
    args: ["--no-sandbox", "--disable-setuid-sandbox"],
  });

  const page = await browser.newPage();
  await page.goto(`file:///${htmlPath.replace(/\\/g, "/")}`, {
    waitUntil: "networkidle0",
  });

  const pdfPath = path.join(__dirname, "BRD-IMS-Complete-Package.pdf");
  await page.pdf({
    path: pdfPath,
    format: "A4",
    printBackground: true,
    margin: { top: "20mm", bottom: "20mm", left: "15mm", right: "15mm" },
    displayHeaderFooter: true,
    headerTemplate: "<span></span>",
    footerTemplate:
      '<div style="width:100%;font-size:8pt;text-align:center;color:#718096;padding:0 15mm;"><span class="pageNumber"></span> / <span class="totalPages"></span></div>',
  });

  await browser.close();
  fs.unlinkSync(htmlPath);

  const stats = fs.statSync(pdfPath);
  console.log(`PDF created: ${pdfPath}`);
  console.log(`Size: ${(stats.size / 1024 / 1024).toFixed(2)} MB`);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
