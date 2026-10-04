[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/cut](../index.md) / MaterializationOutcome

# Type Alias: MaterializationOutcome

> **MaterializationOutcome** = \{ `errors`: [`CutValidationError`](../../../../api-shared/gantt/cut-planner/type-aliases/CutValidationError.md)[]; `ok`: `false`; \} \| \{ `createdCourses`: `object`[]; `documents`: [`DbEventDocument`](../../../../api-shared/types/event/type-aliases/DbEventDocument.md)[]; `hiveSubjectsUnavailable`: `boolean`; `ok`: `true`; `overlaps`: `number`; `report`: [`CutPlanReport`](../../../../api-shared/gantt/cut-planner/type-aliases/CutPlanReport.md); \}

Defined in: [ui/src/api-server/gantt/cut.ts:875](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/api-server/gantt/cut.ts#L875)

The documents a plan materializes into, plus what producing them created.

## Union Members

### Type Literal

\{ `errors`: [`CutValidationError`](../../../../api-shared/gantt/cut-planner/type-aliases/CutValidationError.md)[]; `ok`: `false`; \}

***

### Type Literal

\{ `createdCourses`: `object`[]; `documents`: [`DbEventDocument`](../../../../api-shared/types/event/type-aliases/DbEventDocument.md)[]; `hiveSubjectsUnavailable`: `boolean`; `ok`: `true`; `overlaps`: `number`; `report`: [`CutPlanReport`](../../../../api-shared/gantt/cut-planner/type-aliases/CutPlanReport.md); \}

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
