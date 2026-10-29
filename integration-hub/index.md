# Integration Hub — module guide

_Integration Hub_

Where agency data enters UAPTS: upload spreadsheets using locked templates, register live feeds, review every batch and monitor whether data is actually landing.

> 🎬 **Video tutorial:** _coming soon._  
> <!-- VIDEO-URL: integration-hub/index | paste the link here -->

## Pages in this module

| Page | What it shows |
|---|---|
| [Upload & Connect](upload-and-connect.md) | Get a file in, or register how a live feed connects. |
| [Files & Feeds](files-and-feeds.md) | seesAllAgencies       ? 'Every batch submitted, and every live feed connected, across every agency.'       : 'Every batch your agency has submitted, and every live feed it has connected.' |
| [Upload detail](upload-detail.md) | headerSubtitle |
| [Feed detail](feed-detail.md) | source ? `${source.source_system} · ${source.mode} · last synced ${source.last_sync_at ? fmtDate(source.last_sync_at) : 'never'}` : '' |
| [Ingestion Analytics](ingestion-analytics.md) | statsRes?.scope === 'agency' ? 'Is your agency\'s data actually landing, and where is it not?' : 'Is data actually landing everywhere, and where is it not?' |

## Data feeding this module

Upload templates (download from the catalogue):

| Feed ID | Agency | Sheet | Download |
|---|---|---|---|
| `krb-funding` | KRB | Funding Allocation | [xlsx](../data-templates/krb-funding.xlsx) · [csv](../data-templates/krb-funding.csv) |
| `kura-maintenance-work-orders` | KURA | Maintenance Work Orders | [xlsx](../data-templates/kura-maintenance-work-orders.xlsx) · [csv](../data-templates/kura-maintenance-work-orders.csv) |
| `kenha-bridge-register` | KeNHA | Bridge Register | [xlsx](../data-templates/kenha-bridge-register.xlsx) · [csv](../data-templates/kenha-bridge-register.csv) |
| `kenha-maintenance-work-orders` | KeNHA | Maintenance Work Orders | [xlsx](../data-templates/kenha-maintenance-work-orders.xlsx) · [csv](../data-templates/kenha-maintenance-work-orders.csv) |
| `kerra-bridge-register` | KeRRA | Bridge Register | [xlsx](../data-templates/kerra-bridge-register.xlsx) · [csv](../data-templates/kerra-bridge-register.csv) |
| `kerra-maintenance-work-orders` | KeRRA | Maintenance Work Orders | [xlsx](../data-templates/kerra-maintenance-work-orders.xlsx) · [csv](../data-templates/kerra-maintenance-work-orders.csv) |

## Who can use it

Module **M12 · Data Integration Hub**. Agencies with full access in the baseline policy: KENHA, KURA, SDR, SDR_MTD, KRA, KENTRADE, SDT, NTSA, NAMATA, KRC, KPA, KMA, NCTTCA, LAPSSET.

## Support

- **Your agency administrator** is the first contact for access, role and data-quality questions.
- **Data feeds, templates and API questions:** `api-support@uapts.go.ke` (include the `X-Request-ID` response header from a failing call).
- **Security concerns:** `security@uapts.go.ke`. Do not report suspected vulnerabilities publicly.
