[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/cut](../index.md) / MaterializationOutcome

# Type Alias: MaterializationOutcome

> **MaterializationOutcome** = \{ `errors`: [`CutValidationError`](../../../../api-shared/gantt/cut-planner/type-aliases/CutValidationError.md)[]; `ok`: `false`; `weeks`: [`ApiCutWeek`](../../../../api-shared/types/gantt/cut/type-aliases/ApiCutWeek.md)[]; \} \| \{ `createdCourses`: `object`[]; `documents`: [`DbEventDocument`](../../../../api-shared/types/event/type-aliases/DbEventDocument.md)[]; `hiveSubjectsUnavailable`: `boolean`; `ok`: `true`; `overlaps`: `number`; `report`: [`CutPlanReport`](../../../../api-shared/gantt/cut-planner/type-aliases/CutPlanReport.md); `weekRange`: `DateRange` \| `null`; `weeks`: [`ApiCutWeek`](../../../../api-shared/types/gantt/cut/type-aliases/ApiCutWeek.md)[]; \}

Defined in: [ui/src/api-server/gantt/cut.ts:1329](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-server/gantt/cut.ts#L1329)

The documents a plan materializes into, plus what producing them created.

## Union Members

### Type Literal

\{ `errors`: [`CutValidationError`](../../../../api-shared/gantt/cut-planner/type-aliases/CutValidationError.md)[]; `ok`: `false`; `weeks`: [`ApiCutWeek`](../../../../api-shared/types/gantt/cut/type-aliases/ApiCutWeek.md)[]; \}

***

### Type Literal

\{ `createdCourses`: `object`[]; `documents`: [`DbEventDocument`](../../../../api-shared/types/event/type-aliases/DbEventDocument.md)[]; `hiveSubjectsUnavailable`: `boolean`; `ok`: `true`; `overlaps`: `number`; `report`: [`CutPlanReport`](../../../../api-shared/gantt/cut-planner/type-aliases/CutPlanReport.md); `weekRange`: `DateRange` \| `null`; `weeks`: [`ApiCutWeek`](../../../../api-shared/types/gantt/cut/type-aliases/ApiCutWeek.md)[]; \}

#### createdCourses

> **createdCourses**: `object`[]

#### documents

> **documents**: [`DbEventDocument`](../../../../api-shared/types/event/type-aliases/DbEventDocument.md)[]

#### hiveSubjectsUnavailable

> **hiveSubjectsUnavailable**: `boolean`

True when Hive could not supply the module → subject map and at
least one event was left subject-less because of it (#662). The
events are still written; the caller is expected to tell the user
a reload will fix their colors.

#### ok

> **ok**: `true`

#### overlaps

> **overlaps**: `number`

#### report

> **report**: [`CutPlanReport`](../../../../api-shared/gantt/cut-planner/type-aliases/CutPlanReport.md)

What the balancer, break pass and constraint solver did.

#### weekRange

> **weekRange**: `DateRange` \| `null`

The cut week's dates, when only one week was asked for (#970).

#### weeks

> **weeks**: [`ApiCutWeek`](../../../../api-shared/types/gantt/cut/type-aliases/ApiCutWeek.md)[]

The timeline's weeks, for picking one to cut.
