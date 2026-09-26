[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/RealtimeStatus](../index.md) / RealtimeStatus

# Function: RealtimeStatus()

> **RealtimeStatus**(`__namedParameters`): `Element`

Defined in: [ui/src/components/base/RealtimeStatus.tsx:67](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/base/RealtimeStatus.tsx#L67)

Publishes the browser's WebSocket connection state into the DOM.

The realtime layer fails silently by design: `SessionWs` logs a console
error and retries on a backoff forever, and every spec drives a single
browser whose own writes update its own view regardless. That made "realtime
is entirely dead" indistinguishable from "realtime is fine" — the whole
client side of it was down in e2e for months while the suite stayed green
(#636). This renders nothing visible; it exists so a test can tell the two
apart.

The socket's host is published alongside its state, because "a socket is
open" is not the assertion worth making on its own: the bug was an address,
not an outage. A developer machine that also runs the dev stack has
something listening on the wrong address, so the browser connects there and
the connection looks healthy while pointing at a different deployment
entirely. Comparing this against the page's own origin is what catches that.

The state is sampled rather than subscribed to because the package exposes
the socket as a ref, which gives no notification when it is replaced on a
reconnect.

## Parameters

### \_\_namedParameters

[`RealtimeStatusProps`](../type-aliases/RealtimeStatusProps.md)

## Returns

`Element`
