[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/snapshot-range](../index.md) / eventsDateRange

# Function: eventsDateRange()

> **eventsDateRange**(`events`): `object`

Defined in: [ui/src/api-shared/snapshot-range.ts:14](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-shared/snapshot-range.ts#L14)

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
