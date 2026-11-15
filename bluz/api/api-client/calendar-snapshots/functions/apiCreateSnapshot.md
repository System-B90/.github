[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-client/calendar-snapshots](../index.md) / apiCreateSnapshot

# Function: apiCreateSnapshot()

> **apiCreateSnapshot**(`label`, `range`, `iterationId?`): `Promise`\<[`CalendarSnapshotSummary`](../../../api-shared/types/type-aliases/CalendarSnapshotSummary.md)\>

Defined in: [ui/src/api-client/calendar-snapshots.ts:35](https://github.com/System-B90/Bluz/blob/d77dcf130db661461363a52910f62a34b3514ebd/ui/src/api-client/calendar-snapshots.ts#L35)

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
