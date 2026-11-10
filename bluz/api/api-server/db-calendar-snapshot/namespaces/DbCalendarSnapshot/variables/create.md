[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-calendar-snapshot](../../../index.md) / [DbCalendarSnapshot](../index.md) / create

# Variable: create

> `const` **create**: (`label`, `events`, `controller`, `iterationId?`, `range?`) => `Promise`\<[`CalendarSnapshotSummary`](../../../../../api-shared/types/type-aliases/CalendarSnapshotSummary.md)\> = `createSnapshot`

Defined in: [ui/src/api-server/db-calendar-snapshot.ts:365](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-server/db-calendar-snapshot.ts#L365)

Captures a named, git-tag-like restore point of the calendar. The full event
documents are stored so the calendar can later be restored to this exact state.

With `events` undefined and a `range`, the server reads the saved events
inside the range itself (the UI's form), so a snapshot never records a
browser's unsaved or partially loaded state. Passed `events` are stored as
given (the CLI's form).

## Parameters

### label

`string`

### events

[`DbEventDocument`](../../../../../api-shared/types/event/type-aliases/DbEventDocument.md)[] \| `undefined`

### controller?

[`DatabaseController`](../../../../mongo-db-controller/classes/DatabaseController.md) = `databaseController`

### iterationId?

`string`

### range?

[`CalendarDraftRange`](../../../../../api-shared/types/type-aliases/CalendarDraftRange.md)

## Returns

`Promise`\<[`CalendarSnapshotSummary`](../../../../../api-shared/types/type-aliases/CalendarSnapshotSummary.md)\>

The lightweight summary of the created snapshot (no events payload).
