# Border Crossings

_Corridor & Trade › Border Crossings_ · Route `/corridor/border-crossings`

**Border Crossings** lets you see one-stop border posts - queues, waiting and clearance times, truck volumes and the main cause of delay.

> 🎬 **Video tutorial:** _coming soon._  
> <!-- VIDEO-URL: corridor/border-crossings | paste the link here, e.g. [Watch the walkthrough](https://…) -->

## Highlights

- **6 headline tiles** — Avg waiting time, Avg clearance time, Trucks crossed, Longest queue, Slowest post, Posts reporting.
- **4 panels** — daily trend All posts, Posts, What delays crossings · days as top cause, Latest uploads Both directionsInboundOutbound.
- An **interactive map** with a legend, full-screen, locate-me and base-map controls.
- **Filters and search** to narrow tables to what you need.
- Every figure is traceable to the data feed or upload template that supplies it — see [Data sources and feeds](#data-sources-and-feeds).

## Enabling and access

1. Sign in to UAPTS (see [How to access](../getting-started/how-to-access.md)).
2. In the left sidebar expand **Corridor & Trade** and click **Border Crossings**.
3. The page opens at `/corridor/border-crossings`. You can also reach it with the global search (**Ctrl + K**).

This page belongs to module **M15 · Corridor and Trade**. The sidebar and the global search only list pages your agency and role can open, and a link to a page you cannot reach sends you back to the Command Centre. If a page you expect is missing, ask your agency administrator to check your agency's [Module Access](../access-control/module-access.md).

![Border Crossings page](../assets/screenshots/corridor-border-crossings.webp)

## Page tour

### Headline tiles

![Border Crossings headline tiles](../assets/screenshots/corridor-border-crossings--kpis.webp)

| Tile | What it shows | Data from | Table → ingested via |
|---|---|---|---|
| **Avg waiting time** | Across posts reporting | `/corridor/border-crossings/performance/` | _BorderCrossingDaily_ → [`ncttca-border-crossing-daily`](../data-templates/ncttca-border-crossing-daily.xlsx) |
| **Avg clearance time** | Customs and immigration | — | — |
| **Trucks crossed** | Loaded, empty, tankers, containers | `/corridor/border-crossings/performance/` | _BorderCrossingDaily_ → [`ncttca-border-crossing-daily`](../data-templates/ncttca-border-crossing-daily.xlsx) |
| **Longest queue** | — | `/corridor/border-crossings/performance/` | _BorderCrossingDaily_ → [`ncttca-border-crossing-daily`](../data-templates/ncttca-border-crossing-daily.xlsx) |
| **Slowest post** | — | `/corridor/border-crossings/performance/` | _BorderCrossingDaily_ → [`ncttca-border-crossing-daily`](../data-templates/ncttca-border-crossing-daily.xlsx) |
| **Posts reporting** | One-stop border posts | `/corridor/border-crossings/performance/` | _BorderCrossingDaily_ → [`ncttca-border-crossing-daily`](../data-templates/ncttca-border-crossing-daily.xlsx) |

### daily trend All posts

![daily trend All posts](../assets/screenshots/corridor-border-crossings--daily-trend-all-posts.webp)

Contains a chart.

**Data from:** `/corridor/border-crossings/`, `/corridor/border-crossings/daily-trend/`, `/corridor/border-crossings/delay-causes/`, `/corridor/border-crossings/performance/`  
**Table → ingested via:** _BorderCrossingDaily_ → [`ncttca-border-crossing-daily`](../data-templates/ncttca-border-crossing-daily.xlsx)

### Posts


Contains a table with the columns **Border post**, **Wait**, **Clearance**, **Peak queue**, **Utilisation**, **Trucks**, **Main delay**.

**Data from:** `/corridor/border-crossings/performance/`  
**Table → ingested via:** _BorderCrossingDaily_ → [`ncttca-border-crossing-daily`](../data-templates/ncttca-border-crossing-daily.xlsx)

### What delays crossings · days as top cause

![What delays crossings · days as top cause](../assets/screenshots/corridor-border-crossings--what-delays-crossings-days-as-top-caus.webp)

**Data from:** `/corridor/border-crossings/delay-causes/`  
**Table → ingested via:** _BorderCrossingDaily_ → [`ncttca-border-crossing-daily`](../data-templates/ncttca-border-crossing-daily.xlsx)

### Latest uploads Both directionsInboundOutbound

![Latest uploads Both directionsInboundOutbound](../assets/screenshots/corridor-border-crossings--latest-uploads-both-directionsinboundout.webp)

Contains a table with the columns **Date**, **Post**, **Direction**, **Loaded**, **Empty**, **Tankers**, **Containers**, **Wait (h)**, **Queue**, **Lanes**, **Main delay**.

## Working with this page

1. Open **Corridor & Trade → Border Crossings** from the sidebar.
2. Use the **Both directions** drop-down to narrow the list. Choices include: Inbound, Outbound.
3. Use the date-range / day toggle above the charts to change the reporting window; the tiles and charts update together.
4. Click a row to open its detail.
5. On the map, drag to pan and scroll (or pinch) to zoom. Click a marker or line for its details. Use the map toolbar to go full-screen, centre on your location, reset the view or switch the base map; click the legend chip to expand it.

## Data sources and feeds

Every number and table on this page is read from the API endpoints below. The **Ingested via** column says how the underlying records get into UAPTS: a downloadable **upload template** (xlsx/CSV, loaded through the [Integration Hub](../integration-hub/upload-and-connect.md)), a **live feed** that pushes records to the ingest API, or — where neither exists yet — it is stated plainly.

| Endpoint | Records | Ingested via |
|---|---|---|
| `GET /corridor/alignments/` | _Aggregate of 2 tables (rows below)_ | — |
| ↳ Corridor | Corridors | **No ingestion template yet** — populated by seed data or direct entry |
| ↳ CorridorAlignment | Corridor Alignments | **No ingestion template yet** — populated by seed data or direct entry |
| `GET /corridor/border-crossings/` | Border Crossing Dailys | [`ncttca-border-crossing-daily`](../data-templates/ncttca-border-crossing-daily.xlsx) |
| `GET /corridor/border-crossings/daily-trend/` | Border Crossing Dailys | [`ncttca-border-crossing-daily`](../data-templates/ncttca-border-crossing-daily.xlsx) |
| `GET /corridor/border-crossings/delay-causes/` | Border Crossing Dailys | [`ncttca-border-crossing-daily`](../data-templates/ncttca-border-crossing-daily.xlsx) |
| `GET /corridor/border-crossings/performance/` | Border Crossing Dailys | [`ncttca-border-crossing-daily`](../data-templates/ncttca-border-crossing-daily.xlsx) |

Full details of every template (columns, formats) are in the [Data sources catalogue](../reference/data-sources.md). Interactive API documentation is available at `/api/docs/`.

## Permissions

| Who | What they can do here |
|---|---|
| Public / read-only accounts | View the page where the module is enabled for their agency (read-only). |
| Operator | View the page. |
| Analyst | View and **export CSV**. |
| Agency admin | Everything an analyst can do, plus the administrative capabilities listed in [Roles & Permissions](../access-control/roles-and-permissions.md). |
| Super admin | Sees every agency's data. |

**Agencies with the Corridor and Trade module:** full — SDR, SDT, NCTTCA, LAPSSET; read-only — KENTRADE.

_Access is evaluated by the server from the baseline policy plus any agency overrides, so a super admin or agency admin may have changed it from the defaults above._

## Related topics

- [Overview](corridor-overview.md)
- [Northern Corridor](northern-corridor.md)
- [Transit Declarations](transit-declarations.md)
- [LAPSSET Corridor](lapsset-corridor.md)
- [Corridor & Trade overview](index.md)
- [Upload & Connect (Integration Hub)](../integration-hub/upload-and-connect.md)
- [Data sources catalogue](../reference/data-sources.md)

## On this page

- [Highlights](#highlights)
- [Enabling and access](#enabling-and-access)
- [Page tour](#page-tour)
- [Working with this page](#working-with-this-page)
- [Data sources and feeds](#data-sources-and-feeds)
- [Permissions](#permissions)
- [Related topics](#related-topics)

## Support

- **Your agency administrator** is the first contact for access, role and data-quality questions.
- **Data feeds, templates and API questions:** `api-support@uapts.go.ke` (include the `X-Request-ID` response header from a failing call).
- **Security concerns:** `security@uapts.go.ke`. Do not report suspected vulnerabilities publicly.
