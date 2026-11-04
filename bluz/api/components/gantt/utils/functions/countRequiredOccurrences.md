[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/gantt/utils](../index.md) / countRequiredOccurrences

# Function: countRequiredOccurrences()

> **countRequiredOccurrences**(`event`, `eventId`, `state`, `__namedParameters`): `number`

Defined in: [ui/src/components/gantt/utils.tsx:131](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/components/gantt/utils.tsx#L131)

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
