[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/state/recurrence-exceptions/context](../index.md) / DeleteOccurrence

# Type Alias: DeleteOccurrence

> **DeleteOccurrence** = (`{
    eventId,
    dayId,
}`) => `Promise`\<[`GanttEventRecurrenceException`](../../../../../../api-shared/types/gantt/models/recurrence-exception/type-aliases/GanttEventRecurrenceException.md) \| `undefined`\>

Defined in: [ui/src/components/gantt/state/recurrence-exceptions/context.ts:14](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/gantt/state/recurrence-exceptions/context.ts#L14)

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
