[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/gantt/utils](../index.md) / countRequiredOccurrences

# Function: countRequiredOccurrences()

> **countRequiredOccurrences**(`event`, `eventId`, `state`, `__namedParameters`): `number`

Defined in: [ui/src/components/gantt/utils.tsx:131](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/components/gantt/utils.tsx#L131)

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
