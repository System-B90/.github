[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/CalendarFilterProvider](../index.md) / isBusyDuring

# Function: isBusyDuring()

> **isBusyDuring**(`event`, `busy`): `boolean`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:124](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/components/base/CalendarFilterProvider.tsx#L124)

True when one of `busy` (other than `event` itself) overlaps `event`: the
instructor is busy then, so `event` is no PA slot for them.

## Parameters

### event

`Pick`\<[`Event`](../../../../api-shared/types/event/type-aliases/Event.md), `"endTime"` \| `"id"` \| `"startTime"`\>

### busy

[`BusyInterval`](../type-aliases/BusyInterval.md)[]

## Returns

`boolean`
