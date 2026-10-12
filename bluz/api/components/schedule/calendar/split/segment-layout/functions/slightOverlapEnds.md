[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/split/segment-layout](../index.md) / slightOverlapEnds

# Function: slightOverlapEnds()

> **slightOverlapEnds**(`events`, `accessors`): `Map`\<[`EventSegment`](../../segments/type-aliases/EventSegment.md), `Date`\>

Defined in: [ui/src/components/schedule/calendar/split/segment-layout.ts:47](https://github.com/System-B90/Bluz/blob/4bd90f164a3cfe171409116b1f28d79f80797dcd/ui/src/components/schedule/calendar/split/segment-layout.ts#L47)

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
