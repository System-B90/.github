[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/split/segment-layout](../index.md) / slightOverlapEnds

# Function: slightOverlapEnds()

> **slightOverlapEnds**(`events`, `accessors`): `Map`\<[`EventSegment`](../../segments/type-aliases/EventSegment.md), `Date`\>

Defined in: [ui/src/components/schedule/calendar/split/segment-layout.ts:41](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/components/schedule/calendar/split/segment-layout.ts#L41)

For each event that runs at most [SLIGHT\_OVERLAP\_MS](../variables/SLIGHT_OVERLAP_MS.md) into a later
one, the later event's start: where the layout should consider it ended.
Starting together is never "slight"; those still share the column.

## Parameters

### events

[`EventSegment`](../../segments/type-aliases/EventSegment.md)[]

### accessors

`Accessors`

## Returns

`Map`\<[`EventSegment`](../../segments/type-aliases/EventSegment.md), `Date`\>
