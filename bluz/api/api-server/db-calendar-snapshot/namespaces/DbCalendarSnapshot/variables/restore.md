[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-calendar-snapshot](../../../index.md) / [DbCalendarSnapshot](../index.md) / restore

# Variable: restore

> `const` **restore**: (`snapshotId`, `controller`, `iterationId?`) => `Promise`\<[`CalendarSnapshotRestoreResult`](../../../../../api-shared/types/type-aliases/CalendarSnapshotRestoreResult.md)\> = `restoreSnapshot`

Defined in: [ui/src/api-server/db-calendar-snapshot.ts:297](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/api-server/db-calendar-snapshot.ts#L297)

Restores the calendar to a snapshot's state within the snapshot's own date
range: live events inside the range are archived (soft-deleted), the
snapshot's events are upserted back, and connected clients are notified via
WebSocket broadcasts.

## Parameters

### snapshotId

`string`

### controller?

[`DatabaseController`](../../../../mongo-db-controller/classes/DatabaseController.md) = `databaseController`

### iterationId?

`string`

## Returns

`Promise`\<[`CalendarSnapshotRestoreResult`](../../../../../api-shared/types/type-aliases/CalendarSnapshotRestoreResult.md)\>
