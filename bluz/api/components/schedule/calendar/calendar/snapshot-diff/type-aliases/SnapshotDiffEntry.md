[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar/snapshot-diff](../index.md) / SnapshotDiffEntry

# Type Alias: SnapshotDiffEntry

> **SnapshotDiffEntry** = `object`

Defined in: [ui/src/components/schedule/calendar/calendar/snapshot-diff.ts:32](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/schedule/calendar/calendar/snapshot-diff.ts#L32)

## Properties

### change

> **change**: [`SnapshotChange`](../enumerations/SnapshotChange.md)

Defined in: [ui/src/components/schedule/calendar/calendar/snapshot-diff.ts:34](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/schedule/calendar/calendar/snapshot-diff.ts#L34)

***

### event

> **event**: [`Event`](../../../../../../api-shared/types/event/type-aliases/Event.md)

Defined in: [ui/src/components/schedule/calendar/calendar/snapshot-diff.ts:36](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/schedule/calendar/calendar/snapshot-diff.ts#L36)

The version a restore leaves behind, or the one it removes for `Added`.

***

### fields

> **fields**: `string`[]

Defined in: [ui/src/components/schedule/calendar/calendar/snapshot-diff.ts:40](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/schedule/calendar/calendar/snapshot-diff.ts#L40)

For `Changed`: the fields a restore puts back.

***

### id

> **id**: [`EventId`](../../../../../../api-shared/types/event/type-aliases/EventId.md)

Defined in: [ui/src/components/schedule/calendar/calendar/snapshot-diff.ts:33](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/schedule/calendar/calendar/snapshot-diff.ts#L33)

***

### live?

> `optional` **live?**: [`Event`](../../../../../../api-shared/types/event/type-aliases/Event.md)

Defined in: [ui/src/components/schedule/calendar/calendar/snapshot-diff.ts:38](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/schedule/calendar/calendar/snapshot-diff.ts#L38)

The live version, when there is one.
