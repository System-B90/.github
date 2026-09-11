[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-calendar-snapshot](../../../index.md) / [DbCalendarSnapshot](../index.md) / create

# Variable: create

> `const` **create**: (`label`, `events`, `controller`, `iterationId?`) => `Promise`\<[`CalendarSnapshotSummary`](../../../../../api-shared/types/type-aliases/CalendarSnapshotSummary.md)\> = `createSnapshot`

Defined in: [ui/src/api-server/db-calendar-snapshot.ts:269](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/db-calendar-snapshot.ts#L269)

Captures a named, git-tag-like restore point of the calendar. The full event
documents are stored so the calendar can later be restored to this exact state.

## Parameters

### label

`string`

### events

[`DbEventDocument`](../../../../../api-shared/types/event/type-aliases/DbEventDocument.md)[]

### controller?

[`DatabaseController`](../../../../mongo-db-controller/classes/DatabaseController.md) = `databaseController`

### iterationId?

`string`

## Returns

`Promise`\<[`CalendarSnapshotSummary`](../../../../../api-shared/types/type-aliases/CalendarSnapshotSummary.md)\>

The lightweight summary of the created snapshot (no events payload).
