[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/cut](../index.md) / countOverlappingOccurrences

# Function: countOverlappingOccurrences()

> **countOverlappingOccurrences**(`occurrences`): `number`

Defined in: [ui/src/api-server/gantt/cut.ts:422](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/gantt/cut.ts#L422)

Number of overlapping pairs of occurrences: two occurrences on the same date
whose time ranges intersect. Purely informational for the cut summary.

## Parameters

### occurrences

[`PlannedOccurrence`](../../../../api-shared/gantt/cut-planner/type-aliases/PlannedOccurrence.md)[]

## Returns

`number`
