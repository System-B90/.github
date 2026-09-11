[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/cut-planner](../index.md) / CutSpillDetail

# Type Alias: CutSpillDetail

> **CutSpillDetail** = `object`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:223](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/gantt/cut-planner.ts#L223)

One relocated slot, described in terms a user can read: which event moved,
from which date to which. A slot the balancer bounced twice (off ראשון, then
off שני) collapses into a single detail spanning its first and last day.

## Properties

### durationMinutes

> **durationMinutes**: `number`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:234](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/gantt/cut-planner.ts#L234)

***

### eventId

> **eventId**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:225](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/gantt/cut-planner.ts#L225)

***

### fromDate

> **fromDate**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:231](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/gantt/cut-planner.ts#L231)

ISO date (yyyy-MM-dd) the slot was originally mapped to.

***

### fromDayId

> **fromDayId**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:228](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/gantt/cut-planner.ts#L228)

***

### slotKey

> **slotKey**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:224](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/gantt/cut-planner.ts#L224)

***

### title

> **title**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:227](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/gantt/cut-planner.ts#L227)

Event title at plan time; falls back to the id for generated slots.

***

### toDate

> **toDate**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:233](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/gantt/cut-planner.ts#L233)

ISO date (yyyy-MM-dd) it ended up on.

***

### toDayId

> **toDayId**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:229](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/gantt/cut-planner.ts#L229)
