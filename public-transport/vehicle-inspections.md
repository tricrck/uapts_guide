# Vehicle Inspections

_Public Transport › Vehicle Inspections_ · Route `/public-transport/vehicle-inspections`

**Vehicle Inspections** lets you see roadworthiness inspection records, pass/fail outcomes, re-inspection chains, and inspection-centre/inspector workload. Data on this page comes from NTSA.

> 🎬 **Video tutorial:** _coming soon._  
> <!-- VIDEO-URL: public-transport/vehicle-inspections | paste the link here, e.g. [Watch the walkthrough](https://…) -->

## Highlights

- **10 headline tiles** — Inspections (loaded), Passed, Failed, Conditional Pass, Pass Rate, Re-inspections….
- **1 panels** — Inspection Registry.
- **Refreshes itself every 120 seconds**, so you do not need to reload the page.
- **Filters and search** to narrow tables to what you need.
- Every figure is traceable to the data feed or upload template that supplies it — see [Data sources and feeds](#data-sources-and-feeds).

## Enabling and access

1. Sign in to UAPTS (see [How to access](../getting-started/how-to-access.md)).
2. In the left sidebar expand **Public Transport** and click **Vehicle Inspections**.
3. The page opens at `/public-transport/vehicle-inspections`. You can also reach it with the global search (**Ctrl + K**).

This page belongs to module **M04 · Public Transport**. The sidebar and the global search only list pages your agency and role can open, and a link to a page you cannot reach sends you back to the Command Centre. If a page you expect is missing, ask your agency administrator to check your agency's [Module Access](../access-control/module-access.md).

![Vehicle Inspections page](../assets/screenshots/public-transport-vehicle-inspections.webp)

## Page tour

### Headline tiles

![Vehicle Inspections headline tiles](../assets/screenshots/public-transport-vehicle-inspections--kpis.webp)

| Tile | What it shows | Data from | Table → ingested via |
|---|---|---|---|
| **Inspections (loaded)** | Most recent records _(window: LIVE)_ | `/fleet/vehicle-inspections/`, `/fleet/vehicle-inspections/{id}/reinspections/` | _VehicleInspection_ → no template yet |
| **Passed** | Roadworthy _(window: LIVE)_ | — | — |
| **Failed** | Not roadworthy _(window: LIVE)_ | — | — |
| **Conditional Pass** | Passed with conditions _(window: LIVE)_ | — | — |
| **Pass Rate** | Pass / (pass + fail) _(window: LIVE)_ | — | — |
| **Re-inspections** | Follow-up records _(window: LIVE)_ | `/fleet/vehicle-inspections/`, `/fleet/vehicle-inspections/{id}/reinspections/` | _VehicleInspection_ → no template yet |
| **Overdue** | Next inspection due date passed _(window: LIVE)_ | `/fleet/vehicle-inspections/`, `/fleet/vehicle-inspections/{id}/reinspections/` | _VehicleInspection_ → no template yet |
| **Due ≤30d** | Next inspection approaching _(window: 30D)_ | `/fleet/vehicle-inspections/`, `/fleet/vehicle-inspections/{id}/reinspections/` | _VehicleInspection_ → no template yet |
| **Active Centres** | Distinct inspection centres _(window: LIVE)_ | `/fleet/vehicle-inspections/`, `/fleet/vehicle-inspections/{id}/reinspections/` | _VehicleInspection_ → no template yet |
| **Active Inspectors** | Distinct inspectors on file _(window: LIVE)_ | `/fleet/vehicle-inspections/`, `/fleet/vehicle-inspections/{id}/reinspections/` | _VehicleInspection_ → no template yet |

### Inspection Registry


Contains a table with the columns **Vehicle**, **Centre**, **Inspector**, **Inspected**, **Result**, **Sticker No.**, **Next Due**, **Re-inspection**, **Report**.

**Data from:** `/fleet/vehicle-inspections/`, `/fleet/vehicle-inspections/{id}/reinspections/`  
**Table → ingested via:** _VehicleInspection_ → no template yet

## Working with this page

1. Open **Public Transport → Vehicle Inspections** from the sidebar.
2. Wait for the page to finish loading. It re-fetches its data every **120 s**; the figures you see are the latest the platform holds, not a one-time snapshot.
3. Type in the **“Search plate / centre / inspector…”** box to filter what is shown.
4. Use the **All results** drop-down to narrow the list. Choices include: Pass, Fail, Conditional pass.
5. Click a row to open its detail.
6. Click **Apply** to use this action.

## Status and value meanings

These are the values the platform stores for the fields shown on this page (`value` followed by the label you see).

| Field | Table | Values |
|---|---|---|
| result | VehicleInspection | `pass` · `fail` · `conditional_pass` |

## Data sources and feeds

Every number and table on this page is read from the API endpoints below. The **Ingested via** column says how the underlying records get into UAPTS: a downloadable **upload template** (xlsx/CSV, loaded through the [Integration Hub](../integration-hub/upload-and-connect.md)), a **live feed** that pushes records to the ingest API, or — where neither exists yet — it is stated plainly.

| Endpoint | Records | Ingested via |
|---|---|---|
| `GET /fleet/vehicle-inspections/` | Vehicle Inspections | **No ingestion template yet** — populated by seed data or direct entry |
| `GET /fleet/vehicle-inspections/{id}/reinspections/` | Vehicle Inspections | **No ingestion template yet** — populated by seed data or direct entry |

Full details of every template (columns, formats) are in the [Data sources catalogue](../reference/data-sources.md). Interactive API documentation is available at `/api/docs/`.

## Permissions

| Who | What they can do here |
|---|---|
| Public / read-only accounts | View the page where the module is enabled for their agency (read-only). |
| Operator | View the page. |
| Analyst | View and **export CSV**. |
| Agency admin | Everything an analyst can do, plus the administrative capabilities listed in [Roles & Permissions](../access-control/roles-and-permissions.md). |
| Super admin | Sees every agency's data. |

**Agencies with the Public Transport module:** full — KURA, SDT, NTSA, NAMATA; selected pages only — COUNTY_GOV.

_Access is evaluated by the server from the baseline policy plus any agency overrides, so a super admin or agency admin may have changed it from the defaults above._

## Related topics

- [Operations Overview](operations-overview.md)
- [PSV Compliance](psv-compliance.md)
- [BRT Stops & Headway](brt-stops-headway.md)
- [Public Operators](public-operators.md)
- [Vehicle Registration](vehicle-registration.md)
- [Driver Licensing](driver-licensing.md)
- [Public Transport overview](index.md)
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
