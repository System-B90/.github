[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/db-week](../index.md) / DbWeek

# Variable: DbWeek

> `const` **DbWeek**: `object`

Defined in: [ui/src/api-server/gantt/db-week.ts:263](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/gantt/db-week.ts#L263)

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

> `readonly` **createNewItem**: (`data`) => `Promise`\<[`ApiCurriculumWeek`](../../../../api-shared/types/gantt/api-layer/type-aliases/ApiCurriculumWeek.md)\> = `createWeek`

#### Parameters

##### data

[`CreateGanttWeekPayload`](../../../../api-shared/types/gantt/create-payloads/type-aliases/CreateGanttWeekPayload.md)

#### Returns

`Promise`\<[`ApiCurriculumWeek`](../../../../api-shared/types/gantt/api-layer/type-aliases/ApiCurriculumWeek.md)\>

### deleteItem

> `readonly` **deleteItem**: (`id`) => `Promise`\<`void`\>

#### Parameters

##### id

`string`

#### Returns

`Promise`\<`void`\>

### getItem

> `readonly` **getItem**: (`id`) => `Promise`\<[`ApiCurriculumWeek`](../../../../api-shared/types/gantt/api-layer/type-aliases/ApiCurriculumWeek.md)\> = `getFullWeek`

#### Parameters

##### id

`string`

#### Returns

`Promise`\<[`ApiCurriculumWeek`](../../../../api-shared/types/gantt/api-layer/type-aliases/ApiCurriculumWeek.md)\>

### getMultipleItems

> `readonly` **getMultipleItems**: (`ids`) => `Promise`\<[`GanttWeek`](../../../../api-shared/types/gantt/models/week/type-aliases/GanttWeek.md)[]\>

#### Parameters

##### ids

`string`[]

#### Returns

`Promise`\<[`GanttWeek`](../../../../api-shared/types/gantt/models/week/type-aliases/GanttWeek.md)[]\>

### listItems

> `readonly` **listItems**: (`withParents?`) => `Promise`\<`Record`\<`string`, `string`\> \| `Record`\<`string`, \{ `title`: `string`; \}\>\>

#### Parameters

##### withParents?

`boolean`

#### Returns

`Promise`\<`Record`\<`string`, `string`\> \| `Record`\<`string`, \{ `title`: `string`; \}\>\>

### updateItem

> `readonly` **updateItem**: (`id`, `updates`, `executor?`) => `Promise`\<[`GanttWeek`](../../../../api-shared/types/gantt/models/week/type-aliases/GanttWeek.md)\>

#### Parameters

##### id

`string`

##### updates

`Partial`\<`T`\>

##### executor?

[`GanttDbExecutor`](../../type-aliases/GanttDbExecutor.md)

#### Returns

`Promise`\<[`GanttWeek`](../../../../api-shared/types/gantt/models/week/type-aliases/GanttWeek.md)\>
