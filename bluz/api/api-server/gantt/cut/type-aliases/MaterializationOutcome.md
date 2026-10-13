[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/cut](../index.md) / MaterializationOutcome

# Type Alias: MaterializationOutcome

> **MaterializationOutcome** = \{ `errors`: [`CutValidationError`](../../../../api-shared/gantt/cut-planner/type-aliases/CutValidationError.md)[]; `ok`: `false`; \} \| \{ `createdCourses`: `object`[]; `documents`: [`DbEventDocument`](../../../../api-shared/types/event/type-aliases/DbEventDocument.md)[]; `hiveSubjectsUnavailable`: `boolean`; `ok`: `true`; `overlaps`: `number`; `report`: [`CutPlanReport`](../../../../api-shared/gantt/cut-planner/type-aliases/CutPlanReport.md); `weekRange`: `DateRange` \| `null`; `weeks`: [`ApiCutWeek`](../../../../api-shared/types/gantt/cut/type-aliases/ApiCutWeek.md)[]; \}

Defined in: [ui/src/api-server/gantt/cut.ts:979](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-server/gantt/cut.ts#L979)

The documents a plan materializes into, plus what producing them created.

## Union Members

### Type Literal

\{ `errors`: [`CutValidationError`](../../../../api-shared/gantt/cut-planner/type-aliases/CutValidationError.md)[]; `ok`: `false`; \}

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
a reload will fix their colours.

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
