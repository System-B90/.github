[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/db-syllabus](../index.md) / DbSyllabus

# Variable: DbSyllabus

> `const` **DbSyllabus**: `object`

Defined in: [ui/src/api-server/gantt/db-syllabus.ts:336](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/gantt/db-syllabus.ts#L336)

## Type Declaration

### applyShuffles

> **applyShuffles**: (`id`, `shuffles`) => `Promise`\<[`ShuffleUsages`](../../../../api-shared/types/gantt/shuffles/type-aliases/ShuffleUsages.md)\>

Replaces the syllabus' shuffle list, cascading every removed name off the
modules and events that carry it (#485).

Without the cascade the child keeps a dangling name and the UI only offers
to clear it once the user retypes the deleted shuffle on the syllabus — so
the caller confirms first (see `SyllabusShuffles`) and this applies both
sides in one transaction.

#### Parameters

##### id

`string`

##### shuffles

`string`[]

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

> `readonly` **linkItem**: (`curriculumId`, `syllabusId`) => `Promise`\<[`ApiSyllabus`](../../../../api-shared/types/gantt/api-layer/type-aliases/ApiSyllabus.md)\> = `addSyllabusToCurriculum`

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

> `readonly` **updateItem**: (`id`, `updateData`) => `Promise`\<[`GanttSyllabus`](../../../../api-shared/types/gantt/models/syllabus/type-aliases/GanttSyllabus.md)\> = `updateSyllabus`

Blocks a plain PATCH that drops a shuffle still in use (#485). Callers that
mean to cascade go through `applyShuffles` after confirming with the user.

#### Parameters

##### id

`string`

##### updateData

`Partial`\<[`GanttSyllabus`](../../../../api-shared/types/gantt/models/syllabus/type-aliases/GanttSyllabus.md)\>

#### Returns

`Promise`\<[`GanttSyllabus`](../../../../api-shared/types/gantt/models/syllabus/type-aliases/GanttSyllabus.md)\>
