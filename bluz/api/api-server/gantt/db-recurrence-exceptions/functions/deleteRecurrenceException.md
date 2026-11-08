[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/db-recurrence-exceptions](../index.md) / deleteRecurrenceException

# Function: deleteRecurrenceException()

> **deleteRecurrenceException**(`data`): `Promise`\<`boolean`\>

Defined in: [ui/src/api-server/gantt/db-recurrence-exceptions.ts:135](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-server/gantt/db-recurrence-exceptions.ts#L135)

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
