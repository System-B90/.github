[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/student-view/no-overlap-layout](../index.md) / slightOverlapEnds

# Function: slightOverlapEnds()

> **slightOverlapEnds**\<`TEvent`\>(`events`, `accessors`): `Map`\<`TEvent`, `Date`\>

Defined in: [ui/src/components/student-view/no-overlap-layout.ts:38](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/components/student-view/no-overlap-layout.ts#L38)

For each event that runs at most [SLIGHT\_OVERLAP\_MS](../variables/SLIGHT_OVERLAP_MS.md) into a later
one, the later event's start: where the layout should consider it ended.
Starting together is never "slight"; those still share the column.

## Type Parameters

### TEvent

`TEvent`

## Parameters

### events

`TEvent`[]

### accessors

`Accessors`\<`TEvent`\>

## Returns

`Map`\<`TEvent`, `Date`\>
