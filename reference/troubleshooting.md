# Troubleshooting

_Reference_

> 🎬 **Video tutorial:** _coming soon._  
> <!-- VIDEO-URL: reference/troubleshooting | paste the link here -->

| Symptom | Likely cause | What to do |
|---|---|---|
| The page shows **“unavailable”** on tiles | The data source for that tile has no data yet (for example _KeNHA ATC feed unavailable_). | Check the tile's **Data from / ingested via** entry on its guide page and whether the feed or template has been loaded (Integration Hub → Files & Feeds). |
| An error banner says **Unable to reach the UAPTS … API** | The request failed (network, server or permission). | Reload; if it persists tell your administrator and quote the page and time. |
| **Offline** in the top bar | The real-time connection is down. | Pages still load on request; reload to reconnect. |
| Tables are empty | No records for your agency or filters. | Press **Reset**, widen the time range, and confirm data has been committed. |
| Upload says **Column names don't match the template** | Headers were changed or an old template was used. | Download the current template or use **Map columns →**. |
| Upload is **Rejected** | Every row failed validation. | Open the batch, read **What's wrong, grouped**, fix and **Upload a correction**. |
| A feed shows **connected** but nothing appears | It receives records but none are written. | Open the feed detail → **Top handler errors** / **Unrecognised record types**. |
| I cannot sign in | Wrong details or temporary lock. | See [How to access](../getting-started/how-to-access.md#if-you-cannot-sign-in). |
| **Export CSV** is missing | Export needs the Analyst tier or above. | Ask your agency administrator. |

## Support

- **Your agency administrator** is the first contact for access, role and data-quality questions.
- **Data feeds, templates and API questions:** `api-support@uapts.go.ke` (include the `X-Request-ID` response header from a failing call).
- **Security concerns:** `security@uapts.go.ke`. Do not report suspected vulnerabilities publicly.
