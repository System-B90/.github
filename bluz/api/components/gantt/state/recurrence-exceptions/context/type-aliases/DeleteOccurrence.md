[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/state/recurrence-exceptions/context](../index.md) / DeleteOccurrence

# Type Alias: DeleteOccurrence

> **DeleteOccurrence** = (`{
    eventId,
    dayId,
}`) => `Promise`\<[`GanttEventRecurrenceException`](../../../../../../api-shared/types/gantt/models/recurrence-exception/type-aliases/GanttEventRecurrenceException.md) \| `undefined`\>

Defined in: [ui/src/components/gantt/state/recurrence-exceptions/context.ts:14](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/state/recurrence-exceptions/context.ts#L14)

## Parameters

### \{
    eventId,
    dayId,
\}

#### dayId

[`GanttDayId`](../../../../../../api-shared/types/gantt/models/day/type-aliases/GanttDayId.md)

#### eventId

[`GanttEventId`](../../../../../../api-shared/types/gantt/models/shared/type-aliases/GanttEventId.md)

## Returns

`Promise`\<[`GanttEventRecurrenceException`](../../../../../../api-shared/types/gantt/models/recurrence-exception/type-aliases/GanttEventRecurrenceException.md) \| `undefined`\>
