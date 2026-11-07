[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/CalendarFilterProvider](../index.md) / isBusyDuring

# Function: isBusyDuring()

> **isBusyDuring**(`event`, `busy`): `boolean`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:124](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/components/base/CalendarFilterProvider.tsx#L124)

True when one of `busy` (other than `event` itself) overlaps `event`: the
instructor is busy then, so `event` is no PA slot for them.

## Parameters

### event

`Pick`\<[`Event`](../../../../api-shared/types/event/type-aliases/Event.md), `"endTime"` \| `"id"` \| `"startTime"`\>

### busy

[`BusyInterval`](../type-aliases/BusyInterval.md)[]

## Returns

`boolean`
