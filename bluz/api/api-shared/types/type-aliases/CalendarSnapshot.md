[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/types](../index.md) / CalendarSnapshot

# Type Alias: CalendarSnapshot

> **CalendarSnapshot** = `object`

Defined in: [ui/src/api-shared/types.ts:56](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-shared/types.ts#L56)

## Properties

### createdAt

> **createdAt**: `string`

Defined in: [ui/src/api-shared/types.ts:59](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-shared/types.ts#L59)

***

### events

> **events**: [`DbEventDocument`](../event/type-aliases/DbEventDocument.md)[]

Defined in: [ui/src/api-shared/types.ts:71](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-shared/types.ts#L71)

***

### id

> **id**: `string`

Defined in: [ui/src/api-shared/types.ts:57](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-shared/types.ts#L57)

***

### iterationId?

> `optional` **iterationId?**: `string`

Defined in: [ui/src/api-shared/types.ts:61](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-shared/types.ts#L61)

***

### label

> **label**: `string`

Defined in: [ui/src/api-shared/types.ts:58](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-shared/types.ts#L58)

***

### rangeEnd?

> `optional` **rangeEnd?**: `string`

Defined in: [ui/src/api-shared/types.ts:69](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-shared/types.ts#L69)

***

### rangeStart?

> `optional` **rangeStart?**: `string`

Defined in: [ui/src/api-shared/types.ts:68](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-shared/types.ts#L68)

Calendar range the snapshot covers (ISO instants). Restoring replaces
the live schedule inside this range only, so a range that held no
events restores to empty. Absent on snapshots taken before it existed —
the events' own span stands in.
