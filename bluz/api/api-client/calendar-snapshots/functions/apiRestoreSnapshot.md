[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-client/calendar-snapshots](../index.md) / apiRestoreSnapshot

# Function: apiRestoreSnapshot()

> **apiRestoreSnapshot**(`snapshotId`, `iterationId?`): `Promise`\<[`CalendarSnapshotRestoreResult`](../../../api-shared/types/type-aliases/CalendarSnapshotRestoreResult.md)\>

Defined in: [ui/src/api-client/calendar-snapshots.ts:72](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-client/calendar-snapshots.ts#L72)

Restores the calendar to a snapshot's state on the server. The server
archives live events within the snapshot's date range, re-inserts the
snapshot's events, and broadcasts the change to all connected clients.

## Parameters

### snapshotId

`string`

### iterationId?

`string`

## Returns

`Promise`\<[`CalendarSnapshotRestoreResult`](../../../api-shared/types/type-aliases/CalendarSnapshotRestoreResult.md)\>
