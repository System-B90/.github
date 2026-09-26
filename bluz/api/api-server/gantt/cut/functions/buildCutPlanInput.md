[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/cut](../index.md) / buildCutPlanInput

# Function: buildCutPlanInput()

> **buildCutPlanInput**(`args`): [`CutPlanInput`](../../../../api-shared/gantt/cut-planner/type-aliases/CutPlanInput.md)

Defined in: [ui/src/api-server/gantt/cut.ts:317](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/gantt/cut.ts#L317)

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
