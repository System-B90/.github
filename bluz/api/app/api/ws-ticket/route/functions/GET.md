[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [app/api/ws-ticket/route](../index.md) / GET

# Function: GET()

> **GET**(): `Promise`\<`NextResponse`\<`unknown`\>\>

Defined in: [ui/src/app/api/ws-ticket/route.ts:16](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/app/api/ws-ticket/route.ts#L16)

Issues a session-server WebSocket ticket, scoped to the caller's clearance
(#656).

The scope is signed, so the browser cannot upgrade itself, and it is what
the session server gates on: a `hanich` socket may not register a session
(which would put it on the untargeted broadcast, where course/outsider/room
payloads travel) and may listen only to the student refresh channel, which
carries nothing but empty pings.

## Returns

`Promise`\<`NextResponse`\<`unknown`\>\>
