[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/types](../index.md) / CalendarDraft

# Type Alias: CalendarDraft

> **CalendarDraft** = `object`

Defined in: [ui/src/api-shared/types.ts:86](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/types.ts#L86)

## Properties

### createdAt

> **createdAt**: `string`

Defined in: [ui/src/api-shared/types.ts:89](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/types.ts#L89)

***

### events

> **events**: [`DbEventDocument`](../event/type-aliases/DbEventDocument.md)[]

Defined in: [ui/src/api-shared/types.ts:103](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/types.ts#L103)

***

### id

> **id**: `string`

Defined in: [ui/src/api-shared/types.ts:87](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/types.ts#L87)

***

### iterationId?

> `optional` **iterationId?**: `string`

Defined in: [ui/src/api-shared/types.ts:94](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/types.ts#L94)

***

### label

> **label**: `string`

Defined in: [ui/src/api-shared/types.ts:88](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/types.ts#L88)

***

### rangeEnd?

> `optional` **rangeEnd?**: `string`

Defined in: [ui/src/api-shared/types.ts:102](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/types.ts#L102)

***

### rangeStart?

> `optional` **rangeStart?**: `string`

Defined in: [ui/src/api-shared/types.ts:101](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/types.ts#L101)

Calendar range the draft covers (ISO instants). Publishing a draft
replaces the live schedule inside this range only: a live event in it
that the draft lacks is one the draft deleted. Absent on drafts saved
before it existed — the events' own span stands in.

***

### updatedAt

> **updatedAt**: `string`

Defined in: [ui/src/api-shared/types.ts:90](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/types.ts#L90)

***

### updatedBy

> **updatedBy**: `string`

Defined in: [ui/src/api-shared/types.ts:91](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/types.ts#L91)

***

### updatedById?

> `optional` **updatedById?**: `string`

Defined in: [ui/src/api-shared/types.ts:92](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/types.ts#L92)
