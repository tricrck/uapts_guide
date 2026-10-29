# Aviation — module guide

_Aviation_

Airport and airline operations: flight movements, on-time performance, passenger and cargo volumes, aircraft and operator licensing, and aviation infrastructure.

> 🎬 **Video tutorial:** _coming soon._  
> <!-- VIDEO-URL: aviation/index | paste the link here -->

## Pages in this module

| Page | What it shows |
|---|---|
| [Overview](aviation-overview.md) | headline fleet, flight, punctuality and passenger figures at a glance |
| [Flight Movements](flight-movements.md) | Real-time ADS-B flight tracking, OTP, passenger volumes, cargo, KMD weather advisories, and KCAA safety oversight |
| [Flight Log](flight-log.md) | Full flight-by-flight log with delay, passenger and cargo detail |
| [Passenger Stats](passenger-stats.md) | Airport throughput, domestic vs international volumes, KenTrade air cargo clearances, and revenue trends |
| [Aircraft Licencing](aircraft-licencing.md) | Certificate of Registration, Certificate of Airworthiness, AOC, noise/insurance/radio certificates, and pilot licences - with renewal tracking |
| [Aviation Infrastructure](aviation-infrastructure.md) | Airport registry, capacity utilisation, runway/navaid condition, terminal & ATC facilities, and capital works |

## Data feeding this module

Upload templates (download from the catalogue):

| Feed ID | Agency | Sheet | Download |
|---|---|---|---|
| `kaa-air-cargo-statistics` | KAA | Air Cargo Statistics | [xlsx](../data-templates/kaa-air-cargo-statistics.xlsx) · [csv](../data-templates/kaa-air-cargo-statistics.csv) |
| `kaa-airport-register` | KAA | Airport Register | [xlsx](../data-templates/kaa-airport-register.xlsx) · [csv](../data-templates/kaa-airport-register.csv) |
| `kaa-flight-movements` | KAA | Flight Movements | [xlsx](../data-templates/kaa-flight-movements.xlsx) · [csv](../data-templates/kaa-flight-movements.csv) |
| `kaa-ground-handlers` | KAA | Ground Handlers | [xlsx](../data-templates/kaa-ground-handlers.xlsx) · [csv](../data-templates/kaa-ground-handlers.csv) |
| `kaa-passenger-statistics` | KAA | Passenger Statistics | [xlsx](../data-templates/kaa-passenger-statistics.xlsx) · [csv](../data-templates/kaa-passenger-statistics.csv) |
| `kaa-runway-register` | KAA | Runway Register | [xlsx](../data-templates/kaa-runway-register.xlsx) · [csv](../data-templates/kaa-runway-register.csv) |
| `kcaa-aircraft-register` | KCAA | Aircraft Register | [xlsx](../data-templates/kcaa-aircraft-register.xlsx) · [csv](../data-templates/kcaa-aircraft-register.csv) |
| `kcaa-airline-register` | KCAA | Airline Register | [xlsx](../data-templates/kcaa-airline-register.xlsx) · [csv](../data-templates/kcaa-airline-register.csv) |
| `kcaa-aoc-register` | KCAA | AOC Register | [xlsx](../data-templates/kcaa-aoc-register.xlsx) · [csv](../data-templates/kcaa-aoc-register.csv) |
| `kcaa-atm-performance` | KCAA | ATM Performance | [xlsx](../data-templates/kcaa-atm-performance.xlsx) · [csv](../data-templates/kcaa-atm-performance.csv) |
| `kcaa-occurrence-reports` | KCAA | Occurrence Reports | [xlsx](../data-templates/kcaa-occurrence-reports.xlsx) · [csv](../data-templates/kcaa-occurrence-reports.csv) |
| `kmd-aviation-weather` | KMD | Aviation Weather | [xlsx](../data-templates/kmd-aviation-weather.xlsx) · [csv](../data-templates/kmd-aviation-weather.csv) |

Live feeds with a handler: `kaa-aodb`, `kmd-synop`.

## Who can use it

Module **M07a · Aviation**. Agencies with full access in the baseline policy: KAA, KCAA, SDT.

## Support

- **Your agency administrator** is the first contact for access, role and data-quality questions.
- **Data feeds, templates and API questions:** `api-support@uapts.go.ke` (include the `X-Request-ID` response header from a failing call).
- **Security concerns:** `security@uapts.go.ke`. Do not report suspected vulnerabilities publicly.
