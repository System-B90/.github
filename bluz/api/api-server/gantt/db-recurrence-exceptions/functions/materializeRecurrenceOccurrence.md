[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/db-recurrence-exceptions](../index.md) / materializeRecurrenceOccurrence

# Function: materializeRecurrenceOccurrence()

> **materializeRecurrenceOccurrence**(`data`): `Promise`\<\{ `event`: [`GanttEvent`](../../../../api-shared/types/gantt/models/event/type-aliases/GanttEvent.md) \| [`ApiModuleEvent`](../../../../api-shared/types/gantt/api-layer/type-aliases/ApiModuleEvent.md); `mapping`: \{ `allottedMinutes`: `number`; `createdAt`: `Date`; `curriculumId`: `string`; `dayId`: `string`; `eventId`: `string` \| `null`; `id`: `string`; `moduleId`: `string`; `sortOrder`: `number`; `updatedAt`: `Date`; \}; \}\>

Defined in: [ui/src/api-server/gantt/db-recurrence-exceptions.ts:57](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/gantt/db-recurrence-exceptions.ts#L57)

Materializes a recurring occurrence into its own standalone event: copies
the source event's fields (recurrence reset to "none"), links the copy to
the same module, maps it onto the occurrence day, and excepts the source
event from echoing onto that day going forward.

## Parameters

### data

#### curriculumId

`string`

#### dayId

`string`

#### eventId

`string`

#### moduleId

`string`

## Returns

`Promise`\<\{ `event`: [`GanttEvent`](../../../../api-shared/types/gantt/models/event/type-aliases/GanttEvent.md) \| [`ApiModuleEvent`](../../../../api-shared/types/gantt/api-layer/type-aliases/ApiModuleEvent.md); `mapping`: \{ `allottedMinutes`: `number`; `createdAt`: `Date`; `curriculumId`: `string`; `dayId`: `string`; `eventId`: `string` \| `null`; `id`: `string`; `moduleId`: `string`; `sortOrder`: `number`; `updatedAt`: `Date`; \}; \}\>
