# GIS & Spatial Analysis — module guide

_GIS & Spatial Analysis_

A national map explorer for road, rail, public-transport and port layers, plus the catalogue, coverage tracker and upload requests for every agency's spatial layers.

> 🎬 **Video tutorial:** _coming soon._  
> <!-- VIDEO-URL: gis/index | paste the link here -->

## Pages in this module

| Page | What it shows |
|---|---|
| [GIS Explorer](gis-explorer.md) | National road network, PT routes, rail lines, port infrastructure, and UAPTS spatial layers |
| [Layer Overview](layer-overview.md) | One card per expected spatial layer - size, completeness and how it breaks down - for every layer an agency has uploaded |
| [Layer Coverage](layer-coverage.md) | Which spatial layers each agency is expected to provide, and where they stand - missing, requested, processing or uploaded |
| [Layer Catalogue](layer-catalogue.md) | Every spatial layer on the platform - agency uploads and reference layers - with status, size and provenance |
| [Layer analysis](layer-analysis.md) | layer ? `${layer.agency_code || 'Reference'} · ${GEOM_LABEL[layer.geom_type] || 'layer'} · v${layer.version} · updated ${fmtDate(layer.updated_at)}` : 'Loading…' |
| [Layer Requests](layer-requests.md) | Uploads that admins have asked specific people to provide - who, for which layer, by when |

## Data feeding this module

Upload templates (download from the catalogue):

| Feed ID | Agency | Sheet | Download |
|---|---|---|---|
| `kenha-bridge-register` | KeNHA | Bridge Register | [xlsx](../data-templates/kenha-bridge-register.xlsx) · [csv](../data-templates/kenha-bridge-register.csv) |
| `kerra-bridge-register` | KeRRA | Bridge Register | [xlsx](../data-templates/kerra-bridge-register.xlsx) · [csv](../data-templates/kerra-bridge-register.csv) |

## Who can use it

Module **M13 · GIS**. Agencies with full access in the baseline policy: KENHA, KURA, KERRA, SDR, SDR_MTD, KWS, SDT, NTSA, NAMATA, KRC, KPA, KMA, NCTTCA, LAPSSET; read-only: KMD.

## Support

- **Your agency administrator** is the first contact for access, role and data-quality questions.
- **Data feeds, templates and API questions:** `api-support@uapts.go.ke` (include the `X-Request-ID` response header from a failing call).
- **Security concerns:** `security@uapts.go.ke`. Do not report suspected vulnerabilities publicly.
