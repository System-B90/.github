[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/types](../index.md) / CalendarSnapshotRestoreRequest

# Type Alias: CalendarSnapshotRestoreRequest

> **CalendarSnapshotRestoreRequest** = `object`

Defined in: [ui/src/api-shared/types.ts:95](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/api-shared/types.ts#L95)

Body of POST /api/calendar/snapshots/restore. `eventIds` picks the events
to restore (snapshot events to write back, events added since to remove);
absent ⇒ the whole snapshot.

## Properties

### eventIds?

> `optional` **eventIds?**: `string`[]

Defined in: [ui/src/api-shared/types.ts:96](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/api-shared/types.ts#L96)
