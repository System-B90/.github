[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/types](../index.md) / CalendarSnapshotRestoreRequest

# Type Alias: CalendarSnapshotRestoreRequest

> **CalendarSnapshotRestoreRequest** = `object`

Defined in: [ui/src/api-shared/types.ts:95](https://github.com/System-B90/Bluz/blob/04ebae9cb334a01c6e7a55f885993f021e83cd92/ui/src/api-shared/types.ts#L95)

Body of POST /api/calendar/snapshots/restore. `eventIds` picks the events
to restore (snapshot events to write back, events added since to remove);
absent ⇒ the whole snapshot.

## Properties

### eventIds?

> `optional` **eventIds?**: `string`[]

Defined in: [ui/src/api-shared/types.ts:96](https://github.com/System-B90/Bluz/blob/04ebae9cb334a01c6e7a55f885993f021e83cd92/ui/src/api-shared/types.ts#L96)
