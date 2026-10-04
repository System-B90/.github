[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/db-recurrence-exceptions](../index.md) / createRecurrenceException

# Function: createRecurrenceException()

> **createRecurrenceException**(`data`, `executor?`): `Promise`\<\{ `createdAt`: `Date`; `curriculumId`: `string`; `dayId`: `string`; `eventId`: `string`; `id`: `string`; `materializedEventId`: `string` \| `null`; \}\>

Defined in: [ui/src/api-server/gantt/db-recurrence-exceptions.ts:36](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/api-server/gantt/db-recurrence-exceptions.ts#L36)

Removes a single recurring occurrence: marks the day as excepted so the
event no longer echoes onto it, without touching the source event.

## Parameters

### data

#### curriculumId

`string`

#### dayId

`string`

#### eventId

`string`

#### materializedEventId?

`string` \| `null`

### executor?

[`GanttDbExecutor`](../../type-aliases/GanttDbExecutor.md) = `postgresDb`

## Returns

`Promise`\<\{ `createdAt`: `Date`; `curriculumId`: `string`; `dayId`: `string`; `eventId`: `string`; `id`: `string`; `materializedEventId`: `string` \| `null`; \}\>
