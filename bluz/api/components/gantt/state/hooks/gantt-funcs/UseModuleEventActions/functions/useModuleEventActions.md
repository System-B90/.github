[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/gantt/state/hooks/gantt-funcs/UseModuleEventActions](../index.md) / useModuleEventActions

# Function: useModuleEventActions()

> **useModuleEventActions**(): `object`

Defined in: [ui/src/components/gantt/state/hooks/gantt-funcs/UseModuleEventActions.tsx:21](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/components/gantt/state/hooks/gantt-funcs/UseModuleEventActions.tsx#L21)

## Returns

`object`

### allocateTimeToModuleEvent

> `readonly` **allocateTimeToModuleEvent**: (`id`, `curriculumId`, `allocatedDuration`) => `Promise`\<`void`\> = `actions.allocateTime`

#### Parameters

##### id

`string`

##### curriculumId

`string`

##### allocatedDuration

`number`

#### Returns

`Promise`\<`void`\>

### createEvent

> **createEvent**: (`title`, `moduleId`, `type`, `minimumDuration`, `allocatedDuration`, `hiveSubjectId`, `hiveModuleId`, `hiveLessonId`) => `Promise`\<`object` & [`BaseGantItem`](../../../../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`BaseDocument`](../../../../../../../api-client/gantt/base/type-aliases/BaseDocument.md)\>

#### Parameters

##### title

`string`

##### moduleId

`string`

##### type?

[`ModuleEventType`](../../../../../../../api-shared/types/gantt/models/event/enumerations/ModuleEventType.md) = `ModuleEventType.Lecture`

##### minimumDuration?

`number` = `0`

##### allocatedDuration?

`number` = `0`

##### hiveSubjectId?

`number` \| `null`

##### hiveModuleId?

`number` \| `null`

##### hiveLessonId?

`number` \| `null`

#### Returns

`Promise`\<`object` & [`BaseGantItem`](../../../../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`BaseDocument`](../../../../../../../api-client/gantt/base/type-aliases/BaseDocument.md)\>

### deleteEvent

> `readonly` **deleteEvent**: (`containerId`, `id`) => `Promise`\<`void`\> = `actions.remove`

#### Parameters

##### containerId

`string`

##### id

`string`

#### Returns

`Promise`\<`void`\>

### duplicateEvent

> **duplicateEvent**: (`eventId`, `moduleId`) => `Promise`\<[`ModuleEventDocument`](../../../../../../../api-client/gantt/module-event/type-aliases/ModuleEventDocument.md)\>

#### Parameters

##### eventId

`string`

##### moduleId

`string`

#### Returns

`Promise`\<[`ModuleEventDocument`](../../../../../../../api-client/gantt/module-event/type-aliases/ModuleEventDocument.md)\>

### linkEventToModule

> `readonly` **linkEventToModule**: (`containerId`, `id`) => `Promise`\<`object` & [`BaseGantItem`](../../../../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`BaseDocument`](../../../../../../../api-client/gantt/base/type-aliases/BaseDocument.md)\> = `actions.link`

#### Parameters

##### containerId

`string`

##### id

`string`

#### Returns

`Promise`\<`object` & [`BaseGantItem`](../../../../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`BaseDocument`](../../../../../../../api-client/gantt/base/type-aliases/BaseDocument.md)\>

### moveEvent

> **moveEvent**: (`eventId`, `fromModuleId`, `toModuleId`) => `Promise`\<`void`\>

#### Parameters

##### eventId

`string`

##### fromModuleId

`string`

##### toModuleId

`string`

#### Returns

`Promise`\<`void`\>

### unlinkEventFromModule

> `readonly` **unlinkEventFromModule**: (`containerId`, `id`) => `Promise`\<`void`\> = `actions.unlink`

#### Parameters

##### containerId

`string`

##### id

`string`

#### Returns

`Promise`\<`void`\>

### updateEvent

> `readonly` **updateEvent**: (`id`, `updates`) => `Promise`\<`object` & [`BaseGantItem`](../../../../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`BaseDocument`](../../../../../../../api-client/gantt/base/type-aliases/BaseDocument.md)\> = `actions.update`

#### Parameters

##### id

`string`

##### updates

`Partial`\<`TEntity`\>

#### Returns

`Promise`\<`object` & [`BaseGantItem`](../../../../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`BaseDocument`](../../../../../../../api-client/gantt/base/type-aliases/BaseDocument.md)\>
