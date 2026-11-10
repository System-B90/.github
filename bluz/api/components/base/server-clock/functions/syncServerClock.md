[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/server-clock](../index.md) / syncServerClock

# Function: syncServerClock()

> **syncServerClock**(`serverMs`, `sentAt`, `receivedAt?`): `void`

Defined in: [ui/src/components/base/server-clock.ts:44](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/base/server-clock.ts#L44)

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
