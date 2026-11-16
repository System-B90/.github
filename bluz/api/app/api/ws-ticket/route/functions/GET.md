[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [app/api/ws-ticket/route](../index.md) / GET

# Function: GET()

> **GET**(): `Promise`\<`NextResponse`\<`unknown`\>\>

Defined in: [ui/src/app/api/ws-ticket/route.ts:17](https://github.com/System-B90/Bluz/blob/182d51c797407c7b0ea37986b1a45ab0e64c4df0/ui/src/app/api/ws-ticket/route.ts#L17)

Issues a session-server WebSocket ticket, scoped to the caller's clearance
(#656).

The scope is signed, so the browser cannot upgrade itself, and it is what
the session server gates on: a `hanich` socket may not register a session
(which would put it on the untargeted broadcast, where course/outsider/room
payloads travel) and may listen only to the student refresh channel, which
carries nothing but empty pings. A `checker` socket receives the staff
wire but may not relay (lock presence) frames.

## Returns

`Promise`\<`NextResponse`\<`unknown`\>\>
