[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-client/calendar-snapshots](../index.md) / apiRestoreSnapshot

# Function: apiRestoreSnapshot()

> **apiRestoreSnapshot**(`snapshotId`, `iterationId?`): `Promise`\<[`CalendarSnapshotRestoreResult`](../../../api-shared/types/type-aliases/CalendarSnapshotRestoreResult.md)\>

Defined in: [ui/src/api-client/calendar-snapshots.ts:75](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-client/calendar-snapshots.ts#L75)

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
