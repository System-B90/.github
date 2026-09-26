[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-client/gantt/mappings](../index.md) / curriculumModuleDayMappingApi

# Variable: curriculumModuleDayMappingApi

> `const` **curriculumModuleDayMappingApi**: `object`

Defined in: [ui/src/api-client/gantt/mappings.ts:112](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-client/gantt/mappings.ts#L112)

Client-side API client wrapper for managing curriculum module and event day mappings.
Provides endpoints for retrieving, creating, updating, and deleting mappings.

## Type Declaration

### apiCreate

> `readonly` **apiCreate**: (`curriculumId`, `payload`, `options?`) => `Promise`\<[`GanttCurriculumEventDayMapping`](../../../../api-shared/types/gantt/models/curriculum-day-module-mapping/type-aliases/GanttCurriculumEventDayMapping.md)\> = `apiCreateModuleDayMapping`

POST: Creates a new module-to-day mapping.

#### Parameters

##### curriculumId

`string`

##### payload

[`CreateGanttCurriculumEventDayMapping`](../../../../api-shared/types/gantt/create-payloads/type-aliases/CreateGanttCurriculumEventDayMapping.md)

##### options?

[`ClientApiProps`](../../../common/type-aliases/ClientApiProps.md)

#### Returns

`Promise`\<[`GanttCurriculumEventDayMapping`](../../../../api-shared/types/gantt/models/curriculum-day-module-mapping/type-aliases/GanttCurriculumEventDayMapping.md)\>

### apiDelete

> `readonly` **apiDelete**: (`curriculumId`, `moduleId`, `eventId`, `dayId`, `options?`) => `Promise`\<`void`\> = `apiDeleteModuleDayMapping`

DELETE: Removes a module-to-day mapping.

#### Parameters

##### curriculumId

`string`

##### moduleId

`string`

##### eventId

`string` \| `null`

##### dayId

`string`

##### options?

[`ClientApiProps`](../../../common/type-aliases/ClientApiProps.md)

#### Returns

`Promise`\<`void`\>

### apiGet

> `readonly` **apiGet**: (`curriculumId`, `dayId?`, `options?`) => `Promise`\<[`GanttCurriculumEventDayMapping`](../../../../api-shared/types/gantt/models/curriculum-day-module-mapping/type-aliases/GanttCurriculumEventDayMapping.md)[]\> = `apiGetModuleDayMapping`

GET: Retrieves all module mappings for a curriculum.

#### Parameters

##### curriculumId

`string`

##### dayId?

`string` \| `string`[]

##### options?

[`ClientApiProps`](../../../common/type-aliases/ClientApiProps.md)

#### Returns

`Promise`\<[`GanttCurriculumEventDayMapping`](../../../../api-shared/types/gantt/models/curriculum-day-module-mapping/type-aliases/GanttCurriculumEventDayMapping.md)[]\>

### apiUpdate

> `readonly` **apiUpdate**: (`curriculumId`, `moduleId`, `eventId`, `oldMapping`, `newValues`, `options?`) => `Promise`\<[`GanttCurriculumEventDayMapping`](../../../../api-shared/types/gantt/models/curriculum-day-module-mapping/type-aliases/GanttCurriculumEventDayMapping.md)\> = `apiUpdateModuleDayMapping`

PATCH: Updates an existing mapping or reorders it.

#### Parameters

##### curriculumId

`string`

##### moduleId

`string`

##### eventId

`string` \| `null`

##### oldMapping

###### dayId

`string`

##### newValues

###### dayId?

`string`

###### sortOrder?

`number`

##### options?

[`ClientApiProps`](../../../common/type-aliases/ClientApiProps.md)

#### Returns

`Promise`\<[`GanttCurriculumEventDayMapping`](../../../../api-shared/types/gantt/models/curriculum-day-module-mapping/type-aliases/GanttCurriculumEventDayMapping.md)\>
