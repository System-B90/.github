[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/calendar](../index.md) / eventDateFixupToDayjs

# Function: eventDateFixupToDayjs()

> **eventDateFixupToDayjs**\<`T`\>(`event`): `Omit`\<`T`, `"startTime"` \| `"endTime"`\> & `Pick`\<[`Event`](../../types/event/type-aliases/Event.md), `"startTime"` \| `"endTime"`\>

Defined in: [ui/src/api-shared/calendar.ts:48](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-shared/calendar.ts#L48)

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
