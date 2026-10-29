# UAPTS User Guide

_Unified Analytics and Predictive Transport System — help for users, analysts and administrators._

Start with **[Welcome](getting-started/welcome.md)**, then pick a module from the menu ([`_sidebar.md`](_sidebar.md)). Open **`index.html`** in a browser for the full menu, search box and “On this page” index.

## Modules

| Module | What it is for |
|---|---|
| [Command Centre](command-centre/index.md) | The Command Centre is the landing page after sign-in. Ministry and platform users see the National view; agency users see their own Agency view; and an administrator can assign a custom dashboard to an agency, department, role or person. |
| [Road Traffic Management](traffic/index.md) | Live and historical traffic on the national road network: counting-station health, congestion events, speed compliance, vehicle mix, weather impact, origin–destination flows and short-term forecasts. |
| [Fleet & Vehicle Tracking](fleet/index.md) | Tracks public-service and government vehicles: utilisation, speed-governor compliance, driver behaviour, live GPS positions, geofence breaches and historical trip replay. |
| [Public Transport](public-transport/index.md) | Operational and regulatory view of public transport: BRT, PSV licensing and compliance, operators, vehicle registration and inspection, and driver licensing. |
| [Safety & Incidents](safety/index.md) | Road-safety intelligence: national KPIs, active incidents and emergency dispatch, accident black spots and predictive hotspots, and traffic-violation trends. |
| [Road Infrastructure](infrastructure/index.md) | Road network inventory and condition, construction and maintenance programmes, bridges and roadside assets, and funding allocations by agency and fiscal year. |
| [Aviation](aviation/index.md) | Airport and airline operations: flight movements, on-time performance, passenger and cargo volumes, aircraft and operator licensing, and aviation infrastructure. |
| [Maritime](maritime/index.md) | Ports and shipping: vessel traffic and registry, berth and port operations, cargo and trade flows, waterways, maritime safety, green-transport indicators and port performance ranking. |
| [Railway](railway/index.md) | SGR and MGR rail operations: train positions and delays, freight volumes and port-rail reconciliation, timetables, track and signalling assets, network inventory and rail safety. |
| [Corridor & Trade](corridor/index.md) | Northern Corridor and LAPSSET trade data: transit declarations, one-stop border-post performance, corridor KPIs and corridor development. |
| [Analytics & Reporting](analytics-reporting/index.md) | Predictive models, ad-hoc querying and report generation across all modules. |
| [Integration Hub](integration-hub/index.md) | Where agency data enters UAPTS: upload spreadsheets using locked templates, register live feeds, review every batch and monitor whether data is actually landing. |
| [GIS & Spatial Analysis](gis/index.md) | A national map explorer for road, rail, public-transport and port layers, plus the catalogue, coverage tracker and upload requests for every agency's spatial layers. |
| [Training Institutes](training/index.md) | Accredited transport and safety training: course catalogue, cohorts, enrolments and certificates. |
| [Notifications](notifications/index.md) | Real-time alerts from every module, and the rules that decide who is alerted and when. |
| [Access Control](access-control/index.md) | Manage who can sign in and what they can reach: agencies, users, roles, module access, custom dashboards and the audit trail. |

## Every page follows the same pattern

Summary and highlights → Enabling and access → Page tour (a screenshot of every section; for every tile, chart and table the **API endpoint** and the **upload template or live feed** behind it) → Working with this page (numbered steps) → Status and value meanings → Data sources and feeds → Permissions → Related topics → On this page → Support.

## Quick links

- [Data sources catalogue](reference/data-sources.md) — all 86 upload templates (xlsx + csv), live feeds, and tables with no feed yet
- [API endpoint index](reference/api-endpoints.md)
- [Troubleshooting](reference/troubleshooting.md) · [Glossary](reference/glossary.md) · [Video tutorial index](reference/video-index.md)

## Maintaining this guide

- **Markdown (`*.md`) is the source.** Edit it directly. The `*.html` files beside it are generated: run `python3 docs/guide/_tools/build_site.py` (needs `pip install markdown`).
- **Videos:** on each page replace `_coming soon._` and the `<!-- VIDEO-URL: … -->` comment with your link, then tick the page in the [video index](reference/video-index.md).
- **Screenshots** are in `assets/screenshots/` (WebP). They were captured from the web app at 1440×900 from `uapts_frontend_v2.3` against a throw-away demo database seeded with `python -m seeds`, so figures are demo data. The top-bar clock shows East Africa Time. Replace a file with the same name to refresh it.
- **Templates** in `data-templates/` were generated from `apps/integrations` (`build_template_workbook`). If a template changes, regenerate it so the guide stays in step.
- Endpoint, table and feed links were derived from the frontend code (`frontend_konza/app`) and the backend registry; the widget-to-endpoint match is best-effort, so review it when a page changes.
