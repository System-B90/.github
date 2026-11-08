[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-calendar-snapshot](../../../index.md) / [DbCalendarSnapshot](../index.md) / restore

# Variable: restore

> `const` **restore**: (`snapshotId`, `controller`, `iterationId?`, `eventIds?`) => `Promise`\<[`CalendarSnapshotRestoreResult`](../../../../../api-shared/types/type-aliases/CalendarSnapshotRestoreResult.md)\> = `restoreSnapshot`

Defined in: [ui/src/api-server/db-calendar-snapshot.ts:369](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-server/db-calendar-snapshot.ts#L369)

Restores the calendar to a snapshot's state within the snapshot's range
(stored at capture; the events' own span for older snapshots): live events
inside the range are archived (soft-deleted), the snapshot's events are
upserted back, and connected clients are notified via WebSocket broadcasts.
A snapshot of an empty range restores that range to empty.

With `eventIds`, only those events are restored: a listed snapshot event is
written back as captured, and a listed live event inside the range that the
snapshot does not hold (added since) is archived. Everything else is left
as it is now.

## Parameters

### snapshotId

`string`

### controller?

[`DatabaseController`](../../../../mongo-db-controller/classes/DatabaseController.md) = `databaseController`

### iterationId?

`string`

### eventIds?

readonly `string`[]

## Returns

`Promise`\<[`CalendarSnapshotRestoreResult`](../../../../../api-shared/types/type-aliases/CalendarSnapshotRestoreResult.md)\>
