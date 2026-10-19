[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/gantt/utils](../index.md) / countRequiredOccurrences

# Function: countRequiredOccurrences()

> **countRequiredOccurrences**(`event`, `eventId`, `state`, `__namedParameters`): `number`

Defined in: [ui/src/components/gantt/utils.tsx:107](https://github.com/System-B90/Bluz/blob/9713962ebc3106e4e61b30619aa36a3bd2b7d3c7/ui/src/components/gantt/utils.tsx#L107)

How many times a recurring event is required to occur: every day (daily)
or week (weekly) its recurrence pattern hits inside its recurrence window,
minus explicitly skipped or materialized occurrences. Independent of where
the event is placed, except that a placed weekly event fixes its weekday.
A non-recurring event is required once.

## Parameters

### event

[`GanttEvent`](../../../../api-shared/types/gantt/models/event/type-aliases/GanttEvent.md)

### eventId

`string`

### state

[`NormalizedStore`](../../../../api-client/gantt/drizzle-normalize/type-aliases/NormalizedStore.md)

### \_\_namedParameters

`Pick`\<[`RecurrenceOccurrenceContext`](../type-aliases/RecurrenceOccurrenceContext.md), `"constraintsByEvent"` \| `"dateOf"` \| `"exceptions"` \| `"linearDays"` \| `"mappings"`\>

## Returns

`number`
