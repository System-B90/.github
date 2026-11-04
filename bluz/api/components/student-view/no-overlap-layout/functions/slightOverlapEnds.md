[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/student-view/no-overlap-layout](../index.md) / slightOverlapEnds

# Function: slightOverlapEnds()

> **slightOverlapEnds**\<`TEvent`\>(`events`, `accessors`): `Map`\<`TEvent`, `Date`\>

Defined in: [ui/src/components/student-view/no-overlap-layout.ts:38](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/components/student-view/no-overlap-layout.ts#L38)

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
