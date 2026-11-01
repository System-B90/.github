[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/curriculum-view/gantt-time-utils](../index.md) / getWeekOverAllocationSeverity

# Function: getWeekOverAllocationSeverity()

> **getWeekOverAllocationSeverity**(`days`): `"error"` \| `"warning"` \| `null`

Defined in: [ui/src/components/gantt/curriculum-view/gantt-time-utils.ts:343](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/components/gantt/curriculum-view/gantt-time-utils.ts#L343)

Severity of a week's over-allocation, for the weeks-view week header (#467).

A single day spilling over its own hours is recoverable — the work can move
to another day in the same week — so it is amber. Red is reserved for the
case that no reshuffle can fix: the week needs more hours than it has in
total. `null` means no day is over its capacity at all.

## Parameters

### days

readonly `object`[]

## Returns

`"error"` \| `"warning"` \| `null`
