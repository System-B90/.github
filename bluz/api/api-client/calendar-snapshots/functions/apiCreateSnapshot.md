[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-client/calendar-snapshots](../index.md) / apiCreateSnapshot

# Function: apiCreateSnapshot()

> **apiCreateSnapshot**(`label`, `range`, `iterationId?`): `Promise`\<[`CalendarSnapshotSummary`](../../../api-shared/types/type-aliases/CalendarSnapshotSummary.md)\>

Defined in: [ui/src/api-client/calendar-snapshots.ts:35](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-client/calendar-snapshots.ts#L35)

Creates a named snapshot of `range`. The server captures the saved events
inside it, so the snapshot never holds this browser's unsaved state.

## Parameters

### label

`string`

### range

[`CalendarDraftRange`](../../../api-shared/types/type-aliases/CalendarDraftRange.md)

### iterationId?

`string`

## Returns

`Promise`\<[`CalendarSnapshotSummary`](../../../api-shared/types/type-aliases/CalendarSnapshotSummary.md)\>
