# Traffic Alerts

_Road Traffic Management › Traffic Alerts_ · Route `/traffic/alerts`

**Traffic Alerts** lets you see active traffic alerts, congestion events, KMD weather warnings, and NCTTCA corridor risk forecasts. Data on this page comes from KeNHA, KURA, KMD and NCTTCA.

> 🎬 **Video tutorial:** _coming soon._  
> <!-- VIDEO-URL: traffic/traffic-alerts | paste the link here, e.g. [Watch the walkthrough](https://…) -->

## Highlights

- **6 headline tiles** — Active Alerts, Critical, Warning, Active Congestion Events, Forecast Risk Events, Resolved (all).
- **2 panels** — Alert Log, Upcoming Congestion Risk.
- **Refreshes itself every 60 seconds**, so you do not need to reload the page.
- **Filters and search** to narrow tables to what you need.
- Every figure is traceable to the data feed or upload template that supplies it — see [Data sources and feeds](#data-sources-and-feeds).

## Enabling and access

1. Sign in to UAPTS (see [How to access](../getting-started/how-to-access.md)).
2. In the left sidebar expand **Road Traffic Management** and click **Traffic Alerts**.
3. The page opens at `/traffic/alerts`. You can also reach it with the global search (**Ctrl + K**).

This page belongs to module **M02 · Road Traffic**. The sidebar and the global search only list pages your agency and role can open, and a link to a page you cannot reach sends you back to the Command Centre. If a page you expect is missing, ask your agency administrator to check your agency's [Module Access](../access-control/module-access.md).

![Traffic Alerts page](../assets/screenshots/traffic-alerts.webp)

## Page tour

### Headline tiles

![Traffic Alerts headline tiles](../assets/screenshots/traffic-alerts--kpis.webp)

| Tile | What it shows | Data from | Table → ingested via |
|---|---|---|---|
| **Active Alerts** | Unresolved right now _(window: LIVE)_ | `/traffic/alerts/` | _TrafficAlert_ → computed by UAPTS |
| **Critical** | Immediate action needed _(window: LIVE)_ | `/traffic/alerts/` | _TrafficAlert_ → computed by UAPTS |
| **Warning** | Monitor closely _(window: LIVE)_ | `/traffic/alerts/` | _TrafficAlert_ → computed by UAPTS |
| **Active Congestion Events** | Network congestion live _(window: LIVE)_ | `/traffic/congestion-events/active/` | _CongestionEvent_ → live telemetry push (no template yet) |
| **Forecast Risk Events** | Predicted congestion in 12h _(window: 12H)_ | `/traffic/congestion-events/active/`, `/traffic/forecasts/` | _CongestionEvent, TrafficForecast_ → live telemetry push (no template yet) |
| **Resolved (all)** | Cleared alerts in log _(window: ALL)_ | `/traffic/alerts/` | _TrafficAlert_ → computed by UAPTS |

### Alert Log


Contains a table with the columns **Title**, **Type**, **Severity**, **Segment**, **Status**, **Issued**, **Resolved**, **Avg Speed (km/h)**, **Delay (min)**, **Impact (km)**, **Expected Duration**, **Started**.

**Data from:** `/traffic/alerts/`, `/traffic/congestion-events/active/`  
**Table → ingested via:** _TrafficAlert, CongestionEvent_ → computed by UAPTS

### Upcoming Congestion Risk


Contains a table with the columns **Segment**, **Model**, **Target Time**, **Predicted Congestion**, **Predicted Volume**, **Predicted Speed (km/h)**, **Horizon**.

**Data from:** `/traffic/congestion-events/active/`, `/traffic/forecasts/`  
**Table → ingested via:** _CongestionEvent, TrafficForecast_ → live telemetry push (no template yet)

## Working with this page

1. Open **Road Traffic Management → Traffic Alerts** from the sidebar.
2. Wait for the page to finish loading. It re-fetches its data every **60 s**; the figures you see are the latest the platform holds, not a one-time snapshot.
3. Use the **All severities** drop-down to narrow the list. Choices include: Critical, Warning, Info.
4. Use the **All types** drop-down to narrow the list. Choices include: Congestion, Incident, Weather, Road Closure.
5. Click **↻ Refresh** to refresh the data.

## Status and value meanings

These are the values the platform stores for the fields shown on this page (`value` followed by the label you see).

| Field | Table | Values |
|---|---|---|
| alert type | TrafficAlert | `congestion` · `incident` · `weather` · `road_closure` |
| severity | TrafficAlert | `info` · `warning` · `critical` |
| severity | CongestionEvent | `low` · `medium` · `high` · `critical` |
| status | CongestionEvent | `active` · `cleared` · `scheduled` |
| model name | TrafficForecast | `arima` · `lstm` · `gradient_boost` · `timesfm` TimesFM (foundation model) |

## Data sources and feeds

Every number and table on this page is read from the API endpoints below. The **Ingested via** column says how the underlying records get into UAPTS: a downloadable **upload template** (xlsx/CSV, loaded through the [Integration Hub](../integration-hub/upload-and-connect.md)), a **live feed** that pushes records to the ingest API, or — where neither exists yet — it is stated plainly.

| Endpoint | Records | Ingested via |
|---|---|---|
| `GET /traffic/alerts/` | Traffic Alerts | Computed by UAPTS from other data (no direct feed) |
| `GET /traffic/alerts/{id}/resolve/` | Traffic Alerts | Computed by UAPTS from other data (no direct feed) |
| `GET /traffic/congestion-events/active/` | Congestion Events | Live telemetry — push via `POST /api/v1/integrations/<source_id>/ingest/`; **no template or handler yet** |
| `GET /traffic/forecasts/` | Traffic Forecasts | Computed by UAPTS from other data (no direct feed) |

Full details of every template (columns, formats) are in the [Data sources catalogue](../reference/data-sources.md). Interactive API documentation is available at `/api/docs/`.

## Permissions

| Who | What they can do here |
|---|---|
| Public / read-only accounts | View the page where the module is enabled for their agency (read-only). |
| Operator | View the page. |
| Analyst | View and **export CSV**. |
| Agency admin | Everything an analyst can do, plus the administrative capabilities listed in [Roles & Permissions](../access-control/roles-and-permissions.md). |
| Super admin | Sees every agency's data. |

**Agencies with the Road Traffic module:** full — KENHA, KURA, KERRA, SDR, SDT, NAMATA; read-only — COUNTY_GOV, KRB, NPS; selected pages only — KMD, NTSA, NCTTCA.

_Access is evaluated by the server from the baseline policy plus any agency overrides, so a super admin or agency admin may have changed it from the defaults above._

## Related topics

- [Live Traffic Map](live-traffic-map.md)
- [Traffic Analytics](traffic-analytics.md)
- [Road Traffic Management overview](index.md)
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
