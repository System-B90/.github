[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/cut-balancer](../index.md) / balanceWeeks

# Function: balanceWeeks()

> **balanceWeeks**(`input`): [`BalancerResult`](../type-aliases/BalancerResult.md)

Defined in: [ui/src/api-shared/gantt/cut-balancer.ts:158](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/gantt/cut-balancer.ts#L158)

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
