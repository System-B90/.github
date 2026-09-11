[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/cut](../index.md) / buildCutPlanInput

# Function: buildCutPlanInput()

> **buildCutPlanInput**(`args`): [`CutPlanInput`](../../../../api-shared/gantt/cut-planner/type-aliases/CutPlanInput.md)

Defined in: [ui/src/api-server/gantt/cut.ts:290](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/gantt/cut.ts#L290)

Adapt the loaded Postgres rows into the pure planner's plain-data input.
Weeks are ordered by `number` and days within a week by `dayIndex`, matching
the timeline ordering used by the client normalizer.

## Parameters

### args

#### breakfastTime?

`string`

#### constraints?

[`GanttConstraint`](../../../../api-shared/types/gantt/models/constraint/type-aliases/GanttConstraint.md)[]

Constraint rows for this curriculum (owned by its events and modules).

#### curriculum

[`ApiCurriculum`](../../../../api-shared/types/gantt/api-layer/type-aliases/ApiCurriculum.md)

#### dayStartTime

`string`

#### dinnerTime?

`string`

#### exceptions

[`CutExceptionRow`](../type-aliases/CutExceptionRow.md)[]

#### lunchTime?

`string`

#### mappings

[`CutMappingRow`](../type-aliases/CutMappingRow.md)[]

#### prayerTimes?

`object`[]

Prayer windows bridged over from the MongoDB schedule settings.

#### weekendHomeStartTime?

`string`

## Returns

[`CutPlanInput`](../../../../api-shared/gantt/cut-planner/type-aliases/CutPlanInput.md)
