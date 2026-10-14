[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-calendar-snapshot](../../../index.md) / [DbCalendarSnapshot](../index.md) / list

# Variable: list

> `const` **list**: (`controller`, `iterationId?`) => `Promise`\<[`CalendarSnapshotSummary`](../../../../../api-shared/types/type-aliases/CalendarSnapshotSummary.md)[]\> = `listSnapshots`

Defined in: [ui/src/api-server/db-calendar-snapshot.ts:281](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/api-server/db-calendar-snapshot.ts#L281)

Lists snapshots newest-first, without their (large) events payload.

## Parameters

### controller?

[`DatabaseController`](../../../../mongo-db-controller/classes/DatabaseController.md) = `databaseController`

### iterationId?

`string`

## Returns

`Promise`\<[`CalendarSnapshotSummary`](../../../../../api-shared/types/type-aliases/CalendarSnapshotSummary.md)[]\>
