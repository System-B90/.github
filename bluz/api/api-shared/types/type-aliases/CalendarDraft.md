[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/types](../index.md) / CalendarDraft

# Type Alias: CalendarDraft

> **CalendarDraft** = `object`

Defined in: [ui/src/api-shared/types.ts:94](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/api-shared/types.ts#L94)

## Properties

### createdAt

> **createdAt**: `string`

Defined in: [ui/src/api-shared/types.ts:97](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/api-shared/types.ts#L97)

***

### events

> **events**: [`DbEventDocument`](../event/type-aliases/DbEventDocument.md)[]

Defined in: [ui/src/api-shared/types.ts:111](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/api-shared/types.ts#L111)

***

### id

> **id**: `string`

Defined in: [ui/src/api-shared/types.ts:95](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/api-shared/types.ts#L95)

***

### iterationId?

> `optional` **iterationId?**: `string`

Defined in: [ui/src/api-shared/types.ts:102](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/api-shared/types.ts#L102)

***

### label

> **label**: `string`

Defined in: [ui/src/api-shared/types.ts:96](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/api-shared/types.ts#L96)

***

### rangeEnd?

> `optional` **rangeEnd?**: `string`

Defined in: [ui/src/api-shared/types.ts:110](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/api-shared/types.ts#L110)

***

### rangeStart?

> `optional` **rangeStart?**: `string`

Defined in: [ui/src/api-shared/types.ts:109](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/api-shared/types.ts#L109)

Calendar range the draft covers (ISO instants). Publishing a draft
replaces the live schedule inside this range only: a live event in it
that the draft lacks is one the draft deleted. Absent on drafts saved
before it existed — the events' own span stands in.

***

### updatedAt

> **updatedAt**: `string`

Defined in: [ui/src/api-shared/types.ts:98](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/api-shared/types.ts#L98)

***

### updatedBy

> **updatedBy**: `string`

Defined in: [ui/src/api-shared/types.ts:99](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/api-shared/types.ts#L99)

***

### updatedById?

> `optional` **updatedById?**: `string`

Defined in: [ui/src/api-shared/types.ts:100](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/api-shared/types.ts#L100)
