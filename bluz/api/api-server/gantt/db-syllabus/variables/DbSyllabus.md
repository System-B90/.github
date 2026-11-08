[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/db-syllabus](../index.md) / DbSyllabus

# Variable: DbSyllabus

> `const` **DbSyllabus**: `object`

Defined in: [ui/src/api-server/gantt/db-syllabus.ts:549](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-server/gantt/db-syllabus.ts#L549)

## Type Declaration

### applyShuffles

> `readonly` **applyShuffles**: (...`args`) => `Promise`\<[`ShuffleUsages`](../../../../api-shared/types/gantt/shuffles/type-aliases/ShuffleUsages.md)\> = `applyShufflesAndCourseLinks`

#### Parameters

##### args

...\[`string`, `string`[], [`ShuffleDescriptions`](../../../../api-shared/gantt/shuffle-names/type-aliases/ShuffleDescriptions.md), [`ShuffleRenames`](../../../../api-shared/gantt/shuffle-names/type-aliases/ShuffleRenames.md)\]

#### Returns

`Promise`\<[`ShuffleUsages`](../../../../api-shared/types/gantt/shuffles/type-aliases/ShuffleUsages.md)\>

### attachParentIds

> `readonly` **attachParentIds**: \<`TItem`\>(`items`) => `Promise`\<`TItem`[]\>

#### Type Parameters

##### TItem

`TItem` *extends* `object`

#### Parameters

##### items

`TItem`[]

#### Returns

`Promise`\<`TItem`[]\>

### createNewItem

> `readonly` **createNewItem**: (`payload`, `executor?`) => `Promise`\<[`GanttSyllabus`](../../../../api-shared/types/gantt/models/syllabus/type-aliases/GanttSyllabus.md) \| [`ApiSyllabus`](../../../../api-shared/types/gantt/api-layer/type-aliases/ApiSyllabus.md)\>

Server-side widening of the shared `createNewItem` contract: the second
parameter enlists the create in a caller's transaction (#518). It stays
out of `BasicGantOperations` because that type is shared with the client
layer, which has no database handle to pass.

#### Parameters

##### payload

[`CreateGanttSyllabusPayload`](../../../../api-shared/types/gantt/create-payloads/type-aliases/CreateGanttSyllabusPayload.md)

##### executor?

[`GanttDbExecutor`](../../type-aliases/GanttDbExecutor.md)

#### Returns

`Promise`\<[`GanttSyllabus`](../../../../api-shared/types/gantt/models/syllabus/type-aliases/GanttSyllabus.md) \| [`ApiSyllabus`](../../../../api-shared/types/gantt/api-layer/type-aliases/ApiSyllabus.md)\>

### createNewItems

> `readonly` **createNewItems**: (`payloads`, `executor?`) => `Promise`\<[`GanttSyllabus`](../../../../api-shared/types/gantt/models/syllabus/type-aliases/GanttSyllabus.md)[]\>

Bulk `createNewItem`; returns the items in payload order.

#### Parameters

##### payloads

[`CreateGanttSyllabusPayload`](../../../../api-shared/types/gantt/create-payloads/type-aliases/CreateGanttSyllabusPayload.md)[]

##### executor?

[`GanttDbExecutor`](../../type-aliases/GanttDbExecutor.md)

#### Returns

`Promise`\<[`GanttSyllabus`](../../../../api-shared/types/gantt/models/syllabus/type-aliases/GanttSyllabus.md)[]\>

### deleteItem

> `readonly` **deleteItem**: (`id`) => `Promise`\<`void`\>

#### Parameters

##### id

`string`

#### Returns

`Promise`\<`void`\>

### findShuffleUsages

> **findShuffleUsages**: (`syllabusId`, `shuffleNames`, `executor`) => `Promise`\<[`ShuffleUsages`](../../../../api-shared/types/gantt/shuffles/type-aliases/ShuffleUsages.md)\>

Modules and events under `syllabusId` tagged with any of `shuffleNames`.

Walks s2m → m2e so the scan stays scoped to the syllabus that owns the
names; an event reached through another syllabus keeps its own tags.

#### Parameters

##### syllabusId

`string`

##### shuffleNames

`string`[]

##### executor?

[`GanttDbExecutor`](../../type-aliases/GanttDbExecutor.md) = `postgresDb`

#### Returns

`Promise`\<[`ShuffleUsages`](../../../../api-shared/types/gantt/shuffles/type-aliases/ShuffleUsages.md)\>

### getItem

> `readonly` **getItem**: (`id`) => `Promise`\<[`ApiSyllabus`](../../../../api-shared/types/gantt/api-layer/type-aliases/ApiSyllabus.md)\> = `getFullSyllabus`

#### Parameters

##### id

`string`

#### Returns

`Promise`\<[`ApiSyllabus`](../../../../api-shared/types/gantt/api-layer/type-aliases/ApiSyllabus.md)\>

### getMultipleItems

> `readonly` **getMultipleItems**: (`ids`) => `Promise`\<[`GanttSyllabus`](../../../../api-shared/types/gantt/models/syllabus/type-aliases/GanttSyllabus.md)[]\>

#### Parameters

##### ids

`string`[]

#### Returns

`Promise`\<[`GanttSyllabus`](../../../../api-shared/types/gantt/models/syllabus/type-aliases/GanttSyllabus.md)[]\>

### linkItem

> `readonly` **linkItem**: (`curriculumId`, `syllabusId`) => `Promise`\<[`ApiSyllabus`](../../../../api-shared/types/gantt/api-layer/type-aliases/ApiSyllabus.md)\> = `addSyllabusToCurriculumAndCourseLinks`

#### Parameters

##### curriculumId

`string`

##### syllabusId

`string`

#### Returns

`Promise`\<[`ApiSyllabus`](../../../../api-shared/types/gantt/api-layer/type-aliases/ApiSyllabus.md)\>

### listItems

> `readonly` **listItems**: (`withParents?`) => `Promise`\<`Record`\<`string`, `string`\> \| `Record`\<`string`, \{ `title`: `string`; \}\>\>

#### Parameters

##### withParents?

`boolean`

#### Returns

`Promise`\<`Record`\<`string`, `string`\> \| `Record`\<`string`, \{ `title`: `string`; \}\>\>

### reorderModules

> **reorderModules**: (`syllabusId`, `moduleIds`) => `Promise`\<`void`\>

#### Parameters

##### syllabusId

`string`

##### moduleIds

`string`[]

#### Returns

`Promise`\<`void`\>

### unlinkItem

> `readonly` **unlinkItem**: (`curriculumId`, `syllabusId`) => `Promise`\<`void`\> = `removeSyllabusFromCurriculum`

#### Parameters

##### curriculumId

`string`

##### syllabusId

`string`

#### Returns

`Promise`\<`void`\>

### updateItem

> `readonly` **updateItem**: (`id`, `updateData`) => `Promise`\<[`GanttSyllabus`](../../../../api-shared/types/gantt/models/syllabus/type-aliases/GanttSyllabus.md)\> = `updateSyllabusAndCourseLinks`

#### Parameters

##### id

`string`

##### updateData

`Partial`\<[`GanttSyllabus`](../../../../api-shared/types/gantt/models/syllabus/type-aliases/GanttSyllabus.md)\>

#### Returns

`Promise`\<[`GanttSyllabus`](../../../../api-shared/types/gantt/models/syllabus/type-aliases/GanttSyllabus.md)\>
