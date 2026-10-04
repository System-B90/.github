[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/db-recurrence-exceptions](../index.md) / deleteRecurrenceException

# Function: deleteRecurrenceException()

> **deleteRecurrenceException**(`data`): `Promise`\<`boolean`\>

Defined in: [ui/src/api-server/gantt/db-recurrence-exceptions.ts:123](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/api-server/gantt/db-recurrence-exceptions.ts#L123)

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
