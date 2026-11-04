[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/cut-planner](../index.md) / CutPlanReport

# Type Alias: CutPlanReport

> **CutPlanReport** = `object`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:275](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-shared/gantt/cut-planner.ts#L275)

Everything the balancer and the break pass did, for the preview and dialog.

## Properties

### breaks

> **breaks**: [`GeneratedBreak`](../../cut-breaks/type-aliases/GeneratedBreak.md) & `object`[]

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:283](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-shared/gantt/cut-planner.ts#L283)

Breaks the post-pass inserted, keyed to the day they landed on.

***

### constraintProposals

> **constraintProposals**: [`ConstraintMoveProposal`](../../cut-constraints/type-aliases/ConstraintMoveProposal.md)[]

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:285](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-shared/gantt/cut-planner.ts#L285)

Cross-day moves the constraint solver would like to make.

***

### constraintViolations

> **constraintViolations**: [`ConstraintViolation`](../../cut-constraints/type-aliases/ConstraintViolation.md)[]

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:287](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-shared/gantt/cut-planner.ts#L287)

Constraints no legal placement satisfies.

***

### decisions

> **decisions**: [`CutDecision`](CutDecision.md)[]

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:289](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-shared/gantt/cut-planner.ts#L289)

Open questions for the dialog, in the order they should be asked.

***

### moves

> **moves**: [`SpillMove`](../../cut-balancer/type-aliases/SpillMove.md)[]

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:277](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-shared/gantt/cut-planner.ts#L277)

Occurrences the balancer relocated to a later day in the same week.

***

### overflows

> **overflows**: [`WeekOverflow`](../../cut-balancer/type-aliases/WeekOverflow.md)[]

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:281](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-shared/gantt/cut-planner.ts#L281)

Weeks that still exceed their working hours after balancing.

***

### spills

> **spills**: [`CutSpillDetail`](CutSpillDetail.md)[]

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:279](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-shared/gantt/cut-planner.ts#L279)

The same relocations, resolved to titles and dates for display.
