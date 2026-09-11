[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/web-socket-utils](../index.md) / SendServerRequestToSessionServer

# Function: SendServerRequestToSessionServer()

> **SendServerRequestToSessionServer**(`type`, `data?`, `targets?`): `void`

Defined in: [ui/src/api-server/web-socket-utils.ts:129](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/web-socket-utils.ts#L129)

Dispatch an asynchronous server-to-server request over WebSocket to the Session Server.
This runs within Next.js server-side API routes to broadcast event changes, additions,
or deletions to all connected clients in real-time.

The underlying connection is persistent and re-established lazily, so a broadcast
costs one `send()` on the hot path instead of a full connection handshake.

## Parameters

### type

[`MessageTypes`](../../../settings/enumerations/MessageTypes.md)

The type of message being broadcasted (e.g. MessageTypes.EVENT_DATA_UPDATE).

### data?

`any`

Optional payload containing details of the updated/added/removed entities.

### targets?

`string` \| `string`[]

Sync-object id(s) to scope delivery to (see `iterationSyncId`).
Omit only for data that every connected client should receive regardless of
which iteration it's viewing.

## Returns

`void`

## Example

```typescript
SendServerRequestToSessionServer(
  MessageTypes.EVENT_ADDED_OR_REMOVED,
  { action: "added", newData: fixedEvent, eventId: eventId },
  iterationSyncId(iterationId),
);
```
