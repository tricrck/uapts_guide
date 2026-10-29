# Road Traffic Management — module guide

_Road Traffic Management_

Live and historical traffic on the national road network: counting-station health, congestion events, speed compliance, vehicle mix, weather impact, origin–destination flows and short-term forecasts.

> 🎬 **Video tutorial:** _coming soon._  
> <!-- VIDEO-URL: traffic/index | paste the link here -->

## Pages in this module

| Page | What it shows |
|---|---|
| [Live Traffic Map](live-traffic-map.md) | Real-time flow, congestion events, speed compliance, KMD weather impact, and NCTTCA corridor alerts |
| [Traffic Analytics](traffic-analytics.md) | Volume trends, speed compliance, vehicle class breakdown, O-D matrix, and AI forecasts |
| [Traffic Alerts](traffic-alerts.md) | Active traffic alerts, congestion events, KMD weather warnings, and NCTTCA corridor risk forecasts |

## Data feeding this module

Upload templates (download from the catalogue):

| Feed ID | Agency | Sheet | Download |
|---|---|---|---|
| `kura-counting-station-register` | KURA | Counting Station Register | [xlsx](../data-templates/kura-counting-station-register.xlsx) · [csv](../data-templates/kura-counting-station-register.csv) |
| `kenha-counting-station-register` | KeNHA | Counting Station Register | [xlsx](../data-templates/kenha-counting-station-register.xlsx) · [csv](../data-templates/kenha-counting-station-register.csv) |
| `ntsa-counting-station-register` | NTSA | Counting Station Register | [xlsx](../data-templates/ntsa-counting-station-register.xlsx) · [csv](../data-templates/ntsa-counting-station-register.csv) |
| `ntsa-psv-fleet-register` | NTSA | Vehicle Register | [xlsx](../data-templates/ntsa-psv-fleet-register.xlsx) · [csv](../data-templates/ntsa-psv-fleet-register.csv) |

## Who can use it

Module **M02 · Road Traffic**. Agencies with full access in the baseline policy: KENHA, KURA, KERRA, SDR, SDT, NAMATA; read-only: COUNTY_GOV, KRB, NPS.

## Support

- **Your agency administrator** is the first contact for access, role and data-quality questions.
- **Data feeds, templates and API questions:** `api-support@uapts.go.ke` (include the `X-Request-ID` response header from a failing call).
- **Security concerns:** `security@uapts.go.ke`. Do not report suspected vulnerabilities publicly.
