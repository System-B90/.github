[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/snapshot-range](../index.md) / eventsDateRange

# Function: eventsDateRange()

> **eventsDateRange**(`events`): `object`

Defined in: [ui/src/api-shared/snapshot-range.ts:14](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-shared/snapshot-range.ts#L14)

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
