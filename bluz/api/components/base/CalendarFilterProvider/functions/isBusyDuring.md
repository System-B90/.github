[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/CalendarFilterProvider](../index.md) / isBusyDuring

# Function: isBusyDuring()

> **isBusyDuring**(`event`, `busy`): `boolean`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:163](https://github.com/System-B90/Bluz/blob/04ebae9cb334a01c6e7a55f885993f021e83cd92/ui/src/components/base/CalendarFilterProvider.tsx#L163)

True when one of `busy` (other than `event` itself) overlaps `event`: the
instructor is busy then, so `event` is no PA slot for them.

## Parameters

### event

`Pick`\<[`Event`](../../../../api-shared/types/event/type-aliases/Event.md), `"endTime"` \| `"id"` \| `"startTime"`\>

### busy

[`BusyInterval`](../type-aliases/BusyInterval.md)[]

## Returns

`boolean`
