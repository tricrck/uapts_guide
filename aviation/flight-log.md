# Flight Log

_Aviation › Flight Log_ · Route `/aviation/flights`

**Flight Movements** lets you see full flight-by-flight log with delay, passenger and cargo detail. Data on this page comes from KAA ATC.

> 🎬 **Video tutorial:** _coming soon._  
> <!-- VIDEO-URL: aviation/flight-log | paste the link here, e.g. [Watch the walkthrough](https://…) -->

## Highlights

- **4 headline tiles** — Flights Loaded, Delayed, Cancelled, Avg Departure Delay.
- **1 panels** — Flight Log.
- **Refreshes itself every 120 seconds**, so you do not need to reload the page.
- **Export to CSV** for the rows you are looking at (Analyst tier and above).
- **Filters and search** to narrow tables to what you need.
- Every figure is traceable to the data feed or upload template that supplies it — see [Data sources and feeds](#data-sources-and-feeds).

## Enabling and access

1. Sign in to UAPTS (see [How to access](../getting-started/how-to-access.md)).
2. In the left sidebar expand **Aviation** and click **Flight Log**.
3. The page opens at `/aviation/flights`. You can also reach it with the global search (**Ctrl + K**).

This page belongs to module **M07a · Aviation**. The sidebar and the global search only list pages your agency and role can open, and a link to a page you cannot reach sends you back to the Command Centre. If a page you expect is missing, ask your agency administrator to check your agency's [Module Access](../access-control/module-access.md).

![Flight Log page](../assets/screenshots/aviation-flights.webp)

## Page tour

### Headline tiles


| Tile | What it shows | Data from | Table → ingested via |
|---|---|---|---|
| **Flights Loaded** | — | `/aviation-maritime/aviation/flights/` | _Flight_ → [`kaa-flight-movements`](../data-templates/kaa-flight-movements.xlsx)<br>live feed `kaa-aodb` |
| **Delayed** | Departure delay > 0 | `/aviation-maritime/aviation/flights/` | _Flight_ → [`kaa-flight-movements`](../data-templates/kaa-flight-movements.xlsx)<br>live feed `kaa-aodb` |
| **Cancelled** | This window | `/aviation-maritime/aviation/flights/` | _Flight_ → [`kaa-flight-movements`](../data-templates/kaa-flight-movements.xlsx)<br>live feed `kaa-aodb` |
| **Avg Departure Delay** | All loaded flights | `/aviation-maritime/aviation/flights/` | _Flight_ → [`kaa-flight-movements`](../data-templates/kaa-flight-movements.xlsx)<br>live feed `kaa-aodb` |

### Flight Log


Contains a table with the columns **Flight**, **Airline**, **Route**, **Status**, **Dep Delay**, **Arr Delay**, **Passengers**, **Gate**.

**Data from:** `/aviation-maritime/aviation/airlines/`, `/aviation-maritime/aviation/flights/`  
**Table → ingested via:** _Airline, Flight_ → [`kaa-flight-movements`](../data-templates/kaa-flight-movements.xlsx)<br>[`kcaa-airline-register`](../data-templates/kcaa-airline-register.xlsx)<br>live feed `kaa-aodb`

## Working with this page

1. Open **Aviation → Flight Log** from the sidebar.
2. Wait for the page to finish loading. It re-fetches its data every **120 s**; the figures you see are the latest the platform holds, not a one-time snapshot.
3. Type in the **“Search flight no. / route…”** box to filter what is shown.
4. Use the **All statuses** drop-down to narrow the list. Choices include: In Flight, Delayed, Cancelled, Landed, Scheduled.
5. Click a row to open its detail.
6. Click **Export CSV** to download the rows currently loaded (after filters). The button only appears for Analyst tier and above.

## Status and value meanings

These are the values the platform stores for the fields shown on this page (`value` followed by the label you see).

| Field | Table | Values |
|---|---|---|
| status | Flight | `scheduled` · `boarding` · `departed` · `in_flight` · `landed` · `arrived` Arrived (gate) · `delayed` · `cancelled` · `diverted` |

## Data sources and feeds

Every number and table on this page is read from the API endpoints below. The **Ingested via** column says how the underlying records get into UAPTS: a downloadable **upload template** (xlsx/CSV, loaded through the [Integration Hub](../integration-hub/upload-and-connect.md)), a **live feed** that pushes records to the ingest API, or — where neither exists yet — it is stated plainly.

| Endpoint | Records | Ingested via |
|---|---|---|
| `GET /aviation-maritime/aviation/airlines/` | Airlines | [`kcaa-airline-register`](../data-templates/kcaa-airline-register.xlsx) |
| `GET /aviation-maritime/aviation/flights/` | Flights | [`kaa-flight-movements`](../data-templates/kaa-flight-movements.xlsx)<br>live feed `kaa-aodb` (KAA AODB) |

Full details of every template (columns, formats) are in the [Data sources catalogue](../reference/data-sources.md). Interactive API documentation is available at `/api/docs/`.

## Permissions

| Who | What they can do here |
|---|---|
| Public / read-only accounts | View the page where the module is enabled for their agency (read-only). |
| Operator | View the page. |
| Analyst | View and **export CSV**. |
| Agency admin | Everything an analyst can do, plus the administrative capabilities listed in [Roles & Permissions](../access-control/roles-and-permissions.md). |
| Super admin | Sees every agency's data. |

**Agencies with the Aviation module:** full — KAA, KCAA, SDT.

_Access is evaluated by the server from the baseline policy plus any agency overrides, so a super admin or agency admin may have changed it from the defaults above._

## Related topics

- [Overview](aviation-overview.md)
- [Flight Movements](flight-movements.md)
- [Passenger Stats](passenger-stats.md)
- [Aircraft Licencing](aircraft-licencing.md)
- [Aviation Infrastructure](aviation-infrastructure.md)
- [Aviation overview](index.md)
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
