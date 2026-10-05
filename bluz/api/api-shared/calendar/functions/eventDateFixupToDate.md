[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/calendar](../index.md) / eventDateFixupToDate

# Function: eventDateFixupToDate()

> **eventDateFixupToDate**\<`T`\>(`event`): `Omit`\<`T`, `"startTime"` \| `"endTime"`\> & `Pick`\<[`DbEventDocument`](../../types/event/type-aliases/DbEventDocument.md), `"startTime"` \| `"endTime"`\>

Defined in: [ui/src/api-shared/calendar.ts:23](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-shared/calendar.ts#L23)

Server-side: turns startTime/endTime into native `Date`s.

## Type Parameters

### T

`T` *extends* `Partial`\<[`Event`](../../types/event/type-aliases/Event.md) \| [`DbEventDocument`](../../types/event/type-aliases/DbEventDocument.md)\>

## Parameters

### event

`T`

## Returns

`Omit`\<`T`, `"startTime"` \| `"endTime"`\> & `Pick`\<[`DbEventDocument`](../../types/event/type-aliases/DbEventDocument.md), `"startTime"` \| `"endTime"`\>
