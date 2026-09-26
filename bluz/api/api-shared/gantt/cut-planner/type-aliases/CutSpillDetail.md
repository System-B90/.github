[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/cut-planner](../index.md) / CutSpillDetail

# Type Alias: CutSpillDetail

> **CutSpillDetail** = `object`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:229](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-planner.ts#L229)

One relocated slot, described in terms a user can read: which event moved,
from which date to which. A slot the balancer bounced twice (off ראשון, then
off שני) collapses into a single detail spanning its first and last day.

## Properties

### durationMinutes

> **durationMinutes**: `number`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:240](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-planner.ts#L240)

***

### eventId

> **eventId**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:231](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-planner.ts#L231)

***

### fromDate

> **fromDate**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:237](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-planner.ts#L237)

ISO date (yyyy-MM-dd) the slot was originally mapped to.

***

### fromDayId

> **fromDayId**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:234](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-planner.ts#L234)

***

### slotKey

> **slotKey**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:230](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-planner.ts#L230)

***

### title

> **title**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:233](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-planner.ts#L233)

Event title at plan time; falls back to the id for generated slots.

***

### toDate

> **toDate**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:239](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-planner.ts#L239)

ISO date (yyyy-MM-dd) it ended up on.

***

### toDayId

> **toDayId**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:235](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/gantt/cut-planner.ts#L235)
