[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/cut-balancer](../index.md) / WeekOverflow

# Type Alias: WeekOverflow

> **WeekOverflow** = `object`

Defined in: [ui/src/api-shared/gantt/cut-balancer.ts:68](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/gantt/cut-balancer.ts#L68)

A week whose load exceeds its own working hours even after balancing.

## Properties

### appliedResolution

> **appliedResolution**: [`WeekOverflowResolution`](../../cut-rules/type-aliases/WeekOverflowResolution.md)

Defined in: [ui/src/api-shared/gantt/cut-balancer.ts:75](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/gantt/cut-balancer.ts#L75)

What the balancer did, absent a user decision.

***

### excessMinutes

> **excessMinutes**: `number`

Defined in: [ui/src/api-shared/gantt/cut-balancer.ts:71](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/gantt/cut-balancer.ts#L71)

Minutes of load that could not be placed inside any day's window.

***

### overloadedDays

> **overloadedDays**: `object`[]

Defined in: [ui/src/api-shared/gantt/cut-balancer.ts:73](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/gantt/cut-balancer.ts#L73)

Day ids still over capacity, with their overflow.

#### dayId

> **dayId**: `string`

#### overflowMinutes

> **overflowMinutes**: `number`

***

### weekId

> **weekId**: `string`

Defined in: [ui/src/api-shared/gantt/cut-balancer.ts:69](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/gantt/cut-balancer.ts#L69)
