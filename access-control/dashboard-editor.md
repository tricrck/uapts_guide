# Dashboard editor

_Access Control › Dashboard Manager › Editor_ · Route `/admin/dashboards/<id>`

The **dashboard editor** is a canvas where you arrange widgets, set filters and actions, choose the audience, preview the result as a typical viewer, and publish with a change note. Every publish creates a **version** you can restore.

> 🎬 **Video tutorial:** _coming soon._  
> <!-- VIDEO-URL: access-control/dashboard-editor | paste the link here, e.g. [Watch the walkthrough](https://…) -->

## Highlights

- Drag-and-drop canvas with a **widget palette** and an **inspector** for each widget.
- **Preview** the dashboard as a specific agency, department or role — widgets they cannot access are hidden.
- **Versions** with **Restore to draft**.
- Validation: _N widgets need attention_ and **Fix these before publishing**.
- Settings: **Description**, **Density** (Comfortable / Compact), **Row height**, **Gap**, **Auto-refresh** (Off, every 1, 2, 5 or 15 minutes).

## Enabling and access

Opened from [Dashboard Manager](dashboard-manager.md) (`/admin/dashboards/<id>`) or from **Edit** on a dashboard you are viewing. Same permissions as the Dashboard Manager.

## Widgets you can add

KPI, KPI row, Stat, Series (trend), Breakdown, Status list, Table, Heatmap, Points (map), Risk map, Progress, Agency card, Alerts, Feed health, Incident trend, Fatality bars, Text, Image. Each widget is bound to data (a measure, filters and a query) and can carry actions such as opening a page.

## Build and publish

1. Open the dashboard. The header shows **Unsaved changes** or **Draft has unpublished edits**.
2. Use the tabs **Widgets**, **Filters**, **Actions** and **Audience**. In **Widgets**, add from the palette, drag to move, drag the corner to resize, and edit it in the inspector.
3. Set the dashboard options (description, density, row height, gap, auto-refresh). **Duplicate** copies the dashboard; **Archive** retires it.
4. In **Audience**, assign it to agencies, departments, roles or people. _Nobody yet_ means only editors can open it.
5. Click **Preview** and choose the viewer to see exactly what they will see. Click **Back to editing** to return.
6. Fix anything flagged, then click **Publish…**, add a **Change note** and click **Publish now**.
7. To undo, open **Versions** and click **Restore to draft** on an earlier version, then publish again.

## Data sources and feeds

Widget data comes from the module endpoints (see each module page) and from the dashboard query catalogue; the dashboard itself is stored by UAPTS. Endpoints: `/dashboards/<id>/`, `/dashboards/<id>/publish/`, `/dashboards/<id>/versions/`, `/dashboards/<id>/assignments/`.

## Related topics

- [Dashboard Manager](dashboard-manager.md)
- [Command Centre home](../command-centre/home.md)

## On this page

- [Highlights](#highlights)
- [Enabling and access](#enabling-and-access)
- [Widgets you can add](#widgets-you-can-add)
- [Build and publish](#build-and-publish)
- [Data sources and feeds](#data-sources-and-feeds)
- [Related topics](#related-topics)

## Support

- **Your agency administrator** is the first contact for access, role and data-quality questions.
- **Data feeds, templates and API questions:** `api-support@uapts.go.ke` (include the `X-Request-ID` response header from a failing call).
- **Security concerns:** `security@uapts.go.ke`. Do not report suspected vulnerabilities publicly.
