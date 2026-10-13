[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/cut](../index.md) / buildGeneratedBreakEvent

# Function: buildGeneratedBreakEvent()

> **buildGeneratedBreakEvent**(`occurrence`, `courseIds`, `curriculumId`): [`DbEventDocument`](../../../../api-shared/types/event/type-aliases/DbEventDocument.md)

Defined in: [ui/src/api-server/gantt/cut.ts:628](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-server/gantt/cut.ts#L628)

Build a schedule event for a break the post-pass invented. It has no gantt
event behind it, so everything comes from the occurrence itself. The
synthetic `ganttEventId` marks it as cut-generated, which is exactly what
`pullBackCutSchedule` matches on — breaks are archived with the rest of the
cut and never survive to be duplicated by a re-cut.

## Parameters

### occurrence

[`PlannedOccurrence`](../../../../api-shared/gantt/cut-planner/type-aliases/PlannedOccurrence.md)

### courseIds

`string`[]

### curriculumId

`string`

## Returns

[`DbEventDocument`](../../../../api-shared/types/event/type-aliases/DbEventDocument.md)
