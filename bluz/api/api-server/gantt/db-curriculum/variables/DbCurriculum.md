[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/db-curriculum](../index.md) / DbCurriculum

# Variable: DbCurriculum

> `const` **DbCurriculum**: `object`

Defined in: [ui/src/api-server/gantt/db-curriculum.ts:381](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/gantt/db-curriculum.ts#L381)

## Type Declaration

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

> `readonly` **createNewItem**: (`data`) => `Promise`\<[`GanttCurriculum`](../../../../api-shared/types/gantt/models/curriculum/type-aliases/GanttCurriculum.md) \| [`ApiCurriculum`](../../../../api-shared/types/gantt/api-layer/type-aliases/ApiCurriculum.md)\> = `createCurriculum`

#### Parameters

##### data

[`CreateGanttCurriculumPayload`](../../../../api-shared/types/gantt/create-payloads/type-aliases/CreateGanttCurriculumPayload.md)

#### Returns

`Promise`\<[`GanttCurriculum`](../../../../api-shared/types/gantt/models/curriculum/type-aliases/GanttCurriculum.md) \| [`ApiCurriculum`](../../../../api-shared/types/gantt/api-layer/type-aliases/ApiCurriculum.md)\>

### deleteItem

> `readonly` **deleteItem**: (`id`) => `Promise`\<`void`\>

#### Parameters

##### id

`string`

#### Returns

`Promise`\<`void`\>

### duplicateCurriculum

> **duplicateCurriculum**: (`sourceId`, `overrides`) => `Promise`\<[`ApiCurriculum`](../../../../api-shared/types/gantt/api-layer/type-aliases/ApiCurriculum.md)\>

Clones a curriculum into a brand-new copy (#319, #322). Syllabuses (and
their modules/events) are shared, not cloned — the copy is linked to the
same syllabus rows as the source. Weeks → days are deep-cloned with fresh
ids, and the per-curriculum event configurations (cEC) plus module/event →
day mappings (cMDA) are cloned and repointed at the copy's own curriculum
id / day ids. Constraints and recurrence exceptions are intentionally out
of scope.

#### Parameters

##### sourceId

`string`

##### overrides?

[`DuplicateCurriculumOverrides`](../type-aliases/DuplicateCurriculumOverrides.md) = `{}`

#### Returns

`Promise`\<[`ApiCurriculum`](../../../../api-shared/types/gantt/api-layer/type-aliases/ApiCurriculum.md)\>

### getItem

> `readonly` **getItem**: (`id`) => `Promise`\<[`ApiCurriculum`](../../../../api-shared/types/gantt/api-layer/type-aliases/ApiCurriculum.md)\> = `getFullCurriculum`

#### Parameters

##### id

`string`

#### Returns

`Promise`\<[`ApiCurriculum`](../../../../api-shared/types/gantt/api-layer/type-aliases/ApiCurriculum.md)\>

### getMultipleItems

> `readonly` **getMultipleItems**: (`ids`) => `Promise`\<[`GanttCurriculum`](../../../../api-shared/types/gantt/models/curriculum/type-aliases/GanttCurriculum.md)[]\>

#### Parameters

##### ids

`string`[]

#### Returns

`Promise`\<[`GanttCurriculum`](../../../../api-shared/types/gantt/models/curriculum/type-aliases/GanttCurriculum.md)[]\>

### listItems

> `readonly` **listItems**: (`withParents?`) => `Promise`\<`Record`\<`string`, `string`\> \| `Record`\<`string`, \{ `title`: `string`; \}\>\>

#### Parameters

##### withParents?

`boolean`

#### Returns

`Promise`\<`Record`\<`string`, `string`\> \| `Record`\<`string`, \{ `title`: `string`; \}\>\>

### seedMealBreaksSyllabus

> **seedMealBreaksSyllabus**: (`curriculumId`) => `Promise`\<`void`\>

Seeds every new curriculum with a "הפסקות" syllabus/module holding 3 daily
meal events (breakfast/lunch/dinner). The cut planner (`cut-planner.ts`)
recognizes these by title and pins them to the exact clock time configured
in the global meal-time settings instead of stacking them.

#### Parameters

##### curriculumId

`string`

#### Returns

`Promise`\<`void`\>

### updateItem

> `readonly` **updateItem**: (`id`, `updates`, `executor?`) => `Promise`\<[`GanttCurriculum`](../../../../api-shared/types/gantt/models/curriculum/type-aliases/GanttCurriculum.md)\>

#### Parameters

##### id

`string`

##### updates

`Partial`\<`T`\>

##### executor?

[`GanttDbExecutor`](../../type-aliases/GanttDbExecutor.md)

#### Returns

`Promise`\<[`GanttCurriculum`](../../../../api-shared/types/gantt/models/curriculum/type-aliases/GanttCurriculum.md)\>
