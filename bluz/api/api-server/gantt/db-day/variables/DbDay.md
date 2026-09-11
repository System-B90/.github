[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/db-day](../index.md) / DbDay

# Variable: DbDay

> `const` **DbDay**: `object`

Defined in: [ui/src/api-server/gantt/db-day.ts:43](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/gantt/db-day.ts#L43)

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

> `readonly` **createNewItem**: (`payload`, `executor?`) => `Promise`\<[`GanttDay`](../../../../api-shared/types/gantt/models/day/type-aliases/GanttDay.md) \| `Omit`\<`object` & [`BaseGantItem`](../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`RawBaseDocument`](../../../../api-shared/types/gantt/api-layer/type-aliases/RawBaseDocument.md), `"title"`\>\>

Server-side widening of the shared `createNewItem` contract: the second
parameter enlists the create in a caller's transaction (#518). It stays
out of `BasicGantOperations` because that type is shared with the client
layer, which has no database handle to pass.

#### Parameters

##### payload

[`CreateGanttDayPayload`](../../../../api-shared/types/gantt/create-payloads/type-aliases/CreateGanttDayPayload.md)

##### executor?

[`GanttDbExecutor`](../../type-aliases/GanttDbExecutor.md)

#### Returns

`Promise`\<[`GanttDay`](../../../../api-shared/types/gantt/models/day/type-aliases/GanttDay.md) \| `Omit`\<`object` & [`BaseGantItem`](../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`RawBaseDocument`](../../../../api-shared/types/gantt/api-layer/type-aliases/RawBaseDocument.md), `"title"`\>\>

### deleteItem

> `readonly` **deleteItem**: (`id`) => `Promise`\<`void`\>

#### Parameters

##### id

`string`

#### Returns

`Promise`\<`void`\>

### getItem

> `readonly` **getItem**: (`id`) => `Promise`\<`Omit`\<`object` & [`BaseGantItem`](../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`RawBaseDocument`](../../../../api-shared/types/gantt/api-layer/type-aliases/RawBaseDocument.md), `"title"`\>\> = `getFullDay`

#### Parameters

##### id

`string`

#### Returns

`Promise`\<`Omit`\<`object` & [`BaseGantItem`](../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`RawBaseDocument`](../../../../api-shared/types/gantt/api-layer/type-aliases/RawBaseDocument.md), `"title"`\>\>

### getMultipleItems

> `readonly` **getMultipleItems**: (`ids`) => `Promise`\<[`GanttDay`](../../../../api-shared/types/gantt/models/day/type-aliases/GanttDay.md)[]\>

#### Parameters

##### ids

`string`[]

#### Returns

`Promise`\<[`GanttDay`](../../../../api-shared/types/gantt/models/day/type-aliases/GanttDay.md)[]\>

### listItems

> `readonly` **listItems**: (`withParents?`) => `Promise`\<`Record`\<`string`, `string`\> \| `Record`\<`string`, \{ `title`: `string`; \}\>\>

#### Parameters

##### withParents?

`boolean`

#### Returns

`Promise`\<`Record`\<`string`, `string`\> \| `Record`\<`string`, \{ `title`: `string`; \}\>\>

### updateItem

> `readonly` **updateItem**: (`id`, `updates`, `executor?`) => `Promise`\<[`GanttDay`](../../../../api-shared/types/gantt/models/day/type-aliases/GanttDay.md)\>

#### Parameters

##### id

`string`

##### updates

`Partial`\<`T`\>

##### executor?

[`GanttDbExecutor`](../../type-aliases/GanttDbExecutor.md)

#### Returns

`Promise`\<[`GanttDay`](../../../../api-shared/types/gantt/models/day/type-aliases/GanttDay.md)\>
