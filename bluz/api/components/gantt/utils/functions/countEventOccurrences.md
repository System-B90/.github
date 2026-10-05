[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/gantt/utils](../index.md) / countEventOccurrences

# Function: countEventOccurrences()

> **countEventOccurrences**(`event`, `eventId`, `state`, `ctx?`): `number`

Defined in: [ui/src/components/gantt/utils.tsx:55](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/utils.tsx#L55)

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
