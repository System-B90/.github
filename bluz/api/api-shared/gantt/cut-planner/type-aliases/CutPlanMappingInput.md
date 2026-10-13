[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/cut-planner](../index.md) / CutPlanMappingInput

# Type Alias: CutPlanMappingInput

> **CutPlanMappingInput** = `object`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:104](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/gantt/cut-planner.ts#L104)

## Properties

### allottedMinutes

> **allottedMinutes**: `number`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:109](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/gantt/cut-planner.ts#L109)

Minutes the event takes on this day; 0 leaves it out of the cut.

***

### dayId

> **dayId**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:106](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/gantt/cut-planner.ts#L106)

***

### eventId

> **eventId**: `string`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:105](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/gantt/cut-planner.ts#L105)

***

### sortOrder

> **sortOrder**: `number`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:107](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/gantt/cut-planner.ts#L107)

***

### weekOnly?

> `optional` **weekOnly?**: `boolean`

Defined in: [ui/src/api-shared/gantt/cut-planner.ts:114](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/gantt/cut-planner.ts#L114)

Placed for the week, not this exact day (#964). A week whose mappings are
all week-only is cut onto the weekend window instead of its weekdays.
