[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-client/gantt/recurrence-exceptions](../index.md) / recurrenceExceptionApi

# Variable: recurrenceExceptionApi

> `const` **recurrenceExceptionApi**: `object`

Defined in: [ui/src/api-client/gantt/recurrence-exceptions.ts:89](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-client/gantt/recurrence-exceptions.ts#L89)

## Type Declaration

### apiDeleteOccurrence

> **apiDeleteOccurrence**: (`eventId`, `payload`, `options?`) => `Promise`\<[`GanttEventRecurrenceException`](../../../../api-shared/types/gantt/models/recurrence-exception/type-aliases/GanttEventRecurrenceException.md)\>

POST: Deletes a single recurring occurrence (excepts that day only).

#### Parameters

##### eventId

`string`

##### payload

###### curriculumId

`string`

###### dayId

`string`

##### options?

[`ClientApiProps`](../../../common/type-aliases/ClientApiProps.md)

#### Returns

`Promise`\<[`GanttEventRecurrenceException`](../../../../api-shared/types/gantt/models/recurrence-exception/type-aliases/GanttEventRecurrenceException.md)\>

### apiGet

> `readonly` **apiGet**: (`curriculumId`, `options?`) => `Promise`\<[`GanttEventRecurrenceException`](../../../../api-shared/types/gantt/models/recurrence-exception/type-aliases/GanttEventRecurrenceException.md)[]\> = `apiGetRecurrenceExceptions`

GET: Retrieves every recurrence exception for a curriculum.

#### Parameters

##### curriculumId

`string`

##### options?

[`ClientApiProps`](../../../common/type-aliases/ClientApiProps.md)

#### Returns

`Promise`\<[`GanttEventRecurrenceException`](../../../../api-shared/types/gantt/models/recurrence-exception/type-aliases/GanttEventRecurrenceException.md)[]\>

### apiMaterializeOccurrence

> **apiMaterializeOccurrence**: (`eventId`, `payload`, `options?`) => `Promise`\<\{ `event`: `object` & [`BaseGantItem`](../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & `object`; `mapping`: \{ `dayId`: `string`; `eventId`: `string`; `moduleId`: `string`; \}; \}\>

POST: Materializes a recurring occurrence into its own standalone event.

#### Parameters

##### eventId

`string`

##### payload

###### curriculumId

`string`

###### dayId

`string`

###### moduleId

`string`

##### options?

[`ClientApiProps`](../../../common/type-aliases/ClientApiProps.md)

#### Returns

`Promise`\<\{ `event`: `object` & [`BaseGantItem`](../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & `object`; `mapping`: \{ `dayId`: `string`; `eventId`: `string`; `moduleId`: `string`; \}; \}\>

### apiRestoreOccurrence

> **apiRestoreOccurrence**: (`eventId`, `payload`, `options?`) => `Promise`\<\{ `curriculumId`: `string`; `dayId`: `string`; `eventId`: `string`; \}\>

DELETE: Restores a previously skipped occurrence (#469).

#### Parameters

##### eventId

`string`

##### payload

###### curriculumId

`string`

###### dayId

`string`

##### options?

[`ClientApiProps`](../../../common/type-aliases/ClientApiProps.md)

#### Returns

`Promise`\<\{ `curriculumId`: `string`; `dayId`: `string`; `eventId`: `string`; \}\>
