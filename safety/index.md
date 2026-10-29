# Safety & Incidents — module guide

_Safety & Incidents_

Road-safety intelligence: national KPIs, active incidents and emergency dispatch, accident black spots and predictive hotspots, and traffic-violation trends.

> 🎬 **Video tutorial:** _coming soon._  
> <!-- VIDEO-URL: safety/index | paste the link here -->

## Pages in this module

| Page | What it shows |
|---|---|
| [Safety Overview](safety-overview.md) | National road safety KPIs, active incidents, KMD weather correlation, KeNHA road intervention effectiveness, and predictive hotspot analysis |
| [Incident Command](incident-command.md) | Real-time active incidents, NPS emergency dispatch coordination, KMD weather context, and investigation workflows |
| [Blackspot Analysis](blackspot-analysis.md) | KDE accident cluster analysis, KeNHA road geometry context, KMD weather correlation, and predictive hotspot overlays |
| [Safety KPIs](safety-kpis.md) | National crash rates, injury severity, county breakdowns by road authority, and traffic violation trends |

## Time period

All four pages share one time-period control: **24 Hours**, **7 Days**, **30 Days**, a calendar **Year**, or a **Custom** from/to range for looking at a specific stretch of an agency's historic incidents. See [Filtering by time period](safety-overview.md#filtering-by-time-period).

## Data feeding this module

Upload templates (download from the catalogue):

| Feed ID | Agency | Sheet | Download |
|---|---|---|---|
| `kenha-crash-records` | KeNHA | Road Crash Records | [xlsx](../data-templates/kenha-crash-records.xlsx) · [csv](../data-templates/kenha-crash-records.csv) |
| `ntsa-crash-records` | NTSA | Road Crash Records | [xlsx](../data-templates/ntsa-crash-records.xlsx) · [csv](../data-templates/ntsa-crash-records.csv) |
| `sdr-crash-records` | SDR | Road Crash Records | [xlsx](../data-templates/sdr-crash-records.xlsx) · [csv](../data-templates/sdr-crash-records.csv) |

Live feeds with a handler: `ntsa-itims`.

## Who can use it

Module **M05 · Safety and Incidents**. Agencies with full access in the baseline policy: KENHA, KURA, KERRA, SDR, NPS, SDT, NTSA; read-only: KCAA, KWS.

## Support

- **Your agency administrator** is the first contact for access, role and data-quality questions.
- **Data feeds, templates and API questions:** `api-support@uapts.go.ke` (include the `X-Request-ID` response header from a failing call).
- **Security concerns:** `security@uapts.go.ke`. Do not report suspected vulnerabilities publicly.
