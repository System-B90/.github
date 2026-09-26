[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-client/gantt/curriculum](../index.md) / curriculumApi

# Variable: curriculumApi

> `const` **curriculumApi**: `object`

Defined in: [ui/src/api-client/gantt/curriculum.ts:86](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-client/gantt/curriculum.ts#L86)

## Type Declaration

### apiCreate

> `readonly` **apiCreate**: (`payload`, `options?`) => `Promise`\<`object` & [`BaseGantItem`](../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`BaseDocument`](../../base/type-aliases/BaseDocument.md)\>

#### Parameters

##### payload

`TCreatePayload`

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

> **apiDuplicate**: (`id`, `overrides`, `options?`) => `Promise`\<[`GanttCurriculumDocument`](../type-aliases/GanttCurriculumDocument.md)\>

Server-side deep clone of a curriculum into a fully independent copy (#319,
#322). Returns the freshly created curriculum.

#### Parameters

##### id

`string`

##### overrides?

[`DuplicateCurriculumOverrides`](../type-aliases/DuplicateCurriculumOverrides.md) = `{}`

##### options?

[`ClientApiProps`](../../../common/type-aliases/ClientApiProps.md)

#### Returns

`Promise`\<[`GanttCurriculumDocument`](../type-aliases/GanttCurriculumDocument.md)\>

### apiExport

> **apiExport**: (`id`, `options?`) => `Promise`\<[`GanttCurriculumExport`](../type-aliases/GanttCurriculumExport.md)\>

#### Parameters

##### id

`string`

##### options?

[`ClientApiProps`](../../../common/type-aliases/ClientApiProps.md)

#### Returns

`Promise`\<[`GanttCurriculumExport`](../type-aliases/GanttCurriculumExport.md)\>

### apiGet

> `readonly` **apiGet**: (`id`, `options?`) => `Promise`\<[`ApiCurriculum`](../../../../api-shared/types/gantt/api-layer/type-aliases/ApiCurriculum.md)\>

#### Parameters

##### id

`string`

##### options?

[`ClientApiProps`](../../../common/type-aliases/ClientApiProps.md)

#### Returns

`Promise`\<[`ApiCurriculum`](../../../../api-shared/types/gantt/api-layer/type-aliases/ApiCurriculum.md)\>

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

### apiImport

> **apiImport**: (`payload`, `options?`) => `Promise`\<[`GanttCurriculumDocument`](../type-aliases/GanttCurriculumDocument.md)\>

#### Parameters

##### payload

`unknown`

##### options?

[`ClientApiProps`](../../../common/type-aliases/ClientApiProps.md)

#### Returns

`Promise`\<[`GanttCurriculumDocument`](../type-aliases/GanttCurriculumDocument.md)\>

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

> `readonly` **apiListWithParents**: (`options?`) => `Promise`\<`Record`\<`string`, [`ListEntryWithParent`](../../base/type-aliases/ListEntryWithParent.md)\<[`GanttCurriculum`](../../../../api-shared/types/gantt/models/curriculum/type-aliases/GanttCurriculum.md)\>\>\>

Same listing as `apiList`, but each value carries the parent id. Use
when you need child → parent without fetching each item. See #310.

#### Parameters

##### options?

[`ClientApiProps`](../../../common/type-aliases/ClientApiProps.md)

#### Returns

`Promise`\<`Record`\<`string`, [`ListEntryWithParent`](../../base/type-aliases/ListEntryWithParent.md)\<[`GanttCurriculum`](../../../../api-shared/types/gantt/models/curriculum/type-aliases/GanttCurriculum.md)\>\>\>

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

`Partial`\<[`GanttCurriculum`](../../../../api-shared/types/gantt/models/curriculum/type-aliases/GanttCurriculum.md)\> & `object`

##### options?

[`ClientApiProps`](../../../common/type-aliases/ClientApiProps.md)

#### Returns

`Promise`\<`object` & [`BaseGantItem`](../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`BaseDocument`](../../base/type-aliases/BaseDocument.md)\>
