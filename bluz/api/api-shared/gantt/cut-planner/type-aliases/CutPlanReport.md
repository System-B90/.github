[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/cut-planner](../index.md) / CutPlanReport

# Type Alias: CutPlanReport

> **CutPlanReport** = `object`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:252](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/api-shared/gantt/cut-planner.ts#L252)

Everything the balancer and the break pass did, for the preview and dialog.

## Properties

### breaks

> **breaks**: [`GeneratedBreak`](../../cut-breaks/type-aliases/GeneratedBreak.md) & `object`[]

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:260](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/api-shared/gantt/cut-planner.ts#L260)

Breaks the post-pass inserted, keyed to the day they landed on.

***

### constraintProposals

> **constraintProposals**: [`ConstraintMoveProposal`](../../cut-constraints/type-aliases/ConstraintMoveProposal.md)[]

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:262](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/api-shared/gantt/cut-planner.ts#L262)

Cross-day moves the constraint solver would like to make.

***

### constraintViolations

> **constraintViolations**: [`ConstraintViolation`](../../cut-constraints/type-aliases/ConstraintViolation.md)[]

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:264](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/api-shared/gantt/cut-planner.ts#L264)

Constraints no legal placement satisfies.

***

### decisions

> **decisions**: [`CutDecision`](CutDecision.md)[]

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:266](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/api-shared/gantt/cut-planner.ts#L266)

Open questions for the dialog, in the order they should be asked.

***

### moves

> **moves**: [`SpillMove`](../../cut-balancer/type-aliases/SpillMove.md)[]

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:254](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/api-shared/gantt/cut-planner.ts#L254)

Occurrences the balancer relocated to a later day in the same week.

***

### overflows

> **overflows**: [`WeekOverflow`](../../cut-balancer/type-aliases/WeekOverflow.md)[]

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:258](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/api-shared/gantt/cut-planner.ts#L258)

Weeks that still exceed their working hours after balancing.

***

### spills

> **spills**: [`CutSpillDetail`](CutSpillDetail.md)[]

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:256](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/api-shared/gantt/cut-planner.ts#L256)

The same relocations, resolved to titles and dates for display.
