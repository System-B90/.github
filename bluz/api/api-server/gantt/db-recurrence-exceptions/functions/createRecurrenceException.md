[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/db-recurrence-exceptions](../index.md) / createRecurrenceException

# Function: createRecurrenceException()

> **createRecurrenceException**(`data`, `executor?`): `Promise`\<\{ `createdAt`: `Date`; `curriculumId`: `string`; `dayId`: `string`; `eventId`: `string`; `id`: `string`; `materializedEventId`: `string` \| `null`; \}\>

Defined in: [ui/src/api-server/gantt/db-recurrence-exceptions.ts:38](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-server/gantt/db-recurrence-exceptions.ts#L38)

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
