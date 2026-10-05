[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/state/recurrence-exceptions/context](../index.md) / MaterializeOccurrence

# Type Alias: MaterializeOccurrence

> **MaterializeOccurrence** = (`{
    moduleId,
    eventId,
    dayId,
}`) => `Promise`\<\{ `event`: [`GanttEvent`](../../../../../../api-shared/types/gantt/models/event/type-aliases/GanttEvent.md) & `object`; \} \| `undefined`\>

Defined in: [ui/src/components/gantt/state/recurrence-exceptions/context.ts:22](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/state/recurrence-exceptions/context.ts#L22)

## Parameters

### \{
    moduleId,
    eventId,
    dayId,
\}

#### dayId

[`GanttDayId`](../../../../../../api-shared/types/gantt/models/day/type-aliases/GanttDayId.md)

#### eventId

[`GanttEventId`](../../../../../../api-shared/types/gantt/models/shared/type-aliases/GanttEventId.md)

#### moduleId

[`GanttModuleId`](../../../../../../api-shared/types/gantt/models/shared/type-aliases/GanttModuleId.md)

## Returns

`Promise`\<\{ `event`: [`GanttEvent`](../../../../../../api-shared/types/gantt/models/event/type-aliases/GanttEvent.md) & `object`; \} \| `undefined`\>
