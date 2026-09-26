[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/calendar](../index.md) / eventDateFixupToDayjs

# Function: eventDateFixupToDayjs()

> **eventDateFixupToDayjs**\<`T`\>(`event`): `Omit`\<`T`, `"startTime"` \| `"endTime"`\> & `Pick`\<[`Event`](../../types/event/type-aliases/Event.md), `"startTime"` \| `"endTime"`\>

Defined in: [ui/src/api-shared/calendar.ts:45](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/calendar.ts#L45)

Client-side: turns startTime/endTime into a `Dayjs` anchored to the app
timezone, so the wall-clock is DST-correct and independent of the
viewer's browser timezone (#168).

## Type Parameters

### T

`T` *extends* `Partial`\<[`Event`](../../types/event/type-aliases/Event.md) \| [`DbEventDocument`](../../types/event/type-aliases/DbEventDocument.md)\>

## Parameters

### event

`T`

## Returns

`Omit`\<`T`, `"startTime"` \| `"endTime"`\> & `Pick`\<[`Event`](../../types/event/type-aliases/Event.md), `"startTime"` \| `"endTime"`\>
