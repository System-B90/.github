[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar/snapshot-diff](../index.md) / diffSnapshot

# Function: diffSnapshot()

> **diffSnapshot**(`snapshotEvents`, `liveEvents`, `range`): [`SnapshotDiffEntry`](../type-aliases/SnapshotDiffEntry.md)[]

Defined in: [ui/src/components/schedule/calendar/calendar/snapshot-diff.ts:72](https://github.com/System-B90/Bluz/blob/04ebae9cb334a01c6e7a55f885993f021e83cd92/ui/src/components/schedule/calendar/calendar/snapshot-diff.ts#L72)

Every event a restore of the snapshot would touch, in calendar order.
Unchanged events are left out: restoring them does nothing.

## Parameters

### snapshotEvents

readonly [`Event`](../../../../../../api-shared/types/event/type-aliases/Event.md)[]

The events the snapshot captured.

### liveEvents

readonly [`Event`](../../../../../../api-shared/types/event/type-aliases/Event.md)[]

Live events; those outside the range are ignored.

### range

`Range`

The range the snapshot covers.

## Returns

[`SnapshotDiffEntry`](../type-aliases/SnapshotDiffEntry.md)[]
