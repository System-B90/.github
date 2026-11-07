[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [app/(themed)/(student)/student-view/page](../index.md) / default

# Function: default()

> **default**(`__namedParameters`): `Promise`\<`Element`\>

Defined in: [ui/src/app/(themed)/(student)/student-view/page.tsx:24](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/app/(themed)/(student)/student-view/page.tsx#L24)

`/student-view` — what a student ("חניך") sees, and the staff preview of it
(#656).

The board itself is identical for both audiences; only the preview bar is
conditional, and it is rendered from a *server-side* clearance check rather
than a client flag, so a student cannot summon it. The `?date=` param is
likewise honoured only for staff — the server rejects it for a student
session regardless of what this page passes down.

## Parameters

### \_\_namedParameters

`PageProps`

## Returns

`Promise`\<`Element`\>
