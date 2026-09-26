[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/db-module-event](../index.md) / DbModuleEvent

# Variable: DbModuleEvent

> `const` **DbModuleEvent**: `object`

Defined in: [ui/src/api-server/gantt/db-module-event.ts:375](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/gantt/db-module-event.ts#L375)

## Type Declaration

### applyShuffleGroup

> **applyShuffleGroup**: (`eventId`, `moduleId`, `shuffles`) => `Promise`\<\{ `members`: [`GanttEvent`](../../../../api-shared/types/gantt/models/event/type-aliases/GanttEvent.md)[]; `removedIds`: `string`[]; \}\>

Makes `eventId` cover exactly `shuffles`, one event per shuffle.

The group is stored as separate rows rather than one event with many times:
each shuffle's copy has to be placed, cut and Hive-linked on its own. This
reconciles the group against the requested names in one transaction - the
origin keeps the first uncovered name, missing names get a fresh copy, and
members whose name is gone are deleted - so a repeated call is idempotent.

Returns every surviving member plus the ids that were removed, letting the
client patch its store instead of refetching the curriculum.

#### Parameters

##### eventId

`string`

##### moduleId

`string`

##### shuffles

`string`[]

#### Returns

`Promise`\<\{ `members`: [`GanttEvent`](../../../../api-shared/types/gantt/models/event/type-aliases/GanttEvent.md)[]; `removedIds`: `string`[]; \}\>

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

> `readonly` **createNewItem**: (`payload`, `executor?`) => `Promise`\<[`GanttEvent`](../../../../api-shared/types/gantt/models/event/type-aliases/GanttEvent.md) \| [`ApiModuleEvent`](../../../../api-shared/types/gantt/api-layer/type-aliases/ApiModuleEvent.md)\>

Server-side widening of the shared `createNewItem` contract: the second
parameter enlists the create in a caller's transaction (#518). It stays
out of `BasicGantOperations` because that type is shared with the client
layer, which has no database handle to pass.

#### Parameters

##### payload

[`CreateGanttEventPayload`](../../../../api-shared/types/gantt/create-payloads/type-aliases/CreateGanttEventPayload.md)

##### executor?

[`GanttDbExecutor`](../../type-aliases/GanttDbExecutor.md)

#### Returns

`Promise`\<[`GanttEvent`](../../../../api-shared/types/gantt/models/event/type-aliases/GanttEvent.md) \| [`ApiModuleEvent`](../../../../api-shared/types/gantt/api-layer/type-aliases/ApiModuleEvent.md)\>

### deleteItem

> `readonly` **deleteItem**: (`id`) => `Promise`\<`void`\>

#### Parameters

##### id

`string`

#### Returns

`Promise`\<`void`\>

### findGroupMembers

> **findGroupMembers**: (`groupId`, `executor`) => `Promise`\<[`GanttEvent`](../../../../api-shared/types/gantt/models/event/type-aliases/GanttEvent.md)[]\>

Every event sharing `groupId`, oldest first.

#### Parameters

##### groupId

`string`

##### executor?

[`GanttDbExecutor`](../../type-aliases/GanttDbExecutor.md) = `postgresDb`

#### Returns

`Promise`\<[`GanttEvent`](../../../../api-shared/types/gantt/models/event/type-aliases/GanttEvent.md)[]\>

### getAllocatedTime

> **getAllocatedTime**: (`eventId`, `curriculumId`) => `Promise`\<`number`\>

Retrieves the specific allocated duration for an event within a curriculum context.

#### Parameters

##### eventId

`string`

##### curriculumId

`string`

#### Returns

`Promise`\<`number`\>

### getItem

> `readonly` **getItem**: (`id`) => `Promise`\<[`ApiModuleEvent`](../../../../api-shared/types/gantt/api-layer/type-aliases/ApiModuleEvent.md)\> = `getFullModuleEvent`

#### Parameters

##### id

`string`

#### Returns

`Promise`\<[`ApiModuleEvent`](../../../../api-shared/types/gantt/api-layer/type-aliases/ApiModuleEvent.md)\>

### getMultipleItems

> `readonly` **getMultipleItems**: (`ids`) => `Promise`\<[`GanttEvent`](../../../../api-shared/types/gantt/models/event/type-aliases/GanttEvent.md)[]\>

#### Parameters

##### ids

`string`[]

#### Returns

`Promise`\<[`GanttEvent`](../../../../api-shared/types/gantt/models/event/type-aliases/GanttEvent.md)[]\>

### linkItem

> `readonly` **linkItem**: (`moduleId`, `eventId`) => `Promise`\<[`ApiModuleEvent`](../../../../api-shared/types/gantt/api-layer/type-aliases/ApiModuleEvent.md)\> = `addEventToModule`

Associates a specific event with a module in the junction table.

#### Parameters

##### moduleId

`string`

##### eventId

`string`

#### Returns

`Promise`\<[`ApiModuleEvent`](../../../../api-shared/types/gantt/api-layer/type-aliases/ApiModuleEvent.md)\>

### listItems

> `readonly` **listItems**: (`withParents?`) => `Promise`\<`Record`\<`string`, `string`\> \| `Record`\<`string`, \{ `title`: `string`; \}\>\>

#### Parameters

##### withParents?

`boolean`

#### Returns

`Promise`\<`Record`\<`string`, `string`\> \| `Record`\<`string`, \{ `title`: `string`; \}\>\>

### setAllocatedTime

> **setAllocatedTime**: (`eventId`, `curriculumId`, `duration`) => `Promise`\<`void`\>

Sets or updates the allocated duration for a specific event in a curriculum.
Uses an upsert strategy to maintain data integrity.

#### Parameters

##### eventId

`string`

##### curriculumId

`string`

##### duration

`number`

#### Returns

`Promise`\<`void`\>

### unlinkItem

> `readonly` **unlinkItem**: (`moduleId`, `eventId`) => `Promise`\<`void`\> = `removeEventFromModule`

Removes the association between a module and an event.

#### Parameters

##### moduleId

`string`

##### eventId

`string`

#### Returns

`Promise`\<`void`\>

### updateItem

> `readonly` **updateItem**: (`id`, `updates`, `executor?`) => `Promise`\<[`GanttEvent`](../../../../api-shared/types/gantt/models/event/type-aliases/GanttEvent.md)\>

#### Parameters

##### id

`string`

##### updates

`Partial`\<`T`\>

##### executor?

[`GanttDbExecutor`](../../type-aliases/GanttDbExecutor.md)

#### Returns

`Promise`\<[`GanttEvent`](../../../../api-shared/types/gantt/models/event/type-aliases/GanttEvent.md)\>
