[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/gantt/cut](../index.md) / ApiCurriculumCutPreviewResponse

# Type Alias: ApiCurriculumCutPreviewResponse

> **ApiCurriculumCutPreviewResponse** = \{ `errors`: [`CutValidationError`](../../../../gantt/cut-planner/type-aliases/CutValidationError.md)[]; `ok`: `false`; \} \| \{ `occurrences`: [`ApiCutPreviewOccurrence`](ApiCutPreviewOccurrence.md)[]; `ok`: `true`; `overlaps`: `number`; `report`: [`CutPlanReport`](../../../../gantt/cut-planner/type-aliases/CutPlanReport.md); `skipped`: [`CutValidationError`](../../../../gantt/cut-planner/type-aliases/CutValidationError.md)[]; \}

Defined in: [ui/src/api-shared/types/gantt/cut.ts:130](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/cut.ts#L130)

Response of GET .../cut/preview — a dry-run of the cut planner. Never
writes. `ok: false` carries the planner's validation errors (e.g. missing
start date) so the preview UI can explain why nothing renders.

## Union Members

### Type Literal

\{ `errors`: [`CutValidationError`](../../../../gantt/cut-planner/type-aliases/CutValidationError.md)[]; `ok`: `false`; \}

***

### Type Literal

\{ `occurrences`: [`ApiCutPreviewOccurrence`](ApiCutPreviewOccurrence.md)[]; `ok`: `true`; `overlaps`: `number`; `report`: [`CutPlanReport`](../../../../gantt/cut-planner/type-aliases/CutPlanReport.md); `skipped`: [`CutValidationError`](../../../../gantt/cut-planner/type-aliases/CutValidationError.md)[]; \}

#### occurrences

> **occurrences**: [`ApiCutPreviewOccurrence`](ApiCutPreviewOccurrence.md)[]

#### ok

> **ok**: `true`

#### overlaps

> **overlaps**: `number`

#### report

> **report**: [`CutPlanReport`](../../../../gantt/cut-planner/type-aliases/CutPlanReport.md)

What the balancer, break pass and constraint solver did.

#### skipped

> **skipped**: [`CutValidationError`](../../../../gantt/cut-planner/type-aliases/CutValidationError.md)[]

Events the real cut would reject (unmapped / unsatisfied
recurrence) that the preview skipped instead of failing on.
