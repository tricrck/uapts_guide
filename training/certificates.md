# Certificates

_Training Institutes › Certificates_ · Route `/training/completions`

**Certificates & Completions** lets you see certificate register for all accredited training completions - issued by NTSA · KCAA · KMA · NITA-K with validity tracking and pass/fail outcomes.

> 🎬 **Video tutorial:** _coming soon._  
> <!-- VIDEO-URL: training/certificates | paste the link here, e.g. [Watch the walkthrough](https://…) -->

## Highlights

- **6 headline tiles** — Total Completions, Pass, Fail, Certificates Valid, Certificates Expired, Avg Score.
- **1 panels** — Certificate Register.
- **Filters and search** to narrow tables to what you need.
- Every figure is traceable to the data feed or upload template that supplies it — see [Data sources and feeds](#data-sources-and-feeds).

## Enabling and access

1. Sign in to UAPTS (see [How to access](../getting-started/how-to-access.md)).
2. In the left sidebar expand **Training Institutes** and click **Certificates**.
3. The page opens at `/training/completions`. You can also reach it with the global search (**Ctrl + K**).

This page belongs to module **M14 · Training Institutes**. The sidebar and the global search only list pages your agency and role can open, and a link to a page you cannot reach sends you back to the Command Centre. If a page you expect is missing, ask your agency administrator to check your agency's [Module Access](../access-control/module-access.md).

![Certificates page](../assets/screenshots/training-completions.webp)

## Page tour

### Headline tiles

![Certificates headline tiles](../assets/screenshots/training-completions--kpis.webp)

| Tile | What it shows | Data from | Table → ingested via |
|---|---|---|---|
| **Total Completions** | This page _(window: LIVE)_ | `/training/completions/` | _TrainingCompletion_ → no template yet |
| **Pass** | Successful completions _(window: LIVE)_ | `/training/completions/` | _TrainingCompletion_ → no template yet |
| **Fail** | Failed assessments _(window: LIVE)_ | — | — |
| **Certificates Valid** | Currently valid _(window: LIVE)_ | `/training/completions/` | _TrainingCompletion_ → no template yet |
| **Certificates Expired** | Renewal required _(window: LIVE)_ | `/training/completions/` | _TrainingCompletion_ → no template yet |
| **Avg Score** | Final assessment score _(window: LIVE)_ | `/training/completions/` | _TrainingCompletion_ → no template yet |

### Certificate Register


Contains a table with the columns **Certificate No.**, **Student**, **National ID**, **Cohort**, **Outcome**, **Score**, **Theory**, **Practical**, **Attendance**, **Issued By**, **Issued**, **Expiry**, **Validity**.

**Data from:** `/training/completions/`  
**Table → ingested via:** _TrainingCompletion_ → no template yet

## Working with this page

1. Open **Training Institutes → Certificates** from the sidebar.
2. Type in the **“Search certificate no. or student…”** box to filter what is shown.
3. Use the **All outcomes** drop-down to narrow the list. Choices include: Pass, Distinction, Fail, Incomplete, Deferred.
4. Use the **All validity** drop-down to narrow the list. Choices include: Valid only, Expired only.
5. Click **Apply** to use this action.

## Status and value meanings

These are the values the platform stores for the fields shown on this page (`value` followed by the label you see).

| Field | Table | Values |
|---|---|---|
| outcome | TrainingCompletion | `pass` · `fail` · `distinction` Pass with Distinction · `incomplete` · `deferred_resit` Deferred - Resit Required |

## Data sources and feeds

Every number and table on this page is read from the API endpoints below. The **Ingested via** column says how the underlying records get into UAPTS: a downloadable **upload template** (xlsx/CSV, loaded through the [Integration Hub](../integration-hub/upload-and-connect.md)), a **live feed** that pushes records to the ingest API, or — where neither exists yet — it is stated plainly.

| Endpoint | Records | Ingested via |
|---|---|---|
| `GET /training/completions/` | Training Completions | **No ingestion template yet** — populated by seed data or direct entry |

Full details of every template (columns, formats) are in the [Data sources catalogue](../reference/data-sources.md). Interactive API documentation is available at `/api/docs/`.

## Permissions

| Who | What they can do here |
|---|---|
| Public / read-only accounts | View the page where the module is enabled for their agency (read-only). |
| Operator | View the page. |
| Analyst | View and **export CSV**. |
| Agency admin | Everything an analyst can do, plus the administrative capabilities listed in [Roles & Permissions](../access-control/roles-and-permissions.md). |
| Super admin | Sees every agency's data. |

**Agencies with the Training Institutes module:** full — SDT, KRC.

_Access is evaluated by the server from the baseline policy plus any agency overrides, so a super admin or agency admin may have changed it from the defaults above._

## Related topics

- [Overview](training-overview.md)
- [Cohorts](cohorts.md)
- [Enrollments](enrollments.md)
- [Training Institutes overview](index.md)
- [Upload & Connect (Integration Hub)](../integration-hub/upload-and-connect.md)
- [Data sources catalogue](../reference/data-sources.md)

## On this page

- [Highlights](#highlights)
- [Enabling and access](#enabling-and-access)
- [Page tour](#page-tour)
- [Working with this page](#working-with-this-page)
- [Status and value meanings](#status-and-value-meanings)
- [Data sources and feeds](#data-sources-and-feeds)
- [Permissions](#permissions)
- [Related topics](#related-topics)

## Support

- **Your agency administrator** is the first contact for access, role and data-quality questions.
- **Data feeds, templates and API questions:** `api-support@uapts.go.ke` (include the `X-Request-ID` response header from a failing call).
- **Security concerns:** `security@uapts.go.ke`. Do not report suspected vulnerabilities publicly.
