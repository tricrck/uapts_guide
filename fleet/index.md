# Fleet & Vehicle Tracking — module guide

_Fleet & Vehicle Tracking_

Tracks public-service and government vehicles: utilisation, speed-governor compliance, driver behaviour, live GPS positions, geofence breaches and historical trip replay.

> 🎬 **Video tutorial:** _coming soon._  
> <!-- VIDEO-URL: fleet/index | paste the link here -->

## Pages in this module

| Page | What it shows |
|---|---|
| [Fleet Overview](fleet-overview.md) | Fleet utilization, speed governor compliance, KMD weather-correlated driver behaviour events, and operator leaderboard |
| [Driver Behaviour](driver-behaviour.md) | NTSA iTIMS - Full driver behaviour event log and the fleet utilization leaderboard |
| [Live Positions](live-positions.md) | Real-time GPS positions for all active PSVs and government fleet - refreshes every 30 seconds |
| [Geofences](geofences.md) | Configure zones (depots, ports, restricted areas) and monitor entry/exit breach events |
| [Trip Playback](trip-playback.md) | Replay any vehicle's historical route - select a trip to visualize the path on the map |

## Data feeding this module

Upload templates (download from the catalogue):

| Feed ID | Agency | Sheet | Download |
|---|---|---|---|
| `ntsa-geofence-register` | NTSA | Geofence Register | [xlsx](../data-templates/ntsa-geofence-register.xlsx) · [csv](../data-templates/ntsa-geofence-register.csv) |
| `ntsa-psv-fleet-register` | NTSA | Vehicle Register | [xlsx](../data-templates/ntsa-psv-fleet-register.xlsx) · [csv](../data-templates/ntsa-psv-fleet-register.csv) |

## Who can use it

Module **M03 · Fleet and Vehicle Tracking**. Agencies with full access in the baseline policy: SDR, SDR_MTD, SDT, NTSA.

## Support

- **Your agency administrator** is the first contact for access, role and data-quality questions.
- **Data feeds, templates and API questions:** `api-support@uapts.go.ke` (include the `X-Request-ID` response header from a failing call).
- **Security concerns:** `security@uapts.go.ke`. Do not report suspected vulnerabilities publicly.
