# LAPSSET Corridor

_Corridor & Trade › LAPSSET Corridor_ · Route `/corridor/lapsset`

**LAPSSET Corridor** lets you see lamu Port – South Sudan – Ethiopia Transport corridor - port operations, highway and railway construction, and investment against plan.

> 🎬 **Video tutorial:** _coming soon._  
> <!-- VIDEO-URL: corridor/lapsset-corridor | paste the link here, e.g. [Watch the walkthrough](https://…) -->

## Highlights

- **3 panels** — Construction and investment progress, Trend, Against the Northern Corridor.
- **Filters and search** to narrow tables to what you need.
- Every figure is traceable to the data feed or upload template that supplies it — see [Data sources and feeds](#data-sources-and-feeds).

## Enabling and access

1. Sign in to UAPTS (see [How to access](../getting-started/how-to-access.md)).
2. In the left sidebar expand **Corridor & Trade** and click **LAPSSET Corridor**.
3. The page opens at `/corridor/lapsset`. You can also reach it with the global search (**Ctrl + K**).

This page belongs to module **M15 · Corridor and Trade**. The sidebar and the global search only list pages your agency and role can open, and a link to a page you cannot reach sends you back to the Command Centre. If a page you expect is missing, ask your agency administrator to check your agency's [Module Access](../access-control/module-access.md).

![LAPSSET Corridor page](../assets/screenshots/corridor-lapsset.webp)

## Page tour

### Construction and investment progress

![Construction and investment progress](../assets/screenshots/corridor-lapsset--construction-and-investment-progress.webp)

**Data from:** `/corridor/kpis/series/`  
**Table → ingested via:** _CorridorKPIValue_ → [`lapsset-corridor-kpis`](../data-templates/lapsset-corridor-kpis.xlsx)<br>[`ncttca-corridor-kpis`](../data-templates/ncttca-corridor-kpis.xlsx)

### Trend

![Trend](../assets/screenshots/corridor-lapsset--trend.webp)

Contains a chart.

**Data from:** `/corridor/kpis/series/`  
**Table → ingested via:** _CorridorKPIValue_ → [`lapsset-corridor-kpis`](../data-templates/lapsset-corridor-kpis.xlsx)<br>[`ncttca-corridor-kpis`](../data-templates/ncttca-corridor-kpis.xlsx)

### Against the Northern Corridor


Contains a table with the columns **Indicator**, **LAPSSET**, **Northern**, **LAPSSET as % of Northern**.

**Data from:** `/corridor/corridors/compare/`  
**Table → ingested via:** _Corridor_ → no template yet

## Working with this page

1. Open **Corridor & Trade → LAPSSET Corridor** from the sidebar.
2. Scroll down to move through the panels; every panel has a heading matching those in the Page tour.

## Data sources and feeds

Every number and table on this page is read from the API endpoints below. The **Ingested via** column says how the underlying records get into UAPTS: a downloadable **upload template** (xlsx/CSV, loaded through the [Integration Hub](../integration-hub/upload-and-connect.md)), a **live feed** that pushes records to the ingest API, or — where neither exists yet — it is stated plainly.

| Endpoint | Records | Ingested via |
|---|---|---|
| `GET /corridor/corridors/compare/` | Corridors | **No ingestion template yet** — populated by seed data or direct entry |
| `GET /corridor/kpis/series/` | Corridor Kpi Values | [`lapsset-corridor-kpis`](../data-templates/lapsset-corridor-kpis.xlsx)<br>[`ncttca-corridor-kpis`](../data-templates/ncttca-corridor-kpis.xlsx) |

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
- [Border Crossings](border-crossings.md)
- [Transit Declarations](transit-declarations.md)
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
