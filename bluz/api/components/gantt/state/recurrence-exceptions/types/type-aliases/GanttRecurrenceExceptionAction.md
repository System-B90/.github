[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/state/recurrence-exceptions/types](../index.md) / GanttRecurrenceExceptionAction

# Type Alias: GanttRecurrenceExceptionAction

> **GanttRecurrenceExceptionAction** = \{ `payload`: \{ `dayId`: [`GanttDayId`](../../../../../../api-shared/types/gantt/models/day/type-aliases/GanttDayId.md); `eventId`: [`GanttEventId`](../../../../../../api-shared/types/gantt/models/shared/type-aliases/GanttEventId.md); \}; `type`: `"REMOVE_EXCEPTION"`; \} \| \{ `payload`: [`GanttEventRecurrenceException`](../../../../../../api-shared/types/gantt/models/recurrence-exception/type-aliases/GanttEventRecurrenceException.md)[]; `type`: `"SET_EXCEPTIONS"`; \} \| \{ `payload`: `boolean`; `type`: `"SET_LOADING"`; \} \| \{ `payload`: [`GanttEventRecurrenceException`](../../../../../../api-shared/types/gantt/models/recurrence-exception/type-aliases/GanttEventRecurrenceException.md); `type`: `"UPSERT_EXCEPTION"`; \}

Defined in: [ui/src/components/gantt/state/recurrence-exceptions/types.ts:13](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/state/recurrence-exceptions/types.ts#L13)
