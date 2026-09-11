[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-client/gantt/module-event](../index.md) / moduleEventApi

# Variable: moduleEventApi

> `const` **moduleEventApi**: `object`

Defined in: [ui/src/api-client/gantt/module-event.ts:35](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-client/gantt/module-event.ts#L35)

## Type Declaration

### apiCreate

> `readonly` **apiCreate**: (`payload`, `options?`) => `Promise`\<`object` & [`BaseGantItem`](../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`BaseDocument`](../../base/type-aliases/BaseDocument.md)\>

#### Parameters

##### payload

[`CreateGanttEventPayload`](../../../../api-shared/types/gantt/create-payloads/type-aliases/CreateGanttEventPayload.md)

##### options?

[`ClientApiProps`](../../../common/type-aliases/ClientApiProps.md)

#### Returns

`Promise`\<`object` & [`BaseGantItem`](../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`BaseDocument`](../../base/type-aliases/BaseDocument.md)\>

### apiDelete

> `readonly` **apiDelete**: (`id`, `options?`) => `Promise`\<`void`\>

#### Parameters

##### id

`string`

##### options?

[`ClientApiProps`](../../../common/type-aliases/ClientApiProps.md)

#### Returns

`Promise`\<`void`\>

### apiDuplicate

> **apiDuplicate**: (`eventId`, `moduleId`) => `Promise`\<[`ModuleEventDocument`](../type-aliases/ModuleEventDocument.md)\>

#### Parameters

##### eventId

`string`

##### moduleId

`string`

#### Returns

`Promise`\<[`ModuleEventDocument`](../type-aliases/ModuleEventDocument.md)\>

### apiGet

> `readonly` **apiGet**: (`id`, `options?`) => `Promise`\<[`ApiModuleEvent`](../../../../api-shared/types/gantt/api-layer/type-aliases/ApiModuleEvent.md)\>

#### Parameters

##### id

`string`

##### options?

[`ClientApiProps`](../../../common/type-aliases/ClientApiProps.md)

#### Returns

`Promise`\<[`ApiModuleEvent`](../../../../api-shared/types/gantt/api-layer/type-aliases/ApiModuleEvent.md)\>

### apiGetAllocatedTime

> `readonly` **apiGetAllocatedTime**: (`itemId`, `containerId`, `options?`) => `Promise`\<`number`\>

#### Parameters

##### itemId

`string`

##### containerId

`string`

##### options?

[`ClientApiProps`](../../../common/type-aliases/ClientApiProps.md)

#### Returns

`Promise`\<`number`\>

### apiGetMany

> `readonly` **apiGetMany**: (`ids`, `options?`) => `Promise`\<`Record`\<`string`, `object` & [`BaseGantItem`](../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`BaseDocument`](../../base/type-aliases/BaseDocument.md)\>\>

#### Parameters

##### ids

`string`[]

##### options?

[`ClientApiProps`](../../../common/type-aliases/ClientApiProps.md)

#### Returns

`Promise`\<`Record`\<`string`, `object` & [`BaseGantItem`](../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`BaseDocument`](../../base/type-aliases/BaseDocument.md)\>\>

### apiLink

> `readonly` **apiLink**: (`itemId`, `newParentId`, `options?`) => `Promise`\<`object` & [`BaseGantItem`](../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`BaseDocument`](../../base/type-aliases/BaseDocument.md)\>

#### Parameters

##### itemId

`string`

##### newParentId

`string`

##### options?

[`ClientApiProps`](../../../common/type-aliases/ClientApiProps.md)

#### Returns

`Promise`\<`object` & [`BaseGantItem`](../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`BaseDocument`](../../base/type-aliases/BaseDocument.md)\>

### apiList

> `readonly` **apiList**: (`options?`) => `Promise`\<`Record`\<`string`, `string`\>\>

#### Parameters

##### options?

[`ClientApiProps`](../../../common/type-aliases/ClientApiProps.md)

#### Returns

`Promise`\<`Record`\<`string`, `string`\>\>

### apiListWithParents

> `readonly` **apiListWithParents**: (`options?`) => `Promise`\<`Record`\<`string`, [`ListEntryWithParent`](../../base/type-aliases/ListEntryWithParent.md)\<[`GanttEvent`](../../../../api-shared/types/gantt/models/event/type-aliases/GanttEvent.md)\>\>\>

Same listing as `apiList`, but each value carries the parent id. Use
when you need child → parent without fetching each item. See #310.

#### Parameters

##### options?

[`ClientApiProps`](../../../common/type-aliases/ClientApiProps.md)

#### Returns

`Promise`\<`Record`\<`string`, [`ListEntryWithParent`](../../base/type-aliases/ListEntryWithParent.md)\<[`GanttEvent`](../../../../api-shared/types/gantt/models/event/type-aliases/GanttEvent.md)\>\>\>

### apiSetAllocatedTime

> `readonly` **apiSetAllocatedTime**: (`itemId`, `containerId`, `allocatedTime`, `options?`) => `Promise`\<`void`\>

#### Parameters

##### itemId

`string`

##### containerId

`string`

##### allocatedTime

`number`

##### options?

[`ClientApiProps`](../../../common/type-aliases/ClientApiProps.md)

#### Returns

`Promise`\<`void`\>

### apiUnlink

> `readonly` **apiUnlink**: (`itemId`, `oldParentId`, `options?`) => `Promise`\<`void`\>

#### Parameters

##### itemId

`string`

##### oldParentId

`string`

##### options?

[`ClientApiProps`](../../../common/type-aliases/ClientApiProps.md)

#### Returns

`Promise`\<`void`\>

### apiUpdate

> `readonly` **apiUpdate**: (`updates`, `options?`) => `Promise`\<`object` & [`BaseGantItem`](../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`BaseDocument`](../../base/type-aliases/BaseDocument.md)\>

#### Parameters

##### updates

`Partial`\<[`GanttEvent`](../../../../api-shared/types/gantt/models/event/type-aliases/GanttEvent.md)\> & `object`

##### options?

[`ClientApiProps`](../../../common/type-aliases/ClientApiProps.md)

#### Returns

`Promise`\<`object` & [`BaseGantItem`](../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`BaseDocument`](../../base/type-aliases/BaseDocument.md)\>
