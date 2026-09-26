[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/cut-planner](../index.md) / CutPlanReport

# Type Alias: CutPlanReport

> **CutPlanReport** = `object`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:244](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-planner.ts#L244)

Everything the balancer and the break pass did, for the preview and dialog.

## Properties

### breaks

> **breaks**: [`GeneratedBreak`](../../cut-breaks/type-aliases/GeneratedBreak.md) & `object`[]

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:252](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-planner.ts#L252)

Breaks the post-pass inserted, keyed to the day they landed on.

***

### constraintProposals

> **constraintProposals**: [`ConstraintMoveProposal`](../../cut-constraints/type-aliases/ConstraintMoveProposal.md)[]

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:254](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-planner.ts#L254)

Cross-day moves the constraint solver would like to make.

***

### constraintViolations

> **constraintViolations**: [`ConstraintViolation`](../../cut-constraints/type-aliases/ConstraintViolation.md)[]

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:256](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-planner.ts#L256)

Constraints no legal placement satisfies.

***

### decisions

> **decisions**: [`CutDecision`](CutDecision.md)[]

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:258](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-planner.ts#L258)

Open questions for the dialog, in the order they should be asked.

***

### moves

> **moves**: [`SpillMove`](../../cut-balancer/type-aliases/SpillMove.md)[]

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:246](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-planner.ts#L246)

Occurrences the balancer relocated to a later day in the same week.

***

### overflows

> **overflows**: [`WeekOverflow`](../../cut-balancer/type-aliases/WeekOverflow.md)[]

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:250](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-planner.ts#L250)

Weeks that still exceed their working hours after balancing.

***

### spills

> **spills**: [`CutSpillDetail`](CutSpillDetail.md)[]

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:248](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-planner.ts#L248)

The same relocations, resolved to titles and dates for display.
