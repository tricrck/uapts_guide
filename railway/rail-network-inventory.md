# Rail Network Inventory

_Railway › Rail Network Inventory_ · Route `/railway/network-inventory`

**Rail Network Inventory** lets you see line, station and rolling-stock registry with an SGR/MGR comparison panel and cross-network data quality checks. Data on this page comes from KRC and NCTTCA.

> 🎬 **Video tutorial:** _coming soon._  
> <!-- VIDEO-URL: railway/rail-network-inventory | paste the link here, e.g. [Watch the walkthrough](https://…) -->

## Highlights

- **8 panels** — Network Map, Line Inventory, Station Inventory, Rolling Stock Registry, Missing Geometry (), Stale Station Records ()….
- An **interactive map** with a legend, full-screen, locate-me and base-map controls.
- **Refreshes itself every 120 seconds**, so you do not need to reload the page.
- **Filters and search** to narrow tables to what you need.
- Every figure is traceable to the data feed or upload template that supplies it — see [Data sources and feeds](#data-sources-and-feeds).

## Enabling and access

1. Sign in to UAPTS (see [How to access](../getting-started/how-to-access.md)).
2. In the left sidebar expand **Railway** and click **Rail Network Inventory**.
3. The page opens at `/railway/network-inventory`. You can also reach it with the global search (**Ctrl + K**).

This page belongs to module **M08 · Railway**. The sidebar and the global search only list pages your agency and role can open, and a link to a page you cannot reach sends you back to the Command Centre. If a page you expect is missing, ask your agency administrator to check your agency's [Module Access](../access-control/module-access.md).

![Rail Network Inventory page](../assets/screenshots/railway-network-inventory.webp)

## Page tour

### Network Map


Contains an interactive map.

**Data from:** `/geojson/rail-lines/`, `/geojson/rail-stations/`, `/railway/lines/`  
**Table → ingested via:** _RailLine_ → no template yet

### Line Inventory


Contains a table with the columns **Line**, **Network**, **Gauge**, **Region**, **Length (km)**, **Stations**, **Status**, **Operator**, **Electrification**, **Source Updated**.

**Data from:** `/railway/lines/`  
**Table → ingested via:** _RailLine_ → no template yet

### Station Inventory


Contains a table with the columns **Code**, **Name**, **Type**, **Network**, **Coordinates**, **County**, **Capacity/day**, **Freight Terminal**, **Platforms**.

**Data from:** `/railway/freight/`, `/railway/operations/`, `/railway/stations/`, `/railway/tickets/`  
**Table → ingested via:** _FreightManifest, TrainOperation, RailStation, RailTicket_ → [`krc-rail-station-register`](../data-templates/krc-rail-station-register.xlsx)

### Rolling Stock Registry


Contains a table with the columns **Unit ID**, **Type**, **Network**, **Status**, **Capacity**, **Current Assignment**, **Maintenance**, **Age**, **Depot**, **Available**.

**Data from:** `/railway/trains/`  
**Table → ingested via:** _Train_ → [`krc-train-register`](../data-templates/krc-train-register.xlsx)

### Missing Geometry ()


**Data from:** `/geojson/rail-lines/`, `/geojson/rail-stations/`, `/railway/lines/`, `/railway/stations/`, `/railway/trains/`  
**Table → ingested via:** _RailLine, RailStation, Train_ → [`krc-rail-station-register`](../data-templates/krc-rail-station-register.xlsx)<br>[`krc-train-register`](../data-templates/krc-train-register.xlsx)

### Stale Station Records ()


**Data from:** `/geojson/rail-lines/`, `/geojson/rail-stations/`, `/railway/lines/`, `/railway/stations/`, `/railway/trains/`  
**Table → ingested via:** _RailLine, RailStation, Train_ → [`krc-rail-station-register`](../data-templates/krc-rail-station-register.xlsx)<br>[`krc-train-register`](../data-templates/krc-train-register.xlsx)

### Unknown Rolling Stock Status ()


**Data from:** `/geojson/rail-lines/`, `/geojson/rail-stations/`, `/railway/lines/`, `/railway/stations/`, `/railway/trains/`  
**Table → ingested via:** _RailLine, RailStation, Train_ → [`krc-rail-station-register`](../data-templates/krc-rail-station-register.xlsx)<br>[`krc-train-register`](../data-templates/krc-train-register.xlsx)

### Inconsistent Network / Gauge Classification ()

![Inconsistent Network / Gauge Classification ()](../assets/screenshots/railway-network-inventory--inconsistent-network-gauge-classificat.webp)

**Data from:** `/geojson/rail-lines/`, `/geojson/rail-stations/`, `/railway/lines/`, `/railway/stations/`, `/railway/trains/`  
**Table → ingested via:** _RailLine, RailStation, Train_ → [`krc-rail-station-register`](../data-templates/krc-rail-station-register.xlsx)<br>[`krc-train-register`](../data-templates/krc-train-register.xlsx)

## Working with this page

1. Open **Railway → Rail Network Inventory** from the sidebar.
2. Wait for the page to finish loading. It re-fetches its data every **120 s**; the figures you see are the latest the platform holds, not a one-time snapshot.
3. Type in the **“Search station name/code…”** box to filter what is shown.
4. Type in the **“Search unit ID…”** box to filter what is shown.
5. Use the **All networks** drop-down to narrow the list. Choices include: SGR, MGR, Uganda Railway.
6. Use the **All types** drop-down to narrow the list. Choices include: Terminal, Interchange, Intermediate, Halt, Freight, Depot.
7. Use the **All statuses** drop-down to narrow the list. Choices include: In Service, Standby, Maintenance, Inspection, Retired.
8. Use the **All networks** drop-down to narrow the list. Choices include: SGR, MGR, Other / Freight.
9. Click a row to open its detail.
10. On the map, drag to pan and scroll (or pinch) to zoom. Click a marker or line for its details. Use the map toolbar to go full-screen, centre on your location, reset the view or switch the base map; click the legend chip to expand it.

## Status and value meanings

These are the values the platform stores for the fields shown on this page (`value` followed by the label you see).

| Field | Table | Values |
|---|---|---|
| severity | RailIncident | `fatal` Fatality · `serious` Serious injury · `minor` Minor injury · `none` No injury |
| status | RailIncident | `open` · `investigating` · `resolved` · `closed` |
| status | RailLine | `operational` · `under_construction` · `planned` · `suspended` Service suspended · `abandoned` · `decommissioned` |
| status | TrainOperation | `scheduled` · `boarding` · `departed` · `in_transit` · `arrived` · `delayed` · `cancelled` · `diverted` |
| station type | RailStation | `terminal` · `interchange` · `intermediate` · `halt` · `freight` Freight only · `depot` Depot / marshalling |
| train type | Train | `sgr_emu` SGR EMU (electric) · `sgr_dmu` SGR DMU (diesel) · `mgr_loco` MGR locomotive · `mgr_coach` MGR coach set · `freight_loco` Freight locomotive · `maintenance` Maintenance vehicle |
| status | Train | `in_service` · `standby` On standby · `maintenance` Under maintenance · `retired` · `inspection` Under inspection |

## Data sources and feeds

Every number and table on this page is read from the API endpoints below. The **Ingested via** column says how the underlying records get into UAPTS: a downloadable **upload template** (xlsx/CSV, loaded through the [Integration Hub](../integration-hub/upload-and-connect.md)), a **live feed** that pushes records to the ingest API, or — where neither exists yet — it is stated plainly.

| Endpoint | Records | Ingested via |
|---|---|---|
| `GET /geojson/rail-lines/` | _Aggregate of 1 tables (rows below)_ | — |
| ↳ RailLine | Rail Lines | **No ingestion template yet** — populated by seed data or direct entry |
| `GET /geojson/rail-stations/` | _Aggregate of 1 tables (rows below)_ | — |
| ↳ RailStation | Rail Stations | [`krc-rail-station-register`](../data-templates/krc-rail-station-register.xlsx) |
| `GET /railway/freight/` | Freight Manifests | **No ingestion template yet** — populated by seed data or direct entry |
| `GET /railway/incidents/` | Rail Incidents | [`krc-rail-incident-log`](../data-templates/krc-rail-incident-log.xlsx) |
| `GET /railway/lines/` | Rail Lines | **No ingestion template yet** — populated by seed data or direct entry |
| `GET /railway/operations/` | Train Operations | **No ingestion template yet** — populated by seed data or direct entry |
| `GET /railway/schedules/` | Train Schedules | [`krc-train-schedule-register`](../data-templates/krc-train-schedule-register.xlsx) |
| `GET /railway/stations/` | Rail Stations | [`krc-rail-station-register`](../data-templates/krc-rail-station-register.xlsx) |
| `GET /railway/tickets/` | Rail Tickets | **No ingestion template yet** — populated by seed data or direct entry |
| `GET /railway/trains/` | Trains | [`krc-train-register`](../data-templates/krc-train-register.xlsx) |

Full details of every template (columns, formats) are in the [Data sources catalogue](../reference/data-sources.md). Interactive API documentation is available at `/api/docs/`.

## Permissions

| Who | What they can do here |
|---|---|
| Public / read-only accounts | View the page where the module is enabled for their agency (read-only). |
| Operator | View the page. |
| Analyst | View and **export CSV**. |
| Agency admin | Everything an analyst can do, plus the administrative capabilities listed in [Roles & Permissions](../access-control/roles-and-permissions.md). |
| Super admin | Sees every agency's data. |

**Agencies with the Railway module:** full — SDT, KRC; selected pages only — KENHA, NAMATA, KPA, NCTTCA, LAPSSET.

_Access is evaluated by the server from the baseline policy plus any agency overrides, so a super admin or agency admin may have changed it from the defaults above._

## Related topics

- [Railway Overview](railway-overview.md)
- [Train Operations](train-operations.md)
- [Freight Volumes](freight-volumes.md)
- [Schedules](schedules.md)
- [Rail Infrastructure](rail-infrastructure.md)
- [Rail Safety](rail-safety.md)
- [Railway overview](index.md)
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
