[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [app/api/server-time/route](../index.md) / GET

# Variable: GET

> `const` **GET**: `ServerApiServerTimeGet`

Defined in: [ui/src/app/api/server-time/route.ts:22](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/app/api/server-time/route.ts#L22)

GET /api/server-time — the server's clock. The student board's only source
of "now" (the day on screen, the midnight rollover, the time line), and the
staff calendar's "today".

Reachable by a Hanich session, like the `student-view/` routes: read-only,
and it carries nothing but the time. A student's request is also where a
wound device clock is caught (`clock-tampering`) — detection only, the
answer is the server's clock regardless.
