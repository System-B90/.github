[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/cut](../index.md) / countOverlappingOccurrences

# Function: countOverlappingOccurrences()

> **countOverlappingOccurrences**(`occurrences`, `events`): `number`

Defined in: [ui/src/api-server/gantt/cut.ts:526](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-server/gantt/cut.ts#L526)

Number of overlapping pairs of occurrences: two occurrences on the same date
whose time ranges intersect. Purely informational for the cut summary.
Shuffle-group siblings (#699) run side by side by design, so a pair sharing a
`groupId` is not an overlap that needs manual fixing.

## Parameters

### occurrences

[`PlannedOccurrence`](../../../../api-shared/gantt/cut-planner/type-aliases/PlannedOccurrence.md)[]

### events

[`CutPlanEventInput`](../../../../api-shared/gantt/cut-planner/type-aliases/CutPlanEventInput.md)[]

## Returns

`number`
