[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/tools/gantt-allotment](../index.md) / SetAllottedTimeArgs

# Type Alias: SetAllottedTimeArgs

> **SetAllottedTimeArgs** = `object`

Defined in: [ui/src/api-server/ai/tools/gantt-allotment.ts:25](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/ai/tools/gantt-allotment.ts#L25)

AI write for an event's allotted time (#857). An event's scheduled time is
the sum of `allottedMinutes` over its (curriculum, event, day) mappings, so
the tool sets one mapping's minutes, placing the event on that day first
when it is not there yet. 0 keeps the mapping but leaves the event out of
the cut, exactly like the grid.

## Properties

### curriculumId?

> `optional` **curriculumId?**: `string`

Defined in: [ui/src/api-server/ai/tools/gantt-allotment.ts:26](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/ai/tools/gantt-allotment.ts#L26)

***

### dayId

> **dayId**: `string`

Defined in: [ui/src/api-server/ai/tools/gantt-allotment.ts:29](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/ai/tools/gantt-allotment.ts#L29)

***

### eventId

> **eventId**: `string`

Defined in: [ui/src/api-server/ai/tools/gantt-allotment.ts:28](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/ai/tools/gantt-allotment.ts#L28)

***

### minutes

> **minutes**: `number`

Defined in: [ui/src/api-server/ai/tools/gantt-allotment.ts:30](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/ai/tools/gantt-allotment.ts#L30)

***

### moduleId

> **moduleId**: `string`

Defined in: [ui/src/api-server/ai/tools/gantt-allotment.ts:27](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/ai/tools/gantt-allotment.ts#L27)
