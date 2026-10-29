# Geofences

_Fleet & Vehicle Tracking › Geofences_ · Route `/fleet/geofences`

**Geofence Zones** lets you see configure zones (depots, ports, restricted areas) and monitor entry/exit breach events.

> 🎬 **Video tutorial:** _coming soon._  
> <!-- VIDEO-URL: fleet/geofences | paste the link here, e.g. [Watch the walkthrough](https://…) -->

## Highlights

- **4 headline tiles** — Total Zones, Active Zones, Breaches (24h), Critical Zones.
- **2 panels** — Recent Breach Events, Geofence Zone Inventory.
- An **interactive map** with a legend, full-screen, locate-me and base-map controls.
- **Refreshes itself every 60 seconds**, so you do not need to reload the page.
- **Export to CSV** for the rows you are looking at (Analyst tier and above).
- **Filters and search** to narrow tables to what you need.
- Every figure is traceable to the data feed or upload template that supplies it — see [Data sources and feeds](#data-sources-and-feeds).

## Enabling and access

1. Sign in to UAPTS (see [How to access](../getting-started/how-to-access.md)).
2. In the left sidebar expand **Fleet & Vehicle Tracking** and click **Geofences**.
3. The page opens at `/fleet/geofences`. You can also reach it with the global search (**Ctrl + K**).

This page belongs to module **M03 · Fleet and Vehicle Tracking**. The sidebar and the global search only list pages your agency and role can open, and a link to a page you cannot reach sends you back to the Command Centre. If a page you expect is missing, ask your agency administrator to check your agency's [Module Access](../access-control/module-access.md).

![Geofences page](../assets/screenshots/fleet-geofences.webp)

## Page tour

### Headline tiles

![Geofences headline tiles](../assets/screenshots/fleet-geofences--kpis.webp)

| Tile | What it shows | Data from | Table → ingested via |
|---|---|---|---|
| **Total Zones** | Configured geofence zones _(window: LIVE)_ | `/fleet/geofences/` | _Geofence_ → [`ntsa-geofence-register`](../data-templates/ntsa-geofence-register.xlsx) |
| **Active Zones** | Currently monitoring _(window: LIVE)_ | `/fleet/geofences/` | _Geofence_ → [`ntsa-geofence-register`](../data-templates/ntsa-geofence-register.xlsx) |
| **Breaches (24h)** | All entry / exit / dwell events _(window: 24H)_ | `/fleet/geofence-events/recent/` | _GeofenceEvent_ → live telemetry push (no template yet) |
| **Critical Zones** | Highest-severity geofences _(window: LIVE)_ | `/fleet/geofences/` | _Geofence_ → [`ntsa-geofence-register`](../data-templates/ntsa-geofence-register.xlsx) |

### Recent Breach Events

![Recent Breach Events](../assets/screenshots/fleet-geofences--recent-breach-events.webp)

**Data from:** `/fleet/geofence-events/recent/`  
**Table → ingested via:** _GeofenceEvent_ → live telemetry push (no template yet)

### Geofence Zone Inventory


Contains a table with the columns **Zone Name**, **Type**, **Severity**, **Radius (m)**, **Active**, **Agency**, **Created**.

**Data from:** `/fleet/geofences/`  
**Table → ingested via:** _Geofence_ → [`ntsa-geofence-register`](../data-templates/ntsa-geofence-register.xlsx)

## Working with this page

1. Open **Fleet & Vehicle Tracking → Geofences** from the sidebar.
2. Wait for the page to finish loading. It re-fetches its data every **60 s**; the figures you see are the latest the platform holds, not a one-time snapshot.
3. Type in the **“Search zone name…”** box to filter what is shown.
4. Use the **All zone types** drop-down to narrow the list. Choices include: Depot, Port, Restricted, School zone, Hospital, Weighbridge.
5. Use the **All severities** drop-down to narrow the list. Choices include: Critical, High, Medium, Low.
6. Click a row to open its detail.
7. On the map, drag to pan and scroll (or pinch) to zoom. Click a marker or line for its details. Use the map toolbar to go full-screen, centre on your location, reset the view or switch the base map; click the legend chip to expand it.
8. Click **↻ Refresh** to refresh the data.
9. Click **Export CSV** to download the rows currently loaded (after filters). The button only appears for Analyst tier and above.

## Status and value meanings

These are the values the platform stores for the fields shown on this page (`value` followed by the label you see).

| Field | Table | Values |
|---|---|---|
| event type | GeofenceEvent | `entry` · `exit` · `dwell` Excessive Dwell |
| zone type | Geofence | `county_boundary` · `restricted_area` · `route_corridor` · `school_zone` · `depot` · `custom` |
| severity | Geofence | `info` · `warning` · `critical` |

## Data sources and feeds

Every number and table on this page is read from the API endpoints below. The **Ingested via** column says how the underlying records get into UAPTS: a downloadable **upload template** (xlsx/CSV, loaded through the [Integration Hub](../integration-hub/upload-and-connect.md)), a **live feed** that pushes records to the ingest API, or — where neither exists yet — it is stated plainly.

| Endpoint | Records | Ingested via |
|---|---|---|
| `GET /fleet/geofence-events/recent/` | Geofence Events | Live telemetry — push via `POST /api/v1/integrations/<source_id>/ingest/`; **no template or handler yet** |
| `GET /fleet/geofences/` | Geofences | [`ntsa-geofence-register`](../data-templates/ntsa-geofence-register.xlsx) |

Full details of every template (columns, formats) are in the [Data sources catalogue](../reference/data-sources.md). Interactive API documentation is available at `/api/docs/`.

## Permissions

| Who | What they can do here |
|---|---|
| Public / read-only accounts | View the page where the module is enabled for their agency (read-only). |
| Operator | View the page. |
| Analyst | View and **export CSV**. |
| Agency admin | Everything an analyst can do, plus the administrative capabilities listed in [Roles & Permissions](../access-control/roles-and-permissions.md). |
| Super admin | Sees every agency's data. |

**Agencies with the Fleet and Vehicle Tracking module:** full — SDR, SDR_MTD, SDT, NTSA; selected pages only — KENHA, NAMATA, KRC.

_Access is evaluated by the server from the baseline policy plus any agency overrides, so a super admin or agency admin may have changed it from the defaults above._

## Related topics

- [Fleet Overview](fleet-overview.md)
- [Driver Behaviour](driver-behaviour.md)
- [Live Positions](live-positions.md)
- [Trip Playback](trip-playback.md)
- [Fleet & Vehicle Tracking overview](index.md)
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
