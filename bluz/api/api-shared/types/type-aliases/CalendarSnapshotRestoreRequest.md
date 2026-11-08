[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/types](../index.md) / CalendarSnapshotRestoreRequest

# Type Alias: CalendarSnapshotRestoreRequest

> **CalendarSnapshotRestoreRequest** = `object`

Defined in: [ui/src/api-shared/types.ts:95](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-shared/types.ts#L95)

Body of POST /api/calendar/snapshots/restore. `eventIds` picks the events
to restore (snapshot events to write back, events added since to remove);
absent ⇒ the whole snapshot.

## Properties

### eventIds?

> `optional` **eventIds?**: `string`[]

Defined in: [ui/src/api-shared/types.ts:96](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-shared/types.ts#L96)
