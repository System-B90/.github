[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/types](../index.md) / CalendarDraft

# Type Alias: CalendarDraft

> **CalendarDraft** = `object`

Defined in: [ui/src/api-shared/types.ts:103](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-shared/types.ts#L103)

## Properties

### createdAt

> **createdAt**: `string`

Defined in: [ui/src/api-shared/types.ts:106](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-shared/types.ts#L106)

***

### events

> **events**: [`DbEventDocument`](../event/type-aliases/DbEventDocument.md)[]

Defined in: [ui/src/api-shared/types.ts:120](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-shared/types.ts#L120)

***

### id

> **id**: `string`

Defined in: [ui/src/api-shared/types.ts:104](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-shared/types.ts#L104)

***

### iterationId?

> `optional` **iterationId?**: `string`

Defined in: [ui/src/api-shared/types.ts:111](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-shared/types.ts#L111)

***

### label

> **label**: `string`

Defined in: [ui/src/api-shared/types.ts:105](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-shared/types.ts#L105)

***

### rangeEnd?

> `optional` **rangeEnd?**: `string`

Defined in: [ui/src/api-shared/types.ts:119](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-shared/types.ts#L119)

***

### rangeStart?

> `optional` **rangeStart?**: `string`

Defined in: [ui/src/api-shared/types.ts:118](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-shared/types.ts#L118)

Calendar range the draft covers (ISO instants). Publishing a draft
replaces the live schedule inside this range only: a live event in it
that the draft lacks is one the draft deleted. Absent on drafts saved
before it existed — the events' own span stands in.

***

### updatedAt

> **updatedAt**: `string`

Defined in: [ui/src/api-shared/types.ts:107](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-shared/types.ts#L107)

***

### updatedBy

> **updatedBy**: `string`

Defined in: [ui/src/api-shared/types.ts:108](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-shared/types.ts#L108)

***

### updatedById?

> `optional` **updatedById?**: `string`

Defined in: [ui/src/api-shared/types.ts:109](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-shared/types.ts#L109)
