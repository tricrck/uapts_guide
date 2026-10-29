# Port Operations

_Maritime › Port Operations_ · Route `/maritime/port-ops`

**Port Operations** lets you see berth occupancy, container throughput, KenTrade clearance data, NCTTCA corridor dwell analysis, and 60-day trends. Data on this page comes from KPA, KMA, KenTrade and NCTTCA.

> 🎬 **Video tutorial:** _coming soon._  
> <!-- VIDEO-URL: maritime/port-operations | paste the link here, e.g. [Watch the walkthrough](https://…) -->

## Highlights

- **6 headline tiles** — Active Ports, Live Vessels, Avg Yard Dwell, Total TEU (30d), Berths (Total), Active Berths.
- **3 panels** — Port &amp; Berth Map, Berth Directory & Status, Yard Dwell by Direction.
- An **interactive map** with a legend, full-screen, locate-me and base-map controls.
- **Refreshes itself every 120 seconds**, so you do not need to reload the page.
- **Filters and search** to narrow tables to what you need.
- Every figure is traceable to the data feed or upload template that supplies it — see [Data sources and feeds](#data-sources-and-feeds).

## Enabling and access

1. Sign in to UAPTS (see [How to access](../getting-started/how-to-access.md)).
2. In the left sidebar expand **Maritime** and click **Port Operations**.
3. The page opens at `/maritime/port-ops`. You can also reach it with the global search (**Ctrl + K**).

This page belongs to module **M07b · Maritime**. The sidebar and the global search only list pages your agency and role can open, and a link to a page you cannot reach sends you back to the Command Centre. If a page you expect is missing, ask your agency administrator to check your agency's [Module Access](../access-control/module-access.md).

![Port Operations page](../assets/screenshots/maritime-port-ops.webp)

## Page tour

### Headline tiles

![Port Operations headline tiles](../assets/screenshots/maritime-port-ops--kpis.webp)

| Tile | What it shows | Data from | Table → ingested via |
|---|---|---|---|
| **Active Ports** | KPA operational _(window: LIVE)_ | `/aviation-maritime/maritime/operations/` | aggregate of several tables — see [per-table feeds](#data-sources-and-feeds) |
| **Live Vessels** | Currently in port _(window: LIVE)_ | `/aviation-maritime/maritime/operations/` | _VesselMovement_ → live feed `kpa-tos` |
| **Avg Yard Dwell** | Network-wide average _(window: 30D)_ | `/aviation-maritime/maritime/operations/` | _YardDwell_ → no template yet |
| **Total TEU (30d)** | All ports _(window: 30D)_ | `/aviation-maritime/maritime/container-throughput/trend/`, `/aviation-maritime/maritime/operations/` | _ContainerThroughput_ → computed by UAPTS |
| **Berths (Total)** | Across all ports _(window: LIVE)_ | `/aviation-maritime/maritime/berths/` | _Berth_ → [`kpa-berth-register`](../data-templates/kpa-berth-register.xlsx) |
| **Active Berths** | — _(window: LIVE)_ | `/aviation-maritime/maritime/berths/` | _Berth_ → [`kpa-berth-register`](../data-templates/kpa-berth-register.xlsx) |

### Port &amp; Berth Map


Contains an interactive map.

### Berth Directory & Status


Contains a table with the columns **Berth Code**, **Name**, **Type**, **Port**, **Length (m)**, **Max Draft (m)**, **Max LOA (m)**, **Cranes**, **Status**.

**Data from:** `/aviation-maritime/maritime/berths/`  
**Table → ingested via:** _Berth_ → [`kpa-berth-register`](../data-templates/kpa-berth-register.xlsx)

### Yard Dwell by Direction


Contains a table with the columns **Port**, **Direction**, **Container Count**, **Avg Dwell (days)**, **Max Dwell (days)**, **Date**.

**Data from:** `/aviation-maritime/maritime/yard-dwell/`  
**Table → ingested via:** _YardDwell_ → no template yet

## Working with this page

1. Open **Maritime → Port Operations** from the sidebar.
2. Wait for the page to finish loading. It re-fetches its data every **120 s**; the figures you see are the latest the platform holds, not a one-time snapshot.
3. Use the **All berth types** drop-down to narrow the list. Choices include: Container, Bulk, Tanker, General Cargo, Ro-Ro, Cruise.
4. On the map, drag to pan and scroll (or pinch) to zoom. Click a marker or line for its details. Use the map toolbar to go full-screen, centre on your location, reset the view or switch the base map; click the legend chip to expand it.
5. Click **↻ Refresh** to refresh the data.

## Status and value meanings

These are the values the platform stores for the fields shown on this page (`value` followed by the label you see).

| Field | Table | Values |
|---|---|---|
| berth type | Berth | `container` Container terminal · `general_cargo` · `bulk` Bulk cargo · `tanker` Tanker / liquid · `fishing` · `ro_ro` RoRo · `cruise` |

## Data sources and feeds

Every number and table on this page is read from the API endpoints below. The **Ingested via** column says how the underlying records get into UAPTS: a downloadable **upload template** (xlsx/CSV, loaded through the [Integration Hub](../integration-hub/upload-and-connect.md)), a **live feed** that pushes records to the ingest API, or — where neither exists yet — it is stated plainly.

| Endpoint | Records | Ingested via |
|---|---|---|
| `GET /aviation-maritime/maritime/berths/` | Berths | [`kpa-berth-register`](../data-templates/kpa-berth-register.xlsx) |
| `GET /aviation-maritime/maritime/container-throughput/trend/` | Container Throughputs | Computed by UAPTS from other data (no direct feed) |
| `GET /aviation-maritime/maritime/operations/` | _Aggregate of 5 tables (rows below)_ | — |
| ↳ ContainerThroughput | Container Throughputs | Computed by UAPTS from other data (no direct feed) |
| ↳ MaritimeIncident | Maritime Incidents | [`kma-marine-incidents`](../data-templates/kma-marine-incidents.xlsx) |
| ↳ MaritimeInspection | Maritime Inspections | [`kma-vessel-inspections`](../data-templates/kma-vessel-inspections.xlsx) |
| ↳ VesselMovement | Vessel Movements | live feed `kpa-tos` (KPA TOS) |
| ↳ YardDwell | Yard Dwells | **No ingestion template yet** — populated by seed data or direct entry |
| `GET /aviation-maritime/maritime/yard-dwell/` | Yard Dwells | **No ingestion template yet** — populated by seed data or direct entry |

Full details of every template (columns, formats) are in the [Data sources catalogue](../reference/data-sources.md). Interactive API documentation is available at `/api/docs/`.

## Permissions

| Who | What they can do here |
|---|---|
| Public / read-only accounts | View the page where the module is enabled for their agency (read-only). |
| Operator | View the page. |
| Analyst | View and **export CSV**. |
| Agency admin | Everything an analyst can do, plus the administrative capabilities listed in [Roles & Permissions](../access-control/roles-and-permissions.md). |
| Super admin | Sees every agency's data. |

**Agencies with the Maritime module:** full — SDT, KPA, KMA; selected pages only — KENHA, KRA, KENTRADE, KRC, NCTTCA, LAPSSET.

_Access is evaluated by the server from the baseline policy plus any agency overrides, so a super admin or agency admin may have changed it from the defaults above._

## Related topics

- [Overview](maritime-overview.md)
- [Vessel Movements](vessel-movements.md)
- [Vessel Registry](vessel-registry.md)
- [Port Services](port-services.md)
- [Cargo Tracking](cargo-tracking.md)
- [Imports and Exports](imports-and-exports.md)
- [Maritime overview](index.md)
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
