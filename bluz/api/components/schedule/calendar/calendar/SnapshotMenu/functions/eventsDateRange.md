[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar/SnapshotMenu](../index.md) / eventsDateRange

# Function: eventsDateRange()

> **eventsDateRange**(`events`): `object`

Defined in: [ui/src/components/schedule/calendar/calendar/SnapshotMenu.tsx:38](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/components/schedule/calendar/calendar/SnapshotMenu.tsx#L38)

The span a set of restored events covers.

Folded rather than spread into `Math.min`/`Math.max` (#614): spreading passes
one argument per event, which overflows the call stack on a large snapshot
and surfaces as an opaque "restore failed".

## Parameters

### events

[`Event`](../../../../../../api-shared/types/event/type-aliases/Event.md)[]

## Returns

`object`

### rangeEnd

> **rangeEnd**: `Date`

### rangeStart

> **rangeStart**: `Date`
