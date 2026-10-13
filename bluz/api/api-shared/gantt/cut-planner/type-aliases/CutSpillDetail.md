[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/cut-planner](../index.md) / CutSpillDetail

# Type Alias: CutSpillDetail

> **CutSpillDetail** = `object`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:236](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/gantt/cut-planner.ts#L236)

One relocated slot, described in terms a user can read: which event moved,
from which date to which. A slot the balancer bounced twice (off ראשון, then
off שני) collapses into a single detail spanning its first and last day.

## Properties

### durationMinutes

> **durationMinutes**: `number`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:247](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/gantt/cut-planner.ts#L247)

***

### eventId

> **eventId**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:238](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/gantt/cut-planner.ts#L238)

***

### fromDate

> **fromDate**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:244](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/gantt/cut-planner.ts#L244)

ISO date (yyyy-MM-dd) the slot was originally mapped to.

***

### fromDayId

> **fromDayId**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:241](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/gantt/cut-planner.ts#L241)

***

### slotKey

> **slotKey**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:237](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/gantt/cut-planner.ts#L237)

***

### title

> **title**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:240](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/gantt/cut-planner.ts#L240)

Event title at plan time; falls back to the id for generated slots.

***

### toDate

> **toDate**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:246](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/gantt/cut-planner.ts#L246)

ISO date (yyyy-MM-dd) it ended up on.

***

### toDayId

> **toDayId**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:242](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/gantt/cut-planner.ts#L242)
