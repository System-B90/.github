[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/cut-balancer](../index.md) / balanceWeeks

# Function: balanceWeeks()

> **balanceWeeks**(`input`): [`BalancerResult`](../type-aliases/BalancerResult.md)

Defined in: [ui/src/api-shared/gantt/cut-balancer.ts:158](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-shared/gantt/cut-balancer.ts#L158)

Rebalance every week so no day carries more than its working window, moving
work only forward and only within its own week.

The invariants enforced here mirror [SPILLOVER\_RULES](../../cut-rules/variables/SPILLOVER_RULES.md):
spill never crosses a week boundary, never lands on a day that cannot hold
the event inside its window, and never places anything past a day's end.
When a week cannot absorb its own load, the leftover stays where it was
mapped (overlapping) and the week is reported as an overflow for the dialog
to resolve.

## Parameters

### input

[`BalancerInput`](../type-aliases/BalancerInput.md)

## Returns

[`BalancerResult`](../type-aliases/BalancerResult.md)
