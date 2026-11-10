[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/types](../index.md) / CalendarSnapshotRestoreRequest

# Type Alias: CalendarSnapshotRestoreRequest

> **CalendarSnapshotRestoreRequest** = `object`

Defined in: [ui/src/api-shared/types.ts:95](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/types.ts#L95)

Body of POST /api/calendar/snapshots/restore. `eventIds` picks the events
to restore (snapshot events to write back, events added since to remove);
absent ⇒ the whole snapshot.

## Properties

### eventIds?

> `optional` **eventIds?**: `string`[]

Defined in: [ui/src/api-shared/types.ts:96](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/types.ts#L96)
