[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/gantt/cut](../index.md) / ApiCurriculumCutPlanResponse

# Type Alias: ApiCurriculumCutPlanResponse

> **ApiCurriculumCutPlanResponse** = \{ `errors`: [`CutValidationError`](../../../../gantt/cut-planner/type-aliases/CutValidationError.md)[]; `ok`: `false`; \} \| \{ `ok`: `true`; `overlaps`: `number`; `plannedEvents`: `number`; `report`: [`CutPlanReport`](../../../../gantt/cut-planner/type-aliases/CutPlanReport.md); `weeks`: [`ApiCutWeek`](ApiCutWeek.md)[]; \}

Defined in: [ui/src/api-shared/types/gantt/cut.ts:73](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/types/gantt/cut.ts#L73)

Response of POST .../cut/plan — the "plan" half of the plan-then-confirm
flow. Runs the whole pipeline without writing and reports what the cut would
do plus every open question, so the dialog can ask them one at a time before
committing. Never writes.

## Union Members

### Type Literal

\{ `errors`: [`CutValidationError`](../../../../gantt/cut-planner/type-aliases/CutValidationError.md)[]; `ok`: `false`; \}

***

### Type Literal

\{ `ok`: `true`; `overlaps`: `number`; `plannedEvents`: `number`; `report`: [`CutPlanReport`](../../../../gantt/cut-planner/type-aliases/CutPlanReport.md); `weeks`: [`ApiCutWeek`](ApiCutWeek.md)[]; \}

#### ok

> **ok**: `true`

#### overlaps

> **overlaps**: `number`

#### plannedEvents

> **plannedEvents**: `number`

Schedule events the commit would create.

#### report

> **report**: [`CutPlanReport`](../../../../gantt/cut-planner/type-aliases/CutPlanReport.md)

What the balancer, break pass and constraint solver did.

#### weeks

> **weeks**: [`ApiCutWeek`](ApiCutWeek.md)[]

The timeline's weeks, for a single-week cut (#970).
