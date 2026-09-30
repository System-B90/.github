[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/cut-planner](../index.md) / CutPlanReport

# Type Alias: CutPlanReport

> **CutPlanReport** = `object`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:249](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/gantt/cut-planner.ts#L249)

Everything the balancer and the break pass did, for the preview and dialog.

## Properties

### breaks

> **breaks**: [`GeneratedBreak`](../../cut-breaks/type-aliases/GeneratedBreak.md) & `object`[]

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:257](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/gantt/cut-planner.ts#L257)

Breaks the post-pass inserted, keyed to the day they landed on.

***

### constraintProposals

> **constraintProposals**: [`ConstraintMoveProposal`](../../cut-constraints/type-aliases/ConstraintMoveProposal.md)[]

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:259](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/gantt/cut-planner.ts#L259)

Cross-day moves the constraint solver would like to make.

***

### constraintViolations

> **constraintViolations**: [`ConstraintViolation`](../../cut-constraints/type-aliases/ConstraintViolation.md)[]

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:261](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/gantt/cut-planner.ts#L261)

Constraints no legal placement satisfies.

***

### decisions

> **decisions**: [`CutDecision`](CutDecision.md)[]

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:263](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/gantt/cut-planner.ts#L263)

Open questions for the dialog, in the order they should be asked.

***

### moves

> **moves**: [`SpillMove`](../../cut-balancer/type-aliases/SpillMove.md)[]

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:251](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/gantt/cut-planner.ts#L251)

Occurrences the balancer relocated to a later day in the same week.

***

### overflows

> **overflows**: [`WeekOverflow`](../../cut-balancer/type-aliases/WeekOverflow.md)[]

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:255](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/gantt/cut-planner.ts#L255)

Weeks that still exceed their working hours after balancing.

***

### spills

> **spills**: [`CutSpillDetail`](CutSpillDetail.md)[]

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:253](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/gantt/cut-planner.ts#L253)

The same relocations, resolved to titles and dates for display.
