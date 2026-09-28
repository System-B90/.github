[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/gantt/utils](../index.md) / countEventOccurrences

# Function: countEventOccurrences()

> **countEventOccurrences**(`event`, `eventId`, `state`, `ctx?`): `number`

Defined in: [ui/src/components/gantt/utils.tsx:51](https://github.com/System-B90/Bluz/blob/23625511d59d71bc9679adc341fb0bcb28897208/ui/src/components/gantt/utils.tsx#L51)

Number of times an event occurs on the timeline: 1 for a non-recurring or
unplaced event, otherwise 1 (its mapped start day) plus every surviving
echoed occurrence — skipping days recorded as recurrence exceptions (#111).

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
