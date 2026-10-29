# Bridges & Assets

_Road Infrastructure › Bridges & Assets_ · Route `/infrastructure/bridges`

**Bridge & Asset Registry** lets you see bridge inventory, condition scores, inspection schedules, streetlights, signals, WIM stations and closures. Data on this page comes from KeNHA, KRB and LAPSSET.

> 🎬 **Video tutorial:** _coming soon._  
> <!-- VIDEO-URL: infrastructure/bridges-and-assets | paste the link here, e.g. [Watch the walkthrough](https://…) -->

## Highlights

- **10 headline tiles** — Total Bridges, Good Condition, Fair Condition, Poor / Critical, Avg Condition Score, Overdue Inspections….
- **4 panels** — Critical Bridges - Immediate Action Required (), Condition by Bridge Type, Bridge Inventory (), Closures / Restrictions ().
- An **interactive map** with a legend, full-screen, locate-me and base-map controls.
- **Refreshes itself every 120 seconds**, so you do not need to reload the page.
- **Export to CSV** for the rows you are looking at (Analyst tier and above).
- **Filters and search** to narrow tables to what you need.
- Every figure is traceable to the data feed or upload template that supplies it — see [Data sources and feeds](#data-sources-and-feeds).

## Enabling and access

1. Sign in to UAPTS (see [How to access](../getting-started/how-to-access.md)).
2. In the left sidebar expand **Road Infrastructure** and click **Bridges & Assets**.
3. The page opens at `/infrastructure/bridges`. You can also reach it with the global search (**Ctrl + K**).

This page belongs to module **M06 · Road Infrastructure**. The sidebar and the global search only list pages your agency and role can open, and a link to a page you cannot reach sends you back to the Command Centre. If a page you expect is missing, ask your agency administrator to check your agency's [Module Access](../access-control/module-access.md).

![Bridges & Assets page](../assets/screenshots/infrastructure-bridges.webp)

## Page tour

### Headline tiles


| Tile | What it shows | Data from | Table → ingested via |
|---|---|---|---|
| **Total Bridges** | agencyLabel _(window: LIVE)_ | `/infrastructure/bridges/` | _Bridge_ → [`kenha-bridge-register`](../data-templates/kenha-bridge-register.xlsx)<br>[`kerra-bridge-register`](../data-templates/kerra-bridge-register.xlsx) |
| **Good Condition** | Condition score ≥ 80 _(window: LIVE)_ | — | — |
| **Fair Condition** | Score 60–79, monitor closely _(window: LIVE)_ | — | — |
| **Poor / Critical** | Urgent inspection required _(window: LIVE)_ | `/infrastructure/bridges/critical/` | _Bridge_ → [`kenha-bridge-register`](../data-templates/kenha-bridge-register.xlsx)<br>[`kerra-bridge-register`](../data-templates/kerra-bridge-register.xlsx) |
| **Avg Condition Score** | Out of 100 _(window: LIVE)_ | `/infrastructure/bridges/` | _Bridge_ → [`kenha-bridge-register`](../data-templates/kenha-bridge-register.xlsx)<br>[`kerra-bridge-register`](../data-templates/kerra-bridge-register.xlsx) |
| **Overdue Inspections** | Next inspection date passed _(window: LIVE)_ | `/infrastructure/bridges/` | _Bridge_ → [`kenha-bridge-register`](../data-templates/kenha-bridge-register.xlsx)<br>[`kerra-bridge-register`](../data-templates/kerra-bridge-register.xlsx) |
| **Streetlights Operational** | Of registered streetlights _(window: LIVE)_ | `/infrastructure/summary/` | _Streetlight_ → no template yet |
| **Traffic Signal Faults** | agencyLabel _(window: LIVE)_ | `/infrastructure/traffic-signals/faults/` | _TrafficSignal_ → no template yet |
| **WIM Overload Rate** | Network-wide · 30d _(window: 30D)_ | `/infrastructure/summary/` | _WIMReading_ → [`kura-weighbridge-transactions`](../data-templates/kura-weighbridge-transactions.xlsx)<br>[`kenha-weighbridge-transactions`](../data-templates/kenha-weighbridge-transactions.xlsx) |
| **Closures / Restrictions** | Active rural road reports _(window: LIVE)_ | `/infrastructure/rural-road-status/` | _RuralRoadStatus_ → no template yet |

### Critical Bridges - Immediate Action Required ()


Contains an interactive map.

**Data from:** `/infrastructure/bridges/`, `/infrastructure/bridges/critical/`  
**Table → ingested via:** _Bridge_ → [`kenha-bridge-register`](../data-templates/kenha-bridge-register.xlsx)<br>[`kerra-bridge-register`](../data-templates/kerra-bridge-register.xlsx)

### Condition by Bridge Type


**Data from:** `/infrastructure/bridges/`  
**Table → ingested via:** _Bridge_ → [`kenha-bridge-register`](../data-templates/kenha-bridge-register.xlsx)<br>[`kerra-bridge-register`](../data-templates/kerra-bridge-register.xlsx)

### Bridge Inventory ()


Contains a table with the columns **Bridge Name**, **Code**, **Agency**, **Type**, **Span (m)**, **Load Limit (t)**, **Condition Score**, **Condition**, **Year Built**, **Last Inspection**, **Next Inspection**.

**Data from:** `/infrastructure/bridges/`, `/infrastructure/bridges/critical/`, `/infrastructure/rural-road-status/`  
**Table → ingested via:** _Bridge, RuralRoadStatus_ → [`kenha-bridge-register`](../data-templates/kenha-bridge-register.xlsx)<br>[`kerra-bridge-register`](../data-templates/kerra-bridge-register.xlsx)

### Closures / Restrictions ()


Contains a table with the columns **Road**, **Status**, **Reason**, **Reported**.

## Working with this page

1. Open **Road Infrastructure → Bridges & Assets** from the sidebar.
2. Wait for the page to finish loading. It re-fetches its data every **120 s**; the figures you see are the latest the platform holds, not a one-time snapshot.
3. Type in the **“Search bridge name…”** box to filter what is shown.
4. Use the **All conditions** drop-down to narrow the list. Choices include: Excellent, Good, Fair, Poor, Critical.
5. Use the **All types** drop-down to narrow the list. Choices include: Beam, Arch, Suspension, Truss, Culvert, Bailey.
6. Click a row to open its detail.
7. On the map, drag to pan and scroll (or pinch) to zoom. Click a marker or line for its details. Use the map toolbar to go full-screen, centre on your location, reset the view or switch the base map; click the legend chip to expand it.
8. Click **All Agencies** to use this action.
9. Click **Export CSV** to download the rows currently loaded (after filters). The button only appears for Analyst tier and above.

## Status and value meanings

These are the values the platform stores for the fields shown on this page (`value` followed by the label you see).

| Field | Table | Values |
|---|---|---|
| bridge type | Bridge | `suspension` · `beam` · `arch` · `truss` · `culvert` · `bailey` · `box_culvert` |
| condition class | Bridge | `excellent` · `good` · `fair` · `poor` · `critical` |
| status | RuralRoadStatus | `passable` · `partially_passable` · `impassable` · `closed` |
| status | TrafficSignal | `operational` · `degraded` · `fault` · `offline` · `maintenance` Under Maintenance |

## Data sources and feeds

Every number and table on this page is read from the API endpoints below. The **Ingested via** column says how the underlying records get into UAPTS: a downloadable **upload template** (xlsx/CSV, loaded through the [Integration Hub](../integration-hub/upload-and-connect.md)), a **live feed** that pushes records to the ingest API, or — where neither exists yet — it is stated plainly.

| Endpoint | Records | Ingested via |
|---|---|---|
| `GET /infrastructure/bridges/` | Bridges | [`kenha-bridge-register`](../data-templates/kenha-bridge-register.xlsx)<br>[`kerra-bridge-register`](../data-templates/kerra-bridge-register.xlsx) |
| `GET /infrastructure/bridges/critical/` | Bridges | [`kenha-bridge-register`](../data-templates/kenha-bridge-register.xlsx)<br>[`kerra-bridge-register`](../data-templates/kerra-bridge-register.xlsx) |
| `GET /infrastructure/rural-road-status/` | Rural Road Statuss | **No ingestion template yet** — populated by seed data or direct entry |
| `GET /infrastructure/summary/` | _Aggregate of 8 tables (rows below)_ | — |
| ↳ Bridge | Bridges | [`kenha-bridge-register`](../data-templates/kenha-bridge-register.xlsx)<br>[`kerra-bridge-register`](../data-templates/kerra-bridge-register.xlsx) |
| ↳ ConstructionProject | Construction Projects | [`krb-workplans`](../data-templates/krb-workplans.xlsx)<br>[`kura-project-progress`](../data-templates/kura-project-progress.xlsx)<br>[`kenha-project-progress`](../data-templates/kenha-project-progress.xlsx)<br>[`kerra-project-progress`](../data-templates/kerra-project-progress.xlsx)<br>+3 more ([catalogue](../reference/data-sources.md)) |
| ↳ DeteriorationForecast | Deterioration Forecasts | Computed by UAPTS from other data (no direct feed) |
| ↳ MaintenanceBudget | Maintenance Budgets | [`krb-funding`](../data-templates/krb-funding.xlsx) |
| ↳ MaintenanceOrder | Maintenance Orders | [`kura-maintenance-work-orders`](../data-templates/kura-maintenance-work-orders.xlsx)<br>[`kenha-maintenance-work-orders`](../data-templates/kenha-maintenance-work-orders.xlsx)<br>[`kerra-maintenance-work-orders`](../data-templates/kerra-maintenance-work-orders.xlsx) |
| ↳ RoadSegment | Road Segments | [`krb-road-condition`](../data-templates/krb-road-condition.xlsx)<br>[`kura-road-network`](../data-templates/kura-road-network.xlsx)<br>[`kenha-road-network`](../data-templates/kenha-road-network.xlsx)<br>[`kerra-road-network`](../data-templates/kerra-road-network.xlsx)<br>+1 more ([catalogue](../reference/data-sources.md)) |
| ↳ Streetlight | Streetlights | **No ingestion template yet** — populated by seed data or direct entry |
| ↳ WIMReading | Wim Readings | [`kura-weighbridge-transactions`](../data-templates/kura-weighbridge-transactions.xlsx)<br>[`kenha-weighbridge-transactions`](../data-templates/kenha-weighbridge-transactions.xlsx) |
| `GET /infrastructure/traffic-signals/faults/` | Traffic Signals | **No ingestion template yet** — populated by seed data or direct entry |

Full details of every template (columns, formats) are in the [Data sources catalogue](../reference/data-sources.md). Interactive API documentation is available at `/api/docs/`.

## Permissions

| Who | What they can do here |
|---|---|
| Public / read-only accounts | View the page where the module is enabled for their agency (read-only). |
| Operator | View the page. |
| Analyst | View and **export CSV**. |
| Agency admin | Everything an analyst can do, plus the administrative capabilities listed in [Roles & Permissions](../access-control/roles-and-permissions.md). |
| Super admin | Sees every agency's data. |

**Agencies with the Road Infrastructure module:** full — KENHA, KURA, KERRA, SDR, KRB, SDT; selected pages only — SDR_MTD, COUNTY_GOV, NTSA, LAPSSET.

_Access is evaluated by the server from the baseline policy plus any agency overrides, so a super admin or agency admin may have changed it from the defaults above._

## Related topics

- [Overview](infrastructure-overview.md)
- [Road Network Inventory](road-network-inventory.md)
- [Road Infrastructure Status](road-infrastructure-status.md)
- [Funding Allocations](funding-allocations.md)
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
