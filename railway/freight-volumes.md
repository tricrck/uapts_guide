# Freight Volumes

_Railway › Freight Volumes_ · Route `/railway/freight`

**Freight Operations** lets you see freight manifests, corridor analysis, KenTrade single-window clearances, NCTTCA transit tracking, and KPA port-rail reconciliation. Data on this page comes from KRC, KPA, KenTrade and NCTTCA.

> 🎬 **Video tutorial:** _coming soon._  
> <!-- VIDEO-URL: railway/freight-volumes | paste the link here, e.g. [Watch the walkthrough](https://…) -->

## Highlights

- **6 headline tiles** — Total Shipments, Total Tonnage, Total Revenue, Avg Wagons/Shipment, Port-Rail Manifests, Transit Manifests.
- **5 panels** — Cargo Type Mix, Top Freight Corridors (), Port-Rail Container Reconciliation, Intermodal Transfer Analysis, Freight Manifest Log.
- **Refreshes itself every 120 seconds**, so you do not need to reload the page.
- **Export to CSV** for the rows you are looking at (Analyst tier and above).
- **Filters and search** to narrow tables to what you need.
- Every figure is traceable to the data feed or upload template that supplies it — see [Data sources and feeds](#data-sources-and-feeds).

## Enabling and access

1. Sign in to UAPTS (see [How to access](../getting-started/how-to-access.md)).
2. In the left sidebar expand **Railway** and click **Freight Volumes**.
3. The page opens at `/railway/freight`. You can also reach it with the global search (**Ctrl + K**).

This page belongs to module **M08 · Railway**. The route needs at least the **Operator** tier to open it. The sidebar and the global search only list pages your agency and role can open, and a link to a page you cannot reach sends you back to the Command Centre. If a page you expect is missing, ask your agency administrator to check your agency's [Module Access](../access-control/module-access.md).

![Freight Volumes page](../assets/screenshots/railway-freight.webp)

## Page tour

### Headline tiles


| Tile | What it shows | Data from | Table → ingested via |
|---|---|---|---|
| **Total Shipments** | Manifests in view | `/railway/freight/` | _FreightManifest_ → no template yet |
| **Total Tonnage** | Freight tonne-km | `/railway/freight/` | _FreightManifest_ → no template yet |
| **Total Revenue** | Freight revenue | `/railway/freight/` | _FreightManifest_ → no template yet |
| **Avg Wagons/Shipment** | Average wagon count | `/railway/freight/` | _FreightManifest_ → no template yet |
| **Port-Rail Manifests** | Rail-nominated containers (KPA) | `/railway/freight/` | _FreightManifest_ → no template yet |
| **Transit Manifests** | From port of origin | `/railway/freight/` | _FreightManifest_ → no template yet |

### Cargo Type Mix


**Data from:** `/railway/freight/`  
**Table → ingested via:** _FreightManifest_ → no template yet

### Top Freight Corridors ()


**Data from:** `/railway/freight/by-corridor/`  
**Table → ingested via:** _FreightManifest_ → no template yet

### Port-Rail Container Reconciliation


Contains a table with the columns **Manifest Ref**, **Customs Ref (KPA)**, **Port of Origin**, **Cargo Type**, **Tonnage**, **Wagons**, **Route**, **Operator**, **Dispatched**, **Arrived**.

**Data from:** `/railway/freight/`  
**Table → ingested via:** _FreightManifest_ → no template yet

### Intermodal Transfer Analysis


Contains a table with the columns **Port of Origin**, **Manifests**, **Tonnage**, **Avg Transit Time**, **Pending Arrival**.

**Data from:** `/railway/freight/`  
**Table → ingested via:** _FreightManifest_ → no template yet

### Freight Manifest Log


Contains a table with the columns **Manifest Ref**, **Cargo Type**, **Tonnage**, **Wagons**, **Route**, **Train**, **Revenue (KES)**, **Dispatched**, **Arrived**.

**Data from:** `/railway/freight/`  
**Table → ingested via:** _FreightManifest_ → no template yet

## Working with this page

1. Open **Railway → Freight Volumes** from the sidebar.
2. Wait for the page to finish loading. It re-fetches its data every **120 s**; the figures you see are the latest the platform holds, not a one-time snapshot.
3. Type in the **“Search manifest / route…”** box to filter what is shown.
4. Use the **All cargo types** drop-down to narrow the list. Choices include: Container, Bulk Fuel, Bulk Cement, Grain, General, Vehicle.
5. Click a row to open its detail.
6. Click **Export CSV** to download the rows currently loaded (after filters). The button only appears for Analyst tier and above.

## Status and value meanings

These are the values the platform stores for the fields shown on this page (`value` followed by the label you see).

| Field | Table | Values |
|---|---|---|
| cargo type | FreightManifest | `container` · `bulk_fuel` · `bulk_cement` Bulk cement / clinker · `grain` · `general` General goods · `vehicle` Vehicles · `steel` Steel / metals · `other` |

## Data sources and feeds

Every number and table on this page is read from the API endpoints below. The **Ingested via** column says how the underlying records get into UAPTS: a downloadable **upload template** (xlsx/CSV, loaded through the [Integration Hub](../integration-hub/upload-and-connect.md)), a **live feed** that pushes records to the ingest API, or — where neither exists yet — it is stated plainly.

| Endpoint | Records | Ingested via |
|---|---|---|
| `GET /railway/freight/` | Freight Manifests | **No ingestion template yet** — populated by seed data or direct entry |
| `GET /railway/freight/by-corridor/` | Freight Manifests | **No ingestion template yet** — populated by seed data or direct entry |

Full details of every template (columns, formats) are in the [Data sources catalogue](../reference/data-sources.md). Interactive API documentation is available at `/api/docs/`.

## Permissions

| Who | What they can do here |
|---|---|
| Public / read-only accounts | No access to this page. |
| Operator | View the page. |
| Analyst | View and **export CSV**. |
| Agency admin | Everything an analyst can do, plus the administrative capabilities listed in [Roles & Permissions](../access-control/roles-and-permissions.md). |
| Super admin | Sees every agency's data. |

**Agencies with the Railway module:** full — SDT, KRC; selected pages only — KENHA, NAMATA, KPA, NCTTCA, LAPSSET.

_Access is evaluated by the server from the baseline policy plus any agency overrides, so a super admin or agency admin may have changed it from the defaults above._

## Related topics

- [Railway Overview](railway-overview.md)
- [Train Operations](train-operations.md)
- [Schedules](schedules.md)
- [Rail Infrastructure](rail-infrastructure.md)
- [Rail Network Inventory](rail-network-inventory.md)
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
