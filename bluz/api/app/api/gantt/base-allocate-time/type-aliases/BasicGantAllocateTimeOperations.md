[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [app/api/gantt/base-allocate-time](../index.md) / BasicGantAllocateTimeOperations

# Type Alias: BasicGantAllocateTimeOperations\<_TEntity\>

> **BasicGantAllocateTimeOperations**\<`_TEntity`\> = `object`

Defined in: [ui/src/app/api/gantt/base-allocate-time.ts:23](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/app/api/gantt/base-allocate-time.ts#L23)

## Type Parameters

### _TEntity

`_TEntity` *extends* [`BaseGantItem`](../../../../../api-shared/types/gantt/models/shared/type-aliases/BaseGantItem.md)

## Properties

### getAllocatedTime

> **getAllocatedTime**: (`eventId`, `containerId`) => `Promise`\<`number`\>

Defined in: [ui/src/app/api/gantt/base-allocate-time.ts:24](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/app/api/gantt/base-allocate-time.ts#L24)

#### Parameters

##### eventId

[`GanttEventId`](../../../../../api-shared/types/gantt/models/shared/type-aliases/GanttEventId.md)

##### containerId

[`GanttCurriculumId`](../../../../../api-shared/types/gantt/models/curriculum/type-aliases/GanttCurriculumId.md)

#### Returns

`Promise`\<`number`\>

***

### setAllocatedTime

> **setAllocatedTime**: (`eventId`, `containerId`, `duration`) => `Promise`\<`void`\>

Defined in: [ui/src/app/api/gantt/base-allocate-time.ts:28](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/app/api/gantt/base-allocate-time.ts#L28)

#### Parameters

##### eventId

[`GanttEventId`](../../../../../api-shared/types/gantt/models/shared/type-aliases/GanttEventId.md)

##### containerId

[`GanttCurriculumId`](../../../../../api-shared/types/gantt/models/curriculum/type-aliases/GanttCurriculumId.md)

##### duration

`number`

#### Returns

`Promise`\<`void`\>
