# Module Access

_Access Control › Module Access_ · Route `/access-policies`

**Module Access** controls which modules, pages and restricted data categories each agency — and each role inside it — can reach. It is the screen behind what appears in a user's sidebar and search.

> 🎬 **Video tutorial:** _coming soon._  
> <!-- VIDEO-URL: access-control/module-access | paste the link here, e.g. [Watch the walkthrough](https://…) -->

## How it works

Access is built in layers, and each layer can only **narrow** the one above:

| Layer | Who sets it | What it holds |
|---|---|---|
| **Allowed by super admin** (ceiling) | Super admin only | The most an agency can ever have. |
| **Enabled for agency** | Super admin, or that agency's admin | What the agency has switched on, within the ceiling. |
| **Pages by role** | Super admin, or that agency's admin | What each role (analyst, operator …) may open, within what the agency enabled. |

Scopes are ordered **Restricted** (none) < **Read** < **Full**. A module's scope applies to every page in it unless a page is set individually. With nothing saved, the baseline policy applies.

## Highlights

- Pick an **Agency**, then work through four tabs: **Modules and pages**, **Data categories**, **Pages by role** and **Capabilities**.
- A **preview** shows exactly what a role in that agency would see.
- **Unsaved changes** are counted per agency, with **Discard** and **Save changes**.
- A **history** of every change, and an **export** of the policy.
- Warnings for saved settings that refer to modules or pages that no longer exist (**Clear** removes them).

## Enabling and access

Open **Access Control → Module Access** (`/access-policies`), module **M10**; needs the **Admin** tier. A **super admin** can edit every agency and the ceiling; an **agency admin** can edit only their own agency within the ceiling. Others see a message that their role can view but not change.

![Module Access page](../assets/screenshots/access-policies.webp)

## Change what an agency can reach

1. Choose the **Agency** (code – name).
2. On **Modules and pages**, find the module. Use the filters to narrow the list; open a module to set its pages individually.
3. For each module set **Allowed by super admin** (super admin only) and **Enabled for agency** to **Full**, **Read** or **Restricted**. _Enabled can never exceed Allowed._
4. On **Data categories**, untick any category that should be masked on every page for this agency (for example parcel-level land records). Admin-only categories stay masked for analysts and operators regardless.
5. On **Pages by role**, set what each role may open. _A role can never exceed what the agency has enabled._
6. On **Capabilities**, choose which roles hold `export`, `query_builder`, `run_reports`, `manage_users`, `approve_uploads`, `register_feeds` and `configure_rules`.
7. Check the **Preview**, then click **Save changes** (or **Discard**). Changes are written to the history and the Audit Trail.

## Safeguards

- **Self-lockout guard:** an agency admin cannot save a change that would remove their own admin role's access to this page or the `manage_users` capability.
- Unknown modules, pages, categories or roles are refused.
- Platform-blocked categories cannot be changed by anyone.
- Role tiers the baseline does not know resolve as **denied**.

## Data sources and feeds

| Data point | Endpoint | Ingested via |
|---|---|---|
| Policy (baseline + overrides) | `GET /access-control/`, `PUT /access-control/` | Baseline file shipped with UAPTS plus overrides saved on this page. |
| Change history | `GET /access-control/history/` | Written by the server whenever a policy is saved. |

## Permissions

| Who | Can |
|---|---|
| Super admin | Edit the ceiling, enabled scopes and roles for every agency. |
| Agency admin | Edit enabled scopes and roles for their own agency, within the ceiling. |
| Everyone else | View only, or no access. |

## Related topics

- [Roles & Permissions](roles-and-permissions.md)
- [Audit Trail](audit-trail.md)
- [User Management](user-management.md)

## On this page

- [How it works](#how-it-works)
- [Highlights](#highlights)
- [Enabling and access](#enabling-and-access)
- [Change what an agency can reach](#change-what-an-agency-can-reach)
- [Safeguards](#safeguards)
- [Data sources and feeds](#data-sources-and-feeds)
- [Permissions](#permissions)
- [Related topics](#related-topics)

## Support

- **Your agency administrator** is the first contact for access, role and data-quality questions.
- **Data feeds, templates and API questions:** `api-support@uapts.go.ke` (include the `X-Request-ID` response header from a failing call).
- **Security concerns:** `security@uapts.go.ke`. Do not report suspected vulnerabilities publicly.
