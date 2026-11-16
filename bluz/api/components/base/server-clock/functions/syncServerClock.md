[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/server-clock](../index.md) / syncServerClock

# Function: syncServerClock()

> **syncServerClock**(`serverMs`, `sentAt`, `receivedAt?`): `void`

Defined in: [ui/src/components/base/server-clock.ts:44](https://github.com/System-B90/Bluz/blob/182d51c797407c7b0ea37986b1a45ab0e64c4df0/ui/src/components/base/server-clock.ts#L44)

Records the server's clock from a response. `sentAt` / `receivedAt` are
performance.now readings around the request; the server's reading is
taken to be from their midpoint.

## Parameters

### serverMs

`number`

### sentAt

`number`

### receivedAt?

`number` = `...`

## Returns

`void`
