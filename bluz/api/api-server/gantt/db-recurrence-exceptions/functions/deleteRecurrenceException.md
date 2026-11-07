[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/db-recurrence-exceptions](../index.md) / deleteRecurrenceException

# Function: deleteRecurrenceException()

> **deleteRecurrenceException**(`data`): `Promise`\<`boolean`\>

Defined in: [ui/src/api-server/gantt/db-recurrence-exceptions.ts:135](https://github.com/System-B90/Bluz/blob/1b02178048002eee34d502b2e3e2a402e1b9c9c0/ui/src/api-server/gantt/db-recurrence-exceptions.ts#L135)

Restores a skipped occurrence: drops the exception so the event echoes onto
that day again (#469). Materialized occurrences are left alone — their
standalone event still holds the day, so removing the exception would
double-book it. Returns whether a row was actually removed.

## Parameters

### data

#### curriculumId

`string`

#### dayId

`string`

#### eventId

`string`

## Returns

`Promise`\<`boolean`\>
