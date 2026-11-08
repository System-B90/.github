[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/recurrence](../index.md) / getRecurrenceOccurrenceDayIds

# Function: getRecurrenceOccurrenceDayIds()

> **getRecurrenceOccurrenceDayIds**(`__namedParameters`): `Set`\<`string`\>

Defined in: [ui/src/api-shared/gantt/recurrence.ts:71](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-shared/gantt/recurrence.ts#L71)

The day ids a recurring event echoes onto, excluding its start day and any
excepted days (deleted occurrences or occurrences materialized into their
own standalone event).
Returns an empty set for non-recurring or unmapped events.

## Parameters

### \_\_namedParameters

[`GetRecurrenceOccurrenceDayIdsParams`](../type-aliases/GetRecurrenceOccurrenceDayIdsParams.md)

## Returns

`Set`\<`string`\>
