[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/cut-planner](../index.md) / CutPlanMappingInput

# Type Alias: CutPlanMappingInput

> **CutPlanMappingInput** = `object`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:105](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/gantt/cut-planner.ts#L105)

## Properties

### allottedMinutes

> **allottedMinutes**: `number`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:110](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/gantt/cut-planner.ts#L110)

Minutes the event takes on this day; 0 leaves it out of the cut.

***

### dayId

> **dayId**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:107](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/gantt/cut-planner.ts#L107)

***

### eventId

> **eventId**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:106](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/gantt/cut-planner.ts#L106)

***

### sortOrder

> **sortOrder**: `number`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:108](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/gantt/cut-planner.ts#L108)

***

### weekOnly?

> `optional` **weekOnly?**: `boolean`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:115](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/api-shared/gantt/cut-planner.ts#L115)

Placed for the week, not this exact day (#964). A week whose mappings are
all week-only is cut onto the weekend window instead of its weekdays.
