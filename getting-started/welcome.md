# Welcome to UAPTS

_Getting started › Welcome_

**UAPTS — the Unified Analytics and Predictive Transport System** — brings the data of Kenya's transport agencies into one place: roads, public transport, rail, maritime and aviation. Each agency keeps ownership of its data; UAPTS collects it, checks it, and shows it as live dashboards, maps, forecasts and reports for planners, regulators, operators and analysts.

> 🎬 **Video tutorial:** _coming soon._  
> <!-- VIDEO-URL: getting-started/welcome | paste the link here, e.g. [Watch the walkthrough](https://…) -->

## Who this guide is for

- **Operators and officers** who monitor traffic, fleets, incidents, ports, rail and flights day to day.
- **Analysts** who explore data, run the Query Builder, use forecasts and generate reports.
- **Agency administrators** who manage their agency's users, upload data and register live feeds.
- **Super administrators** who oversee every agency, the data feeds and the audit trail.

## How the guide is organised

The left-hand menu of this guide follows the **sidebar of the UAPTS web application**, group by group. Each page of the guide matches one screen of the application and always follows the same pattern:

- A short **summary** and a list of **highlights**.
- **Enabling and access** — how to open the screen and who may see it.
- A **Page tour** with a screenshot of every section, and for every tile, chart and table: which **API endpoint** supplies it and which **upload template or live feed** loads the underlying records.
- **Working with this page** — numbered steps.
- **Status and value meanings**, **Permissions**, **Related topics**, an **On this page** index and **Support** contacts.

## Where the data comes from

Nothing on a UAPTS screen is typed in by the page itself. Records reach the platform in one of three ways, and the guide names the route for each data point:

| Route | What it looks like | Where to find it |
|---|---|---|
| **Upload template** | An agency fills a locked Excel/CSV template and uploads it in the Integration Hub. Rows are validated, previewed and committed. | [Data sources catalogue](../reference/data-sources.md) — every template can be downloaded as `.xlsx` or `.csv`. |
| **Live feed** | A system such as KeNHA's counting stations or NTSA iTIMS pushes records to the ingest API with an API key. | [Integration Hub → Upload & Connect](../integration-hub/upload-and-connect.md) |
| **Computed by UAPTS** | Forecasts, black spots, alerts and scores are calculated from other data. | Marked _“computed by UAPTS”_ in the Data sources tables. |

Where a table has **no template or live feed yet**, the guide says so plainly (_“no template yet”_). The full list is in the [Data sources catalogue](../reference/data-sources.md#tables-without-an-ingestion-template-yet).

## The modules

| Module | What it is for |
|---|---|
| [Command Centre](../command-centre/index.md) | The Command Centre is the landing page after sign-in. Ministry and platform users see the National view; agency users see their own Agency view; and an administrator can assign a custom dashboard to an agency, department, role or person. |
| [Road Traffic Management](../traffic/index.md) | Live and historical traffic on the national road network: counting-station health, congestion events, speed compliance, vehicle mix, weather impact, origin–destination flows and short-term forecasts. |
| [Fleet & Vehicle Tracking](../fleet/index.md) | Tracks public-service and government vehicles: utilisation, speed-governor compliance, driver behaviour, live GPS positions, geofence breaches and historical trip replay. |
| [Public Transport](../public-transport/index.md) | Operational and regulatory view of public transport: BRT, PSV licensing and compliance, operators, vehicle registration and inspection, and driver licensing. |
| [Safety & Incidents](../safety/index.md) | Road-safety intelligence: national KPIs, active incidents and emergency dispatch, accident black spots and predictive hotspots, and traffic-violation trends. |
| [Road Infrastructure](../infrastructure/index.md) | Road network inventory and condition, construction and maintenance programmes, bridges and roadside assets, and funding allocations by agency and fiscal year. |
| [Aviation](../aviation/index.md) | Airport and airline operations: flight movements, on-time performance, passenger and cargo volumes, aircraft and operator licensing, and aviation infrastructure. |
| [Maritime](../maritime/index.md) | Ports and shipping: vessel traffic and registry, berth and port operations, cargo and trade flows, waterways, maritime safety, green-transport indicators and port performance ranking. |
| [Railway](../railway/index.md) | SGR and MGR rail operations: train positions and delays, freight volumes and port-rail reconciliation, timetables, track and signalling assets, network inventory and rail safety. |
| [Corridor & Trade](../corridor/index.md) | Northern Corridor and LAPSSET trade data: transit declarations, one-stop border-post performance, corridor KPIs and corridor development. |
| [Analytics & Reporting](../analytics-reporting/index.md) | Predictive models, ad-hoc querying and report generation across all modules. |
| [Integration Hub](../integration-hub/index.md) | Where agency data enters UAPTS: upload spreadsheets using locked templates, register live feeds, review every batch and monitor whether data is actually landing. |
| [GIS & Spatial Analysis](../gis/index.md) | A national map explorer for road, rail, public-transport and port layers, plus the catalogue, coverage tracker and upload requests for every agency's spatial layers. |
| [Training Institutes](../training/index.md) | Accredited transport and safety training: course catalogue, cohorts, enrolments and certificates. |
| [Notifications](../notifications/index.md) | Real-time alerts from every module, and the rules that decide who is alerted and when. |
| [Access Control](../access-control/index.md) | Manage who can sign in and what they can reach: agencies, users, roles, module access, custom dashboards and the audit trail. |

## Roles at a glance

| Role | Typical use |
|---|---|
| Public | Read-only access to published dashboards. |
| Operator | Day-to-day operations: acknowledge alerts, update incidents, submit uploads. |
| Analyst | Everything an operator can read, plus export, Query Builder and reports. |
| Admin | Manages the agency's users, approves uploads, registers feeds and configures alert rules. |
| Super admin | Platform-wide: every agency, every setting. |

See [Roles & Permissions](../access-control/roles-and-permissions.md) for the complete list.

## Adding your own recordings

Every guide page contains a **Video tutorial** placeholder. To add a recording, replace the `_coming soon._` text with a link, and keep the `VIDEO-URL` comment so the [video index](../reference/video-index.md) stays accurate.

## Related topics

- [How to access UAPTS](how-to-access.md)
- [Navigation and shortcuts](navigation-and-shortcuts.md)
- [Data sources catalogue](../reference/data-sources.md)

## On this page

- [Who this guide is for](#who-this-guide-is-for)
- [How the guide is organised](#how-the-guide-is-organised)
- [Where the data comes from](#where-the-data-comes-from)
- [The modules](#the-modules)
- [Roles at a glance](#roles-at-a-glance)
- [Adding your own recordings](#adding-your-own-recordings)
- [Related topics](#related-topics)

## Support

- **Your agency administrator** is the first contact for access, role and data-quality questions.
- **Data feeds, templates and API questions:** `api-support@uapts.go.ke` (include the `X-Request-ID` response header from a failing call).
- **Security concerns:** `security@uapts.go.ke`. Do not report suspected vulnerabilities publicly.
