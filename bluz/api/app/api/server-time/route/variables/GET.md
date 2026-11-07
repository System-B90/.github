[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [app/api/server-time/route](../index.md) / GET

# Variable: GET

> `const` **GET**: `ServerApiServerTimeGet`

Defined in: [ui/src/app/api/server-time/route.ts:22](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/app/api/server-time/route.ts#L22)

GET /api/server-time — the server's clock. The student board's only source
of "now" (the day on screen, the midnight rollover, the time line), and the
staff calendar's "today".

Reachable by a Hanich session, like the `student-view/` routes: read-only,
and it carries nothing but the time. A student's request is also where a
wound device clock is caught (`clock-tampering`) — detection only, the
answer is the server's clock regardless.
