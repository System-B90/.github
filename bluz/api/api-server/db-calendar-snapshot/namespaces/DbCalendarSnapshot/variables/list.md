[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-calendar-snapshot](../../../index.md) / [DbCalendarSnapshot](../index.md) / list

# Variable: list

> `const` **list**: (`controller`, `iterationId?`) => `Promise`\<[`CalendarSnapshotSummary`](../../../../../api-shared/types/type-aliases/CalendarSnapshotSummary.md)[]\> = `listSnapshots`

Defined in: [ui/src/api-server/db-calendar-snapshot.ts:366](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-server/db-calendar-snapshot.ts#L366)

Lists snapshots newest-first, without their (large) events payload.

## Parameters

### controller?

[`DatabaseController`](../../../../mongo-db-controller/classes/DatabaseController.md) = `databaseController`

### iterationId?

`string`

## Returns

`Promise`\<[`CalendarSnapshotSummary`](../../../../../api-shared/types/type-aliases/CalendarSnapshotSummary.md)[]\>
