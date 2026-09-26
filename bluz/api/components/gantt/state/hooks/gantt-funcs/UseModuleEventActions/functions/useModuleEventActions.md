[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/gantt/state/hooks/gantt-funcs/UseModuleEventActions](../index.md) / useModuleEventActions

# Function: useModuleEventActions()

> **useModuleEventActions**(): `object`

Defined in: [ui/src/components/gantt/state/hooks/gantt-funcs/UseModuleEventActions.tsx:22](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/state/hooks/gantt-funcs/UseModuleEventActions.tsx#L22)

## Returns

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

### applyEventShuffleGroup

> **applyEventShuffleGroup**: (`eventId`, `moduleId`, `shuffles`) => `Promise`\<[`ModuleEventDocument`](../../../../../../../api-client/gantt/module-event/type-aliases/ModuleEventDocument.md)[]\>

Makes the event's shuffle group cover exactly `shuffles`: one sibling
event per shuffle, so the same lesson can sit at a different time for
each of them (#699). Fewer than two shuffles ungroups the event.

#### Parameters

##### eventId

`string`

##### moduleId

`string`

##### shuffles

`string`[]

#### Returns

`Promise`\<[`ModuleEventDocument`](../../../../../../../api-client/gantt/module-event/type-aliases/ModuleEventDocument.md)[]\>

### createEvent

> **createEvent**: (`title`, `moduleId`, `type`, `minimumDuration`, `allocatedDuration`, `hiveSubjectId`, `hiveModuleId`, `hiveLessonId`, `orchestratorId`) => `Promise`\<`object` & [`BaseGantItem`](../../../../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md) & [`BaseDocument`](../../../../../../../api-client/gantt/base/type-aliases/BaseDocument.md)\>

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

##### orchestratorId?

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
