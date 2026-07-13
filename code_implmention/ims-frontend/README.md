# IMS Frontend - Inventory Management System

Angular 19 standalone application for the Inventory Management System, built from the approved SRS screen inventory (UI-001 to UI-050) and component inventory (C-001 to C-060).

## Architecture

```
src/app/
├── core/           # Auth, guards, shell layout, mock data
├── shared/ui/      # 60 reusable components (layout, forms, tables, workflow, etc.)
└── features/       # 50 screen pages by business domain
    ├── auth/
    ├── home/
    ├── notifications/
    ├── products/
    ├── locations/
    ├── governance/
    ├── procurement/
    ├── inbound/
    ├── inventory/
    ├── fulfillment/
    ├── transfers/
    ├── returns/
    ├── reports/
    └── administration/
```

## Quick Start

Requires the Sprint 1 backend running on `http://localhost:8080` (see `ims-backend/README.md`).

```bash
cd ims-frontend
npm install
npm start
```

Open http://localhost:4200

### Login (wired to backend)

| Email | Password |
|-------|----------|
| admin@ims.local | demo |
| warehouse@ims.local | demo |

Auth uses `POST /api/v1/auth/token`, stores the JWT in `sessionStorage`, and attaches `Authorization: Bearer` via interceptor.

## Scripts

| Command | Description |
|---------|-------------|
| `npm start` | Dev server |
| `npm run build` | Production build |
| `npm test` | Unit tests |

## Mock Data

Business screens still use `MockDataService` for non-auth data. Auth (UI-001) is wired to the real backend.

## Regenerate Scaffolding

```bash
node scripts/scaffold-ims.mjs
```
