# Access Control — module guide

_Access Control_

Manage who can sign in and what they can reach: agencies, users, roles, module access, custom dashboards and the audit trail.

> 🎬 **Video tutorial:** _coming soon._  
> <!-- VIDEO-URL: access-control/index | paste the link here -->

## Pages in this module

| Page | What it shows |
|---|---|
| [Agencies](agencies.md) | canWrite ? 'Platform-wide agency directory (tbl_agencies) - create and adjust the agencies UAPTS tracks' : 'Platform-wide agency directory - read-only for your role, contact a Super Admin to make changes' |
| [User Management](user-management.md) | unscoped ? 'Platform account directory - create accounts, manage status, and view profiles across all UAPTS agencies' : `Account directory for ${ownAgencyCode} - create accounts, manage status, and view profiles within your own agency` |
| [Roles & Permissions](roles-and-permissions.md) | RBAC role assignments, user status management, and organisational departments across UAPTS agencies |
| [Module Access](module-access.md) | Control which modules, pages and restricted data each agency, and each role inside it, can reach |
| [Dashboard Manager](dashboard-manager.md) | Build dashboards from widgets, then choose which agencies, departments, roles and people land on them |
| [Dashboard editor](dashboard-editor.md) |  |
| [Audit Trail](audit-trail.md) | scopeSubtitle |

## Data feeding this module

No upload template or live handler feeds this module's tables yet — see the per-page **Data sources and feeds** sections and the [catalogue](../reference/data-sources.md#tables-without-an-ingestion-template-yet).

## Who can use it

Module **M10 · Access Control**. Agencies with full access in the baseline policy: KENHA, KURA, KERRA, SDR, SDR_MTD, COUNTY_GOV, KAA, KCAA, KMD, KRA, KRB, KENTRADE, NPS, KWS, SDT, NTSA, NAMATA, KRC, KPA, KMA, NCTTCA, LAPSSET.

## Support

- **Your agency administrator** is the first contact for access, role and data-quality questions.
- **Data feeds, templates and API questions:** `api-support@uapts.go.ke` (include the `X-Request-ID` response header from a failing call).
- **Security concerns:** `security@uapts.go.ke`. Do not report suspected vulnerabilities publicly.
