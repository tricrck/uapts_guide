# Funding Allocations

_Road Infrastructure › Funding Allocations_ · Route `/infrastructure/funding`

**Funding Allocations** lets you see budget allocations, disbursements, absorption, and variance analytics per agency and fiscal year. Data on this page comes from KeNHA, KURA, KeRRA, KRB, LAPSSET and National Treasury.

> 🎬 **Video tutorial:** _coming soon._  
> <!-- VIDEO-URL: infrastructure/funding-allocations | paste the link here, e.g. [Watch the walkthrough](https://…) -->

## Highlights

- **8 headline tiles** — Total Allocated, Disbursed, Committed, Balance, Absorption Rate, Allocation / km….
- **5 panels** — Allocation vs. Condition Need, Disbursement vs. Physical Progress, Low Disbursement (), Over / Under-Utilized Allocations, Contractor / Project Funding Risk.
- **Refreshes itself every 120 seconds**, so you do not need to reload the page.
- **Export to CSV** for the rows you are looking at (Analyst tier and above).
- Every figure is traceable to the data feed or upload template that supplies it — see [Data sources and feeds](#data-sources-and-feeds).

## Enabling and access

1. Sign in to UAPTS (see [How to access](../getting-started/how-to-access.md)).
2. In the left sidebar expand **Road Infrastructure** and click **Funding Allocations**.
3. The page opens at `/infrastructure/funding`. You can also reach it with the global search (**Ctrl + K**).

This page belongs to module **M06 · Road Infrastructure**. The route needs at least the **Analyst** tier to open it. The sidebar and the global search only list pages your agency and role can open, and a link to a page you cannot reach sends you back to the Command Centre. If a page you expect is missing, ask your agency administrator to check your agency's [Module Access](../access-control/module-access.md).

![Funding Allocations page](../assets/screenshots/infrastructure-funding.webp)

## Page tour

### Headline tiles

![Funding Allocations headline tiles](../assets/screenshots/infrastructure-funding--kpis.webp)

| Tile | What it shows | Data from | Table → ingested via |
|---|---|---|---|
| **Total Allocated** | — _(window: LIVE)_ | `/infrastructure/maintenance-budgets/`, `/infrastructure/road-segments/`, `/infrastructure/summary/` | _MaintenanceBudget, RoadSegment_ → [`krb-funding`](../data-templates/krb-funding.xlsx)<br>[`krb-road-condition`](../data-templates/krb-road-condition.xlsx)<br>[`kura-road-network`](../data-templates/kura-road-network.xlsx)<br>[`kenha-road-network`](../data-templates/kenha-road-network.xlsx)<br>+2 more |
| **Disbursed** | — _(window: LIVE)_ | `/infrastructure/maintenance-budgets/`, `/infrastructure/road-segments/`, `/infrastructure/summary/` | _MaintenanceBudget, RoadSegment_ → [`krb-funding`](../data-templates/krb-funding.xlsx)<br>[`krb-road-condition`](../data-templates/krb-road-condition.xlsx)<br>[`kura-road-network`](../data-templates/kura-road-network.xlsx)<br>[`kenha-road-network`](../data-templates/kenha-road-network.xlsx)<br>+2 more |
| **Committed** | Contractually obligated _(window: LIVE)_ | `/infrastructure/maintenance-budgets/`, `/infrastructure/road-segments/`, `/infrastructure/summary/` | _MaintenanceBudget, RoadSegment_ → [`krb-funding`](../data-templates/krb-funding.xlsx)<br>[`krb-road-condition`](../data-templates/krb-road-condition.xlsx)<br>[`kura-road-network`](../data-templates/kura-road-network.xlsx)<br>[`kenha-road-network`](../data-templates/kenha-road-network.xlsx)<br>+2 more |
| **Balance** | Allocated minus disbursed _(window: LIVE)_ | `/infrastructure/maintenance-budgets/`, `/infrastructure/road-segments/`, `/infrastructure/summary/` | _MaintenanceBudget, RoadSegment_ → [`krb-funding`](../data-templates/krb-funding.xlsx)<br>[`krb-road-condition`](../data-templates/krb-road-condition.xlsx)<br>[`kura-road-network`](../data-templates/kura-road-network.xlsx)<br>[`kenha-road-network`](../data-templates/kenha-road-network.xlsx)<br>+2 more |
| **Absorption Rate** | Disbursed / allocated _(window: LIVE)_ | `/infrastructure/maintenance-budgets/`, `/infrastructure/road-segments/`, `/infrastructure/summary/` | _MaintenanceBudget, RoadSegment_ → [`krb-funding`](../data-templates/krb-funding.xlsx)<br>[`krb-road-condition`](../data-templates/krb-road-condition.xlsx)<br>[`kura-road-network`](../data-templates/kura-road-network.xlsx)<br>[`kenha-road-network`](../data-templates/kenha-road-network.xlsx)<br>+2 more |
| **Allocation / km** | — _(window: LIVE)_ | `/infrastructure/maintenance-budgets/`, `/infrastructure/road-segments/`, `/infrastructure/summary/` | _MaintenanceBudget, RoadSegment_ → [`krb-funding`](../data-templates/krb-funding.xlsx)<br>[`krb-road-condition`](../data-templates/krb-road-condition.xlsx)<br>[`kura-road-network`](../data-templates/kura-road-network.xlsx)<br>[`kenha-road-network`](../data-templates/kenha-road-network.xlsx)<br>+2 more |
| **AI-Flagged Critical Needs** | At-risk segments (12mo) - proxy for unfunded need _(window: 12MO)_ | `/infrastructure/deterioration-forecasts/at-risk/`, `/infrastructure/road-segments/` | _DeteriorationForecast, RoadSegment_ → [`krb-road-condition`](../data-templates/krb-road-condition.xlsx)<br>[`kura-road-network`](../data-templates/kura-road-network.xlsx)<br>[`kenha-road-network`](../data-templates/kenha-road-network.xlsx)<br>[`kerra-road-network`](../data-templates/kerra-road-network.xlsx)<br>+1 more |
| **Avg Utilization** | — _(window: LIVE)_ | `/infrastructure/maintenance-budgets/`, `/infrastructure/road-segments/`, `/infrastructure/summary/` | _MaintenanceBudget, RoadSegment_ → [`krb-funding`](../data-templates/krb-funding.xlsx)<br>[`krb-road-condition`](../data-templates/krb-road-condition.xlsx)<br>[`kura-road-network`](../data-templates/kura-road-network.xlsx)<br>[`kenha-road-network`](../data-templates/kenha-road-network.xlsx)<br>+2 more |

### Allocation vs. Condition Need

![Allocation vs. Condition Need](../assets/screenshots/infrastructure-funding--allocation-vs-condition-need.webp)

**Data from:** `/infrastructure/maintenance-budgets/`, `/infrastructure/road-segments/`  
**Table → ingested via:** _MaintenanceBudget, RoadSegment_ → [`krb-funding`](../data-templates/krb-funding.xlsx)<br>[`krb-road-condition`](../data-templates/krb-road-condition.xlsx)<br>[`kura-road-network`](../data-templates/kura-road-network.xlsx)<br>[`kenha-road-network`](../data-templates/kenha-road-network.xlsx)<br>+2 more

### Disbursement vs. Physical Progress

![Disbursement vs. Physical Progress](../assets/screenshots/infrastructure-funding--disbursement-vs-physical-progress.webp)

**Data from:** `/infrastructure/construction-projects/`, `/infrastructure/maintenance-budgets/`  
**Table → ingested via:** _ConstructionProject, MaintenanceBudget_ → [`krb-funding`](../data-templates/krb-funding.xlsx)<br>[`krb-workplans`](../data-templates/krb-workplans.xlsx)<br>[`kura-project-progress`](../data-templates/kura-project-progress.xlsx)<br>[`kenha-project-progress`](../data-templates/kenha-project-progress.xlsx)<br>+4 more

### Low Disbursement ()


**Data from:** `/infrastructure/maintenance-budgets/`  
**Table → ingested via:** _MaintenanceBudget_ → [`krb-funding`](../data-templates/krb-funding.xlsx)

### Over / Under-Utilized Allocations

![Over / Under-Utilized Allocations](../assets/screenshots/infrastructure-funding--over-under-utilized-allocations.webp)

**Data from:** `/infrastructure/maintenance-budgets/`  
**Table → ingested via:** _MaintenanceBudget_ → [`krb-funding`](../data-templates/krb-funding.xlsx)

### Contractor / Project Funding Risk

![Contractor / Project Funding Risk](../assets/screenshots/infrastructure-funding--contractor-project-funding-risk.webp)

**Data from:** `/infrastructure/construction-projects/`  
**Table → ingested via:** _ConstructionProject_ → [`krb-workplans`](../data-templates/krb-workplans.xlsx)<br>[`kura-project-progress`](../data-templates/kura-project-progress.xlsx)<br>[`kenha-project-progress`](../data-templates/kenha-project-progress.xlsx)<br>[`kerra-project-progress`](../data-templates/kerra-project-progress.xlsx)<br>+3 more

## Working with this page

1. Open **Road Infrastructure → Funding Allocations** from the sidebar.
2. Wait for the page to finish loading. It re-fetches its data every **120 s**; the figures you see are the latest the platform holds, not a one-time snapshot.
3. Click **All Agencies** to use this action.
4. Click **Export CSV** to download the rows currently loaded (after filters). The button only appears for Analyst tier and above.

## Status and value meanings

These are the values the platform stores for the fields shown on this page (`value` followed by the label you see).

| Field | Table | Values |
|---|---|---|
| status | ConstructionProject | `planning` · `procurement` · `in_progress` · `on_hold` · `completed` · `cancelled` |

## Data sources and feeds

Every number and table on this page is read from the API endpoints below. The **Ingested via** column says how the underlying records get into UAPTS: a downloadable **upload template** (xlsx/CSV, loaded through the [Integration Hub](../integration-hub/upload-and-connect.md)), a **live feed** that pushes records to the ingest API, or — where neither exists yet — it is stated plainly.

| Endpoint | Records | Ingested via |
|---|---|---|
| `GET /accounts/agencies/` | Agencies | Platform data (accounts / configuration) |
| `GET /infrastructure/construction-projects/` | Construction Projects | [`krb-workplans`](../data-templates/krb-workplans.xlsx)<br>[`kura-project-progress`](../data-templates/kura-project-progress.xlsx)<br>[`kenha-project-progress`](../data-templates/kenha-project-progress.xlsx)<br>[`kerra-project-progress`](../data-templates/kerra-project-progress.xlsx)<br>[`lapsset-project-progress`](../data-templates/lapsset-project-progress.xlsx)<br>[`namata-project-progress`](../data-templates/namata-project-progress.xlsx)<br>+1 more ([catalogue](../reference/data-sources.md)) |
| `GET /infrastructure/deterioration-forecasts/at-risk/` | Deterioration Forecasts | Computed by UAPTS from other data (no direct feed) |
| `GET /infrastructure/maintenance-budgets/` | Maintenance Budgets | [`krb-funding`](../data-templates/krb-funding.xlsx) |
| `GET /infrastructure/maintenance-budgets/export/` | Maintenance Budgets | [`krb-funding`](../data-templates/krb-funding.xlsx) |
| `GET /infrastructure/road-segments/` | Road Segments | [`krb-road-condition`](../data-templates/krb-road-condition.xlsx)<br>[`kura-road-network`](../data-templates/kura-road-network.xlsx)<br>[`kenha-road-network`](../data-templates/kenha-road-network.xlsx)<br>[`kerra-road-network`](../data-templates/kerra-road-network.xlsx)<br>[`sdr-road-network-register`](../data-templates/sdr-road-network-register.xlsx) |
| `GET /infrastructure/summary/` | _Aggregate of 8 tables (rows below)_ | — |
| ↳ Bridge | Bridges | [`kenha-bridge-register`](../data-templates/kenha-bridge-register.xlsx)<br>[`kerra-bridge-register`](../data-templates/kerra-bridge-register.xlsx) |
| ↳ ConstructionProject | Construction Projects | [`krb-workplans`](../data-templates/krb-workplans.xlsx)<br>[`kura-project-progress`](../data-templates/kura-project-progress.xlsx)<br>[`kenha-project-progress`](../data-templates/kenha-project-progress.xlsx)<br>[`kerra-project-progress`](../data-templates/kerra-project-progress.xlsx)<br>+3 more ([catalogue](../reference/data-sources.md)) |
| ↳ DeteriorationForecast | Deterioration Forecasts | Computed by UAPTS from other data (no direct feed) |
| ↳ MaintenanceBudget | Maintenance Budgets | [`krb-funding`](../data-templates/krb-funding.xlsx) |
| ↳ MaintenanceOrder | Maintenance Orders | [`kura-maintenance-work-orders`](../data-templates/kura-maintenance-work-orders.xlsx)<br>[`kenha-maintenance-work-orders`](../data-templates/kenha-maintenance-work-orders.xlsx)<br>[`kerra-maintenance-work-orders`](../data-templates/kerra-maintenance-work-orders.xlsx) |
| ↳ RoadSegment | Road Segments | [`krb-road-condition`](../data-templates/krb-road-condition.xlsx)<br>[`kura-road-network`](../data-templates/kura-road-network.xlsx)<br>[`kenha-road-network`](../data-templates/kenha-road-network.xlsx)<br>[`kerra-road-network`](../data-templates/kerra-road-network.xlsx)<br>+1 more ([catalogue](../reference/data-sources.md)) |
| ↳ Streetlight | Streetlights | **No ingestion template yet** — populated by seed data or direct entry |
| ↳ WIMReading | Wim Readings | [`kura-weighbridge-transactions`](../data-templates/kura-weighbridge-transactions.xlsx)<br>[`kenha-weighbridge-transactions`](../data-templates/kenha-weighbridge-transactions.xlsx) |

Full details of every template (columns, formats) are in the [Data sources catalogue](../reference/data-sources.md). Interactive API documentation is available at `/api/docs/`.

## Permissions

| Who | What they can do here |
|---|---|
| Public / read-only accounts | No access to this page. |
| Operator | No access (page needs Analyst). |
| Analyst | View and **export CSV**. |
| Agency admin | Everything an analyst can do, plus the administrative capabilities listed in [Roles & Permissions](../access-control/roles-and-permissions.md). |
| Super admin | Sees every agency's data. |

**Agencies with the Road Infrastructure module:** full — KENHA, KURA, KERRA, SDR, KRB, SDT; selected pages only — SDR_MTD, COUNTY_GOV, NTSA, LAPSSET.

_Access is evaluated by the server from the baseline policy plus any agency overrides, so a super admin or agency admin may have changed it from the defaults above._

## Related topics

- [Overview](infrastructure-overview.md)
- [Road Network Inventory](road-network-inventory.md)
- [Road Infrastructure Status](road-infrastructure-status.md)
- [Bridges & Assets](bridges-and-assets.md)
- [Maintenance Orders](maintenance-orders.md)
- [Road Infrastructure overview](index.md)
- [Upload & Connect (Integration Hub)](../integration-hub/upload-and-connect.md)
- [Data sources catalogue](../reference/data-sources.md)

## On this page

- [Highlights](#highlights)
- [Enabling and access](#enabling-and-access)
- [Page tour](#page-tour)
- [Working with this page](#working-with-this-page)
- [Status and value meanings](#status-and-value-meanings)
- [Data sources and feeds](#data-sources-and-feeds)
- [Permissions](#permissions)
- [Related topics](#related-topics)

## Support

- **Your agency administrator** is the first contact for access, role and data-quality questions.
- **Data feeds, templates and API questions:** `api-support@uapts.go.ke` (include the `X-Request-ID` response header from a failing call).
- **Security concerns:** `security@uapts.go.ke`. Do not report suspected vulnerabilities publicly.
