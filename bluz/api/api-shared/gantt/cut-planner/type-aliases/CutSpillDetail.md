[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/cut-planner](../index.md) / CutSpillDetail

# Type Alias: CutSpillDetail

> **CutSpillDetail** = `object`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:259](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/gantt/cut-planner.ts#L259)

One relocated slot, described in terms a user can read: which event moved,
from which date to which. A slot the balancer bounced twice (off ראשון, then
off שני) collapses into a single detail spanning its first and last day.

## Properties

### durationMinutes

> **durationMinutes**: `number`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:270](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/gantt/cut-planner.ts#L270)

***

### eventId

> **eventId**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:261](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/gantt/cut-planner.ts#L261)

***

### fromDate

> **fromDate**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:267](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/gantt/cut-planner.ts#L267)

ISO date (yyyy-MM-dd) the slot was originally mapped to.

***

### fromDayId

> **fromDayId**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:264](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/gantt/cut-planner.ts#L264)

***

### slotKey

> **slotKey**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:260](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/gantt/cut-planner.ts#L260)

***

### title

> **title**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:263](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/gantt/cut-planner.ts#L263)

Event title at plan time; falls back to the id for generated slots.

***

### toDate

> **toDate**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:269](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/gantt/cut-planner.ts#L269)

ISO date (yyyy-MM-dd) it ended up on.

***

### toDayId

> **toDayId**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:265](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/gantt/cut-planner.ts#L265)
