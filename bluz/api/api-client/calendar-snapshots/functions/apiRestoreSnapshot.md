[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-client/calendar-snapshots](../index.md) / apiRestoreSnapshot

# Function: apiRestoreSnapshot()

> **apiRestoreSnapshot**(`snapshotId`, `iterationId?`, `eventIds?`): `Promise`\<[`CalendarSnapshotRestoreResult`](../../../api-shared/types/type-aliases/CalendarSnapshotRestoreResult.md)\>

Defined in: [ui/src/api-client/calendar-snapshots.ts:85](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-client/calendar-snapshots.ts#L85)

Restores the calendar to a snapshot's state on the server. The server
archives live events within the snapshot's date range, re-inserts the
snapshot's events, and broadcasts the change to all connected clients.
With `eventIds`, only those events are restored.

## Parameters

### snapshotId

`string`

### iterationId?

`string`

### eventIds?

`string`[]

## Returns

`Promise`\<[`CalendarSnapshotRestoreResult`](../../../api-shared/types/type-aliases/CalendarSnapshotRestoreResult.md)\>
