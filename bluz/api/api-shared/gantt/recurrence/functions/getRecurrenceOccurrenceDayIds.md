[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/recurrence](../index.md) / getRecurrenceOccurrenceDayIds

# Function: getRecurrenceOccurrenceDayIds()

> **getRecurrenceOccurrenceDayIds**(`__namedParameters`): `Set`\<`string`\>

Defined in: [ui/src/api-shared/gantt/recurrence.ts:71](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-shared/gantt/recurrence.ts#L71)

The day ids a recurring event echoes onto, excluding its start day and any
excepted days (deleted occurrences or occurrences materialized into their
own standalone event).
Returns an empty set for non-recurring or unmapped events.

## Parameters

### \_\_namedParameters

[`GetRecurrenceOccurrenceDayIdsParams`](../type-aliases/GetRecurrenceOccurrenceDayIdsParams.md)

## Returns

`Set`\<`string`\>
