# Layer Coverage

_GIS & Spatial Analysis › Layer Coverage_ · Route `/gis/coverage`

**Layer Coverage** lets you see which spatial layers each agency is expected to provide, and where they stand - missing, requested, processing or uploaded.

> 🎬 **Video tutorial:** _coming soon._  
> <!-- VIDEO-URL: gis/layer-coverage | paste the link here, e.g. [Watch the walkthrough](https://…) -->

## Highlights

- **5 headline tiles** — Expected layers, Complete, Missing, In progress, Failed.
- **1 panels** — Agency completeness.
- **Filters and search** to narrow tables to what you need.
- Every figure is traceable to the data feed or upload template that supplies it — see [Data sources and feeds](#data-sources-and-feeds).

## Enabling and access

1. Sign in to UAPTS (see [How to access](../getting-started/how-to-access.md)).
2. In the left sidebar click **GIS & Spatial Analysis**.
3. The page opens at `/gis/coverage`. You can also reach it with the global search (**Ctrl + K**).

This page belongs to module **M13 · GIS**. The route needs at least the **Operator** tier to open it. The sidebar and the global search only list pages your agency and role can open, and a link to a page you cannot reach sends you back to the Command Centre. If a page you expect is missing, ask your agency administrator to check your agency's [Module Access](../access-control/module-access.md).

![Layer Coverage page](../assets/screenshots/gis-coverage.webp)

## Page tour

### Headline tiles


| Tile | What it shows | Data from | Table → ingested via |
|---|---|---|---|
| **Expected layers** | — | `/gis/layer-requirements/`, `/gis/layer-requirements/coverage/`, `/gis/layer-requirements/{id}/` | _GeoLayer, GeoLayerRequest, GeoLayerRequirement_ → no template yet |
| **Complete** | — | `/gis/layer-requirements/`, `/gis/layer-requirements/coverage/`, `/gis/layer-requirements/{id}/` | aggregate of several tables — see [per-table feeds](#data-sources-and-feeds) |
| **Missing** | — | `/gis/layer-requirements/`, `/gis/layer-requirements/coverage/`, `/gis/layer-requirements/{id}/` | aggregate of several tables — see [per-table feeds](#data-sources-and-feeds) |
| **In progress** | — | `/gis/layer-requirements/`, `/gis/layer-requirements/coverage/`, `/gis/layer-requirements/{id}/` | aggregate of several tables — see [per-table feeds](#data-sources-and-feeds) |
| **Failed** | — | `/gis/layer-requirements/`, `/gis/layer-requirements/coverage/`, `/gis/layer-requirements/{id}/` | aggregate of several tables — see [per-table feeds](#data-sources-and-feeds) |

### Agency completeness


Contains a table with the columns **Agency**, **Expected**, **Uploaded**, **Requested**, **Processing**, **Failed**, **Missing**, **Complete**.

**Data from:** `/gis/layer-requirements/`, `/gis/layer-requirements/coverage/`, `/gis/layer-requirements/{id}/`, `/gis/layer-requirements/{id}/request-upload/`  
**Table → ingested via:** _GeoLayerRequest_ → no template yet

## Working with this page

1. Open **GIS & Spatial Analysis → Layer Coverage** from the sidebar.
2. Type in the **“Search layer or agency…”** box to filter what is shown.
3. Click a row to open its detail.

## Data sources and feeds

Every number and table on this page is read from the API endpoints below. The **Ingested via** column says how the underlying records get into UAPTS: a downloadable **upload template** (xlsx/CSV, loaded through the [Integration Hub](../integration-hub/upload-and-connect.md)), a **live feed** that pushes records to the ingest API, or — where neither exists yet — it is stated plainly.

| Endpoint | Records | Ingested via |
|---|---|---|
| `GET /gis/layer-requirements/` | _Aggregate of 7 tables (rows below)_ | — |
| ↳ User | Users | Platform data (accounts / configuration) |
| ↳ Bridge | Bridges | [`kenha-bridge-register`](../data-templates/kenha-bridge-register.xlsx)<br>[`kerra-bridge-register`](../data-templates/kerra-bridge-register.xlsx) |
| ↳ GeoFeature | Geo Features | **No ingestion template yet** — populated by seed data or direct entry |
| ↳ GeoLayer | Geo Layers | **No ingestion template yet** — populated by seed data or direct entry |
| ↳ GeoLayerRequest | Geo Layer Requests | **No ingestion template yet** — populated by seed data or direct entry |
| ↳ GeoLayerRequirement | Geo Layer Requirements | **No ingestion template yet** — populated by seed data or direct entry |
| ↳ GeoPromotionRun | Geo Promotion Runs | **No ingestion template yet** — populated by seed data or direct entry |
| `GET /gis/layer-requirements/coverage/` | _Aggregate of 7 tables (rows below)_ | — |
| ↳ User | Users | Platform data (accounts / configuration) |
| ↳ Bridge | Bridges | [`kenha-bridge-register`](../data-templates/kenha-bridge-register.xlsx)<br>[`kerra-bridge-register`](../data-templates/kerra-bridge-register.xlsx) |
| ↳ GeoFeature | Geo Features | **No ingestion template yet** — populated by seed data or direct entry |
| ↳ GeoLayer | Geo Layers | **No ingestion template yet** — populated by seed data or direct entry |
| ↳ GeoLayerRequest | Geo Layer Requests | **No ingestion template yet** — populated by seed data or direct entry |
| ↳ GeoLayerRequirement | Geo Layer Requirements | **No ingestion template yet** — populated by seed data or direct entry |
| ↳ GeoPromotionRun | Geo Promotion Runs | **No ingestion template yet** — populated by seed data or direct entry |
| `GET /gis/layer-requirements/{id}/` | _Aggregate of 7 tables (rows below)_ | — |
| ↳ User | Users | Platform data (accounts / configuration) |
| ↳ Bridge | Bridges | [`kenha-bridge-register`](../data-templates/kenha-bridge-register.xlsx)<br>[`kerra-bridge-register`](../data-templates/kerra-bridge-register.xlsx) |
| ↳ GeoFeature | Geo Features | **No ingestion template yet** — populated by seed data or direct entry |
| ↳ GeoLayer | Geo Layers | **No ingestion template yet** — populated by seed data or direct entry |
| ↳ GeoLayerRequest | Geo Layer Requests | **No ingestion template yet** — populated by seed data or direct entry |
| ↳ GeoLayerRequirement | Geo Layer Requirements | **No ingestion template yet** — populated by seed data or direct entry |
| ↳ GeoPromotionRun | Geo Promotion Runs | **No ingestion template yet** — populated by seed data or direct entry |
| `GET /gis/layer-requirements/{id}/request-upload/` | _Aggregate of 3 tables (rows below)_ | — |
| ↳ User | Users | Platform data (accounts / configuration) |
| ↳ GeoLayerRequest | Geo Layer Requests | **No ingestion template yet** — populated by seed data or direct entry |
| ↳ GeoLayerRequirement | Geo Layer Requirements | **No ingestion template yet** — populated by seed data or direct entry |

Full details of every template (columns, formats) are in the [Data sources catalogue](../reference/data-sources.md). Interactive API documentation is available at `/api/docs/`.

## Permissions

| Who | What they can do here |
|---|---|
| Public / read-only accounts | No access to this page. |
| Operator | View the page. |
| Analyst | View and **export CSV**. |
| Agency admin | Everything an analyst can do, plus the administrative capabilities listed in [Roles & Permissions](../access-control/roles-and-permissions.md). |
| Super admin | Sees every agency's data. |

**Agencies with the GIS module:** full — KENHA, KURA, KERRA, SDR, SDR_MTD, KWS, SDT, NTSA, NAMATA, KRC, KPA, KMA, NCTTCA, LAPSSET; read-only — KMD.

_Access is evaluated by the server from the baseline policy plus any agency overrides, so a super admin or agency admin may have changed it from the defaults above._

## Related topics

- [GIS Explorer](gis-explorer.md)
- [Layer Overview](layer-overview.md)
- [Layer Catalogue](layer-catalogue.md)
- [Layer analysis](layer-analysis.md)
- [Layer Requests](layer-requests.md)
- [GIS & Spatial Analysis overview](index.md)
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
