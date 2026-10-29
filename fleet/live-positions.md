# Live Positions

_Fleet & Vehicle Tracking › Live Positions_ · Route `/fleet/live`

**Live Vehicle Positions** lets you see real-time GPS positions for all active PSVs and government fleet - refreshes every 30 seconds.

> 🎬 **Video tutorial:** _coming soon._  
> <!-- VIDEO-URL: fleet/live-positions | paste the link here, e.g. [Watch the walkthrough](https://…) -->

## Highlights

- **2 panels** — Recent Geofence Breaches, Live Vehicle List.
- An **interactive map** with a legend, full-screen, locate-me and base-map controls.
- **Refreshes itself every 30 seconds**, so you do not need to reload the page.
- **Filters and search** to narrow tables to what you need.
- Every figure is traceable to the data feed or upload template that supplies it — see [Data sources and feeds](#data-sources-and-feeds).

## Enabling and access

1. Sign in to UAPTS (see [How to access](../getting-started/how-to-access.md)).
2. In the left sidebar expand **Fleet & Vehicle Tracking** and click **Live Positions**.
3. The page opens at `/fleet/live`. You can also reach it with the global search (**Ctrl + K**).

This page belongs to module **M03 · Fleet and Vehicle Tracking**. The route needs at least the **Operator** tier to open it. The sidebar and the global search only list pages your agency and role can open, and a link to a page you cannot reach sends you back to the Command Centre. If a page you expect is missing, ask your agency administrator to check your agency's [Module Access](../access-control/module-access.md).

![Live Positions page](../assets/screenshots/fleet-live.webp)

## Page tour

### Recent Geofence Breaches

![Recent Geofence Breaches](../assets/screenshots/fleet-live--recent-geofence-breaches.webp)

**Data from:** `/fleet/geofence-events/recent/`  
**Table → ingested via:** _GeofenceEvent_ → live telemetry push (no template yet)

### Live Vehicle List


Contains a table with the columns **Plate**, **Type**, **Status**, **Speed (km/h)**, **Route**, **Operator**, **Last Seen**.

**Data from:** `/fleet/vehicles/live/`  
**Table → ingested via:** _Vehicle_ → [`ntsa-psv-fleet-register`](../data-templates/ntsa-psv-fleet-register.xlsx)

## Working with this page

1. Open **Fleet & Vehicle Tracking → Live Positions** from the sidebar.
2. Wait for the page to finish loading. It re-fetches its data every **30 s**; the figures you see are the latest the platform holds, not a one-time snapshot.
3. Type in the **“Search plate number…”** box to filter what is shown.
4. Use the **All vehicle types** drop-down to narrow the list. Choices include: PSV Matatu, PSV Bus, BRT, Taxi, Truck, Government.
5. On the map, drag to pan and scroll (or pinch) to zoom. Click a marker or line for its details. Use the map toolbar to go full-screen, centre on your location, reset the view or switch the base map; click the legend chip to expand it.
6. Click **Apply** to use this action.
7. Click **↻ Refresh** to refresh the data.

## Status and value meanings

These are the values the platform stores for the fields shown on this page (`value` followed by the label you see).

| Field | Table | Values |
|---|---|---|
| event type | GeofenceEvent | `entry` · `exit` · `dwell` Excessive Dwell |
| vehicle type | Vehicle | `psv_matatu` · `psv_bus` · `brt` · `taxi` · `truck` · `government` · `private` · `rail` |
| status | Vehicle | `operational` · `maintenance` · `impounded` |

## Data sources and feeds

Every number and table on this page is read from the API endpoints below. The **Ingested via** column says how the underlying records get into UAPTS: a downloadable **upload template** (xlsx/CSV, loaded through the [Integration Hub](../integration-hub/upload-and-connect.md)), a **live feed** that pushes records to the ingest API, or — where neither exists yet — it is stated plainly.

| Endpoint | Records | Ingested via |
|---|---|---|
| `GET /fleet/geofence-events/recent/` | Geofence Events | Live telemetry — push via `POST /api/v1/integrations/<source_id>/ingest/`; **no template or handler yet** |
| `GET /fleet/vehicles/live/` | Vehicles | [`ntsa-psv-fleet-register`](../data-templates/ntsa-psv-fleet-register.xlsx) |

Full details of every template (columns, formats) are in the [Data sources catalogue](../reference/data-sources.md). Interactive API documentation is available at `/api/docs/`.

## Permissions

| Who | What they can do here |
|---|---|
| Public / read-only accounts | No access to this page. |
| Operator | View the page. |
| Analyst | View and **export CSV**. |
| Agency admin | Everything an analyst can do, plus the administrative capabilities listed in [Roles & Permissions](../access-control/roles-and-permissions.md). |
| Super admin | Sees every agency's data. |

**Agencies with the Fleet and Vehicle Tracking module:** full — SDR, SDR_MTD, SDT, NTSA; selected pages only — KENHA, NAMATA, KRC.

_Access is evaluated by the server from the baseline policy plus any agency overrides, so a super admin or agency admin may have changed it from the defaults above._

## Related topics

- [Fleet Overview](fleet-overview.md)
- [Driver Behaviour](driver-behaviour.md)
- [Geofences](geofences.md)
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
