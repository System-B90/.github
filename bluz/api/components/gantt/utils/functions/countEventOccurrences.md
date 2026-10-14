[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/gantt/utils](../index.md) / countEventOccurrences

# Function: countEventOccurrences()

> **countEventOccurrences**(`event`, `eventId`, `state`, `ctx?`): `number`

Defined in: [ui/src/components/gantt/utils.tsx:58](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/components/gantt/utils.tsx#L58)

Number of times an event occurs. Without `onlyDayIds` this is its required
count ([countRequiredOccurrences](countRequiredOccurrences.md)). With it, the placed occurrences on
those days: its mapped start day plus every surviving echo inside the
recurrence window, skipping recurrence exceptions (#111, #468).

## Parameters

### event

[`GanttEvent`](../../../../api-shared/types/gantt/models/event/type-aliases/GanttEvent.md)

### eventId

`string`

### state

[`NormalizedStore`](../../../../api-client/gantt/drizzle-normalize/type-aliases/NormalizedStore.md)

### ctx?

[`RecurrenceOccurrenceContext`](../type-aliases/RecurrenceOccurrenceContext.md)

## Returns

`number`
