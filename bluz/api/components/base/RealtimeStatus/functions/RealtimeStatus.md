[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/RealtimeStatus](../index.md) / RealtimeStatus

# Function: RealtimeStatus()

> **RealtimeStatus**(): `Element`

Defined in: [ui/src/components/base/RealtimeStatus.tsx:58](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/base/RealtimeStatus.tsx#L58)

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

## Returns

`Element`
