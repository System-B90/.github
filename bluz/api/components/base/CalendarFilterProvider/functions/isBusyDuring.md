[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/CalendarFilterProvider](../index.md) / isBusyDuring

# Function: isBusyDuring()

> **isBusyDuring**(`event`, `busy`): `boolean`

Defined in: [ui/src/components/base/CalendarFilterProvider.tsx:134](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/base/CalendarFilterProvider.tsx#L134)

True when one of `busy` (other than `event` itself) overlaps `event`: the
instructor is busy then, so `event` is no PA slot for them.

## Parameters

### event

`Pick`\<[`Event`](../../../../api-shared/types/event/type-aliases/Event.md), `"endTime"` \| `"id"` \| `"startTime"`\>

### busy

[`BusyInterval`](../type-aliases/BusyInterval.md)[]

## Returns

`boolean`
