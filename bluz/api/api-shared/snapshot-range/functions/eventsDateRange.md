[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/snapshot-range](../index.md) / eventsDateRange

# Function: eventsDateRange()

> **eventsDateRange**(`events`): `object`

Defined in: [ui/src/api-shared/snapshot-range.ts:14](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/snapshot-range.ts#L14)

The span a set of events covers: earliest start to latest end.

Folded rather than spread into `Math.min`/`Math.max` (#614): spreading passes
one argument per event, which overflows the call stack on a large snapshot.

## Parameters

### events

readonly `Timed`[]

## Returns

`object`

### rangeEnd

> **rangeEnd**: `Date`

### rangeStart

> **rangeStart**: `Date`
