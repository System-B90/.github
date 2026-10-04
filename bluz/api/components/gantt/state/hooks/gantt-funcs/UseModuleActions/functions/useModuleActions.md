[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/gantt/state/hooks/gantt-funcs/UseModuleActions](../index.md) / useModuleActions

# Function: useModuleActions()

> **useModuleActions**(): `object`

Defined in: [ui/src/components/gantt/state/hooks/gantt-funcs/UseModuleActions.tsx:16](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/components/gantt/state/hooks/gantt-funcs/UseModuleActions.tsx#L16)

## Returns

`object`

### createModule

> **createModule**: (`title`, `syllabusId`, `description`, `hiveIds`) => `Promise`\<`object` & [`BaseGantItem`](../../../../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`BaseDocument`](../../../../../../../api-client/gantt/base/type-aliases/BaseDocument.md)\>

#### Parameters

##### title

`string`

##### syllabusId

`string`

##### description?

`string` = `""`

##### hiveIds?

`number`[] = `[]`

#### Returns

`Promise`\<`object` & [`BaseGantItem`](../../../../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`BaseDocument`](../../../../../../../api-client/gantt/base/type-aliases/BaseDocument.md)\>

### deleteModule

> `readonly` **deleteModule**: (`containerId`, `id`) => `Promise`\<`void`\> = `actions.remove`

#### Parameters

##### containerId

`string`

##### id

`string`

#### Returns

`Promise`\<`void`\>

### linkModuleToSyllabus

> `readonly` **linkModuleToSyllabus**: (`containerId`, `id`) => `Promise`\<`object` & [`BaseGantItem`](../../../../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`BaseDocument`](../../../../../../../api-client/gantt/base/type-aliases/BaseDocument.md)\> = `actions.link`

#### Parameters

##### containerId

`string`

##### id

`string`

#### Returns

`Promise`\<`object` & [`BaseGantItem`](../../../../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`BaseDocument`](../../../../../../../api-client/gantt/base/type-aliases/BaseDocument.md)\>

### unlinkModuleToSyllabus

> `readonly` **unlinkModuleToSyllabus**: (`containerId`, `id`) => `Promise`\<`void`\> = `actions.unlink`

#### Parameters

##### containerId

`string`

##### id

`string`

#### Returns

`Promise`\<`void`\>

### updateModule

> `readonly` **updateModule**: (`id`, `updates`) => `Promise`\<`object` & [`BaseGantItem`](../../../../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`BaseDocument`](../../../../../../../api-client/gantt/base/type-aliases/BaseDocument.md)\> = `actions.update`

#### Parameters

##### id

`string`

##### updates

`Partial`\<`TEntity`\>

#### Returns

`Promise`\<`object` & [`BaseGantItem`](../../../../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`BaseDocument`](../../../../../../../api-client/gantt/base/type-aliases/BaseDocument.md)\>
