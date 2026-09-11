[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/gantt/state/hooks/gantt-funcs/UseSyllabusActions](../index.md) / useSyllabusActions

# Function: useSyllabusActions()

> **useSyllabusActions**(): `object`

Defined in: [ui/src/components/gantt/state/hooks/gantt-funcs/UseSyllabusActions.tsx:19](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/state/hooks/gantt-funcs/UseSyllabusActions.tsx#L19)

## Returns

`object`

### createSyllabus

> **createSyllabus**: (`title`, `curriculumId`, `hiveIds`) => `Promise`\<`object` & [`BaseGantItem`](../../../../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`BaseDocument`](../../../../../../../api-client/gantt/base/type-aliases/BaseDocument.md)\>

#### Parameters

##### title

`string`

##### curriculumId

`string`

##### hiveIds?

`number`[] = `[]`

#### Returns

`Promise`\<`object` & [`BaseGantItem`](../../../../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`BaseDocument`](../../../../../../../api-client/gantt/base/type-aliases/BaseDocument.md)\>

### deleteSyllabus

> `readonly` **deleteSyllabus**: (`containerId`, `id`) => `Promise`\<`void`\> = `actions.remove`

#### Parameters

##### containerId

`string`

##### id

`string`

#### Returns

`Promise`\<`void`\>

### linkSyllabusToCurriculum

> **linkSyllabusToCurriculum**: (`curriculumId`, `syllabusId`) => `Promise`\<[`ApiSyllabus`](../../../../../../../api-shared/types/gantt/api-layer/type-aliases/ApiSyllabus.md)\>

#### Parameters

##### curriculumId

`string`

##### syllabusId

`string`

#### Returns

`Promise`\<[`ApiSyllabus`](../../../../../../../api-shared/types/gantt/api-layer/type-aliases/ApiSyllabus.md)\>

### unlinkSyllabusFromCurriculum

> `readonly` **unlinkSyllabusFromCurriculum**: (`containerId`, `id`) => `Promise`\<`void`\> = `actions.unlink`

#### Parameters

##### containerId

`string`

##### id

`string`

#### Returns

`Promise`\<`void`\>

### updateSyllabus

> `readonly` **updateSyllabus**: (`id`, `updates`) => `Promise`\<`object` & [`BaseGantItem`](../../../../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`BaseDocument`](../../../../../../../api-client/gantt/base/type-aliases/BaseDocument.md)\> = `actions.update`

#### Parameters

##### id

`string`

##### updates

`Partial`\<`TEntity`\>

#### Returns

`Promise`\<`object` & [`BaseGantItem`](../../../../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`BaseDocument`](../../../../../../../api-client/gantt/base/type-aliases/BaseDocument.md)\>
